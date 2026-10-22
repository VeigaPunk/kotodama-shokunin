# ScoutBestiaryAberdeen — the Aberdeen Bestiary on naming, composing and judging a monster

- seat: `KotodamaR55.ScoutBestiaryAberdeen` (scout, claim C ground: monsters and hybrid beings)
- round: kotodama 55 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `8eda9543e940bdc4938fad90182ee6a6fe271d0f`, claim base `f4015e70b829523ed81e14ce4279bfab0e0233e4`
- assignment: one or two opened sources on the Aberdeen Bestiary for claim C's monster and hybrid-being entry; quote a moralised reading of a monstrous creature and the bestiary's own framing of animals as lessons
- draft ids used below: `NEW-ScoutBestiaryAberdeen-1` … `-4`; the L1 assigns the final `S` ids at integration

## Route summary (one source, four files)

Everything below was opened by ordinary means — plain `curl`, no browser, no challenge, no archive needed.
Two URLs families, read as one source: the University of Aberdeen's digitisation of its own manuscript
(Aberdeen University Library MS 24) and that project's own explanatory page.

| file | URL | status | bytes |
|---|---|---|---|
| folio 13r (apes cont., satyrs, deer) | `https://www.abdn.ac.uk/bestiary/ms24/f13r` | direct plain request, HTTP 200 | 18778 |
| folio 11v (ibex cont., hyena) | `https://www.abdn.ac.uk/bestiary/ms24/f11v` | direct plain request, HTTP 200 | 19217 |
| folio 15v (bear cont., leocrota) | `https://www.abdn.ac.uk/bestiary/ms24/f15v` | direct plain request, HTTP 200 | 19831 |
| "What is a Bestiary?" | `https://www.abdn.ac.uk/bestiary/what.php` | direct plain request, HTTP 200 | 26105 |

Two further pages were also opened and are reported in Findings as unregistered evidence (folio 65v, folio 15v's
neighbour folio 69v, and the project's About page), because the entry's four rows should stay on the pages that
carry what each row claims.

Access date for every file above: 2026-10-22. Page shape: each folio page carries a heading, the running English
translation, a `Commentary` block (`Text`, `Illustration`, `Comment`, `Folio Attributes`) and a `Transcription and
Translation` block with the Latin. Quotations below are byte-checked against the fetched HTML (all four files
re-checked by substring match, 0 misses).

---

### NEW-ScoutBestiaryAberdeen-1

citation: Aberdeen University Library, MS 24 (the Aberdeen Bestiary), folio 13r, England, c. 1200; digitised with Latin transcription and English translation by the University of Aberdeen Bestiary Project. No author or publication date on the page.

url: https://www.abdn.ac.uk/bestiary/ms24/f13r

route: direct plain request (curl), HTTP 200, no challenge, 2026-10-22

kind: book

tier: A — the holding library digitises its own manuscript and prints the Latin transcription beside its translation; primary for this folio's text. The English wording is the project's own translation, so a claim about English phrasing is a claim about the project's rendering, not about a published scholarly edition.

scope: how this copy's satyr chapter names and builds a hybrid (face, gestures, goat's beard and horns, broad tail, shaggy human body), how the illustration note describes the figure and its thyrsus, the chapter's placement of satyrs and sphynxes among apes, and the one-sky habitat given to the neighbouring callitrix. Says nothing about satyrs in classical sources or in other bestiary copies, and gives the satyr no moral reading.

quotes:
- translation, `Of satyrs`, first sentence: "There are also apes that men call satyrs. They have quite attractive faces, and are restless, making pantomimed gestures."
- translation, `Of satyrs`, end of the sphynx passage: "Sphynxes are also included among apes."
- translation, `Of satyrs`, sphynx description: "They have shaggy hair on their arms and are easily taught to forget their wild nature."
- commentary, `Illustration`: "He is partly like a goat with a beard, horns, and broad tail."
- commentary, `Illustration`: "His rather human body is covered with shaggy hair."
- commentary, `Illustration`: "He holds his thyrsus or wand, used in his lustful and disorderly revels."
- translation, `Of satyrs`, on the callitrix: "They do not live elsewhere than under the Ethiopian sky, that is their native sky."

teaches: A bestiary names a hybrid by what people call it, then gives it a face, a part-by-part body, one far-off sky and an attribute, and no moral.

