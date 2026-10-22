# ScoutCryptozoology — claim C source evidence, round 55

- seat: KotodamaR55.ScoutCryptozoology (leaf; no subagents, no background jobs)
- claim: C (coverage, learning + sourced), entry `corpus/knowledge/myth-symbol/monsters-hybrid-beings.md`
- assignment: calibration item — cryptozoology as a pseudoscience — plus opened-source evidence on the entry's design decisions
- base: `f4015e70b829523ed81e14ce4279bfab0e0233e4`; work read at the live worktree on 2026-10-22
- rows below are drafts for the L1: ids are provisional `NEW-ScoutCryptozoology-<n>`, the L1 assigns S-ids at integration
- no install or upgrade was needed; nothing was installed this seat

## Gap re-check at the worktree (read-only)

- `ls corpus/knowledge/*/*monster* corpus/knowledge/*/*bestiar* corpus/knowledge/*/*hybrid*` → 0 paths. The entry filename has no owner.
- `grep -ril monster corpus/knowledge --include='*.md' | wc -l` → 10; `grep -ril bestiar ...` → 7. Same counts as the claim's gap note.
- Densest passing mentions: `myth-symbol/trickster.md` (3), `myth-symbol/hero-journey-variants.md` (2), `myth-symbol/flood-traditions.md` (2), then one each in `myth-symbol/divination-omen-systems.md`, `myth-symbol/comparative-frameworks.md`, `civilizations/{zimbabwe-shona,olmec,hawaii}.md`, `synthesis/worked-example-mini-culture.md`, `verification/real-world-inspiration-boundaries.md`.
- Live coupling point found: `myth-symbol/symbolism-synthesis-method.md:29` already names "the medieval Latin package: bestiary + lapidary + numerology + heraldic code" with no bestiary file to point at. Rows 4 and 5 below give that line its primary anchor, and row 7 covers the restricted-being leg.

## Findings that shape the entry

1. The word axis and the omen axis are the same axis in Latin, and the lexicon states it in one entry: `monstrum` is religious language first ("a divine omen indicating misfortune"), a monster only by transfer. A culture that names its monsters with a descendant of this word has already committed to monsters-as-signs.
2. The bestiary is a moral book, not a failed zoology. The Aberdeen project says so in its own words, and its folio 13r shows the machinery: a composite being filed among the apes, named by hearsay, anatomised part by part, and given one distant homeland.
3. Wonder-catalogues are counted, not narrated. The Hereford page gives the object's own inventory in numbers (cities, biblical events, plants and animals and strange creatures, peoples, classical pictures) — a usable model for a culture's map as a census of marvels.
4. The cryptozoology calibration is a demarcation claim, not a claim that unknown animals cannot exist. Both opened sources make the distinction: the field's failure is method (unfalsifiable claims kept after failure), and the one clean success story (giant squid) leaves the field the moment the animal becomes zoology. A worldbuilder can therefore write monster-hunters who are wrong in a specific, arguable way rather than credulous in general.

---

### NEW-ScoutCryptozoology-1

- citation: Schembri, Elise. 2011. "Cryptozoology as a pseudoscience: beasts in transition." *Studies by Undergraduate Researchers at Guelph* 5(1): 5–10. DOI 10.21083/surg.v5i1.1341. Open access.
- url: https://journal.lib.uoguelph.ca/index.php/surg/article/download/1341/2371/9738
- route: direct plain GET, HTTP 200, `application/pdf`, six PDF pages (printed pp. 5–10) read in full this session; 2026-10-22
- kind: paper
- tier: B — a refereed undergraduate research journal (faculty review, stated open access), not a specialist zoology journal: sound for the demarcation argument and for the field's own vocabulary, not authoritative for zoology.
- scope: cryptozoology's status under the science/pseudoscience demarcation; the field's internal split from "paracryptozoology" (dragons, unicorns, satyrs, centaurs, merbeings); the giant squid as the case where a myth animal became zoology and left the field; the naming history of Sasquatch and the paper's report of over 200 further names among Native American tribes. Not ethnography, and not evidence for or against any animal.
- quotes:
  - printed p. 6, section "Cryptozoology as a Pseudoscience", second paragraph: "a field that tries to appropriate the prestige of science and copies its outward trappings"
  - printed p. 8, section "Paracryptozoology", first paragraph: "Paracryptozoology is concerned with the most paranormal of cryptozoology reports including dragons, unicorns, satyrs, centaurs, and merbeings."
  - printed p. 8, section "The Cryptids", paragraph on the giant squid: "once the cryptids are no longer in the transitory state between myth and reality, they no longer belong to the cryptozoologists"
  - printed p. 10, conclusion, first column: "by its nature, cryptozoology is bound to remain, at worst, a pseudo-science and, at best, a transitional field of research"
