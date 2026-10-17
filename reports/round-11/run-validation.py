#!/usr/bin/env python3
"""Round-11 acceptance runner — claims D / O / F (kotodama-shokunin).

X03 deliverable: one runner that grades the round-11 evidence over the three
declared claims and exits 0 only when all three pass. It writes exactly one
file — ``reports/round-11/validation.json`` — and never edits the evidence it
reads (no commits, no report rewrites, no corpus writes, no re-pin).

Claim contracts, as declared in ``reports/round-11/claims.json``:

D (depth)      the round-8 typed-label projection is wired into the D2 flow:
               the end-to-end command over examples/culture-d2 exits 0 with
               findings exactly equal to the expected hold set; translated
               labels never enter the sound channel (no PHON-INVENTORY
               artifact names a translated GAR label); owed native forms are
               carried as named holds; the frozen replay is re-pinned and
               green; d2/d3 selftests and the gate battery remain green; the
               committed D2 packet still regenerates byte-identically.
O (operability) a runnable exercise (``tools/exercise-handoff-e2e.py``, or a
               documented equivalent) assembles a handoff packet from live
               D2/D3 artifacts, validates it through
               ``tools/gates/handoff-packet-check.py`` in an isolated copy,
               and exits 0 with 16/16 envelope fields, 20/20 glossary entries
               and a clean gate verdict; a frozen expected.json baseline is
               committed; the exercise selftest carries positive + malformed
               controls.
F (freshness)  recheck receipts under ``reports/round-11/recheck/`` re-run
               >=15 round-10 ledger commands 1:1 with hash comparison; >=95%
               hash-stable; every drifted row dispositioned with a named
               cause (legitimate change / environmental / defect); an
               independent auditor re-runs >=5 commands with zero unexplained
               mismatches; a summary JSON matches the receipts.

Accepted evidence shapes (fail-closed: an absent artifact is a failure, not a
skip; the runner prefers the machine-readable shape and says which leg it
measured):

D e2e — either
  (a) a JSON receipt anywhere under ``reports/round-11/`` (``reports/
      round-11/recheck/`` excluded) carrying a ``command`` (string or argv
      list), an expected-hold list under one of ``expected``,
      ``expected_holds``, ``expected_hold_set``, ``expected_findings`` and an
      observed list under one of ``findings``, ``observed``,
      ``observed_findings``, ``observed_holds`` (plus optional
      ``exit``/``exit_code``, ``output_sha256``/``stdout_sha256``,
      ``owed_forms``/``owed_native_forms`` and a translated-on-sound-channel
      counter). The runner re-runs the recorded command itself (repo root,
      TMPDIR under .scratch), requires exit 0, set-equality between expected
      and the fresh run's findings (or the receipt's observed list when the
      output is not machine-readable), every expected hold's id and where
      token present in the fresh stdout, and no PHON-INVENTORY line naming a
      translated GAR label. Receipts whose path/payload mark them as
      negative drills (``neg``/``control``/``malformed``) are recorded but
      never chosen as the clean primary;
  (b) a documented live flow: a ``tools/*.py`` whose source names both the
      typed projection and ``gates/`` and whose ``--help`` offers one of
      ``--e2e``/``--flow``/``--typed-flow``/``--wired-flow``; or a bare
      ``python3`` command for an existing repo script appearing on an
      ``e2e``/``end-to-end`` line of ``reports/round-11/depth/*.md`` that
      names ``examples/culture-d2`` and ``exit 0`` (metacharacter-free). The
      expected hold set may then come from a JSON block in ``reports/
      round-11/depth/design.md`` (``expected_holds``-style key) or from the
      command's own JSON output; if no expected set is found the equality leg
      fails with instructions.

O — the exercise tool is ``tools/exercise-handoff-e2e.py`` when present, else
    a ``tools/*.py`` naming ``handoff-packet-check`` and ``expected.json``
    with e2e/exercise wording and a glossary/envelope or temp-dir marker. The
    runner runs ``--selftest`` (exit 0, positive + malformed controls named)
    and the exercise itself (default mode, with ``--json``/``--check``
    retried only if the default is non-zero and ``--help`` offers them). It
    then requires, in the exercise's own output, 16/16 fields, 20/20 glossary
    entries, a clean gate verdict (``findings=0``/empty findings), and a
    reference to ``handoff-packet-check``. A frozen ``*expected*.json``
    baseline must exist in the exercise's tree or beside it (recorded;
    trackedness reported, not required — workers never commit).

F — receipts are ``reports/round-11/recheck/row-<NNN>.json`` (a consolidated
    ``*rows*.json`` with a row map is accepted as a fallback). Each receipt's
    index must address a round-10 ledger row, its ``command`` must be the
    ledger row's command text 1:1, and its ``prior_hash`` must equal that
    row's recorded ``output_sha256`` (the binding guard); ``stable`` must
    agree with ``new_hash == prior_hash``. Rows with a byte-comparable
    ``new_hash`` are the >=15 re-run 1:1 population and the >=95% stability
    denominator; rows with ``new_hash`` null (prose-only ledger text) are
    dispositioned as unreproducible-by-construction and must still carry a
    cause. Unstable rows need a cause (or ``drift_class``) naming a licensed
    class: legitimate change / environmental / defect. The auditor artifact
    is ``reports/round-11/recheck/audit.md`` (>=5 independent re-runs by
    ledger command text, zero positive mismatch readings) and the scribe
    artifact is ``reports/round-11/recheck/summary.json`` (counts must match
    the receipts, tolerating the measured / unreproducible split).

Usage::

    python3 reports/round-11/run-validation.py     # writes validation.json

Exit: 0 = all three claims pass; 1 = at least one fails (the receipt lists
every failure and the artifacts still missing).

The runner is author-side only: it admits nothing, certifies no canon, and
replaces no independent promotion review. It executes the round's own gates
and exercises (read-only modes: --check/--selftest/plain battery/replay); it
does not re-run the ledger commands itself — that is the recheck seats' and
the auditor's recorded work, cross-checked here against the ledger hashes.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SELF_REL = "reports/round-11/run-validation.py"
CLAIMS_REL = "reports/round-11/claims.json"
TARGETS_REL = "reports/round-11/targets.json"
OUTPUT_REL = "reports/round-11/validation.json"

DEPTH_DIR_REL = "reports/round-11/depth"
DEPTH_DESIGN_REL = "reports/round-11/depth/design.md"
RECHECK_DIR_REL = "reports/round-11/recheck"
RECHECK_AUDIT_REL = "reports/round-11/recheck/audit.md"
RECHECK_SUMMARY_REL = "reports/round-11/recheck/summary.json"
LEDGER_REL = "reports/round-10/drift/ledger.json"

D2_ASSEMBLER_REL = "tools/assemble-d2.py"
D2_TYPED_REL = "tools/d2-typed-labels.py"
D2_TYPED_PROJECTION_REL = "examples/culture-d2/typed-labels.d2.yml"
D3_ASSEMBLER_REL = "tools/assemble-culture-d3.py"
D3_COUPLING_REL = "tools/check-evidence-coupling.py"
D3_PACKET_REL = "examples/culture-d3/packet.json"
D3_EXPECTED_REL = "examples/culture-d3/expected.json"
BATTERY_REL = "tools/check-gate-battery.py"
REPLAY_REL = "tools/replay-frozen.py"
HANDOFF_CHECK_REL = "tools/gates/handoff-packet-check.py"
EXERCISE_REL = "tools/exercise-handoff-e2e.py"

D2_SELFTESTS = (
    (D2_ASSEMBLER_REL, ["--selftest"]),
    (D2_TYPED_REL, ["--selftest"]),
)
D3_SELFTESTS = (
    (D3_ASSEMBLER_REL, ["--selftest"]),
    (D3_COUPLING_REL, ["--selftest"]),
)

BATTERY_ROOT_CANDIDATES = (
    "tools/gates/frozen",
    "tools/gates/expected",
    "reports/round-9/baselines",
)

O_REQUIRED_FIELDS = 16
O_REQUIRED_GLOSSARY = 20

F_MIN_ROWS = 15
F_MIN_STABILITY = 0.95
F_MIN_AUDIT_RERUNS = 5

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
TRACEBACK_RE = re.compile(r"Traceback \(most recent call last\)")
CLASS_PATTERNS = (
    ("legitimate-change",
     re.compile(r"(?i)legit|intentional|re-?pin|commit|added|landed|land\b|"
                r"grew|admitted|new entry|repaired")),
    ("unreproducible",
     re.compile(r"(?i)non-?literal|prose|not[-_ ]?filed|not[-_ ]?reproduc|"
                r"reconstruct|unreproduc|byte[-_ ]?compar|not-applicable")),
    ("environmental",
     re.compile(r"(?i)environment|env\b|nondetermin|non-?determin|volatile|"
                r"flak|concurren|tempor|random|embed|wall-?clock|timestamp|"
                r"reproducib|absolute|mktemp|tmpdir|token|mirror|hash[-_ ]"
                r"method|stream|stale|drift")),
    ("defect",
     re.compile(r"(?i)defect|bug|regress|broken|fabricat")),
)

CMD_KEYS = ("command", "command_line", "cmd", "argv", "recheck_command")
EXIT_KEYS = ("exit", "exit_code", "observed_exit", "command_exit", "new_exit")
EXPECTED_KEYS = ("expected", "expected_holds", "expected_hold_set",
                 "expected_findings", "expected_hold_ids", "expect")
OBSERVED_KEYS = ("findings", "observed", "observed_findings", "observed_holds",
                 "observed_hold_set", "actual_findings", "holds")
OWED_KEYS = ("owed_forms", "owed_native_forms", "owed_native_form_ids",
             "owed")
SOUND_KEYS = ("translated_on_sound_channel", "translations_on_sound_channel",
              "sound_channel_translations", "phon_translated_count",
              "translated_label_phon_findings")
HASH_KEYS = ("output_sha256", "stdout_sha256", "merged_sha256",
             "fresh_stdout_sha256")

LEDGER_INDEX_KEYS = ("row", "idx", "index", "row_index", "ledger_index")
PRIOR_HASH_KEYS = ("prior_hash", "ledger_output_sha256", "prior_output_sha256")
NEW_HASH_KEYS = ("new_hash", "recheck_output_sha256", "observed_sha256",
                 "hash")
CAUSE_KEYS = ("drift_cause", "cause", "disposition", "cause_class",
              "classification", "drift_class", "unstable_reason", "reason")


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def sha256_file(relative: str):
    path = ROOT / relative
    if not path.is_file():
        return None
    digest = hashlib.sha256()
    try:
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1 << 16), b""):
                digest.update(chunk)
    except OSError:
        return None
    return digest.hexdigest()


def load_json(relative: str):
    path = ROOT / relative
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return None


def read_text(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def sanitize(text, limit=200) -> str:
    if isinstance(text, bytes):
        text = text.decode("utf-8", "replace")
    text = str(text).replace("\n", " ").replace("\r", " ")
    return text[:limit]


def scratch_tmp() -> Path:
    path = ROOT / ".scratch/r11x03-tmp"
    try:
        path.mkdir(parents=True, exist_ok=True)
    except OSError:
        pass
    return path


def system_tmp_base() -> Path:
    """A temp directory outside the repo (replay mirrors refuse in-repo)."""
    root = ROOT.resolve()
    for candidate in (Path(tempfile.gettempdir()), Path("/tmp")):
        try:
            resolved = candidate.resolve()
        except OSError:
            continue
        if resolved == root or root in resolved.parents:
            continue
        if resolved.is_dir():
            return resolved
    return Path(tempfile.gettempdir())


def run_cli(argv, timeout=180, tmpdir="in-repo"):
    """Run a repo command read-only-ish with a bounded TMPDIR.

    tmpdir="in-repo" puts TMPDIR under .scratch (lane convention).
    tmpdir="system" uses a disposable directory in the system temp location:
    replay-frozen refuses a mirror rooted inside the repo by design, so its
    invocations need one even when the caller exported TMPDIR into .scratch.
    """
    argv = [str(item) for item in argv]
    env = os.environ.copy()
    disposable = None
    if tmpdir == "system":
        disposable = Path(tempfile.mkdtemp(prefix="r11x03-",
                                           dir=str(system_tmp_base())))
        env["TMPDIR"] = str(disposable)
    else:
        env["TMPDIR"] = str(scratch_tmp())
    env.setdefault("PYTHONDONTWRITEBYTECODE", "1")
    result = {"argv": argv}
    try:
        proc = subprocess.run(argv, cwd=str(ROOT), capture_output=True,
                              timeout=timeout, env=env)
    except subprocess.TimeoutExpired as error:
        result.update({"exit": None, "timeout": True,
                       "stdout": (error.stdout or b"").decode("utf-8",
                                                              "replace"),
                       "stderr": (error.stderr or b"").decode("utf-8",
                                                              "replace"),
                       "error": f"timeout after {timeout}s"})
        return result
    except (OSError, subprocess.SubprocessError) as error:
        result.update({"exit": None, "error": sanitize(str(error))})
        return result
    finally:
        if disposable is not None:
            shutil.rmtree(disposable, ignore_errors=True)
    stdout = proc.stdout.decode("utf-8", "replace")
    stderr = proc.stderr.decode("utf-8", "replace")
    result.update({
        "exit": proc.returncode,
        "stdout": stdout,
        "stderr": stderr,
        "stdout_sha256": hashlib.sha256(proc.stdout).hexdigest(),
        "stderr_sha256": hashlib.sha256(proc.stderr).hexdigest(),
        "merged_sha256": hashlib.sha256(proc.stdout + proc.stderr).hexdigest(),
        "traceback": bool(TRACEBACK_RE.search(stdout + stderr)),
    })
    return result


def git(*args, timeout=60):
    try:
        proc = subprocess.run(("git",) + tuple(args), cwd=str(ROOT),
                              timeout=timeout, capture_output=True, text=True)
    except (OSError, subprocess.SubprocessError):
        return None
    if proc.returncode != 0:
        return None
    return proc.stdout


def json_objects(text: str):
    """Every top-level JSON object/array embedded in *text* (bounded scan)."""
    decoder = json.JSONDecoder()
    found = []
    position = 0
    while position < len(text) and len(found) < 12:
        index = text.find("{", position)
        if index < 0:
            break
        try:
            payload, end = decoder.raw_decode(text[index:])
        except json.JSONDecodeError:
            position = index + 1
            continue
        found.append(payload)
        position = index + max(end, 1)
    return found


def first_key(payload: dict, keys):
    for key in keys:
        if key in payload and payload[key] is not None:
            return key, payload[key]
    return None, None


def finding_token(item) -> str:
    """A stable comparison token for one finding/hold entry."""
    if isinstance(item, str):
        return item.strip()
    if isinstance(item, dict):
        ident = ""
        for key in ("id", "code", "finding", "finding_id", "name", "hold"):
            value = item.get(key)
            if isinstance(value, str) and value.strip():
                ident = value.strip()
                break
        where = ""
        for key in ("where", "entity", "target", "record", "record_id",
                    "subject", "locator"):
            value = item.get(key)
            if isinstance(value, str) and value.strip():
                where = value.strip()
                break
        if ident and where:
            return f"{ident}:{where}"
        if ident or where:
            return ident or where
        return json.dumps(item, sort_keys=True)[:160]
    return str(item).strip()


def token_parts(token: str):
    if ":" in token:
        head, tail = token.split(":", 1)
        return head.strip(), tail.strip()
    return token.strip(), ""


def infer_cause_class(text: str):
    for name, pattern in CLASS_PATTERNS:
        if pattern.search(text):
            return name
    return None


def recheck_class(payload: dict):
    _, raw = first_key(payload, ("drift_class", "cause_class",
                                 "classification", "drift_type"))
    if isinstance(raw, str) and raw.strip():
        token = raw.strip().lower()
        if "legit" in token:
            return "legitimate-change"
        if "environment" in token or "env" in token:
            return "environmental"
        if "defect" in token or "bug" in token or "regress" in token:
            return "defect"
        if re.search(r"non-?literal|prose|not[-_ ]?reproduc|reconstruct|"
                     r"unreproduc", token):
            return "unreproducible"
        found = infer_cause_class(raw)
        return found or f"other:{token}"
    cause = recheck_cause(payload, None)
    if cause:
        found = infer_cause_class(cause)
        return found or f"other:{cause[:48]}"
    return None


# --------------------------------------------------------------------------
# D — depth: typed pipeline wired through the D2 flow
# --------------------------------------------------------------------------

def measure_d_selftests():
    result, failures = {"runs": {}}, []
    for relative, argv in D2_SELFTESTS + D3_SELFTESTS:
        if not (ROOT / relative).is_file():
            failures.append(f"missing selftest target: {relative}")
            result["runs"][relative] = {"present": False}
            continue
        run = run_cli([sys.executable or "python3", relative, *argv],
                      timeout=300)
        counts = []
        for line in run.get("stdout", "").splitlines():
            if re.search(r"selftest", line, re.I):
                counts.extend(re.findall(r"(\d+)\s*/\s*(\d+)", line))
        entry = {
            "present": True, "argv": [relative, *argv],
            "exit": run.get("exit"), "traceback": run.get("traceback"),
            "stdout_sha256": run.get("stdout_sha256"),
            "tail": sanitize(run.get("stdout", ""), 160),
            "counts": counts[:6],
        }
        result["runs"][relative] = entry
        if run.get("exit") != 0:
            failures.append(
                f"{relative} {' '.join(argv)} exit {run.get('exit')} "
                f"(expected 0): {sanitize(run.get('stdout', ''), 160)}")
        if run.get("traceback"):
            failures.append(f"{relative} {' '.join(argv)} printed a traceback")
        for passed, total in entry["counts"]:
            if int(passed) != int(total):
                failures.append(
                    f"{relative} reports failing selftest controls "
                    f"{passed}/{total}")
    return result, failures


def measure_d_assembly():
    result, failures = {}, []
    if not (ROOT / D2_ASSEMBLER_REL).is_file():
        failures.append(f"missing assembler: {D2_ASSEMBLER_REL}")
        return result, failures
    run = run_cli(["python3", D2_ASSEMBLER_REL, "--check"], timeout=300)
    result["assembler_check"] = {
        "exit": run.get("exit"),
        "stdout_sha256": run.get("stdout_sha256"),
        "tail": sanitize(run.get("stdout", ""), 160)}
    if run.get("exit") != 0:
        failures.append(
            f"{D2_ASSEMBLER_REL} --check exit {run.get('exit')} (expected 0: "
            f"byte-identical deterministic assembly): "
            f"{sanitize(run.get('stdout', ''), 160)}")
    if (ROOT / D2_TYPED_PROJECTION_REL).is_file():
        typed = run_cli(["python3", D2_TYPED_REL, "--check"], timeout=300)
        result["typed_projection_check"] = {
            "path": D2_TYPED_PROJECTION_REL,
            "exit": typed.get("exit"),
            "stdout_sha256": typed.get("stdout_sha256"),
            "tail": sanitize(typed.get("stdout", ""), 160)}
        if typed.get("exit") != 0:
            failures.append(
                f"{D2_TYPED_REL} --check exit {typed.get('exit')} (expected 0: "
                f"the committed typed projection regenerates): "
                f"{sanitize(typed.get('stdout', ''), 160)}")
    else:
        failures.append(
            f"missing typed projection: {D2_TYPED_PROJECTION_REL}")
    return result, failures


def measure_d_battery():
    result, failures = {}, []
    if not (ROOT / BATTERY_REL).is_file():
        failures.append(f"missing battery runner: {BATTERY_REL}")
        return result, failures
    selftest = run_cli(["python3", BATTERY_REL, "--selftest"], timeout=600)
    result["selftest"] = {
        "exit": selftest.get("exit"),
        "traceback": selftest.get("traceback"),
        "stdout_sha256": selftest.get("stdout_sha256"),
        "tail": sanitize(selftest.get("stdout", ""), 200)}
    if selftest.get("exit") != 0:
        failures.append(
            f"{BATTERY_REL} --selftest exit {selftest.get('exit')} "
            f"(expected 0): {sanitize(selftest.get('stdout', ''), 200)}")
    if selftest.get("traceback"):
        failures.append(f"{BATTERY_REL} --selftest printed a traceback")

    env = os.environ.copy()
    env["TMPDIR"] = str(scratch_tmp())
    roots = [rel for rel in BATTERY_ROOT_CANDIDATES if (ROOT / rel).is_dir()]
    # only gate-shaped round-11 baselines join the run: a <root>/<gate-stem>/
    # expected.json whose stem is a live gate. Non-gate expected.json files
    # (e.g. the handoff exercise's own baseline) are never fed to the battery.
    gate_stems = {path.stem for path in
                  (ROOT / "tools/gates").glob("*.py")}
    report_root = ROOT / "reports/round-11"
    if report_root.is_dir():
        for path in sorted(report_root.rglob("expected.json")):
            if path.parent.name not in gate_stems:
                continue
            rel = path.parent.parent.relative_to(ROOT).as_posix()
            if rel not in roots:
                roots.append(rel)
    argv = ["python3", BATTERY_REL]
    for root in roots:
        argv += ["--baselines-root", root]
    run = run_cli(argv, timeout=900)
    summary, baselines = {}, {}
    for payload in json_objects(run.get("stdout", "")):
        if isinstance(payload, dict) and payload.get("tool") == \
                "check-gate-battery":
            summary = payload.get("summary") or {}
            baselines = (payload.get("baselines") or {}).get("summary") or {}
            break
    result["run"] = {
        "argv": argv[1:], "roots": roots, "exit": run.get("exit"),
        "summary": summary, "baseline_summary": baselines,
        "stdout_sha256": run.get("stdout_sha256"),
        "tail": sanitize(run.get("stdout", "")[-400:], 260)}
    if run.get("exit") != 0:
        detail = (f"summary={json.dumps(summary)} "
                  f"baselines={json.dumps(baselines)}")
        failures.append(
            f"{BATTERY_REL} battery exit {run.get('exit')} (expected 0: all "
            f"seven gates covered, none failing): {detail}")
    else:
        if summary.get("fail"):
            failures.append(
                f"{BATTERY_REL}: {summary.get('fail')} gate(s) failing")
        if summary.get("unevaluable"):
            failures.append(
                f"{BATTERY_REL}: {summary.get('unevaluable')} gate(s) "
                f"unevaluable")
        if baselines.get("gates_uncovered"):
            failures.append(
                f"{BATTERY_REL}: gates uncovered by baselines: "
                f"{', '.join(baselines['gates_uncovered'])}")
    return result, failures


def discover_e2e_receipts():
    """JSON receipts under reports/round-11 that declare a command + holds."""
    root = ROOT / "reports/round-11"
    if not root.is_dir():
        return []
    receipts = []
    for path in sorted(root.rglob("*.json")):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(RECHECK_DIR_REL + "/") or path == ROOT / OUTPUT_REL:
            continue
        if path.name in ("claims.json", "targets.json",
                         "validation.json"):
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(payload, dict):
            continue
        _, command = first_key(payload, CMD_KEYS)
        if isinstance(command, list):
            command = " ".join(str(item) for item in command)
        if not isinstance(command, str) or "python3" not in command:
            continue
        _, expected = first_key(payload, EXPECTED_KEYS)
        if not isinstance(expected, list):
            continue
        _, observed = first_key(payload, OBSERVED_KEYS)
        _, exit_code = first_key(payload, EXIT_KEYS)
        if isinstance(exit_code, str) and exit_code.strip().isdigit():
            exit_code = int(exit_code.strip())
        if not isinstance(exit_code, int):
            exit_code = None
        negative = bool(re.search(r"neg|control|malformed|broken",
                                  rel, re.I)) or bool(re.search(
            r"neg|control|malformed", json.dumps(payload)[:500], re.I))
        score = 0
        if "e2e" in rel.lower():
            score += 5
        if rel.startswith(DEPTH_DIR_REL):
            score += 2
        if exit_code == 0:
            score += 2
        if isinstance(observed, list):
            score += 1
        receipts.append({
            "path": rel, "command": command, "expected": expected,
            "observed": observed, "exit": exit_code, "negative": negative,
            "score": score, "payload": payload,
        })
    return receipts


def extract_expected_from_design():
    """expected_holds-style JSON block in the depth design, when present."""
    for relative in (DEPTH_DESIGN_REL,):
        text = read_text(relative)
        if not text:
            continue
        for payload in json_objects(text):
            if not isinstance(payload, dict):
                continue
            _, expected = first_key(payload, EXPECTED_KEYS)
            if isinstance(expected, list) and expected:
                return {"path": relative, "expected": expected}
    return None


def run_e2e_command(command: str, timeout=300):
    try:
        argv = shlex.split(command)
    except ValueError as error:
        return {"exit": None, "error": f"unparseable command: {error}"}
    if not argv or not argv[0].endswith("python3"):
        return {"exit": None, "error": "command does not start with python3"}
    return run_cli(argv, timeout=timeout)


def output_findings(stdout: str):
    """Findings list parsed from a machine-readable run output, else None."""
    stripped = stdout.strip()
    if stripped[:1] in ("[", "{"):
        try:
            whole = json.loads(stripped)
        except json.JSONDecodeError:
            whole = None
        if isinstance(whole, list):
            return whole
        if isinstance(whole, dict):
            _, findings = first_key(whole, OBSERVED_KEYS)
            if isinstance(findings, list):
                return findings
    for payload in json_objects(stdout):
        if isinstance(payload, dict):
            _, findings = first_key(payload, OBSERVED_KEYS)
            if isinstance(findings, list):
                return findings
    return None


def sound_channel_readings(run):
    stdout = run.get("stdout", "") or ""
    lines = [line.strip() for line in stdout.splitlines()
             if "PHON-INVENTORY" in line]
    translated = [line for line in lines
                  if "GAR-" in line or "translated" in line.lower()]
    return {"phon_lines": len(lines), "translated_phon_lines": translated[:3],
            "translated_phon_count": len(translated)}


def measure_d_e2e():
    result, failures = {"receipts": [], "evidence": None}, []
    receipts = discover_e2e_receipts()
    result["receipts"] = [
        {"path": item["path"], "exit": item["exit"],
         "expected_count": len(item["expected"]),
         "observed": isinstance(item["observed"], list),
         "negative": item["negative"], "score": item["score"]}
        for item in receipts]
    primaries = [item for item in receipts
                 if not item["negative"] and item["exit"] in (None, 0)
                 and item["expected"]]
    primaries.sort(key=lambda item: (-item["score"], item["path"]))
    if primaries:
        chosen = primaries[0]
        result["evidence"] = {"shape": "receipt", "path": chosen["path"]}
        run = run_e2e_command(chosen["command"])
        result["rerun"] = {
            "command": chosen["command"], "exit": run.get("exit"),
            "stdout_sha256": run.get("stdout_sha256"),
            "error": run.get("error"),
            "tail": sanitize(run.get("stdout", ""), 200)}
        if run.get("exit") != 0:
            failures.append(
                f"e2e: {chosen['path']} command exit {run.get('exit')} "
                f"(expected 0): "
                f"{sanitize(run.get('stdout', '') or run.get('error', ''), 200)}")
            return result, failures
        payload = chosen["payload"]
        context_text = "\n".join((json.dumps(payload)[:4000], chosen["command"],
                                  run.get("stdout", "")[:8000]))
        expected = [finding_token(item) for item in chosen["expected"]
                    if finding_token(item)]
        expected_set = set(expected)
        fresh = output_findings(run.get("stdout", ""))
        if fresh is not None:
            observed_set = {finding_token(item) for item in fresh
                            if finding_token(item)}
            result["observed_source"] = "fresh-run-output"
        elif isinstance(chosen["observed"], list) and chosen["observed"]:
            observed_set = {finding_token(item) for item in chosen["observed"]
                            if finding_token(item)}
            result["observed_source"] = "receipt-declared"
        else:
            observed_set = set()
            result["observed_source"] = None
            failures.append(
                f"e2e: no machine-readable findings in the rerun output and "
                f"{chosen['path']} declares no observed list")
        if not expected_set:
            failures.append("e2e: expected hold set is empty")
        if "culture-d2" not in context_text:
            failures.append(
                "e2e: neither the receipt, the command nor the fresh output "
                "references examples/culture-d2")
        if fresh is not None and isinstance(chosen["observed"], list) \
                and chosen["observed"]:
            declared = {finding_token(item) for item in chosen["observed"]
                        if finding_token(item)}
            if declared and declared != observed_set:
                failures.append(
                    "e2e: receipt's observed list disagrees with the fresh "
                    f"run's findings (receipt {len(declared)}, fresh "
                    f"{len(observed_set)})")
        if observed_set != expected_set:
            missing = sorted(expected_set - observed_set)
            extra = sorted(observed_set - expected_set)
            failures.append(
                "e2e: findings != expected hold set exactly "
                f"(missing {len(missing)}: {missing[:6]}; "
                f"extra {len(extra)}: {extra[:6]})")
        stdout = run.get("stdout", "") or ""
        for token in sorted(expected_set):
            head, tail = token_parts(token)
            if head and head not in context_text:
                failures.append(
                    f"e2e: expected hold {token!r} absent from the fresh "
                    "output")
            elif tail and tail not in stdout and tail not in context_text:
                failures.append(
                    f"e2e: expected hold {token!r} names {tail!r}, absent "
                    "from the fresh output")
        sound = sound_channel_readings(run)
        result["sound_channel"] = sound
        if sound["translated_phon_count"]:
            failures.append(
                "e2e: translated label(s) on the sound channel — "
                f"{sound['translated_phon_lines'][0][:160]}")
        for key in SOUND_KEYS:
            value = payload.get(key)
            if isinstance(value, int) and value != 0:
                failures.append(
                    f"e2e: {chosen['path']} declares {key}={value} "
                    "(expected 0: translated labels never enter the sound "
                    "channel)")
        _, owed = first_key(payload, OWED_KEYS)
        if isinstance(owed, list) and owed:
            owed_tokens = {finding_token(item) for item in owed}
            expected_parts = set()
            for token in expected_set:
                head, tail = token_parts(token)
                expected_parts.update({token, head, tail})
            for token in sorted(owed_tokens):
                if token not in expected_parts:
                    failures.append(
                        f"e2e: owed native form {token!r} is not carried as a "
                        "named expected hold")
                if token not in context_text:
                    failures.append(
                        f"e2e: owed native form {token!r} absent from the "
                        "fresh output")
        for key in HASH_KEYS:
            pinned = payload.get(key)
            if isinstance(pinned, str) and SHA256_RE.match(pinned):
                if pinned not in (run.get("stdout_sha256"),
                                  run.get("merged_sha256"),
                                  run.get("stderr_sha256")):
                    failures.append(
                        f"e2e: {chosen['path']} pins {key}={pinned[:12]}... "
                        "but the fresh run's stdout/stderr hashes differ")
                break
        return result, failures

    # shape (b): a documented live flow
    for path in sorted((ROOT / "tools").glob("*.py")):
        rel = path.relative_to(ROOT).as_posix()
        try:
            source = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if D2_TYPED_REL in source and "gates/" in source:
            help_run = run_cli(["python3", rel, "--help"], timeout=60)
            flags = sorted(set(re.findall(r"--[a-z0-9][a-z0-9-]+",
                                          help_run.get("stdout", ""))))
            flow_flags = [flag for flag in flags
                          if flag in ("--e2e", "--flow", "--typed-flow",
                                      "--wired-flow")]
            if flow_flags:
                argv = ["python3", rel, flow_flags[0]]
                if "--json" in flags:
                    argv.append("--json")
                run = run_cli(argv, timeout=300)
                expected_block = extract_expected_from_design()
                fresh = output_findings(run.get("stdout", ""))
                expected = [finding_token(item)
                            for item in (expected_block or {}).get("expected",
                                                                   [])]
                result["evidence"] = {"shape": "live-flow", "path": rel,
                                      "argv": argv[1:]}
                result["rerun"] = {
                    "command": " ".join(argv), "exit": run.get("exit"),
                    "stdout_sha256": run.get("stdout_sha256"),
                    "tail": sanitize(run.get("stdout", ""), 200)}
                if run.get("exit") != 0:
                    failures.append(
                        f"e2e: {rel} {' '.join(argv[1:])} exit "
                        f"{run.get('exit')} (expected 0)")
                    return result, failures
                sound = sound_channel_readings(run)
                result["sound_channel"] = sound
                if sound["translated_phon_count"]:
                    failures.append(
                        "e2e: translated label(s) on the sound channel — "
                        f"{sound['translated_phon_lines'][0][:160]}")
                if expected and fresh is not None:
                    observed = {finding_token(item) for item in fresh}
                    if observed != set(expected):
                        failures.append(
                            "e2e: live-flow findings != expected hold set "
                            f"(design.md block): missing "
                            f"{sorted(set(expected) - observed)[:6]}, extra "
                            f"{sorted(observed - set(expected))[:6]}")
                else:
                    failures.append(
                        f"e2e: {rel} ran but no expected hold set was found "
                        "(no design.md expected_holds JSON block and no "
                        "findings in the output); land the round's e2e "
                        "receipt or a machine-readable expected set")
                return result, failures

    documented = []
    design_text = read_text(DEPTH_DESIGN_REL)
    if design_text:
        for line in design_text.splitlines():
            if "python3" not in line or "culture-d2" not in line:
                continue
            if not re.search(r"(?i)e2e|end-to-end", line):
                continue
            for span in re.findall(r"`([^`]*python3[^`]*)`", line):
                if re.search(r"[<>|&;$]|\.\.\.", span):
                    continue
                parts = shlex.split(span)
                script = next((token for token in parts[1:]
                               if token.endswith(".py")), None)
                if script and (ROOT / script).is_file():
                    documented.append(span.strip())
    if documented:
        command = documented[0]
        run = run_e2e_command(command)
        expected_block = extract_expected_from_design()
        fresh = output_findings(run.get("stdout", ""))
        result["evidence"] = {"shape": "documented-command", "command": command}
        result["rerun"] = {"command": command, "exit": run.get("exit"),
                           "stdout_sha256": run.get("stdout_sha256"),
                           "tail": sanitize(run.get("stdout", ""), 200)}
        if run.get("exit") != 0:
            failures.append(
                f"e2e: documented command exit {run.get('exit')} (expected "
                f"0): {sanitize(run.get('stdout', '') or run.get('error', ''),
                                200)}")
        else:
            sound = sound_channel_readings(run)
            if sound["translated_phon_count"]:
                failures.append(
                    "e2e: translated label(s) on the sound channel — "
                    f"{sound['translated_phon_lines'][0][:160]}")
            expected = [finding_token(item)
                        for item in (expected_block or {}).get("expected", [])]
            if expected and fresh is not None:
                observed = {finding_token(item) for item in fresh}
                if observed != set(expected):
                    failures.append(
                        "e2e: documented-command findings != expected hold "
                        "set")
            else:
                failures.append(
                    "e2e: documented command ran but no expected hold set "
                    "was found to compare against; land the round's e2e "
                    "receipt (command + expected_holds + observed) or a "
                    "design.md expected_holds JSON block")
        return result, failures

    result["evidence"] = None
    failures.append(
        "e2e: no round-11 e2e evidence found — no JSON receipt under "
        "reports/round-11 with command + expected_holds, no wired flow "
        "(--e2e/--flow) tool, no documented e2e command in "
        f"{DEPTH_DESIGN_REL}")
    return result, failures


def discover_replay_manifests():
    found = set()
    for pattern in ("reports/round-11/**/*.tsv",
                    "tools/gates/frozen/round-11/**/*.tsv",
                    "tools/gates/frozen/r11*/**/*.tsv"):
        for path in ROOT.glob(pattern):
            if path.is_file():
                found.add(path)
    ranked = []
    for path in sorted(found):
        try:
            first = path.read_text(encoding="utf-8", errors="replace") \
                .splitlines()[:1]
        except OSError:
            continue
        header = first[0] if first else ""
        if "sha256" in header.lower():
            ranked.append(path)
    return ranked


def measure_d_replay():
    result, failures = {"manifests": [], "runs": []}, []
    manifests = discover_replay_manifests()
    result["manifests"] = [path.relative_to(ROOT).as_posix()
                           for path in manifests]
    if not manifests:
        failures.append(
            "replay: no round-11 frozen manifest found (reports/round-11/"
            "**/*.tsv or tools/gates/frozen/round-11/**) — the re-pin is not "
            "recorded")
        return result, failures
    green = 0
    for path in manifests[:3]:
        rel = path.relative_to(ROOT).as_posix()
        negative = bool(re.search(r"neg|control|broken", rel, re.I))
        run = run_cli(["python3", REPLAY_REL, rel, "--json"], timeout=300,
                      tmpdir="system")
        summary = {}
        for payload in json_objects(run.get("stdout", "")):
            if isinstance(payload, dict) and isinstance(payload.get("summary"),
                                                       dict):
                summary = payload["summary"]
                break
        entry = {"manifest": rel, "exit": run.get("exit"), "summary": summary,
                 "negative_control": negative,
                 "stdout_sha256": run.get("stdout_sha256"),
                 "tail": sanitize(run.get("stdout", ""), 200)}
        result["runs"].append(entry)
        ok = (run.get("exit") == 0 and summary
              and not summary.get("mismatch")
              and not summary.get("could_not_evaluate")
              and summary.get("rows")
              and summary.get("reproduced") == summary.get("rows"))
        entry["green"] = bool(ok)
        if ok:
            green += 1
        elif not negative:
            failures.append(
                f"replay: {rel} not green (exit {run.get('exit')}, summary "
                f"{json.dumps(summary) if summary else 'unparseable'}): "
                f"{sanitize(run.get('stdout', ''), 160)}")
    if green == 0:
        failures.append(
            "replay: no round-11 manifest reproduces every row without "
            "digest drift")
    return result, failures


def measure_d_interop():
    result, failures = {}, []
    if not (ROOT / D3_ASSEMBLER_REL).is_file():
        failures.append(f"missing D3 assembler: {D3_ASSEMBLER_REL}")
        return result, failures
    check = run_cli(["python3", D3_ASSEMBLER_REL, "--check"], timeout=300)
    result["d3_assembler_check"] = {
        "exit": check.get("exit"), "stdout_sha256": check.get("stdout_sha256"),
        "tail": sanitize(check.get("stdout", ""), 200)}
    if check.get("exit") != 0:
        failures.append(
            f"interop: {D3_ASSEMBLER_REL} --check exit {check.get('exit')} "
            f"(expected 0): {sanitize(check.get('stdout', ''), 160)}")
    if (ROOT / D3_PACKET_REL).is_file() and (ROOT / D3_EXPECTED_REL).is_file():
        frozen = run_cli(["python3", D3_COUPLING_REL, D3_PACKET_REL,
                          "--frozen", D3_EXPECTED_REL], timeout=300)
        totals = None
        for payload in json_objects(frozen.get("stdout", "")):
            if isinstance(payload, dict) and isinstance(payload.get("counts"),
                                                        dict):
                totals = payload["counts"].get("total")
                break
        result["d3_frozen_replay"] = {
            "exit": frozen.get("exit"), "findings_total": totals,
            "stdout_sha256": frozen.get("stdout_sha256"),
            "tail": sanitize(frozen.get("stdout", ""), 200)}
        if frozen.get("exit") != 0 or (isinstance(totals, int) and totals):
            failures.append(
                f"interop: {D3_COUPLING_REL} {D3_PACKET_REL} --frozen "
                f"{D3_EXPECTED_REL} exit {frozen.get('exit')} with "
                f"{totals} finding(s) (expected 0/0)")
    else:
        failures.append(
            f"interop: missing D3 frozen acceptance inputs "
            f"({D3_PACKET_REL} / {D3_EXPECTED_REL})")
    return result, failures


def measure_d():
    selftests, selftest_failures = measure_d_selftests()
    assembly, assembly_failures = measure_d_assembly()
    battery, battery_failures = measure_d_battery()
    e2e, e2e_failures = measure_d_e2e()
    replay, replay_failures = measure_d_replay()
    interop, interop_failures = measure_d_interop()
    failures = (selftest_failures + assembly_failures + battery_failures
                + e2e_failures + replay_failures + interop_failures)
    return {
        "passed": not failures,
        "failures": failures,
        "measurement": {
            "selftests": selftests, "assembly": assembly, "battery": battery,
            "e2e": e2e, "replay_frozen": replay, "interop_d3": interop,
        },
        "missing_dependencies": sorted({
            item for item, absent in (
                (D2_ASSEMBLER_REL, not (ROOT / D2_ASSEMBLER_REL).is_file()),
                (D2_TYPED_REL, not (ROOT / D2_TYPED_REL).is_file()),
                (D2_TYPED_PROJECTION_REL,
                 not (ROOT / D2_TYPED_PROJECTION_REL).is_file()),
                (BATTERY_REL, not (ROOT / BATTERY_REL).is_file()),
                (DEPTH_DIR_REL, not (ROOT / DEPTH_DIR_REL).is_dir()),
            ) if absent}),
    }


# --------------------------------------------------------------------------
# O — operability: handoff e2e exercise
# --------------------------------------------------------------------------

def discover_exercise_tools():
    named = ROOT / EXERCISE_REL
    candidates = []
    if named.is_file():
        candidates.append(named)
    tools_dir = ROOT / "tools"
    if tools_dir.is_dir():
        for path in sorted(tools_dir.glob("*.py")):
            if path == named:
                continue
            name = path.name.lower()
            if "handoff" in name and re.search(r"e2e|exercise", name):
                candidates.append(path)
                continue
            try:
                source = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            if ("handoff-packet-check" in source and "expected.json" in source
                    and re.search(r"e2e|exercise", source, re.I)
                    and re.search(r"glossary|envelope|mkdtemp|"
                                  r"TemporaryDirectory", source)):
                candidates.append(path)
    return candidates


def measure_o_exercise():
    result, failures = {}, []
    candidates = discover_exercise_tools()
    result["candidates"] = [path.relative_to(ROOT).as_posix()
                            for path in candidates]
    if not candidates:
        failures.append(
            f"exercise: no handoff e2e exercise found (expected "
            f"{EXERCISE_REL} or a documented equivalent)")
        return result, failures
    tool = candidates[0].relative_to(ROOT).as_posix()
    result["tool"] = tool

    selftest = run_cli(["python3", tool, "--selftest"], timeout=300)
    combined = selftest.get("stdout", "") + selftest.get("stderr", "")
    malformed = bool(re.search(r"malformed|invalid|corrupt|refus|reject",
                               combined, re.I))
    positive = bool(re.search(r"positive|clean|valid|accept", combined, re.I))
    counts = re.findall(r"(\d+)\s*/\s*(\d+)", selftest.get("stdout", ""))
    result["selftest"] = {
        "exit": selftest.get("exit"), "traceback": selftest.get("traceback"),
        "malformed_controls": malformed, "positive_controls": positive,
        "counts": counts[:6],
        "stdout_sha256": selftest.get("stdout_sha256"),
        "tail": sanitize(selftest.get("stdout", ""), 220)}
    if selftest.get("exit") != 0:
        failures.append(
            f"exercise: {tool} --selftest exit {selftest.get('exit')} "
            f"(expected 0): {sanitize(selftest.get('stdout', ''), 200)}")
    if selftest.get("traceback"):
        failures.append(f"exercise: {tool} --selftest printed a traceback")
    if not malformed:
        failures.append(
            f"exercise: {tool} --selftest names no malformed-input controls")
    if not positive:
        failures.append(
            f"exercise: {tool} --selftest names no positive/clean control")
    for passed, total in counts:
        if int(passed) != int(total):
            failures.append(
                f"exercise: {tool} --selftest reports failing controls "
                f"{passed}/{total}")

    help_run = run_cli(["python3", tool, "--help"], timeout=60)
    flags = sorted(set(re.findall(r"--[a-z0-9][a-z0-9-]+",
                                  help_run.get("stdout", ""))))
    result["flags"] = flags
    attempts = []
    chosen_run = None
    for argv in ([], ["--json"] if "--json" in flags else [],
                 ["--check"] if "--check" in flags else []):
        run = run_cli(["python3", tool, *argv], timeout=600)
        attempts.append({"argv": argv, "exit": run.get("exit"),
                         "stdout_sha256": run.get("stdout_sha256")})
        if run.get("exit") == 0:
            chosen_run = run
            chosen_run["_argv"] = argv
            break
    result["run_attempts"] = attempts
    if chosen_run is None:
        failures.append(
            f"exercise: {tool} run modes {[a['argv'] for a in attempts]} all "
            "non-zero (expected exit 0)")
        return result, failures
    combined = chosen_run.get("stdout", "") + chosen_run.get("stderr", "")
    result["run"] = {
        "argv": chosen_run["_argv"], "exit": chosen_run.get("exit"),
        "stdout_sha256": chosen_run.get("stdout_sha256"),
        "tail": sanitize(chosen_run.get("stdout", ""), 260)}

    fields = None
    glossary = None
    findings_zero = False
    scan = re.search(r"fields=(\d+)/(\d+)\s+glossary-entries=(\d+)\s+"
                     r"findings=(\d+)", combined)
    if scan:
        fields, glossary = int(scan.group(1)), int(scan.group(3))
        findings_zero = int(scan.group(4)) == 0
        result["scan_line"] = sanitize(scan.group(0), 120)
    else:
        for match in re.finditer(r"fields[^\d]{0,24}(\d+)\s*/\s*(\d+)",
                                 combined, re.I):
            fields = int(match.group(1))
            break
        for match in re.finditer(r"glossary[^\d]{0,32}(\d+)\s*/\s*(\d+)",
                                 combined, re.I):
            glossary = int(match.group(1))
            break
        if fields is None:
            for match in re.finditer(r"(\d+)\s*/\s*(\d+)[^\n]{0,20}fields",
                                     combined, re.I):
                fields = int(match.group(1))
                break
        if glossary is None:
            for match in re.finditer(r"(\d+)\s*/\s*(\d+)[^\n]{0,24}glossary",
                                     combined, re.I):
                glossary = int(match.group(1))
                break
        if re.search(r"findings\s*[:=]\s*0\b", combined, re.I) or \
                re.search(r'"findings"\s*:\s*\[\s*\]', combined):
            findings_zero = True
    result["packet_counts"] = {"fields": fields, "glossary": glossary,
                               "findings_zero": findings_zero}
    if fields != O_REQUIRED_FIELDS:
        failures.append(
            f"exercise: 16/16 envelope fields not demonstrated (read "
            f"{fields!r}): {sanitize(combined, 200)}")
    if glossary != O_REQUIRED_GLOSSARY:
        failures.append(
            f"exercise: 20/20 glossary entries not demonstrated (read "
            f"{glossary!r}): {sanitize(combined, 200)}")
    if not findings_zero:
        failures.append(
            "exercise: no clean gate verdict in the exercise output "
            "(findings=0 / empty findings not found)")
    if "handoff-packet-check" not in combined:
        failures.append(
            "exercise: output never references handoff-packet-check — the "
            "packet was not shown to pass through the gate")

    baselines = []
    patterns = (
        "tools/*handoff*expected*.json",
        "tools/*expected*.json",
        "examples/*handoff*.json",
        "reports/round-11/**/*expected*.json",
        "reports/round-11/handoff/**/*.json",
    )
    for pattern in patterns:
        for path in sorted(ROOT.glob(pattern)):
            rel = path.relative_to(ROOT).as_posix()
            if path.is_file() and rel not in baselines:
                baselines.append(rel)
    try:
        source = (ROOT / tool).read_text(encoding="utf-8", errors="replace")
    except OSError:
        source = ""
    for match in re.findall(r"[\w./-]*expected[\w./-]*\.json", source):
        candidate = match.lstrip("./")
        if (ROOT / candidate).is_file() and candidate not in baselines:
            baselines.append(candidate)
    result["baselines"] = baselines
    if not baselines:
        failures.append(
            "exercise: no frozen expected.json baseline found (expected*"
            ".json in tools/, examples/ or reports/round-11/)")
    else:
        primary = baselines[0]
        payload = load_json(primary)
        tracked = git("ls-files", "--error-unmatch", "--", primary)
        result["baseline"] = {
            "path": primary, "parseable": payload is not None,
            "git_tracked": tracked is not None,
            "size": (ROOT / primary).stat().st_size
            if (ROOT / primary).is_file() else 0}
        if payload is None:
            failures.append(
                f"exercise: frozen baseline {primary} is not parseable JSON")
        if "expected" not in source.lower():
            failures.append(
                f"exercise: {tool} source never reads a frozen expected "
                "baseline")
    return result, failures


def measure_o():
    exercise, failures = measure_o_exercise()
    return {
        "passed": not failures,
        "failures": failures,
        "measurement": {"exercise": exercise},
        "missing_dependencies": sorted({
            item for item, absent in (
                (EXERCISE_REL, not (ROOT / EXERCISE_REL).is_file()),
                (HANDOFF_CHECK_REL, not (ROOT / HANDOFF_CHECK_REL).is_file()),
            ) if absent}),
    }


# --------------------------------------------------------------------------
# F — freshness: round-10 ledger recheck
# --------------------------------------------------------------------------

def ledger_rows():
    payload = load_json(LEDGER_REL)
    if isinstance(payload, list):
        return [row for row in payload if isinstance(row, dict)]
    if isinstance(payload, dict):
        for key in ("rows", "entries", "ledger", "commands"):
            if isinstance(payload.get(key), list):
                return [row for row in payload[key] if isinstance(row, dict)]
    return []


def discover_recheck_receipts():
    directory = ROOT / RECHECK_DIR_REL
    receipts = []
    if not directory.is_dir():
        return receipts, []
    notes = []
    for path in sorted(directory.glob("row-*.json")):
        rel = path.relative_to(ROOT).as_posix()
        match = re.search(r"row-(\d+)", path.stem)
        payload = load_json(rel)
        if not isinstance(payload, dict):
            notes.append(f"{rel}: unparseable")
            continue
        index = None
        if match:
            index = int(match.group(1))
        else:
            _, value = first_key(payload, LEDGER_INDEX_KEYS)
            if isinstance(value, int):
                index = value
        receipts.append({"path": rel, "index": index, "payload": payload})
    if not receipts:
        for pattern in ("*.json", "*/*.json"):
            for path in sorted(directory.glob(pattern)):
                rel = path.relative_to(ROOT).as_posix()
                payload = load_json(rel)
                if not isinstance(payload, dict):
                    continue
                rows_map = None
                for key in ("rows", "receipts", "row_receipts"):
                    if isinstance(payload.get(key), dict):
                        rows_map = payload[key]
                        break
                if rows_map is None:
                    continue
                for key, value in rows_map.items():
                    if not isinstance(value, dict):
                        continue
                    try:
                        index = int(str(key).lstrip("row-"))
                    except ValueError:
                        _, raw = first_key(value, LEDGER_INDEX_KEYS)
                        index = raw if isinstance(raw, int) else None
                    receipts.append({"path": rel, "index": index,
                                     "payload": value})
                if receipts:
                    notes.append(f"{rel}: consolidated row map")
                    break
    return receipts, notes


def recheck_cause(payload: dict, summary_dispositions):
    _, value = first_key(payload, CAUSE_KEYS)
    if value:
        return str(value).strip()
    if isinstance(summary_dispositions, dict):
        for key in (str(payload.get("row", "")), str(payload.get("index",
                                                                 ""))):
            if key and key in summary_dispositions:
                return str(summary_dispositions[key]).strip()
    return ""


def measure_f():
    result, failures = {}, []
    rows = ledger_rows()
    result["ledger_rows"] = len(rows)
    if not rows:
        failures.append(f"recheck: {LEDGER_REL} absent or carries no rows")
    receipts, notes = discover_recheck_receipts()
    result["notes"] = notes
    if not receipts:
        failures.append(
            f"recheck: no row receipts under {RECHECK_DIR_REL}/row-*.json")

    summary = load_json(RECHECK_SUMMARY_REL)
    dispositions = None
    if isinstance(summary, dict):
        for key in ("dispositions", "drift_dispositions"):
            if isinstance(summary.get(key), (dict, list)):
                dispositions = summary[key]
                break

    measured, unreproducible, unstable, contradictions = [], [], [], []
    index_conflicts = {}
    for receipt in receipts:
        rel, payload = receipt["path"], receipt["payload"]
        index = receipt["index"]
        if not isinstance(index, int) or index < 0 or index >= len(rows):
            failures.append(
                f"recheck: {rel} does not address a ledger row "
                f"(index {index!r})")
            continue
        entry = index_conflicts.setdefault(index, [])
        entry.append(rel)
        row = rows[index]
        _, prior = first_key(payload, PRIOR_HASH_KEYS)
        _, new = first_key(payload, NEW_HASH_KEYS)
        stable = payload.get("stable")
        if not (isinstance(prior, str) and SHA256_RE.match(prior)):
            failures.append(
                f"recheck: {rel} carries no 64-hex prior_hash")
            continue
        if prior != row.get("output_sha256"):
            failures.append(
                f"recheck: {rel} prior_hash {prior[:12]}... does not match "
                f"ledger row {index}'s recorded output_sha256 "
                f"{str(row.get('output_sha256'))[:12]}... (1:1 binding "
                "broken)")
            continue
        if not isinstance(stable, bool):
            failures.append(f"recheck: {rel} 'stable' is not a boolean")
            continue
        command = payload.get("command")
        if isinstance(command, str) and isinstance(row.get("command"), str) \
                and " ".join(command.split()) != " ".join(row["command"].split()):
            failures.append(
                f"recheck: {rel} command is not the ledger row's command "
                "1:1 — keep the ledger text in `command` (the row-006 "
                "convention) and record the executed form separately")
        record = {"row": index, "path": rel, "stable": stable,
                  "payload": payload}
        if isinstance(new, str) and SHA256_RE.match(new):
            hash_stable = new == prior
            if stable != hash_stable:
                contradictions.append(
                    f"{rel}: stable={stable} but new_hash "
                    f"{'==' if hash_stable else '!='} prior_hash")
            record["hash_stable"] = hash_stable
            measured.append(record)
            _, new_exit = first_key(payload, EXIT_KEYS)
            prior_exit = row.get("exit")
            exit_changed = (isinstance(new_exit, int)
                            and isinstance(prior_exit, int)
                            and new_exit != prior_exit)
            record["exit_changed"] = exit_changed
            if not hash_stable or exit_changed:
                reason = ("hash drift" if not hash_stable else
                          f"exit changed {prior_exit}->{new_exit}")
                unstable.append({"row": index, "path": rel, "reason": reason,
                                 "receipt": record})
        else:
            # no byte-comparable re-run: the row is a dispositioned
            # not-reproducible case, never silently counted as stable
            record["hash_stable"] = False
            unreproducible.append(record)
            reason = str(payload.get("comparison")
                         or payload.get("hash_method")
                         or "no byte-comparable re-run recorded")
            unstable.append({"row": index, "path": rel,
                             "reason": f"unreproducible ({reason})",
                             "receipt": record})

    for index, paths in index_conflicts.items():
        if len(paths) > 1:
            hashes = {json.dumps(load_json(path), sort_keys=True)
                      for path in paths}
            if len(hashes) > 1:
                failures.append(
                    f"recheck: ledger row {index} has {len(paths)} "
                    "conflicting receipts")

    result["rows_rechecked"] = len(measured)
    result["unreproducible_dispositioned"] = len(unreproducible)
    result["stable"] = sum(1 for item in measured if item["stable"])
    result["unstable"] = len(measured) - result["stable"]
    result["stability"] = (result["stable"] / len(measured)) if measured \
        else None
    result["contradictions"] = contradictions
    if contradictions:
        failures.append(
            f"recheck: {len(contradictions)} receipt(s) contradict their own "
            f"hashes: {contradictions[:3]}")
    if len(measured) < F_MIN_ROWS:
        failures.append(
            f"recheck: {len(measured)} ledger commands re-run 1:1 < required "
            f"{F_MIN_ROWS}")
    if measured and result["stability"] < F_MIN_STABILITY:
        failures.append(
            f"recheck: stability {result['stability']:.3f} < required "
            f"{F_MIN_STABILITY}")
    for item in unstable:
        payload = item["receipt"]["payload"]
        cause = recheck_cause(payload, dispositions)
        klass = recheck_class(payload)
        item["drift_cause"] = cause
        item["drift_class"] = klass
        if not cause and not klass:
            failures.append(
                f"recheck: row {item['row']} ({item['path']}) drifted "
                f"({item['reason']}) with no disposition")
        elif klass is None:
            failures.append(
                f"recheck: row {item['row']} drift cause {cause[:80]!r} names "
                "none of the licensed classes (legitimate change / "
                "environmental / defect / unreproducible-by-construction)")
    result["drift_rows"] = [{key: value for key, value in item.items()
                             if key != "receipt"} for item in unstable]

    audit_present = (ROOT / RECHECK_AUDIT_REL).is_file()
    if not audit_present:
        failures.append(f"recheck: auditor artifact {RECHECK_AUDIT_REL} "
                        "absent")
        audit_commands, mismatch_readings = [], []
    else:
        text = read_text(RECHECK_AUDIT_REL)
        audit_commands = []
        for row in rows:
            command = row.get("command")
            if isinstance(command, str) and command.strip() and \
                    " ".join(command.split()) in " ".join(text.split()):
                audit_commands.append(command)
        if not audit_commands:
            audit_commands = sorted(set(
                match.strip() for match in re.findall(r"python3 [^\n`]+",
                                                      text)))
        mismatch_readings = []
        for match in re.finditer(r"(?i)mismatch\w*[^0-9\n]{0,24}(\d+)", text):
            if int(match.group(1)) > 0:
                mismatch_readings.append(match.group(0).strip()[:120])
        for match in re.finditer(r"(\d+)\s+mismatch", text):
            if int(match.group(1)) > 0:
                mismatch_readings.append(match.group(0).strip()[:120])
        if len(audit_commands) < F_MIN_AUDIT_RERUNS:
            failures.append(
                f"recheck: audit.md shows {len(audit_commands)} independent "
                f"re-runs < required {F_MIN_AUDIT_RERUNS}")
        if mismatch_readings:
            failures.append(
                f"recheck: audit.md records {len(mismatch_readings)} "
                f"unexplained mismatch reading(s): {mismatch_readings[:3]}")
        if not re.search(r"receipt|row-\d", text):
            failures.append(
                "recheck: audit.md never references the recheck receipts")
    result["audit"] = {"present": audit_present,
                       "independent_reruns": len(audit_commands),
                       "mismatch_readings": mismatch_readings}

    if not isinstance(summary, dict):
        failures.append(f"recheck: {RECHECK_SUMMARY_REL} absent or "
                        "unparseable")
    else:
        _, rows_declared = first_key(summary, ("rows_rechecked", "rows_reckecked",
                                               "rows", "total", "count"))
        stable_declared = summary.get("stable")
        unstable_declared = summary.get("unstable")
        result["summary"] = {"rows": rows_declared, "stable": stable_declared,
                             "unstable": unstable_declared}
        if rows_declared is None:
            failures.append(
                "recheck: summary.json carries no rows_rechecked count")
        elif rows_declared not in (len(measured),
                                   len(measured) + len(unreproducible)):
            failures.append(
                f"recheck: summary.json declares rows_rechecked="
                f"{rows_declared} but {len(measured)} receipts were measured "
                f"1:1 (+{len(unreproducible)} dispositioned unreproducible)")
        if isinstance(stable_declared, int) and stable_declared != \
                result["stable"]:
            failures.append(
                f"recheck: summary.json stable={stable_declared} != "
                f"receipts' {result['stable']}")
        if isinstance(unstable_declared, int) and unstable_declared not in \
                (result["unstable"], len(unstable),
                 result["unstable"] + len(unreproducible)):
            failures.append(
                f"recheck: summary.json unstable={unstable_declared} != "
                f"receipts' {result['unstable']} measured-hash drift "
                f"(+{len(unreproducible)} unreproducible, "
                f"{len(unstable)} dispositioned rows)")
        elif isinstance(unstable_declared, list) and \
                len(unstable_declared) not in (result["unstable"],
                                               len(unstable),
                                               result["unstable"] +
                                               len(unreproducible)):
            failures.append(
                f"recheck: summary.json lists {len(unstable_declared)} "
                f"dispositions but the receipts show {result['unstable']} "
                f"measured drift(s) (+{len(unreproducible)} unreproducible)")

    return {
        "passed": not failures,
        "failures": failures,
        "measurement": result,
        "missing_dependencies": sorted({
            item for item, absent in (
                (LEDGER_REL, not (ROOT / LEDGER_REL).is_file()),
                (RECHECK_DIR_REL, not (ROOT / RECHECK_DIR_REL).is_dir()),
                (RECHECK_AUDIT_REL,
                 not (ROOT / RECHECK_AUDIT_REL).is_file()),
                (RECHECK_SUMMARY_REL,
                 not (ROOT / RECHECK_SUMMARY_REL).is_file()),
            ) if absent}),
    }


# --------------------------------------------------------------------------
# receipt
# --------------------------------------------------------------------------

def main():
    claims = load_json(CLAIMS_REL) or {}
    results = {"D": measure_d(), "O": measure_o(), "F": measure_f()}
    passed = all(result["passed"] for result in results.values())

    consumed = {CLAIMS_REL, TARGETS_REL, LEDGER_REL, DEPTH_DESIGN_REL,
                RECHECK_AUDIT_REL, RECHECK_SUMMARY_REL, D2_ASSEMBLER_REL,
                D2_TYPED_REL, D2_TYPED_PROJECTION_REL, D3_ASSEMBLER_REL,
                D3_COUPLING_REL, D3_PACKET_REL, D3_EXPECTED_REL, BATTERY_REL,
                REPLAY_REL, HANDOFF_CHECK_REL, EXERCISE_REL}
    d_measurement = results["D"]["measurement"]
    e2e_evidence = (d_measurement.get("e2e") or {}).get("evidence") or {}
    if e2e_evidence.get("path"):
        consumed.add(e2e_evidence["path"])
    o_measurement = results["O"]["measurement"].get("exercise") or {}
    if o_measurement.get("tool"):
        consumed.add(o_measurement["tool"])
    consumed.update(o_measurement.get("baselines") or [])
    consumed.update(d_measurement.get("replay_frozen", {}).get("manifests",
                                                               []))
    for receipt in (results["F"]["measurement"].get("drift_rows") or []):
        consumed.add(receipt.get("path", ""))
    recheck_dir = ROOT / RECHECK_DIR_REL
    if recheck_dir.is_dir():
        consumed.update(f"{RECHECK_DIR_REL}/{path.name}"
                        for path in recheck_dir.glob("row-*.json"))
    depth_dir = ROOT / "reports/round-11/depth"
    if depth_dir.is_dir():
        consumed.update(path.relative_to(ROOT).as_posix()
                        for path in depth_dir.rglob("*.json"))

    missing = sorted({item for result in results.values()
                      for item in result["missing_dependencies"]} |
                     {item for item in consumed if item and
                      not (ROOT / item).exists()})
    receipt = {
        "round": 11,
        "runner": SELF_REL,
        "runner_sha256": sha256_file(SELF_REL),
        "counting_command": "python3 reports/round-11/run-validation.py",
        "claims_declared": {claim.get("id"): claim.get("axis")
                            for claim in claims.get("claims", [])},
        "baseline_revision": claims.get("baseline_revision"),
        "date": claims.get("date"),
        "regimen": claims.get("regimen"),
        "thresholds": {
            "D": {
                "e2e": "exit 0; findings set == expected hold set exactly; "
                       "no PHON-INVENTORY line naming a translated GAR "
                       "label; owed forms carried as named holds; output "
                       "hash pin (when declared) reproduced",
                "selftests": [f"{rel} {' '.join(argv)}"
                              for rel, argv in D2_SELFTESTS + D3_SELFTESTS],
                "assembly": f"{D2_ASSEMBLER_REL} --check exit 0",
                "typed_projection": f"{D2_TYPED_REL} --check exit 0",
                "battery": "check-gate-battery --selftest exit 0; battery "
                           "run with the frozen/expected/round-9 baselines "
                           "roots (+ round-11 roots) exit 0, 7 pass, 0 "
                           "fail, 0 unevaluable, 0 uncovered",
                "replay": "a round-11 MANIFEST.tsv reproduces every row with "
                          "no digest drift",
                "interop": "assemble-culture-d3 --check exit 0; "
                           "check-evidence-coupling --frozen exit 0 with 0 "
                           "findings",
            },
            "O": {
                "fields": O_REQUIRED_FIELDS, "glossary": O_REQUIRED_GLOSSARY,
                "selftest": "exit 0 with positive + malformed controls",
                "exercise": "exit 0; 16/16 fields; 20/20 glossary entries; "
                            "clean gate verdict; handoff-packet-check "
                            "referenced",
                "baseline": "frozen *expected*.json exists and parses; the "
                            "exercise source reads it",
            },
            "F": {
                "min_rows": F_MIN_ROWS, "min_stability": F_MIN_STABILITY,
                "min_audit_reruns": F_MIN_AUDIT_RERUNS,
                "binding": "receipt prior_hash == round-10 ledger row "
                           "output_sha256; command text 1:1; stable == "
                           "(new_hash == prior_hash)",
                "dispositions": "every unstable row carries a cause naming "
                                "legitimate change / environmental / defect",
                "summary": "summary.json counts equal the receipts'",
            },
        },
        "acceptance_checks_passed": passed,
        "claims": results,
        "failures": [f"claim {claim_id}: {failure}"
                     for claim_id in ("D", "O", "F")
                     for failure in results[claim_id]["failures"]],
        "missing_dependencies": missing,
        "input_sha256": {relative: sha256_file(relative)
                         for relative in sorted(consumed)
                         if relative and sha256_file(relative) is not None},
        "limits": [
            "Structural/evidence-presence checks plus the round's own "
            "read-only commands (--check/--selftest/battery/replay). The "
            "runner does not re-run the ledger commands itself; the F leg "
            "cross-checks the recheck seats' receipts against the ledger's "
            "recorded hashes and the audit's independent re-runs.",
            "The D e2e leg prefers a machine-readable receipt and re-runs "
            "its recorded command; when the output is not JSON the "
            "expected-vs-observed equality is read from the receipt's own "
            "lists, so a receipt that fabricates both lists is caught only "
            "by the output-hash pin (when declared) and the expected-token "
            "presence checks. Receipt shapes outside the documented keys "
            "are misses, not skips.",
            "The sound-channel check is concrete: no PHON-INVENTORY line "
            "may name a GAR label or the word 'translated'. A different "
            "smuggling route (e.g. an owed form silently dropped) is "
            "covered only through the exact expected-set equality.",
            "The battery is run with the committed baseline roots (frozen, "
            "expected, reports/round-9/baselines) plus any round-11 root "
            "carrying a gate-shaped <root>/<gate-stem>/expected.json; the "
            "plain default-root run leaves two gates uncovered (myth/naming) "
            "and is not used as the acceptance reading. Non-gate "
            "expected.json files (e.g. the handoff exercise's own baseline) "
            "are never fed to the battery.",
            "The replay leg runs replay-frozen.py with a disposable TMPDIR "
            "outside the repo (the tool refuses an in-repo mirror by "
            "design), falling back to /tmp when the caller's TMPDIR sits "
            "under .scratch.",
            "The exercise leg parses 16/16 and 20/20 from the exercise's "
            "own output (INFO scan line or JSON); a tool that hides its "
            "counts fails this leg even if its packet is correct.",
            "'Committed' expected.json baseline is checked as an existing, "
            "parseable file read by the exercise; git-trackedness is "
            "recorded, not required — workers never commit.",
            "The F 1:1 binding uses the receipt's index against the 192-row "
            "round-10 ledger; a receipt for a row whose ledger hash it "
            "cannot reproduce is rejected regardless of its own claims. "
            "Rows with no byte-comparable re-run (prose-only ledger rows, "
            "new_hash null) are bucketed as dispositioned unreproducible: "
            "excluded from the >=95% stability ratio and from the >=15 "
            "re-run count, but still required to carry a named cause.",
            "Unstable-row causes are read from drift_class/drift_cause or "
            "inferred from the cause text; the licensed vocabulary is "
            "legitimate change / environmental / defect plus the "
            "unreproducible-by-construction class for prose-only ledger "
            "rows.",
            "Calibration controls (disposable, untracked, 2026-10-17): "
            ".scratch/x03/make-fixture.py builds a hardlink/tar fixture "
            "whose synthetic round-11 evidence passes all three claims "
            "(exit 0), and .scratch/x03/controls.py plants 15 defects — an "
            "extra expected hold, a dropped owed form, a translated GAR "
            "label on the sound channel, a non-zero e2e exit, a missing "
            "re-pinned manifest, a stale typed projection, a 15/16 field "
            "count, an abandoned malformed control, an unshown gate "
            "reference, an absent baseline, a tampered ledger binding, "
            "undispositioned drift below the stability floor, an inflated "
            "summary count, a missing auditor artifact and a non-1:1 "
            "command — each was caught with exit 1 and the expected "
            "failure text. Scratch is not a deliverable and is not "
            "required for this runner to work.",
            "Author-side only: no admission, promotion or canon decision; "
            "this runner replaces no independent review.",
        ],
    }
    output = ROOT / OUTPUT_REL
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                 ensure_ascii=False) + "\n",
                      encoding="utf-8")
    for claim_id in ("D", "O", "F"):
        state = "PASS" if results[claim_id]["passed"] else "FAIL"
        print(f"claim {claim_id}: {state}")
        for failure in results[claim_id]["failures"]:
            print(f"  - {failure}")
    print(f"acceptance_checks_passed: {passed}")
    if not passed:
        print("missing_dependencies: " + ", ".join(missing))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
