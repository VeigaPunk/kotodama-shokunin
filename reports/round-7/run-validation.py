#!/usr/bin/env python3
"""Round-7 local acceptance runner: measures claims F and O against the
declared contract, plus dispatch binding, preservation, inventory and the
previous round's acceptance on delivered old surfaces.

Run:  python3 reports/round-7/run-validation.py

Writes ONLY reports/round-7/validation.json in this repository (plus
disposable scratch in a system temporary directory whose absolute paths are
never recorded). The receipt is deterministic: sorted keys, no wall-clock
timestamps, no scratch paths. Missing parent inputs (expected.json,
parent reconciliation, parent spot-checks, native request binding) are
reported as failing dependencies — never synthesized, never self-blessed.

Claim F (freshness): the five fixed round-7 source ledgers 08..12 must bind
exactly to targets.json (fixed ids/questions/entries/URLs/kinds/previous
ids), carry the full required schema with real booleans, baseline and date,
an explicit result and limits, a main excerpt of at most 40 whitespace
tokens, deduplicated URL+NFKC-normalized locator/excerpt passages, at least
three distinct substantive non-bibliographic main passages across at least
three entries, a parent reconciliation binding exactly the fixed ids with a
conservative 3 scoped-support + 2 partial-support mix, and at least two
distinct bound successful parent URL re-fetch receipts. Only the
source_excerpt field counts as a passage; basis/limits prose and
bibliography never count.

Claim O (operability): the real CLIs — assembler --check/--selftest, the
evidence-coupling guard positive/--frozen/--selftest, the legacy naming and
costume gates, the handoff gate and the README — are executed as
subprocesses. The runner applies controls.json JSON-pointer patches with its
own independent implementation through the real guard CLI (the guard's patch
helper is not imported and expected diagnostics are never derived from it),
demands at least twelve distinct stable-id exit-1 negatives, at least four
exit-2 malformed controls without tracebacks, clean positives, private-copy
frozen digest tamper and traversal/absolute/unknown manifest rejects, and
proves guard foreign-cwd runs write no inputs (bytes + mtime_ns).

Stdlib only; read-only over repository inputs."""

import collections
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "reports/round-7"
ASSEMBLER = "tools/assemble-culture-d3.py"
GUARD = "tools/check-evidence-coupling.py"
PACKET_REL = "examples/culture-d3/packet.json"
LEGACY_REL = "examples/culture-d3/packet.gates.yml"
CONTROLS_REL = "examples/culture-d3/controls.json"
HANDOFF_REL = "examples/culture-d3/handoff.md"
README_REL = "examples/culture-d3/README.md"
COMPONENT_RELS = [f"examples/culture-d3/components/{name}"
                  for name in ("04-language.json", "05-ritual.json",
                               "06-material.json", "07-evidence.json")]
CLOSED_LEDGERS = ["corpus/lessons/round-6-sources/05.json",
                  "corpus/lessons/round-6-sources/03.json",
                  "corpus/lessons/round-6-sources/13.json",
                  "corpus/lessons/round-6-sources/09.json"]
WORLDBIBLE_CONTRACT = "corpus/knowledge/synthesis/worldbible-integration-contract.md"
NAMING_GATE = ROOT / "tools/gates/naming-collision-gate.py"
COSTUME_GATE = ROOT / "tools/gates/costume-era-consistency-gate.py"
HANDOFF_GATE = ROOT / "tools/gates/handoff-packet-check.py"
INVENTORY_TOOL = "tools/source-audit-inventory.py"
APPEND_ONLY = {"LOG.md", "SKILL.md"}
EDITABLE = {"SCORECARD.md", "corpus/README.md"}
NEW_EXACT = {ASSEMBLER, GUARD, "corpus/lessons/round-7.md"}
NEW_PREFIXES = ("reports/round-7/", "examples/culture-d3/",
                "corpus/lessons/round-7-sources/")
INVENTORY_TOTALS = {"files": 179, "raw_lines": 592, "raw_occurrences": 598,
                    "ci_occurrences": 600, "marker_occurrences": 568}
PROFILE = "kotodama-d3-evidence-coupling/1"
PACKET_NAME = "D3 source-bounded culture drill (NON-CANON)"
FIXED_IDS = [f"R7-F{i:02d}" for i in range(1, 6)]
CONSERVATIVE_MIX = {"scoped-support": 3, "partial-support": 2}
ROUND6_RECONCILIATION = "reports/round-6/parent-reconciliation.json"
REQUIRED_MANIFEST = sorted(
    [PACKET_REL, CONTROLS_REL, "reports/round-7/d3-contract.json",
     "reports/round-7/targets.json", "reports/round-7/baseline.json",
     ASSEMBLER, GUARD, ROUND6_RECONCILIATION,
     WORLDBIBLE_CONTRACT] + COMPONENT_RELS + CLOSED_LEDGERS)
HANDOFF_FIELDS_16 = 16
NAMING_ARGV = [sys.executable, "tools/gates/naming-collision-gate.py", LEGACY_REL]
COSTUME_ARGV = [sys.executable, "tools/gates/costume-era-consistency-gate.py", LEGACY_REL]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(relative):
    return sha((ROOT / relative).read_bytes())


def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def text(value, what):
    require(isinstance(value, str) and value.strip(), f"empty or non-text {what}")
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def url(value, what="url"):
    require(isinstance(value, str) and not any(c.isspace() for c in value),
            f"not a single URL: {what}")
    parts = urlsplit(value)
    require(parts.scheme in {"http", "https"} and parts.hostname
            and not parts.username and not parts.password,
            f"not a public HTTP(S) source URL: {what}")
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(),
                       parts.path.rstrip("/"), parts.query, parts.fragment))


def excerpt_of(value, what):
    require(isinstance(value, str), f"non-string excerpt: {what}")
    require(len(value.split()) <= 40, f"excerpt over 40 whitespace tokens: {what}")
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def passage_key(source_url, locator, quotation, what):
    return (url(source_url, what), text(locator, what + " locator"),
            excerpt_of(quotation, what))


def git(args, env_extra=None, cwd=None, check=True):
    env = {**os.environ, **(env_extra or {})}
    result = subprocess.run(["git", *args], cwd=str(cwd or ROOT), env=env,
                            capture_output=True, text=True)
    if check and result.returncode != 0:
        raise ValueError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result


# --------------------------------------------------------------------------
# preservation / inventory (no-harm)
# --------------------------------------------------------------------------

