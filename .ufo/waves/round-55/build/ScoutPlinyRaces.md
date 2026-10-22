# ScoutPlinyRaces — Pliny's monstrous *nations* and the wonder-catalogue as a book

- seat: `KotodamaR55.ScoutPlinyRaces` (scout, leaf; no subagents, no background jobs)
- round: kotodama 55 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `8eda9543e940bdc4938fad90182ee6a6fe271d0f`, claim base `f4015e70b829523ed81e14ce4279bfab0e0233e4`
- assignment: claim C source item — Pliny the Elder, *Natural History* 7.2, the monstrous races of Scythia, India and Ethiopia, with Pliny's sources and his framing of the races at the edge of the world; and one second source by ordinary means
- draft ids used below: `NEW-ScoutPlinyRaces-1` and `-2`; the L1 assigns the final `S` ids at integration
- nothing was installed or upgraded this seat; no LSP server answers a web page, so every statement below is a literal reading of the opened file and is labelled with its locator; no semantic-proof claim is made

## Scope check against the brief

The brief named Arimaspi, Astomi, Sciapodes, Blemmyes. Three of those four are in the chapter; **Blemmyes are not in *NH* 7.2** and I did not quote them. The chapter's only headless-type people are a neckless tribe with "eyes in their shoulders", listed inside the Monocoli paragraph; the named Blemmyes would need a different text and a different row, and I did not open one. I did not chase them this seat because the entry's naming, body and map axes are already carried by the peoples below; the gap is recorded rather than papered over.

## Route summary (two sources; every file quoted was opened this session)

Everything below was opened by ordinary means — plain `curl`, no browser, no archive, no challenge, no key.

| source | file read | status | size | sha256 of the fetched file |
|---|---|---|---|---|
| Pliny, *NH* 7.2 (Bostock–Riley) | `pliny7_2_en.html`, text extracted by tag-strip to `pliny7_2_en.txt` | direct plain request, HTTP 200 | 697032 B | `69a92700bb84299ac07d0010bbd5b1797347d1baaa17eca35f776ca4095ff30d` |
| Gellius, *NA* 9.4 (Rolfe) | `gellius9.html`, text extracted to `gellius9.txt` | direct plain request, HTTP 200 | 122461 B | `aaa75d65a4749f11a29ae3888277454d19c3c7b0de84a1f16a49640fcf9dacc1` |

Working copies at `/fast/scratch/hyaku/kotodama-r55/ScoutPlinyRaces/`. Every quoted string below — the registry-row quotes and the phrases quoted inside draft sentences — was substring-checked against the extracted text (0 misses); one further Gellius sentence was dropped from the quote list because it straddles a printed page marker (note below).

**Access detail for Pliny.** The first two requests in this session returned HTTP 429 (rate limit). I waited 20–25 s, sent an ordinary browser user-agent string, and the third request returned HTTP 200 with the full chapter. No challenge was met, so nothing was routed around. This is recorded because a reviewer re-running the URL cold may see a 429 and should retry rather than conclude the page is gone.

**One quote shortened deliberately.** The Gellius sentence on backward feet straddles the printed page marker `p165` in the extracted text; I quote only `of marvellous swiftness, whose feet are turned backwards` so the fragment is contiguous in the file. I did not bridge the page marker with an ellipsis.

## Gap re-check at the worktree (read-only)

- `ls corpus/knowledge/myth-symbol/monsters-hybrid-beings.md` → does not exist yet; the filename still has no owner.
- `grep -ril monster corpus/knowledge --include='*.md' | wc -l` → 10; `grep -ril bestiar … | wc -l` → 7. Same counts as the claim's gap note at base.
- The omen-vocabulary axis is already owned: `corpus/knowledge/myth-symbol/divination-omen-systems.md:5,72` already carries the *monstrum / ostentum / portentum / prodigium* set from Cicero *De Div.* 1.93, with the Linnaean-style gloss that *monster* descends from *monstrum*. Rows below carry **peoples, not omen words**, so the entry should not restate that etymology as new.
- Sibling seats already own neighbouring ground: `ScoutBestiaryAberdeen.md` (medieval moralised bestiary), `ScoutGriffinFossil.md` (griffin-origin dispute), `ScoutCryptozoology.md` (demarcation, and the L&S *monstrum* entry). My row 1 is the **classical wonder-catalogue of nations**; it must not be used as a griffin-origin source (Pliny describes the gold-guardian, he does not explain where griffins came from) and must not be used for medieval allegory (Pliny gives no moral reading of any being in this chapter).

