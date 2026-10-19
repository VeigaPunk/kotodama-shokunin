- Seat: X00 | connector | cross | date 2026-10-19 | baseline fd55e1f

# Collision matrix + integration order (binding per P01 §4)

Vantage at write: HEAD `fd55e1f` (== `claims.json:7` baseline). Landed peer
fragments 9/23 (P01, K01, K03, C01, X01, Ca03, A01, A02, S02) + instruments
claims/targets/dispatch-declared; in-flight 14/23 (K02, C02–C07, Ca01, Ca02,
Ca04, A03, R01, R02, S01) — counted with S02's census method
(`find reports/round-40 -type f`, 2026-10-19). Tree: `git status --porcelain`
→ ` M LOG.md` (parent-owned) + `?? reports/round-40/` only — **zero corpus
staging so far** (X01 F5 watch-item holds at this stamp).

## 1. Write-path matrix — zero byte collisions by construction

All 24 `out` paths in `targets.json` are distinct; cross/ holds X00 + X01 as
separate files. Shared-surface rules:

| shared surface | single draft owner | single applier | rule |
|---|---|---|---|
| `corpus/knowledge/linguistics/*.md` (+4) | C01–C04 as fenced blocks | integrator | seats never stage (shared_rules; r39 incident recorded) |
| `corpus/README.md` rev 2.3 | C06 delta block only | integrator | row/`- topic:` byte-equal; sweep green is post-apply |
| `reports/round-40/op/defect-queue-v2.json` | Ca01 fenced JSON | integrator | supersession-as-new-row (X01 T4a); v1 never rewritten |
| `LOG.md`, `SCORECARD.md`, `MANIFEST.json`, fleet `.ufo` | — | parent only | workers write assigned fragments only (AGENTS.md) |
| filed bytes r1..39 / lessons / frozen / declared-in-r7 | read-only | — | absolute (shared_rules:7–8) |

## 2. Content collisions (the binding matrix)

**C1 — E1 filename conflict (open, integrator decides).** C01 proposes
`corpus/knowledge/linguistics/taboo-strata-lifecycle.md`
(`cov/C01-entry-1.md:3`); K03's collision table proposes
`taboo-euphemism-lifecycle-stages.md` (`scout/K03-gaps.md:33`). Same topic,
no third claimant. Both sort cleanly in the measured 21-file listing; C01's
"between syntax-typology and writing-systems" is coarser but consistent with
K03's finer placement (translation-protocol-fidelity sorts between them).
Resolution: integrator picks one name per entry at apply time; binding
constraints are (a) README row byte-equal to the landed `- topic:`, (b)
`python3 -B reports/round-28/readme/sweep.py` green, (c) C06 re-derives all
four rows from the FINAL filename set — C06 drafts against candidates and
marks the rows provisional if C01–C04 names are not yet fixed. K03's name
differs from `synthesis/taboo-euphemism-lifecycle.md` only by a `-stages`
suffix: basename-couples confusion check routed to C05/integrator
(to-verify against `reports/round-39/calib/basename-couples-policy.md`, not
read by this seat).

**C2 — topic assignment reconciled (closed).** C01 authored blind on the
claims.json ordering (`C01-entry-1.md:3,144`); K03 has since landed E1–E4.
Mapping: C01→E1 taboo lifecycle (topic-match confirmed — C01's
read-off/bracketing content is the ordering instrument K03's CONDITIONAL
PASS scope calls for, not a restatement), C02→E2 dialect/register
consistency, C03→E3 translation-protocol fidelity, C04→E4 sacred registers /
liturgical language (K03 §3-E4, sources pre-registered). C01's Owed
reconciliation resolves to the filename delta in C1 only. K03's per-entry
scope boundaries and §5 non-restatement criteria become C05's audit
criteria verbatim (`K03-gaps.md:166-177`).

**C3 — Ca01 fold-in set (complete inventory).** queue-v2 must contain:
(a) r37's 24 rows with Ca03 §3 per-row dispositions (rows 5/7/11
fixed-with-evidence; 8 merged into 20; 23 closed-with-pointer + D1/D2 split);
(b) Ca03 §4 N1–N7; (c) ids + owners for rows 13–17 — without them the
"every row owner-complete" threshold fails honestly (Ca03 §5); (d) A01's
`.scratch/c05/c05-audit.py` durability row (digest filed, bytes ephemeral —
`adj/A01-audit.md:62-66` + Owed); (e) A02's F-A02-1 row, routed explicitly
"pointer to calib/Ca01-queue-v2.md" (`adj/A02-province.md:52,62`); (f) A02
Owed re-verification of contested items #6/#7 against the successor ledger
before close. Arithmetic: 24 + N1–N7 = 31 ≥ 28 (Ca03 §4); +2 filed this
round ≥ 33; no padding, every added row cites origin (Ca03 §5). K01/K02
overlap only at `op/defect-queue.json` (K01:163-165) — no double-census
risk. Ca03's receipt is a DRAFT: final receipt numbers belong to the
integrator after Ca01's actual row count lands; any Ca01↔Ca03 disagreement
is filed, not silently reconciled.

