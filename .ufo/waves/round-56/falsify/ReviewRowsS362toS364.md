# ReviewRowsS362toS364 — Kotodama round 56 FALSIFY wave

Verdict: **CARRIED** — all four checks pass for rows S362, S363, S364. No defect found in this slice. Two residual observations (both outside this slice) noted at the end.

Method: re-opened every row URL by ordinary means fresh on 2026-10-22 (plain curl, no browsers, no challenges). Host spacing respected: archive.org requests spaced 10 s, eprints/Openedition separate hosts. Files kept under /fast/scratch/hyaku/kotodama-r56-falsify/KotodamaR56.ReviewRowsS362toS364/. No tools installed (curl, python3, pdftotext already present) — no install record needed.

## S362 (Bentley 1895 Appendix, Internet Archive dictionarygramma00bentuoft)

- Re-open: djvu.txt HTTP 200, 969,065 bytes (matches row), 43,241 lines; page-level XML also fetched (11.84 MB); page images n7, n8, n28, n29 fetched and read.
- S362 anchor quotes — CARRIED, all verbatim, all <= 25 words, at stated locators:
  - Preface p. vi "simba appears as ximba under X in the Dictionary, and as simba under S in the Appendix" — image n7 (printed "PREFACE vi" header) reads it word for word; 17 words.
  - Preface p. vi "pronounce s and z before i as sh and j" — image n7, verbatim (10 words).
  - Preface p. vii "This is a very objectionable use of nkisi, fetish." — page vii, verbatim (9 words).
  - Preface p. vii "Anquissi (-ankisi, fetish) is used for holy, sacred" — page vii, verbatim. Note: OCR text (djvu.txt and XML) reads "-aukisi", but the printed page image shows "-ankisi" clearly; row quote matches the printed page, OCR is the noisy one (8 words).
  - Preface p. vii "untotela (p. 39) used for majesty, so that Ntotela is not simply a dynastic name" — page vii, verbatim (15 words).
  - p. 739 s.v. Currency (image n28, printed "( 739 )"): "The oldest currency we can hear of was a mat of palm-fibre cloth" (13 words); "They were replaced about 1830 by red glass olive beads, mbembe, 2" (12 words); "gave way in about 1863 to a hexagonal blue pipe glass bead" (12 words) — all verbatim on the printed page.
  - p. 744 s.v. Dowry (printed "( 744 )"): "Dowry paid for a wife, n., nzimbu (pl. 2) or mbiya (sing. 2) or nkanda (4) a longo." — verbatim (18 words).
  - p. 747 s.v. Epilepsy (printed "( 747 )"): "Epilepsy, n., nkisi (4) a teke (Bake); nsansi, 4 (fits of all kinds)." — verbatim (13 words).
  - p. 835 s.v. Fulula (printed "( 835 )"): "fulula 0 nkisi (4), to propitiate a fetish for some broken restriction (konko) or reinstate it" — verbatim (16 words).
