#!/usr/bin/env python3
"""R28-X62 — frozen replay audit (read-only; own re-derivation).

Seat R28-X62 (SCRIBE X62: replay audit) for round 28, claim O
(`operability`, `final-pin-sweep`; `reports/round-28/claims.json`). NON-CANON
engineering evidence. This tool admits nothing and certifies no round.

X61 asks *does the recorded verdict reproduce?* — the row question. X62 asks
*is the frozen surface a sound record?* — the generation question. The two are
independent: a record can be internally consistent and still not replay, and a
row can replay while its record contradicts itself.

This is the round-28 successor of `reports/round-27/audit/x62-frozen-record-audit.py`.
It keeps round-27's four duties and adds two, each of which round-27 named as a
finding but could not measure:

  A. INVENTORY — every generation directory carrying a `MANIFEST.tsv`, its rows,
     its receipt, its README, and which rows read a snapshot outside their own
     directory. Scope is the round-28 X61 scope: `tools/gates/frozen/**` **and**
     `reports/**/tests/frozen/**` (finding X61R28-A1).
  B. RECORD INTERNALS — per row, with no gate launched: the recorded output's
     `^FINDING ` count against `finding_count`, the output's digest against
     `output_sha256`, the snapshot against `input_sha256`, and the recorded
     `command` against the row's own gate and input.
  C. RECEIPT AGREEMENT — where a generation carries `freeze-receipt.json`, every
     row it declares must agree with the manifest. Three receipt shapes exist on
     this tree and each is handled shape-aware; an unaddressable shape is
     reported, never read as a pass.
  D. CURRENT-GENERATION REPLAY — the newest generation is re-executed row by row
     in a mirror outside the repo.
  E. SUCCESSOR COVERAGE — **new.** For every generation whose rows no longer
     reproduce because their input moved, is there a later generation pinning
     the live digest? Round-27 reported the supersessions; it never asked
     whether the cascade was re-pinned, which is the whole point of a sweep.
  F. FROZEN-ROOT INDEX — **new.** `corpus/knowledge/verification/
     gate-frozen-run-standard.md:54` declares a `tools/gates/frozen/README.md`
     index. Round-27 measured it absent (its findings X61-B2 / X62-B1). Duty F
     re-measures it and, when absent, reports how many generations are therefore
     unindexed, so the finding carries a size rather than a boolean.

Exit codes: 0 all records consistent, receipts agree, current generation
replays; 1 a record contradicts itself, a receipt disagrees, or the current
generation fails; 2 could-not-evaluate (a pinned file is missing, a path is
unsafe, or a manifest is malformed). 2 outranks 1.

Usage:
    export TMPDIR=/var/tmp PYTHONDONTWRITEBYTECODE=1   # /tmp is a shared tmpfs
    python3 -B reports/round-28/audit/x62-frozen-record-audit.py [--json]
    python3 -B reports/round-28/audit/x62-frozen-record-audit.py --selftest
    python3 -B reports/round-28/audit/x62-frozen-record-audit.py --no-replay
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
FINDING_PREFIX = "FINDING "
COLUMNS = (
    "gate", "gate_sha256", "input", "input_sha256", "exit_code",
    "finding_count", "output", "output_sha256", "input_snapshot", "command",
)
TIMEOUT = 120
STANDARD = ROOT / "corpus" / "knowledge" / "verification" / "gate-frozen-run-standard.md"
INDEX_DECLARED = FROZEN / "README.md"


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


def generation_key(manifest_rel):
    """(`round`, `phase`) ordinal, so "later" is a property of the path."""
    parts = Path(manifest_rel).parts
    for index, part in enumerate(parts):
        if part.startswith("round-") and part[6:].isdigit():
            phase = parts[index + 1] if index + 1 < len(parts) else ""
            return (int(part[6:]), phase)
    return (0, "")


def manifest_paths():
    gates = sorted(FROZEN.rglob("MANIFEST.tsv"))
    reports = []
    for path in sorted((ROOT / "reports").rglob("tests/frozen/MANIFEST.tsv")):
        if "/scratch/" in str(path.relative_to(ROOT)):
            continue
        reports.append(path)
    return gates + reports


def audit_row(row):
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
            if sha_file(output) != row["output_sha256"]:
                findings.append(f"output_tampered: {row['output']} is not the pinned bytes")
            observed = count_findings(output.read_bytes())
            if observed != int(row["finding_count"]):
                findings.append(
                    f"record_inconsistent: finding_count={row['finding_count']} but the "
                    f"recorded output carries {observed} FINDING line(s)")
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
    for manifest in manifest_paths():
        directory = manifest.parent
        rel = str(directory.relative_to(ROOT))
        rows, problems = read_manifest(manifest)
        reads = []
        for row in rows:
            try:
                reads.append(str(safe_path(row["input_snapshot"], "snapshot").relative_to(ROOT)))
            except Refused:
                reads.append(None)
        own = [r for r in reads if r and r.startswith(rel + "/")]
        foreign = sorted({r for r in reads if r and not r.startswith(rel + "/")})
        generations.append({
            "generation": rel,
            "manifest": str(manifest.relative_to(ROOT)),
            "round": generation_key(rel),
            "rows": len(rows),
            "problems": problems,
            "has_freeze_txt": (directory / "freeze.txt").is_file(),
            "has_freeze_receipt_json": (directory / "freeze-receipt.json").is_file(),
            "has_readme": (directory / "README.md").is_file(),
            "own_snapshots": len(own),
            "foreign_snapshots": foreign,
            "row_findings": [{"row": row["_row"], "findings": audit_row(row)} for row in rows],
            "rows_raw": rows,
        })
    return generations


def receipt_agreement(generation):
    """Duty C — the receipt's declared rows against the manifest's rows.

    Shape-aware, because three receipt shapes exist on this tree:
    a `rows` list of objects, a `manifest_rows` list, and an int `rows` with a
    positional `verdicts` list. A shape this function cannot address is reported
    as such, never as a pass.
    """
    path = ROOT / generation["generation"] / "freeze-receipt.json"
    if not path.is_file():
        return None
    rel = str(path.relative_to(ROOT))
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

    def compare(item, row, key):
        for field in ("exit_code", "finding_count", "gate_sha256", "input_sha256",
                      "output", "output_sha256"):
            if field in item and str(item[field]) != str(row.get(field)):
                findings.append(f"receipt/manifest disagree on {key} {field}: "
                                f"receipt={item[field]!r} manifest={row.get(field)!r}")

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
            compare(item, row, key)
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
            compare(item, row, key)
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
                rows = [r for r in manifest
                        if r["input"] == name or r["input_snapshot"].endswith(name)]
                for row in rows:
                    if digest != row["input_sha256"]:
                        findings.append(f"receipt input_pin for {name} disagrees with the manifest")
    else:
        findings.append("receipt carries no row-addressable list (rows/verdicts/manifest_rows)")

    return {"receipt": rel, "declared_rows": compared, "findings": findings}


def replay_generation(generation, tmpdir):
    """Duty D — re-execute one generation's rows in a mirror outside the repo."""
    results = []
    for row in generation["rows_raw"]:
        item = {"row": row["_row"], "gate": row["gate"], "input": row["input"],
                "input_pin": row["input_sha256"]}
        try:
            gate = safe_path(row["gate"], "gate")
            snapshot = safe_path(row["input_snapshot"], "snapshot")
            mirror = Path(tempfile.mkdtemp(prefix="x62r28-mirror-", dir=tmpdir))
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
                live = safe_path(row["input"], "input")
                live_sha = sha_file(live) if live.is_file() else None
                item["live_input_sha256"] = live_sha
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


