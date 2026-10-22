# ScoutFlorentineAhuitzotl — the *ahuitzotl* in the Florentine Codex, Book 11, and the 1571 Molina gloss

- seat: `KotodamaR55.ScoutFlorentineAhuitzotl` (scout, claim C ground: monsters and hybrid beings)
- round: kotodama 55 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `8eda9543e940bdc4938fad90182ee6a6fe271d0f`, claim base `f4015e70b829523ed81e14ce4279bfab0e0233e4`
- assignment: one water being, opened in the source that records it, for the entry's decisions on naming, composite anatomy, habitat, the book that holds it, and restricted handling
- draft ids used below: `NEW-ScoutFlorentineAhuitzotl-1` … `-3`; the L1 assigns the final `S` ids at integration
- access date for every source below: 2026-10-22
- installs: none. Everything used (`curl`, `python3`, Pillow) was already present; no package was installed or upgraded.
- verification: all 20 quotations taken from the two HTML sources were substring-checked against the saved bytes (whitespace, italic markup and soft hyphens normalised only): 0 misses. The two Molina quotations were read from the page image, not from the item's OCR, and are not machine-checkable against text; the leaf (scan `n279`) and the entry order (`Auitequi`, `Auitoca`, `Auitzocalaqui`, `Auitzotl`) were confirmed on the image.

## Route summary

| row | file actually read | route | size |
|---|---|---|---|
| 1 | `https://florentinecodex.getty.edu/en/book/11/folio/70v`, `…/folio/71r`, `…/folio/71v` | direct plain `curl`, HTTP 200 each, `text/html` (server-rendered payload carries the four text columns); no challenge, no login | 234502 / 232304 / ~233000 bytes |
| 2 | `https://web.archive.org/web/20260113063147/https://www.loc.gov/item/2021667856/` | live URL `https://www.loc.gov/item/2021667856/` returns HTTP 403 to a plain request (5635-byte block page; `/item/2021667859/` and the search endpoint also 403) — challenge met, not passed; read from Wayback capture `20260113063147` | 202039 bytes |
| 3 | `https://archive.org/download/vocabularioenlen00moli_0/page/n279_w1000.jpg` (page image) and `…/vocabularioenlen00moli_0_djvu.txt` (OCR, cross-check only) | direct plain `curl`, HTTP 200, JPEG 1618×2184 and plain text; no challenge | 648987 / 2509158 bytes |

Two textual cautions. (a) The Getty folio pages print four text columns per page — the manuscript Nahuatl, a López Austin/García Quintana Spanish transcription, a Spanish-to-English translation (García Garagarza 2023) and a Nahuatl-to-English translation (Anderson & Dibble 1953–1982) — and the paragraphs are physically split across folios 70v, 71r and 71v; every locator below names the folio and the column's named translator. (b) The Molina quotations are read from the **page image**, because the item's OCR mangles the same line (`ciertoanimalejo`, `petri-`); the OCR file was used only to locate the leaf.

---

### NEW-ScoutFlorentineAhuitzotl-1

citation: Sahagún, Bernardino de. *Historia general de las cosas de Nueva España* (Florentine Codex), Book 11, fols. 70v–71v, ch. 2 ("second paragraph"), manuscript Biblioteca Medicea Laurenziana. Digital edition: *Digital Florentine Codex*, edited by Kim N. Richter, Alicia Maria Houtrouw, Kevin Terraciano, Jeanette Peterson, Diana Magaloni, and Lisa Sousa. Los Angeles: Getty Research Institute, 2023. Text columns used: López Austin & García Quintana 2000 (Spanish transcription), García Garagarza 2023 (Spanish-to-English), Anderson & Dibble 1953–1982 (Nahuatl-to-English).

url: https://florentinecodex.getty.edu/en/book/11/folio/70v ; https://florentinecodex.getty.edu/en/book/11/folio/71r ; https://florentinecodex.getty.edu/en/book/11/folio/71v

route: direct plain request (curl), HTTP 200 on all three folios, `text/html`; no challenge, 2026-10-22

kind: book

tier: A — the Getty Research Institute publishes the digitised manuscript leaves beside a diplomatic Nahuatl transcription and named scholarly translations; primary for the passage and authoritative for what the page says. B for any claim that the Nahua "believed" this in general: the page records one book's account, compiled under a Franciscan editor, and nothing here surveys other communities or periods.

