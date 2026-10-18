# R25-D02 — what D4 actually declares today (the argot surfaces, measured)

Worker: R25-D01..D04 (D axis, argot analysis). Round 25, 2026-10-18.
All commands run with `export TMPDIR=$PWD/.scratch`, cwd = lane root
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Worktree revision
`f74fc9403d4b02c8ee76439eb133e3dea9b65b14`, `git status --porcelain` empty (clean at measurement).

Every count below is of the **delivered** tree unless a path says `reports/round-17/`.

## 0. Digests of the surfaces measured

```
sha256sum examples/culture-d4/components/04-lexicon.yml examples/culture-d4/components/05-naming.yml \
          examples/culture-d4/packet.d4.yml examples/culture-d4/packet.d4.typed.yml \
          tools/gates/lexicon-coverage-audit.py tools/gates/naming-collision-gate.py
```

| surface | sha256 |
|---|---|
| `examples/culture-d4/components/04-lexicon.yml` | `74c2561b7c875c7c98708c589002b85b7989fc64bafa6abf794210401c69a9a5` |
| `examples/culture-d4/components/05-naming.yml` | `b154d80700c47719dcf8395f6017f68c00c21a5eea79965d205df4bdbb688e0c` |
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` |
| `examples/culture-d4/packet.d4.typed.yml` | `ffece0feb52c5b0b8ae6b0f8c1848d6220ad2dc2b36b1faac6385d62f4bfd84e` |
| `tools/gates/lexicon-coverage-audit.py` | `2c4dd39702a15ea3fa62d3597fe42304e3bda4122d7b17d6c00121f9d27d4287` |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |

## 1. The component the writer owns — `04-lexicon.yml`

`04-lexicon.yml` is the only component that declares morphology
(`grep -ln "^morphology:" examples/culture-d4/components/*.yml` → `04-lexicon.yml`).

**`constructions:` block, lines 55-83** — exactly three, and this is the whole registry:

| id | name | `pattern` | base classes | available_from |
|---|---|---|---|---|
| CX-01 | STACK-COMPOUND | `B1-B2` | noun | E0 |
| CX-02 | CRAFT-AGENT | `B1-ar` | noun | E0 |
| CX-03 | ATTRIBUTIVE | `B1-en` | noun | E0 |

Each also carries `description`, `productivity`, `base_eligibility: native-only`, `axis`,
`evidence`, `follows`.

**`morphology.derivation_rules:` block, lines 192-195** — the machine-readable pattern/output
pairs the naming gate replays:

| id | kind | pattern | output | note |
|---|---|---|---|---|
| CX-01 | compound | `^(?P<a>.+)\+(?P<b>.+)$` | `{a}{b}` | STACK-COMPOUND … |
| CX-02 | suffix | `^(?P<stem>.+)$` | `{stem}ar` | CRAFT-AGENT … |
| CX-03 | suffix | `^(?P<stem>.+)$` | `{stem}en` | ATTRIBUTIVE … |

`derivation_note` (`:196`): "the three rules replay the four derived or compound records in this
file and the eight names in 05-naming; rule ids match the constructions block."

That is the entire declared morphology. **No `head2`, no `reverse`, no argot operation of any
kind.** Counts:

```
grep -c "ARGOT\|argot\|head2\|reverse\|derived_from" examples/culture-d4/components/04-lexicon.yml   # → 0
grep -c "ARGOT\|argot\|head2\|reverse\|derived_from" examples/culture-d4/components/*.yml | paste -sd+   # → 0 across all 12
```

The omission is **not** landed-vs-design drift: `wc -l` gives 219 lines for both
`reports/round-17/d4/components/04-lexicon.yml` and `examples/culture-d4/components/04-lexicon.yml`,
and the design-side copy declares the same three CX rules (`:56,68,80,193-195`) and no argot rule.
The round-17 design *components* never carried the argot operations either.

## 2. The register fields that exist, and the ones that do not

The forecast's Δ1 asked the register law to live in a `06-register-contract.yml` with packet keys
`registers` and `doublets`, and asked "each lexeme carries `register: plain|quote` and `era_ids`"
(`design-brief.md:232,236`). Measured:

| register surface | present? | count / evidence |
|---|---|---|
| `registers` top-level packet key | **no** | `grep -c "registers" examples/culture-d4/packet.d4.yml` → 1, and that one hit is the prose string `"…signs couple to the craft and law registers"` inside `provenance` (`:2211`), not a key |
| `doublets` key | **no** | `grep -c "doublets" examples/culture-d4/packet.d4.yml` → 0 |
| `register:` on a **lexicon record** | **no** | `register:` lines inside the `lexicon:` block → 0; the packet's own `contract.record_fields.lexicon` list (`id, term, gloss, field, route, bases, construction, layer, stage, axis, evidence, follows`) has **no** `register` field |
| `register:` on a **layer** (`LY-01`, `LY-02`) | yes | `04-lexicon.yml:103` (`trade`), `:117` (`craft`) — a loan-layer field, not a form's register |
| `register:` on **symbols** | yes | `07-symbolism.yml:28-35`, eight `SYM-*` rows (`"craft and law"`, `"public"`, `"ritual"`, `"trade"`, …); `register` is in the packet's `contract.record_fields.symbols` |
| `slot_ref` / `doublet_of` / `<id>#plain` / `<id>#quote` | **no** | `grep -c "slot_ref" examples/culture-d4/packet.d4.yml` → 0; `doublet_of` → 0; `#plain`/`#quote` → 0 |
| `form_slots` | yes, D2-shaped | 6 slots `LEX-GAR-01..06`, `kind_owed` `native-form` ×5 + `borrowed-strata` ×1, `status: unfilled`, `owner: GAR-0n` (`packet.d4.yml:2124-…`) |

So the register half of the argot design is present only as (a) a **loan-layer** `register` field
and (b) the D2-era `form_slots` block. The **register-scoped slot** of Δ1 — a `<id>#quote` slot a
supplied quote form may occupy — does not exist as data anywhere.

## 3. The packet the gates read — `packet.d4.yml`

Top-level keys (34, `grep -E "^[a-z_]+:" | wc -l`):
`name, canon, contract, phonology, morphology, orthography, lexicon, layers, constructions,
cloth_sources, pantheon, roles, motifs, narratives, calendar, festivals, rites, symbols, materials,
costumes, rank_rules, eras, era_records, era_dates, source_era_dates, named_eras, names,
cross_culture_review, form_slots, provenance, contact, routes, era_tags, assembly`.

Against the design's §4 packet shape (`design-brief.md:243`), which asked for D2's key set **plus**
D4's `registers`, `doublets`, `measures`, `oaths`: `registers` **ABSENT**, `doublets` **ABSENT**,
`measures` **ABSENT**, `oaths` **ABSENT**; `sayings` **ABSENT** (the delivered packet uses
`motifs`/`narratives`). The design's D4-specific key set was not built.

`lexicon:` — **54 records** (`grep -c 'term: "'` → 54; `grep -c '^  - $'`-style id scan → 54 `L-` ids):

| route | count |
|---|---|
| root | 43 |
| derived | 2 (`L-46 mesar` CRAFT-AGENT, `L-47 kalen` ATTRIBUTIVE) |
| compound | 2 (`L-45 tikmes`, `L-48 haitun`, both STACK-COMPOUND) |
| borrowed | 6 (`L-49..L-54`) |
| lexicalized | 1 (`L-05 mam`) |

Only those **4** records carry `bases` + `construction`; the rest carry neither. There are no
`derived_from` / `derivation` fields anywhere (`grep -c` → 0).

`names:` — **8** records (`NM-01..NM-08`), every one with a `formation` block whose `rule` is
`"CX-01"` and whose `operation` is `"concatenate"` (`rule` value census: `{CX-01: 8}`;
`operation` census: `{concatenate: 8}`). No `quote` key on any name record
(`grep -c "quote"` inside the `names:` block → 0), so the design's eight quote names have no home
in the schema.

## 4. The argot-specific token census (the headline measurement)

```
for t in ARGOT argot head2 reverse derived_from derived_forms derived_ok doublet_of slot_ref; do
  printf "%-14s packet=%s typed=%s components=%s tools=%s\n" "$t" \
    "$(grep -c -- "$t" examples/culture-d4/packet.d4.yml)" \
    "$(grep -c -- "$t" examples/culture-d4/packet.d4.typed.yml)" \
    "$(grep -rho -- "$t" examples/culture-d4/components/*.yml | wc -l)" \
    "$(grep -rho -- "$t" tools/*.py tools/gates/*.py | wc -l)"; done
```

| token | packet.d4.yml | packet.d4.typed.yml | components | tools/ |
|---|---|---|---|---|
| `ARGOT` | 0 | 0 | 0 | 0 |
| `argot` | 0 | 0 | 0 | 0 |
| `head2` | 0 | 0 | 0 | 0 |
| `reverse` | 0 | 0 | 0 | 6 (all `sorted(..., reverse=True)`, unrelated) |
| `derived_from` | 0 | 0 | 0 | 0 |
| `derived_forms` | 0 | 0 | 0 | 0 |
| `derived_ok` | 0 | 0 | 0 | 0 |
| `doublet_of` | 0 | 0 | 0 | 0 |
| `slot_ref` | 0 | 0 | 0 | 7 (`tools/d2-typed-labels.py` rank-property `slot_ref`, a D2 mechanism, not the D4 register slot) |

The only `derived_from` in the repo is in unrelated documents (`examples/handoff-packet.sample.yml:31`
and `corpus/knowledge/synthesis/worldbible-integration-contract.md:151`, both about handoff revision
references). `derivation` occurs twice in the packet — `morphology.derivation_rules` and
`morphology.derivation_note` (`:205`, `:226`) — and nowhere else.

**Staleness note (2026-10-18T17:32Z).** This table is a snapshot of worktree `f74fc94` at
2026-10-18T17:25Z. At 17:31Z a sibling seat landed `tools/gates/argot-derivation-gate.py`, which
carries `head2`, `reverse`, `derived_from` and `D4L-ARGOT-DERIV`. The **`tools/` column is therefore
stale**; the `examples/` and packet columns are not (the delivered tree still has none of it). See
`delta.md` §8 for the re-measured values. The `examples/`-side findings — no argot data, no
`derived_from` field on any delivered record — are what this file exists to establish, and they are
unchanged.

### 4.1 The 11 forecast bases and quote forms, against the delivered lexicon

```
python3 -c "import re; lex=open('examples/culture-d4/packet.d4.yml').read().split('\nlexicon:',1)[1].split('\nlayers:',1)[0]; print(re.findall(r'term: \"([^\"]+)\"',lex))"
```

| forecast base | delivered as `term:`? | forecast quote form | delivered? |
|---|---|---|---|
| saalumi | no | saalu | no |
| min | no | nim | no |
| kus | no | suk | no |
| nam | no | man | no |
| nes | **yes** (`L-16 nes`, an unrelated body word) | sen | no |
| sam | **yes** (`L-39 sam`, charcoal) | mas | no |
| mus | no | sum | no (`sum` exists as `L-32`, gloss "soul, shade" — an accidental string match, not a quote form) |
| kin | no | nik | no |
| sun | no | nus | no |
| samun | no | numas | no |
| makun | no | nukam | no |

The design-language ids `D4-X02`, `D4-X13..X22` occur in **zero** files under `examples/` or
`tools/` (`grep -rl "D4-X" examples/ tools/` → 0 files): the delivered packet renumbers the same
records `L-nn`, and neither numbering carries the argot pair.

Likewise the six argot loan forms (`design-language.md:406-424`) are not delivered as such:
`res` and `kan` occur as unrelated lexemes (`L-52 res` = bale; `L-34 kan`), `gun`/`suk`/`man`/`nis`
occur 0 times, and `AL-0` occurs once in the packet — inside `CAL-01`. The eight quote names
(`inak, usam, urin, akas, akim, aruk, isun, asum`) occur 0 times each.

## 5. The typed artifacts

`packet.d4.typed.yml` adds `schema`, `typed_channel`, `typed_assembly`, `pipeline_findings`,
`pipeline_counts` to the 34 keys above. `typed_channel` holds **12** rows, every one
`kind: "translated-label"`, `channel: "off-sound-and-identity"`, `hold: "D2L-FORM-UNRESOLVED"`,
`owed_slot: null`; the 12 `where`s are the six `GAR-0n` records and the six `LEX-GAR-0n` labels.
There is no register row and no `D4L-*` row of any class. (The 6 `D4L-FORM-UNRESOLVED` strings that
`grep` finds in this file are the *declaration* echoed through `contract` — see `delta.md` A-11 —
not emitted findings; the 37 `D2L-FORM-UNRESOLVED` are the findings.)

`expected-holds.json`: `counts {hold: 12, note: 0, fail: 0}`, all 12 rows `D2L-FORM-UNRESOLVED`
(`revision_note` records the round-22 D source repair; pins `packet_sha256 e7ecd204…`,
`projection_sha256 60b526b0…`, `projector_sha256 2819f687…`).

### 5.1 The D4L-* vocabulary: declared in design, absent from the delivered tree

```
for id in D4L-ARGOT-DERIV D4L-REGISTER-UNRESOLVED D4L-ERA D4L-NATIVE D4L-DATA D4L-SCOPE \
          D4L-BORROW D4L-MATERIAL D4L-RANK D4L-FORM-UNRESOLVED; do
  printf "%-26s examples=%s tools=%s r17=%s\n" "$id" \
    "$(grep -rl -- "$id" examples/ | wc -l)" "$(grep -rl -- "$id" tools/ | wc -l)" \
    "$(grep -rl -- "$id" reports/round-17/ | wc -l)"; done
```

| id | files in `examples/` | files in `tools/` | files in `reports/round-17/` |
|---|---|---|---|
| `D4L-ARGOT-DERIV` | **0** | **0** | 2 |
| `D4L-REGISTER-UNRESOLVED` | **0** | **0** | 10 |
| `D4L-ERA` | **0** | **0** | 8 |
| `D4L-NATIVE` | **0** | **0** | 9 |
| `D4L-DATA` | **0** | **0** | 4 |
| `D4L-SCOPE` | **0** | **0** | 5 |
| `D4L-BORROW` | **0** | **0** | 10 |
| `D4L-MATERIAL` | **0** | **0** | 9 |
| `D4L-RANK` | **0** | **0** | 9 |
| `D4L-FORM-UNRESOLVED` | 5 | 13 | 16 |

The `D4L-*` vocabulary exists **only in the round-17 design documents**, with one exception:
`D4L-FORM-UNRESOLVED` is the only id the live engine carries. `D4L-ARGOT-DERIV` is not produced by
any code path.

## 6. What actually replays a derivation today

Two live gates do derivation replay, and **neither knows an argot operation**.

### 6.1 `tools/gates/naming-collision-gate.py` — gate C, name formations

Reads `morphology.derivation_rules` (`:1206-1220`) into an id→rule table, then for each `names[]`
record with a `formation` (`:1359-1370`) replays the rule's packet-authored `pattern` (a regex run
under a match budget) and `output` (a packet-authored `str.format` template) against
`formation.stem`, comparing to `formation.expected` / the record's form. Ids emitted:
`DERIV-AFFIX` (rule id or affix not licensed by morphology), `DERIV-REPLAY` (chain does not yield the
candidate), `DERIV-HOLD` (no replayable evidence / pattern over budget / template outside the
accepted subset).

Measured over the D4 packet:

```
python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml
```
→ exit **1**; finding ids `CROSS-HOLD` ×1, `NAME-NEAR` ×7, `PHON-INVENTORY` ×6, and
`grep -ci "deriv"` on the output → **0**. So all 8 names' declared CX-01 chains replayed clean; the
exit-1 is the name/collision/costume-name legs, not the replay leg.

`--selftest` → `selftest: OK — fixture findings 12 across 11 ids (CROSS-HOLD, DERIV-AFFIX,
DERIV-HOLD, DERIV-REPLAY, NAME-LEXEME, NAME-NEAR, NAME-REUSE, NAME-VISUAL, PHON-CODA,
PHON-INVENTORY, PHON-ONSET)`.

Note the gate reads `formation` only — **never a lexicon record's `bases`/`construction`** — so it
cannot grade a quote form even if one were added as a lexicon record.

### 6.2 `tools/gates/lexicon-coverage-audit.py` — leg D, lexicon derivations

Reads `constructions` (`:664`) and, per lexicon record, replays `bases` against
`construction.pattern` by substituting `B1`, `B2`, … then stripping `+` and `-` (`:740-880`). Ids:
`D-route-missing`, `D-rule-underspecified`, `D-form-mismatch`, `D-rule-violation`,
`D-meaning-mismatch`, `D-exception-unlicensed`, `D-stage-mismatch`.

Measured over the D4 packet:

```
python3 tools/gates/lexicon-coverage-audit.py examples/culture-d4/packet.d4.yml ; echo $?
```
→ exit **0**, **no output** (the 4 CX-class records all reproduce). `--selftest` → `14/14 checks
passed`.

The replay model is the point: for each record the audit takes `construction.pattern`, substitutes
`B1`…`Bn` with the base terms, then does `expected.replace("+", "").replace("-", "")` and compares to
the record's `term`. It is a **concatenation** replayer, with no operation field and no
alternate-operation branch.

**Controls (mine, in `TMPDIR=$PWD/.scratch`, all scratch copies — the delivered tree untouched):**

| # | fixture | result |
|---|---|---|
| N-1 | `.scratch/r25d/neg-deriv.yml` — delivered packet with `L-46 mesar` → `mesor` | `FINDING D-form-mismatch: 'mesor' does not reproduce from bases mes under construction 'CRAFT-AGENT' (expected 'mesar'); recorded form and rule disagree`, exit **1** |
| N-2 | `.scratch/r25d/ctrl-argot-constructions.yml` — `ARGOT-REVERSE` declared in `constructions` with `pattern: "B1"`, plus a base `L-55 min` and a derived record `L-56 nim` from base `min` (the **correct** reversal) | `FINDING D-form-mismatch: 'nim' does not reproduce from bases min under construction 'ARGOT-REVERSE' (expected 'min')`, exit **1** |
| N-3 | same, with the record's form set to `min2` (a **wrong** reversal) | identical `D-form-mismatch … (expected 'min')`, exit **1** |

N-2 is the load-bearing measurement: the audit's replay model is **concatenation only** (substitute
`B1`…, strip `+`/`-`). Under it a correct `reverse` derivation and a wrong one produce the *same*
finding, and the correct one is a **false FAIL**. So the argot operation class is not merely
missing — it is **not representable** in the live replay engine, and a naive addition of
`ARGOT-REVERSE` to `constructions` would manufacture a red row on a correct packet.

### 6.3 The typed gate

```
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1
```
→ `summary: 19/19 legs passed` (L1-profile, L1-assembler, L1-expected-holds, L1-build, L1-schema,
L1-routing, L2-channel, L2-retention, L3-holds, L3-notes, L3-fails, L3-counts, L3-baseline,
L3-details, L3-baseline-set, L3-routing-consistency, L4-pins, …). `grep -c "ARGOT"` on its output
→ **0**. Its L3 legs compare the observed finding set against `expected-holds.json`; with no argot
leg and no `D4L-*` id in the engine, the leg has nothing to grow from.

## 7. Counting commands for this file

```
sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/packet.d4.typed.yml \
          examples/culture-d4/components/04-lexicon.yml tools/gates/lexicon-coverage-audit.py
grep -n "CX-0\|derivation_rules\|derivation_note" examples/culture-d4/components/04-lexicon.yml
grep -c "ARGOT\|head2\|reverse\|derived_from\|derived_forms\|derived_ok" examples/culture-d4/packet.d4.yml
python3 tools/gates/lexicon-coverage-audit.py examples/culture-d4/packet.d4.yml ; echo "exit=$?"
python3 tools/gates/lexicon-coverage-audit.py .scratch/r25d/neg-deriv.yml ; echo "exit=$?"
python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml | grep -ci deriv
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1
```
