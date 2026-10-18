#!/usr/bin/env python3
"""Round-24 acceptance runner: claims C (calibration), O (operability), D (depth).

Claim C — the four SHONEN promotion boxes independently verified by named
non-author reviewers, filed at reports/round-24/promotion-review.md:
  box 1 — SKILL.md decision tables / error patterns / checklists with cited
          sources (adversarial citation-resolving pass); this runner adds its
          own teeth: every repo-path citation in SKILL.md must resolve to an
          existing file with in-range line numbers;
  box 2 — end-to-end domain task chain D2->D3->D4->handoff executed and logged
          in LOG.md; this runner re-runs the fixed round-23 regression
          inventory (assemblers, gates, projector, handoff v2/v3), which
          exercises that chain, and requires the chain logged in LOG.md;
  box 3 — cold-run executability by a fresh-context seat (evidence from
          reports/round-24/cold-run.md or the cold-run*.md fragment set),
  box 4 — no cross-domain bleed; PROVINCE.md still accurate.
  Per box: verdict verified | verified-with-conditions (conditions named) |
  failed, at least one named reviewer, at least one resolvable evidence
  pointer (box 1 must cite SKILL.md, box 2 LOG.md, box 3 cold-run.md,
  box 4 PROVINCE.md), and at least two distinct reviewers across the dossier.
  The promotion DECISION stays operator-owned; this dossier is its evidence.

Claim O — reports/round-24/cold-run.md records the fresh-context cold run:
  >=2 distinct named seats, each with an executed command list (>=6 commands
  total); every invoked repo tool path exists; every recorded break/ambiguity
  is dispositioned either fixed-with-control (resolvable pointer + named
  control) or as a named box-3 condition; a no-breaks run must say so
  explicitly; conditions surfaced for box 3 must appear in promotion-review.md.

Claim D — reports/round-24/skill-audit.md audits every SKILL.md table row:
  every data row of every SKILL.md table is covered by an evidenced
  disposition (current | fixed | erratum); header and separator rows carry no
  executable claims and are excluded by declaration (counts recorded in the
  receipt); fixed rows name a control; erratum rows carry a date; a bare
  "stale" without fix or erratum is silent staleness and fails; if the audit
  pins a SKILL.md digest it must match the measured bytes.

Run only in an isolated Git clone under the lane's .scratch, as
  python3 reports/round-24/run-validation.py            (measure + write receipt)
  python3 reports/round-24/run-validation.py --check    (measure only, print)
  python3 reports/round-24/run-validation.py --selftest (dependency-free controls)
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import runpy
import shlex
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-24"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
COMMAND = f"python3 {RUNNER}"
REVIEW = f"{ROUND_DIR}/promotion-review.md"
COLD_RUN = f"{ROUND_DIR}/cold-run.md"
SKILL_AUDIT = f"{ROUND_DIR}/skill-audit.md"
SKILL = "SKILL.md"
LOG = "LOG.md"
PROVINCE = "PROVINCE.md"
SHONEN = "SHONEN.md"
SYNC_PATHS = (ROUND_DIR, SKILL, LOG, "SCORECARD.md", PROVINCE, SHONEN,
              "corpus", "examples", "tools")
PROTECTED = tuple(f"reports/round-{n}" for n in range(8, 24)) + tuple(
    f"tools/gates/frozen/round-{n}" for n in range(8, 24))
VERDICT_CANON = {"verified": "verified",
                 "verified-with-conditions": "verified-with-conditions",
                 "verified-with-condition": "verified-with-conditions",
                 "verified with conditions": "verified-with-conditions",
                 "failed": "failed", "fail": "failed"}
VERDICT_FIELD_RE = re.compile(
    r"(?i)\bverdict\s*[:=]\s*[`\"']*(verified[- ]with[- ]conditions?|verified|failed?)\b")
VERDICT_STANDALONE_RE = re.compile(
    r"(?im)^\s*(?:[-*+]\s+)?\**\s*(verified[- ]with[- ]conditions?|verified|failed?)\s*\**\s*(?:[:=\u2014-]|$)")
REVIEWER_RE = re.compile(
    r"(?i)\b(?:reviewers?|reviewed by|verifier|verified by|seat)\s*[:=]\s*"
    r"([A-Za-z0-9][\w./-]*(?:\s*[,/&+]\s*[A-Za-z0-9][\w./-]*){0,5})")
CONDITIONS_RE = re.compile(r"(?im)^\s*(?:[-*+]|\d+[.)])?\s*\**conditions?\**\s*[:=]\s*(\S[^\n]*)")
CONDITIONS_HEADING_RE = re.compile(r"(?im)^#{1,6}\s*\**conditions?\**\s*:?\s*\**\s*$")
BULLET_RE = re.compile(r"(?m)^\s*(?:[-*+]|\d+[.)])\s+")
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
HEX_RE = re.compile(r"\b(?=[0-9a-f]*\d)[0-9a-f]{7,64}(?:\u2026)?\b")
CITATION_RE = re.compile(
    r"(?<![\w./-])(?:(?:reports|tools|examples|corpus)/[\w./+-]+\.(?:json|md|py|ya?ml|tsv|txt|sh)"
    r"|\b(?:LOG|SKILL|SCORECARD|PROVINCE|README|SHONEN|MINT)\.md)(?::(\d+)(?:-(\d+))?)?")
REPO_PATH_RE = re.compile(
    r"(?<![\w./-])(?:reports|tools|examples|corpus)/[\w./+-]+\.(?:json|md|py|ya?ml|tsv|txt|sh)\b")
COMMAND_LINE_RE = re.compile(
    r"^\s*(?:\$\s+)?(?:python3?(?:\.\d+)?|sha256sum|git|diff|cmp|rg|grep|test|wc|date)\b")
INVOKED_TOOL_RE = re.compile(r"^\s*(?:\$\s+)?python3?(?:\.\d+)?\s+(\S+)")
SEAT_FIELD_RE = re.compile(
    r"(?im)^\s*(?:#{1,6}\s*)?(?:\*\*)?seat(?:[ -]?id)?(?:\*\*)?\s*[:=]\s*`?([A-Za-z0-9][\w ./-]{0,40})")
SEAT_HEAD_RE = re.compile(r"(?im)^#{1,6}[^\n]*\bseat[- ]([A-Za-z0-9][\w.-]*)")
BOX_HEAD_RE = re.compile(r"(?im)^#{1,6}[^\n]*\bbox\s*([1-4])\b[^\n]*$")
BOX_ROW_RE = re.compile(r"(?im)^\|[^\n]*\bbox\s*([1-4])\b[^\n]*$")
FINDING_INLINE_RE = re.compile(
    r"(?im)^\s*(?:[-*+]|\d+[.)])?\s*\**(?:[BF]-?\d{1,3}\b\s*\(|(?:break|finding|ambiguity|issue|defect)\b)")
FINDING_TABLE_RE = re.compile(r"(?m)^\|[^|\n]*\b[BF]-?\d{1,3}\b")
FIX_EVIDENCE_RE = re.compile(
    r"control|before ?/ ?after|(?:reports|tools)/[\w./-]*fixes?[\w./-]*|audit-fixes\.md")
NO_BREAKS_RE = re.compile(r"(?i)\bno (?:breaks|breaks or ambiguities|findings|break or ambiguity)\b")
DISPOSITION_CURRENT = ("current", "re-verified", "verified", "accurate", "holds", "still true")
DISPOSITION_FIXED = ("fixed", "fixed-with-control")
DISPOSITION_ERRATUM = ("erratum",)
DISPOSITION_RES = {name: tuple(re.compile(rf"(?<!\w){re.escape(token)}(?!\w)")
                               for token in tokens)
                   for name, tokens in (("current", DISPOSITION_CURRENT),
                                        ("fixed", DISPOSITION_FIXED),
                                        ("erratum", DISPOSITION_ERRATUM))}


def word_hit(low, group):
    return any(pattern.search(low) for pattern in DISPOSITION_RES[group])


def fix_ledger_ids(text):
    """Fix ids (F1, F2, ...) recorded in this document's own fix-ledger sections."""
    ids = set()
    for section in split_sections(text):
        head = section.splitlines()[0] if section else ""
        if re.search(r"(?i)\bfix", head):
            ids.update(re.findall(r"\bF\d+\b", section))
    return ids


