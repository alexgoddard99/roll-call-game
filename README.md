# Yea or Nay 🏛️

**The daily congressional vote game.** Each day presents a real bill that came
to the U.S. Senate floor, and five senators with short profiles of their
politics. Stamp each senator's ballot **Yea** or **Nay**, then see how the
roll call actually went. Three bills per day, same five senators — 15 votes
to call.

Every answer is a **real recorded vote**, extracted from the official
roll-call XML published by the [United States Senate](https://www.senate.gov/legislative/votes_new.htm).
Portraits come from the Biographical Directory of the U.S. Congress.

## Play locally

Open `web/index.html` in a browser, or:

```sh
cd web && python3 -m http.server 8642
# → http://localhost:8642
```

Add `?p=N` to the URL to play any puzzle in the archive (N = 0–73).

## How it's built

- `build/puzzles_source.py` — puzzle definitions: eras, senator groups,
  hand-written bill context and senator profiles. **No vote answers live here.**
- `build/fetch.py` — downloads each named roll-call vote from senate.gov,
  extracts the featured senators' actual votes, verifies everyone cast a
  Yea/Nay (flagging absences and "present" votes), downloads portraits, and
  emits `web/puzzles.json` + `web/puzzles.js`.

To rebuild the data (e.g. after adding a puzzle):

```sh
cd build && python3 fetch.py
```

The site itself (`web/`) is fully static — no backend, no build step.
Daily puzzle selection is date-based (days since epoch, modulo puzzle count),
and progress is saved in `localStorage`.

## Current puzzle bank

**74 puzzles · 222 bills · 1,110 verified votes**, spanning the Civil Rights Act
of 1964 through the 119th Congress (2025). Two verified data sources: senate.gov
roll-call XML (1989–present) and voteview.com (pre-1989). Highlights: the 1964
civil-rights filibuster, Gulf of Tonkin, the Panama Canal treaties, Bork, both
Clinton impeachment articles, TARP, the Obamacare wars, both Trump trials, the
January 6th electoral objections, and the 2025 confirmation fights.

Puzzle packs live in `build/batches/batch_*.py` and are auto-merged into the
daily rotation by `build/fetch.py` — add a pack, run the pipeline, redeploy.
