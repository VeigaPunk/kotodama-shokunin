#!/usr/bin/env python3
"""Round-9 local acceptance runner (shard R9-O16): measures claims F, O and D
against reports/round-9/claims.json and reports/round-9/targets.json.

Run:  python3 reports/round-9/run-validation.py

Writes ONLY reports/round-9/validation.json in this repository (no scratch, no
network). The receipt is deterministic: sorted keys, no wall-clock timestamps,
no temporary paths, sha256 digests of every consumed input; child output is
recorded after normalizing temporary paths, timestamps and durations. Missing
worker evidence is recorded as a failing dependency with the exact missing
paths -- never synthesized, and expectations are never weakened to fit a
defect.

Claim F (freshness, declared thresholds): the four residuals R9-R8-F01..F04
(targets.json freshness) must each carry at least two escalated-strategy
retrieval receipts under reports/round-9/freshness/, counted per residual as
distinct documents (a .md companion of a same-stem .json counts once, and an
aggregated receipt that carries its own retrieval/hunter units counts those
units); every residual's combined receipt text must name an escalation role
(hunter, verifier, primary-source/museum, scholarly-fulltext, alternate-angle);
each residual's receipts must carry a retrieved passage (URL + named location +
excerpt) or a documented access failure (attempt + status), where a passage may
inherit its URL and kind from a source the receipt cites by key or from its
container key; at least two of the four must move to partial-support-or-better
on a primary or scholarly passage. The row verdict is read claim-level and by
tier (reconciled/verifier verdict, then whole-claim, then a top-level
verdict-like field, then shard-contribution phrasing, then scope) with raw,
prior and round-8 fields excluded and per-element (passage/retrieval/leg/
witness/quote) verdicts excluded; a label is classified on its verdict head so
a long qualification tail cannot flip it, and labels that disagree within the
same tier are read fail-closed (below-partial, recorded as a note). A
primary/scholarly passage is one whose declared kind, cited source kind or text
classifies as a primary object record or a scholarly full text. Every residual
that stays below partial-support must carry deeper-limit evidence naming what
remains unreadable or unretrievable (a limit-named field or an explicit
unreadable/unretrievable statement, >= 8 tokens total). The raw worker labels
must be preserved apart from reconciled dispositions: reports/round-9/
freshness/reconciliation.json when present (bound to exactly the four ids, raw
field distinct from the reconciled field, the raw value consistent with the
round-8 reconciliation's own raw label, raw scope or reconciled disposition for
that row), otherwise raw labels kept apart from a disposition reading inside
the residuals' own receipts. A raw label matching none of the row's preserved
round-8 labels is a failure in the reconciliation-file path; in the
receipt-pair path a raw field that carries the round-8 reconciled disposition
rather than the round-6 worker label is recorded as a note, because both are
preserved labels of the same row.

Claim O (operability, declared thresholds): after establishing the actual
count, all seven structural gates (tools/gates/*.py) must carry a committed
expected.json baseline laid out to the lane's frozen-run standard
(corpus/knowledge/verification/gate-frozen-run-standard.md section 4), wherever
that baseline lives (tools/gates/frozen/<gate>/, tools/gates/expected/<gate>/,
reports/round-9/baselines/<gate>/): schema, gate binding, gate_sha256,
revision, frozen_at/frozen_by, a non-empty `inputs` map of path -> sha256
digests, and `expected` {exit 0|1, class clean|findings, findings list}. Every
pinned digest must resolve -- baseline-local snapshot first, repository path
second -- and match the bytes on disk; an unresolvable or mismatched pin is a
failure (snapshot_tampered / snapshot missing), and each baseline must hold at
least one baseline-local snapshot copy rather than re-inheriting a live path.
A gate_sha256 that differs from the live gate bytes is `gate_revised` and
fails closed. The battery runner (tools/check-gate-battery.py) must carry the
baseline-validation extension (its source names expected.json), its --selftest
must stay green AND demonstrate baseline tamper/drift handling, and it must pin
every baseline of the round's delivered layout: the runner re-runs it naming
the roots the baselines actually landed in (tools/gates/expected/,
tools/gates/frozen/, reports/round-9/baselines/), which must exit 0 with every
baseline pinned, all seven gates covered and no finding. The battery's own
committed default roots (tools/gates/expected, tools/gates/frozen) are also run
and their coverage recorded: when they do not cover every baseline the gap is
reported with the uncovered gates and the existing valid baseline paths, and it
is not a failure, because audit-18 section 6.1 leaves the root-list
reconciliation (add the third root, or relocate the two baselines) to the
orchestrator. A baseline-validation CLI mode is run when the tool advertises a
boolean one, and value-taking modes are recorded rather than run with a guessed
argument. No gate behaviour may change: the seven gate files must be
byte-identical to HEAD, or a modified gate must carry a documented reason in a
reports/round-9 fragment (untracked baseline additions are new evidence, not
behaviour change). The runner's own digest reader is exercised against
synthetic baselines (good / tampered / missing / unpinned / gate-revised) so
the check is shown to be load-bearing.

Claim D (depth, declared thresholds): tools/assemble-culture-d3.py --check must
exit 0 twice with identical output (byte-identical deterministic assembly);
tools/check-evidence-coupling.py --selftest must be green (its own
selftest_passed true); the D3 frozen expectation must replay without digest
drift (check-evidence-coupling.py examples/culture-d3/packet.json --frozen
examples/culture-d3/expected.json exits 0); and a discovered round-9 D3 replay
manifest, when one is delivered, must replay through tools/replay-frozen.py
with zero mismatch and zero could-not-evaluate rows. Round-9 d3 fragments are
recorded as evidence inventory, not as a threshold.

Acceptance reading (declared, not weakened): missing worker evidence fails the
claim it belongs to and is listed in missing_dependencies; this runner decides
no admission, promotion or closure.

Stdlib only; read-only over repository inputs; the only write is
reports/round-9/validation.json.
"""

import collections
import copy
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "reports/round-9"
CLAIMS_REL = "reports/round-9/claims.json"
TARGETS_REL = "reports/round-9/targets.json"
FRESHNESS_DIR = HERE / "freshness"
RECONCILIATION_REL = "reports/round-9/freshness/reconciliation.json"
R8_RECONCILIATION_REL = "reports/round-8/freshness/reconciliation.json"
BASELINE_ROOTS = ("tools/gates/frozen", "tools/gates/expected",
                  "reports/round-9/baselines")
GATES_DIR_REL = "tools/gates"
BATTERY_REL = "tools/check-gate-battery.py"
D3_ASSEMBLER_REL = "tools/assemble-culture-d3.py"
COUPLING_REL = "tools/check-evidence-coupling.py"
REPLAY_REL = "tools/replay-frozen.py"
D3_PACKET_REL = "examples/culture-d3/packet.json"
D3_EXPECTED_REL = "examples/culture-d3/expected.json"
D3_DIR_REL = "reports/round-9/d3"
OUTPUT_REL = "reports/round-9/validation.json"
FROZEN_STANDARD_REL = ("corpus/knowledge/verification/"
                       "gate-frozen-run-standard.md")

F_MIN_RECEIPTS = 2
F_MIN_MOVED = 2
F_MIN_LIMIT_TOKENS = 8
CONTROL_TIMEOUT = 180
BATTERY_TIMEOUT = 600

ID_FIELDS = ("id", "row_id", "question_id", "receipt_id", "target_id",
             "declared_id", "residual_id")
RAW_FIELDS = ("raw_label", "worker_label", "raw_verdict", "worker_verdict",
              "raw_result", "original_label", "raw_disposition")
RECONCILED_FIELDS = ("reconciled_disposition", "reconciled", "parent_disposition",
                     "reconciled_label", "parent_reconciled", "reconciled_result")
EXCERPT_FIELDS = ("source_excerpt", "excerpt", "quoted_passage", "passage_text",
                  "passage", "quote", "quote_text", "text")
LOCATOR_FIELDS = ("source_locator", "locator", "location", "passage_location",
                  "source_location", "section", "page", "pages", "line", "lines",
                  "range", "quote_pages", "page_range", "pages_range", "span",
                  "quote_span", "pdf_pages", "printed_pages")
URL_FIELDS = ("source_url", "url", "href", "link", "human_url")
ACCESSED_FIELDS = ("accessed_at", "accessed", "access_date", "checked_at",
                   "retrieved_at", "timestamp")
ATTEMPT_FIELDS = ("attempted_command", "attempted", "attempt", "command",
                  "request", "attempted_request")
STATUS_FIELDS = ("status", "status_code", "http_status", "error_status",
                 "access_status", "result_status", "outcome_status")
KIND_FIELDS = ("source_kind", "kind", "evidence_class", "passage_kind",
               "source_type", "witness_kind", "material_kind", "evidence_kind",
               "priority", "role", "role_in_claim")
SOURCE_REF_FIELDS = ("source", "source_key", "source_ref", "source_id", "src",
                     "key")
CONTAINER_KEYS = ("rows", "receipts", "entries", "records", "questions",
                  "results", "items", "freshness", "receipt")

DISSENY_KEY_RE = re.compile(r"reconcil|round[_ -]?9|escalat|disposition"
                            r"|verdict|support_scope|result|outcome", re.I)
RAW_LABEL_KEY_RE = re.compile(r"raw|worker|original|prior[_ ]?label", re.I)
ELEMENT_PATH_RE = re.compile(r"retrieval|passage|witness|quote|leg|bridge"
                             r"|sweep|negative_claim|access_failure|evidence"
                             r"|record|item|row|receipt", re.I)
PROSE_DISPOSITION_RE = re.compile(
    r"(?:reconciled|round[-_ ]?9|final)[ _-]*(?:whole[-_ ]?claim[ _-]*)?"
    r"(?:disposition|verdict|label|reading)\s*[:\-\u2014]\s*([^\n]{3,200})"
    r"|[Ww]hole[-_ ]?claim\s+(?:verdict|disposition)\s*[:\-\u2014]\s*"
    r"([^\n]{3,200})")
RAW_EXCLUDE_RE = re.compile(r"prior|raw|round[_ -]?6|round[_ -]?8|r6|r8", re.I)
LIMIT_KEY_RE = re.compile(r"deeper[_ -]?limit|remaining|unread|unretriev"
                          r"|what_remains|residual[_ -]?limit|limit", re.I)
