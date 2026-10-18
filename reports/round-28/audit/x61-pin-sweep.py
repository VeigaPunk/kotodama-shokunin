#!/usr/bin/env python3
"""R28-X61 — pin-sweep double-check (read-only; own re-derivation).

Seat R28-X61 (SCRIBE X61: sweep double-check) for round 28, claim O
(`operability`, `final-pin-sweep`; `reports/round-28/claims.json`). NON-CANON
engineering evidence. This tool admits nothing and certifies no round.

It is the round-28 successor of `reports/round-27/audit/x61-pin-sweep.py`, and
it differs from it in three measured ways — each difference is a finding, not a
refactor:

  * SCOPE. The round-27 seat swept `tools/gates/frozen/**` only: 11 manifests /
    81 rows. Two peer sweeps in this lane count a twelfth manifest —
    `reports/round-17/tests/frozen/MANIFEST.tsv` (5 rows) — which the lane's own
    validator names in its replay command (`reports/round-21/recount/r17-2.md:15`)
    and which `tools/replay-frozen.py` accepts as a first-class argument. This
    tool sweeps **every** `MANIFEST.tsv` under `tools/gates/frozen/**` **and**
    `reports/**/tests/frozen/**`, and reports both totals separately so the
    boundary is visible rather than implied. Finding **X61R28-A1**.
  * SUCCESSOR PINS. A supersession is only benign if a later generation re-pins
    the moved surface. Round-27 classified supersessions but never asked whether
    a successor row exists. Duty C answers that per row, by digest, across every
    manifest in scope. Finding **X61R28-A2**.
  * TMPDIR. Round-27 ran with the operator-mandated `TMPDIR=$PWD/.scratch` and
    measured the resulting `mirror_unsafe` void (its finding X61-B1). `/tmp` on
    this host is a 16 GB tmpfs shared with the whole fleet and was at 80% during
    this window; the mirror parent therefore defaults to `/var/tmp`. The probe
    still measures both parents, so the sensitivity is a measurement either way.

Duties:
  A. MANIFEST sweep — per row, before any gate runs: `gate_sha256` against the
     live gate, `input_sha256` against the committed snapshot, `output_sha256`
     against the recorded output; then re-execute the gate in a mirror whose
     real path is outside the repo and compare exit code, `^FINDING ` count and
     output bytes.
  B. BASELINE sweep — every `expected.json` under the three roots
     `tools/check-gate-battery.py` discovers.
  C. SUCCESSOR-PIN sweep — for every row whose live input no longer hashes to
     its own pin, ask whether any *other* manifest in scope carries a row for
     the same `(gate, input)` at the live digest.
  D. TMPDIR sensitivity probe — the same manifest replayed under an in-repo and
     an out-of-repo mirror parent.

Exit codes: 0 all green; 1 an evaluated row mismatched; 2 could-not-evaluate
(a pin failed, a path is unsafe, or a manifest is malformed). 2 outranks 1.

Usage:
    export TMPDIR=/var/tmp PYTHONDONTWRITEBYTECODE=1   # /tmp is a shared tmpfs
    python3 -B reports/round-28/audit/x61-pin-sweep.py [--json] [--selftest]
"""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[3]
FROZEN = ROOT / "tools" / "gates" / "frozen"
EXPECTED = ROOT / "tools" / "gates" / "expected"
FINDING_PREFIX = "FINDING "
COLUMNS = (
    "gate", "gate_sha256", "input", "input_sha256", "exit_code",
    "finding_count", "output", "output_sha256", "input_snapshot", "command",
)
HEX = frozenset("0123456789abcdef")
TIMEOUT = 120
# Filled by `main()` with the manifests the sweep actually walked, so duty C can
# separate "a later row exists somewhere in the repo" from "a later row exists
# inside the swept scope". The gap between the two is finding X61R28-A2.
SCOPE_MANIFESTS = set()
REGISTERED_GATES = (
    "costume-era-consistency-gate.py",
    "handoff-packet-check.py",
    "lexicon-coverage-audit.py",
    "myth-consistency-gate.py",
    "naming-collision-gate.py",
    "phonology-sanity-gate.py",
    "provenance-audit.py",
    "d4-typed-labels-check-gate.py",
    "d4-assembly-check-gate.py",
)


