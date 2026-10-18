#!/usr/bin/env python3
"""Independent Round-30 operability sweep; prior rounds are read-only."""
from __future__ import annotations

import argparse
import concurrent.futures
import copy
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import runpy
import shlex
import stat
import subprocess
import sys
import tempfile
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "reports/round-30"
SCRIPT = "reports/round-30/verify-operability.py"
COMMAND = f"python3 {SCRIPT}"
BASELINE = "87bfc9956f0fc60e6821fe53b622d0043e28be10"
PACKET = "examples/culture-d4/packet.d4.yml"
LAW = "tools/gates/register-law-gate.py"
ENTRY = "corpus/knowledge/linguistics/register-lexicon-ceilings.md"
PROTECTED = tuple(f"reports/round-{n}" for n in range(8, 30)) + tuple(
    f"tools/gates/frozen/round-{n}" for n in range(8, 30)
)
REGRESSIONS = (
    ("battery-selftest", "tools/check-gate-battery.py", "--selftest"),
    ("battery", "tools/check-gate-battery.py"),
    ("craft-selftest", "tools/check-craft-exercise.py", "--selftest"),
    ("craft-positive", "tools/check-craft-exercise.py", "examples/supplement-opencode-1/sound-change-vs-taboo.json"),
    ("links-selftest", "tools/harness/packet_links.py", "--selftest"),
    ("uncertainty-selftest", "tools/harness/packet_uncertainty.py", "--selftest"),
    ("d2-assembly", "tools/assemble-d2.py", "--check"),
    ("d2-assembly-selftest", "tools/assemble-d2.py", "--selftest"),
    ("d2-typed-assembly", "tools/assemble-d2-typed.py", "--check"),
    ("d2-typed-assembly-selftest", "tools/assemble-d2-typed.py", "--selftest"),
    ("d3-assembly", "tools/assemble-culture-d3.py", "--check"),
    ("d3-assembly-selftest", "tools/assemble-culture-d3.py", "--selftest"),
    ("d4-assembly", "tools/assemble-culture-d4.py", "--check"),
    ("d4-assembly-selftest", "tools/assemble-culture-d4.py", "--selftest"),
    ("d4-typed-assembly", "tools/assemble-d4-typed.py", "--check"),
    ("d4-typed-assembly-selftest", "tools/assemble-d4-typed.py", "--selftest"),
    ("projector-selftest", "tools/d2-typed-labels.py", "--selftest"),
    ("d2-projection", "tools/d2-typed-labels.py", "--check"),
    ("d4-projection", "tools/d2-typed-labels.py", "--packet", PACKET, "--check", "examples/culture-d4/typed-labels.d4.yml"),
    ("d4-typed-gate", "tools/gates/d4-typed-labels-check-gate.py", "examples/culture-d4/typed-labels.d4.yml"),
    ("d4-assembly-gate", "tools/gates/d4-assembly-check-gate.py", PACKET),
    ("typed-pipeline-selftest", "tools/gates/typed-pipeline-gate.py", "--selftest"),
    ("typed-pipeline-d2", "tools/gates/typed-pipeline-gate.py", "examples/culture-d2/packet.d2.yml"),
    ("typed-pipeline-d4", "tools/gates/typed-pipeline-gate.py", PACKET),
    ("typed-pipeline-typed-d4", "tools/gates/typed-pipeline-gate.py", "examples/culture-d4/packet.d4.typed.yml"),
    ("argot-selftest", "tools/gates/argot-derivation-gate.py", "--selftest"),
    ("argot-d4", "tools/gates/argot-derivation-gate.py", PACKET),
    ("law-selftest", LAW, "--selftest"),
    ("law-clean", LAW, "--packet", PACKET),
    ("handoff-v2", "tools/exercise-handoff-e2e.py", "--profile", "v2", "--quiet"),
    ("handoff-v2-selftest", "tools/exercise-handoff-e2e.py", "--profile", "v2", "--selftest", "--quiet"),
    ("handoff-v3", "tools/exercise-handoff-e2e.py", "--profile", "v3", "--quiet"),
    ("handoff-v3-selftest", "tools/exercise-handoff-e2e.py", "--profile", "v3", "--selftest", "--quiet"),
    ("coupling-selftest", "tools/check-evidence-coupling.py", "--selftest"),
    ("coupling-d3", "tools/check-evidence-coupling.py", "examples/culture-d3/packet.json"),
    ("frozen-replay-selftest", "tools/replay-frozen.py", "--selftest"),
    ("pin-repoint-selftest", "reports/round-26/remainders/pin-repoint-check.py", "--selftest"),
    ("r28-sweep-selftest", "reports/round-28/sweep/sweep.py", "--selftest"),
    ("ceiling-selftest", "reports/round-28/ceiling/measure-ceiling.py", "--selftest"),
    ("ceiling-measurement", "reports/round-28/ceiling/measure-ceiling.py"),
)
EXTERNAL_TMP = {"frozen-replay-selftest", "r28-sweep-selftest"}


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def source_snapshot():
    paths = {ROOT / "AGENTS.md", ROOT / ENTRY}
    for suffix in ("*.py", "*.json"):
        paths.update((ROOT / "tools").rglob(suffix))
    for directory in (HERE / "telemetry", HERE / "fixes"):
        paths.update(p for p in directory.rglob("*") if p.is_file() and p.suffix in (".py", ".json", ".md"))
    for family in ("culture-d2", "culture-d3", "culture-d4"):
        paths.update(p for p in (ROOT / "examples" / family).rglob("*")
                     if p.is_file() and p.suffix in (".yml", ".json", ".md"))
    return {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in sorted(paths) if p.is_file()}


