# R18-D04 — gate run 2: the D4 build path under declared stand-in adapters

- round 18, shard **D04** (gate runs ×4, second leg); claim **D** (`depth`).
  Assignment and write scope as in `gate-runs-1.md`; this file only, plus
  gitignored scratch under `.scratch/r18d03-06/`.
- date: 2026-10-18, local -03:00. Gate revision at run time:
  `tools/gates/typed-pipeline-gate.py` sha256 `286d6e82711427ea…` (full sha in
  `gate-runs-1.md` §1).
- canon: NON-CANON engineering evidence.

## 0. Verdict

**The D4 build path can be driven end-to-end only with a stand-in adapter, and
no stand-in reachable from the delivered machinery is green: the run advances to
`L1` clean and then fails `L2-channel`.** Three stand-ins were run; the failure
chain localizes three separate obstructions (§2), and the third is a concrete
defect of reusing the D2 typed adapter for a D4-shaped packet — it **replaces
the packet's 333-line `assembly` block** (component digest pins, reader and
serializer pins, `skipped_keys`) with a 4-entry typed block, which the naming
gate reads: the typed run gains 8 `DERIV-REPLAY` findings the delivered packet
does not produce.

The D4 run therefore exits 2 (declared run, no adapter) or 1 (stand-in runs) at
this revision — never 0. Equality with the expected set is **not achieved**; the
closest stand-in passes the hold-set legs and still dies on the channel leg.

## 1. Invocation

```
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml \
    --adapter <stand-in>            # plus --assembler/--projection/--expected where noted
```

Stand-ins (scratch, never in `tools/`; each `build(packet, projection)` reuses
the delivered `tools/assemble-d2-typed.py` machinery and replaces only the
D2-bound assembler-identity input — the fixture pattern first published by
R18-O12 in `.scratch/r18-o11/d4_adapter_fixture.py`, copied and pinned here):

| stand-in | sha256 | shape it builds |
|---|---|---|
| `assemble-d4-typed-fixture.py` | `66278146b1f07fba…` | D2 semantics: routing rows for every label record |
| `assemble-d4-typed-remap.py` | `c037187ff1e210511…` | form-slot rows folded onto their owning costume, field moved off channel |
| `assemble-d4-typed-onchannel.py` | `d9d322248613582313…` | same fold, register rows kept on channel (`off_channel_field: null`) |

## 2. The obstruction chain (each step measured)

1. **Coverage rule vs form-slot records** — with the faithful fixture:
   ```
   ok   L1-assembler / L1-expected-holds / L1-assembler_identity / L1-projection_freshness
   FAIL L1-coverage: routing row names record LEX-GAR-01 … LEX-GAR-06 which is not in
        the packet's costume ledger          (exit 2)
   ```
   Source: `tools/assemble-d2-typed.py:215-219`. The D4 projection carries six
   label records keyed `LEX-GAR-0x` (the packet's `form_slots` block, owner
   `GAR-0x`); the adapter's coverage rule requires every routed record to be a
   costume-ledger record.
2. **Routing consistency vs the 12-hold set** — folding the six form-slot rows
   onto their owning costumes clears the coverage rule, and the run then fails
   ```
   FAIL L3-routing-consistency — holds ['GAR-01'…'GAR-06','LEX-GAR-01'…'LEX-GAR-06']
        vs routed ['GAR-01'…'GAR-06']; owed slots match (6 vs 6)      (exit 1)
   ```
   Source: `tools/gates/typed-pipeline-gate.py:621-633` (`hold_records ==
   moved_records`). The pinned expected set has **12** `D2L-FORM-UNRESOLVED`
   holds — six naming costumes, six naming form slots — while the packet's
   costume ledger has six records. Keeping the same rows *on channel*
   (`off_channel_field: null`, the D4 register class the gate documents at
   `:185-193`) removes them from both sides and the leg passes; any *moved*
   variant fails it.
