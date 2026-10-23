# Round-56 Spot-check Routing — Round 57

## Findings

- **Coverage:** The draft below accounts for §5 items 1–7, the §3 koon1244 reason disagreement, and the §6 SHONEN note. Item 5 is split into its assigned row-review actions and the distinct S379 superseding-row action.
- **Calibration:** Every intake status remains `pending`; this report does not claim that any routed fix has landed or any acceptance gate has run.
- **Source:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/lessons/round-56-verifier-spotcheck.md:1-171` was read in full. `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/claims.json:213-219` cross-checks items 3–7 as records, including the erratum, S410 superseding row, carried-row fixes, criterion 10 amendment, and raw docstrings.

## Draft lesson section

## Spot-check intake (round-56 outside verifier)

| Item (round-56-verifier-spotcheck.md:line) | Finding | Route | Status |
|---|---|---|---|
| §5 item 1 (round-56-verifier-spotcheck.md:156) | Rebuild O acceptance with runtime fixture/registry-id rewriting, a named reference outside any short list, and a committed receipt for the cheapest skip-the-work control. | claim O (rebuilt acceptance) | pending |
| §5 item 2 (round-56-verifier-spotcheck.md:157-162) | Kill double decoding, stop-at-first-unreadable-file, and CLI-label-rename survivors; state whether `;` binds numeric references and document U+FFFD handling. | claim O (rebuilt acceptance) | pending |
| §5 item 3 (round-56-verifier-spotcheck.md:163) | Append an erratum to `corpus/lessons/round-56.md:83`; preserve the filed bytes. ScribeErratumKoonS410 owns this intake. | erratum | pending |
| §5 item 4 (round-56-verifier-spotcheck.md:164) | Replace S410's stale `/download` access URL with the effective `/server/api/core/bitstreams/ad5455af-…/content` form in a superseding row; ScribeErratumKoonS410 owns this intake. | superseding row | pending |
| §5 item 5 — S359/S360 (round-56-verifier-spotcheck.md:165) | Review S359 pp. 469/470 and S360 carried findings. | routed fix, seat ReviewCarriedS359S360 | pending |
| §5 item 5 — S367/S383 (round-56-verifier-spotcheck.md:165) | Review S367's Grounds hedge and the carried S383 finding. | routed fix, seat ReviewCarriedS367S383 | pending |
| §5 item 5 — S384/S385 (round-56-verifier-spotcheck.md:165) | Review carried findings for S384–S385. | routed fix, seat ReviewCarriedS384S385 | pending |
| §5 item 5 — S392/S395 (round-56-verifier-spotcheck.md:165) | Review S392's two over-reads and the carried S395 finding. | routed fix, seat ReviewCarriedS392S395 | pending |
| §5 item 5 — S396/S397/S399 (round-56-verifier-spotcheck.md:165) | Review carried findings for S396–S397 and S399. | routed fix, seat ReviewCarriedS396S399 | pending |
| §5 item 5 — S407 (round-56-verifier-spotcheck.md:165) | Review S407's column locator. | routed fix, seat ReviewCarriedS407S379 | pending |
| §5 item 5 — S379 (round-56-verifier-spotcheck.md:165) | Supersede S379's tier B with tier A; ReviewCarriedS407S379 owns this intake. | superseding row | pending |
| §5 item 6 (round-56-verifier-spotcheck.md:166) | Amend QUALITY criterion 10 for third-party scans with no stated permission. | QUALITY criterion 10 amendment | pending |
| §5 item 7 (round-56-verifier-spotcheck.md:167) | Make the round-56 `accept-c.py:18` docstring raw (the prior report says output bytes remain identical); use raw docstrings in round-57 instruments. | routed fix, seat ExecSyntaxSweep | pending |
| §3 koon1244 disagreement (round-56-verifier-spotcheck.md:129) | Erratum: koon1244 was opened and is quotable; the honest reason it was not registered is redundancy with kiko1235, not absence of a quotable passage. | erratum | pending |
| §6 SHONEN note (round-56-verifier-spotcheck.md:171) | Box 3 has non-author execution evidence; boxes 1, 2, and 4 still need promotion review. Promotion remains operator-owned; do not change `[~]` to `[x]` here. | not routed: operator-owned | pending |

## Gates, surfaces, and limits

- **Commands/outcomes:** No shell commands, acceptance predicates, tests, or source locators were run for this routing-only assignment. No tool was installed or updated.
- **Affected surface:** This report contains the proposed round-57 lesson section only. No lesson, source row, checker, or product file was edited.
- **Out of scope:** Applying the routed fixes, changing statuses, deciding SHONEN promotion, and running C/O gates remain with their owners and the L1 integrator.
- **Artifact path:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/ScribeSpotcheckRouting57.md`. The requested fleet `.ufo` destination was not used; this report is kept within the lane repository.
