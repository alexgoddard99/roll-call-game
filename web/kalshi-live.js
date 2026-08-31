/* Kalshi sponsor integration (presented-by partner units).

   Shape (the "E6 / stamp" treatment): "Presented by Kalshi" ticker under the
   masthead, a featured-market ledger with outcome rows + stamp buttons under
   the vote button on each bill and on the score page, and the midterms-hub CTA
   on the score page. The featured market rotates daily per kalshi-schedule.txt
   (one line per day: date, Kalshi event ticker, optional URL). Live prices come
   from /api/kalshi (web/_worker.js). Add ?kdate=YYYY-MM-DD to preview another
   day's market. */
(function () {
  "use strict";

  var app = document.getElementById("app");
  if (!app) return;

  var MIDTERMS_URL = "https://kalshi.com/category/elections/midterms";
  // Attribution tag for Kalshi's analytics, appended to every outbound link.
  function kUrl(u) { return u + (u.indexOf("?") > -1 ? "&" : "?") + "utm_source=yeaornay"; }
  var FINE_PRINT = "Sponsored by Kalshi. Prices reflect live trading on Kalshi, a " +
    "CFTC-regulated exchange, and are not predictions or investment advice.";
  var MAX_ROWS = 4;
  var SHORT = { "Democratic Party": "Democrats", "Republican Party": "Republicans" };
  var params = new URLSearchParams(location.search);
  var dateStr = /^\d{4}-\d{2}-\d{2}$/.test(params.get("kdate") || "") ? params.get("kdate")
    : new Intl.DateTimeFormat("en-CA", { timeZone: "America/New_York" }).format(new Date());

  var MARKET = null;

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function fmtMoney(n) {
    return n >= 1e6 ? "$" + (n / 1e6).toFixed(1) + "M" : n >= 1e3 ? "$" + Math.round(n / 1e3) + "K" : "$" + n;
  }
  function fmtDate(iso) {
    return new Date(iso).toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });
  }

  /* ---------- schedule ---------- */
  // kalshi-schedule.txt: "YYYY-MM-DD  EVENT-TICKER  [https://kalshi.com/...]  [| custom question]  # note"
  // Today's line wins; otherwise the most recent past line (so the unit never goes dark).
  function parseSchedule(text) {
    return text.split("\n")
      .map(function (l) { return l.replace(/#.*$/, "").trim(); })
      .filter(Boolean)
      .map(function (l) {
        var parts = l.split("|"), p = parts[0].trim().split(/\s+/);
        return { date: p[0], event: (p[1] || "").toUpperCase(), url: p[2] || "", label: (parts[1] || "").trim() };
      })
      .filter(function (r) { return /^\d{4}-\d{2}-\d{2}$/.test(r.date) && /^[A-Z0-9-]+$/.test(r.event); })
      .sort(function (a, b) { return a.date < b.date ? -1 : a.date > b.date ? 1 : 0; });
  }
  function pickEntry(rows) {
    var past = rows.filter(function (r) { return r.date <= dateStr; });
    return past.length ? past[past.length - 1] : rows[0] || null;
  }
  function loadSchedule() {
    return fetch("kalshi-schedule.txt", { cache: "no-store" })
      .then(function (r) { if (!r.ok) throw new Error("schedule " + r.status); return r.text(); })
      .then(parseSchedule);
  }

  /* ---------- market data ---------- */
  function loadMarket(entry) {
    var key = "kalshi-market-" + entry.event;
    var cached = null;
    try { cached = JSON.parse(localStorage.getItem(key)); } catch (e) {}
    return fetch("/api/kalshi?event=" + encodeURIComponent(entry.event), { cache: "no-store" })
      .then(function (r) { if (!r.ok) throw new Error("proxy " + r.status); return r.json(); })
      .then(function (d) {
        if (!d.markets || !d.markets.length) throw new Error("no markets");
        try { localStorage.setItem(key, JSON.stringify(d)); } catch (e) {}
        return d;
      })
      .catch(function (e) {
        console.warn("Kalshi proxy unavailable for " + entry.event, e);
        if (cached) return cached;
        return fetch("kalshi-snapshot.json").then(function (r) { return r.json(); })
          .then(function (d) { if (d.event.ticker !== entry.event) throw e; return d; });
      });
  }

  function buildMarket(d, entry) {
    var live = d.markets.filter(function (m) { return m.status === "active" || m.status === "open"; });
    var ms = (live.length ? live : d.markets).slice().sort(function (a, b) { return b.last - a.last; });
    var volume = d.markets.reduce(function (a, m) { return a + (m.volume || 0); }, 0);
    var title = (d.event.title || "").trim(), sub = (d.event.sub_title || "").trim();
    // Kalshi titles read like "Michigan Senate winner?" + "In 2026"; make them a sentence.
    var question, year = (sub.match(/\b(20\d\d)\b/) || [])[1], race = title.match(/^(.+?)\s+winner\??(?:\s*\(.*\))?$/i);
    if (entry.label) question = entry.label;
    else if (race && year) question = "Who will win the " + year + " " + race[1].replace(/\s*\(person\)/i, "") + " race?";
    else if (sub && /\?$/.test(title) && /^in /i.test(sub)) question = title.replace(/\?$/, "") + " " + sub.replace(/^In /, "in ") + "?";
    else if (sub && !/\?$/.test(title)) question = title + " " + sub + (/\?$/.test(sub) ? "" : "?");
    else question = title;
    MARKET = {
      event: d.event.ticker,
      question: question,
      url: kUrl(entry.url || d.event.url || "https://kalshi.com/markets/" + (d.event.series || "").toLowerCase()),
      volume: fmtMoney(volume) + " traded",
      settles: "settles " + fmtDate(ms[0].close_time),
      outcomes: ms.slice(0, MAX_ROWS).map(function (m) {
        return { name: SHORT[m.name] || m.name, pct: m.last, delta: m.last - m.prev };
      }),
      more: Math.max(0, ms.length - MAX_ROWS),
      fetchedAt: d.fetched_at
    };
  }

  /* ---------- units ---------- */
  function attribution() {
    return '<div class="k-feat-head"><img class="k-logo" src="kalshi-logo.svg" alt="Kalshi">' +
      '<span class="k-sponsored">| Sponsored</span>' +
      '<span class="k-feat-info" title="Prices reflect live trading on Kalshi, a ' +
        'CFTC-regulated prediction market. Not investment advice.">i</span></div>';
  }

  function unitLedger() {
    var rows = MARKET.outcomes.map(function (o) {
      var deltaHtml = o.delta ? '<span class="k-row-delta ' + (o.delta > 0 ? "up" : "down") + '">' +
        (o.delta > 0 ? "&#9650;" : "&#9660;") + Math.abs(o.delta) + '</span>' : "";
      return '<div class="k-row">' +
        '<span class="k-row-name">' + esc(o.name) + '</span>' +
        '<span class="k-row-chance">' + o.pct + '%' + deltaHtml + '</span>' +
        '<a class="k-row-stamp" data-k="row" data-outcome="' + esc(o.name) + '" href="' + esc(MARKET.url) + '" target="_blank" rel="noopener sponsored">' +
          'Yes &middot; ' + o.pct + '%</a>' +
      '</div>';
    }).join("");
    var more = MARKET.more ? '<a class="k-led-more" data-k="more" href="' + esc(MARKET.url) + '" target="_blank" rel="noopener sponsored">' +
      '+' + MARKET.more + ' more on Kalshi &rarr;</a>' : "";
    return '<div class="kalshi-unit k-ledger">' +
      '<div class="k-led-left">' + attribution() +
        '<a class="k-led-q" data-k="question" href="' + esc(MARKET.url) + '" target="_blank" rel="noopener sponsored">' +
          esc(MARKET.question) + '</a>' +
        '<a class="k-led-cta" data-k="odds_cta" href="' + esc(MARKET.url) + '" target="_blank" rel="noopener sponsored">' +
          'See the live odds on Kalshi &rarr;</a></div>' +
      '<div class="k-led-right">' + rows + more +
        '<div class="k-led-vol">' + esc(MARKET.volume.replace(" traded", "")) +
          ' traded &middot; ' + esc(MARKET.settles) + '</div></div>' +
      '<p class="k-fine">' + esc(FINE_PRINT) + '</p>' +
    '</div>';
  }

  function unitCTA() {
    return '<div class="kalshi-unit k-midterms">' +
      '<div class="k-sponsored-tag">Sponsored &middot; Kalshi</div>' +
      '<p class="k-mid-q">Who will be a part of the 120th Congress?</p>' +
      '<div class="k-cta"><a data-k="midterms_cta" href="' + kUrl(MIDTERMS_URL) + '" target="_blank" rel="noopener sponsored">' +
        'Check out the odds on Kalshi &rarr;</a></div>' +
    '</div>';
  }

  function injectTicker() {
    if (document.querySelector(".kalshi-ticker")) return;
    var head = document.querySelector(".masthead");
    if (!head) return;
    var t = document.createElement("div");
    t.className = "kalshi-ticker";
    t.innerHTML = '<span class="grp"><span class="k-sponsored">Sponsored</span>' +
        '<span class="bar">|</span>Presented by ' +
        '<img class="k-logo" src="kalshi-logo.svg" alt="Kalshi">' +
        '<span class="bar">|</span>Today&rsquo;s Market:</span>' +
      '<a class="q" data-k="ticker" href="' + esc(MARKET.url) + '" target="_blank" rel="noopener sponsored">' +
        esc(MARKET.question) + '</a>';
    head.appendChild(t);
  }

  /* ---------- injection ---------- */
  function injectUnits() {
    if (!MARKET) return;
    var screen = app.querySelector(".screen");
    if (!screen || screen.querySelector(".kalshi-unit")) return;
    var onSummary = !!screen.querySelector(".summary-score");
    var onBill = !!screen.querySelector(".docket") && !onSummary;
    if (onBill) {
      var act = screen.querySelector(".live-count") || screen.querySelector(".action-row");
      if (act) act.insertAdjacentHTML("afterend", unitLedger());
    }
    if (onSummary) {
      var anchor = screen.querySelector(".share-row") || screen.querySelector(".action-row");
      var html = unitLedger() + unitCTA();
      if (anchor) anchor.insertAdjacentHTML("beforebegin", html);
      else screen.insertAdjacentHTML("beforeend", html);
    }
  }
  function refreshUnits() {
    app.querySelectorAll(".kalshi-unit").forEach(function (u) { u.remove(); });
    injectUnits();
  }

  new MutationObserver(injectUnits).observe(app, { childList: true });

  /* ---------- analytics: GA4 "kalshi_click" on any outbound Kalshi link ---------- */
  function currentScreen() {
    if (app.querySelector(".summary-score")) return "score";
    if (app.querySelector(".docket")) return "vote";
    return "cover";
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[data-k]");
    if (!a || !/kalshi\.com/.test(a.href)) return;
    var c = window.YonCloud;
    if (!c || !c.enabled) return;
    var params = {
      placement: a.dataset.k,
      screen: currentScreen(),
      event_ticker: MARKET ? MARKET.event : "",
      link_url: a.href
    };
    if (a.dataset.outcome) params.outcome = a.dataset.outcome;
    if (window.COURT_DATA) params.game = "court";
    c.logEvent("kalshi_click", params);
  });

  loadSchedule().then(function (rows) {
    var entry = pickEntry(rows);
    if (!entry) throw new Error("schedule is empty");
    return loadMarket(entry).then(function (d) { buildMarket(d, entry); });
  }).then(function () {
    injectTicker();
    refreshUnits();
  }).catch(function (e) {
    console.error("Kalshi integration: no market to show", e);
  });
})();
