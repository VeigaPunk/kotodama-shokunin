# R25-O16..O17 — regression sweep (initial + closing)

**Operational regression verdict: GREEN at the closing stamp.** Battery, craft, every
runnable typed/assembly selftest and production check, the d2/d4 gates, the two D4
adapters, handoff v2/v3, the projector suites, the harness selftests and the new
argot-derivation gate all pass after the round-25 wave landed. The **11** nonzero matrix
legs at close break down as **six documented historical/known controls** (round-11,
round-18, round-3 and round-3/attempt-1 manifests; `tie-break --check`; the flagless
`d4-assembly-check-gate.py`), **one deliberate negative fixture** (the argot gate's own
control), and **four declared pin-cascade refusals** — every one named below, none
rewritten. This is a regression measurement, not round acceptance, canon clearance, or a
claim that historical manifests exit zero.

## Isolation, revision and evidence

- Observation date: **2026-10-18**. Times are **UTC−03:00**; each table row's time is
  that command's start, not a claimed completion time.
- Before scratch-writing commands: `export TMPDIR=$PWD/.scratch;
  export PYTHONDONTWRITEBYTECODE=1` from the lane root.
- Driver: `python3 .scratch/r25-o16-o17-regression/sweep.py <phase>`. Each phase creates
  a real Git clone under `.scratch/r25-o16-o17-regression/<phase>/repo`, overlays the
  measured live working-tree bytes plus manifest-referenced ignored receipts, and runs
  the whole matrix inside the clone with a per-command TMPDIR root. Every result row
  records argv, dated start/end, exit, and stream SHA-256. The isolation matters here
  because the battery is fail-closed on a live-tree edit and 64 workers were writing
  concurrently. **No round validator was executed by this seat**, in the live lane or
  otherwise; the round-25 runner's own regression inventory is a different instrument
  and its verdict is the parent's.
