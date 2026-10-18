# R27-O33..O36 — regression sweep (initial + closing)

**Operational regression verdict: GREEN for every current lane surface, and GREEN
for all four assigned legs** — battery 9/9, the d2/d4 gates, handoff v2/v3, and
the projector/adapter/craft selftests. **NOT GREEN for three pinned round-26-own
legs**, each named and attributed below: the round-26 `post-register` and
`gate-input` frozen generations, the round-26 pin-repoint checker, and the
round-26 gate-tests battery. Every one is the **same single mechanism** — the
round-27 register-law amendment moved the D4 packet — and each is closed by a
round-27 successor row that replays green. No filed round-8..26 byte was edited,
no historical manifest repaired in place.

This seat wrote only `reports/round-27/regression.md` and scratch under
`.scratch/r27-o33-o36-regression/`. No git mutation, no commit, no push, no
`tools/` or `examples/` byte edited, no round validator executed by this seat.

## Isolation, revision and evidence

- Observation date: **2026-10-18**. Times are **UTC−03:00**; each row's time is
  that command's start, not a claimed completion time.
- Before scratch-writing commands: `export TMPDIR=$PWD/.scratch;
  export PYTHONDONTWRITEBYTECODE=1` from the lane root.
- Driver: `python3 .scratch/r27-o33-o36-regression/sweep.py <phase>`. Each phase
  clones the lane (`git clone --shared --no-hardlinks`), overlays the measured
  live working-tree bytes **plus every manifest-referenced and ignored receipt**,
  and runs the whole matrix inside the clone with a per-command `TMPDIR` root.
  Every result row records argv, dated start/end, exit, and stream SHA-256. The
  isolation matters because the battery is fail-closed on a live-tree edit and
  64 workers were writing concurrently.
