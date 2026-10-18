# Round 24 — SHONEN promotion review dossier (scribe merge)

- **Round:** 24 (operator regimen: loop 2, GLM round 2 of 2; 16 workers on
  zai-coding-plan/glm-5.3-flash-low, host-pinned MAX effort) · **Date:** 2026-10-18.
- **Scribe:** X1 (dossier scribe). **Non-author:** this seat authored none of the
  lane's artifacts; the 14 reviewer/cold-run/audit artifacts merged below were all
  authored by other round-24 seats. Write scope: this file only. No git commits,
  no edits to filed artifacts of rounds 8-23, no scratch writes.
- **Purpose:** merge the round-24 non-author box verdicts, the fresh-context
  cold-run evidence, and the SKILL.md staleness audit into one dossier for claim C
  (`reports/round-24/claims.json`). **The promotion DECISION stays operator-owned;
  this dossier is evidence, not a claim.** No SHONEN box is marked here: per
  `SHONEN.md:10-11` marks are operator-owned, and this scribe merges verifier
  verdicts, it does not award `[x]`.
- **Tree state at merge:** round-24 baseline `b5d9844` (round-23 admit), lane HEAD
  `8fbcee9` ("round-24: declare GLM-2 claims C/O/D"), working tree carries the
  round-24 in-round SKILL.md fixes **uncommitted** (`git status`: ` M SKILL.md`,
  20 insertions / 20 deletions, plus the untracked `reports/round-24/` artifacts;
  `reports/round-7/validation.json` was restored byte-identical after a mid-round
  clobber — see the fix ledger).

## Merged box verdicts (summary)

| # | Subject | Merged verdict | Reviewers (seats) | Primary artifacts |
|---|---|---|---|---|
| 1 | SKILL.md decision tables, error patterns, checklists, cited sources | verified-with-conditions | r24-box1a, r24-box1b | box1-tables.md, box1-craft.md |
| 2 | End-to-end domain task chain D2->D3->D4->handoff executed and logged | verified-with-conditions | r24-box2a, r24-box2b | box2-chain.md, box2-d4.md |
| 3 | Instructions executable by an agent without oral context (cold run) | verified-with-conditions | r24-coldrun-a, r24-coldrun-b, r24-coldrun-4, r24-coldrun-3 | cold-run-a.md, cold-run-b.md, cold-run-conditions.md, cold-run-fixes.md |
| 4 | No cross-domain bleed; PROVINCE.md still accurate | verified-with-conditions | r24-box4-bleed, r24-box4-province | box4-bleed.md, box4-province.md |

Reviewer labels are this scribe's identifiers for the round-24 swarm seats, mapped
to their filed artifacts above; every seat self-declares non-author status in its
artifact. No box failed; no box verified without conditions.

## Box 1 — SKILL.md contains real decision tables, error patterns, checklists, cited sources

Verdict: verified-with-conditions

Reviewer: r24-box1a
Reviewer: r24-box1b

Evidence: `SHONEN.md:6`; `SKILL.md:20` (decision table), `SKILL.md:356`
(error patterns), `SKILL.md:408` (executable checklist), `SKILL.md:501` (battery
row, post-fix); `reports/round-24/box1-tables.md`; `reports/round-24/box1-craft.md`;
controls and independent re-verification in `reports/round-24/audit-fixes.md` and
`reports/round-24/audit-typed.md`.

- **r24-box1a (adversarial citation-resolving pass over all 598 lines):**
  verified-with-conditions. 143 distinct citation tokens across 88 distinct cited
  files: all exist, every line locator in range, zero fabricated sources, zero
  contradictions; conditions were 6 stale/wrong line pointers, 2 unresolvable
  section anchors, 3 stray fences (`reports/round-24/box1-tables.md:15-66`).
