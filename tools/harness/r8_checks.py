#!/usr/bin/env python3
"""Round-8 O02 fix: parent-check receipt identity semantics for the round-7
claim-F parent leg, implemented as new code (the filed round-7 runner is never
edited or imported on the fixed path).

Defect fixed (reports/round-7/validation.json, claim F):
    "wrong rejection for duplicate-parent-receipt-does-not-inflate:
     parent check identity collision"

The round-7 runner (reports/round-7/run-validation.py:314-315) rejected any
repeated check id outright, before the distinct-passage rule could speak. That
made two shapes indistinguishable:

  * genuine identity collision -- one check label bound to two receipts with
    different binding-relevant fields (ambiguous: the label no longer names
    one receipt); must be rejected;
  * benign duplicate receipt -- repeated labels whose members share one receipt
    identity (a retry / re-recording, prose fields may differ); must be
    deduplicated, never treated as a collision, and must not inflate the
    distinct-passage count that the "fewer than two distinct parent passage
    receipts" rule guards.

Corrected semantics (R8-O01 diagnosis reports/round-8/operability/o01-diagnosis.md
section 4, rules S1-S7): group checks by label; within a group, receipt identity
R = (row_id, normalized source_url, source_kind, normalized locator, normalized
excerpt) -- binding-relevant fields only, prose fields never enter R; more than
one distinct R in a group rejects "parent check identity collision: <label>"
(S1), one R deduplicates to the first member (S2), counting keeps set semantics
(S3), per-check binding checks run over the deduplicated representatives (S4),
label groups iterate in sorted order (S5), and the positive measurement must not
drift (S6). Identity normalization reuses this module's passage-key
normalization, so identity and counting cannot drift apart.

Modes (read-only over repository inputs; stdout receipts only, no file writes):
    --selftest   regression controls: real round-7 inputs accepted; benign
                 duplicate accepted (not mis-diagnosed, no inflation);
                 genuine collision still rejected; fail-before demonstrated
                 against the round-7 implementation; malformed inputs fail
                 closed without tracebacks. Exit 0 all-pass, 1 any-fail.
    --measure    corrected measurement over the real round-7 parent inputs.

Stdlib only. Constants FIXED_IDS and CONSERVATIVE_MIX mirror the round-7
contract (reports/round-7/run-validation.py:84-85) and are re-asserted against
reports/round-7/targets.json."""

import argparse
import collections
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import unicodedata
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[2]
R7 = ROOT / "reports/round-7"
RECONCILIATION_REL = "reports/round-7/parent-reconciliation.json"
SPOTCHECKS_REL = "reports/round-7/parent-source-spotchecks.json"
TARGETS_REL = "reports/round-7/targets.json"
BASELINE_REL = "reports/round-7/baseline.json"
LEDGER_DIR_REL = "corpus/lessons/round-7-sources"
FIXED_IDS = [f"R7-F{i:02d}" for i in range(1, 6)]
CONSERVATIVE_MIX = {"scoped-support": 3, "partial-support": 2}
TOOL = "tools/harness/r8_checks.py"
ROUND7_RUNNER_REL = "reports/round-7/run-validation.py"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def file_sha(relative):
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


def url(value, what="url"):
    require(isinstance(value, str) and not any(c.isspace() for c in value),
            f"not a single URL: {what}")
    parts = urlsplit(value)
    require(parts.scheme in {"http", "https"} and parts.hostname
            and not parts.username and not parts.password,
            f"not a public HTTP(S) source URL: {what}")
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(),
                       parts.path.rstrip("/"), parts.query, parts.fragment))


def text(value, what):
    require(isinstance(value, str) and value.strip(), f"empty or non-text {what}")
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def excerpt_of(value, what):
    require(isinstance(value, str), f"non-string excerpt: {what}")
    require(len(value.split()) <= 40, f"excerpt over 40 whitespace tokens: {what}")
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def passage_key(source_url, locator, quotation, what):
    return (url(source_url, what), text(locator, what + " locator"),
            excerpt_of(quotation, what))


