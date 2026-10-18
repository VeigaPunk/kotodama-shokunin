# R18-D09 — the round-18 frozen manifest

- round 18, shard **D09** (claim **D**, determinism + replay x4). Seat header,
  date, baseline, canon and write scope are shared with
  `reports/round-18/d4/determinism.md` (§0 header block); measurements
  10:21–10:41Z 2026-10-18.
- deliverable: `tools/gates/frozen/round-18/` — a **new** frozen generation
  (`MANIFEST.tsv`, `inputs/**`, recorded outputs, `freeze-receipt.json`,
  `README.md`). No byte of `tools/gates/frozen/round-3|4|11/**` is edited, and no
  earlier-round receipt is re-pinned in place. (`repin-d2/` inside the same
  directory is the round-18 O07-O10 re-pin seat's generation, not this one's.)

## 1. Rows

Claim D names three checks. Two are recorded and replay green; the first is
carried as a **pending** row because its input does not exist yet.

| row | gate | input | recorded verdict |
|---|---|---|---|
| 1 (pending) | `tools/gates/typed-pipeline-gate.py` (generalized) | `examples/culture-d4/packet.d4.typed.yml` | **not recorded** — input missing at freeze time |
| 2 | `tools/gates/d4-typed-labels-check-gate.py` | `examples/culture-d4/typed-labels.d4.yml` | exit 0, sha256 `1c8add321259a9f0…`, 0 `FINDING` lines |
| 3 | `tools/gates/d4-assembly-check-gate.py` | `examples/culture-d4/packet.d4.yml` | exit 0, sha256 `c60820a54742ecaa…`, 0 `FINDING` lines |

Pins, as recorded in `MANIFEST.tsv` and `freeze-receipt.json`
(schema `kotodama-frozen-manifest-v1`):

| row | gate_sha256 | input_sha256 | output_sha256 |
|---|---|---|---|
| 2 | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` | `a59990bbfe5a8992ffa6e67e9b3e43e7ff477df9fc754e5af92b6f40d23fe11d` | `1c8add321259a9f026d6e37b0dbd95b0f548f31fe0a10c56098911c21532a6fe` |
| 3 | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` | `c60820a54742ecaa1edef972c6c94cce3f88313fbace8ef19eaeddd9a42572a7` |

The pending row's reason is recorded verbatim in `freeze-receipt.json`
(`pending[0].reason`): the D4 typed packet and its family adapter had not landed
at freeze time. At gate revision `286d6e82` the D4 packet run reaches
`ok L1-assembler`, `ok L1-expected-holds`, then
`FAIL L1-build: adapter missing: tools/assemble-d4-typed.py` (exit 2), and
`tools/assemble-d2-typed.py` still refuses the D4 packet
(`FAIL assembler_identity: packet bytes are not assemble-d2.py's deterministic
assembly (e7ecd2045ef0 vs e0f21509e14a)`).

## 2. Why two of the rows are new gate files

`tools/replay-frozen.py` launches a pinned gate as exactly
`[python3, tools/gates/<gate>.py, <input>]` — one input path, no flags — and
requires the gate to be a Python file directly under `tools/gates/`. The two
checks claim D names are flag-shaped invocations of tools that live outside that
directory:

    python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check <projection>
    python3 tools/assemble-culture-d4.py --check

Both checks are therefore wrapped by two thin, read-only gate-shaped entry
points added by this shard:

| gate | what it does | what it never does |
|---|---|---|
| `tools/gates/d4-typed-labels-check-gate.py` | runs `tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check <input>` and forwards the peer's stdout, stderr and exit code unchanged | re-implement the check, write any file, judge the projection's content |
| `tools/gates/d4-assembly-check-gate.py` | loads `tools/assemble-culture-d4.py` with `runpy.run_path` (read-only) and byte-compares its own `assemble()` payload against the input path | re-implement assembly, write the packet, judge the culture |

Both print only the input path they were handed, so the recorded bytes are stable
across recording and replay (the replay mirror holds the frozen snapshot at the
same relative path). Controls run by this shard: default-argument run (exit 0),
missing input (assembly shim exit 2 "assembly error", projection shim exit 1
"differs" — the peer's own semantics), and both shims leave the tree unchanged.

## 3. Determinism before freezing

The recording harness (`.scratch/r18d07/freeze.py`) runs every row twice from the
repo root and refuses to freeze on a missing gate, a missing required input,
non-deterministic stdout/exit, or an exit code outside `{0, 1}`. Recorded outputs
are the bytes of the first run; the second run must match.

## 4. What changed between the first and the final freeze (reported, not hidden)

The first recording (10:37Z) also carried a fourth row — the generalized gate
over round-11's frozen D2 typed packet, a re-pin of the round-11 filed row. That
row was re-recorded as valid at gate `ea95e2a1`, and then invalidated minutes
later when the gate was revised again (`gate_digest_mismatch`). Because
`reports/round-18/run-validation.py:884-893` requires **every** round-18 manifest
to replay green, a gate-pinned row is a liability while the gate is still being
revised, and the re-pin cascade is already carried by two dedicated records:

- `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` (O07-O10, 11 rows, the
  round-11 manifest with one `gate_sha256` cell replaced);
- the validator's own frozen-row leg (`reports/round-18/run-validation.py:542`),
  which re-runs `[gate, round-11 typed packet]` and compares stdout to the filed
  pin.

The row was therefore dropped from this generation, the pending row was made
optional (recorded automatically once its input exists), and the final manifest
pins only artifacts that are stable under gate revision: the two D4 check legs.
The harness still supports the re-pin row (`ROWS[3]` in `freeze.py`, plus
`add_repin_evidence`, which refuses unless the recorded output bytes, exit code
and finding count equal the round-11 filed row's). The D2 verdict-preservation
evidence this shard measured directly: at gate revisions `d4785d9a` and
`ea95e2a1` the D2 typed-packet run was byte-identical to the pre-change baseline
and to the round-11 pin `9a69985a…` (`determinism.md` §2-§3).

## 5. Re-running the recording (the exact completion procedure)

When the D4 typed packet lands, the pending row is added by re-running the same
harness — a new recording, never an edit of a recorded row:

```sh
export TMPDIR=$PWD/.scratch
python3 tools/assemble-d2-typed.py --packet examples/culture-d4/packet.d4.yml \
    --projection examples/culture-d4/typed-labels.d4.yml \
    --emit examples/culture-d4/packet.d4.typed.yml      # once the adapter accepts the D4 assembler
python3 .scratch/r18d07/freeze.py                       # all rows; adds row 1
mkdir -p /var/tmp/kotodama-r18
TMPDIR=/var/tmp/kotodama-r18 python3 tools/replay-frozen.py \
    tools/gates/frozen/round-18/MANIFEST.tsv
```

The same re-run is also the correct response to a later revision of any pinned
gate or input: the row goes red by digest, and the answer is a new recording.

## 6. Limits

- A frozen row pins bytes and a verdict, not a design: exit 0 on the D4 rows only
  says the two checks are byte-identical reproductions; the D4 culture keeps its
  15 holds.
- Rows 2/2b read live peer files (the packet, projection, components, assembler,
  projector) beside the frozen input; the pins in `freeze-receipt.json` name them,
  and a later edit there turns the affected row red by design.
- `freeze-receipt.json` is deliberately not named `expected.json`:
  `tools/check-gate-battery.py` discovers every `expected.json` under its
  baseline roots and fails closed on a gate outside its seven-name constant (the
  round-11 README records the same constraint).
