#!/usr/bin/env python3
r"""Recheck-cadence auditor for the SOURCES.md registry (kotodama round 82, claim O).

Every registry row promises a recheck cadence in its `recheck` cell. This
tool turns each promise into a due date as of one audit day:

  NNd         due date = opened + N days
  ISO date    due date = that date itself
  on-release  exempt; never due

Usage:
  python3 tools/check-sources-recheck.py [--registry PATH] --as-of YYYY-MM-DD [--window N]
  python3 tools/check-sources-recheck.py --selftest

--registry defaults to corpus/SOURCES.md relative to the current working
directory (the tool never assumes a repo root). --window is the upcoming
horizon in days, default 90. A parsed row is

  due         when due_date <= as-of
  upcoming    when as-of < due_date <= as-of + window days
  on-release  when the cadence is exempt

Registry rows are lines matching the census grammar ^\s{0,3}\|\s*S\d{3,}\s*\|;
after stripping the outer pipes a row must split on `|` into exactly 11 cells
(id, source, kind, tier, scope, anchor, teaches, status, opened, recheck,
used-by). Cells 0 (id), 8 (opened) and 9 (recheck) drive the audit; any other
cell count is an error.

Stdout: one `DUE <id> <iso-date>` line per due row in file order, then
exactly one summary line

  RECHECK-QUEUE: <due> due / <upcoming> upcoming / <on-release> on-release / <rows> rows

where rows counts parsed rows. Any input or parse problem -- missing or
unreadable registry, bad --as-of, wrong cell count, unparseable opened or
cadence cell -- prints a single `RECHECK-ERROR <detail>` line on stdout and
exits 2 with no traceback.

--selftest builds throwaway registries under TMPDIR and runs the contract
cases; it prints `SELFTEST: PASS (<n> checks)` and exits 0 only when every
check passes.

Read-only; stdlib only; the output depends only on the bytes read.
"""

from __future__ import annotations

import argparse
import datetime
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROW_RE = re.compile(r"^\s{0,3}\|\s*S\d{3,}\s*\|")
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DAYS_RE = re.compile(r"(\d{1,4})d")
CELLS_EXPECTED = 11
ID_CELL = 0
OPENED_CELL = 8
RECHECK_CELL = 9
DEFAULT_REGISTRY = os.path.join("corpus", "SOURCES.md")
DEFAULT_WINDOW = 90
HEADER = ("| id | source | kind | tier | scope | anchor | teaches | status | "
          "opened | recheck | used-by |")
SCRIPT = os.path.abspath(__file__)


class RecheckError(Exception):
    """A condition that must exit 2 with a RECHECK-ERROR line."""


class Parser(argparse.ArgumentParser):
    def error(self, message):
        print(f"RECHECK-ERROR argument: {message}")
        raise SystemExit(2)


def build_parser():
    parser = Parser(
        prog="check-sources-recheck.py",
        description="Audit SOURCES.md recheck cadences as of one audit day.")
    parser.add_argument("--registry", default=DEFAULT_REGISTRY,
                        help="registry path (default: corpus/SOURCES.md relative to CWD)")
    parser.add_argument("--as-of", default=None, metavar="YYYY-MM-DD",
                        help="audit date (required unless --selftest)")
    parser.add_argument("--window", type=int, default=DEFAULT_WINDOW, metavar="N",
                        help="upcoming horizon in days (default: 90)")
    parser.add_argument("--selftest", action="store_true",
                        help="run contract selftest on throwaway fixtures")
    return parser


def parse_iso_date(text, what):
    if not ISO_RE.fullmatch(text):
        raise RecheckError(f"{what} {text!r} is not an ISO date (YYYY-MM-DD)")
    try:
        return datetime.date.fromisoformat(text)
    except ValueError:
        raise RecheckError(f"{what} {text!r} is not a real calendar date") from None


def parse_row(line, lineno):
    if not ROW_RE.match(line):
        return None
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    cells = [cell.strip() for cell in body.split("|")]
    if len(cells) != CELLS_EXPECTED:
        raise RecheckError(
            f"line {lineno}: row has {len(cells)} cells, expected {CELLS_EXPECTED}")
    return cells


def due_date(row_id, opened, cadence):
    if cadence == "on-release":
        return None
    match = DAYS_RE.fullmatch(cadence)
    if match:
        return opened + datetime.timedelta(days=int(match.group(1)))
    if ISO_RE.fullmatch(cadence):
        return parse_iso_date(cadence, f"row {row_id}: recheck")
    raise RecheckError(f"row {row_id}: unparseable recheck cadence {cadence!r}")


