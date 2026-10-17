#!/usr/bin/env python3
"""Round-8 local acceptance runner (shard R8-O15): measures claims F, O and D
against reports/round-8/claims.json and reports/round-8/targets.json.

Run:  python3 reports/round-8/run-validation.py

Writes ONLY reports/round-8/validation.json in this repository (no scratch, no
network). The receipt is deterministic: sorted keys, no wall-clock timestamps,
no temporary paths, sha256 digests of every consumed input. Missing worker
evidence is recorded as a failing dependency with the exact missing paths --
never synthesized, and expectations are never weakened to fit a defect.

Claim F (freshness): the fifteen declared residuals R8-F01..R8-F15 must each
carry a round-8 receipt under reports/round-8/freshness/ that is either a
retrieved-passage record (source URL, accessed-at date, quoted passage with a
named location, support scope) or a documented access failure (attempted
command and status); at least eight receipts must carry a substantive
retrieved passage (>= 10 whitespace tokens, named location, not
bibliographic); passage support and whole-claim support must live in separate
fields per receipt; reports/round-8/freshness/reconciliation.json must bind
exactly the fifteen ids with a raw worker label preserved next to a distinct
reconciled disposition, and that raw label must match the round-6 ledger's own
worker verdict for the row (the receipts' prior-disposition fields are audit
dispositions, so a mismatch there is recorded as a note, not a failure).
Receipts are read structurally at any nesting depth: quoted passages inside
retrieval lists inherit their record's URL and accessed-at date, and access
failures count as attempt+status pairs anywhere in the tree.

Claim O (operability): the R8-O02 harness fix (tools/harness/r8_checks.py)
must run --selftest green with both named semantics demonstrated (benign
duplicate receipt accepted, genuine identity collision still rejected); the
R8-O03 defect inventory must cover the parser defects D1..D9 of supplemental
review 26 and the selftest/regex findings F1 and F5 of review 29 (D10 and the
frozen-boundary findings are optional coverage), each repaired or quarantined
with a documented reason, and every repaired defect must be referenced by an
isolated negative control that exits 0 on the live tree; a defect is repaired
only when every control that references it passes, so a control reporting the
pre-fix pattern leaves its defect unrepaired. reports/round-8/operability/
battery-rerun.json must record both legacy selftests at exit 0 and the runner
re-executes both on the delivered tree, accepting a stale stdout hash only when
the tool bytes themselves changed after the receipt (the receipt's own declared
caveat) and rejecting any unexplained drift. Control stdout digests are taken
after normalizing temporary paths and timestamps, so the receipt is
reproducible across runs.

Claim D (depth): tools/d2-typed-labels.py --selftest must pass with malformed
controls and no traceback; the D2 packet must regenerate deterministically
(tools/assemble-d2.py --check) and a round-8/D2 frozen manifest must replay
through tools/replay-frozen.py with zero mismatch and zero could-not-evaluate
rows; SKILL.md must carry the label-typing decision table; SCORECARD.md must
carry the d2-typed-labels capability row only alongside a demonstrated run.
When --check fails, the runner diagnoses the packet's embedded reader_sha256
pin against the live reader file, because repairing that shared reader makes
the deterministic assembly differ by exactly that pinned line.

Acceptance reading (declared, not weakened): at least one legacy defect must
be actually repaired (an all-quarantine inventory would leave the O before-
state materially unchanged); a legacy manifest (round-3/round-4) is not
accepted as D replay evidence because its gate digests legitimately drifted.

Stdlib only; read-only over repository inputs; the only write is the receipt
file below the runner's own round-8 report directory.
"""

import collections
import copy
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "reports/round-8"
CLAIMS_REL = "reports/round-8/claims.json"
TARGETS_REL = "reports/round-8/targets.json"
FRESHNESS_DIR = HERE / "freshness"
RECONCILIATION_REL = "reports/round-8/freshness/reconciliation.json"
OPERABILITY_DIR = HERE / "operability"
DEPTH_DIR = HERE / "depth"
NEG_CONTROLS_DIR = OPERABILITY_DIR / "neg-controls"
BATTERY_RERUN_REL = "reports/round-8/operability/battery-rerun.json"
DEFECT_INVENTORY_REL = "reports/round-8/operability/defect-inventory.json"
HARNESS_FIX_REL = "reports/round-8/operability/harness-fix.json"
HARNESS_REL = "tools/harness/r8_checks.py"
D2_TOOL_REL = "tools/d2-typed-labels.py"
D2_ASSEMBLER_REL = "tools/assemble-d2.py"
REPLAY_REL = "tools/replay-frozen.py"
BATTERY_REL = "tools/check-gate-battery.py"
CRAFT_REL = "tools/check-craft-exercise.py"
SKILL_REL = "SKILL.md"
SCORECARD_REL = "SCORECARD.md"
REVIEW_26_REL = "reports/supplement-opencode-1/26-parser-controls.md"
REVIEW_29_REL = "reports/supplement-opencode-1/29-local-boundaries.md"
ROUND7_DIR_REL = "reports/round-7/"
OUTPUT_REL = "reports/round-8/validation.json"

F_MIN_SUBSTANTIVE = 8
F_MIN_TOKENS = 10
CONTROL_TIMEOUT = 120

ID_FIELDS = ("id", "row_id", "question_id", "receipt_id", "target_id", "declared_id")
RAW_FIELDS = ("raw_label", "worker_label", "raw_verdict", "worker_verdict",
              "raw_result", "original_label", "raw_disposition")
RECONCILED_FIELDS = ("reconciled_disposition", "reconciled", "parent_disposition",
                     "reconciled_label", "parent_reconciled", "reconciled_result")
EXCERPT_FIELDS = ("source_excerpt", "excerpt", "quoted_passage", "passage_text",
                  "passage", "quote")
STATUS_FIELDS = ("status", "status_code", "http_status", "error_status",
                 "access_status", "result_status", "outcome_status")
NODE_EXCERPT_FIELDS = ("source_excerpt", "excerpt", "quotation", "quote",
                       "quote_text", "passage_text", "text")
NODE_LOCATOR_FIELDS = ("source_locator", "locator", "location", "passage_location",
                       "source_location", "section", "page", "pages", "line",
                       "lines", "range")
NODE_URL_FIELDS = ("source_url", "url", "href", "link")
NODE_ACCESSED_FIELDS = ("accessed_at", "accessed", "access_date", "checked_at",
                        "retrieved_at", "timestamp")
ATTEMPT_FIELDS = ("attempted_command", "attempted", "attempt", "command",
                  "request", "attempted_request")
PASSAGE_LEG_RE = re.compile(r"passage|excerpt|quote|support_scope", re.I)
CLAIM_LEG_RE = re.compile(r"whole[_ ]?claim|claim|disposition|verdict|^result$"
                          r"|support_label|reconciled", re.I)
RAW_LABEL_KEY_RE = re.compile(r"raw_worker_label|raw_label|worker_label|raw_verdict"
                              r"|prior_disposition|prior_worker_label", re.I)
BIBLIOGRAPHIC_KINDS = {"bibliography", "bibliographic", "bibliographies"}
PASSAGE_MIN_TOKENS = 3
CONTAINER_KEYS = ("rows", "receipts", "entries", "records", "questions",
                  "results", "items", "freshness")
