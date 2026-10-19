# R32-D11 — SHONEN boxes re-surveyed post-Register-craft

- **Seat:** D11 (dossier leg 1 of 3), round 32 — the regimen's final round
  (operator: loop 3, GLM round 2 of 2; 16 workers, zai-coding-plan/glm-5.3-flash-low,
  host-pinned MAX effort). Claim **D** / depth, `reports/round-32/claims.json`.
- **Date:** 2026-10-18. Declared baseline
  `17e90b9047b289d7a63180a1dc1bebb074137e29`; lane HEAD at this seat's evidence cut
  `4d50050` ("round-32: declare THE FINAL ROUND claims C/O/D").
- **Non-author declaration:** this seat authored none of the lane's artifacts
  before this file; every artifact it cites was authored by other seats/rounds.
  **Write scope:** this file only (siblings D12/D13 and the assembled
  `final-dossier.md` are this round's other D-lane deliverables). No git commit,
  no push, no edit to any filed round-8..31 byte. Scratch: `TMPDIR=$PWD/.scratch`.
- **Canon:** NON-CANON engineering evidence. A green gate or a pin is integrity,
  never truth, canon, or clearance.

## Survey lineage

r23 prepared the box evidence survey (`reports/round-23/shonen-survey.md`); r24
merged the only non-author box verdicts so far (`reports/round-24/promotion-review.md`,
all four boxes verified-with-conditions); r30 landed the Register-craft
subsection and re-ran box 1's executable inventory post-landing
(`reports/round-30/craft/box1-landed-survey.json`, 28/28). This seat re-surveys
all four boxes at the final tree, re-measuring every open r24 condition against
current bytes (commands + dates below), and restates boxes 2-4 with their r24
verdicts plus the regimen's subsequent evidence (rounds 25-31).

## Box 1 — SKILL.md contains real decision tables, error patterns, checklists, cited sources

**r24 verdict:** verified-with-conditions (reviewers r24-box1a/r24-box1b:
143 citation tokens all resolving; deep sample 10/15 exact; zero filler, zero
fabricated citations; `promotion-review.md:35-62`).

**Post-r24 substance growth:** SKILL.md grew 598 → 715 lines across the regimen's
landed craft: label-typing decision table + 15 error rows (r8), claim-uncertainty
table + 13 error rows (r15), slot-routing + derivation-replay subsections (r19),
family-clean projection rule (r23), and the unified **Register-craft subsection**
(r30; stratum + law + composition with typing and the typed pipeline, every row
cited — `reports/round-30/craft/skill-draft.md`, LOG.md:3422 entry, SCORECARD r30
claim-D row).

**Condition status, re-measured at HEAD (`4d50050`, 2026-10-18):**

1. **Inventory condition — CLOSED (r30, re-verified this seat).** The r24 finding
   was seven live executables absent from SKILL.md
   (`promotion-review.md:66-70`). r30's Register-craft landing named them; the
   landed survey read 28 named / 28 resolvable
   (`craft/box1-landed-survey.json`). This seat re-ran the survey unchanged at
   the current SKILL bytes — sha256
   `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d` (HEAD,
   post-r31 checklist edit) — **28/28 resolvable, exit 0**:
   `python3 -B reports/round-30/craft/box1-survey.py` (2026-10-18).
2. **Loanword-dating cite cluster — STILL OPEN.** `SKILL.md:486` still cites
   `loanword-material-dating.md:26,60` and `:488` cites `:57`. The corpus file is
   unchanged since round 8 (`git log`: last commit `e1694ba`); the sense-referent
   pairing is at `:63` and the prestige/dictionary-bias content at `:59`
   (`grep -n "sense–referent\|prestige terminology" …`, 2026-10-18). Exactly as
   the r24 reviewers measured (`promotion-review.md:71-76`).
3. **`worldbible-integration-contract.md:183` mis-cite — STILL OPEN.**
   `SKILL.md:501` (and `:128`) still cite `:183`, which carries the
   delivered-record checklist item ("Every delivered record has scope, stable
   identity…"), not the basis-is-never-boilerplate rule. Contract unchanged
   since round 1 (`git log`: `291c714`).
4. **Dangling tool anchors — STILL OPEN.** `TL-01`, `TL-02`, `FIELD_DEFAULTS`,
   `fictional-coordinate`, `descriptive-gloss` occur **0** times in
   `tools/d2-typed-labels.py` (`grep -c …` = 0, 2026-10-18); the rows
   (`SKILL.md:479-491`) describe real, selftest-enforced behaviors but the named
   anchors resolve to no tool token.
5. **Duplicated uncertainty status block — reads closed at HEAD.** This seat's
   phrase census finds one occurrence of the status grammar
   (`grep -c "supported / partial / unresolved" SKILL.md` = 1, section at
   `SKILL.md:77`, decision-table row at `:420`); no verbatim duplication found.
   The r24 measurement stands on record (`promotion-review.md:86-88`); no later
   round claims this dedupe explicitly, so this is a re-measurement, not a
   disposition.

**Net:** box 1 remains **verified-with-conditions**; its load-bearing inventory
condition is closed and digest-pinned; three citation-level conditions (2-4)
remain open and are now re-confirmed at the final tree with dated commands.

## Box 2 — at least one end-to-end domain task executed and logged in LOG.md

**r24 verdict:** verified-with-conditions — the D2→D3→D4→handoff chain was
re-executed live from filed instructions alone (15 chain legs; typed gate
findings == expected hold set; handoff v3 byte-identical to its receipt;
`promotion-review.md:89-132`).

**r24 condition dispositions (subsequent rounds):**

1. **`LOG.md:3278` 102/102-vs-105/105 misquote — dispositioned r21:** the loop-2
   recount ledger names every mismatch class including this link drift (mtime
   tie-break, non-hermetic) — SCORECARD r21 claim-C row;
   `reports/round-21/recount/`.
2. **Round-7 acceptance aggregate exits 1 by design** — context recorded at r24
   (`promotion-review.md:125-127`); the per-leg commands reproduce. Related open
   text debt tracked as cold-run condition N1 (see box 3).
3. **Round-18 recount byte-pin drift** — expected drift, documented mechanism;
   the r21 recount re-censused rounds 17-20 with receipts.

**Subsequent end-to-end evidence (rounds 25-31):**

- Handoff v3 executed and logged (r20, `LOG.md:3273`); contract re-verified r21
  (`LOG.md:3286`; 16/16 + 20/20 + 27 claims 16/7/4 + 105/105 links current pair).
- The register program closed the r17 forecast end-to-end: stratum lands with 8
  verified register forms and the axis-to-operation rule (r26, `LOG.md:3375`),
  the register law lands (RGL-01..05, r27, `LOG.md:3388`), and the law replay
  leg lands and immediately surfaces 4 real design defects (r28, `LOG.md:3398`)
  — resolved r30 (QREG-05..08 land; law gate clean 4→0; battery 10/10;
  `LOG.md:3422`).
- The whole chain re-executes in the r31 final green sweep: `handoff-v2`,
  `handoff-v3`, `typed-pipeline-d4`, `argot-d4`, `law-d4-clean` rows all exit 0
  (`reports/round-31/final-sweep.md` §1; 50/50 rows exit 0, 2026-10-18).

**Standing design debts (named, not hidden):** 12 D4 garment-form holds remain
open by design (r24 `box2-d4.md:104-108`; still the filed state), the `head2`
proper domain is empty (r26 named gap), and RL-3 records the register-lexicon
ceiling — the register cannot spell its own law's five legal abstractions — as a
craft constraint, not a defect (r27/r28; ceilings entry).

**Net:** box 2 remains **verified-with-conditions**; every named condition is
either dispositioned (1) or recorded context (2, 3); the demonstrated chain now
extends through the register program and replays green in the final sweep.

## Box 3 — instructions executable by an agent without oral context (cold run)

**r24 verdict:** verified-with-conditions — four fresh-context seats executed
the SKILL.md surface (~80 invocations, zero tree mutations); machinery and pins
held; one live-inverted doc row found by three seats independently and fixed
in-round (`promotion-review.md:133-196`).

**Condition status at HEAD (this seat's byte checks, 2026-10-18):**

- **N3 — CLOSED (r25).** "Repairing the typed-input direction changes pinned
  gate bytes" — done exactly so: named input-class refusals + the owed_slot
  nullish guard, false red eliminated, source-packet entry 19/19 byte-identical,
  repin cascade landed as new rows (`LOG.md:3362` entry; SCORECARD r25 claim-O
  row).
- **N6 — CLOSED (in SKILL text).** The D3 replay "snapshot mode" now names the
  option: `--frozen examples/culture-d3/expected.json` (`SKILL.md:672`).
- **N2 — machinery documented.** `tools/harness/receipt_guard.py` refuses
  committed-receipt overwrites (r14; `SKILL.md:453` row), and checklist item 5
  now states "It writes its own receipt, not historical receipts"
  (`SKILL.md:701-703`). The isolation caveat text stands; no fresh cold run has
  re-tested it since r24.
- **N1 — NOT closed by text.** Checklist item 5 still names no expected verdict
  for the round-5/6/7 acceptance re-runs (which exit 1 at clean HEAD for
  distinct, explainable causes); the errata N1 asks for are not in SKILL.md
  (checked `:695-712`, 2026-10-18). The pointer to
  `reports/round-7/integration-attempts.json` ("corrected failures") is present.
- **N4 / N5 / N7 — remain as filed.** No real costume/era artifact set or handoff
  packet path is named in the cold-run file set (declarations only);
  "history-retaining export" wording is not in SKILL.md; the parent's pin of the
  canonical executable-surface reading was never issued as a durable artifact.

**Subsequent executability evidence:** the r31 final sweep re-executed the whole
capability surface in one deterministic pass — 50/50 green rows exit 0, 13
filed-red historical controls at exactly their codes, cross-run determinism
61/63 byte-identical rows with the two stamp-bearing exceptions explained
(`final-sweep.md` §0-§1). The jin'i-ryu round added an executable checklist
audit item with a runnable one-liner (`SKILL.md:710-715`), the regimen's own
falsifiable self-check. Round 32's O-sweep re-runs the same matrix over the
settled tree (sibling-owned; in flight at this seat's cut — see the dossier's
evidence-cut note).

**Net:** box 3 remains **verified-with-conditions**; the machinery layer is
stronger than at r24 (input-class honesty, receipt guard, closure audit), two
conditions closed, N1/N4/N5/N7 remain open as filed.

## Box 4 — no cross-domain bleed; PROVINCE.md still accurate

**r24 verdict:** verified-with-conditions — live D4 projection clean of the
filed fixture bleed (A21-D4-XF-01 verified gone; projector digest matched the
pin), no canon assertion / rights ruling / game mechanics anywhere in rounds
19-23 content, PROVINCE byte-identical to baseline (`promotion-review.md:197-232`).

**Conditions 3a/3b/3c — standing readings, not defects (re-stated):** the fix
must not be read as resolving D2's historical rank debts or filling D4's owed
terms; the r22 "never implemented" ledger row must be read with its append-only
correction (`LOG.md:3312`); exactly one `examples/culture-d2/` string survives in
the live projection as the negative-provenance line and must stay distinguished
from an import in both directions.

**Subsequent evidence (rounds 25-31):**

- r21 consolidated the per-round posture into one audit: handoff v3 contract
  re-verified; the one filed D2→D4 fixture bleed routed and fixed; zero unfiled
  bleed (SCORECARD r21 claim-A row).
- r29 (loop-3 verify): register/law bleed check clean (speech-act framework
  in-world by design), **PROVINCE byte-identical**, the ceilings-entry evidence
  defect filed rather than absorbed, zero unfiled bleed (`LOG.md:3411` entry;
  `reports/round-29/adjacency/`).
- `PROVINCE.md` is unchanged since before the fleet rounds: `git log --
  PROVINCE.md` shows its last commit as `c53782a` (supplement-opencode-1,
  2026-10-17) — 31 lines, byte-stable across all 32 rounds.
- The r31 closure ledger re-verified 22/22 filed reports commit-ancestor-valid
  (`reports/round-31/closure-ledger.json`), the provenance leg box 4 rests on.

**Net:** box 4 remains **verified-with-conditions**; no new bleed class appeared
in rounds 25-31; the three standing readings carry forward unchanged.

## Summary table

| box | r24 verdict | post-r24 delta | open at HEAD |
|---|---|---|---|
| 1 decision tables/errors/checklists/sources | verified-with-conditions | Register-craft landing (r30); inventory condition closed, 28/28 re-verified at `79fe91d3…` | conditions 2, 3, 4 (citation-level; re-confirmed today) |
| 2 end-to-end domain task | verified-with-conditions | register program r26→r30; chain green in r31 sweep (50/50) | none of the r24 three; standing design debts named (12 garment holds, head2, RL-3) |
| 3 executable without oral context | verified-with-conditions | r25 input-class honesty (N3 closed); N6 closed; receipt-guard documented | N1, N4, N5, N7 (as filed) |
| 4 no bleed / PROVINCE accurate | verified-with-conditions | r21 + r29 adjacency audits; PROVINCE untouched since `c53782a` | standing readings 3a/3b/3c (by design) |

The marks themselves stay operator-owned: per `SHONEN.md:10-11`, `[~]` requires
an evidence pointer and `[x]` requires a named non-author verifier; this survey
awards neither. See D13 (`dossier-d13-operator-decisions.md`) for the decision
materials this feeds.

## Method and limits

Read in full: `SHONEN.md`, `PROVINCE.md`, `reports/round-24/promotion-review.md`,
`reports/round-31/final-sweep.md`, `reports/round-32/claims.json`; SCORECARD
round tables 5-31; LOG.md entries `:3348-3483`. Byte-level re-measurements
(date-stamped 2026-10-18, all inside the lane): the box-1 survey re-run
(exit 0), the loanword/contract line checks, the anchor grep (0 hits), the
status-phrase census (1 hit), `git log` on `PROVINCE.md`, `SKILL.md`,
`loanword-material-dating.md`, `worldbible-integration-contract.md`. This seat
re-graded nothing it did not measure: r24 verdicts are quoted as merged; every
"still open" is this seat's own re-measurement with the command recorded; the
r32 sibling artifacts (completion audit, final sweep re-run, validator) were not
yet landed at this cut and are cited at their claimed paths, not executed here.
