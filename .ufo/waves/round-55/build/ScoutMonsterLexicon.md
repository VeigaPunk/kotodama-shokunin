# ScoutMonsterLexicon — Greek τέρας, Latin monstrum, Arabic ghūl

- seat: `KotodamaR55.ScoutMonsterLexicon` (scout, claim C ground: monsters and hybrid beings)
- round: kotodama 55 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `8eda9543e940bdc4938fad90182ee6a6fe271d0f`, claim base `f4015e70b829523ed81e14ce4279bfab0e0233e4`
- assignment: the entry's language coupling — the three words, quoted at their head senses with locators, aimed at design decisions (what the culture calls the being; what the word means; body composition; habitat; whether it warns, guards, punishes, teaches or devours; who records it and in what kind of book; what changes across periods)
- draft ids used below: `NEW-ScoutMonsterLexicon-1`, `-2`, `-3`; the L1 assigns the final `S` ids at integration
- no LSP server answers a web page, and this seat read no repository source file that a server would index, so nothing below is presented as semantic proof; every statement is a literal reading of an opened page or of the scan's own text layer, each with its locator. No tool was installed or upgraded and no pacman command was run.

## Route summary

| file | URL actually read | route | bytes | sha256 |
|---|---|---|---|---|
| LSJ, entry τέρας | `https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0057%3Aentry%3Dte%2Fras` | direct plain request, HTTP 200, `text/html` | 176,244 | `d102ae983f63cbfbe537dfa8b609783ce951661e8d0dee9f6413e9cc7fc095ff` |
| L&S, entry monstrum | `https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0059%3Aentry%3Dmonstrum` | direct plain request, HTTP 200, `text/html` | 133,864 | `811c9786ff87bee941a819d320bc0a213e79ed59d407175e3ab10fe736890375` |
| Lane, Book I Part 6 (Ghayn–Fā), OCR text | `https://archive.org/download/lane-e.-w.-an-arabic-english-lexicon-book-1-part-6-gain-fa-1877/Lane%2C%20E.W.%2C%20An%20Arabic%20-%20English%20Lexicon%2C%20Book%201%2C%20Part%206%2C%20Gain-%20Fa%2C%201877_djvu.txt` | direct plain request, HTTP 200, `text/plain; charset=utf-8` | 2,190,170 | `68776863b0746f04addff26da0fc764cee8c2aa1c3397c905c9a2c3d646751ad` |
| Lane, part 6, second independent OCR derivation | `https://archive.org/download/LANESARABICENGLISHLEXICONDIGITIZEDTEXTVERSION/AnArabic-englishLexiconPart6-86.00.02-_djvu.txt` | direct plain request, HTTP 200 | 2,042,401 | `a66d929210113cbd1d4a373c75fd3d7348821f8a4f23b708160cfd6e372cc047` |
| Lane, part 6, PDF text layer (folio check) | `https://archive.org/download/lane-e.-w.-an-arabic-english-lexicon-book-1-part-6-gain-fa-1877/Lane%2C%20E.W.%2C%20An%20Arabic%20-%20English%20Lexicon%2C%20Book%201%2C%20Part%206%2C%20Gain-%20Fa%2C%201877.pdf` | direct plain request, HTTP 200, `application/pdf`, converted with `pdftotext -layout` (poppler 26.08.0) | 30,238,705 | — |

Access date for every file: 2026-10-22. No challenge, captcha, paywall or login was met on any route.

Every quote below was re-checked by substring match against the fetched bytes with whitespace normalised only (LSJ 4/4, L&S 4/4, Lane 4/4 in the digitised-text OCR). Three of the four Lane spans also match the Google OCR derivation of the same page; in the fourth, the Google OCR reads `hind` where the other readings have `kind`, and the PDF text layer of the same scan also reads `kind`, so the quoted word is `kind` and the `hind` is recorded here so that a spot-check is not surprised by it. Lane's editorial preface exists only in the Google OCR text of the item; the digitised-text copy begins at the lexicon's title page, so the preface quote at the end of `NEW-ScoutMonsterLexicon-3` comes from the Google OCR. The Lane page number is read off the scan's own running head, not inferred from position: PDF page 140 of the part carries `Book I.] … 2311`, the preceding printed page is 2310 and the following is 2312.

