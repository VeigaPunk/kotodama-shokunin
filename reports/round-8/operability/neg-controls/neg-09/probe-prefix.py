#!/usr/bin/env python3
"""Pre-fix probe for R8-O09 (defect D5): capture what each of the five
culture-packet gates does with tab indentation and multi-document streams.

Its capture is the pre-fix leg of the control pair: the same payloads are
re-run post-fix (live) by neg-09-control.py, so the two outputs can be
diffed directly.

Read-only: payloads go into a TemporaryDirectory; gates are subprocesses.
Run from the lane repo root.  Usage: python3 probe-prefix.py [--gates DIR]
"""

import argparse
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
GATES = ["phonology-sanity-gate.py", "naming-collision-gate.py",
         "myth-consistency-gate.py", "costume-era-consistency-gate.py",
         "lexicon-coverage-audit.py"]

TAB_PACKET = (
    "name: t\n"
    "phonology:\n"
    "\tconsonants: [p, t, k, m, n, s, l]\n"
    "\tvowels: [a, e, i, o, u]\n"
    "\tphonotactics: (C)V(C)\n"
    "\ttones: 0\n"
    "\tnotable_rules:\n"
    "\t  - \"t \u2192 ts / _i\"\n"
)
SPACE_TWIN = TAB_PACKET.replace("\t", "  ")

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


def run_gate(gate, text, timeout=30):
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "packet.yml")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
        proc = subprocess.run([sys.executable, gate, path],
                              capture_output=True, text=True, timeout=timeout)
        return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gates", default=os.path.join(REPO, "tools", "gates"))
    args = ap.parse_args()
    for label, payload in (("tab-indent", TAB_PACKET),
                           ("space-twin", SPACE_TWIN),
                           ("multi-document", MULTIDOC),
                           ("leading-marker", LEADING_MARKER)):
        for name in GATES:
            rc, out = run_gate(os.path.join(args.gates, name), payload)
            first = [l for l in out.splitlines() if l.strip()][:1]
            print("%-15s %-32s rc=%-3s %s"
                  % (label, name, rc, (first[0][:110] if first else "(silent)")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
