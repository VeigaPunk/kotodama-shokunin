# R17-D31 — negative: an owed form silently dropped (run receipts)

- round: 17 (loop 2 of 3, build round 1 of 4) · shard: **D31** (negatives ×3,
  claim D `culture-d4-assembly`) · owner: L2 worker, kotodama-shokunin lane
- assignment (verbatim): "D4 R17-D30..D32 (negatives x3): gloss smuggled onto
  sound channel; owed form silently dropped; loan without layer ref — each must
  be caught; reports/round-17/tests/neg-<n>.md."
- date: 2026-10-18. Baseline revision
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (`reports/round-17/claims.json:5`);
  working-tree HEAD `9b49a4a` at write time.
- canon: NON-CANON engineering evidence. Fixtures are synthetic controls derived
  from the filed D2 example; nothing here is a culture design, a canon record, a
  handoff, or a real-world claim.
- writes: **this file only** plus gitignored scratch under `.scratch/r17-d-neg/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No
  tool, gate, packet, component, projection or earlier-round byte is edited by
  this seat. No commit, no push.
- **status: complete — caught, both directions.** Dropping the routing row's
  `owed_slot` (§3.1) and dropping the hold itself (§3.2) each exit 1 with a
  check that names the missing owed slot/record.

## 1. The hazard, and the catch criterion

An owed form is a routed record whose native/borrowed form is unresolved: the
typed packet carries one `D2L-FORM-UNRESOLVED` hold per routed record and one
`owed_slot` per `typed_channel` row (`examples/culture-d2/packet.d2.typed.yml:3324-3424`,
`pipeline_findings` `:3433-3529`). "Silently dropped" is the failure mode where
the debt stops being named — either the routing row loses its `owed_slot`, or the
hold leaves `pipeline_findings` — and the artifact still assembles.

Catch criterion (design §2.2 coverage, D18; `tools/gates/typed-pipeline-gate.py:341-353`):
the run must exit non-zero **and** the hold set / routing cross-check must name
the dropped slot. A shorter hold set alone is not enough — the cross-check must
name which debt went missing.

## 2. Fixtures (scratch, byte-pinned)

| id | fixture (`.scratch/r17-d-neg/…`) | sha256 | injection |
|---|---|---|---|
| 2a | `typed-owed-slot-drop.yml` | `f5c3809099cf1913f381a4cf7869c5317ce1e90152fccc7c05c13c9314dfd42f` | first `    owed_slot: "LEX-GAR-01"\n` removed from the routing table (the debt declaration deleted, the hold retained) |
| 2b | `typed-hold-drop.yml` | `b43769b30e5be37ffc2fa7459119e643880415ff190b13083351d7a84c3aab92` | the GAR-01 finding block removed from `pipeline_findings` (the hold deleted, the routing row retained) |

Base bytes: `examples/culture-d2/packet.d2.typed.yml` sha256
`1b5010b7f449ec78755e9a8b0efea62c705af7ec5c592ceda6cf2c072dfac8a3`.
Both fixtures are one byte-range deletion each; generation was a `python3`
heredoc from the lane root with `TMPDIR=$PWD/.scratch` (the deletion strings are
the table's injection column, byte for byte). The gate's own selftest carries the
2a-shaped control (`tools/gates/typed-pipeline-gate.py:520-527`); this shard runs
it standalone, adds the 2b direction, and pins the receipts.

Tool revisions at every run below: `tools/gates/typed-pipeline-gate.py`
`d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d`.
Python 3.14.7.

## 3. Receipts

Positive control, same date and revision: `python3 tools/gates/typed-pipeline-gate.py`
→ exit 0, `summary: 16/16 legs passed` (`.scratch/r17-d-neg/gate-positive.txt`);
the live packet's cross-check reads
`ok L3-routing-consistency` with 10 routed records and 10 owed slots.

### 3.1 Routing row's `owed_slot` dropped — caught by `L3-routing-consistency`

```sh
python3 tools/gates/typed-pipeline-gate.py .scratch/r17-d-neg/typed-owed-slot-drop.yml
```

counts (that command, 2026-10-18): exit **1**, `summary: 12/13 legs passed`
(`run-typed-owed-slot-drop.txt:32`). The failing leg, verbatim (`:30`, wrapped):

```text
FAIL L3-routing-consistency — holds ['GAR-01' … 'GAR-10'] vs routed ['GAR-01' … 'GAR-10']; owed slots ['LEX-GAR-01' … 'LEX-GAR-10'] vs routing ['LEX-GAR-02' … 'LEX-GAR-10']
```

The catch names the dropped debt: `LEX-GAR-01` is in the hold set and absent from
the routing set. The check requires `hold_records == off_records and hold_slots
== routed_slots` (`tools/gates/typed-pipeline-gate.py:350`) — a row whose debt
declaration was deleted cannot pass.

### 3.2 Hold dropped from `pipeline_findings` — caught by four legs

```sh
python3 tools/gates/typed-pipeline-gate.py .scratch/r17-d-neg/typed-hold-drop.yml
```

counts (that command, 2026-10-18): exit **1**, `summary: 9/13 legs passed`
(`run-typed-hold-drop.txt:32`). Four legs fail, verbatim:

```text
FAIL L3-holds — missing [('D2L-FORM-UNRESOLVED', 'hold', 'GAR-01')]; extra []            (:22)
FAIL L3-counts — observed counts differ from {'hold': 15, 'note': 1, 'fail': 0}          (:25)
FAIL L3-baseline-set — committed set differs from the observed finding set                (:28)
FAIL L3-routing-consistency — holds ['GAR-02' … 'GAR-10'] vs routed ['GAR-01' … 'GAR-10']; owed slots ['LEX-GAR-02' … 'LEX-GAR-10'] vs routing ['LEX-GAR-01' … 'LEX-GAR-10']   (:29)
```

The catch names the record (`GAR-01`) and the debt (`LEX-GAR-01`) in the
same run. The exact-set comparison against the frozen expected hold set
(`:306-313`) is what makes "silently" impossible: a shorter hold set is a
failure even when every remaining line is valid.

## 4. Sweep

Every run of this shard is recorded under `.scratch/r17-d-neg/`; the sweep is
`ls .scratch/r17-d-neg/run-*` plus the control receipts (2026-10-18). Exits
observed: positive 0, 2a **1**, 2b **1**; no dropped-owed-form variant exited 0,
and no run produced a traceback.

## 5. D4 re-point (to-verify at write time)

D4's design contracts landed during this shard
(`reports/round-17/d4/typed-support-1.md` §5.3-5.6,
`typed-support-2.md` §2-3); state at last poll (2026-10-18 09:32Z):
`tools/assemble-culture-d4.py` has landed, while `examples/culture-d4/` is still
absent (components drafting under `reports/round-17/d4/components/`, 3/12 at
that stamp). Re-point recipe when D4 lands:

1. apply the same single deletion to D4's typed packet
   (`examples/culture-d4/packet.d4.typed.yml`) — remove one routing row's
   `owed_slot` (2a) and, separately, remove one owed-form hold from
   `pipeline_findings` (2b); the D4 hold id is `D4L-FORM-UNRESOLVED` and the
   rule is one hold per owed slot (`typed-support-2.md` §3);
2. run the D4 gate over each tampered packet;
3. caught = nonzero exit **and** a cross-check naming the dropped slot. If D4's
   gate names the checks differently (`L3-routing-consistency` here), the
   record/slot-addressed line is the criterion, not the check id. The D4 gate's
   exact-set comparison (`typed-support-1.md` §5.4) is what makes a shortened
   hold set a failure.

This is `to-verify` — the mechanism is shared (`typed-pipeline-gate.py` grading,
`:341-353`), but it has not been re-run over D4 bytes by this seat.

D4's candidate set (`reports/round-17/d4/design-brief.md` §7.1) pins the two owed
classes the drop test applies to: 6 `D4L-FORM-UNRESOLVED` holds
(`GD-01`..`GD-06`) and 6 `D4L-REGISTER-UNRESOLVED` holds
(`AL-01#plain`..`AL-06#plain`); the D4-specific control battery is separate
(§8, C-01..C-10 — e.g. C-04, "routing row deleted while a plain doublet is
owed"). This file is the pipeline-level analog of that class and does not
discharge it.

## 6. Sources

- `tools/gates/typed-pipeline-gate.py` `d102fd1d…` — routing-consistency check
  (`:341-353`), L3 hold/count/baseline checks (`:294-338`), hazard control 2
  (`:520-527`)
- `examples/culture-d2/packet.d2.typed.yml` `1b5010b7…` (`typed_channel`
  `:3324-3424`, `pipeline_findings` `:3433-3529`)
- receipts: `.scratch/r17-d-neg/gate-positive.txt`,
  `run-typed-owed-slot-drop.txt`, `run-typed-hold-drop.txt`
- `reports/round-11/depth/design.md` §2.2/§3.1 (the coverage rule this check
  implements) — read as prior art
