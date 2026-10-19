- Seat: R02 | reviewer | claim cross | date 2026-10-19 | baseline fd55e1f

# R02 — second review: defect-queue-v2 currentness (are the r38/r39 findings REALLY all in?) and the entry fabrication hunt

**Mission** (`reports/round-40/targets.json` seat R02): *"Second review: the queue-v2
currentness (are the r38/r39 findings REALLY all in?) and the entry fabrication hunt."*
Out path: this file only.

**Method.** Every load-bearing number below was re-measured by this seat from filed bytes
or the live tree at HEAD `fd55e1f` (2026-10-19, lane root,
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`). Nothing was accepted from a
sibling's self-report without reproduction. No `reports/round-*/run-validation.py` was
executed anywhere; no corpus byte staged; no filed byte edited; no git-mutating, network or
install action taken. This seat wrote only this file.

**Reviewed fragments** (what had landed at this seat's stamp, `ls` 2026-10-19 ~14:25–14:31Z):
`calib/Ca01-queue-v2.md`, `calib/Ca03-receipt.md`, `cov/C01-entry-1.md`,
`scout/K03-gaps.md`, plus the primary records (r37 queue, r38/r39 receipts and fragments,
LOG.md, corpus). Absent at stamp: K02 scout, C02–C04, C05/C07, Ca02, Ca04, X00, R01, S01 —
their absence bounds what this review can cover (## Owed).

---

## Part A — queue-v2 currentness (second review of `calib/Ca01-queue-v2.md`)

### A.1 What reproduces (Ca01's evidence, re-measured by this seat)

Every Ca01 HEAD measurement I re-ran returns exactly what the v2 records:

| Ca01 claim | my re-run | verdict |
|---|---|---|
| `runner_sha256: null` at r38 `validation.json:130` and r39 `validation.json:126` | `grep -c 'runner_sha256.*null'` → 1 and 1 | reproduced |
| r39 runner absolute ROOT + stale docstring | `head -12 reports/round-39/run-validation.py` → `ROOT = "/home/vgpnk/…"` at `:5`; docstring `"""Round-38 acceptance runner."""` at `:2` | reproduced (locator nit → R02-3) |
| duplicate H1 live | `grep -c '^# kotodama-shokunin corpus index' corpus/README.md` → **2** | reproduced |
| E3 placeholders gone | `grep -c '__E3_PLACEHOLDER__' corpus/README.md` → **0** (no match) | reproduced |
| O07 fragment 0 bytes | `wc -c reports/round-38/op/O07-scribe.md` → **0** | reproduced |
| R01-2..14 dispositions unrecorded | `grep -c 'R01-' reports/round-39/validation.json` → **0**; LOG.md r39 entry names R01-1's ruling only (`LOG.md:3750-3753`, "with R01-1's mechanism ruling") | reproduced |
| basename policy landed without Ca04's D1/D2 fixes | `grep -n 'block extraction\|blocker\|C12\|disposition' reports/round-39/calib/basename-couples-policy.md` → **no match** | reproduced |
| r39 stray corpus staging | LOG.md r39 entry: "a seat's stray `corpus/knowledge/verification/C03-draft.md` removed at integration (digest-proven provenance)" (`:3752-3754`) | reproduced |

**The 24→33 row accounting verifies.** The r37 queue carries exactly 24 rows (12 named
census rows `defect-queue.json:12-131`, 5 `id: null` rows `:133-181`, 7 later-origin rows
`:183-251`) — read in full by this seat. Ca01 accounts for all 24 (4 fixed + 1 of the
minted rows fixed, 19 carried/worsened/partially-addressed) and adds 9 new rows
(5 r38 + 4 r39). Row count 33 ≥ the claim's 28 threshold
(`reports/round-40/claims.json:24`).

**The minted-id mapping is real.** The five `R37-O01-CAND-*` rows map 1:1 onto the filed
queue's five `id: null` rows by next_touch text, and each minted row's origin cites a
candidate group that actually exists in `reports/round-37/op/O01-queue-draft.md:259-294`:
C01-F1..F6 + C03-couples-fire-fuel (the timekeeping group; the draft's "stale
201-file/28-term sweep at lines 4 and 8" matches Ca01's TIMEKEEPING row), R35-A-F1..F13,
OI-01..12, RC-2/RC-3/RC-34-3/RC-34-5/R36-README-PREDICTION-DELIVERY, and the
R34-N1/CO4/402 historical group. Verified line-by-line by this seat.

**The exclusions are precedented.** Ca01's `notes` deliberately keep telemetry deviations
(grok→devin, RL-8 host decision, r39 C05 re-dispatch) out of the queue — the r37 queue's
own `notes` set that rule ("the r36 D-rejection is a round record, not a defect
(excluded)", `defect-queue.json:5`), and Ca03 §4 independently applies the same exclusion.
Consistent; not a gap.

### A.2 **R02-1 (major): the v2 is NOT complete — three fold-in findings are missing**

The answer to the mission question is **no**. Ca03's fold-in inventory
(`calib/Ca03-receipt.md` §4, candidates N1–N7) and Ca01's 9 new rows overlap on 6 of 7 —
but three Ca03 candidates have **no row in the v2**:

- **N7 — receipt-fidelity defect (the big one).** The r39 receipt
  (`reports/round-39/validation.json`) carries r38's `named_findings` and `limits`
  **verbatim** (Ca03's §7 diff: identical strings, only `measured_at_utc` differs) —
  including "O07-scribe.md landed 0 bytes" (an r38 event) and the grok-403 route
  deviation. **This seat independently extends N7**: the receipt's cross/CO
  `route_deviation` block is stale too — it records `declared: "xai-oauth/grok-4.7-fast"`,
  `observed: devin/…`, `wave_shape: "22+10 = 32/32"` (`reports/round-39/validation.json:47-58`)
  while r39's own declaration is `zai-coding-plan / glm-5.3-flash`, 16 workers
  (`reports/round-39/claims.json:5-8`) and r39's own telemetry records zai 16/16 with
  actual route "zai-coding-plan lane … as declared"
  (`reports/round-39/telemetry/observed-dispatch.json`: `launched_workers: 16`,
  `completed_workers: 16`, `actual_route`). The r39 runner is a partial-constants update
  (round/baseline/claims updated; CO/named_findings/limits/docstring copied) — anyone
  folding "r39 named findings" or the r39 route **from the receipt** imports r38 facts.
  Ca01 avoided the trap in its own census but did not file the row. Filed bytes are
  immutable → this needs a correction-class row (owner: the r40 runner generation, per
  Ca03's disposition: round-specific named findings/limits/CO at authoring).
- **N3 — argot-gate digest supersession.** r38 moved the argot gate
  `b5406bcd… → 10c88433…`; the filed r30 digest rows are superseded forever and future
  register-leg audits must cite the new digest with that provenance (origin
  `reports/round-38/depth/D07-receipt.md` §5; Ca03 §4 N3). No v2 row carries it. (Ca01's
  R36-D-F6 row cites the live counters but does not file the digest-provenance obligation.)
- **N6 — corpus couples phantoms owed repair dispositions.** X26-1's
  `../linguistics/phonology-sanity.md` ×2, 3 never-written seeds at
  `corpus/knowledge/linguistics/language-contact.md:7`, and Ca04-D1's 2 phantoms — a
  rollup row with an integrator owner (origin `reports/round-39/calib/Ca03-basename-policy.md`
  Part 2 + Ca04 D1; Ca03 §4 N6). No v2 row carries it (Ca01's
  `r39-basename-successor-instrument` covers the instrument work, not the corpus-side
  repair dispositions).

With N3/N6/N7 folded the v2 is 36 rows; at 33 it clears the ≥ 28 threshold but fails the
claim's own standard ("the r38/r39 findings incorporated", `claims.json:20`) on a
completeness reading — and the round-40 claim Ca's `after_required` says the findings are
incorporated, not merely sampled. **Disposition: integrator folds the three rows (they are
fully drafted in Ca03 §4 with origins and dispositions) or files the disagreement.**

### A.3 R02-2 (finding, folded into R02-1): N7's scope is wider than its origin states

Ca03's N7 names `named_findings` + `limits` (`validation.json:118-123`). This seat's read
adds the **CO `route_deviation` block** (`:47-58`) to the same defect — see A.2 for the
evidence. The correction row should name all three surfaces, so the r40+ runner leg spec
cures them together.

### A.4 R02-3 (minor): chdir locator off by one in three v2 rows

Ca01 cites the r39 runner's `os.chdir` at `:12` (rows R36-ABSOLUTE-ROOT,
r39-runner-root-regression; evidence `:2,5,12`). Measured: `grep -n chdir
reports/round-39/run-validation.py` → **`13:os.chdir(ROOT)`**; `:12` is
`RENDERER_SHA_UNUSED = …`. `:2` (stale docstring) and `:5` (absolute ROOT) are correct.
Fix the locators in the v2 before landing; the substance of the rows is unaffected.

### A.5 R02-4 (major, adjudication): Ca01 and Ca03 disagree on R36-D-DECLARATION — filed, not absorbed

- **Ca01** (`calib/Ca01-queue-v2.md` row 4): `fixed-with-evidence` — "the corrected,
  scoped claim the row demanded is the admitted r38 claim D".
- **Ca03** (`calib/Ca03-receipt.md` §3 row 4): the row's actual demand — "fields completed
  at the r38 census cut" (`defect-queue.json:47`, owner "r38+ defect-queue completion
  (O05/O06 owners)") — **never executed**; no r38 defect-queue census exists (LOG.md
  r38 entry has none); verdict "overdue completion folds into the v2 assembly".

Both readings are defensible from the filed row's own ambiguity (r37
`defect-queue.json:42-51`). This review does not pick a winner: the row names both a
D-claim defect class and a census-completion promise. The conservative disposition — and
the one that keeps the v2's own census honest — is Ca03's: keep the row **carried** (the
census completion is *this round's* v2 landing, unverifiable until Ca02/K02 close), and
let the r41 re-census flip it to fixed-with-evidence with the v2 itself as evidence. The
integrator adjudicates; a `fixed` class filed on a disputed reading is how a queue
launders a disagreement (the round contract: disagreements filed, never absorbed).

### A.6 Second-order checks that pass

- Ca01's `census_coverage` keeps `K02_r40_census_rows_seen: null` with the absence reason
  (K02's scout absent, checked twice) — honest-null discipline per AGENTS.md, verified by
  this seat's own `ls` (K02 still absent at this stamp).
- Next-touch alignment (Ca01 §"Next-touch alignment") is consistent with
  `REGIMEN.md:13-23` (r41 codex verify, r42 devin, r43 zai-low, r44 antigravity,
  r45 antigravity-deep, r46 swe-2 audit) and with Ca03 §6's independent alignment; the two
  seats' assignments agree on every row they both touch (O10/O12/N1/N4/N5 to r41-r43;
  OI-02 to r45; re-freeze family deliberately loop-2/condition-gated per non_goals).
- The 4-row `recount-ledger-successor.json` fold (R37-Ca-05..08
  `reproduced-under-protocol`, Ca02-verified) is cited correctly; read by this seat
  (`:9-49`, all four rows, replay_commit `4a7aede`).
- O12/R36-ABSOLUTE-ROOT dedupe (canonical id + census alias, "no third id") matches the
  r39 X00-4 ruling as cited.

---

## Part B — entry fabrication hunt (`cov/C01-entry-1.md`, the only entry landed at this stamp)

### B.1 Verdict: no fabrication found

Every load-bearing citation I checked resolves to real bytes that say what the draft says.
Reproduced by this seat (all at HEAD `fd55e1f`):

- **Absence sweeps reproduce exactly**: `grep -ril treadmill corpus/knowledge/*/*.md | wc -l`
  → **4**; `minced` → **3**; `read-off` → **1**; `"ordering test" / "sound-law bracket" /
  "bracketing"` → **0 0 0**. All five counts equal the draft's `- gap filled:` claims.
- **Head-block provenance line**: `git log --oneline -1` → `fd55e1f round-39: admit C/Ca —
  verification partition 24 (216 total), isolation-replay protocol, basename-couples
  policy` — byte-identical to the draft's `- verified-at:` quote.
- **Source registrations all resolve**: Allan & Burridge 2006 **and** 1991 both at
  `politeness-taboo-euphemism.md:24`; Pinker 2007 ch. 7 at `:28`; Baugh & Cable 1993 4th
  ed. at `:29`; Mallory & Adams 2006 at `:30`; Rosa's Law at `:32` (and
  `synthesis/taboo-euphemism-lifecycle.md:15`); Hughes 1991 + Mohr 2013 at `:34`;
  Campbell 2013 at `synthesis:7`; Wilkinson 2022 at `synthesis:8`; Rösel 2007 JSOT 31(4)
  at `synthesis:9`; Tov 2012 at `synthesis:10`; Mishnah Yoma 6:2/Danby at `synthesis:11`;
  OED/etymonline *zounds* at `synthesis:17`; Thomason & Kaufman 1988 at
  `language-contact.md:4` (sources line) — all exactly as the draft's `- sources:` states,
  with the one locator exception below (R02-5).
- **Body anchors spot-checked and correct**: `politeness:75` (bìhuì missing-character
  dating), `:76` (sanction gradient), `:95` (algospeak), `:101` (medvědь / lokys /
  Mesikämmen), `:102` (zounds / sacrébleu / chikushō), `:103` (conquest strata), `:104`
  (Eumenides / Plouton / YHWH-Adonai-HaShem-G-d), `:127` (treadmill anti-overclaim),
  `:128` (in-world folk etymologies wrong on purpose); `synthesis:29` (no constant rate),
  `:62` ("S3 can persist without S4a; S4b and S4c can coexist"), `:121` (Y6:2
  speaker/place/occasion exception), `:122` (loss of utterance opportunity ≠ erased
  written record), `:150` (step 3 mechanism), `:152` (step 5 independent anchors),
  `:153` (terminus discipline; mandatory form constrains a compliant copy), `:156`
  (interval + confidence or "insufficient evidence"), `:163` (two-rival-euphemisms row),
  `:185` (stable endpoint); `historical-linguistics.md:3` (comparative method topic),
  `:7` (taboo routed away as couples destinations), `:233` (the taboo paragraph).
- **No-network honesty**: the draft claims no external source was resolved and carries the
  inherited-verification caveat explicitly (`- verified-at:` "Not done this round…"); no
  fabricated page numbers, DOIs, or consultation dates appear anywhere in the draft. The
  invented-data demonstration (§9) is declared NON-CANON and invented — as labeled.
- **Boundary compliance**: the draft reuses `politeness-taboo-euphemism.md` ladders as
  inputs and adds the sequencing instrument, exactly the non-restatement shape K03's audit
  criteria demand (`scout/K03-gaps.md` §5); the divine-name cluster K03 scoped for E1
  (Rösel/Tov/Mishnah) is present and correctly cited.

### B.2 R02-5 (minor, precision): one off-by-one locator

The draft registers Baugh & Cable "5th ed. at `language-contact.md:3`". Measured:
`language-contact.md:3` is the `- topic:` line; the `- sources:` line carrying
"Baugh & Cable (2002) *A History of the English Language*, 5th ed. (Longman)" is
**`:4`**. The work IS registered in that file (and the 4th ed. the entry actually uses is
registered at `politeness-taboo-euphemism.md:29` — also the edition
`politeness-taboo-euphemism.md:103` itself cites). One-character-class fix at C06/audit
time; not a fabrication. Note for the audit trail: the corpus registers Baugh & Cable in
three editions across three entries (1993 4th, 2002 5th, "6th ed. 2002" at
`semantic-fields-lexicon-building.md:4`) — the entry's edition choices are internally
consistent with what it cites.

### B.3 Reconciliation note (not a defect): entry-1 filename vs K03's proposal

C01 lands `taboo-strata-lifecycle.md`; K03 §2 proposed
`taboo-euphemism-lifecycle-stages.md`. Both seats flag the parallel-batch divergence (C01
under `## Owed`), and both names sort in the same slot (between `syntax-typology.md` and
`writing-systems.md`), so nothing downstream breaks — the integrator picks one name and
keeps the README row byte-equal to the landed head block. Recorded so the choice is
deliberate, not accidental.

### B.4 Coverage limit

C02–C04 and the C05/C07 audits had not landed at this stamp. The hunt above covers C01
only; the remaining three entries need the same treatment when they land (the sweeps and
source registrations verified here are reusable as the checklist).

---

## Owed

- **Fold N3/N6/N7 into the v2** (or file the disagreement with reasons) before the v2
  lands at `reports/round-40/op/defect-queue-v2.json`. Owner: integrator, from Ca03 §4's
  drafted rows + this review's A.2/A.3. After fold: 36 rows, all origin-cited.
- **Adjudicate R02-4** (R36-D-DECLARATION class) — carried vs fixed. Owner: integrator;
  recommended disposition in A.5.
- **Fix the `:12` → `:13` chdir locators** in v2 rows R36-ABSOLUTE-ROOT /
  r39-runner-root-regression before landing (A.4). Owner: integrator (applies to Ca01's
  fenced draft) or Ca01 in a correction fragment.
- **Fabrication hunt on C02–C04** + independent verification of C05's audit — next seats
  in the contract (C07's mission is exactly this); this review's B-checklist is the
  starting kit. Owner: C07/R-seats, then the integrator.
- **K02's queue scout** still absent at this stamp — Ca01's `census_coverage` null and
  owed-cross-check remain correctly open. Owner: K02.
- **to-verify**: whether any r39 record outside the files this seat grepped
  (`validation.json`, LOG.md, SCORECARD.md) records the N7-class staleness — if one
  surfaces, N7's row cites it as first-recorded instead. (Ca03's §4 N7 was the first
  record of it found by this seat.)

## Citations

- **Claims/rules**: `reports/round-40/claims.json:18-24` (claim Ca before/after/thresholds),
  `:32-33` (non_goals); `reports/round-40/targets.json:3-9` (shared_rules), `:147-158`
  (R02 seat row).
- **r37 queue (read in full)**: `reports/round-37/op/defect-queue.json:5-10` (notes +
  census_coverage), `:12-131` (12 named rows), `:133-181` (5 null-id rows),
  `:183-251` (7 later-origin rows); `reports/round-37/op/O01-queue-draft.md:259-294`
  (the five unresolved-candidate groups; the 201-file timekeeping note).
- **r38/r39 receipts**: `reports/round-38/validation.json:112-130` (limits,
  named_findings, `runner_sha256: null`); `reports/round-39/validation.json:47-58` (stale
  CO route_deviation — this seat's read), `:108-126` (duplicated limits/named_findings;
  `runner_sha256: null` at `:126`); `reports/round-39/claims.json:5-8` (zai declaration);
  `reports/round-39/telemetry/observed-dispatch.json` (`launched_workers: 16`,
  `completed_workers: 16`, `actual_route` zai as declared).
- **r39 runner**: `grep -n chdir reports/round-39/run-validation.py` → `13:os.chdir(ROOT)`;
  `:2` docstring, `:5` ROOT (this seat's head -12).
- **Round-40 fragments reviewed**: `calib/Ca01-queue-v2.md` (all 33 rows + summary table +
  alignment section), `calib/Ca03-receipt.md` (§3 row 4, §4 N1–N7, §6, §7 command
  transcript), `cov/C01-entry-1.md` (full), `scout/K03-gaps.md` (§2–§5).
- **This seat's re-measurements** (2026-10-19, lane root, `fd55e1f`): the table in A.1;
  the sweep battery and source-registration checks in B.1 (commands shown inline);
  `grep -rn "Baugh" corpus/knowledge/linguistics/` (edition/locator census);
  `find corpus -name "*sacred-kingship*"` → `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md`;
  LOG.md `:3745-3771` (r39 entry + amendment 7);
  `reports/round-39/calib/recount-ledger-successor.json:9-49`.
- **Prior precedent applied**: r39 `review/R01-review.md:15-34` (findings filed for
  disposition, verdict table), `:25-34` (the R01-1..R01-14 family Ca01's
  `r39-review-findings-disposition` row folds); r37 queue `:5` (round-record exclusion
  precedent); AGENTS.md availability rules (honest-null discipline).