class Refused(Exception):
    def __init__(self, reason, detail):
        super().__init__(detail)
        self.reason = reason
        self.detail = detail


def sha_bytes(payload):
    return hashlib.sha256(payload).hexdigest()


def sha_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def gate_script_name(value):
    if not isinstance(value, str) or not value.strip():
        return None
    candidate = value.strip()
    for name in REGISTERED_GATES:
        if candidate in (name, name[:-3]) or Path(candidate).name in (name, name[:-3]):
            return name
    return None


def implied_gate(baseline_rel):
    for component in Path(baseline_rel).parts:
        resolved = gate_script_name(component)
        if resolved:
            return resolved
    return None


def safe_path(raw, what, root=None):
    root = root or ROOT
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
    target = root / os.path.normpath(raw)
    if target.is_symlink():
        raise Refused(f"{what}_unsafe_path", f"{what}: symlink refused: {raw!r}")
    try:
        target.resolve().relative_to(root.resolve())
    except ValueError:
        raise Refused(f"{what}_unsafe_path", f"{what}: resolves outside the repo: {raw!r}")
    return target


def count_findings(payload):
    return sum(1 for line in payload.decode("utf-8", "replace").splitlines()
               if line.startswith(FINDING_PREFIX))


def gate_ok(raw):
    segments = [s for s in raw.split("/") if s not in ("", ".")]
    return len(segments) == 3 and tuple(segments[:2]) == ("tools", "gates") \
        and segments[2].endswith(".py")


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


def manifest_paths():
    """Every frozen manifest in scope, split by the root that carries it.

    `tools/gates/frozen/**` is the round-27 seat's scope. `reports/**/tests/
    frozen/**` carries the round-17 manifest the lane's own validator replays;
    excluding it is the completeness gap finding X61R28-A1 names.
    """
    under_gates, under_reports = [], []
    for path in sorted(FROZEN.rglob("MANIFEST.tsv")):
        under_gates.append(path)
    for path in sorted((ROOT / "reports").rglob("tests/frozen/MANIFEST.tsv")):
        rel = str(path.relative_to(ROOT))
        if "/scratch/" in rel:
            continue
        under_reports.append(path)
    return under_gates, under_reports


def classify_mismatch(live_input_sha256, pinned_sha256):
    """D20 §3.1: a moved live input is a supersession, an unmoved one is drift."""
    if live_input_sha256 is None:
        return "unknown"
    return "supersession" if live_input_sha256 != pinned_sha256 else "drift"


