- Seat: D01 | executor | claim D (depth) | date 2026-10-19 | baseline ce103bf

# D01 — the register-form component content: what the claim asks for, what is already
delivered, and the design for the surface that is genuinely open

- **Seat:** D01 (executor, claim **D**), round 36, loop 1, position 4.
- **Mission (binding, `reports/round-36/targets.json`):** "Design the register-form component
  content (fenced draft): the form records, their fields, and the derivation pairs, per P01."
- **Baseline:** `ce103bf5885af00023cdc4a174c17602476cdcf8` (`git rev-parse HEAD`).
- **Write scope:** this file only. No tool, gate, packet, component, pin, or filed 1–35 byte
  written; no commit, no push. Every command ran with
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` from the lane root.
- **Dependency note:** the mission says "per P01", but neither `reports/round-36/plan/P01-d-plan.md`
  nor `reports/round-36/scout/K01-register-scout.md` exists at write time
  (`ls reports/round-36/` → `claims.json  targets.json  telemetry`). This seat therefore derives
  its plan from the **filed** sources the claim names (`reports/round-25/argot/`,
  `reports/round-26/register/`, `reports/round-27/law/`) rather than from P01's fragment. If P01
  lands a different component/packet shape, this design is subordinate to it — recorded under
  `## Owed`.
- **Canon:** NON-CANON engineering design. No real language, institution, script or argot is
  described, cited or approximated. No clearance claimed.

## 0. Headline — the claim's `before` is stale: the register-form domain is NOT empty

Claim D's `before` reads:

> "Register-form domain empty (`reports/round-25/argot/` + SCORECARD r25 row); register law/strata
> exist but the form class has no instances"

That was true at round 25. **It is false at baseline `ce103bf`.** The domain was closed by round 26
(the `stamp` stratum landing) and extended by round 30 (the QREG amendment), and both rounds are
ancestors of this round's baseline. Measured this seat:

```
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
exit=0
```

`derived_pairs=8` — eight register forms are **delivered and replay clean**. The landing history:

```
$ git log --oneline -S "register: stamp" -- examples/culture-d4/components/04-lexicon.yml
11df1fd round-30 wave integration: QREG landing, speaker candidate, law baseline, craft synthesis draft, telemetry
4f09c99 round-26: admit D/O/C — register stratum closes the r17 forecast; r5 pin chain (devin)
```

| the claim's `before` asserts | measured at `ce103bf` | evidence |
|---|---|---|
| register-form domain empty | **8 register records delivered** (L-55..L-62) | `04-lexicon.yml:236-243`; packet `lexicon` rows at `packet.d4.yml:1019-1178` |
| "the form class has no instances" | 8 instances, each with `register: stamp` | `grep -c "register: stamp" examples/culture-d4/components/04-lexicon.yml` → 16 (8 records × 2: record + law rows) |
| register law/strata "exist" | law **and** forms both delivered: `registers:` (8 QREG rows) + `register_law:` (RGL-01..05) | `packet.d4.yml:1329`, `:2788` |
| the checking legs needed | green: argot gate exit 0, law gate exit 0, typed gate 20/20, battery 7 pass | §2 below |

So **claim D's `after_required` is already satisfied at the baseline** ("register-form domain
non-empty with verified forms (derivation replay clean over the new forms; law gate exit 0 over
them…)"). This seat did not build it and does not claim it. The honest reading is that D's premise
survived from the r25 record and was not re-measured when the claim was written; `SCORECARD.md:329`
(the r26 row) already records the closure.

**Consequence for this fragment.** Drafting the eight form records again would be dead work that
duplicates filed bytes. So this design (a) records the stale premise with citations, and (b) designs
the register-form surface that **is** genuinely open at `ce103bf`: the `doublets:` block, the
base-side pointer, and the two unimplemented legs the r26/r27 designs named. That is the part of
claim D that can still move the depth axis.

## 1. What is delivered, exactly (so the design does not duplicate it)

Measured, not read from the claim.

