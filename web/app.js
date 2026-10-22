/* Yea or Nay — daily congressional vote guessing game */
(function () {
  "use strict";

  const DATA = window.ROLLCALL_DATA;
  if (!DATA) {
    document.getElementById("app").innerHTML =
      "<p style='text-align:center'>Couldn't load puzzle data. Run <code>build/fetch.py</code> first.</p>";
    return;
  }

  const PUZZLES = DATA.puzzles;
  const app = document.getElementById("app");

  // ---------- daily selection ----------
  // The edition flips at midnight US Eastern time for all players worldwide.
  const today = new Date();
  const dateStr = new Intl.DateTimeFormat("en-CA",
    { timeZone: "America/New_York" }).format(today); // YYYY-MM-DD in ET
  const dayNumber = Math.max(0, Math.round(
    (Date.parse(dateStr) - Date.parse(DATA.epoch)) / 86400000));

  const params = new URLSearchParams(location.search);
  const practiceIdx = params.has("p") ? parseInt(params.get("p"), 10) : null;
  const isPractice = practiceIdx !== null && !Number.isNaN(practiceIdx);

  // ---------- first-visit flow ----------
  // First-time visitors land straight on bill 1: the cover lost about half of
  // them before they ever voted (funnel analysis, 2026-10-20). The choice is
  // stored so a player keeps the flow they started with; legacy players who
  // already have an archive keep the cover. "#play" forces the direct flow for
  // anyone (the deep link partners get). DIRECT_FIRST_VISIT is the kill switch.
  // Every GA4 event carries `flow` so the funnel can be split by it.
  const DIRECT_FIRST_VISIT = true;
  const FLOW_KEY = "yon-flow";
  let flow = null; // "direct" | "deeplink" | "cover" | null (legacy player)
  let docketTracked = false; // open_docket fires once per page load

  // the archive holds only the last 10 published editions (by day, so it
  // follows the rotation correctly even after the bank wraps)
  const archDays = [];
  for (let d = Math.max(0, dayNumber - 9); d <= dayNumber; d++)
    archDays.push(d % PUZZLES.length);
  // early days: pad the archive to 10 with editions from the far end of the
  // bank, which won't come up in the daily rotation for months
  for (let i = PUZZLES.length - 1; archDays.length < 10 && i >= 0; i--)
    if (!archDays.includes(i)) archDays.unshift(i);
  // YON_DEV_PREVIEW is set only by the dev-only preview wrapper (web-dev/)
  if (isPractice && !archDays.includes(practiceIdx) && !window.YON_DEV_PREVIEW) {
    document.getElementById("dateline-left").textContent = "ARCHIVE";
    document.getElementById("dateline-right").textContent = "NOT AVAILABLE";
    app.innerHTML = `<section class="screen" style="text-align:center">
      <p class="practice-note" style="margin-top:40px">This edition isn&rsquo;t available
        &mdash; the archive holds the ten most recent daily puzzles.</p>
      <div class="share-row" style="justify-content:center">
        <a class="btn-primary" href="./" style="text-decoration:none">Play Today&rsquo;s Edition</a>
      </div>
    </section>`;
    return;
  }

  const puzzleIdx = isPractice
    ? ((practiceIdx % PUZZLES.length) + PUZZLES.length) % PUZZLES.length
    : dayNumber % PUZZLES.length;
  const puzzle = PUZZLES[puzzleIdx];
  const puzzleNo = dayNumber + 1;
  const nBills = puzzle.bills.length;
  const nSens = puzzle.senators.length;

  // ---------- crowd counters (shared per-day doc in Firestore, see firestore.rules) ----------
  // Dev previews share the Firebase project, so they write to a separate "-dev-" doc.
  const IS_DEV_HOST = /^(dev\.|localhost$|127\.)/.test(location.hostname)
                      || location.protocol === "file:";
  const DAILY_ID = "senate" + (IS_DEV_HOST ? "-dev" : "") + "-" + dateStr;
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

  // ---------- dateline ----------
  document.getElementById("dateline-left").textContent = today
    .toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric",
                                   year: "numeric", timeZone: "America/New_York" })
    .toUpperCase();
  document.getElementById("dateline-right").textContent = isPractice
    ? "ARCHIVE EDITION" : "PUZZLE № " + puzzleNo;

  // ---------- state ----------
  const storeKey = "rollcall-" + dateStr;
  let state = { guesses: puzzle.bills.map(() => ({})), revealed: puzzle.bills.map(() => false) };

  if (!isPractice) {
    try {
      const saved = JSON.parse(localStorage.getItem(storeKey));
      if (saved && saved.puzzleIdx === puzzleIdx) state = saved.state;
    } catch (e) { /* fresh start */ }
  }
  function persist() {
    if (isPractice) return;
    try { localStorage.setItem(storeKey, JSON.stringify({ puzzleIdx, state })); } catch (e) {}
  }

  // ---------- helpers ----------
  const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
                      .replace(/"/g, "&quot;");

  function billScore(i) {
    let s = 0;
    for (const sen of puzzle.senators)
      if (state.guesses[i][sen.key] === puzzle.bills[i].votes[sen.key]) s++;
    return s;
  }
  const totalScore = () => puzzle.bills.reduce((a, _, i) => a + billScore(i), 0);
  const allRevealed = () => state.revealed.every(Boolean);

  function rank(score, max) {
    const pct = score / max;
    if (pct === 1)    return ["Master of the Senate", "Lyndon Johnson is taking notes."];
    if (pct >= 0.86) return ["Majority Whip", "You can count votes with the best of them."];
    if (pct >= 0.66) return ["Committee Chair", "A seasoned reader of the chamber."];
    if (pct >= 0.46) return ["Junior Senator", "You know the players, if not every play."];
    if (pct >= 0.26) return ["Freshman Legislator", "Still learning where the cloakroom is."];
    return ["Congressional Intern", "At least you found the chamber."];
  }

  function senatorCard(sen) {
    return `<div class="senator-card">
      <div class="portrait-frame">
        <img src="${sen.photo}" alt="Portrait of ${esc(sen.name)}">
        <span class="party-seal party-${sen.party}">${sen.party}</span>
      </div>
      <div class="senator-name">${esc(sen.name)}</div>
      <div class="senator-meta">${sen.party}&ndash;${sen.state}</div>
      <div class="senator-blurb">${esc(sen.blurb)}</div>
    </div>`;
  }

  // ---------- screens ----------
  function showCover() {
    pageview("/cover", "Cover — " + puzzle.title);
    app.innerHTML = `<section class="screen">
      <div class="era-banner">${esc(puzzle.era)}</div>
      <h2 class="puzzle-title">${esc(puzzle.title)}</h2>
      <p class="puzzle-intro">${esc(puzzle.intro)}</p>
      <div class="section-rule">The Senators</div>
      <div class="senator-grid">${puzzle.senators.map(senatorCard).join("")}</div>
      <p class="whip-note">Three bills came to the floor. Stamp each senator&rsquo;s ballot
        <strong>Yea</strong> or <strong>Nay</strong> &mdash; then see the real roll call.</p>
      <div class="action-row">
        <button class="btn-primary" id="go">Open the Docket &rarr;</button>
      </div>
    </section>`;
    document.getElementById("go").onclick = () => {
      if (!docketTracked) track("open_docket", {});
      docketTracked = true;
      const next = state.revealed.findIndex((r) => !r);
      next === -1 ? showSummary() : showBill(next);
    };
  }

  // One line of edition context on every bill screen (era · № · title), so a
  // player who never saw the cover still knows which story they're in.
  function editionLine() {
    return `<div class="edition-line"><span>${esc(puzzle.era)}</span><span class="sep">&middot;</span>` +
      `<span>${isPractice ? "Archive edition" : "№ " + puzzleNo}</span><span class="sep">&middot;</span>` +
      `<em>${esc(puzzle.title)}</em></div>`;
  }

  function showBill(i) {
    const bill = puzzle.bills[i];
    const revealed = state.revealed[i];
    pageview("/bill/" + (i + 1), "Bill " + (i + 1) + " — " + bill.name);
    // Direct arrivals get the cover's standfirst on the first bill, and a
    // one-line how-to the very first time they play.
    const directIntro = !revealed && !state.revealed.some(Boolean)
                        && (flow === "direct" || flow === "deeplink");
    const firstPlay = directIntro && !Object.keys(loadArchive()).length;
    const introHTML = directIntro
      ? `<p class="edition-intro">${esc(puzzle.intro)}
           <a href="#" id="see-docket">Meet the senators &rarr;</a></p>` : "";
    const howToHTML = firstPlay
      ? `<p class="whip-note how-to">Stamp each senator&rsquo;s ballot <strong>Yea</strong> or
           <strong>Nay</strong>, then record the vote to see the real roll call.</p>` : "";
    const pips = puzzle.bills.map((_, j) =>
      `<span class="pip ${state.revealed[j] ? "done" : j === i ? "now" : ""}"></span>`).join("");

    const [labYea, labNay] = bill.labels || ["YEA", "NAY"];
    const rows = puzzle.senators.map((sen) => {
      const guess = state.guesses[i][sen.key];
      let right;
      if (!revealed) {
        right = `<div class="stamp-pair">
          <button class="stamp ${guess === "yea" ? "stamped-yea" : guess ? "faded" : ""}"
                  data-sen="${sen.key}" data-vote="yea">${labYea}</button>
          <button class="stamp ${guess === "nay" ? "stamped-nay" : guess ? "faded" : ""}"
                  data-sen="${sen.key}" data-vote="nay">${labNay}</button>
        </div>`;
      } else {
        const actual = bill.votes[sen.key];
        const hit = guess === actual;
        right = `<div class="stamp-pair">
          <span class="verdict ${hit ? "hit" : "miss"}">${hit ? "✓" : "✗"}</span>
          <span class="reveal-cell">
            <span class="reveal-label">Your call</span>
            <span class="your-call ${hit ? "" : "wrong"}">${guess === "yea" ? labYea : labNay}</span>
          </span>
          <span class="reveal-cell">
            <span class="reveal-label">Voted</span>
            <span class="actual-stamp ${actual}">${actual === "yea" ? labYea : labNay}</span>
          </span>
        </div>`;
      }
      const note = revealed && bill.notes && bill.notes[sen.key]
        ? `<div class="vote-note">${esc(bill.notes[sen.key])}</div>` : "";
      return `<div class="ballot-row">
        <img class="ballot-portrait" src="${sen.photo}" alt="">
        <div class="ballot-id">
          <div class="senator-name">${esc(sen.name)}</div>
          <div class="senator-meta">${sen.party}&ndash;${sen.state}</div>
          <div class="ballot-blurb">${esc(sen.blurb)}</div>
        </div>
        ${right}${note}
      </div>`;
    }).join("");

    const tally = revealed
      ? `<div class="tally-banner">
           <strong>${esc(bill.result.toUpperCase())} &middot; ${bill.yeas}&ndash;${bill.nays}</strong><br>
           <span style="color:var(--ink-faint)">${esc(bill.question)}</span>
           <span class="tally-round-score">You called ${billScore(i)} of ${nSens} correctly</span>
         </div>` : "";

    const lastBill = i === nBills - 1;
    const btnLabel = revealed
      ? (lastBill && allRevealed() ? "See Your Score →" : "Next Bill →")
      : "Record the Vote";

    app.innerHTML = `<section class="screen${revealed ? " is-revealed" : ""}">
      ${editionLine()}
      ${introHTML}
      <div class="bill-progress"><span>Bill ${i + 1} of ${nBills}</span>${pips}</div>
      <div class="docket">
        <div class="docket-eyebrow">On the floor &mdash; ${esc(puzzle.era)}</div>
        <h2 class="docket-title">${esc(bill.name)}</h2>
        <div class="docket-date">${esc(bill.date)} &middot; roll call vote</div>
        <p class="docket-desc">${esc(bill.desc)}</p>
        ${howToHTML}
        <div class="ballot">${rows}</div>
        ${tally}
      </div>
      <div class="action-row">
        <button class="btn-primary" id="advance" ${revealed ? "" : "disabled"}>${btnLabel}</button>
      </div>
    </section>`;

    const seeDocket = document.getElementById("see-docket");
    if (seeDocket) seeDocket.onclick = (e) => { e.preventDefault(); showCover(); window.scrollTo({ top: 0 }); };

    if (!revealed) {
      app.querySelectorAll(".stamp").forEach((b) => {
        b.onclick = () => {
          if (!startTracked) {
            startTracked = true;
            const fresh = state.guesses.every((g) => !Object.keys(g).length)
                          && !state.revealed.some(Boolean);
            if (fresh) track("puzzle_start", {});
          }
          state.guesses[i][b.dataset.sen] = b.dataset.vote;
          persist();
          showBillStamps(i);
        };
      });
      updateAdvance(i);
    }
    document.getElementById("advance").onclick = () => {
      if (!state.revealed[i]) {
        state.revealed[i] = true;
        persist();
        track("bill_revealed", {
          bill_index: i + 1, bill_name: bill.name, bill_score: billScore(i),
        });
        if (allRevealed()) {
          recordResult();
          const score = totalScore(), max = nBills * nSens;
          const pct = Math.round(100 * score / max);
          track("puzzle_complete", {
            score, max, pct_correct: pct,
            perfect: score === max ? 1 : 0,
            rank: rank(score, max)[0],
            streak: isPractice ? 0 : computeStats(loadArchive()).cur,
          });
        }
        showBill(i); // re-render in revealed mode
        window.scrollTo({ top: 0, behavior: "smooth" });
      } else if (i + 1 < nBills && !state.revealed[i + 1]) {
        showBill(i + 1);
        window.scrollTo({ top: 0, behavior: "smooth" });
      } else {
        const next = state.revealed.findIndex((r) => !r);
        next === -1 ? showSummary() : showBill(next);
      }
    };
  }

  function showBillStamps(i) {
    // update stamp classes in place (no full re-render, keeps animation tight)
    app.querySelectorAll(".stamp").forEach((b) => {
      const guess = state.guesses[i][b.dataset.sen];
      b.className = "stamp " +
        (guess === b.dataset.vote ? "stamped-" + b.dataset.vote : guess ? "faded" : "");
    });
    updateAdvance(i);
  }

  function updateAdvance(i) {
    const done = puzzle.senators.every((s) => state.guesses[i][s.key]);
    document.getElementById("advance").disabled = !done;
  }

  function showSummary() {
    pageview("/score", "Score — " + puzzle.title);
    const score = totalScore();
    const max = nBills * nSens;
    const [title, note] = rank(score, max);

    const header = `<tr><th></th>${puzzle.senators.map((s) =>
      `<th>${esc(s.name.split(" ").pop())}</th>`).join("")}</tr>`;
    const body = puzzle.bills.map((b, i) => `<tr>
        <td class="bill-name">${esc(b.name)}</td>
        ${puzzle.senators.map((s, si) => {
          const hit = state.guesses[i][s.key] === b.votes[s.key];
          return `<td class="${hit ? "hit" : "miss"}" data-cell="${i * nSens + si}">${hit ? "✓" : "✗"}${isPractice ? "" : `<span class="cell-pct"></span>`}</td>`;
        }).join("")}
      </tr>`).join("");

    app.innerHTML = `<section class="screen">
      <div class="era-banner">${esc(puzzle.era)} &mdash; ${esc(puzzle.title)}</div>
      <div class="summary-score">${score}<span class="of"> / ${max}</span></div>
      <div class="summary-rank">&ldquo;${title}&rdquo;</div>
      <p class="summary-rank-note">${note}</p>
      ${isPractice ? `<p class="practice-note">Archive edition &mdash; played for practice,
        not counted in your record. Come back tomorrow for the next scored daily.</p>`
        : `<div class="crowd-line" id="crowd-line"></div>${streakBannerHTML()}`}
      <table class="result-table">${header}${body}</table>
      <div class="share-row">
        <button class="btn-primary" id="share">Share Result</button>
        <button class="btn-ghost" id="review">Review the Votes</button>
        <button class="btn-ghost" id="practice">Play the Archive</button>
      </div>
      <div class="share-feedback" id="share-fb"></div>
    </section>`;
    if (!isPractice) { bindStreakBanner(); renderCrowd(score, max); }

    document.getElementById("share").onclick = () => {
      const grid = puzzle.bills.map((b, i) => puzzle.senators.map((s) =>
        state.guesses[i][s.key] === b.votes[s.key] ? "\u{1F7E9}" : "\u{1F7E5}").join("")).join("\n");
      const cur = isPractice ? 0 : computeStats(loadArchive()).cur;
      const streakBit = cur >= 2 ? ` · 🔥 ${cur}-day streak` : "";
      const text = `Yea or Nay №${isPractice ? " (archive)" : puzzleNo} — ${puzzle.title}\n` +
                   `${score}/${max} · ${title}${streakBit}\n${grid}\nplayyeaornay.com`;
      const shareParams = { score, max, streak: cur };
      if (crowdBeat !== null) shareParams.beat_pct = crowdBeat;
      track("share_result", shareParams);
      navigator.clipboard.writeText(text).then(() => {
        document.getElementById("share-fb").textContent = "COPIED TO CLIPBOARD";
      }).catch(() => {
        document.getElementById("share-fb").textContent = text;
      });
    };
    document.getElementById("review").onclick = () => {
      track("review_votes", {});
      showBillReview(0);
    };
    document.getElementById("practice").onclick = () => {
      track("archive_click", {});
      const pos = archDays.indexOf(puzzleIdx);
      location.search = "?p=" + archDays[(pos + 1) % archDays.length];
    };
  }

  // ---------- streak banner (results screen) ----------
  const MILESTONES = {
    7: "A full week. The whip count knows your name.",
    14: "Two weeks straight. Seniority is accruing.",
    30: "A full month. Frankly senatorial.",
    50: "Fifty days. They&rsquo;re saving you a desk.",
    100: "One hundred days. Master of the Senate indeed.",
    365: "A full year. Lyndon Johnson is taking notes.",
  };
  // Sign-in card on the score screen: shown after every daily completion while
  // signed out (once auth has settled, so it never flashes for signed-in
  // players); "Not now" snoozes it for a week, but streak milestones always
  // bring it back. Funnel: signin_prompt_shown -> signin_prompt_click -> login.
  const SNOOZE_KEY = "yon-signin-snooze", SNOOZE_MS = 7 * 86400000;
  const PROMPT_MILESTONES = [3, 7, 14, 30];
  let promptLogged = false;
  function signinSnoozed() {
    try { return +localStorage.getItem(SNOOZE_KEY) > Date.now(); } catch (e) { return false; }
  }
  function streakBannerHTML() {
    const s = computeStats(loadArchive());
    const c = window.YonCloud;
    const signedIn = c && c.enabled && c.user();
    const settled = c && c.enabled && c.settled && c.settled();
    const showCard = settled && !signedIn
                     && (!signinSnoozed() || PROMPT_MILESTONES.includes(s.cur));
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
    const card = showCard ? `<div class="signin-card" data-streak="${s.cur}">
        <div class="signin-head">Keep your streak</div>
        <div class="signin-sub">${s.cur <= 1 ? "Today&rsquo;s score is stored on this device only."
          : `Your ${s.cur}-day streak is stored on this device only.`}
          Sign in to save it and play on any device.</div>
        <div class="signin-actions">
          <button class="btn-primary" id="signin-go">Sign in with Google</button>
          <button class="btn-ghost" id="signin-later">Not now</button>
        </div>
      </div>` : "";
    return `<div class="streak-banner">
      <div class="streak-main">${main}</div>
      <div class="streak-sub">${sub}</div>
      ${card}
    </div>`;
  }
  function bindStreakBanner() {
    const card = app.querySelector(".signin-card");
    if (!card) return;
    const streak = +card.dataset.streak || 0;
    if (!promptLogged) { promptLogged = true; track("signin_prompt_shown", { streak }); }
    document.getElementById("signin-go").onclick = () => {
      track("signin_prompt_click", { streak });
      const c = window.YonCloud;
      if (c && c.enabled)
        c.signIn().then(() => cloud("logEvent", "login", { method: "google", placement: "score_prompt" }))
                  .catch(() => {});
    };
    document.getElementById("signin-later").onclick = () => {
      try { localStorage.setItem(SNOOZE_KEY, String(Date.now() + SNOOZE_MS)); } catch (e) {}
      track("signin_prompt_dismiss", { streak });
      card.remove();
    };
  }
  // Re-render streak surfaces after anything that can change the archive or auth
  function refreshStreakUI() {
    updateStreakChip();
    const b = app.querySelector(".streak-banner");
    if (b) { b.outerHTML = streakBannerHTML(); bindStreakBanner(); }
  }

  // ---------- crowd comparison ----------
  function submitCrowd(score) {
    const keys = ["n", "s" + score];
    puzzle.bills.forEach((b, bi) => puzzle.senators.forEach((s, si) => {
      if (state.guesses[bi][s.key] === b.votes[s.key]) keys.push("v" + (bi * nSens + si));
    }));
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

  function showBillReview(i) {
    state.revealed[i] = true;
    showBill(i);
    const btn = document.getElementById("advance");
    btn.textContent = i + 1 < nBills ? "Next Bill →" : "Back to Score →";
    btn.onclick = () => (i + 1 < nBills ? showBillReview(i + 1) : showSummary());
  }

  // ---------- results archive (local, + cloud sync when signed in) ----------
  const ARCHIVE_KEY = "yon-results";

  function loadArchive() {
    try { return JSON.parse(localStorage.getItem(ARCHIVE_KEY)) || {}; }
    catch (e) { return {}; }
  }
  function saveArchive(a) {
    try { localStorage.setItem(ARCHIVE_KEY, JSON.stringify(a)); } catch (e) {}
  }

  // Reconstruct results from old per-day saves (pre-stats players keep history)
  function reconstructArchive() {
    const archive = loadArchive();
    let changed = false;
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      const m = k && k.match(/^rollcall-(\d{4}-\d{2}-\d{2})$/);
      if (!m || archive[m[1]]) continue;
      try {
        const saved = JSON.parse(localStorage.getItem(k));
        const pz = PUZZLES[saved.puzzleIdx];
        if (!pz || !saved.state.revealed.every(Boolean)) continue;
        let score = 0;
        pz.bills.forEach((b, bi) => pz.senators.forEach((s) => {
          if (saved.state.guesses[bi][s.key] === b.votes[s.key]) score++;
        }));
        archive[m[1]] = { puzzleId: pz.id, title: pz.title, era: pz.era,
                          score, max: pz.bills.length * pz.senators.length };
        changed = true;
      } catch (e) { /* skip */ }
    }
    if (changed) saveArchive(archive);
    return archive;
  }

  function recordResult() {
    if (isPractice) return;
    const archive = loadArchive();
    if (archive[dateStr]) return;
    const result = { puzzleId: puzzle.id, title: puzzle.title, era: puzzle.era,
                     score: totalScore(), max: nBills * nSens, no: puzzleNo };
    archive[dateStr] = result;
    saveArchive(archive);
    cloud("saveResult", dateStr, result);
    submitCrowd(result.score);
    updateStreakChip();
  }

  // ---------- cloud / auth ----------
  function cloud(method, ...args) {
    const c = window.YonCloud;
    if (c && c.enabled && c[method]) return c[method](...args);
  }

  // GA4 events. The cloud layer is a module loaded after this script, so
  // anything fired during boot (the first page_view, the direct flow's
  // open_docket) is queued and flushed on yon-cloud-ready instead of dropped.
  const eventQueue = [];
  function send(name, params) {
    if (window.YonCloud) cloud("logEvent", name, params);
    else if (eventQueue.length < 50) eventQueue.push([name, params]);
  }
  // GA4 event with common game context on every hit
  function track(name, extra) {
    const common = { puzzle_id: puzzle.id, puzzle_no: puzzleNo, era: puzzle.era,
                     practice: isPractice ? 1 : 0 };
    if (flow) common.flow = flow;
    send(name, Object.assign(common, extra || {}));
  }
  let startTracked = false;

  // Synthetic page_view per screen, so GA4 Views reflect screens seen rather
  // than one hit per session.
  let lastPageview = null;
  function pageview(path, title) {
    if (path === lastPageview) return; // same-screen re-render (e.g. reveal)
    lastPageview = path;
    // The landing screen's view is already counted by gtag's automatic
    // page_view on load, so only screens shown after the cloud layer is up
    // send a synthetic one.
    if (!window.YonCloud) return;
    send("page_view", { page_title: title, page_path: path,
                        page_location: location.origin + path });
  }

  async function syncWithCloud() {
    const c = window.YonCloud;
    if (!c || !c.enabled || !c.user()) return;
    try {
      const remote = await c.fetchResults();
      const local = loadArchive();
      let changed = false;
      for (const [date, r] of Object.entries(remote)) {
        if (!local[date]) { local[date] = r; changed = true; }
      }
      for (const [date, r] of Object.entries(local)) {
        if (!remote[date]) c.saveResult(date, r);
      }
      if (changed) saveArchive(local);
      refreshStreakUI();
    } catch (e) { /* offline is fine */ }
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
      if (c.user()) {
        track("sign_out", {});
        c.signOut();
      } else {
        c.signIn().then(() => cloud("logEvent", "login", { method: "google" }))
                  .catch(() => {});
      }
    };
    track("page_open", {});
    eventQueue.splice(0).forEach(([n, p]) => cloud("logEvent", n, p));
  });

  // ---------- stats modal ----------
  function computeStats(archive) {
    const dates = Object.keys(archive).sort();
    const n = dates.length;
    const total = dates.reduce((a, d) => a + archive[d].score, 0);
    const maxes = dates.reduce((a, d) => a + archive[d].max, 0);
    const perfect = dates.filter((d) => archive[d].score === archive[d].max).length;
    let best = 0, cur = 0;
    const dayMs = 86400000;
    const played = new Set(dates);
    const key = (t) => new Date(t).toISOString().slice(0, 10); // date-only keys, UTC
    for (let i = 0; i < n; i++) {
      let run = 1;
      let t = Date.parse(dates[i]); // date-only string parses as UTC midnight
      while (played.has(key(t + dayMs))) { run++; t += dayMs; }
      best = Math.max(best, run);
    }
    // current streak: count back from today (or yesterday if today unplayed)
    let t = Date.parse(dateStr);
    if (!played.has(dateStr)) t -= dayMs;
    while (played.has(key(t))) { cur++; t -= dayMs; }
    return { played: n, avg: n ? (total / n).toFixed(1) : "–",
             pct: maxes ? Math.round(100 * total / maxes) : 0, perfect, best, cur };
  }

  function showStats() {
    const archive = reconstructArchive();
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
        <div class="stat"><div class="stat-num">${s.pct}%</div><div class="stat-label">Votes Called</div></div>
        <div class="stat"><div class="stat-num">${s.cur}</div><div class="stat-label">Streak</div></div>
        <div class="stat"><div class="stat-num">${s.best}</div><div class="stat-label">Best Streak</div></div>
        <div class="stat"><div class="stat-num">${s.perfect}</div><div class="stat-label">Perfect</div></div>
      </div>
      ${rows ? `<div class="history-scroll"><table class="result-table">
          <tr><th>Date</th><th>Edition</th><th>Score</th></tr>${rows}</table></div>`
        : `<p class="whip-note">No completed games yet — finish today's edition and it will appear here.</p>`}
      <p class="sync-note">${signedIn
        ? "Synced to your Google account."
        : `Stored on this device — <a href="#" id="sync-signin">sign in with Google</a> to save your scores.`}</p>
    </div>`;
    document.body.appendChild(overlay);
    const close = () => overlay.remove();
    overlay.querySelector(".modal-close").onclick = close;
    overlay.onclick = (e) => { if (e.target === overlay) close(); };
    const signin = overlay.querySelector("#sync-signin");
    if (signin) signin.onclick = (e) => {
      e.preventDefault();
      close();
      const c = window.YonCloud;
      if (c && c.enabled)
        c.signIn().then(() => cloud("logEvent", "login", { method: "google" }))
                  .catch(() => {});
    };
    track("stats_open", { games_played: s.played, streak: s.cur });
  }
  document.getElementById("stats-link").onclick = showStats;

  // ---------- header streak chip ----------

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
  if (streakChip) streakChip.onclick = showStreakModal;

  // ---------- boot ----------
  const archiveAtBoot = reconstructArchive();
  updateStreakChip();
  // A first visit: nothing in the archive and nothing started today. The
  // handoff from the old address has already merged any imported record by
  // now, so a player arriving from playyeaornay.com is not a first visit.
  const isFirstVisit = !isPractice && !Object.keys(archiveAtBoot).length
                       && !localStorage.getItem(storeKey);
  try { flow = localStorage.getItem(FLOW_KEY); } catch (e) {}
  if (flow !== "direct" && flow !== "cover") flow = null;
  if (location.hash === "#play") flow = "deeplink";
  else if (DIRECT_FIRST_VISIT && !flow && isFirstVisit) {
    flow = "direct";
    try { localStorage.setItem(FLOW_KEY, flow); } catch (e) {}
  }
  const direct = (flow === "direct" || flow === "deeplink") && !isPractice;
  if (allRevealed() && Object.keys(state.guesses[0]).length) { recordResult(); showSummary(); }
  else if (direct) {
    docketTracked = true;
    track("open_docket", { auto: 1 });
    const next = state.revealed.findIndex((r) => !r);
    next === -1 ? showSummary() : showBill(next);
  }
  else showCover();

  // record at the moment the last bill is revealed
  const _origShowSummary = showSummary;
  showSummary = function () { recordResult(); _origShowSummary(); };
})();
