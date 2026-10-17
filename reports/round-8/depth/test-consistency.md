# R8-D11 — test-consistency: typed-label output × D2-referenced civilizations entries

- shard: R8-D11 (test) · round 8 (loop 1 of 3, build 1 of 4) · 2026-10-17 · lane: kotodama-shokunin
- writes: this file only. No sibling artifact, no source component, no `tools/` file was edited.
- assignment (targets.json `depth` R8-D06..D11, "Test shards"): cross-check the new
  typed-label output against `corpus/knowledge/civilizations` entries referenced by D2,
  with scoped era/material claims consistent.
- canon: this is a NON-CANON test report over a design drill. Nothing here is a claim
  about any real culture, and nothing here decides lore-shokunin's canon.

## 1. Method and pinned revisions

Two halves, because the cross-check has a tool side and a corpus side:

1. **Corpus side (tool-independent).** Enumerate every site where the D2 design cites a
   `corpus/knowledge/civilizations` entry, verify each cited section resolves, extract the
   scoping rule each entry imposes on labels, and audit the D2 label ledger's own
   era/material scoping against those rules. This half is reproducible today and does not
   depend on `tools/d2-typed-labels.py`.
2. **Tool side.** Run `tools/d2-typed-labels.py`, take its typed-label output, and check
   each label's kind, era scope and material scope against the same rule set plus the D2
   ledger. This half is pinned to the tool revision sha256 that was stable when the check
   ran; the tool was being edited concurrently during the round, and §6 records the drift.

Pinned inputs at read time (2026-10-17):

| input | sha256 (16) | note |
|---|---|---|
| `examples/culture-d2/packet.d2.yml` | `8da90b0788f86fd1` | HEAD worktree copy, matches `tools/assemble-d2.py` output |
| `examples/culture-d2/components/11-costumes.yml` | `b6e2c5c29cc5d689` | label ledger, era reconciliation, materials |
| `examples/culture-d2/components/10-materials.yml` | see §4 command | material arrival eras |
| `tools/d2-typed-labels.py` | `623b5b1f2f9f50b3` | revision R1, stable 20:23:30–20:24:30Z; superseded during the round (§6) |
| `examples/culture-d2/typed-labels.d2.yml` | `820b75352fb0f20d` | artifact written by R1; byte-identical to its in-process build |

Entry digests at read time (`sha256sum corpus/knowledge/civilizations/*.md`, 2026-10-17T20:22:45Z):
`mongol 0c85e10f14f3295d`, `ainu 1142b9116bb6934f`, `finnic-sami 79dd14e82d1bd4fb`,
`inca b68758083ec283a9`, `tibet e9bbf5dadfa2be9e`, `inuit 80926e8fbb43d02e`,
`amazigh-berber 1b5163c7ab1286ba`, `newar-nepal 4856028409e9db02`.

**Line-number caution.** A concurrent metadata sweep (targets.json `metadata_sweep`) is
editing these entries while this shard runs: `mongol.md` gained three frontmatter lines
between two reads (`§Heaven` moved 80→83). Every citation below names the **section
heading**, which is the stable locator; the line numbers are the ones read at the
timestamp above.

## 2. The reference set: 16 sites, 8 entries, all resolved

Command (2026-10-17T20:22:36Z):

```sh
grep -n "corpus/knowledge/civilizations" examples/culture-d2/components/*.yml
```

16 sites in 3 components, citing 8 distinct entries. Resolution check
(resolution script in §7.1): every cited section name was matched against the entry's own
headings; **16/16 resolved, 0 unresolved**.