### 1.1 The eight form records

`examples/culture-d4/components/04-lexicon.yml:236-243` (sha256 `ed7093d6b92111c2…`), landed r26,
carried into the packet at `packet.d4.yml:1008-1178`:

| record | base | axis | op | form | `doublet_of` | packet line |
|---|---|---|---|---|---|---|
| L-56 | `tik` (L-42) | mark | reverse | `kit` | L-42 | `:1019` |
| L-57 | `mol` (L-38) | mark | reverse | `lom` | L-38 | `:1041` |
| L-55 | `tum` (L-02) | fire | lengthen | `tuum` | L-02 | `:1063` |
| L-58 | `nes` (L-16) | fire | lengthen | `nees` | L-16 | `:1085` |
| L-59 | `hum` (L-09) | fire | lengthen | `huum` | L-09 | `:1107` |
| L-60 | `mes` (L-43) | fire | lengthen | `mees` | L-43 | `:1129` |
| L-61 | `rek` (L-37) | fire | lengthen | `reek` | L-37 | `:1151` |
| L-62 | `sam` (L-39) | fire | lengthen | `saam` | L-39 | `:1173` |

Each carries the full field set the claim asks for — `register: stamp`, `derived_from`,
`derivation: {op, base}`, `doublet_of`, `bases`, `construction: STAMP-REVERSE|STAMP-LENGTHEN`,
`stage: E1` — and the contract already admits every one of them
(`packet.d4.yml:30-44`, `contract.record_fields.lexicon` includes `register`, `derived_from`,
`derivation`, `doublet_of`). **No schema work is owed for the forms.**

### 1.2 The two operations and the declared rule

`04-lexicon.yml:98-121` declares `STAMP-REVERSE` (mark → reverse) and `STAMP-LENGTHEN`
(fire → lengthen); `:263-269` declares the machine-readable `lengthen` row
(`^(?P<onset>[^aeiou]*)(?P<vowel>[aeiou])(?P<rest>.*)$` → `{onset}{vowel}{vowel}{rest}`, `:267`) plus
`derivation_ops: [head2, reverse, lengthen]` (`:269`). The gate computes `reverse`/`head2` as functions
(`OP_FUNCTIONS`, `tools/gates/argot-derivation-gate.py:243`) and replays `lengthen` from the packet.

### 1.3 The law

`packet.d4.yml:1329` `registers:` (QREG-01..08) and `:2788` `register_law:` (RGL-01..05);
`register-law-gate.py` over the delivered packet:

```
coverage: examples/culture-d4/packet.d4.yml law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0
exit=0
```

## 2. The four legs, re-run on the delivered revision (the claim's own thresholds)

| # | leg | command | result | exit |
|---|---|---|---|---|
| V-1 | derivation replay | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `derived_pairs=8 violations=0 rule_holds=0` | 0 |
| V-2 | replay selftest | `… argot-derivation-gate.py --selftest` | `27/27 checks passed` | 0 |
| V-3 | law gate | `python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | `findings=0` | 0 |
| V-4 | typed pipeline | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml \| tail -1` | `summary: 20/20 legs passed` | 0 |
| V-5 | gate battery | `python3 tools/check-gate-battery.py \| tail -6` | `pass 7, fail 0, unevaluable 0` | 0 |

Every leg claim D's `after_required` names is green **at the baseline**, over the delivered forms.

## 3. The genuinely-open surface (what this design drafts)

Three gaps remain, all measured. They are what a claim-D round can still deliver.

### 3.1 Gap A — the `doublets:` block is absent (the forecast's Δ2)

