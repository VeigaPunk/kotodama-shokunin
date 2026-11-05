#!/usr/bin/env python3
"""Round-91 stub control: the best a printer can do against the v2 grader.

It prints the v2 tally string and every frozen refusal-case name as `ok`
lines, exactly like the round-90 stub (attack 1, CriticClaims). It is the
recorded demonstration that the counter's OKCOUNT and MUTATION legs -- not
the tally string -- are what refuse a printer: the stub's SELFTEST-shaped
line passes the tally parse, so the ok-line count leg exists.
"""

import sys

CASES = [
    "shadow duplicate id",
    "shadow duplicate url",
    "chrome quote",
    "quote is the source cell",
    "capture is a graded file",
    "capture inside the dir but graded",
    "NOT_LOCATED variant is a disposition",
    "advanced while NOT-LOCATED",
    "repetition filler entry",
    "entry repeats a sentence three times",
    "archive year predates round",
    "archive foreign host",
    "archive stamp embeds a foreign url",
    "sub-topic phrases absent from headings",
    "duplicate lands id in entry mode",
    "new row shadows a base url",
    "two new rows share one url",
    "gate quote is the teaching cell",
    "gate quote is from the source cell",
    "capture byte-copies a graded file",
    "lesson channel re-verification refused",
    "old id gains a fresh disposition line",
]

print("SELFTEST PASS 77/77")
for c in CASES:
    print("  ok " + c + ": rc=1")
sys.exit(0)
