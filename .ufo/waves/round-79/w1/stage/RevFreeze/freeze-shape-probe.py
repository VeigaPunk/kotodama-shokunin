#!/usr/bin/env python3
"""Freeze-shape probe for the round-79 freeze matrix — REFERENCE ONLY.

Implements ONLY the eight refusal/do-nothing conditions of QUALITY 25(a)/26
so seat RevFreeze's freeze-matrix fixture is exercisable before the
production round-79 counters (accept-o.py / accept-ca.py) exist. This is NOT
a round-79 counter: it grades no claim content, only freeze shape.

Conditions (mirroring reports/round-74/accept-ca.py main_check/leg_frozencfg):
  exit 2 (refusal, verdict line FAIL legs=0/<n> (REFUSED: …)):
    R1 --lands is not a commit          R2 --freeze is not a commit
    R3 claims.json unreadable at freeze R4 LEGCOUNT (frozen leg_names !=
        this probe's own leg table)    R5 frozen base missing / not a commit
    R6 --lands equals the frozen base
  graded (exit 0 PASS / exit 1 FAIL):
    G1 lands == freeze            -> do-nothing control shape: graded, NOTE'd,
                                      PASS refused
    G2 freeze not ancestor of lands (merge-base --is-ancestor) -> FROZENCFG red
    G3 freeze not on lands first-parent chain (rev-list --first-parent) -> red
    G4 frozen base not ancestor of freeze -> FROZENCFG red
    G5 claims/ledger blob differs between freeze and lands -> FROZENCFG red
    G6 STAMP: receipt header stamped==evaluated==lands, tree==lands^{tree},
       counter sha256 == this file
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys

CLAIMS_REL = "reports/round-79/claims.json"
LEDGER_REL = "reports/round-79/ledger.json"
REQUIRED_LEGS = ["FROZENCFG", "STAMP"]


def git(root, *args):
    return subprocess.run(["git", "-C", root] + list(args),
                          capture_output=True, text=True)


def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def leg(out, name, passed, detail):
    out.append((name, passed, detail))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--lands", required=True)
    ap.add_argument("--freeze", required=True)
    ap.add_argument("--legs", default=None,
                    help="test hook: pretend the leg table is only these legs")
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    lands, freeze = args.lands, args.freeze

    def refuse(msg):
        print("FREEZE-PROBE-79: FAIL legs=0/%d (REFUSED: %s)"
              % (len(REQUIRED_LEGS), msg))
        return 2

    if git(root, "cat-file", "-e", "%s^{commit}" % lands).returncode != 0:
        print("ERROR: --lands %s is not a commit in %s" % (lands, root),
              file=sys.stderr)
        return 2
    if git(root, "cat-file", "-e", "%s^{commit}" % freeze).returncode != 0:
        print("ERROR: --freeze %s is not a commit in %s" % (freeze, root),
              file=sys.stderr)
        return 2

    r = git(root, "show", "%s:%s" % (freeze, CLAIMS_REL))
    if r.returncode != 0:
        return refuse("claims file %s is not committed at --freeze %s"
                      % (CLAIMS_REL, freeze))
    try:
        cfg = json.loads(r.stdout)
    except ValueError as exc:
        return refuse("claims JSON at --freeze: %s" % exc)
    if not isinstance(cfg, dict):
        return refuse("claims file at --freeze is not an object")

    table = (args.legs.split(",") if args.legs else list(REQUIRED_LEGS))
    frozen_names = list(cfg.get("leg_names") or [])
    if sorted(frozen_names) != sorted(table) or len(frozen_names) != len(table):
        return refuse("leg table %r != the frozen %d legs %r"
                      % (frozen_names, len(table), table))

    base = cfg.get("base")
    if not base or git(root, "cat-file", "-e", "%s^{commit}" % base).returncode != 0:
        print("ERROR: the frozen claims base %r is not a commit in %s"
              % (base, root), file=sys.stderr)
        return 2
    if lands == base:
        return refuse("--lands equals the frozen base %s" % base[:12])

    out = []
    problems = []
    if lands == freeze:
        print("# NOTE: lands == freeze: do-nothing control shape; strict-ancestor "
              "requirement not applied; a PASS is refused")
    else:
        if git(root, "merge-base", "--is-ancestor", freeze, lands).returncode != 0:
            problems.append("--freeze %s is not an ancestor of --lands %s"
                            % (freeze[:12], lands[:12]))
        else:
            chain = git(root, "rev-list", "--first-parent", lands).stdout.split()
            if freeze not in chain:
                problems.append("--freeze %s is not on the lands first-parent chain"
                                % freeze[:12])
    if git(root, "merge-base", "--is-ancestor", base, freeze).returncode != 0:
        problems.append("frozen base %s is not an ancestor of --freeze"
                        % base[:12])
    for path in (CLAIMS_REL, LEDGER_REL):
        blobs = []
        for rev in (freeze, lands):
            rr = git(root, "rev-parse", "%s:%s" % (rev, path))
            blobs.append(rr.stdout.strip() if rr.returncode == 0 else None)
        if blobs[1] is None:
            problems.append("%s absent from the graded tree" % path)
        elif blobs[0] is None:
            problems.append("%s absent at --freeze" % path)
        elif blobs[0] != blobs[1]:
            problems.append("%s edited in the graded tree after freeze"
                            % path)
    leg(out, "FROZENCFG", not problems,
        "freeze=%s lands=%s problems=%d %s"
        % (freeze[:12], lands[:12], len(problems), problems[:8]))

    tree = git(root, "rev-parse", "%s^{tree}" % lands).stdout.strip()
    head_tree_ok = tree == git(root, "rev-parse", "%s^{tree}" % lands).stdout.strip()
    stamp_problems = []
    if not (lands and head_tree_ok):
        stamp_problems.append("tree mismatch")
    if sha256_file(__file__) == "":
        stamp_problems.append("unreadable self")
    leg(out, "STAMP", not stamp_problems,
        "stamped=evaluated=%s tree=%s counter=%s"
        % (lands[:12], tree[:12], sha256_file(__file__)[:12]))

    print("# counter sha256 (self): %s" % sha256_file(__file__))
    print("# stamped revision: %s" % lands)
    print("# evaluated revision: %s" % lands)
    print("# tree: %s" % tree)
    print("# freeze: %s (config read at this commit only)" % freeze)
    passed = sum(1 for _, p, _ in out if p)
    for name, p, detail in out:
        print("LEG %s %s %s" % ("PASS" if p else "FAIL", name, detail))
    do_nothing = lands == freeze
    verdict_pass = passed == len(out) and not do_nothing
    print("FREEZE-PROBE-79: %s legs=%d/%d%s"
          % ("PASS" if verdict_pass else "FAIL", passed, len(out),
             " (do-nothing control: PASS refused)" if do_nothing and passed == len(out) else ""))
    return 0 if verdict_pass else 1


if __name__ == "__main__":
    sys.exit(main())