- **r24-box1b (coverage-of-craft substance leg):** verified-with-conditions.
  Deep sample of 15 rows/probes: 10 exact matches, one live gate re-run passing,
  zero generic filler, zero fabricated citations; conditions: seven real
  executables never named in SKILL.md (two of them frozen-pinned gates),
  citation drift on three pointers, one stale present-tense measurement, stray
  fences (`reports/round-24/box1-craft.md:9-71`).
- Both seats independently found the tables real, domain-specific, and
  citation-anchored. The pointer-level defects they surfaced were fixed or
  erratum-ed in-round by the audit/cold-run fixer seats (see the fix ledger);
  the conditions below are what remains open at merge time.

### Conditions

1. **Inventory condition (r24-box1b):** seven live executables are absent from
   SKILL.md — at minimum `exercise-handoff-e2e.py` (the principal handoff
   exerciser), `assemble-d2-typed.py`, and the two frozen-pinned D4 adapter
   gates — or an explicit scoping note that SKILL.md indexes craft rules, not
   the full executable inventory.
2. **Loanword-dating cite cluster (both reviewers; re-confirmed by this scribe
   against current bytes):** the error-pattern row citing
   `loanword-material-dating.md:26,60` is doubly wrong (:26 is blank; the
   sense-referent pairing is at :63) and the prestige-terminology row cites :57
   where the content is at :59 — both seats measured this and the in-round fixes
   did not touch these two rows.
3. **`worldbible-integration-contract.md:183` mis-cite (r24-audit2):** the
   "basis is never boilerplate" caution cites a contract line that carries other
   content; the rule itself is executable-verified; needs re-point or dated
   erratum.
4. **Dangling tool anchors (r24-audit2):** `TL-01`, `TL-02`, `FIELD_DEFAULTS`
   and the vocabulary `fictional-coordinate`/`descriptive-gloss` exist in no
   tool; the described behaviors are real and enforced; rows need dated errata
   or re-pointing.
5. **Duplicated uncertainty status block (r24-audit2):** the three status rows
   appear verbatim twice in SKILL.md; dedupe or cross-reference before future
   edits.

## Box 2 — at least one end-to-end domain task executed and logged in LOG.md

Verdict: verified-with-conditions

Reviewer: r24-box2a
Reviewer: r24-box2b

Evidence: `LOG.md:1967` (round-3 D2 build, box-2 evidence), `LOG.md:2706`
(round-7 D3 declaration), `LOG.md:3010` (round-11 e2e), `LOG.md:3273` (round-20
handoff e2e v3), `LOG.md:3286` (round-21 contract re-verify), `LOG.md:3312`
(append-only r22 correction); `reports/round-24/box2-chain.md`;
`reports/round-24/box2-d4.md`.

- **r24-box2a (D2->D3 leg, re-executed live):** verified. 15 chain legs re-run
  from SKILL.md/LOG instructions alone: assemblers byte-identical, typed gate
  16/16 with the emitted hold set equal to the frozen expected set, selftests
  163/163 + 42/42 + 85/85, D3 coupling green against its pin, legacy D3 gates
  red at exactly the documented severities, handoff envelope 16/16 + 20/20,
  handoff v2 green (`reports/round-24/box2-chain.md:87-99`).
- **r24-box2b (D4 + handoff v3, re-executed live):** verified-with-conditions.
  D4 typed-pipeline gate 19/19 with stdout byte-identical to the filed round-22
  receipt; handoff v3 exit 0 with packet sha byte-identical to the filed
  receipt; the full logged chain (rounds 11, 20, 21, 22-correction) reproduces
  (`reports/round-24/box2-d4.md:18-115`).
- The chain is executable now and logged with resolving pointers. Note: green
  gates verify structure, not canon — 12 open D4 garment-form holds remain
  named design debt (`reports/round-24/box2-d4.md:104-108`).

### Conditions

1. **LOG.md:3278 misquote (r24-box2b; re-confirmed by this scribe against the
   bytes):** the admitted round-20 entry says "102/102 links" while every filed
   artifact and the live rerun say 105/105. The integrator owes a dated erratum
   or disposition (append-only; the r22-correction precedent applies). This
   seat did not edit LOG.md.
