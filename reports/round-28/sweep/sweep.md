# R28-O25..O32 — the final pin sweep: every frozen surface re-verified, the drifted ones re-pinned

- **Seat:** R28-O25..O32 (the final build-round pin sweep x8), round 28, loop 3
  build 4 of 4 (the last build round), claim **O** `operability`
  (`reports/round-28/claims.json`).
- **Date:** 2026-10-18. Declared baseline revision
  `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede` (round-27 admit); lane HEAD
  `69cecbc7dcf575a29f29660ecac470e05260fd86` (round-28 declare).
- **Writes:** `reports/round-28/sweep/` and `reports/round-28/pinsweep/` only, plus
  the two `V3_*_DEFAULT` constants in `tools/exercise-handoff-e2e.py`. No filed
  round-8..27 byte was edited; no git commit, no push.
- **Canon:** NON-CANON engineering evidence. A pin is integrity, never truth and
  never clearance; a reproduced red verdict stays red.
- The machine census is `sweep-census.md` / `sweep-receipt.json`; this file is the
  human reading of it.

## 0. Verdict

Every file class in the lane that carries a digest pin over a D4 surface is
enumerated and re-verified against the amended packet: **121 surfaces, 10
families, 39 findings**. **Eight D4 surfaces drifted**, and all eight are
re-pinned as NEW rows, each verifying green:

| # | drifted surface (filed) | new row | control | fix |
|---|---|---|---|---|
| 1 | `tools/gates/expected/d4-assembly-check-gate/r19-pre/` | `pinsweep/baselines/d4-assembly-check-gate/r28-post/` | exit **1** drift | exit **0**, `c60820a5…` |
| 2 | `tools/gates/expected/d4-typed-labels-check-gate/{r19-pre,r20-post,r22-post}/` | `pinsweep/baselines/d4-typed-labels-check-gate/r28-post/` | exit **1** drift | exit **0**, `1c8add32…` |
| 3 | `reports/round-27/pinsweep/frozen/r27-post/` (family J) | `pinsweep/frozen/r28-post/MANIFEST.tsv` | replay mismatch 2/2 | **REPLAY OK 4/4** |
| 4 | `tools/gates/frozen/round-{18,22}/**` (D4-leg rows) | `pinsweep/frozen/r28-post/MANIFEST.tsv` | replay mismatch 2/2 | **REPLAY OK 4/4** |
| 5 | the `typed-pipeline-gate.py` D4 rows (**X61R28-A2**) | `pinsweep/frozen/r28-post/` rows 4–5 | exit **2** at the filed snapshots | **REPLAY OK 4/4** |
| 6 | `tools/exercise-handoff-e2e.py` `V3_BASELINE_DEFAULT` (the tool's own default) | re-pointed to `pinsweep/v3-baseline-r28/expected.json` | default `--profile v3 --quiet` exit **1** | exit **0** |
| 7 | the v3 handoff chain `reports/round-{20,22,25,26,27}/*/expected.json` | `pinsweep/v3-baseline-r28/` | `E2E-DIGEST` | exit **0**, packet `a20ae059…` |
| 8 | the D4 hold set `examples/culture-d4/expected-holds.json` | re-pinned by the D seat to `543d68a8…` | (D seat's row) | green |

Independently: the gate battery over the four roots reads **9/9 coverage, 21
pinned, 0 unevaluable, exit 0**; the battery's own selftest is **35/35**; this
sweep's own selftest is **12/12**; and the lane validator
(`python3 reports/round-28/run-validation.py`) reads **D PASS / O PASS / C PASS,
acceptance true, exit 0, missing dependencies none**. The validator's own sweep
reading is 307 pin rows, 157 green, 150 drift, **8/8 drifted surfaces re-pinned,
unrepinned empty**.

## 1. What moved, and why — the stamp table

The round-28 D claim lands the RL-1 law replay leg and the RL-4 `packet_keys`
fix. Both amend the D4 component tree, so the packet and its derived artifacts
moved once inside this round's window.

| stamp (local) | `packet.d4.yml` | `typed-labels.d4.yml` | `expected-holds.json` | what happened |
|---|---|---|---|---|
| round-27 close | `86079a67…` | `88a94422…` | `857417e9…` | the round-27 register law (revision 2) |
| ~20:13Z | **`543d68a8…`** | **`339bfd83…`** | `857417e9…` (stale) | **RL-4 lands**: `03-orthography.yml` declares `packet_keys: [orthography, records, literacy_institutions]` and `09-costumes.yml` adds `enforcement`; `records`, `literacy_institutions` and `enforcement` enter the packet as list blocks |
| ~20:21Z | `543d68a8…` | `339bfd83…` | **`65f5a03e…`** | the D seat re-pins the hold set to the amended packet |
| **final (settled)** | **`543d68a8…`** | **`339bfd83…`** | **`65f5a03e…`** | the stamp every row below is re-pinned at |

Measured commands: `sha256sum examples/culture-d4/packet.d4.yml
examples/culture-d4/typed-labels.d4.yml examples/culture-d4/expected-holds.json`;
the tree was read repeatedly at 25–60 s intervals with no byte changing after the
hold-set re-pin. The round-27 pinsweep's own `frozen-rows.md` (§1) and the round-28
audit `x61-pin-sweep.md` (§0) independently record the same `86079a67…` →
`543d68a8…` movement.

**A reader who pins the middle stamp pins bytes that no longer exist** — the hold
set was still stale at ~20:13Z, and the v3 chain moved again when the D seat
re-pinned it.

## 2. The census — 10 surface families

`sweep.py` walks these families itself and re-derives every pin from the bytes;
it never reads a verdict from a replayer for the pin comparison.

| family | what it is | surfaces | drifted |
|---|---|---:|---:|
| A | `MANIFEST.tsv` rows under `tools/gates/frozen/**` + `reports/**/frozen/**` | 12 manifests / 86 rows (16 D4) | 11 |
| B/C | committed `expected.json` under the battery's three roots | 4 (D4) | 4 |
| D | `freeze-receipt.json` embedded pin maps under `tools/gates/frozen/**` | 3 (all D4) | 3 |
| E | `reports/**/expected*.json` handoff baselines (v2 + v3 families) | 11 | 9 |
| F | `tools/gates/typed-pipelines.json` (the live L1-profile channel) | 1 | 0 |
| G | `expected-holds.json` self-pins | 1 (D4) | 0 |
| H | `twin.json` `artifact_manifest` pins | 8 | 8 |
| I | `reports/**/evidence/*.json` embedded D4 path→digest pairs (historical) | 3 (25 pins) | 14 stale pins |
| **J** | **the round-27 pinsweep's own NEW rows** (filed, superseded) | **4** | **4** |

**121 surfaces, 39 findings.** Family I's 14 stale pins are *historical by
design* — an evidence receipt records the stamp it measured — so they are a
coverage surface, not drift owed a successor.

### 2.1 Family J — the R28 addition, and why it is the load-bearing one

R27's sweep excluded its own output with a `"round-27" in rel` guard. That was
defensible for R27 (a sweep cannot treat its own fresh rows as independent
surfaces) and **wrong for R28**: `reports/round-27/pinsweep/` is now a *filed
round-27 artifact* whose rows pin the round-27 stamp, and the round-28 landing
moves the D4 bytes under them. This sweep's guard excludes `round-28` only.

Measured, the family is not decoration — **all four rows drift**, and each is a
different surface class:

| row | drifted pins | why |
|---|---:|---|
| `baselines/d4-assembly-check-gate/r27-post/expected.json` | 3 | pins the pre-RL-4 packet + components |
| `baselines/d4-typed-labels-check-gate/r27-post/expected.json` | 2 | pins the pre-RL-4 projection |
| `frozen/r27-post/freeze-receipt.json` | 2 | its `input_pins`/`pins` maps name the pre-RL-4 bytes |
| `v3-baseline-r27/expected.json` | 6 | the v3 read set moved |

Replayed, `reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` now reads
**mismatch 2/2** where it read green 2/2 when frozen in round 27 — the same
cascade class the round-26 `register/repin.json` reported for its own
predecessors, one round later. This sweep's selftest asserts that supersession
rather than assuming the old generation still reproduces.

### 2.2 Two scoping decisions, recorded so a reader can disagree

- **A frozen generation's `inputs/` copies are historical by design.**
  `tools/gates/frozen/<round>/<gen>/inputs/<path>` is the snapshot that
  generation recorded against; its pins deliberately name that stamp's bytes.
  Re-verifying them against the live tree would flag every filed generation —
  that is the append-only rule working, not a finding.
- **`examples/culture-d2/expected-holds.json` is out of surface.** It pins the
  D2 packet; the D2 drill is not this sweep's subject. Family G admits a hold set
  by its `packet_sha256` naming a recorded D4 packet digest, and the recorded set
  is now *discovered* from the lane's own `supersedes_pins` maps and the profile's
  `superseded` notes rather than hand-copied — so it tracks the lane instead of
  freezing a round-27 list.

## 3. Every frozen generation, replayed

`TMPDIR` outside the repo (an in-repo `TMPDIR` makes every row `mirror_unsafe` —
the tool's designed boundary, §5). 12 manifests, all replayed:

| manifest | exit | reproduced | mismatch | could-not-evaluate |
|---|---:|---:|---:|---:|
| `reports/round-17/tests/frozen` | 0 | 5 | 0 | 0 |
| `round-11` | 2 | 10 | 0 | 1 |
| `round-18` | 1 | 0 | 2 | 0 |
| `round-18/repin-d2` | 2 | 10 | 0 | 1 |
| `round-20/repin-d2` | 2 | 10 | 0 | 1 |
| `round-22/d4-repin` | 2 | 0 | 2 | 1 |
| `round-23/repin-d2` | 2 | 10 | 0 | 1 |
| `round-25/gate-input` | 2 | 0 | 0 | 6 |
| `round-26/gate-input` | 1 | 4 | 2 | 0 |
| `round-26/post-register` | 1 | 4 | 2 | 0 |
| `round-3`, `round-3/attempt-1` | 2 | 0 | 0 | 7 |

**The load-bearing readings:** `round-26/post-register` replays 4/6, mismatch 2
(the same supersession round 27 reported), and the round-27 generation is now
superseded too (§2.1). The successor for the D4-leg rows is
`pinsweep/frozen/r28-post/` (§4.2).

## 4. The re-pins, each with its control

Every re-pin is a **NEW row** through the surface's own freezer; no filed byte is
edited (`corpus/knowledge/verification/gate-frozen-run-standard.md` §3). The
machine table is `pinsweep/d4-pins.json` → `rows`; the flat structured rows the
round-28 runner reads are `sweep/repin-rows.json`.

### 4.1 The two D4 adapter baselines

Frozen through `repin.py`, which copies the measured read set into the baseline at
the gate's own relative path.

- `pinsweep/baselines/d4-assembly-check-gate/r28-post/` — 17 inputs pinned;
  stdout `c60820a54742ecaa…`, exit 0.
- `pinsweep/baselines/d4-typed-labels-check-gate/r28-post/` — 6 inputs pinned;
  stdout `1c8add321259a9f0…`, exit 0.

**Controls** (each drifted row re-run at its own filed bytes, 2026-10-18):

```
python3 tools/gates/d4-assembly-check-gate.py  tools/gates/expected/d4-assembly-check-gate/r19-pre/packet.d4.yml
  -> exit 1  "<path> differs from the deterministic assembly"
python3 tools/gates/d4-typed-labels-check-gate.py tools/gates/expected/d4-typed-labels-check-gate/{r19-pre,r20-post,r22-post}/typed-labels.d4.yml
  -> exit 1, 1, 1  "<path> differs from the deterministic projection"
```

**Battery over the new root** (`--baselines-root reports/round-28/pinsweep/baselines`):
`pinned 2, unevaluable 0`. With all four roots declared the run reads **9/9
coverage, 21 pinned, 0 unevaluable, findings 0, exit 0**.

### 4.2 The D4-leg frozen generation — four rows, including the X61R28-A2 closure

`pinsweep/frozen/r28-post/MANIFEST.tsv` records **four** rows, each with its
snapshot under `inputs/`:

```
python3 tools/replay-frozen.py reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv
  -> REPLAY OK: 4/4 rows reproduced the recorded verdicts
```

| row | gate | input | exit | findings |
|---|---|---|---:|---:|
| 2 | `d4-assembly-check-gate.py` | `packet.d4.yml` | 0 | 0 |
| 3 | `d4-typed-labels-check-gate.py` | `typed-labels.d4.yml` | 0 | 0 |
| 4 | `typed-pipeline-gate.py` | `packet.d4.yml` | 0 | 12 |
| 5 | `typed-pipeline-gate.py` | `packet.d4.typed.yml` | 0 | 12 |

**Rows 4–5 close the round-28 audit X61's finding X61R28-A2.** X61 measured that
"the re-pin surface never extended to `typed-pipeline-gate.py`" — the four
`typed-pipeline-gate.py` rows moved by the round-27 law landing and the round-28
RL-4 fix had no successor anywhere in the repo, and the gate is the one the
round's own regression battery names first. This generation supplies those
successors.

Two implementation details worth naming, because a naive version fails:

- **The finding counter must be `^FINDING ` lines, not a JSON `findings` list.**
  `tools/replay-frozen.py:88` counts `FINDING `-prefixed lines. A row written by a
  JSON counter reads 0 against the tool's observed 12 and refuses on replay. Rows
  4–5 use the line counter and replay `count=12/12`.
- **The typed-pipeline rows are graded at their own snapshot**, and the filed
  generations' snapshots pin pre-landing packets, so re-running them at those
  bytes reads exit 2 — the refusal side, measured in §4.4.

`freeze-receipt.json` records the pins, the verdicts and the supersession reason,
including the X61R28-A2 closure.

### 4.3 The v3 handoff baseline, and the default pointer

The lane's own regression (`tools/exercise-handoff-e2e.py --profile v3 --quiet`)
reads a **default** baseline constant inside the tool. Round 27's sweep closed
that surface for the round-27 successor; the round-28 landing re-opened it,
because the constant still named `v3-baseline-r27`, whose packet digest moved.

```
python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-28/pinsweep/v3-baseline-r28
  -> froze packet sha256 a20ae059aa7cac9e28345d1a80a4dae3fa302117e26b5b1405f05b38d12f0001
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet            # the default pointer
  -> handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105
     claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=a20ae059…
```

The tool edit (`tools/exercise-handoff-e2e.py:1933-1934`):

```
- V3_BASELINE_DEFAULT  = "reports/round-27/pinsweep/v3-baseline-r27/expected.json"
- V3_FROZEN_DIR_DEFAULT = "reports/round-27/pinsweep/v3-baseline-r27"
+ V3_BASELINE_DEFAULT  = "reports/round-28/pinsweep/v3-baseline-r28/expected.json"
+ V3_FROZEN_DIR_DEFAULT = "reports/round-28/pinsweep/v3-baseline-r28"
```

**The freeze must follow the re-point, and this row was frozen after it.** The
renderer writes the *live default path* into the packet's own provenance line, so
re-pointing the constant changes the assembled packet by exactly that one line. A
freeze taken before the re-point is self-inconsistent. Measured: the v3 baseline
re-froze to the same `a20ae059…` on a second run — the freeze is **idempotent**.

`expected.json` `b3b21b44…`; `packet.md` `a20ae059…`; read set 58 files;
component digests 26/26; d4 pins 8/8.

**Controls** — the filed v3 baselines it supersedes, each run through the same
replayer:

| baseline | exit | code |
|---|---:|---|
| `reports/round-20/handoff/expected.json` | 1 | `E2E-DIGEST` |
| `reports/round-22/handoff/declared-in/expected.json` | 1 | `E2E-DIGEST` |
| `reports/round-22/handoff/declared-in-r2/expected.json` | 1 | `E2E-DIGEST` |
| `reports/round-26/register/v3-baseline-r26/expected.json` | 1 | `E2E-DIGEST` |
| `reports/round-26/remainders/v3-baseline-r26/expected.json` | 1 | `E2E-DIGEST` |
| `reports/round-27/pinsweep/v3-baseline-r27/expected.json` | 1 | `E2E-DIGEST` |

The round-27 row is the direct predecessor: it was green when frozen in round 27
and the RL-4 landing moved the packet under it.

### 4.4 The controls, measured in one place

`repin.py` re-measures the *refusal* side of every re-pin: each filed row re-run
at its own bytes. **Seventeen rows, all red** (2026-10-18, `TMPDIR` outside the
repo):

| filed control surface | exit |
|---|---:|
| `tools/gates/expected/d4-assembly-check-gate/r19-pre/packet.d4.yml` | 1 |
| `tools/gates/expected/d4-typed-labels-check-gate/{r19-pre,r20-post,r22-post}/typed-labels.d4.yml` | 1, 1, 1 |
| `tools/gates/frozen/round-{22,25,26}/*/inputs/examples/culture-d4/packet.d4.yml` (typed-pipeline) | 2, 2, 2 |
| `tools/gates/frozen/round-18/MANIFEST.tsv` | 1 |
| `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` | 2 |
| `tools/gates/frozen/round-26/post-register/MANIFEST.tsv` | 1 |
| `reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` | 1 |
| `reports/round-{20,22,22,26,26,27}/…/expected.json` (the v3 chain) | 1, 1, 1, 1, 1, 1 |

The green side of each pair is measured by the freeze itself and re-verified in
§4.1–§4.3.

## 5. The `TMPDIR` boundary, measured

`tools/replay-frozen.py:171-198` refuses a mirror whose real path is inside the
repo. This is the tool's designed boundary, not a defect — and it is the trap the
assignment's own `export TMPDIR=$PWD/.scratch` rule walks into for *replays*
specifically. `sweep.py --tmp-parent` refuses an in-repo parent rather than
silently reporting every row unevaluable.

A second environment hazard, found by the round-28 audit X61 (finding
X61R28-A3): `/tmp` is a 16 GB tmpfs shared fleet-wide and hit
`OSError: [Errno 122] Disk quota exceeded` at 80% during this round. Every
measurement in this file wrote its scratch and its JSON receipts to `/var/tmp`,
not `/tmp`.

## 6. What this seat did not do, and what stays open

- **No filed round-8..27 byte was written.** The new rows live under
  `reports/round-28/{sweep,pinsweep}/`. The one non-new-row edit is the tool's own
  `V3_*_DEFAULT` constant, which is a pointer, not a filed artifact, and is
  recorded as its own row.
- **Family H (twins) is reported, not re-projected.** Eight filed twins carry
  `artifact_manifest` pins over the moved D4 artifacts. Three are superseded by
  the v3 chain this seat re-pinned; their successors are the twins in
  `v3-baseline-r28/`. Re-projecting the round-26 r4-revision twins is a *different*
  surface (the r4 twin generator refuses without `--source-root` at its own pinned
  read set) and this seat does not absorb it.
- **`round-26/post-register` is a supersession, not a re-pin target this round.**
  Its D4 rows moved when the register law landed after it was frozen. Its
  typed-pipeline rows are now covered by rows 4–5 of this generation; its
  remaining rows are a named, un-re-pinned remainder.
- **A pin is integrity, never truth.** Re-pinning asserts the bytes moved, never
  that the move was correct, and never that the round arc is complete.
- **This sweep's own rows are excluded from its census** by a `"round-28" in rel`
  guard. That is the R27 guard narrowed by one round, and it inherits R27's
  caveat: it is a substring guard rather than a filed scope decision, so it would
  also silently exclude any *other* round-28 surface that carries a pin.
- **The X61R28-A1 scope note is inherited, not absorbed.** The round-28 audit X61
  measured that `reports/round-17/tests/frozen/MANIFEST.tsv` sits outside the
  round-27 X61 scope although the lane's validator replays it. This sweep's
  family A does walk it (12 manifests / 86 rows, one more manifest than round
  27's 11/81), so the surface is covered here — but X61's own reach is not this
  sweep's to repair.

## 7. Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=/var/tmp/kotodama-r28-sweep      # OUTSIDE the repo

python3 reports/round-28/sweep/sweep.py                    # the census + every replay
python3 reports/round-28/sweep/sweep.py --json             # the receipt
python3 reports/round-28/sweep/sweep.py --selftest         # 12 dependency-free controls
python3 reports/round-28/sweep/repin.py                    # re-freeze every row
python3 reports/round-28/sweep/poll-d-landing.py 20 60     # the dependency poller
python3 tools/replay-frozen.py reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
python3 tools/check-gate-battery.py --baselines-root tools/gates/expected \
        --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines \
        --baselines-root reports/round-28/pinsweep/baselines
python3 reports/round-28/run-validation.py
```

Machine-readable rows: `pinsweep/d4-pins.json` (stale → live, per row, with the
replayer and the control/fix exit codes) and `sweep/repin-rows.json` (the flat
`surface → live digest` rows the round-28 runner reads). Census receipt:
`sweep/sweep-receipt.json`; census text: `sweep/sweep-census.md`; selftest:
`sweep/sweep-selftest.json`.
