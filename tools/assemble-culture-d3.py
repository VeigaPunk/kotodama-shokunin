#!/usr/bin/env python3
"""Assemble the D3 NON-CANON culture packet and its native-only legacy projection.

Run from any directory: python3 tools/assemble-culture-d3.py [--check | --selftest]

Merges exactly the four assigned component JSONs under
examples/culture-d3/components/ without overriding collisions, hashes each
source, and deterministically writes the only two outputs this tool owns:

    examples/culture-d3/packet.json       D3 evidence-coupling packet
    examples/culture-d3/packet.gates.yml  legacy gate projection

Boundary rules baked into the projection:
  - Only constructed native forms reach the gate-facing `name`/`garment`
    slots; the naming gate phonology-tests costumes[].garment directly, so
    English display labels never ride those fields. Labels stay in
    packet.json and in assembly.legacy_projection.trace (native form vs
    display label).
  - morphology.derivation_rules are exactly six explicit per-name concat
    replay rules over the declared E1 base forms (regex-escaped).
  - cross_culture_review stays {languages: [], unresolved:
    ['real-language sweep not performed']}: CROSS-HOLD with exit 1 is the
    expected legacy outcome, not clearance.
  - C03's declared prohibition violation is retained (R-01 note), never
    repaired into a lawful case.

--check compares bytes without writing: exit 0 equal / 1 drift / 2 error.
A missing or malformed component fails closed with exit 2 before any write.
--selftest drives this same CLI over a fixture component tree inside one
temporary directory, then runs the real committed naming and costume gates
read-only against the fixture projection; it touches no file outside that
directory. The yaml_lines serializer is loaded read-only from
tools/assemble-d2.py; no third-party dependency is added.
"""

import argparse
import hashlib
import json
import re
import runpy
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPONENTS = ROOT / "examples/culture-d3/components"
PACKET = ROOT / "examples/culture-d3/packet.json"
LEGACY = ROOT / "examples/culture-d3/packet.gates.yml"
SERIALIZER = ROOT / "tools/assemble-d2.py"
NAMING_GATE = ROOT / "tools/gates/naming-collision-gate.py"
COSTUME_GATE = ROOT / "tools/gates/costume-era-consistency-gate.py"

PROFILE = "kotodama-d3-evidence-coupling/1"
PACKET_NAME = "D3 source-bounded culture drill (NON-CANON)"
LEGACY_NAME = "D3 source-bounded culture drill (NON-CANON) — legacy gate projection"
UNRESOLVED_SWEEP = "real-language sweep not performed"

COMPONENT_KEYS = {
    "04-language.json": {
        "phonology": dict,
        "lexicon": list,
        "names": list,
        "sound_changes": list,
        "utterances": list,
    },
    "05-ritual.json": {
        "beliefs": list,
        "speech_rules": list,
        "symbols": list,
        "naming_rule": dict,
    },
    "06-material.json": {
        "eras": list,
        "materials": list,
        "objects": list,
        "costumes": list,
        "rank_rules": list,
    },
    "07-evidence.json": {
        "references": list,
        "bridges": list,
        "canon_status": str,
        "handoff_status": str,
        "scope_notes": list,
        "screening": dict,
    },
}

MINIMUM_COUNTS = {
    "eras": 2,
    "lexicon": 20,
    "names": 6,
    "beliefs": 2,
    "costumes": 4,
    "references": 5,
    "bridges": 5,
}

PROJECTION_LIMITS = [
    "gate-facing strings are constructed native forms only; English display "
    "labels are never projected into name/garment slots that the naming gate "
    "phonology-tests (costumes[].garment is read directly as a sound form)",
    "lexicon terms are the declared E1 ordinary forms; E0 citation forms ride "
    "in packet.json and this trace; the ritual citation layer stays E0",
    "morphology.derivation_rules are exactly six per-name concat replays over "
    "declared E1 base forms; no general morphology, affix or sound law is "
    "projected",
    "AV1 substitution, utterance register law, beliefs, symbols, objects, "
    "references, bridges, scope notes and screening have no legacy-gate "
    "consumer and stay in packet.json only",
    "cross_culture_review keeps languages empty and the unresolved "
    "real-language sweep note: CROSS-HOLD with exit 1 is the expected legacy "
    "outcome, not clearance",
    "C03's declared violation of the hall material prohibition is retained as "
    "a violation (expected R-01 note), never repaired into a lawful case",
    "all native spellings are constructed and unscreened; no real-language or "
    "community clearance is claimed anywhere in the projection",
    "the component's coda_subset is additionally projected as legacy "
    "phonology.coda (the original key rides through unchanged) so the naming "
    "gate enforces the declared coda inventory",
]


def fail(message):
    raise ValueError(message)


def digest_bytes(data):
    return hashlib.sha256(data).hexdigest()


def file_digest(path):
    if not path.is_file():
        fail(f"required file not found: {path.relative_to(ROOT)}")
    return digest_bytes(path.read_bytes())


def yaml_lines_serializer():
    """The D2 assembler's yaml_lines, loaded read-only; no dependency added."""
    if not SERIALIZER.is_file():
        fail(f"yaml serializer not found: {SERIALIZER.relative_to(ROOT)}")
    namespace = runpy.run_path(str(SERIALIZER))
    lines = namespace.get("yaml_lines")
    if not callable(lines):
        fail("tools/assemble-d2.py does not expose a callable yaml_lines")
    return lines


