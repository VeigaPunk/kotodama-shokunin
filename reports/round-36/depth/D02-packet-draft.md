# D02 — the packet `register_forms` block, drafted: bytes, integration diffs, and the receipts

- Seat: D02 | executor | claim D (register-form domain) | date 2026-10-19 | baseline ce103bf
- Write scope: this file only. Scratch under `.scratch/d02/` only. No component,
  packet, tool, gate or filed round-1..35 byte written by this seat.
- Canon: NON-CANON engineering evidence. A draft plus measurements; the
  integrator applies the fenced blocks, not this seat.

## 0. The finding that changes the claim's premise

The claim's `before` reads "Register-form domain empty (reports/round-25/argot/
+ SCORECARD r25 row)". **That premise is stale.** It was true when round 25
filed it and it was closed by round 26. Measured on the current tree:

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 \
  derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
exit 0
```

`derived_pairs=8` is not zero. The eight register forms are delivered as
**lexicon rows** `L-55..L-62` (`examples/culture-d4/packet.d4.yml:1053` is
`id: "L-55"`, `:1163` is `id: "L-62"`), each carrying `register: "stamp"`,
`derived_from`, `derivation: {op, base}` and `doublet_of`. The r25 record this
claim cites (`reports/round-25/argot/execution-4.md:35-36`, "**Result: zero
register forms to replay**", and the SCORECARD row at `SCORECARD.md:312`) was
superseded by the r26 `register-stratum` landing (`SCORECARD.md:329`).

**So the honest reading of claim D's after_required is not "author content" but
"give the delivered domain a first-class block".** Authoring new forms would
duplicate eight existing ones and manufacture exactly the defect r26's own
`forms.md` §1.1 flags as a `D4L-DATA` class ("two records, one form"). This file
drafts the index route and measures it.

## 1. The hazard that fixes the block's shape

`tools/gates/argot-derivation-gate.py:304-314` `record_blocks()` walks **every**
top-level list-of-mappings block, and `:549` grades each record that
`record_form()` finds a `term`/`quote_form`/`form`/`candidate`/`name` field on
(`:109`) **and** that `is_form_record()` accepts (`:343-357`). A row that
restates `form` + `derived_from` + `derivation` is therefore graded a second
time. Measured over the same 8-form block in three field variants
(`records` baseline 187):

| variant | fields on each RF row | `register_scoped` | `derived_pairs` | verdict |
|---|---|---|---|---|
| full duplication | `form`, `derived_from`, `derivation` | 14 → **22** | 8 | the 8 derivations are graded **twice** |
| pointer-only | `form`, `op` (no `derived_from`/`derivation`) | 14 | 8 | single grading |
| off-channel | `attested_form`, `op` | 14 | 8 | single grading |

Command (all three probes, scratch only):

```
$ python3 -B tools/gates/argot-derivation-gate.py .scratch/d02/probe-<variant>.yml
full     records=195 register_scoped=22 derived_pairs=8 violations=0   exit 0
pointer  records=195 register_scoped=14 derived_pairs=8 violations=0   exit 0
attested records=195 register_scoped=14 derived_pairs=8 violations=0   exit 0
```

**The block therefore carries the form string for legibility and `op` for the
rule, but never the `derived_from`/`derivation` pair.** The derivation relation
stays declared once, on the lexicon row that owns it. `authority: "lexicon"` is
stated on every row so a reader cannot mistake the index for a second source of
truth.

## 2. The integration route: one new component, **zero** assembler edits

The mission asks for "the integration diffs for `tools/assemble-culture-d4.py`
if a new component is needed". **No assembler diff is needed.** Measured:

- `tools/assemble-culture-d4.py:218-220` `component_files()` globs *every*
  `*.yml`/`*.yaml`/`*.json` in `examples/culture-d4/components/`, minimum 12
  (`MINIMUM_COMPONENTS`). There are 13 today; adding a 14th is admitted with no
  code change.
- `:258-266` — a component's own top-level `packet_keys:` list fixes its packet
  contribution **exactly**, bypassing the `PACKET_KEYS` allowlist.
- `:367-371` — `build_packet` carries every merged key not in `PACKET_KEYS`
  (`for key in sorted(set(merged) - set(PACKET_KEYS))`).

So a component declaring `packet_keys: [register_forms]` lands its block even
though `register_forms` is absent from both `PACKET_KEYS` and `RECORD_FIELDS`.
This is not a new mechanism: it is exactly how `register_law` already works —
`'register_law' in PACKET_KEYS → False`, yet the block is in the packet
(`examples/culture-d4/packet.d4.yml:2788`), landed by
`components/13-register-law.yml:18` `packet_keys: [register_law]`.

Proven on a scratch component tree:

```
register_forms merged: True [{'id': 'RF-01', 'form': 'tuum', 'lexicon_id': 'L-55'}]
sources includes 14: ['.scratch/d02/comps/14-register-forms.yml']
```

### 2.1 Consequence: a block that is not in `RECORD_FIELDS` is not field-validated

`validate_blocks` (`:315-325`) enforces `RECORD_FIELDS` (`:109`, `"registers":
("id",)` at `:118`) per block. A new block
absent from that dict gets only the generic checks (`:304-309`: every record a
mapping, ids non-empty strings, ids unique). **A row missing `lexicon_id` or
`op` would assemble silently.** The integrator should therefore either add the
fenced `RECORD_FIELDS` diff in §5 (belt and braces) or accept the weaker
guarantee knowingly. This seat recommends applying it: it is 4 lines and turns a
missing field into a fail-closed assembly error.

## 3. The block bytes (fenced — the integrator applies)

New file `examples/culture-d4/components/14-register-forms.yml`. Its eight rows
were generated by text-extraction from the delivered lexicon rows, never by
re-serialisation, so the `form`/`base`/`op`/`axis`/`base_id` values are the
delivered bytes' own.

```yaml
# examples/culture-d4/components/14-register-forms.yml
# D4 design drill — component 14 of the round-17 registry's lineage.
# NON-CANON: this file proposes a design; it records nothing about any world.
#
# Write seat: D02 (D axis, register-form block draft). Round 36, 2026-10-19.
# NEW file: it supersedes nothing and no filed byte is rewritten by it. It adds
# ONE packet block that indexes the eight register forms round 26 already
# delivered as lexicon rows L-55..L-62 (reports/round-26/register/forms.md
# section 1, the authoritative table), so the register-form DOMAIN is a
# first-class block rather than a filter over `lexicon`.
component: 14-register-forms
culture: D4
canon: not canonized (D4 design drill)
title: "14-register-forms — the register-form index: the eight stamp forms and the lexicon row that owns each"
status: "round-36 component write, 2026-10-19; supersede-by-new-file only"
packet_keys: [register_forms]
scope: >
  An index, not a second copy. Each row names the delivered lexicon record
  that owns the form (lexicon_id) and the record it derives from (base_id);
  the form string itself is carried for legibility and is declared
  non-authoritative. The lexicon row is the single source of truth.
