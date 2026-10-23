#!/usr/bin/env python3
r"""Round-58 control re-score: score every pre-data control fixture with the frozen counter at one revision.

  python3 -B reports/round-58/rescore-controls.py --rev REV [--jobs N] FIXTURE_DIR...

A FIXTURE_DIR holds `fixture.patch` (a `git diff` of the seat's sandbox clone against the declaration it
built on). For each, a fresh clone of the lane is checked out at REV under /fast/scratch/hyaku/
(GIT_DIR, GIT_WORK_TREE, GIT_INDEX_FILE unset), the patch is applied with `git apply`; when the patch does
not carry the entry file, the dir's `untracked/` or `corpus/` tree is copied over the clone root. Any
support directory at REV is removed from the clone; when the fixture dir has `support/` (a registry.json
and the reviewer verdict files judged for that fixture's rows), it is installed as
.ufo/waves/round-58/support/, so the SUPPORT leg reads only that fixture's own verdicts. A patch
that touches reports/round-58/*.py (an instrument mutant) is not a claim control and is skipped with
`SKIP mutant`. Then `timeout 1200 python3 -B reports/round-58/accept-c.py` runs in the clone.

Prints one block per fixture: `## <dir>`, the counter's leg lines, `exit <n>`, and the verdict line
`<dir> -> <last counter line> failing=[legs]`; exit 0 when no fixture printed `ACCEPT-C-58: PASS`,
1 otherwise (a control met the counter), 2 on usage error. Never writes the lane.
"""
import concurrent.futures
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(HERE))
SCRATCH = "/fast/scratch/hyaku"
ENTRY = "corpus/knowledge/linguistics/toponymy-place-names.md"
ENV = {k: v for k, v in os.environ.items() if k not in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE")}


def score(rev, fixture):
    patch = os.path.join(fixture, "fixture.patch")
    body = open(patch, encoding="utf-8", errors="replace").read()
    if re.search(r"^\+\+\+ \S*reports/round-58/[^/\s]+\.py", body, re.M):
        return fixture, "SKIP mutant (patch edits an instrument)", None
    clone = tempfile.mkdtemp(prefix="kotodama-r58-rescore-", dir=SCRATCH)
    subprocess.run(["git", "clone", "--quiet", "--no-checkout", LANE, clone], env=ENV, check=True)
    subprocess.run(["git", "-C", clone, "-c", "advice.detachedHead=false", "checkout", "--quiet", rev], env=ENV, check=True)
    applied = subprocess.run(["git", "-C", clone, "apply", "--whitespace=nowarn", os.path.abspath(patch)],
                             env=ENV, capture_output=True, text=True)
    notes = [] if applied.returncode == 0 else [f"git apply exit {applied.returncode}: {applied.stderr.strip()[:300]}"]
    if not os.path.isfile(os.path.join(clone, ENTRY)):
        for extra in ("untracked", "corpus"):
            src = os.path.join(fixture, extra)
            if os.path.isdir(src):
                dst = clone if extra == "untracked" else os.path.join(clone, "corpus")
                shutil.copytree(src, dst, dirs_exist_ok=True)
                notes.append(f"copied {extra}/")
    support = os.path.join(fixture, "support")
    target = os.path.join(clone, ".ufo/waves/round-58/support")
    shutil.rmtree(target, ignore_errors=True)
    if os.path.isdir(support):
        shutil.copytree(support, target)
        notes.append("installed support/ (the fixture's own registered verdicts)")
    run = subprocess.run(["timeout", "1200", sys.executable, "-B", "reports/round-58/accept-c.py"], cwd=clone,
                         env=ENV, capture_output=True, text=True)
    shutil.rmtree(clone, ignore_errors=True)
    return fixture, "\n".join(notes), run


def main(argv):
    if len(argv) < 3 or argv[0] != "--rev":
        print(__doc__, file=sys.stderr)
        return 2
    rev, rest = argv[1], argv[2:]
    jobs = 4
    if rest[:1] == ["--jobs"]:
        jobs, rest = int(rest[1]), rest[2:]
    full = subprocess.run(["git", "-C", LANE, "rev-parse", "--verify", rev + "^{commit}"], env=ENV,
                          capture_output=True, text=True, check=True).stdout.strip()
    print(f"# measured-revision {full}")
    met = False
    with concurrent.futures.ThreadPoolExecutor(jobs) as pool:
        for fixture, notes, run in pool.map(lambda f: score(full, f), rest):
            name = os.path.relpath(fixture, LANE)
            print(f"## {name}")
            if notes:
                print(f"# {notes}")
            if run is None:
                print(f"{name} -> SKIP")
                continue
            out = run.stdout.rstrip("\n")
            print(out)
            if run.stderr.strip():
                print(f"# stderr: {run.stderr.strip()[:400]}")
            print(f"exit {run.returncode}")
            last = out.splitlines()[-1] if out else "(no output)"
            failing = re.findall(r"^(\w+) FAIL", out, re.M)
            met |= last == "ACCEPT-C-58: PASS"
            print(f"{name} -> {last} failing={failing}")
    return 1 if met else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
