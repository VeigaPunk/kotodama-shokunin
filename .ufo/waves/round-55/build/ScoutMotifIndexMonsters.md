# Scout report — Thompson's Motif-Index, chapters B (mythical animals), F (marvels) and G (ogres)

- seat: KotodamaR55.ScoutMotifIndexMonsters (source seat, claim C)
- date: 2026-10-22
- lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin, base `f4015e70b829523ed81e14ce4279bfab0e0233e4`
- question: open a public copy of Stith Thompson's Motif-Index and quote the chapter headings of B (B0–B99 mythical animals) and of F or G with their motif numbers, as source rows for the new entry `corpus/knowledge/myth-symbol/monsters-hybrid-beings.md`.
- axes I worked: (1) source count for claim C, (2) tier strength of the B/F/G chapter evidence, (3) design-decision coverage (name, body, map, function, record, period). No file outside this report was touched.

## Observed facts (opened this session)

Both copies are of the 1955–58 edition: the ruthenia pages state "Revised and enlarged. edition. Bloomington : Indiana University Press, 1955-1958", the Wikisource index record gives Indiana University Press, 1955, LCCN 55008085, and its scan set is named `Thompson Motif-Index 2nd 1.djvu`. That is the standard citation edition the lane already uses (`corpus/knowledge/myth-symbol/motif-index-usage.md:3`).