- teaches: The peer-reviewed article argues that cryptozoology fails the demarcation test and that its own literature separates hidden animals from frankly supernatural beings.
- draft sentences:
  - Decide whether the culture's monster-seekers are a profession with a method or enthusiasts with a vocabulary, because the fault this article names is not the search but the keeping of claims that evidence has already failed (NEW-ScoutCryptozoology-1, printed p. 6).
  - Draw the line the field itself draws, between animals that might be found and beings that are frankly supernatural: the article files dragons, unicorns, satyrs, centaurs and merbeings under a separate heading (NEW-ScoutCryptozoology-1, printed p. 8).
  - Give a successful discovery a social cost: once a creature stops being a cryptid it stops belonging to the cryptozoologists, which is a ready scene of professional loss for a hunter who finds one (NEW-ScoutCryptozoology-1, printed p. 8).
  - Let an in-world critic make the demarcation argument on the page instead of the narrator settling it, since the article's verdict is a judgement about method, not about whether unknown animals exist (NEW-ScoutCryptozoology-1, printed p. 10).
  - Expect many names for one beast and name it through the people who claim it: the article reports over 200 further names for Sasquatch among Native American tribes alone, so a single catalogue label flattens a real naming field (NEW-ScoutCryptozoology-1, printed p. 6).

### NEW-ScoutCryptozoology-2

- citation: Loxton, Daniel, and Donald R. Prothero. 2013. *Abominable Science! Origins of the Yeti, Nessie, and Other Famous Cryptids*. Foreword by Michael Shermer. New York: Columbia University Press. Hardcover ISBN 9780231153201 (August 2013); paperback 2015, ISBN 9780231153218; e-book 9780231526814. Publisher's book page.
- url: https://cup.columbia.edu/book/abominable-science/9780231153201/
- route: direct plain GET, HTTP 200, `text/html`, full book page read (description, contents, reviews); 2026-10-22
- kind: book
- tier: B — the publisher's own description of a scholarly trade book: it states the book's programme and case list, not the book's evidence; the book itself was not opened.
- scope: that the book examines the nature of science and pseudoscience in relation to cryptozoology and sets out to challenge the pseudoscience around named cryptids; its case list (Bigfoot; the Yeti and its cross-cultural incarnations; the Loch Ness monster; the Great Sea Serpent; Mokele Mbembe); its closing topic, the psychology of persistent belief. Not usable for any fact about a cryptid, a culture or a sighting.
- quotes:
  - description, first paragraph: "After examining the nature of science and pseudoscience and their relation to cryptozoology"
  - description, first paragraph: "presenting the arguments both for and against their existence and systematically challenging the pseudoscience that perpetuates their myths"
  - description, second paragraph: "the Yeti, or Abominable Snowman, and its cross-cultural incarnations"
  - description, second paragraph: "They conclude with an analysis of the psychology behind the persistent belief in paranormal phenomena"
- teaches: The publisher's description states that the book tests science against pseudoscience in cryptozoology and challenges the claims behind five named cryptids.
- draft sentences:
  - If the setting has monster-hunters, decide whether their story is a science story or a belief story, because this book's stated structure runs from the science/pseudoscience distinction to the psychology of belief rather than to the animals (NEW-ScoutCryptozoology-2, description, first and second paragraphs).
  - Build an imported monster as a cross-cultural object: the case list follows the Yeti through its cross-cultural incarnations, which is the shape a worldbuilder needs when one being arrives under several names in several regions (NEW-ScoutCryptozoology-2, description, second paragraph).
  - Give the local record-keepers a stake in the outcome, since the book's method is to present the arguments both for and against and then test them, which is exactly the scene of a hearing or a refutation (NEW-ScoutCryptozoology-2, description, first paragraph).
  - Treat "pseudoscience" as the culture's own possible charge against its monster-scholars, not as a narrator's verdict: the analytic label belongs to arguments about method, and the page frames it as a relation to be examined (NEW-ScoutCryptozoology-2, description, first paragraph).

