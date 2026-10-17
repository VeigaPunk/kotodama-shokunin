#!/usr/bin/env python3
"""Isolated battery for the seven legacy gate selftests.

Stdlib only. Copies the seven tools/gates/*.py scripts and their fixture tree
into a disposable mirror directory, runs each ``--selftest`` there, and never
invokes a gate on a live path. Before and after the run it snapshots the live
tree (per-file sha256 AND the path set of the seven scripts + fixture tree), so
"originals preserved" is measured, not assumed: modified bytes, added files and
deleted files under the live gates tree are all detected. Note what this
proves: matching hashes prove byte preservation, not absence of writes — a
rewrite with identical bytes passes; a new file or a deletion does not.

Exit codes:
  0  all seven gate selftests passed (exit 0) and the original tree preserved
  1  at least one gate selftest ran, exited 1, AND printed recognizable stable
     failure evidence (see below) — treated as a genuine test failure
  2  could-not-evaluate: gate file missing, copy mismatch, live tree changed,
     launch error, timeout, abnormal exit, or a child that exited 1 without
     recognizable stable failure evidence (conservatively read as a crash)

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
[sys.executable, <resolved gate path>, "--selftest"] with shell=False.

Usage:
  python3 tools/check-gate-battery.py [--timeout S] [--keep-mirror]
  python3 tools/check-gate-battery.py --selftest

``--timeout`` must be a positive finite number of seconds; zero, negative,
non-numeric or non-finite values are rejected as usage errors (exit 2).
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


def run_battery(timeout, keep_mirror):
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
            "summary": {"battery_exit": 2, "pass": 0, "fail": 0, "unevaluable": len(problems)},
            "mirror": {"root": None, "removed": None},
        }, 2

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
    code = battery_exit(outcomes, findings)
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
    parser = argparse.ArgumentParser(description="Isolated battery for the seven gate selftests")
    parser.add_argument(
        "--timeout",
        type=positive_float,
        default=DEFAULT_TIMEOUT,
        help="per-gate seconds; positive finite (default 120)",
    )
    parser.add_argument("--keep-mirror", action="store_true", help="keep the disposable mirror for inspection")
    parser.add_argument("--selftest", action="store_true", help="run isolated controls instead of the battery")
    args = parser.parse_args(argv[1:])

    if args.selftest:
        return run_selftest()
    report, code = run_battery(args.timeout, args.keep_mirror)
    print(json.dumps(report, indent=2, sort_keys=True))
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
