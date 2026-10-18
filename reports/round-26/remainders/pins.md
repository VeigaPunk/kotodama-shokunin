# R26-O33..O36 — the two sibling pin tails, re-pointed as new rows

- **Seat:** O, round-26 claims R26-O33..O36 (the pin tails x4). This seat authored
  none of the lane's filed round 8–25 artifacts.
- **Date:** 2026-10-18. Baseline revision `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`.
- **Writes:** `reports/round-26/remainders/` only — `v2-successor-r26/expected.json`,
  `v3-baseline-r26/{expected.json,packet.md,twin.json,freeze.txt,run.log}`,
  `pin-repoint-check.py`, `pin-repoint-receipt.json`, `pins.json`, this file. No
  git commit or push. No filed round 8–25 artifact touched. Scratch under
  `.scratch/` with `TMPDIR=$PWD/.scratch`.
- **Declared by:** `reports/round-25/audit/x48-v3-supersession.md:148-158`, which
  named them "the stale combined-source v2 successor pin" and "the stale v3
  packet-baseline pin", both **open since round 23** and both left untouched by
  the round-25 r4 claim-prose supersession. Round 25's own `evidence.md:179-180`
  repeats them as its follow-up 2.

## 1. The hazard, measured

Two sibling pins are stale against the live bytes. Both were re-measured at
this stamp, on the bytes, not read from any printed verdict:

| tail | surface (filed, byte-identical) | stale pin | live value |
|---|---|---|---|
| A | `reports/round-20/wart/expected-v2-07-r20.json` (`ad761a61…`) | `inputs["tools/d2-typed-labels.py"]` `76536a92…` | `2819f68769dfc0b5…` |
| B | `reports/round-20/handoff/expected.json` (`e2bfa52a…`) | `packet_sha256` `e92f5e6775b6…` | `a97a0f0a0a49…` |

Commands: `sha256sum tools/d2-typed-labels.py` → `2819f687…`;
`python3 tools/exercise-handoff-e2e.py --profile v3` → `packet_sha256=a97a0f0a0a49…`.
Both on 2026-10-18.

Each stale pin refuses its own replayer, and the refusal is the control:

- **Tail A control** — `python3 reports/round-15/handoff/frozen-verify.py --baseline
  reports/round-20/wart/expected-v2-07-r20.json` → **exit 2**,
  `V2F-DIGEST: 1 pinned file(s) changed since the freeze: tools/d2-typed-labels.py`.
- **Tail B control** — `python3 tools/exercise-handoff-e2e.py --profile v3 --baseline
  reports/round-20/handoff/expected.json` → **exit 1**, `E2E-DIGEST: 4 read-set
  file(s) changed since the baseline was frozen: examples/culture-d4/expected-holds.json,
  examples/culture-d4/packet.d4.typed.yml, examples/culture-d4/typed-labels.d4.yml`.
  Tail B's red is wider than its name suggests: the round-20 v3 baseline pins four
  read-set files that the round-22 family-clean repair and the round-20–22 projector
  work moved, so the packet digest is one symptom of a four-file drift.

## 2. The re-point, and why it is this shape

The filed convention is **re-pins are new rows; corrections are new files** — never
an in-place edit of a filed byte (round-20 lesson; `corpus/lessons/round-18.md`).
Both tails are re-pointed by **re-freezing through the tail's own filed freezer**,
which measures the live bytes and writes a fresh row:

- **A** — `reports/round-15/handoff/frozen-verify.py --freeze --baseline
  reports/round-26/remainders/v2-successor-r26/expected.json` → 28 inputs pinned,
  26 manifest rows, census `{supported: 8, partial: 5, unresolved: 2}`, links 50/50.
  The row differs from its filed predecessor in **exactly two values**: the moved
  input and the derived `baseline_digest` (`44b3c299…` → `803ec02f…`). The
  freezer re-measures every pinned input, so the row cannot silently inherit a
  stale digest.
- **B** — `tools/exercise-handoff-e2e.py --profile v3 --freeze
  reports/round-26/remainders/v3-baseline-r26` → froze packet `a97a0f0a0a49…`,
  twin `d3de56a8be1d…`, 58 read-set files, gate 16/16 + 20/20 + findings 0,
  links 105/105, census 16/7/4, `v2_subset ad35c860…`, alias leg `landed`.