def preservation():
    baseline = load("reports/round-7/baseline.json")
    base = baseline["baseline_revision"]
    require(re.fullmatch(r"[0-9a-f]{40}", base), "baseline revision is not a sha1")
    git(["cat-file", "-e", f"{base}^{{commit}}"])
    tracked = git(["ls-tree", "-r", "--name-only", base]).stdout.splitlines()
    counts = collections.Counter()
    for relative in tracked:
        current = ROOT / relative
        require(current.is_file() and not current.is_symlink(),
                f"missing/linked tracked-at-BASE file: {relative}")
        original = subprocess.check_output(["git", "show", f"{base}:{relative}"],
                                           cwd=str(ROOT))
        actual = current.read_bytes()
        if relative in APPEND_ONLY:
            require(actual.startswith(original), f"append-only prefix lost: {relative}")
            counts["append_only_prefix_preserved"] += 1
        elif relative in EDITABLE:
            counts["explicitly_editable"] += 1
        else:
            require(actual == original, f"historical file changed vs BASE: {relative}")
            counts["byte_identical"] += 1
    visible = set(filter(None, git(["ls-files", "--cached", "--others",
                                    "--exclude-standard", "-z"]).stdout.split("\0")))
    allowed = set(tracked) | NEW_EXACT | {
        path for path in visible if path.startswith(NEW_PREFIXES)}
    unexpected = visible - allowed
    require(not unexpected, f"unexpected deliverable files: {sorted(unexpected)}")
    return {"base_revision": base, "tracked_at_base": len(tracked),
            **dict(counts),
            "unexpected_new_files": sorted(unexpected)}


def inventory():
    argv = [sys.executable, INVENTORY_TOOL, "--json", "--summary",
            "--root", "corpus/knowledge"]
    result = subprocess.run(argv, cwd=str(ROOT), capture_output=True, text=True,
                            timeout=120)
    require(result.returncode == 0, f"inventory failed: {result.stderr.strip()}")
    data = json.loads(result.stdout)
    totals = {key: data["totals"][key] for key in INVENTORY_TOTALS}
    require(totals == INVENTORY_TOTALS, f"historical knowledge totals changed: {totals}")
    partitions = dict(sorted(collections.Counter(
        record["path"].split("/")[0] for record in data["files"]).items()))
    return {"argv": argv, "exit": 0, "totals": totals, "partitions": partitions,
            "limit": "Preserved knowledge inventory/marker counts, not a quality score "
                     "and not historical truth."}


# --------------------------------------------------------------------------
# claim F — five fixed source ledgers + parent reconciliation + spot-checks
# --------------------------------------------------------------------------

def measure_f_ledgers(bundle):
    targets = bundle["targets"]
    schema = bundle["schema"]
    documents = bundle["ledgers"]
    source_dir = ROOT / "corpus/lessons/round-7-sources"
    found = sorted(path.stem for path in source_dir.glob("*.json"))
    require(found == [f"{i:02d}" for i in range(8, 13)],
            f"expected exactly the five raw ledgers 08..12, found {found}")
    require(sorted(documents) == FIXED_IDS, "ledger ids do not match the fixed five")
    require(len(schema["required"]) == len(set(schema["required"])), "schema fields")
    require(schema["excerpt_word_cap"] == 40, "excerpt cap changed")
    require(set(schema["results"]) == {"scoped-support", "partial-support",
                                       "contradicted", "unresolved"},
            "result vocabulary changed")
    counted = {}
    entries_with_passages = set()
    raw_keys = set()
    for assignment in ("08", "09", "10", "11", "12"):
        target = targets[assignment]
        document = documents.get(target["id"])
        require(document is not None, f"missing ledger for {target['id']}")
        what = target["id"]
        require(set(schema["required"]) <= set(document),
                f"incomplete schema: {what}")
        require(document["round"] == 7, f"wrong round: {what}")
        require(document["baseline_revision"] == bundle["base"],
                f"wrong baseline: {what}")
        for field, expected in (("id", target["id"]),
                                ("question", target["question"]),
                                ("entry", target["entry"]),
                                ("previous_id", target["previous_id"]),
                                ("source_url", target["source_url"]),
                                ("source_kind", target["source_kind"])):
            require(document[field] == expected,
                    f"fixed {field} binding differs: {what}")
        require(re.match(r"\d{4}-\d{2}-\d{2}", document["accessed_at"]),
                f"accessed_at does not begin with an ISO date: {what}")
        text(document["retrieval_method"], what + " retrieval_method")
        text(document["source_locator"], what + " source_locator")
        text(document["basis"], what + " basis")
        text(document["limits"], what + " limits")
        require(document["result"] in schema["results"],
                f"invalid result value: {what}")
        for flag in ("retrieved_passage", "directly_relevant_nonbibliographic"):
            require(isinstance(document[flag], bool),
                    f"{flag} is not a real boolean: {what}")
        if document["retrieved_passage"]:
            key = passage_key(document["source_url"], document["source_locator"],
                              document["source_excerpt"], what)
            raw_keys.add(key)
            if document["directly_relevant_nonbibliographic"]:
                counted.setdefault(key, {"row_id": what, "entry": target["entry"],
                                         "url": key[0], "excerpt": key[2]})
                entries_with_passages.add(target["entry"])
        else:
            require(document["source_excerpt"] == "",
                    f"failed retrieval must keep an empty excerpt: {what}")
    distinct = len(counted)
    require(distinct >= 3,
            f"fewer than three distinct substantive main passages: {distinct}")
    require(len(entries_with_passages) >= 3,
            f"main passages cover fewer than three entries: {len(entries_with_passages)}")
    return {"ledger_files": found, "fixed_ids": FIXED_IDS,
            "ledger_rows": len(documents),
            "results": dict(collections.Counter(
                doc["result"] for doc in documents.values())),
            "distinct_main_passage_keys": distinct,
            "entries_with_main_passages": len(entries_with_passages),
            "counted_passages": sorted(counted.values(),
                                       key=lambda record: record["row_id"]),
            "limits": "Only source_excerpt counts as a passage; basis/limits prose, "
                      "locator text and bibliography never count. Distinctness is "
                      "URL + NFKC whitespace-normalized locator/excerpt."}


