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

  // ---------- crowd counters (silent tracking; UI ships separately) ----------
  // One shared per-day doc in Firestore (collection "daily", see firestore.rules):
  // n completions, s0..s11 score histogram, v0..v9 per-call correct counts
  // (v9 = split call), t1..t30 current-streak histogram. Dev previews share the
  // Firebase project, so they write to a separate "-dev-" doc.
  const IS_DEV_HOST = /^(dev\.|localhost$|127\.)/.test(location.hostname)
                      || location.protocol === "file:";
  const DAILY_ID = "court" + (IS_DEV_HOST ? "-dev" : "") + "-" + dateStr;
  const STREAK_CAP = 30;   // t30 = 30 days or more
  const cloudReady = new Promise((res) => {
    if (window.YonCloud) res();
    else window.addEventListener("yon-cloud-ready", () => res(), { once: true });
  });
  function submitCrowd(score) {
    const keys = ["n", "s" + score];
    puzzle.justices.forEach((j, i) => {
      if (state.guesses[j.key] === puzzle.votes[j.key]) keys.push("v" + i);
    });
    if (tallyHit()) keys.push("v" + nJust);
    // today's streak (archive already includes today) joins the histogram
    keys.push("t" + Math.min(STREAK_CAP, Math.max(1, computeStats(loadArchive()).cur)));
    cloudReady.then(() => cloud("bumpDaily", DAILY_ID, keys)).catch(() => {});
  }

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
  }

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
    });
    authLink.onclick = () => {
      if (c.user()) { track("sign_out", {}); c.signOut(); }
      else c.signIn().then(() => cloud("logEvent", "login", { method: "google" })).catch(() => {});
    };
    track("page_open", {});
  });

  // ---------- screens ----------
  function showCover() {
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
    const score = totalScore();
    const [title, note] = rank(score);
    const cells = puzzle.justices.map((j) => {
      const hit = state.guesses[j.key] === puzzle.votes[j.key];
      return `<td class="${hit ? "hit" : "miss"}">${hit ? "✓" : "✗"}</td>`;
    }).join("");
    app.innerHTML = `<section class="screen">
      <div class="era-banner">${esc(puzzle.era)} &mdash; ${esc(puzzle.caseTitle)}</div>
      <div class="summary-score">${score}<span class="of"> / ${maxScore}</span></div>
      <div class="summary-rank">&ldquo;${title}&rdquo;</div>
      <p class="summary-rank-note">${note}</p>
      ${isPractice ? `<p class="practice-note">Archive edition &mdash; played for practice,
        not counted in your record. A new case is argued daily.</p>` : ""}
      <table class="result-table">
        <tr>${puzzle.justices.map((j) =>
          `<th>${esc(j.name.split(" ").pop())}</th>`).join("")}<th>Split</th></tr>
        <tr>${cells}<td class="${tallyHit() ? "hit" : "miss"}">${tallyHit() ? "✓" : "✗"}</td></tr>
      </table>
      <div class="share-row">
        <button class="btn-primary" id="share">Share Result</button>
        <button class="btn-ghost" id="review">Review the Votes</button>
        <button class="btn-ghost" id="practice">Play the Archive</button>
      </div>
      <div class="share-feedback" id="share-fb"></div>
    </section>`;

    document.getElementById("share").onclick = () => {
      const grid = puzzle.justices.map((j) =>
        state.guesses[j.key] === puzzle.votes[j.key] ? "\u{1F7E9}" : "\u{1F7E5}").join("");
      const text = `Split Decision №${isPractice ? " (archive)" : puzzleNo} — a Yea or Nay game\n` +
        `${score}/${maxScore} · ${title}\n${grid} ⚖️ split ${tallyHit() ? "✓" : "✗"}`;
      track("share_result", { score, max: maxScore });
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
  if (state.revealed) showSummary();
  else showCover();
})();
