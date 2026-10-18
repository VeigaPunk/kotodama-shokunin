# R18-D03 — gate run 1: declared resolution over the D4 packet (in place)

- round: 18 (operator loop 2 of 3, build round 2 of 4; 64 declared workers,
  `reports/round-18/claims.json`) · shard **D03** (gate runs ×4, first leg).
- claim **D** (`depth`). Assignment (verbatim): "D R18-D03..D06 (gate runs x4):
  run the generalized gate over the D4 packet (4 independent runs incl. one in
  an isolated copy); findings == expected set EXACTLY; exit-code semantics;
  reports/round-18/d4/gate-runs-{1..4}.md."
- date: 2026-10-18, local -03:00; run stamps below. Reference revision `c66ac3c`
  (round-18 declare), baseline `3dd3754207032cb81f5fb3e202fe85cf79211339`.
- writes: this file only, plus gitignored scratch under `.scratch/r18d03-06/`
  (`TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No tool,
  packet, component, projection, baseline, or earlier-round byte is edited; no
  commit, no push.
- canon: NON-CANON engineering evidence — not a canon record, a lore handoff, a
  clearance, or a rights statement.

## 0. Verdict

**Exit 2 — BLOCKED: the generalized gate resolves the D4 pipeline correctly
(declared assembler identity and declared expected set both verify) and then
stops at `L1-build: adapter missing: tools/assemble-d4-typed.py`. No finding is
emitted, so the equality leg ("findings == expected set EXACTLY") is not
reached — it is not failed, it is unreachable at this artifact state.** Two
independent in-place runs are byte-identical (`stdout sha256 0e82305b…`), and the
`--json` run exits 2 with no document.

## 1. Run record

| field | value |
|---|---|
| command | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` |
| cwd | lane root |
| run 1 started / exit | 2026-10-18 07:58 -03:00 · **2** |
| run 2 (independent process) | exit **2**; `cmp` vs run 1 → **byte-identical** |
| stdout sha256 | `0e82305b59b159de2310fa646f792792878468ffdd1bb37068753e4416ad3281` |
| stderr | empty |
| `--json` companion | `python3 tools/gates/typed-pipeline-gate.py --json examples/culture-d4/packet.d4.yml` → exit 2, sha256 `fb305699a28f7dadb4063ae50941d6c84db6918e90499a62c32447244cb47d40` |

Gate revision at run time: `tools/gates/typed-pipeline-gate.py` sha256
`286d6e82711427ea03a9a42e5cb10f6c369f0f1b0cd589c74a4092f3b8c12af9` (the
generalized build; the file was still being revised during the wave — see §5).

Inputs (sha256, all read-only):

| path | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` |
| `examples/culture-d4/typed-labels.d4.yml` | `a59990bbfe5a8992ffa6e67e9b3e43e7ff477df9fc754e5af92b6f40d23fe11d` |
| `examples/culture-d4/expected-holds.json` | `09490a2756d123ebbc2023be89fc01c95ec2f8cc7e6df42ecc5b8cd438058e98` |
| `tools/assemble-culture-d4.py` | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` |
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` |

## 2. What the gate resolved (verbatim legs)

```
ok   L1-assembler:
ok   L1-expected-holds:
FAIL L1-build: adapter missing: tools/assemble-d4-typed.py
```

- `L1-assembler` — the packet's declared assembler (`assembly.generator:
  tools/assemble-culture-d4.py`, self-pinned `assembly.assembler_sha256`
  `943f487b…`) reproduces the packet bytes through the assembler's own
  `assemble()` call. Independently confirmed for this report:
  `python3 tools/assemble-culture-d4.py --check` → exit 0, "packet.d4.yml:
  byte-identical deterministic assembly"; `--selftest` → 81/81.
- `L1-expected-holds` — `examples/culture-d4/expected-holds.json` (landed by
  R18-D01/D02) is consistent: schema `kotodama-typed-pipeline-holds-v1`,
  counts `{hold: 15, note: 1, fail: 0}`, 15 holds, 1 note.
- `L1-build` — the family convention resolves the typed adapter to
  `tools/assemble-d4-typed.py`; the file does not exist at this revision (nor
  `tools/assemble-culture-d4-typed.py`, nor a delivered
  `examples/culture-d4/packet.d4.typed.yml`).

## 3. Equality against the expected set

| leg | observed |
|---|---|
| emitted `FINDING`/`NOTE` lines | **0** (no run reached L3) |
| expected set | 15 holds + 1 note + 0 fails (`examples/culture-d4/expected-holds.json`) |
| missing / extra | not evaluable — the gate emitted nothing to compare |
| counts | not evaluable |

The expectation used for the comparison in runs 2-4 is the landed file above; an
independent derivation made before it landed (frozen projection →
`findings`, no gate/projector import) produced exactly the same 16 `(id,
severity, where)` rows — delta none (`.scratch/r18d03-06/expected-independent.json`).

## 4. Exit-code semantics exercised here

- **2 = could-not-evaluate** — a declared artifact that the resolution requires
  is absent. Distinct from a mismatch: nothing about the packet, projection or
  expected set is judged false.
- Determinism of the blocked verdict: two independent processes → identical
  bytes; the isolated copy (run 4, `gate-runs-4.md`) reproduces the same
  `0e82305b…` stdout byte-for-byte, so the block is a property of the artifact
  set, not of this working tree.

## 5. Caveats

- The gate file was still moving during the wave: observed shas at
  07:29–07:41 -03:00 were `2a08fb2d…`, `b4232690…`, `be4099dc…`, `edfec5f3…`,
  `38978331…`, `5b4501a9…`, `d4785d9a…`, `ea95e2a1…`, `84dc177e…`, `a201afee…`,
  `286d6e82…` (one of those reads caught a half-written file mid-save, whose
  traceback is **not** evidence of a defect). Every statement here is pinned to
  `286d6e82…`; a later revision needs a re-run.
- The missing adapter is upstream work, not this shard's to author: writing
  `tools/assemble-d4-typed.py` belongs to the D-shard's adapter owner, and this
  seat's write scope is its four run reports (plus scratch).
- Nothing here is a clearance: exit 2/1/0 refer to engineering agreement with a
  NON-CANON expected set, never to lore acceptance.

## 6. Revision watch (appended while the wave was still moving)

Samples taken after this run, at later gate revisions `65b1d4f7…`, `45a78b41…`,
`cc721ee0…`, `7ec051df…` (2026-10-18 07:48–07:52 -03:00):

- the D4 declared run stayed at **exit 2** at every sample — the failing leg was
  renamed (`L1-build: adapter missing` → `L1-profile: adapter: pins None, live
  None (tools/assemble-d4-typed.py)`), and the gate grew a declared-pipeline
  registry (`tools/gates/typed-pipelines.json`, sha256 `434e90509a1c…`) that now
  names the D4 profile explicitly;
- the D2 default run stayed at **exit 0, stdout `15cdfbda…`** — byte-identical
  to the pre-generalization baseline at every sample, including revisions newer
  than the one this report is pinned to.

So the blocked verdict and the D2 byte-identity are stable across the observed
revisions, while the leg names are not. **The D4 run must be re-run on the final
gate revision once `tools/assemble-d4-typed.py` (or a delivered
`examples/culture-d4/packet.d4.typed.yml`) lands**; the prepared harness is
`.scratch/r18d03-06/run-gate.py` (recorded run + exact set comparison),
`isolate.sh` (isolated copy) and `derive-expected.py` (independent expected set).
