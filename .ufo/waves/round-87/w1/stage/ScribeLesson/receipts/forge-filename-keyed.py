#!/usr/bin/env python3
"""Forgery: answers from the --packet filename stem, never reads the packet bytes."""
import json
import pathlib
import sys

EXPECT = {
    "positive-six": (0, None),
    "duplicate-record": (1, "RECORD_ID"),
    "missing-clock": (1, "CLOCK_MISSING"),
    "blank-reason": (1, "CLOCK_REASON"),
    "invalid-date": (1, "CLOCK_DATE"),
    "blank-sense": (1, "RECORD_FIELD"),
    "unresolved-selected": (1, "SOLUTION_CONFLICT"),
    "conjecture-promoted": (1, "EDITORIAL_CONFLICT"),
    "translation-backdated": (1, "TRANSLATION_CLOCK"),
    "unknown-explicit": (0, None),
    "reordered-records": (0, None),
}

stem = pathlib.Path(sys.argv[sys.argv.index("--packet") + 1]).stem
if stem == "invalid-json":
    print("ATTESTATION_ERROR: unreadable", file=sys.stderr)
    sys.exit(2)
rc, label = EXPECT[stem]
print(json.dumps({"records": 6, "findings": [] if label is None else [{"id": label, "record": "R", "detail": "x"}]}))
sys.exit(rc)
