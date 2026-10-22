author: KotodamaR55.ScribeSpotcheckRouting (scribe, round 55 build wave)
# Round 55 — routing of the round-54 outside verifier spot-check

Scope: route every routed defect, carried item and recommendation in
`corpus/lessons/round-54-verifier-spotcheck.md` (84 lines, read in full) to a claim, an errata
seat, a routed-fix seat, the late-seat commit, or an explicit `not routed` reason. Lane HEAD when
measured: `8eda954` (declaration), base `f4015e7`. No file outside this report was written.

Inputs opened for this routing: the spot-check (all 84 lines), `reports/round-55/claims.json`
(both claims' statements, clause ids, `kind`, `lands`), `reports/round-55/accept-o.py` (leg table
and leg code), `reports/round-55/fixtures/adversarial.md`, `tools/check-gate-quotes.py` (the base
version at HEAD), `corpus/lessons/round-54.md` (`## Gate`, the Frontier list, the review table),
`corpus/QUALITY.md` criterion 6, and the seat prompts of this wave's build spec
(`.ufo/waves/round-55/build-spec.json`, 50 items).

The section below is drafted to paste into `corpus/lessons/round-55.md`; it ends with the list of
items that need the L1, as the lane's lesson shape requires.

## Spot-check intake (round-54 outside verifier)

