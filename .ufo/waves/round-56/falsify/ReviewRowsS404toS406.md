# Falsify review: rows S404, S405, S406 (claim C, Kongo entry)

Verdict: **CARRIED with one DEFECT** (S406 Italian-transcription quote is not verbatim: "Re" vs "Ré"), plus two minor locator/citation notes and one residual verification gap.

Method: re-opened each row's URL by the route recorded in the row (plain curl / pdftotext; no challenge, no headless browser). S404 download byte-for-byte identical to the recorded size (441,931 bytes); S405 PDF 3,093,683 bytes (row says 3.0 MB); S406 HTML 25,842 bytes, HTTP 200. Ghent record page `https://biblio.ugent.be/publication/5814106` returns HTTP 200. Archive.org metadata confirms creators [Lopes, Pigafetta, Hutchinson], title, "London: John Murray" (redirect chain 302 → 200, mirror differs from the recorded one but same behavior). No tools installed (existing python3/pdftotext used).

## (1) Anchor quotes and Gate quotes: verbatim, ≤25 words, stated locator

- S404 (book, tier A) — all four anchors verbatim on the djvu OCR text at the stated locators:
  - `SOURCES.md:433` anchor / Gate `lessons/round-56.md:50`: "This ifland furniflies the money ufed by the King of Congo and the neighbouring people" — verbatim at pp. 18 (running heads "1 7"=17 before, "I 8"=18 at line 1440, "i 9"=19 after), Book I ch. IV. 15 words. CARRIED.
  - "This kingdom is divided into fix provinces, called Bamba, Sogno, Sundi, Pango, Batta, and Pemba." — verbatim on p. 43 (head 43 immediately before). 15 words. CARRIED.
  - "Note that this word Mani means Lord, the fecond half referring to the country and government under his rule" — verbatim on p. 43. 19 words. CARRIED.
  - "In ancient times the king and his courtiers, as we faid before, wore garments made from the palm-tree" — verbatim on p. 108 (heads 107 before, 109 after). 18 words. CARRIED.
