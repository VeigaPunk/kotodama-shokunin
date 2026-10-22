# ScoutIsidorePortents — Isidore's *De portentis* and Pliny's monstrous peoples

- seat: `KotodamaR55.ScoutIsidorePortents` (scout, claim C ground: monsters and hybrid beings)
- round: kotodama 55 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `8eda9543e940bdc4938fad90182ee6a6fe271d0f`, claim base `f4015e70b829523ed81e14ce4279bfab0e0233e4`
- assignment: one or two opened sources for claim C's monster and hybrid-being entry; quote Isidore's distinction among *portentum*, *ostentum*, *monstrum* and *prodigium* and his claim that portents are not against nature
- draft ids used below: `NEW-ScoutIsidorePortents-1` and `-2`; the L1 assigns the final `S` ids at integration
- no LSP server answers a web page, and this seat read no repository file that a server would index, so every statement below is a literal reading of the opened page, each marked with its locator. No semantic-proof claim is made. No tool was installed or upgraded and no pacman command was run.

## Route summary (two sources, both direct, no challenge)

| file | URL actually read | status | bytes | sha256 |
|---|---|---|---|---|
| Isidore, *Etymologiae* XI (whole book) | `https://penelope.uchicago.edu/Thayer/L/Roman/Texts/Isidore/11%2A.html` | direct plain `curl`, HTTP 200 | 75,022 | `85b0e0812c4b787afcf27ae8dff131aff980e0f0c29315ebbb0f0273d9b0dc24` |
| Pliny, *Naturalis Historia* VII (whole book) | `https://penelope.uchicago.edu/Thayer/L/Roman/Texts/Pliny_the_Elder/7%2A.html` | direct plain `curl`, HTTP 200 | 142,611 | `4bf5016d4c5bbd848c6b9555d2199e7de3c0139461cb78bd4a9b58323abadbcb` |
| cross-witness for the Isidore wording | `https://www.thelatinlibrary.com/isidore/11.shtml` | direct plain `curl`, HTTP 200 | 53,817 | — |
| cross-witness for two Pliny sentences | `https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.02.0138%3Abook%3D7%3Achapter%3D2` | direct plain `curl`, HTTP 200 | 473,226 | — |

Access date for every file: 2026-10-22. All five quotes below were re-checked by substring match against the fetched
bytes (0 misses, whitespace normalised only). The Isidore quotes were found identically in the Latin Library copy of
the same Lindsay text, and the two Pliny sentences I cross-checked were found identically in Perseus's copy of the same
Mayhoff text — independent transcriptions agreeing, which is the strongest check available to me without print.

Anchors: the Isidore page numbers its sections as `#3`, `#3.2` … `#3.39` (chapter 3 is `#3`); the Pliny page numbers
book-wide sections as `#1` … `#215`. Both pages place the chapter numeral in a margin column and the section numeral
beside the text, so the chapter/section split below is read off the page, not inferred.

---

### NEW-ScoutIsidorePortents-1

citation: Isidore of Seville, *Etymologiae sive Origines* XI.3 "De portentis", in W. M. Lindsay (ed.), *Isidori Hispalensis Episcopi Etymologiarum sive Originum Libri XX*, Oxford: Clarendon Press, 1911, Book XI as transcribed at LacusCurtius (ed. Bill Thayer); public-domain text.

url: https://penelope.uchicago.edu/Thayer/L/Roman/Texts/Isidore/11%2A.html#3

route: direct plain request (curl), HTTP 200, 75,022 bytes, no challenge, 2026-10-22. The page states in its own Latin head that it carries Lindsay's Clarendon text, "cujus textus in dominio publico est", and that the transcriber has reviewed it ("Quem diligentissime perscrutavi et recensui"). The page's HTML comment block records `PROOFREAD: ok`.

kind: book

tier: A — a primary text in the standard critical edition, for the exact scope of Isidore's own wording in XI.3. The transcription is a private scholar's, not the Clarendon plates; the four quoted sentences below were found identically in a second independent transcription of the same edition (Latin Library), so the wording as quoted is not one site's error.

