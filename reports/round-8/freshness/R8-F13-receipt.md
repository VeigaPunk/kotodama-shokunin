# R8-F13 — Etruscan language/alphabet recheck receipt

- round: 8 (baseline `e7ca0faeb6680fa9891b907be628d9db578c28f4`)
- id: R8-F13; prior row R6-10-A; prior ledger `corpus/lessons/round-6-sources/10.json`
- entry: `corpus/knowledge/civilizations/etruria.md` §2 — Genealogy (line 41), Script ancestry (line 42), Sign selection (line 43), Morphology (line 46), Sound change (line 47), bullets lines 49 and 51
- question: Check the entry's Etruscan language/alphabet relationship using epigraphic or scholarly evidence; readable adapted Greek letters do not establish Indo-European affiliation or complete lexical understanding.
- accessed-at: 2026-10-17 (session start `date -u +%FT%TZ` → `2026-10-17T20:13:05Z`)

## Fresh retrieved passages (5; each quoted from the retrieved page text, not a search snippet)

### P1 — main, target URL: Posth et al. 2021, *Science Advances* 7(39):eabi7673, PMC open-access copy

- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8462907/ — HTTP 200 (curl, 2026-10-17); full text returned by FetchURL (111,036 chars, host-saved)
- Location: Abstract; INTRODUCTION first paragraph; subtitle
- Quote: "This culture is renowned for its outstanding skills in metallurgy, its sophisticated cultural representations, and its extinct language, a non–Indo-European language not yet fully understood (1, 2)." … "the persistence of a probable non–Indo-European language isolate surrounded by Italic Indo-European–speaking groups (such as the Latins) is an intriguing and still unexplained phenomenon"
- Passage scope: the source's own characterization of the language (non-IE; explicitly paired with incomplete understanding). A genetics paper's wording — not a linguistic/epigraphic argument, and no position on the Tyrsenian grouping.

### P2 — Mnamon SNS, "Etruscan" (Maras; the entry's [M22])

- URL: https://mnamon.sns.it/index.php?page=Scrittura&id=10&lang=en — HTTP 200 (curl, 2026-10-17); full page retrieved
- Location: body paragraphs on the origin of the writing system and sign selection; closing paragraph on syncope
- Quote: "The Euboean-Chalcidian variant of the Greek alphabet in use among the earliest colonists to Campania was at first adopted in its entirety by the Etruscans" … "The needs of the Etruscan language, different from those of Greek, lead to a selection of the signs to be used which excluded the voiced plosives (beta and delta) and the vowel /o/." … "Menrva instead of Menerva (name of a goddess) or turce in the place of turuce (verb for offerings)"
- Passage scope: script leg (adoption/adaptation; sign selection) plus one syncope exemplar (entry line 47). Repository-scholarship synthesis; no inscription photograph inspected.

### P3 — BMCR 2008.05.37 (Turfa review of van der Meer 2007; the entry's [T08]), fresh re-fetch

- URL: https://bmcr.brynmawr.edu/2008/2008.05.37/ — HTTP 200 (curl, 2026-10-17); full review retrieved
- Location: opening paragraph; "Liber linteus" section; "Discrepancies with other translators" section
- Quote: "the Etruscan language is generally knowable" … "multiple variant translations exist for many terms" … "about 1330 words, but only about 50 major terms (30-40% is lost)" … "we are in uncharted territory, and should not expect polished translations."
- Passage scope: readable-letters vs incomplete-understanding leg. Peer-reviewed review venue (secondary).

### P4 — BMCR 2009.12.33 (López Montero review of Wallace, *Zikh Rasna*, 2008)