def load_components():
    """Read exactly the four assigned components; fail closed on any defect."""
    merged = {}
    owner = {}
    sources = {}
    for filename, key_types in COMPONENT_KEYS.items():
        path = COMPONENTS / filename
        if not path.is_file():
            fail(f"missing component: {path.relative_to(ROOT)}")
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            fail(f"{filename}: not valid UTF-8 ({exc})")
        try:
            doc = json.loads(text)
        except json.JSONDecodeError as exc:
            fail(f"{filename}: invalid JSON ({exc})")
        if not isinstance(doc, dict):
            fail(f"{filename}: root must be a JSON object")
        expected = set(key_types)
        actual = set(doc)
        if actual != expected:
            fail(f"{filename}: top-level keys must be exactly {sorted(expected)}; "
                 f"missing={sorted(expected - actual)} unexpected={sorted(actual - expected)}")
        for key, want in key_types.items():
            value = doc[key]
            if isinstance(value, bool) or not isinstance(value, want):
                fail(f"{filename}.{key}: expected {want.__name__}")
        sources[f"examples/culture-d3/components/{filename}"] = digest_bytes(raw)
        for key, value in doc.items():
            if key in merged:
                fail(f"component collision: {key!r} defined by both "
                     f"{owner[key]} and {filename}; refusing to override")
            merged[key] = value
            owner[key] = filename
    for key, minimum in sorted(MINIMUM_COUNTS.items()):
        records = merged.get(key)
        got = len(records) if isinstance(records, list) else "absent"
        if not isinstance(records, list) or len(records) < minimum:
            fail(f"{key}: {got} records, below the declared minimum of {minimum}")
    return merged, sources


def e1_forms(lexicon):
    """lexeme id -> declared E1 form; strict because the projection needs it."""
    forms = {}
    for record in lexicon:
        lid = record.get("id") if isinstance(record, dict) else None
        declared = record.get("forms") if isinstance(record, dict) else None
        if (not isinstance(lid, str) or not lid
                or not isinstance(declared, dict)
                or not isinstance(declared.get("E1"), str) or not declared["E1"]):
            fail(f"lexicon: record {lid!r} lacks a string forms.E1 needed for projection")
        forms[lid] = declared["E1"]
    return forms


def era_sort_key(entry):
    ordinal = entry.get("ordinal") if isinstance(entry, dict) else None
    ident = entry.get("id") if isinstance(entry, dict) else None
    return (0, ordinal, str(ident) if ident is not None else "") \
        if isinstance(ordinal, (int, float)) and not isinstance(ordinal, bool) \
        else (1, 0, str(ident))


def record_field(record, key, what):
    value = record.get(key) if isinstance(record, dict) else None
    if not isinstance(value, str) or not value.strip():
        fail(f"{what}: missing non-empty string {key!r} needed for projection")
    return value


def compact(mapping):
    return {k: v for k, v in mapping.items() if v is not None}


