# R26-D27 — frozen rows for the register stratum and the round-26 pin tails (new rows only)

- round: 26 (operator: loop 3 of 3, build round 2 of 4; 64 declared workers,
  `devin/deepseek-v4-1-flash-high`). Seat **R26-D27** (D-scribe 3 of 4).
- claim under draft: `reports/round-26/claims.json` claim **D** (rows), with the
  claim **O** pin tails named in §4 because the rows that close them are the same
  generation.
- date: 2026-10-18. Declared baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`.
  Lane HEAD `1ad491a1a4b0aef9ebdc1861dfb8237727503825`; `git status --porcelain`
  clean at the opening read and carrying only round-26 in-flight evidence after.
- **writes: this file only** plus gitignored scratch under `.scratch/r26d/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch write; the frozen replays
  themselves need `TMPDIR` **outside** the repo — §3a).
- **no filed frozen row was edited.** No `MANIFEST.tsv`, no `expected.json`, no
  `freeze-receipt.json` under `tools/gates/frozen/` or `tools/gates/expected/`
  was touched. No commit, no push.
- canon: **NON-CANON engineering evidence.** A freeze pins bytes and verdicts,
  never design quality, scholarship or lore standing; a reproduced red verdict
  stays red.

## 1. The frozen-row discipline this file works inside

`tools/gates/frozen/round-18/README.md` states the rule verbatim: "a re-freeze
is a new recording, never an in-place edit", and "the row is added as a NEW row,
never by editing a recorded one". Round-20, round-22, round-23 and round-25 each
landed a **new generation directory** rather than editing an earlier one. This
file follows that rule: every row proposed here is a new row, and every
superseded row is *named*, never rewritten.

Three mechanical constraints shape any freezable row:

1. `tools/replay-frozen.py` launches a pinned gate as
   `[python3, tools/gates/<gate>.py, <input>]` — **one path, no flags**. A
   flag-shaped check is not freezable, so the gate must resolve flaglessly (the
   reason the round-22 rows R25-2/R25-3 exist over the D4 peer tools).
2. The whitelist is `*.py` files **directly under** `tools/gates`. A row naming
   `tools/d2-typed-labels.py` or `tools/assemble-d4-typed.py` is refused
   `gate_not_whitelisted` **before** any digest check.
3. `TMPDIR` must be **outside** the repo, or every row reads `mirror_unsafe`
   exit 2. The lane's usual `$PWD/.scratch` is inside it. Measured control in
   §3a.

**Two conditions gate every row below.** (i) The register stratum is **not on
disk** at this seat's stamp (measured 18:05:08Z and re-measured 18:06:36Z:
`registers:` / `doublets:` / `doublet_of` / `#plain` / `#quote` → **0** files
under `examples/` and **0** under `tools/`), so no register row can be recorded
as a *demonstrated* capability yet; the rows in §2 are the rows a successor
round records **after** the stratum lands, written now so the recording seat
does not re-derive them. (ii) The `typed-pipeline-gate.py` pin **moved** this
round and every generation that pinned its predecessor now refuses its
typed-pipeline row — §4 is the measurement and the row class that closes it.

## 2. The frozen rows the register capability needs (proposed; record after landing)

All digests measured 2026-10-18T18:05:08Z (`sha256sum`, cwd = lane root). Column
schema is the `MANIFEST.tsv` schema:
`gate  gate_sha256  input  input_sha256  exit_code  finding_count  output  output_sha256  input_snapshot  command`.

### 2.1 Rows that exist today and are replayable

