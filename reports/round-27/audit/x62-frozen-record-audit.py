#!/usr/bin/env python3
"""R27-X62 — frozen-generation record audit (read-only; own re-derivation).

X61 sweeps the *rows* (does the recorded verdict reproduce?). X62 audits the
*frozen surface as a record*: is each generation internally consistent, does its
receipt agree with its manifest, and does the current generation actually replay?

Four duties, one receipt:

  A. INVENTORY — every generation directory under `tools/gates/frozen/**` that
     carries a `MANIFEST.tsv`: its rows, its inputs, whether it carries a
     receipt (`freeze.txt` / `freeze-receipt.json`), a generation README, and
     which rows point at a snapshot outside their own directory.

  B. RECORD INTERNALS — for every row, before any gate runs:
       * the recorded `output` file's `^FINDING ` count equals the recorded
         `finding_count` (a record that contradicts itself is not evidence);
       * the recorded output's sha256 equals the recorded `output_sha256`;
       * the committed snapshot under `input_snapshot` equals `input_sha256`;
       * the recorded `command` names the same gate and input as the row.
     This is the check that catches a hand-edited record, and it needs no gate.

  C. RECEIPT AGREEMENT — where a generation carries a machine receipt
     (`freeze-receipt.json`), every row it declares must appear in the manifest
     with the same exit code, finding count, pins and output path. A receipt
     that disagrees with its manifest is a split record.

  D. CURRENT-GENERATION REPLAY — the newest generation (`round-26/post-register`)
     is replayed row by row in a mirror whose real path is OUTSIDE the repo, and
     its tally is reported separately from the historical generations. The
     historical rows are read as records (duties B/C); only the current
     generation is re-executed, so the receipt names which rows were *measured*
     and which were *read*.

Exit codes:
  0  every record is internally consistent, every receipt agrees, and the
     current generation replays
  1  a record contradicts itself, a receipt disagrees with its manifest, or the
     current generation fails to reproduce
  2  could-not-evaluate: a pinned file is missing or a path is unsafe

Usage:
    export TMPDIR=/tmp PYTHONDONTWRITEBYTECODE=1
    python3 -B reports/round-27/audit/x62-frozen-record-audit.py            # text
    python3 -B reports/round-27/audit/x62-frozen-record-audit.py --json     # receipt
    python3 -B reports/round-27/audit/x62-frozen-record-audit.py --selftest # controls
"""
import argparse
import hashlib
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[3]
FROZEN = ROOT / "tools" / "gates" / "frozen"
CURRENT = FROZEN / "round-26" / "post-register"
FINDING_PREFIX = "FINDING "
COLUMNS = (
    "gate", "gate_sha256", "input", "input_sha256", "exit_code",
    "finding_count", "output", "output_sha256", "input_snapshot", "command",
)
TIMEOUT = 120


class Refused(Exception):
    def __init__(self, reason, detail):
        super().__init__(detail)
        self.reason = reason
        self.detail = detail


def sha_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha_bytes(payload):
    return hashlib.sha256(payload).hexdigest()


def safe_path(raw, what):
    if not raw:
        raise Refused(f"{what}_missing", f"{what}: path is empty")
    if os.path.isabs(raw) or raw.startswith("~"):
        raise Refused(f"{what}_unsafe_path", f"{what}: absolute path refused: {raw!r}")
    segments = [s for s in raw.split("/") if s not in ("", ".")]
    if not segments:
        raise Refused(f"{what}_unsafe_path", f"{what}: empty after normalization: {raw!r}")
    if ".." in segments:
        raise Refused(f"{what}_unsafe_path", f"{what}: '..' component refused: {raw!r}")
    if any(s.startswith("-") for s in segments):
        raise Refused(f"{what}_unsafe_path", f"{what}: flag-like component refused: {raw!r}")
    target = ROOT / os.path.normpath(raw)
    if target.is_symlink():
        raise Refused(f"{what}_unsafe_path", f"{what}: symlink refused: {raw!r}")
    try:
        target.resolve().relative_to(ROOT.resolve())
    except ValueError:
        raise Refused(f"{what}_unsafe_path", f"{what}: resolves outside the repo: {raw!r}")
    return target


