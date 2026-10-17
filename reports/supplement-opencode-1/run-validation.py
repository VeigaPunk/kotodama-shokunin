#!/usr/bin/env python3
"""Re-run this supplemental wave's bounded acceptance checks from the repo root."""

import collections
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
BASE = "fe34faaafbe0add59ff68827a0df6c5782a72404"
HERE = ROOT / "reports/supplement-opencode-1"
NAMES = "ottoman slavs sogdian tibet turkic africa mesoamerica color kinship orality phonetics registers lexicon".split()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def execute(argv, *, cwd=ROOT, expected=0):
    result = subprocess.run(argv, cwd=cwd, capture_output=True, timeout=120)
    record = {
        "argv": argv,
        "cwd": "repo" if cwd == ROOT else "isolated-export",
        "exit": result.returncode,
        "stdout": result.stdout.decode("utf-8", "replace"),
        "stderr": result.stderr.decode("utf-8", "replace"),
        "stdout_sha256": sha(result.stdout),
    }
    if result.returncode != expected:
        raise AssertionError(f"{argv}: expected {expected}, got {result.returncode}: {record['stdout']} {record['stderr']}")
    return record


def main():
    checks = []
    for script in ("tools/assemble-d2.py", "tools/replay-frozen.py", "tools/source-audit-inventory.py"):
        checks.append(execute([sys.executable, script, "--selftest"]))
    checks.append(execute([sys.executable, "tools/assemble-d2.py", "--check"]))
    replay = execute([sys.executable, "tools/replay-frozen.py", "tools/gates/frozen/round-3/MANIFEST.tsv", "--json"])
    assert json.loads(replay["stdout"])["summary"]["reproduced"] == 7
    checks.append(replay)
    checks.append(execute([sys.executable, "tools/replay-frozen.py", "tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv"]))

    fixture_before = {p.relative_to(ROOT).as_posix(): sha(p.read_bytes())
                      for p in (ROOT / "tools/gates/fixtures").rglob("*") if p.is_file()}
    with tempfile.TemporaryDirectory(prefix="kotodama-gate-export-") as directory:
        export = Path(directory)
        shutil.copytree(ROOT / "tools/gates", export / "tools/gates",
                        ignore=shutil.ignore_patterns("__pycache__", "frozen"))
        gates = sorted((export / "tools/gates").glob("*.py"))
        assert len(gates) == 7
        for gate in gates:
            checks.append(execute([sys.executable, gate.relative_to(export).as_posix(), "--selftest"], cwd=export))
    fixture_after = {p.relative_to(ROOT).as_posix(): sha(p.read_bytes())
                     for p in (ROOT / "tools/gates/fixtures").rglob("*") if p.is_file()}
    assert fixture_before == fixture_after
    assert not subprocess.check_output(["git", "diff", "--name-only", BASE, "--", "tools/gates"], cwd=ROOT).strip()

    domain = []
    for gate in ("phonology-sanity-gate", "lexicon-coverage-audit", "myth-consistency-gate", "costume-era-consistency-gate", "naming-collision-gate"):
        expected = 1 if gate in {"phonology-sanity-gate", "naming-collision-gate"} else 0
        result = execute([sys.executable, f"tools/gates/{gate}.py", "examples/culture-d2/packet.d2.yml"], expected=expected)
        classes = collections.Counter(line.split(":", 1)[0].removeprefix("FINDING ")
                                      for line in result["stdout"].splitlines() if line.startswith("FINDING "))
        result["finding_classes"] = dict(classes)
        result["finding_count"] = sum(classes.values())
        if gate == "naming-collision-gate":
            assert classes == {"NAME-NEAR": 6, "PHON-INVENTORY": 10, "CROSS-HOLD": 1}, classes
        domain.append(result)
    checks.append(execute([sys.executable, "tools/gates/handoff-packet-check.py", "examples/handoff-packet.sample.md"]))
    checks.append(execute([sys.executable, "tools/check-craft-exercise.py", "examples/supplement-opencode-1/sound-change-vs-taboo.json", "--report", "reports/supplement-opencode-1/32-craft-exercise.md"]))
    checks.append(execute([sys.executable, "tools/check-craft-exercise.py", "--selftest"]))

    verdicts = collections.Counter()
    audit_ids = set()
    entry_reports = []
    for name in NAMES:
        path = ROOT / "corpus/lessons/supplement-opencode-1/sources" / f"{name}.json"
        record = json.loads(path.read_text())
        entry = record["entry"]
        baseline = subprocess.check_output(["git", "show", f"{BASE}:{entry}"], cwd=ROOT)
        assert sha(baseline) == record["entry_sha256_before"], name
        assert (ROOT / entry).read_bytes().startswith(baseline), name
        assert record["baseline_revision"] == BASE
        for audit in record["audits"]:
            key = (entry, audit["id"])
            assert key not in audit_ids
            audit_ids.add(key)
            assert audit["verdict"] in {"supported", "contradicted", "unresolved"}
            assert audit["claim"] and audit["source_url"] and audit["basis"]
            assert len(audit["source_excerpt"].split()) <= 40
            if audit["verdict"] != "unresolved":
                assert audit["source_excerpt"] and audit["source_locator"]
            verdicts[audit["verdict"]] += 1
        entry_reports.append({"entry": entry, "ledger": path.relative_to(ROOT).as_posix(),
                              "audits": len(record["audits"]), "append_only": True})
    assert len(audit_ids) >= 10
    parent_checks = json.loads((HERE / "parent-source-spotchecks.json").read_text())["checks"]
    assert len(parent_checks) >= 5

    inventory_run = execute([sys.executable, "tools/source-audit-inventory.py", "--json", "--summary", "--root", "corpus/knowledge"])
    inventory = json.loads(inventory_run["stdout"])
    totals = inventory["totals"]
    assert totals["files"] == 179
    index = (ROOT / "corpus/README.md").read_text()
    assert "Total knowledge entries: 179." in index
    assert "## civilizations/ (94)" in index
    assert "- `africa-primary-sources.md`" in index
    checks.append(execute(["git", "diff", "--check"]))
    pinned_inputs = [ROOT / "tools/assemble-d2.py", ROOT / "tools/replay-frozen.py",
                     ROOT / "tools/source-audit-inventory.py", ROOT / "tools/check-craft-exercise.py",
                     ROOT / "examples/culture-d2/packet.d2.yml"]
    report = {
        "wave": "supplement-opencode-1", "baseline_revision": BASE,
        "tested_file_sha256": {p.relative_to(ROOT).as_posix(): sha(p.read_bytes()) for p in pinned_inputs},
        "checks": checks, "legacy_fixture_bytes_unchanged": True,
        "legacy_selftests_run_in_isolation": 7, "source_audits": entry_reports,
        "source_verdicts": dict(verdicts), "source_audits_total": len(audit_ids),
        "parent_passage_spotchecks": len(parent_checks),
        "inventory_totals": totals, "d2_gate_results": domain,
        "d2_findings_total": sum(item["finding_count"] for item in domain),
        "limits": ["148 worker verdicts are not 148 independent parent confirmations; five source rows were re-fetched by parent.",
                   "Expected red design verdicts are retained, not failed test assertions or culture clearance.",
                   "Legacy corpus metadata, parser coverage, fixture selftest side effects, per-gate expected.json layout and lore receipt remain debts.",
                   "Supplemental wave does not replace the three numbered non-flash Z.ai rounds."],
        "acceptance_checks_passed": True,
    }
    (HERE / "validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"acceptance_checks_passed": True, "source_audits": len(audit_ids),
                      "source_verdicts": dict(verdicts), "selftests": "7 legacy + assembler + replay + inventory + craft",
                      "round3_replay": "7/7", "d2_findings": report["d2_findings_total"],
                      "raw_marker_lines": totals["raw_lines"]}, indent=2))


if __name__ == "__main__":
    main()
