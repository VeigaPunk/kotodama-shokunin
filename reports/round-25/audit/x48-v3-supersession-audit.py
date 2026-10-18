#!/usr/bin/env python3
"""X48 — v3 supersession prose-diff audit (round 25), read-only.

The handoff v3 packet family carries D4 claim prose copied from the round-20
baseline. Round 22's family-clean re-pin removed the inherited D2 rank
passengers from D4 ownership, so those rows described a state that no longer
exists. This seat measures the delta rather than asserting it, and — critically
— distinguishes a row that still *asserts* a stale number from one that names
that number as **removed**.

  R25-X48-1  live present state: the numbers the current D4 projection and
             expected-holds file actually carry.
  R25-X48-2  supersession-aware census: per revision and per claim row, whether
             the row asserts the stale value as present, asserts the live value,
             or names the old value as removed/superseded.
  R25-X48-3  supersession chain: the revision order, and which revision first
             corrects the five stale lines.
  R25-X48-4  passenger disposition: is `OQ-V3-05` still asserting the removed
             rank passengers, or has it been superseded?

Read-only. Opens nothing for writing; the receipt is the caller's stdout
redirect. `--selftest` runs in-memory controls and touches no repo byte.

    export TMPDIR=$PWD/.scratch
    python3 -B reports/round-25/audit/x48-v3-supersession-audit.py --selftest
    python3 -B reports/round-25/audit/x48-v3-supersession-audit.py
    python3 -B reports/round-25/audit/x48-v3-supersession-audit.py --json
"""

import argparse
import hashlib
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
PROJECTION = os.path.join(ROOT, "examples", "culture-d4", "typed-labels.d4.yml")
EXPECTED = os.path.join(ROOT, "examples", "culture-d4", "expected-holds.json")

# The v3 packet family in supersession order (oldest first). r4 is the round-25
# successor; a revision landing after this audit's stamp needs a dated refresh.
REVISIONS = [
    ("r20-packet", "reports/round-20/handoff/packet.md"),
    ("r22-declared-in", "reports/round-22/handoff/declared-in/packet.md"),
    ("r22-declared-in-r2", "reports/round-22/handoff/declared-in-r2/packet.md"),
    ("r23-declared-in-r3", "reports/round-23/wording/declared-in-r3/packet.md"),
    ("r25-declared-in-r4", "reports/round-25/v3-supersession/declared-in-r4/packet.md"),
]

CLAIM_IDS = ("D4-CL05", "D4-CL06", "D4-CL07", "D4-CL09")
OQ_ID = "OQ-V3-05"

# A row is STALE only if it asserts the old number *as present*. A row that
# names the old number as removed/superseded is CORRECTED, not stale — the
# distinction the claim's before-clause leaves unresolved.
REMOVED_MARKERS = (
    r"no longer D4-owned",
    r"removed from D4 ownership",
    r"pre-family-clean generation",
    r"stay open in D2",
    r"are D2-owned",
    r"was superseded",
    r"superseded for D4 ownership",
)

PROBES = [
    {
        "claim": "D4-CL05",
        "asserts": "findings_total",
        "live_surface": "typed-labels.d4.yml#coverage.findings_total",
        "stale_pattern": r"findings_total 16",
        "live_pattern": r"findings_total 12",
    },
    {
        "claim": "D4-CL05",
        "asserts": "findings_hold_or_fail",
        "live_surface": "typed-labels.d4.yml#coverage.findings_hold_or_fail",
        "stale_pattern": r"findings_hold_or_fail 15",
        "live_pattern": r"findings_hold_or_fail 12",
    },
    {
        "claim": "D4-CL06",
        "asserts": "counts.hold",
        "live_surface": "expected-holds.json#counts.hold",
        "stale_pattern": r"counts \(hold 15,",
        "live_pattern": r"counts \(hold 12,",
    },
    {
        "claim": "D4-CL06",
        "asserts": "counts.note",
        "live_surface": "expected-holds.json#counts.note",
        "stale_pattern": r"counts \(hold 15, note 1,",
        "live_pattern": r"counts \(hold 12, note 0,",
    },
    {
        "claim": "D4-CL07",
        "asserts": "coverage.conflicts",
        "live_surface": "typed-labels.d4.yml#coverage.conflicts",
        "stale_pattern": r"conflicts \(4\)",
        "live_pattern": r"zero conflicts",
    },
    {
        "claim": "D4-CL09",
        "asserts": "coverage.rank_rules_unresolved_items",
        "live_surface": "typed-labels.d4.yml#coverage.rank_rules_unresolved_items",
        "stale_pattern": r"rank_rules_unresolved_items 13",
        "live_pattern": r"zero unresolved rank items",
    },
    {
        "claim": "D4-CL09",
        "asserts": "coverage.rank_quarantine_handles",
        "live_surface": "typed-labels.d4.yml#coverage.rank_quarantine_handles",
        "stale_pattern": r"rank_quarantine_handles 3",
        "live_pattern": r"zero quarantine handles",
    },
    {
        "claim": OQ_ID,
        "asserts": "open-question rank passengers",
        "live_surface": "typed-labels.d4.yml#coverage.rank_rules_unresolved_items",
        "stale_pattern": r"twelve form holds \+ three rank holds \+ one note",
        "live_pattern": r"twelve form holds, zero rank holds, zero notes",
    },
]


