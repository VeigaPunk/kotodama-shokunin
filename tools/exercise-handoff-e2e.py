#!/usr/bin/env python3
"""exercise-handoff-e2e — kotodama-shokunin handoff-e2e exercise (v1/v2/v3 profiles, R20-D05..D12).

Assembles a world-bible handoff packet from the live drill artifacts — no
hand-written packet body, every field derived from bytes on disk — copies the
assembled packet (and, from v3, its machine twin) into an isolated directory
outside the repository, and validates it there through
`tools/gates/handoff-packet-check.py` run from that foreign working directory.

Profiles (R20 design.md §6):

    python3 tools/exercise-handoff-e2e.py                      # v1 path (round-11 baseline) — unchanged
    python3 tools/exercise-handoff-e2e.py --profile v2         # v2 path (round-15 surfaces) — unchanged
    python3 tools/exercise-handoff-e2e.py --profile v3         # assemble -> links -> uncertainty -> gate -> v3 baseline
    python3 tools/exercise-handoff-e2e.py --profile v3 --selftest
    python3 tools/exercise-handoff-e2e.py --profile v3 --root DIR --baseline PATH

- **v1** (default) is the round-11 exercise (design.md R11-O01 §2/§3/§5/§6/§8/§9/§10)
  preserved byte-for-byte in behaviour: 21-file read set, the D2/D3 dual-drill
  packet, `reports/round-11/handoff/expected.json`. The default stays v1 so the
  filed round-11 path is not re-pointed.
- **v2** verifies the filed round-15 surfaces without re-rendering them:
  `reports/round-15/handoff/packet-v2-05.{md,yml}` digest-pinned, the shape gate
  over the Markdown, `tools/harness/packet_uncertainty.py` (15 claims) and
  `tools/harness/packet_links.py` (50/50 links) over the machine twin. The one
  pre-existing round-16 drift (the v2 packet's manifest pins the pre-round-16
  `tools/harness/packet_links.py`) is named in the receipt, never hidden: the
  link leg passes with `--no-digests`, and the digest leg's only tolerated
  finding is the named allowance row.
- **v3** extends the exercise to the D2/D3/D4 triple drill with the round-15
  v2 semantics and the round-17/18 D4 tree: the 15 v2 claim rows and 34 v2 edge
  rows are carried from `reports/round-15/handoff/packet-v2-05.yml` with
  subset-equality controls, twelve D4 rows enter the ledger from
  `reports/round-20/handoff/claims-map.md`, the D4 coupling-edge families are
  atomic rows with claim back-links, and the machine twin — re-parsed from the
  delivered Markdown — is judged by both harness validators against live repo
  bytes. Renderer 3.1.x restores declared_in and full edge text; its current
  baseline is under `reports/round-22/handoff/declared-in-r2/` (3.1.1, final
  combined-projector pins). The first round-22 `declared-in/` row and the filed
  round-20 3.0.0 baseline stay untouched.

Read sets

  v1: corpus/knowledge/synthesis/worldbible-integration-contract.md §1/§4;
      examples/culture-d3/{packet.json,packet.gates.yml,controls.json,expected.json}
      and its four components; examples/culture-d2/{packet.d2.yml,typed-labels.d2.yml};
      the four closed round-6 source ledgers; reports/round-6/parent-reconciliation.json;
      the gate and the four tools it names (21 files).
  v2: adds reports/round-15/handoff/packet-v2-05.{md,yml} and the two harness
      validators; the v2 baseline is reports/round-15/handoff/expected.json.
  v3: v1's 21 files, the v2 twins, the four D2 component inputs the D2
      projector's selftest fixture copies, the twelve D4 components, the D4
      tree (packet.d4.yml, packet.d4.typed.yml, typed-labels.d4.yml,
      expected-holds.json, brief.md, ASSEMBLY.md), the two D4 tools, the two D4
      adapter gates, the D4 reader gate, the four round-18 D4 receipts the D4
      claims ground in (holds.md, determinism.md, manifest.md, replay.md), the
      two harness validators, reports/round-20/handoff/claims-map.md (the D4
      rows' copy surface) and reports/round-19/validation.json (a D4-CL08 link
      target) — 58 files.

Assertions the v3 run makes

  1. read-set digests match the frozen v3 baseline (drift names the file);
  2. preflight: 16 fields, non-canon marker, licensed glossary vocabulary, no
     floating version, and the uncertainty/link grammar below;
  3. v2-subset equality: the 15 v2 claims parsed out of the v3 ledger are
     identical (kind, evidence_status, status, basis, links) to the v2 packet's
     rows after whitespace normalization; the 34 v2 edge mappings are identical
     in Markdown and twin, including declared_in and untruncated mechanism and
     limits — any drift is `E2E-DIGEST`;
  4. every claim row carries an uncertainty status in the licensed vocabulary
     and a unique, non-placeholder basis in the clause grammar (`grounding:`
     always; `restriction:` iff partial; `open:` + `owner:` iff unresolved),
     and every unresolved row is routed in open_questions;
  5. every claim row carries links; every link is a `path#token` spec that
     `tools/harness/packet_links.py` resolves against live bytes (exit 0, zero
     findings, every link resolved);
  6. the uncertainty census equals the declared/landed state and
     `packet_uncertainty.py --require-oq` exits 0 with zero findings;
  7. the shape gate over the isolated copy exits 0 with
     `fields=16/16 glossary-entries=20 findings=0`;
  8. the D4 legs this run can honestly run: `assemble-culture-d4.py --check`,
     `assemble-d4-typed.py --check`, `d2-typed-labels.py --selftest` (the D2
     byte-identity control) and `assemble-d4-typed.py --selftest` (the
     mirror-without-D2 run that keys D4-CL08);
  9. the frozen packet and twin digests, the claim-id list and the glossary id
     set; 10. preservation — no read-set file changes while the run runs.

Exit codes (stable messages, no traceback): 0 clean; 1 mismatch —
`E2E-DIGEST`, `E2E-COUNT`, `E2E-GATE`, `E2E-SCAN`, `E2E-UNC` (uncertainty
findings), `E2E-LINK` (link findings); 2 could-not-evaluate — `E2E-ARTIFACT`
(missing/unreadable read-set file), `E2E-BASELINE` (absent or edited baseline),
`E2E-DATA` (malformed input). Writes go only to a fresh directory under
`TMPDIR` (plus `--freeze DIR`); the read set is never modified, there is no
network access, and the tool is stdlib-only (the D2/D4 YAML packets are read
as bytes with id-level regex extraction, never through a third-party YAML
loader; the JSON-formatted projections are loaded with `json`).
"""

import argparse
import datetime
import hashlib
import json
import re
import runpy
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

EXIT_PASS = 0
EXIT_FAIL = 1
EXIT_UNEVALUATED = 2

ROOT = Path(__file__).resolve().parents[1]

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

D4_PACKET = "examples/culture-d4/packet.d4.yml"
D4_TYPED_PACKET = "examples/culture-d4/packet.d4.typed.yml"
D4_TYPED_LABELS = "examples/culture-d4/typed-labels.d4.yml"
D4_HOLDS = "examples/culture-d4/expected-holds.json"
D4_BRIEF = "examples/culture-d4/brief.md"
D4_ASSEMBLY = "examples/culture-d4/ASSEMBLY.md"
D4_COMPONENTS = (
    "examples/culture-d4/components/01-brief.yml",
    "examples/culture-d4/components/02-phonology.yml",
    "examples/culture-d4/components/03-orthography.yml",
    "examples/culture-d4/components/04-lexicon.yml",
    "examples/culture-d4/components/05-naming.yml",
    "examples/culture-d4/components/06-myth.yml",
    "examples/culture-d4/components/07-symbolism.yml",
    "examples/culture-d4/components/08-eras.yml",
    "examples/culture-d4/components/09-costumes.yml",
    "examples/culture-d4/components/10-ritual-calendar.yml",
    "examples/culture-d4/components/11-contact-history.yml",
    "examples/culture-d4/components/12-provenance.yml",
)
D4_ASSEMBLER = "tools/assemble-culture-d4.py"
D4_TYPED_TOOL = "tools/assemble-d4-typed.py"
D4_TYPED_GATE = "tools/gates/d4-typed-labels-check-gate.py"
D4_ASSEMBLY_GATE = "tools/gates/d4-assembly-check-gate.py"
D4_READER = "tools/gates/costume-era-consistency-gate.py"
D4_RECEIPTS = (
    "reports/round-18/d4/holds.md",
    "reports/round-18/d4/determinism.md",
    "reports/round-18/d4/manifest.md",
    "reports/round-18/d4/replay.md",
)
UNCERTAINTY_TOOL = "tools/harness/packet_uncertainty.py"
LINKS_TOOL = "tools/harness/packet_links.py"
HARNESS = (UNCERTAINTY_TOOL, LINKS_TOOL)
V2_PACKET_MD = "reports/round-15/handoff/packet-v2-05.md"
V2_PACKET_YML = "reports/round-15/handoff/packet-v2-05.yml"
V2_BASELINE = "reports/round-15/handoff/expected.json"
CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"

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

# Contract §6 claim kinds, plus the screening-statement note the design allows.
CLAIM_KINDS = (
    "real-world reference",
    "generative rule",
    "candidate world-fact",
    "attributed in-world belief",
    "designer interpretation",
    "screening statement",
)

# v2-design §2.2: exactly these three tokens, case-sensitive lowercase.
UNCERTAINTY_STATUSES = ("supported", "partial", "unresolved")
UNCERTAINTY_MIN_BASIS = 40

PLACEHOLDERS = {
    "", "-", "--", "—", "–", "n/a", "na", "n.a.", "tbd", "t.b.d.", "todo",
    "unknown", "(to-verify)", "to-verify", "?",
}
ETYM_STATUSES = ("attested", "reconstructed", "constructed", "contested", "unknown")

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

LEDGER_HEADER = (
    "claim_id", "kind", "evidence_status", "uncertainty_status", "uncertainty_basis",
    "links", "statement",
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
# shared helpers
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
    """Top-level `name:` block of the YAML-subset packets — a block splitter, not a loader."""
    match = re.search(rf"^{name}:\n(.*?)(?=^[A-Za-z_][A-Za-z0-9_]*:\s*$|\Z)", text, re.M | re.S)
    if not match:
        raise ArtifactError(f"section `{name}` not found — the packet shape changed")
    return match.group(1)


def yaml_entry(block, entry_id):
    """Id-level extraction of one `- id: "X"` entry inside a YAML block."""
    match = re.search(rf'^\s*-\s*\n\s*id:\s*"{re.escape(entry_id)}"\n(.*?)(?=^\s*-\s*\n\s*id:|\Z)', block, re.M | re.S)
    if not match:
        raise ArtifactError(f"record {entry_id} not found — the packet shape changed")
    return dict(re.findall(r'^\s{4}([a-z_]+):\s*"([^"]*)"', match.group(1), re.M))


def yaml_records(block):
    """Every `- id: "X"` entry of a YAML block as a dict of its 4-space quoted scalars."""
    records = []
    for part in re.split(r"^\s*-\s*$", block, flags=re.M)[1:]:
        fields = dict(re.findall(r'^\s{4}([a-z_]+):\s*"([^"]*)"', part, re.M))
        if fields.get("id"):
            records.append(fields)
    return records


def top_level_keys(text):
    return re.findall(r"^([A-Za-z_][A-Za-z0-9_]*):", text, re.M)


def extract_field_values(text):
    """Field values as the exercise emits them: `## field` bodies and `| field | value |` rows."""
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
    """Field-name tokens carried by headings that are not the bare field name itself."""
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


def mutated(packet, anchor, replacement, count=1):
    if anchor not in packet:
        raise MissingArtifact(f"selftest control anchor not found: {anchor!r}")
    return packet.replace(anchor, replacement, count)


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


# ==========================================================================
# v1 profile — the round-11 exercise, preserved (default profile)
# ==========================================================================

V1_PROFILE = "kotodama-handoff-e2e/1"
V1_PACKET_ID = "kotodama.handoff.d2d3-e2e"
V1_PACKET_VERSION = "1.0.0"
V1_BASELINE_DEFAULT = "reports/round-11/handoff/expected.json"
V1_FROZEN_DIR_DEFAULT = "reports/round-11/handoff"
V1_READ_SET = (
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
V1_DECLARED = {
    "expected_exit": EXIT_PASS,
    "expected_finding_ids": [],
    "expected_scan": {"fields": "16/16", "glossary_entries": 20, "findings": 0},
}
V1_DECLARED_EXPECTATION = (
    "exit 0 / findings [] fixed before implementation; hashes measured from bytes, never generated "
    "from a printed verdict"
)
V1_BASELINE_LIMITS = (
    "pins computational inputs only; not lore acceptance, not canon, not completion of the round arc; "
    "documentation surfaces excluded"
)
V1_SCALAR_FIELDS = (
    "packet_id", "packet_version", "contract_ref", "producer", "recipient", "request_ref",
    "baseline_bible_ref", "subject_refs", "scope",
)
V1_SECTION_FIELDS = (
    "artifact_manifest", "dependency_manifest", "claim_ledger", "coupling_edges",
    "requested_decisions", "validation", "open_questions",
)


def v1_mine_contract(root):
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


def v1_gate_field_names(root):
    text = read_text(root, GATE)
    match = re.search(r"^FIELD_NAMES = \(\n(.*?)^\)", text, re.M | re.S)
    if not match:
        raise ArtifactError(f"{GATE}: could not read the FIELD_NAMES tuple")
    return tuple(re.findall(r'"([a-z_]+)"', match.group(1)))


def v1_mine_d2(root):
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
        "lineage": yaml_entry(blocks["lexicon"], "L-04"),
        "sky_holder": yaml_entry(blocks["pantheon"], "PAN-01"),
        "era": yaml_entry(blocks["era_records"], "ER-01"),
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


def v1_mine_d3(root):
    obj = json_file(root, D3_PACKET)
    missing = [key for key in D3_REQUIRED if key not in obj]
    if missing:
        raise ArtifactError(f"{D3_PACKET}: missing top-level keys {missing}")
    facts = {key: obj[key] for key in D3_REQUIRED}
    facts["components"] = dict(obj["assembly"].get("source_sha256", {}))
    if not facts["components"] or not facts["lexicon"] or not facts["bridges"]:
        raise ArtifactError(f"{D3_PACKET}: assembly digests, lexicon or bridges are empty")
    return facts


def v1_mine_typed_labels(root):
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


def v1_verify_component_digests(root, d2, d3):
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


def v1_derived_etymology(entry, sound_change):
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


def v1_build_glossary(d3):
    lexicon = d3["lexicon"]
    expected = V1_DECLARED["expected_scan"]["glossary_entries"]
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
                v1_derived_etymology(entry, changes[0]),
            )
        )
    return rows


def v1_manifest_rows(root, digests, sizes, d2, d3, typed, contract, d3_expected, d3_controls, glossary):
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
    for index, rel in enumerate(V1_READ_SET, start=1):
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


def v1_build_packet(root, d2, d3, typed, contract, digests, sizes, glossary, fields_supplied):
    d2_component_count = len(d2["components"])
    d3_component_count = len(d3["components"])
    rows = v1_manifest_rows(root, digests, sizes, d2, d3, typed, contract, json_file(root, D3_EXPECTED), json_file(root, D3_CONTROLS), glossary)

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
    add(f"| packet_id | {V1_PACKET_ID} |")
    add(f"| packet_version | {V1_PACKET_VERSION} (pure function of the pinned read set; no wall-clock content) |")
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
        f"checks digest presence only, this exercise checks equality (design §1). {len(V1_READ_SET)} read-set "
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
    add(f"- profile {V1_PROFILE} (this exercise; renderer revision {V1_PACKET_VERSION})")
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
        f"- read set: {len(V1_READ_SET)} files re-measured (`sha256`, same run) against the frozen baseline's "
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
        f"exit {V1_DECLARED['expected_exit']}, fields={V1_DECLARED['expected_scan']['fields']}, "
        f"glossary-entries={V1_DECLARED['expected_scan']['glossary_entries']}, "
        f"findings={V1_DECLARED['expected_scan']['findings']}; the observed values are compared against the frozen "
        f"baseline in `{V1_BASELINE_DEFAULT}`, whose run log records the verdict of the run it froze"
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