| site | entry | cited section (heading as it appears) | resolved at |
|---|---|---|---|
| `01-brief.yml:124` | mongol | Heaven, earth, ancestors — sacred lexicon with time-depth | mongol.md:83 |
| `01-brief.yml:125` | ainu | Language family, structure, and writing; Kamuy reciprocity | ainu.md:33 |
| `01-brief.yml:126` | finnic-sami | Language family, writing, and substrate; Sky-god terminology debate; Era model | finnic-sami.md:21 |
| `01-brief.yml:127` | inca | Khipu: record system before a writing verdict | inca.md:44 |
| `01-brief.yml:128` | tibet | Script creation: charter narrative versus historical reconstruction; Era staging: institutions develop on different clocks | tibet.md:35 |
| `01-brief.yml:129` | inuit | Polysynthetic morphology: a generative model, not long-word decoration; Parka/anorak technology | inuit.md:61 |
| `08-symbols.yml:200` | tibet | §5 (media-and-authority audit) | tibet.md:91 |
| `08-symbols.yml:279` | finnic-sami | Sky-god terminology debate: words, offices, and equations | finnic-sami.md:58 |
| `08-symbols.yml:436` | mongol | Symbolic system — anchor meanings to an event | mongol.md:107 |
| `08-symbols.yml:516` | mongol | Heaven, earth, ancestors — sacred lexicon with time-depth; Symbolic system | mongol.md:83 |
| `08-symbols.yml:517` | tibet | §5; §6 (separate timelines for orthography, production, public practice) | tibet.md:91 |
| `08-symbols.yml:518` | finnic-sami | Sky-god terminology debate: words, offices, and equations | finnic-sami.md:58 |
| `12-rank-rules.yml:106` | mongol | Deel and dress code — silhouette, occasion, entitlement | mongol.md:121 |
| `12-rank-rules.yml:107` | amazigh-berber | Tuareg matriliny and the apparent dress inversion | amazigh-berber.md:110 |
| `12-rank-rules.yml:108` | finnic-sami | Gákti: identity map with changing conventions | finnic-sami.md:121 |
| `12-rank-rules.yml:109` | newar-nepal | §6 (Guthi: association, endowment, obligation) | newar-nepal.md:94 |

## 3. The scoping rules each entry imposes, and the check bound to each

Each rule below is quoted from the entry at the line read 2026-10-17T20:23:47Z. The
"bound check" column names the machine-checkable consequence for typed-label output.

| # | entry:line | quoted rule | bound check |
|---|---|---|---|
| R1 | inuit.md:146 | "English “parka” and “anorak” are broad reference labels, not a single universal Inuit garment name; local cut, layer, material, wearer, and task matter." | analyst-language costume labels are typed `translated-label` (never sound-checked); no `translated-label` carries a sound-channel field |
| R2 | inca.md:118 | "Do not confuse **qumpi**, fine cloth, with **chumpi**, a belt; translations and historical spellings need attention." | native forms and translated labels are never merged; loan-stratum forms are typed `borrowed-strata`, native terms `native-form` |
| R3 | tibet.md:135 | "Sheep wool, sheepskin, lambskin, and yak hair are not interchangeable labels." | materials reconcile by slot id, never by label; a label-merge lookup must be refused, not guessed |
| R4 | mongol.md:125 | "Lexical continuity does not prove an unchanged cut, collar, sleeve, or closure arrangement." | a native form carries its stage/era scope; a label never inherits a later era by default |
| R5 | mongol.md:139 | "Separate **documented rule**, **observed preference**, and **design inference**." | adapted rank rules carry authority/jurisdiction/basis and a held reason when a field is undetermined |
| R6 | finnic-sami.md:124 | "…these are socially learned readings, not a universal cryptographic table…" | rank-rule adaptation is per-rule with jurisdiction and exceptions, not a global meaning→rank table |
| R7 | finnic-sami.md:155 | "Date **language, literacy, livelihood, religion, institutions, and dress separately**." | era reconciliation rows carry scope (identity / slot-level / label-level / warning) and a disposition; a `(to-verify)` source row stays held |
| R8 | amazigh-berber.md:126 | "write a dress rule as condition → action → audience interpretation → exception" | executable rules carry jurisdiction (audience), effect (action), wearer_ranks and exempt_ranks (exception) |
| R9 | ainu.md:134 | "Keep textile terms, stitch/loom techniques, garment categories, and motif names as separate lexical fields." | labels are keyed by source field (garment / material / form_slot / gloss / name) and the kind separates a gloss from a form |
| R10 | newar-nepal.md:126 | "Use separate tracks for **political sovereignty, language prestige, script practice, ritual organization, garment silhouette and textile supply**." | unresolved and `(to-verify)` records stay flagged (`status: unresolved`, hold findings), never silently resolved |
| R11 | newar-nepal.md:138 | "Evidence layer | What to record | What it cannot establish by itself" (table) | every output record keeps its status/evidence field; no `to-verify` item is reported as a pass |

