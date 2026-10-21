# Round 50 falsify — C coverage: `corpus/SOURCES.md` conformance

Seat: `KotodamaR50-2.ReviewSourcesConformance-21` (reviewer, non-author, read-only attack seat).
Item attacked: **C coverage** of the landed build wave at `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`
(base `4ad2683…`) — the SOURCES registry rows S048–S069, their tier/scope honesty, the round-50
search-log note, and the SOURCES preamble pointer change, checked against the frozen contract
`/home/vgpnk/Projects/shokunin/CORPUS.md` §"SOURCES.md — where a shokunin learns"
(`SOURCES-CONTRACT-v1`, kaika 2026-10-19) and `corpus/QUALITY.md` criterion 6.

All landed bytes were read with `git -C … show 1c779e4a…:<path>`; all measurements were re-run in
this session against the landed tree (private clone `/tmp/kotodama-revsrc-*`, deleted at sweep) and
against live publisher URLs. Working-tree drift is flagged explicitly wherever it matters
(the lane working tree already carries uncommitted falsify-wave edits: S070 row, `S048–S070`
pointer, a new lesson section).

---

## VERDICT: **PARTIAL**

The registry's *shape* and *mechanics* hold — every row is legal, the census is clean, tier
inflation did not recur, the Gate carries all 22 rows, and the preamble pointer change is legal,
logged and factually corrective. Five defects are real and checkable; two of them (S060's
bibliography and its "emic" claim) are still wrong in the landed SOURCES row itself, and three are
locator/negative-claim defects that make a re-opener unable to reproduce a quoted passage from the
route the registry records.

Severity order: F1/F2 (landed registry asserts wrong facts) · F3 (false durable negative claim) ·
F4/F6 (anchor arithmetic off by one) · F5 (rule-5 note incompleteness + unlocatable exclusions) ·
F7/F8 (unreproducible quote routes).

---

## F1 — HIGH · S060's published page range is wrong in the landed row

`corpus/SOURCES.md:89` (landed), cell `source`:

> `Ahearn 2018, … Natural Hazards 92(Suppl 1):95–107, doi 10.1007/s11069-017-3128-4`

Publisher-deposited metadata for that exact DOI says otherwise:

```
$ curl -s "https://api.crossref.org/works/10.1007/s11069-017-3128-4" | python3 -c "…"
title: ['Herders and hazards: covariate dzud risk and the cost of risk management strategies in a Mongolian subdistrict']
container: ['Natural Hazards']
volume: 92 issue: S1 page: 165-181
issued: {'date-parts': [[2017, 12, 13]]}
```

The PDF I re-fetched (`https://d-nb.info/1152169939/34`, HTTP 200, 979,718 B, 18 text pages) carries
neither `95–107` nor `165–181` in its text layer — it is the accepted-manuscript layout
(running head `Nat Hazards`, no final pagination), so the registry's page range is not sourced from
the document it cites either. A reader following "92(Suppl 1):95–107" lands on the wrong pages of
the wrong issue.

**Smallest fix:** the registry row is append-only, so this must be a new superseding row
(`teaches` opening `supersedes S060 —`). The falsify wave already drafted exactly that as **S070**
in the working tree (`corpus/SOURCES.md:99`, `message.page` = `165-181`, volume 92, issue S1) —
it needs landing, not rewriting. Until S070 lands, the landed row is factually wrong.

## F2 — HIGH · S060's `teaches` upgrades a statistical aggregate to an "emic portfolio term"

`corpus/SOURCES.md:89`, cell `teaches`:

> `the five snouts as an emic portfolio term; reliability-seeking risk management; covariate dzud risk limits risk sharing`

The row's own `scope` cell says the opposite: *"…and the five-snouts aggregate **as reported from the
National Statistical Yearbook 2013**"*. The source text (PDF p. 4, verified verbatim this session):

> `In Bayankhongor, the total herd count for 2012 was 2,640,831 head of livestock, which is an
> aggregate of the "five snouts" represented by horses, yaks/cattle, camel, goats and sheep`

That is a national statistical yearbook aggregate presented by the author; nothing in the source
presents "five snouts" as an attested herder-side (emic) term. `teaches` therefore overstates what
the cited scope licenses — the same claim-strength inflation QUALITY criterion 6 and
`CORPUS.md` rule 1 ("a ≤25-word quote … grounding `teaches`") exist to prevent.