Anchors: Perseus prints the lexicon entries with roman sense numerals (`I`, `II`, `III`) and arabic sub-senses (`2`), so every locator below is the entry's own numbering. Lane's part prints a headword per root with an English gloss sequence; the ghūl entry is one such sequence on p. 2311, and its parenthetical source letters are Lane's own abbreviations of the Arabic lexica he is digesting.

---

### NEW-ScoutMonsterLexicon-1

citation: Liddell, Henry George; Scott, Robert; revised by Jones, Henry Stuart, with McKenzie, Roderick. 1940. *A Greek-English Lexicon*, 9th ed. Oxford: Clarendon Press. Entry τέρας. Perseus Digital Library, `Perseus:text:1999.04.0057:entry=te/ras`.

url: https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0057%3Aentry%3Dte%2Fras

route: direct plain request (curl, and the corpus reader), HTTP 200, `text/html;charset=UTF-8`, 176,244 bytes, no challenge, 2026-10-22. The page's own citation line reads "Henry George Liddell. Robert Scott. A Greek-English Lexicon. revised and augmented throughout by. Sir Henry Stuart Jones. with the assistance of. Roderick McKenzie. Oxford. Clarendon Press. 1940." The registry already holds this edition at S279 for the headword πρόσωπον; this row is a different headword, not a second edition.

kind: book

tier: A — the standard lexicon of classical Greek, authoritative for the attested senses of this exact word and for the passages it cites in support. A for the sense inventory and its citations; not for any claim about what an individual Greek speaker believed, and not a primary text.

scope: the sense range of τέρας as LSJ orders it — (I) sign, wonder, marvel, portent, with examples of signs in the sky and of Strife carried in the hands as a sign of the coming battle; (II) in concrete sense, monster, exemplified by the Gorgon's head, a serpent, Typhoeus, Cerberus and the Sphinx; (II.2) monstrous birth, monstrosity, cited to Plato's *Cratylus* and Aristotle's *Generation of Animals*; (III) colloquial use as a marvel, and the plural for incredible statements. Does not support anything about Roman, Arabic or later European monster words, and says nothing about cult, law or the display of monsters.

quotes:
- sense I, head gloss: "sign, wonder, marvel, portent"
- sense II, head gloss: "in concrete sense, monster"
- sense II.2, head gloss: "monstrous birth, monstrosity"
- sense III, final clause of the sense: "of incredible statements"

teaches: Greek τέρας names a divine sign or wonder before it names a creature, and the same word then covers a concrete monster, a monstrous birth and a tall story.

draft sentences:
- Decide which sense your word for the being descends from, because this lexicon puts the sign first and marks the creature sense as a concrete use of it, so a being called by this word is a thing to be read before it is a thing to be fought (NEW-ScoutMonsterLexicon-1, sense I and sense II).
- Make the sign an event or a displayed object rather than a species: the examples under the sign sense are a star sent to sailors and Strife held in the hands as a sign of the coming battle (NEW-ScoutMonsterLexicon-1, sense I).
- Fill the creature sense with a body list rather than one shape: the entry's own examples are the Gorgon's head, a serpent, Typhoeus, Cerberus and the Sphinx, spanning an image carried in battle and living beasts (NEW-ScoutMonsterLexicon-1, sense II).
- Keep portentous births in a separate institution from monstrous species, since a distinct sense covers monstrous birth and monstrosity and cites Plato and Aristotle's zoology for it (NEW-ScoutMonsterLexicon-1, sense II.2).
- Let the plural also name a tall story, because the lexicon glosses it as the word for incredible statements, which is the register a wonder catalogue is written in (NEW-ScoutMonsterLexicon-1, sense III).

---

### NEW-ScoutMonsterLexicon-2

citation: Lewis, Charlton T.; Short, Charles. 1879. *A Latin Dictionary*. Oxford: Clarendon Press. Entry monstrum. Perseus Digital Library, `Perseus:text:1999.04.0059:entry=monstrum`.

