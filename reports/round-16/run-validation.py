#!/usr/bin/env python3
"""Round-16 validator — the round's counting command (claims C and O).

Claim C (coverage): reports/round-16/civ-map.json gives every one of the 94
`corpus/knowledge/civilizations/*.md` entries a status receipt — `current`
(re-fetched or verified in-repo this round, with date+command), `stale-fixed`
(corrected with evidence), or `stale-documented` (named reason); zero entries
without a status; an auditor independently spot-checks >=10 entries in its own
dated, command-carried artifact; the count 94 is reproduced here from the
corpus directory. This is a coverage/staleness map, NOT a freshness axis-move:
the freshness pause (LOG.md "freshness axis-move claims pause pending operator
recalibration") remains in force and no source freshness verdict is issued.

Claim O (operability): the three round-15 reviewer findings are closed with
controls — F10-1 edge `source` resolution (a prose aggregate source is
rejected `E-SOURCE-UNKNOWN`), F9-1 the `#L<n>` anchor collision (a dangling
record-id-shaped selector like `examples/culture-d3/packet.json#L99` is
rejected `L-SELECTOR-UNRESOLVED` while real ids still resolve), F9-2 the
design §3.2.4 record-coverage rule (every delivered D3 record id appears in
>=1 claim link or edge target on the amended keyed packet build, or the
residual deviation is documented with an owner note); packet_links +
packet_uncertainty selftests stay green and the link judge's inventory grows
past its round-15 stamped 31 checks (uncertainty must not shrink from 19);
the shape gate still reads 16/16 fields + 20/20 glossary entries with zero
findings on the amended packet.

Filed rounds 8-15 are compared against the declared baseline
(`16652e8…`, the round-15 admit) and must not change other than append-only
during validation; a NEW keyed packet build may be added under
reports/round-15/handoff/ or reports/round-16/ — filed bytes never rewritten.
Only fixed read-only check/selftest commands and this runner's own fixture in
`.scratch/` are executed; no command is ever taken from an evidence file.
This runner writes only its own receipt. It measures, it does not certify
truth, canon, lore receipt, or source freshness.
"""
from __future__ import annotations

import argparse
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

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-16"
RUNNER = f"{ROUND_DIR}/run-validation.py"
OUTPUT = f"{ROUND_DIR}/validation.json"
COMMAND = f"python3 {RUNNER}"
GUARD = "tools/harness/receipt_guard.py"
GATE = "tools/gates/handoff-packet-check.py"
LINKS = "tools/harness/packet_links.py"
UNCERTAINTY = "tools/harness/packet_uncertainty.py"
CIV_DIR = "corpus/knowledge/civilizations"
CIV_MAP = f"{ROUND_DIR}/civ-map.json"
D3_PACKET = "examples/culture-d3/packet.json"
FILED = tuple(f"reports/round-{number}" for number in range(8, 16))
# Round-15 stamped selftest inventories (reports/round-15/handoff/
# review-10.md §F10-2: "packet_uncertainty.py + packet_links.py (both with
# passing selftests: 19/19, 31/31)"). Growth is judged against these pins.
LINKS_PRIOR = 31
UNCERTAINTY_PRIOR = 19
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}")
COMMAND_RE = re.compile(r"\b(?:python3?|git|sha256sum|shasum|curl|wget|command)\b", re.I)
POINTER_RE = re.compile(
    r"(?<![\w./-])(?:reports|tools|corpus|examples)/[\w./+-]+\.(?:json|md|py|ya?ml|tsv|txt|sh)\b"
    r"|(?<![\w./-])(?:SCORECARD|LOG|SHONEN|PROVINCE|SKILL|MINT|README)\.md\b")
SHA_RE = re.compile(r"\b[0-9a-f]{64}\b")
PLACEHOLDER_RE = re.compile(
    r"\b(tbd|tba|todo|n/?a|placeholder|boilerplate|same[- ]as[- ](?:above|below)|"
    r"as (?:above|below)|see (?:above|below|other)|copy of|unchanged)\b", re.I)
STATUS_VOCAB = ("current", "stale-fixed", "stale-documented")
STATUS_KEY_CANDIDATES = ("status", "staleness", "state", "receipt", "verdict")
ENTRY_KEY_CANDIDATES = ("entry", "civilization", "file", "name", "id", "path", "basename")
MAP_CONTAINER_KEYS = ("rows", "entries", "civilizations", "map", "records")
GATE_SCAN_RE = re.compile(
    r"INFO scan: fields=(\d+)/(\d+) glossary-entries=(\d+) findings=(\d+)")
SELFTEST_COUNT_RE = re.compile(r"(\d+)\s+checks?\s+passed", re.I)
BASELINE_RE = re.compile(r"[0-9a-f]{40,64}")
PACKET_NAME_RE = re.compile(r"^packet[\w.-]*\.(?:md|ya?ml)$")
PACKET_EXCLUDE_RE = re.compile(r"shard|review|design|contract|frozen|expected|audit", re.I)
EXCLUDE_NAMES = {"claims.json", "targets.json", "validation.json", "scope.md",
                 "run-validation.py", "civ-map.json"}
RECORD_ID_KEY = "id"


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


def result(failures, measurement, missing=()):
    return {"passed": not failures, "failures": failures,
            "measurement": measurement, "missing_dependencies": sorted(set(missing))}


def run_command(parts, timeout=300):
    argv = [sys.executable, *parts]
    child_env = dict(os.environ)
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
                    stdout_tail=run.stdout.decode("utf-8", "replace")[-1200:],
                    stderr_tail=run.stderr.decode("utf-8", "replace")[-1200:])
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        item.update(exit=None, error=str(error), timeout=isinstance(error, subprocess.TimeoutExpired))
    return item


def git(*args, data=None):
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1", LC_ALL="C")
    proc = subprocess.run(["git", "--literal-pathspecs", *args], cwd=ROOT,
                          input=data, capture_output=True, timeout=120, env=env)
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
            raise ValueError("no filed round-8..15 blobs at the declared baseline")
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


# ------------------------------------------------------------------ claim C


