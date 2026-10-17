#!/usr/bin/env python3
"""Negative control for round-8 defect index 4 = `R26-D2-lexicon`
(supplement review 26 §3 defect D2, lexicon loader instance).

Defect under control: `tools/gates/lexicon-coverage-audit.py` let duplicate
mapping keys last-win silently — in block mappings (`lexicon:` declared twice)
and on the JSON path (`json.loads` without `object_pairs_hook`), with the flow
mapping path overwriting too. Review 26 §3 D2 cites the overwrite site
(`:465` block, JSON `:498-503`); the inventory's own HEAD-byte reproduction is
`load_packet('{"lexicon":[a],"lexicon":[b]}') -> [{'term': 'b'}]`, no error.
An author's stale key therefore changed the audit outcome with no diagnostic.

State of the repair (attribution): the duplicate-key rejection is **already
present in the working tree** when shard R8-O08 ran (`duplicate key` in flow
mappings and block mappings, `object_pairs_hook=_json_object_no_duplicates` on
the JSON path). This shard did not write those hunks; it verified them and
ships the isolated control the O-claim requires (fail-before = the pre-fix
bytes, pass-after = the working tree).

Contract (one expectation set, both modes):
  * pointed at the LIVE (post-fix) gate -> every check passes, exit 0;
  * pointed at PRE-FIX bytes (`--gate <pre-fix copy>` or
    `--pre-fix-from-git [REV]`, default REV `cf338a7`) -> the duplicate-key
    checks observe the pre-fix pattern (no duplicate diagnostic, the packet is
    evaluated with the last key winning) and the control exits 1, naming the
    pattern.

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
    <repo>/tools/gates/lexicon-coverage-audit.py
"""

import argparse
import hashlib
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
DEFAULT_GATE = os.path.join(REPO, "tools", "gates", "lexicon-coverage-audit.py")
GATE_REL = "tools/gates/lexicon-coverage-audit.py"

# Review 26 §0 pin for the committed pre-fix bytes (HEAD cf338a7 / e7ca0fa).
PREFIX_SHA256_COMMITTED = (
    "63ee4ec6b15188fefa3e997766971d66fe4d7d7bf9eed65cdcdd55f548fe8a80")
KNOWN_PREFIX = {
    PREFIX_SHA256_COMMITTED: "review-26 §0 pin / committed cf338a7 bytes",
}

ENTRY_A = '{"term": "a", "gloss": "g", "field": "body"}'
ENTRY_B = '{"term": "b", "gloss": "g", "field": "body"}'

JSON_DUP = '{"lexicon": [%s], "lexicon": [%s]}' % (ENTRY_A, ENTRY_B)
JSON_CLEAN = '{"name": "t", "lexicon": [%s]}' % ENTRY_A
YAML_BLOCK_DUP = (
    "name: t\n"
    "lexicon:\n"
    "  - {term: a, gloss: g, field: body}\n"
    "lexicon:\n"
    "  - {term: b, gloss: g, field: body}\n"
)
YAML_QUOTED_DUP = (
    "name: t\n"
    "lexicon:\n"
    "  - {term: a, gloss: g, field: body}\n"
    '"lexicon":\n'
    "  - {term: b, gloss: g, field: body}\n"
)
YAML_CLEAN = (
    "name: t\n"
    "lexicon:\n"
    "  - {term: a, gloss: g, field: body}\n"
)
YAML_FLOW_DUP = "name: t\nlexicon: {a: 1, a: 2}\n"
YAML_NESTED_DUP = (
    "name: t\n"
    "lexicon:\n"
    "  - {term: a, gloss: g, gloss: h, field: body}\n"
)
YAML_REPEATED_KEYS_OK = (
    "name: t\n"
    "lexicon:\n"
    "  - {term: a, gloss: g, field: body}\n"
    "  - {term: b, gloss: g, field: body}\n"
)
YAML_TAB = (
    "name: t\n"
    "lexicon:\n"
    "\t- {term: a, gloss: g, field: body}\n"
)


def _scratch():
    """TemporaryDirectory, falling back next to this control on temp failure."""
    try:
        return tempfile.TemporaryDirectory()
    except OSError:
        return tempfile.TemporaryDirectory(dir=HERE)


