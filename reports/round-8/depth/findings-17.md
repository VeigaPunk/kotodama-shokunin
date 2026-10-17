# findings-17 — R8-D17 adversarial review: two hand-typed D2 label cases

- shard: R8-D17 (adversarial reviewer, depth claim D / `d2-typed-labels`)
- wave: round 8 (loop 1, build 1 of 4), 2026-10-17
- reviewer scope: read-only over the lane tree; this file is the only write
- assignment: independently re-derive two label-typing cases from
  `examples/culture-d2` by hand; check that `tools/d2-typed-labels.py` agrees;
  every divergence is a finding
- method: the hand derivation below was written from the source components
  only, while `tools/d2-typed-labels.py` did not exist on disk (checked
  `ls -la tools/d2-typed-labels.py` → `No such file or directory`,
  2026-10-17T20:15Z), so it is blind to the tool's schema and cannot be
  retro-fitted to it

Pinned inputs (sha256, `sha256sum` 2026-10-17):

| file | sha256 |
|---|---|
| `examples/culture-d2/components/11-costumes.yml` | `b6e2c5c29cc5d68900d6cde5a8487e64f27d85ecb3d2bd7f3f5beb1113483f22` |
| `examples/culture-d2/components/05-lexicon.yml` | `9bdcb8d895be0592047260361c4c12493569e7d38318b3508a5bde314d87abdf` |
| `examples/culture-d2/components/02-phonology.yml` | `23500df0f97a43c8800e3a678df6928f476254e56ff844fabe0c71829ecbb538` |
| `examples/culture-d2/packet.d2.yml` | `8da90b0788f86fd19babc67958715c8c16cb90a98e13572380b1c1892622b81e` |
| `tools/gates/naming-collision-gate.py` | `8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526` |

## 0. Live baseline of the defect class this tool must close (reproduction)

```sh
python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml > /tmp/d17-naming-gate.out 2>&1; echo $?
# exit=1; 17 lines; output sha256 ebc8850d08ec1b7e32616cbca9092ba66f3b6f148a61515a033e6bed6fa66f4b
```

Lines 7–8 of that output (verbatim):

```
FINDING PHON-INVENTORY: FAIL — name GAR-01 'winter valley coat (heavy felted wool; uncombed finish optional)': symbol /v/ at position 7 is not in the declared inventory (consonants {p, t, k, b, d, g, m, n, s, ʃ, r, l, j, w, h}, vowels {a, e, i, o, u})
FINDING PHON-INVENTORY: FAIL — name GAR-02 'high-pasture coat (fine first-shear felt; narrow placket; wind-flap at the shoulder)': symbol /-/ at position 5 is not in the declared inventory (...)
```

So today the gate grades the English display string of a costume record on the
D2 sound channel. Both of my hand cases are chosen inside this class.

## 1. Hand derivation, case C1 — GAR-01 garment label

Source record: `examples/culture-d2/components/11-costumes.yml:215-233`
(GAR-01; packet copy `examples/culture-d2/packet.d2.yml:1848-1882`).

Locations read:

- `:216` `garment: "winter valley coat (heavy felted wool; uncombed finish optional)"` — English descriptive gloss, parenthetical construction notes.
- `:217` `form_slot: "LEX-GAR-01, the valley grade of L35 mirken (to-verify with 05-lexicon)"` — the record's own statement that its surface form is owed to another component and unresolved.
- `:26` (scope_note) "Surface forms are the lexicon component's: this file coins none and carries its requirements as form slots (LEX-GAR-*)".
- `:77` (note) "L34 mir (fleece, wool) and L35 mirken (wool cloak, the felted wrap worn at both pastures) are the two costume-field lexemes already landed, and GAR-01/GAR-02 are their valley and high-pole grades."
- `:407` `- {id: LEX-GAR-01, gloss: "the valley/winter grade of the felted wrap (L35 mirken)", register: "everyday", form: "(to-verify)"}` — the owed form is explicitly `(to-verify)`.
- `:418` `form_slots_note: "This file coins no surface form; any form the lexicon component supplies for these slots must arrive in a declared layer (CP-08) — the imported-cloth terms by trade loan, the rest native."`
- `examples/culture-d2/components/13-naming.yml:157-171` (`cross_component_repairs`):
  status "pending owner integration; proposals, not completed source-field
  fixes"; the GAR-01 proposal is `name: tolmirken` (bases `tol` + `mirken`,
  syllables `[tol, mir, ken]`), and the ledger itself says "do not suppress
  them or substitute this ledger for the owner records." So a *proposed* form
  exists, but it is explicitly not the owner's native form.

