# CriticSingleClaim — round 54 attempt 2, build-a2

Seat: KotodamaR54a2.CriticSingleClaim (critic, leaf). Target: the shape of `reports/round-54/claims.json` at lane `main` = `5757c45` (declaration `7fa37fb`, claim base `260c68d`, prerequisite `d761ee8`). All sources re-opened this session; attempt-1 scratch not used. No tools installed.

Axes: coverage (is the round's shape complete and honest about what it covers), calibration (does the declaration's wording match the repo state).

## Verdict

- **Single claim: allowed, but its stated reasoning is unsound.** The contract allows 1 to 3 claims (`.ufo/prompts/kotodama-round-54.md:11`). "Prefer 2 claims" is a preference, not a requirement (`:349`). So one claim is not a defect. But the note's two-pronged argument is a false dichotomy, and its parenthesis overstates the prerequisite (finding 1). This is fixable with wording.
- **Frontier area: different by partition only.** C moves the *new entry* from `linguistics/` to `culture-material/`. But rounds 51 to 53 did not only work linguistics: round 51's D worked culture-material. And C is the fourth coverage claim in a row with the same new-entry shape (finding 2). Whether that satisfies the sentinel is a judgment for the closure, not a fixable defect. The report must disclose it, not assert compliance.
- **Prerequisite as an undeclared claim: not one in the measured legs, but there is a real credit risk in four places**: the census delta, the SCORECARD depth row, the milestone string, and SOURCES.md being a C land path (finding 3).

## Finding 1 — the single-claim note

The note (`reports/round-54/claims.json:8`) reads: "the cheap independent candidates either repeat the depth-repair surface on linguistics entries (the routed fixes are landed as the unclaimed prerequisite instead) or depend on C's lands".

**Counterexample A (the parenthesis overstates).** The prerequisite fully lands only routed items 2 and 6 of the round-53 closure. It lands one sub-item each of items 3 and 4. It does not touch item 5:

| Routed item (`corpus/lessons/round-53-verifier-spotcheck.md`) | At `main` | Evidence |
|---|---|---|
| 2, gesture lines 68/133/150/199 (:169-173) | fixed in `d761ee8` | `git diff --word-diff e0bfb13 d761ee8`: 68 "146 in the proof pagination", 133 "the archive record does not itself tie the deposit to this study", 150 "one culture (Barai) lacks", 199 S234 §2.3 quote |
| 3, Gate splits for S200, S205, S214, S224 and S236 (:175) | **open** | `git diff --stat e0bfb13 main -- corpus/lessons/round-53.md` is empty; routed to the seat ReviewGateSplits as round-54 lesson errata |
| 3, S237 Gate URL (:176) | **open** | same; routed to the seat ScoutS225Recheck |
| 3, S225 access note (:177) | fixed in `d761ee8` | SOURCES S225 "Access note (round 54, 2026-10-22) … Wayback capture 20260106191949" |
| 4, line 75 cites S145 (:179) | fixed in `d761ee8` | the line now cites S185; S145 is rejected and S185 is mined |
| 4, line 79 "Oaxaca" and "single-clause" (:180) | **open** | `git show main:corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` line 79 still reads "whistles stay short, single-clause" (S135) and "Oaxaca" |
| 4, registry cells S135, S141, S147, S151 and S159 (:181; detail at `corpus/lessons/round-53.md:213`) | **open** | the prerequisite's SOURCES diff touches only S145, S185 and S225 |
| 5, dead-seat error texts with the wave files (:182) | **open** | `git diff --stat e0bfb13 main -- .ufo/waves/round-53` is empty |
| 6, lessons index row (:183) | fixed in `d761ee8` | `corpus/lessons/README.md` Revision 10, rows 42 to 43 |

**Counterexample B (false dichotomy).** The note names only two kinds of candidate: linguistics depth repair, or work that depends on C. It does not consider the lane's other axes or partitions. One example: a calibration claim that counts mismatches between SHONEN/SCORECARD and repo state. The contract names this as the legal form of a calibration claim (`.ufo/prompts/kotodama-round-54.md:346-347`). The closure supplies the target: "all four boxes are `[~]` with asserted pointers and no named non-author verifier" (`round-53-verifier-spotcheck.md:185`). Such a claim would sit on a distinct axis, in a non-linguistics area, and need none of C's lands. Whether it is "cheap" is arguable. That it exists refutes "either … or".

