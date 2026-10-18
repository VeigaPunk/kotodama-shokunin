# R20-O11 — re-pin: the round-18 re-pin-d2 generation, new generation `round-20/repin-d2`

- round: 20 (operator: loop 2 of 3, build round 4 of 4) · shard: **O11..O14**
  (re-pin ×4) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "O R20-O11..O14 (re-pin x4): update the pins that name
  d2-typed-labels.py (round-18 repin-d2 rows, round-16 v2-07 expected.json pins,
  round-9 baselines if pinned) as NEW rows with the before/after table extended;
  replay green; reports/round-20/repin/."
- date: 2026-10-18. Declared `baseline_revision`
  `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`; HEAD at seat start `122086b`. All
  readings stamped UTC; the freeze stamp is `2026-10-18T10:14:25-03:00`
  (= 13:14:25Z).
- canon: NON-CANON engineering evidence. `exit 0` here means "the emitted findings
  equal the frozen expected hold set"; the 15 hold lines are still open design
  debt — a reproduced red verdict stays red.
- writes: **new** `tools/gates/frozen/round-20/repin-d2/**` (MANIFEST.tsv,
  run-receipt-repin.json, freeze.txt, snapshot dir `typed-pipeline/`) and this
  file. The filed round-11 and round-18 generations are opened read-only
  (§5 re-hashes prove it).
- **status: COMPLETE. New manifest replays 11/11, exit 0** (13:14Z and 13:15Z);
  the receipt records the one pin that moved — the projector
  `tools/d2-typed-labels.py 0da0015f… → 76536a92…` — with the D2 verdict bytes
  unchanged.

## 1. What is being re-pinned, and why a new generation

`tools/d2-typed-labels.py` is named by several pin surfaces. The round-18
re-pin receipt records it in `tool_pins` at
`0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`. Round 20's
claim O landed the per-family era-alias resolution, which edits that file:
measured at 13:01:06Z the projector moved to
`76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb`
(`git diff --stat -- tools/d2-typed-labels.py` → `41 insertions(+), 23
deletions(-)`: the declared-reconciliation shaping is extracted into
`shape_reconciliation_rows`, so a packet-declared table is shaped by the same
function as the D2 component leg).

A pin file is not rewritten to match a later revision (append-only), so the
re-pin is a **new generation** at the standard's path, one home on purpose
(`tools/gates/frozen/round-20/repin-d2/`, the path the round-18 generation used
under its own round number):

```text
tools/gates/frozen/round-20/repin-d2/
  MANIFEST.tsv              derived from the round-18 re-pin manifest
  run-receipt-repin.json    schema kotodama-frozen-run-v1; supersedes the round-18 receipt
  freeze.txt                steps, readings, exposure
  typed-pipeline/           the snapshot dir for this generation
    packet.d2.typed.yml     byte copy of the filed round-11 frozen typed packet
    packet.d2.yml           byte copy of the filed round-11 frozen legacy packet
    run.log                 verbatim stdout of the live gate over the frozen copy
```

## 2. Before pins (filed generations, measured 12:56Z and 13:14Z)

| item | value |
|---|---|
| `tools/gates/frozen/round-11/MANIFEST.tsv` | `aad230bfdcc1bfe4cc137339b47daf0154208b6c69225e0c0a4505ce52532063` (11 rows) |
| `tools/gates/frozen/round-11/typed-pipeline/run-receipt.json` | `c49ebc9e71ce870af621604bb0e00886b45ad8f4028777f202ec845ede6cc902`; `tool_pins` projector `0da0015f…` |
| `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` | `2556b084b73c2d03cc9919b179153660f1512641382040f6c4f0fa26316e3e9d` (12 rows; row 1 gate cell `04ad4bb4…`, re-pointed by the round-18 integrator after the round-18 receipt was written) |
| `tools/gates/frozen/round-18/repin-d2/run-receipt-repin.json` | `d90c09e8789bb9dfb303071853a15a28f88ac2a18e3fe3715e8c0cb0b7f7dc03`; `tool_pins` projector `0da0015f…` |
| replay, filed round-11 manifest | 10 reproduced, **1 could-not-evaluate** — row 1 `gate_digest_mismatch` (the round-18 supersession class; the filed row names `d102fd1d…`) |
| replay, filed round-18 manifest | **11/11 reproduced, exit 0** |
| D2 path, pre-change (12:56Z) | selftest 12/12; default `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b`; `--json` `19765ddf2c36a7db5d71bd262079d6164b24f6222d9df83d0cefdeaeb8f47e62`; frozen packet `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606`; projector selftest 39/39 |