The forecast asked for `doublets` as a packet fact with `slot_ref`/`doublet_of` as the slot
cardinality mechanism (`design-brief.md:283-295`, control C-07 "two supplied forms in one slot →
exit 2 `D4L-DATA`"). The assembler **admits** the block — `PACKET_KEYS` includes `"doublets"`
(`tools/assemble-culture-d4.py:81`), `RECORD_FIELDS["doublets"] = ("id",)` (`:122`), and the
assembler's own fixture template emits a `doublets:` block (`:469-471`) — but:

```
$ grep -c "doublets" examples/culture-d4/packet.d4.yml          # 0
$ for f in examples/culture-d4/components/*.yml; do grep -c 'doublets' $f; done   # 0 for all 13
```

So the block is **representable and unpopulated**. The pair relation exists only as the eight
forward pointers `doublet_of: L-42` etc. on the register records.

### 3.2 Gap B — the base-side pointer is missing (the relation is one-directional)

Each register record points back at its base (`doublet_of: L-42`), but no base record points
forward at its register form:

```
$ grep -c "doublet_of" examples/culture-d4/components/04-lexicon.yml   # 9 = 8 records + 1 comment
$ grep -n "{id: L-42," examples/culture-d4/components/04-lexicon.yml
205:  - {id: L-42, term: tik, ... axis: mark, ...}    # no `doublet_of`, no forward pointer
$ grep -n "{id: L-02," examples/culture-d4/components/04-lexicon.yml
156:  - {id: L-02, term: tum, ... axis: fire, ...}    # no `doublet_of`, no forward pointer
```

Consequence: a consumer reading a **plain** record cannot tell whether a register form exists for
it without scanning all 62 records. The r26 design's own frame ("a record carries a register pair
`<id>#plain` / `<id>#quote`", forecast Δ1) expects the pair to be a property of the pair, not a
one-way edge. This is the cheapest honest depth move: the eight pairs are already known.

### 3.3 Gap C — two legs the r26/r27 designs named are still unimplemented

`reports/round-27/law/rules.md:1` §1 lists six register rules, of which only `RLAW-06`
(derivation) has an executable owner. Two are directly leg-shaped and both are unimplemented:

```
$ grep -c "D4L-ERA" tools/gates/argot-derivation-gate.py    # 0  (no era concept in the gate)
$ grep -rl "D4L-REGISTER-UNRESOLVED" tools/ examples/ | wc -l   # 0 (no code path emits it)
```

- **RLAW-04 / REGISTER-ERA-01 (era leg):** a `stamp` record at `stage: E0` should be `D4L-ERA`.
  The r26 control C-E1 was measured and produced **no finding** (`reports/round-26/register/rules.md`
  §5). All eight delivered forms are `stage: E1`, so the control has no live trigger — but the
  mechanism is owed.
- **RLAW-05 (inventory leg):** "the register owns no segment; a `stamp` form is inventory-checked
  exactly as a plain form". The gate has no inventory leg (its `is_legal_syllable` grades the
  `head2` syllabifier, not record forms).

Both are named-and-unowned in filed bytes; neither is this seat's to write (tools are drafted as
fenced blocks, integrator applies).

## 4. The measured refinement that matters for any future form set — the rule's productive
domain is shrinking

The r26 review filed "13 of 54 unusable" for the axis→operation rule
(`reports/round-26/register/review.md` §3, finding RD-2). That figure is a **pre-landing forecast**
and it is now wrong in a way that is structural, not incidental. Re-measured this seat over the 54
base records (records with no `derived_from`), applying the same three checks r26 applied — legality
under PHON-01, collision with a delivered term, collision with the D2B-03 fixture ledger
(`04-lexicon.yml:22`):

```
bases: 54   usable: 32   unusable: 22
```

The r26 filed 13 unusable rows are **all still unusable** (`mine − r26` contains all 13; the
comparison is exact). The **nine new** unusable rows are the eight bases whose derived form the r26
landing then spent, plus one the landing's own re-check did not carry:

| base | r26 verdict | now | why |
|---|---|---|---|
| L-02 `tum` | usable (`tuum`) | **unusable** | `tuum` is landed as L-55 |
| L-09 `hum` | usable (`huum`) | **unusable** | `huum` is landed as L-59 |
| L-16 `nes` | usable (`nees`) | **unusable** | `nees` is landed as L-58 |
| L-37 `rek` | usable (`reek`) | **unusable** | `reek` is landed as L-61 |
| L-38 `mol` | usable (`lom`) | **unusable** | `lom` is landed as L-57 |
| L-39 `sam` | usable (`saam`) | **unusable** | `saam` is landed as L-62 |
| L-42 `tik` | usable (`kit`) | **unusable** | `kit` is landed as L-56 |
| L-43 `mes` | usable (`mees`) | **unusable** | `mees` is landed as L-60 |
| L-45 `tikmes` | not in r26's 13 | **unusable** | reverse → `semkit`, an onset cluster (`sk`), illegal under PHON-01 |

Arithmetic check: 54 − 13 (r26 unusable) = 41 usable at r26; 41 − 9 = **32**, which is the measured
value. So the rule is **self-limiting**: every register form landed consumes one previously-productive
base, because the derived form then collides with a delivered form under the rule's own collision
check. A future round that wants a larger stratum has at most 32 bases left before it must either
accept collisions or change the rule (an amendment).

**Honesty note on the two candidate figures.** A narrower reading of the r26 check (legality +
delivered-term collision only, without the D2B-03 ledger term) gives **33 usable / 21 unusable** and
the same eight spent bases but not L-45. The 32/22 figure is the one that reproduces r26's own
method exactly, so it is the figure this fragment reports; the 33/21 variant is named so the
difference is not mistaken for noise. Both readings agree on the structural point and on the eight
spent bases.

