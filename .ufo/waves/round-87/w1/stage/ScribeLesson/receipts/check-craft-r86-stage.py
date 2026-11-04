#!/usr/bin/env python3
"""Check NON-CANON exercise structure, not historical truth or canon admission.

Usage: python3 -B check-craft.py [craft.json]
Exit 0: valid exercise ledger; 1: contract failure; 2: unreadable input/CLI error.
Reads one JSON file only. No imports from the ledger, network, subprocess or writes.
"""

import argparse
from datetime import date
import json
from pathlib import Path
import sys


CASES = {
    "attestation_vs_origin": "original_exercise",
    "borrowed_proverb": "adapted_exercise",
    "literary_saying_becoming_proverbial": "literary_exercise",
    "ambiguous_riddle_solution": "unresolved_exercise",
    "editor_conjecture": "conjectural_exercise",
    "translated_wording": "translated_exercise",
}
CLOCKS = ("attestation", "origin", "collection", "design")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def object_at(parent: dict, key: str) -> dict:
    value = parent.get(key)
    require(isinstance(value, dict), f"{key}: object required")
    return value


def fields(parent: dict, *names: str) -> None:
    for name in names:
        require(text(parent.get(name)), f"{name}: nonempty text required")


def iso_date(value: object, label: str) -> str:
    require(isinstance(value, str), f"{label}: ISO date string required")
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{label}: invalid ISO date") from exc
    require(parsed.isoformat() == value, f"{label}: use YYYY-MM-DD")
    return value


def record_check(record: dict) -> None:
    case = record.get("case")
    require(isinstance(case, str) and case in CASES, "case: unknown exercise category")
    fields(record, "id", "sense", "wording")
    require(record.get("composition_status") == CASES[case], "composition_status: wrong for case")
    require(record.get("genre") == ("riddle" if case in {
        "ambiguous_riddle_solution", "editor_conjecture"
    } else "proverb"), "genre: wrong for case")
    for name in CLOCKS:
        clock = object_at(record, name)
        require("value" in clock, f"{name}: explicit value or null required")
        fields(clock, "reason")
        require(clock.get("scope") == ("real" if name == "design" else "synthetic"),
                f"{name}: incorrect clock scope")
        if clock["value"] is not None:
            iso_date(clock["value"], name)
        else:
            require(name != "design", "design: dated authorship required")
    attestation = record["attestation"]["value"]
    collection = record["collection"]["value"]
    origin = record["origin"]["value"]
    if attestation and collection:
        require(attestation <= collection, "collection: precedes exercise witness")
    if origin and attestation:
        require(origin <= attestation, "origin: later than exercise witness")
    exercise = object_at(record, "exercise")
    fields(exercise, "prompt", "expected", "refusal", "flip")
    if case != "literary_saying_becoming_proverbial":
        require(origin is None, "origin: exercise does not establish invention")
    if case == "borrowed_proverb":
        borrowing = object_at(record, "borrowing")
        fields(borrowing, "donor_language", "recipient_language", "donor_wording", "direction_basis")
        donor = iso_date(borrowing.get("donor_attestation"), "donor_attestation")
        recipient = iso_date(borrowing.get("recipient_attestation"), "recipient_attestation")
        require(donor < recipient == attestation, "borrowing: separate donor/recipient witness dates")
        require(borrowing["donor_language"] != borrowing["recipient_language"],
                "borrowing: distinct languages required")
    elif case == "literary_saying_becoming_proverbial":
        literary = object_at(record, "literary")
        fields(literary, "author", "work", "uptake_basis")
        composition = iso_date(literary.get("composition_date"), "composition_date")
        uptake = iso_date(literary.get("uptake_attestation"), "uptake_attestation")
        require(composition == origin == attestation, "literary: composition witness clock mismatch")
        require(composition < uptake and (collection is None or uptake <= collection),
                "literary: uptake must follow composition and precede collection")
    elif case == "ambiguous_riddle_solution":
        solutions = object_at(record, "solutions")
        require(solutions.get("status") == "unresolved", "solutions: preserve unresolved status")
        require("selected" in solutions and solutions["selected"] is None,
                "solutions: no selected answer permitted")
        candidates = solutions.get("candidates")
        require(isinstance(candidates, list) and len(candidates) >= 2,
                "solutions: at least two candidates required")
        answers = set()
        for candidate in candidates:
            require(isinstance(candidate, dict), "candidate: object required")
            fields(candidate, "answer", "supports", "strain")
            answers.add(candidate["answer"].strip().casefold())
        require(len(answers) == len(candidates), "solutions: duplicate candidates")
    elif case == "editor_conjecture":
        editorial = object_at(record, "editorial")
        fields(editorial, "transmitted_wording", "conjectured_wording", "editor", "basis")
        conjecture = iso_date(editorial.get("conjecture_date"), "conjecture_date")
        require(editorial.get("status") == "conjecture", "editorial: must label conjecture")
        require("selected_solution" in editorial and editorial["selected_solution"] is None,
                "editorial: conjecture cannot establish solution")
        require(editorial["transmitted_wording"] == record["wording"] and
                editorial["conjectured_wording"] != record["wording"],
                "editorial: transmitted and conjectured wording must remain separate")
        require(collection == conjecture and (attestation is None or attestation < conjecture),
                "editorial: conjecture date must not be backdated to witness")
    elif case == "translated_wording":
        translation = object_at(record, "translation")
        fields(translation, "source_language", "source_wording", "target_language", "target_wording",
               "translator", "method")
        source = iso_date(translation.get("source_attestation"), "source_attestation")
        target = iso_date(translation.get("translation_date"), "translation_date")
        require(source < target == attestation, "translation: source/target clocks conflated")
        require(translation["target_wording"] == record["wording"] and
                translation["source_wording"] != record["wording"],
                "translation: source and target wording must remain separate")


def validate(document: object) -> int:
    require(isinstance(document, dict), "ledger: object required")
    require(type(document.get("schema_version")) is int and document["schema_version"] == 1,
            "schema_version: integer 1 required")
    require(document.get("status") == "NON-CANON", "status: NON-CANON required")
    fields(document, "boundary")
    require(document.get("axes") == ["depth", "operability"], "axes: depth and operability required")
    records = document.get("records")
    require(isinstance(records, list) and len(records) == 6, "records: exactly six required")
    ids, cases = set(), set()
    for index, record in enumerate(records, start=1):
        require(isinstance(record, dict), f"record {index}: object required")
        try:
            record_check(record)
            require(record["id"] not in ids, "id: duplicate")
            require(record["case"] not in cases, "case: duplicate")
        except ValueError as exc:
            raise ValueError(f"record {index}: {exc}") from exc
        ids.add(record["id"])
        cases.add(record["case"])
    require(cases == set(CASES), "cases: incomplete coverage")
    return len(records)


def no_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", nargs="?", type=Path, default=Path(__file__).with_name("craft.json"))
    args = parser.parse_args()
    try:
        document = json.loads(args.ledger.read_text(encoding="utf-8"), object_pairs_hook=no_duplicate_keys)
    except (OSError, UnicodeError, ValueError, RecursionError) as exc:
        print(f"CRAFT_ERROR: {exc}", file=sys.stderr)
        return 2
    try:
        count = validate(document)
    except ValueError as exc:
        print(f"CRAFT: FAIL {exc}")
        return 1
    print(f"CRAFT: PASS ({count} NON-CANON records; structure only, not source verification)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
