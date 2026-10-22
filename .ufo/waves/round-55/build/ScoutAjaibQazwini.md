# ScoutAjaibQazwini — al-Qazwīnī's *ʿAjāʾib al-makhlūqāt* and the wonder-catalogue as a monster book

- seat: `KotodamaR55.ScoutAjaibQazwini` (scout, claim C ground: monsters and hybrid beings)
- round: kotodama 55 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `8eda9543e940bdc4938fad90182ee6a6fe271d0f`, claim base `f4015e70b829523ed81e14ce4279bfab0e0233e4`
- assignment: opened sources on Arabic and Persian wonder literature for claim C's monster and hybrid-being entry — how the genre classifies wonders and strange creatures, aimed at what a worldbuilder must decide
- draft ids used below: `NEW-ScoutAjaibQazwini-1` … `-5`; the L1 assigns the final `S` ids at integration
- access date for every source below: 2026-10-22. Every quotation in the five rows, and every page-carried string listed under Findings, was substring-checked against the saved bytes (0 misses, whitespace-normalised only).

## Route summary

| row | file actually read | route | bytes |
|---|---|---|---|
| 1 | `https://www.uni-muenster.de/imperia/md/content/arabistikislam/publikationen/2005_hees_the_astonishing.pdf` | direct plain `curl`, HTTP 200, `application/pdf`, 21 pages, text via `pdftotext -layout`; no challenge | 229251 |
| 2 | `https://www.nlm.nih.gov/hmd/arabic/natural_hist2.html` | direct plain `curl`, HTTP 200, `text/html`; no challenge | 14797 |
| 3 | `https://thedigitalwalters.org/Data/WaltersManuscripts/html/W593/description.html` | direct plain `curl`, HTTP 200, `text/html`; no challenge (URL re-checked live: HTTP 200, 123780 bytes) | 123780 |
| 4 | `https://web.archive.org/web/20250318040834/https://art.thewalters.org/object/W.659/` | live URL HTTP 403 to a plain request (5394-byte block page) — challenge met, not passed; read from Wayback capture `20250318040834` | 645244 |
| 5 | `https://web.archive.org/web/20250208230803/https://www.loc.gov/item/2021667318/` | live URL HTTP 403 to a plain request (5486-byte block page; the LoC search JSON endpoint also returned 403) — challenge met, not passed; read from Wayback capture `20250208230803` | 187117 |

Two transliteration cautions. The von Hees PDF is typeset with a legacy Arabic-transliteration font: `pdftotext` recovers `cağā7ib` and `cAğā7ib al-mahlūqāt` where the printed page has ʿajāʾib and ʿAjāʾib al-makhlūqāt. The four row quotes were chosen so that the mangled token never appears inside a quotation; the article's own words around it are quoted as printed. The museum records write the title as `'Aja'ib al-makhluqat`, `ʿAjāyib al-makhlūqāt va-gharāyib al-mawjūdāt` and `ʻAjāʼib al-makhlūqāt`; each quote keeps the record's own spelling.

---

### NEW-ScoutAjaibQazwini-1

citation: von Hees, Syrinx. 2005. "The Astonishing: a critique and re-reading of ʿAjāʾib literature." *Middle Eastern Literatures* 8(2): 101–120. DOI 10.1080/14752620500115452. Publisher's typeset PDF posted in the author's institute publications directory (Orientalisches Seminar, Rheinische Friedrich-Wilhelms-Universität Bonn).

url: https://www.uni-muenster.de/imperia/md/content/arabistikislam/publikationen/2005_hees_the_astonishing.pdf

route: direct plain request (curl), HTTP 200, `application/pdf`, 21 pages, read with `pdftotext -layout`; no challenge, no login, 2026-10-22

kind: paper

tier: A — the peer-reviewed article that makes this argument, read in the publisher's own typeset version, so authoritative for its thesis. B for any statement about medieval practice outside the three texts it discusses, which it treats as a sample. The transliteration-font mangling noted above means a quotation about the *word* must be taken from the printed page, not from the extracted bytes.

