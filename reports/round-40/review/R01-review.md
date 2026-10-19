- Seat: R01 | reviewer | claim cross | date 2026-10-19 | baseline fd55e1f

# R01 — adversarial review of all three blocks (C coverage / Ca calibration / A adjacency)

Scope: `reports/round-40/targets.json` seat R01 — adversarial review of all three blocks.
Every load-bearing number below was re-measured by this seat from the filed bytes or
reproduced as a command; nothing is accepted from a sibling's self-audit without
reproduction. Wave snapshot at review close: **13 of 23 peer fragments landed** (P01, K01,
K03, C01, C02, Ca01, Ca03, A01, A02, X00, X01, S02 + this file's antecedents); absent at
cut: K02, C03–C07, Ca02, Ca04, A03, R02, S01 — their absence is recorded under Owed, not
treated as defect (r39 R01-4 precedent). No `reports/round-*/run-validation.py` was
executed anywhere, in-tree or otherwise; no replay; no re-freeze; no corpus staging; this
seat wrote only this fragment plus disposable scratch. Readings 2026-10-19 at HEAD
`fd55e1fdfd6cc684f121fd02f32eb5cdd4c88106` == declared baseline; `git status --porcelain`
→ ` M LOG.md` (parent-owned amendment-7 append, `LOG.md:3763-3771`) + `?? reports/round-40/`
only — **zero corpus staging at review close** (X01 F5 watch-item holds). Findings are
filed for the integrator to disposition; this seat certifies no claim and files no
admission verdict (`REGIMEN.md:42-43`).

## 1. Verdict summary

**No fabrication found.** Every sweep count, digest pin, and line anchor I checked in the
landed fragments resolves to real bytes; three precision defects and one completeness gap
are filed below. The round's substantive adversarial yield is in the Ca block.

| fragment | hunt result | findings filed here |
|---|---|---|
| K01 census | clean — per-window diff counts reconcile with git (74 A / 5 M collapsed over fa90c77..fd55e1f == 75+42+32 A / 3+4+3 M per-window) | R01-40-6 (r37 telemetry count) |
| K03 gaps | clean — all spot-checked anchors and sweeps reproduce | none |
| C01 entry 1 | clean — all 7 sweep commands reproduce exactly | R01-40-5 (filename + K03-scope adjudication) |
| C02 entry 2 | clean — sweeps reproduce; staged digest reproduces under a stated convention | R01-40-4 (digest convention), R01-40-11 (duplicated self-audit bullet) |
| Ca03 receipt | clean — N7 diff independently confirmed by this seat | R01-40-3 (R36-D-DECLARATION conflict, adjudicated) |
| Ca01 queue-v2 | mechanically valid (§4); census defects found | **R01-40-1 (fold-in gap, major)**, R01-40-2 (null-receipt count) |
| A01 audit | clean — git cross-checks pass; one count corrected | R01-40-6 |
| A02 province | clean — F-A02-1 anchors verified live by this seat | none |
| X00/X01/P01/S02 | conformance posture verified; no violations found | R01-40-7 (F1 arithmetic), R01-40-8 (class-vocabulary tension, softened) |

## 2. Claim C (coverage) — before-state exact; entries 1–2 clean; two open adjudications

**Before-state verified exactly as declared:** linguistics 21
(`ls corpus/knowledge/linguistics/*.md | wc -l`), total 216, partitions 94/25/21/23/29/24,
README rev 2.2 (`corpus/README.md:5`), totals line `:518`, footer `:520-522`, README sha256
`e73dc971c80207640c90eb671e738a24f2e02561245336f75fb6d5220240181a` (recomputed — matches
A01 §3's sweep-receipt pin). No drift between `claims.json:16` and the tree.

**C01 (`cov/C01-entry-1.md`) — fabrication hunt clean.** All sweep numbers reproduce
exactly as quoted: `treadmill` → 4 files; `minced` → 3; `"ordering test" / "sound-law
bracket" / "bracketing"` → 0/0/0; `read-off` → 1 file (`civilizations/parthia.md`);
`grep -n -i taboo language-contact.md` → 0. K03's load-bearing anchors reproduce
(`politeness-taboo-euphemism.md:80,102,106,118`; `sociolinguistics-registers.md:64` with
Kerswill & Williams). Boundary management is real, not decorative: the entry consumes the
politeness ladders as inputs and routes document-dating to `synthesis/taboo-euphemism-lifecycle.md`
§10, matching K03's CONDITIONAL-PASS scope; no restatement of `politeness:80-118` found.
Single 4-backtick outer fence, no internal fence lines (measured). Couples 9/9 resolve
 (`ls`-checked this seat against the named paths — all exist at HEAD).

**C02 (`cov/C02-entry-2.md`) — fabrication hunt clean.** Sweeps reproduce exactly:
`founder effect` → 1 file (`synthesis/migration-founder-effects.md`); `new.dialect` → 0;
`second.life` → 0; `anti-society` → 5 hits in exactly 3 files at the claimed lines
(`linguistic-anthropology.md` ×3, `register-lexicon-ceilings.md:12`,
`dialect-faction-map-workflow.md:202`); `koineization` → exactly the 5 claimed files;
`focusing` → 1 hit (`dialect-faction-map-workflow.md:94`). Trudgill (1986) is registered
on `sociolinguistics-registers.md:13` (same line as 1974/1972 — locator accurate);
Chambers & Trudgill `:14`, Milroy `:15`, K&W `:16` all verified. Authored directly on
K03's binding E2 scope with the consistency gate explicitly routed-not-absorbed (`- scope:`,
§6, §10) — the cleanest scout-conformance in the wave so far.

- **R01-40-4 (minor — digest convention unstated):** C02's self-audit pins the staged
  entry at 33,090 bytes / 129 lines / sha256 `e0ea25439192…`. My fence extraction gives
  33,091 bytes / 130 lines, sha `eb5f75d7ae59…`; **minus exactly one trailing newline the
  pin reproduces byte-exact** (measured both). The pin is real, but the
  trailing-newline-stripped convention is not stated in the fragment — the same defect
  class as r39's R01-8/R01-9. C05 must audit with (or explicitly record) this convention,
  or a false digest mismatch will be filed at audit time.
- **R01-40-5 (adjudication — E1 filename + scope):** C01 proposes
  `taboo-strata-lifecycle.md` (authored blind, before K03 landed, declared in its Owed);
  K03 proposes `taboo-euphemism-lifecycle-stages.md` for the same slot. X00 §C1 already
  routes the filename to the integrator; this seat adds two constraints on the ruling:
  (a) X00's basename-confusion warning is right — K03's name is the synthesis basename
  plus `-stages`, the exact shape the r39 basename-couples fallback muddles; prefer
  maximal distance from `synthesis/taboo-euphemism-lifecycle` when picking.
  (b) C01's entry is an stratum-ordering read-off, while K03's binding E1 scope named
  per-stage diagnostics/triad/divine-name split/cross-domain spread and routed the
  dating-instrument angle away. C01 does not restate the neighbours and routes document
  dating to synthesis §10, so CONDITIONAL PASS is defensible — but **C05 must rule on
  scope conformance, not assume it** (K03 §5 makes non-restatement an audit criterion).
  If C05 rules C01 off-scope, the entry re-slots as a candidate and claim C lands 3/4
  honestly rather than forced (P01 §1.3's own fallback).
- **R01-40-11 (note — C02 self-audit):** the "Head-block fields present" bullet appears
  twice verbatim (C02 lines 140 and 142). Editorial only; both copies say the same thing.

Neither landed entry has been audited by C05 or independently verified by C07 — both
absent at this cut. **Claim C's own threshold ("audit 4/4 PASS") is unmet at review time**
(R01-4 precedent applies verbatim); the integrator must not apply any entry until C05
lands, and C06's delta (also absent) must re-derive rows from the FINAL filename set
(X00 §C1 rule c).

## 3. Claim Ca (calibration) — the round's real findings live here

**Before-state verified:** `reports/round-37/op/defect-queue.json` = 24 rows, three
families (12 named census / 5 `id: null` unassigned / 7 r36-r37 findings), exactly as
Ca03 §2 and Ca01 §2 describe; parent digest `5cf827e2dd17b638acf023b1c6423b0602ba88e3c08d9698b68bae6c6cc60d5d`
recomputed — matches Ca01's `parent_sha256_at_assembly`.

**Ca01's v2 draft passes every mechanical check Ca04 will run** (this seat ran them
first, on the fenced JSON): strict JSON parse OK; **33 rows ≥ 28**; **0 duplicate ids**;
**every row has non-empty owner/reason/next_touch**; field set identical to the r37
queue's; class vocabulary exactly `{carried-with-owner, fixed-with-evidence}` with the new
class declared in `notes`; **no row takes an r46 implementation next-touch** (X00 §C4 /
X01 T3 satisfied); `census_coverage` keeps `K02_r40_census_rows_seen: null` with the
absence reason rather than an inferred count. The five `id: null` rows carry minted
`R37-O01-CAND-*` ids whose next_touch-text mapping to the filed rows is 1:1 and coherent
(each mapping matches its source row's operative sentence). The WORSENED markers are
real: I re-measured `runner_sha256: null` in r38 `validation.json:130` and r39
`validation.json:126`, and the r39 runner's absolute ROOT at `:5` + `os.chdir` at `:13`
with the stale "Round-38 acceptance runner." docstring at `:2` — the six-runner
absolute-ROOT streak (r34–r39) and `r39-runner-root-regression` row are accurate
(locator correction adopted from R02-3, see §7; this review's first draft also carried
the `:12` misread).

- **R01-40-1 (major — fold-in completeness):** the v2 is **missing five rows the round's
  own connector matrix mandates**. X00 §C3 requires (b) Ca03 §4's N1–N7, (d) A01's
  `.scratch/c05/c05-audit.py` durability row (digest filed at
  `reports/round-39/cov/C05-audit.md:30`, bytes ephemeral), and (e) A02's F-A02-1
  (`examples/culture-d4/components/13-register-law.yml:57` stale enforcement prose,
  filed at `adj/A02-province.md:43-52` with route "pointer to calib/Ca01-queue-v2.md").
  Ca01 (cut before A01/A02 landed; its source set names neither fragment) folds N1 ✓,
  N2 ✓, N4/N5 ✓ but **omits N3** (r38 argot-gate digest supersession of the r30 pins —
  Ca03 §4 N3), **N6** (the corpus couples-phantom repair rollup: X26-1
  `../linguistics/phonology-sanity.md` ×2 at `verification/label-channel-routing-verification.md:14`,
  the 3 never-written seeds at `linguistics/language-contact.md:7`, the 2 D1 phantoms —
  Ca03 §4 N6), **N7** (r39 `validation.json` named_findings/limits duplicated from r38
  verbatim, including the grok-403 route deviation inapplicable to r39's zai 16/16
  dispatch — Ca03 §4 N7, independently confirmed by this seat by reading both receipts:
  r38 `:112-127` ≡ r39 `:108-123`), **A01's durability row**, and **F-A02-1**. The count
  threshold survives (33 ≥ 28) only because Ca01's independent finds (frozen-row census,
  O02/O08 fragment defects, stray-staging, review-disposition rows) are legitimate — but
  the claim's substance ("the r38/r39 findings incorporated", "every finding") is **not
  met by this draft**. Ca02's ≥30% origin sample will not catch composition gaps; R02's
  dedicated hunt is the designed second gate. Required: Ca01 (or the integrator at
  assembly) folds the five rows — each already has origin, owner, and next-touch text
  written in Ca03 §4 / A01 Owed / A02 §4 — or records each omission with owner and
  reason. Note F-A02-1 is an **r40** finding, so its absence is a fold-in sequencing
  gap, not an r38/r39 hunt failure; N3/N6/N7 are the hunt failures.
- **R01-40-2 (minor — census undercount):** Ca01's O10 row and headline say **three**
  receipts carry `runner_sha256: null` (r36 carried; r38 `:130`; r39 `:126`). Measured:
  **four** — r37's own receipt is also null (`reports/round-37/validation.json:148`).
  The "missed twice" phrasing survives (the r37 queue and its receipt were filed in the
  same round, so r38/r39 are the two post-filing misses), but the census count is wrong
  and should read four at landing.
- **R01-40-3 (adjudication — Ca01 vs Ca03 on R36-D-DECLARATION):** Ca03 §3 row 4 calls
  it overdue (reading the row's boilerplate "fields completed at the r38 census cut" as
  a queue-census promise); Ca01 classifies it `fixed-with-evidence` at r38 (the r36-D
  family reading: the corrected scoped claim the row demanded is r38's admitted claim D).
  This seat adjudicates **toward Ca01**: all three R36-D-* rows share identical boilerplate
  reasons in the filed queue (`defect-queue.json:42-81`), the family interpretation
  matches the r36 D-rejection record ("stale premise"), and Ca03's reading would leave
  the row un-actionable. The integrator rules; the disagreement is filed, not silent
  (Ca03 §8 already requires exactly that).
- **R01-40-8 (note — class-vocabulary tension softened):** P01 §2.4 planned "class
  vocabulary ⊆ r37 queue's existing classes"; Ca01 introduced `fixed-with-evidence`.
  Ca01's `notes` justify it, and the r37 queue's own `notes` field already used the term
  ("R34-N1 is fixed at r35 (fixed-with-evidence …)", `defect-queue.json:5`) — so the
  extension is attested-in-v1 vocabulary, not an invention. Ca04 should check the class
  set against **both** the v1 row classes and the v1 notes, and the landed `notes` must
  keep Ca01's justification.
- Supersession hygiene (X01 T4): the v2 bumps the schema string to
  `kotodama-defect-queue-v2` and names its parent + parent digest — correct
  new-row discipline; the integrator's LOG/SCORECARD row must name v2 as the queue's
  current revision so future rounds cite it, not the stale v1.

## 4. Claim A (adjacency) — census cross-checks pass; PROVINCE holds; one count corrected

- **K01's census reconciles with git as run by this seat:** per-window adds/edits
  (75+3, 42+4, 32+3) are consistent with the collapsed `fa90c77..fd55e1f` view (74 A / 5 M
  — per-window sums double-count shared surfaces, correctly labeled as per-window in
  K01 §Census totals); the "15 new corpus entries" birth-commit attribution
  (10@ce103bf + 1@57c8409 + 4@fd55e1f) matches `git log --diff-filter=A`; `examples/`
  empty across the window; frozen/lessons boundaries held.
- **R01-40-6 (minor — census count):** A01 §1 lists r37 telemetry as "×6"; measured
  `find reports/round-37/telemetry -type f | wc -l` → **5** (close, declared, observed,
  inputs/claims, inputs/targets). X00 §C5 found the same; A03 must carry the corrected
  count into the final assembly. The surface verdict (GREEN, closing snapshot present)
  is unaffected.
- **A02's PROVINCE re-verification holds under adversarial re-check:** PROVINCE.md
  sha256 `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` ==
  `git show HEAD:PROVINCE.md` (recomputed); partition census matches; the contract file
  digest claim is consistent with r37's pin. **F-A02-1 verified live by this seat:** the
  component's `law_binding.enforcement` at `13-register-law.yml:57` asserts the era leg
  "is specified and unimplemented … has no era concept", while the landed argot gate
  carries the RL-8 era leg at `tools/gates/argot-derivation-gate.py:670-692` emitting
  `D4L-ARGOT-ERA` (grep count → 5, as A02 and Ca01 both report). A02's precision holds:
  "no gate executes these rows" remains literally true (law rows carry no `stage` key and
  the leg skips them by design, `:676`), only the "unimplemented/no era concept" half is
  now false. The finding is correctly routed (packet change → re-freeze-owning window,
  operator-gated), not absorbed.
- Claim A's "zero unfiled bleed" is **not yet closeable**: the r40 slice of the census is
  partial by construction at any seat cut (X01 T5), A03 (final assembly + independent
  verification) had not landed, and the wave's remaining fragments are exactly the kind
  of surfaces the audit must sweep at close. A01's Owed chain (K01 reconciliation via
  X00 §C5 — discharged; A03 verification) is the right closure path.

## 5. Cross-block conformance

- **Runner ban holds across the wave:** no landed fragment claims to execute any
  `reports/round-*/run-validation.py`; Ca/A's declared counting commands remain
  integrator-only-in-isolated-copy (X00 §C8, X01 T6). Ca03 §7's "to-verify at validation"
  wording is the correct seat-side posture. The round-40 runner obligations (relative
  ROOT, `runner_sha256` leg, round-specific named_findings) are now pointed at by four
  queue rows — the integrator must treat them as this round's own close gates
  (R01-40-1's N7 and R01-40-2 make them admission-relevant, not just hygiene).
- **r39's stale receipt (N7) is real and load-bearing:** this seat independently read
  both `validation.json` files — the `limits` and `named_findings` arrays are identical
  strings, and r39's own telemetry (`observed-dispatch.json`) proves the grok→devin
  record is inapplicable to r39 (zai lane, 16/16, route as declared). This is a filed
  bytes defect: never edit the receipt; the row plus a correction record is the fix.
- **X01 F1 (lowest-axis arithmetic):** claims.json's "Adjacency (3); coverage and
  calibration follow (3-4)" is imprecise — measured SCORECARD counts are coverage 3 =
  adjacency 3 (calibration 4, depth 3, operability 5). Claiming A still satisfies the
  lowest-non-paused-axis rule; the wording should not be quoted as arithmetic elsewhere.
- **Telemetry posture (S02):** partial sampling labeled partial; worker counters stay
  null-with-owner; the closing snapshot is correctly self-declared owed until
  validation.json lands (AGENTS.md close-what-you-open) — X00 §3.6f's ordering
  (LOG.md last) encodes it correctly.
- **Corpus hygiene:** zero staged corpus bytes at review close (`git status` scoped);
  the r39 stray-staging row's "third instance escalates" tripwire is armed and untripped.

## 6. Required integrator actions (ordered)

1. **R01-40-1**: fold the five missing rows (N3, N6, N7, A01 durability, F-A02-1) into
   `defect-queue-v2.json` at assembly — or record each with owner + reason. R02's hunt
   should reconcile against this review's list, not only against Ca03 §4.
2. **R01-40-2/R01-40-3**: correct the null-receipt count to four; record the
   R36-D-DECLARATION adjudication (this seat's recommendation: Ca01's ruling).
3. **R01-40-4**: C05 audits C02 at the pinned digest **minus trailing newline** (or
   re-pins under a stated convention); same check for C01/C03/C04's staged digests as
   they land.
4. **R01-40-5**: integrator fixes the four filenames (X00 §C1), preferring basename
   distance from `synthesis/taboo-euphemism-lifecycle`; C05 rules C01's scope conformance
   against K03 §5 before any entry is applied.
5. **R01-40-6**: A03 carries the r37-telemetry-5 correction into the final audit assembly.
6. Hold claim C unapplied until C05 + C06 + C07 land; hold Ca unadjudicated until Ca02 +
   Ca04 + R02 land; hold A unfinalized until A03 lands. Absences recorded under Owed
   below.

## 7. Addendum — late landings at this seat's close (~15:0xZ): R02 + C03

Wave count at review close: **15 of 23 peers** (adds `review/R02-review.md`,
`cov/C03-entry-3.md`). Still absent: K02, C04, C05, C06, C07, Ca02, Ca04, A03, S01.

- **R02 convergence:** R02-1 finds the v2 missing exactly N3/N6/N7 — the same three
  r38/r39-origin rows as my R01-40-1. **R01-40-1 is strictly broader**: my five-row list
  adds A01's `.scratch/c05/c05-audit.py` durability row and A02's F-A02-1 (both r40-origin,
  both X00 §C3(d)/(e) mandates; R02's stamp predated the A-fragments). R02-2 additionally
  widens N7 to include the receipt's stale CO `route_deviation` block
  (`reports/round-39/validation.json:47-58`, declared xai/grok vs r39's zai 16/16) —
  verified by this seat against r39's own telemetry; the correction row should name all
  three stale surfaces (CO block, named_findings, limits).
- **R02-4 counter-adjudication:** R02 recommends keeping R36-D-DECLARATION **carried**
  (Ca03's reading) until the r41 re-census can flip it on the v2's own evidence, arguing
  a `fixed` class on a disputed reading launders a disagreement; my §3 leaned Ca01
  (fixed-by-r38-claim-D). Both are filed; the integrator picks. This seat notes R02's is
  the conservative disposition; either way the disagreement must stay visible in the
  landed v2's notes.
- **R02-3 adopted:** the r39 `os.chdir` locator is `:13`, not `:12` — fixed in this
  review's §3 and Citations (my first draft repeated Ca01's off-by-one).
- **R02-5 noted (not re-verified in full):** C01's Baugh & Cable 5th-edition registration
  sits at `language-contact.md:4`, not `:3`; the work is registered and the edition
  choices are internally consistent — C06/audit-time one-line fix.
- **C03 hunt: clean.** All four pinned source digests recompute exactly
  (`cultural-translation-protocol.md` `fb5d705b…`, `verification-method-overview.md`
  `f52708d9…`, `two-reader-interop-agreement.md` `daebba3ae…`, `naming-systems.md`
  `d972a1d6…`); `thick translation` → exactly 1 file corpus-wide as claimed; in-partition
  absence sweeps re-measure K03's 0-file result; single 4-backtick fence, no internal
  fence lines. **C03's staged digest pins under the OPPOSITE convention from C02's**:
  C03's `2289a9b7…` / 47,417 bytes reproduces **as-captured (trailing newline included)**,
  while C02's `e0ea2543…` reproduces only **minus the trailing newline** — both verified
  by this seat. R01-40-4 therefore upgrades from "convention unstated" to "conventions
  diverge across entries in the same wave": C05 must extract per-fragment and record
  which convention each pin uses, or two of the four audits will misfire in opposite
  directions.
- C03 conformance positives worth keeping: topic authority is X00 §C2's reconciled
  mapping (not an independent pick); false-positive sweep classes are reported rather
  than omitted (its own §2 table); source list carries per-source sha256 pins — the
  strongest provenance shape in the wave so far. Its `gloss`/`interpreter` class
  dispositions and the assert/license boundary vs `two-reader-interop-agreement.md`
  match K03's E3 scope; the fidelity criteria are new surface, not protocol restatement
  (spot-checked against the protocol anchors C03 cites at `:16,:132,:192`).

## 8. Final addendum — second landing wave (~15:0x–15:1xZ): Ca02, A03, C04, C06, Ca04

Wave count at close: **20 of 23 peers**. Still absent: `scout/K02-queue-scout.md`,
`cov/C05-audit.md`, `cov/C07-verify.md`, `scribe/S01-integration-draft.md`.

- **Ca02 (`calib/Ca02-verify.md`)**: sampled 24/33 rows (72.7%) against origins — all
  MATCH, both worsening claims re-derived first-hand; independently found the same
  `:12`→`:13` chdir locator nit (its N-1 = R02-3 = this review's adopted correction).
  Its sample did not test fold-in completeness (origin-sampling mission) — exactly the
  gap R01-40-1 fills. Note: Ca02 row 10 repeats Ca01's "three receipts" null count
  (r36 `:167`, r38 `:130`, r39 `:126`); **R01-40-2 stands** — r37 `validation.json:148`
  is a fourth null its sample did not probe.
- **Ca04 (`calib/Ca04-consistency.md`)**: 20/20 consistency checks PASS on the fenced
  draft (strict parse, no dup keys, 33 rows, classes {carried-with-owner: 25,
  fixed-with-evidence: 8}, 33/33 unique ids, owner-complete, field-set parity with v1,
  zero route-backs to r33–39, census arithmetic 24+5+4=33). Corroborates this review's
  §3 mechanical validation independently. Draft-block landing digest pinned
  (`3edb4e52…`, 33,616 bytes). Mission is structure-only — completeness (R01-40-1)
  is by design outside its lane, and remains open.
- **A03 (`adj/A03-verify-assembly.md`)**: every A01/A02 command reproduced; couples
  check refined to 67 refs / 55 distinct / 0 dangling; K01↔A01 reconciliation closed
  with no risk-class disagreement; two A01 line-cite typos filed. **A03's Owed now
  lists F-A02-1 and the `.scratch/c05` durability row as queue-v2 owed items** —
  converging with R01-40-1 — and adds a third durability candidate (the r39 couples
  re-check ran as an unfiled inline script). The assembled claim-A threshold read is
  correctly caveated: the r40 census row closes only at integration re-census.
- **C04 (`cov/C04-entry-4.md`) hunt: clean.** All six sweep counts reproduce exactly
  (`event-typed` 0; `recitation accuracy` 1; `liturgical fossilization` 2;
  `sacred register` 7; `recitation` 52; `liturg` 86 corpus-wide / 13 of 21 linguistics —
  all re-run by this seat). K03's E4 scope is implemented with the unrouted
  verification gates explicitly carried open; the sweep caveat (post-landing self-match)
  is honestly stated.
- **C06 (`cov/C06-delta-receipt.md`) arithmetic: correct.** The totals leg is 216→220
  (the mission's "212→216→220" is explained: 212→216 was rev 2.2's landed move —
  `corpus/README.md:9-10`); after-vector 25/23/25/29/24/94; four rows with measured
  anchors; the C01-vs-K03 filename divergence is recorded, not smoothed (`:290`); the
  apply probe ran on a **scratch copy** with a redirected sweep (220 rows vs 220
  files) — the live tree stayed untouched, so X01 T2's wording discipline holds
  ("sweep green" remains the integrator's post-apply leg).
- **Net effect on my findings**: R01-40-1's five-row list is now mandated by two
  independent seats (R02 for three, A03's Owed for two) plus this review; the
  `:13` locator fix is triply confirmed (R02-3, Ca02 N-1, this seat). All other
  findings stand as filed. **Claim-gating absences at close**: C05's pre-landing
  audit (claim C's own threshold), C07's independent verification, K02's census
  cross-check (census_coverage stays carried-with-owner), S01's dossier — each gates
  its claim per X00 §3 and must land (or be recorded absent with owner+reason)
  before the integrator finalizes.

## 9. K02 landed last (~15:1xZ) — census agreement, same blind spots

`scout/K02-queue-scout.md` independently agrees with every Ca01 headline delta (§7),
confirms the six-runner streak and the verbatim-landing of the basename policy, and adds
a correct precision note (4-row row-local frozen-row census vs the 6/10 row-blindness
figures). Two review-relevant facts: (a) K02's "every finding" inventory **also** lacks
the five rows of R01-40-1 (N3/N6/N7/F-A02-1/`.scratch` durability) — the completeness gap
is systematic across both Ca-block census seats, and R02 + this review are its only
catchers in-wave; (b) K02 §7 repeats Ca01's "three-null receipts" reading — R01-40-2
(four: r36 `:167`, r37 `:148`, r38 `:130`, r39 `:126`; the last three re-grepped by this
seat, r36/r37 by Ca02's row 10 and this seat's grep loop respectively) stands. The
minted-id mapping cross-check K02 owed is satisfied (its §7 + Ca02's row 9 both verify
it). With K02 in, `census_coverage`'s carried owner-check is dischargeable at
integration; C05, C07, S01 remain the open claim-gaters.

## Owed

- Absent at this seat's cut (concurrency, not defect; each gates a claim per X00 §3):
  `scout/K02-queue-scout.md`, `cov/C03-entry-3.md`, `cov/C04-entry-4.md`,
  `cov/C05-audit.md`, `cov/C06-delta-receipt.md`, `cov/C07-verify.md`,
  `calib/Ca02-verify.md`, `calib/Ca04-consistency.md`, `adj/A03-verify-assembly.md`,
  `review/R02-review.md`, `scribe/S01-integration-draft.md`. My §3 fold-in list is
  R02's starting inventory; my §2.1/2.2 hunts are evidence toward C05, not substitutes.
- This review's main body covers fragments landed through ~14:55Z 2026-10-19; §7's
  addendum covers R02 + C03 (~15:0xZ). Fragments landing after that cut are the
  integrator's validation leg + R02's to review.
- `to-verify`: whether K02's census (when it lands) disagrees with any Ca01 minted-id
  mapping — `census_coverage` already carries the check.
- This seat certifies neither claim; admission stays the integrator's (`REGIMEN.md:42-43`).

## Citations

- Contract: `reports/round-40/targets.json` seat R01 + shared_rules; `reports/round-40/claims.json:13-30` (C/Ca/A), `:32-33` (non_goals).
- Before-states (all re-measured this seat): `ls corpus/knowledge/linguistics/*.md | wc -l` → 21; partition census 94/25/21/23/29/24 = 216; `sha256sum corpus/README.md` → `e73dc971…`; `sha256sum reports/round-37/op/defect-queue.json` → `5cf827e2…`; `reports/round-37/op/defect-queue.json:11-252` (24 rows; families `:12-131`, `:132-181`, `:182-251`; boilerplate reasons `:42-81`; v1 notes fixed-with-evidence `:5`).
- C01/C02 hunts: sweep commands and counts quoted in §2 — all re-run by this seat 2026-10-19 (`treadmill` 4 / `minced` 3 / bracketing 0 0 0 / `read-off` 1 = `civilizations/parthia.md` / language-contact taboo 0; `founder effect` 1 / `new.dialect` 0 / `second.life` 0 / `anti-society` 5-in-3 / `koineization` 5 files / `focusing` 1); C02 digest variants (33,091/`eb5f75d7…` as-captured; 33,090/`e0ea2543…` minus trailing NL — target); `sociolinguistics-registers.md:13-16` source registrations read.
- Ca01 mechanical validation (this seat, fenced-JSON parse): rows 33, dup ids 0, owner/reason/next_touch complete, classes {carried-with-owner, fixed-with-evidence}, no r46 next-touches, field set == r37's, `K02_r40_census_rows_seen: null`.
- Runner/receipt defects: `reports/round-37/validation.json:148`, `reports/round-38/validation.json:130`, `reports/round-39/validation.json:126` (`runner_sha256: null` ×4); `reports/round-39/run-validation.py:2,5,13` (stale docstring, absolute ROOT, chdir — `grep -n chdir` → `13:os.chdir(ROOT)`); r38 `validation.json:112-127` ≡ r39 `:108-123` (limits + named_findings verbatim); `reports/round-39/telemetry/observed-dispatch.json` (zai 16/16, route as declared).
- Fold-in sources: `reports/round-40/calib/Ca03-receipt.md:74-96` (N1–N7), `reports/round-40/adj/A01-audit.md:62-66` + Owed (`.scratch/c05` durability), `reports/round-40/adj/A02-province.md:43-52,60-64` (F-A02-1 + route), `reports/round-40/cross/X00-connector.md:56-70` (§C3 mandate).
- A-block cross-checks: `git diff --name-status` per window and collapsed (74 A / 5 M over `fa90c77..fd55e1f`); `find reports/round-37/telemetry -type f | wc -l` → 5; `sha256sum PROVINCE.md` == `git show HEAD:PROVINCE.md | sha256sum` → `05b34a57…`; `examples/culture-d4/components/13-register-law.yml:57`; `tools/gates/argot-derivation-gate.py:670-692` + `grep -c D4L-ARGOT-ERA` → 5.
- Peer fragments read in full: K01, K03, C01, C02, Ca01, Ca03, A01, A02, X00, X01, P01, S02 (all under `reports/round-40/`).
- Commands run by this seat: all quoted outputs above; `python3` fenced-block extraction/digest + JSON validation; no round runner, no replay, no re-freeze, no git mutation, no corpus staging, no network, no installs.