LINE_REF_SINGLE_RE = re.compile(
    r"(?i)\bSKILL\.md\s*[:#]\s*(\d{1,4})\b|\bline\s*[:#]?\s*(\d{1,4})\b|\(\s*:\s*(\d{1,4})\s*\)")
LINE_REF_SKILL_RANGE_RE = re.compile(
    r"(?i)\bSKILL\.md\s*[:#]\s*(\d{1,4})\s*-\s*(\d{1,4})\b|\(\s*:\s*(\d{1,4})\s*-\s*(\d{1,4})\s*\)")
LINE_REF_BARE_RANGE_RE = re.compile(r"(?<![\d-])\b(\d{1,4})\s*-\s*(\d{1,4})\b(?![\d-])")
LINE_REF_CELL_RE = re.compile(r"(?:^|[|:#\s])(\d{1,4})(?=$|[|:#\s)])")
EVIDENCE_TOKEN_RE = re.compile(
    REPO_PATH_RE.pattern + r"|" + DATE_RE.pattern + r"|" + HEX_RE.pattern
    + r"|(?<![\w./-])[\w][\w.-]*\.(?:py|md|json|ya?ml|tsv|sh)\b|\bW-\d+\b")
REGRESSIONS = (
    ("battery-selftest", ("tools/check-gate-battery.py", "--selftest")),
    ("battery", ("tools/check-gate-battery.py",)),
    ("craft-selftest", ("tools/check-craft-exercise.py", "--selftest")),
    ("craft", ("tools/check-craft-exercise.py", "examples/supplement-opencode-1/sound-change-vs-taboo.json")),
    ("d2-assembly-selftest", ("tools/assemble-d2.py", "--selftest")),
    ("d2-assembly", ("tools/assemble-d2.py", "--check")),
    ("d2-adapter-selftest", ("tools/assemble-d2-typed.py", "--selftest")),
    ("d2-adapter", ("tools/assemble-d2-typed.py", "--check")),
    ("d3-assembly-selftest", ("tools/assemble-culture-d3.py", "--selftest")),
    ("d3-assembly", ("tools/assemble-culture-d3.py", "--check")),
    ("d4-assembly-selftest", ("tools/assemble-culture-d4.py", "--selftest")),
    ("d4-assembly", ("tools/assemble-culture-d4.py", "--check")),
    ("d4-adapter-selftest", ("tools/assemble-d4-typed.py", "--selftest")),
    ("d4-adapter", ("tools/assemble-d4-typed.py", "--check")),
    ("projector-selftest", ("tools/d2-typed-labels.py", "--selftest")),
    ("d2-projection", ("tools/d2-typed-labels.py", "--check")),
    ("d4-projection", ("tools/d2-typed-labels.py", "--packet", "examples/culture-d4/packet.d4.yml",
                       "--check", "examples/culture-d4/typed-labels.d4.yml")),
    ("typed-pipeline-selftest", ("tools/gates/typed-pipeline-gate.py", "--selftest")),
    ("typed-pipeline-generalized-selftest", ("tools/gates/typed-pipeline-gate.py", "--selftest-generalized")),
    ("d2-gate", ("tools/gates/typed-pipeline-gate.py",)),
    ("d4-gate", ("tools/gates/typed-pipeline-gate.py", "examples/culture-d4/packet.d4.yml")),
    ("d4-label-gate", ("tools/gates/d4-typed-labels-check-gate.py",)),
    ("d4-assembly-gate", ("tools/gates/d4-assembly-check-gate.py",)),
    ("coupling-selftest", ("tools/check-evidence-coupling.py", "--selftest")),
    ("replay-selftest", ("tools/replay-frozen.py", "--selftest")),
    ("handoff-v2", ("tools/exercise-handoff-e2e.py", "--profile", "v2", "--quiet")),
    ("handoff-v3-selftest", ("tools/exercise-handoff-e2e.py", "--profile", "v3", "--selftest")),
    ("handoff-v3", ("tools/exercise-handoff-e2e.py", "--profile", "v3", "--quiet")),
)
MIN_COLD_COMMANDS = 6
MIN_COLD_SEATS = 2
MIN_REVIEWERS = 2


def today():
    return dt.date.today().isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def metric(value, operation):
    return {"value": value, "command": f"{COMMAND} ({operation})", "date": today()}


def safe_path(relative):
    if not isinstance(relative, str) or not relative:
        raise ValueError("evidence path must be a nonempty string")
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or ".git" in path.parts:
        raise ValueError(f"not an in-repository path: {relative}")
    resolved = ROOT / path
    for ancestor in (resolved, *resolved.parents):
        if ancestor == ROOT:
            break
        if ancestor.is_symlink():
            raise ValueError(f"symlink evidence path refused: {relative}")
    if not resolved.resolve().is_relative_to(ROOT):
        raise ValueError(f"evidence path escapes repository: {relative}")
    return resolved


def strict_json(text):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(text, object_pairs_hook=pairs)


class Evidence:
    def __init__(self):
        self.inputs = {}
        self.missing = set()
        self.errors = []

    def text(self, relative):
        try:
            data = safe_path(relative).read_bytes()
            self.inputs[relative] = sha(data)
            return data.decode("utf-8")
        except (OSError, UnicodeError, ValueError) as error:
            self.missing.add(relative)
            self.errors.append(f"{relative}: {error}")
            return ""

    def document(self, relative):
        text = self.text(relative)
        try:
            return strict_json(text) if text else None
        except (ValueError, TypeError) as error:
            self.errors.append(f"{relative}: {error}")
            return None


def result(failures, measurement, missing=()):
    return {"passed": not failures, "failures": failures,
            "measurement": measurement, "missing_dependencies": sorted(set(missing))}


def git(*argv, timeout=120, cwd=None):
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1")
    try:
        proc = subprocess.run(["git", *argv], cwd=cwd or ROOT, capture_output=True,
                              timeout=timeout, env=env)
        return proc.stdout if proc.returncode == 0 else None
    except (OSError, subprocess.SubprocessError):
        return None


def live_lane():
    """The real lane root: nearest ancestor without a .scratch path component."""
    for ancestor in (ROOT, *ROOT.parents):
        if ".scratch" in ancestor.parts:
            continue
        if (ancestor / ".git").is_dir() and (ancestor / f"{ROUND_DIR}/claims.json").is_file():
            return ancestor
    return None