These rules are the corpus-side acceptance criteria for the typed-label output; they are
not new requirements invented by this shard — each is D2's own declared use of the entry
(`01-brief.yml:124-129`, `08-symbols.yml:200-518`, `12-rank-rules.yml:106-109`).

## 4. Tool-independent audit: the D2 label ledger's own era/material scoping

Before checking any tool output, the ledger the tool projects must itself be
consistent — otherwise the cross-check would test a moving target. Two checks, both
run 2026-10-17 (reproduce script in §7.2).

### 4.1 Canonicalization (the ERX map)

`11-costumes.yml era_reconciliation` is the lane's own canonicalization table. Its rows:
`ERX-0` (09-eras-calendar: identity, confirmed), `ERX-R` (12-rank-rules: identity,
confirmed), `ERX-1` (10-materials/08-symbols local `E1 shelter era` → `E0`), `ERX-2`
(`E2 road era` → `E1`), `ERX-3` (`E3 assembly era` → `E1 -> E2`, two-to-one), `ERX-4`
(`E4 script era` → `E2`), `ERX-W` (warning: E-numbers do **not** coincide across
components; merge by slot, never by number). The contract tag space is `E0–E3`, and
`11-costumes.yml:56` states `E3` is unoccupied in the costume records.

### 4.2 Costume era vs material arrival

Method: resolve each `GAR-*` record's `material:` through the costume component's own
`CMAT-*` → `maps_to` → `MAT-*` slot chain, take the MAT record's earliest route era
(`routes[].eras`, excluding `excluded_eras`), canonicalize both sides through the ERX
map, and require the costume's era to be inside the material's availability window.

Result (10 garment records): **8 PASS, 2 declared-unmapped, 0 FAIL.**

- The two unmapped are `CMAT-03 pack-ox down` and `CMAT-08 silk`, whose `maps_to` is
  `null` by the component's own declaration ("REPORT, do not merge" — the OQ-3 finding
  already carried in `11-costumes.yml`). They are reported, not silently passed.
- The sharp cases pass on the exclusion side too: `GAR-04` lowland plant-thread cloth at
  `E1` is legal (`MAT-05` route eras `E2,E3,E4` → canonical `E1,E2`; `excluded_eras [E1]`
  → canonical `E0`), i.e. no lowland cloth in `E0`.

### 4.3 Negative controls for the ledger check (isolated, synthetic)

| control | input | expected | observed |
|---|---|---|---|
| POS-1 | `GAR-01` felt `E0` (real record) | PASS | PASS |
| POS-2 | `GAR-04` lowland cloth `E1` (real record) | PASS | PASS |
| NEG-1 | lowland plant-thread cloth **back-projected to `E0`** | `FAIL-excluded-era` | `FAIL-excluded-era` |
| NEG-2 | a `MAT`-space name (`traded-madder-root`) fed as a costume material | `FAIL-no-slot` (must not resolve) | `FAIL-no-slot` |
| NEG-3 | `silk` (unmapped slot) | `DECLARED-UNMAPPED`, never a silent pass | `DECLARED-UNMAPPED` |
| DUP-1 | the same (material, era) receipt twice | both PASS — a benign duplicate is not a collision | PASS, PASS |

## 5. Typed-label output cross-check (tool revision R1, sha `623b5b1f`)

