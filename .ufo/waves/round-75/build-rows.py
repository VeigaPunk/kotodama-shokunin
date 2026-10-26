#!/usr/bin/env python3
"""Final claim-C registry rows: the nine scratch-mirror rows with used-by recomputed from the staged entries' `source:` lines."""
import re, sys, os
W = "/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-75"
ENT = W + "/w2/stage/corpus/knowledge/myth-symbol"
names = ["narrative-structure-frameworks.md", "narrative-structure-frameworks.amend-2026-10-23.md", "narrative-structure-frameworks.amend-2026-10-23b.md"]
cites = {}
for n in names:
    for l in open(f"{ENT}/{n}", encoding="utf-8"):
        m = re.match(r"^- source: (S\d{3}) ", l)
        if m: cites.setdefault(m.group(1), []).append("corpus/knowledge/myth-symbol/" + n)
rows = []
for l in open(W + "/assimilation/validate/corpus/SOURCES.md", encoding="utf-8"):
    m = re.match(r"^\|\s*(S8(?:8[5-9]|9[0-3]))\s*\|", l)
    if not m: continue
    c = [x.strip() for x in l.rstrip("\n").strip().strip("|").split("|")]
    assert len(c) == 11, (m.group(1), len(c))
    c[10] = ", ".join(cites[m.group(1)])
    rows.append("| " + " | ".join(c) + " |")
assert len(rows) == 9 and len(cites) == 9, (len(rows), sorted(cites))
open(W + "/w2/stage/corpus/SOURCES.rows", "w", encoding="utf-8").write("\n".join(rows) + "\n")
for r in rows: print(r.split("|")[1].strip(), "->", r.rstrip().rsplit("|", 2)[-2].strip().replace("corpus/knowledge/myth-symbol/narrative-structure-frameworks", "nsf"))
