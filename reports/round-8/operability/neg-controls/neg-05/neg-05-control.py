#!/usr/bin/env python3
"""Negative control for round-8 defect R8-O05 (supplement review 26, defect D2).

Defect under control: tools/gates/phonology-sanity-gate.py let duplicate
mapping keys silently last-win with no diagnostic — a second `phonology:`
block overwrote the first (block mapping, review §3 D2 cited site :416), a
flow mapping `{consonants: [p], consonants: [k]}` kept only the last entry
(:382), and a sequence mapping entry merged later keys over earlier ones.
An author's stale key therefore changed the audit outcome with no finding,
instead of the documented exit 2 "could-not-evaluate" for an unparseable
packet (module docstring, exit-code contract).

Contract:
  * pointed at the LIVE (post-fix) gate -> every check passes, exit 0;
  * pointed at PRE-FIX bytes (`--gate <pre-fix copy>`) -> the duplicate-key
    checks observe the pre-fix pattern (rc=1, a *verdict* printed for a
    document whose keys collide, or a silent merge) and the control exits 1,
    naming the pattern.

Isolation: payloads are written only into a temp directory outside the
repository (system temp when it has room, otherwise a user scratch dir);
the gate under test is invoked as a subprocess; nothing under the repository
is written by this control.

Usage:
    python3 neg-05-control.py [--gate PATH]

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

# Two identical `phonology:` blocks: pure duplicate, no verdict change.
DUP_BLOCK = (
    "name: t\n"
    "phonology:\n"
    "  consonants: [p, t, k, m, n, s, l]\n"
    "  vowels: [a, e, i, o, u]\n"
    "  phonotactics: (C)V(C)\n"
    "  tones: 0\n"
    "phonology:\n"
    "  consonants: [p, t, k, m, n, s, l]\n"
    "  vowels: [a, e, i, o, u]\n"
    "  phonotactics: (C)V(C)\n"
    "  tones: 0\n"
)
# Review 26 §3 D2 counterexample: the second block differs, so last-wins
# silently audits a document that is not valid YAML (pre-fix: M-EJECT).
DUP_BLOCK_FLIP = (
    "name: t\n"
    "phonology:\n"
    "  consonants: [p, t, k, m, n, s, l]\n"
    "  vowels: [a, e, i, o, u]\n"
    "  phonotactics: (C)V(C)\n"
    "  tones: 0\n"
    "phonology:\n"
    "  consonants: [p, t, k, m, n, s, l, q\u02bc]\n"
    "  vowels: [a, e, i, o, u]\n"
    "  phonotactics: (C)V(C)\n"
    "  tones: 0\n"
)
# Flow-mapping duplicate (review 26 §3 D2 flow path).
DUP_FLOW = (
    "name: t\n"
    "phonology: {consonants: [p], consonants: [k]}\n"
)
# Sequence mapping entry with a repeated key.
DUP_SEQ = (
    "name: t\n"
    "phonology:\n"
    "  consonants: [p, t, k, m, n, s, l]\n"
    "  vowels: [a, e, i, o, u]\n"
    "  phonotactics: (C)V(C)\n"
    "  tones: 0\n"
    "names:\n"
    "  - name: A\n"
    "    name: B\n"
)
# Duplicate-free twin: the first block of DUP_BLOCK alone.
FIRST_BLOCK = (
    "name: t\n"
    "phonology:\n"
    "  consonants: [p, t, k, m, n, s, l]\n"
    "  vowels: [a, e, i, o, u]\n"
    "  phonotactics: (C)V(C)\n"
    "  tones: 0\n"
)
# Complete valid packet (the gate's own clean selftest packet).
VALID_CLEAN = (
    "name: gate-selftest-clean\n"
    "phonology:\n"
    "  consonants: [p, t, k, m, n, s, l]\n"
    "  vowels: [a, e, i, o, u]\n"
    "  phonotactics: (C)V(C)\n"
    "  tones: 0\n"
    "  notable_rules:\n"
    "    - \"t \u2192 ts / _i\"\n"
    "    - \"n \u2192 \u014b / _k\"\n"
    "names:\n"
    "  - {name: \"Senna\", type: place, era: \"First Era\"}\n"
    "eras: [First Era]\n"
)


def scratch_parent():
    """First writable scratch parent outside the repository.

    The system temp directory is preferred; when it is full (round-8 host:
    /tmp hit 100% inode use) a user scratch dir is used instead. Payloads
    never land inside the repository.
    """
    candidates = [os.environ.get("NEG05_SCRATCH"), tempfile.gettempdir(),
                  os.path.join(os.path.expanduser("~"), "tmp")]
    for candidate in candidates:
        if not candidate:
            continue
        try:
            os.makedirs(candidate, exist_ok=True)
            probe = os.path.join(candidate, ".neg05-probe")
            with open(probe, "w", encoding="utf-8") as handle:
                handle.write("probe")
            os.remove(probe)
            return candidate
        except OSError:
            continue
    raise RuntimeError("no writable scratch parent outside the repository")


SCRATCH_PARENT = scratch_parent()


def run_gate(gate, text, timeout=30):
    with tempfile.TemporaryDirectory(dir=SCRATCH_PARENT) as d:
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
        print("NEG-05 ERROR: gate not found: %s" % gate)
        return 2
    with open(gate, "rb") as handle:
        digest = hashlib.sha256(handle.read()).hexdigest()
    print("NEG-05 gate under test: %s" % gate)
    print("NEG-05 gate sha256: %s" % digest)
    print("NEG-05 scratch parent: %s" % SCRATCH_PARENT)
    if digest == PREFIX_SHA256:
        print("NEG-05 note: this is the review-26 pinned PRE-FIX byte copy "
              "(fb05c644...); checks below are expected to FAIL.")

    failures = []
    checks = 0

    def check(name, payload, predicate, describe):
        nonlocal checks
        checks += 1
        rc, out = run_gate(gate, payload)
        ids = finding_ids(out)
        ok = predicate(rc, ids, out)
        print("NEG-05 %-34s rc=%s ids=%s %s"
              % (name, rc, ",".join(ids) or "-", "PASS" if ok else "FAIL"))
        if not ok:
            failures.append("%s: %s" % (name, describe(rc, ids, out)))

    # C1: an exact duplicate `phonology:` block must be rejected.
    check(
        "duplicate-block-key",
        DUP_BLOCK,
        lambda rc, ids, out: rc == 2 and ids == ["G-DATA"]
        and "duplicate key 'phonology'" in out,
        lambda rc, ids, out: (
            "PRE-FIX PATTERN OBSERVED: rc=%s ids=%s (expected rc=2 with only "
            "G-DATA naming 'duplicate key'); the duplicate block was silently "
            "merged. output=%r" % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C2: the review's verdict-flip counterexample (second block adds qʼ).
    check(
        "duplicate-block-verdict-flip",
        DUP_BLOCK_FLIP,
        lambda rc, ids, out: rc == 2 and ids == ["G-DATA"]
        and "duplicate key 'phonology'" in out,
        lambda rc, ids, out: (
            "PRE-FIX PATTERN OBSERVED: rc=%s ids=%s (expected rc=2 with only "
            "G-DATA); last-wins audited a document that is not valid YAML. "
            "output=%r" % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C3: duplicate key inside a flow mapping must be rejected.
    check(
        "duplicate-flow-key",
        DUP_FLOW,
        lambda rc, ids, out: rc == 2 and ids == ["G-DATA"]
        and "duplicate key 'consonants'" in out,
        lambda rc, ids, out: (
            "PRE-FIX PATTERN OBSERVED: rc=%s ids=%s (expected rc=2 with only "
            "G-DATA); the flow mapping kept only the last entry. output=%r"
            % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C4: duplicate key in a sequence mapping entry must be rejected.
    check(
        "duplicate-sequence-entry-key",
        DUP_SEQ,
        lambda rc, ids, out: rc == 2 and ids == ["G-DATA"]
        and "duplicate key 'name'" in out,
        lambda rc, ids, out: (
            "PRE-FIX PATTERN OBSERVED: rc=%s ids=%s (expected rc=2 with only "
            "G-DATA); the repeated entry key was silently overwritten. "
            "output=%r" % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C5 (positive twin): the duplicate-free packet must still evaluate.
    check(
        "first-block-twin-still-evaluates",
        FIRST_BLOCK,
        lambda rc, ids, out: rc == 1 and "G-DATA" in ids
        and "duplicate key" not in out,
        lambda rc, ids, out: (
            "regression: duplicate-free twin no longer evaluates: rc=%s "
            "ids=%s output=%r" % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C6 (positive): a complete valid packet stays clean.
    check(
        "valid-packet-still-clean",
        VALID_CLEAN,
        lambda rc, ids, out: rc == 0 and ids == [],
        lambda rc, ids, out: (
            "regression: valid packet no longer clean: rc=%s ids=%s output=%r"
            % (rc, ids, out.strip().splitlines()[:3])),
    )

    # C7: the stdin path ('-') must reject the same duplicate payload.
    checks += 1
    rc, out = run_gate_stdin(gate, DUP_BLOCK)
    ids = finding_ids(out)
    ok = (rc == 2 and ids == ["G-DATA"]
          and "duplicate key 'phonology'" in out)
    print("NEG-05 %-34s rc=%s ids=%s %s"
          % ("stdin-duplicate-block", rc, ",".join(ids) or "-",
             "PASS" if ok else "FAIL"))
    if not ok:
        failures.append(
            "stdin-duplicate-block: PRE-FIX PATTERN OBSERVED: rc=%s ids=%s "
            "(expected rc=2 with only G-DATA naming 'duplicate key')"
            % (rc, ids))

    if failures:
        print("NEG-05 RESULT: FAIL (%d/%d checks)" % (len(failures), checks))
        for line in failures:
            print("NEG-05 FAILURE: %s" % line)
        return 1
    print("NEG-05 RESULT: PASS (%d/%d checks)" % (checks, checks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
