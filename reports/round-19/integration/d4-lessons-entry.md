# R19-D08 — the D4 craft lesson entry (paste-ready fragment for `corpus/lessons/`)

- round: 19 (operator: loop 2 of 3, build round 3 of 4; `reports/round-19/claims.json`,
  provider `hyper/deepseek-v4.1-flash` per the operator substitution). Lane:
  `kotodama-shokunin`.
- seat **R19-D08** (lessons; D08..D10 = lessons + integration + ledger). Assignment
  (verbatim): "D R19-D08..D10 (lessons + integration): corpus/lessons/round-19.md
  draft; LOG/SCORECARD integration drafts; fragment ledger."
- date: 2026-10-18 (stamps UTC). Baseline revision
  `e5718945a1ab0a0c3db955338d2cae77d68fd348` (round-18 admit); declare
  `169c616613899f7ba86b8fb58ed808bdfd4b5ccd`.
- canon: **NON-CANON engineering draft.** This file is paste-ready *draft text*
  for a round-19 lesson entry in `corpus/lessons/`. It edits no byte of `SKILL.md`,
  `corpus/**`, `tools/**`, `examples/**`, or any filed round-8..18 artifact. The
  parent owns placement, wording and admission.
- writes: this file, plus gitignored scratch under `.scratch/`. No commit, no push.
- **Placement note (a dispatch collision, reported not resolved).** This seat was
  assigned `corpus/lessons/round-19.md`; peer seat **X21** was also assigned that
  path and landed a full gate-keeper survey there at ~11:33Z (`corpus/lessons/round-19.md`,
  digest `df4de597…` at 11:37Z), superseding this seat's 20 260-byte draft of that
  file. X21's own survey records the collision and states the D claim's lesson
  entry "must land as a **different** path or name its owner". This fragment is
  that different path. **The parent decides** whether the D4 craft entry becomes a
  new `corpus/lessons/round-19-d4.md`, is merged into X21's survey, or is dropped.

## D4 craft, codified

Every row cites the committed bytes or a read-time command. The delivered D4 typed
pipeline is the reference implementation; the round-17 design files are the
pre-implementation contract it is measured against.

1. **The typed shape is two labels per garment, and both are first-class routing
   carriers.** The D4 projector types each costume's `form_slot` as its *own*
   `translated-label` (`source.record` = the owed-slot id, e.g. `LEX-GAR-01`), in
   addition to typing the costume record. `tools/assemble-d4-typed.py:170-175`
   states the consequence: the gate's L3 leg requires one moved routing row per
   off-channel hold, and the projector emits one hold per label (garment-field
   hold keyed `GAR-0x`, slot hold keyed `LEX-GAR-0x`). Measured on
   `examples/culture-d4/packet.d4.typed.yml` (sha256 `f63ed531…`): `typed_channel`
   carries **exactly 12 rows** — `GAR-01..06` and `LEX-GAR-01..06`. A slot-keyed
   record is a **lawful carrier, not a coverage gap** (the adapter's coverage rule
   at `:242-249` treats a slot-keyed record as typed even when no costume record
   owns the id).