## Findings that shape the entry (design decisions)

| Decision | What the opened text carries | Confidence |
|---|---|---|
| Is the being a people or a specimen? | The chapter's own title in this edition is "The Wonderful Forms of Different Nations"; the man-eaters are "tribes of the Scythians"; the one-eyed are "a nation"; the mouthless are "the nation of the Astomi". Pliny classifies by *gens*, and the wonder is that a whole people is built that way | high (four separate passages read) |
| What does the name mean? | Names are functional glosses, not proper names: `Monocoli` is given as "one-legged" and the same people are "also called Sciapodæ" *because* they shade themselves with their feet; `Astomi` is glossed by the mouthlessness. The label is an explanation of the body or the behaviour | high |
| How is the body composed? | By moving, removing or doubling one part and leaving the rest human: one eye centred in the forehead; a human frame under a dog's head, with claws and bark instead of speech; no mouth at all; feet reversed against the legs; one leg only; eight toes; no neck. Nothing is invented wholesale | high |
| Where does it live? | On the edge, named as an edge: "the very extremity of India, on the eastern side, near the source of the river Ganges" for the Astomi; "Beyond these people, and at the very extremity of the mountains" for the Trispithami and Pygmies; the Arimaspi next to the cave of the north wind (Geskleithron); Abarimon in a valley of Mount Imaus. Distance is measured in days' journey from named rivers | high |
| Does it warn, guard, devour, teach? | The chapter assigns two functions plainly: the Scythian tribes **devour** human flesh, and the Griffins **guard** gold, fighting the Arimaspi for it, "with a singular degree of cupidity". No being in this chapter teaches a lesson and none is read as an omen of a coming event; the moralising is a later layer (see `NEW-ScoutPlinyRaces-2` and the Aberdeen row) | high |
| Who records it, in what kind of book? | Each item is tagged with a named authority — Herodotus and Aristeas of Proconnesus for the Arimaspi; Isigonus of Nicæa, Crates of Pergamus, Agatharchides, Calliphanes, Aristotle, Apollonides, Phylarchus, Damon, Cicero, Megasthenes, Ctesias, Tauron, Eudoxus, Onesicritus, Artemidorus, Durisis, Clitarchus elsewhere. The chapter is a citation chain, not an observation | high |
| What is the catalogue *for*? | Pliny closes the chapter by calling the whole set "amusements to herself, though they appear miraculous to us" and boasts that he cited "whole nations in the list of her prodigies". The purpose is the display of Nature's range | high |
| Can a wonder live inside the centre? | Yes, once, and as a privilege: the Hirpi at Mount Soracte walk over a burning pile of wood unscorched, and by senate decree are "always exempted from military service, and from all other public duties". A monster kept inside the city is a legal status, not a geography | high |
| What hedges does the reporter use? | Pliny concedes incredibility and answers it from the centre (Italy and Sicily once had the Cyclopes and Læstrygones); the Griffins are winged "as they are commonly represented", which flags the image as received iconography rather than report | medium (the hedge is explicit; what it implies about Pliny's sources is inference) |
| What changes across periods? | A century later Gellius has the same list in cheap Greek books and calls them worthless — the beings are stable, the *valuation* is not | high (both texts read) |

---

### NEW-ScoutPlinyRaces-1

citation: Pliny the Elder. *Natural History*, Book 7, chapter 2 ("The Wonderful Forms of Different Nations"), trans. John Bostock and H. T. Riley (London: Taylor and Francis, 1855). Perseus Digital Library, `Perseus:text:1999.02.0137:book=7:chapter=2`.

url: https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.02.0137:book=7:chapter=2

route: direct plain request (curl), HTTP 200, `text/html`, 697032 bytes, sha256 `69a92700…`, access date 2026-10-22. Two earlier requests in the same session returned HTTP 429 (rate limit); the chapter was read on a third request after a 20–25 s pause with an ordinary browser user-agent. No challenge, no archive, no key.

kind: book

tier: A — Perseus's scholarly digital edition of the primary text in a standard published translation; the chapter is the primary evidence for how Pliny orders, names, sources and frames the monstrous peoples, and the entry quotes only words this translation carries. The Latin of the same chapter could not be read (see `unopened`), so nothing here is a claim about Pliny's Latin wording.

scope: the chapter as a catalogue of *nations* — cannibal Scythians, the one-eyed Arimaspi and the gold-guarding Griffins, backward-footed Abarimon, dog-headed hunters, the Monocoli/Sciapodæ, the neckless, the Satyr, the mouthless Astomi, the Trispithami and Pygmies, and the fire-walking Hirpi with their senate exemption — together with the named authority Pliny attaches to each item, his concessions about credibility, and his closing framing of the set as Nature's amusements and prodigies. It does not support any claim about what these peoples meant to themselves, gives no moral reading of any being, and is not evidence for griffin origins or for medieval bestiary use.

quotes:
- Book 7, ch. 2, opening paragraph: "We have already stated, that there are certain tribes of the Scythians, and, indeed, many other nations, which feed upon human flesh."
- Book 7, ch. 2, opening paragraph: "in the very centre of the earth, in Italy and Sicily, nations formerly existed with these monstrous propensities"
- Book 7, ch. 2, Arimaspi paragraph (opening "In the vicinity also of those who dwell"): "a nation remarkable for having but one eye, and that placed in the middle of the forehead"
- Book 7, ch. 2, same Arimaspi paragraph: "carry on a perpetual warfare with the Griffins, a kind of monster, with wings"
- Book 7, ch. 2, same Arimaspi paragraph: "keep watch over with a singular degree of cupidity"
- Book 7, ch. 2, same Arimaspi paragraph: "with wings, as they are commonly represented"
- Book 7, ch. 2, same Arimaspi paragraph: "among the most illustrious of whom are Herodotus and Aristeas of Proconnesus"
- Book 7, ch. 2, paragraph beginning "India, and the region of Æthiopia more especially": "India, and the region of Æthiopia more especially, abounds in wonders"
- Book 7, ch. 2, paragraph beginning "On many of the mountains again": "there is a tribe of men who have the heads of dogs, and clothe themselves with the skins of wild beasts"
- Book 7, ch. 2, paragraph on Ctesias's Monocoli: "who are known as Monocoli, who have only one leg, but are able to leap with surprising agility"
- Book 7, ch. 2, same Monocoli paragraph: "protect themselves from the sun by the shade of their feet"
- Book 7, ch. 2, paragraph beginning "Among the mountainous districts": "These go sometimes on four feet, and sometimes walk erect; they have also the features of a human being."
- Book 7, ch. 2, paragraph beginning "At the very extremity of India": "the nation of the Astomi, a people who have no mouths"
- Book 7, ch. 2, same Astomi paragraph: "These people subsist only by breathing and by the odours which they inhale through the nostrils."
- Book 7, ch. 2, paragraph beginning "Beyond these people": "Beyond these people, and at the very extremity of the mountains, the Trispithami and the Pygmies are said to exist"
- Book 7, ch. 2, paragraph on the Hirpi: "they walk over a burning pile of wood, without being scorched even"
- Book 7, ch. 2, same Hirpi paragraph: "by virtue of a decree of the senate, they are always exempted from military service"
- Book 7, ch. 2, closing paragraph: "as so many amusements to herself, though they appear miraculous to us"
- Book 7, ch. 2, closing paragraph: "let it be sufficient for me to have cited whole nations in the list of her prodigies"

teaches: Pliny lists monstrous peoples as nations, names an authority for each, places them at the world's edges, and calls them Nature's amusements.

draft sentences:
- File the being as a people before you file it as a species: Pliny's man-eaters are "tribes of the Scythians", his one-eyed people are "a nation", and the Monocoli are named for their one leg while being "also called Sciapodæ" for the shade of their feet, so decide whether your label belongs to a people, a body, or a behaviour (NEW-ScoutPlinyRaces-1, Book 7, ch. 2, opening paragraph and the paragraph on Ctesias's Monocoli).
- Build the hybrid by moving one part and leaving the rest human — a single eye centred in the forehead, a dog's head on a hunting body that barks instead of speaking, no mouth at all — and say what the being can still do with what remains (NEW-ScoutPlinyRaces-1, Book 7, ch. 2, Arimaspi paragraph).
- Place each being on an edge you can name and travel to: the Astomi live at "the very extremity of India", beyond them "the Trispithami and the Pygmies are said to exist" at "the very extremity of the mountains", so decide the direction, the distance in days, and what the edge is an edge *of* (NEW-ScoutPlinyRaces-1, Book 7, ch. 2, paragraphs beginning "At the very extremity of India" and "Beyond these people").
- Give the guardian an object, a rival and a motive: the Griffins keep watch over gold dug from mines and fight the Arimaspi for it out of cupidity, so decide what your being guards, who else wants it, and whether the guarding is instinct, duty, or an arrangement someone made (NEW-ScoutPlinyRaces-1, Book 7, ch. 2, Arimaspi paragraph).
- Show the record as a chain of named authorities rather than an observation — Herodotus and Aristeas for the one-eyed, Ctesias for the one-legged, Megasthenes for the backward feet — so a sceptical reader can see exactly whose word each entry rests on (NEW-ScoutPlinyRaces-1, Book 7, ch. 2, Arimaspi paragraph and the India paragraph).
- Decide what a society grants a wonder it keeps rather than expels: the Hirpi walk over burning wood unscorched and are exempted from military service by senate decree, which makes the monster's place inside the centre a legal status, not a geography (NEW-ScoutPlinyRaces-1, Book 7, ch. 2, paragraph on the Hirpi).

