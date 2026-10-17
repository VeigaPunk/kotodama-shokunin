#!/usr/bin/env python3
"""Assemble D2's gate-facing records, without reconciling design disagreements.

Run from any directory: python3 tools/assemble-d2.py [--check].
Uses the existing costume gate's stdlib YAML-subset reader on selected blocks;
this is not a general YAML loader. --check compares bytes without writing.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import runpy
import sys

ROOT = Path(__file__).resolve().parent.parent
COMPONENTS = ROOT / "examples/culture-d2/components"
OUTPUT = ROOT / "examples/culture-d2/packet.d2.yml"
READER = ROOT / "tools/gates/costume-era-consistency-gate.py"
TOP_KEY = re.compile(r"^([A-Za-z_][\w-]*):")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract(path, key, parse):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    starts = [(i, match.group(1)) for i, line in enumerate(lines)
              if (match := TOP_KEY.match(line))]
    matches = [j for j, (_, name) in enumerate(starts) if name == key]
    if len(matches) != 1:
        raise ValueError(f"{path.name}: expected exactly one top-level {key!r}")
    index = matches[0]
    start = starts[index][0]
    end = starts[index + 1][0] if index + 1 < len(starts) else len(lines)
    block = parse("".join(lines[start:end]))
    value = block[key]
    if not isinstance(value, (dict, list)) or not value:
        raise ValueError(f"{path.name}: {key!r} has no usable records")
    return value


def scalar(value):
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    return json.dumps(value, ensure_ascii=False, allow_nan=False)


def yaml_lines(value, indent=0):
    prefix = " " * indent
    if isinstance(value, dict):
        for key, child in value.items():
            key = key if re.fullmatch(r"[A-Za-z_][\w-]*", key) else scalar(key)
            if isinstance(child, (list, dict)) and child:
                yield f"{prefix}{key}:"
                yield from yaml_lines(child, indent + 2)
            else:
                yield f"{prefix}{key}: {scalar(child)}"
    elif isinstance(value, list):
        for child in value:
            if isinstance(child, (list, dict)) and child:
                yield prefix + "-"
                yield from yaml_lines(child, indent + 2)
            else:
                yield f"{prefix}- {scalar(child)}"
    else:
        raise ValueError("root must be a mapping or sequence")


def assemble():
    parse = runpy.run_path(str(READER))["parse_packet"]
    sources = {}

    def take(stem, key, expected_type):
        path = COMPONENTS / f"{stem}.yml"
        value = extract(path, key, parse)
        if not isinstance(value, expected_type):
            raise ValueError(f"{stem}.{key}: expected {expected_type.__name__}")
        sources[str(path.relative_to(ROOT))] = digest(path)
        return value

    phonology = take("02-phonology", "phonology", dict)
    phonology["coda"] = ["n", "l", "r", "s"]
    phonology["onset_clusters"] = False
    packet = {
        "name": "D2 highland pastoralists — round-3 design drill",
        "canon": "not canonized (D2 design drill)",
        "phonology": phonology,
        "morphology": take("03-morphosyntax", "morphology", dict),
        "lexicon": take("05-lexicon", "lexicon", list),
        "pantheon": take("06-pantheon", "pantheon", list),
        "symbols": take("08-symbols", "symbols", list),
        "costumes": take("11-costumes", "costumes", list),
        "names": take("13-naming", "names", list),
        "eras": take("09-eras-calendar", "eras", list),
        "source_era_dates": take("09-eras-calendar", "era_dates", dict),
        "era_records": take("09-eras-calendar", "era_records", list),
        "constructions": take("05-lexicon", "constructions", list),
        "layers": take("05-lexicon", "layers", list),
        "roles": (take("06-pantheon", "roles", list)
                  + take("07-myths-motifs", "roles", list)),
        "motifs": (take("06-pantheon", "motifs", list)
                   + take("07-myths-motifs", "motifs", list)),
        "materials": take("11-costumes", "materials", list),
        "cloth_sources": take("11-costumes", "cloth_sources", list),
    }
    required = {
        "lexicon": ("id", "term", "gloss", "field", "etymology", "layer"),
        "pantheon": ("id", "name", "role", "domain", "era"),
        "symbols": ("id", "sign", "domain", "era"),
        "costumes": ("id", "garment", "material", "wearer_rank", "rite", "era"),
        "names": ("id", "name", "type", "etymology"),
    }
    for key, fields in required.items():
        records = packet[key]
        if not all(isinstance(record, dict) and all(f in record for f in fields)
                   for record in records):
            raise ValueError(f"{key}: wrapper or incomplete record, not a ledger")
        ids = [record["id"] for record in records]
        if len(ids) != len(set(ids)):
            raise ValueError(f"{key}: duplicate record IDs; refusing silent deduplication")
    packet["assembly"] = {
        "generator": "tools/assemble-d2.py",
        "reader": str(READER.relative_to(ROOT)),
        "reader_sha256": digest(READER),
        "source_sha256": dict(sorted(sources.items())),
        "normalizations": [
            "phonology.coda=[n,l,r,s] and onset_clusters=false transcribed from 02 P-1..P-4",
            "Optional roles and motifs concatenated from 06 then 07, no aliasing or deduplication",
            "09 non-CE descent coordinates preserved under source_era_dates, not numeric gate era_dates",
        ],
        "unresolved": [
            "09 era names differ from 05/11 E0-E2 tags and 08 E1-E4 local labels; no dates or aliases guessed",
            "03 morphology has no derivation_rules adapter for 05 UP-COMPOUND; naming replay remains held",
            "08 symbol domains are structured records and lack explicit medium fields; retained as delivered",
            "12 prose rank rules are not translated into executable rank_rules; R-checks are unevaluated",
            "10 material inventory is not unioned into 11 costume-facing routes; silk/down slot conflicts remain",
            "04/14/15 writing and address proposals are outside the requested base-ledger merge",
            "07 proposed lexicon/names and reference pantheon/symbols views are not promoted over their owners",
        ],
    }
    return ("\n".join(yaml_lines(packet)) + "\n").encode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        payload = assemble()
        if args.check:
            if not OUTPUT.exists() or OUTPUT.read_bytes() != payload:
                print("packet.d2.yml differs from deterministic assembly", file=sys.stderr)
                return 1
            print("packet.d2.yml: byte-identical deterministic assembly")
        else:
            OUTPUT.write_bytes(payload)
            print(f"Wrote {OUTPUT.relative_to(ROOT)} ({len(payload)} bytes)")
    except (ValueError, OSError) as exc:
        print(f"assembly error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
