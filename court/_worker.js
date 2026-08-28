/* Split Decision — Pages worker (advanced mode).

   The featured-market schedule is shared with the senate site: this worker
   serves /kalshi-schedule.txt by fetching it from KALSHI_SCHEDULE_URL
   (default https://playyeaornay.com/kalshi-schedule.txt, cached 5 minutes),
   so there is exactly one file to edit — web/kalshi-schedule.txt in the repo.

   Proxies Kalshi's public market-data API for the sponsor prototype: those
   endpoints need no API key, but Kalshi's edge returns 403 to any request that
   carries a browser Origin header, so the page can't call them directly.
   Kalshi rate-limits unauthenticated calls from Cloudflare's shared egress IPs
   (429), so when the Pages secrets KALSHI_KEY_ID and KALSHI_PRIVATE_KEY (PKCS#8
   PEM) are present, requests are signed per Kalshi's API-key scheme:
   RSA-PSS/SHA-256 over `${timestamp_ms}${METHOD}${path-without-query}`.
   Only event tickers listed in kalshi-schedule.txt are proxied, so the signed
   key's rate budget can't be spent on arbitrary lookups.
   Everything except /api/kalshi is served as a normal static asset. */

const KALSHI = "https://api.elections.kalshi.com/trade-api/v2";
const DEFAULT_SCHEDULE_URL = "https://playyeaornay.com/kalshi-schedule.txt";
const CACHE_SECONDS = 120;
const EVENT_RE = /^[A-Z0-9]{2,24}-[A-Z0-9]{2,24}$/;

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (url.pathname === "/api/kalshi") return kalshi(url, env, ctx, request);
    if (url.pathname === "/kalshi-schedule.txt") return scheduleResponse(env);
    return env.ASSETS.fetch(request);
  },
};

// ---- Kalshi API-key signing (WebCrypto) ----
let signingKey = null;
async function importKey(pem) {
  const b64 = pem.replace(/-----[A-Z ]+-----/g, "").replace(/\s+/g, "");
  const der = Uint8Array.from(atob(b64), (c) => c.charCodeAt(0));
  return crypto.subtle.importKey("pkcs8", der, { name: "RSA-PSS", hash: "SHA-256" }, false, ["sign"]);
}
async function authHeaders(env, method, path) {
  if (!env.KALSHI_KEY_ID || !env.KALSHI_PRIVATE_KEY) return {};
  if (!signingKey) signingKey = await importKey(env.KALSHI_PRIVATE_KEY);
  const ts = String(Date.now());
  const msg = new TextEncoder().encode(ts + method + path);
  const sig = await crypto.subtle.sign({ name: "RSA-PSS", saltLength: 32 }, signingKey, msg);
  return {
    "KALSHI-ACCESS-KEY": env.KALSHI_KEY_ID,
    "KALSHI-ACCESS-TIMESTAMP": ts,
    "KALSHI-ACCESS-SIGNATURE": btoa(String.fromCharCode(...new Uint8Array(sig))),
  };
}

function json(body, status, extra) {
  return new Response(JSON.stringify(body), {
    status: status || 200,
    headers: Object.assign({
      "content-type": "application/json; charset=utf-8",
      "access-control-allow-origin": "*",
    }, extra || {}),
  });
}

async function get(env, path) {
  const signedPath = "/trade-api/v2" + path.split("?")[0];
  const r = await fetch(KALSHI + path, {
    headers: Object.assign({ accept: "application/json", "user-agent": "yea-or-nay-dev-proto/1.0" },
                           await authHeaders(env, "GET", signedPath)),
  });
  if (!r.ok) throw new Error("kalshi " + r.status + " for " + path);
  return r.json();
}

const pct = (dollars) => Math.round(parseFloat(dollars) * 100);