def protected_snapshot():
    entries = git("ls-tree", "-r", "-z", BASELINE, "--", *PROTECTED).split(b"\0")
    manifest, differences = {}, []
    for entry in entries:
        if not entry:
            continue
        metadata, rawpath = entry.split(b"\t", 1)
        expected_mode, _, expected_oid = metadata.decode().split()
        relative = os.fsdecode(rawpath)
        path = ROOT / relative
        try:
            mode = path.lstat().st_mode
            data = os.readlink(path).encode() if stat.S_ISLNK(mode) else path.read_bytes()
            live_mode = "120000" if stat.S_ISLNK(mode) else ("100755" if mode & 0o111 else "100644")
            oid = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
            manifest[relative] = {"sha256": digest(data), "mode": live_mode}
            if (live_mode, oid) != (expected_mode, expected_oid):
                differences.append(relative)
        except OSError:
            differences.append(relative)
    status = git("status", "--porcelain=v1", "-uall", "--", *PROTECTED).decode().splitlines()
    return {"date": utc()[:10], "command": f"{COMMAND} (git ls-tree baseline blob/mode comparison)",
            "baseline_revision": BASELINE, "paths_checked": len(manifest),
            "manifest_sha256": digest(json.dumps(manifest, sort_keys=True).encode()),
            "differences": differences, "status_rows": status,
            "passed": not differences and not status}


def run(name, argv, env=None):
    child_env = dict(os.environ if env is None else env)
    child_env["PYTHONDONTWRITEBYTECODE"] = "1"
    child_env["TMPDIR"] = "/var/tmp" if name in EXTERNAL_TMP else str(ROOT / ".scratch")
    start = utc()
    begun = time.monotonic()
    try:
        result = subprocess.run(argv, cwd=ROOT, env=child_env, capture_output=True,
                                text=True, errors="replace", timeout=240)
        code, stdout, stderr = result.returncode, result.stdout, result.stderr
    except (OSError, subprocess.TimeoutExpired) as exc:
        code, stdout, stderr = None, "", f"{type(exc).__name__}: {exc}"
    return {"name": name, "command": shlex.join(argv), "date": start[:10],
            "started_at_utc": start, "finished_at_utc": utc(),
            "seconds": round(time.monotonic() - begun, 3), "tmpdir": child_env["TMPDIR"],
            "exit_code": code, "passed": code == 0,
            "stdout_sha256": digest(stdout.encode()), "stderr_sha256": digest(stderr.encode()),
            "stdout": stdout, "stderr": stderr}