This is the one genuinely new, falsifiable depth measurement this seat contributes, and it is a
correction of a **filed** figure — reported, not silently smoothed (`REGIMEN.md`: "a trade is
reported, never averaged into an accept").


## 5. The design, as a fenced draft (the integrator applies; this seat writes no component bytes)

Two additive changes, both inside the assembler's existing contract, neither disturbing a CX rule
(so `morphology.derivation_rules`'s three delivered rows keep their bytes).

### 5.1 Draft 1 — the `doublets:` block, declared by `04-lexicon.yml`

The pair relation is already fully determined by the eight landed records; this block makes it a
first-class packet fact (forecast Δ2) and gives the base side its forward pointer.

```yaml
# fenced draft — for reports/round-36 integration; NOT applied by this seat
# site: examples/culture-d4/components/04-lexicon.yml
# change 1: extend the top-level declaration (currently:
#   packet_keys: [lexicon, constructions, layers, morphology, registers])
packet_keys: [lexicon, constructions, layers, morphology, registers, doublets]

# change 2: add the block. One row per register pair, in base-id order.
# `plain_slot` names the base record; `register_form` names the register record;
# `register` names the marked variety. `owner` and `slot` carry the forecast's
# Δ1/Δ2 cardinality fields so the pair is addressable as (owner, slot).
doublets:
  - {id: DB-01, plain_slot: L-02, register_form: L-55, register: stamp, owner: L-02, slot: register-form, op: lengthen, axis: fire, evidence: design-choice, follows: [F-2]}
  - {id: DB-02, plain_slot: L-09, register_form: L-59, register: stamp, owner: L-09, slot: register-form, op: lengthen, axis: fire, evidence: design-choice, follows: [F-2]}
  - {id: DB-03, plain_slot: L-16, register_form: L-58, register: stamp, owner: L-16, slot: register-form, op: lengthen, axis: fire, evidence: design-choice, follows: [F-2]}
  - {id: DB-04, plain_slot: L-37, register_form: L-61, register: stamp, owner: L-37, slot: register-form, op: lengthen, axis: fire, evidence: design-choice, follows: [F-2]}
  - {id: DB-05, plain_slot: L-38, register_form: L-57, register: stamp, owner: L-38, slot: register-form, op: reverse, axis: mark, evidence: design-choice, follows: [F-2]}
  - {id: DB-06, plain_slot: L-39, register_form: L-62, register: stamp, owner: L-39, slot: register-form, op: lengthen, axis: fire, evidence: design-choice, follows: [F-2]}
  - {id: DB-07, plain_slot: L-42, register_form: L-56, register: stamp, owner: L-42, slot: register-form, op: reverse, axis: mark, evidence: design-choice, follows: [F-2]}
  - {id: DB-08, plain_slot: L-43, register_form: L-60, register: stamp, owner: L-43, slot: register-form, op: lengthen, axis: fire, evidence: design-choice, follows: [F-2]}
```

Notes the integrator needs:

- **No new assembler edit.** `doublets` is already in `PACKET_KEYS` and `RECORD_FIELDS`
  (`assemble-culture-d4.py:81,122`); `RECORD_FIELDS["doublets"] = ("id",)` requires only `id`.
- **Cardinality.** The eight rows are one-per-`(owner, slot)` by construction — the forecast's Δ2
  invariant. A ninth row for an existing `(owner, slot)` would be the `D4L-DATA` control C-07, which
  no delivered code path emits today (§3.3).
- **Read-set exposure.** `doublets` would be a **new packet top-level key**, so the packet digest
  moves and every pin reading `packet.d4.yml` drifts — the r26 landing's own `repin.json` records
  that cascade (`reports/round-26/register/impl.md` §7: `expected-holds.json`,
  `tools/gates/typed-pipelines.json` profile `d4`, and the filed round-22 v3 read-set). D04's
  re-pin list owns this; this seat names it so it is not discovered late. The r7 freeze read set
  (`reports/round-34/handoff/declared-in-r7/freeze.txt`: "read set: 58 files; component digests
  26/26; d4 pins 8/8") is a **filed** artifact and must not be re-frozen
  (`REGIMEN.md` / `claims.json` non-goals; the ABSOLUTE rule).

### 5.2 Draft 2 — the base-side pointer on the eight base records

Independent of Draft 1, the eight base records can carry the forward pointer, making the relation
navigable in both directions:

```yaml
# fenced draft — eight one-field additions, site: examples/culture-d4/components/04-lexicon.yml
# each base record gains: register_form: <the register record id>
  - {id: L-02, term: tum, ..., register_form: L-55}   # line 156
  - {id: L-09, term: hum, ..., register_form: L-59}   # line 165
  - {id: L-16, term: nes, ..., register_form: L-58}   # line 173
  - {id: L-37, term: rek, ..., register_form: L-61}   # line 199
  - {id: L-38, term: mol, ..., register_form: L-57}   # line 200
  - {id: L-39, term: sam, ..., register_form: L-62}   # line 201
  - {id: L-42, term: tik, ..., register_form: L-56}   # line 205
  - {id: L-43, term: mes, ..., register_form: L-60}   # line 206
```

Caveat: `register_form` is **not** in `contract.record_fields.lexicon` today
(`packet.d4.yml:30-44`), so Draft 2 owes a one-line contract addition or it would be an undeclared
field. Draft 1 (the `doublets` block) carries the same information **without** a contract change,
because `doublets` is already admitted — so Draft 1 is the cheaper landing and Draft 2 is the
optional navigability add-on. This is a genuine trade, stated not averaged.

### 5.3 Draft 3 — the two unimplemented legs, as specs (tools are integrator-applied)

Not component bytes: the fenced shape of the two legs named in §3.3, so a later round has a
starting point rather than a re-derivation.

```text
# fenced draft — leg spec for tools/gates/argot-derivation-gate.py (owner: whoever grows the leg)
# REGISTER-ERA-01 (RLAW-04), the era leg:
#   for each lexicon record with register in MARKED_REGISTERS:
#     if record.stage < "E1"  ->  FINDING D4L-ERA: FAIL —
#         register-scoped form <id> '<term>' (register '<register>') is claimed at
#         stage '<stage>'; the register is available_from E1
#   control C-E1 (r26 rules.md §5): a probe with every stage: E1 -> E0 must emit 8 findings, exit 1.
#   delivered-packet expectation: 0 findings (all 8 landed forms are stage E1).
#
# INVENTORY leg (RLAW-05):
#   for each register form: re-check it against phonology (template (C)V(V)(C),
#   codas [n,m,s,k,l,r,t,d] per 02-phonology.yml PHON-01, onset_clusters: false,
#   identical_syllables: none) exactly as a plain form.
#   a violation -> FINDING D4L-ARGOT-DATA: FAIL
#   delivered-packet expectation: 0 findings (all 8 forms are inventory-legal — r26 forms.md §1).
```

## 6. Honest limits

- **L-1.** This seat did not run `reports/round-36/run-validation.py` (it does not exist yet, and
  the ABSOLUTE rule forbids in-tree runner execution). All verification above is per-leg on the
  delivered revision; the round-level runner is S01's spec.
- **L-2.** The claim's `counting_commands` name `reports/round-36/run-validation.py`; since it is
  absent, the per-leg commands in §2 stand in as the measured evidence. Recorded, not smoothed.
- **L-3.** §4's 32/54 figure (and the 33/21 narrow variant) is this seat's arithmetic over the
  component's text (regex-parsed); it is a **single-seat** measurement and claim D's threshold
  requires "verified by two independent seats". D07/D08's independent census is the second read;
  until it lands this is `to-verify` at the claim level.
- **L-4.** The r26 filed "13 of 54" is **not** edited — it is a filed byte (`reports/round-26/**`).
  §4 records the correction as a new statement with its own provenance, per `AGENTS.md`
  ("Corrections and final-wave updates are new snapshots or rows with their own provenance").
- **L-5.** Drafts 1–3 are **fenced drafts**, not applied. No component, tool, packet or pin byte was
  written by this seat.

## Owed

- `reports/round-36/plan/P01-d-plan.md` — the plan this mission is "per"; absent at write time. This
  design derives its shape from filed r25/r26/r27 bytes instead. If P01's plan differs (e.g. a new
  component rather than an amendment to `04-lexicon.yml`), the drafts in §5 are subordinate.
- `reports/round-36/depth/D02-packet-draft.md` — the packet `register_form`/`doublets` block bytes
  and the `tools/assemble-culture-d4.py` diff if a new component is chosen; D02 owns that.
- `reports/round-36/depth/D04-repin.md` — the pin re-freeze list for the new `doublets` key (§5.1
  read-set exposure); D04 owns that.
- `reports/round-36/depth/D07-verify.md` — the independent second census of §4's 32/54 (claim D
  threshold: "verified by two independent seats").

## Citations

Every claim above carries a file:line or a command output. Commands ran from the lane root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

**Baseline and digests**

```
$ git rev-parse HEAD
ce103bf5885af00023cdc4a174c17602476cdcf8
$ sha256sum examples/culture-d4/components/04-lexicon.yml examples/culture-d4/packet.d4.yml \
            examples/culture-d4/packet.d4.typed.yml tools/gates/argot-derivation-gate.py \
            tools/gates/register-law-gate.py
ed7093d6b92111c2300e7c04b9100f9e57f6d5802101b69335f9fe138858755d  examples/culture-d4/components/04-lexicon.yml
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182  examples/culture-d4/packet.d4.typed.yml
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
```

**§0 the stale premise**

```
$ git log --oneline -S "register: stamp" -- examples/culture-d4/components/04-lexicon.yml
11df1fd round-30 wave integration: QREG landing, speaker candidate, law baseline, craft synthesis draft, telemetry
4f09c99 round-26: admit D/O/C — register stratum closes the r17 forecast; r5 pin chain (devin)
$ grep -c "register: stamp" examples/culture-d4/components/04-lexicon.yml      # 16
$ grep -n "term: tuum\|term: kit\|term: lom" examples/culture-d4/components/04-lexicon.yml
236:  - {id: L-56, term: kit, ...}
237:  - {id: L-57, term: lom, ...}
238:  - {id: L-55, term: tuum, ...}
```

Filed records of the closure: `SCORECARD.md:329` (r26 row: "The round-17 register forecast CLOSED"),
`SCORECARD.md:312` (r25 row: the empty-domain statement this claim's `before` quotes),
`reports/round-25/argot/delta.md` §8.3, `reports/round-26/register/impl.md`.

**§1 delivered forms and fields**

```
$ grep -n "register:\|derived_from\|doublet_of" examples/culture-d4/packet.d4.yml | head -20
1019:    register: "stamp"     1020:    derived_from: "tik"     1024:    doublet_of: "L-42"
...
$ sed -n '30,44p' examples/culture-d4/packet.d4.yml     # contract.record_fields.lexicon
    lexicon:
      - "id" ... - "register" - "derived_from" - "derivation" - "doublet_of" ...
```

**§2 the four legs** — command outputs quoted verbatim in the §2 table; exits 0 for V-1..V-5.

**§3.1 the absent `doublets` block**

```
$ grep -c "doublets" examples/culture-d4/packet.d4.yml                              # 0
$ for f in examples/culture-d4/components/*.yml; do grep -c 'doublets' $f; done     # 0 (all 13 files)
$ sed -n '81p;122p;469,471p' tools/assemble-culture-d4.py
    "registers", "doublets", "sayings", "oaths",
    "doublets": ("id",),
doublets:
  - id: DB-01
    plain_slot: L-01#plain
```

Forecast authority: `reports/round-17/d4/design-brief.md:283-295` (Δ2), `:461-462` (controls C-07/C-08).

**§3.2 the one-directional relation**

```
$ grep -c "doublet_of" examples/culture-d4/components/04-lexicon.yml     # 9
$ sed -n '205p' examples/culture-d4/components/04-lexicon.yml
  - {id: L-42, term: tik, ..., axis: mark, evidence: design-choice, etymology: "underived root; the attestation institution in one word", follows: "craft-artisan-lexicon.md §6"}
```

**§3.3 the two unimplemented legs**

```
$ grep -c "D4L-ERA" tools/gates/argot-derivation-gate.py                   # 0
$ grep -rl "D4L-REGISTER-UNRESOLVED" tools/ examples/ | wc -l             # 0
$ grep -n "OP_FUNCTIONS\|CODAS" tools/gates/argot-derivation-gate.py
136:CODAS = frozenset("nmsklrtd")
243:OP_FUNCTIONS = {"head2": op_head2, "reverse": op_reverse}
```

Filed authority: `reports/round-27/law/rules.md` §1 (RLAW-01..06; only RLAW-06 replayable),
`reports/round-26/register/rules.md` §5 (C-E1 no finding), `reports/round-26/register/review.md`
§6 (RL-8, the missing legs).

**§4 the 32/54 refinement** — the measurement script (scratch, not promoted):

```python
# regex-parse the lexicon block; bases = records with no derived_from;
# lengthen = double the first nucleus; reverse = string reversal;
# unusable = illegal under PHON-01 (codas n m s k l r t d, no clusters)
#            OR collides with a delivered term OR collides with the D2B-03 fixture ledger
bases: 54   usable: 32   unusable: 22
# the narrower reading (legality + delivered-term collision only, no D2B-03 term): 33 / 21
```

PHON-01 authority: `examples/culture-d4/components/02-phonology.yml:117-123`
(`template: "(C)V(V)(C)"`, `codas: [n, m, s, k, l, r, t, d]`, `clusters: "no onset or coda clusters anywhere"`).
Filed figure being corrected: `reports/round-26/register/review.md` §3 (RD-2, "13 of 54 unusable").
D2B-03 ledger authority: `examples/culture-d4/components/04-lexicon.yml:22`.

**§5 read-set exposure** — `reports/round-34/handoff/declared-in-r7/freeze.txt`
("read set: 58 files; component digests 26/26; d4 pins 8/8");
`reports/round-26/register/impl.md` §7 (the r26 pin cascade and its `repin.json`).

**§5.2 contract check**

```
$ sed -n '30,44p' examples/culture-d4/packet.d4.yml    # lexicon fields; `register_form` absent
```