def build_legacy(packet):
    """Native-only legacy projection plus the native-vs-display trace."""
    lines = yaml_lines_serializer()
    e1 = e1_forms(packet["lexicon"])

    gate_name_of = {}
    for material in packet["materials"]:
        mid = material.get("id") if isinstance(material, dict) else None
        gate_name_of[mid] = record_field(material, "gate_name",
                                         f"materials[{mid!r}]")

    rules = []
    projected_names = []
    trace_names = {}
    for name in packet["names"]:
        nid = record_field(name, "id", "names record")
        native = record_field(name, "native_form", f"names[{nid}]")
        formation = name.get("formation")
        bases = formation.get("bases") if isinstance(formation, dict) else None
        if (not isinstance(bases, list) or len(bases) != 2
                or not all(isinstance(b, str) and b for b in bases)):
            fail(f"names[{nid}]: formation.bases must be a pair of lexeme ids")
        missing = [b for b in bases if b not in e1]
        if missing:
            fail(f"names[{nid}]: base(s) {missing} have no declared E1 form")
        b1, b2 = bases
        stem = f"{e1[b1]}+{e1[b2]}"
        rule_id = f"D3-{nid}-CONCAT"
        rules.append({
            "id": rule_id,
            "kind": "concat",
            "gloss": f"explicit concat replay for {nid}: {b1}+{b2} E1 forms",
            "pattern": "^(?P<B1>{}){}(?P<B2>{})$".format(
                re.escape(e1[b1]), re.escape("+"), re.escape(e1[b2])),
            "output": "{B1}{B2}",
            "source": f"{nid}.formation.bases [{b1}, {b2}]; "
                      "E1 forms after the declared sound change",
        })
        projected_names.append(compact({
            "id": nid,
            "name": native,
            "type": name.get("type"),
            "era": name.get("era"),
            "formation": {
                "stem": stem,
                "rule": rule_id,
                "bases": list(bases),
                "operation": formation.get("operation", "concat"),
                "expected": native,
            },
        }))
        trace_names[nid] = compact({
            "name_projected": native,
            "display_label": name.get("display_label"),
            "bases": list(bases),
        })

    projected_lexicon = []
    trace_lexicon = {}
    for lexeme in packet["lexicon"]:
        lid = record_field(lexeme, "id", "lexicon record")
        declared = lexeme.get("forms") if isinstance(lexeme, dict) else {}
        declared = declared if isinstance(declared, dict) else {}
        projected_lexicon.append(compact({
            "id": lid,
            "term": e1[lid],
            "gloss": lexeme.get("gloss"),
            "status": lexeme.get("status"),
            "available_from": lexeme.get("available_from"),
            "era_forms": {era: declared[era]
                          for era in ("E0", "E1") if isinstance(declared.get(era), str)},
        }))
        trace_lexicon[lid] = compact({
            "e0_form": declared.get("E0"),
            "e1_form": e1[lid],
            "term_projected": e1[lid],
        })

    projected_costumes = []
    trace_costumes = {}
    for costume in packet["costumes"]:
        cid = record_field(costume, "id", "costumes record")
        native = record_field(costume, "native_form", f"costumes[{cid}]")
        material_id = record_field(costume, "material_id", f"costumes[{cid}]")
        if material_id not in gate_name_of:
            fail(f"costumes[{cid}]: material_id {material_id!r} has no declared material")
        projected_costumes.append(compact({
            "id": cid,
            "garment": native,
            "material": gate_name_of[material_id],
            "wearer_rank": costume.get("wearer_rank"),
            "rite": costume.get("rite"),
            "era": costume.get("era"),
            "place": costume.get("place"),
            "claimed_status": costume.get("claimed_status"),
            "provenance": costume.get("provenance"),
        }))
        trace_costumes[cid] = compact({
            "garment_projected": native,
            "display_label": costume.get("display_label"),
            "lexeme_id": costume.get("lexeme_id"),
            "material": gate_name_of[material_id],
        })

    projected_materials = []
    for material in packet["materials"]:
        mid = record_field(material, "id", "materials record")
        projected_materials.append(compact({
            "name": gate_name_of[mid],
            "composition": material.get("composition"),
            "available_from": material.get("available_from"),
            "provenance": material.get("provenance"),
            "routes": material.get("routes"),
        }))

    eras = [entry.get("id") for entry in sorted(packet["eras"], key=era_sort_key)]
    if not all(isinstance(e, str) and e for e in eras):
        fail("eras: every entry needs a string id for the legacy projection")

    trace = {"lexicon": trace_lexicon, "names": trace_names, "costumes": trace_costumes}
    # the naming gate enforces codas only through phonology.coda; the declared
    # component key is coda_subset, so project it under the legacy key too and
    # keep the original key unchanged for traceability.
    projected_phonology = dict(packet["phonology"])
    if not isinstance(projected_phonology.get("coda"), list) \
            and isinstance(projected_phonology.get("coda_subset"), list):
        projected_phonology["coda"] = list(projected_phonology["coda_subset"])
    projected = {
        "name": LEGACY_NAME,
        "canon": "not canonized (D3 NON-CANON drill)",
        "phonology": projected_phonology,
        "morphology": {
            "type": "concat-only naming derivations for a bounded NON-CANON drill; "
                    "no general morphology is claimed",
            "derivation_rules": rules,
        },
        "lexicon": projected_lexicon,
        "names": projected_names,
        "eras": eras,
        "costumes": projected_costumes,
        "materials": projected_materials,
        "rank_rules": packet["rank_rules"],
        "cross_culture_review": {"languages": [], "unresolved": [UNRESOLVED_SWEEP]},
        "assembly": {
            "generator": "tools/assemble-culture-d3.py",
            "source_sha256": {},  # filled by assemble() after trace is built
            "rule": "native constructed forms only in gate-facing slots; English "
                    "display labels are never projected as native strings",
            "limits": PROJECTION_LIMITS,
            "trace": trace,
        },
    }
    legacy_bytes = ("\n".join(lines(projected)) + "\n").encode("utf-8")
    return legacy_bytes, trace


def assemble():
    packet_core, sources = load_components()
    legacy_bytes, trace = build_legacy(packet_core)
    packet = {"profile": PROFILE, "name": PACKET_NAME}
    packet.update(packet_core)
    packet["assembly"] = {
        "generator": "tools/assemble-culture-d3.py",
        "serializer": "tools/assemble-d2.py (yaml_lines loaded read-only)",
        "serializer_sha256": file_digest(SERIALIZER),
        "source_sha256": dict(sorted(sources.items())),
        "legacy_projection": {
            "output": "examples/culture-d3/packet.gates.yml",
            "rule": "native constructed forms only in gate-facing slots; English "
                    "display labels are carried here and in packet records, "
                    "never projected as native strings",
            "trace": trace,
            "limits": PROJECTION_LIMITS,
        },
    }
    packet_bytes = (json.dumps(packet, ensure_ascii=False, sort_keys=True,
                               indent=2) + "\n").encode("utf-8")
    return packet_bytes, legacy_bytes


# --------------------------------------------------------------------------
# selftest fixtures
# --------------------------------------------------------------------------

