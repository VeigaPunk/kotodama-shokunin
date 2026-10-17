#!/usr/bin/env python3
"""Negative control for round-8 defect R8-O06 — defect index 2 = review 26 §3 D2
(duplicate mapping keys silently last-win), on the three culture-packet loaders
still carrying the defect when this shard started:

  * tools/gates/costume-era-consistency-gate.py  (inventory row R26-D2-costume)
  * tools/gates/lexicon-coverage-audit.py        (inventory row R26-D2-lexicon)
  * tools/gates/myth-consistency-gate.py         (inventory row R26-D2-myth)

Sibling shards repaired and controlled the other two rows of the same register
entry (R8-O05/neg-05 = phonology, R8-O07/neg-07 = naming); this control closes
the remaining three loaders so review 26's recommended move 2 ("reject
duplicate keys uniformly in block and flow mappings, and on the JSON path")
holds for all five packet gates.

Defect under control (review 26 §3 D2, reports/supplement-opencode-1/
26-parser-controls.md): a repeated mapping key silently overwrote the earlier
value with no diagnostic, so an author's stale key changed the audit outcome
while the gate still printed an ordinary verdict. Repaired sites:

  * costume: block mapping (_parse_map), flow mapping (_flow), sequence
    mapping entry merge (_parse_list), JSON path (object_pairs_hook);
  * lexicon: block mapping (_parse_map), flow mapping (_flow_value), JSON path
    (load_packet object_pairs_hook);
  * myth: flow mapping (_parse_flow); its block-mapping duplicate check
    pre-existed (review 26 §1.4) and is exercised here as a control too.

Contract (one expectation set, two legs):
  * live (post-fix) gates — every check passes, exit 0;
  * pre-fix bytes (--prefix-dir DIR, or --pre-fix-from-git [REV] which
    materialises them from git into a scratch directory) — the duplicate-key
    checks observe the pre-fix pattern and this control exits 1, naming it.
    Fail-before, pass-after: on the pre-fix bytes the CLI checks print a clean
    verdict (rc=0) for a packet whose keys collide, and the in-memory checks
    receive a silently merged dict whose value is the LAST one.

The CLI payloads are the live example packet (examples/culture-d2/packet.d2.yml,
rc=0 on all three gates) with one duplicate appended, so a pre-fix run is a
*verdict* about colliding keys, not an unrelated rejection. The in-memory
checks call the loader's own parse entry point (importlib, no file written).

Isolation: payloads are written only into a scratch directory (TMPDIR when
writable, else a per-user cache dir); gates are invoked as subprocesses or
imported read-only (bytecode writing disabled); nothing under the repository
is written by this control.

Usage:
    python3 neg-06-control.py                      # live gates -> exit 0
    python3 neg-06-control.py --prefix-dir DIR     # pre-fix copies -> exit 1
    python3 neg-06-control.py --pre-fix-from-git   # same, via git show HEAD
"""

import argparse
import hashlib
import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
GATES_DIR = os.path.join(REPO, "tools", "gates")
EXAMPLE_PACKET = os.path.join(REPO, "examples", "culture-d2", "packet.d2.yml")

GATES = ("costume-era-consistency-gate.py",
         "lexicon-coverage-audit.py",
         "myth-consistency-gate.py")

# Loader entry points used by the in-memory checks (per gate).
PARSE_ENTRY = {"costume-era-consistency-gate.py": "parse_packet",
               "lexicon-coverage-audit.py": "load_packet",
               "myth-consistency-gate.py": "parse_packet"}
HAS_JSON_PATH = {"costume-era-consistency-gate.py",
                 "lexicon-coverage-audit.py"}

