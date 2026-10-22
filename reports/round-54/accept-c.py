#!/usr/bin/env python3
"""Round-54 claim C acceptance. Run from the lane root:

  python3 -B reports/round-54/accept-c.py [--root DIR]

One leg per mechanical clause of claim C (reports/round-54/claims.json), each printed
with PASS or FAIL:
  SET       the *.md files under corpus/knowledge are exactly the 229 paths listed in
            reports/round-54/base-knowledge-files.txt plus ENTRY: count 230, added [ENTRY],
            removed [] (a second added file with a base file removed fails this leg)
  SWEEP     python3 -B reports/round-28/readme/sweep.py, run on its own, exits 0 and prints
            `rows 230 files 230` and `missing_from_index 0 []`; its exit status is read
            directly (no pipe), so a missing or misnamed README index row fails this leg
  FLOOR     the entry cites at least 20 distinct S-ids
  RANGE     every S-id the entry cites is S239 or above and is a corpus/SOURCES.md row
  STATUS    every cited row has status `mined`
  USEDBY    every cited row names ENTRY in its used-by cell
  ACCESS    python3 -B tools/check-source-access.py exits 0 (QUALITY criterion 10)
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
Review-only (no leg): the entry's topic and whether each sentence is carried by its cited
row's page.
"""
import argparse
import os
import re
import subprocess
import sys

ENTRY = "corpus/knowledge/culture-material/masks-masquerade.md"
BASE_LIST = "reports/round-54/base-knowledge-files.txt"
TOTAL = 230
FIRST_SID = 239
FLOOR = 20


def run(root, argv):
    try:
        return subprocess.run(argv, cwd=root, capture_output=True, text=True, timeout=300)
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f"ACCEPT_C_INPUT_ERROR {' '.join(argv)} {error}", file=sys.stderr)
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    try:
        base = {l.strip() for l in open(os.path.join(root, BASE_LIST), encoding="utf-8") if l.strip()}
    except OSError as error:
        print(f"ACCEPT_C_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    if len(base) != TOTAL - 1:
        print(f"ACCEPT_C_INPUT_ERROR base list has {len(base)} paths, expected {TOTAL - 1}", file=sys.stderr)
        return 2
    live = {os.path.relpath(os.path.join(d, f), root)
            for d, _, fs in os.walk(os.path.join(root, "corpus/knowledge")) for f in fs if f.endswith(".md")}
    added, removed = sorted(live - base), sorted(base - live)
    legs = [("SET", len(live) == TOTAL and added == [ENTRY] and removed == [],
             f"count={len(live)} required={TOTAL} added={added} removed={removed}")]
    sweep = run(root, [sys.executable, "-B", "reports/round-28/readme/sweep.py"])
    if sweep is None:
        return 2
    rows = re.search(r"^rows (\d+) files (\d+)$", sweep.stdout, re.M)
    missing = re.search(r"^missing_from_index (\d+) (.*)$", sweep.stdout, re.M)
    sweep_ok = (sweep.returncode == 0 and rows is not None and missing is not None
                and int(rows.group(1)) == TOTAL and int(rows.group(2)) == TOTAL
                and int(missing.group(1)) == 0)
    legs.append(("SWEEP", sweep_ok, f"exit={sweep.returncode} {rows.group(0) if rows else 'rows ?'} "
                 f"{missing.group(0) if missing else 'missing_from_index ?'}"))
    path = os.path.join(root, ENTRY)
    cited, table = [], {}
    try:
        if os.path.isfile(path):
            cited = sorted(set(re.findall(r"\bS\d{3}\b", open(path, encoding="utf-8").read())))
        for line in open(os.path.join(root, "corpus/SOURCES.md"), encoding="utf-8"):
            if re.match(r"^\| S\d{3} ", line):
                cells = line.split("|")
                table[cells[1].strip()] = cells
    except OSError as error:
        print(f"ACCEPT_C_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    legs.append(("FLOOR", len(cited) >= FLOOR, f"cited={len(cited)} floor={FLOOR}"))
    range_bad = [s for s in cited if int(s[1:]) < FIRST_SID or s not in table or len(table[s]) < 13]
    legs.append(("RANGE", not range_bad, f"bad={range_bad}"))
    ok_rows = [s for s in cited if s not in range_bad]
    status_bad = [f"{s}:{table[s][8].strip()}" for s in ok_rows if table[s][8].strip() != "mined"]
    legs.append(("STATUS", not status_bad, f"bad={status_bad}"))
    used_bad = [s for s in ok_rows if ENTRY not in table[s][11]]
    legs.append(("USEDBY", not used_bad, f"bad={used_bad}"))
    access = run(root, [sys.executable, "-B", "tools/check-source-access.py"])
    if access is None:
        return 2
    legs.append(("ACCESS", access.returncode == 0, f"exit={access.returncode} "
                 f"{(access.stdout.strip().splitlines() or ['?'])[-1]}"))
    for name, ok, detail in legs:
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
    return 0 if all(ok for _, ok, _ in legs) else 1


if __name__ == "__main__":
    sys.exit(main())
