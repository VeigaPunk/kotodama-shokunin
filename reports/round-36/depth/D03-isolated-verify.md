- Seat: D03 | executor (claim D, apply-and-verify) | isolated-copy integration of D01's drafts + D02's component 14 + leg verification | date 2026-10-19 | baseline ce103bf

# D03 — isolated apply-and-verify for claim D

**Write scope:** this file only. All scratch work under `.scratch/d03/`. No in-tree
byte written, no commit, no push, no network, no install. Every number below is a
command output from an isolated `git archive ce103bf` copy. Every leg ran with
`export TMPDIR=$PWD/../../../.scratch PYTHONDONTWRITEBYTECODE=1`.

Five isolated copies were used:

| copy | contents | purpose |
|---|---|---|
| `.scratch/d03/iso` | pristine ce103bf + a seat-authored test form `L-63` | tamper controls (§3) and the first pin-cascade measurement (§5) |
| `.scratch/d03/iso-base` | pristine ce103bf, **never touched** | causality control (§5) |
| `.scratch/d03/iso-d01` | ce103bf + **D01's Drafts 1+2 applied** | §4.1, §4.2, §4.3, §4.3b |
| `.scratch/d03/iso-p01` | ce103bf + **P01's Surface-A row shape applied** | the row-shape comparison (§4.4) |
| `.scratch/d03/iso-d02` | ce103bf + **D02's component 14**, then **+ D01's Draft 1** | D02's claim (§5b.1), the double-grading hazard (§5b.2), the combined state (§5b.3) |

## 0. Mission status

Assigned: *"Apply-and-verify in an isolated git-archive copy: integrate D01+D02 there,
run assemble-d4 --selftest, the register legs (derivation replay, law gate), and the
typed pipeline; capture outputs."*

**All three named dependencies landed mid-seat, in sequence**: D01
(`reports/round-36/depth/D01-design.md`, 27049 bytes), then P01/K01
(`plan/P01-d-plan.md`, `scout/K01-register-scout.md`), then D02
(`reports/round-36/depth/D02-packet-draft.md`, 35682 bytes). **The assigned mission is
therefore fully executed**: D01's component drafts are integrated in §4, D02's component
14 is integrated and its hazard independently reproduced in §5b, and the combined
D01+D02 state is swept green in §5b.3.

**P01 and K01.** P01 re-aims the plan onto the same open surface and recommends
**Surface A + B-1 only** — the `doublets` block *is* the forward index, no per-record
edit, no contract change — pricing B-2 (`register_form` on base records) as "a contract
amendment and a larger pin cascade. Recorded, not recommended" (`P01-d-plan.md:4.2`).
Its row shape differs from D01's (it carries `era` and names the base field `plain`, not
`plain_slot`). **Both shapes were integrated and run (§4.4).** K01 independently reached
the same stale-premise finding as D01 and this seat, and adds `SCORECARD.md` row lineage
for the r26/r27/r28/r30 closure.

D01's Draft 3 and P01's §4.3 Surface-C guard are *leg specs for gate tools*
(`D01-design.md:5.3`, `P01-d-plan.md:4.3`), not component bytes, and are not integrable
by this seat (tool bytes are the integrator's). Every copy is reproducible from §7.

## 1. Premise correction — the register-form domain is NOT empty at ce103bf

Claim D's `before` reads: *"Register-form domain empty (reports/round-25/argot/ +
SCORECARD r25 row); register law/strata exist but the form class has no instances."*