INVENTORY_KEYS = ("defects", "entries", "inventory", "rows", "items")
SEPARATION_LEG_MARKERS = {
    "pre_fix": re.compile(r"pre[-_ ]?fix|fail[-_ ]?before|before[-_ ]?fix|prefix_sha|pre-fix",
                          re.I),
    "post_fix": re.compile(r"post[-_ ]?fix|pass[-_ ]?after|after[-_ ]?fix|live|fixed",
                           re.I),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(relative):
    path = ROOT / relative
    return sha(path.read_bytes()) if path.is_file() else None


def load_json(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def norm(value):
    return " ".join(str(value).split())


def tokens(value):
    return norm(value).split()


TIMESTAMP_RE = re.compile(r"\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}"
                          r"(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:?\d{2})?)?")
SCRATCH_RE = re.compile(r"/(?:var/)?tmp/[^\s\"'<>]+")


def sanitize(text, limit=400):
    """Normalize temporary paths and timestamps so recorded output and its
    digest are reproducible across runs."""
    text = SCRATCH_RE.sub("<scratch>", text or "")
    text = TIMESTAMP_RE.sub("<date>", text)
    text = " ".join(text.split())
    return text[:limit]


def run_cli(relative, args=(), timeout=CONTROL_TIMEOUT):
    argv = [sys.executable, relative, *args]
    try:
        proc = subprocess.run(argv, cwd=str(ROOT), capture_output=True,
                              timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"argv": argv, "exit": None, "timeout": True,
                "stdout": "", "stderr": "", "stdout_sha256": None,
                "stderr_sha256": None}
    except OSError as error:
        return {"argv": argv, "exit": None, "timeout": False,
                "stdout": "", "stderr": str(error), "stdout_sha256": None,
                "stderr_sha256": None}
    out = proc.stdout.decode("utf-8", "replace")
    err = proc.stderr.decode("utf-8", "replace")
    return {"argv": argv, "exit": proc.returncode, "timeout": False,
            "stdout": out, "stderr": err, "stdout_sha256": sha(out.encode()),
            "stderr_sha256": sha(err.encode())}


def first_key(record, fields):
    for field in fields:
        if field in record:
            return field
    return None


def first_text(record, fields):
    for field in fields:
        value = record.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def first_value(record, fields):
    for field in fields:
        if field in record and record[field] is not None:
            return record[field]
    return None


def boolish(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.strip().casefold()
        if lowered in ("true", "yes", "1"):
            return True
        if lowered in ("false", "no", "0"):
            return False
    return None


def bibliographic(record):
    for field in ("bibliographic", "is_bibliographic"):
        if boolish(record.get(field)) is True:
            return True
    if boolish(record.get("directly_relevant_nonbibliographic")) is False:
        return True
    kind = str(first_value(record, ("source_kind", "source_type", "kind")) or "")
    return kind.strip().casefold() in ("bibliography", "bibliographic")


def canonical(record):
    return json.dumps(record, sort_keys=True, ensure_ascii=False)


# --------------------------------------------------------------------------
# claim F — freshness receipts
# --------------------------------------------------------------------------

def declared_freshness():
    return load_json(TARGETS_REL)["freshness"]


def iter_records(document):
    if isinstance(document, list):
        for item in document:
            if isinstance(item, dict):
                yield item
        return
    if not isinstance(document, dict):
        return
    yielded = False
    for key in CONTAINER_KEYS:
        value = document.get(key)
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    yield item
            yielded = True
    if not yielded:
        yield document


def resolve_id(record, stem, declared_ids, prior_map):
    candidates = []
    for field in ID_FIELDS:
        value = record.get(field)
        if isinstance(value, str) and value.strip():
            candidates.append(value.strip())
    if record.get("prior_row_id"):
        candidates.append(str(record["prior_row_id"]))
    if stem:
        candidates.append(stem)
    for candidate in candidates:
        upper = candidate.upper().replace("_", "-").replace(" ", "")
        if upper in declared_ids:
            return upper
        if upper in prior_map:
            return prior_map[upper]
        match = re.fullmatch(r"(?:R8-)?F?0*(\d{1,2})", upper)
        if match:
            guess = f"R8-F{int(match.group(1)):02d}"
            if guess in declared_ids:
                return guess
    return None


def load_freshness(declared_rows):
    declared_ids = {row["id"] for row in declared_rows}
    prior_map = {row.get("prior_row_id", "").upper(): row["id"]
                 for row in declared_rows if row.get("prior_row_id")}
    grouped = collections.defaultdict(list)
    sources = {}
    problems = []
    if FRESHNESS_DIR.is_dir():
        paths = sorted(FRESHNESS_DIR.rglob("*.json")) + sorted(FRESHNESS_DIR.rglob("*.jsonl"))
        for path in paths:
            relative = str(path.relative_to(ROOT))
            if path.name == "reconciliation.json":
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except OSError as error:
                problems.append(f"{relative}: unreadable ({error})")
                continue
            documents = []
            if path.suffix == ".jsonl":
                for line in text.splitlines():
                    if line.strip():
                        try:
                            documents.append(json.loads(line))
                        except json.JSONDecodeError as error:
                            problems.append(f"{relative}: bad JSON line ({error})")
            else:
                try:
                    documents.append(json.loads(text))
                except json.JSONDecodeError as error:
                    problems.append(f"{relative}: bad JSON ({error})")
                    continue
            for document in documents:
                for record in iter_records(document):
                    row_id = resolve_id(record, path.stem, declared_ids, prior_map)
                    if row_id is None:
                        continue
                    grouped[row_id].append(record)
                    sources.setdefault(row_id, relative)
    records = {}
    mirrors = {}
    collisions = []
    for row_id in sorted(grouped):
        group = grouped[row_id]
        payloads = {canonical(record) for record in group}
        if len(payloads) == 1:
            records[row_id] = group[0]
            mirrors[row_id] = len(group) - 1
            continue
        richest = max(group, key=lambda record: (len(record), canonical(record)))
        if all(set(record.items()) <= set(richest.items()) for record in group):
            records[row_id] = richest
            mirrors[row_id] = len(group) - 1
        else:
            collisions.append(row_id)
            records[row_id] = richest
    return {"records": records, "mirrors": mirrors, "collisions": collisions,
            "sources": sources, "problems": problems}


def walk_dicts(node, path="", inherited=None):
    """Yield (path, node, context) for every dict node, carrying the nearest
    source context (url / accessed / locator) down the tree, so a quoted
    passage nested inside a retrieval record inherits that record's URL."""
    if not isinstance(node, dict):
        return
    context = dict(inherited or {})
    for field in NODE_URL_FIELDS:
        value = node.get(field)
        if isinstance(value, str) and value.strip():
            context["url"] = value.strip()
            break
    for field in NODE_ACCESSED_FIELDS:
        value = node.get(field)
        if isinstance(value, str) and value.strip():
            context["accessed"] = value.strip()
            break
    own_locator = first_text(node, NODE_LOCATOR_FIELDS)
    if own_locator:
        context["locator"] = own_locator
    yield path, node, context
    for key, value in node.items():
        if isinstance(value, dict):
            yield from walk_dicts(value, f"{path}{key}.", context)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                if isinstance(item, dict):
                    yield from walk_dicts(item, f"{path}{key}[{index}].", context)


def receipt_passages(receipt):
    """Quoted passages with a source URL and a named location, found at any
    nesting depth. `tokens` separates substantive (>= F_MIN_TOKENS) from merely
    present (>= PASSAGE_MIN_TOKENS) passages; `locator_scope` records whether
    the location is the passage's own or inherited from its retrieval record."""
    passages = []

    def consider(text, path, node, context):
        count = len(tokens(text))
        if count < PASSAGE_MIN_TOKENS:
            return
        if boolish(node.get("retrieved_passage")) is False:
            return
        kind = str(node.get("source_kind", "")).strip().casefold()
        if kind in BIBLIOGRAPHIC_KINDS or bibliographic(node):
            return
        url = context.get("url", "")
        own_locator = first_text(node, NODE_LOCATOR_FIELDS)
        locator = own_locator or context.get("locator", "")
        if not url or not locator:
            return
        passages.append({"path": path, "tokens": count, "url": url,
                         "locator_scope": "own" if own_locator else "inherited",
                         "key": (url, norm(locator).casefold(),
                                 norm(text).casefold())})

    def visit(node, path, context):
        if not isinstance(node, dict):
            return
        context = dict(context)
        for field in NODE_URL_FIELDS:
            value = node.get(field)
            if isinstance(value, str) and value.strip():
                context["url"] = value.strip()
                break
        for field in NODE_ACCESSED_FIELDS:
            value = node.get(field)
            if isinstance(value, str) and value.strip():
                context["accessed"] = value.strip()
                break
        own_locator = first_text(node, NODE_LOCATOR_FIELDS)
        if own_locator:
            context["locator"] = own_locator
        text = first_text(node, NODE_EXCERPT_FIELDS)
        if text:
            consider(text, path, node, context)
        for key, value in node.items():
            if isinstance(value, dict):
                visit(value, f"{path}{key}.", context)
            elif isinstance(value, list):
                quote_list = re.search(r"quot|excerpt|passage", key, re.I)
                for index, item in enumerate(value):
                    if isinstance(item, dict):
                        visit(item, f"{path}{key}[{index}].", context)
                    elif quote_list and isinstance(item, str):
                        consider(item, f"{path}{key}[{index}]", node, context)

    visit(receipt, "", {})
    return passages


def receipt_failures(receipt):
    """Documented access failures: any nested record with an attempted command
    and a status."""
    found = []
    for path, node, _context in walk_dicts(receipt):
        attempt = first_text(node, ATTEMPT_FIELDS)
        status = first_value(node, STATUS_FIELDS)
        if attempt and status is not None and norm(str(status)):
            found.append({"path": path, "attempt": sanitize(attempt, 120),
                          "status": sanitize(str(status), 120)})
    return found


def receipt_legs(receipt):
    """Passage-level support and whole-claim support as distinct fields (any
    nesting depth). Keys naming both legs at once are ambiguous and skipped."""
    passage_paths, claim_paths = [], []
    for path, node, _context in walk_dicts(receipt):
        for key, value in node.items():
            full = f"{path}{key}"
            if isinstance(value, str):
                filled = bool(value.strip())
            elif isinstance(value, dict):
                filled = bool(value)
            elif isinstance(value, (list, tuple)):
                filled = bool(value)
            elif isinstance(value, bool):
                filled = value
            else:
                filled = value is not None
            if not filled:
                continue
            passage_hit = bool(PASSAGE_LEG_RE.search(key))
            claim_hit = bool(CLAIM_LEG_RE.search(key))
            if passage_hit and not claim_hit:
                passage_paths.append(full)
            elif claim_hit and not passage_hit:
                claim_paths.append(full)
    return passage_paths, claim_paths


def receipt_raw_labels(receipt):
    """Raw worker labels preserved anywhere in the receipt (scalar or nested
    verdict/support-scope pair)."""
    labels = []
    for _path, node, _context in walk_dicts(receipt):
        for key, value in node.items():
            if not RAW_LABEL_KEY_RE.search(key):
                continue
            if isinstance(value, str) and value.strip():
                labels.append(norm(value))
            elif isinstance(value, dict):
                for sub in ("verdict", "label", "value", "support_scope", "scope"):
                    item = value.get(sub)
                    if isinstance(item, str) and item.strip():
                        labels.append(norm(item))
    return labels


def f_failures(declared_rows, bundle, reconciliation, reconciliation_present):
    failures = list(bundle["problems"])
    records = bundle["records"]
    for row_id in sorted(bundle["collisions"]):
        failures.append(f"{row_id}: duplicate receipt id bound to differing "
                        "payloads (identity collision)")
    missing = [row["id"] for row in declared_rows if row["id"] not in records]
    if missing:
        failures.append("missing receipts: " + ", ".join(missing))
    substantive = []
    shapes = {}
    separation = {}
    passage_keys = {}
    for row in declared_rows:
        row_id = row["id"]
        record = records.get(row_id)
        if record is None:
            continue
        passages = receipt_passages(record)
        failures_found = receipt_failures(record)
        substantive_passages = [item for item in passages
                                if item["tokens"] >= F_MIN_TOKENS]
        if passages:
            shapes[row_id] = "retrieved"
        elif failures_found:
            shapes[row_id] = "documented-failure"
        else:
            shapes[row_id] = "unshaped"
            failures.append(
                f"{row_id}: neither a retrieved-passage nor a documented "
                "access-failure receipt (no quoted passage with URL and named "
                "location, no attempted-command/status pair)")
        if substantive_passages:
            substantive.append(row_id)
        for item in substantive_passages:
            passage_keys.setdefault(item["key"], row_id)
        passage_paths, claim_paths = receipt_legs(record)
        separation[row_id] = bool(passage_paths and claim_paths)
        if not separation[row_id]:
            failures.append(
                f"{row_id}: passage support and whole-claim support are not "
                f"held in separate fields (passage fields={passage_paths[:3] or 'none'}, "
                f"claim fields={claim_paths[:3] or 'none'})")
    if len(substantive) < F_MIN_SUBSTANTIVE:
        failures.append(f"fewer than {F_MIN_SUBSTANTIVE} substantive retrieved "
                        f"passages: {len(substantive)}")
    reconciliation_failures, reconciliation_detail = f_reconciliation(
        declared_rows, records, reconciliation, reconciliation_present)
    failures.extend(reconciliation_failures)
    return failures, {"shapes": shapes, "separation": separation,
                      "substantive": substantive,
                      "distinct_substantive_passage_keys": len(passage_keys),
                      "reconciliation": reconciliation_detail}


def f_reconciliation(declared_rows, records, reconciliation,
                     reconciliation_present):
    failures = []
    detail = {"present": reconciliation_present}
    if not reconciliation_present:
        failures.append(f"missing reconciliation file: {RECONCILIATION_REL}")
        return failures, detail
    rows = [row for row in reconciliation_rows(reconciliation)
            if isinstance(row, dict)]
    declared_ids = [row["id"] for row in declared_rows]
    declared_by_id = {row["id"]: row for row in declared_rows}
    ledger_labels_by_prior = round6_ledger_labels(declared_rows)
    bound = []
    for row in rows:
        row_id = resolve_id(row, "", set(declared_ids),
                            {r.get("prior_row_id", "").upper(): r["id"]
                             for r in declared_rows if r.get("prior_row_id")})
        if row_id is None:
            failures.append("reconciliation row without a declared id: "
                            + canonical(row)[:120])
            continue
        bound.append(row_id)
        raw_key = first_key(row, RAW_FIELDS)
        reconciled_key = first_key(row, RECONCILED_FIELDS)
        if not raw_key or not reconciled_key or raw_key == reconciled_key:
            failures.append(
                f"{row_id}: reconciliation does not keep the raw worker label "
                f"apart from a distinct reconciled disposition "
                f"(raw field={raw_key or 'absent'}, reconciled field="
                f"{reconciled_key or 'absent'})")
            continue
        raw_value = norm(row.get(raw_key)) if not isinstance(row.get(raw_key), dict) \
            else " ".join(norm(item) for item in row[raw_key].values()
                          if isinstance(item, str))
        if not raw_value:
            failures.append(f"{row_id}: reconciliation raw worker label is empty")
        prior = declared_by_id.get(row_id, {}).get("prior_row_id", "").upper()
        ledger_labels = ledger_labels_by_prior.get(prior, {})
        if raw_value and ledger_labels.get("verdict"):
            needle = raw_value.casefold()
            verdict = ledger_labels["verdict"].casefold()
            if not (needle in verdict or verdict in needle):
                failures.append(
                    f"{row_id}: reconciliation raw label '{raw_value}' does not "
                    f"match the round-6 ledger verdict "
                    f"'{ledger_labels['verdict']}' ({ledger_labels['ledger']})")
        scope_value = ""
        for scope_field in ("raw_support_scope", "raw_scope", "support_scope"):
            candidate = row.get(scope_field)
            if isinstance(candidate, str) and candidate.strip():
                scope_value = norm(candidate)
                break
        if scope_value and ledger_labels.get("scope") \
                and scope_value.casefold() != ledger_labels["scope"].casefold():
            failures.append(
                f"{row_id}: reconciliation raw scope '{scope_value}' does not "
                f"match the round-6 ledger scope '{ledger_labels['scope']}'")
        receipt = records.get(row_id)
        if receipt is not None:
            receipt_labels = sorted(set(receipt_raw_labels(receipt)))
            if receipt_labels and raw_value:
                needle = raw_value.casefold()
                if not any(needle in label.casefold()
                           or label.casefold() in needle
                           for label in receipt_labels):
                    detail.setdefault("receipt_label_notes", {})[row_id] = (
                        f"receipt carries {receipt_labels}; the reconciliation "
                        f"preserves the round-6 worker label '{raw_value}' "
                        f"(the receipt's own prior-disposition is the round-6 "
                        f"audit disposition, not the worker label)")
        if not norm(row.get(reconciled_key)):
            failures.append(f"{row_id}: reconciled disposition is empty")
    duplicates = [row_id for row_id, count in
                  collections.Counter(bound).items() if count > 1]
    if duplicates:
        failures.append("reconciliation binds duplicate ids: "
                        + ", ".join(sorted(duplicates)))
    missing = [row_id for row_id in declared_ids if row_id not in set(bound)]
    if missing:
        failures.append("reconciliation misses declared ids: " + ", ".join(missing))
    extra = sorted(set(bound) - set(declared_ids))
    if extra:
        failures.append("reconciliation binds undeclared ids: " + ", ".join(extra))
    detail.update({"rows": len(rows), "bound": len(bound),
                   "missing": missing, "duplicates": sorted(duplicates),
                   "ledger_labels_checked": len(ledger_labels_by_prior)})
    return failures, detail


def reconciliation_rows(document):
    """The document's own row list (not a copy), so negative controls can
    mutate it in place."""
    for key in INVENTORY_KEYS:
        value = document.get(key)
        if isinstance(value, list):
            return value
    return []


def round6_ledger_labels(declared_rows):
    """prior_row_id -> the round-6 ledger's raw worker verdict and support
    scope, read from the ledger named by targets.json. Used to verify that the
    round-8 reconciliation preserves the raw labels apart from its reconciled
    dispositions."""
    labels = {}
    for row in declared_rows:
        ledger = row.get("prior_ledger")
        prior = str(row.get("prior_row_id", "")).strip().upper()
        if not ledger or not prior or not (ROOT / ledger).is_file():
            continue
        try:
            document = load_json(ledger)
        except json.JSONDecodeError:
            continue
        for audit in document.get("audits") or []:
            if not isinstance(audit, dict):
                continue
            if str(audit.get("id", "")).strip().upper() != prior:
                continue
            verdict = ""
            for field in ("verdict", "worker_verdict", "worker_label", "label",
                          "result"):
                value = audit.get(field)
                if isinstance(value, str) and value.strip():
                    verdict = norm(value)
                    break
            scope = ""
            for field in ("support_scope", "worker_scope_label", "scope"):
                value = audit.get(field)
                if isinstance(value, str) and value.strip():
                    scope = norm(value)
                    break
            labels[prior] = {"verdict": verdict, "scope": scope,
                             "ledger": ledger}
    return labels


def f_negative_controls(declared_rows, bundle, reconciliation):
    controls = []
    available = [row["id"] for row in declared_rows if row["id"] in bundle["records"]]

    def pick(index):
        return available[index % len(available)] if available else None

    def observe(name, expected, mutate, forbidden=None):
        if not available:
            controls.append({"control": name, "rejected": False,
                             "skipped": "no receipts landed yet"})
            return
        trial_bundle = copy.deepcopy(bundle)
        trial_reconciliation = copy.deepcopy(reconciliation)
        if mutate(trial_bundle, trial_reconciliation) is False:
            controls.append({"control": name, "rejected": False,
                             "skipped": "evidence this control needs has not "
                                        "landed yet"})
            return
        failures, _ = f_failures(declared_rows, trial_bundle,
                                 trial_reconciliation, True)
        joined = " | ".join(failures)
        if expected and expected not in joined:
            raise ValueError(f"control {name}: expected {expected!r}, got {joined!r}")
        if forbidden and forbidden in joined:
            raise ValueError(f"control {name}: forbidden {forbidden!r} present "
                             f"in {joined!r}")
        controls.append({"control": name, "rejected": True,
                         "diagnostic": expected or forbidden})

    def drop_receipt(trial, _recon):
        trial["records"].pop(pick(0), None)

    def collision(trial, _recon):
        row_id = pick(1)
        clone = copy.deepcopy(trial["records"][row_id])
        excerpt_key = first_key(clone, EXCERPT_FIELDS) or "source_excerpt"
        clone[excerpt_key] = "different payload for the same declared id"
        trial["records"][row_id] = clone
        trial["collisions"] = [row_id]

    def mirror_duplicate(trial, _recon):
        row_id = pick(2)
        trial["mirrors"][row_id] = trial["mirrors"].get(row_id, 0) + 1

    def drop_leg(record, which):
        targets = []
        for _path, node, _context in walk_dicts(record):
            for key in node:
                passage_hit = bool(PASSAGE_LEG_RE.search(key))
                claim_hit = bool(CLAIM_LEG_RE.search(key))
                if which == "passage" and passage_hit and not claim_hit:
                    targets.append((node, key))
                elif which == "claim" and claim_hit and not passage_hit:
                    targets.append((node, key))
        for node, key in targets:
            node.pop(key, None)
        return bool(targets)

    def strip_passage_leg(trial, _recon):
        if not drop_leg(trial["records"][pick(3)], "passage"):
            return False

    def strip_claim_leg(trial, _recon):
        if not drop_leg(trial["records"][pick(4)], "claim"):
            return False

    def thin_substantive(trial, _recon):
        changed = False
        for row in declared_rows:
            record = trial["records"].get(row["id"])
            if record is None:
                continue
            for _path, node, _context in walk_dicts(record):
                for field in NODE_EXCERPT_FIELDS:
                    if isinstance(node.get(field), str) and node[field].strip():
                        node[field] = "short"
                        changed = True
                for key, value in list(node.items()):
                    if isinstance(value, list) and re.search(r"quot|excerpt|passage",
                                                             key, re.I):
                        if any(isinstance(item, str) for item in value):
                            node[key] = ["short" for item in value
                                         if isinstance(item, str)]
                            changed = True
        if not changed:
            return False

    def drop_raw_label(_trial, trial_recon):
        rows = reconciliation_rows(trial_recon)
        if not rows:
            return False
        rows[0].pop(first_key(rows[0], RAW_FIELDS), None)

    def drop_recon_row(_trial, trial_recon):
        rows = reconciliation_rows(trial_recon)
        if not rows:
            return False
        rows.pop()

    observe("missing-receipt-rejected", "missing receipts", drop_receipt)
    observe("identity-collision-rejected", "identity collision", collision)
    observe("benign-mirror-deduplicated", "", mirror_duplicate,
            forbidden="identity collision")
    observe("passage-leg-separation-enforced", "separate fields", strip_passage_leg)
    observe("claim-leg-separation-enforced", "separate fields", strip_claim_leg)
    observe("substantive-floor-enforced", "substantive retrieved", thin_substantive)
    observe("reconciliation-raw-label-required", "raw worker label",
            drop_raw_label)
    observe("reconciliation-coverage-required", "misses declared ids",
            drop_recon_row)
    return controls


# --------------------------------------------------------------------------
# claim O — operability
# --------------------------------------------------------------------------

def measure_o_harness():
    result = {"path": HARNESS_REL}
    pointer = None
    if (ROOT / HARNESS_FIX_REL).is_file():
        fix = load_json(HARNESS_FIX_REL)
        for field in ("harness_path", "harness", "tool", "artifact", "path"):
            value = fix.get(field)
            if isinstance(value, str) and (ROOT / value).is_file():
                pointer = value
                break
    harness_rel = pointer or HARNESS_REL
    result["path"] = harness_rel
    result["pointer"] = pointer
    if not (ROOT / harness_rel).is_file():
        result["failure"] = f"missing harness fix: {harness_rel}"
        return result, [result["failure"]]
    result["sha256"] = file_sha(harness_rel)
    run = run_cli(harness_rel, ["--selftest"])
    result.update({"exit": run["exit"], "stdout_sha256": run["stdout_sha256"],
                   "stderr_tail": sanitize(run["stderr"], 200)})
    failures = []
    if run["exit"] != 0:
        failures.append(f"harness fix selftest exit {run['exit']} (expected 0): "
                        + sanitize(run["stdout"], 200))
        return result, failures
    receipt = None
    try:
        receipt = json.loads(run["stdout"])
    except json.JSONDecodeError:
        pass
    if receipt is None:
        failures.append("harness fix selftest emitted no JSON receipt")
        return result, failures
    controls = receipt.get("controls") or []
    result["controls_passed"] = receipt.get("controls_passed")
    result["controls_total"] = receipt.get("controls_total")
    result["selftest_passed"] = receipt.get("selftest_passed")
    if not receipt.get("selftest_passed") or not controls:
        failures.append("harness fix selftest did not report all controls passing")
    duplicate_ok = any(
        "duplicate" in str(control.get("control", "")).casefold()
        and control.get("passed") is True
        and "accepted" in str(control.get("observed", "")).casefold()
        for control in controls)
    collision_ok = any(
        "collision" in str(control.get("control", "")).casefold()
        and control.get("passed") is True
        and "identity collision" in str(control.get("observed", "")).casefold()
        for control in controls)
    result["benign_duplicate_accepted_demonstrated"] = duplicate_ok
    result["genuine_collision_rejected_demonstrated"] = collision_ok
    if not duplicate_ok:
        failures.append("harness fix selftest lacks an accepted benign-duplicate "
                        "control with an 'accepted' observation")
    if not collision_ok:
        failures.append("harness fix selftest lacks a rejected genuine-collision "
                        "control with an 'identity collision' observation")
    if (ROOT / ROUND7_DIR_REL).is_dir():
        diff = subprocess.run(["git", "status", "--porcelain", "--",
                               ROUND7_DIR_REL.rstrip("/")],
                              cwd=str(ROOT), capture_output=True, timeout=60)
        dirty = [line for line in diff.stdout.decode().splitlines() if line.strip()]
        result["round7_touched"] = dirty
        if dirty:
            failures.append("round-7 filed artifacts were edited: "
                            + "; ".join(dirty[:5]))
    return result, failures


QUARANTINE_RE = re.compile(r"quarantin|defer|declin|wontfix|limit|accepted"
                           r"|boundary|not[_ ]defect|out[-_ ]of[-_ ]scope", re.I)


def review_defect_ids():
    """Required scope per the O claim: review-26 parser defects (excluding the
    heading that says "not a defect") plus review-29 findings whose headings
    name a selftest or regex surface; every other finding is optional coverage."""
    required, optional = [], []
    text26 = (ROOT / REVIEW_26_REL).read_text(encoding="utf-8")
    for defect_id, rest in re.findall(r"^###\s+(D\d+)\b(.*)$", text26, re.M):
        if "not a defect" in rest.casefold():
            optional.append(defect_id)
        else:
            required.append(defect_id)
    text29 = (ROOT / REVIEW_29_REL).read_text(encoding="utf-8")
    for defect_id, rest in re.findall(r"^##\s+(F\d+)\s*[-\u2014]\s*(.*)$",
                                      text29, re.M):
        heading = rest.casefold()
        if "selftest" in heading or "regex" in heading:
            required.append(defect_id)
        else:
            optional.append(defect_id)
    return required, optional


def inventory_rows(document):
    if isinstance(document, list):
        return [row for row in document if isinstance(row, dict)]
    for key in INVENTORY_KEYS:
        value = document.get(key)
        if isinstance(value, list):
            return [row for row in value if isinstance(row, dict)]
    return []


def row_status(row):
    for field, value in row.items():
        if re.search(r"status|disposition|decision|verdict", field, re.I) \
                and isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def row_documentation(row):
    parts = []
    for field in ("defect", "evidence_pointer", "suggested_control", "reason",
                  "quarantine_reason", "rationale", "justification", "notes"):
        value = row.get(field)
        if isinstance(value, str) and value.strip():
            parts.append(value.strip())
        elif isinstance(value, dict):
            parts.append(" ".join(str(item) for item in value.values()))
    return " ".join(parts)


def row_defect_ids(row):
    ids = []
    for field in ("id", "defect_id", "defect", "key", "review_id",
                  "source_section"):
        value = row.get(field)
        if isinstance(value, str) and value.strip():
            ids.append(value.strip())
    covers = row.get("covers")
    if isinstance(covers, list):
        ids.extend(str(item).strip() for item in covers)
    return ids


def mentions(text, defect_id):
    return bool(re.search(rf"(?<![A-Za-z0-9]){re.escape(defect_id)}(?![0-9])",
                          text))


def measure_o_defects():
    result = {"inventory": DEFECT_INVENTORY_REL}
    failures = []
    required, optional = review_defect_ids()
    result["required_review_ids"] = required
    result["optional_review_ids"] = optional
    if not (ROOT / DEFECT_INVENTORY_REL).is_file():
        failures.append(f"missing defect inventory: {DEFECT_INVENTORY_REL}")
        result["failure"] = failures[-1]
        return result, failures
    rows = inventory_rows(load_json(DEFECT_INVENTORY_REL))
    result["rows"] = len(rows)
    if not rows:
        failures.append("defect inventory carries no defect rows")
        return result, failures
    coverage = collections.defaultdict(list)
    for row in rows:
        status = row_status(row)
        documented = bool(row_documentation(row))
        for defect_id in required:
            if any(mentions(item, defect_id) for item in row_defect_ids(row)):
                coverage[defect_id].append({"status": status,
                                            "documented": documented})
    result["statuses"] = {defect_id: sorted({entry["status"]
                                             for entry in entries})
                          for defect_id, entries in sorted(coverage.items())}
    controls, control_failures, control_detail, repaired = \
        measure_neg_controls(required)
    result["neg_controls"] = control_detail
    result["controls"] = controls
    result["repaired"] = sorted(repaired)
    quarantined, unrepaired = [], []
    for defect_id in required:
        if defect_id in repaired:
            continue
        entries = coverage.get(defect_id, [])
        if any(QUARANTINE_RE.search(entry["status"]) and entry["documented"]
               for entry in entries):
            quarantined.append(defect_id)
        else:
            unrepaired.append(defect_id)
    result["quarantined"] = quarantined
    result["unrepaired"] = unrepaired
    uncovered = [defect_id for defect_id in required if defect_id not in coverage]
    result["uncovered_required"] = uncovered
    result["uncovered_optional"] = [defect_id for defect_id in optional
                                    if defect_id not in coverage]
    if uncovered:
        failures.append("defect inventory does not cover required review ids: "
                        + ", ".join(uncovered))
    if unrepaired:
        failures.append("required review defects neither repaired with a passing "
                        "control nor quarantined with a documented reason: "
                        + ", ".join(unrepaired))
    if not repaired:
        failures.append("no legacy defect is actually repaired (an all-quarantine "
                        "inventory leaves the O before-state unchanged)")
    failures.extend(control_failures)
    return result, failures


def measure_neg_controls(required_ids):
    """Run every negative-control script on the live tree and map each required
    defect id to the controls that reference it. A defect counts as repaired
    only when every control that references it exits 0; a control that reports
    the pre-fix pattern leaves its defect unrepaired."""
    failures = []
    repaired = set()
    detail = {"dir": str(NEG_CONTROLS_DIR.relative_to(ROOT)), "artifacts": []}
    if not NEG_CONTROLS_DIR.is_dir():
        failures.append(f"missing negative-control directory: {detail['dir']}")
        return [], failures, detail, repaired
    artifacts = [path for path in sorted(NEG_CONTROLS_DIR.rglob("*"))
                 if path.is_file() and path.suffix in (".py", ".json", ".md", ".txt")]
    if not artifacts:
        failures.append("no negative-control artifacts under " + detail["dir"])
        return [], failures, detail, repaired
    for path in artifacts:
        relative = str(path.relative_to(ROOT))
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as error:
            failures.append(f"{relative}: unreadable ({error})")
            continue
        ids = sorted({token for token in
                      re.findall(r"(?<![A-Za-z0-9])(?:D\d+|F\d+)(?![0-9])", text)
                      if token in required_ids})
        entry = {"path": relative, "ids": ids,
                 "leg_markers": {name: bool(pattern.search(text))
                                 for name, pattern in SEPARATION_LEG_MARKERS.items()},
                 "sha256": sha(text.encode())}
        if path.suffix == ".py":
            run = run_cli(relative)
            entry.update({"exit": run["exit"],
                          "stdout_sha256": sha(sanitize(run["stdout"], 1000000).encode()),
                          "stderr_sha256": run["stderr_sha256"],
                          "traceback": "Traceback" in run["stderr"],
                          "stdout_tail": sanitize(run["stdout"], 200)})
            if entry["traceback"]:
                failures.append(f"{relative}: control printed a traceback on "
                                "stderr")
        detail["artifacts"].append(entry)
    for defect_id in required_ids:
        refs = [entry for entry in detail["artifacts"] if defect_id in entry["ids"]]
        if not refs:
            continue
        if all(entry.get("exit", 0) == 0 for entry in refs):
            repaired.add(defect_id)
            if not any(all(entry["leg_markers"].values()) for entry in refs):
                failures.append(f"repaired defect {defect_id} has no control "
                                "artifact declaring both a pre-fix and a "
                                "post-fix leg")
    detail["repaired_ids"] = sorted(repaired)
    detail["unreferenced_required"] = sorted(
        set(required_ids) - {defect_id for entry in detail["artifacts"]
                             for defect_id in entry["ids"]})
    return detail["artifacts"], failures, detail, repaired


def measure_o_battery():
    result = {"receipt": BATTERY_RERUN_REL}
    failures = []
    if not (ROOT / BATTERY_RERUN_REL).is_file():
        failures.append(f"missing battery rerun receipt: {BATTERY_RERUN_REL}")
        result["failure"] = failures[-1]
        return result, failures
    receipt = load_json(BATTERY_RERUN_REL)
    summary = receipt.get("summary_by_command") or {}
    recorded_tools = {entry.get("path"): entry for entry in
                      (receipt.get("revision_binding", {})
                       .get("tools_under_test") or []) if isinstance(entry, dict)}
    result["recorded"] = {}
    for relative, recorded_key in ((BATTERY_REL, "check-gate-battery"),
                                   (CRAFT_REL, "check-craft-exercise")):
        entry = summary.get(recorded_key) or {}
        exits = entry.get("exit_codes") or []
        if not exits or any(code != 0 for code in exits):
            failures.append(f"{recorded_key}: recorded exit codes {exits} are "
                            "not all zero")
        if not entry.get("stdout_sha256"):
            failures.append(f"{recorded_key}: recorded stdout hash missing")
        live = run_cli(relative, ["--selftest"])
        current_sha = file_sha(relative)
        recorded_sha = (recorded_tools.get(relative) or {}).get("sha256_worktree")
        state = {"recorded_stdout_sha256": entry.get("stdout_sha256"),
                 "live_stdout_sha256": live["stdout_sha256"],
                 "live_exit": live["exit"],
                 "tool_sha256_now": current_sha,
                 "tool_sha256_at_receipt": recorded_sha,
                 "stdout_tail": sanitize(live["stdout"], 160)}
        if live["exit"] != 0:
            failures.append(f"{recorded_key}: live selftest exit {live['exit']} "
                            "(expected 0)")
            state["verdict"] = "live-run-failed"
        elif entry.get("stdout_sha256") == live["stdout_sha256"]:
            state["verdict"] = "stdout-hash-reproduced"
        elif recorded_sha and current_sha and recorded_sha != current_sha:
            state["verdict"] = "tool-repaired-after-receipt"
        else:
            state["verdict"] = "unexplained-stdout-drift"
            failures.append(f"{recorded_key}: stdout hash drifted while the tool "
                            "bytes are unchanged (unexplained)")
        result["recorded"][recorded_key] = state
    return result, failures


def measure_o():
    harness, harness_failures = measure_o_harness()
    defects, defect_failures = measure_o_defects()
    battery, battery_failures = measure_o_battery()
    failures = harness_failures + defect_failures + battery_failures
    return {"passed": not failures,
            "measurement": {"harness_fix": harness, "defect_repairs": defects,
                            "battery_rerun": battery},
            "failures": failures}


# --------------------------------------------------------------------------
# claim D — depth capability
# --------------------------------------------------------------------------

def measure_d_selftest():
    result = {"path": D2_TOOL_REL}
    failures = []
    if not (ROOT / D2_TOOL_REL).is_file():
        failures.append(f"missing capability tool: {D2_TOOL_REL}")
        result["failure"] = failures[-1]
        return result, failures
    result["sha256"] = file_sha(D2_TOOL_REL)
    run = run_cli(D2_TOOL_REL, ["--selftest"])
    result.update({"exit": run["exit"], "stdout_sha256": run["stdout_sha256"],
                   "stdout_tail": sanitize(run["stdout"], 240)})
    if run["exit"] != 0:
        failures.append(f"{D2_TOOL_REL} --selftest exit {run['exit']} (expected 0)")
    combined = run["stdout"] + run["stderr"]
    if "Traceback" in combined:
        failures.append(f"{D2_TOOL_REL} --selftest printed a traceback")
    result["malformed_mentioned"] = bool(re.search(r"malformed", run["stdout"], re.I))
    counts = []
    for line in run["stdout"].splitlines():
        if re.search(r"selftest", line, re.I):
            counts.extend(re.findall(r"(\d+)\s*/\s*(\d+)", line))
    result["selftest_counts"] = counts
    if not result["malformed_mentioned"]:
        failures.append(f"{D2_TOOL_REL} --selftest does not report malformed-input "
                        "controls")
    if not counts:
        failures.append(f"{D2_TOOL_REL} --selftest reports no self-test counts")
    if counts and any(int(passed) != int(total) for passed, total in counts):
        failures.append(f"{D2_TOOL_REL} --selftest reports failing controls: {counts}")
    return result, failures


def discover_manifest():
    patterns = ("reports/round-8/**/MANIFEST*.tsv",
                "reports/round-8/**/*manifest*.tsv",
                "tools/gates/frozen/round-8/**/MANIFEST.tsv",
                "examples/culture-d2/**/MANIFEST*.tsv")
    found = []
    for pattern in patterns:
        for path in sorted(ROOT.glob(pattern)):
            if path.is_file():
                found.append(path)
    for path in sorted(ROOT.glob("reports/round-8/**/*.tsv")):
        if not path.is_file() or path in found:
            continue
        try:
            header = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        first = header.splitlines()[:1]
        if first and "sha256" in first[0]:
            found.append(path)
    unique = sorted(set(found))
    ranked = sorted(unique, key=lambda path: (
        0 if "d2" in str(path.relative_to(ROOT)).casefold() else 1,
        str(path.relative_to(ROOT))))
    return ranked


def replay_isolated():
    """Reproduce the D2 packet's frozen replay in a disposable tree holding the
    pinned gate revisions (git HEAD). The live tree cannot replay the round-3
    pins because the O shards legitimately repaired six gate files and the pins
    refuse edited bytes by design; the isolated tree isolates "the pins, the
    snapshots and the records are self-consistent" from "the worktree has
    drifted". Nothing is written inside the repository and the scratch path is
    never recorded."""
    result = {"manifest": "tools/gates/frozen/round-3/MANIFEST.tsv"}
    manifest = ROOT / result["manifest"]
    if not manifest.is_file():
        result["failure"] = "missing frozen manifest: " + result["manifest"]
        return result
    scratch = Path(tempfile.mkdtemp(prefix="r8-replay-"))
    try:
        iso = scratch / "iso"
        (iso / "tools/gates").mkdir(parents=True)
        shutil.copy2(ROOT / REPLAY_REL, iso / REPLAY_REL)
        restored = 0
        for gate in sorted((ROOT / "tools/gates").glob("*.py")):
            relative = f"tools/gates/{gate.name}"
            blob = subprocess.run(["git", "show", f"HEAD:{relative}"],
                                  cwd=str(ROOT), capture_output=True,
                                  timeout=60)
            if blob.returncode == 0:
                (iso / relative).write_bytes(blob.stdout)
                restored += 1
            else:
                shutil.copy2(gate, iso / relative)
        shutil.copytree(ROOT / "tools/gates/frozen", iso / "tools/gates/frozen",
                        dirs_exist_ok=True)
        run = subprocess.run(
            [sys.executable, str(iso / REPLAY_REL), result["manifest"],
             "--repo-root", str(iso), "--json"],
            cwd=str(iso), capture_output=True, timeout=300)
        result["exit"] = run.returncode
        result["gates_restored_from_head"] = restored
        try:
            result["summary"] = json.loads(run.stdout.decode()).get("summary")
        except json.JSONDecodeError:
            result["stdout_tail"] = sanitize(run.stdout.decode(), 200)
        result["stderr_tail"] = sanitize(run.stderr.decode(), 200)
    except (OSError, subprocess.SubprocessError) as error:
        result["failure"] = sanitize(str(error), 200)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    return result


def measure_d_replay():
    result = {}
    failures = []
    candidates = discover_manifest()
    result["round8_manifest_candidates"] = [str(path.relative_to(ROOT))
                                            for path in candidates]
    reference = run_cli(REPLAY_REL, ["tools/gates/frozen/round-3/MANIFEST.tsv",
                                     "--json"])
    result["live_reference"] = {"manifest": "tools/gates/frozen/round-3/MANIFEST.tsv",
                                "exit": reference["exit"]}
    try:
        result["live_reference"]["summary"] = json.loads(
            reference["stdout"]).get("summary")
    except json.JSONDecodeError:
        pass
    accepted = None
    if candidates:
        chosen = candidates[0]
        relative = str(chosen.relative_to(ROOT))
        run = run_cli(REPLAY_REL, [relative, "--json"])
        result["live"] = {"manifest": relative, "exit": run["exit"],
                          "stdout_sha256": run["stdout_sha256"]}
        try:
            summary = json.loads(run["stdout"]).get("summary") or {}
            result["live"]["summary"] = summary
            if run["exit"] == 0 and not summary.get("mismatch") \
                    and not summary.get("could_not_evaluate"):
                accepted = "live-manifest"
        except json.JSONDecodeError:
            failures.append("replay-frozen emitted no JSON document for " + relative)
    if accepted is None:
        isolated = replay_isolated()
        result["isolated"] = isolated
        summary = isolated.get("summary") or {}
        if isolated.get("exit") == 0 and summary.get("rows") \
                and summary.get("reproduced") == summary.get("rows") \
                and not summary.get("mismatch") \
                and not summary.get("could_not_evaluate"):
            accepted = "isolated-pinned-revisions"
        else:
            failures.append("no D2 frozen replay without digest drift: no "
                            "round-8 manifest reproduced in the live tree and "
                            "the isolated pinned-revision replay did not "
                            "reproduce every row "
                            f"({json.dumps(summary) if summary else isolated.get('failure')})")
    result["accepted"] = accepted
    return result, failures


def measure_d_docs():
    result = {}
    failures = []
    skill = (ROOT / SKILL_REL).read_text(encoding="utf-8")
    match = re.search(r"label[-_ ]typing|typed[-_ ]label|translated[-_ ]label",
                      skill, re.I)
    if not match:
        failures.append(f"{SKILL_REL} carries no label-typing decision table")
        result["skill_table"] = False
    else:
        line_index = skill[:match.start()].count("\n")
        window = skill.splitlines()[line_index:line_index + 120]
        table_lines = sum(1 for line in window if line.strip().startswith("|"))
        result["skill_table"] = True
        result["skill_table_lines"] = table_lines
        result["skill_match"] = sanitize(skill[match.start():match.start() + 80], 80)
        if table_lines < 3:
            failures.append(f"{SKILL_REL} mentions label typing but carries no "
                            "table rows near the mention")
    scorecard = (ROOT / SCORECARD_REL).read_text(encoding="utf-8")
    row = re.search(r"d2[-_ ]typed[-_ ]labels", scorecard, re.I)
    result["scorecard_row"] = bool(row)
    if not row:
        failures.append(f"{SCORECARD_REL} carries no d2-typed-labels capability row")
    return result, failures


def reader_pin_diagnostic():
    """The D2 packet embeds the sha256 of the costume gate it uses as its YAML
    reader. When the reader is repaired after the packet was generated, the
    deterministic assembly differs by exactly that pinned line: a regeneration
    task for the packet's owner, not a code defect."""
    packet = ROOT / "examples/culture-d2/packet.d2.yml"
    reader_rel = "tools/gates/costume-era-consistency-gate.py"
    if not packet.is_file() or not (ROOT / reader_rel).is_file():
        return None
    match = re.search(r'reader_sha256:\s*"([0-9a-f]{64})"',
                      packet.read_text(encoding="utf-8"))
    if not match:
        return None
    current = file_sha(reader_rel)
    return {"packet_reader_sha256": match.group(1),
            "live_reader_sha256": current,
            "reader": reader_rel,
            "drifted": match.group(1) != current}


def measure_d():
    selftest, selftest_failures = measure_d_selftest()
    regenerate = {}
    regen_failures = []
    if (ROOT / D2_ASSEMBLER_REL).is_file():
        run = run_cli(D2_ASSEMBLER_REL, ["--check"])
        regenerate = {"exit": run["exit"], "stdout_sha256": run["stdout_sha256"],
                      "stdout_tail": sanitize(run["stdout"], 160),
                      "reader_pin": reader_pin_diagnostic()}
        if run["exit"] != 0:
            note = ""
            pin = regenerate["reader_pin"]
            if pin and pin["drifted"]:
                note = (" — the packet's reader_sha256 pin "
                        f"{pin['packet_reader_sha256'][:12]}... no longer matches "
                        f"the live {pin['reader']} "
                        f"{pin['live_reader_sha256'][:12]}..., so the assembly "
                        "differs by that pinned line alone; the packet needs "
                        "regeneration (owner action)")
            regen_failures.append(f"{D2_ASSEMBLER_REL} --check exit {run['exit']} "
                                  "(expected 0: deterministic regeneration)" + note)
    else:
        regen_failures.append(f"missing assembler: {D2_ASSEMBLER_REL}")
    replay, replay_failures = measure_d_replay()
    docs, docs_failures = measure_d_docs()
    if docs.get("scorecard_row") and selftest.get("exit") != 0:
        docs_failures.append("SCORECARD carries the d2-typed-labels row although "
                             "the tool selftest did not pass (row must enter only "
                             "on a demonstrated run)")
    fragments = []
    if DEPTH_DIR.is_dir():
        for path in sorted(DEPTH_DIR.rglob("*.json")):
            fragments.append(str(path.relative_to(ROOT)))
    failures = selftest_failures + regen_failures + replay_failures + docs_failures
    return {"passed": not failures,
            "measurement": {"selftest": selftest, "regeneration": regenerate,
                            "replay_frozen": replay, "docs": docs,
                            "depth_evidence_files": fragments},
            "failures": failures}


# --------------------------------------------------------------------------
# runner
# --------------------------------------------------------------------------

def main():
    claims = load_json(CLAIMS_REL)
    declared_rows = declared_freshness()
    reconciliation_present = (ROOT / RECONCILIATION_REL).is_file()
    reconciliation = load_json(RECONCILIATION_REL) if reconciliation_present else {}
    bundle = load_freshness(declared_rows)

    f_failure_list, f_detail = f_failures(declared_rows, bundle, reconciliation,
                                          reconciliation_present)
    try:
        f_controls = f_negative_controls(declared_rows, bundle, reconciliation)
        control_error = None
    except ValueError as error:
        f_controls = []
        control_error = str(error)
        f_failure_list.append("F negative controls: " + control_error)

    o_result = measure_o()
    d_result = measure_d()

    claims_result = {
        "F": {"passed": not f_failure_list,
              "measurement": {
                  "declared_ids": [row["id"] for row in declared_rows],
                  "receipts_present": sorted(bundle["records"]),
                  "receipt_sources": bundle["sources"],
                  "mirrored_duplicates": bundle["mirrors"],
                  "substantive_passages": f_detail["substantive"],
                  "distinct_substantive_passage_keys":
                      f_detail.get("distinct_substantive_passage_keys"),
                  "shapes": f_detail["shapes"],
                  "separation": f_detail["separation"],
                  "reconciliation": f_detail["reconciliation"],
                  "negative_controls": f_controls,
                  "control_error": control_error},
              "failures": f_failure_list},
        "O": o_result,
        "D": d_result,
    }
    passed = all(claims_result[key]["passed"] for key in ("F", "O", "D"))
    missing_dependencies = []
    if not (ROOT / RECONCILIATION_REL).is_file():
        missing_dependencies.append(RECONCILIATION_REL)
    if not bundle["records"]:
        missing_dependencies.append(str(FRESHNESS_DIR.relative_to(ROOT)) + "/")
    if not (ROOT / DEFECT_INVENTORY_REL).is_file():
        missing_dependencies.append(DEFECT_INVENTORY_REL)
    if not (ROOT / D2_TOOL_REL).is_file():
        missing_dependencies.append(D2_TOOL_REL)

    receipt = {
        "round": 8,
        "runner": str(Path(__file__).relative_to(ROOT)),
        "runner_sha256": file_sha(str(Path(__file__).relative_to(ROOT))),
        "counting_command": "python3 reports/round-8/run-validation.py",
        "claims_declared": {claim["id"]: claim["axis"] for claim in claims["claims"]},
        "baseline_revision": claims.get("baseline_revision"),
        "acceptance_checks_passed": passed,
        "claims": claims_result,
        "failures": [f"claim {key}: {failure}"
                     for key in ("F", "O", "D")
                     for failure in claims_result[key]["failures"]],
        "missing_dependencies": sorted(missing_dependencies),
        "input_sha256": {
            relative: file_sha(relative) for relative in sorted({
                CLAIMS_REL, TARGETS_REL, RECONCILIATION_REL, BATTERY_RERUN_REL,
                DEFECT_INVENTORY_REL, HARNESS_FIX_REL, HARNESS_REL, D2_TOOL_REL,
                D2_ASSEMBLER_REL, REPLAY_REL, BATTERY_REL, CRAFT_REL, SKILL_REL,
                SCORECARD_REL, REVIEW_26_REL, REVIEW_29_REL}
                | set(bundle["sources"].values()))
            if file_sha(relative) is not None},
        "limits": [
            "Receipt/schema/count/execution checks, not automated quotation "
            "truth, historical authenticity or cultural permission.",
            "F separation and reconciliation checks are structural: they verify "
            "that the evidence keeps passage support, whole-claim support and "
            "raw worker labels in distinct fields; they do not adjudicate the "
            "labels' correctness.",
            "Negative-control scripts are executed read-only with a 120s "
            "timeout; their recorded stdout digest is taken after normalizing "
            "temporary paths and timestamps, so the receipt is reproducible "
            "across runs, and a control that wrote to the repository would be "
            "visible in git status but is not otherwise sandboxed.",
            "The replay leg accepts only a manifest with zero mismatch and zero "
            "could-not-evaluate rows; historical manifests (round-3/round-4) "
            "are not accepted as D evidence.",
            "All reviews are author-side; this runner decides no admission, "
            "promotion or closure, and never certifies canon.",
        ],
    }
    output = ROOT / OUTPUT_REL
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                 ensure_ascii=False) + "\n", encoding="utf-8")
    for claim_id in ("F", "O", "D"):
        state = "PASS" if claims_result[claim_id]["passed"] else "FAIL"
        print(f"claim {claim_id}: {state}")
        for failure in claims_result[claim_id]["failures"]:
            print(f"  - {failure}")
    print(f"acceptance_checks_passed: {passed}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
