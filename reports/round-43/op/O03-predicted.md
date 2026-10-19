- Seat: O03 | executor (claim O) | date 2026-10-19 | baseline `7ceff59`
- Mission (verbatim, `reports/round-43/targets.json` → `seats[id=O03].mission`): *"Predicted census: dry-run the resolver logic against the live corpus by hand/script-in-scratch; predict the four-class totals and name every expected fallback mapping + every expected unresolved/ambiguous token, citing the r37/r39 filed counts (334/319/15) as the comparison baseline."*
- Out path: this file. Scratch only: `.scratch/o03/` (`predict.py`, `predict.out`; `predict.py` sha256 `7a3be4f9032aa24fae28fc449e3918523cc687ce9f90cc144964e116e0b5bf29`). Zero bytes written outside this file and disposable scratch; no `corpus/**`, `tools/**`, or filed-round byte; no `reports/round-*/run-validation.py` executed; no git commit/push, no install, no network.
- Status: **prediction**. The durable instrument does not exist yet at this baseline; O01 authors it and its `--census` run is the authoritative corrected census. This file gives the numbers and every named row that instrument must reproduce, plus the exact assumptions under which they hold.

# O03 — predicted basename-couples census (live corpus, 223 entries)

## 0. Headline

At live tree `7ceff59` — 223 knowledge entries, partition vector `25/26/25/29/24/94` — the r39 basename-couples policy, applied with block extraction and with glob fragments separately classed per §5.6, predicts:

| class | occurrences (per-entry tokens) | distinct token strings | entries carrying ≥1 |
|---|---:|---:|---:|
| `direct` | 2556 | — (not required by §3) | 223 |
| `fallback` | 166 | 50 | 21 |
| `unresolved` | 7 | 6 | 4 |
| `ambiguous` | 0 | 0 | 0 |
| `glob-fragment` (quarantined, not an unresolved finding) | 1 | 1 | 1 |
| **all extracted tokens** | **2730** | **422 global-distinct** | **223** |

- Check: `2556 + 166 + 7 + 1 = 2730`.
- The one wrapped `- couples:` field, `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`, reads **4/4 named targets**: `sound-change.md` (unresolved), `tone-prosody.md` (unresolved), `sound-symbolism.md` (direct), `writing-systems.md` (direct). The single-line extractor reads **0/4** there, confirming Ca04 D1.
- Prototype validity: the same code reproduces the filed r39 eleven-entry baseline **exactly** — `refs=334 → direct=319 fallback=15 ambiguous=0 unresolved=0`, sacred-kingship `36 = 21 direct + 15 fallback`, **222 global-distinct** tokens (`reports/round-42/calib/basename-couples-policy-full.md:223-225`; `reports/round-37/adj/A06-verify.md:29`).

## 1. Method and assumptions (what a conformant tool must do to hit these numbers)

Policy object: `reports/round-42/calib/basename-couples-policy-full.md` §1 token extraction (`:14-25`), §2 two tiers/four classes (`:27-48`), §3 reporting (`:50-58`), §4 group alignment (`:60-69`), §5 limits incl. §5.1 slash gate (`:71-79`) and §5.6 glob fragments (`:97-101`), §6 recipe and filed run (`:104-217`, `:220-233`).

Token extraction used here:

1. Match each entry's `^- couples:` line and, when present, its indented continuation lines up to the next blank line or header field. Exactly one entry has continuations (`phonetics-phonology.md:72-77`); a corpus-wide scan found **no** continuation line that is unindented or otherwise unrecognised.
2. Reconstruct the field: join continuation lines with a single space, **except** when the preceding physical line ends in `-`, where the join is direct (no separator) so a hyphenated wrap heals. This is the load-bearing assumption for `tone-\n  prosody.md` → `tone-prosody.md`.
3. Extract every match of `[A-Za-z0-9_./{},\-]+\.md`, brace-expand one level (`{a,b}.md` → `a.md`, `b.md`), strip `:NN`/`:NN-NN` anchors implicitly (the anchor characters are outside the token class), deduplicate per entry.
4. Resolve Tier 1 against entry directory → lane root → `corpus/knowledge/<token>`; Tier 2 only for slash-free tokens, against the one-level index `corpus/knowledge/*/*.md`; one hit = `fallback` with mapping, ≥2 = `ambiguous`, zero = `unresolved`. A slash-bearing Tier-1 miss is `unresolved` and never falls back (§5.1).
5. Glob fragments (a token beginning `-` produced by `*`-glob syntax in the field) are quarantined as `glob-fragment`, never counted as unresolved and never fallback-resolved (§5.6).

Assumption A1 (wrapped-field join) is the one place a different implementation would move a **token name without moving the counts**: the C14-style newline join (`reports/round-35/cov/C14-audit-6-10.md:227-236`) yields `prosody.md` (mangled) instead of `tone-prosody.md`; both are unresolved, so totals stay the same but the claim's "4 named targets" fails. A pure `""` join also heals this field but risks fusing two adjacent tokens across a line boundary when a comma-separated list wraps; the hyphen rule avoids that. O01 must state which rule it implements; O04/O05 should test exactly this field.

Assumption A2: the glob fragment is separately classed. If the tool instead follows the r39 recipe literally (glob fragment as unresolved), the same tree yields **8 unresolved occurrences / 7 distinct** and no separate glob bucket. Either output is reconcilable; the policy's §5.6 wording prefers the separate class, which is what the headline table uses.

The exact prototype is reproduced below so the numbers survive scratch cleanup:

```python
import glob, os, re, collections
LANE=os.getcwd(); KNOW=os.path.join(LANE,'corpus','knowledge')
MDREF=re.compile(r"[A-Za-z0-9_./{},\-]+\.md")
BRACE=re.compile(r"\{([^{}]*)\}")
FIELD=re.compile(r"^- couples:")
HEADER=re.compile(r"^- (topic|sources|couples|source|verified-at|recheck|status|gap):")

def expand(s):
    m=BRACE.search(s)
    if not m: return [s]
    out=[]
    for part in m.group(1).split(','):
        out.extend(expand(s[:m.start()]+part+s[m.end():]))
    return out

def couples_field_block(text):
    lines=text.splitlines()
    for i,l in enumerate(lines):
        if FIELD.match(l):
            parts=[l.split(':',1)[1].strip()]; j=i+1
            while j<len(lines) and lines[j].strip() and lines[j][:1] in (' ','\t') \
                  and not HEADER.match(lines[j]):
                parts.append(lines[j].strip()); j+=1
            out=parts[0]
            for p in parts[1:]:
                out = out + p if out.endswith('-') else out + ' ' + p
            return out
    return None

IDX=collections.defaultdict(list)
for p in glob.glob(os.path.join(KNOW,'*','*.md')):
    IDX[os.path.basename(p)].append(os.path.relpath(p,LANE))

def classify(ref, entry_dir):
    for b in (entry_dir, LANE, KNOW):
        if os.path.isfile(os.path.normpath(os.path.join(b,ref))):
            return 'direct', None
    if '/' in ref:
        return 'unresolved', None
    hits=IDX.get(os.path.basename(ref),[])
    if len(hits)==1: return 'fallback', hits[0]
    if len(hits)>1: return 'ambiguous', sorted(hits)
    return 'unresolved', None

def refs_of(field):
    out=set()
    for raw in MDREF.findall(field):
        for c in expand(raw): out.add(c.strip())
    return out
```

## 2. Baseline reproduction (prototype validity)

Run against the same eleven entries the r39 policy §6 uses (`reports/round-42/calib/basename-couples-policy-full.md:152-163`):

| entry | refs |
|---|---:|
| `culture-material/agrarian-field-system-lexicon.md` | 22 |
| `culture-material/bathing-and-body-hygiene.md` | 25 |
| `culture-material/fire-fuel-light.md` | 44 |
| `culture-material/funerary-material-culture.md` | 48 |
| `culture-material/furniture-interior-lexicon.md` | 19 |
| `culture-material/writing-media-surface-economy.md` | 20 |
| `culture-material/timekeeping-instruments.md` | 25 |
| `myth-symbol/binding-speech-complex.md` | 40 |
| `myth-symbol/death-afterlife-eschatology.md` | 25 |
| `myth-symbol/eschatology-world-end-systems.md` | 30 |
| `myth-symbol/sacred-kingship-mythic-charter.md` | 36 |
| **totals** | **334** |

- Classes: `direct=319`, `fallback=15`, `ambiguous=0`, `unresolved=0` → **334 = 319 + 15**.
- Global-distinct across the eleven: **222**, matching `reports/round-37/adj/A06-verify.md:29` ("334 per-entry refs, 319 direct, 15 unique fallback, 0 ambiguous, 0 unresolved… a global union contains 222 distinct path strings").
- `sacred-kingship-mythic-charter.md` (`:37`): `36 = 21 direct + 15 fallback`; all 15 fallback targets are the mappings listed in §5 below (the r37 A12 set).
- Group alignment supplementary check: among the 28 couples fields that use a recognised `myth-symbol|linguistics|culture-material|civilizations|verification|synthesis —` label, 27 fallback tokens fall under a label and **0** are misaligned; the sacred-kingship 15 are among them. This is not a full §4 adjudication (O08 owns that), just a cross-check that no obvious alignment finding is hiding in the fallback class.

The exact match on all four baseline numbers is the reason to trust the live prediction below.

## 3. Live corpus prediction — totals and per-entry non-direct counts

Tree state: `git rev-parse --short HEAD` → `7ceff59`; `ls corpus/knowledge/*/*.md | wc -l` → `223`; partition vector `civilizations 94 / culture-material 25 / linguistics 25 / myth-symbol 26 / synthesis 29 / verification 24` (sum 223). All 223 entries have a `- couples:` field (zero missing).

Global counts: **2730 per-entry deduplicated tokens**, **422 global-distinct** strings. Four classes as in the headline; the glob fragment is held out of `unresolved`.

Per-entry rows with any non-direct token (26 entries; rows sum to `direct=2556, fallback=166, unresolved=7, ambiguous=0, glob=1` when the 197 all-direct entries are added):

| entry | refs | direct | fallback | unresolved | ambiguous | glob |
|---|---:|---:|---:|---:|---:|---:|
| `corpus/knowledge/civilizations/aegean-minoan-mycenaean.md` | 13 | 5 | 8 | 0 | 0 | 0 |
| `corpus/knowledge/civilizations/ancestral-puebloan.md` | 14 | 3 | 11 | 0 | 0 | 0 |
| `corpus/knowledge/civilizations/arabia-pre-islamic.md` | 11 | 3 | 8 | 0 | 0 | 0 |
| `corpus/knowledge/civilizations/australia-aboriginal.md` | 11 | 3 | 8 | 0 | 0 | 0 |
| `corpus/knowledge/civilizations/china-qing.md` | 15 | 3 | 12 | 0 | 0 | 0 |
| `corpus/knowledge/civilizations/japan-yayoi-kofun.md` | 13 | 3 | 10 | 0 | 0 | 0 |
| `corpus/knowledge/civilizations/java-majapahit.md` | 13 | 3 | 10 | 0 | 0 | 0 |
| `corpus/knowledge/civilizations/persia-sasanian.md` | 16 | 4 | 12 | 0 | 0 | 0 |
| `corpus/knowledge/culture-material/costume-semiotics.md` | 15 | 13 | 2 | 0 | 0 | 0 |
| `corpus/knowledge/culture-material/dress-through-eras.md` | 13 | 12 | 1 | 0 | 0 | 0 |
| `corpus/knowledge/culture-material/textile-technology.md` | 12 | 11 | 1 | 0 | 0 | 0 |
| `corpus/knowledge/linguistics/language-contact.md` | 5 | 2 | 0 | 3 | 0 | 0 |
| `corpus/knowledge/linguistics/numerals-and-measures.md` | 17 | 8 | 9 | 0 | 0 | 0 |
| `corpus/knowledge/linguistics/phonetics-phonology.md` | 4 | 2 | 0 | 2 | 0 | 0 |
| `corpus/knowledge/linguistics/sacred-registers-liturgical-language.md` | 12 | 9 | 3 | 0 | 0 | 0 |
| `corpus/knowledge/linguistics/sound-symbolism.md` | 17 | 11 | 6 | 0 | 0 | 0 |
| `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md` | 36 | 21 | 15 | 0 | 0 | 0 |
| `corpus/knowledge/synthesis/symbol-lexicon-colexification.md` | 12 | 4 | 8 | 0 | 0 | 0 |
| `corpus/knowledge/synthesis/symbolism-consistency-rules.md` | 13 | 3 | 10 | 0 | 0 | 0 |
| `corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md` | 13 | 4 | 9 | 0 | 0 | 0 |
| `corpus/knowledge/synthesis/typed-label-routing-workflow.md` | 13 | 12 | 0 | 1 | 0 | 0 |
| `corpus/knowledge/verification/citation-format-and-source-registry.md` | 9 | 3 | 6 | 0 | 0 | 0 |
| `corpus/knowledge/verification/gate-frozen-run-standard.md` | 5 | 4 | 0 | 0 | 0 | 1 |
| `corpus/knowledge/verification/label-channel-routing-verification.md` | 12 | 11 | 0 | 1 | 0 | 0 |
| `corpus/knowledge/verification/naming-collision-gate.md` | 12 | 3 | 9 | 0 | 0 | 0 |
| `corpus/knowledge/verification/phonology-sanity-gate.md` | 11 | 3 | 8 | 0 | 0 | 0 |

