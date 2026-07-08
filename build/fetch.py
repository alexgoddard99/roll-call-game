#!/usr/bin/env python3
"""Build web/puzzles.json from official senate.gov roll-call XML.

Downloads each roll-call vote named in puzzles_source.py, extracts the real
vote cast by each featured senator, and emits the game data file. Also
downloads member photos from bioguide.congress.gov.

Every answer in the game comes from this pipeline — nothing is hand-entered.
"""
import json
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

from puzzles_source import SENATORS, PUZZLES

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "build" / "cache"
WEB = ROOT / "web"
PHOTOS = WEB / "photos"

VOTE_URL = ("https://www.senate.gov/legislative/LIS/roll_call_votes/"
            "vote{c}{s}/vote_{c}_{s}_{n:05d}.xml")
PHOTO_URL = "https://bioguide.congress.gov/photo/{letter}/{bioguide}.jpg"

UA = {"User-Agent": "roll-call-game-builder/1.0 (personal project)"}


def get(url: str, dest: Path, binary: bool = False) -> bytes:
    if dest.exists() and dest.stat().st_size > 0:
        return dest.read_bytes()
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    dest.write_bytes(data)
    time.sleep(0.5)  # be polite to senate.gov
    return data


def parse_vote(xml_bytes: bytes) -> dict:
    root = ET.fromstring(xml_bytes)
    members = {}
    for m in root.iter("member"):
        last = (m.findtext("last_name") or "").strip()
        state = (m.findtext("state") or "").strip()
        members[(last, state)] = {
            "cast": (m.findtext("vote_cast") or "").strip(),
            "party": (m.findtext("party") or "").strip(),
        }
    count = root.find("count")
    return {
        "date": (root.findtext("vote_date") or "").split(",  ")[0].strip(),
        "question": (root.findtext("vote_question_text") or "").strip(),
        "result": (root.findtext("vote_result") or "").strip(),
        "yeas": int(count.findtext("yeas") or 0) if count is not None else 0,
        "nays": int(count.findtext("nays") or 0) if count is not None else 0,
        "members": members,
    }


def main() -> int:
    CACHE.mkdir(parents=True, exist_ok=True)
    PHOTOS.mkdir(parents=True, exist_ok=True)
    problems = []
    out = {"gameName": "Roll Call", "epoch": "2026-07-08", "puzzles": []}

    for pz in PUZZLES:
        print(f"\n=== {pz['title']} ({pz['era']}) ===")
        sen_keys = [k for k, _ in pz["senators"]]
        p_out = {
            "id": pz["id"],
            "title": pz["title"],
            "era": pz["era"],
            "intro": pz["intro"],
            "senators": [],
            "bills": [],
        }
        for key, blurb in pz["senators"]:
            bioguide, name, party, state = SENATORS[key]
            p_out["senators"].append({
                "key": key, "name": name, "party": party, "state": state,
                "blurb": blurb, "photo": f"photos/{bioguide}.jpg",
            })

        for bill in pz["bills"]:
            c, s, n = bill["congress"], bill["session"], bill["vote"]
            cache_file = CACHE / f"vote_{c}_{s}_{n:05d}.xml"
            data = get(VOTE_URL.format(c=c, s=s, n=n), cache_file)
            v = parse_vote(data)
            b_out = {
                "name": bill["name"], "desc": bill["desc"],
                "date": v["date"], "question": v["question"],
                "result": v["result"], "yeas": v["yeas"], "nays": v["nays"],
                "votes": {}, "notes": {},
            }
            overrides = bill.get("overrides", {})
            print(f"  {bill['name']}  [{v['result']} {v['yeas']}-{v['nays']}]  ({v['date']})")
            for key in sen_keys:
                bioguide, name, party, state = SENATORS[key]
                last = name.split()[-1]
                rec = v["members"].get((last, state))
                if rec is None:
                    problems.append(f"{pz['id']}/{bill['name']}: {name} ({state}) NOT FOUND in roll call")
                    print(f"    {name:20s} *** NOT FOUND ***")
                    continue
                cast = rec["cast"]
                mark = "yea" if cast == "Yea" else "nay" if cast == "Nay" else None
                if mark is None and key in overrides:
                    mark, note = overrides[key]
                    b_out["notes"][key] = note
                    cast = f"{cast} -> override {mark}"
                elif mark is None:
                    problems.append(f"{pz['id']}/{bill['name']}: {name} cast '{cast}'")
                b_out["votes"][key] = mark
                print(f"    {name:20s} {cast}")
            p_out["bills"].append(b_out)
        out["puzzles"].append(p_out)

    # Photos
    print("\n=== Photos ===")
    needed = {SENATORS[k][0] for pz in PUZZLES for k, _ in pz["senators"]}
    for bioguide in sorted(needed):
        dest = PHOTOS / f"{bioguide}.jpg"
        try:
            data = get(PHOTO_URL.format(letter=bioguide[0], bioguide=bioguide), dest, binary=True)
            if not data.startswith(b"\xff\xd8"):
                dest.unlink(missing_ok=True)
                problems.append(f"photo {bioguide}: not a JPEG")
                print(f"  {bioguide}: BAD CONTENT")
            else:
                print(f"  {bioguide}: ok ({len(data)//1024} KB)")
        except Exception as e:  # noqa: BLE001
            problems.append(f"photo {bioguide}: {e}")
            print(f"  {bioguide}: FAILED {e}")

    (WEB / "puzzles.json").write_text(json.dumps(out, indent=1))
    (WEB / "puzzles.js").write_text("window.ROLLCALL_DATA = " + json.dumps(out) + ";")
    print(f"\nWrote {WEB / 'puzzles.json'} and puzzles.js")

    if problems:
        print("\n!!! PROBLEMS !!!")
        for p in problems:
            print(" -", p)
        return 1
    print("All votes verified Yea/Nay for all featured senators.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
