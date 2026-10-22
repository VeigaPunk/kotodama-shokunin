# ScoutPareMonsters — claim C source item: Paré, *Des monstres et prodiges* (1573)

Axes: coverage (a sourced row for the monsters entry) and accuracy (nothing quoted beyond what was opened).
Opened this session: three sources — the 1573 edition itself in the BIU Santé digitisation, the National
Library of Medicine's exhibition record of the same edition, and an open-access article on Paré's causes.
No installs, no upgrades. Tools used: `curl`, `pdftotext` (already present).

Reading note on the primary text: the Internet Archive item is a page-image scan with a machine OCR text
layer of sixteenth-century letterforms. The OCR is dense with long-s read as `f`, u/v exchange and broken
hyphenation (`monflres`, `Jont chofes`, `apparoifet`). The quotes below are the printed words with long s,
u/v and word division normalised; nothing is added or reordered. Quotations are marked where the OCR
itself is uncertain.

---

### NEW-ScoutPareMonsters-1

citation: Paré, Ambroise. 1573. *Deux livres de chirurgie*, second book: *Des monstres tant terrestres que marins, avec leurs portraicts*. Paris: André Wechel, with royal privilege. BIU Santé (Paris) copy 35181; Internet Archive item `BIUSante_35181` (contributor: Bibliothèque interuniversitaire de santé, Paris; scan public 2018-03-03).
url: https://archive.org/download/BIUSante_35181/BIUSante_35181_djvu.txt — item page https://archive.org/details/BIUSante_35181 — metadata https://archive.org/metadata/BIUSante_35181
route: direct plain request, HTTP 200, `text/plain`, 520,638 bytes (OCR text layer of the scanned volume); item metadata HTTP 200, item rights field "Licence ouverte / Open licence Etalab"; item description records "Preface, p. 1-5 ; au Lecteur, p. 581". Access date 2026-10-22.
kind: book
tier: A — the holding library's own digitisation of the 1573 edition; authoritative for what this edition prints, in its own words.
scope: the wording of Paré's definition of monster and prodigy, the thirteen causes of monsters, the chapters on composite human-animal bodies, terrestrial and marine monsters, and the case narratives Paré attaches to named places and dates (Verona, Brussels, Rome, the Nile, the sea off Norway, Angers). Does not support any claim about how sixteenth-century readers received the book, nor any modern medical reading of the conditions described.
quotes:
- Book II, opening definition of "monstres" (before ch. I): "Monstres sont choses qui apparaissent contre le cours de nature (& sont le plus souvent signes de quelque malheur à avenir)"
- Book II, ch. I "Des causes des monstres": "Les causes des monstres sont plusieurs. La première est la gloire de DIEU. La seconde, son ire."
- Book II, ch. XX, on beings born half beast and half human: "Il y a des monstres qui naissent moitié de figures de bêtes, & l'autre humaine"
- Book II, p. 484, the half-human calf and Albertus Magnus: "le pasteur fut délivré & purgé de l'imposition de tel exécrable crime"
teaches: Paré defines monsters as departures from nature's ordinary course and usually omens, then gives one birth thirteen causes from God to fraud: the word carries forecast and explanation.
draft sentences:
- A culture that calls a birth a monster rather than a prodigy places it against the ordinary course of nature but not against nature altogether, and Paré adds that such things are usually signs of some misfortune to come (NEW-ScoutPareMonsters-1, book II, opening definition).
- The first two causes are the glory of God and God's wrath, so the same body can be read as a divine sign before any bodily cause is weighed (NEW-ScoutPareMonsters-1, book II, ch. I).
- The remaining causes run through seed quantity, imagination, the narrowness of the womb, the mother's posture, a blow to the belly, hereditary disease, putrefaction, mixed seed, the trickery of beggars and demons (NEW-ScoutPareMonsters-1, book II, ch. I).
- Composite beings are built with a seam: a child conceived of a woman and a dog has the mother's parts above the navel and the animal's below, so the anatomy records where two natures were joined (NEW-ScoutPareMonsters-1, book II, ch. XX).
- Monsters are also pinned to real ground and dates — a sea monster seen at Rome on 3 November 1323, human above the navel, and a monk-shaped fish taken in the sea off Norway, which everyone who saw it called a monk — so a bestiary must decide whether its beings are single dated events or a standing population (NEW-ScoutPareMonsters-1, book II, ch. XXXII).
- A village's killing of such a being can itself be tried: near Verona in 1254 the man who killed a human-headed foal was acquitted, and at Brussels a pig-monster was killed with its mother for the horror the people had of it (NEW-ScoutPareMonsters-1, book II, ch. XX, p. 481).