## 3. After pins (new generation, frozen 13:14:25Z)

| item | value |
|---|---|
| `MANIFEST.tsv` | `2556b084b73c2d03cc9919b179153660f1512641382040f6c4f0fa26316e3e9d` — **byte-identical to the round-18 manifest**: no gate cell moved, so the derivation substituted nothing (12 rows, row 1 gate `04ad4bb4…`) |
| `run-receipt-repin.json` | `11854da180b2ca5c7abaa8581f8cce7d8e48d087a85b32f39ce2cd2ab1d14528` |
| receipt `supersedes` | `tools/gates/frozen/round-18/repin-d2/run-receipt-repin.json` (sha `d90c09e8…`) |
| receipt `tool_pins` | projector **`76536a92…`**, `tools/assemble-d2-typed.py c7e5a749…`, `tools/assemble-d2.py 8ea6bdde…` |
| receipt `tool_pins_moved_from_round18` | `["tools/d2-typed-labels.py"]` (adapter and serializer byte-equal) |
| `gate_sha256_before / at_freeze / after_run` | `04ad4bb4… / 04ad4bb4… / 04ad4bb4…` — `gate_bytes_stable_across_run: true` |
| snapshot `typed-pipeline/` | `packet.d2.typed.yml 1b5010b7…` (= the filed round-11 snapshot pin), `packet.d2.yml e0f21509…`, `run.log 9a69985a…` |
| graded run | exit 0, 15 `FINDING` lines, 1 `NOTE` line, **stderr 0 bytes**, stdout `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606` — `stdout_bytes_equal_to_round11: true` |
| `freeze.txt` | `936a2b86861b16ec572de92d7d51612e653303acde3fde9fff259dd215689b7c` |
| replay (new manifest) | `TMPDIR=/var/tmp/kotadama-r20-repin python3 tools/replay-frozen.py tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv` → **REPLAY OK: 11/11 rows reproduced**, exit 0 (13:14Z, re-read 13:15Z) |
| D2 path, post-change | selftest 12/12; default `15cdfbda…` exit 0; `--json` `19765ddf…` exit 0; frozen packet `9a69985a…` exit 0; projector selftest **50/50** (the round-20 selftest additions) |

## 4. Before/after movement — one row per cell

| pin | before (round-18 generation) | after (round-20 generation) | movement |
|---|---|---|---|
| receipt `tool_pins["tools/d2-typed-labels.py"]` | `0da0015f…` | `76536a92…` | **changed — this is the re-pin** |
| receipt `tool_pins["tools/assemble-d2-typed.py"]` | `c7e5a749…` | `c7e5a749…` | none |
| receipt `tool_pins["tools/assemble-d2.py"]` | `8ea6bdde…` | `8ea6bdde…` | none |
| manifest rows 1–12 | 12 rows, gate cell `04ad4bb4…` | byte-identical | **none** (no gate cell moved; the new file is a new *generation*, not a new row set) |
| manifest file | `2556b084…` (filed round-18) | `2556b084…` (new round-20 file, same bytes) | new file, same bytes |
| snapshot `packet.d2.typed.yml` / `packet.d2.yml` | `1b5010b7…` / `e0f21509…` | identical | none |
| `run.log` (stdout of the frozen packet) | `9a69985a…` | `9a69985a…` | **none — the D2 verdict bytes did not move** |
| recorded verdict | exit 0, 15 findings, 0 fails | exit 0, 15 findings, 0 fails | none |

