#!/usr/bin/env python3
"""Measure the fixed round-6 F claim without rewriting historical receipts."""

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
HERE = ROOT / "reports/round-6"
BASE = "030c3928de74ed514853bc1f7490e0f8bb4d451f"
CHECKPOINT = "104aa54c737d79c5df1382f65d578b61cbf831f2"
ARCHIVE_PIN = "https://web.archive.org/web/20231003011254/https://sacred-texts.com/hin/sbe30/sbe30020.htm"
ALLOWED_KINDS = {"primary-text", "peer-reviewed", "repository-scholarship", "museum-object", "secondary-scholarly"}
KIND_CORRECTIONS = {"R6-05-A": "secondary-scholarly", "R6-10-B": "secondary-scholarly"}
APPEND_ONLY = {"LOG.md", "SKILL.md", "corpus/lessons/round-6.md", "reports/round-6/kotodama.md",
               "corpus/knowledge/civilizations/india-vedic.md", "corpus/knowledge/civilizations/persia-achaemenid.md"}
EDITABLE = {"SCORECARD.md", "corpus/README.md"}
NEW_FILES = {f"reports/round-6/{name}" for name in (
    "parent-source-spotchecks.json", "parent-reconciliation.json", "run-validation.py", "validation.json", "outcome.json")}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def pinned(revision, relative):
    return subprocess.check_output(["git", "show", f"{revision}:{relative}"], cwd=ROOT)


def text(value):
    require(isinstance(value, str) and value.strip(), "empty or non-text evidence")
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def url(value):
    require(isinstance(value, str) and not any(c.isspace() for c in value), "not a single URL")
    parts = urlsplit(value)
    require(parts.scheme in {"http", "https"} and parts.hostname and not parts.username and not parts.password,
            "not a public HTTP(S) source URL")
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), parts.query, parts.fragment))


def excerpt(value):
    require(isinstance(value, str) and value.strip() and len(value.split()) <= 40, "missing or oversized excerpt")
    return text(value)


def passage_key(source_url, locator, quotation):
    return (url(source_url), text(locator), excerpt(quotation))