### NEW-ScoutPareMonsters-2

citation: National Library of Medicine, History of Medicine Division. n.d. *From "Monsters" to Medical Miracles: Moments in the History of Conjoined Twins*, gallery "Age of Superstition", page "A Sixteenth-Century Woodcut" (2 of 4). Bethesda, Maryland. No author or publication date is given on the page.
url: https://www.nlm.nih.gov/hmd/topics/conjoined-twins/Pare_2274010R-sm.html
route: direct plain request, HTTP 200, `text/html`, 21,252 bytes. Access date 2026-10-22. (The gallery's `index.html` at the same path returned HTTP 404.)
kind: record
tier: A — a national medical library's published record and exhibition text about the copy and the woodcut it holds; authoritative for the object's fields and for the library's own stated assessment. It is not evidence of sixteenth-century reception.
scope: the library's characterisation of Paré's treatise and of the Verona twins' case, the figure's credit to the 1573 edition at p. 375, and the exhibition's placement of Paré in a gallery named "Age of Superstition". Does not support any claim about the number of editions, Paré's sources, or the twins' own testimony.
quotes:
- Gallery text on the woodcut, opening sentence: "surgeon Ambroise Paré brought a more scientific approach to the genre in his treatise, Des monstres et prodiges"
- Gallery text, second sentence: "His descriptions of malformed humans and animal-human hybrids avoided fantastical stories in favor of simple, realistic statements"
- Gallery text, on the twins: "joined at the posterior, from the shoulders to the buttocks and shared their kidneys"
- Gallery text, on the parents: "Their parents earned money by exhibiting the pair in various Italian cities"
teaches: A national medical library presents Paré's book as the Renaissance's sober monster treatise and records the Verona twins' public exhibition and the 1573 page of the woodcut.
draft sentences:
- The library characterises Paré's descriptions of malformed humans and animal-human hybrids as avoiding fantastical stories in favour of simple, realistic statements, which is a later institution's verdict on the book rather than the book's own method (NEW-ScoutPareMonsters-2, gallery text on the woodcut).
- The twins shown lived at Verona about 1475, were joined from the shoulders to the buttocks, shared their kidneys, and were exhibited by their parents in Italian cities to people burning to see the spectacle (NEW-ScoutPareMonsters-2, gallery text and figure caption).
- The cut is credited to Paré's *Deux livres de chirurgie*, Paris, André Wechel, 1573, page 375, so a bestiary plate is keyed to an edition and a page rather than to a species (NEW-ScoutPareMonsters-2, figure credit).
- The library places Paré in a gallery titled "Age of Superstition" while calling his work the monster book of the Renaissance, which shows the same object filed under two different judgements (NEW-ScoutPareMonsters-2, gallery heading and text).

### NEW-ScoutPareMonsters-3

citation: Eudave, Cecilia. 2014. "Del cuerpo monstruoso a la representación fantástica: el caso de Monstruos y prodigios de Ambroise Paré". *Sincronía* 18(66): 113–131. Universidad de Guadalajara, Departamento de Filosofía / Departamento de Letras. ISSN 1562-384X. Open access.
url: https://revistasincronia.cucsh.udg.mx/index.php/sincronia/article/download/890/1036/3103 — landing page https://revistasincronia.cucsh.udg.mx/index.php/sincronia/article/view/890
route: direct plain request, HTTP 200, `application/pdf`, 1,273,822 bytes, 19 pages; landing page HTTP 200 (`text/html`, 51,702 bytes) giving Vol. 18 Núm. 66 (2014): Enero-Junio, section LETRAS, pp. 113–131. Access date 2026-10-22.
kind: paper
tier: B — peer-reviewed open-access article in a university journal; authoritative for its own reading of Paré, not for Paré's text, which it quotes from a 1993 Spanish translation.
scope: a scholarly reading of Paré's causal scheme as a mix of divine, physiological, imaginary and demonic explanations, of likeness as the criterion that makes a body a monster, and of the book's continued appetite for marvels. Does not support any statement about the 1573 printing, and its quotations of Paré are from the Siruela translation, not the French.
quotes:
- Opening of the section on Paré's definition, p. 114: "Los monstruos son cosas que aparecen fuera del curso de la Naturaleza"
- Continuation of the same definition, p. 114: "y que, en la mayoría de los casos, constituyen signos de alguna desgracia que ha de ocurrir"
- On likeness as the premise, p. 115: "si se parece a nosotros es como nosotros, si no, es un aberración de la naturaleza"
- On the book's remaining marvels, p. 116: "dedica un gran número de páginas para hablar de monstruos de naturalezas increíbles en cielo, tierra y mar"
teaches: Eudave argues Paré's causal list mixes divine, physiological, imaginary and demonic explanations, marking a transition, while most of the book still catalogues marvels of sky, earth and sea.
draft sentences:
- The article reads the monster as a thing outside the course of nature that in most cases carries a sign of some misfortune to come, so naming a being is a forecast as much as a description (NEW-ScoutPareMonsters-3, p. 114).
- It states the premise as comparison: if it looks like us it is like us, and if not it is an aberration of nature, an error or a punishment, so a culture's yardstick of likeness decides who counts as a monster (NEW-ScoutPareMonsters-3, p. 115).
- It argues that Paré already attempts a subtle break at the level of the pseudo-scientific discourse by separating the monster from the prodigy, which lets a worldbuilder date its bestiary to a period of transition rather than a settled taxonomy (NEW-ScoutPareMonsters-3, p. 115).
- It observes that most of the book is still spent on monsters of incredible natures in sky, earth and sea, so the sober and the marvellous share one volume and one authority (NEW-ScoutPareMonsters-3, p. 116).

---

## What this hands to the entry

Observed facts, with the row that carries each:

- The two words are defined against each other, not against "normal": monster = against the course of nature and usually an omen; prodigy = wholly against nature (NEW-ScoutPareMonsters-1, definition). A worldbuilder must decide which of the two words its culture uses, because only the first still leaves the being inside nature.
- The causal list is the book's spine: thirteen causes spanning divine will, embryology, maternal imagination, injury, heredity, putrefaction, mixed seed, human fraud and demons (NEW-ScoutPareMonsters-1, ch. I). The same body therefore supports a religious, a medical, a legal and a sceptical reading, and the culture's institutions choose among them.
- Two legal cases show that choice being made. At Verona (1254) a villager killed a human-headed foal near the town and was acquitted on the ground of the horror it caused him (p. 481). At the half-human calf on p. 484 the villagers accused the shepherd in court and wanted him burned with the cow; Albertus Magnus answered with a special constellation and the shepherd was released. Who may reclassify a monster is therefore a question of standing, not of anatomy.
- Composite anatomy is recorded as a join: mother's parts above the navel, the animal father's below (ch. XX). The seam is the describable fact, and it is where a bestiary's plate will put its line.
- Location is concrete and dated: Rome, 3 November 1323, a sea monster human to the navel (ch. XXXII); the sea off Norway (Paré's "mer de Nortwege"), a monk-shaped fish named a monk as soon as it was taken (ch. XXXII); the Nile, a triton and a siren seen from the bank (ch. XXXII). Monsters arrive at named coasts on named days.
- Naming by resemblance is explicit: the fishermen's catch is a fish "lequel tost qu'il fut pris, chacun luy donna le nom de moine", and the caption reads "monstre marin ayant la teste d'un moine armé" (ch. XXXII). A culture's monster names are often the names of its own social roles.
- Paré says he collected the figures and stories from named wonder-books and authorities — Boaistuau's *Histoires prodigieuses*, Claude Desférant, Scripture, Hippocrates, Galen, Aristotle, Pliny, Lycosthenes (opening, after the definition). A bestiary in this genre is a compilation with a visible shelf behind it.
- Exhibition is part of the being's life: the Verona twins were shown in Italian cities for money (NEW-ScoutPareMonsters-2). Decision: does the monster live in hiding, at a court, at a fair, or in a book.

Inference, labelled as such:

- [INFERENCE] The three sources together describe a shift of authority rather than a shift of belief: the omen reading does not disappear, it is joined by an expert reading (surgeon, astrologer) that can dissolve a criminal charge. The entry should say "joined", not "replaced", because both readings sit in the same 1573 volume.
- [INFERENCE] NLM's "avoided fantastical stories" conflicts with the book's own citations of Boaistuau and its Nile and Norway-sea reports. The conflict is useful evidence for the entry's "what changes across periods" axis but must not be presented as a fact about the 1573 contents.

Cautions for the L1:

- Do not cite the 1573 copy for page numbers from the OCR sequence. The digitised text's running heads are not monotonic (they run 568, 574, 580, then 388, 400, 401, 474, 481, 484), so the text layer is either a bound-with or a duplicated scan. Locators above use book and chapter, with a page only where the printed head sits beside the quoted words (p. 481, p. 484, and NLM's p. 375 for the twins woodcut).
- The volume's title page names the second book *Des monstres tant terrestres que marins, avec leurs portraicts* (item metadata and title page), while the book's own head reads "DES MONSTRES ET PRODIGES". The entry may give both, but should not present "Des monstres et prodiges" as the 1573 title-page title.
- The Spanish article's Paré quotations come from the 1993 Siruela translation. If the entry quotes the definition, quote the French from NEW-ScoutPareMonsters-1, not the Spanish.

## fit with the round

- Ground: myth-symbol, monsters and hybrid beings; the entry's filename has no owner at base.
- This row set supplies the naming decision (monster vs prodigy), the causal inventory, composite anatomy as a seam, map placement with dates, the social life of the being (exhibition, killing, trial), the compiler's shelf, and the periodisation caution.
- It does not cover: heraldic or temple guardians, moralised beast fables, or non-European bestiaries. The entry will need other seats for guardian and moral functions; nothing here should be stretched to cover them.

unopened:
- Gallica (BnF) SRU query for Paré editions, https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&query=... — HTTP 403 Cloudflare block page ("Sorry, you have been blocked"). Challenge met, not passed; no attempt was made to route around it, and no Gallica text is used.
- OpenEdition Books, Yves Baille, "Les monstres chez Ambroise Paré : un regard rétrospectif", https://books.openedition.org/pup/6829 — HTTP 200, but the served "Texte intégral" is a freemium preview that stops mid-word ("...les bornes et limites de la chir…"); only the first two paragraphs and the plan are open. Not used, since three other sources carry the ground.
- NLM exhibition index, https://www.nlm.nih.gov/hmd/topics/conjoined-twins/index.html — HTTP 404 (site redesign notice). The gallery page itself was opened.
- Internet Archive item `BIUSante_01709` (Paré, *Les Œuvres*, 1585) — not opened; the 1573 copy already carries the passages needed.

## unrun checks

- No acceptance script was run (claim C belongs to the L1; `python3 -B reports/round-55/accept-c.py` is not mine to run).
- No registry edit was made; no S-id was assigned. Draft ids only: NEW-ScoutPareMonsters-1, -2, -3.
- Quote word counts were checked locally against the 25-word ceiling; no repo tool was run.
