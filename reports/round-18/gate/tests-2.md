# R18-O12 — D4-path positive: the emitted D4 finding set equals the committed expected set

- round: 18 (operator loop 2 of 3, build round 2 of 4; 64 workers) · shard:
  **O12** (tests ×4, claim O `gate-generalization`; the measured subject is claim
  **D** `d4-gate`) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "O R18-O11..O14 (tests x4): default-path byte-identity
  proof (D2 gate verdict unchanged before/after on the same D4-untouched
  inputs); D4-path positive; D4-path negatives (forged assembler pin rejected,
  stale packet rejected); selftest additions; reports/round-18/gate/tests-{1..4}.md."
- date: 2026-10-18. Baseline revision `c66ac3c` (round-18 declare;
  `reports/round-18/claims.json:6` names `3dd3754…`). Evidence window
  10:26–10:29Z.
- canon: NON-CANON engineering evidence. Nothing here is a canon record, a lore
  handoff, a clearance, or a rights/attribution ruling.
- writes: **this file only** plus gitignored scratch under `.scratch/r18-o11/`
  (`export TMPDIR=$PWD/.scratch` before every scratch-writing command). No tool,
  gate, packet, projection, component, expected file or earlier-round byte is
  edited by this seat. No commit, no push.
- **status: COMPLETE — the pipeline-level leg is green; the gate-level leg is
  reachable and blocked on a missing delivered artifact, recorded in §4**
  (`tools/assemble-d4-typed.py` does not exist, so the gate stops at
  `L1-build: adapter missing` after passing its declared-assembler and
  expected-file legs).

## 1. What is measured

Claim D: "The generalized gate runs over `examples/culture-d4/packet.d4.yml`:
findings exactly equal the D4 expected hold set (15 holds + the declared note
set)" (`reports/round-18/claims.json:22`). Claim O requires the D4 path to be
*reachable* — the assembler-identity leg of the D2 gate is pinned to
`tools/assemble-d2-typed.py` and refuses the D4 packet (§3, receipt 1), which is
the round-17 rejection. This shard measures, independently of the D01/D02 seat:

1. the emitted D4 finding set — re-derived by this seat from the delivered
   packet, compared to the committed `examples/culture-d4/expected-holds.json`
   as sets of `(id, severity, where)` and of detail strings;
2. run determinism (two projector runs byte-identical);
3. the pins the expected file carries, re-hashed against the live tree;
4. the gate-level run (§4, pending landing).

## 2. Method

All commands cwd = lane root, `TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE`
inherited from the tools. Raw outputs kept in `.scratch/r18-o11/`.

- emitted set: `python3 tools/d2-typed-labels.py --packet
  examples/culture-d4/packet.d4.yml --json` (twice) → `.scratch/r18-o11/d4-projector-run{,-2}.json`.
  The finding rows are read **from that output**, never from the expected file.
- comparison: set of `(id, severity, str(where))` over all emitted findings vs
  `holds + notes` of `examples/culture-d4/expected-holds.json`; plus a detail
  equality check keyed by `(id, where)`.
- reachability probe: the D2 typed adapter over the D4 packet
  (`python3 tools/assemble-d2-typed.py --packet examples/culture-d4/packet.d4.yml
  --projection examples/culture-d4/typed-labels.d4.yml`).

## 3. Receipts (2026-10-18, 10:26–10:29Z)

| # | command | exit | observed |
|---|---|---:|---|
| 1 | `python3 tools/assemble-d2-typed.py --packet examples/culture-d4/packet.d4.yml --projection examples/culture-d4/typed-labels.d4.yml` | **2** | `FAIL assembler_identity: packet bytes are not assemble-d2.py's deterministic assembly (e7ecd2045ef0 vs e0f21509e14a)` — the round-17 blocker, reproduced as the *before* state: the D2 gate's assembler-identity leg is D2-bound and cannot reach the D4 packet |
| 2 | `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json` | 1 (= holds present) | `stats {"fail": 0, "hold": 15, "labels": 74, "note": 1}` |
| 3 | the same command a second time | 1 | `cmp` of the two stdout captures → **byte-identical**, run digest `991b8d310ced1fd1d767340b56d6bde464e59897e868a06c1876f52a43d47cfa` |
| 4 | set comparison, emitted vs `examples/culture-d4/expected-holds.json` | — | **equal**: 15 holds + 1 note; 0 only-emitted, 0 only-expected |
| 5 | detail comparison, keyed `(id, where)` | — | **16/16 detail strings equal** |
| 6 | pin re-hash of the expected file's declared pins vs the live bytes | — | `packet_sha256 e7ecd204…` = live `packet.d4.yml`; `projection_sha256 a59990bb…` = live `typed-labels.d4.yml`; `projector_sha256 0da0015f…` = live `tools/d2-typed-labels.py` — all three fresh |
| 7 | `sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/typed-labels.d4.yml` after every run above | — | unchanged (`e7ecd204…`, `a59990bb…`) |

The expected file itself: `examples/culture-d4/expected-holds.json`, 2850 bytes,
sha256 `09490a2756d123ebbc2023be89fc01c95ec2f8cc7e6df42ecc5b8cd438058e98`,
`counts {hold 15, note 1, fail 0}`, schema `kotodama-typed-pipeline-holds-v1`.

**This is an independent re-derivation, not a re-read of the committed file.**
Receipt 2's output is the projector's own emission; receipt 4 compares it to the
committed set. A committed expected file that had been copied from a stale
fragment, or a hold laundered into a note, would show here as a set delta. Zero
delta was found. This corroborates `reports/round-18/d4/holds.md` §0 (R18-D01/D02)
on the same digests without reading its scratch.