## 4. Delta bridge from the filed r39 counts

The r39 recipe parsed only the first physical line of a `couples:` field; the successor policy parses the whole block. That is the only definitional change between the two lower rows:

| measurement | entries | refs | direct | fallback | ambiguous | unresolved | glob |
|---|---:|---:|---:|---:|---:|---:|---:|
| r39 filed, §6 Part 2 (`basename-couples-policy-full.md:228-233`) | 212 | 2504 | 2335 | 163 | 0 | 6 (incl. 1 glob; 5 distinct) | — |
| current tree, r39 single-line recipe (reproduced this seat) | 223 | 2726 | 2554 | 166 | 0 | 6 (incl. 1 glob; 5 distinct) | — |
| current tree, block extraction + §5.6 quarantine (**prediction**) | 223 | 2730 | 2556 | 166 | 0 | 7 (6 distinct) | 1 |

Decomposition of the differences:

- **11 entries added since the r39 baseline `dfb0719`** contribute **+222 refs**: 219 direct + 3 fallback. The files (verified by `comm -13 <(git ls-tree -r --name-only dfb0719 -- corpus/knowledge | sort) <(find corpus/knowledge -name '*.md' | sort)`) and their contributions:

| new entry | refs | classes |
|---|---:|---|
| `linguistics/dialect-register-consistency.md` | 10 | 10 direct |
| `linguistics/sacred-registers-liturgical-language.md` | 12 | 9 direct + 3 fallback |
| `linguistics/taboo-strata-lifecycle.md` | 10 | 10 direct |
| `linguistics/translation-protocol-fidelity.md` | 11 | 11 direct |
| `myth-symbol/mineral-stone-symbolism.md` | 44 | 44 direct |
| `myth-symbol/purity-pollution-boundary-systems.md` | 36 | 36 direct |
| `myth-symbol/sacred-topography-pilgrimage.md` | 39 | 39 direct |
| `verification/append-only-record-verification.md` | 16 | 16 direct |
| `verification/contact-strata-verification-gate.md` | 12 | 12 direct |
| `verification/index-sweep-verification.md` | 12 | 12 direct |
| `verification/worked-example-verification.md` | 20 | 20 direct |
| **sum** | **222** | **219 direct + 3 fallback** |

- **Block extraction** on the one wrapped field adds **+4 tokens**: `sound-symbolism.md` and `writing-systems.md` are direct (both exist in `corpus/knowledge/linguistics/`), `sound-change.md` and `tone-prosody.md` are unresolved (neither is written). This closes Ca04 D1's live instance (`reports/round-39/calib/Ca04-verify.md:78-93`): the old extractor read 0/4; the block extractor reads 4/4.
- Arithmetic: `2504 + 222 + 4 = 2730`; `2335 + 219 + 2 = 2556`; `163 + 3 = 166`; `6 + 2 = 8 = 7 unresolved + 1 glob`.
- The r39 Part 2 unresolved set had 5 distinct names: the glob fragment `-gate.md`, the X26 phantom `../linguistics/phonology-sanity.md` (x2), and the three `language-contact.md:7` seeds. The prediction keeps all five and adds the two phonetics phantoms.

## 5. Every expected fallback mapping (166 occurrences, 50 distinct tokens, 50 distinct targets)

No fallback target leaves `corpus/knowledge/`; the target-partition distribution is `linguistics 67 / culture-material 53 / myth-symbol 30 / synthesis 8 / verification 5 / civilizations 3`. These are `fallback` only under §2 Tier 2 and must never be merged into the direct count (§3.2).

### `civilizations/aegean-minoan-mycenaean.md` (8)
- `architecture-settlement-lexicon.md` → `corpus/knowledge/culture-material/architecture-settlement-lexicon.md`
- `costume-semiotics.md` → `corpus/knowledge/culture-material/costume-semiotics.md`
- `historical-linguistics.md` → `corpus/knowledge/linguistics/historical-linguistics.md`
- `language-contact.md` → `corpus/knowledge/linguistics/language-contact.md`
- `material-culture-inference-method.md` → `corpus/knowledge/culture-material/material-culture-inference-method.md`
- `myth-ritual-theories.md` → `corpus/knowledge/myth-symbol/myth-ritual-theories.md`
- `naming-systems.md` → `corpus/knowledge/linguistics/naming-systems.md`
- `symbolism-synthesis-method.md` → `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md`

