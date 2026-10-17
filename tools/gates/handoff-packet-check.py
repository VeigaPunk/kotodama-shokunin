#!/usr/bin/env python3
"""handoff-packet-check — kotodama-shokunin adjacency gate.

Validates one handoff packet — UTF-8 Markdown, the serialization the
contract defaults to — against
`corpus/knowledge/synthesis/worldbible-integration-contract.md`:

  §4  the handoff envelope: the 16 required field names (`packet_id`,
      `packet_version`, `contract_ref`, `producer`, `recipient`,
      `request_ref`, `baseline_bible_ref`, `artifact_manifest`,
      `subject_refs`, `scope`, `dependency_manifest`, `claim_ledger`,
      `coupling_edges`, `requested_decisions`, `validation`,
      `open_questions`), plus the required content of `contract_ref`
      (ID, revision, digest), `baseline_bible_ref` (`none` only for a
      deliberately unbound research packet), `artifact_manifest` (file
      digests) and `dependency_manifest` (no floating `latest`);
  §1  the pinned contract revision/digest precede any transfer;
  §6  canon standing is lore's (`not canonized` unless lore's own record
      says otherwise; §8.7 is the terminal producer-side wording), and
      the §11 checklist forbids producer-issued canon certification;
  §5  artifact payloads: a delivered glossary/lexicon term resolves to an
      `etymology` per `corpus/knowledge/synthesis/glossary-registry-format.md`
      §2 (status, source references, link chain), whose status vocabulary
      §4 licenses as attested / reconstructed / constructed / contested /
      unknown — explicit unknowns are valid, unsupported derivations are not.

The gate is read-only: it never edits a packet and never writes to the
corpus. It judges the packet document, not the truth of its contents; every
field is required content, so a field that is present but blank or carries
only a placeholder counts as absent evidence, not as compliance.

Interface
---------
    python3 tools/gates/handoff-packet-check.py <packet.md>
    python3 tools/gates/handoff-packet-check.py -            # packet on stdin
    python3 tools/gates/handoff-packet-check.py --selftest

Output — one line each on stdout:

  FINDING <id>: <level> — <message>     level in FAIL / REVIEW / HOLD
  INFO glossary-external: <ref>: <reason>
  INFO scan: fields=<n>/16 glossary-entries=<n> findings=<n>

Exit codes: 0 clean; 1 at least one finding (review-level included);
2 could-not-evaluate (not a Markdown document, unreadable, not UTF-8,
HO-DATA, or an argparse usage error). `--selftest` exits 0 when the
fixture pair and the controls behave and 1 when they do not.

Finding IDs (contract / profile citation)
-----------------------------------------
  HO-DATA          HOLD, exit 2  input is not a Markdown document (no
                    level-1 heading) — nothing else can be evaluated
  HO-MISSING       FAIL  a required §4 field/section is absent (one finding
                    per field, so the count is the missing-field count)
  HO-EMPTY         FAIL  a required field is present but blank/placeholder
  HO-BASELINE      REVIEW §4: `baseline_bible_ref: none` allowed only for a
                    deliberately unbound research packet
  HO-CONTRACT-REF  REVIEW §4/§1: `contract_ref` names no revision or no
                    digest (both lanes pin the digest before transfer)
  HO-MANIFEST-DIGEST REVIEW §4: `artifact_manifest` identifies no delivered
                    bytes (no file digest)
  HO-DEP-FLOAT     REVIEW §4: `dependency_manifest` floats `latest`
  HO-CANON-MARKER  FAIL  no `not canonized` / `not yet canonized` marker
                    (§6 canon standing; §8.7)
  HO-CANON-CLAIM   FAIL  a producer-side canon certification appears
                    (§11 checklist: "no producer-issued canon certification")
  HO-GLOSS-ETYM    FAIL  a delivered glossary entry carries no etymology
                    text, or its stated status is outside the §4 vocabulary
                    (glossary-registry-format.md §§2, 4); a table with no
                    `etymology` column fails once per table

Field recognition: a required field counts as supplied when its name
appears as a `## field` section heading, as a `- field: value` list item
(also `*`/`+`, sibling fields may share a row or item as `a, b`), or as
the first cell of a Markdown table row (`| field | value |`, backticks
stripped). A heading's value is its body up to the next heading; a list
item's empty value continues on indented following lines. First
non-placeholder occurrence wins. Known limit, stated rather than guessed:
a packet that quotes the specification table as documentation without
supplying its own data cannot be told apart from a filled packet; the
committed fixture shows the expected shape.

Scope that stays outside this kernel: judging whether the declared checks
were really run, whether digests match bytes, whether subject references
resolve to lore entities, and whether the payload content is any good.
Those are lore's receipt review (§8.5) and the domain gates' work. The
kernel checks the envelope, the non-canon marker, and the glossary
etymology presence/vocabulary the contract and the local entry profile
require.

Glossary-payload recognition: an explicit table counts as a glossary
payload when its header carries an entry-id column (`entry_id`,
`lexeme_id`, `sense_id`, `form_id`, `entry`, `term`, `id`) plus a
`gloss`/`meaning`/`form`/`lemma`/`definition` or `etymology` column;
artifact-manifest tables (`artifact_id`) are never read as glossary
payloads. Glossary bytes delivered only as external files get an INFO
line rather than a verdict — the gate does not open files it was not
given.

`--selftest` reads the committed pair
`tools/gates/fixtures/handoff-packet-check.md` (a packet with planted
defects) and `.expected` (one ID per line), asserts exit 1 with exactly
those IDs and counts, then runs a clean control packet plus one probe for
each check the fixture does not plant, malformed inputs, the grouped-row
and heading field forms, and a subprocess run from a different working
directory.
"""

