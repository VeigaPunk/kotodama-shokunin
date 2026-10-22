# ScoutNorseMonsters — claim C source report (Norse monster lineage: Snorri's Gylfaginning and Völuspá)

Two sources were opened in this session (2026-10-22) by plain `curl` from
`/fast/scratch/hyaku/kotodama-r55/ScoutNorseMonsters/`, each HTTP 200: Brodeur's English
Gylfaginning on sacred-texts, and Bellows's *Poetic Edda* in the Project Gutenberg
transcription of the 1923 edition. No browser, no challenge, no captcha, no paywall, no
bypass. No tool installs and no pacman. Seat name for draft ids: `ScoutNorseMonsters`.

Working files (scratch only, not lane bytes): `out_pre04.htm` (sacred-texts page),
`brodeur_gylf.txt` (same page with tags stripped and space runs collapsed; the printed page
markers `{p. NN}` survive in it), `pg73533.txt` and `pg18947.txt` (Gutenberg plain text,
CRLF). Quote checks: each quoted string below was tested for exact containment in those
files after collapsing line breaks and space runs only; wording, punctuation and the
typographic apostrophes are unchanged.

Finding in one line: Snorri gives the three children of Loki and one giantess a single
parentage, then separates them by *place* (the sea around all land, Niflheim, the gods' own
home) and by *restraint* (two fetters that failed, a third made of impossibilities, a pledge,
a sword for a gag), while Völuspá puts the breeding of the wolf-kin at Ironwood in the east
and makes the brood an omen in the sky — and the word Ironwood is, in Bellows's printed
note, "a conjectural emendation of an obscure phrase".

---

### NEW-ScoutNorseMonsters-1