- S405 (paper, tier B) — all four anchors verbatim on printed pages (mapped via PDF page headers: PDF p1=printed 23, p5=printed 27):
  - Gate quote "nzimbu shells (Olivancillaria nana), collected in the Luanda region to the southwest of the Kongo Kingdom, were used as a means of payment" — verbatim on printed p. 23, followed by "(Mahieu 1924:47)" (confirms the tier note's background citation). 23 words. CARRIED.
  - "both the kaori shells (Cypraea moneta), originally from the Far East" — verbatim, p. 23. 11 words. CARRIED.
  - "The kingdom was ruled by a king or ntinu, its capital was Mbanza Kongo" — verbatim, p. 23. 14 words. CARRIED.
  - "kaori shells had lost their value almost completely in the Kingdom of Kongo and were only used for ornamental purposes" — verbatim, printed p. 27. 20 words. CARRIED.
- S406 (docs, tier B):
  - Translation anchors verbatim: "They are fished on the beach by order of the King." (11 words), "They are spent by quantities not one by one." (8 words), note "They are nzimbu shells [Olivancillaria nana]." (7 words). CARRIED.
  - **DEFECT — Gate quote and row anchor are NOT verbatim.** `lessons/round-56.md:52` and `SOURCES.md:435` quote the Italian transcription as "Si pescano al lido per ordine del **Re**. Si chiamano Zimbo." The served page prints "Si pescano al lido per ordine del **Ré**. Si chiamano Zimbo. Si spende à misura non uno ad uno." (precomposed U+00E9; verified at byte level in the served HTML). Old → new fix: `del Re.` → `del Ré.` in both the SOURCES S406 anchor cell and the lesson Gate line. (Claim O's checker `tools/check-gate-quotes.py` does not catch this: it checks quote caps, HTML entities, doubled locators and truncated Grounds, not page verbatim of diacritics.)

## (2) Tier vs QUALITY criterion 6

- S404 A: the 1591 report itself in a complete documented translation, primary for what it reports — A fits.
- S405 B: peer-reviewed paper in an open repository; the nzimbu sentence is background-cited to Mahieu 1924 (verified), so not authoritative for that identification — B fits.
- S406 B: curated university-project card, not peer-reviewed, not a museum accession — B fits.
All three tiers fit criterion 6 line 29.

## (3) Entry sentences citing S404/S405/S406 — carried at stated strength, hedges kept

- `kongo-kingdom.md:101`: "The island of Luanda furnished the shells used as money by the king of Kongo; women dived for them, and gold and silver bought nothing there (S404, Book I, ch. IV, pp. 18-19)" — carried: p. 18 "This ifland furniflies the money ufed by the King of Congo ... women dive under water ... gold, filver ... nothing can be bought except with Lumache". CARRIED.
- `kongo-kingdom.md:101`: "The shell is *Olivancillaria nana* from the Luanda region (S405, p. 23)" — carried verbatim. CARRIED.
- `kongo-kingdom.md:101`: "a curated source says shells were spent by quantities, not one by one (S406, card translation)" — carried; hedge "a curated source says" kept. CARRIED.
- `kongo-kingdom.md:99`: "only the king and those he pleased could wear the finest palm cloth (S404, Book I, ch. VI, pp. 30-31)" — carried: "The king only, and those he pleaseth, are permitted to wear this cloth" spans printed pp. 30-31. CARRIED.
- `kongo-kingdom.md:99`: "nobles began to dress in Portuguese fashion after conversion (S404, Book II, ch. VII, pp. 108-109)" — carried on p. 109: "the nobles of the court have begun to dress according to the Portuguefe fashion". CARRIED.
- `kongo-kingdom.md:64`: "Lopes tells of three princes claiming the throne at once (S404, Book II, ch. IV, pp. 92-94)" — carried on p. 93: "three princes darting up ... to claim the succession at the same time". CARRIED.
- `kongo-kingdom.md:65`: "Lopes says no one held estates; all land belonged to the Crown (S404, Book II, ch. VII, p. 110)" — carried on p. 110: "No one possessing estates or lands, but all belonging to the Crown". CARRIED.
- `kongo-kingdom.md:71`: "Lopes lists six: Bamba, Sogno, Sundi, Pango, Batta and Pemba (S404, Book I, ch. VIII, pp. 42-43)" — carried on p. 43. CARRIED.
- `kongo-kingdom.md:62`: Mani explanation, p. 43 — CARRIED.
- `kongo-kingdom.md:145` (§13 H): "Lopes's six provinces support a kingdom ... (S404, Book I, ch. VIII, pp. 42-43)" — CARRIED.
- `kongo-kingdom.md:43` (§3 limit cell): "European analogies for cloth names are the reporter's (S404, Book I, ch. VI, pp. 30-31)" — carried (velvets/brocades/satins/taffetas/damasks on pp. 30-31). CARRIED.
- No over-read: museum/card labels are not read as studies; the S404 shell-money sentence is a report statement, not a modern finding; S405's identification is the article's own background sentence and the entry states it as the page states it.

## (4) Gate Grounds vs teaches cell

- S404 Grounds ("The 1591 report taken from Duarte Lopes describes Kongo kingship, six provinces and Mani-titled lords, palm-cloth dress reserved by rank, and shell money gathered on Loanda island.") is a faithful subset of the teaches cell — adds no claim beyond it; omits court etiquette/crown land/succession clauses. Not verbatim-equal.
- S405 Grounds is a faithful subset of the teaches cell (omits Nsundi-tomb absence and kingdom naming); adds nothing.
- S406 Grounds is a faithful subset (omits the identification clause); adds nothing.
No Grounds asserts anything the teaches cell does not; none is a truncated *prefix* (so `check-gate-quotes.py`'s truncated-grounds check does not fire). Under the omn the lesson uses (gist restatement) all three pass; under a strict literal-equality reading none equals. Not a defect; observation only.

## Minor notes (not blocking)

- `kongo-kingdom.md:43` (§3 witness-what-cell): "provinces, titles, cloth licences, shell money (S404, Book I, ch. VIII, pp. 42-43)" — one locator for four facts; cloth licences are at ch. VI pp. 30-31 and shell money at ch. IV pp. 18-19. Suggest: "provinces, titles (S404, Book I, ch. VIII, pp. 42-43); cloth licences (S404, Book I, ch. VI, pp. 30-31); shell money (S404, Book I, ch. IV, pp. 18-19)".
- `kongo-kingdom.md:110` (§11 era table, row "1590s–1640s"): "Lopes's report (1591)" appears in the changes cell but S404 is not listed in that row's Rows cell (S374, S387, S386). Suggest adding `S404` to that cell. (Date 1591 is traceable to the S404 row's own title, so not a fabrication.)
- S404 tier note says "the Italian print of 1591 was also opened (see below) and carries the same statements" — no separate row/URL is present in SOURCES for the Italian print, so I could not re-open it; the entry does not cite it, so no entry claim depends on it. Residual verification gap only.

## Unrun checks

- None in scope: all four assignment items were exercised for the three rows.
- Not re-run (out of scope): claim-O tool behavior beyond noting it does not check page diacritics; other rows' reviews.
