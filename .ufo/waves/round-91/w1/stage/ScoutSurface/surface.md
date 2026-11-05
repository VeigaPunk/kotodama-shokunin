# ScoutSurface — round 91 coverage surface (secret, ludic, anti-language registers)

Seat: ScoutSurface (read-only scout). Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin.
Date of measurement: 2026-11-05.
No URL was fetched by this seat. All bytes read from the local repository (committed base tree and
the working tree). No file outside this stage dir and the seat's Report trailer was written.

## 0. Which bytes were used

| what | which bytes | how obtained |
|---|---|---|
| base coverage (the frozen comparison point) | committed tree at base `d39434b3bc8458e1b66edd2d0d0fea9ea32f3331` | `git archive d39434b3 corpus \| tar -x -C <scratch>/base-tree` (rc 0) |
| working-tree coverage (the pending landing) | working tree at `691aebf247ebea4dd50577bb64ac99d12fa1145a` + untracked/modified lane files | `git ls-files`/`find` + `grep` on the working tree |

Base tree and working tree differ in `corpus/knowledge` only by the new untracked entry
`corpus/knowledge/linguistics/secret-and-ludic-languages.md` (git status: `??`). `git diff
d39434b3 -- corpus/knowledge` is empty (rc 0) and `git diff d39434b3 691aebf -- corpus/knowledge`
is empty (rc 0). `corpus/SOURCES.md` is modified in the worktree (+6 rows: S952–S956) and
`corpus/README.md` is modified (linguistics partition 35 → 36).

Both readings are reported below so the L1 can see the gap at base and the surface after landing.

## 1. Files under corpus/knowledge whose headings or topic line name a register term

Term set (from the seat brief): argot, cant, anti-language, ludling, Pig Latin, verlan, backslang,
Polari, rhyming slang, secret language, jargon, slang, reversal. Matched case-insensitively with
non-alphabetic boundaries so that *polarity*, *overland*, *significant*, *supplicant*, *dedicant*
are not counted as *polari*, *verlan* or *cant*.

### 1a. Base tree `d39434b3` — 12 matching lines in 7 files

Verbatim heading / topic line, with its line number:

**corpus/knowledge/linguistics/dialect-register-consistency.md**
- `:1` — `# Lect formation and drift mechanics: founder effects, koineization, focal and relic areas, and anti-language formation — what a built dialect map must not contradict`
- `:3` — `- topic: how lects form and drift inside one language — founder effects and migration trajectories, the koineization process model (mixing, leveling, simplification, reallocation, focusing) with its focusing deadline reconciled, focal/relic/transition area mechanics, and anti-language formation (anti-society conditions, overlexicalization zones, renewal, second-life trajectories) — the reference mechanics a built dialect map's internal consistency is checked against`
- `:71` — `## 5. Anti-language formation — conditions, renewal, second life`

**corpus/knowledge/linguistics/linguistic-anthropology.md**
- `:3` — `- topic: Language as cultural practice — ethnography of communication (Hymes SPEAKING grid), calibrated linguistic relativity, language ideology, register ecology (diglossia, politeness, speech levels), and special languages (ritual registers, avoidance registers, argot/anti-languages). Reference knowledge and method only; canon decisions belong to lore-shokunin.`
- `:115` — `### 5.3 Thieves' argot and anti-languages`

**corpus/knowledge/linguistics/register-lexicon-ceilings.md**
- `:3` — `- topic: Why a marked register built by a **mechanical operation** (reversal, truncation, lengthening, reduplication) can only spell some of the semantic fields its own institution needs — and how to measure the ceiling before it is designed into a law. States the general craft rule (**a register's derivation operation constrains which semantic fields it can natively spell**), gives the measurement procedure over a syllable template, works the NON-CANON D4 stamp register as a measured case (four of five legal/institutional abstractions refuse `reverse`), and supplies the three dispositions (hand-pick the base list, choose an operation whose domain covers the needed fields, or accept the ceiling and write the law inside it) plus the calibration shelf for the real-world analogues (verlan, anti-languages, avoidance registers) and their limits. Reference knowledge and…`

**corpus/knowledge/linguistics/sociolinguistics-registers.md**
- `:110` — `## 7. Age-grading and slang`

