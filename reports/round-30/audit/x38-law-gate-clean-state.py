#!/usr/bin/env python3
"""R30-X38: read-only clean-state spot-check with real law-gate controls."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[3]
GATE = "tools/gates/register-law-gate.py"
PACKET = "examples/culture-d4/packet.d4.yml"
TYPED = "examples/culture-d4/packet.d4.typed.yml"
LAW_IDS = ["RGL-%02d" % i for i in range(1, 6)]
INPUTS = [GATE, "tools/gates/naming-collision-gate.py", PACKET, TYPED,
          "examples/culture-d4/typed-labels.d4.yml",
          "examples/culture-d4/expected-holds.json", "tools/gates/typed-pipelines.json",
          "tools/assemble-culture-d4.py", "tools/assemble-d4-typed.py",
          "tools/gates/typed-pipeline-gate.py",
          "tools/gates/argot-derivation-gate.py"]


def now():
    return datetime.now(timezone.utc).isoformat()


def run(argv):
    started = now()
    proc = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True,
                          env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
                          timeout=180)
    return {"command": " ".join(str(part) for part in argv),
            "started_at_utc": started, "finished_at_utc": now(),
            "exit": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}


def python(*args):
    return run(["python3", "-B", *args])


def digests():
    paths = [ROOT / relative for relative in INPUTS]
    paths.extend(sorted((ROOT / "examples/culture-d4/components").glob("*.yml")))
    paths.extend(sorted((ROOT / "examples/culture-d4").glob("expected-holds*.json")))
    return {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in paths if path.is_file()}


def snapshot():
    before = digests()
    calls = [(GATE, "--packet", PACKET), (GATE, "--packet", TYPED),
             (GATE, "--selftest")]
    with ThreadPoolExecutor(max_workers=len(calls)) as executor:
        results = list(executor.map(lambda args: python(*args), calls))
    return {"measured_at_utc": now(), "inputs_before": before,
            "inputs_after": digests(),
            "runs": dict(zip(("raw", "typed", "selftest"), results))}


def packet_clean(reading):
    return (reading["inputs_before"] == reading["inputs_after"]
            and all(reading["runs"][key]["exit"] == 0 for key in ("raw", "typed"))
            and all("FINDING " not in reading["runs"][key]["stdout"]
                    for key in ("raw", "typed")))


def ready(reading):
    return packet_clean(reading) and reading["runs"]["selftest"]["exit"] == 0


def full_yaml(packet):
    result = run(["ruby", "-ryaml", "-rjson", "-e",
                  "puts JSON.generate(YAML.load_file(ARGV[0]))", packet])
    if result["exit"]:
        raise RuntimeError(result["stderr"])
    document = json.loads(result["stdout"])
    ids = {str(row["id"]) for block in document.values() if isinstance(block, list)
           for row in block if isinstance(row, dict) and row.get("id")}
    law = document.get("register_law") or []
    refs = [{"row": row.get("id"), "field": field, "target": token,
             "resolved": token in ids}
            for row in law for field in ("design_row", "design_rows")
            for token in (row.get(field) if isinstance(row.get(field), list)
                          else [row[field]] if row.get(field) else [])]
    return {"command": result["command"], "measured_at_utc": result["finished_at_utc"],
            "record_ids": len(ids), "law_ids": [row.get("id") for row in law],
            "register_ids": [row.get("id") for row in document.get("registers", [])],
            "design_references": refs,
            "unresolved_references": [row for row in refs if not row["resolved"]],
            "law_fields": [{key: row.get(key) for key in
                            ("id", "act", "speaker", "holder", "force", "consequence")}
                           for row in law]}


def replace_field(text, field, value):
    block = re.search(r"(?ms)^register_law:\n.*?(?=^\S|\Z)", text)
    if not block:
        raise RuntimeError("register_law block not found")
    law = block.group(0)
    pattern = r"(?m)^(    %s:)[^\n]*(?:\n      -[^\n]*)*" % re.escape(field)
    replaced, count = re.subn(pattern, lambda match: match[1] + " " + value,
                              law, count=1)
    if count != 1 or replaced == law:
        raise RuntimeError("could not plant %s control" % field)
    return text[:block.start()] + replaced + text[block.end():]


def controls():
    text = (ROOT / PACKET).read_text(encoding="utf-8")
    specs = [
        ("dangling", "design_row", '["ZZ-99"]', "D4L-LAW-DANGLING", "HOLD"),
        ("force", "force", '"no-such-force"', "D4L-LAW-FORCE", "FAIL"),
        ("speaker-id", "speaker", '"nobody-nowhere (ZZ-99)"', "D4L-LAW-SPEAKER", "FAIL"),
        ("speaker-tokenless", "speaker", '"nobody-nowhere"', "D4L-LAW-SPEAKER", "FAIL"),
        ("consequence", "consequence", '"the act evaporates silently"',
         "D4L-LAW-CONSEQUENCE", "FAIL"),
    ]
    with tempfile.TemporaryDirectory(prefix="r30-x38-", dir=os.environ["TMPDIR"]) as temp:
        paths = []
        for name, field, value, expected, level in specs:
            path = Path(temp) / (name + ".yml")
            path.write_text(replace_field(text, field, value), encoding="utf-8")
            paths.append(path)
        with ThreadPoolExecutor(max_workers=len(paths)) as executor:
            runs = list(executor.map(lambda path: python(GATE, "--packet", str(path)), paths))
    results = []
    for (name, field, value, expected, level), result in zip(specs, runs):
        lines = [line for line in result["stdout"].splitlines() if line.startswith("FINDING ")]
        targeted = [line for line in lines
                    if line.startswith("FINDING %s: %s" % (expected, level))
                    and "RGL-01" in line]
        results.append({"name": name, "field": field, "value": value,
                        "expected_class": expected, "expected_level": level,
                        "passed": result["exit"] == 1 and bool(targeted),
                        "finding_lines": lines, **result})
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wait", type=int, default=0, choices=range(0, 1201))
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    scratch = ROOT / ".scratch"
    if Path(os.environ.get("TMPDIR", "")).resolve() != scratch:
        parser.error("export TMPDIR=$PWD/.scratch before running")
    scratch.mkdir(exist_ok=True)
    started = now()
    deadline = time.monotonic() + args.wait
    history = []
    while True:
        reading = snapshot()
        history.append(reading)
        summary = {key: value["exit"] for key, value in reading["runs"].items()}
        print("%s law-gate exits=%s" % (now(), json.dumps(summary)), file=sys.stderr, flush=True)
        if ready(reading) or time.monotonic() + 60 > deadline:
            break
        time.sleep(60)
    before = digests()
    with ThreadPoolExecutor(max_workers=7) as executor:
        independent = list(executor.map(full_yaml, (PACKET, TYPED)))
        calls = [("assembly", ("tools/assemble-culture-d4.py", "--check")),
                 ("typed-assembly", ("tools/assemble-d4-typed.py", "--check")),
                 ("typed-pipeline", ("tools/gates/typed-pipeline-gate.py", PACKET)),
                 ("argot", ("tools/gates/argot-derivation-gate.py", PACKET))]
        futures = [(name, executor.submit(python, *argv)) for name, argv in calls]
        controls_future = executor.submit(controls)
        regressions = {name: future.result() for name, future in futures}
        planted = controls_future.result()
    after = digests()
    final = snapshot()
    checks = {
        "raw-and-typed-clean": packet_clean(final),
        "law-selftest": final["runs"]["selftest"]["exit"] == 0,
        "independent-reference-resolution": all(not row["unresolved_references"]
                                                 for row in independent),
        "five-law-rows-preserved": all(row["law_ids"] == LAW_IDS for row in independent),
        "typed-law-surface-matches-raw": all(independent[0][key] == independent[1][key]
                                            for key in ("law_fields", "design_references")),
        "controls": all(row["passed"] for row in planted),
        "regressions": all(row["exit"] == 0 for row in regressions.values()),
        "stable-inputs": before == after == final["inputs_after"] == final["inputs_before"],
    }
    report = {"seat": "R30-X38", "axis": "operability",
              "command": "export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1; "
                         + " ".join(["python3", "-B", *sys.argv]),
              "started_at_utc": started, "finished_at_utc": now(),
              "head": run(["git", "rev-parse", "HEAD"])["stdout"].strip(),
              "history": history, "final": final,
              "independent_yaml": dict(zip(("raw", "typed"), independent)),
              "controls": planted, "regressions": regressions,
              "checks": checks, "passed": all(checks.values()),
              "limitations": ["This spot-check is not whole-round admission or canon clearance.",
                              "The independent parser is Ruby YAML; no lane parser is imported.",
                              "Controls are temporary packet copies, not edits to delivered artifacts."]}
    payload = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.receipt:
        target = args.receipt.resolve()
        if target.parent != Path(__file__).resolve().parent or not target.name.startswith("x38-"):
            parser.error("receipt must be an x38-* file alongside this instrument")
        target.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    print("X38 %s checks=%s controls=%d/%d" %
          ("PASS" if report["passed"] else "NOT-GREEN", json.dumps(checks),
           sum(row["passed"] for row in planted), len(planted)), file=sys.stderr)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
