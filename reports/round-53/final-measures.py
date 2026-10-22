#!/usr/bin/env python3
"""Round-53 after-measurements and red-before controls.

  python3 -B reports/round-53/final-measures.py --tree DIR [--label TEXT]

DIR is an exported lane tree (for example `git -C <lane> archive <commit> | tar -x -C DIR`).
Runs, in DIR: the declared D and C counting and acceptance commands, the README sweep on its
own, the separability and agreement commands, the dry-run receipt check, the access checker
and the draft-id checker. Then builds scratch copies of DIR with each claim made false and runs
that claim's acceptance there; each control must exit non-zero for its stated reason:
  D-red-1  one fragment `, -6` restored after the S162 citation on the 'working their farms' line
  D-red-2  line 113 cites S163 again
  C-red-1  the README index row for the gesture entry removed
  C-red-2  the used-by cell of the entry's first cited S-id emptied to '—'
  C-red-3  the gesture entry deleted
  C-red-4  a second new knowledge file added and an existing one removed (clauses.py C1)
  C-red-5  the entry's `- topic:` line no longer names gesture and pointing (clauses.py C2)
  D-red-3  one routed line deleted from the speech-surrogates entry (clauses.py D1)
Prints a receipt; exits 0 when every after-command meets its declaration and every red control
fails as stated, 1 otherwise. Stdlib only; never touches a git repository.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

ED = "corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md"
EC = "corpus/knowledge/linguistics/gesture-co-speech-pointing.md"
PY = [sys.executable, "-B"]


def run(cwd, argv, shell=False):
    shown = argv if shell else " ".join(argv)
    res = subprocess.run(argv, cwd=cwd, shell=shell, capture_output=True, text=True, timeout=600)
    text = (res.stdout + res.stderr).rstrip("\n")
    print(f"$ {shown}")
    if text:
        print(text)
    print(f"exit {res.returncode}")
    return res.returncode, res.stdout


def scratch(tree):
    path = tempfile.mkdtemp(prefix="r53-red-")
    shutil.copytree(tree, path, dirs_exist_ok=True)
    return path


def edit(path, rel, fn):
    full = os.path.join(path, rel)
    with open(full, encoding="utf-8") as fh:
        text = fh.read()
    new = fn(text)
    if new == text:
        raise SystemExit(f"CONTROL_SETUP_ERROR {rel}: mutation changed nothing")
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(new)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tree", required=True)
    ap.add_argument("--label", default="final measures")
    ap.add_argument("--lane", required=True, help="lane git repository, read-only, for the separability base")
    ap.add_argument("--base-tree", required=True, help="export of the claim base a9cf95f, for clauses.py")
    args = ap.parse_args()
    tree = os.path.abspath(args.tree)
    print(f"# {args.label} {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} tree={tree}")
    ok = True
    want = [
        (["python3", "-B", "reports/round-53/d-count.py"], 0),
        ("find corpus/knowledge -name '*.md' | wc -l", None),
        (["python3", "-B", "reports/round-53/accept-c.py"], 0),
        (["python3", "-B", "reports/round-28/readme/sweep.py"], 0),
        (["python3", "-B", "tools/check-claim-separability.py", "reports/round-53/separability-manifest.json",
          "--lane", os.path.abspath(args.lane), "--root", "."], 0),
        (["python3", "-B", "reports/round-53/claims-agree.py"], 0),
        (["python3", "-B", "reports/round-53/dry-run.py", "check", "reports/round-53/telemetry/declaration-dry-run.txt"], 0),
        (["python3", "-B", "tools/check-source-access.py"], 0),
        (["python3", "-B", "tools/check-draft-ids.py"], 0),
        (["python3", "-B", "reports/round-53/clauses.py", "--base-tree", os.path.abspath(args.base_tree)], 0),
    ]
    print("\n## After-commands")
    for argv, expect in want:
        shell = isinstance(argv, str)
        code, out = run(tree, argv, shell=shell)
        if shell:
            if out.strip() != "229":
                ok = False
                print("# MISMATCH: expected 229")
        elif code != expect:
            ok = False
            print(f"# MISMATCH: expected exit {expect}")
    print("\n## Red-before controls (scratch copies of the tree, claim made false)")

    def d_red_1(p):
        def f(t):
            lines = t.split("\n")
            for i, line in enumerate(lines):
                if "working their farms" in line:
                    lines[i] = line.replace("S162", "S162, -6", 1)
            return "\n".join(lines)
        edit(p, ED, f)
        return ["python3", "-B", "reports/round-53/d-count.py"], "FRAG"

    def d_red_2(p):
        def f(t):
            lines = t.split("\n")
            for i, line in enumerate(lines):
                if "mobile phone" in line:
                    lines[i] = line.replace("S159", "S163", 1)
            return "\n".join(lines)
        edit(p, ED, f)
        return ["python3", "-B", "reports/round-53/d-count.py"], "WROW2"

    def c_red_1(p):
        name = os.path.basename(EC)
        edit(p, "corpus/README.md", lambda t: "\n".join(l for l in t.split("\n") if not l.startswith(f"- `{name}`")))
        return ["python3", "-B", "reports/round-53/accept-c.py"], "SWEEP FAIL"

    def c_red_2(p):
        text = open(os.path.join(p, EC), encoding="utf-8").read()
        first = sorted(set(re.findall(r"\bS\d{3}\b", text)))[0]

        def f(t):
            out = []
            for line in t.split("\n"):
                if line.startswith(f"| {first} "):
                    cells = line.split("|")
                    cells[11] = " — "
                    line = "|".join(cells)
                out.append(line)
            return "\n".join(out)
        edit(p, "corpus/SOURCES.md", f)
        return ["python3", "-B", "reports/round-53/accept-c.py"], "SIDS FAIL"

    def c_red_3(p):
        os.remove(os.path.join(p, EC))
        return ["python3", "-B", "reports/round-53/accept-c.py"], "ENTRY FAIL"

    clauses = ["python3", "-B", "reports/round-53/clauses.py", "--base-tree", os.path.abspath(args.base_tree)]

    def c_red_4(p):
        extra = os.path.join(p, "corpus/knowledge/linguistics/zz-probe.md")
        with open(extra, "w", encoding="utf-8") as fh:
            fh.write("# probe\n")
        os.remove(os.path.join(p, "corpus/knowledge/linguistics/numerals-and-measures.md"))
        return clauses, "C1 FAIL"

    def c_red_5(p):
        edit(p, EC, lambda t: re.sub(r"(?m)^- topic:.*$", "- topic: hand-made pottery", t, count=1))
        return clauses, "C2 FAIL"

    def d_red_3(p):
        edit(p, ED, lambda t: "\n".join(l for l in t.split("\n") if "working their farms" not in l))
        return clauses, "D1 FAIL"

    for name, build in [("D-red-1", d_red_1), ("D-red-2", d_red_2), ("D-red-3", d_red_3),
                        ("C-red-1", c_red_1), ("C-red-2", c_red_2), ("C-red-3", c_red_3),
                        ("C-red-4", c_red_4), ("C-red-5", c_red_5)]:
        p = scratch(tree)
        try:
            argv, reason = build(p)
            print(f"\n### {name}: expect non-zero exit with '{reason}'")
            code, out = run(p, argv)
            good = code != 0 and reason in out
            print(f"# {name} {'RED-AS-STATED' if good else 'CONTROL-FAILED'}")
            ok = ok and good
        finally:
            shutil.rmtree(p, ignore_errors=True)
    print(f"\nFINAL {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