def v1_preflight(text):
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
    if len(rows) != V1_DECLARED["expected_scan"]["glossary_entries"]:
        problems.append(
            f"glossary payload holds {len(rows)} rows, expected {V1_DECLARED['expected_scan']['glossary_entries']}"
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


class V1Assembly:
    def __init__(self, root):
        self.root = root
        self.digests = {}
        self.sizes = {}
        for rel in V1_READ_SET:
            digest, size = measure(root, rel)
            self.digests[rel] = digest
            self.sizes[rel] = size
        self.contract = v1_mine_contract(root)
        self.gate_fields = v1_gate_field_names(root)
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
        self.d2 = v1_mine_d2(root)
        self.d3 = v1_mine_d3(root)
        self.typed = v1_mine_typed_labels(root)
        self.component_checked, self.component_matched = v1_verify_component_digests(root, self.d2, self.d3)
        self.glossary = v1_build_glossary(self.d3)
        self.packet = v1_build_packet(
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
        if checked != len(V1_READ_SET):
            raise Failed("E2E-COUNT", f"manifest re-measured {checked} files, expected {len(V1_READ_SET)}")

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


def v1_baseline_payload(baseline):
    return {key: value for key, value in baseline.items() if key != "baseline_digest"}


def v1_baseline_digest(baseline):
    return sha256_text(json.dumps(v1_baseline_payload(baseline), sort_keys=True, separators=(",", ":"), ensure_ascii=False))


def v1_load_baseline(root, baseline_rel):
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
    if baseline["profile"] != V1_PROFILE:
        raise BaselineError(f"frozen baseline profile {baseline['profile']!r} is not {V1_PROFILE!r}")
    if baseline.get("baseline_digest") != v1_baseline_digest(baseline):
        raise BaselineError(
            "baseline integrity digest mismatch — the baseline file was edited without re-freezing "
            "(re-freeze with --freeze DIR and read the diff it prints)"
        )
    for key in ("expected_exit", "expected_finding_ids", "expected_scan"):
        if baseline[key] != V1_DECLARED[key]:
            raise BaselineError(f"baseline declares {key}={baseline[key]!r}, the exercise declares {V1_DECLARED[key]!r}")
    return path, baseline


def v1_exercise(root=ROOT, baseline_rel=V1_BASELINE_DEFAULT):
    """Run the v1 exercise; return (exit code, code-or-None, records)."""
    records = []

    def record(name, ok, detail=""):
        records.append({"check": name, "ok": bool(ok), "detail": detail})

    try:
        baseline_path, baseline = v1_load_baseline(root, baseline_rel)
        snapshot_before = {rel: measure(root, rel)[0] for rel in V1_READ_SET}
        assembly = V1Assembly(root)

        drifted = [
            rel for rel, digest in baseline["inputs"].items() if assembly.digests.get(rel) != digest
        ]
        if drifted:
            for rel in drifted:
                record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
            raise Failed("E2E-DIGEST", f"{len(drifted)} read-set file(s) changed since the baseline was frozen: {', '.join(drifted[:3])}")
        record("input-digest", True, f"{len(V1_READ_SET)} read-set digests match the frozen baseline")

        problems = v1_preflight(assembly.packet)
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
            f"manifest digests equal bytes for {len(V1_READ_SET)} files",
        )

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

        snapshot_after = {rel: measure(root, rel)[0] for rel in V1_READ_SET}
        unchanged = snapshot_before == snapshot_after
        record(
            "preservation",
            unchanged,
            f"the {len(V1_READ_SET)} read-set files are byte-identical before and after the run"
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


def v1_freeze(root, target_dir):
    """Write the v1 frozen baseline (and the packet/run log beside it), printing diffs."""
    assembly = V1Assembly(root)
    problems = v1_preflight(assembly.packet)
    if problems:
        raise Failed("E2E-COUNT", f"refusing to freeze a packet that fails preflight: {problems[0]}")
    with tempfile.TemporaryDirectory(prefix="handoff-freeze-") as workdir:
        gate = assembly.run_gate(workdir)
    if gate["exit"] != V1_DECLARED["expected_exit"] or gate["findings"]:
        raise Failed("E2E-GATE", f"refusing to freeze: gate exit {gate['exit']} with findings {gate['findings']}")
    expected_scan = {
        "fields": f"{gate['fields']}/{gate['fields_total']}",
        "glossary_entries": gate["glossary_entries"],
        "findings": gate["findings_count"],
    }
    if expected_scan != V1_DECLARED["expected_scan"]:
        raise Failed("E2E-SCAN", f"refusing to freeze: observed scan {expected_scan} != declared {V1_DECLARED['expected_scan']}")

    baseline = {
        "profile": V1_PROFILE,
        "packet_id": V1_PACKET_ID,
        "packet_version": V1_PACKET_VERSION,
        "frozen_at": datetime.date.today().isoformat(),
        "frozen_by": "tools/exercise-handoff-e2e.py",
        **V1_DECLARED,
        "packet_sha256": assembly.packet_sha256,
        "glossary_entry_ids": [row[0] for row in assembly.glossary],
        "inputs": {rel: assembly.digests[rel] for rel in V1_READ_SET},
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
        "declared_expectation": V1_DECLARED_EXPECTATION,
        "limits": V1_BASELINE_LIMITS,
    }
    baseline["baseline_digest"] = v1_baseline_digest(baseline)

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
        f"exercise: tools/exercise-handoff-e2e.py ({V1_PROFILE}, packet {V1_PACKET_ID} {V1_PACKET_VERSION})",
        f"gate: python3 {GATE} packet.md (isolated copy, foreign working directory)",
        f"gate verdict: exit {gate['exit']}, fields={gate['fields']}/{gate['fields_total']}, "
        f"glossary-entries={gate['glossary_entries']}, findings={gate['findings_count']}",
        f"packet sha256: {assembly.packet_sha256}",
        f"read set: {len(V1_READ_SET)} files measured; component digests {assembly.component_matched}/"
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
        f"read set: {len(V1_READ_SET)} files; component digests {assembly.component_matched}/{assembly.component_checked}",
    ]
    freeze_lines.extend(diff or ["no tracked value changed since the previous freeze"])
    (target / "freeze.txt").write_text("\n".join(freeze_lines) + "\n", encoding="utf-8")
    return baseline, previous, diff, freeze_lines


def v1_build_fixture_root(workdir):
    """A throwaway copy of every file the v1 exercise reads or re-measures, inside one temp dir."""
    fixture = Path(workdir) / "fixture"
    components = set(v1_mine_d2(ROOT)["components"]) | set(v1_mine_d3(ROOT)["components"])
    for rel in (*V1_READ_SET, GATE, *sorted(components)):
        source = ROOT / rel
        if not source.is_file():
            raise MissingArtifact(f"selftest fixture source missing: {rel}")
        target = fixture / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    return fixture


def v1_freezed_copy(fixture, workdir, name="frozen"):
    target = Path(workdir) / name
    shutil.copytree(fixture, target)
    baseline, _, _, _ = v1_freeze(target, target / V1_FROZEN_DIR_DEFAULT)
    return target, baseline


def v1_selftest():
    results = []
    with tempfile.TemporaryDirectory(prefix="handoff-selftest-") as workdir:
        fixture = v1_build_fixture_root(workdir)
        frozen_root, baseline = v1_freezed_copy(fixture, workdir, "frozen-root")
        baseline_rel = V1_FROZEN_DIR_DEFAULT + "/expected.json"

        code, err, records = v1_exercise(root=frozen_root, baseline_rel=baseline_rel)
        assert code == EXIT_PASS, [(r["check"], r["detail"]) for r in records if not r["ok"]]
        scan = next(r["detail"] for r in records if r["check"] == "gate-scan")
        assert "fields=16/16" in scan and "glossary-entries=20" in scan and "findings=0" in scan, scan
        results.append(f"positive: exit 0 — {scan}")

        run = subprocess.run(
            [sys.executable, str(ROOT / "tools/exercise-handoff-e2e.py"), "--root", str(frozen_root), "--quiet"],
            cwd=workdir,
            capture_output=True,
            text=True,
        )
        assert run.returncode == EXIT_PASS, (run.returncode, run.stdout, run.stderr)
        assert "handoff-e2e: exit=0" in run.stdout, run.stdout
        results.append("isolation: the CLI run from a foreign cwd exits 0 with the same scan")

        assembly = V1Assembly(frozen_root)
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

        dropped = "\n".join(
            line for line in packet.splitlines() if not line.startswith("| L20 |")
        ) + "\n"
        assert not any(name == "L20" for name, _ in glossary_rows(dropped)), "control anchor failed"
        assert any("holds 19 rows" in problem for problem in v1_preflight(dropped)), v1_preflight(dropped)
        results.append("malformed-07 dropped glossary row: the gate counts 19 rows silently; preflight fails closed")

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

        before = {rel: measure(frozen_root, rel)[0] for rel in V1_READ_SET}
        v1_exercise(root=frozen_root, baseline_rel=baseline_rel)
        after = {rel: measure(frozen_root, rel)[0] for rel in V1_READ_SET}
        assert before == after, "a read-set file changed during the run"
        results.append(f"preservation: the {len(V1_READ_SET)} read-set files are byte-identical before and after a run")

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            tampered_root, _ = v1_freezed_copy(fixture, control_dir, "tampered-baseline")
            victim = tampered_root / baseline_rel
            edited = json.loads(victim.read_text(encoding="utf-8"))
            edited["packet_sha256"] = "0" * 64
            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
            code, err, records = v1_exercise(root=tampered_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_UNEVALUATED, "E2E-BASELINE"), (code, err, records)
        results.append("tamper baseline: exit 2 E2E-BASELINE (integrity digest mismatch), never a pass")

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            drifted_root, _ = v1_freezed_copy(fixture, control_dir, "drifted-input")
            victim = drifted_root / D2_TYPED
            victim.write_text(victim.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            code, err, records = v1_exercise(root=drifted_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_FAIL, "E2E-DIGEST"), (code, err, records)
        results.append("tamper read-set: exit 1 E2E-DIGEST naming the changed file")

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            scan_root, _ = v1_freezed_copy(fixture, control_dir, "scan-disagreement")
            victim = scan_root / baseline_rel
            edited = json.loads(victim.read_text(encoding="utf-8"))
            edited["expected_scan"]["glossary_entries"] = 21
            edited["baseline_digest"] = v1_baseline_digest(edited)
            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
            code, err, records = v1_exercise(root=scan_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_UNEVALUATED, "E2E-BASELINE"), (code, err, records)
        results.append("tamper scan expectation: exit 2 E2E-BASELINE (a re-signed expectation is refused, not honoured)")

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            missing_root = Path(control_dir) / "missing"
            shutil.copytree(frozen_root, missing_root)
            (missing_root / D3_PACKET).unlink()
            code, err, records = v1_exercise(root=missing_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_UNEVALUATED, "E2E-ARTIFACT"), (code, err, records)
        results.append("missing artifact: exit 2 E2E-ARTIFACT naming the unreadable path")

    print(
        f"selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0) plus "
        f"{len(results) - 1} controls:"
    )
    for line in results:
        print(f"  - {line}")
    return EXIT_PASS


# ==========================================================================
# v2 profile — verify the filed round-15 surfaces without re-rendering them
# ==========================================================================

V2_PROFILE = "kotodama-handoff-v2/1"
# The v2 packet's own manifest pins tool bytes that have since moved. Two
# named, re-pinned-as-new-rows drifts are tolerated in the digest leg and
# reported; every other finding fails:
#   - tools/harness/packet_links.py — the round-16 harness fix (commit f30b6f8)
#   - tools/d2-typed-labels.py — the round-20 O-seat per-family alias change
#     (its D2 output stays byte-identical; the tool bytes are re-pinned as new
#     rows by the O seat's repin cascade)
V2_NAMED_DIGEST_DRIFT = (LINKS_TOOL, "tools/d2-typed-labels.py")


def v2_run_harness(root, tool, extra, workdir):
    tool_path = Path(root) / tool
    if not tool_path.is_file():
        raise MissingArtifact(f"harness tool not found: {tool}")
    arguments = list(extra)
    if tool == LINKS_TOOL:
        arguments.extend(["--repo-root", str(root)])
    run = subprocess.run(
        [sys.executable, str(tool_path), "--packet", str(Path(root) / V2_PACKET_YML), *arguments, "--json"],
        cwd=str(workdir),
        capture_output=True,
        text=True,
    )
    try:
        payload = json.loads(run.stdout)
    except json.JSONDecodeError as exc:
        raise Failed(
            "E2E-DATA",
            f"{tool} produced no JSON receipt (exit {run.returncode}): "
            f"{(run.stdout or run.stderr).strip()[:200]}",
        ) from exc
    return {"exit": run.returncode, "payload": payload}


def v2_verify(root=ROOT):
    """Verify the filed v2 packet twins and their verdicts; return (exit, code, records)."""
    records = []

    def record(name, ok, detail=""):
        records.append({"check": name, "ok": bool(ok), "detail": detail})

    try:
        baseline = json.loads(read_text(root, V2_BASELINE))
        if baseline.get("profile") != V2_PROFILE:
            raise BaselineError(f"{V2_BASELINE} profile {baseline.get('profile')!r} is not {V2_PROFILE!r}")

        for rel in (V2_PACKET_MD, V2_PACKET_YML):
            measured = measure(root, rel)[0]
            frozen = baseline["inputs"].get(rel)
            if measured != frozen:
                record("packet-digest", False, f"{rel}: live {measured[:12]}… vs v2 baseline {str(frozen)[:12]}…")
                raise Failed("E2E-DIGEST", f"{rel} differs from the v2 baseline pin")
        record("packet-digest", True, f"{V2_PACKET_MD} and {V2_PACKET_YML} match the v2 baseline pins")

        with tempfile.TemporaryDirectory(prefix="handoff-v2-") as workdir:
            isolated = Path(workdir) / "isolated"
            isolated.mkdir(parents=True, exist_ok=True)
            packet_text = read_text(root, V2_PACKET_MD)
            (isolated / "packet.md").write_text(packet_text, encoding="utf-8")
            run = subprocess.run(
                [sys.executable, str(Path(root) / GATE), "packet.md"],
                cwd=str(isolated),
                capture_output=True,
                text=True,
            )
            scan = re.search(r"^INFO scan: fields=(\d+)/(\d+) glossary-entries=(\d+) findings=(\d+)", run.stdout, re.M)
            if scan is None:
                raise Failed("E2E-DATA", f"the gate produced no scan line over {V2_PACKET_MD}")
            observed = {
                "fields": f"{scan.group(1)}/{scan.group(2)}",
                "glossary_entries": int(scan.group(3)),
                "findings": int(scan.group(4)),
            }
            if run.returncode != 0 or observed != baseline["expected_scan"]:
                record("gate", False, f"exit {run.returncode}, scan {observed}")
                raise Failed("E2E-GATE", f"the v2 gate run exited {run.returncode} with scan {observed}")
            record("gate", True, f"{V2_PACKET_MD}: exit 0, fields={observed['fields']} "
                                 f"glossary-entries={observed['glossary_entries']} findings={observed['findings']}")

            uncertainty = v2_run_harness(root, UNCERTAINTY_TOOL, ["--require-oq"], workdir)
            payload = uncertainty["payload"]
            if uncertainty["exit"] != 0 or payload.get("findings"):
                record("uncertainty", False, f"exit {uncertainty['exit']}, findings {payload.get('findings')}")
                raise Failed("E2E-UNC", f"the v2 uncertainty leg exited {uncertainty['exit']}")
            claims = payload.get("claims")
            if claims != baseline["census"]["claims"]:
                record("uncertainty", False, f"claims {claims} != baseline {baseline['census']['claims']}")
                raise Failed("E2E-COUNT", f"the v2 uncertainty census {claims} != {baseline['census']['claims']}")
            record("uncertainty", True, f"{UNCERTAINTY_TOOL}: exit 0, claims={claims}, findings 0 (--require-oq)")

            links_clean = v2_run_harness(root, LINKS_TOOL, ["--no-digests"], workdir)
            payload = links_clean["payload"]
            checked, resolved = payload.get("links_checked"), payload.get("resolved")
            if links_clean["exit"] != 0 or payload.get("findings") or checked != resolved:
                record("links", False, f"exit {links_clean['exit']}, {resolved}/{checked} resolved")
                raise Failed("E2E-LINK", f"the v2 link leg exited {links_clean['exit']}")
            if checked != baseline["links"]["links"] or resolved != baseline["links"]["resolved"]:
                record("links", False, f"{resolved}/{checked} != baseline {baseline['links']['resolved']}/{baseline['links']['links']}")
                raise Failed("E2E-COUNT", "the v2 link census differs from the v2 baseline")
            record("links", True, f"{LINKS_TOOL} --no-digests: exit 0, {resolved}/{checked} links resolved, findings 0")

            links_digests = v2_run_harness(root, LINKS_TOOL, [], workdir)
            payload = links_digests["payload"]
            tolerated, unexpected = [], []
            for finding in payload.get("findings", []):
                if finding.get("code") == "M-DIGEST-MISMATCH" and finding.get("subject") in V2_NAMED_DIGEST_DRIFT:
                    tolerated.append(finding)
                else:
                    unexpected.append(finding)
            if unexpected:
                record("links-digests", False, f"unexpected findings {unexpected[:2]}")
                raise Failed("E2E-LINK", f"the v2 digest leg reported unexpected findings: {unexpected[:2]}")
            record(
                "links-digests",
                True,
                f"{LINKS_TOOL} with digests: {len(tolerated)} named round-16 drift row(s) "
                f"({', '.join(f['subject'] for f in tolerated) or 'none'}), no other findings",
            )
        return EXIT_PASS, None, records

    except Failed as exc:
        record("verdict", False, str(exc))
        return EXIT_FAIL, exc.code, records
    except Unevaluatable as exc:
        record("verdict", False, str(exc))
        return EXIT_UNEVALUATED, exc.code if issubclass(type(exc), Unevaluatable) and getattr(type(exc), "code", None) else "E2E-DATA", records


# ==========================================================================
# v3 profile — the D2/D3/D4 triple drill with the v2 semantics
# ==========================================================================

V3_PROFILE = "kotodama-handoff-e2e/3"
V3_PACKET_ID = "kotodama.handoff.d2d3d4-e2e"
V3_PACKET_VERSION = "3.1.1"
V3_BASELINE_DEFAULT = "reports/round-28/pinsweep/v3-baseline-r28/expected.json"
V3_FROZEN_DIR_DEFAULT = "reports/round-28/pinsweep/v3-baseline-r28"
V3_READ_SET = (
    *V1_READ_SET,
    V2_PACKET_MD,
    V2_PACKET_YML,
    "examples/culture-d2/components/05-lexicon.yml",
    "examples/culture-d2/components/09-eras-calendar.yml",
    "examples/culture-d2/components/11-costumes.yml",
    "examples/culture-d2/components/12-rank-rules.yml",
    D4_PACKET,
    D4_TYPED_PACKET,
    D4_TYPED_LABELS,
    D4_HOLDS,
    D4_BRIEF,
    D4_ASSEMBLY,
    *D4_COMPONENTS,
    D4_ASSEMBLER,
    D4_TYPED_TOOL,
    D4_TYPED_GATE,
    D4_ASSEMBLY_GATE,
    D4_READER,
    *D4_RECEIPTS,
    *HARNESS,
    CLAIMS_MAP,
    "reports/round-19/validation.json",
)
V3_DECLARED = {
    "expected_exit": EXIT_PASS,
    "expected_finding_ids": [],
    "expected_scan": {"fields": "16/16", "glossary_entries": 20, "findings": 0},
    "expected_uncertainty_findings": 0,
    "expected_links_findings": 0,
    "expected_links_unresolved": 0,
}
V3_DECLARED_EXPECTATION = (
    "exit 0 / findings [] / uncertainty+links findings 0 with every link resolved, fixed before "
    "implementation; hashes measured from bytes, never generated from a printed verdict"
)
V3_BASELINE_LIMITS = (
    "pins computational inputs only; not lore acceptance, not canon, not completion of the round arc; "
    "documentation surfaces excluded"
)
# The D4-CL08 landed-form guard (design §4 rule 2 / m11): a `supported`
# D4-CL08 must carry the run witness in its basis, not only a statement.
V3_ALIAS_WITNESS_TOKENS = ("era_reconciliation", "12/12")

D4_SECTIONS = (
    "lexicon", "layers", "constructions", "cloth_sources", "pantheon", "roles", "motifs",
    "narratives", "calendar", "festivals", "rites", "symbols", "materials", "costumes",
    "rank_rules", "era_records", "names", "cross_culture_review", "form_slots",
    "provenance", "contact", "routes", "era_tags", "assembly",
)


def v3_mine_d2(root):
    """The v1 D2 mining plus the v3 additions: per-record coupling notes and the
    record-id index the edges and the twin resolve against."""
    text = read_text(root, D2_PACKET)
    base = v1_mine_d2(root)
    coupling = []
    last_id = None
    for line in text.splitlines():
        found = re.match(r'^\s*id:\s*"([^"]+)"', line)
        if found:
            last_id = found.group(1)
        if "coupling_note:" in line:
            note = re.search(r'coupling_note:\s*"(.*)"\s*$', line)
            coupling.append((last_id, note.group(1) if note else ""))
    record_ids = sorted(set(re.findall(r'^\s*id:\s*"([^"]+)"', text, re.M)))
    # anchors the v2 packet's D2 edges already resolved against this file
    for anchor in ("A-03", "R-01", "R-03", "SYN-23"):
        if re.search(rf"(?<![A-Za-z0-9_-]){re.escape(anchor)}(?![A-Za-z0-9_-])", text):
            record_ids.append(anchor)
    # the contract rules are carried as id tokens in the packet's own prose
    record_ids.extend(sorted(set(re.findall(r"RG-\d\d", text))))
    cit_ids = sorted(set(re.findall(r'"CIT-\d\d"', text)))
    base.update({
        "coupling": coupling,
        "record_ids": sorted(set(record_ids)),
        "cit_ids": cit_ids,
    })
    return base


D3_ID_KEYS = (
    "lexicon", "names", "eras", "beliefs", "symbols", "costumes", "objects", "materials",
    "utterances", "bridges", "references", "rank_rules", "sound_changes", "speech_rules",
)


def v3_mine_d3(root):
    facts = v1_mine_d3(root)
    obj = json_file(root, D3_PACKET)
    record_ids = []
    for key in D3_ID_KEYS:
        value = obj.get(key)
        if isinstance(value, list):
            record_ids.extend(str(item["id"]) for item in value if isinstance(item, dict) and item.get("id"))
        elif isinstance(value, dict) and value.get("id"):
            record_ids.append(str(value["id"]))
    naming = obj.get("naming_rule")
    if isinstance(naming, dict) and naming.get("id"):
        record_ids.append(str(naming["id"]))
    facts["record_ids"] = sorted(set(record_ids))
    return facts


def v3_mine_d4(root):
    text = read_text(root, D4_PACKET)
    blocks = {name: section(text, name) for name in D4_SECTIONS}
    records = {name: yaml_records(blocks[name]) for name in D4_SECTIONS if name != "assembly"}
    counts = {name: len(rows) for name, rows in records.items()}
    for label in ("lexicon", "symbols", "costumes", "rank_rules", "era_records", "names", "contact"):
        if not counts.get(label):
            raise ArtifactError(f"{D4_PACKET}: mined `{label}` is empty — refusing to emit a placeholder field")
    assembly = blocks["assembly"]
    components = dict(re.findall(r'^\s{4}"([^"]+)":\s*"([0-9a-f]{64})"', assembly, re.M))
    if not components:
        raise ArtifactError(f"{D4_PACKET}: no `assembly.source_sha256` component digests found")
    pins = {}
    for key in ("assembler_sha256", "reader_sha256", "serializer_sha256"):
        found = re.search(rf'^\s*{key}:\s*"([0-9a-f]{{64}})"', assembly, re.M)
        if found:
            pins[key] = found.group(1)
    era_tags = re.findall(r'^\s*-\s*"(E\d)"', blocks["era_tags"], re.M)
    name = re.search(r'^name:\s*"([^"]*)"', text, re.M)
    if not name:
        raise ArtifactError(f"{D4_PACKET}: no `name:` line found")
    record_ids = sorted(set(re.findall(r'^\s*id:\s*"([^"]+)"', text, re.M)))
    # value tokens the D4 edge families name: era tags, rank names, layer names
    rank_names = sorted(set(re.findall(r'^\s{6}- "([a-z][a-z-]*)"', blocks["rank_rules"], re.M)))
    layer_names = sorted({row.get("name", "") for row in records["layers"]} - {""})
    index_extra = sorted(set(era_tags) | set(rank_names) | set(layer_names))
    witness = {}
    for section_name, entry_id in (("lexicon", "L-01"), ("symbols", "SYM-01"), ("costumes", "GAR-01"),
                                   ("rank_rules", "RK-01"), ("era_records", "ER-01"), ("contact", "CT-01"),
                                   ("names", "NM-01"), ("materials", "CMAT-01")):
        row = next((item for item in records[section_name] if item["id"] == entry_id), None)
        if row is None:
            raise ArtifactError(f"{D4_PACKET}: witness {entry_id} not found in `{section_name}`")
        witness[entry_id] = row
    # live relation tables (the D4 edge families, measured from the bytes)
    costume_materials = [(row["id"], row["material_ref"]) for row in records["costumes"] if row.get("material_ref")]
    form_slots = [(row["id"], row["owner"]) for row in records["form_slots"] if row.get("owner")]
    garment_slots = [(row["form_slot"], row["id"]) for row in records["costumes"] if row.get("form_slot")]
    era_garments = {}
    for row in records["costumes"]:
        era_garments.setdefault(row.get("era", ""), []).append(row["id"])
    contact_loans = []
    for part in re.split(r"^\s*-\s*$", blocks["contact"], flags=re.M)[1:]:
        entry = dict(re.findall(r'^\s{4}([a-z_]+):\s*"([^"]*)"', part, re.M))
        loans = re.findall(r'^\s{6}- "(L-\d\d)"', part, re.M)
        if entry.get("id") and loans:
            contact_loans.append((entry["id"], entry.get("name", ""), loans))
    rank_ranks = []
    for part in re.split(r"^\s*-\s*$", blocks["rank_rules"], flags=re.M)[1:]:
        entry = dict(re.findall(r'^\s{4}([a-z_]+):\s*"([^"]*)"', part, re.M))
        ranks = re.findall(r'^\s{6}- "([a-z][a-z-]*)"', part, re.M)
        if entry.get("id") and ranks:
            rank_ranks.append((entry["id"], ranks))
    term_to_lexeme = {}
    for row in records["lexicon"]:
        term_to_lexeme.setdefault(row.get("term", ""), row["id"])
    name_formations = []
    for part in re.split(r"^\s*-\s*$", blocks["names"], flags=re.M)[1:]:
        entry = dict(re.findall(r'^\s{4}([a-z_]+):\s*"([^"]*)"', part, re.M))
        bases = re.findall(r'^\s{8}- "([^"]+)"', part, re.M)
        rule = re.search(r'^\s{6}rule:\s*"([^"]+)"', part, re.M)
        if entry.get("id") and (bases or rule):
            name_formations.append((entry["id"], bases, rule.group(1) if rule else None))
    symbol_eras = [(row["id"], row.get("era", ""), row.get("register", "")) for row in records["symbols"]]
    festival_units = [row["id"] for row in records["festivals"]] + [row["id"] for row in records["rites"]]
    route_names = {row.get("route", ""): row["id"] for row in records["routes"]}
    layer_for_lexeme = []
    for row in records["lexicon"]:
        layer = row.get("loan_layer") or row.get("layer") or ""
        if row.get("route") == "borrowed" and layer:
            layer_for_lexeme.append((row["id"], layer))
    borrowed = len(re.findall(r'^\s{4}route:\s*"borrowed"', blocks["lexicon"], re.M))
    return {
        "name": name.group(1),
        "counts": counts,
        "records": records,
        "era_tags": era_tags,
        "components": components,
        "pins": pins,
        "record_ids": record_ids,
        "index_extra": index_extra,
        "witness": witness,
        "costume_materials": costume_materials,
        "form_slots": form_slots,
        "garment_slots": garment_slots,
        "era_garments": era_garments,
        "contact_loans": contact_loans,
        "rank_ranks": rank_ranks,
        "term_to_lexeme": term_to_lexeme,
        "name_formations": name_formations,
        "symbol_eras": symbol_eras,
        "festival_units": festival_units,
        "route_names": route_names,
        "layer_for_lexeme": layer_for_lexeme,
        "borrowed": borrowed,
        "to_verify_lines": sum(1 for line in text.splitlines() if "to-verify" in line),
    }


def v3_mine_d4_typed(root):
    text = read_text(root, D4_TYPED_PACKET)
    typed_assembly = section(text, "typed_assembly")
    pipeline_counts = section(text, "pipeline_counts")
    channel = section(text, "typed_channel")
    generator = re.search(r'^\s*generator:\s*"([^"]*)"', typed_assembly, re.M)
    projection = re.search(r'^\s*projection:\s*"([^"]*)"', typed_assembly, re.M)
    counts = {key: int(found.group(1)) for key, found in (
        (name, re.search(rf'^\s*{name}:\s*(\d+)\s*$', pipeline_counts, re.M))
        for name in ("hold", "note", "fail")
    ) if found}
    if generator is None or projection is None or "hold" not in counts:
        raise ArtifactError(f"{D4_TYPED_PACKET}: typed_assembly/pipeline_counts shape changed")
    return {
        "generator": generator.group(1),
        "projection": projection.group(1),
        "counts": counts,
        "channel_rows": len(re.findall(r'^\s*record:\s*"', channel, re.M)),
    }


def v3_mine_d4_labels(root):
    obj = json_file(root, D4_TYPED_LABELS)
    missing = [key for key in ("coverage", "era_reconciliation", "rank_rules", "assembly") if key not in obj]
    if missing:
        raise ArtifactError(f"{D4_TYPED_LABELS}: missing top-level keys {missing}")
    coverage = obj["coverage"]
    assembly = obj["assembly"]
    era = obj["era_reconciliation"]
    return {
        "labels": coverage.get("typed_labels"),
        "by_kind": coverage.get("labels_by_kind", {}),
        "findings_total": coverage.get("findings_total"),
        "hold_or_fail": coverage.get("findings_hold_or_fail"),
        "unresolved_items": coverage.get("rank_rules_unresolved_items"),
        "quarantine": coverage.get("rank_quarantine_handles"),
        "conflicts": coverage.get("conflicts"),
        "reconciliations": coverage.get("reconciliation_records"),
        "alias_rows": len(era.get("alias_rows", [])),
        "alias_basis": era.get("basis", []),
        "verdicts": len(era.get("verdicts", [])),
        "packet_sha256": assembly.get("packet_sha256"),
        "reader_sha256": assembly.get("reader_sha256"),
    }


def v3_mine_d4_holds(root):
    obj = json_file(root, D4_HOLDS)
    missing = [key for key in ("counts", "holds", "packet_sha256", "projection_sha256", "projector_sha256") if key not in obj]
    if missing:
        raise ArtifactError(f"{D4_HOLDS}: missing top-level keys {missing}")
    counts = obj["counts"]
    return {
        "hold": counts.get("hold"),
        "note": counts.get("note"),
        "fail": counts.get("fail"),
        "rows": len(obj["holds"]) if isinstance(obj["holds"], list) else None,
        "notes": len(obj.get("notes", [])) if isinstance(obj.get("notes"), list) else None,
        "packet_sha256": obj["packet_sha256"],
        "projection_sha256": obj["projection_sha256"],
        "projector_sha256": obj["projector_sha256"],
    }


def v3_verify_component_digests(root, d2, d3, d4):
    checked = matched = 0
    for label, components in (("D2", d2["components"]), ("D3", d3["components"]), ("D4", d4["components"])):
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


def v3_verify_d4_pins(root, d4, d4_labels, d4_holds):
    """Every pin the D4 tree states about itself, re-measured against live bytes."""
    checked = matched = 0

    def check(label, recorded, rel):
        nonlocal checked, matched
        if recorded is None:
            raise ArtifactError(f"{label}: pin absent — the D4 tree shape changed")
        checked += 1
        measured, _ = measure(root, rel)
        if measured == recorded:
            matched += 1
        else:
            raise Failed(
                "E2E-DIGEST",
                f"{label}: the tree recorded {recorded[:12]}… for {rel} but the bytes measure "
                f"{measured[:12]}…",
            )

    check(f"{D4_PACKET} assembly.assembler_sha256", d4["pins"].get("assembler_sha256"), D4_ASSEMBLER)
    check(f"{D4_PACKET} assembly.reader_sha256", d4["pins"].get("reader_sha256"), D4_READER)
    check(f"{D4_PACKET} assembly.serializer_sha256", d4["pins"].get("serializer_sha256"), "tools/assemble-d2.py")
    check(f"{D4_TYPED_LABELS} assembly.packet_sha256", d4_labels["packet_sha256"], D4_PACKET)
    check(f"{D4_TYPED_LABELS} assembly.reader_sha256", d4_labels["reader_sha256"], D4_READER)
    check(f"{D4_HOLDS} packet_sha256", d4_holds["packet_sha256"], D4_PACKET)
    check(f"{D4_HOLDS} projection_sha256", d4_holds["projection_sha256"], D4_TYPED_LABELS)
    check(f"{D4_HOLDS} projector_sha256", d4_holds["projector_sha256"], "tools/d2-typed-labels.py")
    return checked, matched


# D2 component inputs the D2 projector's own selftest fixture copies (the D2
# byte-identity control's inputs; the D4 path does not read them post-flip).
D2_COMPONENT_INPUTS = (
    "examples/culture-d2/components/05-lexicon.yml",
    "examples/culture-d2/components/09-eras-calendar.yml",
    "examples/culture-d2/components/11-costumes.yml",
    "examples/culture-d2/components/12-rank-rules.yml",
)


def v3_load_v2_rows(root):
    """The 15 v2 claim rows and open questions, read from the filed v2 machine
    twin with the same reader the harness judges use (subset-equality source)."""
    try:
        namespace = runpy.run_path(str(Path(root) / UNCERTAINTY_TOOL))
        data = namespace["read_packet"](Path(root) / V2_PACKET_YML)
        claims, open_questions = namespace["packet_sections"](data)
    except (OSError, ValueError) as exc:
        raise ArtifactError(f"{V2_PACKET_YML}: cannot read the v2 machine twin ({exc})") from exc
    rows = []
    for claim in claims:
        rows.append(
            {
                "claim_id": str(claim["claim_id"]),
                "kind": str(claim.get("claim_kind", "")),
                "evidence_status": str(claim.get("evidence_status", "")),
                "status": str(claim["uncertainty"]["status"]),
                "basis": str(claim["uncertainty"]["basis"]),
                "links": [str(link) for link in claim.get("links", [])],
                "statement": str(claim.get("statement", "")),
            }
        )
    return rows, open_questions


D4_ROW_RE = re.compile(r"^### (D4-CL\d\d) — (.+?) — (.+?) — `([a-z]+)`\s*$", re.M)


def v3_parse_claims_map(root):
    """The twelve D4 rows as filed in reports/round-20/handoff/claims-map.md."""
    text = read_text(root, CLAIMS_MAP)
    matches = list(D4_ROW_RE.finditer(text))
    if len(matches) != 12:
        raise ArtifactError(f"{CLAIMS_MAP}: expected 12 D4 rows, found {len(matches)}")
    rows = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end():end]
        statement = re.search(r"- \*\*statement:\*\*\s*(.*?)(?=\n- \*\*)", body, re.S)
        basis = re.search(r"- \*\*u\.basis:\*\*\s*(.*?)(?=\n- \*\*)", body, re.S)
        links = re.search(r"- \*\*links:\*\*\s*(.*?)(?=\n- \*\*|\n#{2,3} |\Z)", body, re.S)
        if not statement or not basis or not links:
            raise ArtifactError(f"{CLAIMS_MAP}: row {match.group(1)} lacks statement/basis/links")
        basis_text = cell(basis.group(1).strip().strip("`").strip())
        link_specs = re.findall(r"`([^`]+)`", links.group(1))
        if not link_specs:
            raise ArtifactError(f"{CLAIMS_MAP}: row {match.group(1)} names no links")
        rows.append(
            {
                "claim_id": match.group(1),
                "kind": match.group(2).strip(),
                "evidence_status": match.group(3).strip(),
                "status": match.group(4).strip(),
                "basis": basis_text,
                "links": link_specs,
                "statement": cell(statement.group(1).strip()),
            }
        )
    return rows


def v3_load_v2_edges(root):
    try:
        namespace = runpy.run_path(str(Path(root) / LINKS_TOOL))
        data = namespace["read_packet"](Path(root) / V2_PACKET_YML)
        return [dict(edge) for edge in data["coupling_edges"]]
    except (OSError, ValueError) as exc:
        raise ArtifactError(f"{V2_PACKET_YML}: cannot read the v2 edge rows ({exc})") from exc


def v3_build_edge_rows(d2, d3, d4, root=ROOT):
    """The v3 edge table: the 34 v2 rows carried from the v2 machine twin plus
    the D4 families, one atomic row per live relation (design §3)."""
    rows = v3_load_v2_edges(root)
    position = 0

    def d4_edge(source, relation, targets, claims, mechanism, limits, applicability):
        nonlocal position
        position += 1
        rows.append(
            {
                "edge_id": f"D4E-{position:02d}",
                "source": source,
                "relation": relation,
                "target_ids": targets,
                "claims": claims,
                "applicability": applicability,
                "mechanism": mechanism,
                "limits": limits,
                "declared_in": D4_PACKET,
            }
        )

    for slot, garment in d4["garment_slots"]:
        d4_edge(
            garment,
            "costume-to-form-slot (declared, unfilled)",
            [slot],
            ["D4-CL04"],
            f"the costume record names its form slot in form_slot ({garment} → {slot}); the slot is unfilled",
            "the owed term is held (D2L-FORM-UNRESOLVED), never promoted",
            "the costume record's own form_slot field as carried in the packet bytes",
        )
    for garment, material in d4["costume_materials"]:
        d4_edge(
            garment,
            "costume-to-material (declared)",
            [material],
            ["D4-CL07"],
            f"the costume record names its material record in material_ref ({garment} → {material})",
            "carried as declared; the exercise neither adjudicates nor repairs the coupling",
            "the costume record's own material_ref field as carried in the packet bytes",
        )
    for rule, ranks in d4["rank_ranks"]:
        d4_edge(
            rule,
            "rank-rule-to-wearer-ranks (declared)",
            ranks,
            ["D4-CL03"],
            f"the rank rule names its permitted wearer ranks ({rule} → {', '.join(ranks)})",
            "the rank names are the packet's own wearer_ranks values, indexed from its bytes",
            "the rank rule's own wearer_ranks list as carried in the packet bytes",
        )
    for era in d4["records"]["era_records"]:
        tag = era.get("tag", "")
        garments = d4["era_garments"].get(tag, [])
        if not garments:
            continue
        d4_edge(
            era["id"],
            "era-to-costume-seam (derived from the records' own era tags)",
            garments,
            ["D4-CL02"],
            f"the costume records dated to this era tag ({era['id']} tag {tag} → {', '.join(garments)})",
            "the seam prose names no record ids; the edge is derived from the records' own era fields, never guessed",
            "the era record's tag and the costume records' era fields as carried in the packet bytes",
        )
    for lexeme, layer in d4["layer_for_lexeme"]:
        layer_id = next((row["id"] for row in d4["records"]["layers"] if row.get("name") == layer), None)
        if layer_id is None:
            continue
        d4_edge(
            lexeme,
            "borrowed-label-to-layer (declared)",
            [layer_id],
            ["D4-CL10"],
            f"the borrowed record names its layer ({lexeme} → {layer} = {layer_id})",
            "donor stages stay unmodelled; the layer name is the packet's own value token",
            "the lexicon record's own loan_layer/layer field as carried in the packet bytes",
        )
    for name_id, bases, rule in d4["name_formations"]:
        targets = []
        if rule:
            targets.append(rule)
        unresolved = []
        for base in bases:
            lexeme = d4["term_to_lexeme"].get(base)
            if lexeme:
                targets.append(lexeme)
            else:
                unresolved.append(base)
        if not targets:
            continue
        limits = "bases resolved by the lexicon's own term fields, never guessed"
        if unresolved:
            limits += f"; bases resolving to no lexicon term stay text: {', '.join(unresolved)}"
        d4_edge(
            name_id,
            "name-to-formation-and-bases (declared)",
            targets,
            ["D4-CL01"],
            f"the name record names its formation rule and base lexemes ({name_id} → {', '.join(targets)})",
            limits,
            "the name record's own formation block as carried in the packet bytes",
        )
    for symbol_id, era, register in d4["symbol_eras"]:
        if not era:
            continue
        d4_edge(
            symbol_id,
            "symbol-to-era (declared; register carried in limits)",
            [era],
            ["D4-CL02"],
            f"the symbol record names its era ({symbol_id} → {era}); register `{register}`",
            f"the register value `{register}` is a carried text token, not a record id",
            "the symbol record's own era and register fields as carried in the packet bytes",
        )
    for unit in d4["festival_units"]:
        d4_edge(
            unit,
            "festival-rite-to-calendar-unit (declared)",
            ["CAL-01"],
            ["D4-CL02"],
            f"the festival/rite record is timed within the drill's single calendar unit ({unit} → CAL-01)",
            "the timing text is carried in the record; no date is synthesized",
            "the calendar record CAL-01 and the festival/rite records' timing fields as carried in the packet bytes",
        )
    for layer, name, loans in d4["contact_loans"]:
        route_id = d4["route_names"].get(name)
        targets = [route_id] if route_id else []
        targets.extend(loans)
        if not targets:
            continue
        d4_edge(
            layer,
            "contact-layer-to-route-and-loans (declared)",
            targets,
            ["D4-CL10"],
            f"the contact layer names its road and loan lexemes ({layer} → {', '.join(targets)})",
            "donor stages stay unmodelled; the transfer is a declared design construction",
            "the contact record's own name and loans list as carried in the packet bytes",
        )
    return rows


def v3_manifest_rows(root, digests, sizes, d2, d3, typed, contract, d3_expected, d3_controls, glossary, d4, d4_typed, d4_labels, d4_holds):
    """One row per read-set file, each digest measured live; the D4 rows carry
    the D4 tree's own provenance notes."""
    recon = json_file(root, RECONCILIATION)
    controls = set(d3_controls) if isinstance(d3_controls, dict) else set()
    component_record_counts = {}
    for rel in D3_COMPONENTS:
        component_record_counts[rel] = json_file(root, rel)
    counts = d4["counts"]

    def comp_note(rel):
        obj = component_record_counts[rel]
        collected = []
        for key in ("lexicon", "names", "utterances", "beliefs", "symbols", "materials", "objects", "costumes", "eras", "references", "bridges", "rank_rules", "sound_changes"):
            value = obj.get(key)
            if isinstance(value, list) and value:
                collected.append(f"{len(value)} {key}")
        return "; ".join(collected) or f"{len(obj)} keys"

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
        GATE: "this run's shape judge; the authoritative verdict authority for the assembled packet",
        "tools/assemble-culture-d3.py": "d3 assembler named by the packet's own assembly block",
        "tools/assemble-d2.py": "d2 assembler and yaml_lines serializer dependency (read-only)",
        "tools/d2-typed-labels.py": "d2/d4 typed-label projection generator (the D2 path stays byte-identical)",
        "tools/check-evidence-coupling.py": "d3 evidence-coupling guard (read-only)",
        V2_PACKET_MD: "filed v2 packet (Markdown), digest-pinned; the subset-equality source's gate surface",
        V2_PACKET_YML: "filed v2 machine twin: the 15 v2 claim rows and the 34 v2 edge rows carried into this packet",
        D4_PACKET: (
            f"d4 assembled drill (read-only input): {counts['lexicon']} lexicon / {counts['names']} names / "
            f"{counts['symbols']} symbols / {counts['costumes']} costumes / {counts['rank_rules']} rank rules / "
            f"{counts['era_records']} era records / {counts['contact']} contact layers / "
            f"{counts['provenance']} provenance rows; {len(d4['components'])} component digests in its assembly"
        ),
        D4_TYPED_PACKET: (
            f"d4 typed-channel twin: {d4_typed['channel_rows']} typed-channel rows; pipeline counts "
            f"{d4_typed['counts'].get('hold')} hold / {d4_typed['counts'].get('note')} note / "
            f"{d4_typed['counts'].get('fail')} fail"
        ),
        D4_TYPED_LABELS: (
            f"d4 typed-label projection: {d4_labels['labels']} labels "
            f"({d4_labels['by_kind'].get('native-form', 0)} native-form / "
            f"{d4_labels['by_kind'].get('translated-label', 0)} translated-label / "
            f"{d4_labels['by_kind'].get('borrowed-strata', 0)} borrowed-strata), "
            f"{d4_labels['findings_total']} findings, {d4_labels['unresolved_items']} unresolved rank items, "
            f"{d4_labels['alias_rows']} era-alias rows"
        ),
        D4_HOLDS: (
            f"d4 committed hold set: {d4_holds['hold']} holds / {d4_holds['note']} note / {d4_holds['fail']} fail, "
            "pinned to packet, projection and projector digests"
        ),
        D4_BRIEF: "d4 tree brief: the canon-boundary block and the fixture-relative era declaration",
        D4_ASSEMBLY: "d4 assembly record (documentation surface, digest-pinned here; its prose is not propagated)",
        D4_ASSEMBLER: "d4 assembler named by the packet's own assembly block",
        D4_TYPED_TOOL: "d4 typed-channel assembler; its selftest is the mirror-without-D2 run witness",
        D4_TYPED_GATE: "d4 typed adapter gate (the O seat's receipt surface; not asserted by this exercise)",
        D4_ASSEMBLY_GATE: "d4 assembly gate (the O seat's receipt surface; not asserted by this exercise)",
        D4_READER: "d4 reader gate named by the packet's own assembly block",
        UNCERTAINTY_TOOL: "this run's uncertainty judge (round-15 harness validator, read-only here)",
        LINKS_TOOL: "this run's link judge (round-15 harness validator, read-only here)",
        CLAIMS_MAP: "the twelve D4 claim rows as filed; this packet carries them verbatim",
    }
    for rel in SOURCE_LEDGERS:
        obj = json_file(root, rel)
        by_rel[rel] = f"closed round-6 source ledger: {len(obj)} top-level keys (read-only evidence binding)"
    for rel in D3_COMPONENTS:
        by_rel[rel] = f"d3 component: {comp_note(rel)}"
    for rel in D4_COMPONENTS:
        by_rel[rel] = "d4 authored component input (digest pinned by packet.d4.yml assembly)"
    for rel in D4_RECEIPTS:
        by_rel[rel] = "round-18 d4 receipt cited by the D4 claim rows (read-only)"
    for rel in D2_COMPONENT_INPUTS:
        by_rel[rel] = "d2 component input of the D2 projector's selftest fixture (byte-identity control)"

    rows = []
    for index, rel in enumerate(V3_READ_SET, start=1):
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