- Binding: lane `HEAD = f74fc9403d4b02c8ee76439eb133e3dea9b65b14` (round-25 declare
  commit); declared baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`
  (`reports/round-25/claims.json:5`). Both sweeps measure the **uncommitted integration
  overlay** at that HEAD, not an assertion that HEAD contains it.
- Raw evidence: `.scratch/r25-o16-o17-regression/{initial,closing}/{snapshot,source-manifest,results}.json`
  and per-command `*.stdout.txt` / `*.stderr.txt`. The filed evidence is this report
  alone; no shared bookkeeping or source file is this seat's write.

## Initial sweep (R25-O16) — pre-fix binding

- `python3 .scratch/r25-o16-o17-regression/sweep.py initial`, clone/snapshot started
  **14:25:16**, matrix completed **14:26:03**. Snapshot: **1,977** inputs, copied-manifest
  SHA-256 `4dbc1bc32c96e27a…`, `source_drift_after_copy: []`.
- Matrix: **45** commands, **39** exit-zero. All my assigned surfaces green; the six
  nonzeros were the pre-existing controls listed below (round-11, round-18, round-3 ×2,
  `tie-break --check`, `d4-assembly-gate-selftest`). The derived-packet hazard was live at
  this stamp but is measured by the live capture below, since this sweep predates the
  derived-packet leg.
- Preservation: `clone_copied_paths_changed: []`, `source_changes_since_snapshot: []`,
  **1,350** locked historical paths (rounds 8–24 reports + all frozen generations outside
  round-25) with `locked_paths_changed: []`.

## Closing sweep (R25-O17) — post-wave

- Settle: a 60 s watcher (`.scratch/r25-o16-o17-regression/watch.sh`, log `watch.log`)
  hashed the nine pin-relevant surfaces every minute from 14:26:58. The digest changed three
  times (14:30:58, 14:31:58, 14:33:58) and then held byte-identical for **six** consecutive
  samples (14:33:58 → 14:38:58), which covers the whole closing matrix. The closing sweep
  began at 14:37:34.
- `python3 .scratch/r25-o16-o17-regression/sweep.py closing`, clone/snapshot started
  **14:37:34**, matrix completed **14:38:26**. Snapshot: **2,045** inputs, copied-manifest
  SHA-256 `64eaf2671957cc06…`. One live file changed between copy and check —
  `reports/round-25/scribe/fragment-ledger.md` (a concurrent seat's write, recorded in
  `source_drift_after_copy`); it is not in the executed set and not a source this seat
  reads, so the matrix is unaffected. `clone_copied_paths_changed: []`.
- Matrix: **51** commands, **40** exit-zero.

### Current commands — all exit 0 (14:37:35–14:37:39)

| Group | Measured result (command + date: driver above, 2026-10-18) |
|---|---|
| Battery | 7/7 structural selftests, fail 0 / unevaluable 0, **19/19** baselines pinned, coverage **9/9**, `preserved: true` (32 files, 0 added/deleted/modified); `--selftest` **35/35** |
| Craft | **10/10** tamper + **18/18** CLI selftests; full check `audits=7, mech_cases=11, derivations=9, approx_checks_runner=37`; census 5 supported / 2 unresolved / 0 contradicted, 1 blocked |
| Assembly | d2 **42/42**, d2-typed **11/11**, d3 **85/85**, d4 **81/81**, d4-typed **12/12** selftests; all five production `--check` outputs byte-identical |
| Projector | `d2-typed-labels.py --selftest` **163/163** (the D4 label gate delegates the same suite); D2 and D4 projections byte-identical |
| Typed gate | `--selftest` **19/19** (grew from 12/12 as the argot and input-class legs landed), `--selftest-generalized` **14/14**; D2 default **16/16**; D4 source **19/19**; D4 derived **16/16** (see below) |
| d2/d4 gates | D4 label gate `--selftest` **163/163**, projection byte-identical; D4 assembly gate on the source packet byte-identical |
| Argot gate (new) | `--selftest` **18/18**; D4 run exit 0 (`records=156 register_scoped=6 derived_pairs=0 borrow_pairs=6 violations=0 rule_holds=0`) |
| Handoff | v2 exit 0, claims 15, links **50/50**, named drift only; v2 `--selftest` exit 0; v3 `--selftest` exit 0 (39 controls); v3 exit 0, fields **16/16**, glossary **20/20**, findings 0, links **105/105**, v2 subset equal, packet sha `a97a0f0a…` |
| Harness | coupling selftest + D3 packet zero findings; packet_links **38**; packet_uncertainty **19**; replay-frozen selftest **79/79** |
| Selector control | `tie-break.py --root . --selftest` exit 0, **23/23** controls |

### The O-hazard, measured — before and after

The round-24 cold run recorded that feeding the gate its own derived artifact exits 1 with
manufactured findings (`reports/round-24/cold-run-conditions.md` C2, `cold-run-fixes.md`
FX7). This seat reproduced it independently before the fix and re-measured after. The
pre-fix readings are live-lane manual captures taken at **14:25:1x** (raw stdout
`.scratch/r25-derived-in.out`, `.scratch/r25-source-in.out`) against the pre-fix gate digest
`04ad4bb4…` — the sweep driver only gained these legs afterwards, so the initial **clone**
matrix (which predates them) is not the source of the pre-fix column; the closing column is
the closing clone matrix at 14:37:38.

| Entry (2026-10-18) | pre-fix 14:25 (live capture, gate `04ad4bb4…`) | closing 14:37 (clone matrix, gate `879d40bf…`) |
|---|---|---|
| `typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` (documented source) | exit 0, **19/19** | exit 0, **19/19** |
| `typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` (derived) | exit **1**, **14/16**, 8 `DERIV-REPLAY` FAILs + 6 `'null'` routing rows | exit 0, **16/16**, zero such findings |
| `typed-pipeline-gate.py` (flagless D2 default) | exit 0, 16/16 | exit 0, 16/16 |

Independent mechanism check (not quoted from another seat): `naming-collision-gate.py` run
**directly** on `packet.d4.yml` and on `packet.d4.typed.yml` each emits **zero**
`DERIV-REPLAY` lines, and the typed packet carries 6 literal `owed_slot: null` rows. So the
eight findings the pre-fix gate run printed were manufactured inside the gate's legacy
rebuild, exactly as recorded — the derived red was not a genuine property of either packet.
Gate bytes: pre-fix `04ad4bb479562c419b48d750a8f9303c4a5a717ca7f2fe3b3658cc1bb9578a48` (the
round-22 freeze pin) → closing `879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126`.

### Argot gate — capability control

`tools/gates/argot-derivation-gate.py` (new this round) is measured three ways, so its green
D4 reading is not a vacuous pass. The closing-clone matrix ran it at digest
`07db6e9b4e01539e1dbb8af9e51eada6fe37784145915a0387f48f2ecd99f8fe`; the gate was then
touched again by its owner at **14:41:48** (digest `dbcb43b985064d3d…`) and re-measured live
at **14:42:05** with **identical readings** — so the counts below hold across both bytes:

- `--selftest` → exit 0, **18/18** (including `head2-maximal-onset`,
  `head2-maximal-coda-differs`, `reverse-involution`, `fixture-exits-1`,
  `fixture-ids-match-expected-file`, `fixture-counts-pinned`).
- D4 source packet → exit 0, 6 register-scoped forms, 0 violations.
- Negative fixture `tools/gates/fixtures/argot-derivation-gate.yml` → **exit 1** with four
  `D4L-ARGOT-DERIV` FAILs and one `D4L-ARGOT-RULE` HOLD. This is the discriminator: the
  gate reports findings when the derivation does not replay.

Note for the pin owner: the argot gate carries **no frozen row yet** in
`tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` (0 argot rows), and its digest moved
after the closing sweep. A later freeze must pin the final bytes, and the battery does not
register this gate among its nine, so its conformance evidence is its own selftest and this
measurement.

## Nonzero legs at close — each named, none rewritten

### New round-25 successor generation — replayed green

`python3 tools/replay-frozen.py tools/gates/frozen/round-25/gate-input/MANIFEST.tsv --json`
(2026-10-18, 14:37:39): exit 0, **6/6** recorded verdicts reproduced, zero mismatch /
could-not-evaluate. Four input-class rows (both families, source and typed packet) plus two
fail-closed controls.

### The declared pin cascade — four successor generations, one refused row each

The gate re-pin moves the gate digest, so every earlier generation that pinned the
predecessor now refuses exactly its `typed-pipeline-gate.py` row. The round-25 freeze
receipt (`tools/gates/frozen/round-25/gate-input/freeze.txt`) declares this cascade
verbatim; this sweep reproduces it:

| generation | initial | closing | refused row |
|---|---|---|---|
| `round-18/repin-d2` | 0 (11/11) | **2** | 1 row, `gate_digest_mismatch` on typed-pipeline-gate; other 10 reproduce |
| `round-20/repin-d2` | 0 (11/11) | **2** | same shape, 10 reproduce |
| `round-22/d4-repin` | 0 (3/3) | **2** | same shape, 2 reproduce |
| `round-23/repin-d2` | 0 (11/11) | **2** | same shape, 10 reproduce |

These are **expected, not defects**: the append-only discipline is that a re-pin is a new
recording, so the predecessor generations keep their filed bytes and their superseded pins
read could-not-evaluate once the live gate moves. The successor reading is the new round-25
generation (6/6 green, above).

**Cascade control, executed (not inherited).** In a throwaway copy of the closing clone,
`git show f74fc94:tools/gates/typed-pipeline-gate.py` restored the predecessor blob
(digest `04ad4bb4…`) and every one of the four generations returned to **full
reproduction** — `round-18/repin-d2` 11/11, `round-20/repin-d2` 11/11, `round-22/d4-repin`
3/3, `round-23/repin-d2` 11/11, all exit 0. So the exit-2 readings are attributable to the
single moved gate digest and nothing else. The clone was then restored to the live bytes
(`879d40bf…`); no historical manifest and no lane byte was edited (the live lane's gate
digest is unchanged and its only tracked modification is the same one that was already
there).

### The argot gate's own negative fixture — a deliberate exit 1

`python3 tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml`
(2026-10-18, 14:37:39) → **exit 1** with four `D4L-ARGOT-DERIV` FAILs and one
`D4L-ARGOT-RULE` HOLD. This leg is in the matrix precisely because it *must* be nonzero:
it is the discriminator proving the gate reports findings when a derivation does not
replay, and the gate's `--selftest` pins it (`fixture-exits-1`,
`fixture-ids-match-expected-file`, `fixture-counts-pinned`). Counted as a control, not a
failure.

### Historical negative controls — explicitly nonzero, never rewritten

- `round-11` exit 2 (10/11): the typed row is `gate_digest_mismatch` against the
  pre-generalization pin `d102fd1d…` — documented since round-18.
- `round-18` (the original, not repin-d2) exit 1 (1/2): `replay_mismatch` on the superseded
  D4 projection row.
- `round-3` and `round-3/attempt-1` exit 2 (0/7 each): obsolete gate pins.
- `tie-break.py --root . --check` exit 1 (14:37:38): the documented round-20
  `PLACEHOLDER_RE` false positive plus the stale round-20 v2 digest row, with
  `filed_rounds_8_21_changes: []`. The filed round-20 validator is not claimed to pass.

### Adapter legs — measured, with the non-answering one named

- `d4-typed-labels-check-gate.py --selftest` → exit 0, **163/163** (delegates the projector
  suite); its D4 projection run is byte-identical.
- `tools/gates/d4-assembly-check-gate.py --selftest` → **exit 2**: the adapter is flagless
  by design (its CLI is `[PACKET]` only), so `--selftest` is read as an input path. This is
  the known non-answering leg, unchanged since round-19 (`reports/round-19/regression.md`
  F-O13-2/N1); its conformance evidence is its committed baseline and its source-packet run
  (exit 0, byte-identical), both measured here. It is listed as its own labelled leg rather
  than dropped, so the report names the reading instead of hiding it.

## Before/after controls and preservation

- **Before (14:25:16) → after (14:37:34), compared by manifest rather than by matrix
  label** (the frozen legs are index-labelled, and the new round-25 generation shifted the
  indices). Every command present in both sweeps gave the same exit **except** the deltas
  accounted for above: the four cascaded successor manifests (round-18/repin-d2,
  round-20/repin-d2, round-22/d4-repin, round-23/repin-d2: 0 → 2, the declared re-pin) and
  the derived-packet entry (1 → 0, the fix). `round-11`, the original `round-18`,
  `round-3` and `round-3/attempt-1` read identically in both sweeps (2 / 1 / 2 / 2). The
  round-25 generation is new (absent → 0). No current command regressed.
- **The round-25 frozen generation was added between the sweeps** by the pin owners
  (`tools/gates/frozen/round-25/gate-input/`, six rows). The closing sweep measures it green
  6/6; the initial sweep could not, since it did not exist.
- Closing preservation: `clone_copied_paths_changed: []`; **1,350** locked historical paths
  with `locked_paths_changed: []`.
- Live-vs-snapshot drift is exactly one concurrent round-25 report fragment
  (`reports/round-25/scribe/fragment-ledger.md`), a file this seat never executes or reads.
- No filed round-8–24 artifact, old frozen manifest, shared LOG/SCORECARD/SKILL, or source
  tool was edited by this seat. No commit or push. This seat's only filed write is this
  report.

## Limits

- Regression reproduction is not round acceptance: this report proves the measured working
  tree at `HEAD=f74fc94…` behaves as recorded; it does not adjudicate the O/D/C claims (that
  is `python3 reports/round-25/run-validation.py`, run by the parent in an isolated clone).
  This seat executed no round validator.
- The closing matrix binds bytes that were still moving this round. The settle watcher held
  six quiet samples over the nine pin-relevant surfaces, and the drift instrumentation can
  see any under-matrix movement (it caught the one fragment write above), but a later write
  by another seat is not covered by this report. **This is not hypothetical:** the
  watcher's full 15-minute run finished at 14:40:58 with the digest still stable, and then
  `tools/gates/argot-derivation-gate.py` changed at **14:41:48** — after the watcher and
  after the closing sweep. That gate's three readings were re-measured live at 14:42:05 and
  are identical (18/18, D4 exit 0, fixture exit 1), so no count in this report changes; the
  event is recorded because it bounds the sweep's byte binding.
- The `d4-assembly-check-gate.py` exit 2 is a measurement of a design choice, not a defect
  claim; whether the lane wants that adapter executed rather than covered is a scope
  decision for the parent, already routed since round-19.
- The historical nonzero manifests and `tie-break --check` remain historical evidence;
  "all current commands green" is a statement about the live tree and the successor
  generations, not about rounds 3/11/18.

## Commands (all 2026-10-18, windows above)

- Sweeps: `export TMPDIR=$PWD/.scratch; python3 .scratch/r25-o16-o17-regression/sweep.py initial`
  and `… closing`; per-command stdout/stderr under
  `.scratch/r25-o16-o17-regression/<phase>/`.
- Settle watcher: `.scratch/r25-o16-o17-regression/watch.sh` (60 s, nine surfaces), log
  `.scratch/r25-o16-o17-regression/watch.log`.
- Hazard isolation (live lane, `TMPDIR=$PWD/.scratch`):
  `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` (0, 19/19)
  vs `… packet.d4.typed.yml` (initial 1, 14/16; closing 0, 16/16) vs flagless (0, 16/16);
  `python3 tools/gates/naming-collision-gate.py` on each packet (exit 1 each, **0**
  `DERIV-REPLAY` lines each).
- Argot gate: `python3 tools/gates/argot-derivation-gate.py --selftest` (0, 18/18);
  `… examples/culture-d4/packet.d4.yml` (0); `… tools/gates/fixtures/argot-derivation-gate.yml`
  (1, four `D4L-ARGOT-DERIV`).
- Digests: `sha256sum tools/gates/typed-pipeline-gate.py tools/gates/argot-derivation-gate.py
  tools/d2-typed-labels.py tools/check-gate-battery.py tools/assemble-d4-typed.py
  tools/gates/naming-collision-gate.py`; `git rev-parse HEAD`.
- Replays: the driver runs every `tools/gates/frozen/**/MANIFEST.tsv` with
  `tools/replay-frozen.py … --json`; the round-25 row is the one claimed green.

## Compliance self-attestation

This seat wrote only `reports/round-25/regression.md` and scratch under
`.scratch/r25-o16-o17-regression/`. No git mutation, no commit, no push, no filed-round byte
of rounds 8–24 touched, no tool under `tools/` edited, no historical validator executed. All
nonzeros are routed and named, not absorbed.

Two disclosures on scratch placement. (1) The sweep driver sets each command's `TMPDIR` to a
per-command directory inside the lane's `.scratch`, as the lane rule requires. (2) The
cascade control needed `tools/replay-frozen.py`, which **refuses an in-repo mirror root by
design** (`mirror_unsafe`, exit 2) — so that one control ran with `TMPDIR=/tmp/r25-cascade`,
outside the repo. Both temporary paths (`/tmp/r25-cascade`, `/tmp/prev-gate.py`) were removed
after use. Nothing was written outside the lane repo except those two, and nothing was
written outside the lane's `.scratch` in the live tree.
