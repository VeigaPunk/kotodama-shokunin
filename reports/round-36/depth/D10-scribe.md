- Seat: D10 | scribe | claim D (depth) | date 2026-10-19 | baseline ce103bf

# D10 — D-block material for the fleet report: Work performed, Landed changes, paths, commit-ready list

**Mission** (`reports/round-36/targets.json`, seat `D10`): *"Landed-changes material."*
Out path: `reports/round-36/depth/D10-scribe.md`.

**Baseline.** `git rev-parse HEAD` → `ce103bf5885af00023cdc4a174c17602476cdcf8`.
`git status --porcelain` **at this seat's first reads** → `?? reports/round-36/` (one row): the
tracked tree was byte-clean and this seat moved no tracked byte. **At this seat's close the same
command returns a dirty row whose path moved during the window** (`reports/round-34/validation.json`,
then `reports/round-35/validation.json`) — filed artifacts another seat or the parent is editing
in flight. See the observation table in the path inventory (§2) and §7; this seat wrote neither
path.

**Method.** Every number in §4 is this seat's own read at `ce103bf`, citable to a `file:line`
or to a command quoted in `## Citations`. Where a peer fragment's figure is quoted it is
attributed at the point of use and was re-measured first-hand where re-measurable. Env for every
command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, cwd = lane root — with the
single exception recorded in §4.1 (V-8's first run used a `TMPDIR` inside the repo, which the
tool refused, and was re-run with `TMPDIR=/tmp`).

**Non-author declaration.** This seat authored no lane artifact before this round and moved no
lane byte. No promotion, canon, clearance, closure or acceptance verdict is claimed anywhere
below; each such token appears only as a negation or a quoted pattern.

**F-C13-1 / freeze rule honoured.** No `reports/round-*/run-validation.py` was executed, in-tree
or in a copy. No `--freeze` of `reports/round-34/handoff/declared-in-r7` was run. The only filed
code executed is the read-only gate family named in §4 (`tools/gates/*`), plus
`tools/check-gate-battery.py` and `tools/replay-frozen.py` (§4 V-7/V-8).

---

## §0 Dependency state at this seat's cut (2026-10-19)

**Note on this section's timing.** The D block landed in waves while this seat wrote. The
census immediately below is the state at this seat's *first* cut; §0.1 records what had landed
by the time this file was finalized, and §5 folds the peer findings.

`find reports/round-36 -type f` at the first cut:

```
reports/round-36/claims.json
reports/round-36/targets.json
reports/round-36/telemetry/availability-attempt-1.json
reports/round-36/telemetry/dispatch-declared.json
reports/round-36/cov/C01-audit.md
reports/round-36/cross/X02-conformance.md
reports/round-36/depth/D01-design.md
```

