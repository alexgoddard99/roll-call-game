/* The Court — daily Supreme Court vote guessing game (Yea or Nay sibling) */
(function () {
  "use strict";

  const DATA = window.COURT_DATA;
  if (!DATA) {
    document.getElementById("app").innerHTML =
      "<p style='text-align:center'>Couldn't load case data. Run <code>build_court/fetch_court.py</code> first.</p>";
    return;
  }

  const PUZZLES = DATA.puzzles;
  const app = document.getElementById("app");
  const TALLY_BONUS = 2;

  // ---------- daily selection (flips at midnight US Eastern) ----------
  const today = new Date();
  const dateStr = new Intl.DateTimeFormat("en-CA",
    { timeZone: "America/New_York" }).format(today);
  const dayNumber = Math.max(0, Math.round(
    (Date.parse(dateStr) - Date.parse(DATA.epoch)) / 86400000));

  const params = new URLSearchParams(location.search);
  const practiceIdx = params.has("p") ? parseInt(params.get("p"), 10) : null;
  const isPractice = practiceIdx !== null && !Number.isNaN(practiceIdx);

  const puzzleIdx = isPractice
    ? ((practiceIdx % PUZZLES.length) + PUZZLES.length) % PUZZLES.length
    : dayNumber % PUZZLES.length;
  const puzzle = PUZZLES[puzzleIdx];
  const puzzleNo = dayNumber + 1;
  const nJust = puzzle.justices.length;
  const maxScore = nJust + TALLY_BONUS;

  // ---------- crowd counters (shared per-day doc in Firestore, see firestore.rules) ----------
  // Dev previews share the Firebase project, so they write to a separate "-dev-" doc.
  const IS_DEV_HOST = /^(dev\.|localhost$|127\.)/.test(location.hostname)
                      || location.protocol === "file:";
  const DAILY_ID = "court" + (IS_DEV_HOST ? "-dev" : "") + "-" + dateStr;
  const MIN_CROWD = 10;      // other players needed before comparisons show
  const RARE_PCT = 35;       // a correct call fewer than this % got is highlighted
  const STREAK_CAP = 30;   // streak buckets t1..t30; 30 means 30+
  let crowdSubmit = null;    // this session's counter write (promise)
  let crowdCache = null;     // today's counters once fetched
  let crowdBeat = null;      // "beat X%" once computed (for analytics)
  const cloudReady = new Promise((res) => {
    if (window.YonCloud) res();
    else window.addEventListener("yon-cloud-ready", () => res(), { once: true });
  });

  document.getElementById("dateline-left").textContent = today
    .toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric",
                                   year: "numeric", timeZone: "America/New_York" })
    .toUpperCase();
  document.getElementById("dateline-right").textContent = isPractice
    ? "ARCHIVE EDITION" : "CASE № " + puzzleNo;

  // ---------- state ----------
  const storeKey = "court-" + dateStr;
  let state = { guesses: {}, revealed: false };
  if (!isPractice) {
    try {
      const saved = JSON.parse(localStorage.getItem(storeKey));
      if (saved && saved.puzzleIdx === puzzleIdx) state = saved.state;
    } catch (e) { /* fresh */ }
  }
  function persist() {
    if (isPractice) return;
    try { localStorage.setItem(storeKey, JSON.stringify({ puzzleIdx, state })); } catch (e) {}
  }

  // ---------- helpers ----------
  const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
                      .replace(/"/g, "&quot;");

  const justiceScore = () => puzzle.justices.reduce(
    (a, j) => a + (state.guesses[j.key] === puzzle.votes[j.key] ? 1 : 0), 0);
  const actualYesCount = () => Object.values(puzzle.votes).filter((v) => v === "yes").length;
  const guessYesCount = () => puzzle.justices.reduce(
    (a, j) => a + (state.guesses[j.key] === "yes" ? 1 : 0), 0);
  const tallyHit = () => guessYesCount() === actualYesCount();
  const totalScore = () => justiceScore() + (tallyHit() ? TALLY_BONUS : 0);

  function guessSplit() {
    const y = guessYesCount(), n = nJust - y;
    return y >= n ? `${y}–${n} YES` : `${n}–${y} NO`;
  }

  function rank(score) {
    const pct = score / maxScore;
    if (pct === 1)    return ["Chief Justice", "You could write the opinion yourself."];
    if (pct >= 0.8) return ["Senior Associate Justice", "The conference respects your count."];
    if (pct >= 0.6) return ["Federal Appellate Judge", "Reversed less often than most."];
    if (pct >= 0.4) return ["Law Clerk", "Promising. Keep reading the slip opinions."];
    if (pct >= 0.2) return ["Second-Year Law Student", "Con Law is at 9 a.m. sharp."];
    return ["Held in Contempt", "The marshal will escort you out."];
  }

  function justiceCard(j) {
    return `<div class="senator-card">
      <div class="portrait-frame">
        <img src="${j.photo}" alt="Portrait of ${esc(j.name)}">
      </div>
      <div class="senator-name">${esc(j.name)}</div>
      <div class="senator-meta">Associate Justice</div>
      <div class="senator-blurb">${esc(j.blurb)}</div>
    </div>`;
  }

  // ---------- cloud / auth / analytics ----------
  function cloud(method, ...args) {
    const c = window.YonCloud;
    if (c && c.enabled && c[method]) return c[method](...args);
  }
  function track(name, extra) {
    cloud("logEvent", name, Object.assign({
      game: "court", puzzle_id: puzzle.id, puzzle_no: puzzleNo, era: puzzle.era,
      practice: isPractice ? 1 : 0,
    }, extra || {}));
  }
  let startTracked = false;
  // Synthetic page_view per screen, so GA4 Views reflect screens seen rather
  // than one hit per session. Views fired before the cloud layer loads are
  // queued and flushed on yon-cloud-ready.
  let lastPageview = null;
  const pageviewQueue = [];
  function pageview(path, title) {
    if (path === lastPageview) return; // same-screen re-render (e.g. reveal)
    lastPageview = path;
    const params = { game: "court", page_title: title, page_path: path,
                     page_location: location.origin + path };
    if (window.YonCloud) cloud("logEvent", "page_view", params);
    else pageviewQueue.push(params);
  }


  const ARCHIVE_KEY = "court-results";
  function loadArchive() {
    try { return JSON.parse(localStorage.getItem(ARCHIVE_KEY)) || {}; } catch (e) { return {}; }
  }
  function saveArchive(a) {
    try { localStorage.setItem(ARCHIVE_KEY, JSON.stringify(a)); } catch (e) {}
  }
  function recordResult() {
    if (isPractice) return;
    const archive = loadArchive();
    if (archive[dateStr]) return;
    archive[dateStr] = { puzzleId: puzzle.id, title: puzzle.caseTitle, era: puzzle.era,
                         score: totalScore(), max: maxScore, no: puzzleNo };
    saveArchive(archive);
    cloud("saveResult", dateStr, archive[dateStr]);
    submitCrowd(archive[dateStr].score);
    updateStreakChip();
  }

  // ---------- crowd comparison ----------
  // v0..v8 = the nine justices (in puzzle order), v9 = the split call
  function submitCrowd(score) {
    const keys = ["n", "s" + score];
    puzzle.justices.forEach((j, i) => {
      if (state.guesses[j.key] === puzzle.votes[j.key]) keys.push("v" + i);
    });
    if (tallyHit()) keys.push("v" + nJust);
    // today's streak (archive already includes today) joins the histogram
    keys.push("t" + Math.min(STREAK_CAP, Math.max(1, computeStats(loadArchive()).cur)));
    crowdSubmit = cloudReady.then(() => cloud("bumpDaily", DAILY_ID, keys)).catch(() => {});
  }
  async function fetchCrowd() {
    if (crowdCache) return crowdCache;
    await cloudReady;
    if (crowdSubmit) await crowdSubmit;
    try { crowdCache = (await cloud("fetchDaily", DAILY_ID)) || null; } catch (e) { crowdCache = null; }
    return crowdCache;
  }
  async function renderCrowd(score, max) {
    const d = await fetchCrowd();
    const line = document.getElementById("crowd-line");
    if (!d || !line) return; // no data, or the player already moved on
    const n = d.n || 0, others = Math.max(0, n - 1);
    if (others < MIN_CROWD) {
      line.innerHTML = `<span class="crowd-wait">Crowd comparison unlocks later today &mdash; check back</span>`;
      return;
    }
    let below = 0;
    for (let k = 0; k < score; k++) below += d["s" + k] || 0;
    const beat = Math.round(100 * below / others);
    crowdBeat = beat;
    const lead = score === max ? "Perfect &mdash; you beat" : beat === 0 ? "Everyone else today matched or beat you &mdash; you beat" : "You beat";
    line.innerHTML = `${lead} <strong>${beat}%</strong> of today&rsquo;s players`;
    app.querySelectorAll("td[data-cell]").forEach((td) => {
      const pct = Math.round(100 * (d["v" + td.dataset.cell] || 0) / n);
      const span = td.querySelector(".cell-pct");
      if (!span) return;
      span.textContent = pct + "%";
      if (td.classList.contains("hit") && pct < RARE_PCT) span.classList.add("rare");
    });
  }

  // ---------- streak banner (results screen) ----------
  const MILESTONES = {
    7: "A full week. The clerks have noticed.",
    14: "Two weeks straight. Seniority on the bench.",
    30: "A full month. You could write the opinion yourself.",
    50: "Fifty days. Your dissents are getting cited.",
    100: "One hundred days. Chief Justice material.",
    365: "A full year. A term for the history books.",
  };
  function streakBannerHTML() {
    const s = computeStats(loadArchive());
    const c = window.YonCloud;
    const signedIn = c && c.enabled && c.user();
    let main, sub;
    if (s.cur <= 1) {
      main = "Day 1";
      sub = s.best > 1 ? `A new streak starts here &mdash; your best is ${s.best}.`
                       : "Come back tomorrow to start a streak.";
    } else {
      main = `🔥 ${s.cur}-day streak`;
      sub = MILESTONES[s.cur]
         || (s.cur >= s.best ? "A personal best. Keep it going tomorrow."
                             : `Best: ${s.best}. Play tomorrow to keep it alive.`);
    }
    return `<div class="streak-banner">
      <div class="streak-main">${main}</div>
      <div class="streak-sub">${sub}</div>
      ${signedIn ? "" : `<div class="streak-save">Stored on this device &mdash;
        <a href="#" id="streak-signin">sign in with Google</a> to save your streak.</div>`}
    </div>`;
  }
  function bindStreakBanner() {
    const a = document.getElementById("streak-signin");
    if (!a) return;
    a.onclick = (e) => {
      e.preventDefault();
      track("streak_signin_prompt", {});
      const c = window.YonCloud;
      if (c && c.enabled)
        c.signIn().then(() => cloud("logEvent", "login", { method: "google" }))
                  .catch(() => {});
    };
  }
  // Re-render streak surfaces after anything that can change the archive or auth
  function refreshStreakUI() {
    updateStreakChip();
    const b = app.querySelector(".streak-banner");
    if (b) { b.outerHTML = streakBannerHTML(); bindStreakBanner(); }
  }

  // ---------- streak modal (chip click) ----------
  async function showStreakModal() {
    const s = computeStats(loadArchive());
    const cur = Math.max(1, s.cur);
    const overlay = document.createElement("div");
    overlay.className = "modal-overlay";
    overlay.innerHTML = `<div class="modal-card streak-card">
      <button class="modal-close" aria-label="Close">×</button>
      <div class="section-rule">Your Streak</div>
      <div class="streak-big">🔥 ${cur}</div>
      <div class="streak-big-label">${cur === 1 ? "day — today is day one" : "days running"}</div>
      <div class="streak-rank" id="streak-rank">Sizing up today&rsquo;s streaks&hellip;</div>
      <div class="stat-row streak-stat-row">
        <div class="stat"><div class="stat-num">${s.cur}</div><div class="stat-label">Current</div></div>
        <div class="stat"><div class="stat-num">${s.best}</div><div class="stat-label">Best</div></div>
        <div class="stat"><div class="stat-num">${s.played}</div><div class="stat-label">Played</div></div>
      </div>
      <p class="sync-note"><a href="#" id="streak-record">See my full record →</a></p>
    </div>`;
    document.body.appendChild(overlay);
    const close = () => overlay.remove();
    overlay.querySelector(".modal-close").onclick = close;
    overlay.onclick = (e) => { if (e.target === overlay) close(); };
    overlay.querySelector("#streak-record").onclick = (e) => { e.preventDefault(); close(); showStats(); };
    track("streak_open", { streak: s.cur });

    // percentile vs everyone with a live streak today (today's completions)
    const el = overlay.querySelector("#streak-rank");
    const d = await fetchCrowd().catch(() => null);
    if (!overlay.isConnected) return;
    let total = 0, below = 0;
    if (d) for (let k = 1; k <= STREAK_CAP; k++) {
      const c = d["t" + k] || 0;
      total += c;
      if (k < Math.min(cur, STREAK_CAP)) below += c;
    }
    const played = !isPractice && !!loadArchive()[dateStr];
    const others = played ? total - 1 : total; // don't compare yourself to yourself
    if (!d || others < MIN_CROWD) {
      el.innerHTML = `<span class="crowd-wait">Not enough streaks logged yet today &mdash; check back later</span>`;
      return;
    }
    const pct = Math.round(100 * below / others);
    el.innerHTML = `Longer than <strong>${pct}%</strong> of streaks alive right now`;
  }
  const streakChip = document.getElementById("streak-chip");
  function updateStreakChip() {
    if (!streakChip) return;
    // Always shown; a player with no streak yet sees "1-day streak" (today is day 1).
    const cur = Math.max(1, computeStats(loadArchive()).cur);
    streakChip.hidden = false;
    streakChip.innerHTML = `🔥 ${cur}<span class="long">-day streak</span>`;
  }
  if (streakChip) streakChip.onclick = () => showStreakModal();

  async function syncWithCloud() {
    const c = window.YonCloud;
    if (!c || !c.enabled || !c.user()) return;
    try {
      const remote = await c.fetchResults();
      const local = loadArchive();
      let changed = false;
      for (const [date, r] of Object.entries(remote))
        if (!local[date]) { local[date] = r; changed = true; }
      for (const [date, r] of Object.entries(local))
        if (!remote[date]) c.saveResult(date, r);
      if (changed) saveArchive(local);
      refreshStreakUI();
    } catch (e) { /* offline fine */ }
  }

  const authLink = document.getElementById("auth-link");
  window.addEventListener("yon-cloud-ready", () => {
    const c = window.YonCloud;
    if (!c.enabled) return;
    authLink.hidden = false;
    c.onUser((u) => {
      authLink.textContent = u ? "Sign Out (" + (u.displayName || "you").split(" ")[0] + ")" : "Sign In";
      if (u) syncWithCloud();
      refreshStreakUI();
    });
    authLink.onclick = () => {
      if (c.user()) { track("sign_out", {}); c.signOut(); }
      else c.signIn().then(() => cloud("logEvent", "login", { method: "google" })).catch(() => {});
    };
    track("page_open", {});
    pageviewQueue.splice(0).forEach((p) => cloud("logEvent", "page_view", p));
  });

  // ---------- screens ----------
  function showCover() {
    pageview("/cover", "Cover — " + puzzle.caseTitle);
    app.innerHTML = `<section class="screen">
      <div class="era-banner">${esc(puzzle.era)}</div>
      <h2 class="puzzle-title">${esc(puzzle.caseTitle)}</h2>
      <p class="puzzle-intro">${esc(puzzle.intro)}</p>
      <div class="section-rule">The Bench</div>
      <div class="bench-grid">${puzzle.justices.map(justiceCard).join("")}</div>
      <p class="whip-note">Read the case, then mark how each justice answered the question
        &mdash; and try to call the exact split.</p>
      <div class="action-row">
        <button class="btn-primary" id="go">Hear the Case &rarr;</button>
      </div>
    </section>`;
    document.getElementById("go").onclick = () => {
      track("open_docket", {});
      showCase();
    };
  }

  function showCase() {
    pageview("/case", "Case — " + puzzle.caseTitle);
    const revealed = state.revealed;
    const rows = puzzle.justices.map((j) => {
      const guess = state.guesses[j.key];
      let right;
      if (!revealed) {
        right = `<div class="stamp-pair">
          <button class="stamp ${guess === "yes" ? "stamped-yea" : guess ? "faded" : ""}"
                  data-j="${j.key}" data-vote="yes">YES</button>
          <button class="stamp ${guess === "no" ? "stamped-nay" : guess ? "faded" : ""}"
                  data-j="${j.key}" data-vote="no">NO</button>
        </div>`;
      } else {
        const actual = puzzle.votes[j.key];
        const hit = guess === actual;
        right = `<div class="stamp-pair">
          <span class="verdict ${hit ? "hit" : "miss"}">${hit ? "✓" : "✗"}</span>
          <span class="reveal-cell">
            <span class="reveal-label">Your call</span>
            <span class="your-call ${hit ? "" : "wrong"}">${guess === "yes" ? "YES" : "NO"}</span>
          </span>
          <span class="reveal-cell">
            <span class="reveal-label">Ruled</span>
            <span class="actual-stamp ${actual === "yes" ? "yea" : "nay"}">${actual.toUpperCase()}</span>
          </span>
        </div>`;
      }
      return `<div class="ballot-row">
        <img class="ballot-portrait" src="${j.photo}" alt="">
        <div class="ballot-id">
          <div class="senator-name">${esc(j.name)}</div>
          ${j.meta ? `<div class="senator-meta">${esc(j.meta)}</div>` : ""}
          <div class="ballot-blurb">${esc(j.blurb)}</div>
        </div>
        ${right}
      </div>`;
    }).join("");

    const held = revealed ? (() => {
      const ansWord = puzzle.answer.toUpperCase();
      const cls = puzzle.answer === "yes" ? "held-yes" : "held-no";
      const bonus = tallyHit();
      return `<div class="held-banner">
        <div class="held-line">The Court held: <span class="${cls}">${ansWord}</span>
          &middot; ${esc(puzzle.split)}</div>
        <div class="tally-bonus ${bonus ? "hit" : "miss"}">
          Your bench: ${guessSplit()} — ${bonus
            ? "exact split called, +" + TALLY_BONUS + " bonus"
            : "split missed, no bonus"}</div>
      </div>` })() : "";

    app.innerHTML = `<section class="screen${revealed ? "" : " has-count"}">
      <div class="docket">
        <div class="docket-eyebrow">In the Supreme Court &mdash; ${esc(puzzle.era)}</div>
        <h2 class="docket-title">${esc(puzzle.caseTitle)}</h2>
        <div class="docket-date">Decided ${esc(puzzle.decided)}</div>
        <p class="docket-desc">${esc(puzzle.desc)}</p>
        <div class="question-box">
          <div class="question-label">The question before the Court</div>
          <div class="question-text">${esc(puzzle.question)}</div>
        </div>
        <div class="ballot bench-ballot">${rows}</div>
        ${held}
      </div>
      <div class="action-row">
        <button class="btn-primary" id="advance" ${revealed ? "" : "disabled"}>
          ${revealed ? "See Your Score →" : "Hand Down the Decision"}</button>
      </div>
      ${revealed ? "" : `<div class="live-count" id="live-count"></div>`}
    </section>`;
    updateLiveCount();

    if (!revealed) {
      app.querySelectorAll(".stamp").forEach((b) => {
        b.onclick = () => {
          if (!startTracked) {
            startTracked = true;
            if (!Object.keys(state.guesses).length) track("puzzle_start", {});
          }
          state.guesses[b.dataset.j] = b.dataset.vote;
          persist();
          app.querySelectorAll(".stamp").forEach((s) => {
            const g = state.guesses[s.dataset.j];
            s.className = "stamp " + (g === s.dataset.vote
              ? (s.dataset.vote === "yes" ? "stamped-yea" : "stamped-nay") : g ? "faded" : "");
          });
          document.getElementById("advance").disabled =
            !puzzle.justices.every((j) => state.guesses[j.key]);
          updateLiveCount();
        };
      });
      document.getElementById("advance").disabled =
        !puzzle.justices.every((j) => state.guesses[j.key]);
    }
    document.getElementById("advance").onclick = () => {
      if (!state.revealed) {
        state.revealed = true;
        persist();
        recordResult();
        track("puzzle_complete", {
          score: totalScore(), max: maxScore,
          pct_correct: Math.round(100 * totalScore() / maxScore),
          justices_correct: justiceScore(), tally_called: tallyHit() ? 1 : 0,
          perfect: totalScore() === maxScore ? 1 : 0,
          rank: rank(totalScore())[0],
          streak: isPractice ? 0 : computeStats(loadArchive()).cur,
        });
        showCase();
        window.scrollTo({ top: 0, behavior: "smooth" });
      } else {
        showSummary();
      }
    };
  }

  function updateLiveCount() {
    const el = document.getElementById("live-count");
    if (!el) return;
    const yes = guessYesCount();
    const marked = puzzle.justices.filter((j) => state.guesses[j.key]).length;
    const no = marked - yes, left = nJust - marked;
    el.innerHTML = `<span class="lc-yes">${yes} yes</span>
      <span class="lc-sep">&middot;</span>
      <span class="lc-no">${no} no</span>
      <span class="lc-sep">&middot;</span>
      <span class="lc-left">${left ? left + " undecided" : "the bench is set"}</span>`;
  }

  function showSummary() {
    pageview("/score", "Score — " + puzzle.caseTitle);
    const score = totalScore();
    const [title, note] = rank(score);
    const cells = puzzle.justices.map((j, i) => {
      const hit = state.guesses[j.key] === puzzle.votes[j.key];
      return `<td class="${hit ? "hit" : "miss"}" data-cell="${i}">${hit ? "✓" : "✗"}${isPractice ? "" : `<span class="cell-pct"></span>`}</td>`;
    }).join("");
    app.innerHTML = `<section class="screen">
      <div class="era-banner">${esc(puzzle.era)} &mdash; ${esc(puzzle.caseTitle)}</div>
      <div class="summary-score">${score}<span class="of"> / ${maxScore}</span></div>
      <div class="summary-rank">&ldquo;${title}&rdquo;</div>
      <p class="summary-rank-note">${note}</p>
      ${isPractice ? `<p class="practice-note">Archive edition &mdash; played for practice,
        not counted in your record. A new case is argued daily.</p>`
        : `<div class="crowd-line" id="crowd-line"></div>${streakBannerHTML()}`}
      <table class="result-table">
        <tr>${puzzle.justices.map((j) =>
          `<th>${esc(j.name.split(" ").pop())}</th>`).join("")}<th>Split</th></tr>
        <tr>${cells}<td class="${tallyHit() ? "hit" : "miss"}" data-cell="${nJust}">${tallyHit() ? "✓" : "✗"}${isPractice ? "" : `<span class="cell-pct"></span>`}</td></tr>
      </table>
      <div class="share-row">
        <button class="btn-primary" id="share">Share Result</button>
        <button class="btn-ghost" id="review">Review the Votes</button>
        <button class="btn-ghost" id="practice">Play the Archive</button>
      </div>
      <div class="share-feedback" id="share-fb"></div>
    </section>`;
    if (!isPractice) { bindStreakBanner(); renderCrowd(score, maxScore); }

    document.getElementById("share").onclick = () => {
      const grid = puzzle.justices.map((j) =>
        state.guesses[j.key] === puzzle.votes[j.key] ? "\u{1F7E9}" : "\u{1F7E5}").join("");
      const cur = isPractice ? 0 : computeStats(loadArchive()).cur;
      const streakBit = cur >= 2 ? ` · 🔥 ${cur}-day streak` : "";
      const text = `Split Decision №${isPractice ? " (archive)" : puzzleNo} — a Yea or Nay game\n` +
        `${score}/${maxScore} · ${title}${streakBit}\n${grid} ⚖️ split ${tallyHit() ? "✓" : "✗"}`;
      const shareParams = { score, max: maxScore, streak: cur };
      if (crowdBeat !== null) shareParams.beat_pct = crowdBeat;
      track("share_result", shareParams);
      navigator.clipboard.writeText(text).then(() => {
        document.getElementById("share-fb").textContent = "COPIED TO CLIPBOARD";
      }).catch(() => {
        document.getElementById("share-fb").textContent = text;
      });
    };
    document.getElementById("review").onclick = () => { track("review_votes", {}); showCase(); };
    document.getElementById("practice").onclick = () => {
      track("archive_click", {});
      location.search = "?p=" + ((puzzleIdx + 1) % PUZZLES.length);
    };
  }

  // ---------- stats modal (same shape as the Senate game) ----------
  function computeStats(archive) {
    const dates = Object.keys(archive).sort();
    const n = dates.length;
    const total = dates.reduce((a, d) => a + archive[d].score, 0);
    const maxes = dates.reduce((a, d) => a + archive[d].max, 0);
    const perfect = dates.filter((d) => archive[d].score === archive[d].max).length;
    const played = new Set(dates);
    const dayMs = 86400000;
    const key = (t) => new Date(t).toISOString().slice(0, 10);
    let best = 0, cur = 0;
    for (const d of dates) {
      let run = 1, t = Date.parse(d);
      while (played.has(key(t + dayMs))) { run++; t += dayMs; }
      best = Math.max(best, run);
    }
    let t = Date.parse(dateStr);
    if (!played.has(dateStr)) t -= dayMs;
    while (played.has(key(t))) { cur++; t -= dayMs; }
    return { played: n, avg: n ? (total / n).toFixed(1) : "–",
             pct: maxes ? Math.round(100 * total / maxes) : 0, perfect, best, cur };
  }

  function showStats() {
    const archive = loadArchive();
    const s = computeStats(archive);
    const rows = Object.keys(archive).sort().reverse().slice(0, 60).map((d) => {
      const r = archive[d];
      const nice = new Date(d + "T12:00:00Z").toLocaleDateString("en-US",
        { month: "short", day: "numeric", year: "numeric" });
      return `<tr><td class="bill-name">${nice}</td>
        <td class="bill-name" style="font-style:italic">${esc(r.title || "")}</td>
        <td><strong>${r.score}/${r.max}</strong></td></tr>`;
    }).join("");
    const signedIn = window.YonCloud && window.YonCloud.enabled && window.YonCloud.user();
    const overlay = document.createElement("div");
    overlay.className = "modal-overlay";
    overlay.innerHTML = `<div class="modal-card">
      <button class="modal-close" aria-label="Close">×</button>
      <div class="section-rule">My Record</div>
      <div class="stat-row">
        <div class="stat"><div class="stat-num">${s.played}</div><div class="stat-label">Played</div></div>
        <div class="stat"><div class="stat-num">${s.avg}</div><div class="stat-label">Avg Score</div></div>
        <div class="stat"><div class="stat-num">${s.pct}%</div><div class="stat-label">Calls Made</div></div>
        <div class="stat"><div class="stat-num">${s.cur}</div><div class="stat-label">Streak</div></div>
        <div class="stat"><div class="stat-num">${s.best}</div><div class="stat-label">Best Streak</div></div>
        <div class="stat"><div class="stat-num">${s.perfect}</div><div class="stat-label">Perfect</div></div>
      </div>
      ${rows ? `<div class="history-scroll"><table class="result-table">
          <tr><th>Date</th><th>Case</th><th>Score</th></tr>${rows}</table></div>`
        : `<p class="whip-note">No decisions yet — finish today's case and it will appear here.</p>`}
      <p class="sync-note">${signedIn ? "Synced to your Google account."
        : `Stored on this device — <a href="#" id="sync-signin">sign in with Google</a> to save your scores.`}</p>
    </div>`;
    document.body.appendChild(overlay);
    overlay.querySelector(".modal-close").onclick = () => overlay.remove();
    overlay.onclick = (e) => { if (e.target === overlay) overlay.remove(); };
    const signin = overlay.querySelector("#sync-signin");
    if (signin) signin.onclick = (e) => {
      e.preventDefault();
      overlay.remove();
      const c = window.YonCloud;
      if (c && c.enabled)
        c.signIn().then(() => cloud("logEvent", "login", { method: "google" }))
                  .catch(() => {});
    };
    track("stats_open", { games_played: s.played, streak: s.cur });
  }
  document.getElementById("stats-link").onclick = showStats;

  // ---------- boot ----------
  updateStreakChip();
  if (state.revealed) showSummary();
  else showCover();
})();