def civilization_entries(evidence):
    """The corpus partition: sorted basenames of corpus/knowledge/civilizations/*.md."""
    base = ROOT / CIV_DIR
    entries = []
    if base.is_dir():
        for path in sorted(base.glob("*.md")):
            if path.is_file():
                entries.append(path.stem)
                evidence.inputs[f"{CIV_DIR}/{path.name}"] = sha(path.read_bytes())
    return entries


def normalize_status(value):
    return re.sub(r"[\s_]+", "-", str(value).strip().lower()) if value is not None else None


def normalize_entry(value):
    name = str(value or "").strip().strip("`")
    name = re.sub(r"^corpus/knowledge/civilizations/", "", name)
    name = re.sub(r"\.md$", "", name)
    return Path(name).stem if name else ""


def map_rows(payload):
    """Accept any of the map's plausible containers; return the row list."""
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in MAP_CONTAINER_KEYS:
            value = payload.get(key)
            if isinstance(value, list):
                return value
    return None


def row_entry(row):
    if not isinstance(row, dict):
        return ""
    for key in ENTRY_KEY_CANDIDATES:
        if row.get(key):
            return normalize_entry(row[key])
    return ""


def row_status(row):
    if not isinstance(row, dict):
        return None
    for key in STATUS_KEY_CANDIDATES:
        if row.get(key):
            return normalize_status(row[key])
    return None


def row_text(row):
    if isinstance(row, dict):
        return " ".join(f"{key}: {value}" for key, value in sorted(row.items())
                        if isinstance(value, (str, int, float)))
    return str(row)


STATUS_REQUIREMENTS = {
    "current": lambda text: (bool(DATE_RE.search(text)) and bool(COMMAND_RE.search(text))
                             and any(d in accepted_round_dates()
                                     for d in DATE_RE.findall(text))),
    "stale-fixed": lambda text: bool(POINTER_RE.search(text) or SHA_RE.search(text)
                                     or COMMAND_RE.search(text)),
    "stale-documented": lambda text: bool(text.strip())
    and not PLACEHOLDER_RE.search(text),
}
STATUS_REQUIREMENT_TEXT = {
    "current": "a date matching this round (today) and a command (re-fetch or "
               "in-repo verification)",
    "stale-fixed": "evidence: a repo pointer, a sha256, or a command",
    "stale-documented": "a named, non-placeholder reason",
}


def audit_receipt_state(text):
    """Dated + command-carried green auditor receipt, or the failing parts."""
    dated = bool(DATE_RE.search(text))
    commanded = bool(COMMAND_RE.search(text))
    return {"dated": dated, "command_carried": commanded}


def accepted_round_dates():
    """Dates whose evidence counts as 'this round': the declared round date
    from claims.json, local today, and the UTC date of the running window
    (shards stamp Z; the round spans local midnight)."""
    now_utc = dt.datetime.now(dt.timezone.utc)
    accepted = {dt.date.today().isoformat(), now_utc.date().isoformat()}
    try:
        claims = strict_json((ROOT / ROUND_DIR / "claims.json").read_text(encoding="utf-8"))
        if isinstance(claims.get("date"), str):
            accepted.add(claims["date"])
    except (OSError, ValueError, UnicodeError):
        pass
    return accepted


def civ_auditors(evidence, entries):
    """Find independent auditor artifact(s) naming >=10 distinct civ entries.

    Two candidate routes: any file whose name matches `audit` (the auditor
    seat files e.g. civ/map-audit.md), and any file outside civ/ whose body
    audits civ entries. The C-shard range receipts under civ/ (001-012.md
    …) are the shards' own evidence and never qualify by body alone.
    """
    base = ROOT / ROUND_DIR
    candidates = []
    if base.is_dir():
        for path in sorted(base.rglob("*")):
            relative = path.relative_to(ROOT).as_posix()
            if (path.is_file() and "__pycache__" not in path.parts
                    and path.name not in EXCLUDE_NAMES
                    and path.suffix in (".md", ".json", ".txt")
                    and path.as_posix() != CIV_MAP):
                in_civ = relative.startswith(f"{ROUND_DIR}/civ/")
                named_auditor = bool(re.search(r"audit", path.name, re.I))
                if named_auditor or (not in_civ and "shard" not in path.name.lower()):
                    candidates.append(relative)
    found = []
    for relative in candidates:
        text = evidence.text(relative)
        if not text:
            continue
        named = sorted({entry for entry in entries
                        if re.search(r"(?<![\w/-])" + re.escape(entry) + r"(?![\w-])", text)})
        state = audit_receipt_state(text)
        judged = bool(re.search(r"\b(audit|spot.?check|re-?check|verif)", text, re.I))
        if len(named) >= 10 and judged:
            found.append({"path": relative, "entries_named": len(named),
                          "sample": named[:12], **state})
    return found


