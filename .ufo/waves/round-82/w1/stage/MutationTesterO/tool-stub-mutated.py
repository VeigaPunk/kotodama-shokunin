#!/usr/bin/env python3
"""Scratch contract stub of tools/check-sources-recheck.py for MutationTesterO's
round-82 mutation probe. Contract-exact EXCEPT one deliberate predicate
mutation: an `NNd` recheck cell means opened + N*30 days (the real contract is
opened + N days). The stub's own --selftest is self-consistent with the mutated
predicate, so the counter's SELFTEST leg stays green and only the counter's
independent QUEUE tally can expose the defect. Every other contract behavior
(exit 2 + RECHECK-ERROR on malformed rows / unparseable cadences, no traceback,
summary + DUE-line shapes, defaults, 0-3 leading spaces on rows) is faithful.
"""
import argparse
import datetime
import re
import sys

ROW = re.compile(r"^\s{0,3}\|\s*S\d{3,}\s*\|")


def queue(text, as_of, window):
    """Return (due, upcoming, on_release, rows, due_lines); raise ValueError on
    a malformed row or an unparseable cadence."""
    due = up = ex = 0
    rows = 0
    due_lines = []
    for line in text.splitlines():
        if not ROW.match(line):
            continue
        rows += 1
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 11:
            raise ValueError("row %d has %d cells" % (rows, len(cells)))
        opened, recheck = cells[8], cells[9]
        if recheck == "on-release":
            ex += 1
            continue
        m = re.fullmatch(r"(\d+)d", recheck)
        try:
            if m:
                # MUTATION (probe): NNd -> opened + N*30 days (contract: +N days)
                d = datetime.date.fromisoformat(opened) + datetime.timedelta(days=int(m.group(1)) * 30)
            else:
                d = datetime.date.fromisoformat(recheck)
        except ValueError:
            raise ValueError("row %d unparseable cadence %r" % (rows, recheck))
        if d <= as_of:
            due += 1
            due_lines.append("DUE %s %s" % (cells[0], d.isoformat()))
        elif d <= as_of + datetime.timedelta(days=window):
            up += 1
    return due, up, ex, rows, due_lines


def selftest():
    ok = 0
    total = 0

    def check(label, cond):
        nonlocal ok, total
        total += 1
        ok += bool(cond)
        if not cond:
            print("stub-selftest FAIL %s" % label)

    hdr = ("| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n"
           "|---|---|---|---|---|---|---|---|---|---|---|\n")
    A = datetime.date(2026, 11, 4)
    W = 90

    t = hdr + "| S001 | a | book | A | s | a | t | queued | 2026-11-04 | on-release | x |\n"
    check("on-release exempt", queue(t, A, W)[:4] == (0, 0, 1, 1))

    t = hdr + "| S002 | a | book | A | s | a | t | mined | 2026-01-01 | 30d | x |\n"
    d0 = datetime.date(2026, 1, 1) + datetime.timedelta(days=900)
    exp = (1, 0, 0, 1) if d0 <= A else ((0, 1, 0, 1) if d0 <= A + datetime.timedelta(days=W) else (0, 0, 0, 1))
    check("NNd stub-encoded arithmetic", queue(t, A, W)[:4] == exp)

    t = hdr + "| S003 | a | book | A | s | a | t | mined | 2020-01-01 | 2026-11-04 | x |\n"
    check("ISO due on as-of boundary", queue(t, A, W)[:4] == (1, 0, 0, 1))

    t = hdr + "| S004 | a | book | A | s | a | t | mined | 2020-01-01 | 2027-02-02 | x |\n"
    check("window edge upcoming", queue(t, A, W)[:4] == (0, 1, 0, 1))

    t = hdr + "| S005 | a | book | A | s | a | t | mined | 2020-01-01 | 2027-02-03 | x |\n"
    check("beyond window not counted", queue(t, A, W)[:4] == (0, 0, 0, 1))

    t = hdr + "| S006 | a | book | A | s | a | t | mined | 2020-01-01 | 90d | x | extra |\n"
    try:
        queue(t, A, W)
        bad = False
    except ValueError:
        bad = True
    check("12-cell row rejected", bad)

    t = hdr + "| S007 | a | book | A | s | a | t | mined | 2020-01-01 | fortnight | x |\n"
    try:
        queue(t, A, W)
        bad = False
    except ValueError:
        bad = True
    check("bad cadence rejected", bad)

    t = hdr + "| S008 | a | book | A | s | a | t | mined | 2020-01-01 | 2026-11-04 | x |\n"
    check("DUE line shape", queue(t, A, W)[4] == ["DUE S008 2026-11-04"])

    print("SELFTEST: PASS (%d checks)" % total)
    return 0 if ok == total else 1


def main():
    ap = argparse.ArgumentParser(prog="check-sources-recheck")
    ap.add_argument("--registry", default="corpus/SOURCES.md")
    ap.add_argument("--as-of")
    ap.add_argument("--window", type=int, default=90)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    try:
        if not a.as_of:
            raise ValueError("--as-of is required outside --selftest")
        as_of = datetime.date.fromisoformat(a.as_of)
        with open(a.registry, encoding="utf-8") as fh:
            text = fh.read()
        due, up, ex, rows, due_lines = queue(text, as_of, a.window)
    except Exception as exc:
        print("RECHECK-ERROR %s" % exc)
        return 2
    for ln in due_lines:
        print(ln)
    print("RECHECK-QUEUE: %d due / %d upcoming / %d on-release / %d rows" % (due, up, ex, rows))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:
        print("RECHECK-ERROR %s" % exc)
        sys.exit(2)