| # | gate | gate_sha256 | input | input_sha256 | exit | count | output_sha256 |
|---|---|---|---:|---:|---:|---|
| R26-1 | `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | **1** | **14** | `0c613c9d973f3c32bb20f4db7a43a02da7a5edcaa1bc3382531acce21e2a89f7` |
| R26-2 | `tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` | `examples/culture-d4/typed-labels.d4.yml` | `60b526b0b3d07141875d20c472451cdf6658f61936d39fe18af4f3d981981092` | 0 | 0 | `1c8add321259a9f026d6e37b0dbd95b0f548f31fe0a10c56098911c21532a6fe` |
| R26-3 | `tools/gates/d4-assembly-check-gate.py` | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` | `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | 0 | 0 | `c60820a54742ecaa1edef972c6c94cce3f88313fbace8ef19eaeddd9a42572a7` |
| **R26-4** | `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` | `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | 0 | 12 | `5b67905b67ca8b67b9ea3fcf6d6eb320c82389307cd3f0a7e9b820f6d8b7a711` |
| **R26-5** | `tools/gates/argot-derivation-gate.py` | `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211` | `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | **0** | 0 | `9412621f5473f8611ae4a2e3e93ddfb9566c24be23c1af1bd21d65a31bdf4859` |

Measured verdicts (this seat, 2026-10-18T18:02–18:06Z, `TMPDIR=$PWD/.scratch`):

| row | command | exit | findings | notes |
|---|---|---|---:|---|
| R26-1 | `python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` | 1 | 14 | 7 `NAME-NEAR` REVIEW + 6 `PHON-INVENTORY` FAIL on the six garment glosses + 1 `CROSS-HOLD` HOLD. **A reproduced red verdict stays red**; recording it is the contract. Re-run twice, byte-stable |
| R26-2 | `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` | 0 | 0 | green; `--selftest` **163/163** |
| R26-3 | `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | 0 | 0 | green. **Not selftest-capable**: `--selftest` is read as an input path → `assembly error: [Errno 2] No such file or directory: '--selftest'`, exit 2. The row must carry no selftest claim for this gate |
| R26-4 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | 12 | **20/20 legs incl. `L3b-argot`**; the 12 findings equal `examples/culture-d4/expected-holds.json` (`3826ba68…`, counts 12/0/0). `--selftest` 19/19 |
| R26-4b | `… examples/culture-d4/packet.d4.typed.yml` | 0 | 12 | **17/17 legs**; output sha256 `f326de09de02ef3b1045751c3730e3178e2f367e2498087a11e3c9072ef3ddee`. A second row, not a variant of R26-4 |
| **R26-5** | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | **0** | 0 | coverage line: `records=156 register_scoped=6 derived_pairs=0 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0`. `--selftest` **21/21**. Flagless and single-input by design, so no adapter is needed |
| R26-5b | `… examples/culture-d4/packet.d4.typed.yml` | 0 | 0 | coverage `records=180 register_scoped=6 derived_pairs=0 …`; output sha256 `4eb67d62a2f5fe1d453c147f2fd44e6a54eae4b0eacf8c06feea324e801b305b` |
| R26-5c | `… tools/gates/fixtures/argot-derivation-gate.yml` | 1 | 5 | the planted set: 4 `D4L-ARGOT-DERIV` + 1 `D4L-ARGOT-RULE`, exactly `tools/gates/fixtures/argot-derivation-gate.expected`; output sha256 `556d31d6f66715cbcb0c8dc7d5820e0be60b62fae39e304a79537dad06c205a6` |

**R26-5 is the argot row, and it must carry its own honest scope.** The gate's
docstring states it and this row repeats it: exit 0 means "every register-scoped
form that states its inputs re-derives", **not** that the stratum is complete.
On D4 it reads `derived_pairs=0`, so the row records a **landed mechanism with
no domain**. A recording seat that cites R26-5 as a register-stratum capability
without that clause would be making the round-25 F-5 vacuity error.

**R26-1's red is the row's content, not its failure.** The 14 findings are the
delivered packet's real state: the six `PHON-INVENTORY` FAILs name the six
garment *glosses* (`'forge apron (thick hide; spark and slag protection)'` etc.)
being read on the sound channel — which is exactly the label-typing class the
`d4-typed-labels` row (R26-2) and the typed pipeline (R26-4) route off-channel.
The differential between R26-1's 14 and R26-4's 12 is the routing working.

