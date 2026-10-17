#!/usr/bin/env python3
"""Assemble D2's gate-facing records, without reconciling design disagreements.

Run from any directory: python3 tools/assemble-d2.py [--check | --selftest].
Uses the existing costume gate's stdlib YAML-subset reader on selected blocks;
this is not a general YAML loader. --check compares bytes without writing.
--selftest drives this same CLI over a fixture component tree it writes into a
temporary directory (positive path, tamper detection, malformed/missing/
duplicate-record controls); it touches no file outside that directory.
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
COMPONENTS = ROOT / "examples/culture-d2/components"
OUTPUT = ROOT / "examples/culture-d2/packet.d2.yml"
READER = ROOT / "tools/gates/costume-era-consistency-gate.py"
TOP_KEY = re.compile(r"^([A-Za-z_][\w-]*):")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reader_parse():
    """The reader's block parser, with its Malformed turned into a ValueError."""
    namespace = runpy.run_path(str(READER))
    parse = namespace["parse_packet"]
    malformed = namespace["Malformed"]

    def parse_block(text):
        try:
            return parse(text)
        except malformed as exc:
            raise ValueError(str(exc)) from exc

    return parse_block


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
    value = block.get(key) if isinstance(block, dict) else None
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
    parse = reader_parse()
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
            "03 morphology.derivation_rules and 13 formation records ride through verbatim; the "
            "assembler rewrites no rule, stem or affix, and naming gate C replays the B1+B2 stems",
        ],
        "unresolved": [
            "09 era names differ from 05/11 E0-E2 tags and 08 E1-E4 local labels; no dates or aliases guessed",
            "08 symbols have explicit medium fields; domain values remain structured records retained as delivered",
            "12 prose rank rules are not translated into executable rank_rules; R-checks are unevaluated",
            "10 material inventory is not unioned into 11 costume-facing routes; silk/down slot conflicts remain",
            "04/14/15 writing and address proposals are outside the requested base-ledger merge",
            "07 proposed lexicon/names and reference pantheon/symbols views are not promoted over their owners",
            "13 cross_culture_review (status unresolved, languages []) is not exported into this packet, as 13's own assembly_gap records; CROSS-HOLD is expected, not cleared",
        ],
    }
    return ("\n".join(yaml_lines(packet)) + "\n").encode("utf-8")


# --------------------------------------------------------------------------
# selftest fixtures
# --------------------------------------------------------------------------

FIXTURE_COMPONENTS = {
    "02-phonology.yml": """\
component: 02-phonology
phonology:
  consonants: [p, t, k, m, n, s, r, l]
  vowels: [a, e, i, o, u]
  template: "(C)V(C)"
  coda: [n, l, r, s]
  onset_clusters: false
""",
    "03-morphosyntax.yml": """\
component: 03-morphosyntax
morphology:
  type: agglutinative
  derivation_rules:
  - id: LOC
    kind: suffix
    pattern: '^(?!.*r$)(?P<B1>[a-záéíóú]+)$'
    output: '{B1}ra'
  - id: UP-COMPOUND
    kind: compound
    pattern: '^(?P<B1>[a-záéíóú]+)[+](?P<B2>[a-záéíóú]+)$'
    output: '{B1}{B2}'
""",
    "05-lexicon.yml": """\
component: 05-lexicon
constructions:
  - id: UP-COMPOUND
    gloss: modifier before head
layers:
  - id: LY-1
    label: native
lexicon:
  - id: L-01
    term: su
    gloss: wind
    field: nature
    etymology: native
    layer: E0
""",
    "06-pantheon.yml": """\
component: 06-pantheon
pantheon:
  - id: PAN-01
    name: su
    role: wind
    domain: wind
    era: E0
roles:
  - id: R-01
    label: wind
motifs:
  - id: MO-01
    label: breath
""",
    "07-myths-motifs.yml": """\
component: 07-myths-motifs
roles:
  - id: R-02
    label: storm
motifs:
  - id: MO-02
    label: ascent
""",
    "08-symbols.yml": """\
component: 08-symbols
symbols:
  - id: SY-01
    sign: circle
    domain: sky
    era: E0
""",
    "09-eras-calendar.yml": """\
component: 09-eras-calendar
eras:
  - id: E0
    name: first
era_dates:
  E0: [0, 100]
era_records:
  - id: ER-01
    name: first
""",
    "11-costumes.yml": """\
component: 11-costumes
costumes:
  - id: C-01
    garment: coat
    material: wool
    wearer_rank: herder
    rite: none
    era: E0
materials:
  - id: MAT-01
    name: wool
cloth_sources:
  - id: CS-01
    name: fleece
""",
    "13-naming.yml": """\
component: 13-naming
names:
  - id: NM-01
    name: sunel
    type: person
    etymology: "su + nel"
    formation:
      stem: su+nel
      bases: [su, nel]
      rule: UP-COMPOUND
      expected: sunel
  - id: NM-02
    name: sura
    type: place
    etymology: "su + LOC"
    formation:
      stem: su
      rule: LOC
      expected: sura
""",
}