### `civilizations/ancestral-puebloan.md` (11)
- `architecture-settlement-lexicon.md` → `corpus/knowledge/culture-material/architecture-settlement-lexicon.md`
- `color-symbolism.md` → `corpus/knowledge/myth-symbol/color-symbolism.md`
- `cosmology-cosmography.md` → `corpus/knowledge/myth-symbol/cosmology-cosmography.md`
- `language-contact.md` → `corpus/knowledge/linguistics/language-contact.md`
- `material-culture-inference-method.md` → `corpus/knowledge/culture-material/material-culture-inference-method.md`
- `naming-systems.md` → `corpus/knowledge/linguistics/naming-systems.md`
- `ritual-garments.md` → `corpus/knowledge/culture-material/ritual-garments.md`
- `sociolinguistics-registers.md` → `corpus/knowledge/linguistics/sociolinguistics-registers.md`
- `symbolism-synthesis-method.md` → `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md`
- `textile-technology.md` → `corpus/knowledge/culture-material/textile-technology.md`
- `writing-systems.md` → `corpus/knowledge/linguistics/writing-systems.md`

### `civilizations/arabia-pre-islamic.md` (8)
- `costume-semiotics.md` → `corpus/knowledge/culture-material/costume-semiotics.md`
- `material-culture-inference-method.md` → `corpus/knowledge/culture-material/material-culture-inference-method.md`
- `naming-systems.md` → `corpus/knowledge/linguistics/naming-systems.md`
- `orality-formulaic-language.md` → `corpus/knowledge/linguistics/orality-formulaic-language.md`
- `pantheon-archetypes.md` → `corpus/knowledge/myth-symbol/pantheon-archetypes.md`
- `symbolism-synthesis-method.md` → `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md`
- `trade-economy-lexicon.md` → `corpus/knowledge/culture-material/trade-economy-lexicon.md`
- `writing-systems.md` → `corpus/knowledge/linguistics/writing-systems.md`

### `civilizations/australia-aboriginal.md` (8)
- `adornment-body-codes.md` → `corpus/knowledge/culture-material/adornment-body-codes.md`
- `material-culture-inference-method.md` → `corpus/knowledge/culture-material/material-culture-inference-method.md`
- `naming-systems.md` → `corpus/knowledge/linguistics/naming-systems.md`
- `politeness-taboo-euphemism.md` → `corpus/knowledge/linguistics/politeness-taboo-euphemism.md`
- `ritual-garments.md` → `corpus/knowledge/culture-material/ritual-garments.md`
- `sociolinguistics-registers.md` → `corpus/knowledge/linguistics/sociolinguistics-registers.md`
- `symbolism-synthesis-method.md` → `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md`
- `writing-systems.md` → `corpus/knowledge/linguistics/writing-systems.md`

### `civilizations/china-qing.md` (12)
- `animal-symbolism.md` → `corpus/knowledge/myth-symbol/animal-symbolism.md`
- `color-symbolism.md` → `corpus/knowledge/myth-symbol/color-symbolism.md`
- `cosmology-cosmography.md` → `corpus/knowledge/myth-symbol/cosmology-cosmography.md`
- `dress-through-eras.md` → `corpus/knowledge/culture-material/dress-through-eras.md`
- `era-periodization-models.md` → `corpus/knowledge/culture-material/era-periodization-models.md`
- `historical-linguistics.md` → `corpus/knowledge/linguistics/historical-linguistics.md`
- `material-culture-inference-method.md` → `corpus/knowledge/culture-material/material-culture-inference-method.md`
- `naming-systems.md` → `corpus/knowledge/linguistics/naming-systems.md`
- `sociolinguistics-registers.md` → `corpus/knowledge/linguistics/sociolinguistics-registers.md`
- `sumptuary-law-rank-display.md` → `corpus/knowledge/culture-material/sumptuary-law-rank-display.md`
- `symbolism-synthesis-method.md` → `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md`
- `writing-systems.md` → `corpus/knowledge/linguistics/writing-systems.md`

### `civilizations/japan-yayoi-kofun.md` (10)
- `adornment-body-codes.md` → `corpus/knowledge/culture-material/adornment-body-codes.md`
- `comparative-frameworks.md` → `corpus/knowledge/myth-symbol/comparative-frameworks.md`
- `costume-semiotics.md` → `corpus/knowledge/culture-material/costume-semiotics.md`
- `dress-through-eras.md` → `corpus/knowledge/culture-material/dress-through-eras.md`
- `language-contact.md` → `corpus/knowledge/linguistics/language-contact.md`
- `material-culture-inference-method.md` → `corpus/knowledge/culture-material/material-culture-inference-method.md`
- `naming-systems.md` → `corpus/knowledge/linguistics/naming-systems.md`
- `ritual-liminality.md` → `corpus/knowledge/myth-symbol/ritual-liminality.md`
- `symbolism-synthesis-method.md` → `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md`
- `writing-systems.md` → `corpus/knowledge/linguistics/writing-systems.md`

### `civilizations/java-majapahit.md` (10)
- `architecture-settlement-lexicon.md` → `corpus/knowledge/culture-material/architecture-settlement-lexicon.md`
- `costume-semiotics.md` → `corpus/knowledge/culture-material/costume-semiotics.md`
- `naming-systems.md` → `corpus/knowledge/linguistics/naming-systems.md`
- `orality-formulaic-language.md` → `corpus/knowledge/linguistics/orality-formulaic-language.md`
- `pantheon-archetypes.md` → `corpus/knowledge/myth-symbol/pantheon-archetypes.md`
- `sociolinguistics-registers.md` → `corpus/knowledge/linguistics/sociolinguistics-registers.md`
- `symbolism-synthesis-method.md` → `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md`
- `textile-technology.md` → `corpus/knowledge/culture-material/textile-technology.md`
- `warrior-material-culture.md` → `corpus/knowledge/culture-material/warrior-material-culture.md`
- `writing-systems.md` → `corpus/knowledge/linguistics/writing-systems.md`