ESCALATION_RE = re.compile(r"hunter|verifier|primary[-_ ]?source|museum"
                           r"|scholarly|full[-_ ]?text|alternate[-_ ]angle"
                           r"|escalat", re.I)
UNRESOLVED_RE = re.compile(r"unresolved|not[-_ ]established|no[-_ ]support"
                           r"|unsupported|refut|fail|insufficient|inconclusive"
                           r"|unverified|to[-_ ]verify|pending|unmet", re.I)
ATLEAST_PARTIAL_RE = re.compile(r"partial|scoped|support|established|corroborat"
                                r"|full|strong|resolved|adopted", re.I)
STRONG_SCHOLARLY_RE = re.compile(r"press|journal|universit|academ|monograph"
                                 r"|dissertat|persee|jstor|\bdoi\b|proceedings"
                                 r"|reallexikon|handbuch|iranica|studi|scholar"
                                 r"|peer[-_ ]?review", re.I)
TERTIARY_KIND_RE = re.compile(r"tertiary|encyclop|wikipedia|wiki|blog|web"
                              r"|summary|compendium|popular", re.I)
PRIMARY_KIND_RE = re.compile(r"primary|museum|catalog|catalogue|excavat"
                             r"|inscription|tablet|relief|plate|photo|artifact"
                             r"|artefact|object|witness|edition|translat"
                             r"|facsimile|archive|monument|stele|seal|vessel"
                             r"|circular|rock[-_ ]?art", re.I)
UNREADABLE_RE = re.compile(r"unreadable|unretrievable|not retrievable|remains unread"
                           r"|remains untranslated|no readable copy|not digiti[sz]ed"
                           r"|behind a paywall|offline|closed[-_ ]access"
                           r"|unavailable|restricted|could not be read", re.I)

TIMESTAMP_RE = re.compile(r"\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}"
                          r"(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:?\d{2})?)?")
DURATION_RE = re.compile(r"\b\d+(?:\.\d+)?\s*(?:ms|s|sec|secs|seconds|m|min)"
                         r"\b")
JSON_TIMING_RE = re.compile(r'("(?:seconds|elapsed|duration|runtime|took)"\s*:\s*)'
                            r'[0-9.eE+-]+')
SCRATCH_RE = re.compile(r"/(?:var/)?tmp/[^\s\"'<>]+")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
BASELINE_SKIP_PARTS = {"round-3", "round-4", "round-5"}


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


def sanitize(text, limit=400):
    """Normalize temporary paths, timestamps and durations so recorded child
    output (and its digest) is reproducible across runs."""
    text = SCRATCH_RE.sub("<scratch>", text or "")
    text = TIMESTAMP_RE.sub("<date>", text)
    text = DURATION_RE.sub("<dur>", text)
    text = JSON_TIMING_RE.sub(r"\1<dur>", text)
    text = " ".join(text.split())
    return text[:limit]


def run_cli(relative, args=(), timeout=CONTROL_TIMEOUT):
    argv = [sys.executable, relative, *args]
    try:
        proc = subprocess.run(argv, cwd=str(ROOT), capture_output=True,
                              timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"argv": argv, "exit": None, "timeout": True, "stdout": "",
                "stderr": "", "stdout_sha256": None, "stderr_sha256": None}
    except OSError as error:
        return {"argv": argv, "exit": None, "timeout": False, "stdout": "",
                "stderr": sanitize(str(error), 200), "stdout_sha256": None,
                "stderr_sha256": None}
    out = proc.stdout.decode("utf-8", "replace")
    err = proc.stderr.decode("utf-8", "replace")
    return {"argv": argv, "exit": proc.returncode, "timeout": False,
            "stdout": out, "stderr": err,
            "stdout_sha256": sha(sanitize(out, 100000000).encode()),
            "stderr_sha256": sha(sanitize(err, 100000000).encode())}


def first_match(record, fields):
    for field in fields:
        value = record.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


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


def canonical(record):
    return json.dumps(record, sort_keys=True, ensure_ascii=False)


def walk_dicts(node, path=""):
    """Yield (path, node) for every dict node at any nesting depth."""
    if not isinstance(node, dict):
        return
    yield path, node
    for key, value in node.items():
        if isinstance(value, dict):
            yield from walk_dicts(value, f"{path}{key}.")
        elif isinstance(value, list):
            for index, item in enumerate(value):
                if isinstance(item, dict):
                    yield from walk_dicts(item, f"{path}{key}[{index}].")


def iter_records(document):
    """The declared row list of a receipt document, or the document itself."""
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


def classify_kind(text):
    """primary (object record) / scholarly (full text) / tertiary / unclassified."""
    text = text or ""
    if STRONG_SCHOLARLY_RE.search(text):
        return "scholarly"
    if TERTIARY_KIND_RE.search(text):
        return "tertiary"
    if PRIMARY_KIND_RE.search(text):
        return "primary"
    return "unclassified"


def classify_disposition(label):
    if not label:
        return "absent"
    if UNRESOLVED_RE.search(label):
        return "below-partial"
    if ATLEAST_PARTIAL_RE.search(label):
        return "partial-or-better"
    return "unknown"


# --------------------------------------------------------------------------
# claim F -- freshness
# --------------------------------------------------------------------------

def declared_freshness():
    return load_json(TARGETS_REL)["freshness"]


def resolve_row_id(text, declared_ids, prior_map):
    upper = norm(text).upper().replace("_", "-").replace(" ", "")
    if not upper:
        return None
    if upper in declared_ids:
        return upper
    if upper in prior_map:
        return prior_map[upper]
    for token in [upper] + upper.split("-"):
        match = re.fullmatch(r"(?:R9-)?(?:R8-)?F0*(\d{1,2})[A-Z]?", token)
        if match:
            guess = f"R9-R8-F{int(match.group(1)):02d}"
            if guess in declared_ids:
                return guess
    for candidate in sorted(declared_ids, key=len, reverse=True):
        if upper.endswith(candidate) or candidate.endswith(upper):
            return candidate
    return None


def document_bindings(text, declared_ids, prior_map, scoped=False):
    """Row ids named by a document's own text (id fields or filename). With
    scoped=True only the receipt-naming family tokens (R9-F0Na) bind, so a JSON
    receipt that merely cross-references another residual's id does not inherit
    that residual's row."""
    bound = set()
    for candidate in declared_ids | set(prior_map):
        if candidate in text.upper() or candidate.replace("R9-", "") in text.upper():
            resolved = candidate if candidate in declared_ids \
                else prior_map.get(candidate)
            if resolved:
                bound.add(resolved)
    pattern = r"R9-?F0*\d{1,2}[A-Z]?(?![0-9])" if scoped \
        else r"(?:R9-?)?(?:R8-?)?F0*\d{1,2}[A-Z]?(?![0-9])"
    for short in re.findall(pattern, text.upper()):
        resolved = resolve_row_id(short, declared_ids, prior_map)
        if resolved:
            bound.add(resolved)
    return bound


def nested_retrieval_units(document):
    """Retrieval units aggregated inside one receipt file (a `retrievals` or
    `hunters` list of records), each counted as its own escalated-strategy
    retrieval receipt so an aggregated delivery is read on its merits."""
    units = {}
    for path, node in walk_dicts(document):
        if path == "":
            continue
        has_url = bool(first_match(node, URL_FIELDS))
        has_locator = bool(first_match(node, LOCATOR_FIELDS))
        has_excerpt = bool(first_match(node, EXCERPT_FIELDS))
        has_attempt = bool(first_match(node, ATTEMPT_FIELDS))
        role_keys = " ".join(node.keys())
        has_role = bool(re.search(r"hunter|verifier|scout|strategy|role|shard"
                                  r"|retrieval", role_keys, re.I))
        if (has_url and (has_locator or has_excerpt)) or has_attempt or has_role:
            units[canonical(node)] = path
    return sorted(units.values())