def verify_row(row, tmpdir=None):
    # `input_pin` is carried on every result, not only on mismatches: duty C
    # asks whether a *later* row pins the digest a superseded row's surface now
    # has, and that question needs each row's own frozen digest as an index key.
    result = {"row": row["_row"], "gate": row["gate"], "input": row["input"],
              "input_pin": row["input_sha256"]}
    try:
        for field in ("gate_sha256", "input_sha256", "output_sha256"):
            value = row[field]
            if len(value) != 64 or any(c not in HEX for c in value):
                raise Refused("record_malformed", f"{field}: not a sha256 digest: {value!r}")
        if not gate_ok(row["gate"]):
            raise Refused("gate_not_whitelisted",
                          f"gate is not a python file directly under tools/gates: {row['gate']!r}")
        gate = safe_path(row["gate"], "gate")
        if not gate.is_file():
            raise Refused("gate_missing", f"gate not on disk: {row['gate']}")
        result["gate_live_sha256"] = sha_file(gate)
        result["gate_pin_holds"] = result["gate_live_sha256"] == row["gate_sha256"]
        if not result["gate_pin_holds"]:
            raise Refused("gate_digest_mismatch",
                          f"gate: on-disk bytes are not the pinned revision: {row['gate']}")

        snapshot = safe_path(row["input_snapshot"], "snapshot")
        if not snapshot.is_file():
            raise Refused("snapshot_missing", f"snapshot not on disk: {row['input_snapshot']}")
        result["snapshot_sha256"] = sha_file(snapshot)
        result["snapshot_pin_holds"] = result["snapshot_sha256"] == row["input_sha256"]
        if not result["snapshot_pin_holds"]:
            raise Refused("snapshot_tampered",
                          f"snapshot bytes are not the pinned input: {row['input_snapshot']}")

        recorded = safe_path(row["output"], "output")
        if not recorded.is_file():
            raise Refused("output_missing", f"recorded output not on disk: {row['output']}")
        result["output_sha256"] = sha_file(recorded)
        result["output_pin_holds"] = result["output_sha256"] == row["output_sha256"]
        if not result["output_pin_holds"]:
            raise Refused("expected_output_tampered",
                          f"recorded output is not the pinned bytes: {row['output']}")
    except Refused as refused:
        result.update(status="could-not-evaluate", reason=refused.reason, detail=refused.detail,
                      launched=False)
        return result

    try:
        observed = run_in_mirror(gate, snapshot, row["input"], tmpdir=tmpdir)
    except Refused as refused:
        result.update(status="could-not-evaluate", reason=refused.reason, detail=refused.detail,
                      launched=False)
        return result

    result.update(launched=True, exit=observed["exit"], recorded_exit=int(row["exit_code"]),
                  finding_count=observed["count"], recorded_count=int(row["finding_count"]),
                  bytes_match=observed["sha256"] == row["output_sha256"])
    agrees = (result["exit"] == result["recorded_exit"]
              and result["finding_count"] == result["recorded_count"]
              and result["bytes_match"])
    result["status"] = "reproduced" if agrees else "mismatch"
    result["reason"] = "-" if agrees else "replay_mismatch"
    if not agrees:
        detail = []
        if result["exit"] != result["recorded_exit"]:
            detail.append(f"exit code {result['exit']} != recorded {result['recorded_exit']}")
        if result["finding_count"] != result["recorded_count"]:
            detail.append(f"finding count {result['finding_count']} != recorded {result['recorded_count']}")
        if not result["bytes_match"]:
            detail.append("output bytes differ from the recorded output")
        result["detail"] = "; ".join(detail)
        try:
            live = safe_path(row["input"], "input")
            live_sha = sha_file(live) if live.is_file() else None
        except Refused:
            live_sha = None
        result["live_input_sha256"] = live_sha
        result["live_input_moved"] = bool(live_sha) and live_sha != row["input_sha256"]
        result["class"] = classify_mismatch(live_sha, row["input_sha256"])
    return result


def run_in_mirror(gate, snapshot, input_rel, tmpdir=None):
    if tmpdir is None:
        tmpdir = tempfile.gettempdir()
    mirror = Path(tempfile.mkdtemp(prefix="x61r28-mirror-", dir=tmpdir))
    try:
        try:
            mirror.resolve().relative_to(ROOT.resolve())
            raise Refused("mirror_unsafe", f"mirror: temporary root is inside the repo: {mirror}")
        except ValueError:
            pass
        destination = mirror / input_rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(snapshot, destination)
        environment = dict(os.environ)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        try:
            proc = subprocess.run([sys.executable, str(gate), input_rel], cwd=mirror,
                                  stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, timeout=TIMEOUT, env=environment)
        except subprocess.TimeoutExpired:
            raise Refused("gate_timeout", f"gate: exceeded {TIMEOUT}s")
        except OSError as exc:
            raise Refused("gate_launch_failed", f"gate: could not start: {exc}")
        return {"exit": proc.returncode, "count": count_findings(proc.stdout),
                "sha256": sha_bytes(proc.stdout)}
    finally:
        shutil.rmtree(mirror, ignore_errors=True)


def sweep_manifests(paths, root_label, tmpdir=None):
    manifests = []
    for path in paths:
        rows, problems = read_manifest(path)
        results = [verify_row(row, tmpdir=tmpdir) for row in rows]
        tally = {"reproduced": 0, "mismatch": 0, "could-not-evaluate": 0}
        for item in results:
            tally[item["status"]] += 1
        manifests.append({"manifest": str(path.relative_to(ROOT)), "root": root_label,
                          "rows": len(rows), "problems": problems, "tally": tally,
                          "results": results})
    return manifests


