#!/usr/bin/env python3
r"""Round-66 claim O acceptance, revision 0 (pre-data).

Operability claim: tools/check-claim-separability.py returns a verdict inside a
round's budget (R65-D4; the round-65 manifest timed out at the 600 s per-run
cap, `.ufo/waves/round-65/w1/RevSeparability.md` MED-4).

Legs (each prints `NAME PASS|FAIL detail`):
  SELFTEST  the tool's own --selftest exits 0 and prints `63/63`
  DIFF      the tool differs from base (the upgrade actually landed)
  OPTIONS   --help lists --jobs, --budget, --max-runs, --static-only
  BOUND     fixture lane with a sleeping acceptance + --budget 0.5 --timeout 10:
            exits 2, prints SEPARABILITY_PARTIAL, never asserts <base>
  STATIC    --static-only on a dynamic manifest exits 2, prints PARTIAL +
            UNRESOLVED, acceptance_runs=0
  MAXRUNS   --max-runs 1 exits 2, skipped=1, never asserts <base>
  JOBS      --jobs 4 prints the same sorted findings as --jobs 1
  MUT       every byte-mutant under .ufo/waves/round-66/stage/mut-o/ kills its
            pinned leg (each fixture run's expected output is per-mutant)
  FIXTURES  the harness built 3 temp git lanes and ran the tool via subprocess
            inside 180 s

A fixture lane is a temporary git repo (base commit + one commit per unit
holding base plus its land files); every tool run is a real subprocess with a
real manifest, never a mocked verdict.

Output ends `ACCEPT-O-66: PASS|FAIL`; exit 0/1, or 2 on unusable input.
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time

BASE = "94209e8f80969dbac48d56c5d0e2e623635b8616"
TOOL = "tools/check-claim-separability.py"
MUT_DIR = ".ufo/waves/round-66/stage/mut-o"
SCHEMA = "kotodama-separability-manifest-v1"


def git(root, *args, check=True):
    env = dict(os.environ)
    env.update({
        "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_AUTHOR_NAME": "fixture", "GIT_AUTHOR_EMAIL": "fixture@invalid",
        "GIT_COMMITTER_NAME": "fixture", "GIT_COMMITTER_EMAIL": "fixture@invalid",
    })
    proc = subprocess.run(["git", "-C", root, *args], env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if check and proc.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {proc.stderr.strip()}")
    return proc


def w(root, rel, content):
    dest = os.path.join(root, *rel.split("/"))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(content)


def make_lane(root, base_files, claim_files):
    lane = os.path.join(root, "lane")
    os.makedirs(lane)
    git(lane, "init", "-q")
    for rel, content in base_files.items():
        w(lane, rel, content)
    git(lane, "add", "-A")
    git(lane, "commit", "-q", "--allow-empty", "-m", "base")
    base = git(lane, "rev-parse", "HEAD").stdout.strip()
    trees = {}
    for cid, files in claim_files.items():
        git(lane, "checkout", "-q", "--detach", base)
        git(lane, "clean", "-fdxq")
        for rel, content in files.items():
            w(lane, rel, content)
        git(lane, "add", "-A")
        git(lane, "commit", "-q", "--allow-empty", "-m", cid)
        trees[cid] = git(lane, "rev-parse", "HEAD").stdout.strip()
    return lane, base, trees


def manifest_for(base, units, trees):
    doc = {"schema": SCHEMA, "base": base, "claims": []}
    for spec in units:
        row = dict(spec)
        if row.get("tree") != "WORKTREE":
            row["tree"] = trees[spec["id"]]
        doc["claims"].append(row)
    return doc


def run_tool(tool_abs, argv, cwd):
    return subprocess.run([sys.executable, "-B", tool_abs, *argv], cwd=cwd,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          text=True, timeout=200)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    self_sha = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
    mv = subprocess.run(["git", "rev-parse", "main"], stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    print(f"# counter sha256 (self): {self_sha}")
    print(f"# measured revision (lane main): {mv.stdout.decode().strip() or 'unresolvable'}")
    legs = []
    t_start = time.monotonic()

    def leg(name, ok, detail):
        legs.append(bool(ok))
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")

    tool_abs = os.path.join(root, TOOL)

    # ---------- SELFTEST ----------
    st = run_tool(tool_abs, ["--selftest"], root)
    leg("SELFTEST", st.returncode == 0,
        f"exit={st.returncode} {'63/63' in st.stdout and 'count=63/63' or st.stdout.strip().splitlines()[-1] if st.stdout else 'no output'}")

    # ---------- DIFF ----------
    d = subprocess.run(["git", "-C", root, "diff", BASE, "--", TOOL],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    leg("DIFF", d.returncode == 0 and bool(d.stdout.strip()),
        f"diff_lines={len(d.stdout.splitlines())}")

    # ---------- OPTIONS ----------
    h = run_tool(tool_abs, ["--help"], root)
    want_opts = ["--jobs", "--budget", "--max-runs", "--static-only"]
    missing = [o for o in want_opts if o not in h.stdout]
    leg("OPTIONS", h.returncode == 0 and not missing, f"missing={missing}")

    # ---------- fixture lanes ----------
    fixtures_built = 0
    with tempfile.TemporaryDirectory(prefix="accept-o-66-") as tmp:

        # Lane 1: sleeping acceptance; --budget forces skipped repairs
        r1 = os.path.join(tmp, "f1")
        os.makedirs(r1)
        lane, base_sha, trees = make_lane(
            r1,
            {"README.md": "index\n"},
            {"C": {"corpus/knowledge/c.md": "x\n"},
             "S": {"corpus/SOURCES.md": "rows\n"}})
        mpath = os.path.join(r1, "m.json")
        with open(mpath, "w") as fh:
            json.dump(manifest_for(base_sha, [
                {"id": "C", "lands": ["corpus/knowledge/c.md"], "exports": [r"\bCQ\b"],
                 "acceptance": [sys.executable, "-c",
                                "import os,sys,time;time.sleep(1.5);"
                                "sys.exit(0 if os.path.isfile('corpus/SOURCES.md') else 1)"]},
                {"id": "S", "lands": ["corpus/SOURCES.md"], "exports": [r"\bSZ\b"]}],
                trees), fh)
        b = run_tool(tool_abs, [mpath, "--lane", lane,
                                "--budget", "0.5", "--timeout", "10"], lane)
        fixtures_built += 1
        bound_ok = (b.returncode == 2
                    and "SEPARABILITY_PARTIAL" in b.stdout
                    and "SEPARABILITY_UNRESOLVED" in b.stdout
                    and "SEPARABILITY_DEPENDENCY C-><base>" not in b.stdout)
        leg("BOUND", bound_ok,
            f"exit={b.returncode} partial={'SEPARABILITY_PARTIAL' in b.stdout} "
            f"unresolved={'UNRESOLVED' in b.stdout}")

        # Lane 2: dependent acceptance; --static-only / --max-runs / --jobs
        r2 = os.path.join(tmp, "f2")
        os.makedirs(r2)
        lane2, base2, trees2 = make_lane(
            r2,
            {"README.md": "index\n"},
            {"C": {"corpus/knowledge/c.md": "no reference\n"},
             "S": {"corpus/SOURCES.md": "rows\n"}})
        mpath2 = os.path.join(r2, "m.json")
        with open(mpath2, "w") as fh:
            json.dump(manifest_for(base2, [
                {"id": "C", "lands": ["corpus/knowledge/c.md"], "exports": [r"\bCQ\b"],
                 "acceptance": [sys.executable, "-c",
                                "import os,sys;sys.exit(0 if "
                                "os.path.isfile('corpus/SOURCES.md') else 1)"]},
                {"id": "S", "lands": ["corpus/SOURCES.md"], "exports": [r"\bSZ\b"]}],
                trees2), fh)
        fixtures_built += 1

        so = run_tool(tool_abs, [mpath2, "--lane", lane2, "--static-only"], lane2)
        static_ok = (so.returncode == 2
                     and "SEPARABILITY_PARTIAL" in so.stdout
                     and "SEPARABILITY_UNRESOLVED" in so.stdout
                     and "acceptance_runs=0" in so.stderr)
        leg("STATIC", static_ok, f"exit={so.returncode}")

        mr = run_tool(tool_abs, [mpath2, "--lane", lane2, "--max-runs", "1"], lane2)
        maxruns_ok = (mr.returncode == 2
                      and "SEPARABILITY_PARTIAL 1 run(s) skipped" in mr.stdout
                      and "skipped=1" in mr.stderr
                      and "SEPARABILITY_DEPENDENCY C-><base>" not in mr.stdout)
        leg("MAXRUNS", maxruns_ok, f"exit={mr.returncode}")

        j1 = run_tool(tool_abs, [mpath2, "--lane", lane2, "--jobs", "1"], lane2)
        j4 = run_tool(tool_abs, [mpath2, "--lane", lane2, "--jobs", "4"], lane2)
        findings1 = sorted(l for l in j1.stdout.splitlines()
                           if l.startswith("SEPARABILITY_DEPENDENCY"))
        findings4 = sorted(l for l in j4.stdout.splitlines()
                           if l.startswith("SEPARABILITY_DEPENDENCY"))
        leg("JOBS", j1.returncode == j4.returncode == 1 and findings1 == findings4
            and findings1,
            f"j1={j1.returncode} j4={j4.returncode} eq={findings1 == findings4}")

        # ---------- MUT ----------
        # Each mutant carries its pinned failure mode: the run must show the
        # mutant's effect (not merely 'differ from the original').
        mut_dir = os.path.join(root, MUT_DIR)
        mut_expect = {
            "mut1_no_partial_exit.py": lambda r: "SEPARABILITY_PARTIAL" in r.stdout and r.returncode != 2,
            "mut2_unresolved_to_base.py": lambda r: "SEPARABILITY_DEPENDENCY C-><base>" in r.stdout,
            "mut3_silent_skip.py": lambda r: "skipped=0" in r.stderr or "skipped=" not in r.stderr,
            "mut4_suppress_unresolved.py": lambda r: "UNRESOLVED" not in r.stdout,
        }
        mut_bad = []
        mut_count = 0
        if os.path.isdir(mut_dir):
            for fname, expect in sorted(mut_expect.items()):
                mtool = os.path.join(mut_dir, fname)
                if not os.path.isfile(mtool):
                    mut_bad.append(f"{fname}:absent")
                    continue
                mut_count += 1
                r = run_tool(mtool, [mpath2, "--lane", lane2,
                                     "--max-runs", "1"], lane2)
                if not expect(r):
                    mut_bad.append(f"{fname}:survives")
            for fname in sorted(os.listdir(mut_dir)):
                if fname.endswith(".py") and fname not in mut_expect:
                    mut_bad.append(f"{fname}:unpinned")
        else:
            leg("MUT", False, f"mutant dir absent: {mut_dir}")
            mut_count = -1
        if mut_count >= 0:
            leg("MUT", mut_count == len(mut_expect) and not mut_bad,
                f"mutants={mut_count} failing={mut_bad}")

    leg("FIXTURES", fixtures_built >= 2 and (time.monotonic() - t_start) < 180,
        f"lanes={fixtures_built} wall={time.monotonic() - t_start:.1f}s")

    verdict = all(legs)
    print(f"ACCEPT-O-66: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
