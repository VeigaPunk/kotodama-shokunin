#!/usr/bin/env python3
"""Negative control for round-8 defect R8-O07 (supplement review 26, defect D3).

Defect under control: the five culture-packet gates parsed YAML anchor (`&`),
alias (`*`) and tag (`!`) syntax as literal scalar text instead of rejecting it
as outside their declared YAML subset. The naming gate's own documented policy
(naming-collision-gate.py:57-60, pre-fix numbering) says: "No anchors, tags,
multi-document streams, or tab indentation; input outside the subset exits 2
instead of being guessed." Observed pre-fix: `name: *tag` was audited as the
form `*tag` and produced an invented PHON-INVENTORY finding; all five gates
evaluated the anchor/alias/tag forms (exit 1) instead of the documented exit 2.

Contract (same protocol as neg-04):
  * pointed at the LIVE (post-fix) gates -> every check passes, exit 0;
  * pointed at PRE-FIX bytes (`--prefix-dir DIR`, extracted with
    `--extract-prefix DIR` from the pinned review-26 blobs) -> the
    anchor/alias/tag checks observe the pre-fix pattern (rc=1: the syntax was
    evaluated) and the control exits 1, naming that pattern.

Isolation: probe packets are written only into tempfile.TemporaryDirectory();
each gate under test is invoked as a subprocess; nothing under the repository
is written by this control. Probes are built by textual replacement inside the
committed gate fixtures (read-only), so every probe is a complete packet.

Usage:
    python3 neg-07-d3-control.py                    # live gates -> expect exit 0
    python3 neg-07-d3-control.py --extract-prefix /tmp/neg07-prefix
    python3 neg-07-d3-control.py --prefix-dir /tmp/neg07-prefix   # expect exit 1
    python3 neg-07-d3-control.py --gate naming-collision-gate     # one gate only

Default gate paths resolve from this file's location:
    <repo>/tools/gates/<gate>.py
"""

import argparse
import hashlib
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
LIVE_DIR = os.path.join(REPO, "tools", "gates")
FIXTURE_DIR = os.path.join(LIVE_DIR, "fixtures")

# Review 26 section 0 pins: pre-fix sha256 of the bytes executed, and the
# fe34faa/e7ca0fa git blobs that carry them (verified equal by this shard:
# `git rev-parse e7ca0fa:tools/gates/<gate>.py`).
PREFIX_PINS = {
    "naming-collision-gate": (
        "8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526",
        "a32267a718760d4cc0c515bd48bdc32a37853e57",
    ),
    "phonology-sanity-gate": (
        "fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655",
        "441f1c5dada40cf6a35691f648dc7a3ec6c4d874",
    ),
    "myth-consistency-gate": (
        "26d246e9936db4375c31c6eb260545bf55051d11ec00bb1e757458399b1b55c5",
        "21a5e3b5c88f8a4e65a64770da2c78d93b80b534",
    ),
    "costume-era-consistency-gate": (
        "29a9361c7b96a354c41a3994e3459a951ce0a43425b3984d6506b3e5b3a43f03",
        "700747e287af740b87b1672dd6233e68a1125348",
    ),
    "lexicon-coverage-audit": (
        "63ee4ec6b15188fefa3e997766971d66fe4d7d7bf9eed65cdcdd55f548fe8a80",
        "2e7662bd9a12580b60efb2d688d061057f1735c1",
    ),
}