def protected_baseline(revision):
    failures, rows = [], []
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-f]{40,64}", revision):
        return result(["Round-24 declared baseline is not a full Git revision"], {})
    raw = git("ls-tree", "-r", "-z", revision, "--", *PROTECTED)
    if raw is None:
        return result([f"Cannot inspect protected baseline {revision}"], {})
    expected = {}
    for entry in raw.split(b"\0"):
        if not entry:
            continue
        metadata, name = entry.split(b"\t", 1)
        mode, kind, oid = metadata.decode("ascii").split()
        if kind != "blob" or mode not in ("100644", "100755"):
            failures.append(f"Protected baseline has a nonregular entry: {os.fsdecode(name)}")
        expected[os.fsdecode(name)] = oid
    extra = git("status", "--porcelain=v1", "--untracked-files=all", "--", *PROTECTED)
    worktree = [line for line in (extra or b"").decode("utf-8", "replace").splitlines()
                if line.strip()]
    for relative in sorted(expected):
        path = ROOT / relative
        data = None
        if path.is_file():
            try:
                data = path.read_bytes()
            except OSError:
                data = None
        if data is None:
            rows.append({"path": relative, "baseline_blob": expected[relative],
                         "observed_blob": None})
            continue
        blob = git_blob_sha(data)
        if blob != expected[relative]:
            rows.append({"path": relative, "baseline_blob": expected[relative],
                         "observed_blob": sha(data)})
    for line in worktree:
        flag, _, path = line.partition(" ")
        if flag == "??" and path.strip():
            rows.append({"path": path.strip(), "baseline_blob": None, "observed_blob": "untracked"})
    if rows:
        failures.append("Filed rounds 8-23 or their frozen generations differ from the declared baseline")
    return result(failures, {"baseline_revision": revision,
                             "protected_paths": metric(len(expected), "git ls-tree of protected baseline"),
                             "differences": rows[:20],
                             "differences_total": metric(len(rows), "compare protected Git blobs to working bytes"),
                             "protected_status_rows": metric(len(worktree), "git status over protected paths")})


def run_command(label, parts, timeout=900):
    scratch = ROOT / ".scratch" / "round-24" / "validation" / label
    scratch.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "TMPDIR": str(scratch), "PYTHONDONTWRITEBYTECODE": "1",
           "GIT_OPTIONAL_LOCKS": "0"}
    item = {"label": label, "command": shlex.join(["python3", *parts]),
            "argv": ["python3", *parts], "date": today()}
    try:
        item["tool_sha256"] = sha(safe_path(parts[0]).read_bytes())
        proc = subprocess.run([sys.executable, *parts], cwd=ROOT, capture_output=True,
                              timeout=timeout, env=env)
        item.update(exit=proc.returncode, stdout=proc.stdout.decode("utf-8", "replace"),
                    stderr=proc.stderr.decode("utf-8", "replace"),
                    stdout_sha256=sha(proc.stdout), stderr_sha256=sha(proc.stderr))
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        item.update(exit=None, error=str(error), timeout=isinstance(error, subprocess.TimeoutExpired))
    return item


def run_receipt(item):
    return {key: (value[-7000:] if key == "stdout" else value[-2000:]
                  if key == "stderr" else value) for key, value in item.items()}


def measure_regressions():
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        items = list(pool.map(lambda pair: run_command(*pair), REGRESSIONS))
    failures = [f"Regression failed: {item['command']} (exit {item.get('exit')}, {item['date']})"
                for item in items if item.get("exit") != 0]
    measurement = {"runs_total": metric(len(items), "fixed regression command inventory"),
                   "labels": {item["label"]: {"exit": item.get("exit"), "command": item["command"],
                                              "date": item["date"]} for item in items},
                   "runs": [run_receipt(item) for item in items]}
    return result(failures, measurement)


def citation_problems(text, read_line_count):
    """Every repo-path citation must resolve to an existing file with in-range lines."""
    problems = []
    resolved = 0
    for match in CITATION_RE.finditer(text):
        relative = match.group(0).split(":")[0]
        try:
            path = safe_path(relative)
        except ValueError as error:
            problems.append(f"unsafe citation {match.group(0)}: {error}")
            continue
        if not path.is_file():
            problems.append(f"citation does not resolve: {match.group(0)}")
            continue
        low, high = match.group(1), match.group(2)
        if low:
            limit = read_line_count.get(relative)
            if limit is None:
                try:
                    limit = len(path.read_bytes().decode("utf-8", "replace").splitlines())
                    read_line_count[relative] = limit
                except OSError:
                    limit = None
            if limit is not None and int(low) > limit:
                problems.append(f"citation line out of range: {match.group(0)} (file has {limit} lines)")
        resolved += 1
    return resolved, problems


def parse_conditions(text):
    named = [match.group(1).strip() for match in CONDITIONS_RE.finditer(text)]
    heading = CONDITIONS_HEADING_RE.search(text)
    if heading:
        tail = text[heading.end():]
        next_heading = re.search(r"(?m)^#{1,6}\s", tail)
        block = tail[:next_heading.start()] if next_heading else tail
        for item in re.split(r"(?m)^(?:[-*+]|\d+[.)])\s+", block):
            item = item.strip()
            if item and not item.startswith("#"):
                named.append(item.splitlines()[0])
    return [item for item in named if item]


def canon_verdict(raw):
    return VERDICT_CANON.get(raw.strip().lower().replace(" ", "-").replace("—", "-"))


def parse_promotion_review(text):
    """Box sections from headings, plus any table row naming the box."""
    boxes = {str(n): {"sections": []} for n in range(1, 5)}
    heads = sorted(BOX_HEAD_RE.finditer(text), key=lambda m: m.start())
    for index, match in enumerate(heads):
        box = match.group(1)
        end = heads[index + 1].start() if index + 1 < len(heads) else len(text)
        boxes[box]["sections"].append(text[match.end():end])
    for row in BOX_ROW_RE.finditer(text):
        boxes[row.group(1)]["sections"].append(row.group(0))
    parsed = {}
    for box, payload in boxes.items():
        body = "\n".join(payload["sections"])
        verdict = None
        for match in VERDICT_FIELD_RE.finditer(body):
            verdict = canon_verdict(match.group(1))
            if verdict:
                break
        if verdict is None:
            for match in VERDICT_STANDALONE_RE.finditer(body):
                verdict = canon_verdict(match.group(1))
                if verdict:
                    break
        reviewers = sorted({name.strip(" `*") for match in REVIEWER_RE.finditer(body)
                            for name in [match.group(1)] if name.strip(" `*")})
        conditions = parse_conditions(body)
        pointers = [match.group(0) for match in CITATION_RE.finditer(body)]
        parsed[box] = {"verdict": verdict, "reviewers": reviewers,
                       "conditions": conditions[:10], "evidence_pointers": sorted(set(pointers))[:12]}
    return parsed


def review_problems(parsed, read_line_count):
    failures = []
    box_anchors = {"1": "SKILL.md", "2": "LOG.md",
                   "3": "reports/round-24/cold-run", "4": PROVINCE}
    reviewers = set()
    for box in ("1", "2", "3", "4"):
        entry = parsed.get(box) or {}
        verdict = entry.get("verdict")
        if verdict is None:
            failures.append(f"box {box}: no verdict in the allowed vocabulary "
                            "(verified | verified-with-conditions | failed)")
        if verdict == "verified-with-conditions" and not entry.get("conditions"):
            failures.append(f"box {box}: verified-with-conditions without named conditions")
        if not entry.get("reviewers"):
            failures.append(f"box {box}: no named reviewer")
        reviewers.update(entry.get("reviewers") or [])
        anchors = {token.split(":")[0] for token in entry.get("evidence_pointers") or []}
        anchor = box_anchors[box]
        if not any(name.startswith(anchor) for name in anchors):
            failures.append(f"box {box}: evidence does not cite {anchor}")
        resolved, problems = citation_problems("\n".join(entry.get("evidence_pointers") or []),
                                               read_line_count)
        failures.extend(f"box {box}: {problem}" for problem in problems)
    if len(reviewers) < MIN_REVIEWERS:
        failures.append(f"independent verification needs >= {MIN_REVIEWERS} distinct named "
                        f"reviewers across the dossier; found {sorted(reviewers)}")
    return failures, reviewers


def skill_citations_problems(skill_text, read_line_count):
    resolved, problems = citation_problems(skill_text, read_line_count)
    return {"resolved": metric(resolved, "repo-path citations resolved in SKILL.md"),
            "problems": problems[:30], "problems_total": metric(len(problems), "unresolved SKILL.md citations")}