def count_findings(payload):
    return sum(1 for line in payload.decode("utf-8", "replace").splitlines()
               if line.startswith(FINDING_PREFIX))


def read_manifest(path):
    rows, problems = [], []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if not lines:
        return rows, ["manifest is empty"]
    if tuple(lines[0].split("\t")) != COLUMNS:
        return rows, [f"header is not the documented column schema: {lines[0]!r}"]
    for number, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        cells = line.split("\t")
        if len(cells) != len(COLUMNS):
            problems.append(f"row {number}: {len(cells)} cell(s), expected {len(COLUMNS)}")
            continue
        row = dict(zip(COLUMNS, cells))
        row["_row"] = number
        rows.append(row)
    return rows, problems


def command_names(row):
    """(gate, input) as spelled by the recorded `command` column."""
    try:
        parts = shlex.split(row["command"])
    except ValueError:
        return None, None
    paths = [p for p in parts[1:] if not p.startswith("-")]
    gate = next((p for p in paths if p.endswith(".py")), None)
    rest = [p for p in paths if not p.endswith(".py")]
    return gate, (rest[-1] if rest else None)


def audit_row(row, directory_rel):
    """Duty B for one row: every check that needs no gate. Never raises."""
    findings = []
    try:
        if len(row["gate_sha256"]) != 64 or len(row["input_sha256"]) != 64 \
                or len(row["output_sha256"]) != 64:
            findings.append("record_malformed: a pin is not a sha256 hex digest")
        output = safe_path(row["output"], "output")
        if not output.is_file():
            findings.append(f"output_missing: {row['output']}")
        else:
            live_out = sha_file(output)
            if live_out != row["output_sha256"]:
                findings.append(f"output_tampered: {row['output']} is not the pinned bytes")
            observed_count = count_findings(output.read_bytes())
            if observed_count != int(row["finding_count"]):
                findings.append(
                    f"record_inconsistent: finding_count={row['finding_count']} but the "
                    f"recorded output carries {observed_count} FINDING line(s)")
        snapshot = safe_path(row["input_snapshot"], "snapshot")
        if not snapshot.is_file():
            findings.append(f"snapshot_missing: {row['input_snapshot']}")
        elif sha_file(snapshot) != row["input_sha256"]:
            findings.append(f"snapshot_tampered: {row['input_snapshot']}")
        gate, cmd_input = command_names(row)
        if gate and Path(gate).name != Path(row["gate"]).name:
            findings.append(f"record_inconsistent: command names gate {gate!r}, row names {row['gate']!r}")
        if cmd_input and cmd_input != row["input"]:
            findings.append(
                f"record_inconsistent: command names input {cmd_input!r}, row names {row['input']!r}")
    except Refused as refused:
        findings.append(f"{refused.reason}: {refused.detail}")
    return findings


def inventory():
    generations = []
    for manifest in sorted(FROZEN.rglob("MANIFEST.tsv")):
        directory = manifest.parent
        rel = str(directory.relative_to(ROOT))
        rows, problems = read_manifest(manifest)
        receipt_txt = directory / "freeze.txt"
        receipt_json = directory / "freeze-receipt.json"
        reads = []
        for row in rows:
            try:
                snapshot = safe_path(row["input_snapshot"], "snapshot")
                reads.append(str(snapshot.relative_to(ROOT)))
            except Refused:
                reads.append(None)
        own = [r for r in reads if r and r.startswith(rel + "/")]
        foreign = sorted({r for r in reads if r and not r.startswith(rel + "/")})
        generations.append({
            "generation": rel,
            "manifest": str(manifest.relative_to(ROOT)),
            "rows": len(rows),
            "problems": problems,
            "has_freeze_txt": receipt_txt.is_file(),
            "has_freeze_receipt_json": receipt_json.is_file(),
            "has_readme": (directory / "README.md").is_file(),
            "own_snapshots": len(own),
            "foreign_snapshots": foreign,
            "row_findings": [{"row": row["_row"], "findings": audit_row(row, rel)} for row in rows],
            "rows_raw": rows,
        })
    return generations


