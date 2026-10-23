#!/usr/bin/env python3
r"""Round-58 claim C acceptance (adapted from reports/round-57/accept-c.py: entry path, totals, C's
reserved block S500-S559, LOCATE with no slack, and three new legs, BOILER, RELEVANCE and TOPIC, from
reports/round-58/rowcheck.py, written for the round-57 closure's routed defect 2). Run from the
lane root:

  python3 -B reports/round-58/accept-c.py [--root DIR]

One leg per mechanical clause of claim C (reports/round-58/claims.json), each printed
with PASS or FAIL:
  SET       the files under corpus/knowledge (every file, not only *.md) are exactly the 233 paths
            listed in reports/round-58/base-knowledge-files.txt plus ENTRY: count 234, added
            [ENTRY], removed []
  SWEEP     python3 -B reports/round-28/readme/sweep.py, run on its own, exits 0 and prints
            `rows 234 files 234` and `missing_from_index 0 []` (exit status read directly)
  FLOOR     the entry cites at least 20 distinct S-ids
  RANGE     every S-id the entry cites lies in claim C's reserved block S500-S559 and is exactly one
            corpus/SOURCES.md row (`^\|\s*(S\d{3,})\s*\|`, at least 13 cells); the entry carries no
            S-id range notation
  STATUS    every cited row has status `mined`
  USEDBY    every cited row names ENTRY as one whole comma- or semicolon-separated item of its used-by cell
  ACCESS    python3 -B tools/check-source-access.py exits 0 (QUALITY criterion 10)
  LOCATE    at least one S-id is cited and EVERY cited row is located: reports/round-58/reopen-quote.py
            (a byte copy of reports/round-57/reopen-quote.py; rules in its docstring) finds the first
            double-quoted span of the row's anchor cell, at least 8 words, in the text one of the
            row's source URLs (at most four) serves now. No slack: one unlocated row fails the leg.
            Measured live: the result names the run's UTC time
  BOILER    at least one S-id is cited and for every cited row the located quote is NOT on the root
            page of the site that located it (reports/round-58/rowcheck.py `boiler`: root fetched
            live; unfetchable root, source-is-root, or not located all fail): a site-wide footer,
            header, cookie or navigation sentence fails
  RELEVANCE at least one S-id is cited and every cited row's quote shares at least 2 content stems
            with its `teaches` cell, its `teaches` cell copies no 6-word run of the quote, and both
            its `teaches` cell and its quote share at least 2 content stems with the entry lines
            that cite it (reports/round-58/rowcheck.py `relevance` (a)-(d); stems defined there)
  TOPIC     at least one S-id is cited and for every cited row the quote holds at least 1
            NAMING-PLACE window and the page that located it (fetched live again) at least 3
            (reports/round-58/rowcheck.py `topic`; sets NAMING and PLACE, WINDOW 3, PAGE_HITS 3
            there): page-anchored text about something other than place names cannot carry a row
  FRESH     no cited row names a source URL that a corpus/SOURCES.md row below S500 also names
            (URLs compared lower-cased, without scheme, `www.`, trailing `/`, and with a Wayback
            capture prefix removed)
Frozen predicate (the same sentence in reports/round-58/claims.json and in the receipts):
  ACCEPT-C-58: every leg above prints PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
Review-only (no leg; the claims file lists them): the entry's topic; whether each sentence is
carried by its cited row's page beyond the stem overlap (sampled by non-author reviewers);
whether each cited row was opened this round by ordinary means; whether the entry points to
partial owners one-way; whether the ground is uncovered in substance.
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

ENTRY = "corpus/knowledge/linguistics/toponymy-place-names.md"
BASE_LIST = "reports/round-58/base-knowledge-files.txt"
TOTAL = 234
FIRST_SID = 500
LAST_SID = 559
FLOOR = 20
ROWCHECK = "reports/round-58/rowcheck.py"


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
        spec = importlib.util.spec_from_file_location("rowcheck_58", os.path.join(root, ROWCHECK))
        rowcheck = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(rowcheck)
        locator = rowcheck.locator
        entry_text = open(path, encoding="utf-8").read() if os.path.isfile(path) else ""
    except (OSError, SyntaxError, UnicodeDecodeError) as error:
        print(f"ACCEPT_C_INPUT_ERROR {ROWCHECK} {error}", file=sys.stderr)
        return 2
    rowsok = {s: table[s] for s in cited if s in table and len(table[s]) >= 13}
    targets = {s: locator.row_target(cells) for s, cells in rowsok.items()}

    def probe(sid):
        return sid, rowcheck.check_row(rowsok[sid], entry_text)

    with concurrent.futures.ThreadPoolExecutor(8) as pool:
        checked = dict(pool.map(probe, sorted(rowsok)))
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
    for leg in ("LOCATE", "BOILER", "RELEVANCE", "TOPIC"):
        hits = [s for s in cited if s in checked and checked[s][leg][0]]
        misses = [f"{s}: {checked[s][leg][1][:160] if s in checked else 'no row'}" for s in cited if s not in hits]
        legs.append((leg, bool(cited) and len(hits) == len(cited),
                     f"passing={len(hits)} cited={len(cited)} at={stamp} failing={misses}"))

    def norm(url):
        url = re.sub(r"^https?://", "", locator.trim(url).lower())
        url = re.sub(r"^web\.archive\.org/web/[^/]+/(?:https?://)?", "", url)
        return re.sub(r"^www\.", "", url).rstrip("/")

    old = {norm(u) for s, cells in table.items() if int(s[1:]) < FIRST_SID
           for u in locator.URL.findall(cells[2])}
    stale = sorted(s for s in targets if any(norm(u) in old for u in targets[s][0]))
    legs.append(("FRESH", not stale, f"rows_reusing_registry_urls={stale}"))
    for name, ok, detail in legs:
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
    verdict = all(ok for _, ok, _ in legs)
    print(f"ACCEPT-C-58: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