def extract_commands(text):
    """Commands from fenced blocks, shell-prompt lines, indented lines and
    backtick spans (the lane records execution logs as table cells)."""
    commands = []
    in_fence = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        in_command_context = in_fence or stripped.startswith("$ ") or re.match(r"^\s{2,}\S", line)
        if in_command_context and COMMAND_LINE_RE.match(stripped.lstrip("$ ")):
            commands.append(stripped.lstrip("$ ").strip())
        for span in re.findall(r"`([^`\n]+)`", line):
            span = span.strip().lstrip("$ ").strip()
            if COMMAND_LINE_RE.match(span):
                commands.append(span)
    deduped = []
    for command in commands:
        if command not in deduped:
            deduped.append(command)
    return deduped


def split_sections(text):
    sections, current = [], []
    for line in text.splitlines():
        if re.match(r"^#{1,6}\s", line):
            if current:
                sections.append("\n".join(current))
            current = [line]
        else:
            current.append(line)
    if current:
        sections.append("\n".join(current))
    return sections


def parse_cold_run(text):
    seats = set()
    for match in SEAT_FIELD_RE.finditer(text):
        seats.add(re.sub(r"\s+", "-", match.group(1).strip(" `*").lower()))
    for match in SEAT_HEAD_RE.finditer(text):
        seats.add(match.group(1).strip(" `*").lower())
    seats.discard("")
    commands = extract_commands(text)
    missing_tools = []
    for command in commands:
        tool = INVOKED_TOOL_RE.match(command)
        if not tool:
            continue
        target = tool.group(1).strip("`\"'")
        if not (target.startswith("reports/") or target.startswith("tools/")
                or target.startswith("examples/") or target.startswith("corpus/")
                or target.endswith((".py", ".md", ".json", ".yml", ".tsv", ".sh"))):
            continue
        try:
            if not safe_path(target).is_file():
                missing_tools.append({"command": command, "tool": target})
        except ValueError:
            missing_tools.append({"command": command, "tool": target})
    no_breaks_declared = bool(NO_BREAKS_RE.search(text))
    findings, undispositioned, conditions = 0, [], []
    for section in split_sections(text):
        paragraphs = [par for par in re.split(r"\n\s*\n", section) if par.strip()]
        finding_pars = [par for par in paragraphs
                        if FINDING_INLINE_RE.search(par) or FINDING_TABLE_RE.search(par)]
        if not finding_pars:
            continue
        findings += len(finding_pars)
        low = section.lower()
        fixed_ctrl = ("fixed-with-control" in low
                      or (("fixed" in low or "fix " in low) and FIX_EVIDENCE_RE.search(section)))
        conditioned = "condition" in low
        if fixed_ctrl and not REPO_PATH_RE.search(section):
            undispositioned.append(f"fixed-with-control without a resolvable pointer: "
                                   f"{finding_pars[0][:80]!r}")
        elif conditioned:
            conditions.extend(par.strip().splitlines()[0] for par in finding_pars)
        elif not (fixed_ctrl or no_breaks_declared):
            undispositioned.append(f"undispositioned break/ambiguity: "
                                   f"{finding_pars[0][:80]!r}")
    for line in text.splitlines():
        if "condition" in line.lower() and len(line.strip()) > 12:
            conditions.append(line.strip())
    deduped_conditions = []
    for item in conditions:
        if item not in deduped_conditions:
            deduped_conditions.append(item)
    return {"seats": sorted(seats), "commands": commands, "missing_tools": missing_tools,
            "findings_total": findings, "undispositioned": undispositioned[:10],
            "conditions": deduped_conditions[:10], "no_breaks_declared": no_breaks_declared}


def cold_run_problems(parsed):
    failures = []
    if len(parsed["seats"]) < MIN_COLD_SEATS:
        failures.append(f"cold run needs >= {MIN_COLD_SEATS} distinct named fresh-context seats; "
                        f"found {parsed['seats']}")
    if len(parsed["commands"]) < MIN_COLD_COMMANDS:
        failures.append(f"cold run records only {len(parsed['commands'])} executed commands; "
                        f"an end-to-end checklist execution needs >= {MIN_COLD_COMMANDS}")
    for entry in parsed["missing_tools"]:
        failures.append(f"cold-run command invokes a repo tool that does not exist: "
                        f"{entry['tool']} ({entry['command']})")
    failures.extend(parsed["undispositioned"])
    if parsed["findings_total"] == 0 and not parsed["no_breaks_declared"]:
        failures.append("cold run reports no findings and never declares an explicit no-breaks run")
    return failures


def skill_table_rows(skill_lines):
    """Data rows of every SKILL.md table; header rows and separators excluded by declaration."""
    data, headers, separators = [], [], []
    awaiting_header = True
    for number, line in enumerate(skill_lines, start=1):
        if not line.lstrip().startswith("|"):
            awaiting_header = True
            continue
        body = line.strip().strip("|")
        cells = [cell.strip() for cell in body.split("|")]
        if cells and all(re.fullmatch(r"[:\-\s]*", cell) for cell in cells):
            separators.append(number)
            continue
        if awaiting_header:
            headers.append(number)
            awaiting_header = False
            continue
        data.append(number)
    return data, headers, separators


def logical_lines(text):
    """Markdown logical lines: bullets keep their hard-wrapped continuation lines."""
    current = None
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            if current is not None:
                yield current
                current = None
            continue
        is_bullet_start = bool(re.match(r"(?:[-*+]|\d+[.)])\s", stripped))
        is_struct = stripped.startswith(("|", "#", "```"))
        if is_bullet_start or is_struct or current is None:
            if current is not None:
                yield current
            current = stripped
        else:
            current += " " + stripped
    if current is not None:
        yield current


def parse_skill_audit(text, skill_lines_total, skill_lines=None):
    ledger = fix_ledger_ids(text)
    covered, stale_fixed, errata, silent_stale, unevidenced = set(), [], [], [], []
    for logical in logical_lines(text):
        stripped = logical
        low = stripped.lower()
        in_table = stripped.startswith("|")
        is_bullet = bool(re.match(r"(?:[-*+]|\d+[.)])\s", stripped))
        numbers = set()
        for match in LINE_REF_SINGLE_RE.finditer(stripped):
            numbers.add(int(match.group(1) or match.group(2) or match.group(3)))
        if in_table:
            for match in LINE_REF_SKILL_RANGE_RE.finditer(stripped):
                low_n = int(match.group(1) or match.group(3))
                high_n = int(match.group(2) or match.group(4))
                if 1 <= low_n <= high_n <= low_n + 120:
                    numbers.update(range(low_n, high_n + 1))
            for match in LINE_REF_BARE_RANGE_RE.finditer(stripped):
                low_n, high_n = int(match.group(1)), int(match.group(2))
                if 1 <= low_n <= high_n <= low_n + 120:
                    numbers.update(range(low_n, high_n + 1))
            numbers.update(int(match.group(1)) for match in LINE_REF_CELL_RE.finditer(stripped))
        has_current = word_hit(low, "current")
        has_fixed = word_hit(low, "fixed")
        has_erratum = word_hit(low, "erratum")
        has_stale = bool(re.search(r"(?<!\w)STALE(?!\w)", stripped))
        evidencd = bool(EVIDENCE_TOKEN_RE.search(stripped))
        dispositioned = has_current or has_fixed or has_erratum
        audit_row = in_table or is_bullet
        if audit_row and has_stale and not (has_fixed or has_erratum):
            silent_stale.append(stripped[:100])
        if in_table and has_fixed:
            ids = set(re.findall(r"\bF-?\d+\b", stripped))
            named = bool(FIX_EVIDENCE_RE.search(stripped)) or bool(ids and ids & ledger)
            if not named:
                stale_fixed.append(stripped[:100])
        if audit_row and has_erratum and not (has_current or has_fixed):
            dated_in_row = bool(DATE_RE.search(stripped))
            if not dated_in_row and skill_lines is not None:
                dated_in_row = any(
                    int(match.group(1)) <= len(skill_lines)
                    and DATE_RE.search(skill_lines[int(match.group(1)) - 1])
                    for match in LINE_REF_SINGLE_RE.finditer(stripped)
                    if match.group(1))
            if not dated_in_row:
                errata.append(stripped[:100])
        if in_table and dispositioned and not evidencd:
            unevidenced.append(stripped[:100])
        if dispositioned and evidencd:
            covered.update(n for n in numbers if 1 <= n <= skill_lines_total)
    return {"covered": covered, "stale_fixed_rows": stale_fixed[:12],
            "undated_errata": errata[:12], "silent_stale": silent_stale[:12],
            "unevidenced_rows": unevidenced[:12]}


