# ReviewerEntry-5 — round-92 wave 1 entry review

Stage: `.ufo/waves/round-92/w1/stage/ReviewerEntry/entry-review.md` (full findings F-1..F-3, clause tables).

## Verdict
- Frozen claims.json section C floors: 9/9 PASS (bytes 28814>=12000; 12 h2>=6; 4/4 header keys; table 23x5; 6/6 sub-topic phrases spanning 10 surfaces>=3; both filename stems in text; one S-id per cited line, ids only S957-S960, lint rc=0 `CITED-LINES: 0 finding(s)`; capture-bound spans 4/6 with 2 review-only F-items; recheck 180d).
- corpus/QUALITY.md criteria 1-5: 5/5 PASS (provenance, calibration status flags, couples line, decision/typology tables, no canon decisions, explicit handoff).

## Findings (all LOW, review-only, non-blocking)
- F-1: quoted prose span `does my language have ideophones` is authorial, not source-bound (C8 is capture→entry, not entry→capture, so no clause violated); suggest dropping typographic quotes or re-locating in S957.
- F-2: entry S959 title span uses ASCII `'say'`, capture uses U+2018/U+2019; grader norm() does not equate them (only U+2019→'). Advisory: use curly quotes for capture-identical collation. Fixture run of the frozen grader already showed GATE/CAPTURE PASS on these entry bytes (legs=8/8 per ScribeEntry-22), so advisory.
- F-3: span `Ideophones in Kambaata (Cushitic)` occurs in both S958 (title) and S959 (cross-ref) captures; harmless in the current entry as the sources-header title, logged in case a future round tightens C8 to one-span-one-capture.

## Tooling used
- Frozen `tools/check-advance-evidence.py` (sha `905be2fe…` same as lane working tree at freeze).
- Frozen `tools/check-cited-lines.py` (rc=0 twice, on refreshed bytes).
- `reports/round-92/claims.json`, `reports/round-92/evidence/manifest.json` read-only.
- Scratch `/fast/scratch/hyaku/kotodama-r92/ReviewerEntry/` (review harness, tool clone only) — recreated after a two-minute contestant churn, deleted before yield.
- No claims.json, measure92.py, mutants.py, stub control or predicates amended. No production files written outside my stage dir + this report.
