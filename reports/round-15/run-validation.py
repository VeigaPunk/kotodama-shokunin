#!/usr/bin/env python3
"""Round-15 validator — closes the round-12 adjacency reject on the handoff packet.

Claim O (operability): handoff packet v2 (reports/round-15/handoff/packet-v2.*)
adds per-claim uncertainty {status, basis} with zero boilerplate and
claim-to-record links that resolve to real repo records; the shape gate still
reads 16/16 fields + 20/20 glossary entries; a durable builder with --selftest
and a frozen expected.json baseline exists; the round-12 contract audit re-run
over v2 yields a semantic PASS verdict or names remaining gaps with owner notes.

Claim D (depth): the label-uncertainty decision table draft exists with the
supported/partial/unresolved rules, the required basis field, a cross-reference
to the verification partition, and every rule cited to corpus paths or
round-12/15 artifacts.

Historical rounds 8-14 are compared byte-for-byte against the declared
baseline and must not change during validation. This runner writes only its
own receipt. It measures, it does not certify truth, canon, or lore receipt.
"""
from __future__ import annotations

import argparse
import ast
import collections
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-15"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
COMMAND = f"python3 {RUNNER}"
GUARD = "tools/harness/receipt_guard.py"
GATE = "tools/gates/handoff-packet-check.py"
PACKET_DIR = f"{ROUND_DIR}/handoff"
FILED = tuple(f"reports/round-{number}" for number in range(8, 15))
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}(?:T[\d:.]+Z?)?(?=\b|)")
POINTER_RE = re.compile(
    r"(?<![\w./-])(?:reports|tools|corpus|examples)/[\w./+-]+\.(?:json|md|py|ya?ml|tsv|txt|sh)\b"
    r"|(?<![\w./-])(?:SCORECARD|LOG|SHONEN|PROVINCE|SKILL|MINT|README)\.md\b")
STATUS_VOCAB = ("supported", "partial", "unresolved")
PLACEHOLDER_RE = re.compile(
    r"\b(tbd|tba|todo|n/?a|placeholder|boilerplate|same[- ]as[- ](?:above|below)|"
    r"as (?:above|below)|see (?:above|below|other)|copy of|unchanged)\b", re.I)
BASELINE_RE = re.compile(r"[0-9a-f]{40,64}")
PACKET_BASENAMES = ("packet-v2.yml", "packet-v2.md", "packet.yml", "packet.md")
EXCLUDE_NAMES = {"claims.json", "targets.json", "validation.json", "scope.md",
                 "run-validation.py"}


def today():
    return dt.date.today().isoformat()


def metric(value, operation):
    return {"value": value, "command": f"{COMMAND} ({operation})", "date": today()}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def safe_path(relative):
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or ".git" in path.parts:
        raise ValueError(f"not an in-lane evidence path: {relative}")
    resolved = (ROOT / path).resolve()
    if not resolved.is_relative_to(ROOT):
        raise ValueError(f"evidence path escapes lane: {relative}")
    return resolved


def strict_json(text):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    return json.loads(text, object_pairs_hook=pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(
                          ValueError(f"non-finite JSON number: {value}")))


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

    def pointers(self, text):
        records = []
        for relative in sorted(set(POINTER_RE.findall(text))):
            try:
                path = safe_path(relative)
                if path.is_file():
                    data = path.read_bytes()
                    self.inputs[relative] = sha(data)
                    records.append({"path": relative, "sha256": sha(data), "exists": True})
                else:
                    records.append({"path": relative, "exists": False})
            except (OSError, ValueError) as error:
                records.append({"path": relative, "exists": False, "error": str(error)})
        return records


def result(failures, measurement, missing=()):
    return {"passed": not failures, "failures": failures,
            "measurement": measurement, "missing_dependencies": sorted(set(missing))}


def run_command(parts, timeout=300, env=None):
    argv = [sys.executable, *parts]
    child_env = dict(os.environ if env is None else env)
    child_env.update(TMPDIR=str(ROOT / ".scratch"), PYTHONDONTWRITEBYTECODE="1")
    item = {"command": shlex.join(["python3", *parts]), "date": today(),
            "argv": ["python3", *parts]}
    try:
        source = safe_path(parts[0])
        item["source_sha256_before"] = sha(source.read_bytes())
        run = subprocess.run(argv, cwd=ROOT, capture_output=True,
                             timeout=timeout, env=child_env)
        item["source_sha256_after"] = sha(source.read_bytes())
        item["source_unchanged"] = item["source_sha256_before"] == item["source_sha256_after"]
        item.update(exit=run.returncode if item["source_unchanged"] else None,
                    stdout_sha256=sha(run.stdout), stderr_sha256=sha(run.stderr),
                    stdout_tail=run.stdout.decode("utf-8", "replace")[-1000:],
                    stderr_tail=run.stderr.decode("utf-8", "replace")[-1000:])
        try:
            item["json"] = strict_json(run.stdout.decode("utf-8"))
        except (ValueError, UnicodeError):
            pass
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        item.update(exit=None, error=str(error), timeout=isinstance(error, subprocess.TimeoutExpired))
    return item