def receipt_identity(check):
    """R8-O01 S1: binding-relevant fields only -- (row_id, normalized
    source_url, source_kind, normalized locator, normalized excerpt). Prose
    fields (basis, limits, accessed_at, retrieval_method,
    language_and_mediation, excerpt_form, citation) never enter identity."""
    label = check.get("id") if isinstance(check.get("id"), str) else "check"
    return (check.get("row_id"),
            url(check.get("source_url"), label),
            check.get("source_kind"),
            text(check.get("locator"), label + " locator"),
            excerpt_of(check.get("excerpt"), label + " excerpt"))


# --------------------------------------------------------------------------
# corrected parent-check measurement
# --------------------------------------------------------------------------

def measure_parent_receipts(reconciliation, spotchecks, targets, ledgers):
    """Round-7 parent semantics (rows, dispositions, URL/kind binding,
    receipt fields, distinctness) with corrected check-identity handling."""
    require(reconciliation["round"] == spotchecks["round"] == 7,
            "wrong parent round")
    require(reconciliation["baseline_revision"]
            == spotchecks["baseline_revision"] == ledgers_base(),
            "wrong parent baseline")
    rows = reconciliation["rows"]
    require(len(rows) == len({row["id"] for row in rows}) == 5,
            "reconciliation must bind exactly the five fixed target ids")
    dispositions = collections.Counter()
    for row in rows:
        what = row["id"]
        require(what in FIXED_IDS, f"reconciliation row is not a fixed id: {what}")
        target = targets[target_assignment(what, targets)]
        require(row["disposition"] in CONSERVATIVE_MIX,
                f"disposition outside the conservative pair: {what}")
        dispositions[row["disposition"]] += 1
        for flag in ("main_passage_eligible", "directly_relevant"):
            require(isinstance(row[flag], bool), f"non-boolean parent flag: {what}")
        text(row["basis"], what + " parent basis")
        text(row["limits"], what + " parent limits")
        kind = row.get("effective_source_kind", target["source_kind"])
        require(kind == target["source_kind"],
                f"unrecorded effective kind override: {what}")
        effective_url = row.get("effective_source_url", target["source_url"])
        require(url(effective_url, what) == url(target["source_url"], what),
                f"unrecorded effective URL override: {what}")
        document = ledgers[what]
        if row["main_passage_eligible"]:
            require(document["retrieved_passage"]
                    and document["directly_relevant_nonbibliographic"],
                    f"ineligible ledger row promoted: {what}")
    require(dict(dispositions) == CONSERVATIVE_MIX,
            "parent dispositions must stay conservative 3 scoped + 2 partial: "
            f"{dict(dispositions)}")

    checks = spotchecks["checks"]
    require(isinstance(checks, list), "parent checks must be a list")
    for check in checks:
        require(isinstance(check, dict), "parent check must be an object")
        require(isinstance(check.get("id"), str) and check["id"].strip(),
                "parent check missing id")

    groups = {}
    for check in checks:
        groups.setdefault(check["id"], []).append(check)
    unique_checks = []
    benign_duplicates = 0
    for label in sorted(groups):
        group = groups[label]
        identities = {receipt_identity(check) for check in group}
        if len(identities) > 1:
            raise ValueError(f"parent check identity collision: {label}")
        unique_checks.append(group[0])
        benign_duplicates += len(group) - 1

    parent_keys = set()
    parent_urls = set()
    for check in unique_checks:
        what = check["id"]
        require(check.get("row_id") in FIXED_IDS,
                f"parent check is not bound to a fixed id: {what}")
        require(check.get("result") == "success"
                and check.get("retrieved_passage") is True
                and check.get("directly_relevant_nonbibliographic") is True,
                f"unsuccessful/non-content parent check: {what}")
        document = ledgers[check["row_id"]]
        require(url(check.get("source_url"), what) == url(document["source_url"], what),
                f"parent URL does not match the bound ledger row: {what}")
        require(check.get("source_kind") == document["source_kind"],
                f"parent kind mismatch: {what}")
        for field in ("accessed_at", "retrieval_method", "basis", "locator",
                      "language_and_mediation", "limits", "excerpt_form"):
            text(check.get(field), what + " " + field)
        key = passage_key(check["source_url"], check["locator"],
                          check["excerpt"], what)
        parent_keys.add(key)
        parent_urls.add(key[0])
    require(len(parent_keys) >= 2,
            f"fewer than two distinct parent passage receipts: {len(parent_keys)}")
    require(len(parent_urls) >= 2,
            f"fewer than two distinct bound parent refetch URLs: {len(parent_urls)}")
    return {"reconciliation_rows": len(rows),
            "parent_dispositions": dict(dispositions),
            "parent_checks_raw": len(checks),
            "parent_checks_unique": len(unique_checks),
            "parent_benign_duplicate_receipts": benign_duplicates,
            "parent_distinct_passage_keys": len(parent_keys),
            "parent_distinct_refetch_urls": len(parent_urls),
            "semantics": "same label + one receipt identity R = (row_id, "
                         "normalized source_url, source_kind, normalized "
                         "locator, normalized excerpt) = benign duplicate "
                         "(deduplicated, counted once); same label + >1 "
                         "distinct R = identity collision (rejected, label "
                         "named); prose fields never enter R"}