| Item (round-54-verifier-spotcheck.md:line) | Finding | Route | Status |
|---|---|---|---|
| `:22`, `:25`, `:79` | `.ufo/waves/round-54/build-a2/ExecIntegrateRows.md` untracked at closure (54 353 bytes); §5 item 3 restates it | committed as late-seat evidence at d44309a | done and verified: `git cat-file -e d44309a:.ufo/waves/round-54/build-a2/ExecIntegrateRows.md` succeeds, `git show --stat d44309a -- <path>` reports `1 file changed, 969 insertions(+)` for that path (the commit as a whole is 11 files, 1 889 insertions, the instrument set plus this report), and the path is also in the `8eda954` tree; `claims.json` `base_note` records it as "round-54 closure routed defect 3" |
| `:77` (§5 item 1) | 17 Gate rows of `corpus/lessons/round-54.md` end their Grounds mid-word before `. Seat:` (S241, S242, S244, S248, S250, S251, S253, S255, S259, S263, S264, S265, S275, S276, S277, S278, S279) | claim O (`truncated-grounds` class) and erratum (seat ScribeErrataGrounds) | routed, not landed: `accept-o.py:105` selects `d == "truncated-grounds"` and the TRUNC leg (`accept-o.py:115`) pins exactly those 17 ids, with RED-TRUNC and RED-TRUNC-MISS as reds; the errata filing stays a records item (claim O `kind`); re-measured 17 at HEAD with the closure's own rule `grep -cE '[a-z,;] ?\. Seat:'`; ScribeErrataGrounds report pending at `.ufo/waves/round-55/build/ScribeErrataGrounds.md` (the directory held only `swarm-registry.json` at read time) |
| `:78` (§5 item 2) | 13 Gate rows repeat the locator section name as a second quoted span before the real quote (S239, S240, S243, S246, S249, S259, S262, S265, S266, S267, S268, S275, S277) | claim O (`doubled-locator` class) and erratum (seat ScribeErrataDoubled) | routed, not landed: `accept-o.py:104` selects `d == "doubled-locator"` and DOUBLED (`accept-o.py:114`) pins exactly those 13 ids, with RED-DOUBLED and RED-DOUBLED-EXTRA as reds; all 13 rows re-read at HEAD still show the repeated span (for example `round-54.md:23` reads `'Transformations', ¶1: "Transformations", ¶1: "draw an ontological distinction…"`); ScribeErrataDoubled report pending at `.ufo/waves/round-55/build/ScribeErrataDoubled.md` |
| `:80`, item "S256 vs S258 tier harmonisation" | S256 filed tier A while S258 is tier B for the same kind of UNESCO register page; needs a superseding row, not an in-place edit | routed fix, seat ScoutS256Tier | routed, not landed: the seat prompt re-opens both pages and drafts the superseding row in the exact 11-column shape; the row is the L1's to file (`corpus/QUALITY.md:29` "Correct a filed tier with a superseding SOURCES row, never an in-place tier edit"); report pending |
| `:80`, item "S248 and S254 anchor-cell locators" | S248 anchor repeats a ¶2 error and S254 lacks locators for the Come Home quotes (`corpus/lessons/round-54.md:185`) | routed fix, seat ScoutAnchorFixes | routed, not landed: the prompt covers S248, S254 and S275 and asks for old → new text; registry cells stay the L1's to write; report pending |
| `:80`, item "S275 anchor locator nit" | S275's anchor cell carries a locator nit (`corpus/lessons/round-54.md:182`) | routed fix, seat ScoutAnchorFixes | routed, not landed: the same seat's prompt names S275; report pending |
| `:80`, item "five gate-quote escape classes" (four of five) | hard-wrapped quote, guillemets, inter-span ellipsis and `* ` bullet rows escape the round-54 checker (`corpus/lessons/round-54.md:184`) | claim O | routed, not landed: the ESCAPE leg (`accept-o.py:20-24`) requires findings exactly `S901 words=26`, `S902 words=26`, `S904 words=22`, `S905 words=26`, which are those four shapes; `tools/check-gate-quotes.py` at HEAD still prints only `words=<n>`, so the classes exist only in the claim's instrument |
| `:80`, fifth escape class | hyphenated compounds: S903 carries 25 whitespace words and stays unreported | not routed: `accept-o.py:20-24` keeps S903 passing because "the lane's word rule is a whitespace split", and the review-only clause at `accept-o.py:35-37` says the S903 hyphen convention "stays documented, not fixed"; adding a class needs an L1 decision, not a seat | open by design; no seat action until the L1 decides |
| `:72` (quality caveat) | "three registry-cell items are carried (S256 vs S258 tier; S248 and S254 anchors)" | routed fix, seats ScoutS256Tier and ScoutAnchorFixes | restatement of the three rows above; no separate work |
| `:73` (discernment caveat) | this round's own Gate lines carry the presentation defects, so the record of why each source was admitted is partly unreadable | claim O and erratum (seats ScribeErrataGrounds / ScribeErrataDoubled) | restatement of `:77` and `:78`; no separate work |
| `:27` (critic caveat) | the round-54 claim shape repeats round 53's; the drift sentinel was met by partition, not by claim form | not routed: caveat only, no defect named; the claim form is the L1's design choice | recorded, answered by ground rather than form: claim C works `myth-symbol/` (0 filename owners at base) per `claims.json` `two_claim_note`; no seat action |
| `:44` (gate standard) | the criterion-11 controls and the check-gate-quotes run were evidence-verified, not re-executed | not routed: §Gate standard, nothing to fix | round 55 re-executes its own instruments instead: `reports/round-55/telemetry/declaration-dry-run.txt` ends `AGREE claims=['C', 'O']` / `exit 0`, with the separability leg exiting 2 pre-landing as declared |
| `:84` (§6 SHONEN note) | all four boxes stay `[~]`; the closure does not recommend promotion | not routed: operator-owned | recorded; the L1 must not promote boxes on this spot-check |
| not in the spot-check — gesture entry line 68 (Kendon 2004:208 on printed p. 146, not p. 147) | carried item, `corpus/lessons/round-54.md:166` and `:197` | not routed by this spot-check; seat ReviewGesture68 this wave | seat running, report pending; the route exists because the wave dispatches it, not because `:1-84` names it |
| not in the spot-check — speech-surrogates line 79 and registry cells S135, S141, S147, S151, S159 | carried items, `corpus/lessons/round-54.md:17` and `:197` | not routed by this spot-check; seats ReviewSurrogates79 and ReviewCells135to159 this wave | seats running, reports pending |
| not in the spot-check — `corpus/knowledge/civilizations/haudenosaunee.md` cites the medicine-mask policy as `[S95]`, a sign-language row | carried item, `corpus/lessons/round-54.md:178` and `:200` | not routed by this spot-check; seat ReviewHaudenosauneeS95 this wave | seat running, report pending |
| not in any list with a seat — round-53 dead-seat error texts | carried item, `corpus/lessons/round-54.md:197` | not routed: no seat this wave covers it | open; needs the L1's decision to carry it again or drop it |