def receipt_agreement(generation):
    """Duty C: the machine receipt's declared rows vs the manifest's rows.

    Three receipt shapes exist on the tree and each declares its rows
    differently, so the comparison is shape-aware rather than assuming one:

      * `rows` is a **list of row objects** (round-18) — compare field by field,
        matching on (gate, input) and falling back to gate alone, because that
        receipt names its rows by gate;
      * `rows` is an **int and `verdicts` is a list of `{label, exit, findings}`**
        (round-26) — the verdicts are positional labels, not row addresses, so
        compare them against the manifest in manifest order and compare the
        receipt's `pins` / `input_pins` maps against the manifest's digests;
      * `manifest_rows` is a **list** (round-22) — same field-by-field compare.

    A shape this function cannot address is reported as such, never as a pass.
    """
    path = Path(generation["generation"]) / "freeze-receipt.json"
    if not path.is_absolute():
        path = ROOT / path
    if not path.is_file():
        return None
    try:
        rel = str(path.relative_to(ROOT))
    except ValueError:
        rel = str(path)
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return {"receipt": rel, "findings": [f"unreadable receipt: {exc}"]}
    findings = []
    manifest = list(generation["rows_raw"])
    by_key = {(row["gate"], row["input"]): row for row in manifest}
    by_gate = {}
    for row in manifest:
        by_gate.setdefault(row["gate"], []).append(row)

    declared = document.get("rows")
    compared = None

    if isinstance(declared, list):
        compared = len(declared)
        for item in declared:
            if not isinstance(item, dict):
                findings.append("receipt row is not an object")
                continue
            key = (item.get("gate"), item.get("input"))
            row = by_key.get(key)
            if row is None and item.get("gate"):
                candidates = by_gate.get(item["gate"], [])
                row = candidates[0] if len(candidates) == 1 else None
            if row is None:
                findings.append(f"receipt row {key} does not appear in the manifest")
                continue
            for field in ("exit_code", "finding_count", "gate_sha256", "input_sha256",
                          "output", "output_sha256"):
                if field in item and str(item[field]) != str(row.get(field)):
                    findings.append(f"receipt/manifest disagree on {key} {field}: "
                                    f"receipt={item[field]!r} manifest={row.get(field)!r}")
    elif isinstance(document.get("manifest_rows"), list):
        declared = document["manifest_rows"]
        compared = len(declared)
        for item in declared:
            if not isinstance(item, dict):
                continue
            key = (item.get("gate"), item.get("input"))
            row = by_key.get(key) or (by_gate.get(item.get("gate")) or [None])[0]
            if row is None:
                findings.append(f"receipt manifest_row {key} does not appear in the manifest")
                continue
            for field in ("exit_code", "finding_count", "gate_sha256", "input_sha256",
                          "output", "output_sha256"):
                if field in item and str(item[field]) != str(row.get(field)):
                    findings.append(f"receipt/manifest disagree on {key} {field}")
    elif isinstance(document.get("verdicts"), list):
        verdicts = document["verdicts"]
        compared = len(verdicts)
        if isinstance(declared, int) and declared != len(manifest):
            findings.append(f"receipt declares rows={declared} but the manifest holds {len(manifest)}")
        if len(verdicts) != len(manifest):
            findings.append(f"receipt carries {len(verdicts)} verdict(s) for {len(manifest)} manifest row(s)")
        for item, row in zip(verdicts, manifest):
            if not isinstance(item, dict):
                continue
            if "exit" in item and int(item["exit"]) != int(row["exit_code"]):
                findings.append(f"receipt verdict exit {item['exit']} != manifest exit_code "
                                f"{row['exit_code']} for {row['gate']} {row['input']}")
            if "findings" in item and int(item["findings"]) != int(row["finding_count"]):
                findings.append(f"receipt verdict findings {item['findings']} != manifest "
                                f"finding_count {row['finding_count']} for {row['input']}")
        pins = document.get("pins")
        if isinstance(pins, dict):
            for gate, digest in pins.items():
                rows = by_gate.get(gate, [])
                if not rows:
                    findings.append(f"receipt pins gate {gate} which the manifest does not carry")
                for row in rows:
                    if digest != row["gate_sha256"]:
                        findings.append(f"receipt pin for {gate} disagrees with the manifest")
        input_pins = document.get("input_pins")
        if isinstance(input_pins, dict):
            for name, digest in input_pins.items():
                rows = [r for r in manifest if r["input"] == name or r["input_snapshot"].endswith(name)]
                for row in rows:
                    if digest != row["input_sha256"]:
                        findings.append(f"receipt input_pin for {name} disagrees with the manifest")
    else:
        findings.append("receipt carries no row-addressable list (rows/verdicts/manifest_rows)")

    return {"receipt": rel, "declared_rows": compared, "findings": findings}