scope: the codex's own heading words for the being, its body, its habitat, its manner of killing, the state of the recovered corpse, who may recover it, the penalty for a layperson who tries, the destination of the drowned, and the burial place. Also supports that the passage sits inside a catalogue of animals and cross-refers between entries. Does not support: any etymology of the name, any identification with a real species, any distribution beyond "springs/sources", any modern category word ("monster", "cryptid"), or the date(s) at which any of this was first told.

quotes:
- fol. 70v, heading of the second paragraph (López Austin Spanish transcription): "de un animalejo llamado ahuítzotl, notablemente monstruoso en su cuerpo y en sus obras"
- fol. 70v, heading of the second paragraph (García Garagarza translation): "On a small animal called ahuitzotl, whose body and actions are remarkably monstrous"
- fol. 70v, second paragraph, first sentence: "In this land, there is an animal—one never heard of before—that lives in the water"
- fol. 70v, second paragraph, description: "It has a long tail, and at the tip of the tail, there is a hand, like a person’s hand."
- fol. 70v, second paragraph, description: "its feet and hands are like a monkey’s"
- fol. 70v, second paragraph, habitat sentence: "This animal lives in deep water springs."
- fol. 71r, continuation of the second paragraph: "snatches this person with the hand of its tail and drags him or her underwater and into the deep"
- fol. 71r, continuation, recovery of the body: "comes out without eyes, without teeth, and without nails"
- fol. 71r, continuation, closing sentence: "Nobody would dare to take that body out."
- fol. 71r, Nahuatl-to-English column (Anderson & Dibble): "But sometimes the auitzotl or the tlilcoatl raises him to the surface."
- fol. 71v, on who may recover the body: "only they could take this person out, because they said that the others were not worthy of touching him or her"
- fol. 71v, on the drowned person’s fate: "the Tlaloque gods had sent the soul of the one who had drowned to earthly paradise"
- fol. 71v, on burial: "to be buried in one of the shrines that they call ayauhcalco"
- fol. 71v, on the penalty for a layperson: "this person would also drown in the water or become afflicted with arthritic gout"

teaches: The codex files the ahuitzotl among animals as a "monstrous" being with a hand on its tail that drowns people in springs and takes their eyes, teeth and nails.

draft sentences:
- The account is filed inside a catalogue of animals and opens by naming the being and calling it monstrous, so a worldbuilder must decide whether a monster gets its own list or a numbered place among the fauna (NEW-ScoutFlorentineAhuitzotl-1, fol. 70v, heading of the second paragraph).
- The stated reason for recording it is novelty rather than hybridity — "an animal—one never heard of before"—which lets a bestiary admit a being on the ground that no one has heard of it before, without needing a rule about mixed bodies (NEW-ScoutFlorentineAhuitzotl-1, fol. 70v, second paragraph, first sentence).
- Its composite anatomy is one diagnostic joint, not a general patchwork: dog-sized, short-furred, black and smooth, with a long tail whose tip is "a hand, like a person’s hand", and feet and hands "like a monkey’s" (NEW-ScoutFlorentineAhuitzotl-1, fol. 70v, second paragraph, description).
- Its place on the map is a water source and its threshold, not a wilderness: it "lives in deep water springs", and the encounter happens when a person reaches the edge of the water where it lives (NEW-ScoutFlorentineAhuitzotl-1, fol. 70v, second paragraph, habitat sentence).
- The killing leaves a signature a worldbuilder can use as evidence: the body comes back "without eyes, without teeth, and without nails", unmarked by wounds but bruised (NEW-ScoutFlorentineAhuitzotl-1, fol. 71r, continuation of the second paragraph).
- Handling of the corpse is restricted to cult specialists and enforced by a penalty — laypeople are "not worthy of touching him", and one who tries "would also drown in the water or become afflicted with arthritic gout" (NEW-ScoutFlorentineAhuitzotl-1, fol. 71v, on who may recover the body and on the penalty for a layperson).

---

### NEW-ScoutFlorentineAhuitzotl-2

citation: Library of Congress / World Digital Library. "General History of the Things of New Spain by Fray Bernardino de Sahagún: The Florentine Codex. Book XI: Natural Things." Item 2021667856, digital id `https://hdl.loc.gov/loc.wdl/wdl.10622`; original at Biblioteca Medicea Laurenziana, Florence, 1577.

url: https://www.loc.gov/item/2021667856/ (read as `https://web.archive.org/web/20260113063147/https://www.loc.gov/item/2021667856/`)

route: live URL HTTP 403 to a plain request — challenge met, not passed; the record was read from the Wayback capture `20260113063147` of the same page, HTTP 200, 2026-10-22