def sweep():
    before, sources_before = protected_snapshot(), source_snapshot()
    matrix = REGRESSIONS + (("typed-pipeline-generalized-selftest", "tools/gates/typed-pipeline-gate.py", "--selftest-generalized"),)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(run, row[0], ["python3", "-B", *row[1:]]) for row in matrix]
        all_rows = [future.result() for future in futures]
    rows = [row for row in all_rows if row["name"] != "r28-sweep-selftest"]
    historical = next(row for row in all_rows if row["name"] == "r28-sweep-selftest")
    try:
        controls = json.loads(historical["stdout"])["controls"]
        failed = [row["control"] for row in controls if not row["passed"]]
        accepted = ({"r28-generation-replays-green"},
                    {"r28-generation-replays-green", "hold-walker-finds-the-committed-hold-set"})
        historical["expected_later_tree_drift"] = historical["exit_code"] == 1 and set(failed) in accepted
        historical["failed_controls"] = failed
    except (ValueError, KeyError, TypeError):
        historical["expected_later_tree_drift"] = False
    historical["disposition"] = "The immutable R28 selftest replays the superseded R28 generation. Its hold walker also does not recognize the old current packet after successor-row repinning. These actual reds remain red; current typed-pipeline successor pins are tested separately."
    after, sources_after = protected_snapshot(), source_snapshot()
    moved = sorted(p for p in sources_before.keys() | sources_after.keys()
                   if sources_before.get(p) != sources_after.get(p))
    unchanged = before["manifest_sha256"] == after["manifest_sha256"]
    return {"round": 30, "assignment": "R30-O13", "date": utc()[:10],
            "counting_command": f"{COMMAND} --regressions-only", "head": git("rev-parse", "HEAD").decode().strip(),
            "commands_executed": len(all_rows), "commands_total": len(rows),
            "commands_passed": sum(row["passed"] for row in rows),
            "all_commands_green": all(row["passed"] for row in all_rows),
            "all_current_regressions_green": all(row["passed"] for row in rows),
            "historical_controls": [historical],
            "source_drift": moved, "input_sha256": sources_after,
            "protected_before": before, "protected_after": after,
            "protected_unchanged": unchanged, "results": rows,
            "passed": all(row["passed"] for row in rows) and historical["expected_later_tree_drift"]
                      and before["passed"] and after["passed"] and unchanged and not moved,
            "limits": ["Historical acceptance runners and receipt-writing gate-test runners are not run.",
                       "The R28 frozen-generation selftest is retained separately, with its actual nonzero exit and failed controls.",
                       "The flagless D4 adapters are exercised through their actual input CLI, not a nonexistent --selftest.",
                       "Battery coverage is digest/pin validation, not frozen verdict replay."]}


def finding_lines(row):
    return sorted(line.strip() for line in row["stdout"].splitlines() if line.startswith("FINDING D4L-LAW-"))


def mutate_law(text, field, value):
    lines = text.splitlines(keepends=True)
    in_law, changes = False, 0
    for index, line in enumerate(lines):
        if re.match(r"^register_law:\s*$", line.rstrip()):
            in_law = True
            continue
        if in_law and line.strip() and not line.startswith((" ", "#")):
            break
        if not in_law:
            continue
        if field == "design_row":
            pattern = r"\bdesign_row:\s*\[[^\]\n]*\]"
            replacement = "design_row: [QREG-99]"
        else:
            pattern = r'\b' + re.escape(field) + r':\s*(?:"(?:[^"\\]|\\.)*"|[^,}\n]+)'
            replacement = field + ": " + json.dumps(value)
        changed, amount = re.subn(pattern, lambda _: replacement, line, count=1)
        if amount:
            lines[index], changes = changed, 1
            break
    return "".join(lines), changes