def measure_c(evidence):
    failures = []
    entries = civilization_entries(evidence)
    entry_count = metric(len(entries), f"count {CIV_DIR}/*.md")
    payload = evidence.document(CIV_MAP)
    rows = map_rows(payload) if payload is not None else None
    status_counts = {status: 0 for status in STATUS_VOCAB}
    named_entries, audited_rows, auditors = [], [], []
    if payload is None:
        failures.append(f"{CIV_MAP} is missing or not strict JSON "
                        "(the map-scribe's deliverable has not landed)")
    elif rows is None:
        failures.append(f"{CIV_MAP} has no recognizable row container "
                        f"(one of {', '.join(MAP_CONTAINER_KEYS)} or a top-level list)")
    else:
        declared_count = payload.get("count") if isinstance(payload, dict) else None
        if declared_count is not None and declared_count != len(entries):
            failures.append(f"civ-map declares count {declared_count} != corpus "
                            f"{len(entries)}")
        if isinstance(payload, dict) and payload.get("complete") is False:
            failures.append("civ-map declares complete: false")
        unreceipted = payload.get("unreceipted") if isinstance(payload, dict) else None
        if unreceipted:
            failures.append(f"civ-map still lists unreceipted entries: "
                            f"{str(unreceipted)[:200]}")
        shard_pins = payload.get("shards") if isinstance(payload, dict) else {}
        seen = {}
        for position, row in enumerate(rows):
            entry = row_entry(row)
            status = row_status(row)
            if not entry:
                failures.append(f"civ-map row #{position} names no civilization entry")
                continue
            if entry in seen:
                failures.append(f"civ-map duplicates entry {entry} (rows {seen[entry]}, {position})")
                continue
            seen[entry] = position
            named_entries.append(entry)
            if status not in STATUS_VOCAB:
                failures.append(f"civ-map {entry}: status {status!r} off vocabulary "
                                f"{list(STATUS_VOCAB)}")
                continue
            status_counts[status] += 1
            evidence_path = row.get("evidence_path") if isinstance(row, dict) else None
            evidence_text = ""
            if evidence_path:
                relative = str(evidence_path)
                try:
                    path = safe_path(relative)
                    if path.is_file():
                        data = path.read_bytes()
                        evidence.inputs[relative] = sha(data)
                        evidence_text = data.decode("utf-8", "replace")
                        pin = (shard_pins or {}).get(path.name, {}).get("sha256") \
                            if isinstance(shard_pins, dict) else None
                        if pin and pin != sha(data):
                            failures.append(f"civ-map {entry}: evidence shard {relative} "
                                            f"sha256 drifts from the map's pin")
                    else:
                        failures.append(f"civ-map {entry}: evidence_path {relative} "
                                        f"is not a file in the repo")
                except (OSError, ValueError) as error:
                    failures.append(f"civ-map {entry}: evidence_path {relative}: {error}")
            elif status != "stale-documented":
                failures.append(f"civ-map {entry}: status {status!r} names no evidence_path")
            text = row_text(row) + "\n" + evidence_text
            requirement = STATUS_REQUIREMENTS[status]
            if not requirement(text):
                failures.append(f"civ-map {entry}: status {status!r} lacks "
                                f"{STATUS_REQUIREMENT_TEXT[status]}")
            if entry not in entries:
                failures.append(f"civ-map names {entry}: no such file under {CIV_DIR}/")
        missing = sorted(set(entries) - set(named_entries))
        extra = sorted(set(named_entries) - set(entries))
        if missing:
            failures.append(f"civ-map has no status receipt for {len(missing)} corpus "
                            f"entries: {', '.join(missing[:8])}"
                            + (" …" if len(missing) > 8 else ""))
        if extra:
            failures.append(f"civ-map names {len(extra)} non-corpus entries: "
                            f"{', '.join(extra[:8])}")
        if set(named_entries) != set(entries):
            failures.append(f"civ-map row set != corpus partition: map {len(named_entries)} "
                            f"rows vs {len(entries)} corpus entries")
        audited_rows = metric(len(named_entries), "statused civ-map rows")
    map_count = metric(len(named_entries), "count statused rows in civ-map.json")
    auditors = civ_auditors(evidence, entries)
    if not auditors:
        failures.append(f"No auditor artifact found under {ROUND_DIR}/ (outside civ/) "
                        f"independently spot-checking >=10 civilization entries "
                        f"(dated, command-carried)")
    else:
        for auditor in auditors:
            if not (auditor["dated"] and auditor["command_carried"]):
                failures.append(f"Auditor artifact not dated+command-carried: "
                                f"{auditor['path']}")
    best_auditor = max((item["entries_named"] for item in auditors), default=0)
    auditor_metric = metric(best_auditor,
                            "max distinct civ entries named by one auditor artifact")
    defect_classes = {}
    for failure in failures:
        if "is not a file in the repo" in failure:
            key = "dangling-evidence-path (F-AUD-6 class; owner: map scribe C09)"
        elif "lacks" in failure:
            key = "status-requirement-unmet-on-evidence (consequence of the dangling path)"
        elif "No auditor artifact" in failure:
            key = "auditor-artifact-absent"
        else:
            key = "other"
        defect_classes[key] = defect_classes.get(key, 0) + 1
    return result(failures, {
        "civ_dir": CIV_DIR,
        "civ_entries": entry_count,
        "map_rows": map_count,
        "statused": audited_rows,
        "defect_classes": metric(defect_classes,
                                 "count C failures grouped by defect class"),
        "status_histogram": {status: metric(count, f"rows with status {status!r}")
                             for status, count in status_counts.items()},
        "zero_unstatused": metric(1 if (payload is not None and rows is not None
                                        and set(named_entries) == set(entries)) else 0,
                                  "1 when every corpus entry has exactly one statused row"),
        "auditor": {"artifacts": auditors, "entries_spot_checked": auditor_metric,
                    "required": 10},
    }, missing=([] if payload is not None else [CIV_MAP])
        + ([] if auditors or payload is None else [f"{ROUND_DIR}/<civ-audit>.md"]))


# ------------------------------------------------------------------ claim O


def round16_files():
    base = ROOT / ROUND_DIR
    if not base.is_dir():
        return []
    return [path.relative_to(ROOT).as_posix() for path in sorted(base.rglob("*"))
            if path.is_file() and "__pycache__" not in path.parts]


def packet_candidates():
    """Keyed packet builds, newest first: round-16 builds, then round-15 attempts."""
    found = []
    for directory in (ROUND_DIR, "reports/round-15/handoff"):
        base = ROOT / directory
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*")):
            if (path.is_file() and PACKET_NAME_RE.match(path.name)
                    and not PACKET_EXCLUDE_RE.search(path.name)
                    and "__pycache__" not in path.parts):
                attempt = re.search(r"(\d+)", path.name)
                found.append({"path": path.relative_to(ROOT).as_posix(),
                              "dir": directory,
                              "stem": re.sub(r"\.(?:md|ya?ml)$", "", path.name),
                              "attempt": int(attempt.group(1)) if attempt else 0,
                              "suffix": path.suffix})
    pairs = {}
    for item in found:
        key = (item["dir"], item["stem"])
        pairs.setdefault(key, {})["md" if item["suffix"] == ".md" else "yml"] = item["path"]
    ranked = []
    for (directory, stem), pair in pairs.items():
        numbers = re.findall(r"(\d+)", stem)
        ranked.append({"dir": directory, "stem": stem,
                       "attempt": int(numbers[-1]) if numbers else 0,
                       "md": pair.get("md"), "yml": pair.get("yml")})
    ranked.sort(key=lambda item: (item["dir"] != ROUND_DIR, -item["attempt"], item["stem"]))
    return ranked