def declared_pin_index():
    """(gate, input) -> [(manifest, pinned digest)] for every declared manifest.

    The frozen root is not the only place a generation is declared: this lane's
    re-pin convention writes successors under
    `reports/<round>/pinsweep/frozen/<id>/`. A successor question asked only of
    the frozen root can never be answered yes, which is finding X62R28-A2. The
    rows are read, never replayed, so widening costs a file read per manifest.
    """
    index = {}
    for path in sorted((ROOT / "reports").rglob("MANIFEST.tsv")):
        rel = str(path.relative_to(ROOT))
        if "/scratch/" in rel:
            continue
        rows, _ = read_manifest(path)
        for row in rows:
            index.setdefault((row["gate"], row["input"]), []).append(
                (rel, row["input_sha256"]))
    for path in sorted(FROZEN.rglob("MANIFEST.tsv")):
        rel = str(path.relative_to(ROOT))
        rows, _ = read_manifest(path)
        for row in rows:
            index.setdefault((row["gate"], row["input"]), []).append(
                (rel, row["input_sha256"]))
    return index


def successor_coverage(generations, index=None, scope=None):
    """Duty E — for every moved surface, does a LATER generation pin the live digest?

    Indexed on each row's own frozen digest, so two superseded rows cannot vouch
    for each other. "Later" comes from the generation ordinal, never from walk
    order. The index defaults to `declared_pin_index()` (repo-wide) and both it
    and the scope are injectable so the selftest controls stay in memory.

    Two successor sets are reported: `successors` (inside the swept scope) and
    `declared_successors` (repo-wide). The gap between them is finding
    X62R28-A2, so collapsing them would hide it.
    """
    index = declared_pin_index() if index is None else index
    scope = ({g["generation"] for g in generations} if scope is None else scope)
    records = []
    for generation in generations:
        for item in generation.get("replay", []):
            if item.get("class") != "supersession":
                continue
            live = item.get("live_input_sha256")
            candidates = [rel for rel, digest in index.get((item["gate"], item["input"]), [])
                          if digest == live and generation_key(rel) > generation["round"]]
            successors = [rel for rel in candidates if rel in scope]
            records.append({"generation": generation["generation"], "row": item["row"],
                            "gate": item["gate"], "input": item["input"],
                            "live_input_sha256": live, "successors": successors,
                            "declared_successors": candidates,
                            "re_pinned": bool(candidates),
                            "re_pinned_in_scope": bool(successors)})
    return records