**corpus/knowledge/myth-symbol/ritual-liminality.md**
- `:3` — `- topic: The ritual toolkits a worldbuilder uses to generate transitions, exchanges, killings, and time-cycles — van Gennep's three-phase rite-of-passage grammar (separation / liminality / incorporation) applied to life-crisis, territorial and funerary rites; Turner's deepened liminality, communitas vs anti-structure, social-drama four-phase plot engine, liminoid; Mauss's gift (three obligations, hau, kula, potlatch with full colonial-contact calibration); sacrifice theories and a working typology table with substitution logic; calendrical rites (renewal, reversal, intercalation, invented traditions); and the mapping of ritual grammar onto narrative structure (plot skeletons, liminal characters and spaces, performative ritual language) — with build or…`

**corpus/knowledge/synthesis/dialect-faction-map-workflow.md**
- `:2` — `- topic: Map dialect features and situational registers onto travel networks, factions, hereditary strata, and eras without making political borders into linguistic facts; diagnose focal/relic areas, koineization, and faction jargon.`
- `:116` — `## 7. Build faction jargon from tasks and symbolic reuse`

**corpus/knowledge/synthesis/religion-language-co-evolution.md**
- `:3` — `- topic: How ritual authority preserves, translates, restricts, and reforms language; coupling liturgical fossilization, prayer languages, schism linguistics, priestly cants, sacred symbols, historical stages, and material display without generating canon.`
- `:79` — `## 6. Priestly cants as closed registers, not automatic secret languages`

Counts by term (same command, one term at a time; base tree):
`argot` 2 · `anti-language` 3 · `cants` 2 · `jargon` 2 · `reversal` 2 · `slang` 1 · `secret language` 1
(in `secret languages`) · `verlan` 1 · `ludling` 0 · `backslang` 0 · `polari` 0 · `pig latin` 0 ·
`rhyming slang` 0.

### 1b. Working tree — 19 matching lines in 8 files

Same 12 lines, plus 7 lines of the pending entry `corpus/knowledge/linguistics/secret-and-ludic-languages.md`:

- `:1` — `# Secret, ludic and anti-language registers`
- `:3` — `- topic: secret, ludic and anti-language registers: argot and cant as closed in-group vocabularies, anti-languages as social structure maintained through conversation, backslang and reversal games, ludling and Pig Latin style word play, in-group concealment and identity functions, and the design procedure for a fictional secret register`
- `:12` — `## 1. Scope: argot and cant as design questions`
- `:61` — `## 4. Anti-language: design the conversational relationship`
- `:77` — `## 5. Backslang and reversal games: define the operation`
- `:95` — `## 6. Ludling and Pig Latin style word play: a bounded prototype`
- `:109` — `## 7. Argot and cant: build a useful lexical slice`

### 1c. Body prose at base that names the same topic (not headings/topic lines, but the same ground)

- `corpus/knowledge/linguistics/linguistic-anthropology.md:120` — "many synonyms in salient domains (dozens of cant terms for "gallows" or "prostitute" in early modern cant lists)"
- `corpus/knowledge/linguistics/linguistic-anthropology.md:121` — "Metaphor and deformation: backslang, rhyming substitution, phonological disguising (Pig Latin, French verlan, Cockney rhyming slang)."
- `corpus/knowledge/linguistics/linguistic-anthropology.md:122` — "Resocialization: learning the argot IS induction into the anti-society (Maurer 1940, The Big Con, on grifter cant)."
- `corpus/knowledge/linguistics/linguistic-anthropology.md:125` — "Documented corpus to draw on: Harman 1566, A Caveat for Common Cursitors (first English cant list); B.E., c.1698, New Dictionary …; Grose 1785 …; Spanish germanía …; Lunfardo …; Polari (fairground, naval, gay men's code; Baker 2002); Grypsera in Polish prisons (Halliday 1976)."
- `corpus/knowledge/linguistics/linguistic-anthropology.md:135` — decision-table row `| Argot / anti-language | Criminal or persecuted group | Re-/overlexicalization, deformation | Fast turnover | Insider vs police | Cant, Polari (Halliday 1976; Baker 2002) |`
- `corpus/knowledge/linguistics/linguistic-anthropology.md:136` — decision-table row `| Ludling (word game) | Play, child culture | Phonological rule applied live | Learned in minutes | Wit, brief secrecy | Verlan, Pig Latin |`
- `corpus/knowledge/linguistics/sociolinguistics-registers.md:35` — "- Baker (2002), Polari: The Lost Language of Gay Men, Routledge; Tiersma (1999), Legal Language, U Chicago Press"
- `corpus/knowledge/linguistics/sociolinguistics-registers.md:84` — "Anti-languages (Halliday 1976): underworlds, soldiery, prisons relexicalize … Elizabethan canting, Polish grypsera, Polari (Baker 2002)"
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:13,180,233-234` — Gotowski (2019) "La règle du jeu: Verlan as an example of anti-faithfulness", with a verlan row (`:180`) and the contested-constraint note (`:233-234`)
- `corpus/knowledge/linguistics/dialect-register-consistency.md:74` — "an anti-language presupposes an **anti-society** — a defined excluded group …"
- `corpus/knowledge/culture-material/trade-economy-lexicon.md:103` — "**Trade tongues and cants**: … beggar-and-peddler cant codified by Harman (1566); Cockney rhyming slang out of 19th-c. East End market porters."
- `corpus/knowledge/synthesis/religion-language-co-evolution.md:15` — "**Priestly cant:** use this analytical label only for a demonstrably bounded specialist repertoire …"

## 2. The exact command for (1), and its count

Run from the lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (base reading run from the
materialized base tree `<scratch>/base-tree`, same relative path `corpus/knowledge`):

```
grep -rnEi '^(#{1,6} |- topic:)' corpus/knowledge \
  | grep -Ei '(^|[^a-z])(argot|anti-language|ludling|cants?|pig latin|verlan|backslang|polari|rhyming slang|secret languages?|jargon|slang|reversals?)([^a-z]|$)'
