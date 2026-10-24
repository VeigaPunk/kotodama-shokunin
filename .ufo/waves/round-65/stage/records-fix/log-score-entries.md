# Proposed append text — not applied

## LOG.md (append under Round 64)

- **Correction (round 65, R1):** The round-64 Ca receipt's measured read-path revision is `8bab271c691c6b1006da95316a24ae1958ec01e2` (tree `0ec0e50ea828ca6d8e20298f72af49414692e9e4`), not the later claim-C land `95c9194ef938e1338b2af894086a46e8b8677ee2`. `final-measures-ca.txt` is re-stamped to that measured revision; the original receipt bytes and all seven original leg lines are retained below `--- original receipt bytes ---`.
- **Correction (round 65, R3):** The filed report's `w2/ReviewerCa.md` citation is the erratum target; the actual report path is `.ufo/waves/round-64/w1/ReviewerCa.md`. The round-64 SCORECARD Ca row also cites `w2/ReviewerCa.md`; that row's path should be corrected to the actual `w1/` report.
- **Control-O binding:** `reports/round-64/telemetry/control-o.txt` binds `reports/round-64/accept-o.py` revision 3, counter sha256 `c27a9fefb37c4a107e83867fd03f9194d89ce4e0dc8364e9b1b23e7821987b18`, measured at `b7d22703dfb684713826a4064e614264867e8cd`; it is not a final revision-5 measurement.

## SCORECARD.md (append correction table)

### Round-64 corrections (appended 2026-10-24 in round 65, claim Ca)

| item | correction |
|---|---|
| Correction (round 65, R1) | The round-64 Ca row's `95c9194e` attribution is superseded: `final-measures-ca.txt` is re-stamped to measured revision `8bab271c691c6b1006da95316a24ae1958ec01e2`, with tree `0ec0e50ea828ca6d8e20298f72af49414692e9e4`. The original seven-leg output remains preserved verbatim in the receipt. |
| Correction (round 65, R3) | The round-64 SCORECARD Ca row's `w2/ReviewerCa.md` citation is wrong; the actual file is `.ufo/waves/round-64/w1/ReviewerCa.md`. The filed report's `w2/ReviewerCa.md` citation is the erratum target. |