def frozen_root_index():
    """Duty F — the index the frozen-run standard declares, and what it costs."""
    declared = STANDARD.is_file() and "frozen/" in STANDARD.read_text(
        encoding="utf-8", errors="replace")
    generations = [str(p.parent.relative_to(ROOT)) for p in manifest_paths()]
    return {
        "standard": str(STANDARD.relative_to(ROOT)),
        "standard_present": STANDARD.is_file(),
        "index_declared": bool(declared),
        "index_path": str(INDEX_DECLARED.relative_to(ROOT)),
        "index_present": INDEX_DECLARED.is_file(),
        "generations_unindexed": len(generations) if not INDEX_DECLARED.is_file() else 0,
    }


def selftest():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    tmp = Path(tempfile.mkdtemp(prefix="x62r28-selftest-", dir=tempfile.gettempdir()))
    try:
        out = tmp / "out.txt"
        out.write_bytes(b"FINDING a\nok\n")
        check("finding-count mismatch is caught", count_findings(out.read_bytes()) != 2)

        real_output = FROZEN / "round-26" / "post-register" / "d4-source.out"
        if real_output.is_file():
            real_sha = sha_file(real_output)
            real_count = count_findings(real_output.read_bytes())
            snapshot_rel = ("tools/gates/frozen/round-26/post-register/"
                            "inputs/examples/culture-d4/packet.d4.yml")
            # The fixture's `input_sha256` must be the SNAPSHOT's real digest:
            # the frozen row pins the committed copy, not the live packet, and
            # `audit_row` checks the snapshot against that pin.
            base = {"gate": "tools/gates/typed-pipeline-gate.py", "gate_sha256": "a" * 64,
                    "input": "examples/culture-d4/packet.d4.yml",
                    "input_sha256": sha_file(ROOT / snapshot_rel),
                    "exit_code": "0", "finding_count": str(real_count),
                    "output": str(real_output.relative_to(ROOT)),
                    "output_sha256": real_sha,
                    "input_snapshot": snapshot_rel,
                    "command": "python3 tools/gates/typed-pipeline-gate.py "
                               "examples/culture-d4/packet.d4.yml", "_row": 2}
            check("a clean frozen row audits clean", audit_row(base) == [])
            check("a self-contradicting record is caught",
                  any("record_inconsistent" in f
                      for f in audit_row(dict(base, finding_count=str(real_count + 1)))))
            check("a re-written output is caught",
                  any("output_tampered" in f for f in audit_row(dict(base, output_sha256="b" * 64))))
            check("a command naming another gate is caught",
                  any("command names gate" in f for f in audit_row(
                      dict(base, command="python3 tools/gates/myth-consistency-gate.py x"))))

        check("command gate parsed",
              command_names({"command": "python3 tools/gates/x.py a.yml"})[0]
              == "tools/gates/x.py")
        check("command input parsed",
              command_names({"command": "python3 tools/gates/x.py a.yml"})[1] == "a.yml")
        check("flags are not read as inputs",
              command_names({"command": "python3 tools/gates/x.py --json a.yml"})[1] == "a.yml")

        for raw in ("../../etc/passwd", "/etc/passwd", "--selftest",
                    "tools/gates/../gates/x.py"):
            try:
                safe_path(raw, "gate")
                check(f"unsafe refused: {raw}", False)
            except Refused as refused:
                check(f"unsafe refused: {raw}", refused.reason == "gate_unsafe_path")

        check("generation ordinal orders phases",
              generation_key("tools/gates/frozen/round-26/post-register/MANIFEST.tsv")
              > generation_key("tools/gates/frozen/round-26/gate-input/MANIFEST.tsv"))
        check("generation ordinal orders rounds",
              generation_key("tools/gates/frozen/round-27/x/MANIFEST.tsv")
              > generation_key("tools/gates/frozen/round-26/post-register/MANIFEST.tsv"))
        check("generation ordinal tolerates an unnumbered path",
              generation_key("reports/whatever/MANIFEST.tsv") == (0, ""))

        # duty-E controls: an earlier superseded row is not a successor, and the
        # verdict must not depend on walk order. The index and scope are injected
        # so these controls stay in memory and never read the repo.
        live = "d" * 64
        moved = {"row": 2, "gate": "tools/gates/x.py", "input": "a.yml",
                 "class": "supersession", "live_input_sha256": live}
        gens = [
            {"generation": "tools/gates/frozen/round-18", "round": (18, ""),
             "rows_raw": [{"gate": "tools/gates/x.py", "input": "a.yml", "input_sha256": "c" * 64}],
             "replay": [dict(moved)]},
            {"generation": "tools/gates/frozen/round-22", "round": (22, ""),
             "rows_raw": [{"gate": "tools/gates/x.py", "input": "a.yml", "input_sha256": live}],
             "replay": [dict(moved, row=3)]},
        ]

        def gen_index(gs):
            idx = {}
            for g in gs:
                for row in g["rows_raw"]:
                    idx.setdefault((row["gate"], row["input"]), []).append(
                        (g["generation"], row["input_sha256"]))
            return idx

        def gen_scope(gs):
            return {g["generation"] for g in gs}

        records = successor_coverage(gens, index=gen_index(gens), scope=gen_scope(gens))
        check("successor coverage: a later row at the live digest is a re-pin",
              len(records) == 2 and records[0]["re_pinned"] and not records[1]["re_pinned"])
        gens[1]["rows_raw"] = [{"gate": "tools/gates/x.py", "input": "a.yml",
                                "input_sha256": "c" * 64}]
        records = successor_coverage(gens, index=gen_index(gens), scope=gen_scope(gens))
        check("successor coverage: an earlier superseded row is not a successor",
              not any(r["re_pinned"] for r in records))
        records_reversed = successor_coverage(list(reversed(gens)),
                                             index=gen_index(gens), scope=gen_scope(gens))
        check("successor coverage: verdict is order-independent",
              sorted(r["re_pinned"] for r in records)
              == sorted(r["re_pinned"] for r in records_reversed))
        check("successor coverage: a row is never its own successor",
              all(r["generation"] not in r["successors"] for r in records))
        # the scope/index split is the finding: a successor OUTSIDE the swept
        # scope must read declared but not in-scope, which is the round-28 shape.
        outside = [{"generation": "tools/gates/frozen/round-18", "round": (18, ""),
                    "rows_raw": [{"gate": "tools/gates/x.py", "input": "a.yml",
                                  "input_sha256": "c" * 64}],
                    "replay": [dict(moved)]}]
        idx = gen_index(outside)
        idx[("tools/gates/x.py", "a.yml")].append(
            ("reports/round-28/pinsweep/frozen/r28-post", live))
        records = successor_coverage(outside, index=idx, scope=gen_scope(outside))
        check("successor coverage: an out-of-scope successor reads declared but not in-scope",
              records[0]["re_pinned"] and not records[0]["re_pinned_in_scope"])

        index = frozen_root_index()
        check("duty F reports the index path",
              index["index_path"] == "tools/gates/frozen/README.md")
        check("duty F reports a size when the index is absent",
              index["index_present"] or index["generations_unindexed"] > 0)
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
    parser.add_argument("--no-replay", action="store_true")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()

    tmpdir = tempfile.gettempdir()
    try:
        Path(tmpdir).resolve().relative_to(ROOT.resolve())
        tmpdir_inside = True
    except ValueError:
        tmpdir_inside = False

    generations = inventory()
    receipts = {}
    for generation in generations:
        result = receipt_agreement(generation)
        if result is not None:
            receipts[generation["generation"]] = result

    current = max(generations, key=lambda g: g["round"]) if generations else None
    if current is not None and not args.no_replay:
        current["replay"] = replay_generation(current, tmpdir)

    successors = successor_coverage(generations)
    record_findings = sum(len(item["findings"]) for g in generations for item in g["row_findings"])
    receipt_findings = sum(len(r["findings"]) for r in receipts.values())
    tally = {}
    if current is not None and "replay" in current:
        for item in current["replay"]:
            tally[item["status"]] = tally.get(item["status"], 0) + 1

    receipt = {
        "tool": "reports/round-28/audit/x62-frozen-record-audit.py",
        "seat": "R28-X62",
        "date": "2026-10-18",
        "command": "python3 -B reports/round-28/audit/x62-frozen-record-audit.py --json",
        "head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True,
                               text=True).stdout.strip(),
        "python": sys.version.split()[0],
        "tmpdir": tmpdir,
        "tmpdir_inside_repo": tmpdir_inside,
        "generations": [{k: v for k, v in g.items() if k not in ("rows_raw", "row_findings")}
                        for g in generations],
        "row_findings": {g["generation"]: g["row_findings"] for g in generations},
        "receipts": receipts,
        "current_generation": current["generation"] if current else None,
        "current_replay": current.get("replay") if current else None,
        "successors": successors,
        "frozen_root_index": frozen_root_index(),
        "summary": {
            "generations": len(generations),
            "rows": sum(g["rows"] for g in generations),
            "record_findings": record_findings,
            "receipt_findings": receipt_findings,
            "manifest_problems": sum(len(g["problems"]) for g in generations),
            # Two receipt counts, deliberately: `freeze-receipt.json` is the
            # machine receipt duty C compares against, `freeze.txt` is the human
            # one. Round-27 reported a single count of 8 by treating either as
            # "carries a receipt"; splitting them keeps the shape of the record
            # visible instead of collapsing two different things into one number.
            "generations_with_receipt": len(receipts),
            "generations_with_receipt_json": sum(1 for g in generations
                                                 if g["has_freeze_receipt_json"]),
            "generations_with_receipt_txt": sum(1 for g in generations if g["has_freeze_txt"]),
            "generations_with_either_receipt": sum(
                1 for g in generations if g["has_freeze_receipt_json"] or g["has_freeze_txt"]),
            "generations_with_readme": sum(1 for g in generations if g["has_readme"]),
            "foreign_snapshot_rows": sum(len(g["foreign_snapshots"]) for g in generations),
            "current_replay_tally": tally,
            "superseded_rows": len(successors),
            "superseded_rows_re_pinned": sum(1 for s in successors if s["re_pinned"]),
            "superseded_rows_unpinned": sum(1 for s in successors if not s["re_pinned"]),
            "superseded_rows_re_pinned_in_scope": sum(
                1 for s in successors if s["re_pinned_in_scope"]),
        },
    }

    if args.json:
        print(json.dumps(receipt, indent=1, sort_keys=True))
    else:
        s = receipt["summary"]
        lines = [f"X62 round-28 frozen record audit — {receipt['date']} — lane HEAD {receipt['head']}",
                 f"  TMPDIR={receipt['tmpdir']} (inside_repo={receipt['tmpdir_inside_repo']})",
                 f"  {s['generations']} generation(s), {s['rows']} row(s); "
                 f"{s['record_findings']} record finding(s), {s['receipt_findings']} receipt finding(s), "
                 f"{s['manifest_problems']} manifest problem(s)",
                 f"  receipts: json {s['generations_with_receipt_json']}/{s['generations']}, "
                 f"txt {s['generations_with_receipt_txt']}/{s['generations']}, "
                 f"either {s['generations_with_either_receipt']}/{s['generations']}; "
                 f"READMEs {s['generations_with_readme']}/{s['generations']}"]
        for generation in receipt["generations"]:
            lines.append(f"  {generation['generation']}: {generation['rows']} row(s), "
                         f"receipt={generation['has_freeze_receipt_json']}, "
                         f"readme={generation['has_readme']}")
        if receipt["current_generation"]:
            lines.append(f"  current {receipt['current_generation']}: "
                         f"{json.dumps(s['current_replay_tally'])}")
        lines.append(f"  successors: {s['superseded_rows_re_pinned']}/{s['superseded_rows']} "
                     f"moved row(s) carry a declared successor anywhere in the repo "
                     f"({s['superseded_rows_re_pinned_in_scope']} inside the swept scope)")
        index = receipt["frozen_root_index"]
        lines.append(f"  frozen-root index {index['index_path']}: present={index['index_present']} "
                     f"(declared by the standard: {index['index_declared']}); "
                     f"{index['generations_unindexed']} generation(s) unindexed")
        print("\n".join(lines))

    if s["record_findings"] or s["receipt_findings"] or s["manifest_problems"]:
        return 1
    if "could-not-evaluate" in tally and tally["could-not-evaluate"]:
        return 2
    if "mismatch" in tally and tally["mismatch"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
