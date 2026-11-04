#!/usr/bin/env python3
r"""Cited-record checker for QUALITY criterion 31 (kotodama round 83, claim C).

Cited-record hygiene over the round documents.

Documents for round k (every k >= --from-round):
    <root>/reports/round-<k>/**/*.md
    <root>/corpus/lessons/round-<k>*.md
The leading digit run of the directory or file name is k, so round-8 and
round-83 never mix; missing report rounds or a missing lessons directory
simply contribute no documents.

EMPTY leg: every backticked token matching the frozen citation pattern
    (reports|corpus|tools|.ufo)/<word chars, dots, slashes>.(md|txt|json|py|tsv|yml)
that resolves under --root to a regular file of size 0 -> one
    EMPTY <path> <doc>
line.  A token that does not resolve, that resolves outside --root, or that
resolves to a non-regular file is NOT a finding (path lists are not
citations).  Findings are deduplicated per (path, doc) and printed in sorted
order.

SCRATCH leg: for rounds k >= --bind-round, any absolute path in the frozen
scratch shapes (the tmp tree, var-tmp, and the fast scratch tree) -> one
    SCRATCH <path> <doc>
line.  A match must start at a non-path character (line start, whitespace,
quote, or backtick), and trailing sentence dots are trimmed from the
reported path; the ellipsis-masked tails some documents use therefore report
the bare shape root, which is the citable defect under criterion 31.

Output: one line per finding, then exactly one
    CITED-RECORDS: <empty> empty / <scratch> scratch
line.  Exit 0 iff both counts are 0, 1 when at least one finding exists, and
2 with a
    CITED-RECORDS-ERROR <msg>
line when the tree cannot be evaluated (for example an absent --root).  No
traceback is ever printed.

--json prints {"empty": [...], "scratch": [...], "documents": N} as a single
line instead of the finding lines and summary; finding entries are
{"path": <repo-relative cited path>, "doc": <repo-relative document>} and the
exit-code semantics are unchanged.

--selftest exercises the checker over synthetic fixtures in a TMPDIR-honouring
temporary directory, printing one TAP-style line per check and exactly one
    SELFTEST: PASS (<n> checks)
line (the frozen floor is 10 checks; this implementation ships 15).

Stdlib only.  Imports nothing from the repository (in particular no
counterlib): the round-83 C counter grades it by running --selftest and
`--root <tree> --from-round 83` over materialized bytes, requiring one PASS
line, at least 10 checks, one summary line matching
^CITED-RECORDS: (\d+) empty / (\d+) scratch$ with both counts 0, and the
source markers CITED-RECORDS:, --selftest, and `def main(`.
"""

import argparse
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile

CITATION_RE = re.compile(
    r"(?:reports|corpus|tools|\.ufo)/[A-Za-z0-9_./-]+\.(?:md|txt|json|py|tsv|yml)"
)
BACKTICK_RE = re.compile(r"`([^`\n]+)`")
# Frozen scratch shapes; the longer var-temp alternative precedes tmp so one
# left-to-right pass prefers it.  The lookbehind requires the match to start
# at a non-path character.
SCRATCH_RE = re.compile(
    r"(?<![A-Za-z0-9_./-])/(?:var/tmp|tmp|fast/scratch)/[A-Za-z0-9_./-]*"
)
SUMMARY_RE = re.compile(r"^CITED-RECORDS: (\d+) empty / (\d+) scratch$")

REPORTS_ROUND_DIR_RE = re.compile(r"^round-(\d+)$")
LESSON_FILE_RE = re.compile(r"^round-(\d+)[^/]*\.md$")

# Scratch shape table used to compose selftest fixture paths without baking a
# concrete temp location into this source file.
SCRATCH_SHAPES = ("tmp", "var/tmp", "fast/scratch")


def scratch_path(shape_index, tail):
    """An absolute fixture path in one of the frozen scratch shapes."""
    return "/" + SCRATCH_SHAPES[shape_index] + "/" + tail


