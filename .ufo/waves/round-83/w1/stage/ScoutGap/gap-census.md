# Claim-D absence census — marriage as an alliance-and-transfer institution

Seat `ScoutGap`, round 83 wave 1. Read-only recon. Every byte below was read from the lane
object store at the pinned revisions, never from a working tree:

- base `3088bd7fe2a55a123214abba7008dcddf12b301c` (`round-82 verifier spot-check (integrator, hyaku): non-author admit/reject`)
- frozen claims/counters `21277b089e3c64c247bb4e0fcb033abfdfa1e668`

`$LANE` below means the lane repository root (`kotodama-shokunin`); no out-of-repo working path is cited
anywhere in this file (QUALITY criterion 31 binds from this round).

## 0. Reading authority (R82-M3)

Three readers touch this surface this wave. The lane's rule: **`ScribeRows`' fetch receipts bind
the registry rows; `ScoutSources`' reading is the independent second reading.** This census is a
**third, non-binding reading**: it measures committed bytes at the pinned base and, in §6 only,
probes candidate pages over plain HTTP. Where it disagrees with a binding receipt, the binding
receipt wins and the disagreement is reported, not silently resolved. No receipt from either peer
was readable when this seat ran (the wave stage tree held no `ScribeRows`/`ScoutSources` output),
so **no cross-reading comparison could be made** — that gap is stated in §8, not papered over.

## 1. Headline

| question | measured answer at base |
|---|---|
| does any `corpus/knowledge/**/*.md` basename own marriage? | **no — 0 of 256** |
| does any file own the *institution* (alliance + transfer)? | **no — 0 headings, 0 gap blocks, 0 topic claims** |
| is the surface present as passing attribute? | **yes — 9 files / 14 lines / 16 matches** for the exact institutional core; 116 files / 374 lines for the wide family |
| would the new file be the 257th? | **yes — 256 `.md` files at base** |
| are the four candidate works already registered? | **no — 0 rows each** (see §5) |
| are the two already-opened works usable instead of re-registered? | **yes — S904 (Homer) and S905 (Tacitus), both `mined`, both `used-by` the guest-right entry** |
| next free registry id | **S909** (max row `S908`; 832 rows on disk) |

## 2. Before-state A — filename sweep

