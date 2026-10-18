# R20-O07 — shard 3/6: mirror faithfulness without the foreign examples tree

- round 20, seat **R20-O05..O10**, claim **O**. Fragment 3 of 6.
- date 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- canon: NON-CANON. Read sets are measured with an audit hook, never assumed.
- writes: `tools/d2-typed-labels.py` (selftest section 5), this file.

## 1. The claim under test

Before the fix, a faithful D4 mirror had to carry
`examples/culture-d2/components/{12-rank-rules,11-costumes}.yml`: the projector
read them for a D4 packet. This shard measures that the requirement is gone and
that the mirror that no longer carries them is still *faithful* — it rebuilds
the filed D4 projection byte for byte.

## 2. Before/after read set (reproducible, both from committed bytes)

Method: `sys.addaudithook("open")` over the peer run in-process, absolute paths,
scratch script `.scratch/o05/readset.py` (not committed). The "before" reading
runs the **r19-pre committed peer copy** (`tools/gates/expected/d4-typed-labels-check-gate/r19-pre/tools/d2-typed-labels.py`)
against its own committed packet and projection, so it is reproducible after the
live tree moved; the "after" reading runs the live peer.

| reading (2026-10-18) | command | non-stdlib reads | verdict |
|---|---|---|---|
| BEFORE | `python3 .scratch/o05/readset.py <r19-pre>/tools/d2-typed-labels.py --packet <r19-pre>/examples/culture-d4/packet.d4.yml --check <r19-pre>/typed-labels.d4.yml` | 6: the peer, the D4 packet, **`examples/culture-d2/components/12-rank-rules.yml`**, the reader gate, **`examples/culture-d2/components/11-costumes.yml`**, the graded projection | exit 0, "byte-identical deterministic projection" |
| AFTER | `python3 .scratch/o05/readset.py tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | 4: the peer, the D4 packet, the reader gate, the graded projection | exit 0, "byte-identical deterministic projection" |

The two bold rows are the wart. The r19-pre baseline had to declare exactly
those two D2 files as inputs of a D4 command; the new `r20-post` baseline
declares four inputs and no D2 file (shard 4 §2).

## 3. The mirror test itself (selftest section 5, `--selftest` legs 46–50)

The mirror is built in a temporary directory and holds **three** files: the
projector, the reader gate the projection names, and the D4 packet. It holds no
`examples/culture-d2` directory at all — asserted, not assumed
(`check("mirror: the d4 mirror holds no examples/culture-d2 tree",
not (d4mirror / "examples/culture-d2").exists())`).

| leg | question | observed |
|---|---|---|
| `mirror: the d4 mirror holds no examples/culture-d2 tree` | is the foreign tree really absent? | absent |
| `mirror: the d4 build runs with no foreign tree (exit 0/1)` | does the build complete? | exit 1 (findings present, the D4 holds), projection written |
| `mirror: the mirror build is byte-identical to the filed d4 projection` | is the mirror *faithful*? | `cbcf997f5f38fac89b0fb1b6a6841ec42c9041a2599df44083ddefc5c22cfb4f`, equal to the filed projection |
| `mirror: --check exits 0 in the mirror` | does the mirror agree with itself? | exit 0 |

Control that this is a real property and not a tautology: the same mirror, with
the D4 packet's `named_eras` block removed, still runs (the documented-skip
branch) — the `family: a packet declaring no alias rules is skipped, never
aliased` leg in section 3d exercises exactly that path, and before the fix the
same mirror died with `missing examples/culture-d2/components/12-rank-rules.yml;
A1 cannot be recorded`.

## 4. What this test does **not** cover

- It does not cover the rank-rule ledger: the ledger's rule set is the round-8
  literal set baked into the projector, so it reads no component file in any
  family. That is why removing the foreign tree is sufficient for the D4 path —
  and also why the D4 projection still carries those literal rules (a named
  residual: shard 6 §3).
- It does not cover D2: the D2 leg *does* read its own components by design, and
  the D2 CLI legs in selftest section 4 keep copying them into their mirror.
- It does not prove the projection's content is sound — only that no foreign
  byte contributes to it.

## 5. Limits

- The read-set traces pin the *reads*, not the writes: an audit hook sees
  `open`, and the mirror's own build is what the byte comparison checks.
- The mirror byte-identity leg depends on the filed D4 projection being current;
  a stale filed projection reads as a failure by design.
