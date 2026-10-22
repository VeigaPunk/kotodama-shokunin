# ScoutCavazzi — claim C source item: Cavazzi 1687 and its reliability

Role: scout (leaf). Nothing edited outside this report. No installs, no pacman, no git/jj writes.
Scratch: `/fast/scratch/hyaku/kotodama-r56/ScoutCavazzi/`.

## Findings in one paragraph

The 1687 Bologna printing of Cavazzi's *Istorica descrizione de' tre' regni Congo, Matamba et
Angola* is open on archive.org in two independent scans, and its Book One pages 2-6 carry exactly
the material the Kongo entry needs: the list of principal provinces, the *Zimbi* shell currency,
the rule that a province's government goes to the prince of the blood in line to succeed, and
`Mani-` prefixed lordships. Thornton's open general introduction to the Araldi manuscript
supplies the counterweight: the printed book was edited by Fortunato Alamandini before it reached
the press, Cavazzi took Kongo history partly from other writers, he smoothed contradictions
between informants into one narrative, and he was hostile to Africans. Confidence: high for the
printed wording (transcribed from page images, not from OCR); high for the reliability points
(direct quotation from Thornton); the entry may not use Cavazzi as an eyewitness for Kongo.

Observed (opened this session): both archive.org items exist, return 200, and the page images
match the OCR text file. Inference (flagged): that Cavazzi's Kongo chapters are mostly compiled,
which Thornton states in general terms but does not quantify per chapter. Gap: no peer-reviewed
open article on Cavazzi's reliability was opened (Cambridge Core and JSTOR both answered HTTP 429
to plain requests); a peer-reviewed open edition of part of Book One was downloaded but is not
filed as a row (see `leads`).

## Sources

### NEW-ScoutCavazzi-1

citation: Cavazzi da Montecuccolo, Giovanni Antonio, comp.; reduced by Fortunato Alamandini da Bologna. 1687. *Istorica descrizione de' tre' regni Congo, Matamba et Angola*. Bologna: Giacomo Monti. Getty Research Institute copy (archive.org collection `getty`), archive.org item `istoricadescrizi00cava`, 986 imagecount.

url: https://archive.org/download/istoricadescrizi00cava/istoricadescrizi00cava_djvu.txt and page images https://archive.org/download/istoricadescrizi00cava/page/n25.jpg , .../n26.jpg , .../n27.jpg , .../n29.jpg (item page: https://archive.org/details/istoricadescrizi00cava)

route: direct, HTTP 200, 2026-10-22. OCR text 3,423,164 bytes, sha256 9fd49577988706fcd78b6eba79bd31aa1ae8d56ef2455a77ca03e498e4ff305b; page images JPEG 2672x3823. Quotes below are transcribed from the page images (printed pages 2, 3, 4, 6), because the OCR renders long s as f and is unusable for quotation. Transcription rules used: long s written s; a word split by a line-end hyphen is joined; u/v left as printed. Paragraph numbers are the book's own (§4, §5, §8, §11, §12).

kind: book

tier: A for what the 1687 print says (it is the printing itself); not authoritative for Kongo fact once past the printed page. Secondary scans of the same edition also open: `bub_gb_7MpQAAAAcAAJ` (Google/Ghent, 1000 pp.) and `istoricadescritt00cava_0` (1690 issue), so the text can be cross-checked.

scope: Libro Primo, pp. 2-6: province names, the Zimbi currency, the Sundi governorship and succession clause, Pemba as royal burial place, `Mani-` titles and the Dembi/Imbuilla dependency, Soyo as the landing place of the faith. Also usable, outside this row's quotes, for the book's Kongo Christianity chapters. Not usable for chronology or for anything Cavazzi did not see.

quotes:
- Libro Primo §4, p. 2: "sei principali, Pamba, Sogno, Sundi, Pango, Batta, e Pemba"
- Libro Primo §5 (Bamba), p. 3: "le numerose Pescagioni de Zimbi, ò Lumachette, le quali in tutto il Regno spacciansi per vnica Moneta"
- Libro Primo §8 (Sundi), p. 4: "Il Gouerno tocca quasi sempre à quel Principe del Sangue, che ha da succedere nel Regno"
- Libro Primo §12, p. 6: "li Dembi, che soggiacciono al gouerno del Signore, ò Mani-Imbuilla"

teaches: The 1687 print names six Kongo provinces, a shell currency, a succession-linked governorship and Mani- prefixed lords, in spellings and categories an outsider chose.