---

### NEW-ScoutPlinyRaces-2

citation: Gellius, Aulus. *Noctes Atticae* 9.4, "On some extraordinary marvels found among barbarian peoples; and on awful and deadly spells; and also on the sudden change of women into men", in *Attic Nights*, trans. John C. Rolfe, Loeb Classical Library (1927), public domain. LacusCurtius edition by Bill Thayer, University of Chicago.

url: https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Gellius/9*.html

route: direct plain request (curl), HTTP 200, `text/html`, 122461 bytes, sha256 `aaa75d65…`, access date 2026-10-22. No challenge, no archive. (The `9%2A.html` form used for S281 in the registry resolves to the same page; I read the literal `9*.html` form.)

kind: book

tier: A — a primary text in a standard published Loeb translation, on a scholarly edition site; the bookstall scene, the list and the judgement on the books are Gellius's own words in Rolfe's rendering. As with row 1, nothing here is a claim about Gellius's Latin.

scope: the second-century reception of the wonder-catalogue as **merchandise and as bad literature**: the port bookstall at Brundisium, the cheap Greek books and their named authors (Aristeas of Proconnesus, Isigonus of Nicæa, Ctesias, Onesicritus, Philostephanus, Hegesias), the list of monstrous peoples that repeats Pliny's canon, Gellius's disgust at what he has copied, and his decision to add Pliny's eyewitness reports on Pliny's authority. It does not give any being a moral or an omen reading, and it is not evidence for the existence of any people it lists.