The declared-vs-emitted delta (claim D's reconciliation half, owned by D01/D02):
the delivered packet's own pre-implementation declaration is 6 ×
`D4L-FORM-UNRESOLVED` @ `GAR-01`…`GAR-06` (`examples/culture-d4/packet.d4.yml`
`contract.hold_set_declaration`, `grep -c "D4L-FORM-UNRESOLVED" …` → 6), while
the engine emits 15 × `D2L-*` holds + 1 note (`grep -c "D2L-" …
examples/culture-d4/packet.d4.yml` → 0, i.e. the ids come from the engine, not
from the packet). The committed expected file carries the **emitted** set. The
disposition of that +9/+1 delta is written by the owning seat in
`reports/round-18/d4/holds.md` §3–§4 (union and delivered-declaration deltas
enumerated); this shard records only that the expected file and the emitted set
agree exactly.

## 4. The gate-level run — reachable, but blocked on the D4 typed adapter

The generalized gate landed (first generalized revision measured `2a08fb2d…`,
final `84dc177e79688e0ed7f323ead42233205b7df7c68183d434bd32a906d647bad4`), and the
D4 path resolves by **family convention** with no flags at all —
`resolve_config` maps `examples/culture-d4/packet.d4.yml` to family `d4`:
assembler `tools/assemble-culture-d4.py`, projection
`examples/culture-d4/typed-labels.d4.yml`, expected
`examples/culture-d4/expected-holds.json`, adapter `tools/assemble-d4-typed.py`.
Running it on the delivered tree (10:29Z and again 10:37Z, both revisions):

```sh
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
# exit 2
# ok   L1-assembler:                       (the declared assembler reproduces the packet bytes)
# ok   L1-expected-holds:                  (the committed expected file is consistent)
# FAIL L1-build: adapter missing: tools/assemble-d4-typed.py
```

**The D4 gate-level positive cannot be reached in this round.** The blocker is a
missing delivered artifact, not a gate defect: `tools/assemble-d4-typed.py` and
`examples/culture-d4/packet.d4.typed.yml` do not exist (`ls` → no such file), and
the delivered `tools/assemble-d2-typed.py` refuses the D4 packet (receipt 1).
Eight independent D-seat reports file the same line
(`reports/round-18/d4/scribe-1.md:203`, `scribe-3.md:113`, `scribe-6.md:137`,
`scribe-7.md:155`, `scribe-8.md:102`, `review-1.md:187`, `review-2.md:166`,
`review-4.md:29`), and `review-4.md:85` names the same two artifacts as the gap.

I did **not** fabricate the missing step to force a green: a scratch fixture that
reuses the delivered adapter's `build_typed_packet` was tried
(`.scratch/r18-o11/d4_adapter_fixture.py`, run via `--adapter`) and it reaches
`ok L1-assembler_identity`, `ok L1-projection_freshness` and then
`FAIL L1-coverage: routing row names record LEX-GAR-01 which is not in the
packet's costume ledger` — the D4 projection types twelve translated labels, six
of them sourced from the **lexicon** (`LEX-GAR-0n`) rather than the costume
ledger, which is exactly the D4-specific routing semantics the missing D4 adapter
owns. A fixture that papered over that would be measuring my own interpretation,
not the pipeline.

**The L3 shape collision I observed mid-window was fixed, not left open.** At
revisions `ea95e2a1…`/`84dc177e…` the gate's `L3-routing-consistency` leg compared
hold `where` values with routing `record` values, and the generalized selftest's
own D9 fixture failed on exactly the D4 shape (a hold at the label `LEX-RF-01`,
a routing row at the record `RF-01` — `tests-4.md` §4). By revision `286d6e82…`
the leg had been revised to filter on **moved** rows and to read the hold id off
the routing rows themselves (`tools/gates/typed-pipeline-gate.py:616-629`,
"a D4-family packet checks its own class (`D4L-FORM-UNRESOLVED`)"), and my
independent replay of the same fixture returns `ok: True, exit_code: 0`
(`tests-4.md` §4). So the only remaining blocker on the D4 gate-level positive is
the missing adapter — with one obligation it inherits: the routing rows a D4
adapter emits must carry a `hold` id that the projector's finding set also
carries, otherwise the revised L3 leg has nothing to match. That obligation is
stated here as a check to run when the artifact lands, not as a measured defect.

What *is* measured green on the D4 path, without the adapter: the declared
assembler leg and the expected-file leg (above, re-verified at revisions
`84dc177e…` and `286d6e82…`), the pipeline-level set equality (§3), and the four
negatives (`tests-3.md` §3/§5 — the rejection happens at `L1-assembler`, before
the build).

## 5. What this does not say

- The D4 tree is NON-CANON and every finding above is open design debt, not a
  clearance; 15 holds + 1 note stay visible.
- Set equality is asserted for the pins named in receipt 6. If the D4 packet or
  projection is regenerated after this stamp, the comparison must be re-run.
- The gate's D4 path is measured only as far as the tree allows: the
  declared-assembler leg, the expected-file leg and the four negatives are green;
  the end-to-end green (§4 expects exit 0 with the committed finding set) is not
  claimed, because the run cannot pass `L1-build` without
  `tools/assemble-d4-typed.py`. When that artifact lands, the run is one command
  (`python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`)
  and this shard's §4 must be re-stamped with its result.
