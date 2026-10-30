#!/usr/bin/env python3
"""ref-guard.py — minimal HONEST reference guard for the noop-killer battery.

Purpose: prove the kill fixture is not vacuous. Every battery leg must read
GUARD-OK against this reference. It implements the semantics the O claim
draft names, in the smallest possible form, using the ledger grammar the
killer writes:

  pair.observe = ["git", "show", "<rev>:<path>", "|parse", "<python-regex>"]

Behaviour:
  - observation runs against committed bytes only (`git show <rev>:<path>`);
  - approved grammar is exactly that 5-element form with <rev> a 40-hex commit
    — anything else (branch, interpreter, shell, extra args) is refused exit 2;
  - per pair: observed token echoed as `pair <id> observed <token>`;
    exit 1 if observed != observed_at_base (record mismatch) or if
    stated_token == observed (the record is a no-op lie);
    exit 0 + `GUARD: PASS` only when every pair is green.
  - --selftest builds a fresh-nonce fixture repo, runs the clean ledger through
    the real batch logic, and leaves the fixture + selftest-manifest.json under
    --work so the killer re-derives every observed token.

This is a behavioural spec for tools/ledger-token-guard.py, not the deliverable.
"""
import json
import os
import re
import secrets
import subprocess
import sys

PROBE = "probe.txt"
HEX40 = re.compile(r"^[0-9a-f]{40}$")


def _git(args, cwd):
    env = dict(os.environ, GIT_AUTHOR_NAME="ref", GIT_AUTHOR_EMAIL="r@x",
               GIT_COMMITTER_NAME="ref", GIT_COMMITTER_EMAIL="r@x")
    return subprocess.run(["git"] + args, cwd=cwd, env=env, capture_output=True,
                          text=True, timeout=30)


def observe(repo, observe):
    """Run the approved read-only observation; return (token, error)."""
    if (not isinstance(observe, list) or len(observe) != 5 or observe[0] != "git"
            or observe[1] != "show" or observe[3] != "|parse"):
        return None, "refused: grammar outside approved read-only form"
    target = observe[2]
    if ":" not in target:
        return None, "refused: target not <rev>:<path>"
    rev, path = target.split(":", 1)
    if not HEX40.match(rev):
        return None, "refused: revision is not an immutable 40-hex commit"
    if os.path.isabs(path) or ".." in path.split("/"):
        return None, "refused: path escapes repo"
    r = _git(["show", "%s:%s" % (rev, path)], cwd=repo)
    if r.returncode != 0:
        return None, "observe failed: %s" % r.stderr.strip()
    m = re.search(observe[4], r.stdout, re.M)
    if not m:
        return None, "parse found no token"
    return m.group(1), None


def guard_batch(ledger_path, repo):
    doc = json.load(open(ledger_path))
    if not repo:
        print("GUARD: FAIL no repo", file=sys.stderr)
        return 2
    for pr in doc["pairs"]:
        token, err = observe(repo, pr.get("observe"))
        if err:
            print("GUARD: REFUSE %s %s" % (pr["id"], err), file=sys.stderr)
            return 2
        print("pair %s observed %s" % (pr["id"], token))
        if token != pr["observed_at_base"]:
            print("GUARD: FAIL %s observed_at_base mismatch" % pr["id"], file=sys.stderr)
            return 1
        if pr["stated_token"] == token:
            print("GUARD: FAIL %s stated_token equals actual observation" % pr["id"],
                  file=sys.stderr)
            return 1
    print("GUARD: PASS pairs=%d" % len(doc["pairs"]))
    return 0


def guard_selftest(work_dir):
    os.makedirs(work_dir, exist_ok=True)
    repo = os.path.join(work_dir, "fixture")
    os.makedirs(repo, exist_ok=True)
    _git(["init", "-q", "-b", "main", "."], cwd=repo)
    token = "n-" + secrets.token_hex(8)
    with open(os.path.join(repo, PROBE), "w") as f:
        f.write("calibration probe\ntoken: %s\n" % token)
    _git(["add", PROBE], cwd=repo)
    _git(["commit", "-q", "-m", "probe"], cwd=repo)
    commit = _git(["rev-parse", "HEAD"], cwd=repo).stdout.strip()

    ledger = {"pairs": [{"id": "G", "stated_token": "S884-stated-decoy",
                         "observed_at_base": token,
                         "observe": ["git", "show", "%s:%s" % (commit, PROBE),
                                     "|parse", r"^token: (.+)$"]}]}
    ledger_path = os.path.join(work_dir, "ledger.json")
    with open(ledger_path, "w") as f:
        json.dump(ledger, f)
    code = guard_batch(ledger_path, repo)
    print("selftest: clean -> exit=%d" % code)
    if code != 0:
        return 1
    manifest = [{"scenario": "clean", "fixture_commit": commit, "repo_dir": "fixture",
                 "ledger_path": "ledger.json", "pair_id": "G",
                 "observed_token": token, "expect_exit": 0}]
    with open(os.path.join(work_dir, "selftest-manifest.json"), "w") as f:
        json.dump(manifest, f, indent=1)
    print("SELFTEST: 1/1")
    return 0


def main():
    args = sys.argv[1:]
    if "--selftest" in args:
        return guard_selftest(args[args.index("--work") + 1])
    ledger = args[args.index("--ledger") + 1]
    repo = args[args.index("--repo") + 1] if "--repo" in args else None
    return guard_batch(ledger, repo)


if __name__ == "__main__":
    sys.exit(main())
