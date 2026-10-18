#!/usr/bin/env python3
"""Assemble the D4 NON-CANON culture packet from the round-17 component registry.

Run from any directory: python3 tools/assemble-culture-d4.py [--check | --selftest]

Merges the component files under examples/culture-d4/components/ (12 required,
per the round-17 D4 registry: `reports/round-17/d4/design-brief.md` §5 and the
component fragments the integrator lands) into exactly one deterministic output
this tool owns:

    examples/culture-d4/packet.d4.yml    gate-facing D4 packet

Contract rules baked in:

  - component files are parsed with the costume gate's stdlib YAML-subset reader
    (loaded read-only via runpy); no third-party dependency is added and JSON
    components parse under the same reader; block-scalar prose (key: | / key: >-)
    is elided to a quoted placeholder first, because the subset reader reads
    indented continuation lines as mapping entries and component prose contains
    colons;
  - a component's own top-level `packet_keys:` declaration (else the
    PACKET_KEYS allowlist) fixes its packet contribution; every other top-level
    key is per-file design metadata and is recorded under
    `assembly.skipped_keys` with the files that declared it — nothing is merged
    silently and nothing is dropped invisibly;
  - a block declared by two components with unequal values is a hard collision
    (exit 2); equal duplicates collapse;
  - the required blocks (phonology, lexicon, names, eras, costumes, materials)
    must be present, typed, non-empty and record-shaped, with unique record ids
    and the declared minimum counts; anything missing fails closed before any
    write;
  - `name`, `canon` and `assembly` are packet-owned; the packet declares
    NON-CANON and carries no real-world clearance or rights statement;
  - the `assembly` block pins every component digest, the reader and serializer
    digests, and this tool's own digest (self-pin, the D3 serializer_sha256
    precedent), so a changed component or tool is drift, never a silent edit.

--check compares bytes without writing: exit 0 equal / 1 drift / 2 error. A
missing or malformed component fails closed with exit 2 before any write.
--selftest drives this same CLI over a fixture component tree inside one
temporary directory (positive, tamper, malformed and missing controls, plus
collision, duplicate-id, wrong-type, below-minimum and too-few-files controls);
it touches no file outside that directory. `assemble()` is the callable build
path the D4 typed adapter's assembler-identity leg calls (never re-implemented).
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import runpy
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
COMPONENTS = ROOT / "examples/culture-d4/components"
PACKET = ROOT / "examples/culture-d4/packet.d4.yml"
READER = ROOT / "tools/gates/costume-era-consistency-gate.py"
SERIALIZER = ROOT / "tools/assemble-d2.py"

PACKET_NAME = "D4 culture drill — round-17 design build (NON-CANON)"
CANON = "not canonized (D4 NON-CANON design drill)"
MINIMUM_COMPONENTS = 12
SUFFIXES = (".yml", ".yaml", ".json")

# Packet-shaped top-level blocks, in deterministic emission order: the D2
# packet key set (`reports/round-17/d4/design-brief.md` §5 R15), the round-17
# D4 component registry's packet_keys (`reports/round-17/d4/components/
# 01-brief.yml` C-01..C-12), and the block names the parallel D4 design
# families may declare. A component may also fix its own contribution with a
# top-level `packet_keys:` list; that declaration is honored per file. Any
# other component top-level key is per-file metadata and is recorded under
# assembly.skipped_keys, never merged.
PACKET_KEYS = (
    "contract",
    "phonology", "morphology", "script", "orthography",
    "lexicon", "layers", "constructions", "cloth_sources",
    "registers", "doublets", "sayings", "oaths",
    "pantheon", "roles", "motifs", "narratives", "myths",
    "rituals", "ritual", "calendar", "festivals", "rites", "symbols",
    "materials", "measures", "costumes", "rank_rules",
    "eras", "era_records", "era_dates", "source_era_dates", "named_eras",
    "names", "cross_culture_review", "form_slots", "typed_labels",
    "references", "bridges", "screening",
    "canon_status", "handoff_status", "scope_notes", "provenance",
    "contact", "routes",
)

REQUIRED_BLOCKS = {
    "phonology": dict,
    "lexicon": list,
    "names": list,
    "eras": list,
    "costumes": list,
    "materials": list,
}

MINIMUM_COUNTS = {
    "lexicon": 1,
    "names": 1,
    "eras": 1,
    "costumes": 1,
    "materials": 1,
}

RECORD_FIELDS = {
    "lexicon": ("id", "term", "gloss"),
    "names": ("id", "name"),
    "costumes": ("id", "garment", "material", "era"),
    "materials": ("id",),
    "eras": ("id",),
    "symbols": ("id",),
    "rank_rules": ("id",),
    "layers": ("id",),
    "registers": ("id",),
    "measures": ("id",),
    "sayings": ("id",),
    "oaths": ("id",),
    "doublets": ("id",),
    "era_records": ("id",),
    "constructions": ("id",),
    "cloth_sources": ("id",),
}


def fail(message):
    raise ValueError(message)


def digest_bytes(data):
    return hashlib.sha256(data).hexdigest()


def file_digest(path):
    if not path.is_file():
        fail(f"required file not found: {path.relative_to(ROOT)}")
    return digest_bytes(path.read_bytes())


def reader_parse():
    """The costume gate's reader, with its Malformed turned into a ValueError."""
    if not READER.is_file():
        fail(f"component reader not found: {READER.relative_to(ROOT)}")
    namespace = runpy.run_path(str(READER))
    parse = namespace["parse_packet"]
    malformed = namespace["Malformed"]

    def parse_document(text):
        try:
            return parse(text)
        except malformed as exc:
            raise ValueError(str(exc)) from exc

    return parse_document


