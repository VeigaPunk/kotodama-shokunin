# shard-8 — regression state: v1 drift, v2 named drifts, what is owed (R20-D05..D12)

- topic: the honest regression state of the three profiles on the live tree,
  with the evidence for each red or tolerated row, and the owner of each
  remainder.
- date: 2026-10-18.

## 1. v1 path — exit 1, one named input drift (O seat)

```sh
export TMPDIR=$PWD/.scratch
python3 tools/exercise-handoff-e2e.py
# -> FAIL input-digest: tools/d2-typed-labels.py: frozen 0da0015f7003… live 76536a924280…
# -> handoff-e2e: exit=1 … E2E-DIGEST: 1 read-set file(s) changed since the baseline was frozen
```

- The v1 code path is preserved verbatim in behaviour (21-file read set,
  round-11 packet renderer, `reports/round-11/handoff/expected.json`) and its
  control matrix passes 17/17 on a fresh fixture.
- The live-tree red is an input change by the **O seat's round-20 per-family
  alias work**: `tools/d2-typed-labels.py` moved from `0da0015f…` to
  `76536a92…`. That file is pinned by the filed round-11 baseline and is
  embedded in the v1 packet's `dependency_manifest`, so the v1 path detects
  the drift and fails closed — exactly what a pinned path should do.
- This is a re-pin owed as a **new row** (the wave rule: filed round-8..19
  artifacts are never edited in place); the round-11 baseline cannot be
  re-frozen. Owner: O seat's repin cascade / integrator. The v1 path becomes
  green again only if the O bytes are reverted or a new v1 row is recorded.

## 2. v2 path — exit 0 with two named drift rows

```sh
python3 tools/exercise-handoff-e2e.py --profile v2
# -> handoff-v2: exit=0 claims=15 links=50/50 drift=named(tools/harness/packet_links.py round-16)
```

- Green: the v2 twins match their baseline pins; the shape gate exits 0
  `16/16 + 20/20 + 0`; `packet_uncertainty.py` exits 0 over 15 claims; the
  link leg resolves 50/50 (with `--no-digests`).
- Two digest-leg rows are named, never hidden (every other finding fails):
  1. `tools/harness/packet_links.py` — the round-16 harness fix (commit
     `f30b6f8`), committed before round 20;
  2. `tools/d2-typed-labels.py` — the round-20 O-seat change (§1).
  Both are M-DIGEST-MISMATCH rows in the v2 packet's own manifest, i.e. the
  v2 build pins older tool bytes; the v2 packet bytes themselves are
  unchanged and stay green.

## 3. v3 path — exit 0 (green)

- See shard-1/2/4/5/6. The v3 baseline is frozen on the current live bytes
  (including the O landing), so any further movement of a pinned file re-pins
  as a new row with the reason recorded (`--profile v3 --freeze`).

## 4. Owed / follow-ups

- O seat: its two adapter-gate receipts and the negative control (the D4 run
  with the D2 tree restored) — pinned read-only in the v3 manifest, not
  asserted by this exercise. The two adapter gates are currently red on the
  working tree (`d4-typed-labels-check-gate.py` exit 1 "differs from the
  deterministic projection"; `typed-pipeline-gate.py` 14/16 legs over the D4
  typed packet) — reported here as the O seat's in-flight state, not
  absorbed.
- Integrator: the v1 re-pin row (§1); the `OQ-V3-04` id retained as the
  re-open id if the O bytes are reverted.
