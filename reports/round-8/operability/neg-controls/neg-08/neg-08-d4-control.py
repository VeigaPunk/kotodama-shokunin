#!/usr/bin/env python3
"""Secondary control, shard R8-O08: supplement review 26 §3 defect D4
(inventory `R26-D4`, 0-based list position 7).

The assigned defect of shard R8-O08 is index 4 = `R26-D2-lexicon`; that control
lives in `neg-08-control.py`. This file covers D4, which this shard repaired as
well because the sibling shards read the shared "defect index N" assignment in
two different spaces (see neg-08-report.md §0).

Defect under control: `tools/gates/naming-collision-gate.py` coerced every YAML
1.1 boolean/number scalar (`yes|no|true|false`, bare integers/floats) and then
re-rendered it with `_s()`, so a form-bearing field was audited as a *different
form* than the packet authored. Counterexample (review 26 §3 D4, re-confirmed
on the pre-fix bytes): a name authored `no` was audited as `'false'` —

    FINDING PHON-INVENTORY: FAIL — name N1 'false': symbol /f/ at position 1
    is not in the declared inventory (consonants {p, t, n}, vowels {a, o})

— a FAIL finding about a name that appears nowhere in the packet, while the
quoted twin `"no"` audited clean; `yes` became `'true'`, `007` became `'7'`.

Contract (one expectation set, both modes):
  * pointed at the LIVE (post-fix) gate -> every check passes, exit 0;
  * pointed at PRE-FIX bytes (`--gate <pre-fix copy>` or
    `--pre-fix-from-git [REV]`, default REV `cf338a7`) -> the authored-form
    checks observe the pre-fix pattern (twin mismatch and a re-rendered
    `false`/`true`/`7` in the finding text) and the control exits 1, naming
    the pattern.

Isolation: payloads are written only into a scratch directory (system temp,
with a local fallback because /tmp inode exhaustion was observed in this
batch); the gate under test is invoked as a subprocess; nothing under the
repository is written by this control, and the git-materialised pre-fix copy
lives only in the scratch directory.

Usage:
    python3 neg-08-control.py
    python3 neg-08-control.py --gate /path/to/pre-fix-copy.py
    python3 neg-08-control.py --pre-fix-from-git cf338a7

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
GATE_REL = "tools/gates/naming-collision-gate.py"

# Review 26 §0 pin for the committed pre-fix bytes (blob a32267a / sha256 below,
# unchanged between fe34faa and the round-8 baseline commit cf338a7).
PREFIX_SHA256_COMMITTED = (
    "8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526")
# Worktree bytes immediately before this shard's D4 edit (the D1/D3/D5/D6
# repairs from sibling shards were already present; the coercion was not).
PREFIX_SHA256_WORKTREE = (
    "db3cee7cd907ab28e2023f89ec9a352ff815f556f9c97799cf79369cca80c2f3")
KNOWN_PREFIX = {
    PREFIX_SHA256_COMMITTED: "review-26 §0 pin / committed cf338a7 bytes",
    PREFIX_SHA256_WORKTREE: "worktree bytes just before the R8-O08 edit",
}

INVENTORY = (
    "name: t\n"
    "phonology:\n"
    "  consonants: [p, t, n]\n"
    "  vowels: [a, o]\n"
    "  phonotactics: (C)V\n"
    "  tones: 0\n"
)


def packet(name_scalar, name_id="N1"):
    return INVENTORY + "names:\n  - {name: %s, id: %s, type: person}\n" % (
        name_scalar, name_id)


def _scratch():
    """TemporaryDirectory, falling back next to this control on temp failure."""
    try:
        return tempfile.TemporaryDirectory()
    except OSError:
        return tempfile.TemporaryDirectory(dir=HERE)


def run_gate(gate, text, timeout=30):
    with _scratch() as d:
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
    ap.add_argument("--gate", default=None)
    ap.add_argument("--pre-fix-from-git", nargs="?", const="cf338a7",
                    default=None, metavar="REV",
                    help="materialise the pre-fix gate from git (scratch copy)")
    args = ap.parse_args()

    scratch = None
    gate = args.gate
    if args.pre_fix_from_git is not None:
        scratch = _scratch()
        gate = os.path.join(scratch.name, "naming-collision-gate.prefix.py")
        proc = subprocess.run(
            ["git", "show", "%s:%s" % (args.pre_fix_from_git, GATE_REL)],
            cwd=REPO, capture_output=True, text=True)
        if proc.returncode != 0:
            print("NEG-08 ERROR: git show failed: %s" % proc.stderr.strip())
            return 2
        with open(gate, "w", encoding="utf-8") as handle:
            handle.write(proc.stdout)
    if gate is None:
        gate = DEFAULT_GATE
    gate = os.path.abspath(gate)
    if not os.path.isfile(gate):
        print("NEG-08 ERROR: gate not found: %s" % gate)
        return 2
    with open(gate, "rb") as handle:
        digest = hashlib.sha256(handle.read()).hexdigest()
    print("NEG-08 gate under test: %s" % gate)
    print("NEG-08 gate sha256: %s" % digest)
    if digest in KNOWN_PREFIX:
        print("NEG-08 note: PRE-FIX bytes (%s); authored-form checks below are "
              "expected to FAIL." % KNOWN_PREFIX[digest])

    failures = []
    checks = 0

    def check(name, payload, predicate, describe):
        nonlocal checks
        checks += 1
        rc, out = run_gate(gate, payload)
        ids = finding_ids(out)
        ok = predicate(rc, ids, out)
        print("NEG-08 %-38s rc=%s ids=%s %s"
              % (name, rc, ",".join(ids) or "-", "PASS" if ok else "FAIL"))
        if not ok:
            failures.append("%s: %s" % (name, describe(rc, ids, out)))

    def twin(name, scalar):
        """Authored scalar and its quoted twin must audit identically."""
        authored = packet(scalar)
        quoted = packet('"%s"' % scalar)
        rc_a, out_a = run_gate(gate, authored)
        rc_q, out_q = run_gate(gate, quoted)

        def ok(rc, ids, out):
            return (rc_a, out_a) == (rc_q, out_q) and "false" not in out_a \
                and "true" not in out_a

        def why(rc, ids, out):
            return ("PRE-FIX PATTERN OBSERVED: authored %r and quoted %r audit "
                    "differently or the authored form was re-rendered — "
                    "authored rc=%s %r vs quoted rc=%s %r"
                    % (scalar, scalar, rc_a, out_a.strip().splitlines()[:1],
                       rc_q, out_q.strip().splitlines()[:1]))

        check(name, authored, ok, why)
        return rc_a, out_a

    # F1: a name authored `no` is not re-rendered as `false`.
    twin("name-authored-no-preserved", "no")
    # F2: a name authored `yes` is not re-rendered as `true`.
    twin("name-authored-yes-preserved", "yes")
    # F3: a name authored `007` keeps its leading zeros.
    twin("name-authored-007-preserved", "007")

    # F4: an identifier authored `007` renders as authored, not as `7`. The
    # name is chosen so a FAIL finding carries the id into the message.
    authored_id = packet("tani", name_id="007")
    quoted_id = packet("tani", name_id='"007"')
    rc_a, out_a = run_gate(gate, authored_id)
    rc_q, out_q = run_gate(gate, quoted_id)
    checks += 1
    if (rc_a, out_a) == (rc_q, out_q) and "name 007" in out_a and "name 7 " not in out_a:
        print("NEG-08 %-38s rc=%s ids=%s PASS"
              % ("id-authored-007-preserved", rc_a,
                 ",".join(finding_ids(out_a)) or "-"))
    else:
        print("NEG-08 %-38s rc=%s ids=%s FAIL"
              % ("id-authored-007-preserved", rc_a,
                 ",".join(finding_ids(out_a)) or "-"))
        failures.append(
            "id-authored-007-preserved: PRE-FIX PATTERN OBSERVED: authored "
            "id 007 vs quoted '007' differ or the id was re-rendered as '7' "
            "— authored rc=%s %r vs quoted rc=%s %r"
            % (rc_a, out_a.strip().splitlines()[:1], rc_q,
               out_q.strip().splitlines()[:1]))

    # G1 (guard): `similarity.enabled: false` is still a typed boolean — the
    # unquoted token must keep suppressing NAME-NEAR.
    near = (INVENTORY
            + "names:\n"
            + "  - {name: Senna, id: N1, type: person}\n"
            + "  - {name: Sena, id: N2, type: place}\n")
    near_off = near + "similarity: {enabled: false}\n"
    check("guard-enabled-false-still-typed", near,
          lambda rc, ids, out: "NAME-NEAR" in ids,
          lambda rc, ids, out: "regression: NAME-NEAR no longer emitted: rc=%s ids=%s"
          % (rc, ids))
    check("guard-enabled-false-suppresses-near", near_off,
          lambda rc, ids, out: "NAME-NEAR" not in ids,
          lambda rc, ids, out: "regression: `enabled: false` no longer typed as a "
          "boolean (NAME-NEAR still emitted): rc=%s ids=%s" % (rc, ids))

    # G2 (guard): `opaque: true` is still a typed boolean — it suppresses the
    # DERIV-HOLD of a name with an etymology but no formation record.
    etym = (INVENTORY
            + "names:\n  - {name: tana, id: N1, type: person, etymology: "
            + "\"from proto-form\"}\n")
    etym_opaque = (INVENTORY
                   + "names:\n  - {name: tana, id: N1, type: person, "
                   + "etymology: \"from proto-form\", opaque: true}\n")
    check("guard-opaque-true-still-typed", etym,
          lambda rc, ids, out: "DERIV-HOLD" in ids,
          lambda rc, ids, out: "regression: DERIV-HOLD no longer emitted: rc=%s ids=%s"
          % (rc, ids))
    check("guard-opaque-true-suppresses-hold", etym_opaque,
          lambda rc, ids, out: "DERIV-HOLD" not in ids,
          lambda rc, ids, out: "regression: `opaque: true` no longer typed as a "
          "boolean (DERIV-HOLD still emitted): rc=%s ids=%s" % (rc, ids))

    # G3 (guard): `max_distance` is still a typed number — 0 disables the
    # recall-oriented distance layer.
    check("guard-max-distance-typed", near + "similarity: {max_distance: 0}\n",
          lambda rc, ids, out: "NAME-NEAR" not in ids,
          lambda rc, ids, out: "regression: `max_distance: 0` no longer typed as a "
          "number (NAME-NEAR still emitted): rc=%s ids=%s" % (rc, ids))

    # G4 (guard): a non-boolean token on a typed key must not crash the parser.
    check("guard-non-boolean-token-no-crash",
          near_off.replace("enabled: false", "enabled: maybe"),
          lambda rc, ids, out: rc in (0, 1) and "Traceback" not in out,
          lambda rc, ids, out: "regression: untyped token on a typed key crashed "
          "or exited %s: %r" % (rc, out.strip().splitlines()[:3]))

    # G5 (guard): the declared subset still rejects tab indentation (the
    # sibling D5 repair must not be weakened by this parser change).
    check("guard-tab-indentation-still-exit-2",
          INVENTORY.replace("  consonants", "\tconsonants"),
          lambda rc, ids, out: rc == 2 and "G-DATA" in ids,
          lambda rc, ids, out: "regression: tab indentation no longer rejected: "
          "rc=%s ids=%s" % (rc, ids))

    if scratch is not None:
        scratch.cleanup()
    if failures:
        print("NEG-08 RESULT: FAIL (%d/%d checks)" % (len(failures), checks))
        for line in failures:
            print("NEG-08 FAILURE: %s" % line)
        return 1
    print("NEG-08 RESULT: PASS (%d/%d checks)" % (checks, checks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