- Binding: lane `HEAD = b95fca1e40f32f7346937ab6426f9ccca60e319f` (round-27
  declare commit); declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`
  (`reports/round-27/claims.json`). Both sweeps measure the **uncommitted
  integration overlay** at that HEAD, not an assertion that HEAD contains it.
- Raw evidence: `.scratch/r27-o33-o36-regression/{initial,closing}/{snapshot,source-manifest,results}.json`
  and per-command `*.stdout.txt` / `*.stderr.txt`.

### A driver defect this seat found and fixed (F0) — named before any result

The first initial run (`.scratch/r27-o33-o36-regression/initial-unoverlaid/`)
copied only Git-tracked bytes plus manifest-named receipts. `.gitignore` line 3
is `*.log`, so **every `run.log` / `tamper-control.log` is untracked** and the
clone silently lacked it. The round-26 pin checker's control
`v3-row-carries-the-full-five-file-set` reads
`reports/round-26/remainders/v3-baseline-r26/run.log`, and in that clone it read
**16/17 while the live tree read 17/17** — a measurement artifact, not a lane
defect. The driver was extended to overlay every ignored receipt outside
`.scratch`/`.ufo`/`__pycache__` and outside the bulk
`reports/supplement-opencode-1/scratch/` tree (31 such receipt files), and the
initial phase was re-run. The corrected initial sweep reads the same checker
**17/17**. Round 26's driver carried manifest-referenced ignored receipts but not
this class; the gap is fixed here and the flawed run is preserved, not deleted.

## Initial sweep (R27-O33..O36, pre-wave) — the honest before-picture

- `python3 .scratch/r27-o33-o36-regression/sweep.py initial`, clone/snapshot
  started **16:15:42**, matrix completed **16:16:35**. Snapshot: **2,234**
  inputs, `source_drift_after_copy: []`.
- Matrix: **76** commands, **60** exit-zero. The round-27 artifacts did not exist
  yet (only `claims.json`, `targets.json`, `scribe/x56-census.py`), so the D4
  packet was still the round-26 register packet and the register law was absent.
- Preservation: `clone_copied_paths_changed: []`, **1,587** locked historical
  paths (rounds 8–26 reports + every frozen generation outside `round-27/`) with
  `locked_paths_changed: []`.

## Settle, then the closing sweep (R27-O33..O36, post-wave)

- Settle: a 60 s watcher (`.scratch/r27-o33-o36-regression/settle.sh`) hashed the
  pin-relevant surfaces (`tools`, `examples`, `corpus`, `reports/round-27`,
  `SCORECARD.md`, `SKILL.md`, `LOG.md`). The digest changed at every sample until
  **16:54:30**, then held byte-identical for **three** consecutive samples
  (16:54:30 → 16:57:30, digest `f8e247b8379106f2…`). The first watcher window
  timed out at 25 min with the wave still writing; it was restarted, and it is
  the restart that settled. The closing sweep began after settle.
- `python3 .scratch/r27-o33-o36-regression/sweep.py closing`, clone/snapshot
  started **17:02:58**, matrix completed **17:03:54**. Snapshot: **2,356**
  inputs, `source_drift_after_copy: []`, `clone_copied_paths_changed: []`.
- Matrix: **78** commands, **59** exit-zero. The count grew from 76 because the
  round-27 frozen manifest (`reports/round-27/pinsweep/frozen/r27-post/`) and the
  round-27 v3 successor-baseline leg landed between the sweeps.

### Assigned legs (O33..O36) — all exit 0, post-sweep

| Assigned leg | Measured result (command + date: driver above, 2026-10-18) |
|---|---|
| **O33 battery 9/9** | `tools/check-gate-battery.py` exit 0: `pass 7 / fail 0 / unevaluable 0`, coverage **9/9**, **19/19** baselines pinned, `gates_uncovered: []`, `preserved: true`; `--selftest` **35/35** |
| **O34 d2/d4 gates** | d2 typed-pipeline **16/16**; d4 typed-pipeline **20/20**; d4 label gate byte-identical projection and `--selftest` **163/163**; d4 assembly gate byte-identical; d2/d3/d4 assemblers + both typed adapters all `--check` byte-identical; `--selftest` 42/42, 11/11, 85/85, 81/81, 12/12 |
| **O35 handoff v2/v3** | v2 exit 0 (`claims=15 links=50/50 drift=named`); v3 exit 0 (`fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed`); both `--selftest` exit 0; v3 successor baseline (`reports/round-27/pinsweep/v3-baseline-r27/expected.json`) **exit 0** |
| **O36 projector/adapter/craft** | projector `--selftest` **163/163**, D2 and D4 projections byte-identical; typed-pipeline `--selftest` **19/19**, `--selftest-generalized` **16/16**; craft `--selftest` 10/10 tamper + 18/18 CLI, full check `audits=7, mech_cases=11, derivations=9, approx_checks_runner=37` |

Also green post-sweep: `argot-gate-d4` exit 0 (`records=175 register_scoped=14
derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0`),
`argot-gate-selftest` **27/27**, `frozen-selftest` **79/79**, the harness
selftests, and every round-27 instrument this seat ran:
`reports/round-27/gate-tests/run-gate-tests.py --check` exit 0, its `--selftest`
exit 0; `reports/round-27/readme/sweep.py` exit 0 (`rows 200 files 200`,
`missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `totals_ok True`);
`reports/round-27/audit/x63-entry-source-resolvability.py <entry>` exit 0
(`locators=41 unresolved=0 findings=0`); `reports/round-27/audit/x64-cold-rerun.py`
exit 0; `reports/round-27/pinsweep/frozen/r27-post` replay **2/2 reproduced**.

## The three round-27 findings — one mechanism, each closed by a round-27 successor

### F1. The D4 register-law amendment moved the packet, so every pre-law D4 pin is stale

The round-27 D claim landed `examples/culture-d4/components/13-register-law.yml`
and amended the D4 packet at **16:31:37**. Live digests now read
`packet.d4.yml 86079a67…`, `packet.d4.typed.yml 1c4b8808…`; the round-26
generations pin `dd25077b…` / `618a78c9…` (`post-register`) and `e7ecd204…` /
`ffece0fe…` (`gate-input`).

**Finding, measured.** Two frozen generations moved between the sweeps:

| generation | initial | closing | rows |
|---|---|---|---|
| `tools/gates/frozen/round-26/post-register` (label `frozen-08`) | 0 (6/6) | **1** (4/6) | 2 D4 `replay_mismatch`: `exit 2 != recorded 0`, `finding count 0 != recorded 12` |
| `tools/gates/frozen/round-26/gate-input` (label `frozen-07`) | 1 (4/6) | **1** (4/6) | same two rows (already red in the initial sweep) |

Both mismatching rows are the D4 packet pair; both D2 rows and both fail-closed
controls reproduce exactly in every run.

**Control, executed.** In a throwaway clone checked out at the **declared
baseline** `4f09c99` (pre-amendment), the same replay returned **6/6 reproduced,
0 mismatch, exit 0**. So the two mismatches are attributable to the D4 input move
and nothing else. Direct mechanism check in the closing clone: the gate on the
round-26 snapshot packet reports `FAIL L1-assembler: packet bytes dd25077bc016
are not tools/assemble-culture-d4.py's deterministic assembly (86079a6708a0)` —
the frozen packet is no longer the current component set's assembly. The clone
was removed after use; no historical manifest or lane byte was edited.

### F2. The round-26 pin-repoint checker's own successor row went stale

`python3 reports/round-26/remainders/pin-repoint-check.py --check`: **17/17 in
the initial sweep (0)**, **16/17 at close (exit 1)**. The single failing control
is `new-v3-row-replays-green`:

```
FAIL new-v3-row-replays-green
  FAIL input-digest: examples/culture-d4/components/01-brief.yml: frozen feca7bda25be… live 649aa111db2e…
  FAIL input-digest: examples/culture-d4/expected-holds.json: frozen d6136488e22f… live 857417e949…
```

The round-26 r5 row (`reports/round-26/handoff/declared-in-r5/expected.json`)
pinned the post-register read set; the round-27 amendment moved two more files of
that read set. Its **red controls still pass** (`control-stale-v3-row-replays-red`,
`v3-stale-row-pins-the-old-packet`, `filed-rounds-8-25-unchanged` with
`changed: []`), so the checker is discriminating correctly — it is grading a row
that is now superseded, not a defect in the checker.

**Successor, measured.** `reports/round-27/pinsweep/v3-baseline-r27/` is the
round-27 re-pin (five-file set, `packet_sha256 6ea03…`) and replays **exit 0**.
Measured in the same matrix: the round-26 r5 row and both round-26 v3 rows read
exit 1; the round-27 row reads exit 0.

### F3. The round-26 gate-tests battery's D20 leg reads the same stale generation

`reports/round-26/gate-tests/run-gate-tests.py --check`: **62/62 (0) initial**,
**61/62 (exit 1)** at close. The single FAIL is
`D20 tools/gates/frozen/round-26/post-register/MANIFEST.tsv (newest round-26)
replays clean` — the same generation as F1, reached by a second independent
instrument. Every teeth control and every D17/D19 leg still passes. Round 27's
own `reports/round-27/gate-tests/run-gate-tests.py --check` is **exit 0**.

### F1–F3 as one reading

All three are **one mechanism**: a D4 input move invalidates every pin taken
before it. Each is closed by a round-27 successor that replays green:
`pinsweep/frozen/r27-post` (2/2), `pinsweep/baselines/*/r27-post` (both pinned),
`pinsweep/v3-baseline-r27` (exit 0). The round-27 freeze receipts name the
supersession explicitly, and the round-27 pin-sweep's own O38 adjudication
(`reports/round-27/pinsweep/o38-sweep-inventory-adjudication.md`) independently
reproduces the same family-G reach defect. **This seat did not repair any
historical row**, and the round-26 legs' red readings are reported, not absorbed.

## Nonzero legs at close — each named, none rewritten

### Round-27 successors — replayed green

`reports/round-27/pinsweep/frozen/r27-post` **2/2, exit 0**;
`reports/round-27/pinsweep/v3-baseline-r27` **exit 0**; the two
`pinsweep/baselines/*/r27-post` rows pinned (19/19 battery coverage holds).

### The declared pin cascade — the same four successor generations as round 26

