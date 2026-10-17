# R9-F01b — freshness receipt (scholarly-fulltext hunter)

- **Round:** 9 (loop 1 of 3, build round 2 of 4) · **Date:** 2026-10-17 · **Shard:** FRESHNESS R9-F01b
- **Residual:** R8-F01 / prior row R6-02-A (Sumerian–Akkadian contact; scribal survival vs spoken replacement)
- **Entry:** `corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md` — live sha256 `bf6c92f9…4b478` (= git blob at baseline `e1694ba`; worktree clean)
- **Locators rechecked against the live file:** line 39 (Contact ecology row), line 41 (timing hedge), line 46 (word-signs ≠ spoken language), line 169 (craft grid "Ritual language survives vernacular change")
- **Question (verbatim):** Check the entry's evidence for Sumerian/Akkadian language contact and the separation of scribal language survival from spoken-language replacement; which dated text or scholarly passage supports the institutional coupling?

## Headline

Six scholarly fulltexts that **round 8 never touched** are retrieved and read at named printed pages: a Max Planck OA monograph chapter and its volume introduction, a Ca' Foscari OA book, a Finnish OA journal article, a South African OA volume chapter, and a Romanian OA journal article. Five legs of the entry row now each carry an independent 2016–2023 scholarly passage, including the one round 8 left unnamed: the **institution** that carries Sumerian after speech loss (temple lamentation office, scribal school, royal-epigraphic convention).

## Escalation beyond round 8 — verified non-overlap

Sweep (2026-10-17):

```
for t in Wagensonner mprl-series journal.fi foscari 'African Sun Media' \
         'van Dijk-Coombes' Viano Studies10Chap8 'Barber Sumerian'; do
  grep -ril "$t" reports/round-8/ reports/round-6 reports/round-7 | wc -l; done
```

→ **0 for every token.** Round 8's retrieved set (Wikipedia + Jagersma 2010 + Rubio/Woods/Michalowski in OIS 2 + Zólyomi 2000) is disjoint from everything below.

Strategies: (SS1) OpenAlex API metadata sweeps; (SS2) direct repository/publisher OA PDF retrieval; (SS3) whole-volume OA fetch (MPRL Studies 10, 543 pp.) for volume-level statements; (SS4) non-overlap sweep; (SS5) deeper-limit tracking of Sallaberger's OBO 160/3 argument.

## Retrieved sources (all sha256-pinned; scratch dir `~/.cache/kotodama-r9/`)

### S1 — Wagensonner 2018, "Sumerian in the Middle Assyrian Period" (MPRL Studies 10, ch. 8, pp. 225–296)
`https://mprl-series.mpg.de/media/studies/10/11/Studies10Chap8.pdf` · accessed 2026-10-17T20:49:37Z · 4,445,650 B · 74 pp. · sha256 `02839a70…`

- **p. 227:** "This paper deals with a period in which copying Sumerian scribal lore was still at its peak. Scholarly texts deriving from various sites in Babylonia reached its northern periphery." · "By the Middle Assyrian period, bilingualism fully infiltrated scholarly texts."
- **p. 233:** "When exactly the Sumerian language ceased to be used as vernacular is a cause of much debate and might have happened in various stages after the downfall of the Ur III Empire at the end of the third millennium BCE. … The decline of Sumerian is due further to the ever-increasing infiltration of Akkadian into the economic and daily life."
- **p. 234:** "But one has to bear in mind that the Old Babylonian texts are, strictly speaking, not a product of speakers of the Sumerian language." · "There is ample evidence that Sumerian at the end of the second millennium BCE was not just widely used in the scholarly tradition, but was given a pivotal role in the scribal sphere as well."
- **p. 235:** "In the Middle Assyrian period, the elite of Assur came into contact with a huge amount of literary and lexical texts, which originated in Babylonia."

### S2 — Braarvig & Geller 2018, volume introduction (MPRL Studies 10, pp. 7–10)
`https://mprl-series.mpg.de/media/studies/10/Studies10.pdf` · accessed 20:50:09Z · 5,290,603 B · 543 pp. · sha256 `592b4990…`

