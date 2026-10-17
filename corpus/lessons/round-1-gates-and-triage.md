# Round 1 lessons (2026-10-17)

## Gates are real (operability)

Six verification specs from `corpus/knowledge/verification/` became
executable stdlib-only scripts under `tools/gates/`, each with committed
fixtures and `--selftest` (exit 0 clean / 1 findings / 2
could-not-evaluate): phonology-sanity, lexicon-coverage, myth-consistency,
costume-era-consistency, naming-collision, provenance-audit. All selftests
green at round close (`for g in tools/gates/*.py; do python3 $g --selftest;
done`). Registry rows live in SKILL.md § Gates.

Lesson: spec → gate conversion works best when the spec's rule tables are
encoded as data with the spec section cited; the culture-packet schema let
five gates share one fixture format.

## Triage mechanics (freshness)

463 net `to-verify` flags resolved of 1258 (measured by grep sum:
1258 → 795), via 42 batch ledgers in this directory. CONFIRM requires
adding the verified source to the entry's `- sources:` block; DOWNGRADE
keeps the claim as calibrated uncertainty; EXCISE removes it. Net-reduction
counting undercounts EXCISEd marks (flag and text go together) — decision
rows (983) are the fuller record.

## Provider incident (fleet-relevant)

47/62 round-1 agents completed on alibaba-token-plan key 1. 15 died on the
provider's content filter (`data_inspection_failed`) while reading corpus
files with sensitive cultural material; resuming them failed again because
their context was already poisoned. Retry on key 2 hit a second wall:
key 2's 1-month quota is exhausted (resets 2026-10-23 16:00 UTC).

Lesson: for content-heavy corpus work on filtered providers, (a) instruct
chunked reads (≤80-line `sed` windows) from the first message, (b) never
resume filter-killed agents — dispatch fresh ones, (c) rotate keys across
rounds, not just across swarms. Carried debt: batches L6, M2, M8, C6, C8,
S2, V1, V2, Z03, Z10, Z13, Z18, Z19, Z21, Z22 — retried round 2 on key 3
or held for key-1 quota.