def load_freshness(declared_rows):
    """Per residual: distinct receipt documents (json/jsonl records and
    standalone .md files), their text, and the escalation/limit material."""
    declared_ids = {row["id"] for row in declared_rows}
    prior_map = {str(row.get("prior_row_id", "")).strip().upper(): row["id"]
                 for row in declared_rows if row.get("prior_row_id")}
    bundle = {"documents": collections.defaultdict(list),
              "json_stems": set(), "problems": [], "sources": {}}
    if not FRESHNESS_DIR.is_dir():
        bundle["problems"].append(f"missing freshness evidence directory: "
                                  f"{FRESHNESS_DIR.relative_to(ROOT)}")
        return bundle
    paths = sorted([p for p in FRESHNESS_DIR.rglob("*") if p.is_file()
                    and not any(part.startswith(".") for part in
                                p.relative_to(FRESHNESS_DIR).parts)])
    seen_digests = collections.defaultdict(set)
    for path in paths:
        relative = str(path.relative_to(ROOT))
        if path.name == "reconciliation.json":
            continue
        if path.suffix not in (".json", ".jsonl", ".md", ".txt"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as error:
            bundle["problems"].append(f"{relative}: unreadable ({error})")
            continue
        if path.suffix in (".json", ".jsonl"):
            documents = []
            if path.suffix == ".jsonl":
                for line in text.splitlines():
                    if line.strip():
                        try:
                            documents.append(json.loads(line))
                        except json.JSONDecodeError as error:
                            bundle["problems"].append(
                                f"{relative}: bad JSON line ({error})")
            else:
                try:
                    documents.append(json.loads(text))
                except json.JSONDecodeError as error:
                    bundle["problems"].append(f"{relative}: bad JSON ({error})")
                    continue
            for document in documents:
                bound = set()
                for record in iter_records(document):
                    for field in ID_FIELDS:
                        value = record.get(field)
                        if isinstance(value, str):
                            resolved = resolve_row_id(value, declared_ids,
                                                      prior_map)
                            if resolved:
                                bound.add(resolved)
                if isinstance(document, dict):
                    for field in ID_FIELDS + ("prior_row_id",):
                        value = document.get(field)
                        if isinstance(value, str):
                            resolved = resolve_row_id(value, declared_ids,
                                                      prior_map)
                            if resolved:
                                bound.add(resolved)
                bound |= document_bindings(path.stem, declared_ids, prior_map)
                if not bound:
                    bound |= document_bindings(text, declared_ids, prior_map,
                                               scoped=True)
                digest = sha(canonical(document).encode())
                units = nested_retrieval_units(document)
                for row_id in bound:
                    if digest in seen_digests[(row_id, "json")]:
                        continue
                    seen_digests[(row_id, "json")].add(digest)
                    bundle["documents"][row_id].append(
                        {"kind": "json", "path": relative, "sha256": digest,
                         "text": text, "record": document, "units": units})
            bundle["json_stems"].add(path.stem)
        else:
            bound = document_bindings(path.stem, declared_ids, prior_map)
            if not bound:
                bound = document_bindings(text, declared_ids, prior_map)
            digest = sha(text.encode())
            for row_id in bound:
                if digest in seen_digests[(row_id, "text")]:
                    continue
                seen_digests[(row_id, "text")].add(digest)
                bundle["documents"][row_id].append(
                    {"kind": "text", "path": relative, "sha256": digest,
                     "text": text, "record": {"text": text}})
        for row_id in bound:
            bundle["sources"].setdefault(row_id, relative)
    # a .md companion of a same-stem .json is a rendering, not a second receipt
    for row_id, docs in bundle["documents"].items():
        json_stems = {Path(doc["path"]).stem for doc in docs
                      if doc["kind"] == "json"}
        bundle["documents"][row_id] = [
            doc for doc in docs
            if doc["kind"] == "json"
            or Path(doc["path"]).stem not in json_stems]
    return bundle


def row_disposition_label(documents):
    """The row-level (reconciled / round-9) disposition label. Prior, raw and
    round-8 fields are excluded by design, and per-element evidence verdicts
    (passages, retrievals, legs, witnesses, quotes inside lists) are excluded so
    the reading is claim-level. Verifier prose receipts are read for explicit
    `verdict:` / `reconciled disposition:` lines. When claim-level labels
    disagree, the reading is fail-closed: any below-partial label makes the row
    below-partial, and the disagreement is recorded as a note."""
    candidates = []
    for doc in documents:
        for path, node in walk_dicts(doc["record"]):
            for key, value in node.items():
                if not DISSENY_KEY_RE.search(key) or RAW_EXCLUDE_RE.search(key):
                    continue
                if re.search(r"\[", path) and ELEMENT_PATH_RE.search(path):
                    continue
                if isinstance(value, str) and value.strip():
                    score = disposition_tier(key, path)
                    candidates.append((score, norm(value), f"{path}{key}"))
                elif isinstance(value, dict):
                    for sub in ("verdict", "label", "disposition", "disposition_label",
                                "value"):
                        item = value.get(sub)
                        if isinstance(item, str) and item.strip():
                            score = disposition_tier(key, path)
                            candidates.append((score, norm(item), f"{path}{key}.{sub}"))
        if doc.get("kind") == "text":
            for match in PROSE_DISPOSITION_RE.finditer(doc["text"]):
                label = norm(match.group(1) or match.group(2) or "")[:200]
                if label:
                    candidates.append((0, label,
                                       f"{doc['path']}:prose:{match.start()}"))
    if not candidates:
        return "", None, "absent", []
    classes = {label: classify_disposition(disposition_head(label))
               for _score, label, _path in candidates}
    notes = []
    best_score = min(score for score, _label, _path in candidates)
    same_tier = sorted({label for score, label, _path in candidates
                        if score == best_score}, key=lambda label: (-len(label), label))
    tier_classes = {classes[label] for label in same_tier}
    below = [label for label in same_tier if classes[label] == "below-partial"]
    if below and len(tier_classes) > 1:
        choice = sorted(below, key=lambda label: (len(label), label))[0]
        others = [label for label in same_tier if classes[label] != "below-partial"]
        notes.append("claim-level labels at the same tier disagree; the "
                     f"fail-closed reading is below-partial ({choice[:80]!r}) over "
                     + "; ".join(repr(label[:80]) for label in others[:2]))
        source = next(path for _score, value, path in candidates if value == choice)
        return choice, source, "below-partial", notes
    label = next((item for item in same_tier
                  if classes[item] == "below-partial"), same_tier[0])
    source = next(path for score, value, path in candidates
                  if value == label and score == best_score)
    state = classes[label]
    if state == "unknown":
        known = sorted({classes[item] for item in classes
                        if classes[item] not in ("unknown", "absent")})
        if known:
            state = known[0]
            notes.append(f"label {label[:80]!r} is not a recognizable disposition; "
                         f"row read from sibling claim-level labels {known}")
    if best_score > 0:
        notes.append(f"row verdict read from tier {best_score} labels "
                     f"(no reconciled/whole-claim verdict present)")
    return label, source, state, notes


def disposition_head(label):
    """The verdict head of a label: long receipts qualify their verdict in the
    tail ('partial-support (raw label, preserved; not upgraded...)'), and the
    qualification must not flip the reading of the head."""
    head = re.split(r"[;(\u2014]|\.\s|,\s+(?:but|though|however)", label,
                    maxsplit=1)[0]
    return norm(head) or norm(label)


def disposition_tier(key, path):
    """Rank a claim-level key: 0 reconciled/verifier verdict, 1 whole-claim,
    2 top-level verdict-like field, 3 shard contribution phrasing, 4 scope."""
    full = f"{path}{key}"
    if re.search(r"reconciled[-_ ]?(?:disposition|verdict|label)|final[-_ ]?"
                 r"(?:disposition|verdict)|round[-_ ]?9[-_ ]?(?:disposition|verdict)"
                 r"|verifier[-_ ]?(?:disposition|verdict|finding)", full, re.I) \
            and not re.search(r"contribution|propos|support", key, re.I):
        return 0
    if re.search(r"whole[-_ ]?claim", full, re.I):
        return 1
    if re.fullmatch(r"(result|verdict|disposition|outcome|finding)", key, re.I) \
            and path.count(".") <= 1:
        return 2
    if re.search(r"contribution|supports|propos|recommend|movement", full, re.I):
        return 3
    return 4


def receipt_failures(document):
    found = []
    for path, node in walk_dicts(document.get("record", {})):
        attempt = first_match(node, ATTEMPT_FIELDS)
        status = node.get(first_match(node, STATUS_FIELDS)) \
            if first_match(node, STATUS_FIELDS) else None
        if attempt and status is not None and norm(str(status)):
            found.append({"path": path, "attempt": sanitize(attempt, 120),
                          "status": sanitize(str(status), 120)})
    return found


def source_registry(document):
    """Source-key -> {url, kind, accessed} index, so a passage record that
    cites its source by key (`source: S1`) inherits that source's URL and kind
    (the receipts' own cross-reference convention)."""
    registry = {}
    for path, node in walk_dicts(document.get("record", {})):
        url = first_match(node, URL_FIELDS)
        if not url:
            continue
        entry = {"url": url, "kind": first_match(node, KIND_FIELDS),
                 "accessed": first_match(node, ACCESSED_FIELDS)}
        for field in SOURCE_REF_FIELDS:
            value = node.get(field)
            if isinstance(value, str) and value.strip() and len(value) <= 48:
                registry.setdefault(value.strip().upper(), entry)
    return registry


def receipt_passages(document):
    """Passages with a URL and a named location at any nesting depth, plus the
    per-passage kind classification and whether that kind is primary/scholarly.
    A passage may inherit its URL/kind from a source it cites by key, and its
    kind from the container key it sits under (e.g. museum_records)."""
    passages = []
    registry = source_registry(document)

    def visit(node, path, context):
        if not isinstance(node, dict):
            return
        context = dict(context)
        url = first_match(node, URL_FIELDS)
        if url:
            context["url"] = url
        accessed = first_match(node, ACCESSED_FIELDS)
        if accessed:
            context["accessed"] = accessed
        for field in SOURCE_REF_FIELDS:
            value = node.get(field)
            if isinstance(value, str) and value.strip().upper() in registry:
                entry = registry[value.strip().upper()]
                if not url:
                    context["url"] = entry["url"]
                if entry["kind"]:
                    context.setdefault("kind", entry["kind"])
                break
        locator_own = first_match(node, LOCATOR_FIELDS)
        locator = locator_own or context.get("locator", "")
        if locator_own:
            context["locator"] = locator_own
        kind_own = first_match(node, KIND_FIELDS)
        kind = kind_own or context.get("kind", "") or context.get("container", "")
        if kind_own:
            context["kind"] = kind_own
        text = first_match(node, EXCERPT_FIELDS)
        if text and len(tokens(text)) >= 3:
            effective_kind = classify_kind(kind)
            if effective_kind == "unclassified":
                effective_kind = classify_kind(text)
            if context.get("url") and locator:
                passages.append({
                    "path": path, "tokens": len(tokens(text)),
                    "url": context["url"], "locator": locator,
                    "locator_scope": "own" if locator_own else "inherited",
                    "kind": kind,
                    "evidence_class": effective_kind})
        for key, value in node.items():
            if isinstance(value, dict):
                visit(value, f"{path}{key}.", context)
            elif isinstance(value, list):
                quote_list = re.search(r"quot|excerpt|passage", key, re.I)
                child_context = dict(context)
                if not child_context.get("container"):
                    child_context["container"] = key
                for index, item in enumerate(value):
                    if isinstance(item, dict):
                        visit(item, f"{path}{key}[{index}].", child_context)
                    elif quote_list and isinstance(item, str) \
                            and len(tokens(item)) >= 3:
                        visit({"text": item}, f"{path}{key}[{index}].", child_context)

    visit(document.get("record", {}), "", {})
    return passages


def limit_evidence(documents):
    """Strings that name what remains unreadable/unretrievable."""
    items = []
    for doc in documents:
        for path, node in walk_dicts(doc["record"]):
            for key, value in node.items():
                if not LIMIT_KEY_RE.search(key) or RAW_EXCLUDE_RE.search(key):
                    continue
                if isinstance(value, str) and value.strip():
                    items.append((f"{doc['path']}:{path}{key}", norm(value)))
                elif isinstance(value, list):
                    for index, item in enumerate(value):
                        if isinstance(item, str) and item.strip():
                            items.append((f"{doc['path']}:{path}{key}[{index}]",
                                          norm(item)))
                        elif isinstance(item, dict):
                            blob = " ".join(str(v) for v in item.values()
                                            if isinstance(v, str))
                            if blob.strip():
                                items.append((f"{doc['path']}:{path}{key}[{index}]",
                                              norm(blob)))
        for match in UNREADABLE_RE.finditer(doc["text"]):
            start = max(0, match.start() - 120)
            items.append((f"{doc['path']}:unreadable-statement",
                          norm(doc["text"][start:match.end() + 120])))
    return items


def f_reconciliation(declared_rows, documents, reconciliation,
                     reconciliation_present, r8_rows):
    """Raw labels kept apart from reconciled dispositions."""
    failures = []
    detail = {"round9_file": reconciliation_present,
              "round8_reference": bool(r8_rows)}
    declared_ids = [row["id"] for row in declared_rows]
    prior_map = {str(row.get("prior_row_id", "")).strip().upper(): row["id"]
                 for row in declared_rows if row.get("prior_row_id")}
    if reconciliation_present:
        rows = reconciliation_rows(reconciliation)
        detail["rows"] = len(rows)
        bound = []
        for row in rows:
            if not isinstance(row, dict):
                continue
            resolved = None
            for field in ID_FIELDS + ("prior_row_id", "prior_row"):
                value = row.get(field)
                if isinstance(value, str) and value.strip():
                    resolved = resolve_row_id(value, set(declared_ids), prior_map)
                    if resolved:
                        break
            if resolved is None:
                failures.append("reconciliation row without a declared id: "
                                + canonical(row)[:120])
                continue
            bound.append(resolved)
            raw_key = next((f for f in RAW_FIELDS if f in row), None)
            reconciled_key = next((f for f in RECONCILED_FIELDS if f in row), None)
            if not raw_key or not reconciled_key or raw_key == reconciled_key:
                failures.append(
                    f"{resolved}: reconciliation does not keep the raw worker "
                    f"label apart from a distinct reconciled disposition "
                    f"(raw field={raw_key or 'absent'}, reconciled field="
                    f"{reconciled_key or 'absent'})")
                continue
            raw_value = norm(row.get(raw_key))
            reconciled_value = norm(row.get(reconciled_key))
            if not raw_value:
                failures.append(f"{resolved}: reconciliation raw worker label is empty")
            if not reconciled_value:
                failures.append(f"{resolved}: reconciliation reconciled disposition "
                                "is empty")
            if raw_value and raw_value == reconciled_value:
                detail.setdefault("notes", []).append(
                    f"{resolved}: raw field and reconciled field carry the same "
                    f"value '{raw_value}'; the fields are distinct, so the raw "
                    "label is preserved next to the disposition")
            prior = next((row2.get("prior_row_id", "") for row2 in declared_rows
                          if row2["id"] == resolved), "")
            reference = r8_rows.get(str(prior).upper(), {})
            if raw_value and reference:
                haystack = " ".join(str(value) for value in reference.values()
                                    if isinstance(value, str)).casefold()
                needle = raw_value.casefold()
                if needle not in haystack and not any(
                        part and part in needle for part in
                        (reference.get("raw_label", "").casefold(),
                         reference.get("raw_support_scope", "").casefold(),
                         reference.get("reconciled_disposition", "").casefold())):
                    failures.append(
                        f"{resolved}: reconciliation raw label '{raw_value}' is "
                        f"none of the preserved round-8 labels for {prior} "
                        f"(raw_label={reference.get('raw_label')!r}, "
                        f"scope={reference.get('raw_support_scope')!r}, "
                        f"reconciled={reference.get('reconciled_disposition')!r})")
                elif raw_value.casefold() == \
                        str(reference.get("reconciled_disposition", "")).casefold():
                    detail.setdefault("notes", []).append(
                        f"{resolved}: raw field carries the round-8 reconciled "
                        f"disposition '{raw_value}'; the round-8 raw worker label "
                        f"{reference.get('raw_label')!r} remains preserved in "
                        f"{R8_RECONCILIATION_REL}")
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
        detail["bound"] = len(bound)
        return failures, detail
    # fallback: raw labels kept apart from a disposition reading inside the
    # residuals' own receipts (the receipts' own convention: `raw_worker_label`
    # / `raw_labels_preserved` next to `result` / `whole_claim_support`)
    pairs = 0
    round8_notes = []
    for row_id in declared_ids:
        docs = documents.get(row_id, [])
        found = None
        for doc in docs:
            raw_labels = []
            dispositions = []
            for path, node in walk_dicts(doc["record"]):
                for key, value in node.items():
                    if RAW_EXCLUDE_RE.search(key) and RAW_LABEL_KEY_RE.search(key):
                        if isinstance(value, str) and value.strip():
                            raw_labels.append((f"{path}{key}", norm(value)))
                        elif isinstance(value, (list, dict)):
                            blob = " ".join(str(item) for item in
                                            (value.values() if isinstance(value, dict)
                                             else value) if isinstance(item, str))
                            if blob.strip():
                                raw_labels.append((f"{path}{key}", norm(blob)))
                    elif isinstance(value, str) and value.strip() \
                            and disposition_tier(key, path) <= 2 \
                            and value not in ("", "true", "false"):
                        dispositions.append((f"{path}{key}", norm(value)))
            for raw_key, raw_value in raw_labels:
                for reconciled_key, reconciled_value in dispositions:
                    if raw_key == reconciled_key or not raw_value \
                            or not reconciled_value or raw_value == reconciled_value:
                        continue
                    if len(reconciled_value) < 3:
                        continue
                    found = {"raw": raw_value, "raw_field": raw_key,
                             "disposition": reconciled_value,
                             "disposition_field": reconciled_key,
                             "receipt": doc["path"]}
                    break
                if found:
                    break
            if found:
                break
        if found:
            pairs += 1
            prior = str(next((row2.get("prior_row_id", "") for row2 in declared_rows
                              if row2["id"] == row_id), "")).upper()
            reference = r8_rows.get(prior, {})
            needle = found["raw"].casefold()
            matched = True
            if reference:
                matched = any(
                    part and (part in needle or needle in part) for part in
                    (str(reference.get("raw_label", "")).casefold(),
                     str(reference.get("raw_support_scope", "")).casefold(),
                     str(reference.get("reconciled_disposition", "")).casefold()))
                if not matched:
                    round8_notes.append(
                        f"{row_id}: receipt raw label {found['raw'][:60]!r} "
                        f"matches none of the preserved round-8 labels for "
                        f"{prior} (raw_label={reference.get('raw_label')!r})")
            found["round8_match"] = matched
            detail.setdefault("receipt_pairs_detail", {})[row_id] = found
        else:
            failures.append(
                f"{row_id}: no reconciliation file and no raw label kept apart "
                "from a disposition reading inside the residual's receipts "
                "(raw labels not preserved)")
    detail["receipt_pairs"] = pairs
    if round8_notes:
        detail.setdefault("notes", []).extend(round8_notes)
    if not reconciliation_present:
        detail["note"] = (f"{RECONCILIATION_REL} absent; raw labels kept apart "
                          "from disposition readings inside the receipts were "
                          "read instead")
    return failures, detail


def reconciliation_rows(document):
    for key in ("rows", "entries", "records", "items", "reconciliation",
                "residuals"):
        value = document.get(key)
        if isinstance(value, list):
            return value
    return []


def load_r8_reconciliation():
    if not (ROOT / R8_RECONCILIATION_REL).is_file():
        return {}
    try:
        document = load_json(R8_RECONCILIATION_REL)
    except json.JSONDecodeError:
        return {}
    rows = {}
    for row in reconciliation_rows(document):
        if isinstance(row, dict) and isinstance(row.get("id"), str):
            rows[norm(row["id"]).upper()] = row
    return rows


def f_measure(declared_rows, bundle, reconciliation):
    failures = list(bundle["problems"])
    row_results = {}
    moved_rows = []
    unresolved_rows = []
    detail = {"receipt_counts": {}, "dispositions": {}, "primary_scholarly_rows": []}
    for row in declared_rows:
        row_id = row["id"]
        docs = bundle["documents"].get(row_id, [])
        top_documents = len(docs)
        units = sum(len(doc.get("units") or []) for doc in docs)
        receipts = max(top_documents, units)
        detail["receipt_counts"][row_id] = receipts
        if receipts < F_MIN_RECEIPTS:
            failures.append(
                f"{row_id}: {receipts} receipt document(s) under "
                f"{FRESHNESS_DIR.relative_to(ROOT)}/, fewer than the declared "
                f"{F_MIN_RECEIPTS} escalated-strategy retrieval receipts")
        escalation_markers = sorted({match.group(0).casefold()
                                     for doc in docs
                                     for match in ESCALATION_RE.finditer(doc["text"])})
        if docs and not escalation_markers:
            failures.append(f"{row_id}: no receipt names an escalation role "
                            "(hunter/verifier/primary-source/museum/scholarly/"
                            "alternate-angle)")
        passages = [p for doc in docs for p in receipt_passages(doc)]
        failures_found = [f for doc in docs for f in receipt_failures(doc)]
        primary_scholarly = [p for p in passages
                             if p["evidence_class"] in ("primary", "scholarly")]
        label, label_source, state, disposition_notes = \
            row_disposition_label(docs)
        limits = limit_evidence(docs)
        limit_tokens = sum(len(tokens(text)) for _source, text in limits)
        row_results[row_id] = {
            "receipts": receipts,
            "documents": top_documents,
            "nested_retrieval_units": units,
            "document_paths": sorted({doc["path"] for doc in docs}),
            "escalation_markers": escalation_markers,
            "passages": len(passages),
            "primary_scholarly_passages": len(primary_scholarly),
            "documented_failures": len(failures_found),
            "passage_shapes": sorted({p["evidence_class"] for p in passages}),
            "disposition_label": label,
            "disposition_source": label_source,
            "disposition_class": state,
            "disposition_notes": disposition_notes,
            "limit_evidence_tokens": limit_tokens,
            "limit_evidence_items": len(limits)}
        detail["dispositions"][row_id] = label
        if docs and not passages and not failures_found:
            failures.append(
                f"{row_id}: receipts carry neither a retrieved passage (URL + "
                "named location + excerpt) nor a documented access failure "
                "(attempt + status)")
        if state == "partial-or-better" and primary_scholarly:
            moved_rows.append(row_id)
            detail["primary_scholarly_rows"].append(row_id)
        if state == "partial-or-better" and not primary_scholarly:
            detail.setdefault("notes", []).append(
                f"{row_id}: reconciled disposition '{label}' is at "
                "partial-support-or-better but no primary/scholarly passage was "
                "classified, so the row does not count toward the declared "
                f"{F_MIN_MOVED} rows on primary or scholarly passages")
        if state in ("below-partial", "absent", "unknown"):
            unresolved_rows.append(row_id)
            if limit_tokens < F_MIN_LIMIT_TOKENS:
                failures.append(
                    f"{row_id}: disposition '{label or 'absent'}' stays below "
                    f"partial-support without a deeper-limit receipt naming what "
                    f"remains unreadable/unretrievable ({limit_tokens} limit "
                    f"token(s), {F_MIN_LIMIT_TOKENS} required)")
    if len(moved_rows) < F_MIN_MOVED:
        failures.append(
            f"fewer than {F_MIN_MOVED} of the {len(declared_rows)} residuals "
            f"moved to partial-support-or-better on a primary or scholarly "
            f"passage: {moved_rows}")
    reconciliation_failures, reconciliation_detail = f_reconciliation(
        declared_rows, bundle["documents"], reconciliation,
        (ROOT / RECONCILIATION_REL).is_file(), load_r8_reconciliation())
    failures.extend(reconciliation_failures)
    detail["moved_rows"] = moved_rows
    detail["unresolved_rows"] = unresolved_rows
    detail["reconciliation"] = reconciliation_detail
    return failures, {"rows": row_results, "detail": detail}


def f_negative_controls(declared_rows, bundle):
    """In-memory controls: each mutation of the landed evidence must be
    rejected with the expected diagnostic (or the check is not load-bearing)."""
    controls = []

    def observe(name, expected, mutate):
        trial = copy.deepcopy(bundle)
        if mutate(trial) is False:
            controls.append({"control": name, "rejected": False,
                             "skipped": "evidence this control needs has not "
                                        "landed yet"})
            return
        failures, _ = f_measure(declared_rows, trial, {})
        joined = " | ".join(failures)
        if expected not in joined:
            raise ValueError(f"control {name}: expected {expected!r} in "
                             f"diagnostics, got {joined!r}")
        controls.append({"control": name, "rejected": True,
                         "diagnostic": expected})

    def drop_receipts(trial):
        row_id = next((row["id"] for row in declared_rows
                       if trial["documents"].get(row["id"])), None)
        if row_id is None:
            return False
        trial["documents"][row_id] = [
            {"kind": "json", "path": "control", "sha256": "0" * 64,
             "text": "control receipt", "units": [],
             "record": {"id": row_id}}]

    def strip_escalation(trial):
        changed = False
        for docs in trial["documents"].values():
            for doc in docs:
                if ESCALATION_RE.search(doc["text"]):
                    doc["text"] = ESCALATION_RE.sub("retrieved", doc["text"])
                    doc["record"] = {"text": doc["text"]}
                    changed = True
        return changed

    def force_unresolved(trial):
        changed = False
        for docs in trial["documents"].values():
            for doc in docs:
                doc["record"] = {"reconciled_disposition": "unresolved",
                                 "text": "no limits recorded"}
                doc["text"] = "no limits recorded"
                changed = True
        return changed

    observe("missing-receipt-floor-enforced", "fewer than the declared", 
            drop_receipts)
    observe("escalation-role-required", "no receipt names an escalation role",
            strip_escalation)
    observe("deeper-limit-receipt-required", "without a deeper-limit receipt",
            force_unresolved)
    return controls


def measure_f():
    declared_rows = declared_freshness()
    bundle = load_freshness(declared_rows)
    reconciliation = load_json(RECONCILIATION_REL) \
        if (ROOT / RECONCILIATION_REL).is_file() else {}
    failures, measured = f_measure(declared_rows, bundle, reconciliation)
    try:
        controls = f_negative_controls(declared_rows, bundle)
        control_error = None
    except ValueError as error:
        controls = []
        control_error = str(error)
        failures.append("F negative controls: " + control_error)
    measurement = measured["detail"]
    measurement["negative_controls"] = controls
    measurement["control_error"] = control_error
    measurement["receipt_sources"] = bundle["sources"]
    measurement["declared_ids"] = [row["id"] for row in declared_rows]
    measurement["row_measurements"] = measured["rows"]
    return {"passed": not failures, "measurement": measurement,
            "failures": failures}


# --------------------------------------------------------------------------
# claim O -- operability
# --------------------------------------------------------------------------

def gate_modules():
    return sorted((ROOT / GATES_DIR_REL).glob("*.py"))


def normalize_token(text):
    return re.sub(r"[^a-z0-9]+", "-", str(text).casefold()).strip("-")


def gate_binding(payload, path, gates):
    """Which gate a baseline dir/expected.json belongs to, or None."""
    candidates = []
    for field in ("gate", "gate_name", "gate_path", "tool"):
        value = payload.get(field)
        if isinstance(value, str) and value.strip():
            candidates.append(value)
    relative = Path(path.relative_to(ROOT))
    candidates.append(relative.as_posix())
    for gate in gates:
        stem = normalize_token(gate.stem)
        for candidate in candidates:
            token = normalize_token(Path(candidate).name)
            if len(stem) >= 6 and (stem in token or token in stem):
                return gate.relative_to(ROOT).as_posix()
        for part in relative.parts:
            token = normalize_token(part)
            if len(stem) >= 6 and (stem in token or token in stem):
                return gate.relative_to(ROOT).as_posix()
    return None


def discover_baselines():
    found = []
    for root_rel in BASELINE_ROOTS:
        root = ROOT / root_rel
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("expected.json")):
            relative_parts = path.relative_to(root).parts
            if any(part.startswith(".") or part in BASELINE_SKIP_PARTS
                   for part in relative_parts):
                continue
            found.append(path)
    return found