import argparse
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

EXIT_CLEAN = 0
EXIT_FINDINGS = 1
EXIT_UNEVALUATED = 2

# The §4 envelope table names these 16 fields; each is required content.
FIELD_NAMES = (
    "packet_id",
    "packet_version",
    "contract_ref",
    "producer",
    "recipient",
    "request_ref",
    "baseline_bible_ref",
    "artifact_manifest",
    "subject_refs",
    "scope",
    "dependency_manifest",
    "claim_ledger",
    "coupling_edges",
    "requested_decisions",
    "validation",
    "open_questions",
)

# Values that mean "no evidence supplied". `none` is deliberately absent:
# §4 accepts `none` for baseline_bible_ref (routed to HO-BASELINE), and an
# explicit "no open questions" is content.
PLACEHOLDERS = {
    "",
    "-",
    "--",
    "—",
    "–",
    "n/a",
    "na",
    "n.a.",
    "tbd",
    "t.b.d.",
    "todo",
    "unknown",
    "(to-verify)",
    "to-verify",
    "?",
}

# §4: "file digests" / §1: the pinned digest. Hex-anchored so the word
# "digest" alone is not mistaken for a delivered digest.
DIGEST_RE = re.compile(
    r"(?i)(?:sha-?256|sha-?1|digest)\s*[:=]?\s*[0-9a-f]{8,}\b"
    r"|\b[0-9a-f]{32,}\b"
)
REVISION_RE = re.compile(r"\b\d+\.\d+\.\d+\b")

# §6 canon standing: "otherwise `not canonized`"; §8.7: "not yet canonized".
CANON_MARKER_RE = re.compile(r"(?i)\bnot[-\s]+(?:yet[-\s]+)?canon(?:ized)?\b")

# glossary-registry-format.md §4 licenses exactly these status values.
ETYM_STATUSES = ("attested", "reconstructed", "constructed", "contested", "unknown")

GLOSSARY_ID_HEADERS = ("entry_id", "lexeme_id", "sense_id", "form_id", "entry", "term", "id")
GLOSSARY_CONTENT_HEADERS = ("gloss", "meaning", "form", "lemma", "definition")


def _finding(fid, level, message):
    return {"id": fid, "level": level, "message": message}


def format_finding(finding):
    return f"FINDING {finding['id']}: {finding['level']} — {finding['message']}"


# --------------------------------------------------------------------------
# Markdown structure
# --------------------------------------------------------------------------


def _norm_cell(text):
    return text.strip().strip("`*").strip()


def _is_placeholder(value):
    return _norm_cell(value).lower() in PLACEHOLDERS


def _mentions(text, name):
    return re.search(
        rf"(?<![0-9A-Za-z_]){re.escape(name)}(?![0-9A-Za-z_])", text
    ) is not None


def _is_separator(line):
    stripped = line.strip()
    if not stripped.startswith("|"):
        return False
    inner = stripped.replace("|", "").strip()
    return bool(inner) and "-" in inner and all(ch in "-: " for ch in inner)


def _split_row(line):
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def parse_tables(lines):
    """Return every GFM table as {start, header, rows}; escaped pipes unsupported."""
    tables = []
    index = 0
    while index < len(lines):
        if lines[index].lstrip().startswith("|") and index + 1 < len(lines) and _is_separator(lines[index + 1]):
            header = _split_row(lines[index])
            rows = []
            cursor = index + 2
            while cursor < len(lines) and lines[cursor].lstrip().startswith("|"):
                rows.append(_split_row(lines[cursor]))
                cursor += 1
            tables.append({"start": index, "header": header, "rows": rows})
            index = cursor
        else:
            index += 1
    return tables


def _resolve_names(key):
    """Split a heading/list/table key into required field names, if it names any."""
    normalized = _norm_cell(key)
    tokens = [_norm_cell(token) for token in re.split(r"[,;/]", normalized) if _norm_cell(token)]
    if tokens and all(token in FIELD_NAMES for token in tokens):
        return tokens
    if normalized in FIELD_NAMES:
        return [normalized]
    return []