scope: what Isidore says in XI.3 — the four words for a portent and their common sense of foretelling; the refusal of Varro's against-nature definition and its replacement by against-known-nature; the classification of monstrous bodies by size, parts, transformation and mixture of kind; monstrous *peoples* as monsters of the human race, each with a named region; and his reduction of Geryon, the Gorgons, the Sirens, Scylla, Cerberus, the Hydra, the Chimaera, the Centaurs, the Minotaur and the onocentaur to misread real things. Does not support any claim about what later bestiaries, maps or legal texts did with this chapter, and does not cover XI.4 (transformations) beyond noting that it follows.

quotes:
- XI.3 §1, opening sentence: "Portenta esse Varro ait quae contra naturam nata videntur: sed non sunt contra naturam"
- XI.3 §2, first sentence: "Portentum ergo fit non contra naturam, sed contra quam est nota natura."
- XI.3 §2, second sentence: "Portenta autem et ostenta, monstra atque prodigia ideo nuncupantur, quod portendere atque ostendere, monstrare ac praedicare aliqua futura videntur."
- XI.3 §28, after the peoples: "alia hominum fabulosa portenta, quae non sunt, sed ficta in causis rerum interpretantur"

teaches: Isidore derives all four words for a portent from foretelling, replaces the against-nature definition with against-known-nature, classifies monstrous bodies, and reads heroes' monsters as misread real things.

draft sentences:
- Decide what the name of the being asserts before you name it: in this vocabulary *portentum*, *ostentum*, *prodigium* and *monstrum* all say the being gives notice of something to come, so the noun is a claim about function, not a description of shape (NEW-ScoutIsidorePortents-1, XI.3 §2).
- Put the boundary of the monstrous in the culture's knowledge rather than in nature: Isidore denies that such births are against nature and says they are against the nature that is *known*, so a worldbuilder must fix what the inhabitants already know before deciding what counts as a portent (NEW-ScoutIsidorePortents-1, XI.3 §1 and §2).
- Compose the body by choosing a category of departure — the whole body too large or too small, excess or defect of parts, parts cut away, parts transformed, or a mixture of kind, which is the class that holds hermaphrodites — instead of inventing a shapeless grotesque (NEW-ScoutIsidorePortents-1, XI.3 §7–§11).
- Treat anatomy as a sentence when you want the being to warn: the monster born to Alexander had a dead human upper half and living beast lower half, and was read as the king's imminent murder because the worse parts outlived the better (NEW-ScoutIsidorePortents-1, XI.3 §5).
- Scale the category from persons to peoples and place each on the map: as there are monsters among each people, Isidore says, so there are monsters among the whole human race, and he assigns the dog-headed and one-eyed to India, the headless to Libya, the long-eared to Scythia, the shadow-footed to Ethiopia, and the faceless to the far east where the world is written out (NEW-ScoutIsidorePortents-1, XI.3 §12, §15–§18).
- Keep the reduction available as a second register for the same being: Isidore says some of these portents do not exist but are fictions that interpret causes, and reads Geryon as three brothers of one mind, the Gorgons as three sisters sharing one eye, and the Sirens as prostitutes who ruined sailors, so one entry can be omen, map-people and moral at once (NEW-ScoutIsidorePortents-1, XI.3 §28–§31).

---

### NEW-ScoutIsidorePortents-2

citation: Pliny the Elder, *Naturalis Historia* VII (the monstrous peoples, ch. 2 = §§9–32), in Karl Friedrich Theodor Mayhoff (ed.), *Naturalis Historia*, Leipzig: Teubner, 1906, Book VII as transcribed at LacusCurtius (ed. Bill Thayer); public-domain text.

url: https://penelope.uchicago.edu/Thayer/L/Roman/Texts/Pliny_the_Elder/7%2A.html#32