FILED_PACKET = "reports/round-15/handoff/packet-v2-05"


def is_amended(candidate):
    """A NEW keyed build: anything but the filed packet-v2-05 in round-15."""
    return bool(candidate and (candidate["dir"] == ROUND_DIR
                               or candidate["stem"] != Path(FILED_PACKET).name))


def measure_o(evidence, paths):
    failures = []
    candidates = packet_candidates()
    chosen = candidates[0] if candidates else None
    amended = is_amended(chosen)
    packet_md = chosen["md"] if chosen else None
    machine = chosen["yml"] or chosen["md"] if chosen else None
    gate_target = packet_md
    if not chosen:
        failures.append("No keyed packet build found under reports/round-16/ or "
                        "reports/round-15/handoff/")
    elif not amended:
        failures.append(f"No amended keyed packet build landed: newest build is still the "
                        f"filed {FILED_PACKET}.md/.yml (F9-2's amended build is a missing "
                        f"dependency; filed bytes must not be edited in place)")

    # harness selftests: green, deterministic, grown
    def selftest_state(tool, prior, runs):
        rows = [run_command((tool, "--selftest")) for _ in range(runs)]
        counts = []
        for run in rows:
            match = SELFTEST_COUNT_RE.search(run.get("stdout_tail", ""))
            counts.append(int(match.group(1)) if match else None)
        deterministic = len({run.get("stdout_sha256") for run in rows}) == 1
        return {"command": rows[0].get("command"), "runs": [
            {"exit": run.get("exit"), "checks": count, "date": run.get("date"),
             "stdout_tail": run.get("stdout_tail", "")[:200]}
            for run, count in zip(rows, counts)],
            "checks_now": counts[0], "checks_prior": prior,
            "green": all(run.get("exit") == 0 for run in rows) and None not in counts,
            "deterministic": deterministic,
            "grew": bool(counts and counts[0] is not None and counts[0] > prior),
            "shrank": bool(counts and counts[0] is not None and counts[0] < prior)}

    links_selftest = selftest_state(LINKS, LINKS_PRIOR, 2)
    uncertainty_selftest = selftest_state(UNCERTAINTY, UNCERTAINTY_PRIOR, 1)
    for name, state in (("packet_links", links_selftest),
                        ("packet_uncertainty", uncertainty_selftest)):
        if not state["green"]:
            failures.append(f"{name} --selftest not green: {state['command']}")
        if not state["deterministic"]:
            failures.append(f"{name} --selftest not deterministic across runs")
    if not links_selftest["grew"]:
        failures.append(f"packet_links selftest did not grow past its round-15 stamp "
                        f"({LINKS_PRIOR} checks): now {links_selftest['checks_now']}")
    if uncertainty_selftest["shrank"]:
        failures.append(f"packet_uncertainty selftest shrank below its round-15 stamp "
                        f"({UNCERTAINTY_PRIOR} checks): now {uncertainty_selftest['checks_now']}")

    # regression fixtures (F9-1 + F10-1), fixed commands over this runner's fixture
    fixture_rel, fixture_probes, fixture_clean = o_fixture()
    fixture_path = ROOT / ".scratch" / fixture_rel
    fixture_path.parent.mkdir(exist_ok=True)
    fixture_path.write_text(fixture_probes, encoding="utf-8")
    fixture_run = run_command((LINKS, "--packet", f".scratch/{fixture_rel}",
                               "--repo-root", ".", "--no-digests"))
    clean_path = ROOT / ".scratch" / (fixture_rel.replace(".yml", "-clean.yml"))
    clean_path.write_text(fixture_clean, encoding="utf-8")
    clean_run = run_command((LINKS, "--packet", f".scratch/{fixture_rel.replace('.yml', '-clean.yml')}",
                             "--repo-root", ".", "--no-digests"))
    probe_dangling = run_command((LINKS, "--links", f"{D3_PACKET}#L99", "--repo-root", "."))
    probe_real_id = run_command((LINKS, "--links", f"{D3_PACKET}#L01,{D3_PACKET}#SC1",
                                 "--repo-root", "."))

    fixture_codes = sorted(set(re.findall(r"\b([ELM]-[A-Z-]+)\s+\[",
                                          fixture_run.get("stdout_tail", ""))))
    expected_codes = ["E-EDGE-NO-SOURCE", "E-SOURCE-UNKNOWN"]
    if fixture_run.get("exit") != 1:
        failures.append(f"Aggregate-source fixture not rejected: {fixture_run.get('command')} "
                        f"exit {fixture_run.get('exit')} — expected exit 1")
    if fixture_codes != expected_codes:
        failures.append(f"Aggregate-source fixture codes {fixture_codes} != {expected_codes} "
                        "(E-SOURCE-UNKNOWN per F10-1, E-EDGE-NO-SOURCE for the source-less edge)")
    if clean_run.get("exit") != 0 or re.search(r"\bfindings=[1-9]", clean_run.get("stdout_tail", "")):
        failures.append(f"Clean-edge fixture flagged (harm-none control): exit "
                        f"{clean_run.get('exit')} — {(clean_run.get('stdout_tail') or '')[:200]}")
    if probe_dangling.get("exit") != 1 or "L-SELECTOR-UNRESOLVED" not in probe_dangling.get("stdout_tail", ""):
        failures.append(f"Dangling #L99 probe not rejected (F9-1 control): exit "
                        f"{probe_dangling.get('exit')} — {(probe_dangling.get('stdout_tail') or '')[:200]}")
    if probe_real_id.get("exit") != 0:
        failures.append(f"Real record-id probe (#L01,#SC1) regressed (harm-none control): "
                        f"exit {probe_real_id.get('exit')} — {(probe_real_id.get('stdout_tail') or '')[:200]}")

    # battery over the newest keyed build
    gate_run = uncertainty_run = links_run = None
    scan = None
    links_mode = "digests-on"
    if chosen and not gate_target:
        failures.append(f"Newest keyed build {chosen['stem']} has no markdown twin for "
                        f"the shape gate")
    if gate_target:
        gate_run = run_command((GATE, gate_target))
        scan_match = GATE_SCAN_RE.search(gate_run.get("stdout_tail", ""))
        scan = ({"fields": int(scan_match.group(1)), "fields_total": int(scan_match.group(2)),
                 "glossary_entries": int(scan_match.group(3)), "findings": int(scan_match.group(4))}
                if scan_match else None)
        if gate_run.get("exit") != 0:
            failures.append(f"Shape gate not clean on {gate_target}: exit "
                            f"{gate_run.get('exit')} — {(gate_run.get('stderr_tail') or gate_run.get('stdout_tail') or '')[:200]}")
        if scan is None:
            failures.append(f"Shape gate produced no parsable scan line on {gate_target}")
        else:
            if (scan["fields"], scan["fields_total"]) != (16, 16):
                failures.append(f"Shape gate fields {scan['fields']}/{scan['fields_total']} != 16/16 "
                                f"on {gate_target}")
            if scan["glossary_entries"] != 20 or scan["findings"] != 0:
                failures.append(f"Shape gate glossary {scan['glossary_entries']} entries with "
                                f"{scan['findings']} findings != 20/20 clean on {gate_target}")
        uncertainty_run = run_command((UNCERTAINTY, "--packet", machine))
        if uncertainty_run.get("exit") != 0:
            failures.append(f"packet_uncertainty not clean on {machine}: exit "
                            f"{uncertainty_run.get('exit')} — {(uncertainty_run.get('stderr_tail') or '')[:200]}")
        links_argv = (LINKS, "--packet", machine, "--repo-root", ".")
        if not amended:
            # The filed build pins the pre-edit harness digest by design; judge
            # its links without digests and record the stale pin separately.
            links_argv += ("--no-digests",)
            links_mode = "digests-off (filed build pins the pre-edit harness bytes)"
        links_run = run_command(links_argv)
        if links_run.get("exit") != 0:
            failures.append(f"packet_links not clean on {machine}: exit "
                            f"{links_run.get('exit')} — {(links_run.get('stdout_tail') or links_run.get('stderr_tail') or '')[:240]}")
    digest_state = None
    if machine and links_mode.startswith("digests-on"):
        digest_state = "verified in run"
    elif machine:
        with_digest = run_command((LINKS, "--packet", machine, "--repo-root", "."))
        digest_state = ("stale-pin (M-DIGEST-MISMATCH expected on the filed build; "
                        "clears on the amended build)" if with_digest.get("exit") == 1
                        and "M-DIGEST-MISMATCH" in with_digest.get("stdout_tail", "")
                        else f"exit {with_digest.get('exit')}")

    # F9-2: design §3.2.4 record-coverage census over the chosen build
    census = coverage_census(evidence, packet_md)
    deviation = None
    if census["universe"] and census["orphans"]:
        deviation = coverage_deviation(evidence, paths, census["orphans"])
        if not deviation:
            failures.append(
                f"Design §3.2.4 coverage unmet on {packet_md}: {len(census['orphans'])} "
                f"delivered D3 records have no claim link or edge target: "
                f"{', '.join(census['orphans'][:12])}"
                + (" …" if len(census["orphans"]) > 12 else "")
                + " — and no owner-noted deviation document found in reports/round-16/")

    # filed baseline + no filed churn during validation
    preservation = filed_preservation_current()
    failures.extend(preservation["failures"])

    return result(failures, {
        "packet": {"candidates": candidates, "chosen": chosen,
                   "amended_keyed_build": amended,
                   "filed_build": FILED_PACKET},
        "shape_gate": {"scan": scan, "run": gate_run and {
            "command": gate_run.get("command"), "exit": gate_run.get("exit"),
            "date": gate_run.get("date")}},
        "harness_runs": {
            "packet_links": links_run and {"command": links_run.get("command"),
                                           "exit": links_run.get("exit"),
                                           "stdout_tail": links_run.get("stdout_tail", "")[:400]},
            "packet_uncertainty": uncertainty_run and {
                "command": uncertainty_run.get("command"), "exit": uncertainty_run.get("exit"),
                "stdout_tail": uncertainty_run.get("stdout_tail", "")[:300]},
            "manifest_digests": digest_state},
        "selftests": {"packet_links": links_selftest,
                      "packet_uncertainty": uncertainty_selftest,
                      "prior_stamp": "reports/round-15/handoff/review-10.md §F10-2 (19/19, 31/31)"},
        "regression_controls": {
            "aggregate_source_fixture": {
                "command": fixture_run.get("command"), "exit": fixture_run.get("exit"),
                "codes": fixture_codes, "date": fixture_run.get("date"),
                "fixture": f".scratch/{fixture_rel}"},
            "clean_edge_fixture": {"command": clean_run.get("command"),
                                   "exit": clean_run.get("exit"), "date": clean_run.get("date")},
            "dangling_l99_probe": {"command": probe_dangling.get("command"),
                                   "exit": probe_dangling.get("exit"),
                                   "date": probe_dangling.get("date")},
            "real_id_probe": {"command": probe_real_id.get("command"),
                              "exit": probe_real_id.get("exit"), "date": probe_real_id.get("date")}},
        "f9_2_coverage": {**census, "deviation_docs": deviation},
        "filed_bytes": preservation,
    }, missing=([] if chosen else ["reports/round-16/handoff/packet-<key>.md"])
        + ([] if amended or not chosen else [f"reports/round-16/ or round-15 handoff: amended keyed packet build"]))


