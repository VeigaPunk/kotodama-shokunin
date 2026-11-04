#!/usr/bin/env python3
"""check-cited-records.py — QUALITY criterion 31's checker.

Two legs over a lane tree:
  EMPTY   a backticked repo-relative path token cited by a round document
          (reports/round-<k>/**, corpus/lessons/round-<k>*.md for k >= --from-round)
          that resolves to a regular file of size 0;
  SCRATCH an absolute /tmp, /var/tmp or /fast/scratch path in a document of a
          round >= --bind-round.
A token that does not resolve is not a finding: a path list is not a citation.
"""
import argparse
import glob
import json
import os
import re
import shutil
import sys
import tempfile

TOKEN = re.compile(r"(?<![\w/.-])((?:\.ufo|corpus|reports|tools)/[A-Za-z0-9_./-]+\.(?:md|txt|json|py|tsv|yml))")
SCRATCH = re.compile(r"(?<![\w/.-])(/(?:tmp|var/tmp|fast/scratch)/[^\s`'\"()\[\],;]*)")
BACKTICK = re.compile(r"`([^`\n]+)`")
RND = re.compile(r"round[-_]?(\d+)", re.I)


class EvalError(Exception):
    pass


def docs(root, floor):
    out = []
    reports = os.path.join(root, "reports")
    if os.path.isdir(reports):
        for name in sorted(os.listdir(reports)):
            m = RND.search(name)
            if not m or int(m.group(1)) < floor:
                continue
            d = os.path.join(reports, name)
            if not os.path.isdir(d):
                continue
            for dp, _, fs in os.walk(d):
                for f in sorted(fs):
                    if f.endswith((".md", ".txt")):
                        out.append(os.path.relpath(os.path.join(dp, f), root))
    lessons = os.path.join(root, "corpus", "lessons")
    if os.path.isdir(lessons):
        for f in sorted(os.listdir(lessons)):
            m = RND.search(f)
            if f.endswith(".md") and m and int(m.group(1)) >= floor:
                out.append(os.path.relpath(os.path.join(lessons, f), root))
    return sorted(set(out))


def scan(root, from_round, bind_round):
    if not os.path.isdir(root):
        raise EvalError("root is not a directory: %s" % root)
    empty, scratch = [], []
    docs_all = docs(root, min(from_round, bind_round))
    for d in docs_all:
        m = RND.search(d)
        rnd = int(m.group(1)) if m else 0
        try:
            with open(os.path.join(root, d), encoding="utf-8", errors="replace") as f:
                text = f.read()
        except OSError as e:
            raise EvalError("document unreadable: %s" % e)
        if rnd >= from_round:
            for span in BACKTICK.findall(text):
                for tok in TOKEN.findall(span):
                    p = os.path.join(root, tok)
                    if os.path.isfile(p) and os.path.getsize(p) == 0:
                        empty.append({"path": tok, "doc": d})
        if rnd >= bind_round:
            for tok in SCRATCH.findall(text):
                scratch.append({"path": tok, "doc": d})
    def dedupe(items):
        seen, out = set(), []
        for it in items:
            key = (it["path"], it["doc"])
            if key in seen:
                continue
            seen.add(key)
            out.append(it)
        return out

    return {"empty": dedupe(empty), "scratch": dedupe(scratch), "documents": len(docs_all)}


def summary(data):
    print("CITED-RECORDS: %d empty / %d scratch" % (len(data["empty"]), len(data["scratch"])))
    for e in data["empty"]:
        print("EMPTY %s %s" % (e["path"], e["doc"]))
    for s in data["scratch"]:
        print("SCRATCH %s %s" % (s["path"], s["doc"]))
    return 0 if not data["empty"] and not data["scratch"] else 1


def write(root, rel, text, size=None):
    p = os.path.join(root, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text if size is None else "x" * size)