def v3_build_claim_rows(v2_rows, d4_rows, d4, d4_labels, d4_holds, d4_typed, d4_legs):
    """The v3 ledger: the 15 v2 rows carried verbatim + the 12 D4 rows."""
    rows = []
    for row in v2_rows:
        rows.append(dict(row))
    rows.extend(dict(row) for row in d4_rows)
    if len(rows) != 27:
        raise ArtifactError(f"the ledger holds {len(rows)} rows, expected 27 (15 v2 + 12 D4)")
    # design §4 rule 2 / m11: a `supported` D4-CL08 must carry the run witness.
    alias = next((row for row in rows if row["claim_id"] == "D4-CL08"), None)
    if alias is None:
        raise ArtifactError("the ledger carries no D4-CL08 row")
    if alias["status"] == "supported":
        missing = [token for token in V3_ALIAS_WITNESS_TOKENS if token not in alias["basis"]]
        if missing:
            raise Failed(
                "E2E-UNC",
                f"D4-CL08 is typed supported but its basis lacks the run witness {missing}",
            )
    return rows


def v3_build_twin(ledger, edges, open_questions, ids, digests, d2, d3, d4):
    """The machine twin judged by tools/harness/{packet_uncertainty,packet_links}.py.

    It is a projection of the delivered Markdown: the ledger and edge rows are
    the parsed tables, so a byte the gate sees and a byte the harness judges are
    the same byte.
    """
    manifest = []
    for rel in V3_READ_SET:
        row = {"artifact_id": ids[rel], "path": rel, "sha256": digests[rel]}
        if rel == D2_PACKET:
            row["record_ids"] = sorted(set(d2["record_ids"]) | set(d2["cit_ids"]))
        elif rel == D3_PACKET:
            row["record_ids"] = list(d3["record_ids"])
        elif rel == RECONCILIATION:
            row["record_ids"] = sorted(set(re.findall(r'"R6-\d\d-[A-Z]"', read_text(ROOT, RECONCILIATION))))
        elif rel == D4_PACKET:
            row["record_ids"] = sorted(set(d4["record_ids"]) | set(d4["index_extra"]))
        manifest.append(row)
    return {
        "packet_id": V3_PACKET_ID,
        "packet_version": V3_PACKET_VERSION,
        "profile": V3_PROFILE,
        "claim_ledger": [
            {
                "claim_id": row["claim_id"],
                "claim_kind": row["kind"],
                "evidence_status": row["evidence_status"],
                "uncertainty": {"status": row["uncertainty_status"], "basis": row["uncertainty_basis"]},
                "links": list(row["links"]),
                "statement": row["statement"],
            }
            for row in ledger
        ],
        "open_questions": list(open_questions),
        "artifact_manifest": manifest,
        "coupling_edges": [
            {
                "edge_id": row["edge_id"],
                "source": row["source"],
                "relation": row["relation"],
                "target_ids": list(row["target_ids"]),
                "claims": list(row["claims"]),
                "applicability": row["applicability"],
                "mechanism": row["mechanism"],
                "limits": row["limits"],
                "declared_in": row["declared_in"],
            }
            for row in edges
        ],
    }


