#!/usr/bin/env python3
"""X45 — lessons-index *pointer and prose* audit (round 25), read-only.

The sibling C seat's tool (`reports/round-25/audit/c31-lessons-index-audit.py`)
answers four structural questions about `corpus/lessons/README.md`: rows==files,
owners resolve, formats documented, pins re-derived. It deliberately does **not**
read the index's `disposition pointer` column, and it does not compare the
index's prose claims about the partition against the live tree. This tool
answers those two questions:

  X45-P1  every path a disposition pointer names resolves, unless the pointer
          explicitly says the path was never filed.
  X45-P2  the index's prose counts ("N of M" contributing rows, declared file
          totals) equal the measurement taken from the same bytes.
  X45-P3  cross-consistency: every open-question id a §2 row claims to carry
          exists as a §4 queue row, and every §4 row is claimed by some §2 row.

Stdlib only. Opens no file for writing; `--json` is a stdout receipt.

    export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
    python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py --selftest
    python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py
    python3 -B reports/round-25/audit/x45-lessons-pointer-audit.py --json
"""

import argparse
import hashlib
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
LESSONS = os.path.join(ROOT, "corpus", "lessons")
INDEX = os.path.join(LESSONS, "README.md")

# A §2 row: `| `corpus/lessons/x.md` | ... |` (the row may also be a bare name
# in older revisions; both are accepted).
MD_ROW_RE = re.compile(r"^\|\s*`?(?:corpus/lessons/)?([A-Za-z0-9_.-]+\.md)`?\s*\|(.*)\|\s*$")
Q_ROW_RE = re.compile(r"^\|\s*(Q-[A-Za-z0-9]+-[0-9]+)\s*\|")
# A range cell like `Q-02-1..4` or a comma list.
RANGE_RE = re.compile(r"(Q-[A-Za-z0-9]+-)(\d+)(?:\.\.(\d+))?")
# A pointer that names a path it knows is absent, e.g. "`reports/round-1` not filed".
NOT_FILED_RE = re.compile(r"not filed|no `validation\.json`|not round-numbered", re.I)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def section(text, start, end):
    """Return the text between the heading matching `start` and the next `end`."""
    a = text.find(start)
    if a < 0:
        return ""
    b = text.find(end, a + len(start))
    return text[a:b] if b > 0 else text[a:]


def parse_rows(text):
    """Return (md_rows, queue_rows) from the index bytes."""
    md_rows = []
    for line in text.splitlines():
        m = MD_ROW_RE.match(line)
        if m:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            md_rows.append({"file": m.group(1), "cells": cells, "raw": line})
    queue_rows = []
    for line in text.splitlines():
        m = Q_ROW_RE.match(line)
        if m:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            queue_rows.append({"id": m.group(1), "cells": cells, "raw": line})
    return md_rows, queue_rows


def carried_ids(cell):
    """Expand a `open-questions carried` cell into concrete ids."""
    ids = set()
    for prefix, lo, hi in RANGE_RE.findall(cell):
        if hi:
            width = len(lo)
            for n in range(int(lo), int(hi) + 1):
                ids.add(f"{prefix}{n:0{width}d}" if width > 1 else f"{prefix}{n}")
        else:
            ids.add(f"{prefix}{lo}")
    return ids


def pointer_paths(cell):
    """Backticked tokens in a disposition cell that look like repo paths."""
    out = []
    for tok in re.findall(r"`([^`]+)`", cell):
        tok = tok.strip()
        if "/" in tok or tok.endswith((".md", ".json", ".py")):
            out.append(tok)
    return out


def resolves(tok):
    tok = tok.strip()
    if tok.startswith("."):  # e.g. `.ufo/l0-questions.md` — resolve from the lane root
        return os.path.exists(os.path.join(ROOT, tok))
    return os.path.exists(os.path.join(ROOT, tok))