def measure_f_parents(reconciliation, spotchecks, targets, ledgers):
    require(reconciliation["round"] == spotchecks["round"] == 7, "wrong parent round")
    require(reconciliation["baseline_revision"]
            == spotchecks["baseline_revision"] == ledgers_base(), "wrong parent baseline")
    rows = reconciliation["rows"]
    require(len(rows) == len({row["id"] for row in rows}) == 5,
            "reconciliation must bind exactly the five fixed target ids")
    dispositions = collections.Counter()
    for row in rows:
        what = row["id"]
        require(what in FIXED_IDS, f"reconciliation row is not a fixed id: {what}")
        target = targets[target_assignment(what)]
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
            require(document["retrieved_passage"] and document["directly_relevant_nonbibliographic"],
                    f"ineligible ledger row promoted: {what}")
    require(dict(dispositions) == CONSERVATIVE_MIX,
            f"parent dispositions must stay conservative 3 scoped + 2 partial: {dict(dispositions)}")
    checks = spotchecks["checks"]
    require(len(checks) == len({check["id"] for check in checks}),
            "parent check identity collision")
    parent_keys = set()
    parent_urls = set()
    for check in checks:
        what = check["id"]
        require(check["row_id"] in FIXED_IDS,
                f"parent check is not bound to a fixed id: {what}")
        require(check["result"] == "success" and check["retrieved_passage"] is True
                and check["directly_relevant_nonbibliographic"] is True,
                f"unsuccessful/non-content parent check: {what}")
        document = ledgers[check["row_id"]]
        require(url(check["source_url"], what) == url(document["source_url"], what),
                f"parent URL does not match the bound ledger row: {what}")
        require(check["source_kind"] == document["source_kind"],
                f"parent kind mismatch: {what}")
        for field in ("accessed_at", "retrieval_method", "basis", "locator",
                      "language_and_mediation", "limits", "excerpt_form"):
            text(check[field], what + " " + field)
        key = passage_key(check["source_url"], check["locator"], check["excerpt"], what)
        parent_keys.add(key)
        parent_urls.add(key[0])
    require(len(parent_keys) >= 2,
            f"fewer than two distinct parent passage receipts: {len(parent_keys)}")
    require(len(parent_urls) >= 2,
            f"fewer than two distinct bound parent refetch URLs: {len(parent_urls)}")
    return {"reconciliation_rows": len(rows),
            "parent_dispositions": dict(dispositions),
            "parent_checks": len(checks),
            "parent_distinct_passage_keys": len(parent_keys),
            "parent_distinct_refetch_urls": len(parent_urls)}


_TARGETS_CACHE = {}


def targets_by_assignment():
    if not _TARGETS_CACHE:
        raw = load("reports/round-7/targets.json")["targets"]
        require(len(raw) == 5 and len({t["assignment"] for t in raw}) == 5,
                "targets must carry five fixed assignments")
        for target in raw:
            _TARGETS_CACHE[target["assignment"]] = target
    return _TARGETS_CACHE


def target_assignment(row_id):
    for assignment, target in targets_by_assignment().items():
        if target["id"] == row_id:
            return assignment
    raise ValueError(f"unknown fixed id: {row_id}")


def ledgers_base():
    return load("reports/round-7/baseline.json")["baseline_revision"]


def f_inputs():
    documents = {}
    for assignment, target in sorted(targets_by_assignment().items()):
        path = ROOT / "corpus/lessons/round-7-sources" / f"{assignment}.json"
        documents[target["id"]] = json.loads(path.read_text(encoding="utf-8"))
    return documents


def f_bundle_with(reconciliation, spotchecks):
    return {"ledgers": f_inputs(), "targets": targets_by_assignment(),
            "schema": load("reports/round-7/targets.json")["ledger_schema"],
            "base": ledgers_base(), "reconciliation": reconciliation,
            "spotchecks": spotchecks}


def f_negative_controls(bundle, parents_present):
    controls = []

    def reject(name, change, expected, mutate_parents=False):
        altered = copy.deepcopy(bundle)
        change(altered["ledgers"] if not mutate_parents else altered)
        try:
            if mutate_parents:
                measure_f_parents(altered["reconciliation"], altered["spotchecks"],
                                  altered["targets"], altered["ledgers"])
            else:
                measure_f_ledgers(altered)
        except ValueError as error:
            require(expected in str(error),
                    f"wrong rejection for {name}: {error}")
            controls.append({"control": name, "rejected": True,
                             "diagnostic": str(error)})
        else:
            raise ValueError(f"mutation survived: {name}")

    def drop_fifth(ledgers):
        ledgers.pop(FIXED_IDS[-1])

    reject("missing-fifth-ledger", drop_fifth, "ledger ids do not match")
    reject("invalid-result-value",
           lambda ledgers: ledgers[FIXED_IDS[0]].update(result="full-support"),
           "invalid result value")
    reject("bool-like-invalid-flag",
           lambda ledgers: ledgers[FIXED_IDS[0]].update(retrieved_passage="true"),
           "not a real boolean")
    reject("excerpt-over-40-tokens",
           lambda ledgers: ledgers[FIXED_IDS[0]].update(
               source_excerpt="word " * 41),
           "excerpt over 40 whitespace tokens")

    def two_entries_only(ledgers):
        for row_id in FIXED_IDS:
            if row_id not in ("R7-F01", "R7-F03", "R7-F04"):
                ledgers[row_id].update(retrieved_passage=False, source_excerpt="")

    reject("insufficient-entries", two_entries_only, "fewer than three entries")

    if parents_present:
        def flip_disposition(bundle_all):
            row = bundle_all["reconciliation"]["rows"][0]
            row["disposition"] = ("partial-support"
                                  if row["disposition"] == "scoped-support"
                                  else "scoped-support")

        def duplicate_parent_receipt(bundle_all):
            clone = dict(bundle_all["spotchecks"]["checks"][0])
            clone["id"] = "PX99"
            bundle_all["spotchecks"]["checks"] = [clone, dict(clone)]

        reject("duplicate-parent-receipt-does-not-inflate", duplicate_parent_receipt,
               "fewer than two distinct parent passage receipts", mutate_parents=True)
        reject("wrong-disposition-mix", flip_disposition,
               "conservative 3 scoped + 2 partial", mutate_parents=True)
        reject("bad-parent-url",
               lambda bundle_all: bundle_all["spotchecks"]["checks"][0].update(
                   source_url="https://example.org/not-the-bound-url"),
               "parent URL does not match", mutate_parents=True)
        reject("parent-not-success",
               lambda bundle_all: bundle_all["spotchecks"]["checks"][0].update(
                   result="failed"),
               "unsuccessful/non-content parent check", mutate_parents=True)
        reject("insufficient-parents",
               lambda bundle_all: bundle_all["spotchecks"].update(
                   checks=bundle_all["spotchecks"]["checks"][:1]),
               "fewer than two distinct parent passage receipts", mutate_parents=True)
        return {"passed": len(controls), "controls": controls}
    return {"passed": len(controls), "controls": controls,
            "skipped": ["parent-file negatives skipped: parent reconciliation/"
                        "spot-checks not present yet"]}


# --------------------------------------------------------------------------
# dispatch binding
# --------------------------------------------------------------------------