### NEW-ScoutCryptozoology-3

- citation: Lewis, Charlton T.; Short, Charles. 1879. *A Latin Dictionary*. Oxford: Clarendon Press. Entry *monstrum*. Perseus Digital Library, `Perseus:text:1999.04.0059:entry=monstrum`.
- url: https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0059%3Aentry%3Dmonstrum
- route: direct plain GET, HTTP 200 (Perseus Hopper), entry read through sense II.B; 2026-10-22
- kind: book
- tier: A — a standard Latin lexicon read at its own entry: authoritative for the attested senses and for the classical citations it gives, not for any theory of monsters.
- scope: the sense range of *monstrum* — religious language for an omen of misfortune (sense I, with the synonym gloss and the Cicero passage on the ostenta family), the transferred sense monster or monstrosity of a living being or a thing (II), the application to character (II.A), and the phrase for telling marvels (II.B). The entry also tags the word to *moneo*.
- quotes:
  - sense I: "a divine omen indicating misfortune, an evil omen, portent"
  - sense I, Cicero citation (*Div.* 1, 42, 93): "ostenta, portenta, monstra, prodigia dicuntur"
  - sense II: "a monster, monstrosity (whether a living being or an inanimate thing)"
  - sense II.B: "monstra narrare, dicere, to relate wonders, prodigies"
- teaches: The Latin entry shows *monstrum* beginning as a religious omen of misfortune and only by transfer naming a monster or monstrosity, including a person's character.
- draft sentences:
  - Choose the culture's word for the being knowing that this word family begins as a warning: *monstrum* is first an evil omen, and the creature sense is a transfer from it (NEW-ScoutCryptozoology-3, sense I).
  - Let one word cover a beast, an object and a person, since the transferred sense covers a living being or an inanimate thing and a following subsection applies it to character (NEW-ScoutCryptozoology-3, sense II).
  - Group the portent vocabulary instead of isolating one term: the cited Cicero sentence collects *ostenta*, *portenta*, *monstra* and *prodigia* as one family of things that show, portend, point out and foretell (NEW-ScoutCryptozoology-3, sense I).
  - Give wonder-telling its own verb and occasion, because the entry records a phrase for relating wonders and prodigies, which makes the monster report a recognised performance rather than an aside (NEW-ScoutCryptozoology-3, sense II.B).
  - Decide whether an appearance is a sign to be read or a beast to be fought: a word that means omen first puts the creature inside a calendar of warnings before it puts it inside a landscape (NEW-ScoutCryptozoology-3, sense I).

### NEW-ScoutCryptozoology-4

- citation: University of Aberdeen, University Collections. n.d. "What is a Bestiary?" section of *The Aberdeen Bestiary* project site (Aberdeen University Library MS 24; manuscript written and illuminated in England around 1200). No author or publication date on the page.
- url: https://www.abdn.ac.uk/bestiary/about.php
- route: direct plain GET, HTTP 200, `text/html`, full "About The Manuscript" page read; 2026-10-22
- kind: web
- tier: A — the holding library's own published description of its manuscript and of the bestiary genre; descriptive, not an edition, so it is cited for the genre and the object's history, not for the text.
- scope: what a bestiary is as a book form (short descriptions of real and imaginary animals, birds and even rocks, each with a moralising explanation); that it was never meant to be a scientific text; that accurate observations carry the same weight as fabulous accounts; the manuscript's English origin around 1200 and its 1542 listing in the Old Royal Library inventory at Westminster.
- quotes:
  - section "What is a Bestiary?", first sentence: "a collection of short descriptions about all sorts of animals, real and imaginary, birds and even rocks, accompanied by a moralising explanation"
  - section "What is a Bestiary?", second sentence: "Although it deals with the natural world it was never meant to be a scientific text and should not be read as such."
  - section "What is a Bestiary?", third sentence: "Some observations may be quite accurate but they are given the same weight as totally fabulous accounts"
  - section "Project Background", second sentence: "written and illuminated in England around 1200"