scope: what the genre label does and does not establish; what ʿajāʾib denotes (things that evoke astonishment, overwhelmingly real ones); how al-Qazwīnī's book is ordered; how large a share marvel-beasts take of it; where wholly fictitious places sit; what al-Qazwīnī says his purpose is. It is an argument about classification and about one author's stated aim, not a survey of monsters and not a source for any individual creature's description.

quotes:
- p. 101, Abstract: "I argue that the genre of literature of marvels does not exist"
- p. 102, "The Concept of ʿajāʾib Literature", on al-Qazwīnī's book: "In a systematic fashion it catalogues and describes all natural phenomena"
- p. 105, section "3. One-dimensional interpretation of the term ʿajāʾib": "the vast majority of which belong to the realm of reality"
- p. 105, same section: "these marvellous beasts represent a negligible, marginal phenomenon in the literature"

teaches: The genre title's word means things that evoke astonishment, mostly real; the article denies "wonders literature" is a genre and calls marvel-beasts marginal.

draft sentences:
- Fix the sense of your culture's wonder-word before you fill the book: ʿajāʾib names themes that evoke astonishment, and the article holds that the vast majority of them belong to the realm of reality (NEW-ScoutAjaibQazwini-1, p. 105).
- Do not let a shared title-word manufacture a genre: the article argues that "the genre of literature of marvels does not exist", and that grouping a sailors' anecdote collection, a traveller's compilation and a natural-history encyclopaedia under one label misreads all three (NEW-ScoutAjaibQazwini-1, p. 101).
- Order the catalogue from the top down — heavens, then the four elements, then the three natural kingdoms — because "In a systematic fashion it catalogues and describes all natural phenomena", and the monster inherits its slot from that order (NEW-ScoutAjaibQazwini-1, p. 102).
- Budget monsters as a tail rather than a spine: against the whole described creation "these marvellous beasts represent a negligible, marginal phenomenon in the literature", so a monster-heavy bestiary is a different kind of book (NEW-ScoutAjaibQazwini-1, p. 105).
- Put wholly invented places at the rim: the article's examples of places it calls fictitious sit "at the western and eastern edge of the world", not in the middle of the travelled map (NEW-ScoutAjaibQazwini-1, p. 105).
- Give the catalogue a stated purpose beyond inventory: al-Qazwīnī's declared aim is to restore in readers the amazement they had as children, and that astonishment is meant to end in knowledge of God (NEW-ScoutAjaibQazwini-1, p. 106).

---

### NEW-ScoutAjaibQazwini-2

citation: U.S. National Library of Medicine, History of Medicine Division. "Islamic Medical Manuscripts, Natural History 2: Note on ʿAjāʾib al-makhlūqāt wa-gharāʾib al-mawjūdāt." Catalogue note, no author or date on the page; cites Richter-Bernburg in *Encyclopedia of Arabic Literature* (1998) and Bosworth and Afshar in *Encyclopaedia Iranica* I: 695–9.

url: https://www.nlm.nih.gov/hmd/arabic/natural_hist2.html

route: direct plain request (curl), HTTP 200, `text/html`, no challenge, 2026-10-22

kind: docs

