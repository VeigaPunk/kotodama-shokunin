# Round 25 — O R25-O04..O07 — gate-input implementation (single writer of the gate file)

- **Seat:** R25-O04..O07, round 25 (operator loop 3 of 3, build 1 of 4;
  `devin/deepseek-v4-1-flash-high`). Claim **O** / operability, before-clause (a)
  (`reports/round-25/claims.json`).
- **Assignment (verbatim):** "O R25-O04..O07 (gate-input impl, single writer of
  the gate file): implement the chosen fix (named input-class diagnostic exit 2
  OR correct null handling) with selftest controls; D2 default 16/16
  byte-identical; pin cascade as new rows. reports/round-25/gate-input/impl.md."
- **Date:** 2026-10-18. Baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`;
  worktree HEAD `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- **canon:** NON-CANON engineering evidence. A freeze pins bytes and verdicts,
  never design quality or lore standing.
- **writes:** `reports/round-25/gate-input/impl.md` (this file) plus gitignored
  scratch under `.scratch/r25-o04/` (`export TMPDIR=$PWD/.scratch` preceded every
  scratch-writing command; the frozen replays need `TMPDIR` **outside** the repo).
  No filed artifact of rounds 8–24 was edited; no git mutation.

## 0. What this seat actually did, and the concurrency that shaped it

**Honest framing first.** The assignment names this seat the *single writer* of
`tools/gates/typed-pipeline-gate.py`. That did not hold: a **concurrent sibling
round-25 seat (O08..O10)** wrote the same file while this seat worked, and the
landed revision is a convergence of two independent derivations. This file
records exactly which parts are this seat's and verifies the whole.

Timeline measured from the file's own mtime and `sha256sum` (all 2026-10-18):

| time | gate sha256 (12) | event |
|---|---|---|
| seat start | `04ad4bb47956…` | the pinned revision (the `d4-repin` MANIFEST pin); both symptoms live |
| 14:2x | `04ad4bb47956…` | this seat reproduces the false red, prototypes the fix on scratch copies |
| 14:31:58 | `ec65d6550e87…` | **sibling O08..O10 lands the implementation body** in the working tree |
| 14:33:25 | `879d40bf977e…` | the file settles at the revision the round-25 generation pins |
| 14:34:14 | `daeaa7220a06…` | this seat removes one vacuous control; **reverted** byte-identically (see §5) |

**Landed revision (verified by this seat):** `sha256
tools/gates/typed-pipeline-gate.py` =
`879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126`, 1528 lines,
`git diff --stat` = **+199/−31** against HEAD (`04ad4bb4…`).

**What landed (two root causes, fixed independently from the same round-24
reading):**

1. **Null-ish `owed_slot`** — a new `nullish()` predicate next to `moved_field()`
   (`:193`), factored out and reused by both `moved_field` (`:202`) and the new
   `owed_slot_of` (`:213`); `routed_slots` now filters through it (`:840`). The
   lane's reader keeps an unquoted YAML `null` as the **string** `"null"`, so the
   bare truthiness test admitted six phantom owed slots on the D4 typed packet.
2. **L2 legacy arm** — a typed packet handed in directly now grades against the
   source it **declares** under `typed_assembly.packet` (read by
   `declared_paths`, `:285`), digest-checked against its own
   `assembly.packet_sha256` (`:634-689`). Unreadable or stale → **named
   input-class refusal, exit 2** (`typed-unresolvable` / `typed-stale-source`);
   only an unnamed packet falls back to the lossy `yaml_lines` rebuild, and then
   only if it round-trips, so a manufactured delta becomes `typed-unfaithful-rebuild`
   (exit 2) instead of a plausible false red. `result["input_class"]` is exposed
   in `--json` (`:977`).

**What is this seat's:** the `owed_slot_of` helper and the declared-assembler
rebuild branch this seat prototyped were **superseded** by the sibling's
equivalent (stronger) forms; the parts of this seat's work that **survived into
the landed revision** are the selftest controls 3b/3c/3d (`:1085-1117`) — see §4.
No design credit is claimed for the implementation body.