def ledgers_base():
    return load(BASELINE_REL)["baseline_revision"]


def targets_by_assignment():
    raw = load(TARGETS_REL)["targets"]
    require(len(raw) == 5 and len({t["assignment"] for t in raw}) == 5,
            "targets must carry five fixed assignments")
    require(sorted(t["id"] for t in raw) == FIXED_IDS,
            "round-7 fixed ids drifted from the five R7-F ids")
    return {target["assignment"]: target for target in raw}


def target_assignment(row_id, targets):
    for assignment, target in targets.items():
        if target["id"] == row_id:
            return assignment
    raise ValueError(f"unknown fixed id: {row_id}")


def round7_bundle():
    targets = targets_by_assignment()
    ledgers = {}
    for assignment, target in sorted(targets.items()):
        path = ROOT / LEDGER_DIR_REL / f"{assignment}.json"
        ledgers[target["id"]] = json.loads(path.read_text(encoding="utf-8"))
    return {"reconciliation": load(RECONCILIATION_REL),
            "spotchecks": load(SPOTCHECKS_REL),
            "targets": targets, "ledgers": ledgers}


def round7_input_hashes():
    relatives = [RECONCILIATION_REL, SPOTCHECKS_REL, TARGETS_REL, BASELINE_REL]
    relatives += [f"{LEDGER_DIR_REL}/{i:02d}.json" for i in range(8, 13)]
    return {relative: file_sha(relative) for relative in relatives}


def measure_real_inputs():
    bundle = round7_bundle()
    return measure_parent_receipts(bundle["reconciliation"], bundle["spotchecks"],
                                   bundle["targets"], bundle["ledgers"])


# --------------------------------------------------------------------------
# fail-before reference: the filed round-7 implementation, imported read-only
# --------------------------------------------------------------------------

def round7_module():
    spec = importlib.util.spec_from_file_location(
        "kotodama_round7_runner", ROOT / ROUND7_RUNNER_REL)
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


def round7_measure(spotchecks):
    module = round7_module()
    bundle = round7_bundle()
    module.measure_f_parents(bundle["reconciliation"], spotchecks,
                             bundle["targets"], bundle["ledgers"])


# --------------------------------------------------------------------------
# regression controls
# --------------------------------------------------------------------------

def _verbatim_duplicate_set(spotchecks):
    altered = copy.deepcopy(spotchecks)
    altered["checks"] = [copy.deepcopy(spotchecks["checks"][0]),
                         copy.deepcopy(spotchecks["checks"][0])]
    return altered


def _benign_duplicate_added(spotchecks):
    altered = copy.deepcopy(spotchecks)
    altered["checks"] = altered["checks"] + [copy.deepcopy(altered["checks"][0])]
    return altered


