#!/usr/bin/env python3
"""Applies the pre-freeze (wave-1 + wave-2) predicate corrections to reports/round-75/claims.json.
Usage: build-claims-final.py [--freeze-date 2026-10-27] [--map-sha <sha256>]
Idempotent over the DRAFT bytes it was written against: it asserts every old string it replaces."""
import json, hashlib, sys
LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
P = f"{LANE}/reports/round-75/claims.json"
c = json.load(open(P))
C, A = c["claims"][0], c["claims"][1]

def sub(text, old, new):
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new)

# --- C INDEX: SHONEN summary is Ca-owned (CritClaimsFinal F1, closure-rejecting): C-alone must not grade it.
i = next(k for k, l in enumerate(C["legs"]) if l.startswith("INDEX:"))
C["legs"][i] = sub(C["legs"][i],
    "the SHONEN.md:6 registry summary reflects the registry and mined/queued/rejected counts at <lands>, and ",
    "")
# --- Ca: state the Ca-alone tuple explicitly (CritClaimsFinal F6) and the combined expectation.
A["after"] = A["after"] + (" Ca-alone tuple (measured against the base registry, independent of claim C): registry 808 rows / 713 mined / 58 queued / 37 rejected; "
    "README headings `## linguistics/ (32)` and `## culture-material/ (40)`; the SHONEN.md:6 summary is Ca-owned and states exactly that tuple at <Ca-lands>. "
    "Combined-tree expectation (COMBINED leg, informational for SHONEN): claim C appends nine rows so the live registry is 817 rows / 722 mined / 58 queued / 37 rejected at the combined revision; "
    "claim C never grades SHONEN.md.")
C["after"] = C["after"] + (" Claim C is checked at <lands> without claim Ca landed: the registry totals it moves are 808 -> 817 rows and 249 -> 252 knowledge files; "
    "SHONEN.md and the linguistics/culture-material README headings are Ca-owned and not graded by C.")

c["status"] = ("FINAL — wave-1 and wave-2 attacks applied; frozen by the commit that adds this file together with ledger.json, id-renumber-map.json, "
               "both counters, the do-nothing and junk-landing controls and the build evidence; no seat has scored landed data (nothing has landed at the freeze).")
c["frozen"] = "2026-10-27"
c["attempt"] = 2
c["pre_data_corrections"] = c.get("pre_data_corrections", []) + [
    {"id": "W2-F1", "by": "CritClaimsFinal F1/F6", "fix": "C INDEX no longer grades SHONEN.md:6 (Ca-owned); Ca `after` states the Ca-alone tuple 808/713/58/37 and the combined 817/722/58/37 expectation; C `after` states it is checked without Ca landed."},
    {"id": "A2-note", "by": "L1", "fix": "Attempt 1 of round 75 ran a 42-seat w1 and never froze; its drafts were attacked, repaired and re-attacked by attempt 2's wave 2 before this freeze; no landed byte existed at any point."},
]
json.dump(c, open(P, "w"), ensure_ascii=False, indent=1)
print("claims final:", len(C["legs"]), len(A["legs"]))
