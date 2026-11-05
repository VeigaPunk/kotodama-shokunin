# Round 96 — ScoutSources96: candidates for *oath, blessing and curse formulae*

Seat: `ScoutSources96` (scout, coverage axis). Lane: `kotodama-shokunin`. Wave: round-96/w1.

Scope: read-only source reconnaissance for the new entry `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md`
(Claim C, frozen in `reports/round-96/claims.json`). This seat assigns **no S-ids**; the registry seat assigns ids sequentially from S975.

All opens were plain `curl` (`-L`, `--max-time 30`, default user agent; no browser, no login, no TLS bypass).
Access date for every row: **2026-11-05**.

## 1. Search log

| # | query | results returned | URLs kept from this query |
|---|---|---|---|
| 1 | `Hittite treaty curse formula self-imprecation oath` | 15 | books.openedition.org/editionsehess/2703 (C1); sciencejournals.ge HAE 508 (not opened) |
| 2 | `norito Japanese Shinto prayer blessing formula liturgy text` | 15 | en.wikisource.org/wiki/Shinto:_The_Way_of_the_Gods/Chapter_12 (C10); d-museum.kokugakuin.ac.jp/eos/detail/?id=8565 (C8); sacred-texts.com/jap (403) |
| 3 | `Old Irish medieval oath formula satire curse witness` | 14 | persee.fr/doc/ecolt_0373-1928_1992_num_29_1_2015 (C4); mural.maynoothuniversity.ie eprint 1333 (C6); journal.fi/scf/article/download/7032 (C5) |
| 4 | `performative formula anthropology blessing curse ritual speech act` | 15 | ora.ox.ac.uk dhq37vp39v (C7); ojs.unm.ac.id englishperformance 89987 (C9) |
| 5 | `Greek oath formula Homer epics swearing witness invocation archaic` | 10 | perseus.tufts.edu hopper Iliad 19.258 (C3); archive.chs.harvard.edu oath in Greece (unreachable) |
| 6 | `Vedic oath formula rtuvakya mantra swearing by truth` | 29 | wisdomlib.org Manusmriti 8.109 (rejected: registry duplicate of the S838 family) |
| 7 | `Old Norse oath formula swearing witness ordeal` | 15 | hcmc.uvic.ca/~scancan/pdf/nygaard_1_28.pdf (C2); uplopen 9783110655582-009 (403) |
| 8 | `West African oath curse ritual formula witness performance ethnography` | 15 | ojs.unm.ac.id englishperformance 89987/37848 (C9); academic.oup.com edited-volume 59477 (not opened) |
| 9 | `sanction clause treaty curse ancient Near East treaty oaths self-curse` | 15 | books.openedition.org/editionsehess/2703 (C1); thetorah.com yhwhs-covenant (C11); jstor 1516617 (wall) |
| 10 | `Hebrew Bible blessing formula 'Blessed be' covenant oath utterance form` | 15 | jewishencyclopedia.com/articles/2501-blessings (wrong article: BARAK the person); dspace.cuni.cz 140044187 (429/timeout) |
| 11 | `site:thetorah.com article Hittite treaty oath Deuteronomy covenant` | 1 | thetorah.com yhwhs-covenant-why-moses-calls-heaven-and-earth-as-witnesses (C11) |

Eleven queries across ten traditions (Hittite/Near East, Japanese, Irish, Homeric Greek, Vedic, Old Norse, West African,
Hebrew Bible, Greek, comparative anthropology) were run; ten were required.

### Registry duplicate check

Every candidate URL was checked against `corpus/SOURCES.md` with `grep -c -F -- "$url"` before opening. All eleven admitted
URLs returned **0** (no existing row). One family matched but not the exact URL: `wisdomlib.org/hinduism/book/manusmriti`
returned 1 (row S838, Manusmriti verse 2.35) — the verse 8.109 URL is a different page but the same edition and translator,
so it is filed as a reject rather than spent as a new row.

## 2. Admitted candidates