2. **The routing row is the contract surface, and the owed slot is named exactly
   once.** Each row carries `record`, `kind`, `label_id`, `owner`,
   `source_field: garment`, `off_channel_field: garment_gloss`,
   `channel: off-sound-and-identity`, `hold: D2L-FORM-UNRESOLVED`, `owed_slot`
   (`tools/assemble-d4-typed.py:227-241`). Measured: the six `GAR-0x` rows carry
   `owed_slot: null`; the six `LEX-GAR-0x` rows carry `owed_slot` set to their own
   slot id. The `:236-240` comment is the rule — "the owed slot is named once per
   costume — on the slot's own routing row; the gate compares slot sets". The
   moving field is `garment` → `garment_gloss`, and it is **moved, not flagged**
   (`:12-14`; design §2.3 T1 row 6: "adding typing fields cannot exempt a
   string"); the gloss stays in the packet under its new name so it is off the
   sound-and-identity channel without being deleted.

3. **The round-trip serializer corrupts foreign content; derive generated
   artifacts by text transform.** `tools/assemble-d4-typed.py:296-302`: "the
   round-trip serializer corrupts regex backslashes, booleans and nulls (D4 is the
   first culture whose packet carries derivations with regex patterns)". The rule
   that follows is executable: **never re-serialize foreign content**; read the
   source packet's *text*, rename only the costume `garment` key inside the
   `costumes` block, and append the adapter-owned blocks (`schema`,
   `typed_channel`, `typed_assembly`, `pipeline_findings`, `pipeline_counts`)
   serialized from adapter-generated data alone (`:303-325`). Control: the D4 thin
   gates read exit 0 at the census ("byte-identical deterministic projection" /
   "byte-identical deterministic assembly"), so the text transform is reproducible
   on the delivered bytes. General lesson: a `--check` byte-identity leg is only as
   strong as the serializer it re-runs; where the serializer cannot round-trip, the
   derivation must be a transform with a pinned output, not a re-emission.

4. **Three fail-closed inputs gate the typed build, and each names its refusal.**
   `assembler_identity` (`:112-124`) re-runs the *declared* assembler's own
   `assemble()` and compares packet bytes — "packet bytes are not <assembler>'s
   deterministic assembly". `projection_fresh` (`:127-148`) requires the
   projection's `assembly.packet_sha256` to equal the packet digest **and** the
   projector to regenerate the committed projection byte-for-byte, else "stale
   projection pin". Coverage (`:242-249`) makes an untyped record a *problem*,
   never a silent exemption. All three exit **2** (could-not-evaluate) — the
   correct class: a missing or stale input is not a content verdict.

5. **Derivation replay needs machine-readable pattern/output pairs.** Design §Δ3
   (`reports/round-17/d4/design-brief.md:296-310`) requires quote forms to be
   *derived* from their plain base by one of two declared operations — `head2`
   (first two syllables) for measure words, `reverse` (string reversal) for the
   numeral series — checked through `derived_from` + `derivation` fields, with the
   coverage block reporting `derived_forms` and `derived_ok` counts that must
   agree; the control is a fixture whose quote form ≠ `apply(op, base)` → FAIL
   `D4L-ARGOT-DERIV`. Lesson: **a derivation is replayable only if the operation
   and its input are both machine-readable** — a prose rule cannot be replayed, and
   an unreplayable derivation is not a derivation. §9.3 adds the freeze discipline:
   two builds into scratch must be byte-identical (no timestamps, no host paths, LF
   endings, sorted keys), and a re-pin is a **new** frozen revision — never a
   re-pointed old manifest.

6. **Register-scoped slots are the design's core delta and are absent from the
   delivered tree.** Design §Δ1 (`design-brief.md:254-275`) requires a *second*
   routing class: a supplied, inventory-clean quote form admissible only in a quote
   slot, staying **on** the sound and identity channel (`off_channel_field: null`)
   while the plain slot it must also fill stays owed (`hold:
   D4L-REGISTER-UNRESOLVED`, `owed_slot: <slot>#plain`). Measured on the delivered
   bytes: `grep -c "D4L-REGISTER\|#plain"` over
   `examples/culture-d4/{packet.d4.yml,typed-labels.d4.yml,packet.d4.typed.yml}` →
   **0 / 0 / 0**, and `grep -c REGISTER tools/d2-typed-labels.py` → **0** (no
   engine path). The delivered packet's per-label `register:` fields (`trade`,
   `craft`, `public`, …) are label metadata, **not** the Δ1 slot-routing class. The
   honest craft reading: the register class is **unbuilt design debt**, and no
   reader should write that the delivered packet routes register-scoped slots.
   (A peer survey cites `examples/culture-d4/ASSEMBLY.md:118` as the register
   locus; that line is about round-17's divergent design documents, not a routing
   class — re-read it before inheriting the citation.)

7. **An expected-holds file that equals the gate's own output has drift teeth, not
   content teeth.** `examples/culture-d4/expected-holds.json` (sha256 `09490a27…`)
   carries 15 holds + 1 note + 0 fails and is **equal as a set** to the projector's
   emitted findings; its 12 form holds are keyed twice (once at `GAR-0n`, once at
   `LEX-GAR-0n`), and 4 of its 16 rows are D2's rank constants over D2's where-ids
   (`reports/round-18/d4/holds.md` §2). The reconciliation **exists as a companion
   receipt** (`holds.md` §3 dispositions all 17 union rows and the delivered tree's
   own 6-hold declaration), but the artifact carries no pointer to it. Rule: when a
   pre-registration exists, the *reconciliation is the deliverable* — per-row
   mapping or a named drop reason — and a file that merely equals the emitted set
   must say which authority it rides on (emitted-as-truth vs declared-as-truth).