- teaches: The holding library describes the bestiary as a moralising collection of real and imaginary animals that was never meant to be read as a scientific text.
- draft sentences:
  - If the world has a monster book, decide what kind of book it is: this form puts real and imaginary animals, birds and even rocks under one moralising explanation, so a monster sits beside the goat and the stone rather than in a separate volume (NEW-ScoutCryptozoology-4, "What is a Bestiary?").
  - Do not write the bestiary as proto-zoology: the library says in terms that it was never meant to be a scientific text, which frees the worldbuilder to make its truth-claims moral and its errors structural (NEW-ScoutCryptozoology-4, "What is a Bestiary?").
  - Give the compiler an explicit rule that weighs a true observation and a fabulous report equally, since that is the equal footing the page describes; the book's authority then rests on the moral, not on the sighting (NEW-ScoutCryptozoology-4, "What is a Bestiary?").
  - Write the book as a dated object with owners: an English manuscript of about 1200, later entered in a royal inventory, supplies a copy-history a found bestiary can inherit (NEW-ScoutCryptozoology-4, "Project Background" and "History of The Aberdeen Bestiary").

### NEW-ScoutCryptozoology-5

- citation: University of Aberdeen. n.d. "Folio 13r — Apes, continued. De satiris; satyrs. De cervis; deer", *The Aberdeen Bestiary* (Aberdeen University Library MS 24) folio page with transcription, facing translation, illustration commentary and codicological note.
- url: https://www.abdn.ac.uk/bestiary/ms24/f13r
- route: direct plain GET, HTTP 200, `text/html`, whole folio page read (translation, commentary, transcription); 2026-10-22
- kind: record
- tier: A — the holding library's digitisation of the folio with its own transcription, translation and commentary; authoritative for what the manuscript page says, not for the beings it describes.
- scope: how a composite being is filed and described inside a bestiary: sphinxes included among the apes; satyrs as "apes that men call satyrs" with attractive faces and pantomime gestures; the commentary's part-by-part body (partly goat, beard, horns, broad tail, human body, shaggy hair); the Ethiopian sky as the satyr's only homeland; the callitrix as a further neighbouring kind.
- quotes:
  - translation, end of the ape chapter: "Sphynxes are also included among apes."
  - translation, "Of satyrs": "There are also apes that men call satyrs."
  - commentary, paragraph on the satyr illustration: "He is partly like a goat with a beard, horns, and broad tail."
  - translation, "Of satyrs", on the callitrix: "They do not live elsewhere than under the Ethiopian sky, that is their native sky."
- teaches: A digitised folio shows a composite being filed among apes, named by hearsay, described part by part, and placed under a distant sky.
- draft sentences:
  - File the composite being inside an ordinary animal chapter instead of a monsters appendix: this bestiary puts sphinxes among the apes, and the filing decision does more worldbuilding than any description (NEW-ScoutCryptozoology-5, translation, ape chapter).
  - Let the compiler name the being by hearsay, as "apes that men call satyrs", so the book's authority is the report and not the observation (NEW-ScoutCryptozoology-5, translation, "Of satyrs").
  - Describe the hybrid body in the order a reader would check it — face, hair, beard, horns, tail, gait — because the folio's commentary anatomises the satyr exactly that way (NEW-ScoutCryptozoology-5, commentary).
  - Put the being at the edge of the known world and say so geographically: the folio gives the satyr no home but the Ethiopian sky, which it calls the creature's native sky (NEW-ScoutCryptozoology-5, translation, "Of satyrs").
  - Decide whether the monster's strangeness is anatomical or geographical; here it is both at once, a goat-and-man body assigned to a distant sky rather than to a nearby forest (NEW-ScoutCryptozoology-5, commentary and translation).

### NEW-ScoutCryptozoology-6

- citation: Hereford Cathedral. 2016 (published 8 June 2016; updated 20 July 2021). "Mappa Mundi." Cathedral website page. No named author.
- url: https://www.herefordcathedral.org/mappa-mundi
- route: direct plain GET, HTTP 200, `text/html`, full page read; 2026-10-22
- kind: web
- tier: A — the holding institution's own published account of the object in its care; a summary of the map's making and contents, not a scholarly edition and not a transcription of its legends.
- scope: the map as a spiritual and geographical record made about 1300 and bearing the name of Richard of Haldingham or Lafford; its drawing inventory (about 420 cities and towns, 15 biblical events, 33 plants, animals, birds and strange creatures, 32 images of the peoples of the world, 8 pictures from classical mythology); Jerusalem at the centre; the vellum sheet's dimensions.
- quotes:
  - paragraph on the map's significance, opening sentence: "it records how 13th-century scholars interpreted the world in spiritual as well as geographical terms"
  - paragraph on the vellum sheet: "reflects the thinking of the medieval Church with Jerusalem at the centre of the world"
  - paragraph on the drawings, first sentence: "Superimposed on to the continents are drawings of the history of humankind and the marvels of the natural world."
  - paragraph on the drawings, inventory list: "33 plants, animals, birds and strange creatures, 32 images of the peoples of the world"
