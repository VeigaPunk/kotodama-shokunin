# R8-F12 freshness receipt — winged-figure/Faravahar identification problem

- receipt: `reports/round-8/freshness/R8-F12-receipt.json` (machine record; this file is its human mirror)
- prior row: `R6-09-B` — disposition `partial-support`; raw round-6 worker label preserved: verdict `supported`, support_scope `partial` (`corpus/lessons/round-6-sources/09.json`)
- entry: `corpus/knowledge/civilizations/persia-achaemenid.md`, sha256 `e50e281be670eae31a101a61c5713c15ac8819bd1c2279a9eb515868172065d0` — **changed since the R6-09 ledger's before-hash** (`4edaa91a…`, round-6 integration); untouched by this shard (pure evidence refresh)
- question (verbatim from `reports/round-8/targets.json`): *Check the winged-figure/Faravahar identification problem against scholarly wording: separate contemporary caption, proposed Ahuramazda/fravashi/xvarenah identification and modern ethical feather/ring diagrams.*
- accessed-at for all retrievals: **2026-10-17** (single session; `date -u` at receipt-writing time read `2026-10-17T20:17:59Z`)

## Round-6 limits this receipt targets

1. Shahbazi 1974, "An Achaemenid Symbol, I" (AMI n.F. 7: 135–144) was unread — his argument was bibliographic only.
2. The 2008 Zoroastrian community essay quoted at entry line 83 could not be found (`tenets.zoroastrianism.com/farohar33.html` 404s).
3. No single ancient referent or feather/ring interpretation was established.

## Fresh retrievals (8; 7 carry substantive quoted passages, 1 is an explicit tertiary pointer)