- URL: https://bmcr.brynmawr.edu/2009/2009.12.33/ — HTTP 200 (FetchURL, 2026-10-17); full review retrieved
- Location: review body chapter summaries — Ch. II (pp. 17–28 writing system/alphabet), Ch. IV (pp. 43–56 morphology), Ch. X (pp. 135–195 inscriptions cited by Rix's *ET* / ETPO), Ch. XII (pp. 215–225 genetic relationship)
- Quote (Ch. IV): "Señala el carácter aglutinante del etrusco, hecho que lo distancia de las lenguas indoeuropeas." (Ch. XII): "Aduce la prueba de los numerales para alejar el etrusco del latín, del griego y del sánscrito, es decir, del indoeuropeo. A su vez, compara la inscripción de la estela de Kaminia (Lemnos) y algunas del rético para concluir que estas dos lenguas comparten con el etrusco correspondencias en la morfología nominal y verbal."
- Passage scope: affiliation argued from morphology/numerals (not script); Lemnian (Kaminia stele) and Raetic morphological correspondences. Review-mediated — describes the manual's content; not independently inspected inscriptions.

### P5 — Met Heilbrunn Timeline essay (Huntsman 2013), pinned Wayback snapshot

- URL: https://web.archive.org/web/20250323221325/https://www.metmuseum.org/essays/etruscan-language-and-inscriptions — snapshot located via `curl 'https://web.archive.org/cdx/search/cdx?url=metmuseum.org/essays/etruscan-language-and-inscriptions&output=json&limit=5'` (2026-10-17); full essay text retrieved
- Location: essay body, first two paragraphs and closing paragraph; contributor line "Theresa Huntsman, Washington University in St. Louis, June 2013"
- Quote: "The Etruscan language is a unique, non-Indo-European outlier in the ancient Greco-Roman world. There are no known parent languages to Etruscan" … "it is the Euboean Greek alphabet that the Etruscans adopted and adapted to fulfill the phonological and grammatical needs of their native tongue" … "While there is still much we do not know about the Etruscan language, the corpus of inscriptions continues to grow"
- Passage scope: museum scholarly-educational essay (named academic contributor) on alphabet adoption/adaptation, non-IE status, and remaining unknowns. Tertiary; cited to the pinned snapshot because the live page body is JavaScript-rendered.

## Passage support vs whole-claim support (kept separate)

- Per-passage scopes are recorded above and in the JSON (`passage_support_scope` per passage).
- Whole-claim support: **bounded compound**. All four components of the entry's §2 claim now carry fresh round-8 passages (non-IE affiliation: P1+P4+P5; alphabet adoption/sign selection: P2+P5; readable-vs-understood: P3+P5; Tyrsenian morphology comparisons: P4). It is **not** whole-claim "supported": [R98] Rix 1998 and [B02] Bonfante & Bonfante 2002 remain unread, no inscription photograph was inspected first-hand, and every fresh corroboration is web-mediated.
- Negative test in the question holds against fresh evidence: no retrieved source derives Indo-European affiliation from the readable adapted Greek letters — Mnamon and the Met essay present the alphabet as a borrowed/adapted script, while affiliation statements come from morphology/numerals (P4) and the main paper's wording (P1).
- Raw worker label preserved (NOT overwritten): round-6 verdict `supported`, scope `whole-bounded-claim` (`corpus/lessons/round-6-sources/10.json`). Prior reconciled disposition from `reports/round-8/targets.json` freshness[12]: `partial-support`. Round-8 proposal: `scoped-support`, because each previously partial leg gained a fresh retrieved passage at repository-scholarship or peer-reviewed venue level while the print-access limits persist.

## Documented access failures and limits (attempted command + status, 2026-10-17)

- [R98] Rix 1998 *Rätisch und Etruskisch*: `curl -L 'https://archive.org/advancedsearch.php?q=title%3A%28R%C3%A4tisch+und+Etruskisch%29&…&output=json'` → HTTP 200, `numFound: 0`; HathiTrust `babel.hathitrust.org/cgi/pt?id=mdp.39015048952074` → 403. Monograph unread.
- [B02] Bonfante & Bonfante 2002: `curl 'https://archive.org/metadata/etruscanlanguage0000bonf'` → `access-restricted-item: true` (lending-restricted; not read). A second archive.org item (`bonfantebonfantetheetruscanlanguageanintroduction2ndedition2002`, collection `folkscanomy`, no access restriction) is an unverified user upload with unstated rights and was **not** used.
- Etruscan Texts Project / Etruscan Texts Project Online (epigraphic corpus cited in BMCR 2009.12.33): `http://etp.umass.edu/` → curl exit 6 "Could not resolve host" (code 000); `http://etpo.umass.edu/` and `https://etpo.umass.edu/` → 000; `http://www.umass.edu/etpo/` → 403; Wayback CDX for both hostnames → `[]`. No first-hand epigraphic corpus consulted.
- Met essay live page: FetchURL → HTTP 200 but main-text extract contained only image captions; curl retry → HTTP 429; Wayback availability API said no snapshots while the CDX index returned 20250323221325 (used).
- Freeman 1999, *Etruscan Studies* (De Gruyter): `curl -L https://www.degruyter.com/document/doi/10.1515/etst.1999.6.1.1/html` → HTTP 202 (JavaScript challenge); not fetched further, not used.

## Counting commands

- `date -u +%FT%TZ` (2026-10-17) → `2026-10-17T20:13:05Z`.
- Status sweep `for u in …; do curl -sS -m 25..30 -o /dev/null -w '%{http_code}' -L "$u"; done` (2026-10-17) → Mnamon 200; PMC8462907 200; BMCR 2008.05.37 200; archive.org details 200; etp.umass.edu 000; etpo.umass.edu 000; umass.edu/etpo 403; HathiTrust 403; Wayback etp 404; De Gruyter 202.
- Fresh-passage count for this row: **5** (1 main + 4 corroborations), each with a named location and quoted text. The F-claim's global threshold (≥8 of 15 rows with a retrieved substantive passage) is measured by `reports/round-8/run-validation.py`, not by this receipt.

## Entry hash and leg coverage

- `entry_sha256_at_recheck`: `1c6f5b043c631849875998956d6342562b6d5e34f4b0689d4ea37c890045cd04` (`sha256sum corpus/knowledge/civilizations/etruria.md`, 2026-10-17). The round-8 metadata sweep appended two header lines (`verified-at`, `recheck:`; lines 21–22); `git diff --stat` = 2 insertions, 0 deletions, so the §2 rows rechecked here are byte-unchanged. This shard did not modify the entry.
- Leg coverage: non-IE affiliation (P1+P4+P5); Tyrsenian/Lemnian/Raetic morphology (P4, review-mediated); alphabet adoption (P2+P5); sign selection (P2); readable-vs-understood (P3+P5); syncope (P2); four-relationships separation (P4+P5). The entry's own hedge on branching/separation dates/migration scenarios was not re-verified this round — no fresh passage adds dating.

## Notes

- Reconciliation across rows is owned by another shard (`reports/round-8/freshness/reconciliation.json`); this receipt preserves the raw round-6 label verbatim and proposes `scoped-support` as the round-8 disposition.
- All readings are author-side, not independent promotion verification; no restricted-work content was redistributed.
