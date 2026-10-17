#!/usr/bin/env python3
"""Negative control for round-8 defect R8-O09 (supplement review 26, defect D5).

Defect under control (review 26 §3 D5, "Tab indentation has four different
outcomes"; the same register entry also files the naming gate's multi-document
merge): the five culture-packet gates disagreed about tab indentation and about
`---`-separated streams, so the same authored bytes were audited as a different
document depending on which gate read them:

  * phonology-sanity-gate.py  silently rewrote tabs to 2 spaces and audited the
    rewritten document (rc=0 on a clean tab-indented packet);
  * costume-era-consistency-gate.py silently rewrote tabs to 4 spaces and
    audited that (rc=1, identical findings to the space-indented twin);
  * myth-consistency-gate.py's tab guard tested only the *space* prefix, so a
    leading tab slipped through and died later with the misleading
    `FINDING G-DATA: unparsed YAML content at token N`;
  * naming-collision-gate.py merged `---`-separated documents into one packet
    and evaluated the union (rc=1) although its docstring declares
    "No anchors, tags, multi-document streams, or tab indentation; input
    outside the subset exits 2 instead of being guessed."

Correct semantics (the declared subset policy, already implemented by
naming-collision-gate.py and lexicon-coverage-audit.py): input outside the
subset exits 2 with an explicit diagnostic instead of being guessed.  A single
leading `---` (document-start marker, not a second document) stays accepted.

Contract:
  * pointed at the LIVE (post-fix) gates -> every check passes, exit 0;
  * pointed at PRE-FIX bytes (`--baseline-rev REV` extracts
    `REV:tools/gates/<gate>.py` with `git show` into a temporary directory;
    `--gates DIR` accepts an already-extracted copy) -> the tab and
    multi-document checks observe the pre-fix pattern and the control exits 1,
    naming each pattern.

Isolation: payloads and baseline copies are written only into
tempfile.TemporaryDirectory(); gates are invoked as subprocesses; nothing under
the repository is written by this control.

Usage:
    python3 neg-09-control.py
    python3 neg-09-control.py --baseline-rev <git-rev>
    python3 neg-09-control.py --gates <dir-with-five-gate-copies>
"""

import argparse
import hashlib
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
LIVE_GATES = os.path.join(REPO, "tools", "gates")
FIXTURES = os.path.join(REPO, "tools", "gates", "fixtures")

# Review 26 §0 pins for the pre-fix bytes (blob fe34faa, unchanged at the
# round-8 baseline cf338a7).
PREFIX_PINS = {
    "phonology-sanity-gate.py":
        "fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655",
    "naming-collision-gate.py":
        "8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526",
    "myth-consistency-gate.py":
        "26d246e9936db4375c31c6eb260545bf55051d11ec00bb1e757458399b1b55c5",
    "costume-era-consistency-gate.py":
        "29a9361c7b96a354c41a3994e3459a951ce0a43425b3984d6506b3e5b3a43f03",
    "lexicon-coverage-audit.py":
        "63ee4ec6b15188fefa3e997766971d66fe4d7d7bf9eed65cdcdd55f548fe8a80",
}

GATES = ["phonology-sanity-gate.py", "naming-collision-gate.py",
         "myth-consistency-gate.py", "costume-era-consistency-gate.py",
         "lexicon-coverage-audit.py"]

# Review 26 §4 reproduce block, tab-indented variant (its §2 matrix payload).
TAB_MINIMAL = (
    "name: t\n"
    "phonology:\n"
    "\tconsonants: [p, t, k, m, n, s, l]\n"
    "\tvowels: [a, e, i, o, u]\n"
    "\tphonotactics: (C)V(C)\n"
    "\ttones: 0\n"
    "\tnotable_rules:\n"
    "\t  - \"t \u2192 ts / _i\"\n"
)

MULTIDOC = (
    "name: m\n"
    "phonology:\n"
    "  consonants: [p, t, k, m, n, s, l]\n"
    "  vowels: [a, e, i, o, u]\n"
    "  phonotactics: (C)V(C)\n"
    "  tones: 0\n"
    "names:\n"
    "  - {name: tl, id: N1, type: person}\n"
    "---\n"
    "name: m2\n"
    "names:\n"
    "  - {name: tl, id: N2, type: place}\n"
)
LEADING_MARKER = (
    "---\n"
    "name: lm\n"
    "phonology:\n"
    "  consonants: [p, t, k, m, n, s, l]\n"
    "  vowels: [a, e, i, o, u]\n"
    "  phonotactics: (C)V(C)\n"
    "  tones: 0\n"
)