register_forms:
  -
    id: "RF-01"
    form: "tuum"
    authority: "lexicon"
    lexicon_id: "L-55"
    register: "stamp"
    base: "tum"
    base_id: "L-02"
    op: "lengthen"
    axis: "fire"
    available_from: "E1"
    evidence: "design-choice"
    follows:
      - "F-2"
  -
    id: "RF-02"
    form: "kit"
    authority: "lexicon"
    lexicon_id: "L-56"
    register: "stamp"
    base: "tik"
    base_id: "L-42"
    op: "reverse"
    axis: "mark"
    available_from: "E1"
    evidence: "design-choice"
    follows:
      - "F-2"
  -
    id: "RF-03"
    form: "lom"
    authority: "lexicon"
    lexicon_id: "L-57"
    register: "stamp"
    base: "mol"
    base_id: "L-38"
    op: "reverse"
    axis: "mark"
    available_from: "E1"
    evidence: "design-choice"
    follows:
      - "F-2"
  -
    id: "RF-04"
    form: "nees"
    authority: "lexicon"
    lexicon_id: "L-58"
    register: "stamp"
    base: "nes"
    base_id: "L-16"
    op: "lengthen"
    axis: "fire"
    available_from: "E1"
    evidence: "design-choice"
    follows:
      - "F-2"
  -
    id: "RF-05"
    form: "huum"
    authority: "lexicon"
    lexicon_id: "L-59"
    register: "stamp"
    base: "hum"
    base_id: "L-09"
    op: "lengthen"
    axis: "fire"
    available_from: "E1"
    evidence: "design-choice"
    follows:
      - "F-2"
  -
    id: "RF-06"
    form: "mees"
    authority: "lexicon"
    lexicon_id: "L-60"
    register: "stamp"
    base: "mes"
    base_id: "L-43"
    op: "lengthen"
    axis: "fire"
    available_from: "E1"
    evidence: "design-choice"
    follows:
      - "F-2"
  -
    id: "RF-07"
    form: "reek"
    authority: "lexicon"
    lexicon_id: "L-61"
    register: "stamp"
    base: "rek"
    base_id: "L-37"
    op: "lengthen"
    axis: "fire"
    available_from: "E1"
    evidence: "design-choice"
    follows:
      - "F-2"
  -
    id: "RF-08"
    form: "saam"
    authority: "lexicon"
    lexicon_id: "L-62"
    register: "stamp"
    base: "sam"
    base_id: "L-39"
    op: "lengthen"
    axis: "fire"
    available_from: "E1"
    evidence: "design-choice"
    follows:
      - "F-2"
