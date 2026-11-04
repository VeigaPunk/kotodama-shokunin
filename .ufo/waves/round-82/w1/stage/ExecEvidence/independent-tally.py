#!/usr/bin/env python3
"""ExecEvidence independent tally for the r82 recheck-cadence receipt.

Implemented from the round contract ONLY (not from the draft tool):
11-cell Registry rows, 0-3 leading spaces; cadence NNd -> opened+NN days,
ISO date -> itself, on-release -> exempt.  due = due_date <= as-of;
upcoming = as-of < due_date <= as-of + window; on-release exempt count;
rows = rows parsed.  Prints the RECHECK-QUEUE line plus DUE lines.
"""
import re
import sys
from datetime import date, timedelta

ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DAYS = re.compile(r"^(\d+)d$")


def main(argv):
    registry_path, as_of_s, window = argv[1], argv[2], int(argv[3])
    as_of = date.fromisoformat(as_of_s)
    horizon = as_of + timedelta(days=window)
    with open(registry_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    due, upcoming, on_release, rows = 0, 0, 0, 0
    due_lines = []
    problems = []
    for lineno, line in enumerate(lines, 1):
        if "|" not in line:
            continue
        stripped = line.lstrip(" ")
        if len(line) - len(stripped) > 3:
            problems.append(f"line {lineno}: leading spaces > 3")
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        # markdown rows like "| a | b |" -> strip yields empty ends; rebuild
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped[1:-1].split("|")]
        if not cells or cells[0] == "id" or set(cells[0]) <= {"-"}:
            continue  # header / separator
        rows += 1
        if len(cells) != 11:
            problems.append(
                f"line {lineno}: {len(cells)} cells (row id {cells[0]!r})"
            )
            continue
        rid, opened_s, cadence = cells[0], cells[8], cells[9]
        if cadence == "on-release":
            on_release += 1
            continue
        m = DAYS.match(cadence)
        if m:
            opened = date.fromisoformat(opened_s)
            due_date = opened + timedelta(days=int(m.group(1)))
        elif ISO.match(cadence):
            due_date = date.fromisoformat(cadence)
        else:
            problems.append(f"line {lineno}: unparseable cadence {cadence!r}")
            continue
        if due_date <= as_of:
            due += 1
            due_lines.append(f"DUE {rid} {due_date.isoformat()}")
        elif due_date <= horizon:
            upcoming += 1

    print(
        f"RECHECK-QUEUE: {due} due / {upcoming} upcoming / "
        f"{on_release} on-release / {rows} rows"
    )
    for d in due_lines:
        print(d)
    if problems:
        print("PROBLEMS:", file=sys.stderr)
        for p in problems:
            print("  " + p, file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv)