def git(*args, data=None):
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1", LC_ALL="C")
    proc = subprocess.run(["git", "--literal-pathspecs", *args], cwd=ROOT,
                          input=data, capture_output=True, timeout=90, env=env)
    if proc.returncode:
        raise ValueError(f"git {shlex.join(args)}: {proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout


def json_extends(old, new):
    if isinstance(old, dict):
        return isinstance(new, dict) and all(
            key in new and json_extends(value, new[key]) for key, value in old.items())
    if isinstance(old, list):
        return isinstance(new, list) and len(new) >= len(old) and all(
            json_extends(value, new[index]) for index, value in enumerate(old))
    return type(old) is type(new) and old == new


def preservation_kind(relative, old, new):
    if old == new:
        return "byte-identical"
    if new.startswith(old):
        if relative.endswith(".json"):
            try:
                strict_json(new.decode("utf-8"))
            except (ValueError, UnicodeError):
                return "violation"
        return "append-only"
    if relative.endswith(".json"):
        try:
            unchanged_values = json_extends(strict_json(old.decode("utf-8")),
                                            strict_json(new.decode("utf-8")))
            remaining = iter(new)
            if unchanged_values and all(byte in remaining for byte in old):
                return "append-only-json-entries"
        except (ValueError, UnicodeError):
            pass
    return "violation"


def filed_snapshot():
    snapshot = {}
    for directory in FILED:
        base = ROOT / directory
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                relative = path.relative_to(ROOT).as_posix()
                try:
                    snapshot[relative] = sha(safe_path(relative).read_bytes())
                except (OSError, ValueError) as error:
                    snapshot[relative] = f"ERROR: {error}"
    return snapshot


def filed_preservation(baseline):
    failures, rows = [], []
    try:
        if not isinstance(baseline, str) or not BASELINE_RE.fullmatch(baseline):
            raise ValueError("claims.json has no full baseline revision")
        entries = []
        for record in git("ls-tree", "-r", "-z", baseline, "--", *FILED).split(b"\0"):
            if not record:
                continue
            metadata, raw_path = record.split(b"\t", 1)
            mode, kind, oid = metadata.split()
            if kind != b"blob" or mode not in (b"100644", b"100755"):
                raise ValueError(f"non-regular filed entry: {raw_path!r}")
            entries.append((raw_path.decode("utf-8"), oid))
        if not entries:
            raise ValueError("no filed round-8..14 blobs at the declared baseline")
        objects = git("cat-file", "--batch", data=b"".join(oid + b"\n" for _, oid in entries))
        offset = 0
        for relative, oid in entries:
            end = objects.index(b"\n", offset)
            header = objects[offset:end].split()
            if len(header) != 3 or header[0] != oid or header[1] != b"blob":
                raise ValueError(f"unexpected Git blob reply for {relative}")
            size = int(header[2])
            old = objects[end + 1:end + 1 + size]
            offset = end + size + 2
            try:
                new = safe_path(relative).read_bytes()
                disposition = preservation_kind(relative, old, new)
            except (OSError, ValueError) as error:
                new, disposition = b"", "violation"
                failures.append(f"Filed artifact unreadable: {relative}: {error}")
            rows.append({"path": relative, "baseline_sha256": sha(old),
                         "current_sha256": sha(new), "preservation": disposition})
            if disposition == "violation":
                failures.append(f"Filed bytes changed other than append-only: {relative}")
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        failures.append(f"Cannot establish filed-byte preservation: {error}")
    return result(failures, {"baseline_revision": baseline, "files": rows,
                            "checked": metric(len(rows), "compare baseline Git blobs with filed worktree bytes"),
                            "violations": metric(sum(row["preservation"] == "violation" for row in rows),
                                                 "count non-append-only filed changes")})


# ---------------------------------------------------------------- packet v2


def find_packet(evidence):
    """The v2 packet: final names first, then the highest packet-attempt pair."""
    directory = ROOT / PACKET_DIR
    markdown = source = None
    if directory.is_dir():
        def rank(name):
            attempt = re.search(r"(\d+)", name)
            final = 0 if re.fullmatch(r"packet(?:-v2)?\.(?:md|ya?ml)", name) else 1
            return (final, 0 if "-v2" in name else 1,
                    -int(attempt.group(1)) if attempt else 0,
                    0 if name.endswith(".md") else 1, name)
        candidates = sorted((path for path in directory.iterdir()
                             if path.is_file()
                             and re.match(r"packet[\w.-]*\.(?:md|ya?ml)$", path.name)
                             and "shard" not in path.name), key=lambda path: rank(path.name))
        for candidate in candidates:
            relative = candidate.relative_to(ROOT).as_posix()
            evidence.text(relative)
            if candidate.suffix == ".md" and markdown is None:
                markdown = relative
            elif candidate.suffix in (".yml", ".yaml") and source is None:
                source = relative
            if markdown and source:
                break
    return markdown, source


def parse_claim_ledger(text):
    """Extract claim rows from a v2 packet (markdown table or YAML-ish blocks).

    Each row: {id, format, uncertainty: {status, basis} | None, links, raw}.
    """
    rows = []
    lines = text.splitlines()
    section_start = None
    for index, line in enumerate(lines):
        if re.match(r"#{1,6}\s", line) and "claim_ledger" in line.lower().replace(" ", "_").replace(" ", "_"):
            section_start = index + 1
            break
    if section_start is not None:
        end = len(lines)
        for index in range(section_start, len(lines)):
            if re.match(r"#{1,6}\s", lines[index]) and not lines[index].lstrip("#").strip().lower().startswith("claim"):
                end = index
                break
        body = lines[section_start:end]
        separator_rows = [line for line in body if line.strip().startswith("|")
                          and set(line.replace("|", "").strip()) <= set("-: ")]
        header = None
        if separator_rows:
            separator_index = body.index(separator_rows[0])
            for line in reversed(body[:separator_index]):
                if line.strip().startswith("|"):
                    header = [cell.strip().lower()
                              for cell in line.strip().strip("|").split("|")]
                    break
        if header is None:
            for line in body:
                if line.strip().startswith("|"):
                    header = [cell.strip().lower() for cell in line.strip().strip("|").split("|")]
                    break
        if header:
            separator_seen = False
            status_index = next((i for i, name in enumerate(header)
                                 if "uncertainty_status" in name
                                 or name.strip() == "uncertainty status"), None)
            basis_index = next((i for i, name in enumerate(header)
                                if "uncertainty_basis" in name
                                or name.strip() == "uncertainty basis"), None)
            legacy_index = next((i for i, name in enumerate(header)
                                 if "uncertainty" in name
                                 and i not in (status_index, basis_index)), None)
            links_index = next((i for i, name in enumerate(header)
                                if name.strip().rstrip("s") == "link"), None)
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
                raw = stripped
                uncertainty = None
                if status_index is not None and status_index < len(cells):
                    status = re.search(r"\b(supported|partial|unresolved)\b",
                                       cells[status_index], re.I)
                    basis = cells[basis_index] if basis_index is not None \
                        and basis_index < len(cells) else ""
                    uncertainty = ({"status": status.group(1).lower(),
                                    "basis": basis.strip().strip("**")} if status
                                   else {"status": None, "basis": basis.strip()})
                elif legacy_index is not None and legacy_index < len(cells):
                    uncertainty = parse_uncertainty_cell(cells[legacy_index])
                row = {"id": cells[0], "format": "markdown-table",
                       "uncertainty": uncertainty, "raw": raw,
                       "link_refs": cells[links_index] if links_index is not None
                       and links_index < len(cells) else ""}
                rows.append(row)
            if rows:
                for row in rows:
                    row.setdefault("raw", "")
                return rows
    block = None
    for line in lines:
        match = re.match(r"\s*-?\s*(?:claim_id|id):\s*(\S+)", line)
        if match:
            if block:
                rows.append(block)
            block = {"id": match.group(1), "format": "yaml-block",
                     "lines": [line], "uncertainty": None, "raw": "", "link_refs": ""}
            continue
        if block is not None:
            if re.match(r"\S", line) and not line.startswith((" ", "-", "#")):
                rows.append(block)
                block = None
                continue
            block["lines"].append(line)
            status = re.search(r"\bstatus:\s*(supported|partial|unresolved)\b", line, re.I)
            basis = re.search(r"\bbasis:\s*(.+?)\s*$", line)
            links = re.match(r"\s*links:\s*(.+?)\s*$", line)
            if links:
                block["link_refs"] = links.group(1).strip().strip("\"'")
            if status and isinstance(block.get("uncertainty"), dict):
                block["uncertainty"]["status"] = status.group(1).lower()
            elif status:
                block["uncertainty"] = {"status": status.group(1).lower(), "basis": ""}
            if basis and isinstance(block.get("uncertainty"), dict):
                block["uncertainty"]["basis"] = basis.group(1).strip().strip("\"'")
    if block:
        rows.append(block)
    for row in rows:
        if "raw" not in row or not row["raw"]:
            row["raw"] = "\n".join(row.get("lines", []))
    return rows


def parse_uncertainty_cell(cell):
    """Parse one markdown uncertainty cell: status vocabulary + basis text."""
    status = re.search(r"\b(supported|partial|unresolved)\b", cell, re.I)
    if not status:
        return None
    rest = cell[:status.start()] + cell[status.end():]
    rest = rest.replace("**", "").strip(" `:;-—")
    basis = rest
    match = re.search(r"basis\s*[:\-—]\s*(.+)", rest, re.I)
    if match:
        basis = match.group(1).strip()
    return {"status": status.group(1).lower(), "basis": basis.strip()}


ARTIFACT_REF_RE = re.compile(r"\b([A-Z]+-\d+)\b")


def parse_manifest(text):
    """artifact_manifest rows -> {id: {"path": str, "sha256": str|None}}."""
    manifest = {}
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if re.match(r"#{1,6}\s", line) and "artifact_manifest" in line.lower().replace(" ", "_"):
            start = index + 1
            break
    if start is None:
        return manifest
    for line in lines[start:]:
        if re.match(r"#{1,6}\s", line):
            break
        stripped = line.strip()
        if not stripped.startswith("|"):
            if manifest:
                break
            continue
        cells = [cell.strip().strip("`") for cell in stripped.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", cell) for cell in cells if cell):
            continue
        if not cells or not ARTIFACT_REF_RE.fullmatch(cells[0].split("#")[0]):
            continue
        paths = POINTER_RE.findall(stripped)
        digest = re.search(r"\b([0-9a-f]{64})\b", stripped)
        manifest[cells[0].split("#")[0]] = {"path": paths[0] if paths else None,
                                            "sha256": digest.group(1) if digest else None}
    return manifest


def row_links(row):
    found = set(POINTER_RE.findall(row["raw"]))
    found.update(re.findall(r"\b[A-Z]+-\d+(?:#[\w.\[\]-]+)?",
                            row.get("link_refs", "") or ""))
    return sorted(found)


def manifest_path(ref, manifest):
    entry = manifest.get(ref.split("#", 1)[0])
    return entry.get("path") if entry else None


def uncertainty_audit_rows(claims):
    """Judge per-claim uncertainty population and return per-claim verdict rows."""
    judgments = []
    seen_bases = collections.Counter()
    for claim in claims:
        uncertainty = claim.get("uncertainty")
        entry = {"claim": claim["id"], "status": None, "basis_cited": False,
                 "links": row_links(claim), "resolved_links": [],
                 "problems": []}
        if uncertainty is None:
            entry["problems"].append("no uncertainty dimension")
        else:
            entry["status"] = uncertainty.get("status")
            basis = (uncertainty.get("basis") or "").strip()
            if entry["status"] not in STATUS_VOCAB:
                entry["problems"].append(f"status off vocabulary: {entry['status']!r}")
            if not basis:
                entry["problems"].append("empty basis")
            elif PLACEHOLDER_RE.search(basis):
                entry["problems"].append(f"placeholder basis: {basis!r}")
            elif not (POINTER_RE.search(basis) or re.search(r":\d+", basis)
                      or re.search(r"\bgrounding\s*:", basis, re.I)
                      or ARTIFACT_REF_RE.search(basis)):
                entry["problems"].append("basis names no location")
            else:
                entry["basis_cited"] = True
            entry["basis"] = basis
            seen_bases[re.sub(r"\s+", " ", basis).lower()] += 1
        judgments.append(entry)
    duplicates = [basis for basis, count in seen_bases.items() if count > 1 and basis]
    for judgment in judgments:
        basis = judgment.get("basis", "")
        if basis and re.sub(r"\s+", " ", basis).lower() in duplicates:
            judgment["problems"].append("boilerplate basis repeated on multiple claims")
    return judgments


def resolve_links(judgments, evidence, packet_relative, manifest):
    """Claim-to-record links must resolve to real repo records, not the packet."""
    failures = []
    for judgment in judgments:
        resolved = []
        for ref in judgment["links"]:
            relative = manifest_path(ref, manifest) if re.match(
                r"^[A-Z]+-\d+(#|$)", ref) else ref
            if relative is None:
                continue
            try:
                path = safe_path(relative)
                exists = path.is_file()
            except ValueError:
                exists = False
            if exists:
                evidence.text(relative)
                resolved.append(relative)
        judgment["resolved_links"] = resolved
        records = [item for item in resolved if item != packet_relative
                   and not item.startswith(PACKET_DIR + "/")]
        if not records:
            failures.append(f"claim {judgment['claim']}: no claim-to-record link resolves "
                            f"to a real repo record (links: {judgment['links'] or 'none'})")
    return failures


def gate_scan(stdout):
    match = re.search(r"INFO scan: fields=(\d+)/(\d+) glossary-entries=(\d+) findings=(\d+)",
                      stdout)
    if not match:
        return None
    return {"fields": int(match.group(1)), "fields_total": int(match.group(2)),
            "glossary_entries": int(match.group(3)), "findings": int(match.group(4))}


def contract_audit_verdict(text):
    """Classify a contract-audit re-run: pass / pass-with-named-gaps / fail."""
    dated = bool(DATE_RE.search(text))
    commanded = bool(re.search(r"\b(?:python3?|git|sha256sum|command)\b", text, re.I))
    label = r"(?:verdict|overall|conclusion|result)"
    entries = [(match.start(), match.group(1)) for match in re.finditer(
        rf"(?im)^\s*(?:[-*]\s+)?(?:\*\*)?{label}(?:\*\*)?\s*[:—-]\s*(.+?)\s*(?:\*\*)?$", text)]
    verdict_value = entries[-1][1].strip() if entries else ""
    if re.search(r"\b(?:pass|green)\b", verdict_value, re.I) and not re.search(
            r"\b(?:not\s+|un)\s*pass|\breject|\bfail", verdict_value, re.I):
        state = "pass"
    else:
        state = "other"
    gap_items = []
    for line in text.splitlines():
        if re.search(r"\bgap\b|\bremaining\b|\bopen\b|\bblocker\b|\bpending\b", line, re.I) \
                and re.match(r"\s*(?:[-*]|\d+\.)\s+", line):
            gap_items.append(line.strip())
    owned_gaps = [item for item in gap_items
                  if re.search(r"\bowner\b|owner:\s*\S|responsible[:\s]", item, re.I)]
    named_gaps = bool(gap_items) and len(owned_gaps) >= max(1, len(gap_items))
    if state == "pass" and dated and commanded:
        classification = "pass"
    elif named_gaps and dated and commanded:
        classification = "pass-with-named-gaps"
    elif not dated or not commanded:
        classification = "unparseable"
    else:
        classification = "fail"
    return {"classification": classification, "dated": dated, "commanded": commanded,
            "verdict": verdict_value, "gap_items": gap_items,
            "owned_gaps": owned_gaps}


# ------------------------------------------------------------- discoveries


def round15_files():
    base = ROOT / ROUND_DIR
    if not base.is_dir():
        return []
    return [path.relative_to(ROOT).as_posix() for path in sorted(base.rglob("*"))
            if path.is_file() and "__pycache__" not in path.parts
            and Path(path).name not in EXCLUDE_NAMES]


def discover(paths, name_pattern, content_pattern, suffixes=(".md", ".json")):
    """Deterministic candidate list: name matches first, then content matches."""
    name_re = re.compile(name_pattern, re.I)
    content_re = re.compile(content_pattern, re.I)
    named, content = [], []
    for relative in paths:
        if not relative.endswith(suffixes):
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


def builder_source(relative):
    try:
        return (ROOT / relative).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def builder_invocations(relative, packet_relative):
    """Derive (selftest_argv, receipt_argv) from the tool's own CLI surface."""
    source = builder_source(relative)
    selftest_argv = (relative, "--selftest")
    if "--packet" in source and packet_relative:
        receipt_argv = (relative, "--packet", packet_relative,
                        "--json" if "--json" in source else "-")
        if "--json" not in source:
            receipt_argv = (relative, "--packet", packet_relative)
    else:
        receipt_argv = (relative,)
    return selftest_argv, receipt_argv


def pick_builder(paths):
    """The durable v2 builder: --selftest flag and a packet-v2/expected.json tie."""
    candidates = []
    for relative in paths:
        if not relative.endswith(".py"):
            continue
        name = Path(relative).name
        if relative.startswith("tools/gates/") or re.search(
                r"check|audit|verify|review|guard|replay|validation", name, re.I):
            continue
        try:
            source = (ROOT / relative).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "--selftest" not in source:
            continue
        try:
            ast.parse(source)
        except SyntaxError:
            continue
        ties_v2 = bool(re.search(r"packet[-_ ]?v2|packet-v2\.(?:yml|md)", source, re.I))
        ties_semantics = relative.startswith("tools/harness/") and bool(
            re.search(r"uncertainty|claim.to.record|claim_ledger|record links|record_links",
                      source, re.I))
        if ties_v2 or ties_semantics:
            candidates.append(relative)
    return sorted(candidates, key=lambda item: (len(item), item))


def find_expected_baseline(paths, builder_relative):
    directory = ROOT / PACKET_DIR
    for name in ("expected.json", "packet-v2.expected.json"):
        candidate = directory / name
        if candidate.is_file():
            return candidate.relative_to(ROOT).as_posix()
    if builder_relative:
        try:
            source = (ROOT / builder_relative).read_text(encoding="utf-8", errors="replace")
        except OSError:
            return None
        for match in re.finditer(r"([\w./-]*expected\.json)", source):
            candidate = match.group(1)
            if (ROOT / candidate).is_file():
                return candidate
    for relative in paths:
        if relative.startswith(PACKET_DIR + "/") and relative.endswith("expected.json"):
            return relative
    return None


def measure_o(evidence, paths, packet_md, packet_src, builder, expected, gate_run,
              builder_selftests, builder_receipts, preservation, d_draft=None):
    failures = []
    claims = []
    packet_relative = packet_md or packet_src
    if packet_relative:
        claims = parse_claim_ledger(evidence.text(packet_relative))
    if not packet_relative:
        failures.append(f"Handoff packet v2 is missing under {PACKET_DIR}/ "
                        "(no packet*.md|yml document found)")
    if packet_relative and not claims:
        failures.append(f"No claim_ledger rows parsed from {packet_relative}")

    # (a) per-claim uncertainty, zero boilerplate
    judgments = uncertainty_audit_rows(claims)
    for judgment in judgments:
        for problem in judgment["problems"]:
            failures.append(f"claim {judgment['claim']}: {problem}")
    coverage = metric(sum(1 for item in judgments
                          if item["status"] in STATUS_VOCAB and item["basis_cited"]),
                      "claims with populated status and cited basis")
    total = metric(len(judgments), "claim_ledger rows in packet v2")

    # (b) claim-to-record links resolve (repo paths and A-NN manifest refs)
    if packet_relative and claims:
        failures.extend(resolve_links(judgments, evidence, packet_relative,
                                      parse_manifest(evidence.text(packet_relative))))
    resolved = metric(sum(1 for item in judgments if item["resolved_links"]),
                      "claims with at least one resolving record link")

    # uncertainty audit artifact (per audit); builder boilerplate controls count
    audit_paths = []
    for relative in paths:
        if not relative.endswith((".md", ".json")) or relative == d_draft:
            continue
        if not re.search(r"audit|review|verify|rerun", Path(relative).name, re.I):
            continue
        try:
            audit_text = (ROOT / relative).read_text(encoding="utf-8", errors="replace")[:40000]
        except OSError:
            continue
        if re.search(r"uncertainty|boilerplate", audit_text, re.I):
            audit_paths.append(relative)
    audits = [receipt_state(evidence, relative) for relative in audit_paths]
    audits = [item for item in audits if item]
    audit_green = [item for item in audits if item["green"]]
    builder_pass = {}
    expected_payload = evidence.document(expected) if expected else None
    sources = [("expected_baseline", expected_payload or {})]
    sources += [("receipt:" + entry["tool"], entry["run"].get("json") or {})
                for entry in builder_receipts]
    if builder:
        for source_name, source in sources:
            keys = [key for key in source if re.search(
                r"boilerplate|basis[._-]?unique|unique[._-]?basis|status[._-]?histogram",
                key, re.I)]
            if keys and all(source[key] is not False for key in keys):
                builder_pass[source_name] = keys
    if not audits and not builder_pass:
        failures.append(f"No uncertainty-population audit receipt found in {ROUND_DIR}/ "
                        "(non-boilerplate per audit is unproven)")
    elif audits and not audit_green and not builder_pass:
        failures.append("Uncertainty audit receipt is not a dated, command-carried green result: "
                        + ", ".join(item["path"] for item in audits))
    blocked_rerun = None
    rerun_relative = f"{ROUND_DIR}/rerun.json"
    rerun_payload = evidence.document(rerun_relative)
    if isinstance(rerun_payload, dict) and re.search(
            r"blocked|missing", str(rerun_payload.get("status", "")), re.I):
        blocked_rerun = {"path": rerun_relative,
                         "status": rerun_payload.get("status"),
                         "note": "an independent seat's rerun journal records the same "
                                 "missing-integration state; it is corroboration, not the audit"}

    # shape gate 16/16 + 20/20
    scan = gate_scan(gate_run.get("stdout_tail", "") if gate_run else "")
    if gate_run is None or gate_run.get("exit") is None:
        failures.append("Shape gate did not run (packet missing or unreadable)")
    elif gate_run.get("exit") != 0:
        detail = (gate_run.get("stdout_tail", "") + " "
                  + gate_run.get("stderr_tail", "")).strip()
        failures.append(f"Shape gate not clean: {gate_run.get('command')} exit "
                        f"{gate_run.get('exit')} — {detail[:280]}")
    if scan is None:
        if gate_run and gate_run.get("exit") == 0:
            failures.append("Shape gate produced no parsable scan line")
    else:
        if (scan["fields"], scan["fields_total"]) != (16, 16):
            failures.append(f"Shape gate fields {scan['fields']}/{scan['fields_total']} != 16/16")
        if scan["glossary_entries"] != 20 or scan["findings"] != 0:
            failures.append(f"Shape gate glossary {scan['glossary_entries']} entries with "
                            f"{scan['findings']} findings != 20/20 clean")
    scan_metric = {"value": scan,
                   "command": gate_run.get("command") if gate_run else f"python3 {GATE} <packet>",
                   "date": today()}

    # durable builder with selftest + frozen expected.json baseline
    if not builder:
        failures.append(f"No durable packet builder discovered (a .py with --selftest "
                        f"referencing packet-v2/expected.json under tools/ or {ROUND_DIR}/)")
    else:
        for run in builder_selftests:
            payload = run.get("json") or {}
            if run.get("exit") != 0 or payload.get("selftest_passed") is False:
                failures.append(f"Builder selftest not green: {run.get('command')} exit "
                                f"{run.get('exit')}")
        if len(builder_selftests) >= 2 and builder_selftests[0].get("stdout_sha256") != \
                builder_selftests[1].get("stdout_sha256"):
            failures.append("Builder selftest is not deterministic across two runs")
        for entry in builder_receipts:
            run = entry["run"]
            if run.get("exit") != 0:
                failures.append(f"Builder run not clean over v2: {entry['tool']} → "
                                f"{run.get('command')} exit {run.get('exit')} — "
                                f"{(run.get('stderr_tail') or run.get('stdout_tail') or '')[:160]}")
    builder_metric = {"candidates": builder,
                      "selftests": [{"command": run.get("command"), "exit": run.get("exit"),
                                     "date": run.get("date"),
                                     "selftest_passed": (run.get("json") or {}).get("selftest_passed")}
                                    for run in builder_selftests],
                      "receipts": [{"tool": entry["tool"], "command": entry["run"].get("command"),
                                    "exit": entry["run"].get("exit"), "date": entry["run"].get("date"),
                                    "summary": entry["run"].get("stdout_tail", "")[:300]}
                                   for entry in builder_receipts]}
    if expected:
        payload = expected_payload
        if payload is None:
            failures.append(f"Frozen baseline {expected} is not strict JSON")
        else:
            text = json.dumps(payload, ensure_ascii=False, sort_keys=True)
            dated = bool(DATE_RE.search(text))
            digest = payload.get("packet_sha256") or payload.get("sha256")
            if not dated:
                failures.append(f"Frozen baseline {expected} carries no freeze date")
            if not any(key in payload for key in ("packet_sha256", "sha256", "digests",
                                                  "expected_scan", "counts")):
                failures.append(f"Frozen baseline {expected} pins no packet values")
            if isinstance(digest, str) and packet_relative:
                actual = sha(safe_path(packet_relative).read_bytes())
                if digest != actual:
                    failures.append(f"Frozen baseline digest {digest[:12]}… != packet bytes "
                                    f"{actual[:12]}… ({packet_relative})")
    elif builder:
        failures.append(f"No frozen expected.json baseline found for builder {builder[0]}")
    builder_metric["frozen_baseline"] = expected

    # contract audit re-run verdict (name-based: the audit is a distinct artifact)
    audit_candidate = discover(paths, r"contract", r"(?!)")
    verdict_record = {"candidates": audit_candidate}
    chosen = None
    for relative in audit_candidate:
        text = evidence.text(relative)
        if "packet-v2" in text or "packet_v2" in text:
            chosen = relative
            break
        chosen = chosen or relative
    if chosen:
        text = evidence.text(chosen)
        verdict_record.update({"path": chosen, **contract_audit_verdict(text)})
        if verdict_record["classification"] not in ("pass", "pass-with-named-gaps"):
            failures.append(f"Contract audit re-run verdict over v2 is "
                            f"{verdict_record['classification']!r}, not a semantic PASS "
                            f"or named gaps with owner notes: {chosen}")
    else:
        failures.append(f"No contract-audit re-run artifact found in {ROUND_DIR}/")
    verdict_record["verdict_recorded"] = verdict_record.get("classification")

    # filed baseline + no filed churn during validation
    failures.extend(preservation["failures"])

    return result(failures, {
        "packet": packet_relative, "claims": judgments,
        "uncertainty": {"populated": coverage, "total": total,
                        "audit_receipts": audits, "builder_controls": builder_pass,
                        "blocked_rerun_corroboration": blocked_rerun,
                        "zero_boilerplate": metric(
                            1 if (claims and not any(judgment["problems"] for judgment in judgments))
                            else 0, "packet-level zero-boilerplate flag")},
        "record_links": {"resolved": resolved},
        "shape_gate": {"scan": scan_metric, "run": gate_run},
        "builder": builder_metric, "contract_audit": verdict_record,
        "filed_bytes": preservation,
    }, missing=([] if packet_relative else [f"{PACKET_DIR}/packet-v2.md"])
        + ([] if builder else [f"tools/<packet-v2 builder>.py"])
        + ([] if expected or not builder else [f"{PACKET_DIR}/expected.json"])
        + ([] if audits or builder_pass else [f"{ROUND_DIR}/<uncertainty-audit>.md"])
        + ([] if chosen else [f"{ROUND_DIR}/<contract-audit-rerun>.md"]))

def receipt_state(evidence, relative):
    """Dated + command-carried green receipt, or None when absent."""
    text = evidence.text(relative)
    if not text:
        return None
    dated = bool(DATE_RE.search(text))
    commanded = bool(re.search(r"\b(?:python3?|git|sha256sum|command)\b", text, re.I))
    label = r"(?:overall(?: result| verdict)?|verdict|result|status|conclusion)"
    states = []
    for match in re.finditer(rf"(?im)^\s*(?:[-*]\s+)?(?:\*\*)?{label}(?:\*\*)?\s*[:—-]\s*(.+)$", text):
        value = match.group(1).lstrip(" *`_")
        if re.match(r"FAIL(?:ED)?\b|BLOCKED\b|PENDING\b|INCOMPLETE\b|NOT GREEN\b", value, re.I):
            states.append(False)
        elif re.search(r"\bPASS(?:ED)?\b|\bGREEN\b", value, re.I):
            states.append(True)
    return {"path": relative, "dated": dated, "command_carried": commanded,
            "green": dated and commanded and bool(states) and states[-1],
            "verdicts": [value for value in states]}


# ------------------------------------------------------------------- depth


def alias_map(text):
    """alias basename -> unique in-doc full path (full pointers + §8 pin lines)."""
    candidates = collections.defaultdict(set)
    for match in POINTER_RE.finditer(text):
        candidates[Path(match.group(0)).name].add(match.group(0))
    for line in text.splitlines():
        pinned = re.match(r"^([0-9a-f]{40,64})\s+(\S+)\s*$", line.strip())
        if pinned and re.match(r"(?:reports|tools|corpus|examples)/", pinned.group(2)):
            candidates[Path(pinned.group(2)).name].add(pinned.group(2))
    return {alias: sorted(paths)[0] for alias, paths in candidates.items()
            if len(paths) == 1}


CITE_RE_TEMPLATE = r"(?<![\w./-]){}\b(?=[:\s,;)\]`*]|$)"


def citations_in(text, aliases):
    """Full pointer paths plus alias:name tokens resolvable via the doc map."""
    found = set(POINTER_RE.findall(text))
    for alias in aliases:
        if re.search(CITE_RE_TEMPLATE.format(re.escape(alias)), text):
            found.add(aliases[alias])
    return found


def admissible(citation):
    return citation.startswith(("corpus/", "reports/round-12/", "reports/round-15/"))


def evaluate_draft(evidence, chosen):
    failures = []
    text = evidence.text(chosen)
    dated = bool(DATE_RE.search(text))
    if not dated:
        failures.append(f"Decision-table draft is undated: {chosen}")
    aliases = alias_map(text)
    lines = text.splitlines()

    tables, current, start = [], [], None
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            if not current:
                start = index
            current.append([cell.strip() for cell in stripped.strip("|").split("|")])
        else:
            if len(current) >= 2:
                context = "\n".join(lines[max(0, start - 6):start])
                tables.append((current, context))
            current, start = [], None
    if len(current) >= 2:
        context = "\n".join(lines[max(0, start - 6):start])
        tables.append((current, context))

    status_table_rows = []
    for table, context in tables:
        for cells in table[1:]:
            if all(re.fullmatch(r":?-{2,}:?", cell or "---") for cell in cells):
                continue
            if re.search(rf"\b{'|'.join(STATUS_VOCAB)}\b", " ".join(cells), re.I):
                status_table_rows.append((cells, context))
    covered = {status for row, _ in status_table_rows
               for status in STATUS_VOCAB
               if re.search(rf"\b{status}\b", " ".join(row), re.I)}
    if len(status_table_rows) < 3:
        failures.append(f"Decision table has {len(status_table_rows)} rule rows, need ≥3: {chosen}")
    for status in STATUS_VOCAB:
        if status not in covered:
            failures.append(f"Decision table never states a rule for status {status!r}: {chosen}")
    if not re.search(r"\bbasis\b", "\n".join(" | ".join(row) for row, _ in status_table_rows)
                     or text, re.I):
        failures.append(f"Decision table never requires the basis field: {chosen}")
    partition = bool(re.search(r"verification partition", text, re.I)) \
        or bool(re.search(r"corpus/knowledge/verification/[\w./+-]+", text)) \
        or bool(re.search(r"\bS/C/H/R/U/V\b|source-discipline-calibration", text, re.I))
    if not partition:
        failures.append(f"Decision table does not cross-reference the verification "
                        f"partition: {chosen}")

    cited_rows, context_cited, restated = 0, 0, 0
    status_cited = {status: False for status in STATUS_VOCAB}
    for row, context in status_table_rows:
        row_text = " | ".join(row)
        row_statuses = {status for status in STATUS_VOCAB
                        if re.search(rf"\b{status}\b", row_text, re.I)}
        in_row = citations_in(row_text, aliases)
        found = in_row | citations_in(context, aliases)
        if any(admissible(item) and safe_path(item).is_file() for item in found):
            cited_rows += 1
            if not in_row:
                context_cited += 1
            for status in row_statuses:
                status_cited[status] = True
        elif row_statuses and all(status_cited[status] for status in row_statuses):
            restated += 1
        else:
            failures.append(f"Decision-table rule row lacks a resolvable corpus or "
                            f"round-12/15 citation (row or table context): {chosen} — "
                            f"row: {row_text[:160]}")
    broken = [item["path"] for item in evidence.pointers(text) if not item["exists"]]
    if broken:
        failures.append(f"Decision-table draft has unresolvable citations: "
                        f"{', '.join(sorted(set(broken)))}")
    return result(failures, {
        "draft": chosen, "dated": dated,
        "aliases": len(aliases),
        "tables": metric(len(tables), "tables in draft"),
        "rule_rows": metric(len(status_table_rows), "decision-table rule rows"),
        "statuses_covered": sorted(covered),
        "cited_rows": metric(cited_rows, "rule rows citing corpus or round-12/15 artifacts"),
        "context_cited_rows": metric(context_cited, "rule rows cited via table context"),
        "restated_rows": metric(restated, "rule rows restating an already-cited status"),
        "partition_crossref": partition,
    })


def measure_d(evidence, paths):
    candidates = discover(paths, r"uncertainty|decision[ -]?table|skill[ -]?table|skill[ -]?draft",
                          r"uncertainty.{0,200}decision table|decision table.{0,200}uncertainty")
    ranked, fallback = [], None
    for relative in candidates:
        text = evidence.text(relative)
        if not (re.search(r"\b(supported|partial|unresolved)\b", text, re.I) and "|" in text):
            continue
        verdict = evaluate_draft(evidence, relative)
        ranked.append(verdict)
        if verdict["passed"]:
            return result([], {**verdict["measurement"], "candidates": candidates,
                               "drafts_evaluated": metric(len(ranked), "drafts evaluated")})
        fallback = fallback or verdict
    if fallback:
        return {**fallback, "measurement": {**fallback["measurement"],
                                            "candidates": candidates,
                                            "drafts_evaluated": metric(len(ranked), "drafts evaluated")}}
    return result([f"No label-uncertainty decision-table draft found in {ROUND_DIR}/ "
                   "(D workers' draft is a missing dependency)"],
                  {"candidates": candidates},
                  [f"{ROUND_DIR}/<uncertainty-decision-table-draft>.md"])


# -------------------------------------------------------------- validation


def guard_preflight():
    spec = importlib.util.spec_from_file_location("round15_receipt_guard", ROOT / GUARD)
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
    before = filed_snapshot()
    paths = round15_files()
    tool_paths = [path.relative_to(ROOT).as_posix()
                  for path in sorted((ROOT / "tools").rglob("*.py"))
                  if "__pycache__" not in path.parts]
    packet_md, packet_src = find_packet(evidence)
    builder = pick_builder(paths + tool_paths)
    gate_target = packet_md or packet_src
    gate_argv = [GATE, gate_target] if gate_target else [GATE, "--selftest"]
    with ThreadPoolExecutor(max_workers=4) as pool:
        gate_future = pool.submit(run_command, gate_argv)
        guard_future = pool.submit(run_command, (GUARD, "--selftest"))
        plan = []
        if builder:
            suite_packet = packet_src or packet_md
            invocations = {relative: builder_invocations(relative, suite_packet)
                           for relative in builder}
            plan.append(("selftest", builder[0], invocations[builder[0]][0]))
            plan.insert(1, ("selftest", builder[0], invocations[builder[0]][0]))
            plan.append(("receipt", builder[0], invocations[builder[0]][1]))
            for relative in builder[1:]:
                plan.append(("selftest", relative, invocations[relative][0]))
                plan.append(("receipt", relative, invocations[relative][1]))
        futures = [pool.submit(run_command, argv) for _, _, argv in plan]
        gate_run = gate_future.result()
        guard_run = guard_future.result()
        outcomes = [future.result() for future in futures]
    builder_selftests = [run for (kind, _, _), run in zip(plan, outcomes)
                         if kind == "selftest"]
    builder_receipts = [{"tool": tool, "run": run}
                        for (kind, tool, _), run in zip(plan, outcomes)
                        if kind == "receipt"]
    if gate_target == packet_src and packet_src and not packet_md \
            and "HO-DATA" in gate_run.get("stderr_tail", ""):
        gate_run["note"] = ("gate could not evaluate the YAML source as Markdown; "
                            "handoff-packet-check reads Markdown documents")
    expected = find_expected_baseline(paths, builder[0] if builder else None)
    preservation = filed_preservation(claims.get("baseline_revision"))
    depth = measure_d(evidence, paths)
    d_draft = depth["measurement"].get("draft")
    results = {"O": measure_o(evidence, paths, packet_md, packet_src, builder, expected,
                              gate_run if gate_target else None, builder_selftests,
                              builder_receipts, preservation, d_draft=d_draft),
               "D": depth}
    if guard_run.get("exit") != 0 or (guard_run.get("json") or {}).get("selftest_passed") is not True:
        results["O"]["failures"].append("Receipt guard selftest not green")
        results["O"]["passed"] = False
    results["O"]["measurement"]["guard_selftest"] = {
        "command": guard_run.get("command"), "exit": guard_run.get("exit"),
        "date": guard_run.get("date")}
    after = filed_snapshot()
    changes = [{"path": path, "before": before.get(path), "after": after.get(path)}
               for path in sorted(before.keys() | after.keys()) if before.get(path) != after.get(path)]
    if changes:
        results["O"]["failures"].append("Filed round-8..14 bytes/path set changed during "
                                        "validation; rerun on a settled tree")
        results["O"]["passed"] = False
    declared = {claim.get("id"): claim.get("axis") for claim in claims.get("claims", [])
                if isinstance(claim, dict)}
    if declared != {"O": "operability", "D": "depth"}:
        results["O"]["failures"].append(f"Round-15 declared claims do not match O/D: {declared}")
        results["O"]["passed"] = False
    if evidence.errors:
        results["O"]["failures"].extend(evidence.errors)
        results["O"]["passed"] = False
    return {
        "round": 15, "runner": RUNNER, "runner_sha256": sha((ROOT / RUNNER).read_bytes()),
        "counting_command": COMMAND, "date": today(),
        "baseline_revision": claims.get("baseline_revision"), "targets_date": targets.get("date"),
        "claims_declared": declared,
        "acceptance_checks_passed": all(item["passed"] for item in results.values()),
        "claims": results, "input_sha256": dict(sorted(evidence.inputs.items())),
        "failures": [f"claim {claim_id}: {failure}" for claim_id, item in results.items()
                     for failure in item["failures"]],
        "missing_dependencies": sorted(evidence.missing | {path for item in results.values()
                                                           for path in item["missing_dependencies"]}),
        "filed_rounds": {"baseline": preservation, "changed_during_validation": changes,
                         "snapshot_before": before, "snapshot_after": after,
                         "command": f"{COMMAND} (hash filed round-8..14 paths before/after checks)",
                         "date": today()},
        "limits": [
            "Historical validators are never executed. Only fixed read-only check/selftest "
            "commands run; no command is executed from an evidence file.",
            "Filed rounds 8-14 are compared with the declared baseline; any non-append-only "
            "byte change or churn during validation fails closed.",
            "The uncertainty/boilerplate and contract-audit verdict checks are structural: "
            "vocabulary, basis presence and location citation, link resolution against the "
            "worktree, dated command-carried receipts, and owner-attributed gap lists. They "
            "do not certify the truth of any claim, and all artifacts remain NON-CANON.",
            "The shape gate result is the packet's own gate reading; 16/16 + 20/20 is shape, "
            "not semantic conformance, lore review, or a transfer acceptance.",
            "The contract-audit verdict is recorded as stated by the re-run artifact; a "
            "pass-with-named-gaps classification still names every remaining gap and owner.",
            "Freshness axis-move claims remain paused; this round closes the round-12 "
            "adjacency reject on packet semantics only.",
        ],
    }


# ---------------------------------------------------------------- selftest


def selftest():
    controls = []

    def check(name, value):
        controls.append({"control": name, "passed": bool(value)})

    md_packet = """# packet v2
## claim_ledger

| claim_id | kind | evidence_status | uncertainty | record_links | summary |
|---|---|---|---|---|---|
| CL01 | generative rule | invented | supported — basis: examples/culture-d3/packet.json sound_changes | examples/culture-d3/packet.json | rule |
| CL02 | generative rule | invented | partial — basis: reports/round-15/handoff/packet-v2.md §scope | reports/round-6/parent-reconciliation.json | rule |
| CL03 | generative rule | invented | unresolved — basis: TBD | none | rule |
| CL04 | generative rule | invented | unresolved — basis: examples/culture-d3/packet.json screening | examples/culture-d3/packet.json | rule |
| CL05 | generative rule | invented | unresolved — basis: examples/culture-d3/packet.json screening | examples/culture-d3/packet.json | rule |
"""
    rows = parse_claim_ledger(md_packet)
    check("md-rows-parsed", [row["id"] for row in rows] == ["CL01", "CL02", "CL03", "CL04", "CL05"])
    check("md-uncertainty-parsed",
          rows[0]["uncertainty"] == {"status": "supported",
                                     "basis": "examples/culture-d3/packet.json sound_changes"})
    judgments = uncertainty_audit_rows(rows)
    check("cited-basis-accepted", judgments[0]["basis_cited"])
    check("placeholder-basis-rejected", any("placeholder basis" in problem
                                            for problem in judgments[2]["problems"]))
    check("duplicate-basis-flagged",
          any("boilerplate" in problem for problem in judgments[4]["problems"]))
    check("status-vocab-held", judgments[1]["status"] == "partial")
    yaml_packet = """claims:
  - claim_id: Y1
    uncertainty:
      status: supported
      basis: corpus/knowledge/synthesis/loanword-material-dating.md:43-57
  - claim_id: Y2
    uncertainty:
      status: unresolved
      basis: examples/culture-d3/packet.json screening
"""
    yrows = parse_claim_ledger(yaml_packet)
    check("yaml-rows-parsed", [row["id"] for row in yrows] == ["Y1", "Y2"])
    check("yaml-status-parsed", yrows[0]["uncertainty"]["status"] == "supported")
    check("yaml-basis-parsed", "loanword-material-dating.md" in yrows[0]["uncertainty"]["basis"])
    v1_packet = ("## claim_ledger\n\n| claim_id | kind | evidence_status | summary |\n"
                 "|---|---|---|---|\n| CL01 | generative rule | invented | x |\n")
    v1_rows = parse_claim_ledger(v1_packet)
    check("v1-uncertainty-absent-detected",
          v1_rows and v1_rows[0]["uncertainty"] is None
          and any("no uncertainty dimension" in problem
                  for problem in uncertainty_audit_rows(v1_rows)[0]["problems"]))
    check("gate-scan-parsed", gate_scan("INFO scan: fields=16/16 glossary-entries=20 findings=0")
          == {"fields": 16, "fields_total": 16, "glossary_entries": 20, "findings": 0})
    check("gate-scan-absent", gate_scan("nothing here") is None)
    passing = ("# contract audit re-run\nDate: 2026-10-17. command: python3 x\n"
               "Verdict: PASS — packet v2 satisfies §4 semantics.\n")
    check("audit-pass-classified", contract_audit_verdict(passing)["classification"] == "pass")
    gaps_owned = ("# re-run\nDate: 2026-10-17. command: python3 x\n"
                  "Verdict: remaining gaps named below.\n"
                  "- Gap: bilateral acknowledgment pending (owner: lore-lane integrator).\n"
                  "- Remaining: L0 digest question open (owner: lore-shokunin).\n")
    check("audit-owned-gaps-classified",
          contract_audit_verdict(gaps_owned)["classification"] == "pass-with-named-gaps")
    gaps_unowned = ("# re-run\nDate: 2026-10-17. command: python3 x\n"
                    "Verdict: gaps remain.\n- Gap: acknowledgment pending.\n")
    check("audit-unowned-gaps-not-pass",
          contract_audit_verdict(gaps_unowned)["classification"] != "pass-with-named-gaps")
    undated = "# re-run\nVerdict: PASS\n"
    check("audit-undated-not-pass", contract_audit_verdict(undated)["classification"] != "pass")
    green = receipt_probe("2026-10-17 command: python3 tool.py\nResult: PASS\n")
    red = receipt_probe("Result: PASS\n")
    check("receipt-green-detected", green["dated"] and green["command_carried"] and green["green"])
    check("undated-receipt-rejected", not red["green"])
    v2_packet = """## claim_ledger

| claim_id | kind | evidence_status | uncertainty_status | uncertainty_basis | links | statement |
|---|---|---|---|---|---|---|
| V1 | generative rule | invented | supported | grounding: A-02; owner: none needed | A-02#lexicon.L01 | rule one |
| V2 | real-world reference | attested | partial | grounding: A-05; restriction: translation only | A-05, reports/round-6/parent-reconciliation.json | rule two |
| V3 | candidate world-fact | (to-verify) | unresolved | grounding: A-05; open: no baseline; owner: lore | A-05#scope_notes | rule three |

## artifact_manifest

| artifact_id | path | sha256 |
|---|---|---|
| A-02 | examples/culture-d3/packet.json | bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829 |
| A-05 | examples/culture-d3/expected.json | 562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc |
"""
    v2_rows = parse_claim_ledger(v2_packet)
    check("v2-columns-parsed",
          [row["uncertainty"]["status"] for row in v2_rows] == ["supported", "partial", "unresolved"])
    check("v2-basis-parsed", "grounding: A-02" in v2_rows[0]["uncertainty"]["basis"])
    check("v2-grounding-basis-cited", all(
        item["basis_cited"] for item in uncertainty_audit_rows(v2_rows)))
    manifest = parse_manifest(v2_packet)
    check("manifest-parsed", manifest.get("A-02", {}).get("path") ==
          "examples/culture-d3/packet.json")
    check("artifact-refs-extracted",
          "A-02#lexicon.L01" in row_links(v2_rows[0]) and
          "reports/round-6/parent-reconciliation.json" in row_links(v2_rows[1]))
    check("manifest-ref-resolves",
          manifest_path("A-02#lexicon.L01", manifest) == "examples/culture-d3/packet.json"
          and manifest_path("A-99#x", manifest) is None)
    digest = manifest.get("A-02", {}).get("sha256")
    check("manifest-digest-captured", digest is not None and len(digest) == 64)
    old = b'{"rows": [{"id": 1}]}\n'
    check("filed-identical", preservation_kind("x.json", old, old) == "byte-identical")
    check("filed-append-allowed", preservation_kind(
        "x.md", b"filed\n", b"filed\naddendum\n") == "append-only")
    check("filed-rewrite-rejected",
          preservation_kind("x.json", old, old.replace(b"1", b"2")) == "violation")
    for relative in ("../outside.md", "/outside.md", ".git/config"):
        try:
            safe_path(relative)
        except ValueError:
            check("unsafe-pointer-rejected-" + relative, True)
        else:
            check("unsafe-pointer-rejected-" + relative, False)
    fake_paths = ["tools/assemble-d2.py", "tools/gates/handoff-packet-check.py",
                  "reports/round-15/handoff/builder-v2.py"]
    check("builder-discovery-skips-gates",
          "tools/gates/handoff-packet-check.py" not in pick_builder(fake_paths))
    sample = metric(3, "unit")
    check("metric-carries-command-and-date",
          sample["command"].startswith(COMMAND) and sample["date"] == today())
    draft_excerpt = (
        "cited corpus/knowledge/verification/to-verify-triage-protocol.md above\n"
        "9fb89a062253a9273196ee8b8122f62598d74ce6b32b124034be5029c44ba0a2  "
        "reports/round-12/adjacency/contract.md\n")
    aliases = alias_map(draft_excerpt)
    check("alias-map-built",
          aliases.get("contract.md") == "reports/round-12/adjacency/contract.md")
    check("alias-citation-resolved",
          "reports/round-12/adjacency/contract.md"
          in citations_in("see `contract.md:27-28`", aliases))
    check("unknown-alias-ignored", citations_in("see `packet.md:9`", aliases) == set())
    check("admissible-classification",
          admissible("corpus/knowledge/x.md")
          and admissible("reports/round-15/claims.json")
          and not admissible("reports/round-11/handoff/packet.md"))
    payload = {"runner": RUNNER, "command": COMMAND + " --selftest", "date": today(),
               "selftest_passed": all(item["passed"] for item in controls), "controls": controls,
               "passed": metric(sum(item["passed"] for item in controls), "validator selftest controls"),
               "total": metric(len(controls), "validator selftest control inventory")}
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["selftest_passed"] else 1


def receipt_probe(text):
    """In-memory receipt check used by --selftest; reads no repo file."""
    dated = bool(DATE_RE.search(text))
    commanded = bool(re.search(r"\b(?:python3?|git|sha256sum|command)\b", text, re.I))
    label = r"(?:overall(?: result| verdict)?|verdict|result|status|conclusion)"
    states = []
    for match in re.finditer(rf"(?im)^\s*(?:[-*]\s+)?(?:\*\*)?{label}(?:\*\*)?\s*[:—-]\s*(.+)$", text):
        value = match.group(1).lstrip(" *`_")
        if re.match(r"FAIL(?:ED)?\b|BLOCKED\b|PENDING\b|INCOMPLETE\b|NOT GREEN\b", value, re.I):
            states.append(False)
        elif re.search(r"\bPASS(?:ED)?\b|\bGREEN\b", value, re.I):
            states.append(True)
    return {"dated": dated, "command_carried": commanded,
            "green": dated and commanded and bool(states) and states[-1]}


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate round-15 O/D without touching filed rounds 8-14.")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--selftest", action="store_true",
                       help="run in-memory validator controls, no receipt write")
    modes.add_argument("--check", action="store_true",
                       help="run full acceptance and print JSON without writing validation.json")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.check:
        try:
            guard_preflight()
        except (OSError, RuntimeError, ImportError) as error:
            print(f"RECEIPT-GUARD-UNAVAILABLE: {error}", file=sys.stderr)
            return 3
    receipt = validate()
    if args.check:
        print(json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False))
    else:
        guard_preflight()
        (ROOT / OUTPUT).write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                              ensure_ascii=False) + "\n", encoding="utf-8")
        for claim_id, item in receipt["claims"].items():
            print(f"claim {claim_id}: {'PASS' if item['passed'] else 'FAIL'}")
        print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
        if receipt["missing_dependencies"]:
            print("missing_dependencies: " + ", ".join(receipt["missing_dependencies"]))
    return 0 if receipt["acceptance_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
