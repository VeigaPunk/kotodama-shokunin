#!/usr/bin/env python3
"""Negative control for round-8 defect R8-O04 (supplement review 26, defect D1).

Defect under control: tools/gates/phonology-sanity-gate.py silently closed an
unterminated flow sequence (`consonants: [p, t, k` became the 3-item list
['p', 't', 'k']), so the gate audited a document that is not valid YAML and
exited 1 with findings instead of the documented exit 2 "could-not-evaluate".

Contract:
  * pointed at the LIVE (post-fix) gate -> every check passes, exit 0;
  * pointed at PRE-FIX bytes (`--gate <pre-fix copy>`) -> the truncated-flow
    checks observe the pre-fix pattern (rc=1 and an evaluation finding printed
    for invalid YAML) and the control exits 1, naming the pattern.

Isolation: payloads are written only into a tempfile.TemporaryDirectory();
the gate under test is invoked as a subprocess; nothing under the repository
is written by this control.

Usage:
    python3 neg-04-control.py [--gate PATH]

Default gate path is the lane's live tool, resolved from this file's location:
    <repo>/tools/gates/phonology-sanity-gate.py
"""

import argparse
import hashlib
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
DEFAULT_GATE = os.path.join(REPO, "tools", "gates", "phonology-sanity-gate.py")

# Review 26 §0 pin for the pre-fix bytes (blob fe34faa / HEAD cf338a7, unchanged).
PREFIX_SHA256 = "fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655"

TRUNCATED_SEQ = (
    "name: t\n"
    "phonology:\n"
    "  consonants: [p, t, k\n"
    "  vowels: [a, e, i]\n"
    "  phonotactics: (C)V\n"
    "  tones: 0\n"
)
TRUNCATED_MAP = (
    "name: t\n"
    "phonology: {consonants: [p, t, k, m, n, s, l], vowels: [a, e, i, o, u], "
    "phonotactics: \"(C)V(C)\", tones: 0\n"
)
TRUNCATED_NESTED = (
    "name: t\n"
    "phonology:\n"
    "  consonants: [p, [t, k]\n"
    "  vowels: [a, e, i]\n"
    "  phonotactics: (C)V\n"
    "  tones: 0\n"
)
CLOSED_TWIN = (
    "name: t\n"
    "phonology:\n"
    "  consonants: [p, t, k]\n"
    "  vowels: [a, e, i]\n"
    "  phonotactics: (C)V\n"
    "  tones: 0\n"
)
VALID_CLEAN = (
    "name: t\n"
    "phonology:\n"
    "  consonants: [p, t, k, m, n, s, l]\n"
    "  vowels: [a, e, i, o, u]\n"
    "  phonotactics: (C)V(C)\n"
    "  tones: 0\n"
    "  notable_rules:\n"
    "    - \"t \u2192 ts / _i\"\n"
)


def run_gate(gate, text, timeout=30):
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "packet.yml")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
        proc = subprocess.run(
            [sys.executable, gate, path],
            capture_output=True, text=True, timeout=timeout)
        return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def run_gate_stdin(gate, text, timeout=30):
    proc = subprocess.run(
        [sys.executable, gate, "-"],
        input=text, capture_output=True, text=True, timeout=timeout)
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
        print("NEG-04 ERROR: gate not found: %s" % gate)
        return 2
    with open(gate, "rb") as handle:
        digest = hashlib.sha256(handle.read()).hexdigest()
    print("NEG-04 gate under test: %s" % gate)
    print("NEG-04 gate sha256: %s" % digest)
    if digest == PREFIX_SHA256:
        print("NEG-04 note: this is the review-26 pinned PRE-FIX byte copy "
              "(fb05c644...); checks below are expected to FAIL.")

    failures = []
    checks = 0

    def check(name, payload, predicate, describe):
        nonlocal checks
        checks += 1
        rc, out = run_gate(gate, payload)
        ids = finding_ids(out)
        ok = predicate(rc, ids, out)
        print("NEG-04 %-34s rc=%s ids=%s %s"
              % (name, rc, ",".join(ids) or "-", "PASS" if ok else "FAIL"))
        if not ok:
            failures.append("%s: %s" % (name, describe(rc, ids, out)))

    # C1: truncated flow sequence must be rejected, never evaluated.
    check(
        "truncated-flow-sequence",
        TRUNCATED_SEQ,
        lambda rc, ids, out: rc == 2 and ids == ["G-DATA"]
        and "unterminated flow sequence" in out,
        lambda rc, ids, out: (
            "PRE-FIX PATTERN OBSERVED: rc=%s ids=%s (expected rc=2 with only "
            "G-DATA and 'unterminated flow sequence'); the gate evaluated a "
            "document that is not valid YAML. output=%r"
            % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C2: truncated flow mapping (unbalanced '{') must be rejected.
    check(
        "truncated-flow-mapping",
        TRUNCATED_MAP,
        lambda rc, ids, out: rc == 2 and ids == ["G-DATA"]
        and "unterminated flow mapping" in out,
        lambda rc, ids, out: (
            "PRE-FIX PATTERN OBSERVED: rc=%s ids=%s (expected rc=2 with only "
            "G-DATA and 'unterminated flow mapping'). output=%r"
            % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C3: nested unbalanced flow inside a closed outer bracket must be rejected.
    check(
        "nested-unbalanced-flow",
        TRUNCATED_NESTED,
        lambda rc, ids, out: rc == 2 and ids == ["G-DATA"]
        and "unterminated flow sequence" in out,
        lambda rc, ids, out: (
            "PRE-FIX PATTERN OBSERVED: rc=%s ids=%s (expected rc=2 with only "
            "G-DATA). output=%r" % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C4 (positive twin): the same packet with the bracket closed must evaluate.
    check(
        "closed-twin-still-evaluates",
        CLOSED_TWIN,
        lambda rc, ids, out: rc == 1 and "G-DATA" in ids and "T-C" in ids,
        lambda rc, ids, out: (
            "regression: closed flow sequence no longer evaluates: rc=%s "
            "ids=%s output=%r" % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C5 (positive): a complete valid packet stays clean.
    check(
        "valid-packet-still-clean",
        VALID_CLEAN,
        lambda rc, ids, out: rc == 0 and ids == [],
        lambda rc, ids, out: (
            "regression: valid packet no longer clean: rc=%s ids=%s output=%r"
            % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C6: the stdin path ('-') must reject the same truncated payload.
    checks += 1
    rc, out = run_gate_stdin(gate, TRUNCATED_SEQ)
    ids = finding_ids(out)
    ok = rc == 2 and ids == ["G-DATA"] and "unterminated flow sequence" in out
    print("NEG-04 %-34s rc=%s ids=%s %s"
          % ("stdin-truncated-flow", rc, ",".join(ids) or "-",
             "PASS" if ok else "FAIL"))
    if not ok:
        failures.append(
            "stdin-truncated-flow: PRE-FIX PATTERN OBSERVED: rc=%s ids=%s "
            "(expected rc=2 with only G-DATA and 'unterminated flow sequence')"
            % (rc, ids))

    if failures:
        print("NEG-04 RESULT: FAIL (%d/%d checks)" % (len(failures), checks))
        for line in failures:
            print("NEG-04 FAILURE: %s" % line)
        return 1
    print("NEG-04 RESULT: PASS (%d/%d checks)" % (checks, checks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