def sweep_baselines():
    baselines = []
    roots = [EXPECTED, FROZEN, ROOT / "reports" / "round-9" / "baselines"]
    seen, paths = set(), []
    for root in roots:
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("expected.json")):
            rel = str(path.relative_to(ROOT))
            if rel in seen:
                continue
            seen.add(rel)
            paths.append((path, root))
    for path, root in paths:
        rel = str(path.relative_to(ROOT))
        entry = {"baseline": rel, "root": str(root.relative_to(ROOT)), "findings": []}
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            entry["findings"].append(f"unreadable baseline: {exc}")
            baselines.append(entry)
            continue
        directory = path.parent
        declared_gate = document.get("gate_script") or document.get("gate")
        gate_name = gate_script_name(declared_gate) or implied_gate(rel)
        entry["gate"] = gate_name
        if gate_name is None:
            entry["findings"].append(
                f"gate_unknown: declared gate {declared_gate!r} resolves to no registered gate")
        else:
            gate = ROOT / "tools" / "gates" / gate_name
            if not gate.is_file():
                entry["findings"].append(f"gate not on disk: {gate_name}")
            else:
                live = sha_file(gate)
                entry["gate_sha256_live"] = live
                pin = document.get("gate_sha256")
                entry["gate_pin_holds"] = live == pin
                if pin is None:
                    entry["findings"].append(f"gate_unpinned: {rel} names no gate revision")
                elif live != pin:
                    entry["findings"].append(
                        f"gate_revised: {gate_name} live {live[:12]}… is not the pinned {str(pin)[:12]}…")
        declared = document.get("inputs")
        entry["inputs_declared"] = len(declared) if isinstance(declared, dict) else None
        entry["inputs_unpinned"] = 0
        entry["inputs_verified"] = 0
        if not isinstance(declared, dict) or not declared:
            entry["findings"].append("unpinned (legacy): no inputs map")
        else:
            for input_rel, pin in declared.items():
                try:
                    target = safe_path(input_rel, "input", root=directory)
                except Refused as refused:
                    entry["findings"].append(f"{refused.reason}: {refused.detail}")
                    continue
                if not pin:
                    entry["inputs_unpinned"] += 1
                    entry["findings"].append(f"unpinned (legacy): {input_rel}")
                    continue
                if not target.is_file():
                    entry["findings"].append(f"snapshot missing: {input_rel}")
                    continue
                if sha_file(target) != pin:
                    entry["findings"].append(f"snapshot_tampered: {input_rel}")
                else:
                    entry["inputs_verified"] += 1
        entry["verdict"] = "pinned" if not entry["findings"] else "not-pinned"
        baselines.append(entry)
    return baselines


def generation_key(manifest_rel):
    """Ordinal for a manifest path: (`round`, `phase`) so later generations sort last.

    `<...>/round-26/post-register/MANIFEST.tsv` -> (26, "post-register").
    A path with no `round-N` component sorts first: it is not a numbered
    generation and must never be read as a successor of one.
    """
    parts = Path(manifest_rel).parts
    for index, part in enumerate(parts):
        if part.startswith("round-") and part[6:].isdigit():
            phase = parts[index + 1] if index + 1 < len(parts) else ""
            return (int(part[6:]), phase)
    return (0, "")


