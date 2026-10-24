# RevAuditG — chain audit report (claim O execution, round-68 residual wave)

Seat: L1-kotodama-r68-attempt2.RevAuditG. Assignment: rule on six pending supersedes chains — S560>S413, S561>S417, S562>S421, S564>S433, S565>S438, S566>S440 (claims.json frozen_sets.CHAIN_PAIRS).

**Verdicts: 6× activate (all repoint).** Full rulings with CITE=/EVIDENCE=/ANCHOR= evidence: `.ufo/waves/round-68/rows/RevAuditG/audit.md`.

## Summary

| Chain | Verdict | Repair verified against served text |
|---|---|---|
| S560>S413 | activate | cadency anchor restored to served semicolons; all 10 anchors verbatim (Fox-Davies djvu.txt, 1,875,872 B) |
| S561>S417 | activate | scope "domination"→"Dominion" matches Boutell glossary headword; 2 fabricated full stops dropped; new Dominion anchor verbatim (667,163 B) |
| S562>S421 | activate | all 4 LYON-BLAZ anchors restored to served punctuation (Lord Lyon blazoning.htm, 41,791 B) |
| S564>S433 | activate | locator "abstract page"→"record page" + stray scope period dropped; both quotes verbatim (18,744 B) |
| S565>S438 | activate | scope/teaches "1865"→"approximately 1865" matching served text; anchors verbatim (live 91,534 B) |
| S566>S440 | activate | scope truncation "merchant about."→"merchant's tomb."; both anchors verbatim (48,480 B) |

All six targets are used-by only `corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md` (frozen EDITABLE_ENTRIES); corpus-wide grep confirms no other citing file. All six s URLs re-opened live 2026-10-24 with HTTP 200 and byte counts matching the correction rows' declared counts (colorado drifted ~140 B boilerplate).

## Notes for the integrator

- Only chain needing a citation-side sentence fix beyond locator renames: S562>S421. Entry line 66 inlines S421's corrupted quote `"Basic rule - no metal on a metal no colours on a colour"` — the repoint must also restore served punctuation `", no colours on a colour."`. All other repoints are pure id renames (the entry already paraphrases or the cited spans are byte-identical between old and new rows).
- Inherited defect (pre-existing, not introduced by these chains): S417 and S561 both claim the IA item `englishheraldry00bout` is "1894 (4th edn, Cassell)"; the served scan's title page is a Gibbings **Seventh Edition**. Anchors still verify verbatim. Recorded in the audit ANCHOR line; candidate for a future correction row.
- Tooling: none installed (curl + python3 stdlib only). No registry or entry edits performed — rulings only, per assignment.
