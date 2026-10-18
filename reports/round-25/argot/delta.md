# R25-D03 — the implementation delta: forecast element → delivered / not delivered

Worker: R25-D01..D04 (D axis, argot analysis). Round 25, 2026-10-18. Claim **D**
(`reports/round-25/claims.json:20-27`), capability `argot-derivation-check`.
Sources: `forecast.md` (R25-D01) and `current-state.md` (R25-D02) in this directory.
Baseline revision `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`; worktree
`f74fc9403d4b02c8ee76439eb133e3dea9b65b14`.

**Bottom line.** The round-17 argot-derivation forecast is **not delivered**, and the gap is wider
than "the leg was never written": the delivered schema has **no field** for a derivation relation
between two records, the delivered `constructions` registry has **no operation** dimension, and the
one live replay engine that reads `bases`+`construction` is a **concatenation replayer** whose model
of a derivation is `form == bases_joined`. Against that model a *correct* argot derivation is a
false FAIL and a *non*-derivation passes. So the delta is a **schema + engine + gate** delta, not a
gate delta alone. Each element below is named; nothing is silently dropped.

**Root cause, and it is not an omission (verified this seat, §1.2).** The forecast was written
against a culture that round 17 did **not** ship. `design-brief.md` designs a **weigh-court
brokerage** (spine COUNT × QUOTE, §2-§3; `design-language.md:55-57` ranks it authority 1);
`design-language.md:61` states its own spine assumption as "**TIDE + LEDGER**"; the landed tree is
the **furnace-league** (FIRE × MARK), built to the `components/01-brief.yml` registry. The brief seat
itself recorded the divergence without resolving it (`design-brief.md:596-670`: eight files from
eight seats that "do **not** agree on the D4 culture, the component registry, or the hold set", plus
reconciliation paths A/B/C, "parent's decision; this seat implements none"). Path **A** — keep the
landed furnace-league tree — was taken. So the argot's quote register, its loan layers and its
measure/numeral series were never built, and Δ3 has **no domain to grade**. An implementation
written now would be a leg over an empty set, not a delivered capability.

## 1. Element-by-element disposition

Element ids are `forecast.md` §2 (F-1..F-8) and §3-§4 for the surrounding material.

| # | forecast element | source line | delivered? | evidence (R25-D02) |
|---|---|---|---|---|
| F-1 | quote forms derived from their plain base by one of two declared operations | `design-brief.md:301-302` | **NOT DELIVERED** | 0 occurrences of `derived_from`/`derivation`-as-relation anywhere in `examples/`; the 54 lexicon records carry `bases` only on the 4 CX-class records |
| F-2 | `head2` (first two syllables) for measure words | `design-brief.md:302-303` | **NOT DELIVERED** | `head2` → 0 occurrences in `examples/`, `tools/`, `corpus/` |
| F-2b | `reverse` (string reversal) for the numeral series | `design-brief.md:303-304` | **NOT DELIVERED** | `reverse` → 0 in `examples/`; the 6 hits in `tools/` are all `sorted(..., reverse=True)` |
| F-3 | the derivation is **checked** through `derived_from` + `derivation` fields | `design-brief.md:303` | **NOT DELIVERED — no such fields exist** | `derived_from` → 0 in `examples/`; `packet.d4.yml` `contract.record_fields.lexicon` = `id, term, gloss, field, route, bases, construction, layer, stage, axis, evidence, follows` — no `derived_from`, no `derivation` |
| F-4 | a relation between two records of the same packet | `design-brief.md:304` | **NOT DELIVERED** | no code path in `tools/` reads two records and compares one as a derivation of the other |
| F-5 | signature: zero fails in the delivered packet | `design-brief.md:305-306` | **VACUOUSLY SATISFIED** | trivially true — there is no argot form and no leg, so no fail can exist. Not a delivery. |
| F-6 | signature: coverage block reports `derived_forms` / `derived_ok` agreeing | `design-brief.md:306-307` | **NOT DELIVERED** | both tokens → 0 occurrences repo-wide. The live coverage block (`typed-labels.d4.yml:29`) has `labels_by_kind`, `typed_labels: 74`, `rank_rules_*`, `reconciliation_records` — no derivation counts |
| F-7 | control: quote form ≠ `apply(op, base)` → FAIL `D4L-ARGOT-DERIV`, new id, **control-only** | `design-brief.md:308-310` | **NOT DELIVERED** | `D4L-ARGOT-DERIV` in 2 files under `reports/round-17/`, **0** files under `examples/` and **0** under `tools/` — no code path emits it |
| F-8 | required-controls row C-02 of the negatives battery | `design-brief.md:456` | **NOT DELIVERED** | same as F-7; no battery fixture on disk exercises it |