def _section_body(lines, heading_index):
    body = []
    for line in lines[heading_index + 1:]:
        if re.match(r"^\s{0,3}#{1,6}\s+\S", line):
            break
        body.append(line)
    return "\n".join(body).strip()


def _item_continuation(lines, index):
    body = []
    for line in lines[index + 1:]:
        if not line.strip():
            break
        if re.match(r"^\s{0,3}[-*+]\s+\S", line) or not re.match(r"^\s", line):
            break
        body.append(line.strip())
    return "\n".join(body).strip()


def collect_fields(lines, tables):
    """Map required field name -> {"value", "where"}; first occurrence wins."""
    candidates = {name: [] for name in FIELD_NAMES}

    for index, line in enumerate(lines):
        heading = re.match(r"^\s{0,3}(#{1,6})\s+(.*?)\s*$", line)
        if heading:
            names = [name for name in FIELD_NAMES if _mentions(heading.group(2), name)]
            if names:
                body = _section_body(lines, index)
                for name in names:
                    candidates[name].append({"value": body, "where": f"section heading line {index + 1}"})
            continue
        item = re.match(r"^\s{0,3}[-*+]\s+(.*)$", line)
        if item:
            list_key = r"`?\s*[A-Za-z][A-Za-z0-9_]*(?:\s*[,;/]\s*`?\s*[A-Za-z][A-Za-z0-9_]*)*`?"
            pair = re.match(rf"^({list_key})\s*[:=]\s*(.*)$", item.group(1))
            if pair:
                names = _resolve_names(pair.group(1))
                if names:
                    value = pair.group(2).strip() or _item_continuation(lines, index)
                    for name in names:
                        candidates[name].append({"value": value, "where": f"list item line {index + 1}"})

    for table in tables:
        for row in table["rows"]:
            if len(row) < 2:
                continue
            names = _resolve_names(row[0])
            if names:
                value = " | ".join(cell.strip() for cell in row[1:] if cell.strip())
                for name in names:
                    candidates[name].append({"value": value, "where": f"table row line {table['start'] + 2 + table['rows'].index(row) + 1}"})

    fields = {}
    for name, entries in candidates.items():
        if not entries:
            continue
        chosen = next((entry for entry in entries if not _is_placeholder(entry["value"])), entries[0])
        fields[name] = chosen
    return fields


# --------------------------------------------------------------------------
# canon standing (§6, §8.7, §11 checklist)
# --------------------------------------------------------------------------

_CANON_AFFIRM = re.compile(r"(?i)\b(canoniz\w*|canonical|canon|approved|established|ratified|final|granted)\b")
_CANON_NEGATED = re.compile(r"(?i)\b(not|no|non|never|without|denied)\b")
_CANON_PENDING = re.compile(
    r"(?i)\b(pending|await\w*|require\w*|request\w*|review\w*|propos\w*|will|would|may|might|to be|future|once|after|if|when)\b"
)


def _affirmative(fragment):
    return bool(_CANON_AFFIRM.search(fragment)) and not _CANON_NEGATED.search(fragment) and not _CANON_PENDING.search(fragment)


def canon_claims(lines):
    """Lines that issue or assert a producer-side canon standing, one per line."""
    hits = []
    for index, line in enumerate(lines):
        spans = []
        standing = re.search(r"(?im)^\s*(?:[-*+]\s*)?(?:\|\s*)?\bcanon[_ -]?(?:standing|status)\b\s*(?:[:=]\s*|\|\s*)([^\n]*)", line)
        if standing and _affirmative(standing.group(1)):
            spans.append(standing.group(0).strip())
        for match in re.finditer(r"(?i)\b(certif\w*|establish\w*|grant\w*|award\w*)\b[^.\n|]{0,80}?\bcanon(?:iz\w*|ical)?\b", line):
            if _affirmative(match.group(0)):
                spans.append(match.group(0).strip())
        for match in re.finditer(
            r"(?i)\bthis\s+(?:packet|handoff|delivery|document|release|manifest)\b[^.\n|]{0,40}?\b(?:is|becomes|constitutes|counts as)\b[^.\n|]{0,40}?\bcanon(?:iz\w*|ical)?\b",
            line,
        ):
            if _affirmative(match.group(0)):
                spans.append(match.group(0).strip())
        for match in re.finditer(r"(?i)\bcanoniz\w*\s+(?:by|in)\s+(?:lore|the\s+world[- ]bible)\b", line):
            prefix = line[max(0, match.start() - 40):match.start()]
            if _affirmative(match.group(0)) and not _CANON_NEGATED.search(prefix) and not _CANON_PENDING.search(prefix):
                spans.append(match.group(0).strip())
        if spans:
            hits.append((index + 1, spans[0]))
    return hits


