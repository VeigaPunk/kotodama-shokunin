#!/usr/bin/env python3
"""Round-79 freeze/ancestry/do-nothing fixture matrix (seat RevFreeze, W1 pre-data).

Builds a DETERMINISTIC isolated fixture git repository and runs a scenario
matrix against a counter command template. The template is a shell string
with {repo} {lands} {freeze} placeholders, e.g.:

  python3 -B freeze-matrix.py \
    --repo /path/to/fixture.git \
    --counter-cmd 'python3 -B reports/round-79/accept-ca.py --root {repo} --lands {lands} --freeze {freeze} --fleet-root /home/vgpnk/Projects/shokunin'

With no --counter-cmd, the bundled freeze-shape probe (freeze-shape-probe.py,
same directory) is used: a MINIMAL reference implementing ONLY the eight
refusal/do-nothing conditions so the matrix is exercisable before the
production counters exist. It is a shape reference, NOT a round-79 counter.

Fixture topology (branch main, first-parent chain C0 -> C1 -> C2 -> C3/C2m):

  C0  "base"      LOG.md, base.txt
  C1  "freeze"    + reports/round-79/claims.json, ledger.json,
                  counters/accept-dummy.py        (the round-79 freeze shape)
  C2  "landing"   + reports/round-79/correction.json   (the claim landing)
  C3  "amended"   C2 with claims.json EDITED post-freeze (FROZENCFG red)
  S1  side commit off C0, never merged            (freeze: not an ancestor)
  S2  side commit off C1, merged --no-ff at C2m   (freeze: ancestor but NOT
                                                  on the lands first-parent chain)

Scenarios (expected against the bundled shape probe):
  s01_green              freeze=C1 lands=C2    -> exit 0 (strict first-parent
                                                   ancestor; freeze blobs == lands blobs)
  s02_do_nothing         freeze=C1 lands=C1    -> graded, PASS refused (exit 1)
  s03_lands_eq_base      freeze=C1 lands=C0    -> exit 2 (refused: lands==base)
  s04_off_first_parent   freeze=S2 lands=C2m   -> exit 1 FROZENCFG red
  s05_not_ancestor       freeze=S1 lands=C2    -> exit 1 FROZENCFG red
  s06_claims_amended     freeze=C1 lands=C3    -> exit 1 FROZENCFG red
  s07_freeze_non_commit  freeze=0000..0 lands=C2 -> exit 2
  s08_lands_non_commit   freeze=C1 lands=0000..0 -> exit 2
  s09_claims_not_at_freeze freeze=C0 lands=C2  -> exit 2 (claims.json absent at freeze)
  s10_legcount           freeze=C1 lands=C2 with --legs FROZENCFG ONLY
                                                   -> exit 2 refused LEGCOUNT

Determinism: GIT_AUTHOR/COMMITTER_DATE and identities are fixed, so the
rebuilt fixture's commit ids are stable and the receipt can pin them.
"""
import argparse
import json
import os
import shlex
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

ENV_BASE = {
    "GIT_AUTHOR_NAME": "RevFreeze Fixture",
    "GIT_AUTHOR_EMAIL": "revfreeze@fixture.local",
    "GIT_COMMITTER_NAME": "RevFreeze Fixture",
    "GIT_COMMITTER_EMAIL": "revfreeze@fixture.local",
    "GIT_AUTHOR_DATE": "2026-10-30T00:00:00+00:00",
    "GIT_COMMITTER_DATE": "2026-10-30T00:00:00+00:00",
    "GIT_CONFIG_NOSYSTEM": "1",
    "HOME": "/nonexistent-fixture-home",
}

CLAIMS = {
    "round": 79,
    "claims": {
        "O": {"legs": ["FROZENCFG", "STAMP"]},
        "Ca": {"legs": ["FROZENCFG", "STAMP"]},
    },
    "leg_names": ["FROZENCFG", "STAMP"],
    "ledger_rel": "reports/round-79/ledger.json",
    "claims_rel": "reports/round-79/claims.json",
}
CLAIMS_REL = "reports/round-79/claims.json"
LEDGER_REL = "reports/round-79/ledger.json"


def git(repo, *args, check=True):
    env = dict(os.environ)
    env.update(ENV_BASE)
    r = subprocess.run(["git", "-C", repo] + list(args),
                       capture_output=True, text=True, env=env)
    if check and r.returncode != 0:
        raise SystemExit("fixture git %s failed: %s" % (args, r.stderr))
    return r