## 1. The false red, before and after

Gate bytes pinned at the `d4-repin` MANIFEST pin `04ad4bb4…` for the "before"
column; `879d40bf…` for the "after" column. `TMPDIR=$PWD/.scratch` unless noted.

| # | Command | Before | After |
|---|---|---|---|
| R1 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit 0, 19/19 | exit **0, 19/19** (unchanged) |
| R2 | `… examples/culture-d4/packet.d4.typed.yml` | exit **1, 14/16** (`FAIL L2-channel` 8 `DERIV-REPLAY`; `FAIL L3-routing-consistency` 6 `'null'`) | exit **0, 16/16** |
| R3 | `…` (flagless, D2 default) | exit 0, 16/16 | exit **0, 16/16, byte-identical** |
| R4 | `… --selftest` | exit 0, 12/12 | exit **0, 19/19** |
| R5 | `… --selftest-generalized` | exit 0, 14/14 | exit **0, 14/14** |

R2's `--json` now reports `input_class = "typed-declared-source"`, `ok: true`,
`exit_code: 0`, `derived_packet.deriv_replay_lines = 0`,
`nullish_routing = false`. The documented source entry (R1) still passes 19/19 —
the claim's `after_required` in full.

## 2. Regression evidence (the "harm none" half)

| # | Run | Result | Identity check |
|---|---|---|---|
| C1 | `examples/culture-d4/packet.d4.yml` | exit 0, 19/19 | stdout sha256 `b064da286d2dd02904788fc3fe4f3bd97fe7e88bbcac657cee114d0a607100bd` = the `d4-repin` MANIFEST output pin |
| C2 | `examples/culture-d4/packet.d4.typed.yml` | exit 0, 16/16 | stdout sha256 `38dc76dc5965ceecbb6d0aac141655344111dd558e301b2b0dfd7e741d9131ce` = the round-25 frozen row pin |
| C3 | flagless D2 default | exit 0, 16/16 | stdout **byte-identical** to the pre-fix capture (both `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b`) |
| C4 | `examples/culture-d2/packet.d2.typed.yml` | exit 0, 13/13 | stdout sha `9a69985aabdf3e9b…` = the round-11/23 frozen pin |
| C5 | `tools/gates/frozen/round-11/typed-pipeline/packet.d2.typed.yml` | exit 0, 13/13 | stdout sha `9a69985aabdf3e9b…` = the frozen row pin |
| C6 | `python3 tools/check-gate-battery.py` | exit **0** | 7/7 selftests, 9/9 coverage, `unevaluable: 0` |

C3 is the round-18 O claim's invariant (the default path is exactly the
pre-generalization behavior) and it holds at the byte level, not merely at the
exit level.

## 3. The pin cascade, as new rows

`typed-pipeline-gate.py` is sha-pinned, so the fix is a re-pin cascade routed
like the round-22→25 recipe — **new rows, never edits to a filed receipt**.

- **New generation:** `tools/gates/frozen/round-25/gate-input/` (14 files):
  `MANIFEST.tsv` (6 rows), four input snapshots under `inputs/`, two fail-closed
  control inputs under `controls/` (`typed-without-source.yml`,
  `typed-stale-source.yml`), four captured outputs, and `freeze.txt`.
- **Replay:** `TMPDIR=<outside repo> python3 tools/replay-frozen.py
  tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` → **exit 0, 6/6 rows
  reproduced, bytes=match** (four input-class rows: D2/D4 × source/typed; two
  exit-2 controls). In-repo `TMPDIR` is refused `mirror_unsafe` by design.
