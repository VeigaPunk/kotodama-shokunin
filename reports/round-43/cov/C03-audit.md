# C03 — Pre-landing source audit 1: the C01 lithic spare

- seat: C03 (verifier, claim C) · round 43 · 2026-10-19
- audited artifact: `reports/round-42/cov/C01-mineral-spare.md`
  (sha256 `2b9326e351de0e324bce3e71d45390c4a03e838138902ffcf23a971704ef6156`, 219 lines)
- audit HEAD: `7ceff59` (`git rev-parse --short HEAD`)
- comparison baseline named by the spare: `ac47c78` (r41 admission)
- commands run with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; no
  `run-validation.py` executed; no filed byte edited; scratch scripts under
  `.scratch/c03/` only.

## Verdict (read this first)

**Citation integrity: PASS with two minor defects (F3, F4).**
Every in-repo path in the spare resolves, every cited line range is within
bounds, and the spare's own measured sweeps reproduce exactly at the HEAD it
names. No fabricated source was found: all unconsulted literature is already
marked `(to-verify)` by the spare itself.

**Landing readiness: FAIL — blocking findings F1 and F2.**
The spare is not a gap-filler at the current HEAD. Its topic — the lithic
register — is already owned by `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`,
which is byte-for-byte the r42 C04 draft and is indexed in README rev 2.4. The
spare's `- gap filled:` line ("no entry owns stone", zero filename hits) was true
at `ac47c78` but is false at `7ceff59`. Landing it as the round-43 C claim
describes would create a duplicate topic and a stale provenance claim.

An auditor cannot clear this draft for landing under the claim's present scope.
Reporting the collision, not routing around it.

---

## F1 (blocking) — the lithic slot is already owned; C04's landing is byte-identical

Evidence, each independently checkable:

1. The spare's own first line, `reports/round-42/cov/C01-mineral-spare.md:1`:

   > Integrator ruling 2026-10-19: C01 and C04 authored the same lithic topic
   > mid-wave (K02's gap scout assigned it twice). C04 lands ...; THIS draft is
   > routed as the named spare for a future re-scoped claim.

   So the r42 ruling is explicit: the spare is valid only after a **re-scope**.
   No re-scope has been filed; round-43 claim C re-uses the same topic.

2. `corpus/README.md:5-9` (rev 2.4) records the same ruling in the filed index:

   > revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
   > myth-symbol entries landed (`mineral-stone-symbolism.md`, ...); a fourth
   > draft (C01's lithic register) collided with C04's and is routed as a named
   > spare by integrator ruling.

3. The landed file exists and is the C04 draft, not a different lithic take.
   Fence extraction from `reports/round-42/cov/C04-entry-4.md` and the landed
   `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` both hash to
   `072d1f1a18de501041036ef94609adc79ec92a2ba4351302d8e16099c71911f1`
   (61,342 chars; `identical: True`). Landed file sha256:
   `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f`.

4. `git show --diff-filter=A --name-only --format="" 7ceff59` lists
   `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` among the three
   files added by the round-42 commit.

5. Live partition at audit HEAD:

   ```
   $ ls corpus/knowledge/myth-symbol/*.md | wc -l
   26
   $ find corpus/knowledge -name '*.md' | wc -l
   223
   $ ls corpus/knowledge/*/ | grep -i 'mineral\|stone\|gem\|lithic'
   mineral-stone-symbolism.md
   ```

   The natural target filename is also taken: K02 proposed exactly
   `mineral-stone-symbolism.md` (`reports/round-42/scout/K02-myth-gaps.md:212`),
   and that is the file C04 landed.

**Consequence for claim C.** The claim's premise — "lithic slot named but
unbuilt since r42" — is contradicted by the live tree and by the filed README.
A C01 landing at myth-symbol 26→27 would be a second lithic register, not the
completion of an unbuilt slot. It would also make README rev 2.5's row
description false. This is a claim-scope defect upstream of the audit, not a
defect the integrator can patch by renaming a file.

## F2 (blocking, same root) — the spare's absence sweep is stale at HEAD

The spare's `- gap filled:` line (spare:7) states, dated at `ac47c78`:

> no **filename** carries `mineral`, `stone`, `gem` or `lithic`
> (`ls corpus/knowledge/*/ | grep -i 'mineral\|stone\|gem\|lithic'` → 0 hits)

That measurement is **true at the revision it names** and **false at the
revision a round-43 landing would create**. Re-run at audit HEAD:

```
$ ls corpus/knowledge/*/ | grep -i 'mineral\|stone\|gem\|lithic'
mineral-stone-symbolism.md
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
25 26 25 29 24 94
```

The spare's `- verified-at:` line (spare:24) still names `ac47c78` and 220
files. Applying it unchanged would file a date-stamped provenance claim that is
already false on the day it lands. This is exactly the "measured absence"
failure mode the round's shared rules forbid: a stale count presented as a
current gap.

## F3 (minor) — Frazer citation is off by one line

Spare:21 (calibration) says the sympathetic-magic disposition is:

> the same disposition the corpus applies to Frazer at
> `corpus/knowledge/linguistics/politeness-taboo-euphemism.md:73`

Measured:

```
$ sed -n '73p' corpus/knowledge/linguistics/politeness-taboo-euphemism.md
- Steiner (1956): taboo is not "forbidden" but **charged** ... Radcliffe-Brown (1939) ... Douglas (1966) ...
$ grep -n "Frazer" corpus/knowledge/linguistics/politeness-taboo-euphemism.md
21:  - Frazer (1890), The Golden Bough (taboo chapters; ethnography discredited — see Calibration); ...
74:- Frazer's two laws — contagion ... and similarity ... — are discredited as ethnographic history but survive as a usable **folk-model** ...
124:- **Frazer's Golden Bough**: comparative ethnography discredited; the contagion/similarity laws survive as folk-model ...
```

Line 73 contains no Frazer and no disposition. The disposition the spare
describes is at **:74** (method) and **:124** (calibration), with the
registration at **:21**. Verdict: wrong line locator, correct file, correct
substance — an off-by-one, not a fabricated source.

## F4 (minor) — `symbolism-synthesis-method.md:48` paraphrase drift

Spare:80 cites `:48` for "3–5 load-bearing **slots** chosen from a real
**enumeration**". Actual line 48:

> 1. **Choose 3–5 load-bearing polarity axes** (hot/cold, wet/dry, ...).

The `3–5` count is right; "polarity axes" is not "slots" and no "enumeration"
appears on the line. Verdict: paraphrase, usable as an analogue, but the
citation should not be read as a literal statement about material-class slots.
No action required beyond wording if the entry is ever re-scoped.

## F5 (provenance nuance) — three same-round `reports/round-42/` paths did not exist at `ac47c78`

`git cat-file -e ac47c78:<path>` returns nonzero for:

```
reports/round-42/claims.json
reports/round-42/plan/P01-plan.md
reports/round-42/scout/K02-myth-gaps.md
```

They are cited by the spare as topic authority (spare:7, :20, :23, :24) and all
exist at HEAD with the content claimed. They are same-round artifacts authored
after the declared baseline, so "resolves on disk at that HEAD" in spare:24 is
overbroad for them. Not fabrication; a provenance wording defect. Worth noting
because the round-43 O-claim and C-claim both depend on same-round artifacts in
the same way.

---

## Citation inventory — every backticked in-repo path

Scanner: `.scratch/c03/audit.py` extracts the fenced entry, every backticked
token containing `.md`, resolves bare basenames uniquely, then checks each
`:N` / `:N-M` against the target file's line count. Two passes: at HEAD and
against `git show ac47c78:<path>`.

- 173 backticked `.md` occurrences; **86 unique citation tokens**.
- 85 resolve to exactly one path; 1 is basename-ambiguous and resolves by
  context (`maya-classic.md:10` inside a bullet that names
  `corpus/knowledge/civilizations/maya-classic.md` in full; the competing hit is
  a filed r17 report, not the intended target).
- 38 distinct full-path citations; 0 missing at HEAD.
- 0 out-of-bounds line ranges at `ac47c78` and 0 at HEAD.
- 16 context-relative locators (`:14`, `:127`, `:84-91`, ...) attributed to the
  preceding path in the same bullet: all in range.

| cited file | spare lines | locators asserted | file lines (HEAD) | status |
|---|---|---|---|---|
| `corpus/QUALITY.md` | 22–214 | :9-12, :16-17, :18-20 | 24 | OK |
| `corpus/knowledge/civilizations/china-shang-zhou.md` | 7–145 | :106 | 187 | OK |
| `corpus/knowledge/civilizations/maori.md` | 7–192 | :13, :14, :20 | 208 | OK |
| `corpus/knowledge/civilizations/maya-classic.md` | 7–190 | :10, :127 | 209 | OK |
| `corpus/knowledge/civilizations/rome.md` | 7 | :33 | 200 | OK |
| `corpus/knowledge/civilizations/siam-thai.md` | 7–190 | :126 | 188 | OK |
| `corpus/knowledge/culture-material/architecture-settlement-lexicon.md` | 22–217 | path only | 150 | OK |
| `corpus/knowledge/culture-material/craft-artisan-lexicon.md` | 7–217 | path only | 155 | OK |
| `corpus/knowledge/culture-material/funerary-material-culture.md` | 7–217 | :22 | 222 | OK |
| `corpus/knowledge/culture-material/material-culture-inference-method.md` | 7–217 | path only | 110 | OK |
| `corpus/knowledge/culture-material/ritual-garments.md` | 7–217 | :59 | 157 | OK |
| `corpus/knowledge/culture-material/sumptuary-law-rank-display.md` | 7–217 | path only | 113 | OK |
| `corpus/knowledge/culture-material/trade-economy-lexicon.md` | 19–217 | path only | 167 | OK |
| `corpus/knowledge/culture-material/vessel-container-lexicon.md` | 7–217 | path only | 176 | OK |
| `corpus/knowledge/linguistics/naming-systems.md` | 22–216 | path only | 137 | OK |
| `corpus/knowledge/linguistics/politeness-taboo-euphemism.md` | 21–184 | :73 | 136 | **F3 — line exists, content is not Frazer** |
| `corpus/knowledge/linguistics/semantic-fields-lexicon-building.md` | 22–216 | path only | 163 | OK |
| `corpus/knowledge/linguistics/semantics-pragmatics.md` | 22–216 | path only | 138 | OK |
| `corpus/knowledge/myth-symbol/animal-symbolism.md` | 7–215 | :13, :84-91 | 134 | OK |
| `corpus/knowledge/myth-symbol/color-symbolism.md` | 7–215 | :11 | 167 | OK |
| `corpus/knowledge/myth-symbol/cosmology-cosmography.md` | 7–215 | path only | 156 | OK |
| `corpus/knowledge/myth-symbol/death-afterlife-eschatology.md` | 22 | path only | 192 | OK |
| `corpus/knowledge/myth-symbol/direction-symbolism.md` | 7–215 | path only | 203 | OK |
| `corpus/knowledge/myth-symbol/number-symbolism.md` | 22 | path only | 144 | OK |
| `corpus/knowledge/myth-symbol/pantheon-archetypes.md` | 22 | path only | 118 | OK |
| `corpus/knowledge/myth-symbol/plant-symbolism.md` | 7–32 | :15 | 198 | OK |
| `corpus/knowledge/myth-symbol/ritual-liminality.md` | 22 | path only | 137 | OK |
| `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md` | 22–215 | path only | 204 | OK |
| `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md` | 7–215 | :9, :23, :29, :47, :48, :51, :64 | 173 | OK (F4 on :48 wording) |
| `corpus/knowledge/synthesis/coupling-model.md` | 22 | path only | 204 | OK |
| `corpus/knowledge/synthesis/myth-to-language-derivation.md` | 22 | path only | 183 | OK |
| `corpus/knowledge/synthesis/symbol-lexicon-colexification.md` | 22 | path only | 198 | OK |
| `corpus/knowledge/verification/calibration-registry.md` | 22–218 | path only | 191 | OK |
| `corpus/knowledge/verification/myth-consistency-gate.md` | 22–218 | path only | 215 | OK |
| `corpus/knowledge/verification/real-world-inspiration-boundaries.md` | 7–218 | path only | 173 | OK |
| `corpus/knowledge/verification/to-verify-triage-protocol.md` | 22–218 | path only | 219 | OK |
| `reports/round-42/plan/P01-plan.md` | 7–23 | :352-365 | 621 | OK at HEAD; absent at `ac47c78` (F5) |
| `reports/round-42/scout/K02-myth-gaps.md` | 7–97 | path only | 545 | OK at HEAD; absent at `ac47c78` (F5) |
| `reports/round-42/claims.json` | 24 | path only | — | OK at HEAD; absent at `ac47c78` (F5) |

Non-citation backticked strings (`corpus/knowledge/`, two `find`/`for` shell
commands) are excluded — they are commands, not paths.

## Line-content verification — the load-bearing citations

Each row: what the spare claims the cited line says, versus what the line
actually says at HEAD. Quotations below are excerpts; line numbers are the
spare's Read numbering.

| spare line | citation | claim in spare | measured line content | verdict |
|---|---|---|---|---|
| 7 | `symbolism-synthesis-method.md:23` | the five canonical registers, colour/animal/number/celestial/direction | "the five canonical registers: **color, animal, number, celestial body, direction**" | VERIFIED exact |
| 7 | `symbolism-synthesis-method.md:29` | package = bestiary + lapidary + numerology + heraldic code | "**The medieval Latin package**: bestiary + lapidary + numerology + heraldic code" | VERIFIED exact |
| 7 | `plant-symbolism.md:15` | plant cannot flee; owned/inherited/fenced/taxed/boundary marker | identical sentence at :15 | VERIFIED exact |
| 7 | `color-symbolism.md:11` | "A color never carries a meaning by itself; a code does" | identical sentence at :11 | VERIFIED exact |
| 7 | `ritual-garments.md:59` | choshen, 12 gemstones one per tribe, zodiac reading attributed to Philo/Josephus | "12 gemstones, one per tribe ... the 12 stones as the zodiac (Philo; Josephus)" | VERIFIED |
| 7 | `funerary-material-culture.md:22` | Pliny *NH* 36.27, *sarcophagus* stone of Assos, Bostock & Riley | "Pliny ... 36.27 (the *sarcophagus* stone of Assos ...); ... Bostock & Riley's (1855)" | VERIFIED |
| 7 | `maya-classic.md:10` | Taube 2005 registered with DOI and inspected abstract | "[T] Karl A. Taube (2005) ... 16(1):23–50. [DOI](https://doi.org/10.1017/S0956536105050017). Bibliography and publisher abstract inspected" | VERIFIED |
| 7 | `maya-classic.md:127` | caution: "not every jade object expresses all associations simultaneously" | identical caveat at :127 | VERIFIED exact |
| 7 | `china-shang-zhou.md:106` | heirloom rule: old object in later burial ≠ later manufacture | identical sentence at :106 | VERIFIED exact |
| 7 | `maori.md:13`, `:14` | Ngāi Tahu "Pounamu" read 2026-10-17; Te Ara pounamu entry retrieved 2026-10-17 | both registrations present with those dates | VERIFIED |
| 7 | `maori.md:20` | named knowledge holders; local checking before reuse | "require named knowledge holders, local checking, and the cited editions before reuse" | VERIFIED (spare paraphrases, does not quote) |
| 7 | `siam-thai.md:126` | Emerald Buddha as dynastic palladium + anti-universal caveat | "functions as a dynastic palladium in Reynolds's analysis ... not a universal rule that every epic needs a sacred gemstone" | VERIFIED exact |
| 7 | `rome.md:33` | "lapidary capitals" epigraphic sense, not gem-lore | "an empire does not write everything in lapidary capitals" | VERIFIED |
| 7 | `vessel-container-lexicon.md` | same container-name mechanism for vessels | file owns "container-as-unit metonymy" and a material-based naming strategy (:3); no *sarcophagus* | VERIFIED in substance, not literal |
| 17, 19 | `animal-symbolism.md:13` | White 1954 and Fox-Davies 1909 registered | both named at :13 | VERIFIED |
| 18 | `symbolism-synthesis-method.md:9` | Hopper 1938 registered | "Hopper (1938), Mediaeval Number Symbolism, Columbia UP" | VERIFIED |
| 19 | `symbolism-synthesis-method.md:64` | rule of tincture quoted | "heraldry's **rule of tincture** (metal on colour; Fox-Davies 1909)" | VERIFIED exact |
| 149 | `symbolism-synthesis-method.md:47` | step 0, fix the material substrate | "0. **Fix the material substrate** ..." | VERIFIED exact |
| 158 | `symbolism-synthesis-method.md:51` | mark UNALIGNED with a reason | "mark the cell **UNALIGNED** with a reason — never force smoothness" | VERIFIED exact |
| 22, 214 | `corpus/QUALITY.md:18-20` | canon decisions belong to lore-shokunin; entries end at handoff | lines 18-20 say exactly that | VERIFIED exact |
| 196 | `corpus/QUALITY.md:9-12` | calibration clause | "every framework entry names its status: mainstream / contested / discredited" | VERIFIED |
| 196 | `corpus/QUALITY.md:16-17` | usability clause | "a worldbuilder can act on it: decision tables, typology" | VERIFIED |
| 21 | `politeness-taboo-euphemism.md:73` | Frazer disposition | line 73 = Steiner/Radcliffe-Brown/Douglas; Frazer at :74, :124, :21 | **F3 FAIL** |

## The spare's measured sweeps, reproduced at its own HEAD

All counts below were produced with `git grep ... ac47c78 -- 'corpus/knowledge/**/*.md'`
and `git ls-tree -r --name-only ac47c78 corpus/knowledge`, i.e. against the
committed tree the spare names, not the working tree.

| claim in spare:7 | measured at `ac47c78` | match |
|---|---|---|
| corpus total 220 files | 220 | YES |
| partition vector 25/23/25/29/24/94 | 25/23/25/29/24/94 | YES |
| filename sweep `mineral\|stone\|gem\|lithic` → 0 | 0 | YES |
| `grep -rli lapidary` → 2 files | 2 (`rome.md`, `symbolism-synthesis-method.md`) | YES |
| `grep -rli gemstone` → 2 files | 2 (`siam-thai.md`, `ritual-garments.md`) | YES |
| `grep -rli 'precious stone'` → 1 file | 1 (`newar-nepal.md`) | YES |
| `grep -rli mineral` → 6 files | 6 | YES |
| `grep -rli lithic` → 24 files | 24 | YES |
| topic-line sweep → 2 files, both false positives | 2 (`sound-symbolism.md` match is "Dingemanse"; `death-afterlife-eschatology.md` match is "gement") | YES |
| demand 39/220 files, 0 topic-owners | `K02-myth-gaps.md:115` row: demand 39, owners 0 | YES |
| commit message at `ac47c78` = "round-41: admit O/Ca ... luna 32/32 in 7 min" | `git log --oneline -1 ac47c78` → exact match | YES |

This is the strongest part of the draft: its measurements were real, correctly
commanded, and honestly dated. The failure is that they were not re-measured
after C04 landed the same topic in the same round.

## External-source audit — no fabricated source

| source leg in spare | status asserted by the spare | audit |
|---|---|---|
| Pliny, *NH* book 37 | not consulted; genre authority; powers layer discredited; `(to-verify)` | consistent; Pliny 36.27 and the Bostock & Riley edition verified in-lane at `funerary-material-culture.md:22`; no book-37 locator claimed |
| Marbod, *De lapidibus*; Philippe de Thaon | not consulted; `(to-verify)` | no in-lane registration claimed; marked |
| Taube 2005 | registered in-lane with DOI at `maya-classic.md:10`; not re-fetched | verified, including the DOI string and "abstract inspected" wording |
| Fu Hao tomb / heirloom rule | cited by path `china-shang-zhou.md:106`; `[C21; R95]` | verified |
| Ngāi Tahu "Pounamu"; Keane, *Te Ara* | registered `maori.md:13`, `:14`; read 2026-10-17 | verified, including retrieval dates |
| Emerald Buddha | `siam-thai.md:126`, Reynolds analysis + caveat | verified |
| Choshen twelve stones | `ritual-garments.md:59`, attributed to Philo/Josephus | verified |
| White 1954; Hopper 1938; Fox-Davies 1909 | registered at `animal-symbolism.md:13` and `symbolism-synthesis-method.md:9`; rule of tincture at `:64` | verified |
| Mineralogical properties (jade fibre, conchoidal fracture, corundum hardness) | standard reference knowledge, not retrieved; cite concept not page | explicitly flagged; no page locator asserted |
| Etymologies (*sarcophagus*, *obsidian*, *amethyst*, *jet*, *adamant*) | route/mechanism exemplars; chains `(to-verify)` | explicitly flagged; no dictionary locator asserted |

No invented work, DOI, page, or line was found. Every unverifiable literature
leg is already labelled `(to-verify)` by the draft itself (spare:9-11, :21, :24).

## Recommendation to the integrator

1. **Do not apply the C01 spare under the round-43 C claim as written.** The
   claim's premise ("lithic slot named but unbuilt") is contradicted by
   `mineral-stone-symbolism.md`, README rev 2.4, and the r42 ruling quoted at
   spare:1. This is a scope collision, not a byte-level fix.
2. If claim C is to proceed, it needs a **new, distinct scope** filed before
   landing — not a rename. The spare itself names one unowned adjacent surface
   in its couples line (`spare:22`): "the **quarry/mine production side**, which
   no corpus entry owns at this HEAD (owed — see §Owed)". Any such entry must be
   re-drafted and re-audited against the now-27th slot; it cannot be this file's
   fence applied unchanged.
3. README rev 2.5 as drafted by the C-claim seats inherits the same false
   premise (a new lithic row at 224). Do not land it until the scope question
   is resolved.
4. If, contrary to this audit, the parent decides the spare's unique material is
   wanted, it must go through a new-entry claim with a new filename (the K02
   name is taken) and a re-measured absence sweep, and its Frazer locator
   corrected from `:73` to `:74`/`:124`.

## What was not verified

- Any external work's text, edition or page — no network in this seat and the
  spare itself does not claim otherwise. `to-verify` as the spare already says.
- Semantic correctness of the entry's claims about real cultures. That is the
  contract/lore review surface (C04, R01, A01), not a source-locator audit.
- Whether the r42 C04 landing itself was admitted: `git log` says round-42 was
  "NOT ADMITTED on C". That is a filed-round fact, reported here only because it
  bears on the spare's status; this audit does not re-adjudicate it.

## Reproduce

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B .scratch/c03/audit.py            # path + line-bound inventory at HEAD
git ls-tree -r --name-only ac47c78 corpus/knowledge | grep '\.md$' | wc -l   # 220
git grep -l -i lapidary ac47c78 -- 'corpus/knowledge/**/*.md' | wc -l        # 2
git grep -l -i lithic   ac47c78 -- 'corpus/knowledge/**/*.md' | wc -l        # 24
git grep -l -i mineral  ac47c78 -- 'corpus/knowledge/**/*.md' | wc -l        # 6
ls corpus/knowledge/myth-symbol/*.md | wc -l                                 # 26
find corpus/knowledge -name '*.md' | wc -l                                   # 223
sha256sum reports/round-42/cov/C01-mineral-spare.md                          # 2b9326e3...
sha256sum corpus/knowledge/myth-symbol/mineral-stone-symbolism.md            # c99f44ca...
```