def read_baseline(path, gates, payload=None, resolver=None):
    """Evaluate one expected.json baseline against the frozen-run standard."""
    relative = path.relative_to(ROOT).as_posix()
    result = {"path": relative, "baseline_id": path.parent.name,
              "failures": []}
    try:
        if payload is None:
            payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, UnicodeDecodeError) as error:
        result["failures"].append(f"{relative}: unreadable or malformed "
                                  f"expected.json ({error})")
        return result
    if not isinstance(payload, dict):
        result["failures"].append(f"{relative}: expected.json is not a JSON object")
        return result
    result["gate_binding"] = gate_binding(payload, path, gates)
    if result["gate_binding"] is None:
        result["failures"].append(f"{relative}: baseline does not bind to any "
                                  "tools/gates/*.py gate")
    schema = payload.get("schema")
    result["schema"] = schema
    if not isinstance(schema, str) or not re.search(r"frozen[-_ ]?run", schema, re.I):
        result["failures"].append(f"{relative}: schema {schema!r} is not a "
                                  "frozen-run schema (standard section 4)")
    for field in ("gate", "gate_sha256", "revision", "frozen_at", "frozen_by"):
        value = payload.get(field)
        if not isinstance(value, str) or not value.strip():
            result["failures"].append(f"{relative}: required field {field!r} "
                                      "missing or empty")
    gate_sha = payload.get("gate_sha256")
    result["gate_sha_ok"] = None
    if isinstance(gate_sha, str) and result["gate_binding"]:
        live = file_sha(result["gate_binding"])
        result["gate_sha_ok"] = (gate_sha.lower() == (live or ""))
        if not result["gate_sha_ok"]:
            result["failures"].append(
                f"{relative}: gate_sha256 {gate_sha[:16]}... differs from the "
                f"live {result['gate_binding']} ({(live or 'absent')[:16]}...) "
                "-- gate_revised, could-not-evaluate, re-freeze required")
    inputs = payload.get("inputs")
    if not isinstance(inputs, dict) or not inputs:
        result["failures"].append(f"{relative}: inputs map is absent or empty "
                                  "(unpinned baseline, standard KTD-FR-S-0002)")
    else:
        resolved, local, missing, tampered, unsafe = 0, 0, [], [], []
        for key, digest in sorted(inputs.items()):
            if not isinstance(digest, str) or not SHA_RE.match(digest):
                result["failures"].append(f"{relative}: input {key!r} digest is "
                                          f"not a lowercase sha256: {digest!r}")
                continue
            if Path(key).is_absolute() or ".." in Path(key).parts:
                unsafe.append(key)
                result["failures"].append(f"{relative}: input key {key!r} is "
                                          "absolute or traverses outside the "
                                          "baseline")
                continue
            if resolver is not None:
                data, source = resolver(key)
                if data is None:
                    missing.append(key)
                    continue
                resolved += 1
                if source == "baseline":
                    local += 1
                actual = sha(data)
            else:
                local_path = path.parent / key
                repo_path = ROOT / key
                if local_path.is_file():
                    resolved += 1
                    local += 1
                    actual = sha(local_path.read_bytes())
                elif repo_path.is_file():
                    resolved += 1
                    actual = sha(repo_path.read_bytes())
                else:
                    missing.append(key)
                    continue
            if actual != digest:
                tampered.append(key)
                result["failures"].append(
                    f"{relative}: snapshot_tampered for {key!r} (pinned "
                    f"{digest[:16]}..., actual {actual[:16]}...)")
        result["inputs"] = len(inputs)
        result["resolved"] = resolved
        result["local_snapshots"] = local
        result["missing_inputs"] = missing
        result["tampered_inputs"] = tampered
        result["unsafe_inputs"] = unsafe
        if missing:
            result["failures"].append(
                f"{relative}: pinned input(s) resolve neither inside the "
                f"baseline nor in the repository: {missing}")
        if resolved and not local:
            result["failures"].append(
                f"{relative}: no input is a baseline-local snapshot copy -- the "
                "baseline re-inherits live paths (standard KTD-FR-S-0003)")
    expected = payload.get("expected")
    result["expected"] = expected if isinstance(expected, dict) else None
    if not isinstance(expected, dict):
        result["failures"].append(f"{relative}: expected block missing")
    else:
        exit_code = expected.get("exit")
        klass = expected.get("class")
        findings = expected.get("findings")
        if exit_code not in (0, 1) or isinstance(exit_code, bool):
            result["failures"].append(f"{relative}: expected.exit {exit_code!r} "
                                      "is not 0 or 1")
        if klass not in ("clean", "findings"):
            result["failures"].append(f"{relative}: expected.class {klass!r} is "
                                      "not clean or findings")
        if exit_code == 0 and klass != "clean":
            result["failures"].append(f"{relative}: expected.exit 0 requires "
                                      "class clean, got {klass!r}")
        if exit_code == 1 and klass != "findings":
            result["failures"].append(f"{relative}: expected.exit 1 requires "
                                      "class findings, got {klass!r}")
        if not isinstance(findings, list) or not all(
                isinstance(item, str) for item in findings):
            result["failures"].append(f"{relative}: expected.findings must be a "
                                      "list of stable finding ids"
                                      if findings is not None else
                                      f"{relative}: expected.findings missing")
        else:
            result["findings_count"] = len(findings)
    result["valid"] = not result["failures"]
    return result