Note the inconsistency **inside the landed tree**: the uncommitted C-entry repair already dropped
"emic" for S060 (worktree `corpus/lessons/round-50.md`, falsify-wave section), while the landed
`corpus/SOURCES.md` row still asserts it. Registry and entry disagree at HEAD.

**Smallest fix:** land S070, whose `teaches` already states the corrected reading
("S060's quoted aggregate supports 'five snouts' as a reported herd aggregate, not an attested emic
term"). No in-place edit is lawful.

## F3 — MEDIUM · S052 records a false, unfalsifiable-by-sweep negative claim

`corpus/SOURCES.md:81`, cell `source`:

> `… (Internet Archive-digitized scan; **archive.org itself unreachable 2026-10-21**)`

and `corpus/lessons/round-50.md:37` (landed Gate bullet): `Seat: SrcEvansPritchard (archive.org
unreachable; …)`. Re-probed **the same day** (2026-10-21) from this host:

```
https://archive.org/details/nuer0000eeev          -> 200  (210629 B) "The Nuer : E.E. Evans-Pritchard : Free Download, Borrow, and Streaming : Internet Archive"
https://archive.org/details/nuerdescriptiono00evan -> 200  (219588 B) "The Nuer : a description of the modes of livelihood and political institutions of a Nilotic people : Evans-Pritchard, E."
https://web.archive.org/details/nuer0000eeev       -> 200  (154579 B)
```

archive.org's item pages are reachable; what is restricted is the borrow-gated full text
(`_djvu.txt` → HTTP 401). The registry asserts a broader falsehood ("archive.org itself
unreachable") and CORPUS.md requires that **"a negative claim carries its sweep"** — no sweep,
command or status code is recorded for this one, and it is contradicted on the day it is written.

**Smallest fix:** superseding row for S052 recording what is actually true — item page reachable
(IA item `nuerdescriptiono00evan`, whose live title matches the cited book), full text
borrow-restricted (401) — and pointing the anchor at the IA item rather than the Duke course mirror.

## F4 — MEDIUM · S052's anchor conversion formula is wrong for the very pages it cites

`corpus/SOURCES.md:81`, cell `anchor`:

> `Ch. I §I pp. 18–19; §VIII pp. 41–46 (printed page = PDF page − 24)`

Measured on the cited PDF (`https://people.duke.edu/~ldbaker/classes/gradtheory/Evans_Pritchard_E_E_The_Nuer_a_description_of_the_modes_1940.pdf`),
mapping each PDF page's printed folio via `pdftotext` page heads:

```
pdf 44 -> printed 20   (offset 24)
pdf 45 -> printed 21   (offset 24)
pdf 46 -> printed 22   (offset 24)
pdf 47 -> PLATE III           <-- inserted leaf
pdf 68 -> printed 38   (offset 30)
pdf 70 -> printed 40   (offset 30)
pdf 71 -> printed 41   (offset 30)
pdf 74 -> printed 44   (offset 30)
pdf 75 -> printed 45   (offset 30)
pdf 76 -> printed 46   (offset 30)
```

Offset −24 holds only for the §I range; from the inserted plates on it is −30 — and §VIII
pp. 41–46 (PDF 71–76) is exactly the −30 region. Applying the anchor's own formula to §VIII
sends the reader to PDF 65–70 (printed 35–40), i.e. the wrong text. (The falsify wave logged the
same defect as a carried erratum, `ReopenS052`; my measurement independently confirms it and pins
the break point at PDF 47.)

**Smallest fix:** superseding row: "PDF pp. 42–46 = printed 18–22 (offset −24); PDF pp. 71–76 =
printed 41–46 (offset −30, after PLATE III)". The §VIII range itself is right; only the formula is wrong.

## F5 — MEDIUM · the round-50 search-log note is incomplete under rule 5, and its exclusions are unlocatable

`corpus/SOURCES.md:142` (landed), the round-50 note. Contract rule 5 requires
*"question/query, where searched, date, identified / screened / included / excluded counts,
exclusion reasons, stop rationale."* The note supplies question, where-searched, date, an included
count ("Included 22 rows (A 16, B 6)") and two exclusion lists — but **no identified count, no
screened count, no excluded count and no stop rationale**. The three older notes in the same file
all carry them, e.g. `corpus/SOURCES.md:136` (`Identified 15, screened 15, included 15 rows …,
excluded 0, rejected 0`) and `:138` (`Identified 14 (…), Screened 13 by opening, Included 12 …`,
`Stop rationale: …`). The round-50 note is measurably weaker than its own predecessors.

Two further defects in the same note:

* The exclusion list says "Opened but not registered" and then enumerates 16 distinct sources,
  but the sentence contains 17 comma-separated fragments — the first item, `Dyson-Hudson 1980
  (identity only, no abstract)`, is split by its own parenthetical comma. A count-taking reader
  (or the census prose) sees 17; there are 16.
* Of those 16, **13 carry no URL at all** (`Dyson-Hudson 1980`, `Herskovits 1926`,
  `Galaty & Johnson 1990`, `Khazanov 1994 publisher page`, `Barfield 1993 abstract record`,
  `FAO newsroom story and Knowledge Hub pages`, `Sametinget companion pages and statutes`,
  `Morello & Rizk 2022`, `Ostrom 1990 publisher record`, `Marett 1940 review`,
  `Goody & Tambiah via HRAF`, `Kozuh 2014 publisher summary`, `Hammurabi (Avalon)`) and the rest
  name a work without a route. A later round cannot re-open them.
* They also do not belong where they were put. Contract Shape reserves `## Leads (unopened)` for
  unopened leads and says "a lead is not evidence and never a row"; these were *opened*, and they
  are not in `## Leads` either (the landed `## Leads` section, `corpus/SOURCES.md:144+`, still
  ends with the hunting-foraging round). Under the contract's status vocabulary an opened,
  worth-mining source is a `queued` **row**.

**Smallest fix:** (a) extend the round-50 note with `Identified N / Screened N / Excluded N` and a
one-line stop rationale, fixing the fragment count to 16; (b) register the opened-but-unregistered
items as `queued` rows (status `queued`, `used-by` `—`) with their URLs, or move them to
`## Leads` with locators; (c) amend the lesson's Frontier line that points at the search log
instead of the registry.

## F6 — MEDIUM · S050's anchor points one paragraph off the herd-management passage

`corpus/SOURCES.md:79`, cell `anchor`:

> `Abstract; §Initial Animal Domestication in the Fertile Crescent, paragraph 3 and penultimate paragraph`

Re-parsed the PMC full text (`https://pmc.ncbi.nlm.nih.gov/articles/PMC2575338/`, HTTP 200,
212,318 B) by heading boundaries. The section's prose paragraphs are:

```
sec¶1 Until the late 1990s archeozoologists relied on morphological changes …
sec¶2 The utility of this size reduction marker … attributed to differences in the culling strategies of herders …
sec¶3 Although the linkage between domestication and body size was called into question …
sec¶4 Application of this approach … has identified the clear signature of a managed herd of goats (harvesting of young males and prolonged survivorship of females) …
sec¶5 … unusual demographic profiles …
sec¶6 Lower-resolution demographic methods …
sec¶7 (Fig. 1 caption) sec¶8 … sec¶9 … sec¶10 Animal domestication in the Near East can then be seen as arising … with all four major livestock species coming under management over a period from ca. 11,000 to 10,000 B.P. …
sec¶11 As is the case with animal domestication in the Near East …
```

The four-species quote is in sec¶10 of 11 → the "penultimate paragraph" locator is **correct** (the
Gate bullet's own quote and locator check out). But the herd-management claim lives in **sec¶2**
("culling strategies of herders") and **sec¶4** ("harvesting of young males and prolonged
survivorship of females"); "paragraph 3" matches neither under any consistent counting (the
falsify wave's `ReopenS050` reached ¶4 by the same route). Also present and supporting
`teaches`: "Different species seem to have been domesticated in different parts of the Fertile
Crescent" (global ¶8) — i.e. "species order is regional" is supported, but by ¶8, not by the cited
¶3.

**Smallest fix:** superseding row for S050 with the anchor "§Initial Animal Domestication in the
Fertile Crescent ¶2 and ¶4 (and the penultimate paragraph)".

## F7 — LOW-MEDIUM · S051's Gate locator is wrong, and its route no longer serves the text

`corpus/lessons/round-50.md:36` (landed Gate bullet) and `corpus/SOURCES.md:80`:

> Gate: `Abstract, opening sentence: "a more diversified exploitation of secondary applications and products such as milk, wool, textiles, and traction"`

The publisher abstract (OpenAlex inverted index for the same DOI) reads:

> `Andrew Sherratt is perhaps best known for the concept of a 'Secondary Products Revolution',
> which stressed that the 'primary' pattern of exploiting domesticated animals for meat in the
> Early Neolithic was followed by a more diversified exploitation of secondary applications and
> products such as milk, wool, textiles, and traction.`

The quoted fragment is in the **second** sentence and is not a whole sentence; "opening sentence" is
false. Separately, the URL the row records now yields no text to a plain fetch:

```
https://link.springer.com/article/10.1007/s10963-011-9045-7 -> code=200 size=3038  (bot wall; abstract not in body)
```

The row records no fallback route, so the quote is not reproducible from the registry as written
(unlike S062/S064, which do record their capture). The `teaches` clause "not tied to one century or
millennium" is **UNEVALUATED by me** — it would come from Discussion/Conclusions ¶1, which I could
not open (publisher wall).

**Smallest fix:** superseding row: anchor "Abstract, second sentence", and record the abstract route
actually used (OpenAlex/Crossref mirror) alongside the DOI.

## F8 — LOW-MEDIUM · S053's row records only a route that is now a challenge wall

`corpus/SOURCES.md:82` and Gate bullet `corpus/lessons/round-50.md:38`. Live:

```
https://journals.openedition.org/tc/14002 -> code=200 size=5217
  body contains "Anubis could not load its JavaScript" / challenge JSON; no article text
```

The Gate quote **is** verbatim at the recorded location — I fetched the Wayback capture
`20250120100330` (HTTP 200, 209,807 B) and matched it byte-for-byte in context:

> `… Plan Imitation, identification, équivalence … Texte intégral PDF Partager par e-mail
> L'omniprésence des bovins dans les pratiques et les discours des populations nilotiques d'Afrique
> de l'Est fut à l'origine de l'expression cattle complex (Herskovits 1926). …`

so "Texte intégral, opening paragraph" is accurate. But the row's `source` cell records only the
live (walled) URL and, unlike S062/S064, no capture route — a re-opener following SOURCES gets a
challenge page and no quote.

**Smallest fix:** superseding row adding the capture route `web.archive.org/web/20250120100330/…`
(same shape as S062's recorded captures and S064's).

---

## What HOLDS (checked, no finding)

* **Census — 7 commands on the landed tree** (private clone at `1c779e4a`): rows **69**; malformed
  rows **0**; tier histogram `A=50 B=12 C=7`; status histogram `mined=42 queued=22 rejected=5`;
  duplicate ids **none**; enum/tier-inflation violations **none**; mined rows whose `used-by` path
  does not exist **none**. The maintained parser agrees:
  `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → `kotodama ok`,
  exit **0** (run against the live lane tree, which by then also contains the uncommitted S070 row).
* **Legality of S048–S069 (kind / tier / status / used-by):** all 22 rows use enum kinds
  (`docs|paper|book|dataset`), tiers A/B, `status = mined`, `opened = 2026-10-21`, `recheck = 365d`,
  and `used-by = corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (file exists).
  No `|` inside any cell; NF=13 for all. Every one of S048…S069 is actually cited in that entry
  (checked: no missing id).
* **Tier inflation did NOT recur (QUALITY criterion 6):** no A row is a publisher description.
  The r49 failure mode (S034/S038/S039 publisher descriptions at A) is absent — the description-class
  rows are correctly demoted: S051 review **B**, S057 Routledge description **B**, S061 FAO book **B**,
  S065 dictionary **B**, S048/S049 FAO institutional synthesis **B**; the A rows are primary sources
  (Zeder PNAS, Hardin *Science*, Ostrom Nobel lecture, Khazanov, Evans-Pritchard 1940, Ahearn,
  Nature 2021, D-PLACE variable page, Sametinget register, UNESCO inscription/decision records).
  Borderline but defensible: S064 (ETCSL, tier A, kind `dataset`) is A for "the composition's own
  wording" — an English translation; acceptable only because the scope says so explicitly.
* **Gate completeness (rule 1):** exactly 22 bullets for S048–S069, one per row, each with URL +
  access date + location + seat; every quote ≤25 words (max 25 at S055 and S068) — verified by
  parsing all 22.
* **Preamble pointer change HOLDS.** Landed `corpus/SOURCES.md:8` now reads
  `` `lessons/round-49.md` for S001–S047, `lessons/round-50.md` for S048–S069 `` (previously
  `S001–S043`). It is legal (prose outside the frozen contract section and outside the registry
  table), it is logged old→new in `corpus/lessons/round-50.md:63–65`, and it is **factually
  corrective**: `corpus/lessons/round-49.md:79–82` really do carry Gate bullets for S044–S047, so the
  old pointer was stale. The later working-tree change to `S048–S070` (S070 added) keeps the same
  property.
* **Search-log counts that are present are honest:** "22 build-wave source seats plus 13 section
  scribes" matches `.ufo/waves/round-50/build-assignments.json` exactly (22 `Src*` seats, 13
  `ScribeSec*` seats, 16 `Scribe*` total); "Included 22 rows (A 16, B 6)" matches the S048–S069
  tier histogram I recomputed from the landed file (A=16, B=6).
* **Spot re-opens that succeeded this session:** FAO S048 quote ("there is little or no impetus to
  herd animals") verbatim in `y2647e02.htm` §Classifying pastoral systems; FAO S049 quote ("Tenure is
  thus divided by both ecology and the potential for agriculture") verbatim in `y2647e08.htm`;
  FAO S048 "two to four species" — FAO's own scoping is *"in Mongolia and the northern Sudan"*; FAO's
  stage-ladder wording is *"may have seemed reasonable … a more complex story … In most parts of the
  world, Africa excepted, agriculture seems to have started earlier than pastoralism"*; Zeder S050
  four-species quote verbatim in the penultimate section paragraph; Hardin S054 quote verbatim in
  the MIT PDF (`Picture a pasture open to all`, PDF p. 3 of the two-column scan; the section heading
  prints as `Tragedy of Freedom`); Nuer S052 colour-naming sentence verbatim on PDF p. 71;
  Eczet S053 French quote verbatim in the 20250120100330 capture; Ahearn S060 "five snouts" sentence
  verbatim on PDF p. 4.

---

## Residual risk / verification gaps

* **Not independently re-verified by me** (no route or no budget): S055 Ostrom lecture p. 15;
  S056 Khazanov PDF pp. 1–3; S057 Routledge description; S058 FAO `y5115e08` chapter; S059 Sametinget
  page (claimed verbatim Swedish + "Senast uppdaterad: 13 december 2024"); S061 FAO *The Yak* ch. 8
  ¶1 and ch. 10 ("butter", "faeces"); S064 ETCSL lines 130–142 / 180–191 (quote presence verified
  earlier in this session via Wayback capture 20260605210113; the "third speech" ordinal — which the
  wave's `ReopenS064` disputes — is **UNEVALUATED by me**); S065 AHD headword; S066 D-PLACE
  Description + Values table; S067 Nature abstract; S068 PMC8214430 Introduction ¶1; S069 UNESCO
  decision sentence 4 and element 01964.
* **C-entry side:** the landed `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`
  was not audited here (other seats own it). Note only that the **landed entry and the landed
  SOURCES row disagree on S060's "emic" reading** (F2) and on S048's two-to-four-species scope
  (FAO scopes it to Mongolia and the northern Sudan); the entry was repaired in the working tree,
  the SOURCES row was not.
* **Working-tree state:** the lane working tree already contains uncommitted falsify-wave edits
  (S070 row, `S048–S070` pointer, lesson additions, `reports/round-50/validation.json`). Findings
  F1–F8 are stated against the **landed** bytes at `1c779e4a`; where the working tree already
  carries the repair (S070 for F1/F2) the report says so explicitly — the remaining work is to
  **land** it, and to add the F3–F8 superseding rows.

## Smallest aggregate fix list (author lane)

1. Land **S070** (already drafted) → fixes F1 + F2.
2. Add superseding rows for **S052** (F3 + F4 in one row), **S050** (F6), **S051** (F7),
   **S053** (F8).
3. Extend the round-50 search-log note with identified/screened/excluded counts + stop rationale,
   correct 17→16, and register or locate the 16 opened-but-unregistered sources (F5).

## Tooling

No installs were performed in this seat. Everything used was already present on the host:
`git`, `curl`, `python3` (stdlib only), `pdftotext` (poppler), `grep`/`awk`/`sed` for text
extraction, plus the repo's own `scripts/sources-census.sh`. No credentials, no live-process
probing, no writes outside this report path. Temporary artefacts (`/tmp/kotodama-revsrc-*` clone,
downloaded PDFs/HTML) were deleted at sweep.

*Author-lane advice, not admission. Verdict is advisory; the author lane decides and lands.*
