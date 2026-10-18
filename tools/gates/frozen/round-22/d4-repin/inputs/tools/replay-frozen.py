#!/usr/bin/env python3
"""Replay a frozen gate manifest without ever executing its recorded commands.

Usage:
    python3 tools/replay-frozen.py <MANIFEST.tsv> [--repo-root DIR] [--json]
    python3 tools/replay-frozen.py --selftest

The manifest is the column schema of tools/gates/frozen/round-3/MANIFEST.tsv:

    gate  gate_sha256  input  input_sha256  exit_code  finding_count
    output  output_sha256  input_snapshot  command

For every row this tool:

  1. refuses unsafe paths before any normalization — absolute, `~`, any `..`
     component (even internal, e.g. `tools/gates/../gates/x.py`), flag-like
     components (`--selftest`, `./--selftest`, `-`, which a gate's own CLI could
     read as an option or as stdin), symlinks, and anything resolving outside
     the repo — and requires the gate to be a Python file directly under
     `tools/gates`;
  2. verifies gate_sha256, the input_snapshot's input_sha256 and the recorded
     output's output_sha256 *before* any gate runs;
  3. copies the pinned snapshot into an isolated temporary mirror at the row's
     own `input` relative path and runs
         [python3, <pinned gate>, <input>]        (cwd = mirror)
     so no string from the `command` column is ever parsed or executed, and the
     path text a gate echoes matches the recording;
  4. compares observed exit code, finding count (`^FINDING ` lines) and output
     bytes against the record.

Exit codes:
    0  every row reproduced its recorded verdict. This asserts reproduction
       only: a reproduced `exit_code=1` row is still a red verdict, and this
       tool never reads a design as clean.
    1  replay mismatch: the pins verified and the gate ran, but the observed
       exit code, finding count or output bytes disagree with the record.
    2  could-not-evaluate: a pinned value failed verification before any
       comparison was possible (`gate_digest_mismatch`, `snapshot_tampered`,
       `expected_output_tampered`, `record_inconsistent`, ...), a path is
       unsafe, or the manifest/row is malformed. Argparse usage errors exit 2
       as well. This tool's own `--selftest` failure exits 1.

Exit 2 has precedence over exit 1: a row that could not be evaluated leaves the
replay incomplete whatever the other rows showed. Nothing is written inside the
repository; the scratch mirror is a self-cleaning temp directory.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

COLUMNS = (
    "gate", "gate_sha256", "input", "input_sha256", "exit_code",
    "finding_count", "output", "output_sha256", "input_snapshot", "command",
)
GATE_PARTS = ("tools", "gates")
FINDING_PREFIX = "FINDING "
HEX_DIGITS = frozenset("0123456789abcdef")


class RowError(Exception):
    """A reason a row could not be evaluated, carrying a stable machine id."""

    def __init__(self, reason, detail):
        super().__init__(detail)
        self.reason = reason
        self.detail = detail


def sha256_bytes(payload):
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def count_findings(payload):
    text = payload.decode("utf-8", "replace")
    return sum(1 for line in text.splitlines() if line.startswith(FINDING_PREFIX))


def check_digest(value, field):
    if len(value) != 64 or any(char not in HEX_DIGITS for char in value):
        raise RowError("record_malformed", f"{field}: not a sha256 hex digest: {value!r}")


def repo_path(root, raw, what):
    """Resolve a manifest path inside the repo, refusing traversal and symlinks.

    Every refusal runs on the raw spelling, before normalization: an internal
    `..` component or a flag-like component would otherwise normalize into a
    legal-looking path (or be handed to a gate's own option parser), so nothing
    hostile is ever normalized into acceptance.
    """
    if not raw:
        raise RowError(f"{what}_missing", f"{what}: path is empty")
    if os.path.isabs(raw) or raw.startswith("~"):
        raise RowError(f"{what}_unsafe_path", f"{what}: absolute path refused: {raw!r}")
    segments = [segment for segment in raw.split("/") if segment not in ("", ".")]
    if not segments:
        raise RowError(f"{what}_unsafe_path", f"{what}: empty after normalization: {raw!r}")
    if ".." in segments:
        raise RowError(f"{what}_unsafe_path", f"{what}: '..' component refused: {raw!r}")
    if any(segment.startswith("-") for segment in segments):
        raise RowError(
            f"{what}_unsafe_path",
            f"{what}: flag-like component refused (options and stdin are not paths): {raw!r}")
    normalized = os.path.normpath(raw)
    target = root
    for segment in Path(normalized).parts:
        target = target / segment
        if target.is_symlink():
            raise RowError(f"{what}_unsafe_path", f"{what}: symlink refused: {raw!r}")
    real = Path(os.path.realpath(target))
    if real != root and root not in real.parents:
        raise RowError(f"{what}_unsafe_path", f"{what}: resolves outside the repo: {raw!r}")
    return target, normalized


def gate_path(root, raw):
    target, normalized = repo_path(root, raw, "gate")
    if tuple(Path(normalized).parts[:-1]) != GATE_PARTS or not normalized.endswith(".py"):
        raise RowError(
            "gate_not_whitelisted",
            f"gate: only *.py files directly under tools/gates are replayable: {raw!r}")
    if not target.is_file():
        raise RowError("gate_missing", f"gate: not a file: {raw!r}")
    return target


def read_manifest(path):
    try:
        text = Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise RowError("manifest_unreadable", f"manifest: {exc}") from exc
    lines = text.splitlines()
    if not lines:
        raise RowError("manifest_malformed", "manifest: no header row")
    header = lines[0].split("\t")
    if len(header) != len(COLUMNS) or sorted(header) != sorted(COLUMNS):
        raise RowError(
            "manifest_malformed",
            f"manifest: header must carry the documented columns {list(COLUMNS)}: got {header}")
    index = {name: position for position, name in enumerate(header)}
    rows = []
    for number, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        fields = line.split("\t")
        if len(fields) != len(header):
            raise RowError(
                "record_malformed",
                f"line {number}: {len(fields)} fields, expected {len(header)}")
        rows.append((number, {name: fields[index[name]] for name in COLUMNS}))
    if not rows:
        raise RowError("manifest_malformed", "manifest: no data rows")
    return rows


def run_in_mirror(root, gate, input_rel, snapshot, input_sha256, timeout):
    """Run the pinned gate over a private copy of the pinned snapshot."""
    mirror = Path(tempfile.mkdtemp(prefix="replay-frozen-"))
    try:
        real_mirror = Path(os.path.realpath(mirror))
        if real_mirror == root or root in real_mirror.parents:
            raise RowError("mirror_unsafe", f"mirror: temporary root is inside the repo: {real_mirror}")
        destination = mirror / input_rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(snapshot, destination)
        if sha256_file(destination) != input_sha256:
            raise RowError("mirror_unsafe", "mirror: copied snapshot drifted from the pinned digest")
        environment = dict(os.environ)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        try:
            return subprocess.run(
                [sys.executable, str(gate), input_rel],
                cwd=mirror, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, timeout=timeout, env=environment,
            )
        except subprocess.TimeoutExpired as exc:
            raise RowError("gate_timeout", f"gate: exceeded {timeout:g}s") from exc
        except OSError as exc:
            raise RowError("gate_launch_failed", f"gate: could not start: {exc}") from exc
    finally:
        shutil.rmtree(mirror, ignore_errors=True)


def replay_row(root, row, line_number, timeout):
    result = {
        "line": line_number,
        "gate": row["gate"],
        "input": row["input"],
        "snapshot": row["input_snapshot"],
        "recorded_gate_sha256": row["gate_sha256"],
        "recorded_input_sha256": row["input_sha256"],
        "recorded_output_sha256": row["output_sha256"],
        "recorded_exit": None,
        "recorded_finding_count": None,
        "observed_exit": None,
        "observed_finding_count": None,
        "observed_output_sha256": None,
        "gate_launched": False,
        "stderr_excerpt": "",
        "recorded_command_ignored": row["command"],
        "status": None,
        "reason": None,
        "detail": None,
    }
    try:
        gate = gate_path(root, row["gate"])
        snapshot, _ = repo_path(root, row["input_snapshot"], "snapshot")
        if not snapshot.is_file():
            raise RowError("snapshot_missing", f"snapshot: not a file: {row['input_snapshot']!r}")
        output, _ = repo_path(root, row["output"], "output")
        if not output.is_file():
            raise RowError("output_missing", f"output: not a file: {row['output']!r}")
        repo_path(root, row["input"], "input")  # the live path is validated, never opened

        check_digest(row["gate_sha256"], "gate_sha256")
        if sha256_file(gate) != row["gate_sha256"]:
            raise RowError(
                "gate_digest_mismatch",
                f"gate: on-disk bytes are not the pinned revision: {row['gate']}")
        check_digest(row["input_sha256"], "input_sha256")
        if sha256_file(snapshot) != row["input_sha256"]:
            raise RowError(
                "snapshot_tampered",
                f"snapshot: bytes differ from the pinned input_sha256: {row['input_snapshot']}")
        check_digest(row["output_sha256"], "output_sha256")
        expected_bytes = output.read_bytes()
        if sha256_bytes(expected_bytes) != row["output_sha256"]:
            raise RowError(
                "expected_output_tampered",
                f"output: recorded bytes differ from the pinned output_sha256: {row['output']}")
        try:
            expected_exit = int(row["exit_code"])
            expected_count = int(row["finding_count"])
        except ValueError as exc:
            raise RowError("record_malformed", f"exit_code/finding_count: {exc}") from exc
        result["recorded_exit"] = expected_exit
        result["recorded_finding_count"] = expected_count
        recorded_count = count_findings(expected_bytes)
        if recorded_count != expected_count:
            raise RowError(
                "record_inconsistent",
                f"finding_count {expected_count} disagrees with {recorded_count} "
                f"'{FINDING_PREFIX.rstrip()}' line(s) in the recorded output")

        observed = run_in_mirror(root, gate, row["input"], snapshot, row["input_sha256"], timeout)
    except RowError as exc:
        result["status"] = "could-not-evaluate"
        result["reason"] = exc.reason
        result["detail"] = exc.detail
        return result

    result["gate_launched"] = True
    result["observed_exit"] = observed.returncode
    result["observed_finding_count"] = count_findings(observed.stdout)
    result["observed_output_sha256"] = sha256_bytes(observed.stdout)
    if observed.stderr:
        result["stderr_excerpt"] = observed.stderr.decode("utf-8", "replace")[:400]

    disagreements = []
    if observed.returncode != expected_exit:
        disagreements.append(f"exit code {observed.returncode} != recorded {expected_exit}")
    if result["observed_finding_count"] != expected_count:
        disagreements.append(
            f"finding count {result['observed_finding_count']} != recorded {expected_count}")
    if observed.stdout != expected_bytes:
        disagreements.append("output bytes differ from the recorded output")
    if disagreements:
        result["status"] = "mismatch"
        result["reason"] = "replay_mismatch"
        result["detail"] = "; ".join(disagreements)
    else:
        result["status"] = "reproduced"
    return result


def render(results, manifest, root):
    lines = []
    for result in results:
        if result["observed_output_sha256"] is None:
            verdict = "skipped"
        elif result["observed_output_sha256"] == result["recorded_output_sha256"]:
            verdict = "match"
        else:
            verdict = "differ"
        lines.append(
            "ROW %d %s reason=%s gate=%s input=%s exit=%s/%s count=%s/%s bytes=%s launched=%s"
            % (result["line"], result["status"], result["reason"] or "-", result["gate"],
               result["input"], result["observed_exit"], result["recorded_exit"],
               result["observed_finding_count"], result["recorded_finding_count"],
               verdict, "yes" if result["gate_launched"] else "no"))
        if result["status"] != "reproduced":
            lines.append("  detail: %s" % result["detail"])
    reproduced = sum(1 for r in results if r["status"] == "reproduced")
    mismatch = sum(1 for r in results if r["status"] == "mismatch")
    unevaluated = sum(1 for r in results if r["status"] == "could-not-evaluate")
    if unevaluated:
        lines.append(
            "REPLAY COULD-NOT-EVALUATE: %d could-not-evaluate, %d mismatch, %d reproduced "
            "of %d row(s) in %s" % (unevaluated, mismatch, reproduced, len(results), manifest))
    elif mismatch:
        lines.append(
            "REPLAY MISMATCH: %d mismatch, %d reproduced of %d row(s) in %s"
            % (mismatch, reproduced, len(results), manifest))
    else:
        lines.append(
            "REPLAY OK: %d/%d rows reproduced the recorded verdicts (reproduction only: "
            "a reproduced red verdict stays red)" % (reproduced, len(results)))
    return lines


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="replay-frozen.py", description=__doc__.split("\n\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("manifest", nargs="?", help="frozen MANIFEST.tsv to replay")
    parser.add_argument("--repo-root", default=None,
                        help="repository root (default: this tool's own repository)")
    parser.add_argument("--timeout", type=float, default=120.0,
                        help="per-gate wall-clock limit in seconds (default: 120)")
    parser.add_argument("--json", action="store_true", help="emit one JSON document")
    parser.add_argument("--selftest", action="store_true",
                        help="run the isolated fixture controls and exit")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.manifest:
        parser.error("give a MANIFEST.tsv path or --selftest")
    root = Path(os.path.realpath(args.repo_root or Path(__file__).resolve().parent.parent))

    try:
        rows = read_manifest(args.manifest)
    except RowError as exc:
        print(f"COULD-NOT-EVALUATE {exc.reason}: {exc.detail}", file=sys.stderr)
        if args.json:
            print(json.dumps({"manifest": str(args.manifest), "repo_root": str(root),
                              "rows": [], "summary": {"reproduced": 0, "mismatch": 0,
                                                      "could_not_evaluate": 0, "exit": 2,
                                                      "reason": exc.reason,
                                                      "detail": exc.detail}}, indent=2))
        return 2

    results = [replay_row(root, row, number, args.timeout) for number, row in rows]
    reproduced = sum(1 for r in results if r["status"] == "reproduced")
    mismatch = sum(1 for r in results if r["status"] == "mismatch")
    unevaluated = sum(1 for r in results if r["status"] == "could-not-evaluate")
    exit_code = 2 if unevaluated else (1 if mismatch else 0)
    if args.json:
        print(json.dumps({
            "manifest": str(args.manifest), "repo_root": str(root),
            "tool": "tools/replay-frozen.py",
            "rows": results,
            "summary": {"rows": len(results), "reproduced": reproduced, "mismatch": mismatch,
                        "could_not_evaluate": unevaluated, "exit": exit_code},
        }, indent=2))
    else:
        for line in render(results, args.manifest, root):
            print(line)
    return exit_code


# --------------------------------------------------------------------------
# Selftest: isolated fixtures, positive and negative controls
# --------------------------------------------------------------------------

FAKE_GATE = '''#!/usr/bin/env python3
"""Fixture gate written by tools/replay-frozen.py --selftest; not a real gate."""
import hashlib
import pathlib
import sys

pathlib.Path({marker!r}).write_text({label!r}, encoding="utf-8")
if len(sys.argv) == 2 and sys.argv[1] in ("--selftest", "--self-test", "-"):
    pathlib.Path({regenerate!r}).write_text("fixture tree regenerated by the gate",
                                           encoding="utf-8")
    print("selftest: fixture regenerated")
    sys.exit(0)
if len(sys.argv) != 2:
    sys.exit(2)
payload = pathlib.Path(sys.argv[1]).read_bytes()
{read_line}
{extra}
sys.exit({code})
'''

FAKE_GATE_READ_LINE = (
    'print("FINDING SELFTEST-A: fixture \\u2014 read %d bytes (sha256 %s)"\n'
    '      % (len(payload), hashlib.sha256(payload).hexdigest()))')
FAKE_GATE_EXTRA_LINE = 'print("FINDING SELFTEST-B: fixture \\u2014 second planted finding")'


def fixture_case(scratch_root, name, *, findings=1, gate_exit=1):
    """Build one isolated fixture repository and record a gate run in it.

    The generated gate carries a stand-in for the real gates' own `--selftest`
    branch (which regenerates fixtures in this repository): it is disabled by
    construction unless a manifest hands it a flag-like or `-` argument, which
    is exactly what the input-safety cases must never do.
    """
    root = scratch_root / name
    gate_dir = root / "tools" / "gates"
    gate_dir.mkdir(parents=True)
    marker = root / "gate-launched.txt"
    regenerate = root / "gate-selftest-ran.txt"
    gate = gate_dir / "fake-gate.py"
    extra = FAKE_GATE_EXTRA_LINE if findings > 1 else 'print("no second finding")'
    read_line = FAKE_GATE_READ_LINE if findings > 0 else 'pass'
    gate.write_text(
        FAKE_GATE.format(marker=str(marker), regenerate=str(regenerate), label=name,
                         code=gate_exit, read_line=read_line, extra=extra),
        encoding="utf-8")
    input_rel = "examples/fixture-input.yml"
    snapshot_rel = "tools/gates/frozen/%s/inputs/%s" % (name, input_rel)
    snapshot = root / snapshot_rel
    snapshot.parent.mkdir(parents=True)
    snapshot.write_bytes(("# fixture input for replay-frozen.py --selftest (%s)\n"
                          "name: fixture-%s\n" % (name, name)).encode("utf-8"))
    recorded = subprocess.run([sys.executable, str(gate), str(snapshot)], cwd=root,
                              stdin=subprocess.DEVNULL, capture_output=True, timeout=60)
    if marker.exists():
        marker.unlink()  # the recording run is this fixture's own, not the replay's
    output_rel = "tools/gates/frozen/%s/recorded.out" % name
    output = root / output_rel
    output.write_bytes(recorded.stdout)
    case = {
        "name": name,
        "root": root,
        "marker": marker,
        "regenerate": regenerate,
        "manifest": root / "tools" / "gates" / "frozen" / name / "MANIFEST.tsv",
        "gate": gate,
        "gate_rel": "tools/gates/fake-gate.py",
        "snapshot": snapshot,
        "snapshot_rel": snapshot_rel,
        "output": output,
        "output_rel": output_rel,
        "input_rel": input_rel,
        "recorded_exit": recorded.returncode,
        "recorded_count": count_findings(recorded.stdout),
    }
    return case


def case_manifest(case, *, gate_sha=None, gate_rel=None, input_rel=None, input_sha=None,
                  snapshot_rel=None, output_sha=None, output_rel=None,
                  exit_code=None, finding_count=None, command=None, mutate=None):
    """Write the case manifest, then optionally tamper with a pinned file."""
    gate_rel = gate_rel if gate_rel is not None else case["gate_rel"]
    snapshot_rel = snapshot_rel if snapshot_rel is not None else case["snapshot_rel"]
    output_rel = output_rel if output_rel is not None else case["output_rel"]
    input_token = case["input_rel"] if input_rel is None else input_rel
    row = {
        "gate": gate_rel,
        "gate_sha256": gate_sha or sha256_file(case["gate"]),
        "input": input_token,
        "input_sha256": input_sha or sha256_file(case["snapshot"]),
        "exit_code": str(case["recorded_exit"] if exit_code is None else exit_code),
        "finding_count": str(case["recorded_count"] if finding_count is None else finding_count),
        "output": output_rel,
        "output_sha256": output_sha or sha256_file(case["output"]),
        "input_snapshot": snapshot_rel,
        "command": command or ("python3 %s %s" % (gate_rel, input_token)),
    }
    case["manifest"].write_text(
        "\t".join(COLUMNS) + "\n" + "\t".join(row[name] for name in COLUMNS) + "\n",
        encoding="utf-8")
    if mutate:
        mutate(case)
    return case


def tree_state(root, exclude):
    state = {}
    for path in sorted(root.rglob("*")):
        if path.is_file() and path != exclude:
            state[str(path.relative_to(root))] = sha256_file(path)
    return state


def selftest():
    checks = []

    def check(name, ok, detail=""):
        checks.append((name, bool(ok), detail))

    def run_tool(case):
        return subprocess.run(
            [sys.executable, str(Path(__file__).resolve()), str(case["manifest"]),
             "--repo-root", str(case["root"])],
            cwd=case["root"], stdin=subprocess.DEVNULL, capture_output=True,
            text=True, timeout=120)

    scratch_root = Path(tempfile.mkdtemp(prefix="replay-frozen-selftest-"))
    try:
        def scenario(name, expected_exit, expected_status, expected_reason, launched,
                     regenerate_absent=False):
            return {"name": name, "exit": expected_exit, "status": expected_status,
                    "reason": expected_reason, "launched": launched,
                    "regenerate_absent": regenerate_absent}

        cases = []

        # 1. clean green replay: the recorded verdict is green and reproduces.
        case = fixture_case(scratch_root, "clean-green", findings=0, gate_exit=0)
        cases.append((case_manifest(case, command="touch pwned-marker.txt"),
                      scenario("clean-green", 0, "reproduced", None, True)))

        # 2. expected-red replay: the recorded verdict is red; exit 0 means the
        #    red verdict reproduced, not that the design passed.
        case = fixture_case(scratch_root, "expected-red", findings=2, gate_exit=1)
        cases.append((case_manifest(case), scenario("expected-red", 0, "reproduced", None, True)))

        # 3. verdict mismatch in output bytes and finding count: the record is
        #    internally consistent (its own digest and count agree) but the gate
        #    no longer prints those bytes.
        case = fixture_case(scratch_root, "mismatch-bytes", findings=1, gate_exit=1)
        case["output"].write_bytes(case["output"].read_bytes()
                                   + b"FINDING SELFTEST-C: fixture \xe2\x80\x94 planted drift\n")
        cases.append((case_manifest(case, finding_count=2),
                      scenario("mismatch-bytes", 1, "mismatch", "replay_mismatch", True)))

        # 4. verdict mismatch in the exit code only.
        case = fixture_case(scratch_root, "mismatch-exit", findings=1, gate_exit=1)
        cases.append((case_manifest(case, exit_code=0),
                      scenario("mismatch-exit", 1, "mismatch", "replay_mismatch", True)))

        # 5. tampered snapshot: exit 2 snapshot_tampered, and the gate must not run.
        case = fixture_case(scratch_root, "snapshot-tampered", findings=1, gate_exit=1)
        cases.append((case_manifest(case, mutate=lambda c: c["snapshot"].write_bytes(
            c["snapshot"].read_bytes() + b"# tampered after the pin was recorded\n")),
            scenario("snapshot-tampered", 2, "could-not-evaluate", "snapshot_tampered", False)))

        # 6. gate bytes are not the pinned revision.
        case = fixture_case(scratch_root, "gate-digest-mismatch", findings=1, gate_exit=1)
        cases.append((case_manifest(case, gate_sha=sha256_bytes(b"#!/usr/bin/env python3\n")),
                      scenario("gate-digest-mismatch", 2, "could-not-evaluate",
                               "gate_digest_mismatch", False)))

        # 7. recorded output edited after the pin was recorded.
        case = fixture_case(scratch_root, "output-tampered", findings=1, gate_exit=1)
        cases.append((case_manifest(case, mutate=lambda c: c["output"].write_bytes(
            c["output"].read_bytes() + b"FINDING SELFTEST-D: fixture \xe2\x80\x94 edited record\n")),
            scenario("output-tampered", 2, "could-not-evaluate",
                     "expected_output_tampered", False)))

        # 8. self-contradicting record: the count does not match its own output.
        case = fixture_case(scratch_root, "record-inconsistent", findings=1, gate_exit=1)
        cases.append((case_manifest(case, finding_count=7),
                      scenario("record-inconsistent", 2, "could-not-evaluate",
                               "record_inconsistent", False)))

        # 9. traversal gate path.
        case = fixture_case(scratch_root, "traversal-gate", findings=1, gate_exit=1)
        cases.append((case_manifest(case, gate_rel="../tools/gates/fake-gate.py"),
                      scenario("traversal-gate", 2, "could-not-evaluate",
                               "gate_unsafe_path", False)))

        # 10. symlinked gate file.
        case = fixture_case(scratch_root, "symlink-gate", findings=1, gate_exit=1)
        link = case["gate"].parent / "link-gate.py"
        link.symlink_to(case["gate"])
        cases.append((case_manifest(case, gate_rel="tools/gates/link-gate.py"),
                      scenario("symlink-gate", 2, "could-not-evaluate",
                               "gate_unsafe_path", False)))

        # 11. gate outside the whitelist directory.
        case = fixture_case(scratch_root, "gate-not-whitelisted", findings=1, gate_exit=1)
        outside = case["root"] / "tools" / "fake-gate.py"
        outside.write_bytes(case["gate"].read_bytes())
        cases.append((case_manifest(case, gate_rel="tools/fake-gate.py"),
                      scenario("gate-not-whitelisted", 2, "could-not-evaluate",
                               "gate_not_whitelisted", False)))

        # 12. absolute snapshot path.
        case = fixture_case(scratch_root, "absolute-snapshot", findings=1, gate_exit=1)
        cases.append((case_manifest(case, snapshot_rel="/nowhere/absolute-snapshot.yml"),
                      scenario("absolute-snapshot", 2, "could-not-evaluate",
                               "snapshot_unsafe_path", False)))

        # 13. internal '..' in the gate path: it normalizes to a legal gate, so
        #     the refusal must happen on the raw spelling, before normalization.
        case = fixture_case(scratch_root, "traversal-internal-gate", findings=1, gate_exit=1)
        cases.append((case_manifest(case, gate_rel="tools/gates/../gates/fake-gate.py"),
                      scenario("traversal-internal-gate", 2, "could-not-evaluate",
                               "gate_unsafe_path", False)))

        # 14. internal '..' in the snapshot path, likewise normalizing to the
        #     real snapshot.
        case = fixture_case(scratch_root, "traversal-internal-snapshot", findings=1, gate_exit=1)
        cases.append((case_manifest(case, snapshot_rel="tools/gates/frozen/%s/inputs/../inputs/%s"
                                    % (case["name"], case["input_rel"])),
                      scenario("traversal-internal-snapshot", 2, "could-not-evaluate",
                               "snapshot_unsafe_path", False)))

        # 15. internal '..' in the input argument.
        case = fixture_case(scratch_root, "traversal-internal-input", findings=1, gate_exit=1)
        cases.append((case_manifest(case, input_rel="examples/../examples/fixture-input.yml"),
                      scenario("traversal-internal-input", 2, "could-not-evaluate",
                               "input_unsafe_path", False)))

        # 16-18. flag-like and stdin spellings as the gate argument: the real
        #     gates' own `--selftest` branches rewrite fixtures in this repo, and
        #     `-` means stdin. The manifest's `command` column claims exactly the
        #     dangerous invocation; neither it nor the argv token may reach the
        #     gate, which the guard marker proves.
        for flag_name, flag_token in (("flag-input-selftest", "--selftest"),
                                      ("flag-input-dot-selftest", "./--selftest"),
                                      ("flag-input-stdin", "-")):
            case = fixture_case(scratch_root, flag_name, findings=1, gate_exit=1)
            cases.append((case_manifest(case, input_rel=flag_token),
                          scenario(flag_name, 2, "could-not-evaluate",
                                   "input_unsafe_path", False, regenerate_absent=True)))

        for case, expectation in cases:
            name = expectation["name"]
            before = tree_state(case["root"], case["marker"])
            completed = run_tool(case)
            after = tree_state(case["root"], case["marker"])
            output = completed.stdout + completed.stderr
            check(f"{name}: exit {expectation['exit']}", completed.returncode == expectation["exit"],
                  f"got {completed.returncode}: {output.strip()[:200]}")
            check(f"{name}: status={expectation['status']}"
                  + (f" reason={expectation['reason']}" if expectation["reason"] else ""),
                  expectation["status"] in output
                  and (expectation["reason"] is None or expectation["reason"] in output),
                  output.strip()[:200])
            launched = case["marker"].exists()
            check(f"{name}: gate {'launched' if expectation['launched'] else 'not launched'}",
                  launched == expectation["launched"],
                  f"marker {'present' if launched else 'absent'}")
            check(f"{name}: fixture tree unchanged", before == after,
                  "the replay wrote inside the fixture repository")
            if name == "clean-green":
                check("clean-green: recorded command string never executed",
                      not (case["root"] / "pwned-marker.txt").exists(),
                      "the manifest `command` column ran")
            if expectation["regenerate_absent"]:
                check(f"{name}: gate's own selftest never triggered",
                      not case["regenerate"].exists(),
                      "a flag-like argument reached the gate and could rewrite fixtures")

        # 13. malformed manifest header.
        case = fixture_case(scratch_root, "bad-header", findings=1, gate_exit=1)
        case_manifest(case)
        case["manifest"].write_text("gate\tinput\nx\ty\n", encoding="utf-8")
        completed = run_tool(case)
        output = completed.stdout + completed.stderr
        check("bad-header: exit 2", completed.returncode == 2, f"got {completed.returncode}")
        check("bad-header: reason=manifest_malformed", "manifest_malformed" in output,
              output.strip()[:200])
        check("bad-header: gate not launched", not case["marker"].exists(), "marker present")
    finally:
        shutil.rmtree(scratch_root, ignore_errors=True)

    for name, ok, detail in checks:
        print("%s %s%s" % ("PASS" if ok else "FAIL", name, "" if ok else ": " + detail))
    failures = sum(1 for _, ok, _ in checks if not ok)
    print("selftest: %d/%d checks passed" % (len(checks) - failures, len(checks)))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
