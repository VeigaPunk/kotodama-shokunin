# ReviewDKongoC59 — claim D falsify: kongo fixes 110, 140, 141, 146 and the speech remap (S570–S574)

Seat: `KotodamaR59.ReviewDKongoC59` (reviewer, leaf, no delegation). Session 2026-10-23 UTC. Every source re-opened this session by ordinary means only: plain `curl` GETs, `pdftotext` (poppler 26.08.0), `soffice --headless` (LibreOffice 26.8.1.1) for the .doc, and the frozen locator `reports/round-59/reopen-quote.py`. No challenge, captcha, login or paywall met. Downloads and working files: `/fast/scratch/hyaku/kotodama-r59/ReviewDKongoC59/`. Recommendation only: I wrote no file but this report.

State reviewed: the working tree, where the fixes have already been applied (by ExecDApply59). Each of the four assigned `new` strings occurs once in `corpus/knowledge/civilizations/kongo-kingdom.md` and no `old` string remains. `speech-surrogates-whistled-drummed.md` carries S570/S571/S572/S573/S574 at 16/2/3/2/4 and zero S135/S141/S147/S151/S159.

## Verdict summary

| fix | verdict | old text right? | note |
|---|---|---|---|
| 110 | **agree** | no (p. 489 is wrong) | the three-officials and clearance clause is wholly on p. 490 |
| 140 | **agree**, with one residual | no (p. 469 and p. 489 are both wrong) | the "no slave trade" wish starts on p. 470 and ends on p. 471; best locator is `pp. 470–471` |
| 141 | **agree**, with one wording nit | substance yes, but lossy | "older" glosses the abstract's "has generally been"; the rest is verbatim or a close paraphrase |
| 146 | **agree** | **yes**: p. 469 was already a page of doc. 142 | for "the letters exist", any page of doc. 142 (pp. 468–471) supports it; the new text is equally right, not more right |
| speech remap | rows carry the passages for 6 of 6 sampled sites, plus 1 extra site | — | **one carried-over overread at entry :106** (S574), and one loose paraphrase at :78 (S570) |

Nothing here blocks ACCEPT-D-59. The KONGO and SPEECH legs require byte equality with the frozen substitutions, so the refinements below are for round 60 and must not be landed this round.

## S359 page map (applies to fixes 110, 140, 146)

The Brásio OCR file (`…/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt`, HTTP 200, 896,693 B, text/plain) prints each page number as a **footer**. Doc. 142 starts on p. 468 and doc. 143 on p. 472, which matches the volume's index (`mma1.txt:1324` "6 de Julho dc 1526 468", `:1328` "9 de Julho dc 1526 . 472", `:1344` "18 de Outubro de 1526 488"). Only the footer reading fits that index.

I confirmed this independently with the item's per-leaf files. In `_djvu.xml` (HTTP 200, 8,938,662 B, 641 OBJECTs), aligned to `_scandata.xml` (641 leaves, all in the access formats), the printed page equals leaf − 61 throughout: leaf 530 ends "4 *9", leaf 531 ends "* 7 °", leaf 536 ends "475" and leaf 551 ends "49°". Phrase → leaf → page:

| phrase | leaf | printed page |
|---|---|---|
| "CARTA DO REI DO CONGO" (doc. 142 heading, 6‑7‑1526) | 529 | 468 |
| "Raynha dona Lyanor nossa Yrmáa era falecyda" | 530 | 469 |
| "mercadores leuam cada dia nossos naturaes" / "nossa vontade hé que nestes Reynos nam aja" | 531 | 470 |
| "trato de esprauos nem sayda pera elles" … date, signature "EIRey … dom A.°" | 532 | 471 |
| doc. 147 heading (18‑10‑1526) | 549 | 488 |
| "furtam muitos dos nossos naturaees forros e jsemtos" | 550 | 489 |
| "a tres fidallgos e ofiçiaes de nossa Corte" … "as poderam leuar e embarquar" | 551 | 490 |

### Fix 110 — agree

New: `S359 (doc. 147, p. 490)`. Served sentence (OCR, leaf 551 = p. 490, `mma1.txt:20285-20295`):