def v3_build_packet(root, d2, d3, typed, d4, d4_typed, d4_labels, d4_holds, contract, digests, sizes, glossary, fields_supplied, claim_rows, edge_rows, open_questions, d4_legs, v2_subset_digest, alias_state):
    component_total = len(d2["components"]) + len(d3["components"]) + len(d4["components"])
    rows = v3_manifest_rows(root, digests, sizes, d2, d3, typed, contract, json_file(root, D3_EXPECTED), json_file(root, D3_CONTROLS), glossary, d4, d4_typed, d4_labels, d4_holds)
    statuses = {status: sum(1 for row in claim_rows if row["status"] == status) for status in UNCERTAINTY_STATUSES}
    links_total = sum(len(row["links"]) for row in claim_rows)
    d4_claims = [row for row in claim_rows if row["claim_id"].startswith("D4-")]
    counts = d4["counts"]
    witness = d4["witness"]
    d4_rules = d4["records"]["rank_rules"]

    lines = []
    add = lines.append
    add(
        "# Handoff packet — D2/D3/D4 triple-drill exercise "
        "(deliberately unbound research packet; not canonized)"
    )
    add("")
    add(
        "NON-CANON handoff packet, kotodama-shokunin → lore-shokunin, assembled by "
        "`tools/exercise-handoff-e2e.py --profile v3` from the live lane artifacts named in "
        "§artifact_manifest: the D2 highland-pastoralist design drill and its typed-label projection, the D3 "
        "source-bounded culture drill with its legacy gate projection, and the D4 furnace-league drill with "
        "its typed twin, typed-label projection and committed hold set. This build supersedes the filed "
        "round-15 keyed build `reports/round-15/handoff/packet-v2-05.md` (contract §9 supersedes discipline): "
        "that build stays filed and green, and its 15 claim rows are carried into this ledger verbatim. Every "
        "field below is derived from the files named here at assembly time; the twelve D4 rows are carried "
        "from `reports/round-20/handoff/claims-map.md`. The ledger carries the round-15 uncertainty dimension "
        "and machine-checkable claim-to-record links, and the delivered tables are re-parsed into a machine "
        "twin judged by `tools/harness/packet_uncertainty.py` and `tools/harness/packet_links.py` (read-only "
        "here). This is an operability exercise, not a delivery: no lore brief, no baseline bible and no "
        "receipt surface exist, and no canon standing is asserted here. Canon standing is lore's alone "
        "(contract §6, §8.7). All native spellings are constructed and unscreened ASCII lowercase; no "
        "real-language clearance, community consultation, or cultural permission is claimed, performed, or "
        "granted."
    )
    add("")
    add(
        f"Renderer {V3_PACKET_VERSION} is the round-22 correcting revision, derived from and superseding "
        "the filed `reports/round-20/handoff/packet.md` 3.0.0 exercise without rewriting it: the optional "
        "declared_in edge column and full mechanism/limits text are restored. The 34 carried v2 edge "
        "mappings are checked for exact equality after Markdown parsing and twin projection; the claim "
        "rows and their evidence statuses are unchanged. This is an additive provenance correction, not "
        "a lore disposition or an automatic adopted replacement."
    )
    add("")
    add("- canon_standing: not canonized — lore disposition required (lore-shokunin owns canon)")
    add(
        f"- handoff_status: prepared-not-accepted (live value from {D3_PACKET}: `{d3['handoff_status']}`; "
        f"canon status `{d3['canon_status']}`; D4 drill status: `{d4['name']}`)"
    )
    add("")
    add("| field | value |")
    add("|---|---|")
    add(f"| packet_id | {V3_PACKET_ID} |")
    add(f"| packet_version | {V3_PACKET_VERSION} (pure function of the pinned read set; no wall-clock content) |")
    add(
        f"| contract_ref | {contract['id']} {contract['revision']}, contract digest "
        f"sha256:{digests[CONTRACT]} (§1 pin, re-measured at assembly time from {CONTRACT}; the "
        "bilateral same-revision read is still pending) |"
    )
    add(
        "| producer | kotodama-shokunin (round-20 handoff-e2e exercise v3; generative craft and design "
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
        "| subject_refs | 12 namespaced candidates, all unresolved — no lore entity ID was supplied and none "
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
        f"`cand:kotodama.d2.open-grazing-era` (witness: era record ER-01 \"{witness_era}\"), "
        f"`cand:kotodama.d4.culture` (witness: {D4_PACKET} name \"{cell(d4['name'], 60)}\"), "
        f"`cand:kotodama.d4.stamp-holder-office` (witness: symbol SYM-01 holder \"{cell(witness['SYM-01']['holder'], 70)}\"), "
        f"`cand:kotodama.d4.furnace-right` (witness: rank rule RK-01 authority \"{cell(witness['RK-01']['authority'], 60)}\"), "
        f"`cand:kotodama.d4.league-charter` (witness: rank rule RK-02 authority \"{cell(d4_rules[1]['authority'], 60)}\") |"
    )
    add(
        f"| scope | three unbound design drills, no real place and no dates: D2 \"{witness_culture}\" "
        f"(eras {'/'.join(d2['eras'])}, {len(d2['lexicon_ids'])} lexicon records, {len(d2['name_ids'])} names, "
        f"{len(d2['costume_ids'])} costumes, {len(d2['material_ids'])} materials, everyday/ritual/ledger "
        f"registers, read-only input bytes); D3 {D3_PACKET} ({'/'.join(era['id'] for era in d3['eras'])} "
        f"fixture-relative eras, {len(d3['lexicon'])} lexemes, {len(d3['names'])} names, "
        f"{len(d3['utterances'])} utterances, {len(d3['beliefs'])} attributed beliefs, {len(d3['symbols'])} "
        f"symbols, {len(d3['costumes'])} costumes — one declared rank-rule violation — "
        f"{len(d3['bridges'])} design-only bridges, ordinary/ritual registers); D4 {D4_PACKET} "
        f"({', '.join(d4['era_tags'])} fixture-relative tags with E3 declared reserved, {counts['lexicon']} "
        f"lexicon records, {counts['names']} names, {counts['symbols']} symbols, {counts['costumes']} "
        f"costumes — each owing an unfilled form slot — {counts['rank_rules']} rank rules, "
        f"{counts['contact']} contact layers, twelve authored components); all native spellings are "
        "constructed ASCII-lowercase, unscreened, with no ISO code or real language family claimed |"
    )
    add("")

    add("## delivered record sets")
    add("")
    add(
        "The per-set scope detail behind the one-line §scope above, read out of the three packets: every "
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
        f"| D4 drill records | {D4_PACKET} | furnace-league drill; one invented furnace town (no real place) | "
        "invented craft and trade registers; ASCII-lowercase spellings, no ISO code claimed | craft, law and "
        f"trade registers ({counts['rank_rules']} rank rules over the furnace right and league charter) | "
        f"{'/'.join(d4['era_tags'])} (fixture-relative; E3 reserved and unoccupied) |"
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
        f"checks digest presence only, this exercise checks equality. {len(V3_READ_SET)} read-set files plus "
        f"one inline-payload row; the drills carry no declared packet version, so their bytes are pinned by "
        "digest alone. The filed v2 twins are pinned here too: they are the subset-equality source and stay "
        "untouched."
    )
    add("")
    add("| artifact_id | path | role | sha256 | records |")
    add("|---|---|---|---|---|")
    for artifact_id, path, role, digest, records in rows:
        add(f"| {artifact_id} | {path} | {cell(role, 260)} | {digest} | {records} |")
    add("")

    add("## dependency_manifest")
    add("")
    add(f"- profile {V3_PROFILE} (this exercise; renderer revision {V3_PACKET_VERSION})")
    add(f"- {GATE} @sha256:{digests[GATE]} (the shape gate this packet is judged by)")
    add(f"- {CONTRACT} @sha256:{digests[CONTRACT]} (pinned contract; interface revision {contract['revision']})")
    add(
        f"- {V2_PACKET_MD} @sha256:{digests[V2_PACKET_MD]}; {V2_PACKET_YML} @sha256:{digests[V2_PACKET_YML]} "
        "(filed v2 build: superseded by this one, carried verbatim and digest-pinned)"
    )
    add(
        f"- {D3_PACKET} @sha256:{digests[D3_PACKET]}; {D3_GATES} @sha256:{digests[D3_GATES]}; "
        f"{D3_EXPECTED} @sha256:{digests[D3_EXPECTED]} (d3 payload, legacy projection, freeze manifest)"
    )
    add(
        f"- {D4_PACKET} @sha256:{digests[D4_PACKET]}; {D4_TYPED_PACKET} @sha256:{digests[D4_TYPED_PACKET]}; "
        f"{D4_TYPED_LABELS} @sha256:{digests[D4_TYPED_LABELS]}; {D4_HOLDS} @sha256:{digests[D4_HOLDS]} "
        "(d4 drill, typed twin, typed-label projection, committed hold set — read-only inputs)"
    )
    add(
        f"- tools/assemble-culture-d3.py @sha256:{digests['tools/assemble-culture-d3.py']} and "
        f"tools/assemble-d2.py @sha256:{digests['tools/assemble-d2.py']} (assemblers named by the packets' "
        "own assembly blocks; the second is also the yaml_lines serializer, read-only)"
    )
    add(
        f"- {D4_ASSEMBLER} @sha256:{digests[D4_ASSEMBLER]} and {D4_TYPED_TOOL} "
        f"@sha256:{digests[D4_TYPED_TOOL]} (d4 assemblers named by the d4 packets' own assembly blocks)"
    )
    add(
        f"- tools/d2-typed-labels.py @sha256:{digests['tools/d2-typed-labels.py']} and "
        f"tools/check-evidence-coupling.py @sha256:{digests['tools/check-evidence-coupling.py']} "
        "(d2/d4 typed-label generator and d3 evidence-coupling guard, both read-only here)"
    )
    add(
        f"- {D4_READER} @sha256:{digests[D4_READER]} (d4 reader gate; its digest and the "
        f"{len(d4['components'])} d4 component digests are re-measured against the d4 packets' own assembly "
        "manifests at assembly time)"
    )
    add(
        f"- {D4_TYPED_GATE} @sha256:{digests[D4_TYPED_GATE]}; {D4_ASSEMBLY_GATE} "
        f"@sha256:{digests[D4_ASSEMBLY_GATE]} (the two d4 adapter gates: the O seat's receipt surface, "
        "pinned here read-only and not asserted by this exercise)"
    )
    add(
        f"- {UNCERTAINTY_TOOL} @sha256:{digests[UNCERTAINTY_TOOL]} and {LINKS_TOOL} "
        f"@sha256:{digests[LINKS_TOOL]} (this run's semantic judges: claim uncertainty in the clause "
        "grammar, and claim-to-record links plus coupling-edge records resolved against live bytes)"
    )
    add(
        f"- {CLAIMS_MAP} @sha256:{digests[CLAIMS_MAP]} (the twelve D4 claim rows carried verbatim into the "
        "ledger)"
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
        f"- D4 rank rules {d4_rules[0]['id']}–{d4_rules[-1]['id']} ({counts['rank_rules']} rules: authority "
        f"\"{cell(d4_rules[0]['authority'], 50)}\" … \"{cell(d4_rules[-1]['authority'], 50)}\"), with the "
        f"{counts['form_slots']} form slots LEX-GAR-01..06 declared unfilled (d4 obligations, held)"
    )
    add(
        f"- D2 grammar rule ids {d2['rule_ids'][0]}–{d2['rule_ids'][-1]} ({len(d2['rule_ids'])} distinct ids in "
        f"{D2_PACKET} morphology) and {d2['to_verify_lines']} lines carrying a `to-verify` flag"
    )
    add(
        f"- prerequisites: the {component_total} component digests recorded by the three assemblers' own "
        "`assembly.source_sha256` manifests (d2, d3, d4), re-measured and matched at assembly time, plus the "
        "d4 tree's own pins (assembler, reader, serializer, projection and hold-set digests); every reference "
        "above is pinned by exact digest or version (contract §4, §9)"
    )
    add("")

    add("## claim_ledger")
    add("")
    add(
        "Claim kinds are the contract §6 kinds. The 15 v2 rows are carried verbatim from "
        f"{V2_PACKET_YML} (subset-equality control: their normalized digest is "
        f"`{v2_subset_digest[:16]}…`); the twelve D4 rows are carried from {CLAIMS_MAP}. Every row carries "
        "the round-15 uncertainty dimension as `uncertainty_status` + `uncertainty_basis` in the clause "
        "grammar (`grounding:` always; `restriction:` on partial rows; `open:` + `owner:` on unresolved rows) "
        "and a `links` cell of machine-checkable `path#token` specs; the delivered tables are parsed back into "
        "a machine twin and judged by tools/harness/packet_uncertainty.py and tools/harness/packet_links.py "
        "(read-only here). The D2 rows are labelled a derived projection (author-side) so they cannot be read "
        "as world claims. Statements are read from the live records and the filed rows, not paraphrased from "
        "documentation."
    )
    add("")
    add("| claim_id | kind | evidence_status | uncertainty_status | uncertainty_basis | links | statement |")
    add("|---|---|---|---|---|---|---|")
    for row in claim_rows:
        add(
            f"| {row['claim_id']} | {row['kind']} | {cell(row['evidence_status'], 160)} | {row['status']} | "
            f"{cell(row['basis'])} | {'; '.join(row['links'])} | {cell(row['statement'])} |"
        )
    add("")

    add("## coupling_edges")
    add("")
    add(
        "Typed source→target relations, one row per declared coupling. The 34 v2 rows (BR01–BR05 and "
        f"D2E-01..29) are carried verbatim from {V2_PACKET_YML}, including declared_in and the full "
        "mechanism and limits text (full-row equality checked after Markdown and twin projection): the D2 "
        "packet states its couplings as one `coupling_note` per record, carried as one edge each — the "
        "round-11 aggregate row is gone. The D4 "
        "families (costume→slot, costume→material, rank rule→wearer ranks, era→costume seam, borrowed "
        "label→layer, name→formation/bases, symbol→era, festival/rite→calendar, contact→route) are one "
        "atomic row per live relation, measured from the packet bytes at assembly time. Every source and "
        "target resolves through the §artifact_manifest record index, and the claims cell names the ledger "
        "claim each edge realizes; declared_in names the source packet, not a canon authority."
    )
    add("")
    add("| edge_id | source | relation | target_ids | claims | applicability | mechanism | limits | declared_in |")
    add("|---|---|---|---|---|---|---|---|---|")
    for row in edge_rows:
        add(
            f"| {row['edge_id']} | {row['source']} | {cell(row['relation'])} | "
            f"{', '.join(row['target_ids'])} | {', '.join(row['claims'])} | "
            f"{cell(row['applicability'])} | {cell(row['mechanism'])} | "
            f"{cell(row['limits'])} | {row['declared_in']} |"
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
        (
            "RD-D4-01 D4 sixth form slot",
            "decide the delivery route of the sixth garment term (LEX-GAR-06, the imported-cloth coat): may "
            "its term arrive as a salt-road loan, or must the slot stay a lexicon-native form?",
            "allow the loan route / require a native form / defer",
            "the slot's own note leaves the route to a lexicon decision; the term is owed either way",
        ),
        (
            "RD-D4-02 D4 E3 reserved stratum",
            "keep the E3 tag reserved and unoccupied, occupy it with delivered records, or defer?",
            "keep reserved / occupy / defer",
            "no delivered record occupies E3; occupying it would add records, not read them",
        ),
        (
            "RD-D4-03 D4 furnace-right rank set",
            f"record the furnace right ({d4_rules[0]['id']}) and the league charter ({d4_rules[1]['id']}) as "
            "candidate in-world rank institutions, with their wearer-rank sets?",
            "record as candidate / defer / reject",
            "no lore baseline or entity keys exist; nothing is importable as canon",
        ),
        (
            "RD-D4-04 D4 loan donor stage",
            "leave the loan donors' own stages unmodelled, model them, or defer?",
            "leave unmodelled / model / defer",
            "the donor stages are marked unmodelled or (to-verify); modelling them is new research, not a read",
        ),
        (
            "RD-D4-05 D4 baseline question",
            "name the baseline bible revision, entity keys and receipt surface the D4 culture should deliver "
            "against, or keep it unbound?",
            "supply a baseline / keep unbound / defer",
            "the D4 rows are namespaced candidates only; nothing is importable without a baseline",
        ),
    ]
    for record_id, question, alternatives, blocker in decisions:
        add(f"| {record_id} | {question} | {alternatives} | {blocker} |")
    add("")

    add("## validation")
    add("")
    add(
        "Observed rows only: what this run actually measured, with the command shapes it used. These are "
        "local generation, identity and semantic checks of one envelope — not bible-wide consistency and not "
        "a canon decision (contract §8 step 3)."
    )
    add("")
    add(
        f"- read set: {len(V3_READ_SET)} files re-measured (`sha256`, same run) against the frozen baseline's "
        "`inputs` block; the §artifact_manifest digests are those measured values, not copied from any document"
    )
    add(
        f"- component digests: {component_total} digests recorded by the three assemblers' own "
        f"`assembly.source_sha256` manifests ({len(d2['components'])} D2, {len(d3['components'])} D3, "
        f"{len(d4['components'])} D4) re-measured against the component bytes on disk — all matched, so each "
        "packet still describes the files it names"
    )
    add(
        "- d4 tree pins: the d4 packets' own pins (assembler, reader, serializer, typed projection and hold-set "
        "digests) re-measured against live bytes — all matched"
    )
    add(
        "- manifest equality: every §artifact_manifest row's digest equals the sha256 of the file it names, "
        "measured in this run; the gate checks digest presence only, so this equality is the exercise's own "
        "assertion"
    )
    add(
        f"- field agreement: the contract §4 table yields {len(contract['section4_names'])} required field names, "
        f"the gate's own FIELD_NAMES tuple yields {len(fields_supplied[1])}, and this packet supplies "
        f"{len(fields_supplied[0])} — the three sets are compared, not assumed"
    )
    add(
        f"- glossary identity: the {len(glossary)} rows are the live D3 lexicon in source order (id, E0 form, "
        "computed E1 form, gloss) and every etymology carries the record's own status token, which is inside the "
        "licensed vocabulary; no D4 lexicon row enters the payload, so the gate scan stays 20/20"
    )
    add(
        "- D2 read-only facts carried into this packet's D2 claim rows: "
        f"{typed['labels']} typed labels ({typed['by_kind'].get('native-form', 0)} native-form / "
        f"{typed['by_kind'].get('translated-label', 0)} translated-label / "
        f"{typed['by_kind'].get('borrowed-strata', 0)} borrowed-strata), {typed['findings_total']} findings "
        f"({typed['hold_or_fail']} hold-or-fail), {typed['unresolved_items']} unresolved rank items, "
        f"{typed['quarantine']} quarantine handles, {typed['conflicts']} conflicts, "
        f"{typed['reconciliations']} reconciliation records"
    )
    add(
        f"- D4 read-only facts carried into this packet's D4 claim rows: {counts['lexicon']} lexicon / "
        f"{counts['names']} names / {counts['symbols']} symbols / {counts['costumes']} costumes / "
        f"{counts['rank_rules']} rank rules / {counts['era_records']} era records / {counts['contact']} "
        f"contact layers / {counts['provenance']} provenance rows; typed channel {d4_labels['labels']} labels "
        f"({d4_labels['by_kind'].get('native-form', 0)} native-form / "
        f"{d4_labels['by_kind'].get('translated-label', 0)} translated-label / "
        f"{d4_labels['by_kind'].get('borrowed-strata', 0)} borrowed-strata), {d4_labels['findings_total']} "
        f"findings ({d4_labels['hold_or_fail']} hold-or-fail), {d4_labels['unresolved_items']} unresolved "
        f"rank items, {d4_labels['quarantine']} quarantine handles; hold set {d4_holds['hold']} holds / "
        f"{d4_holds['note']} note"
    )
    add(
        f"- v2-subset equality: the 15 v2 rows parsed out of this ledger equal the rows of {V2_PACKET_YML} "
        f"(normalized subset digest `{v2_subset_digest[:16]}…`, recorded in the frozen baseline) after "
        "whitespace normalization — kind, evidence_status, status, basis and links compared; the v2 twins "
        "are digest-pinned in the same baseline, so a re-typed v2 row is an `E2E-DIGEST`"
    )
    add(
        f"- uncertainty dimension: {len(claim_rows)} claim rows parsed back from the delivered table, "
        f"statuses {statuses['supported']} supported / {statuses['partial']} partial / "
        f"{statuses['unresolved']} unresolved; every basis is non-placeholder, unique and in the clause "
        "grammar, and every unresolved row is routed in §open_questions"
    )
    add(
        f"- claim-to-record links: {links_total} links over {len(claim_rows)} rows; `{LINKS_TOOL}` resolves "
        "all of them against the live bytes with zero findings in this run"
    )
    add(
        f"- semantic twin: the delivered ledger and edge tables are re-parsed into a JSON twin (sha256 "
        f"recorded in the frozen baseline) and judged by `{UNCERTAINTY_TOOL} --require-oq` and "
        f"`{LINKS_TOOL} --repo-root <repo>`; both exit 0 with zero findings over {len(edge_rows)} coupling "
        "edges with concrete sources and targets"
    )
    for leg in d4_legs:
        add(
            f"- d4 leg: `python3 {leg['command']}` — exit {leg['exit']}; observed: {cell(leg['observed'], 160)}"
        )
    add(
        f"- d4 alias evidence state: `{alias_state}` — the D4-CL08 row's status is keyed to this state; the "
        "O seat's two adapter gates and its negative control remain its own receipt surface (pinned read-only "
        "here, not asserted)"
    )
    add(
        f"- gate: `python3 {GATE} packet.md` over the isolated copy, run from a directory outside the "
        "repository; declared expectation, checked after the run — "
        f"exit {V3_DECLARED['expected_exit']}, fields={V3_DECLARED['expected_scan']['fields']}, "
        f"glossary-entries={V3_DECLARED['expected_scan']['glossary_entries']}, "
        f"findings={V3_DECLARED['expected_scan']['findings']}; the observed values are compared against the frozen "
        f"baseline in `{V3_BASELINE_DEFAULT}`, whose run log records the verdict of the run it froze"
    )
    add("")

    add("## open_questions")
    add("")
    for row in open_questions:
        claims = row.get("unresolved_claims") or ""
        if isinstance(claims, list):
            claims = ", ".join(claims)
        suffix = f" (unresolved claims: {claims})" if claims and claims != "—" else ""
        add(f"- {row['id']}: {row['question']}{suffix}")
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
# v3 parsing, preflight, assembly and run
# --------------------------------------------------------------------------