def filed_preservation_current():
    claims = strict_json((ROOT / ROUND_DIR / "claims.json").read_text(encoding="utf-8")) \
        if (ROOT / ROUND_DIR / "claims.json").is_file() else {}
    return filed_preservation(claims.get("baseline_revision"))


# --------------------------------------------------------- F9-2 coverage


def section_tables(text, section):
    """Markdown pipe tables under `## … <section>`: [(header, rows)]."""
    tables = []
    lines = text.splitlines()
    in_section = False
    header = None
    body = []
    for line in lines:
        heading = re.match(r"#{1,6}\s+(.*)", line)
        if heading:
            if in_section and header and body:
                tables.append((header, body))
            in_section = section.lower() in heading.group(1).lower()
            header, body = None, []
            continue
        if not in_section:
            continue
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", cell) for cell in cells if cell):
                continue
            if header is None:
                header = [cell.lower() for cell in cells]
            else:
                body.append(cells)
    if in_section and header and body:
        tables.append((header, body))
    return tables


def column(header, names, body):
    index = next((i for i, name in enumerate(header) if any(token in name for token in names)), None)
    if index is None:
        return []
    values = []
    for cells in body:
        if index < len(cells):
            values.append(cells[index])
    return values


def d3_record_universe(evidence):
    """Delivered D3 record ids: every top-level list-of-{id} collection."""
    payload = evidence.document(D3_PACKET)
    universe = {}
    if isinstance(payload, dict):
        for key, value in sorted(payload.items()):
            if (isinstance(value, list) and value
                    and all(isinstance(row, dict) and row.get(RECORD_ID_KEY) for row in value)):
                universe[key] = sorted({str(row[RECORD_ID_KEY]) for row in value})
    return universe