def measure_f(documents, targets, baseline, schema, reconciliation, parent):
    require(len(documents) == len(targets) == 12, "twelve source fragments required")
    require(reconciliation["round"] == parent["round"] == 6, "wrong parent round")
    require(reconciliation["baseline_revision"] == parent["baseline_revision"] == BASE, "wrong parent baseline")
    policy = reconciliation["passage_policy"]
    require(policy["mains_only"] is True and set(policy["allowed_source_kinds"]) == ALLOWED_KINDS,
            "main-only source-class policy changed")
    require(set(policy["excluded_source_kinds"]) == {"tertiary", "catalogue", "unavailable"}, "exclusion policy changed")
    text(reconciliation["whole_claim_rule"])
    decisions = reconciliation["rows"]
    require(len(decisions) == len({d["id"] for d in decisions}) == 24, "reconciliation ID count/collision")
    by_id = {d["id"]: d for d in decisions}
    rows = []
    effective = {}
    counted = {}
    raw_keys = set()
    entries = set()
    for document, target in zip(documents, targets):
        require(set(schema["top_level"]) <= set(document), "incomplete top-level schema")
        entry = target["entry"]
        require(document["round"] == 6 and document["baseline_revision"] == BASE and document["entry"] == entry,
                f"entry binding differs: {entry}")
        require(document["entry_sha256_before"] == baseline["entries_sha256"][entry], f"entry hash differs: {entry}")
        text(document["worker_scope"])
        require(len(document["audits"]) == len(target["questions"]) == 2, f"two fixed questions required: {entry}")
        entries.add(entry)
        for audit, question in zip(document["audits"], target["questions"]):
            row_id = question["id"]
            require(set(schema["each_audit"]) <= set(audit), f"incomplete audit: {row_id}")
            require(audit["id"] == row_id and audit["question"] == question["question"], f"fixed question changed: {row_id}")
            require(audit["verdict"] in schema["verdicts"] and audit["support_scope"] in schema["support_scopes"],
                    f"invalid worker verdict/scope: {row_id}")
            require(audit["source_kind"] in schema["source_kinds"], f"invalid source kind: {row_id}")
            for field in ("entry_locator", "entry_claim", "source_citation", "accessed_at", "retrieval_method", "basis", "coupling_implication", "limits"):
                text(audit[field])
            url(audit["source_url"])
            require(isinstance(audit["retrieved_passage"], bool), f"invalid retrieval flag: {row_id}")
            require(isinstance(audit["source_excerpt"], str) and len(audit["source_excerpt"].split()) <= 40,
                    f"invalid excerpt: {row_id}")
            if audit["retrieved_passage"]:
                raw_keys.add(passage_key(audit["source_url"], audit["source_locator"], audit["source_excerpt"]))
            decision = by_id[row_id]
            require(decision["disposition"] in {"scoped-support", "partial-support", "unresolved"}, f"invalid parent disposition: {row_id}")
            kind = decision["effective_source_kind"]
            require(kind == KIND_CORRECTIONS.get(row_id, audit["source_kind"]), f"unrecorded source-kind promotion: {row_id}")
            require(isinstance(decision["main_passage_eligible"], bool) and isinstance(decision["directly_relevant"], bool),
                    f"invalid parent relevance flags: {row_id}")
            text(decision["basis"])
            text(decision["limits"])
            source_url = decision.get("effective_source_url", audit["source_url"])
            locator = decision.get("effective_source_locator", audit["source_locator"])
            require("effective_source_url" not in decision or row_id == "R6-13-A", f"unrecorded URL substitution: {row_id}")
            require("effective_source_locator" not in decision or row_id == "R6-09-A", f"unrecorded locator substitution: {row_id}")
            effective[row_id] = {"url": source_url, "kind": kind, "entry": entry}
            if row_id == "R6-13-A":
                require(source_url == ARCHIVE_PIN, "Gobhila capture is not pinned")
            if decision["main_passage_eligible"]:
                require(audit["retrieved_passage"] and decision["directly_relevant"] and kind in ALLOWED_KINDS,
                        f"ineligible passage promoted: {row_id}")
                if urlsplit(source_url).hostname == "web.archive.org":
                    require(re.match(r"/web/\d{14}/https?://", urlsplit(source_url).path), f"unpinned archive: {row_id}")
                key = passage_key(source_url, locator, audit["source_excerpt"])
                counted.setdefault(key, {"key": list(key), "row_ids": [], "entries": []})
                counted[key]["row_ids"].append(row_id)
                if entry not in counted[key]["entries"]:
                    counted[key]["entries"].append(entry)
            rows.append(audit)
    ids = {a["id"] for a in rows}
    require(len(rows) == len(ids) == 24 and ids == set(by_id), "exact 24 fixed questions not covered")
    counted_entries = {entry for record in counted.values() for entry in record["entries"]}
    require(len(counted) >= 6, "fewer than six distinct eligible main passages")
    require(len(counted_entries) >= 4, "fewer than four eligible entries")
    checks = parent["checks"]
    require(len(checks) == len({c["id"] for c in checks}), "parent check identity collision")
    parent_keys = set()
    parent_urls = set()
    parent_entries = set()
    checks_by_id = {}
    for check in checks:
        require(check["row_id"] in ids, "parent check is not tied to a fixed question")
        require(check["result"] == "success" and check["retrieved_passage"] is True
                and check["directly_relevant_nonbibliographic"] is True, "unsuccessful/non-content parent check")
        source = effective[check["row_id"]]
        require(check["source_kind"] in ALLOWED_KINDS and check["source_kind"] == source["kind"], "parent kind mismatch")
        require(url(check["source_url"]) == url(source["url"]), "parent URL does not match effective source")
        key = passage_key(check["source_url"], check["locator"], check["excerpt"])
        for field in ("accessed_at", "retrieval_method", "basis", "language_and_mediation", "limits", "excerpt_form"):
            text(check[field])
        parent_keys.add(key)
        parent_urls.add(key[0])
        parent_entries.add(source["entry"])
        checks_by_id[check["id"]] = check
    require(len(parent_keys) >= 3 and len(parent_urls) >= 3, "fewer than three distinct parent re-fetches")
    for decision in decisions:
        for check_id in decision.get("parent_check_ids", []):
            require(check_id in checks_by_id and checks_by_id[check_id]["row_id"] == decision["id"], "parent-check cross-reference mismatch")
    require(any(c["row_id"] == "R6-13-A" and c["source_url"] == ARCHIVE_PIN for c in checks), "archive pin lacks parent receipt")
    return {"question_rows": len(rows), "source_entries": len(entries), "raw_distinct_main_keys": len(raw_keys),
            "worker_verdicts": dict(collections.Counter(a["verdict"] for a in rows)),
            "worker_scope_labels": dict(collections.Counter(a["support_scope"] for a in rows)),
            "eligible_distinct_main_passages": len(counted), "eligible_entries": len(counted_entries),
            "eligible_distinct_main_urls": len({key[0] for key in counted}),
            "excluded_main_rows": sorted(d["id"] for d in decisions if not d["main_passage_eligible"]),
            "parent_dispositions": dict(collections.Counter(d["disposition"] for d in decisions)),
            "parent_distinct_passage_checks": len(parent_keys), "parent_distinct_source_urls": len(parent_urls),
            "parent_entries": len(parent_entries), "counted_passages": sorted(counted.values(), key=lambda record: record["row_ids"])}


