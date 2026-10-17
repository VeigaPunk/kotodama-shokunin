#!/usr/bin/env python3
"""exercise-handoff-e2e — kotodama-shokunin handoff-e2e exercise (R11-O02..O05).

Assembles a world-bible handoff packet **from the live D2 and D3 drill
artifacts** — no hand-written packet body, every field derived from bytes on
disk — copies the assembled packet into an isolated directory outside the
repository, and validates it there through `tools/gates/handoff-packet-check.py`
run from that foreign working directory. The exercise passes only when the gate
exits 0 with `fields=16/16 glossary-entries=20 findings=0` and when everything
the run observed equals the committed frozen baseline.

Implements `reports/round-11/handoff/design.md` (R11-O01): its §2 read set, §3
field map, §5 glossary rule, §6 cross-reference assertions, §8 baseline and
tamper controls, §9 control matrix and §10 CLI/exit-code surface.

Read set (21 files, design §2; digests measured live, never copied)

  corpus/knowledge/synthesis/worldbible-integration-contract.md   §1/§4 authority
  examples/culture-d3/{packet.json,packet.gates.yml,controls.json,expected.json}
  examples/culture-d3/components/{04-language,05-ritual,06-material,07-evidence}.json
  examples/culture-d2/{packet.d2.yml,typed-labels.d2.yml}
  corpus/lessons/round-6-sources/{05,03,13,09}.json    closed S01–S05 bindings
  reports/round-6/parent-reconciliation.json          effective scope/kind authority
  tools/gates/handoff-packet-check.py                 this run's judge
  tools/{assemble-culture-d3,assemble-d2,d2-typed-labels,check-evidence-coupling}.py

  Deliberately excluded: `examples/culture-d3/handoff.md` and the directory
  `README.md` — documentation surfaces outside the D3 computational freeze,
  which currently carry stale digests (design §7). The exercise reads no prose
  packet; it re-renders one from the bytes above.

Two measured gaps the exercise closes on its own side (design §1)

  1. the gate counts glossary rows, it does not know how many there should be —
     the exercise asserts 20 rows with the live lexicon's id set and statuses;
  2. the gate checks digest *presence*, never digest *equality* — the exercise
     re-measures every digest it emits and asserts equality with the bytes.

Assertions the exercise runs (design §6)

  three-way field agreement (contract §4 table = gate FIELD_NAMES = supplied
  fields); contract digest equality; claim kinds drawn from contract §6;
  no unnegated version float; candidate refs stay namespaced and unresolved;
  every manifest digest equals the named file's measured bytes.

Interface

    python3 tools/exercise-handoff-e2e.py                 # assemble -> gate -> baseline
    python3 tools/exercise-handoff-e2e.py --selftest      # positive + control matrix
    python3 tools/exercise-handoff-e2e.py --root DIR      # alternate repo root
    python3 tools/exercise-handoff-e2e.py --baseline PATH # baseline override
    python3 tools/exercise-handoff-e2e.py --keep          # keep the isolated packet dir
    python3 tools/exercise-handoff-e2e.py --json          # receipt document on stdout
    python3 tools/exercise-handoff-e2e.py --freeze DIR    # (re)write a baseline, printing diffs

Exit codes (stable messages, no traceback): 0 clean; 1 mismatch — `E2E-DIGEST`,
`E2E-COUNT`, `E2E-GATE`, `E2E-SCAN`; 2 could-not-evaluate — `E2E-ARTIFACT`
(missing/unreadable read-set file), `E2E-BASELINE` (absent or edited baseline),
`E2E-DATA` (malformed input). Writes go only to a fresh directory under
`TMPDIR`; the read set is never modified, there is no network access, and the
tool is stdlib-only (the D2 packet is read as bytes with id-level regex
extraction, never through a third-party YAML loader; the JSON-formatted
`typed-labels.d2.yml` is loaded with `json`).
"""

import argparse
import datetime
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

EXIT_PASS = 0
EXIT_FAIL = 1
EXIT_UNEVALUATED = 2

ROOT = Path(__file__).resolve().parents[1]

PROFILE = "kotodama-handoff-e2e/1"
PACKET_ID = "kotodama.handoff.d2d3-e2e"
PACKET_VERSION = "1.0.0"
BASELINE_DEFAULT = "reports/round-11/handoff/expected.json"
FROZEN_DIR_DEFAULT = "reports/round-11/handoff"

CONTRACT = "corpus/knowledge/synthesis/worldbible-integration-contract.md"
D3_PACKET = "examples/culture-d3/packet.json"
D3_GATES = "examples/culture-d3/packet.gates.yml"
D3_CONTROLS = "examples/culture-d3/controls.json"
D3_EXPECTED = "examples/culture-d3/expected.json"
D3_COMPONENTS = (
    "examples/culture-d3/components/04-language.json",
    "examples/culture-d3/components/05-ritual.json",
    "examples/culture-d3/components/06-material.json",
    "examples/culture-d3/components/07-evidence.json",
)
D2_PACKET = "examples/culture-d2/packet.d2.yml"
D2_TYPED = "examples/culture-d2/typed-labels.d2.yml"
SOURCE_LEDGERS = (
    "corpus/lessons/round-6-sources/05.json",
    "corpus/lessons/round-6-sources/03.json",
    "corpus/lessons/round-6-sources/13.json",
    "corpus/lessons/round-6-sources/09.json",
)
RECONCILIATION = "reports/round-6/parent-reconciliation.json"
GATE = "tools/gates/handoff-packet-check.py"
TOOLS = (
    GATE,
    "tools/assemble-culture-d3.py",
    "tools/assemble-d2.py",
    "tools/d2-typed-labels.py",
    "tools/check-evidence-coupling.py",
)

READ_SET = (
    CONTRACT,
    D3_PACKET,
    D3_GATES,
    D3_CONTROLS,
    D3_EXPECTED,
    *D3_COMPONENTS,
    D2_PACKET,
    D2_TYPED,
    *SOURCE_LEDGERS,
    RECONCILIATION,
    *TOOLS,
)

# The §4 envelope table in the contract names these 16 fields; the exercise
# re-derives the set from the contract and from the gate's own tuple (§6.1).
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
SCALAR_FIELDS = (
    "packet_id",
    "packet_version",
    "contract_ref",
    "producer",
    "recipient",
    "request_ref",
    "baseline_bible_ref",
    "subject_refs",
    "scope",
)
SECTION_FIELDS = (
    "artifact_manifest",
    "dependency_manifest",
    "claim_ledger",
    "coupling_edges",
    "requested_decisions",
    "validation",
    "open_questions",
)

# Contract §6 claim kinds, plus the screening-statement note the design allows.
CLAIM_KINDS = (
    "real-world reference",
    "generative rule",
    "candidate world-fact",
    "attributed in-world belief",
    "designer interpretation",
    "screening statement",
)

PLACEHOLDERS = {
    "", "-", "--", "—", "–", "n/a", "na", "n.a.", "tbd", "t.b.d.", "todo",
    "unknown", "(to-verify)", "to-verify", "?",
}
ETYM_STATUSES = ("attested", "reconstructed", "constructed", "contested", "unknown")

DECLARED = {
    "expected_exit": EXIT_PASS,
    "expected_finding_ids": [],
    "expected_scan": {"fields": "16/16", "glossary_entries": 20, "findings": 0},
}
DECLARED_EXPECTATION = (
    "exit 0 / findings [] fixed before implementation; hashes measured from bytes, never generated "
    "from a printed verdict"
)
BASELINE_LIMITS = (
    "pins computational inputs only; not lore acceptance, not canon, not completion of the round arc; "
    "documentation surfaces excluded"
)

# Gate patterns, copied so the exercise can fail closed with its own message
# before the gate run (the gate stays the authoritative judge).
DIGEST_RE = re.compile(
    r"(?i)(?:sha-?256|sha-?1|digest)\s*[:=]?\s*[0-9a-f]{8,}\b|\b[0-9a-f]{32,}\b"
)
CANON_MARKER_RE = re.compile(r"(?i)\bnot[-\s]+(?:yet[-\s]+)?canon(?:ized)?\b")
CANON_TRAP_RES = (
    re.compile(r"(?i)\b(certif\w*|establish\w*|grant\w*|award\w*)\b[^.\n|]{0,80}?\bcanon(?:iz\w*|ical)?\b"),
    re.compile(
        r"(?i)\bthis\s+(?:packet|handoff|delivery|document|release|manifest)\b[^.\n|]{0,40}?"
        r"\b(?:is|becomes|constitutes|counts as)\b[^.\n|]{0,40}?\bcanon(?:iz\w*|ical)?\b"
    ),
    re.compile(r"(?i)\bcanoniz\w*\s+(?:by|in)\s+(?:lore|the\s+world[- ]bible)\b"),
)


class Unevaluatable(Exception):
    """Input cannot be evaluated: missing, unreadable, or structurally wrong."""

    code = "E2E-DATA"


class ArtifactError(Unevaluatable):
    code = "E2E-ARTIFACT"


class MissingArtifact(ArtifactError):
    pass


class BaselineError(Unevaluatable):
    code = "E2E-BASELINE"


class Failed(Exception):
    """The exercise ran and its verdict is negative."""

    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_text(text):
    return sha256_bytes(text.encode("utf-8"))


def read_text(root, rel):
    path = Path(root) / rel
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise MissingArtifact(f"read-set file unreadable: {rel} ({exc})") from exc
    except UnicodeDecodeError as exc:
        raise ArtifactError(f"read-set file is not UTF-8 text: {rel} ({exc})") from exc


def measure(root, rel):
    path = Path(root) / rel
    try:
        data = path.read_bytes()
    except OSError as exc:
        raise MissingArtifact(f"read-set file unreadable: {rel} ({exc})") from exc
    return sha256_bytes(data), len(data)


def norm_cell(value):
    return value.strip().strip("`*").strip()


def is_placeholder(value):
    return norm_cell(value).lower() in PLACEHOLDERS