draft sentences:
- Cavazzi lists six principal provinces, Pamba, Sogno, Sundi, Pango, Batta and Pemba, and says he passes over the others as uncultivated, so his list is a shortlist of the rich provinces rather than a survey of the kingdom. (NEW-ScoutCavazzi-1, Libro Primo §4, p. 2)
- The Zimbi, or little snails, whose fisheries Cavazzi counts among the king's revenues in Bamba, pass through the whole kingdom as the only money in civil contracts, so a currency can rest on one province's fishery. (NEW-ScoutCavazzi-1, Libro Primo §5, p. 3)
- In Sundi the government usually goes to the prince of the blood who is to succeed, which makes a provincial office a stage in the succession rather than a separate career. (NEW-ScoutCavazzi-1, Libro Primo §8, p. 4)
- Cavazzi renders a territorial lord as Mani-Imbuilla and puts the Dembi under his government, so Mani- in his spellings marks a lord set over a named people or place. (NEW-ScoutCavazzi-1, Libro Primo §12, p. 6)
- For Pemba he says the name covers the province and its banza alike, the chief residence of the viceroy or governor, so at least one banza is a governor's seat rather than the king's city. (NEW-ScoutCavazzi-1, Libro Primo §11, p. 6)
- Cavazzi fits Kongo offices to European ranks, calling Soyo a county whose lords are counts and naming Bamba's governors dukes, so those ranks are his translation and a worldbuilder should keep the Mani- title as the office and the European word as the gloss. (NEW-ScoutCavazzi-1, Libro Primo §5-§6, p. 3)

### NEW-ScoutCavazzi-2

citation: Thornton, John K. n.d. (posted 2008-2010 era). "Cavazzi, Missione Evangelica: General Introduction." Boston University, African American & Black Diaspora Studies, faculty pages. No DOI.

url: https://www.bu.edu/afam/people/faculty/john-thornton/cavazzi-missione-evangelica-2/

route: direct, HTTP 200, 2026-10-22, 208,904 bytes HTML; tags stripped locally to plain text and every quoted string re-grepped in the served page. Wayback was not needed and archive.org's availability API answered HTTP 429 during this session.

kind: web (scholarly introduction to a text edition, first person by the translator)

tier: B — expert write-up by the leading historian of Kongo and translator of the manuscript, hosted by his university; not peer-reviewed and undated, so it supports provenance claims, not new factual claims about Kongo.

scope: provenance and reliability of Cavazzi's text: the 1687 print's editor, Cavazzi's use of other writers for Kongo history, his handling of contradictory informants, the excision of miracle stories, his hostile outlook, and the orthography problem for Kikongo and Kimbundu terms.

quotes:
- section "The Araldi Manuscripts", first paragraph: "brought to the publisher by Fortunato Alamandini, who acknowledged having edited the material before publishing it"
- section "Giovanni Antonio Cavazzi: Background and Travels", paragraph beginning "Not surprisingly": "he sought historical accounts in the writings of others whose work he used to write Istorica Descrizione"
- same section, paragraph beginning "Unfortunately for modern historians": "contradictions in his numerous African informants’ accounts are worked out in one smooth narrative"
- same section, paragraph beginning "Cavazzi’s personality and outlook": "Cavazzi was essentially anti-African in his outlook"

teaches: Cavazzi's printed book is an edited compilation whose Kongo sections rest partly on other writers, and its author's hostile outlook and smoothed contradictions limit what a single passage proves.

draft sentences:
- The 1687 book reached the press through Fortunato Alamandini, who admitted editing the material, so its smooth prose belongs to an editor as well as to Cavazzi. (NEW-ScoutCavazzi-2, section "The Araldi Manuscripts")
- Cavazzi sought Kongo history in other men's writings, and Thornton calls his Kongo section one of the most detailed on record, so a Kongo detail may be borrowed rather than observed. (NEW-ScoutCavazzi-2, section "Giovanni Antonio Cavazzi: Background and Travels")
- He worked contradictions between his informants into one smooth narrative, so the printed text no longer shows which informant supplied which version. (NEW-ScoutCavazzi-2, section "Giovanni Antonio Cavazzi: Background and Travels")
- Thornton says Cavazzi was essentially anti-African, so his judgements of Kongo persons and rites must be quoted as his opinion, never carried into canon as description. (NEW-ScoutCavazzi-2, section "Giovanni Antonio Cavazzi: Background and Travels")