def selftest(inputs):
    result = measure_f(*inputs)
    require(result["eligible_distinct_main_passages"] == 20 and result["eligible_entries"] == 11,
            "positive round-6 measurement changed")
    require(result["parent_dispositions"] == {"unresolved": 4, "scoped-support": 9, "partial-support": 11},
            "positive reconciliation counts changed")
    mutations = []

    def reject(name, change, expected):
        altered = copy.deepcopy(inputs)
        change(altered)
        try:
            measure_f(*altered)
        except ValueError as error:
            require(expected in str(error), f"wrong rejection for {name}: {error}")
            mutations.append({"control": name, "rejected": True, "diagnostic": str(error)})
        else:
            raise ValueError(f"mutation survived: {name}")

    reject("missing-24th-question", lambda x: x[0][-1]["audits"].pop(), "two fixed questions")
    reject("changed-fixed-question", lambda x: x[0][0]["audits"][0].update(question="different question"), "fixed question changed")
    reject("all-passages-ineligible", lambda x: [d.update(main_passage_eligible=False) for d in x[4]["rows"]], "fewer than six")

    def collapse(values):
        for document in values[0]:
            for audit in document["audits"]:
                audit.update(source_url="https://example.org/one-passage", source_locator="one locator", source_excerpt="one passage")
        for decision in values[4]["rows"]:
            decision.pop("effective_source_locator", None)

    reject("duplicate-passage-inflation", collapse, "fewer than six")
    reject("only-two-parent-checks", lambda x: x[5].update(checks=x[5]["checks"][:2]), "fewer than three")
    reject("wildcard-archive-pin", lambda x: next(d for d in x[4]["rows"] if d["id"] == "R6-13-A").update(
        effective_source_url="https://web.archive.org/web/2023/https://sacred-texts.com/hin/sbe30/sbe30020.htm"), "capture is not pinned")
    reject("tertiary-relabelled-scholarly", lambda x: x[4]["rows"][0].update(effective_source_kind="secondary-scholarly", main_passage_eligible=True),
           "source-kind promotion")
    reject("parent-missing-excerpt", lambda x: x[5]["checks"][0].update(excerpt=""), "missing or oversized excerpt")
    reject("parent-metadata-as-content", lambda x: x[5]["checks"][0].update(directly_relevant_nonbibliographic=False), "non-content parent check")
    return {"positive_control": True, "negative_controls_passed": len(mutations), "controls": mutations,
            "limit": "In-memory receipt/count-boundary controls, not mutation tests of historical truth or general cultural validity."}


