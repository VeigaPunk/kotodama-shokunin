#!/usr/bin/env python3
"""Round-55 claim C acceptance. Run from the lane root:

  python3 -B reports/round-55/accept-c.py [--root DIR]

One leg per mechanical clause of claim C (reports/round-55/claims.json), each printed
with PASS or FAIL:
  SET       the files under corpus/knowledge (every file, not only *.md; at base all 230 are
            *.md) are exactly the 230 paths listed in reports/round-55/base-knowledge-files.txt
            plus ENTRY: count 231, added [ENTRY], removed [] (a second added file of any
            extension, or one added with a base file removed, fails this leg)
  SWEEP     python3 -B reports/round-28/readme/sweep.py, run on its own, exits 0 and prints
            `rows 231 files 231` and `missing_from_index 0 []`; its exit status is read
            directly (no pipe), so a missing or misnamed README index row fails this leg
  FLOOR     the entry cites at least 20 distinct S-ids
  RANGE     every S-id the entry cites is S285 or above and is exactly one corpus/SOURCES.md
            row (a cited id with no row or with two or more rows fails); the entry carries no
            S-id range notation such as `S250–S255` (a range would hide the ids inside it)
  STATUS    every cited row has status `mined`
  USEDBY    every cited row names ENTRY in its used-by cell
  ACCESS    python3 -B tools/check-source-access.py exits 0 (QUALITY criterion 10)
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
Review-only (no leg; the claims file lists them): the entry's topic; whether each sentence is
carried by its cited row's page; whether each cited row was opened this round by ordinary means
(ACCESS reads only the marker words a row records); whether the entry points to partial owners
one-way; whether the ground is uncovered in substance.
"""
import argparse
import os
import re
import subprocess
import sys

ENTRY = "corpus/knowledge/myth-symbol/monsters-hybrid-beings.md"
BASE_LIST = "reports/round-55/base-knowledge-files.txt"
TOTAL = 231
FIRST_SID = 285
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
            for d, _, fs in os.walk(os.path.join(root, "corpus/knowledge")) for f in fs}
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
    cited, table, rows_per_id, spans = [], {}, {}, []
    try:
        if os.path.isfile(path):
            text = open(path, encoding="utf-8").read()
            cited = sorted(set(re.findall(r"\bS\d{3}\b", text)))
            spans = re.findall(r"\bS\d{3}\s*(?:[–—-]|to)\s*S?\d{3}\b", text)
        for line in open(os.path.join(root, "corpus/SOURCES.md"), encoding="utf-8"):
            if re.match(r"^\| S\d{3} ", line):
                cells = line.split("|")
                table[cells[1].strip()] = cells
                rows_per_id[cells[1].strip()] = rows_per_id.get(cells[1].strip(), 0) + 1
    except (OSError, UnicodeDecodeError) as error:
        print(f"ACCEPT_C_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    legs.append(("FLOOR", len(cited) >= FLOOR, f"cited={len(cited)} floor={FLOOR}"))
    range_bad = [s for s in cited if int(s[1:]) < FIRST_SID or rows_per_id.get(s, 0) != 1 or len(table[s]) < 13]
    legs.append(("RANGE", not range_bad and not spans, f"bad={range_bad} range_notation={spans}"))
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
