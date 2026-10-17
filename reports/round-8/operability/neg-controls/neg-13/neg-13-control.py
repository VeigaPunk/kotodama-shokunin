#!/usr/bin/env python3
"""Negative control for round-8 defect R8-O13 (defect index 9 = review 26 §3 D9).

Defect under control: `formation.output` is a packet-authored `str.format`
template, and pre-fix the naming gate rendered it with
`output.format(**match.groupdict())` (naming-collision-gate.py:1300-1324 at
baseline e7ca0fa).  Attribute access, indexing, conversions and format specs
were accepted, so a rule output such as `{stem.__class__}` rendered
`"<class 'str'>"` — and `{stem.__class__.__mro__}` a tuple of classes — into
the DERIV-REPLAY finding text: interpreter internals reachable from packet
text and echoed into a report (review 26 §3 D9,
reports/supplement-opencode-1/26-parser-controls.md:159-162).

Post-fix contract asserted here (the accepted subset is plain `{name}`
placeholders naming the pattern's named groups; anything else is refused as a
DERIV-HOLD instead of being rendered):
  * `{stem.__class__}`, `{stem.__class__.__mro__}` -> exit 1 with DERIV-HOLD
    "outside the accepted subset" and NO `<class` substring anywhere;
  * `{stem[0]}`, `{stem!r}`, `{stem:>8}` -> exit 1 with DERIV-HOLD
    "outside the accepted subset";
  * malformed `{stem}in{` -> exit 1 with a stable DERIV-HOLD, never a
    traceback;
  * positive regression: a plain `{stem}in` template still renders and is
    compared (clean packet exits 0; a mismatching name still exits 1 with
    DERIV-REPLAY naming the replayed form).

Fail-before / pass-after:
  * `--from-git e7ca0fa` materializes the pre-fix gate bytes with
    `git archive` (sha256 8c5afb0a…, the review-26 §0 pin) and the control
    exits 1, naming the pre-fix pattern (template rendered: internals echoed
    in DERIV-REPLAY, indexed/converted/padded values compared);
  * the default (live tree) run must exit 0.

Isolation: payloads are written only into a tempfile.TemporaryDirectory();
the gate under test is invoked as a subprocess; nothing under the repository
is written by this control.

Usage:
    python3 neg-13-control.py                      # live tree, post-fix expected
    python3 neg-13-control.py --from-git e7ca0fa   # pre-fix bytes, control fails
    python3 neg-13-control.py --gate PATH          # any gate copy
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tarfile
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
DEFAULT_GATE = os.path.join(REPO, "tools", "gates", "naming-collision-gate.py")

# Review 26 §0 pin for the pre-fix naming gate bytes (baseline fe34faa; the
# same bytes are the e7ca0fa blob, so the control binds to the declared
# round-8 baseline as well).
PRE_FIX_SHA256 = "8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526"

BASE_PACKET = {
    "name": "F-probe",
    "phonology": {
        "consonants": ["p", "t", "k", "m", "n", "s", "l", "r"],
        "vowels": ["a", "i", "u"],
        "phonotactics": "(C)V(C)",
        "coda": ["n", "s"],
        "onset_clusters": False,
    },
    "orthography": {"case": "display-only"},
    "morphology": {
        "derivation_rules": [
            {"id": "R1", "kind": "suffix", "affix": "-in",
             "pattern": "^(?P<stem>.+)a$", "output": "{stem}in"}
        ]
    },
    "names": [
        {"name": "talin", "id": "F01", "type": "person",
         "formation": {"stem": "tala", "rule": "R1"}}
    ],
    "cross_culture_review": {
        "reviewed": "2026-10-17",
        "languages": [{"language": "F-toy (fixture-only)", "result": "no-material-hit"}],
    },
}


def sha256(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def make_scratch_root(explicit=None):
    """Scratch root with the most free space among the writable candidates.

    The fleet runs many workers in parallel and the default system temp dir
    can fill up mid-run (observed: ENOSPC during this control's development),
    so ``--scratch-root`` or ``NEG13_SCRATCH_DIR`` overrides the choice and
    the candidates are ranked by free bytes.
    """
    candidates = [explicit, os.environ.get("NEG13_SCRATCH_DIR"),
                  tempfile.gettempdir(), "/var/tmp", "/tmp"]
    best = None
    for base in candidates:
        if not base or not os.path.isdir(base):
            continue
        try:
            stat = os.statvfs(base)
        except OSError:
            continue
        free = stat.f_bavail * stat.f_frsize
        if best is None or free > best[1]:
            best = (base, free)
    if best is None:
        raise SystemExit("NEG-13 ERROR: no writable scratch root")
    return tempfile.mkdtemp(prefix="neg-13-", dir=best[0])


def materialize_from_git(rev, tmp):
    dest = os.path.join(tmp, "git-%s" % rev.replace("/", "_"))
    os.makedirs(dest, exist_ok=True)
    proc = subprocess.Popen(["git", "-C", REPO, "archive", rev, "tools/gates"],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with tarfile.open(fileobj=proc.stdout, mode="r|") as tar:
        try:
            tar.extractall(path=dest, filter="data")
        except TypeError:  # Python < 3.12
            tar.extractall(path=dest)
    stderr = proc.stderr.read().decode("utf-8", "replace")
    if proc.wait() != 0:
        raise SystemExit("NEG-13 ERROR: git archive %s failed: %s" % (rev, stderr))
    return os.path.join(dest, "tools", "gates", "naming-collision-gate.py")


def run_gate(gate, scratch, template, name="talin", timeout=60):
    packet = json.loads(json.dumps(BASE_PACKET))
    packet["morphology"]["derivation_rules"][0]["output"] = template
    packet["names"][0]["name"] = name
    path = os.path.join(scratch, "packet.json")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(json.dumps(packet))
    proc = subprocess.run([sys.executable, gate, path],
                          capture_output=True, text=True, timeout=timeout)
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def finding_ids(output):
    ids = []
    for line in output.splitlines():
        if line.startswith("FINDING "):
            ids.append(line.split(":", 1)[0].split()[1])
    return ids


def main():
    parser = argparse.ArgumentParser(
        description="Negative control for round-8 defect R8-O13 (review 26 D9).",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--gate", default=None,
                        help="gate copy to test (default: the live repo gate)")
    parser.add_argument("--from-git", metavar="REV", default=None,
                        help="materialize tools/gates from git revision REV and test that gate")
    parser.add_argument("--scratch-root", default=None,
                        help="directory for scratch payloads (default: most free of "
                             "NEG13_SCRATCH_DIR, system temp, /var/tmp, /tmp)")
    args = parser.parse_args()

    tmp_root = make_scratch_root(args.scratch_root)
    try:
        if args.from_git:
            gate = materialize_from_git(args.from_git, tmp_root)
            print("NEG-13 gate source: git revision %s (git archive)" % args.from_git)
        elif args.gate:
            gate = os.path.abspath(args.gate)
            print("NEG-13 gate source: %s" % gate)
        else:
            gate = DEFAULT_GATE
            print("NEG-13 gate source: live tree %s" % gate)
        if not os.path.isfile(gate):
            print("NEG-13 ERROR: gate not found: %s" % gate)
            return 2
        digest = sha256(gate)
        print("NEG-13 gate under test: %s" % gate)
        print("NEG-13 gate sha256: %s" % digest)
        if digest == PRE_FIX_SHA256:
            print("NEG-13 note: this is the review-26 pinned PRE-FIX byte copy "
                  "(8c5afb0a…); the subset checks below are expected to FAIL.")

        failures = []
        checks = 0

        def check(name, template, predicate, describe, gate_name="talin"):
            nonlocal checks
            checks += 1
            rc, out = run_gate(gate, tmp_root, template, name=gate_name)
            ids = finding_ids(out)
            ok = predicate(rc, ids, out)
            print("NEG-13 %-30s rc=%s ids=%s %s"
                  % (name, rc, ",".join(ids) or "-", "PASS" if ok else "FAIL"))
            if not ok:
                failures.append("%s: %s" % (name, describe(rc, ids, out)))

        def subset_ok(rc, ids, out):
            return (rc == 1 and ids == ["DERIV-HOLD"]
                    and "outside the accepted subset" in out
                    and "<class" not in out)

        def subset_desc(rc, ids, out):
            if "<class" in out:
                return ("PRE-FIX PATTERN OBSERVED: internals echoed into the report "
                        "(rc=%s ids=%s): %r" % (rc, ids, out.strip().splitlines()[:2]))
            return ("PRE-FIX PATTERN OBSERVED: template rendered instead of refused "
                    "(rc=%s ids=%s; expected rc=1 with only DERIV-HOLD and "
                    "'outside the accepted subset'): %r"
                    % (rc, ids, out.strip().splitlines()[:2]))

        check("attribute-access-__class__", "{stem.__class__}", subset_ok, subset_desc)
        check("attribute-chain-__mro__", "{stem.__class__.__mro__}", subset_ok, subset_desc)
        check("indexing-stem-0", "{stem[0]}", subset_ok, subset_desc)
        check("conversion-stem-repr", "{stem!r}", subset_ok, subset_desc)
        check("format-spec-stem", "{stem:>8}", subset_ok, subset_desc)

        def malformed_ok(rc, ids, out):
            return (rc == 1 and ids == ["DERIV-HOLD"] and "template is malformed" in out
                    and "Traceback (most recent call last)" not in out)

        def malformed_desc(rc, ids, out):
            return ("PRE-FIX PATTERN OBSERVED: malformed template not refused as a stable "
                    "DERIV-HOLD (rc=%s ids=%s): %r" % (rc, ids, out.strip().splitlines()[:2]))

        check("malformed-single-brace", "{stem}in{", malformed_ok, malformed_desc)

        def clean_ok(rc, ids, out):
            return rc == 0 and ids == []

        def clean_desc(rc, ids, out):
            return ("regression: a plain {stem} template no longer replays cleanly "
                    "(rc=%s ids=%s): %r" % (rc, ids, out.strip().splitlines()[:2]))

        check("plain-template-still-clean", "{stem}in", clean_ok, clean_desc)

        def mismatch_ok(rc, ids, out):
            return (rc == 1 and "DERIV-REPLAY" in ids and "yields 'talin'" in out
                    and "<class" not in out)

        def mismatch_desc(rc, ids, out):
            return ("regression: a plain {stem} template no longer compares "
                    "(rc=%s ids=%s): %r" % (rc, ids, out.strip().splitlines()[:2]))

        check("plain-template-mismatch-fails", "{stem}in", mismatch_ok, mismatch_desc,
              gate_name="talim")

        if failures:
            print("NEG-13 RESULT: FAIL (%d/%d checks)" % (len(failures), checks))
            for line in failures:
                print("NEG-13 FAILURE: %s" % line)
            return 1
        print("NEG-13 RESULT: PASS (%d/%d checks)" % (checks, checks))
        return 0
    finally:
        import shutil
        shutil.rmtree(tmp_root, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