| id | source | kind | locator | passage support |
|---|---|---|---|---|
| F12-R1 | [Boyce, "Fravaši," EIr X/2: 195–199 (Wayback 20261009104155)](https://web.archive.org/web/20261009104155/https://www.iranicaonline.org/articles/fravasi-/) | scholarly reference work (archived) | final paragraphs, print pp. 198–199; extraction line 14 | supports |
| F12-R2 | [Boyce, "AHURA MAZDĀ," EIr I/7: 684–687 (Wayback 20251119090540)](https://web.archive.org/web/20251119090540/https://www.iranicaonline.org/articles/ahura-mazda/) | scholarly reference work (archived) | Achaemenid-period section; extraction line 36 | supports |
| F12-R3 | [Gnoli, "FARR(AH)," EIr (Wayback 20251119085639)](https://web.archive.org/web/20251119085639/https://www.iranicaonline.org/articles/farrah/) | scholarly reference work (archived) | "Iconography," opening; extraction line 34 | supports (contested status) |
| F12-R4 | [de Jong, *Traditions of the Magi*, Brill 1997 — archive.org full text](https://archive.org/download/TraditionsOfTheMagiZoroastrianismInGreekAndLatinLiterature/ebooksclub.org__Traditions_of_the_Magi__Zoroastrianism_in_Greek_and_Latin_Literature__Religions_in_the_Graeco_Roman_World_113__djvu.txt) | peer-reviewed monograph (OCR) | ch. 4, pp. 299–300; fn. 65, 189; OCR lines 17484–17551 | supports |
| F12-R5 | [Jonker (Stellenbosch), "A Conflation of Divine and Royal Imagery?" (© 2020) PDF](https://www.sblcentral.org/API/ConferencePresentations/ConferencePresentation_53616.pdf) | scholarly-authored conference paper | §2 identification list, text lines 41–44, 53–58 | supports (attribution-level) |
| F12-R6 | ["The Significance of the Faravahar / Farohar Figure," Dr. H.P.B. Neku (ahuramazda.com)](https://www.ahuramazda.com/pages/farohar_figure_.html) | modern community/devotional text | ring sentence, extraction line 24; feathers, line 19 | supports (reception leg) |
| F12-R7 | [Eduljee, *Farohar/Fravahar Motif* (abridged), Zoroastrian Heritage Monographs 2013](https://www.heritageinstitute.com/zoroastrianism/reference/farohar_motif_eduljee_abridged.pdf) | community monograph | §I, p. 28; §J, p. 29; text lines 1487–1524 | supports (summary-level) |
| F12-R8 | [Achaemenica, "The Winged Symbol"](https://achaemenica.org/articles/the-winged-symbol) | tertiary curated site | identification-history paragraph | pointer-only, not load-bearing |

### Load-bearing passages

**F12-R1 — Boyce, "Fravaši" (fresh re-fetch of the round-6 main source).** Same article, retrieved again this round (HTTP 200, 400,626 bytes; effective snapshot `20261009104155`):

> There is no certain plastic representation of the fravaši s.

> Moulton accordingly (p. 260), rejecting the then prevailing Western interpretation of the Achaemenid winged symbol as that of Ahura Mazdā, identified it as the king's fravaši, and it is still generally regarded as a fravaši symbol by Zoroastrians. Strong arguments, however, have by now been put forward by Western scholars for its representing xᵛarənah …

Reading: the Ahuramazda reading was *the then prevailing Western interpretation* (a modern scholarly identification, not a caption); the fravaši reading is recorded and remains a living Zoroastrian reading; the xᵛarənah reading is backed by "strong arguments". None of the three is settled by an ancient caption.

**F12-R2 — Boyce, "AHURA MAZDĀ" (EIr I/7: 684–687; new this round).**

> No representations of Ahuramazda are recorded in the early Achaemenid period. (The winged symbol with male figure, formerly regarded by European scholars as his, has been shown to represent the royal xvarənah.)

Reading: same author, stronger tone — the xvarənah reading is presented as shown, not merely alternative. See calibration notes below.

**F12-R3 — Gnoli, "FARR(AH)" (new this round).**

> Iconography. The iconography of farr(ah)/xᵛarənah has been much debated (…). Not all the theories that have been proposed are convincing, for example, association with the winged sun disk, which appears frequently in Achaemenid art (Shahbazi, 1977, p. 199-200; idem, 1980; …), or with the ring that is shown in investiture scenes (…).

Reading: even the xvarənah↔winged-disk association is contested in the reference literature; the in-text "Shahbazi, 1977" resolves in this article's bibliography to "From Pārsa to Taxt-e Jamšīd," AMI n.F. 10, 1977, pp. 197–207 — a different article from the 1974 one. *Declared normalization:* HTML tag-strip spacing artifacts (raw: "Iconography . The iconography of farr(ah) / xᵛarənah - has been much debated") are normalized in the quote; no wording change.

**F12-R4 — de Jong, *Traditions of the Magi* (Brill 1997), pp. 299–300 (new this round; strongest Shahbazi locator).**

> Three interpretations have been offered for this figure: it was seen as the representation of the fravasi (guardian spirit) of the king, of Ahura Mazda himself, and of the royal khvarenah. It is at [OCR block break — the footnote block and the running head "300 CHAPTER FOUR" intervene in the archive.org text] present perhaps impossible to reach a consensus, but the argument advanced by A.Sh. Shahbazi and others, that the exact similitude between the figure in the winged disk and the king makes an interpretation of the figure as Ahura Mazda unlikely, appears to be very strong.

> (fn. 189) The suggestion that it represents khvarenah [OCR block interleaving — in the raw stream the unrelated fragment "Guests at a royal banquet" immediately precedes "was argued most fully"] was argued most fully by A.Sh. Shahbazi, 'An Achaemenid symbol I. A farewell to "Fravahr and Ahuramazda"', AMI 7 (1974) 135-144; 'An Achaemenid symbol II. Farnah "(God given) Fortune" symbolised', AMI 13 (1980) 119-147.

> (fn. 189 cont.) … Lecoq defends an interpretation of the figure as Ahura Mazda.

Reading: the three competing identifications named exactly; consensus "perhaps impossible"; Shahbazi's argument judged "very strong" but not declared settled; and the Ahuramazda reading has a scholarly defender (Lecoq 1984). *Declared normalizations:* line-break hyphenation rejoined ("argu-ment", "si-militude", "interpreta-tion") and the two page-block breaks marked above; all raw fragments verified by grep (see Commands). The OCR also contains misreadings elsewhere (e.g. "Grientalia", "JTproastrianism").

**F12-R5 — Jonker 2020 conference paper (new this round).** Identification list, two adjacent table rows quoted verbatim: `"fravashi (spirit) of the king" (Unvala 1950)` / `"royal khvarenah/glory" (Shahbazi 1974)` — the same list also carries `"the deity Ahura Mazda" (Root 1979: 169–176)`. Plus Garrison 2009: "The most perplexing and often-debated question in the study of religious iconography of the Achaemenid Persians is the identification of the figure in the winged symbol." And Garrison 2009 (mid-block, no quotation marks at that point in the source): "While its specific divine signifier may have varied with context, its political content is without question: the legitimacy of specifically Achaemenid rule." *Declared normalization:* one hyphenated line break rejoined ("le-gitimacy").

**F12-R6 — Neku page (live mirror, reception leg).** Exact devotional wording the entry quotes at line 83:

> The other hand holds a ring. Some interpreters consider that as the ring of covenant, representing loyalty and faithfulness which is the basis of Zarathustra's philosophy.

> There are two wings in two sides of the picture, which have three main feathers. These main feathers indicate three symbols of good reflection, good words, and good deed …

**F12-R7 — Eduljee 2013 (summary-level).** "In the first article, An Achaemenid Symbol (Part) I, A Farewell to Fravahr and Ahuramazda, Shahbazi noted why he felt the farohar motif could not represent either the farohar/fravahar or Ahura Mazda." Plus the modern-reception note: the names "farohar"/"fravahar" are "now engrained in popular culture". Non-peer-reviewed community work with a declared advocacy stance — used as relay only.

## Access failures / limits (documented, with attempted command and status)

- **Live Iranica** (`/articles/fravasi-/`, `/articles/faravahar`) → `curl` HTTP **403**, 5,476 bytes each. Resolved via Wayback snapshots (R1–R3).
- **The entry's cited 2008 essay URL** (`tenets.zoroastrianism.com/farohar33.html`) → live HTTP **404** (13 bytes) on both domains; Wayback replay HTTP **404** for www/non-www/parsizoroastrianism variants; Wayback **CDX API HTTP 503** ("Internet Archive: Temporarily Offline") during the window. → original URL unresolved (`to-verify`); exact wording located on a live mirror instead (R6); mirror↔2008-essay identity not proven.
- **Shahbazi 1974 article itself** → no open digital copy located (WebSearch sweep + candidate-host probes; archive.org search offline in-window). Still unread; accessed only via R4/R5/R7 relays. `to-verify`.
- **MDPI** `2571-9408/7/1/1` (HTML and /pdf) → HTTP **403** (bot block); not used.
- **naturalisms.org Skjærvø 2014 mirror** → HTTP **404** (dead link); not pursued.
- **dokumen.pub** essay page → HTTP **403**; not needed.
- **timetravel.mementoweb.org** → curl exit 6, could not resolve host; abandoned.
- **archive.org /stream/ wrapper** → HTTP 200 but HTML wrapper with no book text; resolved via the direct `/download/` djvu.txt route (HTTP 200, 1,315,868 bytes).

## Passage support vs whole-claim support

- **Passage support:** 7 of 8 records carry substantive quoted passages with named locations (R8 is an explicit pointer-only record). Requirement was ≥1 per receipt / ≥8 across the 15 residuals — this receipt's share is satisfied.
- **Whole-claim support: `supported-with-residue`.** Every leg of the R6-09-B bounded claim now carries a fresh located passage: the three competing identifications and their contested status (R1/R3/R4/R5), the absence of a contemporary caption and the modern provenance of the readings (R2/R4), and the modern devotional feather/ring wording (R6).
- **Residue (not resolved):**
  - Shahbazi 1974/1980 themselves still unread — his argument's details rest on de Jong's appraisal and secondary relays. `to-verify`.
  - Original 2008 essay URL dead (404 live + Wayback, CDX 503) — mirror identity unproven. `to-verify`.
  - No object, relief or seal inspected; the ancient referent remains contested by the sources' own account.
  - Boyce, *Zoroastrianism* II and Boyce & Grenet III (the works Boyce cites for the xvarənah arguments) not opened.
- **Calibration notes for the parent (entry not edited here):**
  1. Retrieved scholarly wording is not uniform: Boyce (R2) writes "has been shown to represent the royal xvarənah" (settled tone), while Gnoli (R3) lists the winged-disk association among theories "not all … convincing" and de Jong (R4) says consensus is "perhaps impossible". The entry's "contested" framing (lines 79–81) is safe; line 80's "Important scholarly alternative" understates Boyce's own confidence — a calibration choice, not an error.
  2. The Ahuramazda reading is a defended scholarly position (Lecoq 1984, per R4 fn. 189), consistent with entry line 79.
  3. No retrieved passage attests an ancient caption; the line-84 absence claim is a sweep result (absence-of-attestation), not proof of non-existence.

## Commands

```
sha256sum corpus/knowledge/civilizations/persia-achaemenid.md   # e50e281b… (!= R6 ledger before-hash 4edaa91a…)
curl -sSL -A '…research-fetch' -o boyce-fravasi.html 'https://web.archive.org/web/20261009104155/https://www.iranicaonline.org/articles/fravasi-/'   # HTTP 200 400626
curl -sSL -A '…research-fetch' -o ir-ahura.html      'https://web.archive.org/web/2025/https://www.iranicaonline.org/articles/ahura-mazda'          # HTTP 200 399202
curl -sSL -A '…research-fetch' -o ir-farrah2.html    'https://web.archive.org/web/2025/https://www.iranicaonline.org/articles/farrah'              # HTTP 200 435196
curl -sSL -A '…research-fetch' -o magi.txt 'https://archive.org/download/TraditionsOfTheMagiZoroastrianismInGreekAndLatinLiterature/…_djvu.txt'      # HTTP 200 1315868
sed -n '17484,17551p' magi.txt                                  # de Jong pp. 299–300 + fn. 189
curl -sSL -A '…research-fetch' -o sbl-conflation.pdf 'https://www.sblcentral.org/API/ConferencePresentations/ConferencePresentation_53616.pdf'     # HTTP 200 227499
pdftotext -layout sbl-conflation.pdf sbl-conflation.txt         # 263 lines
curl -sSL -A '…research-fetch' -o am-farohar.html    'https://www.ahuramazda.com/pages/farohar_figure_.html'                                            # HTTP 200 19428
curl -sSL -A '…research-fetch' -o eduljee.pdf        'https://www.heritageinstitute.com/zoroastrianism/reference/farohar_motif_eduljee_abridged.pdf'    # HTTP 200 3880382
python3 reports/round-8/run-validation.py                       # 20:25Z: exit 1, acceptance_checks_passed False; claim F FAIL lists 'missing receipts: R8-F02' + issues for F01/F04/F05/F07/F09/F11 — NO R8-F12 issue reported (20:19Z run aborted earlier with KeyError 'R8-F02')
grep -c 'present perhaps impossible to reach a consensus, but the argu-' magi.txt                 # 1 — de Jong OCR fragment (sentence straddles a block break)
grep -c 'was argued most fully by A.Sh. Shahbazi' magi.txt                                       # 1 — fn. 189 fragment, same interleaving
grep -c 'Iconography \. The iconography of farr(ah) / xᵛarənah - has been much debated' ir-farrah2.txt   # 1 — raw spacing artifacts
grep -o 'the le- ' sbl-conflation.txt                                                            # 1 — hyphenated line break rejoined
python3 -c "import json;json.load(open('reports/round-8/freshness/R8-F12-receipt.json'))"        # parses; 20 quoted passages — 17 verbatim/normalization-aware probes matched, 3 declared-normalization with raw fragments verified above
```

Scope: entry untouched; raw round-6 label preserved; no canon decisions; no git commit. Scratch artifacts kept in `/tmp/r8-f12-scratch/` so only the two assigned receipt files are written into `reports/round-8/freshness/`. Handoff stays with the orchestrator.
