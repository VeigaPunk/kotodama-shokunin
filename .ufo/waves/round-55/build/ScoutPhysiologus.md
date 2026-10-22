# ScoutPhysiologus — claim C source report (Physiologus and the medieval bestiary)

Two sources were opened in this session (2026-10-22) by plain `curl` from
`/fast/scratch/hyaku/kotodama-r55/ScoutPhysiologus/`, each returning HTTP 200: the British
Library's own account of the bestiary, and the Getty's *Book of Beasts* exhibition page with
its official object checklist. No browser, no challenge, no bypass, no paywall. No tool
installs and no pacman (the preinstalled `pdftotext` was used only to confirm checklist item
numbers and page numbers). Seat name for draft ids: `ScoutPhysiologus`.

Finding in one line: the two institutions say the same two things from opposite ends — the
bestiary is a *variable* book whose creatures are read morally inside a Christian world view
(British Library), and it is a *popular* book type whose beasts also leave the page for
vessels, caskets and tapestries (Getty); between them they supply the entry's book-type,
function, illustration practice, a map-edge monster, the place of legendary peoples in the
book, and the object afterlife.

---

### NEW-ScoutPhysiologus-1

citation: Harrison, Julian. 2019. "What is a bestiary?" British Library, *Medieval manuscripts blog*, 18 August 2019. — https://www.bl.uk/stories/blogs/posts/what-is-a-bestiary
url: https://www.bl.uk/stories/blogs/posts/what-is-a-bestiary
route: direct plain request, HTTP 200 (native), full page read, 2026-10-22
kind: web
tier: A — the British Library's own curator describes the Library's own bestiaries and states the institution's account of the genre; authoritative for what the Library says and holds. Caveat: a dated institutional blog post, not a peer-reviewed study, so use it for the genre's stated function, the Library's holdings and its catalogue facts, not for contested dating or authorship.
scope: what the Library says the bestiary is for (each creature read inside a Christian world view, the animals taken as evidence of God's divine plan); the genre's descent from the Greek *Physiologus* with Isidore's *Etymologies* added around the eleventh century; the variability of copies (families; number and order of animals differ); that illustrators of exotic beasts worked from text and imagination; the whale mistaken for an island; and the scale of survival (the Getty catalogue's 62 illuminated Latin bestiaries dispersed across the United Kingdom, Belgium, Denmark, France, Germany, Italy, the Netherlands, Russia and the USA, 8 of them at the British Library, whose eight shelfmarks the page lists from Add MS 11283 to Stowe MS 1067).
quotes:
- Function and origins, ¶1: "each creature was described in terms of its place within the Christian worldview, rather than as a purely scientific phenomenon"
- Function and origins, ¶2, quoting Elizabeth Morrison: "the bestiary was not a single text, but a series of changeable texts that could be reconfigured in numerous ways"
- Real and imagined, ¶1: "normally, the artists were relying upon the text and their own imaginations when depicting such beasts, rather than working from first-hand experience"
- Bestiary folklore, ¶1: "the whale was so large that it could rest on the surface of the water until greenery grew on its back"
teaches: The bestiary reads every creature as moral evidence within a Christian world view, and it is a variable family of texts illustrated from words rather than observation.
draft sentences:
- Decide whether a beast entry explains nature or judges it: the British Library says each creature was described "in terms of its place within the Christian worldview, rather than as a purely scientific phenomenon", so the entry's job is signification before zoology (NEW-ScoutPhysiologus-1, Function and origins, ¶1).
- Draw the composite body from the sentence rather than the specimen, because the Library says "normally, the artists were relying upon the text and their own imaginations when depicting such beasts, rather than working from first-hand experience" (NEW-ScoutPhysiologus-1, Real and imagined, ¶1).
- Put a monster where the map runs out: in the bestiary the whale could rest on the surface until greenery grew on its back, so sailors took it for an island and camped on it before it dived (NEW-ScoutPhysiologus-1, Bestiary folklore, ¶1).
- Fix the culture's catalogue as one recension among several: the Library quotes Elizabeth Morrison that the bestiary "was not a single text, but a series of changeable texts that could be reconfigured in numerous ways", with the number and order of animals varying between copies (NEW-ScoutPhysiologus-1, Function and origins, ¶2).

### NEW-ScoutPhysiologus-2

