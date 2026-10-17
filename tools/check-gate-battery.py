#!/usr/bin/env python3
"""Isolated battery for the seven legacy gate selftests, plus the baseline check.

Two duties, one report.

1. Gate selftests (unchanged). Stdlib only. Copies the seven tools/gates/*.py
   scripts and their fixture tree into a disposable mirror directory, runs each
   ``--selftest`` there, and never invokes a gate on a live path. Before and
   after the run it snapshots the live tree (per-file sha256 AND the path set of
   the seven scripts + fixture tree), so "originals preserved" is measured, not
   assumed: modified bytes, added files and deleted files under the live gates
   tree are all detected. Note what this proves: matching hashes prove byte
   preservation, not absence of writes — a rewrite with identical bytes passes;
   a new file or a deletion does not.

2. Committed baseline validation (round 9, claim O15). Discovers every committed
   ``expected.json`` under the baseline roots (default ``tools/gates/expected/``
   and ``tools/gates/frozen/``) and verifies, per
   ``corpus/knowledge/verification/gate-frozen-run-standard.md`` §4/§6: every
   declared input digest against the snapshot bytes inside the baseline, the
   ``gate_sha256`` pin against the live gate script, the declared gate against
   the seven-name constant, and the shape of the ``expected`` verdict block.
   A baseline is never re-executed here: reading ``pinned`` means the digests
   and pins hold, not that the verdict was compared — the comparison is the
   baseline's own re-run receipt. Tampered snapshot bytes, a missing or empty
   ``inputs`` map (``unpinned (legacy)``), an unnamed gate revision, an unknown
   or unreadable baseline, an input resolved outside the baseline, and any of
   the seven gates without a committed baseline all read could-not-evaluate and
   force exit 2. A tampered baseline is never a silent pass.

Exit codes:
  0  all seven gate selftests passed (exit 0), the original tree preserved, every
     discovered baseline pinned, and all seven gates covered
  1  at least one gate selftest ran, exited 1, AND printed recognizable stable
     failure evidence (see below) — treated as a genuine test failure
  2  could-not-evaluate: gate file missing, copy mismatch, live tree changed,
     launch error, timeout, abnormal exit, a child that exited 1 without
     recognizable stable failure evidence (conservatively read as a crash), or
     any baseline finding (tamper, revision, unpinned, uncovered gate, ...)

Baseline vocabulary (deliberately the frozen-run standard's, §6): reading
``snapshot_tampered``, ``gate_revised``, ``unpinned (legacy)``, ``no baseline`` or
``pinned``; class/exit is the standard's 0/1 verdict mapping, 2 reserved for
could-not-evaluate. ``stdout_sha256`` is verified against ``run.log`` when both
exist and reported as an advisory pin — per §4 it is never the finding contract
and never changes the exit code.

Conservative exit-1 rule: an exit-1 child maps to "genuine failure" only when
its captured output contains at least one line-anchored failure marker drawn
from the legacy gates' own conventions — a line starting with
``SELFTEST FAIL`` (provenance-audit.py, lexicon-coverage-audit.py spawn
failure), ``FAIL <token>`` (lexicon-coverage-audit.py check printer,
check-craft-exercise.py finding printer), or ``failed: <token>``
(lexicon-coverage-audit.py failure summary). An exit-1 child without such
evidence — e.g. an uncaught Python traceback — is reported as unevaluable with
a stable ``GATE-CRASH-EXIT1`` finding and forces exit 2; it is never surfaced
as a genuine finding. Documented consequence: five of the seven legacy gates
(costume-era, handoff, myth, naming, phonology) assert with bare ``assert``
statements, so a genuine selftest failure in those gates is crash-shaped and
will classify as exit 2, not exit 1. The battery still reports a nonzero,
not-green result either way; it only refuses to vouch for which kind.

The gate list is a fixed constant in this file. Nothing is ever executed from
a manifest and no shell string is built: each child is launched as
[sys.executable, <resolved gate path>, "--selftest"] with shell=False. No gate
script is modified by, or reachable from, the baseline check (it reads bytes
only), and baseline paths are never followed outside the baseline directory.

Usage:
  python3 tools/check-gate-battery.py [--timeout S] [--keep-mirror]
  python3 tools/check-gate-battery.py [--baselines-root PATH]
  python3 tools/check-gate-battery.py --selftest

``--timeout`` must be a positive finite number of seconds; zero, negative,
non-numeric or non-finite values are rejected as usage errors (exit 2).
``--baselines-root`` replaces the default baseline roots for one run and exists
for tamper drills on a copied tree; it is not a way to silence a committed
baseline defect.
"""
import argparse
import hashlib
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

GATE_NAMES = (
    "costume-era-consistency-gate.py",
    "handoff-packet-check.py",
    "lexicon-coverage-audit.py",
    "myth-consistency-gate.py",
    "naming-collision-gate.py",
    "phonology-sanity-gate.py",
    "provenance-audit.py",
)
FIXTURE_DIRNAME = "fixtures"
HERE = Path(__file__).resolve().parent
GATES_DIR = HERE / "gates"
DEFAULT_TIMEOUT = 120.0
STREAM_HEAD = 2000
STREAM_TAIL = 600
STABLE_ID_RE = re.compile(r"^[A-Z][A-Z0-9-]+$")
FAILURE_MARKER_RES = (
    re.compile(r"^SELFTEST FAIL", re.MULTILINE),
    re.compile(r"^FAIL \S", re.MULTILINE),
    re.compile(r"^failed: \S", re.MULTILINE),
)
BASELINE_SCHEMA = "kotodama-frozen-run-v1"
BASELINE_ROOTS = (GATES_DIR / "expected", GATES_DIR / "frozen")
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
# Value-bearing reading per gate-frozen-run-standard.md §6; earlier wins.
BASELINE_READING_ORDER = (
    "snapshot_tampered",
    "gate_revised",
    "gate_unpinned",
    "unpinned (legacy)",
    "no baseline",
)
BASELINE_STATE_READING = {
    "snapshot_tampered": "snapshot_tampered",
    "gate_revised": "gate_revised",
    "gate_unpinned": "gate_unpinned",
    "unpinned": "unpinned (legacy)",
    "path_escape": "no baseline",
    "input_external": "no baseline",
    "input_missing": "no baseline",
    "malformed": "no baseline",
    "expected_malformed": "no baseline",
    "gate_unknown": "no baseline",
}
STDERR_TAIL_NOTE = "verdicts are read from declared findings, never from stdout order (§4)"