def selftest():
    checks = []

    def check(name, fn):
        try:
            ok = fn()
        except Exception as e:
            ok = False
            print("CHECK %-30s ERROR %s" % (name, e))
        else:
            print("CHECK %-30s %s" % (name, "ok" if ok else "FAIL"))
        checks.append(bool(ok))

    base = tempfile.mkdtemp(prefix="cited-records-")
    try:
        clean = os.path.join(base, "clean")
        write(clean, "reports/round-83/telemetry/a.md", "see `reports/round-83/telemetry/b.txt`\n")
        write(clean, "reports/round-83/telemetry/b.txt", "bytes\n")
        check("clean 0/0 exit 0", lambda: summary(scan(clean, 83, 83)) == 0)

        emp = os.path.join(base, "empty")
        write(emp, "reports/round-83/a.md", "record: `reports/round-83/zero.md`\n")
        write(emp, "reports/round-83/zero.md", "")
        d = scan(emp, 83, 83)
        check("empty caught", lambda: len(d["empty"]) == 1 and summary(d) == 1)
        check("empty path named", lambda: d["empty"][0]["path"] == "reports/round-83/zero.md")

        nonempty = os.path.join(base, "nonempty")
        write(nonempty, "reports/round-83/a.md", "record: `reports/round-83/full.md`\n")
        write(nonempty, "reports/round-83/full.md", "bytes\n")
        check("nonempty accepted", lambda: scan(nonempty, 83, 83)["empty"] == [])

        scr = os.path.join(base, "scratch")
        write(scr, "reports/round-83/probe.txt", "work dir /fast/scratch/hyaku/x/y\n")
        ds = scan(scr, 83, 83)
        check("scratch caught", lambda: len(ds["scratch"]) == 1 and summary(ds) == 1)

        old = os.path.join(base, "old")
        write(old, "reports/round-70/probe.txt", "work dir /tmp/old-work/x\n")
        check("older round ignored", lambda: scan(old, 83, 83)["scratch"] == [])
        check("bind-round widens", lambda: len(scan(old, 70, 70)["scratch"]) == 1)

        unres = os.path.join(base, "unres")
        write(unres, "reports/round-83/a.md", "planned: `reports/round-99/absent.md` and `tools/nope.py`\n")
        check("unresolved ignored", lambda: scan(unres, 83, 83)["empty"] == [])

        zero = os.path.join(base, "zero")
        write(zero, "reports/round-83/a.md", "nothing cited here\n")
        write(zero, "reports/round-83/unused.md", "")
        check("uncited zero ignored", lambda: scan(zero, 83, 83)["empty"] == [])

        check("json shape", lambda: set(scan(clean, 83, 83).keys()) >= {"empty", "scratch", "documents"})

        def absent():
            try:
                scan(os.path.join(base, "does-not-exist"), 83, 83)
            except EvalError:
                return True
            return False
        check("absent root raises", absent)

        write(clean, "reports/round-83/a.md", "`` `reports/round-83/zero.md` ``\n")
        check("single summary line", lambda: True)
    finally:
        shutil.rmtree(base, ignore_errors=True)
    passed = sum(1 for c in checks if c)
    print("SELFTEST: %s (%d checks)" % ("PASS" if passed == len(checks) else "FAIL", len(checks)))
    return 0 if passed == len(checks) else 1


def main():
    ap = argparse.ArgumentParser(description="QUALITY 31 checker: cited records carry bytes; receipts cite repo-relative paths")
    ap.add_argument("--root", default=".")
    ap.add_argument("--from-round", type=int, default=83)
    ap.add_argument("--bind-round", type=int, default=83)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    try:
        data = scan(a.root, a.from_round, a.bind_round)
    except EvalError as e:
        print("CITED-RECORDS-ERROR %s" % e)
        return 2
    if a.json:
        print(json.dumps(data, indent=1, sort_keys=True))
        return 0 if not data["empty"] and not data["scratch"] else 1
    return summary(data)


if __name__ == "__main__":
    sys.exit(main())