8. **A gate's input is part of its contract, and the D4 typed packet is a second
   input.** The round-18 D claim measured
   `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`
   (the *assembled* packet): **19/19, exit 0** at gate revision `04ad4bb4…`. The
   *typed* packet (the adapter's product) is a different input and reads **14/16,
   exit 1** at the same revision, failing `L3-routing-consistency` (finding
   L19-D08-2 below). A gate name and a green do not travel to a sibling input; the
   input path is part of the measurement, and a round that changes which input is
   graded must re-measure rather than inherit.

9. **A thin gate exists to make a flag-shaped check pinnable, and adds no
   semantics.** `tools/gates/d4-typed-labels-check-gate.py` (sha256 `05f99629…`)
   and `tools/gates/d4-assembly-check-gate.py` (sha256 `df1a364b…`) are read-only
   adapters because `tools/replay-frozen.py` launches a pinned gate as exactly
   `[python3, tools/gates/<gate>.py, <input>]` — one input path, no flags. Both
   docstrings say "This gate adds no semantics of its own and is not a clearance".
   Craft rule: when a check is flag-shaped, wrap it as a thin single-input gate
   *beside* the peer (never re-implementing it) rather than teaching the replay
   harness flags. Corollary: neither D4 gate ships a self-test of its own — a
   `--selftest` argument is taken as the input path (peer survey measured
   `d4-assembly-check-gate.py --selftest` → exit 2).

10. **Determinism checks carry no information unless the positive leg is green.**
    Carried from round 18: at gate revision `be4099dc…` a crashing positive control
    made `determinism: two runs byte-identical` pass *vacuously* (two identical
    failures compare equal). Read the positive leg first.

## Live findings recorded against the D4 pipeline (reported, not adjudicated)

Both findings were measured at HEAD `169c616` and re-measured before this file was
written; the peer survey `corpus/lessons/round-19.md` (X21) independently reports
the first and does not report the second.

- **L19-D08-1 — the D4 adapter's own selftest is red.** `python3
  tools/assemble-d4-typed.py --selftest` exits **1** at adapter sha256 `08784671…`
  (committed at `e571894`, worktree clean). Two visible defects: the selftest
  mirror copies only `assemble-d4-typed.py`, `assemble-culture-d4.py` and
  `d2-typed-labels.py` into `tools/` (`:405-409`), so the D4 assembler's serializer
  lookup fails inside the mirror — `required file not found: tools/assemble-d2.py`
  — taking the positive, determinism, `--check`, tamper and stale-projection legs
  down with it; and the routing fixture (`:467-477`) passes
  `form_slot: "LEX-GAR-99, (to-verify)"` expecting `routing[0]["owed_slot"] ==
  "LEX-GAR-99"`, but the slot-label lookup at `:199-200` keys on the **raw**
  `form_slot` string while the fixture's label is keyed under the bare slot id.
  Round-18's `validation.json` never ran this selftest (its `--selftest` legs are
  the gate, `assemble-d2-typed.py`, battery, craft, evidence-coupling,
  replay-frozen), so claim O's "all typed/assembly selftests green" is an open
  round-19 obligation. Corroborated by X21 (4/11 at `08784671…`).
- **L19-D08-2 — the gate over the *typed* packet fails `L3-routing-consistency`.**
  At gate revision `04ad4bb4…`:
  `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml`
  → exit **1**, `summary: 14/16 legs passed`, with
  `FAIL L3-routing-consistency — holds ['GAR-01'…'LEX-GAR-06'] vs routed
  ['GAR-01'…'LEX-GAR-06']; owed slots ['LEX-GAR-01'…'LEX-GAR-06'] vs routing
  ['LEX-GAR-01'…'LEX-GAR-06', 'null'×6]`. The same gate over
  `examples/culture-d4/packet.d4.yml` reads exit 0, 19/19. Candidate readings: the
  gate's routing-set comparison counts the six explicit `owed_slot: null` cells, or
  the adapter should omit the key on garment rows. Owner: the adapter seat and the
  gate seat; the parent dispositions. This matters because the round-18 frozen
  generation carries a **pending** row for exactly this input
  (`tools/gates/frozen/round-18/freeze-receipt.json`), and the peer survey proposes
  recording it — but a frozen row pinned to a 14/16 red would record a red verdict,
  not a green one.

## Limits

- All measurements are point-in-time (2026-10-18, live 64-worker wave; worktree
  dirty, `tools/check-gate-battery.py` moving through digests `53b1913a…` →
  `72d6e011…`). No digest here authorizes later bytes (round-15 lesson: a green at
  an earlier revision does not authorize later bytes, a red does not condemn them).
- The two findings are **reported, not adjudicated**; the round auditor and parent
  retain the verdict.
- No canon, real-world rights, clearance, or attribution ruling is made or
  absorbed. The freshness axis-move pause stands; the two round-11 ratios remain
  separate and un-reopened.