def yaml_lines_serializer():
    """The D2 assembler's yaml_lines, loaded read-only; no dependency added."""
    if not SERIALIZER.is_file():
        fail(f"yaml serializer not found: {SERIALIZER.relative_to(ROOT)}")
    namespace = runpy.run_path(str(SERIALIZER))
    lines = namespace.get("yaml_lines")
    if not callable(lines):
        fail("tools/assemble-d2.py does not expose a callable yaml_lines")
    return lines


BLOCK_SCALAR_RE = re.compile(
    r"^(\s*)([A-Za-z_][\w-]*)\s*:\s*[|>][-+]?\s*$")


def elide_block_scalars(text):
    """Neutralize block-scalar prose before the stdlib subset reader sees it.

    The costume gate's reader (the lane's stdlib YAML subset) treats an indented
    continuation line as a mapping entry, so a `key: >-` / `key: |` prose block
    whose text contains a colon is a parse error — and the D4 component seats
    write such prose blocks (scope, notes, rationale) in every file. The shim
    replaces each block scalar's header with a quoted placeholder and drops its
    continuation lines; a packet block declared as a block scalar therefore
    arrives as a string and fails validate_blocks closed, never silently.
    Returns the neutralized text and the count of elided scalars.
    """
    lines = text.splitlines()
    out = []
    elided = 0
    index = 0
    while index < len(lines):
        match = BLOCK_SCALAR_RE.match(lines[index])
        if not match:
            out.append(lines[index])
            index += 1
            continue
        indent = len(match.group(1))
        out.append(f"{match.group(1)}{match.group(2)}: "
                   f"\"<block scalar elided by tools/assemble-culture-d4.py>\"")
        elided += 1
        index += 1
        while index < len(lines):
            line = lines[index]
            if not line.strip():
                index += 1
                continue
            if len(line) - len(line.lstrip()) > indent:
                index += 1
                continue
            break
    return "\n".join(out) + ("\n" if text.endswith("\n") else ""), elided


def component_files():
    """The component registry on disk: >= 12 parseable component files."""
    if not COMPONENTS.is_dir():
        fail(f"components directory not found: {COMPONENTS.relative_to(ROOT)}")
    files = sorted((path for path in COMPONENTS.iterdir()
                    if path.is_file() and path.suffix.lower() in SUFFIXES),
                   key=lambda path: path.name)
    if len(files) < MINIMUM_COMPONENTS:
        fail(f"components: {len(files)} component file(s) found, "
             f"{MINIMUM_COMPONENTS} required by the round-17 D4 registry")
    return files


