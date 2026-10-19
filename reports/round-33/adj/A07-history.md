- Seat: A07 | executor | claim A (adjacency) | date 2026-10-19 | baseline 139e3b6

# A07 — adjacency history consistency: r21/r29 filed commands re-run at HEAD

**Mission (binding):** re-run 2-3 filed commands from the r21/r29 adjacency audits and confirm their filed verdicts still hold at HEAD.

**Revision under test:** `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb` at `2026-10-19T03:53:42Z`, equal to the declared round-33 baseline; `git ls-files | wc -l` → `2655`, matching the claims.json tracked-path baseline. Working tree at run time carried only round-33 in-flight paths (`M LOG.md`, `?? REGIMEN.md`, `?? reports/round-33/`).

**Method:** each filed command was re-executed verbatim at HEAD with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. Filed round bytes were read only, never edited. Where a filed verdict is a *count* rather than a pass/fail, the count's revision of origin was reconstructed by archiving the audit-time tree (`git archive 8115eaaeb57c9dce157fe291337cb52dd914c6cf | tar -x -C .scratch/r21-tree`) and re-running the same command inside that archive. Eleven filed checks were re-run: the three primary r21/r29 commands, plus eight supporting checks that the same audits filed as evidence. Every receipt is quoted below as emitted.

## Re-run results

