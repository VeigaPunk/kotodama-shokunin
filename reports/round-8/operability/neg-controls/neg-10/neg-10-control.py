#!/usr/bin/env python3
"""Negative control for round-8 defect R8-O10 (defect index 6 = review 26 §3 D6).

Defect under control: a balanced but deeply nested flow value (3000 nested
`[`…`]` inside `phonology.consonants`) drove the packet parsers past Python's
recursion limit, so the gate printed a `RecursionError` traceback and exited 1
— the gates' "findings" code — instead of the documented exit 2
"could-not-evaluate". Review 26 §3 D6 registers the recursive sites at
`tools/gates/phonology-sanity-gate.py:327` and
`tools/gates/naming-collision-gate.py:324-345`; this control extends the same
class to `tools/gates/myth-consistency-gate.py` and
`tools/gates/costume-era-consistency-gate.py`, where the identical payload
reproduces the traceback at the declared baseline (fresh probe, recorded in
neg-10-report.md).

Repair under control (this shard): a `MAX_FLOW_DEPTH = 64` cap in each gate's
flow scanner raises the gate's own parse error (→ exit 2 through the existing
could-not-evaluate path), plus a `RecursionError` catch at each gate's
parse/evaluate entry as defence in depth. `tools/gates/lexicon-coverage-audit.py`
already conformed (exit 2 on the same payload) and is kept as an untouched
reference check.

Contract:
  * pointed at the LIVE (post-fix) gates -> every check passes, exit 0;
  * pointed at PRE-FIX bytes (`--rev cf338a7`, materialised with `git show`
    into a temp directory and verified against the review-26 §0 sha256 pins)
    -> the deep-nesting checks observe the pre-fix pattern (rc=1,
    `RecursionError` on stderr, no G-DATA finding) and the control exits 1,
    naming the pattern.

Isolation: payloads and any pre-fix gate copies are written only into a
tempfile directory (honours TMPDIR; `--scratch` picks the parent); every gate
runs as a subprocess; nothing under the repository is written.

Usage:
    python3 neg-10-control.py                     # live gates (post-fix)
    python3 neg-10-control.py --rev cf338a7       # pinned pre-fix bytes
    python3 neg-10-control.py --gate PATH         # one gate copy (name inferred)
    python3 neg-10-control.py --json OUT.json     # write a machine receipt
"""

import argparse
import datetime
import hashlib
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))

GATES = {
    "phonology": "tools/gates/phonology-sanity-gate.py",
    "naming": "tools/gates/naming-collision-gate.py",
    "myth": "tools/gates/myth-consistency-gate.py",
    "costume": "tools/gates/costume-era-consistency-gate.py",
}
FIXTURES = {
    "phonology": "tools/gates/fixtures/phonology-sanity-gate.yml",
    "naming": "tools/gates/fixtures/naming-collision-gate.yml",
    "myth": "tools/gates/fixtures/myth-consistency-gate.yml",
    "costume": "tools/gates/fixtures/costume-era-consistency-gate.yml",
}
# Review 26 §0 baseline pins (fe34faa == cf338a7 for these four files;
# re-verified with `git show cf338a7:<path> | sha256sum` when this control ran).
PRE_FIX_SHA256 = {
    "phonology": "fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655",
    "naming": "8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526",
    "myth": "26d246e9936db4375c31c6eb260545bf55051d11ec00bb1e757458399b1b55c5",
    "costume": "29a9361c7b96a354c41a3994e3459a951ce0a43425b3984d6506b3e5b3a43f03",
}
LEXICON = "tools/gates/lexicon-coverage-audit.py"
CAP_MARK = "nesting deeper than the supported"
DEEP_N = 3000


def deep_bracket(n=DEEP_N):
    return ("name: d\nphonology:\n  consonants: " + "[" * n + "]" * n
            + "\n  vowels: [a]\n  phonotactics: (C)V\n  tones: 0\n")


def deep_brace(n=DEEP_N):
    return ("name: d\nphonology:\n  consonants: " + "{a: " * n + "x" + "}" * n
            + "\n  vowels: [a]\n  phonotactics: (C)V\n  tones: 0\n")


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    with open(path, "rb") as handle:
        return sha256_bytes(handle.read())