### 2.1b **THE GENERATION LANDED** — `tools/gates/frozen/round-26/gate-input/` (measured 18:09:01Z)

This seat's §5 predicted the cascade's correct response would be a new
generation. **It landed while this file was being written**, at
`freeze-receipt.json` `frozen_at: 2026-10-18T18:08:08.652644+00:00`, and it is
green:

```sh
TMPDIR=/var/tmp/kotodama-r26 python3 tools/replay-frozen.py \
  tools/gates/frozen/round-26/gate-input/MANIFEST.tsv
# REPLAY OK: 6/6 rows reproduced the recorded verdicts
#   (reproduction only: a reproduced red verdict stays red)
```

`freeze-receipt.json` (schema `kotodama-r26-gate-input-freeze-v1`, 6 rows,
`frozen_by: round-26 D17..D20 gate+tests seats`) pins
`tools/gates/typed-pipeline-gate.py` at `b749ad07…` and carries an explicit
`supersedes` block naming `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv`
with the reason: "the round-25 generation pins a gate revision that is not on
disk; every row refuses `gate_digest_mismatch` before a gate runs. **A re-pin is
a new generation, never an edit.**"

**The generation's rows and this file's §2.1 agree exactly** — which is the
check that matters, because §2.1 was written before the generation landed:

| generation row | gate_sha256 | input | exit | count | output_sha256 | matches §2.1? |
|---|---|---:|---:|---:|---|---|
| d4 source | `b749ad07…` | `examples/culture-d4/packet.d4.yml` | 0 | 12 | `5b67905b67ca8b67b9ea3fcf6d6eb320c82389307cd3f0a7e9b820f6d8b7a711` | **yes — R26-4** |
| d4 typed | `b749ad07…` | `examples/culture-d4/packet.d4.typed.yml` | 0 | 12 | `f326de09de02ef3b1045751c3730e3178e2f367e2498087a11e3c9072ef3ddee` | **yes — R26-4b** |
| d2 source | `b749ad07…` | `examples/culture-d2/packet.d2.yml` | 0 | 15 | `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b` | new (not in §2.1) |
| d2 typed | `b749ad07…` | `examples/culture-d2/packet.d2.typed.yml` | 0 | 15 | `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606` | new (not in §2.1) |
| control `typed-without-source.yml` | `b749ad07…` | the control fixture | **2** | 0 | `b8bfefa9e0ba86d3e3f16ef37925e09af73509bbbb1d0c1e0903d2e9fbb2a923` | new fail-closed control |
| control `typed-stale-source.yml` | `b749ad07…` | the control fixture | **2** | 0 | `a2ce68d6bf3f582f0e4f9dbdbb4cdbeffecf6efeefe0c80c5b428c5b2a4e9709` | new fail-closed control |

The D4 output digests are **byte-identical** to this seat's independent
measurements (§2.1 R26-4/R26-4b), from a different working directory and a
different stamp. Two rows (R26-4, R26-4b) are therefore confirmed by two
independent runs, and the generation adds the two D2 rows and the two
fail-closed controls this file did not measure. **The two control rows are
exit 2** — the fail-closed behaviour, not a defect: a typed packet whose declared
source is absent or stale is refused rather than graded.

**Consequence for §5.** The cascade is **dispositioned, not merely named**: the
round-25 generation remains red by design (re-measured at 18:09:01Z: 6/6
`could-not-evaluate`, `gate_digest_mismatch`) and its successor is on disk and
green. The four older generations (`round-18/repin-d2`, `round-20/repin-d2`,
`round-22/d4-repin`, `round-23/repin-d2`) each still refuse **one** row for the
same reason and are **not** superseded by this generation, because it pins only
the typed-pipeline gate — their other rows reproduce. A successor seat that
wants those four back to full reproduction can restore the predecessor blob
(`git show f74fc94:tools/gates/typed-pipeline-gate.py`), which the round-25
`freeze.txt` names.

### 2.2 The register rows a successor round records **after** the stratum lands

These rows cannot be measured today because the domain is empty. They are
specified so the successor seat records rather than re-derives.

