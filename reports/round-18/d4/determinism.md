# R18-D07/D08 — determinism: the generalized gate and the D4 legs

- round 18 (operator loop 2 of 3, build round 2 of 4; `reports/round-18/claims.json`,
  claim **D**, shards **D07/D08**). Lane: `kotodama-shokunin`.
- assignment (verbatim): "D R18-D07..D10 (determinism+replay x4): two consecutive
  gate runs byte-identical findings; build the round-18 frozen manifest (rows:
  generalized gate over D4 typed packet + typed-labels --check + assemble-culture-d4
  --check) with input snapshots; replay green via tools/replay-frozen.py;
  reports/round-18/d4/{determinism,manifest,replay}.md."
- date: 2026-10-18; measurements 10:21–10:41Z (local -03:00). Baseline revision
  `3dd3754207032cb81f5fb3e202fe85cf79211339` (round-17, D rejected); round-18
  declare `c66ac3c`.
- canon: NON-CANON engineering evidence. Nothing here is a canon record, a lore
  handoff, a clearance, or a rights/attribution ruling.
- writes: this file, `reports/round-18/d4/{manifest,replay}.md`,
  `tools/gates/frozen/round-18/**`, `tools/gates/d4-typed-labels-check-gate.py`,
  `tools/gates/d4-assembly-check-gate.py`, plus gitignored scratch under
  `.scratch/r18d07/`. The one command that runs with `TMPDIR` outside the repo is
  the `tools/replay-frozen.py` subprocess itself, which refuses an in-repo mirror
  root by design (`replay.md`). No tool, packet, projection, component, baseline,
  receipt or earlier-round byte is edited by this shard; no commit, no push.

## 0. Verdict

**Deterministic on every path measured, and the D4 typed-packet row is blocked,
not measured.** The projector, the D4 assembler and the generalized gate each
produced byte-identical output across two consecutive runs; the gate's D2 path
still reproduces the pre-generalization bytes exactly. The one row claim D needs
first — the generalized gate over `examples/culture-d4/packet.d4.typed.yml` —
cannot be recorded yet because the D4 typed packet and the family adapter that
builds it (`tools/assemble-d4-typed.py`) do not exist; the gate's D4 packet run
is a *stable* exit-2 refusal (byte-identical across runs) and the pending row is
carried in the frozen receipt (see `manifest.md` §1, §6).

## 1. What is measured, and why this shape

1. **Byte-identity of two consecutive runs** — stdout bytes and the `--json`
   document, compared run-to-run; a gate whose interface is stdout plus an exit
   code is "deterministic/unchanged" exactly when those bytes repeat.
2. **Identity against a pre-change recording** — the D2 typed-packet run's stdout
   bytes compared against the bytes captured *before* the gate was generalized at
   all, and against the round-11 filed pin.
3. **Equality against the pinned D4 record** — the projector's emitted finding set
   mapped to `(id, severity, where)` and compared two ways with
   `examples/culture-d4/expected-holds.json` (15 holds, 1 note, 0 fails; delta none).

## 2. Pre-change baseline (before the generalization landed)

Gate revision `d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d`
(the pre-round-18 bytes; `.scratch/r18d07/d2-baseline/`, 10:26–10:27Z):

| command | exit | observed |
|---|---:|---|
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.typed.yml` | 0 | stdout sha256 `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606`; 15 `FINDING` + 1 `NOTE`. **Equal to the round-11 frozen row's filed output bytes** — the harness is measuring the right bytes |
| the same, twice | 0/0 | stdout, findings and `--json` byte-identical |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.yml` | 0 | stdout sha256 `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b` |

## 3. After the generalization

The gate was still being revised while this shard ran (digests observed within
twenty minutes: `d102fd1d`, `2a08fb2d`, `b4232690`, `a2948ebb`, `be4099dc`,
`edfec5f3`, `7fad95e0`, `d09f7c3b`, `391a7255`, `38978331`, `7a3bb816`,
`d4785d9a`, `ea95e2a1`, `68e4835a`, `286d6e82`). Every reading below names the
revision it was taken at.

| reading | revision | exit | observed |
|---|---:|---:|---|
| D2 typed packet, twice | `d4785d9a`, `ea95e2a1` | 0/0 | stdout **byte-identical to §2** (`9a69985a…`) and to each other; `--json` identical |
| generalized-gate selftest | `d4785d9a`, `ea95e2a1` | 0 | `12/12 checks passed` |
| gate over `examples/culture-d4/packet.d4.yml`, twice | `286d6e82` | 2/2 | stdout byte-identical (sha256 `0e82305b59b159de2310fa646f792792878468ffdd1bb37068753e4416ad3281`): `ok L1-assembler`, `ok L1-expected-holds`, then `FAIL L1-build: adapter missing: tools/assemble-d4-typed.py` — a **stable refusal**, not a flapping one |
| `tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json`, twice | — | 1/1 | byte-identical JSON (sha256 `991b8d310ced1fd1d767340b56d6bde464e59897e868a06c1876f52a43d47cfa`), 15 holds / 1 note / 0 fails, equal as a set to `examples/culture-d4/expected-holds.json` (delta none both ways) |
| `tools/assemble-culture-d4.py --check`, twice | — | 0/0 | byte-identical output |
| gate over the D4 **typed** packet | — | — | **not measured: `examples/culture-d4/packet.d4.typed.yml` does not exist** (§0, `manifest.md` §1) |

The projector equality leg is the one the round needs to be true before the gate
can be asked anything: the D4 finding set is exactly the pinned 16-row set, with
the 12 owed-form holds naming `GAR-0x`/`LEX-GAR-0x` and the 4 `D2L-RANK` rows
inherited from the D2 constant block (a fact recorded independently by
`reports/round-18/d4/holds.md` and `.scratch/r18d03-06/common-evidence.md`).

From 10:43:14Z the gate held revision
`286d6e82711427ea03a9a42e5cb10f6c369f0f1b0cd589c74a4092f3b8c12af9` across twelve
consecutive 20-second polls (through 10:45Z) with `--selftest` green and the D2
typed-packet run byte-identical to §2 — the revision the two D4 readings above
were taken at, and the first revision to hold still for more than two polls.

## 4. Controls

| control | command | observed |
|---|---|---:|
| battery (my two new gate files present) | `python3 tools/check-gate-battery.py` | exit 0, 7 pass / 0 fail / 0 unevaluable |
| generalized-gate selftest | `python3 tools/gates/typed-pipeline-gate.py --selftest` | 12/12 (at `d4785d9a`, `ea95e2a1`) |
| round-11 frozen generation, pre-change | `TMPDIR=/var/tmp/kotodama-r18 python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` | `REPLAY OK: 11/11` (10:21Z) |
| projector `--check` (D4) | `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | exit 0 |
| assembler `--check` (D4) | `python3 tools/assemble-culture-d4.py --check` | exit 0 |

## 5. Limits

- Determinism here is run-to-run on one machine and **one tool revision per
  reading**; the gate was a moving target during this shard, so every number
  above names its revision and the frozen manifest (`manifest.md`) pins the
  revisions instead of relying on this file.
- Exit 0 is not a clearance: the gate prints the holds verbatim, and the D4
  culture stays NON-CANON design debt with 15 open holds.
- Nothing in this file asserts that `tools/assemble-d4-typed.py` or
  `examples/culture-d4/packet.d4.typed.yml` exist, that the D4 typed packet is
  sound, or that the round-18 validator passes.