# Review 26 §0 sha256 pins for the pre-fix bytes of each repaired loader
# (blob fe34faa == HEAD cf338a7 at control-authoring time, unchanged).
PREFIX_SHA256 = {
    "costume-era-consistency-gate.py":
        "29a9361c7b96a354c41a3994e3459a951ce0a43425b3984d6506b3e5b3a43f03",
    "lexicon-coverage-audit.py":
        "63ee4ec6b15188fefa3e997766971d66fe4d7d7bf9eed65cdcdd55f548fe8a80",
    "myth-consistency-gate.py":
        "26d246e9936db4375c31c6eb260545bf55051d11ec00bb1e757458399b1b55c5",
}

BLOCK_DUP_SUFFIX = "\nname: dup-probe\n"
FLOW_DUP_SUFFIX = "\nprobe: {k: 1, k: 2}\n"
ENTRY_DUP_SUFFIX = "\nprobe_list:\n  - a: 1\n    a: 2\n"
JSON_DUP = '{"name": "a", "name": "b"}'


def scratch_dir():
    """A writable scratch directory outside the repository.

    The round-8 wave observed /tmp inode/space exhaustion, so the system temp
    dir is probed (a directory can be created while writing a file still
    fails); a per-user cache directory is used when that probe fails.
    """
    fallback = os.path.join(os.path.expanduser("~"), ".cache", "neg06-scratch")
    last_error = None
    for base in (None, fallback):
        try:
            if base:
                os.makedirs(base, exist_ok=True)
            path = tempfile.mkdtemp(prefix="neg06-", dir=base)
            probe = os.path.join(path, ".probe")
            with open(probe, "w", encoding="utf-8") as handle:
                handle.write("x")
            os.remove(probe)
            return path
        except OSError as error:
            last_error = error
    raise OSError("no writable scratch directory for neg-06: %s" % last_error)


def run_gate(gate, text, suffix=".yml", timeout=60):
    last_error = None
    for _ in range(2):
        work = scratch_dir()
        try:
            path = os.path.join(work, "packet" + suffix)
            try:
                with open(path, "w", encoding="utf-8") as handle:
                    handle.write(text)
            except OSError as error:
                last_error = error
                continue
            proc = subprocess.run([sys.executable, gate, path],
                                  capture_output=True, text=True, timeout=timeout)
            return proc.returncode, (proc.stdout or "") + (proc.stderr or "")
        finally:
            shutil.rmtree(work, ignore_errors=True)
    raise OSError("neg-06 could not write its payload: %s" % last_error)


def load_gate_module(gate):
    """Import a gate script in-process without writing bytecode."""
    spec = importlib.util.spec_from_file_location(
        "neg06_gate_" + os.path.basename(gate).replace("-", "_").replace(".", "_"),
        gate)
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


def call_parse(module, entry, text):
    """Return ('raised', message) or ('returned', value)."""
    try:
        return "returned", getattr(module, entry)(text)
    except Exception as error:  # the gates raise their own parse errors
        return "raised", "%s: %s" % (type(error).__name__, error)