draft sentences:
- Name the being by report before you describe it: the satyr paragraph opens with apes "that men call satyrs", so the category comes from usage and the description follows (NEW-ScoutBestiaryAberdeen-1, translation, Of satyrs).
- Build the body as a list of borrowed parts rather than a single invention: a quite attractive face, restlessness and pantomimed gestures in the text, a goat's beard, horns and broad tail in the picture note (NEW-ScoutBestiaryAberdeen-1, commentary, Illustration).
- File the hybrid inside a familiar genus so it inherits that genus's properties — satyrs and sphynxes are both "included among apes", and the ape chapter is where wild nature can be taught away (NEW-ScoutBestiaryAberdeen-1, translation, Of satyrs).
- Place a marginal being by giving it a single sky: the bearded, broad-tailed callitrix of the same chapter lives nowhere but "under the Ethiopian sky", named as its native sky (NEW-ScoutBestiaryAberdeen-1, translation, Of satyrs).
- Give the being an object and an occasion rather than a threat: the thyrsus or wand marks it as a reveller in lustful and disorderly rites, not a predator (NEW-ScoutBestiaryAberdeen-1, commentary, Illustration).

---

### NEW-ScoutBestiaryAberdeen-2

citation: Aberdeen University Library, MS 24 (the Aberdeen Bestiary), folio 11v, England, c. 1200; digitised with Latin transcription and English translation by the University of Aberdeen Bestiary Project. No author or publication date on the page.

url: https://www.abdn.ac.uk/bestiary/ms24/f11v

route: direct plain request (curl), HTTP 200, no challenge, 2026-10-22

kind: book

tier: A — same holding-library digitisation and transcription as row 1; primary for this folio's text and for the project's illustration note on it.

scope: the hyena chapter end to end — the body rule (sometimes male, sometimes female), the tomb dwelling and corpse diet, the rigid spine, the night circling of shepherds' houses and the learned imitation of human speech, the explicit allegory identifying the sons of Israel with the hyena, and the manuscript's own "unclean, not to be eaten" judgement in the illustration note. Also the tail of the preceding ibex moralisation, which shows the same page's method of reading a body part as doctrine. Does not support any claim that this allegory is the only medieval reading of the hyena.

quotes:
- translation, `Of the hyena`, opening: "There is an animal called the hyena, which inhabits the tombs of the dead and feeds on their bodies."
- translation, `Of the hyena`, second sentence: "Its nature is that it is sometimes male, sometimes female, and it is therefore an unclean animal."
- translation, `Of the hyena`, on the spine: "Since its spine is rigid, all in one piece, it cannot turn round except by turning its body right around."
- translation, `Of the hyena`, on the lure: "by listening carefully learns their speech, so that it can imitate the human voice"
- translation, `Of the hyena`, the allegory: "The sons of Israel resemble the hyena."
- translation, `Of the hyena`, the proof text: "My heritage is to me as the den of a hyena."
- commentary, `Illustration`: "The hyena should not be eaten because it is dirty and has two natures, male and female."
- translation, end of the preceding ibex chapter: "with the harmony of the two Testaments as if with a sound constitution"

teaches: The hyena chapter fuses a monstrous body, a tomb diet, a voice-mimicking lure and a scriptural allegory, then rules the animal unclean and inedible.

draft sentences:
- State the monster's anomaly as a rule of nature, not as a sighting: the hyena is "sometimes male, sometimes female", and that is the stated ground of its uncleanness (NEW-ScoutBestiaryAberdeen-2, translation, Of the hyena).
- Let dwelling and diet carry the judgement before any moral is spoken: it inhabits the tombs of the dead, feeds on their bodies, and digs up graves in search of buried bodies (NEW-ScoutBestiaryAberdeen-2, translation, Of the hyena).
- Give the being a mechanism for its danger that a hearer could act on: it circles shepherds' houses by night, learns human speech by listening, and imitates a voice to draw a man out (NEW-ScoutBestiaryAberdeen-2, translation, Of the hyena).
- Close the entry with an explicit identification and its scriptural warrant — "the sons of Israel resemble the hyena", the synagogue compared to an unclean animal, the den of a hyena from the prophet (NEW-ScoutBestiaryAberdeen-2, translation, Of the hyena).
- Decide the restriction explicitly: the note on the picture says the hyena should not be eaten because it is dirty and has two natures (NEW-ScoutBestiaryAberdeen-2, commentary, Illustration).
- Show the method beside the monster, on the same page: the ibex's two horns are read as the harmony of the two Testaments (NEW-ScoutBestiaryAberdeen-2, translation, end of the preceding chapter).