def read_registry(path):
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return handle.read()
    except UnicodeDecodeError as exc:
        raise RecheckError(f"registry {path}: not valid UTF-8: {exc}") from None
    except OSError as exc:
        raise RecheckError(f"registry {path}: {exc.strerror or exc}") from None


def audit(path, as_of, window):
    text = read_registry(path)
    due = []
    upcoming = exempt = rows = 0
    for lineno, line in enumerate(text.splitlines(), 1):
        cells = parse_row(line, lineno)
        if cells is None:
            continue
        rows += 1
        row_id = cells[ID_CELL]
        opened = parse_iso_date(cells[OPENED_CELL], f"row {row_id}: opened")
        when = due_date(row_id, opened, cells[RECHECK_CELL])
        if when is None:
            exempt += 1
        elif when <= as_of:
            due.append((row_id, when))
        elif when <= as_of + datetime.timedelta(days=window):
            upcoming += 1
    lines = [f"DUE {row_id} {when.isoformat()}" for row_id, when in due]
    lines.append(summary(len(due), upcoming, exempt, rows))
    return lines


def summary(due, upcoming, exempt, rows):
    return (f"RECHECK-QUEUE: {due} due / {upcoming} upcoming / "
            f"{exempt} on-release / {rows} rows")


def row(row_id, opened, recheck):
    cells = [row_id, "Selftest source", "book", "A", "scope", "anchor",
             "teaches", "mined", opened, recheck, "-"]
    return "| " + " | ".join(cells) + " |"


def write_registry(root, name, rows):
    path = os.path.join(root, name)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("# selftest registry\n\n")
        handle.write(HEADER + "\n")
        handle.write("|---" * CELLS_EXPECTED + "|\n")
        for line in rows:
            handle.write(line + "\n")
    return path


def run_tool(args, cwd):
    return subprocess.run([sys.executable, SCRIPT, *args], cwd=cwd,
                          capture_output=True, text=True)


def expect_error(checks, name, proc, needle):
    lines = proc.stdout.strip().splitlines()
    ok = (proc.returncode == 2
          and len(lines) == 1
          and lines[0].startswith("RECHECK-ERROR ")
          and needle in lines[0]
          and "Traceback" not in proc.stdout + proc.stderr)
    checks.append(ok)
    if not ok:
        print(f"SELFTEST: FAIL {name}: rc={proc.returncode} "
              f"stdout={proc.stdout!r} stderr={proc.stderr!r}")


def expect_output(checks, name, proc, want):
    ok = (proc.returncode == 0
          and proc.stdout.splitlines() == want
          and "Traceback" not in proc.stderr)
    checks.append(ok)
    if not ok:
        print(f"SELFTEST: FAIL {name}: rc={proc.returncode} "
              f"stdout={proc.stdout!r} stderr={proc.stderr!r}")


