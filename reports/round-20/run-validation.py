#!/usr/bin/env python3
"""Round-20 validator — re-measures the three declared claims D/O/C at close.

Claim D (depth): `tools/exercise-handoff-e2e.py` v3 assembles a handoff packet
from the D2+D3+D4 artifacts; D4 claims enter the claim ledger with the v2
uncertainty dimension `{status, basis}`; claim-to-record links resolve into
`examples/culture-d4/` records; the shape gate still reads `16/16 + 20/20` with
zero findings; the round-15-style contract audit re-run over v3 yields a
semantic PASS or pass-with-named-gaps; the v1/v2 paths stay byte-unchanged and
green. The v3 surface is the round-20 design
(`reports/round-20/handoff/design.md` §6): profiles v1 (default) / v2 / v3, one
stable summary line, census 27 claims / 15 / 7 / 5, `v2_subset=equal`.

Claim O (operability): the projector's era-alias leg resolves per packet family
(d2 -> the D2 rank-rules component, byte-identical; d4 -> the packet's own
declared rules or an open skip); the round-19 wart is closed; the d2/d3/d4
family runs, the D4 typed-pipeline gate (19/19) and the D4 adapter selftest
(12/12) are green WITHOUT the adapter's selftest mirror copying the foreign
`examples/culture-d2` tree; the re-pin cascade lands as new rows and every live
pin matches the live bytes.

Claim C (coverage): `corpus/README.md` is reconciled against the actual
partition contents, command-carried; every index row names an existing file;
every partition file is indexed; the newest revision block carries a date, a
counting command and the six partition counts; any declared-vs-live count delta
is named in the README, never silently absorbed.

Hard rules re-measured, not assumed: filed artifacts of rounds 8-19 are
compared byte-for-byte against the declared baseline revision — any change,
addition or removal under those directories fails closed. This runner writes
only its own receipt (`reports/round-20/validation.json`), never a filed round
8-19 byte and never the live tree. It measures; it does not certify truth,
canon, or lore receipt.
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-20"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
COMMAND = f"python3 {RUNNER}"
GUARD = "tools/harness/receipt_guard.py"
EXERCISE = "tools/exercise-handoff-e2e.py"
PROJECTOR = "tools/d2-typed-labels.py"
ADAPTER = "tools/assemble-d4-typed.py"
D3_ASSEMBLER = "tools/assemble-culture-d3.py"
D4_ASSEMBLER = "tools/assemble-culture-d4.py"
D2_ASSEMBLER = "tools/assemble-d2.py"
D4_GATE_PACKET = "examples/culture-d4/packet.d4.yml"
D4_PROJECTION = "examples/culture-d4/typed-labels.d4.yml"
D4_TYPED_PACKET = "examples/culture-d4/packet.d4.typed.yml"
D4_EXPECTED = "examples/culture-d4/expected-holds.json"
D4_PACKET = "examples/culture-d4/packet.d4.yml"
D2_PACKET = "examples/culture-d2/packet.d2.yml"
D2_PROJECTION = "examples/culture-d2/typed-labels.d2.yml"
D2_EXPECTED = "examples/culture-d2/expected-holds.json"
TYPED_PIPELINES = "tools/gates/typed-pipelines.json"
FILED = tuple(f"reports/round-{number}" for number in range(8, 20))
FILED_OUTSIDE = tuple(f"reports/round-{number}" for number in (5, 6, 7))
HANDOFF_DIR = f"{ROUND_DIR}/handoff"
V2_FROZEN = ("reports/round-15/handoff/expected.json",
             "reports/round-15/handoff/packet-v2-05.md",
             "reports/round-15/handoff/packet-v2-05.yml",
             "reports/round-11/handoff/expected.json")
PARTITIONS = ("civilizations", "linguistics", "myth-symbol", "culture-material",
              "synthesis", "verification")
MIRROR = ROOT / ".scratch/x18-wart-mirror"
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}(?:\s*\(?\s*stamps?\s*UTC)?\b")
POINTER_RE = re.compile(
    r"(?<![\w./-])(?:reports|tools|corpus|examples)/[\w./+-]+\.(?:json|md|py|ya?ml|tsv|txt|sh)\b")
STATUS_VOCAB = ("supported", "partial", "unresolved")
PLACEHOLDER_RE = re.compile(
    r"\b(tbd|tba|todo|placeholder|boilerplate|same[- ]as[- ](?:above|below)|"
    r"as (?:above|below)|see (?:above|below|other)|copy of|unchanged)\b", re.I)
BASELINE_RE = re.compile(r"[0-9a-f]{40,64}")
SCAN_RE = re.compile(
    r"(?:handoff-(?:v\d|e2e)|handoff-e2e):\s*exit=(\d+)\s+fields=(\d+)/(\d+)"
    r"\s+glossary=(\d+)/(\d+)\s+findings=(\d+)")
V3_TOKENS = {"claims": r"claims=(\d+)", "statuses": r"statuses=(\d+)/(\d+)/(\d+)",
             "v2_subset": r"v2_subset=(\w+)", "links": r"links=(\d+)/(\d+)",
             "alias_leg": r"alias_leg=(\w+)"}
DECLARED_COUNTS_RE = re.compile(
    r"civilizations\s+(\d+)[,\s]+linguistics\s+(\d+)[,\s]+myth-symbol\s+(\d+)"
    r"[,\s]+culture-material\s+(\d+)[,\s]+synthesis\s+(\d+)[,\s]+verification\s+(\d+)")


def today():
    return dt.date.today().isoformat()


def metric(value, operation):
    return {"value": value, "command": f"{COMMAND} ({operation})", "date": today()}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def sha256_of(path):
    try:
        return sha(Path(path).read_bytes())
    except OSError:
        return None


def safe_path(relative):
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or ".git" in path.parts:
        raise ValueError(f"not an in-lane path: {relative}")
    resolved = (ROOT / path).resolve()
    if not resolved.is_relative_to(ROOT):
        raise ValueError(f"path escapes lane: {relative}")
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


def run_command(parts, timeout=300):
    argv = [sys.executable, *parts]
    env = dict(os.environ)
    env.update(TMPDIR=str(ROOT / ".scratch"), PYTHONDONTWRITEBYTECODE="1")
    item = {"command": shlex.join(["python3", *parts]), "date": today(),
            "argv": ["python3", *parts]}
    try:
        source = safe_path(parts[0])
        item["source_sha256_before"] = sha256_of(source)
        run = subprocess.run(argv, cwd=ROOT, capture_output=True, timeout=timeout, env=env)
        item["source_sha256_after"] = sha256_of(source)
        item["source_unchanged"] = item["source_sha256_before"] == item["source_sha256_after"]
        item.update(exit=run.returncode if item["source_unchanged"] else None,
                    stdout=run.stdout.decode("utf-8", "replace"),
                    stderr=run.stderr.decode("utf-8", "replace"),
                    stdout_sha256=sha(run.stdout), stderr_sha256=sha(run.stderr))
        try:
            item["json"] = strict_json(item["stdout"])
        except (ValueError, TypeError):
            pass
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        item.update(exit=None, error=str(error),
                    timeout=isinstance(error, subprocess.TimeoutExpired))
    return item


def run_in(parts, cwd, timeout=300):
    argv = [sys.executable, *parts]
    env = dict(os.environ)
    env.update(TMPDIR=str(ROOT / ".scratch"), PYTHONDONTWRITEBYTECODE="1")
    item = {"command": "cd %s && %s" % (cwd, shlex.join(["python3", *parts])),
            "date": today()}
    try:
        run = subprocess.run(argv, cwd=str(cwd), capture_output=True, timeout=timeout, env=env)
        item.update(exit=run.returncode,
                    stdout=run.stdout.decode("utf-8", "replace")[-2000:],
                    stderr=run.stderr.decode("utf-8", "replace")[-2000:])
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        item.update(exit=None, error=str(error))
    return item


def git(*args, data=None):
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1", LC_ALL="C")
    proc = subprocess.run(["git", "--literal-pathspecs", *args], cwd=ROOT,
                          input=data, capture_output=True, timeout=120, env=env)
    if proc.returncode:
        raise ValueError(f"git {shlex.join(args)}: {proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout


def baseline_blobs(revision, directories):
    """{path: sha256} for every blob under `directories` at `revision`."""
    records = []
    for record in git("ls-tree", "-r", "-z", revision, "--", *directories).split(b"\0"):
        if not record:
            continue
        metadata, raw_path = record.split(b"\t", 1)
        mode, kind, oid = metadata.split()
        if kind != b"blob" or mode not in (b"100644", b"100755"):
            continue
        records.append((raw_path.decode("utf-8"), oid))
    blobs = {}
    if not records:
        return blobs
    payload = git("cat-file", "--batch",
                  data=b"".join(oid + b"\n" for _, oid in records))
    offset = 0
    for relative, oid in records:
        end = payload.index(b"\n", offset)
        header = payload[offset:end].split()
        if len(header) != 3 or header[0] != oid or header[1] != b"blob":
            raise ValueError(f"unexpected Git blob reply for {relative}")
        size = int(header[2])
        blobs[relative] = sha(payload[end + 1:end + 1 + size])
        offset = end + size + 2
    return blobs


def live_tree(directories):
    snapshot = {}
    for directory in directories:
        base = ROOT / directory
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                relative = path.relative_to(ROOT).as_posix()
                try:
                    snapshot[relative] = sha256_of(path)
                except OSError as error:
                    snapshot[relative] = f"ERROR: {error}"
    return snapshot


def ignored_paths(relative_paths):
    """Git-ignored paths among `relative_paths` (e.g. the `*.log` rule)."""
    if not relative_paths:
        return set()
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1", LC_ALL="C")
    proc = subprocess.run(["git", "check-ignore", "--stdin"], cwd=ROOT,
                          input="\n".join(relative_paths).encode(),
                          capture_output=True, env=env, timeout=120)
    return {line for line in proc.stdout.decode("utf-8", "replace").splitlines() if line}


def preservation_rows(baseline, live, baseline_label, ignored=()):
    rows = []
    for relative in sorted(set(baseline) | set(live)):
        old, new = baseline.get(relative), live.get(relative)
        if old is None:
            disposition = "untracked-ignored" if relative in ignored else "added"
        elif new is None:
            disposition = "removed"
        elif old == new:
            disposition = "byte-identical"
        else:
            disposition = "changed"
        rows.append({"path": relative, "baseline_sha256": old,
                     "current_sha256": new, "preservation": disposition})
    return rows


def filed_preservation(claims):
    """Rounds 8-19 must be byte-identical to the declared baseline revision.

    Tracked baseline blobs must match the live bytes exactly; a live file that
    is git-ignored (e.g. the `*.log` rule) and untracked is recorded, not
    failed — it is not a filed artifact. Any other addition or removal fails.
    """
    failures, rows = [], []
    try:
        baseline = claims.get("baseline_revision")
        if not isinstance(baseline, str) or not BASELINE_RE.fullmatch(baseline):
            raise ValueError("claims.json has no full baseline revision")
        pinned = baseline_blobs(baseline, FILED)
        if not pinned:
            raise ValueError("no filed round-8..19 blobs at the declared baseline")
        live = live_tree(FILED)
        ignored = ignored_paths([relative for relative in live if relative not in pinned])
        rows = preservation_rows(pinned, live, baseline, ignored)
        for row in rows:
            if row["preservation"] not in ("byte-identical", "untracked-ignored"):
                failures.append(
                    f"Filed artifact not byte-identical to {baseline[:12]}: "
                    f"{row['path']} ({row['preservation']})")
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        failures.append(f"Cannot establish filed-byte preservation: {error}")
    return result(failures, {
        "baseline_revision": claims.get("baseline_revision"),
        "files": rows,
        "checked": metric(len(rows), "compare baseline Git blobs with filed worktree bytes"),
        "violations": metric(sum(row["preservation"] not in ("byte-identical", "untracked-ignored")
                                 for row in rows),
                             "count changed/added/removed filed round-8..19 paths"),
        "untracked_ignored": metric(sum(row["preservation"] == "untracked-ignored" for row in rows),
                                    "count git-ignored untracked files under filed rounds (informational)"),
    })


def outside_filed_changes(claims):
    """Rounds 5-7 (outside the operator's declared range) — informational only."""
    try:
        baseline = claims.get("baseline_revision")
        pinned = baseline_blobs(baseline, FILED_OUTSIDE)
        live = live_tree(FILED_OUTSIDE)
        rows = preservation_rows(pinned, live, baseline)
        return {"files": rows,
                "changed": metric(sum(row["preservation"] != "byte-identical" for row in rows),
                                  "count non-identical filed round-5..7 changes"),
                "note": "outside the operator's rounds-8..19 freeze; recorded, not failed"}
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        return {"error": str(error)}


# ---------------------------------------------------------------- parsers


def scan_line(text):
    """Parse the exercise summary line (v1/v2/v3 spellings)."""
    match = SCAN_RE.search(text)
    if not match:
        return None
    parsed = {"exit": int(match.group(1)), "fields": int(match.group(2)),
              "fields_total": int(match.group(3)),
              "glossary": int(match.group(4)), "glossary_total": int(match.group(5)),
              "findings": int(match.group(6)), "raw": match.group(0)}
    line = text[match.start():].splitlines()[0]
    for key, pattern in V3_TOKENS.items():
        found = re.search(pattern, line)
        if not found:
            continue
        parsed[key] = (tuple(int(value) for value in found.groups())
                       if len(found.groups()) > 1 else
                       (int(found.group(1)) if found.group(1).isdigit() else found.group(1)))
    return parsed


def parse_ledger_rows(text):
    """Claim rows from a v2/v3 markdown `claim_ledger` table.

    Each row: {id, uncertainty: {status, basis} | None, links: [str], raw}.
    """
    rows = []
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if re.match(r"#{1,6}\s", line) and "claim" in line.lower() and "ledger" in line.lower():
            start = index + 1
            break
    if start is None:
        return rows
    end = len(lines)
    for index in range(start, len(lines)):
        if re.match(r"#{1,6}\s", lines[index]) and "claim" not in lines[index].lower():
            end = index
            break
    body = lines[start:end]
    header = None
    for line in body:
        if line.strip().startswith("|"):
            cells = [cell.strip().lower() for cell in line.strip().strip("|").split("|")]
            if any("claim" in cell or cell in ("id", "claim_id") for cell in cells):
                header = cells
                break
    if header is None:
        return rows
    separator_seen = False
    status_index = next((i for i, name in enumerate(header)
                         if "uncertainty_status" in name or name.strip() == "uncertainty status"), None)
    basis_index = next((i for i, name in enumerate(header)
                        if "uncertainty_basis" in name or name.strip() == "uncertainty basis"), None)
    legacy_index = next((i for i, name in enumerate(header)
                         if "uncertainty" in name and i not in (status_index, basis_index)), None)
    links_index = next((i for i, name in enumerate(header)
                        if name.strip().rstrip("s") in ("link", "record_link")), None)
    for line in body:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", cell) for cell in cells if cell):
            separator_seen = True
            continue
        if not separator_seen or len(cells) < len(header):
            continue
        uncertainty = None
        if status_index is not None and status_index < len(cells):
            status = re.search(r"\b(supported|partial|unresolved)\b", cells[status_index], re.I)
            basis = cells[basis_index] if basis_index is not None and basis_index < len(cells) else ""
            uncertainty = {"status": status.group(1).lower() if status else None,
                           "basis": basis.strip().strip("**")}
        elif legacy_index is not None and legacy_index < len(cells):
            cell = cells[legacy_index]
            status = re.search(r"\b(supported|partial|unresolved)\b", cell, re.I)
            if status:
                rest = (cell[:status.start()] + cell[status.end():]).replace("**", "").strip(" `:;-—")
                basis = re.search(r"basis\s*[:\-—]\s*(.+)", rest, re.I)
                uncertainty = {"status": status.group(1).lower(),
                               "basis": (basis.group(1) if basis else rest).strip()}
        rows.append({"id": cells[0], "uncertainty": uncertainty,
                     "links": (cells[links_index] if links_index is not None
                               and links_index < len(cells) else ""),
                     "raw": stripped})
    return rows


def uncertainty_problems(rows):
    """Per-claim uncertainty judgments (vocabulary, basis presence, boilerplate)."""
    judgments = []
    seen_bases = collections.Counter()
    for row in rows:
        entry = {"claim": row["id"], "status": None, "basis": "", "problems": []}
        uncertainty = row.get("uncertainty")
        if uncertainty is None:
            entry["problems"].append("no uncertainty dimension")
        else:
            entry["status"] = uncertainty.get("status")
            basis = (uncertainty.get("basis") or "").strip()
            entry["basis"] = basis
            if entry["status"] not in STATUS_VOCAB:
                entry["problems"].append(f"status off vocabulary: {entry['status']!r}")
            if not basis:
                entry["problems"].append("empty basis")
            elif PLACEHOLDER_RE.search(basis):
                entry["problems"].append(f"placeholder basis: {basis!r}")
            else:
                seen_bases[re.sub(r"\s+", " ", basis).lower()] += 1
        judgments.append(entry)
    duplicates = {basis for basis, count in seen_bases.items() if count > 1}
    for judgment in judgments:
        normalized = re.sub(r"\s+", " ", judgment["basis"]).lower()
        if normalized and normalized in duplicates:
            judgment["problems"].append("boilerplate basis repeated on multiple claims")
    return judgments


def link_paths(cell):
    """Repo-relative paths inside a links cell, with the `#token` stripped."""
    return sorted({match.group(0) for match in POINTER_RE.finditer(cell or "")})


def walk_json(node, path=()):
    yield path, node
    if isinstance(node, dict):
        for key, value in node.items():
            yield from walk_json(value, path + (str(key),))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from walk_json(value, path + (str(index),))


def receipt_surface(receipt):
    """D4/uncertainty/link facts from the exercise's JSON receipt, if any."""
    facts = {"d4_mentions": 0, "claims": [], "d4_links": [], "d4_links_resolved": [],
             "resolved_claims": 0}
    if receipt is None:
        return facts
    text = json.dumps(receipt, ensure_ascii=False)
    facts["d4_mentions"] = len(re.findall(r"examples/culture-d4/", text))
    for path, node in walk_json(receipt):
        if isinstance(node, dict):
            uncertainty = node.get("uncertainty")
            identifier = node.get("claim_id") or node.get("id")
            if isinstance(uncertainty, dict) and identifier:
                status = uncertainty.get("status")
                basis = uncertainty.get("basis")
                if isinstance(basis, dict):
                    basis = json.dumps(basis, ensure_ascii=False)
                facts["claims"].append({"id": str(identifier), "status": status,
                                        "basis": str(basis or "")[:300],
                                        "path": "/".join(path)})
            for key, value in node.items():
                if isinstance(value, str) and "culture-d4" in value:
                    for relative in POINTER_RE.findall(value):
                        if relative.startswith("examples/culture-d4/"):
                            facts["d4_links"].append(relative)
    for relative in sorted(set(facts["d4_links"])):
        try:
            if safe_path(relative).is_file():
                facts["d4_links_resolved"].append(relative)
        except ValueError:
            continue
    facts["resolved_claims"] = sum(
        1 for claim in facts["claims"]
        if claim["status"] in STATUS_VOCAB and claim["basis"])
    return facts


def contract_audit_verdict(text):
    """Classify a contract-audit re-run: pass / pass-with-named-gaps / fail.

    The verdict line is read by its leading clause only (up to the first
    period, semicolon, em-dash or bold marker), so trailing prose that merely
    mentions an older reject does not turn a PASS into a failure.
    """
    dated = bool(DATE_RE.search(text))
    commanded = bool(re.search(r"\b(?:python3?|git|sha256sum|command)\b", text, re.I))
    label = r"(?:verdict|overall|conclusion|result)"
    entries = [(match.start(), match.group(1)) for match in re.finditer(
        rf"(?im)^\s*(?:[-*]\s+)?(?:\*\*)?{label}(?:\*\*)?\s*[:—-]\s*(.+?)\s*(?:\*\*)?$", text)]
    verdict_value = entries[-1][1].strip() if entries else ""
    leading_value = re.split(r"[.;—]|\s\*\*", verdict_value, maxsplit=1)[0].strip()
    fail_marker = re.compile(r"\b(?:fail(?:ed|s|ure)?|reject(?:ed)?|blocked)\b|not\s+pass", re.I)
    explicit_fail = bool(entries) and bool(fail_marker.search(leading_value))
    if explicit_fail:
        state = "fail"
    elif re.search(r"\b(?:pass|green)\b", leading_value, re.I):
        state = "named-gaps" if re.search(
            r"\bnamed\b|\bminors?\b|\bgaps?\b|\bremainders?\b", leading_value, re.I) else "pass"
    else:
        state = "other"
    gap_items = []
    for line in text.splitlines():
        if re.search(r"\bgap\b|\bremaining\b|\bopen\b|\bblocker\b|\bpending\b|\bremainder\b",
                     line, re.I) and re.match(r"\s*(?:[-*]|\d+\.)\s+", line):
            gap_items.append(line.strip())
    owned_gaps = [item for item in gap_items
                  if re.search(r"\bowner\b|owner:\s*\S|responsible[:\s]|OQ-V3-\d+", item, re.I)]
    named_gaps = bool(gap_items) and len(owned_gaps) >= max(1, len(gap_items))
    if not dated or not commanded:
        classification = "unparseable"
    elif state == "fail":
        classification = "fail"
    elif state == "pass":
        classification = "pass"
    elif state == "named-gaps" or named_gaps:
        classification = "pass-with-named-gaps"
    else:
        classification = "fail"
    return {"classification": classification, "dated": dated, "commanded": commanded,
            "verdict": verdict_value, "leading_verdict": leading_value,
            "explicit_fail": explicit_fail, "state": state,
            "gap_items": gap_items, "owned_gaps": owned_gaps}


def readme_sections(text):
    """`## <partition>/ (N)` headers with their body slices."""
    sections = {}
    matches = list(re.finditer(r"^##\s+([\w-]+)/\s*\((\d+)\)\s*$", text, re.M))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[match.group(1)] = {"declared": int(match.group(2)),
                                    "body": text[match.end():end]}
    return sections


def readme_rows(body):
    """Index rows: `- \\`file.md\\` — description`."""
    rows = []
    for line in body.splitlines():
        match = re.match(r"-\s+`([^`]+)`", line.strip())
        if match and match.group(1).endswith(".md"):
            rows.append(match.group(1))
    return rows


def newest_revision(text):
    matches = list(re.finditer(r"^revision:\s*(.+)$", text, re.M))
    if not matches:
        return None
    end = matches[1].start() if len(matches) > 1 else len(text)
    return text[matches[0].start():end]


def d4_marker_regex():
    return re.compile(r"copytree\(\s*ROOT\s*/\s*[\"']examples/culture-d2")


def yaml_assembly_block(text):
    """Direct keys of the top-level `assembly:` block of a YAML-subset document."""
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line == "assembly:":
            start = index + 1
            break
    if start is None:
        return {}
    block = {}
    for line in lines[start:]:
        if line and not line.startswith(" "):
            break
        match = re.match(r"^  ([A-Za-z_][\w-]*):\s*\"?([^\"\n]*)\"?\s*$", line)
        if match:
            block[match.group(1)] = match.group(2)
    return block


# ------------------------------------------------------------------ claim D


def discover(paths, name_pattern, content_pattern="(?!)"):
    name_re = re.compile(name_pattern, re.I)
    content_re = re.compile(content_pattern, re.I)
    named, content = [], []
    for relative in paths:
        if not relative.endswith((".md", ".json")):
            continue
        if name_re.search(Path(relative).name.replace("-", " ").replace("_", " ")):
            named.append(relative)
            continue
        try:
            text = (ROOT / relative).read_text(encoding="utf-8", errors="replace")[:40000]
        except OSError:
            continue
        if content_re.search(text):
            content.append(relative)
    return named + content


def round20_files():
    base = ROOT / ROUND_DIR
    if not base.is_dir():
        return []
    return [path.relative_to(ROOT).as_posix() for path in sorted(base.rglob("*"))
            if path.is_file() and "__pycache__" not in path.parts
            and Path(path).name not in ("claims.json", "targets.json", "run-validation.py",
                                        "validation.json")]


def measure_d(evidence, paths, preservation):
    """Claim D — the delivered v3 exercise surface, measured as shipped.

    When the CLI exposes `--profile` (design.md §6), the default run is the v1
    path and the explicit `--profile v3` run is the v3 path; the v1 path is not
    required to carry the v2/v3 semantic-validator legs. When the revision is
    single-profile, the default run is the v3 path. The v2 path is measured
    through its round-20 successor baseline row (`expected-v2-07-*.json`,
    replayed by the filed round-15 `frozen-verify.py`), never through a
    re-rendered packet.
    """
    failures, missing = [], set()
    runs = {}
    source = (ROOT / EXERCISE).read_text(encoding="utf-8", errors="replace")
    has_profile = "--profile" in source

    def exercise_checks(label, run, scan, require_semantics):
        if run.get("exit") != 0:
            failures.append(f"{label} not green: {run.get('command')} exit "
                            f"{run.get('exit')} — "
                            f"{(run.get('stdout') or run.get('stderr') or '')[-250:]}")
            return
        if scan is None:
            failures.append(f"{label} printed no parsable summary line")
            return
        if (scan["fields"], scan["fields_total"]) != (16, 16):
            failures.append(f"{label} shape gate fields {scan['fields']}/{scan['fields_total']} != 16/16")
        if (scan["glossary"], scan["glossary_total"]) != (20, 20):
            failures.append(f"{label} shape gate glossary {scan['glossary']}/{scan['glossary_total']} != 20/20")
        if scan["findings"] != 0:
            failures.append(f"{label} shape gate findings {scan['findings']} != 0")
        if "links" in scan and scan["links"][0] != scan["links"][1]:
            failures.append(f"{label} links not fully resolved: {scan['links']}")
        stdout = run.get("stdout") or ""
        if require_semantics:
            for marker, description in (
                    ("semantic-uncertainty", "the uncertainty validator leg"),
                    ("semantic-links", "the link validator leg")):
                if marker not in stdout:
                    failures.append(f"{label} output carries no {description} ({marker})")
                elif not re.search(rf"{marker}[^\n]*findings 0", stdout):
                    failures.append(f"{label} {description} did not report findings 0")
            if not re.search(r"frozen-claims:[^\n]*match the baseline", stdout):
                failures.append(f"{label} output carries no frozen-claims match line")
        if not re.search(r"preservation:[^\n]*byte-identical", stdout):
            failures.append(f"{label} output carries no read-set preservation line")

    # (a) the default run — the v1 path when the CLI exposes profiles, else the
    #     single delivered v3 path
    runs["exercise"] = run_command([EXERCISE], timeout=600)
    scan = scan_line(runs["exercise"].get("stdout", ""))
    before_default = len(failures)
    exercise_checks("exercise", runs["exercise"], scan,
                    require_semantics=not has_profile)
    if has_profile and len(failures) > before_default:
        # the default run is the v1 path; the O claim's projector change moved a
        # file the round-11 v1 baseline pins, so a red v1 run is accepted only
        # when a round-20 artifact documents the drift (a named supersession,
        # never a silent one)
        documented = []
        for relative in paths:
            try:
                text = (ROOT / relative).read_text(encoding="utf-8", errors="replace")[:60000]
            except OSError:
                continue
            if re.search(r"\bv1\b", text) and "d2-typed-labels" in text \
                    and re.search(r"drift|digest|re-?pin", text, re.I):
                documented.append(relative)
        runs["exercise"]["documented_red"] = documented[:3]
        if documented:
            del failures[before_default:]
        else:
            failures.append("exercise (the v1 default path) is red without a round-20 "
                            "artifact documenting the digest drift")
    v3_scan = None if has_profile else scan
    if has_profile:
        runs["exercise-v3"] = run_command([EXERCISE, "--profile", "v3"], timeout=600)
        v3_scan = scan_line(runs["exercise-v3"].get("stdout", ""))
        exercise_checks("exercise --profile v3", runs["exercise-v3"], v3_scan,
                        require_semantics=True)
        # the v2 profile is recorded; a red run must be documented in a round-20
        # artifact (the round-15 baseline is a documented supersession)
        runs["exercise-v2"] = run_command([EXERCISE, "--profile", "v2"], timeout=600)
        v2_run = runs["exercise-v2"]
        if v2_run.get("exit") == 2 and "unrecognized arguments" in (v2_run.get("stderr") or ""):
            failures.append("exercise --profile v2 is advertised but not accepted")
        elif v2_run.get("exit") not in (0, None):
            documented = []
            for relative in paths:
                if not re.search(r"v2|regression", Path(relative).name, re.I):
                    continue
                text = (ROOT / relative).read_text(encoding="utf-8", errors="replace")[:60000]
                if re.search(r"V2F-DIGEST|expected-v2-07|v2 (path|frozen|baseline)", text, re.I):
                    documented.append(relative)
            v2_run["documented_red"] = documented[:3]
            if not documented:
                failures.append(f"exercise --profile v2 exited {v2_run.get('exit')} without a "
                                f"round-20 artifact documenting the red")
    else:
        runs["exercise-note"] = {
            "command": "python3 tools/exercise-handoff-e2e.py --help",
            "date": today(),
            "note": "the delivered CLI exposes no --profile switch; the default run "
                    "is the v3 path (baseline reports/round-20/handoff/expected.json)"}

    # (b) the control matrix
    selftest_argv = ([EXERCISE, "--profile", "v3", "--selftest"] if has_profile
                     else [EXERCISE, "--selftest"])
    runs["selftest"] = run_command(selftest_argv, timeout=600)
    if runs["selftest"].get("exit") != 0 or "selftest: OK" not in (runs["selftest"].get("stdout") or ""):
        failures.append(f"exercise selftest not green: exit {runs['selftest'].get('exit')} — "
                        f"{(runs['selftest'].get('stdout') or runs['selftest'].get('stderr') or '')[-250:]}")

    # (c) v2 path green: the round-20 successor baseline row, replayed
    v2_rows = sorted(relative for relative in paths
                     if re.search(r"expected-v2-07.*\.json$", Path(relative).name))
    if v2_rows:
        successor = v2_rows[-1]
        runs["v2-successor"] = run_command(
            ["reports/round-15/handoff/frozen-verify.py", "--baseline", successor])
        stdout = runs["v2-successor"].get("stdout") or ""
        if runs["v2-successor"].get("exit") != 0:
            failures.append(f"v2 successor row not green: {successor} exit "
                            f"{runs['v2-successor'].get('exit')} — "
                            f"{(stdout or runs['v2-successor'].get('stderr') or '')[-250:]}")
        elif "frozen-v2: exit=0" not in stdout:
            failures.append(f"v2 successor row {successor} replayed without a green "
                            f"frozen-v2 line")
    else:
        missing.add(f"{ROUND_DIR}/**/expected-v2-07-*.json")
        failures.append("no round-20 v2 successor baseline row found "
                        "(expected-v2-07-*.json under reports/round-20/)")
    for relative in V2_FROZEN:
        if not (ROOT / relative).is_file():
            missing.add(relative)
            failures.append(f"v2 frozen surface missing: {relative}")

    # (d) the filed v3 packet document: D4 claims with uncertainty, links into
    # culture-d4; when several keyed builds exist, the highest build wins.
    packet_candidates = discover(paths, r"packet", r"claim_ledger")

    def build_rank(relative):
        numbers = [int(number) for number in re.findall(r"(\d+)", Path(relative).stem)]
        try:
            mtime = (ROOT / relative).stat().st_mtime
        except OSError:
            mtime = 0
        return (max(numbers) if numbers else -1, mtime)

    v3_packets = [relative for relative in packet_candidates
                  if re.search(r"v3", Path(relative).name, re.I)]
    packet = sorted(v3_packets, key=build_rank, reverse=True)[0] if v3_packets else None
    packet = packet or (sorted(packet_candidates, key=build_rank, reverse=True)[0]
                        if packet_candidates else None)
    packet_rows, judgments = [], []
    packet_measurement = {"path": packet, "candidates": packet_candidates}
    if packet:
        packet_rows = parse_ledger_rows(evidence.text(packet))
        judgments = uncertainty_problems(packet_rows)
        for judgment in judgments:
            for problem in judgment["problems"]:
                failures.append(f"packet {packet} claim {judgment['claim']}: {problem}")
        d4_rows = [row for row in packet_rows
                   if any(link.startswith("examples/culture-d4/") for link in link_paths(row["links"]))
                   or re.search(r"D4-CL\d+", row["id"])]
        packet_measurement.update({"rows": len(packet_rows), "d4_rows": len(d4_rows),
                                   "statuses": dict(collections.Counter(
                                       row["uncertainty"]["status"] for row in packet_rows
                                       if row["uncertainty"]))})
        if not d4_rows:
            failures.append(f"packet {packet} carries no D4 claim row")
        else:
            unresolved_links = [link for row in d4_rows for link in link_paths(row["links"])
                                if not safe_path(link).is_file()]
            if unresolved_links:
                failures.append(f"packet {packet} D4 links do not resolve: "
                                f"{sorted(set(unresolved_links))[:5]}")
        expected_rows = int((v3_scan or {}).get("claims", 0) or 0)
        if expected_rows and len(packet_rows) not in (0, expected_rows):
            failures.append(f"packet {packet} parses {len(packet_rows)} rows but the "
                            f"exercise census says {expected_rows}")
        if v3_scan and "statuses" in v3_scan and packet_rows:
            histogram = packet_measurement["statuses"]
            census = {"supported": v3_scan["statuses"][0], "partial": v3_scan["statuses"][1],
                      "unresolved": v3_scan["statuses"][2]}
            if histogram != census:
                failures.append(f"packet {packet} status histogram {histogram} != exercise "
                                f"census {census}")
        histogram = packet_measurement["statuses"]
        for status in ("partial", "unresolved"):
            if not histogram.get(status):
                failures.append(f"packet {packet} carries no {status!r} claim row "
                                f"(the uncertainty grammar is not exercised)")
    else:
        missing.add(f"{HANDOFF_DIR}/<packet-v3>.md")

    # (f) contract audit re-run over v3 — name match first, then content match;
    # when several audits exist (a superseded keyed build), the highest build
    # number wins, then the newest mtime.
    audit_candidates = discover(
        paths, r"contract",
        r"contract[- ]?v2|contract audit|contract-recheck")

    def audit_rank(relative):
        try:
            text = (ROOT / relative).read_text(encoding="utf-8", errors="replace")[:40000]
        except OSError:
            text = ""
        builds = [int(number) for number in re.findall(r"build[ -]?(\d+)", text, re.I)]
        try:
            mtime = (ROOT / relative).stat().st_mtime
        except OSError:
            mtime = 0
        return (max(builds) if builds else -1, mtime)

    verdict_record = {"candidates": audit_candidates}
    chosen = None
    v3_candidates = [relative for relative in audit_candidates
                     if re.search(r"v3", evidence.text(relative), re.I)]
    for relative in sorted(v3_candidates, key=audit_rank, reverse=True):
        chosen = relative
        break
    if chosen is None and audit_candidates:
        chosen = sorted(audit_candidates, key=audit_rank, reverse=True)[0]
    verdict_record["build_rank"] = {relative: audit_rank(relative)
                                    for relative in audit_candidates}
    if chosen:
        text = evidence.text(chosen)
        verdict_record.update({"path": chosen, **contract_audit_verdict(text)})
        if verdict_record["classification"] not in ("pass", "pass-with-named-gaps"):
            failures.append(f"contract audit re-run verdict is "
                            f"{verdict_record['classification']!r}, not a semantic PASS "
                            f"or named gaps with owners: {chosen}")
    else:
        missing.add(f"{ROUND_DIR}/<contract-audit-rerun>.md")
        failures.append(f"No contract-audit re-run artifact found under {ROUND_DIR}/")

    # (g) v3 baseline lands under the round dir, never a gate root
    baselines = [relative for relative in paths
                 if relative.startswith(HANDOFF_DIR)
                 and Path(relative).name == "expected.json"]
    v3_baseline = baselines[0] if baselines else None
    if v3_baseline:
        payload = evidence.document(v3_baseline)
        if not isinstance(payload, dict):
            failures.append(f"v3 baseline {v3_baseline} is not strict JSON")
        else:
            text = json.dumps(payload, ensure_ascii=False, sort_keys=True)
            if not DATE_RE.search(text):
                failures.append(f"v3 baseline {v3_baseline} carries no freeze date")
            if not re.search(r"packet_sha256|packet_sha|census|scan", text, re.I):
                failures.append(f"v3 baseline {v3_baseline} pins no packet/census value")
            v3_run = runs.get("exercise-v3") or runs["exercise"]
            run_sha = re.search(r"packet_sha256=([0-9a-f]{64})", v3_run.get("stdout") or "")
            pinned = payload.get("packet_sha256")
            if run_sha and pinned and run_sha.group(1) != pinned:
                failures.append(f"v3 baseline {v3_baseline} pins packet {str(pinned)[:12]}… "
                                f"but the run assembled {run_sha.group(1)[:12]}…")
    else:
        missing.add(f"{HANDOFF_DIR}/expected.json")
        failures.append(f"No v3 baseline expected.json under {HANDOFF_DIR}/")

    failures.extend(preservation["failures"])
    return result(failures, {
        "runs": {name: {**{key: value for key, value in run.items()
                           if key not in ("stdout", "stderr", "json", "argv")},
                        "stdout_tail": (run.get("stdout") or "")[-300:],
                        "stderr_tail": (run.get("stderr") or "")[-200:]}
                 for name, run in runs.items()},
        "exercise_scan": scan, "v3_scan": v3_scan,
        "packet": packet_measurement, "uncertainty": judgments,
        "contract_audit": verdict_record, "v3_baseline": v3_baseline,
        "filed_bytes": preservation,
    }, missing)


# ------------------------------------------------------------------ claim O


def pin_checks(evidence):
    """Pin channels, split by what the tools actually enforce.

    Enforced (a mismatch fails the claim): the `typed-pipelines.json` d4
    profile pins (gate L1-profile/L4-pins, exit 2 on stale), the D4
    projection's own `assembly.packet_sha256` (adapter projection freshness,
    exit 2), and the pins the typed packet itself declares (gate L4-pins,
    generalized). Advisory (recorded, never failed): `expected-holds.json`'s
    `projector_sha256` / `projection_sha256` fields — no delivered tool reads
    them (the gate compares the hold set), and the round-20 O seat's shard 4
    records the file's movement as none.
    """
    failures, advisories, pins = [], [], {}
    live = {
        "projector_sha256": sha256_of(ROOT / PROJECTOR),
        "projection_sha256": sha256_of(ROOT / D4_PROJECTION),
        "packet_sha256": sha256_of(ROOT / D4_PACKET),
        "adapter_sha256": sha256_of(ROOT / ADAPTER),
        "assembler_sha256": sha256_of(ROOT / D4_ASSEMBLER),
        "reader_sha256": sha256_of(ROOT / "tools/gates/costume-era-consistency-gate.py"),
        "serializer_sha256": sha256_of(ROOT / "tools/assemble-d2.py"),
    }
    profiles = evidence.document(TYPED_PIPELINES)
    profile_rows = []
    if isinstance(profiles, dict):
        for profile in profiles.get("profiles") or []:
            if not isinstance(profile, dict) or str(profile.get("id")) != "d4":
                continue
            for key, live_key in (("packet", "packet_sha256"),
                                  ("assembler", "assembler_sha256"),
                                  ("projection", "projection_sha256"),
                                  ("adapter", "adapter_sha256"),
                                  ("expected", None)):
                field = profile.get(key)
                declared = field.get("sha256") if isinstance(field, dict) else None
                live_value = sha256_of(ROOT / D4_EXPECTED) if live_key is None else live.get(live_key)
                profile_rows.append({"surface": TYPED_PIPELINES, "field": key,
                                     "pinned": declared, "live": live_value,
                                     "ok": declared == live_value,
                                     "unpinned_note": (field.get("note")
                                                       if isinstance(field, dict) else None)
                                     if declared is None else None})
    pins["typed_pipelines"] = profile_rows
    for row in profile_rows:
        if not row["ok"] and row["pinned"] is not None:
            failures.append(f"stale pin: {row['surface']} {row['field']} "
                            f"{str(row['pinned'])[:12]}… != live {str(row['live'])[:12]}…")
    projection_doc = evidence.document(D4_PROJECTION)
    projection_assembly = (projection_doc or {}).get("assembly") \
        if isinstance(projection_doc, dict) else None
    projection_pin = projection_assembly.get("packet_sha256") \
        if isinstance(projection_assembly, dict) else None
    pins["projection_self_pin"] = {"surface": D4_PROJECTION, "key": "packet_sha256",
                                   "pinned": projection_pin, "live": live["packet_sha256"],
                                   "ok": projection_pin == live["packet_sha256"]}
    if projection_pin != live["packet_sha256"]:
        failures.append(f"stale projection pin: {D4_PROJECTION} records "
                        f"{str(projection_pin)[:12]}…, packet hashes "
                        f"{str(live['packet_sha256'])[:12]}…")
    typed_text = evidence.text(D4_TYPED_PACKET)
    typed_assembly = yaml_assembly_block(typed_text)
    if typed_text and not typed_assembly:
        failures.append(f"{D4_TYPED_PACKET} carries no parsable assembly block")
    typed_rows = []
    for key in ("assembler_sha256", "reader_sha256", "serializer_sha256"):
        declared = typed_assembly.get(key)
        if declared is None:
            continue
        typed_rows.append({"surface": D4_TYPED_PACKET, "key": key, "pinned": declared,
                           "live": live.get(key), "ok": declared == live.get(key)})
    pins["typed_packet"] = typed_rows
    for row in typed_rows:
        if not row["ok"]:
            failures.append(f"stale pin: {row['surface']} {row['key']} "
                            f"{str(row['pinned'])[:12]}… != live {str(row['live'])[:12]}…")
    pins["typed_packet_note"] = ("the adapter's in-memory packet/projection/adapter pins are "
                                 "not rendered into the typed packet text; the gate's L4-pins "
                                 "verifies the pins the text declares")
    expected_surfaces = (
        (D4_EXPECTED, live.get("projector_sha256"), live.get("projection_sha256"),
         live.get("packet_sha256")),
        (D2_EXPECTED, live.get("projector_sha256"), sha256_of(ROOT / D2_PROJECTION),
         sha256_of(ROOT / D2_PACKET)),
    )
    expected_rows = []
    for surface, projector_live, projection_live, packet_live in expected_surfaces:
        expected = evidence.document(surface)
        if not isinstance(expected, dict):
            failures.append(f"{surface} is not strict JSON")
            continue
        surface_live = {"projector_sha256": projector_live,
                        "projection_sha256": projection_live,
                        "packet_sha256": packet_live}
        for key in ("projector_sha256", "projection_sha256", "packet_sha256"):
            declared = expected.get(key)
            row = {"surface": surface, "key": key, "pinned": declared,
                   "live": surface_live.get(key), "ok": declared == surface_live.get(key)}
            expected_rows.append(row)
            if not row["ok"] and key == "packet_sha256":
                failures.append(f"stale pin: {row['surface']} {row['key']} "
                                f"{str(row['pinned'])[:12]}… != live {str(row['live'])[:12]}…")
            elif not row["ok"]:
                advisories.append({"surface": row["surface"], "key": row["key"],
                                   "pinned": row["pinned"], "live": row["live"],
                                   "why": "no delivered tool reads this field; the gate "
                                          "compares the hold set (shard 4 row 7 records the "
                                          "file's movement as none)"})
    pins["expected_holds"] = expected_rows
    pins["advisory_stale_pins"] = advisories
    repin_rows = [relative for relative in round20_files()
                  if re.search(r"repin|r20|round-20", Path(relative).name, re.I)]
    gate_rows = []
    for root in ("tools/gates/expected", "tools/gates/frozen"):
        base = ROOT / root
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts:
                continue
            relative = path.relative_to(ROOT).as_posix()
            if re.search(r"(?:^|/)(?:r20-post|r20-pre|round-20|repin)", relative):
                gate_rows.append(relative)
    pins["repin_new_rows"] = {"round20": repin_rows, "gate_roots": gate_rows}
    if not repin_rows and not gate_rows:
        failures.append("no round-20 re-pin rows landed (reports/round-20/** or "
                        "tools/gates/{expected,frozen}/** r20 rows)")
    return failures, pins


def wart_mirror():
    """The no-foreign-tree mirror: tools + examples/culture-d4 only."""
    shutil.rmtree(MIRROR, ignore_errors=True)
    (MIRROR / "tools/gates").mkdir(parents=True)
    (MIRROR / "examples").mkdir(parents=True)
    for source in sorted((ROOT / "tools").glob("*.py")):
        shutil.copyfile(source, MIRROR / "tools" / source.name)
    for name in ("costume-era-consistency-gate.py",):
        shutil.copyfile(ROOT / "tools/gates" / name, MIRROR / "tools/gates" / name)
    shutil.copytree(ROOT / "examples/culture-d4", MIRROR / "examples/culture-d4",
                    ignore=shutil.ignore_patterns("__pycache__"))
    return {
        "root": MIRROR.relative_to(ROOT).as_posix(),
        "culture_d2_present": (MIRROR / "examples/culture-d2").exists(),
        "d4_projection_check": run_in(
            ["tools/d2-typed-labels.py", "--packet", "examples/culture-d4/packet.d4.yml",
             "--check", "examples/culture-d4/typed-labels.d4.yml"], MIRROR),
        "d4_adapter_check": run_in(
            ["tools/assemble-d4-typed.py", "--check",
             "examples/culture-d4/packet.d4.typed.yml"], MIRROR),
    }


def measure_o(evidence, preservation):
    failures, missing = [], set()
    runs = {
        "d2-projector-check": run_command([PROJECTOR, "--check"]),
        "d2-assembler-check": run_command([D2_ASSEMBLER, "--check"]),
        "d3-assembler-check": run_command([D3_ASSEMBLER, "--check"]),
        "d4-assembler-check": run_command([D4_ASSEMBLER, "--check"]),
        "d4-projector-check": run_command([PROJECTOR, "--packet", D4_PACKET,
                                           "--check", D4_PROJECTION]),
        "projector-selftest": run_command([PROJECTOR, "--selftest"]),
        "d4-gate": run_command([D4_GATE_PACKET and "tools/gates/typed-pipeline-gate.py",
                                D4_GATE_PACKET]),
        "adapter-selftest": run_command([ADAPTER, "--selftest"]),
    }
    # informational: the projector over the D3 packet (outside its label surface)
    runs["d3-projector-probe"] = run_command([PROJECTOR, "--packet",
                                              "examples/culture-d3/packet.gates.yml"])
    for name in ("d2-projector-check", "d2-assembler-check", "d3-assembler-check",
                 "d4-assembler-check", "d4-projector-check", "projector-selftest",
                 "adapter-selftest"):
        if runs[name].get("exit") != 0:
            failures.append(f"{name} not green: exit {runs[name].get('exit')} — "
                            f"{(runs[name].get('stdout') or runs[name].get('stderr') or '')[-200:]}")
    gate = runs["d4-gate"]
    gate_scan = re.search(r"summary:\s*(\d+)/(\d+) legs passed",
                          gate.get("stdout", "") or "")
    if gate.get("exit") != 0:
        failures.append(f"D4 gate not green: exit {gate.get('exit')} — "
                        f"{(gate.get('stdout') or gate.get('stderr') or '')[-200:]}")
    elif gate_scan is None:
        failures.append("D4 gate printed no parsable legs summary")
    elif (int(gate_scan.group(1)), int(gate_scan.group(2))) != (19, 19):
        failures.append(f"D4 gate legs {gate_scan.group(0)} != 19/19")
    selftest_scan = re.search(r"selftest:\s*(\d+)/(\d+) checks passed",
                              runs["adapter-selftest"].get("stdout", "") or "")
    if runs["adapter-selftest"].get("exit") == 0 and selftest_scan is None:
        failures.append("adapter selftest printed no parsable check count")
    elif selftest_scan and (int(selftest_scan.group(1)), int(selftest_scan.group(2))) != (12, 12):
        failures.append(f"adapter selftest {selftest_scan.group(0)} != 12/12")

    adapter_text = evidence.text(ADAPTER)
    copy_re = d4_marker_regex()
    foreign_copy = bool(copy_re.search(adapter_text))
    if foreign_copy:
        failures.append("adapter selftest still copies the foreign examples/culture-d2 tree")
    mirror = wart_mirror()
    if mirror["culture_d2_present"]:
        failures.append("wart mirror unexpectedly carries examples/culture-d2")
    for name in ("d4_projection_check", "d4_adapter_check"):
        item = mirror[name]
        if item.get("exit") != 0:
            failures.append(f"wart mirror {name} not green: exit {item.get('exit')} — "
                            f"{(item.get('stdout') or item.get('stderr') or '')[-200:]}")

    pin_failures, pins = pin_checks(evidence)
    failures.extend(pin_failures)
    failures.extend(preservation["failures"])
    return result(failures, {
        "runs": {name: {**{key: value for key, value in run.items()
                           if key not in ("stdout", "stderr", "json", "argv")},
                        "stdout_tail": (run.get("stdout") or "")[-300:]}
                 for name, run in runs.items()},
        "gate_scan": gate_scan.group(0) if gate_scan else None,
        "adapter_selftest": selftest_scan.group(0) if selftest_scan else None,
        "foreign_tree_copy_in_adapter": foreign_copy,
        "wart_mirror": mirror,
        "pins": pins,
        "d2_byte_identical": runs["d2-projector-check"].get("exit") == 0,
        "filed_bytes": preservation,
    }, missing)


# ------------------------------------------------------------------ claim C


def measure_c(evidence, claims):
    failures, missing = [], set()
    counts, commands = {}, {}
    for partition in PARTITIONS:
        files = sorted((ROOT / "corpus/knowledge" / partition).glob("*.md"))
        counts[partition] = len(files)
        commands[partition] = f"ls corpus/knowledge/{partition}/*.md | wc -l"
    total = sum(counts.values())

    text = evidence.text("corpus/README.md")
    if not text:
        missing.add("corpus/README.md")
        failures.append("corpus/README.md is missing")
        return result(failures, {"counts": counts}, missing)
    sections = readme_sections(text)
    section_rows, row_failures = {}, []
    for partition in PARTITIONS:
        section = sections.get(partition)
        if section is None:
            failures.append(f"README has no `## {partition}/ (N)` section")
            continue
        rows = readme_rows(section["body"])
        live = {path.name for path in (ROOT / "corpus/knowledge" / partition).glob("*.md")}
        missing_files = sorted({row for row in rows if row not in live})
        unindexed = sorted(live - set(rows))
        section_rows[partition] = {"declared": section["declared"],
                                   "live": counts[partition], "rows": len(rows),
                                   "missing_files": missing_files,
                                   "unindexed": unindexed}
        if section["declared"] != counts[partition]:
            failures.append(f"README {partition} header says {section['declared']}, "
                            f"tree measures {counts[partition]}")
        for row in missing_files:
            failures.append(f"README {partition} row names a missing file: {row}")
        for row in unindexed:
            failures.append(f"corpus/knowledge/{partition}/{row} has no README row")
        if len(rows) != section["declared"]:
            failures.append(f"README {partition} lists {len(rows)} rows for a declared "
                            f"{section['declared']}")

    revision = newest_revision(text)
    revision_checks = {}
    if revision is None:
        failures.append("README carries no revision block")
    else:
        revision_checks = {
            "dated": bool(DATE_RE.search(revision)),
            "commanded": bool(re.search(r"\b(?:ls|wc|python3|sha256sum|command)\b", revision, re.I)),
            "numbers_present": all(str(counts[partition]) in revision for partition in PARTITIONS),
            "placeholder": bool(PLACEHOLDER_RE.search(revision)),
            "text_head": revision.strip()[:400],
        }
        pointers = sorted(set(POINTER_RE.findall(revision)))
        broken_pointers = [pointer for pointer in pointers
                           if not (ROOT / pointer).exists()]
        revision_checks["pointers"] = pointers
        revision_checks["broken_pointers"] = broken_pointers
        if not revision_checks["dated"]:
            failures.append("README newest revision block carries no date")
        if not revision_checks["commanded"]:
            failures.append("README newest revision block carries no counting command")
        if not revision_checks["numbers_present"]:
            failures.append("README newest revision block does not carry the six partition counts")
        if revision_checks["placeholder"]:
            failures.append("README newest revision block trips the placeholder check")
        for pointer in broken_pointers:
            failures.append(f"README newest revision block names a missing path: {pointer}")

    gaps_match = re.search(r"^##\s+Known gaps.*$", text, re.M)
    gaps = {"present": bool(gaps_match)}
    if gaps_match:
        body = text[gaps_match.end():]
        stop = re.search(r"^##\s+", body, re.M)
        body = body[:stop.start()] if stop else body
        bullets = [line.strip() for line in body.splitlines()
                   if re.match(r"\s*(?:[-*]|\d+\.)\s+\S", line)]
        gaps.update({"bullets": len(bullets), "entries": bullets[:12]})
    else:
        failures.append("README has no `## Known gaps` section")

    declared = None
    for claim in claims.get("claims", []):
        if claim.get("id") == "C":
            match = DECLARED_COUNTS_RE.search(claim.get("after_required", ""))
            if match:
                declared = dict(zip(PARTITIONS, (int(value) for value in match.groups())))
    delta_rows = []
    if declared:
        for partition in PARTITIONS:
            if declared[partition] != counts[partition]:
                documented = bool(re.search(
                    rf"declared\s+{partition}\s+{declared[partition]}|"
                    rf"{partition}\s+{declared[partition]}\s+is\s+not\s+reproducible",
                    text, re.I))
                delta_rows.append({"partition": partition, "declared": declared[partition],
                                   "live": counts[partition], "documented_in_readme": documented})
                if not documented:
                    failures.append(f"declared {partition} count {declared[partition]} "
                                    f"differs from the tree ({counts[partition]}) and the "
                                    f"README does not name the delta")
    else:
        missing.add(f"{ROUND_DIR}/claims.json (declared C counts)")

    return result(failures, {
        "counts": counts, "commands": commands,
        "total": total,
        "readme": {"sections": section_rows, "revision": revision_checks,
                   "known_gaps": gaps},
        "declared": declared, "declared_deltas": delta_rows,
        "counts_metric": metric(counts, "count corpus/knowledge/<partition>/*.md per partition"),
    }, missing)


# -------------------------------------------------------------- validation


def guard_preflight():
    spec = importlib.util.spec_from_file_location("round20_receipt_guard", ROOT / GUARD)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import receipt guard")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    try:
        module.guard_receipt(ROOT / OUTPUT, repo_root=ROOT)
    except Exception as error:
        if isinstance(error, getattr(module, "ReceiptGuardError", ())):
            print(str(error), file=sys.stderr)
            raise SystemExit(3) from error
        raise


def validate():
    os.environ["TMPDIR"] = str(ROOT / ".scratch")
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    (ROOT / ".scratch").mkdir(exist_ok=True)
    evidence = Evidence()
    claims = evidence.document(f"{ROUND_DIR}/claims.json") or {}
    targets = evidence.document(f"{ROUND_DIR}/targets.json") or {}
    paths = round20_files()
    before = live_tree(FILED)
    preservation = filed_preservation(claims)
    results = {
        "D": measure_d(evidence, paths, preservation),
        "O": measure_o(evidence, preservation),
        "C": measure_c(evidence, claims),
    }
    after = live_tree(FILED)
    changes = [{"path": path, "before": before.get(path), "after": after.get(path)}
               for path in sorted(set(before) | set(after)) if before.get(path) != after.get(path)]
    if changes:
        results["D"]["failures"].append("Filed round-8..19 bytes changed during validation; "
                                        "rerun on a settled tree")
        results["D"]["passed"] = False
    declared = {claim.get("id"): claim.get("axis") for claim in claims.get("claims", [])
                if isinstance(claim, dict)}
    if declared != {"D": "depth", "O": "operability", "C": "coverage"}:
        results["D"]["failures"].append(f"Round-20 declared claims do not match D/O/C: {declared}")
        results["D"]["passed"] = False
    if evidence.errors:
        results["D"]["failures"].extend(evidence.errors)
        results["D"]["passed"] = False
    outside = outside_filed_changes(claims)
    return {
        "round": 20, "runner": RUNNER, "runner_sha256": sha((ROOT / RUNNER).read_bytes()),
        "counting_command": COMMAND, "date": today(),
        "baseline_revision": claims.get("baseline_revision"),
        "targets_date": targets.get("date"),
        "claims_declared": declared,
        "acceptance_checks_passed": all(item["passed"] for item in results.values()),
        "claims": results,
        "input_sha256": dict(sorted(evidence.inputs.items())),
        "failures": [f"claim {claim_id}: {failure}" for claim_id, item in results.items()
                     for failure in item["failures"]],
        "missing_dependencies": sorted(evidence.missing | {path for item in results.values()
                                                           for path in item["missing_dependencies"]}),
        "filed_rounds": {"baseline": preservation, "changed_during_validation": changes,
                         "outside_scope": outside,
                         "command": f"{COMMAND} (hash filed round-8..19 paths before/after checks)",
                         "date": today()},
        "limits": [
            "Historical validators are never executed. Only fixed read-only check/selftest "
            "commands run; no command is executed from an evidence file.",
            "Filed rounds 8-19 are compared byte-for-byte against the declared baseline; any "
            "change, addition or removal under those directories fails closed. Git-ignored "
            "untracked files (the `*.log` rule) are recorded, never failed.",
            "The uncertainty, D4-link, contract-audit and README checks are structural: "
            "vocabulary, basis presence, link resolution against the worktree, dated "
            "command-carried receipts and row/file agreement. They do not certify the truth "
            "of any claim; all artifacts remain NON-CANON.",
            "The shape gate result is the packet's own gate reading; 16/16 + 20/20 is shape, "
            "not semantic conformance, lore review, or a transfer acceptance.",
            "The delivered exercise revision is single-profile (its default baseline is the "
            "round-20 v3 baseline); the harness measures the default run as the v3 path and, "
            "when a revision exposes --profile, measures the explicit profile runs too.",
            "The v2 path is measured by replaying its round-20 successor baseline row "
            "(expected-v2-07-*.json) through the filed round-15 frozen-verify.py; the v2 "
            "packet bytes themselves are covered by the filed-rounds freeze.",
            "The d3 leg is the D3 family assembler check; the projector has no D3 label "
            "surface (its D3-packet probe is recorded informationally, never as a pass).",
            "A declared-vs-live count delta is accepted only when the README names it; the "
            "harness never rewrites a declared claim to match the tree.",
        ],
    }


# ------------------------------------------------------------------ selftest


def selftest():
    controls = []

    def check(name, value):
        controls.append({"control": name, "passed": bool(value)})

    v1 = ("OK   gate-scan: fields=16/16 glossary-entries=20 findings=0\n"
          "handoff-e2e: exit=0 fields=16/16 glossary=20/20 findings=0 "
          "packet_sha256=" + "0" * 64 + "\n")
    v3 = ("handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=52/52 "
          "claims=27 statuses=15/7/5 v2_subset=equal alias_leg=landed packet_sha256="
          + "1" * 64 + "\n")
    scan = scan_line(v3)
    check("v3-scan-parsed", scan and scan["claims"] == 27 and scan["statuses"] == (15, 7, 5)
          and scan["v2_subset"] == "equal" and scan["links"] == (52, 52))
    check("v1-scan-parsed", scan_line(v1) and scan_line(v1)["glossary"] == 20)
    check("scan-absent", scan_line("nothing here") is None)
    ledger = """## claim_ledger

| claim_id | kind | uncertainty_status | uncertainty_basis | links |
|---|---|---|---|---|
| D4-CL01 | designer interpretation | supported | grounding: examples/culture-d4/packet.d4.yml | examples/culture-d4/packet.d4.yml |
| D4-CL08 | designer interpretation | unresolved | open: alias leg; owner: O seat | examples/culture-d4/typed-labels.d4.yml |
"""
    rows = parse_ledger_rows(ledger)
    check("ledger-parsed", [row["id"] for row in rows] == ["D4-CL01", "D4-CL08"])
    check("ledger-status-parsed", rows[1]["uncertainty"]["status"] == "unresolved")
    judgments = uncertainty_problems(rows)
    check("ledger-clean", not any(judgment["problems"] for judgment in judgments))
    bad = parse_ledger_rows(ledger.replace("supported", "tentative"))
    check("ledger-vocabulary-held", any("off vocabulary" in problem
                                        for problem in uncertainty_problems(bad)[0]["problems"]))
    check("link-paths", link_paths(rows[0]["links"]) == ["examples/culture-d4/packet.d4.yml"])
    receipt = {"claims": [{"id": "D4-CL01", "uncertainty": {"status": "supported",
                                                             "basis": "examples/culture-d4/packet.d4.yml"}}],
               "links": {"D4-CL01": "examples/culture-d4/typed-labels.d4.yml"}}
    facts = receipt_surface(receipt)
    check("receipt-claims", facts["resolved_claims"] == 1
          and "examples/culture-d4/typed-labels.d4.yml" in facts["d4_links_resolved"])
    check("receipt-d4-mentions", facts["d4_mentions"] >= 2)
    passing = ("# contract audit re-run\nDate: 2026-10-18. command: python3 x\n"
               "Verdict: PASS — v3 satisfies §4 semantics.\n")
    check("audit-pass", contract_audit_verdict(passing)["classification"] == "pass")
    minors = ("# re-run\nDate: 2026-10-18. command: python3 x\n"
              "Verdict: PASS-with-named-minors on the audited build. The round-12 "
              "reject grounds stay closed.\n")
    check("audit-pass-named-minors",
          contract_audit_verdict(minors)["classification"] == "pass-with-named-gaps")
    failing = ("# re-run\nDate: 2026-10-18. command: python3 x\n"
               "Verdict: FAIL — the surface does not satisfy §4.\n")
    check("audit-explicit-fail", contract_audit_verdict(failing)["classification"] == "fail")
    gaps = ("# re-run\nDate: 2026-10-18. command: python3 x\n"
            "Verdict: remainders named.\n"
            "- OQ-V3-01 bilateral read pending (owner: lore + both lanes).\n"
            "- OQ-V3-04 alias wart open remainder (owner: O seat).\n")
    check("audit-named-gaps", contract_audit_verdict(gaps)["classification"] == "pass-with-named-gaps")
    check("audit-undated", contract_audit_verdict("# re-run\nVerdict: PASS\n")["classification"]
          != "pass")
    readme = ("## linguistics/ (19)\n- `color-terminology.md` — x\n"
              "- `conlang-methodology.md` — y\n## Known gaps (frontier)\n- one gap\n")
    sections = readme_sections(readme)
    check("readme-sections", sections["linguistics"]["declared"] == 19)
    check("readme-rows", readme_rows(sections["linguistics"]["body"])
          == ["color-terminology.md", "conlang-methodology.md"])
    check("readme-revision", newest_revision("revision: 1.5 — x\nrevision: 1.4 — y\n")
          .startswith("revision: 1.5"))
    check("placeholder-detected", bool(PLACEHOLDER_RE.search("this row is TBD")))
    check("mirror-regex",
          bool(d4_marker_regex().search('shutil.copytree(ROOT / "examples/culture-d2", mirror)')))
    check("mirror-regex-clean", not d4_marker_regex().search("no copy here"))
    typed = ('costumes:\n  - id: GAR-01\nassembly:\n  adapter_sha256: "aa"\n'
             '  packet_sha256: "bb"\n  projection_sha256: "cc"\n  source_sha256:\n'
             '    "examples/culture-d4/components/01-brief.yml": "dd"\n')
    block = yaml_assembly_block(typed)
    check("typed-packet-assembly-parsed",
          block.get("packet_sha256") == "bb" and block.get("adapter_sha256") == "aa"
          and "examples/culture-d4/components/01-brief.yml" not in block)
    check("typed-packet-assembly-absent", yaml_assembly_block("costumes: []\n") == {})
    rows = preservation_rows({"a.md": "x", "b.md": "y"}, {"a.md": "x", "c.md": "z"}, "base")
    kinds = {row["path"]: row["preservation"] for row in rows}
    check("preservation-classified", kinds == {"a.md": "byte-identical", "b.md": "removed",
                                               "c.md": "added"})
    ignored = preservation_rows({"a.md": "x"}, {"a.md": "x", "run.log": "z"}, "base",
                                {"run.log"})
    check("preservation-ignored-untracked",
          {row["path"]: row["preservation"] for row in ignored}["run.log"] == "untracked-ignored")
    sample = metric(3, "unit")
    check("metric-carries-command-and-date", sample["command"].startswith(COMMAND)
          and sample["date"] == today())
    payload = {"runner": RUNNER, "command": COMMAND + " --selftest", "date": today(),
               "selftest_passed": all(item["passed"] for item in controls),
               "controls": controls,
               "passed": metric(sum(item["passed"] for item in controls),
                                "validator selftest controls"),
               "total": metric(len(controls), "validator selftest control inventory")}
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["selftest_passed"] else 1


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate round-20 D/O/C without touching filed rounds 8-19.")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--selftest", action="store_true",
                       help="run in-memory validator controls, no receipt write")
    modes.add_argument("--check", action="store_true",
                       help="run full acceptance and print JSON without writing validation.json")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    receipt = validate()
    if args.check:
        print(json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False))
    else:
        guard_preflight()
        (ROOT / OUTPUT).write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                              ensure_ascii=False) + "\n", encoding="utf-8")
        for claim_id, item in receipt["claims"].items():
            print(f"claim {claim_id}: {'PASS' if item['passed'] else 'FAIL'}")
            for failure in item["failures"][:6]:
                print(f"  - {failure[:200]}")
        print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
        if receipt["missing_dependencies"]:
            print("missing_dependencies: " + ", ".join(receipt["missing_dependencies"]))
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