## notes: further passages read on the same page images (short fragments only; no filed quote)

All from the same page images of NEW-ScoutCavazzi-1, read this session:
- p. 3, Libro Primo §5 (Bamba): its governors "s'intitolano Duchi" and are always among the first princes of the kingdom's blood; they abuse their authority and withhold the annual tribute. Bamba also holds the salt pans and the Zimbi fishery, with a margin note that gold mines exist but are kept closed.
- p. 4, Libro Primo §7: Soyo is "la Porta" through which the Gospel entered the kingdoms of Kongo, and its ruler was the first of all to be baptised; Cavazzi reckons the church there was founded about 1482.
- p. 4, Libro Primo §7: in the capital, also called Sogno, three churches are held in great veneration, one inside the court precincts, one outside where the Counts are buried, and one of St Antony of Padua that is the friars' hospice.
- p. 4, Libro Primo §8: Sundi lies thirteen leagues from S. Salvatore, "Metropoli del Regno".
- p. 6, Libro Primo §11: Pemba, last of the six, "gloriasi di essere Culla, Trono, e Tomba à tutti li suoi Rè tanto Idolatri, quanto Christiani".
- p. 6, Libro Primo §12: a family called Imbuella is said to have held in past centuries the title and prerogatives of king while depending on the king of Kongo; Ouando's capital is San Michele.
- p. 6, Libro Primo §12: other province names as Cavazzi spells them: Quioua, Quiamaxondo, Ndamba, Nsuffo, Nsella, Iuua, Alombo, Nzolo, Nzanga, Marzinga, Metondo.
- p. 2, Libro Primo §3: beyond the Zaire the country is held by "diuersi Potentati, che del nome di Rè si pregiano", naming Mani Loango, Mani-Cacconda and Mani Engoi.
- Reliability, from NEW-ScoutCavazzi-2: Church authorities took exception to the miracle stories in the Araldi manuscripts and the printed book carries far fewer; and in the section "Orthography and Conventions" Thornton notes that Kikongo has several different national orthographies (Congo-Brazzaville, Zaire and Angola), so Cavazzi's Italianate spellings must not be treated as a standard.

## leads: opened, not filed as a row

- Precioso, Daniel. 2025. "Religiões centro-africanas pela ótica de um capuchinho: rituais, objetos sagrados e sacerdócios na Istorica Descrizione (1687), de Giovanni Cavazzi." *Revista de fontes* 12(22), ISSN 2359-2648, starting p. 134. PDF at https://periodicos.unifesp.br/fontes/article/download/16466/13990/89054 — HTTP 200, 462,524 bytes, 31 pages, opened 2026-10-22. The journal's article listing gives DOI 10.34024/fontes.2025.v12.16466; the PDF prints no DOI itself. It transcribes and translates paragraphs 166 to 204 of Livro Primeiro, the subsections "Da Idolatria" and "Dos Sacerdócios", so it is the cleanest route to Cavazzi's paragraphs on ritual objects and ritual specialists without reading the OCR. Not filed because its subject is religion, not reliability, and this seat's cap was two sources. Worth a row if the entry needs the minkisi material with a citable paragraph number.

## unopened:

- Thornton, John K. 1979. "New Light on Cavazzi's Seventeenth-Century Description of Kongo." *History in Africa* 6: 253-264. PDF URL on cambridge.org returned HTTP 429 with an HTML body, and the JSTOR stable page returned HTTP 429 as well: challenge met, not passed; no bypass attempted (no headless browser, no proxy route). This is the article a reliability row would rather cite, and it should be retried another day.
- MAVCOR Journal, Fromont, "Depicting Kongo and Angola in the Seventeenth and Eighteenth Centuries" (https://mavcor.yale.edu/mavcor-journal/depicting-kongo-and-angola-seventeenth-and-eighteenth-centuries): fetch returned HTTP 200 and 87,806 bytes, but the extracted body in this session's copy was navigation only, so the essay itself was never read and no quote was taken.
- 1732 French translation, archive.org `relationhistoriq01cava` to `relationhistoriq05cava`: located in search, not opened, because the Italian 1687 print was available and is the stronger anchor.

## unrun checks

- No Gate, no acceptance script, no quote-fidelity tool was run (main agent's job).
- Nothing was written to the lane; the acc-c legs (SET, SWEEP, FLOOR, RANGE, STATUS, USEDBY, ACCESS) are untouched by this seat.