tier: B — a national library's curatorial note on a genre and on its own four copies; the genre paragraph summarises others' reference work rather than arguing from manuscripts, so it is strong secondary. A for what NLM says about its own holdings (the 1546 Mughal-workshop copy and the dated owner's stamp).

scope: the genre's name and scope ("mirabilia"), what kinds of topic it counted as wonder, the place it gives strange creatures (edges of the inhabited world), the affect it aims at (awe), the subject list that includes demons, and the translation history into Persian and Turkish with NLM's four Persian copies.

quotes:
- opening note, first sentence: "is the most well-known example of a genre of classical Islamic literature that was concerned with 'mirabilia' or wonders of creation"
- opening note, second paragraph: "The literature was concerned with cosmographical and geographical topics that challenged understanding."
- opening note, third paragraph, list of subject matter: "strange creatures at the edges of the inhabited world"
- opening note, second paragraph: "These could include aspects of God's creation that inspire awe, such as human anatomy or the variety of plants."

teaches: The National Library of Medicine describes the genre as works on cosmographical and geographical topics that challenged understanding, with strange creatures placed at the edges of the inhabited world.

draft sentences:
- Classify the book before you write it: NLM calls this treatise "the most well-known example of a genre of classical Islamic literature that was concerned with 'mirabilia' or wonders of creation" (NEW-ScoutAjaibQazwini-2, opening note, first sentence).
- Set the test at comprehension rather than at truth: the genre's topics are "cosmographical and geographical topics that challenged understanding", so a wonder is whatever outruns the reader's model of the world (NEW-ScoutAjaibQazwini-2, opening note, second paragraph).
- Place strange beings at the edge of the map and say so in the text: the page lists "strange creatures at the edges of the inhabited world" beside anatomy, plants and animals (NEW-ScoutAjaibQazwini-2, opening note, third paragraph).
- Choose awe over horror as the register: wonders may be "aspects of God's creation that inspire awe", and the page's examples are human anatomy and the variety of plants, not predators (NEW-ScoutAjaibQazwini-2, opening note, second paragraph).
- Plan for translation drift: the treatise was rendered into Persian and Turkish and survives in many illustrated copies, so a bestiary should name which language version it descends from (NEW-ScoutAjaibQazwini-2, holdings paragraphs).

---

### NEW-ScoutAjaibQazwini-3

citation: The Walters Art Museum. "Walters Ms. W.593, Wonders of creation." Digital Walters manuscript description (TEI-derived), principal cataloguer Adam Gacek; catalogue record for Walters Art Museum MS W.593, Persian, 10th century AH / 16th century CE, said to be written in Ottoman Turkey, 181 paintings; licensed CC BY-NC-SA 3.0.

url: https://thedigitalwalters.org/Data/WaltersManuscripts/html/W593/description.html

route: direct plain request (curl), HTTP 200, `text/html`, 123780 bytes; no challenge, no login, 2026-10-22

kind: record

tier: A — the holding museum's own catalogue description of its own manuscript, authoritative for the object's fields and for the museum's titles of its paintings. The titles are the cataloguer's English, not a translation of al-Qazwīnī's or al-Ṭūsī's words, so they are evidence of what is depicted and where, not of the text's phrasing.

scope: the manuscript's language version, date, size, illustration count, and the one-by-one titled list of its 181 paintings, which is the page's real value: it shows the text's sections indexed by town, island, sea and river, the world map inside the book, composite beings, and a dragon that guards a treasure. Also the record's own attribution knot: it names al-Ṭūsī as author of the Persian version and dates him to the sixth century AH / twelfth CE, earlier than al-Qazwīnī's death in 682 AH / 1283 CE, without resolving the conflict.

quotes:
- Abstract: "one hundred eighty-one paintings of different sizes"
- fol. 32a, illustration title: "A fabulous creature in Sind that appears at a fire-temple"
- fol. 44b, illustration title: "Divers in the Sea of ʿUmān save themselves by feeding the fish and monsters"
- fol. 178a, illustration title: "A bird like a peacock with a lion’s head"

teaches: A sixteenth-century Persian copy spreads its 181 paintings across named towns, islands and seas, includes a world map, and composes hybrids from two named animals.

draft sentences:
- Let the picture count carry the ambition: this copy is illustrated with "one hundred eighty-one paintings of different sizes", each titled separately, so the book's wonders are enumerated rather than implied (NEW-ScoutAjaibQazwini-3, Abstract).
- Index beings by toponym before species: the list runs "A fabulous creature in Sind that appears at a fire-temple", then entries tied to the Sea of ʿUmān, Lake Zarah, the Sea of Harkand and named islands (NEW-ScoutAjaibQazwini-3, fol. 32a and the following folio titles).
- Make the monster a cost of the route: in the Sea of ʿUmān "Divers … save themselves by feeding the fish and monsters", which turns the being into a toll on a named crossing (NEW-ScoutAjaibQazwini-3, fol. 44b).
- Compose hybrids out of two recognisable animals and name both: "A bird like a peacock with a lion’s head" is legible only because the parts are borrowed from known species (NEW-ScoutAjaibQazwini-3, fol. 178a).
- Put a map inside the wonder book: the sequence includes "First half of a map of the world" and its second half at fols. 52b–53a, so every later place name can be located on a diagram (NEW-ScoutAjaibQazwini-3, fol. 52b).
- Keep one monster in place as a guardian: a dragon guards the treasure found by Anūshīrvān and Būzurjmihr, so a being can hold a spot instead of roaming (NEW-ScoutAjaibQazwini-3, fol. 74a).

---

### NEW-ScoutAjaibQazwini-4

citation: The Walters Art Museum. "Turkish Version of the Wonders of Creation", accession W.659, Ottoman, 1121 AH/AD 1717, ink and pigments on European laid paper, 33 × 20 cm, scribe Muḥammad ibn Muḥammad Shākir Ruzmah-ʿi Nāthanī, 444 paintings, made at the request of Vizier Murtaḍā Pasha; acquired by Henry Walters, bequeathed 1931.

url: https://web.archive.org/web/20250318040834/https://art.thewalters.org/object/W.659/

route: live URL `https://art.thewalters.org/object/W.659/` returned HTTP 403 to a plain request (5394-byte block page) — challenge met, not passed; record read from Wayback capture `20250318040834` of the same URL (HTTP 200, 645244 bytes), 2026-10-22

kind: record

tier: A — the holding museum's own object record for its own manuscript, authoritative for the object's fields and for the museum's titles of the individual paintings listed under Related Objects. A for the titles as the museum's labelling; not a translation of the Ottoman text.

scope: the 1717 Ottoman Turkish version — patron, scribe, materials, size, 444 paintings — and the museum's titles of its paintings, which are the clearest published evidence of how this book names monsters: by borrowed body ("Half-crow, Half-man", "Having Two Bodies"), by deed ("Carries a Mountain with which to Kill Moses and His Men"), by eschatological people ("The Monster of Gog and Magog"), by place ("The Monster of the Caspian Sea", "Creatures of Saksar Island"), and by rank ("The King of the Jinnis Enthroned"). It carries one internal oddity to report rather than harmonise: it gives the author's death as 692 AH/AD 1293 where W.593 and the Library of Congress give 682 AH/1283, and it dates the vizier who commissioned it to the eleventh century AH/AD seventeenth, before the codex's own 1717 completion.

quotes:
- record description, first paragraph: "made at the request of the Vizier Murtaza Pasa (Murtadá Pasha)"
- record description, first paragraph: "There are 444 paintings illustrating the text."
- Related Objects list: "The Monster of Gog and Magog"
- Related Objects list: "The Creatures Zagh abu 'ujwah (Half-crow, Half-man) and Dhu al-badanayn (Having Two Bodies)"

teaches: An Ottoman vizier's 1717 Turkish copy, with 444 paintings, titles monsters by borrowed body and by deed: Gog and Magog, half-crow half-man, two-bodied.

draft sentences:
- Date and count the pictures, because expansion is visible as picture count: this codex was completed in 1121 AH/AD 1717 and "There are 444 paintings illustrating the text" (NEW-ScoutAjaibQazwini-4, record description, first paragraph).
- Name a hybrid by the parts it borrows: "The Creatures Zagh abu 'ujwah (Half-crow, Half-man) and Dhu al-badanayn (Having Two Bodies)" put the composition rule into the being's name (NEW-ScoutAjaibQazwini-4, Related Objects list).
- Name some beings by a deed instead of a body: "The Demon 'Uj ibn 'Unuq Carries a Mountain with which to Kill Moses and His Men" makes the giant a weapon inside a story the reader already knows (NEW-ScoutAjaibQazwini-4, Related Objects list).
- Keep one monster at the world's boundary: "The Monster of Gog and Magog" belongs to the wall that holds a people in, so its meaning is spatial and eschatological rather than zoological (NEW-ScoutAjaibQazwini-4, Related Objects list).
- Record the patron, because it explains the book's existence: the copy was "made at the request of the Vizier Murtaza Pasa", so a court official, not a scholar, is the reader being equipped (NEW-ScoutAjaibQazwini-4, record description, first paragraph).
- Sort the sea and island beings by name of water or island (the Caspian, Vaynah, Saksar, Aturan, Hanah, Qasr, Vaqvaq), so a reader can look a monster up by where a ship would meet it (NEW-ScoutAjaibQazwini-4, Related Objects list).

---

### NEW-ScoutAjaibQazwini-5

citation: Library of Congress, World Digital Library item, "The Wonders of Creation", LCCN 2021667318, digital id `hdl.loc.gov/loc.wdl/wdl.15264`; Arabic manuscript, 340 folios, 218 × 153 mm, dated 1838-11-20, scribe Muḥammad ibn Muḥammad Fāḍil, original resource at the Wellcome Library.

url: https://web.archive.org/web/20250208230803/https://www.loc.gov/item/2021667318/

route: live URL `https://www.loc.gov/item/2021667318/` returned HTTP 403 to a plain request (5486-byte block page), and `https://www.loc.gov/search/?q=ajaib+al-makhluqat&fo=json` also returned HTTP 403 — challenge met, not passed; record read from Wayback capture `20250208230803` (HTTP 200, 187117 bytes), 2026-10-22

kind: record

tier: B — the descriptive summary is World Digital Library partner data re-hosted by the Library of Congress, and the record says so ("Description based on data extracted from World Digital Library"), so tier B for the description of the work's structure. A for the record's own fields (extent, language, date, holding library), which are the holding institution's catalogue data.

scope: the work's three-part architecture (introduction, supra-terrestrial, terrestrial), the statement that monsters and angels form the closing section, the genre's Arabic-and-Persian extent, and one concrete late copy's physical description — a nineteenth-century Arabic paper codex of 340 folios in a European library.

quotes:
- Summary: "the first on supra-terrestrial, the second on terrestrial creatures"
- Summary: "Al-Qazwini concludes his work with a section on monsters and angels."
- Summary: "includes texts in Arabic and Persian that describe the marvels of the heavens and the earth"
- Notes: "Original resource extent: 340 folios ; 218 x 153 millimeters."

teaches: The Library of Congress record says the book ends with a section on monsters and angels, after supra-terrestrial then terrestrial creatures.

draft sentences:
- Decide whether monsters get their own chapter or sit inside zoology: this record says "Al-Qazwini concludes his work with a section on monsters and angels", so the category is a terminal book division (NEW-ScoutAjaibQazwini-5, Summary).
- Split the cosmos before you split the creatures: the work has "two sections, the first on supra-terrestrial, the second on terrestrial creatures", and every being inherits its section from that cut (NEW-ScoutAjaibQazwini-5, Summary).
- Expect the genre to travel in more than one language: the record says the genre "includes texts in Arabic and Persian that describe the marvels of the heavens and the earth" (NEW-ScoutAjaibQazwini-5, Summary).
- Know what your copy is: this one is Arabic, 340 folios at 218 × 153 mm, copied in 1838 and now in the Wellcome Library, so a late paper copy still carries a thirteenth-century monster chapter (NEW-ScoutAjaibQazwini-5, Notes and Created/Published).

---

## Findings for the L1

### What these five sources can carry, section by section

- **What a culture calls a monster, and what the word means.** Rows 1 and 2 are the pair to use. The genre word is not "monster": it is a word for what provokes astonishment, and the astonishment is mostly produced by real things (row 1, p. 105). The genre label "wonders of creation" is a modern grouping that row 1 argues against as a genre. Design consequence the entry can state: a culture's wonder-word is a *response* category, not a *species* category, so a being enters it by outrunning the reader's model, not by being hostile.
- **Composite anatomy.** Rows 3 and 4 give the naming rule in the museum's own titles: the composite is announced as two named parts ("Half-crow, Half-man", "Having Two Bodies", "A bird like a peacock with a lion’s head"). The body is borrowed from known species, and the name says the recipe. Row 4 adds "A Half-human, Half-frog Creature" and the pair "Dabbabi (Half-man, Half-bear) and Dabaghi (Half-wolf, Half-hyena)"; row 3, working in Persian two centuries earlier, adds "A man with wings and feet like a horse" and "A tree on Mount Lābīs with the heads of humans and animals growing from it". The pattern holds across two manuscripts and two languages, which is what makes it a method rather than one copyist's taste.
- **Where monsters live on the world's map.** Three independent placements, all quotable: edges of the inhabited world (row 2), fictitious places at the western and eastern edge (row 1, p. 105), and island/sea/water toponyms that function as index headings (rows 3 and 4 — Sind, the Sea of ʿUmān, Lake Zarah, the Sea of Harkand, the Caspian, Vaynah, Saksar, Aturan, Hanah, Qasr, Vaqvaq, Dhabikh). Row 3 also shows a two-folio world map inside the book, so the map and the monster list are the same apparatus.
- **Bestiaries and wonder catalogues.** Row 5 gives the book's architecture and the terminal monster-and-angels section; row 2 gives the genre's scope and NLM's four Persian copies with the earliest dated 1546 in a provincial Mughal workshop; row 1 gives the ordering principle and the purpose statement. Together they support the claim "wonder catalogue is a book form with a fixed order and a declared aim", which is the entry's method point.
- **The monster as omen, guardian, moral or devourer.** Row 3 (dragon guarding a treasure, fol. 74a; monsters as a sea hazard, fol. 44b) and row 4 (Gog and Magog as a boundary being; 'Uj ibn 'Unuq as the giant who attacks Moses; the enthroned king of the jinn) show functions assigned by narrative slot, not by species. Row 4's "A Long-legged Person who Climbs on the Shoulders of Strangers" and "A Sick Person and Creatures of Saksar Island" are function-first titles: the being is what it does to a person.
- **What changes across periods.** Rows 3, 4 and 5 give a dated series: a thirteenth-century Arabic compilation (row 5's text, in an 1838 copy), a sixteenth-century Persian version with 181 paintings (row 3), a 1717 Ottoman Turkish version with 444 paintings (row 4). The pictures multiply and the language changes; the classification vocabulary does not.
- **Who records it, and in what kind of book or object.** Rows 3–5 answer with named objects: a 232-folio Persian codex in Baltimore, a 33 × 20 cm Ottoman codex on European laid paper commissioned by a vizier, a 340-folio Arabic paper codex dated 1838 and held at the Wellcome. For "who depicts", the answer these records support is a paid scribe and a workshop, working from an author's text — not a lone observer.

### What these sources do not carry (leave to other seats)

- **Restricted beings.** Nothing here gives a community's own public statement about access to a being, a depiction, or a name. Row 4's jinn and demons are book subjects, not restricted knowledge; do not turn a manuscript's depiction of a jinn into a claim about who may look at it.
- **A monster's own words or a first-person text.** No source opened here quotes al-Qazwīnī describing a creature's body in his own prose; all body evidence is the museum's titles of paintings. If the entry needs Qazwīnī's own wording, that requires the Arabic text (Wüstenfeld's edition), which was not opened.
- **Any classical or medieval European bestiary overlap.** Deliberately not touched; `ScoutBestiaryAberdeen.md` holds that ground.

### Disagreements to report, not harmonise

- Author's death: row 4 gives "died 692 AH/AH 1293"; row 3 gives "d. 682 AH / 1283 CE"; row 5's summary gives "circa 1203-83". Report as a cross-record disagreement.
- Persian version's author: row 3 attributes the Persian text to Shams al-Dīn Muḥammad al-Ṭūsī and dates him to the sixth century AH / twelfth CE, earlier than al-Qazwīnī's death in 1283. The record does not resolve it. Do not build a chronology across rows 3 and 4 without flagging this.
- Patron's date: row 4 dates Vizier Murtaḍā Pasha to the eleventh century AH / seventeenth CE, while the codex he commissioned was completed in 1717. Report the record's own wording; it is not this seat's to correct.

### Extra page-carried evidence the L1 may use in prose (verified present, not quoted as row quotes)

From row 3's folio list: "A dragon guards the treasure found by Anūshīrvān and his vizier Būzurjmihr" (fol. 74a); "First half of a map of the world" (fol. 52b) and its second half (fol. 53a); "Giant women, who later became part of Alexander the Great’s army, battle warriors on horseback" (fol. 136a); "A king watches strange creatures (people of the sea)" (fol. 168b); "The demon Halhāl with an animal head and feet" (fol. 162a); "A sea-horse with large wings" (fol. 182b); "A man with wings and feet like a horse" (fol. 183a); "An angel warning the prophet Khiz̤r not to explore the depths of the Sea of Harkand" (fol. 46b — the warning being is an angel, and the prohibition is about *depth*, a usable restriction motif).
From row 4's Related Objects list: "The King of the Jinnis Enthroned in the Company of Two Attendants"; "A Half-human, Half-frog Creature"; "A Fish with the Head of an Owl"; "The Creatures Dabbabi (Half-man, Half-bear) and Dabaghi (Half-wolf, Half-hyena)"; "Two Neckless Inhabitants of Hanah Island"; "A Long-legged Person who Climbs on the Shoulders of Strangers"; "Queen of the Island of Vaqvaq".
From row 2: the treatise's subject list ends "angels, and demons", and NLM's four Persian copies include three "highly illustrated products of Indian workshops".

### Calibration notes for whoever writes the entry

- Row 1 is an argument, not a reference work. Cite it for "the label is contested" and "the word denotes astonishment", never as a neutral definition of a genre it denies.
- Rows 3 and 4 are museum catalogues: their titles are modern English editorial work. A sentence that says "the manuscript labels the being X" is safe; a sentence that says "the text calls the being X" is not, unless the Arabic or Persian is quoted.
- Row 5's summary is WDL partner data, so it is the weakest of the five for the work's structure, and the strongest for one copy's physical facts.
- All five agree that the beings sit inside a creation survey ordered from heavens to earth; none of them supports a reading of the monsters as a separate pantheon or as a species taxonomy.

## unopened

- `https://cudl.lib.cam.ac.uk/view/MS-NN-00003-00074/1` (Cambridge University Library, Persian ʿAjāʾib al-makhlūqāt, MS Nn.3.74) — HTTP 403 to a plain request; challenge met, not passed, and not routed around.
- `https://www.iranicaonline.org/articles/ajaeb-al-makluqat/` — HTTP 403 to a plain request; challenge met, not passed. The Encyclopaedia Iranica entry would be the obvious tier A genre row; it is the first thing a later round should retry.
- `https://www.loc.gov/item/2021667228/` and `https://www.loc.gov/item/2021667227/` (LoC's other Qazwīnī items, seen in search results) — not requested individually; the LoC host answered HTTP 403 to both a plain item request and the search JSON endpoint in this session, so a further attempt was judged the same block.
- Wüstenfeld's edition and German translation, *Zakarija ben Muhammed ben Mahmud al-Cazwini's Kosmographie* (Göttingen, 1848–9), and the Arabic text itself — not located in an ordinary public copy and not searched further; without it no row here quotes al-Qazwīnī's own words.
- al-Qazwīnī's four introductory passages on ʿajāʾib, which row 1 cites in its note 38 — the passages live in the Arabic text, which was not opened, so row 1's account of the author's aim is second-hand by one step and its tier note says so.
- The Harvard dissertation *The Ethics of Wonder: The Persian Qazvini Corpus (1300–1632)* (`https://dash.harvard.edu/entities/publication/faa539e9-c7eb-4f0b-abaf-1b6035466fe5`) — seen as a search lead only, not opened; it is the natural next row for period drift across thirty Persian manuscripts.
- The Public Domain Review collection page on the Mughal Persian translation — seen as a search lead, not opened, because an image-collection page is tier C for the text.
- `https://art.thewalters.org/object/W.593/` (the live object record for the Persian copy) — not requested separately: its content is superseded for this question by the Digital Walters description, which the museum publishes with the folio-level titles.

## unrun checks

No lane command was run: claim C's acceptance (`reports/round-55/accept-c.py`), the README sweep and `tools/check-source-access.py` belong to the L1 at integration, and no corpus file was edited by this seat. No install or upgrade was made; no tool version changed this session (curl 8.23.0, poppler `pdftotext` used as present).
