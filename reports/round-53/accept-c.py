#!/usr/bin/env python3
"""Round-53 claim C acceptance. Run from the lane root:

  python3 -B reports/round-53/accept-c.py [--root DIR]

Legs, each printed with PASS or FAIL:
  COUNT   find corpus/knowledge -name '*.md' counts exactly 229
  ENTRY   corpus/knowledge/linguistics/gesture-co-speech-pointing.md exists
  SWEEP   python3 -B reports/round-28/readme/sweep.py, run on its own, exits 0 and prints
          `rows 229 files 229` and `missing_from_index 0 []` (the README index row exists)
  SIDS    the entry cites at least one S-id; every S-id it cites is S187 or above, is a
          corpus/SOURCES.md row with status `mined`, and names the entry in its used-by cell
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
The sweep's own exit code is read directly (no pipe), so a missing README row fails SWEEP.
"""
import argparse
import os
import re
import subprocess
import sys

ENTRY = "corpus/knowledge/linguistics/gesture-co-speech-pointing.md"
TOTAL = 229
FIRST_SID = 187


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    legs = []
    count = sum(1 for d, _, fs in os.walk(os.path.join(root, "corpus/knowledge"))
                for f in fs if f.endswith(".md"))
    legs.append(("COUNT", count == TOTAL, f"knowledge_files={count} required={TOTAL}"))
    path = os.path.join(root, ENTRY)
    exists = os.path.isfile(path)
    legs.append(("ENTRY", exists, ENTRY))
    try:
        sweep = subprocess.run([sys.executable, "-B", "reports/round-28/readme/sweep.py"],
                               cwd=root, capture_output=True, text=True, timeout=300)
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f"ACCEPT_C_INPUT_ERROR sweep {error}", file=sys.stderr)
        return 2
    out = sweep.stdout
    rows = re.search(r"^rows (\d+) files (\d+)$", out, re.M)
    missing = re.search(r"^missing_from_index (\d+) (.*)$", out, re.M)
    sweep_ok = (sweep.returncode == 0 and rows is not None and missing is not None
                and int(rows.group(1)) == TOTAL and int(rows.group(2)) == TOTAL
                and int(missing.group(1)) == 0)
    legs.append(("SWEEP", sweep_ok,
                 f"exit={sweep.returncode} {rows.group(0) if rows else 'rows ?'} "
                 f"{missing.group(0) if missing else 'missing_from_index ?'}"))
    bad, cited = ["entry absent"], []
    if exists:
        try:
            text = open(path, encoding="utf-8").read()
            table = {}
            for line in open(os.path.join(root, "corpus/SOURCES.md"), encoding="utf-8"):
                if re.match(r"^\| S\d{3} ", line):
                    cells = line.split("|")
                    table[cells[1].strip()] = cells
        except OSError as error:
            print(f"ACCEPT_C_INPUT_ERROR {error}", file=sys.stderr)
            return 2
        cited = sorted(set(re.findall(r"\bS\d{3}\b", text)))
        bad = []
        for sid in cited:
            cells = table.get(sid)
            if int(sid[1:]) < FIRST_SID:
                bad.append(f"{sid}:below-S{FIRST_SID}")
            elif cells is None or len(cells) < 12:
                bad.append(f"{sid}:no-row")
            elif cells[8].strip() != "mined":
                bad.append(f"{sid}:status-{cells[8].strip()}")
            elif ENTRY not in cells[11]:
                bad.append(f"{sid}:used-by")
        if not cited:
            bad.append("no S-id cited")
    legs.append(("SIDS", not bad, f"cited={len(cited)} bad={bad}"))
    for name, ok, detail in legs:
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
    return 0 if all(ok for _, ok, _ in legs) else 1


if __name__ == "__main__":
    sys.exit(main())