2. **Round-7 acceptance aggregate (r24-box2a F-2):** re-running
   `reports/round-7/run-validation.py` today reads `acceptance false` by design
   (round-7-era invariants vs a grown tree); box-2 reproducibility rests on the
   per-leg commands, which all reproduce. Record as context, not a break.
3. **Round-21 recount byte-pin drift (r24-box2b F-2, note):** the r18 recount's
   byte-pin is revision-specific and no longer reproduces byte-wise at head;
   expected drift, documented mechanism, new census filed with a receipt this
   seat reproduces exactly.

## Box 3 — instructions executable by an agent without oral context (cold run)

Verdict: verified-with-conditions

Reviewer: r24-coldrun-a
Reviewer: r24-coldrun-b
Reviewer: r24-coldrun-4
Reviewer: r24-coldrun-3

Evidence: `SKILL.md:408` (prose checklist executed by r24-coldrun-a),
`SKILL.md:501` (the one live doc break both executors found independently);
`reports/round-24/cold-run-a.md:146` (conditions under which the checklist is
executable), `reports/round-24/cold-run-b.md:162` (conditions for the full
executable surface), `reports/round-24/cold-run-conditions.md:194` (severity-
classified condition list), `reports/round-24/cold-run-fixes.md:138` (the seven
named conditions N1-N7).

- Four fresh-context seats (zero lane history beyond four named files each)
  executed the SKILL.md executable surface end-to-end: ~80 invocations across
  the two executors and the condition scribe, all with `TMPDIR=$PWD/.scratch`
  discipline and no tree mutations.
- **What held:** every pointer the executable surface names resolves; pinned
  selftest counts reproduce exactly (163/163, 42/42, 85/85, 19/19 legs, 12/12);
  the hardest documented recipe (restore six gates from `291c714`, replay the
  round-3 manifest isolated) reproduces 7/7 exit 0 exactly as written; the
  documented steady-state reds reproduce verbatim; gate write discipline held
  everywhere claimed.
- **What broke:** one stale documentation row that actively misleads
  (the `SKILL.md:501` battery cell — default exits 0, the documented
  `--baselines-root` remedy now *causes* exit 2; found independently by
  r24-coldrun-a, r24-coldrun-b, and r24-audit1, fixed in-round with controls);
  prose-checklist items 1/3/4 lack operands (item 1 self-declares; items 3/4
  now declare their status/machinery in-round); the round-5/6/7 acceptance
  re-run commands exit 1 at clean HEAD with no documented expected verdicts and
  overwrite filed receipts in place; a plausible-false-red input hazard on the
  D4 gate (feeding it the derived typed packet) — convention now named in
  SKILL.md in-round, code repair routed as a repin cascade.
- Merged reading (per r24-coldrun-b §4 and r24-coldrun-4 §C, concurred by this
  scribe): the machinery executes and matches its pins; the prose checklist is
  executable 1-of-4 by design, now honestly declared; the acceptance re-runs
  execute but have no declared pass state. Box 3 is green only with the
  conditions attached.

### Conditions

1. **N1 (major):** dated expected-verdict errata for the round-5/6/7 acceptance
   re-run commands (all exit 1 at clean HEAD for distinct, explainable causes).
2. **N2 (major):** the three acceptance scripts rewrite filed tracked receipts
   in place; the isolation caveat must cover them (run in a disposable copy or
   restore afterwards).
3. **N3 (major):** repairing the typed-input direction itself (null-ish
   `routed_slots` guard, faithful legacy rebuild) changes pinned gate bytes —
   a repin cascade routed like the round-22->25 recipe.
4. **N4 (major):** no real costume/era artifact set and no real handoff packet
   path is named in the cold-run file set; checklist items 3/4 gain
   declarations, not operands.