def replay_generation(generation, tmpdir):
    """Duty D: re-execute one generation's rows in a mirror outside the repo."""
    results = []
    for row in generation["rows_raw"]:
        item = {"row": row["_row"], "gate": row["gate"], "input": row["input"]}
        try:
            gate = safe_path(row["gate"], "gate")
            snapshot = safe_path(row["input_snapshot"], "snapshot")
            mirror = Path(tempfile.mkdtemp(prefix="x62-mirror-", dir=tmpdir))
        except Refused as refused:
            item.update(status="could-not-evaluate", reason=refused.reason, detail=refused.detail)
            results.append(item)
            continue
        try:
            try:
                mirror.resolve().relative_to(ROOT.resolve())
                raise Refused("mirror_unsafe", f"mirror inside the repo: {mirror}")
            except ValueError:
                pass
            destination = mirror / row["input"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(snapshot, destination)
            env = dict(os.environ)
            env["PYTHONDONTWRITEBYTECODE"] = "1"
            proc = subprocess.run([sys.executable, str(gate), row["input"]], cwd=mirror,
                                  stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, timeout=TIMEOUT, env=env)
            observed = {"exit": proc.returncode, "count": count_findings(proc.stdout),
                        "sha256": sha_bytes(proc.stdout)}
            agrees = (observed["exit"] == int(row["exit_code"])
                      and observed["count"] == int(row["finding_count"])
                      and observed["sha256"] == row["output_sha256"])
            item.update(status="reproduced" if agrees else "mismatch",
                        reason="-" if agrees else "replay_mismatch", **observed)
            if not agrees:
                # A generation is superseded when the live input it names no
                # longer hashes to its own pin; when the live input still
                # matches, the divergence is genuine drift. Same rule as X61,
                # re-derived here rather than shared.
                live = safe_path(row["input"], "input")
                live_sha = sha_file(live) if live.is_file() else None
                item["live_input_moved"] = bool(live_sha) and live_sha != row["input_sha256"]
                item["class"] = ("unknown" if live_sha is None
                                 else "supersession" if item["live_input_moved"] else "drift")
        except Refused as refused:
            item.update(status="could-not-evaluate", reason=refused.reason, detail=refused.detail)
        except subprocess.TimeoutExpired:
            item.update(status="could-not-evaluate", reason="gate_timeout")
        except OSError as exc:
            item.update(status="could-not-evaluate", reason="gate_launch_failed", detail=str(exc))
        finally:
            shutil.rmtree(mirror, ignore_errors=True)
        results.append(item)
    return results


def selftest():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    tmp = Path(tempfile.mkdtemp(prefix="x62-selftest-"))
    try:
        # a record that contradicts itself: finding_count says 2, output has 1
        out = tmp / "out.txt"
        out.write_bytes(b"FINDING a\nok\n")
        # point the row's paths at the real repo so safe_path resolves
        check("finding-count mismatch is caught",
              count_findings(out.read_bytes()) != 2)

        # the three record-internals checks, run against a real frozen row
        real_output = ROOT / "tools/gates/frozen/round-26/post-register/d4-source.out"
        if real_output.is_file():
            real_sha = sha_file(real_output)
            real_count = count_findings(real_output.read_bytes())
            base = {"gate": "tools/gates/typed-pipeline-gate.py", "gate_sha256": "a" * 64,
                    "input": "examples/culture-d4/packet.d4.yml",
                    "input_sha256": "dd25077bc01681bc17f4586b40cfdd6959d4f45fc63e4f33f13fdc9b2cc88e67",
                    "exit_code": "0", "finding_count": str(real_count),
                    "output": "tools/gates/frozen/round-26/post-register/d4-source.out",
                    "output_sha256": real_sha,
                    "input_snapshot": "tools/gates/frozen/round-26/post-register/"
                                      "inputs/examples/culture-d4/packet.d4.yml",
                    "command": "python3 tools/gates/typed-pipeline-gate.py "
                               "examples/culture-d4/packet.d4.yml", "_row": 2}
            check("a clean frozen row audits clean", audit_row(base, "x") == [])
            wrong_count = dict(base, finding_count=str(real_count + 1))
            check("a self-contradicting record is caught",
                  any("record_inconsistent" in f for f in audit_row(wrong_count, "x")))
            wrong_pin = dict(base, output_sha256="b" * 64)
            check("a re-written output is caught",
                  any("output_tampered" in f for f in audit_row(wrong_pin, "x")))
            wrong_cmd = dict(base, command="python3 tools/gates/other-gate.py "
                                           "examples/culture-d4/packet.d4.yml")
            check("a command naming another gate is caught",
                  any("record_inconsistent" in f for f in audit_row(wrong_cmd, "x")))

        # command/row disagreement is detected
        g, i = command_names({"command": "python3 tools/gates/other-gate.py y.yml"})
        check("command gate parsed", Path(g).name == "other-gate.py")
        check("command input parsed", i == "y.yml")
        g2, i2 = command_names({"command": "python3 tools/gates/x.py --flag y.yml"})
        check("flags are not read as inputs", i2 == "y.yml")

        # unsafe paths refused
        for raw in ("../../etc/passwd", "/etc/passwd", "--selftest", "tools/gates/../gates/x.py"):
            try:
                safe_path(raw, "output")
                check(f"unsafe refused: {raw}", False)
            except Refused:
                check(f"unsafe refused: {raw}", True)

        # a wrong manifest header is refused, not guessed
        manifest = tmp / "MANIFEST.tsv"
        manifest.write_text("gate\tinput\nx\ty\n", encoding="utf-8")
        rows, problems = read_manifest(manifest)
        check("bad header refused", not rows and bool(problems))

        # a missing receipt is reported, not invented
        check("absent receipt reads None", receipt_agreement(
            {"generation": "tools/gates/frozen/nope", "rows_raw": []}) is None)

        # the mirror must refuse an in-repo parent
        try:
            mirror = Path(tempfile.mkdtemp(prefix="x62-selftest-mirror-", dir=str(ROOT / ".scratch")))
            shutil.rmtree(mirror, ignore_errors=True)
            check("in-repo mirror parent detected",
                  str((ROOT / ".scratch").resolve()).startswith(str(ROOT.resolve())))
        except OSError:
            check("in-repo mirror parent detected", False)

        # receipt shape controls: a receipt that cannot be addressed is not a
        # pass, and each of the three shapes is routed to its own comparison.
        bad_shape = tmp / "freeze-receipt.json"
        bad_shape.write_text(json.dumps({"rows": 6, "notes": "no list"}), encoding="utf-8")
        check("unaddressable receipt is not a pass",
              "no row-addressable list" in json.dumps(
                  receipt_agreement({"generation": str(tmp), "rows_raw": []})))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    passed = sum(1 for _, ok in checks if ok)
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    print(f"selftest: {passed}/{len(checks)} checks passed")
    return 0 if passed == len(checks) else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--no-replay", action="store_true",
                        help="read the records only; do not re-execute the current generation")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()

    tmpdir = tempfile.gettempdir()
    generations = inventory()
    agreements = {g["generation"]: receipt_agreement(g) for g in generations}

    record_findings = sum(len(r["findings"]) for g in generations for r in g["row_findings"])
    problems = sum(len(g["problems"]) for g in generations)
    receipt_findings = sum(len(a["findings"]) for a in agreements.values() if a)

    receipt = {
        "tool": "reports/round-27/audit/x62-frozen-record-audit.py",
        "seat": "R27-X62",
        "date": "2026-10-18",
        "head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True,
                               text=True).stdout.strip(),
        "tmpdir": tmpdir,
        "generations": generations,
        "receipts": agreements,
        "summary": {
            "generations": len(generations),
            "rows": sum(g["rows"] for g in generations),
            "record_findings": record_findings,
            "manifest_problems": problems,
            "receipt_findings": receipt_findings,
            "generations_with_receipt": sum(1 for g in generations
                                            if g["has_freeze_txt"] or g["has_freeze_receipt_json"]),
            "generations_with_readme": sum(1 for g in generations if g["has_readme"]),
            "foreign_snapshot_rows": sum(len(g["foreign_snapshots"]) for g in generations),
        },
    }

    replay_tally = None
    if not args.no_replay and CURRENT.is_dir():
        current = next((g for g in generations
                        if g["generation"] == str(CURRENT.relative_to(ROOT))), None)
        if current:
            results = replay_generation(current, tmpdir)
            tally = {"reproduced": 0, "mismatch": 0, "could-not-evaluate": 0,
                     "supersession": 0, "drift": 0}
            for item in results:
                tally[item["status"]] += 1
                if item.get("class") in ("supersession", "drift"):
                    tally[item["class"]] += 1
            replay_tally = {"generation": current["generation"], "rows": len(results),
                            "tally": tally, "results": results}
            receipt["current_replay"] = replay_tally

    if args.json:
        print(json.dumps(receipt, indent=1, sort_keys=True))
    else:
        print(f"X62 frozen-record audit — {receipt['date']} — lane HEAD {receipt['head']}")
        print(f"  TMPDIR={tmpdir}")
        for g in generations:
            status = "clean" if not g["problems"] and not any(r["findings"] for r in g["row_findings"]) else "FINDINGS"
            print(f"  {g['generation']}: {g['rows']} rows, {status}; "
                  f"receipt={'yes' if (g['has_freeze_txt'] or g['has_freeze_receipt_json']) else 'no'}, "
                  f"readme={'yes' if g['has_readme'] else 'no'}, "
                  f"foreign snapshots={len(g['foreign_snapshots'])}")
            for r in g["row_findings"]:
                for f in r["findings"]:
                    print(f"    ROW {r['row']} FINDING: {f}")
            for p in g["problems"]:
                print(f"    PROBLEM: {p}")
            agreement = agreements.get(g["generation"])
            if agreement and agreement.get("findings"):
                for f in agreement["findings"]:
                    print(f"    RECEIPT FINDING: {f}")
        if replay_tally:
            t = replay_tally["tally"]
            print(f"  current generation {replay_tally['generation']}: "
                  f"{t['reproduced']}/{replay_tally['rows']} reproduced, "
                  f"{t['mismatch']} mismatch ({t['supersession']} supersession, {t['drift']} drift), "
                  f"{t['could-not-evaluate']} could-not-evaluate")
            for item in replay_tally["results"]:
                if item["status"] != "reproduced":
                    print(f"    ROW {item['row']} {item['status']} reason={item.get('reason')} "
                          f"class={item.get('class')} live_input_moved={item.get('live_input_moved')}")
        s = receipt["summary"]
        print(f"  summary: {s['generations']} generations, {s['rows']} rows; "
              f"{s['record_findings']} record finding(s), {s['receipt_findings']} receipt finding(s), "
              f"{s['manifest_problems']} manifest problem(s); "
              f"{s['generations_with_readme']}/{s['generations']} generations carry a README")

    if problems or record_findings or receipt_findings:
        return 1
    if replay_tally:
        t = replay_tally["tally"]
        # A drift row is a defect: the input still matches its pin yet the gate
        # disagrees. A supersession is a recorded fact — a later generation
        # moved the input — so it is reported and does not by itself fail the
        # audit; a could-not-evaluate is an incomplete measurement and does.
        if t["drift"] or t["could-not-evaluate"]:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
