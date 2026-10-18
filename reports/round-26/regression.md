# R26-O37..O38 — regression sweep (initial + closing)

**Operational regression verdict: GREEN for every current lane surface; NOT GREEN
for three pinned/round-26-own legs, each named and attributed below.** Battery,
craft, every runnable typed/assembly selftest and production check, the d2/d4
gates and adapters, handoff v2/v3, the projector suites, the harness selftests,
the round-26 instruments and the **`round-26/post-register`** frozen generation
all pass after the round-26 wave landed. The **23** nonzero matrix legs at close
break down as **seven historical/known-control labels** (the flagless
`d4-assembly-check-gate.py` under two labels, `tie-break --check`, and the
round-11 / round-18-original / round-3 / round-3-attempt-1 manifests), **one
deliberate negative fixture**, **four re-pin-cascade generations** (one of which
additionally carries the D4 input-move mismatches), **one un-committed round-25
pin generation**, and **ten round-26 legs** — every one named below, none
rewritten. This is a regression measurement, not round acceptance, canon
clearance, or a claim that historical manifests exit zero.

## Isolation, revision and evidence

- Observation date: **2026-10-18**. Times are **UTC−03:00**; each table row's
  time is that command's start, not a claimed completion time.
- Before scratch-writing commands: `export TMPDIR=$PWD/.scratch;
  export PYTHONDONTWRITEBYTECODE=1` from the lane root.
- Driver: `python3 .scratch/r26-o37-o38-regression/sweep.py <phase>`. Each phase
  creates a real Git clone under `.scratch/r26-o37-o38-regression/<phase>/repo`,
  overlays the measured live working-tree bytes plus manifest-referenced ignored
  receipts, and runs the whole matrix inside the clone with a per-command TMPDIR
  root. Every result row records argv, dated start/end, exit, and stream
  SHA-256. The isolation matters here because the battery is fail-closed on a
  live-tree edit and 64 workers were writing concurrently. **No round validator
  was executed by this seat**, in the live lane or otherwise; the round-26
  runner's own regression inventory is a different instrument and its verdict is
  the parent's.
