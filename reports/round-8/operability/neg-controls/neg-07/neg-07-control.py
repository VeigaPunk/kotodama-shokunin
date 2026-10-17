#!/usr/bin/env python3
"""Negative control for round-8 defect R8-O07 — defect index 3 = review 26 §3 D2
at tools/gates/naming-collision-gate.py (inventory id R26-D2-naming).

Defect under control: the naming gate let duplicate mapping keys last-win with
no diagnostic, in both flow mappings (`{case: contrastive, case: display-only}`)
and block mappings (a second top-level `orthography:` line). The review's
verdict-flip counterexample: with a single `orthography: {case: contrastive}`
the packet emits NAME-CASE; adding a stale second
`orthography: {case: display-only}` silently removes NAME-CASE and changes the
emitted ids — a stale key changes the audit verdict with no duplicate-key
finding. Inventory `evidence_pointer`: "Repro: 'orthography: {case:
contrastive}' -> {CROSS-HOLD, NAME-CASE, PHON-INVENTORY}; adding a second
'orthography: {case: display-only}' -> {CROSS-HOLD, NAME-REUSE} — a stale key
silently flips the verdict with no duplicate-key finding." Inventory
`suggested_control`: "assert exit 2 + a duplicate-key finding naming
'orthography'; fail-before = the NAME-REUSE verdict."

Contract (same protocol as neg-04):
  * pointed at the LIVE (post-fix) gate -> every check passes, exit 0;
  * pointed at PRE-FIX bytes (`--gate <pre-fix copy>`) -> the duplicate-key
    checks observe the pre-fix pattern (rc=1: last-wins verdict, no
    duplicate-key finding) and the control exits 1, naming that pattern.

Isolation: probe packets are written only into tempfile.TemporaryDirectory();
the gate under test is invoked as a subprocess; nothing under the repository
is written by this control. Probes are built by textual replacement inside the
committed fixture (read-only), so every probe is a complete packet.

Usage:
    python3 neg-07-control.py [--gate PATH]

Default gate path is the lane's live tool, resolved from this file's location:
    <repo>/tools/gates/naming-collision-gate.py
"""

import argparse
import hashlib
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
DEFAULT_GATE = os.path.join(REPO, "tools", "gates", "naming-collision-gate.py")
FIXTURE = os.path.join(REPO, "tools", "gates", "fixtures",
                       "naming-collision-gate.yml")

# Review 26 section 0 pin for the pre-fix bytes (blob fe34faa == e7ca0fa).
PREFIX_SHA256 = "8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526"

# The fixture's committed orthography block, replaced per probe.
ORTHO_BLOCK = (
    "orthography:\n"
    "  script: latin\n"
    "  case: display-only\n"
    "  separators: [\"-\"]\n"
)
# The nested block inside orthography, for the nested-duplicate probe.
NESTED_BLOCK = (
    "  script: latin\n"
    "  case: display-only\n"
)

PROBES = {
    "dup-block-orthography": (
        ORTHO_BLOCK,
        "orthography: {case: contrastive}\n"
        "orthography: {case: display-only}\n",
    ),
    "dup-flow-case": (
        ORTHO_BLOCK,
        "orthography: {case: contrastive, case: display-only}\n",
    ),
    "dup-nested-block-case": (
        NESTED_BLOCK,
        "  case: contrastive\n"
        "  case: display-only\n",
    ),
    "single-contrastive-twin": (
        ORTHO_BLOCK,
        "orthography: {case: contrastive}\n",
    ),
}


def build_probe(key):
    with open(FIXTURE, encoding="utf-8") as handle:
        text = handle.read()
    old, new = PROBES[key]
    if text.count(old) != 1:
        raise SystemExit("NEG-07 SETUP ERROR: fixture anchor occurs %d times"
                         % text.count(old))
    return text.replace(old, new, 1)


