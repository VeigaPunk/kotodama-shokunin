#!/usr/bin/env python3
"""Reference BINDING checker for the Ca correction — the minimal contract the
real accept-ca.py must implement so the junk payloads in junk-corrections.json
fail. Every constant is re-derived from committed bytes via git show; the
correction's own prose is never trusted.

Legs:
  RECEIPT-UNCHANGED  receipt bytes at --lands == receipt bytes at --freeze
  RECEIPT-DIGEST     correction.receipt_sha256 == sha256(receipt at measured_revision)
  REVISION           measured_revision is 40-hex, ancestor of --lands
  OLD-TOKEN          correction.old_token == token in receipt's S884 line at measured_revision
  ACTUAL-TOKEN       correction.actual_token == S884 used-by cell in corpus/SOURCES.md
                     at measured_revision, and != old_token
Baseline: no correction lands -> MISMATCH=1 UNRESOLVED=1 (exit 0).
All legs pass -> MISMATCH=1 UNRESOLVED=0 (exit 0). Any leg fails -> exit 1.

Usage: binding-checker.py --repo R --lands L --freeze F
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys

RECEIPT = "reports/round-78/telemetry/census-end.txt"
REGISTRY = "corpus/SOURCES.md"
CORRECTION = "reports/round-79/telemetry/census-correction.json"


def git_show(repo, rev, path):
    p = subprocess.run(
        ["git", "-C", repo, "show", f"{rev}:{path}"],
        capture_output=True, text=True,
    )
    if p.returncode != 0:
        return None
    return p.stdout


def receipt_token(text):
    for line in text.splitlines():
        if "W01 S884" in line:
            m = re.search(r"used-by=(\S+)", line)
            if m:
                return m.group(1)
    return None


def registry_used_by(text):
    for line in text.splitlines():
        parts = line.split("|")
        if len(parts) > 12 and parts[1].strip() == "S884":
            return parts[11].strip()
    return None


def is_ancestor(repo, anc, desc):
    return subprocess.run(
        ["git", "-C", repo, "merge-base", "--is-ancestor", anc, desc],
        capture_output=True,
    ).returncode == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--lands", required=True)
    ap.add_argument("--freeze", required=True)
    ap.add_argument("--expect-revision", default=None,
                    help="frozen expected measured_revision (real counter reads it from "
                         "git show <freeze>:reports/round-79/claims.json)")
    a = ap.parse_args()

    fails = []

    # Baseline re-derivation at the freeze commit: committed receipt vs committed registry.
    fz_receipt = git_show(a.repo, a.freeze, RECEIPT)
    fz_registry = git_show(a.repo, a.freeze, REGISTRY)
    if fz_receipt is None or fz_registry is None:
        print("ERROR: freeze bytes unreadable", file=sys.stderr)
        return 2
    base_mismatch = int(receipt_token(fz_receipt) != registry_used_by(fz_registry))
    print("BASELINE MISMATCH=%d (receipt token != registry token at freeze)"
          % base_mismatch)

    raw = git_show(a.repo, a.lands, CORRECTION)
    if raw is None:
        # do-nothing control: unresolved stays at the baseline count.
        print("MISMATCH=%d UNRESOLVED=%d (no correction landed)" % (base_mismatch, base_mismatch))
        return 0
    try:
        corr = json.loads(raw)
    except json.JSONDecodeError:
        print("LEG FAIL BINDABLE (correction is not parseable JSON)")
        return 1

    # RECEIPT-UNCHANGED
    ld_receipt = git_show(a.repo, a.lands, RECEIPT)
    if ld_receipt != fz_receipt:
        fails.append("RECEIPT-UNCHANGED")
        print("LEG FAIL RECEIPT-UNCHANGED (receipt bytes at lands != freeze)")

    # REVISION
    meas = corr.get("measured_revision", "")
    expect = a.expect_revision
      # the real accept-ca.py takes this constant from git show <freeze>:reports/round-79/claims.json
    if not (
        re.fullmatch(r"[0-9a-f]{40}", meas)
        and is_ancestor(a.repo, meas, a.lands)
        and (expect is None or meas == expect)
    ):
        fails.append("REVISION")
        print("LEG FAIL REVISION (measured_revision=%r not 40-hex ancestor of lands%s)"
              % (meas, "" if expect is None else " or != frozen expected %r" % expect))

    # RECEIPT-DIGEST
    m_receipt = git_show(a.repo, meas, RECEIPT) if re.fullmatch(r"[0-9a-f]{40}", meas) else None
    digest_ok = (
        m_receipt is not None
        and corr.get("receipt_sha256") == hashlib.sha256(m_receipt.encode()).hexdigest()
    )
    if not digest_ok:
        fails.append("RECEIPT-DIGEST")
        print("LEG FAIL RECEIPT-DIGEST (stated digest != committed receipt bytes)")

    # OLD-TOKEN
    old_ok = m_receipt is not None and corr.get("old_token") == receipt_token(m_receipt)
    if not old_ok:
        fails.append("OLD-TOKEN")
        print("LEG FAIL OLD-TOKEN (stated old_token != token in committed receipt S884 line)")

    # ACTUAL-TOKEN
    m_registry = git_show(a.repo, meas, REGISTRY) if re.fullmatch(r"[0-9a-f]{40}", meas) else None
    actual = registry_used_by(m_registry) if m_registry else None
    if not (actual and corr.get("actual_token") == actual and corr.get("actual_token") != corr.get("old_token")):
        fails.append("ACTUAL-TOKEN")
        print("LEG FAIL ACTUAL-TOKEN (stated actual_token != registry S884 used-by cell at measured revision)")

    if fails:
        print("MISMATCH=%d UNRESOLVED=%d VERDICT=FAIL legs failed: %s"
              % (base_mismatch, base_mismatch, ",".join(fails)))
        return 1
    print("MISMATCH=%d UNRESOLVED=0 VERDICT=PASS (all bindings re-derived from committed bytes)"
          % base_mismatch)
    return 0


if __name__ == "__main__":
    sys.exit(main())