Revision R1 was stable for 90 s (20:23:30–20:24:30Z); every number below was produced
against that revision and its artifact `examples/culture-d2/typed-labels.d2.yml`
(sha256 `820b75352fb0f20d…`, byte-identical to R1's own deterministic build).

### 5.1 Tool health at R1

```sh
python3 tools/d2-typed-labels.py --selftest     # 32/32 checks passed; exit 0
python3 tools/d2-typed-labels.py --check        # byte-identical deterministic build; exit 0
```

Determinism: two in-process builds at R1 serialized to identical bytes
(`sha256 820b7535…`, 68 643 bytes), equal to the artifact on disk.

### 5.2 Output shape

94 labels. Kinds (tool's own registry, `label_kinds`): `native-form` 48,
`translated-label` 19, `descriptive-gloss` 16, `fictional-coordinate` 9,
`borrowed-strata` 2. `labels_unresolved` 26 (16 `descriptive-gloss` + 10 slot
requirements). Findings: 41 (35 hold, 6 note) — `TL-01` 10, `RR-01` 18, `RR-02` 3,
`PR-01` 3, `RC-01` 4, `RC-03` 1, `RC-04` 2. Rank adapter: 3 executable (`WR-02`,
`WR-05`, `WR-09`), 18 held. Coverage: costume rows 10, rank-resolved 7; era rows 7,
held 4; canonical tags referenced `E0,E1,E2`.

### 5.3 Rule-bound checks

| rule | check | result |
|---|---|---|
| R1 (inuit:146) | costume `garment` strings and material names are analyst-language labels: 10 + 9 typed `translated-label`; 0 `translated-label` carries `stage` or `stratum` (the sound-channel fields) | **PASS** |
| R2 (inca:118) | lexicon labels: `stratum: native` → `native-form` (34), `stratum: loan` → `borrowed-strata` (2), sacred/taboo strata → `native-form` (3+1); no label mixes a native and a translated identity | **PASS** |
| R3 (tibet:135) | material rows 9 = 7 `mapped` + 2 `reported-unmapped` (`CMAT-03 pack-ox down`, `CMAT-08 silk`); both label-merge lookups (`pack-ox down`, `felt`) return `unresolved` (refused); slot lookup `CMAT-02` → `MAT-02 felt` resolves | **PASS** |
| R4/R7 (mongol:125, finnic-sami:155) | era rows 7: `ERX-0`/`ERX-R` `confirmed`, `ERX-1..4` `hold` (their source rows are `(to-verify)`), `ERX-W` `warning`; `maps_to` values `E0`, `E1`, `E1 -> E2`, `E2` match the source table row-for-row; canonical tags referenced stop at `E2` (E3 unoccupied, `11-costumes.yml:56`) | **PASS** |
| R5/R6/R8 (mongol:139, finnic-sami:124, amazigh:126) | all 3 executable rules carry `authority`, `jurisdiction`, `eras`, `rites`, `effect`, `property`, `wearer_ranks`, `exempt_ranks` (plus `basis` and residual-clause fields); all 18 held rules carry a `hold_reason` with a verbatim `span` (e.g. `WR-01` → `grade-not-expressible`) | **PASS** |
| R9 (ainu:134) | labels are keyed by source field (`garment` / `material` / `form_slot` / `gloss` / `name`) and glosses are a separate kind (`descriptive-gloss`) from forms | **PASS with caveat** — see finding F1 |
| R10/R11 (newar:126,138) | 26 unresolved labels stay `status: unresolved`; `(to-verify)` era rows stay held; nothing unresolved is reported as a pass | **PASS** |
| §4 ledger audit | the tool's material rows reproduce exactly the independent audit of §4.2 (7 mapped + 2 reported-unmapped = 8 PASS + 2 declared-unmapped, 0 FAIL); costume projection matches the packet components on `era` + `material` for all 10 rows (0 mismatches) | **PASS** |

### 5.4 Findings from the cross-check

- **F1 (medium at R1; resolved at R2).** At R1 the 10 `form_slot` requirements are emitted
  as `kind: native-form` with `status: unresolved`, but their `text` is the requirement
  string itself (e.g. `LBL-GAR-01-SLOT` = "LEX-GAR-01, the valley grade of L35 mirken
  (to-verify with 05-lexicon)"). A consumer dispatching on `kind` alone (the defect class
  of `ASSEMBLY.md:94` and R1/inuit:146) would phonologically test English requirement
  text; and R1's own `TL-01` message ("…is not emitted as a native-form") contradicts the
  emitted record. **At R2 the requirements are no longer emitted as labels at all** — they
  become `D2L-FORM-UNRESOLVED` holds (§5.5), which closes F1. If the frozen revision keeps
  the R2 architecture, no fix is needed; if it reverts to R1's, the message/record
  contradiction stands.
- **F2 (info, D01↔D02 divergence; resolved at R2).** `reports/round-8/depth/design-spec.md`
  §1.1 fixes the kinds as "exactly three" (`native-form`, `translated-label`,
  `borrowed-strata`); R1 emitted five (`fictional-coordinate` 9, `descriptive-gloss` 16
  added) in its own `label_kinds` registry. **R2 emits exactly the three spec kinds**
  (§5.5), so the delta is closed in the newer architecture.
- **F3 (info).** Earlier in the same window the tool emitted 4 labels with `kind: null`
  (`L-30..L-33`, sacred/taboo lexicon terms) under `TL-02` holds; R1 types them
  `native-form` (and R2 likewise). Resolved within the window, recorded for the drift
  history.
- **F4 (info, not a defect).** R1 held 18 of 21 prose rules and projected 3 executable
  rules (7/10 costume rows rank-resolved); R2 projects 5 gate rules from 21 component
  rules (9 normalized, 13 unresolved items, 3 quarantine handles) and raises 4
  `R-RANK-CONFLICT` items (3 hold, 1 note). Neither revision claims an un-evaluated rule
  as a pass; the D claim should quote the revision's actual numbers, not "21 rules
  adapted".

### 5.5 Re-check against revision R2 (sha `e9209f28`, run 20:31:53–20:32:03Z)

The tool was re-architected again after R1 (spec-conformant schema, new CLI
`--packet/--json/--emit`, `run_pipeline`). Re-running the same rule set against R2:

```sh
python3 tools/d2-typed-labels.py --selftest   # 34/34 checks passed; exit 0 (20:31:32Z)
# in-process: run_pipeline('examples/culture-d2/packet.d2.yml') -> exit 1 (holds present)
```

| rule | R2 observation | result |
|---|---|---|
| R1 (inuit:146) | `translated-label` 10 = the 10 `garment` strings, `representation: english-gloss`, `scheme: null` with the issue note "english-gloss needs no romanization scheme"; the sound channel is not applied to them | **PASS** |
| R2 (inca:118) | lexicon 40 labels: 38 `native-form` (incl. sacred/taboo strata), 2 `borrowed-strata` (L-26, L-27 = the loan layer); kinds are exactly the spec's three | **PASS** |
| R3 (tibet:135) | materials are **not** merged: all 9 `CMAT-*` records carry a `R-MAT-BRIDGE-MISSING` hold (the CMAT→MAT bridge is absent from the packet), and per-record material claims resolve only to the costume-side `CMAT-*` id. Conservative and consistent with "not interchangeable labels"; note R2 does not perform the cross-inventory slot merge that R1 did | **PASS (held, not merged)** |
| R4/R7 (mongol:125, finnic-sami:155) | era/material reconciliation: 10 records, each era `R-ERA-IN-SCOPE` with its tag; era aliases applied from the components' own table | **PASS** |
| R5/R6/R8 (mongol:139, finnic-sami:124, amazigh:126) | rank rules: 21 component rules → 9 normalized → 5 gate-projected; conflicts surfaced as `R-RANK-CONFLICT` (e.g. `WR-02#g|WR-09#g` "genuine-priority-gap", hold) rather than silently resolved | **PASS** |
| R9 (ainu:134) | no `native-form` carries English requirement text (0 of 46) | **PASS** |
| R10/R11 (newar:126,138) | 10 `D2L-FORM-UNRESOLVED` holds for the slots; 2 `D2L-NATIVE` holds for `sára`/`sará` (the acute accent is declared by `02-phonology.yml:73`'s minimal pair; the tool holds for the form's owner instead of failing the segment inventory — a calibrated call); `stats: labels 58, fail 2, hold 10` | **PASS** |
| §4 ledger audit | R2 does not reproduce §4.2's CMAT→MAT resolution (it holds the bridge instead); the §4.2 audit therefore remains the independent ledger check, and its result (8 PASS / 2 declared-unmapped / 0 FAIL) is unchanged | **note** |

R2 therefore keeps every rule-bound check passing while resolving F1 and F2; its one
difference from R1 is that the CMAT→MAT slot merge is held rather than performed. The
revision churn continued after this run: at 20:32:25Z the tool was again mid-edit
(sha `46ad603d`) and `run_pipeline` raised `Malformed: cannot read
examples/culture-d2/components/11-costumes.yml`.

## 6. Revision drift during the cross-check window

The tool was being written by its owner shard (R8-D02) while this test ran. Observed
states, `sha256sum tools/d2-typed-labels.py`:

| time (UTC) | sha256 (16) | state |
|---|---|---|
| 20:19:5x | `13e828571a2a283f` | `--selftest` 26/30; earlier revision of the same window crashed every path with `NameError: name 'assemble' is not defined` (line 1132) |
| 20:21:2x | `ae0cb050e1fc277b` | mid-edit: `TypeError: adapt_rules() missing 1 required positional argument: 'tag_space'` |
| 20:22:0x–20:23:0x | `da86132e`, `097a23a3`, `623b5b1f` | settling |
| 20:23:30–20:24:30 | `623b5b1f2f9f50b3` | **stable 90 s; revision R1 used for §5**; `--selftest` 32/32, `--check` byte-identical |
| 20:25:4x | `56c0db1423f2aac1` | re-architected again (new CLI `--packet/--json/--emit`; `build_artifact` removed) |
| 20:27:1x | `d98731f8754954a4` | mid-edit: `run_pipeline` raises `KeyError: 'source_rule'` inside `conflicts()` |
| 20:31:3x | `e9209f280c6d7655` | **revision R2** (spec-conformant: exactly 3 kinds, new projection schema); `--selftest` 34/34; artifact regenerated (`typed-labels.d2.yml` sha `59a53456…`); re-checked in §5.5 |
| 20:32:2x | `46ad603dff462e55` | mid-edit: `run_pipeline` raises `Malformed: cannot read examples/culture-d2/components/11-costumes.yml` |

The artifact on disk changed with R2 (`820b7535…` → `59a53456…`), so §5's byte-identity
claims apply to the R1 artifact only; R2's own `--check` should be re-run by the parent.

Consequence for the parent: the D-claim validation must pin the tool sha. A validation
run against a moving file can report pass or fail depending on the minute. §5 records
the revision it used; §7 carries the re-run commands and the expected values to compare.

## 7. Reproduce

Corpus side (any time; the entries may have moved lines, match by heading):

```sh
# 7.1 reference sites and section resolution (ran 2026-10-17T20:22:36Z; 16/16 resolved)
grep -n "corpus/knowledge/civilizations" examples/culture-d2/components/*.yml
python3 - <<'PY'
import re, pathlib
cites=[]
for f in sorted(pathlib.Path('examples/culture-d2/components').glob('*.yml')):
    for i,line in enumerate(f.read_text().splitlines(),1):
        for m in re.finditer(r'corpus/knowledge/civilizations/([a-z-]+)\.md\s*(§[^"\(\)]*|§\d+)', line):
            cites.append((f.name, i, m.group(1), m.group(2).strip()))
heads={}
for name in sorted({c[2] for c in cites}):
    p=pathlib.Path(f'corpus/knowledge/civilizations/{name}.md')
    heads[name]=[(i,l.strip()) for i,l in enumerate(p.read_text().splitlines(),1) if l.startswith('#')]
def resolve(name, sec):
    sec=sec.replace('§','').strip()
    pat = re.compile(r'^#+\s*'+sec+r'\.') if re.fullmatch(r'\d+', sec) \
          else re.compile(re.escape(sec.split('(')[0].split('—')[0].strip().strip("'\"")[:28]), re.I)
    return next(((i,h) for i,h in heads[name] if pat.search(h)), None)
print("sites:", len(cites), "| resolved:", sum(1 for c in cites if resolve(c[2], c[3])))
PY

# 7.2 independent era/material audit (ran 2026-10-17T20:17:51Z; 8 PASS / 2 declared / 0 FAIL)
# resolve each GAR material: 11-costumes CMAT-* -> maps_to -> 10-materials MAT-*
# take routes[].eras minus excluded_eras, canonicalize via the 11-costumes ERX map
# (local E1->E0, E2->E1, E3->E1|E2, E4->E2), require costume era in the window
python3 - <<'PY'
import re, pathlib
c11 = pathlib.Path('examples/culture-d2/components/11-costumes.yml').read_text()
m10 = pathlib.Path('examples/culture-d2/components/10-materials.yml').read_text()
mat = {}
for b in re.split(r'\n  - id: MAT-', m10.split('\nmaterials:')[1].split('\nbulk_materials:')[0])[1:]:
    mid = 'MAT-'+b[:2]
    avail = set()
    for rm in re.finditer(r'\{id: RT-\S+.*?eras: \[([^\]]*)\]\}', b):
        avail |= {e.strip() for e in rm.group(1).split(',') if e.strip()}
    exc = re.search(r'\n    excluded_eras: \[([^\]]*)\]', b)
    mat[mid] = (avail, {e.strip() for e in exc.group(1).split(',')} if exc else set())
canon = {'E1':'E0','E2':'E1','E3':'E1/E2','E4':'E2'}
cset = lambda es: {x for e in es for x in canon.get(e,'?').split('/')}
cmat = {}
for m in re.finditer(r'- id: (CMAT-\d+)\n    material: "?([^"\n]+)"?\n(?:.*\n)*?    maps_to: "?([^"\n]+)"?',
                     c11.split('\nmaterials:')[1].split('\ncloth_sources:')[0]):
    t = re.search(r'(MAT-\d+)', m.group(3))
    cmat[m.group(2).strip()] = t.group(1) if t else None
n2c = {v:k for k,v in cmat.items()}
for b in re.split(r'\n  - id: GAR-', c11)[1:]:
    gid='GAR-'+b[:2]
    mm=re.search(r'\n    material: "?([^"\n]+)"?', b); em=re.search(r'\n    era: "?([^"\n]+)"?', b)
    mname, era = mm.group(1).strip(), em.group(1).strip()
    tgt = cmat.get(mname)
    if tgt is None: print(gid, 'DECLARED-UNMAPPED'); continue
    av, ex = mat[tgt]
    ok = era in cset(av) and era not in cset(ex)
    print(gid, 'PASS' if ok else 'FAIL', era, mname, '->', tgt)
PY
```

Tool side (ran against R1, sha `623b5b1f`; expected values are §5's):

```sh
sha256sum tools/d2-typed-labels.py            # must equal 623b5b1f… to reproduce §5
python3 tools/d2-typed-labels.py --selftest   # expect: 32/32 checks passed, exit 0
python3 tools/d2-typed-labels.py --check      # expect: byte-identical deterministic build, exit 0
# then, against the frozen revision's own API:
#   R1 API: build_artifact() -> {"labels": [...], "era_reconciliation": {...},
#           "material_reconciliation": {...}, "rank_rule_adapter": {...}, "coverage": {...}}
#   check: costume labels are translated-label/descriptive-gloss only;
#          lexicon stratum native -> native-form, loan -> borrowed-strata;
#          material rows = 7 mapped + 2 reported-unmapped; era rows = 7 with
#          ERX-0/R confirmed, ERX-1..4 hold, ERX-W warning; 3 executable rules
#          carrying jurisdiction/effect/wearer_ranks/exempt_ranks.
```

If the frozen revision exposes the newer `run_pipeline(packet_path)` API instead, the
same checks run over `result["projection"]` / `result["json_document"]`; the checks are
schema-level, and §5 states the values to expect.

## 8. Limits and open items

- **Revision pinning is the main limit.** §5's numbers hold for tool sha `623b5b1f` and
  artifact sha `820b7535` (revision R1); §5.5's for `e9209f28` (R2, stable only ~60 s).
  The tool kept changing for the whole window (§6: 15+ distinct shas, several mid-edit
  crash states). The parent must re-run §7 against the frozen revision and compare to
  §5/§5.5 before the D claim is validated. A red re-run against a later revision is a
  D02 defect, not a contradiction of this report.
- **Line numbers in the corpus shift under the concurrent metadata sweep.** §3's quotes
  are matched by section heading; the quoted text itself was read 2026-10-17T20:23:47Z.
- **This shard checked label typing and scoping only.** It did not re-verify the D2
  design's phonology, morphology, or myth content, and it makes no claim that the
  referenced entries' own statements are true — it checks that D2's use of them is
  scoped the way the entries require.
- **F1 is resolved in R2, open in R1.** If the frozen revision keeps the R2 architecture
  (slot requirements held as `D2L-FORM-UNRESOLVED`, never typed), F1 needs no fix; if it
  reverts to R1's emission, the native-form typing of English requirement text stands as
  the one cross-check finding touching the defect class the capability exists to close.
- The ledger audit's NEG-2 control exercises slot-name resolution, not a real packet
  contradiction; the real exclusion case is NEG-1 (lowland cloth back-projected to `E0`).