def pick_scratch(explicit=None):
    """First writable scratch root: --scratch, TMPDIR, /var/tmp, system temp, repo.

    The swarm saturates the tmpfs /tmp (ENOSPC observed 2026-10-17), so a
    scratch root is probed with a one-byte write before it is used.
    """
    candidates = [explicit] if explicit else []
    candidates += [os.environ.get("TMPDIR"), "/var/tmp", tempfile.gettempdir(), REPO]
    for candidate in candidates:
        if not candidate:
            continue
        try:
            os.makedirs(candidate, exist_ok=True)
            probe = os.path.join(candidate, ".neg-10-probe-%d" % os.getpid())
            with open(probe, "w", encoding="utf-8") as handle:
                handle.write("probe")
            os.unlink(probe)
            return candidate
        except OSError:
            continue
    return None


def run_gate(gate, text, scratch, timeout=60):
    with tempfile.TemporaryDirectory(dir=scratch) as d:
        path = os.path.join(d, "packet.yml")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
        try:
            proc = subprocess.run(
                [sys.executable, gate, path],
                capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            return "TIMEOUT", ""
        return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def pre_fix_pattern(rc, out):
    """The defect's signature: crash code 1, traceback, no G-DATA finding."""
    return (rc == 1 and "RecursionError" in out and "G-DATA" not in out)


def materialize_pre_fix(rev, names, scratch):
    out_dir = tempfile.mkdtemp(dir=scratch, prefix="neg-10-pre-fix-")
    paths, digests = {}, {}
    for name in names:
        rel = GATES[name]
        proc = subprocess.run(
            ["git", "-C", REPO, "show", "%s:%s" % (rev, rel)],
            capture_output=True)
        if proc.returncode != 0:
            raise SystemExit("NEG-10 ERROR: git show %s:%s failed: %s"
                             % (rev, rel, proc.stderr.decode("utf-8", "replace").strip()))
        data = proc.stdout
        digest = sha256_bytes(data)
        digests[name] = digest
        if digest != PRE_FIX_SHA256[name]:
            raise SystemExit(
                "NEG-10 ERROR: %s at %s is not the pinned pre-fix revision "
                "(%s != %s)" % (rel, rev, digest, PRE_FIX_SHA256[name]))
        path = os.path.join(out_dir, os.path.basename(rel))
        with open(path, "wb") as handle:
            handle.write(data)
        paths[name] = path
    return paths, digests


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="neg-10-control.py",
        description=__doc__.split("\n\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--rev", default=None,
                        help="materialise pre-fix gate bytes from this git revision "
                             "(e.g. cf338a7) instead of testing the live gates")
    parser.add_argument("--gate", default=None,
                        help="test one gate copy at this path (name inferred by basename)")
    parser.add_argument("--scratch", default=None,
                        help="parent directory for temporary payloads/pre-fix copies")
    parser.add_argument("--json", default=None,
                        help="write a machine-readable receipt to this path")
    args = parser.parse_args(argv)

    if args.scratch:
        os.makedirs(args.scratch, exist_ok=True)
    scratch = pick_scratch(args.scratch)
    print("NEG-10 scratch root: %s" % scratch)

    names = list(GATES)
    paths = {name: os.path.join(REPO, GATES[name]) for name in names}
    digests = {name: sha256_file(path) for name, path in paths.items()}
    source = "live worktree"
    if args.rev:
        paths, digests = materialize_pre_fix(args.rev, names, scratch)
        source = "git %s (pinned pre-fix bytes)" % args.rev
    elif args.gate:
        gate = os.path.abspath(args.gate)
        if not os.path.isfile(gate):
            print("NEG-10 ERROR: gate not found: %s" % gate)
            return 2
        base = os.path.basename(gate)
        inferred = [n for n in names if os.path.basename(GATES[n]) == base]
        if not inferred:
            print("NEG-10 ERROR: cannot infer gate name from %s" % base)
            return 2
        names = inferred
        paths = {names[0]: gate}
        digests = {names[0]: sha256_file(gate)}
        source = "explicit copy %s" % gate

    print("NEG-10 gates under test (%s):" % source)
    for name in names:
        print("NEG-10   %-9s %s  sha256=%s%s"
              % (name, paths[name], digests[name],
                 "  [PINNED PRE-FIX]" if digests[name] == PRE_FIX_SHA256[name] else ""))

    checks = []
    failures = []
    pre_fix_seen = []

    def check(name, gate_name, payload_label, payload, predicate, describe):
        rc, out = run_gate(paths[gate_name], payload, scratch)
        ok = predicate(rc, out)
        checks.append({"gate": gate_name, "check": payload_label,
                       "rc": rc, "ok": bool(ok),
                       "output_head": out.strip().splitlines()[:3]})
        print("NEG-10 %-9s %-24s rc=%-4s %s"
              % (gate_name, payload_label, rc, "PASS" if ok else "FAIL"))
        if not ok:
            failures.append("%s/%s: %s" % (gate_name, payload_label, describe(rc, out)))
            if pre_fix_pattern(rc, out):
                pre_fix_seen.append("%s/%s" % (gate_name, payload_label))

    for name in names:
        deep_ok = lambda rc, out: (  # noqa: E731
            rc == 2 and "G-DATA" in out and CAP_MARK in out
            and "RecursionError" not in out and "Traceback" not in out)
        deep_desc = lambda rc, out: (  # noqa: E731
            "expected rc=2 with a G-DATA finding naming the depth cap and no "
            "traceback; observed rc=%s output=%r" % (rc, out.strip().splitlines()[:3]))
        check(name, name, "deep-bracket-nesting", deep_bracket(), deep_ok, deep_desc)
        check(name, name, "deep-brace-nesting", deep_brace(), deep_ok, deep_desc)

        fixture = os.path.join(REPO, FIXTURES[name])
        if os.path.isfile(fixture):
            with open(fixture, encoding="utf-8") as handle:
                fixture_text = handle.read()
            check(
                name, name, "fixture-packet-unaffected", fixture_text,
                lambda rc, out: (CAP_MARK not in out
                                 and "RecursionError" not in out
                                 and "Traceback" not in out),
                lambda rc, out: (
                    "regression: the committed fixture packet now hits the "
                    "depth cap or a traceback: rc=%s output=%r"
                    % (rc, out.strip().splitlines()[:3])))
        else:
            print("NEG-10 %-9s %-24s SKIP (fixture missing)" % (name, "fixture-packet-unaffected"))

    if not args.gate and not args.rev:
        paths["lexicon"] = os.path.join(REPO, LEXICON)
        check(
            "lexicon", "lexicon", "deep-bracket-nesting",
            deep_bracket(),
            lambda rc, out: rc == 2 and "Traceback" not in out,
            lambda rc, out: (
                "reference gate no longer rejects deep nesting with exit 2: "
                "rc=%s output=%r" % (rc, out.strip().splitlines()[:3])))

    passed = sum(1 for item in checks if item["ok"])
    if not failures:
        verdict = "PASS"
    elif pre_fix_seen and len(pre_fix_seen) == len(failures):
        verdict = "PRE-FIX-PATTERN-OBSERVED"
    else:
        verdict = "CONTROL-FAILED"

    print("NEG-10 SUMMARY: %d/%d checks passed; verdict=%s"
          % (passed, len(checks), verdict))
    for item in failures:
        print("NEG-10 FAILURE: %s" % item)

    if args.json:
        receipt = {
            "control": "neg-10-control.py",
            "shard": "R8-O10",
            "defect_index": 6,
            "defect": "review 26 §3 D6 — uncaught RecursionError on deep flow nesting",
            "source": source,
            "checked_at_utc": datetime.datetime.now(
                datetime.timezone.utc).replace(microsecond=0).isoformat(),
            "gate_digests": digests,
            "pre_fix_pins": PRE_FIX_SHA256,
            "checks": checks,
            "failures": failures,
            "verdict": verdict,
        }
        with open(args.json, "w", encoding="utf-8") as handle:
            json.dump(receipt, handle, indent=1, sort_keys=True)
            handle.write("\n")

    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