- **Superseded rows are named, not rewritten.** The predecessor `04ad4bb4…` is
  pinned in five filed generations; four of them carry a `typed-pipeline-gate.py`
  row that now reads one `could-not-evaluate` (`gate_digest_mismatch`):

  | generation | replay after the fix |
  |---|---|
  | `round-25/gate-input/MANIFEST.tsv` | **REPLAY OK 6/6** |
  | `round-22/d4-repin/MANIFEST.tsv` | could-not-evaluate 1, reproduced 2/3 |
  | `round-11/MANIFEST.tsv` | could-not-evaluate 1, reproduced 10/11 |
  | `round-18/repin-d2/MANIFEST.tsv` | could-not-evaluate 1, reproduced 10/11 |
  | `round-20/repin-d2/MANIFEST.tsv` | could-not-evaluate 1, reproduced 10/11 |
  | `round-23/repin-d2/MANIFEST.tsv` | could-not-evaluate 1, reproduced 10/11 |

  Restoring the predecessor blob (`git show
  f74fc94:tools/gates/typed-pipeline-gate.py`) returns those four manifests to
  full reproduction; no historical manifest is edited here. This is the
  documented cascade convention (`tools/gates/frozen/round-18/README.md`: "a
  re-freeze is a new recording, never an in-place edit").
- **`tools/gates/typed-pipelines.json`** carries no gate-sha field, so it does
  not move. **No committed baseline pins this gate**: `grep -rl
  typed-pipeline-gate tools/gates/expected` returns only the two
  `d4-typed-labels-check-gate` baselines, and those pin `tools/d2-typed-labels.py`,
  not this gate — so `check-gate-battery.py` duty 2 stays green (C6).

## 4. Selftest controls (this seat's surviving contribution)

The landed `--selftest` grew from 12 to **19** checks. This seat's three are:

- **3b — `owed_slot normalization: the null-ish truth table holds`** (`:1085`):
  drives `owed_slot_of` over a seven-row truth table (`{}`, `None`, `"null"`,
  `"  ~ "`, `""`, `5`, `"LEX-GAR-01"`) and asserts the null-ish rows map to
  `None` while a real slot id passes through.
- **3c — `phantom owed slot: a null-ish owed_slot never reaches the
  comparison`** (`:1095`): rewrites the D2 typed fixture's `owed_slot:
  "LEX-GAR-01"` to `owed_slot: null`, runs the gate `--json`, and asserts exit 1
  with the literal `'null'` **absent** from the `L3-routing-consistency` detail —
  i.e. the phantom slot no longer enters `routed_slots`.
- **3d — `declared-assembler source leg: absent without a declared assembler`**
  (`:1111`): asserts the D2 mirror emits no `L2-legacy-source` leg.

The sibling's controls (also green) are the input-class set at `:1140`: a typed
input graded against its declared source (exit 0, `--json` reports the class), a
typed input whose source is absent (exit 2, class named), and one whose source is
stale against its pin (exit 2, class named).

Full `--selftest`: **19/19 passed, exit 0**. `--selftest-generalized`: **14/14
passed, exit 0**.

**Disclosed limitation (3d is vacuous).** The landed implementation never emits a
check id `L2-legacy-source` — it uses `input_class` values instead
(`typed-declared-source`, `typed-unrebuilt`, …). Control 3d therefore asserts the
absence of a leg that could not appear, i.e. it is a tautology that can never
fail. It is a leftover from this seat's superseded prototype, and it is **not**
evidence. §5 records why it was left in place.

## 5. The one edit this seat made and reverted, and why

At 14:34:14 this seat removed the vacuous 3d control (§4) — a genuine small
improvement. That edit changed the gate digest to `daeaa7220a06…`, which
**immediately invalidated the round-25 generation a sibling had frozen 25 seconds
earlier** at 17:33:49Z:

```
$ python3 tools/replay-frozen.py tools/gates/frozen/round-25/gate-input/MANIFEST.tsv
REPLAY COULD-NOT-EVALUATE: 6 could-not-evaluate, 0 mismatch, 0 reproduced of 6 row(s)
```

Three sibling round validators were mid-run against that generation at the time.
Since the control is a no-op either way (it cannot fail), the fix's value was
zero while its cost — a second cascade on top of a cascade, mid-flight — was
real. **The edit was reverted byte-identically**: the gate is back at
`879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126` and the
round-25 replay is `6/6` again. The vacuous control is left in place and named
here instead. **Follow-up for a seat that owns a fresh re-pin window:** delete
`:1111-1117` and re-freeze `round-25/gate-input/` as a successor generation.

## 6. Counting command — the claim's own runner

`reports/round-25/run-validation.py` refuses to run outside an isolated clone
("run round validators only in an isolated Git clone under the lane's
`.scratch`"), so this seat ran it in `.scratch/r25-o04/vclone` (git clone +
`rsync` overlay of the working tree, `TMPDIR` outside the repo):

```
claim O: FAIL
claim D: FAIL
claim C: PASS
acceptance_checks_passed: False
missing_dependencies: reports/round-25 (successor v3 row)
```

**The gate-input leg of claim O passes in full.** From the runner's own
measurement (`claims.O.measurement.gate_input_honesty`):

| leg | measured |
|---|---|
| `source_packet` | exit 0, **19/19** |
| `derived_packet` | exit 0, **16/16**, `deriv_replay_lines: 0`, `nullish_routing: false` |
| `control_corrupted_packet` | exit **2** |
| `control_tampered_expectation` | exit **1** |

The single O failure is the **v3-supersession** leg ("no superseding v3 row
landed under `reports/round-25`") — a different seat's assignment. Claim D's two
failures are the argot capability (also a different seat). This seat's assignment
(gate-input impl + controls + cascade) is complete and green; **the round as a
whole is not green**, and this file does not claim otherwise.

## 7. Reproduce everything

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
G=tools/gates/typed-pipeline-gate.py
python3 $G examples/culture-d4/packet.d4.yml          # 0, 19/19  (source entry)
python3 $G examples/culture-d4/packet.d4.typed.yml   # 0, 16/16  (the false red is gone)
python3 $G                                            # 0, 16/16  (D2 default, byte-identical)
python3 $G examples/culture-d2/packet.d2.typed.yml   # 0, 13/13
python3 $G --selftest                                 # 0, 19/19
python3 $G --selftest-generalized                     # 0, 14/14
python3 tools/check-gate-battery.py                   # 0, 7/7 selftests, 9/9 coverage
# cascade replay (TMPDIR must be OUTSIDE the repo)
TMPDIR=/tmp/r25 python3 tools/replay-frozen.py tools/gates/frozen/round-25/gate-input/MANIFEST.tsv
#   -> REPLAY OK: 6/6 rows reproduced
```

Scratch artifacts (gitignored): `.scratch/r25-o04/` — `typed-pipeline-gate.prefix.py`
(pre-fix copy), `d2-default.prefix.out` / `d2-default.final.out` (the byte-identity
pair, both `15cdfbda…`), `selftest*.out`, `gate.proto.py` / `gate.proto2.py`
(this seat's superseded prototypes), `vclone/` + `vtmp/` (the isolated runner
clone), `o04-check.json`.

## 8. Named residuals and open items (not fixed here)

- **3d vacuity** (§4/§5) — needs a fresh re-pin window to remove; named, not
  silently dropped.
- **The five historical `typed-pipeline-gate.py` rows** now read one
  `could-not-evaluate` each (§3). The runner does **not** catch this: it runs
  `replay-frozen.py --selftest` only (`run-validation.py:162`), which replays no
  manifest, so a broken pin is invisible to the counting command.
- **`reports/round-25/gate-input/verify.md`** — referenced by
  `tools/gates/frozen/round-25/gate-input/freeze.txt` (`frozen_by: … (…/verify.md)`).
  It did not exist when this file was written; a sibling seat landed it at 14:36
  (11 KB). This `impl.md` is the impl-side record, not that verification.
- **`design.md` §8** (the sibling seat) already records the same cascade state and
  the same convergence; this file is the impl-side confirmation, not a duplicate
  claim.
- **R1/R2/R4** in `design.md` §5.4 (`hold: null` on a moved row; the `hold` key
  absent; `moved_records` built from all 12 routing rows) remain out of scope and
  unmeasured by this seat.
