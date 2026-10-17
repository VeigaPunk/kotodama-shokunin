# R9-D02 — D3 packet determinism (regenerate twice, byte-compare)

- round 9 · worker `R9-D02` · date 2026-10-17 · runs at 2026-10-17T20:48–20:49Z
- baseline revision `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (HEAD of the delivered tree; all commands below run there)
- interpreter `Python 3.14.7 (main, Aug 10 2026, 07:46:56) [GCC 16.1.1 20260728]` on `Linux-7.2.3-arch1-3-x86_64-with-glibc2.44`
- owner of the artifacts under test: `tools/assemble-culture-d3.py` (sha256 `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014`)
- scope note: this fragment records determinism only. `--check` drift diagnosis is R9-D01; evidence-coupling, frozen replay, CLI negatives and interop are R9-D03..D06.

## Claim under test (from `reports/round-9/targets.json`, depth `R9-D02`)

Regenerating the D3 packet twice with `tools/assemble-culture-d3.py` yields byte-identical
outputs; if a diagnosed drift makes regeneration the legitimate owner-action, perform it and
record old/new pins.

## 1. Pre-state: no drift existed at the start

Command (2026-10-17T20:48Z), exit code 0:

```
$ python3 tools/assemble-culture-d3.py --check
packet.json: byte-identical deterministic assembly; packet.gates.yml: byte-identical deterministic assembly
EXIT=0
```

Because `--check` already reported a byte-identical deterministic assembly, **no drift was
diagnosed on this tree**, so regeneration was not a repair but a reproduction test. It was
still performed in place twice (section 2), with the pre-state saved first.

## 2. In-place double regeneration, byte-compared

Sequence (all inside `.scratch/r9d02/det/`, exit codes as printed):

```
$ cp examples/culture-d3/packet.json examples/culture-d3/packet.gates.yml .scratch/r9d02/det/gen0/
$ python3 tools/assemble-culture-d3.py      # run 1: RUN1_EXIT=0
Wrote examples/culture-d3/packet.json (37222 bytes)
Wrote examples/culture-d3/packet.gates.yml (14191 bytes)
$ cp ... .scratch/r9d02/det/gen1/
$ python3 tools/assemble-culture-d3.py      # run 2: RUN2_EXIT=0
Wrote examples/culture-d3/packet.json (37222 bytes)
Wrote examples/culture-d3/packet.gates.yml (14191 bytes)
$ cp ... .scratch/r9d02/det/gen2/
$ cmp gen1/packet.json gen2/packet.json         -> packet.json: IDENTICAL
$ cmp gen1/packet.gates.yml gen2/packet.gates.yml -> packet.gates.yml: IDENTICAL
$ cmp gen0/packet.json gen1/packet.json         -> committed packet.json: REPRODUCED
$ cmp gen0/packet.gates.yml gen1/packet.gates.yml -> committed packet.gates.yml: REPRODUCED
```

Both runs wrote 0 bytes to stderr (`wc -c .scratch/r9d02/det/run{1,2}.stderr` → 0 0).

### Pins — OLD (gen0, committed) vs NEW (gen1 = gen2, regenerated): identical

| artifact | OLD sha256 (gen0) | NEW sha256 (gen1/gen2) | delta |
|---|---|---|---|
| `examples/culture-d3/packet.json` | `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829` | same | none |
| `examples/culture-d3/packet.gates.yml` | `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425` | same | none |

`old == new`: the two regenerations reproduce the committed artifacts bit-for-bit, and the
delivered tree was left unchanged by the regeneration (section 5).

## 3. Independent probe matrix — 13 runs, one byte target

Every probe ran the real CLI in its **own copied tree** under `.scratch/r9d02/var/<probe>/`
(`cp -a tools examples`), then both outputs were `cmp`-ed against the section-2 reference
`gen1`. Reference pins: packet.json `bdf635ce…24829`, packet.gates.yml `306bcac7…70425`.

| probe | invocation / environment | exit | byte-compare |
|---|---|---|---|
| base | plain `python3 tools/assemble-culture-d3.py` in a copied tree | 0 | IDENTICAL |
| hseed0 | `PYTHONHASHSEED=0` | 0 | IDENTICAL |
| hseed12345 | `PYTHONHASHSEED=12345` | 0 | IDENTICAL |
| tz | `TZ=Pacific/Kiritimati` | 0 | IDENTICAL |
| lc | `LC_ALL=C LANG=C` | 0 | IDENTICAL |
| locale-utf8 | `LC_ALL=C.UTF-8 LANG=C.UTF-8 PYTHONUTF8=1` | 0 | IDENTICAL |
| epoch0 | `SOURCE_DATE_EPOCH=0` | 0 | IDENTICAL |
| epochmax | `SOURCE_DATE_EPOCH=9999999999` | 0 | IDENTICAL |
| umask077 | `umask 077 && python3 tools/assemble-culture-d3.py` | 0 | IDENTICAL |
| cwdroot | outputs deleted, then `cd / && python3 <abs>/tools/assemble-culture-d3.py` | 0 | IDENTICAL |
| deeppath | tree at `…/nested/a/b/c/tree`, run from that tree | 0 | IDENTICAL |
| optflag | `python3 -O tools/assemble-culture-d3.py` | 0 | IDENTICAL |
| isolated | `python3 -I tools/assemble-culture-d3.py` (isolated mode: ignores env/PYTHONPATH) | 0 | IDENTICAL |

Selected raw evidence (2026-10-17T20:49Z):

```
$ ( cd / && python3 <scratch>/cwdroot/tools/assemble-culture-d3.py )
Wrote examples/culture-d3/packet.json (37222 bytes)
Wrote examples/culture-d3/packet.gates.yml (14191 bytes)     CWDROOT_EXIT=0
bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829  …/cwdroot/examples/culture-d3/packet.json
306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425  …/cwdroot/examples/culture-d3/packet.gates.yml
$ ( cd / && python3 <scratch>/cwdroot/tools/assemble-culture-d3.py --check )
packet.json: byte-identical deterministic assembly; packet.gates.yml: byte-identical deterministic assembly   CHECK_EXIT=0
```

Determinism therefore holds across hash-seed randomisation, locale, timezone, `SOURCE_DATE_EPOCH`,
umask, `-O`, isolated interpreter mode, working directory and tree path depth; the output carries
no path or time dependency.

## 4. Coupling and leak checks on the regenerated pair

```
$ git hash-object examples/culture-d3/packet.json            -> 0a971d5a3f894030f35c28adaef93ae204000482
$ git rev-parse HEAD:examples/culture-d3/packet.json         -> 0a971d5a3f894030f35c28adaef93ae204000482   MATCH
$ git hash-object examples/culture-d3/packet.gates.yml        -> 6ee7eb395dedbb1399536aca12de727f7242837f
$ git rev-parse HEAD:examples/culture-d3/packet.gates.yml    -> 6ee7eb395dedbb1399536aca12de727f7242837f   MATCH
```

The regenerated files hash to the **committed git blobs at HEAD**, i.e. the worktree is a fresh
assembly of the committed inputs, not a stale copy.

Input coupling (`assembly.source_sha256` declared in packet.json vs actual file digests, all
MATCH): `04-language.json` `fee4ad61a6aa9ca5…`, `05-ritual.json` `20ec0b1ffbc64a04…`,
`06-material.json` `ba9866e37448b18e…`, `07-evidence.json` `1579aa84c3c924e9…`;
`assembly.serializer_sha256` `8ea6bdde9514ee96…` equals the actual
`tools/assemble-d2.py` digest `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d`.

Leak sweep over both regenerated outputs (`grep -c -E '<pattern>' <file>`, 2026-10-17T20:49Z):

- `\.scratch|/tmp/|/home/vgpnk` → 0 hits in each of packet.json, packet.gates.yml
- `[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}` → 0 hits in each

## 5. Delivered tree after the runs

```
$ git status --porcelain
?? .scratch/
?? reports/round-9/baselines/
?? reports/round-9/freshness/
?? louvre_ao17551.html  ?? melqart.html  ?? sumerian_language.html  ?? yazilikaya.html
```

No `M` entries: regeneration changed nothing in the delivered tree (`.scratch/`, the round-9
freshness/baseline fragments and the retrieved HTML are other workers' untracked files).

## 6. Limits and residuals (honest scope)

- Not tested: other machines, other Python minor versions, other OS/glibc, concurrent
  invocations, and read-only-filesystem behaviour. All 13 probes ran on one host/one interpreter.
- Non-atomic publish: the tool writes `packet.json` then `packet.gates.yml` as two separate
  writes, so an interruption between them can leave a mixed-generation pair. This is a
  crash-window property, not a determinism failure; `--check` detects the resulting drift.
- Byte-identity is a property of the pinned input digests in section 4; any component edit must
  be followed by a re-run of this double-regeneration before the pins are quoted again.

## 7. Evidence locations and reproduction

- scratch trees/pins/outputs: `.scratch/r9d02/det/` (gen0/gen1/gen2 + `pins-gen0.txt`,
  `pins-gen12.txt`, `run{1,2}.std{out,err}`) and `.scratch/r9d02/var/<probe>/` — untracked scratch,
  not part of the deliverable.
- reproduce in three commands from the repo root:
  `python3 tools/assemble-culture-d3.py && cp examples/culture-d3/packet.json /tmp/a.json `
  `&& python3 tools/assemble-culture-d3.py && cmp /tmp/a.json examples/culture-d3/packet.json && python3 tools/assemble-culture-d3.py --check`
  (note: `/tmp` was out of inodes at run time on 2026-10-17 — substitute any writable scratch path).