def cell(text, limit=None):
    """Live free text as a table cell: no pipes, no newlines, word-boundary cut."""
    flat = re.sub(r"\s+", " ", str(text)).replace("|", "/").strip()
    if limit and len(flat) > limit:
        cut = flat[: limit - 1]
        space = cut.rfind(" ")
        flat = (cut[:space] if space > limit // 2 else cut).rstrip() + "…"
    return flat


def id_range(ids):
    """`A-01–A-09`, plus any id whose prefix differs from the first id's."""
    first, last = ids[0], ids[-1]
    prefix = first.rsplit("-", 1)[0] if "-" in first else first
    others = sorted({i for i in ids if (i.rsplit("-", 1)[0] if "-" in i else i) != prefix})
    text = f"{first}–{last}"
    if others:
        text += f" (plus {', '.join(others)})"
    return text


def json_file(root, rel):
    try:
        return json.loads(read_text(root, rel))
    except json.JSONDecodeError as exc:
        raise ArtifactError(f"{rel} is not valid JSON: {exc}") from exc


def section(text, name):
    """Top-level `name:` block of the D2 YAML subset — a block splitter, not a loader."""
    match = re.search(rf"^{name}:\n(.*?)(?=^[A-Za-z_][A-Za-z0-9_]*:\s*$|\Z)", text, re.M | re.S)
    if not match:
        raise ArtifactError(f"{D2_PACKET}: section `{name}` not found — the packet shape changed")
    return match.group(1)


def yaml_entry(text, block, entry_id):
    """Id-level extraction of one `- id: "X"` entry inside a D2 block."""
    match = re.search(rf'^\s*-\s*\n\s*id:\s*"{re.escape(entry_id)}"\n(.*?)(?=^\s*-\s*\n\s*id:|\Z)', block, re.M | re.S)
    if not match:
        raise ArtifactError(f"{D2_PACKET}: record {entry_id} not found in `{text}`")
    return dict(re.findall(r'^\s{4}([a-z_]+):\s*"([^"]*)"', match.group(1), re.M))


def top_level_keys(text):
    return re.findall(r"^([A-Za-z_][A-Za-z0-9_]*):", text, re.M)


# --------------------------------------------------------------------------
# mining the live inputs
# --------------------------------------------------------------------------


def mine_contract(root):
    text = read_text(root, CONTRACT)
    contract_id = re.search(r"Contract ID:\s*`([^`]+)`", text)
    revision = re.search(r"initial interface revision:\s*`([^`]+)`", text)
    if not contract_id or not revision:
        raise ArtifactError(f"{CONTRACT}: could not parse the contract ID / revision (§1)")
    names = set()
    for row in re.finditer(r"^\|\s*([^|]+?)\s*\|", text, re.M):
        tokens = [norm_cell(token) for token in row.group(1).split(",")]
        if tokens and all(re.fullmatch(r"[a-z_]+", token or "") for token in tokens):
            names.update(tokens)
    if len(names) != len(FIELD_NAMES):
        raise ArtifactError(
            f"{CONTRACT}: §4 field-table scan produced {len(names)} names, expected {len(FIELD_NAMES)}"
        )
    return {"id": contract_id.group(1), "revision": revision.group(1), "section4_names": names}


def gate_field_names(root):
    text = read_text(root, GATE)
    match = re.search(r"^FIELD_NAMES = \(\n(.*?)^\)", text, re.M | re.S)
    if not match:
        raise ArtifactError(f"{GATE}: could not read the FIELD_NAMES tuple")
    return tuple(re.findall(r'"([a-z_]+)"', match.group(1)))


def mine_d2(root):
    text = read_text(root, D2_PACKET)
    blocks = {name: section(text, name) for name in ("lexicon", "names", "pantheon", "costumes", "materials", "eras", "assembly", "era_records")}
    lexicon_ids = re.findall(r'^\s*id:\s*"(L-\d\d)"', blocks["lexicon"], re.M)
    name_ids = re.findall(r'^\s*id:\s*"(NM-\d\d)"', blocks["names"], re.M)
    pantheon_ids = re.findall(r'^\s*id:\s*"((?:PAN|NE)-\d\d)"', blocks["pantheon"], re.M)
    costume_ids = re.findall(r'^\s*id:\s*"(GAR-\d\d)"', blocks["costumes"], re.M)
    material_ids = re.findall(r'^\s*id:\s*"(CMAT-\d\d)"', blocks["materials"], re.M)
    eras = re.findall(r'^\s*-\s*"(E\d)"', blocks["eras"], re.M)
    for label, values in (
        ("lexicon_ids", lexicon_ids), ("name_ids", name_ids), ("pantheon_ids", pantheon_ids),
        ("costume_ids", costume_ids), ("material_ids", material_ids), ("eras", eras),
    ):
        if not values:
            raise ArtifactError(f"{D2_PACKET}: mined `{label}` is empty — refusing to emit a placeholder field")
    components = dict(re.findall(r'^\s{4}"([^"]+)":\s*"([0-9a-f]{64})"', blocks["assembly"], re.M))
    if not components:
        raise ArtifactError(f"{D2_PACKET}: no `assembly.source_sha256` component digests found")
    witnesses = {
        "culture": re.search(r'^name:\s*"([^"]*)"', text, re.M),
        "lineage": yaml_entry("lexicon", blocks["lexicon"], "L-04"),
        "sky_holder": yaml_entry("pantheon", blocks["pantheon"], "PAN-01"),
        "era": yaml_entry("era_records", blocks["era_records"], "ER-01"),
    }
    if not witnesses["culture"]:
        raise ArtifactError(f"{D2_PACKET}: no `name:` line found")
    return {
        "lexicon_ids": lexicon_ids,
        "name_ids": name_ids,
        "pantheon_ids": pantheon_ids,
        "costume_ids": costume_ids,
        "material_ids": material_ids,
        "eras": eras,
        "rule_ids": sorted(set(re.findall(r"\bM-\d\d\b", text))),
        "coupling_notes": len(re.findall(r"^\s*coupling_note:", text, re.M)),
        "to_verify_lines": sum(1 for line in text.splitlines() if "to-verify" in line),
        "components": components,
        "culture_name": witnesses["culture"].group(1),
        "witness_lineage": witnesses["lineage"],
        "witness_sky_holder": witnesses["sky_holder"],
        "witness_era": witnesses["era"],
    }


D3_REQUIRED = (
    "profile", "canon_status", "handoff_status", "lexicon", "names", "eras", "beliefs", "symbols",
    "costumes", "objects", "materials", "utterances", "bridges", "references", "rank_rules",
    "sound_changes", "speech_rules", "naming_rule", "screening", "scope_notes", "assembly",
)


def mine_d3(root):
    obj = json_file(root, D3_PACKET)
    missing = [key for key in D3_REQUIRED if key not in obj]
    if missing:
        raise ArtifactError(f"{D3_PACKET}: missing top-level keys {missing}")
    facts = {key: obj[key] for key in D3_REQUIRED}
    facts["components"] = dict(obj["assembly"].get("source_sha256", {}))
    if not facts["components"] or not facts["lexicon"] or not facts["bridges"]:
        raise ArtifactError(f"{D3_PACKET}: assembly digests, lexicon or bridges are empty")
    return facts


def mine_typed_labels(root):
    obj = json_file(root, D2_TYPED)
    missing = [key for key in ("coverage", "findings", "era_material_reconciliation", "assembly") if key not in obj]
    if missing:
        raise ArtifactError(f"{D2_TYPED}: missing top-level keys {missing}")
    coverage = obj["coverage"]
    reconciliation = obj["era_material_reconciliation"]
    return {
        "labels": coverage.get("typed_labels"),
        "by_kind": coverage.get("labels_by_kind", {}),
        "findings_total": coverage.get("findings_total"),
        "hold_or_fail": coverage.get("findings_hold_or_fail"),
        "unresolved_items": coverage.get("rank_rules_unresolved_items"),
        "quarantine": coverage.get("rank_quarantine_handles"),
        "conflicts": coverage.get("conflicts"),
        "reconciliations": coverage.get("reconciliation_records"),
        "mat_findings": (reconciliation.get("summary") or {}).get("findings"),
        "mat_codes": (reconciliation.get("summary") or {}).get("by_code", {}),
        "packet_sha256": (obj.get("assembly") or {}).get("packet_sha256"),
        "finding_rows": len(obj["findings"]) if isinstance(obj["findings"], list) else None,
    }


def component_counts(d3, d2):
    return {
        "d2": len(d2["components"]),
        "d3": len(d3["components"]),
    }


def verify_component_digests(root, d2, d3):
    checked = matched = 0
    for label, components in (("D2", d2["components"]), ("D3", d3["components"])):
        for rel, recorded in sorted(components.items()):
            checked += 1
            measured, _ = measure(root, rel)
            if measured == recorded:
                matched += 1
            else:
                raise Failed(
                    "E2E-DIGEST",
                    f"{label} component {rel}: the assembler recorded {recorded[:12]}… but the bytes "
                    f"measure {measured[:12]}…",
                )
    return checked, matched


# --------------------------------------------------------------------------
# packet assembly (design §3, §5)
# --------------------------------------------------------------------------


def derived_etymology(entry, sound_change):
    """Design §5 row rule: status, E0→E1 change note, availability era."""
    e0 = entry["forms"].get("E0") or entry["native_form"]
    e1 = entry["forms"].get("E1") or entry["native_form"]
    status = entry.get("status")
    if status not in ETYM_STATUSES:
        raise ArtifactError(f"{D3_PACKET}: lexeme {entry['id']} states status {status!r}, outside the licensed vocabulary")
    if e0 != e1:
        change = (
            f"changed by {sound_change['id']} initial /{sound_change['from']}/ > /{sound_change['to']}/ "
            f"({sound_change['register']} register)"
        )
    else:
        change = "unchanged into E1"
    return (
        f"status: {status} — E0 *{e0} → E1 {e1} ({change}); available_from {entry['available_from']}"
    )


def build_glossary(d3):
    lexicon = d3["lexicon"]
    expected = DECLARED["expected_scan"]["glossary_entries"]
    if len(lexicon) != expected:
        raise Failed(
            "E2E-COUNT",
            f"{D3_PACKET}: live lexicon holds {len(lexicon)} entries, the declared expectation is {expected}",
        )
    changes = [change for change in d3["sound_changes"] if change.get("register") == "ordinary"]
    if len(changes) != 1:
        raise ArtifactError(f"{D3_PACKET}: expected exactly one ordinary-register sound change, found {len(changes)}")
    rows, seen = [], set()
    for entry in lexicon:
        if entry["id"] in seen:
            raise ArtifactError(f"{D3_PACKET}: duplicate lexeme id {entry['id']}")
        seen.add(entry["id"])
        rows.append(
            (
                entry["id"],
                entry["forms"].get("E0") or entry["native_form"],
                entry["forms"].get("E1") or entry["native_form"],
                entry["gloss"],
                derived_etymology(entry, changes[0]),
            )
        )
    return rows


def manifest_rows(root, digests, sizes, d2, d3, typed, contract, d3_expected, d3_controls, glossary):
    """One row per read-set file (design §3 row 8, §5), each digest measured live."""
    recon = json_file(root, RECONCILIATION)
    controls = set(d3_controls) if isinstance(d3_controls, dict) else set()
    component_record_counts = {}
    for rel in D3_COMPONENTS:
        component_record_counts[rel] = json_file(root, rel)

    def comp_note(rel):
        obj = component_record_counts[rel]
        counts = []
        for key in ("lexicon", "names", "utterances", "beliefs", "symbols", "materials", "objects", "costumes", "eras", "references", "bridges", "rank_rules", "sound_changes"):
            value = obj.get(key)
            if isinstance(value, list) and value:
                counts.append(f"{len(value)} {key}")
        return "; ".join(counts) or f"{len(obj)} keys"

    by_rel = {
        CONTRACT: (
            f"pinned adjacency contract §1/§4 authority; interface revision {contract['revision']}; "
            f"{len(contract['section4_names'])} §4 field names parsed from it"
        ),
        D3_PACKET: (
            f"d3 evidence-coupling payload: {len(d3['lexicon'])} lexemes / {len(d3['names'])} names / "
            f"{len(d3['utterances'])} utterances / {len(d3['beliefs'])} beliefs / {len(d3['symbols'])} symbols / "
            f"{len(d3['materials'])} materials / {len(d3['objects'])} objects / {len(d3['costumes'])} costumes / "
            f"{len(d3['rank_rules'])} rank rule / {len(d3['references'])} references / {len(d3['bridges'])} bridges"
        ),
        D3_GATES: (
            f"d3 legacy projection: {len(top_level_keys(read_text(root, D3_GATES)))} top-level sections, "
            "constructed native forms only in the gate-facing slots"
        ),
        D3_CONTROLS: f"d3 guard control expectations: {len(controls)} control classes",
        D3_EXPECTED: (
            f"d3 freeze manifest: {len((d3_expected.get('manifest') or {}))} computational input hashes; "
            f"declared exit {d3_expected.get('expected_exit')}; handoff/README deliberately excluded"
        ),
        D2_PACKET: (
            f"d2 design drill (read-only input): {len(d2['lexicon_ids'])} lexicon / {len(d2['name_ids'])} names / "
            f"{len(d2['pantheon_ids'])} pantheon / {len(d2['costume_ids'])} costumes / {len(d2['material_ids'])} materials / "
            f"{len(d2['rule_ids'])} rule ids / {d2['coupling_notes']} coupling notes"
        ),
        D2_TYPED: (
            f"d2 typed-label channel: {typed['labels']} labels, {typed['findings_total']} findings, "
            f"{typed['unresolved_items']} unresolved rank items"
        ),
        RECONCILIATION: (
            f"effective round-6 scope/kind authority: {len(recon) if hasattr(recon, '__len__') else '?'} top-level keys"
        ),
        GATE: "this run's judge; the authoritative verdict authority for the assembled packet",
        "tools/assemble-culture-d3.py": "d3 assembler named by the packet's own assembly block",
        "tools/assemble-d2.py": "d2 assembler and yaml_lines serializer dependency (read-only)",
        "tools/d2-typed-labels.py": "d2 typed-label projection generator",
        "tools/check-evidence-coupling.py": "d3 evidence-coupling guard (read-only)",
        D3_COMPONENTS[0]: f"d3 component: {comp_note(D3_COMPONENTS[0])}",
        D3_COMPONENTS[1]: f"d3 component: {comp_note(D3_COMPONENTS[1])}",
        D3_COMPONENTS[2]: f"d3 component: {comp_note(D3_COMPONENTS[2])}",
        D3_COMPONENTS[3]: f"d3 component: {comp_note(D3_COMPONENTS[3])}",
    }
    for rel in SOURCE_LEDGERS:
        obj = json_file(root, rel)
        by_rel[rel] = f"closed round-6 source ledger: {len(obj)} top-level keys (read-only evidence binding)"

    rows = []
    for index, rel in enumerate(READ_SET, start=1):
        size = sizes[rel]
        role = by_rel.get(rel) or f"read-set input, {size:,} bytes (digest-pinned)"
        rows.append((f"A-{index:02d}", rel, role, digests[rel], f"{size:,} bytes"))
    packet_digest = digests[D3_PACKET]
    rows.append(
        (
            "A-GLOSS",
            "§glossary payload (inline, this packet)",
            "constructed lexemes re-rendered from the d3 packet's lexicon[] in source order; "
            "the payload's source bytes are the d3 packet named above",
            packet_digest,
            f"{len(glossary)} entries",
        )
    )
    return rows


def build_packet(root, d2, d3, typed, contract, digests, sizes, glossary, fields_supplied):
    d2_component_count = len(d2["components"])
    d3_component_count = len(d3["components"])
    rows = manifest_rows(root, digests, sizes, d2, d3, typed, contract, json_file(root, D3_EXPECTED), json_file(root, D3_CONTROLS), glossary)

    lines = []
    add = lines.append
    add(
        "# Handoff packet — D2/D3 dual-drill exercise "
        "(deliberately unbound research packet; not canonized)"
    )
    add("")
    add(
        "NON-CANON handoff packet, kotodama-shokunin → lore-shokunin, assembled by "
        "`tools/exercise-handoff-e2e.py` from the live lane artifacts named in §artifact_manifest: the D2 "
        "highland-pastoralist design drill and its typed-label projection, and the D3 source-bounded "
        "culture drill with its legacy gate projection. Every field below is derived from those files at "
        "assembly time; no prose about the two drills is hand-authored here. This is an operability "
        "exercise, not a delivery: no lore brief, no baseline bible and no receipt surface exist, and no "
        "canon standing is asserted here. Canon standing is lore's alone (contract §6, §8.7). All native "
        "spellings are constructed and unscreened ASCII lowercase; no real-language clearance, community "
        "consultation, or cultural permission is claimed, performed, or granted."
    )
    add("")
    add("- canon_standing: not canonized — lore disposition required (lore-shokunin owns canon)")
    add(
        f"- handoff_status: prepared-not-accepted (live value from {D3_PACKET}: `{d3['handoff_status']}`; "
        f"canon status `{d3['canon_status']}`)"
    )
    add("")
    add("| field | value |")
    add("|---|---|")
    add(f"| packet_id | {PACKET_ID} |")
    add(f"| packet_version | {PACKET_VERSION} (pure function of the pinned read set; no wall-clock content) |")
    add(
        f"| contract_ref | {contract['id']} {contract['revision']}, contract digest "
        f"sha256:{digests[CONTRACT]} (§1 pin, re-measured at assembly time from {CONTRACT}; the "
        "bilateral same-revision read is still pending) |"
    )
    add(
        "| producer | kotodama-shokunin (round-11 handoff-e2e exercise; generative craft and design "
        "records only) |"
    )
    add("| recipient | lore-shokunin (canon, world-bible entities, chronology, bible-wide consistency) |")
    add("| request_ref | none — no lore brief exists; assembled as a deliberately unbound research drill (contract §4) |")
    add(
        "| baseline_bible_ref | none — deliberately unbound research packet; cannot be imported as canon "
        "without a lore baseline and a new reviewed handoff (contract §4) |"
    )
    witness_culture = cell(d2["culture_name"], 60)
    witness_lineage = d2["witness_lineage"].get("term", "?")
    witness_sky = d2["witness_sky_holder"].get("name", "?")
    witness_era = f"{d2['witness_era'].get('tag', '?')} {d2['witness_era'].get('name', '?')}"
    add(
        "| subject_refs | 8 namespaced candidates, all unresolved — no lore entity ID was supplied and none "
        "is guessed (contract §4): `cand:kotodama.d3.language-variety` (witness: "
        f"{D3_PACKET} lexicon {d3['lexicon'][0]['id']}–{d3['lexicon'][-1]['id']}, "
        f"{len(d3['lexicon'])} constructed lexemes), `cand:kotodama.d3.record-keeper-office` (witness: "
        f"belief {d3['beliefs'][0]['id']} attributed to {cell(d3['beliefs'][0]['speaker'], 70)}), "
        "`cand:kotodama.d3.voice-of-the-record-office` (witness: belief "
        f"{d3['beliefs'][-1]['id']} attributed to {cell(d3['beliefs'][-1]['speaker'], 70)}), "
        "`cand:kotodama.d3.hall-assembly-institution` (witness: rank rule "
        f"{d3['rank_rules'][0]['id']} jurisdiction `{d3['rank_rules'][0]['jurisdiction']}`), "
        f"`cand:kotodama.d2.culture` (witness: {D2_PACKET} name \"{witness_culture}\"), "
        f"`cand:kotodama.d2.pasture-lineage-institution` (witness: lexicon L-04 `{witness_lineage}`), "
        f"`cand:kotodama.d2.archaic-sky-holder` (witness: pantheon PAN-01 `{witness_sky}`), "
        f"`cand:kotodama.d2.open-grazing-era` (witness: era record ER-01 \"{witness_era}\") |"
    )
    add(
        f"| scope | two unbound design drills, no real place and no dates: D2 \"{witness_culture}\" "
        f"(eras {'/'.join(d2['eras'])}, {len(d2['lexicon_ids'])} lexicon records, {len(d2['name_ids'])} names, "
        f"{len(d2['costume_ids'])} costumes, {len(d2['material_ids'])} materials, everyday/ritual/ledger "
        f"registers, read-only input bytes); D3 {D3_PACKET} ({'/'.join(era['id'] for era in d3['eras'])} "
        f"fixture-relative eras, {len(d3['lexicon'])} lexemes, {len(d3['names'])} names, "
        f"{len(d3['utterances'])} utterances, {len(d3['beliefs'])} attributed beliefs, {len(d3['symbols'])} "
        f"symbols, {len(d3['costumes'])} costumes — one declared rank-rule violation — "
        f"{len(d3['bridges'])} design-only bridges, ordinary/ritual registers); all native spellings are "
        "constructed ASCII-lowercase, unscreened, with no ISO code or real language family claimed |"
    )
    add("")

    add("## delivered record sets")
    add("")
    add(
        "The per-set scope detail behind the one-line §scope above, read out of the two packets: every "
        "record set is a bounded design construction with no real-world referent asserted."
    )
    add("")
    add("| record set | source artifact | culture group / region | variety / script | register context | era applicability |")
    add("|---|---|---|---|---|---|")
    add(
        f"| D2 drill records | {D2_PACKET} | {cell(d2['culture_name'], 70)} (highland pastoral, stipulated; no real place) | "
        "invented variety; ASCII-lowercase spellings, no ISO code claimed | everyday, ritual and ledger registers | "
        f"{'/'.join(d2['eras'])} (fixture-relative, not BCE/CE) |"
    )
    add(
        f"| D3 drill records | {D3_PACKET} | source-bounded culture drill; one invented hall settlement (no real place) | "
        "invented ordinary and ritual citation layers; ASCII-lowercase spellings, no ISO code claimed | "
        f"ordinary and ritual registers (avoidance rule {d3['speech_rules'][0]['id']} scoped to place "
        f"`{d3['speech_rules'][0]['place']}`) | {'/'.join(era['id'] for era in d3['eras'])} (fixture-relative, not BCE/CE) |"
    )
    add(
        f"| glossary payload | {D3_PACKET} | as above | {len(glossary)} constructed lexemes with E0 citation and "
        "computed E1 ordinary forms | avoidance applies in the ritual register only | "
        f"{d3['lexicon'][0]['available_from']}→{d3['eras'][-1]['id']} |"
    )
    add("")

    add("## artifact_manifest")
    add("")
    add(
        f"Every digest below was re-measured (sha256) at assembly time from the bytes on disk — the gate "
        f"checks digest presence only, this exercise checks equality (design §1). {len(READ_SET)} read-set "
        f"files plus one inline-payload row; the D2 and D3 drills carry no declared packet version, so their "
        "bytes are pinned by digest alone."
    )
    add("")
    add("| artifact_id | path | role | sha256 | records |")
    add("|---|---|---|---|---|")
    for artifact_id, path, role, digest, records in rows:
        add(f"| {artifact_id} | {path} | {cell(role, 260)} | {digest} | {records} |")
    add("")

    add("## dependency_manifest")
    add("")
    add(f"- profile {PROFILE} (this exercise; renderer revision {PACKET_VERSION})")
    add(f"- {GATE} @sha256:{digests[GATE]} (the gate this packet is judged by)")
    add(f"- {CONTRACT} @sha256:{digests[CONTRACT]} (pinned contract; interface revision {contract['revision']})")
    add(
        f"- {D3_PACKET} @sha256:{digests[D3_PACKET]}; {D3_GATES} @sha256:{digests[D3_GATES]}; "
        f"{D3_EXPECTED} @sha256:{digests[D3_EXPECTED]} (d3 payload, legacy projection, freeze manifest)"
    )
    add(
        f"- tools/assemble-culture-d3.py @sha256:{digests['tools/assemble-culture-d3.py']} and "
        f"tools/assemble-d2.py @sha256:{digests['tools/assemble-d2.py']} (assemblers named by the two "
        "packets' own assembly blocks; the second is also the yaml_lines serializer, read-only)"
    )
    add(
        f"- tools/d2-typed-labels.py @sha256:{digests['tools/d2-typed-labels.py']} and "
        f"tools/check-evidence-coupling.py @sha256:{digests['tools/check-evidence-coupling.py']} "
        "(d2 typed-label generator and d3 evidence-coupling guard, both read-only here)"
    )
    add(
        f"- {D2_PACKET} @sha256:{digests[D2_PACKET]}; {D2_TYPED} @sha256:{digests[D2_TYPED]} "
        "(d2 design drill and its typed-label projection, read-only inputs)"
    )
    for change in d3["sound_changes"]:
        add(
            f"- {change['id']} sound law /{change['from']}/ > /{change['to']}/, {change['environment']}, "
            f"{change['from_era']}→{change['to_era']}, register `{change['register']}` (constructed; "
            f"{D3_PACKET} sound_changes[0])"
        )
    for rule in d3["speech_rules"]:
        add(
            f"- {rule['id']} avoidance rule: {rule['lexeme_id']} in register `{rule['register']}`, place "
            f"`{rule['place']}`, substitutes {rule['substitute_lexeme_id']} (constructed; {D3_PACKET} speech_rules)"
        )
    naming = d3["naming_rule"]
    add(
        f"- {naming['id']} naming-timing rule: offsets {naming['allowed_offsets']}, chosen "
        f"{naming['chosen_offset']} {naming['unit']}, source {naming['source_id']} ({naming['status']}; "
        f"{D3_PACKET} naming_rule)"
    )
    rank = d3["rank_rules"][0]
    add(
        f"- {rank['id']} rank rule: authority \"{cell(rank['authority'], 80)}\", {rank['effect']} "
        f"{rank['property']['kind']} `{rank['property']['value']}` for wearer ranks "
        f"{', '.join(rank['wearer_ranks'])}, jurisdiction `{rank['jurisdiction']}`, rites "
        f"{', '.join(rank['rites'])}, eras {', '.join(rank['eras'])} (constructed; {D3_PACKET} rank_rules)"
    )
    add(
        f"- D2 grammar rule ids {d2['rule_ids'][0]}–{d2['rule_ids'][-1]} ({len(d2['rule_ids'])} distinct ids in "
        f"{D2_PACKET} morphology) and {d2['to_verify_lines']} lines carrying a `to-verify` flag"
    )
    add(
        f"- prerequisites: the {d2_component_count + d3_component_count} component digests recorded by the two "
        "assemblers' own `assembly.source_sha256` manifests, re-measured and matched at assembly time; every "
        "reference above is pinned by exact digest or version (contract §4, §9)"
    )
    add("")

    add("## claim_ledger")
    add("")
    add(
        "Claim kinds are the contract §6 kinds; the two D2 rows are labelled a derived projection (author-side) "
        "so they cannot be read as world claims. Statements are read from the live records, not paraphrased "
        "from documentation."
    )
    add("")
    add("| claim_id | kind | evidence_status | summary |")
    add("|---|---|---|---|")
    by_kind = typed["by_kind"]
    add(
        f"| D2-CL01 | designer interpretation | derived projection (author-side) | {typed['labels']} D2 typed "
        f"labels ({by_kind.get('native-form', 0)} native-form / {by_kind.get('translated-label', 0)} "
        f"translated-label / {by_kind.get('borrowed-strata', 0)} borrowed-strata) with {typed['findings_total']} "
        f"findings, {typed['hold_or_fail']} of them hold-or-fail; the label channel is a projection of the D2 "
        f"packet's own records ({D2_TYPED} coverage) |"
    )
    codes = ", ".join(f"{count} {code}" for code, count in sorted((typed["mat_codes"] or {}).items()))
    add(
        f"| D2-CL02 | designer interpretation | derived projection (author-side), holds open | D2 normalization "
        f"residuals: {typed['unresolved_items']} unresolved rank items, {typed['quarantine']} quarantine handles, "
        f"{typed['conflicts']} conflicts, {typed['reconciliations']} reconciliation records, "
        f"{typed['mat_findings']} material-bridge holds ({codes or 'no codes recorded'}) ({D2_TYPED}) |"
    )
    add(
        f"| CL01 | generative rule | invented | {d3['sound_changes'][0]['id']} sound law "
        f"/{d3['sound_changes'][0]['from']}/ > /{d3['sound_changes'][0]['to']}/ word-initially separates the "
        f"{d3['eras'][-1]['id']} spoken forms from the {d3['eras'][0]['id']} citation forms; the ritual citation "
        f"layer keeps the earlier forms ({D3_PACKET} sound_changes) |"
    )
    add(
        f"| CL02 | generative rule | invented | {d3['speech_rules'][0]['id']} substitutes "
        f"{d3['speech_rules'][0]['substitute_lexeme_id']} for {d3['speech_rules'][0]['lexeme_id']} exactly in "
        f"register `{d3['speech_rules'][0]['register']}` / place `{d3['speech_rules'][0]['place']}`; no "
        f"generalized avoidance outside it ({D3_PACKET} speech_rules) |"
    )
    add(
        f"| CL03 | generative rule | invented | {naming['id']} allows name-giving at offsets "
        f"{naming['allowed_offsets']} {naming['unit']}, chosen {naming['chosen_offset']}, source "
        f"{naming['source_id']} ({naming['status']}) — a constructed discrete set, not a historical "
        f"prescription ({D3_PACKET} naming_rule) |"
    )
    add(
        f"| CL04 | generative rule | invented | {rank['id']} prohibits {rank['property']['kind']} "
        f"`{rank['property']['value']}` for wearer ranks {', '.join(rank['wearer_ranks'])} in jurisdiction "
        f"`{rank['jurisdiction']}` ({', '.join(rank['eras'])}); the violation recorded in the costume records is "
        f"retained visibly, never repaired ({D3_PACKET} rank_rules) |"
    )
    add(
        f"| CL05 | generative rule | invented | {len(d3['symbols'])} sign→reading rules "
        f"({d3['symbols'][0]['id']}–{d3['symbols'][-1]['id']}) are audience- and era-scoped conventions of one "
        f"fictional hall; no colour key and no universal meaning is asserted ({D3_PACKET} symbols) |"
    )
    add(
        f"| CL06 | attributed in-world belief | invented; truth status "
        f"`{d3['beliefs'][0]['truth_status']}` | {len(d3['beliefs'])} attributed accounts "
        f"({d3['beliefs'][0]['id']}–{d3['beliefs'][-1]['id']}) with named in-world speakers and opposing "
        f"readings; no narrator asserts either account, and no supernatural claim is endorsed "
        f"({D3_PACKET} beliefs) |"
    )
    add(
        f"| CL07 | designer interpretation | invented | The {'/'.join(era['id'] for era in d3['eras'])} staging, "
        f"the two invented offices and the invented hall authority are an author's design genealogy, not a "
        f"reconstruction of any real institution ({D3_PACKET} scope_notes) |"
    )
    for index, reference in enumerate(d3["references"], start=8):
        add(
            f"| CL{index:02d} | real-world reference | {reference['source_kind']}; support {reference['support_scope']}; "
            f"audit {reference['audit_id']} | {reference['id']} ({cell(reference.get('source_url', ''), 70)}) grounds "
            f"only a design method-transfer: {cell(reference['limits'], 240)} ({D3_PACKET} references) |"
        )
    add(
        f"| CL{8 + len(d3['references']):02d} | screening statement | {d3['screening']['status']} | No real-language "
        f"sweep, novelty check or community consultation has been performed for any D2 or D3 spelling "
        f"(`real_language_sweep_performed: {str(d3['screening']['real_language_sweep_performed']).lower()}`); no "
        f"clearance or permission may be inferred ({D3_PACKET} screening) |"
    )
    add("")

    add("## coupling_edges")
    add("")
    add(
        "Typed source→target relations. The D3 bridge ledger is carried row by row from the live records "
        "(relation, target ids, mechanism and limits verbatim from the packet); the D2 packet states its "
        "couplings per record rather than as an edge list, so it is carried as one aggregate edge."
    )
    add("")
    add("| edge_id | source | relation | target_ids | mechanism | limits |")
    add("|---|---|---|---|---|---|")
    add(
        f"| D2-EDGES | {d2['coupling_notes']} `coupling_note` fields over {D2_PACKET} | dependency (as declared "
        f"per record) | {id_range(d2['lexicon_ids'])}, {id_range(d2['name_ids'])}, {id_range(d2['costume_ids'])} | "
        "each note names the record's own coupling to a lexicon, naming or material record | "
        "carried as declared; the exercise neither adjudicates nor repairs the coupling |"
    )
    for bridge in d3["bridges"]:
        add(
            f"| {bridge['id']} | {bridge['source_id']} | {bridge['relation']} (asserted scope "
            f"`{bridge['asserted_scope']}`, kind {bridge['claim_kind']}) | {', '.join(bridge['target_ids'])} | "
            f"{cell(bridge['mechanism'], 300)} | {cell(bridge['limits'], 320)} |"
        )
    add("")

    add("## requested_decisions")
    add("")
    add(
        "Per-record questions for lore, with mutually exclusive alternatives and blockers. `accept` always "
        "means retain as non-canon candidate material; it never means canonize."
    )
    add("")
    add("| record_id | question | alternatives | blocker |")
    add("|---|---|---|---|")
    decisions = [
        (
            f"RD-01 {d3['lexicon'][0]['id']}–{d3['lexicon'][-1]['id']} + {d3['names'][0]['id']}–{d3['names'][-1]['id']}",
            f"accept the {len(d3['lexicon'])} constructed D3 lexemes and {len(d3['names'])} names as candidate "
            "world material, with the naming rule as proposed?",
            "accept / defer / reject per record",
            "real-language sweep unperformed; names stay namespaced candidates",
        ),
        (
            f"RD-02 {d3['beliefs'][0]['id']}–{d3['beliefs'][-1]['id']}",
            "record the attributed accounts as in-world belief, and decide whether either becomes a world-fact?",
            "belief only / belief plus world-fact ruling / defer",
            "canon standing is lore's; truth status stays unresolved here",
        ),
        (
            f"RD-03 {d3['symbols'][0]['id']}–{d3['symbols'][-1]['id']}",
            "adopt the audience- and era-scoped sign→reading rules, including their competing readings?",
            "adopt scoped / adopt with a single reading only / defer",
            "a single reading would drop the recorded counter-reading",
        ),
        (
            f"RD-04 {'/'.join(era['id'] for era in d3['eras'])}",
            "adopt the relative era stages, with or without dates?",
            "adopt without dates / adopt with dates supplied by lore / defer",
            "no calendar exists; dates are lore's decision",
        ),
        (
            f"RD-05 {d3['costumes'][0]['id']}–{d3['costumes'][-1]['id']} + {rank['id']}",
            "adopt the costume records and the rank rule, accepting that one costume stays a declared violation?",
            "accept with the violation retained / accept without the violating record / defer",
            "the violation is evidence of the rule's reach, not an error to repair",
        ),
        (
            f"RD-06 {d3['names'][0]['id']}–{d3['names'][-1]['id']} + screening",
            "approve the name records, given that no real-language screening has been performed?",
            "approve as provisional / hold until screened / reject",
            "screening is unresolved kotodama-side work, not a lore disposition",
        ),
        (
            f"RD-07 {d3['bridges'][0]['id']}–{d3['bridges'][-1]['id']}",
            f"accept the {len(d3['bridges'])} design-only source bridges as method-transfer evidence?",
            "accept as design-only / defer",
            "bridge support is partial or scoped; no real-world fact is claimed",
        ),
        (
            "RD-08 transfer surface",
            "name the baseline bible revision, entity keys and receipt surface this lane should deliver against?",
            "supply a baseline and receipt surface / keep the lane unbound / defer",
            "no lore baseline exists, so nothing here can be imported as canon",
        ),
        (
            "RD-D2-01 D2 typed-label channel",
            f"record the D2 label channel ({typed['labels']} labels, {typed['hold_or_fail']} holds) as a "
            "author-side projection to be resolved before any D2 record is handed over?",
            "record as author-side / require resolution first / defer",
            "the channel is a projection of D2 design records, not a delivered payload",
        ),
        (
            "RD-D2-02 D2 retained holds",
            f"decide the disposition of the {typed['unresolved_items']} unresolved D2 rank items and "
            f"{d2['to_verify_lines']} `to-verify` lines?",
            "resolve kotodama-side first / accept with holds recorded / defer",
            "held rows are explicit unknowns and are not promoted by this packet",
        ),
    ]
    for record_id, question, alternatives, blocker in decisions:
        add(f"| {record_id} | {question} | {alternatives} | {blocker} |")
    add("")

    add("## validation")
    add("")
    add(
        "Observed rows only: what this run actually measured, with the command shapes it used. These are "
        "local generation and identity checks of one envelope — not bible-wide consistency and not a canon "
        "decision (contract §8 step 3)."
    )
    add("")
    add(
        f"- read set: {len(READ_SET)} files re-measured (`sha256`, same run) against the frozen baseline's "
        f"`inputs` block; the §artifact_manifest digests are those measured values, not copied from any document"
    )
    add(
        f"- component digests: {d2_component_count + d3_component_count} digests recorded by the two assemblers' "
        f"own `assembly.source_sha256` manifests ({d2_component_count} D2, {d3_component_count} D3) re-measured "
        "against the component bytes on disk — all matched, so each packet still describes the files it names"
    )
    add(
        "- manifest equality: every §artifact_manifest row's digest equals the sha256 of the file it names, "
        "measured in this run; the gate checks digest presence only, so this equality is the exercise's own "
        "assertion (design §1, §6.6)"
    )
    add(
        f"- field agreement: the contract §4 table yields {len(contract['section4_names'])} required field names, "
        f"the gate's own FIELD_NAMES tuple yields {len(fields_supplied[1])}, and this packet supplies "
        f"{len(fields_supplied[0])} — the three sets are compared, not assumed (design §6.1)"
    )
    add(
        f"- glossary identity: the {len(glossary)} rows are the live D3 lexicon in source order (id, E0 form, "
        "computed E1 form, gloss) and every etymology carries the record's own status token, which is inside the "
        "licensed vocabulary (design §5)"
    )
    add(
        "- D2 read-only facts carried into this packet's D2 claim rows: "
        f"{typed['labels']} typed labels ({by_kind.get('native-form', 0)} native-form / "
        f"{by_kind.get('translated-label', 0)} translated-label / {by_kind.get('borrowed-strata', 0)} "
        f"borrowed-strata), {typed['findings_total']} findings ({typed['hold_or_fail']} hold-or-fail), "
        f"{typed['unresolved_items']} unresolved rank items, {typed['quarantine']} quarantine handles, "
        f"{typed['conflicts']} conflicts, {typed['reconciliations']} reconciliation records, "
        f"{typed['mat_findings']} material-bridge holds"
    )
    add(
        f"- gate: `python3 {GATE} packet.md` over the isolated copy, run from a directory outside the "
        "repository; declared expectation, checked after the run — "
        f"exit {DECLARED['expected_exit']}, fields={DECLARED['expected_scan']['fields']}, "
        f"glossary-entries={DECLARED['expected_scan']['glossary_entries']}, "
        f"findings={DECLARED['expected_scan']['findings']}; the observed values are compared against the frozen "
        f"baseline in `{BASELINE_DEFAULT}`, whose run log records the verdict of the run it froze"
    )
    add("")

    add("## open_questions")
    add("")
    add(
        f"- OQ-E2E-01: no real-language homophone, offensive-association or novelty sweep has been performed "
        f"for any D2 or D3 spelling ({D3_PACKET} screening: {d3['screening']['status']}) — kotodama "
        "pre-publication + lore; blocking for official name approval."
    )
    add(
        "- OQ-E2E-02: no lore baseline, entity keys, receipt surface or bilateral same-revision read exists "
        f"for {CONTRACT} (revision {contract['revision']}) — lore + both lanes; blocking for the first transfer "
        "(contract §1, §4, §8)."
    )
    add(
        f"- OQ-E2E-03: {len(d3['scope_notes'])} D3 scope notes and {d2['to_verify_lines']} D2 `to-verify` lines "
        "carry unresolved residuals (partial-support sources, unperformed screening, unresolved rank items) — "
        "kotodama; blocking for the affected records, not for this envelope."
    )
    add(
        "- OQ-E2E-04: the D2 and D3 drills are separate design fixtures with no shared chronology, and this "
        "packet asserts none; any combined reading is a lore decision — lore; non-blocking."
    )
    add(
        "- OQ-E2E-05: documentation surfaces outside this read set (`examples/culture-d3/handoff.md`, "
        "`examples/culture-d3/README.md`, `examples/culture-d2/ASSEMBLY.md`) are excluded from the computational "
        "freeze; R11-O01 §7 measured stale digests in their prose. This exercise re-measures the bytes it reads "
        "and propagates no documentation figure — kotodama-owned; non-blocking."
    )
    add("")

    add(f"## glossary payload (inline; the live D3 lexicon, {glossary[0][0]}–{glossary[-1][0]})")
    add("")
    add(
        f"All {len(glossary)} rows are the assembled D3 packet's lexicon in source order (E0 citation form, "
        "computed E1 ordinary form, packet gloss). Every etymology carries `status: <record status>` — a "
        "constructed design derivation by the declared sound rule, with no real-language derivation, "
        "borrowing, or novelty-in-all-languages claim."
    )
    add("")
    add("| entry_id | E0 form | E1 form | gloss (packet) | etymology |")
    add("|---|---|---|---|---|")
    for entry_id, e0, e1, gloss, etymology in glossary:
        add(f"| {entry_id} | {e0} | {e1} | {cell(gloss)} | {cell(etymology)} |")
    add("")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# preflight (the exercise's own format discipline; the gate stays authoritative)
# --------------------------------------------------------------------------


def extract_field_values(text):
    """Field values as this exercise emits them: `## field` bodies and `| field | value |` rows."""
    lines = text.splitlines()
    values = {}
    for index, line in enumerate(lines):
        heading = re.match(r"^## ([a-z_]+)\s*$", line)
        if heading and heading.group(1) in FIELD_NAMES:
            body = []
            for following in lines[index + 1:]:
                if re.match(r"^#{1,6}\s+\S", following):
                    break
                body.append(following)
            values.setdefault(heading.group(1), "\n".join(body).strip())
            continue
        row = re.match(r"^\|\s*`?([a-z_]+)`?\s*\|(.*)\|\s*$", line)
        if row and row.group(1) in FIELD_NAMES:
            values.setdefault(row.group(1), row.group(2).strip().strip("|").strip())
    return values


def mentions(text, name):
    """The gate's `_mentions` boundary test, mirrored for the heading-hazard probe."""
    return re.search(rf"(?<![0-9A-Za-z_]){re.escape(name)}(?![0-9A-Za-z_])", text) is not None


def heading_field_tokens(text):
    """Field-name tokens carried by headings that are not the bare field name itself.

    The gate collects a heading as a supply for every §4 name its text mentions
    (design §4b), so any such heading would silently replace that field's value.
    """
    hazards = []
    for line in text.splitlines():
        heading = re.match(r"^\s{0,3}#{1,6}\s+(.*?)\s*$", line)
        if not heading:
            continue
        title = heading.group(1)
        for name in FIELD_NAMES:
            if title == name:
                continue
            if mentions(title, name):
                hazards.append(name)
    return sorted(set(hazards))


def glossary_rows(text):
    """(entry_id, etymology) for the packet's inline glossary table."""
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if not line.lstrip().startswith("|") or index + 1 >= len(lines):
            continue
        header = [norm_cell(cell_text).lower() for cell_text in line.strip().strip("|").split("|")]
        if "entry_id" not in header:
            continue
        if not re.match(r"^\|[\s:|-]+\|$", lines[index + 1].strip()):
            continue
        etym_column = next((i for i, name in enumerate(header) if name.startswith("etymology")), None)
        rows = []
        cursor = index + 2
        while cursor < len(lines) and lines[cursor].lstrip().startswith("|"):
            cells = [part.strip() for part in lines[cursor].strip().strip("|").split("|")]
            entry_id = cells[0] if cells else "?"
            etymology = cells[etym_column] if etym_column is not None and etym_column < len(cells) else ""
            rows.append((entry_id, etymology))
            cursor += 1
        return rows
    return []


def preflight(text):
    problems = []
    values = extract_field_values(text)
    for name in FIELD_NAMES:
        value = values.get(name)
        if value is None:
            problems.append(f"field `{name}` not emitted")
        elif is_placeholder(value):
            problems.append(f"field `{name}` carries only a placeholder value")
    supplied = set(values)
    if supplied != set(FIELD_NAMES):
        problems.append(f"supplied field set differs from the §4 set: {sorted(set(FIELD_NAMES) - supplied)}")
    if not CANON_MARKER_RE.search(text):
        problems.append("non-canon marker `not canonized` missing")
    dependencies = values.get("dependency_manifest", "")
    if re.search(r"(?i)\blatest\b", dependencies):
        problems.append("dependency_manifest carries a floating `latest` reference")
    if not DIGEST_RE.search(values.get("artifact_manifest", "")):
        problems.append("artifact_manifest names no file digest")
    contract_value = values.get("contract_ref", "")
    if not re.search(r"\b\d+\.\d+\.\d+\b", contract_value) or not re.search(r"[0-9a-f]{32,}", contract_value):
        problems.append("contract_ref names no revision and/or no digest")
    for trap in CANON_TRAP_RES:
        match = trap.search(text)
        if match:
            problems.append(f"producer-side canon certification pattern: {match.group(0)[:80]!r}")
    rows = glossary_rows(text)
    if len(rows) != DECLARED["expected_scan"]["glossary_entries"]:
        problems.append(
            f"glossary payload holds {len(rows)} rows, expected {DECLARED['expected_scan']['glossary_entries']}"
        )
    for entry_id, etymology in rows:
        if is_placeholder(etymology):
            problems.append(f"glossary entry {entry_id} carries no etymology text")
            continue
        named = re.search(r"(?i)\bstatus\s*[:=]\s*[`*]?([A-Za-z_-]+)", etymology)
        if named and named.group(1).lower() not in ETYM_STATUSES:
            problems.append(f"glossary entry {entry_id} states unlicensed status {named.group(1)!r}")
        elif not named and not any(re.search(rf"(?i)\b{status}\b", etymology) for status in ETYM_STATUSES):
            problems.append(f"glossary entry {entry_id} names no licensed etymology status")
    return problems


# --------------------------------------------------------------------------
# assembly and the run
# --------------------------------------------------------------------------


class Assembly:
    def __init__(self, root):
        self.root = root
        self.digests = {}
        self.sizes = {}
        for rel in READ_SET:
            digest, size = measure(root, rel)
            self.digests[rel] = digest
            self.sizes[rel] = size
        self.contract = mine_contract(root)
        self.gate_fields = gate_field_names(root)
        if tuple(self.gate_fields) != FIELD_NAMES:
            raise ArtifactError(
                f"{GATE}: its FIELD_NAMES tuple disagrees with the exercise's §4 field list "
                f"({len(self.gate_fields)} vs {len(FIELD_NAMES)} names)"
            )
        if self.contract["section4_names"] != set(FIELD_NAMES):
            missing = sorted(set(FIELD_NAMES) - self.contract["section4_names"])
            extra = sorted(self.contract["section4_names"] - set(FIELD_NAMES))
            raise ArtifactError(
                f"{CONTRACT}: §4 field table disagrees with the envelope set (missing {missing}, extra {extra})"
            )
        self.d2 = mine_d2(root)
        self.d3 = mine_d3(root)
        self.typed = mine_typed_labels(root)
        self.component_checked, self.component_matched = verify_component_digests(root, self.d2, self.d3)
        self.glossary = build_glossary(self.d3)
        self.packet = build_packet(
            root,
            self.d2,
            self.d3,
            self.typed,
            self.contract,
            self.digests,
            self.sizes,
            self.glossary,
            (set(FIELD_NAMES), self.gate_fields),
        )
        self.packet_sha256 = sha256_text(self.packet)
        self.field_values = extract_field_values(self.packet)

        # design §6 cross-reference assertions the gate cannot make
        self.assert_contract_digest()
        self.assert_claim_kinds()
        self.assert_candidates_unresolved()
        self.assert_manifest_equality()

    def value(self, name):
        return self.field_values.get(name, "")

    def assert_contract_digest(self):
        expected = f"sha256:{self.digests[CONTRACT]}"
        if expected not in self.value("contract_ref"):
            raise Failed("E2E-DIGEST", f"contract_ref does not carry the measured contract digest {expected[:19]}…")

    def assert_claim_kinds(self):
        rows = re.findall(r"^\| (CL\d\d|D2-CL\d\d) \| ([^|]+?) \|", self.packet, re.M)
        if not rows:
            raise Failed("E2E-COUNT", "claim_ledger carries no claim rows")
        for claim_id, kind in rows:
            if kind.strip() not in CLAIM_KINDS:
                raise Failed(
                    "E2E-COUNT",
                    f"claim {claim_id} states kind {kind.strip()!r}, outside the contract §6 kinds "
                    f"{CLAIM_KINDS}",
                )

    def assert_candidates_unresolved(self):
        subject = self.value("subject_refs")
        tokens = re.findall(r"`([^`]+)`", subject)
        candidates = [token for token in tokens if token.startswith("cand:")]
        if len(candidates) != 8:
            raise Failed("E2E-COUNT", f"subject_refs names {len(candidates)} candidate refs, expected 8")
        if "unresolved" not in subject:
            raise Failed("E2E-COUNT", "subject_refs does not state that the candidates are unresolved")

    def assert_manifest_equality(self):
        manifest = self.value("artifact_manifest")
        checked = 0
        for row in re.findall(r"^\| (A-[\w-]+) \| ([^|]+?) \|.*?\| ([0-9a-f]{64}) \|", manifest, re.M):
            artifact_id, path, digest = row
            if path.startswith("§"):
                continue
            measured = self.digests.get(path) or (measure(self.root, path)[0] if (Path(self.root) / path).exists() else None)
            if measured is None:
                raise Failed("E2E-DIGEST", f"manifest row {artifact_id} names {path}, which is not in the read set")
            checked += 1
            if measured != digest:
                raise Failed(
                    "E2E-DIGEST",
                    f"manifest row {artifact_id}: {path} measures {measured[:12]}… but the row says {digest[:12]}…",
                )
        if checked != len(READ_SET):
            raise Failed("E2E-COUNT", f"manifest re-measured {checked} files, expected {len(READ_SET)}")

    def run_gate(self, workdir):
        isolated = Path(workdir) / "isolated"
        isolated.mkdir(parents=True, exist_ok=True)
        (isolated / "packet.md").write_text(self.packet, encoding="utf-8")
        gate = Path(self.root) / GATE
        if not gate.is_file():
            raise MissingArtifact(f"gate not found: {GATE}")
        run = subprocess.run(
            [sys.executable, str(gate), "packet.md"],
            cwd=str(isolated),
            capture_output=True,
            text=True,
        )
        findings = re.findall(r"^FINDING ([A-Za-z0-9-]+):", run.stdout, re.M)
        scan = re.search(r"^INFO scan: fields=(\d+)/(\d+) glossary-entries=(\d+) findings=(\d+)", run.stdout, re.M)
        if scan is None:
            raise Failed(
                "E2E-DATA",
                f"the gate produced no `INFO scan` line (exit {run.returncode}): "
                f"{(run.stdout or run.stderr).strip()[:200]}",
            )
        return {
            "exit": run.returncode,
            "findings": findings,
            "fields": int(scan.group(1)),
            "fields_total": int(scan.group(2)),
            "glossary_entries": int(scan.group(3)),
            "findings_count": int(scan.group(4)),
            "stdout": run.stdout,
            "cwd": str(isolated),
        }


def baseline_payload(baseline):
    return {key: value for key, value in baseline.items() if key != "baseline_digest"}


def baseline_digest(baseline):
    return sha256_text(json.dumps(baseline_payload(baseline), sort_keys=True, separators=(",", ":"), ensure_ascii=False))


def load_baseline(root, baseline_rel):
    path = Path(baseline_rel) if Path(baseline_rel).is_absolute() else Path(root) / baseline_rel
    if not path.is_file():
        raise BaselineError(f"frozen baseline not found: {path} (write one with --freeze DIR)")
    try:
        baseline = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError) as exc:
        raise BaselineError(f"frozen baseline unreadable: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise BaselineError(f"frozen baseline is not valid JSON: {exc}") from exc
    required = (
        "profile", "packet_id", "packet_version", "expected_exit", "expected_finding_ids", "expected_scan",
        "packet_sha256", "glossary_entry_ids", "inputs", "baseline_digest",
    )
    missing = [key for key in required if key not in baseline]
    if missing:
        raise BaselineError(f"frozen baseline is missing {missing} — it was not written by this exercise")
    if baseline["profile"] != PROFILE:
        raise BaselineError(f"frozen baseline profile {baseline['profile']!r} is not {PROFILE!r}")
    if baseline.get("baseline_digest") != baseline_digest(baseline):
        raise BaselineError(
            "baseline integrity digest mismatch — the baseline file was edited without re-freezing "
            "(re-freeze with --freeze DIR and read the diff it prints)"
        )
    for key in ("expected_exit", "expected_finding_ids", "expected_scan"):
        if baseline[key] != DECLARED[key]:
            raise BaselineError(f"baseline declares {key}={baseline[key]!r}, the exercise declares {DECLARED[key]!r}")
    return path, baseline


def exercise(root=ROOT, baseline_rel=BASELINE_DEFAULT, isolation=None):
    """Run the exercise; return (exit code, code-or-None, records)."""
    records = []

    def record(name, ok, detail=""):
        records.append({"check": name, "ok": bool(ok), "detail": detail})

    try:
        baseline_path, baseline = load_baseline(root, baseline_rel)
        snapshot_before = {rel: measure(root, rel)[0] for rel in READ_SET}
        assembly = Assembly(root)

        drifted = [
            rel for rel, digest in baseline["inputs"].items() if assembly.digests.get(rel) != digest
        ]
        if drifted:
            for rel in drifted:
                record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
            raise Failed("E2E-DIGEST", f"{len(drifted)} read-set file(s) changed since the baseline was frozen: {', '.join(drifted[:3])}")
        record("input-digest", True, f"{len(READ_SET)} read-set digests match the frozen baseline")

        problems = preflight(assembly.packet)
        if problems:
            for problem in problems:
                record("preflight", False, problem)
            raise Failed("E2E-COUNT", f"{len(problems)} preflight problem(s): {problems[0]}")
        record(
            "preflight",
            True,
            f"{len(FIELD_NAMES)} fields supplied, non-canon marker present, glossary vocabulary licensed, "
            "no floating version reference",
        )
        record(
            "cross-references",
            True,
            f"contract §4 names = gate FIELD_NAMES = supplied fields; contract digest measured; claim kinds "
            f"in the §6 set; {assembly.component_matched}/{assembly.component_checked} component digests matched; "
            f"manifest digests equal bytes for {len(READ_SET)} files",
        )

        keep_dir = isolation is not None
        with tempfile.TemporaryDirectory(prefix="handoff-e2e-") as workdir:
            gate = assembly.run_gate(workdir)
        record(
            "gate-exit",
            gate["exit"] == baseline["expected_exit"],
            f"{GATE} exit {gate['exit']} (expected {baseline['expected_exit']}) over the isolated copy at {gate['cwd']}",
        )
        if gate["exit"] != baseline["expected_exit"]:
            raise Failed("E2E-GATE", f"the gate exited {gate['exit']}: {gate['stdout'].strip()[:300]}")
        if gate["findings"]:
            raise Failed("E2E-GATE", f"the gate reported findings: {', '.join(gate['findings'])}")
        observed_scan = {
            "fields": f"{gate['fields']}/{gate['fields_total']}",
            "glossary_entries": gate["glossary_entries"],
            "findings": gate["findings_count"],
        }
        if observed_scan != baseline["expected_scan"]:
            record("gate-scan", False, f"observed {observed_scan}, expected {baseline['expected_scan']}")
            raise Failed("E2E-SCAN", f"gate scan {observed_scan} != baseline scan {baseline['expected_scan']}")
        record("gate-scan", True, f"fields={observed_scan['fields']} glossary-entries={observed_scan['glossary_entries']} findings={observed_scan['findings']}")

        if assembly.packet_sha256 != baseline["packet_sha256"]:
            record(
                "frozen-packet",
                False,
                f"assembled {assembly.packet_sha256[:12]}… vs frozen {str(baseline['packet_sha256'])[:12]}…",
            )
            raise Failed("E2E-DIGEST", "the assembled packet does not match the frozen packet digest")
        record("frozen-packet", True, f"packet sha256 {assembly.packet_sha256}")
        if [row[0] for row in assembly.glossary] != baseline["glossary_entry_ids"]:
            record("frozen-glossary", False, "the glossary entry-id set drifted from the baseline")
            raise Failed("E2E-COUNT", "the glossary entry-id set drifted from the frozen baseline")
        record("frozen-glossary", True, f"{len(assembly.glossary)} entry ids match the baseline")

        snapshot_after = {rel: measure(root, rel)[0] for rel in READ_SET}
        unchanged = snapshot_before == snapshot_after
        record(
            "preservation",
            unchanged,
            f"the {len(READ_SET)} read-set files are byte-identical before and after the run"
            if unchanged
            else "a read-set file changed while the exercise ran",
        )
        if not unchanged:
            raise Failed("E2E-DIGEST", "a read-set file changed while the exercise ran")
        return EXIT_PASS, None, records

    except Failed as exc:
        record("verdict", False, str(exc))
        return EXIT_FAIL, exc.code, records
    except Unevaluatable as exc:
        record("verdict", False, str(exc))
        return EXIT_UNEVALUATED, exc.code if issubclass(type(exc), Unevaluatable) and getattr(type(exc), "code", None) else "E2E-DATA", records


def freeze(root, target_dir):
    """Write the frozen baseline (and the packet/run log beside it), printing diffs."""
    assembly = Assembly(root)
    problems = preflight(assembly.packet)
    if problems:
        raise Failed("E2E-COUNT", f"refusing to freeze a packet that fails preflight: {problems[0]}")
    with tempfile.TemporaryDirectory(prefix="handoff-freeze-") as workdir:
        gate = assembly.run_gate(workdir)
    if gate["exit"] != DECLARED["expected_exit"] or gate["findings"]:
        raise Failed("E2E-GATE", f"refusing to freeze: gate exit {gate['exit']} with findings {gate['findings']}")
    expected_scan = {
        "fields": f"{gate['fields']}/{gate['fields_total']}",
        "glossary_entries": gate["glossary_entries"],
        "findings": gate["findings_count"],
    }
    if expected_scan != DECLARED["expected_scan"]:
        raise Failed("E2E-SCAN", f"refusing to freeze: observed scan {expected_scan} != declared {DECLARED['expected_scan']}")

    baseline = {
        "profile": PROFILE,
        "packet_id": PACKET_ID,
        "packet_version": PACKET_VERSION,
        "frozen_at": datetime.date.today().isoformat(),
        "frozen_by": "tools/exercise-handoff-e2e.py",
        **DECLARED,
        "packet_sha256": assembly.packet_sha256,
        "glossary_entry_ids": [row[0] for row in assembly.glossary],
        "inputs": {rel: assembly.digests[rel] for rel in READ_SET},
        "field_digests": {name: sha256_text(value) for name, value in sorted(assembly.field_values.items())},
        "cross_refs": {
            "contract_id": assembly.contract["id"],
            "contract_revision": assembly.contract["revision"],
            "contract_digest": f"sha256:{assembly.digests[CONTRACT]}",
            "component_digests_checked": assembly.component_checked,
            "component_digests_matched": assembly.component_matched,
            "gate_exit": gate["exit"],
            "gate_scan": expected_scan,
        },
        "counts": {
            "d2_lexicon": len(assembly.d2["lexicon_ids"]),
            "d2_names": len(assembly.d2["name_ids"]),
            "d2_coupling_notes": assembly.d2["coupling_notes"],
            "d2_to_verify_lines": assembly.d2["to_verify_lines"],
            "d3_lexicon": len(assembly.d3["lexicon"]),
            "d3_names": len(assembly.d3["names"]),
            "d3_bridges": len(assembly.d3["bridges"]),
            "d3_references": len(assembly.d3["references"]),
            "d2_typed_labels": assembly.typed["labels"],
        },
        "declared_expectation": DECLARED_EXPECTATION,
        "limits": BASELINE_LIMITS,
    }
    baseline["baseline_digest"] = baseline_digest(baseline)

    target = Path(target_dir)
    target.mkdir(parents=True, exist_ok=True)
    baseline_path = target / "expected.json"
    previous = None
    if baseline_path.is_file():
        try:
            previous = json.loads(baseline_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            previous = None
    baseline_path.write_text(json.dumps(baseline, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    (target / "packet.md").write_text(assembly.packet, encoding="utf-8")
    run_log = [
        f"exercise: tools/exercise-handoff-e2e.py ({PROFILE}, packet {PACKET_ID} {PACKET_VERSION})",
        f"gate: python3 {GATE} packet.md (isolated copy, foreign working directory)",
        f"gate verdict: exit {gate['exit']}, fields={gate['fields']}/{gate['fields_total']}, "
        f"glossary-entries={gate['glossary_entries']}, findings={gate['findings_count']}",
        f"packet sha256: {assembly.packet_sha256}",
        f"read set: {len(READ_SET)} files measured; component digests {assembly.component_matched}/"
        f"{assembly.component_checked} matched",
    ]
    run_log.extend(gate["stdout"].strip().splitlines())
    (target / "run.log").write_text("\n".join(run_log) + "\n", encoding="utf-8")
    diff = []
    if previous:
        for key in ("packet_sha256", "glossary_entry_ids"):
            if previous.get(key) != baseline[key]:
                diff.append(f"re-frozen {key}: {str(previous.get(key))[:40]}… -> {str(baseline[key])[:40]}…")
        for rel, digest in sorted(baseline["inputs"].items()):
            if previous.get("inputs", {}).get(rel) != digest:
                diff.append(f"re-frozen input {rel}: {str(previous.get('inputs', {}).get(rel))[:12]}… -> {digest[:12]}…")
    freeze_lines = [
        f"frozen: {baseline['frozen_at']} by tools/exercise-handoff-e2e.py",
        f"packet_sha256: {assembly.packet_sha256}",
        f"gate: exit {gate['exit']}, fields={gate['fields']}/{gate['fields_total']}, "
        f"glossary-entries={gate['glossary_entries']}, findings={gate['findings_count']}",
        f"read set: {len(READ_SET)} files; component digests {assembly.component_matched}/{assembly.component_checked}",
    ]
    freeze_lines.extend(diff or ["no tracked value changed since the previous freeze"])
    (target / "freeze.txt").write_text("\n".join(freeze_lines) + "\n", encoding="utf-8")
    return baseline, previous, diff, freeze_lines


# --------------------------------------------------------------------------
# selftest (design §8 tamper controls, §9 control matrix)
# --------------------------------------------------------------------------


def build_fixture_root(workdir):
    """A throwaway copy of every file the exercise reads or re-measures, inside one temp dir.

    Beyond the read set and the gate, this copies the component files the two
    assemblers name in their own `assembly.source_sha256` manifests, because the
    exercise re-measures those against the manifests (design §6 cross-checks).
    """
    fixture = Path(workdir) / "fixture"
    components = set(mine_d2(ROOT)["components"]) | set(mine_d3(ROOT)["components"])
    for rel in (*READ_SET, GATE, *sorted(components)):
        source = ROOT / rel
        if not source.is_file():
            raise MissingArtifact(f"selftest fixture source missing: {rel}")
        target = fixture / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    return fixture


def gate_over(fixture, text, workdir):
    isolated = Path(workdir) / "isolated"
    isolated.mkdir(parents=True, exist_ok=True)
    (isolated / "packet.md").write_text(text, encoding="utf-8")
    run = subprocess.run(
        [sys.executable, str(fixture / GATE), "packet.md"],
        cwd=str(isolated),
        capture_output=True,
        text=True,
    )
    findings = re.findall(r"^FINDING ([A-Za-z0-9-]+):", run.stdout, re.M)
    return {"exit": run.returncode, "findings": sorted(set(findings)), "stdout": run.stdout}


def mutated(packet, anchor, replacement, count=1):
    if anchor not in packet:
        raise MissingArtifact(f"selftest control anchor not found: {anchor!r}")
    return packet.replace(anchor, replacement, count)


def freezed_copy(fixture, workdir, name="frozen"):
    target = Path(workdir) / name
    shutil.copytree(fixture, target)
    baseline, _, _, _ = freeze(target, target / FROZEN_DIR_DEFAULT)
    return target, baseline


def selftest():
    results = []
    with tempfile.TemporaryDirectory(prefix="handoff-selftest-") as workdir:
        fixture = build_fixture_root(workdir)
        frozen_root, baseline = freezed_copy(fixture, workdir, "frozen-root")
        baseline_rel = FROZEN_DIR_DEFAULT + "/expected.json"

        code, err, records = exercise(root=frozen_root, baseline_rel=baseline_rel)
        assert code == EXIT_PASS, [(r["check"], r["detail"]) for r in records if not r["ok"]]
        scan = next(r["detail"] for r in records if r["check"] == "gate-scan")
        assert "fields=16/16" in scan and "glossary-entries=20" in scan and "findings=0" in scan, scan
        results.append(f"positive: exit 0 — {scan}")

        # isolation probe: the same run through the CLI from a foreign working directory
        run = subprocess.run(
            [sys.executable, str(ROOT / "tools/exercise-handoff-e2e.py"), "--root", str(frozen_root), "--quiet"],
            cwd=workdir,
            capture_output=True,
            text=True,
        )
        assert run.returncode == EXIT_PASS, (run.returncode, run.stdout, run.stderr)
        assert "handoff-e2e: exit=0" in run.stdout, run.stdout
        results.append("isolation: the CLI run from a foreign cwd exits 0 with the same scan")

        assembly = Assembly(frozen_root)
        packet = assembly.packet

        def gate_case(label, text, expect_exit, expect_ids):
            with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
                observed = gate_over(frozen_root, text, control_dir)
            assert observed["exit"] == expect_exit, (label, observed["exit"], observed["stdout"])
            for finding_id in expect_ids:
                assert finding_id in observed["findings"], (label, observed["findings"])
            results.append(f"{label}: gate exit {observed['exit']}, {'+'.join(observed['findings']) or 'no findings'}")

        gate_case(
            "malformed-01 dropped request_ref row",
            mutated(packet, "| request_ref |", "| request-ref-unused |"),
            EXIT_FAIL, ["HO-MISSING"],
        )
        gate_case(
            "malformed-02 blank scope value",
            mutated(packet, "| scope | two unbound design drills", "| scope | - |\n| scope-unused | two unbound design drills"),
            EXIT_FAIL, ["HO-EMPTY"],
        )
        gate_case(
            "malformed-03 floating version",
            mutated(packet, f"- {CONTRACT} @sha256:", f"- {CONTRACT} @latest (@sha256:"),
            EXIT_FAIL, ["HO-DEP-FLOAT"],
        )
        gate_case(
            "malformed-04 canon marker removed",
            mutated(
                mutated(packet, "not canonized — lore disposition required", "kept as a working record"),
                "; not canonized)",
                "; kept as a working record)",
            ),
            EXIT_FAIL, ["HO-CANON-MARKER"],
        )
        gate_case(
            "malformed-05 producer canon claim",
            mutated(
                packet,
                "| packet_version |",
                "| canon_standing | canonized — producer certification (control) |\n| packet_version |",
            ),
            EXIT_FAIL, ["HO-CANON-CLAIM"],
        )
        gate_case(
            "malformed-06 unlicensed etymology status",
            mutated(packet, "| L01 | pina | fina | spoken pledge | status: constructed", "| L01 | pina | fina | spoken pledge | status: invented"),
            EXIT_FAIL, ["HO-GLOSS-ETYM"],
        )
        gate_case(
            "malformed-08 hyphenated coupling_edges heading",
            mutated(packet, "## coupling_edges", "## coupling-edges"),
            EXIT_FAIL, ["HO-MISSING"],
        )
        gate_case(
            "malformed-09 renamed open_questions heading",
            mutated(packet, "## open_questions", "## open-questions-notes"),
            EXIT_FAIL, ["HO-MISSING"],
        )
        gate_case(
            "malformed-10 malformed input (no heading)",
            "plain prose, no markdown heading at all\n",
            EXIT_UNEVALUATED, ["HO-DATA"],
        )

        # malformed-07: the gate misses a dropped glossary row; the exercise must not
        dropped = "\n".join(
            line for line in packet.splitlines() if not line.startswith("| L20 |")
        ) + "\n"
        assert not any(name == "L20" for name, _ in glossary_rows(dropped)), "control anchor failed"
        assert any("holds 19 rows" in problem for problem in preflight(dropped)), preflight(dropped)
        results.append("malformed-07 dropped glossary row: the gate counts 19 rows silently; preflight fails closed")

        # hazard probe: a heading carrying a field-name token hijacks that field in the
        # gate's reader while the run still exits 0; the renderer must emit none (design §4b)
        assert heading_field_tokens(packet) == [], heading_field_tokens(packet)
        hijack = mutated(packet, "## delivered record sets", "## scope-notes")
        assert heading_field_tokens(hijack) == ["scope"], heading_field_tokens(hijack)
        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            observed = gate_over(frozen_root, hijack, control_dir)
        assert observed["exit"] == EXIT_PASS, observed["stdout"]
        results.append(
            "hazard probe: a `scope-notes` heading is read as a `scope` supply with exit still 0; "
            "the renderer emits no heading carrying a field-name token"
        )

        # preservation probe: the read set is untouched by a run
        before = {rel: measure(frozen_root, rel)[0] for rel in READ_SET}
        exercise(root=frozen_root, baseline_rel=baseline_rel)
        after = {rel: measure(frozen_root, rel)[0] for rel in READ_SET}
        assert before == after, "a read-set file changed during the run"
        results.append(f"preservation: the {len(READ_SET)} read-set files are byte-identical before and after a run")

        # design §8 tamper controls
        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            tampered_root, _ = freezed_copy(fixture, control_dir, "tampered-baseline")
            victim = tampered_root / baseline_rel
            edited = json.loads(victim.read_text(encoding="utf-8"))
            edited["packet_sha256"] = "0" * 64
            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
            code, err, records = exercise(root=tampered_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_UNEVALUATED, "E2E-BASELINE"), (code, err, records)
        results.append("tamper baseline: exit 2 E2E-BASELINE (integrity digest mismatch), never a pass")

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            drifted_root, _ = freezed_copy(fixture, control_dir, "drifted-input")
            victim = drifted_root / D2_TYPED
            victim.write_text(victim.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            code, err, records = exercise(root=drifted_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_FAIL, "E2E-DIGEST"), (code, err, records)
        results.append("tamper read-set: exit 1 E2E-DIGEST naming the changed file")

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            scan_root, _ = freezed_copy(fixture, control_dir, "scan-disagreement")
            victim = scan_root / baseline_rel
            edited = json.loads(victim.read_text(encoding="utf-8"))
            edited["expected_scan"]["glossary_entries"] = 21
            edited["baseline_digest"] = baseline_digest(edited)
            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
            code, err, records = exercise(root=scan_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_UNEVALUATED, "E2E-BASELINE"), (code, err, records)
        results.append("tamper scan expectation: exit 2 E2E-BASELINE (a re-signed expectation is refused, not honoured)")

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            missing_root = Path(control_dir) / "missing"
            shutil.copytree(frozen_root, missing_root)
            (missing_root / D3_PACKET).unlink()
            code, err, records = exercise(root=missing_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_UNEVALUATED, "E2E-ARTIFACT"), (code, err, records)
        results.append("missing artifact: exit 2 E2E-ARTIFACT naming the unreadable path")

    print(
        f"selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0) plus "
        f"{len(results) - 1} controls:"
    )
    for line in results:
        print(f"  - {line}")
    return EXIT_PASS


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="exercise-handoff-e2e.py",
        description=(
            "Assemble a handoff packet from the live D2/D3 drill artifacts and validate it through "
            "tools/gates/handoff-packet-check.py in an isolated copy."
        ),
    )
    parser.add_argument("--selftest", action="store_true", help="run the positive run and the control matrix")
    parser.add_argument("--root", metavar="DIR", help="alternate repo root holding the read set")
    parser.add_argument("--baseline", metavar="PATH", help=f"baseline override (default {BASELINE_DEFAULT})")
    parser.add_argument("--keep", metavar="DIR", help="keep the isolated packet directory at DIR")
    parser.add_argument("--json", action="store_true", help="print a receipt document on stdout")
    parser.add_argument("--freeze", metavar="DIR", help="(re)write the frozen baseline into DIR, printing diffs")
    parser.add_argument("--quiet", action="store_true", help="print only the summary line")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve() if args.root else ROOT
    if args.selftest:
        return selftest()

    if args.freeze:
        try:
            baseline, previous, diff, freeze_lines = freeze(root, args.freeze)
        except (Unevaluatable, Failed) as exc:
            print(f"could not freeze: {getattr(exc, 'code', 'E2E-DATA')} {exc}")
            return EXIT_UNEVALUATED if isinstance(exc, Unevaluatable) else EXIT_FAIL
        if not args.quiet:
            for line in freeze_lines:
                print(line)
            for line in diff:
                print(f"  changed: {line}")
        print(f"{'re-froze' if previous else 'froze'} {args.freeze}: packet sha256 {baseline['packet_sha256']}")
        return EXIT_PASS

    code, err, records = exercise(root=root, baseline_rel=args.baseline or BASELINE_DEFAULT)
    if not args.quiet:
        for item in records:
            print(f"{'OK  ' if item['ok'] else 'FAIL'} {item['check']}: {item['detail']}")
    scan = next((item["detail"] for item in records if item["check"] == "gate-scan"), "gate not reached")
    packet_sha = next((item["detail"] for item in records if item["check"] == "frozen-packet"), "")
    matches = re.search(r"([0-9a-f]{64})", packet_sha)
    fields = re.search(r"fields=(\d+/\d+)", scan)
    glossary = re.search(r"glossary-entries=(\d+)", scan)
    findings = re.search(r"findings=(\d+)", scan)
    print(
        f"handoff-e2e: exit={code} fields={fields.group(1) if fields else '?'} "
        f"glossary={glossary.group(1) if glossary else '?'}/20 findings={findings.group(1) if findings else '?'} "
        f"packet_sha256={matches.group(1) if matches else '(not assembled)'}"
    )
    if err and not args.quiet:
        print(f"handoff-e2e: {err}: {records[-1]['detail'] if records else ''}")
    if args.json:
        receipt = {
            "profile": PROFILE,
            "root": str(root),
            "baseline": args.baseline or BASELINE_DEFAULT,
            "exit": code,
            "code": err,
            "checks": records,
        }
        print(json.dumps(receipt, indent=1, sort_keys=True, ensure_ascii=False))
    return code


if __name__ == "__main__":
    sys.exit(main())