url: https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0059%3Aentry%3Dmonstrum

route: direct plain request (curl, and the corpus reader), HTTP 200, `text/html;charset=UTF-8`, 133,864 bytes, no challenge, 2026-10-22. The page's citation line reads "A Latin Dictionary. Founded on Andrews' edition of Freund's Latin dictionary. revised, enlarged, and in great part rewritten by. Charlton T. Lewis, Ph.D. and. Charles Short, LL.D. Oxford. Clarendon Press. 1879." The registry already holds this edition at S280 for the headword persōna; this row is a different headword.

kind: book

tier: A — the standard Latin-English dictionary, authoritative for the attested senses of this word and for the ancient etymology it reports. A for usage and for the fact that the derivation was argued in antiquity; the derivation itself is an attributed Roman antiquarian claim quoted from Festus, not a modern etymology.

scope: the sense range of monstrum — (I) the religious sense, a divine omen indicating misfortune, with the synonym set monstrum, ostentum, prodigium, portentum and the Festus derivation from monere; (II) the transferred sense, a monster or monstrosity, whether a living being (II.A, including the abusive use of a person) or an inanimate thing (II.B, the sea, the Trojan horse, the ship Argo), and the phrase for telling such things. Does not support any claim about Etruscan or Roman ritual procedure, about the legal treatment of prodigies, or about later bestiaries.

quotes:
- sense I, head gloss: "Orig. belonging to relig. lang., a divine omen indicating misfortune, an evil omen, portent"
- sense I, the Festus gloss quoted inside the entry: "monstrum dictum velut monestrum, quod moneat aliquid futurum"
- sense II, head gloss: "a monster, monstrosity (whether a living being or an inanimate thing)"
- sense II.B, gloss on the phrase monstra narrare, dicere: "to relate wonders, prodigies, marvels"

teaches: Latin monstrum begins as a divine omen of misfortune, is derived from monere, and extends to a monster, to monstrosity and to the telling of marvels.

draft sentences:
- Take the word's own etymology as a design statement, because the entry derives monstrum from monere and quotes Festus's gloss that it is so called because it warns of something future, which makes the being's function to give notice (NEW-ScoutMonsterLexicon-2, sense I).
- Keep the omen sense primary and the creature sense transferred, so a world's monster word can be an omen noun that its speakers also use for animals, and the entry's own order tells you which use is the older claim (NEW-ScoutMonsterLexicon-2, sense I and sense II).
- Allow inanimate monsters, since the transferred sense is explicitly extended to things and its examples are the sea, the Trojan horse and the ship Argo, which lets a monster be an object or a vessel rather than a species (NEW-ScoutMonsterLexicon-2, sense II.B).
- Separate the encounter from the telling, because the entry has a phrase for narrating such things glossed to relate wonders, prodigies, marvels, so the wonder catalogue is a recognised speech genre in its own right (NEW-ScoutMonsterLexicon-2, sense II.B).
- Use the word for persons as well as beasts, since it is applied to a monster of a man, a monster of a woman and a political enemy, which is the insult a world's monster term will also carry (NEW-ScoutMonsterLexicon-2, sense II.A).

---

### NEW-ScoutMonsterLexicon-3

citation: Lane, Edward William. *An Arabic-English Lexicon*, Book I, Part 6 (Ghayn–Fā). Edited, with a memoir, by Stanley Lane Poole. London: Williams and Norgate; Edinburgh: 20 South Frederick Street, 1877. Entry غول (ghayn–wāw–lām), p. 2311. Internet Archive item `lane-e.-w.-an-arabic-english-lexicon-book-1-part-6-gain-fa-1877` (Google scan of the printed part).

url: https://archive.org/download/lane-e.-w.-an-arabic-english-lexicon-book-1-part-6-gain-fa-1877/Lane%2C%20E.W.%2C%20An%20Arabic%20-%20English%20Lexicon%2C%20Book%201%2C%20Part%206%2C%20Gain-%20Fa%2C%201877_djvu.txt