```

| tree | matching lines | distinct files | rc of the pipeline |
|---|---|---|---|
| base `d39434b3` (materialized) | **12** | **7** | 0 |
| working tree | **19** | **8** | 0 |

Distinct base files (7): `linguistics/dialect-register-consistency.md`,
`linguistics/linguistic-anthropology.md`, `linguistics/register-lexicon-ceilings.md`,
`linguistics/sociolinguistics-registers.md`, `myth-symbol/ritual-liminality.md`,
`synthesis/dialect-faction-map-workflow.md`, `synthesis/religion-language-co-evolution.md`.

Excluded as substring artefacts (checked, not counted): *polarity* in
`culture-material/calendar-festival-systems.md:3` and `myth-symbol/purity-pollution-boundary-systems.md:4,23`;
*overland* in `culture-material/transport-mobility-lexicon.md:4`.

For comparison, the claim's own topic list (`argot;anti-language;backslang;ludling;cant;in-group concealment`)
matches only **3** linguistics topic lines at base (`dialect-register-consistency.md`,
`linguistic-anthropology.md`, `register-lexicon-ceilings.md`) and **4** corpus-wide `- topic:` lines.
Widening the term set to the whole register family (`register|secret|jargon|slang|argot|cant|anti-language|ludic|special language|vernacular|in-group|conceal|occupational`) gives **12** linguistics topic-line owners, and **13** only if pun/riddle/word-play/child vocabulary is added — so the frozen claim's "13 linguistics entries" figure is not reproducible from a term set narrower than that, while the narrow-set figure (3) is what the frozen topic list actually yields.

## 3. Rows in corpus/SOURCES.md whose `teaches` or `scope` cell names one of those terms

Command (run from the lane root; boundary-safe, so *significant*/*supplicant*/*dedicant* do not count
as *cant*):

```
awk -F'|' '/^\| S/ {s=tolower($6" "$8); if (s ~ /(^|[^a-z])(argot|anti-language|ludling|cants?|pig latin|verlan|backslang|polari|rhyming slang|secret languages?|jargon|slang|reversals?)([^a-z]|$)/) print $2" tier="$5" status="$9}' corpus/SOURCES.md
```

Column map (header at `corpus/SOURCES.md:28`): `$2`=id, `$5`=tier, `$6`=scope, `$8`=teaches, `$9`=status.

### Working tree (880 rows) — count = 5

| id | tier | status | term | scope cell | teaches cell |
|---|---|---|---|---|---|
| S414 | A | mined | reversal | "…; the medieval reversal (wives impaled husbands' arms, on ladies' seals)" | heraldic impalement/quartering — **not** a language register (lexical false positive for this round) |
| S952 | B | mined | polari | "named scholar's overview of Polari lexicon and social use" | "Polari's spelling variants and mixed lexical sources distinguish a social register from a complete invented grammar." |
| S953 | B | mined | polari | "publisher description, not inspection of full book" | "The publisher places Polari's British urban users in the twentieth century…" |
| S954 | A | mined | cant | "the printed hostile representation of cant, not transparent community testimony" | "A hostile compiler's framing must remain attached to a printed cant glossary rather than becoming a neutral account of its users." |
| S955 | B | mined | verlan | "sociolinguistic interpretation of French urban verlan" | "Verlan's exclusion and recognition functions require named audiences and social relations in a fictional register." |

All five are `mined`; S952–S955 opened 2026-11-05 with `used-by = corpus/knowledge/linguistics/secret-and-ludic-languages.md`;
S956 (rejected, tier C) is **not** in this list — its scope/teaches cells carry no register term (its *source* cell
reads "Wikipedia, Argot").

### Base tree `d39434b3` (875 rows) — count = 1

Only **S414** (heraldry, false positive). At base there is **no** registry row for argot, cant, anti-language,
Polari, verlan, ludling, Pig Latin, backslang, rhyming slang, secret language or jargon.

Registry row count: base 875 (`grep -c '^| S'` on base SOURCES.md), working tree 880 (+6: S952–S956; base last id S951, worktree last id S956).

## 4. Which existing rows already hold the ground the four captures would hold

**No base registry row duplicates any of S952–S955.** Measured against the base registry (875 rows):

| cited work or subject | base `corpus/SOURCES.md` hits | base corpus prose |
|---|---|---|
| Halliday 1976 "Anti-languages" | 0 | `linguistic-anthropology.md:117`, `sociolinguistics-registers.md:84` |
| Baker 2002 *Polari: The Lost Language of Gay Men* | 0 ("Lost Language" → 0, "Polari" → 0) | `linguistic-anthropology.md:135`, `sociolinguistics-registers.md:35` |
| Harman, *A Caveat for Common Cursitors* | 0 ("Caveat for Common" → 0) | `linguistic-anthropology.md:125`, `trade-economy-lexicon.md:103` (both give the year as **1566**) |
| Gotowski 2019 on verlan | 0 | `register-lexicon-ceilings.md:13,180,233-234` |
| Maurer 1940 *The Big Con*, Grose 1785, Coleman's dictionary tradition | 0 / 0 / 0 | `linguistic-anthropology.md:121-125` |
| LEME lexicon 109; lancaster.ac.uk Baker Polari page; taylorfrancis 10.4324/9780203167045; openedition cdlm/729 | 0 / 0 / 0 / 0 (and `journals.openedition.org/cdlm` → 0) | — |

Consequence: the four captures are **net-new registry rows** over sources the corpus already *cites in prose*
but never registered. The duplication risk is therefore not a registry row but the two adjacent corpus owners
named in the frozen claim's bounds:

- `corpus/knowledge/linguistics/linguistic-anthropology.md` §5.3 "Thieves' argot and anti-languages" and the
  §5.4 decision table already hold the mechanism list, the anti-society account, the documented-corpus list
  (Harman, Grose, germanía, Lunfardo, Polari, grypsera) and the `Argot / anti-language` and `Ludling` rows.
- `corpus/knowledge/synthesis/religion-language-co-evolution.md` §6 "Priestly cants as closed registers, not
  automatic secret languages" already holds the access-ledger design heuristic for closed registers.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md` already holds verlan as a *mechanical operation*
  with a measured constraint ceiling (`:180`), which is a different question from verlan as a social register.