> E por evitarmos tam grande mall, possemos por Iey que todo [o] home bramco que em nossos reynos esteuer e conprara peças per qualquer maneyra que seja, que primeiro ho faça saber a tres fidallgos e ofiçiaes de nossa Corte, … pera veré as ditas peças, se sam catiuos, se forros; e semdo per elles despachados, ao diate nam terá nenhuüa duuyda nem embargo e as poderam leuar e embarquar.

```
LOCATED https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt
```
(quote: `se sam catiuos, se forros e semdo per elles despachados ao diate nam terá nenhuüa duuyda nem embargo e as poderam leuar e embarquar`, the frozen support quote)

"Police who may be enslaved and exported, not abolition" is a faithful reading. The old p. 489 holds the complaint that subjects are stolen and sold ("furtam muitos dos nossos naturaees forros e jsemtos … os leuam a vender aos homés brãcos"), not the policing measure.

### Fix 140 — agree; residual: the wish spans pp. 470–471

New: `… no slave trade (S359, doc. 142, p. 470), but his October 1526 letter sends each sale to three court officials who judge captive or free and lets cleared captives be shipped (S359, doc. 147, p. 490)`.

- Second half: as fix 110, faithful. "Each sale" corresponds to "todo home bramco … conprara peças per qualquer maneyra que seja"; "judge captive or free" to "se sam catiuos, se forros"; "cleared … shipped" to "semdo per elles despachados … as poderam leuar e embarquar". October 1526 matches "esprita aos xbiij dia de oytobro … de j b°xxbj annos" (`mma1.txt:20321`). LOCATED (receipt above, and `primeiro ho faça saber a tres fidallgos e ofiçiaes de nossa Corte` → `LOCATED …_djvu.txt`).
- First half, served text (leaf 531 → 532):