```

Row order follows the lexicon order (`L-55..L-62`), not r26's deliberate
reverse-before-lengthen order (`reports/round-26/register/impl.md` §3): that
ordering was a measurement-facing choice for the **lexicon** block, and this
index does not feed the runner's teeth control. Recorded so the difference is
not read as a contradiction.

## 4. The measured end-to-end (isolated `git archive` copy)

Never in-tree. Built with `git archive HEAD | tar -x -C .scratch/d02/iso`, then
the component from §3 written into that copy.

| # | command (cwd = `.scratch/d02/iso`) | observed | exit |
|---|---|---|---|
| 1 | `python3 -B tools/assemble-culture-d4.py` | `Wrote examples/culture-d4/packet.d4.yml (104622 bytes)` | 0 |
| 2 | `python3 -B tools/assemble-culture-d4.py --check` | `packet.d4.yml: byte-identical deterministic assembly` | 0 |
| 3 | `python3 -B tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | `byte-identical deterministic assembly` | 0 |
| 4 | `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `records=195 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` | 0 |
| 5 | `python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | `law_rows=5 identity_rows=8 record_ids=191 registers=17 … dangling=0 findings=0` | 0 |
| 6 | `python3 -B tools/d2-typed-labels.py --packet … --json` | `stats {fail: 0, hold: 12, labels: 82, note: 0}`; 12 findings, all `D2L-FORM-UNRESOLVED` (the six owed GAR slots × 2) | 1 (holds) |
| 7 | `python3 -B tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml` | `byte-identical deterministic typed packet` | 0 |
| 8 | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed` | 0 |
| 9 | `python3 -B tools/assemble-culture-d4.py --selftest` | `81/81 checks passed` | 0 |
| 10 | `python3 -B tools/d2-typed-labels.py --selftest` | `163/163 checks passed` | 0 |
| 11 | `python3 -B tools/assemble-d4-typed.py --selftest` | `12/12 checks passed` | 0 |

Row 6's `12 holds / 0 fails` is **identical to the count round 26 filed**
(`reports/round-26/validation.json:962` context, `stats.fail 0 / hold 12 /
labels 82`). The landing moves no hold and no fail.

Row 8 required the re-pin cascade in §6 first; it was green both before (at
`packet: 66c34ad5a4eb`) and after.

`register_forms:` lands at packet line 2788 of the rebuilt packet, carrying 8
`id: "RF-nn"` rows.

## 5. The optional assembler diffs (belt and braces; not required)

Two fenced edits to `tools/assemble-culture-d4.py`. Neither is needed for the
block to land (§2); apply them only if field-validation on the new block is
wanted (§2.1).

Diff 1 — add the key to the allowlist (`PACKET_KEYS`, currently `:77-91`,
between the `"registers", "doublets", …` line and the `"pantheon"` line):

```diff
--- a/tools/assemble-culture-d4.py
+++ b/tools/assemble-culture-d4.py
@@ -80,7 +80,7 @@
     "lexicon", "layers", "constructions", "cloth_sources",