def check_dispatch(conformance_defects):
    missing = []
    plan = load("reports/round-7/dispatch-plan.json")
    dispatch = load("reports/round-7/dispatch.json")
    require(dispatch["workers"] == dispatch["completed"] == 16
            and dispatch["failed"] == 0, "dispatch incomplete")
    require(dispatch["actual_executed_batches"] == 1, "extra round-7 swarm")
    require(len(plan["items"]) == len(set(plan["items"])) == 16,
            "assignment count/collision in plan")
    require(dispatch["requested_model"] == plan["model"]
            == "zai-coding-plan/glm-5.3-flash-low", "model route drift")
    require(dispatch["requested_profile"] == plan["subagent_type"]
            == "sec-fast-zai-flash-low", "profile route drift")
    workers = dispatch["workers_by_assignment"]
    require(len(workers) == len({w["agent_id"] for w in workers}) == 16,
            "worker identity collision")
    require({w["assignment"] for w in workers} == {f"{i:02d}" for i in range(1, 17)}
            and all(w["outcome"] == "completed" for w in workers),
            "worker assignment/return mismatch")
    binding_path = dispatch.get("native_request_binding")
    binding = None
    if binding_path and (ROOT / binding_path).is_file():
        binding = load(binding_path)
        require(binding["model"] == dispatch["requested_model"]
                and binding["subagent_type"] == dispatch["requested_profile"],
                "binding route drift")
        require(binding.get("tool_call_id") == dispatch.get("native_tool_call_id"),
                "binding does not carry the native tool-call id")
        require(binding.get("width") == 16, "binding width drift")
        require(binding.get("all_other_arguments_match") is True,
                "binding declares arguments other than the documented replacement differ")
        saved_template = (HERE / "prompt-template.txt").read_text(encoding="utf-8")
        args = {"description": plan["description"], "subagent_type": plan["subagent_type"],
                "model": plan["model"], "prompt_template": saved_template,
                "items": plan["items"]}
        planned_digest = sha(json.dumps(args, sort_keys=True, separators=(",", ":"),
                                        ensure_ascii=False).encode("utf-8"))
        require(planned_digest == binding["planned_canonical_args_sha256"],
                "saved-template request reconstruction digest differs from binding")
        replacement = binding.get("template_replacement")
        require(isinstance(replacement, dict)
                and isinstance(replacement.get("old"), str)
                and isinstance(replacement.get("new"), str)
                and replacement["old"] in saved_template,
                "binding must document the single template replacement as old/new text")
        actual_args = dict(args)
        actual_args["prompt_template"] = saved_template.replace(
            replacement["old"], replacement["new"])
        actual_digest = sha(json.dumps(actual_args, sort_keys=True,
                                       separators=(",", ":"),
                                       ensure_ascii=False).encode("utf-8"))
        require(actual_digest == binding["actual_canonical_args_sha256"],
                "actual request reconstruction (template with the one documented "
                "replacement) digest differs from binding")
        require(binding.get("documented_replacement_count") == 1,
                "binding must document exactly one template replacement")
        saved = binding.get("saved_template_matches_actual")
        require(isinstance(saved, bool),
                "binding must declare saved_template_matches_actual as a boolean")
        if saved is False:
            conformance_defects.append(
                "binding declares saved_template_matches_actual=false: the quoted "
                "fleet template was not byte-verbatim at step 6 of the actual "
                "prompt (documented old->new replacement; digest mapping verified "
                "planned and actual); recorded as an honest conformance defect, "
                "not an F or O failure")
        dispatch_result = {"completed": 16, "executed_batches": 1,
                           "planned_canonical_args_sha256": planned_digest,
                           "actual_canonical_args_sha256": actual_digest,
                           "digest_mapping_verified": True,
                           "saved_template_matches_actual": saved,
                           "limit": "Saved-argument digest binding, not upstream wire "
                                    "identity or simultaneous runtime concurrency."}
    else:
        missing.append(f"native request binding not present yet: {binding_path}")
        dispatch_result = {"completed": 16, "executed_batches": 1,
                           "canonical_args_sha256": None}
    return dispatch_result, missing


# --------------------------------------------------------------------------
# claim O — real CLI subprocesses
# --------------------------------------------------------------------------

def run_repo(argv, timeout=240, cwd=None):
    return subprocess.run(argv, cwd=str(cwd or ROOT), capture_output=True,
                          text=True, timeout=timeout)


def json_stdout(result, label):
    require(result.returncode != 2 or "Traceback" not in result.stderr,
            f"{label}: traceback printed")
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{label}: stdout is not one JSON object: {exc}: "
                         f"{result.stdout[:200]}") from exc


def assembler_checks():
    check = run_repo([sys.executable, ASSEMBLER, "--check"])
    require(check.returncode == 0,
            f"assembler --check exit {check.returncode}: {check.stderr.strip()}")
    selftest = run_repo([sys.executable, ASSEMBLER, "--selftest"], timeout=300)
    require(selftest.returncode == 0,
            f"assembler --selftest exit {selftest.returncode}: {selftest.stderr.strip()}")
    return {"assembler_check_exit": check.returncode,
            "assembler_selftest_exit": selftest.returncode,
            "assembler_selftest_stdout": selftest.stdout.strip()[:400]}


def guard_positive_and_selftest():
    positive = run_repo([sys.executable, GUARD, PACKET_REL])
    payload = json_stdout(positive, "guard positive")
    require(positive.returncode == 0 and payload["exit"] == 0
            and payload.get("findings") == [],
            f"guard positive not clean: {payload}")
    selftest = run_repo([sys.executable, GUARD, "--selftest"], timeout=300)
    payload = json_stdout(selftest, "guard selftest")
    require(selftest.returncode == 0 and payload.get("selftest_passed") is True,
            f"guard selftest failed: {payload.get('note')}")
    require(not payload.get("missing_inputs"),
            f"guard selftest missing inputs: {payload.get('missing_inputs')}")
    counts = {key: payload[key] for key in ("positive_controls", "domain_controls",
                                            "malformed_controls", "frozen_checks")}
    require(counts["positive_controls"]["passed"] >= 5
            and counts["positive_controls"]["passed"] == counts["positive_controls"]["total"],
            f"guard positive controls below the declared five: {counts}")
    require(counts["domain_controls"]["passed"] >= 16
            and counts["domain_controls"]["passed"] == counts["domain_controls"]["total"],
            f"guard domain controls below the declared sixteen: {counts}")
    require(counts["malformed_controls"]["passed"] >= 4
            and counts["malformed_controls"]["passed"] == counts["malformed_controls"]["total"],
            f"guard malformed controls below the declared four: {counts}")
    require(counts["frozen_checks"]["passed"] >= 3
            and counts["frozen_checks"]["passed"] == counts["frozen_checks"]["total"],
            f"guard frozen checks below the declared three: {counts}")
    return {"guard_positive_exit": positive.returncode,
            "guard_selftest_exit": selftest.returncode,
            "guard_selftest_counts": counts}