- **Wikisource** (`Index:Thompson Motif-Index 2nd 1.djvu`; index record: publisher Indiana University Press, year 1955, LCCN 55008085, volume 1 = A–C) is scan-backed: every page I quote carries `pagequality level="3"` ("Proofread") and a running head, and the scanned title page (`/7`) is level 4 ("Validated"). It holds **volume 1 only (A–C)**; a page listing for `Page:Thompson Motif-Index 2nd 3.djvu` returns an empty set, so chapter F and G text is **not** there.
- **ruthenia.ru** (RSUH folklore department's `Фольклор и постфольклор` project) hosts the **full English text of chapters F and G** as one HTML page per chapter, with an explicit edition statement. It is OCR-derived: it prints `ж`, `д`, `ь` where the book prints `ä`, `ü`, `ö` (e.g. `Drachenkдmpfer`, `Sжrtryk`), has no printed page numbers, and runs words together inside the synopsis tables (`G10--G99. Cannibals and cannibalismG10--G49.`). Quotable only where the text is ASCII-clean, which the headings are.
- Structure observed on the page (not a quote): the B chapter prints its **detailed synopsis on printed p. 346** and its **entries from printed p. 348**, and the volume's front matter prints a **"General Synopsis of the Index"** — one block per lettered chapter, number ranges only — with the **B block on printed p. 30** and the **F and G blocks on printed p. 31**. That General Synopsis is the cheapest single place to quote chapter scope for any letter.

### NEW-ScoutMotifIndexMonsters-1

- citation: Thompson, Stith. 1955. *Motif-Index of Folk-Literature*, Vol. 1 (A–C). Bloomington: Indiana University Press. Wikisource proofread transcription of the scanned copy, `Index:Thompson Motif-Index 2nd 1.djvu` (index record: publisher Indiana University Press, year 1955, LCCN 55008085, volume scope A–C); title page transcribed at `Page:Thompson Motif-Index 2nd 1.djvu/7` (page status "Validated") reads only "Motif-Index of Folk-Literature / Vol. 1", so the long subtitle used in NEW-2 is not quoted from this copy.
- url: https://en.wikisource.org/wiki/Page:Thompson_Motif-Index_2nd_1.djvu/37 (General Synopsis, printed p. 31); also /36 (printed p. 30), /352 (printed p. 346), /354 (printed p. 348), /355 (printed p. 349), rendered at https://en.wikisource.org/wiki/Motif-Index_of_Folk-Literature/Volume_1/B
- route: direct plain request, HTTP 200, `text/html; charset=UTF-8`, 2026-10-22; text read through the MediaWiki API (`action=query&prop=revisions|proofread`) on the same host, which returned page status "Proofread" for pages 36, 37, 352, 353, 354, 355. Printed page numbers taken from the running heads on those pages (p. 353 → "B. Animals 347"; p. 355 → "B. Animals 349"; p. 356 → "350 Motif-Index of Folk-Literature"; p. 351 → "A. Mythological Motifs 345"); p. 346 is the chapter opening with the running head suppressed and is numbered by sequence between pp. 345 and 347. The synopsis sets ranges with hidden alignment characters (`{{0}}` templates, invisible on the page); the quoted strings are the visible rendering, and the entry page prints the same range plainly as "B0—B99. Mythical animals."
- kind: book
- tier: A — a page-by-page proofread transcription of the 1955 Indiana UP edition with page images behind each page, printed pagination preserved, and every quoted heading independently confirmed against NEW-2. Authoritative for heading wording, number ranges and page numbers of the B chapter; not for Thompson's argument, which is in the Introduction I did not open.
- scope: the class numbers and headings of chapter B (B0–B99 mythical animals and its non-composite neighbours), the composite-body ladder B10/B20/B30/B40/B50/B60/B70/B80/B90, the General Synopsis ranges for chapters B, F and G, the placement of "Witches" inside the G chapter's "Kinds of ogres", and the entry text of B0, B10, B11.1.3 with their bibliography and cross-references.
- quotes:
  - General Synopsis, printed p. 30, B table, first line: "B0—B99. Mythical animals"
  - General Synopsis, printed p. 30, B table, third line: "B200—B299. Animals with human traits"
  - General Synopsis, printed p. 31, F table, second line: "F200—F699. Marvelous creatures"
  - General Synopsis, printed p. 31, G table, first line: "G10—G399. Kinds of ogres"
  - General Synopsis, printed p. 31, G table, fourth line (inside the "Kinds of ogres" block): "G200—G299. Witches"
  - chapter B detailed synopsis, printed p. 346, first subdivision: "B10. Mythical beasts and hybrids"
  - chapter B detailed synopsis, printed p. 346, second subdivision: "B20. Beast-men"
  - chapter B detailed synopsis, printed p. 346, eighth subdivision: "B80. Fish-men"
  - chapter B entries, printed p. 348, entry B0: "Lum (Peter) Fabulous Beasts (New York, 1951). — Irish myth: Cross; Jewish: Neuman."
  - chapter B entries, printed p. 348, B0 cross-reference column: "A417.1. Beast guardians of the four quarters of the world."
  - chapter B entries, printed p. 349, B11 cross-reference column: "C92.2. Tabu: killing sacred dragon."
  - chapter B entries, printed p. 349, entry B11.1.3: "Dragon from transformed man lying on his treasures (Fáfnir)."
- teaches: The 1955 index files monstrous beings by what the body is made of before what the being does, and its B-chapter subdivisions give a three-grade ladder for composite bodies.
- draft sentences:
  - The index names the class by anatomy, not by behaviour, and puts the animal-bodied hybrid and the human-bodied hybrid one hundred numbers apart: "B0—B99. Mythical animals" and "B200—B299. Animals with human traits" are separate classes (NEW-ScoutMotifIndexMonsters-1, vol. 1, General Synopsis, printed p. 30).
  - The composite body has its own ladder, printed as one run on the synopsis page — B10 "Mythical beasts and hybrids", B20 "Beast-men", B30 "Mythical birds", B40 "Bird-beasts", B50 "Bird-men", B60 "Mythical fish", B70 "Fish-beasts", B80 "Fish-men", B90 "Other mythical animals" — so a culture that files its hybrid at B10 or at B80 has already answered whether the beast or the person supplies the body (NEW-ScoutMotifIndexMonsters-1, vol. 1, chapter B detailed synopsis, printed p. 346).
  - Who records the being is printed in the entry: B0 cites the modern wonder catalogue "Lum (Peter) Fabulous Beasts (New York, 1951)" beside per-people source tags "Irish myth: Cross; Jewish: Neuman", so each culture's evidence is a named scholarly collection (NEW-ScoutMotifIndexMonsters-1, vol. 1, chapter B, entry B0, printed p. 348).
  - The guardian role is filed as a cross-reference into the mythology chapter, not as a monster class — B0 points to "A417.1. Beast guardians of the four quarters of the world" — so a worldbuilder must decide whether a boundary guardian is a being or a cosmological function (NEW-ScoutMotifIndexMonsters-1, vol. 1, chapter B, entry B0, printed p. 348).
  - Prohibition attaches to the named beast rather than to the class: the dragon's entry B11 carries "C92.2. Tabu: killing sacred dragon", so a restriction belongs in the culture's tabu list beside the being that carries it (NEW-ScoutMotifIndexMonsters-1, vol. 1, chapter B, printed pp. 348–349).
  - The G chapter is built as "G10—G399. Kinds of ogres" and places "G200—G299. Witches" inside it, so a culture that separates witch from ogre is making a distinction the index does not make (NEW-ScoutMotifIndexMonsters-1, vol. 1, General Synopsis, printed p. 31).

### NEW-ScoutMotifIndexMonsters-2

- citation: Thompson, Stith. 1955–1958. *Motif-index of folk-literature: a classification of narrative elements in folktales, ballads, myths, fables, medieval romances, exempla, fabliaux, jest-books, and local legends*. Revised and enlarged edition. Bloomington: Indiana University Press. Full text of chapters F and G as published by the folklore department project "Фольклор и постфольклор" (ruthenia.ru), grant support INTAS 05-1000008-7922 and RFBR 06-06-80-420a / 07-06-00441-а.
- url: https://www.ruthenia.ru/folklore/thompson/f.htm and https://www.ruthenia.ru/folklore/thompson/g.htm
- route: direct plain request, HTTP 200, `text/html; charset=windows-1251`, 2026-10-22, both chapters read in full and normalised from windows-1251 to UTF-8. Chapter index page https://www.ruthenia.ru/folklore/thompson/indexleft.htm also read (HTTP 200) to confirm the letter-to-page mapping (a.htm–z.htm, I, O and Y absent).
- kind: book
- tier: B — a university folklore-department project's full-text transcription of the 1955–58 edition; reliable for chapter and entry headings and for motif numbers, weaker than NEW-1 because it is OCR-derived, carries no printed pagination, corrupts diacritics, and shows no rights statement. Not used alone for any wording NEW-1 could confirm.
- scope: the detailed synopses of chapters F and G including their section ranges down to F900–F1099 and G600–G699, the entry bodies at F110, F130.1–F130.2, F200, F211, F420, F531, F600, F701, G100, G200, G230–G235, G310–G311, G360–G361, the title-page subtitle listing the genres indexed, and the edition statement. Supports the placement of fairies, spirits, witches and giants; does not support any printed page number, any 1932–36 numbering, or any claim about a particular living tradition.
- quotes:
  - chapter-page header, title line: "a classification of narrative elements in folktales, ballads, myths, fables, medieval romances, exempla, fabliaux, jest-books, and local legends"
  - chapter-page header, edition line: "Revised and enlarged. edition. Bloomington : Indiana University Press, 1955-1958."
  - chapter F, detailed synopsis, under F110—F199: "F110. Journey to terrestrial otherworlds"
  - chapter F, entry F130.1: "Land of India (Greece) as otherworld."
  - chapter F, entry F211: "Fairyland under hollow knoll. Usually entered under roots of trees."
  - chapter F, entry F200: "See also F420 (Water Spirits), F451 (Dwarfs) and F460 (Mountain Spirits) for many common motifs."
  - chapter G, detailed synopsis, under "G10--G399. KINDS OF OGRES", first sub-block: "G10--G99. Cannibals and cannibalism"
  - chapter G, detailed synopsis, under G10--G399: "G200--G299. Witches"
  - chapter G, detailed synopsis, other-ogres block: "G310. Ogres with characteristic methods"
  - chapter G, entry G100: "Giant ogre. Polyphemus. (For motifs concerning giants who are not malevolent but merely large, see F531.)"
  - chapter G, entry G311: "Old man of the sea. Burr-woman. Ogre who jumps on one's back and sticks there magically." (the copy prints a curly apostrophe in "one's"; normalised here)
  - chapter G, entry G233: "Witch lives in fairy mound."
- teaches: Thompson's F and G chapters put wonder-beings on a real-world map, rank ogres by method and malevolence, and cross-list fairies, witches and spirits instead of fixing them.
- draft sentences:
  - The catalogue states which kinds of book it was built from — "folktales, ballads, myths, fables, medieval romances, exempla, fabliaux, jest-books, and local legends" — so a monster drawn from a culture's sermons or romances is admissible beside one from its oral tales (NEW-ScoutMotifIndexMonsters-2, chapter-page header, title line).
  - The wonder-world is placed on the map rather than outside it: F130.1 "Land of India (Greece) as otherworld" and F130.2 "Spain as otherworld" name real countries as the otherworld's location (NEW-ScoutMotifIndexMonsters-2, chapter F, entry F130.1 and F130.2).
  - Access runs through a small opening in the ground — F211 "Fairyland under hollow knoll. Usually entered under roots of trees" — so the entry's map question is where the entrance is and who controls it (NEW-ScoutMotifIndexMonsters-2, chapter F, entry F211).
  - Malevolence, not size, makes an ogre: G100 heads "Giant ogre. Polyphemus." and sends "giants who are not malevolent but merely large" to F531, so a worldbuilder must decide whether the being is dangerous or only big (NEW-ScoutMotifIndexMonsters-2, chapter G, entry G100).
  - The ogre is also defined by method rather than shape — G311 "Old man of the sea. Burr-woman. Ogre who jumps on one's back and sticks there magically" — so write down what the being does to a traveller before deciding what it looks like (NEW-ScoutMotifIndexMonsters-2, chapter G, entry G311).
  - The classes leak in practice and the index cross-lists instead of policing them: F200 "Fairies (elves)" points to F420 Water Spirits, F451 Dwarfs and F460 Mountain Spirits, and G233 records that a "Witch lives in fairy mound" (NEW-ScoutMotifIndexMonsters-2, chapter F entry F200 and chapter G entry G233).

## Design-decision coverage map (for the entry's section order)

| worldbuilder decision | evidence | strength |
|---|---|---|
| what the culture calls the being, what the word means | G100 splits "ogre" from "giant who is merely large"; the G chapter's own sub-blocks are "Cannibals and cannibalism", "Giant ogres", "Witches", "Other ogres"; the F chapter's are "Fairies and elves", "Spirits and demons", "Remarkable persons", "Persons with extraordinary powers" | solid: the index names by role and habitat, never by etymology. The **word-meaning** axis is not supported by these two sources. |
| composite anatomy | B10/B20/B30/B40/B50/B60/B70/B80/B90 (NEW-1, p. 346); G360 "Ogres with monstrous features", G361 "Ogre monstrous as to head", G361.1 "Many-headed ogre" (NEW-2) | solid |
| where monsters live on the world's map | F0–F199 otherworld journeys, F130 location/bounds, F130.1–F130.2 real countries, F211 hollow knoll, F210 fairyland, G230–G235 "Habitat of witches" (cliff, glass mountain, fairy mound, tree, monastery) | strong — this is the best-evidenced axis |
| warns, guards, punishes, teaches, devours | G10–G79 cannibalism (devouring), G400–G499 "Falling into ogre's power", G500–G599 "Ogre defeated", B300–B599 "Friendly animals" / B350 "Grateful animals" (helping), A417.1 beast guardians as a *cross-reference* | partial: guardian and devourer are documented; **omen** is not. Omens sit in chapter M, which neither copy gave me in section detail. |
| who records or depicts it, in what book or object | NEW-1 B0 cites "Lum (Peter) Fabulous Beasts (New York, 1951)" plus per-people tags; NEW-2 title line lists the genres indexed | solid for the scholar's bestiary and the genre list; nothing on objects, images or ritual display |
| restricted beings | B11 cross-references "C92.2. Tabu: killing sacred dragon"; B2 cross-references "C221.2. Tabu: eating totem animal" and "C841. Tabu: killing certain animals"; F210.1 "Tabu: fighting battle in fairyland" | partial: the index records prohibitions on killing and on conduct in the otherworld, but every such motif is a cross-reference into chapter C, never text under the being |
| what changes across periods | NEW-2 states "Revised and enlarged. edition … 1955-1958" | **weak/absent**: the 1932–36 first edition was not opened, so no numbering or wording change can be dated. Do not write a period-drift sentence from these rows. |

## Coupling to the lane and routed observations

- `corpus/knowledge/myth-symbol/motif-index-usage.md:33` (B row, "wonder beasts, animal traits", exemplar B11 Dragon) — confirmed: B11's entry begins at the foot of printed p. 348 and continues on p. 349, while B10 is a bare grouping heading with no entry text.
- `motif-index-usage.md:37` (F row, "fantastic places, beings, objects", glossed "fairyland / wonder-object block") — **imprecise**: the General Synopsis (printed p. 31) splits F into F0–F199 Otherworld journeys, F200–F699 *Marvelous creatures* (F200–F399 fairies and elves, F400–F499 spirits and demons, F500–F599 remarkable persons, F600–F699 persons with extraordinary powers), F700–F899 *Extraordinary places and things*, F900–F1099 extraordinary occurrences. Fairyland is F200–F399, inside the creatures block; wonder objects are F700–F899. A routed correction candidate for the L1.
- `motif-index-usage.md:38` (G row, G310 "Ogres with characteristic methods") — confirmed literally, and G310 sits in "Other ogres" (G300–G399), not in the giant block.
- The new entry should carry at least these two rows as its bestiary spine and cite them for structure only; every culture-specific sentence in the entry needs a different source (museum record, edition, community statement). These rows cannot support statements about any living tradition.
- No file in the lane was edited. Nothing was installed.

## Unrun checks

- I did not run `reports/round-55/accept-c.py`, `accept-o.py`, the separability command or any sweep; claim verification belongs to the L1.
- I did not run any git or jj command: no sandbox clone was needed for a read-only source seat.

## unopened

- `archive.org/download/motifindexoffolk0005thom/motifindexoffolk0005thom_djvu.txt` — the Internet Archive's own 1955 scan. HTTP 302 to the lending flow; `access-restricted-item: true`. **Challenge met, not passed**: no attempt to defeat the lending restriction was made, and no Wayback route was tried for the text layer.
- `archive.org` items `B-001-002-578` (vol. I A–C, 1955) and `B-001-002-766` (vol. III F–H, 1956), collection `patron-library-collection` / `nicolai-woodenko-library` — plain-text and PDF files present and unrestricted, but these are bulk patron uploads of an in-copyright 1955 book with no publisher metadata: refused as shadow copies under the wave's source rule, not read.
- `archive.org` item `Thompson2016MotifIndex` (collection `robert-bedrosian-library`, `patron-library-collection`) — same reason, refused without opening.
- Wikisource volume 3 (F–H): an `allpages` query with prefix `Page:Thompson Motif-Index 2nd 3.djvu` returned an empty set, so no transcribed F or G text exists there; only volume 1 (A–C) is transcribed.
- HathiTrust: an OCLC-based catalogue lookup (OCLC 3054424, an unverified guess) returned no records; no title search on HathiTrust was run, so a full-view copy may exist and is unclaimed.
- The 1932–36 first edition (FF Communications 89–106) — not opened. Needed before any sentence about numbering or wording drift between editions.
- Thompson's Introduction and the "how to use" matter in vol. 1 — not opened, so no sentence in the entry should describe Thompson's theory of the motif, only the chapter structure.
