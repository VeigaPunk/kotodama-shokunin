#!/usr/bin/env python3
"""Second pre-freeze correction (after build-claims-final.py): state the INDEX README diff scope in the leg text
(ExecLegIndex interface finding: the counter must not be stricter than the wording)."""
import json
P = "/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-75/claims.json"
c = json.load(open(P)); C = c["claims"][0]
i = next(k for k, l in enumerate(C["legs"]) if l.startswith("INDEX:"))
old = "per-directory vector 32/32/40/29/24/95; older footers are byte-identical"
new = ("per-directory vector 32/32/40/29/24/95; every base footer block is preserved byte-identical and in order (the new footer is a new appended block); "
       "README lines changed, removed or added outside {the three adopted index rows, the myth-symbol heading, the appended footer block (`Total knowledge entries: N.` and its `Counts checked` paragraph), "
       "partition-heading lines whose only change is the count parenthetical (claim Ca's), index rows naming a knowledge file that exists at base (claim Ca's index-gap rows)} fail, and an added row-shaped `| S-id |` line fails")
assert C["legs"][i].count(old) == 1
C["legs"][i] = C["legs"][i].replace(old, new)
c["pre_data_corrections"].append({"id": "W2-F2", "by": "ExecLegIndex interface report", "fix": "C INDEX leg text states the README diff scope the counter enforces, including the exemptions for claim Ca's heading parentheticals and index-gap rows; Ca lands before C (as in round 74) so C is graded at a tree that carries Ca's README edits."})
json.dump(c, open(P, "w"), ensure_ascii=False, indent=1); print("ok")