The pending entry already handles this: `secret-and-ludic-languages.md:16` names
`linguistic-anthropology.md` §5.3 as the adjacent owner and states it "does not reproduce its mechanism list or
comparative catalogue". It does not cite `religion-language-co-evolution.md` §6, `register-lexicon-ceilings.md`,
`sociolinguistics-registers.md`, `dialect-register-consistency.md` or `trade-economy-lexicon.md` anywhere
(`grep -n` over the entry: 0 hits for each of those five paths).

**One discrepancy to flag (not fixed by this seat, no write):** the base corpus dates Harman **1566**
(`linguistic-anthropology.md:125`, `trade-economy-lexicon.md:103`), while the LEME capture, the manifest
(`reports/round-91/evidence/manifest.json`, S954) and the new registry row S954 all give **1567**
(`LEMEdate:"1567"`, `lextitle:"... (1567)"` in `reports/round-91/evidence/S954.txt`). The new row and the
adjacent base prose therefore state different years for the same work; the base rows are append-only and
cannot be edited, so the L1 should decide whether the entry needs to name the divergence.

## 5. Verdict — is there a dedicated entry on this topic at base?

Command, run exactly as the brief specifies:

```
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree -r --name-only d39434b3bc8458e1b66edd2d0d0fea9ea32f3331 corpus/knowledge | grep -Ei 'argot|slang|secret|ludic|cant|jargon|pig|verlan|polari'
```