def law_probes():
    text = (ROOT / PACKET).read_text()
    clean = run("independent-law-clean", ["python3", "-B", LAW, "--packet", PACKET])
    probes = {"clean": clean}
    with tempfile.TemporaryDirectory(prefix="r30-o14-law-", dir=ROOT / ".scratch") as tmp:
        for name, field, value, expected in (
            ("dangling", "design_row", "QREG-99", "D4L-LAW-DANGLING"),
            ("tokenless-speaker", "speaker", "no-such-speaker", "D4L-LAW-SPEAKER"),
            ("token-speaker", "speaker", "stamp-holder (ZZ-99)", "D4L-LAW-SPEAKER"),
            ("force", "force", "no-such-force", "D4L-LAW-FORCE"),
            ("consequence", "consequence", "the act evaporates silently", "D4L-LAW-CONSEQUENCE"),
        ):
            tampered, changed = mutate_law(text, field, value)
            target = Path(tmp) / f"{name}.yml"
            target.write_text(tampered)
            row = run(name, ["python3", "-B", LAW, "--packet", str(target.relative_to(ROOT))])
            added = sorted(set(finding_lines(row)) - set(finding_lines(clean)))
            row.update({"mutated_rows": changed, "expected_finding": expected,
                        "added_finding_lines": added,
                        "passed": changed == 1 and row["exit_code"] == 1
                                  and any(expected + ":" in line for line in added)})
            probes[name] = row
    return probes


def battery_probe():
    module = runpy.run_path(str(ROOT / "tools/check-gate-battery.py"))
    names = tuple(module["REGISTERED_GATE_NAMES"])
    law_registered = "register-law-gate.py" in names
    with tempfile.TemporaryDirectory(prefix="r30-o14-battery-", dir=ROOT / ".scratch") as tmp:
        root = Path(tmp)
        for name in names:
            if name == "register-law-gate.py":
                continue
            baseline = root / name
            baseline.mkdir()
            packet = b"independent negative-control snapshot\n"
            (baseline / "packet.txt").write_bytes(packet)
            (baseline / "expected.json").write_text(json.dumps({
                "schema": "kotodama-frozen-run-v1", "gate": name,
                "gate_sha256": digest((ROOT / "tools/gates" / name).read_bytes()),
                "inputs": {"packet.txt": digest(packet)},
                "expected": {"exit": 0, "class": "clean", "findings": []}}))
        row = run("law-baseline-omitted", ["python3", "-B", "tools/check-gate-battery.py", "--baselines-root", str(root)])
        try:
            report = json.loads(row["stdout"])
            uncovered = report["baselines"]["summary"]["gates_uncovered"]
            coverage = report["baselines"]["summary"]["coverage"]
        except (KeyError, ValueError, TypeError):
            uncovered, coverage = None, None
        row.update({"registered_gates": list(names), "registered_count": len(names),
                    "coverage_with_law_baseline_omitted": coverage, "uncovered": uncovered,
                    "passed": law_registered and len(names) == len(set(names)) == 10
                              and row["exit_code"] == 2 and uncovered == ["register-law-gate.py"]
                              and coverage == "9/10"})
    return row


def ceiling_probe():
    baseline = git("show", f"{BASELINE}:{ENTRY}")
    live = (ROOT / ENTRY).read_bytes()
    companion_path = HERE / "fixes/x63-f2.md"
    companion = companion_path.read_text() if companion_path.is_file() else ""
    appended = live[len(baseline):].decode(errors="replace") if live.startswith(baseline) else ""
    correction = appended + "\n" + companion
    witness = git("show", "6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede:corpus/knowledge/linguistics/sound-symbolism.md").decode()
    hits = [i for i, line in enumerate(witness.splitlines(), 1) if "which semantic fields" in line.lower()]
    markers = {"original_bytes_preserved": live.startswith(baseline),
               "new_correction_section_or_file": bool(appended.strip() or companion.strip()),
               "names_finding": bool(re.search(r"X63-F2|A29-ADJ-EVID-01", correction)),
               "names_preexisting_witness": "sound-symbolism.md:106" in correction,
               "withdraws_false_absence_evidence": "withdraw this phrase as evidence" in correction,
               "dated_command": bool(re.search(r"2026-10-\d{2}", correction)) and "python3" in correction,
               "false_zero_control": hits == [106] and "ideophones" in witness.splitlines()[105]}
    return {"date": utc()[:10], "command": f"{COMMAND} (preserved corpus and new-file amendment control)",
            "source": ENTRY, "amendment": "reports/round-30/fixes/x63-f2.md",
            "baseline_sha256": digest(baseline), "live_sha256": digest(live),
            "amendment_sha256": digest(companion.encode()),
            "appended_corpus_bytes": len(live) - len(baseline), "checks": markers,
            "control": {"command": "git show 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede:corpus/knowledge/linguistics/sound-symbolism.md (case-insensitive phrase census)",
                        "date": utc()[:10], "matching_lines": hits, "matches": len(hits),
                        "original_zero_assertion_rejected": bool(hits)},
            "passed": all(markers.values()),
            "scope_note": "The authorized companion file qualifies the original statement; the historical auditor does not consume amendments and remains finding-bearing."}


