# The Court — case batch authoring brief

You are writing daily puzzles for "The Court", the Supreme Court sibling of the
Yea or Nay game. Players read a real case, then guess how each justice answered
the question presented (YES/NO), plus the exact split. Your deliverable: ONE
file `build_court/batches/court_batch_<LETTER>.py` with `JUSTICES_EXTRA` and
`PUZZLES`. Do not modify any other file.

## Non-negotiable rules

1. **Never write a vote from memory.** Votes come from the Supreme Court
   Database CSV at `build_court/cache/SCDB_2024_01_justiceCentered_Citation.csv`
   (justice-centered; look up cases by `caseName` (UPPERCASE) and year to find
   the `caseId`, e.g. "1988-124").
2. **Verify**: `cd build_court && python3 fetch_court.py batches/court_batch_<LETTER>.py`
   must exit 0. The pipeline checks: case exists; every listed justice voted on
   it; nobody who voted is missing from your list (recusal => list only the 8
   who sat); clean majority/dissent coding (it flags plurality messes — swap
   those cases out).
3. **The `answer` field is the crux**: phrase `question` as a clean yes/no that
   a general reader understands, and set `answer` to how the MAJORITY actually
   answered it. Get this right from your knowledge of the holding and
   double-check the printed per-justice votes look historically correct (e.g.
   the famous dissenters must show on the losing side). If the printout looks
   wrong, your answer direction is flipped — fix it.
4. **Portraits**: JUSTICES_EXTRA maps key -> (SCDB justiceName, display name,
   English Wikipedia page title). The pipeline resolves the portrait from the
   Wikipedia page — exact page titles only (e.g. "William J. Brennan Jr.").
   The verify run confirms each downloads.
5. Reuse justice keys/blurbs across your batch's cases when the bench is the
   same. If another batch defines the same key, the tuple must match exactly —
   check other court_batch_*.py files first. Era-specific blurb differences →
   use era-suffixed keys (e.g. "rehnquist86" vs "rehnquist_cj").

## Format

```python
JUSTICES_EXTRA = {
    "scalia": ("AScalia", "Antonin Scalia", "Antonin Scalia"),
}
PUZZLES = [{
    "id": "texas-v-johnson",
    "era": "The Rehnquist Court · October Term 1988",
    "caseTitle": "Texas v. Johnson",
    "scdb": "1988-124",
    "question": "May the government punish burning the American flag as political protest?",
    "answer": "no",
    "intro": "...",   # 25-45 words, cover-page scene-setting, present tense
    "desc": "...",    # 50-90 words: the facts, the stakes, the atmosphere
    "justices": [("key", "blurb"), ...],  # every justice who voted, seniority order
}]
```

## Style (match build/puzzles_source.py register exactly)

- **Justice blurbs** (25-45 words): judicial philosophy and temperament AT THAT
  TIME, written like a WSJ profile. Real signal, never the vote itself. A blurb
  is reused across the era's cases, so keep it case-agnostic.
- **desc**: the human story (who was arrested/sued/fired), the legal collision,
  what hangs on it. No outcome spoilers beyond what any newspaper reader of the
  day would know going in.
- **question**: neutral phrasing; avoid double negatives; the yes/no must be
  crisp ("May a state...?", "Does the First Amendment protect...?").
- Case mix: mostly contested splits (5-4, 6-3); one or two famous unanimous
  rulings are fine as gimmes. Avoid per curiam or plurality tangles the
  pipeline flags.

Report back one line per case: id — verified split and answer — any cases you
swapped out and why.