> … porque nossa vontade hé que nestes Reynos nam aja *[p. 470 ends; footnotes 12–16; footer "* 7 °"]* trato de esprauos nem sayda pera elles, pollos respeitos sobreditos

  "Wish … no slave trade" is a faithful reading of "nossa vontade hé que … nam aja trato de esprauos nem sayda pera elles". July 1526 matches "escryta aos bj djas de yulho … de jb°xxbj annos" (p. 471). The new p. 470 is correct where the sentence starts, and p. 469 (Queen Leonor's death) was wrong. However, the words that name the slave trade, "trato de esprauos", are printed on **p. 471**. The instrument shows the break: the whole clause does not locate as one string because the page break and footnotes sit inside it.

```
NOT_LOCATED https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt quote-absent
```
(quote: `porque nossa vontade hé que nestes Reynos nam aja trato de esprauos nem sayda pera elles`.) The frozen support quote for this fix locates on p. 470:
```
LOCATED https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt
```
(quote: `os ditos mercadores leuam cada dia nossos naturaes, filhos da terra e filhos de nossos fidallgos e vassallos`)

  **Round-60 refinement:** `(S359, doc. 142, pp. 470–471)`. ReviewDKongoA59 reached the same split on its own (its report, lines 28 and 33). Do not change it this round, because the KONGO leg is byte-exact.

### Fix 141 — agree; wording nit "older"

New: `Thornton names the older scholarly opinion that the conversion was 'superficial, diplomatically oriented, impure' and argues instead that Christianity in Kongo took a distinctly African form, widely accepted in Kongo and Europe as being the religion of the country (S383, Extract, para. 1).`

Both captures were re-opened with `curl`. Capture 20260203111247 (HTTP 200, 1,158,754 B) and the id_ capture 20240909103530 (HTTP 200, 499,103 B) serve the same Extract. It sits in `<div class="abstract">` as **two** `<p>`; paragraph 1 is exactly these two sentences:

> Scholarly opinion on the conversion of the Kingdom of Kongo to Christianity has generally been that it was superficial, diplomatically oriented, impure, dangerous to national sovereignty or rejected by the mass of the population. This article argues that although Christianity in Kongo took a distinctly African form it was widely accepted both in Kongo and in Europe as being the religion of the country.

Locator receipts this session:
```
LOCATED https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693
```
(quote: `has generally been that it was superficial, diplomatically oriented, impure, dangerous to national sovereignty`)
```
LOCATED https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693
LOCATED https://web.archive.org/web/20240909103530id_/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693
```
(quote: `This article argues that although Christianity in Kongo took a distinctly African form`)

The frozen support quote `was widely accepted both in Kongo and in Europe as being the religion of the country` is verbatim in both `curl` copies, and the instrument located it once on each capture:
```
LOCATED https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693
LOCATED https://web.archive.org/web/20240909103530id_/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693
```
Its other 8 attempts ended in transient fetch errors (`NOT_LOCATED … URLError` ×6, `NOT_LOCATED … HTTPError` ×2), never `quote-absent`. A first attempt with the 25-word "Scholarly opinion on the conversion of the Kingdom of Kongo …" quote returned `url-reflects-quote`, as expected, because "of the kingdom of kongo" is in the URL slug.

Reading: "names the scholarly opinion … argues instead … distinctly African form, widely accepted in Kongo and Europe as being the religion of the country" is faithful, and `para. 1` is exact. The single-quoted span is a verbatim prefix of a five-item list; dropping "dangerous to national sovereignty or rejected by the mass of the population" without an ellipsis is acceptable under the entry's practice and does not change the sense. **Nit (no overread of substance):** "older" is the seat's gloss. The page says the opinion "has generally been", meaning the prevailing view as of 1984, not an older or superseded one. A literal round-60 wording would be "the prevailing scholarly opinion". The old text ("Thornton argues an African church accepted as the country's religion") was right in substance but dropped the opinion Thornton argues against, which is the point of the "thin veneer" myth line. The fix is a real improvement.

### Fix 146 — agree; the old text was already right

New: `(S374, title page; S359, doc. 142, p. 470)`, supporting "the 1526 royal letters exist".

Doc. 142 runs pp. 468–471 (map above), and any page of it shows the letter exists. The strongest single page for existence is p. 471, which carries the date line and the royal signature ("desta nosa cydade de Cõgo, escryta aos bj djas de yulho, dom Joham Teyxeira o fez, de jb°xxbj annos / / a) EIRey i* dom A.°"; `desta nosa cydade de Cõgo, escryta aos bj djas de yulho` → `LOCATED …_djvu.txt`). **The old p. 469 was a page of the same letter and was not wrong for this sentence.** The change is a consistency edit (it aligns with lines 18 and 140), not a correction. Harmless: agree. If it is ever revisited, `doc. 142, pp. 468–471` is the exact span.

## Speech remap — sample of re-pointed sentences (S570–S574 vs the entry as landed)

S570–S574 were each re-fetched: S570 PDF HTTP 200, 1,439,365 B, 10 pages; S571 PDF HTTP 200, 233,242 B, 17 pages; S572 PDF HTTP 200, 337,860 B, 4 pages; S573 HTML HTTP 200, 29,619 B; S574 .doc HTTP 200, 236,544 B, sha256 `85b777c9…d2b7`, the same hash round 58 recorded. Page numbers below are PDF pages from `pdftotext` form feeds.

| # | entry line (as landed) | row | served sentence | locator | verdict |
|---|---|---|---|---|---|
| 1 | :54 Hmong "seven to eight contour tones", Suruí "two level tones", low load → "more formulaic and therefore more predictable" (S570) | S570 p. 7 | "this informational load is much higher in Hmong (seven to eight contour tones, depending on the dialect) than in Suruí (two level tones). For this reason, in tonal languages with low informational load on spoken pitch, whistled sentences are more formulaic and therefore more predictable" | `LOCATED http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf` (both quotes) | **supported** |
| 2 | :79 Chinantec: rich tonal system holds intelligibility in unpredictable sentences; whistled sentences "simple, single-clause utterances, with equally simple conversational repairs" (S570) | S570 p. 7 | "high levels of intelligibility can be reached in unpredictable sentences in tonal languages with rich tonal systems for lexical load, such as Chinantec"; "in both tonal and tonal languages whistled sentences tend to be simple with single-clause utterances and equally simple conversational repairs (Díaz Reyes, 2008; Sicoli, 2016)" | `LOCATED …Encyclopedy.pdf` (both quotes) | **supported**. The single-clause point is stated for whistled languages in general (the page's "tonal and tonal" is a misprint, from context meaning tonal and non-tonal); applying it to Chinantec is within that scope, and Sicoli 2016 is the Chinantec study. |
| 3 | :58 "On the Hmong qeej the tones and the vowels are reproducible, consonants are not" (S571) | S571 p. 6, ¶[15] | "Each of these tones can be replicated on the Hmong qeej along with all of the Hmong vowel sounds. Consonants, however, cannot be pronounced by the qeej." | `LOCATED https://www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf` (both sentences) | **supported** |
| 4 | :76 Turkish: consonants as frequency and amplitude modulations, "silence for stops"; "/p/ whistled 'very similar to [k]'" (S572; S146) | S572 p. 3 (printed 839), §3 | "Whistled consonants are modulations in frequency and amplitude … When the amplitude modulation shuts off the whistle, consonants are also characterized by silent gaps."; "The occlusive [p] is expressed mainly with this process and is therefore very similar to [k] in whistles." | `LOCATED http://www.icphs2007.de/conference/Papers/1286/1286.pdf` (both) | **supported** ("silence for stops" is a fair compression of "silent gaps" plus the glottal-occlusion stop of [m], [p], [b]) |
| 5 | :79 "an archive deposit records spoken and whistled Chinantec elicited from children in San Pedro Sochiápam" (S573) | S573 Details → Description | "David Yetman and Mark Sicoli elicit spoken and whistled Chinantec from children in San Pedro Sochiápam" | `LOCATED https://archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0016_B509_0` | **supported**; the entry keeps "(to-verify)" on learning age, which is honest under S573 |
| 6 | :113 the Turkish whistled language, "with mobile phones now one of its main threats", is "about to lose its communication function" (S574) | S574 §2 | "One of the most important threats to this element is the increase in the use of mobile phones. … Today, however, it is about to lose its communication function." | `LOCATED https://ich.unesco.org/doc/src/36234-EN.doc` (both) | **supported** |
| 7 (extra) | :106 "Turkish whistling now survives in 'a few words spoken by shepherds'" (S574) | S574 §D | see finding F1 | see F1 | **NOT supported as worded: overreads** |

Row-level check: each sampled passage falls within its row's scope and locator. S570's anchor names the "tone-load and intelligibility paragraph p. 7"; S571's anchor quotes ¶[15] p. 6; S572's anchor quotes the [p]/[k] sentence at §3 p. 839; S573's anchor quotes the description verbatim; S574's anchor names §2 (mobile phones, loss of function) and §D (shepherd remainder). The remap is mechanically sound: it re-points to rows that carry the passages.

### F1 (medium; overread carried through the remap) — entry :106 with S574

Served text, S574 §D "Geographical location and range of the element" (`soffice` conversion; raw .doc bytes at offsets 6960 and 8255):

> The whistled language is practiced in Turkey's Eastern Black Sea Region … The element is widely practiced in; Çanakçı district of Giresun: Kuşköy, Karabörk Villages. The element is very rarely practiced in; [villages of Çanakçı, Görele, Eynesil, Tirebolu, Kürtün] … It's identified that until 50 years ago, it was being spoken in certain districts, especially in Trabzon, Rize, Ordu, Artvin and Bayburt; although, it has now either disappeared or is limited to a few words spoken by shepherds.

```
LOCATED https://ich.unesco.org/doc/src/36234-EN.doc
```
(quote: `districts, especially in Trabzon, Rize, Ordu, Artvin and Bayburt; although, it has now either disappeared or is limited to a few words spoken by shepherds`)

The form limits "a few words spoken by shepherds" to the districts where the language was spoken until 50 years ago. In the same section it says the element is "widely practiced" in Kuşköy and Karabörk, and §C reports nearly 10,000 people able to speak or understand it. Entry :106 ("Turkish whistling now survives in 'a few words spoken by shepherds'") makes the remainder in the former districts into the state of Turkish whistling as a whole. That is a scope overread. S572 (§1, p. 837) also contradicts it: "still practiced in the village of Kusköy and by the shepherds going in summer in the high plateaus" (`LOCATED http://www.icphs2007.de/conference/Papers/1286/1286.pdf`, round 58). The round-58 seat ReviewCarry151to159 judged every S159 site "supported"; I disagree for :106. The overread predates the remap, which only moved it from S159 to S574.

Two instrument notes for the L1:
- `until 50 years ago, it was being spoken in certain districts, especially in Trabzon, Rize, Ordu, Artvin and Bayburt` → `NOT_LOCATED https://ich.unesco.org/doc/src/36234-EN.doc quote-absent`, and the same quote starting "certain districts" also fails. Both are instrument artifacts. The .doc stores "It's identified that until 50 years ago, it was being spoken in ce" as UTF‑16LE, which `reopen-quote.py` decodes as UTF‑8 (raw bytes at offset 8255 show the switch inside "ce|rtain"). The quote starting at "districts" locates, as above.
- `The region where whistled language is keeping alive, includes the following communities` → `NOT_LOCATED … quote-absent` for the same reason: that run is UTF‑16LE at offset 6960. It is verbatim in the `soffice` text.

**Round-60 fix (not this round; the SPEECH leg is byte-exact):** :106 → `Turkish whistling is still widely practiced in Kuşköy and Karabörk, while in Trabzon, Rize, Ordu, Artvin and Bayburt, where it was spoken until 50 years ago, it "has now either disappeared or is limited to a few words spoken by shepherds" (S574)`. S574's anchor wording "(shepherd remainder)" and its teaches clause "use reduced to 'a few words spoken by shepherds'" carry the same ambiguity. A later superseding row should scope it to the five former districts.

### F2 (low; loose paraphrase carried through the remap) — entry :78 with S570

:78 places the Hmong row's terrain as "hill and mountain country of the Hmong dispersal; distance (to-verify) (S570)". S570 p. 2 says "Whistled language is largely areal, with hotspots found in the Southeast Asian mountains" (`LOCATED …Encyclopedy.pdf`) and "usually found in rural, rugged terrain with mountains and dense forest". Hmong appears on pp. 4, 5 and 7, but the page never says "Hmong dispersal" and never ties Hmong to hill country itself. Round 58 (ReviewCarry135to147, residual notes) already called this a loose paraphrase. Round-60 wording: "Southeast Asian mountains, one of the whistled-language hotspots (S570, p. 2)".

## Residual risk and verification gaps

- **CARRY-leg flake risk (fixes 82 and 141):** both list only web.archive.org captures of the Cambridge page, whose live copy answered 429 in round 58. This session, `reopen-quote.py` fetches of these captures failed transiently in 10 of 16 attempts (`URLError`/`HTTPError`; the two `url-reflects-quote` refusals made no fetch). `curl` fetched both cleanly, and 141's exact support quote located once on each capture. Under FETCH-59 a failed fetch is skipped and never passes, so one CARRY run can FAIL on 141 (or 82) through no fault of the text. If CARRY fails on these ids only with fetch errors, rerun it; do not treat the failure as a fidelity verdict.
- Fix 140 page split (`pp. 470–471`), the fix 141 "older" nit, F1 (:106) and F2 (:78) are all round-60 items. None may be landed in round 59 without failing the byte-exact KONGO or SPEECH legs.
- Not assigned and not re-checked here: kongo fixes 18, 65, 82, 84a, 84b, 85, 89, 93, 97a, 97b. The S359 page map above also shows that fix 18's "doc. 142, p. 470" is a page of the letter, so that fix is right for "a royal voice", as is the old p. 469.
- Speech sites not sampled: the other 21 of the 27 re-pointed citations. In particular, the S570 sites at :16, :18, :23, :24, :26, :53 and :78 (F2 aside), and the S572 site at :80, were not re-read by me; round 58 verified them.
- No LSP server applies (markdown corpus, PDFs, .doc). Literal checks were `grep` counts and Python string counts on the entries and `SOURCES.md`; they are used only for counting, not as semantic proof.
- I did not run `accept-d.py`, `rowcheck.py` or `accept-c.py`; those are the L1's landing gates.

installs: none. Tools used, all already present: curl 8.23.0, pdftotext 26.08.0, LibreOffice 26.8.1.1 (`soffice --headless`), python3, and `uv` (already at `~/.local/bin/uv`), which `reopen-quote.py` uses to run `pypdf==5.4.0` from PyPI in an ephemeral environment. No pacman use.

rejected: none. Every source opened (the S359 OCR text plus its `_djvu.xml`, `_scandata.xml` and item metadata; both S383 captures; S570–S574) was used above.