def load_components():
    """Read every component; fail closed on any defect; merge packet blocks.

    A component's own top-level `packet_keys:` list, when declared, fixes that
    file's packet contribution exactly (the round-17 furnace registry's C-01..C-12
    contract); otherwise the PACKET_KEYS allowlist applies. Everything else is
    per-file metadata and is recorded under assembly.skipped_keys.
    """
    parse = reader_parse()
    merged = {}
    owner = {}
    sources = {}
    skipped = {}
    elided = {}
    for path in component_files():
        relative = path.relative_to(ROOT).as_posix()
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            fail(f"{path.name}: not valid UTF-8 ({exc})")
        neutralized, elided_count = elide_block_scalars(text)
        if elided_count:
            elided[relative] = elided_count
        try:
            document = parse(neutralized)
        except ValueError as exc:
            fail(f"{path.name}: {exc}")
        if not isinstance(document, dict) or not document:
            fail(f"{path.name}: root must be a non-empty mapping")
        sources[relative] = digest_bytes(raw)
        declared = document.get("packet_keys")
        if isinstance(declared, list) and all(isinstance(item, str) for item in declared):
            contributes = set(declared)
        else:
            contributes = set(PACKET_KEYS)
        for key, value in document.items():
            if key not in contributes or key == "packet_keys":
                skipped.setdefault(key, []).append(relative)
                continue
            if key in merged:
                if merged[key] == value:
                    continue
                fail(f"component collision: {key!r} is declared differently by "
                     f"{owner[key]} and {relative}; refusing to override")
            merged[key] = value
            owner[key] = relative
    return (merged, sources,
            {key: sorted(files) for key, files in sorted(skipped.items())},
            {key: elided[key] for key in sorted(elided)})


def validate_blocks(merged):
    """Fail closed on missing, mistyped, empty or record-broken packet blocks."""
    for key, wanted in REQUIRED_BLOCKS.items():
        value = merged.get(key)
        if value is None:
            fail(f"missing required block {key!r}: no component declares it")
        if wanted is dict:
            if not isinstance(value, dict) or not value:
                fail(f"{key}: expected a non-empty mapping")
            continue
        if not isinstance(value, list) or not value:
            fail(f"{key}: expected a non-empty record list")
    for key, value in sorted(merged.items()):
        if isinstance(value, bool):
            fail(f"{key}: expected a block, not a boolean")
        if not isinstance(value, (dict, list)):
            fail(f"{key}: expected a mapping or record list, got {type(value).__name__}")
        if not value and (key in REQUIRED_BLOCKS or key in RECORD_FIELDS):
            fail(f"{key}: block is empty; an empty declared block is refused")
        if isinstance(value, list):
            if key in RECORD_FIELDS and not (key == "eras" and value and
                                             all(isinstance(item, str) for item in value)):
                for index, record in enumerate(value):
                    if not isinstance(record, dict):
                        fail(f"{key}[{index}]: record is not a mapping")
            ids = [record.get("id") for record in value
                   if isinstance(record, dict) and "id" in record]
            if ids and not all(isinstance(record_id, str) and record_id for record_id in ids):
                fail(f"{key}: every declared id must be a non-empty string")
            if len(ids) != len(set(ids)):
                fail(f"{key}: duplicate record IDs; refusing silent deduplication")
    for key, minimum in sorted(MINIMUM_COUNTS.items()):
        records = merged[key]
        if len(records) < minimum:
            fail(f"{key}: {len(records)} records, below the declared minimum "
                 f"of {minimum}")
    for key, fields in sorted(RECORD_FIELDS.items()):
        records = merged.get(key)
        if not isinstance(records, list):
            continue
        for index, record in enumerate(records):
            if not isinstance(record, dict):
                continue
            missing = [field for field in fields if field not in record]
            if missing:
                fail(f"{key}[{index}]: missing field(s) {missing} needed by the "
                     f"gate-facing packet")


