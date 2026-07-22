# Yea or Nay — batch puzzle authoring brief

You are writing new daily puzzles for "Yea or Nay", a game where players guess how
5 real senators voted on 3 real bills. Your output: ONE python file at
`build/batches/batch_<LETTER>.py` (letter given in your task) containing
`SENATORS_EXTRA` and `PUZZLES`. Do not modify ANY other file in the repo.

## Non-negotiable rules

1. **Never write a vote answer from memory.** The pipeline fetches every vote
   from senate.gov XML (congress >= 101) or voteview.com CSV (congress <= 100).
   Your job is to pick the RIGHT roll-call numbers, verified against the data.
2. **Verify before you finish**: run `cd build && python3 fetch.py batches/batch_<LETTER>.py`
   — it prints every senator's actual vote and must exit 0 (no PROBLEMS).
   If a senator was absent ("Not Voting", cast_code 7/9), swap the bill for
   another suitable one, or swap the senator, and re-run. Iterate until clean.
3. **Vote numbers**: senate.gov menus are pre-downloaded at
   `/private/tmp/claude-501/-Users-alexgoddard-Desktop-congress-game/42d4d1fe-f47a-43b7-bdd9-f63eb72d225c/scratchpad/menu_<congress>_<session>.xml`
   (grep them for bill numbers/titles). For voteview (pre-1989), download
   `https://voteview.com/static/data/out/rollcalls/S0<congress>_rollcalls.csv`
   and grep vote_desc/date (the pipeline caches its own copies in build/cache/).
4. **Senator IDs**: look up bioguide IDs in the legislators datasets at the same
   scratchpad dir (`leg_hist.json`, `leg_curr.json`) or voteview members CSVs —
   never guess. Before using ANY new senator, verify their photo exists:
   `curl -sL -o /dev/null -w "%{http_code}" "https://bioguide.congress.gov/photo/<X>/<BIOGUIDE>.jpg"`
   must print 200 (X = first letter of the ID). If 404, pick a different senator.
5. **Reuse existing senator keys** from `build/puzzles_source.py` SENATORS —
   do NOT redefine them in SENATORS_EXTRA. Only add senators not already there.
   (If two batches add the same new senator with the same key/tuple, that's fine.)
6. Party labels must be era-accurate for the puzzle's time (e.g. Specter was R
   until 2009; Sinema D until Dec 2022; Thurmond D until Sept 1964).

## Data formats

Bill from senate.gov (congress 101+):
```python
{"congress": 111, "session": 1, "vote": 396,
 "name": "The Affordable Care Act",
 "desc": "..."}
```
Bill from voteview (congress <= 100). ALWAYS supply question + result text:
```python
{"source": "voteview", "congress": 88, "roll": 409,
 "name": "The Civil Rights Act of 1964",
 "question": "On Passage of H.R. 7152", "result": "Bill Passed",
 "desc": "..."}
```
Impeachment votes: add `"labels": ["GUILTY", "NOT GUILTY"]` to the bill dict
(guilty maps to yea). Frame the desc so the player knows yea=convict.
Optional per-senator override for Present/paired votes with a declared position:
```python
"overrides": {"murkowski": ["nay", "explanatory note shown after reveal"]},
```
Only use overrides when the senator's actual position is documented; the note
must explain honestly what happened.

## Puzzle structure & style

```python
{
    "id": "kebab-slug", "title": "Short Evocative Title",
    "era": "88th Congress · 1964",
    "intro": "...",     # 25-45 words, scene-setting, present tense
    "senators": [ ("key", "blurb"), x5 ],
    "bills": [ {...}, {...}, {...} ],   # exactly 3
}
```

- **Senator blurbs** (25-45 words): era-specific politics and personality at
  that moment. Give the player real signal about how they MIGHT vote, but never
  state the vote. Written like a WSJ profile: concrete, wry, specific. Study the
  examples in build/puzzles_source.py and match their register exactly.
- **Bill descs** (40-80 words): date, what the bill does, political context,
  the stakes. Vivid, specific numbers, no editorializing about who's right.
- **Group composition**: 5 senators, both parties represented (aim 3/2 or 2/2+1I),
  at least one likely defector or surprise per bill.
- **Spread check**: after verifying, look at the 15 answers. Reject/rework a
  puzzle if all three bills have the same yea/nay pattern across the five, or
  if 13+ of 15 answers are the same mark. At least one bill should split the
  group. Party-line-only puzzles are boring.
- The 3 bills may come from different congresses if the concept spans years
  (all five senators must have voted on all three bills).

## Deliverable

`build/batches/batch_<LETTER>.py` with SENATORS_EXTRA + PUZZLES (your 15
puzzles, in the order given), verified clean (exit 0). Then report: one line
per puzzle (id — verified tallies of the 3 bills — any swaps you made and why).
Concepts marked (flex) allow you to substitute a nearby bill/senator if the
data forces it; preserve the theme.