### `civilizations/persia-sasanian.md` (12)
- `costume-semiotics.md` → `corpus/knowledge/culture-material/costume-semiotics.md`
- `creation-myths-taxonomy.md` → `corpus/knowledge/myth-symbol/creation-myths-taxonomy.md`
- `dress-through-eras.md` → `corpus/knowledge/culture-material/dress-through-eras.md`
- `language-contact.md` → `corpus/knowledge/linguistics/language-contact.md`
- `material-culture-inference-method.md` → `corpus/knowledge/culture-material/material-culture-inference-method.md`
- `naming-systems.md` → `corpus/knowledge/linguistics/naming-systems.md`
- `orality-formulaic-language.md` → `corpus/knowledge/linguistics/orality-formulaic-language.md`
- `pantheon-archetypes.md` → `corpus/knowledge/myth-symbol/pantheon-archetypes.md`
- `ritual-garments.md` → `corpus/knowledge/culture-material/ritual-garments.md`
- `symbolism-synthesis-method.md` → `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md`
- `textile-technology.md` → `corpus/knowledge/culture-material/textile-technology.md`
- `writing-systems.md` → `corpus/knowledge/linguistics/writing-systems.md`

### `culture-material/costume-semiotics.md` (2)
- `language-contact.md` → `corpus/knowledge/linguistics/language-contact.md`
- `semantics-pragmatics.md` → `corpus/knowledge/linguistics/semantics-pragmatics.md`

### `culture-material/dress-through-eras.md` (1)
- `historical-linguistics.md` → `corpus/knowledge/linguistics/historical-linguistics.md`

### `culture-material/textile-technology.md` (1)
- `language-contact.md` → `corpus/knowledge/linguistics/language-contact.md`

### `linguistics/numerals-and-measures.md` (9)
- `calendar-festival-systems.md` → `corpus/knowledge/culture-material/calendar-festival-systems.md`
- `coupling-model.md` → `corpus/knowledge/synthesis/coupling-model.md`
- `inca.md` → `corpus/knowledge/civilizations/inca.md`
- `lexicon-coverage-audit.md` → `corpus/knowledge/verification/lexicon-coverage-audit.md`
- `loanword-material-dating.md` → `corpus/knowledge/synthesis/loanword-material-dating.md`
- `maya-classic.md` → `corpus/knowledge/civilizations/maya-classic.md`
- `mesopotamia-sumer-akkad.md` → `corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md`
- `number-symbolism.md` → `corpus/knowledge/myth-symbol/number-symbolism.md`
- `trade-economy-lexicon.md` → `corpus/knowledge/culture-material/trade-economy-lexicon.md`

### `linguistics/sacred-registers-liturgical-language.md` (3)
- `era-language-staging.md` → `corpus/knowledge/synthesis/era-language-staging.md`
- `real-world-inspiration-boundaries.md` → `corpus/knowledge/verification/real-world-inspiration-boundaries.md`
- `religion-language-co-evolution.md` → `corpus/knowledge/synthesis/religion-language-co-evolution.md`

### `linguistics/sound-symbolism.md` (6)
- `calibration-registry.md` → `corpus/knowledge/verification/calibration-registry.md`
- `music-instrument-lexicon.md` → `corpus/knowledge/culture-material/music-instrument-lexicon.md`
- `myth-to-language-derivation.md` → `corpus/knowledge/synthesis/myth-to-language-derivation.md`
- `real-world-inspiration-boundaries.md` → `corpus/knowledge/verification/real-world-inspiration-boundaries.md`
- `source-discipline-calibration.md` → `corpus/knowledge/synthesis/source-discipline-calibration.md`
- `taboo-euphemism-lifecycle.md` → `corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md`

### `myth-symbol/sacred-kingship-mythic-charter.md` (15 — the r37 A12 set)
- `architecture-settlement-lexicon.md` → `corpus/knowledge/culture-material/architecture-settlement-lexicon.md`
- `calendar-festival-systems.md` → `corpus/knowledge/culture-material/calendar-festival-systems.md`
- `calibration-registry.md` → `corpus/knowledge/verification/calibration-registry.md`
- `consistency-verification-checklist.md` → `corpus/knowledge/synthesis/consistency-verification-checklist.md`
- `costume-semiotics.md` → `corpus/knowledge/culture-material/costume-semiotics.md`
- `historical-linguistics.md` → `corpus/knowledge/linguistics/historical-linguistics.md`
- `kinship-terminology.md` → `corpus/knowledge/linguistics/kinship-terminology.md`
- `naming-systems.md` → `corpus/knowledge/linguistics/naming-systems.md`
- `orality-formulaic-language.md` → `corpus/knowledge/linguistics/orality-formulaic-language.md`
- `register-strata-attestation.md` → `corpus/knowledge/linguistics/register-strata-attestation.md`
- `ritual-garments.md` → `corpus/knowledge/culture-material/ritual-garments.md`
- `semantics-pragmatics.md` → `corpus/knowledge/linguistics/semantics-pragmatics.md`
- `sociolinguistics-registers.md` → `corpus/knowledge/linguistics/sociolinguistics-registers.md`
- `sumptuary-law-rank-display.md` → `corpus/knowledge/culture-material/sumptuary-law-rank-display.md`
- `trade-economy-lexicon.md` → `corpus/knowledge/culture-material/trade-economy-lexicon.md`

### `synthesis/symbol-lexicon-colexification.md` (8)
- `comparative-frameworks.md` → `corpus/knowledge/myth-symbol/comparative-frameworks.md`
- `garment-lexicon-crosslinguistic.md` → `corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md`
- `historical-linguistics.md` → `corpus/knowledge/linguistics/historical-linguistics.md`
- `language-contact.md` → `corpus/knowledge/linguistics/language-contact.md`
- `material-culture-inference-method.md` → `corpus/knowledge/culture-material/material-culture-inference-method.md`
- `naming-systems.md` → `corpus/knowledge/linguistics/naming-systems.md`
- `semantics-pragmatics.md` → `corpus/knowledge/linguistics/semantics-pragmatics.md`
- `writing-systems.md` → `corpus/knowledge/linguistics/writing-systems.md`