def build_packet(merged, sources, skipped, elided):
    """Packet-owned keys plus the merged blocks plus the pin block."""
    normalizations = [
        "component files are parsed with the costume gate's stdlib YAML-subset "
        "reader (read-only); a component's own packet_keys declaration (or the "
        "PACKET_KEYS allowlist) fixes its packet contribution; every other "
        "component key is recorded under assembly.skipped_keys",
        "packet-owned keys name/canon/assembly are constants of "
        "tools/assemble-culture-d4.py; component declarations of them are "
        "recorded under assembly.skipped_keys, never merged",
        "block-scalar prose (key: | / key: >- at any depth) is elided to a "
        "quoted placeholder before the reader, because the stdlib subset "
        "reader reads indented continuation lines as mapping entries; the "
        "elided counts are recorded under assembly.block_scalars_elided and a "
        "packet block declared as a block scalar still fails closed",
        "the packet declares NON-CANON; no real-language sweep, clearance, "
        "canon decision or lore acceptance is claimed or implied",
    ]
    if "era_dates" in merged and "source_era_dates" not in merged:
        merged["source_era_dates"] = merged.pop("era_dates")
        normalizations.append(
            "a component-declared era_dates block is carried as "
            "source_era_dates (the assemble-d2.py precedent: source dates never "
            "ride the gate's numeric era_dates key)")
    if isinstance(merged.get("eras"), list) and merged["eras"] and all(
            isinstance(record, dict) for record in merged["eras"]):
        records = merged["eras"]
        tags = []
        for record in records:
            tag = record.get("tag") or record.get("id")
            if isinstance(tag, str) and tag not in tags:
                tags.append(tag)
        merged["era_records"] = list(merged.get("era_records") or []) + records
        merged["eras"] = tags
        normalizations.append(
            "eras mapping records are emitted as a flat tag list under `eras` "
            "(the typed projector's contract) with the records carried under "
            "`era_records` (the projector's name-mapping block)")
    packet = {"name": PACKET_NAME, "canon": CANON}
    for key in PACKET_KEYS:
        if key in merged:
            packet[key] = merged[key]
    for key in sorted(set(merged) - set(PACKET_KEYS)):
        packet[key] = merged[key]
    packet["assembly"] = {
        "generator": "tools/assemble-culture-d4.py",
        "assembler_sha256": file_digest(Path(__file__).resolve()),
        "reader": "tools/gates/costume-era-consistency-gate.py",
        "reader_sha256": file_digest(READER),
        "serializer": "tools/assemble-d2.py (yaml_lines loaded read-only)",
        "serializer_sha256": file_digest(SERIALIZER),
        "source_sha256": dict(sorted(sources.items())),
        "skipped_keys": skipped,
        "block_scalars_elided": elided,
        "normalizations": normalizations,
        "unresolved": [
            "D4 is a NON-CANON design drill: no real-language sweep was "
            "performed and none is claimed; all forms are constructed and "
            "unscreened",
            "the typed pipeline's hold set, projection and typed packet are "
            "owned by the D4 typed tools, not by this gate-facing packet",
            "design questions raised by parallel component seats remain "
            "reported, never absorbed, by this assembler",
        ],
    }
    return packet


def assemble():
    """The deterministic build path; returns the packet bytes."""
    merged, sources, skipped, elided = load_components()
    validate_blocks(merged)
    packet = build_packet(merged, sources, skipped, elided)
    lines = yaml_lines_serializer()
    return ("\n".join(lines(packet)) + "\n").encode("utf-8")


# --------------------------------------------------------------------------
# selftest fixtures
# --------------------------------------------------------------------------

def _fixture_components():
    """A 12-file registry-shaped fixture tree; deterministic, self-contained."""
    return {
        "01-brief.yml": """\
component: 01-brief
canon: not canonized (D4 NON-CANON fixture)
status: fixture record
registry_note: fixture registry; packet keys fixed by the contract
scope_note: >-
  Fixture prose with a colon: this continuation line must not break the
  reader shim, and it must not become a packet block.
""",
        "02-phonology.yml": """\
component: 02-phonology
phonology:
  consonants: [p, t, k, m, n, s, r, l]
  vowels: [a, e, i, o, u]
  template: "(C)V(C)"
  coda: [n, l, r, s]
  onset_clusters: false
  stress: initial
""",
        "03-morphosyntax.yml": """\
component: 03-morphosyntax
morphology:
  type: agglutinative
  derivation_rules:
  - id: D4-COMPOUND
    kind: compound
    pattern: '^(?P<B1>[a-z]+)[+](?P<B2>[a-z]+)$'
    output: '{B1}{B2}'
""",
        "04-ledger-script.yml": """\
component: 04-ledger-script
script:
  type: stamp-derived
  sign_count: 12
""",
        "05-lexicon.yml": """\
component: 05-lexicon
lexicon:
  - id: L-01
    term: peta
    gloss: grain
    register: plain
  - id: L-02
    term: talu
    gloss: measure
    register: plain
layers:
  - id: LY-1
    label: native
""",
        "06-register-contract.yml": """\
component: 06-register-contract
registers:
  - id: RG-01
    name: plain
  - id: RG-02
    name: quote
doublets:
  - id: DB-01
    plain_slot: L-01#plain
""",
        "07-oaths-sayings.yml": """\
component: 07-oaths-sayings
sayings:
  - id: SA-01
    text: the mark attests
oaths:
  - id: OA-01
    register: plain
""",
        "08-symbols-tokens.yml": """\
component: 08-symbols-tokens
symbols:
  - id: SY-01
    sign: notch
""",
        "09-eras-calendar.yml": """\
component: 09-eras-calendar
eras:
  - id: E0
    name: stamp era
  - id: E1
    name: ledger era
era_records:
  - id: ER-01
    era: E0
""",
        "10-measures-materials.yml": """\
component: 10-measures-materials
materials:
  - id: M-01
    name: local leather
    gate_name: leather
measures:
  - id: MS-01
    unit: weight
""",
        "11-costumes.yml": """\
component: 11-costumes
costumes:
  - id: C-01
    garment: sash
    material: M-01
    era: E0
    wearer_rank: broker
    rite: none
constructions:
  - id: CN-01
    kind: wrap
cloth_sources:
  - id: CS-01
    name: court loom
""",
        "12-ranks-names.yml": """\
component: 12-ranks-names
rank_rules:
  - id: RR-01
    effect: prohibit
    property: {kind: register, value: quote}
names:
  - id: N-01
    name: petalu
    type: person
""",
    }