# --------------------------------------------------------------------------
# glossary payloads (glossary-registry-format.md §§2, 4)
# --------------------------------------------------------------------------


def _is_glossary_table(table):
    header = [_norm_cell(cell).lower() for cell in table["header"]]
    if "artifact_id" in header:
        return False
    has_id = any(cell in GLOSSARY_ID_HEADERS for cell in header)
    has_content = any(cell in GLOSSARY_CONTENT_HEADERS for cell in header) or any(
        cell.startswith("etymology") for cell in header
    )
    return has_id and has_content


def _etymology_column(header):
    for index, cell in enumerate(header):
        if _norm_cell(cell).lower().startswith("etymology"):
            return index
    return None


def _entry_id(row, header):
    for index, cell in enumerate(header):
        if _norm_cell(cell).lower() in GLOSSARY_ID_HEADERS:
            return _norm_cell(row[index]) if index < len(row) else "?"
    return _norm_cell(row[0]) if row else "?"


def check_glossary(tables):
    """Per-entry etymology findings; returns (findings, entry count)."""
    findings = []
    entries = 0
    for table in tables:
        if not _is_glossary_table(table):
            continue
        header = table["header"]
        etym_column = _etymology_column(header)
        if etym_column is None:
            findings.append(
                _finding(
                    "HO-GLOSS-ETYM",
                    "FAIL",
                    f"glossary table at line {table['start'] + 1} has no `etymology` column "
                    f"({len(table['rows'])} entries): glossary-registry-format.md §2 requires the "
                    "etymology field group (status, source references, link chain)",
                )
            )
            entries += len(table["rows"])
            continue
        for row in table["rows"]:
            entries += 1
            entry_id = _entry_id(row, header)
            cell = row[etym_column] if etym_column < len(row) else ""
            if _is_placeholder(cell):
                findings.append(
                    _finding(
                        "HO-GLOSS-ETYM",
                        "FAIL",
                        f"glossary entry {entry_id} carries no etymology text; an explicit "
                        f"`unknown` with a reason is valid, an empty cell is not (glossary-registry-format.md §4)",
                    )
                )
                continue
            named = re.search(r"(?i)\bstatus\s*[:=]\s*[`*]?([A-Za-z_-]+)", cell)
            if named:
                token = named.group(1).lower()
                if token not in ETYM_STATUSES:
                    findings.append(
                        _finding(
                            "HO-GLOSS-ETYM",
                            "FAIL",
                            f"glossary entry {entry_id} states etymology status {token!r}, outside the "
                            f"licensed vocabulary {', '.join(ETYM_STATUSES)} (glossary-registry-format.md §4)",
                        )
                    )
            elif not any(re.search(rf"(?i)\b{status}\b", cell) for status in ETYM_STATUSES):
                findings.append(
                    _finding(
                        "HO-GLOSS-ETYM",
                        "FAIL",
                        f"glossary entry {entry_id} names no etymology status from "
                        f"{{{'/'.join(ETYM_STATUSES)}}} (glossary-registry-format.md §§2, 4)",
                    )
                )
    return findings, entries


def _glossary_manifest_refs(value):
    """Artifact refs in the manifest that name a glossary payload."""
    refs = []
    for line in value.splitlines():
        if "glossary" not in line.lower():
            continue
        if "|" in line:
            cells = [cell.strip() for cell in _split_row(line)]
            ref = " ".join(cell for cell in cells[:3] if cell) if cells else line.strip()
        else:
            ref = line.strip()
        ref = _norm_cell(ref)
        if ref and "inline" not in ref.lower() and ref not in refs:
            refs.append(ref)
    return refs


# --------------------------------------------------------------------------
# kernel
# --------------------------------------------------------------------------