kind: record

tier: A — the holding library's own catalogue description of the item it digitised (shelfmark, date, language, what the book is), written by the institution that publishes the surrogate. B for any statement about the society the book describes: it summarises scholarship, it does not read the passage.

scope: what a holding library says the book is — its size and scope, Book XI's place and subject, the mixture of real and legendary animals in it, its illustrations, its two languages, and the 1577 date. Does not support: anything about the ahuitzotl text, any specific creature, or the codex's internal chapter order.

quotes:
- Summary: "an encyclopedic work about the people and culture of central Mexico"
- Summary: "Commonly referred to as the Florentine Codex, the manuscript consists of 12 books devoted to different topics."
- Summary: "Book XI, the longest in the codex, is a treatise on natural history."
- Summary: "The discussion of animals draws upon Aztec legends about various animals, both real and mythical."
- Summary: "Book XI contains numerous illustrations of animals, including mammals (jaguar and armadillo)"
- Notes: "Content in Coatepec Nahuatl and Spanish."
- Created / Published field: "1577"

teaches: The Library of Congress record calls Book XI, the longest of twelve, a treatise on natural history whose animals come from legends both real and mythical, with many illustrations.

draft sentences:
- A twelve-book encyclopedic work is the container a bestiary section has to fit into, and Book XI — "the longest in the codex" — is the one that holds the animals, so a worldbuilder should decide where the creature volume sits in the whole work rather than inventing it in isolation (NEW-ScoutFlorentineAhuitzotl-2, Summary).
- The record itself says the "discussion of animals draws upon Aztec legends about various animals, both real and mythical", which is a holding library asserting that one catalogue mixes observed fauna with narrated beings (NEW-ScoutFlorentineAhuitzotl-2, Summary).
- Because "Book XI contains numerous illustrations of animals", a being in this tradition is normally drawn as well as described, and the choice between a text list and a picture list is a design decision, not a formatting detail (NEW-ScoutFlorentineAhuitzotl-2, Summary).
- The manuscript is dated 1577 and its content is in two languages side by side, so one being can carry a name in one language and a description in another, and the entry must say which one it is quoting (NEW-ScoutFlorentineAhuitzotl-2, Notes).

---

### NEW-ScoutFlorentineAhuitzotl-3

citation: Molina, Alonso de. 1571. *Vocabulario en lengua castellana y mexicana* (part two: *Vocabulario en lengua mexicana y castellana*). Mexico: Antonio de Spinosa. Copy: Thomas Fisher Rare Book Library, University of Toronto, call number `buc f 00124`; digitised by the Internet Archive as `vocabularioenlen00moli_0`.

url: https://archive.org/download/vocabularioenlen00moli_0/page/n279_w1000.jpg (item: https://archive.org/details/vocabularioenlen00moli_0)

route: direct plain request (curl), HTTP 200, JPEG page image 1618×2184, read as an image; the item's OCR (`…_djvu.txt`, HTTP 200) was used only to locate the leaf; no challenge, 2026-10-22

kind: book

tier: A — a 1571 printed primary dictionary, read from the leaf itself in a named library copy. It is authoritative for the gloss and for the spelling of the headword as printed, and for nothing else.

scope: the headword's one-line Spanish gloss and one neighbouring water verb, on the page whose running head reads "A ANTE V, ET X" (second part, entry `Auitzotl`, scan leaf 279). Supports that *auitzotl* was a dictionary word glossed as a small water animal, and that *auitzocalaqui* meant to swim under water. Does not support: any anatomy beyond the comparison to a small dog, any behaviour, any habitat detail, any claim that the dictionary and the codex describe the same being.

quotes:
- leaf 279, second part, s.v. `Auitzotl`: "Auitzotl. cierto animalejo de agua como perrillo."
- leaf 279, second part, s.v. `Auitzocalaqui`: "Auitzocalaqui. n. nadar debaxo del agua."

The first quotation resolves the typesetter's line-break hyphen: the leaf prints `como perri-` at the line end and `llo.` at the start of the next line. No words are joined across entries or passages; the spacing of the OCR file (`ciertoanimalejo`, `petri-`) is an OCR artefact and is not reproduced.

teaches: A 1571 Mexico-printed Nahuatl dictionary glosses auitzotl only as a small water animal like a small dog, and records auitzocalaqui, to swim under the water.