- **p. 8:** "…long after Sumerian ceased to be spoken but retained its status as the classical language of scholarship, incantations, and liturgy." · "Wagensonner argues that the processes of translating Sumerian into Akkadian contributed to the survival of Sumerian, even if orthographies no longer reflected the standard writings of earlier periods."

### S3 — Viano 2016, *The Reception of Sumerian Literature in the Western Periphery* (Antichistica 9, Ca' Foscari OA)
`https://edizionicafoscari.it/media/pdf/books/978-88-7543-417-5/978-88-7543-417-5.pdf` · accessed 20:49:27Z · 2,941,956 B · 428 pp. · sha256 `e2d8f8c3…`

- **p. 5 (Abstract):** "Sumerian is the most ancient language so far documented and remained for about three millennia the language of culture in Mesopotamia for its association with scribal education."
- **p. 23:** "After the fall of the Ur III dynasty and the collapse of its centralized administrative system, Sumerian went out of use as a spoken language by the 19th century, even though a certain level of proficiency was probably retained in scribal schools."
- **p. 24:** "In the second half of the second millennium B.C., Sumerian had been a dead language for over half a millennium, but it continued to function as a written language of scholarship and education in scribal circles, very much like Latin in the Middle Ages." · "Sumerian was the principal part of this training, because the study of cuneiform was always associated with Sumerian, even when it had gone out of use as a spoken language. A knowledge of Sumerian was indispensable for every scribe… because Sumerograms were used as logograms to write texts in all languages and in all text genres…"
- **p. 88 (dated witnesses):** "Unlike MB manuscripts, MA tablets are in some cases dated according to the līmu system. Eponyms go back to the reigns of different Middle Assyrian kings up to Tiglath-Pileser I. […] Imported Babylonian tablets date to a time spanning the Late Old Babylonian and Kassite periods…"
- **p. 104 (catalogue 2.1.4):** "Balaĝ-prayer to Enlil – KAR 375"; **pp. 109–112 (2.1.5):** "Prayer to Assur for Tukulti-Ninurta I", "A Praise Poem of Tukulti-Ninurta I".
- **p. 382 (dissemination table):** "16th – 15th Ḫattuša Monolingual Incantations in Phonetic Writing (CTH 800) | 15th – mid-14th Ḫattuša Sumerian Forerunner to the Hittite Prayers… KBo 19 98 | 14th – 13th Ḫattuša Assyro-Mitannian Incantations… | Emar A Prayer for a King | Ugarit Incantations (?)".

### S4 — Jordan & Fink 2023, "Scribal Identities, Renaissances, and Dead Languages" (Studia Orientalia Electronica 11(2): 30–52)
`https://journal.fi/store/article/download/129805/78658` · accessed 20:49:25Z · 591,441 B · 23 pp. · sha256 `191c417e…`

- **p. 31:** "After Sumerian had become an extinct language, knowledge of it became the third pillar of scribal self-consciousness (Høyrup 2018: 218)."
- **p. 32:** "…the kalûs (as they were called in Akkadian), who studied and copied ancient Emesal lamentations until the knowledge of cuneiform writing slowly faded away around the turn of the era."
- **p. 42:** "However, the Sumerian lamentations, which were performed on a regular basis in the temple and during rituals, continued to be transmitted until the first century bce or more."
- **p. 43:** "…the last guardians of the Sumerian tradition through their transmission of the large corpus of lamentations in Emesal."
- **p. 47:** "They describe school life in a non-Sumerian milieu where it was forbidden to speak Akkadian, and where a fluent conversation in Sumerian seemed to be the ideal for a well-educated scribe (Volk 2000: 13–14)."

