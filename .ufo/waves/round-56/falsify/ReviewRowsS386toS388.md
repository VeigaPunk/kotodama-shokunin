# ReviewRowsS386toS388 — falsify findings (Kotodama round 56, claim C)

**Verdict: 1 defect (WRONG-LOCATOR) in row S386; all quotes carried, tiers fit, Grounds consistent. Claim C stands for this slice after the locator fix.**

Scope: rows S386, S387, S388 of corpus/SOURCES.md; Gate lines in corpus/lessons/round-56.md; citing sentences in corpus/knowledge/civilizations/kongo-kingdom.md. Sources re-opened by plain requests: SMK Open API (search + object endpoints, HTTP 200), UPSpace postprint (HTTP 200, application/pdf, 338,227 bytes), Walters catalogue PDF via Wayback capture 20260730042357 (the live URL now answers 403 Cloudflare interstitial to a plain GET; the capture is byte-identical in size to the row's recorded 3,089,744 bytes, so it is the same file; challenge met, not passed). No tool installs made (curl, pdftotext 26.08.0, python3 standard library only).

## Findings

- SOURCES S386 anchor "KMS8 gallery label 1: 'Den kostbare elefantstødtand var måske én af de gaver, som delegationen havde med.'" — **WRONG-LOCATOR**. The quoted sentence appears verbatim in KMS8 gallery label 2 (record `labels[1]`), not label 1 (`labels[0]`), in both the Danish and English API records; label 1's servant sentence ("Med sig havde han sine to tjenere, Pedro Sunda og Diego Bemba.") is correctly located.
  - Fix: in the SOURCES S386 quote cell change `KMS8 gallery label 1: "Den kostbare elefantstødtand var måske én af de gaver, som delegationen havde med."` to `KMS8 gallery label 2: "Den kostbare elefantstødtand var måske én af de gaver, som delegationen havde med."` (old -> new; the Gate line and entry are unaffected).

## Checked items (one line each)

- S386 Gate quote "Dom Miguel de Castro, Ambassadør for herren af Sonho" — CARRIED. Verbatim in KMS7 record second title field; 9 words (<= 25).
- S386 anchors, 12 of 12 listed — 11 CARRIED, 1 WRONG-LOCATOR (above). All quoted texts verbatim on the re-opened API records; all <= 25 words.
- S386 kongo-kingdom.md line 102 "SMK's record dresses the Soyo envoy Dom Miguel de Castro in European clothing (S386, KMS7 gallery labels 1-2)" — CARRIED. KMS7 label 1: "Det er bemærkelsesværdigt, at han har valgt at lade sig afbilde i europæisk klædedragt, med en rigt mønstret skjorte, brun jakke, hvid kniplingskrave samt en hat i bæverskind med metalkæde og en lang, rød fjer"; label 2: "Han er klædt efter tidens franske mode." Both attributed to SMK's record in the sentence; no over-read.
- S386 kongo-kingdom.md line 111 era row "envoys to Rome (bust dated 1629) and to Dutch Brazil (1640s)" citing S386 (KMS7 gallery label 1) — CARRIED. Label 1 names Dom Miguel ambassador of the lord of Soyo, his mission for support from the Dutch Republic, the 200 enslaved people given to the governor of Dutch Brazil, and the portrait commissioned on his journey to the Netherlands.
- S386 tier doc/A — FITS criterion 6: the holding museum's own catalogue records and gallery labels for its own three objects are primary for that exact scope; the dress reading is curatorial and the row scopes it.
- S386 Grounds vs teaches — CONSISTENT. Gate Grounds ("three 1643 portraits names a Kongo embassy sent by the lord of Soyo, its European dress, its named servants and its royal-collection afterlife") is a subset of the teaches cell's list; no untaught claim.
- S387 Gate quote "Antonio Manuel, Marquis of Ne-Vunda, 1629. Marble." — CARRIED. Verbatim in fig. 46 caption on printed p. 104 (PDF page index 105); 7 words.
- S387 anchors, 16 of 16 listed — CARRIED. Verbatim on printed pp. 104, 105 and 114 (notes), matched in reading-order extraction; all <= 25 words. (pdftotext -layout interleaves the two columns; the default reading-order extraction gives contiguous sentences.)
- S387 kongo-kingdom.md line 102 "Lowe identifies the raffia tunic on Antonio Manuel ne Vunda's bust as a garment reserved for chiefs (S387, p. 104)" — CARRIED. p. 104: "He wears a tunic or cape in raffia openwork mesh or netting known as a kinzembe or zamba kya mfumu, an article of clothing reserved in the Congo for chiefs or other important people." Attribution to Lowe is accurate; no over-read.
- S387 kongo-kingdom.md line 111 "envoys to Rome (bust dated 1629)" citing S387 (p. 104) — CARRIED. Caption and passage date the bust 1629.
- S387 tier book/A — FITS criterion 6: footnoted catalogue essay by a Renaissance-history professor, authoritative for the scope; the row itself notes it is not the bust and that the kinzembe identification rests on note 29.
- S387 Grounds vs teaches — CONSISTENT. Grounds ("raffia regalia called kinzembe ... prints and frescoes show European dress and a medal invents an audience") matches the teaches list's items; no untaught claim.
- S388 Gate quote "still very little is understood about the origins of the kingdom" — CARRIED. Verbatim on postprint p. 2, opening paragraph of the project summary (line-wrapped in extraction; contiguous after whitespace normalization); 11 words.
- S388 anchors, 4 of 4 listed — CARRIED. "remains archaeologically elusive" on p. 2; "Most male tombs contained swords and sabres of honour" and "anklets and large quantities of glass, copper and shell beads were found in female burials" on p. 3; all <= 25 words.
- S388 kongo-kingdom.md line 69 "A provincial seat can be archaeologically almost invisible (S388, postprint p. 2)" — CARRIED. p. 2: "The Kindoki site, associated with the provincial capital of Mbanza Nsundi, remains archaeologically elusive ... Mbanza Nsundi was characterised by a low population density. Consequently, pinpointing its historical centre has proven challenging."
- S388 tier paper/A — FITS criterion 6: the project's own archaeologists reporting their own 2012-2014 excavations in a peer-reviewed venue, primary for the fieldwork summary and dating; the row scopes out what it is not primary for.
- S388 Grounds vs teaches — CONSISTENT. Grounds ("dispersed low-density capitals, rank marked in graves by swords or by beads, and a trade town whose imports date its rise") maps onto the teaches items (low-density mbanza form; elite cemetery grave goods; radiocarbon and imported-ceramic chronology of Ngongo Mbata); no untaught claim.

## Unrun checks

None. All four assignment items were run for each of S386, S387, S388.