def baseline_reader_controls():
    """Exercise the runner's own baseline reader on synthetic payloads so the
    digest/failure reading is shown to be load-bearing. Only the file-system
    seam (byte resolution) is stubbed; every structural and digest assertion
    runs the real code path."""
    controls = []
    packet = "tools/gates/fixtures/myth-consistency-gate.yml"
    packet_bytes = (ROOT / packet).read_bytes()
    good_digest = sha(packet_bytes)
    gate = ROOT / "tools/gates/myth-consistency-gate.py"
    gate_digest = sha(gate.read_bytes())

    def synthetic(**overrides):
        payload = {"schema": "kotadama-frozen-run-v1",
                   "gate": "myth-consistency-gate",
                   "gate_sha256": gate_digest, "revision": "0" * 40,
                   "frozen_at": "2026-10-17T00:00:00", "frozen_by": "r9-control",
                   "inputs": {packet: good_digest},
                   "expected": {"exit": 1, "class": "findings",
                                "findings": ["MC-P01"]}}
        payload["schema"] = "kotodama-frozen-run-v1"
        payload.update(overrides)
        return payload

    def resolver(key):
        if key == packet:
            return packet_bytes, "baseline"
        return None, None

    def evaluate(name, payload, expect_valid, expect_token):
        failures = []

        class FakePath:
            def __init__(self, payload):
                self.payload = payload

            def read_text(self, encoding="utf-8"):
                return json.dumps(self.payload)

            @property
            def parent(self):
                return ROOT / "tools/gates/frozen/myth-consistency-gate/r9-control"

            def relative_to(self, _root):
                return Path("tools/gates/frozen/myth-consistency-gate/"
                            "r9-control/expected.json")

        result = read_baseline(FakePath(payload), gate_modules(),
                               resolver=resolver)
        joined = " | ".join(result["failures"])
        ok = result["valid"] is expect_valid and expect_token in joined
        controls.append({"control": name, "behaved": ok,
                         "valid": result["valid"],
                         "diagnostic": sanitize(joined, 200)})
        return ok

    good = evaluate("good-baseline-accepted", synthetic(), True, "")
    tampered = evaluate("tampered-digest-rejected",
                        synthetic(inputs={packet: "0" * 64}),
                        False, "snapshot_tampered")
    missing = evaluate("missing-snapshot-rejected",
                       synthetic(inputs={"tools/gates/fixtures/absent.yml":
                                         "0" * 64}),
                       False, "resolve neither")
    unpinned = evaluate("unpinned-rejected", synthetic(inputs={}),
                        False, "unpinned baseline")
    revised = evaluate("gate-revision-rejected",
                       synthetic(gate_sha256="f" * 64),
                       False, "gate_revised")
    return {"controls": controls,
            "all_behaved": all([good, tampered, missing, unpinned, revised])}


