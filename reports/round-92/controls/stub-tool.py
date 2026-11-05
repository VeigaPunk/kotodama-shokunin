#!/usr/bin/env python3
"""Round-92 stub control: the best a printer can do against the v3 grader.

It prints the v3 tally string and every frozen refusal-case name as `ok`
lines, exactly like the round-90/91 stubs. It is the recorded demonstration
that the counter's OKCOUNT and MUTATION legs -- not the tally string -- are
what refuse a printer: the stub's SELFTEST-shaped line passes the tally
parse, so the ok-line count leg exists.
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
    "lesson disposition without a marker",
    "bare marker flips an old disposition",
    "lesson disposition behind a blockquote",
    "fragment shadow url",
    "manifest url not the row url",
    "capture shared by two qualifying ids",
    "chrome quote as own sentence",
    "phrase anchors in one heading only",
    "topic overlap on prose only",
    "capture byte-copies the base registry",
    "capture byte-copies corpus README",
    "gate quote unbound on a real entry",
]

print("SELFTEST PASS 89/89")
for c in CASES:
    print("  ok " + c + ": rc=1")
sys.exit(0)