def audit_pin(text):
    for match in re.finditer(r"(?i)SKILL\.md[^`\n]{0,40}?`?([0-9a-f]{64})`?", text):
        return match.group(1)
    return None


def measure_calibration(evidence, regressions):
    failures, missing = [], []
    measurement = {}
    review_text = evidence.text(REVIEW)
    if not review_text:
        failures.append(f"promotion dossier missing: {REVIEW}")
        missing.append(REVIEW)
        return result(failures, measurement, missing)
    read_line_count = {}
    parsed = parse_promotion_review(review_text)
    measurement["boxes"] = parsed
    review_failures, reviewers = review_problems(parsed, read_line_count)
    failures.extend(review_failures)
    skill_text = evidence.text(SKILL)
    if not skill_text:
        failures.append(f"{SKILL} unreadable")
        missing.append(SKILL)
        return result(failures, measurement, missing)
    citations = skill_citations_problems(skill_text, read_line_count)
    measurement["box1_skill_citations"] = citations
    failures.extend(f"box 1: SKILL.md citation fails to resolve: {problem}"
                    for problem in citations["problems"])
    chain_failures = list(regressions["failures"])
    measurement["box2_chain_rerun"] = {
        "runs_total": regressions["measurement"]["runs_total"],
        "failures": chain_failures,
        "handoff": {label: regressions["measurement"]["labels"].get(label)
                    for label in ("handoff-v2", "handoff-v3", "d2-gate", "d4-gate")},
    }
    chain_failures = [f"box 2: {failure}" for failure in chain_failures]
    failures.extend(chain_failures)
    log_text = evidence.text(LOG)
    if not log_text:
        failures.append("box 2: LOG.md unreadable")
        missing.append(LOG)
    else:
        chain_logged = all(token in log_text for token in ("culture-d2", "culture-d4", "handoff"))
        measurement["box2_chain_logged"] = metric(chain_logged, "D2/D4/handoff logged in LOG.md")
        if not chain_logged:
            failures.append("box 2: the D2->D3->D4->handoff chain is not logged in LOG.md")
    province_text = evidence.text(PROVINCE)
    if not province_text:
        failures.append("box 4: PROVINCE.md unreadable")
        missing.append(PROVINCE)
    else:
        province_pointers = REPO_PATH_RE.findall(province_text)
        unresolved = []
        for relative in sorted(set(province_pointers)):
            try:
                if not safe_path(relative).is_file():
                    unresolved.append(relative)
            except ValueError:
                unresolved.append(relative)
        measurement["box4_province_pointers"] = {
            "total": metric(len(set(province_pointers)), "repo paths named in PROVINCE.md"),
            "unresolved": unresolved[:10]}
        if unresolved:
            failures.append(f"box 4: PROVINCE.md names paths that do not resolve: {unresolved[:5]}")
    measurement["distinct_reviewers"] = metric(len(reviewers), "distinct named non-author reviewers")
    return result(failures, measurement, missing)


def measure_operability(evidence, regressions, review_boxes):
    failures, missing = [], []
    measurement = {"regressions": {
        "runs_total": regressions["measurement"]["runs_total"],
        "failures": regressions["failures"],
        "labels": regressions["measurement"]["labels"]}}
    failures.extend(f"chain: {failure}" for failure in regressions["failures"])
    cold_text = evidence.text(COLD_RUN)
    if not cold_text:
        failures.append(f"cold-run report missing: {COLD_RUN}")
        missing.append(COLD_RUN)
        return result(failures, measurement, missing)
    parsed = parse_cold_run(cold_text)
    measurement["cold_run"] = {"seats": parsed["seats"],
                               "commands_total": metric(len(parsed["commands"]), "executed cold-run commands"),
                               "commands": parsed["commands"][:40],
                               "missing_tools": parsed["missing_tools"][:10],
                               "findings_total": metric(parsed["findings_total"], "recorded breaks/ambiguities"),
                               "no_breaks_declared": parsed["no_breaks_declared"],
                               "conditions": parsed["conditions"]}
    failures.extend(cold_run_problems(parsed))
    box3 = (review_boxes or {}).get("3") or {}
    conditions = parsed["conditions"]
    if conditions and box3.get("verdict") == "verified":
        failures.append("cold run names box-3 conditions but promotion-review box 3 is verified "
                        "without conditions")
    if conditions and not box3.get("conditions"):
        failures.append("cold run names box-3 conditions that are absent from promotion-review box 3")
    return result(failures, measurement, missing)


def measure_depth(evidence):
    failures, missing = [], []
    measurement = {}
    audit_text = evidence.text(SKILL_AUDIT)
    if not audit_text:
        failures.append(f"SKILL staleness audit missing: {SKILL_AUDIT}")
        missing.append(SKILL_AUDIT)
        return result(failures, measurement, missing)
    skill_text = evidence.text(SKILL)
    if not skill_text:
        failures.append(f"{SKILL} unreadable")
        missing.append(SKILL)
        return result(failures, measurement, missing)
    skill_lines = skill_text.splitlines()
    data, headers, separators = skill_table_rows(skill_lines)
    measurement["skill_rows"] = {
        "data_rows": metric(len(data), "SKILL.md table data rows"),
        "header_rows_excluded": metric(len(headers), "SKILL.md table header rows excluded by declaration"),
        "separator_rows_excluded": metric(len(separators), "SKILL.md table separator rows excluded by declaration")}
    fragment_paths = sorted(str(path.relative_to(ROOT))
                            for path in (ROOT / ROUND_DIR).glob("audit-*.md") if path.is_file())
    covered, silent_stale, stale_fixed, errata, unevidenced = set(), [], [], [], []
    audit_sources = {SKILL_AUDIT: audit_text}
    for relative in fragment_paths:
        text = evidence.text(relative)
        if text:
            audit_sources[relative] = text
    for relative, text in sorted(audit_sources.items()):
        parsed = parse_skill_audit(text, len(skill_lines), skill_lines)
        covered |= parsed["covered"]
        silent_stale.extend(f"{relative}: {row}" for row in parsed["silent_stale"])
        stale_fixed.extend(f"{relative}: {row}" for row in parsed["stale_fixed_rows"])
        errata.extend(f"{relative}: {row}" for row in parsed["undated_errata"])
        unevidenced.extend(f"{relative}: {row}" for row in parsed["unevidenced_rows"])
    measurement["audit"] = {"sources": sorted(audit_sources),
                            "data_rows_covered": metric(len(set(data) & covered), "audit coverage over data rows"),
                            "uncovered_total": metric(len(set(data) - covered), "data rows with no evidenced disposition"),
                            "uncovered_first": sorted(set(data) - covered)[:12],
                            "stale_fixed_rows": stale_fixed[:12],
                            "undated_errata": errata[:12],
                            "silent_stale": silent_stale[:12],
                            "unevidenced_rows": unevidenced[:12]}
    uncovered = sorted(set(data) - covered)
    if uncovered:
        failures.append(f"zero silent staleness violated: {len(uncovered)} SKILL.md data rows have "
                        f"no per-row evidenced disposition reference in the audit set (sections may "
                        f"carry aggregate verdicts; first uncovered rows: {uncovered[:12]})")
    failures.extend(f"silent staleness: audit row says stale without fix or erratum: {row!r}"
                    for row in silent_stale)
    failures.extend(f"fixed audit row without a named control: {row!r}"
                    for row in stale_fixed)
    failures.extend(f"erratum audit row without a date: {row!r}" for row in errata)
    failures.extend(f"audit row carries a disposition but no evidence pointer/date/digest: {row!r}"
                    for row in unevidenced)
    pin = audit_pin(audit_text)
    if pin is not None:
        observed = sha(skill_text.encode("utf-8"))
        measurement["audit"]["skill_pin"] = {"expected": pin, "observed": observed,
                                             "matches": pin == observed}
        if pin != observed:
            failures.append("skill-audit pins a SKILL.md digest that does not match the measured bytes")
    else:
        measurement["audit"]["skill_pin"] = None
    return result(failures, measurement, missing)