| # | filed command and source | filed verdict | HEAD verdict | disposition |
|---|---|---|---|---|
| 1 | `python3 -B tools/assemble-d4-typed.py --selftest` — `reports/round-21/adjacency/province.md:11` | 12/12 checks passed | `selftest: 12/12 checks passed — build/determinism/--check/tamper plus stale-projection, coverage-gap and malformed-packet controls; no file outside the temporary mirror touched`; exit 0 | **holds exactly** |
| 2 | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` — `reports/round-21/adjacency/province.md:11` | 19/19 legs passed | `summary: 20/20 legs passed`; exit 0 | **pass verdict holds; leg count superseded 19→20** — D1 |
| 3 | RGL ID + index-row + disclaimer extraction block — `reports/round-29/adjacency/A09-A12-handoff.md` §Measured commands (block at `:30-46`) | both surfaces `5` unique `RGL-01..05`; one index row per entry; disclaimers true | `examples/culture-d4/components/13-register-law.yml: ids=[RGL-01..RGL-05] count=5 unique=5`; `examples/culture-d4/packet.d4.yml: ids=[...] count=5 unique=5`; `index register-strata-attestation.md: rows=1`; `index register-lexicon-ceilings.md: rows=1`; both entries `noncanon=True canon_boundary=True`; `law disclaimers: component_no_real_world_rights=True; packet_noncanon=True` | **holds exactly, field for field** |
| 4 | `sha256sum PROVINCE.md AGENTS.md corpus/knowledge/synthesis/worldbible-integration-contract.md` — `reports/round-29/adjacency/province-entries.md:15` | `05b34a57…`, `be3a9477…`, `5f4c02bf…` | `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` (match), `1afaf106f20b440ad263ab231c215773436c7f42ab106848f5550b87ecf41035` (**no match**), `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` (match) | **2 of 3 hold; AGENTS.md component superseded** — D2 |
| 5 | `git diff --quiet -- PROVINCE.md` + `git rev-parse HEAD:PROVINCE.md` — `reports/round-21/adjacency/province.md:17` | exit 0; blob `313b182f251564b7997b06996b4f063370778f11` | exit 0; blob `313b182f251564b7997b06996b4f063370778f11` | **holds exactly** (PROVINCE byte-identical r21→HEAD) |
| 6 | ledger census block — `reports/round-29/adjacency/A09-A12-handoff.md` §Final ledger census (block at `:128-137`) | `ledger_paths=6 entries=2 rows=0 audits=4 bleed=0 unfiled_bleed=0 filed_non_bleed_findings=1 sweep_dispositions=4` | same string, character for character; all boundary/filing/disposition assertions passed; exit 0 | **holds exactly** |
| 7 | `python3 -B reports/round-28/audit/entry-audit.py --json --new … --new …` — `reports/round-29/adjacency/province-entries.md:31` | exit 0; `entries=201`, `index_failing=[]`, `bar_failing_count=184` | exit 0; `entries = 201`, `index_failing = []`, `bar_failing_count = 184`; empty stderr | **holds exactly** |
| 8 | `python3 -B reports/round-28/audit/x63-entry-source-resolvability.py --offline --json --baseline 6c0ac44…` — `reports/round-29/adjacency/province-entries.md:42` | exit 1 with four non-reproducing sweeps; 25/0 and 46/0 locators; 2 and 3 URLs not attempted offline; 4 pins re-derived; amendment 313 preserved / 123 inserted / 0 rewritten | exit 1; `findings count= 4` (1 `sweep-authoring-defect` + 3 `sweep-sibling-landing`); ceilings `resolved=25 unresolved=0 urls=2`; strata `resolved=46 unresolved=0 urls=3 pins=4`; strata `amendment = {baseline_lines: 313, live_lines: 436, preserved: 313, inserted: 123, deleted_or_rewritten: 0, append_only: true}`; 10 sweeps, 6 `reproduces`, 4 classified | **holds exactly, every number** |
| 9 | four-sweep absence reconstruction block — `reports/round-29/adjacency/A09-A12-handoff.md` §Reconstructed quoted absence sweeps (block at `:63-92`) | 1 authoring defect + 3 sibling landings; current line hits 315 / 106+399 / 125 / 4,9,17 | output byte-identical to the filed block, including every line number: `RLC lexicon ceiling: baseline={}; current={'…register-strata-attestation.md': [315]}`; `RLC which semantic fields: baseline={'…sound-symbolism.md': [106]}; current={'…sound-symbolism.md': [106], '…register-strata-attestation.md': [399]}`; `RSA attestation register\|attestation speech: … [125]`; `RSA register law\|register-law: … [4, 9, 17]` | **holds exactly, byte-identical** |
| 10 | r21 inventory census block — `reports/round-21/adjacency/entries.md` §Inventory evidence | `R19 corpus: 10 10`, `R19 author fragments: 10 10`, `R20 author fragments: 4 4` | `R19 corpus: 10 10`, `R19 author fragments: 10 10`, `R20 author fragments: 4 4`; exit 0 | **holds exactly** |
| 11 | cited locator `corpus/README.md:138-139` — `reports/round-29/adjacency/A09-A12-handoff.md:18` | one filename row per entry at those lines | `138:- \`register-lexicon-ceilings.md\` — …`, `139:- \`register-strata-attestation.md\` — …` | **holds exactly** |

Net: **9 of 11 filed verdicts hold exactly at HEAD; 2 are partially superseded, both by later filed rounds, neither by drift.** No filed verdict was found false as filed.

## D1 — r21 gate leg count 19 → 20, explained by a later filed round

- At the r21 audit revision `8115eaa`, the same command inside the archived tree emits `summary: 19/19 legs passed`, exit 0, with `grep -c '^ok '` → `19`. The r21 filed number is therefore exact for its revision.
- At HEAD the same command emits `summary: 20/20 legs passed`, exit 0. The extra leg is `L3b-argot`; `git log --oneline -S'L3b-argot' -- tools/gates/typed-pipeline-gate.py` → `fc13cd2` (the round-25 round commit, which also rewrote `tools/gates/typed-pipeline-gate.py` by 295 lines and filed `reports/round-25/validation.json`).
- **Disposition: superseded, not false.** The r21 verdict's substance — the gate runs green on the D4 packet and every registered leg passes — still holds; the count is a moving quantity that a later filed round deliberately advanced. No correction is owed to the r21 record, which is append-only and correct for its revision.

