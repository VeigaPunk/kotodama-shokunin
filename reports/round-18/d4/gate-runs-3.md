# R18-D05 — gate run 3: exit-code semantics and the regression set

- round 18, shard **D05** (gate runs ×4, third leg); claim **D** (`depth`).
  Assignment and write scope as in `gate-runs-1.md`; this file only, plus
  gitignored scratch under `.scratch/r18d03-06/`.
- date: 2026-10-18, local -03:00. Gate revision at run time:
  `tools/gates/typed-pipeline-gate.py` sha256
  `286d6e82711427ea03a9a42e5cb10f6c369f0f1b0cd589c74a4092f3b8c12af9`.
- canon: NON-CANON engineering evidence.

## 0. Verdict

**The default D2 path is byte-identical to its pre-generalization self, all four
filed regression rows reproduce, and `--selftest-generalized` is 14/14 — but one
fail-closed control is broken on the D4 family: a nonexistent D4-family packet
path exits 1 with a raw `FileNotFoundError` traceback instead of exit 2 with a
stable diagnostic.** Every other control measured (forged self-pin, wrong
generator, truncated packet, tampered expected set, missing D2 or family-less
packet) fails closed at exit 2.

## 1. Regression set (default D2 path, pre- vs post-generalization)

| command | pre-gen gate `d102fd1d…` | generalized `286d6e82…` | reading |
|---|---|---|---|
| `python3 tools/gates/typed-pipeline-gate.py` | exit 0, stdout `15cdfbda…` | exit 0, stdout `15cdfbda…` | **byte-identical** |
| `… --json` | exit 0, stdout `19765ddf…` | exit 0, stdout `19765ddf…` | **byte-identical** |
| `… --selftest` | 12/12, exit 0 | 12/12, exit 0 | unchanged |
| `… tools/gates/frozen/round-11/typed-pipeline/packet.d2.typed.yml` | exit 0, stdout `9a69985a…` | exit 0, stdout `9a69985a…` | **byte-identical** (round-11 filed row 1) |
| `… --selftest-generalized` | (mode did not exist) | 14/14, exit 0 | new mode, green at this revision |

The pre-generalization values are the ones frozen in `gate-runs-1.md` §5's
timeline and in `reports/round-11`'s receipts; each was re-measured on
2026-10-18 before the generalization landed. The D2 finding set over the run
(15 holds + 1 note, `(id, severity, where)` equal in both directions) was parsed
and compared, not only the digests (`.scratch/r18d03-06/d2-regression-1.json`).

Timeline note: at the mid-wave revision `ea95e2a1…` the new mode was **11/14**
(three declared-identity controls failed: the d9 typed fixture, the
`L1-assembler` pin re-verification, and the stale declared pin). The O shard
fixed them; at `286d6e82…` the mode is 14/14. Recorded because the claim-O
re-pin/replay story rests on these controls, and because it shows the gate file
was mid-iteration while this round's evidence was being collected.

## 2. Exit-code battery over the D4 packet (scratch copies; delivered bytes never written)

| # | invocation (input mutated in `.scratch/r18d03-06/tampered/`) | exit | observed leg |
|---|---:|---:|---|
| 1 | `… tampered/forged-assembler-pin.yml` (`assembly.assembler_sha256` → 64 zeros) | **2** | `FAIL L1-assembler: packet bytes 00d0c2811b45 are not tools/assemble-culture-d4.py's deterministic assembly (e7ecd2045ef0…)` |
| 2 | `… tampered/wrong-generator.yml` (`generator` → `tools/assemble-d2.py`) | **2** | `FAIL L1-assembler_identity: packet bytes are not assemble-d2.py's deterministic assembly` — the declared assembler is called, it is the wrong one, fail closed |
| 3 | `… tampered/truncated.yml` (packet halved) | **2** | same identity leg fires |
| 4 | `… --expected tampered/tampered-expected.json <packet>` (first hold's `where` → `GAR-99`, `counts` dropped) | **2** | `FAIL L1-expected-holds: inconsistent expected file: … counts {}, 15 holds, 1 note` — a tampered expectation is refused as could-not-evaluate, not reported as a hold-set mismatch |
| 5 | `… examples/culture-d4/absent.yml` (nonexistent D4-family path) | **1** | **Traceback**: `FileNotFoundError … 'examples/culture-d4/absent.yml'` — defect, see §3 |
| 6 | `… examples/culture-d2/absent.yml` | **2** | clean, no traceback |
| 7 | `… absent.yml` (no family directory) | **2** | clean, no traceback |
| 8 | `… examples/culture-d4/packet.d4.yml` (declared run) | **2** | `L1-build: adapter missing` (run 1) |
| 9 | `… --adapter <stand-in>` (run 2 shapes) | **1** | hold-set legs green, channel leg red |

Codes 0/1/2 therefore behave as designed on every path **except** #5: the
generalized resolver reads the packet before checking that it exists, and the
D4-family branch raises instead of failing closed. Exit 1 for a crash also
collides with the documented meaning of 1 ("a leg mismatched"), so a missing
file is currently indistinguishable from a hold-set mismatch.

## 3. Defect record (for the claim-O owner)

- **Symptom:** `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/absent.yml`
  → `FileNotFoundError`, exit 1, traceback on stderr.
- **Contrast:** the same command shape on the D2 family and on a family-less
  path exits 2 with no traceback, so this is a regression the generalization
  introduced on the new code path only.
- **Reproduction:** isolated-copy run 4 (`gate-runs-4.md` §2) reproduces it in a
  mirror of the working tree, so it is not a local workspace artifact.
- **Scope:** read-only diagnosis; the fix belongs to the gate's owner, not to
  this shard.

## 4. Caveats

- All controls are scratch mutations of an immutable delivered packet; the
  delivered `examples/culture-d4/packet.d4.yml` is byte-unchanged
  (`e7ecd204…` before and after).
- Digests are revision-pinned: a later gate revision invalidates the table and
  needs a re-run (the file moved repeatedly during this wave).
- Exit 0 anywhere in this file is engineering agreement with a NON-CANON
  expected set, never a clearance.

## 5. Revision watch (appended while the wave was still moving)

Re-sampled at later revisions `65b1d4f7…`, `45a78b41…`, `cc721ee0…`, `7ec051df…`
(2026-10-18 07:48–07:52 -03:00): the D2 default run remains **exit 0 / stdout
`15cdfbda…`** (byte-identical) at every sample, and the D4 declared run remains
**exit 2** with the adapter named as missing (the leg name is now `L1-profile`,
behind a declared-pipeline registry `tools/gates/typed-pipelines.json`). The
missing-D4-family-path traceback of §3 was observed at `286d6e82…`; it should be
re-tested on the final revision, together with a full re-run of the battery.
