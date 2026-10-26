#!/usr/bin/env python3
"""Third pre-freeze correction: declare rejects.counts (ExecSelftestFixtures risk: REJECTS arithmetic) like r74's 2/4/34=40."""
import json
P = "/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-75/claims.json"
c = json.load(open(P)); C = c["claims"][0]
assert "counts" not in C["rejects"]
C["rejects"]["counts"] = {"adopted": 3, "path_present": 6, "refused": 31, "total_staged_files": 40,
  "note": "40 staged knowledge files (find merge/kotodama/knowledge -name '*.md' = 40): 3 adopted now (narrative base + 2 amendments); 6 path-present at base (2 worldbuilding-setting-practice adopted in round 74 + 4 heritage-taxonomy/conlang-scholarship whose staged bytes differ); 31 refused (naming-systems 11, verification 9, calendar-festival 3, era-periodization 2, conlang-scholarship amendments 3, conlang-methodology 1, narrative amend-23c and amend-24 2) = 40. The 4 files under merge/kotodama/amendments are outside the 40."}
i = next(k for k, l in enumerate(C["legs"]) if l.startswith("REJECTS:"))
old = "the lesson states the triage counts of the 40 staged knowledge files adopted/refused as of round 75,"
new = "the lesson states the triage counts of the 40 staged knowledge files as `3 adopted / 6 path-present / 31 refused` (the three numbers sum to 40 and equal rejects.counts at the freeze),"
assert C["legs"][i].count(old) == 1; C["legs"][i] = C["legs"][i].replace(old, new)
c["pre_data_corrections"].append({"id": "W2-F3", "by": "ExecSelftestFixtures REJECTS risk", "fix": "rejects.counts declared 3/6/31 = 40 (round-74 shape 2/4/34); REJECTS states the sum identity."})
json.dump(c, open(P, "w"), ensure_ascii=False, indent=1); print("ok")
