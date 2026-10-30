#!/usr/bin/env python3
"""stub-guards.py — simulated cheapest no-work attacks on the O guard.

Mode 1 "canned-selftest": the classic print-stub. Batch mode echoes the
ledger's stated_token as the "observed" token (no committed byte is ever
read); --selftest prints a plausible green receipt and exits 0 without
building any fixture.

Mode 2 "echo-lookup": work-shaped stub. Batch echoes stated_token;
--selftest leaves a manifest, but the observed tokens in it are echoed from
the ledger (stated values / copied constants), not derived from the fixture
commits it wrote.

Both are the attacks QUALITY 28 warns about ("a four-line stub printing the
expected line") and QUALITY 25 J4 ("a receipt typed without the run does not
count"). noop-killer.py must kill both.
"""
import json
import os
import subprocess
import sys


def _ledger(args):
    p = args[args.index("--ledger") + 1]
    return json.load(open(p))


def _batch(mode, args):
    doc = _ledger(args)
    # no-work observe leg: echo the stated token; never run git show.
    for pr in doc["pairs"]:
        print("pair %s observed %s" % (pr["id"], pr["stated_token"]))
    print("GUARD: PASS pairs=%d (simulated %s stub)" % (len(doc["pairs"]), mode))
    return 0


def _selftest_canned(args):
    # Canned receipt: the shape a QUALITY-23-addendum grep wants, printed only.
    work = args[args.index("--work") + 1]
    os.makedirs(work, exist_ok=True)
    print("selftest: clean -> exit=0 OBS=PASS MISMATCH=PASS REFUSE=PASS")
    print("selftest: m1-stated-eq-actual -> exit=1 OBS=FAIL")
    print("selftest: m2-observed-tampered -> exit=1 OBS=FAIL")
    print("selftest: m3-constant-printer -> exit=2 REFUSE=PASS")
    print("selftest: m4-mutable-revision -> exit=2 REFUSE=PASS")
    print("SELFTEST: 5/5 (simulated canned-selftest stub: no fixture was built)")
    return 0


def _selftest_echo(args):
    # Work-shaped: build a repo and a manifest, but observed tokens are echoed
    # constants, not bytes read from the commits.
    work = args[args.index("--work") + 1]
    os.makedirs(work, exist_ok=True)
    repo = os.path.join(work, "fixture")
    os.makedirs(repo, exist_ok=True)
    env = dict(os.environ, GIT_AUTHOR_NAME="stub", GIT_AUTHOR_EMAIL="s@x",
               GIT_COMMITTER_NAME="stub", GIT_COMMITTER_EMAIL="s@x")
    with open(os.path.join(repo, "probe.txt"), "w") as f:
        f.write("calibration probe\ntoken: n-realfixturetoken\n")
    for c in (["git", "init", "-q", "-b", "main", "."],
              ["git", "add", "probe.txt"],
              ["git", "commit", "-q", "-m", "probe"]):
        subprocess.run(c, cwd=repo, env=env, capture_output=True)
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo,
                            env=env, capture_output=True, text=True).stdout.strip()
    manifest = [{
        "scenario": "clean", "fixture_commit": commit, "repo_dir": "fixture",
        "ledger_path": "ledger.json", "pair_id": "G",
        "observed_token": "echoed-not-derived",   # <-- the lie: not read from commit
        "expect_exit": 0,
    }]
    with open(os.path.join(work, "selftest-manifest.json"), "w") as f:
        json.dump(manifest, f, indent=1)
    print("selftest: clean -> exit=0 OBS=PASS")
    print("SELFTEST: 1/1 (simulated echo-lookup stub)")
    return 0


def main():
    mode = sys.argv[1]
    args = sys.argv[2:]
    if "--selftest" in args:
        return _selftest_canned(args) if mode == "canned-selftest" else _selftest_echo(args)
    return _batch(mode, args)


if __name__ == "__main__":
    sys.exit(main())
