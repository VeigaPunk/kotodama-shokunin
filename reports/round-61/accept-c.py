#!/usr/bin/env python3
r"""Round-61 claim C acceptance (adapted from reports/round-57/accept-c.py: entry path, totals, C's
reserved block, LOCATE share 1.0, and four new legs LINES, TOPIC, LINK, COPY, OPENED). Run from the
lane root:

  python3 -B reports/round-61/accept-c.py [--root DIR]

One leg per mechanical clause of claim C (reports/round-61/claims.json), each printed with PASS or FAIL:
  SET       the files under corpus/knowledge (every file, not only *.md) are exactly the 235 paths in
            reports/round-61/base-knowledge-files.txt plus ENTRY: count 236, added [ENTRY], removed []
  SWEEP     python3 -B reports/round-28/readme/sweep.py exits 0 and prints `rows 236 files 236` and
            `missing_from_index 0 []` (exit status read directly, no pipe)
  FLOOR     the entry cites at least 20 distinct S-ids
  RANGE     every cited S-id lies in claim C's reserved block S652-S699 and is exactly one
            corpus/SOURCES.md row of 13 cells; the entry carries no S-id range notation
  STATUS    every cited row has status `mined`
  OPENED    every cited row's `opened` cell is 2026-10-23
  USEDBY    every cited row names ENTRY as one whole comma- or semicolon-separated used-by item
  ACCESS    python3 -B tools/check-source-access.py exits 0 (QUALITY criterion 10)
  LINES     one row, one clause: every entry line that carries an S-id is a bullet line (`- ` after
            optional indentation), carries exactly one distinct S-id, and is not a table row or heading
  TOPIC     every cited row's anchor quote (first double-quoted span of its `anchor` cell), normalised
            as the locator does, contains at least one word of the frozen footwear lexicon TOPIC_WORDS
  LINK      every S-id-bearing entry line shares at least 3 distinct normalised words of 4 or more
            characters, outside STOP, with its cited row's anchor quote
  COPY      no S-id-bearing entry line repeats more than 12 consecutive normalised words of its cited
            row's anchor quote (a quote pasted as the line is not a restatement)
  LOCATE    every cited row (share 1.0) is LOCATED by reports/round-61/reopen-quote.py (row mode: the
            http(s) URLs of the row's `source` cell, at most four, in order, fetched live by an ordinary
            GET; a Wayback capture listed in the cell is one of those URLs; the match rule is in that
            file's docstring). A fabricated quote, a search/echo/code-host/self-named URL, or a fetch
            error on every listed URL is not located. Measured live; the result names the run's UTC time
  FRESH     no cited row names a source URL that a corpus/SOURCES.md row below S652 also names (URLs
            compared lower-cased, without scheme, `www.`, trailing `/`, Wayback prefix removed)
Frozen predicate (the same sentence in reports/round-61/claims.json and in every receipt):
  ACCEPT-C-61: every leg above prints PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
Review-only (no leg; claims.json lists them): whether each line's wording is carried by its cited
page beyond the shared words; the entry's craft usability; one-way pointing to partial owners; the
lore handoff.
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

ENTRY = "corpus/knowledge/culture-material/footwear-codes-terminology.md"
BASE_LIST = "reports/round-61/base-knowledge-files.txt"
TOTAL = 236
FIRST_SID = 652
LAST_SID = 699
FLOOR = 20
LOCATOR = "reports/round-61/reopen-quote.py"
SHARE = 1.0
OPENED = "2026-10-23"
LINK_MIN = 3
COPY_MAX = 12
SID = re.compile(r"\bS\d{3,}\b")
TOPIC_WORDS = frozenset("""
shoe shoes shod unshod barefoot footwear sandal sandals boot boots clog clogs moccasin moccasins
slipper slippers heel heels sole soles insole insoles geta zori zōri waraji tabi chopine chopines
poulaine poulaines patten pattens sabot sabots lapti opanak opanci caliga caligae kamik kamiks kamiit
mukluk mukluks paduka padukas shoemaker shoemakers shoemaking cordwainer cordwainers cobbler cobblers
footgear brogue brogues buskin buskins talaria
""".split())
STOP = frozenset("""
that this with from were which have been their they them there these those what when where while
into onto upon than then also only such some more most other over under about after before during
between because could would should shall will your yours ours here very much many each every both
either neither same like just even ever made make makes been being does done have having
""".split())


def run(root, argv):
    try:
        return subprocess.run(argv, cwd=root, capture_output=True, text=True, timeout=300)
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f"ACCEPT_C_INPUT_ERROR {' '.join(argv)} {error}", file=sys.stderr)
        return None


def longest_run(a, b):
    """Length of the longest run of consecutive words shared by word lists a and b."""
    best, prev = 0, [0] * (len(b) + 1)
    for x in a:
        cur = [0] * (len(b) + 1)
        for j, y in enumerate(b, 1):
            if x == y:
                cur[j] = prev[j - 1] + 1
                best = max(best, cur[j])
        prev = cur
    return best


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
    try:
        spec = importlib.util.spec_from_file_location("reopen_quote", os.path.join(root, LOCATOR))
        locator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(locator)
    except (OSError, SyntaxError) as error:
        print(f"ACCEPT_C_INPUT_ERROR {LOCATOR} {error}", file=sys.stderr)
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
    cited, table, rows_per_id, spans, lines = [], {}, {}, [], []
    try:
        if os.path.isfile(path):
            text = open(path, encoding="utf-8").read()
            cited = sorted(set(re.findall(r"\bS\d{3}\b", text)) | set(SID.findall(text)))
            spans = re.findall(r"\bS\d{3}\s*(?:[-‐‑‒–—―−~…]|\.{2,3}|to|through|thru)\s*S?\d{2,3}\b", text)
            lines = [(n, l) for n, l in enumerate(text.splitlines(), 1) if SID.search(l)]
        for line in open(os.path.join(root, "corpus/SOURCES.md"), encoding="utf-8"):
            row = re.match(r"^\|\s*(S\d{3,})\s*\|", line)
            if row:
                table[row.group(1)] = line.split("|")
                rows_per_id[row.group(1)] = rows_per_id.get(row.group(1), 0) + 1
    except (OSError, UnicodeDecodeError) as error:
        print(f"ACCEPT_C_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    legs.append(("FLOOR", len(cited) >= FLOOR, f"cited={len(cited)} floor={FLOOR}"))
    range_bad = [s for s in cited if not FIRST_SID <= int(s[1:]) <= LAST_SID
                 or rows_per_id.get(s, 0) != 1 or len(table[s]) != 13]
    legs.append(("RANGE", not range_bad and not spans, f"bad={range_bad} range_notation={spans}"))
    ok_rows = [s for s in cited if s not in range_bad]
    status_bad = [f"{s}:{table[s][8].strip()}" for s in ok_rows if table[s][8].strip() != "mined"]
    legs.append(("STATUS", not status_bad, f"bad={status_bad}"))
    opened_bad = [f"{s}:{table[s][9].strip()}" for s in ok_rows if table[s][9].strip() != OPENED]
    legs.append(("OPENED", not opened_bad, f"bad={opened_bad}"))
    used_bad = [s for s in ok_rows if ENTRY not in [u.strip() for u in re.split(r"[,;]", table[s][11])]]
    legs.append(("USEDBY", not used_bad, f"bad={used_bad}"))
    access = run(root, [sys.executable, "-B", "tools/check-source-access.py"])
    if access is None:
        return 2
    legs.append(("ACCESS", access.returncode == 0, f"exit={access.returncode} "
                 f"{(access.stdout.strip().splitlines() or ['?'])[-1]}"))
    lines_bad = []
    for n, l in lines:
        ids = set(SID.findall(l))
        if not re.match(r"^\s*- ", l) or len(ids) != 1:
            lines_bad.append(f"{n}:{','.join(sorted(ids))}")
    legs.append(("LINES", bool(lines) and not lines_bad, f"cited_lines={len(lines)} bad={lines_bad}"))
    targets = {s: locator.row_target(table[s]) for s in ok_rows}
    topic_bad = [s for s in ok_rows if not set(locator.normalise(targets[s][1]).split()) & TOPIC_WORDS]
    legs.append(("TOPIC", bool(ok_rows) and not topic_bad, f"rows={len(ok_rows)} bad={topic_bad}"))
    link_bad, copy_bad = [], []
    for n, l in lines:
        ids = set(SID.findall(l))
        if len(ids) != 1 or next(iter(ids)) not in targets:
            link_bad.append(f"{n}:no-row")
            copy_bad.append(f"{n}:no-row")
            continue
        quote = locator.normalise(targets[next(iter(ids))][1]).split()
        words = [w for w in locator.normalise(SID.sub(" ", l)).split()]
        shared = {w for w in words if len(w) >= 4 and w not in STOP} & set(quote)
        if len(shared) < LINK_MIN:
            link_bad.append(f"{n}:{len(shared)}")
        run_len = longest_run(words, quote)
        if run_len > COPY_MAX:
            copy_bad.append(f"{n}:{run_len}")
    legs.append(("LINK", bool(lines) and not link_bad, f"min={LINK_MIN} bad={link_bad}"))
    legs.append(("COPY", bool(lines) and not copy_bad, f"max={COPY_MAX} bad={copy_bad}"))

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
    print(f"ACCEPT-C-61: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