def _fixture_components():
    """Contract-shaped fixture tree; anchored E0 lexemes, deterministic."""
    e0 = {"L01": "pina", "L02": "suma", "L03": "talu", "L04": "kalu", "L05": "mita",
          "L06": "nupi", "L07": "tola", "L08": "kimi", "L09": "lanu", "L10": "tapu",
          "L11": "mura", "L12": "pila", "L13": "kanti", "L14": "lomi", "L15": "peta",
          "L16": "ruti", "L17": "nara", "L18": "salu", "L19": "mila", "L20": "kuru"}
    e1 = {k: ("f" + v[1:] if v.startswith("p") else v) for k, v in e0.items()}

    lexicon = [{"id": lid, "native_form": e0[lid], "gloss": f"constructed gloss {lid}",
                "status": "constructed", "available_from": "E0",
                "forms": {"E0": e0[lid], "E1": e1[lid]}} for lid in sorted(e0)]
    names = []
    for i, (b1, b2) in enumerate([("L01", "L03"), ("L02", "L17"), ("L03", "L18"),
                                  ("L17", "L19"), ("L18", "L20"), ("L19", "L20")], 1):
        nid = f"N{i:02d}"
        expected = e1[b1] + e1[b2]
        names.append({"id": nid, "native_form": expected,
                      "display_label": f"constructed person name {i} (translated label)",
                      "type": "person", "era": "E1",
                      "formation": {"bases": [b1, b2], "operation": "concat",
                                    "expected": expected}})
    comp04 = {
        "phonology": {"consonants": ["p", "f", "t", "k", "m", "n", "s", "r", "l"],
                      "vowels": ["a", "e", "i", "o", "u"],
                      "phonotactics": "(C)V(C)", "coda_subset": ["n", "l", "r", "s"],
                      "onset_clusters": False},
        "lexicon": lexicon,
        "names": names,
        "sound_changes": [{"id": "SC1", "from": "p", "to": "f", "environment": "initial",
                           "from_era": "E0", "to_era": "E1", "register": "ordinary"}],
        "utterances": [
            {"id": "U01", "lexeme_id": "L01", "era": "E1", "register": "ordinary",
             "place": "market", "spoken_form": e1["L01"], "written_form": e0["L01"]},
            {"id": "U02", "lexeme_id": "L01", "era": "E1", "register": "ritual",
             "place": "hall", "spoken_form": e0["L01"], "written_form": e0["L01"]},
            {"id": "U03", "lexeme_id": "L03", "era": "E1", "register": "ordinary",
             "place": "market", "spoken_form": e1["L03"], "written_form": e0["L03"]},
            {"id": "U04", "lexeme_id": "L03", "era": "E1", "register": "ritual",
             "place": "hall", "spoken_form": e0["L03"], "written_form": e0["L03"]},
        ],
    }
    comp05 = {
        "beliefs": [
            {"id": "B01", "speaker": "hall record-keeper Ael (fictional)", "era": "E1",
             "claim_kind": "attributed-belief", "truth_status": "unresolved",
             "proposition": "the hall record keeps a voice of its own when read aloud"},
            {"id": "B02", "speaker": "market scribe Ruka (fictional)", "era": "E1",
             "claim_kind": "attributed-belief", "truth_status": "unresolved",
             "proposition": "the record is silent cloth; only its readers speak"},
        ],
        "speech_rules": [{"id": "AV1", "lexeme_id": "L01", "era": "E1",
                          "register": "ritual", "place": "hall",
                          "substitute_lexeme_id": "L02",
                          "claim_kind": "constructed-rule"}],
        "symbols": [
            {"id": "SY01", "display_label": "knotted cord badge (translated label)",
             "era": "E1", "audience": "appointed hall officers",
             "reading": "record authority inside the hall",
             "claim_kind": "constructed-rule"},
            {"id": "SY02", "display_label": "split weave sign (translated label)",
             "era": "E1", "audience": "market workers",
             "reading": "market membership", "claim_kind": "constructed-rule"},
        ],
        "naming_rule": {"id": "NR1", "allowed_offsets": [2, 8, 20],
                        "unit": "fictional-nights", "chosen_offset": 8,
                        "status": "constructed-not-historical", "source_id": "S03"},
    }
    comp06 = {
        "eras": [{"id": "E0", "ordinal": 0, "display_label": "settlement era"},
                 {"id": "E1", "ordinal": 1, "display_label": "assembly era"}],
        "materials": [
            {"id": "M01", "gate_name": "felt", "composition": "fulled local wool",
             "available_from": "E0", "provenance": "local-production",
             "routes": [{"kind": "local", "stage": "cloth", "eras": ["E0", "E1"]}]},
            {"id": "M02", "gate_name": "plant-cloth",
             "composition": "woven plant-fibre cloth", "available_from": "E1",
             "provenance": "import",
             "routes": [{"kind": "import", "stage": "cloth", "eras": ["E1"]}]},
            {"id": "M03", "gate_name": "horn", "composition": "carved local horn",
             "available_from": "E0", "provenance": "local-production",
             "routes": [{"kind": "local", "stage": "trim", "eras": ["E0", "E1"]}]},
        ],
        "objects": [
            {"id": "O01", "material_id": "M01", "object_kind": "ground-surface",
             "worn": False, "display_label": "ground spread (translated label)"},
            {"id": "O02", "material_id": "M01", "object_kind": "garment", "worn": True,
             "display_label": "work smock (translated label)"},
            {"id": "O03", "material_id": "M02", "object_kind": "garment", "worn": True,
             "display_label": "visitor assembly robe (translated label)"},
            {"id": "O04", "material_id": "M03", "object_kind": "worn-attachment",
             "worn": True, "display_label": "horn clasp (translated label)"},
        ],
        "costumes": [
            {"id": "C01", "object_id": "O02", "lexeme_id": "L17",
             "native_form": e0["L17"], "display_label": "work smock (translated label)",
             "material_id": "M01", "era": "E0", "wearer_rank": "worker",
             "rite": "none", "place": "market", "claimed_status": "lawful",
             "provenance": "local-production"},
            {"id": "C02", "object_id": "O02", "lexeme_id": "L18",
             "native_form": e1["L18"],
             "display_label": "work smock, later cut (translated label)",
             "material_id": "M01", "era": "E1", "wearer_rank": "worker",
             "rite": "none", "place": "market", "claimed_status": "lawful",
             "provenance": "local-production"},
            {"id": "C03", "object_id": "O03", "lexeme_id": "L19",
             "native_form": e1["L19"],
             "display_label": "visitor assembly robe (translated label)",
             "material_id": "M02", "era": "E1", "wearer_rank": "visitor",
             "rite": "assembly", "place": "hall", "claimed_status": "violation",
             "provenance": "import"},
            {"id": "C04", "object_id": "O04", "lexeme_id": "L20",
             "native_form": e1["L20"], "display_label": "horn clasp (translated label)",
             "material_id": "M03", "era": "E1", "wearer_rank": "appointed",
             "rite": "assembly", "place": "hall", "claimed_status": "lawful",
             "provenance": "local-production"},
        ],
        "rank_rules": [{"id": "RR1", "authority": "Hall Wardens (fictional)",
                        "jurisdiction": "hall", "eras": ["E1"], "rites": ["assembly"],
                        "effect": "prohibit",
                        "property": {"kind": "material", "value": "plant-cloth"},
                        "wearer_ranks": ["visitor"], "exempt_ranks": []}],
    }
    bindings = {"S01": ("corpus/lessons/round-6-sources/05.json", "R6-05-A",
                        "partial-support"),
                "S02": ("corpus/lessons/round-6-sources/03.json", "R6-03-B",
                        "scoped-support"),
                "S03": ("corpus/lessons/round-6-sources/13.json", "R6-13-A",
                        "scoped-support"),
                "S04": ("corpus/lessons/round-6-sources/13.json", "R6-13-B",
                        "scoped-support"),
                "S05": ("corpus/lessons/round-6-sources/09.json", "R6-09-A",
                        "partial-support")}
    references = [{"id": sid, "ledger_path": path, "audit_id": audit,
                   "file_sha256": f"{i:064x}",
                   "source_url": f"https://example.invalid/{sid.lower()}",
                   "source_kind": "secondary-scholarly", "support_scope": scope,
                   "limits": "fixture binding; scope rides the round-6 reconciliation"}
                  for i, (sid, (path, audit, scope))
                  in enumerate(sorted(bindings.items()))]
    bridges = [{"id": bid, "source_id": sid, "relation": "method-transfer",
                "target_ids": targets, "asserted_scope": "design-only",
                "claim_kind": "constructed-rule", "mechanism": mechanism,
                "limits": "design-only analogy; no historical reconstruction claimed"}
               for bid, sid, targets, mechanism in [
                   ("BR01", "S01", ["U01", "U02"], "written form vs read form"),
                   ("BR02", "S02", ["C01", "C02"],
                    "object evidence is not an exclusive era marker"),
                   ("BR03", "S03", ["NR1"],
                    "discrete fictional timing, not historical numbers"),
                   ("BR04", "S04", ["O01", "O04"],
                    "surface vs worn attachment, not a copied rite"),
                   ("BR05", "S05", ["SY01", "B01"],
                    "institution-specific record, not universal speech")]]
    comp07 = {"references": references, "bridges": bridges,
              "canon_status": "NON-CANON", "handoff_status": "prepared-not-accepted",
              "scope_notes": [
                  "all genealogy is invented; no real-language derivation is claimed",
                  "no cultural permission is claimed or granted for any form",
                  "no lore receipt exists; handoff stays prepared-not-accepted",
                  "historical and corpus residuals from earlier rounds remain "
                  "unresolved"],
              "screening": {"status": "unresolved",
                            "real_language_sweep_performed": False,
                            "limits": "no real-language or community sweep "
                                      "performed; spellings unscreened"}}
    return {filename: json.dumps(doc, ensure_ascii=False, indent=2) + "\n"
            for filename, doc in (("04-language.json", comp04),
                                  ("05-ritual.json", comp05),
                                  ("06-material.json", comp06),
                                  ("07-evidence.json", comp07))}