def copy_into_clone(live, relative, target_root):
    source = live / relative
    if not source.exists():
        return False
    destination = target_root / relative
    if source.is_dir():
        shutil.copytree(source, destination, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns(".scratch", "__pycache__"))
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    return True


def sync_round_surface(live):
    synced = {}
    for relative in SYNC_PATHS:
        source = live / relative
        if not source.exists():
            continue
        if source.is_dir():
            for child in sorted(source.iterdir()):
                if child.name in ("validation.json", ".scratch", "__pycache__"):
                    continue
                copy_into_clone(live, f"{relative}/{child.name}", ROOT)
        else:
            copy_into_clone(live, relative, ROOT)
        synced[relative] = sha(source.read_bytes()) if source.is_file() else "tree"
    return synced


def selftest():
    controls = []

    def check(name, passed, **details):
        controls.append({"control": name, "passed": bool(passed), **details})

    for raw, canon in (("verified", "verified"), ("Verified", "verified"),
                       ("verified-with-conditions", "verified-with-conditions"),
                       ("verified with conditions", "verified-with-conditions"),
                       ("failed", "failed"), ("fail", "failed")):
        check(f"verdict-canon-{raw.replace(' ', '-')}", canon_verdict(raw) == canon)
    check("verdict-canon-rejects", canon_verdict("seems fine") is None)

    good_review = (
        "# Promotion review\n\n## Box 1 — SKILL craft\nverdict: verified\n"
        "reviewer: C-R1 (round-24 seat)\nevidence: SKILL.md:20-30; reports/round-24/box1-craft.md\n\n"
        "## Box 2 — chain\nverdict: verified\nreviewer: C-R2\nevidence: LOG.md; "
        "reports/round-24/box2-chain.md\n\n"
        "## Box 3 — cold run\nverdict: verified-with-conditions\nconditions: the C-gate CLI lacks "
        "a --json mode; named as a condition\nreviewer: C-R1\nevidence: reports/round-24/cold-run.md\n\n"
        "## Box 4 — province\nverdict: verified\nreviewer: C-R2\nevidence: PROVINCE.md; "
        "reports/round-24/box4-province.md\n")
    parsed = parse_promotion_review(good_review)
    check("review-parses-4-boxes", sorted(parsed) == ["1", "2", "3", "4"])
    check("review-verdicts", all(parsed[str(n)]["verdict"] for n in range(1, 5)),
          verdicts={box: entry["verdict"] for box, entry in parsed.items()})
    check("review-reviewers", all(parsed[str(n)]["reviewers"] for n in range(1, 5)))
    check("review-conditions-required-satisfied",
          parsed["3"]["verdict"] == "verified-with-conditions" and parsed["3"]["conditions"])
    anchors = {box: [token.split(":")[0] for token in entry["evidence_pointers"]]
               for box, entry in parsed.items()}
    check("review-anchors", "SKILL.md" in anchors["1"] and "LOG.md" in anchors["2"]
          and "reports/round-24/cold-run.md" in anchors["3"] and "PROVINCE.md" in anchors["4"],
          anchors=anchors)
    bad_review = good_review.replace("conditions: the C-gate CLI lacks a --json mode; named as a condition\n", "")
    parsed_bad = parse_promotion_review(bad_review)
    failures, _ = review_problems(parsed_bad, {})
    check("review-conditions-required-detected",
          any("without named conditions" in failure for failure in failures), failures=failures[:4])
    parsed_solo = parse_promotion_review(good_review.replace("reviewer: C-R2", "reviewer: C-R1"))
    failures_solo, reviewers_solo = review_problems(parsed_solo, {})
    check("review-single-reviewer-detected",
          any("distinct named reviewers" in failure for failure in failures_solo)
          and len(reviewers_solo) == 1)

    cold_good = (
        "# Cold run\n\n## seat C-O1\nseat: C-O1\ncommands:\n```\n"
        "python3 tools/check-gate-battery.py\npython3 tools/exercise-handoff-e2e.py --profile v2 --quiet\n"
        "sha256sum SKILL.md\n```\nno findings.\n\n## seat C-O2\nseat: C-O2\ncommands:\n```\n"
        "python3 tools/assemble-culture-d4.py --check\npython3 tools/d2-typed-labels.py --selftest\n"
        "git status --porcelain\n```\n")
    cold = parse_cold_run(cold_good)
    problems = cold_run_problems(cold)
    check("cold-seats-and-commands", len(cold["seats"]) == 2 and len(cold["commands"]) == 6
          and not problems, seats=cold["seats"], problems=problems)
    cold_bad = cold_good.replace("python3 tools/assemble-culture-d4.py --check\n", "")
    cold_bad = cold_bad.replace("python3 tools/d2-typed-labels.py --selftest\n",
                                "python3 tools/nonexistent-gate.py --selftest\n")
    cold = parse_cold_run(cold_bad)
    problems = cold_run_problems(cold)
    check("cold-missing-tool-detected", any("does not exist" in p for p in problems), problems=problems)
    cold_few = parse_cold_run(cold_good.replace("python3 tools/check-gate-battery.py\n", "")
                              .replace("python3 tools/exercise-handoff-e2e.py --profile v2 --quiet\n", ""))
    check("cold-command-floor", any("executed commands" in p for p in cold_run_problems(cold_few)))
    cold_break = ("# Cold run\n\nseat: C-O1\nseat: C-O2\n\n- finding: the checklist item has no tool\n\n"
                  "fixed-with-control: added tools/check-x.py; control is its --selftest (reports/round-24/fixes/f1.md)\n")
    parsed_break = parse_cold_run(cold_break)
    check("cold-break-dispositioned", parsed_break["findings_total"] == 1
          and not parsed_break["undispositioned"])
    cold_open = ("# Cold run\n\nseat: C-O1\nseat: C-O2\n\n- finding: step 4 is ambiguous\n\nno disposition here\n")
    parsed_open = parse_cold_run(cold_open)
    check("cold-undispositioned-detected", any("undispositioned" in p
                                               for p in cold_run_problems(parsed_open)))
    parsed_none = parse_cold_run(cold_good)
    check("cold-no-breaks-declared", parsed_none["findings_total"] == 0
          and parsed_none["no_breaks_declared"] and not cold_run_problems(parsed_none),
          problems=cold_run_problems(parsed_none))
    cold_table = ("# Cold run\n\nSeat: executor A, round 24.\n\n| Step | Command | Exit |\n|---|---|---|\n"
                  "| E1 | `python3 tools/gates/provenance-audit.py --selftest` | 0 |\n"
                  "| E2 | `python3 tools/source-audit-inventory.py --root corpus/knowledge` | 0 |\n"
                  "| E3 | `python3 tools/gates/handoff-packet-check.py --selftest` | 0 |\n"
                  "| E4 | `grep -rln \"typological basis\" tools/` | 1 |\n"
                  "no findings.\n")
    cold = parse_cold_run(cold_table)
    check("cold-table-commands", len(cold["commands"]) == 4 and not cold["missing_tools"],
          commands=cold["commands"][:6], missing=cold["missing_tools"])
    cold_silent = "# Cold run\n\nseat: C-O1\nseat: C-O2\ncommands:\n```\npython3 tools/replay-frozen.py --selftest\npython3 tools/replay-frozen.py --selftest\npython3 tools/replay-frozen.py --selftest\npython3 tools/replay-frozen.py --selftest\npython3 tools/replay-frozen.py --selftest\npython3 tools/replay-frozen.py --selftest\n```\n"
    check("cold-silent-run-detected",
          any("no findings" in p for p in cold_run_problems(parse_cold_run(cold_silent))))

    rows = ["## T", "| A | B |", "|---|---|", "| r1 | x |", "prose", "| C | D |", "|---|---|",
            "| r2 | y |", "| :---: | --- |", "| r3 | z |"]
    data, headers, seps = skill_table_rows(rows)
    check("rows-classified", data == [4, 8, 10] and headers == [2, 6] and len(seps) == 3,
          data=data, headers=headers, separators=seps)
    audit_good = ("| SKILL.md line | disposition | evidence |\n|---|---|---|\n"
                  "| 4 | current | re-run 2026-10-18, tools/d2-typed-labels.py --check exit 0 |\n"
                  "| 8 | fixed | control: --selftest 11/11 (reports/round-24/fixes/row8.md) |\n"
                  "| 10 | erratum | dated 2026-10-18: prose only, no executable claim |\n")
    parsed_audit = parse_skill_audit(audit_good, 12)
    check("audit-covers-all", parsed_audit["covered"] == {4, 8, 10}
          and not parsed_audit["silent_stale"], covered=sorted(parsed_audit["covered"]))
    audit_bad = ("| line | disposition | evidence |\n|---|---|---|\n"
                 "| 4 | STALE | known drift |\n| 8 | fixed | examples/culture-d4/expected-holds.json |\n"
                 "| 10 | erratum | prose only |\n| 124 | current | 2026-10-18 |\n")
    parsed_bad_audit = parse_skill_audit(audit_bad, 12)
    check("audit-silent-stale-detected", any("known drift" in row for row in parsed_bad_audit["silent_stale"]),
          silent=parsed_bad_audit["silent_stale"])
    check("audit-fixed-without-control-detected",
          any("fixed" in row and "expected-holds" in row
              for row in parsed_bad_audit["stale_fixed_rows"]),
          stale_fixed=parsed_bad_audit["stale_fixed_rows"])
    check("audit-undated-erratum-detected",
          any("prose only" in row for row in parsed_bad_audit["undated_errata"]))
    check("audit-bare-count-no-false-coverage", 124 not in parsed_bad_audit["covered"]
          and parsed_bad_audit["covered"] == {8}, covered=sorted(parsed_bad_audit["covered"]))
    check("audit-pin-found", audit_pin("audit over SKILL.md sha256 "
                                       "fa498538482cc856efab0f7f055e1635e41c4b764d9985ce70dccdf8a868d4a9")
          == "fa498538482cc856efab0f7f055e1635e41c4b764d9985ce70dccdf8a868d4a9")
    audit_refs = ("Scope: registry rows at SKILL.md:490-501 at HEAD (prose range).\n\n"
                  "| # | row | verdict | evidence |\n|---|---|---|---|\n"
                  "| 1 | gate (:490) | CURRENT | probe W-1, 2026-10-18, tools/g.py |\n"
                  "| 2 | rows (:491-492) | CURRENT | dated 2026-10-18 |\n")
    parsed_refs = parse_skill_audit(audit_refs, 600)
    check("audit-paren-and-range-refs", {490, 491, 492} <= parsed_refs["covered"]
          and not (parsed_refs["covered"] & set(range(493, 502)))
          and not parsed_refs["silent_stale"] and not parsed_refs["stale_fixed_rows"],
          covered=sorted(parsed_refs["covered"]))
    audit_date_leak = ("| 3 | row | CURRENT | re-run 2026-10-18, exit 0 |\n")
    parsed_leak = parse_skill_audit(audit_date_leak, 600)
    check("audit-date-no-false-range", not (parsed_leak["covered"] & set(range(10, 19))),
          covered=sorted(parsed_leak["covered"]))
    parsed_title = parse_skill_audit(
        "# Round-24 consolidated SKILL.md staleness audit — D-claim audit table\n", 600)
    check("audit-title-staleness-no-hit", not parsed_title["silent_stale"]
          and not parsed_title["covered"],
          silent=parsed_title["silent_stale"])
    audit_ledger = ("## 2. Re-run ledger\n| M7 | battery row | STALE to FIXED (F3) | 2026-10-18 |\n"
                    "| M9 | other row | FIXED (F9) | 2026-10-18 |\n\n"
                    "## 4. Landed fixes\n| F3 | battery anchors, control: before/after grep |\n")
    parsed_ledger = parse_skill_audit(audit_ledger, 600)
    check("audit-fix-id-needs-ledger",
          not any("M7" in row for row in parsed_ledger["stale_fixed_rows"])
          and any("M9" in row for row in parsed_ledger["stale_fixed_rows"]),
          stale_fixed=parsed_ledger["stale_fixed_rows"])
    audit_foreign_id = ("## 2. Re-run ledger\n| M8 | row | STALE to FIXED (F3), corroborates F-1 | 2026-10-18 |\n\n"
                        "## 4. Landed fixes\n| F3 | control: grep -n |\n")
    parsed_foreign = parse_skill_audit(audit_foreign_id, 600)
    check("audit-any-ledger-id-names-control", not parsed_foreign["stale_fixed_rows"],
          stale_fixed=parsed_foreign["stale_fixed_rows"])
    audit_bare = "| 42 | VERIFIED | d2-typed-labels.py --selftest exit 0, 163/163 |\n"
    parsed_bare = parse_skill_audit(audit_bare, 600)
    check("audit-bare-filename-evidence", 42 in parsed_bare["covered"]
          and not parsed_bare["unevidenced_rows"], covered=sorted(parsed_bare["covered"]))
    audit_residual = ("- **R1 — mis-cite twice (`SKILL.md:128` and `:387`)**: Proposed erratum: "
                      "re-point to tools/harness/packet_uncertainty.py\n")
    parsed_residual = parse_skill_audit(audit_residual, 600)
    check("audit-residual-bullet", 128 in parsed_residual["covered"]
          and any("R1" in row for row in parsed_residual["undated_errata"]),
          covered=sorted(parsed_residual["covered"]), errata=parsed_residual["undated_errata"])
    audit_wrapped = ("- Method: each stale row below is either fixed with a\n"
                     "  before/after control recorded here, or dated (F2 ledger)\n\n"
                     "## 4. Landed fixes\n| F2 | control: grep -n byte-identical |\n")
    parsed_wrapped = parse_skill_audit(audit_wrapped, 600)
    check("audit-wrapped-bullet", not parsed_wrapped["stale_fixed_rows"]
          and not parsed_wrapped["silent_stale"],
          fixed=parsed_wrapped["stale_fixed_rows"], silent=parsed_wrapped["silent_stale"])
    audit_mixed = "| 9 | VERIFIED after F4 (dated erratum landed inside the row) | 2026-10-18 |\n"
    parsed_mixed = parse_skill_audit(audit_mixed, 600)
    check("audit-erratum-mention-with-verdict", not parsed_mixed["undated_errata"]
          and 9 in parsed_mixed["covered"], errata=parsed_mixed["undated_errata"])
    resolved, problems = citation_problems(
        "cites reports/round-23/validation.json:1-9 and MISSING-FILE.md and SKILL.md:99999", {})
    check("citation-problems-detected", resolved == 2 and len(problems) == 1
          and "out of range" in problems[0],
          resolved=resolved, problems=problems)
    try:
        safe_path("/tmp/outside")
        refused = False
    except ValueError:
        refused = True
    check("unsafe-evidence-path-refused", refused)
    try:
        strict_json('{"status": "open", "status": "closed"}')
        duplicate = False
    except ValueError:
        duplicate = True
    check("duplicate-json-key-refused", duplicate)
    check("git-blob-sha-known-answer",
          git_blob_sha(b"hello\n") == "ce013625030ba8dba906f756967f9e9ca394464a")
    passed = all(row["passed"] for row in controls)
    print(json.dumps({"round": 24, "command": f"{COMMAND} --selftest", "date": today(),
                      "selftest_passed": passed, "controls": controls,
                      "controls_passed": metric(sum(row["passed"] for row in controls), "runner positive/negative controls"),
                      "controls_total": metric(len(controls), "runner positive/negative controls")},
                     indent=2, sort_keys=True))
    return 0 if passed else 1