| # | gate | input | what it will read | landing gate |
|---|---|---|---|---|
| R26-6 | `tools/gates/argot-derivation-gate.py` | the register-bearing D4 packet | `derived_pairs > 0`, `violations=0`, `rule_holds=0` | **`derived_pairs > 0`** — the exact condition `reports/round-26/scribe/capability-row.md` §3.1 names |
| R26-7 | `tools/gates/typed-pipeline-gate.py` | the same packet | `L3b-argot` green **and** the hold set updated with a named `D4L-REGISTER-UNRESOLVED` (or the design's emitted id) row | the hold-set file re-pinned; a hold-set change is a **new** expected file, never an in-place edit |
| R26-8 | `tools/gates/d4-typed-labels-check-gate.py` | the regenerated `typed-labels.d4.yml` | `labels_by_kind` carrying a register-scoped kind, or an explicit statement that the projection does not model register scopes | the projector's own dispatch — this seat measured the delivered projection carries **no** register-scoped kind (74 labels = 56 `native-form` + 12 `translated-label` + 6 `borrowed-strata`) |

**Control the successor row needs, and this seat measured it available.** The
register relation replays and can fail on a **D4** packet — not only on the
fixture. Three correct register pairs injected into the real packet:

| control | mutation | exit | coverage |
|---|---|---|---|
| baseline | none | 0 | `records=156 register_scoped=6 derived_pairs=0 … violations=0` |
| **CTL-A** | 3 correct register pairs added | **0** | `records=159 register_scoped=9 derived_pairs=3 … violations=0` |
| **CTL-B** | `nim` → `min2` | **1** | `violations=1`; `FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form Q-02 'min2' (register 'quote'): declared chain 'reverse' applied to 'min' yields 'nim' …` |
| **CTL-C** | `derivation: ARGOT-NOSUCH` | **1** | `rule_holds=1`; `FINDING D4L-ARGOT-RULE: HOLD — … 'ARGOT-NOSUCH' is neither a declared argot operation (head2, reverse) nor a licensed packet rule (CX-01, CX-02, CX-03) …` |

Scratch fixtures: `.scratch/r26d/ctl/reg-{ok,bad,rule}.yml`, built by copying
`examples/culture-d4/packet.d4.yml` and injecting at the head of the `lexicon`
block; the delivered tree was untouched. The full detail is
`reports/round-26/scribe/capability-row.md` §5.

## 3. Generation inventory (re-replayed 2026-10-18T18:02:14Z)

```
find tools/gates/frozen -name MANIFEST.tsv | sort
```

| generation | rows | replay at 18:02:14Z | reason | notes |
|---|---:|---|---|---|
| `round-3/MANIFEST.tsv` | 7 | **could-not-evaluate 7/7** | `gate_digest_mismatch` | pins the gate bytes at `291c714`; the live tree is not that revision |
| `round-3/attempt-1/MANIFEST.tsv` | 7 | **could-not-evaluate 7/7** | `gate_digest_mismatch` | same class |
| `round-11/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | one row pinned `provenance-audit.py` at a superseded revision |
| `round-18/MANIFEST.tsv` | 2 | **mismatch 1, reproduced 1/2** | `replay_mismatch` | row 2 is the **superseded projection pin** — §3b |
| `round-18/repin-d2/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | row 2 pins `typed-pipeline-gate.py`; the gate moved |
| `round-20/repin-d2/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | same row class |
| `round-22/d4-repin/MANIFEST.tsv` | 3 | **could-not-evaluate 1, reproduced 2/3** | `gate_digest_mismatch` | row 3 pins `typed-pipeline-gate.py` at `04ad4bb4…` |
| `round-23/repin-d2/MANIFEST.tsv` | 11 | **could-not-evaluate 1, reproduced 10/11** | `gate_digest_mismatch` | same row class |
| `round-25/gate-input/MANIFEST.tsv` | 6 | **could-not-evaluate 6/6** | `gate_digest_mismatch` | every row pins `typed-pipeline-gate.py` at `879d40bf…` and the live gate is `b749ad07…`; **superseded by §2.1b's new generation**, re-measured red at 18:09:01Z |
| `round-26/gate-input/MANIFEST.tsv` | 6 | **REPLAY OK 6/6** | — | **the new generation (§2.1b)**, landed 18:08:08Z, pins `b749ad07…`; `freeze-receipt.json` carries the `supersedes` block |

Replay command (run by this seat; `TMPDIR` **outside** the repo):

```sh
mkdir -p /var/tmp/kotodama-r26
for m in round-3 round-3/attempt-1 round-11 round-18 round-18/repin-d2 \
         round-20/repin-d2 round-22/d4-repin round-23/repin-d2 round-25/gate-input \
         round-26/gate-input; do
  printf "%-24s " "$m"
  TMPDIR=/var/tmp/kotodama-r26 python3 tools/replay-frozen.py \
    "tools/gates/frozen/$m/MANIFEST.tsv" | tail -1
done
```

### 3a. The `TMPDIR` control (a row recorded with the wrong one is refused)

```sh
export TMPDIR=$PWD/.scratch        # inside the repo
python3 tools/replay-frozen.py tools/gates/frozen/round-25/gate-input/MANIFEST.tsv
# every row reads mirror_unsafe, exit 2
```

So a recording seat that runs the replay from the lane's usual scratch shape
sees a refusal rather than a verdict. **This is the designed behaviour**
(`tools/replay-frozen.py:177`), and it is the reason §3's command uses
`/var/tmp/kotodama-r26`. A row's own `freeze.txt` states the same requirement in
its own words ("temp mirror root must sit outside this repository; in-repo
TMPDIR is refused as `mirror_unsafe`").

### 3b. `round-18/MANIFEST.tsv` row 2 is a superseded pin, not drift

Measured `--json` at 18:02:14Z:

```json
{"line": 2, "gate": "tools/gates/d4-typed-labels-check-gate.py",
 "recorded_gate_sha256": "05f99629…", "recorded_input_sha256": "a59990bb…",
 "recorded_exit": 0, "observed_exit": 1,
 "observed_output_sha256": "e3b0c442…", "status": "mismatch",
 "reason": "replay_mismatch",
 "stderr_excerpt": "examples/culture-d4/typed-labels.d4.yml differs from the deterministic projection\n"}
```

The attribution matters and is measured, not assumed:

- The **gate digest verifies** (`05f99629…` = the live
  `tools/gates/d4-typed-labels-check-gate.py`), so the reason is
  `replay_mismatch`, **not** `gate_digest_mismatch`.
- The **input snapshot verifies** against its own pin
  (`tools/gates/frozen/round-18/inputs/examples/culture-d4/typed-labels.d4.yml`
  = `a59990bb…`), so **no** `snapshot_tampered`.
- The gate launched and exited 1 saying the snapshot differs from the
  deterministic projection. The live projection is `60b526b0…` — the
  round-22 family-clean build.

So the row is honest and its pins are intact; what changed is the projector's
output, and the successor was correctly recorded as a **new row** in a new
generation (`tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv`). This is the
supersession discipline working as designed, and it is named here because the
round-18 generation reads **1 mismatch** on a live run — a future reader must not
mistake it for a fresh defect. The disposition (leave it historical under a named
revision, or annotate the generation README) is the parent's; this seat does not
edit a filed row.

## 4. The two round-26 pin tails, measured (new rows only)

The round-25 closeout named "two sibling pin tails (stale v2 successor pin;
stale v3 packet-baseline pin in the r4 checker)". Both reproduce, and **a third
appeared** this round.

### 4a. Tail 1 — the v2 successor pin (**closed by the O lane, 17/17 controls**)

**The tail is closed by a new row, and the row is on disk.**
`reports/round-26/remainders/v2-successor-r26/expected.json` (4435 B, 70 lines,
sha256 `f695b910699ab5310b0853fe38471b7714616973f7deff366e1298888b766bc3`,
mtime 18:04:35Z) is the successor capture, and
`reports/round-26/remainders/pin-repoint-receipt.json` (4722 B, sha256
`ffe8269d…`, `date: 2026-10-18T18:08:57.472923+00:00`) records the re-point with
**17/17 controls passed**:

```json
{"tale": "A",
 "surface": "reports/round-20/wart/expected-v2-07-r20.json",
 "stale_pin": "76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb",
 "live_pin": "2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3",
 "replayer": "reports/round-15/handoff/frozen-verify.py",
 "control": {"code": "V2F-DIGEST", "exit": 2},
 "fix": {"exit": 0}}
```

So the stale row **replays red** (`V2F-DIGEST`, exit 2, "1 pinned file(s)
changed since the freeze: `tools/d2-typed-labels.py`") and the new row **replays
green** (exit 0) — the pair of controls the freeze discipline requires, and a
named control rather than an assertion. Measured 18:05:08Z: the live
`tools/d2-typed-labels.py` is **still** `2819f687…`, equal to the round-23 pin and
to the new row's pin, so the round-26 row is a **re-witness** as well as a
re-point — and the receipt's own limit says it plainly: "A pin is integrity,
never truth and never clearance; re-pointing a pin asserts the bytes moved, not
that the move was correct."

### 4b. Tail 2 — the v3 packet-baseline pin (**closed by the O lane, 17/17 controls**)

**Reproduces as a deliberate tail, and it too is now re-pointed.** The r4
checker (`reports/round-25/v3-supersession/v3-supersession-check.py:56-57`)
carries

```python
OLD_BASELINE = "reports/round-23/wording/declared-in-r3/expected.json"
OLD_PACKET   = "reports/round-23/wording/declared-in-r3/packet.md"
OPEN_TAIL_V3_PIN = ("claim D: v3 baseline reports/round-20/handoff/expected.json "
                    "pins packet")
CLAIM_D_LEGACY_V3_PIN = ("claim D: v3 baseline "
                         f"{REVISION_BASELINE} pins packet")
```

and its own `freeze.txt` records the tail as **declared and owned elsewhere**:
"remaining failures are exactly the declared open tails inherited from the
round-23 successor check (v2 successor row projector re-pin; v3 baseline pin
re-point), both owned by other seats". The round-26 receipt's tale **B** is that
re-point:

```json
{"surface": "reports/round-20/handoff/expected.json",
 "stale_pin": "e92f5e6775b657c24fa6260e340e4e7a04cf6c3777188cba80678bed079ae43b",
 "live_pin": "a97a0f0a0a497cb4410124607065df7686bbc7f78b4b46bdaaaa1d66ba4d1b6e",
 "replayer": "tools/exercise-handoff-e2e.py --profile v3",
 "control": {"code": "E2E-DIGEST", "exit": 1},
 "fix": {"exit": 0}}
```

Measured 18:05:17Z — the pin chain, all three revisions live and resolving:

| revision | `packet.md` sha256 | resolves | has `twin.json` |
|---|---|---|---|
| `reports/round-22/handoff/declared-in-r2` | `a97a0f0a0a497cb4410124607065df7686bbc7f78b4b46bdaaaa1d66ba4d1b6e` | yes | **yes** |
| `reports/round-23/wording/declared-in-r3` | `084dc5db9a8d923bb06a987b0b437bf5bfee3caac2e41cd16743da0c71499250` | yes | **no** |
| `reports/round-25/v3-supersession/declared-in-r4` | `5f58db4a52b688568eac054b1c75e9bd110843370a1943cf4353fff75b46aa03` | yes | **no** (re-checked 18:09Z) |

And the tail itself, measured: `tools/exercise-handoff-e2e.py:1933-1934` still
resolves

```python
V3_BASELINE_DEFAULT = "reports/round-22/handoff/declared-in-r2/expected.json"
V3_FROZEN_DIR_DEFAULT = "reports/round-22/handoff/declared-in-r2"
```

so **the validator still reads r2, not r4** — the "filed is not wired" finding
the round-25 lesson recorded, unchanged at this stamp. **The round-26 O lane
landed the wiring row**: `reports/round-26/remainders/v3-baseline-r26/` (mtime
18:04:39Z) carries `packet.md` (`a97a0f0a…`, byte-equal to r2's packet),
`expected.json` (`4879e7602efcbc57f134b0e1604d38ca54d837bcbf8407d1667ef9bf30e238b7`),
`twin.json` (`d3de56a8…`), `freeze.txt` (`adad86ab…`) and `run.log`
(`ba68aee7…`), and its `freeze.txt` reads "frozen: 2026-10-18 by
`tools/exercise-handoff-e2e.py --profile v3`". **The successor seat re-points the
default at this new row** — the file on disk is the row, not the wiring; the
`V3_BASELINE_DEFAULT` constant is a `tools/` byte and this seat writes none.

**A third tail is closed by the same receipt.** Its controls include
`control-stale-v3-row-replays-red` (exit 1, `E2E-DIGEST`, naming the four
read-set files that changed) and `new-v3-row-replays-green` (exit 0). So both
tails carry the required red/green control pair, and the receipt's own limit
records the discipline that protects the filed rounds: "The re-pointed rows land
under `reports/round-26/`; the filed round-20 rows stay byte-identical and were
not edited."

### 4c. The r4 twin gap — **NOT closed** (the O claim's other branch)

The round-25 remainders also named the **r4 twin gap**: the revision landed
packet-only. **Measured 18:09:01Z: `reports/round-25/v3-supersession/declared-in-r4/`
still holds `expected.json`, `freeze.txt`, `packet.md` and no `twin.json`.**
The round-26 O lane addressed it on the **other permitted branch** — the new
`reports/round-26/remainders/v3-baseline-r26/` row carries a `twin.json`
(`d3de56a8…`), which is the "new row" branch rather than an edit of the filed r4
directory. Whether that satisfies the claim's wording ("the r4 twin generated +
frozen, **or** the twin omission documented as a convention with a control") is
the parent's reading; this seat measures only that (a) the r4 directory is
unchanged and (b) a round-26 row with a twin exists.

### 4d. Tail 3 — `typed-pipelines.json`'s `d4` profile pin (named; not re-pointed)

Named because it is the same class and it moved this round.
`tools/gates/typed-pipelines.json` (`396f4678…`) pins `typed-pipeline-gate.py` at
`879d40bf…`; the live gate is `b749ad07…`. **Measured, and the behaviour is
correct:** the D4 source run prints `ok L1-profile` and exits 0 at 20/20, because
the profile pin is checked against the profile's own declared targets, so the pin
is stale as a *record*, not as a *gate*. The row that closes it is a re-pin with
a command and a date, per the file's own note ("a stale pin refuses (exit 2,
`L1-profile`) until it is re-pinned with a command and a date").

## 5. The cascade, and the correct response

**One wave edit turned five generations red at once.** `typed-pipeline-gate.py`
moved between round 25 and the round-26 declared baseline
(`879d40bf…` → `b749ad07…`), and every generation that pins that gate in any row
now reads `gate_digest_mismatch` for that row: `round-18/repin-d2`,
`round-20/repin-d2`, `round-22/d4-repin`, `round-23/repin-d2` and
`round-25/gate-input`. Measured per-generation, each refuses **exactly one** row
(the typed-pipeline row) except `round-25/gate-input`, where **all six** rows pin
that gate and all six refuse.

This is the designed fail-closed behaviour ("a later edit to that gate turns the
row red by design — a re-freeze is a new recording, never an in-place edit"), and
the correct response is a **new generation** recording the settled revision.
**That generation landed at 18:08:08Z and replays 6/6 OK (§2.1b)**; the rows
R26-4/R26-4b in §2.1 are its typed-pipeline rows, and its output digests are
byte-identical to this seat's independent measurements. **No historical manifest
is edited by this seat**, and the `round-25/gate-input` generation is not
defective — it was green 6/6 when it was recorded; it is red now because the
pinned gate moved, and its successor is on disk with an explicit `supersedes`
block naming it. The round-25 `freeze.txt` states the same cascade in advance and
even names the restore command:

```
cascade: this re-pin moves the gate digest, so every earlier generation that pinned the
predecessor now refuses its typed-pipeline row with gate_digest_mismatch … Restoring the
predecessor blob (git show f74fc94:tools/gates/typed-pipeline-gate.py) returns those
manifests to full reproduction; no historical manifest is edited here.
```

## 6. Freeze rules a recording seat must honour (binding)

1. **New generation, new rows.** `tools/gates/frozen/round-26/` is a new
   directory; no earlier `MANIFEST.tsv`, `expected.json` or receipt is edited.
   Precedent: `round-18/`, `round-20/`, `round-22/`, `round-23/`, `round-25/`.
2. **A freeze receipt that is not a battery baseline is not named
   `expected.json` under a battery root.** The `tools/gates/expected/` tree
   carries four battery baselines (`costume-era-consistency-gate`,
   `d4-assembly-check-gate`, `d4-typed-labels-check-gate`, `phonology-sanity-gate`)
   plus `r19-pre`; a receipt landing under a name the battery discovers as a
   baseline fails the standing battery closed. Use `freeze.txt` +
   `freeze-receipt.json`, the round-22/round-25 shape.
3. **`TMPDIR` outside the repo, always.** §3a.
4. **A row the gate cannot prove does not enter the file.** `d4-assembly-check-gate.py`
   has no `--selftest` (§2.1 R26-3), so its row carries no selftest claim.
5. **A red verdict reproduces as red.** R26-1 is exit 1 / 14 findings; the
   recording seat must not "clean" it. `tools/gates/frozen/round-18/README.md`:
   "expected red remains red".
6. **A hold-set change is a new expected file, never an in-place edit.** R26-7
   will change the D4 hold set when the register stratum lands; that is a new
   `expected-holds.json` with `supersedes_pins`, the round-22 pattern
   (`examples/culture-d4/expected-holds.json` carries exactly that block today).

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
sha256sum tools/gates/*.py examples/culture-d4/*.yml examples/culture-d4/*.json
find tools/gates/frozen -name MANIFEST.tsv | sort
mkdir -p /var/tmp/kotodama-r26
TMPDIR=/var/tmp/kotodama-r26 python3 tools/replay-frozen.py --json \
  tools/gates/frozen/round-25/gate-input/MANIFEST.tsv | tail -1
TMPDIR=/var/tmp/kotodama-r26 python3 tools/replay-frozen.py --json \
  tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv | tail -1
grep -rn "V3_BASELINE_DEFAULT" tools/exercise-handoff-e2e.py
ls reports/round-26/remainders/v2-successor-r26/ reports/round-26/remainders/v3-baseline-r26/
grep -rn "registers:\|doublets:\|doublet_of\|#plain\|#quote" examples/ tools/   # 0 — stratum absent
python3 tools/gates/argot-derivation-gate.py --selftest 2>&1 | tail -1        # 21/21
python3 tools/gates/typed-pipeline-gate.py --selftest 2>&1 | tail -1          # 19/19
```

## 8. Limits

- The register rows in §2.2 are **prospective**: the stratum is not on disk
  (§1, and `reports/round-26/scribe/capability-row.md` §0/§4). §2.1's rows are
  measured today and are the rows the round-26 generation can record.
- Every reading binds to the digest and stamp beside it. `typed-pipeline-gate.py`
  and `argot-derivation-gate.py` both moved between round 25 and this seat's
  measurements; a successor must re-hash before quoting any digest here.
- The `round-26/remainders/` files are the **O lane's** artifacts, cited here as
  measured bytes. This seat did not write them and does not certify them.
- A freeze pins bytes and verdicts, never design quality, scholarship, lore
  standing or promotion. This file admits nothing.