def _reid_clone(check, new_id):
    clone = copy.deepcopy(check)
    clone["id"] = new_id
    return clone


def guard_fired(message):
    if message.startswith("parent check identity collision"):
        return "S1-identity-collision"
    if message.startswith("fewer than two distinct"):
        return "S3-counting"
    if message.startswith("unsuccessful/non-content parent check"):
        return "S4-binding"
    if (message.startswith(("parent checks must be a list",
                            "parent check must be an object",
                            "parent check missing id"))
            or "not a single URL" in message
            or message.startswith(("empty or non-text", "non-string excerpt",
                                   "excerpt over 40 whitespace tokens"))):
        return "malformed-input"
    return "other-guard"


def run_controls():
    bundle = round7_bundle()
    spotchecks = bundle["spotchecks"]
    controls = []

    def observe(name, expectation, call, expected_substring,
                forbidden_substring=None, guard=None):
        def record(message, passed):
            controls.append({
                "control": name, "guard": guard, "expectation": expectation,
                "observed": message,
                "guard_fired": (None if message.startswith("accepted:")
                                else guard_fired(message)),
                "passed": passed})

        try:
            result = call()
        except (ValueError, KeyError, TypeError) as error:
            message = str(error)
            passed = (expected_substring in message
                      and (forbidden_substring is None
                           or forbidden_substring not in message))
            record(message, passed)
            return
        record(f"accepted: {json.dumps(result, sort_keys=True)}",
               expected_substring is None)

    # 1. real round-7 inputs are accepted by the corrected semantics (S6)
    def real_inputs():
        measurement = measure_real_inputs()
        require(measurement["parent_distinct_passage_keys"] == 2
                and measurement["parent_distinct_refetch_urls"] == 2
                and measurement["parent_checks_raw"] == 2
                and measurement["parent_dispositions"] == CONSERVATIVE_MIX
                and measurement["parent_benign_duplicate_receipts"] == 0,
                f"unexpected real-input measurement: {measurement}")
        return measurement

    observe("real-inputs-accepted", "positive: real round-7 parent inputs pass",
            real_inputs, None, guard="S6-no-drift")

    # 2. fail-before: round-7 implementation mis-rejects the verbatim duplicate
    observe("fail-before-round7-verbatim-duplicate",
            "round-7 runner rejects a benign duplicate with the collision "
            "diagnostic (the filed defect)",
            lambda: round7_measure(_verbatim_duplicate_set(spotchecks)),
            "parent check identity collision", guard="S1-identity-collision")

    # 3. pass-after: corrected semantics catch the same mutation by distinctness
    observe("benign-duplicate-not-misdiagnosed",
            "same mutation now rejected as fewer than two distinct parent "
            "passage receipts, never as an identity collision",
            lambda: measure_parent_receipts(
                bundle["reconciliation"], _verbatim_duplicate_set(spotchecks),
                bundle["targets"], bundle["ledgers"]),
            "fewer than two distinct parent passage receipts",
            forbidden_substring="identity collision", guard="S3-counting")

    # 4. benign duplicate accepted when the valid set is otherwise intact
    def benign_accepted():
        measurement = measure_parent_receipts(
            bundle["reconciliation"], _benign_duplicate_added(spotchecks),
            bundle["targets"], bundle["ledgers"])
        require(measurement["parent_benign_duplicate_receipts"] == 1
                and measurement["parent_checks_raw"] == 3
                and measurement["parent_checks_unique"] == 2
                and measurement["parent_distinct_passage_keys"] == 2,
                f"benign duplicate altered the measurement: {measurement}")
        return measurement

    observe("benign-duplicate-receipt-accepted",
            "benign duplicate accepted, deduplicated and not counted as distinct",
            benign_accepted, None, guard="S2-dedupe")

    # 5. fail-before: round-7 implementation also mis-rejects that valid set
    observe("fail-before-round7-benign-duplicate-valid-set",
            "round-7 runner rejects the otherwise valid set containing a "
            "benign duplicate (filed defect, sharpest form)",
            lambda: round7_measure(_benign_duplicate_added(spotchecks)),
            "parent check identity collision", guard="S1-identity-collision")

    # 6. S7 required control: genuine collision on a binding-relevant field
    def collision_excerpt():
        altered = copy.deepcopy(spotchecks)
        second = copy.deepcopy(altered["checks"][0])
        second["excerpt"] = second["excerpt"] + " [divergent re-fetch]"
        altered["checks"] = [altered["checks"][0], second]
        return altered

    observe("genuine-parent-check-identity-collision",
            "same label, one binding-relevant field (excerpt) changed: still "
            "rejected with the label named",
            lambda: measure_parent_receipts(
                bundle["reconciliation"], collision_excerpt(),
                bundle["targets"], bundle["ledgers"]),
            "parent check identity collision: P01", guard="S1-identity-collision")

    # 7. genuine collision: same label, differing URL
    def collision_url():
        altered = copy.deepcopy(spotchecks)
        second = copy.deepcopy(altered["checks"][0])
        second["source_url"] = "https://example.org/divergent-refetch"
        altered["checks"] = [altered["checks"][0], second]
        return altered

    observe("genuine-collision-differing-url",
            "same label bound to a different bound URL still rejected",
            lambda: measure_parent_receipts(
                bundle["reconciliation"], collision_url(),
                bundle["targets"], bundle["ledgers"]),
            "parent check identity collision: P01", guard="S1-identity-collision")

    # 8. mixed group: verbatim duplicate plus one divergent receipt
    def collision_mixed():
        altered = copy.deepcopy(spotchecks)
        first = altered["checks"][0]
        divergent = copy.deepcopy(first)
        divergent["excerpt"] = divergent["excerpt"] + " [divergent re-fetch]"
        altered["checks"] = [first, copy.deepcopy(first), divergent]
        return altered

    observe("genuine-collision-mixed-group",
            "a mixed group (duplicate + divergent receipt) still rejected",
            lambda: measure_parent_receipts(
                bundle["reconciliation"], collision_mixed(),
                bundle["targets"], bundle["ledgers"]),
            "parent check identity collision: P01", guard="S1-identity-collision")

    # 9. non-binding prose differences must not be a collision (S1/S2)
    def nonbinding_prose():
        altered = copy.deepcopy(spotchecks)
        second = copy.deepcopy(altered["checks"][0])
        second["basis"] = second["basis"] + " Reworded basis prose."
        second["limits"] = second["limits"] + " Reworded limits prose."
        second["accessed_at"] = "2026-10-17"
        altered["checks"] = altered["checks"] + [second]
        measurement = measure_parent_receipts(
            bundle["reconciliation"], altered, bundle["targets"],
            bundle["ledgers"])
        require(measurement["parent_benign_duplicate_receipts"] == 1
                and measurement["parent_checks_unique"] == 2
                and measurement["parent_distinct_passage_keys"] == 2,
                f"prose-only difference changed the measurement: {measurement}")
        return measurement

    observe("nonbinding-prose-difference-is-benign",
            "same label, same receipt identity, reworded prose: benign "
            "duplicate, not a collision",
            nonbinding_prose, None, guard="S2-dedupe")

    # 10. the exact filed control mutation now yields the expected diagnostic
    def round7_control_shape():
        altered = copy.deepcopy(spotchecks)
        clone = _reid_clone(altered["checks"][0], "PX99")
        altered["checks"] = [clone, copy.deepcopy(clone)]
        return altered

    observe("duplicate-parent-receipt-does-not-inflate",
            "the filed control mutation reaches the distinctness diagnostic "
            "it declares (S7, kept control)",
            lambda: measure_parent_receipts(
                bundle["reconciliation"], round7_control_shape(),
                bundle["targets"], bundle["ledgers"]),
            "fewer than two distinct parent passage receipts",
            forbidden_substring="identity collision", guard="S3-counting")

    # 11. re-ided duplicates cannot inflate the distinct count
    def reid_duplicates():
        altered = copy.deepcopy(spotchecks)
        first = altered["checks"][0]
        altered["checks"] = [_reid_clone(first, "PX98"), _reid_clone(first, "PX99")]
        return altered

    observe("re-ided-duplicates-do-not-inflate",
            "duplicate passages under fresh labels are deduplicated by "
            "passage key",
            lambda: measure_parent_receipts(
                bundle["reconciliation"], reid_duplicates(),
                bundle["targets"], bundle["ledgers"]),
            "fewer than two distinct parent passage receipts", guard="S3-counting")

    # 11. malformed inputs fail closed with a clean message
    def malformed_checks():
        altered = copy.deepcopy(spotchecks)
        altered["checks"] = "P01"
        return altered

    observe("malformed-checks-not-a-list",
            "non-list checks fail closed without a traceback",
            lambda: measure_parent_receipts(
                bundle["reconciliation"], malformed_checks(),
                bundle["targets"], bundle["ledgers"]),
            "parent checks must be a list", guard="malformed-input")

    def malformed_missing_id():
        altered = copy.deepcopy(spotchecks)
        broken = copy.deepcopy(altered["checks"][0])
        broken.pop("id")
        altered["checks"] = [broken, copy.deepcopy(altered["checks"][1])]
        return altered

    observe("malformed-check-missing-id",
            "a check without an id fails closed without a traceback",
            lambda: measure_parent_receipts(
                bundle["reconciliation"], malformed_missing_id(),
                bundle["targets"], bundle["ledgers"]),
            "parent check missing id", guard="malformed-input")

    def malformed_missing_url():
        altered = copy.deepcopy(spotchecks)
        broken = copy.deepcopy(altered["checks"][0])
        broken.pop("source_url")
        altered["checks"] = [broken, copy.deepcopy(altered["checks"][1])]
        return altered

    observe("malformed-check-missing-url",
            "a check without a source_url fails closed without a traceback",
            lambda: measure_parent_receipts(
                bundle["reconciliation"], malformed_missing_url(),
                bundle["targets"], bundle["ledgers"]),
            "not a single URL", guard="malformed-input")

    return controls


