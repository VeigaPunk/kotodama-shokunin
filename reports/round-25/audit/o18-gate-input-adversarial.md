# R25-O18 — adversarial review: the gate-input honesty fix

- Seat **R25-O18** (reviewer 1 of 3, gate-input honesty). Round 25 (operator:
  loop 3 of 3, build 1 of 4; 64 workers on `devin/deepseek-v4-1-flash-high` —
  `reports/round-25/targets.json`).
- Date **2026-10-18**. Declared baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`;
  lane HEAD at review start `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.
- Assignment (verbatim): "O R25-O18..O20 (reviewers x3): adversarial pass on
  both fixes (bypass paths, supersession honesty)."
- **Write scope: this fragment and `reports/round-25/audit/o18-probe-matrix.sh`
  only.** No `tools/**`, `examples/**`, `corpus/**`, `SKILL.md`, or filed
  round-8–24 byte is edited; no Git mutation. NON-CANON engineering evidence.
- **This seat authored none of the artifacts it reviews.** It did not write
  `tools/gates/typed-pipeline-gate.py`, `reports/round-25/gate-input/**`, the
  frozen round-25 rows, or the argot gate.
- Scratch: `.scratch/r25-o18/` (`TMPDIR=$PWD/.scratch` preceded every
  scratch-writing command). The frozen replays in §5 need `TMPDIR` **outside**
  the repo; that is stated where it is used.
- **Revision binding.** The gate moved **five times** during this review
  (`04ad4bb4…` → a `61240b8…`-based working state → `879d40bf…` → `bbe3f6ad…` →
  `e0c27f96…` → `b749ad07…`). The **exit codes** of every probe in §4, §7 and §8
  were re-measured at each and are **unchanged**; only the leg *counts* grew as
  the pipeline gained the `L3b-argot` leg (D4 source 19/19 → **20/20**, typed
  16/16 → **17/17**). The §1-§8 prose quotes `879d40bf…` counts; §5's frozen-row
  figures were re-run at `879d40bf…`; §6 records the intermediate selftest red.
  At the last sample (`b749ad07…`, 17:46Z): `absent-source` exit 1 with a
  traceback (§7), `hold-null` exit 0 (§8), `L3b-argot` present, selftest 19/19.
  Both findings therefore stand at every revision this seat sampled.

## 0. Verdict at a glance