3. **Channel leg vs the packet's own pins** — the on-channel stand-in reaches
   ```
   ok L1-assembler, L1-expected-holds, L1-assembler_identity, L1-projection_freshness,
      L1-coverage, L1-build, L1-schema, L1-routing, L2-retention
   ok L3-holds, L3-notes, L3-fails       (hold set legs pass)
   FAIL L2-channel: naming-collision-gate.py: unexpected added findings: 8× DERIV-REPLAY;
        retained findings are not the legacy set                     (exit 1)
   ```
   Isolated cause: the D2 adapter's `build_typed_packet` rebuilds the packet's
   `assembly` block. Measured on the built payload
   (`.scratch/r18d03-06/typed-onchannel.yml`, 70 386 bytes vs the delivered
   82 859) — block line counts: `assembly` **333 → 4**, plus the added
   `schema`/`typed_channel`/`pipeline_findings`/`pipeline_counts`/
   `typed_assembly` blocks. The naming gate over the typed packet adds exactly
   the eight `DERIV-REPLAY` FAILs for `NM-01..NM-08` ("rule 'CX-01' does not
   apply to stem 'tum+hai'", …, `.scratch/r18d03-06/naming-typed.out` vs
   `naming-legacy.out`), so the typed run is not the legacy run minus the
   routed lines.

## 3. Equality against the expected set

| stand-in | exit | FINDING/NOTE lines | equality |
|---|---:|---:|---|
| none (declared run, run 1) | 2 | 0 | unreachable |
| fixture | 2 | 0 | unreachable (L1 coverage) |
| remap (moved) | 1 | 16 (L3 legs ok) | hold set legs pass; channel leg red |
| on-channel | 1 | 16 (L3 legs ok) | hold set legs pass; channel leg red |

In both 16-line runs the hold-set legs (`L3-holds`, `L3-notes`, `L3-fails`,
`L3-counts`) are green against `examples/culture-d4/expected-holds.json`, so the
15-hold/1-note expectation is *reachable* — it is the channel leg that is not
satisfiable by a stand-in built from the delivered D2 machinery.

## 4. What a green D4 run requires (evidence-backed)

A delivered `tools/assemble-d4-typed.py` must (a) route by costume ledger (or
fold form-slot rows onto their owners), (b) keep the D4 register rows on channel
so the routing-consistency leg is not asked for 12 moved records, and (c)
**preserve the packet's own `assembly` block** (component/reader/serializer
pins) instead of replacing it with a D2-shaped typed block. Items (a) and (b) are
satisfiable by the stand-in pattern; item (c) is the residual defect: the reused
`build_typed_packet` is D2-shaped, and no D4 adapter can pass the channel leg
while it rebuilds `assembly`.

## 5. Caveats

- The stand-ins are scratch diagnostics, not deliverables: they are named in no
  manifest, they are never installed into `tools/`, and every verdict above is
  pinned to the adapter sha in §1 and the gate sha in §1. A delivered adapter
  must be re-run, not assumed equal to these.
- My stand-in `remap`/`onchannel` variants re-implement one mapping decision
  (form-slot → owner costume). They are the smallest probes that separate the
  three failures; they do not claim to be the design intent.
- Exit 0 nowhere in this file means "clearance"; it means agreement with a
  NON-CANON expected set.

## 6. Revision watch (appended while the wave was still moving)

The stand-in runs above are pinned to gate `286d6e82…`. At later revisions
sampled 2026-10-18 07:48–07:52 -03:00 (`65b1d4f7…`, `45a78b41…`, `cc721ee0…`,
`7ec051df…`) the declared D4 run stays at exit 2 (adapter absent; the leg is now
`L1-profile`) and the D2 default run stays byte-identical (`15cdfbda…`). The
three obstructions in §2 are read from the packet/projection/adapter shapes, not
from a gate internal: (a) `tools/assemble-d2-typed.py:215-219` needs every
routed record in the costume ledger, (b) `typed-pipeline-gate.py:621-633` needs
the moved records to equal the hold records, (c) the reused `build_typed_packet`
rebuilds the packet's `assembly` block. A re-run on the final revision is
required; the stand-ins are in `.scratch/r18d03-06/adapters/` with pinned shas.