citation: Snorri Sturluson. *The Prose Edda*, trans. Arthur Gilchrist Brodeur (1916), Gylfaginning. Read in the Internet Sacred Text Archive copy, which the site titles "The Prose Edda — Brodeur English Translation". The 1916 year is confirmed inside this session from two opened pages: Bellows's General Introduction names "the admirable translation by Arthur G. Brodeur, published by the American-Scandinavian Foundation in 1916", and Internet Archive metadata record `proseedda00brodgoog` (creator "Brodeur, Arthur Gilchrist, 1888-", date 1916) answers on a plain JSON request, HTTP 200.
url: https://sacred-texts.com/book/the-prose-edda/gylfaginning
route: direct plain request with redirect: `https://sacred-texts.com/neu/pre/pre04.htm` answered 301 and the reader served HTTP 200 at the URL above (`text/html`, 387,542 bytes); page text extracted in full, the cited chapters read in full, 2026-10-22
kind: book
tier: A — a public copy of a public-domain English translation of the medieval text, authoritative for what this translation's Gylfaginning says at the chapters quoted. It is not evidence for the Old Norse wording, for manuscript readings, or for the date of composition; those need the Old Norse editions and are out of this row's scope.
scope: the naming and parentage of Loki (ch. XXXIII); the three children by the giantess Angrboda and their three placements (ch. XXXIV); the naming of Hel's hall and its furniture and her half blue-black, half flesh-colour body (ch. XXXIV); the binding of the wolf — two fetters that broke, Gleipnir and its six impossible ingredients, the pledge of a hand in the mouth, the band that tightens under struggle, the rock and pin, the sword-gag, the river Ván (ch. XXXIV); the gods' stated reason for not killing the wolf (ch. XXXIV); and the wolf at the Weird of the Gods with its jaw against earth and heaven (ch. LI). Chapter numbers are this copy's continuous Roman numbering of Gylfaginning.
quotes:
- Gylfaginning ch. XXXIII (p. 41), opening sentence on Loki: "he is named Loki or Loptr, son of Fárbauti the giant; his mother was Laufey or Nál"
- Gylfaginning ch. XXXIV (p. 42), the three children: "one was Fenris-Wolf, the second Jörmungandr--that is the Midgard Serpent,--the third is Hel"
- Gylfaginning ch. XXXIV (p. 42), the serpent's placement: "he cast the serpent into the deep sea, where he lies about all the land"
- Gylfaginning ch. XXXIV (p. 42), Hel's placement: "Hel he cast into Niflheim, and gave to her power over nine worlds"
- Gylfaginning ch. XXXIV (p. 42), the furniture of Hel's hall: "Pit of Stumbling, her threshold, by which one enters; Disease, her bed; Gleaming Bale, her bed-hangings"
- Gylfaginning ch. XXXIV (p. 45), the wolf's condition for the third fetter: "let some one of you lay his hand in my mouth, for a pledge that this is done in good faith"
- Gylfaginning ch. XXXIV (p. 45), the band under strain: "the fetter became hardened; and the more he struggled against it, the tighter the band was"
- Gylfaginning ch. XXXIV (p. 45), the gag: "they thrust into his mouth a certain sword: the guards caught in his lower jaw, and the point in the upper"
- Gylfaginning ch. XXXIV (p. 45), why the wolf is not killed: "So greatly did the gods esteem their holy place and sanctuary, that they would not stain it with the Wolf's blood"
- Gylfaginning ch. XXXIV (p. 45), the close of the binding episode: "there he lies till the Weird of the Gods"
- Gylfaginning ch. LI (p. 78), the wolf at the Weird of the Gods: "Fenris-Wolf shall advance with gaping mouth, and his lower jaw shall be against the earth, but the upper against heaven"
teaches: Snorri names Loki's three children by one giantess, places each of them differently, and binds the wolf with a fetter, a pledge and a sword.
draft sentences:
- Decide what a name carries into a people's mouth before you decide the body: Snorri opens with the pedigree, "he is named Loki or Loptr, son of Fárbauti the giant; his mother was Laufey or Nál", so the being arrives classified by kin first and by shape later (NEW-ScoutNorseMonsters-1, Gylfaginning ch. XXXIII, p. 41).
- Count the brood as one family and give each member a different address rather than one monster province: "one was Fenris-Wolf, the second Jörmungandr--that is the Midgard Serpent,--the third is Hel", and the sea, Niflheim and the gods' own home take one each (NEW-ScoutNorseMonsters-1, Gylfaginning ch. XXXIV, p. 42).
- Put the world-encircling body in the water that is the map's edge: the gods "cast the serpent into the deep sea, where he lies about all the land", which makes the ocean a boundary with a tenant (NEW-ScoutNorseMonsters-1, Gylfaginning ch. XXXIV, p. 42).
- Furnish the other world instead of mapping it: Hel's hall is named through its objects, "Pit of Stumbling, her threshold, by which one enters; Disease, her bed; Gleaming Bale, her bed-hangings", so a visitor learns the realm by what it does to them (NEW-ScoutNorseMonsters-1, Gylfaginning ch. XXXIV, p. 42).
- Bind a monster by consent and craft, not only by force: the wolf sets his own price, "let some one of you lay his hand in my mouth, for a pledge that this is done in good faith", and the band answers struggle by tightening (NEW-ScoutNorseMonsters-1, Gylfaginning ch. XXXIV, p. 45).
- Give the culture a rule that explains why the monster is kept rather than killed: "So greatly did the gods esteem their holy place and sanctuary, that they would not stain it with the Wolf's blood", and the same book ends with that wolf's "lower jaw shall be against the earth, but the upper against heaven" (NEW-ScoutNorseMonsters-1, Gylfaginning ch. XXXIV, p. 45; ch. LI, p. 78).

### NEW-ScoutNorseMonsters-2