def selftest():
    """Fixture-driven controls over the real CLI plus the real legacy gates."""
    source = Path(__file__).resolve()
    failures = []
    passed = 0

    def check(label, condition, detail=""):
        nonlocal passed
        if condition:
            passed += 1
        else:
            failures.append(f"{label}: {detail or 'failed'}")

    def finding_ids(text):
        return {m.group(1) for m in re.finditer(r"^FINDING (\S+):", text, re.M)}

    with tempfile.TemporaryDirectory(prefix="assemble-culture-d3-selftest-") as tmpdir:
        tmp = Path(tmpdir)
        script = tmp / "tools" / "assemble-culture-d3.py"
        script.parent.mkdir(parents=True)
        shutil.copyfile(source, script)
        shutil.copyfile(SERIALIZER, tmp / "tools" / "assemble-d2.py")
        components = tmp / "examples" / "culture-d3" / "components"
        components.mkdir(parents=True)
        packet_out = tmp / "examples" / "culture-d3" / "packet.json"
        legacy_out = tmp / "examples" / "culture-d3" / "packet.gates.yml"

        def write_fixtures(files):
            for name, text in files.items():
                (components / name).write_text(text, encoding="utf-8")

        def run(*args):
            return subprocess.run([sys.executable, str(script), *args],
                                  capture_output=True, text=True,
                                  cwd=str(tmp), check=False)

        def run_gate(gate, packet_path):
            return subprocess.run([sys.executable, str(gate), str(packet_path)],
                                  capture_output=True, text=True, check=False)

        def clear_outputs():
            for out in (packet_out, legacy_out):
                if out.exists():
                    out.unlink()

        good = _fixture_components()
        write_fixtures(good)

        # positive control: the real CLI assembles the fixture tree, twice.
        first = run()
        check("positive: CLI exit 0", first.returncode == 0,
              f"exit {first.returncode}: {first.stderr.strip()}")
        check("positive: both outputs written",
              packet_out.exists() and legacy_out.exists(), first.stdout.strip())
        packet_bytes = packet_out.read_bytes() if packet_out.exists() else b""
        legacy_bytes = legacy_out.read_bytes() if legacy_out.exists() else b""
        second = run()
        check("positive: second CLI run exit 0", second.returncode == 0,
              second.stderr.strip())
        check("positive: deterministic packet bytes",
              packet_out.exists() and packet_out.read_bytes() == packet_bytes)
        check("positive: deterministic legacy bytes",
              legacy_out.exists() and legacy_out.read_bytes() == legacy_bytes)

        clean = run("--check")
        check("--check: exit 0 on clean outputs", clean.returncode == 0,
              f"exit {clean.returncode}: {clean.stderr.strip()}")
        check("--check: byte-identical report", "byte-identical" in clean.stdout,
              clean.stdout.strip())

        # packet.json structural controls
        try:
            packet_doc = json.loads(packet_bytes.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            packet_doc = {}
            check("packet: valid UTF-8 JSON", False, str(exc))
        wanted_core = ({key for types in COMPONENT_KEYS.values() for key in types}
                       | {"profile", "name", "assembly"})
        check("packet: profile", packet_doc.get("profile") == PROFILE,
              packet_doc.get("profile"))
        check("packet: name", packet_doc.get("name") == PACKET_NAME,
              packet_doc.get("name"))
        check("packet: merged top-level keys", set(packet_doc) == wanted_core,
              sorted(set(packet_doc) ^ wanted_core))
        check("packet: canon/status ride through",
              packet_doc.get("canon_status") == "NON-CANON"
              and packet_doc.get("handoff_status") == "prepared-not-accepted",
              (packet_doc.get("canon_status"), packet_doc.get("handoff_status")))
        canonical = (json.dumps(packet_doc, ensure_ascii=False, sort_keys=True,
                                indent=2) + "\n").encode("utf-8")
        check("packet: sorted-key indent-2 final-newline bytes",
              packet_bytes == canonical, "bytes differ from canonical dump")
        sources = packet_doc.get("assembly", {}).get("source_sha256", {})
        check("assembly: every source digest recorded",
              sorted(sources) == sorted(f"examples/culture-d3/components/{name}"
                                        for name in good), sorted(sources))
        check("assembly: digests match the fixture files",
              all(sources.get(rel) == digest_bytes((components / Path(rel).name)
                                                   .read_bytes())
                  for rel in sources))
        check("assembly: no absolute path or timestamp",
              str(tmp) not in packet_bytes.decode("utf-8", "replace")
              and str(tmp) not in legacy_bytes.decode("utf-8", "replace"))
        trace = (packet_doc.get("assembly", {}).get("legacy_projection", {})
                 .get("trace", {}))
        check("assembly: trace covers names/costumes/lexicon",
              sorted(trace.get("names", {})) == [f"N{i:02d}" for i in range(1, 7)]
              and sorted(trace.get("costumes", {})) == ["C01", "C02", "C03", "C04"]
              and len(trace.get("lexicon", {})) == 20, sorted(trace))
        check("assembly: limits nonempty",
              bool(packet_doc.get("assembly", {}).get("legacy_projection", {})
                   .get("limits")))

        # legacy projection structural controls via the costume gate's reader
        reader_ns = runpy.run_path(str(COSTUME_GATE))
        parse_packet = reader_ns["parse_packet"]
        try:
            legacy_doc = parse_packet(legacy_bytes.decode("utf-8"))
            parse_ok = True
            parse_detail = ""
        except reader_ns["Malformed"] as exc:
            legacy_doc = {}
            parse_ok = False
            parse_detail = str(exc)
        check("legacy: parses under the costume gate reader", parse_ok, parse_detail)
        check("legacy: no English display label in garment slots",
              all(rec.get("garment") not in ("work smock (translated label)",
                                             "visitor assembly robe (translated label)")
                  and rec.get("garment") != rec.get("display_label")
                  for rec in legacy_doc.get("costumes", [])),
              [rec.get("garment") for rec in legacy_doc.get("costumes", [])])
        check("legacy: garments are the native E-era forms",
              [rec.get("garment") for rec in legacy_doc.get("costumes", [])]
              == ["nara", "salu", "mila", "kuru"],
              [rec.get("garment") for rec in legacy_doc.get("costumes", [])])
        check("legacy: names are native forms",
              [rec.get("name") for rec in legacy_doc.get("names", [])]
              == ["finatalu", "sumanara", "talusalu", "naramila", "salukuru",
                  "milakuru"],
              [rec.get("name") for rec in legacy_doc.get("names", [])])
        check("legacy: eras are strings", legacy_doc.get("eras") == ["E0", "E1"],
              legacy_doc.get("eras"))
        check("legacy: coda_subset projected as phonology.coda",
              legacy_doc.get("phonology", {}).get("coda") == ["n", "l", "r", "s"]
              and legacy_doc.get("phonology", {}).get("coda_subset")
              == ["n", "l", "r", "s"],
              legacy_doc.get("phonology"))
        rules = {rule.get("id"): rule
                 for rule in legacy_doc.get("morphology", {}).get("derivation_rules", [])}
        check("legacy: exactly six concat rules", len(rules) == 6, sorted(rules))
        for rec in legacy_doc.get("names", []):
            formation = rec.get("formation", {})
            rule = rules.get(formation.get("rule"), {})
            match = re.fullmatch(rule.get("pattern", ""), formation.get("stem", "")) \
                if rule.get("pattern") else None
            replayed = match and rule["output"].format(**match.groupdict())
            check(f"legacy: replay {rec.get('id')}",
                  bool(match) and replayed == rec.get("name"),
                  f"{replayed!r} != {rec.get('name')!r}")
        check("legacy: lexicon terms are E1 forms",
              all(rec.get("term") and rec.get("era_forms", {}).get("E0")
                  for rec in legacy_doc.get("lexicon", []))
              and len(legacy_doc.get("lexicon", [])) == 20,
              len(legacy_doc.get("lexicon", [])))
        check("legacy: cross_culture_review unresolved",
              legacy_doc.get("cross_culture_review")
              == {"languages": [], "unresolved": [UNRESOLVED_SWEEP]},
              legacy_doc.get("cross_culture_review"))
        check("legacy: RR1 prohibition retained",
              legacy_doc.get("rank_rules")
              and legacy_doc["rank_rules"][0].get("effect") == "prohibit"
              and legacy_doc["rank_rules"][0].get("property", {}).get("value")
              == "plant-cloth",
              legacy_doc.get("rank_rules"))
        check("legacy: C03 stays a declared violation",
              any(rec.get("id") == "C03" and rec.get("claimed_status") == "violation"
                  for rec in legacy_doc.get("costumes", [])),
              [rec.get("claimed_status") for rec in legacy_doc.get("costumes", [])])

        # the real committed gates, run read-only against the fixture projection
        naming = run_gate(NAMING_GATE, legacy_out)
        naming_ids = finding_ids(naming.stdout)
        check("naming gate: exit 1", naming.returncode == 1,
              f"exit {naming.returncode}: {naming.stderr.strip()}")
        check("naming gate: CROSS-HOLD kept", "CROSS-HOLD" in naming_ids,
              sorted(naming_ids))
        check("naming gate: no native phonotactic or derivation FAIL",
              not any(i.startswith(("PHON-", "DERIV-")) for i in naming_ids)
              and ": FAIL" not in naming.stdout,
              sorted(naming_ids))
        costume = run_gate(COSTUME_GATE, legacy_out)
        costume_ids = finding_ids(costume.stdout)
        check("costume gate: exit 1", costume.returncode == 1,
              f"exit {costume.returncode}: {costume.stderr.strip()}")
        check("costume gate: R-01 note retained", "R-01" in costume_ids,
              sorted(costume_ids))
        check("costume gate: no false lawful claim (no R-02)",
              "R-02" not in costume_ids, sorted(costume_ids))

        # tamper control: one changed source byte must fail --check with exit 1.
        tampered = dict(good)
        tampered["04-language.json"] = good["04-language.json"].replace(
            '"vowels": [\n        "a",\n        "e",\n        "i",\n        "o",\n        "u"\n      ]',
            '"vowels": [\n        "a",\n        "e",\n        "i",\n        "o"\n      ]')
        if tampered["04-language.json"] == good["04-language.json"]:
            tampered["04-language.json"] = good["04-language.json"].replace(
                '"peta"', '"petra"')
        check("tamper: fixture mutation applied",
              tampered["04-language.json"] != good["04-language.json"])
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

        # drift on a missing output file
        legacy_out.unlink()
        missing_out = run("--check")
        check("missing output: --check exit 1", missing_out.returncode == 1,
              f"exit {missing_out.returncode}: {missing_out.stderr.strip()}")
        regenerated = run()
        check("missing output: regenerated by default run",
              regenerated.returncode == 0 and legacy_out.exists(),
              regenerated.stderr.strip())

        # fail-closed negative controls, each through the real CLI
        lexicon_cut = json.loads(good["04-language.json"])
        lexicon_cut["lexicon"] = lexicon_cut["lexicon"][:5]
        wrong_type = json.loads(good["04-language.json"])
        wrong_type["lexicon"] = {}
        missing_key = json.loads(good["05-ritual.json"])
        missing_key.pop("symbols")
        extra_key = json.loads(good["04-language.json"])
        extra_key["unexpected"] = 1
        negatives = [
            ("missing component", None, "missing component"),
            ("invalid JSON", {"06-material.json": '{"eras": ['}, "invalid JSON"),
            ("invalid UTF-8", None, "not valid UTF-8"),
            ("root not an object", {"04-language.json": "[]"}, "root must be a JSON object"),
            ("unexpected top-level key", {"04-language.json": json.dumps(extra_key)},
             "unexpected"),
            ("missing assigned key", {"05-ritual.json": json.dumps(missing_key)},
             "missing"),
            ("wrong value type", {"04-language.json": json.dumps(wrong_type)},
             "expected list"),
            ("below minimum count", {"04-language.json": json.dumps(lexicon_cut)},
             "below the declared minimum"),
        ]
        for label, files, fragment in negatives:
            write_fixtures(good)
            clear_outputs()
            if label == "missing component":
                (components / "05-ritual.json").unlink()
            elif label == "invalid UTF-8":
                (components / "07-evidence.json").write_bytes(b"\xff\xfe{}")
            else:
                write_fixtures(files)
            result = run()
            check(f"negative {label}: exit 2", result.returncode == 2,
                  f"exit {result.returncode}: {result.stderr.strip()}")
            check(f"negative {label}: message names the defect",
                  fragment in result.stderr, result.stderr.strip())
            check(f"negative {label}: no traceback",
                  "Traceback" not in result.stderr, result.stderr.strip())
            check(f"negative {label}: fail closed, no outputs written",
                  not packet_out.exists() and not legacy_out.exists())

        # cross-component collision: the contract's key sets are disjoint, so
        # this merge branch is only reachable if the contract itself overlaps;
        # patch the copied script's key map to make 05 also claim phonology.
        write_fixtures(good)
        clear_outputs()
        collision = json.loads(good["05-ritual.json"])
        collision["phonology"] = {}
        write_fixtures({"05-ritual.json": json.dumps(collision)})
        script_text = script.read_text(encoding="utf-8")
        patched = script_text.replace(
            '    "05-ritual.json": {\n        "beliefs": list,',
            '    "05-ritual.json": {\n        "phonology": dict,\n'
            '        "beliefs": list,')
        check("collision: script patch applied", patched != script_text)
        script.write_text(patched, encoding="utf-8")
        result = run()
        check("negative cross-component collision: exit 2", result.returncode == 2,
              f"exit {result.returncode}: {result.stderr.strip()}")
        check("negative cross-component collision: message names the collision",
              "component collision" in result.stderr, result.stderr.strip())
        check("negative cross-component collision: no traceback",
              "Traceback" not in result.stderr, result.stderr.strip())
        check("negative cross-component collision: fail closed",
              not packet_out.exists() and not legacy_out.exists())
        script.write_text(script_text, encoding="utf-8")

        # serializer missing -> fail closed too
        write_fixtures(good)
        clear_outputs()
        (tmp / "tools" / "assemble-d2.py").unlink()
        no_serializer = run()
        check("negative serializer missing: exit 2", no_serializer.returncode == 2,
              f"exit {no_serializer.returncode}: {no_serializer.stderr.strip()}")
        check("negative serializer missing: fail closed",
              not packet_out.exists() and not legacy_out.exists())

    if failures:
        for failure in failures:
            print(f"selftest FAIL: {failure}", file=sys.stderr)
        print(f"selftest: {passed}/{passed + len(failures)} checks passed",
              file=sys.stderr)
        return 1
    print(f"selftest: {passed}/{passed} checks passed — fixture CLI assemble/--check/"
          "determinism/tamper plus missing, invalid-JSON, invalid-UTF8, wrong-root, "
          "unexpected-key, missing-key, collision, wrong-type, below-minimum and "
          "serializer-absent fail-closed controls; real naming gate (CROSS-HOLD, "
          "no PHON/DERIV FAIL) and real costume gate (R-01 note, no R-02) run "
          "read-only; no file outside the temporary directory touched")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true",
                       help="compare both outputs against the assembly without writing")
    group.add_argument("--selftest", "--self-test", action="store_true", dest="selftest",
                       help="run the fixture controls in a temporary directory")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    try:
        packet_bytes, legacy_bytes = assemble()
        if args.check:
            drifted = []
            for output, payload in ((PACKET, packet_bytes), (LEGACY, legacy_bytes)):
                if not output.exists() or output.read_bytes() != payload:
                    drifted.append(str(output.relative_to(ROOT)))
            if drifted:
                for rel in drifted:
                    print(f"{rel} differs from deterministic assembly", file=sys.stderr)
                return 1
            print("packet.json: byte-identical deterministic assembly; "
                  "packet.gates.yml: byte-identical deterministic assembly")
        else:
            PACKET.parent.mkdir(parents=True, exist_ok=True)
            PACKET.write_bytes(packet_bytes)
            print(f"Wrote {PACKET.relative_to(ROOT)} ({len(packet_bytes)} bytes)")
            LEGACY.write_bytes(legacy_bytes)
            print(f"Wrote {LEGACY.relative_to(ROOT)} ({len(legacy_bytes)} bytes)")
    except (ValueError, OSError) as exc:
        print(f"assembly error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