def measure():
    evidence = Evidence()
    claims = evidence.document(f"{ROUND_DIR}/claims.json") or {}
    targets = evidence.document(f"{ROUND_DIR}/targets.json") or {}
    baseline = claims.get("baseline_revision")
    live = live_lane()
    if live is None:
        raise ValueError("cannot locate the live lane root above the isolated clone")
    synced = sync_round_surface(live)
    preservation = protected_baseline(baseline)
    regressions = measure_regressions()
    review_text = evidence.text(REVIEW)
    review_boxes = parse_promotion_review(review_text) if review_text else None
    results = {}
    for claim_id, operation in (
            ("C", lambda: measure_calibration(evidence, regressions)),
            ("O", lambda: measure_operability(evidence, regressions, review_boxes)),
            ("D", lambda: measure_depth(evidence))):
        try:
            results[claim_id] = operation()
        except (OSError, ValueError, TypeError, KeyError, RuntimeError, AttributeError,
                subprocess.SubprocessError, shutil.Error) as error:
            results[claim_id] = result([f"Could not evaluate claim {claim_id}: "
                                        f"{type(error).__name__}: {error}"], {})
    changed_inputs = []
    for relative, expected in evidence.inputs.items():
        try:
            observed = sha(safe_path(relative).read_bytes())
        except (OSError, ValueError):
            observed = None
        if expected != observed:
            changed_inputs.append(relative)
    coherence = []
    if claims.get("round") != 24 or targets.get("round") != 24:
        coherence.append("Claims/targets are not both round 24")
    if targets.get("baseline_revision") != baseline:
        coherence.append("Claims/targets disagree on the declared baseline")
    declared = {row.get("id"): row.get("axis") for row in claims.get("claims", []) if isinstance(row, dict)}
    if declared != {"C": "calibration", "O": "operability", "D": "depth"}:
        coherence.append("Declared claim set is not C/calibration, O/operability, D/depth")
    worker_total = sum(targets.get("workers", {}).values()) if isinstance(targets.get("workers"), dict) else None
    if worker_total != claims.get("workers"):
        coherence.append("Targets worker counts do not sum to the declared worker wave")
    shonen = evidence.text(SHONEN)
    if shonen and shonen.count("- [ ]") != 4:
        coherence.append("SHONEN.md no longer carries exactly four unchecked promotion boxes")
    if changed_inputs:
        coherence.append("Evidence changed while being measured: " + ", ".join(changed_inputs))
    coherence.extend(evidence.errors)
    failures = [f"claim {claim_id}: {failure}" for claim_id, item in results.items()
                for failure in item["failures"]]
    failures.extend("preservation: " + item for item in preservation["failures"])
    failures.extend("evidence: " + item for item in coherence)
    return {"round": 24, "runner": RUNNER, "runner_sha256": sha(safe_path(RUNNER).read_bytes()),
            "counting_command": COMMAND, "date": today(), "baseline_revision": baseline,
            "targets_date": targets.get("date"), "claims_declared": declared,
            "acceptance_checks_passed": not failures, "claims": results,
            "failures": failures, "missing_dependencies": sorted(evidence.missing | {
                path for item in results.values() for path in item["missing_dependencies"]}),
            "protected_filed_artifacts": preservation,
            "protected_bytes_unchanged_during_run": metric(True, "protected inventory is a single snapshot against the declared baseline"),
            "synced_from_live": {key: value for key, value in sorted(synced.items())},
            "input_sha256": dict(sorted(evidence.inputs.items())),
            "limits": [
                "Run this round validator only in an isolated repository clone under the lane's .scratch with TMPDIR below that clone's .scratch. It never edits filed bytes, never commits, and never pushes.",
                "Claim C is measured from reports/round-24/promotion-review.md: four boxes, verdicts in the declared vocabulary, named non-author reviewers (>=2 distinct across the dossier), resolvable evidence with per-box anchors (SKILL.md, LOG.md, cold-run.md, PROVINCE.md), and conditions required for verified-with-conditions. The promotion decision itself stays operator-owned.",
                "Box 1 gets independent teeth here: every repo-path citation in SKILL.md is existence- and line-bound-resolved. Box 2 gets the fixed round-23 regression inventory re-run (D2->D3->D4->handoff), plus a LOG.md chain-presence check. Box 4 gets PROVINCE.md path resolution. No recorded command string from any evidence file is executed.",
                "Claim O is measured from reports/round-24/cold-run.md: >=2 distinct named seats, >=6 executed commands, invoked repo tools must exist, every break fixed-with-control (pointer + named control) or named as a box-3 condition, and an explicit no-breaks declaration otherwise.",
                "Claim D is measured from reports/round-24/skill-audit.md plus the audit-*.md fragments it consolidates (the fragments carry the per-row line refs) against every SKILL.md table data row; header and separator rows carry no executable claims and are excluded by declaration (counts in the receipt). Coverage requires an evidenced disposition (current | fixed | erratum) keyed on explicit SKILL.md:N, (:N), 'line N' and evidenced-table-range references; fixed names a control (or a fix-ledger id present in the document's own fix-ledger sections); a row whose sole disposition is erratum carries a date in the audit row or at the SKILL.md line it cites; an uppercase STALE verdict without fix or erratum is silent staleness and fails; a SKILL.md digest pin in the audit, if present, must match the measured bytes.",
                "Protected reports and frozen generations of rounds 8-23 must match the round-24 declared baseline; new round-24 files live under reports/round-24 only.",
            ]}