V3_EDGE_HEADER = (
    "edge_id", "source", "relation", "target_ids", "claims", "applicability", "mechanism", "limits",
    "declared_in",
)


def table_rows(text, first_header):
    """The first table whose header starts with `first_header`; rows as cell lists."""
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if not line.lstrip().startswith("|"):
            continue
        header = [norm_cell(cell_text).lower() for cell_text in line.strip().strip("|").split("|")]
        if tuple(header[: len(first_header)]) != tuple(first_header):
            continue
        if index + 1 >= len(lines) or not re.match(r"^\|[\s:|-]+\|$", lines[index + 1].strip()):
            continue
        rows = []
        cursor = index + 2
        while cursor < len(lines) and lines[cursor].lstrip().startswith("|"):
            rows.append([part.strip() for part in lines[cursor].strip().strip("|").split("|")])
            cursor += 1
        return header, rows
    return None, []


def parse_ledger(text):
    header, raw = table_rows(text, LEDGER_HEADER)
    if header is None or tuple(header) != tuple(LEDGER_HEADER):
        raise ArtifactError(f"claim_ledger table missing or header wrong: {header}")
    rows = []
    for cells in raw:
        if len(cells) != len(LEDGER_HEADER):
            raise ArtifactError(f"claim row holds {len(cells)} cells, expected {len(LEDGER_HEADER)}")
        row = dict(zip(LEDGER_HEADER, cells))
        row["links"] = [link.strip() for link in row["links"].split(";") if link.strip()]
        rows.append(row)
    return rows


def parse_edges(text):
    header, raw = table_rows(text, V3_EDGE_HEADER)
    if header is None or tuple(header) != tuple(V3_EDGE_HEADER):
        raise ArtifactError(f"coupling_edges table missing or header wrong: {header}")
    rows = []
    for cells in raw:
        if len(cells) != len(V3_EDGE_HEADER):
            raise ArtifactError(f"edge row holds {len(cells)} cells, expected {len(V3_EDGE_HEADER)}")
        row = dict(zip(V3_EDGE_HEADER, cells))
        row["target_ids"] = [token.strip() for token in row["target_ids"].split(",") if token.strip()]
        row["claims"] = [token.strip() for token in row["claims"].split(",") if token.strip()]
        rows.append(row)
    return rows


def parse_basis_slots(basis):
    """The harness's clause-slot splitter, mirrored for the exercise's own preflight."""
    slots = {"grounding": None, "restriction": None, "open": None, "owner": None}
    matches = list(re.finditer(r"(grounding|restriction|open|owner)\s*:\s*", basis, re.IGNORECASE))
    for position, match in enumerate(matches):
        name = match.group(1).lower()
        end = matches[position + 1].start() if position + 1 < len(matches) else len(basis)
        value = basis[match.end():end].strip().rstrip(";").strip()
        if slots.get(name) is None:
            slots[name] = value
    return slots


LINK_SPEC_RE = re.compile(r"^([^#\s]+)(?:#(\S+))?$")