def positive_float(text):
    try:
        value = float(text)
    except ValueError:
        raise argparse.ArgumentTypeError(f"not a number: {text!r}")
    if not math.isfinite(value) or value <= 0:
        raise argparse.ArgumentTypeError(
            f"timeout must be a positive finite number of seconds, got {text!r}"
        )
    return value


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def battery_paths(base):
    """File paths of a gates tree (original or mirror): scripts + fixture tree."""
    paths = [base / name for name in GATE_NAMES]
    paths.extend(sorted(p for p in (base / FIXTURE_DIRNAME).rglob("*") if p.is_file()))
    return paths


def hash_snapshot(paths, base):
    return {str(p.relative_to(base)): sha256_file(p) for p in paths}


def diff_snapshots(before, after):
    """(modified, added, deleted) key sets between two hash snapshots."""
    modified = sorted(k for k in before if k in after and before[k] != after[k])
    added = sorted(k for k in after if k not in before)
    deleted = sorted(k for k in before if k not in after)
    return modified, added, deleted


def recognized_failure_evidence(text):
    """A Python traceback takes precedence over earlier failure markers."""
    if re.search(r"^Traceback \(most recent call last\):", text, re.MULTILINE):
        return None
    for pattern in FAILURE_MARKER_RES:
        match = pattern.search(text)
        if match:
            return text[match.start():].splitlines()[0][:200]
    return None


def battery_exit(outcomes, findings):
    if any(f["id"] != "GATE-SELFTEST-FAIL" for f in findings):
        return 2
    outs = [o for o in outcomes if o in ("pass", "fail")]
    if len(outs) != len(outcomes) or not outs:
        return 2
    if "fail" in outs:
        return 1
    return 0