-    "registers", "doublets", "sayings", "oaths",
+    "registers", "register_law", "register_forms", "doublets", "sayings", "oaths",
     "pantheon", "roles", "motifs", "narratives", "myths",
```

(`register_law` is added in the same line only to close the existing asymmetry
noted in §2; if the integrator prefers to leave filed behaviour alone, add
`register_forms` alone.)

Diff 2 — declare the block's required fields (`RECORD_FIELDS`, opens `:109`,
after the `"registers": ("id",),` row):

```diff
--- a/tools/assemble-culture-d4.py
+++ b/tools/assemble-culture-d4.py
@@
     "registers": ("id",),
+    "register_forms": ("id", "form", "lexicon_id", "register", "base", "base_id", "op", "axis"),
     "measures": ("id",),
```

Measured effect of diff 2: with it, a row missing `lexicon_id` fails closed at
`validate_blocks`; without it, the same row assembles silently.

## 6. The owed re-pin cascade (D04's surface — measured here, not claimed)

The landing moves four D4 artifacts and the profile that pins them. Measured by
comparing the r7 read set's own pins against the rebuilt copy:

```
$ python3 -B -c "…compare reports/round-34/handoff/declared-in-r7/expected.json inputs against .scratch/d02/iso…"
read-set files whose digest the landing MOVES: 4 of 58
  examples/culture-d4/expected-holds.json    r7= e6ae9828d6c8 -> f8ea35c4d45b
  examples/culture-d4/packet.d4.typed.yml    r7= d581e0ad5384 -> 564b4b3ac666
  examples/culture-d4/packet.d4.yml          r7= aac91246cede -> 66c34ad5a4eb
  examples/culture-d4/typed-labels.d4.yml    r7= c23b0ab532cf -> 105d91181d42