def evaluate_text(text):
    """Return (exit code, findings, infos) for one packet document (no I/O)."""
    findings = []
    infos = []
    lines = text.splitlines()

    if not any(re.match(r"^\s{0,3}#\s+\S", line) for line in lines):
        return EXIT_UNEVALUATED, [
            _finding("HO-DATA", "HOLD", "input could not be evaluated: no Markdown level-1 heading — not a packet document")
        ], infos

    tables = parse_tables(lines)
    fields = collect_fields(lines, tables)

    supplied = 0
    for name in FIELD_NAMES:
        entry = fields.get(name)
        if entry is None:
            findings.append(
                _finding(
                    "HO-MISSING",
                    "FAIL",
                    f"required field/section `{name}` absent — the contract §4 handoff envelope names it, "
                    "and a required field is not satisfied by silence",
                )
            )
        elif _is_placeholder(entry["value"]):
            findings.append(
                _finding(
                    "HO-EMPTY",
                    "FAIL",
                    f"required field `{name}` is present at {entry['where']} but carries only a "
                    "blank/placeholder value (contract §4 required content; §11: unknowns are not blank cells)",
                )
            )
        else:
            supplied += 1

    baseline = fields.get("baseline_bible_ref")
    if baseline and _norm_cell(baseline["value"]).lower() == "none":
        # §4: "`none` only for a deliberately unbound research packet" — the
        # declaration is read on one line, or inside the baseline value itself.
        unbound = re.search(r"(?i)\bunbound\b[^.\n]{0,60}\bresearch\b|\bresearch\b[^.\n]{0,60}\bunbound\b", text) or re.search(r"(?i)\bunbound\b", baseline["value"])
        if not unbound:
            findings.append(
                _finding(
                    "HO-BASELINE",
                    "REVIEW",
                    "`baseline_bible_ref: none` without a deliberate unbound-research declaration — "
                    "§4 allows `none` only for a deliberately unbound research packet, which cannot be "
                    "imported as canon without a lore baseline and a new reviewed handoff",
                )
            )

    contract_ref = fields.get("contract_ref")
    if contract_ref and not _is_placeholder(contract_ref["value"]):
        value = contract_ref["value"]
        missing = [part for part, present in (("revision", REVISION_RE.search(value)), ("digest", DIGEST_RE.search(value))) if not present]
        if missing:
            findings.append(
                _finding(
                    "HO-CONTRACT-REF",
                    "REVIEW",
                    f"`contract_ref` names no {' or no '.join(missing)} — §4 requires contract ID, revision "
                    "and digest acknowledged by both lanes; §1 pins the digest before a transfer",
                )
            )

    manifest = fields.get("artifact_manifest")
    if manifest and not _is_placeholder(manifest["value"]):
        if not DIGEST_RE.search(manifest["value"]):
            findings.append(
                _finding(
                    "HO-MANIFEST-DIGEST",
                    "REVIEW",
                    "`artifact_manifest` names no file digest — §4 requires artifact IDs, record IDs, "
                    "paths/sections, versions, file digests and record counts; identify the exact delivered bytes",
                )
            )

    dependencies = fields.get("dependency_manifest")
    if dependencies and not _is_placeholder(dependencies["value"]):
        value = dependencies["value"]
        if re.search(r"(?i)\blatest\b", value) and not re.search(r"(?i)\b(no|not|never)\b[^.\n]{0,30}\blatest\b", value):
            findings.append(
                _finding(
                    "HO-DEP-FLOAT",
                    "REVIEW",
                    "`dependency_manifest` floats `latest` — §4 requires exact system/rule/lexicon versions "
                    "and no floating `latest`",
                )
            )

    if not CANON_MARKER_RE.search(text):
        findings.append(
            _finding(
                "HO-CANON-MARKER",
                "FAIL",
                "no non-canon marker: the packet must carry `not canonized` (or `not yet canonized`) — "
                "§6 leaves canon standing to lore, and §8.7 makes that the terminal producer-side wording",
            )
        )
    for line_number, span in canon_claims(lines):
        findings.append(
            _finding(
                "HO-CANON-CLAIM",
                "FAIL",
                f"producer-side canon certification at line {line_number}: {span!r} — the §11 checklist "
                "forbids producer-issued canon certification; canon standing is a lore decision (§6)",
            )
        )

    glossary_findings, entries = check_glossary(tables)
    findings.extend(glossary_findings)

    if manifest and not _is_placeholder(manifest["value"]):
        for ref in _glossary_manifest_refs(manifest["value"]):
            infos.append(
                f"INFO glossary-external: {ref}: entries not inline — the etymology profile "
                "(glossary-registry-format.md §§2, 4) is not checkable from the packet body"
            )

    infos.append(f"INFO scan: fields={supplied}/{len(FIELD_NAMES)} glossary-entries={entries} findings={len(findings)}")
    return (EXIT_CLEAN if not findings else EXIT_FINDINGS), findings, infos


# --------------------------------------------------------------------------
# selftest
# --------------------------------------------------------------------------

FIXTURE_EXPECTED = Counter(
    {
        "HO-MISSING": 2,
        "HO-EMPTY": 1,
        "HO-BASELINE": 1,
        "HO-CONTRACT-REF": 1,
        "HO-MANIFEST-DIGEST": 1,
        "HO-DEP-FLOAT": 1,
        "HO-CANON-MARKER": 1,
        "HO-CANON-CLAIM": 1,
        "HO-GLOSS-ETYM": 2,
    }
)