def measure_o_baselines(gates):
    result = {"gates": len(gates), "baselines": [], "per_gate": {}}
    failures = []
    discovered = discover_baselines()
    result["discovered"] = [path.relative_to(ROOT).as_posix()
                            for path in discovered]
    for path in discovered:
        evaluation = read_baseline(path, gates)
        result["baselines"].append(evaluation)
        gate = evaluation.get("gate_binding")
        if gate:
            result["per_gate"].setdefault(gate, []).append(evaluation)
        failures.extend(evaluation["failures"])
    for gate in gates:
        binding = gate.relative_to(ROOT).as_posix()
        entries = result["per_gate"].get(binding, [])
        if not entries:
            failures.append(f"{binding}: no expected.json baseline found under "
                            + ", ".join(BASELINE_ROOTS))
    result["gates_covered"] = sum(1 for gate in gates
                                  if result["per_gate"].get(
                                      gate.relative_to(ROOT).as_posix()))
    return result, failures


def measure_o_battery(baselines=None):
    baselines = baselines or {"baselines": []}
    result = {"path": BATTERY_REL}
    failures = []
    if not (ROOT / BATTERY_REL).is_file():
        failures.append(f"missing battery runner: {BATTERY_REL}")
        result["failure"] = failures[-1]
        return result, failures
    source = (ROOT / BATTERY_REL).read_text(encoding="utf-8")
    result["sha256"] = file_sha(BATTERY_REL)
    result["extension_present"] = bool(re.search(r"expected\.json|baseline",
                                                 source, re.I))
    if not result["extension_present"]:
        failures.append(f"{BATTERY_REL}: baseline-validation extension not "
                        "landed (source names neither expected.json nor a "
                        "baseline)")
    selftest = run_cli(BATTERY_REL, ["--selftest"], timeout=BATTERY_TIMEOUT)
    result["selftest"] = {"exit": selftest["exit"],
                          "stdout_sha256": selftest["stdout_sha256"],
                          "tail": sanitize(selftest["stdout"], 300)}
    if selftest["exit"] != 0:
        failures.append(f"{BATTERY_REL} --selftest exit {selftest['exit']} "
                        "(expected 0): " + sanitize(selftest["stdout"], 200))
    combined = selftest["stdout"] + selftest["stderr"]
    if "Traceback" in combined:
        failures.append(f"{BATTERY_REL} --selftest printed a traceback")
    baseline_control = bool(re.search(r"baseline|expected\.json", combined, re.I))
    tamper_control = bool(re.search(r"tamper|snapshot[-_ ]?tampered|drift"
                                    r"|could[-_ ]not[-_ ]evaluate", combined, re.I))
    result["selftest"]["baseline_control"] = baseline_control
    result["selftest"]["tamper_or_drift_control"] = tamper_control
    if selftest["exit"] == 0 and not baseline_control:
        failures.append(f"{BATTERY_REL} --selftest does not exercise baseline "
                        "validation")
    if selftest["exit"] == 0 and not tamper_control:
        failures.append(f"{BATTERY_REL} --selftest does not demonstrate "
                        "tamper/drift handling (never a silent pass)")
    help_run = run_cli(BATTERY_REL, ["--help"], timeout=60)
    flags = sorted(set(re.findall(r"--[a-z0-9][a-z0-9-]+", help_run["stdout"])))
    result["flags"] = flags
    validation_flags = [flag for flag in flags
                        if re.search(r"baseline|frozen|validate", flag)]
    result["validation_flags"] = validation_flags
    result["value_taking_flags"] = [flag for flag in validation_flags
                                    if flag_takes_value(flag, help_run["stdout"])]
    for flag in [flag for flag in validation_flags
                 if not flag_takes_value(flag, help_run["stdout"])][:1]:
        run = run_cli(BATTERY_REL, [flag], timeout=BATTERY_TIMEOUT)
        result["field_run"] = {"flag": flag, "exit": run["exit"],
                               "stdout_sha256": run["stdout_sha256"],
                               "tail": sanitize(run["stdout"], 300)}
        if run["exit"] != 0:
            failures.append(f"{BATTERY_REL} {flag} exit {run['exit']} "
                            "(expected 0): " + sanitize(run["stdout"], 200))
    plain = run_cli(BATTERY_REL, [], timeout=BATTERY_TIMEOUT)
    result["plain_run"] = {"exit": plain["exit"],
                           "stdout_sha256": plain["stdout_sha256"],
                           "tail": sanitize(plain["stdout"], 300)}
    for run in (plain,):
        try:
            document = json.loads(run["stdout"])
        except json.JSONDecodeError:
            document = None
        if isinstance(document, dict):
            baseline_block = document.get("baselines")
            if isinstance(baseline_block, dict):
                result["baseline_check"] = {
                    "summary": baseline_block.get("summary"),
                    "roots": [entry.get("root") for entry in
                              (baseline_block.get("roots") or [])
                              if isinstance(entry, dict)],
                    "findings": [{"id": item.get("id"),
                                  "message": item.get("message")}
                                 for item in (baseline_block.get("findings") or [])
                                 if isinstance(item, dict)][:8]}
            result["battery_summary"] = document.get("summary")
    # the round's own layout: the battery validates every committed baseline
    # when the roots the baselines actually landed in are named. The default
    # roots are the battery's committed default and are recorded separately;
    # audit-18 section 6.1 leaves their reconciliation to the orchestrator
    # (add the third root or relocate the two baselines), so the round-roots
    # reading is the declared "validates every baseline" evidence and the
    # default-root gap is reported with both options.
    round_roots = [root for root in BASELINE_ROOTS
                   if (ROOT / root).is_dir() and any(
                       (ROOT / root).rglob("expected.json"))]
    result["round_roots"] = round_roots
    if round_roots:
        argv = [item for root in round_roots
                for item in ("--baselines-root", root)]
        run = run_cli(BATTERY_REL, argv, timeout=BATTERY_TIMEOUT)
        summary = {}
        findings = []
        try:
            document = json.loads(run["stdout"])
            summary = (document.get("baselines") or {}).get("summary") or {}
            findings = [{"id": item.get("id"), "message": item.get("message")}
                        for item in ((document.get("baselines") or {})
                                     .get("findings") or [])
                        if isinstance(item, dict)][:8]
        except json.JSONDecodeError:
            document = None
        result["round_roots_run"] = {
            "argv": [BATTERY_REL, *argv], "exit": run["exit"],
            "stdout_sha256": run["stdout_sha256"], "summary": summary,
            "findings": findings, "tail": sanitize(run["stdout"], 200)}
        if run["exit"] != 0:
            failures.append(
                f"{BATTERY_REL} with the round's baseline roots "
                f"({', '.join(round_roots)}) exit {run['exit']} (expected 0): "
                + sanitize(run["stdout"], 220))
        elif summary.get("gates_uncovered") or summary.get("findings") or \
                summary.get("pinned") != summary.get("baselines_found"):
            failures.append(
                f"{BATTERY_REL} with the round's baseline roots does not pin "
                f"every baseline: {json.dumps(summary, sort_keys=True)}")
    else:
        failures.append(f"{BATTERY_REL}: no baseline root holds an expected.json")
    if plain["exit"] != 0:
        summary = ((result.get("baseline_check") or {}).get("summary") or {})
        uncovered = summary.get("gates_uncovered")
        hints = []
        for gate in uncovered or []:
            stem = Path(gate).stem
            for entry in baselines.get("baselines", []):
                if entry.get("gate_binding") and \
                        Path(entry["gate_binding"]).stem == stem \
                        and entry.get("valid"):
                    hints.append(f"{stem}: a valid baseline exists at "
                                 f"{entry['path']}")
                    break
        detail = ("; ".join(hints) if hints else sanitize(plain["stdout"], 200))
        result["default_root_gap"] = {
            "exit": plain["exit"], "gates_uncovered": uncovered,
            "note": ("the battery's committed default roots do not cover every "
                     "baseline; audit-18 section 6.1 leaves the root-list "
                     "reconciliation to the orchestrator (add "
                     "reports/round-9/baselines/ to the battery's committed "
                     "roots, or relocate the named baselines into a committed "
                     "root)"),
            "existing_valid_baselines": hints}
        if not round_roots:
            failures.append(f"{BATTERY_REL} exit {plain['exit']} on the delivered "
                            "tree (expected 0)" + note_or_empty(uncovered)
                            + ": " + detail)
    return result, failures