def declared_pin_index():
    """(gate, input) -> [(manifest, pinned digest)] for EVERY manifest in the repo.

    The frozen root is not the only place a generation is declared. This lane's
    re-pin convention writes its successor manifests under
    `reports/<round>/pinsweep/frozen/<id>/` — round 27's at
    `reports/round-27/pinsweep/frozen/r27-post/`, round 28's at
    `reports/round-28/pinsweep/frozen/r28-post/`. A successor question asked
    only of `tools/gates/frozen/**` can therefore never be answered yes, which
    is finding X61R28-A2. The rows are read, never replayed, so widening the
    index costs a file read per manifest.
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


def index_from_results(manifests):
    """(gate, input) -> [(manifest, pinned digest)] built from swept results.

    The key is each row's OWN frozen digest (`input_pin`), never the live digest
    of the row under audit. Indexing live digests would let two superseded rows
    vouch for each other: both have moved, so both would find a "successor"
    while no generation actually re-pinned the surface. The duty-C controls bite
    on exactly that confusion.
    """
    index = {}
    for manifest in manifests:
        for item in manifest["results"]:
            index.setdefault((item["gate"], item["input"]), []).append(
                (manifest["manifest"], item["input_pin"]))
    return index


def sweep_successors(manifests, index=None, scope=None):
    """Duty C — for every superseded row, does a LATER row pin the live digest?

    The index defaults to `declared_pin_index()`, which spans every declared
    manifest in the repo, not only the frozen root — otherwise the answer is
    structurally always no (finding X61R28-A2). Two successor sets are reported
    per row: `successors` (in the swept scope) and `declared_successors`
    (repo-wide). The distinction is the finding, so collapsing them would hide
    it. Both the index and the scope are injectable so the selftest controls
    stay in memory and never depend on the state of the repo.

    "Later" is decided by the generation id, not by which manifest happened to
    be walked first: the ids are `<round>` or `<round>/<phase>`, so the round
    number is the ordinal and the phase breaks ties inside a round. Without that
    ordering the answer would depend on directory walk order.
    """
    index = declared_pin_index() if index is None else index
    scope = SCOPE_MANIFESTS if scope is None else scope
    records = []
    for manifest in manifests:
        for item in manifest["results"]:
            if item.get("class") != "supersession":
                continue
            live = item.get("live_input_sha256")
            candidates = [rel for rel, digest in index.get((item["gate"], item["input"]), [])
                          if digest == live and generation_key(rel) > generation_key(manifest["manifest"])]
            successors = [rel for rel in candidates if rel in scope]
            records.append({"manifest": manifest["manifest"], "row": item["row"],
                            "gate": item["gate"], "input": item["input"],
                            "live_input_sha256": live, "successors": successors,
                            "declared_successors": candidates,
                            "re_pinned": bool(candidates),
                            "re_pinned_in_scope": bool(successors)})
    return records


def tmpdir_probe(manifest, tmpdirs):
    probe = []
    for label, tmpdir in tmpdirs:
        rows, _ = read_manifest(manifest)
        tally = {"reproduced": 0, "mismatch": 0, "could-not-evaluate": 0, "mirror_unsafe": 0}
        for row in rows:
            item = verify_row(row, tmpdir=tmpdir)
            tally[item["status"]] += 1
            if item.get("reason") == "mirror_unsafe":
                tally["mirror_unsafe"] += 1
        probe.append({"tmpdir": label, "tally": tally})
    return probe


def summarise(manifests, baselines, successors):
    items = [item for m in manifests for item in m["results"]]
    return {
        "manifests": len(manifests),
        "manifest_rows": sum(m["rows"] for m in manifests),
        "rows_reproduced": sum(m["tally"]["reproduced"] for m in manifests),
        "rows_mismatched": sum(m["tally"]["mismatch"] for m in manifests),
        "rows_unevaluable": sum(m["tally"]["could-not-evaluate"] for m in manifests),
        "mismatch_supersession": sum(1 for i in items if i.get("class") == "supersession"),
        "mismatch_drift": sum(1 for i in items if i.get("class") == "drift"),
        "gate_digest_mismatch": sum(1 for i in items if i.get("reason") == "gate_digest_mismatch"),
        "superseded_rows": len(successors),
        "superseded_rows_re_pinned": sum(1 for s in successors if s["re_pinned"]),
        "superseded_rows_unpinned": sum(1 for s in successors if not s["re_pinned"]),
        "superseded_rows_re_pinned_in_scope": sum(
            1 for s in successors if s["re_pinned_in_scope"]),
        "baselines": len(baselines),
        "baselines_pinned": sum(1 for b in baselines if b["verdict"] == "pinned"),
        "baselines_not_pinned": sum(1 for b in baselines if b["verdict"] != "pinned"),
        "baseline_findings": sum(len(b["findings"]) for b in baselines),
        "baseline_inputs_verified": sum(b.get("inputs_verified", 0) for b in baselines),
    }


def text_report(receipt):
    lines = [f"X61 round-28 pin sweep — {receipt['date']} — lane HEAD {receipt['head']}",
             f"  TMPDIR={receipt['tmpdir']} (inside_repo={receipt['tmpdir_inside_repo']})"]
    for root, entries in receipt["scope"].items():
        lines.append(f"  scope {root}: {len(entries)} manifest(s), "
                     f"{sum(e['rows'] for e in entries)} row(s)")
    for manifest in receipt["manifests"]:
        t = manifest["tally"]
        lines.append(f"  {manifest['manifest']}: {t['reproduced']} reproduced, "
                     f"{t['mismatch']} mismatch, {t['could-not-evaluate']} could-not-evaluate "
                     f"of {manifest['rows']}")
        for item in manifest["results"]:
            if item["status"] == "reproduced":
                continue
            lines.append(f"    ROW {item['row']} {item['status']} reason={item.get('reason')} "
                         f"gate={item['gate']} input={item['input']}")
            if item.get("class"):
                lines.append(f"      class: {item['class']} "
                             f"(live input moved={item.get('live_input_moved')})")
        for problem in manifest["problems"]:
            lines.append(f"    PROBLEM: {problem}")
    for baseline in receipt["baselines"]:
        if baseline["findings"]:
            lines.append(f"  {baseline['baseline']}: NOT PINNED")
            for finding in baseline["findings"]:
                lines.append(f"    FINDING: {finding}")
    s = receipt["summary"]
    lines.append(f"  summary: {s['rows_reproduced']}/{s['manifest_rows']} rows reproduced; "
                 f"{s['rows_mismatched']} mismatch ({s['mismatch_supersession']} supersession, "
                 f"{s['mismatch_drift']} drift); {s['rows_unevaluable']} could-not-evaluate "
                 f"({s['gate_digest_mismatch']} gate_digest_mismatch); "
                 f"baselines {s['baselines_pinned']}/{s['baselines']} pinned")
    lines.append(f"  successors: {s['superseded_rows_re_pinned']}/{s['superseded_rows']} "
                 f"superseded rows carry a later row at the live digest "
                 f"({s['superseded_rows_unpinned']} do not)")
    if "tmpdir_probe" in receipt:
        lines.append(f"  TMPDIR probe on {receipt['tmpdir_probe']['manifest']}:")
        for run in receipt["tmpdir_probe"]["runs"]:
            t = run["tally"]
            lines.append(f"    {run['tmpdir']}: {t['reproduced']} reproduced, {t['mismatch']} mismatch, "
                         f"{t['could-not-evaluate']} could-not-evaluate ({t['mirror_unsafe']} mirror_unsafe)")
    return "\n".join(lines)


def selftest():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    header = "\t".join(COLUMNS)
    sample = (f"{header}\n"
              f"tools/gates/naming-collision-gate.py\t{'a' * 64}\texamples/x.yml\t{'b' * 64}\t"
              f"0\t0\tout.out\t{'c' * 64}\texamples/x.yml\tpython3 x\n")
    tmp = Path(tempfile.mkdtemp(prefix="x61r28-selftest-", dir=tempfile.gettempdir()))
    try:
        manifest = tmp / "MANIFEST.tsv"
        manifest.write_text(sample, encoding="utf-8")
        rows, problems = read_manifest(manifest)
        check("well-formed manifest parses", len(rows) == 1 and not problems)

        manifest.write_text("gate\tinput\nx\ty\n", encoding="utf-8")
        rows, problems = read_manifest(manifest)
        check("bad header refused", not rows and bool(problems))

        manifest.write_text(header + "\ntools/gates/x.py\t" + "a" * 64 + "\n", encoding="utf-8")
        rows, problems = read_manifest(manifest)
        check("short row refused", not rows and bool(problems))

        bad = dict(zip(COLUMNS, sample.split("\n")[1].split("\t")))
        bad["_row"] = 2
        bad["gate_sha256"] = "not-a-digest"
        item = verify_row(bad, tmpdir=str(tmp))
        check("bad digest pin refused", item["status"] == "could-not-evaluate"
              and item["reason"] == "record_malformed")

        bad2 = dict(bad)
        bad2["gate_sha256"] = "a" * 64
        bad2["gate"] = "tools/replay-frozen.py"
        item = verify_row(bad2, tmpdir=str(tmp))
        check("non-whitelisted gate refused", item["status"] == "could-not-evaluate"
              and item["reason"] == "gate_not_whitelisted")

        for raw in ("../../etc/passwd", "tools/gates/../gates/x.py", "--selftest",
                    "/etc/passwd", "~/x"):
            try:
                safe_path(raw, "gate")
                check(f"unsafe path refused: {raw}", False)
            except Refused as refused:
                check(f"unsafe path refused: {raw}", refused.reason == "gate_unsafe_path")

        check("legal path resolves", safe_path("tools/replay-frozen.py", "gate").is_file())

        try:
            run_in_mirror(ROOT / "tools" / "replay-frozen.py", ROOT / "tools" / "replay-frozen.py",
                          "tools/replay-frozen.py", tmpdir=str(ROOT / ".scratch"))
            check("in-repo mirror refused", False)
        except Refused as refused:
            check("in-repo mirror refused", refused.reason == "mirror_unsafe")

        check("finding count is prefix-anchored",
              count_findings(b"FINDING a\nok x\nFINDING b\nFINDINGX c\n") == 2)

        check("classifier: moved input is supersession",
              classify_mismatch("b" * 64, "a" * 64) == "supersession")
        check("classifier: unmoved input is drift",
              classify_mismatch("a" * 64, "a" * 64) == "drift")
        check("classifier: unreadable input is unknown",
              classify_mismatch(None, "a" * 64) == "unknown")
        check("classifier: missing input is not supersession",
              classify_mismatch(None, "a" * 64) != "supersession")

        check("gate resolves from bare name",
              gate_script_name("myth-consistency-gate") == "myth-consistency-gate.py")
        check("gate resolves from script path",
              gate_script_name("tools/gates/myth-consistency-gate.py") == "myth-consistency-gate.py")
        check("gate resolves from baseline path",
              implied_gate("tools/gates/expected/phonology-sanity-gate/r9-pre/expected.json")
              == "phonology-sanity-gate.py")
        check("unknown gate is not guessed", gate_script_name("not-a-gate") is None)

        # duty-C controls: a supersession with a LATER row at the live digest must
        # read re-pinned; one with no later row must read unpinned. Built in
        # memory so the controls bite without touching the lane's frozen surface.
        # Every fixture uses real `round-N/phase` paths, because the ordering
        # that decides "later" is derived from the path, not from list order.
        live = "d" * 64
        frozen_old = {"row": 2, "gate": "tools/gates/x.py", "input": "a.yml",
                      "class": "supersession", "live_input_sha256": live,
                      "input_pin": "c" * 64}
        fake = [
            {"manifest": "tools/gates/frozen/round-18/MANIFEST.tsv", "results": [frozen_old]},
            {"manifest": "tools/gates/frozen/round-22/repin/MANIFEST.tsv", "results": [
                {"row": 2, "gate": "tools/gates/x.py", "input": "a.yml",
                 "input_pin": live}]},
        ]
        records = sweep_successors(fake, index=index_from_results(fake),
                                   scope={m["manifest"] for m in fake})
        check("successor: a later row at the live digest counts as re-pinned",
              len(records) == 1 and records[0]["re_pinned"])
        fake[1]["results"] = []
        records = sweep_successors(fake, index=index_from_results(fake),
                                   scope={m["manifest"] for m in fake})
        check("successor: no later row reads unpinned",
              len(records) == 1 and not records[0]["re_pinned"])
        fake[1]["results"] = [{"row": 2, "gate": "tools/gates/x.py", "input": "a.yml",
                               "input_pin": "e" * 64}]
        records = sweep_successors(fake, index=index_from_results(fake),
                                   scope={m["manifest"] for m in fake})
        check("successor: a later row at a different digest is not a re-pin",
              len(records) == 1 and not records[0]["re_pinned"])
        # the bug this control exists for: an EARLIER row that also moved must
        # not vouch for the row under audit — two superseded rows are not a
        # re-pin, and indexing live digests would have read this as one.
        fake[0]["results"] = [frozen_old, dict(frozen_old, row=3, input_pin="c" * 64)]
        fake[1]["results"] = [{"row": 2, "gate": "tools/gates/x.py", "input": "a.yml",
                               "input_pin": "c" * 64}]
        records = sweep_successors(fake, index=index_from_results(fake),
                                   scope={m["manifest"] for m in fake})
        check("successor: an earlier superseded row is not a successor",
              len(records) == 2 and not any(r["re_pinned"] for r in records))
        # and the ordering must not be list order: the same pair reversed must
        # give the same verdict.
        reversed_fake = list(reversed(fake))
        reversed_records = sweep_successors(reversed_fake,
                                            index=index_from_results(reversed_fake),
                                            scope={m["manifest"] for m in reversed_fake})
        check("successor: verdict is order-independent",
              sorted(r["re_pinned"] for r in records)
              == sorted(r["re_pinned"] for r in reversed_records))
        check("successor: the row's own manifest is not its own successor",
              all(r["manifest"] not in r["successors"] for r in records))
        # the scope/index split is the finding: a successor OUTSIDE the swept
        # scope must read declared_successors=True while re_pinned_in_scope is
        # False. Collapsing the two would hide exactly the round-28 case.
        outside = [{"manifest": "tools/gates/frozen/round-18/MANIFEST.tsv",
                    "results": [frozen_old]}]
        index = index_from_results(outside)
        index[("tools/gates/x.py", "a.yml")].append(
            ("reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv", live))
        records = sweep_successors(outside, index=index,
                                   scope={"tools/gates/frozen/round-18/MANIFEST.tsv"})
        check("successor: an out-of-scope successor reads declared but not in-scope",
              records[0]["re_pinned"] and not records[0]["re_pinned_in_scope"])
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
    parser.add_argument("--no-probe", action="store_true")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()

    tmpdir = tempfile.gettempdir()
    try:
        Path(tmpdir).resolve().relative_to(ROOT.resolve())
        tmpdir_inside = True
    except ValueError:
        tmpdir_inside = False

    gates_paths, report_paths = manifest_paths()
    manifests = sweep_manifests(gates_paths, "tools/gates/frozen") \
        + sweep_manifests(report_paths, "reports/**/tests/frozen")
    baselines = sweep_baselines()
    global SCOPE_MANIFESTS
    SCOPE_MANIFESTS = {m["manifest"] for m in manifests}
    successors = sweep_successors(manifests)
    summary = summarise(manifests, baselines, successors)

    scope = {}
    for manifest in manifests:
        scope.setdefault(manifest["root"], []).append(manifest)

    receipt = {
        "tool": "reports/round-28/audit/x61-pin-sweep.py",
        "seat": "R28-X61",
        "date": "2026-10-18",
        "command": "python3 -B reports/round-28/audit/x61-pin-sweep.py --json",
        "head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True,
                               text=True).stdout.strip(),
        "python": sys.version.split()[0],
        "tmpdir": tmpdir,
        "tmpdir_inside_repo": tmpdir_inside,
        "scope": {root: [{"manifest": m["manifest"], "rows": m["rows"]} for m in entries]
                  for root, entries in scope.items()},
        "manifests": manifests,
        "baselines": baselines,
        "successors": successors,
        "summary": summary,
    }
    if not args.no_probe:
        probe_manifest = FROZEN / "round-26" / "post-register" / "MANIFEST.tsv"
        if probe_manifest.is_file():
            receipt["tmpdir_probe"] = {
                "manifest": str(probe_manifest.relative_to(ROOT)),
                "runs": tmpdir_probe(probe_manifest,
                                     [("inside-repo", str(ROOT / ".scratch")),
                                      ("outside-repo", tmpdir)]),
            }

    print(json.dumps(receipt, indent=1, sort_keys=True) if args.json else text_report(receipt))

    if summary["rows_unevaluable"] or summary["baselines_not_pinned"]:
        return 2
    if summary["rows_mismatched"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