def preservation():
    old_paths = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", CHECKPOINT], cwd=ROOT, text=True).splitlines()
    counts = collections.Counter()
    for relative in old_paths:
        current = ROOT / relative
        require(current.is_file() and not current.is_symlink(), f"missing/linked historical file: {relative}")
        original = pinned(CHECKPOINT, relative)
        actual = current.read_bytes()
        if relative in APPEND_ONLY:
            require(actual.startswith(original), f"append-only prefix lost: {relative}")
            counts["prefix_preserved"] += 1
        elif relative in EDITABLE:
            counts["explicitly_editable"] += 1
        else:
            require(actual == original, f"historical file changed: {relative}")
            counts["byte_identical"] += 1
    visible = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT).decode().split("\0")
    unexpected = set(filter(None, visible)) - set(old_paths) - NEW_FILES
    require(not unexpected, f"unexpected deliverable files: {sorted(unexpected)}")
    for relative, expected in load("reports/round-6/baseline.json")["entries_sha256"].items():
        require(sha(pinned(BASE, relative)) == expected, f"baseline hash drift: {relative}")
        require((ROOT / relative).read_bytes().startswith(pinned(BASE, relative)), f"entry prefix lost: {relative}")
    return dict(counts)


def check_dispatch():
    plan = load("reports/round-6/dispatch-plan.json")
    dispatch = load("reports/round-6/dispatch.json")
    binding = load("reports/round-6/native-request-binding.json")
    require(dispatch["workers"] == dispatch["completed"] == 16 and dispatch["failed"] == 0, "dispatch incomplete")
    require(dispatch["actual_executed_batches"] == 1, "extra round-6 swarm")
    require(len(plan["items"]) == len(set(plan["items"])) == 16, "assignment count/collision")
    workers = dispatch["workers_by_assignment"]
    require(len(workers) == len({w["agent_id"] for w in workers}) == 16, "worker collision")
    require({w["assignment"] for w in workers} == {f"{i:02}" for i in range(1, 17)}
            and all(w["outcome"] == "completed" for w in workers), "worker assignment/return mismatch")
    require(len(dispatch["existing_worker_continuations"]) == 3 and all(
        w["outcome"] == "completed" and w["agent_id"] in {a["agent_id"] for a in workers}
        for w in dispatch["existing_worker_continuations"]), "continuation identity/return mismatch")
    require(plan["model"] == binding["model"] == dispatch["requested_model"] == "zai-coding-plan/glm-5.3-flash-low",
            "model route drift")
    require(plan["subagent_type"] == binding["subagent_type"] == "sec-fast-zai-flash-low", "profile route drift")
    args = {"description": "Round 6 Flash MAX source swarm", "subagent_type": plan["subagent_type"],
            "model": plan["model"], "prompt_template": (HERE / "prompt-template.txt").read_text(), "items": plan["items"]}
    digest = sha(json.dumps(args, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    require(digest == binding["canonical_args_sha256"], "native request reconstruction changed")
    return {"completed": 16, "executed_batches": 1, "existing_identity_continuations": 3,
            "canonical_args_sha256": digest, "limit": "Host request/return binding, not upstream wire identity or simultaneous runtime concurrency."}


def previous_acceptance():
    scratch = ROOT / "reports/supplement-opencode-1/scratch"
    scratch.mkdir(parents=True, exist_ok=True)
    git_dir = subprocess.check_output(["git", "rev-parse", "--absolute-git-dir"], cwd=ROOT, text=True).strip()
    with tempfile.TemporaryDirectory(prefix="round6-final-previous-", dir=scratch) as directory:
        export = Path(directory)
        for relative in ("tools", "examples", "corpus", "reports/round-5", "reports/supplement-opencode-1"):
            shutil.copytree(ROOT / relative, export / relative, ignore=shutil.ignore_patterns("scratch", "__pycache__"))
        env = {**os.environ, "GIT_DIR": git_dir, "GIT_WORK_TREE": str(export), "TMPDIR": str(scratch.resolve())}
        result = subprocess.run([sys.executable, "reports/round-5/run-validation.py"], cwd=export, env=env,
                                capture_output=True, text=True, timeout=240)
        require(result.returncode == 0, f"previous acceptance failed: {result.stdout} {result.stderr}")
        receipt = json.loads((export / "reports/round-5/validation.json").read_text())
    require(receipt["acceptance_checks_passed"], "previous acceptance receipt is red")
    return {"passed": True, "argv": [sys.executable, "reports/round-5/run-validation.py"], "exit": result.returncode,
            "cwd": "disposable copy inside ignored child scratch", "stdout": result.stdout, "stderr": result.stderr,
            "tested_file_sha256": receipt["tested_file_sha256"],
            "gate_selftests_passed": receipt["claims"]["O"]["measurement"]["gate_selftests_passed"],
            "round3_manifests_reproduced": receipt["claims"]["O"]["measurement"]["round3_manifests_reproduced"],
            "d2_findings_unchanged": receipt["claims"]["O"]["measurement"]["d2_findings_unchanged"]}


def inventory():
    argv = [sys.executable, "tools/source-audit-inventory.py", "--json", "--summary", "--root", "corpus/knowledge"]
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=60)
    require(result.returncode == 0, f"inventory failed: {result.stderr}")
    data = json.loads(result.stdout)
    partitions = dict(sorted(collections.Counter(record["path"].split("/")[0] for record in data["files"]).items()))
    require(data["totals"]["files"] == 179 and sorted(partitions.values()) == [13, 16, 16, 16, 24, 94], "coverage changed")
    require({key: data["totals"][key] for key in ("raw_lines", "raw_occurrences", "ci_occurrences", "marker_occurrences")} == {
        "raw_lines": 592, "raw_occurrences": 598, "ci_occurrences": 600, "marker_occurrences": 568}, "historical marker counts changed")
    return {"argv": argv, "exit": 0, "totals": data["totals"], "partitions": partitions,
            "limit": "Marker counts are preserved inventory, not historical truth or a quality score."}


def main():
    report = {"round": 6, "baseline_revision": BASE, "raw_records_revision": CHECKPOINT,
              "counting_command": "python3 reports/round-6/run-validation.py", "acceptance_checks_passed": False}
    try:
        report["preservation_before"] = preservation()
        claims = load("reports/round-6/claims.json")
        baseline = load("reports/round-6/baseline.json")
        targets = load("reports/round-6/targets.json")["targets"]
        paths = sorted((ROOT / "corpus/lessons/round-6-sources").glob("*.json"))
        require([p.stem for p in paths] == [f"{i:02}" for i in range(2, 14)], "fragment set differs")
        inputs = ([json.loads(p.read_text(encoding="utf-8")) for p in paths], targets, baseline, claims["source_schema"],
                  load("reports/round-6/parent-reconciliation.json"), load("reports/round-6/parent-source-spotchecks.json"))
        report["dispatch"] = check_dispatch()
        report["count_boundary_selftest"] = selftest(inputs)
        report["claims"] = {"F": {"passed": True, "measurement": measure_f(*inputs)}}
        report["previous_acceptance"] = previous_acceptance()
        report["inventory"] = inventory()
        report["preservation_after"] = preservation()
        require(report["preservation_before"] == report["preservation_after"], "preservation changed during checks")
        whitespace = subprocess.run(["git", "diff", "--check"], cwd=ROOT, capture_output=True, text=True)
        require(whitespace.returncode == 0, f"whitespace failure: {whitespace.stdout} {whitespace.stderr}")
        report["acceptance_checks_passed"] = True
    except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError) as error:
        report["error"] = str(error)
    report["limits"] = ["Receipt/schema/count/preservation and actual regression checks, not automated quotation truth or historical authenticity.",
                         "Twenty qualifying worker mains are not twenty independently parent-retrieved whole claims; five parent checks are separate.",
                         "All reviews are author-side. No canon, cultural permission, fleet closure or promotion is certified.",
                         "The historical checkpoint checker applies to its checkpoint tree; this runner permits only named append-only errata and frontier bookkeeping."]
    report["evidence_sha256"] = {relative: sha((ROOT / relative).read_bytes()) for relative in (
        "reports/round-6/run-validation.py", "reports/round-6/parent-reconciliation.json", "reports/round-6/parent-source-spotchecks.json")}
    (HERE / "validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    measurement = report.get("claims", {}).get("F", {}).get("measurement", {})
    print(json.dumps({"acceptance_checks_passed": report["acceptance_checks_passed"],
                      "F": report.get("claims", {}).get("F", {}).get("passed", False),
                      "counts": {key: value for key, value in measurement.items() if key != "counted_passages"},
                      "count_boundary_negative_controls": report.get("count_boundary_selftest", {}).get("negative_controls_passed"),
                      "preservation": report.get("preservation_after", report.get("preservation_before")),
                      "previous_acceptance_passed": report.get("previous_acceptance", {}).get("passed", False),
                      "error": report.get("error")}, ensure_ascii=False, indent=2))
    return 0 if report["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