def note_or_empty(uncovered):
    return (f" (battery reports uncovered gates: {uncovered})" if uncovered else "")


def flag_takes_value(flag, help_text):
    """A discovered long option is value-taking when argparse renders a
    metavar after it (`--baselines-root PATH`)."""
    for line in help_text.splitlines():
        if flag in line:
            rest = line.split(flag, 1)[1].strip()
            tokens_rest = rest.split()
            if not tokens_rest:
                return False
            token = tokens_rest[0]
            return token.isupper() or token.startswith("<")
    return False


def measure_o_gates_unchanged(gates, fragment_texts):
    result = {"gates": []}
    failures = []
    for gate in gates:
        relative = gate.relative_to(ROOT).as_posix()
        live = sha(gate.read_bytes())
        head = subprocess.run(["git", "show", f"HEAD:{relative}"],
                              cwd=str(ROOT), capture_output=True, timeout=60)
        head_sha = sha(head.stdout) if head.returncode == 0 else None
        entry = {"path": relative, "sha256": live, "head_sha256": head_sha,
                 "unchanged": live == head_sha}
        if live != head_sha:
            documented = [name for name, text in fragment_texts.items()
                          if Path(relative).name in text
                          and re.search(r"behavior|behaviour|rationale|reason",
                                        text, re.I)]
            entry["documented_reason"] = documented
            if documented:
                entry["reading"] = "modified with a documented reason fragment"
            else:
                failures.append(f"{relative}: gate bytes differ from HEAD "
                                "without a documented reason fragment")
        result["gates"].append(entry)
    status = subprocess.run(["git", "status", "--porcelain", "--",
                             GATES_DIR_REL], cwd=str(ROOT),
                            capture_output=True, timeout=60)
    entries = [line for line in
               status.stdout.decode("utf-8", "replace").splitlines()
               if line.strip()]
    result["git_status"] = entries
    modified = [line for line in entries
                if not line.startswith("??") and line.split()[-1].endswith(".py")]
    result["modified_gate_scripts"] = modified
    result["untracked_additions"] = [line for line in entries
                                     if line.startswith("??")]
    if modified:
        failures.append("gate script(s) modified against HEAD: "
                        + "; ".join(modified[:5]))
    result["unchanged_count"] = sum(1 for entry in result["gates"]
                                    if entry["unchanged"])
    return result, failures


def round9_fragment_texts():
    texts = {}
    root = ROOT / "reports/round-9"
    if not root.is_dir():
        return texts
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path == ROOT / OUTPUT_REL:
            continue
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        if path.suffix not in (".md", ".txt", ".json", ".jsonl"):
            continue
        try:
            texts[path.relative_to(ROOT).as_posix()] = path.read_text(
                encoding="utf-8", errors="replace")
        except OSError:
            continue
    return texts


def measure_o():
    gates = gate_modules()
    baselines, baseline_failures = measure_o_baselines(gates)
    battery, battery_failures = measure_o_battery(baselines)
    fragments = round9_fragment_texts()
    gate_state, gate_failures = measure_o_gates_unchanged(gates, fragments)
    reader_controls = baseline_reader_controls()
    if not reader_controls["all_behaved"]:
        baseline_failures.append("baseline reader controls did not all behave "
                                 "as declared")
    failures = baseline_failures + battery_failures + gate_failures
    return {"passed": not failures,
            "measurement": {"baselines": baselines, "battery": battery,
                            "gate_revisions": gate_state,
                            "reader_controls": reader_controls},
            "failures": failures}


# --------------------------------------------------------------------------
# claim D -- depth (D3 acceptance)
# --------------------------------------------------------------------------

def discover_d3_manifests():
    patterns = ("reports/round-9/d3/**/*.tsv",
                "reports/round-9/**/MANIFEST*.tsv",
                "tools/gates/frozen/round-9/**/*.tsv",
                "tools/gates/frozen/r9*/**/*.tsv",
                "examples/culture-d3/**/*.tsv")
    found = []
    for pattern in patterns:
        for path in sorted(ROOT.glob(pattern)):
            if path.is_file() and path not in found:
                found.append(path)
    ranked = []
    for path in found:
        try:
            header = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        if header and "gate_sha256" in header[0] and "input_sha256" in header[0]:
            ranked.append(path)
    return ranked


def measure_d():
    result = {}
    failures = []
    # 1. deterministic D3 assembly
    if (ROOT / D3_ASSEMBLER_REL).is_file():
        first = run_cli(D3_ASSEMBLER_REL, ["--check"], timeout=300)
        second = run_cli(D3_ASSEMBLER_REL, ["--check"], timeout=300)
        result["assembler_check"] = {
            "path": D3_ASSEMBLER_REL, "exit": first["exit"],
            "exit_second": second["exit"],
            "stdout_sha256": first["stdout_sha256"],
            "stdout_sha256_second": second["stdout_sha256"],
            "repeat_identical": first["stdout_sha256"] == second["stdout_sha256"],
            "tail": sanitize(first["stdout"], 240)}
        if first["exit"] != 0:
            failures.append(f"{D3_ASSEMBLER_REL} --check exit {first['exit']} "
                            "(expected 0: byte-identical deterministic "
                            "assembly): " + sanitize(first["stdout"], 200))
        if first["exit"] == 0 and first["stdout_sha256"] != second["stdout_sha256"]:
            failures.append(f"{D3_ASSEMBLER_REL} --check output differs between "
                            "two runs (non-deterministic)")
    else:
        failures.append(f"missing D3 assembler: {D3_ASSEMBLER_REL}")
    # 2. evidence coupling selftest
    if (ROOT / COUPLING_REL).is_file():
        run = run_cli(COUPLING_REL, ["--selftest"], timeout=300)
        payload = None
        try:
            payload = json.loads(run["stdout"])
        except json.JSONDecodeError:
            pass
        result["coupling_selftest"] = {
            "path": COUPLING_REL, "exit": run["exit"],
            "stdout_sha256": run["stdout_sha256"],
            "selftest_passed": (payload or {}).get("selftest_passed"),
            "tail": sanitize(run["stdout"], 160)}
        if run["exit"] != 0:
            failures.append(f"{COUPLING_REL} --selftest exit {run['exit']} "
                            "(expected 0)")
        if payload is not None and payload.get("selftest_passed") is not True:
            failures.append(f"{COUPLING_REL} --selftest did not report "
                            "selftest_passed true")
        if "Traceback" in run["stdout"] + run["stderr"]:
            failures.append(f"{COUPLING_REL} --selftest printed a traceback")
    else:
        failures.append(f"missing coupling checker: {COUPLING_REL}")
    # 3. frozen expectation replay (digest drift check)
    if (ROOT / COUPLING_REL).is_file() and (ROOT / D3_EXPECTED_REL).is_file():
        run = run_cli(COUPLING_REL, [D3_PACKET_REL, "--frozen", D3_EXPECTED_REL],
                      timeout=300)
        findings = []
        try:
            findings = [item.get("id") for item in
                        (json.loads(run["stdout"]).get("findings") or [])]
        except json.JSONDecodeError:
            pass
        drift_paths = []
        try:
            for item in (json.loads(run["stdout"]).get("findings") or []):
                match = re.search(r"manifest digest mismatch for '([^']+)': "
                                  r"declared ([0-9a-f]{8})[0-9a-f]*, actual "
                                  r"([0-9a-f]{8})", str(item.get("message", "")))
                if match:
                    drift_paths.append({"path": match.group(1),
                                        "declared": match.group(2),
                                        "actual": match.group(3)})
        except json.JSONDecodeError:
            pass
        result["frozen_replay"] = {"argv": [COUPLING_REL, D3_PACKET_REL,
                                            "--frozen", D3_EXPECTED_REL],
                                   "exit": run["exit"], "finding_ids": findings,
                                   "drift_paths": drift_paths,
                                   "stdout_sha256": run["stdout_sha256"],
                                   "tail": sanitize(run["stdout"], 300)}
        if run["exit"] != 0:
            detail = ", ".join(f"{item['path']} ({item['declared']}... -> "
                               f"{item['actual']}...)" for item in drift_paths) \
                if drift_paths else sanitize(run["stdout"], 300)
            pointer = [path.relative_to(ROOT).as_posix()
                       for path in sorted((ROOT / D3_DIR_REL).rglob("*.md"))
                       if path.is_file()
                       and "--frozen" in path.read_text(encoding="utf-8",
                                                        errors="replace")
                       and "expected.json" in path.read_text(encoding="utf-8",
                                                             errors="replace")]
            pointer.sort(key=lambda rel: ("D3-SNAPSHOT" not in
                                          (ROOT / rel).read_text(
                                              encoding="utf-8", errors="replace"),
                                          rel))
            pointer = pointer[:8]
            result["remediation_evidence"] = pointer
            failures.append(f"{COUPLING_REL} --frozen {D3_EXPECTED_REL} exit "
                            f"{run['exit']} (expected 0: no digest drift): "
                            + detail
                            + (f" -- the round's own re-freeze diagnosis and "
                               f"demonstrated remediation path are recorded in "
                               f"{', '.join(pointer)}; re-freezing the pin is "
                               "the parent's act, and this leg turns green only "
                               "when the committed expectation replay exits 0"
                               if pointer else ""))
    else:
        failures.append(f"missing D3 frozen expectation: {D3_EXPECTED_REL}")
    # 4. replay manifest, when one is delivered
    manifests = discover_d3_manifests()
    result["replay_manifests"] = [path.relative_to(ROOT).as_posix()
                                  for path in manifests]
    result["replays"] = []
    if manifests:
        for path in manifests[:3]:
            relative = path.relative_to(ROOT).as_posix()
            run = run_cli(REPLAY_REL, [relative, "--json"], timeout=300)
            summary = {}
            try:
                summary = json.loads(run["stdout"]).get("summary") or {}
            except json.JSONDecodeError:
                pass
            result["replays"].append({"manifest": relative, "exit": run["exit"],
                                      "summary": summary,
                                      "stdout_sha256": run["stdout_sha256"]})
            clean = (run["exit"] == 0 and summary.get("rows")
                     and not summary.get("mismatch")
                     and not summary.get("could_not_evaluate")
                     and summary.get("reproduced") == summary.get("rows"))
            if not clean:
                failures.append(
                    f"{REPLAY_REL} {relative} exit {run['exit']} summary "
                    f"{json.dumps(summary, sort_keys=True) if summary else 'unparsed'} "
                    "-- expected a full reproduction with zero mismatch and "
                    "zero could-not-evaluate rows")
    else:
        result["replay_note"] = ("no round-9 D3 replay manifest discovered; the "
                                 "frozen-expectation replay above carries the "
                                 "digest-drift requirement")
    d3_dir = ROOT / D3_DIR_REL
    fragments = []
    if d3_dir.is_dir():
        for path in sorted(d3_dir.rglob("*")):
            if path.is_file() and not any(part.startswith(".")
                                          for part in
                                          path.relative_to(d3_dir).parts):
                fragments.append(path.relative_to(ROOT).as_posix())
    result["fragments"] = fragments
    result["packet_sha256"] = file_sha(D3_PACKET_REL)
    result["expected_sha256"] = file_sha(D3_EXPECTED_REL)
    return {"passed": not failures, "measurement": result, "failures": failures}