- Gate quote (Preface p. vi) — CARRIED, verbatim, 17 words.
- Tier — CARRIED. Tier A fits QUALITY criterion 6: the row is the primary source for its own scope (same compiler's appendix volume), not a publisher description or abstract.
- Citing sentences in kongo-kingdom.md — all CARRIED at stated strength:
  - line 57: "notes that *untotela* was used for majesty (S362, Preface p. vii)" — page vii: "untotela (p. 39) used for majesty"; carried.
  - line 83: "Bentley calls the older missionaries' use of *nkisi* for 'holy' a very objectionable use (S362, Preface p. vii)" — page vii: "Anquissi (-ankisi, fetish) is used for holy, sacred" and "This is a very objectionable use of nkisi, fetish."; "older missionaries" matches the same page's "these early missionaries" context; carried.
  - line 101: "in Bentley's San Salvador of the 1890s *nzimbu* named hexagonal blue pipe beads, not shells (S362, p. 739), and dowry was glossed as nzimbu or other named goods (S362, p. 744)" — p. 739 has "hexagonal blue pipe glass bead ... nzimbu, 2": p. 744 has the Dowry gloss; carried.
  - Era table line 115: "currency moves from palm-cloth mats to red glass beads (about 1830) and blue pipe beads called nzimbu (about 1863)" — p. 739 verbatim supports "; carried.
- Grounds — CARRIED. Gate Grounds text equals the row's teaches cell exactly (only the teaches cell ends with a full stop; the lesson Grounds omits the terminal period — formatting only).

## S363 (Torrend 1891 Comparative Grammar, Internet Archive comparativegramm00torruoft)

- Re-open: djvu.txt HTTP 200, 1,167,842 bytes (matches row), 54,998 lines (matches row); page-level XML fetched (14.68 MB).
- S363 anchor quotes — CARRIED, all verbatim, all <= 25 words, at stated locators:
  - Introduction §22, p. xxv (page object reading head "Introductioit. XXV"): "In 1659 the Propaganda at Rome published a Congo Grammar of the same author" — verbatim (14 words); "This is a good work, and one which shows much insight into the language." — verbatim (14 words); "It has been lately translated into English by Mr. H. Grattan Guinness, of the Livingstone Congo Mission." — verbatim (17 words).
  - p. 35, note 156 (page object running head "Comparative Phonetics. 35"): "The Congo dialects which are described in the old Grammar of the Capuchin Father Brusciotto a Vetralla" — verbatim (17 words); "were more perfect than the modern San-Salvador dialect described in Rev. W. Holman Bentley's" — verbatim (15 words).
- Gate quote (Introduction §22, p. xxv) — CARRIED, verbatim, 14 words.
- Tier — CARRIED. Tier B fits QUALITY criterion 6: a nineteenth-century comparative grammar is primary only for Torrend's own comparisons and secondary for Brusciotto's 1659 book metadata; the entry uses it only for Torrend's comparative judgment (line 56), so B is right, not over-filed.
- Citing sentences — CARRIED. line 56: "Torrend ranked the old grammar's dialect above Bentley's San Salvador one (S363, p. 35, note 156)" — note 156 states the old grammar's dialects "were more perfect than" Bentley's modern San-Salvador dialect; "ranked above" is a faithful paraphrase, no over-read.
- Grounds — CARRIED (identical, terminal period formatting as S362).

## S364 (Vos 2017, eprints PDF 406,919 bytes exact match; Openedition HTML refetched HTTP 200)

- Re-open: eprints PDF HTTP 200, 406,919 bytes (matches row), application/pdf; Openedition http://journals.openedition.org/cea/2225 fetched HTTP 200 (200,368 bytes). Note: pdftotext drops digit glyphs from the PDF body (font/ToUnicode mapping), but the text is intact and the same sentences are verbatim in the Openedition full text, which the row also cites; paragraph numbers match Openedition's own numbering.
- S364 anchor quotes — CARRIED, verbatim, at stated locators (all <= 25 words):
  - §1 (printed p. 159): "posição consolidada com o estabelecimento do domínio colonial oficial em 1888" — on PDF p. 159 (header "Jelmer Vos 159") and Openedition §1 (11 words).
  - §22 (printed p. 171): "Em dezembro de 1913, os chefes do Kongo responderam à inesperada brutalidade da dominação colonial" — PDF p. 171 and Openedition §22 (15 words).
  - §25 (printed p. 172): "reconhecidos oficialmente como "primeiro chefe" (mfumu antete)" — PDF p. 172 and Openedition §25 (7 words).
  - §27 (printed p. 173): "Na manhã do dia 10 de dezembro, Buta e seus aliados lançaram o primeiro ataque em grande escala" — PDF p. 173 and Openedition §27 (18 words).
- Gate quote (§1, printed p. 159) — CARRIED, verbatim, 11 words.
- Tier — CARRIED. Tier A fits QUALITY criterion 6: peer-reviewed archival study by the specialist historian of nineteenth-century Kongo, authoritative for the revolt's course and actors; not an abstract or publisher description.
- Citing sentences/era table — CARRIED at stated strength:
  - Era table line 116: "Pedro V seeks Portuguese troops in a succession dispute" — S364 §1: "buscou a ajuda militar do governo português em Angola para impor-se numa disputa sucessória com um rival local em 1860"; carried. ("a vassalage treaty, which one historian treats as the irreversible loss of sovereignty" is the S365-attributed clause, not on the S364 page; see residual note.)
  - Era table line 118: "chiefs install the mission-educated Manuel Kiditu (1911)" — S364 §32 "colocaram no trono Manuel Kiditu, que tinha sido educado na missão católica" plus §40 "eleição de Manuel Martins Kiditu em 1911"; carried. "the rising of December 1913 targets him and the labour recruitment" — §22 ("Em dezembro de 1913 ... incluindo o rei Manuel Kiditu ... principal responsável") and §7/§27 (labour recruitment as cause); carried. "in 1914 the governor asks that the king's authority cease and the regalia go to Luanda" is not on the S364 pages; it is the S366-attributed clause (see residual note).
- Grounds — CARRIED (identical, terminal period formatting as above).

## Residual observations / unrun checks (outside this slice)

- Era table line 116 third clause (vassalage treaty, irreversible loss of sovereignty) and line 118 third clause (1914 governor, regalia to Luanda) are attributed to S365 and S366 respectively; I did not verify those rows (S365/S366 are other slices). If those clauses are not carried by S365/S366, the era rows would need a fix — flag for the L1 and the S365/S366 reviewers.
- S364 PDF digit loss is an extraction artifact of pdftotext, not a page defect; the row's byte size and page headers match, and the Openedition full text carries every digit-bearing quote verbatim.
- No installs performed (no tool record needed); no check of check-gate-quotes.py requested for this slice.