---

### NEW-ScoutBestiaryAberdeen-3

citation: Aberdeen University Library, MS 24 (the Aberdeen Bestiary), folio 15v, England, c. 1200; digitised with Latin transcription, English translation and editorial commentary by the University of Aberdeen Bestiary Project. No author or publication date on the page.

url: https://www.abdn.ac.uk/bestiary/ms24/f15v

route: direct plain request (curl), HTTP 200, no challenge, 2026-10-22

kind: book

tier: A — the holding library's record of its own leaf: the part-list and the lacuna statements are the project's editorial commentary on this manuscript, not a secondary retelling. B for the lost text itself, which this leaf does not carry.

scope: the leocrota's composite anatomy as the project's illustration commentary reconstructs it, its stated origin in India, the project's note that the verbal description has dropped out of this copy, and the project's list of pages missing from this copy (leocrota, crocodile, manticore, start of parander). Supports "the composite body is assembled from named animals' parts" and "this copy is defective"; does not supply the lost leocrota wording or any manticore text.

quotes:
- commentary, `Illustration`: "The leocrota is a swift animal born in India."
- commentary, `Illustration`, the part-list: "It is the size of an ass with the hindquarters of a stag, the chest and legs of a lion"
- commentary, `Illustration`, the impossible jaw: "a continuous jawbone instead of teeth"
- commentary, `Comment`: "The last part of the description is absent from this text but is clearly illustrated and occurs in other versions."
- commentary, `Comment`: "there are pages missing for leocrota, crocodile, manticore, and start of parander."

teaches: Aberdeen's leocrota page shows composite anatomy assembled from borrowed parts, a text that has lost its ending, and a page-lacuna list naming the manticore.

draft sentences:
- Compose the hybrid from measured borrowings, each part named with its donor animal, rather than from a single grotesque stroke: ass's size, stag's hindquarters, lion's chest and legs (NEW-ScoutBestiaryAberdeen-3, commentary, Illustration).
- Put the one impossible feature where it does the work — a jaw continuous instead of teeth — and decide whether your book states it or only draws it (NEW-ScoutBestiaryAberdeen-3, commentary, Illustration).
- Expect the page to be the unit of loss: this copy's leocrota description breaks off, "clearly illustrated" but absent from the text, and the project lists missing pages for the leocrota, the crocodile and the manticore (NEW-ScoutBestiaryAberdeen-3, commentary, Comment).
- Treat a bestiary as a workshop with gaps, not a closed canon: a named monster can be missing from the copy in front of you while other copies carry the text (NEW-ScoutBestiaryAberdeen-3, commentary, Comment).

---

### NEW-ScoutBestiaryAberdeen-4

citation: University of Aberdeen, "What is a Bestiary?", with the sections "The Origin of the Text" and "The Families of Text", in *The Aberdeen Bestiary* project site for Aberdeen University Library MS 24. No author or publication date on the page.

url: https://www.abdn.ac.uk/bestiary/what.php

route: direct plain request (curl), HTTP 200, no challenge, 2026-10-22

kind: docs

tier: A — the holding library's own account of the genre and of its manuscript's place in it, which is exactly the scope claimed. B if used for any statement about a bestiary outside this project's holdings.

scope: the project's definition of a bestiary (short descriptions of real and imaginary animals, birds and stones, each with a moralising explanation), its refusal to treat the genre as natural science, the equal weight given to accurate and fabulous observation, the illustrations' stated didactic justification, and the genre's descent from Physiologus with about 50 chapters. Does not date or localise this manuscript; that is on the project's About page (see Findings).