def v3_preflight(text, read_set_paths):
    """The v3 preflight: v1's envelope checks plus the uncertainty grammar and
    the link/edge shape; returns a list of (code, message) pairs."""
    problems = []
    values = extract_field_values(text)
    for name in FIELD_NAMES:
        value = values.get(name)
        if value is None:
            problems.append(("E2E-COUNT", f"field `{name}` not emitted"))
        elif is_placeholder(value):
            problems.append(("E2E-COUNT", f"field `{name}` carries only a placeholder value"))
    supplied = set(values)
    if supplied != set(FIELD_NAMES):
        problems.append(("E2E-COUNT", f"supplied field set differs from the §4 set: {sorted(set(FIELD_NAMES) - supplied)}"))
    if not CANON_MARKER_RE.search(text):
        problems.append(("E2E-COUNT", "non-canon marker `not canonized` missing"))
    dependencies = values.get("dependency_manifest", "")
    if re.search(r"(?i)\blatest\b", dependencies):
        problems.append(("E2E-COUNT", "dependency_manifest carries a floating `latest` reference"))
    if not DIGEST_RE.search(values.get("artifact_manifest", "")):
        problems.append(("E2E-COUNT", "artifact_manifest names no file digest"))
    contract_value = values.get("contract_ref", "")
    if not re.search(r"\b\d+\.\d+\.\d+\b", contract_value) or not re.search(r"[0-9a-f]{32,}", contract_value):
        problems.append(("E2E-COUNT", "contract_ref names no revision and/or no digest"))
    for trap in CANON_TRAP_RES:
        match = trap.search(text)
        if match:
            problems.append(("E2E-COUNT", f"producer-side canon certification pattern: {match.group(0)[:80]!r}"))
    rows = glossary_rows(text)
    if len(rows) != V3_DECLARED["expected_scan"]["glossary_entries"]:
        problems.append(
            ("E2E-SCAN", f"glossary payload holds {len(rows)} rows, expected {V3_DECLARED['expected_scan']['glossary_entries']}")
        )
    for entry_id, etymology in rows:
        if is_placeholder(etymology):
            problems.append(("E2E-SCAN", f"glossary entry {entry_id} carries no etymology text"))
            continue
        named = re.search(r"(?i)\bstatus\s*[:=]\s*[`*]?([A-Za-z_-]+)", etymology)
        if named and named.group(1).lower() not in ETYM_STATUSES:
            problems.append(("E2E-SCAN", f"glossary entry {entry_id} states unlicensed status {named.group(1)!r}"))
        elif not named and not any(re.search(rf"(?i)\b{status}\b", etymology) for status in ETYM_STATUSES):
            problems.append(("E2E-SCAN", f"glossary entry {entry_id} names no licensed etymology status"))

    # uncertainty grammar and links
    header, raw = table_rows(text, LEDGER_HEADER)
    if header is None or tuple(header) != tuple(LEDGER_HEADER):
        problems.append(("E2E-COUNT", f"claim_ledger table missing or header wrong: {header}"))
    else:
        if len(raw) < 27:
            problems.append(("E2E-COUNT", f"claim_ledger holds {len(raw)} rows, expected at least 27"))
        seen_bases = {}
        d4_rows = 0
        for cells in raw:
            if len(cells) != len(LEDGER_HEADER):
                problems.append(("E2E-COUNT", f"claim row holds {len(cells)} cells, expected {len(LEDGER_HEADER)}"))
                continue
            row = dict(zip(LEDGER_HEADER, cells))
            claim_id = norm_cell(row["claim_id"])
            if not re.match(r"^(?:D2-CL\d\d|CL\d\d|D4-CL\d\d)$", claim_id):
                problems.append(("E2E-COUNT", f"claim row id {claim_id!r} is outside the ledger namespaces"))
            kind = norm_cell(row["kind"])
            if kind not in CLAIM_KINDS:
                problems.append(("E2E-COUNT", f"claim {claim_id} states kind {kind!r}, outside the contract §6 kinds"))
            status = norm_cell(row["uncertainty_status"])
            basis = row["uncertainty_basis"].strip()
            if status not in UNCERTAINTY_STATUSES:
                problems.append(
                    ("E2E-UNC", f"claim {claim_id} states uncertainty status {status!r}, outside "
                                f"{'|'.join(UNCERTAINTY_STATUSES)}")
                )
            if is_placeholder(basis):
                problems.append(("E2E-UNC", f"claim {claim_id} carries only a placeholder uncertainty basis"))
            else:
                if len(basis) < UNCERTAINTY_MIN_BASIS:
                    problems.append(("E2E-UNC", f"claim {claim_id} basis is {len(basis)} chars, minimum {UNCERTAINTY_MIN_BASIS}"))
                slots = parse_basis_slots(basis)
                if slots["grounding"] is None:
                    problems.append(("E2E-UNC", f"claim {claim_id} basis lacks the mandatory `grounding:` clause"))
                if status == "partial" and slots["restriction"] is None:
                    problems.append(("E2E-UNC", f"claim {claim_id} is partial but lacks the `restriction:` clause"))
                if status == "unresolved":
                    if slots["open"] is None:
                        problems.append(("E2E-UNC", f"claim {claim_id} is unresolved but lacks the `open:` clause"))
                    if slots["owner"] is None:
                        problems.append(("E2E-UNC", f"claim {claim_id} is unresolved but lacks the `owner:` clause"))
                key = re.sub(r"\s+", " ", basis).strip().casefold()
                if key in seen_bases:
                    problems.append(("E2E-UNC", f"claim {claim_id} basis duplicates claim {seen_bases[key]} after normalization"))
                else:
                    seen_bases[key] = claim_id
            links = [link.strip() for link in row["links"].split(";") if link.strip()]
            if not links:
                problems.append(("E2E-LINK", f"claim {claim_id} carries no claim-to-record links"))
            for link in links:
                match = LINK_SPEC_RE.match(norm_cell(link))
                if not match:
                    problems.append(("E2E-LINK", f"claim {claim_id} link {link!r} is not a `path` or `path#token` spec"))
                    continue
                if match.group(1) not in read_set_paths:
                    problems.append(
                        ("E2E-LINK", f"claim {claim_id} link names {match.group(1)}, outside the v3 read set")
                    )
            if claim_id.startswith("D4-"):
                d4_rows += 1
        if d4_rows < 12:
            problems.append(("E2E-COUNT", f"claim_ledger holds {d4_rows} D4 claim rows, expected 12"))
        unresolved = [norm_cell(cells[0]) for cells in raw if len(cells) == len(LEDGER_HEADER)
                      and norm_cell(cells[3]) == "unresolved"]
        open_text = extract_field_values(text).get("open_questions", "")
        for claim_id in unresolved:
            if claim_id not in open_text:
                problems.append(("E2E-UNC", f"unresolved claim {claim_id} is not referenced by any open_questions row"))

    # edges
    header, raw = table_rows(text, V3_EDGE_HEADER)
    if header is None or tuple(header) != tuple(V3_EDGE_HEADER):
        problems.append(("E2E-COUNT", f"coupling_edges table missing or header wrong: {header}"))
    else:
        if len(raw) < 80:
            problems.append(("E2E-COUNT", f"coupling_edges holds {len(raw)} rows, expected at least 80"))
        claim_ids = [norm_cell(cells[0]) for cells in table_rows(text, LEDGER_HEADER)[1]
                     if len(cells) == len(LEDGER_HEADER)]
        for cells in raw:
            if len(cells) != len(V3_EDGE_HEADER):
                problems.append(("E2E-COUNT", f"edge row holds {len(cells)} cells, expected {len(V3_EDGE_HEADER)}"))
                continue
            row = dict(zip(V3_EDGE_HEADER, cells))
            if not norm_cell(row["source"]):
                problems.append(("E2E-COUNT", f"edge {row['edge_id']} names no source record"))
            targets = [token.strip() for token in row["target_ids"].split(",") if token.strip()]
            if not targets:
                problems.append(("E2E-COUNT", f"edge {row['edge_id']} names no target records"))
            claims = [token.strip() for token in row["claims"].split(",") if token.strip()]
            if not claims:
                problems.append(("E2E-COUNT", f"edge {row['edge_id']} names no claim back-link"))
            for claim in claims:
                if claim not in claim_ids:
                    problems.append(("E2E-COUNT", f"edge {row['edge_id']} names claim {claim}, not a ledger row"))
    return problems


def v3_status_census(ledger):
    return {status: sum(1 for row in ledger if row["uncertainty_status"] == status)
            for status in UNCERTAINTY_STATUSES}


def v3_subset_digest(rows):
    """The normalized digest of the 15 v2 rows as carried in the v3 ledger."""
    v2_ids = ("D2-CL01", "D2-CL02") + tuple(f"CL{index:02d}" for index in range(1, 14))
    payload = []
    for row in rows:
        if row["claim_id"] in v2_ids:
            payload.append(
                {
                    "claim_id": row["claim_id"],
                    "kind": re.sub(r"\s+", " ", row["kind"]).strip(),
                    "evidence_status": re.sub(r"\s+", " ", row["evidence_status"]).strip(),
                    "status": re.sub(r"\s+", " ", row["status"]).strip(),
                    "basis": re.sub(r"\s+", " ", row["basis"]).strip(),
                    "links": sorted(re.sub(r"\s+", " ", link).strip() for link in row["links"]),
                }
            )
    return sha256_text(json.dumps(payload, sort_keys=True, ensure_ascii=False))


def v3_run_leg(root, command):
    parts = command.split()
    run = subprocess.run(
        [sys.executable, *parts],
        cwd=str(root),
        capture_output=True,
        text=True,
    )
    lines = (run.stdout or run.stderr).strip().splitlines()
    return {"command": command, "exit": run.returncode, "observed": lines[-1] if lines else ""}


def v3_selftest_witness(leg, minimum):
    counts = re.match(r"selftest: (\d+)/(\d+) checks passed\b", leg["observed"])
    return bool(
        leg["exit"] == EXIT_PASS and counts
        and int(counts.group(1)) == int(counts.group(2)) >= minimum
    )


class V3Assembly:
    def __init__(self, root):
        self.root = root
        self.digests = {}
        self.sizes = {}
        for rel in V3_READ_SET:
            digest, size = measure(root, rel)
            self.digests[rel] = digest
            self.sizes[rel] = size
        self.contract = v1_mine_contract(root)
        self.gate_fields = v1_gate_field_names(root)
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
        self.d2 = v3_mine_d2(root)
        self.d3 = v3_mine_d3(root)
        self.typed = v1_mine_typed_labels(root)
        self.d4 = v3_mine_d4(root)
        self.d4_typed = v3_mine_d4_typed(root)
        self.d4_labels = v3_mine_d4_labels(root)
        self.d4_holds = v3_mine_d4_holds(root)
        self.component_checked, self.component_matched = v3_verify_component_digests(root, self.d2, self.d3, self.d4)
        self.d4_pins_checked, self.d4_pins_matched = v3_verify_d4_pins(root, self.d4, self.d4_labels, self.d4_holds)
        self.glossary = v1_build_glossary(self.d3)
        self.v2_rows, self.v2_open_questions = v3_load_v2_rows(root)
        if len(self.v2_rows) != 15:
            raise ArtifactError(f"{V2_PACKET_YML}: holds {len(self.v2_rows)} claim rows, expected 15")
        self.d4_rows = v3_parse_claims_map(root)
        self.open_questions = list(self.v2_open_questions) + [
            {
                "id": "OQ-V3-04",
                "question": (
                    "the projector's era-alias leg read a foreign family's component for D4 packets "
                    "(round-19 routed wart); closed by the O seat's landed per-family resolution and "
                    "measured in this run — retained only as the re-open id if the O bytes are reverted "
                    "(claim D4-CL08 is supported in the landed branch)"
                ),
                "unresolved_claims": "—",
            },
            {
                "id": "OQ-V3-05",
                "question": (
                    "D4's inherited and own holds stay open: twelve form holds + three rank holds + one "
                    "note, thirteen unresolved rank items, three quarantine handles and four conflicts — "
                    "kotodama; blocking for the affected D2 rank records and the six garment terms, not for "
                    "this envelope"
                ),
                "unresolved_claims": "D4-CL09",
            },
            {
                "id": "OQ-V3-06",
                "question": (
                    "no lore baseline revision, entity key or receipt surface exists for the D4 culture — "
                    "lore-shokunin; non-blocking for this envelope"
                ),
                "unresolved_claims": "D4-CL12",
            },
        ]
        self.d4_legs = [
            v3_run_leg(root, f"{D4_ASSEMBLER} --check"),
            v3_run_leg(root, f"{D4_TYPED_TOOL} --check"),
            v3_run_leg(root, "tools/d2-typed-labels.py --selftest"),
            v3_run_leg(root, f"{D4_TYPED_TOOL} --selftest"),
        ]
        for leg in self.d4_legs[:2]:
            if leg["exit"] != 0:
                raise Failed("E2E-DIGEST", f"d4 leg failed: {leg['command']} exit {leg['exit']}: {leg['observed']}")
        witnesses = self.d4_legs[2:]
        witness_ok = v3_selftest_witness(witnesses[0], 50) and v3_selftest_witness(witnesses[1], 12)
        self.alias_state = "landed" if witness_ok else "open"
        if not witness_ok:
            summary = "; ".join(f"{leg['command']} exit {leg['exit']}" for leg in witnesses)
            raise Failed(
                "E2E-UNC",
                f"the D4-CL08 landed form is not backed by this run: the alias witnesses are red ({summary})",
            )
        self.claim_rows = v3_build_claim_rows(
            self.v2_rows, self.d4_rows, self.d4, self.d4_labels, self.d4_holds, self.d4_typed, self.d4_legs
        )
        self.edge_rows = v3_build_edge_rows(self.d2, self.d3, self.d4, root=root)
        self.v2_subset_digest = v3_subset_digest(
            [
                {
                    "claim_id": row["claim_id"],
                    "kind": row["kind"],
                    "evidence_status": row["evidence_status"],
                    "status": row["status"],
                    "basis": row["basis"],
                    "links": row["links"],
                }
                for row in self.claim_rows
            ]
        )
        self.packet = v3_build_packet(
            root,
            self.d2,
            self.d3,
            self.typed,
            self.d4,
            self.d4_typed,
            self.d4_labels,
            self.d4_holds,
            self.contract,
            self.digests,
            self.sizes,
            self.glossary,
            (set(FIELD_NAMES), self.gate_fields),
            self.claim_rows,
            self.edge_rows,
            self.open_questions,
            self.d4_legs,
            self.v2_subset_digest,
            self.alias_state,
        )
        self.packet_sha256 = sha256_text(self.packet)
        self.field_values = extract_field_values(self.packet)
        self.ledger = parse_ledger(self.packet)
        self.edges = parse_edges(self.packet)
        self.twin = v3_build_twin(
            self.ledger, self.edges, self.open_questions, {rel: f"A-{i:02d}" for i, rel in enumerate(V3_READ_SET, start=1)},
            self.digests, self.d2, self.d3, self.d4,
        )
        self.twin_text = json.dumps(self.twin, indent=1, sort_keys=True, ensure_ascii=False) + "\n"
        self.twin_sha256 = sha256_text(self.twin_text)

        self.assert_contract_digest()
        self.assert_claim_kinds()
        self.assert_candidates_unresolved()
        self.assert_manifest_equality()
        self.assert_subset_equality()

    def value(self, name):
        return self.field_values.get(name, "")

    def assert_contract_digest(self):
        expected = f"sha256:{self.digests[CONTRACT]}"
        if expected not in self.value("contract_ref"):
            raise Failed("E2E-DIGEST", f"contract_ref does not carry the measured contract digest {expected[:19]}…")

    def assert_claim_kinds(self):
        for row in self.ledger:
            if row["kind"].strip() not in CLAIM_KINDS:
                raise Failed(
                    "E2E-COUNT",
                    f"claim {row['claim_id']} states kind {row['kind'].strip()!r}, outside the contract §6 kinds",
                )

    def assert_candidates_unresolved(self):
        subject = self.value("subject_refs")
        tokens = re.findall(r"`([^`]+)`", subject)
        candidates = [token for token in tokens if token.startswith("cand:")]
        if len(candidates) != 12:
            raise Failed("E2E-COUNT", f"subject_refs names {len(candidates)} candidate refs, expected 12")
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
        if checked != len(V3_READ_SET):
            raise Failed("E2E-COUNT", f"manifest re-measured {checked} files, expected {len(V3_READ_SET)}")

    def assert_subset_equality(self):
        ledger_rows = [
            {
                "claim_id": row["claim_id"],
                "kind": row["kind"],
                "evidence_status": row["evidence_status"],
                "status": row["uncertainty_status"],
                "basis": row["uncertainty_basis"],
                "links": row["links"],
            }
            for row in self.ledger
        ]
        if v3_subset_digest(ledger_rows) != self.v2_subset_digest:
            raise Failed(
                "E2E-DIGEST",
                "the 15 v2 rows parsed out of the delivered ledger differ from the rows carried from "
                f"{V2_PACKET_YML}",
            )
        d4_rows = [row for row in self.ledger if row["claim_id"].startswith("D4-")]
        if len(d4_rows) != 12:
            raise Failed("E2E-COUNT", f"the ledger holds {len(d4_rows)} D4 claim rows, expected 12")
        expected_edges = v3_load_v2_edges(self.root)
        if len(expected_edges) != 34:
            raise ArtifactError(f"{V2_PACKET_YML}: holds {len(expected_edges)} edge rows, expected 34")
        v2_edge_ids = {row["edge_id"] for row in expected_edges}
        for surface, edges in (("Markdown", self.edges), ("twin", self.twin["coupling_edges"])):
            carried = [row for row in edges if row["edge_id"] in v2_edge_ids]
            if carried != expected_edges:
                raise Failed(
                    "E2E-DIGEST",
                    f"the 34 v2 edge rows in the delivered {surface} differ from {V2_PACKET_YML} "
                    "(including declared_in, full mechanism and limits)",
                )

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

    def run_semantics(self, workdir):
        """The machine twin, judged by the two round-15 harness validators."""
        twin_path = Path(workdir) / "twin.json"
        twin_path.write_text(self.twin_text, encoding="utf-8")
        results = {}
        for name, tool, extra in (
            ("uncertainty", UNCERTAINTY_TOOL, ["--require-oq"]),
            ("links", LINKS_TOOL, ["--repo-root", str(self.root)]),
        ):
            tool_path = Path(self.root) / tool
            if not tool_path.is_file():
                raise MissingArtifact(f"harness tool not found: {tool}")
            run = subprocess.run(
                [sys.executable, str(tool_path), "--packet", str(twin_path), *extra, "--json"],
                cwd=str(workdir),
                capture_output=True,
                text=True,
            )
            try:
                payload = json.loads(run.stdout)
            except json.JSONDecodeError as exc:
                raise Failed(
                    "E2E-DATA",
                    f"{tool} produced no JSON receipt (exit {run.returncode}): "
                    f"{(run.stdout or run.stderr).strip()[:200]}",
                ) from exc
            results[name] = {
                "exit": run.returncode,
                "findings": [str(row.get("code")) for row in payload.get("findings", [])],
                "findings_detail": payload.get("findings", []),
                "claims": payload.get("claims"),
                "links_checked": payload.get("links_checked"),
                "resolved": payload.get("resolved"),
                "twin": str(twin_path),
            }
        return results


def v3_baseline_payload(baseline):
    return {key: value for key, value in baseline.items() if key != "baseline_digest"}


def v3_baseline_digest(baseline):
    return sha256_text(json.dumps(v3_baseline_payload(baseline), sort_keys=True, separators=(",", ":"), ensure_ascii=False))


