#!/usr/bin/env python3
"""Round-10 acceptance runner — claims C / F / O (kotodama-shokunin).

X03 deliverable: one runner that grades the round-10 evidence over the three
declared claims and exits 0 only when all three pass. It writes exactly one
file — ``reports/round-10/validation.json`` — and never edits the evidence it
reads (no commits, no report rewrites, no corpus writes).

Claim contracts, as declared in ``reports/round-10/claims.json``:

C (coverage)  >=10 new sourced knowledge entries across the four thin
              partitions (linguistics >=2, myth-symbol >=2, culture-material
              >=2, verification >=2); each with complete source/verified-at/
              recheck frontmatter (plus the lane's topic/couples profile), a
              named gap, a decision-record section, and at least one
              retrievable locator (existing repo path or URL); corpus/README.md
              index rows and per-partition counts match the actual files; the
              source-audit inventory total matches the disk count.
F (freshness) a drift ledger covering every command cited in SKILL.md and
              every SCORECARD counting command, re-run with observed
              output_sha256 + exit + verdict (current | stale-fixed |
              stale-documented); stale rows carry fix evidence or a documented
              reason (zero silent staleness); 13 shard fragments; an
              independent drift audit with >=10 re-runs and zero unexplained
              mismatches; registry rows matched against the live gate files.
O (operability) a findings tracker covering every finding in the four
              adversarial-review files (rounds 8-9), every row dispositioned
              (fixed-with-control demonstrated, or wont-fix/wrong with a
              reason); four verifier verdicts; a scribe report stating zero
              undispositioned rows.

Usage::

    python3 reports/round-10/run-validation.py        # writes validation.json

Exit: 0 = all three claims pass; 1 = at least one fails (the receipt lists
every failure and the artifacts still missing).

The runner is fail-closed: an absent artifact is a failure, not a skip. It
executes no gate and re-runs none of the ledger's commands; it validates the
structure, completeness, and cross-file agreement of the landed evidence, plus
the one cheap counting command the corpus itself cites
(``tools/source-audit-inventory.py``). Author-side only: it admits nothing,
certifies no canon, and replaces no independent promotion review.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SELF_REL = "reports/round-10/run-validation.py"
CLAIMS_REL = "reports/round-10/claims.json"
TARGETS_REL = "reports/round-10/targets.json"
OUTPUT_REL = "reports/round-10/validation.json"

COVERAGE_DIR_REL = "reports/round-10/coverage"
DRIFT_DIR_REL = "reports/round-10/drift"
LEDGER_REL = "reports/round-10/drift/ledger.json"
DRIFT_AUDIT_REL = "reports/round-10/drift/audit.md"
TRACKER_REL = "reports/round-10/findings-tracker.json"
SCRIBE_REL = "reports/round-10/findings-scribe.md"

SKILL_REL = "SKILL.md"
SCORECARD_REL = "SCORECARD.md"
README_REL = "corpus/README.md"
REGISTRY_REL = "reports/round-9/baselines/registry.md"
KNOWLEDGE_REL = "corpus/knowledge"
PARTITIONS = ("linguistics", "myth-symbol", "culture-material",
              "synthesis", "verification", "civilizations")
THIN_PARTITIONS = ("linguistics", "myth-symbol", "culture-material",
                   "verification")
C_PARTITION_MINIMUMS = {"linguistics": 2, "myth-symbol": 2,
                        "culture-material": 2, "verification": 2}
C_MIN_ENTRIES = 10
C_FRONTMATTER_FIELDS = ("topic", "sources", "verified-at", "recheck",
                        "couples")
F_MIN_SHARDS = 13
F_MIN_AUDIT_RERUNS = 10
O_MIN_VERIFY_FILES = 4

# The four adversarial-review files named by claim O, and the finding IDs each
# file declares. IDs come from two heading shapes the files actually use:
# ``^##+ <ID> — ...`` (S2, F1, ...) and bold ``**F-D17-N ...**`` inline
# findings. The extraction is re-done at run time and reported in the receipt.
FINDING_SOURCES = (
    "reports/round-8/depth/findings.md",
    "reports/round-8/depth/findings-17.md",
    "reports/round-9/d3/findings.md",
    "reports/round-9/d3/findings-10.md",
)
FINDING_ID_HEADING = re.compile(r"^#{2,4}\s+([SF]\d+[a-z]?)\s+[—–-]")
FINDING_ID_BOLD = re.compile(r"\*\*(F-D\d+-\d+)\b")

INVENTORY_COMMAND = ("python3", "tools/source-audit-inventory.py", "--json",
                     "--summary", "--root", "corpus/knowledge")

VERDICTS = ("current", "stale-fixed", "stale-documented")
PENDING_LABELS = re.compile(r"^\s*(pending|open|todo|tbd|unset|none|)$", re.I)
FIXED_LABELS = re.compile(r"fixed|repaired|closed|resolved|re-?verif", re.I)
DOCUMENTED_LABELS = re.compile(r"wont[- ]?fix|won't fix|wrong|documented|"
                               r"accept|risk|out[- ]of[- ]scope|"
                               r"not[- ]a[- ]defect|informational", re.I)
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
URL_RE = re.compile(r"https?://[^\s`)\]]+")
REPO_PATH_RE = re.compile(r"\b((?:corpus|tools|reports|examples)/[\w./-]+"
                          r"\.(?:md|json|py|yml|yaml|tsv|txt))\b")


def sha256_file(relative: str):
    path = ROOT / relative
    if not path.is_file():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 16), b""):
            digest.update(chunk)
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
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def git(*args, timeout=60):
    try:
        proc = subprocess.run(("git",) + args, cwd=ROOT, timeout=timeout,
                              capture_output=True, text=True)
    except (OSError, subprocess.SubprocessError):
        return None
    if proc.returncode != 0:
        return None
    return proc.stdout


def norm_script(token: str) -> str:
    token = token.strip().strip("`'\"")
    while token.startswith("./"):
        token = token[2:]
    return token


def command_key(command: str):
    """(script, frozenset(flags)) for a python3 command line, or None.

    Positional arguments are deliberately dropped: the drift ledger records a
    re-run of the command's script+mode, not the exact fixture path. The
    special ``python3 -c`` inline form keys as ("python3 -c", ()).
    """
    tokens = [t for t in command.strip().strip("`").split() if t]
    if not tokens or not tokens[0].endswith("python3"):
        return None
    tokens = tokens[1:]
    if not tokens:
        return None
    if tokens[0] == "-c":
        return ("python3 -c", frozenset())
    script = norm_script(tokens[0])
    if not script.endswith(".py"):
        return None
    flags = frozenset(t for t in tokens[1:] if t.startswith("--"))
    return (script, flags)


def extract_cited_commands(text: str, locator: str):
    """Cited python3 commands in a markdown surface, keyed for comparison.

    A key is required for every script named in a ``python3 <script>`` code
    span. A ``--selftest``/``--self-test`` key is required for the script the
    flag is attached to: the same code span when the span names a script, or —
    for a bare ``--selftest`` cell in a single-script table row (the SKILL.md
    gate tables) — that row's only script.
    """
    required = {}
    for number, line in enumerate(text.splitlines(), 1):
        scripts = {norm_script(s)
                   for s in re.findall(r"(?:tools|reports)/[\w./-]+\.py",
                                       line)}
        if not scripts:
            continue
        for command in re.findall(r"`([^`]*python3[^`]*)`", line):
            key = command_key(command)
            if key is None:
                continue
            if key[0] in scripts:
                required.setdefault(key, []).append(f"{locator}:{number}")
        for span in re.findall(r"`([^`]*)`", line):
            if "--selftest" not in span and "--self-test" not in span:
                continue
            span_scripts = {norm_script(s) for s in
                            re.findall(r"(?:tools|reports)/[\w./-]+\.py",
                                       span)}
            if span_scripts:
                targets = span_scripts & scripts
            elif line.lstrip().startswith("|") and len(scripts) == 1:
                targets = scripts
            else:
                targets = set()
            for script in targets:
                required.setdefault((script, frozenset({"--selftest"})),
                                    []).append(f"{locator}:{number}")
    return required


def ledger_keys(rows):
    keys = []
    for row in rows:
        command = row.get("command")
        if isinstance(command, str):
            key = command_key(command)
            if key is not None:
                keys.append((key, row))
    return keys


def covers(required_key, ledger_rows):
    script, flags = required_key
    exact = None
    superset = None
    for key, row in ledger_keys(ledger_rows):
        if key[0] != script:
            continue
        if key[1] == flags and exact is None:
            exact = row
        elif flags and flags <= key[1] and superset is None:
            superset = row
    if exact is not None:
        return exact
    if superset is not None:
        return superset
    if script == "python3 -c":
        for row in ledger_rows:
            command = row.get("command")
            if isinstance(command, str) and (
                    "availability-attempt-1.json" in command
                    or "python3 -c" in command):
                return row
    return None


def stated_reason(row):
    """First non-empty documented-reason field of a ledger row.

    Literal null placeholders (``None``/``null``/``n/a``) do not count as a
    stated reason.
    """
    for key in ("reason", "documented_reason", "note", "rationale"):
        value = row.get(key)
        if value is None:
            continue
        text = str(value).strip()
        if text and text.lower() not in ("none", "null", "n/a", "-"):
            return text
    return ""


def extract_finding_ids(text: str):
    ids = []
    for line in text.splitlines():
        match = FINDING_ID_HEADING.match(line)
        if match:
            ids.append(match.group(1))
    ids.extend(FINDING_ID_BOLD.findall(text))
    seen, ordered = set(), []
    for finding_id in ids:
        if finding_id not in seen:
            seen.add(finding_id)
            ordered.append(finding_id)
    return ordered


def id_in_text(finding_id: str, text: str) -> bool:
    pattern = r"(?<![A-Za-z0-9-])" + re.escape(finding_id) + r"(?![A-Za-z0-9-])"
    return re.search(pattern, text) is not None


def normalize_source(value: str) -> str:
    value = str(value).strip().strip("`'\"")
    while value.startswith("./"):
        value = value[2:]
    return value


def same_file(candidate: str, declared: str) -> bool:
    candidate = normalize_source(candidate)
    declared = normalize_source(declared)
    if candidate == declared:
        return True
    if candidate.endswith("/" + declared) or declared.endswith("/" + candidate):
        return True
    return Path(candidate).name == Path(declared).name and (
        Path(declared).parent.name in Path(candidate).parts)


# --------------------------------------------------------------------------
# C — coverage
# --------------------------------------------------------------------------

def discover_new_entries():
    """Entries added since the declared baseline, committed or not."""
    baseline = (load_json(CLAIMS_REL) or {}).get("baseline_revision")
    found = {}
    notes = []
    untracked = git("ls-files", "--others", "--exclude-standard", "--",
                    KNOWLEDGE_REL)
    if untracked is None:
        notes.append("git ls-files --others failed")
    else:
        for line in untracked.splitlines():
            line = line.strip()
            if line.endswith(".md") and "/" in line:
                found[line] = "untracked"
    if baseline:
        added = git("diff", "--name-status", "--diff-filter=A", baseline,
                    "--", KNOWLEDGE_REL)
        if added is None:
            notes.append(f"git diff --diff-filter=A {baseline[:9]} failed")
        else:
            for line in added.splitlines():
                parts = line.split("\t")
                if len(parts) >= 2 and parts[-1].strip().endswith(".md"):
                    found.setdefault(parts[-1].strip(), "added-vs-baseline")
    else:
        notes.append("claims.json carries no baseline_revision")
    return found, notes


def entry_checks(relative: str):
    text = read_text(relative)
    report = {"missing_frontmatter": [], "gap": False,
              "decision_record": False, "locators": [],
              "frontmatter_lines": {}}
    for field in C_FRONTMATTER_FIELDS:
        match = re.search(rf"(?m)^\s*[-*]?\s*{re.escape(field)}\s*:\s*(\S.*)$",
                          text)
        if match is None:
            report["missing_frontmatter"].append(field)
        else:
            report["frontmatter_lines"][field] = match.group(1).strip()
    # gap named: a frontmatter field, an inline "Gap filled:" clause, or a
    # body heading that names the gap
    gap_field = re.search(r"(?i)(?:^|[\s.;—–|-])gap(?:[\s-]+(?:filled|"
                          r"addressed|served))?\s*:\s*(\S[^\n]{0,300})", text)
    gap_heading = re.search(r"(?mi)^#{2,4}[^\n]*\bgap\b[^\n]*\n(?:[^\n]*\n)*?"
                            r"[^\n\s][^\n]*$", text)
    report["gap"] = bool(gap_field or gap_heading)
    decision = re.search(r"(?mi)^#{2,4}[^\n]*decision[- ]record[^\n]*\n+"
                         r"\s*(\S[^\n]*)", text)
    report["decision_record"] = bool(decision)
    # retrievable locators: repo paths that exist, or URLs
    for token in REPO_PATH_RE.findall(text):
        if (ROOT / token).exists() and token not in report["locators"]:
            report["locators"].append(token)
    if URL_RE.search(text):
        report["locators"].append("(url)")
    return report


def readme_index():
    text = read_text(README_REL)
    declared, rows, current = {}, {}, None
    for line in text.splitlines():
        heading = re.match(r"^##\s+([a-z][a-z-]*)/\s*\((\d+)\)\s*$", line)
        if heading:
            current = heading.group(1)
            declared[current] = int(heading.group(2))
            rows.setdefault(current, set())
            continue
        if line.startswith("## "):
            current = None
            continue
        if current is not None:
            row = re.match(r"^-\s+`([^`]+\.md)`", line)
            if row:
                rows[current].add(row.group(1))
    total = re.search(r"(?m)^Total knowledge entries:\s*(\d+)\.", text)
    return {"declared": declared, "rows": rows,
            "total_declared": int(total.group(1)) if total else None}


def run_inventory():
    try:
        proc = subprocess.run(INVENTORY_COMMAND, cwd=ROOT, timeout=120,
                              capture_output=True, text=True)
    except (OSError, subprocess.SubprocessError) as error:
        return {"exit": None, "error": str(error)[:200], "total": None}
    total = None
    try:
        payload = json.loads(proc.stdout)
        total = (payload.get("totals") or {}).get("files")
    except (json.JSONDecodeError, AttributeError):
        pass
    return {"exit": proc.returncode, "error": None, "total": total,
            "stderr": proc.stderr.strip()[:200]}


def measure_c():
    failures, missing = [], []
    entries, notes = discover_new_entries()
    if notes:
        failures.extend(f"entry discovery: {note}" for note in notes)
    counts = {partition: 0 for partition in PARTITIONS}
    entry_reports = {}
    for relative in sorted(entries):
        partition = Path(relative).parent.name
        if partition in counts:
            counts[partition] += 1
        report = entry_checks(relative)
        entry_reports[relative] = report
        if report["missing_frontmatter"]:
            failures.append(
                f"{relative}: incomplete frontmatter, missing "
                f"{', '.join(report['missing_frontmatter'])}")
        if not report["gap"]:
            failures.append(f"{relative}: no named gap (filler risk)")
        if not report["decision_record"]:
            failures.append(f"{relative}: no decision-record section")
        if not report["locators"]:
            failures.append(
                f"{relative}: no retrievable locator (existing repo path or "
                f"URL)")
    if len(entries) < C_MIN_ENTRIES:
        failures.append(
            f"coverage: {len(entries)} new entries < required "
            f"{C_MIN_ENTRIES}")
    for partition, minimum in C_PARTITION_MINIMUMS.items():
        if counts.get(partition, 0) < minimum:
            failures.append(
                f"coverage: partition {partition} has {counts.get(partition, 0)}"
                f" new entries < required {minimum}")

    index = readme_index()
    actual = {}
    for partition in PARTITIONS:
        directory = ROOT / KNOWLEDGE_REL / partition
        actual[partition] = sorted(p.name for p in directory.glob("*.md")) \
            if directory.is_dir() else []
    for partition in PARTITIONS:
        if index["declared"].get(partition) != len(actual[partition]):
            failures.append(
                f"README: {partition} heading declares "
                f"{index['declared'].get(partition)} but "
                f"{len(actual[partition])} files exist")
        missing_rows = set(actual[partition]) - index["rows"].get(partition,
                                                                  set())
        phantom_rows = index["rows"].get(partition, set()) - set(
            actual[partition])
        for slug in sorted(missing_rows):
            failures.append(f"README: no index row for {partition}/{slug}")
        for slug in sorted(phantom_rows):
            failures.append(f"README: index row without file {partition}/{slug}")
    total_actual = sum(len(actual[p]) for p in PARTITIONS)
    if index["total_declared"] != total_actual:
        failures.append(
            f"README: total line declares {index['total_declared']} but "
            f"{total_actual} files exist")

    inventory = run_inventory()
    if inventory["exit"] != 0 or inventory["total"] is None:
        missing.append(" ".join(INVENTORY_COMMAND))
        failures.append(
            f"inventory: source-audit-inventory exit {inventory['exit']} "
            f"(no parseable total)")
    elif inventory["total"] != total_actual:
        failures.append(
            f"inventory: reported {inventory['total']} files != "
            f"{total_actual} on disk")

    coverage_dir = ROOT / COVERAGE_DIR_REL
    fragments = sorted(p.name for p in coverage_dir.glob("*.md")) \
        if coverage_dir.is_dir() else []
    review_fragments = [f for f in fragments if f.startswith("review-")]
    audit_fragments = [f for f in fragments if f.startswith("audit-")]
    authorship = [f for f in fragments
                  if not f.startswith("review-")
                  and not f.startswith("audit-")
                  and f != "index-update.md"]
    if not (coverage_dir / "index-update.md").is_file():
        missing.append(f"{COVERAGE_DIR_REL}/index-update.md")
        failures.append("coverage: index-update.md fragment absent")
    else:
        update_text = read_text(f"{COVERAGE_DIR_REL}/index-update.md")
        if "python3" not in update_text or not re.search(r"\d", update_text):
            failures.append(
                "coverage: index-update.md records no sweep command/count")
    if len(audit_fragments) < len(THIN_PARTITIONS):
        failures.append(
            f"coverage: {len(audit_fragments)} audit fragments < required "
            f"{len(THIN_PARTITIONS)}")
    if len(authorship) < C_MIN_ENTRIES:
        failures.append(
            f"coverage: {len(authorship)} authorship fragments < required "
            f"{C_MIN_ENTRIES}")
    if len(review_fragments) < C_MIN_ENTRIES:
        failures.append(
            f"coverage: {len(review_fragments)} review fragments < required "
            f"{C_MIN_ENTRIES}")
    corpus_text = "\n".join(
        read_text(f"{COVERAGE_DIR_REL}/{name}") for name in fragments)
    unmentioned = [relative for relative in sorted(entries)
                   if Path(relative).name not in corpus_text
                   and relative not in corpus_text]
    for relative in unmentioned:
        failures.append(
            f"coverage: no fragment mentions new entry {relative}")

    return {
        "passed": not failures,
        "failures": failures,
        "measurement": {
            "new_entries": len(entries),
            "entry_origins": entries,
            "partition_counts": counts,
            "partition_minimums": C_PARTITION_MINIMUMS,
            "entry_reports": entry_reports,
            "readme": {
                "declared_counts": index["declared"],
                "actual_counts": {p: len(actual[p]) for p in PARTITIONS},
                "total_declared": index["total_declared"],
                "total_actual": total_actual,
            },
            "inventory": inventory,
            "fragments": {
                "authorship": len(authorship),
                "review": len(review_fragments),
                "audit": len(audit_fragments),
                "index_update": (coverage_dir / "index-update.md").is_file(),
            },
        },
        "missing_dependencies": missing,
    }


# --------------------------------------------------------------------------
# F — freshness / drift
# --------------------------------------------------------------------------

def measure_f():
    failures, missing = [], []
    required = {}
    for relative in (SKILL_REL, SCORECARD_REL):
        required.update(extract_cited_commands(read_text(relative), relative))

    drift_dir = ROOT / DRIFT_DIR_REL
    shards = sorted(p.name for p in drift_dir.glob("shard-*.md")) \
        if drift_dir.is_dir() else []
    other_fragments = sorted(p.name for p in drift_dir.glob("*.md")
                             if p.name != "audit.md") \
        if drift_dir.is_dir() else []
    if len(shards) < F_MIN_SHARDS:
        failures.append(
            f"drift: {len(shards)} shard-*.md fragments < required "
            f"{F_MIN_SHARDS}")

    ledger_present = (ROOT / LEDGER_REL).is_file()
    ledger_rows = []
    if not ledger_present:
        missing.append(LEDGER_REL)
        failures.append("drift: ledger.json absent")
    else:
        payload = load_json(LEDGER_REL)
        if isinstance(payload, dict):
            for key in ("rows", "entries", "ledger", "commands"):
                if isinstance(payload.get(key), list):
                    ledger_rows = payload[key]
                    break
            else:
                ledger_rows = [value for value in payload.values()
                               if isinstance(value, dict)]
        elif isinstance(payload, list):
            ledger_rows = payload
        if not ledger_rows:
            failures.append("drift: ledger.json carries no readable rows")
        for position, row in enumerate(ledger_rows):
            if not isinstance(row, dict):
                failures.append(f"drift: ledger row {position} is not an object")
                continue
            label = f"drift: ledger row {position}"
            command = row.get("command")
            if not isinstance(command, str) or not command.strip():
                failures.append(f"{label}: missing command")
            if not str(row.get("source_locator") or "").strip():
                failures.append(f"{label}: missing source_locator")
            verdict = row.get("round10_verdict", row.get("verdict"))
            if verdict not in VERDICTS:
                failures.append(
                    f"{label}: verdict {verdict!r} not in {VERDICTS} "
                    f"(silent staleness)")
                continue
            digest = row.get("output_sha256")
            if not (isinstance(digest, str) and SHA256_RE.match(digest)):
                if not (verdict == "stale-documented" and stated_reason(row)):
                    failures.append(
                        f"{label}: output_sha256 missing/not 64-hex")
            exit_code = row.get("exit")
            if isinstance(exit_code, str) and exit_code.strip().isdigit():
                exit_code = int(exit_code.strip())
            if not isinstance(exit_code, int):
                if not (verdict == "stale-documented" and stated_reason(row)):
                    failures.append(f"{label}: exit missing/not an integer")
            if verdict == "stale-fixed":
                evidence = [row.get(key) for key in
                            ("fix", "fix_evidence", "fixed_in", "evidence")
                            if row.get(key)]
                ok = False
                for item in evidence:
                    text = str(item)
                    path = normalize_source(text)
                    if (ROOT / path).exists():
                        ok = True
                    elif re.search(r"python3 |exit\s*[:=]?\s*\d|sha256",
                                    text):
                        ok = True
                if not ok:
                    failures.append(
                        f"{label}: stale-fixed without demonstrated fix "
                        f"evidence")
            if verdict == "stale-documented":
                reason = stated_reason(row)
                if len(reason) < 12:
                    failures.append(
                        f"{label}: stale-documented without a stated reason")

        missing_keys = []
        for key in sorted(required, key=lambda item: (item[0], sorted(item[1]))):
            if covers(key, ledger_rows) is None:
                missing_keys.append({"command": "python3 " + key[0] +
                                     (" " + " ".join(sorted(key[1]))
                                      if key[1] else ""),
                                     "cited_at": required[key]})
        if missing_keys:
            failures.append(
                f"drift: ledger covers {len(required) - len(missing_keys)}/"
                f"{len(required)} cited commands; {len(missing_keys)} missing")
    if not ledger_present:
        missing_keys = [
            {"command": "python3 " + key[0] +
             (" " + " ".join(sorted(key[1])) if key[1] else ""),
             "cited_at": required[key]}
            for key in sorted(required, key=lambda item: (item[0],
                                                          sorted(item[1])))]

    audit_present = (ROOT / DRIFT_AUDIT_REL).is_file()
    audit_commands, audit_mismatches = [], []
    if not audit_present:
        missing.append(DRIFT_AUDIT_REL)
        failures.append("drift: audit.md absent")
    else:
        audit_text = read_text(DRIFT_AUDIT_REL)
        audit_commands = sorted(set(
            match.strip() for match in
            re.findall(r"python3 [^\n`]+", audit_text)))
        if len(audit_commands) < F_MIN_AUDIT_RERUNS:
            failures.append(
                f"drift: audit.md shows {len(audit_commands)} re-run "
                f"commands < required {F_MIN_AUDIT_RERUNS}")
        for match in re.finditer(r"(?i)mismatch\w*[^0-9\n]{0,24}(\d+)",
                                 audit_text):
            if int(match.group(1)) > 0:
                audit_mismatches.append(match.group(0).strip()[:120])
        for match in re.finditer(r"(\d+)\s+mismatch", audit_text):
            if int(match.group(1)) > 0:
                audit_mismatches.append(match.group(0).strip()[:120])
        if audit_mismatches:
            failures.append(
                f"drift: audit.md records {len(audit_mismatches)} "
                f"unexplained mismatch reading(s): "
                f"{audit_mismatches[:3]}")

    registry_text = read_text(REGISTRY_REL)
    live_gates = sorted(p.name for p in (ROOT / "tools/gates").glob("*.py")) \
        if (ROOT / "tools/gates").is_dir() else []
    drift_text = "\n".join(
        [read_text(f"{DRIFT_DIR_REL}/{name}") for name in other_fragments]
        + [read_text(DRIFT_AUDIT_REL)]
        + [row.get("command", "") for row in ledger_rows
           if isinstance(row, dict)])
    registry_gates = sorted(set(re.findall(r"gates/([\w-]+)\.py",
                                           registry_text)))
    live_stems = sorted(Path(name).stem for name in live_gates)
    for stem in live_stems:
        if stem not in drift_text:
            failures.append(
                f"drift: live gate {stem} not named in any drift artifact "
                f"(registry match unrecorded)")
    if "registry.md" not in drift_text and "registry" not in drift_text.lower():
        failures.append(
            "drift: no drift artifact records the registry.md re-measurement")
    if not registry_gates:
        failures.append(
            f"drift: {REGISTRY_REL} names no gate scripts to match")

    return {
        "passed": not failures,
        "failures": failures,
        "measurement": {
            "required_command_keys": len(required),
            "required_commands": [
                {"command": "python3 " + key[0] +
                 (" " + " ".join(sorted(key[1])) if key[1] else ""),
                 "cited_at": required[key]}
                for key in sorted(required, key=lambda item: (item[0],
                                                              sorted(item[1])))],
            "missing_keys": missing_keys,
            "ledger_rows": len(ledger_rows),
            "verdict_counts": {
                verdict: sum(1 for row in ledger_rows if isinstance(row, dict)
                             and row.get("round10_verdict",
                                         row.get("verdict")) == verdict)
                for verdict in VERDICTS},
            "shards": len(shards),
            "drift_fragments": len(other_fragments),
            "audit": {"present": audit_present,
                      "rerun_commands": len(audit_commands),
                      "mismatch_readings": audit_mismatches},
            "registry": {"live_gates": live_gates,
                         "gates_named_in_registry": registry_gates},
        },
        "missing_dependencies": missing,
    }


# --------------------------------------------------------------------------
# O — operability / findings closure
# --------------------------------------------------------------------------

def tracker_rows(payload):
    if isinstance(payload, list):
        return [row for row in payload if isinstance(row, dict)]
    if isinstance(payload, dict):
        for key in ("findings", "rows", "items", "tracker", "entries"):
            if isinstance(payload.get(key), list):
                return [row for row in payload[key] if isinstance(row, dict)]
    return []


def measure_o():
    failures, missing = [], []
    source_ids = {}
    for relative in FINDING_SOURCES:
        text = read_text(relative)
        if not text:
            missing.append(relative)
            failures.append(f"findings: source file {relative} unreadable")
            continue
        ids = extract_finding_ids(text)
        if not ids:
            failures.append(
                f"findings: no finding IDs extractable from {relative}")
        source_ids[relative] = ids

    tracker_present = (ROOT / TRACKER_REL).is_file()
    rows, pending_rows, bad_labels = [], [], []
    fixed_without_control, documented_without_reason = [], []
    covered_ids = {}
    if not tracker_present:
        missing.append(TRACKER_REL)
        failures.append("findings: findings-tracker.json absent")
    else:
        payload = load_json(TRACKER_REL)
        if payload is None:
            failures.append("findings: findings-tracker.json unparseable")
        rows = tracker_rows(payload)
        if not rows:
            failures.append("findings: tracker carries no rows")
        for position, row in enumerate(rows):
            label = f"findings: tracker row {position}"
            for field in ("idx", "source_file", "finding", "severity",
                          "disposition"):
                value = row.get(field)
                if value is None or not str(value).strip():
                    failures.append(f"{label}: missing {field}")
            disposition = str(row.get("disposition")
                              or row.get("status") or "").strip()
            if PENDING_LABELS.match(disposition):
                pending_rows.append(position)
                continue
            if FIXED_LABELS.search(disposition):
                evidence = [row.get(key) for key in
                            ("control", "control_evidence", "evidence",
                             "control_command", "control_exit",
                             "demonstrated_by")
                            if row.get(key)]
                ok = False
                for item in evidence:
                    text = str(item)
                    if (ROOT / normalize_source(text)).exists():
                        ok = True
                    elif re.search(r"python3 |exit\s*[:=]?\s*\d|sha256|"
                                   r"\d+/\d+", text):
                        ok = True
                if not ok:
                    fixed_without_control.append(position)
            elif DOCUMENTED_LABELS.search(disposition):
                reason = str(row.get("reason")
                             or row.get("documented_reason")
                             or row.get("note") or row.get("rationale")
                             or "").strip()
                if len(reason) < 12:
                    documented_without_reason.append(position)
            else:
                bad_labels.append({"row": position,
                                   "disposition": disposition[:80]})
        if pending_rows:
            failures.append(
                f"findings: {len(pending_rows)} tracker row(s) still pending: "
                f"{pending_rows[:6]}")
        if bad_labels:
            failures.append(
                f"findings: {len(bad_labels)} row(s) with unrecognized "
                f"disposition label (fail-closed): {bad_labels[:3]}")
        if fixed_without_control:
            failures.append(
                f"findings: {len(fixed_without_control)} fixed row(s) without "
                f"a demonstrated control: {fixed_without_control[:6]}")
        if documented_without_reason:
            failures.append(
                f"findings: {len(documented_without_reason)} documented "
                f"row(s) without a stated reason: "
                f"{documented_without_reason[:6]}")

        for relative, ids in source_ids.items():
            file_rows = [row for row in rows
                         if same_file(str(row.get("source_file") or ""),
                                      relative)]
            if not file_rows:
                failures.append(
                    f"findings: no tracker row references {relative}")
                continue
            file_text = "\n".join(json.dumps(row, ensure_ascii=False)
                                  for row in file_rows)
            missing_ids = [finding_id for finding_id in ids
                           if not id_in_text(finding_id, file_text)]
            covered_ids[relative] = {
                "declared": ids,
                "missing": missing_ids,
                "rows": len(file_rows),
            }
            for finding_id in missing_ids:
                failures.append(
                    f"findings: {finding_id} from {relative} has no tracker "
                    f"row")

    verify_files = sorted(p.name for p in (ROOT / "reports/round-10")
                          .glob("findings-verify-*.md")) \
        if (ROOT / "reports/round-10").is_dir() else []
    if len(verify_files) < O_MIN_VERIFY_FILES:
        failures.append(
            f"findings: {len(verify_files)} verifier verdict files < "
            f"required {O_MIN_VERIFY_FILES}")

    scribe_present = (ROOT / SCRIBE_REL).is_file()
    scribe_green = False
    if not scribe_present:
        missing.append(SCRIBE_REL)
        failures.append("findings: findings-scribe.md absent")
    else:
        scribe_text = read_text(SCRIBE_REL)
        green_patterns = (
            r"(?i)(zero|no|0)\s+(undispositioned|un-dispositioned|"
            r"without disposition|pending)",
            r"(?i)(undispositioned|un-dispositioned|pending)\s*[:=]\s*"
            r"(0|none|zero)",
            r"(?i)all\s+\d+\s+(findings\s+)?dispositioned",
        )
        scribe_green = any(re.search(pattern, scribe_text)
                           for pattern in green_patterns)
        contradiction = re.search(
            r"(?i)(?:still|remain|remains|remaining)\s+(?:open|pending|"
            r"undispositioned|un-dispositioned)", scribe_text)
        if contradiction:
            failures.append(
                "findings: findings-scribe.md states no zero-undispositioned "
                f"result (contradiction: {contradiction.group(0)!r})")
        elif not scribe_green:
            failures.append(
                "findings: findings-scribe.md states no zero-undispositioned "
                "result")
        if "tracker" not in scribe_text.lower():
            failures.append(
                "findings: findings-scribe.md does not reference the tracker")

    return {
        "passed": not failures,
        "failures": failures,
        "measurement": {
            "tracker": {"present": tracker_present, "rows": len(rows),
                        "pending_rows": pending_rows,
                        "unrecognized_labels": bad_labels,
                        "fixed_without_control": fixed_without_control,
                        "documented_without_reason":
                            documented_without_reason},
            "source_coverage": covered_ids,
            "verify_files": verify_files,
            "scribe": {"present": scribe_present, "green": scribe_green},
        },
        "missing_dependencies": missing,
    }


# --------------------------------------------------------------------------
# receipt
# --------------------------------------------------------------------------

def main():
    claims = load_json(CLAIMS_REL) or {}
    results = {"C": measure_c(), "F": measure_f(), "O": measure_o()}
    passed = all(result["passed"] for result in results.values())

    missing = sorted({item for result in results.values()
                      for item in result["missing_dependencies"]})
    consumed = {CLAIMS_REL, TARGETS_REL, SKILL_REL, SCORECARD_REL, README_REL,
                REGISTRY_REL, LEDGER_REL, DRIFT_AUDIT_REL, TRACKER_REL,
                SCRIBE_REL, *FINDING_SOURCES}
    for result in results.values():
        measurement = result["measurement"]
        consumed.update(measurement.get("entry_origins", {}))
        for relative in measurement.get("entry_reports", {}):
            consumed.add(relative)
        consumed.update(measurement.get("verify_files", []))
    coverage_dir = ROOT / COVERAGE_DIR_REL
    if coverage_dir.is_dir():
        consumed.update(f"{COVERAGE_DIR_REL}/{p.name}"
                        for p in coverage_dir.glob("*.md"))
    drift_dir = ROOT / DRIFT_DIR_REL
    if drift_dir.is_dir():
        consumed.update(f"{DRIFT_DIR_REL}/{p.name}"
                        for p in drift_dir.glob("*.md"))
    consumed.update(f"reports/round-10/{name}"
                    for name in results["O"]["measurement"]["verify_files"])

    receipt = {
        "round": 10,
        "runner": SELF_REL,
        "runner_sha256": sha256_file(SELF_REL),
        "counting_command": "python3 reports/round-10/run-validation.py",
        "claims_declared": {claim["id"]: claim["axis"]
                            for claim in claims.get("claims", [])},
        "baseline_revision": claims.get("baseline_revision"),
        "date": claims.get("date"),
        "thresholds": {
            "C": {"min_new_entries": C_MIN_ENTRIES,
                  "partition_minimums": C_PARTITION_MINIMUMS,
                  "frontmatter_fields": list(C_FRONTMATTER_FIELDS),
                  "requires": ["named gap", "decision-record section",
                               "retrievable locator (existing repo path or "
                               "URL)", "README counts/rows == files",
                               "inventory total == files",
                               ">=10 authorship + >=10 review + "
                               "index-update + 4 audit fragments"],
                  "discovery": "git untracked ∪ git diff --diff-filter=A "
                               "vs claims.json baseline_revision"},
            "F": {"min_shards": F_MIN_SHARDS,
                  "min_audit_reruns": F_MIN_AUDIT_RERUNS,
                  "verdicts": list(VERDICTS),
                  "stale_fixed_requires": "fix evidence (existing path or "
                                          "command/exit/sha256)",
                  "stale_documented_requires": "stated reason >= 12 chars "
                                               "(reason/documented_reason/"
                                               "note/rationale; a literal "
                                               "'None' placeholder does not "
                                               "count)",
                  "coverage_rule": "every python3 command cited in SKILL.md "
                                   "and SCORECARD.md, keyed script+flags; "
                                   "--selftest is attributed only to the "
                                   "script its span names (or the single "
                                   "script of a table row)",
                  "exit_rule": "int, or a digit string coerced to int",
                  "registry_rule": "every live tools/gates/*.py named in a "
                                   "drift artifact; registry.md re-measured"},
            "O": {"min_verify_files": O_MIN_VERIFY_FILES,
                  "pending_rule": "no row label in "
                                  "{pending,open,todo,tbd,unset,none,empty}",
                  "fixed_rule": "control evidence present (existing path or "
                                "command/exit/sha256/count)",
                  "documented_rule": "reason >= 12 chars",
                  "coverage_rule": "every extracted finding ID per source "
                                   "file appears in a row for that file",
                  "scribe_rule": "zero-undispositioned statement + tracker "
                                 "reference"},
        },
        "acceptance_checks_passed": passed,
        "claims": results,
        "failures": [f"claim {claim_id}: {failure}"
                     for claim_id in ("C", "F", "O")
                     for failure in results[claim_id]["failures"]],
        "missing_dependencies": missing,
        "input_sha256": {relative: sha256_file(relative)
                         for relative in sorted(consumed)
                         if sha256_file(relative) is not None},
        "limits": [
            "Structural/evidence-presence checks, not quotation truth, "
            "historical authenticity or cultural permission. Author-side "
            "only; no admission, promotion or canon decision.",
            "Entry discovery uses git (untracked ∪ added-vs-baseline); a "
            "staged-only or renamed-existing file is not counted as new. "
            "Frontmatter completeness reads the lane's topic/sources/"
            "verified-at/recheck/couples profile (QUALITY.md/README); the "
            "claim minimum is sources/verified-at/recheck.",
            "The gap check accepts a frontmatter gap field or a body "
            "heading/line naming the gap; it verifies that a gap is named, "
            "not that the gap is genuine — reviewers own that judgement.",
            "Locator resolvability requires an existing repo path or a URL; "
            "bibliographic citations without a path/URL do not count as the "
            "retrievable-locator leg.",
            "F command coverage is keyed by script + --flags; positional "
            "fixture arguments are not compared, and the inline "
            "python3 -c SCORECARD count matches on its JSON target. Cited "
            "commands are checked for ledger presence, not re-executed here.",
            "Drift mismatch detection is regex-based over audit.md prose; a "
            "positive mismatch reading fails the claim so that it cannot be "
            "silently absorbed.",
            "O finding-ID extraction covers the two heading shapes the four "
            "source files use (numbered headings and bold F-D17-N markers); "
            "findings-17.md's case tables are covered by the row-per-file "
            "requirement plus its three F-D17 IDs.",
            "This runner executes no gate, battery or previous-round "
            "runner; 'no previously green check regresses' is read through "
            "the F ledger rows for those cited commands, not re-measured "
            "here.",
            "Calibration controls (disposable, untracked): "
            ".scratch/r10x03/make-fixture.py builds a hardlink fixture tree "
            "that passes all three claims, and .scratch/r10x03/controls.py "
            "plants 18 defects (dropped entry, broken frontmatter, README "
            "count/row drift, ledger gaps and silent staleness, audit "
            "absence/mismatch, pending or control-less tracker rows, a red "
            "scribe, missing verifier files) — each was caught with exit 1 "
            "and the expected failure text on 2026-10-17. Scratch is not a "
            "deliverable and is not required for this runner to work.",
        ],
    }
    output = ROOT / OUTPUT_REL
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                 ensure_ascii=False) + "\n",
                      encoding="utf-8")
    for claim_id in ("C", "F", "O"):
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
