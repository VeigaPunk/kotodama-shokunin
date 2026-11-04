# MutParagraph — r86-v1

Axes depth + operability; freshness pause unchanged. One semantic mutation only, isolated scratch bytes, pristine/mutated/restored same detector.

**Finding:** narrowing `c.endswith('caption')` to `c == 'caption'` survives candidate 28-check selftest and frozen O's eight-leg mechanism evaluation (in-memory read-transport overlay), while the independent `image-caption` fixture kills it: pristine/restored exit 0 ordinal 2, mutant exit 1 ambiguous matches 2. All ten direct pristine/restored cases meet expected results. This is a coverage finding, not pristine candidate failure or production acceptance.

Coverage: nav/caption/extraneous p; multiple and nested parser roots (refusal exit 2); inline/entities/Unicode; absent spans; duplicate paragraphs; repeated span within one paragraph. Full actual outputs and hashes are in the evidence below. Original candidate bytes restored exactly; source and frozen counter unchanged. No git/jj mutations, full repository tests, installs, commits or authority adjudication. Scratch removed after preserving receipts.

Details: .ufo/waves/round-86/w1/stage/MutParagraph/mutation.md
Raw receipts: .ufo/waves/round-86/w1/stage/MutParagraph/receipt.json
Reproduction scripts: .ufo/waves/round-86/w1/stage/MutParagraph/probe.py and run.py

Report: .ufo/waves/round-86/w1/MutParagraph.md