def write(repo, rel, text):
    p = os.path.join(repo, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        f.write(text)


def commit(repo, msg):
    git(repo, "add", "-A")
    git(repo, "commit", "-m", msg, "--no-gpg-sign")
    return git(repo, "rev-parse", "HEAD").stdout.strip()


def build(repo):
    if os.path.exists(repo):
        raise SystemExit("fixture repo %s already exists; remove it first" % repo)
    os.makedirs(repo)
    subprocess.run(["git", "-C", repo, "init", "-q", "-b", "main"],
                   check=True, env={**os.environ, **ENV_BASE})
    git(repo, "config", "user.name", ENV_BASE["GIT_AUTHOR_NAME"])
    git(repo, "config", "user.email", ENV_BASE["GIT_AUTHOR_EMAIL"])

    write(repo, "LOG.md", "# fixture log\n\nbase round-79 freeze matrix\n")
    write(repo, "base.txt", "base bytes\n")
    C0 = commit(repo, "base")
    CLAIMS["base"] = C0

    os.makedirs(os.path.join(repo, "reports/round-79"), exist_ok=True)
    write(repo, CLAIMS_REL, json.dumps(CLAIMS, indent=1, sort_keys=True) + "\n")
    write(repo, LEDGER_REL, "{}\n")
    write(repo, "counters/accept-dummy.py", "# frozen counter placeholder\n")
    C1 = commit(repo, "freeze: round-79 claims+ledger+counters")

    # side commit S1 off C1, never merged: carries claims.json but is NOT an
    # ancestor of main -> exercises the graded "not an ancestor" FROZENCFG red
    git(repo, "checkout", "-q", "-b", "side-unmerged", C1)
    write(repo, "side.txt", "unmerged side\n")
    S1 = commit(repo, "side: unmerged, carries claims")

    # side commit S2 off C1, to be merged --no-ff (ancestor, off first-parent)
    git(repo, "checkout", "-q", "-b", "side-merged", C1)
    write(repo, "side2.txt", "merged side\n")
    S2 = commit(repo, "side: to-be-merged")

    git(repo, "checkout", "-q", "main")
    write(repo, "reports/round-79/correction.json",
          json.dumps({"correction": "fixture landing"}, indent=1) + "\n")
    C2 = commit(repo, "landing: correction")

    git(repo, "merge", "-q", "--no-ff", "-m", "merge side-merged", S2)
    C2m = git(repo, "rev-parse", "HEAD").stdout.strip()

    claims2 = dict(CLAIMS)
    claims2["leg_names"] = ["FROZENCFG"]  # post-freeze narrowing
    write(repo, CLAIMS_REL, json.dumps(claims2, indent=1, sort_keys=True) + "\n")
    C3 = commit(repo, "amend: claims.json narrowed after freeze")

    git(repo, "checkout", "-q", "main")
    return {"C0": C0, "C1": C1, "C2": C2, "C2m": C2m, "C3": C3,
            "S1": S1, "S2": S2}


def run(repo, cmd):
    env = dict(os.environ)
    env.update(ENV_BASE)
    return subprocess.run(cmd, shell=True, capture_output=True, text=True,
                          env=env, cwd=HERE)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--counter-cmd",
                    default="python3 -B %s --root {repo} --lands {lands} "
                            "--freeze {freeze}" % os.path.join(HERE, "freeze-shape-probe.py"))
    args = ap.parse_args()

    revs = build(args.repo)

    # tag the anchors so a rebuilt fixture is self-describing
    for name, sha in revs.items():
        git(args.repo, "tag", "-f", "fixture/%s" % name, sha)

    NONCOMMIT = "0" * 40
    scenarios = [
        ("s01_green", "C1", "C2", ""),
        ("s02_do_nothing", "C1", "C1", ""),
        ("s03_lands_eq_base", "C1", "C0", ""),
        ("s04_off_first_parent", "S2", "C2m", ""),
        ("s05_not_ancestor", "S1", "C2", ""),
        ("s06_claims_amended_at_lands", "C1", "C3", ""),
        ("s07_freeze_non_commit", "C1", NONCOMMIT, ""),
        ("s08_lands_non_commit", NONCOMMIT, "C2", ""),
        ("s09_claims_not_at_freeze", "C0", "C2", ""),
        ("s10_legcount", "C1", "C2", "--legs FROZENCFG"),
    ]

    def rev(key):
        return key if len(key) == 40 and set(key) == {"0"} else revs[key]

    print("# freeze-matrix: repo=%s" % os.path.abspath(args.repo))
    print("# counter-cmd template: %s" % args.counter_cmd)
    for name, sha in sorted(revs.items()):
        print("# fixture rev %s=%s" % (name, sha))
    print("#")
    all_ok = True
    for name, freeze_key, lands_key, extra in scenarios:
        cmd = args.counter_cmd.format(repo=os.path.abspath(args.repo),
                                      lands=rev(lands_key),
                                      freeze=rev(freeze_key))
        if extra:
            cmd = cmd + " " + extra
        r = run(args.repo, cmd)
        out = (r.stdout + r.stderr).strip()
        print("=== %s" % name)
        print("cmd: %s" % cmd)
        print("exit: %d" % r.returncode)
        for line in out.splitlines():
            print("out: %s" % line)
        print("---")
        sys.stdout.flush()
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