def gate_sha256(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prefix-dir",
                        help="directory holding pre-fix copies of the three "
                             "gates (same file names); checks are expected to "
                             "fail there")
    parser.add_argument("--pre-fix-from-git", nargs="?", const="HEAD",
                        default=None, metavar="REV",
                        help="materialise pre-fix gate copies with "
                             "`git show REV:tools/gates/<gate>` (default REV "
                             "HEAD) into a scratch dir, then run the pre-fix "
                             "leg")
    args = parser.parse_args()

    if args.prefix_dir and args.pre_fix_from_git:
        parser.error("choose one of --prefix-dir / --pre-fix-from-git")

    prefix_dir = args.prefix_dir
    scratch = None
    if args.pre_fix_from_git:
        scratch = scratch_dir()
        prefix_dir = scratch
        for gate in GATES:
            result = subprocess.run(
                ["git", "-C", REPO, "show",
                 "%s:tools/gates/%s" % (args.pre_fix_from_git, gate)],
                capture_output=True, text=True)
            if result.returncode != 0:
                print("NEG-06 ERROR: git show failed for %s: %s"
                      % (gate, result.stderr.strip()))
                shutil.rmtree(scratch, ignore_errors=True)
                return 2
            with open(os.path.join(scratch, gate), "w", encoding="utf-8") as handle:
                handle.write(result.stdout)

    base_packet = open(EXAMPLE_PACKET, encoding="utf-8").read()
    failures = []
    checks = 0

    def record(name, ok, detail):
        nonlocal checks
        checks += 1
        print("NEG-06 %-42s %s" % (name, "PASS" if ok else "FAIL"))
        if not ok:
            failures.append("%s: %s" % (name, detail))

    def cli_check(name, gate, text, suffix=".yml"):
        rc, out = run_gate(gate, text, suffix)
        dup = "duplicate key" in out
        if rc == 2 and dup:
            record(name, True, "")
        else:
            record(name, False,
                   "PRE-FIX PATTERN OBSERVED: rc=%s, no duplicate-key "
                   "diagnostic — the loader evaluated or silently merged "
                   "colliding keys; expected rc=2 naming the duplicate. "
                   "output=%r" % (rc, out.strip().splitlines()[:2]))

    def clean_check(name, gate, text):
        rc, out = run_gate(gate, text)
        if rc == 0 and "duplicate key" not in out:
            record(name, True, "")
        else:
            record(name, False,
                   "regression: the example packet no longer evaluates "
                   "cleanly: rc=%s output=%r" % (rc, out.strip().splitlines()[:2]))

    def parser_check(name, gate_file, gate, text):
        module = load_gate_module(gate)
        status, payload = call_parse(module, PARSE_ENTRY[gate_file], text)
        if status == "raised" and "duplicate key" in str(payload):
            record(name, True, "")
        else:
            record(name, False,
                   "PRE-FIX PATTERN OBSERVED: parse returned %s (no "
                   "duplicate-key error) — last-wins value=%r; expected a "
                   "parse error naming the duplicate"
                   % (status, payload if status == "returned" else str(payload)))

    for gate_file in GATES:
        gate = (os.path.join(prefix_dir, gate_file) if prefix_dir
                else os.path.join(GATES_DIR, gate_file))
        if not os.path.isfile(gate):
            print("NEG-06 ERROR: gate not found: %s" % gate)
            if scratch:
                shutil.rmtree(scratch, ignore_errors=True)
            return 2
        digest = gate_sha256(gate)
        print("NEG-06 gate under test: %s sha256=%s" % (gate, digest))
        if digest == PREFIX_SHA256[gate_file]:
            print("NEG-06 note: this is the review-26 pinned PRE-FIX byte copy "
                  "for %s; duplicate-key checks below are expected to FAIL."
                  % gate_file)

        cli_check("%s block-duplicate" % gate_file, gate,
                  base_packet.rstrip("\n") + BLOCK_DUP_SUFFIX)
        cli_check("%s flow-duplicate" % gate_file, gate,
                  base_packet.rstrip("\n") + FLOW_DUP_SUFFIX)
        cli_check("%s sequence-entry-duplicate" % gate_file, gate,
                  base_packet.rstrip("\n") + ENTRY_DUP_SUFFIX)
        if gate_file in HAS_JSON_PATH:
            parser_check("%s json-duplicate-in-memory" % gate_file,
                         gate_file, gate, JSON_DUP)
        parser_check("%s block-duplicate-in-memory" % gate_file,
                     gate_file, gate, "name: a\nname: b\n")
        clean_check("%s live-example-packet-clean" % gate_file, gate,
                    base_packet)

    if scratch:
        shutil.rmtree(scratch, ignore_errors=True)

    if failures:
        print("NEG-06 RESULT: FAIL (%d/%d checks)" % (len(failures), checks))
        for line in failures:
            print("NEG-06 FAILURE: %s" % line)
        return 1
    print("NEG-06 RESULT: PASS (%d/%d checks)" % (checks, checks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