Both freezers refuse to emit a row whose control is red, so the frozen rows are
green by construction, and the replay below proves it independently.

**Replays (the fix), through the same filed replayers that produced the red:**

- A: `frozen-v2: exit=0 fields=16/16 glossary=20/20 findings=0 claims=15/15
  statuses={'supported': 8, 'unresolved': 2, 'partial': 5} links=50/50
  packet_sha256=24f9dd39bdad…` — **exit 0**.
- B: `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105
  claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed
  packet_sha256=a97a0f0a0a49…` — **exit 0**.

## 3. The checker, and the A/B control

`reports/round-26/remainders/pin-repoint-check.py` is the round-26 successor
checker bound to the re-pointed rows. `--check` → **exit 0, 17/17 controls**;
`--selftest` → exit 0, 5/5. It asserts, per tail, the stale row's filed digest,
the live re-measurement, that the new row pins the live value, that the stale row
replays red with its named code, and that the new row replays green; then that
the new rows are the only delta and that **filed rounds 8–25 are byte-unchanged**
across the whole run. Receipt: `pin-repoint-receipt.json`.

The frozen round-20 runner discovers its v2 successor row (`expected-v2-07-*.json`)
and its v3 baseline (`reports/round-20/handoff/expected.json`) **under
`reports/round-20/`** (`run-validation.py:769-787`, `:893-915`), which is filed and
must not be edited. So the re-point cannot be proven by moving the runner's
discovery path. It is proven by an A/B control instead: the frozen runner run
twice in isolated clones at the baseline revision, differing **only** in whether
the re-pointed rows occupy those discovery paths.

| arm | fixture | claim D failures |
|---|---|---|
| red | filed rows at filed paths | the two tails, verbatim |
| green | re-pointed rows at the discovery paths | the contract-audit verdict only |

With the re-pointed rows visible, **both tail failures disappear from claim D**.
The residual green-arm failure — `contract audit re-run verdict is 'fail', not a
semantic PASS or named gaps with owners: reports/round-20/handoff/packet-v3-16.md`
— is a different surface that this seat does not own and does not absorb.

## 4. What this seat did not do

- **No filed round-8–25 byte was edited.** Both stale rows are byte-identical to
  the baseline revision (`ad761a61…`, `e2bfa52a…`), asserted by the checker and by
  the A/B red arm reproducing the same red.
- **No runner, gate, projector, renderer, `SKILL.md` or shared bookkeeping changed.**
  The frozen round-20 runner's discovery path is untouched.
- **The `20/20 != 19/19` gate-legs reading is not this seat's tail.** The round-20
  runner hardcodes an expectation that predates the round-25 `L3b-argot` leg; the
  live D4 gate reads `20/20` (re-measured here: `python3
  tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → exit 0,
  `summary: 20/20 legs passed`) and round 25 already recorded the same reading
  (`reports/round-25/audit/o18-gate-input-adversarial.md:23`). Reported, not absorbed.
- The v3 re-point row lands the **full five-file set** (`packet.md`, `twin.json`,
  `run.log`, `freeze.txt`, `expected.json`). That is the shape a v3 row takes when
  produced by its freezer; the round-25 "packet-only, no twin.json" remainder is a
  different tail owned by another seat, and this row does not claim it.

## 5. Limits and handoff

- A pin is **integrity, not truth**: re-pointing asserts the bytes moved, never
  that the move was correct, and never that the round arc is complete. All rows
  remain NON-CANON.
- The re-point is a **worktree record, not a commit or promotion decision**; the
  parent owns integration. `v3-baseline-r26/run.log` is covered by the repo's
  `*.log` ignore rule and needs a force-add if the parent commits this tree.
- Tail B's four-file drift is the wider fact: the round-20 v3 baseline is stale on
  three culture-d4 surfaces as well as the packet digest. This row pins the live
  bytes; it does not adjudicate which of those moves was correct.
- **For the parent's O-claim integration:** the two rows are machine-readable in
  `pins.json`, each naming its tail, its stale and live values, its replayer, and
  its control/fix exit codes. `pin-repoint-check.py` is the bound checker.