5. **N5 (minor):** "isolated repo export" must be defined as history-retaining
   (clone/worktree) for the round-3 restore-and-replay leg.
6. **N6 (minor):** D3 replay step 2's "snapshot mode" names no manifest and
   none exists for round 7; name the `--frozen` option or drop the clause.
7. **N7 (process):** the parent should pin which reading of "the SKILL.md
   executable checklist" future cold runs execute (the two executors diverged
   productively) and the exact per-seat file set.

## Box 4 — no cross-domain bleed; PROVINCE.md still accurate

Verdict: verified-with-conditions

Reviewer: r24-box4-bleed
Reviewer: r24-box4-province

Evidence: `PROVINCE.md:9` (owns), `PROVINCE.md:16` (refusals);
`corpus/knowledge/synthesis/worldbible-integration-contract.md` (adjacency
contract, digest unchanged since round 21); `reports/round-24/box4-bleed.md`;
`reports/round-24/box4-province.md`; `LOG.md:3286` (round-21 adjacency record).

- **r24-box4-bleed (full box, newest content):** verified-with-conditions.
  Fresh bleed census over the live D4 projection: 0 fully qualified D2 rank
  citations (baseline 24), 0 short D2 rank-source fields (baseline 14), D4-local
  owners and the D4-declared scheme on all 74 labels, zero D2L-RANK findings;
  targeted greps over the rounds 19-23 trees found no canon assertion, no
  real-world rights ruling, no game mechanics; every canon mention is a refusal
  or disclaimer. The filed D2->D4 fixture bleed (A21-D4-XF-01) is verified
  **gone live**, with the projector digest matching the pinned `2819f687...`.
- **r24-box4-province (PROVINCE-accuracy sub-claim):** verified. Every surface
  PROVINCE.md names resolves; the six-partition list matches the tree exactly;
  refused siblings all exist; PROVINCE.md is byte-identical to the round-24
  baseline (`git diff b5d9844 -- PROVINCE.md` empty).

### Conditions

1. **3a:** the fix must not be read as resolving D2's historical rank debts or
   filling D4's owed terms (15 D2 holds + 1 note; 12 D4 garment/slot holds
   remain open by design).
2. **3b:** the r22 ledger row of record still reads "never implemented"; it
   stands by design and must be read together with the append-only correction.
3. **3c:** exactly one `examples/culture-d2/` string survives in the live
   projection — the negative-provenance line at `$.era_reconciliation.basis[1]`;
   future digests/bans/re-censuses must keep distinguishing it from an import in
   both directions.

## In-round fix ledger (working tree, uncommitted; operator owns landing)

Twenty changed lines in SKILL.md (19 hunks, all wording/pointer-level, applied
by the audit fixer seat r24-audit3 with before/after controls, independently
re-derived and re-verified by r24-audit2 before reading the fixer's controls;
six line-count-neutral hunks by the cold-run fixer seat r24-coldrun-3):

- Fence debris removed (`:129` four-backtick, `:154`, `:217`).
- T3 anchors re-pinned `:622`/`:793` -> `:639`/`:808-814` with round-18
  provenance kept; dead `holds.md` §4.2 anchor -> §4 (verified to exist).
- Determinism anchor `:369` -> `:387` (cause note: r24-audit2 measures the
  fixer's "round-22 carry_findings" attribution off by two rounds — anchor
  correct, cause sentence imprecise; one-line follow-up).
- Passenger-rows measured instance: dated erratum appended in-row (present-tense
  "carries 3+1" superseded by the repinned 12/0/0 state; history preserved).
- Battery row `:501` rewritten to measured behavior (default exit 0; the flag
  replaces roots and a round-9-only root exits 2) — the row that three seats
  found live-inverted.
- Five corpus citations re-pinned with verbatim controls (`era-language-staging`
  :114->:111, :124->:127; `naming-collision-gate` :52->:54, :69-70->:72;
  `garment-lexicon-crosslinguistic` :26->:28,30 with full path).