quotes:
- 9.4, chapter heading: "marvels found among barbarian peoples"
- 9.4.3: "all those books were in Greek, filled with marvellous tales, things unheard of, incredible"
- 9.4.3: "the writers were ancient and of no mean authority"
- 9.4.3: "Aristeas of Proconnesus, Isigonus of Nicaea, Ctesias and Onesicritus"
- 9.4.3: "extraordinary and unexpected cheapness"
- 9.4.4: "The volumes themselves, however, were filthy from long neglect"
- 9.4.6: "eat human flesh and subsist on the nourishment of that food"
- 9.4.6: "having one eye in the middle of the forehead and called Arimaspi"
- 9.4.6: "of marvellous swiftness, whose feet are turned backwards"
- 9.4.9: "run by hopping with their single leg"
- 9.4.10: "bodies that are rough and covered with feathers like birds"
- 9.4.10: "live by inhaling the perfume of flowers"
- 9.4.11: "not more than two feet and a quarter in height"
- 9.4.12: "I was seized with disgust for such worthless writings"
- 9.4.12: "which contribute nothing to the enrichment or profit of life"
- 9.4.13: "not as something that he had heard or read, but that he knew to be true and had himself seen"

teaches: Gellius buys a large lot of cheap Greek wonder-books at Brundisium, copies their list of monstrous peoples, and calls the books worthless.