- Binding: lane `HEAD = 1ad491a1a4b0aef9ebdc1861dfb8237727503825` (round-26
  declare commit); declared baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`
  (`reports/round-26/claims.json:5`). Both sweeps measure the **uncommitted
  integration overlay** at that HEAD, not an assertion that HEAD contains it.
- Raw evidence: `.scratch/r26-o37-o38-regression/{initial,closing}/{snapshot,source-manifest,results}.json`
  and per-command `*.stdout.txt` / `*.stderr.txt`. The filed evidence is this
  report alone; no shared bookkeeping or source file is this seat's write.

## Initial sweep (R26-O37) — pre-wave binding

- `python3 .scratch/r26-o37-o38-regression/sweep.py initial`, clone/snapshot
  started **15:01:28**, matrix completed **15:02:28**. Snapshot: **2,063**
  inputs, copied-manifest SHA-256 `ecebe2bfbdec37f7…`, `source_drift_after_copy: []`.
- Matrix: **63** commands, **50** exit-zero. All assigned current surfaces green;
  the 13 nonzeros were the pre-existing controls plus the round-25 pin tail
  (listed below). The round-26 artifacts did not exist yet, so this sweep is the
  honest before-picture.
- Preservation: `clone_copied_paths_changed: []`, `source_changes_since_snapshot: []`,
  **1,431** locked historical paths (rounds 8–25 reports + all frozen generations
  outside `round-26/`) with `locked_paths_changed: []`.

## Closing sweep (R26-O38) — post-wave

- Settle: a 60 s watcher
  (`.scratch/r26-o37-o38-regression/watch.sh`, log `watch.log`) hashed the
  pin-relevant surfaces every minute from 15:04. The digest changed at every
  sample until **15:44:12**, then held byte-identical for **five** consecutive
  samples (15:44:12 → 15:48:50, digest `949a4d2c5a066567…`, log `settle.log`).
  The closing sweep began at **15:49:05**.
- `python3 .scratch/r26-o37-o38-regression/sweep.py closing`, clone/snapshot
  started **15:49:05**, matrix completed **15:49:55**. Snapshot: **2,188**
  inputs, copied-manifest SHA-256 `5202f7a158c83f1b…`, `source_drift_after_copy: []`.
  `clone_copied_paths_changed: []`.
- Matrix: **80** commands, **57** exit-zero. The count grew from 63 because the
  round-26 instruments, the `--quiet` handoff legs, the three successor-baseline
  legs and a second round-26 frozen generation landed between the sweeps.

### Current commands — all exit 0 (15:49:0x–15:49:5x)

| Group | Measured result (command + date: driver above, 2026-10-18) |
|---|---|
| Battery | 7/7 structural selftests, fail 0 / unevaluable 0, **19/19** baselines pinned, coverage **9/9**, `preserved: true`; `--selftest` **35/35** |
| Craft | **10/10** tamper + **18/18** CLI selftests; full check `audits=7, mech_cases=11, derivations=9, approx_checks_runner=37` |
| Assembly | d2 **42/42**, d2-typed **11/11**, d3 **85/85**, d4 **81/81**, d4-typed **12/12** selftests; all five production `--check` outputs byte-identical |
| Projector | `d2-typed-labels.py --selftest` **163/163** (the D4 label gate delegates the same suite); D2 and D4 projections byte-identical |
| Typed gate | `--selftest` **19/19**, `--selftest-generalized` **16/16**; D2 default **16/16**; D4 source **20/20**; D4 derived **17/17** (the round-25 `L3b-argot` leg is present in both) |
| d2/d4 gates | D4 label gate `--selftest` **163/163**, projection byte-identical; D4 assembly gate on the source packet byte-identical |
| Argot gate | `--selftest` **21/21**; D4 run exit 0 (`records=170 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0`) |
| Handoff | v2 exit 0, claims 15, links **50/50**, named drift only; v2 `--selftest` exit 0; v3 `--selftest` exit 0 (39 controls); v3 successor baseline green (below) |
| Harness | coupling selftest + D3 packet zero findings; packet_links / packet_uncertainty / receipt_guard selftests exit 0; replay-frozen selftest **79/79** |
| Round-26 instruments | openq `--json` 78/78 rows, 0 undispositioned, all six checks ok; openq `--selftest` exit 0; gate-tests `--check` **62/62**; gate-tests `--selftest` exit 0; r4-twin/pin-repoint selftests exit 0 |
| Selector control | `tie-break.py --root . --check` exit 1 (documented round-20 class, below) |

## Round-26 findings — three legs, each attributed

### F1. The `round-26/gate-input` pin generation was pinned before its own subject

`tools/gates/frozen/round-26/gate-input/freeze-receipt.json` records
`frozen_at: 2026-10-18T18:08:08Z` (15:08:08 local). The D register stratum landed
after it: `examples/culture-d4/packet.d4.yml` and `typed-labels.d4.yml` were
written at **15:30:03**, `expected-holds.json` and `04-lexicon.yml` at
**15:27:13**. The generation therefore pins the pre-register D4 inputs while
`pins` names the committed gate `b749ad07…`.

Replay at the closing stamp (`python3 tools/replay-frozen.py
tools/gates/frozen/round-26/gate-input/MANIFEST.tsv --json`, 15:49:2x):
**4/6 reproduced, 2 mismatch** — both D4 rows observe exit 2 where exit 0 and 12
findings were recorded (`examples/culture-d4/packet.d4.yml`,
`examples/culture-d4/packet.d4.typed.yml`). The two D2 rows and both fail-closed
controls reproduce exactly.

**Control, executed.** In a throwaway clone of the declaration HEAD, the frozen
`round-26/gate-input` generation was copied in and `git checkout --
examples/culture-d4` restored the pre-register D4 artifacts
(`typed-labels.d4.yml` back to `60b526b0b3d0…`, `packet.d4.yml` to
`e7ecd2045ef0…`). The same replay then returned **6/6 reproduced, 0 mismatch,
exit 0**. So the two mismatches are attributable to the D4 input move and nothing
else. The clone was not written back; no historical manifest or lane byte was
edited.

### F2. `round-26/post-register` is the generation that closes the tail — and it replays green

A **second** round-26 generation exists, `tools/gates/frozen/round-26/post-register/`
(`freeze-receipt.json`, `frozen_at 2026-10-18T18:22:07Z`), whose `input_pins`
carry the post-register D4 digests (`packet.d4.yml dd25077bc016…`,
`packet.d4.typed.yml 618a78c90fc0…`) and whose `supersedes` block names the
round-25 generation by its un-committed pin. Replay at the closing stamp:
**6/6 reproduced, 0 mismatch, exit 0.**

It landed at **15:22:07**, i.e. **between** my initial (15:00) and closing
(15:49) sweeps, so the initial matrix could not measure it. This is why the
closing matrix's frozen legs are **index-labelled**, not identity-labelled: the
new generation inserted at position 08 and renumbered the tail (`round-26/gate-input`
→ `frozen-07`, `round-3` → `frozen-09`, `round-3/attempt-1` → `frozen-10`).
Before/after comparison below is therefore **by manifest path**, not by label.

### F3. The v3 packet-baseline tail: one stale row, one live-correct row, and the runner points at the stale one

`python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` (the exact entry in
`reports/round-26/run-validation.py:204`) exits **1**:
`E2E-DIGEST: 6 read-set file(s) changed since the baseline was frozen` — naming
`01-brief.yml`, `04-lexicon.yml`, `expected-holds.json`, `packet.d4.typed.yml`,
`packet.d4.yml`, `typed-labels.d4.yml`, i.e. exactly the register stratum's D4
read set. The default baseline is the round-20 packet-baseline pin, which is
stale **because** the D register stratum landed — the coupling claim O itself
names.

Two competing successor rows exist, and they are not equivalent:

| row | packet pin | v3 run with `--baseline <row>` |
|---|---|---|
| `reports/round-26/register/v3-baseline-r26/expected.json` | `69ce3877…` | **exit 0**, `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 v2_subset=equal alias_leg=landed` |
| `reports/round-26/remainders/v3-baseline-r26/expected.json` | `a97a0f0a…` | **exit 1** (same `E2E-DIGEST`) |

`reports/round-26/remainders/pin-repoint-check.py --check` (exit 1) says the same
thing in its own vocabulary: its control `new-v3-row-replays-green` is the single
**FAIL**, while `control-stale-v3-row-replays-red` passes. Its `live_pin` field is
`a97a0f0a…` and its `new_row` is `reports/round-26/remainders/v3-baseline-r26/expected.json`
— the stale row. The v2 half of the same checker is fully green
(`new-v2-row-replays-green`, both red/green controls, `filed-rounds-8-25-unchanged`).

**Consequence for the parent:** the O claim's own remainder is *not* wired into
its counting command. The runner runs `handoff-v3 --quiet` against the stale
default and the re-point row it grades replays red, so the round-26 validator
reports O red. The lane's underlying artifact is fine — the register
`v3-baseline-r26` row replays green at 16/16 and its twin/links/uncertainty
harnesses exit 0.

### F4. `tie-break-selftest` regressed 23/23 → 21/23 — the same root cause, one hop out

`python3 reports/round-22/fixes/tie-break.py --root . --selftest` was **23/23** in
the initial sweep and is **21/23** at close. The two failing controls are
`real-v3-reversed-mtime-0` and `real-v3-reversed-mtime-1`, both of which shell out
to `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` and assert the
summary is byte-identical. They now fail with the same `E2E-DIGEST` exit 1 as F3.
This is a **second instrument** reaching F3's stale default baseline — independent
corroboration that the reading is the baseline pin and not a defect in either
instrument. `tie-break.py --check` remains exit 1 for its own documented round-20
reasons (`PLACEHOLDER_RE` false positive plus the stale round-20 v2 digest row),
with `filed_rounds_8_21_changes: []`.

### F5. Round-26's own lessons instruments read red on the live partition

Two round-26 audit instruments are nonzero at close, both for the same benign
reason — a 27th lessons file (`corpus/lessons/round-26.md`, written 15:29:15)
landed after their pinned stamp:

- `reports/round-26/audit/x63-lessons-audit.py` exit 1: `live partition is 26 md
  files` observed **27**; checks A and F red on live bytes; findings
  `prose-arithmetic-drift` (stated rows 26/49 vs measured files 27) and
  `X63-G1 stale-reading`. Its `--selftest` is **17/20** with the same three
  names failing.
- `reports/round-26/lessons/c51-revision-audit.py` exit 1: `C52-2` finding — the
  `round-26.md` pin cell claims `bytes 46745 / lines 190 / sha8 cf7461fe` while
  live bytes are `60054 / 222 / cae06660`. All seven other checks PASS. Its
  `--selftest` is **13/15**, the two failures being the arithmetic check firing on
  drifted prose and the counting-command check.

These are **stale-pin readings, not defects in the lesson content** — the same
shape round 25 filed for `round-25.md` (C35-3). They are the C claim's own
artifacts going stale on the file the C claim itself added, and the parent owns
whether the index revision is re-pinned before admission.

## Nonzero legs at close — each named, none rewritten

### New round-26 frozen generation — replayed green

`round-26/post-register` (6/6, exit 0) is the successor reading. `round-26/gate-input`
is superseded and reads 4/6 (F1); its bytes are untouched.

### The declared pin cascade — four successor generations, one refused row each

| generation | initial | closing | refused row |
|---|---|---|---|
| `round-18/repin-d2` | 2 (10/11) | **2** (10/11) | 1 row, `gate_digest_mismatch` on typed-pipeline-gate; other 10 reproduce |
| `round-20/repin-d2` | 2 (10/11) | **2** (10/11) | same shape, 10 reproduce |
| `round-22/d4-repin` | 2 (2/3) | **2** (0/3) | 1 `gate_digest_mismatch` **plus 2 D4 `replay_mismatch`** (the register input move, F1's mechanism) |
| `round-23/repin-d2` | 2 (10/11) | **2** (10/11) | same shape, 10 reproduce |
| `round-25/gate-input` | 2 (0/6) | **2** (0/6) | **all 6** `gate_digest_mismatch` — the round-25 pin names a gate blob that is not on disk |

The `round-22/d4-repin` and `round-18` rows each gained **D4 input-move**
mismatches between the sweeps (round-18 original: 1 → 2; round-22: 0 → 2). Those
are F1's mechanism reaching the older generations, and the control in F1 covers
them: with the pre-register D4 artifacts restored, `round-18` returns to 1
mismatch and `round-22/d4-repin` to 2/3 reproduced — i.e. their original readings.
No historical manifest was edited.

### The round-25 pin names a gate revision that never existed

Independent of the input move: `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv`
pins `tools/gates/typed-pipeline-gate.py` at `879d40bf…`, and
`git cat-file -t 879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126`
reports **"Not a valid object name"**. The only gate blobs ever committed are
`d102fd1d…` (round-11), `04ad4bb4…` (round-18), `b749ad07…` (round-25 admit). So
the round-25 freeze pinned an uncommitted working-tree revision, and all six of
its rows refuse before a gate runs. `round-26/post-register` supersedes it by
name and pins the committed blob.

**Pinned-output control.** The round-25 generation's recorded outputs are also
stale by exactly the `L3b-argot` leg: re-run in a mirror-like cwd against the
committed gate, `d4-source.out` differs by exactly the added `ok   L3b-argot` line
and `19/19 → 20/20`, and `d4-typed.out` by the same line and `16/16 → 17/17`,
while `d2-source.out`, `d2-typed.out` and both controls are **byte-identical**.

### The argot gate's own negative fixture — a deliberate exit 1

`python3 tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml`
(15:49:2x) → **exit 1** with four `D4L-ARGOT-DERIV` and one `D4L-ARGOT-RULE`
(`records=14 register_scoped=11 derived_pairs=8 borrow_pairs=3 violations=4 rule_holds=1`).
This leg is in the matrix precisely because it *must* be nonzero: it is the
discriminator proving the gate reports findings when a derivation does not
replay. Counted as a control, not a failure.

### Historical negative controls — explicitly nonzero, never rewritten

- `round-11` exit 2 (10/11): the typed row is `gate_digest_mismatch` against the
  pre-generalization pin `d102fd1d…` — documented since round-18.
- `round-18` (the original, not repin-d2) exit 1: `replay_mismatch` on the
  superseded D4 projection row.
- `round-3` and `round-3/attempt-1` exit 2 (0/7 each): obsolete gate pins.
- `tie-break.py --root . --check` exit 1 (15:49:1x): the documented round-20
  `PLACEHOLDER_RE` false positive plus the stale round-20 v2 digest row, with
  `filed_rounds_8_21_changes: []`. The filed round-20 validator is not claimed to
  pass.

### Adapter legs — measured, with the non-answering one named

- `d4-typed-labels-check-gate.py --selftest` → exit 0, **163/163**; its D4
  projection run is byte-identical.
- `tools/gates/d4-assembly-check-gate.py --selftest` → **exit 2**: the adapter is
  flagless by design (its CLI is `[PACKET]` only), so `--selftest` is read as an
  input path. This is the known non-answering leg, unchanged since round-19
  (`reports/round-19/regression.md` F-O13-2/N1); its conformance evidence is its
  committed baseline and its source-packet run (exit 0, byte-identical), both
  measured here. It is listed as its own labelled leg rather than dropped, so the
  report names the reading instead of hiding it.

## Before/after controls and preservation

- **Before (15:01) → after (15:49), compared by argv rather than by matrix label**
  (the frozen legs are index-labelled and the `post-register` generation inserted
  at position 08). Of **49** commands present in both sweeps, **exactly two
  changed exit**: `tie-break.py --root . --selftest` (0 → 1, F4) and
  `tools/exercise-handoff-e2e.py --profile v3` (0 → 1, F3). Both are the stale
  v3 baseline. **15** legs are new in the closing matrix (the round-26 instruments
  and the `--quiet`/successor-baseline handoff legs); every other common command
  read identically.
- **The only regression among legs present in both sweeps is `tie-break-selftest`
  (23/23 → 21/23)**, fully attributed to F3/F4. `handoff-v3`'s 0 → 1 is the O red
  itself (F3), not a second defect. No current lane surface regressed.
- **Frozen legs, by manifest path:** `round-11`, `round-18/repin-d2`,
  `round-20/repin-d2` and `round-23/repin-d2` read the same summary in both sweeps
  (exit 2, 10/11 reproduced); `round-22/d4-repin` went 2/3 → 0/3 reproduced and the
  original `round-18` 1 → 2 mismatch, both the D4 input-move mechanism covered by
  F1's control; `round-25/gate-input` read 0/6 in both; `round-3` and
  `round-3/attempt-1` read 0/7 in both; `round-26/gate-input` (new, 4/6) and
  `round-26/post-register` (new, 6/6) are the round-26 generations.
- Closing preservation: `clone_copied_paths_changed: []`; **1,431** locked
  historical paths with `locked_paths_changed: []`. The lock set was extended
  from round-25's driver to cover `reports/round-8..25` **and every frozen
  generation outside `round-26/`**, so the new round-26 pins are the live subject
  and nothing older is.
- Live-vs-snapshot drift is exactly zero in both phases (`source_drift_after_copy: []`,
  `source_changes_since_snapshot: []`) — a stronger reading than round 25's, which
  caught one concurrent fragment write.

## Limits

- Regression reproduction is not round acceptance: this report proves the measured
  working tree at `HEAD=1ad491a…` behaves as recorded; it does not adjudicate the
  O/D/C claims (that is `python3 reports/round-26/run-validation.py`, run by the
  parent in an isolated clone). This seat executed no round validator.
- The closing matrix binds bytes that were still moving this round. The settle
  watcher held five quiet samples over the pin-relevant surfaces, and re-checking
  the same digest after the sweep and after this report was written returned
  `949a4d2c5a066567…` — identical to the settle digest, once this seat's own
  `reports/round-26/regression.md` is excluded from the set. So the closing matrix
  measured the settled tree and no other seat wrote during or after it; a later
  write is still not covered by this report.
- F1–F5 are **measurements with controls**, not defect claims about any seat's
  work. F3 in particular measures a wiring choice (which successor row the pin
  checker points at) that the parent owns.
- The historical nonzero manifests and `tie-break --check` remain historical
  evidence; "all current commands green" is a statement about the live tree and
  the successor generations, not about rounds 3/11/18.

## Commands (all 2026-10-18, windows above)

- Sweeps: `export TMPDIR=$PWD/.scratch; python3 .scratch/r26-o37-o38-regression/sweep.py initial`
  and `… closing`; per-command stdout/stderr under
  `.scratch/r26-o37-o38-regression/<phase>/`.
- Settle watcher: `.scratch/r26-o37-o38-regression/watch.sh` (60 s), log
  `watch.log`; settle log `settle.log`.
- Frozen replays: `python3 tools/replay-frozen.py tools/gates/frozen/<gen>/MANIFEST.tsv --json`
  with `TMPDIR` outside the repo (the tool refuses an in-repo mirror root by design).
- F1 control: throwaway clone at `1ad491a`, frozen `round-26/gate-input` copied in,
  `git checkout -- examples/culture-d4`, then the same replay.
- F3 legs: `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` (1) and
  `… --baseline reports/round-26/register/v3-baseline-r26/expected.json` (0) and
  `… --baseline reports/round-26/remainders/v3-baseline-r26/expected.json` (1);
  `python3 reports/round-26/remainders/pin-repoint-check.py --check` (1).
- F4: `python3 reports/round-22/fixes/tie-break.py --root . --selftest` (1, 21/23).
- F5: `python3 reports/round-26/audit/x63-lessons-audit.py` (1) and
  `python3 reports/round-26/lessons/c51-revision-audit.py` (1).
- Digests: `sha256sum tools/gates/typed-pipeline-gate.py tools/gates/argot-derivation-gate.py
  tools/d2-typed-labels.py tools/assemble-d4-typed.py`; `git rev-parse HEAD`;
  `git cat-file -t 879d40bf…`.
- Replays: the driver runs every `tools/gates/frozen/**/MANIFEST.tsv` with
  `tools/replay-frozen.py … --json`.

## Compliance self-attestation

This seat wrote only `reports/round-26/regression.md` and scratch under
`.scratch/r26-o37-o38-regression/`. No git mutation, no commit, no push, no filed
round-8–25 byte touched, no tool under `tools/` or `examples/` edited, no
historical validator executed. All nonzeros are routed and named, not absorbed.

Two disclosures on scratch placement. (1) The sweep driver sets each command's
`TMPDIR` to a per-command directory inside the lane's `.scratch`, as the lane rule
requires. (2) `tools/replay-frozen.py` refuses an in-repo mirror root by design
(`mirror_unsafe`, exit 2), so the standalone replay and control invocations ran
with `TMPDIR` outside the repo (`/tmp/r26-o37-replay`, `/tmp/r26-ctrlhead`,
`/tmp/r26-ctrlhead2`). Every temporary path was removed after use. Nothing was
written outside the lane repo except those, and nothing was written outside the
lane's `.scratch` in the live tree.