### S5 — van Dijk-Coombes 2021, "The Use of Sumerian and Akkadian during the Akkadian Period" (in *Multilingualism in Ancient Contexts*, ch. 8, pp. 129–144, African Sun Media OA)
`https://af77305b-83ae-4652-be9e-daa5e1e5aec2.usrfiles.com/ugd/af7730_516413d8628b4857866b157e1a189d01.pdf` · accessed 20:49:28Z · 1,945,759 B · 18 pp. · sha256 `73a6ee96…`

- **p. 132:** "…the religious elite, including priests and temple personnel, as well as the safeguarders of 'culture'; the second – the secular elite, being royalty, governors, administrators, and military officers. […] these two groups used language or languages differently."
- **p. 133 (quoting Oppenheim):** "[b]ilingualism in Mesopotamia in specific periods and regions may be viewed either in terms of mutual intelligibility between Sumerian and Akkadian, in terms of teaching and research, or in linguistic preferences for specific themes and topics."
- **p. 140:** "During the Akkadian period, Akkadian, for the first time, becomes the language of official inscriptions. […] Frayne… the majority of royal inscriptions during the Akkadian period were written in Akkadian, 'a minority are known in bilingual (Sumerian and Akkadian) versions, and a handful are in Sumerian alone'."
- **p. 143 (with the Ešnunna E-sikil bilingual of Šulgi, RIME E3/1.1.2.27 / E3/2.1.2.28):** "The Akkadian inscription begins by recounting Šulgi's names and titles, while the Sumerian inscription begins by naming Ninazu. In the Akkadian period the ruler therefore becomes the primary focus of the royal inscriptions, rather than the deities… in the succeeding Neo-Sumerian period it has become a language convention."

### S6 — Sommerfeld 2022, "Sumerischer Widerstand gegen semitische Herrschaft" (Studia Antiqua et Archaeologica 28(1): 11–40)
`http://saa.uaic.ro/wp-content/uploads/SAA.2022.28.1.2.pdf` · accessed 20:51:47Z · 632,295 B · 36 pp. · sha256 `60744adc…`