### `synthesis/symbolism-consistency-rules.md` (10)
- `color-symbolism.md` → `corpus/knowledge/myth-symbol/color-symbolism.md`
- `comparative-frameworks.md` → `corpus/knowledge/myth-symbol/comparative-frameworks.md`
- `costume-semiotics.md` → `corpus/knowledge/culture-material/costume-semiotics.md`
- `historical-linguistics.md` → `corpus/knowledge/linguistics/historical-linguistics.md`
- `language-contact.md` → `corpus/knowledge/linguistics/language-contact.md`
- `naming-systems.md` → `corpus/knowledge/linguistics/naming-systems.md`
- `ritual-liminality.md` → `corpus/knowledge/myth-symbol/ritual-liminality.md`
- `sumptuary-law-rank-display.md` → `corpus/knowledge/culture-material/sumptuary-law-rank-display.md`
- `textile-technology.md` → `corpus/knowledge/culture-material/textile-technology.md`
- `writing-systems.md` → `corpus/knowledge/linguistics/writing-systems.md`

### `synthesis/taboo-euphemism-lifecycle.md` (9)
- `dress-through-eras.md` → `corpus/knowledge/culture-material/dress-through-eras.md`
- `historical-linguistics.md` → `corpus/knowledge/linguistics/historical-linguistics.md`
- `material-culture-inference-method.md` → `corpus/knowledge/culture-material/material-culture-inference-method.md`
- `naming-systems.md` → `corpus/knowledge/linguistics/naming-systems.md`
- `pantheon-archetypes.md` → `corpus/knowledge/myth-symbol/pantheon-archetypes.md`
- `ritual-garments.md` → `corpus/knowledge/culture-material/ritual-garments.md`
- `sociolinguistics-registers.md` → `corpus/knowledge/linguistics/sociolinguistics-registers.md`
- `symbolism-synthesis-method.md` → `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md`
- `writing-systems.md` → `corpus/knowledge/linguistics/writing-systems.md`

### `verification/citation-format-and-source-registry.md` (6)
- `comparative-frameworks.md` → `corpus/knowledge/myth-symbol/comparative-frameworks.md`
- `dress-through-eras.md` → `corpus/knowledge/culture-material/dress-through-eras.md`
- `material-culture-inference-method.md` → `corpus/knowledge/culture-material/material-culture-inference-method.md`
- `naming-systems.md` → `corpus/knowledge/linguistics/naming-systems.md`
- `symbolism-synthesis-method.md` → `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md`
- `writing-systems.md` → `corpus/knowledge/linguistics/writing-systems.md`

### `verification/naming-collision-gate.md` (9)
- `costume-semiotics.md` → `corpus/knowledge/culture-material/costume-semiotics.md`
- `garment-lexicon-crosslinguistic.md` → `corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md`
- `historical-linguistics.md` → `corpus/knowledge/linguistics/historical-linguistics.md`
- `language-contact.md` → `corpus/knowledge/linguistics/language-contact.md`
- `morphological-typology.md` → `corpus/knowledge/linguistics/morphological-typology.md`
- `pantheon-archetypes.md` → `corpus/knowledge/myth-symbol/pantheon-archetypes.md`
- `phonetics-phonology.md` → `corpus/knowledge/linguistics/phonetics-phonology.md`
- `politeness-taboo-euphemism.md` → `corpus/knowledge/linguistics/politeness-taboo-euphemism.md`
- `writing-systems.md` → `corpus/knowledge/linguistics/writing-systems.md`

### `verification/phonology-sanity-gate.md` (8)
- `garment-lexicon-crosslinguistic.md` → `corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md`
- `historical-linguistics.md` → `corpus/knowledge/linguistics/historical-linguistics.md`
- `language-contact.md` → `corpus/knowledge/linguistics/language-contact.md`
- `morphological-typology.md` → `corpus/knowledge/linguistics/morphological-typology.md`
- `naming-systems.md` → `corpus/knowledge/linguistics/naming-systems.md`
- `ritual-garments.md` → `corpus/knowledge/culture-material/ritual-garments.md`
- `sociolinguistics-registers.md` → `corpus/knowledge/linguistics/sociolinguistics-registers.md`
- `writing-systems.md` → `corpus/knowledge/linguistics/writing-systems.md`

Count check: `8+11+8+8+12+10+10+12+2+1+1+9+3+6+15+8+10+9+6+9+8 = 166`.

## 6. Every expected unresolved / ambiguous token, and the glob fragment

`ambiguous = 0`. Evidence: the one-level index contains **223 basenames with zero duplicate basenames** (`python3` probe over `corpus/knowledge/*/*.md`: `INDEX basename duplicates: {}`), so no bare token can hit two files at this tree. Any future `ambiguous` row requires a duplicate basename; none exists today. (A landing that reused an existing basename in a second partition would create one — see §8.)

`unresolved` — 6 distinct tokens, 7 occurrences:

| token | occurrences | entry:line | named reason |
|---|---:|---|---|
| `../linguistics/phonology-sanity.md` | 2 | `corpus/knowledge/verification/label-channel-routing-verification.md:14`; `corpus/knowledge/synthesis/typed-label-routing-workflow.md:16` | slash-bearing, so §5.1 forbids fallback; target `corpus/knowledge/linguistics/phonology-sanity.md` does not exist. This is the r19 X26-1 phantom (`reports/round-19/audit/x26-spotcheck-entries.md`; `reports/round-35/cov/C14-audit-6-10.md:114-119`), still live. |
| `honorifics-and-register.md` | 1 | `corpus/knowledge/linguistics/language-contact.md:7` | bare basename; zero index hits. Named in the field as a "sibling knowledge file to seed"; never written. |
| `naming-and-onomastics.md` | 1 | `corpus/knowledge/linguistics/language-contact.md:7` | same seed list; zero index hits; never written. |
| `phonology-basics.md` | 1 | `corpus/knowledge/linguistics/language-contact.md:7` | same seed list; zero index hits; never written. |
| `sound-change.md` | 1 | `corpus/knowledge/linguistics/phonetics-phonology.md:72-77` (wrapped field, line 76) | bare basename; zero index hits. Named as a "prospective sibling file"; never written. Newly visible only under block extraction. |
| `tone-prosody.md` | 1 | `corpus/knowledge/linguistics/phonetics-phonology.md:72-77` (lines 76-77, hyphen-wrapped) | bare basename; zero index hits. Named as a prospective sibling; the hyphenated line break is the field's only wrap. Newly visible only under block extraction with the hyphen join. |