route: direct plain request (curl), HTTP 200, 142,611 bytes, no challenge, 2026-10-22. Two of the four quoted sentences were also matched verbatim in Perseus's copy of the same Mayhoff edition (`Perseus:text:1999.02.0138`, book 7 ch. 2, HTTP 200). The page's HTML comment block records its proofreading as not finished (`PROOFREAD: THRU`), and the site's own home page describes a two-pass scheme in which unfinished books are shown in red; so the wording is this transcription's and a crux should be checked against print.

kind: book

tier: A — a primary text, in the Teubner edition of Mayhoff, for Pliny's own framing and inventory in book VII. The transcription carries one caveat recorded in `scope` and in the route line: it is not marked finally proofread, so it is A for the content and the argument, B for the exact letter of a disputed phrase.

scope: Pliny's framing of the monstrous-peoples catalogue — his admission that he is writing about prodigious and incredible things, his refusal to pledge his own credit and his relegation of it to named authorities, the inventory itself (dog-headed animals herded for milk, headless men with eyes in the shoulders, one-legged shadow-footed men, satyrs in a named region of the Indian mountains), his verdict that such things are nature's sport and our miracles, and his stated purpose of showing nature's power. Not the claims of the authorities he names, and not the later moralised bestiary.

quotes:
- VII, ch. 1, §6, on the peoples far from the sea: "in quibus prodigiosa aliqua et incredibilia multis visum iri haud dubito"
- VII, ch. 1, §8, closing the proem: "nec tamen ego in plerisque eorum obstringam fidem meam potiusque ad auctores relegabo"
- VII, ch. 2, §24, on satyrs: "sunt et satyri subsolanis Indorum montibus (Catarcludorum dicitur regio), pernicissimum animal"
- VII, ch. 2, §32, the verdict: "Haec atque talia ex hominum genere ludibria sibi, nobis miracula ingeniosa fecit natura."

teaches: Pliny inventories monstrous peoples as prodigies that show nature's power, calling them nature's sport and our miracles and handing their credit to named authorities.

draft sentences:
- Choose the stance a catalogue takes toward its own contents: Pliny calls the same beings nature's sport for herself and miracles for us, so the tone of a bestiary is a decision about whose judgement the being serves (NEW-ScoutIsidorePortents-2, VII, ch. 2, §32).
- Separate the recorder from the witness: Pliny declines to pledge his own credit for most of it and hands the report to named authorities, which is how a world's wonder book can cite travellers and still be honest about not having seen (NEW-ScoutIsidorePortents-2, VII, ch. 1, §8).
- Make the list evidence about the world rather than about the beings: Pliny says it is enough to have set these peoples among the prodigies to reveal nature's power, so the catalogue's purpose can be cosmological and the creature only the occasion (NEW-ScoutIsidorePortents-2, VII, ch. 2, §32).
- Let distance license the report and say so: he writes of prodigious and incredible things that many will think they have seen, and puts the peoples far inland — in a named district of the Indian mountains, and as shapes that appear briefly in the African deserts — so remoteness is the warrant the reader is asked to accept (NEW-ScoutIsidorePortents-2, VII, ch. 1, §6; ch. 2, §24, §32).
- Put peoples and single bodies on one list: the same chapter ranges from a nation that herds animals called dog-headed and lives on their milk, to men with no neck and eyes in the shoulders, to one-legged men who shade themselves with a foot, to satyrs in a named Indian region (NEW-ScoutIsidorePortents-2, VII, ch. 2, §23–§24, §31).
- Mark the genre, because the book decides what the being is for: this is a natural history that files the peoples under prodigies and argues from them to nature's power, not a moralised bestiary that reads each body as doctrine (NEW-ScoutIsidorePortents-2, VII, ch. 2, §32).

---

## Findings for the entry's design decisions

Observed on the opened pages unless a line is marked inference.