def id_boundary(text, record_id):
    return re.search(r"(?<![A-Za-z0-9_-])" + re.escape(record_id) + r"(?![A-Za-z0-9_-])",
                     text) is not None


def coverage_census(evidence, packet_md):
    """§3.2.4 census: every delivered D3 record id surfaced by the packet.

    Universe: every top-level `examples/culture-d3/packet.json` collection of
    `{id: …}` rows (lexemes, names, utterances, materials, objects, costumes,
    symbols, beliefs, eras, sound_changes, speech_rules, references, bridges,
    rank_rules). A record is covered when it appears in a claim-link cell, an
    edge target, an edge source, or as an edge_id (row-by-row carriage — the
    review-9 precedent that a record carried as its own edge row is not
    orphaned). Calibrated against the finding of record: on packet-v2-05.md
    this rule reproduces review-9.md F9-2's orphan list exactly (18 lexemes,
    6 names, M01–M03, O02–O03, U03–U06 = 33). The §3.2.4 letter rule
    (claim link or edge target only) is recorded alongside for comparison.
    """
    universe = d3_record_universe(evidence)
    if not packet_md:
        return {"universe": universe, "universe_size": metric(0, "delivered D3 record ids"),
                "orphans": [], "census_run": False,
                "note": "no packet build to census"}
    text = evidence.text(packet_md)
    link_cells = []
    for header, body in section_tables(text, "claim_ledger"):
        link_cells.extend(column(header, ("link",), body))
    target_cells, source_cells, edge_id_cells = [], [], []
    for header, body in section_tables(text, "coupling_edges"):
        target_cells.extend(column(header, ("target",), body))
        source_cells.extend(column(header, ("source",), body))
        edge_id_cells.extend(column(header, ("edge",), body))
    rule_text = "\n".join(link_cells + target_cells)
    surfaced_text = "\n".join(link_cells + target_cells + source_cells + edge_id_cells)
    orphans, letter_orphans, coverage = [], [], {}
    for collection, ids in universe.items():
        for record_id in ids:
            hit = id_boundary(rule_text, record_id)
            surfaced = id_boundary(surfaced_text, record_id)
            coverage[record_id] = ("claim-link-or-edge-target" if hit else
                                   ("edge-source-or-edge-row" if surfaced else "orphan"))
            if not surfaced:
                orphans.append(record_id)
            if not hit:
                letter_orphans.append(record_id)
    return {"universe": universe,
            "universe_size": metric(sum(len(ids) for ids in universe.values()),
                                    "delivered D3 record ids from examples/culture-d3/packet.json"),
            "census_run": True, "packet": packet_md,
            "calibration": "reproduces reports/round-15/handoff/review-9.md F9-2 "
                           "orphan list (33) on packet-v2-05.md",
            "rule_coverage": metric(
                sum(1 for state in coverage.values() if state == "claim-link-or-edge-target"),
                "record ids covered by a claim link or edge target (design §3.2.4 letter)"),
            "surfaced_coverage": metric(
                sum(1 for state in coverage.values() if state != "orphan"),
                "record ids surfaced by any claim link, edge target, source, or edge row"),
            "orphans": orphans, "letter_rule_orphans": letter_orphans,
            "per_record": coverage}


def coverage_deviation(evidence, paths, orphans):
    """A round-16 document noting the §3.2.4 deviation with an owner."""
    docs = []
    for relative in paths:
        if not relative.endswith((".md", ".json")) or relative in EXCLUDE_NAMES:
            continue
        text = evidence.text(relative)
        if not text or not re.search(r"3\.2\.4|orphan|coverage", text, re.I):
            continue
        named = [record_id for record_id in orphans if id_boundary(text, record_id)]
        owner = re.search(r"\bowner\s*[:\-]\s*(\S[^\n]{0,80})", text, re.I)
        if named and owner:
            docs.append({"path": relative, "orphan_ids_named": len(named),
                         "owner": owner.group(1).strip(),
                         "dated": bool(DATE_RE.search(text))})
    return docs or None


# ---------------------------------------------------------------- fixture


def o_fixture():
    """F9-1 + F10-1 falsification fixtures and the harm-none positive.

    Two packet fixtures, written by the runner into .scratch/ (gitignored) in
    the lane's canonical yaml_lines serializer form (`tools/assemble-d2.py`
    yaml_lines: list items sit two columns DEEPER than their key; hand-written
    same-column dash lists truncate in the shared reader). A probe packet
    whose edges carry a prose aggregate source and no source at all over
    otherwise-valid records (expected exactly E-SOURCE-UNKNOWN +
    E-EDGE-NO-SOURCE, exit 1), and a clean packet whose only edge names a
    real source, a real target, and a real claim (expected zero findings,
    exit 0). The bare --links probes run against the live D3 packet: #L99
    must be rejected (the F9-1 dangling bypass, review-9.md reproduction)
    while #L01 and #SC1 must still resolve.
    """
    fixture = """artifact_manifest:
  -
    artifact_id: A-D3
    path: examples/culture-d3/packet.json
    record_ids:
      - SC1
claim_ledger:
  -
    claim_id: CLX-1
coupling_edges:
  -
    edge_id: E-AGG-SURVIVOR
    source: 29 coupling_note fields over examples/culture-d2/packet.d2.yml
    relation: dependency
    target_ids:
      - SC1
    claims:
      - CLX-1
  -
    edge_id: E-NOSRC
    relation: dependency
    target_ids:
      - SC1
    claims:
      - CLX-1
"""
    clean = """artifact_manifest:
  -
    artifact_id: A-D3
    path: examples/culture-d3/packet.json
    record_ids:
      - SC1
claim_ledger:
  -
    claim_id: CLX-1
coupling_edges:
  -
    edge_id: E-CLEAN
    source: SC1
    relation: dependency
    target_ids:
      - SC1
    claims:
      - CLX-1
"""
    return "r16-validation-fixture.yml", fixture, clean