### 1.1 Surrounding forecast material (named so it is not absorbed)

| # | element | source | delivered? | evidence |
|---|---|---|---|---|
| A-1 | the six argot loans `AL-01..AL-06`, supplied in the quote slot, plain doublet owed | `design-language.md:406-424` | **NOT DELIVERED** | `AL-0` occurs once in the packet (inside `CAL-01`); the loan forms `gun`, `suk`, `man`, `nis` occur 0 times; `res`/`kan` exist only as unrelated lexemes (`L-52`, `L-34`) |
| A-2 | the eleven worked derivations, bases `D4-X02`, `D4-X13..X22` | `design-language.md:200-215` | **NOT DELIVERED** | `D4-X` → 0 files under `examples/` and `tools/`; of the 11 bases only `nes` (`L-16`, a body word) and `sam` (`L-39`, charcoal) exist as delivered terms, both unrelated |
| A-3 | the eight quote names by `reverse` (`inak, usam, urin, akas, akim, aruk, isun, asum`) | `design-language.md:485-511` | **NOT DELIVERED** | each → 0 occurrences; the `names:` block has no `quote` key (0) and all 8 records carry `rule: CX-01` / `operation: concatenate` |
| A-4 | Δ1 class 2 register-scoped slots `<id>#plain` / `<id>#quote`, hold `D4L-REGISTER-UNRESOLVED` | `design-brief.md:254-282`, `:560` | **NOT DELIVERED** | `registers`/`doublets` packet keys absent; `doublet_of`, `slot_ref`, `#plain`, `#quote` → 0; the only `form_slots` are the D2-shaped `LEX-GAR-01..06`; `D4L-REGISTER-UNRESOLVED` in 0 files under `examples/`/`tools/` |
| A-5 | Δ2 slot cardinality, `doublet_of` as a packet fact, `D4L-DATA` on two supplied forms in one slot | `design-brief.md:283-295` | **NOT DELIVERED** | `doublet_of` → 0; no `D4L-DATA` producer |
| A-6 | Δ5 register-era clock: every quote form `available_from: E3`, prose span → `D4L-ERA` partial | `design-brief.md:328-341` | **NOT DELIVERED** | `D4L-ERA` in 0 files under `examples/`/`tools/`; no quote form exists to date |
| A-7 | the design's §4 packet shape: D2's keys **plus** `registers, doublets, measures, oaths` | `design-brief.md:243` | **PARTIALLY DELIVERED** | packet has 34 top-level keys; `registers` ABSENT, `doublets` ABSENT, `measures` ABSENT, `oaths` ABSENT, `sayings` ABSENT. Present: `form_slots`, `cross_culture_review`, `cloth_sources`, `constructions`, `layers` |
| A-8 | the design's §4 component plan (`03-morphosyntax` owning `morphology`, `05-lexicon`, `06-register-contract`) | `design-brief.md:225-241` | **REPLANNED, NOT DELIVERED AS DESIGNED** | landed component set is the D2/D3 family (`03-orthography`, `05-naming`, `06-myth`, …). `morphology` is declared by `04-lexicon.yml` (the only file matching `^morphology:`); there is no `06-register-contract.yml` and no component declares the register law |
| A-9 | the design's receipt: "11/11 derivations reproduce" | `design-language.md:588` | **NOT REPRODUCIBLE TODAY** | the receipt's checker was `.scratch/check-d4-language2.py` (scratch, superseded; receipt R-6 records the withdrawn draft). No committed checker reproduces the 11 |
| A-10 | the design's **spine** itself: COUNT × QUOTE | `design-brief.md:30-50`; `design-language.md:55-57,61` | **NOT DELIVERED — superseded by path A** | landed `01-brief.yml:59-90` declares FIRE × MARK (`SP-01` fire, `SP-02` mark) with SEED-01 "Furnace-league culture"; `design-language.md:61` states its own assumption as "TIDE + LEDGER" — a third culture again. Three spines were on file; the furnace-league shipped |
| A-11 | the design's hold-set lettering: `D4L-FORM-UNRESOLVED` at `GAR-01..06` | `01-brief.yml:195-205` (`hold_set_declaration`) | **PARTIALLY DELIVERED, LETTERING DRIFTED** | the declaration names 6 rows `D4L-FORM-UNRESOLVED`; the **engine emits `D2L-FORM-UNRESOLVED`** and the committed `expected-holds.json` carries 12 `D2L-` rows (`Counter({'D2L-FORM-UNRESOLVED': 12})`). In `packet.d4.typed.yml` the two spellings coexist: 6 `D4L-FORM-UNRESOLVED` (the declaration echoed through `contract`) vs 37 `D2L-FORM-UNRESOLVED` (the emitted findings) — measured `grep -c` on each. `grep -rl D4L-FORM-UNRESOLVED examples/` → 5 files, and in every one the hit is the *declaration text* (`01-brief.yml`, `packet.d4.yml`, `packet.d4.typed.yml`, `brief.md`, `ASSEMBLY.md:63`), never an emitted finding. Recorded as a named delta, not repaired (the O claim owns the typed pipeline; see `reports/round-25/gate-input/`) |