| design decision | what the opened pages carry | locator |
|---|---|---|
| what the culture calls the being, and what the word means | a four-term Latin cluster (*portentum*, *ostentum*, *prodigium*, *monstrum*) whose members are each derived from a verb of showing or foretelling, plus separate Greek loan-names for body types (*androgyni*, *hermaphroditae*, *heteromorphia*, *steresios*) | Isidore XI.3 §2–§3, §9, §11 |
| | the same name can attach to a herded animal or to a people: Pliny's Menismini live on the milk of "animals we call dog-headed", while Isidore's dog-headed are a people born in India | Pliny VII.2 §31; Isidore XI.3 §15 |
| how its body is composed | Isidore's five departure classes: the whole (Tityon, pygmies), excess of parts (two-headed, extra-toothed), defect or cutting away, transformation of part or whole (lion-faced, Minotaur), and mixture of kind (hermaphrodites); a separate class for joined or immature births | Isidore XI.3 §7–§11 |
| | a composite body can be a message: dead human upper half, living beast lower half, read as the king's murder | Isidore XI.3 §5 |
| where it lives relative to the known world | named regions inside known lands: India (dog-headed, one-eyed, twelve-foot men, pygmies in the mountains near the ocean), Libya (headless, back-to-front feet), Scythia (long-eared, horse-footed), Ethiopia (prone walkers, one-legged shadow-footed) | Isidore XI.3 §15–§26 |
| | the map's edge as a class of its own: the faceless, the lip-covered, the mouth-holed straw-eaters and the tongueless are said to be "written" at the far end of the east | Isidore XI.3 §18 |
| | Pliny's version: peoples far inland and away from the sea, in a named district of the Indian mountains and beyond the desert peoples, with the reader's disbelief addressed in advance | Pliny VII.1 §6; VII.2 §24, §31 |
| whether it warns, guards, punishes, teaches or devours | warn: the whole vocabulary is forensic; a portent announces a coming disaster to a people or a person, and such monsters are said to die as soon as born | Isidore XI.3 §1–§5 |
| | devour and punish as moral: Cerberus is read as the three ages by which death devours a person; the Hydra as a flooding water source; the Sirens as prostitutes who ruin sailors; the Chimaera as a burning mountain in Cilicia | Isidore XI.3 §33–§36 |
| | worship as a problem: the satyr answers Antony and says that the pagans, deluded by various error, worship beings of his kind as Fauns and Satyrs (Isidore's Latin; the English here is my rendering, not a quoted translation) | Isidore XI.3 §21 |
| who records or depicts it, and in what kind of book or object | an encyclopedic book of origins organised by name and etymology, where the chapter sits inside the book on man and portents, after the body (XI.1) and the ages of man (XI.2), and which says the far-eastern faces are *written* rather than seen | Isidore XI head, XI.1–XI.3 headings, XI.3 §18 |
| | a natural history organised by section, which names its authorities instead of vouching and admits the incredibility of what it lists | Pliny VII.1 §6, §8 |
| what changes across periods | the definition itself moves: Varro's "against nature" is quoted and refused, and the criterion becomes "against known nature"; the same chapter then reduces the mythic hybrids to misread history, geography and love | Isidore XI.3 §1–§2, §28–§39 |
| | genre changes the verdict on the same beings: prodigies that demonstrate nature's power in Pliny, omens and then moral fictions in Isidore | Pliny VII.2 §32; Isidore XI.3 §5, §28–§36 |

### Spare verbatim lines from the same opened pages (not registered as quotes)

The row shape allows four quotes; these are the lines I verified by substring match that the L1 may prefer, or may
use as the locator for a further sentence. Each is one contiguous span from the page named above.

- Isidore XI.3 §3: "Monstra vero a monitu dicta, quod aliquid significando demonstrent"
- Isidore XI.3 §5: "significasse repentinam regis interfectionem: supervixerant enim deteriora melioribus"
- Isidore XI.3 §12: "ita in universo genere humano quaedam monstra sunt gentium, ut Gigantes, Cynocephali, Cyclopes"
- Isidore XI.3 §18: "In ultimo autem Orientis monstruosae gentium facies scribuntur."
- Isidore XI.3 §21: "quos vario delusa errore gentilitas Faunos Satyrosque colit"
- Isidore XI.3 §33: "significantes per eum tres aetates per quas mors hominem devorat"
- Isidore XI.3 §36: "Quam quidam Physiologi non animal, sed Ciliciae montem esse aiunt"
- Isidore XI.3 §37: "quos quidam fuisse equites Thessalorum dicunt"
- Pliny VII.2 §31: "animalium, quae cynocephalos vocamus, lacte vivit, quorum armenta pascit"
- Pliny VII.2 §32: "ad detegendam eius potentiam satis sit inter prodigia posuisse gentes"

## Notes the L1 needs when filing the rows

- **Numbering.** Isidore's chapter is XI.3 in Lindsay, headed "De portentis"; the page's anchors run `#3` for the chapter's first section and `#3.2` … `#3.39` for the rest, and the section count stops at 39 before XI.4 "De transformatis". Pliny's section numbers run continuously through book VII, so the marginal chapter numerals are `i` at §1, `ii` at §9 and `iii` at §33: the monstrous peoples are chapter 2 = §§9–32, and the verdict is §32, which in the standard book-and-section form is *HN* 7.32. Both statements are read off the page's own margin columns.
- **Registry cells.** Recommended: `status` mined, `opened` 2026-10-22, `recheck` 365d (the editions are fixed; the recheck guards the transcription and the URL, not the text), and the `used-by` cell naming `corpus/knowledge/myth-symbol/monsters-hybrid-beings.md` on both rows, which is what the USEDBY leg of `accept-c.py` reads.
- **Separability.** No existing row covers Isidore at all, and the two Pliny rows already in the registry are book 35 (S242, portraits) and a dictionary entry (S255): this row is book VII, a different book and a different claim, so it does not lean on or duplicate an existing row.
- **Not overlapping the sibling seats.** `ScoutBestiaryAberdeen` has the bestiary as a book form (MS 24, its genre page); these two rows carry the upstream classical positions — the etymology of the words and the wonder catalogue of peoples — so the entry can set the two book kinds side by side without either pair of rows being stretched to the other's scope.
- **What I did not find.** Neither chapter I read (Isidore XI.3 in full; Pliny VII.1–2) states that monstrous births were displayed, punished or legally treated, and neither says how a reader was meant to act on a portent beyond being warned. Pliny's later chapters in the same book were not read, so nothing here denies that they say otherwise. Any sentence on display, punishment or law belongs to another source, not to these two rows.

## Not run

No lane command was run: this is a read-only scouting seat and the entry that consumes these rows does not exist yet, so `python3 -B reports/round-55/accept-c.py` would only re-measure the base (count 230, cited 0). No file in the lane was created or modified except this report. No git or jj command was run anywhere. Nothing was installed.

unopened: the Morgan Library & Museum record for its English bestiary (MS M.81) at `https://www.themorgan.org/manuscript/113794` and `https://www.themorgan.org/collection/medieval-and-renaissance-manuscripts/113794` — both returned HTTP 403 with a bot-protection page (33,543 / 33,697 bytes); the challenge was met and not passed, I did not attempt a browser or any other route around it, and I did not fall back to an archive capture because the Aberdeen row already carries the bestiary-as-object ground; the standard English translation of Isidore, Barney, Lewis, Beach and Berghof (Cambridge, 2006) — no open copy, and no publisher page was opened, so this report makes no claim about its rendering; the Migne *Patrologia Latina* vol. 82 reprint of the *Etymologiae*, which would give a second printed witness for XI.3 — not opened, because the two transcriptions I did read agreed on every quoted sentence and the assignment's source budget was spent; Isidore XI.4 "De transformatis" (Circe, the Arcadian werewolves, the *Strigae*) — read on the same page but deliberately left outside both rows, since transformation is a separate category from the portent and would need its own row.