| generation | initial | closing | reading |
|---|---|---|---|
| `round-18/repin-d2` | 2 (10/11) | **2** (10/11) | 1 `gate_digest_mismatch`; 10 reproduce |
| `round-20/repin-d2` | 2 (10/11) | **2** (10/11) | same shape |
| `round-22/d4-repin` | 2 (0/3) | **2** (0/3) | 1 `gate_digest_mismatch` + 2 D4 `replay_mismatch` (F1's mechanism) |
| `round-23/repin-d2` | 2 (10/11) | **2** (10/11) | same shape |
| `round-25/gate-input` | 2 (0/6) | **2** (0/6) | **all 6** `gate_digest_mismatch` — the round-25 pin names a gate blob that is not on disk |
| `round-26/gate-input` | 1 (4/6) | **1** (4/6) | F1's two D4 rows |
| `round-26/post-register` | 0 (6/6) | **1** (4/6) | F1 |

`round-18` (original) and `round-22/d4-repin` read 0-reproduced in both sweeps
for the same D4 input-move reason; `round-11`, `round-3`, `round-3/attempt-1`
read identically in both (historical gate pins, documented since round 18).

### Historical negative controls — explicitly nonzero, never rewritten

- `round-11` exit 2 (10/11): the typed row is `gate_digest_mismatch` against the
  pre-generalization pin `d102fd1d…` — documented since round 18.
- `round-18` (original) exit 1: `replay_mismatch` on the superseded D4 projection row.
- `round-3` and `round-3/attempt-1` exit 2 (0/7 each): obsolete gate pins.
- `argot-gate-fixture` exit 1 with four `D4L-ARGOT-DERIV` and one `D4L-ARGOT-RULE`
  (`records=14 register_scoped=11 derived_pairs=8 borrow_pairs=3 violations=4
  rule_holds=1`): the gate's own negative fixture, in the matrix **because it must
  be nonzero** — it is the discriminator proving the gate reports findings when a
  derivation does not replay. Counted as a control, not a failure.
- `tie-break.py --root . --check` exit 1: the documented round-20 `PLACEHOLDER_RE`
  false positive plus the stale round-20 v2 digest row, with
  `filed_rounds_8_21_changes: []`. Its `--selftest` is **23/23 in both sweeps**
  (exit 0 both) — round 26 closed at 21/23 on the stale v3 default baseline, and
  at the round-27 declare HEAD that baseline is already live-correct, so the two
  `real-v3-reversed-mtime` controls pass here without this round doing anything.
  It is a pre-existing reading, not a round-27 recovery; the recovery belongs to
  the round-26 admit, and this sweep simply does not reproduce round 26's closing
  number.

### Adapter legs — measured, with the non-answering one named

`tools/gates/d4-assembly-check-gate.py --selftest` → **exit 2**: the adapter is
flagless by design (its CLI is `[PACKET]` only), so `--selftest` is read as an
input path. This is the known non-answering leg, unchanged since round 19
(`reports/round-19/regression.md` F-O13-2/N1); it appears under two labels
(`d4-assembly-gate-selftest` and the discovered `gate-selftest-d4-assembly-check-gate`)
and is listed as its own labelled leg rather than dropped. Its conformance
evidence is its committed baseline and its source-packet run (exit 0,
byte-identical), both measured here.

## Before/after controls and preservation

- **Before (16:15) → after (17:02), compared by argv rather than by matrix label.**
  Of the common commands, **exactly three changed exit**:
  `frozen-08` (`round-26/post-register`, 0 → 1, F1), `r26-pin-repoint` (0 → 1,
  F2), and `r26-gate-tests` (0 → 1, F3). `frozen-07` was already 1 in both.
  Every other common command read identically; the only additions are the
  round-27 frozen manifest and the round-27 v3 baseline leg.
- **No recovery and no regression:** `tie-break-selftest` reads **23/23 in both**
  sweeps (round 26 closed at 21/23 on the stale v3 default; at this HEAD that
  baseline is already live-correct, so this round did not move it either way).
  One leg **grew**: `argot-gate-selftest` 21/21 → **27/27**, the round-27 law
  landing adding six controls — a bigger control set at the same exit 0, not a
  behaviour change.
- **No current lane surface regressed.** All four assigned legs, the battery
  coverage, the d2/d4 gates, both handoffs, the projector, and every adapter and
  craft selftest read green in **both** sweeps.
- Frozen legs, by manifest path, read identically in both sweeps except F1's two
  round-26 generations; the round-27 generation is new in the closing matrix.
- Preservation: `clone_copied_paths_changed: []`; **1,587** locked historical
  paths with `locked_paths_changed: []`. Live-vs-snapshot drift is exactly zero
  in both phases (`source_drift_after_copy: []`, `source_changes_since_snapshot: []`).

## Limits

- Regression reproduction is not round acceptance: this report proves the measured
  working tree at `HEAD=b95fca1` behaves as recorded; it does not adjudicate the
  D/O/C claims (that is `python3 reports/round-27/run-validation.py`, run by the
  parent in an isolated clone). This seat executed no round validator; the
  parent's own `reports/round-27/validation.json` reads acceptance true, and this
  report neither confirms nor inherits that reading.
- The closing matrix binds bytes that were still moving this round. The settle
  watcher held three quiet samples over the pin-relevant surfaces; a later write
  is still not covered by this report.
- F1–F3 are **measurements with controls**, not defect claims about any seat's
  work. F2 in particular measures a row that a later landing superseded — a wiring
  outcome the parent owns, exactly as round 26's F3 did.
- The historical nonzero manifests and `tie-break --check` remain historical
  evidence; "all current commands green" is a statement about the live tree and
  the round-27 successor generations, not about rounds 3/11/18/25/26.
- **F0 is a self-disclosure:** the initial phase was run twice because this seat's
  own driver under-overlaid ignored receipts. The first run is preserved under
  `initial-unoverlaid/`; the corrected run is the one cited.

## Commands (all 2026-10-18, windows above)

- Sweeps: `export TMPDIR=$PWD/.scratch; python3 .scratch/r27-o33-o36-regression/sweep.py initial`
  and `… closing`; per-command stdout/stderr under
  `.scratch/r27-o33-o36-regression/<phase>/`.
- Settle watcher: `.scratch/r27-o33-o36-regression/settle.sh 3 30` (60 s), log
  `settle.log`.
- Frozen replays: `python3 tools/replay-frozen.py <manifest> --json` with
  `TMPDIR` outside the repo (the tool refuses an in-repo mirror root by design).
- F1 control: throwaway clone at `4f09c99`, same replay, 6/6 green.
- F1 mechanism: `python3 tools/gates/typed-pipeline-gate.py
  tools/gates/frozen/round-26/post-register/inputs/examples/culture-d4/packet.d4.yml`
  → `FAIL L1-assembler`.
- F2/F3 legs: `python3 reports/round-26/remainders/pin-repoint-check.py --check`
  (1, 16/17) and `python3 reports/round-26/gate-tests/run-gate-tests.py --check`
  (1, 61/62); successors `… --baseline reports/round-27/pinsweep/v3-baseline-r27/expected.json`
  (0) and `python3 reports/round-27/gate-tests/run-gate-tests.py --check` (0).
- Digests: `sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/packet.d4.typed.yml
  tools/gates/typed-pipeline-gate.py tools/gates/argot-derivation-gate.py
  examples/culture-d4/components/13-register-law.yml`; `git rev-parse HEAD`.
- Replays: the driver runs every `MANIFEST.tsv` under `tools/gates/frozen/**`
  **and** `reports/round-27/**` with `tools/replay-frozen.py … --json`.

## Compliance self-attestation

This seat wrote only `reports/round-27/regression.md` and scratch under
`.scratch/r27-o33-o36-regression/`. No git mutation, no commit, no push, no filed
round-8–26 byte touched, no tool under `tools/` or `examples/` edited, no
historical validator executed. All nonzeros are routed and named, not absorbed.
Scratch placement: the sweep driver sets each command's `TMPDIR` to a per-command
directory inside the lane's `.scratch`, as the lane rule requires; the standalone
replay and the F1 control ran with `TMPDIR` outside the repo
(`/tmp/r27-ctl-base`), which was removed after use.