def guard_receipt():
    namespace = runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Measure round-24 C/O/D acceptance; use only in an isolated clone.")
    parser.add_argument("--check", action="store_true", help="print the measured JSON without writing validation.json")
    parser.add_argument("--selftest", action="store_true", help="exercise runner positive/negative controls without dependencies")
    args = parser.parse_args(argv)
    if args.check and args.selftest:
        parser.error("--check and --selftest are mutually exclusive")
    if ".scratch" not in ROOT.parts or not (ROOT / ".git").is_dir():
        print("could-not-evaluate: run round validators only in an isolated Git clone under the lane's .scratch", file=sys.stderr)
        return 2
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    (ROOT / ".scratch").mkdir(parents=True, exist_ok=True)
    if args.selftest:
        return selftest()
    try:
        receipt = measure()
    except (OSError, ValueError, TypeError, subprocess.SubprocessError) as error:
        print(f"could-not-evaluate: {type(error).__name__}: {error}", file=sys.stderr)
        return 2
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.check:
        print(rendered, end="")
    else:
        try:
            guard_receipt()
        except SystemExit as error:
            return error.code if isinstance(error.code, int) else 3
        safe_path(OUTPUT).write_text(rendered, encoding="utf-8")
        for claim_id, item in receipt["claims"].items():
            print(f"claim {claim_id}: {'PASS' if item['passed'] else 'FAIL'}")
        print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
        if receipt["missing_dependencies"]:
            print("missing_dependencies: " + ", ".join(receipt["missing_dependencies"]))
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