Output verbatim: *(no output — zero lines)*. Exit status of the pipeline: `grep` returned **1** (no match);
`git ls-tree` returned 0. **Verdict: no.** At base `d39434b3` there is no dedicated entry on secret, ludic or
anti-language registers: no filename under `corpus/knowledge` holds any of argot, slang, secret, ludic, cant,
jargon, pig, verlan or polari, and the partition holds 35 linguistics files (`git ls-tree -r --name-only
d39434b3 corpus/knowledge/linguistics | wc -l` → 35) with the register ground distributed as sub-sections of
`linguistics/linguistic-anthropology.md` §5.3/§5.4 (argot, anti-languages, ludling as decision-table rows),
`linguistics/sociolinguistics-registers.md` §7 (slang) and its anti-language bullet at `:84`,
`linguistics/dialect-register-consistency.md` §5 (anti-language formation), `linguistics/register-lexicon-ceilings.md`
(verlan as a mechanical operation) and `synthesis/religion-language-co-evolution.md` §6 (priestly cants as closed
registers). Twelve heading/topic lines across seven files name the register; no file owns it. The pending
working-tree entry `corpus/knowledge/linguistics/secret-and-ludic-languages.md` (untracked, 21,472 bytes,
7 matching heading/topic lines) is the first dedicated owner, and it does not exist at base
(`git cat-file -e d39434b3:corpus/knowledge/linguistics/secret-and-ludic-languages.md` → rc 128,
"exists on disk, but not in d39434b3…").

## Commands run (rc)

| command | rc | note |
|---|---|---|
| `git archive d39434b3 corpus \| tar -x -C <scratch>/base-tree` | 0 | materialize base bytes |
| `grep -rnEi '^(#{1,6} \|- topic:)' corpus/knowledge \| grep -Ei '(^\|[^a-z])(argot\|anti-language\|ludling\|cants?\|pig latin\|verlan\|backslang\|polari\|rhyming slang\|secret languages?\|jargon\|slang\|reversals?)([^a-z]\|$)'` | 0 (12 base / 19 worktree lines) | item 1 |
| per-term variants of the same pipeline | 0 | term-by-term counts |
| `awk -F'\|' '/^\| S/ {s=tolower($6" "$8); if (s ~ /…/) print $2" tier="$5" status="$9}' corpus/SOURCES.md` | 0 (5 worktree / 1 base rows) | item 3 |
| `grep -c '^| S' corpus/SOURCES.md` | 0 (880 worktree / 875 base) | registry size |
| `git ls-tree -r --name-only d39434b3 corpus/knowledge \| grep -Ei 'argot\|slang\|secret\|ludic\|cant\|jargon\|pig\|verlan\|polari'` | 1 (empty output) | item 5 |
| `git ls-tree -r --name-only d39434b3 corpus/knowledge \| grep -Eic '(secret\|ludic\|argot\|slang\|cant\|jargon)'` | 1 (0 matches) | claim's own surface figure, reproduced |
| `git ls-tree -r --name-only d39434b3 corpus/knowledge/linguistics \| wc -l` | 0 (35) | partition size at base |
| `git diff --stat d39434b3 -- corpus/knowledge` | 0 (empty) | worktree == base for knowledge, except untracked new entry |
| `git diff --stat d39434b3 691aebf -- corpus/knowledge` | 0 (empty) | freeze == base for knowledge |
| `git cat-file -e d39434b3:corpus/knowledge/linguistics/secret-and-ludic-languages.md` | 128 | entry absent at base |
| `grep -c '<term>'` over base `corpus/SOURCES.md` for Halliday / Baker 2002 / Harman / Gotowski / Polari / verlan / Maurer / Big Con / Grose / LEME / openedition cdlm | 0 | item 4 duplicate check |
| `grep -rniE '1567\|Caveat for Common' corpus/knowledge` on base tree | 0 / 1 | Harman year divergence (1566 in base prose vs 1567 in capture) |

No tool was installed or upgraded by this seat; no network fetch was made.