def run_child(label, argv, timeout, cwd):
    """Launch one child as a fixed argv, no shell. Returns a result dict."""
    result = {
        "id": label,
        "argv_head": [argv[0], Path(argv[1]).name, *argv[2:]],
        "observed_exit": None,
        "outcome": "unevaluable",
        "seconds": None,
        "stdout_head": "",
        "stderr_head": "",
        "stderr_tail": "",
        "stdout_truncated": False,
        "stderr_truncated": False,
        "findings": [],
    }
    script = Path(argv[1])
    if not script.is_file():
        result["findings"].append({"id": "GATE-FILE-MISSING", "detail": str(script)})
        return result
    start = time.monotonic()
    try:
        proc = subprocess.run(
            argv,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            errors="replace",
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        result["seconds"] = round(time.monotonic() - start, 3)
        result["findings"].append(
            {"id": "GATE-TIMEOUT", "detail": f"no exit within {timeout}s"}
        )
        return result
    except OSError as exc:
        result["seconds"] = round(time.monotonic() - start, 3)
        result["findings"].append({"id": "GATE-LAUNCH-ERROR", "detail": str(exc)})
        return result
    result["seconds"] = round(time.monotonic() - start, 3)
    result["observed_exit"] = proc.returncode
    for stream, key in (("stdout", "stdout_head"), ("stderr", "stderr_head")):
        text = getattr(proc, stream) or ""
        if len(text) > STREAM_HEAD:
            result[key] = text[:STREAM_HEAD]
            result[key.replace("head", "truncated")] = True
        else:
            result[key] = text
    stderr = proc.stderr or ""
    result["stderr_tail"] = stderr[-STREAM_TAIL:] if stderr else ""

    if proc.returncode == 0:
        result["outcome"] = "pass"
    elif proc.returncode == 1:
        evidence = recognized_failure_evidence((proc.stdout or "") + "\n" + stderr)
        if evidence:
            result["outcome"] = "fail"
            result["findings"].append(
                {
                    "id": "GATE-SELFTEST-FAIL",
                    "detail": f"selftest exited 1 with stable evidence: {evidence}",
                }
            )
        else:
            result["outcome"] = "unevaluable"
            result["findings"].append(
                {
                    "id": "GATE-CRASH-EXIT1",
                    "detail": "exit 1 with a Python traceback or without stable failure evidence; "
                    "conservatively treated as a crashed child, not a finding",
                }
            )
    elif proc.returncode == 2:
        result["outcome"] = "unevaluable"
        result["findings"].append(
            {"id": "GATE-UNEVALUABLE-EXIT", "detail": "selftest exited 2"}
        )
    else:
        result["outcome"] = "unevaluable"
        result["findings"].append(
            {"id": "GATE-ABNORMAL-EXIT", "detail": f"exit {proc.returncode}"}
        )
    return result


def flatten_findings(results):
    findings = []
    for res in results:
        for f in res["findings"]:
            findings.append({"gate": res["id"], **f})
    return findings


# ---------------------------------------------------------------------------
# Committed baseline validation (round-9 claim O15). Read-only: opens snapshot
# and gate files for hashing, writes nothing, and never launches a gate. The
# contract is gate-frozen-run-standard.md §4 (required fields) and §6 (verify
# table); the readings are that table's vocabulary.
# ---------------------------------------------------------------------------


def combined_exit(selftest_code, baseline_code):
    """A could-not-evaluate in either duty is the battery's verdict: 2, then 1."""
    return max(selftest_code, baseline_code)


def is_hex64(value):
    return isinstance(value, str) and bool(HEX64_RE.match(value))


def gate_script_name(value, gate_names):
    """Map a declared gate label (with or without ``.py``) onto a script name."""
    if not isinstance(value, str) or not value.strip():
        return None
    candidate = value.strip()
    for name in gate_names:
        if candidate in (name, name[:-3]):
            return name
    return None


def implied_gate(label, gate_names):
    """Resolve a gate from the baseline path: <gate>/<baseline-id>/expected.json."""
    parts = Path(label).parts
    for component in parts:
        resolved = gate_script_name(component, gate_names)
        if resolved:
            return resolved
    stem = Path(label).name
    for suffix in (".expected.json", ".json"):
        if stem.endswith(suffix):
            return gate_script_name(stem[: -len(suffix)], gate_names)
    return None


def expand_baseline_specs(doc, gate_names):
    """(label_suffix, spec, implied_gate) for the three document shapes a
    committed expected.json may take: one baseline object, a ``baselines`` /
    ``gates`` collection (list or map), or a top-level map keyed by gate name."""
    if isinstance(doc, dict):
        for key in ("baselines", "gates"):
            collection = doc.get(key)
            if isinstance(collection, list):
                return [(f"{key}[{i}]", item, None) for i, item in enumerate(collection)]
            if isinstance(collection, dict):
                return [
                    (f"{key}[{name}]", value, gate_script_name(name, gate_names))
                    for name, value in collection.items()
                ]
        if doc and not any(
            key in doc for key in ("gate", "inputs", "expected", "gate_sha256")
        ):
            if all(gate_script_name(key, gate_names) for key in doc):
                return [
                    (f"gate[{name}]", value, gate_script_name(name, gate_names))
                    for name, value in doc.items()
                ]
        return [("", doc, None)]
    if isinstance(doc, list):
        return [(f"[{i}]", item, None) for i, item in enumerate(doc)]
    return [("", doc, None)]


def normalize_inputs(raw):
    """(entries, error): entries are [(path, digest)]; a malformed map is refused."""
    if raw is None:
        return None, "absent"
    if isinstance(raw, dict):
        if not raw:
            return [], None
        entries = []
        for path, value in raw.items():
            if isinstance(value, dict):
                value = value.get("sha256") or value.get("digest")
            entries.append((path, value))
        return entries, None
    if isinstance(raw, list):
        if not raw:
            return [], None
        entries = []
        for item in raw:
            if not isinstance(item, dict) or "path" not in item:
                return None, "list entry is not a path/sha256 record"
            entries.append((item.get("path"), item.get("sha256") or item.get("digest")))
        return entries, None
    return None, "not a path->sha256 mapping"


def find_expected_files(root):
    """Every committed expected.json under a baseline root (exact or *.expected)."""
    if not root.is_dir():
        return []
    found = set()
    for pattern in ("expected.json", "*.expected.json"):
        found.update(path for path in root.rglob(pattern) if path.is_file())
    return sorted(found)


def baseline_failure_record(label, finding_id, detail):
    """A record shaped like verify_baseline_spec's for unreadable/unparsable files."""
    return {
        "baseline": label,
        "gate": None,
        "reading": "no baseline",
        "inputs_checked": 0,
        "gate_sha256": {"declared": None, "actual": None, "reading": "not-checked"},
        "expected": None,
        "stdout_pin": {"declared": None, "actual": None, "reading": "not-checked"},
        "findings": [{"id": finding_id, "detail": detail, "state": "malformed"}],
        "verdict_replay": "not-run: the baseline could not be read",
    }


def verify_baseline_spec(spec, label, base_dir, gates_dir, repo_root, gate_names, hint_gate=None):
    """Verify input digests and pins for one baseline spec; never re-executes a gate."""
    record = {
        "baseline": label,
        "gate": None,
        "reading": "pinned",
        "inputs_checked": 0,
        "gate_sha256": {"declared": None, "actual": None, "reading": "not-checked"},
        "expected": None,
        "stdout_pin": {"declared": None, "actual": None, "reading": "not-checked"},
        "findings": [],
        "verdict_replay": "not-run: digests and pins verified only; the verdict "
                          "comparison is the baseline's own re-run receipt",
    }
    findings = record["findings"]

    def add(state, finding_id, detail):
        findings.append({"id": finding_id, "detail": detail, "state": state})

    declared_gate = spec.get("gate") if isinstance(spec, dict) else None
    gate_name = (
        gate_script_name(declared_gate, gate_names)
        or gate_script_name(hint_gate, gate_names)
        or implied_gate(label, gate_names)
    )
    record["gate"] = gate_name
    if gate_name is None:
        add("gate_unknown", "BASELINE-GATE-UNKNOWN",
            f"declared gate {declared_gate!r} is not one of the seven registered gates")

    if gate_name:
        script = gates_dir / gate_name
        if not script.is_file():
            add("gate_unknown", "BASELINE-GATE-UNKNOWN", f"gate script not found: {script}")
        else:
            actual_gate_sha = sha256_file(script)
            declared_sha = spec.get("gate_sha256") if isinstance(spec, dict) else None
            record["gate_sha256"] = {
                "declared": declared_sha, "actual": actual_gate_sha, "reading": "absent"}
            if declared_sha is None:
                add("gate_unpinned", "BASELINE-GATE-UNPINNED",
                    "no gate_sha256: the baseline names no gate revision, so its verdict "
                    "cannot be compared across one (§6 step 2)")
            elif not is_hex64(str(declared_sha).lower()):
                record["gate_sha256"]["reading"] = "malformed"
                add("malformed", "BASELINE-MALFORMED",
                    "gate_sha256 is not 64 hex digits")
            elif str(declared_sha).lower() != actual_gate_sha:
                record["gate_sha256"]["reading"] = "gate_revised"
                add("gate_revised", "BASELINE-GATE-REVISED",
                    f"gate_sha256 {str(declared_sha)[:16]}... differs from the live "
                    f"{gate_name} {actual_gate_sha[:16]}...: re-freeze, never compare "
                    "across an unnamed revision")
            else:
                record["gate_sha256"]["reading"] = "match"

    raw_inputs = spec.get("inputs") if isinstance(spec, dict) else None
    entries, error = normalize_inputs(raw_inputs)
    if entries is None:
        add("malformed", "BASELINE-MALFORMED-INPUTS", f"inputs {error}")
    elif not entries:
        add("unpinned", "BASELINE-UNPINNED",
            "inputs absent or empty: unpinned legacy baseline, held for reading and "
            "barred from any conformance claim (§4)")
    else:
        for path, digest in entries:
            if not isinstance(path, str) or not path:
                add("malformed", "BASELINE-MALFORMED-INPUTS", "inputs key is not a path string")
                continue
            if not is_hex64(str(digest).lower()):
                add("malformed", "BASELINE-MALFORMED-INPUTS",
                    f"{path}: digest is not 64 hex digits")
                continue
            relative = Path(path)
            if relative.is_absolute() or ".." in relative.parts:
                add("path_escape", "BASELINE-PATH-ESCAPE",
                    f"{path}: input path leaves the baseline directory; refused unread")
                continue
            target = base_dir / relative
            external_at = None
            if not target.is_file():
                for candidate_root in (gates_dir, repo_root):
                    candidate = candidate_root / relative
                    if candidate.is_file():
                        target, external_at = candidate, candidate_root
                        break
            if not target.is_file():
                add("input_missing", "BASELINE-INPUT-MISSING",
                    f"{path}: no such file inside the baseline or the fixed roots")
                continue
            actual = sha256_file(target)
            record["inputs_checked"] += 1
            if external_at is not None:
                add("input_external", "BASELINE-EXTERNAL-INPUT",
                    f"{path}: resolved to {target} outside the baseline; §3 requires a "
                    "committed copy inside it")
            if actual != str(digest).lower():
                add("snapshot_tampered", "BASELINE-TAMPERED",
                    f"{path}: digest {actual[:16]}... does not match the pin "
                    f"{str(digest)[:16]}...")

    expected = spec.get("expected") if isinstance(spec, dict) else None
    if not isinstance(expected, dict):
        add("expected_malformed", "BASELINE-EXPECTED-ABSENT",
            "no `expected` block: nothing to compare the run against (§4)")
    else:
        code = expected.get("exit")
        declared_class = expected.get("class")
        names = expected.get("findings")
        record["expected"] = {
            "exit": code,
            "class": declared_class,
            "findings": names if isinstance(names, list) else None,
        }
        if code not in (0, 1):
            add("expected_malformed", "BASELINE-EXPECTED-MALFORMED",
                f"expected.exit {code!r} is not 0 or 1 (§4; 2 is could-not-evaluate)")
        if declared_class is not None:
            want = {0: "clean", 1: "findings"}.get(code)
            if declared_class not in ("clean", "findings") or (want and declared_class != want):
                add("expected_malformed", "BASELINE-CLASS-MISMATCH",
                    f"expected.class {declared_class!r} contradicts expected.exit {code!r}")
        if names is not None and (
            not isinstance(names, list) or not all(isinstance(n, str) and n for n in names)
        ):
            add("expected_malformed", "BASELINE-FINDINGS-MALFORMED",
                "expected.findings is not a list of non-empty finding-id strings")
        elif isinstance(names, list):
            if code == 0 and names:
                add("expected_malformed", "BASELINE-EXPECTED-INCONSISTENT",
                    "expected.exit 0 (clean) declared with a non-empty finding set")
            if code == 1 and not names:
                add("expected_malformed", "BASELINE-EXPECTED-INCONSISTENT",
                    "expected.exit 1 declared with an empty finding set: no finding-ID "
                    "set to compare")

    declared_stdout = spec.get("stdout_sha256") if isinstance(spec, dict) else None
    if isinstance(declared_stdout, str):
        record["stdout_pin"]["declared"] = declared_stdout
        run_log = base_dir / "run.log"
        if run_log.is_file():
            actual_stdout = sha256_file(run_log)
            record["stdout_pin"]["actual"] = actual_stdout
            record["stdout_pin"]["reading"] = (
                "match" if actual_stdout == declared_stdout.lower() else "mismatch")
        else:
            record["stdout_pin"]["reading"] = "run.log absent"

    readings = {BASELINE_STATE_READING[finding["state"]] for finding in findings}
    for reading in BASELINE_READING_ORDER:
        if reading in readings:
            record["reading"] = reading
            break
    return record


def inspect_baseline_file(path, label, gates_dir, repo_root, gate_names):
    """One committed expected.json -> one or more baseline records."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [baseline_failure_record(label, "BASELINE-UNREADABLE", str(exc))]
    except UnicodeDecodeError as exc:
        return [baseline_failure_record(label, "BASELINE-MALFORMED", f"not UTF-8: {exc}")]
    try:
        doc = json.loads(text)
    except ValueError as exc:
        return [baseline_failure_record(label, "BASELINE-MALFORMED", f"not valid JSON: {exc}")]
    records = []
    for suffix, spec, hint in expand_baseline_specs(doc, gate_names):
        records.append(
            verify_baseline_spec(
                spec,
                label + (f"::{suffix}" if suffix else ""),
                path.parent,
                gates_dir,
                repo_root,
                gate_names,
                hint_gate=hint,
            )
        )
    return records


def inspect_baselines(roots, gates_dir=GATES_DIR, repo_root=HERE.parent, gate_names=GATE_NAMES):
    """Validate every committed expected.json under the roots; return a report dict."""
    records = []
    findings = []
    covered = set()
    root_reports = []
    any_root = False
    for root in roots:
        present = root.is_dir()
        any_root = any_root or present
        files = find_expected_files(root) if present else []
        root_reports.append({"root": str(root), "present": present, "files_found": len(files)})
        for path in files:
            label = f"{root.name}/{path.relative_to(root)}"
            for record in inspect_baseline_file(path, label, gates_dir, repo_root, gate_names):
                records.append(record)
                if record["gate"]:
                    covered.add(record["gate"])
                for finding in record["findings"]:
                    findings.append(
                        {"baseline": record["baseline"], "gate": record["gate"], **finding}
                    )
    uncovered = [name for name in gate_names if name not in covered]
    if not any_root:
        findings.append(
            {
                "baseline": None,
                "gate": None,
                "id": "BASELINE-ROOT-MISSING",
                "detail": "no baseline root is a directory: "
                + ", ".join(str(root) for root in roots),
            }
        )
    elif not records:
        findings.append(
            {
                "baseline": None,
                "gate": None,
                "id": "BASELINE-NONE-FOUND",
                "detail": "no expected.json under the baseline roots: nothing is pinned",
            }
        )
    for name in uncovered:
        findings.append(
            {
                "baseline": None,
                "gate": name,
                "id": "BASELINE-GATE-UNCOVERED",
                "detail": f"{name} has no committed expected.json under the declared roots: "
                "the two-evidences clause is unmet (§6 fail-closed); when the baseline was "
                "committed under another root in the round's evidence, declare that root with "
                "--baselines-root instead of reading this as covered",
            }
        )
    readings = {}
    for record in records:
        readings[record["reading"]] = readings.get(record["reading"], 0) + 1
    pinned = readings.get("pinned", 0)
    return {
        "tool": "check-gate-battery",
        "mode": "baselines",
        "roots": root_reports,
        "baselines": records,
        "findings": findings,
        "summary": {
            "baselines_found": len(records),
            "pinned": pinned,
            "unevaluable": len(records) - pinned,
            "readings": readings,
            "gates_covered": [name for name in gate_names if name in covered],
            "gates_uncovered": uncovered,
            "baseline_exit": 2 if findings else 0,
            "verdict_replay": "not-run: the battery verifies digests and pins; the verdict "
            "comparison belongs to the baseline's own re-run receipt",
        },
    }


def run_battery(timeout, keep_mirror, baseline_roots=BASELINE_ROOTS):
    baseline_report = inspect_baselines(
        baseline_roots, gates_dir=GATES_DIR, repo_root=HERE.parent
    )
    baseline_code = baseline_report["summary"]["baseline_exit"]
    problems = []
    scripts = {name: GATES_DIR / name for name in GATE_NAMES}
    for name, path in scripts.items():
        if not path.is_file():
            problems.append({"gate": name, "id": "GATE-FILE-MISSING", "detail": str(path)})
    fixture_root = GATES_DIR / FIXTURE_DIRNAME
    if not fixture_root.is_dir():
        problems.append(
            {"gate": FIXTURE_DIRNAME, "id": "GATE-FILE-MISSING", "detail": str(fixture_root)}
        )
    if problems:
        return {
            "tool": "check-gate-battery",
            "mode": "battery",
            "results": [],
            "findings": problems,
            "originals": {"files_hashed": 0, "preserved": None},
            "summary": {"battery_exit": combined_exit(2, baseline_code), "pass": 0, "fail": 0,
                        "unevaluable": len(problems)},
            "baselines": baseline_report,
            "mirror": {"root": None, "removed": None},
        }, combined_exit(2, baseline_code)

    before = hash_snapshot(battery_paths(GATES_DIR), GATES_DIR)

    mirror = Path(tempfile.mkdtemp(prefix="gate-battery-"))
    removed = False
    results = []
    findings = []
    try:
        for name, path in scripts.items():
            shutil.copy2(path, mirror / name)
        shutil.copytree(fixture_root, mirror / FIXTURE_DIRNAME)
        after_copy = hash_snapshot(battery_paths(mirror), mirror)
        for key, digest in after_copy.items():
            if before.get(key) != digest:
                problems.append(
                    {
                        "gate": key,
                        "id": "GATE-COPY-MISMATCH",
                        "detail": "mirror copy differs from source bytes",
                    }
                )
        if not problems:
            for name in GATE_NAMES:
                results.append(
                    run_child(
                        name,
                        [sys.executable, str(mirror / name), "--selftest"],
                        timeout=timeout,
                        cwd=mirror,
                    )
                )
        findings = flatten_findings(results) + problems
    finally:
        if not keep_mirror:
            shutil.rmtree(mirror, ignore_errors=True)
            removed = True

    after = hash_snapshot(battery_paths(GATES_DIR), GATES_DIR)
    modified, added, deleted = diff_snapshots(before, after)
    preserved = not (modified or added or deleted)
    if not preserved:
        examples = (
            [f"modified:{k}" for k in modified[:5]]
            + [f"added:{k}" for k in added[:5]]
            + [f"deleted:{k}" for k in deleted[:5]]
        )
        findings.append(
            {
                "gate": "originals",
                "id": "GATE-BYTES-CHANGED",
                "detail": "modified=%d added=%d deleted=%d; %s"
                % (len(modified), len(added), len(deleted), "; ".join(examples)),
            }
        )
    outcomes = [r["outcome"] for r in results]
    code = combined_exit(battery_exit(outcomes, findings), baseline_code)
    report = {
        "tool": "check-gate-battery",
        "mode": "battery",
        "mirror": {"root": str(mirror), "removed": removed},
        "gates": results,
        "findings": findings,
        "originals": {
            "files_hashed_before": len(before),
            "files_hashed_after": len(after),
            "preserved": preserved,
            "modified": len(modified),
            "added": len(added),
            "deleted": len(deleted),
        },
        "baselines": baseline_report,
        "summary": {
            "battery_exit": code,
            "pass": outcomes.count("pass"),
            "fail": outcomes.count("fail"),
            "unevaluable": outcomes.count("unevaluable"),
        },
    }
    return report, code


def write_child(dir_path, name, body):
    path = dir_path / name
    path.write_text(body, encoding="utf-8")
    return path


def expect_control(res, want_exit, want_outcome, want_ids, failures, note):
    checks_ok = res["observed_exit"] == want_exit and res["outcome"] == want_outcome
    ids = {f["id"] for f in res["findings"]}
    checks_ok = checks_ok and want_ids.issubset(ids)
    if not checks_ok:
        failures.append(
            "%s: observed exit=%r outcome=%r ids=%s, expected exit=%r outcome=%r ids⊆%s"
            % (res["id"], res["observed_exit"], res["outcome"], sorted(ids),
               want_exit, want_outcome, sorted(want_ids))
        )
    return checks_ok


def run_selftest():
    """Controls run on synthetic children in their own temp dir; no live path."""
    controls = []
    failures = []
    with tempfile.TemporaryDirectory(prefix="gate-battery-selftest-") as tmp:
        root = Path(tmp)

        pass_child = write_child(root, "pass_child.py", "import sys\nsys.exit(0)\n")
        res = run_child("CTRL-PASS-EXIT0", [sys.executable, str(pass_child)], timeout=30, cwd=root)
        controls.append(res)
        expect_control(res, 0, "pass", set(), failures, "clean pass")

        marker_child = write_child(
            root,
            "marker_child.py",
            "import sys\nprint('SELFTEST FAIL: planted-evidence')\nsys.exit(1)\n",
        )
        res = run_child("CTRL-RECOGNIZED-FAIL", [sys.executable, str(marker_child)], timeout=30, cwd=root)
        controls.append(res)
        expect_control(res, 1, "fail", {"GATE-SELFTEST-FAIL"}, failures, "recognized failure keeps exit 1")
        if battery_exit([res["outcome"]], flatten_findings([res])) != 1:
            failures.append("CTRL-RECOGNIZED-FAIL battery mapping is not exit 1")

        line_child = write_child(
            root,
            "line_child.py",
            "import sys\nprint('FAIL PLANTED-CHECK -- detail')\nprint('failed: PLANTED-CHECK')\nsys.exit(1)\n",
        )
        res = run_child("CTRL-FAIL-LINE-ID", [sys.executable, str(line_child)], timeout=30, cwd=root)
        controls.append(res)
        expect_control(res, 1, "fail", {"GATE-SELFTEST-FAIL"}, failures, "FAIL-line evidence keeps exit 1")
        if battery_exit([res["outcome"]], flatten_findings([res])) != 1:
            failures.append("CTRL-FAIL-LINE-ID battery mapping is not exit 1")

        bare_child = write_child(
            root, "bare_child.py", "import sys\nprint('planted noise')\nsys.exit(1)\n"
        )
        res = run_child("CTRL-EXIT1-UNRECOGNIZED", [sys.executable, str(bare_child)], timeout=30, cwd=root)
        controls.append(res)
        expect_control(
            res, 1, "unevaluable", {"GATE-CRASH-EXIT1"}, failures, "bare exit 1 must not be a finding"
        )
        if battery_exit([res["outcome"]], flatten_findings([res])) != 2:
            failures.append("CTRL-EXIT1-UNRECOGNIZED battery mapping is not exit 2")

        crash_child = write_child(root, "crash_child.py", "raise NameError('boom')\n")
        res = run_child("CTRL-CRASH-EXIT1", [sys.executable, str(crash_child)], timeout=30, cwd=root)
        controls.append(res)
        expect_control(
            res, 1, "unevaluable", {"GATE-CRASH-EXIT1"}, failures, "traceback exit 1 must not be a finding"
        )
        if "NameError" not in res["stderr_tail"]:
            failures.append("CTRL-CRASH-EXIT1 stderr_tail lacks the crash exception")
        if battery_exit([res["outcome"]], flatten_findings([res])) != 2:
            failures.append("CTRL-CRASH-EXIT1 battery mapping is not exit 2")

        mixed_child = write_child(
            root, "marker_then_crash.py", "print('FAIL PLANTED-CHECK: seeded')\nraise NameError('boom')\n"
        )
        res = run_child("CTRL-MARKER-THEN-CRASH", [sys.executable, str(mixed_child)], timeout=30, cwd=root)
        controls.append(res)
        expect_control(
            res, 1, "unevaluable", {"GATE-CRASH-EXIT1"}, failures, "a traceback overrides prior failure evidence"
        )
        if battery_exit([res["outcome"]], flatten_findings([res])) != 2:
            failures.append("CTRL-MARKER-THEN-CRASH battery mapping is not exit 2")

        res = run_child(
            "CTRL-MISSING-GATE", [sys.executable, str(root / "no-such-gate.py")], timeout=30, cwd=root
        )
        controls.append(res)
        expect_control(res, None, "unevaluable", {"GATE-FILE-MISSING"}, failures, "missing gate")
        if battery_exit([res["outcome"]], flatten_findings([res])) != 2:
            failures.append("CTRL-MISSING-GATE battery mapping is not exit 2")

        hang_child = write_child(root, "hang_child.py", "import time\ntime.sleep(30)\n")
        res = run_child("CTRL-TIMEOUT-GATE", [sys.executable, str(hang_child)], timeout=1, cwd=root)
        controls.append(res)
        expect_control(res, None, "unevaluable", {"GATE-TIMEOUT"}, failures, "timeout")
        if battery_exit([res["outcome"]], flatten_findings([res])) != 2:
            failures.append("CTRL-TIMEOUT-GATE battery mapping is not exit 2")

    with tempfile.TemporaryDirectory(prefix="gate-battery-baselines-") as tmp:
        root = Path(tmp)
        gates_root = root / "synthetic-gates"
        gates_root.mkdir()
        fake_gate = gates_root / "fake-gate.py"
        fake_gate.write_text(
            "# synthetic gate for baseline controls\nprint('gate ok')\n", encoding="utf-8"
        )
        fake_sha = sha256_file(fake_gate)
        (gates_root / "other-gate.py").write_text("# second synthetic gate\n", encoding="utf-8")

        def write_baseline(base, snapshot=b"era: test\n", gate="fake-gate", gate_sha="actual",
                           inputs=None, expected=None, extra=None):
            base.mkdir(parents=True, exist_ok=True)
            (base / "packet.yml").write_bytes(snapshot)
            spec = {
                "schema": BASELINE_SCHEMA,
                "gate": gate,
                "expected": expected if expected is not None else {
                    "exit": 1, "class": "findings", "findings": ["F-01"]},
            }
            if gate_sha == "actual":
                spec["gate_sha256"] = fake_sha
            elif gate_sha is not None:
                spec["gate_sha256"] = gate_sha
            spec["inputs"] = inputs if inputs is not None else {
                "packet.yml": sha256_file(base / "packet.yml")}
            if extra:
                spec.update(extra)
            (base / "expected.json").write_text(json.dumps(spec, indent=1), encoding="utf-8")
            return base

        def inspect(root_dir, gate_names=("fake-gate.py",)):
            return inspect_baselines([root_dir], gates_dir=gates_root, repo_root=root,
                                     gate_names=gate_names)

        def rollup(control_id, report, want_exit, want_reading, want_ids, note):
            ids = [{"id": f["id"]} for f in report["findings"]]
            readings = ",".join(sorted({r["reading"] for r in report["baselines"]})) or "-"
            control = {"id": control_id, "observed_exit": report["summary"]["baseline_exit"],
                       "outcome": readings, "findings": ids}
            controls.append(control)
            expect_control(control, want_exit, want_reading, want_ids, failures, note)
            return report

        pinned_root = root / "pinned-root"
        write_baseline(pinned_root / "fake-gate" / "r9-pre")
        report = rollup("CTRL-BASELINE-PINNED", inspect(pinned_root), 0, "pinned", set(),
                        "digests and pins hold -> pinned, exit 0")
        if report["summary"]["pinned"] != 1 or report["summary"]["gates_covered"] != ["fake-gate.py"]:
            failures.append("CTRL-BASELINE-PINNED coverage/count differ")

        tampered_root = root / "tampered-root"
        write_baseline(tampered_root / "fake-gate" / "r9-pre")
        with open(tampered_root / "fake-gate" / "r9-pre" / "packet.yml", "ab") as handle:
            handle.write(b"# tampered byte\n")
        rollup("CTRL-BASELINE-TAMPERED", inspect(tampered_root), 2, "snapshot_tampered",
               {"BASELINE-TAMPERED"}, "one appended byte in the snapshot -> could-not-evaluate")

        unpinned_root = root / "unpinned-root"
        write_baseline(unpinned_root / "fake-gate" / "r9-pre", inputs={})
        rollup("CTRL-BASELINE-UNPINNED", inspect(unpinned_root), 2, "unpinned (legacy)",
               {"BASELINE-UNPINNED"}, "an empty inputs map is an unpinned legacy baseline")

        revised_root = root / "revised-root"
        write_baseline(revised_root / "fake-gate" / "r9-pre", gate_sha="0" * 64)
        rollup("CTRL-BASELINE-GATE-REVISED", inspect(revised_root), 2, "gate_revised",
               {"BASELINE-GATE-REVISED"}, "a foreign gate_sha256 names another revision")

        gate_unpinned_root = root / "gate-unpinned-root"
        write_baseline(gate_unpinned_root / "fake-gate" / "r9-pre", gate_sha=None)
        rollup("CTRL-BASELINE-GATE-UNPINNED", inspect(gate_unpinned_root), 2, "gate_unpinned",
               {"BASELINE-GATE-UNPINNED"}, "no gate_sha256 -> could-not-evaluate")

        malformed_root = root / "malformed-root"
        (malformed_root / "fake-gate" / "r9-pre").mkdir(parents=True)
        (malformed_root / "fake-gate" / "r9-pre" / "expected.json").write_text(
            "{not json", encoding="utf-8")
        rollup("CTRL-BASELINE-MALFORMED", inspect(malformed_root), 2, "no baseline",
               {"BASELINE-MALFORMED"}, "unparsable expected.json is no baseline")

        unknown_root = root / "unknown-root"
        write_baseline(unknown_root / "not-a-gate" / "r9-pre", gate="not-a-gate")
        rollup("CTRL-BASELINE-GATE-UNKNOWN", inspect(unknown_root), 2, "no baseline",
               {"BASELINE-GATE-UNKNOWN"}, "a gate outside the seven-name constant fails closed")

        missing_root = root / "missing-root"
        write_baseline(missing_root / "fake-gate" / "r9-pre", inputs={"absent.yml": "0" * 64})
        rollup("CTRL-BASELINE-INPUT-MISSING", inspect(missing_root), 2, "no baseline",
               {"BASELINE-INPUT-MISSING"}, "a pin with no bytes behind it fails closed")

        escape_root = root / "escape-root"
        outside = root / "escape.txt"
        outside.write_text("outside the baseline\n", encoding="utf-8")
        write_baseline(escape_root / "fake-gate" / "r9-pre",
                       inputs={"../escape.txt": sha256_file(outside)})
        report = rollup("CTRL-BASELINE-PATH-ESCAPE", inspect(escape_root), 2, "no baseline",
                        {"BASELINE-PATH-ESCAPE"},
                        "a digest that would match outside the baseline is still refused")
        if report["baselines"][0]["inputs_checked"] != 0:
            failures.append("CTRL-BASELINE-PATH-ESCAPE hashed a file outside the baseline")

        external_root = root / "external-root"
        (gates_root / "gatesrc.txt").write_text("live input\n", encoding="utf-8")
        write_baseline(external_root / "fake-gate" / "r9-pre",
                       inputs={"gatesrc.txt": sha256_file(gates_root / "gatesrc.txt")})
        rollup("CTRL-BASELINE-EXTERNAL-INPUT", inspect(external_root), 2, "no baseline",
               {"BASELINE-EXTERNAL-INPUT"}, "an input resolved outside the baseline is refused")

        absent_root = root / "expected-absent-root"
        write_baseline(absent_root / "fake-gate" / "r9-pre", extra={"expected": None})
        rollup("CTRL-BASELINE-EXPECTED-ABSENT", inspect(absent_root), 2, "no baseline",
               {"BASELINE-EXPECTED-ABSENT"}, "no expected block -> nothing to compare")

        inconsistent_root = root / "inconsistent-root"
        write_baseline(inconsistent_root / "fake-gate" / "r9-pre",
                       expected={"exit": 0, "class": "clean", "findings": ["F-01"]})
        rollup("CTRL-BASELINE-EXPECTED-INCONSISTENT", inspect(inconsistent_root), 2,
               "no baseline", {"BASELINE-EXPECTED-INCONSISTENT"},
               "a clean exit with declared findings is refused")

        aggregate_root = root / "aggregate-root"
        aggregate_snapshot = aggregate_root / "fake-gate" / "r9-pre" / "packet.yml"
        aggregate_snapshot.parent.mkdir(parents=True)
        aggregate_snapshot.write_bytes(b"era: aggregate\n")
        (aggregate_root / "expected.json").write_text(json.dumps({
            "schema": BASELINE_SCHEMA,
            "gates": {"fake-gate": {
                "gate": "fake-gate",
                "gate_sha256": fake_sha,
                "inputs": {"fake-gate/r9-pre/packet.yml": sha256_file(aggregate_snapshot)},
                "expected": {"exit": 0, "class": "clean", "findings": []},
            }},
        }, indent=1), encoding="utf-8")
        report = rollup("CTRL-BASELINE-AGGREGATE", inspect(aggregate_root), 0, "pinned", set(),
                        "a gates-map document expands to one pinned baseline")
        if report["summary"]["baselines_found"] != 1:
            failures.append("CTRL-BASELINE-AGGREGATE did not expand to exactly one baseline")

        advisory_root = root / "advisory-root"
        advisory_base = write_baseline(advisory_root / "fake-gate" / "r9-pre")
        (advisory_base / "run.log").write_text("FINDING F-01: planted\n", encoding="utf-8")
        advisory_spec = json.loads((advisory_base / "expected.json").read_text(encoding="utf-8"))
        advisory_spec["stdout_sha256"] = "0" * 64
        (advisory_base / "expected.json").write_text(
            json.dumps(advisory_spec, indent=1), encoding="utf-8")
        report = rollup("CTRL-BASELINE-STDOUT-ADVISORY", inspect(advisory_root), 0, "pinned",
                        set(), "a wrong advisory stdout pin is reported, never fatal (§4)")
        if report["baselines"][0]["stdout_pin"]["reading"] != "mismatch":
            failures.append("CTRL-BASELINE-STDOUT-ADVISORY did not record the mismatch")

        covered_root = root / "covered-root"
        write_baseline(covered_root / "fake-gate" / "r9-pre")
        rollup("CTRL-BASELINE-UNCOVERED-GATE",
               inspect(covered_root, gate_names=("fake-gate.py", "other-gate.py")), 2,
               "pinned", {"BASELINE-GATE-UNCOVERED"},
               "a gate with no committed baseline is never a silent pass")

        empty_root = root / "empty-root"
        empty_root.mkdir()
        rollup("CTRL-BASELINE-NONE-FOUND", inspect(empty_root), 2, "-",
               {"BASELINE-NONE-FOUND"}, "an existing root with no expected.json is not a pass")

        rollup("CTRL-BASELINE-ROOT-MISSING", inspect(root / "no-such-root"), 2, "-",
               {"BASELINE-ROOT-MISSING"}, "an absent baseline root is could-not-evaluate")

        if (combined_exit(0, 0), combined_exit(1, 0), combined_exit(0, 2),
                combined_exit(1, 2)) != (0, 1, 2, 2):
            failures.append("CTRL-COMBINED-EXIT: combined_exit mapping is not 2 > 1 > 0")
        controls.append({"id": "CTRL-COMBINED-EXIT", "observed_exit": combined_exit(1, 2),
                         "outcome": "-", "findings": []})

    changed, added, deleted = diff_snapshots(
        {"a.yml": "1", "b.yml": "2", "sub/c.yml": "3"},
        {"a.yml": "1x", "sub/c.yml": "3", "d.yml": "4"},
    )
    if (changed, added, deleted) != (["a.yml"], ["d.yml"], ["b.yml"]):
        failures.append(
            "CTRL-TREE-DIFF: diff_snapshots gave %r/%r/%r" % (changed, added, deleted)
        )
    controls.append({"id": "CTRL-TREE-DIFF", "observed_exit": 0 if not failures else 1, "findings": [], "outcome": "-"})

    every_id_stable = all(
        STABLE_ID_RE.match(f["id"]) for c in controls for f in c["findings"]
    ) and all(STABLE_ID_RE.match(c["id"]) for c in controls)
    if not every_id_stable:
        failures.append("CTRL-STABLE-IDS: an emitted control or finding id is not a stable token")
    controls.append(
        {"id": "CTRL-STABLE-IDS", "observed_exit": 0 if every_id_stable else 1, "findings": [], "outcome": "-"}
    )

    for c in controls:
        ids = ",".join(sorted({f["id"] for f in c.get("findings", [])})) or "-"
        print(f"control {c['id']}: exit={c['observed_exit']} outcome={c.get('outcome', '-')} ids={ids}")
    if failures:
        for x in failures:
            print(f"SELFTEST FAIL {x}")
        return 1
    print(f"SELFTEST OK {len(controls)}/{len(controls)} controls behaved as expected")
    return 0


def main(argv):
    parser = argparse.ArgumentParser(
        description="Isolated battery for the seven gate selftests plus the committed baseline check"
    )
    parser.add_argument(
        "--timeout",
        type=positive_float,
        default=DEFAULT_TIMEOUT,
        help="per-gate seconds; positive finite (default 120)",
    )
    parser.add_argument("--keep-mirror", action="store_true", help="keep the disposable mirror for inspection")
    parser.add_argument("--selftest", action="store_true", help="run isolated controls instead of the battery")
    parser.add_argument(
        "--baselines-root",
        action="append",
        default=None,
        metavar="PATH",
        help="baseline root to check instead of the committed roots (repeatable); "
             "for tamper drills on a copied tree",
    )
    args = parser.parse_args(argv[1:])

    if args.selftest:
        return run_selftest()
    roots = tuple(Path(value) for value in args.baselines_root) if args.baselines_root else BASELINE_ROOTS
    report, code = run_battery(args.timeout, args.keep_mirror, roots)
    print(json.dumps(report, indent=2, sort_keys=True))
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