**C4 — next-touch legality (constraint on Ca01).** No carried row may take
next-touch r46 for implementation work (r46 is a read-only audit,
`REGIMEN.md:23`; X01 T3). Ca03 §6's alignment table already conforms
(r46 audits the v2's bookkeeping only); Ca01 must inherit that shape.
Operator-gated items (row-20 re-freeze absorption, N1 renderer half, F-A02-1
packet prose) name the condition, not a position (Ca03 §6; non_goals
`claims.json:32-33`).

**C5 — K01 ↔ A01 census reconciliation (my routed duty, discharged).**
Agreements verified: r37 75A/3M, r38 42A/4M, r39 32A/3M (K01 diff counts ==
A01 commit-stat views); the "15 new corpus entries" = 10@ce103bf + 1@57c8409
+ 4@fd55e1f (`K01:138-144`); `examples/` untouched r37–39; PROVINCE.md
byte-clean since `c53782a` (A01 §4, A02 §1); tree state identical. One
disagreement: r37 telemetry file count — K01 says 5 (`K01:62-63`), A01 §1
says ×6. Measured by this seat: `find reports/round-37/telemetry -type f |
wc -l` → **5** (close, declared, observed, inputs/claims, inputs/targets).
A01's count is high by one; the surface verdict (GREEN, closing snapshot
present) is unaffected. Fix owner: A03's independent verification / final
audit assembly carries the corrected count. Taxonomies are complementary,
not conflicting: K01's R0–R3 risk classes label the census, A01's
GREEN/finding verdicts label surfaces; A03 stitches them. A01's Owed
"route risk-class disagreements to X00/integrator" is discharged by this §C5
(exactly one, resolved above).

**C6 — A-block sequencing.** A01 and A02 are both landed and independent;
A03 (owed) verifies a sample of both seats' commands, absorbs the §C5
correction, and drafts the final consolidated assembly. Claim A's
"rounds 37–40" scope is partial-by-construction for the r40 slice at any
seat cut (X01 T5) — A03 must time-stamp the r40 rows and mark the residual
to-be-closed-by-the-validation-leg.

**C7 — G-space disambiguation.** r38's "G5" is a frozen-row control leg
(`op/O03-verify.md:101` per X01 F7), not a r39-gap ID. R01/R02/S01 must not
conflate the two G-spaces when citing.

**C8 — runner ban vs counting commands.** `claims.json:23,29` declare
`python3 reports/round-40/run-validation.py` as Ca/A counting commands, but
shared_rules:8 + X01 T6 make it integrator-only in an isolated copy (r39
protocol; r36 precedent). No seat pre-runs it — Ca/A verdicts on that leg
are `to-verify` at validation (Ca03 §7 wording). Seat-runnable: `ls | wc`,
and `sweep.py` (not a round runner). Wording rule (X01 T2): seat fragments
say "pre-verified against 21+4 arithmetic"; "sweep green" belongs to the
integrator's post-apply run.

## 3. Integration order (binding)

1. **Scouts** — K01 ✓, K03 ✓, K02 (owed; gates Ca01 and the census_coverage
   completion; if absent, completion is carried with owner Ca01+K02, Ca03 §5).
2. **Executors** — C01 ✓; C02/C03 (unblocked; topics per claims.json + K03
   scopes); C04 (E4 per K03 §3-E4); Ca01 (gated on K02; fold-in set §C3);
   A01 ✓; A02 ✓.
3. **Verifiers** — C05 (4/4 audit; K03 §3/§5 as criteria; fabrication
   spot-checks; C1 filename + basename check) → C06 (final filenames; delta
   re-derived: header 21→25, totals 216→220, vector 25/23/25/29/24/94) →
   C07 independent; Ca02 (≥30% sample) + Ca04 (strict JSON, count, class
   vocabulary, no dup ids) after Ca01, then Ca03 finalization; A03 (§C5/§C6).
4. **Cross** — X00 (this doc) ✓, X01 ✓; R01 adversarial on all three blocks;
   R02 queue-completeness hunt + fabrication hunt (jointly gates Ca with
   Ca02/Ca04 — the P01 double gate).
5. **Scribes** — S01 dossier + validation-leg spec (cites S02 draft + this
   matrix); S02 ✓.
