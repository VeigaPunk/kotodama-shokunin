#!/usr/bin/env python3
"""Materialise only the bytes tools/check-gate-registry.py reads at REV."""
import os
import subprocess
import sys

lane, rev, dest = sys.argv[1:4]
names = subprocess.run(
    ["git", "-C", lane, "ls-tree", "-r", "--name-only", rev, "--", "SKILL.md", "tools", "reports"],
    capture_output=True, text=True, check=True).stdout.split()
keep = [n for n in names if n == "SKILL.md" or n.endswith(".py")]
for n in keep:
    blob = subprocess.run(["git", "-C", lane, "show", "%s:%s" % (rev, n)],
                          capture_output=True, check=True).stdout
    p = os.path.join(dest, n)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "wb") as f:
        f.write(blob)
print("MATERIALIZED %d files at %s" % (len(keep), rev))