Hand typing (derived from the above alone):

| property | hand-derived value | basis |
|---|---|---|
| label kind | translated label (reader-facing English gloss) | `:216`, `:26`, `:418` |
| native form | absent | `:407` (`form: "(to-verify)"`), no `native_form` key anywhere in the record |
| form owner / slot | 05-lexicon / LEX-GAR-01 | `:217`, `:407` |
| related native lexeme | L35 `mirken` — the base garment term, **not** the GAR-01 form | `:77`, `05-lexicon.yml:693-706` |
| proposed form (not adopted) | `tolmirken`, 13-naming proposal, status pending owner integration | `13-naming.yml:157-171` |
| disposition | HOLD / unresolved — record stays visible, never silently passed | `:418` "must arrive in a declared layer"; `:407` |

What "the tool agrees" must mean for C1:

1. GAR-01's `garment` string is typed as a translation/display label, not a
   native form; it is not graded on the D2 sound channel (the `/v/` FAIL above
   must disappear or be reclassified as a form-held, not a name violation).
2. The record is still surfaced as unresolved/held (not dropped, not passed) —
   the `(to-verify)` obligation survives.
3. The tool does **not** resolve LEX-GAR-01 to `mirken`: the component states
   `mirken` is the base term and GAR-01 is one of its grades (`:77`), and the
   slot itself is owed (`:407`). A tool that emits `native_form: mirken` for
   GAR-01 fabricates a form the owner has not supplied.
4. If the tool reads 13-naming, it may carry `tolmirken` only as a proposal
   with its pending status (`13-naming.yml:157-171`), never as the adopted
   native form; and the packet does not contain the proposal at all (the
   packet's top-level blocks are listed at `packet.d2.yml:1-3319`; no
   `cross_component_repairs` block, `grep -n tolmirken packet.d2.yml` → no
   match, 2026-10-17).

Divergence modes that would count as findings: (a) English string graded as a
native form; (b) record silently passed/omitted; (c) slot resolved to `mirken`
(the base lexeme) or to any invented form; (d) the held status not represented
in the output; (e) 13-naming's proposal `tolmirken` presented as an adopted
owner form rather than a pending proposal.

## 2. Hand derivation, case C2 — L-26 `kas` (borrowed stratum)

Source record: `examples/culture-d2/components/05-lexicon.yml:562-576`
(packet copy `examples/culture-d2/packet.d2.yml:838-856`).

Locations read:

- `:563` `term: kas` — the D2 surface form.
- `:564` `gloss: "the written tally-sheet demanded at the salt fair (a debt record)"` — English gloss.
- `:566` `layer: loan` — the stratum statement.
- `:567` `route: loan`; `:568` `loan_layer: Salt-road trade layer`.
- `:569` `donor_form: gas` — the donor form, separate from `term`.
- `:570` `stage: E1`.
- `:575` (etymology) "loan from the lowland trade partner, donor gas (the written tally), devoiced g to k on entry".
- `02-phonology.yml:80` consonants `{p, t, k, b, d, g, m, n, s, ʃ, r, l, j, w, h}`; `:136-137` P-2 onset = any single consonant; `:139-140` P-3 coda = exactly `{n, l, r, s}`.

Hand typing:

| property | hand-derived value | basis |
|---|---|---|
| label kind | borrowed-strata label (loan layer) | `:566-568` |
| checked surface form | `kas` (D2-adapted) | `:563`, `:575` |
| donor form | `gas` — donor-side, not a D2 form to check | `:569`, `:575` |
| gloss | translated label, never on the sound channel | `:564` |
| hand phonotactic check of `kas` | licensed: onset /k/ (P-2), vowel /a/, coda /s/ (P-3); one syllable | `02-phonology.yml:136-140` |
| disposition | checked (a surface form is present) | `:563` |

What "the tool agrees" must mean for C2:

1. The record is typed borrowed/loan, with `kas` as the checked form.
2. `gas` is carried as donor-side provenance only; it is not substituted for
   `kas` on the checked channel (it would pass phonotactics too — `g` is in
   the inventory — so a swap is silent unless the typing is explicit).
3. The English gloss is not graded as a form.
4. The loan layer (`Salt-road trade layer`, E1) is preserved in the typed
   output, because the claim "the form arrived by trade loan at E1" is carried
   by the layer, not by the surface string.

Divergence modes: (a) typed native (loan stratum lost); (b) donor form checked
as the D2 form or emitted as `native_form`; (c) gloss graded; (d) `donor_form`
or `loan_layer` dropped from the output.

## 3. Tool run (Part 2) — comparison against the hand derivation

Snapshot (all commands from the lane root):

| item | value |
|---|---|
| tool `tools/d2-typed-labels.py` | sha256 `623b5b1f2f9f50b3e306975b4107b5f70122e86e7d7b41aeca21bcb5a7979b03` |
| artifact `examples/culture-d2/typed-labels.d2.yml` | sha256 `820b75352fb0f20d3a76b523b202e6b8d4a8668f84a85f3fb78ebabb6422f778`, 68,643 bytes |
| run stamp | 2026-10-17T20:24:33Z |

```sh
python3 tools/d2-typed-labels.py --check      # exit 0: "byte-identical deterministic build"
python3 tools/d2-typed-labels.py --selftest   # exit 0: "selftest: 32/32 checks passed"
# in-memory build via importlib for extraction (only the no-flag CLI mode writes;
# the writing mode was NOT run — it would rewrite D02's artifact)
```

Churn record, for honesty: the tool was mid-edit during this review. Hashes
observed 20:15–20:24Z: `d9e084a8` → `080a3b2f` → `a307b84b` → `429191fd` →
`623b5b1f`, with intermediate broken states (`--report` `TypeError: byte
indices must be integers`, `--check` `TypeError: eras_of() missing 1 required
positional argument`, `--selftest` 26/30 at `ee672c28`). The verdicts below are
against the stable snapshot above; the artifact was regenerated at 17:24 local
(the 17:19 artifact first compared was stale and is not used as evidence).

### Case C1 — GAR-01: agrees

| hand-derived expectation (§1) | observed in the artifact | verdict |
|---|---|---|
| label kind = translated label | `LBL-GAR-01 kind: translated-label`, text = the English `garment` string verbatim, `scope: {era_ids: [E0], material: felt}` | agrees |
| not graded on the D2 sound channel | no inventory-type finding names GAR-01; the only GAR-01 finding is the hold below | agrees |
| native form absent; record held, not passed | `LBL-GAR-01-SLOT status: unresolved` + hold `TL-01` "form slot LEX-GAR-01 carries no native form ('(to-verify)'); the label stays unresolved and is not emitted as a native-form" | agrees |
| not resolved to `mirken`; no invented form | `mirken` occurs only in slot/lexeme text; `tolmirken` count 0; `13-naming` count 0 (JSON-string counts over the built artifact) | agrees |

Nuance, not a divergence: the slot label is typed `kind: native-form` with
`status: unresolved` and `required_kind: native-form` — the kind field names
the *required* kind, not a supplied form, and the artifact's own `label_kinds`
rule says a `(to-verify)` placeholder "is unresolved and is never emitted as a
native form". The model is internally consistent; a consumer reading `kind`
without `status` could still misread the placeholder as a form.