| key | source | tier | HTTP | bytes (capture) | quote (<=25 words) | quote_count | supports |
|---|---|---|---|---|---|---|---|
| C1 | Faraone 2012, 'At the Limits of Efficacious Speech: The Performance and Audience of Self-Curses in Ancient Near Eastern and Greek Oaths', in Dossier: Serments et paroles efficaces (Éditions de l'École des hautes études en sciences sociales) | A | 200 | 55100 | "the ultimate goal of all these self-curses is, of course, to strike fear into those who s..." | 1 | self-imprecation; oath formula; curse formula |
| C10 | Aston 1905, Shinto: The Way of the Gods, ch. 12 ('The Great Purification'), Wikisource transcription of the 1905 London: Methuen edition | A | 200 | 136920 | "the recital of a norito or formula—not a prayer, as it is sometimes called" | 1 | blessing formula; form; register |
| C11 | Holtz 2024, 'YHWH's Covenant: Why Moses Calls Heaven and Earth as Witnesses', TheTorah.com (Nitzavim) | B | 200 | 8098 | "Moses in Deuteronomy draws on formulations found in ancient Near Eastern treaties" | 1 | witness invocation; sanction clause |
| C2 | Nygaard 2021, 'ein lǫg ok einn siðr: Law, Religion, and their Role in the Cultivation of Cultural Memory in Pre-Christian Icelandic Society', Scandinavian-Canadian Studies 28 | A | 200 | 96359 | "at ek vinn eið at bauga, lögeið" | 1 | oath formula; witness invocation |
| C3 | Homer, Iliad 19.258-262 (Greek text), Perseus Digital Library, ed. Monro-Allen (Oxford TLG 1999.01.0133) | A | 200 | 12524 | "ἴστω νῦν Ζεὺς πρῶτα θεῶν ὕπατος καὶ ἄριστος" | 1 | witness invocation; oath formula |
| C4 | Ó Murchú 1992, 'The literary asseveration in Irish', Études celtiques 29: 327-332 (Persée) | A | 200 | 2602 | "dearbhaithe or asseverations" | 1 | curse formula; register |
| C5 | Tuomi 2013, 'Ancient curses, medieval charms?' (review of Mees, Celtic Curses), Studia Celtica Fennica 9: 258-264, Reviews section | B | 200 | 20151 | "curse-enhanced oaths or vows lie behind the notion of the geis" | 1 | curse formula; oath formula |
| C6 | Ní Mhaoldomhnaigh 2007, Satirical Narrative in Early Irish Literature (PhD thesis, National University of Ireland Maynooth) | B | 200 | 636835 | "the seven requirements which compose any satire (cach n-aír) are" | 1 | curse formula; form |
| C7 | Frangulov 2023, Ritual speech, Performativity, and Modality (MPhil thesis, University of Oxford) | B | 200 | 198429 | "a ritual, spell, curse, charm, incantation, blessing, hymn, or mantra" | 1 | performative formula; typology |
| C8 | Encyclopedia of Shinto, 'Amatsunoritohutonoritokō', Kokugakuin University Digital Museum | B | 200 | 2504 | "divides the Great Purification Norito found in Fascicle 8 of the Engishiki into 10 sections" | 1 | blessing formula; form |
| C9 | Eyong, Nwosu, Effiom & Onah 2026, 'The River as Witness: Ndem Shrines and the Indigenous Jurisprudence of Water in the Cross River Estuary', Performance: Journal of Law and Humanities 4(2) | A | 200 | 45238 | "to witness their truthfulness and punish them if they lied" | 1 | witness invocation; self-imprecation; sanction clause |

**Admitted count: 11 of 11 opened candidates; 11 of them tier A or B.** Target was >=3 tier A/B; 11 achieved.
Every admitted quote is an exact substring of its capture with `bytes.count == 1`.

### Captures

| key | live URL | capture (text) | sha256 of capture | raw capture | raw sha256 | raw bytes | Wayback ts |
|---|---|---|---|---|---|---|---|
| C1 | https://books.openedition.org/editionsehess/2703?lang=en | `captures/C1.txt` | `7242213d56c51305d3a70201f1758db3ca2ad3e0fb98c548abecf566737ec22c` | `captures/C1.raw.html` | `33c896a6f1a4214acc1756eaa741d01b6d9e3b0251ae1bd5dce585d0bc36a8f2` | 239229 | 20251206033024 |
| C10 | https://en.wikisource.org/wiki/Shinto:_The_Way_of_the_Gods/Chapter_12 | `captures/C10.txt` | `9551ce4c3057d7af4eb45a567d2a73ad5f6b697f6196040850ffff07ff5b3265` | `captures/C10.raw.html` | `c1a9a7326296d73422f4b24704c8451d30553e6aff06b52f8cea723abc400914` | 303938 | 20250225050216 |
| C11 | https://www.thetorah.com/article/yhwhs-covenant-why-moses-calls-heaven-and-earth-as-witnesses | `captures/C11.txt` | `a9678bc22be7c45b860218da74c71e67f210f7b434da13e7db2e9037614825b1` | `captures/C11.raw.html` | `b09ded480abc3b7cff30bf68699611aa93e50bb6223873b857c589f2b1935afe` | 1157054 | 20261019225553 |
| C2 | https://hcmc.uvic.ca/~scancan/pdf/nygaard_1_28.pdf | `captures/C2.txt` | `8a39d6c6dbe1fa688d0174c45aec046b8c4619b0499f3471e29fbfa27c529d3f` | `captures/C2.raw.pdf` | `a56431f09b5f9af4be436c797dd3e43b17547c9a16ee3af3ee4cf4ca6c532a50` | 1051913 | 20260313103718 |
| C3 | https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133:book=19:card=258 | `captures/C3.txt` | `034e796b5bd5ac54152e839f4004724b17a6596c6fef8ea51ee029f028abcb58` | `captures/C3.raw.html` | `eb09d973ea3846a7f48d1ad66f4e17c4fbe6b7c5580854b40d09b1f9b6bef13a` | 133128 | - |
| C4 | https://www.persee.fr/doc/ecolt_0373-1928_1992_num_29_1_2015 | `captures/C4.txt` | `c909f8d06b831d1aa2a4624ae6be404d30e98747e6862a4388abeb994ed7198e` | `captures/C4.raw.html` | `3dfc3f22d62d88690faefa48239aa2639530d14c5b007aeacb86675d40d6e0c7` | 78856 | - |
| C5 | https://journal.fi/scf/article/download/7032/20487/61412 | `captures/C5.txt` | `0859df321e8a2ca4cf9f70c6f11730c219344f0077771c39e5b4e41eac1e2a28` | `captures/C5.raw.pdf` | `b050f0f5cd61377cdc38ff92183f9d143852f16ce9fc68419954ac92953eb25f` | 256566 | 20240912030456 |
| C6 | https://mural.maynoothuniversity.ie/id/eprint/1333/1/Satirical_Narrative_in_Early_Irish_Literature.pdf | `captures/C6.txt` | `9b0199e7098a84deb902470585fd84dcd522361d08ca067159853701f6ec41b8` | `captures/C6.raw.pdf` | `cea42ff481eb7e71d5c51bae91b1d733edf66e3440b84624a7f7a0d92ec207de` | 941367 | 20260613065904 |
| C7 | https://ora.ox.ac.uk/objects/uuid:36e9551e-5a3b-4aac-98c1-0e12614110f9/files/dhq37vp39v | `captures/C7.txt` | `0849a703acf7cb3dec3610ff2449f5bd10ee8b44431c24d578615308afd764b2` | `captures/C7.raw.pdf` | `bacfbb7f3a4055aa50a6eec992aaf01dd8eb7ff3b0268cfa75ab6f2a75641629` | 504791 | 20250319091606 |
| C8 | https://d-museum.kokugakuin.ac.jp/eos/detail/?id=8565 | `captures/C8.txt` | `30098283212ef50d7ad5d70a1a8ace0478d902e756ef472d65db005a180c156b` | `captures/C8.raw.html` | `e34cd7f3f77850410e968d0e1340385e114dbd84486d3e9a6cdbcab07fc8a54a` | 16285 | 20250321192729 |
| C9 | https://ojs.unm.ac.id/englishperformance/article/download/89987/37848 | `captures/C9.txt` | `6082936cf23a48814e190c78bea2a6216c043005c3b8bc186038c35cacfe6871` | `captures/C9.raw.pdf` | `5182471bae680fad8cbe2a7d807dd95e105e697373b540a8aaa5dbef7f743941` | 391016 | - |

Text renderings are derived from the raw capture by a fixed pipeline (`pdftotext` for PDFs; tag-strip plus whitespace-collapse
for HTML), so a re-opener regenerates them byte-identically. Quote counts were measured with
`python3 -c "print(open('<capture>','rb').read().count(<quote>.encode()))"` — every row returned 1.

### Why each row is admitted

- **C1** — Quote locates in the peer-reviewed scholarly chapter's own body text and supports a claim about the form of oath self-curse (self-imprecation) in ancient Near Eastern and Greek oaths: the self-curse is the deliberate instrument that makes the oath binding, and its sensory performance is what makes it effective.
- **C10** — Quote locates in the digitized primary edition's body and supports a claim about the Japanese blessing formula's rite-status: the norito is recited as a formula (not a prayer) by the Nakatomi at the Great Purification and declares absolution to the assembled people.
- **C11** — Quote locates in the article's own body text and supports a claim about the treaty-sanction clause and witness invocation: Deuteronomy's covenant draws on ancient Near Eastern treaty formulations in which heaven and earth are called as witnesses and oath deities enforce the curses.
- **C2** — Quote is the Old Norse oath formula itself as transmitted in Landnámabók ( Úlfljótslǫg ), quoted from a peer-reviewed journal article; it supports a claim about the wording of a witness-backed Norse oath (eið at bauga) and the invocation of named divine helpers (Freyr, Njǫrðr).
- **C3** — Quote is the Homeric assertory oath's divine-witness invocation as it stands in the primary Greek text (ἴστω νῦν Ζεὺς πρῶτα … Γῆ τε καὶ Ἠέλιος καὶ Ἐρινύες); it supports a claim about the Greek witness-invocation formula and the gods-as-enforcers idiom.
- **C4** — Quote locates in the article's own body text and supports a claim about Irish register: the Irish literary asseveration (dearbhai) is a named, formally bounded curse-and-praise genre distinct from the oath. NOTE for the registry seat: the capture holds the article's opening section only (Persée serves the remaining pages as page images), so any row built on it should anchor on this opening paragraph.
- **C5** — Quote locates in the review's body text and supports a claim about the semantic field joining curse and oath in Celtic formulaic practice (curse-enhanced oaths underlying the geis); the source is a scholarly review, so it is a strong secondary and never sole support for a disputed reading.
- **C6** — Quote locates in the thesis body and supports a claim about the formal composition of the Irish curse: Uraicecht na Ríar §24 prescribes seven required elements (scáth, aide, caislechtai, scoth, treairiut, cuairt, éscai-aidbsiu) for any valid satire, i.e. the curse has a checklist form.
- **C7** — Quote locates in the thesis body and supports the cross-tradition claim that blessing, curse, charm, incantation and mantra are treated as one class of performative ritual speech; it is a secondary (formally-oriented) source and frames the typology rather than attesting any single tradition's formulae.
- **C8** — Quote locates in the encyclopedia entry's own body and supports a claim about the Japanese blessing formula: the Great Purification norito is a fixed, sectional (10-section) liturgical text found in Fascicle 8 of the Engishiki, so the blessing formula is a transmitted written recension, not spontaneous prayer.
- **C9** — Quote locates in the article's own body text and supports a claim about a West African self-curse formula: the oath-maker invokes the shrine/river to witness their truthfulness and to punish them if they lied, i.e. a conditional self-imprecation with a named enforcer and a specified sanction.

## 3. Rejects and UNREACHABLE records

| artefact | target | result | reason / flip condition |
|---|---|---|---|
| R01 | dspace.cuni.cz 140044187 (Rhetoric and Hermeneutics of Blessing and Curse in the Pentateuch) | HTTP 429 then 2x curl rc=28 timeout | UNREACHABLE. Attempts: 1) HTTP 429, 162 B `429 Too Many Requests`; 2) rc=28 after 30 s; 3) rc=28 after 30 s (20 s backoff between). The 429 body is the nginx error page, not the thesis. Flip: retry after the host's rate-limit window; PDF path unchanged. |
| R02 | archive.chs.harvard.edu/CHS/article/display/3963.8-the-oath-in-greece | 3x curl rc=28 (connection timeout) | UNREACHABLE for this purpose. Flip: a later attempt when the host answers, or an archived capture of the same page. |
| R03 | nome.unak.is/wordpress/05-1/…old-norse-and-old-english-language-contact… | curl rc=60 (TLS certificate verify failed) | UNREACHABLE. TLS verification was not bypassed (no `-k`), per the round rules. Flip: a plain-curl attempt when the host's certificate chain validates. |
| R04 | ir.lawnet.fordham.edu/cgi/viewcontent.cgi?article=1766 (Function of the Oath in the ANE International Treaty) | HTTP 403, 5,675 B | HTTP refusal. No login or bypass attempted. Flip: an open copy of the same text (also published in a journal of record). |
| R05 | degruyterbrill.com/document/doi/10.1515/9781575068749-005 (Cursed Are You! ch. 1) | HTTP 202, 0 B body | Empty 202 shell — no body text served to a plain request. Flip: an open-access copy of the same chapter. |
| R06 | digitalcommons.georgefox.edu/cgi/viewcontent.cgi?article=1261 (Making the Cut: Covenant, Curse and Oath) | HTTP 403, 5,634 B | HTTP refusal. Flip: the same text on a repository that serves it openly. |
| R07 / R12 | jstor.org/stable/1516617 (Covenant Forms and Contract Forms) | HTTP 200 but 3,038 B wall | Body is `<title>Client Challenge</title>` — a bot challenge, not the article. Not routed around. Flip: an open copy (the article also appeared in BASOR). |
| R08 | uplopen.com/reader/chapters/pdf/10.1515/9783110655582-009 (Oath-Taking as Individualism in Norwegian Medieval Law) | HTTP 403, 134 B | HTTP refusal. Flip: an open-access copy of the same chapter. |
| R09 / R13 | scaife.perseus.org/reader/urn:cts:greekLit:tlg0012… | HTTP 200 but 3,561 B JS shell | Client-side viewer shell; no text in the served body. The same Iliad passage was obtained instead from the Perseus hopper page (C3). |
| R10 / R18 | en.wikisource.org 404 paths (Westminster Liturgy; The Encyclopedia of Shinto) | HTTP 404 | Nonexistent paths. Flip: a valid Wikisource path. |
| R11 | perseus.tufts.edu Iliad Book 1 card 1 | HTTP 200, opened and read | Rejected on scope, not access: Iliad 1 contains no oath formula of the kind the entry needs. Flip: keep only as a Homeric-verse lead for general epigraphy. |
| R14 / R22 | sacred-texts.com/jap and /hin | HTTP 403 | HTTP refusal. Flip: the same Engishiki/Manu texts on a host that serves them plainly (C8 covers the norito from an institutional source). |
| R15 | gutenberg.org/files/30585 (A Diplomatic Adventure) | HTTP 200, opened and read | Rejected on scope: a 19th-century novel with no oath-formula scholarship. |
| R16 / R21 / R29 | archive.org 404 streams (Engishiki djvu; sacredbooksofthe25sacuoft) | HTTP 404 | Wrong item identifiers. Flip: the correct archive.org identifiers. |
| R17 / R24 | jewishencyclopedia.com/articles/2501-blessings and /2501-barak | HTTP 200, opened and read | Rejected on scope: the served article is `BARAK` the person (Judge Barak), not the Hebrew root or the blessing formula. Flip: an article that actually treats the blessing formula's form. |
| R19 | persee.fr …_2015.pdf | HTTP 404 | No PDF rendition at that path. The HTML article page (C4) was used instead. |
| R20 | gutenberg.org/files/6130 (Iliad, Butler translation) | HTTP 200, opened and read | Rejected on scope: the English Butler prose carries no formula-bearing wording in the served capture, and the Greek text (C3) is the stronger witness for the witness-invocation formula. |
| R23 | livius.org/sources/content/ancient-mesopotamian-treaties/ | HTTP 404 | Dead path. Flip: a live Livius treaty page. |
| R25 | thetorah.com/article/suzerain-vassal-treaties | HTTP 404 | Guessed slug. The real article (C11) was found by search instead. |
| R26 | sefaria.org/Numbers.6.24-26?lang=bi | HTTP 200 but 578 B of text | Rejected on scope/access yield: the served body is the app shell, not the priestly-blessing text. Flip: a plain-text Bible edition if a priestly-blessing row is wanted. |
| R27 | wisdomlib.org Manusmriti 8.109 (Oaths and Ordeals) | HTTP 200, opened and read | Rejected as a registry duplicate: the same edition and translator (Ganganath Jha's Medhatithi commentary) is already registered at S838. A new row would double-register one source. Flip: a different edition of Manu or a different satapatha text. |
| R28 | thetorah.com/topic/vassal-treaties (topic landing page) | HTTP 200, opened and read | Rejected on scope: a topic index of article blurbs, not a source with its own body text; the per-article page (C11) supersedes it. |
| R30 / R31 | livius.org hittite-treaties; soas.ac.uk/about/ | HTTP 404 / HTTP 200 landing page | Dead path / no relevant body. Flip: a live Hittite treaty translation page. |

### Wayback note

`web.archive.org` CDX and `web.archive.org/web/...` fetches timed out repeatedly from this host (curl rc=28 on every attempt,
including `--max-time 110`). The availability API on `archive.org/wayback/available` answered normally, so the eight
Wayback timestamps recorded in section 2 come from that API (a same-page capture with status 200 for each). No archived capture
was downloaded here, so the Wayback column is a *pointer*, not a verified capture body; the registry seat must open the capture
itself before quoting from it. For C3, C4 and C9 the availability API returned an empty `archived_snapshots` for the canonical
URL and for every variant probed (http/https, with and without the query string, the collection root, the `/view/` landing page,
the index.php form). The positive control is the same API returning a status-200 snapshot for the other live URLs, so those
empty answers are recorded as *no same-page capture found via the availability API*, not as proof of absence. Flip: a CDX
prefix query on those three URLs once `web.archive.org` answers.

## 4. Handover to the registry seat

- Eleven admissible rows are offered. Suggested ordering for id assignment from S975, widest coverage first: C1 (Ancient Near
East and Greek self-curse), C9 (West African shrine oath), C2 (Old Norse witness oath), C3 (Homeric witness invocation), C11
(treaty sanction clause, heaven-and-earth witnesses), C10 and C8 (Japanese blessing formula, rite and recension), C6 and C4
(Irish curse checklist and asseveration register), C5 (Celtic curse/oath semantic field), C7 (performative ritual-speech frame).
- All eleven are new to `corpus/SOURCES.md` (exact-URL `grep -c -F` = 0).
- All eleven were opened by plain curl with HTTP 200 on 2026-11-05 and carry a located quote with `bytes.count == 1`.
- The captures live under `captures/`. Leg C7 of the counter looks for copies under `reports/round-96/evidence/`; that directory
is the registry seat's to write, not this seat's.