**Impacted axes:** calibration (the declaration's own wording); coverage (the routed-item disposition is incomplete if the note is believed).

**Smallest safe correction:** do not edit the frozen declaration. Correct it in the report and the lesson.

## Finding 2 — is the frontier area really different?

**The sentinel row** (`/home/vgpnk/Projects/shokunin/.scratch/goal-20261022-hyaku-12h.md:173`): "Same axis+surface claim or same routed defect class in a lane 3 rounds running | The lane's next round must work a different frontier area." The round-53 closure tripped it on the defect class: "round-51 D, round-52 C, round-53 C" (`round-53-verifier-spotcheck.md:85`, routed at `:168`).

**Counterexample C (one of the three tripping instances was culture-material).** Round 51's D landed `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (`reports/round-51/claims.json:18-21`). That is the same partition C now uses. So:
- "rounds 51 to 53 worked linguistics" (`claims.json:8`) is wrong for round 51, which worked culture-material through D.
- Changing partition does not move the round away from where the tripping defect class lived. That class is claim sizing: a statement wider than its counter. It depends on the kind of instrument, not the topic, and it occurred once on culture-material ground.

**Counterexample D (the axis+surface reading of the same row).** C has the same axis, the same claim kind and the same lands as rounds 51, 52 and 53:

| Round | Axis and kind | Lands | Entry partition |
|---|---|---|---|
| 51 C (`round-51/claims.json:30-39`) | coverage; learning and sourced claim | entry, `corpus/README.md`, `corpus/SOURCES.md` | linguistics |
| 52 C (`round-52/claims.json:33-42`) | same | same three | linguistics |
| 53 C (`round-53/claims.json:34-42`) | same | same three | linguistics |
| 54 C (`round-54/claims.json:14-17`, `:103-107`) | same | same three | culture-material |

C's acceptance script is also the direct descendant of round 53's `accept-c.py`. If "surface" means the lands and instrument shape, round 54 is the fourth coverage/new-entry claim in a row. If it means the knowledge partition, it is the first culture-material *entry* in the run, but not the first culture-material *claim*. The lane's PROVINCE lists the six partitions as its areas (`PROVINCE.md:9-11`). It defines no separate frontier-area list (`corpus/README.md:498` "Known gaps (frontier)" lists no areas), so the partition reading is defensible. It is not the only reading.

**Classification:** a tradeoff for the closure, not a defect the round can fix. The declaration is frozen, and narrowing or re-shaping it now would breach `:350`. Criterion 11 instruments with 13/13 controls (`reports/round-54/telemetry/criterion11-controls.txt`) answer the defect class directly. That is stronger evidence of compliance than the change of partition.

**Impacted axes:** coverage (the frontier claim); calibration (the declaration says more than the repo shows).

## Finding 3 — does the prerequisite act as an undeclared claim?

**Not in the measured legs.** `d761ee8` is an ancestor of base `260c68d` (`git merge-base --is-ancestor` exit 0). It adds or removes no knowledge file and does not touch `corpus/README.md`. So SET, SWEEP, FLOOR and RANGE cannot see it. The ACCESS leg's before-PASS already includes the S225 note. Round 53 used the same pattern (`round-53/claims.json:7`, prerequisite `9ae5af9`), and its closure credited that fix in its Gate sample, not as a claim (`round-53-verifier-spotcheck.md:141`). The pattern is accepted precedent.

**Credit risk 1: the census delta.** The start census was run on `e0bfb13`, *before* the prerequisite (`reports/round-54/telemetry/census-start.txt:1`, rows 238). Status totals from the `corpus/SOURCES.md` status column:
- `e0bfb13`: mined 194, queued 35, rejected 9.
- `d761ee8` and `main`: mined 194, queued 34, rejected 10.

So the round-end census will show queued −1 and rejected +1 that come from the prerequisite: S145 mined → rejected, and S185 queued → mined. The mined count stays at 194 only because those two flips cancel. The report's "rows touched old→new" and any mined delta must not credit these to C.

**Credit risk 2: SCORECARD depth.** The prerequisite edits five lines of two linguistics entries: gesture lines 68, 133, 150 and 199, and speech-surrogates line 75. That is depth-repair work committed inside the round. With no depth claim, the SCORECARD depth row and the report's quality evidence must not say depth "improved". Doing so would credit an undeclared claim.

**Credit risk 3: the milestone string.** "Round 54: C masks and masquerade entry 229->230 with sources S239 upward; routed round-53 items" presents the routed items as a second deliverable alongside C. The report must make clear they are records, not claims (`claims.json:7` "Neither commit is a claim").

**Credit risk 4: SOURCES.md is a C land path.** The whole of `corpus/SOURCES.md` is in C's lands (`reports/round-54/separability-manifest.json:9-11`). Any in-round fix of the open registry cells (S135, S141, S147, S151, S159) or the S237 URL would ride on C's land path. A superseding row would also take an id from S239 upward, which is C's export range (`separability-manifest.json:14`). Rows that C's entry does not cite pass C's legs vacuously, so C's legs cannot tell them apart from C's rows.

**Smallest safe correction:** prefer leaving the routed registry cells open and routing them to round 55. If any are fixed in round 54, list each such row id as a record, not a C row, and count them separately from C's rows.

## Wording the report MUST use

Under **Work performed**, first bullet:
> One declared claim, C (coverage; the round's learning claim and sourced claim). The contract allows one to three claims and prefers two (`.ufo/prompts/kotodama-round-54.md:11`, `:349`). This round declares one. The declaration's reason (`reports/round-54/claims.json:8`) is incomplete. It names only linguistics depth repair and work that depends on C as second-claim candidates, and it leaves out independent candidates on other axes, such as a SHONEN/SCORECARD calibration count. Several round-53 routed items are not landed by the prerequisite (below).

Under **Work performed**, a separate bullet for the prerequisite:
> Prerequisite `d761ee825f94f7ae45e098ad551d7f735645ad22` (not a claim; measured by no counting command). It lands round-53 closure routed items 2 (gesture lines 68, 133, 150, 199) and 6 (lessons index row), plus the line-75 sub-item of item 4 (S185 cited, S145 mined → rejected, S185 queued → mined) and the S225 sub-item of item 3 (access note). Still open at the declaration: item 3's Gate splits (S200, S205, S214, S224, S236) and S237 URL; item 4's line 79 ("Oaxaca", "single-clause") and registry cells S135, S141, S147, S151, S159; item 5 (dead-seat error texts with the round-53 wave files). [Then state, per item, what this round did with it, citing the commit or lesson line, or "routed to round 55".]

Under **Before → after measurements**:
> C only: `python3 -B reports/round-54/accept-c.py`, measured from `260c68d58c5d3c2b9a6463ca5c667b7e0fff5987` (which already contains the prerequisite) to <landed hash>. No before→after is claimed for the prerequisite.

Under **Sources & frontier**:
> The start census ran on `e0bfb13` (before the prerequisite; `reports/round-54/telemetry/census-start.txt:1`). Of the round's status changes, S145 mined → rejected and S185 queued → mined (queued −1, rejected +1, mined net 0) are the prerequisite's, not C's. C's rows are S239 to S<n>: <k> rows, all mined. [List any other row written this round by id, as a record.]

Frontier-area sentence (in **Work performed** or **Trend verdicts / discernment**):
> The drift sentinel (`round-53-verifier-spotcheck.md:168`) asks for a different frontier area. C's entry is in `culture-material/`, where the round-51 to 53 entries were in `linguistics/`. Round 51's D also worked culture-material (`pastoralism-animal-husbandry.md`), and C is the fourth coverage new-entry claim in a row with the same lands. Under the partition reading the area differs; under the axis-and-surface reading it does not. The lane's direct answer to the tripping defect class is QUALITY criterion 11 (controls receipt 13/13). Whether the sentinel is satisfied is the closure's ruling.

SCORECARD and trend wording:
> depth: unchanged (no depth claim; the prerequisite's five corrected entry lines are routed repairs, not a claim).

Do not say "quality: improved" on the strength of the prerequisite alone. If it is cited, say "routed repairs landed as an unclaimed prerequisite".

The report MUST NOT say any of the following:
- "rounds 51 to 53 worked linguistics" (round 51's D was culture-material);
- "the routed fixes are landed" or "all routed items fixed" (items 3, 4 and 5 are partly or wholly open at `5757c45`);
- "no cheap independent second claim exists";
- that the sentinel "is satisfied" or "cleared" as a fact.

## Unrun checks

- I did not run `accept-c.py`, `dry-run.py`, `claims-agree.py` or the separability command. That is for the executor seats and the L1.
- I did not re-open the sources of the open routed items. Seats ReviewGateSplits and ScoutS225Recheck own that.
- I did not judge whether a calibration second claim would have been cheap enough. Its existence is the counterexample; its cost is not measured.
- I could not find the text of the "at least one learning claim" rule in the fleet-root `MISSION.md`, `AXES.md`, `CORPUS.md` or `LEARNING.md` (a `learning claim` grep found nothing). C labels itself a learning claim (`claims.json:17`), so the rule is met as the assignment states it.