draft sentences:
- Make the catalogue a physical object with a price and a condition: Gellius finds the books at a port stall, buys them for their "extraordinary and unexpected cheapness", and finds them "filthy from long neglect", so decide what your bestiary physically is — a cheap portable, a chained temple copy, a patron's illuminated codex — and who can afford to own one (NEW-ScoutPlinyRaces-2, 9.4.4).
- Let authority be the product on sale: the books are "ancient and of no mean authority" and the names of Aristeas, Isigonus, Ctesias and Onesicritus are the reason to buy them, so decide whether monster knowledge in your world travels on a named author's reputation or on a repeatable procedure (NEW-ScoutPlinyRaces-2, 9.4.3).
- Treat the list as canonical furniture and the framing as the variable: Gellius's readers meet the same man-eaters, one-eyed Arimaspi, backward feet, one-legged hoppers, feather bodies that live on scent, and two-foot Pygmies that Pliny had, so decide which beings every educated person in your world knows and which are one author's invention (NEW-ScoutPlinyRaces-2, 9.4.6 and the sections following).
- Let the compiler despise what he transmits: Gellius writes the stories down and is "seized with disgust for such worthless writings", then adds Pliny's cases anyway, so decide whether your catalogue's author believes, disbelieves, or merely copies — the third position is the one that keeps a bestiary in circulation (NEW-ScoutPlinyRaces-2, 9.4.12).
- Rank the evidence inside the text, not outside it: Gellius separates hearsay from Pliny's report, which he gives "not as something that he had heard or read, but that he knew to be true and had himself seen", so decide what your catalogue counts as proof and who is entitled to supply it (NEW-ScoutPlinyRaces-2, 9.4.13).

---

## Coupling notes for the L1

1. **Do not let the entry claim Pliny moralises.** He does not: no being in *NH* 7.2 carries a lesson, and the chapter's purpose is stated as Nature's display ("amusements to herself"). The moralised reading belongs to the bestiary traditio (Aberdeen seat) — the entry's "monster as moral" section should attribute it there, and can use Gellius's disgust as the bridge between the two valuations.
2. **The omen axis is already owned** by `myth-symbol/divination-omen-systems.md`. Pliny supplies "prodigies" as a *word for the set* ("whole nations in the list of her prodigies"), not as a claim that these peoples foretell events. A sentence pairing *monstrum* with this chapter would be an inference, not a quote.
3. **Griffins**: `ScoutGriffinFossil.md` owns the origin dispute. This row may be cited for what Pliny says the Griffin *does* (guards gold, fights the Arimaspi, is winged "as commonly represented") and for nothing about fossil origins.
4. **Blemmyes gap**: not in *NH* 7.2. If the entry needs them, they need their own row (Solinus or a later compiler), and this seat did not open one.
5. **Word counts**: every quote above is 3–22 words, under the 25-word cap; no quote joins two fragments across a sentence break or across a printed page marker.

## Unrun checks

No build, lint, test, install or gate command was run: this seat writes one report and nothing else, and claim C's acceptance (`reports/round-55/accept-c.py`) belongs to the L1 after integration. Quote verification was the substring match described above; no orthographic normalisation was applied to the quoted text (the Æ ligatures in row 1 are as served).

## unopened

- **Perseus Latin, Mayhoff edition, `Perseus:text:1999.02.0138:book=7:chapter=2`** — HTTP 200, but unusable: the HTML page serves no text body (the text is injected by script), and the `xmlchunk` endpoint returns a 1589-byte fragment containing only the chapter's first sentence, broken off at an `<unclear>` OCR placeholder; it contains no Arimaspi, Astomi or Sciapodes material, and requests for `&chunk=2,3,4` returned the identical fragment. Not used, and no Latin wording is claimed anywhere above. The one Latin phrase the fragment does carry, "prodigiosa aliqua et incredibilia multis visum iri haud dubito", is therefore recorded here as seen and **not** filed as a row or quoted into the entry.
- **Bibliotheca Augustana, Pliny *NH* 7** (`hs-augsburg.de/~harsch/Chronologia/Lsante01/Plinius/pli_na07.html`) — HTTP 503 on a single attempt; not retried, because the English chapter already carried the evidence.
- **The Latin Library, Pliny** — index page HTTP 200 but lists no *Natural History* text; `pliny.nh7.html` and `pliny.nh7.shtml` both HTTP 404. The site does not host this work.
- **LacusCurtius, Pliny the Elder** — home page HTTP 200, but no book-7 page at `/Pliny_the_Elder/7.html` or `/7*.html` (both HTTP 404); only Gellius was taken from that site.
- **Gellius in Latin** — not attempted; Rolfe's translation carries the sentences the entry needs, and the Latin adds nothing to the naming/body/map/record decisions.
- **Blemmyes in Pliny** — looked for in the chapter and absent; not pursued further this seat.