quotes:
- section `What is a Bestiary?`, first sentence: "A bestiary is a collection of short descriptions about all sorts of animals, real and imaginary, birds and even rocks"
- section `What is a Bestiary?`, first sentence, continued: "accompanied by a moralising explanation"
- section `What is a Bestiary?`, second sentence: "Although it deals with the natural world it was never meant to be a scientific text and should not be read as such."
- section `What is a Bestiary?`, third sentence: "Some observations may be quite accurate but they are given the same weight as totally fabulous accounts."
- section `What is a Bestiary?`, on the pictures: "painted partly for pleasure but justified as a didactic tool"
- section `What is a Bestiary?`, the quoted aim, as the page itself truncates it: "to improve the minds of ordinary people, in such a way that the soul will at least perceive"
- section `The Origin of the Text`, on Physiologus: "It consisted of around 50 chapters about beasts, birds and stones used as a vehicle for explaining Christian dogma."
- section `The Origin of the Text`, on the gloss: "A moralising Christian gloss was added to these stories by a person presumably known as Physiologus."

teaches: The Aberdeen project defines a bestiary as moralised animal description in which accurate and fabulous accounts carry equal weight, written to teach rather than to describe nature.

draft sentences:
- Give the wondrous animal and the ordinary one the same kind of entry, because in this genre accurate observation and a fabulous account are "given the same weight" (NEW-ScoutBestiaryAberdeen-4, section What is a Bestiary?).
- Attach a moralising explanation to every natural description, and do not let the book be read as natural science — the library says plainly it was never meant as one and should not be read as such (NEW-ScoutBestiaryAberdeen-4, section What is a Bestiary?).
- Plan the pictures as argument: they are painted partly for pleasure but "justified as a didactic tool" aimed at ordinary people's minds and souls (NEW-ScoutBestiaryAberdeen-4, section What is a Bestiary?).
- Inherit the form knowingly: it descends from Physiologus, about 50 chapters of beasts, birds and stones explaining Christian dogma, with a moralising gloss added afterwards (NEW-ScoutBestiaryAberdeen-4, section The Origin of the Text).
- Name the recension you are imitating rather than "the medieval bestiary": the project dates the genre's present form to twelfth-century England, compiled from earlier sources (NEW-ScoutBestiaryAberdeen-4, section What is a Bestiary?).

---

## Findings for the entry's design decisions

Map from the six decisions named in the assignment to what the opened pages actually carry. Every line is
observed unless marked inference.

| design decision | what MS 24 shows | evidence |
|---|---|---|
| what the culture calls the being and what the word means | chapters are titled in Latin by a lemma (`De satiris`, `De Yena`) and the English translation opens with the naming formula "apes that men call satyrs" — name by report, then describe | f13r translation; f11v transcription |
| how its body is composed | two different techniques: a part-by-part donor list (ass, stag, lion, horse for the leocrota) and a small set of human-plus-animal features plus an attribute (face, gestures, goat beard, horns, tail, thyrsus for the satyr) | f15v commentary; f13r translation and commentary |
| where it lives relative to the known world | by a single sky or a single human site: the callitrix only "under the Ethiopian sky"; the leocrota "born in India"; the hyena in tombs and around shepherds' houses by night | f13r; f15v; f11v |
| whether it warns, guards, punishes, teaches or devours | MS 24's monsters devour and lure (hyena eats corpses, learns speech, draws a man out) and then are read as doctrine (sons of Israel); the satyr neither threatens nor teaches — it revels | f11v; f13r |
| who records or depicts it, in what book or object | a monastic or cathedral book of moralised nature, copied in England around 1200, with a programme of full-page and framed miniatures plus marginal sketches, pricking and ruling visible; the project's About page puts it in the Old Royal Library by 1542 as No. 518 `Liber de bestiarum natura` | f13r/f15v `Folio Attributes`; about.php (Findings below) |
| what changes across periods | the project's own history of the text: Physiologus (Greek, Alexandria, c. fourth century, about 50 chapters) → Latin versions Y/A/C/B → the bestiary proper in twelfth-century England; and within one copy, losses and additions (the manticore page missing here) | what.php; f15v commentary |

### Opened but not registered as rows (the L1 may register any of these; each was opened this session)

**Folio 65v — the dragon as devourer, and the illustrator overruling the text.**
`https://www.abdn.ac.uk/bestiary/ms24/f65v` (direct plain request, HTTP 200, 2026-10-22, 18723 bytes).
This is the cleanest moralised reading of a monstrous creature in the copy, delivered as an address to the reader
rather than as a labelled allegory: the text warns the reader to "Take heed, therefore, O man, and stay within the
catholic faith", and to be careful "that the dragon, the serpent of old, does not seize you and devour you, as Judas
was at once devoured by the devil and perished" (translation, end of the dragon chapter). Body: "The dragon is bigger
than all other snakes or all other living things on earth." (translation, Of the dragon, first sentence — the page
then breaks to the next folio). The illustration note records a text/image divergence worth a sentence of its own:
"The text says the dragon has a crest, small mouth and does not kill with its teeth but with its tail."
(commentary, Illustration) and "The illustrator has added massive teeth and wings." (commentary, Illustration).