The other two seeds in `language-contact.md:7` resolve and are therefore not rows here: `writing-systems.md` and `numerals-and-measures.md` are direct (both exist in the entry's own partition).

`glob-fragment` — 1 occurrence:

| token | entry:line | source syntax | disposition |
|---|---|---|---|
| `-gate.md` | `corpus/knowledge/verification/gate-frozen-run-standard.md:15` | `corpus/knowledge/verification/*-gate.md` | quarantined per §5.6; not an unresolved couples finding and never fallback-resolved. If the tool counts it as unresolved instead, the row set becomes 7 distinct / 8 occurrences. |

## 7. Wrapped-field evidence (the D1 positive control)

Field bytes, `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`:

```text
72 - couples: language (this file, core method); myth (divine/true names, taboo
73   naming, onomatopoeic etiologies); symbol (sound symbolism, name-shape,
74   bouba/kiki iconography); era (Neolithic bite → f/v, sound-change dating of
75   strata); costume (masks/mouthgear vs articulation, whistle & drum channels);
76   environment/anatomy design; prospective sibling files: sound-change.md, tone-
77   prosody.md, sound-symbolism.md, writing-systems.md
```

- Single-line capture (`re.search(r"^- couples:\s*(.*)$", …, re.M)` as at `reports/round-19/audit/entry-audit.py:75`): **0 tokens** — line 72 contains no `.md`.
- Block extraction with the hyphen rule: **4 tokens**, all four named targets in the claim: `sound-change.md` (unresolved), `tone-prosody.md` (unresolved), `sound-symbolism.md` (direct, `corpus/knowledge/linguistics/sound-symbolism.md`), `writing-systems.md` (direct, `corpus/knowledge/linguistics/writing-systems.md`).
- C14-style newline join (`reports/round-35/cov/C14-audit-6-10.md:227-236`) gives `sound-change.md`, `prosody.md`, `sound-symbolism.md`, `writing-systems.md`: still 4 tokens, but `prosody.md` is an extractor artifact, not a named target. This is why the hyphen join is the required reading of "reads the wrapped field whole"; Ca04 already flagged the mangling as a hazard no current instrument handles (`reports/round-39/calib/Ca04-verify.md:78-93`).
- The next line after the field is blank and then `## 1. Two levels: phonetics vs phonology`; a block extractor must stop at the blank line, not swallow the heading. No other entry has continuation lines (corpus-wide scan: exactly one multi-line couples field).

## 8. Post-C-landing projection (conditional) and the collision it exposes

The C claim lands the r42 C01 spare, moving myth-symbol `26 -> 27` and total `223 -> 224` (`reports/round-43/claims.json` claim C). Resolver-side effect of the spare's own `- couples:` field (`reports/round-42/cov/C01-mineral-spare.md:22`): **30 per-entry tokens, all `direct`** when classified as a myth-symbol entry (its tokens are full `corpus/knowledge/...` paths and partition-prefixed paths such as `myth-symbol/symbolism-synthesis-method.md`, all resolving through the `corpus/knowledge/<token>` Tier-1 base). Projected post-landing totals, **if and only if** the landing uses a new, non-duplicate basename:

| measurement | prediction |
|---|---|
| entries | 224 |
| refs | 2760 |
| direct | 2586 |
| fallback | 166 |
| unresolved | 7 (6 distinct) |
| ambiguous | 0 |
| glob | 1 |

Partition vector after landing: `linguistics 25 / myth-symbol 27 / culture-material 25 / synthesis 29 / verification 24 / civilizations 94` = 224.

**Collision flag (reported, not routed).** The live partition already contains `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` (26 files today; one of the 11 post-r39 additions). Its `#` title, `Stone, gem and metal symbolism — the lithic register: the lapidary code, material prestige, and the quarry-to-regalia chain`, matches C04's fenced entry at `reports/round-42/cov/C04-entry-4.md:54`, so the r42 C04 landing is live. The round-43 C01 spare's title, `Stone, gem, and metal — the lithic register: material properties as symbol, the scarcity ladder, and the lapidary as an institution` (`reports/round-42/cov/C01-mineral-spare.md:4`), covers the same lithic topic; its own header records that C01 and C04 authored the same topic and that C04 landed (`reports/round-42/cov/C01-mineral-spare.md:1`). Therefore:

- the C claim's premise "myth-symbol's named lapidary slot … named but unbuilt since r42" is **not true at the live 223 tree** — the slot is occupied by C04's bytes;
- the natural target basename `mineral-stone-symbolism.md` is **not free**; overwriting is forbidden by the shared rules, and a second file with the same basename in the same partition is impossible;
- any landing under a new filename adds a second lithic entry on the same topic, which is a coverage/duplication decision for K02/P01/the integrator, not a resolver decision. I am reporting the collision and not proposing a path.
- If a landing ever reuses an existing basename in another partition, the index would gain a duplicate basename and bare tokens with that basename would flip `fallback -> ambiguous`; that is not the current proposal, but it is the one census-visible way the C landing could add an ambiguous class instead of only direct tokens.

## 9. Traps the durable tool must get right (prediction-sensitive checks)

- **Anchors**: 19 raw anchor-bearing matches exist in couples fields (e.g. `calibration-registry.md:91` in `sacred-kingship-mythic-charter.md:37`; `civilizations/maori.md:13-14`). The `:NN`/`:NN-NN` suffix must not enter the token. The policy's character class already excludes `:`; a tool that pre-splits on `:` incorrectly would drop or mangle the token.
- **Brace expansion**: 218 literal `{…}.md` groups across the corpus (e.g. `corpus/knowledge/civilizations/akan.md` groups of 4-7 names). One-level expansion, then per-entry dedup, is required to hit the counts; no nested braces were found.
- **`./` prefixes**: 19 tokens use `./name.md` (`binding-speech-complex.md`, `divination-omen-systems.md`); these are `direct` through the entry-directory base. Do not normalise them away or treat the leading dot as an extension.
- **Field termination**: stop the block at the first blank line; the phonetics field is followed by a blank line then a `##` heading. Do not absorb the heading.
- **Hyphen wrap**: the hyphen rule in §1 is required for the "4 named targets" threshold; a space or newline join produces `prosody.md`.
- **Glob fragments**: `-gate.md` is the only one today; §5.6 forbids counting it as unresolved or resolving it via fallback.
- **Slash gate**: a slash-bearing Tier-1 miss is unresolved even when the basename is unique elsewhere (§5.1). The r39 demonstration token `linguistics/hero-journey-variants.md` is synthetic, not a live couples token in this tree; do not let a future selftest expect it to resolve.
- **Counts to compare against**: `2730` total, `2556/166/0/7` + glob `1`; if the tool prints `2504` or a single-line count, it is using the r39 extractor, not the successor policy. If it prints `2554/166/6`, it is single-line on the current tree (the bridge row in §4), not a bug in the corpus.

## 10. Reproduction commands and outputs (this seat, 2026-10-19, lane root)

All runs used `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, were read-only over the corpus, and executed no `run-validation.py`.

```text
$ git rev-parse --short HEAD
7ceff59

$ ls corpus/knowledge/*/*.md | wc -l
223

$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do \
    echo "$p $(ls corpus/knowledge/$p/*.md | wc -l)"; done
civilizations 94
culture-material 25
linguistics 25
myth-symbol 26
synthesis 29
verification 24

$ python3 -B .scratch/o03/predict.py | head -2
ENTRIES 223
TOTALS {'direct': 2556, 'fallback': 166, 'unresolved': 7, 'glob-fragment': 1} sum 2730

$ python3 -B .scratch/o03/predict.py | grep -E '^(UNRESOLVED|AMBIGUOUS|GLOBFRAGS|GLOBAL DISTINCT|INDEX basename)'
UNRESOLVED 6                      # distinct tokens; 7 occurrences
AMBIGUOUS 0
GLOBFRAGS [('corpus/knowledge/verification/gate-frozen-run-standard.md', '-gate.md')]
GLOBAL DISTINCT 422
INDEX basename duplicates: {}

$ python3 -B .scratch/o03/predict.py | grep -c '  FB '
166
```

Baseline reproduction (same script's `classify`/`refs_of`, applied to the eleven r39 entries): `TOTALS {'direct': 319, 'fallback': 15} sum 334 global distinct 222`; `sacred-kingship refs=36`.

Single-line bridge run (same tree, r39 extractor): `SINGLE-LINE current: {'direct': 2554, 'fallback': 166, 'unresolved': 6} sum 2726 unresolved distinct 5`.

New-file attribution: `comm -13 <(git ls-tree -r --name-only dfb0719 -- corpus/knowledge | sort) <(find corpus/knowledge -name '*.md' | sort)` returned exactly the 11 files in §4; their resolver contribution measured `NEW TOTALS {'direct': 219, 'fallback': 3} sum 222`.

## 11. Caveats / to-verify

- This is a **prediction**, not the filed census. The claim's after_required artifact is the durable tool's `--census` output under `reports/round-43/calib/`; O01/O06 own its filename and format. The numbers above are the comparison target; any divergence should be explained by the §1 assumptions, not smoothed over.
- `direct` distinct-token count and per-entry direct counts beyond the 26 non-direct rows are not itemised here; the totals are exact, and O06's disposition leg only requires fallback/unresolved/ambiguous rows.
- §4 group alignment is only spot-checked here (27 fallback tokens under recognised labels, 0 misaligned). Full §4 conformance is O08's seat.
- The post-C projection is conditional on a new basename and on the spare's 30-token couples field landing unmodified. The collision in §8 is a report, not a resolution; K02/P01 must decide the path.
- `to-verify`: the two phonetics phantoms `sound-change.md`/`tone-prosody.md` are named as prospective siblings, not promised files; whether they should be written or the field amended is a corpus decision, not this seat's. Likewise the three `language-contact.md:7` seeds and the X26 phantom remain corpus findings.
- No filed byte was edited; the scratch script is disposable and its logic is reproduced in §1 so this evidence survives cleanup.

## Citations

- Claim/contract: `reports/round-43/claims.json:24-37` (claim O), `reports/round-43/targets.json` seat O03.
- Policy: `reports/round-42/calib/basename-couples-policy-full.md:14-25` (§1), `:27-48` (§2), `:50-58` (§3), `:60-69` (§4), `:71-101` (§5 incl. §5.1 `:76-79` and §5.6 `:97-101`), `:110-217` (§6 recipe), `:220-233` (filed run: `334=319+15`; `212/2504 -> 2335/163/0/6`).
- Prior instruments: `reports/round-19/audit/entry-audit.py:31,34-42,74-96`; `reports/round-35/cov/C14-audit-6-10.md:227-236,249-288`; `reports/round-27/audit/entry-audit.py:129-131`.
- Prior findings: `reports/round-39/calib/Ca04-verify.md:78-93` (D1 wrapped field), `:94-99` (D2 disposition leg); `reports/round-37/adj/A06-verify.md:29` (222 global distinct); `reports/round-37/adj/A12-gap-fill.md:9-26` (15 fallback mappings); `reports/round-35/cov/C12-audit-runbook.md:37` (unresolved disposition); `reports/round-37/op/defect-queue.json:202-211`.
- Live evidence: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`; `corpus/knowledge/linguistics/language-contact.md:7`; `corpus/knowledge/verification/gate-frozen-run-standard.md:15`; `corpus/knowledge/verification/label-channel-routing-verification.md:14`; `corpus/knowledge/synthesis/typed-label-routing-workflow.md:16`; `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:37`.
- C-claim interaction: `reports/round-42/cov/C01-mineral-spare.md:1,3,22` (ruling, title, 30-token couples field); `reports/round-42/cov/C04-entry-4.md:54`; live `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:1`; `reports/round-42/cov/C06-delta-receipt.md` (C01/C04 same-topic collision D4).
- Command outputs: §10 above; scratch digest `sha256sum .scratch/o03/predict.py` → `7a3be4f9032aa24fae28fc449e3918523cc687ce9f90cc144964e116e0b5bf29`.
