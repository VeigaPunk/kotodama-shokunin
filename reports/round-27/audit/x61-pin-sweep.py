#!/usr/bin/env python3
"""R27-X61 — independent D4 pin sweep (read-only; own re-derivation).

This is the X61 double-check of the round-27 claim-O pin surface. It does NOT
call `tools/replay-frozen.py`; it re-derives every frozen row itself so a defect
in that tool cannot hide behind it (and so its own verdict is comparable).

Three duties, one receipt:

  A. MANIFEST sweep — for every `MANIFEST.tsv` under `tools/gates/frozen/**`,
     verify per row, before any gate runs:
       * `gate_sha256` against the live gate bytes;
       * `input_sha256` against the committed snapshot under `input_snapshot`;
       * `output_sha256` against the recorded output file;
     then re-execute the gate in a mirror whose real path is OUTSIDE the repo
     (the round-27 TMPDIR trap: `TMPDIR=$PWD/.scratch` makes every row
     `mirror_unsafe`) and compare exit code, `^FINDING ` count and output bytes
     against the record.

  B. BASELINE sweep — for every `expected.json` under the three roots
     `tools/check-gate-battery.py` discovers (`tools/gates/expected/`,
     `tools/gates/frozen/`, `reports/round-9/baselines/`), verify the
     `gate_sha256` pin against the live gate and every declared `inputs` digest
     against the snapshot bytes inside the baseline directory. A baseline is
     never re-executed here; `pinned` means the digests hold.

  C. TMPDIR sensitivity probe — the same manifest replayed twice, once with the
     mirror parent inside the repo and once outside, so the difference between
     "0 reproduced, N mirror_unsafe" and the real verdict is measured rather
     than asserted.

Exit codes:
  0  every evaluated row reproduced its record and every pin held
  1  at least one evaluated row mismatched its record (a reproduced red verdict
     is still a red verdict; this tool reports reproduction, never quality)
  2  could-not-evaluate: a pin failed verification, a path is unsafe, or the
     manifest/baseline is malformed — exit 2 outranks exit 1

Nothing is written inside the repository: the mirror is a self-cleaning temp
directory, and `--json`/`--md` receipts go to stdout only.

Usage:
    export TMPDIR=/tmp            # OUTSIDE the repo, or every row reads mirror_unsafe
    python3 -B reports/round-27/audit/x61-pin-sweep.py            # text
    python3 -B reports/round-27/audit/x61-pin-sweep.py --json     # receipt
    python3 -B reports/round-27/audit/x61-pin-sweep.py --selftest # in-memory controls
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
GATE_PARTS = ("tools", "gates")
FINDING_PREFIX = "FINDING "
COLUMNS = (
    "gate", "gate_sha256", "input", "input_sha256", "exit_code",
    "finding_count", "output", "output_sha256", "input_snapshot", "command",
)
HEX = frozenset("0123456789abcdef")
TIMEOUT = 120
# The nine registered gates, verbatim from tools/check-gate-battery.py:134. A
# baseline may declare its gate by script path, by bare name, or only through
# its own directory name, so all three spellings must resolve — reading only
# `gate_script` would report a false `no gate_script field` finding on the
# round-9 baselines, which carry neither.
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
    """A row that could not be evaluated, carrying a stable machine id."""

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
    """Map a declared gate label (with or without `.py`) onto a script name."""
    if not isinstance(value, str) or not value.strip():
        return None
    candidate = value.strip()
    for name in REGISTERED_GATES:
        if candidate in (name, name[:-3]) or Path(candidate).name in (name, name[:-3]):
            return name
    return None


def implied_gate(baseline_rel):
    """Resolve a gate from the baseline path: <gate>/<baseline-id>/expected.json."""
    for component in Path(baseline_rel).parts:
        resolved = gate_script_name(component)
        if resolved:
            return resolved
    return None


def safe_path(raw, what, root=None):
    """Resolve a manifest path inside the repo, refusing traversal and symlinks."""
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
    return len(segments) == 3 and tuple(segments[:2]) == GATE_PARTS and segments[2].endswith(".py")


def read_manifest(path):
    """(rows, problems): rows are dicts keyed by COLUMNS; problems are strings."""
    rows, problems = [], []
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    if not lines:
        return rows, ["manifest is empty"]
    header = lines[0].split("\t")
    if tuple(header) != COLUMNS:
        return rows, [f"header is not the documented column schema: {header!r}"]
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


def classify_mismatch(live_input_sha256, pinned_sha256):
    """The D20 §3.1 classification, as a pure function so it can be controlled.

    A mismatch is a *supersession* when the live input the row names no longer
    hashes to the row's own `input_sha256` — a later generation moved it. When
    the live input still hashes to its pin, nothing superseded the row and the
    divergence is genuine *drift*. An unreadable input is neither: absence is
    never evidence that bytes moved.
    """
    if live_input_sha256 is None:
        return "unknown"
    return "supersession" if live_input_sha256 != pinned_sha256 else "drift"


def verify_row(row, manifest_dir, tmpdir=None):
    """Pin-check one row. Returns a result dict; raises nothing.

    `tmpdir` names the parent for the replay mirror explicitly, so a caller can
    probe the TMPDIR sensitivity without mutating process-global state.
    """
    result = {"row": row["_row"], "gate": row["gate"], "input": row["input"]}
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

    result.update(launched=True,
                  exit=observed["exit"], recorded_exit=int(row["exit_code"]),
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
    # The D20 §3.1 classification, re-derived rather than quoted: a mismatch is
    # a supersession when the LIVE input the row names no longer hashes to the
    # row's own input_sha256; when it does, nothing superseded the row and the
    # divergence is genuine drift.
    if not agrees:
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
    """Execute the pinned gate on the snapshot inside a temp mirror.

    The mirror's real path must be outside the repo: a mirror inside the tree
    would let a gate write back into the lane it measures.
    """
    if tmpdir is None:
        tmpdir = tempfile.gettempdir()
    mirror = Path(tempfile.mkdtemp(prefix="x61-mirror-", dir=tmpdir))
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


def sweep_manifests(tmpdir=None):
    manifests = []
    for path in sorted(FROZEN.rglob("MANIFEST.tsv")):
        rows, problems = read_manifest(path)
        results = [verify_row(row, path.parent, tmpdir=tmpdir) for row in rows]
        tally = {"reproduced": 0, "mismatch": 0, "could-not-evaluate": 0}
        for item in results:
            tally[item["status"]] += 1
        manifests.append({
            "manifest": str(path.relative_to(ROOT)),
            "rows": len(rows),
            "problems": problems,
            "tally": tally,
            "results": results,
        })
    return manifests


def sweep_baselines():
    """Every committed baseline under ALL THREE battery roots.

    `tools/check-gate-battery.py` discovers `expected.json` under
    `tools/gates/expected/`, `tools/gates/frozen/` and the legacy
    `reports/round-9/baselines/`. Globbing only the first root would miss the
    ten baselines that live under `tools/gates/frozen/**` and report a
    smaller, flatter "all pinned" than the tree supports — the completeness
    defect a peer auditor named on this tool's first draft.
    """
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


def summarise(manifests, baselines):
    rows = sum(m["rows"] for m in manifests)
    items = [item for m in manifests for item in m["results"]]
    return {
        "manifests": len(manifests),
        "manifest_rows": rows,
        "rows_reproduced": sum(m["tally"]["reproduced"] for m in manifests),
        "rows_mismatched": sum(m["tally"]["mismatch"] for m in manifests),
        "rows_unevaluable": sum(m["tally"]["could-not-evaluate"] for m in manifests),
        "mismatch_supersession": sum(1 for i in items if i.get("class") == "supersession"),
        "mismatch_drift": sum(1 for i in items if i.get("class") == "drift"),
        "gate_digest_mismatch": sum(1 for i in items if i.get("reason") == "gate_digest_mismatch"),
        "baselines": len(baselines),
        "baselines_pinned": sum(1 for b in baselines if b["verdict"] == "pinned"),
        "baselines_not_pinned": sum(1 for b in baselines if b["verdict"] != "pinned"),
        "baseline_findings": sum(len(b["findings"]) for b in baselines),
        "baseline_inputs_verified": sum(b.get("inputs_verified", 0) for b in baselines),
    }


def tmpdir_probe(manifest, tmpdirs):
    """Replay one manifest under each mirror parent and record the tally."""
    probe = []
    for label, tmpdir in tmpdirs:
        rows, _ = read_manifest(manifest)
        tally = {"reproduced": 0, "mismatch": 0, "could-not-evaluate": 0, "mirror_unsafe": 0}
        for row in rows:
            item = verify_row(row, manifest.parent, tmpdir=tmpdir)
            tally[item["status"]] += 1
            if item.get("reason") == "mirror_unsafe":
                tally["mirror_unsafe"] += 1
        probe.append({"tmpdir": label, "tally": tally})
    return probe


def text_report(receipt):
    lines = []
    lines.append(f"X61 pin sweep — {receipt['date']} — lane HEAD {receipt['head']}")
    lines.append(f"  TMPDIR={receipt['tmpdir']} (inside_repo={receipt['tmpdir_inside_repo']})")
    for manifest in receipt["manifests"]:
        tally = manifest["tally"]
        lines.append(f"  {manifest['manifest']}: {tally['reproduced']} reproduced, "
                     f"{tally['mismatch']} mismatch, {tally['could-not-evaluate']} could-not-evaluate "
                     f"of {manifest['rows']}")
        for item in manifest["results"]:
            if item["status"] == "reproduced":
                continue
            lines.append(f"    ROW {item['row']} {item['status']} reason={item.get('reason')} "
                         f"gate={item['gate']} input={item['input']}")
            if item.get("class"):
                lines.append(f"      class: {item['class']} "
                             f"(live input moved={item.get('live_input_moved')})")
            if item.get("detail"):
                lines.append(f"      detail: {item['detail']}")
        for problem in manifest["problems"]:
            lines.append(f"    PROBLEM: {problem}")
    for baseline in receipt["baselines"]:
        lines.append(f"  {baseline['baseline']}: {baseline['verdict']} "
                     f"(inputs {baseline.get('inputs_verified')}/{baseline.get('inputs_declared')})")
        for finding in baseline["findings"]:
            lines.append(f"    FINDING: {finding}")
    summary = receipt["summary"]
    lines.append(f"  summary: {summary['rows_reproduced']}/{summary['manifest_rows']} rows reproduced; "
                 f"{summary['rows_mismatched']} mismatch "
                 f"({summary['mismatch_supersession']} supersession, {summary['mismatch_drift']} drift); "
                 f"{summary['rows_unevaluable']} could-not-evaluate "
                 f"({summary['gate_digest_mismatch']} gate_digest_mismatch); "
                 f"baselines {summary['baselines_pinned']}/{summary['baselines']} pinned")
    if "tmpdir_probe" in receipt:
        lines.append(f"  TMPDIR probe on {receipt['tmpdir_probe']['manifest']}:")
        for run in receipt["tmpdir_probe"]["runs"]:
            tally = run["tally"]
            lines.append(f"    {run['tmpdir']}: {tally['reproduced']} reproduced, "
                         f"{tally['mismatch']} mismatch, {tally['could-not-evaluate']} could-not-evaluate "
                         f"({tally['mirror_unsafe']} mirror_unsafe)")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Selftest — in-memory controls; never touches the lane's frozen surface
# --------------------------------------------------------------------------

def selftest():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    header = "\t".join(COLUMNS)
    sample = (f"{header}\n"
              f"tools/gates/naming-collision-gate.py\t{'a' * 64}\texamples/x.yml\t{'b' * 64}\t"
              f"0\t0\tout.out\t{'c' * 64}\texamples/x.yml\tpython3 x\n")
    tmp = Path(tempfile.mkdtemp(prefix="x61-selftest-"))
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
        item = verify_row(bad, tmp)
        check("bad digest pin refused", item["status"] == "could-not-evaluate"
              and item["reason"] == "record_malformed")

        bad2 = dict(bad)
        bad2["gate_sha256"] = "a" * 64
        bad2["gate"] = "tools/replay-frozen.py"
        item = verify_row(bad2, tmp)
        check("non-whitelisted gate refused", item["status"] == "could-not-evaluate"
              and item["reason"] == "gate_not_whitelisted")

        for raw, what, reason in (("../../etc/passwd", "gate", "gate_unsafe_path"),
                                  ("tools/gates/../gates/x.py", "gate", "gate_unsafe_path"),
                                  ("--selftest", "gate", "gate_unsafe_path"),
                                  ("/etc/passwd", "gate", "gate_unsafe_path"),
                                  ("~/x", "gate", "gate_unsafe_path")):
            try:
                safe_path(raw, what)
                check(f"unsafe path refused: {raw}", False)
            except Refused as refused:
                check(f"unsafe path refused: {raw}", refused.reason == reason)

        check("legal path resolves", safe_path("tools/replay-frozen.py", "gate").is_file())

        try:
            run_in_mirror(ROOT / "tools" / "replay-frozen.py", ROOT / "tools" / "replay-frozen.py",
                          "tools/replay-frozen.py", tmpdir=str(ROOT / ".scratch"))
            check("in-repo mirror refused", False)
        except Refused as refused:
            check("in-repo mirror refused", refused.reason == "mirror_unsafe")

        payload = b"FINDING a\nok x\nFINDING b\nFINDINGX c\n"
        check("finding count is prefix-anchored", count_findings(payload) == 2)

        # the D20 §3.1 classifier: a moved live input is a supersession, an
        # unmoved one is genuine drift, and an unreadable one is neither.
        check("classifier: moved input is supersession",
              classify_mismatch("b" * 64, "a" * 64) == "supersession")
        check("classifier: unmoved input is drift",
              classify_mismatch("a" * 64, "a" * 64) == "drift")
        check("classifier: unreadable input is unknown",
              classify_mismatch(None, "a" * 64) == "unknown")
        # negative control: a missing live file must not read as a supersession —
        # an absent input is not evidence that bytes moved.
        check("classifier: missing input is not supersession",
              classify_mismatch(None, "a" * 64) != "supersession")

        # the gate resolver accepts all three documented spellings
        check("gate resolves from bare name", gate_script_name("myth-consistency-gate") == "myth-consistency-gate.py")
        check("gate resolves from script path",
              gate_script_name("tools/gates/myth-consistency-gate.py") == "myth-consistency-gate.py")
        check("gate resolves from baseline path",
              implied_gate("tools/gates/expected/phonology-sanity-gate/r9-pre/expected.json")
              == "phonology-sanity-gate.py")
        check("unknown gate is not guessed", gate_script_name("not-a-gate") is None)
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
    parser.add_argument("--json", action="store_true", help="emit a JSON receipt on stdout")
    parser.add_argument("--selftest", action="store_true", help="in-memory controls only")
    parser.add_argument("--no-probe", action="store_true", help="skip the TMPDIR sensitivity probe")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()

    tmpdir = tempfile.gettempdir()
    try:
        Path(tmpdir).resolve().relative_to(ROOT.resolve())
        tmpdir_inside = True
    except ValueError:
        tmpdir_inside = False

    manifests = sweep_manifests()
    baselines = sweep_baselines()
    summary = summarise(manifests, baselines)

    receipt = {
        "tool": "reports/round-27/audit/x61-pin-sweep.py",
        "seat": "R27-X61",
        "date": "2026-10-18",
        "command": "python3 -B reports/round-27/audit/x61-pin-sweep.py --json",
        "head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True,
                               text=True).stdout.strip(),
        "python": sys.version.split()[0],
        "tmpdir": tmpdir,
        "tmpdir_inside_repo": tmpdir_inside,
        "manifests": manifests,
        "baselines": baselines,
        "summary": summary,
    }
    if not args.no_probe:
        probe_manifest = FROZEN / "round-26" / "post-register" / "MANIFEST.tsv"
        if probe_manifest.is_file():
            receipt["tmpdir_probe"] = {
                "manifest": str(probe_manifest.relative_to(ROOT)),
                "runs": tmpdir_probe(probe_manifest,
                                     [("inside-repo", str(ROOT / ".scratch")),
                                      ("outside-repo", str(tempfile.gettempdir()))]),
            }

    if args.json:
        print(json.dumps(receipt, indent=1, sort_keys=True))
    else:
        print(text_report(receipt))

    if summary["rows_unevaluable"] or summary["baselines_not_pinned"]:
        return 2
    if summary["rows_mismatched"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