route: direct plain request (curl), HTTP 200, `text/plain; charset=utf-8`, 2,190,170 bytes, no challenge, 2026-10-22. The printed part's own title page is in the same scan: "BOOK I.—PART 6.", "WILLIAMS AND NORGATE, 14, HENRIETTA STREET, COVENT GARDEN, LONDON ; AND 20, SOUTH FREDERICK STREET, EDINBURGH.", "1877.". Page 2311 is fixed from the PDF text layer of the same item: PDF page 139 carries the running head `2310`, page 140 carries `Book I.] … 2311`, page 141 carries `2312`. The four quoted spans were also found verbatim in a second, independently produced OCR of the same part (`AnArabic-englishLexiconPart6-86.00.02-_djvu.txt`). Lane's Arabic headwords are not recoverable from either OCR, so the headword is given in its standard spelling (غول) and no Arabic letterform is quoted here.

kind: book

tier: A — the standard classical Arabic-English lexicon, authoritative for the senses Lane records and for the Arabic authorities he digests (his parenthetical letters S, O, Msb, K, TA, JM). A for what the entry records as the lexicographic sense; not for present-day belief or practice in any Arabic-speaking community, and not for the exact Arabic wording, which this OCR does not preserve.

scope: the ghūl entry on p. 2311 as Lane arranges it — the desert being that appears to men and leads them astray, the report that the Prophet denied this account and the readings of that denial, the male and female forms, the man-eating demon, the tusked beast known to the Arabs and killed by Taabbata Sharra, the shape-changing enchanter and the instruction to utter the call to prayer, and the extended senses (destruction, death, calamity, serpent). Does not support any claim about jinn doctrine in Islam as a whole, about any named community's practice, or about the Arabic text beyond what the English gloss states.

quotes:
- p. 2311, first gloss of the entry: "A kind of [goblin,] demon, devil, or jinnee, which, the Arabs assert, appears to men in the desert"
- p. 2311, continuing the same sentence: "assuming various forms, causing them to wander from the way, and destroying them"
- p. 2311, the tradition that follows the gloss: "but this the Prophet denied"
- p. 2311, later in the entry, the En-Nadr report: "a demon, or devil, that eats men"

teaches: Lane's ghūl is a desert jinnee that changes shape and waylays travellers, which the Prophet's tradition denies, and also a man-eating demon.