draft sentences:
- The dictionary gives the name a seven-word body and no story: "cierto animalejo de agua como perrillo", a certain little water animal like a small dog, so a worldbuilder must decide which source is doing the describing before fixing anatomy (NEW-ScoutFlorentineAhuitzotl-3, leaf 279, s.v. Auitzotl).
- The neighbouring verb "Auitzocalaqui. n. nadar debaxo del agua" places the name in a family of water-diving words rather than in a family of ogres, so the being's ordinary sense is a diving animal and the monstrous tail is an addition told about it (NEW-ScoutFlorentineAhuitzotl-3, leaf 279, s.v. Auitzocalaqui).
- This entry is a one-line gloss with no hand, no tail and no drowning in it, so the entry should mark the dictionary register and the narrated register separately instead of blending them into one description (NEW-ScoutFlorentineAhuitzotl-3, leaf 279, s.v. Auitzotl).
- The book that records the plain sense is a missionary's two-part bilingual dictionary printed in Mexico in 1571, a different kind of object from the illustrated encyclopaedia, so "who records the being" changes what the record can tell you (NEW-ScoutFlorentineAhuitzotl-3, item description on the Internet Archive record).

---

## Notes for integration (entry sections ← rows)

| entry section | row(s) | what the rows actually carry |
|---|---|---|
| what a culture names, and what the word means | 3 | one-line gloss "small water animal like a small dog"; separate verb "to swim under the water"; no etymology on the page |
| composite anatomy | 1 | dog size, short shedding fur, tiny pointed ears, black smooth body, long tail ending in a human-like hand, monkey-like hands and feet |
| where it lives on the map | 1 | "deep water springs", the water's edge as the meeting point; the paragraph sits in an animal catalogue that cross-refers to the coyote entry |
| bestiaries and wonder catalogues | 2 | 12 books, Book XI longest and "a treatise on natural history", real and mythical animals together, many illustrations, Nahuatl and Spanish, 1577 |
| omen, guardian, punisher, or moral | 1 | drowning; eyes/teeth/nails taken; the drowned go to "earthly paradise" sent by the Tlaloque gods; burial at *ayauhcalco*; the being pairs with the *tlilcoatl* |
| restricted beings | 1 | only the cult specialists may take the body; laypeople are "not worthy"; a layperson who tries drowns or gets gout |
| method | 1 + 3 | the same name carries a plain animal sense in the dictionary and a monstrous narrated sense in the codex: a worldbuilder should record the register, not just the creature |

- Cross-check available inside row 1: the Nahuatl column and both English columns say the same things at fols. 70v–71v; the Anderson & Dibble column names the companion being (`tlilcoatl`) that the Spanish columns omit, so a sentence about the class of water-takers should cite the folio and say which column.
- Do not derive an etymology from these three rows. The dictionary gives a gloss, the codex gives a story, and neither page segments the word.
- Nothing in these rows dates the belief, names a teller, or gives a place name for a spring; if the entry needs "where", it must say "at springs and water sources, as the codex describes" and stop there.

## Unopened

- `https://www.loc.gov/item/2021667856/`, `/item/2021667859/`, `/resource/gdcwdl.wdl_10622/?sp=125` and the LoC search page — direct plain requests returned HTTP 403 (block page, 5.5–5.7 KB). The record body was therefore read from a Wayback capture; the *resource* viewer (`?sp=125`, a manuscript page image) has no Wayback capture and was not opened.
- `http://mss.bmlonline.it/` and `https://teca.bmlonline.it/` (Biblioteca Medicea Laurenziana manuscript viewer, the holding library of the codex) — connection timed out on three attempts; `https://www.bmlonline.it/` answered HTTP 200 but the viewer did not. The Laurenziana's own digitisation of the manuscript was not read.
- `https://www.getty.edu/research/digital-florentine-codex/`, `…/publications/florentine-codex/`, `…/research/scholars/digital-florentine-codex/` — HTTP 404; `digitalflorentinecodex.getty.edu` and `dfc.getty.edu` do not resolve. The working host is `florentinecodex.getty.edu`, used above.
- Getty *Codex* about-page (`https://florentinecodex.getty.edu/codex`) — HTTP 200, but its prose is client-rendered and no manuscript description was in the payload, so no quotation was taken from it.
- Internet Archive search-inside endpoints (`ia-fts.archive.org`, `api.archivelab.org`) — DNS failure and connection timeout; the Molina leaf was located by matching OCR pages to page images instead.
- Unrun checks: `reports/round-55/accept-c.py` and `tools/check-source-access.py` were not run here; they belong to the L1's integration pass.
