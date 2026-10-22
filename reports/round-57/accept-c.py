#!/usr/bin/env python3
r"""Round-57 claim C acceptance (adapted from reports/round-56/accept-c.py: entry path, totals, C's reserved block, a raw docstring (round-56 spot-check §5 item 7), and the LOCATE leg). Run from the lane root:

  python3 -B reports/round-57/accept-c.py [--root DIR]

One leg per mechanical clause of claim C (reports/round-57/claims.json), each printed
with PASS or FAIL:
  SET       the files under corpus/knowledge (every file, not only *.md; at base all 232 are
            *.md) are exactly the 232 paths listed in reports/round-57/base-knowledge-files.txt
            plus ENTRY: count 233, added [ENTRY], removed [] (a second added file of any
            extension, or one added with a base file removed, fails this leg)
  SWEEP     python3 -B reports/round-28/readme/sweep.py, run on its own, exits 0 and prints
            `rows 233 files 233` and `missing_from_index 0 []`; its exit status is read
            directly (no pipe), so a missing or misnamed README index row fails this leg
  FLOOR     the entry cites at least 20 distinct S-ids
  RANGE     every S-id the entry cites lies in claim C's reserved block S413-S480 (no id below
            S413 and none above S480) and is exactly one corpus/SOURCES.md
            row (a row is any line matching `^\|\s*(S\d{3,})\s*\|`, the access checker's grammar) (a cited id with no row or with two or more rows fails); the entry carries no
            S-id range notation such as `S250–S255`, `S250 to S255`, `S250 through S255`, `S250…S255`,
            `S250−S255` (U+2212), `S250..S255` or a two-digit tail `S250–55` (a range would hide the ids inside it)
  STATUS    every cited row has status `mined`
  USEDBY    every cited row names ENTRY as one whole comma- or semicolon-separated item of its used-by cell
  ACCESS    python3 -B tools/check-source-access.py exits 0 (QUALITY criterion 10)
  LOCATE    at least one S-id is cited, and for at least ceil(0.8 x cited) of the cited rows
            reports/round-57/reopen-quote.py (row mode: the http(s) URLs of the row's `source` cell,
            at most four, fetched live by an ordinary GET; the first double-quoted span of its
            `anchor` cell; the match rule in that file's docstring) prints LOCATED. A row with a
            fabricated quote, or a URL that serves no such text, is not located; a fetch error is
            not located. Measured live at run time: the result names the run's UTC time
Frozen predicate (the same sentence in reports/round-57/claims.json and in the receipts):
  ACCEPT-C-57: every leg above prints PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
Review-only (no leg; the claims file lists them): the entry's topic; whether each sentence is
carried by its cited row's page; whether each cited row was opened this round by ordinary means
(ACCESS reads only the marker words a row records); whether the entry points to partial owners
one-way; whether the ground is uncovered in substance.
"""
import argparse
import concurrent.futures
import importlib.util
import math
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

ENTRY = "corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md"
BASE_LIST = "reports/round-57/base-knowledge-files.txt"
TOTAL = 233
FIRST_SID = 413
LAST_SID = 480
FLOOR = 20
LOCATOR = "reports/round-57/reopen-quote.py"
SHARE = 0.8


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
            for d, _, fs in os.walk(os.path.join(root, "corpus/knowledge"), followlinks=True) for f in fs}
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
            spans = re.findall(r"\bS\d{3}\s*(?:[-‐‑‒–—―−~…]|\.{2,3}|to|through|thru)\s*S?\d{2,3}\b", text)
        for line in open(os.path.join(root, "corpus/SOURCES.md"), encoding="utf-8"):
            row = re.match(r"^\|\s*(S\d{3,})\s*\|", line)
            if row:
                cells = line.split("|")
                table[row.group(1)] = cells
                rows_per_id[row.group(1)] = rows_per_id.get(row.group(1), 0) + 1
    except (OSError, UnicodeDecodeError) as error:
        print(f"ACCEPT_C_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    legs.append(("FLOOR", len(cited) >= FLOOR, f"cited={len(cited)} floor={FLOOR}"))
    range_bad = [s for s in cited if not FIRST_SID <= int(s[1:]) <= LAST_SID or rows_per_id.get(s, 0) != 1 or len(table[s]) < 13]
    legs.append(("RANGE", not range_bad and not spans, f"bad={range_bad} range_notation={spans}"))
    ok_rows = [s for s in cited if s not in range_bad]
    status_bad = [f"{s}:{table[s][8].strip()}" for s in ok_rows if table[s][8].strip() != "mined"]
    legs.append(("STATUS", not status_bad, f"bad={status_bad}"))
    used_bad = [s for s in ok_rows if ENTRY not in [u.strip() for u in re.split(r"[,;]", table[s][11])]]
    legs.append(("USEDBY", not used_bad, f"bad={used_bad}"))
    access = run(root, [sys.executable, "-B", "tools/check-source-access.py"])
    if access is None:
        return 2
    legs.append(("ACCESS", access.returncode == 0, f"exit={access.returncode} "
                 f"{(access.stdout.strip().splitlines() or ['?'])[-1]}"))
    try:
        spec = importlib.util.spec_from_file_location("reopen_quote", os.path.join(root, LOCATOR))
        locator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(locator)
    except (OSError, SyntaxError) as error:
        print(f"ACCEPT_C_INPUT_ERROR {LOCATOR} {error}", file=sys.stderr)
        return 2
    targets = {s: locator.row_target(table[s]) for s in cited if s in table and len(table[s]) >= 13}

    def probe(sid):
        urls, quote = targets[sid]
        return (sid,) + (locator.locate(urls, quote) if quote else (False, "no quote in anchor"))

    with concurrent.futures.ThreadPoolExecutor(8) as pool:
        located = sorted(pool.map(probe, sorted(targets)))
    hits = [s for s, ok, _ in located if ok]
    need = math.ceil(SHARE * len(cited))
    misses = [f"{s}: {detail[:160]}" for s, ok, detail in located if not ok]
    legs.append(("LOCATE", bool(cited) and len(hits) >= need,
                 f"located={len(hits)} cited={len(cited)} need={need} "
                 f"at={datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%MZ')} not_located={misses}"))
    for name, ok, detail in legs:
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
    verdict = all(ok for _, ok, _ in legs)
    print(f"ACCEPT-C-57: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
