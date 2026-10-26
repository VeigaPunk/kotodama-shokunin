#!/usr/bin/env python3
"""Fourth pre-freeze correction: keep rejects.counts integer-only (FROZENCFG compares int keys); the prose moves to rejects.counts_note."""
import json
P = "/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-75/claims.json"
c = json.load(open(P)); C = c["claims"][0]
n = C["rejects"]["counts"].pop("note")
C["rejects"]["counts_note"] = n
c["pre_data_corrections"].append({"id": "W2-F4", "by": "ExecSelftestFixtures open item 2", "fix": "rejects.counts holds the four integers only; the explanatory text is rejects.counts_note."})
json.dump(c, open(P, "w"), ensure_ascii=False, indent=1); print(C["rejects"]["counts"])