# -------------------------------------------------------------- validation


def guard_preflight():
    spec = importlib.util.spec_from_file_location("round16_receipt_guard", ROOT / GUARD)
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
    paths = round16_files()
    coverage = measure_c(evidence)
    operability = measure_o(evidence, paths)
    results = {"C": coverage, "O": operability}
    guard_run = run_command((GUARD, "--selftest"))
    if guard_run.get("exit") != 0:
        results["O"]["failures"].append("Receipt guard selftest not green")
        results["O"]["passed"] = False
    results["O"]["measurement"]["guard_selftest"] = {
        "command": guard_run.get("command"), "exit": guard_run.get("exit"),
        "date": guard_run.get("date")}
    after = filed_snapshot()
    changes = [{"path": path, "before": before.get(path), "after": after.get(path)}
               for path in sorted(before.keys() | after.keys()) if before.get(path) != after.get(path)]
    if changes:
        for item in results.values():
            item["failures"].append("Filed round-8..15 bytes/path set changed during "
                                    "validation; rerun on a settled tree")
            item["passed"] = False
    declared = {claim.get("id"): claim.get("axis") for claim in claims.get("claims", [])
                if isinstance(claim, dict)}
    if declared != {"C": "coverage", "O": "operability"}:
        results["O"]["failures"].append(f"Round-16 declared claims do not match C/O: {declared}")
        results["O"]["passed"] = False
    if evidence.errors:
        # unreadable/invalid evidence is a real failure for whichever claim
        # consumed it; civ-map absence is already a C failure, not noise here
        for error in evidence.errors:
            consumer = "C" if CIV_MAP in error or CIV_DIR in error else "O"
            results[consumer]["failures"].append(error)
            results[consumer]["passed"] = False
    return {
        "round": 16, "runner": RUNNER, "runner_sha256": sha((ROOT / RUNNER).read_bytes()),
        "counting_command": COMMAND, "date": today(),
        "baseline_revision": claims.get("baseline_revision"), "targets_date": targets.get("date"),
        "claims_declared": declared,
        "acceptance_checks_passed": all(item["passed"] for item in results.values()),
        "claims": results, "input_sha256": dict(sorted(evidence.inputs.items())),
        "failures": [f"claim {claim_id}: {failure}" for claim_id, item in results.items()
                     for failure in item["failures"]],
        "missing_dependencies": sorted({path for item in results.values()
                                        for path in item["missing_dependencies"]}),
        "filed_rounds": {"baseline": results["O"]["measurement"]["filed_bytes"],
                         "changed_during_validation": changes,
                         "command": f"{COMMAND} (hash filed round-8..15 paths before/after checks)",
                         "date": today()},
        "limits": [
            "Historical validators are never executed. Only fixed read-only "
            "check/selftest commands and this runner's own .scratch falsification "
            "fixtures run; no command is executed from an evidence file.",
            "Filed rounds 8-15 are compared with the declared baseline; any "
            "non-append-only byte change or churn during validation fails closed. "
            "A NEW keyed packet build may be added; filed bytes are never rewritten.",
            "Claim C is a coverage/staleness map: statuses are receipts that a "
            "re-check or correction happened, with the cited evidence. The "
            "freshness axis-move remains paused (LOG.md pause record); no source "
            "freshness verdict, re-grade, or rank change is issued or implied.",
            "The §3.2.4 census judges surfacing of delivered D3 record ids on "
            "the packet text: a record counts as surfaced when it appears in a "
            "claim link, an edge target, an edge source, or as an edge row id "
            "(the review-9 precedent that a record carried as its own edge row "
            "is not orphaned). The rule was calibrated to reproduce review-9.md "
            "F9-2's orphan list exactly on packet-v2-05.md; the §3.2.4 letter "
            "count (claim link or edge target only) is recorded alongside. The "
            "census does not judge whether a link's target record is "
            "semantically apt. D2 surfaced records are pinned by the "
            "artifact_manifest record_ids column plus packet_links' own "
            "E-TARGET-UNKNOWN checks, not re-censused here.",
            "Selftest growth is judged against the round-15 stamped inventory "
            "(19/19, 31/31 in review-10.md §F10-2): the link judge must grow; "
            "the uncertainty judge must stay green and not shrink.",
            "Observation from fixture construction (no action by this runner): "
            "the lane's yaml_lines reader keeps only the last item of a "
            "hand-written same-column dash list under a key; the canonical "
            "serializer form (tools/assemble-d2.py yaml_lines, items two "
            "columns deeper than the key) parses fully. Packet authors should "
            "emit lists via the serializer form.",
            "All artifacts measured are NON-CANON; this receipt does not certify "
            "truth, canon, lore receipt, or a transfer acceptance.",
        ],
    }


# ---------------------------------------------------------------- selftest