**Folio 69v — the siren is not a woman-fish in this copy.**
`https://www.abdn.ac.uk/bestiary/ms24/f69v` (direct plain request, HTTP 200, 2026-10-22, 19869 bytes).
The chapter `De sirenis` describes, in the translation, "white snakes, with wings, called sirens" in Arabia, faster
than horses and also said to fly, with no moral reading and no hybrid woman's body. Direct corroboration that a
name which later means a mermaid means a winged serpent here: the word travels, the body does not. (Inference from
this page plus the general repertoire; the page itself says only what it says.)

**Folio 12v — the ape's moralisation.**
`https://www.abdn.ac.uk/bestiary/ms24/f12v` (direct plain request, HTTP 200, 2026-10-22, 19188 bytes).
"The Devil has the form of an ape, with a head but no tail." (translation, Of apes). Useful if the entry wants a
second, very short example of the describe-then-identify move on a near-human animal.

**About page — date, origin and provenance.**
`https://www.abdn.ac.uk/bestiary/about.php` (direct plain request, HTTP 200, 2026-10-22, 9878 bytes).
"The manuscript, written and illuminated in England around 1200" and, for the after-history, "listed as No.518 Liber
de bestiarum natura in the inventory of the Old Royal Library, at Westminster Palace" in 1542, the library
"assembled by Henry VIII, with professional assistance from the antiquary John Leland". Also "one of the best
examples of its type due to its lavish and costly illuminations". The entry's opening paragraph needs the date and
the English origin; this page is where they are stated, so it probably deserves its own row.

**Manuscript index.** `https://www.abdn.ac.uk/bestiary/ms24` (HTTP 200, 206 items) is the full folio-by-folio table
of contents; it is how I located the satyr, hyena, leocrota, dragon, siren and snake chapters. If the L1 wants a
"where monsters sit in the book's order" claim, this is the page for it: the creatures are interleaved with real
animals throughout (lion at f7r, satyr at f13r, hyena at f11v, leocrota at f15v, dragon at f65v, siren at f69v),
not segregated into a monsters section.

### Caveats the L1 should carry into the rows or the entry

- The English is the project's translation, not a named published edition; every quote above is a quote of this
  digitisation's rendering. Latin transcriptions are on the same pages and are the project's diplomatic text.
- Folio pages print translations that begin or end mid-sentence, because the chapter continues on the neighbouring
  leaf. Do not quote a page-opening fragment as though it were the chapter's first sentence without saying so.
- The transcription prints line breaks as backslash marks, so no Latin quotation above is multi-line; I used
  translation-side quotes only, plus the chapter rubric names as locators rather than as quoted text.
- Tier note: A here means "the holding library on its own manuscript for this scope", matching QUALITY criterion 6.
  Nothing in these four rows needs a B downgrade, but the what.php row should not be stretched to statements about
  bestiaries in general beyond what the project says.
- Nothing in these pages supports any claim about monsters in non-Latin-Christian traditions; that ground belongs
  to other seats.

## Not run

No lane command was run: this is a read-only scouting seat and the entry that consumes these rows does not exist
yet, so `python3 -B reports/round-55/accept-c.py` would only re-measure the base (0 cited ids). No file in the lane
was created or modified except this report. No tool was installed or upgraded.

unopened: the Oxford, Bodleian Library's Ashmole Bestiary facsimile, which the Aberdeen commentary names as the
witness carrying the leocrota's lost ending and the manticore — not opened, because the assignment's two-source
budget was spent on the Aberdeen files and the manticore's own text is another seat's ground; the digitised leaf
images (`/bestiary/jpeg/f13r.jpg` and siblings) — not opened, since the project's own illustration commentary is a
stronger record of what the leaf shows than my reading of a JPEG; `history.php`, `codicology.php`,
`introduction.php`, `help.php` and `bibliography.php` on the same site — linked from the pages I read, not opened,
outside the question asked.