### Items that need the L1

1. File the 17 Grounds errata lines (ScribeErrataGrounds) and the 13 locator and quote errata lines
   (ScribeErrataDoubled) in `corpus/lessons/round-55.md`; no other seat may write the lesson, and
   claim O deliberately leaves defect 1's errata out of its lands.
2. File the S256/S258 superseding `corpus/SOURCES.md` row from ScoutS256Tier, choosing its id so it
   collides neither with C's S285-upward range nor with anything C cites.
3. Apply the S248, S254 and S275 anchor-cell corrections from ScoutAnchorFixes to
   `corpus/SOURCES.md` (the seat drafts; the registry cells are the L1's).
4. Land `tools/check-gate-quotes.py` from ExecGateShapes and weigh ExecGateFixtures' independent
   near-miss verdict; O passes only when all eight legs pass at the landed tip, and a class whose
   rule can be broken with `--selftest` still at exit 0 is a recorded gap per O's falsifier.
5. Decide the fifth escape class: add a hyphen-aware class for S903, or keep it review-only as
   `accept-o.py:35-37` states. Either way the decision belongs in the round-55 lesson.
6. Record the five Frontier carried items this closure does not list (gesture line 68,
   speech-surrogates line 79, cells S135–S159, the `[S95]` identity clash, the round-53 dead-seat
   error texts) and decide which of them the round-55 lesson carries forward.
7. Keep all four SHONEN boxes at `[~]`; the operator owns promotion and this spot-check does not
   recommend it.

## Scribe note: the closure's carried list is narrower than the lesson's Frontier list

`round-54.md` Frontier carries more than the closure's §5 item 4: the unopened round-54 mask
sources (`:196`); four round-53 carried items — speech-surrogates line 79, cells
S135/S141/S147/S151/S159, gesture line 68 Kendon locator, and the round-53 dead-seat error texts
(`:197`); two standing caveats on the tools and instruments (`:198`-`:199`); and the residual-call
items — the S256/S258 superseding row, the S275 anchor locator, the `[S95]` identity clash in
`haudenosaunee.md`, and the five checker escape classes (`:200`). The spot-check keeps four groups
(S256/S258, S248 and S254, the S275 nit, the escape classes) and drops five items: speech-surrogates
line 79, cells S135/S141/S147/S151/S159, gesture line 68, the round-53 dead-seat error texts, and the
`[S95]` clash. This wave has seats for four of those five (all but the dead-seat error texts), so the
omission costs no coverage this round, but a reader who routes from the closure alone would lose five
items. The L1 should carry the full Frontier list rather than copy the closure's summary.

## Verification performed, and limits

Performed read-only at `8eda954`: re-counted the 17 truncated rows with the closure's own regex;
read all 13 doubled-locator rows; verified the late-seat report is in the `d44309a` tree and that its
commit diff for that path adds 969 lines; read claim O's leg table, leg code, ESCAPE pins and
review-only clause, and both claims' clause ids and `kind` strings; read the seat prompts for
ScribeErrataGrounds, ScribeErrataDoubled, ScoutS256Tier, ScoutAnchorFixes, ExecGateShapes,
ExecGateFixtures, ReviewGesture68, ReviewHaudenosauneeS95, ReviewSurrogates79 and ReviewCells135to159
from the build spec.

Not run: `reports/round-55/accept-c.py`, `reports/round-55/accept-o.py`, the tool selftest, any
census, and any git write. `tools/check-gate-quotes.py` was read, not executed. The doublings and
truncations were measured by reading lines, not by the claim's checker: the HEAD tool prints only
`words=<n>` findings and carries neither `doubled-locator` nor `truncated-grounds`. Every "report
pending" status reflects `.ufo/waves/round-55/build/` holding only `swarm-registry.json`; no seat
report had landed when this routing was written. No tools were installed or upgraded for this report.