def selftest():
    controls = []

    def check(name, value):
        controls.append({"control": name, "passed": bool(value)})

    check("status-normalized", normalize_status("Stale_Fixed") == "stale-fixed"
          and normalize_status("CURRENT") == "current")
    check("status-vocab-held", normalize_status("freshness-verdict") not in STATUS_VOCAB)
    check("entry-paths-normalized",
          normalize_entry("corpus/knowledge/civilizations/ainu.md") == "ainu"
          and normalize_entry("ainu.md") == "ainu" and normalize_entry("ainu") == "ainu")
    check("map-containers-accepted",
          map_rows({"rows": [1]}) == [1] and map_rows([2]) == [2]
          and map_rows({"entries": [3]}) == [3] and map_rows({"x": 1}) is None)
    good_rows = [
        {"entry": "ainu", "status": "current",
         "checked": f"{today()} via python3 tools/x.py"},
        {"entry": "rome", "status": "stale-fixed", "evidence": "corpus/knowledge/x.md"},
        {"entry": "kush", "status": "stale-documented", "reason": "primary corpus gone"},
    ]
    for row in good_rows:
        requirement = STATUS_REQUIREMENTS[row["status"]]
        check(f"row-requirements-ok-{row['entry']}", requirement(row_text(row)))
    bad_rows = [
        {"entry": "a", "status": "current", "checked": "2020-01-01 python3 x"},
        {"entry": "b", "status": "current", "checked": f"{today()}"},
        {"entry": "c", "status": "stale-fixed", "note": "trust me"},
        {"entry": "d", "status": "stale-documented", "reason": "TBD"},
    ]
    for row in bad_rows:
        requirement = STATUS_REQUIREMENTS[row["status"]]
        check(f"row-requirements-reject-{row['entry']}", not requirement(row_text(row)))
    entries = ["ainu", "rome"]
    rows = [{"entry": "ainu"}, {"entry": "rome"}]
    named = [row_entry(row) for row in rows]
    check("set-equality-symmetric",
          set(named) == set(entries) and len(named) == len(entries))
    dup = [row_entry(row) for row in [{"entry": "ainu"}, {"entry": "ainu"}]]
    check("duplicate-detected", len(dup) != len(set(dup)))
    census_text = "links: A-02#lexicon.L03, examples/culture-d3/packet.json#SC1 | targets: U01, M-01"
    check("id-boundary-matches", id_boundary(census_text, "L03")
          and id_boundary(census_text, "SC1") and id_boundary(census_text, "U01")
          and id_boundary(census_text, "M-01"))
    check("id-boundary-precise", not id_boundary(census_text, "L3")
          and not id_boundary(census_text, "U011") and not id_boundary(census_text, "M-1")
          and not id_boundary("L010 L011", "L01"))
    md = """## claim_ledger

| claim_id | links |
|---|---|
| CL1 | A-02#lexicon.L01, A-02#names.N01 |

## coupling_edges

| edge_id | source | relation | target_ids | claims |
|---|---|---|---|---|
| BR01 | S01 | method-transfer | U01, U02 | CL1 |
| D2E-01 | M-01 | spine-independence | M-01 | CL1 |
"""
    ledger = section_tables(md, "claim_ledger")
    edges = section_tables(md, "coupling_edges")
    check("section-tables-split", len(ledger) == 1 and len(edges) == 1)
    check("links-column-extracted",
          column(ledger[0][0], ("link",), ledger[0][1]) ==
          ["A-02#lexicon.L01, A-02#names.N01"])
    check("edge-columns-extracted",
          column(edges[0][0], ("target",), edges[0][1]) == ["U01, U02", "M-01"]
          and column(edges[0][0], ("source",), edges[0][1]) == ["S01", "M-01"])
    check("section-scan-stops",
          section_tables(md, "glossary") == [])
    fixture_rel, fixture, clean = o_fixture()
    check("fixture-names-aggregate-survivor",
          "E-AGG-SURVIVOR" in fixture and "coupling_note fields over" in fixture)
    check("fixture-clean-edge-real-records",
          "source: SC1" in clean and "      - SC1" in clean and "      - CLX-1" in clean)
    check("gate-scan-parsed",
          GATE_SCAN_RE.search("INFO scan: fields=16/16 glossary-entries=20 findings=0").groups()
          == ("16", "16", "20", "0"))
    check("gate-scan-absent", GATE_SCAN_RE.search("nothing") is None)
    check("selftest-count-parsed",
          SELFTEST_COUNT_RE.search("selftest: 38 checks passed (...)").group(1) == "38")
    sample_candidates = [
        {"dir": "reports/round-16", "stem": "packet-v3-02", "attempt": 2,
         "md": "reports/round-16/packet-v3-02.md", "yml": None},
        {"dir": "reports/round-15/handoff", "stem": "packet-v2-05", "attempt": 5,
         "md": "reports/round-15/handoff/packet-v2-05.md",
         "yml": "reports/round-15/handoff/packet-v2-05.yml"},
    ]
    ranked = sorted(sample_candidates,
                    key=lambda item: (item["dir"] != ROUND_DIR, -item["attempt"], item["stem"]))
    check("packet-ranking-round16-first", ranked[0]["dir"] == ROUND_DIR)
    check("packet-amendment-detected",
          bool(ranked[0]["dir"] == ROUND_DIR
               or ranked[0]["stem"] != Path(FILED_PACKET).name))
    check("filed-build-not-amended",
          is_amended(ranked[0]) and not is_amended(ranked[1]))
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
    auditor = (f"Date: {today()}. command: python3 tools/x.py --civ ainu\n"
               "spot-check verdicts: ainu ok, rome ok, kush ok, carthage ok, "
               "celts ok, byzantium ok, maya-classic ok, inca ok, ottoman ok, "
               "ryukyu ok\n")
    state = audit_receipt_state(auditor)
    named = sorted({entry for entry in
                    ["ainu", "rome", "kush", "carthage", "celts", "byzantium",
                     "maya-classic", "inca", "ottoman", "ryukyu"]
                    if id_boundary(auditor, entry)})
    check("auditor-receipt-dated-commanded", state["dated"] and state["command_carried"])
    check("auditor-names-ten", len(named) == 10)
    undated_auditor = "spot-check: ainu ok, rome ok (no date, no command)"
    check("undated-auditor-rejected",
          not all(audit_receipt_state(undated_auditor).values()))
    sample = metric(94, "count corpus entries")
    check("metric-carries-command-and-date",
          sample["command"].startswith(COMMAND) and sample["date"] == today()
          and sample["value"] == 94)
    payload = {"runner": RUNNER, "command": COMMAND + " --selftest", "date": today(),
               "selftest_passed": all(item["passed"] for item in controls), "controls": controls,
               "passed": metric(sum(item["passed"] for item in controls), "validator selftest controls"),
               "total": metric(len(controls), "validator selftest control inventory")}
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["selftest_passed"] else 1


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate round-16 C/O without touching filed rounds 8-15.")
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