- `design.md` §3 re-pointed to the real "Source-level change contract" header.
- Cold-run fixes: checklist items 2/3/4 gained scope/declarations/enforcement
  pointers; d4-repin pin gained the TMPDIR-outside-repo precondition (an
  in-union contradiction — r24-coldrun-4's §A had misrecorded its TMPDIR — was
  adjudicated by running both arms); D3 checklist heading gained the
  executability caveat; the gate-input convention (source packet, never the
  typed packet) named where the false red was measured.
- Hygiene incident, resolved: `reports/round-7/validation.json` was clobbered
  in-tree by a seat running the round-7 acceptance script (the exact hazard
  become condition N2), observed modified by two seats mid-round, and restored
  byte-identical by another seat before close (`git status` at merge is clean
  for it).

## Integration gaps and discrepancies (for the operator, stated not hidden)

1. **Consolidated artifacts named by the claims never landed.** Claim O's
   after_required names a consolidated cold-run report (`reports/round-24/cold-run.md`)
   and claim D names a consolidated audit table (`reports/round-24/skill-audit.md`)
   at fixed round-dir paths; the counting runner
   (`reports/round-24/run-validation.py`, seat X2) hardcodes those two paths.
   The landed evidence lives in the four `cold-run-*.md` and three `audit-*.md`
   seat artifacts instead. Per `targets.json` the D lane had four seats and
   only three filed; the missing fourth is the likeliely consolidation owner.
   The operator/integrator decides whether to accept the seat artifacts as
   satisfying the claim letter or route consolidation to a follow-up seat.
2. **Claim D coverage is substantial but not letter-complete.** Audited
   row-by-row: the gates registry (r24-audit1, 12 rows + prose + D3 cross-
   coverage) and the five typed/handoff sections (r24-audit2, every executable
   claim re-run). The decision table, error-pattern rows, corpus map, and
   round-5/6 constraint tables were covered by r24-box1a's full citation pass
   (143 tokens, all resolved) and targeted fixes, not by a row-by-row audit
   table. Zero silent staleness is supported for the audited sections; the
   consolidated disposition table the claim letter describes does not exist.
3. **Cross-seat discrepancy, resolved by this scribe's spot-check:** r24-box1b
   recorded loanword-dating ":26 exact" while r24-audit2 recorded ":26 is
   blank". The bytes side with r24-audit2 (:26 is blank; the lexical-clock row
   is at :30; the sense-referent content at :63) — strengthening open box-1
   condition 2. The file lives in `corpus/knowledge/synthesis/`, which both
   seats' findings already reflected.
4. **r24-audit1 measured at committed HEAD**, where the battery row was still
   stale, and noted the in-flight uncommitted fix; r24-audit2 and r24-coldrun-3
   verified the fixed working-tree state. Both states are recorded above; the
   fix is real but uncommitted at merge time.

## Scribe method and limits

Read in full: `reports/round-24/claims.json`, `reports/round-24/targets.json`,
`SHONEN.md`, `PROVINCE.md`, and the 13 filed seat artifacts merged above; plus
`reports/round-24/run-validation.py` (the counting command's parsing contract),
the SKILL.md working-tree diff, and these byte-level spot-checks: `LOG.md:1967,
2706, 3273, 3278, 3286, 3312` (round entries; :3278 confirms the 102/102
misquote), the loanword-dating lines :24-30 and :55-63, and `wc -l` of the cited
files (LOG.md 3338, SKILL.md 598, PROVINCE.md 31, SHONEN.md 11). This scribe
re-graded nothing: verdicts are the reviewers' own, merged; every condition
above is traced to its filing seat; the two cross-seat discrepancies are recorded
with the disambiguating measurements. The 4th D-seat artifact, any consolidated
cold-run/audit artifacts, and the promotion decision itself are outside this
dossier and remain with their owners.