def run_checks():
    text = read(INDEX)
    md_rows, queue_rows = parse_rows(text)
    s2 = section(text, "## 2.", "## 3.")
    s4 = section(text, "## 4.", "## 5.")
    findings = []
    checks = {}

    # ---- P1: disposition pointers resolve (or are declared absent) ----------
    unresolved = []
    declared_absent = []
    for row in md_rows:
        if len(row["cells"]) < 6:
            continue
        if not row["file"].endswith(".md"):
            continue
        disp = row["cells"][4]
        declared = bool(NOT_FILED_RE.search(disp))
        for tok in pointer_paths(disp):
            if resolves(tok):
                continue
            (declared_absent if declared else unresolved).append((row["file"], tok, disp))
    checks["P1_pointers_resolve"] = not unresolved
    if unresolved:
        findings.append({"id": "X45-P1", "class": "unresolved-pointer", "detail": unresolved})

    # ---- P2: prose counts == measurement ------------------------------------
    files = sorted(f for f in os.listdir(LESSONS) if f.endswith(".md"))
    md_rows_md = [r for r in md_rows if r["file"].endswith(".md")]
    carries = [r for r in md_rows_md if not r["cells"][3].strip().startswith("—")
               and r["cells"][3].strip() not in ("", "-")]
    prose = []
    for m in re.finditer(r"(?i)(\d+)\s+of\s+(\d+)\b", s4 + s2):
        prose.append((int(m.group(1)), int(m.group(2)), m.group(0)))
    drift = []
    for a, b, raw in prose:
        # "N of M" about the partition must match the live file count.
        if b in (len(files), len(md_rows_md)):
            want_a = len(carries) if a < b else len(files)
            if a != want_a:
                drift.append({"stated": raw, "measured_a": want_a, "of": b})
    checks["P2_prose_counts"] = not drift
    if drift:
        findings.append({"id": "X45-P2", "class": "prose-count-drift", "detail": drift})

    # ---- P3: carried ids <-> queue ids --------------------------------------
    carried = set()
    for row in md_rows_md:
        if len(row["cells"]) >= 4:
            carried |= carried_ids(row["cells"][3])
    queue_ids = {r["id"] for r in queue_rows}
    orphan_carried = sorted(carried - queue_ids)
    orphan_queue = sorted(queue_ids - carried)
    checks["P3_queue_cross_consistency"] = not orphan_carried and not orphan_queue
    if orphan_carried or orphan_queue:
        findings.append({
            "id": "X45-P3", "class": "queue-cross-inconsistency",
            "detail": {"carried_without_queue_row": orphan_carried,
                       "queue_row_not_carried": orphan_queue},
        })

    return {
        "index": "corpus/lessons/README.md",
        "index_sha256": sha256(INDEX),
        "index_bytes": os.path.getsize(INDEX),
        "lesson_files": len(files),
        "index_rows": len(md_rows_md),
        "queue_rows": len(queue_rows),
        "rows_carrying_questions": len(carries),
        "declared_absent_pointers": declared_absent,
        "checks": checks,
        "findings": findings,
    }


# --------------------------------------------------------------------------
# Selftest — in-memory controls, nothing written.
# --------------------------------------------------------------------------


def selftest():
    ok = total = 0

    def check(label, cond):
        nonlocal ok, total
        total += 1
        ok += bool(cond)
        print(f"  {'PASS' if cond else 'FAIL'} {label}")

    check("md row regex captures bare name",
          MD_ROW_RE.match("| `round-5.md` | gate-keeper |").group(1) == "round-5.md")
    check("md row regex captures prefixed name",
          MD_ROW_RE.match("| `corpus/lessons/round-5.md` | gate-keeper |").group(1) == "round-5.md")
    check("queue row regex captures id",
          Q_ROW_RE.match("| Q-02-1 | x | y |").group(1) == "Q-02-1")
    check("queue row regex rejects header",
          Q_ROW_RE.match("| Q-id | question | owner | status |") is None)
    check("range expands Q-02-1..4",
          carried_ids("Q-02-1..4") == {"Q-02-1", "Q-02-2", "Q-02-3", "Q-02-4"})
    check("range keeps zero width",
          carried_ids("Q-S1-1") == {"Q-S1-1"})
    check("comma list expands",
          carried_ids("Q-17-1, Q-17-2") == {"Q-17-1", "Q-17-2"})
    check("pointer extracts repo path",
          pointer_paths("`reports/round-5`") == ["reports/round-5"])
    check("pointer ignores prose word",
          pointer_paths("the parent owns it") == [])
    check("not-filed prose detected",
          bool(NOT_FILED_RE.search("`reports/round-1` not filed; record is `LOG.md`")))
    check("live path resolves", resolves("corpus/lessons"))
    check("absent path does not resolve", not resolves("reports/__no_such__"))

    res = run_checks()
    check("live index is readable", res["index_rows"] > 0)
    check("live queue is non-empty", res["queue_rows"] > 0)
    check("sha256 well formed", re.fullmatch(r"[0-9a-f]{64}", res["index_sha256"]) is not None)

    print(f"SELFTEST {'OK' if ok == total else 'FAILED'}: {ok}/{total} checks passed")
    return 0 if ok == total else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    res = run_checks()
    if args.json:
        print(json.dumps(res, indent=1, sort_keys=True))
        return 0
    print(f"index:        {res['index']}")
    print(f"sha256:       {res['index_sha256']}")
    print(f"lesson files: {res['lesson_files']}")
    print(f"index rows:   {res['index_rows']}")
    print(f"queue rows:   {res['queue_rows']}")
    print(f"carry rows:   {res['rows_carrying_questions']}")
    for k, v in res["checks"].items():
        print(f"  {'PASS' if v else 'FAIL'} {k}")
    print(f"findings:     {len(res['findings'])}")
    for f in res["findings"]:
        print(f"  {f['id']} {f['class']}: {f['detail']}")
    return 0 if not res["findings"] else 1


if __name__ == "__main__":
    sys.exit(main())