citation: *The Poetic Edda*, trans. Henry Adams Bellows (New York: The American-Scandinavian Foundation, 1923). Project Gutenberg eBook #73533 (release date 4 May 2024), produced from images made available by the Internet Archive/Canadian Libraries. Völuspá stanzas and Bellows's notes; Grimnismol 39 and its note; General Introduction; Völuspá Introductory Note.
url: https://www.gutenberg.org/cache/epub/73533/pg73533.txt
route: direct plain request, HTTP 200 (`text/plain`, 977,828 bytes by HEAD; 24,314 lines; the cited stanzas, notes and introductions read in full), 2026-10-22
kind: book
tier: A — the public-domain translation read in a full plain-text transcription, authoritative for the poem's English wording and for what Bellows's own notes and introduction claim. Bellows's editorial judgements inside those notes (a tenth-century date, the eclipse reading, the Ironwood emendation) are scholarly opinion and are tier B if a sentence presents them as fact rather than as his statement.
scope: the giantess in Ironwood bearing "the brood of Fenrir" and the one in monster's guise who will steal the sun (Völuspá 40); the wolf that tears men in the hall on Nastrond beside Nithhogg (Völuspá 38–39); the fetters bursting and the wolf running free (44); Bellows's identifications in the notes (Nithhogg glossed "the Dread Biter", the brood as Skoll and Hati, the eclipse reading, Ironwood as a conjectural emendation); the poem's preservation in the Codex Regius with a materially different Hauksbók order and his caution about the two hundred years before writing; his gloss of ragna rök; and the General Introduction's account of the prose Edda — manuscripts of the thirteenth and early fourteenth centuries, "clearly a handbook for poets", the attribution to Snorri resting on a note in the Uppsalabok written some fifty or sixty years after his death in 1241, and Brodeur's 1916 translation.
quotes:
- Völuspá 40, first two lines: "The giantess old | in Ironwood sat, In the east, and bore | the brood of Fenrir"
- Völuspá 40, lines three and four: "Among these one | in monster’s guise Was soon to steal | the sun from the sky"
- Völuspá 39, last two lines: "There Nithhogg sucked | the blood of the slain, And the wolf tore men"
- Völuspá 44, second line: "The fetters will burst, | and the wolf run free"
- Note to Völuspá 39, on the dragon: "Nithhogg (“the Dread Biter”): the dragon that lies beneath the ash Yggdrasil"
- Note to Völuspá 40, identifying the brood: "The children of this giantess and the wolf Fenrir are the wolves Skoll and Hati"
- Note to Völuspá 40, on the reading of the omen: "Some scholars naturally see here an eclipse-myth."
- Note to Grimnismol 39, on the place name: "Ironwood: a conjectural emendation of an obscure phrase"
- General Introduction, on the poem's manuscript: "known as the Codex Regius (R2365), has been the basis for all published editions of the Eddic poems"
- Völuspá Introductory Note, on the two versions: "The order of the stanzas in the Hauksbok version differs materially from that in the Codex Regius"
- Völuspá Introductory Note, on the name of the end: "the phrase describing it, ragna rök, “the fate of the gods,”"
- Völuspá Introductory Note, on transmission: "How much the poem was altered during the two hundred years between its composition and its first being committed to writing"
- General Introduction, on the prose work's date: "Preserved in various manuscripts of the thirteenth and early fourteenth centuries"
- General Introduction, on the prose work's kind: "This work, clearly a handbook for poets, was commonly known as the “Edda” of Snorri Sturluson"
- General Introduction, on the attribution: "some fifty or sixty years after Snorri’s death, which was in 1241"
teaches: The poem breeds the wolf-kin at Ironwood in the east, has one of them steal the sun, and leaves the place name a modern editor's conjecture.
draft sentences:
- Put the breeding ground at the edge of the map and give it a name the tradition keeps: Völuspá puts her there in one line, "The giantess old | in Ironwood sat, In the east, and bore | the brood of Fenrir", so the monsters' origin is a place, not a species (NEW-ScoutNorseMonsters-2, Völuspá 40).
- Make the monster an omen with an effect in the sky rather than only a body at the border: one of the brood comes "in monster’s guise" and is fated to steal "the sun from the sky" (NEW-ScoutNorseMonsters-2, Völuspá 40).
- Show how much a worldbuilder inherits from editors: Bellows calls Ironwood "a conjectural emendation of an obscure phrase", so a province fixed on the map rests on a guess about a damaged word (NEW-ScoutNorseMonsters-2, note to Grimnismol 39).
- Treat the moral or natural reading as a reading on the record: Bellows writes, "Some scholars naturally see here an eclipse-myth", which lets the same omen be a sky event for one teller and a judgement for another (NEW-ScoutNorseMonsters-2, note to Völuspá 40).
- Keep the variants and say which one you follow: the stanzas survive in the Codex Regius and in a Hauksbók version whose order "differs materially from that in the Codex Regius", so one tradition reaches a world in two arrangements (NEW-ScoutNorseMonsters-2, Völuspá Introductory Note).
- Separate the two kinds of book a monster can live in: the poem is one thing, and the prose work is "clearly a handbook for poets", attributed to Snorri by a note written "some fifty or sixty years after Snorri’s death, which was in 1241" (NEW-ScoutNorseMonsters-2, General Introduction).

