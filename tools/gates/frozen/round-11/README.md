# Round-11 frozen generation — the D2 typed gate flow

Written by the R11-D05 integration (design.md §5.2). New generation, round-3
manifest idiom; the round-3 and round-4 generations under
`tools/gates/frozen/` are untouched by it.

## Rows (11)

`MANIFEST.tsv` pins four groups; every input is a byte copy under this tree:

| rows | gate | input | recorded verdict |
|---|---|---|---|
| 1 | `tools/gates/typed-pipeline-gate.py` | `typed-pipeline/packet.d2.typed.yml` (the frozen build product) | exit 0, **15** `FINDING` lines (+1 note line) |
| 2-6 | the five legacy gates | `examples/culture-d2/packet.d2.typed.yml` | naming 7, phonology 3, costume 0, lexicon 0, myth 0 |
| 7-11 | the same five gates | `examples/culture-d2/packet.d2.yml` (raw) | naming 17 (**10 `PHON-*` naming the ten English `GAR-*` labels**), phonology 3, rest 0 |

The naming-gate pair is the channel differential on the record: 17 → 7 findings,
exactly the ten artifacts retired, nothing else moved.

Supporting records under `typed-pipeline/`: `run.log` (verbatim stdout of row 1),
`run-receipt.json` (schema `kotodama-frozen-run-v1`: command, exit, hold ids,
`stdout_sha256`, gate hash, input digests, tool pins for the projector, adapter,
serializer and the five reader gates), `freeze.txt` (steps and controls), and the
two packet copies.

**The record is named `run-receipt.json`, not `expected.json`, on purpose**:
`tools/check-gate-battery.py` discovers every `expected.json` under its roots and
fails closed on a gate outside its seven-name constant, so an `expected.json`
naming `typed-pipeline-gate.py` would change the battery's standing reading from
`5 pinned / 2 uncovered` to a `BASELINE-GATE-UNKNOWN` finding. The pins live in
`run-receipt.json`, which the battery does not scan.

## Replay

`TMPDIR` must be outside the repo — `replay-frozen.py` refuses in-repo mirrors by
design, and the lane's usual `$PWD/.scratch` is inside it:

```sh
mkdir -p /var/tmp/kotodama-r11
TMPDIR=/var/tmp/kotodama-r11 python3 tools/replay-frozen.py \
  tools/gates/frozen/round-11/MANIFEST.tsv
# REPLAY OK: 11/11 rows reproduced the recorded verdicts
```

A reproduced red verdict stays red: rows 2 and 7 record `exit_code 1` (the gates'
own findings), which the replay reproduces rather than clears.