def v3_load_baseline(root, baseline_rel):
    path = Path(baseline_rel) if Path(baseline_rel).is_absolute() else Path(root) / baseline_rel
    if not path.is_file():
        raise BaselineError(f"frozen baseline not found: {path} (write one with --profile v3 --freeze DIR)")
    try:
        baseline = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError) as exc:
        raise BaselineError(f"frozen baseline unreadable: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise BaselineError(f"frozen baseline is not valid JSON: {exc}") from exc
    required = (
        "profile", "packet_id", "packet_version", "expected_exit", "expected_finding_ids", "expected_scan",
        "expected_uncertainty_findings", "expected_links_findings", "expected_links_unresolved",
        "packet_sha256", "twin_sha256", "claim_ids", "glossary_entry_ids", "inputs", "uncertainty", "links",
        "v2_subset_digest", "alias_state", "baseline_digest",
    )
    missing = [key for key in required if key not in baseline]
    if missing:
        raise BaselineError(f"frozen baseline is missing {missing} — it was not written by this exercise")
    if baseline["profile"] != V3_PROFILE:
        raise BaselineError(f"frozen baseline profile {baseline['profile']!r} is not {V3_PROFILE!r}")
    if baseline.get("baseline_digest") != v3_baseline_digest(baseline):
        raise BaselineError(
            "baseline integrity digest mismatch — the baseline file was edited without re-freezing "
            "(re-freeze with --profile v3 --freeze DIR and read the diff it prints)"
        )
    for key in (
        "expected_exit", "expected_finding_ids", "expected_scan", "expected_uncertainty_findings",
        "expected_links_findings", "expected_links_unresolved",
    ):
        if baseline[key] != V3_DECLARED[key]:
            raise BaselineError(f"baseline declares {key}={baseline[key]!r}, the exercise declares {V3_DECLARED[key]!r}")
    return path, baseline


def v3_exercise(root=ROOT, baseline_rel=V3_BASELINE_DEFAULT):
    """Run the v3 exercise; return (exit code, code-or-None, records)."""
    records = []

    def record(name, ok, detail=""):
        records.append({"check": name, "ok": bool(ok), "detail": detail})

    try:
        baseline_path, baseline = v3_load_baseline(root, baseline_rel)
        snapshot_before = {rel: measure(root, rel)[0] for rel in V3_READ_SET}
        assembly = V3Assembly(root)

        drifted = [rel for rel, digest in baseline["inputs"].items() if assembly.digests.get(rel) != digest]
        if drifted:
            for rel in drifted:
                record("input-digest", False, f"{rel}: frozen {str(baseline['inputs'][rel])[:12]}… live {assembly.digests[rel][:12]}…")
            raise Failed("E2E-DIGEST", f"{len(drifted)} read-set file(s) changed since the baseline was frozen: {', '.join(drifted[:3])}")
        record("input-digest", True, f"{len(V3_READ_SET)} read-set digests match the frozen baseline")

        problems = v3_preflight(assembly.packet, set(V3_READ_SET))
        if problems:
            for code, message in problems:
                record("preflight", False, f"{code}: {message}")
            raise Failed(problems[0][0], f"{len(problems)} preflight problem(s): {problems[0][1]}")
        record(
            "preflight",
            True,
            f"{len(FIELD_NAMES)} fields supplied, non-canon marker present, glossary vocabulary licensed, "
            f"{len(assembly.ledger)} claim rows carry the uncertainty grammar and read-set links, "
            f"{len(assembly.edges)} edges name claims",
        )
        record(
            "cross-references",
            True,
            f"contract §4 names = gate FIELD_NAMES = supplied fields; contract digest measured; claim kinds "
            f"in the §6 set; {assembly.component_matched}/{assembly.component_checked} component digests matched; "
            f"{assembly.d4_pins_matched}/{assembly.d4_pins_checked} d4 tree pins matched; manifest digests equal "
            f"bytes for {len(V3_READ_SET)} files",
        )
        record(
            "v2-subset",
            True,
            f"the 15 v2 claims in the delivered ledger equal the rows carried from {V2_PACKET_YML}; normalized "
            f"subset digest {assembly.v2_subset_digest[:16]}… (frozen in the baseline); the 34 v2 edge rows "
            "are identical in Markdown and twin, including declared_in and full mechanism/limits",
        )
        record("alias-leg", True, f"d4 alias evidence state: {assembly.alias_state}")

        with tempfile.TemporaryDirectory(prefix="handoff-e2e-") as workdir:
            gate = assembly.run_gate(workdir)
            semantics = assembly.run_semantics(workdir)
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

        uncertainty = semantics["uncertainty"]
        record(
            "semantic-uncertainty",
            uncertainty["exit"] == 0 and not uncertainty["findings"],
            f"{UNCERTAINTY_TOOL} exit {uncertainty['exit']} over {uncertainty['claims']} claims (require-oq); "
            f"findings {len(uncertainty['findings'])}"
            + (f": {', '.join(uncertainty['findings'][:4])}" if uncertainty["findings"] else ""),
        )
        if uncertainty["exit"] != 0 or uncertainty["findings"]:
            raise Failed(
                "E2E-UNC",
                f"packet_uncertainty.py exited {uncertainty['exit']} with findings "
                f"{', '.join(uncertainty['findings'][:6])}",
            )
        links = semantics["links"]
        resolved_ok = links["exit"] == 0 and not links["findings"] and links["links_checked"] == links["resolved"]
        record(
            "semantic-links",
            resolved_ok,
            f"{LINKS_TOOL} exit {links['exit']}; {links['resolved']}/{links['links_checked']} links resolved "
            f"against live bytes; findings {len(links['findings'])}"
            + (f": {', '.join(links['findings'][:4])}" if links["findings"] else ""),
        )
        if not resolved_ok:
            raise Failed(
                "E2E-LINK",
                f"packet_links.py exited {links['exit']} with {links['resolved']}/{links['links_checked']} "
                f"links resolved and findings {', '.join(links['findings'][:6])}",
            )
        if links["links_checked"] != baseline["links"]["links"] or links["resolved"] != baseline["links"]["resolved"]:
            raise Failed(
                "E2E-COUNT",
                f"link census {links['resolved']}/{links['links_checked']} != baseline "
                f"{baseline['links']['resolved']}/{baseline['links']['links']}",
            )
        census = v3_status_census(assembly.ledger)
        if census != baseline["uncertainty"]["statuses"]:
            raise Failed(
                "E2E-COUNT",
                f"uncertainty status census {census} != baseline {baseline['uncertainty']['statuses']}",
            )
        record(
            "uncertainty-census",
            True,
            f"claims={len(assembly.ledger)} statuses="
            f"{census['supported']}/{census['partial']}/{census['unresolved']}",
        )
        if assembly.v2_subset_digest != baseline["v2_subset_digest"]:
            raise Failed("E2E-DIGEST", "the v2-subset digest differs from the frozen baseline")
        if assembly.alias_state != baseline["alias_state"]:
            raise Failed(
                "E2E-UNC",
                f"the d4 alias evidence state {assembly.alias_state!r} differs from the frozen baseline "
                f"{baseline['alias_state']!r} — re-freeze as a new row with the reason recorded",
            )

        if assembly.packet_sha256 != baseline["packet_sha256"]:
            record(
                "frozen-packet",
                False,
                f"assembled {assembly.packet_sha256[:12]}… vs frozen {str(baseline['packet_sha256'])[:12]}…",
            )
            raise Failed("E2E-DIGEST", "the assembled packet does not match the frozen packet digest")
        record("frozen-packet", True, f"packet sha256 {assembly.packet_sha256}")
        if assembly.twin_sha256 != baseline["twin_sha256"]:
            record(
                "frozen-twin",
                False,
                f"assembled {assembly.twin_sha256[:12]}… vs frozen {str(baseline['twin_sha256'])[:12]}…",
            )
            raise Failed("E2E-DIGEST", "the machine twin does not match the frozen twin digest")
        record("frozen-twin", True, f"twin sha256 {assembly.twin_sha256}")
        if [row["claim_id"] for row in assembly.ledger] != baseline["claim_ids"]:
            record("frozen-claims", False, "the claim-id set drifted from the baseline")
            raise Failed("E2E-COUNT", "the claim-id set drifted from the frozen baseline")
        record("frozen-claims", True, f"{len(assembly.ledger)} claim ids match the baseline")
        if [row[0] for row in assembly.glossary] != baseline["glossary_entry_ids"]:
            record("frozen-glossary", False, "the glossary entry-id set drifted from the baseline")
            raise Failed("E2E-COUNT", "the glossary entry-id set drifted from the frozen baseline")
        record("frozen-glossary", True, f"{len(assembly.glossary)} entry ids match the baseline")

        snapshot_after = {rel: measure(root, rel)[0] for rel in V3_READ_SET}
        unchanged = snapshot_before == snapshot_after
        record(
            "preservation",
            unchanged,
            f"the {len(V3_READ_SET)} read-set files are byte-identical before and after the run"
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


def v3_freeze(root, target_dir):
    """Write the v3 frozen baseline (and the packet/twin/run log beside it), printing diffs."""
    assembly = V3Assembly(root)
    problems = v3_preflight(assembly.packet, set(V3_READ_SET))
    if problems:
        raise Failed(problems[0][0], f"refusing to freeze a packet that fails preflight: {problems[0][1]}")
    with tempfile.TemporaryDirectory(prefix="handoff-freeze-") as workdir:
        gate = assembly.run_gate(workdir)
        semantics = assembly.run_semantics(workdir)
    if gate["exit"] != V3_DECLARED["expected_exit"] or gate["findings"]:
        raise Failed("E2E-GATE", f"refusing to freeze: gate exit {gate['exit']} with findings {gate['findings']}")
    expected_scan = {
        "fields": f"{gate['fields']}/{gate['fields_total']}",
        "glossary_entries": gate["glossary_entries"],
        "findings": gate["findings_count"],
    }
    if expected_scan != V3_DECLARED["expected_scan"]:
        raise Failed("E2E-SCAN", f"refusing to freeze: observed scan {expected_scan} != declared {V3_DECLARED['expected_scan']}")
    uncertainty = semantics["uncertainty"]
    links = semantics["links"]
    if uncertainty["exit"] != 0 or uncertainty["findings"]:
        raise Failed("E2E-UNC", f"refusing to freeze: uncertainty findings {uncertainty['findings'][:4]}")
    if links["exit"] != 0 or links["findings"] or links["links_checked"] != links["resolved"]:
        raise Failed(
            "E2E-LINK",
            f"refusing to freeze: links {links['resolved']}/{links['links_checked']} resolved, "
            f"findings {links['findings'][:4]}",
        )

    census = v3_status_census(assembly.ledger)
    baseline = {
        "profile": V3_PROFILE,
        "packet_id": V3_PACKET_ID,
        "packet_version": V3_PACKET_VERSION,
        "frozen_at": datetime.date.today().isoformat(),
        "frozen_by": "tools/exercise-handoff-e2e.py --profile v3",
        **V3_DECLARED,
        "packet_sha256": assembly.packet_sha256,
        "twin_sha256": assembly.twin_sha256,
        "claim_ids": [row["claim_id"] for row in assembly.ledger],
        "glossary_entry_ids": [row[0] for row in assembly.glossary],
        "inputs": {rel: assembly.digests[rel] for rel in V3_READ_SET},
        "field_digests": {name: sha256_text(value) for name, value in sorted(assembly.field_values.items())},
        "v2_subset_digest": assembly.v2_subset_digest,
        "alias_state": assembly.alias_state,
        "uncertainty": {
            "claims": len(assembly.ledger),
            "statuses": census,
            "exit": uncertainty["exit"],
            "findings": len(uncertainty["findings"]),
            "require_oq_findings": len(uncertainty["findings"]),
        },
        "links": {
            "exit": links["exit"],
            "findings": len(links["findings"]),
            "links": links["links_checked"],
            "resolved": links["resolved"],
        },
        "cross_refs": {
            "contract_id": assembly.contract["id"],
            "contract_revision": assembly.contract["revision"],
            "contract_digest": f"sha256:{assembly.digests[CONTRACT]}",
            "component_digests_checked": assembly.component_checked,
            "component_digests_matched": assembly.component_matched,
            "d4_pins_checked": assembly.d4_pins_checked,
            "d4_pins_matched": assembly.d4_pins_matched,
            "gate_exit": gate["exit"],
            "gate_scan": expected_scan,
            "gate_stdout_sha256": sha256_text(gate["stdout"]),
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
            "d4_lexicon": assembly.d4["counts"]["lexicon"],
            "d4_symbols": assembly.d4["counts"]["symbols"],
            "d4_costumes": assembly.d4["counts"]["costumes"],
            "d4_rank_rules": assembly.d4["counts"]["rank_rules"],
            "d4_era_records": assembly.d4["counts"]["era_records"],
            "d4_typed_labels": assembly.d4_labels["labels"],
            "d4_holds": assembly.d4_holds["hold"],
            "d4_edges": sum(1 for row in assembly.edges if row["edge_id"].startswith("D4E-")),
            "d4_claims": sum(1 for row in assembly.ledger if row["claim_id"].startswith("D4-")),
            "claims": len(assembly.ledger),
            "edges": len(assembly.edges),
        },
        "declared_expectation": V3_DECLARED_EXPECTATION,
        "limits": V3_BASELINE_LIMITS,
    }
    baseline["baseline_digest"] = v3_baseline_digest(baseline)

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
    (target / "twin.json").write_text(assembly.twin_text, encoding="utf-8")
    run_log = [
        f"exercise: tools/exercise-handoff-e2e.py --profile v3 ({V3_PROFILE}, packet {V3_PACKET_ID} {V3_PACKET_VERSION})",
        f"gate: python3 {GATE} packet.md (isolated copy, foreign working directory)",
        f"gate verdict: exit {gate['exit']}, fields={gate['fields']}/{gate['fields_total']}, "
        f"glossary-entries={gate['glossary_entries']}, findings={gate['findings_count']}",
        f"semantics: {UNCERTAINTY_TOOL} exit {uncertainty['exit']} (claims {uncertainty['claims']}); "
        f"{LINKS_TOOL} exit {links['exit']} ({links['resolved']}/{links['links_checked']} links resolved)",
        f"v2-subset digest: {assembly.v2_subset_digest}",
        f"alias evidence state: {assembly.alias_state}",
        f"packet sha256: {assembly.packet_sha256}",
        f"twin sha256: {assembly.twin_sha256}",
        f"read set: {len(V3_READ_SET)} files measured; component digests {assembly.component_matched}/"
        f"{assembly.component_checked} matched; d4 tree pins {assembly.d4_pins_matched}/{assembly.d4_pins_checked}",
    ]
    for leg in assembly.d4_legs:
        run_log.append(f"d4 leg: {leg['command']} exit {leg['exit']} — {leg['observed']}")
    run_log.extend(gate["stdout"].strip().splitlines())
    (target / "run.log").write_text("\n".join(run_log) + "\n", encoding="utf-8")
    diff = []
    if previous:
        for key in ("packet_sha256", "twin_sha256", "claim_ids", "glossary_entry_ids", "v2_subset_digest", "alias_state"):
            if previous.get(key) != baseline[key]:
                diff.append(f"re-frozen {key}: {str(previous.get(key))[:40]}… -> {str(baseline[key])[:40]}…")
        for rel, digest in sorted(baseline["inputs"].items()):
            if previous.get("inputs", {}).get(rel) != digest:
                diff.append(f"re-frozen input {rel}: {str(previous.get('inputs', {}).get(rel))[:12]}… -> {digest[:12]}…")
    freeze_lines = [
        f"frozen: {baseline['frozen_at']} by tools/exercise-handoff-e2e.py --profile v3",
        f"packet_sha256: {assembly.packet_sha256}",
        f"twin_sha256: {assembly.twin_sha256}",
        f"gate: exit {gate['exit']}, fields={gate['fields']}/{gate['fields_total']}, "
        f"glossary-entries={gate['glossary_entries']}, findings={gate['findings_count']}",
        f"semantics: uncertainty exit {uncertainty['exit']}, links {links['resolved']}/{links['links_checked']} resolved",
        f"claims: {len(assembly.ledger)} statuses {census['supported']}/{census['partial']}/{census['unresolved']}; "
        f"v2-subset {assembly.v2_subset_digest[:16]}…; alias leg {assembly.alias_state}",
        f"read set: {len(V3_READ_SET)} files; component digests {assembly.component_matched}/{assembly.component_checked}; "
        f"d4 pins {assembly.d4_pins_matched}/{assembly.d4_pins_checked}",
    ]
    freeze_lines.extend(diff or ["no tracked value changed since the previous freeze"])
    (target / "freeze.txt").write_text("\n".join(freeze_lines) + "\n", encoding="utf-8")
    return baseline, previous, diff, freeze_lines


def v3_build_fixture_root(workdir):
    """A throwaway copy of every file the v3 exercise reads or re-measures."""
    fixture = Path(workdir) / "fixture"
    components = (
        set(v1_mine_d2(ROOT)["components"]) | set(v1_mine_d3(ROOT)["components"]) | set(v3_mine_d4(ROOT)["components"])
    )
    for rel in (*V3_READ_SET, GATE, *sorted(components)):
        source = ROOT / rel
        if not source.is_file():
            raise MissingArtifact(f"selftest fixture source missing: {rel}")
        target = fixture / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    return fixture


def v3_freezed_copy(fixture, workdir, name="frozen"):
    target = Path(workdir) / name
    shutil.copytree(fixture, target)
    baseline, _, _, _ = v3_freeze(target, target / V3_FROZEN_DIR_DEFAULT)
    return target, baseline


def v3_selftest():
    results = []
    for minimum in (50, 12):
        for count in (minimum, minimum + 82):
            leg = {"exit": EXIT_PASS, "observed": f"selftest: {count}/{count} checks passed — controls"}
            assert v3_selftest_witness(leg, minimum), leg
        for code, observed in (
            (EXIT_PASS, f"selftest: {minimum - 1}/{minimum} checks passed"),
            (EXIT_PASS, f"selftest: {minimum - 1}/{minimum - 1} checks passed"),
            (EXIT_PASS, f"unparsed output mentioning {minimum}/{minimum}"),
            (EXIT_PASS, "selftest: 0/0 checks passed"),
            (EXIT_FAIL, f"selftest: {minimum}/{minimum} checks passed"),
        ):
            leg = {"exit": code, "observed": observed}
            assert not v3_selftest_witness(leg, minimum), leg
    results.append("selftest witnesses: expanded complete suites accepted; partial, undersized, unparsed and nonzero-exit suites refused")
    with tempfile.TemporaryDirectory(prefix="handoff-selftest-") as workdir:
        fixture = v3_build_fixture_root(workdir)
        frozen_root, baseline = v3_freezed_copy(fixture, workdir, "frozen-root")
        baseline_rel = V3_FROZEN_DIR_DEFAULT + "/expected.json"

        code, err, records = v3_exercise(root=frozen_root, baseline_rel=baseline_rel)
        assert code == EXIT_PASS, [(r["check"], r["detail"]) for r in records if not r["ok"]]
        scan = next(r["detail"] for r in records if r["check"] == "gate-scan")
        assert "fields=16/16" in scan and "glossary-entries=20" in scan and "findings=0" in scan, scan
        semantic = next(r["detail"] for r in records if r["check"] == "semantic-links")
        assert "links resolved" in semantic, semantic
        census = next(r["detail"] for r in records if r["check"] == "uncertainty-census")
        results.append(f"positive: exit 0 — {scan}; {semantic}; {census}")

        run = subprocess.run(
            [sys.executable, str(ROOT / "tools/exercise-handoff-e2e.py"), "--profile", "v3", "--root",
             str(frozen_root), "--quiet"],
            cwd=workdir,
            capture_output=True,
            text=True,
        )
        assert run.returncode == EXIT_PASS, (run.returncode, run.stdout, run.stderr)
        assert "handoff-v3: exit=0" in run.stdout, run.stdout
        results.append("isolation: the v3 CLI run from a foreign cwd exits 0 with the same scan")

        assembly = V3Assembly(frozen_root)
        packet = assembly.packet
        expected_edges = v3_load_v2_edges(frozen_root)
        v2_edge_ids = {row["edge_id"] for row in expected_edges}
        for surface, edges in (("Markdown", assembly.edges), ("twin", assembly.twin["coupling_edges"])):
            assert [row for row in edges if row["edge_id"] in v2_edge_ids] == expected_edges, surface
            victim = edges[0]
            original = dict(victim)
            for field, value in (("declared_in", None), ("declared_in", "wrong-packet.yml"),
                                 ("mechanism", original["mechanism"][:300]),
                                 ("limits", original["limits"][:320])):
                try:
                    if value is None:
                        victim.pop(field)
                    else:
                        victim[field] = value
                    try:
                        assembly.assert_subset_equality()
                        raised = None
                    except Failed as exc:
                        raised = exc.code
                        assert surface in str(exc), str(exc)
                    assert raised == "E2E-DIGEST", (surface, field, raised)
                finally:
                    victim.clear()
                    victim.update(original)
                results.append(f"edge carry {surface} {field} {value is None and 'dropped' or 'changed'}: E2E-DIGEST")
        results.append("edge carry: all 34 v2 edge rows equal the filed source in Markdown and twin, including declared_in and full text")

        edge_root = Path(workdir) / "edge-source-root"
        for rel in (V2_PACKET_YML, LINKS_TOOL):
            target = edge_root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(frozen_root / rel, target)
        reader = runpy.run_path(str(edge_root / LINKS_TOOL))
        edge_source = reader["read_packet"](edge_root / V2_PACKET_YML)
        edge_source["coupling_edges"][0]["declared_in"] = "alternate-root-witness.yml"
        (edge_root / V2_PACKET_YML).write_text(json.dumps(edge_source), encoding="utf-8")
        carried = v3_build_edge_rows(assembly.d2, assembly.d3, assembly.d4, root=edge_root)
        assert carried[:34] == edge_source["coupling_edges"], "v2 edges were read outside the selected root"
        results.append("edge carry root: the generator reads the selected root's v2 edges, not module ROOT")

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
            mutated(packet, "| scope | three unbound design drills", "| scope | - |\n| scope-unused | three unbound design drills"),
            EXIT_FAIL, ["HO-EMPTY"],
        )
        gate_case(
            "malformed-03 floating version",
            mutated(packet, f"- {CONTRACT} @sha256:", f"- {CONTRACT} @latest (@sha256:"),
            EXIT_FAIL, ["HO-DEP-FLOAT"],
        )
        canon_stripped = re.sub(r"not canonized", "kept as a working record", packet)
        assert canon_stripped != packet, "control anchor failed"
        gate_case(
            "malformed-04 canon marker removed",
            canon_stripped,
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
        gate_case(
            "m10 basis cell tripping the canon-verb trap",
            mutated(packet, "grounding: examples/culture-d4/packet.d4.yml#era_records", "grounding: certifies canon (control) examples/culture-d4/packet.d4.yml#era_records"),
            EXIT_FAIL, ["HO-CANON-CLAIM"],
        )

        read_paths = set(V3_READ_SET)
        problems = v3_preflight(packet, read_paths)
        assert problems == [], problems

        dropped = "\n".join(line for line in packet.splitlines() if not line.startswith("| D4-CL12 |")) + "\n"
        problems = v3_preflight(dropped, read_paths)
        assert any(code == "E2E-COUNT" for code, _ in problems), problems
        results.append("m1 dropped D4 claim row: preflight exits E2E-COUNT")

        off_vocab = mutated(packet, "| D4-CL01 | designer interpretation | invented | supported |", "| D4-CL01 | designer interpretation | invented | tentative |")
        problems = v3_preflight(off_vocab, read_paths)
        assert any(code == "E2E-UNC" for code, _ in problems), problems
        results.append("m2 off-vocabulary D4 status: preflight exits E2E-UNC")

        rows = parse_ledger(packet)
        basis_a = next(row["uncertainty_basis"] for row in rows if row["claim_id"] == "D4-CL01")
        basis_b = next(row["uncertainty_basis"] for row in rows if row["claim_id"] == "D4-CL02")
        duplicated = packet.replace(basis_b, basis_a)
        problems = v3_preflight(duplicated, read_paths)
        assert any(code == "E2E-UNC" and "duplicates" in message for code, message in problems), problems
        results.append("m3 duplicated D4 basis: preflight exits E2E-UNC")

        no_restriction = mutated(packet, "restriction: five slots owe", "note: five slots owe")
        problems = v3_preflight(no_restriction, read_paths)
        assert any(code == "E2E-UNC" and "restriction:" in message for code, message in problems), problems
        results.append("m4 partial row without restriction: preflight exits E2E-UNC")

        no_owner = mutated(packet, "owner: kotodama, blocking for the affected D2 rank records", "lane: kotodama, blocking for the affected D2 rank records")
        problems = v3_preflight(no_owner, read_paths)
        assert any(code == "E2E-UNC" and "owner:" in message for code, message in problems), problems
        results.append("m5 unresolved row without owner: preflight exits E2E-UNC")

        outside = mutated(packet, "examples/culture-d4/brief.md; examples/culture-d4/components/01-brief.yml#handoff_recipient", "docs/outside.md; examples/culture-d4/components/01-brief.yml#handoff_recipient")
        problems = v3_preflight(outside, read_paths)
        assert any(code == "E2E-LINK" for code, _ in problems), problems
        results.append("m7 link to a file outside the v3 read set: preflight exits E2E-LINK")

        extra_glossary = packet.replace("| L20 |", "| L21 | control | control | control | status: constructed |\n| L20 |")
        problems = v3_preflight(extra_glossary, read_paths)
        assert any(code == "E2E-SCAN" for code, _ in problems), problems
        results.append("m9 extra glossary row: preflight exits E2E-SCAN")

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            bad_twin = json.loads(assembly.twin_text)
            bad_twin["claim_ledger"][0]["links"] = ["examples/culture-d4/packet.d4.yml#ER-99"]
            isolated = Path(control_dir) / "isolated"
            isolated.mkdir(parents=True, exist_ok=True)
            twin_path = isolated / "twin.json"
            twin_path.write_text(json.dumps(bad_twin, indent=1, sort_keys=True) + "\n", encoding="utf-8")
            run = subprocess.run(
                [sys.executable, str(frozen_root / LINKS_TOOL), "--packet", str(twin_path),
                 "--repo-root", str(frozen_root), "--json"],
                cwd=str(isolated), capture_output=True, text=True,
            )
            payload = json.loads(run.stdout)
        assert run.returncode == 1 and payload["findings"], (run.returncode, payload)
        results.append(
            f"m6 dangling selector in the twin: {LINKS_TOOL} exit {run.returncode} with "
            f"{'+'.join(sorted({row['code'] for row in payload['findings']}))}"
        )

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            bad_twin = json.loads(assembly.twin_text)
            bad_twin["claim_ledger"][0]["uncertainty"]["status"] = "tentative"
            isolated = Path(control_dir) / "isolated"
            isolated.mkdir(parents=True, exist_ok=True)
            twin_path = isolated / "twin.json"
            twin_path.write_text(json.dumps(bad_twin, indent=1, sort_keys=True) + "\n", encoding="utf-8")
            run = subprocess.run(
                [sys.executable, str(frozen_root / UNCERTAINTY_TOOL), "--packet", str(twin_path),
                 "--require-oq", "--json"],
                cwd=str(isolated), capture_output=True, text=True,
            )
            payload = json.loads(run.stdout)
        assert run.returncode == 1 and "U-STATUS-VOCAB" in {row["code"] for row in payload["findings"]}, payload
        results.append(f"m2b off-vocabulary status in the twin: {UNCERTAINTY_TOOL} exit 1 with U-STATUS-VOCAB")

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            m11_root = Path(control_dir) / "m11"
            shutil.copytree(frozen_root, m11_root)
            victim = m11_root / CLAIMS_MAP
            edited = victim.read_text(encoding="utf-8").replace(
                "the run evidence is tools/assemble-d4-typed.py --selftest exit 0 with 12/12 checks",
                "the run evidence is stated but not run",
            )
            assert edited != victim.read_text(encoding="utf-8"), "m11 anchor failed"
            victim.write_text(edited, encoding="utf-8")
            try:
                V3Assembly(m11_root)
                raised = None
            except Failed as exc:
                raised = exc.code
        assert raised == "E2E-UNC", raised
        results.append("m11 D4-CL08 supported without the run witness: assembly exits E2E-UNC")

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

        before = {rel: measure(frozen_root, rel)[0] for rel in V3_READ_SET}
        v3_exercise(root=frozen_root, baseline_rel=baseline_rel)
        after = {rel: measure(frozen_root, rel)[0] for rel in V3_READ_SET}
        assert before == after, "a read-set file changed during the run"
        results.append(f"preservation: the {len(V3_READ_SET)} read-set files are byte-identical before and after a run")

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            tampered_root, _ = v3_freezed_copy(fixture, control_dir, "tampered-baseline")
            victim = tampered_root / baseline_rel
            edited = json.loads(victim.read_text(encoding="utf-8"))
            edited["packet_sha256"] = "0" * 64
            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
            code, err, records = v3_exercise(root=tampered_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_UNEVALUATED, "E2E-BASELINE"), (code, err, records)
        results.append("m12a tamper baseline: exit 2 E2E-BASELINE (integrity digest mismatch), never a pass")

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            drifted_root, _ = v3_freezed_copy(fixture, control_dir, "drifted-input")
            victim = drifted_root / D4_TYPED_LABELS
            victim.write_text(victim.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            code, err, records = v3_exercise(root=drifted_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_FAIL, "E2E-DIGEST"), (code, err, records)
        results.append("m12b tamper read-set (D4 projection): exit 1 E2E-DIGEST naming the changed file")

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            v2_root, _ = v3_freezed_copy(fixture, control_dir, "retouched-v2")
            victim = v2_root / V2_PACKET_YML
            victim.write_text(victim.read_text(encoding="utf-8").replace("status: \"supported\"", "status: \"partial\"", 1), encoding="utf-8")
            code, err, records = v3_exercise(root=v2_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_FAIL, "E2E-DIGEST"), (code, err, records)
        results.append("m8 re-typed v2 row: exit 1 E2E-DIGEST (v2 twin digest-pinned, subset equality enforced)")

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            scan_root, _ = v3_freezed_copy(fixture, control_dir, "scan-disagreement")
            victim = scan_root / baseline_rel
            edited = json.loads(victim.read_text(encoding="utf-8"))
            edited["expected_scan"]["glossary_entries"] = 21
            edited["baseline_digest"] = v3_baseline_digest(edited)
            victim.write_text(json.dumps(edited, indent=1, sort_keys=True) + "\n", encoding="utf-8")
            code, err, records = v3_exercise(root=scan_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_UNEVALUATED, "E2E-BASELINE"), (code, err, records)
        results.append("tamper scan expectation: exit 2 E2E-BASELINE (a re-signed expectation is refused, not honoured)")

        with tempfile.TemporaryDirectory(prefix="handoff-control-") as control_dir:
            missing_root = Path(control_dir) / "missing"
            shutil.copytree(frozen_root, missing_root)
            (missing_root / D4_PACKET).unlink()
            code, err, records = v3_exercise(root=missing_root, baseline_rel=baseline_rel)
        assert (code, err) == (EXIT_UNEVALUATED, "E2E-ARTIFACT"), (code, err, records)
        results.append("missing D4 artifact: exit 2 E2E-ARTIFACT naming the unreadable path")

    census = baseline["uncertainty"]["statuses"]
    print(
        f"selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0, "
        f"links={baseline['links']['resolved']}/{baseline['links']['links']}, claims={baseline['uncertainty']['claims']}, "
        f"statuses={census['supported']}/{census['partial']}/{census['unresolved']}, "
        f"v2_subset=equal, alias_leg={baseline['alias_state']}) plus {len(results) - 1} controls:"
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
            "Assemble a handoff packet from the live drill artifacts and validate it. Profiles: v1 "
            "(default, round-11 path), v2 (verify the filed round-15 surfaces), v3 (D2/D3/D4 triple "
            "drill with the v2 uncertainty and link semantics)."
        ),
    )
    parser.add_argument("--profile", choices=("v1", "v2", "v3"), default="v1",
                        help="which exercise path to run (default v1, the filed round-11 path)")
    parser.add_argument("--selftest", action="store_true", help="run the positive run and the control matrix")
    parser.add_argument("--root", metavar="DIR", help="alternate repo root holding the read set")
    parser.add_argument("--baseline", metavar="PATH", help="baseline override (profile default otherwise)")
    parser.add_argument("--keep", metavar="DIR", help="keep the isolated packet directory at DIR")
    parser.add_argument("--json", action="store_true", help="print a receipt document on stdout")
    parser.add_argument("--freeze", metavar="DIR", help="(re)write the frozen baseline into DIR, printing diffs")
    parser.add_argument("--quiet", action="store_true", help="print only the summary line")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve() if args.root else ROOT

    if args.profile == "v2":
        if args.freeze:
            print("could not freeze: E2E-DATA the v2 baseline is a filed round-15 artifact (read-only)")
            return EXIT_UNEVALUATED
        code, err, records = v2_verify(root)
        if not args.quiet:
            for item in records:
                print(f"{'OK  ' if item['ok'] else 'FAIL'} {item['check']}: {item['detail']}")
        links = next((item["detail"] for item in records if item["check"] == "links"), "")
        counts = re.search(r"(\d+)/(\d+) links resolved", links)
        claims = next((item["detail"] for item in records if item["check"] == "uncertainty"), "")
        claim_count = re.search(r"claims=(\d+)", claims)
        print(
            f"handoff-v2: exit={code} claims={claim_count.group(1) if claim_count else '?'} "
            f"links={counts.group(1) + '/' + counts.group(2) if counts else '?'} "
            f"drift=named(tools/harness/packet_links.py round-16)"
        )
        if err and not args.quiet:
            print(f"handoff-v2: {err}: {records[-1]['detail'] if records else ''}")
        if args.json:
            print(json.dumps({"profile": "v2", "root": str(root), "exit": code, "code": err, "checks": records},
                             indent=1, sort_keys=True, ensure_ascii=False))
        return code

    if args.profile == "v1":
        baseline_default, frozen_default = V1_BASELINE_DEFAULT, V1_FROZEN_DIR_DEFAULT
        if args.selftest:
            return v1_selftest()
        if args.freeze:
            try:
                baseline, previous, diff, freeze_lines = v1_freeze(root, args.freeze)
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
        code, err, records = v1_exercise(root=root, baseline_rel=args.baseline or baseline_default)
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
            print(json.dumps({"profile": "v1", "root": str(root), "baseline": args.baseline or baseline_default,
                              "exit": code, "code": err, "checks": records},
                             indent=1, sort_keys=True, ensure_ascii=False))
        return code

    baseline_default, frozen_default = V3_BASELINE_DEFAULT, V3_FROZEN_DIR_DEFAULT
    if args.selftest:
        return v3_selftest()
    if args.freeze:
        try:
            baseline, previous, diff, freeze_lines = v3_freeze(root, args.freeze)
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
    code, err, records = v3_exercise(root=root, baseline_rel=args.baseline or baseline_default)
    if not args.quiet:
        for item in records:
            print(f"{'OK  ' if item['ok'] else 'FAIL'} {item['check']}: {item['detail']}")
    scan = next((item["detail"] for item in records if item["check"] == "gate-scan"), "gate not reached")
    packet_sha = next((item["detail"] for item in records if item["check"] == "frozen-packet"), "")
    matches = re.search(r"([0-9a-f]{64})", packet_sha)
    fields = re.search(r"fields=(\d+/\d+)", scan)
    glossary = re.search(r"glossary-entries=(\d+)", scan)
    findings = re.search(r"findings=(\d+)", scan)
    links = next((item["detail"] for item in records if item["check"] == "semantic-links"), "")
    link_counts = re.search(r"(\d+)/(\d+) links resolved", links)
    census = next((item["detail"] for item in records if item["check"] == "uncertainty-census"), "")
    census_counts = re.search(r"claims=(\d+) statuses=(\d+)/(\d+)/(\d+)", census)
    subset = "equal" if any(item["check"] == "v2-subset" and item["ok"] for item in records) else "unequal"
    alias = next((item["detail"].split(": ")[-1] for item in records if item["check"] == "alias-leg"), "?")
    print(
        f"handoff-v3: exit={code} fields={fields.group(1) if fields else '?'} "
        f"glossary={glossary.group(1) if glossary else '?'}/20 findings={findings.group(1) if findings else '?'} "
        f"links={link_counts.group(1) + '/' + link_counts.group(2) if link_counts else '?'} "
        f"claims={census_counts.group(1) if census_counts else '?'} "
        f"statuses={census_counts.group(2) + '/' + census_counts.group(3) + '/' + census_counts.group(4) if census_counts else '?'} "
        f"v2_subset={subset} alias_leg={alias} "
        f"packet_sha256={matches.group(1) if matches else '(not assembled)'}"
    )
    if err and not args.quiet:
        print(f"handoff-v3: {err}: {records[-1]['detail'] if records else ''}")
    if args.json:
        print(json.dumps({"profile": "v3", "root": str(root), "baseline": args.baseline or baseline_default,
                          "exit": code, "code": err, "checks": records},
                         indent=1, sort_keys=True, ensure_ascii=False))
    return code


if __name__ == "__main__":
    sys.exit(main())