Seven files. **D01 landed mid-window** (read after this seat's first census) and its headline
finding converges with §5 below, reached independently — it measured
`derived_pairs=8` and named the same stale premise.

### §0.1 Landed by finalization (folded in §5)

`find reports/round-36 -type f` at this seat's close → **33 files**. The D-block peers that
landed during the seat and bear on claim D:

| fragment | what it contributes to this receipt |
|---|---|
| `depth/D02-packet-draft.md` | the packet-block draft and the **double-grade hazard** (`argot-derivation-gate.py:304-314`, `:549`) that fixes the block's field shape |
| `depth/D03-isolated-verify.md` | the isolated apply-and-verify: D01's Drafts 1+2 and P01's Surface-A shape integrated in `git archive ce103bf` copies, all legs captured; §5's pin cascade |
| `depth/D04-repin.md` | the pin re-freeze list, **measured** on three isolated copies rather than derived; owns the row set (the integrator re-measures digests on the landed bytes) |
| `depth/D05-receipt.md` | the depth receipt (claim D's own before→after with counting commands) |
| `depth/D06-gap-fill.md`, `depth/D09-gap-fill.md` | the two spare gap-fills, both re-measuring the premise |
| `depth/D07-verify.md` | **the independent verification**: its own `git archive ce103bf` rebuild, D03's legs reproduced exactly, and its own text-level parse finding 8/8 forms re-deriving — plus a **named unreproduced D03 digest** (`0f0828731366ce52`) |
| `depth/D08-verify-repin.md` | the re-pin census run independently: nine pin surfaces, six falsified by mutation, **without accepting any sibling's list** |
| `plan/P01-d-plan.md` | the plan; re-aims claim D onto "Surface A + B-1 only" and prices B-2 as a contract amendment |
| `scout/K0{1,2,3}-*.md` | the three scouts (register, timekeeping, recount) |
| `review/R0{1,2}-d-review.md`, `R03-cross-review.md` | the two D reviews and the cross review; **R02-D-6 is a new actionable gap** (§5.3) |
| `cross/X00-connector.md`, `X02-conformance.md` | the collision matrix and the conformance audit |
| `scribe/S01-integration-draft.md`, `S02-telemetry-draft.md` | the integration dossier (fleet-report draft + validation-leg spec + selftest list) and the telemetry draft |

Still absent at close: **the round's own `run-validation.py` and `validation.json`** — the
integration pass's output, and the one artifact claim D's own `counting_commands` names. That is
the remaining owed item (§`Owed`).

**Consequence.** §1/§2 are report-register drafts; §3 and §4 are complete as delivered, because
the paths and numbers they carry come from binding files (`claims.json`, `targets.json`), from
filed round-25..30 bytes, and from this seat's own reads of the live tree — not from sibling
prose. The per-seat outcome pointers that were `{{owed …}}` fills in this fragment's first draft
are now supplied by the landed fragments named in §5.

**Seat accounting.** `targets.json` declares `seat_count: 32` and `seats[]` holds **32**
objects — the round-34 64-vs-63 deviation does not repeat, and the round-36 batch is a 32-seat
single wave (half of round 35's 64). The declared route was `hyper / deepseek-v4.1-flash`;
the **observed** route is `devin / deepseek-v4-1-flash-high` after a 402 at launch
(`telemetry/availability-attempt-1.json`: 32 requested, 0 launched, 32 failed). The report must
state declared and observed separately and never read the 32 declared as 32 launched.

---

## §1 Work performed — D block (report-ready draft)

```text
- **Depth (claim D):** the round's declared deliverable is to "close the r25 empty-domain
  record" by building register-form content into the D4 lineage. Measured at the round's own
  baseline `ce103bf`, **that premise is stale and the deliverable is already in the tree**:
  the register-form domain is not empty, and every leg the claim names is green over the
  delivered forms. The closure happened two loops earlier — round 26 landed the eight `stamp`
  forms (SCORECARD.md:329), round 27 landed the register law (SCORECARD.md:345), round 28
  landed the law replay leg (SCORECARD.md:363), round 30 landed the four QREG act records that
  resolved the law's design_row dangles. D10's contribution is therefore the correction itself
  plus the D-block bookkeeping: the before→after table (§4) with each leg re-run first-hand,
  the path inventory and commit-ready list (§2/§3), and the freeze-collision finding (§6).
  **The block converged on the same correction independently — twelve seats measured it in this
  round (table, §5).** The constructive work the block did *not* duplicate is the open surface:
  D01/D02/P01 draft the `doublets:` block and the base-side pointer (Surface A + B-1; D01's
  Drafts 1+2 and P01's row shape both integrated and run in D03 §4), D03 applies and verifies
  them in isolated `git archive ce103bf` copies, and R02 files the one actionable residue
  (**R02-D-6**, §5.3).
- **The register stratum, as delivered at `ce103bf`:** eight register forms `L-55..L-62`
  (`tuum kit lom nees huum mees reek saam`) in
  `examples/culture-d4/components/04-lexicon.yml:236-243`, each carrying the full field set
  (`register: stamp`, `derived_from`, `derivation: {op, base}`, `doublet_of`, `bases`,
  `construction: STAMP-REVERSE|STAMP-LENGTHEN`, `stage: E1`, `axis`). Six are fire-axis
  `lengthen` forms, two are mark-axis `reverse` forms — the axis→operation rule the r26 build
  discovered (`QREG-03`, `04-lexicon.yml:252`). The contract already admits every field
  (`packet.d4.yml:30-44`, `contract.record_fields.lexicon`), so no schema work is owed for the
  forms. **The block's own residue here is the wiring gap, not the content**: the derivation-replay
  leg has no frozen baseline and no battery registration while the law leg has both
  (**R02-D-6**, §5.3). D02's packet-block draft (`depth/D02-packet-draft.md`) lands the index
  route and measures the double-grade hazard that fixes its field shape.
- **The law, as delivered:** `register_law:` RGL-01..05 (`packet.d4.yml:2788`) over the
  `registers:` QREG-01..08 block (`:1329`), with the replay leg `tools/gates/register-law-gate.py`
  over six `D4L-LAW-*` classes and 45/45 selftest checks. The r27/r28 RL-1 gap ("no law replay
  leg yet") is closed; the four r28 `D4L-LAW-DANGLING` findings were resolved by the r30 QREG
  landing rather than by weakening the resolver (`reports/round-30/fixes/qreg-dangles.md:40`).
- **The wiring, as delivered:** the argot leg is a first-class typed-pipeline leg
  (`tools/gates/typed-pipeline-gate.py:517-541`, `L3b-argot`), and the delivered D4 chain reads
  `ok L3b-argot` inside `summary: 20/20 legs passed`. S01's integration dossier
  (`scribe/S01-integration-draft.md`) landed and carries the validation-leg spec and selftest
  list for `reports/round-36/run-validation.py`; the leg names this receipt measures are the five
  in §4.1, and the integrator reconciles the two lists.
```

---

## §2 Landed changes — D block (report-ready draft + path inventory)

```text
- `examples/culture-d4/components/04-lexicon.yml` — the register stratum's home: the two
  `STAMP-*` constructions (`:98-121`), the eight form records (`:236-243`), the
  `morphology.derivation_rules` `lengthen` row (`:267`, with `derivation_ops` at `:269`), and the
  `registers:` QREG-01..08 block (`:244-260`). Delivered by rounds 26 and 30; **not** changed by
  this round.
- `examples/culture-d4/components/13-register-law.yml` — the law component (RGL-01..05 +
  `law_binding` + `calibration`), landed by round 27 as a new file, supersede-by-new-file only.
- `examples/culture-d4/packet.d4.yml` — the assembled packet carrying `registers`,
  `register_law`, the eight form records, and the contract fields for all three. Digest
  `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`.
- `tools/gates/argot-derivation-gate.py` — the derivation replay leg (`head2`/`reverse`
  computed, `lengthen` replayed from the packet), the `D4L-ARGOT-*` finding classes, and the
  coverage line the census is read from. Selftest 27/27.
- `tools/gates/register-law-gate.py` — the law replay leg, six `D4L-LAW-*` classes, four
  resolutions. Selftest 45/45. **Not wired into the typed pipeline and not named in
  `tools/gates/typed-pipelines.json`** (0 hits each) — see §4 G-C.
- `tools/gates/typed-pipeline-gate.py:517-541` — the `L3b-argot` leg that makes the argot gate
  a pipeline leg rather than a standalone script.
- `reports/round-36/depth/D10-scribe.md` — **this file** (claim D's report material; the only
  byte this seat writes).
- Round-36 surfaces the integrator files (outside this seat's write scope): `SCORECARD.md`
  round-36 row, `LOG.md` append-only entry, `MANIFEST.json` `rounds[]` entry, the fleet report
  `../.ufo/reports/round-36/kotodama.md`, `reports/round-36/run-validation.py` + `validation.json`,
  and the closing telemetry snapshot owed by `AGENTS.md`.
```

### Path inventory (what the round's D block adds or touches)

| # | Path | Kind | Owner | State at my cut → close |
|---|---|---|---|---|
| 1 | `reports/round-36/depth/D10-scribe.md` | new seat fragment | D10 (this seat) | **written** |
| 2 | `reports/round-36/depth/D01-design.md` | new seat fragment | D01 | landed mid-window |
| 3 | `reports/round-36/depth/D02-packet-draft.md` | new seat fragment | D02 | **landed at close** |
| 4 | `reports/round-36/depth/D03-isolated-verify.md` | new seat fragment | D03 | **landed at close** |
| 5 | `reports/round-36/depth/D05-receipt.md` | new seat fragment | D05 | **landed at close** |
| 6 | `reports/round-36/depth/D06-gap-fill.md`, `D09-gap-fill.md` | new seat fragments | D06/D09 | **landed at close** |
| 7 | `reports/round-36/depth/D04-repin.md` | new seat fragment | D04 | **landed at close** (the re-pin list, measured on isolated copies) |
| 7b | `reports/round-36/depth/D07-verify.md`, `D08-verify-repin.md` | new seat fragments | D07/D08 | **landed at close** (the verification pair) |
| 8 | `reports/round-36/plan/P01-d-plan.md`, `scout/K0{1,2}-*.md` | new seat fragments | P01/K01/K02 | **landed at close** |
| 9 | `reports/round-36/review/R0{1,2}-d-review.md` | new seat fragments | R01/R02 | **landed at close** |
| 10 | `reports/round-36/run-validation.py` + `validation.json` | new | integration pass | **absent — owed** |
| 11 | `SCORECARD.md` | append row | integrator | no round-36 row |
| 12 | `LOG.md` | append rows | integrator | round-35 rows are the tail |
| 13 | `../MANIFEST.json` (fleet root) | append `rounds[]` entry | integrator | r35 is the last entry |
| 14 | `../.ufo/reports/round-36/kotodama.md` | new fleet report | integrator | absent |

**Byte-preservation (must stay untouched):**
`reports/round-1..35/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`,
`reports/round-34/handoff/declared-in-r7/**` (its bytes are pinned), fleet `.ufo/**` outside
the new round-36 report. Superseded-but-filed means **new rows, never edits** — the ruling the
r33/r35 LOG rows already record. This seat moved none of them and the r7 read-set recomputes
intact to `ok 58, mismatch 0, missing 0` (§6). **The tree is not byte-clean at this window's
close** — see the live observation immediately below, which is *not* this seat's write.

**A moving modification of filed round artifacts, observed live across this seat's window.**
This seat's first reads returned `?? reports/round-36/` **only** (clean tracked tree). Later reads
in the same window returned a dirty row whose **path moved**:

| observation | `git status --porcelain` | mtime of the dirty path |
|---|---|---|
| window start | `?? reports/round-36/` | — |
| mid-window | ` M reports/round-34/validation.json` + `?? reports/round-36/` | `2026-10-19 06:32:04 -0300` |
| later | same path, re-touched | `2026-10-19 06:32:16 -0300` |
| window close | ` M reports/round-35/validation.json` + `?? reports/round-36/` | `2026-10-19 06:33:23 -0300` |

At close the round-34 path is **clean again** and the round-35 path is dirty
(`git diff --stat HEAD -- reports/` → `reports/round-35/validation.json | 6 ++----`,
2 insertions, 4 deletions). So an in-flight process — another seat or the parent — is editing
**filed** `reports/round-3x/validation.json` paths one at a time and reverting as it goes.
`reports/round-1..35/**` is filed-bytes territory under the shared rules, so this is recorded
for the O/adjacency seat or the parent to reconcile; D03 §6 observed the same r34 row from its
own window. **This seat did not touch, read-after-change, or revert any of these paths.** Its
own byte-cleanliness claim is narrowed accordingly: *this seat moved no tracked byte*, and *the
tracked tree was clean at this window's start but not at its close* — the dirty paths are not
this seat's writes and are not stable.

---

## §3 Commit-ready list

Staging set for the round-36 commit (lane repo), in dependency order:

1. `git add reports/round-36` — the whole round tree: `claims.json`, `targets.json`,
   `telemetry/` (declared + availability-attempt-1 + the observed-dispatch and closing records
   `AGENTS.md` requires), the 32 seat fragments per `targets.json`, `depth/`, `cov/`, `calib/`,
   `cross/`, `review/`, `scribe/`, and `run-validation.py` + `validation.json` from the
   integration pass.
2. `SCORECARD.md` — the round-36 row(s) the integrator records for each claim, with per-axis
   verdicts. **This round's D row must not repeat claim D's stale premise** (§5).
3. `LOG.md` — the round-36 append-only entry under the lane git identity.
4. Fleet-root artifacts, by the parent/integrator, outside this repo: `../MANIFEST.json`
   `rounds[]` entry and `../.ufo/reports/round-36/kotodama.md`.
5. No `tools/**` and no `examples/**` change is owed by the D block: the register stratum,
   the law, and both gates are **already delivered** at `ce103bf`. If the round still lands
   D01's `doublets:` draft (§4 G-A), that is a component edit plus a pin cascade — D04's list.

Pre-commit must-exist checklist (state at this seat's close):

- [ ] `reports/round-36/run-validation.py` exits 0 — claim D's own `counting_commands`
      (`claims.json:20`) name this path, and it does not exist yet (`ls` → exit 2). Until it
      lands, claim D's counting command is **owed**, not satisfied.
- [x] Claim D's "forms verified by two independent seats" — **met within this round**:
      `depth/D07-verify.md` §1 (own text-level parse, 8/8 re-deriving) and
      `depth/D03-isolated-verify.md` §1 (own parser and own `op` implementations), plus the
      twelve-seat premise convergence (§5). The *filed* verification of the forms' landing is the
      r26 pair (`reports/round-26/audit/x60-register-derivation-spotcheck.md` +
      `reports/round-26/register/review.md` §1 row G-5).
- [ ] Telemetry: an observed-dispatch record for the devin fallback plus the closing snapshot
      once `validation.json` lands (`telemetry/dispatch-declared.json`
      `closing_snapshot: "open-at-seat-close: owed once validation.json lands"`).
- [ ] The round-36 SCORECARD row and LOG entry.
- [ ] Reconciliation of the in-flight `reports/round-3x/validation.json` modification (§2/§7) —
      **must not be committed blindly**: at this window's close one filed round's
      `validation.json` carries an uncommitted change this seat did not make and cannot attribute.

---

## §4 Before → after measurements (D block), measured by this seat

All commands run at `ce103bf` with exits captured unpiped. Interpreter `python3 -V` →
`Python 3.14.7` (recorded because counting-command output can be interpreter-sensitive).

### 4.1 The claim's own legs, re-run on the delivered revision

| # | leg | command | result | exit |
|---|---|---|---|---|
| V-1 | derivation replay | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` | 0 |
| V-2 | replay selftest | `python3 tools/gates/argot-derivation-gate.py --selftest` | `selftest: 27/27 checks passed` | 0 |
| V-3 | law gate | `python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | `law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0` | 0 |
| V-4 | law selftest | `python3 tools/gates/register-law-gate.py --selftest` | `selftest: 45/45 checks passed` | 0 |
| V-5 | typed pipeline | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `ok L3b-argot` … `summary: 20/20 legs passed` | 0 |
| V-6 | assembler determinism | `python3 tools/assemble-culture-d4.py --check` / `--selftest` | `packet.d4.yml: byte-identical deterministic assembly` / `81/81 checks passed` | 0 |
| V-7 | gate battery | `python3 tools/check-gate-battery.py` | `{"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}` | 0 |
| V-8 | frozen replay (r26 generation) | `python3 tools/replay-frozen.py tools/gates/frozen/round-26/post-register/MANIFEST.tsv` | `REPLAY MISMATCH: 2 mismatch, 4 reproduced of 6 row(s)` | 0 |

V-8's two mismatches are the historical pre-register D4 rows inside a **filed r26 generation**,
which every later landing has moved past — the same drift `reports/round-28/scribe/frozen-rows.md:234`
records ("was 6/6 OK at round 27's 19:16Z, red from 19:21Z, still red — three landings on, and
every red is the artifact moving"). It is not a claim-D regression and not a green.

**Note on V-8's first run.** Executed with `TMPDIR=$PWD/.scratch` it reported
`6 could-not-evaluate reason=mirror_unsafe` — the tool refuses a temporary root inside the repo.
Re-run with `TMPDIR=/tmp` it launched and produced the reading above. Both readings are recorded;
neither was smoothed, and no in-tree runner was involved either way.

### 4.2 The register-form domain — before → after, with filed provenance

| reading | value | source |
|---|---|---|
| r25 (claim D's `before`) | `records=156 register_scoped=6 derived_pairs=0` | `reports/round-25/argot/execution-4.md` §1; `SCORECARD.md:312` |
| r26 candidate (design executed in scratch) | `derived_pairs=8` | `reports/round-26/register/execution-4.md` §3; `reports/round-26/audit/x60-register-derivation-spotcheck.md` §4c |
| r26 landed | `records=170 register_scoped=14 derived_pairs=8` | `SCORECARD.md:329` |
| r27 (law landed) | `records=175 register_scoped=14 derived_pairs=8` | `reports/round-27/scribe/frozen-rows.md:91` |
| r28 (RL-4 records landed) | `records=183 register_scoped=14 derived_pairs=8` | `reports/round-28/scribe/frozen-rows.md:89` |
| **r36 baseline `ce103bf` (this seat)** | **`records=187 register_scoped=14 derived_pairs=8 violations=0`** | V-1 above |

`records` moves with each landing; the register domain (`register_scoped=14 derived_pairs=8`)
has been **unmoved since round 26**. That is the honest reading and the one the round-36 report
must carry: the domain was closed three loops before this round, and this round adds no form.

### 4.3 The forms, enumerated (so the report does not paraphrase them)

Parsed from `examples/culture-d4/packet.d4.yml` (block records carrying `derived_from`):

| record | base | op | axis | `doublet_of` | component line |
|---|---|---|---|---|---|
| L-56 `kit` | `tik` | reverse | mark | L-42 | `04-lexicon.yml:236` |
| L-57 `lom` | `mol` | reverse | mark | L-38 | `:237` |
| L-55 `tuum` | `tum` | lengthen | fire | L-02 | `:238` |
| L-58 `nees` | `nes` | lengthen | fire | L-16 | `:239` |
| L-59 `huum` | `hum` | lengthen | fire | L-09 | `:240` |
| L-60 `mees` | `mes` | lengthen | fire | L-43 | `:241` |
| L-61 `reek` | `rek` | lengthen | fire | L-37 | `:242` |
| L-62 `saam` | `sam` | lengthen | fire | L-39 | `:243` |

**Count discipline.** `grep -o 'register: "stamp"' packet.d4.yml | wc -l` → **20**, of which
exactly **8** are lexicon form records; the other 12 are the law rows — **7** in the `registers:`
block (QREG-02..08; `QREG-01` is `register: plain`, the unmarked baseline) and **5** in the
`register_law:` block (RGL-01..05). A report that quotes "20 register rows" as "20 forms"
overstates the domain by 2.5×. The form count is the `derived_pairs` counter (8), not a grep.

### 4.4 What is still genuinely open (named, not smoothed)

| gap | measured | evidence |
|---|---|---|
| **G-A** the `doublets:` packet block is representable and unpopulated | `grep -c doublets examples/culture-d4/packet.d4.yml` → 0; `PACKET_KEYS` admits it (`tools/assemble-culture-d4.py:81`) | forecast Δ2 (`reports/round-17/d4/design-brief.md:283-295`) |
| **G-B** the pair relation is one-directional | the eight register records carry `doublet_of`; no base record points forward | `grep -c doublet_of 04-lexicon.yml` → 9 (8 records + 1 comment) |
| **G-C** the law leg is not wired | `grep -c 'register-law\|register_law' tools/gates/typed-pipeline-gate.py` → 0; `grep -c 'register-law-gate' tools/gates/typed-pipelines.json` → 0 | V-3 runs as a standalone script only |
| **G-D** the forecast's coverage keys are absent | `derived_forms` / `derived_ok` → 0 files in `examples/` and 0 in `tools/`; the gate prints `derived_pairs` instead | `reports/round-25/argot/delta.md` §8.2 item 1; forecast F-6 (`design-brief.md:306-307`) |
| **G-E** the era leg (RLAW-04) is unimplemented | `grep -c D4L-ERA tools/gates/argot-derivation-gate.py` → 0; `D4L-REGISTER-UNRESOLVED` → 0 files under `tools/` and `examples/` | `reports/round-27/law/rules.md` §1 |
| **G-F** `head2`'s proper domain is all but empty over the delivered tree | 61 of 62 delivered terms are `head2`-identities; the single non-identity is `haitun` → `hai` (`04-lexicon.yml:212`) | `reports/round-27/scribe/x54-syllabify-spotcheck.md:525` ("0 of 70") |

G-F is the honest refinement of a filed figure: r26/r27 published "head2 empty proper domain,
59 of 62", then the r27 spotcheck corrected the number to "0 of 70". Measured now with the
gate's own `op_head2`: **1 of 62** non-identity, not 0. The difference is a **counted set**
(62 lexicon `term` rows vs 70 form records including names) and a **different reading of
`haitun`'s syllabification** — `['ha','i','tun']` → `hai`, where a maximal-onset reading of the
`ai` hiatus could differ. Recorded as `to-verify` against the r27 spotcheck rather than
presented as a contradiction of it: this seat did not re-derive the r27 instrument.

---

## §5 The load-bearing correction: claim D's `before` and `after_required` are stale at `ce103bf`

Claim D (`reports/round-36/claims.json:16-21`) reads:

> `before`: "Register-form domain empty (`reports/round-25/argot/` + SCORECARD r25 row); register
> law/strata exist but the form class has no instances"
> `after_required`: "register-form domain non-empty with verified forms (derivation replay clean
> over the new forms; law gate exit 0 over them; typed pipeline holds updated with named gaps);
> every pin re-frozen as a new row; filed r25-r35 bytes untouched"

Measured at the round's own baseline (§4.1, §4.2, §4.3):

| clause | state at `ce103bf` |
|---|---|
| "register-form domain empty" | **false** — 8 forms delivered, `derived_pairs=8` |
| "the form class has no instances" | **false** — 8 instances, all `register: stamp` |
| "register law/strata exist" | **true and more** — law *and* forms *and* both replay legs delivered |
| "derivation replay clean over the new forms" | **already true** — V-1 `violations=0` |
| "law gate exit 0 over them" | **already true** — V-3 `findings=0` |
| "typed pipeline holds updated with named gaps" | **already true** — V-5 `20/20`, holds `{hold:12, note:0, fail:0}` |
| "every pin re-frozen as a new row" | **already done** — r26/r27/r28/r30 each filed a new pin generation (`examples/culture-d4/expected-holds.json` `pin_generations`: r28 `543d68a8…`, r30 `aac91246c…`, `active_pin_generation: round-30-qreg-records`) |
| "filed r25-r35 bytes untouched" | **true** — `git status --porcelain` clean; no seat may write them |

**The premise is a round-25 record that was never re-measured when round 36's claim was
written.** `SCORECARD.md:312` (the r25 row) carries it verbatim; `SCORECARD.md:329` (the r26
row) records the closure: *"The round-17 register forecast CLOSED: the `stamp` attestation
register lands … 8 verified register forms … derivation replay clean (8 derived pairs, 0
violations over 170 records)"*. `reports/round-30/loop3-retrospective.md:27` says it a third
time. The claim's own `before` cites "SCORECARD r25 row" — and the r25 row is superseded by the
r26 row in the same file, 17 lines below it.

**What this means for the round, stated plainly and not smoothed.** Claim D as written cannot
"improve" the depth axis by building what is already built; a round that re-drafts the eight
form records would be dead work duplicating filed bytes, and a round that claims the closure as
its own after-state would be claiming three earlier rounds' work. Two honest dispositions exist
and **the choice is the integrator's, not this seat's** (`AGENTS.md`: report contested scope,
do not absorb it):

- **(i) Re-scope claim D to what is genuinely open** — §4.4's G-A/G-B (the `doublets:` block and
  the base-side pointer, both representable inside the existing contract), G-C (wire the law
  leg into the pipeline), G-D (the forecast's `derived_forms`/`derived_ok` keys), G-E (the era
  leg). Each is a real depth move with a falsifiable before→after.
- **(ii) Report claim D `harmed`/`unprovable` at the premise and halt depth progression there**,
  per `REGIMEN.md` ("never force a pass — rounds 11/17/22 precedent"). The round still lands
  the correction, which is itself the depth value.

This seat recommends **(i)** but does not decide it. Either way the round-36 SCORECARD row must
carry the corrected before-state, because a row that repeats "domain empty" would file a
measurement the r26 row already falsified.

**Convergent independent finding — the D block's whole wave reached it.** The stale premise was
measured independently by **twelve** seats in this round, each on its own instrument:

| seat | fragment | how it reached the finding |
|---|---|---|
| D01 | `depth/D01-design.md` §0 | its own gate read + `git log -S "register: stamp"` landing history |
| D02 | `depth/D02-packet-draft.md` §0 | its own gate read, quoting `packet.d4.yml:1053`/`:1163` for `L-55`/`L-62` |
| D03 | `depth/D03-isolated-verify.md` §1 | an **independent re-derivation** (own parser, own `op` implementations), never a gate's stdout |
| D05 | `depth/D05-receipt.md` §0 | live measurement in its own window |
| D06 | `depth/D06-gap-fill.md` §1 | the spare's premise falsification |
| D09 | `depth/D09-gap-fill.md` | the second spare |
| K01 | `scout/K01-register-scout.md` | the scout, with SCORECARD row lineage |
| P01 | `plan/P01-d-plan.md` §0 | the planner, which re-aimed the plan onto the open surface |
| R01 | `review/R01-d-review.md` §0 | reviewer; pins the landing commit `4f09c99` and dates the transition |
| R02 | `review/R02-d-review.md` §1 | reviewer; reproduced with its own commands |
| **D07** | **`depth/D07-verify.md` §1** | **verifier; its own text-level parse (no gate stdout), 8/8 forms re-deriving, and an independent decomposition of `register_scoped=14` into 8 forms + 6 loans** |
| X02 | `cross/X02-conformance.md` §0 | the conformance critic, under the heading "claim D's declared `before` is stale and its `after` is already true" |
| **D10** | **this file** §4, §5 | this seat's own gate read + component census + the 20-vs-8 count discipline |

That is twelve seats on one baseline with independent commands. Claim D's threshold ("forms
verified by two independent seats") is therefore **satisfied for the correction itself** — and
D07 supplies this round's own independent read of *the forms* (its §1 table, 8/8 re-deriving),
which is the same-round second read §`Owed` previously listed as owed. The r26 pair
(`reports/round-26/audit/x60-register-derivation-spotcheck.md` + `reports/round-26/register/review.md`
§1 row G-5) remains the *filed* two-seat verification of the forms' landing.

**D07's one unreproduced figure, carried not smoothed.** D07 could not reproduce D03 §5's
post-Draft component digest `0f0828731366ce52` from D01's filed prose across 400+ layout
variants, and files it as a named discrepancy (`depth/D07-verify.md` §3). This seat did not
attempt that reproduction (it is D03's rehearsal figure, not a live-tree digest) and records the
discrepancy with D07 as its owner. It does **not** touch §4's live digests, which this seat
measured directly and which agree with D03's `before` column.

### §5.3 A genuinely open, actionable gap the D block found: **R02-D-6**

Claim D's `after_required` asks for "every pin re-frozen as a new row". Measured first-hand by
this seat, **half of that is done and the half that is missing is the one that grades the forms**:

| leg | script | frozen baseline | registered in the battery |
|---|---|---|---|
| register **law** | `tools/gates/register-law-gate.py` | **yes** — `tools/gates/expected/register-law-gate/r30-post/expected.json` | **yes** — `REGISTER_LAW_GATE_NAMES` |
| register **form** (derivation replay) | `tools/gates/argot-derivation-gate.py` | **no** — no `expected.json` under any `expected/`/`frozen/` root names it | **no** — absent from `REGISTERED_GATE_NAMES` |

This seat's own reproduction:

```
$ python3 tools/check-gate-battery.py | <baselines.summary>
{"baseline_exit": 0, "baselines_found": 20, "coverage": "10/10", "pinned": 20,
 "gates_covered": [..., "register-law-gate.py"], "gates_uncovered": [], "unevaluable": 0}
$ python3 -c "<import tools/check-gate-battery.py>"
GATE_NAMES 7; D4_GATE_NAMES ('d4-typed-labels-check-gate.py','d4-assembly-check-gate.py')
REGISTER_LAW_GATE_NAMES ('register-law-gate.py',); REGISTERED count 10
argot registered? False
```

So the derivation-replay leg — the one that grades the eight register forms this claim is about —
runs inside per-round runners but has **no frozen verdict row and no battery registration**, and
nothing replays its verdict outside a round runner. R02 files this as **R02-D-6**
(`review/R02-d-review.md` §6); this seat reproduced the census independently. **This is the
actionable residue of claim D**, and it is the strongest candidate for disposition (i) in the
list above.

**R02-D-8, folded as a correction to a peer.** R02 audited D03's §3.2 `domain-emptied` control and
found it does **not** reproduce as written: the named transform yields `register_scoped=6`,
`borrow_pairs=6`, exit 1 and a fired `D4L-ARGOT-COVERAGE` hold — not the `0`/`0`/`0` the row
reports (`review/R02-d-review.md` §8). R01 independently reached the same correction
(**R01-D-1**, `review/R01-d-review.md` §6.2), and it runs in the *favourable* direction: the
coverage hold **does** catch an emptied domain, so the r25 failure mode is closed rather than
reproduced. This seat did not re-run the control; both reviewers did, independently of each other,
and this receipt records the disagreement as resolved in favour of the reviewers' measurement
because two seats reproduced it against one. `reports/round-36/depth/D03-isolated-verify.md` §3.2
is **not** edited — filed-round bytes are untouched, and D03 is a peer fragment, not this seat's
to rewrite.

**A stale cross-reference in D08, for the integrator.** D08's citations
(`depth/D08-verify-repin.md:376`) point at `D10-scribe.md:72` and `:174` as recording D04 owed.
Those were true line numbers of this fragment's **first draft**; both paths have since been
rewritten (D04 and D08 landed, and this receipt was revised around them), so the quoted lines no
longer say that. This is the normal hazard of a peer citing a moving draft, not a D08 error.
D08's own `to-verify` record for D04 stands and is now resolvable: `depth/D04-repin.md` landed.

---

## §6 The r7 freeze read-set finding (cross-block, for X00/R03)

The round-34 handoff revision is a **filed** artifact whose bytes are pinned, and its read set
was recomputed by this seat:

```
$ python3 -c "<sha256 each of reports/round-34/handoff/declared-in-r7/expected.json #inputs
             against the live file>"
r7 read-set: ok 58 mismatch 0 missing 0 total 58
```

Every one of the 58 declared inputs still matches its pinned digest at `ce103bf` — including
all 19 D4 members. The freeze is intact and **no seat may re-freeze it** (the ABSOLUTE rule).

Two consequences the D block must carry:

1. **`examples/culture-d4/components/13-register-law.yml` is NOT a read-set member.** The r7
   read set names **12** D4 components — `01-brief` … `12-provenance` — plus the packet, typed
   packet, projection, expected-holds, assembler and the two `.md` files (19 D4 members in all;
   `python3` count over `expected.json#inputs`). The register-law component (landed r27, i.e.
   **after** the r7 read set was derived from the r6 renderer
   inputs) is absent. `reports/round-34/handoff/declared-in-r7/packet.md` carries 24
   `register`/`RGL-`/`QREG-` lines, so the packet *does* describe the register — but the law
   component's own digest is not among the 58 pinned inputs. A reader who assumes "the r7 read
   set is the D4 component set" will be wrong by one file.
2. **Therefore any D-block change to a read-set member moves the r7 packet digest**, and the
   r7 pair cannot be re-frozen to absorb it. D01's `doublets:` draft (G-A) would edit
   `04-lexicon.yml`, which **is** read-set member 4 — so G-A's landing is a genuine collision
   with a pinned revision, not a free component edit. X00's collision matrix and R03's cross
   review own the resolution; this seat reports it with the measurement.

---

## §7 This seat's writes and non-writes

**Written:** `reports/round-36/depth/D10-scribe.md` (this file). Nothing else durable. Two
read-only command families ran with `TMPDIR=$PWD/.scratch` (V-1..V-7) and one with `TMPDIR=/tmp`
(V-8, §4.1 note); the first `replay-frozen` attempt's refusal left a transient tree under
`.scratch/` which is gitignored and named in §4.1.

**Not written:** no `examples/**`, no `tools/**`, no `corpus/**`, no `reports/round-1..35/**`,
no `tools/gates/frozen/**`, no `.ufo/**`, no `SCORECARD.md`, no `LOG.md`, no pin, no
`run-validation.py`, and **none of the `reports/round-3x/validation.json` paths named below**.
No commit, no push, no install, no network call. No `reports/round-*/run-validation.py` was
executed anywhere. No `--freeze` was run.

**The dirty paths in the tree are not this seat's, and they moved.** Across this window
`git status --porcelain` went from `?? reports/round-36/` only, to
` M reports/round-34/validation.json` (mtime 06:32:04, re-touched 06:32:16 -0300), to at close
` M reports/round-35/validation.json` (mtime 06:33:23 -0300) — with the round-34 path clean
again. The full table is in §2. This seat's only in-tree write is
`reports/round-36/depth/D10-scribe.md`. `reports/round-1..35/**` is filed-bytes territory under
the shared rules, the modifications are another seat's or the parent's, and D03 §6 observed the
round-34 row from its own window. This seat did not create, revert, or read-after-change any of
those paths; the reconciliation belongs to the round's O/adjacency seat or the parent. The claim
"this seat moved no tracked byte" stands; the claim "the tracked tree is byte-clean" **does not
hold at this window's close** and is not asserted.

---

## Owed

- `reports/round-36/run-validation.py` — **the only D-block artifact still absent at this seat's
  close** (`ls` → exit 2). It is claim D's own counting command (`claims.json:20`) *and* the
  integration pass's output. Until it lands and exits 0, claim D's `counting_commands` are
  **unsatisfied**, and §4.1's per-leg readings stand in as the measured evidence. Owner: the
  integration pass. (R02-D-7 files the same gap; S01's dossier carries the leg spec it implements.)
- `reports/round-36/validation.json` — same owner, same dependency.
- `reports/round-36/depth/D04-repin.md` and `depth/D08-verify-repin.md` — **both landed at this
  seat's close**, resolving what an earlier draft of this fragment listed as owed. D04 measures
  the re-pin list on three isolated copies rather than deriving it, and names the row set as its
  deliverable (digests re-measured by the integrator on the landed bytes); D08 falsifies the
  census by mutation across nine pin surfaces without accepting any sibling's list. D03 §5's
  cascade and D04's list should be diffed by the integrator — they were produced independently.
- `reports/round-36/depth/D07-verify.md` — **landed at this seat's close.** It rebuilt its own
  `git archive ce103bf` copy, reproduced D03's legs exactly, re-derived 8/8 forms by text-level
  parse, and confirmed the stale premise. So claim D's threshold ("forms verified by two
  independent seats") is met **within this round** for both the correction (twelve seats, §5) and
  the forms (D07 §1 plus D03 §1's independent re-derivation). D07's one unreproduced figure
  (`0f0828731366ce52`, §5 above) is owed to D07.
- `reports/round-36/scribe/S01-integration-draft.md` — **landed at this seat's close**; the
  integration dossier, the validation-leg spec for `reports/round-36/run-validation.py`, and the
  selftest control list. §4.1's five leg names are the ones it should carry; the integrator
  reconciles the two lists.
- The **disposition of claim D** (§5): re-scope onto the open surface (now with **R02-D-6** as the
  strongest candidate, §5.3), or report `harmed`/`unprovable` at the premise. Owner: the
  integrator; this seat recommends the re-scope and decides nothing. **Two independent reviewers
  (R01, R02), the planner (P01), the verifiers (D03, D07) and the scribes (D05, D10) have all
  reached the same "cannot verify as filed" reading**, so the round cannot honestly record a
  claim-D pass as written.
- **G-F's count reconciliation** — 1 of 62 (this seat, gate's own `op_head2`) vs "0 of 70"
  (`reports/round-27/scribe/x54-syllabify-spotcheck.md:525`). The two counts use different
  sets and possibly different syllabifications of `haitun`'s `ai` hiatus. Owner: a seat that
  re-derives the r27 instrument; marked `to-verify` here.
- **The moving ` M reports/round-3x/validation.json` row** (§2, §7) — filed round-34, then
  round-35, `validation.json` paths modified during this round's window by another seat or the
  parent (an in-flight writer; the path moved and the earlier one went clean). D03 §6 flagged the
  round-34 row from its own window. Owner: the round's O/adjacency seat or the parent. This seat
  did not touch, revert, or read-after-change any of them, and its own byte-cleanliness claim is
  narrowed in §7 accordingly.
- **D03 §3.2's `domain-emptied` control** — corrected by R01-D-1 and R02-D-8 (§5.3), which agree
  the named transform fires `D4L-ARGOT-COVERAGE` at exit 1 rather than passing silently. D03's
  fragment is a peer's filed-in-this-round byte; the correction is recorded here rather than by
  editing it. Owner: the integrator, when folding D03.
- `reports/round-36/telemetry/` — the observed-dispatch record for the devin fallback and the
  closing snapshot owed once `validation.json` lands (`AGENTS.md` §telemetry). Owner: the
  integrating parent. S02's telemetry draft (`scribe/S02-telemetry-draft.md`) landed and carries
  the skeleton.

## Citations

Paths:lines and command outputs. Every command ran from the lane root
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` unless a §4.1 note says otherwise.

**Binding files**

- `reports/round-36/targets.json` — seat `D10` (role scribe, claim D, out `depth/D10-scribe.md`),
  `shared_rules` (6 entries), `seat_count: 32` / `len(seats)` → 32.
- `reports/round-36/claims.json:16-21` — claim D's `before`/`after_required`/`counting_commands`/
  `thresholds`; `:22-27` — claim C; `:28-33` — claim Ca; `:35-36` — `non_goals`.
- `reports/round-36/telemetry/availability-attempt-1.json` — 32 requested, 0 launched, 32 failed,
  `402 You're out of credits`; `telemetry/dispatch-declared.json` — declared hyper route,
  `closing_snapshot: "open-at-seat-close: owed once validation.json lands"`, sha256 of
  `claims.json` `b8d1af8f…` and `targets.json` `39ddbc72…` (this seat reproduced both).
- `REGIMEN.md` — position 4 (hyper, declared devin fallback), per-round contract, honest-stop rule.

**Baseline and digests (this seat, 2026-10-19)**

```
$ git rev-parse HEAD
ce103bf5885af00023cdc4a174c17602476cdcf8
$ git status --porcelain                      # at this seat's FIRST reads
?? reports/round-36/
$ git status --porcelain                      # MID-window
 M reports/round-34/validation.json
?? reports/round-36/
$ git status --porcelain                      # at this seat's CLOSE — the path MOVED
 M reports/round-35/validation.json
?? reports/round-36/
$ stat -c '%y %n' reports/round-34/validation.json reports/round-35/validation.json
2026-10-19 06:32:16.341320239 -0300 reports/round-34/validation.json
2026-10-19 06:33:23.612225120 -0300 reports/round-35/validation.json
$ git diff --stat HEAD -- reports/
 reports/round-35/validation.json | 6 ++----
 1 file changed, 2 insertions(+), 4 deletions(-)
$ sha256sum examples/culture-d4/components/04-lexicon.yml \
            examples/culture-d4/components/13-register-law.yml \
            examples/culture-d4/packet.d4.yml \
            examples/culture-d4/packet.d4.typed.yml \
            examples/culture-d4/expected-holds.json \
            tools/gates/argot-derivation-gate.py \
            tools/gates/register-law-gate.py \
            tools/gates/typed-pipeline-gate.py
ed7093d6b92111c2300e7c04b9100f9e57f6d5802101b69335f9fe138858755d  examples/culture-d4/components/04-lexicon.yml
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182  examples/culture-d4/packet.d4.typed.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85  tools/gates/typed-pipeline-gate.py
```

**§0 dependency state**

```
$ find reports/round-36 -type f | sort
reports/round-36/claims.json
reports/round-36/cov/C01-audit.md
reports/round-36/cross/X02-conformance.md
reports/round-36/depth/D01-design.md
reports/round-36/targets.json
reports/round-36/telemetry/availability-attempt-1.json
reports/round-36/telemetry/dispatch-declared.json
$ ls reports/round-36/run-validation.py
ls: cannot access 'reports/round-36/run-validation.py': No such file or directory
```

**§4.1 legs** — V-1..V-7 outputs are quoted verbatim in the table; all exits 0. V-8's two runs:

```
$ export TMPDIR=$PWD/.scratch; python3 tools/replay-frozen.py tools/gates/frozen/round-26/post-register/MANIFEST.tsv
ROW 5 could-not-evaluate reason=mirror_unsafe …
REPLAY COULD-NOT-EVALUATE: 6 could-not-evaluate, 0 mismatch, 0 reproduced of 6 row(s)
$ export TMPDIR=/tmp; python3 tools/replay-frozen.py tools/gates/frozen/round-26/post-register/MANIFEST.tsv
ROW 4 reproduced … ROW 7 reproduced …
REPLAY MISMATCH: 2 mismatch, 4 reproduced of 6 row(s)
$ python3 tools/check-gate-battery.py
"summary": {"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}
```

**§4.2 the domain's history (filed bytes, quoted)**

- `SCORECARD.md:312` (r25 row, the stale premise), `:329` (r26 row, the closure),
  `:345` (r27, the law), `:363` (r28, the law replay leg), `:391` (r30, the integrate round).
- `reports/round-25/argot/execution-4.md:1,35` — "zero register forms to replay", the r25 census.
- `reports/round-26/register/execution-4.md` §2-§4 — census A (delivered `derived_pairs=0`) vs
  census B (candidate `derived_pairs=8`).
- `reports/round-26/audit/x60-register-derivation-spotcheck.md` §4c — the independent instrument,
  "independent-reading-agrees-with-lane-gate ok".
- `reports/round-27/scribe/frozen-rows.md:91` — "**The register domain is no longer empty**".
- `reports/round-28/scribe/frozen-rows.md:89-90` — `records` moves, the domain does not.
- `reports/round-30/loop3-retrospective.md:27-28` — the same story in the retro table.
- `reports/round-29/recount/r25-3.md:11` — the r25 argot command reproduced from the pinned snapshot.
- `examples/culture-d4/expected-holds.json` — `active_pin_generation: round-30-qreg-records`,
  `counts {hold: 12, note: 0, fail: 0}`, `pin_generations` r28 `543d68a8…` / r30 `aac91246c…`.

**§4.3 form census (this seat's parse)**

```
$ python3 - <<'PY'   # split packet on "\n  -\n", keep blocks with derived_from
blocks with derived_from: 9   # 8 lexicon records + the R30-QREG-ACTS section header block
 L-56 stamp reverse / L-57 stamp reverse / L-55 stamp lengthen / L-58 stamp lengthen
 L-59 stamp lengthen / L-60 stamp lengthen / L-61 stamp lengthen / L-62 stamp lengthen
PY
$ grep -o 'register: "stamp"' examples/culture-d4/packet.d4.yml | wc -l      # 20
$ grep -c 'register: stamp, derived_from' examples/culture-d4/components/04-lexicon.yml   # 8
$ grep -o 'register: stamp' examples/culture-d4/components/04-lexicon.yml | wc -l         # 16
$ grep -c 'derived_from:' examples/culture-d4/components/04-lexicon.yml        # 8
$ grep -c 'doublet_of:'  examples/culture-d4/components/04-lexicon.yml         # 8
$ sed -n '236,243p' examples/culture-d4/components/04-lexicon.yml              # the 8 records
```

**§4.4 gaps**

- G-A/G-B: `grep -c doublets examples/culture-d4/packet.d4.yml` → 0; every
  `examples/culture-d4/components/*.yml` → 0; `tools/assemble-culture-d4.py:81`
  (`PACKET_KEYS` includes `"doublets"`), `:122` (`RECORD_FIELDS["doublets"] = ("id",)`),
  `:469-471` (fixture template emits a `doublets:` block); forecast authority
  `reports/round-17/d4/design-brief.md:283-295`.
- G-C: `grep -c 'register-law\|register_law' tools/gates/typed-pipeline-gate.py` → 0;
  `grep -c 'register-law-gate' tools/gates/typed-pipelines.json` → 0;
  `tools/gates/typed-pipeline-gate.py:517-541` is the argot leg's wiring (present).
- G-D: `derived_forms` / `derived_ok` → `examples/` 0, `tools/` 0, `reports/` 18 (prose only);
  `reports/round-25/argot/delta.md:255` §8.2 item 1 ("F-6 remains NOT DELIVERED").
- G-E: `grep -c 'D4L-ERA' tools/gates/argot-derivation-gate.py` → 0;
  `grep -rl 'D4L-REGISTER-UNRESOLVED' tools/ examples/ | wc -l` → 0;
  `reports/round-27/law/rules.md` §1 (RLAW-01..06, only RLAW-06 replayable).
- G-F: `op_head2` imported from `tools/gates/argot-derivation-gate.py:243` (`OP_FUNCTIONS`);
  61 of 62 delivered `term` rows are identities, `haitun` → `hai`
  (`examples/culture-d4/components/04-lexicon.yml:212`); the filed figures are
  `reports/round-26/register/review.md` §4 (RD-3, line 110: "head2(form)==form
  (identity, not a derivation): 59 of 62") and
  `reports/round-27/scribe/x54-syllabify-spotcheck.md:525` (0 of 70).

**§6 the r7 read set (this seat's recomputation)**

```
$ python3 - <<'PY'   # sha256 each input in reports/round-34/handoff/declared-in-r7/expected.json
r7 read-set: ok 58 mismatch 0 missing 0 total 58
D4 members: 19
  examples/culture-d4/ASSEMBLY.md … components/01-brief.yml … components/12-provenance.yml
  examples/culture-d4/{expected-holds.json,packet.d4.typed.yml,packet.d4.yml,typed-labels.d4.yml}
  tools/assemble-culture-d4.py
  # components/13-register-law.yml — ABSENT
PY
$ grep -c 'register\|RGL-0\|QREG-0' reports/round-34/handoff/declared-in-r7/packet.md   # 24
$ head -8 reports/round-34/handoff/declared-in-r7/freeze.txt
frozen: 2026-10-19 by tools/exercise-handoff-e2e.py --profile v3
packet_sha256: 45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
gate: exit 0, fields=16/16, glossary-entries=20, findings=0
read set: 58 files; component digests 26/26; d4 pins 8/8
```

**Peer fragments folded (their bytes were read; every number this receipt asserts was re-taken
first-hand, and where a peer's figure is quoted it is attributed)**

- `reports/round-36/depth/D01-design.md` §0 — the convergent stale-premise finding.
- `reports/round-36/depth/D02-packet-draft.md` §0-§1 — the packet-block draft; the double-grade
  hazard at `tools/gates/argot-derivation-gate.py:304-314`, `:549`.
- `reports/round-36/depth/D03-isolated-verify.md` §0-§6 — the isolated apply-and-verify; §5's pin
  cascade table (7 live surfaces with before→after digests), §5's two-pass self-referential
  hazard, §6's ` M reports/round-34/validation.json` observation.
- `reports/round-36/depth/D05-receipt.md` §0 — the depth receipt.
- `reports/round-36/depth/D06-gap-fill.md` §1, `depth/D09-gap-fill.md` — the two spares.
- `reports/round-36/depth/D07-verify.md` §0-§7 — the independent verification: its own
  `git archive ce103bf` rebuilds, D03's legs reproduced, the §1 8/8 re-derivation table, the
  §3 unreproduced digest `0f0828731366ce52`, the §6 r7 read-set answer.
- `reports/round-36/plan/P01-d-plan.md` §0, §4.2-§4.3 — the plan; "Surface A + B-1 only"; B-2
  priced as a contract amendment.
- `reports/round-36/scout/K01-register-scout.md` — the register scout and the SCORECARD lineage.
- `reports/round-36/review/R01-d-review.md` §0, §6.2 — reviewer verdicts; **R01-D-1** (the
  `domain-emptied` control correction); the landing commit `4f09c99`.
- `reports/round-36/review/R02-d-review.md` §1, §6, §8 — reviewer verdicts; **R02-D-6** (the
  form leg has no baseline and no registration — reproduced first-hand in §5.3);
  **R02-D-7** (the counting command is absent); **R02-D-8** (D03 §3.2 correction).
- `reports/round-36/cross/X00-connector.md` — the collision matrix (owned by X00; §6 defers to it).
- `reports/round-36/cross/X02-conformance.md` §0 — the conformance critic's statement of the same
  finding, under the heading "claim D's declared `before` is stale and its `after` is already true"
  (its audit instant 2026-10-19T09:26:38Z).
- `reports/round-36/cov/C01-audit.md` — claim C's block, read for the report's C material, not
  folded into this D fragment.
- `reports/round-36/scribe/S02-telemetry-draft.md` — the telemetry draft and closing-snapshot
  skeleton (owned by S02; §`Owed` defers to it).

**Not executed (F-C13-1 prevention):** no `reports/round-*/run-validation.py`, in-tree or in a
copy; no `--freeze` of `reports/round-34/handoff/declared-in-r7`.