- teaches: The cathedral's own account shows a world map that carries strange creatures, peoples and biblical events on the continents around a declared centre.
- draft sentences:
  - Decide what object carries the world's monsters: on this map strange creatures are drawn onto the continents beside cities, biblical events and peoples, so a monster is a map feature and a claim about the order of the world (NEW-ScoutCryptozoology-6, paragraph on the drawings).
  - Keep the map's own categories rather than merging them: plants, animals, birds and strange creatures are counted as one group and the peoples of the world as another, so decide whether a monster belongs with fauna or with nations (NEW-ScoutCryptozoology-6, paragraph on the drawings).
  - Declare a centre and let every position be relative to it, since this map is organised around Jerusalem and the creature's distance from that centre is part of its meaning (NEW-ScoutCryptozoology-6, paragraph on the vellum sheet).
  - Treat the map as an argument rather than a survey: the page describes it as a 13th-century reading of the world in spiritual as well as geographical terms, which licenses a monster-bearing map that is also a moral diagram (NEW-ScoutCryptozoology-6, paragraph on the map's significance).
  - Count the marvels if you want the catalogue to feel like an object: an inventory of 420 cities, 15 biblical events, 33 beasts and 32 peoples reads as a made thing with a budget, not as an open list (NEW-ScoutCryptozoology-6, paragraph on the drawings).


### NEW-ScoutCryptozoology-7

- citation: Australia Council for the Arts (now Creative Australia), 2019. *Protocols for using First Nations Cultural and Intellectual Property in the Arts*, third edition (first published 2002; revised 2007 and 2019). Compiled by Dr Terri Janke and Company from the True Tracks ICIP principles; © Australia Council 2019. PDF hosted by Creative Australia.
- url: https://creative.gov.au/sites/creative-australia/files/documents/2025-04/protocols-for-using-first-nati-5f72716d09f01.pdf
- route: direct plain GET, HTTP 200, `application/pdf` (9.2 MB), title pages, contents and the "Protocols in practice" sections at printed pp. 44–47 read this session; the landing page https://www.creative.gov.au/first-nations-arts/protocols-for-using-first-nations-cultural-and-intellectual-property-in-the-arts (HTTP 200) supplied the download link; 2026-10-22
- locator note: page numbers are the printed folios. PDF p. 53 carries no printed number and sits between pp. 44 and 46, so it is cited as printed p. 45.
- kind: docs
- tier: B — a national arts funding body's protocol guide drafted by an Indigenous legal practice: authoritative for the funder's requirements and for the principles it states, not a statement by any single community and not a source on any particular being.
- scope: the guide's working rules for restricted material: ancestral motifs named as the heritage of particular groups and possibly unsuitable for mass dissemination, the requirement to get permission from Indigenous custodians for each intended context, sacred or secret material and gender restrictions, and the rule against distorting an artwork that embodies a creation story. Not a description of any being, and not a substitute for a community's own public statement.
- quotes:
  - printed p. 44, "Traditional motifs", first sentence: "Indigenous traditional motifs such as the Wandjinas and Mimis are part of the cultural heritage of certain Indigenous groups."
  - printed p. 44, "Traditional motifs", second sentence: "They may not be suitable for mass communication or dissemination."
  - printed p. 44, "Traditional motifs", on custodians: "You should also get permission from Indigenous custodians."
  - printed p. 47, "Sensitive subject matter", second sentence: "it is not acceptable in Indigenous communities to circulate widely sacred or secret material or works that have any gender restrictions"
- teaches: A national arts body's protocol guide treats certain ancestral motifs and sacred or gender-restricted material as not for wide circulation without the custodians' permission.
- draft sentences:
  - Decide who may see the being at all, and make access a rule of the culture rather than the narrator's discretion, since the guide states that sacred or secret material and gender-restricted works are not to be circulated widely (NEW-ScoutCryptozoology-7, printed p. 47).
  - Treat an ancestral being as owned heritage with named custodians: the guide calls the Wandjinas and Mimis part of the cultural heritage of certain groups and says they may not suit mass dissemination (NEW-ScoutCryptozoology-7, printed p. 44).
  - Build a permission chain instead of a taboo list, because the guide's instruction is to get permission from the custodians and to discuss each intended context before use (NEW-ScoutCryptozoology-7, printed p. 44).
  - Let gender restriction be a real boundary in the setting, since the guide pairs sacred or secret material with works carrying gender restrictions in one rule (NEW-ScoutCryptozoology-7, printed p. 47).
  - Make fidelity part of the restriction, not only secrecy: the guide calls it culturally inappropriate to distort or adapt an artwork that embodies a creation story, so a copy that changes the being is a different kind of offence (NEW-ScoutCryptozoology-7, printed p. 45).

---

## How these rows should be used (integration notes for the L1)

- Section mapping: rows 3 and 1 carry "what the culture calls the being and what the word means" plus the omen leg; rows 5 and 4 carry composite anatomy and the bestiary as book/object; row 6 carries where monsters live on the map and who counts them; rows 1 and 2 carry the calibration (cryptozoology as a demarcation argument, not as "monsters are impossible").
- Do not let a draft sentence claim more than its quote: row 2 is a publisher description, so it evidences the book's stated programme only. Row 1 is an undergraduate research journal, so it evidences a stated academic argument, not a consensus of zoology.
- Row 3's Perseus text is italicised in the original; HTML extraction inserts spaces around commas, so quotes are given without those extraction spaces. The quoted words themselves are verbatim.
- Couples candidates: `myth-symbol/animal-symbolism.md` (owns fauna, the proximity/salience rules and the bestiary shelf at §7), `myth-symbol/cosmology-cosmography.md` (owns world maps and centres), `myth-symbol/symbolism-synthesis-method.md:29` (the "medieval Latin package" line that currently lacks a bestiary owner), `myth-symbol/divination-omen-systems.md` (omen mechanics: the entry should hand portent classification there), `verification/real-world-inspiration-boundaries.md` (the line between using a tradition and inventing one).
- A disagreement worth stating in the entry rather than smoothing: the Aberdeen project says a bestiary "should not be read" as a scientific text, while the monster-hunting literature (row 1) treats its own failure as a failure of scientific method. These are two different judgements about the same kind of book, and the entry is stronger for naming both.

## Result and unrun checks

- result: seven draft source rows (28 quotes) supplied, every quote re-checked verbatim against a saved copy of the file it is taken from (the PDF checked in reading order, not in `-layout` column order); no entry text and no SOURCES row was written, since the L1 owns both.
- evidence locations for re-checking: `/fast/scratch/hyaku/kotodama-r55/ScoutCryptozoology/{schembri.pdf,schembri.txt,monstrum.txt,abdn_about.html,abdn_f13r.html,hereford.html,icip.pdf}` and `/fast/scratch/hyaku/cup.html`.
- unrun: `python3 -B reports/round-55/accept-c.py`, `reports/round-28/readme/sweep.py`, `tools/check-source-access.py` — all three need the landed entry and its SOURCES rows, which this seat does not write.

## unopened

- `https://www.nature.com/articles/499406a` (Cressey, "Cryptozoology: Beastly fakes", *Nature* 499: 406, 2013): HTTP 200 but paywalled — the page renders only the standfirst and "This is a preview of subscription content"; the review body was not read. Paywall challenge met, not passed, so no quote is taken from it.
- `https://cup.columbia.edu/author-interviews/loxton-prothero-abominable-science/` (Columbia UP author interview with Loxton and Prothero): returns a Cloudflare "Just a moment..." interstitial to a plain request. Challenge met, not passed; the interview was not read.
- `https://journals.sagepub.com/eprint/N9EFE3V5GAZDPK57R8RQ/full` (Foxon 2024, "Heuvelmans the Heretic and Hidden Animals", accepted-manuscript eprint): HTTP 403 to a plain request. Not opened, so the paper is not cited.
- `https://www.britannica.com/topic/cryptozoology`: HTTP 403 to a plain request. Not opened.
- `https://www.jstor.org/stable/10.7312/loxd11532`: HTTP 200 but only a 3 KB landing shell with no readable body. Not used.
- The book *Abominable Science!* itself: not opened; only the publisher's description is cited, and the row's tier and scope say so.