def tabify(text):
    """Convert 2-space indentation steps to one tab, preserving any odd space."""
    out = []
    for line in text.splitlines():
        n = len(line) - len(line.lstrip(" "))
        out.append("\t" * (n // 2) + " " * (n % 2) + line[n:])
    return "\n".join(out) + "\n"


def read_fixture(name):
    with open(os.path.join(FIXTURES, name), encoding="utf-8") as handle:
        return handle.read()


def run_gate(gate_path, text, timeout=30):
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "packet.yml")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
        proc = subprocess.run([sys.executable, gate_path, path],
                              capture_output=True, text=True, timeout=timeout)
        return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def finding_ids(output):
    ids = []
    for line in output.splitlines():
        if line.startswith("FINDING "):
            ids.append(line.split(":", 1)[0].split()[1])
    return ids


def materialize_baseline(rev):
    """Extract the five gate files at `rev` into a fresh temp dir (caller owns)."""
    target = tempfile.mkdtemp(prefix="neg-09-baseline-")
    for name in GATES:
        proc = subprocess.run(
            ["git", "-C", REPO, "show", "%s:tools/gates/%s" % (rev, name)],
            capture_output=True)
        if proc.returncode != 0:
            raise SystemExit("NEG-09 ERROR: git show %s:tools/gates/%s failed: %s"
                             % (rev, name, proc.stderr.decode("utf-8", "replace")))
        with open(os.path.join(target, name), "wb") as handle:
            handle.write(proc.stdout)
    return target


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gates", default=None,
                    help="directory holding the five gate copies (default: live tools/gates)")
    ap.add_argument("--baseline-rev", default=None,
                    help="git revision whose tools/gates bytes are the pre-fix copy")
    args = ap.parse_args()

    if args.gates and args.baseline_rev:
        print("NEG-09 ERROR: pass either --gates or --baseline-rev, not both")
        return 2
    gates_dir = os.path.abspath(args.gates) if args.gates else LIVE_GATES
    extracted = None
    if args.baseline_rev:
        extracted = materialize_baseline(args.baseline_rev)
        gates_dir = extracted

    print("NEG-09 gates under test: %s" % gates_dir)
    if args.baseline_rev:
        print("NEG-09 extracted pre-fix bytes from revision %s" % args.baseline_rev)
    hashes = {}
    for name in GATES:
        path = os.path.join(gates_dir, name)
        if not os.path.isfile(path):
            print("NEG-09 ERROR: gate not found: %s" % path)
            return 2
        with open(path, "rb") as handle:
            hashes[name] = hashlib.sha256(handle.read()).hexdigest()
        state = "PRE-FIX pinned bytes" if hashes[name] == PREFIX_PINS[name] else "post-fix/modified"
        print("NEG-09 %-32s sha256=%s (%s)" % (name, hashes[name][:16], state))
    pre_fix = all(hashes[name] == PREFIX_PINS[name] for name in GATES)
    if pre_fix:
        print("NEG-09 note: all five gates match the review-26 §0 pre-fix pins; "
              "the tab and multi-document checks below are expected to FAIL.")

    failures = []
    checks = 0

    def check(name, payload, predicate, describe):
        nonlocal checks
        checks += 1
        gate_file = name.split("/")[0]
        if not gate_file.endswith(".py"):
            gate_file += ".py"
        rc, out = run_gate(os.path.join(gates_dir, gate_file), payload)
        ids = finding_ids(out)
        ok = predicate(rc, ids, out)
        print("NEG-09 %-38s rc=%s ids=%s %s"
              % (name, rc, ",".join(ids) or "-", "PASS" if ok else "FAIL"))
        if not ok:
            failures.append("%s: %s" % (name, describe(rc, ids, out)))

    def no_tab_message(rc, ids, out):
        return "tab indentation is not supported" in out

    # C1-C5: each gate rejects tab indentation with its own explicit diagnostic.
    check("phonology-sanity-gate/tab-indent", TAB_MINIMAL,
          lambda rc, ids, out: rc == 2 and ids == ["G-DATA"] and no_tab_message(rc, ids, out),
          lambda rc, ids, out: ("PRE-FIX PATTERN OBSERVED: rc=%s ids=%s (expected "
                                "rc=2 G-DATA 'tab indentation is not supported'); "
                                "output=%r" % (rc, ids, out.strip().splitlines()[:2])))
    check("costume-era-consistency-gate/tab-indent",
          tabify(read_fixture("costume-era-consistency-gate.yml")),
          lambda rc, ids, out: rc == 2 and ids == ["G-DATA"] and no_tab_message(rc, ids, out),
          lambda rc, ids, out: ("PRE-FIX PATTERN OBSERVED: rc=%s ids=%s (expected "
                                "rc=2 G-DATA; the gate audited the tab-rewritten "
                                "packet instead). output=%r"
                                % (rc, ids, out.strip().splitlines()[:2])))
    check("myth-consistency-gate/tab-indent",
          tabify(read_fixture("myth-consistency-gate.yml")),
          lambda rc, ids, out: rc == 2 and ids == ["G-DATA"] and no_tab_message(rc, ids, out),
          lambda rc, ids, out: ("PRE-FIX PATTERN OBSERVED: rc=%s ids=%s (expected "
                                "rc=2 G-DATA 'tab indentation is not supported'; the "
                                "pre-fix guard missed leading tabs). output=%r"
                                % (rc, ids, out.strip().splitlines()[:2])))
    check("naming-collision-gate/tab-indent",
          tabify(read_fixture("naming-collision-gate.yml")),
          lambda rc, ids, out: rc == 2 and ids == ["G-DATA"] and no_tab_message(rc, ids, out),
          lambda rc, ids, out: ("regression: rc=%s ids=%s output=%r"
                                % (rc, ids, out.strip().splitlines()[:2])))
    check("lexicon-coverage-audit/tab-indent",
          tabify(read_fixture("lexicon-coverage-audit.yml")),
          lambda rc, ids, out: rc == 2 and "tabs are not allowed for indentation" in out,
          lambda rc, ids, out: ("regression: rc=%s ids=%s output=%r"
                                % (rc, ids, out.strip().splitlines()[:2])))

    # C6: cross-gate conformance on identical bytes (review 26 §6 rec 7):
    # every gate returns the could-not-evaluate code and names the tab.
    def conformance(rc, ids, out):
        return rc == 2 and "tab" in out.lower()

    for name in GATES:
        check("%s/conformance-tab" % name, TAB_MINIMAL, conformance,
              lambda rc, ids, out: ("PRE-FIX PATTERN OBSERVED: rc=%s ids=%s (the "
                                    "same bytes are not rejected by all five gates). "
                                    "output=%r" % (rc, ids, out.strip().splitlines()[:2])))

    # C7: space-indented twins keep their pre-fix verdicts (no over-rejection).
    # Expected (rc, first finding id) captured pre-fix on the committed fixtures;
    # the repair must not change any of them.
    twins = [
        ("phonology-sanity-gate.py", "phonology-sanity-gate.yml", 1, "A-TONE"),
        ("costume-era-consistency-gate.py", "costume-era-consistency-gate.yml", 1, "T-03"),
        ("myth-consistency-gate.py", "myth-consistency-gate.yml", 1, "MC-P01"),
        ("naming-collision-gate.py", "naming-collision-gate.yml", 1, "NAME-REUSE"),
        ("lexicon-coverage-audit.py", "lexicon-coverage-audit.yml", 1, "C-contrast-lost"),
    ]
    for gate_file, fixture, want_rc, want_id in twins:
        payload = read_fixture(fixture)
        check("%s/space-twin" % gate_file, payload,
              lambda rc, ids, out, want_rc=want_rc, want_id=want_id:
                  rc == want_rc and want_id in ids and "tab indentation" not in out,
              lambda rc, ids, out, want_rc=want_rc, want_id=want_id: (
                  "regression: space-indented fixture changed: rc=%s (want %s) "
                  "ids=%s (want %s) output=%r"
                  % (rc, want_rc, ids, want_id, out.strip().splitlines()[:2])))

    # C8: a `---`-separated stream is a second document, not a merged packet.
    check("naming-collision-gate/multi-document", MULTIDOC,
          lambda rc, ids, out: rc == 2 and ids == ["G-DATA"]
          and "multi-document streams are not supported" in out,
          lambda rc, ids, out: ("PRE-FIX PATTERN OBSERVED: rc=%s ids=%s (expected "
                                "rc=2 G-DATA 'multi-document streams are not "
                                "supported'; pre-fix the documents were merged and "
                                "the union evaluated). output=%r"
                                % (rc, ids, out.strip().splitlines()[:2])))

    # C9: one leading `---` is a document-start marker, not a second document;
    # it must keep evaluating (no over-rejection by the C8 fix).
    check("naming-collision-gate/leading-marker", LEADING_MARKER,
          lambda rc, ids, out: rc != 2 and "multi-document" not in out,
          lambda rc, ids, out: ("regression: a single leading `---` is now rejected: "
                                "rc=%s ids=%s output=%r"
                                % (rc, ids, out.strip().splitlines()[:2])))

    if extracted:
        subprocess.run(["rm", "-rf", extracted])
    if failures:
        print("NEG-09 RESULT: FAIL (%d/%d checks)" % (len(failures), checks))
        for line in failures:
            print("NEG-09 FAILURE: %s" % line)
        return 1
    print("NEG-09 RESULT: PASS (%d/%d checks)" % (checks, checks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
