#!/usr/bin/env python3
"""Round-94 pre-dispatch counting receipts (frozen with claims.json).

Usage: predispatch.py --root <lane-root>
Prints one line per declared measurement; exit 0 always (values are data).
"""
import argparse, os, re, subprocess, sys

ap = argparse.ArgumentParser()
ap.add_argument("--root", required=True)
a = ap.parse_args()
R = os.path.abspath(a.root)
os.chdir(R)

def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

# A1: dangling greeting pointers in the two named lines. A pointer is dangling when
# the .md target it names does not exist or does not itself mention greeting/leave-taking.
A_FILES = {
    "corpus/knowledge/culture-material/adornment-body-codes.md": [5],
    "corpus/knowledge/culture-material/costume-semiotics.md": [143],
}
LINK = re.compile(r"((?:[\w.\-]+/)*[\w.\-]+\.md)")
dangling = []
for path, lines in A_FILES.items():
    body = read(path).split("\n")
    for ln in lines:
        text = body[ln - 1]
        if not re.search(r"greet", text, re.I):
            continue
        # rev2: every named .md target is checked (rev1 wrongly excluded
        # greet-named targets, so the counter could never accept a repoint to
        # the owner entry; see counter-revisions.md).
        targets = LINK.findall(text)
        ok = False
        for t in targets:
            cand = [os.path.normpath(os.path.join(os.path.dirname(path), t)),
                    os.path.normpath(os.path.join("corpus/knowledge", t)),
                    os.path.normpath(os.path.join("corpus/knowledge/linguistics", t))]
            for c in cand:
                if os.path.isfile(c) and re.search(r"greet|leave-taking", read(c), re.I):
                    ok = True
        if not ok:
            dangling.append(f"{path}:{ln}")
print(f"A1 dangling-greeting-pointers {len(dangling)} :: {' '.join(dangling)}")

# C1: target entry presence (frozen path)
C_ENTRY = "corpus/knowledge/linguistics/lullaby-child-song-formulae.md"
print(f"C1 entry-present {int(os.path.isfile(C_ENTRY))} :: {C_ENTRY}")

# C2: registry row count and highest id (frozen 11-cell census grammar)
src = read("corpus/SOURCES.md")
rows = re.findall(r"^ {0,3}\|[ \t]*(S\d{3,})[ \t]*\|", src, re.M)
print(f"C2 registry-rows {len(rows)} highest-id {max(rows, key=lambda s: int(s[1:]))}")

# O0: v4 tool sha at base
import hashlib
sha = hashlib.sha256(open("tools/check-advance-evidence.py", "rb").read()).hexdigest()
print(f"O0 tool-sha256 {sha}")

# Census + index at base (exit codes)
for name, cmd in [
    ("CENSUS", ["/home/vgpnk/Projects/shokunin/scripts/sources-census.sh", "validate", "--root", "/home/vgpnk/Projects/shokunin", "kotodama"]),
    ("INDEX", ["python3", "-B", "tools/check-corpus-index.py", "--root", "."]),
]:
    p = subprocess.run(cmd, capture_output=True, text=True)
    print(f"{name} rc={p.returncode} last-line: {(p.stdout.strip().splitlines() or [''])[-1]}")
