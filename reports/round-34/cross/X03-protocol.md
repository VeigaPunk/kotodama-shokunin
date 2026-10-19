- Seat: X03 | critic | claim cross | date 2026-10-19 | baseline da68a6d

# X03 — protocol critic: claim axes, lowest-axis rule, freshness pause, one-batch
shape, threshold checkability

**Mission** (`reports/round-34/targets.json`, seat X03): "Protocol critic: claims
distinct axes, lowest-axis rule (depth), freshness pause, one-batch shape,
thresholds checkable by a round-34 validator."

**Audit window:** 2026-10-19T07:02Z–07:12Z (`date -u +%FT%TZ` → `2026-10-19T07:10:11Z`).
Repo root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, HEAD
`da68a6d705e41f369f21e8607bfaab5b54077f84` (`git rev-parse HEAD`), env
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

**Method / boundary.** Read-only protocol audit. Executed only: (a)
`python3 -B reports/round-30/craft/box1-survey.py` (a print-only survey tool —
verified no write call in its source; not a round runner), (b)
`python3 tools/harness/receipt_guard.py --selftest` (a tool, not a runner), (c)
`python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md`
(read-only gate; post-run `git diff --name-only HEAD -- reports/` → 0 rows), and
(d) static greps. **No `reports/round-*/run-validation.py` was executed in-tree
or in a copy**, and `tools/exercise-handoff-e2e.py` was deliberately not run by
this seat (its write calls are confined to mirror/assembly dirs — `:442`,
`:1355`, `:1581-1610`, `:1752-1771`, `:1856` — but the D-claim legs own that
run). Durable output is this file only.

---

## Verdict summary

| # | mission item | verdict | key evidence |
|---|---|---|---|
| 1 | claims on distinct axes | **PASS** | `claims.json:20-66`; SCORECARD axis set `SCORECARD.md:3` |
| 2 | lowest-axis rule (depth) | **PASS under the r33 reading; literal reading currently unsatisfiable (P-1)** | `claims.json:18`; `reports/round-33/claims.json`; `SCORECARD.md:15,590,675-676` |
| 3 | freshness pause respected | **PASS** | `claims.json:19,69`; zero fetch/network in any seat mission |
| 4 | one-batch shape | **FAIL as declared — 64 declared vs 63 enumerated (P-2)** | `claims.json:13`; `targets.json`; `telemetry/dispatch-declared.json` |
| 5 | thresholds checkable by a round-34 validator | **checkable for all three claims, with 3 declared-defect corrections (P-3, P-4, P-5)** | §5 below |

---

## 1. Claims are on distinct axes — PASS

`claims.json:20-66` declares exactly three claims: **D = depth**, **O =
operability**, **C = calibration** — distinct, and all three inside the
scorecard's axis set (`SCORECARD.md:3`: depth, coverage, operability, freshness,
calibration, adjacency). `axes_in_play` (`claims.json:17`) names the same three.
No seat re-uses another claim's axis: the per-seat `claim` field in
`targets.json` partitions 63 seats into D ×27, O ×15, C ×13, cross ×8, and the
`role` field partitions them into executor/verifier/reviewer/scribe/scout/
critic/planner/connector — no seat carries an attribute outside its declared
claim.

## 2. Lowest-axis rule — PASS under the lane's r33 reading, with a recorded gap (P-1)

**Declared reasoning** (`claims.json:18`): "After round 33, depth and coverage
have zero regimen-2 claims; freshness is paused. Claim D works depth (tied
lowest); coverage is intentionally deferred to a later round."

**Verified.** Regimen 2 = lane rounds 33-74 (`REGIMEN.md:9-13`). The only other
dispatched regimen-2 round is 33, and `reports/round-33/claims.json` claims
O/C/A (`axes_in_play: ["operability","calibration","adjacency"]`) — so **depth 0,
coverage 0, freshness 0** regimen-2 claims, and the tie-break to depth is real.
The deferral of coverage is recorded with a reason in the same field. Claim D
therefore works a lowest axis under any reading that counts claim counts.