# --------------------------------------------------------------------------
# runner
# --------------------------------------------------------------------------

def main():
    claims = load_json(CLAIMS_REL)
    declared_rows = declared_freshness()
    f_result = measure_f()
    o_result = measure_o()
    d_result = measure_d()
    claims_result = {"F": f_result, "O": o_result, "D": d_result}
    passed = all(claim["passed"] for claim in claims_result.values())

    missing_dependencies = []
    if not (ROOT / RECONCILIATION_REL).is_file() and not any(
            f_result["measurement"]["row_measurements"].get(row["id"], {})
            .get("documents") for row in declared_rows):
        missing_dependencies.append(RECONCILIATION_REL)
    for row in declared_rows:
        if not f_result["measurement"]["row_measurements"] \
                .get(row["id"], {}).get("receipts"):
            missing_dependencies.append(
                f"{FRESHNESS_DIR.relative_to(ROOT)}/*{row['id']}*")
        elif f_result["measurement"]["row_measurements"] \
                .get(row["id"], {}).get("receipts") < F_MIN_RECEIPTS:
            missing_dependencies.append(
                f"{FRESHNESS_DIR.relative_to(ROOT)}/*{row['id']}* "
                f"(fewer than {F_MIN_RECEIPTS} receipts landed)")
    baselines = o_result["measurement"]["baselines"]
    if not baselines.get("gates_covered") == baselines.get("gates"):
        for gate in gate_modules():
            binding = gate.relative_to(ROOT).as_posix()
            if not baselines["per_gate"].get(binding):
                missing_dependencies.append(
                    f"{', '.join(BASELINE_ROOTS)}/**/{gate.stem}/expected.json")
    if not o_result["measurement"]["battery"].get("extension_present"):
        missing_dependencies.append(
            f"{BATTERY_REL} (baseline-validation extension)")
    if not (ROOT / D3_DIR_REL).is_dir():
        missing_dependencies.append(D3_DIR_REL + "/")

    consumed = {CLAIMS_REL, TARGETS_REL, RECONCILIATION_REL,
                R8_RECONCILIATION_REL, BATTERY_REL, D3_ASSEMBLER_REL,
                COUPLING_REL, REPLAY_REL, D3_PACKET_REL, D3_EXPECTED_REL,
                FROZEN_STANDARD_REL}
    for gate in gate_modules():
        consumed.add(gate.relative_to(ROOT).as_posix())
    for row in f_result["measurement"].get("receipt_sources", {}).values():
        consumed.add(row)
    for doc in f_result["measurement"].get("row_measurements", {}).values():
        consumed.update(doc.get("document_paths", []))
    for entry in baselines.get("baselines", []):
        consumed.add(entry["path"])
    for path in d_result["measurement"].get("fragments", []):
        consumed.add(path)
    consumed.update(discover_baseline_inputs())

    receipt = {
        "round": 9,
        "runner": str(Path(__file__).relative_to(ROOT)),
        "runner_sha256": file_sha(str(Path(__file__).relative_to(ROOT))),
        "counting_command": "python3 reports/round-9/run-validation.py",
        "claims_declared": {claim["id"]: claim["axis"]
                            for claim in claims["claims"]},
        "baseline_revision": claims.get("baseline_revision"),
        "date": claims.get("date"),
        "thresholds": {
            "F": {"min_receipts_per_residual": F_MIN_RECEIPTS,
                  "min_moved_rows": F_MIN_MOVED,
                  "min_limit_tokens": F_MIN_LIMIT_TOKENS,
                  "reconciliation": RECONCILIATION_REL},
            "O": {"baselines_required": 7,
                  "battery_selftest_exit": 0,
                  "battery_extension_required": True,
                  "battery_round_roots_exit": 0,
                  "battery_round_roots_uncovered": 0,
                  "default_root_gap": "reported with both reconciliation options, "
                                      "not failed (audit-18 section 6.1)",
                  "gate_revisions": "byte-identical to HEAD or documented reason"},
            "D": {"assembler_check_exit": 0,
                  "coupling_selftest_exit": 0,
                  "frozen_replay_exit": 0}},
        "acceptance_checks_passed": passed,
        "claims": claims_result,
        "failures": [f"claim {key}: {failure}"
                     for key in ("F", "O", "D")
                     for failure in claims_result[key]["failures"]],
        "missing_dependencies": sorted(set(missing_dependencies)),
        "input_sha256": {relative: file_sha(relative)
                         for relative in sorted(consumed)
                         if file_sha(relative) is not None},
        "limits": [
            "Receipt/schema/count/execution checks, not automated quotation "
            "truth, historical authenticity or cultural permission.",
            "F counting reads receipts structurally at any nesting depth and "
            "counts distinct documents plus the retrieval units an aggregated "
            "receipt carries; a .md companion of a same-stem .json counts once. "
            "Disposition labels are read claim-level by tier with raw/prior/"
            "round-8 and per-element verdicts excluded, classified on the "
            "verdict head, and read fail-closed when same-tier labels disagree; "
            "primary/scholarly classification is regex-based and can misclassify "
            "an unusual source kind. When no round-9 reconciliation file exists, "
            "raw labels are read as receipt fields kept apart from a disposition "
            "reading rather than as a bound table.",
            "O digest checks recompute every pinned input against the bytes on "
            "disk (baseline-local snapshot first, repository path second); they "
            "do not execute the gates over the baselines -- the battery owns "
            "that, and its baseline coverage and tamper behaviour are read from "
            "its own run and selftest.",
            "Gate behaviour change is measured as byte-identity with HEAD plus "
            "a documented-reason fragment when modified, not as a semantic diff.",
            "D replay accepts only a full reproduction with zero mismatch and "
            "zero could-not-evaluate rows; the check-evidence-coupling --frozen "
            "run is the digest-drift reading for the committed D3 expectation.",
            "Child output is recorded after normalizing temporary paths, "
            "timestamps and durations, so the receipt is reproducible across "
            "runs; child processes write their own temporary mirrors and are "
            "not sandboxed beyond their own declared behaviour.",
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
    if not passed:
        print("missing_dependencies: " + ", ".join(receipt["missing_dependencies"]))
    return 0 if passed else 1


def discover_baseline_inputs():
    """Repository-relative paths pinned by any discovered baseline, so the
    receipt records the exact consumed inputs."""
    consumed = set()
    for path in discover_baselines():
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError, UnicodeDecodeError):
            continue
        inputs = payload.get("inputs")
        if isinstance(inputs, dict):
            for key in inputs:
                if isinstance(key, str) and not Path(key).is_absolute() \
                        and ".." not in Path(key).parts \
                        and (ROOT / key).is_file():
                    consumed.add(key)
    return consumed


if __name__ == "__main__":
    sys.exit(main())