// Shared schedule text, fetched from the senate site and cached 5 minutes.
let sched = { at: 0, text: "" };
async function scheduleText(env) {
  if (sched.text && Date.now() - sched.at < 300000) return sched.text;
  try {
    const r = await fetch(env.KALSHI_SCHEDULE_URL || DEFAULT_SCHEDULE_URL,
                          { headers: { "user-agent": "split-decision-worker/1.0" } });
    if (r.ok) sched = { at: Date.now(), text: await r.text() };
  } catch (e) { /* keep whatever we had */ }
  return sched.text;
}
async function scheduleResponse(env) {
  return new Response(await scheduleText(env), {
    headers: { "content-type": "text/plain; charset=utf-8", "cache-control": "public, max-age=300" },
  });
}
// Allowed event tickers = those in the shared schedule.
async function allowedEvents(env, request) {
  const set = new Set();
  (await scheduleText(env)).split("\n").forEach((l) => {
    const p = l.replace(/#.*$/, "").split("|")[0].trim().split(/\s+/);
    if (/^\d{4}-\d{2}-\d{2}$/.test(p[0]) && p[1]) set.add(p[1].toUpperCase());
  });
  return set;
}

async function kalshi(url, env, ctx, request) {
  const event = (url.searchParams.get("event") || "").toUpperCase();
  const days = Math.min(365, Math.max(7, parseInt(url.searchParams.get("days"), 10) || 90));
  const wantHistory = url.searchParams.get("history") === "1";
  if (!EVENT_RE.test(event)) return json({ error: "bad event ticker" }, 400);
  if (!(await allowedEvents(env, request)).has(event)) return json({ error: "event not scheduled" }, 404);

  const cache = caches.default;
  const cacheKey = new Request("https://kalshi-proxy.invalid/" + event + "/" + days + "/" + (wantHistory ? "h" : "n"));
  const hit = await cache.match(cacheKey);
  if (hit) return hit;

  try {
    const ev = await get(env, "/events/" + event);
    const series = ev.event.series_ticker;
    let seriesTitle = "";
    try { seriesTitle = (await get(env, "/series/" + series)).series.title || ""; } catch (e) { /* optional */ }
    const slug = seriesTitle.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
    const eventUrl = "https://kalshi.com/markets/" + series.toLowerCase() + "/" + (slug || "market") + "/" + event.toLowerCase();
    const now = Math.floor(Date.now() / 1000);
    const start = now - days * 86400;
    const markets = await Promise.all((ev.markets || []).map(async (m) => {
      let history = [];
      if (wantHistory) try {
        const c = await get(env, "/series/" + series + "/markets/" + m.ticker +
          "/candlesticks?start_ts=" + start + "&end_ts=" + now + "&period_interval=1440");
        history = (c.candlesticks || []).map((k) => ({ t: k.end_period_ts, p: pct(k.price.close_dollars) }));
      } catch (e) { /* chart is optional */ }
      return {
        ticker: m.ticker,
        title: m.title,
        name: m.yes_sub_title || m.title,
        status: m.status,
        last: pct(m.last_price_dollars),
        prev: pct(m.previous_price_dollars),
        bid: pct(m.yes_bid_dollars),
        ask: pct(m.yes_ask_dollars),
        volume: Math.round(parseFloat(m.volume_fp) || 0),
        volume_24h: Math.round(parseFloat(m.volume_24h_fp) || 0),
        open_interest: Math.round(parseFloat(m.open_interest_fp) || 0),
        close_time: m.close_time,
        history,
      };
    }));
    const body = {
      event: { ticker: ev.event.event_ticker, series, series_title: seriesTitle, title: ev.event.title,
               sub_title: ev.event.sub_title, category: ev.event.category, url: eventUrl },
      fetched_at: new Date().toISOString(),
      signed: !!(env.KALSHI_KEY_ID && env.KALSHI_PRIVATE_KEY),
      markets,
    };
    const res = json(body, 200, { "cache-control": "public, max-age=" + CACHE_SECONDS });
    ctx.waitUntil(cache.put(cacheKey, res.clone()));
    return res;
  } catch (e) {
    return json({ error: String(e && e.message || e) }, 502,
                { "cache-control": "no-store" });
  }
}
