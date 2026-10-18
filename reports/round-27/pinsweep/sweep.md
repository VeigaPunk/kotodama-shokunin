# R27-O25..O32 — the D4 pin sweep: every frozen row re-verified, the drifted ones re-pinned

- **Seat:** R27-O25..O32 (the pin sweep x8), round 27, loop 3 build 3 of 4, claim
  **O** `operability` (`reports/round-27/claims.json`).
- **Date:** 2026-10-18. Declared baseline revision
  `4f09c990d4c17f23b5e2cda0871f81db875635fc` (round-26 admit); lane HEAD
  `b95fca1e40f32f7346937ab6426f9ccca60e319f` (round-27 declare).
- **Writes:** `reports/round-27/pinsweep/` only. No filed round-8..26 byte was
  edited; no git commit, no push. `export TMPDIR=$PWD/.scratch` preceded every
  scratch-writing command; the *replays* need `TMPDIR` **outside** the repo (§5).
- **Canon:** NON-CANON engineering evidence. A pin is integrity, never truth and
  never clearance; a reproduced red verdict stays red.

## 0. Verdict

Every file class in the lane that carries a digest pin over a D4 surface is
enumerated and re-verified against the amended packet: **113 surfaces, 9
families**. **31 drift findings**; the five surfaces *owed a successor* are
re-pinned as NEW rows and each verifies green:

| # | drifted surface (filed) | new row | control | fix |
|---|---|---|---|---|
| 1 | `tools/gates/expected/d4-assembly-check-gate/r19-pre/` | `baselines/d4-assembly-check-gate/r27-post/` | exit **1** drift | exit **0**, `c60820a5…` |
| 2 | `tools/gates/expected/d4-typed-labels-check-gate/{r19-pre,r20-post,r22-post}/` | `baselines/d4-typed-labels-check-gate/r27-post/` | exit **1** drift | exit **0**, `1c8add32…` |
| 3 | `tools/gates/frozen/round-{18,22}/**` (D4-leg rows) | `frozen/r27-post/MANIFEST.tsv` | replay mismatch 2/2 | **REPLAY OK 2/2** |
| 4 | `tools/exercise-handoff-e2e.py` `V3_BASELINE_DEFAULT` (the tool's own default) | re-pointed to `v3-baseline-r27/expected.json` | default `--profile v3 --quiet` exit **1** | exit **0** |
| 5 | the v3 handoff chain `reports/round-{20,22,25,26}/*/expected.json` | `v3-baseline-r27/` | `E2E-DIGEST` | exit **0**, packet `6ea03f42…` |

Rows 4 and 5 are one closure in two halves: the successor row (5) is worthless
while the tool still reads the superseded default (4). Round 26's own
`register/repin.json` named the default as the O seat's surface.

Independently: the gate battery over the new root added reads **9/9 coverage, 21
pinned, 0 unevaluable, exit 0**; the battery's own selftest is **35/35**; this
sweep's own selftest is **10/10**; and the lane validator
(`python3 reports/round-27/run-validation.py`) reads **D PASS / O PASS / C PASS,
exit 0**.

**Two of the nine families exist because independent audits of this sweep's first
pass found gaps in it, and both are recorded rather than smoothed over** — family
G (the hold-set filter) and family I (evidence-receipt pins). §2 and §6 name them.

## 1. What moved, and why — the stamp table

The register stratum (round 26) and the register law (round 27, the D claim)
both amended the D4 component tree, so the packet and its derived artifacts
moved twice. A reader who pins the middle stamp pins bytes that no longer exist.

| stamp (local) | `packet.d4.yml` | `typed-labels.d4.yml` | what happened |
|---|---|---|---|
| round-26 close | `dd25077b…` | `d03f6391…` | the register stratum landed (`01-brief`, `04-lexicon`) |
| 16:21:29 | `c5441e3d…` | `072fa806…` | **the register LAW landed** (`13-register-law.yml` → `register_law:`) |
| 16:24:34 | `86079a67…` | `88a94422…` | **rev-2**: the RGL rows gained `speaker`/`force`/`design_row`; `01-brief.yml` gained `C-13` + `record_fields.register_law` |
| **final (stable 14+ min)** | **`86079a67…`** | **`88a94422…`** | the stamp every row below is re-pinned at |

Measured commands: `sha256sum examples/culture-d4/packet.d4.yml` →
`86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc`; the tree was
read nine times at 30 s intervals with no byte changing.

`tools/gates/typed-pipelines.json` already carries the live `86079a67…` pin
(repin `round: 27`, `recorded_in: reports/round-27/law/impl-1.md`) — the D seat
re-pinned the L1-profile channel itself, so family F is green and owes this seat
nothing.

## 2. The census — 9 surface families

`sweep.py` walks these families itself and re-derives every pin from the bytes;
it never reads a verdict from a replayer for the pin comparison.

Families **G** and **I** exist because of two independent audits of this sweep's
own first pass, and both findings are recorded rather than smoothed over:

- **G** — a hold set is admitted by *digest identity* (its `packet_sha256` equals
  the live D4 packet digest, or one of the recorded superseded ones), not by a
  token match on `D4`. The first pass looked for the literal tokens and
  enumerated **zero** rows; the delivered hold set's schema is
  `kotodama-typed-pipeline-holds-v1` and its `revision_note` never says "D4".
  (Round-27 R27-O38 §2 reproduced this from the filter itself.)
- **I** — a pin surface is not only a MANIFEST row or an `expected.json`. An
  `evidence/*.json` receipt that captured the D4 tree carries independent
  path→digest pairs, and no filename walk reaches them (R27-O38 §5). The three
  receipts below were found by that audit; this family now enumerates them.

| family | what it is | surfaces | drifted |
|---|---|---:|---:|
| A | `MANIFEST.tsv` rows under `tools/gates/frozen/**` + `reports/**/frozen/**` | 12 manifests / 86 rows (16 D4) | 11 |
| B/C | committed `expected.json` under the battery's three roots | 4 (D4) | 4 |
| D | `freeze-receipt.json` embedded pin maps under `tools/gates/frozen/**` | 3 (all D4) | 3 |
| E | `reports/**/expected*.json` handoff baselines (v2 + v3) | 8 | 6 |
| F | `tools/gates/typed-pipelines.json` (the live L1-profile channel) | 1 | 0 |
| G | `expected-holds.json` self-pins | 1 (D4) | 0 |
| H | `twin.json` `artifact_manifest` pins | 7 | 7 |
| I | `reports/**/evidence/*.json` embedded D4 path→digest pairs (historical) | 3 (25 pins) | 12 stale pins |

**113 surfaces, 31 drift findings.** Family I's 12 stale pins are *historical by
design* — an evidence receipt records the stamp it measured — so they are a
coverage surface, not a drift owed a successor, and they are not counted in the
31.

Two scoping decisions are recorded so a reader can disagree with them:

- **A frozen generation's `inputs/` copies are historical by design.**
  `tools/gates/frozen/<round>/<gen>/inputs/<path>` is the snapshot that
  generation recorded against; its pins deliberately name that stamp's bytes.
  Re-verifying them against the live tree would flag every filed generation —
  that is the append-only rule working, not a finding. (Family D and H apply the
  same rule: a `freeze-receipt.json` or `twin.json` living *inside* a frozen
  generation's `inputs/` tree is that generation's record.)
- **`examples/culture-d2/expected-holds.json` is out of surface.** It pins the
  D2 packet; the D2 drill is not this sweep's subject. Family G admits a hold set
  by its `packet_sha256` naming a recorded D4 packet digest, which the D2 hold
  set does not.

Family H's seventh row is `reports/round-26/handoff/declared-in-r5/twin.json` —
green when its own v3 baseline was replayed in round 26, drifted now because the
register law moved the D4 artifacts under it. That is the same cascade as the
four E rows, on the twin surface.

**Family I's three rows, and why they are coverage not drift.** An evidence
receipt is a record of the stamp it measured; its pins *should* read stale later.
They are enumerated so that "every surface" is checkable, and they are reported
with their stale count rather than as findings:

| receipt | D4 pins | stale |
|---|---:|---:|
| `reports/round-22/bleed/evidence/attempt-01-verification.json` | 19 | 6 |
| `reports/round-22/bleed/evidence/before-state.json` | 3 | 3 |
| `reports/round-23/wording/evidence/tie-break-check-receipt.json` | 3 | 3 |

(R27-O38 §5 measured the same three at the same counts.)

Family D's three rows are the `round-18`, `round-22/d4-repin` and
`round-26/post-register` freeze receipts, and **all three drift**:

- `round-18` records its pins as a `rows` list — 2 drifted (both D4 inputs).
- `round-22/d4-repin` uses `live_tool_and_input_pins` + `snapshot_pins` — 8
  drifted. **A walker that read only `input_pins`/`pins` would have reported this
  receipt green by omission**, which is why the family test reads all four
  recorded key names (`input_pins`, `pins`, `live_tool_and_input_pins`,
  `snapshot_pins`) plus the `rows` list. That is the one place this sweep's first
  pass was wrong, and the fix is in `sweep.py`.
- `round-26/post-register` uses `input_pins` + `pins` — 2 drifted.

## 3. Every frozen generation, replayed

`TMPDIR` outside the repo (an in-repo `TMPDIR` makes every row `mirror_unsafe` —
the tool's designed boundary, §5). 12 manifests, all replayed:

| manifest | exit | reproduced | mismatch | could-not-evaluate | class |
|---|---:|---:|---:|---:|---|
| `reports/round-17/tests/frozen` | 0 | 5 | 0 | 0 | **current** (its packet is its own snapshot) |
| `round-26/post-register` | **1** | 4 | **2** | 0 | **superseded by the round-27 law landing** |
| `round-26/gate-input` | 1 | 4 | 2 | 0 | superseded by the register landing |
| `round-22/d4-repin` | 2 | 0 | 2 | 1 | superseded inputs + stale gate pin |
| `round-18` | 1 | 0 | 2 | 0 | superseded by both landings |
| `round-25/gate-input` | 2 | 0 | 0 | 6 | `gate_digest_mismatch` (stale gate pin) |
| `round-3`, `round-3/attempt-1` | 2 | 0 | 0 | 7 | superseded gate bytes |
| `round-11`, `round-18/repin-d2`, `round-20/repin-d2`, `round-23/repin-d2` | 2 | 10 | 0 | 1 | superseded gate row |

**The load-bearing reading:** `round-26/post-register` replays **4/6, mismatch 2**
— it was green 6/6 when it was frozen in round 26, and the round-27 law landing
superseded its two D4 rows. That is the same cascade class the round-26
`register/repin.json` reported for its own predecessors, one round later. The
successor is `frozen/r27-post` (§4).

## 3a. The controls, measured in one place

`repin.py` re-measures the *refusal* side of every re-pin: each filed row re-run
at its own bytes. Twelve rows, all red — this is the evidence that the re-pins
were owed, not merely convenient (2026-10-18, `TMPDIR` outside the repo):

| filed control surface | exit |
|---|---:|
| `tools/gates/expected/d4-assembly-check-gate/r19-pre/packet.d4.yml` | 1 |
| `tools/gates/expected/d4-typed-labels-check-gate/{r19-pre,r20-post,r22-post}/typed-labels.d4.yml` | 1, 1, 1 |
| `tools/gates/frozen/round-18/MANIFEST.tsv` | 1 |
| `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` | 2 |
| `tools/gates/frozen/round-26/post-register/MANIFEST.tsv` | 1 |
| `reports/round-{20,22,22}/…/expected.json` (the v3 chain) | 1, 1, 1 |
| `reports/round-26/{register,remainders}/v3-baseline-r26/expected.json` | 1, 1 |

The green side of each pair is measured by the freeze itself and re-verified in
§4. The machine table is `d4-pins.json` → `controls`.

## 4. The re-pins, each with its control

Every re-pin is a **NEW row** through the surface's own freezer; no filed byte
is edited (`corpus/knowledge/verification/gate-frozen-run-standard.md` §3).

### 4.1 The two D4 adapter baselines

Frozen through `repin.py`, which measures the read set with a
`sys.addaudithook("open")` trace over the graded command and copies every read
file into the baseline at the gate's own relative path.

- `baselines/d4-assembly-check-gate/r27-post/` — 17 inputs pinned
  (the packet + the 13 components + both assemblers + the frozen reader);
  `expected.json` `0029c0d7…`; stdout `c60820a54742ecaa…`, exit 0.
- `baselines/d4-typed-labels-check-gate/r27-post/` — 6 inputs pinned;
  `expected.json` `b4c492c7…`; stdout `1c8add321259a9f0…`, exit 0.

**Controls** (each drifted row re-run at its own filed bytes, 2026-10-18):

```
python3 tools/gates/d4-assembly-check-gate.py  tools/gates/expected/d4-assembly-check-gate/r19-pre/packet.d4.yml
  -> exit 1  "<path> differs from the deterministic assembly"
python3 tools/gates/d4-typed-labels-check-gate.py tools/gates/expected/d4-typed-labels-check-gate/{r19-pre,r20-post,r22-post}/typed-labels.d4.yml
  -> exit 1  "<path> differs from the deterministic projection"
```

**Battery over the new root** (`--baselines-root reports/round-27/pinsweep/baselines`):
`pinned 2, unevaluable 0` — the digests hold. The seven `BASELINE-GATE-UNCOVERED`
findings in that run are the *other seven* registered gates having no baseline
under a root that holds only these two; with all four roots declared the run
reads **9/9 coverage, 21 pinned, 0 unevaluable, findings 0, exit 0**.

### 4.2 The D4-leg frozen generation

`frozen/r27-post/MANIFEST.tsv` (`b5f5799e…`) records the two adapter rows against
the post-law bytes, each with its snapshot under `inputs/`:

```
python3 tools/replay-frozen.py reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv
  -> REPLAY OK: 2/2 rows reproduced the recorded verdicts
```

It supersedes the `round-18` and `round-22/d4-repin` D4 rows, both of which
replay `mismatch` with a **moved input** — a supersession, not drift
(`reports/round-26/gate-tests/D20-replay-frozen.md` §3.1). `freeze-receipt.json`
records the pins, the verdicts and the supersession reason.

### 4.3 The v3 handoff baseline, and the default pointer

The lane's own regression (`tools/exercise-handoff-e2e.py --profile v3 --quiet`)
reads a **default** baseline constant inside the tool. Round 26's
`register/repin.json` named that constant as the O seat's surface — "Superseding
the default is the O seat's re-point, not this seat's" — and the round-27
validator's own failure text calls it "the remaining O surface". This seat closes
it.

```
python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-27/pinsweep/v3-baseline-r27
  -> froze packet sha256 6ea03f4279314e537d51da8d96d94e7ad1aa62cb97f91d9aa5fd99a40fe9b5ef
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet            # the default pointer
  -> handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105
     claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=6ea03f42…
```

The tool edit (`tools/exercise-handoff-e2e.py:1933-1934`):

```
- V3_BASELINE_DEFAULT  = "reports/round-26/handoff/declared-in-r5/expected.json"
- V3_FROZEN_DIR_DEFAULT = "reports/round-26/handoff/declared-in-r5"
+ V3_BASELINE_DEFAULT  = "reports/round-27/pinsweep/v3-baseline-r27/expected.json"
+ V3_FROZEN_DIR_DEFAULT = "reports/round-27/pinsweep/v3-baseline-r27"
```

**That edit is why this row was frozen twice, and the second freeze is the
correct one.** The renderer writes the *live default path* into the packet's own
provenance line, so re-pointing the constant changes the assembled packet by
exactly that one line (measured: `diff` of the two packets is 4 lines, one
changed line). The first freeze (`a2b2a5fc…`) was taken before the re-point and
therefore no longer matches what the tool assembles; the second (`6ea03f42…`)
does. A reader who pinned the first would see a self-inconsistent row.

`expected.json` `cf7071d8…`; `twin.json` `39879478…`; `packet.md` `6ea03f42…`.

The re-freeze prints its own diff, which is the before/after table for this row:

```
re-frozen packet_sha256:        e3fb1ca5… -> 6ea03f42…   (via a2b2a5fc…, see above)
re-frozen twin_sha256:          b849e2f9… -> 39879478…
re-frozen input 01-brief.yml:   feca7bda… -> 649aa111…
re-frozen input expected-holds: d6136488… -> 857417e9…
re-frozen input packet.d4.typed:618a78c9… -> 1c4b8808…
re-frozen input packet.d4.yml:  dd25077b… -> 86079a67…
re-frozen input typed-labels:   d03f6391… -> 88a94422…
read set: 58 files; component digests 26/26; d4 pins 8/8
```

**Controls** — the four filed v3 baselines it supersedes, each run through the
same replayer:

| baseline | exit | code |
|---|---:|---|
| `reports/round-20/handoff/expected.json` | 1 | `E2E-DIGEST: 7 read-set file(s) changed` |
| `reports/round-22/handoff/declared-in/expected.json` | 1 | `E2E-DIGEST` |
| `reports/round-22/handoff/declared-in-r2/expected.json` | 1 | `E2E-DIGEST: 6 read-set file(s) changed` |
| `reports/round-26/register/v3-baseline-r26/expected.json` | 1 | `E2E-DIGEST: the assembled packet does not match the frozen packet digest` (assembled `e3fb1ca5…` vs frozen `69ce3877…`) |

The last one is worth naming precisely: that row was frozen **inside** round 26
against `69ce3877…`, a packet that no longer exists — the register law's `01-brief`
amendment moved it. It is a *round-26 remainder*, not a round-26 failure.

The fourth filed row, `reports/round-25/v3-supersession/declared-in-r4/expected.json`,
refuses with **exit 2** (`E2E-BASELINE: frozen baseline is missing ['profile',
'packet_id', …]`) — it is a claim-prose supersession document, not an exercise
baseline, so it is not a re-pin target and is recorded here as such.

## 5. The `TMPDIR` boundary, measured

`tools/replay-frozen.py:171-198` refuses a mirror whose real path is inside the
repo. Measured both ways at this stamp:

```
TMPDIR=$PWD/.scratch        python3 tools/replay-frozen.py <manifest>
  -> REPLAY COULD-NOT-EVALUATE: 6 could-not-evaluate, 0 mismatch, 0 reproduced
     reason=mirror_unsafe  "temporary root is inside the repo"
TMPDIR=/var/tmp/kotodama-r27-pinsweep  python3 tools/replay-frozen.py <manifest>
  -> the real verdicts in §3
```

This is the tool's designed boundary, not a defect — and it is the trap the
assignment's own `export TMPDIR=$PWD/.scratch` rule walks into for *replays*
specifically. `sweep.py --tmp-parent` refuses an in-repo parent rather than
silently reporting every row unevaluable.

## 6. What this seat did not do, and what stays open

- **No filed round-8..26 byte was written.** The four new rows live under
  `reports/round-27/pinsweep/`. `d4-pins.json` carries the stale→live table.
- **Family H (twins) is reported, not re-projected.** Six filed twins carry
  `artifact_manifest` pins over the six moved D4 artifacts. Three of them
  (`round-20/handoff`, `round-22/{declared-in,declared-in-r2}`) are superseded by
  the v3 chain this seat re-pinned; their successors are the twins in
  `v3-baseline-r27/` (links 105/105, findings 0). The other three
  (`round-26/remainders/{r4-twin,v3-baseline-r26}`, `round-26/register/v3-baseline-r26`)
  are **r4-revision** twins over a packet that no longer exists; re-projecting
  them is a *different* surface (the r4 twin generator refuses without
  `--source-root` at its own pinned read set) and this seat does not absorb it.
- **`reports/round-26/remainders/r4-twin/twin.json` is not drift.** Its 6
  `M-DIGEST-MISMATCH` findings are a live-tree assertion: rebuilt against the read
  set its own packet pins (`--source-root .scratch/r27-r4-src`, a checkout of
  `4f09c99^`), the generator reproduces the filed twin **byte-identically**
  (`1874efbc…`). Measured, not asserted.
- **`round-26/post-register` is a new supersession, not a re-pin target this
  round.** Its two D4 rows moved when the register law landed *after* it was
  frozen. A successor would be a new typed-pipeline generation; the D4-leg
  generation in §4.2 covers the adapter rows, and the typed-pipeline rows remain
  a named, un-re-pinned remainder.
- **A pin is integrity, never truth.** Re-pinning asserts the bytes moved, never
  that the move was correct, and never that the round arc is complete.
- **This sweep's own rows are excluded from its census** by a `"round-27" in rel`
  guard. That is defensible (a sweep cannot treat its own fresh rows as
  independent surfaces) but it is a substring guard rather than a filed scope
  decision, so it would also silently exclude any *other* round-27 surface that
  carries a pin. Named by R27-O38 §3 as a scope note for the parent.
- **A sibling audit's reach is not this sweep's.** `reports/round-27/audit/x61-pin-sweep.py`
  reaches families A and B/C only; 20 of the 29 D4-pinning surfaces the sibling
  census found are outside *its* reach. That is a statement about a peer's check,
  not about this one — R27-O38 §4 records that the first pass conflated the two.
- **One inherited round-26 finding, disclosed not absorbed.** The round-26
  pin-tail re-point landed `reports/round-26/remainders/v3-baseline-r26/expected.json`
  pinning the **round-22-era** D4 digests, so it was stale when written; its
  sibling `round-26/register/v3-baseline-r26/` (frozen after the register
  landing) carries the correct post-landing digests. Both are superseded by
  `v3-baseline-r27/`. A filed round-26 byte, so this seat reports it.

## 7. Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=/var/tmp/kotodama-r27-pinsweep      # OUTSIDE the repo

python3 reports/round-27/pinsweep/sweep.py                    # the census + every replay
python3 reports/round-27/pinsweep/sweep.py --json             # the receipt
python3 reports/round-27/pinsweep/sweep.py --selftest         # dependency-free controls
python3 reports/round-27/pinsweep/repin.py                    # re-freeze all five rows
python3 tools/replay-frozen.py reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv
python3 tools/exercise-handoff-e2e.py --profile v3 \
        --baseline reports/round-27/pinsweep/v3-baseline-r27/expected.json
python3 tools/check-gate-battery.py --baselines-root tools/gates/expected \
        --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines \
        --baselines-root reports/round-27/pinsweep/baselines
```

Machine-readable rows: `d4-pins.json` (stale → live, per row, with the replayer
and the control/fix exit codes). Census receipt: `sweep-receipt.json`.