def apply_pointer_patch(doc, patch):
    """Independent RFC 6901-style patch application (guard helper not used)."""
    pointer = patch.get("path")
    op = patch.get("op")
    require(isinstance(pointer, str) and pointer.startswith("/"),
            f"JSON pointer must start with '/': {pointer!r}")
    parts = [part.replace("~1", "/").replace("~0", "~")
             for part in pointer.split("/")[1:]]
    require(bool(parts), "empty JSON pointer")

    def descend(node, index):
        key = parts[index]
        if isinstance(node, list):
            try:
                position = int(key)
            except ValueError as exc:
                raise ValueError(f"non-integer array index: {pointer}") from exc
            require(0 <= position < len(node), f"array index out of range: {pointer}")
            if index == len(parts) - 1:
                if op == "remove":
                    node.pop(position)
                elif op == "add":
                    node.insert(position, patch.get("value"))
                else:
                    node[position] = patch.get("value")
            else:
                descend(node[position], index + 1)
        elif isinstance(node, dict):
            if index == len(parts) - 1:
                if op == "remove":
                    node.pop(key, None)
                elif op == "add":
                    node[key] = patch.get("value")
                else:
                    require(key in node, f"replace target missing: {pointer}")
                    node[key] = patch.get("value")
            else:
                require(key in node, f"pointer breaks at {key!r}: {pointer}")
                descend(node[key], index + 1)
        else:
            raise ValueError(f"cannot descend into scalar: {pointer}")

    descend(doc, 0)


def independent_controls(scratch):
    controls = load(CONTROLS_REL)
    require(controls.get("profile") == PROFILE, "controls profile drift")
    packet_doc = load(PACKET_REL)
    outcomes = {"positive": [], "domain": [], "malformed": [], "cli_usage": []}
    tracebacks = []

    def execute(name, argv, expected_exit, expected_ids, kind):
        result = run_repo(argv)
        if "Traceback" in result.stderr:
            tracebacks.append(name)
        payload = json_stdout(result, f"control {name}")
        actual_ids = sorted(finding.get("id") for finding in payload.get("findings", []))
        record = {"name": name, "expected_exit": expected_exit,
                  "actual_exit": result.returncode, "actual_ids": actual_ids}
        require(result.returncode == expected_exit,
                f"control {name}: exit {result.returncode} != {expected_exit}")
        if kind == "positive":
            require(payload.get("findings") == [], f"control {name}: findings not empty")
        elif kind == "domain":
            require(set(expected_ids) <= set(actual_ids),
                    f"control {name}: expected stable ids {expected_ids} not in {actual_ids}")
        else:
            require("D3-DATA" in actual_ids, f"control {name}: D3-DATA missing")
        return record

    base = execute("base-packet-unpatched",
                   [sys.executable, GUARD, PACKET_REL], 0, [], "positive")
    outcomes["positive"].append(base)
    for index, control in enumerate(controls.get("positive", [])):
        doc = copy.deepcopy(packet_doc)
        for patch in control.get("patches", []):
            apply_pointer_patch(doc, patch)
        path = scratch / f"positive-{index}.json"
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
        outcomes["positive"].append(execute(
            control["name"], [sys.executable, GUARD, str(path)],
            control["expected_exit"], control["expected_ids"], "positive"))
    for index, control in enumerate(controls.get("domain", [])):
        doc = copy.deepcopy(packet_doc)
        for patch in control.get("patches", []):
            apply_pointer_patch(doc, patch)
        path = scratch / f"domain-{index}.json"
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
        outcomes["domain"].append(execute(
            control["name"], [sys.executable, GUARD, str(path)],
            control["expected_exit"], control["expected_ids"], "domain"))
    for index, control in enumerate(controls.get("malformed", [])):
        path = scratch / f"malformed-{index}.json"
        kind = control.get("kind")
        if kind == "invalid-json":
            path.write_bytes(b'{"profile":')
        elif kind == "invalid-utf8":
            path.write_bytes(b"\xff\xfe{}")
        elif kind == "wrong-root":
            path.write_bytes(b"[]")
        elif kind == "missing-file":
            path = scratch / "missing-file-does-not-exist.json"
        else:
            raise ValueError(f"unknown malformed kind: {kind}")
        outcomes["malformed"].append(execute(
            control["name"], [sys.executable, GUARD, str(path)],
            control["expected_exit"], control["expected_ids"], "malformed"))
    domain_ids = {stable for record in outcomes["domain"]
                  for stable in record["actual_ids"]}
    require(len(outcomes["domain"]) >= 16,
            f"fewer than sixteen independent domain controls: {len(outcomes['domain'])}")
    require(len(domain_ids) >= 12,
            f"fewer than twelve distinct stable-id domain negatives: {sorted(domain_ids)}")
    require(len(outcomes["malformed"]) >= 4,
            f"fewer than four independent malformed controls: {len(outcomes['malformed'])}")
    require(not tracebacks, f"controls printed tracebacks: {tracebacks}")
    return {"positive_runs": len(outcomes["positive"]),
            "domain_runs": len(outcomes["domain"]),
            "malformed_runs": len(outcomes["malformed"]),
            "distinct_domain_stable_ids": sorted(domain_ids),
            "tracebacks": tracebacks,
            "limit": "Controls executed through the real guard CLI with an "
                     "independent pointer-patch implementation; expected "
                     "diagnostics come from controls.json, never from guard code."}


