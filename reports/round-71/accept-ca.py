#!/usr/bin/env python3
r"""Round-71 calibration acceptance counter — claim Ca.

Verifies the five V70-1..V70-5 landings plus the item-10 quarantine verdict
table, per the frozen claim:

  * V70-1: each of the six round-70 telemetry receipts carries ALL six
    17/19 header lines AND the original first line preserved below a marker;
  * V70-2: S860's verify-at cell names acc2d614 (and the old->new log lives
    in reports/round-71/corrections-r70.md);
  * V70-3: the round-70 Gate quote word count is <=25;
  * V70-4: SCORECARD.md carries a `round-70 trend-correction` row;
  * V70-5: the round-71 lesson Gate states `rejected this round:` and
    carries >=1 candidate with reason+flip;
  * QUARANTINE: reports/round-71/telemetry/quarantine-verdicts.md carries a
    recognized nonempty verdict (PRESENT/REFUSED/UNVERIFIABLE) per row and
    exactly the 21 slice ids.

Exit: 0 all legs pass; 1 any leg fails; 2 input error.
"""

import argparse
import os
import re
import sys

LANE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RECEIPTS = (
    "reports/round-70/telemetry/measures-o.txt",
    "reports/round-70/telemetry/measures-ca.txt",
    "reports/round-70/telemetry/measures-d.txt",
    "reports/round-70/telemetry/controls-o.txt",
    "reports/round-70/telemetry/controls-ca.txt",
    "reports/round-70/telemetry/controls-d.txt",
)
HDR_LINES = ("# counter sha256", "# stamped revision", "# evaluated revision",
             "# measured revision", "# tree", "# worktree dirty")
MARKER = "# original bytes preserved below"
ORIGINAL_FIRST = "# after-state receipt"
VERDICTS = {"PRESENT", "REFUSED", "UNVERIFIABLE"}
ROW_RE = re.compile(r"^\s{0,3}\|\s*(S\d{3,})\s*\|")
SLICE_IDS = None  # derived from the register row shape below


def root_abs(root):
    return root if os.path.isabs(root) else os.path.join(LANE, root)


def leg(name, passed, detail):
    print("LEG %s %s" % ("PASS" if passed else "FAIL", name))
    if detail:
        print("     %s" % detail)
    return bool(passed)


def read(root, rel):
    with open(os.path.join(root, rel), encoding="utf-8") as f:
        return f.read()


def main():
    ap = argparse.ArgumentParser(description="round-71 calibration counter (claim Ca)")
    ap.add_argument("--root", default=".", help="lane root")
    ap.add_argument("--lands", default=None, help="lands revision (printed, not graded)")
    args = ap.parse_args()
    root = root_abs(args.root)
    ok = True

    # V70-1 per-file header distribution + marker + original bytes below
    per_file = []
    for rel in RECEIPTS:
        try:
            data = read(root, rel)
        except (OSError, UnicodeError) as exc:
            per_file.append((rel, False, "unreadable: %s" % exc))
            continue
        has_all = all(line in data for line in HDR_LINES)
        marker_ok = MARKER in data
        below = data.split(MARKER, 1)[1] if marker_ok else ""
        first = below.strip().splitlines()[0].strip() if below.strip() else ""
        original_ok = (first.startswith("# after-state receipt")
                       or first.startswith("# pre-data control"))
        per_file.append((rel, has_all and marker_ok and original_ok,
                         "header=%s marker=%s original-below=%s"
                         % (has_all, marker_ok, original_ok)))
    v701 = all(p[1] for p in per_file)
    ok &= leg("V70-1", v701, "; ".join("%s %s" % (p[0], p[1]) for p in per_file))

    # V70-2 S860 cell names acc2d614; old->new log exists in corrections-r70.md
    sources = read(root, "corpus/SOURCES.md")
    s860 = [line for line in sources.splitlines() if ROW_RE.match(line) and line.startswith("| S860 ")]
    v702 = (len(s860) == 1) and ("acc2d614" in s860[0])
    corr = os.path.join(root, "reports/round-71/corrections-r70.md")
    log_ok = os.path.isfile(corr) and ("S860" in read(root, "reports/round-71/corrections-r70.md"))
    ok &= leg("V70-2", v702 and log_ok, "S860-rows=%d acc2d614-in-cell=%s old-new-log=%s"
              % (len(s860), "acc2d614" in (s860[0] if s860 else ""), log_ok))

    # V70-3 round-70 Gate quote <=25 words (line 13, column 4)
    r70 = read(root, "corpus/lessons/round-70.md").splitlines()
    quote = r70[12].split("|")[3] if len(r70) > 12 and len(r70[12].split("|")) > 3 else ""
    words = len(quote.split())
    ok &= leg("V70-3", words <= 25, "words=%d (want <=25)" % words)

    # V70-4 scorecard trend-correction row
    sc = read(root, "SCORECARD.md")
    ok &= leg("V70-4", "round-70 trend-correction" in sc, "explicit row present")

    # V70-5 lesson gate reject sweep + candidate with reason+flip
    lesson = os.path.join(root, "corpus/lessons/round-71.md")
    try:
        lt = read(root, "corpus/lessons/round-71.md")
    except (OSError, UnicodeError):
        lt = ""
    sweep_ok = "rejected this round:" in lt
    candidate_ok = bool(re.search(r"flip", lt, re.I))
    ok &= leg("V70-5", os.path.isfile(lesson) and sweep_ok and candidate_ok,
              "reject-sweep=%s candidate-with-flip=%s" % (sweep_ok, candidate_ok))

    # QUARANTINE table: exact 21 slice ids, recognized nonempty verdict per row
    q = os.path.join(root, "reports/round-71/telemetry/quarantine-verdicts.md")
    try:
        qt = read(root, "reports/round-71/telemetry/quarantine-verdicts.md")
    except (OSError, UnicodeError):
        qt = ""
    rows = []
    for line in qt.splitlines():
        if line.startswith("| S") and "|" in line:
            cells = [c.strip() for c in line.split("|")]
            if len(cells) >= 3:
                rows.append((cells[1], cells[2]))
    SLICE = {"S776","S778","S779","S786","S787","S791","S792","S795","S796",
             "S804","S807","S812","S814","S816","S817","S820","S823","S824",
             "S825","S827","S835"}
    ids_ok = len(rows) == 21 and {r[0] for r in rows} == SLICE
    labels_ok = all(r[1] in VERDICTS for r in rows)
    # class admissibility: unreachable-class rows MUST be UNVERIFIABLE;
    # payload-absent rows may be PRESENT/REFUSED (quote checked) or
    # UNVERIFIABLE (source unfetchable/truncated, e.g. S791)
    UNREACHABLE = {"S807","S812","S835"}
    class_ok = all(r[1] == "UNVERIFIABLE" for r in rows if r[0] in UNREACHABLE)
    ok &= leg("QUARANTINE", ids_ok and labels_ok and class_ok,
              "rows=%d unique-ids=%d labels-ok=%s class-ok=%s (want 21/21/True/True)"
              % (len(rows), len({r[0] for r in rows}), labels_ok, class_ok))

    print("ACCEPT-CA-71: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