def selftest_receipt():
    controls = run_controls()
    passed = sum(1 for control in controls if control["passed"])
    return {"tool": TOOL,
            "tool_sha256": file_sha(TOOL),
            "round": 8,
            "defect": "reports/round-7/validation.json F: wrong rejection for "
                      "duplicate-parent-receipt-does-not-inflate: parent check "
                      "identity collision",
            "input_sha256": round7_input_hashes(),
            "controls": controls,
            "controls_passed": passed,
            "controls_total": len(controls),
            "selftest_passed": passed == len(controls),
            "limits": [
                "This harness re-measures the parent-check identity leg of "
                "round-7 claim F; it does not re-run the round-7 runner and "
                "writes no files.",
                "The fail-before controls execute the filed round-7 "
                "implementation read-only (imported, never edited).",
                "Receipt/identity semantics only: not quotation truth, not "
                "historical authenticity, not promotion."]}


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog=TOOL, description="Round-8 O02 parent-check identity fix harness")
    parser.add_argument("--selftest", action="store_true",
                        help="run the regression controls (exit 0 all-pass)")
    parser.add_argument("--measure", action="store_true",
                        help="corrected measurement over the real round-7 inputs")
    args = parser.parse_args(argv)
    if args.selftest and args.measure:
        parser.error("choose one of --selftest / --measure")
    try:
        if args.selftest:
            receipt = selftest_receipt()
            print(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True))
            return 0 if receipt["selftest_passed"] else 1
        if args.measure:
            print(json.dumps(measure_real_inputs(), ensure_ascii=False,
                             indent=2, sort_keys=True))
            return 0
    except ValueError as error:
        print(json.dumps({"tool": TOOL, "error": str(error)},
                         ensure_ascii=False, sort_keys=True))
        return 1
    parser.print_usage(sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