def selftest():
    checks = []
    root = tempfile.mkdtemp(prefix="recheck-selftest-")
    try:
        # 1. Clean mixed registry: NNd due, NNd upcoming, ISO exact as-of (due),
        #    ISO beyond the horizon, on-release, NNd on the window boundary,
        #    NNd long past. DUE lines in file order, exact summary.
        mixed = write_registry(root, "mixed.md", [
            row("S901", "2026-08-06", "90d"),         # due 2026-11-04 == as-of
            row("S902", "2026-10-01", "90d"),         # due 2026-12-30 -> upcoming
            row("S903", "2025-01-01", "2026-11-04"),  # ISO == as-of -> due
            row("S904", "2025-06-01", "2027-03-01"),  # beyond the horizon
            row("S905", "2026-01-01", "on-release"),  # exempt
            row("S906", "2026-11-04", "90d"),         # due 2027-02-02 == horizon -> upcoming
            row("S907", "2025-12-25", "14d"),         # due 2026-01-08 -> due
        ])
        expect_output(checks, "mixed registry",
                      run_tool(["--registry", mixed, "--as-of", "2026-11-04",
                                "--window", "90"], root),
                      ["DUE S901 2026-11-04",
                       "DUE S903 2026-11-04",
                       "DUE S907 2026-01-08",
                       "RECHECK-QUEUE: 3 due / 2 upcoming / 1 on-release / 7 rows"])

        # 2. Window boundary: due exactly as-of+window counts as upcoming.
        edge = write_registry(root, "edge.md", [row("S910", "2026-11-04", "90d")])
        expect_output(checks, "window boundary inside",
                      run_tool(["--registry", edge, "--as-of", "2026-11-04",
                                "--window", "90"], root),
                      ["RECHECK-QUEUE: 0 due / 1 upcoming / 0 on-release / 1 rows"])

        # 3. One day shorter window pushes the same row past the horizon.
        expect_output(checks, "window boundary outside",
                      run_tool(["--registry", edge, "--as-of", "2026-11-04",
                                "--window", "89"], root),
                      ["RECHECK-QUEUE: 0 due / 0 upcoming / 0 on-release / 1 rows"])

        # 4. 12-cell row -> exit 2, labelled.
        wide = write_registry(root, "wide.md",
                              [row("S911", "2026-01-01", "30d")[:-1] + "| extra |"])
        expect_error(checks, "12-cell row",
                     run_tool(["--registry", wide, "--as-of", "2026-11-04"], root),
                     "cells")

        # 5. Any other wrong count (short row) -> exit 2, labelled.
        narrow = write_registry(root, "narrow.md", ["| S912 | x | y |"])
        expect_error(checks, "short row cell count",
                     run_tool(["--registry", narrow, "--as-of", "2026-11-04"], root),
                     "cells")

        # 6. Unparseable cadence -> exit 2, labelled.
        cad = write_registry(root, "cad.md", [row("S913", "2026-01-01", "weekly")])
        expect_error(checks, "unparseable cadence",
                     run_tool(["--registry", cad, "--as-of", "2026-11-04"], root),
                     "cadence")

        # 7. Unparseable opened cell -> exit 2, labelled.
        opn = write_registry(root, "opn.md", [row("S914", "recently", "30d")])
        expect_error(checks, "unparseable opened",
                     run_tool(["--registry", opn, "--as-of", "2026-11-04"], root),
                     "opened")

        # 8. Missing registry file -> exit 2, labelled.
        missing = os.path.join(root, "absent.md")
        expect_error(checks, "missing registry",
                     run_tool(["--registry", missing, "--as-of", "2026-11-04"], root),
                     missing)

        # 9. Registry path is a directory (unreadable as a file) -> exit 2.
        expect_error(checks, "registry is a directory",
                     run_tool(["--registry", root, "--as-of", "2026-11-04"], root),
                     "registry")

        # 10. Bad --as-of -> exit 2, labelled.
        good = write_registry(root, "good.md", [row("S915", "2026-01-01", "30d")])
        expect_error(checks, "bad --as-of",
                     run_tool(["--registry", good, "--as-of", "2026-11-4"], root),
                     "--as-of")

        # 11. Missing required --as-of without --selftest -> exit 2.
        expect_error(checks, "missing --as-of",
                     run_tool(["--registry", good], root),
                     "--as-of")

        # 12. Population check: appending a non-due row leaves due and
        #     upcoming unchanged; only rows moves.
        base = write_registry(root, "pop1.md", [row("S916", "2026-11-04", "90d")])
        grown = write_registry(root, "pop2.md", [
            row("S916", "2026-11-04", "90d"),
            row("S917", "2020-01-01", "2030-01-01"),  # non-due, far future
        ])
        first = run_tool(["--registry", base, "--as-of", "2026-11-04"], root)
        second = run_tool(["--registry", grown, "--as-of", "2026-11-04"], root)
        ok = (first.returncode == 0 and second.returncode == 0
              and first.stdout.splitlines() ==
              ["RECHECK-QUEUE: 0 due / 1 upcoming / 0 on-release / 1 rows"]
              and second.stdout.splitlines() ==
              ["RECHECK-QUEUE: 0 due / 1 upcoming / 0 on-release / 2 rows"])
        checks.append(ok)
        if not ok:
            print(f"SELFTEST: FAIL population check: rc={first.returncode}/"
                  f"{second.returncode} stdout={first.stdout!r}/{second.stdout!r}")

        # 13. Leading-space tolerance (2 spaces) and the default --window 90.
        lead = write_registry(root, "lead.md", ["  " + row("S918", "2026-11-04", "90d")])
        expect_output(checks, "leading spaces + default window",
                      run_tool(["--registry", lead, "--as-of", "2026-11-04"], root),
                      ["RECHECK-QUEUE: 0 due / 1 upcoming / 0 on-release / 1 rows"])

        if all(checks):
            print(f"SELFTEST: PASS ({len(checks)} checks)")
            return 0
        print(f"SELFTEST: FAIL ({len(checks) - sum(checks)} of {len(checks)} checks failed)")
        return 1
    finally:
        shutil.rmtree(root, ignore_errors=True)


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        if args.selftest:
            return selftest()
        if args.as_of is None:
            print("RECHECK-ERROR argument: --as-of is required unless --selftest")
            return 2
        as_of = parse_iso_date(args.as_of, "--as-of")
        for line in audit(args.registry, as_of, args.window):
            print(line)
        return 0
    except RecheckError as exc:
        print(f"RECHECK-ERROR {exc}")
        return 2
    except Exception as exc:  # contract: never a traceback
        print(f"RECHECK-ERROR unexpected {type(exc).__name__}: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