# Per gate: fixture, defect probe (anchor/alias/tag scalar), the token the
# post-fix diagnostic must name, and two over-rejection controls (a QUOTED
# indicator scalar, which the subset declares legal, and an indicator inside a
# scalar, which the guard must not touch).
GATES = [
    {
        "name": "naming-collision-gate",
        "defect": ("  - name: talin\n", "  - name: *tag\n"),
        "token": "'*tag'",
        "defect_note": "alias audited as the name form '*tag' -> invented "
                       "PHON-INVENTORY finding",
        "quoted": ("  - name: talin\n", "  - name: \"*tag\"\n"),
        "mid": ("  - name: talin\n", "  - name: ta!lin\n"),
    },
    {
        "name": "phonology-sanity-gate",
        "defect": ("name: gate-selftest-phonology\n",
                   "name: &tag anchor-probe\n"),
        "token": "'&tag anchor-probe'",
        "defect_note": "anchor scalar evaluated as the literal packet name",
        "quoted": ("name: gate-selftest-phonology\n",
                   "name: \"&tag anchor-probe\"\n"),
        "mid": ("name: gate-selftest-phonology\n",
                "name: gate-selftest-phonology!\n"),
    },
    {
        "name": "myth-consistency-gate",
        "defect": ("name: gate-selftest-culture\n", "name: *tag\n"),
        "token": "'*tag'",
        "defect_note": "alias scalar evaluated as the literal packet name",
        "quoted": ("name: gate-selftest-culture\n", "name: \"*tag\"\n"),
        "mid": ("name: gate-selftest-culture\n", "name: gate-selftest-culture!\n"),
    },
    {
        "name": "costume-era-consistency-gate",
        "defect": ("  - material: hemp\n", "  - material: *tag\n"),
        "token": "'*tag'",
        "defect_note": "alias scalar evaluated as a literal material id",
        "quoted": ("  - material: hemp\n", "  - material: \"*tag\"\n"),
        "mid": ("  - material: hemp\n", "  - material: hem!p\n"),
    },
    {
        "name": "lexicon-coverage-audit",
        "defect": ("name: Vethari (gate fixture)\n", "name: *tag\n"),
        "token": "'*tag'",
        "defect_note": "alias scalar evaluated as the literal packet name",
        "quoted": ("name: Vethari (gate fixture)\n", "name: \"*tag\"\n"),
        "mid": ("name: Vethari (gate fixture)\n",
                "name: Vethari! (gate fixture)\n"),
    },
]

SUBSET_MESSAGE = "outside the declared subset"


def sha256_file(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def run_gate(gate, text, timeout=30):
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "packet.yml")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
        proc = subprocess.run(
            [sys.executable, gate, path],
            capture_output=True, text=True, timeout=timeout)
        return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def probe_text(gate_spec, key):
    fixture = os.path.join(FIXTURE_DIR, gate_spec["name"] + ".yml")
    with open(fixture, encoding="utf-8") as handle:
        text = handle.read()
    old, new = gate_spec[key]
    if text.count(old) != 1:
        raise SystemExit(
            "NEG-07-D3 SETUP ERROR: fixture anchor %r occurs %d times in %s"
            % (old, text.count(old), fixture))
    return text.replace(old, new, 1)


