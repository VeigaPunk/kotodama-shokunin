# R8-F01 — freshness recheck receipt

- **Round:** 8 (loop 1 of 3, build round 1 of 4) · **Date:** 2026-10-17 · **Shard:** FRESHNESS R8-F01
- **Prior row:** R6-02-A, disposition `unresolved` — "the requested dated text or directly inspected scholarly passage was not retrieved; Jagersma body text and a dated cuneiform witness remain unread"
- **Entry:** `corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md` (sha256 `730e1be8…ccd365`, unchanged this round)
- **Locators rechecked:** line 36 (Contact ecology row), line 38 (timing hedge), line 48 (word-signs ≠ spoken language), line 166 (craft grid, "Ritual language survives vernacular change")
- **Question:** Check the entry's evidence for Sumerian/Akkadian language contact and the separation of scribal language survival from spoken-language replacement; which dated text or scholarly passage supports the institutional coupling?

## Headline

The residual is now **resolved at passage level**, and the two specific gaps the prior round named are closed: **Jagersma's body text was read** (776-page full text, not the abstract), and a **dated witness** was obtained in scholarly analysis (a Sargon-dynasty legal tablet with Sumerian protocol and Akkadian testimony), plus a tertiary-mediated pointer to the dated bilingual object **Louvre AO 5477** (reign of Rimush) with its 1911 primary publication. Passage support is kept separate from whole-claim support below.

## Cited source (tertiary) — fresh retrieval

- **URL:** https://en.wikipedia.org/wiki/Sumerian_language · **accessed:** 2026-10-17T20:12:50Z · also raw wikitext (`action=raw`, HTTP 200, 287,991 bytes) for exact line locations.
- **Quoted passage** (lead section, third paragraph; raw wikitext line 29):
  > "Akkadian, a Semitic language, gradually replaced Sumerian as the primary spoken language in the area c. 2000 BC (the exact date is debated), but Sumerian continued to be used as a sacred, ceremonial, literary, and scientific language in Akkadian-speaking Mesopotamian states, such as Assyria and Babylonia, until the 1st century AD."
- **support_scope:** `passage-level` (tertiary-mediated; covers replacement + learned survival, supplies no dated text).

Supporting tertiary locations retrieved the same day: lead ¶4 on mutual influence (raw line 31); §Stages, interlinear-translation and Sumerogram-encoding paragraph (raw line 60); §Stages caption for the Rimush bilingual with its Thureau-Dangin 1911 footnote (raw line 35); §Writing system → Development, "the two languages influenced each other, as reflected in numerous loanwords and even word order changes" (raw line 81).

## Primary/eligible passages (priority over tertiary catalogues)

### Jagersma 2010 — the entry's own named anchor, body text now read

`A Descriptive Grammar of Sumerian`, PhD dissertation, Leiden University. Full text: https://scholarlypublications.universiteitleiden.nl/download/1887/16107/2?col=81522199240002711&col=81522199220002711 — PDF, 776 pp., 7,174,092 bytes, sha256 `2e14f1fa…` (accessed 2026-10-17T20:14:10Z; text via `pdftotext -layout`).

- **p. 1 (§1.1):** > "It is documented as a living language from the late fourth millennium, the date of the earliest cuneiform documents, until the early second millennium. Though no longer spoken, Sumerian continued to be used as a language of scholarship and cult until the end of the first millennium BCE."
- **p. 5 (§1.2.2):** > "The earliest texts included in our corpus date from the Old Sumerian period … (ca. 2470 BCE) until the unification of the entire country under the kings of Akkad (ca. 2340 BCE)." — with the Girsu/Lagash archive group: > "well over one hundred inscriptions (ca. 2470-2350 BCE) … and a group of more than 1700 administrative texts (ca. 2380-2350 BCE) concerning the estate of the queen of Lagash".
- **p. 6 (§1.2.2):** > "But it is also the period when Akkadian had become the primary language of the scribes. … Because these texts were produced by scribes who were not native speakers of Sumerian, I have generally excluded them from my corpus." and > "After the early Old Babylonian period, scribes continue to produce Sumerian texts until the late first millennium BCE but with interlinear Akkadian translations added. Sumerian had become a language of scholarship and cult."

This is the dated-text/archive leg and the register separation in the entry's own cited grammar.

### Rubio 2006 — "Writing in Another Tongue", in Sanders (ed.), *Margins of Writing, Origins of Cultures* (OIS 2), pp. 33–70

Volume PDF via web.archive.org id_ snapshot (318 pp., sha256 `c4e4dc3b…`), accessed 2026-10-17T20:14:51Z.

- **p. 49:** > "Sumerian had died out at the end of the third millennium, when it stopped being anyone's mother tongue. Although some still try to resurrect Sumerian and argue that it was a true living language after Ur III, this is completely at odds with the evidence."
- **p. 50:** > "Sumerian was most likely used in scribal circles and probably spoken among teachers and scribes, as was the case of Latin in some academic and clerical circles well into the twentieth century." and > "Throughout Mesopotamian history, scribes painstakingly learned a language that had long died (Sumerian) and had to use an artificial and conservative variant of their native language (an Akkadian dialect)."

