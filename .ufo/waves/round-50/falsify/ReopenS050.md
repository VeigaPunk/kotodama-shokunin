# ReopenS050 — SOURCES row S050 (Zeder 2008, PNAS, PMC2575338)

Seat: KotodamaR50-2.ReopenS050-21 (leaf falsify). Landed work attacked at
`1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All bytes below read via `git -C <lane> show 1c779e4a:<path>`; the lane working tree was not used as evidence.
No lane file was edited; no git/jj write command was run. Tool installations: **none**.

## Verdict

**PARTIAL** — the URL, the Gate quote and its location, the tier/scope, and every load-bearing
entry claim about Zeder 2008 hold. Two small defects survive:

1. **Row anchor is off by one paragraph.** `corpus/SOURCES.md:79` names
   "§Initial Animal Domestication in the Fertile Crescent, paragraph 3"; the row's own culling
   claim ("culling young males, keeping females") is not in paragraph 3. It is in prose ¶2 and,
   verbatim, ¶4. ¶3 carries only the harvest-profile *method*.
2. **Two ecology clauses inside S050-cited table cells are not in the article**:
   `pastoralism-animal-husbandry.md:59` "grass and reliable water" and `:60` "arid-tolerant small
   stock". The page contains "grass" 0 times, "water" 0 times; "arid" only in two unrelated
   body-size/dispersal sentences.

No entry claim fails; the row's three `teaches` statements are all true of the article.

## What was opened (this session)

| URL | Result |
|---|---|
| https://pmc.ncbi.nlm.nih.gov/articles/PMC2575338/ | **HTTP 200**, 212,318 bytes, final URL = canonical, rendered full text |
| https://doi.org/10.1073/pnas.0801317105 | **HTTP 403**, final `https://pnas.org/doi/full/10.1073/pnas.0801317105` (matches the Gate's "PNAS DOI page 403") |
| https://pubmed.ncbi.nlm.nih.gov/18697943/ | HTTP **203**, 5,590-byte cookie/challenge shell only, no bibliographic content — could not re-confirm the seat's "no erratum" claim from PubMed this session; the PMC page itself has 0 occurrences of `Erratum`/`Correction`/`corrected` |