### Case C2 — L-26 `kas`: one divergence

| hand-derived expectation (§2) | observed | verdict |
|---|---|---|
| kind = borrowed-strata | `LBL-L-26 kind: borrowed-strata`, text `kas`, `stratum: loan`, `stage: E1` | agrees |
| checked surface form = `kas` (adapted) | `text: kas` (the donor form is not substituted for it) | agrees |
| gloss not on the sound channel | `gloss` carried separately; no finding on it | agrees |
| loan layer preserved | `donor_layer: "Salt-road trade layer"`, `donor: "the lowland farmer trade partner..."`, `contact_window: [E0, E1]` | agrees |
| donor form carried as donor-side provenance | no `donor_form`, no `gas`, no `substitutions` anywhere in the built artifact | **diverges — F-D17-1** |

**F-D17-1 (hold-level, case C2).** The typed label names the layer and the
donor, but not the donor form (`gas`, `05-lexicon.yml:569`) or the layer's
declared substitutions (`g: k`, `packet.d2.yml:2553`), and no borrow-ledger
derivation check runs (`apply({g: k}, gas) == kas`). Evidence: the artifact
block above (JSON-string counts `gas` 0, `donor_form` 0, `substitution` 0);
the tool's only borrow-attachment code is at the pinned hash
`tools/d2-typed-labels.py:376-384` (`extra["donor_layer" | "donor" |
"contact_window"]` — no donor form, no substitution, no derivation). The
design spec this tool is meant to implement requires both:
`reports/round-8/depth/design-spec.md` §1.4 **B2** ("`donor` must separate
ultimate etymon / immediate donor / carrier") and **B3** ("`apply(substitutions,
donor_form)` must equal `text`"; live fixtures `gas→kas`, `bher→per`), with the
§3 diagnostic `D2L-BORROW`; the spec's selftest line for those derivations
(`design-spec.md:504`) is not implemented in the shipped `--selftest` (32/32
pass without it). Consequence: the artifact asserts `kas` is a borrowed-strata
form but cannot itself demonstrate the adaptation that makes it one; the
`gas`→`kas` step is verifiable only by returning to the lexicon component.

### Interface divergences adjacent to both cases (D16 owns the full audit)

**F-D17-2 (vocabulary).** The tool's status vocabulary is `declared` /
`unresolved` (`LBL-GAR-01 status: declared`, `LBL-GAR-01-SLOT status:
unresolved`, `LBL-L-26 status: declared`) and its hold id is `TL-01`, while the
design spec's vocabulary is `supplied | to-verify | absent` (§1.2 L1) and its
expected hold id for exactly this case is `D2L-FORM-UNRESOLVED` (§1.5 table:
GAR-01..10 → `translated-label`, status `to-verify`, `D2L-FORM-UNRESOLVED`
HOLD ×10). Semantics are preserved (the record is held, never silently
passed); a consumer written against the spec's codes (e.g. a validation runner
checking `D2L-*`) will not find them.

**F-D17-3 (layer reference shape).** The label carries `donor_layer:
"Salt-road trade layer"` inline, derived by stage (`donor_layer()`,
`tools/d2-typed-labels.py:431`), rather than the spec §1.4 B1 `layer_ref`
resolving against a packet `layers` block. The name is correct and matches
`packet.d2.yml:2540`, so the intent (name the declared stratum) is met; the
field name and resolution path differ from the spec.

### Limits of this review

- Two cases only, both chosen before the tool existed; no claim about the
  other 92 labels, the era/material reconciliation or the rank-rule adapter.
- Verdicts are pinned to the hashes above; the tool changed five times during
  the review. If it changes again, re-run the three commands and compare
  against §1–§2 of this file.
- I did not run the tool's writing mode; `--check` exit 0 is the equivalent
  evidence that the delivered artifact is byte-identical to the build.
- The old naming gate's ten PHON-INVENTORY FAILs on the English garment
  strings remain live (§0) — that is the gate owner's channel, not this
  tool's; the tool does not edit it.