### Woods 2006 — "Bilingualism, Scribal Learning, and the Death of Sumerian" (OIS 2, pp. 95–124)

- **p. 100:** > "More compelling, however, are the unorthographic spellings that occur in sale documents from Nippur, which suggest a bond with the spoken language rather than the memorized relics of a dead language."
- **p. 101:** > "As Sallaberger has recently observed, an argument can be made for Sumerian as a spoken language in the Ur III period based on the non-formulaic language of letters and of certain administrative texts…"

This is counter-evidence to any fixed early death date — it supports the entry's line-38 hedge, not a revision of it.

### Michalowski 2006 — "The Lives of the Sumerian Language" (OIS 2, pp. 163–184)

- **p. 164:** > "There is agreement on one thing only: the spoken language died in antiquity. The date of this death has been variously estimated".
- **p. 168 (§Sumerian and Akkadian):** > "Lexical borrowings are the main evidence for interference between Akkadian and Sumerian. The most commonly cited evidence of syntactic borrowing has been the matter of word order in Akkadian."
- **p. 171:** the five write/read combinations after Civil 1984: 76 — written Sumerian can be read in Akkadian and vice versa, so script identity ≠ speech identity.
- **p. 172 (dated witness):** > "The language of writing for this particular scribe and his intellectual milieu was Sumerian, but in reporting stylized direct speech he acknowledged that the vernacular in his world was already Akkadian" — analysing a fragmentary legal tablet edited at Westenholz 1975: 36 / Edzard 1968: 137–38, datable "to the time of the dynasty of Sargon" (Old Akkadian, conventionally ca. 2340–2200 BCE).

### Zólyomi 2000 — "Structural interference from Akkadian in Old Babylonian Sumerian", *Acta Sumerologica* 22

Author preprint PDF (6 pp., sha256 `3c256e65…`) via web.archive.org snapshot 20210228041703, accessed 2026-10-17T20:14:35Z. **§3 opening (PDF p. 3):** > "Given the number and nature of the differences between the two languages, it would be unreasonable to expect no interference to have occurred when a scribe whose native language was Akkadian used Sumerian. … interference did occur and … was fairly substantial…"

## Dated witnesses

| Witness | Source (read this round) | Status |
|---|---|---|
| Girsu/Lagash temple and palace archives, ca. 2470–2350 BCE; Ur III palace archives | Jagersma 2010 pp. 5–7 | body text read |
| Sargon-dynasty legal tablet, Sumerian protocol / Akkadian testimony (Westenholz 1975: 36) | Michalowski 2006 p. 172 | body text read (scholarly analysis) |
| Louvre AO 5477, reign of Rimush; pub. Thureau-Dangin 1911, *RA* 8(3): 138–141 (JSTOR 23284567) | Wikipedia §Stages caption (tertiary pointer + primary-publication footnote) | **pointer only** — object record not retrieved (Louvre HTTP 429; CDLI search client-rendered) |

## Support scopes kept separate

- **Passage-level:** every leg of the bounded entry row now has at least one directly inspected scholarly passage — coexistence/influence (Michalowski p. 168; Zólyomi §3); learned/cultic survival (Jagersma pp. 1, 6; Rubio pp. 49–50); script ≠ speech (Michalowski p. 171; Jagersma p. 6); timing unrecoverable (Michalowski p. 164; Woods pp. 99–101).
- **Whole-claim:** `supported` for the bounded row, with the qualification that no source fixes a vernacular-loss date and Woods argues for Ur III spokenness — which the entry's own line-38 hedge already permits. Nothing retrieved contradicts the row.
- **Not established:** any Sumerian pronunciation reconstruction; that every post-2000 BCE Sumerian register was unspoken.

## Access failures (documented, not worked around silently)

| Attempt | Status |
|---|---|
| `collections.louvre.fr/en/recherche?q=AO+5477` | HTTP 429; guessed-ark retry returned a different object ("vase"), discarded |
| `cdli.earth/search?q=AO+5477` (and quoted variant) | HTTP 200 but results client-rendered; no server-side row for the tablet |
| `assziriologia.hu/…/gz_structural_interference.pdf` | domain now parked (HTML, 51,231 B) → used archive snapshot |
| `isac.uchicago.edu/…/ois2_2007.pdf` | HTTP 200 but HTML, not PDF → used archive `id_` snapshot |
| `openaccess.leidenuniv.nl/bitstream/…Binnenwerk-jagersma.pdf`; `…/access/item:2961988/view` | HTML stubs, not full text → used repository `/download/1887/16107/2` |
| `www-personal.umich.edu/~piotrm/DIGLOS~1.htm` | HTTP 403 (Cloudflare) → superseded by the OIS 2 chapter |

## Disposition

`unresolved` → **`resolved-passage-level`**. Residual limits: the dated object witness remains a pointer (`to-verify` until a museum/CDLI record is retrieved); Michalowski's tablet analysis was read in the chapter, not collated against the tablet. No fabricated sources: every quotation above names its file, page, or URL and section.