def extract_prefix(directory):
    os.makedirs(directory, exist_ok=True)
    for name, (_sha, blob) in sorted(PREFIX_PINS.items()):
        dest = os.path.join(directory, name + ".py")
        proc = subprocess.run(
            ["git", "-C", REPO, "cat-file", "blob", blob],
            capture_output=True)
        if proc.returncode != 0:
            print("NEG-07-D3 EXTRACT FAILED: %s (%s)"
                  % (name, proc.stderr.decode("utf-8", "replace").strip()))
            return 1
        with open(dest, "wb") as handle:
            handle.write(proc.stdout)
        digest = hashlib.sha256(proc.stdout).hexdigest()
        mark = "matches review-26 pin" if digest == _sha else "PIN MISMATCH"
        print("NEG-07-D3 extracted %-30s %s (%s)" % (name, digest, mark))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--prefix-dir",
                    help="directory with pre-fix <gate>.py copies")
    ap.add_argument("--extract-prefix", metavar="DIR",
                    help="write the pinned pre-fix gate bytes into DIR, exit")
    ap.add_argument("--gate", help="restrict to one gate name")
    args = ap.parse_args()

    if args.extract_prefix:
        return extract_prefix(os.path.abspath(args.extract_prefix))

    gates = GATES
    if args.gate:
        gates = [g for g in GATES if g["name"] == args.gate]
        if not gates:
            print("NEG-07-D3 ERROR: unknown gate %r" % args.gate)
            return 2

    failures = []
    checks = 0

    for spec in gates:
        name = spec["name"]
        if args.prefix_dir:
            gate = os.path.join(os.path.abspath(args.prefix_dir), name + ".py")
        else:
            gate = os.path.join(LIVE_DIR, name + ".py")
        if not os.path.isfile(gate):
            print("NEG-07-D3 ERROR: gate not found: %s" % gate)
            return 2
        digest = sha256_file(gate)
        pin_sha, _blob = PREFIX_PINS[name]
        note = ""
        if digest == pin_sha:
            note = " [review-26 pinned PRE-FIX bytes: checks expected to FAIL]"
        print("NEG-07-D3 gate %s sha256=%s%s" % (name, digest, note))

        def check(check_name, payload, predicate, describe):
            nonlocal checks
            checks += 1
            try:
                rc, out = run_gate(gate, payload)
            except subprocess.TimeoutExpired:
                rc, out = "TIMEOUT", ""
            ok = predicate(rc, out)
            print("NEG-07-D3 %-30s %-26s rc=%-3s %s"
                  % (name, check_name, rc, "PASS" if ok else "FAIL"))
            if not ok:
                failures.append("%s/%s: %s" % (name, check_name, describe(rc, out)))

        # C1: anchor/alias/tag scalar must be rejected as outside the subset.
        check(
            "anchor-alias-tag-rejected",
            probe_text(spec, "defect"),
            lambda rc, out: (rc == 2 and SUBSET_MESSAGE in out
                             and spec["token"] in out),
            lambda rc, out: (
                "PRE-FIX PATTERN OBSERVED: rc=%s -- %s; the gate evaluated "
                "syntax its subset declares unrepresentable instead of the "
                "documented exit 2. output=%r"
                % (rc, spec["defect_note"], out.strip().splitlines()[:3])),
        )

        # C2: a QUOTED indicator scalar is legal and must still be evaluated.
        check(
            "quoted-indicator-legal",
            probe_text(spec, "quoted"),
            lambda rc, out: rc != 2 and SUBSET_MESSAGE not in out,
            lambda rc, out: (
                "over-rejection regression: quoted indicator scalar no longer "
                "evaluates: rc=%s output=%r"
                % (rc, out.strip().splitlines()[:3])),
        )

        # C3: an indicator inside a scalar is not YAML indicator syntax.
        check(
            "indicator-inside-scalar-legal",
            probe_text(spec, "mid"),
            lambda rc, out: rc != 2 and SUBSET_MESSAGE not in out,
            lambda rc, out: (
                "over-rejection regression: mid-scalar '!' no longer "
                "evaluates: rc=%s output=%r"
                % (rc, out.strip().splitlines()[:3])),
        )

        # C4: the pristine fixture still evaluates to its planted findings.
        fixture = os.path.join(FIXTURE_DIR, name + ".yml")
        with open(fixture, encoding="utf-8") as handle:
            pristine = handle.read()
        check(
            "pristine-fixture-unchanged",
            pristine,
            lambda rc, out: rc == 1 and SUBSET_MESSAGE not in out,
            lambda rc, out: (
                "regression: pristine fixture no longer evaluates to rc=1: "
                "rc=%s output=%r" % (rc, out.strip().splitlines()[:3])),
        )

    if failures:
        print("NEG-07-D3 RESULT: FAIL (%d/%d checks)" % (len(failures), checks))
        for line in failures:
            print("NEG-07-D3 FAILURE: %s" % line)
        return 1
    print("NEG-07-D3 RESULT: PASS (%d/%d checks)" % (checks, checks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