def selftest():
    """Fixture-driven positive/tamper/malformed/missing controls over the CLI."""
    source = Path(__file__).resolve()
    failures = []
    passed = 0

    def check(label, condition, detail=""):
        nonlocal passed
        if condition:
            passed += 1
        else:
            failures.append(f"{label}: {detail or 'failed'}")

    with tempfile.TemporaryDirectory(prefix="assemble-culture-d4-selftest-") as tmpdir:
        tmp = Path(tmpdir)
        script = tmp / "tools" / "assemble-culture-d4.py"
        script.parent.mkdir(parents=True)
        shutil.copyfile(source, script)
        shutil.copyfile(SERIALIZER, tmp / "tools" / "assemble-d2.py")
        reader = tmp / "tools" / "gates" / "costume-era-consistency-gate.py"
        reader.parent.mkdir(parents=True)
        shutil.copyfile(READER, reader)
        components = tmp / "examples" / "culture-d4" / "components"
        components.mkdir(parents=True)
        packet_out = tmp / "examples" / "culture-d4" / "packet.d4.yml"

        def write_fixtures(files):
            for name, text in files.items():
                (components / name).write_text(text, encoding="utf-8")

        def run(*args):
            return subprocess.run([sys.executable, str(script), *args],
                                  capture_output=True, text=True,
                                  cwd=str(tmp), check=False)

        good = _fixture_components()
        write_fixtures(good)

        # positive control: the real CLI assembles the fixture tree, twice.
        first = run()
        check("positive: CLI exit 0", first.returncode == 0,
              f"exit {first.returncode}: {first.stderr.strip()}")
        check("positive: packet written", "Wrote" in first.stdout and packet_out.exists(),
              first.stdout.strip())
        payload = packet_out.read_bytes() if packet_out.exists() else b""
        check("positive: output present", bool(payload))
        second = run()
        check("positive: second CLI run exit 0", second.returncode == 0,
              second.stderr.strip())
        check("positive: deterministic bytes",
              bool(payload) and packet_out.exists() and packet_out.read_bytes() == payload)

        clean = run("--check")
        check("--check: exit 0 on clean output", clean.returncode == 0,
              f"exit {clean.returncode}: {clean.stderr.strip()}")
        check("--check: byte-identical report", "byte-identical" in clean.stdout,
              clean.stdout.strip())

        # structural controls on the assembled packet.
        parse = reader_parse()
        packet = parse(payload.decode("utf-8"))
        check("packet: profile keys present",
              {"name", "canon", "phonology", "lexicon", "names", "eras",
               "costumes", "materials", "assembly"} <= set(packet),
              sorted(set(packet)))
        check("packet: name is the packet-owned constant",
              packet.get("name") == PACKET_NAME, packet.get("name"))
        check("packet: NON-CANON declared",
              packet.get("canon") == CANON and "NON-CANON" in str(packet.get("canon")),
              packet.get("canon"))
        check("packet: every fixture packet block carried",
              all(key in packet for key in ("script", "layers", "registers", "doublets",
                                            "sayings", "oaths", "symbols", "era_records",
                                            "measures", "rank_rules", "constructions",
                                            "cloth_sources", "morphology")),
              sorted(set(packet)))
        check("packet: fixture metadata never merged",
              "component" not in packet and "status" not in packet
              and "registry_note" not in packet, sorted(set(packet)))
        assembly = packet.get("assembly", {})
        sources = assembly.get("source_sha256", {})
        check("assembly: every fixture source digest recorded",
              sorted(sources) == sorted(f"examples/culture-d4/components/{name}"
                                        for name in good), sorted(sources))
        check("assembly: digests match the fixture files",
              all(sources.get(relative) == digest_bytes(
                  (components / Path(relative).name).read_bytes())
                  for relative in sources))
        check("assembly: skipped keys recorded with their files",
              assembly.get("skipped_keys", {}).get("component")
              == sorted(f"examples/culture-d4/components/{name}" for name in good),
              assembly.get("skipped_keys"))
        check("assembly: block-scalar shim recorded",
              assembly.get("block_scalars_elided")
              == {"examples/culture-d4/components/01-brief.yml": 1},
              assembly.get("block_scalars_elided"))
        check("assembly: elided prose never became a packet block",
              "scope_note" not in packet and packet.get("registry_note") is None,
              sorted(set(packet)))
        check("assembly: generator named", assembly.get("generator")
              == "tools/assemble-culture-d4.py", assembly.get("generator"))
        check("assembly: assembler self-pin matches this script",
              assembly.get("assembler_sha256") == digest_bytes(script.read_bytes()))
        check("assembly: serializer and reader pinned",
              bool(assembly.get("serializer_sha256")) and bool(assembly.get("reader_sha256")))
        check("assembly: no absolute path or timestamp in the bytes",
              str(tmp) not in payload.decode("utf-8", "replace"))
        check("assembly: non-CANON unresolved notes carried",
              any("NON-CANON" in note for note in assembly.get("unresolved", [])),
              assembly.get("unresolved"))

        # tamper control: one changed source byte must fail --check with exit 1.
        tampered = dict(good)
        tampered["02-phonology.yml"] = good["02-phonology.yml"].replace(
            "vowels: [a, e, i, o, u]", "vowels: [a, e, i, o]")
        check("tamper: fixture mutation applied",
              tampered["02-phonology.yml"] != good["02-phonology.yml"])
        write_fixtures(tampered)
        drift = run("--check")
        check("tamper: --check exit 1", drift.returncode == 1,
              f"exit {drift.returncode}: {drift.stderr.strip()}")
        check("tamper: --check names the difference", "differs" in drift.stderr,
              drift.stderr.strip())
        write_fixtures(good)
        restored = run("--check")
        check("tamper: restored fixture passes again", restored.returncode == 0,
              restored.stderr.strip())

        # missing output control: --check exits 1, the default run rebuilds it.
        packet_out.unlink()
        missing_out = run("--check")
        check("missing output: --check exit 1", missing_out.returncode == 1,
              f"exit {missing_out.returncode}: {missing_out.stderr.strip()}")
        regenerated = run()
        check("missing output: regenerated by the default run",
              regenerated.returncode == 0 and packet_out.exists(),
              regenerated.stderr.strip())

        # fail-closed controls, each through the real CLI.
        def reset():
            write_fixtures(good)
            if packet_out.exists():
                packet_out.unlink()

        missing_block = json.loads(json.dumps(good))
        head, sep, _ = good["05-lexicon.yml"].partition("lexicon:")
        assert sep, "fixture must contain the lexicon block"
        missing_block["05-lexicon.yml"] = head + "layers:\n  - id: LY-1\n    label: native\n"
        empty_lexicon = head + "lexicon: []\n"
        wrong_type = head + "lexicon:\n  note: wrapper\n"
        bad_record = head + "lexicon:\n  - plain string record\n"
        empty_optional = "component: 08-symbols-tokens\nsymbols: []\n"
        duplicate_id = head + """\
lexicon:
  - id: L-01
    term: peta
    gloss: grain
  - id: L-01
    term: talu
    gloss: measure
"""
        collision = json.loads(json.dumps(good))
        collision["12-ranks-names.yml"] = good["12-ranks-names.yml"] + \
            "symbols:\n  - id: SY-99\n    sign: foreign\n"
        negatives = [
            ("malformed component", {"06-register-contract.yml": "component: 06\n"
             "registers:\n  - id: RG-01\n    name plain\n"},
             "YAML subset parse error"),
            ("root not a mapping", {"07-oaths-sayings.yml": "- just\n- a list\n"},
             "not one mapping"),
            ("missing required block", missing_block, "missing required block"),
            ("empty block", {"08-symbols-tokens.yml": empty_optional}, "block is empty"),
            ("wrong value type", {"05-lexicon.yml": wrong_type},
             "expected a non-empty record list"),
            ("empty required block", {"05-lexicon.yml": empty_lexicon},
             "expected a non-empty record list"),
            ("record not a mapping", {"05-lexicon.yml": bad_record}, "record is not a mapping"),
            ("duplicate record IDs", {"05-lexicon.yml": duplicate_id}, "duplicate record IDs"),
            ("component collision", collision, "component collision"),
            ("missing field", {"11-costumes.yml": good["11-costumes.yml"].replace(
                "    era: E0\n", "")}, "missing field"),
            ("too few components", None, "12 required"),
        ]
        for label, files, fragment in negatives:
            reset()
            if label == "too few components":
                (components / "01-brief.yml").unlink()
                (components / "04-ledger-script.yml").unlink()
            else:
                write_fixtures(files)
            result = run()
            check(f"negative {label}: exit 2", result.returncode == 2,
                  f"exit {result.returncode}: {result.stderr.strip()}")
            check(f"negative {label}: message names the defect",
                  fragment in result.stderr, result.stderr.strip())
            check(f"negative {label}: no traceback",
                  "Traceback" not in result.stderr, result.stderr.strip())
            check(f"negative {label}: fail closed, no output written",
                  not packet_out.exists())

        # a missing component file, deleted from a complete tree.
        reset()
        (components / "11-costumes.yml").unlink()
        missing = run()
        check("negative missing component: exit 2", missing.returncode == 2,
              f"exit {missing.returncode}: {missing.stderr.strip()}")
        check("negative missing component: message names the count",
              "component file(s) found" in missing.stderr
              and "12 required" in missing.stderr, missing.stderr.strip())
        check("negative missing component: fail closed",
              not packet_out.exists())

        # serializer absent -> fail closed too.
        reset()
        (tmp / "tools" / "assemble-d2.py").unlink()
        no_serializer = run()
        check("negative serializer missing: exit 2", no_serializer.returncode == 2,
              f"exit {no_serializer.returncode}: {no_serializer.stderr.strip()}")
        check("negative serializer missing: fail closed", not packet_out.exists())
        shutil.copyfile(SERIALIZER, tmp / "tools" / "assemble-d2.py")

        # reader absent -> fail closed too.
        reset()
        reader.unlink()
        no_reader = run()
        check("negative reader missing: exit 2", no_reader.returncode == 2,
              f"exit {no_reader.returncode}: {no_reader.stderr.strip()}")
        check("negative reader missing: fail closed", not packet_out.exists())
        shutil.copyfile(READER, reader)

        # fixture tree restored for a final green pass.
        reset()
        final = run()
        check("restored: fixture tree assembles again", final.returncode == 0,
              final.stderr.strip())
        final_check = run("--check")
        check("restored: --check green", final_check.returncode == 0,
              final_check.stderr.strip())

    if failures:
        for failure in failures:
            print(f"selftest FAIL: {failure}", file=sys.stderr)
        print(f"selftest: {passed}/{passed + len(failures)} checks passed",
              file=sys.stderr)
        return 1
    print(f"selftest: {passed}/{passed} checks passed — positive assemble/--check/"
          "determinism, tamper drift, malformed, missing-component and "
          "missing-output controls, plus collision, duplicate-id, wrong-type, "
          "empty-block, missing-field, too-few-files and serializer/reader-absent "
          "fail-closed controls; no file outside the temporary directory touched")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true",
                       help="compare packet.d4.yml against the assembly without writing")
    group.add_argument("--selftest", "--self-test", action="store_true", dest="selftest",
                       help="run the fixture controls in a temporary directory")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    try:
        payload = assemble()
        if args.check:
            if not PACKET.exists() or PACKET.read_bytes() != payload:
                print("packet.d4.yml differs from deterministic assembly",
                      file=sys.stderr)
                return 1
            print("packet.d4.yml: byte-identical deterministic assembly")
        else:
            PACKET.parent.mkdir(parents=True, exist_ok=True)
            PACKET.write_bytes(payload)
            print(f"Wrote {PACKET.relative_to(ROOT)} ({len(payload)} bytes)")
    except (ValueError, OSError) as exc:
        print(f"assembly error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