def run_gate(gate, text, suffix=".yml", timeout=30):
    with _scratch() as d:
        path = os.path.join(d, "packet" + suffix)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
        proc = subprocess.run(
            [sys.executable, gate, path],
            capture_output=True, text=True, timeout=timeout)
        return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


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
        gate = os.path.join(scratch.name, "lexicon-coverage-audit.prefix.py")
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
        print("NEG-08 note: PRE-FIX bytes (%s); duplicate-key checks below are "
              "expected to FAIL." % KNOWN_PREFIX[digest])

    failures = []
    checks = 0

    def check(name, payload, suffix, predicate, describe):
        nonlocal checks
        checks += 1
        rc, out = run_gate(gate, payload, suffix)
        ok = predicate(rc, out)
        print("NEG-08 %-36s rc=%s %s" % (name, rc, "PASS" if ok else "FAIL"))
        if not ok:
            failures.append("%s: %s" % (name, describe(rc, out)))

    def rejects_dup(token):
        return (lambda rc, out: rc == 2 and "duplicate key" in out
                and token in out)

    def dup_why(token):
        return (lambda rc, out: "PRE-FIX PATTERN OBSERVED: the duplicate key "
                "was not reported (expected exit 2 naming %r) — rc=%s output=%r"
                % (token, rc, out.strip().splitlines()[:2]))

    # C1: duplicate key on the JSON path (review 26's own reproduction).
    check("json-duplicate-key-rejected", JSON_DUP, ".json",
          rejects_dup("'lexicon'"), dup_why("'lexicon'"))
    # C2: duplicate block-mapping key.
    check("block-duplicate-key-rejected", YAML_BLOCK_DUP, ".yml",
          rejects_dup("'lexicon'"), dup_why("'lexicon'"))
    # C3: duplicate key in a flow mapping.
    check("flow-duplicate-key-rejected", YAML_FLOW_DUP, ".yml",
          rejects_dup("'a'"), dup_why("'a'"))
    # C4: duplicate key nested inside an entry's flow mapping.
    check("nested-duplicate-key-rejected", YAML_NESTED_DUP, ".yml",
          rejects_dup("'gloss'"), dup_why("'gloss'"))
    # C5: a quoted key colliding with its plain spelling is the same key.
    check("quoted-plain-key-collision-rejected", YAML_QUOTED_DUP, ".yml",
          rejects_dup("'lexicon'"), dup_why("'lexicon'"))

    # G1 (guard): a clean JSON packet still evaluates, and the duplicate
    # diagnostic does not fire.
    rc_json, out_json = run_gate(gate, JSON_CLEAN, ".json")
    checks += 1
    if rc_json in (0, 1) and "duplicate key" not in out_json:
        print("NEG-08 %-36s rc=%s PASS" % ("guard-clean-json-evaluates", rc_json))
    else:
        print("NEG-08 %-36s rc=%s FAIL" % ("guard-clean-json-evaluates", rc_json))
        failures.append("guard-clean-json-evaluates: regression: a duplicate-free "
                        "JSON packet no longer evaluates: rc=%s output=%r"
                        % (rc_json, out_json.strip().splitlines()[:2]))

    # G2 (guard): a clean YAML packet still evaluates identically to its JSON
    # twin (the duplicate screen must not change clean-packet behaviour).
    rc_yaml, out_yaml = run_gate(gate, YAML_CLEAN, ".yml")
    checks += 1
    if (rc_yaml, out_yaml) == (rc_json, out_json):
        print("NEG-08 %-36s rc=%s PASS" % ("guard-clean-yaml-equals-json", rc_yaml))
    else:
        print("NEG-08 %-36s rc=%s FAIL" % ("guard-clean-yaml-equals-json", rc_yaml))
        failures.append("guard-clean-yaml-equals-json: regression: clean YAML and "
                        "JSON twins disagree: yaml rc=%s %r vs json rc=%s %r"
                        % (rc_yaml, out_yaml.strip().splitlines()[:1],
                           rc_json, out_json.strip().splitlines()[:1]))

    # G3 (guard): the same key in *different* mappings is not a duplicate.
    check("guard-repeated-keys-across-entries-ok", YAML_REPEATED_KEYS_OK, ".yml",
          lambda rc, out: "duplicate key" not in out,
          lambda rc, out: "regression: repeated keys in sibling entries are "
          "misreported as duplicates: rc=%s output=%r"
          % (rc, out.strip().splitlines()[:2]))

    # G4 (guard): the declared subset still rejects tab indentation.
    check("guard-tab-indentation-still-exit-2", YAML_TAB, ".yml",
          lambda rc, out: rc == 2 and "tab" in out,
          lambda rc, out: "regression: tab indentation no longer rejected: "
          "rc=%s output=%r" % (rc, out.strip().splitlines()[:2]))

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