def run_gate(gate, text, timeout=30):
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "packet.yml")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
        proc = subprocess.run(
            [sys.executable, gate, path],
            capture_output=True, text=True, timeout=timeout)
        return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def finding_ids(output):
    ids = []
    for line in output.splitlines():
        if line.startswith("FINDING "):
            ids.append(line.split(":", 1)[0].split()[1])
    return ids


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gate", default=DEFAULT_GATE)
    args = ap.parse_args()

    gate = os.path.abspath(args.gate)
    if not os.path.isfile(gate):
        print("NEG-07 ERROR: gate not found: %s" % gate)
        return 2
    with open(gate, "rb") as handle:
        digest = hashlib.sha256(handle.read()).hexdigest()
    print("NEG-07 gate under test: %s" % gate)
    print("NEG-07 gate sha256: %s" % digest)
    if digest == PREFIX_SHA256:
        print("NEG-07 note: this is the review-26 pinned PRE-FIX byte copy "
              "(8c5afb0a...); checks below are expected to FAIL.")

    failures = []
    checks = 0

    def check(name, payload, predicate, describe):
        nonlocal checks
        checks += 1
        rc, out = run_gate(gate, payload)
        ids = finding_ids(out)
        ok = predicate(rc, ids, out)
        print("NEG-07 %-28s rc=%-3s ids=%-12s %s"
              % (name, rc, ",".join(ids[:3]) or "-", "PASS" if ok else "FAIL"))
        if not ok:
            failures.append("%s: %s" % (name, describe(rc, ids, out)))

    # C1: duplicate block-level keys must be rejected, naming the key.
    check(
        "dup-block-orthography",
        build_probe("dup-block-orthography"),
        lambda rc, ids, out: rc == 2 and ids == ["G-DATA"]
        and "duplicate key 'orthography'" in out,
        lambda rc, ids, out: (
            "PRE-FIX PATTERN OBSERVED: rc=%s ids=%s -- the second "
            "'orthography:' block last-won with no duplicate-key finding "
            "(stale key silently changed the verdict); expected rc=2 with "
            "G-DATA and \"duplicate key 'orthography'\". output=%r"
            % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C2: duplicate keys inside a flow mapping must be rejected.
    check(
        "dup-flow-case",
        build_probe("dup-flow-case"),
        lambda rc, ids, out: rc == 2 and ids == ["G-DATA"]
        and "duplicate key 'case'" in out,
        lambda rc, ids, out: (
            "PRE-FIX PATTERN OBSERVED: rc=%s ids=%s -- the second flow-mapping "
            "'case:' last-won with no duplicate-key finding; expected rc=2 "
            "with G-DATA and \"duplicate key 'case'\". output=%r"
            % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C3: duplicate keys in a nested block mapping must be rejected.
    check(
        "dup-nested-block-case",
        build_probe("dup-nested-block-case"),
        lambda rc, ids, out: rc == 2 and ids == ["G-DATA"]
        and "duplicate key 'case'" in out,
        lambda rc, ids, out: (
            "PRE-FIX PATTERN OBSERVED: rc=%s ids=%s -- the nested duplicate "
            "'case:' last-won with no duplicate-key finding; expected rc=2 "
            "with G-DATA and \"duplicate key 'case'\". output=%r"
            % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C4 (positive twin): the single-key packet must still evaluate, with the
    # contrastive casing routed (NAME-CASE) -- no over-rejection.
    check(
        "single-contrastive-twin",
        build_probe("single-contrastive-twin"),
        lambda rc, ids, out: rc == 1 and "NAME-CASE" in ids
        and "duplicate key" not in out,
        lambda rc, ids, out: (
            "regression: the single-key contrastive packet no longer "
            "evaluates with NAME-CASE: rc=%s ids=%s output=%r"
            % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C5 (positive): the pristine fixture still evaluates to rc=1 unchanged.
    with open(FIXTURE, encoding="utf-8") as handle:
        pristine = handle.read()
    check(
        "pristine-fixture-unchanged",
        pristine,
        lambda rc, ids, out: rc == 1 and "duplicate key" not in out,
        lambda rc, ids, out: (
            "regression: pristine fixture no longer evaluates to rc=1: "
            "rc=%s ids=%s output=%r" % (rc, ids, out.strip().splitlines()[:3])),
    )

    if failures:
        print("NEG-07 RESULT: FAIL (%d/%d checks)" % (len(failures), checks))
        for line in failures:
            print("NEG-07 FAILURE: %s" % line)
        return 1
    print("NEG-07 RESULT: PASS (%d/%d checks)" % (checks, checks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
