#!/usr/bin/env python3
"""Check durable round-6 progress without claiming round admission."""

import collections
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "reports/round-6"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def pinned(revision, path):
    return subprocess.check_output(["git", "show", f"{revision}:{path}"], cwd=ROOT)


def check():
    baseline = load("reports/round-6/baseline.json")
    claims = load("reports/round-6/claims.json")
    plan = load("reports/round-6/dispatch-plan.json")
    dispatch = load("reports/round-6/dispatch.json")
    binding = load("reports/round-6/native-request-binding.json")
    targets = load("reports/round-6/targets.json")["targets"]
    base = baseline["baseline_revision"]
    require(dispatch["workers"] == dispatch["completed"] == 16, "dispatch incomplete")
    require(dispatch["actual_executed_batches"] == 1, "unexpected extra batch")
    require(len({w["agent_id"] for w in dispatch["workers_by_assignment"]}) == 16, "worker identity collision")
    require(all(w["outcome"] == "completed" for w in dispatch["existing_worker_continuations"]), "review continuation incomplete")
    args = {"description": "Round 6 Flash MAX source swarm", "subagent_type": plan["subagent_type"],
            "model": plan["model"], "prompt_template": (HERE / "prompt-template.txt").read_text(), "items": plan["items"]}
    digest = hashlib.sha256(json.dumps(args, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    require(digest == binding["canonical_args_sha256"], "saved native request drift")
    require(len(plan["items"]) == len(set(plan["items"])) == 16, "assignment count/collision")
    require(len(targets) == 12, "target entry count differs")
    paths = sorted((ROOT / "corpus/lessons/round-6-sources").glob("*.json"))
    require([p.stem for p in paths] == [f"{i:02}" for i in range(2, 14)], "fragment set differs")
    rows = []
    entries = set()
    keys = set()
    candidate_keys = set()
    candidate_entries = set()
    for target, path in zip(targets, paths):
        document = json.loads(path.read_text(encoding="utf-8"))
        require(set(claims["source_schema"]["top_level"]) <= set(document), f"top schema: {path.name}")
        entry = target["entry"]
        raw = pinned(base, entry)
        require(document["entry"] == entry and document["baseline_revision"] == base and document["round"] == 6, f"entry binding: {path.name}")
        require(hashlib.sha256(raw).hexdigest() == document["entry_sha256_before"] == baseline["entries_sha256"][entry], f"hash: {entry}")
        require((ROOT / entry).read_bytes() == raw, f"existing entry changed: {entry}")
        require(len(document["audits"]) == 2, f"row count: {path.name}")
        entries.add(entry)
        for question, audit in zip(target["questions"], document["audits"]):
            require(set(claims["source_schema"]["each_audit"]) <= set(audit), f"row schema: {path.name}")
            require(audit["id"] == question["id"] and audit["question"] == question["question"], f"question drift: {path.name}")
            require(audit["verdict"] in claims["source_schema"]["verdicts"] and audit["support_scope"] in claims["source_schema"]["support_scopes"], f"verdict/scope: {audit['id']}")
            require(audit["source_kind"] in claims["source_schema"]["source_kinds"], f"kind: {audit['id']}")
            url = urlsplit(audit["source_url"])
            require(url.scheme in {"http", "https"} and url.netloc and not any(c.isspace() for c in audit["source_url"]), f"URL: {audit['id']}")
            require(isinstance(audit["retrieved_passage"], bool) and len(audit["source_excerpt"].split()) <= 40, f"passage shape: {audit['id']}")
            require(all(isinstance(audit[k], str) and audit[k].strip() for k in ("entry_locator", "entry_claim", "source_citation", "retrieval_method", "basis", "coupling_implication", "limits", "accessed_at")), f"empty evidence field: {audit['id']}")
            if audit["retrieved_passage"]:
                require(audit["source_excerpt"] and audit["source_locator"], f"missing passage: {audit['id']}")
                key = (audit["source_url"], audit["source_locator"], " ".join(audit["source_excerpt"].split()))
                keys.add(key)
                if audit["source_kind"] not in {"tertiary", "catalogue", "unavailable"}:
                    candidate_keys.add(key)
                    candidate_entries.add(entry)
            rows.append(audit)
    require(len(rows) == len({a["id"] for a in rows}) == 24, "question row count/collision")
    require((ROOT / "LOG.md").read_bytes().startswith(pinned(base, "LOG.md")), "LOG prefix lost")
    old_paths = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", base, "--", "tools", "examples", "corpus", "reports"], cwd=ROOT, text=True).splitlines()
    for relative in old_paths:
        require((ROOT / relative).read_bytes() == pinned(base, relative), f"historical bytes changed: {relative}")
    scratch = ROOT / "reports/supplement-opencode-1/scratch"
    scratch.mkdir(exist_ok=True)
    git_dir = subprocess.check_output(["git", "rev-parse", "--absolute-git-dir"], cwd=ROOT, text=True).strip()
    with tempfile.TemporaryDirectory(prefix="round6-checkpoint-", dir=scratch) as directory:
        export = Path(directory)
        for relative in ("tools", "examples", "corpus", "reports/round-5", "reports/supplement-opencode-1"):
            shutil.copytree(ROOT / relative, export / relative, ignore=shutil.ignore_patterns("scratch", "__pycache__"))
        env = {**os.environ, "GIT_DIR": git_dir, "GIT_WORK_TREE": str(export)}
        result = subprocess.run([sys.executable, "reports/round-5/run-validation.py"], cwd=export, env=env, capture_output=True, text=True, timeout=180)
        require(result.returncode == 0, f"previous acceptance failed: {result.stdout} {result.stderr}")
        previous = json.loads((export / "reports/round-5/validation.json").read_text())
    subprocess.run(["git", "diff", "--check"], cwd=ROOT, check=True, capture_output=True)
    return {"checkpoint_checks_passed": True, "round6_admission": "pending", "workers_completed": 16,
            "source_fragments": len(paths), "question_rows": len(rows), "source_entries": len(entries),
            "worker_verdicts": dict(collections.Counter(a["verdict"] for a in rows)),
            "worker_scope_labels": dict(collections.Counter(a["support_scope"] for a in rows)),
            "distinct_main_passage_keys": len(keys), "nontertiary_main_candidates": len(candidate_keys),
            "candidate_entries": len(candidate_entries), "historical_files_preserved": len(old_paths),
            "previous_acceptance_passed": previous["acceptance_checks_passed"],
            "previous_tested_code_sha256": previous["tested_file_sha256"],
            "limit": "Mechanical checkpoint checks do not establish quotation truth, source relevance, independent verification or F admission. Parent re-fetches, reconciliation and the declared run-validation.py remain pending."}


def main():
    try:
        receipt = check()
    except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError) as error:
        receipt = {"checkpoint_checks_passed": False, "round6_admission": "pending", "error": str(error)}
    (HERE / "checkpoint-validation.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    return 0 if receipt["checkpoint_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