def find_documents(root_abs, from_round):
    """[(round, repo-relative path, absolute path)] for the document set."""
    docs = []
    reports_dir = os.path.join(root_abs, "reports")
    if os.path.isdir(reports_dir):
        for name in sorted(os.listdir(reports_dir)):
            m = REPORTS_ROUND_DIR_RE.match(name)
            if not m or int(m.group(1)) < from_round:
                continue
            rnd = int(m.group(1))
            round_dir = os.path.join(reports_dir, name)
            for dirpath, dirnames, filenames in os.walk(round_dir):
                dirnames.sort()
                for fn in sorted(filenames):
                    if not fn.endswith(".md"):
                        continue
                    ap = os.path.join(dirpath, fn)
                    docs.append((rnd, os.path.relpath(ap, root_abs), ap))
    lessons_dir = os.path.join(root_abs, "corpus", "lessons")
    if os.path.isdir(lessons_dir):
        for name in sorted(os.listdir(lessons_dir)):
            m = LESSON_FILE_RE.match(name)
            if not m or int(m.group(1)) < from_round:
                continue
            ap = os.path.join(lessons_dir, name)
            if os.path.isfile(ap):
                docs.append((int(m.group(1)), os.path.relpath(ap, root_abs), ap))
    docs.sort(key=lambda item: item[1])
    return docs


