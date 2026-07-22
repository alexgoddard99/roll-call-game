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
  const today = new Date();
  const dateStr = today.toISOString().slice(0, 10);
  const epoch = new Date(DATA.epoch + "T00:00:00");
  const dayNumber = Math.max(0, Math.round(
    (new Date(today.getFullYear(), today.getMonth(), today.getDate()) - epoch) / 86400000));

  const params = new URLSearchParams(location.search);
  const practiceIdx = params.has("p") ? parseInt(params.get("p"), 10) : null;
  const isPractice = practiceIdx !== null && !Number.isNaN(practiceIdx);

  const puzzleIdx = isPractice
    ? ((practiceIdx % PUZZLES.length) + PUZZLES.length) % PUZZLES.length
    : dayNumber % PUZZLES.length;
  const puzzle = PUZZLES[puzzleIdx];
  const puzzleNo = dayNumber + 1;
  const nBills = puzzle.bills.length;
  const nSens = puzzle.senators.length;

  // ---------- dateline ----------
  document.getElementById("dateline-left").textContent = today
    .toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric", year: "numeric" })
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
      const next = state.revealed.findIndex((r) => !r);
      next === -1 ? showSummary() : showBill(next);
    };
  }

  function showBill(i) {
    const bill = puzzle.bills[i];
    const revealed = state.revealed[i];
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
          <span class="actual-stamp ${actual}">${actual === "yea" ? labYea : labNay}</span>
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

    app.innerHTML = `<section class="screen">
      <div class="bill-progress"><span>Bill ${i + 1} of ${nBills}</span>${pips}</div>
      <div class="docket">
        <div class="docket-eyebrow">On the floor &mdash; ${esc(puzzle.era)}</div>
        <h2 class="docket-title">${esc(bill.name)}</h2>
        <div class="docket-date">${esc(bill.date)} &middot; roll call vote</div>
        <p class="docket-desc">${esc(bill.desc)}</p>
        <div class="ballot">${rows}</div>
        ${tally}
      </div>
      <div class="action-row">
        <button class="btn-primary" id="advance" ${revealed ? "" : "disabled"}>${btnLabel}</button>
      </div>
    </section>`;

    if (!revealed) {
      app.querySelectorAll(".stamp").forEach((b) => {
        b.onclick = () => {
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
    const score = totalScore();
    const max = nBills * nSens;
    const [title, note] = rank(score, max);

    const header = `<tr><th></th>${puzzle.senators.map((s) =>
      `<th>${esc(s.name.split(" ").pop())}</th>`).join("")}</tr>`;
    const body = puzzle.bills.map((b, i) => `<tr>
        <td class="bill-name">${esc(b.name)}</td>
        ${puzzle.senators.map((s) => {
          const hit = state.guesses[i][s.key] === b.votes[s.key];
          return `<td class="${hit ? "hit" : "miss"}">${hit ? "✓" : "✗"}</td>`;
        }).join("")}
      </tr>`).join("");

    app.innerHTML = `<section class="screen">
      <div class="era-banner">${esc(puzzle.era)} &mdash; ${esc(puzzle.title)}</div>
      <div class="summary-score">${score}<span class="of"> / ${max}</span></div>
      <div class="summary-rank">&ldquo;${title}&rdquo;</div>
      <p class="summary-rank-note">${note}</p>
      <table class="result-table">${header}${body}</table>
      <div class="share-row">
        <button class="btn-primary" id="share">Share Result</button>
        <button class="btn-ghost" id="review">Review the Votes</button>
        <button class="btn-ghost" id="practice">Play the Archive</button>
      </div>
      <div class="share-feedback" id="share-fb"></div>
    </section>`;

    document.getElementById("share").onclick = () => {
      const grid = puzzle.bills.map((b, i) => puzzle.senators.map((s) =>
        state.guesses[i][s.key] === b.votes[s.key] ? "\u{1F7E9}" : "\u{1F7E5}").join("")).join("\n");
      const text = `Yea or Nay №${isPractice ? " (archive)" : puzzleNo} — ${puzzle.title}\n` +
                   `${score}/${max} · ${title}\n${grid}`;
      navigator.clipboard.writeText(text).then(() => {
        document.getElementById("share-fb").textContent = "COPIED TO CLIPBOARD";
      }).catch(() => {
        document.getElementById("share-fb").textContent = text;
      });
    };
    document.getElementById("review").onclick = () => showBillReview(0);
    document.getElementById("practice").onclick = () => {
      location.search = "?p=" + ((puzzleIdx + 1) % PUZZLES.length);
    };
  }

  function showBillReview(i) {
    state.revealed[i] = true;
    showBill(i);
    const btn = document.getElementById("advance");
    btn.textContent = i + 1 < nBills ? "Next Bill →" : "Back to Score →";
    btn.onclick = () => (i + 1 < nBills ? showBillReview(i + 1) : showSummary());
  }

  // ---------- boot ----------
  if (allRevealed() && Object.keys(state.guesses[0]).length) showSummary();
  else showCover();
})();