6. **Integrator (parent), strict order:**
   a. Fix the four filenames (§C1 rule); apply C01–C04 fenced bytes;
      apply C06's README rev 2.3; run `python3 -B reports/round-28/readme/sweep.py`
      → green 220==220.
   b. Land `op/defect-queue-v2.json` from Ca01's fenced JSON (fold-ins §C3;
      schema-string decision per Ca03 Owed; SCORECARD/LOG name v2 as the
      queue's current revision, X01 T4a).
   c. File the A03 final audit assembly.
   d. Validation leg per the r39 isolation-replay protocol — isolated copy,
      never in-tree (§C8).
   e. Telemetry: `observed-dispatch.json` + `inputs/` from the swarm result
      (S02 §2 template); `availability-close-40.json` ONLY after
      `validation.json` lands, sha-pinning the declared record it closes
      (S02 §2.3).
   f. SCORECARD rows → `LOG.md` append (including committing the
      amendment-7 append at `LOG.md:3763-3771`) **last**: a round is not
      admitted to LOG.md while its availability record owes its closing
      snapshot (AGENTS.md close-what-you-open). Then `MANIFEST.json`
      rounds[] entry + fleet `.ufo/reports/round-40/kotodama.md`.
   Admission bar (REGIMEN.md:42-43): every claim verifies + no axis harmed;
   C's sweep-green and Ca's ≥28 owner-complete rows are measurable only
   post-apply (a); A's thresholds land with (c).

## Owed

- Not owed by this seat; open dependency set at stamp: K02, C02–C07, Ca01,
  Ca02, Ca04, A03, R01, R02, S01 (gates per §3.1–3.5).
- C05/integrator: basename-couples confusion check for the E1 filename
  choice (§C1, to-verify vs `reports/round-39/calib/basename-couples-policy.md`).
- A03: carry the corrected r37 telemetry count (5, not ×6) into the final
  audit assembly (§C5).
- Ca01: fold-in set §C3 is exhaustive as of this stamp — any finding landed
  after X00's cut (e.g. from R01/R02) joins via the same filed-row route.

## Citations

- `reports/round-40/targets.json:4-9` (shared_rules), `:11-180` (24 seat out
  paths, missions); `reports/round-40/claims.json:7` (baseline), `:13-30`
  (C/Ca/A), `:23,29` (runner counting commands), `:32-33` (non_goals).
- `reports/round-40/plan/P01-plan.md:140-160` (§4 routes the binding matrix
  to X00; collision control), `:39-70` (C steps + C04 fallback).
- C1/C2: `reports/round-40/cov/C01-entry-1.md:3,142-147` (proposed filename,
  blind-authoring reconciliation, Owed); `reports/round-40/scout/K03-gaps.md:23-34`
  (collision table + proposed names), `:60-153` (E1–E4 scopes/sources),
  `:166-177` (§5 audit criteria, routed-not-absorbed, byte-consistency duty
  to C01–C04/C06).
- C3/C4: `reports/round-40/calib/Ca03-receipt.md:26-72` (§3 per-row
  dispositions), `:74-96` (§4 N1–N7, 31≥28 arithmetic, grok-403 exclusion),
  `:97-111` (§5 owner-completeness threat, no padding), `:113-131` (§6
  next-touch table incl. r46 audit-only), `:169-189` (Owed: schema decision,
  runner obligations O10/N7).
- C5: `reports/round-40/scout/K01-touched-census.md:54-66,148-158` (r37
  instruments, telemetry "5 files", census totals), `:160-165` (Owed overlap
  note); `reports/round-40/adj/A01-audit.md:26` (r37 "telemetry ×6"),
  `:115-119` (Owed: reconcile via X00/integrator); measured this seat:
  `find reports/round-37/telemetry -type f | wc -l` → 5 (2026-10-19).
- C6/C7/C8: `reports/round-40/adj/A02-province.md:43-52,60-64` (F-A02-1 +
  route, Owed #6/#7); `reports/round-40/cross/X01-trades.md:43-51` (T3 r46),
  `:53-62` (T4 supersession), `:64-70` (T5 r40-partial labeling), `:72-82`
  (T6 runner ban), `:94-101` (F1), `:126-135` (F5/F6), `:138-141` (F7 G5),
  `:36-41` (T2 sweep wording).
- §3.6f ordering: `AGENTS.md` "Close what you open" (round not admitted to
  LOG.md while its availability record owes a closing snapshot);
  `reports/round-40/scribe/S02-telemetry-draft.md:91-107,120-131`
  (availability-close-40 gating + Owed set).
- `REGIMEN.md:23` (r46 read-only audit), `:42-43` (admission bar), `:9-23`
  (position schedule 41–46).
- Measured at stamp (2026-10-19, lane root, `TMPDIR=$PWD/.scratch`
  `PYTHONDONTWRITEBYTECODE=1`): `find reports/round-40 -type f | sort` → 12
  files (9 peer fragments + claims/targets/dispatch-declared);
  `git status --porcelain` → ` M LOG.md` + `?? reports/round-40/`;
  `ls corpus/knowledge/linguistics/` → 21 files, sort positions for all four
  proposed names confirmed clean (dialect-register-consistency between
  conlang-methodology/historical-linguistics; sacred-registers-liturgical-language
  between register-strata-attestation/semantic-fields-lexicon-building;
  taboo-*/translation-protocol-fidelity between syntax-typology/writing-systems).
  No `run-validation.py` executed; no corpus writes; this file is the only
  byte this seat produced.