def telemetry_probe():
    import shutil

    agents = (ROOT / "AGENTS.md").read_text()
    directory = HERE / "telemetry"
    paths = sorted(p for p in directory.rglob("*") if p.is_file()) if directory.is_dir() else []
    records, errors = [], []
    for path in paths:
        if path.suffix not in (".json", ".jsonl"):
            continue
        try:
            text = path.read_text()
            data = json.loads(text) if path.suffix == ".json" else [json.loads(line) for line in text.splitlines() if line.strip()]
            records.append({"path": str(path.relative_to(ROOT)), "sha256": digest(path.read_bytes()), "nonempty": bool(data)})
        except (ValueError, OSError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    rule = "reports/round-<N>/telemetry/" in agents and "never only `.scratch`" in agents
    commands = []
    for name, script, flags in (
        ("durable-telemetry-check", "dispatch-telemetry.py", ["--check"]),
        ("durable-telemetry-selftest", "dispatch-telemetry.py", ["--selftest"]),
        ("declaration-telemetry-selftest", "check-dispatch.py", ["--selftest"]),
    ):
        if (directory / script).is_file():
            commands.append(run(name, ["python3", "-B", str((directory / script).relative_to(ROOT)), *flags]))
    independent = []
    snapshot_path = directory / "dispatch-stats.json"
    if snapshot_path.is_file() and (directory / "dispatch-telemetry.py").is_file():
        with tempfile.TemporaryDirectory(prefix="r30-o14-telemetry-", dir=ROOT / ".scratch") as temporary:
            mirror = Path(temporary)
            shutil.copytree(directory, mirror / "reports/round-30/telemetry")
            shutil.copy2(ROOT / "AGENTS.md", mirror / "AGENTS.md")
            ephemeral = mirror / ".scratch"
            ephemeral.mkdir()
            (ephemeral / "sample.json").write_text("{}\n")
            shutil.rmtree(ephemeral)
            argv = ["python3", "-B", str(mirror / "reports/round-30/telemetry/dispatch-telemetry.py"), "--check"]
            clean = run("independent-telemetry-without-scratch", argv)
            independent.append(clean)
            snapshot = mirror / "reports/round-30/telemetry/dispatch-stats.json"
            original = snapshot.read_bytes()
            candidate = json.loads(original)
            candidate["sources"]["declared_request"]["path"] = ".scratch/claims.json"
            snapshot.write_text(json.dumps(candidate))
            negative = run("independent-scratch-only-telemetry", argv)
            negative["passed"] = negative["exit_code"] == 1 and "non-durable-or-wrong-source:declared_request" in negative["stdout"]
            independent.append(negative)
            snapshot.write_bytes(original)
            raw = mirror / "reports/round-30/telemetry/inputs/claims.json"
            raw.write_bytes(raw.read_bytes() + b"\n")
            negative = run("independent-telemetry-raw-tamper", argv)
            negative["passed"] = negative["exit_code"] == 1 and "source-digest-mismatch:declared_request" in negative["stdout"]
            independent.append(negative)
    return {"date": utc()[:10], "command": f"{COMMAND} (durable CLI replay plus independent scratch/tamper controls)",
            "agents_sha256": digest((ROOT / "AGENTS.md").read_bytes()),
            "convention_present": rule, "directory": "reports/round-30/telemetry/",
            "durable_files": [{"path": str(p.relative_to(ROOT)), "bytes": p.stat().st_size,
                               "sha256": digest(p.read_bytes())} for p in paths],
            "json_records": records, "errors": errors, "commands": commands, "independent_controls": independent,
            "passed": rule and bool(records) and all(row["nonempty"] for row in records) and not errors
                      and len(commands) >= 2 and all(row["passed"] for row in commands)
                      and len(independent) == 3 and all(row["passed"] for row in independent),
            "scope_note": "A durable partial/declaration snapshot is not a provider availability percentage or recovery of lost R25-R28 raw telemetry."}


def verify(regressions):
    before, sources_before = protected_snapshot(), source_snapshot()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        law_future = pool.submit(law_probes)
        battery_future = pool.submit(battery_probe)
        ceiling_future = pool.submit(ceiling_probe)
        telemetry_future = pool.submit(telemetry_probe)
        law, battery, ceiling, telemetry = [f.result() for f in (law_future, battery_future, ceiling_future, telemetry_future)]
    battery_live = next(row for row in regressions["results"] if row["name"] == "battery")
    try:
        summary = json.loads(battery_live["stdout"])["baselines"]["summary"]
    except (KeyError, ValueError, TypeError):
        summary = {}
    live_coverage = summary.get("coverage")
    items = [
        {"id": "R30-QREG-DANGLES", "owner": "R30-O01..O03 register-law packet owner",
         "passed": law["clean"]["exit_code"] == 0 and not finding_lines(law["clean"]) and law["dangling"]["passed"],
         "control": "law.dangling", "evidence": [PACKET, "examples/culture-d4/components/04-lexicon.yml", "reports/round-30/fixes/qreg-dangles.md"],
         "reason": "Require a clean delivered packet plus an independently introduced dangling design_row finding."},
        {"id": "R30-LAW-BATTERY", "owner": "R30-O04..O06 battery owner + orchestrator baseline owner",
         "passed": battery_live["passed"] and live_coverage == "10/10" and battery["passed"],
         "control": "battery_omission", "evidence": ["tools/check-gate-battery.py", "reports/round-30/fixes/battery-registration.md"],
         "reason": "Require the default battery at 10/10 and an omitted-law-baseline CLI control at exit 2, 9/10."},
        {"id": "R30-X63-F2", "owner": "R30-O07..O08 ceilings amendment owner",
         "passed": ceiling["passed"], "control": "ceilings.control", "evidence": [ENTRY, "reports/round-30/fixes/x63-f2.md"],
         "reason": "Require preserved original bytes, a new qualifying amendment section or companion file, and the preexisting witness."},
        {"id": "R30-SPEAKER-TAMPER", "owner": "R30-O09..O10 candidate owner + orchestrator tool integrator",
         "passed": law["clean"]["exit_code"] == 0 and law["tokenless-speaker"]["passed"] and law["token-speaker"]["passed"]
                   and next(row for row in regressions["results"] if row["name"] == "law-selftest")["passed"],
         "control": "law.tokenless-speaker + law.token-speaker", "evidence": [LAW, "reports/round-30/fixes/speaker-tamper.md"],
         "reason": "Require a new speaker finding on one tokenless law-row mutation, not an ID-bearing substitute."},
        {"id": "R30-TELEMETRY-DURABILITY", "owner": "R30-O11..O12 telemetry convention owner",
         "passed": telemetry["passed"], "control": "telemetry", "evidence": ["AGENTS.md", "reports/round-30/fixes/telemetry-convention.md", "reports/round-30/telemetry/dispatch-stats.json"],
         "reason": "Require the operating rule, durable replay after scratch removal, and scratch-only/changed-byte rejection; historical raw loss remains explicit."},
    ]
    after, sources_after = protected_snapshot(), source_snapshot()
    previous = regressions["input_sha256"]
    moved = sorted(p for p in sources_before.keys() | sources_after.keys() | previous.keys()
                   if sources_before.get(p) != sources_after.get(p) or previous.get(p) != sources_before.get(p))
    return {"round": 30, "assignment": "R30-O14", "date": utc()[:10], "counting_command": COMMAND,
            "measured_at_utc": utc(), "runner_sha256": digest(Path(__file__).read_bytes()),
            "regression_receipt": "reports/round-30/regression.json", "regressions_green": regressions["passed"],
            "items": items, "law": law, "battery_omission": battery, "default_battery_coverage": live_coverage,
            "ceilings": ceiling, "telemetry": telemetry, "source_drift": moved,
            "protected_before": before, "protected_after": after,
            "passed": regressions["passed"] and all(row["passed"] for row in items) and all(row["passed"] for row in law.values())
                      and before["passed"] and after["passed"] and before["manifest_sha256"] == after["manifest_sha256"] and not moved,
            "scope_note": "Independent O13-O15 verification only, not Round-30 C/D acceptance or promotion."}


def selftest():
    text = 'registers:\n  - {id: QREG-01, speaker: "outside"}\nregister_law:\n  - {id: RGL-01, speaker: "office (RK-03)", force: "directive-binding", consequence: "roll", design_row: [RK-03]}\nother:\n  speaker: "outside-after"\n'
    checks = []
    changed, count = mutate_law(text, "speaker", "no-such-speaker")
    checks.append(("one-law-row-not-register-row", count == 1 and 'speaker: "outside"' in changed and 'speaker: "no-such-speaker"' in changed))
    checks.append(("later-block-untouched", 'speaker: "outside-after"' in changed))
    changed, count = mutate_law(text, "design_row", "QREG-99")
    checks.append(("design-row-probe", count == 1 and "design_row: [QREG-99]" in changed))
    changed, count = mutate_law("registers:\n  speaker: x\n", "speaker", "no-such-speaker")
    checks.append(("no-law-does-not-pass-mutation", count == 0))
    checks.append(("finding-only-comparison", finding_lines({"stdout": "coverage: x\nFINDING D4L-LAW-SPEAKER: FAIL x\n"}) == ["FINDING D4L-LAW-SPEAKER: FAIL x"]))
    checks.append(("unique-matrix-labels", len({row[0] for row in REGRESSIONS}) == len(REGRESSIONS)))
    checks.append(("mirror-safety-explicit", EXTERNAL_TMP <= {row[0] for row in REGRESSIONS}))
    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    print(f"selftest: {sum(ok for _, ok in checks)}/{len(checks)}; command={COMMAND} --selftest; date={utc()[:10]}")
    return 0 if all(ok for _, ok in checks) else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="print JSON without writing round receipts")
    parser.add_argument("--regressions-only", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--wait", type=int, default=0, help="poll integration every 60s, capped at 1200s")
    args = parser.parse_args()
    if args.wait < 0:
        parser.error("--wait must be nonnegative")
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    if args.selftest:
        return selftest()
    deadline = time.monotonic() + min(args.wait, 1200)
    while True:
        started = time.monotonic()
        regressions = sweep()
        receipt = regressions if args.regressions_only else verify(regressions)
        remaining = deadline - time.monotonic()
        if receipt["passed"] or remaining <= 0:
            break
        print(f"integration pending: {regressions['commands_passed']}/{regressions['commands_total']} current commands green", file=sys.stderr, flush=True)
        time.sleep(min(max(0, 60 - (time.monotonic() - started)), remaining))
    if args.check:
        print(json.dumps(receipt, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        (HERE / "regression.json").write_text(json.dumps(regressions, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
        if not args.regressions_only:
            (HERE / "operability-verification.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
        print(f"commands: {regressions['commands_passed']}/{regressions['commands_total']}; source_drift={regressions['source_drift']}")
        if not args.regressions_only:
            for item in receipt["items"]:
                print(f"{item['id']}: {'PASS' if item['passed'] else 'NOT YET VERIFIED'}")
        print(f"passed: {receipt['passed']}")
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