- **p. 12:** "In sumerischen Quellen werden als Gegner häufig Personen, Städte und Regionen benannt, aber keine ethnischen Gruppen." (In Sumerian sources, opponents are usually named as persons, cities and regions, but not as ethnic groups.)
- **p. 13:** "Die Identifizierung der semitischen Bevölkerungselemente ist mit einigen Problemen verbunden, da der Zusammenhang zwischen der Sprachzugehörigkeit eines Namens und der/den Muttersprache(n) seines Sprechers mit Unschärfen behaftet ist." (Identifying Semitic population elements is problematic: the relation between a name's language and its bearer's mother tongue is fuzzy — the same logical caution as the entry's script ≠ speech guardrail, applied to onomastics.)
- **p. 13:** "Die von der sumerischen Mehrheitsgesellschaft geprägten und kontrollierten Stadtstaaten integrierten problemlos Minoritäten…" (The city states integrated minorities without difficulty.)

## Dated witnesses (all read this round)

| Witness | Source | Status |
|---|---|---|
| MA scholarly tablets at Assur dated by līmu eponyms to Tiglath-Pileser I | Viano p. 88 | read (scholarly fulltext) |
| Balaĝ-prayer to Enlil, Assur ms. KAR 375 | Viano catalogue 2.1.4, p. 104 | catalogue entry read; tablet not collated |
| Prayer to Assur for Tukulti-Ninurta I (reign-dated) | Viano catalogue 2.1.5, pp. 109–112 | catalogue entry read |
| Sumerian texts at Ḫattuša 16th–13th c.; Emar, Ugarit 14th–13th c. | Viano p. 382 | century-level dating from the author's table |
| Ešnunna E-sikil bilingual of Šulgi | van Dijk-Coombes p. 143 (RIME nos.) | discussed; RIME not opened |
| Emesal lament transmission into the 1st c. BCE, temple performance | Jordan & Fink p. 42 | read |
| Louvre AO 5477 (Rimush) | round-8 pointer | to-verify, sibling hunter's lane |

## Access failures (documented, not worked around silently)

| Attempt | Status |
|---|---|
| ZORA `…/151632/1/Sallaberger_Westenholz_1999_Mesopotamien.pdf` (+ landing page) | HTTP 200 but Anubis proof-of-work interstitial HTML (2,266 B); no PDF |
| Wayback `archive.org/wayback/available?url=…zora…pdf` | `{"archived_snapshots": {}}` |
| archive.org advancedsearch `Sallaberger Westenholz Mesopotamien` | numFound 0 |
| DOAJ `articles/Sallaberger Sumerian` | total 0 |
| Brill JANER 21 PDF | HTTP 403 |
| escholarship.org search (Crisostomo) | HTTP 202, 0 bytes |
| hcommons DOI 10.17613/m6746z | HTTP 403 |
| `hdl.handle.net/10831/31083` (Veldhuis 2016 grammar, ELTE) | HTTP 404 |
| `/tmp` scratch | tmpfs user quota full → 0-byte files; scratch moved to `~/.cache/kotodama-r9/` (no repo file affected) |
| Thureau-Dangin 1907, Königsinschriften (archive.org `diesumerischenun00thuruoft_djvu.txt`, 719,502 B) | fulltext downloaded; 1907 OCR too noisy for faithful quotation → no quote extracted, edition left to the primary-source hunter |

**Audit note for the round-9 runner (not a defect in this receipt).** The live `reports/round-9/run-validation.py` at sha256 `7dead4e60bdcaeb030f288647d7245b708571f926ee03b905407640d4bdedd66` mis-parses documented failures: `receipt_failures()` does `node.get(first_match(node, STATUS_FIELDS))`, which looks up the status **value** as if it were a key, so `status` is always `None` and `documented_failures` reads 0 for every receipt. Repro: `python3 -c "import importlib.util,json; spec=importlib.util.spec_from_file_location('v','reports/round-9/run-validation.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); d=json.load(open('reports/round-9/freshness/R9-F01b-receipt.json')); print(len(m.receipt_failures({'record':d})))"` → `0`, while the round-8 parser finds all 9 failure records in the same file. Rows whose only evidence is a documented access failure would be flagged as evidence-free. This shard's own row is unaffected (27 passages); the finding is for the R9-O16 author and the claim-F auditor.

## Support scopes kept separate

- **Passage-level (this shard):** `retrieved` — 6 sources, 27 quoted passages with own printed-page locators; every leg of the bounded row now has at least one independent scholarly passage retrieved this round.
- **Whole-claim:** still `supported` for the bounded row; line-41 hedge intact (Wagensonner "various stages"; Viano "by the 19th century"). No source retrieved this round contradicts the row.
- **Not established:** nothing on pronunciation reconstruction; no single vernacular-loss date; no tablet collation; Sallaberger's OBO 160/3 argument (behind Woods 2006) still unread in OA.

## Residual limits / deeper-limit receipt

1. Scholarly passages are not primary objects: KAR 375, the Tukulti-Ninurta prayer and the Šulgi bilingual are read through Viano's and van Dijk-Coombes's discussions.
2. Sallaberger's own Ur III spokenness discussion (OBO 160/3, 1999) is unretrievable in open access this round — exactly what remains unreadable is named above (Anubis interstitial; no Wayback snapshot; not in archive.org; not in DOAJ).
3. Round-8's recorded entry digest (`730e1be8…`) is stale versus the live file (`bf6c92f9…` = HEAD blob); downstream comparisons should use the live digest.

## Disposition

`unresolved` → **this shard's scholarly-fulltext leg satisfied**: six previously unread scholarly fulltexts retrieved and mined at named printed pages, adding the institutional-coupling passages the round-8 set did not name directly. Contribution to the reconciled disposition: supports movement of R9-R8-F01 to **partial-support-or-better on scholarly passages**; the primary/museum-object leg is a sibling hunter's assignment and the reconciled call belongs to the verifier/orchestrator. No raw label is rewritten here; no other shard's receipt is verified or promoted by this file.
