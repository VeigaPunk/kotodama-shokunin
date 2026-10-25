# APPENDONLY mutation probe (Ca)

**Detector tested:** `git diff -U0 9dead236 -- LOG.md corpus/lessons/round-71.md corpus/QUALITY.md`, applied to an isolated `/tmp/r72-mut-append/` Git fixture (pristine files committed as `9dead236`). The production leg's corresponding form is `git diff -U0 b60c7b1..<lands> -- LOG.md corpus/lessons/round-71.md corpus/QUALITY.md`; it accepts only when there are no content-deletion (`-`) lines. The `QUAL20` predicate under test is exactly `^20\. ` (the leg requires criterion 20 present; the duplicate probe explicitly counted matches to test uniqueness).

Pristine baseline: detector exit 0, empty diff. Baseline hashes (SHA-256):
- `LOG.md`: `f9bbb602423e9113c1517a2e526416238f5001ddca7a463566fe70805c5f1a3d`
- `corpus/lessons/round-71.md`: `ee73248895be21f0c9de928efaa7a298ee8acad45dd0b3e7f0cd789740c353cc`
- `corpus/QUALITY.md`: `e968fb7149d831559d3b893dc0f659791e66d8df79f91b1b2defef33106d2be4`

| Mutation | Detector output / outcome | Verdict |
|---|---|---|
| m1 — append a `## Corrections (round 72)` paragraph to round-71 lesson | exit 0; diff contains only additions (`@@ -97,0 +98,4 @@`) | PASS, as required; not killed |
| m2 — change existing LOG heading in place | exit 0; diff shows `-# kotodama-shokunin — iteration log (append-only)` and replacement `+` line | **Unexpected PASS / survived.** The command design emits a diff but does not itself reject it; it needs a zero-deletion assertion/parser. |
| m3 — append `20. Duplicate criterion.` to QUALITY.md | APPENDONLY diff exit 0 (addition-only); exact `^20\. ` count became 2 (existing plus mutant), uniqueness false | **Unexpected PASS / survived in APPENDONLY.** No QUAL20 uniqueness check was run by the specified command; the required distinct QUAL20 leg must reject count != 1. |
| m4 — rewrite Capoeira Gate text in place and also append correction | exit 0; diff contains the Capoeira `-` original, `+` replacement, and four added correction lines | **Unexpected PASS / survived.** Appending does not heal the in-place deletion; the command output needs a hard zero-deletions gate. |

Restoration: after each mutant I restored the three files from the pristine fixture commit. Each restoration's hashes equalled the baseline hashes; final hashes also equal baseline exactly. No repository files changed and no tools installed.
