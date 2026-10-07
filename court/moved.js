/* The old address of a game now lives at politicaltrivia.com — SOURCE OF TRUTH for the
   copies in congress_game/web/moved.js, congress_game/court/moved.js and
   pollster/functions/moved.js (keep them identical; only the CONFIG in each caller differs).

   moved(request, cfg) returns a Response when the request is for a retired address,
   or null to let the site serve as before (dev previews and other hosts are untouched).

     cfg.hosts        the retired hostnames, exactly (never a dev preview)
     cfg.to           where the game lives now, no trailing slash, e.g. "https://politicaltrivia.com/yeaornay"
     cfg.handoffUntil YYYY-MM-DD (US Eastern). Before it, the game page itself is served as a
                      HANDOFF page: it carries the player's local record across in the URL
                      fragment (never sent to a server) and tells crawlers the move is
                      permanent (canonical + instant refresh). From that day, and for every
                      other path from day one, a plain 301, page for page — which is what
                      moves search authority. Nothing to redeploy on the day.
     cfg.keys         RegExp source: the localStorage keys the handoff carries
     cfg.name         the game's name, for the handoff page

   ?moved-preview on a dev host shows the handoff page for testing. */

export function moved(request, cfg) {
  const url = new URL(request.url);
  const preview = url.searchParams.has("moved-preview");
  if (!cfg.hosts.includes(url.hostname) && !preview) return null;
  const path = url.pathname === "/index.html" ? "/" : url.pathname;
  url.searchParams.delete("moved-preview");
  const target = cfg.to + path + (url.searchParams.toString() ? "?" + url.searchParams.toString() : "");
  const today = new Intl.DateTimeFormat("en-CA", { timeZone: "America/New_York" }).format(new Date());
  const wantsPage = request.method === "GET" && /text\/html/.test(request.headers.get("accept") || "");
  if (path === "/" && wantsPage && (today < cfg.handoffUntil || preview)) {
    return new Response(handoffPage(cfg, target), {
      headers: { "content-type": "text/html; charset=utf-8", "cache-control": "no-store" },
    });
  }
  return new Response(null, { status: 301, headers: { location: target, "cache-control": "public, max-age=86400" } });
}

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

function handoffPage(cfg, target) {
  return `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(cfg.name)} has moved to politicaltrivia.com</title>
<link rel="canonical" href="${esc(target)}">
<noscript><meta http-equiv="refresh" content="0;url=${esc(target)}"></noscript>
<style>
  body { margin: 0; min-height: 100vh; display: grid; place-items: center; background: #e9eef3; color: #0f1419; font: 400 17px/1.5 "Helvetica Neue", Arial, sans-serif; }
  main { max-width: 34em; padding: 24px; text-align: center; }
  b { font-weight: 700; } a { color: #14233f; }
</style></head><body><main>
<p><b>${esc(cfg.name)}</b> is now part of <b>Political Trivia.</b></p>
<p>Taking you, and your record, to <a href="${esc(target)}">politicaltrivia.com</a>&hellip;</p>
</main>
<script>
(function () {
  var re = new RegExp(${JSON.stringify(cfg.keys)}), keys = {}, n = 0;
  try {
    for (var i = 0; i < localStorage.length; i++) {
      var k = localStorage.key(i);
      if (re.test(k)) { keys[k] = localStorage.getItem(k); n++; }
    }
  } catch (e) {}
  var to = ${JSON.stringify(target)};
  if (n) {
    var json = JSON.stringify({ v: 1, from: location.hostname, keys: keys });
    var b64 = btoa(unescape(encodeURIComponent(json))).replace(/\\+/g, "-").replace(/\\//g, "_").replace(/=+$/, "");
    if (b64.length < 200000) to += "#import=" + b64;
  }
  location.replace(to);
})();
</script></body></html>
`;
}