CONTROL_PACKET = """# Handoff packet — F-toy control (fixture; not canonized)

Synthetic control for tools/gates/handoff-packet-check.py. It asserts no
world fact and claims no canon standing; lore-shokunin owns canon.

| field | value |
|---|---|
| packet_id | KTD-HO-CONTROL-0001 |
| packet_version | 1.0.0 |
| producer | kotodama-shokunin |
| recipient | lore-shokunin |
| request_ref | brief F-T02 (synthetic; illustrative only) |
| baseline_bible_ref | lore-bible rev-7 digest sha256:1111111111111111111111111111111111111111111111111111111111111111 |
| subject_refs | ktd:candidate:f-toy/people (namespaced candidates; unresolved — no lore entity IDs supplied) |
| contract_ref | kotodama-lore-adjacency 1.0.0 sha256:0000000000000000000000000000000000000000000000000000000000000000 |

- canon_standing: not canonized — lore disposition required (lore-shokunin owns canon)

## artifact_manifest

| artifact_id | kind | path | version | digest | records |
|---|---|---|---|---|---|
| A1 | system-spec | packets/f-toy/system.md | 1.0.0 | sha256:2222222222222222222222222222222222222222222222222222222222222222 | 12 |
| A2 | glossary | inline §glossary payload | 1.0.0 | sha256:3333333333333333333333333333333333333333333333333333333333333333 | 2 |

## scope

| record_id | culture_group | region | variety | script | register | era |
|---|---|---|---|---|---|---|
| R1 | F-toy (fixture culture) | upland | coast variety | Latn | ritual | E1–E2 |

## dependency_manifest

- F-toy naming rules @1.0.0 (pinned)
- F-toy phonology profile @1.0.0 (pinned)

## claim_ledger

| record_id | kind | statement | provenance | evidence_status |
|---|---|---|---|---|
| C1 | generative rule | F-toy rule R1 (fixture rule) | rule R1 @1.0.0 | invented (toy language) |

## coupling_edges

| edge_id | source | target | relation | justification |
|---|---|---|---|---|
| E-1 | C1 | a fixture lexicon term | dependency | the derived form uses rule R1 @1.0.0 |

## requested_decisions

| record_id | question | alternatives | blocker |
|---|---|---|---|
| C1 | accept the fixture rule as a design input? | accept / defer / reject | none — fixture only |

## validation

| check | input | result |
|---|---|---|
| gate:phonology-sanity | F-toy profile @1.0.0 | exit 0 (fixture run) |

## open_questions

- One non-blocking question: unresolved entity IDs for R1 (responsible lane: lore).

## glossary payload (F-toy fixture entries; inline, artifact A2)

| entry_id | form | gloss | etymology |
|---|---|---|---|
| GE-01 | talin | 'song-line' (fixture) | status: constructed (toy formation; no real-world claim) |
| GE-02 | musa | 'spring (season)' (fixture) | status: unknown (no in-world account drafted yet) |
"""


