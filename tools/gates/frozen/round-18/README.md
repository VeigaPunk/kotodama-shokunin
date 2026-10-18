# Round-18 frozen generation — the D4 check legs and the D2 re-pin

Written by the R18-D07..D10 integration (claim D, determinism + replay shard;
didactic receipts in `reports/round-18/d4/{determinism,manifest,replay}.md`).
Round-3/4/11 generations are untouched by it: this is a new generation
directory, and no earlier-round receipt is edited in place. `repin-d2/` beside
this file belongs to the round-18 O07-O10 re-pin seat, not to this manifest.

## Rows (2 recorded; the D4 typed-packet row is carried as pending)

`MANIFEST.tsv` pins two rows and `freeze-receipt.json` records one **pending**
row; every input is a byte copy under `tools/gates/frozen/round-18/inputs/`:

| row | gate | input | recorded verdict |
|---|---|---|---|
| 1 (pending) | `tools/gates/typed-pipeline-gate.py` (generalized) | `examples/culture-d4/packet.d4.typed.yml` | not recorded — input missing at freeze time |
| 2 | `tools/gates/d4-typed-labels-check-gate.py` | `examples/culture-d4/typed-labels.d4.yml` | the projection check (`d2-typed-labels.py --check`, exit 0) |
| 3 | `tools/gates/d4-assembly-check-gate.py` | `examples/culture-d4/packet.d4.yml` | the assembly check (`assemble-culture-d4.py --check`, exit 0) |

**Pending row (blocked at freeze time, 2026-10-18 10:40Z):** the generalized gate
over `examples/culture-d4/packet.d4.typed.yml` cannot be recorded yet — the D4
typed packet and the family adapter it is built by do not exist. At gate
revision `ea95e2a1…` the D4 packet run reaches `ok L1-assembler`,
`ok L1-expected-holds` and then `FAIL L1-build: adapter missing:
tools/assemble-d4-typed.py` (exit 2); `tools/assemble-d2-typed.py` still refuses
the D4 packet (`FAIL assembler_identity: packet bytes are not assemble-d2.py's
deterministic assembly`). Land the pair, then re-run the recording harness
(`.scratch/r18d07/freeze.py`, all four rows) — the row is added as a NEW row,
never by editing a recorded one.

Rows 2 and 3 exist because `tools/replay-frozen.py` launches a pinned gate as
`[python3, tools/gates/<gate>.py, <input>]` — one path, no flags — while the two
checked tools take a flag and live outside `tools/gates/`. Both gates are thin,
read-only adapters over the peer tool, added by this shard: they call the peer's
own check path (loaded by path, never re-implemented) and forward its output and
exit code.

This generation deliberately pins **no** gate revision (row 1 is pending) while
the generalized gate is still being revised: `reports/round-18/run-validation.py`
requires every round-18 manifest to replay green, and a row that pins the gate
bytes goes red the moment the gate is edited. The round-11 re-pin is carried
instead by `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` (O07-O10, 11 rows,
one `gate_sha256` cell replaced) and by the validator's own frozen-row leg
(`reports/round-18/run-validation.py:542`), which re-runs the round-11 typed
packet under the live gate and compares stdout to the filed pin.

`freeze-receipt.json` (schema `kotodama-frozen-manifest-v1`) carries the per-row
gates, digests, the pending row with its reason, and the two recorded verdicts.
It is deliberately **not** named `expected.json`: `tools/check-gate-battery.py`
discovers every `expected.json` under its baseline roots and fails closed on a
gate outside its seven-name constant (the round-11 README records the same
constraint).

## Replay

`TMPDIR` must be outside the repo — `replay-frozen.py` refuses an in-repo mirror
root by design, and the lane's usual `$PWD/.scratch` is inside it:

```sh
mkdir -p /var/tmp/kotodama-r18
TMPDIR=/var/tmp/kotodama-r18 python3 tools/replay-frozen.py \
  tools/gates/frozen/round-18/MANIFEST.tsv
```

A reproduced red verdict stays red; every row here records exit 0 because every
row is a green check on a NON-CANON artifact. Row 3 pins the generalized gate
revision `ea95e2a1…`: a later edit to that gate turns the row red by design (a
re-freeze is a new recording, never an in-place edit).