The one-line summary: **the tool bytes moved, the verdict bytes did not.** That is
the control the re-pin exists to record, and it is measured, not assumed: the
frozen typed packet was re-run under the new projector revision and its stdout
hashes to the round-11 value.

## 5. Append-only controls (filed bytes re-hashed before and after the build)

```sh
sha256sum tools/gates/frozen/round-11/MANIFEST.tsv                # aad230bf… → aad230bf…
sha256sum tools/gates/frozen/round-11/typed-pipeline/run-receipt.json  # c49ebc9e… → c49ebc9e…
sha256sum tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv       # 2556b084… → 2556b084…
sha256sum tools/gates/frozen/round-18/repin-d2/run-receipt-repin.json  # d90c09e8… → d90c09e8…
git status --porcelain reports/round-8 … reports/round-19 \
  tools/gates/frozen/round-11 tools/gates/frozen/round-18 \
  tools/gates/expected/d4-typed-labels-check-gate/r19-pre          # 0 lines
```

## 6. Re-verification commands (third party, no scratch needed)

```sh
TMPDIR=/var/tmp/kotadama-r20-repin python3 tools/replay-frozen.py \
  tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv        # expect: REPLAY OK: 11/11
python3 tools/gates/typed-pipeline-gate.py \
  tools/gates/frozen/round-20/repin-d2/typed-pipeline/packet.d2.typed.yml | sha256sum   # 9a69985a…
python3 tools/gates/typed-pipeline-gate.py --selftest | tail -1        # 12/12
python3 tools/gates/typed-pipeline-gate.py | sha256sum                 # 15cdfbda…
python3 tools/d2-typed-labels.py --selftest | tail -1                  # 50/50
sha256sum tools/gates/frozen/round-20/repin-d2/MANIFEST.tsv \
          tools/gates/frozen/round-20/repin-d2/run-receipt-repin.json \
          tools/gates/frozen/round-20/repin-d2/freeze.txt
python3 reports/round-20/run-validation.py --check        # read-only; claim O failures []
```

**Operational note (cost the round-18 seat a run):** `tools/replay-frozen.py`
refuses a temporary root inside the repo — with `TMPDIR=$PWD/.scratch` every row
reads `could-not-evaluate reason=mirror_unsafe` ("temporary root is inside the
repo"). Replays need a TMPDIR outside the tree (`/var/tmp/…`), which is why the
lane rule "export TMPDIR=$PWD/.scratch before scratch-writing commands" and this
replay command differ.

## 7. Freshness, stated plainly

- The generation pins the projector revision live at the freeze stamp
  (`76536a92…`, first observed 13:01:06Z, unchanged 13:01–13:15Z). If the
  projector moves again in this wave, the receipt's `tool_pins` cell and (if the
  gate moves) the manifest's gate cell go stale: the answer is one re-run of the
  builder, or a manual two-cell substitution in **this seat's own new files**
  (the filed rounds 8–19 are never touched).
- The manifest is byte-identical to the round-18 manifest. That is a reading, not
  an accident: no gate cell moved, so the derivation had nothing to substitute.
  The movement this generation records lives in the receipt's `tool_pins`.
- The D2 byte-identity above is a **reproduction**, not an endorsement: 15 open
  hold lines remain open design debt, and the projector's new per-family alias
  leg is claim-O work this seat re-pinned but did not design or audit.

## 8. Limits

- A re-pin pins **bytes and a verdict**. It is not a clearance, not a canon
  ruling, and not a statement that the round-20 projector revision is correct.
- The receipt's `tool_pins` cover the three tools the round-18 receipt covered
  (projector, D2 adapter, D2 serializer). Tools the frozen row does not name are
  not pinned here — `tools/assemble-d4-typed.py` and the D4 gates are pinned by
  the D4 baseline and the `typed-pipelines.json` profile, other seats' surfaces.
- `run.log` and `freeze.txt` match the lane `.gitignore` `*.log` pattern only for
  `run.log`; committing this generation needs `git add -f` for that one file
  (same note the round-9, round-11 and round-18 records carry).