**P-1 (restated ambiguity, not a per-round defect).** Under the *literal*
contract text — "at least one claim works the lane's lowest non-retired axis
unless the stagnation nudge is invoked and recorded" (`REGIMEN.md:29-31`) — the
lowest non-retired axis is **freshness**: `SCORECARD.md:15` ("Freshness is
historically the lowest non-retired axis") and `SCORECARD.md:675` ("No
retirement") both stand, while the freshness *pause* only blocks freshness
axis-moves. Three facts then bind together:

- the nudge is not invoked and not recorded anywhere in `claims.json` (no nudge
  field exists in the declaration);
- `SCORECARD.md:676` states "the nudge is not invoked without calibrated scores",
  and no calibrated rubric exists (`SCORECARD.md:13-15`) — so the escape clause is
  itself unavailable;
- round 33 was admitted on the explicit non-literal reading —
  `SCORECARD.md:590` records "adjacency | improved (claim A — **lowest non-paused
  axis**)", i.e. the lane's own precedent redefines "lowest" as "lowest
  non-paused".

**Disposition (integrator).** This is a restatement obligation, not a rejection
trigger: the round report must carry the same "lowest non-paused axis" wording
r33 used, so the reading is on record for round 34 too. Recommended validator
legs (S04's spec): `claims.freshness_pause_in_force is true`; zero seat missions
containing a freshness axis-move; `claims.lowest_axis_reasoning` present,
non-empty, and naming both the tie (depth/coverage) and the non-paused reading.
Nothing in the regulator text should be *edited* by the round; the ambiguity is
operator-owned (`SCORECARD.md:676` "the freshness-threshold ruling remains the
operator's").

## 3. Freshness pause in force and observed — PASS

`claims.json:19` `freshness_pause_in_force: true` and `claims.json:69` non-goal
"no freshness axis-move (pause in force)". Measured against every seat mission
(`targets.json`): **zero** missions name a fetch, network, URL, download or
freshness move — the only `freshness` string in the whole targets file is inside
this seat's own mission line (X03). All three claims' counting commands
(`claims.json:31-35,46-50,61-64`) are in-repo reads/re-runs; the one filed
instrument invoked by a claim, `reports/round-30/craft/box1-survey.py`, is
print-only (`grep -n "write_text\|open(.*w\|json.dump"` → no write call; it ends
`print(json.dumps(out, indent=1))` and is safe to re-run).

## 4. One-batch shape — FAIL as declared: 64 requested vs 63 enumerated (P-2)

| artifact | declared | measured |
|---|---|---|
| `REGIMEN.md:13` | lane round 34 → **Swarm 64** | — |
| `claims.json:11-16` | `requested_workers: 64`, `batched_calls: 1`, key lane `opencode-go-2`, model `deepseek-v4.1-flash` | consistent with the regimen row |
| `targets.json` (`seat_count`) | **64** | `len(seats)` = **63** (ids unique; K×4, P×2, X×5, D×20, O×10, C×9, R×8, S×5) |
| `telemetry/dispatch-declared.json` | `requested_workers: 64`, `batched_agentswarm_calls: 1` | `seat_composition` sums to **63** (`4+2+1+16+4+10+9+8+4+5`) |
| r33 reference | — | `reports/round-33/targets.json`: `seat_count` 64, 64 seats; `SCORECARD.md:580-584` records 64/64 observed |

Command: `python3 -c "import json; d=json.load(open('reports/round-34/targets.json')); print(d['seat_count'], len(d['seats']), len({s['id'] for s in d['seats']}))"`
→ `64 63 63`.

**Effect on checkability.** The round contract's "dispatch exactly ONE batched
AgentSwarm per round at the declared size" (`REGIMEN.md:34`) is a checkable leg;
as declared it would **fail** (`len(seats) == 64` is false), and the round's own
telemetry is internally inconsistent (64 requested vs a 63-seat composition it
then enumerates by class). Two admissible dispositions, integrator's choice — the
point is that one of them must be on record, not neither:

1. **errata row** naming 63 enumerated seats and the reason the 64th slot is
   empty, with the observed-dispatch record (`telemetry/observed-dispatch.json`,
   currently owed per `dispatch-declared.json`'s `closing_snapshot` field) filing
   requested = 64, launched/completed as the route reports, and the 63-seat
   composition; or
2. land the missing seat and re-run the census.

Recommended validator legs: `len(targets.seats) == targets.seat_count`;
`claims.dispatch.requested_workers == targets.seat_count` unless an explicit
`declared_errata` object names the difference; `dispatch.batched_calls == 1`.
This is the only *shape* defect I found; the one-batch requirement itself
(`batched_calls: 1`) and the key/model route (`opencode-go-2`,
`deepseek-v4.1-flash`, key 2 of the round-robin per `REGIMEN.md:13,15`) are as
declared, and r35 rotating to `opencode-go-3` remains consistent.

---

## 5. Threshold checkability — per claim

### 5.1 Claim D (depth) — checkable; before-state citations byte-exact, enumeration partial (P-3)

**Citations verified, line for line** against
`reports/round-30/handoff/declared-in-r6/packet.md` (sha256 `6ced88ad…`):
`:148` D4-CL05 carries the stale 74/56/16/15 set; `:149` D4-CL06 carries "hold 15,
note 1, fail 0" **and** the "twelve … + three D2L-RANK rows, plus one D2L-RANK
note" split; `:150` D4-CL07 carries "conflicts (4), quarantine handles (3)";
`:152` D4-CL09 carries "rank_rules_unresolved_items 13, rank_quarantine_handles 3,
conflicts 4"; `:307` OQ-V3-05 repeats the same. The claim's `self_contradiction`
note (`claims.json:28`) is literally true in one file: **`:68`** (A-30) already
reads "82 labels (64 native-form / 12 translated-label / 6 borrowed-strata), 12
findings, 0 unresolved rank items, 4 era-alias rows" and **`:69`** (A-31) "12
holds / 0 note / 0 fail".

**Live values, recomputed independently** (`examples/culture-d4/typed-labels.d4.yml`
parses as JSON despite the `.yml` suffix — top keys `assembly, canon, coverage,
era_material_reconciliation, era_reconciliation, findings, generator,
label_kinds, name, rank_rules, typed_labels`):

```
typed_labels 82 | native-form 64 | translated-label 12 | borrowed-strata 6
findings_total 12 | findings_hold_or_fail 12 | label_findings_hold 12 |
label_findings_fail 0 | conflicts 0 | rank_quarantine_handles 0 |
rank_rules_unresolved_items 0 | reconciliation_records 6
era_material_reconciliation.summary {claims 6, findings 0} | alias_rows 4
examples/culture-d4/expected-holds.json counts {hold 12, note 0, fail 0},
12 rows, every row id D2L-FORM-UNRESOLVED (6 record-keyed GAR-01..06 +
6 slot-keyed LEX-GAR-01..06)
```

**P-3 — the declared stale set is a partial enumeration.** `claims.json:27`
lists ":150,:152 D4-CL07/09 (conflicts 4, quarantine 3)". Measured, the stale
positions are **seven** (this matches, independently, `depth/D03-ledger-rows.md`
§2 rows 1-7):

| # | position | stale | live |
|---|---|---|---|
| 1 | `:148` grounding | typed_labels 74, native-form 56, findings_total 16, findings_hold_or_fail 15 | 82, 64, 12, 12 |
| 2 | `:148` `#stats` clause | "labels 74" | 82 — **and the live file has no `stats` key at all** (see below) |
| 3 | `:148` statement | 74 / 56 / 16 / 15 | 82 / 64 / 12 / 12 |
| 4 | `:149` | hold 15, note 1; "three D2L-RANK rows, plus one D2L-RANK note"; +9 hold delta | 12, 0; zero rank holds, zero notes; +6 hold delta |
| 5 | `:150` | conflicts 4, quarantine 3 | 0, 0 |
| 6 | `:152` | unresolved rank items 13, quarantine 3, conflicts 4 | 0, 0, 0 |
| 7 | `:307` | "twelve form + three rank + one note"; 13 / 3 / 4 | twelve form + zero rank + zero notes; 0 / 0 / 0 |

Two items in that table are **not** in `claims.json`'s shorthand and must not be
lost by the drafted rows: (a) the `#stats` reference on `:148` — the live
projection has no `stats` block, so a row that keeps citing
`typed-labels.d4.yml#stats` keeps a dangling anchor even after the numbers are
fixed (the claim's threshold "links resolve" therefore has a hard case in row 2);
(b) `:152`'s `rank_rules_unresolved_items 13`.

**Scope correction that protects the D sub-verdict:** the 74/56/16/15-class
numbers remain **live-correct in the D2 family** (`examples/culture-d2/…`), so
"zero stale figures" is a statement about the **D4** rows only; a symmetry fix
that "corrects" the D2 rows would be a false edit. `depth/D03-ledger-rows.md`
:159 records this constraint independently; I confirm it from the packet's own
row split.

**Status-wording item (record, do not silently renumber).** `:152`'s row status
is `unresolved` while the live rank items/handles/conflicts are 0/0/0 — the
number fix and the uncertainty-status wording are two decisions, and the round
must record the second (D03 §4 flags it). Anything that only renumbers leaves the
gate's uncertainty vocabulary asserting an unresolved class with an empty
population.

**Checkable legs (verified runnable forms).** I ran the gate at HEAD on the
current default packet: `python3 tools/gates/handoff-packet-check.py
reports/round-30/handoff/declared-in-r6/packet.md` → `INFO scan: fields=16/16
glossary-entries=20 findings=0`, exit 0 (and it changed no filed byte:
`git diff --name-only HEAD -- reports/` → 0). The same command over
`reports/round-34/handoff/declared-in-r7/packet.md` is a machine leg; the numeric
leg is recomputable from the two JSON files above without any YAML dependency.

**Delivered-vs-declared watch item.** At my read instant **the D after-state is
not on disk**: `ls reports/round-34/handoff/declared-in-r7/` → "No such file or
directory", and `tools/exercise-handoff-e2e.py:1933-1934` still pin
`reports/round-30/handoff/declared-in-r6`. `depth/D10-repin-drafts.md:186-187`
correctly labels its SCORECARD row as a draft ("Replace the number cells with the
measured values actually observed when the round closes; do not copy the planned
figures above into the ledger unmeasured") — that discipline must survive into
S04's integration draft and the final SCORECARD row.

### 5.2 Claim O (operability) — checkable; the declared before-state is false in both directions (P-4)

**Declared** (`claims.json:41`): "Known hazards to classify:
`reports/round-{5,6,7}/run-validation.py` and `reports/round-26/run-validation.py`";
threshold "the four named hazards classified".

**Measured** (static census over the 28 filed round runners; no execution):

```
git ls-files 'reports/round-*/run-validation.py' | wc -l → 28
zero guard_receipt references (unguarded writers, 11):
  r5, r6, r7, r8, r9, r10, r11, r12, r19, r21, r29
guard call present (adopted, 17):
  r14, r15, r16, r17, r18, r20, r22, r23, r24, r25, r26, r27, r28, r30, r31, r32, r33
```

- **False positive — r26 is adopted, and was at filing.** `git log --format=%H
  --diff-filter=A -- reports/round-26/run-validation.py` → `4f09c99…` (the round-26
  admission commit), and that commit's bytes already contain
  `def guard_receipt()` (`:1855-1857`), the call `guard_receipt()` at `:1906`
  inside `try/except SystemExit`, and the write at `:1909` — i.e. the guard
  preflight runs before the receipt write, exactly the sanctioned "callback must
  call guard_receipt itself immediately before writing" form documented in
  `tools/harness/receipt_guard.py`'s module docstring. r26 is **not** a hazard of
  the r5/r6/r7 class. The upstream source of the error is the filed incident
  record itself: `LOG.md:3559` — "The r26 runner carries the same hazard (`:90`,
  `:1909`)" — which round 34's declaration quotes verbatim. LOG.md is append-only;
  the correction must be a **new row**, never an edit.
- **Large false-negative set — 7 runners beyond the named four.** r8, r9, r10,
  r11, r12, r19, r21, r29 write their receipts in place with zero guard
  references (r5/r6/r7 were the four named; the rest were missed). r19 is the
  sharpest shape in the set: `reports/round-19/run-validation.py:19` *reads back*
  the admitted receipt and `:21` writes it again with a mutated field — a
  load-modify-write of a filed artifact, not a rebuild. r10 and r19 have no
  `--check` mode at all, so their only safe route is an isolated copy.
- **Independent agreement inside this round.** `op/O01-impl.md` §4 counts
  "guard-adopted 17, unguarded-writer 11"; `op/O05-routing.md` §2 prints the same
  28/11/17 counts with per-round write sites; `scout/K03-guard-pattern.md:45-59`
  corrects the r26 misread with the same line evidence. So the O block's own
  measurement **contradicts its declared before-state** — that is a
  declaration-vs-finding conflict the round must disposition explicitly
  (`REGIMEN.md:39-43`: never force a pass; a trade is reported, not averaged).
  The honest closure is: the *after-state* (an inventory that classifies all 28
  with zero false positives) verifies, while the *before-state's* "four known
  hazards" is corrected by a named finding and the append-only LOG row.
- **Census-scope defect already caught:** `git ls-files 'reports/**/run-validation.py'`
  → 29 paths; the extra one is `reports/supplement-opencode-1/run-validation.py:132`
  (unguarded, outside the round glob). `op/O09-verify-routing.md` D-4 files this
  as a scope defect. The claim's threshold "inventory covers 100% of filed
  runners" is only checkable once the class is stated: either
  `reports/round-*/run-validation.py` (28) or every `reports/**/run-validation.py`
  (29, with the supplement row classed).

**Recommended restated legs:** `class(r26) == guard-adopted` and
`{r5,r6,r7,r8,r9,r10,r11,r12,r19,r21,r29} ⊆ unguarded-with-receipt-write`; the
supplement path either classified or explicitly out of scope with a reason;
selftest green with the negative control "a guarded runner is NOT flagged" and
the positive control "the r32/r33 two-call pattern IS adopted".

### 5.3 Claim C (calibration) — checkable; the "R1–R8 anchor reissue" conflates two surfaces (P-5)

**Live verification.** `python3 -B reports/round-30/craft/box1-survey.py` →
`{"named": 28, "resolvable": 28, "unnamed_in_skill": [], "skill_sha256":
"f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b"}`, exit 0;
`sha256sum SKILL.md` → the same `f9bd07c2…`; `wc -l SKILL.md` → 732 (matches
`claims.json:58`'s "715 → 732"). **The 28/28 after-state is therefore already
true at HEAD** — the claim's value is durability (a dated, digest-pinned,
re-runnable receipt), which is how `after_required` words it; the validator leg
must pin *the new receipt and its digest fields*, not "28/28 achieved".

**Two tool-side caveats the durable receipt must carry** (both already handled in
`calib/C02-receipt-json.md:45-55`, verified): the survey's `date` field is a
hard-coded constant `"2026-10-18"` (`reports/round-30/craft/box1-survey.py:8`) and
is *not* the run date; and the row scope is tools-only (`tools/[\w./-]+\.py`
regex at `:6`), while SKILL.md also names python surfaces outside `tools/` —
`SKILL.md:221` (`assemble-d2.py`, bare), `:383`
(`reports/round-28/ceiling/measure-ceiling.py`), `:633`, `:658`, `:706` (the
filed runners `reports/round-5|6|7/run-validation.py`), `:713`, `:717`, `:718`
(bare `run-validation.py`). "28/28" is a tools-only denominator; a receipt that
says only "28/28 named executables resolve" over-reads its own filter.

**P-5 — R1–R8 is a deliverables list, not an anchor list.** `A09-pins.md:105-114`
defines R1 = README blob pin, R2 = README sha receipts, R3 = SKILL sha receipts,
R4 = box-1 re-survey, **R5 = SKILL.md line anchors**, R6 = README prose
arithmetic, R7 = x45/x57 control status, R8 = README row landing order. Only R5
(and its findings A09-F3/F5, `A09-pins.md:124,126`) concerns line anchors.
`claims.json:56,60` asks for "the A09 R1–R8 SKILL anchor reissue … a table of old
anchor → new anchor → owning row, each verified by grep" — that table is
well-defined for the anchor subset only; the other seven rows must be
dispositioned as non-anchor deliverables (or the C08 verification leg "verify
every C03 reissue row" is unverifiable as declared).

**Anchor surfaces at HEAD (my independent measurements, for the reissue table's
completeness and its denominator check):**

- `AGENTS.md` is **40 lines and contains zero line anchors**
  (`grep -n ":[0-9]\{2,4\}" AGENTS.md` → no output; `grep -n "SKILL.md" AGENTS.md`
  → no output). A09-F3's named `AGENTS.md:42` anchor ("after :534") **no longer
  exists** — r33's excision (`SCORECARD.md:599-600`, "AGENTS.md drafting residue
  excised (42 → 40 lines)") deleted it. The correct reissue row is therefore
  "closed by excision at da68a6d — zero new anchor", not a re-point.
- SKILL.md's own citation sites `:149` and `:183` both cite `SKILL.md:47`, which
  exists at 732 lines and holds the label-typing / off-channel-exemption row —
  i.e. both sites' *targets* still resolve at HEAD (K04 §5 owns the old→new
  mapping).
- `corpus/lessons/*.md` carries **18** `SKILL.md:NNN` citations over **10**
  distinct targets (`:715`×4, `:294`×4, `:713`×3, `:278`×2, `:323`, `:262`,
  `:208`, `:205`, `:189`, `:157`) — all filed rows, none editable; drift must land
  as superseded readings. This gives the validator a hard denominator: the
  reissue table's lesson-citation coverage either accounts for all 18 instances /
  10 targets or names each omission.
- `scout/K04-anchor-census.md` §5-6 carries the mapping and independently reaches
  the "AGENTS.md:42 deleted, not moved" conclusion.

**P-6 (cross-claim exposure).** `SKILL.md:633,658,706,713,717,718` documents
invoking the filed runners `reports/round-5|6|7/run-validation.py` as historical
red controls — those three are exactly the unguarded writers. The lane's own
instruction surface therefore documents the F-C13-1 hazard. `op/O05-routing.md`
contains **zero** mentions of SKILL.md (`grep -n "SKILL" op/O05-routing.md` → no
output), so the routing receipt does not yet state that "isolated-copy-only for
unguarded runners" extends to SKILL.md-documented invocations. Recommended: one
row in the routing receipt covering the SKILL.md-cited runners, carried into
X00's collision matrix.

---

## 6. Draft-in-advance discipline — PASS, with one watch item

Verified on disk at the audit instant: `reports/round-34/handoff/declared-in-r7/`
absent; `tools/exercise-handoff-e2e.py:1933-1934` still
`reports/round-30/handoff/declared-in-r6/…`. The D block's receipt-shaped
fragments handle this honestly — `depth/D10-repin-drafts.md` is titled a draft,
carries "do not copy the planned figures above into the ledger unmeasured"
(`:186-187`) and lists the applied edit + measured cells as integrator-side in
`## Owed`; `depth/D12-receipt.md:216` marks the validator leg "owed (runner
absent)". The watch item for S04: no round-level prose (integration draft,
SCORECARD row, LOG row) may state the D after-state as achieved until the
artifacts exist.

## 7. F-C13-1 prevention — independent spot check, no violation found

`grep -rn` over `reports/round-34/**` for in-tree runner execution found none;
the only execution of a filed runner recorded in any fragment is `op/O09-verify-routing.md:169`
`cd .scratch/o09/iso/repo && python3 reports/round-5/run-validation.py` → exit 1 —
an isolated copy, the sanctioned route. My own runs are in §Method. X02 owns the
full conformance verdict; this sample agrees with it.

## Owed

- `reports/round-34/cross/X00-connector.md`, `reports/round-34/cross/X01-trades.md`,
  `reports/round-34/cross/X04-honesty.md` — not on disk at my read
  (`find reports/round-34 -type f` at 07:12Z). X00's collision matrix should
  carry **P-2** (batch arithmetic) and **P-6** (SKILL.md-documented runner
  invocations); X04 should carry **P-1/P-3**.
- `reports/round-34/calib/C03-anchor-reissue.md` — absent at my read; **P-5**'s
  scope correction (anchor subset vs the other seven R-rows) and the
  `AGENTS.md:42`-deleted row must be applied by whoever lands the reissue table
  (`K04-anchor-census.md` §5-6 already carries the mapping).
- `reports/round-34/telemetry/observed-dispatch.json` (owed per
  `telemetry/dispatch-declared.json`'s own `closing_snapshot` field) — must carry
  the **P-2** 64-vs-63 disposition (requested vs launched/completed, 63-seat
  composition) and the digest-pinned closing snapshot once `validation.json`
  lands.
- `reports/round-34/run-validation.py` — does not exist (by design); the leg
  formulations in §2, §4, §5.1-5.3 are inputs for S04's validation-leg spec.
- `LOG.md` append-only correction row for `LOG.md:3559`'s r26 sentence (**P-4**),
  and the errata disposition of `claims.json:41`'s four-hazard before-state
  against the measured 11 — integrator/parent, new rows only.
- `reports/round-34/craft/box1-resurvey-durable.json` — the durable artifact
  itself (C02's content is drafted in `calib/C02-receipt-json.md`); its validator
  leg needs the real observation date, not the tool's constant.

## Citations

Declaration / contract (read-only):

- `REGIMEN.md:9-13` (round 34 = lane round 34, key 2, swarm 64), `:25-31` (claim
  and lowest-axis rule), `:33-35` (one batched swarm at declared size), `:39-43`
  (admit only when every claim verifies; never force a pass), `:44-50` (full
  record set incl. telemetry closing snapshot).
- `reports/round-34/claims.json:11-16` (dispatch), `:17-19` (axes, lowest-axis
  reasoning, pause), `:20-37` (claim D + before/after/thresholds), `:38-52`
  (claim O), `:53-66` (claim C), `:68-74` (non-goals).
- `reports/round-34/targets.json` (`seat_count`, `seats`, `shared_rules`).
- `reports/round-34/telemetry/dispatch-declared.json` (requested 64, one batched
  call, seat composition, closing snapshot owed).
- `reports/round-33/claims.json` (r33 claim axes O/C/A), `reports/round-33/targets.json`
  (64/64), `reports/round-33/adj/A09-pins.md:105-114` (R1–R8), `:122-126`
  (A09-F1..F5).
- `SCORECARD.md:3` (axis set), `:13-15` (no calibrated rubric; freshness
  historically lowest), `:580-602` (r33 admission row incl. 42 → 40 AGENTS.md
  excision, SKILL digest move), `:675-676` (no retirement; nudge not invoked
  without calibrated scores).

Filed bytes verified (read-only, never written):

- `reports/round-30/handoff/declared-in-r6/packet.md` — sha256
  `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb`; lines
  `:68,:69` (manifest A-30/A-31 already live), `:148,:149,:150,:152` (stale D4
  rows), `:307` (OQ-V3-05).
- `reports/round-30/handoff/declared-in-r6/expected.json` — sha256 `ea1e2927…`.
- `reports/round-26/run-validation.py` — `:90` (OUTPUT), `:1855-1857`
  (`def guard_receipt()`), `:1906` (guard call), `:1909` (write); present
  unchanged in the filing commit `4f09c99`.
- `reports/round-{5,6,7}/run-validation.py` — write sites `:194`, `:336`, `:1171`;
  zero guard references (F-C13-1 mechanism, `LOG.md:3550-3560`).
- `reports/round-19/run-validation.py:19,21` (load-modify-write of an admitted
  receipt); `reports/round-10/run-validation.py` (no `--check` mode).
- `reports/supplement-opencode-1/run-validation.py:132` (29th path under
  `reports/**`).
- `tools/exercise-handoff-e2e.py:1933-1934` (defaults still r6),
  `tools/harness/receipt_guard.py` (module docstring: refusal exit 3,
  `REFRESH_RECEIPTS=1` the only override; two-call helper contract).
- `examples/culture-d4/typed-labels.d4.yml` (coverage/era blocks above),
  `examples/culture-d4/expected-holds.json` (`counts` 12/0/0; 12
  D2L-FORM-UNRESOLVED rows).
- `SKILL.md` — sha256 `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`,
  732 lines; `:47` (self-cite target), `:149,:183` (self-cite sites), `:221,:383,
  :633,:658,:706,:713,:717,:718` (non-tools python surfaces), `:534`.
- `AGENTS.md` — 40 lines, zero line anchors (r33 excision).
- `corpus/lessons/*.md` — 18 `SKILL.md:NNN` citations over 10 distinct targets.
- `reports/round-34/{depth/D03,D10,D11,D12, op/O01,O05,O09, scout/K03,K04,
  calib/C02, cross/X02}` — sibling fragments cross-checked (not edited).

Commands relied on:

- `python3 -c "import json; d=json.load(open('reports/round-34/targets.json')); print(d['seat_count'], len(d['seats']), len({s['id'] for s in d['seats']}))"` → `64 63 63`.
- `python3 -c` over `reports/round-34/targets.json` for role/claim counts (executor 28, verifier 9, reviewer 8, scribe 7, scout 4, critic 4, planner 2, connector 1; D 27 / O 15 / C 13 / cross 8) and a regex scan of every mission for `network|fetch|http|url|online|download|cite an external` → 0 hits; for `freshness` → only seat X03's own mission text.
- `git ls-files 'reports/round-*/run-validation.py' | wc -l` → 28;
  `git ls-files 'reports/**/run-validation.py' | wc -l` → 29 (extra:
  `reports/supplement-opencode-1/run-validation.py`).
- Per-runner `grep -c 'guard_receipt'` census → 0 for r5,r6,r7,r8,r9,r10,r11,r12,r19,r21,r29; ≥1 for the other 17.
- `git log --format=%H --diff-filter=A -- reports/round-26/run-validation.py` → `4f09c99…`; `git show 4f09c99:reports/round-26/run-validation.py | grep -n 'guard_receipt'` → `:1855,:1857,:1906`.
- `python3 -B reports/round-30/craft/box1-survey.py` → `named 28 / resolvable 28 / "date": "2026-10-18" / skill_sha256 f9bd07c2…`, exit 0.
- `sha256sum SKILL.md` → `f9bd07c2…`; `wc -l SKILL.md` → 732; `wc -l AGENTS.md` → 40; `grep -rn "SKILL\.md:[0-9]\+" corpus/lessons/*.md | wc -l` → 18; distinct targets 10.
- `python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md` → `INFO scan: fields=16/16 glossary-entries=20 findings=0`, exit 0; `git diff --name-only HEAD -- reports/` → 0 rows; `git status --porcelain` → `?? reports/round-34/` only.
- `python3 tools/harness/receipt_guard.py --selftest` → `controls_passed 45 / controls_total 45`, `selftest_passed: true`.
- `python3 -c` JSON loads of `examples/culture-d4/typed-labels.d4.yml` and `examples/culture-d4/expected-holds.json` → values in §5.1.
- `ls reports/round-34/handoff/declared-in-r7/` → No such file or directory (at 07:12Z).