## D2 — r29's three-file pin check: 2 of 3 still hold; AGENTS.md superseded by filed rounds 30 and 31

- `git diff --quiet -- PROVINCE.md` still exits 0 and the blob is still `313b182f251564b7997b06996b4f063370778f11` — the same blob the r21 audit filed at `province.md:17`. `sha256sum PROVINCE.md` still returns `05b34a57…` and the world-bible contract still returns `5f4c02bf…`, the same digests the r29 audit filed at `province-entries.md:15`.
- `AGENTS.md` is the exception. Filed digest `be3a9477ed28ba401352ebce7c182d529223e552d0dba0d75f3b97b956be2c8b`; HEAD digest `1afaf106f20b440ad263ab231c215773436c7f42ab106848f5550b87ecf41035`. The r29 command `git diff --name-status 3b13a2f2821ed6f8ac1217842ab6830d592c7935 -- PROVINCE.md AGENTS.md corpus/knowledge/synthesis/worldbible-integration-contract.md` returned **no paths** as filed; at HEAD it returns `M	AGENTS.md`.
- Cause is two later filed rounds, not unreported edit: `git log --oneline 3b13a2f2821ed6f8ac1217842ab6830d592c7935..HEAD -- AGENTS.md` → `17e90b9` (round-31) and `11df1fd` (round-30); `git diff --stat` over that range → `AGENTS.md | 29 +++`, 29 insertions, 0 deletions. `11df1fd` adds the 18-line `## Availability and dispatch telemetry` section; `17e90b9` adds the 11-line `Close what you open` bullet plus the two stray lines in F1.
- **Disposition: the r29 scope verdict holds; its AGENTS.md pin component is superseded.** The r29 sentence under test — "The Province, local instructions, and contract therefore remain unchanged from the declared round-29 baseline in this check" (`province-entries.md:15`) — remains true for `PROVINCE.md` and the contract and is now false for `AGENTS.md`. Because the amendments are filed by two rounds that ran after r29, this is a dated supersession with named provenance, **not** unfiled bleed and **not** province drift. No correction to the r29 record is proposed; a future audit should cite the current digest with its round attribution rather than the r29 pair.

## D3 — the r21 filed *finding* `A21-D4-XF-01` no longer reproduces its cited evidence (currency read)

A filed *command* reproduces a filed *value*; a filed *finding* can be superseded by a later round without its filing row changing, because the row is append-only. I therefore paired every re-run above with a currency read of the finding it supports, and this is the one that moved.

`reports/round-21/adjacency/ledger.json` files `A21-D4-XF-01` (`path: examples/culture-d4/typed-labels.d4.yml`, `bleed: true`, `filed: true`, `severity: material fixture-boundary defect`) on evidence `examples/culture-d4/typed-labels.d4.yml:28,329,335-649,853-966` plus `tools/d2-typed-labels.py:925-1104`. At HEAD:

- **The cited coordinates no longer carry D2.** `:28` reads `"canon": "not canonized (D4 design drill); derived view of examples/culture-d4/packet.d4.yml"`; `:329` reads `"E2"`. Neither is D2 metadata. The cited rank block now carries D4-local records (`:335-340` → `RK-01#g`, jurisdiction "the forge and the furnace yard", source `examples/culture-d4/components/09-costumes.yml`, `LEX-GAR-02`).
- **The bleed-accounting fields are empty.** `:605-611` → `"quarantine": []`, `"residuals": []`, `"unresolved": []`, with a single `skipped` leg whose `why` reads `"packet-native rank rules only; no foreign fixture data is imported"` — a negative statement, i.e. evidence of the boundary being enforced.
- **The 26 remaining `D2` tokens are not D2 domain data.** 24 of them (`:211-290`) are the typed-labels tool's own finding code `D2L-FORM-UNRESOLVED`, defined in the shared projector's `FINDING_CLASSES` (`tools/d2-typed-labels.py:419,422`) and present in the D4 pipeline's own expected hold set (`examples/culture-d4/expected-holds.json:53,59,65`); one (`:165`) is a skip note stating the D2 leg's file is *not* read for family d4; one (`:607`) is the residual-accounting leg name quoted above.
- **The digests moved.** Live `sha256sum examples/culture-d4/typed-labels.d4.yml` = `c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e`, against the r22 analysis baseline `cbcf997f5f38fac89b0fb1b6a6841ec42c9041a2599df44083ddefc5c22cfb4f` (`reports/round-22/bleed/analysis.md:16`); `tools/d2-typed-labels.py` live `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` against the same r22 baseline `76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb`.
- **The repair is filed, not silent.** `reports/round-24/box4-bleed.md:105-118` accounts the full tail and states it was implemented in the round-22 window at commit `0e81d9d` per an append-only correction (`LOG.md:3312-3324`), with the family-clean projection rule landing in the skill in round 23. `reports/round-29/validation.json:82` records that the finding "remains outside this slice".

