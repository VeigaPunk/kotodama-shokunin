#!/usr/bin/env python3
r"""Compatibility check: the round-75 accept-c.py EVIDENCE leg reads the
round-76 evidence file with its own parsers, unchanged.

Reads nothing it may not: the lane is queried with `git show <base>:<path>`
(read-only), the new file is read from this stage directory.  Writes nothing.

  python3 check-r75-leg.py [--evidence PATH]

Exit 0 when `_evidence_core` reports no problem, the Gate quote is inside the
stored window after the counter's fold, the fetch line names the row's
document, and the new file's header keys are a superset of the round-75 file's.
"""

import argparse
import hashlib
import importlib.util
import os
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
BASE = "98c486bdb4650ba5b8e651d332910e8ee60ad121"
STAGE = os.path.dirname(os.path.abspath(__file__))
R75_EVIDENCE = os.path.join(LANE, "reports", "round-75", "evidence", "S885.txt")


def load_counter():
    path = os.path.join(LANE, "reports", "round-75", "accept-c.py")
    spec = importlib.util.spec_from_file_location("accept_c_75", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def show(path):
    proc = subprocess.run(["git", "-C", LANE, "show", "%s:%s" % (BASE, path)],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit("git show failed for %s: %s" % (path, proc.stderr.strip()))
    return proc.stdout


def header_keys(text):
    keys = []
    for line in text.splitlines():
        if ":" in line and not line.startswith((" ", "\t", "-", "#")):
            name = line.split(":", 1)[0]
            if name and name[0].isalpha() and name not in keys:
                keys.append(name)
    return keys


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence",
                    default=os.path.join(STAGE, "evidence", "S885.txt"))
    ap.add_argument("--sid", default="S885")
    args = ap.parse_args(argv)
    r75 = load_counter()

    with open(args.evidence, "r", encoding="utf-8") as fh:
        new_text = fh.read()
    with open(R75_EVIDENCE, "r", encoding="utf-8") as fh:
        old_text = fh.read()

    def read_tree(mat, path):
        if path == "%s/%s.txt" % (r75.EVIDENCE_DIR, args.sid):
            return new_text
        if path == r75.REGISTRY:
            return show(r75.REGISTRY)
        if path == r75.LESSON:
            return show(r75.LESSON)
        raise r75.Missing("the check serves only the evidence file, the "
                          "registry and the round-75 lesson: %s" % path)

    r75.read_tree = read_tree
    ev = r75._evidence(None, args.sid)
    if ev is None:
        print("FAIL: accept-c _evidence() returned None")
        return 1
    lands_rows = r75.parse_rows(read_tree(None, r75.REGISTRY))
    gate_rows = r75.table_rows(r75.gate_section(read_tree(None, r75.LESSON)))
    access_date = "2026-10-27"

    bad, window = r75._evidence_core(ev, args.sid, access_date, lands_rows)
    print("_evidence_core: %s" % ("PASS" if not bad else "FAIL"))
    for problem in bad:
        print("  - %s" % problem)

    fetch_ok = r75._evidence_fetch_names_row(ev.get("fetch") or ev.get("url"),
                                             lands_rows, args.sid)
    print("fetch names the row's document: %s" % ("PASS" if fetch_ok else "FAIL"))

    grow = r75._gate_admit_row(gate_rows, args.sid, lands_rows)
    print("Gate admit row found: %s" % ("PASS" if grow is not None else "FAIL"))
    spans = []
    if grow is not None:
        spans = r75.dedupe(r75._evidence_gate_quote_candidates(
            gate_rows, grow, lands_rows, args.sid))
    print("Gate quote candidates: %r" % (spans,))
    folded = r75._evidence_fold(window or "")
    inside = [s for s in spans if s and s in folded]
    print("Gate quote inside the stored window: %s"
          % ("PASS" if inside else "FAIL"))

    old_keys, new_keys = header_keys(old_text), header_keys(new_text)
    missing = [k for k in old_keys if k not in new_keys]
    added = [k for k in new_keys if k not in old_keys]
    print("header keys: round-75 %d, round-76 %d, dropped %r, added %r"
          % (len(old_keys), len(new_keys), missing, added))
    digest = hashlib.sha256((window or "").encode("utf-8")).hexdigest()
    print("window digest: header %r, accept-c window %s"
          % (ev.get("window-sha256"), digest))

    ok = (not bad and fetch_ok and grow is not None and bool(inside)
          and not missing and bool(added))
    print("R75-EVIDENCE-LEG-READS-R76-FILE: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
