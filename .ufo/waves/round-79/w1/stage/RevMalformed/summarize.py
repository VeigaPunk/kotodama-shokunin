#!/usr/bin/env python3
"""Derive the RevMalformed counts from manifest.json and probe-raw.txt (no typed numbers).

Usage: python3 -B summarize.py <stage dir>
"""
import collections
import json
import os
import re
import sys

stage = os.path.abspath(sys.argv[1])
manifest = json.load(open(os.path.join(stage, "manifest.json"), encoding="utf-8"))
raw = open(os.path.join(stage, "probe-raw.txt"), encoding="utf-8").read()
summary = {}
in_summary = False
for line in raw.splitlines():
    if line.startswith("== SUMMARY"):
        in_summary = True
        continue
    if in_summary:
        m = re.match(r"^(\S+)\s+(\S+)\s+strict=(\S+)\s+r76=(.*)$", line)
        if m:
            summary[m.group(1)] = m.group(4)
cats = collections.defaultdict(list)
for case in manifest["cases"]:
    fid, expect, label = case["id"], case["strict_expect"], case["strict_label"]
    obs = summary.get(fid, "MISSING")
    if label == "FLOOR":
        key = "floor-not-malformed"
    elif expect == "ACCEPT":
        key = "must-accept: r76 " + ("PASS" if obs.startswith("PASS") else obs.split()[0].split(":")[0])
    elif obs.startswith("PASS"):
        key = "must-refuse: SILENT-ACCEPT by r76"
    elif obs.startswith("CRASH"):
        key = "must-refuse: CRASH in r76 (%s)" % obs.split(":", 1)[1]
    elif obs.startswith("FAIL"):
        key = "must-refuse: refused by r76 (FAIL)"
    else:
        key = "must-refuse: other (%s)" % obs
    cats[key].append(fid)
print("fixtures:", len(manifest["cases"]), "| summary rows parsed:", len(summary))
for key in sorted(cats):
    print("%-48s %3d  %s" % (key, len(cats[key]), " ".join(cats[key])))