PMC header confirms the row's bibliography exactly: `Proc Natl Acad Sci U S A. 2008 Aug 12;105(33):11597–11604.
doi: 10.1073/pnas.0801317105`, `PMCID: PMC2575338 PMID: 18697943`.

## Gate quote and location (`corpus/lessons/round-50.md:35`)

Gate text:
> §Initial Animal Domestication in the Fertile Crescent, penultimate paragraph: "with all four major livestock species coming under management over a period from ca. 11,000 to 10,000 B.P."

Parsed the section from the live HTML (`<h2>` through the next `<h2>`):

```
$ python3 … parse /tmp/s050.html
prose paragraphs: 10
1 Until the late 1990s archaeozoologists relied on morphological changes
2 The utility of this size reduction marker, and indeed of all morpholog
3 Although the linkage between domestication and body size was called in
4 Application of this approach to archaeological assemblages from Iraq a
5 Looking back before Ganj Dareh, unusual demographic profiles detected
6 Lower-resolution demographic methods used by archaeozoologists working
7 Recent research has also clarified the spatial and temporal context of
8 Genetic data from modern and archaeological specimens both support and
9 Animal domestication in the Near East can then be seen as arising from
10 As is the case with animal domestication in the Near East, the leading
quote in section text: True
quote count whole page: 1
```

- **Verbatim:** yes — the only difference is the page's italic markup on `ca.`; the words,
  punctuation and `B.P.` match.
- **Location:** correct. The quote is the eleventh `<p>` (ninth prose paragraph of ten), i.e. the
  **penultimate paragraph** of the section. Its full sentence: "Over time hunting strategies aimed
  at maximizing local availability of wild ungulates developed into active management, with all
  four major livestock species coming under management over a period from *ca.* 11,000 to 10,000 B.P."
- **Occurrence count:** 1 on the whole page, so there is no second, differently-located copy that
  could rescue a wrong locator.

## Tier and scope under `corpus/QUALITY.md:29` (criterion 6)

Criterion 6 reserves A for "sources primary or authoritative for the exact scope"; publisher
descriptions and abstracts are B.

- The row is the full peer-reviewed PNAS article, not a blurb or abstract-only record; the seat's
  report (`.ufo/waves/round-50/build/SrcZederDomestication.md:21-29`) records the 403 publisher page
  and the PMC full-text route. **Tier A is honest for the row's declared scope.**
- The scope is claim-scoped exactly as criterion 6 asks: "the 2008 published evidence … not
  post-2008 chronology, not pastoral social forms". The entry complies: `:11` and `:195` both
  instruct re-opening S050/S067 before quoting a domestication date. No entry sentence presents a
  2008 date as current consensus.

## The row's teaches against the article

| Row teaches | Support found | Status |
|---|---|---|
| herd management (culling young males, keeping females) legible before morphological change | ¶2: "Excess males not needed for herd propagation were harvested at young ages"; females "slaughtered after their prime reproductive years". ¶4 verbatim: "(harvesting of young males and prolonged survivorship of females) at the site of Ganj Dareh"; "no evidence of size reduction or any other domestication-induced morphological change". Abstract: "Evidence for herd management and crop cultivation appears at least 1,000 years earlier than the morphological changes…" | holds |
| four species under management c. 11,000–10,000 BP | penultimate ¶, exact sentence quoted in the Gate | holds |
| species order is regional | ¶4 goats at Ganj Dareh; ¶6 "Sheep seem to be the initial early focus … in this region, with managed goats arriving from outside the area at ca. 10,200 B.P."; ¶9 "probably independently of one another and possibly multiple times" | holds (Fig. 1 map itself is not machine-readable; the text alone supports the regional-order reading) |

## Every S050 citation in `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`

| Line | Cited text | Support in Zeder 2008 | Status |
|---|---|---|---|
| 7 | "S050 Zeder 2008 *PNAS* (herd management before morphology)" | accurate summary of Q2 | holds |
| 11 | "re-open S050/S067 before quoting a domestication date (aDNA moves fast)" | matches the row's "not post-2008 chronology" | holds |
| 16 | "herd management is legible archaeologically before any change in the animals' bodies (S050)" | Abstract sentence + ¶4 "no evidence of size reduction or any other domestication-induced morphological change" | holds |
| 20 | "culling keeps females, harvests young males (S050)" | ¶2 and ¶4 | holds |
| 59 | "grass and reliable water; managed in the upper Euphrates c. 11,000–10,000 BP (S050)" | date: ¶7 exact ("upper Eu-phrates Valley between ca. 11,000 and 10,000 B.P."). Ecology: `grass` 0 hits, `water` 0 hits on the page | **date holds; first clause unsupported** |
| 60 | "arid-tolerant small stock; goats first in the Zagros, sheep in SE Anatolia (S050)" / "species order is regional (S050)" | order: ¶4 + ¶6 + ¶9. Ecology: `arid` occurs only in "increasing heat and aridity positively correlated with smaller size" and "hotter and more arid lowland Iran" (goat dispersal); "arid-tolerant" as a trait is not stated | **order holds; first clause unsupported** |
| 87 | "the culling rule decides the herd's shape (S050)" | ¶2/¶4 | holds |
| 184 | "R — S050: management precedes morphological change" | Abstract + ¶4 | holds |
| 195 | "re-open S050 and S067 before quoting a date" | matches row scope | holds |

## Defects and smallest fixes

**D1 — row anchor paragraph number (`corpus/SOURCES.md:79`, anchor cell).**
The row names "paragraph 3". In the landed PMC HTML the section's prose paragraphs begin:
¶1 "Until the late 1990s…", ¶2 "The utility of this size reduction marker…",
¶3 "Although the linkage between domestication and body size…", ¶4 "Application of this
approach to archaeological assemblages from Iraq and Iran…". The culling rule the row teaches
is in ¶2 and, verbatim, ¶4; ¶3 contains only the method ("harvest profiles … capable of
distinguishing the prey strategies of hunters from the harvest strategies of herders").
The misnumbering entered at the build seat, whose report says
`.ufo/waves/round-50/build/SrcZederDomestication.md:42`: "**third paragraph** (begins
'Application of this approach…')" — that paragraph is the fourth.
*Smallest fix:* change the anchor to `paragraphs 2–4 and penultimate paragraph`, or name the
paragraphs by opening words (as the seat's own row draft at `SrcZederDomestication.md:21` did:
paragraph beginning "Animal domestication in the Near East can then be seen…").

**D2 — unsupported ecology descriptors inside S050-cited cells
(`pastoralism-animal-husbandry.md:59,:60`).**
`grass and reliable water` and `arid-tolerant small stock` are stock-keeping commonplaces, not
Zeder 2008 content (page counts: `grass` 0, `water` 0; `arid` only as a body-size confounder
and as the lowland-Iran destination of managed goats). They sit in cells whose trailing
`(S050)` reads as covering the whole cell, which is scope creep against the row's own
"when and how … came under management" scope. Not contradicted by the article; not attributed
to it by name.
*Smallest fix:* drop both descriptors (nothing depends on them), or move the citation so it
scopes only the dated clause, e.g. "managed in the upper Euphrates c. 11,000–10,000 BP (S050);
grass and water follow the herd" without implying Zeder.

## Registry resolution

Private shared clone at the landed commit (`GIT_CEILING_DIRECTORIES=/tmp`, deleted after use),
running the manifest's own C acceptance body:

```
C_SID_UNRESOLVED 0 []
S050 used-by: corpus/knowledge/culture-material/pastoralism-animal-husbandry.md
S050 pipe fields: 13
```

So S050 resolves, its `used-by` names the entry, and the row parses to the expected 12 columns.

## Limitations

- PubMed did not serve the record (HTTP 203 cookie shell), so "no erratum" is confirmed only by
  the absence of any correction notice on the PMC full text, not by the MEDLINE record.
- Fig. 1 is a raster map; only its caption was read. The "goats first in the Zagros" cell is
  supported by the text (Ganj Dareh managed goats; sheep as the initial SE Anatolia focus), not
  by machine-read figure content.
- No post-2008 synthesis was opened; the row explicitly does not claim currency, and the entry
  carries the recheck instruction.