| # | probe | verdict |
|---|---|---|
| 1 | the false red is gone on the committed typed packet (exit 0, 16/16) | **holds** |
| 2 | the documented source-packet entry is still 19/19, byte-pinned | **holds** |
| 3 | no regression on flagless / D2 typed / frozen rows / battery | **holds** |
| 4 | the fix is content-keyed, so a **renamed** typed copy behaves identically | **holds** (not a bypass) |
| 5 | a real defect still fails closed (`unmoved-field` exit 1; dropped row, smuggled slot in the gate's own selftest) | **holds** |
| 6 | `--legacy-packet <source>` with the typed packet positional no longer false-reds | **holds** |
| 7 | **unreadable declared source still crashes with a traceback** | **FAIL — pre-existing, not introduced by this fix; the fix's own exit-2 branch is unreachable on the D4 shape** |
| 8 | `hold: null` on **one** moved row still reads green (16/16) | **FAIL — pre-existing gap, named by the design seat as R1; the fix does not widen or close it** |
| 9 | `hold` key **absent** on one moved row still reads green (16/16) | **FAIL — pre-existing gap, named as R2** |
| 10 | the landed gate's `--selftest` was **red** at 14:33Z (KeyError `owed_slot_of`) | **caught mid-flight; green at the 14:34Z revision (19/19)** |

The fix is **honest about what it measures and where it refuses**, and it does
not manufacture findings. Two residual holes (§7, §8) are **pre-existing** on
the source path and were named by the fixer before this review; this fragment
confirms them at the landed revision rather than asserting them from the design
doc. One of them (the unreadable-source traceback) makes the fix's advertised
exit-2 input-class refusal **not reachable on the D4 shape** — that is the
substantive finding, and it is stated with its exact reach.

## 1. What "fails closed and honestly" is being tested against

The claim's `after_required` (a) permits either branch: *a named input-class
diagnostic (exit 2)* **or** *the L2/L3 legs handling null `owed_slots`
correctly*. The landed fix does **both**, plus a third thing the design doc did
not propose — it reads the typed packet's **declared** source
(`typed_assembly.packet`) and grades L2 against *those* bytes instead of
rebuilding them. That third element is what actually removes the manufactured
`DERIV-REPLAY` class; the `nullish` guard alone only moves the verdict from
14/16 to 15/16 (§3).

## 2. Baseline reproduction (pre-fix, on the pinned gate)

Gate bytes at the round-24 close were the `d4-repin` MANIFEST pin
`04ad4bb479562c419b48d750a8f9303c4a5a717ca7f2fe3b3658cc1bb9578a48`.

| input | exit | legs |
|---|---|---|
| `examples/culture-d4/packet.d4.yml` | 0 | 19/19 |
| `examples/culture-d4/packet.d4.typed.yml` | **1** | 14/16 |
| flagless (D2 default) | 0 | 16/16 |
| `examples/culture-d2/packet.d2.typed.yml` | 0 | 13/13 |
| `--selftest` | 0 | 12/12 |

The L3 failure detail is exactly the round-24 cold-run reading: the `holds` and
`routed` halves **agree** (12 = 12); only `owed slots` disagrees — 12 observed
against 18 routing entries, six of them the literal string `'null'`.

## 3. Independent reproduction of the two-part fix

This seat applied the design doc's two parts **by hand** to a scratch copy
before the real tool was touched, to test the design rather than the landing.

- **Part 2 alone** (the `nullish`/`owed_slot` guard): typed packet →
  **exit 1, 15/16**. L3 goes green; L2 still fails on the eight
  `DERIV-REPLAY` lines. This confirms the design's own statement that the two
  parts are independent and that part 2 alone is insufficient.
- **Parts 1+2** (declared-source read + guard): typed packet → **exit 0, 16/16**;
  source packet → 0, 19/19; flagless → 0, 16/16; D2 typed → 0, 13/13;
  `--selftest` byte-identical stdout to the unpatched tool.

The landed revision (sha `879d40bf977eef65…`) reproduces all of the above.

## 4. Bypass probes

All commands 2026-10-18, from the lane root, `TMPDIR=$PWD/.scratch`. Re-runnable
via `sh reports/round-25/audit/o18-probe-matrix.sh` (the script is the filed
copy of `.scratch/r25-o18/probe-matrix.sh`; inputs under `.scratch/r25-o18/`).

| # | probe | input | exit | reading |
|---|---|---|---|---|
| B1 | **filename is irrelevant** — the gate detects typed input by *content* (`typed_channel` key), not by a `.typed.` suffix | a copy of the committed typed packet named `renamed-no-dot-typed.yml` | 0 | the fix keys on the packet, not the path; a name-based "diagnostic" would have left this open |
| B2 | typed positional **plus** `--legacy-packet <source>` | `…packet.d4.typed.yml --legacy-packet …packet.d4.yml` | 0 | the flag arm no longer false-reds; the declared source is read, not rebuilt |
| B3 | source positional **plus** `--legacy-packet <typed>` | `…packet.d4.yml --legacy-packet …packet.d4.typed.yml` | 0 | the wrong-declared-source arm is refused earlier by `L1-assembler` pin comparison on the identity path |
| B4 | `typed_channel` block stripped from the typed packet | `stripped.yml` | **2** | a stripped artifact is no longer typed input; it fails closed at `L1-assembler` (packet bytes ≠ deterministic assembly) |
| B5 | **self-referential** declared source (typed packet declares itself) | `selfref.yml` | **2** | `L1-assembler` refuses; the identity leg catches it before L2 |
| B6 | **cross-family** declared source (typed D4 packet declares the D2 source, pin updated to the D2 digest) | `cross-family-source.yml` | **2** | `L1-assembler` refuses: the D2 bytes are not the D4 assembler's output. The gate does not silently grade a foreign family's source |

B1 is the important negative: the round-24 scribe suggested a *named
input-class diagnostic*; a diagnostic implemented by filename matching would
have passed the committed case and failed B1. The landed fix is content-keyed
and passes B1.

## 5. No-regression evidence (the fix is behavior-preserving where pinned)

| surface | command | result |
|---|---|---|
| source packet, byte-pinned | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit 0, 19/19; stdout sha256 `b064da286d2dd02904788fc3fe4f3bd97fe7e88bbcac657cee114d0a607100bd` = the `d4-repin` MANIFEST pin |
| D2 typed direction | `… examples/culture-d2/packet.d2.typed.yml` | exit 0, 13/13; stdout sha256 `9a69985aabdf3e9b…` = the round-18 pre-generalization baseline pin |
| flagless D2 default | `python3 tools/gates/typed-pipeline-gate.py` | exit 0, 16/16 |
| gate's own selftest | `--selftest` | exit 0, **19/19** at the landed revision (§6) |
| generalized selftest | `--selftest-generalized` | exit 0, 14/14 |
| gate battery | `python3 tools/check-gate-battery.py` | exit 0, 7/7 pass, 0 fail |
| round-25 frozen rows (6) | `TMPDIR=/tmp/… python3 tools/replay-frozen.py tools/gates/frozen/round-25/gate-input/MANIFEST.tsv` | `REPLAY OK: 6/6 rows reproduced` (2 of them recorded **exit 2** refusals — a reproduced red stays red) |
| round-22 frozen rows (3) | `TMPDIR=/tmp/… … tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` | 2 reproduced, **1 could-not-evaluate `gate_digest_mismatch`** — expected and correct: the gate was re-pinned in a **new** round-25 generation, and the filed round-22 MANIFEST is never edited |
| round-11 / round-18 / round-20 / round-23 frozen rows | `TMPDIR=/tmp/… … tools/gates/frozen/{round-11,round-18/repin-d2,round-20/repin-d2,round-23/repin-d2}/MANIFEST.tsv` | each: **10/11 reproduced, 1 could-not-evaluate `gate_digest_mismatch`** — the same new-row cascade, independently measured here and matching the fixer's own `verify.md` table |

The last two rows are the pin discipline working as declared: a re-pin is a new
row, and the old row reads `could-not-evaluate` rather than a false green. The
gate sha therefore appears in **five** filed historical MANIFESTs as a
`could-not-evaluate` — that is the honest cost of a pinned-tool fix, and the
round-25 generation is the replacement record. The one row that still reproduces
inside each old manifest is the D2 typed direction (stdout sha
`9a69985aabdf3e9b…`), which is byte-identical across the fix (§5) — so the
cascade is a pin-identity change, not a behaviour change.

## 6. The selftest was red mid-flight (timing finding, since resolved)

At **14:33Z** the landed gate (`sha 61240b8`-based working bytes) had
`--selftest` **exit 1** with `KeyError: 'owed_slot_of'` — the new hazard control
3b called `module["owed_slot_of"]` while the function was still named
`owed_slot`. That is a **worker-visible red** on the claim's own regression
command, and the claim's counting command lists `typed-pipeline-selftest` as a
regression. It was corrected by 14:34Z (`sha 879d40bf…`, selftest 19/19).

This is recorded because the round's "all regressions green" clause is only
true of the **final** revision; a reader who sampled at 14:33Z would have seen
the opposite. The landed revision is green and re-measured in §5.

## 7. FINDING — the advertised exit-2 refusal is unreachable on the D4 shape

The fix adds an input-class refusal: when the typed packet names a source that
is **unreadable**, the gate should print a named diagnostic and exit 2. That
branch exists (`result["input_class"] = "typed-unresolvable"`), but on the D4
artifact shape it **never runs**, because `L1-assembler` aborts the run first:

```
$ python3 tools/gates/typed-pipeline-gate.py <typed packet declaring a missing source>
…
FileNotFoundError: [Errno 2] No such file or directory:
  '…/examples/culture-d4/NOPE-absent.yml'
exit=1        ← a traceback, not a named refusal, and not exit 2
```

`grading()` calls `assembler_identity(config["packet"], …)` at the top of the
generalized path, and `assembler_identity` does
`actual = Path(packet_path).read_bytes()` with no `is_file()` guard. A typed
packet whose declared source is absent therefore crashes **before** the
input-class branch is reachable.

- **Not introduced by this fix**: the same traceback reproduces on the pinned
  pre-fix gate (`04ad4bb4…`), so this is a pre-existing `assembler_identity`
  robustness gap, not a regression.
- **Not covered by the fix's own controls**: the fixer's frozen control
  `controls/typed-without-source.yml` declares
  `typed_assembly.packet: examples/culture-d2/packet.absent.yml` **but keeps a
  valid `assembly.packet_sha256` and is a D2-shaped artifact**, so it takes the
  D2 identity path and reaches the exit-2 branch. The D4 shape does not.
- **Consequence for the claim's wording**: the claim says the fix must "fail
  closed and **honestly**". A traceback at exit 1 on a missing declared source
  is closed but not honest — it is the same class the round-24 cold run named
  for malformed input, which the gate otherwise handles at exit 2 with "no
  traceback" (its own selftest asserts that for the malformed case).
- **Minimal repair** (not applied; outside this seat's write scope): guard
  `assembler_identity`'s read with `Path(packet_path).is_file()` and return a
  named refusal, so the declared-source check and the input-class check agree.

Severity: **medium** — it does not produce a false green or a manufactured
finding, and it is pre-existing; but it means the fix's exit-2 story holds only
for one family shape, and the round must not read "the gate fails closed and
honestly on derived-packet input" as family-general.

## 8. FINDINGS — two pre-existing holes the fix does not close

Both were named by the fixer's `design.md` §5.4 as R1/R2 and are **confirmed
here at the landed revision** by independent mutation of the committed packet.

| # | mutation | landed gate | reading |
|---|---|---|---|
| R1 | `hold: null` on **one** moved `LEX-GAR-0x` routing row | **exit 0, 16/16** | the reader keeps `'null'` as a string; `routing_hold_ids` tests bare truthiness, so the null becomes a hold id and the mismatch with the finding set cancels out |
| R1b | `hold: null` on **all twelve** moved rows | exit 1, 15/16 | only the all-rows mutation is caught — the single-row case is invisible |
| R2 | `hold` key **absent** on one moved row | **exit 0, 16/16** | the record drops out of both sides of the comparison (`routing_hold_ids` and `hold_records`), so the equality still holds |
| R2b | same mutation on the **D2** typed packet | exit 0, 13/13 | the hole is family-general, not D4-specific |

R1/R1b is the sharper one: a **laundered single hold** — exactly the class the
round-18 `neg-1.md` controls were written for — reads green when the hold is
nulled rather than deleted. The gate's own selftest covers the *deleted*
routing row (`dropped routing row`) and the *renamed-to-note* hold
(`laundered hold`), but not the **nulled** hold.

Severity: **medium for R1/R1b, low for R2** — both are pre-existing (the source
path reads the same code and is 19/19), both were disclosed by the fixer, and
neither is a manufactured finding. They are recorded because the claim's
`after_required` says "fail closed and honestly", and §8's evidence bounds that
claim: the L3 leg is honest about the *committed* packet, not about an
adversary who nulls a hold.

## 9. What this review does NOT establish

- It does not certify the round-25 frozen rows' **content** — only that they
  replay. A reproduced red verdict stays red.
- It does not test the argot leg (that is R25-O19/O20's surface).
- It ran no historical validator, so it did not rewrite any filed receipt.
- The mid-flight selftest red (§6) is reported from one sample; it cannot
  establish how long the red window was.

## 10. Reproduce

`reports/round-25/audit/o18-probe-matrix.sh` is **self-contained**: it rebuilds
every mutation it needs under `$TMPDIR/o18-probe/` from the committed packets, so
it does not depend on this seat's gitignored scratch. It grades the gate from its
**live** bytes, so record the gate sha alongside the output.

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
sha256sum tools/gates/typed-pipeline-gate.py             # 879d40bf… at review time
sh reports/round-25/audit/o18-probe-matrix.sh            # the 13-row matrix
TMPDIR=/tmp/r25-probe python3 tools/replay-frozen.py \
  tools/gates/frozen/round-25/gate-input/MANIFEST.tsv    # 6/6
TMPDIR=/tmp/r25-probe python3 tools/replay-frozen.py \
  tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv      # 2 reproduced, 1 cne
python3 tools/gates/typed-pipeline-gate.py --selftest    # 19/19
python3 tools/check-gate-battery.py                      # 0, 7/7
```

Assertions at gate sha `879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126`
(measured 2026-10-18 17:40Z; the leg **counts** quoted in §1-§8 are this
revision's — `19/19`, `16/16`, `13/13`, `15/16`):

| matrix row | expected | at `bbe3f6ad…` (17:44Z) |
|---|---|---|
| `source-packet` | exit 0, 19/19 | exit 0, **20/20** |
| `typed-packet` | exit 0, 16/16 | exit 0, **17/17** |
| `d2-typed-packet` | exit 0, 13/13 | exit 0, 13/13 |
| `renamed-typed-copy` | exit 0, 16/16 | exit 0, **17/17** |
| `typed_channel-stripped` | exit 2 | exit 2 |
| `absent-declared-source` | exit 1 **with a traceback** (§7) | exit 1 **with a traceback** — **unchanged** |
| `selfref-declared-source` | exit 2 | exit 2 |
| `cross-family-source` | exit 2 | exit 2 |
| `unmoved-field` | exit 1 | exit 1 (**16/17**) |
| `hold-null-single-row` | **exit 0** (§8 — the gap) | **exit 0 — unchanged** |
| `hold-null-all-rows` | exit 1 | exit 1 |
| `hold-key-absent-row` | **exit 0** (§8 — the gap) | **exit 0 — unchanged** |
| `d2-hold-null-row` | **exit 0** (§8 — the gap) | **exit 0 — unchanged** |

**Re-verification at the gate's final revision (`bbe3f6ad…`).** The gate moved
again while this review was open (`879d40bf…` → `bbe3f6ad…`, which adds a leg to
the D4 pipeline: 19/19 → 20/20, 16/16 → 17/17). Every **exit code** in the matrix
is unchanged, including both §7 and §8 findings — the leg-count shift is the new
leg, not a behaviour change. The two findings therefore stand at the newest
revision this seat sampled; only the pass *counts* in the prose above are
revision-specific.