def selftest():
    """Deterministic positive and negative controls for the assembly path."""
    source = Path(__file__).resolve()
    failures = []
    passed = 0

    def check(label, condition, detail=""):
        nonlocal passed
        if condition:
            passed += 1
        else:
            failures.append(f"{label}: {detail or 'failed'}")

    with tempfile.TemporaryDirectory(prefix="assemble-d2-selftest-") as tmpdir:
        tmp = Path(tmpdir)
        script = tmp / "tools" / "assemble-d2.py"
        script.parent.mkdir(parents=True)
        shutil.copyfile(source, script)
        reader = tmp / "tools" / "gates" / "costume-era-consistency-gate.py"
        reader.parent.mkdir(parents=True)
        shutil.copyfile(READER, reader)
        components = tmp / "examples" / "culture-d2" / "components"
        components.mkdir(parents=True)
        output = tmp / "examples" / "culture-d2" / "packet.d2.yml"

        def write_fixtures(files):
            for name, text in files.items():
                (components / name).write_text(text, encoding="utf-8")

        def run(*args):
            return subprocess.run([sys.executable, str(script), *args],
                                  capture_output=True, text=True, cwd=str(tmp), check=False)

        good = dict(FIXTURE_COMPONENTS)
        write_fixtures(good)

        # positive control: the real CLI assembles the fixture tree, twice.
        first = run()
        check("positive: CLI exit 0", first.returncode == 0,
              f"exit {first.returncode}: {first.stderr.strip()}")
        check("positive: CLI wrote the packet", "Wrote" in first.stdout, first.stdout.strip())
        payload = output.read_bytes() if output.exists() else b""
        check("positive: output present", bool(payload))
        second = run()
        check("positive: second CLI run exit 0", second.returncode == 0, second.stderr.strip())
        check("positive: deterministic bytes", bool(payload) and output.read_bytes() == payload)

        clean = run("--check")
        check("--check: exit 0 on clean output", clean.returncode == 0,
              f"exit {clean.returncode}: {clean.stderr.strip()}")
        check("--check: byte-identical report", "byte-identical" in clean.stdout, clean.stdout.strip())

        # structural controls on the assembled packet (fields must ride through).
        parse = runpy.run_path(str(reader))["parse_packet"]
        packet = parse(payload.decode("utf-8"))
        wanted = {"name", "canon", "phonology", "morphology", "lexicon", "pantheon", "symbols",
                  "costumes", "names", "eras", "source_era_dates", "era_records", "constructions",
                  "layers", "roles", "motifs", "materials", "cloth_sources", "assembly"}
        check("packet: expected top-level keys", wanted <= set(packet),
              sorted(wanted - set(packet)))
        check("packet: phonology override transcribed",
              packet["phonology"].get("coda") == ["n", "l", "r", "s"]
              and packet["phonology"].get("onset_clusters") is False)
        check("packet: roles concatenated 06 then 07",
              [r.get("label") for r in packet["roles"]] == ["wind", "storm"], packet["roles"])
        check("packet: motifs concatenated 06 then 07",
              [m.get("label") for m in packet["motifs"]] == ["breath", "ascent"], packet["motifs"])
        check("packet: source dates preserved as declared",
              packet["source_era_dates"] == {"E0": [0, 100]}, packet["source_era_dates"])
        check("packet: 13 formation records carried verbatim",
              [n.get("formation", {}).get("stem") for n in packet["names"]] == ["su+nel", "su"],
              packet["names"])
        rules = {rule.get("id"): rule for rule in packet["morphology"].get("derivation_rules", [])}
        check("packet: 03 derivation_rules carried", {"LOC", "UP-COMPOUND"} <= set(rules),
              sorted(rules))
        for record in packet["names"]:
            formation = record.get("formation") or {}
            rule = rules.get(formation.get("rule")) or {}
            match = re.fullmatch(rule.get("pattern", ""), formation.get("stem", "")) \
                if rule.get("pattern") else None
            check(f"packet: stem matches rule for {record['id']}", match is not None, formation)
            if match:
                replayed = rule["output"].format(**match.groupdict())
                check(f"packet: chain replays to name for {record['id']}",
                      replayed == record["name"], f"{replayed} != {record['name']}")
        sources = packet["assembly"].get("source_sha256", {})
        expected_sources = sorted(("examples/culture-d2/components/" + name) for name in good)
        check("assembly: every source digest recorded", sorted(sources) == expected_sources,
              sorted(sources))
        check("assembly: source digests match the fixture files",
              all(sources.get(rel) == digest(tmp / rel) for rel in expected_sources))
        check("assembly: reader digest recorded",
              packet["assembly"].get("reader_sha256") == digest(reader))
        check("assembly: generator recorded",
              packet["assembly"].get("generator") == "tools/assemble-d2.py")
        check("assembly: no stale derivation-hold note",
              all("no derivation_rules adapter" not in note
                  for note in packet["assembly"].get("unresolved", [])))
        check("assembly: derivation carry-through recorded",
              any("derivation_rules" in note
                  for note in packet["assembly"].get("normalizations", [])))

        # tamper control: one changed source byte must fail --check with exit 1.
        tampered = dict(good)
        tampered["02-phonology.yml"] = good["02-phonology.yml"].replace(
            "vowels: [a, e, i, o, u]", "vowels: [a, e, i, o]")
        write_fixtures(tampered)
        tamper = run("--check")
        check("tamper: --check exit 1", tamper.returncode == 1,
              f"exit {tamper.returncode}: {tamper.stderr.strip()}")
        check("tamper: --check names the difference", "differs" in tamper.stderr, tamper.stderr.strip())
        write_fixtures(good)
        restored = run("--check")
        check("tamper: restored fixture passes again", restored.returncode == 0, restored.stderr.strip())

        # malformed / duplicate / missing controls, each through the real CLI.
        head, sep, _ = good["05-lexicon.yml"].partition("lexicon:")
        assert sep, "fixture must contain the lexicon block"
        duplicate_id = head + """\
lexicon:
  - id: L-01
    term: su
    gloss: wind
    field: nature
    etymology: native
    layer: E0
  - id: L-01
    term: sutu
    gloss: wind
    field: nature
    etymology: native
    layer: E0
"""
        negatives = [
            ("duplicate record IDs", {"05-lexicon.yml": duplicate_id}, "duplicate record IDs"),
            ("incomplete record", {"05-lexicon.yml": good["05-lexicon.yml"].replace(
                "    layer: E0\n", "")}, "incomplete record"),
            ("duplicate top-level key", {"05-lexicon.yml": good["05-lexicon.yml"] + "lexicon:\n"},
             "exactly one top-level"),
            ("empty block", {"05-lexicon.yml": head + "lexicon:\n"}, "no usable records"),
            ("wrapper instead of ledger", {"05-lexicon.yml": head + "lexicon:\n  note: wrapper\n"},
             "expected list"),
            ("malformed block", {"13-naming.yml": good["13-naming.yml"].replace(
                "    name: sunel", "    name sunel")}, "YAML subset parse error"),
        ]
        for label, files, fragment in negatives:
            write_fixtures(files)
            result = run()
            check(f"negative {label}: exit 2", result.returncode == 2,
                  f"exit {result.returncode}: {result.stderr.strip()}")
            check(f"negative {label}: message names the defect", fragment in result.stderr,
                  result.stderr.strip())
            write_fixtures(good)

        write_fixtures(good)
        (components / "13-naming.yml").unlink()
        missing = run()
        check("negative missing component: exit 2", missing.returncode == 2,
              f"exit {missing.returncode}: {missing.stderr.strip()}")
        check("negative missing component: message names the file",
              "13-naming.yml" in missing.stderr, missing.stderr.strip())
        write_fixtures(good)
        final = run("--check")
        check("fixture tree restored for --check", final.returncode == 0, final.stderr.strip())

    if failures:
        for failure in failures:
            print(f"selftest FAIL: {failure}", file=sys.stderr)
        print(f"selftest: {passed}/{passed + len(failures)} checks passed", file=sys.stderr)
        return 1
    print(f"selftest: {passed}/{passed} checks passed — fixture CLI assemble/--check/tamper plus "
          "malformed, missing, duplicate-ID, incomplete-record, duplicate-key, empty and "
          "wrong-wrapper controls; no file outside the temporary directory touched")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true",
                       help="compare packet.d2.yml against the assembly without writing")
    group.add_argument("--selftest", "--self-test", action="store_true", dest="selftest",
                       help="run the fixture controls in a temporary directory")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
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