draft sentences:
- Put the being at the edge of the travelled world and make that edge its habitat, because the first gloss has it appear to men in the desert, so the encounter belongs to the road between settlements rather than to a distant elsewhere (NEW-ScoutMonsterLexicon-3, p. 2311).
- Make disorientation the monster's action before violence: it assumes various forms, causes travellers to wander from the way and destroys them, which gives a world a monster whose weapon is the wrong path (NEW-ScoutMonsterLexicon-3, p. 2311).
- Decide whether the tradition restricts the being, since the entry records that the Prophet denied this account, and that some read the denial as rejecting the shape-changing and the power to lead astray rather than the existence of such beings (NEW-ScoutMonsterLexicon-3, p. 2311).
- Give the culture a verbal counter rather than a weapon: on such a shape-change, the entry says, one should hastily utter the call to prayer, so the rite that answers the being is speech (NEW-ScoutMonsterLexicon-3, p. 2311).
- Split the being by sex and by body, because the entry gives a male jinnee with a separately named female, an enchantress of the jinn, a demon that eats men, and a tusked beast known to the Arabs and killed by Taabbata Sharra (NEW-ScoutMonsterLexicon-3, p. 2311).
- Note who finished the record: this part's preface states that Lane died on the tenth of August 1876 and that Stanley Lane Poole completed the work, so a bestiary's alphabet can be a posthumous and edited object (NEW-ScoutMonsterLexicon-3, Editor's preface, part 6).

---

## Findings for the entry's design decisions

Observed on the opened pages unless a line is marked inference.

| design decision | what the opened pages carry | locator |
|---|---|---|
| what the culture calls the being, and what the word means | Greek: a sign or wonder first, then the concrete creature, then a monstrous birth — one word, three institutions | LSJ τέρας, senses I, II, II.2 |
| | Latin: an evil omen first, with three near-synonyms that all name showing or foretelling, then the transferred monster | L&S monstrum, senses I and II |
| | Arabic: one entry that is a place-being (desert), a shape-changer, a killer, a class of jinn, and an abstract noun for destruction and death | Lane, p. 2311 |
| how its body is composed | the words do not compose the body; the lexica hand the job to example: a severed head worn as a device, a serpent, Typhoeus, Cerberus, the Sphinx | LSJ τέρας, sense II |
| | the Arabic entry is a list of bodies rather than one: jinnee, enchantress, man-eater, tusked beast | Lane, p. 2311 |
| where it lives relative to the known world | Greek signs come from the sky, or are carried in the hand | LSJ τέρας, sense I, with *Il.* 4.76 and 11.4 |
| | the ghūl's habitat is the desert between the traveller's points, and the danger is the route, not the destination | Lane, p. 2311 |
| whether it warns, guards, punishes, teaches or devours | warn: both classical words are defined by foretelling, and the Latin derivation is from monere | L&S monstrum, sense I; LSJ τέρας, sense I |
| | devour: the ghūl eats men, destroys travellers, and its name also means destruction and death | Lane, p. 2311 |
| | a tradition can limit a being's power without denying the being: the Prophet's denial is read as rejecting shape-changing and leading astray | Lane, p. 2311 |
| who records or depicts it, and in what kind of book or object | a lexicon ordered by headword, which is the only kind of book in which these three words sit side by side | all three rows; LSJ and L&S headword entries, Lane part 6 |
| | the Arabic record is a posthumous part, edited by Lane's nephew after Lane's death in 1876 | Lane, Editor's preface |
| | the Latin entry distinguishes telling from seeing by giving a phrase for the telling: monstra narrare, dicere | L&S monstrum, sense II.B |
| what changes across periods | within Greek, the same word moves from sign to creature to birth-defect to colloquial marvel, and the dictionary's order records that spread | LSJ τέρας, senses I–III |
| | within Latin, the religious sense is labelled original and the creature sense transferred, and the transferred sense reaches inanimate things | L&S monstrum, sense I versus II |
| | the Arabic entry aggregates authorities who disagree (a beast seen and killed, a jinn, an abstraction), which is what a living tradition looks like in a dictionary | Lane, p. 2311, parenthetical source letters |
| one caution for the entry | none of the three words is the English word "monster", and none of the three lexica says the being is unreal; a sentence that equates them is the entry's own argument, not a quoted one | all three rows, scope cells |

## Spare verbatim lines from the same opened pages (verified, not registered as quotes)

Each is one contiguous span, and the L1 may swap any of them in for a quote above or cite one for an extra sentence.

- LSJ τέρας, sense I, on signs in heaven: "esp. of signs in heaven"
- LSJ τέρας, sense I, the battle sign: "a sign of coming battle"
- LSJ τέρας, sense II, one example: "of the Gorgon's head"
- LSJ τέρας, sense II, one example: "of Cerberus"
- LSJ τέρας, sense III, the colloquial formula: "a marvel"
- L&S monstrum, sense I, the derivation clause: "quod moneat aliquid futurum"
- L&S monstrum, sense II.A, of beasts: "monsters of men"
- L&S monstrum, sense II.B, of things: "of the Trojan horse"
- Lane, p. 2311: "an enchantress of the jinn"
- Lane, p. 2311: "terrible [in appearance], having tusks, or fangs"
- Lane, p. 2311: "one should hastily utter the call to prayer"
- Lane, p. 2311: "anything that takes a man unexpectedly and destroys him"
- Lane, Editor's preface (Google OCR text of the same item): "Mr. Lane died, on the tenth of August, 1876."

## Notes the L1 needs when filing the rows

- **Registry cells.** Recommended for all three rows: `status` mined, `opened` 2026-10-22, `recheck` 365d (the editions and the printed part are fixed; the recheck guards the URL and the OCR, not the text), and the `used-by` cell naming `corpus/knowledge/myth-symbol/monsters-hybrid-beings.md`, which is what the USEDBY leg of `accept-c.py` reads. `kind` is `book` on all three. Suggested `anchor` cell text is the four bullets in each row's `quotes:` block, semicolon-separated, each prefixed by its sense or page as written above.
- **Cell fields to copy verbatim.** LSJ source cell: "Liddell, Henry George; Scott, Robert; revised by Jones, Henry Stuart, with McKenzie, Roderick. 1940. *A Greek-English Lexicon*, 9th ed. Oxford: Clarendon Press. Entry τέρας. Perseus Digital Library, `Perseus:text:1999.04.0057:entry=te/ras`. — https://… (direct plain request, HTTP 200 (Perseus Hopper), 2026-10-22)". L&S source cell: same pattern with `Perseus:text:1999.04.0059:entry=monstrum`.
- **Numbering.** LSJ prints sense numerals `I`, `II`, `II.2`, `III`; L&S prints `I`, `II`, `II.A`, `II.B`. Lane's part has no section numbers, so its locator is the printed page `2311` and the headword, which is how the part is cited in Arabic lexicography. Do not turn the Lane locator into a range: the whole entry is on that one page.
- **Separability.** These three rows are the claim's own lands. They lean on nothing another claim lands. S279 and S280 are the same two editions for different headwords (πρόσωπον, persōna) and are not duplicated, and the registry holds no Lane row at all (grep for `Lane` over `corpus/SOURCES.md` returns 0 lines).
- **Overlap with sibling seats, and why this is not duplication.** `ScoutCiceroDivination` carries *De Divinatione* 1.93 and Livy 21.62, which supply the argument that the four Latin nouns are forensic and the state procedure that answers a prodigy; `ScoutIsidorePortents` carries Isidore's XI.3, which supplies the later Christian redefinition and the peoples catalogue. My rows supply what the dictionaries say the words mean, including the sense those texts do not use (monster, monstrosity) and the wonder-telling phrase in L&S sense II.B. The entry can therefore set word, argument and procedure as three separate layers without stretching any row.
- **What the rows do not carry.** No row here says a monster was displayed, punished, legally classified, or worshipped; none says anything about a named community's practice; and none supports the claim that ghūl or τέρας is "the" word for monster in its language. The Lane row is about what a nineteenth-century dictionary records from medieval Arabic lexica, and the entry must say so rather than present it as ethnography. I also did not read the Arabic side of Lane's columns: the OCR drops the Arabic script, so no Arabic phrase is quoted, and the entry should not quote one from this row.
- **Second-use warning.** LSJ sense II.2 (monstrous birth) is the natural support for a teratology paragraph, but Aristotle's *Generation of Animals* itself was not opened here; cite the sense, not the treatise.

## Not run

No lane command was run: this is a read-only scouting seat and the entry that consumes these rows does not exist yet, so `python3 -B reports/round-55/accept-c.py` would only re-measure the base (count 230, cited 0). No file in the lane was created or modified except this report. No git or jj command was run anywhere. Nothing was installed; the only conversions used were `pdftotext`, which was already present.

unopened: `https://ejtaal.net/aa/` — HTTP 200 on the site root, but the root is a script-driven dictionary interface and I did not establish a plain-request URL for Lane's ghūl entry; I used no browser or automation, so the route is left unopened rather than passed. `https://api.archivelab.org/books/lane-e.-w.-an-arabic-english-lexicon-book-1-part-6-gain-fa-1877/searchinside?q=appears%20to%20men%20in%20the%20desert` — connection failed (curl error 28, no route to the host after 135 s); the printed folio was fixed from the PDF text layer instead. Internet Archive item `AnArabic-englishLexiconInEightPartsPart6Ghayn-fa_466` — the metadata lists no OCR text file for that copy, so it could not be read by plain request. The Perseus XML chunks for both dictionary entries were not needed and were not fetched. No Arabic primary text (Qurʾān, ḥadīth collection, or a jinn treatise) was opened, so nothing here states what the tradition's own books say about ghūl beyond the one sentence Lane reports.