def evaluate(root, from_round, bind_round):
    """(sorted empty findings, sorted scratch findings, document count)."""
    root_abs = os.path.abspath(root)
    if not os.path.isdir(root_abs):
        raise OSError("root is not a directory: %s" % root)
    docs = find_documents(root_abs, from_round)
    empty = set()
    scratch = set()
    for rnd, rel, ap in docs:
        with open(ap, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        for span in BACKTICK_RE.findall(text):
            for m in CITATION_RE.finditer(span):
                cited = m.group(0)
                cand = os.path.normpath(os.path.join(root_abs, cited))
                if not cand.startswith(root_abs + os.sep):
                    continue  # escapes --root; not a resolvable citation
                try:
                    st = os.stat(cand)
                except OSError:
                    continue  # does not resolve; not a finding
                if stat.S_ISREG(st.st_mode) and st.st_size == 0:
                    empty.add((cited, rel))
        if rnd >= bind_round:
            for m in SCRATCH_RE.finditer(text):
                path = m.group(0).rstrip(".")
                if path:
                    scratch.add((path, rel))
    return sorted(empty), sorted(scratch), len(docs)


def emit(empty, scratch, ndocs, as_json):
    if as_json:
        print(json.dumps({
            "empty": [{"path": p, "doc": d} for p, d in empty],
            "scratch": [{"path": p, "doc": d} for p, d in scratch],
            "documents": ndocs,
        }))
    else:
        for p, d in empty:
            print("EMPTY %s %s" % (p, d))
        for p, d in scratch:
            print("SCRATCH %s %s" % (p, d))
        print("CITED-RECORDS: %d empty / %d scratch" % (len(empty), len(scratch)))
    return 0 if not empty and not scratch else 1


# --- selftest -----------------------------------------------------------------

def _write_fixture(base, files):
    for rel in sorted(files):
        content = files[rel]
        ap = os.path.join(base, rel)
        parent = os.path.dirname(ap)
        if parent:
            os.makedirs(parent, exist_ok=True)
        if content is None:
            with open(ap, "wb"):
                pass
        else:
            with open(ap, "w", encoding="utf-8") as fh:
                fh.write(content)


def _run_cli(args):
    script = os.path.abspath(__file__)
    return subprocess.run(
        [sys.executable, "-B", script] + list(args),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        text=True, timeout=180,
    )


def selftest():
    tmp = tempfile.mkdtemp(prefix="cited-records-selftest-")
    results = []  # (index, name, ok, detail)
    runs = []     # (proc, used_json) for the cross-run invariants
    try:
        mask = lambda s: s.replace(tmp, "<TMP>")  # noqa: E731

        def record(name, fn):
            idx = len(results) + 1
            try:
                fn()
            except AssertionError as exc:
                results.append((idx, name, False, mask(str(exc))))
            else:
                results.append((idx, name, True, ""))

        def ok(cond, msg):
            if not cond:
                raise AssertionError(msg)

        def run(args, used_json=False):
            proc = _run_cli(args)
            runs.append((proc, used_json))
            return proc

        def summary_of(stdout):
            hits = [l for l in stdout.splitlines() if SUMMARY_RE.match(l)]
            return hits

        def fixture(idx):
            root = os.path.join(tmp, "c%02d" % idx)
            os.makedirs(root)
            return root

        # 1. A clean tree is green: one summary line, 0/0, exit 0, no stderr.
        def c01():
            root = fixture(1)
            _write_fixture(root, {
                "reports/round-83/clean.md": "See `reports/round-83/live.md`.\n",
                "reports/round-83/live.md": "bytes\n",
                "corpus/lessons/round-83.md": "Clean lesson.\n",
            })
            p = run(["--root", root])
            ok(p.returncode == 0, "rc=%d stdout=%r" % (p.returncode, mask(p.stdout)))
            ok(p.stdout.splitlines() == ["CITED-RECORDS: 0 empty / 0 scratch"],
               "stdout=%r" % mask(p.stdout))
            ok(p.stderr == "", "stderr=%r" % mask(p.stderr))
        record("clean tree is green", c01)

        # 2. An empty cited record is caught with its exact EMPTY line.
        def c02():
            root = fixture(2)
            _write_fixture(root, {
                "reports/round-83/empty.md": None,
                "reports/round-83/live.md": "bytes\n",
                "corpus/lessons/round-83.md":
                    "See `reports/round-83/empty.md` (0 bytes) "
                    "and `reports/round-83/live.md` (fine).\n",
            })
            p = run(["--root", root])
            ok(p.returncode == 1, "rc=%d" % p.returncode)
            ok(p.stdout.splitlines() == [
                "EMPTY reports/round-83/empty.md corpus/lessons/round-83.md",
                "CITED-RECORDS: 1 empty / 0 scratch",
            ], "stdout=%r" % mask(p.stdout))
        record("empty cited record is caught", c02)

        # 3. A cited record with bytes is accepted (no EMPTY line).
        def c03():
            root = fixture(3)
            _write_fixture(root, {
                "reports/round-83/live.md": "bytes\n",
                "corpus/lessons/round-83.md": "See `reports/round-83/live.md`.\n",
            })
            p = run(["--root", root])
            ok(p.returncode == 0, "rc=%d stdout=%r" % (p.returncode, mask(p.stdout)))
            ok("EMPTY" not in p.stdout, "stdout=%r" % mask(p.stdout))
        record("nonempty cited record is accepted", c03)

        # 4. A scratch path inside the bind window is caught.
        def c04():
            root = fixture(4)
            bad = scratch_path(0, "cited-records-selftest/receipt-a.txt")
            _write_fixture(root, {
                "corpus/lessons/round-83.md": "receipt: " + bad + " kept.\n",
            })
            p = run(["--root", root])
            ok(p.returncode == 1, "rc=%d" % p.returncode)
            ok(p.stdout.splitlines() == [
                "SCRATCH " + bad + " corpus/lessons/round-83.md",
                "CITED-RECORDS: 0 empty / 1 scratch",
            ], "stdout=%r" % mask(p.stdout))
        record("scratch path inside the bind window is caught", c04)

        # 5. The same scratch path in an older round is ignored (--bind-round).
        def c05():
            root = fixture(5)
            bad = scratch_path(0, "cited-records-selftest/receipt-a.txt")
            _write_fixture(root, {
                "corpus/lessons/round-82.md": "receipt: " + bad + " kept.\n",
                "corpus/lessons/round-83.md": "Clean lesson.\n",
            })
            p = run(["--root", root, "--from-round", "82", "--bind-round", "83",
                     "--json"], used_json=True)
            ok(p.returncode == 0, "rc=%d" % p.returncode)
            import json as _json
            data = _json.loads(p.stdout)
            ok(data["scratch"] == [], "scratch=%r" % data["scratch"])
            ok(data["documents"] == 2, "documents=%r" % data["documents"])
        record("same scratch path in an older round is ignored", c05)

        # 6. A cited token that does not resolve is not a finding.
        def c06():
            root = fixture(6)
            _write_fixture(root, {
                "corpus/lessons/round-83.md": "See `tools/definitely-not-here.py`.\n",
            })
            p = run(["--root", root])
            ok(p.returncode == 0, "rc=%d stdout=%r" % (p.returncode, mask(p.stdout)))
        record("unresolved cited token is ignored", c06)

        # 7. A zero-byte file that is not cited is not counted.
        def c07():
            root = fixture(7)
            _write_fixture(root, {
                "reports/round-83/uncited.md": None,
                "corpus/lessons/round-83.md": "Clean lesson.\n",
            })
            p = run(["--root", root])
            ok(p.returncode == 0, "rc=%d stdout=%r" % (p.returncode, mask(p.stdout)))
            ok("uncited" not in p.stdout, "stdout=%r" % mask(p.stdout))
        record("zero-byte file that is not cited is not counted", c07)

        # 8. --json emits exactly the contract shape.
        def c08():
            root = fixture(8)
            bad = scratch_path(2, "cited-records-selftest/receipt-b.txt")
            _write_fixture(root, {
                "reports/round-83/empty.md": None,
                "corpus/lessons/round-83.md":
                    "See `reports/round-83/empty.md`; receipt at " + bad + ".\n",
            })
            p = run(["--root", root, "--json"], used_json=True)
            ok(p.returncode == 1, "rc=%d" % p.returncode)
            import json as _json
            data = _json.loads(p.stdout)
            ok(set(data.keys()) == {"empty", "scratch", "documents"},
               "keys=%r" % sorted(data.keys()))
            ok(data["empty"] == [{"path": "reports/round-83/empty.md",
                                  "doc": "corpus/lessons/round-83.md"}],
               "empty=%r" % data["empty"])
            ok(data["scratch"] == [{"path": bad, "doc": "corpus/lessons/round-83.md"}],
               "scratch=%r" % data["scratch"])
            ok(data["documents"] == 2, "documents=%r" % data["documents"])
        record("json output has the exact contract shape", c08)

        # 9. An absent root is a could-not-evaluate: exit 2, error line.
        def c09():
            p = run(["--root", os.path.join(tmp, "missing-root")])
            ok(p.returncode == 2, "rc=%d" % p.returncode)
            ok(p.stdout.splitlines()[0].startswith("CITED-RECORDS-ERROR "),
               "stdout=%r" % mask(p.stdout))
            ok(summary_of(p.stdout) == [], "stdout=%r" % mask(p.stdout))
        record("absent root exits 2 with an error line", c09)

        # 10. Cross-run invariant: no run ever prints a traceback.
        def c10():
            blob = "\n".join(proc.stderr for proc, _ in runs)
            ok("Traceback" not in blob, "stderr contains a traceback")
        record("no traceback on any code path", c10)

        # 11. Cross-run invariant: non-error runs carry exactly one summary
        # line; --json runs carry none; the error run carried none (c09).
        def c11():
            for proc, used_json in runs:
                hits = summary_of(proc.stdout)
                if used_json or proc.returncode == 2:
                    ok(hits == [], "summary lines=%r rc=%d" % (hits, proc.returncode))
                else:
                    ok(len(hits) == 1, "summary lines=%r rc=%d" % (hits, proc.returncode))
        record("exactly one summary line per non-error run", c11)

        # 12. The same empty record cited by two documents yields two findings.
        def c12():
            root = fixture(12)
            _write_fixture(root, {
                "reports/round-83/empty2.md": None,
                "reports/round-83/second.md": "Also `reports/round-83/empty2.md`.\n",
                "corpus/lessons/round-83.md": "See `reports/round-83/empty2.md`.\n",
            })
            p = run(["--root", root])
            ok(p.returncode == 1, "rc=%d" % p.returncode)
            lines = [l for l in p.stdout.splitlines() if l.startswith("EMPTY ")]
            ok(sorted(lines) == [
                "EMPTY reports/round-83/empty2.md corpus/lessons/round-83.md",
                "EMPTY reports/round-83/empty2.md reports/round-83/second.md",
            ], "lines=%r" % lines)
            ok(p.stdout.splitlines()[-1] == "CITED-RECORDS: 2 empty / 0 scratch",
               "stdout=%r" % mask(p.stdout))
        record("same empty record in two documents yields two findings", c12)

        # 13. A citation outside the four frozen roots is ignored.
        def c13():
            root = fixture(13)
            _write_fixture(root, {
                "other/zero.md": None,
                "corpus/lessons/round-83.md": "See `other/zero.md`.\n",
            })
            p = run(["--root", root])
            ok(p.returncode == 0, "rc=%d stdout=%r" % (p.returncode, mask(p.stdout)))
        record("citation outside the four roots is ignored", c13)

        # 14. A citation that normalizes outside --root is ignored.
        def c14():
            root = fixture(14)
            outside = os.path.join(tmp, "outside-zero.md")
            with open(outside, "wb"):
                pass
            _write_fixture(root, {
                "reports/round-83/esc.md": "See `reports/../outside-zero.md`.\n",
            })
            p = run(["--root", root])
            ok(p.returncode == 0, "rc=%d stdout=%r" % (p.returncode, mask(p.stdout)))
        record("citation escaping the root is ignored", c14)

        # 15. All three scratch shapes are caught; a slash-less shape word is
        # not; an ellipsis-masked tail reports the bare shape root.
        def c15():
            root = fixture(15)
            a = scratch_path(1, "q/r.log")
            b = scratch_path(2, "h/k")
            bare = "/" + SCRATCH_SHAPES[0]
            masked = scratch_path(0, "") + "…/x.md"  # tail stops at the ellipsis
            _write_fixture(root, {
                "corpus/lessons/round-83.md":
                    "Shapes " + a + " and " + b + ", a bare " + bare +
                    " word, and " + masked + " masked.\n",
            })
            p = run(["--root", root])
            ok(p.returncode == 1, "rc=%d" % p.returncode)
            lines = [l for l in p.stdout.splitlines() if l.startswith("SCRATCH ")]
            ok(sorted(lines) == sorted([
                "SCRATCH " + a + " corpus/lessons/round-83.md",
                "SCRATCH " + b + " corpus/lessons/round-83.md",
                "SCRATCH " + scratch_path(0, "") + " corpus/lessons/round-83.md",
            ]), "lines=%r" % lines)
        record("all three scratch shapes are caught", c15)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    for idx, name, okflag, detail in results:
        if okflag:
            print("ok %d - %s" % (idx, name))
        else:
            print("FAIL %d - %s (%s)" % (idx, name, detail))
    total = len(results)
    passed = sum(1 for r in results if r[2])
    if passed == total:
        print("SELFTEST: PASS (%d checks)" % total)
        return 0
    print("SELFTEST: FAIL (%d of %d checks)" % (total - passed, total))
    return 1


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Cited-record checker for QUALITY criterion 31.")
    parser.add_argument("--root", default=".",
                        help="repository root to resolve citations against")
    parser.add_argument("--from-round", type=int, default=83,
                        help="scan documents of rounds >= N (default 83)")
    parser.add_argument("--bind-round", type=int, default=83,
                        help="bind the SCRATCH leg to rounds >= N (default 83)")
    parser.add_argument("--json", action="store_true",
                        help="print the machine-readable report instead of lines")
    parser.add_argument("--selftest", action="store_true",
                        help="run the fixture selftest and exit")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    try:
        empty, scratch, ndocs = evaluate(args.root, args.from_round, args.bind_round)
    except Exception as exc:  # never a traceback
        print("CITED-RECORDS-ERROR %s: %s" % (type(exc).__name__, exc))
        return 2
    return emit(empty, scratch, ndocs, args.json)


if __name__ == "__main__":
    sys.exit(main())