---

## What the pair is good for, and what it is not

Design decisions the two rows can carry for the entry:

1. **What the culture calls the being.** A name arrives with kin and parentage (Loki: father a giant, mother named), and the words the text uses for them are relational — giantess, wolf, serpent, Hel — and it has no single word that gathers them.
2. **How the body is composed.** The three children are separate bodies with separate fates, not one composite; a hybrid body is not what these two rows describe. Hel's half blue-black, half flesh-colour body is the one mixed body described here, and it is given as a mark of recognition.
3. **Where it lives on the map.** Three placements for one brood: the encircling sea, Niflheim, and the gods' own home where the wolf is fostered. The map axis is placement by assignment, not habitat.
4. **Omen, guardian, moral, or devourer.** The wolf is kept alive by a rule about sanctuary, not by mercy, and kept until the end; in Völuspá the brood is an omen in the sky (sun-stealing) and a devourer of men at the corpse-strand.
5. **Who records it, and in what kind of book.** One row is a prose work that Bellows calls "clearly a handbook for poets", preserved in thirteenth- and early-fourteenth-century manuscripts and attributed to Snorri on a note written some fifty or sixty years after his death; the other is a poem preserved in the Codex Regius with a second, reordered version. Both are books about words — the stanzas, and the prose that explains them for poets.
6. **What changes across periods.** The prose systematises what the poem leaves as pictures: the poem names Ironwood and the brood, the prose supplies the two failed fetters, the pledge, the gag and the river, and adds the gods' own reason. Bellows's notes then record the modern uncertainty (the Ironwood word, the eclipse reading, the transmission), which is exactly where a worldbuilder must choose rather than copy.

What these rows do **not** carry, and should not be cited for: any Old Norse lexical sense of *jötunn*, *þurs* or *hamr* (no dictionary row was opened; see unopened below); any manuscript-object description written by a holding library (the Codex Regius appears only in a translator's introduction, not in a Royal Library or Árni Magnússon Institute record); any archaeological depiction (no object record opened this seat); and any claim about living practice or belief.

## Also opened, not filed as a row (for the L1 to promote or drop)

Project Gutenberg eBook #18947, *The Younger Edda; Also called Snorre's Edda, or The Prose Edda*, trans. Rasmus Björn Anderson (release date 31 July 2006, most recently updated 4 August 2024) —
https://www.gutenberg.org/cache/epub/18947/pg18947.txt — direct plain request, HTTP 200
(`text/plain`, 407,617 bytes), landing page https://www.gutenberg.org/ebooks/18947 also
HTTP 200, 2026-10-22. This is a second, earlier English translation (Anderson, not Brodeur);
its Gylfaginning ch. IX gives the same three children, so it corroborates row 1 across two
independent translations. It also carries a translator's index that classifies the beings
outright, useful for the naming decision:

- "FENRIS-WOLF. The monster wolf, son of Loke." (index, s.v. FENRIS-WOLF)
- "LOKE. The giant-god of the Norse mythology." (index, s.v. LOKE)
- "LYNGVE. The island where the Fenris-wolf was chained." (index, s.v. LYNGVE)

If the entry wants the point that nineteenth-century English paratext calls Loki a
"giant-god" and the wolf a "monster wolf", this copy is the row for it; otherwise it stays
evidence only.

unopened:
- Dictionary of Old Norse Prose (ONP), University of Copenhagen, https://onp.ku.dk/onp/onp.php — HTTP 200 but the shell served an `altcha` proof-of-work challenge script and no entry content; challenge met, not passed, and not bypassed. No lexical row for *jötunn* / *þurs* / *hamr* this seat.
- handrit.is record for GKS 2365 4to (Codex Regius), https://handrit.is/manuscript/view/is/GKS04-2365 — HTTP 403 (the site root answers 200); not opened, no bypass attempted.
- Cleasby–Vigfússon *An Icelandic-English Dictionary* at the Germanic Lexicon Project, https://www.ling.upenn.edu/~kurisuto/germanic/oi_cleasbyvigfusson_about.html — HTTP 403; not opened.
- Brodeur's Gylfaginning on the old sacred-texts path https://sacred-texts.com/neu/pre/pre04.htm — 301 only; the reader URL in row 1 is what was read.
