#!/usr/bin/env python3
"""X28 — lessons-partition audit (read-only).

Censuses corpus/lessons/*.md, checks each round lesson for the lane's lesson
contract (a `## Gate` section with candidates and admitted/rejected readings,
a `source:` line, a `verified-at:` line), resolves every repo-path reference
against the live tree, and reports the round sequence vs the rounds recorded
in LOG.md. Emits JSON or a summary.

Usage:
    python3 reports/round-19/audit/lessons-audit.py [--json] [--selftest]
"""
import argparse
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LESSONS = os.path.join(LANE, "corpus", "lessons")

ROUND_RE = re.compile(r"^round-(\d+)")
GATE_RE = re.compile(r"^##\s+Gate\b", re.M)
PATH_RE = re.compile(r"`((?:corpus|reports|tools|examples|SKILL|LOG|SCORECARD)[A-Za-z0-9_./-]*\.(?:md|json|py|tsv|yml|yaml))(?::\d+(?:-\d+)?)?`")


def lesson_round(name):
    m = ROUND_RE.match(name)
    return int(m.group(1)) if m else None


def gate_block(text):
    m = GATE_RE.search(text)
    if not m:
        return ""
    rest = text[m.end():]
    nxt = re.search(r"^##\s+\S", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def audit_lesson(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8", "replace")
    name = os.path.basename(path)
    block = gate_block(text)
    cand = re.findall(r"^- \*\*Candidates:\*\*", block, re.M) or re.findall(
        r"^Opening\s+\w+\s+reading:", block, re.M
    )
    admitted = re.findall(r"\*\*Admitted[^:]*:\*\*", block) or re.findall(
        r"Admitted as", block
    )
    rejected = re.findall(r"\*\*Rejected[^:]*:\*\*", block) or re.findall(
        r"Rejected", block
    )
    spot = bool(re.search(r"spot-check", block, re.I))
    refs = sorted(set(PATH_RE.findall(text)))
    missing = [r for r in refs if not os.path.exists(os.path.join(LANE, r))]
    return {
        "file": name,
        "round": lesson_round(name),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "size_bytes": len(raw),
        "has_source_line": bool(re.search(r"^source:", text, re.M)),
        "has_verified_at": bool(re.search(r"^verified-at:", text, re.M)),
        "has_gate": bool(GATE_RE.search(text)),
        "gate_has_candidates": bool(cand),
        "gate_candidates": len(cand),
        "gate_has_admitted": bool(admitted),
        "gate_has_rejected": bool(rejected),
        "gate_has_spotcheck": spot,
        "path_refs": len(refs),
        "path_refs_missing": missing,
    }


def audit():
    files = sorted(f for f in os.listdir(LESSONS) if f.endswith(".md"))
    rows = [audit_lesson(os.path.join(LESSONS, f)) for f in files]
    rounds = sorted(r["round"] for r in rows if r["round"] is not None)
    with open(os.path.join(LANE, "LOG.md"), "rb") as fh:
        log = fh.read().decode("utf-8", "replace")
    logged = sorted({int(m) for m in re.findall(r"Round (\d+) admitted", log)})
    return {
        "schema": "kotodama-lessons-audit-v1",
        "lesson_files": len(rows),
        "rounds_with_lessons": rounds,
        "rounds_logged_admitted": logged,
        "rows": rows,
    }


def selftest():
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        if not cond:
            ok = False
        print(("PASS " if cond else "FAIL ") + name + (" " + detail if detail else ""))

    check("round parse", lesson_round("round-18.md") == 18)
    check("round parse named", lesson_round("round-1-gates-and-triage.md") == 1)
    check("round parse supplement", lesson_round("supplement-opencode-1.md") is None)
    txt = "x\n## Gate\n- **Candidates:** a\n- **Admitted:** b\n- **Rejected:** c\n## Next\n"
    b = gate_block(txt)
    check("gate block bounded", "Next" not in b, repr(b))
    check("gate candidates", bool(re.search(r"^- \*\*Candidates:\*\*", b, re.M)))
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return 0 if selftest() else 1
    rep = audit()
    if args.json:
        print(json.dumps(rep, indent=2, sort_keys=True))
    else:
        print(f"lesson files: {rep['lesson_files']}")
        print(f"rounds with lessons: {rep['rounds_with_lessons']}")
        print(f"rounds logged admitted: {rep['rounds_logged_admitted']}")
        for r in rep["rows"]:
            flag = "OK " if (r["has_gate"] and r["has_source_line"]) else "!! "
            print(f"{flag}{r['file']:36s} round={r['round']} gate={r['has_gate']} "
                  f"cand={r['gate_has_candidates']} refs={r['path_refs']} "
                  f"missing={len(r['path_refs_missing'])}")
            for m in r["path_refs_missing"]:
                print(f"      missing ref: {m}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