def selftest():
    here = Path(__file__).resolve().parent
    fixture_path = here / "fixtures" / "handoff-packet-check.md"
    expected_path = here / "fixtures" / "handoff-packet-check.expected"

    text = fixture_path.read_text(encoding="utf-8")
    code, findings, infos = evaluate_text(text)
    got = Counter(finding["id"] for finding in findings)
    expected_ids = [line.strip() for line in expected_path.read_text(encoding="utf-8").splitlines() if line.strip()]

    assert code == EXIT_FINDINGS, f"fixture must exit 1, got {code}: {[format_finding(f) for f in findings]}"
    assert set(expected_ids) == set(got), f"expected-file ids {sorted(set(expected_ids))} != emitted ids {sorted(got)}"
    assert set(FIXTURE_EXPECTED) == set(expected_ids), (
        "in-code expected counts and the committed .expected file disagree"
    )
    assert got == FIXTURE_EXPECTED, f"fixture finding counts changed: {dict(got)}"

    # The planted defects must name the right witness.
    missing_messages = [f["message"] for f in findings if f["id"] == "HO-MISSING"]
    assert len(missing_messages) == 2, missing_messages
    assert any("`validation`" in m for m in missing_messages), missing_messages
    assert any("`open_questions`" in m for m in missing_messages), missing_messages
    glossary_messages = [f["message"] for f in findings if f["id"] == "HO-GLOSS-ETYM"]
    assert len(glossary_messages) == 2, glossary_messages
    assert any("GE-02" in m for m in glossary_messages), glossary_messages
    assert any("GE-03" in m for m in glossary_messages), glossary_messages
    assert not any("GE-01" in m for m in glossary_messages), glossary_messages
    assert any(info.startswith("INFO glossary-external: A3") for info in infos), infos
    assert any("fields=13/16" in info for info in infos), infos

    # Clean control: every required field, pinned refs, non-canon marker,
    # inline glossary rows with licensed statuses.
    control_code, control_findings, control_infos = evaluate_text(CONTROL_PACKET)
    assert control_code == EXIT_CLEAN, [format_finding(f) for f in control_findings]
    assert control_findings == [], control_findings
    assert not any(info.startswith("INFO glossary-external") for info in control_infos), control_infos

    # A field supplied as a heading body is still recognized.
    heading_form = CONTROL_PACKET.replace(
        "| request_ref | brief F-T02 (synthetic; illustrative only) |\n",
        "",
    ) + "\n## request_ref\n\nbrief F-T02 (synthetic; heading form probe)\n"
    heading_code, heading_findings, _ = evaluate_text(heading_form)
    assert heading_code == EXIT_CLEAN, [format_finding(f) for f in heading_findings]

    # A table row may group the field names exactly as the §4 table does.
    grouped_row = CONTROL_PACKET.replace(
        "| packet_id | KTD-HO-CONTROL-0001 |\n| packet_version | 1.0.0 |\n",
        "| `packet_id`, `packet_version` | KTD-HO-CONTROL-0001 @ 1.0.0 |\n",
    )
    grouped_code, grouped_findings, _ = evaluate_text(grouped_row)
    assert grouped_code == EXIT_CLEAN, [format_finding(f) for f in grouped_findings]

    # Canon probes: certification is a finding; removing the marker is a finding.
    claim_probe = CONTROL_PACKET + "\n| canon_standing | canonized — producer certification (probe) |\n"
    claim_code, claim_findings, _ = evaluate_text(claim_probe)
    claim_ids = {f["id"] for f in claim_findings}
    assert claim_code == EXIT_FINDINGS and "HO-CANON-CLAIM" in claim_ids, claim_ids
    assert "HO-CANON-MARKER" not in claim_ids, claim_ids
    marker_probe = CONTROL_PACKET.replace("not canonized", "kept as a working record")
    marker_code, marker_findings, _ = evaluate_text(marker_probe)
    assert marker_code == EXIT_FINDINGS and {f["id"] for f in marker_findings} == {"HO-CANON-MARKER"}, marker_findings

    # Future-tense canon language is process description, not certification.
    future_probe = CONTROL_PACKET.replace(
        "- canon_standing: not canonized — lore disposition required (lore-shokunin owns canon)",
        "- canon_standing: will be canonized by lore after approval (probe)",
    )
    future_code, future_findings, _ = evaluate_text(future_probe)
    assert future_code == EXIT_CLEAN, [format_finding(f) for f in future_findings]

    # Baseline probes: `none` needs the unbound declaration.
    baseline_probe = CONTROL_PACKET.replace(
        "| baseline_bible_ref | lore-bible rev-7 digest sha256:1111111111111111111111111111111111111111111111111111111111111111 |",
        "| baseline_bible_ref | none |",
    )
    baseline_code, baseline_findings, _ = evaluate_text(baseline_probe)
    assert baseline_code == EXIT_FINDINGS and {f["id"] for f in baseline_findings} == {"HO-BASELINE"}, baseline_findings
    unbound_probe = baseline_probe.replace(
        "# Handoff packet — F-toy control (fixture; not canonized)",
        "# Handoff packet — F-toy control (deliberately unbound research packet; not canonized)",
    )
    unbound_code, unbound_findings, _ = evaluate_text(unbound_probe)
    assert unbound_code == EXIT_CLEAN, [format_finding(f) for f in unbound_findings]

    # Dependency probe: floating `latest`, and the "no floating latest" wording
    # that documents the rule instead of breaking it.
    float_probe = CONTROL_PACKET.replace("F-toy phonology profile @1.0.0 (pinned)", "F-toy phonology profile latest")
    float_code, float_findings, _ = evaluate_text(float_probe)
    assert float_code == EXIT_FINDINGS and {f["id"] for f in float_findings} == {"HO-DEP-FLOAT"}, float_findings
    documented_probe = CONTROL_PACKET.replace(
        "F-toy phonology profile @1.0.0 (pinned)",
        "F-toy phonology profile @1.0.0 (no floating latest references)",
    )
    documented_code, documented_findings, _ = evaluate_text(documented_probe)
    assert documented_code == EXIT_CLEAN, [format_finding(f) for f in documented_findings]

    # §1/§4 contract_ref: revision and digest are both required.
    ref_probe = CONTROL_PACKET.replace(
        "kotodama-lore-adjacency 1.0.0 sha256:0000000000000000000000000000000000000000000000000000000000000000",
        "kotodama-lore-adjacency",
    )
    ref_code, ref_findings, _ = evaluate_text(ref_probe)
    assert ref_code == EXIT_FINDINGS and {f["id"] for f in ref_findings} == {"HO-CONTRACT-REF"}, ref_findings

    # Glossary probes: an unlicensed status, a missing status, and the
    # licensed `unknown` escape hatch.
    status_probe = CONTROL_PACKET.replace(
        "status: unknown (no in-world account drafted yet)",
        "status: plausible (probe)",
    )
    status_code, status_findings, _ = evaluate_text(status_probe)
    assert status_code == EXIT_FINDINGS and {f["id"] for f in status_findings} == {"HO-GLOSS-ETYM"}, status_findings
    bare_probe = CONTROL_PACKET.replace(
        "status: unknown (no in-world account drafted yet)",
        "descended from a proto-form (probe)",
    )
    bare_code, bare_findings, _ = evaluate_text(bare_probe)
    assert bare_code == EXIT_FINDINGS and {f["id"] for f in bare_findings} == {"HO-GLOSS-ETYM"}, bare_findings
    unknown_probe = CONTROL_PACKET.replace(
        "status: unknown (no in-world account drafted yet)",
        "descended from a proto-form; unknown (probe)",
    )
    unknown_code, unknown_findings, _ = evaluate_text(unknown_probe)
    assert unknown_code == EXIT_CLEAN, [format_finding(f) for f in unknown_findings]
    external_probe = CONTROL_PACKET.replace(
        "| A2 | glossary | inline §glossary payload |",
        "| A2 | glossary | packets/f-toy/glossary.md |",
    )
    external_code, external_findings, external_infos = evaluate_text(external_probe)
    assert external_code == EXIT_CLEAN, [format_finding(f) for f in external_findings]
    assert any(info.startswith("INFO glossary-external: A2") for info in external_infos), external_infos

    # Malformed input -> exit 2; a heading with no fields -> missing findings, not a crash.
    prose_code, prose_findings, _ = evaluate_text("plain prose, no heading at all\n")
    assert prose_code == EXIT_UNEVALUATED and prose_findings[0]["id"] == "HO-DATA", prose_findings
    empty_code, empty_findings, _ = evaluate_text("")
    assert empty_code == EXIT_UNEVALUATED and empty_findings[0]["id"] == "HO-DATA", empty_findings
    bare_heading_code, bare_heading_findings, _ = evaluate_text("# Handoff packet\n")
    assert bare_heading_code == EXIT_FINDINGS, bare_heading_findings
    assert sum(1 for f in bare_heading_findings if f["id"] == "HO-MISSING") == len(FIELD_NAMES), bare_heading_findings

    # CLI: fixture exits 1, control exits 0, from a directory that is not the gate's.
    with tempfile.TemporaryDirectory() as tmp:
        control_path = Path(tmp) / "control.md"
        control_path.write_text(CONTROL_PACKET, encoding="utf-8")
        gate = str(Path(__file__).resolve())
        fixture_run = subprocess.run(
            [sys.executable, gate, str(fixture_path)], capture_output=True, text=True, cwd=tmp
        )
        assert fixture_run.returncode == EXIT_FINDINGS, (fixture_run.returncode, fixture_run.stdout)
        control_run = subprocess.run(
            [sys.executable, gate, str(control_path)], capture_output=True, text=True, cwd=tmp
        )
        assert control_run.returncode == EXIT_CLEAN, (control_run.returncode, control_run.stdout, control_run.stderr)
        stdin_run = subprocess.run(
            [sys.executable, gate, "-"], input=CONTROL_PACKET, capture_output=True, text=True, cwd=tmp
        )
        assert stdin_run.returncode == EXIT_CLEAN, (stdin_run.returncode, stdin_run.stderr)
        missing_run = subprocess.run(
            [sys.executable, gate, str(Path(tmp) / "absent.md")], capture_output=True, text=True, cwd=tmp
        )
        assert missing_run.returncode == EXIT_UNEVALUATED, (missing_run.returncode, missing_run.stdout)

    print(
        f"selftest: OK — fixture findings {sum(got.values())} across {len(got)} ids "
        f"({', '.join(sorted(got))}); clean control exit 0; probes cover canon, baseline, dependency, "
        "contract_ref and glossary vocabulary; malformed inputs exit 2; CLI verified from another cwd"
    )
    return EXIT_CLEAN


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="handoff-packet-check.py",
        description="Validate a kotodama handoff packet against the worldbible integration contract (§4 envelope, §6 canon standing, glossary etymologies).",
    )
    parser.add_argument("packet", nargs="?", help="packet Markdown file, or - for stdin")
    parser.add_argument("--selftest", action="store_true", help="run the committed fixture and controls")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()
    if not args.packet:
        parser.error("a packet path (or '-') is required unless --selftest is used")

    if args.packet == "-":
        text = sys.stdin.read()
    else:
        try:
            text = Path(args.packet).read_text(encoding="utf-8")
        except OSError as exc:
            print(format_finding(_finding("HO-DATA", "HOLD", f"input could not be evaluated: {exc}")))
            return EXIT_UNEVALUATED
        except UnicodeDecodeError as exc:
            print(format_finding(_finding("HO-DATA", "HOLD", f"input could not be evaluated: not UTF-8 text: {exc}")))
            return EXIT_UNEVALUATED

    code, findings, infos = evaluate_text(text)
    for finding in findings:
        print(format_finding(finding))
    for info in infos:
        print(info)
    return code


if __name__ == "__main__":
    sys.exit(main())