That was true **at round 25** and false since **round 26**. Verified against the live
packet at ce103bf by independent parse (the naming gate's own `load_yaml`, never a
gate's stdout):

| surface | r25 (`reports/round-25/argot/current-state.md:74-88`) | ce103bf | how measured |
|---|---|---|---|
| `registers` packet key | ABSENT | **PRESENT** (4 identity + 4 act rows) | `load_yaml(packet)['registers']` |
| `register:` on a lexicon record | 0 | **8**, all `stamp` | `[r for r in lex if r.get('register')]` |
| `derived_from` / `derivation` pair | 0 | **8** (`L-55..L-62`) | `[r for r in lex if r.get('derived_from')]` |
| `contract.record_fields.lexicon` carries `register` | no | **yes** (16 fields) | `packet['contract']['record_fields']['lexicon']` |
| `register_law` key | ABSENT | **PRESENT** (5 rows `RGL-01..05`) | `k in packet` |
| `doublets`, `measures`, `oaths` | ABSENT | still ABSENT | `k in packet` |
| top-level keys | 34 | **39** | `len(packet)` |

**Independent re-derivation** (this seat's own implementation, not the gate's):

```
pairs: 8
  L-55 'tuum' op=lengthen base='tum' -> 'tuum' term_match=True base_rec=L-02 doublet_of=L-02 same_packet=True
  L-56 'kit'  op=reverse  base='tik' -> 'kit'  term_match=True base_rec=L-42 doublet_of=L-42 same_packet=True
  L-57 'lom'  op=reverse  base='mol' -> 'lom'  term_match=True base_rec=L-38 doublet_of=L-38 same_packet=True
  L-58 'nees' op=lengthen base='nes' -> 'nees' term_match=True base_rec=L-16 doublet_of=L-16 same_packet=True
  L-59 'huum' op=lengthen base='hum' -> 'huum' term_match=True base_rec=L-09 doublet_of=L-09 same_packet=True
  L-60 'mees' op=lengthen base='mes' -> 'mees' term_match=True base_rec=L-43 doublet_of=L-43 same_packet=True
  L-61 'reek' op=lengthen base='rek' -> 'reek' term_match=True base_rec=L-37 doublet_of=L-37 same_packet=True
  L-62 'saam' op=lengthen base='sam' -> 'saam' term_match=True base_rec=L-39 doublet_of=L-39 same_packet=True
independent re-derivation: 8/8 clean
self-derivations: []
```

Closure is filed and independently recounted: `reports/round-26/report-draft.md:29`
(8/8 re-derived), `reports/round-29/recount/C05.md:30` (`lexicon_rows=62`,
`stamp_rows=8`), `reports/round-30/loop3-retrospective.md:27` (r25 "0 derived pairs"
vs r26).

**D01 reached this same conclusion independently** (`D01-design.md:23-66`, its §0
"the claim's `before` is stale"). Two seats arriving at it by separate measurement is
the corroboration the claim's premise needed.

**Consequence, stated plainly:** claim D's `after_required` ("register-form domain
non-empty with verified forms …") is already satisfied at the baseline by the r26
closure. This seat did **not** build it and does **not** claim it. Whether a round may
take depth credit for a domain closed three rounds earlier, or must re-scope claim D to
the surface that is genuinely open, is the parent's decision — §4 supplies the evidence
for the second reading.

## 2. Baseline legs — isolated `git archive ce103bf`, unmodified

Copy: `mkdir -p .scratch/d03/iso && git archive ce103bf | tar -x -C .scratch/d03/iso`
(69 MB). cwd `.scratch/d03/iso`.

| # | command | result | exit |
|---|---|---|---|
| 1 | `python3 -B tools/assemble-culture-d4.py --selftest` | `selftest: 81/81 checks passed` | 0 |
| 2 | `python3 -B tools/assemble-culture-d4.py --check` | `byte-identical deterministic assembly` | 0 |
| 3 | `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` | 0 |
| 4 | `python3 -B tools/gates/argot-derivation-gate.py --selftest` | `selftest: 27/27 checks passed` | 0 |
| 5 | `python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | `law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0` | 0 |
| 6 | `python3 -B tools/gates/register-law-gate.py --selftest` | `selftest: 45/45 checks passed` | 0 |
| 7 | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed` (incl. `ok L3b-argot`) | 0 |
| 8 | `python3 -B tools/gates/typed-pipeline-gate.py --selftest` | `selftest: 19/19 checks passed` | 0 |
| 9 | `python3 -B tools/assemble-d4-typed.py --check` | `byte-identical deterministic typed packet` | 0 |
| 10 | `python3 -B tools/assemble-d4-typed.py --selftest` | `selftest: 12/12 checks passed` | 0 |
| 11 | `python3 -B tools/gates/d4-assembly-check-gate.py` | `byte-identical deterministic assembly` | 0 |
| 12 | `python3 -B tools/gates/d4-typed-labels-check-gate.py` | `byte-identical deterministic projection` | 0 |
| 13 | `python3 -B tools/check-gate-battery.py` | `summary {battery_exit: 0, fail: 0, pass: 7, unevaluable: 0}`; `originals {modified: 0, preserved: true}` | 0 |
| 14 | `python3 -B tools/replay-frozen.py --selftest` | `selftest: 79/79 checks passed` | 0 |
| 15 | `python3 -B tools/replay-frozen.py reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` | `REPLAY OK: 4/4 rows reproduced the recorded verdicts` | 0 |

Baseline digests (sha256 first 16):

```
aac91246cede8840  examples/culture-d4/packet.d4.yml
ed7093d6b92111c2  examples/culture-d4/components/04-lexicon.yml
c0d77181ac567c4c  examples/culture-d4/components/13-register-law.yml
c23b0ab532cfb9d4  examples/culture-d4/typed-labels.d4.yml
d581e0ad5384ce56  examples/culture-d4/packet.d4.typed.yml
e6ae9828d6c82aa6  examples/culture-d4/expected-holds.json
76ecdfdcbf09c3c7  tools/gates/typed-pipelines.json
```

### 2.1 Two historical manifests replay red — both already filed as superseded

`tools/gates/frozen/round-26/post-register/MANIFEST.tsv` (2/6 mismatch) and
`reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv` (4/4 mismatch) replay red in
the isolated copy. **Not a new defect.** Both are filed as superseded at
`reports/round-32/final-sweep.md:164` ("superseded when the register law moved the D4
tree after its freeze (r27/r28)") and `:166` ("superseded 4/4 by the r30 QREG landing;
successor is `sweep/frozen/r31-post`"). The successor `r31-post` is 4/4 green (row 15).
Recorded so a later sweep does not re-file it.

## 3. Tamper controls — the register legs have teeth (baseline packet)

Probes are text transforms of the assembled packet under `.scratch-probe/`; the baseline
packet was never edited.

| probe | transform | argot gate output | exit |
|---|---|---|---|
| term tamper | `L-56 term: kit → kat` | `FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form L-56 'kat' (register 'stamp'): declared chain 'reverse' applied to 'tik' yields 'kit'; the stated inputs and rules do not yield the candidate`; `violations=1` | 1 |
| op tamper | `L-55 term: tuum → muut` | `FINDING D4L-ARGOT-DERIV: FAIL — … L-55 'muut' … declared chain 'lengthen' applied to 'tum' does not yield the candidate`; `violations=1` | 1 |
| law-row tamper | (selftest family) | `register-law-gate --selftest` 45/45 incl. `delivered-speaker-id-tamper-adds-a-line`, `delivered-consequence-tamper-adds-a-line` | 0 |
| domain emptied | remove the 8 `L-55..L-62` record blocks | `records=179 register_scoped=0 derived_pairs=0 claimed_chains=8 borrow_pairs=0 violations=0 rule_holds=0` | 0 |

Two honest readings:

1. **The derivation leg propagates.** The term-tampered packet fed to the typed gate
   yields `FAIL L3b-argot: argot leg exit 1: FINDING D4L-ARGOT-DERIV …` — the register
   leg is wired into the typed pipeline, not merely runnable beside it. (That run also
   reports `FAIL L1-assembler`, exit 2, because a hand-edited packet is by construction
   not the assembler's build — the assembler-identity fail-closed rule working.)
2. **An emptied domain is silent.** With all 8 pairs removed the gate exits 0 with
   `register_scoped=0`. The `D4L-ARGOT-COVERAGE` HOLD
   (`tools/gates/argot-derivation-gate.py:662-667`) is gated on
   `counters["register_scoped"]` being non-zero, and that counter is itself derived from
   the `registers`/`layers` declarations — so removing the *records* while the register
   block survives leaves the counter at 0 and no hold fires. **This is the r25 failure
   mode reproduced exactly**: a clean exit over an empty domain. Reported as an
   observation, not fixed — gate bytes are outside this seat's write scope.

## 4. The assigned mission — D01's Drafts 1 and 2 integrated in the isolated copy

Copy: `.scratch/d03/iso-d01` (`git archive ce103bf`). Applied exactly as D01's fenced
blocks specify, by text transform of `examples/culture-d4/components/04-lexicon.yml`:

- **Draft 1** (`D01-design.md:5.1`): `packet_keys` extended with `doublets`, and the
  8-row `doublets:` block inserted before `registers:`.
- **Draft 2** (`D01-design.md:5.2`): `register_form: L-nn` added to the 8 base records
  `L-02, L-09, L-16, L-37, L-38, L-39, L-42, L-43`.

### 4.1 Draft 1 alone

| step | command | result | exit |
|---|---|---|---|
| 1 | `assemble-culture-d4.py` | `Wrote examples/culture-d4/packet.d4.yml (103724 bytes)` | 0 |
| 2 | `assemble-culture-d4.py --check` | `byte-identical deterministic assembly` | 0 |
| 3 | parse packet | `doublets PRESENT: True`, **8 rows**, `DB-01 {plain_slot: L-02, register_form: L-55, register: stamp, owner: L-02, slot: register-form, op: lengthen, axis: fire}` | — |
| 4 | `argot-derivation-gate.py` | `records=195 register_scoped=14 derived_pairs=8 … violations=0 rule_holds=0` | 0 |
| 5 | `register-law-gate.py` | `law_rows=5 identity_rows=8 record_ids=191 … findings=0` | 0 |
| 6 | `typed-pipeline-gate.py` | `FAIL L1-profile: packet: pins aac91246cede, live 7c45ac1eef16` — the expected un-re-pinned state | 2 |

**D01's "no new assembler edit" claim is confirmed**: `doublets` is already in
`PACKET_KEYS` (`tools/assemble-culture-d4.py:81`) and `RECORD_FIELDS` (`:122`), and the
block reached the packet without touching any tool byte. `doublets` does **not** appear
in `assembly.skipped_keys`, i.e. it was merged, not dropped as metadata.

**Bidirectional consistency of the new block, checked against the record-level
pointers** (this seat's own cross-check):

```
doublets rows consistent with record-level doublet_of: 8/8; bad=[]
```

Every `doublets` row's `register_form` record does carry `doublet_of == plain_slot` and
`derived_from == the base's term`, so the new block agrees with the eight landed records
rather than restating them differently.

### 4.2 Draft 1 + Draft 2, and the full sweep

| step | command | result | exit |
|---|---|---|---|
| 1 | `assemble-culture-d4.py` | `Wrote examples/culture-d4/packet.d4.yml (103932 bytes)` | 0 |
| 2 | `assemble-culture-d4.py --check` | `byte-identical deterministic assembly` | 0 |
| 3 | `assemble-culture-d4.py --selftest` | `selftest: 81/81 checks passed` | 0 |
| 4 | parse packet | `register_form` present on all 8 bases (`L-02→L-55`, `L-09→L-59`, `L-16→L-58`, `L-37→L-61`, `L-38→L-57`, `L-39→L-62`, `L-42→L-56`, `L-43→L-60`) | — |
| 5 | `argot-derivation-gate.py` | `records=195 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` | 0 |
| 6 | `register-law-gate.py` | `law_rows=5 identity_rows=8 record_ids=191 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0` | 0 |
| 7 | `d2-typed-labels.py --emit` | `Wrote examples/culture-d4/typed-labels.d4.yml` | **1** |
| 8 | `d2-typed-labels.py --check` | `byte-identical deterministic projection` | 0 |
| 9 | `assemble-d4-typed.py --emit` | `Wrote … (110291 bytes, 12 routing row(s))` | 0 |
| 10 | pin re-freeze (§5) | converged after 1 pass | — |
| 11 | `assemble-d4-typed.py --check` | `byte-identical deterministic typed packet` | 0 |
| 12 | `typed-pipeline-gate.py` | `summary: 20/20 legs passed`, exit 0 | 0 |
| 13 | `d4-assembly-check-gate.py` | `byte-identical deterministic assembly` | 0 |
| 14 | `d4-typed-labels-check-gate.py` | `byte-identical deterministic projection` | 0 |
| 15 | `check-gate-battery.py` | `summary {battery_exit: 0, fail: 0, pass: 7, unevaluable: 0}`; `originals {modified: 0, preserved: true}` | 0 |

The typed gate's 12 findings are the expected `D2L-FORM-UNRESOLVED` holds on the six
unfilled garment slots (`GAR-01..06`) — the same count (`12`) the r31-post manifest
records, so the new content changed no hold count.

The emit exit **1** at step 7 is expected and documented: `d2-typed-labels.py` returns 1
when it emits the design's expected holds, and the following `--check` returns 0, proving
deterministic freshness (`reports/round-30/fixes/qreg-dangles.md:49` records the same
emit-1/check-0 pattern).

**D01's Draft-2 contract caveat is confirmed.** `register_form` is **not** in
`contract.record_fields.lexicon`:

```
contract.record_fields.lexicon has register_form: False
```

The assembler admits the field (a lexicon record is only required to carry
`id, term, gloss` — `RECORD_FIELDS["lexicon"]`), so it lands and survives to the packet;
but it is an **undeclared** field, exactly as D01 §5.2 warns. Draft 2 therefore owes a
one-line contract addition, or it is an undeclared-field landing. Draft 1 carries the
same information with no contract change — so D01's trade ("Draft 1 is the cheaper
landing, Draft 2 the optional navigability add-on") is borne out by measurement, and
this seat confirms the ordering.

### 4.3 The control D01 named for Draft 1 — the duplicate-slot row is silent

D01 §5.1 claims a ninth `doublets` row for an existing `(owner, slot)` "would be the
`D4L-DATA` control C-07, which no delivered code path emits today". Measured by
injecting `DB-09 {plain_slot: L-02, register_form: L-55, owner: L-02, slot: register-form}`
on top of Drafts 1+2:

```
assemble_exit=0                    (the duplicate is admitted; no collision failure)
argot-derivation-gate: records=196 register_scoped=14 derived_pairs=8 … violations=0 rule_holds=0   exit=0
register-law-gate:     law_rows=5 identity_rows=8 record_ids=192 … findings=0                        exit=0
```

**No finding of any class is emitted for the duplicate slot.** The cardinality invariant
the forecast asked for (Δ2, one form per `(owner, slot)`) is therefore *stated* by the
`doublets` block but **not enforced** anywhere in the delivered tree — the control C-07
has no live trigger, confirming D01 §3.3/§5.1 and extending it from "no code path emits
it" to "a concrete duplicate lands silently through assemble + both register legs + the
typed pipeline". The block is a declaration with named non-enforcement, and the fragment
records it as such rather than as a verified invariant.

### 4.3b P01's T-1 reproduced independently — the domain can shrink silently

P01 §3 reports four silent-acceptance classes, T-1 being "`L-56` deleted from the
component → `register_scoped=13 derived_pairs=7 … violations=0`, exit 0". Reproduced
here on a separate copy with the Drafts-1+2 component, deleting only the `L-56` record
line and re-assembling:

```
assemble: Wrote examples/culture-d4/packet.d4.yml (103424 bytes)     exit 0
argot-derivation-gate: records=194 register_scoped=13 derived_pairs=7 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0   exit=0
register-law-gate:     law_rows=5 identity_rows=8 record_ids=190 … findings=0                                                    exit=0
```

Confirmed, including the sharper detail: **`claimed_chains` stayed at 8 while
`derived_pairs` fell to 7**, and the two are never compared — so a register form
disappearing reads as *a smaller domain*, not a defect. The count is not pinned
anywhere outside the gate:

```
$ grep -rn "register_scoped\|derived_pairs" tools/ --include=*.py --include=*.json | sed 's/:.*//' | sort | uniq -c
      7 tools/gates/argot-derivation-gate.py
```

This corroborates P01's root cause independently and is the same class as §3's
empty-domain observation: the domain *size* is printed, never asserted. Both are gate
work, outside this seat's write scope.

### 4.4 The two row shapes — D01's and P01's both integrate

P01 §4.1 drafts the same `doublets` block with a different row shape (`plain` instead of
`plain_slot`, no `owner`/`slot`, plus `era: E1`). Applied on a third copy
(`.scratch/d03/iso-p01`):

| step | result | exit |
|---|---|---|
| `assemble-culture-d4.py` | `Wrote … (103308 bytes)` | 0 |
| `assemble-culture-d4.py --check` | `byte-identical deterministic assembly` | 0 |
| `argot-derivation-gate.py` | `records=195 register_scoped=14 derived_pairs=8 … violations=0 rule_holds=0` | 0 |
| `register-law-gate.py` | `law_rows=5 identity_rows=8 record_ids=191 … findings=0` | 0 |

**Both shapes assemble and grade identically clean**, so the choice between them is not
forced by any leg. It is a design decision (P01's shape carries the `era` field the law's
`RGL-05` names; D01's carries the forecast's `(owner, slot)` cardinality fields). Recorded
as a genuine either/or for the integrator, not averaged: this seat integrates and verifies
both and recommends neither, since P01 is the planner of record and D01 the drafting seat.

### 4.5 Independent re-derivation after the integration

Re-parsed the integrated packet and re-checked every pair from scratch: 8/8 clean, 0
self-derivations — unchanged by Drafts 1+2, i.e. the new blocks **add** the pair as a
first-class fact without altering the eight landed records' arithmetic.

## 5. The pin cascade — measured, for D04's re-pin list

A new packet top-level key fails closed at a named pin until every pin is re-frozen.
Measured on the first (un-repinned) Draft-1 rebuild:

```
FAIL L1-profile: packet: pins aac91246cede, live 7c45ac1eef16 (examples/culture-d4/packet.d4.yml)
FAIL projection_freshness: stale projection pin: projection records aac91246cede…, packet hashes 7c45ac1eef16…
examples/culture-d4/typed-labels.d4.yml differs from the deterministic projection
```

Pin census — every live (non-filed) surface that must move, before → after, for the
**Drafts 1+2** state (§4.2; D01's `doublets` block + the 8 `register_form` fields):

| # | surface | field | before (ce103bf) | after (Drafts 1+2) |
|---|---|---|---|---|
| 1 | `examples/culture-d4/components/04-lexicon.yml` | — (the source) | `ed7093d6b92111c2` | `0f0828731366ce52` |
| 2 | `examples/culture-d4/packet.d4.yml` | — (the artifact) | `aac91246cede8840` | `3067107f4a8df6d3` |
| 3 | `examples/culture-d4/typed-labels.d4.yml` | — (the artifact) | `c23b0ab532cfb9d4` | `606e44785071bb0f` |
| 4 | `examples/culture-d4/packet.d4.typed.yml` | — (the artifact) | `d581e0ad5384ce56` | `42986a6eb2b07721` |
| 5 | `examples/culture-d4/expected-holds.json` | `packet_sha256`, `projection_sha256` | `aac91246cede…`, `c23b0ab532cf…` | `3067107f4a8d…`, `606e44785071…` |
| 6 | `tools/gates/typed-pipelines.json` | `profiles[0].{packet,projection,expected}.sha256` | `aac91246cede…`, `c23b0ab532cf…`, `e6ae9828d6c8…` | `3067107f4a8d…`, `606e44785071…`, `4f17e8de5e42…` |
| 7 | `tools/gates/expected/register-law-gate/r30-post/expected.json` | `inputs[packet]` | `aac91246cede…` | **not moved by this rehearsal** |

**Unchanged** — the content change moves artifacts and pins, **never a tool**:
`tools/assemble-culture-d4.py` `943f487ba991d45d`,
`tools/assemble-d4-typed.py` `92f5460bcc34ffbb`,
`tools/d2-typed-labels.py` `2819f68769dfc0b5`,
`tools/gates/argot-derivation-gate.py` `b5406bcdaf41c595`,
`tools/gates/register-law-gate.py` `15f8b23251ca2ad0`,
`tools/gates/typed-pipeline-gate.py` `b749ad07cf171027`,
`tools/gates/naming-collision-gate.py` `d9e4e8f4f93a21b3`.

**The pin chain is self-referential and needs a second pass.** `expected-holds.json`
carries `packet_sha256`/`projection_sha256` but is *itself* pinned by
`typed-pipelines.json[].expected.sha256`; editing it moves its own digest. Measured on
the `L-63` rehearsal: pass 1 moved `packet`+`projection`, then reported
`FAIL L1-profile: expected: pins e6ae9828d6c8, live d18ce2659fc8`; pass 2 moved
`expected`; pass 3 reported `converged after 1 pass(es)`. A re-pin loop that does not
re-check after writing `expected-holds.json` leaves the tree red. Same self-referential
tool-pin subtlety r26 recorded for the v3 baseline (`SCORECARD.md:330`). On the Drafts
1+2 run the loop happened to converge in pass 1 (packet, projection and expected moved
together) — but the two-pass hazard is real and is the reason D04 should re-check, not
assume.

**Causality control.** On the **pristine** `.scratch/d03/iso-base` copy (never touched)
the successor manifest replays `REPLAY OK: 4/4 rows reproduced` exit 0. After the content
change it is `REPLAY MISMATCH: 4 mismatch, 0 reproduced` exit 1, because each row pins
the input digest `aac91246cede…` and snapshots its own input file. The red is caused by
the content change, not by the archive or the host. `r31-post` is therefore **superseded
by any accepted content landing** — D04's list should carry it as a new-row re-freeze,
exactly as the r26→r30 chain did.

## 5b. D02's component 14 integrated — the combined D01+D02 state

D02 landed mid-seat (`reports/round-36/depth/D02-packet-draft.md`, 35682 bytes): a
**new component 14** (`14-register-forms.yml`) declaring `packet_keys: [register_forms]`,
a new packet block indexing the eight delivered forms, plus an optional 4-line
`RECORD_FIELDS` diff. Copy: `.scratch/d03/iso-d02`, built by extracting D02's fenced
`yaml` block from its §3 verbatim.

### 5b.1 D02's central claim confirmed — one new component, **zero** assembler edits

With only component 14 added (no other change):

| step | result | exit |
|---|---|---|
| `assemble-culture-d4.py` | `Wrote … (104622 bytes)` | 0 |
| `assemble-culture-d4.py --check` | `byte-identical deterministic assembly` | 0 |
| `assemble-culture-d4.py --selftest` | `selftest: 81/81 checks passed` | 0 |
| parse packet | `register_forms PRESENT: True`, **8 rows**, top-level keys 39 → **40**; `RF-01 {form: tuum, authority: lexicon, lexicon_id: L-55, base: tum, base_id: L-02, op: lengthen, axis: fire, available_from: E1}` | — |
| `assembly.skipped_keys` | `register_forms` **absent** — merged, not dropped as per-file metadata | — |

So the `packet_keys:` bypass works exactly as D02 §2 argues, and `register_law` (already
in the packet while absent from `PACKET_KEYS`) is the correct precedent.

### 5b.2 D02's double-grading hazard — independently confirmed in its essential counts

D02 §1 reports that a `register_forms` row restating `form` **+** `derived_from` **+**
`derivation` is graded a second time (its table: `register_scoped` 14 → 22,
`derived_pairs` 8 → 16), and that a pointer-only row is graded once. Reproduced on the
combined tree, building the "full duplication" variant from D02's own block by injecting
each row's own `derived_from`/`derivation`:

```
pointer-only (D02's actual draft):  records=203 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0   exit 0
full duplication (probe):           records=203 register_scoped=22 derived_pairs=16 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=8   exit 1
```

**The counts D02 reports are confirmed exactly**: `14 → 22` and `8 → 16`; the eight
derivations are graded twice. **My probe additionally emitted 8 `D4L-ARGOT-RULE` HOLDs
that D02's table does not show** — and those are an artifact of *my* probe, not of D02's
draft: I rebuilt the variant from the parsed records and serialized `derivation` as a
flow string (`derivation: "{op: reverse, base: tik}"`), which the gate cannot read as a
mapping, so it reports the rule unreplayable. A faithful text-level injection (keeping
the block-scalar `derivation:` mapping D02's own bytes use) is what D02's table measures.
**Recorded explicitly so the divergence is not mistaken for a contradiction**: the
hazard's substance and both counts reproduce; the HOLD count is my probe's serialization,
not a property of D02's block.

D02's conclusion therefore stands: the index row must carry `form` + `op` but **never**
the `derived_from`/`derivation` pair, or the derivation relation is declared twice and
graded twice. That is the load-bearing shape constraint, and it is why D02's draft is
correct as written.

### 5b.3 The combined D01 Draft-1 + D02 component-14 state — final sweep

Both landings applied together (D02's component 14 **and** D01's `doublets` block +
`register_form` fields), pins re-frozen:

| step | result | exit |
|---|---|---|
| `assemble-culture-d4.py` | `Wrote … (106454 bytes)` | 0 |
| `assemble-culture-d4.py --check` | `byte-identical deterministic assembly` | 0 |
| `assemble-culture-d4.py --selftest` | `selftest: 81/81 checks passed` | 0 |
| `argot-derivation-gate.py` | `records=203 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` | 0 |
| `register-law-gate.py` | `law_rows=5 identity_rows=8 record_ids=199 registers=17 … findings=0` | 0 |
| `d2-typed-labels.py --emit` / `--check` | wrote / `byte-identical deterministic projection` | 1 / 0 |
| `assemble-d4-typed.py --emit` / `--check` | wrote (112813 bytes, 12 routing rows) / `byte-identical deterministic typed packet` | 0 / 0 |
| pin re-freeze | `pass 1: moved ['packet','projection','expected']` → `converged after 1 pass(es)` | — |
| `typed-pipeline-gate.py` | `summary: 20/20 legs passed` | 0 |
| `d4-assembly-check-gate.py` | `byte-identical deterministic assembly` | 0 |
| `d4-typed-labels-check-gate.py` | `byte-identical deterministic projection` | 0 |
| `check-gate-battery.py` | `{battery_exit: 0, fail: 0, pass: 7, unevaluable: 0}` | 0 |

**The two drafts are compatible and jointly green.** `register_scoped` stays **14** and
`derived_pairs` stays **8** in the combined state — i.e. adding the index block and the
`doublets` block does **not** inflate the graded domain, because both are pointer-shaped
and neither restates the derivation pair. That is the substantive verification result:
the design route D01 and D02 converged on is the one that keeps the domain honest.

Combined-state digests:

```
5231e73be696b020  examples/culture-d4/packet.d4.yml
9bd1c0f0d3851f41  examples/culture-d4/typed-labels.d4.yml
5b68aac56370a3a9  examples/culture-d4/packet.d4.typed.yml
76bbe4e861880cd9  examples/culture-d4/expected-holds.json
1d6eca829034354e  tools/gates/typed-pipelines.json
```

### 5b.4 D02's §2.1 field-validation gap — noted, not exercised

D02 §2.1 warns that a block absent from `RECORD_FIELDS` gets only the generic checks, so
a row missing `lexicon_id` or `op` would assemble silently. This seat did **not** run
that probe (the `RECORD_FIELDS` diff is a tool change the integrator applies, and the
gap is a property of the unmodified assembler that D02 already measured). It is carried
as an owed item rather than as this seat's evidence.

## 6. In-tree integrity

**This seat's write footprint.** The only path this seat created in-tree is
`reports/round-36/`. All mutation performed by this seat happened under
`.scratch/d03/` (gitignored via `.scratch/`); the only in-tree byte this seat wrote is
`reports/round-36/depth/D03-isolated-verify.md`. No `reports/round-*/run-validation.py`
was executed in-tree at any point (F-C13-1); no `--freeze` of
`reports/round-34/handoff/declared-in-r7` was issued.

**Observed transiently during the seat, NOT caused by this seat.** At one point in this
seat's run `git status --porcelain` reported, besides `?? reports/round-36/`:

```
 M reports/round-34/validation.json     (mtime 2026-10-19 06:31:01 -0300; 15 insertions, 11 deletions)
```

This seat never wrote outside `.scratch/d03/` and `reports/round-36/`, and never ran a
round runner, so the change was **another seat's or the parent's** live edit to a filed
round-34 artifact. **By the end of this seat's run that path was clean again** (final
`git status --porcelain` → `?? reports/round-36/` only), so it was a transient concurrent
write, not a standing drift. It is recorded because `reports/round-1..35/**` is
filed-bytes territory under the shared rules: if the round's own reconciliation expects
`reports/round-34/validation.json` to be byte-stable, the parent should confirm the
concurrent writer finished. **Owner: not this seat.** This seat did not touch or revert it.

## Owed

1. **D02's §2.1 field-validation gap** — a block absent from `RECORD_FIELDS` is not
   field-validated, so a `register_forms` row missing `lexicon_id` or `op` would assemble
   silently. D02 measured it; this seat did **not** exercise it (the fix is the 4-line
   `RECORD_FIELDS` diff, a tool change the integrator applies). Owner: whoever lands
   component 14. **Everything else of D02's is integrated and verified** (§5b).
2. **D07 independent verification of this file** — `reports/round-36/depth/D07-verify.md`.
   D07 should rebuild `.scratch/d03/iso-d02` from `git archive ce103bf` independently,
   apply D02's §3 block and D01 §5.1, and re-run §5b.3; this seat's own run is not
   independent verification.
3. **Claim D's verdict** — `after_required` is satisfied at the baseline by the r26
   closure (§1), but the claim's counting command is a round runner this seat may not
   execute. Whether claim D verifies as declared, or is re-scoped to the `doublets` /
   `register_forms` / base-side-pointer surface (§4, §5b), is the parent's decision.
   **Four seats (D01, K01, D02, D03) have now measured the stale premise**, and P01
   re-aimed the plan on it — so the premise correction is corroborated, not one seat's
   reading.
4. **The block shape is an open either/or** — D01's `doublets` block (with
   `plain_slot` + `owner`/`slot`) and D02's `register_forms` block (with
   `lexicon_id`/`base_id`/`authority`) are **two different first-class blocks indexing
   the same eight pairs**, and P01's Surface-A row shape is a third variant. All three
   were integrated and all grade identically clean (§4.4, §5b.3). Landing two index
   blocks would be redundant; the integrator must pick one. This seat verifies all three
   and recommends none, since P01 is the planner of record.
5. **Draft 2's contract line** — `register_form` is not in
   `contract.record_fields.lexicon` (§4.2). Landing Draft 2 without that one-line
   addition ships an undeclared field. P01 prices it as a contract amendment and does
   not recommend it (Surface B-1 instead). Owner: whoever lands Draft 2.
6. **The unenforced invariants** — (a) the empty-domain clean exit (§3), (b) the silent
   duplicate-slot row (§4.3), (c) the silent domain shrink with `claimed_chains`
   diverging from `derived_pairs` (§4.3b), (d) the double-grading of a restated
   derivation (§5b.2, which is a *shape* constraint rather than a defect — the gate
   grades what it is given, twice, and is right to). (a)–(c) are gate/leg work, outside
   this seat's write scope. P01 §4.3 drafts the guard (Surface C) that would close them.
   Owners: whichever seat owns gate changes, or a future round. Recorded, not fixed.
7. **D04's re-pin list** — §5 gives the measured list for the D01 route, the two-pass
   requirement and the `r31-post` supersession; §5b.3 adds the combined-state digests.
   D04 owns the new-row draft; not written by this seat.

## 7. Reproduce

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
mkdir -p .scratch/d03/iso-d01 && git archive ce103bf | tar -x -C .scratch/d03/iso-d01
cd .scratch/d03/iso-d01
# apply D01 §5.1 (packet_keys + the 8-row doublets block) and §5.2 (8 register_form fields)
python3 -B tools/assemble-culture-d4.py && python3 -B tools/assemble-culture-d4.py --check
python3 -B tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --emit examples/culture-d4/typed-labels.d4.yml
python3 -B tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml
python3 -B tools/assemble-d4-typed.py --emit examples/culture-d4/packet.d4.typed.yml
# re-freeze pins: expected-holds.json {packet,projection}_sha256, then typed-pipelines.json
#   profiles[0].{packet,projection,expected}.sha256 — re-check until converged
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/gates/d4-assembly-check-gate.py
python3 -B tools/gates/d4-typed-labels-check-gate.py
python3 -B tools/check-gate-battery.py
```

Expected: `records=195 … derived_pairs=8 violations=0` (argot, exit 0);
`law_rows=5 … findings=0` (law, exit 0); `summary: 20/20 legs passed` (typed, exit 0);
both d4 gates `byte-identical`; battery `pass 7, fail 0`.

Combined D01+D02 state (§5b.3):

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
mkdir -p .scratch/d03/iso-d02 && git archive ce103bf | tar -x -C .scratch/d03/iso-d02
cd .scratch/d03/iso-d02
# write D02's fenced yaml block (its section 3) to
#   examples/culture-d4/components/14-register-forms.yml
# then apply D01 section 5.1 (packet_keys + the 8-row doublets block) to 04-lexicon.yml
python3 -B tools/assemble-culture-d4.py && python3 -B tools/assemble-culture-d4.py --check
python3 -B tools/assemble-culture-d4.py --selftest
python3 -B tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --emit examples/culture-d4/typed-labels.d4.yml
python3 -B tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml
python3 -B tools/assemble-d4-typed.py --emit examples/culture-d4/packet.d4.typed.yml
# re-freeze pins (expected-holds.json, then typed-pipelines.json) until converged
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/check-gate-battery.py
```

Expected: `records=203 register_scoped=14 derived_pairs=8 violations=0` (argot, exit 0);
`law_rows=5 … record_ids=199 findings=0` (law, exit 0); `summary: 20/20 legs passed`
(typed, exit 0); battery `pass 7, fail 0`; packet digest `5231e73be696b020…`.

## Citations

**Files read (in-tree, ce103bf)**
- `REGIMEN.md`; `reports/round-36/claims.json`; `reports/round-36/targets.json`; `reports/round-36/telemetry/{dispatch-declared,availability-attempt-1}.json`
- `reports/round-36/depth/D01-design.md:13-18,23-66,68-123,124-180,231-330` (Drafts 1+2 integrated in §4)
- `reports/round-36/depth/D02-packet-draft.md:9-60,67-105,105-255,255-284,322-383` (the component-14 block integrated in §5b, the double-grading hazard reproduced in §5b.2, the `RECORD_FIELDS` gap)
- `reports/round-36/plan/P01-d-plan.md:28-62,115-175,174-215,323-333,360` (Surface A/B-1/B-2, the four silent-acceptance classes, the row shape tested in §4.4)
- `reports/round-36/scout/K01-register-scout.md:1-40` (independent stale-premise finding, SCORECARD lineage)
- `reports/round-25/argot/{current-state.md:74-88,delta.md:52-56,forecast.md:3-56}`; `reports/round-25/claims.json`; `SCORECARD.md:312`
- `reports/round-26/register/{design,forms,rules,review}.md`; `reports/round-26/report-draft.md:26,29`; `reports/round-26/register/impl.md` §7
- `reports/round-27/law/{design,rules,review,impl-1}.md`; `reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv`
- `reports/round-28/claims.json`; `reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv`
- `reports/round-29/recount/{audit.md,C05,C06,C07,C08,C09}.md`
- `reports/round-30/loop3-retrospective.md:27,80-105`; `reports/round-30/fixes/qreg-dangles.md:21,31,49,58,129,175`
- `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv`; `reports/round-32/final-sweep.md:157-166`; `SCORECARD.md:330`
- `examples/culture-d4/components/04-lexicon.yml:14,22,236-254`; `examples/culture-d4/components/13-register-law.yml`; `examples/culture-d4/components/02-phonology.yml:117-124`
- `tools/assemble-culture-d4.py:75-130` (`PACKET_KEYS`, `RECORD_FIELDS`); `tools/gates/argot-derivation-gate.py:1-90,562-667`; `tools/gates/register-law-gate.py:1-160`; `tools/gates/typed-pipeline-gate.py:1551-1562`; `tools/assemble-d4-typed.py:1-60`; `tools/d2-typed-labels.py:3497-3528,3595-3605`; `tools/gates/typed-pipelines.json`; `tools/gates/expected/register-law-gate/r30-post/expected.json`

**Commands** — all in the isolated copies named in §0, tabulated verbatim in §2, §3,
§4 and §5. Digests by `sha256sum`; integrity by `git status --porcelain` and
`git diff --stat HEAD -- reports examples corpus tools`.

**Scratch (gitignored, not evidence by itself)**: `.scratch/d03/{iso,iso-base,iso-d01}/`,
`.scratch/d03/iso*/.scratch-probe/`.

**Canon**: NON-CANON. This file records an engineering rehearsal and its measurements; it
makes no promotion, canon, clearance or closure verdict. The integrated content is a
fenced draft applied **only inside `.scratch/`**; the in-tree `04-lexicon.yml` is
unmodified.