### 1.2 The divergence this delta rests on (measured, not inferred)

| claim | evidence |
|---|---|
| `design-brief.md` designs a weigh-court brokerage, spine COUNT × QUOTE | `design-brief.md:30-50` (the brief's own §2-§3 scope); `design-language.md:55-57` ranks it authority 1 and names "the culture brief, spine COUNT × QUOTE" |
| `design-language.md` designs a **different** culture again | `design-language.md:61` — "Institution/spine (assumption, the load-bearing one): **TIDE + LEDGER**"; tide-post `:281`, ledger `:322`, tide-mark `:353` |
| the landed tree is a **third** culture | `examples/culture-d4/brief.md:15-18` and `01-brief.yml:59-90` — "A furnace-league culture … Its spine is two axes — **FIRE** … and **MARK**"; `01-brief.yml` SEED-01/SEED-07 |
| round 17 knew and did not resolve this | `design-brief.md:596-670` — the status table ("they do **not** agree on the D4 culture, the component registry, or the hold set"), the three consequences, and paths A/B/C with "parent's decision; this seat implements none" |
| path A is what shipped | `ls examples/culture-d4/components/` → the D05 furnace-league registry stems `01-brief, 02-phonology, 03-orthography, 04-lexicon, 05-naming, 06-myth, 07-symbolism, 08-eras, 09-costumes, 10-ritual-calendar, 11-contact-history, 12-provenance`, byte-identical to `01-brief.yml:149+` registry |
| the argot's home is the culture that did not ship | the quote register, the six argot loans, the eight quote names and the `D4-X` measure/numeral series all belong to the weigh-court's COUNT × QUOTE spine; none has a counterpart in the furnace-league's FIRE × MARK record set |

## 2. What *is* delivered on the derivation axis (do not understate the delta)

The gap is argot-specific. Three real replay mechanisms exist and are green over D4:

1. **`morphology.derivation_rules`** — three machine-readable `pattern`/`output` pairs
   (`CX-01/02/03`), the SKILL's "machine-readable pattern/output pairs" requirement met for the
   concatenation class (`examples/culture-d4/components/04-lexicon.yml:192-195`).
2. **`tools/gates/naming-collision-gate.py` gate C** — replays each name's `formation` chain against
   those rules; emits `DERIV-AFFIX` / `DERIV-REPLAY` / `DERIV-HOLD`. Over D4: exit 1, 14 findings,
   `grep -ci deriv` → **0**, i.e. all 8 names replay clean.
3. **`tools/gates/lexicon-coverage-audit.py` leg D** — replays each record's `bases` against its
   `construction.pattern`; emits `D-route-missing`, `D-rule-underspecified`, `D-form-mismatch`,
   `D-rule-violation`, `D-meaning-mismatch`, `D-exception-unlicensed`, `D-stage-mismatch`. Over D4:
   exit **0**, no output; `--selftest` 14/14.

Neither gate reads an `operation` field (`grep -n "operation"` in both → 0), and neither can grade a
relation between two records. The naming gate reads `formation` on `names[]` only; the audit reads
`bases`/`construction` on `lexicon[]` only. **The argot relation falls in the seam between them.**

## 3. The load-bearing measurement: the operation class is not representable

Four scratch fixtures (all under `TMPDIR=$PWD/.scratch`, the delivered tree untouched), each a copy
of the delivered packet plus one declared `ARGOT-REVERSE` construction
(`pattern: "B1"`, `base_classes: [noun]`, `available_from: E0`) and one derived record whose
`bases` is `min`:

| # | fixture | record's `term` | meaning | audit result |
|---|---|---|---|---|
| N-2 | `.scratch/r25d/ctrl-argot-ok.yml` | `nim` | **correct** `reverse(min)` | `FINDING D-form-mismatch: 'nim' does not reproduce from bases min under construction 'ARGOT-REVERSE' (expected 'min')`, exit **1** |
| N-3 | `.scratch/r25d/ctrl-argot-bad.yml` | `min2` | **wrong** derivation | identical `D-form-mismatch … (expected 'min')`, exit **1** |
| N-4 | `.scratch/r25d/ctrl-argot-identity.yml` | `min` | **not a derivation at all** (form equals base) | exit **0**, no finding |
| N-1 | `.scratch/r25d/neg-deriv.yml` | `mesor` (base `mes`, `CRAFT-AGENT`) | concatenation-class violation | `D-form-mismatch … (expected 'mesar')`, exit **1** |

Read together: the engine's model is `expected = pattern with B1…Bn substituted, then
`+`/`-` stripped`; it accepts **only** `form == bases_joined`. Hence a correct argot derivation
**fails**, a wrong one fails **identically**, and a non-derivation **passes**. N-1 is the positive
control proving the engine is otherwise live and discriminating on its own class.

Consequence for any implementation: **adding `ARGOT-*` to `constructions` alone is a regression** —
it would manufacture a false red on a correct packet and a false green on a missing derivation.
The op must arrive with an `operation` discriminator the replayer dispatches on.

## 4. The implementation delta (named, not executed)

Ordered so each step is independently checkable. Step 0 is the honest-stop gate: if it cannot be
done, the rest must not be attempted.

**Δ-step 0 — schema.** Add the relation to the D4 contract:
`contract.record_fields.lexicon` gains `derived_from` (a term/base reference) and `derivation`
(an operation id + inputs). Add the operation registry: either `constructions[].operation`
(`concat` / `head2` / `reverse`) with the CX rules restated as `concat`, or a sibling
`morphology.argot_operations` block. **Without this step nothing downstream can be honest** — the
current schema cannot express "this form is the reverse of that one".

**Δ-step 1 — operation semantics, declared not implied.** `head2` needs its algorithm stated where
the machine reads it: `design-language.md:191-196` fixes **maximal-onset** syllabification and names
the disagreement (`saalumi` → `saa.lu.mi` → `saalu`, not `saalum`). A `head2` implementation whose
syllabifier differs from that reading is a different operation, so the reading belongs in the
declared rule, with a worked pair (`saalumi`/`saalu`) as its own selftest constant.

**Δ-step 2 — the replay engine.** One of:
(a) extend `lexicon-coverage-audit.py` leg D to dispatch on `operation` (`concat` keeps the present
`replace("+","").replace("-","")` path; `head2`/`reverse` are computed functions), or
(b) add the leg to `tools/gates/d4-typed-labels-check-gate.py` / the projector family where the
typed packet is produced, or
(c) a new `tools/gates/argot-derivation-check.py`.
Whichever, it must satisfy the SKILL's derivation-replay row (`SKILL.md:209`): machine-readable
pattern/output pairs, the row list committed, and the digests it is pinned to recorded. The
pre-registration row (`SKILL.md:214`) governs Δ-step 4's expectation.

**Δ-step 3 — the id and its control.** A violating form → **`D4L-ARGOT-DERIV`**, FAIL class, as
`design-brief.md:308` and §8 C-02 specify. It is control-only for the delivered packet: the D4
packet's own debt set stays free of it (`design-brief.md:310`). A selftest control must carry both
directions — the N-2 shape (correct derivation **passes**) and the N-3 shape (wrong derivation
**fails**) — because N-2 is exactly what the naive implementation gets wrong.

**Δ-step 4 — the signature.** The coverage block reports `derived_forms` and `derived_ok`
(`design-brief.md:306`), and the typed gate's L3 family grows the leg so `expected-holds.json` can
pin it. Note the live gate's L3 legs compare against a **committed** expectation; a new leg with no
expectation row is not a delivered leg (`SKILL.md:214`, pre-registration).

**Δ-step 5 — the data.** Deliver the argot forms themselves (A-1/A-2/A-3): the quote slots, the 11
measure/numeral pairs, the six loans with their owed plain doublets, and the eight quote names.
Until then the leg has an empty domain and F-5 ("zero fails") stays vacuous. Steps 0-4 without 5
deliver an unexercised mechanism.

**Δ-step 6 — the register half (A-4/A-5).** The quote slot a quote form occupies is Δ1's mechanism;
the derivation arithmetic is Δ3's. Δ3 cannot be *demonstrated* without Δ1, because a quote form with
nowhere to sit is indistinguishable from a stray lexeme. This dependency should be declared rather
than discovered late.

**Δ-step 7 — the culture question (A-10), which outranks steps 0-6.** The forecast's argot belongs
to the weigh-court's COUNT × QUOTE spine, which was not shipped; the landed D4 is the furnace-league
FIRE × MARK. Two honest routes, and the choice is **not this seat's** (`AGENTS.md`: report contested
scope, do not absorb it):

- **(i) Host the mechanism on the landed culture.** The brief seat already named the natural host:
  "the furnace-league's own spine offers a natural host for Δ1/Δ6 ('the mold-mark is the
  truth-mark', `components/01-brief.yml:80`: an attestation register distinct from plain speech)"
  (`design-brief.md:659-661`). An attestation/quote register over the furnace-league's stamp-mark
  vocabulary is a coherent FIRE × MARK instantiation, and it would give Δ3 a real domain (the
  count-stamps and the measure vocabulary are already delivered). This is the cheapest route against
  landed bytes and the only one that does not supersede a shipped component.
- **(ii) Re-cause the culture.** Paths B/C (`design-brief.md:664-670`) — supersede the landed
  fragments and rebuild to TIDE + LEDGER or to the weigh-court. Larger, and it invalidates the
  delivered packet, the pins, `expected-holds.json` and every round-18-24 measurement taken against
  them.

Recommendation to the integrator, stated as a recommendation only: **(i)**, because Δ1/Δ3 are
declared culture-independent mechanisms (`design-brief.md:656-661`, "**What is portable from this
file under any culture choice**") and because (ii) would re-open five rounds of pinned measurements
for a design-drill culture that is explicitly NON-CANON.

## 5. Delta summary in one table

*(as measured pre-landing, `f74fc94`; see §8 for the four rows the sibling landing changed — the
`engine`, `id` and `operations` rows are now partly delivered by `tools/gates/argot-derivation-gate.py`)*

| axis | forecast | delivered | delta |
|---|---|---|---|
| **culture** | weigh-court brokerage, spine COUNT × QUOTE | furnace-league, spine FIRE × MARK | **the argot's host was not shipped (Δ-step 7)** |
| schema | `derived_from` + `derivation` fields; `registers`/`doublets` keys | none | **new fields + registry** |
| operations | `head2`, `reverse`, with stated algorithms | `concat` only, unlabelled | **new operation dimension** |
| engine | a replay that computes `apply(op, base)` | concatenation replayer; accepts `form == bases_joined` | **new dispatch + two computed ops** |
| id | `D4L-ARGOT-DERIV`, control-only | not emitted by any code path | **new id + selftest pair** |
| id lettering | holds `D4L-FORM-UNRESOLVED` at `GAR-01..06` | engine emits `D2L-FORM-UNRESOLVED` (12 rows) | **lettering drift (A-11), named not repaired** |
| signature | `derived_forms` / `derived_ok` in coverage | absent | **new coverage keys + gate leg + expectation row** |
| data | 11 derivations, 6 loans, 8 quote names, quote slots | none of it | **data delivery (steps 5-6)** |

## 6. What this worker did **not** do

- Did not write any tool, gate, packet, component or `expected-holds.json` byte. All four fixtures
  live under `.scratch/r25d/`; no scratch file was promoted.
- Did not claim F-5 as a delivery: "zero fails in the delivered packet" is true only because the
  domain is empty, and is recorded as vacuous in §1.
- Did not resolve the Δ1/Δ3 ordering question (§4 step 6) or the culture question (§4 step 7) — both
  are named for the integrator, per `AGENTS.md` ("reports contested scope instead of absorbing it").
- Did not repair the `D2L-`/`D4L-` lettering drift (A-11): the O claim owns the typed pipeline and
  `reports/round-25/gate-input/` is measuring it.
- Did not touch any filed artifact of rounds 8-24, and did not commit or push.

## 7. Counting commands for this file

```
# F-1..F-8 tokens
for t in ARGOT argot head2 derived_from derived_forms derived_ok doublet_of slot_ref; do
  printf "%-14s examples=%s tools=%s\n" "$t" \
    "$(grep -rl -- "$t" examples/ | wc -l)" "$(grep -rl -- "$t" tools/ | wc -l)"; done
# the four controls
python3 tools/gates/lexicon-coverage-audit.py examples/culture-d4/packet.d4.yml            ; echo "exit=$?"  # 0
python3 tools/gates/lexicon-coverage-audit.py .scratch/r25d/neg-deriv.yml                 ; echo "exit=$?"  # 1 (N-1)
python3 tools/gates/lexicon-coverage-audit.py .scratch/r25d/ctrl-argot-ok.yml             ; echo "exit=$?"  # 1 (N-2, false red)
python3 tools/gates/lexicon-coverage-audit.py .scratch/r25d/ctrl-argot-identity.yml       ; echo "exit=$?"  # 0 (N-4, false green)
# the live replay legs
python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml | grep -ci deriv   # 0
python3 tools/gates/lexicon-coverage-audit.py --selftest | tail -1                               # 14/14
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1           # 19/19
```

## 8. Addendum, 2026-10-18T17:32Z — a sibling seat landed an argot gate mid-window

Every measurement in §1-§7 was taken against worktree `f74fc94` with `git status --porcelain`
showing only untracked round-25 report directories. **During this seat's write window the tree
changed under it.** A sibling seat (the argot-execution lane, `R25-D11..D14`, whose
`execution-1..4.md` sit beside this file) landed:

- `tools/gates/argot-derivation-gate.py` (new, untracked, 28,588 bytes, mtime 2026-10-18 14:30); and
- an edit to `tools/gates/typed-pipeline-gate.py` (`git diff --stat` → `45 insertions(+), 4
  deletions(-)`: an `owed_slot_of()` null-normalizer and an `L2-legacy-source` leg — this is the
  **O claim**'s typed-input false-red fix, not this claim's work).

This seat did not write, edit or influence either file. The addendum exists because **four of my
§1 rows are now stale**, and a delta that keeps a stale row is exactly the failure this claim
exists to prevent.

### 8.1 Re-measured, 2026-10-18 (post-landing)

| what | §1 said (pre-landing) | measured now | reading |
|---|---|---|---|
| `D4L-ARGOT-DERIV` producers | 0 files under `tools/` | **1** (`tools/gates/argot-derivation-gate.py`, 6 occurrences) | **F-7's id is now emitted by a live gate** |
| `head2` | 0 occurrences repo-wide | **1 file** (`argot-derivation-gate.py`, incl. `def op_head2` and the selftest `head2-maximal-onset: op_head2("saalumi") == "saalu"`) | **F-2's operation is implemented** |
| `reverse` | 0 in `examples/`, 6 unrelated hits in `tools/` | 31 files in `tools/` | the op is implemented and embedded |
| `derived_from` | 0 in `tools/` | **1** file in `tools/` | F-3's field is now **read** |
| `derived_forms` / `derived_ok` | 0 repo-wide | still **0** | **F-6 remains NOT DELIVERED** — the gate's coverage line uses `derived_pairs` instead, a different key set from the forecast's |
| `doublet_of` / `slot_ref` in `examples/` | 0 | still 0 | A-4/A-5 remain NOT DELIVERED |
| `registers` / `doublets` packet keys | absent | still absent (34 keys) | A-7 unchanged |
| the delivered packet's own argot data | none | still none | A-1/A-2/A-3 unchanged; **F-5 remains vacuous** |

### 8.2 What the new gate does, and what it does not close

Measured, not read from its docstring:

```
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
→ coverage: records=156 register_scoped=18 derived_pairs=0 borrow_pairs=6 violations=0 rule_holds=0
→ dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4…
→ exit 0
```

It **does** close F-2/F-2b/F-7 at the *mechanism* level: it embeds both operations (with the
maximal-onset reading as a named selftest), emits `D4L-ARGOT-DERIV` on a non-replaying pair, and
adds three sibling ids (`D4L-ARGOT-RULE` HOLD, `D4L-ARGOT-COVERAGE` HOLD, `D4L-ARGOT-DATA`).

Verified this seat with two fresh fixtures in the **forecast's own F-3 shape** (a record carrying
`register: quote` + `derived_from: min` + `derivation: {op: reverse, base: min}`), which is the
shape the gate keys on — *not* my earlier `constructions`-route fixtures:

| fixture | record | result |
|---|---|---|
| `.scratch/r25d/gate-ok.yml` | `nim` = `reverse(min)`, correct | `derived_pairs=1 violations=0`, **exit 0** |
| `.scratch/r25d/gate-bad.yml` | `min2` declared as `reverse(min)` | `FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form L-55 'min2' (register 'quote'): declared chain 'reverse' applied to 'min' yields 'nim'; the stated inputs and rules do not yield the candidate`, **exit 1** |

**This corrects §3.** My N-2/N-4 finding — that the *audit* engine's concatenation-only model makes
a correct argot derivation a false red — stands for `lexicon-coverage-audit.py` and is still true
(`python3 tools/gates/lexicon-coverage-audit.py .scratch/r25d/ctrl-argot-ok.yml` → `D-form-mismatch`,
exit 1). It is **not** a statement about the lane as a whole now that a dispatch-on-operation gate
exists. §3's recommendation ("adding `ARGOT-*` to `constructions` alone is a regression") remains
correct as written; the sibling gate avoids it by keying on `derived_from`/`derivation` and never
consulting `constructions` for the argot ops.

**What it does not close** — so the claim's delta is *narrowed*, not erased:

1. **F-6** (`derived_forms` / `derived_ok` in the coverage block) — not delivered; the gate prints
   `derived_pairs`, a different contract.
2. **F-5** — still vacuous: the delivered packet has `derived_pairs=0`, so there is no argot form
   whose check could pass. The gate's own `D4L-ARGOT-COVERAGE` branch (`:482-487`) is the mechanism
   for saying so, and it fires only when the *packet* declares the ops; the delivered packet does
   not, so the gate is silent and green on an empty domain.
3. **§4 Δ-steps 0 and 5** — the schema still lacks `derived_from`/`derivation` on any delivered
   record, and the argot data is still absent. Δ-steps 2 and 3 are now **done by another seat**.
3b. **The new gate is not wired into anything.** `grep -n "argot" tools/gates/typed-pipeline-gate.py`
   → 0 lines: the typed gate does not invoke it, so its `D4L-ARGOT-*` ids cannot enter
   `pipeline_findings` or `expected-holds.json`. `tools/check-gate-battery.py` reads its gate list
   from `GATE_NAMES`/`GATES_DIR` and does not name it either. So the leg exists as a **standalone
   script**, not as a pipeline leg — Δ-step 4 (the signature, and the expectation row that makes the
   leg count) remains open on top of F-6.
4. **The gate's selftest was red, and the state moved three times under this seat.** Four reads
   inside ~2 minutes:
   - 17:31Z: `--selftest` → `selftest: FAIL — fixture unreadable: … argot-derivation-gate.yml`; `ls
     tools/gates/fixtures/ | grep -ci argot` → **0**.
   - 17:32:1xZ: the fixture pair landed (`argot-derivation-gate.yml`, `.expected`, mtime
     14:32:13/14:32:16 local = 17:32:13/17:32:16Z) → `selftest: 16/18 checks passed`, exit **1**,
     the two failures being `fixture-names-the-violating-form` and `coverage-hold-fires`.
   - 17:32:55Z: `selftest: 17/18 checks passed` — still exit 1, one failure left.
   - The gate's `register_scoped` count on the delivered packet moved 18 → **6** between the 17:31Z
     and 17:32:25Z reads — the record-classification rule was being edited live.
   Reported, not repaired: the gate is not this seat's file, and a moving target cannot be pinned by
   a third party. **Any reading of that gate must carry its own timestamp**; this section is a
   snapshot at 2026-10-18T17:32:55Z, not a verdict.
5. **A-10/A-11 unchanged**: the culture divergence and the `D2L-`/`D4L-` lettering drift stand.

### 8.3 Revised bottom line

The claim's "implemented and executed" half is now **partly satisfied by a sibling seat**, on a gate
this seat did not write, whose selftest was 17/18 at the last read (exit 1), whose classification
logic changed twice during this seat's write window, and which is not wired into the typed gate or
the battery. The half that remains open is the one that mattered most: **the argot has no domain**,
because the culture that hosts it was not shipped (§1.2 / Δ-step 7) — `derived_pairs=0` on the
delivered packet at every read. A standalone gate over an empty set is not a delivered capability,
and this seat cannot certify the gate's own correctness.

**For the integrator:** the two facts worth carrying forward are (i) the delivered packet has zero
argot derivations and zero `derived_from` fields, so F-5 is vacuous and F-6 is absent regardless of
what the gate does; and (ii) the argot's host culture (weigh-court, COUNT × QUOTE) was not shipped,
so Δ-step 7 — not Δ-step 2 — is the decision that gates the claim.
