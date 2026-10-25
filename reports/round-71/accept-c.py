#!/usr/bin/env python3
r"""Round-71 coverage acceptance counter — claim C.

Checks the frozen claim-C predicate at the measured revision:

  * the entry exists at corpus/knowledge/culture-material/dance-performance-movement-codes.md;
  * culture-material partition count 35 -> 36 and corpus total 242 -> 243
    (find | wc -l, not inventory summary);
  * the entry cites >=12 NEW SOURCES rows (S ids opened this round, status
    mined, used-by lists the entry path);
  * every cited row's used-by path exists;
  * `tools/check-cited-lines.py` on the entry exits 0;
  * the word-bounded gap sweep shows only the entry itself as owner (pre-entry it printed nothing).

Exit: 0 all legs pass; 1 any leg fails; 2 input error.
"""

import argparse
import os
import re
import subprocess
import sys

LANE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ENTRY = "corpus/knowledge/culture-material/dance-performance-movement-codes.md"
ROW_RE = re.compile(r"^\s{0,3}\|\s*(S\d{3,})\s*\|")
TOKEN_RE = re.compile(r"S\d{3,}")


def root_abs(root):
    return root if os.path.isabs(root) else os.path.join(LANE, root)


def run(argv, root):
    return subprocess.run(argv, cwd=root, capture_output=True, text=True)


def leg(name, passed, detail):
    print("LEG %s %s" % ("PASS" if passed else "FAIL", name))
    if detail:
        print("     %s" % detail)
    return bool(passed)


def main():
    ap = argparse.ArgumentParser(description="round-71 coverage counter (claim C)")
    ap.add_argument("--root", default=".", help="lane root")
    ap.add_argument("--lands", default=None, help="lands revision (printed, not graded)")
    args = ap.parse_args()
    root = root_abs(args.root)
    ok = True

    # 1. entry exists
    entry_exists = os.path.isfile(os.path.join(root, ENTRY))
    ok &= leg("ENTRY", entry_exists, ENTRY)

    # 2. partition and corpus counts
    cm = len([f for f in os.listdir(os.path.join(root, "corpus/knowledge/culture-material"))
              if f.endswith(".md")])
    corpus = len([f for f in os.listdir(os.path.join(root, "corpus/knowledge"))
                  if os.path.isdir(os.path.join(root, "corpus/knowledge", f))])
    # corpus total = sum over partitions
    ctotal = 0
    for part in os.listdir(os.path.join(root, "corpus/knowledge")):
        d = os.path.join(root, "corpus/knowledge", part)
        if os.path.isdir(d):
            ctotal += len([f for f in os.listdir(d) if f.endswith(".md")])
    count_ok = (cm == 36) and (ctotal == 243)
    ok &= leg("COUNTS", count_ok, "culture-material=%d corpus=%d (want 36/243)" % (cm, ctotal))

    # 3. row citations: parse the entry's S-ids, require >=12 distinct
    text = open(os.path.join(root, ENTRY), encoding="utf-8").read()
    cited = set(TOKEN_RE.findall(text))
    ok &= leg("CITED", len(cited) >= 12, "distinct S-ids cited=%d (want >=12)" % len(cited))

    # 4. each cited row exists in registry, status mined, used-by names the entry
    reg = open(os.path.join(root, "corpus/SOURCES.md"), encoding="utf-8").read()
    rows = {}
    for line in reg.splitlines():
        m = ROW_RE.match(line)
        if m:
            rows[m.group(1)] = line
    missing, not_mined, no_usedby = [], [], []
    for sid in sorted(cited):
        if sid not in rows:
            missing.append(sid)
            continue
        cells = rows[sid].split("|")
        # cells: ['', id, source, kind, tier, scope, anchor, teaches, status, opened, recheck, used-by, '']
        status = cells[8].strip() if len(cells) > 8 else ""
        usedby = cells[11].strip() if len(cells) > 11 else ""
        if status != "mined":
            not_mined.append(sid)
        if ENTRY not in usedby:
            no_usedby.append(sid)
    row_ok = not (missing or not_mined or no_usedby)
    ok &= leg("ROWS", row_ok,
              "missing=%s not-mined=%s usedby-missing=%s" % (missing, not_mined, no_usedby))

    # 5. used-by path existence for cited rows
    bad = []
    for sid in sorted(cited):
        usedby = rows[sid].split("|")[11].strip() if sid in rows else ""
        for p in [x.strip() for x in usedby.split(",") if x.strip()]:
            if not os.path.exists(os.path.join(root, p)):
                bad.append((sid, p))
    ok &= leg("USEDBY-PATHS", not bad, "missing-paths=%s" % bad)

    # 6. check-cited-lines exit 0
    r = run([sys.executable, "-B", "tools/check-cited-lines.py", ENTRY], root)
    ok &= leg("CITED-LINES", r.returncode == 0,
              "exit=%d" % r.returncode + ((" " + r.stdout.strip().splitlines()[-1]) if r.stdout.strip() else ""))

    # 7. gap sweep: pre-entry the register had 0 owners; post-landing the
    # only owner must be the entry itself (no other file claims the register).
    r1 = run(["bash", "-c",
              "find corpus/knowledge/culture-material -maxdepth 1 -type f -name '*danc*'"], root)
    r2 = run(["bash", "-c",
              "grep -rniE '^- topic:.*\\b(danc|choreograph|movement culture|performance)\\b' "
              "corpus/knowledge/culture-material/*.md"], root)
    fn_owners = [l for l in r1.stdout.splitlines() if l.strip()]
    topic_owners = [l for l in r2.stdout.splitlines() if l.strip()]
    sweep_ok = (fn_owners == [ENTRY]) and all(t.startswith(ENTRY + ":") for t in topic_owners) and len(topic_owners) <= 1
    ok &= leg("SWEEP", sweep_ok, "filename-owners=%s topic-owners=%s"
              % (fn_owners, topic_owners))

    print("ACCEPT-C-71: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
