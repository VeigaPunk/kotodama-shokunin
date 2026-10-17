#!/usr/bin/env python3
"""Re-run the two bounded round-5 claims and the existing deliverable checks."""

import collections
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "reports/round-5"
BASE = "1ccb2b7119039d8026ad1d004f20427623838b94"
OLD_NAMES = "ottoman slavs sogdian tibet turkic africa mesoamerica color kinship orality phonetics registers lexicon".split()
FIELDS = set("previous_ledger previous_id entry entry_sha256_before claim verdict source_url source_locator source_excerpt retrieved_passage accessed_at retrieval_method basis coupling_implication limits".split())


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git_bytes(path):
    return subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT)


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def snapshot():
    paths = list((ROOT / "tools/gates").glob("*.py"))
    paths += [p for p in (ROOT / "tools/gates/fixtures").rglob("*") if p.is_file()]
    return {p.relative_to(ROOT).as_posix(): sha(p.read_bytes()) for p in paths}


def execute(argv, expected=0, *, cwd=ROOT, env=None):
    result = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, timeout=180)
    record = {"argv": argv, "cwd": "repo" if cwd == ROOT else "isolated",
              "exit": result.returncode, "stdout": result.stdout.decode("utf-8", "replace"),
              "stderr": result.stderr.decode("utf-8", "replace"),
              "stdout_sha256": sha(result.stdout)}
    require(result.returncode == expected,
            f"{argv}: expected {expected}, got {result.returncode}: {record['stdout']} {record['stderr']}")
    return record


def check_sources():
    originals = {}
    for name in OLD_NAMES:
        path = f"corpus/lessons/supplement-opencode-1/sources/{name}.json"
        require((ROOT / path).read_bytes() == git_bytes(path), f"historical ledger changed: {path}")
        document = load(path)
        for audit in document["audits"]:
            if audit["verdict"] == "unresolved":
                originals[(path, audit["id"])] = document["entry"]
    require(len(originals) == 20, "baseline unresolved set changed")
    paths = sorted((ROOT / "corpus/lessons/round-5-sources").glob("*.json"))
    require([p.name for p in paths] == [f"{i:02}.json" for i in range(4, 14)], "source fragment set differs")
    counts = collections.Counter()
    seen = set()
    rows = []
    for path in paths:
        document = json.loads(path.read_text(encoding="utf-8"))
        require(document["round"] == 5 and document["baseline_revision"] == BASE, f"wrong baseline: {path.name}")
        for position, audit in enumerate(document["audits"]):
            require(FIELDS <= set(audit), f"incomplete audit: {path.name}:{position}")
            key = (audit["previous_ledger"], audit["previous_id"])
            require(key in originals, f"not an assigned unresolved claim: {key}")
            require(audit["entry"] == originals[key], f"entry is not canonical: {key}")
            baseline = git_bytes(audit["entry"])
            require(sha(baseline) == audit["entry_sha256_before"], f"wrong entry hash: {key}")
            require((ROOT / audit["entry"]).read_bytes().startswith(baseline), f"non-append corpus edit: {key}")
            require(audit["verdict"] in {"supported", "contradicted", "unresolved"}, f"invalid verdict: {key}")
            require(isinstance(audit["retrieved_passage"], bool), f"invalid retrieval flag: {key}")
            excerpt = audit["source_excerpt"]
            require(isinstance(excerpt, str) and len(excerpt.split()) <= 40, f"excerpt over cap: {key}")
            parsed = urlsplit(audit["source_url"])
            require(parsed.scheme in {"http", "https"} and parsed.netloc and not any(c.isspace() for c in audit["source_url"]), f"not a single URL: {key}")
            require(audit["claim"] and audit["basis"] and audit["limits"] and audit["coupling_implication"], f"missing inference limits: {key}")
            if audit["retrieved_passage"]:
                require(excerpt and audit["source_locator"], f"missing passage/locator: {key}")
            counts[audit["verdict"]] += 1
            seen.add(key)
            rows.append({"ledger": path.relative_to(ROOT).as_posix(), "row": position,
                         "previous_id": audit["previous_id"], "worker_verdict": audit["verdict"],
                         "retrieved_passage": audit["retrieved_passage"]})
    require(seen == set(originals) and len(seen) >= 10, "original claim coverage incomplete")
    passages = sum(row["retrieved_passage"] for row in rows)
    require(passages >= 3, "fewer than three retrieved worker passages")
    parent = load("reports/round-5/parent-source-spotchecks.json")["checks"]
    require(len(parent) >= 3 and sum(c["directly_relevant_passage"] for c in parent) >= 3, "parent passage checks absent")
    require(sum("bibliographic" not in c["kind"] for c in parent) >= 3, "fewer than three parent non-bibliographic passages")
    for check in parent:
        require(check["excerpt"] and len(check["excerpt"].split()) <= 40 and check["locator"] and check["result"], "incomplete parent passage record")
    reconciliation = load("reports/round-5/parent-reconciliation.json")
    logical = reconciliation["logical_claims"]
    require({a["previous_id"] for a in logical} == {key[1] for key in originals} and len(logical) == 20, "logical reconciliation incomplete")
    parent_counts = collections.Counter(a["parent_verdict"] for a in logical)
    require(dict(parent_counts) == {k: v for k, v in reconciliation["parent_counts"].items() if v}, "parent counts differ")
    return {"worker_rows": len(rows), "distinct_original_claims": len(seen),
            "worker_classifications": dict(counts), "retrieved_worker_rows": passages,
            "parent_passage_checks": len(parent), "parent_whole_claim_dispositions": dict(parent_counts),
            "rows": rows}