citation: The J. Paul Getty Museum. 2019. "Book of Beasts: The Bestiary in the Medieval World", exhibition 14 May–18 August 2019, with the exhibition checklist dated 25 April 2019 (© 2019 J. Paul Getty Trust). — https://www.getty.edu/art/exhibitions/bestiary/ and https://www.getty.edu/art/exhibitions/bestiary/downloads/beasts_checklist.pdf
url: https://www.getty.edu/art/exhibitions/bestiary/ (exhibition page); https://www.getty.edu/art/exhibitions/bestiary/downloads/beasts_checklist.pdf (object checklist, 24 pages)
route: exhibition page direct plain request, HTTP 200 (native), full page read; checklist direct plain request, HTTP 200, `application/pdf` (5,595,978 bytes), text extracted and page-checked; 2026-10-22
kind: record
tier: A — the holding and exhibiting museum publishes the exhibition page and the official object checklist; authoritative for what the exhibition showed, the shelfmarks it lists and the museum's own characterisation of the bestiary. Caveat: curatorial copy and object labels, not a scholarly argument, so it carries no claim about the genre's origin or about the manuscripts' provenance beyond the checklist fields.
scope: the museum's definition of the bestiary as a popular medieval book describing the beasts of the world; the claim that beast imagery moved out of manuscripts into other media; and the checklist's identification of a "Legendary Peoples" opening in a bestiary (Ms. Ludwig XV 4, fols. 117v–118, Franco-Flemish artist, 1277 or after) and a brass lion aquamanile (Los Angeles County Museum of Art, about 1250), alongside caskets, tapestries, plates, a parade saddle and further bestiary leaves from the Northumberland and Aberdeen bestiaries.
quotes:
- Exhibition page, opening paragraph: "a popular type of medieval book describing the beasts of the world"
- Exhibition page, opening paragraph: "they often “escaped” from manuscripts to inhabit other art works made during the medieval period"
- Checklist no. 5–6, PDF p. 2 of 24: "Legendary Peoples, 1277 or after"
- Checklist no. 23, PDF p. 5 of 24: "Lion Aquamanile (Water Vessel), about 1250"
teaches: A bestiary is a popular book of beasts whose creatures also leave the page for vessels and objects, and one of its leaves can show legendary peoples.
draft sentences:
- Name the book by its genre rather than its author: the Getty calls the bestiary "a popular type of medieval book describing the beasts of the world", which makes a beast catalogue a book type that many makers can vary (NEW-ScoutPhysiologus-2, exhibition page, opening paragraph).
- Decide whether the monstrous peoples belong in the beast book or in a separate travel account: a bestiary in the exhibition carries a section titled "Legendary Peoples" across the facing leaves Ms. Ludwig XV 4, fols. 117v–118 (NEW-ScoutPhysiologus-2, checklist no. 5–6, PDF p. 2 of 24).
- Let the beast leave the page: the Getty says the creatures often "escaped" from manuscripts into other art works, and the checklist sets a brass "Lion Aquamanile (Water Vessel), about 1250" beside bestiary leaves, so the same body can be a marginal painting and a pouring vessel (NEW-ScoutPhysiologus-2, exhibition page, opening paragraph; checklist no. 23, PDF p. 5 of 24).

---

## What the pair is good for, and what it is not

- Good for: the bestiary as a moralised book type rather than zoology (1); its descent from the *Physiologus* and Isidore (1); copy-to-copy variation and modern family classification (1); illustration from text and imagination, which is the mechanism behind composite anatomy (1); the whale-island as a monster that occupies a place on the map (1); the survival count and the dispersal of the corpus, with the Library's own eight shelfmarks (1); legendary peoples inside a bestiary and beast forms on vessels and other objects (2).
- Not good for: any statement that the bestiary had one fixed text, one author or one purpose; any claim about how a bestiary was read aloud, taught or used liturgically (neither page says); any date or provenance for Ms. Ludwig XV 4 beyond the checklist's "1277 or after"; any claim that all bestiaries include the legendary peoples; and any statement about the *Physiologus*'s own date, language history or theology, which neither page supplies.
- The whale and the "escaped" beasts are the pair's two map-and-object facts; do not stretch either into a general theory of monstrosity. The moral reading is the Library's characterisation of the Latin bestiary, and it should be cited as such.

## Also opened, not filed

The University of Aberdeen's Aberdeen Bestiary project was opened at https://www.abdn.ac.uk/bestiary/ (HTTP 200) and folio 1r at https://www.abdn.ac.uk/bestiary/ms24/f1r (HTTP 200): the holding library's transcription and translation show the book opening with Genesis 1:1–5 and the Creation miniature before any beast. It is a strong tier-A candidate for a third row (the book's created order as the frame for its creatures), but the seat instruction capped this report at two sources, so it is recorded here as an opened page the L1 may file or leave.

## Unopened

- https://www.getty.edu/art/exhibitions/book_beasts/ — direct request, HTTP 404 (stale path for the same exhibition; the live page is `/art/exhibitions/bestiary/`).
- https://www.getty.edu/art/mobile/center/beasts/list.php — direct request, HTTP 502 on two attempts (GettyGuide object list, "Stop 952 Exhibition Overview" per search snippet); not used.
- https://digital.bodleian.ox.ac.uk/objects/1b4bfa22-2b07-4c52-a4be-7d5f0e0f5a6c/ — direct request, HTTP 404 (a guessed object id, not the real one).
- https://www.getty.edu/art/collection/exhibition/103Q8Z — HTTP 200 but the body is rendered client-side and only metadata came back; not used as evidence.
- Leads located in search results and not opened: the Bodleian catalogue record for MS. Ashmole 1511 (`https://medieval.bodleian.ox.ac.uk/catalog/manuscript_290`) and the Digital Bodleian facsimile of the same manuscript; both would make a good tier-A record for one named bestiary's structure and provenance if the entry needs it.