def sha256_file(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def load_json(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def live_state():
    """R25-X48-1: the numbers the live D4 surfaces carry."""
    projection = load_json(PROJECTION)
    expected = load_json(EXPECTED)
    coverage = projection.get("coverage") or {}
    return {
        "coverage": coverage,
        "counts": expected.get("counts") or {},
        "has_stats_block": "stats" in projection,
        "digests": {
            "typed-labels.d4.yml": sha256_file(PROJECTION),
            "expected-holds.json": sha256_file(EXPECTED),
        },
    }


def row_text(path, claim_id):
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("| %s |" % claim_id) or line.startswith("- %s:" % claim_id):
                return line.rstrip("\n")
    return None


def classify_row(text, claim_id):
    """Supersession-aware classification of one claim row.

    Only the probes belonging to *this* claim row are applied — a probe for
    D4-CL06 must never be evaluated against the D4-CL09 row.
    """
    if text is None:
        return {"present": False, "entries": []}
    marked_removed = [marker for marker in REMOVED_MARKERS if re.search(marker, text)]
    entries = []
    for probe in PROBES:
        if probe["claim"] != claim_id:
            continue
        asserts_stale = bool(re.search(probe["stale_pattern"], text))
        asserts_live = bool(re.search(probe["live_pattern"], text))
        supersession_marked = bool(marked_removed)
        stale = asserts_stale and not supersession_marked
        corrected = asserts_live or (asserts_stale and supersession_marked)
        entries.append({
            "claim": probe["claim"],
            "asserts": probe["asserts"],
            "asserts_stale_value": asserts_stale,
            "asserts_live_value": asserts_live,
            "supersession_marked": supersession_marked,
            "stale": stale,
            "corrected": corrected,
            "live_surface": probe["live_surface"],
        })
    return {"present": True, "marked_removed": marked_removed, "entries": entries}


def census(state):
    """R25-X48-2: supersession-aware per-revision census."""
    rows = []
    for label, rel in REVISIONS:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            rows.append({"revision": label, "path": rel, "present": False})
            continue
        by_claim = {}
        for claim in CLAIM_IDS + (OQ_ID,):
            by_claim[claim] = classify_row(row_text(path, claim), claim)
        stale = sum(1 for c in by_claim.values()
                    for e in c["entries"] if e["stale"])
        rows.append({
            "revision": label,
            "path": rel,
            "present": True,
            "sha256": sha256_file(path),
            "stale_assertions": stale,
            "claims": by_claim,
        })
    return rows


def supersession_chain(rows):
    """R25-X48-3: which revision first corrects each stale claim."""
    chain = []
    for row in rows:
        if not row.get("present"):
            chain.append({"revision": row["revision"], "present": False})
            continue
        per_claim = {}
        for claim, info in row["claims"].items():
            if not info["present"]:
                per_claim[claim] = "absent"
                continue
            stale = any(e["stale"] for e in info["entries"])
            corrected = all(e["corrected"] for e in info["entries"] if e["asserts_stale_value"]
                            or e["asserts_live_value"] or e["supersession_marked"])
            per_claim[claim] = "stale" if stale else ("corrected" if corrected else "indeterminate")
        chain.append({
            "revision": row["revision"],
            "sha256": row["sha256"],
            "per_claim": per_claim,
            "fully_corrected": all(v in ("corrected",) for v in per_claim.values()),
            "any_stale": any(v == "stale" for v in per_claim.values()),
        })
    return chain


def first_correction(chain):
    """The first revision (in order) where no claim row is stale."""
    for row in chain:
        if row.get("present", True) and not row.get("any_stale"):
            return row["revision"]
    return None


def selftest():
    """In-memory controls; the repo is read only for the live-state control."""
    checks = []
    checks.append(("probe-count", len(PROBES) == 8))
    checks.append(("claim-ids-covered",
                   set(p["claim"] for p in PROBES) == set(CLAIM_IDS) | {OQ_ID}))
    checks.append(("every-probe-has-live-surface",
                   all(p["live_surface"] for p in PROBES)))
    checks.append(("every-probe-has-both-patterns",
                   all(p["stale_pattern"] and p["live_pattern"] for p in PROBES)))

    # A stale row is read stale.
    stale_row = ("| D4-CL06 | designer interpretation | derived projection (author-side) | "
                 "supported | grounding: examples/culture-d4/expected-holds.json#counts "
                 "(hold 15, note 1, fail 0) with the row list")
    classified = classify_row(stale_row, "D4-CL06")
    checks.append(("stale-row-read-stale",
                   any(e["stale"] for e in classified["entries"])))

    # A row that asserts the live value is corrected, not stale.
    live_row = ("| D4-CL06 | designer interpretation | derived projection (author-side) | "
                "supported | grounding: examples/culture-d4/expected-holds.json#counts "
                "(hold 12, note 0, fail 0) with the row list")
    classified = classify_row(live_row, "D4-CL06")
    checks.append(("live-row-not-stale",
                   not any(e["stale"] for e in classified["entries"])
                   and any(e["asserts_live_value"] for e in classified["entries"])))

    # The load-bearing control: a row that *names* the old numbers as removed is
    # corrected, never stale — this is what the r4 successor does.
    superseded_row = ("| D4-CL09 | designer interpretation | derived projection (author-side), "
                      "holds open | unresolved | grounding: ... zero unresolved rank items ...; "
                      "open: the thirteen unresolved rank items, three quarantine handles and "
                      "four conflicts the pre-family-clean generation inherited are no longer "
                      "D4-owned and were not resolved in D2")
    classified = classify_row(superseded_row, "D4-CL09")
    checks.append(("removed-naming-row-not-stale",
                   not any(e["stale"] for e in classified["entries"])
                   and classified["marked_removed"]))

    # Negative control on the supersession detector itself: a bare stale row
    # carries no removal marker, so the marker cannot be doing blanket work.
    classified = classify_row(stale_row, "D4-CL06")
    checks.append(("stale-row-has-no-removal-marker",
                   not classified["marked_removed"]))

    # Scope control: a D4-CL06 probe must not be applied to a D4-CL09 row.
    classified = classify_row(superseded_row, "D4-CL09")
    checks.append(("probe-scoped-to-its-own-claim",
                   all(e["claim"] == "D4-CL09" for e in classified["entries"])
                   and len(classified["entries"]) == 2))

    # Live-state controls: the current bytes carry the post-fix numbers.
    state = live_state()
    checks.append(("live-hold-is-12", state["counts"].get("hold") == 12))
    checks.append(("live-note-is-0", state["counts"].get("note") == 0))
    checks.append(("live-conflicts-is-0", state["coverage"].get("conflicts") == 0))
    checks.append(("live-unresolved-is-0",
                   state["coverage"].get("rank_rules_unresolved_items") == 0))
    checks.append(("live-findings-total-is-12",
                   state["coverage"].get("findings_total") == 12))

    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print("%-38s %s" % (name, "ok" if ok else "FAIL"))
    print("selftest: %d/%d controls" % (len(checks) - len(failed), len(checks)))
    return 1 if failed else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        return selftest()

    state = live_state()
    rows = census(state)
    chain = supersession_chain(rows)
    oq_rows = {r["revision"]: r for r in rows if r.get("present")}
    result = {
        "seat": "R25-X48",
        "date": "2026-10-18",
        "axis": "O / v3 supersession prose",
        "R25-X48-1_live_state": {
            "counts": state["counts"],
            "coverage_subset": {k: state["coverage"].get(k) for k in (
                "typed_labels", "labels_by_kind", "findings_total",
                "findings_hold_or_fail", "label_findings_fail", "conflicts",
                "rank_rules_unresolved_items", "rank_quarantine_handles",
                "reconciliation_records")},
            "has_stats_block": state["has_stats_block"],
            "digests": state["digests"],
        },
        "R25-X48-2_census": [
            {"revision": r["revision"], "present": r["present"],
             "sha256": r.get("sha256"), "stale_assertions": r.get("stale_assertions")}
            for r in rows],
        "R25-X48-3_supersession_chain": chain,
        "R25-X48-4_passenger_disposition": {
            "oq_id": OQ_ID,
            "first_fully_corrected_revision": first_correction(chain),
            "oq_still_stale_in": [
                r["revision"] for r in rows if r.get("present")
                and r["claims"][OQ_ID]["present"]
                and any(e["stale"] for e in r["claims"][OQ_ID]["entries"])],
        },
    }
    if args.json:
        print(json.dumps(result, indent=1, ensure_ascii=False))
    else:
        print("X48 v3 supersession prose-diff audit — 2026-10-18")
        print("  live: counts=%s findings_total=%s conflicts=%s unresolved=%s"
              % (state["counts"], state["coverage"].get("findings_total"),
                 state["coverage"].get("conflicts"),
                 state["coverage"].get("rank_rules_unresolved_items")))
        for row in rows:
            if row.get("present"):
                print("  %-22s stale assertions: %d" % (row["revision"], row["stale_assertions"]))
        for row in chain:
            if row.get("present"):
                print("  %-22s fully_corrected=%s per_claim=%s"
                      % (row["revision"], row["fully_corrected"], row["per_claim"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