Command (exactly the spec's pattern, basenames only):

```
$LANE> git -C "$LANE" ls-tree -r --name-only 3088bd7fe2a55a123214abba7008dcddf12b301c corpus/knowledge \
        | grep -Ei 'marriage|bride|dowry|wedding|spouse|betroth' | wc -l
```

Raw output: `0`. File count in the same listing: **256**.

A wider filename family (adds `wife|husband|widow|affinal|alliance|kin`) returns 6 files, and
**every one is a substring artifact, not an owner**:

```
civilizations/kongo-kingdom.md              <- "kingdom"
civilizations/korea-three-kingdoms-goryeo.md<- "kingdoms"
culture-material/cartography-and-mapmaking.md<- "mapmaking" -> "king"
culture-material/pastoralism-animal-husbandry.md <- "husbandry"
linguistics/kinship-terminology.md          <- "kin" (kin lexicon, not marriage)
myth-symbol/sacred-kingship-mythic-charter.md<- "kingship"
```

Partition census of the same listing (`awk -F/ '{print $3}' | sort | uniq -c`):

```
     95 civilizations
     42 culture-material
     34 myth-symbol
     32 linguistics
     29 synthesis
     24 verification
```

Sum 256. The entry lands in **`myth-symbol/`** (claim D's path), so that partition moves
**34 → 35**; `culture-material/` stays at 42.

## 3. Before-state B — the exact institutional core, and a refutation

Command:

```
$LANE> git -C "$LANE" --no-pager grep -Ei -n \
        'bridewealth|bride-price|bride price|dowry|betroth' \
        3088bd7fe2a55a123214abba7008dcddf12b301c -- 'corpus/knowledge'
```

Measured: **9 files, 14 lines, 16 matches.** The spec's expectation "9 files / 27 lines" is
**half right**: the file count reproduces exactly, the line count does **not**. No variant of the
pattern produces 27 lines at 9 files:

| pattern | lines | files |
|---|---|---|
| `bridewealth\|bride-price\|bride price\|dowry\|betroth` (spec core) | **14** | **9** |
| core `+ dower` | 16 | 11 |
| core `+ dower + trousseau + bridal` | 40 | 18 |
| core `+ "marriage portion"\|morgengabe\|"morning gift"` | 16 | 11 |
| `bride\|dowry\|betroth` (no bridewealth compounds) | 39 | 22 |

Match count, not line count, is 16: two lines carry two matches each. Likely origin of the
spec's 27: the round-82 hospitality entry's own `- gap filled:` records "vocabulary sweep … →
27 lines in 15 files" (`corpus/knowledge/myth-symbol/guest-right-hospitality-law.md:4`). The
27/15 pair belongs to *that* surface; the marriage core is 14/9. A landing that copies "27
lines" into the new header would install an unmeasured number.

The 14 lines, each classified — all passing attributes inside another system's entry:

| file:line | what it says | class |
|---|---|---|
| `civilizations/kongo-kingdom.md:101` | "dowry was glossed as nzimbu or other named goods" (Bentley 1895) | passing (shell-money entry) |
| `culture-material/adornment-body-codes.md:4` | bibliography line, core term inside the sources list | passing (bibliography) |
| `culture-material/adornment-body-codes.md:21` | "**Bridewealth and the woman's portion**: jewelry as gendered capital — South Asian *strīdhana* …" | passing (jewelry entry) |
| `culture-material/adornment-body-codes.md:22` | "dowry gold was regularly in hock" (Monti di Pietà) | passing |
| `culture-material/furniture-interior-lexicon.md:3` | topic line, dowry named as an extension | passing (topic) |
| `culture-material/furniture-interior-lexicon.md:81` | "the dowry chest (Italian *cassone* …) is a marriage contract in wood" | passing (furniture entry) |
| `culture-material/pastoralism-animal-husbandry.md:3` | topic line lists "bridewealth and raiding" | passing (topic) |
| `culture-material/pastoralism-animal-husbandry.md:23` | "animals move as gift, loan, bridewealth and raid" | passing (distribution row) |
| `culture-material/pastoralism-animal-husbandry.md:113` | "\| Bridewealth \| stock from groom's kin to bride's kin …\|" | passing, **borderline**: the only line in the corpus that states a direction rule |
| `culture-material/ritual-garments.md:104` | "cloth-giving is dowry politics" | passing (craft beat) |
| `culture-material/trade-economy-lexicon.md:125` | "marriage vocabulary is security vocabulary; Germanic *mundr* bride-price in Grágás … Lat. *dōs* → *dowry, dot*" | passing (etymology) |
| `linguistics/naming-systems.md:76` | "cognate theonyms are a comparative-linguistics dowry" — **metaphor** | passing (false positive for the surface) |
| `myth-symbol/animal-symbolism.md:73` | Nuer "cattle of money … names, songs, bridewealth" | passing (symbol entry) |
| `myth-symbol/ritual-liminality.md:22` | van Gennep's examples include "betrothal, marriage" | passing (rite grammar) |

No line of the 14 defines the institution, its parties, its transfer, its estate, its seal or its
breach. The closest to a definition is `pastoralism-animal-husbandry.md:113`, and that row
immediately defers: "the rights it transfers vary by culture `(to-verify)`".

## 4. Before-state C — structural ownership (headings, topics, gap blocks, couplings, index)

Gap-block denominator: **59** files carry exactly one `- gap filled:` and **8** carry exactly one
older `- gap:` (67 statements across 67 files, none with two). Grep for either key with the
surface terms → **0 hits**; in the wide family only two gap lines match, and both do so through a
path citation of `pastoralism-animal-husbandry.md` ("husbandry"), not through a marriage term.
Commands:

```
$LANE> git -C "$LANE" --no-pager grep -Ec '^- gap filled:' <base> -- corpus/knowledge   # 59 files
$LANE> git -C "$LANE" --no-pager grep -Ec '^- gap:'        <base> -- corpus/knowledge   #  8 files
$LANE> git -C "$LANE" --no-pager grep -Ein '^- (gap|gap filled):.*(marri|wedding|bride|dowry|betroth|spouse|alliance)' <base> -- corpus/knowledge
        -> (no output)
```

Headings: across the wide family, **6 headings name the surface, 0 own the institution.** The
word-bounded, sections-only scan (`^#{2,4}`) returns exactly **1** — the kinship §5 — so the
ownership claim rests on one substantive section and five title/passing headings:

```
pastoralism-animal-husbandry.md:1   title line ("bridewealth" inside the title)
ritual-garments.md:1                title line ("lifecycle-rite dres…" / wedding)
ritual-garments.md:93               ### Wedding — the white/red variance
sumptuary-law-rank-display.md:64    ## 6. England: price-schedule statutes, the cap act, and the wives problem
kinship-terminology.md:80           ## 5. Affinal logic: the marriage rule is usually IN the lexicon
linguistic-anthropology.md:104      ### 5.2 Avoidance registers ("mother-in-law languages")
```

Only one is a substantive marriage section — and it is about the **lexicon**, not the
institution (`kinship-terminology.md:80`, see the owner map).

Topic lines: **9** name the surface and **0** take it as the entry's subject. The nine are
`furniture-interior-lexicon.md:3` (dowry chest), `headgear-head-covering-codes.md:3`,
`pastoralism-animal-husbandry.md:3`, `ritual-garments.md:3`, `sumptuary-law-rank-display.md:2`,
`transport-mobility-lexicon.md:4`, `kinship-terminology.md:3`, `sacred-kingship-mythic-charter.md:3`
("marriage-alliance into the divine line" as one of eight legitimation channels),
`contact-scenario-builder.md:3` ("intermarriage naming effects").

Couplings: **0** `- couples:` lines target a marriage path, so there is no dangling pointer to
inherit. Four `- couples:` lines contain the word *marriage* inside a parenthetical
(`furniture-interior-lexicon.md:14`, `kinship-terminology.md:24`,
`purity-pollution-boundary-systems.md:8`, `ritual-liminality.md:14`) — text, not a path.

Corpus index (`corpus/README.md`) at base — measured against the tree:

```
partition   files  rows  missing_rows  ghost_rows
civilizations      95    95            0          0
culture-material   42    41            1          0   missing: maritime-seafaring-lexicon.md
linguistics        32    30            2          0   missing: conlang-scholarship.amend-2026-10-23.md, conlang-scholarship.md
myth-symbol        34    32            2          0   missing: guest-right-hospitality-law.md, ordeal-judicial-proof-rituals.md
synthesis          29    29            0          0
verification       24    24            0          0
TOTAL             256   251
```

So the index is **5 rows short of the tree before this round** and its section headers read
`32/32/41/29/24/95` = 253, against 256 measured — `myth-symbol/` is one of the two stale headers
(32 declared, 34 on disk).

Insertion point: claim D lands the entry at `corpus/knowledge/myth-symbol/`, and filename order
inside `## myth-symbol/` puts `marriage-alliance-bridewealth.md` **between
`hero-journey-variants.md` and `mineral-stone-symbolism.md`** (README rows 16 and 17 of the
section; `marriage…` < `mineral…` on the third character). The two rows that partition is
missing — `guest-right-hospitality-law.md` (g) and `ordeal-judicial-proof-rituals.md` (o) — are
not adjacent to the insertion point, so the row's position is unambiguous and the pre-existing
backlog does not block it. The landing must not read a pre-existing red index as its own failure.

## 5. Duplicate-document check by DOCUMENT (not URL)

Registry at base: **832 rows, ids `S001`–`S908` (max 908), every row exactly 11 cells**
(`awk -F'|' '/^\| S[0-9]{3} \|/{print NF-2}'` → `832 × 11`, no exceptions). Frozen commit touches
no corpus byte: `corpus/SOURCES.md` is the same blob `38dbef6f…` in both revisions (997645 bytes);
the only additions in `21277b08` are the 13 `reports/round-83/` claim files.

| candidate work | rows found at base | verdict |
|---|---|---|
| **Code of Hammurabi** | **0 rows.** One mention, in a round-50 section note, as a *lead*: "… Kozuh 2014 publisher summary, **Hammurabi (Avalon)**, O'Hare 2025 … — leads, not rows, until a later round cites them." (`corpus/SOURCES.md:910`). Knowledge citations without rows: `trade-economy-lexicon.md:44` ("Hammurabi-style codes"), `pantheon-archetypes.md:43` ("Hammurabi stele"), `mesopotamia-sumer-akkad.md:65` | **unregistered as a WORK**; free to open, and note a prior round named it a lead and left it |
| **EB11 article "Marriage"** | **0 rows.** EB11 (11th edn) articles actually rowed: Chess (S765, vol. 5), Veil (S702), Ship (S900, vol. 25), Ordeal (S903, vol. 20), Guest (S907, vol. 12) — none is "Marriage"; the *online* Britannica entries (S351 dragon, S697 Phrygian cap, S701 Tuareg, S712 Wimple, S717 Fez) are a different edition and a different document class; rejects S747 (mortarboard), S857 (dreadlocks), S858 (Tuareg duplicate) | **unregistered as a WORK**; a new EB11 article is a *new document*, not a duplicate of another article's row |
| **Rigveda, any RV 10.85 row** | **0 rows.** `grep -ic 'Rigveda|Rig Veda|Ṛgveda|RV 10.85'` → 0; the single "Vedic" hit is an Ayurveda paper (S806). The translation the corpus actually cites, Jamison & Brereton (2014), has **0 rows** (`india-vedic.md:18`, `sacred-registers-liturgical-language.md:13`, `binding-speech-complex.md:22`, `religion-language-co-evolution.md:198`) | **unregistered as a WORK**, and the corpus is already citing it without a row — a pre-existing citation-without-row pattern, not something this round created |
| **Leviticus** | **0 rows.** One row cites its content: S853 = Jewish Encyclopedia (1906) "Pe'ot", *teaches* "pe'ot sidelocks and the Leviticus 19:27 prohibition". No Bible edition is rowed anywhere (S839 = BibleHub Numbers 6:5 only) | **unregistered as a WORK**; S853 registers a different document |
| **Homer, *Odyssey*** | **S904** — Gutenberg #1727, Butler; `book` / **A**; `mined`; `used-by corpus/knowledge/myth-symbol/guest-right-hospitality-law.md`; 717782 bytes | **already registered → reuse, do not re-open** |
| **Tacitus, *Germania*** | **S905** — Wikisource Church & Brodribb; `book` / **A**; `mined`; `used-by` the same entry | **already registered → reuse, do not re-open** |

Not one of the six candidates, but it changes what the entry can claim: the registry **already
carries the only committed marriage-institution fact that is grounded on registry rows**, through
heraldry.
`myth-symbol/heraldry-emblems-identity-marks.md:79` records "marshalling on marriage … the wife's
arms are impaled unless she is an heraldic heiress, when they go on an escutcheon of pretence",
grounded on two mined rows — **S560** (Fox-Davies 1909, *A Complete Guide to Heraldry*) and
**S414** (Woodward & Burnett 1892, ch. "Marshalling"). So the corpus has a grounded marriage
*consequence* with rows behind it and no owner of the institution that produces it. The new entry
should cite `:79` as its one in-corpus positive control: marriage demonstrably moves a status mark
between houses, and the mechanism is currently housed in a symbol file.

The registry itself already treats marriage as a *coupling*, not a subject: the evidence-chain
note reads "**Kinship and society grounding — S007 → S005:** read D-PLACE codings … then Kinbank
for the actual term inventories and its worked null-result caution **before asserting any
marriage–terminology coupling**" (`corpus/SOURCES.md:877`). That sentence is the closest the
committed bytes come to naming this surface, and it is a warning about a coupling, not an
ownership claim — which is the strongest single piece of evidence that the institution has no
owner.

Consequence for the four planned rows: the *works* that are free are exactly Hammurabi,
EB11 "Marriage", the Rigveda (10.85) and Leviticus — i.e. the four candidates the round already
names. The two works that carry the round-82 hospitality material stay single-rowed: any marriage
passage in the *Odyssey* (Penelope's remarriage contest, Nausicaa) or in *Germania* (ch. 18–20,
the marriage/dowry chapter) must be cited through S904/S905. Opening a second row for an
already-rowed work is what S858 was rejected for ("live URL already rowed - S701 owns this page").

## 6. Source-availability probe (independent, non-binding)

Plain `GET`, browser-shaped UA, no challenge, no login, no automation. These are probes, not
receipts; `ScribeRows`' receipts bind and their byte counts are the ones the rows must carry.

| page | status | size | note |
|---|---|---|---|
| `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Marriage` | 200 | 147040 B | title `1911 Encyclopædia Britannica/Marriage`; stripped text 61,460 chars |
| `https://en.wikisource.org/wiki/The_Code_of_Hammurabi` | 200 | 71525 B | **TRAP: an index/disambiguation page.** 0 occurrences of `wife`, `husband`, `marriage`, `bride`, `dowry`, `betroth` |
| `https://en.wikisource.org/wiki/The_Code_of_Hammurabi_(Harper_translation)` | 200 | 147981 B | real code text: 114 × "If a man", 44 × wife, 39 × husband, 26 × dowry, 3 × betroth |
| `https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_85` | **404** | — | path does not exist |
| `https://www.sacred-texts.com/hin/rigveda/rv10085.htm` | 200 | 296665 B | title `Rig-Veda, Book 10: HYMN LXXXV. Sūrya's Bridal.`; 22 × bride, 82 × Sūryā, 8 × wedding |
| `https://en.wikisource.org/wiki/Bible_(Jewish_Publication_Society_1917)/Leviticus` | 200 | 528437 B | 14 × wife, 32 × nakedness (Lev 18), **0** × bride/marriage/dowry |

Three traps worth carrying into the landing, all measured:

1. **`sacred-texts.com` is not byte-stable.** Two fetches two seconds apart, same UA, both
   296665 bytes, different sha256 (`1082a3463c3d…` vs `35c52153d710…`). A row that binds a byte
   count to that URL without a fixed capture cannot be re-verified. The page is also
   navigation-heavy — the hymn sits inside site chrome, so a tag-stripper must not read the
   nav as article prose (the same failure class as S907's Parsoid scaffold).
2. **The EB11 "Marriage" article's spine is an evolutionary stage law.** Its opening defines
   marriage, then states: "It is possible to discriminate between three stages … the animal or
   physical stage, the proprietary or legal stage, and the personal or moral stage. In the first
   or physical stage the relation of the sexes was unregulated …". That is the same unilinear
   stage law S908 refused as a framework (QUALITY 2). Whatever row is written here cannot be
   load-bearing *for the stage law*; it can ground a definition and the 1911 survey view.
3. **`The_Code_of_Hammurabi` on Wikisource is an index page, not the code.** 71525 bytes with
   **zero** occurrences of `wife`, `husband`, `marriage`, `bride`, `dowry` or `betroth`; the code
   text is at `The_Code_of_Hammurabi_(Harper_translation)` (147981 B, 114 × "If a man", 26 ×
   "dowry"). A row whose URL is the unqualified title would register a navigation page and quote
   nothing — the same class of defect as S858 rowing a page another row already owns.

Also measured on the same page: 0 × `dowry`, 0 × `bride-price`, 0 × `polygamy`, 0 × `endogamy`,
0 × `exogamy`, 9 × `consanguinity`, 18 × `Roman`, 301 × `marriage`. So the EB11 article is a
**legal-history survey of prohibited degrees and Roman/Christian marriage**, not a bridewealth
survey. The transfer vocabulary has to come from Hammurabi (26 × dowry) and the RV hymn, not
from EB11.

## 7. What the census forces on the landing

1. **Count line:** base is 256 files; the landing is the **257th**, and `## myth-symbol/`
   moves **34 → 35** (the section header currently says 32). The index section headers are
   already stale (253 declared vs 256 measured), so the landing must state its own delta, not
   "the total is 257" as if the index had been consistent.
2. **Gap sentence numbers:** "0 filename owners of 256"; "exact institutional core → 9 files /
   14 lines / 16 matches, every one a passing attribute"; "116 files / 374 lines for the wide
   family"; "0 headings, 0 gap blocks, 0 topic claims own the institution". **Not 27 lines.**
3. **The one borderline line** that must be answered in the entry rather than ignored:
   `pastoralism-animal-husbandry.md:113` already states "stock from groom's kin to bride's kin".
   The new entry owns the institution; that row owns herd distribution and says so. The entry
   must cite it and say which of the two is authoritative for the direction rule.
4. **Reuse, not re-register:** S904 and S905 are `mined` and already `used-by` the guest-right
   entry; a second row for either work repeats S858's rejection.
5. **Four works are free** and each anchors a different face of the institution — a candidate
   split the entry should test, not assume:
   - Hammurabi (Harper) → contract and priced transfer (dowry, estate, the written instrument);
   - EB11 "Marriage" → the 1911 comparative/legal survey, definition + prohibited degrees, with
     the stage law refused;
   - Rigveda 10.85 (Sūrya's Bridal) → the wedding as ritual/alliance transfer, but only from a
     stable capture;
   - Leviticus (JPS 1917) → prohibited degrees / the incest boundary and priestly marriage
     rules, **not** the transfer (0 bride/dowry/marriage in the served text).

6. **Partition tension worth one sentence in the header.** Claim D fixes the entry in
   `myth-symbol/`, but the strongest *transfer* evidence in the corpus sits in
   `culture-material/` (dowry chest, pledge etymology, bridewealth stock row) and
   `linguistics/` (affinal lexicon). The myth-symbol home is justified by the seal/rite/boundary
   side; the entry should say that in one line rather than let the partition look arbitrary.

## 8. Cross-check now available

The landing entry (sibling-written, untracked at
`corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md`) states in its `- gap filled:`
line: "**14 lines in 9 files**" at base `3088bd7f` — the same numbers this census measured
independently. So the outlier is the wave spec's "27 lines", not the entry. No disagreement to
report under R82-M3 for this number; the comparison against `ScribeRows`/`ScoutSources` remains
outstanding (see below).

## 9. What this census does not establish

- It does not compare against `ScribeRows`' or `ScoutSources`' readings: neither had published a
  stage file when this seat ran, so the R82-M3 cross-check is **outstanding**, not passed.
- It does not verify any quote as a *located passage* on a page (that is the rows' job); §6 gives
  page-level byte facts and vocabulary counts only.
- It does not establish that all 374 wide-family lines are passing attributes — it *measures*
  the wide population and *classifies* the exact core (14 lines) and the named owner set; the
  remaining prose bullets are sampled, not exhaustively adjudicated. The defensible claim is:
  "116 files / 374 lines mention the surface; 0 headings, 0 gap blocks and 0 topic lines claim
  it; the ten named files and eight further partial owners are quoted in `owners.md`."
- It does not decide the row split or the entry's section plan; §7 lists what the measured
  evidence supports and what it forbids.