**Disposition: superseded by a filed repair.** The r21 row is correct for its revision and stays as filed; it must not be re-read as a live bleed at HEAD. Consumers (including the round-33 audit's bleed section) should cite `A21-D4-XF-01` as **repaired, coordinates and digests stale**, and should not quote its `bleed: true` field as current. This matches, and independently re-measures, the currency caution filed by A13 at `reports/round-33/adj/A13-verify-a07-a09.md` §Findings F3.

## Cross-check against A13's independent A07-class re-run

`reports/round-33/adj/A13-verify-a07-a09.md` executed the A07 check class independently at 2026-10-19T03:52:59Z–03:55:05Z, before this fragment existed, and filed five re-runs (its items 1–5). All five agree with my runs, which were made independently and slightly later: its item 1 = my check 10 (r21 inventory census, identical three lines); its item 2 = my check 4's `PROVINCE.md` component (the same `05b34a57…` digest, filed at r21 `entries.md:4`); its item 3 = my checks 4 + 5 combined (the r29 pair: `git diff --quiet` exit 0 plus the same digest, filed at `A09-A12-handoff.md:20`); its item 4 = my check 6; its item 5 = my check 9. **No conflict.** My fragment adds seven checks A13 did not run (checks 1, 2, 3, 4, 7, 8, 11 — the D4 tool pair, the RGL/index extraction, the three-file digest pair, `entry-audit.py`, `x63`, and the README locator), the D1 leg-count reconstruction, the D2 attribution, and the D3 currency read. A13's pointer corrections to `adj/A10-receipt.md` rows (A07(1) identity claim, A07(2) `province.md:17`) concern A10's receipt, not this fragment, and this fragment cites `province.md:17` for the blob as A13 confirms.

## F1 — named finding: orphan drafting fragment live in `AGENTS.md` (route, do not absorb)

`AGENTS.md` is 42 lines and contains exactly one fence-marked line, `AGENTS.md:40` (```` ``` ````), with no matching opener, followed at `AGENTS.md:42` by:

```
### 2.2 `SKILL.md` — append one item to "## Checklist (executable where a tool exists)" (after :534)
```

Both lines were introduced by the round-31 commit `17e90b9` (`git show 17e90b9 -- AGENTS.md`, trailing hunk). This reads as leaked drafting text for a `SKILL.md` edit that was never applied as a heading, sitting in a live instruction file that every seat in this fleet reads. It is inside filed bytes, so it is not unfiled bleed; it is a defect in a filed file.

- **Owner:** the round-31 integrating parent who landed `17e90b9`; operator-visible, since `AGENTS.md` is fleet instruction surface.
- **Not mine to fix:** my write scope is this fragment only; `AGENTS.md` is outside `reports/round-33/`. Recorded here for the round-33 audit's findings table and for routing, not absorbed.
- **Bounded fix draft (for the integrator, if the operator wants it):** delete `AGENTS.md:40` (the unmatched fence) and `AGENTS.md:42` (the orphan heading), keeping `:41` as the file's trailing blank or dropping it; the substantive round-30/31 telemetry rules at `:13-39` are unaffected and stay. Verification after application: `grep -c '^```' AGENTS.md` → 0 and `wc -l AGENTS.md` → 40.

## F2 — live carry-forward: r29's `A29-ADJ-EVID-01` is still uncorrected at HEAD

The r29 audit filed one non-bleed evidence defect: the quoted absence sweep `which semantic fields` in `corpus/knowledge/linguistics/register-lexicon-ceilings.md:4` was already contradicted at the round-28 baseline by `sound-symbolism.md:106`, and r29 routed an append-only correction to the entry owner / round 30 (`reports/round-29/adjacency/A09-A12-handoff.md`, §Reconstructed quoted absence sweeps and §Disposition and limits). At HEAD the condition is unchanged: my re-run of that exact block (check 9) and the x63 re-run (check 8, `kind: sweep-authoring-defect`, `baseline_hits: [corpus/knowledge/linguistics/sound-symbolism.md]`) both still classify it as an authoring defect, and the entry's sha256 is `bb579d51cea0a900571e77b6690978256a607ec08f500923674738107dc1bffe` at 289 lines with no append-only amendment recorded. No correction landed in rounds 30–32. **This remains a live, owned, uncorrected evidence defect carried into round 33** — recorded here so the consolidated audit does not read r29's "holds exactly" reproduction as its correction.

## Limits

- This is a history-consistency check on filed commands, not a re-audit of the r21/r29 conclusions. Where a re-run reproduced the filed numbers (checks 1, 3, 5–11) that confirms *reproducibility at HEAD*, not the audits' province reasoning.
- Checks 4, 6, 9, 10 read filed bytes or the live corpus read-only; no filed artifact was modified. All scratch output landed under `.scratch/` only.
- The gate leg-count delta (D1) was reconstructed by running an archived copy of the r21 tree; that copy lives at `.scratch/r21-tree` and is disposable.
- Every re-run above is paired with a currency read of the finding it supports (D3), because a filed command reproduces a filed value while a filed finding can be superseded by a later round with its filing row unchanged. Two of the three findings in scope had moved or were still live; only `A21-D4-XF-01` was repaired.
- This is a point reading at HEAD `139e3b6`. Rounds 33's own integration happens after it, so the D2 and D3 digests must be re-measured if the integrator touches the paths they cover.
- No promotion, canon, rights, or round-acceptance judgement is made or implied anywhere in this fragment.

## Owed: none

No dependency fragment was named by this mission; nothing is owed to another seat. The three items below are *routed*, not owed to a missing seat:

- F1 (`AGENTS.md:40,42` orphan fragment + unmatched fence) — owner: round-31 integrating parent; route via the round-33 audit findings table.
- F2 (`A29-ADJ-EVID-01`, `register-lexicon-ceilings.md:4` false-at-authoring absence claim) — owner: the entry owner / a round that lands an append-only corpus correction; route via the round-33 audit.
- D3 (`A21-D4-XF-01` is repaired; its filed `bleed: true` field and cited coordinates are stale) — owner: none needed for repair; the *routing* action is a consumer caution for the round-33 audit's bleed section and for any seat quoting the r21 ledger row as current. No edit to `reports/round-21/**` is proposed or permitted.

## Citations

Paths (all under the lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`):

- `reports/round-21/adjacency/province.md:11` — filed `assemble-d4-typed.py --selftest` 12/12 and `typed-pipeline-gate.py` 19/19 verdicts (checks 1, 2).
- `reports/round-21/adjacency/province.md:17` — filed `git diff --quiet -- PROVINCE.md` exit 0 and blob `313b182f…` (check 5).
- `reports/round-21/adjacency/entries.md` §Inventory evidence — filed r21 census block (check 10).
- `reports/round-29/adjacency/province-entries.md:15` — filed three-file digest pair and `git diff --name-status 3b13a2f…` no-paths verdict (checks 4, D2).
- `reports/round-29/adjacency/province-entries.md:31` — filed `entry-audit.py --json` command (check 7).
- `reports/round-29/adjacency/province-entries.md:42` — filed x63 offline command and its four-sweep classification (check 8).
- `reports/round-29/adjacency/A09-A12-handoff.md:18` — cited `corpus/README.md:138-139` index rows (check 11).
- `reports/round-29/adjacency/A09-A12-handoff.md:20` — filed `PROVINCE.md` sha256 `05b34a57…` (checks 4, 5).
- `reports/round-29/adjacency/A09-A12-handoff.md:30-46` — RGL/index/disclaimer extraction block (check 3).
- `reports/round-29/adjacency/A09-A12-handoff.md:63-92` — four-sweep absence reconstruction block (check 9).
- `reports/round-29/adjacency/A09-A12-handoff.md:128-137,142` — ledger census block and its filed output string (check 6).
- `reports/round-29/adjacency/ledger.json` — sha256 `d3a4f2ef19db61acc87d75f0836600239878d76fe614182b120b03c69a4806bd`; census target (check 6).
- `AGENTS.md:40,42` — unmatched fence and orphan `### 2.2 SKILL.md …` heading (F1); `AGENTS.md:13-39` — the round-30/31 telemetry rules.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:4` — the `which semantic fields` absence claim (F2, check 9); entry sha256 `bb579d51…`, 289 lines.
- `corpus/knowledge/linguistics/sound-symbolism.md:106` — the baseline contradicting hit (F2, checks 8, 9).
- `corpus/README.md:138-139` — index rows (check 11).
- `reports/round-33/claims.json` — claim A text, `before.state` tracked-path baseline 2655 at `139e3b6`.
- `reports/round-21/adjacency/ledger.json` — `A21-D4-XF-01` row: `path: examples/culture-d4/typed-labels.d4.yml`, `bleed: true`, `filed: true`, `severity: material fixture-boundary defect`, evidence `:28,329,335-649,853-966` plus `tools/d2-typed-labels.py:925-1104` (D3).
- `examples/culture-d4/typed-labels.d4.yml:28,329` — live text no longer carries D2 metadata; `:165,211-290,607` — the 26 remaining `D2` tokens (skip note, `D2L-FORM-UNRESOLVED` code, residual leg name); `:605-611` — `quarantine/residuals/unresolved` all empty (D3).
- `tools/d2-typed-labels.py:419,422` — `FINDING_CLASSES` / `D2L_FORM` definitions showing `D2L-FORM-UNRESOLVED` is the shared projector's finding code, not D2 domain data (D3).
- `examples/culture-d4/expected-holds.json:53,59,65` — the D4 pipeline's own expected hold set carrying that code (D3).
- `reports/round-22/bleed/analysis.md:9-16` — r22 baselines `cbcf997f…` (projection) and `76536a92…` (tool) against which both live digests have moved (D3).
- `reports/round-24/box4-bleed.md:105-118` — the filed accounting of the D2→D4 bleed tail, implemented in the round-22 window at commit `0e81d9d` per an append-only correction (`LOG.md:3312-3324`) (D3).
- `reports/round-29/validation.json:82` — records that `A21-D4-XF-01` remained outside the r29 slice (D3).
- `reports/round-33/adj/A13-verify-a07-a09.md` §Findings F3 and §A07 class — independent A07-class re-run and the currency caution this fragment re-measures (cross-check).

Commands (each re-run 2026-10-19, stamped `2026-10-19T03:53:42Z`–`03:58:52Z`, all with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `git rev-parse HEAD`; `git ls-files | wc -l` → `139e3b6…`, `2655`.
- `python3 -B tools/assemble-d4-typed.py --selftest` → `12/12 checks passed`, exit 0.
- `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → `20/20 legs passed`, exit 0.
- `git archive 8115eaa… | tar -x -C .scratch/r21-tree` then the same gate command inside the archive → `19/19 legs passed`, `grep -c '^ok '` → `19` (D1).
- `git log --oneline -S'L3b-argot' -- tools/gates/typed-pipeline-gate.py` → `fc13cd2` (D1).
- `sha256sum PROVINCE.md AGENTS.md corpus/knowledge/synthesis/worldbible-integration-contract.md` → `05b34a57…`, `1afaf106…`, `5f4c02bf…` (check 4, D2).
- `git diff --name-status 3b13a2f2821ed6f8ac1217842ab6830d592c7935 -- PROVINCE.md AGENTS.md corpus/knowledge/synthesis/worldbible-integration-contract.md` → `M	AGENTS.md` (D2).
- `git log --oneline 3b13a2f…..HEAD -- AGENTS.md` → `17e90b9`, `11df1fd`; `git diff --stat 3b13a2f… HEAD -- AGENTS.md` → 29 insertions (D2, F1).
- `git show 11df1fd -- AGENTS.md`; `git show 17e90b9 -- AGENTS.md` → section attribution (D2, F1).
- `grep -n '^```' AGENTS.md` → `40`; `wc -l AGENTS.md` → `42` (F1).
- `python3 -B reports/round-28/audit/entry-audit.py --json --new corpus/knowledge/linguistics/register-lexicon-ceilings.md --new corpus/knowledge/linguistics/register-strata-attestation.md` → `entries = 201`, `index_failing = []`, `bar_failing_count = 184`, exit 0 (check 7).
- `python3 -B reports/round-28/audit/x63-entry-source-resolvability.py --offline --json --baseline 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede` → exit 1, 4 findings, locator/pin/amendment figures above (check 8).
- `grep -nE 'write_text|open\(…w|mkdir|makedirs|unlink|shutil'` over both round-28 audit scripts → `entry-audit.py` clean; `x63` write sites confined to `selftest()` (`:870-1124`) and the `--selftest`-gated `os.makedirs(scratch)` at `:1162`, so the main `--offline --json` path is read-only (method note).
- `grep -n '^- \`register-lexicon-ceilings.md\`\|^- \`register-strata-attestation.md\`' corpus/README.md` → `138`, `139` (check 11).
- `sed -n '28p;329p' examples/culture-d4/typed-labels.d4.yml` → `"canon": "not canonized (D4 design drill); derived view of examples/culture-d4/packet.d4.yml"` and `"E2"`; `sed -n '335,340p;853,857p'` → D4-local `RK-01#g` / `examples/culture-d4/components/09-costumes.yml` records (D3).
- `grep -n 'D2' examples/culture-d4/typed-labels.d4.yml` → 26 hits at `:165,211-290,607`; `grep -n 'D2L-FORM-UNRESOLVED' tools/d2-typed-labels.py` → `419,422`; `grep -n 'D2L-FORM-UNRESOLVED' examples/culture-d4/expected-holds.json` → `53,59,65` (D3).
- `sed -n '600,612p' examples/culture-d4/typed-labels.d4.yml` → `"quarantine": []`, `"residuals": []`, `"unresolved": []`, `skipped` leg with `"why": "packet-native rank rules only; no foreign fixture data is imported"` (D3).
- `sha256sum examples/culture-d4/typed-labels.d4.yml tools/d2-typed-labels.py` → `c23b0ab532…`, `2819f687…` (D3).
- `git log --oneline -3 -- examples/culture-d4/typed-labels.d4.yml` → `11df1fd`, `3b13a2f`, `6c0ac44`; `sed -n '105,118p' reports/round-24/box4-bleed.md` → filed repair accounting (D3).
- `sed -n '80,84p' reports/round-29/validation.json` → the `scope_note` naming `A21-D4-XF-01` as outside that slice (D3).