```

Note `typed-labels.d4.yml` moves only because the projector's emitted
`assembly.packet_sha256` moves with the packet; the label set (82) and hold set
(12) are unchanged.

`tools/gates/typed-pipelines.json` d4 profile, three rows (this is a **new
generation row**, never an in-place edit of a filed receipt):

```diff
--- a/tools/gates/typed-pipelines.json
+++ b/tools/gates/typed-pipelines.json
@@ d4 profile @@
   "packet":     {"path": "examples/culture-d4/packet.d4.yml",
-                 "sha256": "aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3"}
+                 "sha256": "66c34ad5a4eb1f3a6cbd81c951782852235c6f1d1dad691804c1d94dc6fc67fa"}
   "projection": {"path": "examples/culture-d4/typed-labels.d4.yml",
-                 "sha256": "c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e"}
+                 "sha256": "105d91181d42a6b32ca45641bb6c360c5e8ea90da75506a9e79d0ec4bd8a1913"}
   "expected":   {"path": "examples/culture-d4/expected-holds.json",
-                 "sha256": "e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3"}
+                 "sha256": "f8ea35c4d45b90cbcc087bd9a67bade84fe068b2eafe1bcc54a38e6ff7bfdd98"}
```

Plus a `revision_note` on `expected-holds.json` (new row, filed bytes never
edited), drafted verbatim:

```json
"revision_note": "round-36 D02 register_forms landing: the packet gained one block (register_forms, component 14-register-forms.yml, 8 rows indexing L-55..L-62). The hold set is unchanged (12 holds / 0 notes / 0 fails): a register-form index moves no form off the sound-and-identity channel and owes no form slot."
```

### 6.1 The freeze question (the load-bearing one, handed to R03/X00)

`reports/round-34/handoff/declared-in-r7/expected.json` is a 58-file read set
pinning 19 D4 surfaces, including `packet.d4.yml`. It pins components **01-12**
only — **not** `13-register-law.yml`, and it will not pin
`14-register-forms.yml`. Its own `limits` field reads "pins computational
inputs only; not lore acceptance, not canon, not completion of the round arc;
documentation surfaces excluded".

So the read set will report 4 moved digests against the r7 pin. Whether that
requires a **new** freeze row or is the ordinary drift a landing is expected to
cause is **not this seat's call** — X00 (collision matrix) and R03 (cross-review)
own it. This seat records the measurement and the precedent that the same
question was answered by a *successor* freeze, not a re-freeze
(`reports/round-26/register/repin.json`, `successor_frozen_and_green`:
`reports/round-26/register/v3-baseline-r26/`). **The r7 bytes themselves must
not be edited** (hard boundary).

## 6.2 Cross-seat collision with D01 (read after this seat's measurements)

D01 (`reports/round-36/depth/D01-design.md` §3.1) converged on a **different
block name for the same domain**: `doublets`, with `plain_slot`/`register_form`
pointers, landed by amending `04-lexicon.yml`. D01's §3.1 also names the
forecast's Δ2 (`design-brief.md:283-295`, control C-07). Both drafts are live in
this round, so the integrator must choose or combine. The measured facts:

- **D01's route is cheaper on tool surface.** `doublets` is already in
  `PACKET_KEYS` (`tools/assemble-culture-d4.py:81`) and `RECORD_FIELDS`
  (`:122`), and the assembler's own fixture template emits a `doublets:` block
  (`:469`) — so no new key, no new field row, no new component file. This
  seat's route needs one new component file (§3) and, for field validation,
  diff 2 of §5. On that axis D01 wins and this seat says so.
- **Neither block is graded for derivations.** Measured on D01's own row shape:
  `record_form({...plain_slot, register_form...}) → ''`, `is_form_record → False`.
  So neither `doublets` nor `register_forms` can double-grade the eight
  derivations; the hazard of §1 is specific to a block that restates `form` +
  `derived_from`/`derivation`, which D01's row shape does not and this seat's
  does not.
- **They are not mutually exclusive — measured, not assumed.** Installed
  together in one isolated copy (`04-lexicon.yml` + `doublets` **and**
  `components/14-register-forms.yml`):

  ```
  assemble-culture-d4.py            exit 0; --check: byte-identical deterministic assembly
  packet.d4.yml                     106454 bytes, sha256 6b3f6c924b08c8b9…
  register_forms rows               8   (id: "RF-…")
  doublets rows                     8   (id: "DB-…")
  argot-derivation-gate             records=203 register_scoped=14 derived_pairs=8 violations=0   exit 0
  register-law-gate                 record_ids=199 dangling=0 findings=0                           exit 0
  doublets rows consistent with the record-level doublet_of/derived_from/op pointers: 8/8; bad=[]
  ```

  So a combined landing is admissible and both legs stay green. The
  **redundancy is real** — `doublets.register_form` ↔
  `register_forms.lexicon_id` carry the same eight pairs — and the round should
  decide whether the domain wants one block or two rather than land both
  silently. This seat does not decide it (X00/R03 own the cross-claim call) and
  records the measurement so the decision is made on evidence.
- **Different artefacts, different values.** The two drafts are not
  interchangeable on content: D01 indexes `plain_slot ↔ register_form`
  (the Δ2 pair relation, base→register); this seat indexes the register form to
  the lexicon row that **owns** it (`lexicon_id`, plus `base_id`, `op`, `axis`,
  `available_from`) and declares `authority: "lexicon"`. D01's route carries the
  pair relation; this seat's carries ownership and the per-form rule fields.

## 7. Named gaps and limits

- **G1 — the naming gate does not grade the new block.** A row carrying an
  illegal form assembles and passes:

  ```
  $ python3 -B tools/gates/naming-collision-gate.py .scratch/d02/probe-illegal.yml
  exit 1  (14 findings — byte-identical to baseline)   zzqxx findings: NONE
  $ python3 -B tools/gates/argot-derivation-gate.py .scratch/d02/probe-illegal.yml
  exit 0   zzqxx findings: NONE
  ```

  `zzqxx` is not inventory-legal under 02's PHON-01 (`/z/`, `/q/`, `/x/` are not
  in the declared inventory). The block is a declared index whose forms the
  lexicon already owns, so this is **defensible by design** — but it is a real
  coverage gap and it is recorded as such, not smoothed. Closing it would mean
  teaching the naming gate to read `register_forms`, which is a tool change and
  therefore the integrator's, not this seat's.
- **G2 — `naming-collision-gate` and `phonology-sanity-gate` exit 1 at
  baseline too** (measured in-tree, read-only, before any change: `naming 1`,
  `phonology 1`, `d4-typed-labels-check 1`, `typed-pipeline 0`,
  `d4-assembly-check 0`). The landing changes neither: the naming finding set is
  **byte-identical** to baseline (`diff` → no output, 14 lines both sides).
  These are pre-existing conditions, not regressions from this draft.
- **G3 — the field-validation gap** of §2.1, until diff 2 is applied.
- **G4 — content authenticity.** This seat authored **no** new form. Every
  `form`/`base`/`op`/`axis`/`base_id` value is extracted from delivered packet
  bytes; the eight derivations were already replayed clean by the argot gate
  before this draft. No linguistic claim is made here that round 26 did not
  already make and measure. The index adds one editorial field, `authority`,
  whose value `"lexicon"` is a statement about provenance, not about the world.
- **G5 — two-independent-seats threshold.** The claim's threshold requires the
  forms verified by two independent seats. This seat verifies by re-running the
  legs (rows 4-5 above) in its own isolated copy; D07/D08 and R01/R02 are the
  independent reads, and this seat claims no verdict on them.
- **G6 — the D01/D02 block-name collision** of §6.2. Two drafts for one domain
  are live in this round. Both land green, together or apart; which one (or
  both) is the round's landing is X00/R03's and the integrator's call, not this
  seat's.

## 8. Counting commands

```
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/assemble-culture-d4.py --check
python3 -B tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml
python3 -B tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml
grep -c "id: \"RF-" <rebuilt packet>
```

## Owed

- `reports/round-36/depth/D04-repin.md` — the re-pin cascade of §6 is D04's
  surface; this seat measured it and drafted the diff, and does not claim it.
- The freeze-row question of §6.1 is owed to X00 and R03.
- The D01/D02 block-name collision (G6, §6.2) is owed to X00, R03 and the
  integrator.
- The naming-gate coverage gap G1 is owed to whoever owns tool changes; this
  seat may not edit `tools/`.

## Citations

- `reports/round-36/targets.json:18` — this seat's mission and out path.
- `reports/round-36/claims.json:16-21` — claim D, its before/after/thresholds.
- `SCORECARD.md:312` — the r25 row whose "EMPTY" the claim cites.
- `reports/round-25/argot/execution-4.md:35-36` — the r25 empty-domain record.
- `SCORECARD.md:329` — the r26 `register-stratum` row that closed it.
- `reports/round-26/register/forms.md` §1 — the authoritative 8-form table.
- `reports/round-26/register/impl.md` §2, §3 — what r26 amended and where.
- `examples/culture-d4/packet.d4.yml:1053`, `:1163` — `L-55`, `L-62`.
- `examples/culture-d4/packet.d4.yml:1329`, `:2788` — `registers`, `register_law`.
- `tools/gates/argot-derivation-gate.py:109`, `:304-314`, `:343-357`, `:549` —
  the block scan and the form/derivation field sets.
- `tools/assemble-culture-d4.py:218-220`, `:258-266`, `:315-325`, `:367-371` —
  component glob, per-file `packet_keys`, `RECORD_FIELDS` validation, carry
  branch.
- `tools/assemble-culture-d4.py:77-91`, `:109` — `PACKET_KEYS`, `RECORD_FIELDS`.
- `examples/culture-d4/components/13-register-law.yml:18` — the `register_law`
  precedent.
- `reports/round-26/register/repin.json` — the successor-freeze precedent.
- `reports/round-34/handoff/declared-in-r7/expected.json` — the 58-file read set
  (pin comparison; bytes not read for edit and never modified).
- `reports/round-36/depth/D01-design.md` §3.1 — the peer draft this seat's §6.2
  collides with (read after this seat's own measurements; no filed byte touched).
- Isolated work: `.scratch/d02/iso` (`git archive HEAD` copy), `.scratch/d02/`
  probes, `.scratch/d02/both` (the combined D01+D02 landing). All command outputs
  quoted above were produced there.