def frozen_private_copies(scratch):
    """Snapshot-interface checks against a private copy of the guard."""
    private_tools = scratch / "tools"
    private_tools.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / GUARD, private_tools / "check-evidence-coupling.py")
    (scratch / "examples/culture-d3").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / PACKET_REL, scratch / PACKET_REL)
    (scratch / "corpus/lessons/round-6-sources").mkdir(parents=True, exist_ok=True)
    for relative in CLOSED_LEDGERS:
        shutil.copyfile(ROOT / relative, scratch / relative)
    guard_argv = [sys.executable, str(private_tools / "check-evidence-coupling.py"),
                  str(scratch / PACKET_REL), "--frozen"]

    def manifest(overrides=None):
        entries = {PACKET_REL: file_sha(PACKET_REL)}
        entries.update({relative: file_sha(relative) for relative in CLOSED_LEDGERS})
        for override, value in (overrides or {}).items():
            if value is None:
                entries.pop(override, None)
            else:
                entries[override] = value
        expected = {"profile": PROFILE, "manifest": entries,
                    "expected_exit": 0, "finding_ids": []}
        path = scratch / "expected.json"
        path.write_text(json.dumps(expected, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
        return path

    def frozen_case(name, manifest_path, expected_exit, want_snapshot):
        result = run_repo(guard_argv + [str(manifest_path)], cwd=scratch)
        payload = json_stdout(result, f"frozen case {name}")
        ids = {finding.get("id") for finding in payload.get("findings", [])}
        require(result.returncode == expected_exit and payload["exit"] == expected_exit,
                f"frozen case {name}: exit {result.returncode} != {expected_exit}")
        require(not want_snapshot or "D3-SNAPSHOT" in ids,
                f"frozen case {name}: D3-SNAPSHOT missing ({sorted(ids)})")
        require(want_snapshot or payload.get("findings") == [],
                f"frozen case {name}: unexpected findings {sorted(ids)}")
        return {"name": name, "exit": result.returncode, "ids": sorted(ids)}

    good = frozen_case("good-manifest", manifest(), 0, False)
    tampered = frozen_case("tampered-packet-digest", manifest(
        {PACKET_REL: "0" * 64}), 2, True)
    traversal = frozen_case("parent-traversal-key", manifest(
        {"../outside.json": "0" * 64}), 2, True)
    absolute = frozen_case("absolute-path-key", manifest(
        {"/etc/hostname": "0" * 64}), 2, True)
    unknown = frozen_case("unknown-path-key", manifest(
        {"examples/culture-d3/absent.json": "0" * 64}), 2, True)
    return {"frozen_cases": [good, tampered, traversal, absolute, unknown],
            "limit": "Private scratch copy of the guard and inputs; the live "
                     "repository inputs are never edited."}


def guard_foreign_cwd_no_writes(scratch):
    watched = [PACKET_REL, CONTROLS_REL, "reports/round-7/d3-contract.json",
               "reports/round-7/targets.json", "reports/round-7/baseline.json",
               "reports/round-6/parent-reconciliation.json"] + COMPONENT_RELS \
        + CLOSED_LEDGERS

    def snapshot():
        return {relative: (file_sha(relative),
                           (ROOT / relative).stat().st_mtime_ns)
                for relative in watched}

    before = snapshot()
    result = run_repo([sys.executable, GUARD, str(ROOT / PACKET_REL)], cwd=scratch)
    payload = json_stdout(result, "guard foreign-cwd positive")
    require(result.returncode == 0 and payload["exit"] == 0
            and payload.get("findings") == [], f"foreign-cwd run not clean: {payload}")
    require(snapshot() == before, "guard foreign-cwd run modified an input")
    return {"foreign_cwd": "disposable system temporary directory",
            "inputs_watched": len(watched), "input_writes": "none",
            "guard_exit": result.returncode}


def frozen_expected_file():
    path = ROOT / "examples/culture-d3/expected.json"
    if not path.is_file():
        return None, ["examples/culture-d3/expected.json not present yet "
                      "(parent creates it after inputs stabilize)"]
    expected = load("examples/culture-d3/expected.json")
    require(expected.get("profile") == PROFILE, "expected profile drift")
    manifest = expected.get("manifest")
    require(isinstance(manifest, dict) and manifest, "expected manifest missing")
    missing_keys = [key for key in REQUIRED_MANIFEST if key not in manifest]
    require(not missing_keys,
            f"expected manifest is not comprehensive, missing: {missing_keys}")
    cycle_keys = [key for key in manifest
                  if key in ("examples/culture-d3/handoff.md",
                             "examples/culture-d3/README.md")]
    require(not cycle_keys,
            f"expected manifest must not bind the generated handoff/readme "
            f"(digest cycle): {cycle_keys}")
    wrong = [key for key, value in manifest.items() if value != file_sha(key)]
    require(not wrong, f"expected manifest digest drift: {wrong}")
    require(expected.get("expected_exit") == 0
            and isinstance(expected.get("expected_exit"), int)
            and not isinstance(expected.get("expected_exit"), bool),
            "expected_exit must be the strict integer 0")
    require(expected.get("finding_ids") == [], "finding_ids must be empty")
    result = run_repo([sys.executable, GUARD, PACKET_REL,
                       "--frozen", "examples/culture-d3/expected.json"])
    payload = json_stdout(result, "guard --frozen expected.json")
    require(result.returncode == 0 and payload["exit"] == 0,
            f"guard --frozen rejected the committed expectation: {payload}")
    return {"manifest_entries": len(manifest),
            "required_keys": len(REQUIRED_MANIFEST),
            "guard_frozen_exit": result.returncode}, []


def packet_contract_minimums():
    packet = load(PACKET_REL)
    require(packet["profile"] == PROFILE and packet["name"] == PACKET_NAME,
            "packet profile/name drift")
    minimums = {"eras": 2, "lexicon": 20, "names": 6, "beliefs": 2,
                "costumes": 4, "bridges": 5, "references": 5}
    counts = {key: len(packet[key]) for key in minimums}
    require(all(counts[key] >= minimums[key] for key in minimums),
            f"packet below contract minimums: {counts}")
    require(packet["canon_status"] == "NON-CANON", "canon status drift")
    require(packet["handoff_status"] == "prepared-not-accepted",
            "handoff status drift")
    screening = packet["screening"]
    require(screening["status"] == "unresolved"
            and screening["real_language_sweep_performed"] is False
            and isinstance(screening["limits"], str) and screening["limits"].strip(),
            "screening no longer declares the unresolved real-language sweep")
    rule = packet["naming_rule"]
    offsets = rule["allowed_offsets"]
    require(isinstance(offsets, list) and offsets
            and all(isinstance(x, int) and not isinstance(x, bool) for x in offsets)
            and len(offsets) == len(set(offsets)),
            "naming_rule allowed_offsets must be a nonempty unique integer set")
    require(isinstance(rule["chosen_offset"], int)
            and not isinstance(rule["chosen_offset"], bool)
            and rule["chosen_offset"] in offsets,
            "chosen timing offset outside the discrete allowed integer set")
    e1 = {lexeme["id"]: lexeme["forms"]["E1"] for lexeme in packet["lexicon"]}
    for lexeme in packet["lexicon"]:
        e0 = lexeme["forms"]["E0"]
        require(lexeme["forms"]["E1"] == ("f" + e0[1:] if e0.startswith("p") else e0),
                f"E1 form is not the SC1 computation: {lexeme['id']}")
        require(re.fullmatch(r"[a-z]+", lexeme["native_form"]),
                f"native form not ASCII lowercase: {lexeme['id']}")
    for name in packet["names"]:
        formation = name["formation"]
        replayed = e1[formation["bases"][0]] + e1[formation["bases"][1]]
        require(replayed == name["native_form"] == formation["expected"],
                f"name replay fails: {name['id']}")
        require(re.fullmatch(r"[a-z]+", name["native_form"]),
                f"name not ASCII lowercase: {name['id']}")
    costumes = {costume["id"]: costume for costume in packet["costumes"]}
    require(costumes["C03"]["claimed_status"] == "violation",
            "C03 is no longer a declared violation")
    materials = {material["id"]: material for material in packet["materials"]}
    rules = {rule["id"]: rule for rule in packet["rank_rules"]}
    rr1 = rules["RR1"]
    require(rr1["effect"] == "prohibit"
            and rr1["property"]["kind"] == "material"
            and rr1["property"]["value"] == materials["M02"]["gate_name"]
            and costumes["C03"]["wearer_rank"] in rr1["wearer_ranks"],
            "RR1 prohibition shape drifted from the contract")
    return {"counts": counts, "names_replayed": len(packet["names"]),
            "lexicon_replayed": len(packet["lexicon"])}


def legacy_gates():
    naming = run_repo(NAMING_ARGV)
    require(naming.returncode == 1,
            f"naming gate exit {naming.returncode} (expected 1)")
    naming_ids = {match.group(1) for match in
                  re.finditer(r"^FINDING (\S+):", naming.stdout, re.M)}
    require("CROSS-HOLD" in naming_ids, f"CROSS-HOLD missing: {sorted(naming_ids)}")
    require(any("NAME-NEAR" in line and "'E0' vs 'E1'" in line
                for line in naming.stdout.splitlines()),
            f"NAME-NEAR E0/E1 missing: {sorted(naming_ids)}")
    require(not any(identifier.startswith(("PHON-", "DERIV-"))
                    for identifier in naming_ids),
            f"native phonotactic/derivation FAIL: {sorted(naming_ids)}")
    require(": FAIL" not in naming.stdout, "naming gate printed a FAIL finding")
    costume = run_repo(COSTUME_ARGV)
    require(costume.returncode == 1,
            f"costume gate exit {costume.returncode} (expected 1)")
    costume_ids = {match.group(1) for match in
                   re.finditer(r"^FINDING (\S+):", costume.stdout, re.M)}
    require(costume_ids == {"R-01"},
            f"costume gate findings must be exactly the R-01 note: {sorted(costume_ids)}")
    require("C03" in costume.stdout, "R-01 note is not about C03")
    return {"naming_exit": naming.returncode, "naming_ids": sorted(naming_ids),
            "costume_exit": costume.returncode, "costume_ids": sorted(costume_ids)}


def handoff_and_readme():
    failures = []
    missing = []
    if not (ROOT / HANDOFF_REL).is_file():
        missing.append(f"{HANDOFF_REL} not present yet")
    else:
        gate = run_repo([sys.executable, "tools/gates/handoff-packet-check.py",
                         HANDOFF_REL])
        scan = re.search(r"INFO scan: fields=(\d+)/16 glossary-entries=(\d+)",
                         gate.stdout)
        require(scan is not None,
                f"handoff gate printed no scan line: {gate.stdout[:200]}")
        fields, glossary = int(scan.group(1)), int(scan.group(2))
        if gate.returncode != 0 or fields != HANDOFF_FIELDS_16 or glossary < 20:
            failures.append(f"handoff gate not green yet: exit {gate.returncode}, "
                            f"fields {fields}/16, glossary entries {glossary} "
                            "(stale draft; scribe must replace it with actual packet data)")
        packet = load(PACKET_REL)
        handoff_text = (ROOT / HANDOFF_REL).read_text(encoding="utf-8")
        absent_lexemes = [lexeme["native_form"] for lexeme in packet["lexicon"]
                          if lexeme["native_form"] not in handoff_text]
        absent_names = [name["native_form"] for name in packet["names"]
                        if name["native_form"] not in handoff_text]
        absent_bridges = [bridge["id"] for bridge in packet["bridges"]
                          if bridge["id"] not in handoff_text]
        lowered = handoff_text.lower()
        if absent_lexemes or absent_names or absent_bridges:
            failures.append(f"handoff does not carry actual packet data yet: "
                            f"{len(absent_lexemes)} lexemes, {len(absent_names)} names, "
                            f"{len(absent_bridges)} bridges missing")
        if "non-canon" not in lowered or "not canonized" not in lowered:
            failures.append("handoff does not keep the NON-CANON / not canonized standing")
    readme_text = (ROOT / README_REL).read_text(encoding="utf-8") \
        if (ROOT / README_REL).is_file() else ""
    required_commands = [f"{ASSEMBLER} --check", f"{GUARD} --selftest",
                         f"{GUARD} {PACKET_REL}",
                         f"--frozen {('examples/culture-d3/expected.json')}"]
    absent_commands = [command for command in required_commands
                       if command not in readme_text]
    if absent_commands:
        failures.append(f"README does not document real commands yet: {absent_commands}")
    return {"handoff_fields": None, "failures": failures,
            "missing": missing,
            "limit": "Handoff/README checks fail until the scribe replaces the "
                     "stale draft with actual packet data; never weakened."}


# --------------------------------------------------------------------------
# previous round's acceptance on delivered old surfaces
# --------------------------------------------------------------------------

def previous_acceptance():
    baseline = load("reports/round-7/baseline.json")
    base = baseline["baseline_revision"]
    git_dir = git(["rev-parse", "--absolute-git-dir"]).stdout.strip()
    with tempfile.TemporaryDirectory(prefix="round7-previous-acceptance-") as tmp:
        room = Path(tmp)
        export = room / "export"
        export.mkdir()
        index = room / "private-index"
        git(["read-tree", base], env_extra={"GIT_DIR": git_dir,
                                            "GIT_INDEX_FILE": str(index)})
        tracked = git(["ls-tree", "-r", "--name-only", base],
                      env_extra={"GIT_DIR": git_dir}).stdout.splitlines()
        copied = 0
        for relative in tracked:
            source = ROOT / relative
            require(source.is_file() and not source.is_symlink(),
                    f"missing tracked-at-BASE file for old export: {relative}")
            destination = export / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            copied += 1
        # disposable scratch infrastructure the round-6 runner needs as TMPDIR base
        supplement = ROOT / "reports/supplement-opencode-1"
        if supplement.is_dir():
            shutil.copytree(supplement, export / "reports/supplement-opencode-1",
                            ignore=shutil.ignore_patterns("scratch", "__pycache__"),
                            dirs_exist_ok=True)
        env = {**os.environ, "GIT_DIR": git_dir, "GIT_WORK_TREE": str(export),
               "GIT_INDEX_FILE": str(index), "TMPDIR": str(room)}
        result = subprocess.run([sys.executable, "reports/round-6/run-validation.py"],
                                cwd=str(export), env=env, capture_output=True,
                                text=True, timeout=900)
        require(result.returncode == 0,
                f"previous round-6 acceptance failed: {result.stdout} {result.stderr}")
        receipt = json.loads((export / "reports/round-6/validation.json")
                             .read_text(encoding="utf-8"))
    require(receipt["acceptance_checks_passed"] is True,
            "previous acceptance receipt is red")
    measurement = receipt["claims"]["O"]["measurement"]
    return {"argv": [sys.executable, "reports/round-6/run-validation.py"],
            "exit": result.returncode, "cwd": "disposable BASE-tracked export "
            "in a system temporary directory (private index pinned at BASE)",
            "exported_tracked_files": copied,
            "round6_acceptance_checks_passed": receipt["acceptance_checks_passed"],
            "d2_expected_findings_preserved": measurement.get("d2_expected_findings"),
            "old_gate_selftests_passed": measurement.get("gate_selftests_passed"),
            "limit": "Old surfaces only, isolated export, private index; live "
                     "index and historical receipts are never mutated."}


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main():
    report = {"round": 7, "baseline_revision": ledgers_base(),
              "counting_command": "python3 reports/round-7/run-validation.py",
              "acceptance_checks_passed": False,
              "runner_scratch": "disposable system temporary directory; absolute "
                                "scratch paths are never recorded"}
    failures = []
    missing_dependencies = []
    conformance_defects = []

    def section(name, function):
        try:
            report[name] = function()
        except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError,
                subprocess.SubprocessError) as error:
            failures.append(f"{name}: {error}")

    try:
        section("preservation", preservation)
        section("inventory", inventory)

        # ---- claim F ----
        try:
            documents = f_inputs()
            targets = targets_by_assignment()
            schema = load("reports/round-7/targets.json")["ledger_schema"]
            f_measurement = measure_f_ledgers(f_bundle_with(None, None))
            reconciliation_path = "reports/round-7/parent-reconciliation.json"
            spotchecks_path = "reports/round-7/parent-source-spotchecks.json"
            f_missing = []
            reconciliation = spotchecks = None
            if (ROOT / reconciliation_path).is_file():
                reconciliation = load(reconciliation_path)
            else:
                f_missing.append(f"{reconciliation_path} not present yet (parent)")
            if (ROOT / spotchecks_path).is_file():
                spotchecks = load(spotchecks_path)
            else:
                f_missing.append(f"{spotchecks_path} not present yet (parent)")
            parents_measurement = None
            if reconciliation is not None and spotchecks is not None:
                parents_measurement = measure_f_parents(
                    reconciliation, spotchecks, targets, documents)
            bundle = f_bundle_with(reconciliation, spotchecks)
            negatives = f_negative_controls(bundle,
                                            parents_present=reconciliation is not None
                                            and spotchecks is not None)
            report["claims"] = report.get("claims", {})
            report["claims"]["F"] = {
                "passed": not f_missing,
                "measurement": f_measurement,
                "parent_measurement": parents_measurement,
                "negative_controls": negatives,
                "missing_dependencies": f_missing,
            }
            missing_dependencies.extend(f"claim F: {item}" for item in f_missing)
        except (ValueError, OSError, KeyError, TypeError) as error:
            failures.append(f"claim F: {error}")
            report["claims"] = report.get("claims", {})
            report["claims"]["F"] = {"passed": False, "error": str(error)}

        # ---- dispatch ----
        try:
            dispatch_result, dispatch_missing = check_dispatch(conformance_defects)
            report["dispatch"] = dispatch_result
            missing_dependencies.extend(f"dispatch: {item}"
                                        for item in dispatch_missing)
        except (ValueError, OSError, KeyError, TypeError) as error:
            failures.append(f"dispatch: {error}")
        report["conformance_defects"] = conformance_defects

        # ---- claim O ----
        try:
            o_measurement = {}
            o_measurement.update(assembler_checks())
            o_measurement.update(guard_positive_and_selftest())
            with tempfile.TemporaryDirectory(
                    prefix="round7-validation-controls-") as controls_tmp:
                o_measurement["independent_controls"] = independent_controls(
                    Path(controls_tmp))
            with tempfile.TemporaryDirectory(
                    prefix="round7-validation-frozen-") as frozen_tmp:
                o_measurement["frozen_private_copies"] = frozen_private_copies(
                    Path(frozen_tmp))
                o_measurement["guard_foreign_cwd"] = guard_foreign_cwd_no_writes(
                    Path(frozen_tmp))
            expected, expected_missing = frozen_expected_file()
            o_measurement["frozen_expected"] = expected
            missing_dependencies.extend(f"claim O: {item}" for item in expected_missing)
            o_measurement["packet_contract_minimums"] = packet_contract_minimums()
            o_measurement["legacy_gates"] = legacy_gates()
            handoff = handoff_and_readme()
            o_measurement["handoff_and_readme"] = handoff
            for failure in handoff["failures"]:
                failures.append(f"claim O handoff/readme: {failure}")
            report["claims"] = report.get("claims", {})
            o_passed = (expected is not None and not handoff["failures"]
                        and not handoff["missing"])
            report["claims"]["O"] = {
                "passed": o_passed,
                "measurement": o_measurement,
                "missing_dependencies": expected_missing + handoff["missing"],
            }
        except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError,
                subprocess.SubprocessError) as error:
            failures.append(f"claim O: {error}")
            report["claims"] = report.get("claims", {})
            report["claims"]["O"] = {"passed": False, "error": str(error)}

        section("previous_acceptance", previous_acceptance)

        report["missing_dependencies"] = sorted(missing_dependencies)
        report["failures"] = failures
        report["acceptance_checks_passed"] = (
            not failures and not missing_dependencies
            and report.get("claims", {}).get("F", {}).get("passed") is True
            and report.get("claims", {}).get("O", {}).get("passed") is True
            and "preservation" in report and "inventory" in report
            and "previous_acceptance" in report and "dispatch" in report)
    finally:
        report["evidence_sha256"] = {
            relative: file_sha(relative) for relative in (
                "reports/round-7/run-validation.py", PACKET_REL, LEGACY_REL,
                CONTROLS_REL, "reports/round-7/d3-contract.json",
                "reports/round-7/targets.json", "reports/round-7/baseline.json",
                GUARD, ASSEMBLER)}
        report["limits"] = [
            "Receipt/schema/count/preservation and actual regression checks, not "
            "automated quotation truth, historical authenticity or cultural permission.",
            "All reviews are author-side; this runner decides no admission, promotion "
            "or closure, and never certifies canon.",
            "Dispatch binding checks saved arguments, not upstream wire identity or "
            "simultaneous runtime concurrency.",
            "Missing parent inputs are recorded as failing dependencies, never "
            "synthesized; expectations are never weakened to fit a defect."]
        (HERE / "validation.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8")
    f_measurement = report.get("claims", {}).get("F", {})
    o_measurement = report.get("claims", {}).get("O", {})
    print(json.dumps({
        "acceptance_checks_passed": report["acceptance_checks_passed"],
        "F_passed": f_measurement.get("passed", False),
        "O_passed": o_measurement.get("passed", False),
        "F_distinct_main_passages": (f_measurement.get("measurement") or {}).get(
            "distinct_main_passage_keys"),
        "O_guard_counts": (o_measurement.get("measurement") or {}).get(
            "guard_selftest_counts"),
        "missing_dependencies": report.get("missing_dependencies", []),
        "failures": report.get("failures", []),
        "conformance_defects": report.get("conformance_defects", []),
    }, ensure_ascii=False, indent=2))
    return 0 if report["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