def check_operability():
    records = []
    before = snapshot()
    records.append(execute([sys.executable, "tools/check-gate-battery.py", "--selftest"]))
    battery = execute([sys.executable, "tools/check-gate-battery.py"])
    records.append(battery)
    data = json.loads(battery["stdout"])
    require(data["summary"] == {"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}, "seven-gate battery not clean")
    require(data["originals"]["preserved"] and len(data["gates"]) == 7, "battery preservation/count differs")
    records.append(execute([sys.executable, "tools/check-craft-exercise.py", "--selftest"]))
    require("SELFTEST OK 10/10" in records[-1]["stdout"], "original ten tamper controls missing")
    require("CLI-SELFTEST OK" in records[-1]["stdout"], "real CLI controls missing")
    exercise = "examples/supplement-opencode-1/sound-change-vs-taboo.json"
    records.append(execute([sys.executable, "tools/check-craft-exercise.py", exercise, "--report", "reports/supplement-opencode-1/32-craft-exercise.md"]))
    records.append(execute([sys.executable, "tools/check-craft-exercise.py", exercise, "--counts"]))
    controls = []
    with tempfile.TemporaryDirectory(prefix="round5-cli-") as directory:
        temporary = Path(directory)
        (temporary / "invalid.json").write_text("{not json", encoding="utf-8")
        (temporary / "invalid-utf8.json").write_bytes(b"\xff")
        (temporary / "list.json").write_text("[]", encoding="utf-8")
        cases = [("missing-argument", [], "CRAFT-CLI-USAGE"),
                 ("missing-file", [str(temporary / "absent.json")], "CRAFT-CLI-NOT-FOUND"),
                 ("malformed-json", [str(temporary / "invalid.json")], "CRAFT-CLI-JSON"),
                 ("non-utf8", [str(temporary / "invalid-utf8.json")], "CRAFT-CLI-UTF8"),
                 ("wrong-root-shape", [str(temporary / "list.json")], "CRAFT-CLI-SHAPE"),
                 ("missing-report-value", [exercise, "--report"], "CRAFT-CLI-REPORT-VALUE")]
        for label, args, expected_id in cases:
            record = execute([sys.executable, "tools/check-craft-exercise.py", *args], expected=2)
            require(expected_id in record["stderr"] and "Traceback" not in record["stderr"], f"malformed control failed: {label}")
            controls.append({"case": label, "exit": 2, "diagnostic": expected_id, "traceback": False})
        tampered = load(exercise)
        derivation = tampered["exercise"]["derivations"][0]
        require(derivation["id"] == "D1" and "negative_control" in derivation, "negative-control fixture changed")
        del derivation["negative_control"]
        target = temporary / "finding.json"
        target.write_text(json.dumps(tampered), encoding="utf-8")
        finding = execute([sys.executable, "tools/check-craft-exercise.py", str(target)], expected=1)
        require("CONTROL-MISSING" in finding["stdout"], "genuine finding exit/id lost")
        records.append(finding)
        records.append(execute([sys.executable, str(ROOT / "tools/check-craft-exercise.py"), str(ROOT / exercise)], cwd=temporary))
    for manifest in ("tools/gates/frozen/round-3/MANIFEST.tsv", "tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv"):
        record = execute([sys.executable, "tools/replay-frozen.py", manifest])
        require("REPLAY OK: 7/7" in record["stdout"], "frozen replay differs")
        records.append(record)
    for relative in ("tools/replay-frozen.py", "tools/assemble-d2.py", "examples/culture-d2/packet.d2.yml"):
        require((ROOT / relative).read_bytes() == git_bytes(relative), f"no-harm surface changed: {relative}")
    require(snapshot() == before, "original gate/fixture bytes changed")
    with tempfile.TemporaryDirectory(prefix="round5-previous-acceptance-") as directory:
        export = Path(directory)
        for relative in ("tools", "examples", "corpus", "reports/supplement-opencode-1"):
            shutil.copytree(ROOT / relative, export / relative, ignore=shutil.ignore_patterns("__pycache__", "scratch"))
        git_dir = subprocess.check_output(["git", "rev-parse", "--absolute-git-dir"], cwd=ROOT, text=True).strip()
        env = {**os.environ, "GIT_DIR": git_dir, "GIT_WORK_TREE": str(export)}
        records.append(execute([sys.executable, "reports/supplement-opencode-1/run-validation.py"], cwd=export, env=env))
        previous = json.loads((export / "reports/supplement-opencode-1/validation.json").read_text())
        require(previous["acceptance_checks_passed"], "previous acceptance assertions failed")
    records.append(execute(["git", "diff", "--check"]))
    return {"gate_selftests_passed": 7, "malformed_controls": controls,
            "legacy_fixture_bytes_preserved": True, "previous_acceptance_passed": True,
            "round3_manifests_reproduced": 2, "d2_findings_unchanged": previous["d2_findings_total"],
            "commands": records}


def main():
    results = {}
    for name, function in (("F", check_sources), ("O", check_operability)):
        try:
            results[name] = {"passed": True, "measurement": function()}
        except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError) as exc:
            results[name] = {"passed": False, "error": str(exc)}
    files = [ROOT / "tools/check-craft-exercise.py", ROOT / "tools/check-gate-battery.py"]
    report = {"round": 5, "baseline_revision": BASE, "claims": results,
              "tested_file_sha256": {p.relative_to(ROOT).as_posix(): sha(p.read_bytes()) for p in files if p.is_file()},
              "acceptance_checks_passed": all(result["passed"] for result in results.values()),
              "limits": ["Worker classifications are not independent parent confirmation.",
                         "Expected red D2 verdicts remain red; safe battery wrapping does not repair legacy selftest conformance.",
                         "The previous acceptance receipt is regenerated only in an isolated copy, never overwritten in this tree."]}
    (HERE / "validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    freshness = results["F"].get("measurement", {})
    operability = results["O"].get("measurement", {})
    print(json.dumps({"acceptance_checks_passed": report["acceptance_checks_passed"],
                      "claims": {name: result["passed"] for name, result in results.items()},
                      "freshness_counts": {key: freshness[key] for key in
                          ("worker_rows", "distinct_original_claims", "retrieved_worker_rows", "parent_passage_checks", "parent_whole_claim_dispositions")
                          if key in freshness},
                      "operability_counts": {key: operability[key] for key in
                          ("gate_selftests_passed", "round3_manifests_reproduced", "d2_findings_unchanged")
                          if key in operability},
                      "errors": {name: result["error"] for name, result in results.items() if not result["passed"]}}, indent=2))
    return 0 if report["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
