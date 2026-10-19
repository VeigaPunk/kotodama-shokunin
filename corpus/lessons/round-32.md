# Round 32 — lessons gate-keeper: a landing is its diff, not its draft; a falsifier is its first re-execution

source: `reports/round-32/{claims.json,targets.json}` and the wave artifacts that arrived mid-window (`reports/round-32/{completion-audit.md,completion-ledger.json,run-validation.py,scope.md,sweep-audit.py,sweep-audit-O09.json,sweep-audit-O09O10.json,sweep-audit-O10.json,sweep/run-sweep.py,dossier-d11-shonen-boxes.md,dossier-d12-capability-inventory.md,telemetry/*}`); `reports/round-31/{closure-ledger.json,jinii/draft.md,jinii/patch-draft.md}`; `AGENTS.md`; `SKILL.md`; `LOG.md` (round-31 admission tail); `corpus/lessons/README.md` and the r26–r31 lessons; git objects `17e90b9`, `4d50050`, `e06581b`, `fc13cd2`.

verified-at: read-only gate review **2026-10-19T00:36Z–00:40Z**, lane HEAD `4d500501a286d96f2eea8a6188c649255581301a`, declared baseline `17e90b9047b289d7a63180a1dc1bebb074137e29` (HEAD's parent; equals `claims.json` `baseline_revision`). This is a moving tree — the r32 wave's artifacts landed while this seat worked (§Arrivals); every reading carries its own stamp and later readings are new dated sections, never substitutions.

recheck: (1) ledger digest + verdict multiset, `json.loads` + `hashlib.sha256` over `reports/round-31/closure-ledger.json` (§C); (2) `git show 17e90b9 -- AGENTS.md SKILL.md` — the two landing hunks (§Landing); (3) `sed -n '40,42p' AGENTS.md` against `reports/round-31/jinii/draft.md:35,37` (F-X16-1); (4) the `SKILL.md:715` audit command verbatim — prints 5 (F-X16-3); (5) recompute each closing snapshot's `closes_sha256` (§Falsifier); (6) the lessons census and index parse (§Ledger).

scope: SCRIBE X16 writes only `corpus/lessons/round-32.md`. The path was absent before this write. Read-only probes (`python3 -B`, `git show`/`log -S`, `sed`, `sha256sum`, `wc`); no scratch artifact was written (all heredocs via stdin, `PYTHONDONTWRITEBYTECODE=1`); no mirror-safety leg launched by this seat (the in-round evidence is `reports/round-32/telemetry/controls-vartmp.json`); the round's counting command `python3 reports/round-32/run-validation.py` was **not** run by this seat (validator-owned). Filed rounds 8–31, filed lessons, the lessons index, and the AGENTS/SKILL/LOG bytes are read-only here: every finding below routes as a new recorded change, never an in-place edit. No commit, no push. All fictional systems remain NON-CANON; lore owns canon.

## Gate

Axes: **C / calibration** (the completion-criterion audit), **O / operability** (the r32 final sweep), **D / depth** (the final dossier) — conjunctive, and mid-landing at this seat's stamps. This file is the lessons gate record, not the round verdict.

### Rule

**A regimen ends by the rule it ran on: the last artifact gets the first audit.** A landing is its diff, not its draft — verifying an anchor verifies nothing about what else rides the same commit. A falsifier is its first post-landing execution, not its pre-landing design — a condition that can fire for an instrumental reason is not a falsifier until someone shows it also fires on substance. Close the regimen the way every round was closed: re-execute the commands against the bytes that landed.

## C — the closure ledger reproduces byte-identical at the regimen's close

At **00:36Z**, digest over `reports/round-31/closure-ledger.json` = `b9a66c2dbf092bb58788ae3025b7d62e5118371106e00feccc72efc768988ca7` — equal to the pin in `corpus/lessons/round-31.md` §C: **the ledger is unedited since its filing**. Re-derived from the rows: `rounds_8_31` = **24**; verdict multiset **18 closed-admitted / 3 closed-rejected (11, 17, 22) / 1 skipped-operator (13) / 1 closed-with-finding (23) / 1 in-flight (31)**; `report_exists` = `commit_ancestry_ok` = **22/22** (24 minus r13's no-report-owed minus r31 in-flight at audit time); `rounds_1_7` = **7/7 reconfirmed**; `round_32` = `pending-by-construction`; findings `F-C31-1` (r23) and `F-C31-2` (r13). Matches `LOG.md`'s round-31 admission row ("32/32 lane rounds audited" = 7 retro + 24 + the r32 slot).

**One prose hazard recorded, not repaired.** The ledger's own `claim_C_verdict.statement` partitions its rounds as "19 admitted, 3 rejected, 1 operator-skipped, 1 closed-with-finding" over "rounds 8-30" while separately noting r31 in-flight — a sum of 24 over a 23-round domain (or r23 counted twice). The row-level multiset above is the binding one; the prose carries the same force-reconciliation hazard `corpus/lessons/round-31.md` §C named ("three partitions of 18 admitted"), now fossilized inside the ledger's verdict field. The r32 C seat inherits this: read the rows, not the sentence.

Boundary carried (Q-31-4): the ledger's evidence commands are fleet-root-relative; this re-derivation is structural (`json`) at the lane root — command-level falsification still starts at `/home/vgpnk/Projects/shokunin`.

## The landing audit — what `17e90b9` actually carried

The r31 admit commit's hunks (`git show 17e90b9 -- AGENTS.md SKILL.md`, read **00:38Z**):

- **The verified anchor was honored.** The AGENTS hunk `@@ -29,3 +29,14 @@` appends the M1 "Close what you open" rule after old line 31 — exactly the correction Q-31-1 filed before landing. The rule now stands at `AGENTS.md:32-39` (file = 42 lines, `wc -l`).
- **F-X16-1 — patch scaffold rode the same hunk.** The same commit appended `AGENTS.md:40-42`: a dangling ` ``` ` fence (:40 — in `reports/round-31/jinii/draft.md:35` it closes the quoted block; appended to AGENTS.md it opens one that never closes), a blank (:41), and :42 verbatim `draft.md:37` ("### 2.2 `SKILL.md` — append one item … (after :534)") — the draft's landing-checklist heading, not an operating rule. Three lines of the patch's own scaffold landed inside the patched file.
- **F-X16-2 — the SKILL row missed its verified anchor by 179 lines.** `corpus/lessons/round-31.md` verified "`:534` is the checklist's last content line … the draft's SKILL anchor 'append after :534' is **correct**." The landing's single SKILL hunk `@@ -710,3 +710,6 @@` appends the checklist item at `SKILL.md:713-715` — end of file, inside the `## Source-bounded culture drill — D3 (round 7)` section (heading `:660`) — while `## Checklist (executable where a tool exists)` remains `:522-534`. The item exists; the section it was verified against does not contain it.
- **F-X16-4 — the draft's second leg did not land, and the round record says so honestly.** `patch-draft.md` §1 promises "the consistency erratum to the one evidence cell the census falsified" (the `SKILL.md:294`-class cell). The landing's SKILL diff has no hunk before `:710`, and the cell's "round-24 cold run" text dates to `e06581b` (`git log -S'round-24 cold run' -- SKILL.md`) — pre-r31. The LOG delta paragraph lists exactly what landed (AGENTS bullet, SKILL checklist item, five closing snapshots) and claims no erratum: the record is honest; the draft over-promised. Draft-vs-landing delta, owner parent.

## The falsifier legs — substance 5/5, instrument false-fires on day one

Executed **00:36Z**:

- **Integrity leg passes.** Recomputed `sha256` of each record named by the five retroactive closing snapshots — `reports/round-{19,25,26,27,28}/telemetry/availability-close-N.json` → `closes_sha256` matches the record's live bytes **5/5**.
- **F-X16-3 — the landed audit false-fires.** The `SKILL.md:715` audit, verbatim, prints **5 records** (`reports/round-{19,25,26,27,28}/availability.json` — all admitted rounds): it requires a file literally named `telemetry/closing-snapshot.json`, but the landed snapshots are named `telemetry/availability-close-N.json`. Every record it names IS closed; the instrument cannot see the closures. The draft's audit (`draft.md` §2.2) had the opposite defect — no closure check at all, so it would print the same five forever; the landing fixed the semantics and broke the path. `LOG.md`'s recorded falsification clause (i) — "if the checklist audit prints a non-empty list after this round for a round admitted to LOG.md, the rule is falsified and reverts" — has therefore **fired on day one for an instrumental reason**, while the substantive form of the same check (for each `open-at-seat-close` record, a snapshot in that round's `telemetry/` whose `closes_record` names it and whose `closes_sha256` matches) passes 5/5. Disposition belongs to parent/operator: re-key the audit to the landed convention or reword the clause — a new recorded change; this lesson does not edit the rule it audits.

## The lessons ledger at regimen close — the debt the regimen leaves its reader

Census at **00:36Z** (`len([p for p in Path('corpus/lessons').glob('*.md') if p.name != 'README.md'])`): **31**; this write makes **32** — a predicted denominator change, not an index repair. The index (`corpus/lessons/README.md`, last touched `fc13cd2`, round 25) carries **27 data rows**: 26 naming `corpus/lessons/*.md` paths (25 non-README files + the self-row, matching its rows==files==26 under path-counting) plus the round-13 absence row. **6 filed lessons sit outside it — rounds 26–31 — and this file makes 7.** Q-30-2 / Q-31-3 carried: rows are parent-owned additions, never edits. Pins measured now for the missing rows (`bytes/lines/sha8`): round-26 `60054/222/cae06660`; round-27 `54972/203/f15e285b`; round-28 `50419/145/dd832ff7`; round-29 `17847/118/b6765d33`; round-30 `30665/181/56e77835`; round-31 `16637/73/8870bbdd`.

The arc those 32 files record, in one breath: measure, don't declare (r4); a pin binds bytes, not intentions (r22); a close-out closes only what a recorded command can re-open (r31) — and the regimen's own closing artifacts obey none of it automatically. They earned obedience the only way anything in this lane ever did: by being re-executed. That is what this file is.

## Dated integration observation — the r32 wave arrives, 2026-10-19T00:38Z–00:40Z

At **00:38Z** `reports/round-32/` held **18 files**; at **00:40Z**, **21**: arrived in-window were `completion-audit.md` (sha8 `b5fb8942acba`), `completion-ledger.json` (`33362e8c0f9d`), `run-validation.py` (`1809eb6b28eb`), `scope.md`, `sweep-audit.py` + three `sweep-audit-O*.json`, `sweep/run-sweep.py`, `dossier-d11-shonen-boxes.md`, `dossier-d12-capability-inventory.md`, and 7 telemetry files (including `controls-vartmp.json`, the mirror leg's in-round evidence). Still absent at **00:40Z**: `final-dossier.md` (the D assembly), `final-sweep.md` + its sweep receipt (the O artifact), and the round's `validation.json`. Opening readings only — the round verdict belongs to the validator seat and the integrating parent, not to this file. What the gate adds to their reading: the C audit inherits a ledger that reproduces unchanged (§C, including the prose-partition hazard), and the O sweep inherits r31's narrowed remainder (Q-31-2): the sweep manifest must derive from the SCORECARD surface, not restate it.

## Open routes

- **Q-32-1 — parent/operator / falsifier disposition (F-X16-3):** the recorded falsification condition (i) has fired instrumentally; re-key the `SKILL.md:715` audit to the landed snapshot convention (`closes_record` + `closes_sha256`) or reword the clause — new recorded change, never in-place.
- **Q-32-2 — parent / AGENTS residue (F-X16-1):** excise `AGENTS.md:40-42` as a logged change; the bytes are `draft.md:35,37` residue, not rules.
- **Q-32-3 — parent / checklist position (F-X16-2):** the executable item at `SKILL.md:713-715` sits outside `## Checklist` (`:522-534`); move it or cross-reference it — a logged change either way.
- **Q-32-4 — parent / draft-vs-landing (F-X16-4):** the `patch-draft.md` erratum leg (the `SKILL.md:294`-class cell) never landed; the cell carries its own r24-era dated provenance; disposition optional, record kept.
- **Q-32-5 — parent / lesson indexing:** Q-30-2/Q-31-3 carried — 7 unindexed lessons (r26–r32); add parent-owned rows using the §Ledger pins.
- **Q-32-6 — r32 validator / inherited remainders:** Q-31-2's narrowed remainder (manifest derives from the SCORECARD surface) and Q-31-4's boundary (ledger commands run from the fleet root) transfer to this round's C/O reading; read the ledger's rows, not its verdict prose (§C).

## Boundary record

Writes: `corpus/lessons/round-32.md` only. No scratch artifact, no mirror-safety leg, no validator or receipt writer invoked. No filed round, lesson, index, AGENTS/SKILL/LOG byte, tool, or gate touched. No commit, no push. Opening status: the C ledger is gate-verified above; O's and D's round artifacts were absent at 00:40Z; this section grants no round admission, no sweep acceptance, no promotion.

Lesson filed by SCRIBE X16, round 32. Corrections and post-landing observations are new dated sections or successor files, never silent rewrites of the readings above.
