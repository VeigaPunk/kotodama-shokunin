# Conlang scholarship — what constructed-language research says about design

- source: S876 — https://ojs.unito.it/index.php/ricognizioni/article/view/7099 — the abstract paragraph under the "Abstract" heading (page-source line 267 of the served page) plus the `citation_keywords` metadata — fetched 2026-10-25 live (HTTP 200, 30,289 bytes, no wall)
- source: S877 — http://www.philol.msu.ru/~sidorova/files/conlangs.pdf — the whole 184-page book in one PDF (1,055,723 bytes): title page, аннотация, Оглавление, preface pp. 4–7, ch. 1 pp. 8–34 — fetched 2026-10-25 live (HTTP 200), text read with `pdftotext -enc UTF-8` (plain mode)
- verified-at: 2026-10-25
- recheck: 180d — re-open both URLs and re-locate each quoted span at the page or section its sentence names; for S877, re-extract with `pdftotext -enc UTF-8` (plain mode de-hyphenates; `-layout` keeps end-of-line hyphens and splits words) and re-find each quote on the printed page its cite names
- ground: the lane's conlang knowledge stood on craft manuals and typological datasets only — `conlang-methodology.md` cites Rosenfelder, Peterson, Okrent, Higley, WALS, PHOIBLE and APiCS — and the 799-row registry carried no row naming a constructed-language research venue at base 8841ad3 (`git show 8841ad3b896a0227674fa0725b818c999118046f:corpus/SOURCES.md | grep -c 'ojs.unito.it\|philol.msu.ru'` = 0, run 2026-10-25; the rows this round adds are the first)
- gap filled: one peer-reviewed article and one Russian-language monograph on constructed languages as an object of study; the entry's subject is the literature's own framing, which no craft manual supplies
- topic: constructed-language scholarship as a literature in two languages — an English-language argument that language construction teaches linguistic analysis, and a Russian-language monograph's taxonomy of artificial languages, its separation of вымышленные языки from auxiliary languages, its volume rule, and its account of which conlangs left their fictions
- sources: the two rows above, both tier B as the register scopes them, both opened and quoted this round. S877's row is scoped to the book's framing and chapter structure; the opened artefact is the whole book, so the body cites printed pages
- couples: `linguistics/conlang-methodology.md` (the craft pipeline this entry frames), `linguistics/naming-systems.md` (the names file this entry's §4 naming-language row bears on), `linguistics/conlang-scholarship.amend-2026-10-23.md` (the dated amendment: three further sources), `linguistics/phonetics-phonology.md`, `linguistics/historical-linguistics.md` (§6's authored history), `linguistics/writing-systems.md` (the scripts in §7), `synthesis/worldbible-integration-contract.md` (the handoff)
- scope: a reference method for the linguistics partition. It records how two scholarly sources frame construction and classification; it decides no world's language and rules on no real-world attribution
- refuses: canon for any world; any claim that either source settles the field; current population counts of conlangs

## §1 Calibration key — what each source can carry

| Framework | Status | Why it is placed there |
|---|---|---|
| Enguehard's teaching argument (2022) | a single author's position, not a field consensus | one author arguing from his own classroom in one article; the opened abstract carries no curriculum, cohort or count |
| Sidorova & Shuvalova's typology (2006) | published descriptive taxonomy in the Russian tradition; terminology contested | the book records that neither linguists nor conlangers agree on class names, and adopts one of several surveyed classifications |
| Henning's volume rule (§4) | practitioner taxonomy, not peer-reviewed | a conlanger-community organiser's scheme, reported by the book, not tested by it |
| Yaguello's pathology framing (1985) | contested and hostile | reported as the hostile pole; the book notes it selects the strangest cases |
| Schnapp's "impoverishment" thesis | contested | a published position that Higley argues against in the same survey |
| Higley's model-and-artefact account | contested, published, venue not named by the book (to-verify) | the position the book reports as answering Schnapp |

These statuses are this entry's calibration, not either source's self-description. The sources' own words appear below, each with its row's id.

## §2 Construction as a teaching method

Enguehard argues from his own teaching that "the construction of languages by students allows them to better grasp the reality of linguistic analysis" than repeated exercises on natural-language data (S876).
His second claim is the one that makes the article usable here: the reasons that lead him to push natural languages out of teaching are "the same ones that lead most linguists to marginalize constructed languages from research" (S876).
The article's keywords include Constructed languages, Linguistic Analysis, Linguistics Teaching and Method-Oriented Teaching (four of the ten the page lists, with Phonology and Diachronic linguistics among the rest) (S876).
What the abstract does not carry is a curriculum, a cohort or a measured outcome; treat the argument as a position, because the abstract is the whole opened artefact (S876).
Design consequence: a constructed language is a legitimate object of analysis, not only a display. Ask what analysis a language makes possible — a rule to discover, a paradigm gap to explain — before asking how many words it has.

## §3 A taxonomy to file a world's languages into

The book adopts one classification out of several it surveys, and states that neither linguists nor conlangers share a terminology for the classes (S877).

| Class, in the book's numbering (p. 11) | What the book means | Design question it forces |
|---|---|---|
| 1. Auxlangs | international auxiliary languages: Esperanto, Ido, Lojban | is this language meant for real strangers to speak? |
| 2.1 Artlangs | languages invented by authors of fiction, film and games | does the language belong to a story? |
| 2.1.1 | artlangs that left their fictional world: Tolkien's, Klingon, D'ni | did it outlive its text? |
| 2.1.2 | artlangs that function, or are only mentioned, inside the work | is it named but never spoken? |
| 2.2 Personal, or авторские, languages | invented by individuals or groups for their own pleasure, with the Internet as primary habitat | is there an author outside any fiction? |
| 2.2, germinal case | projects the book calls языки-наброски: they never leave the germinal stage, are not tied to a world, or partly revise natural languages | is there a world at all? |

The book's own subject is class 2.2, not the artlangs it surveys beside it (S877).
It reports several competing classifications, with their criteria, without adopting them: structure and purpose (Rosenfelder), a priori versus a posteriori (Harrison, developing a distinction the book traces, via Kuznetsov, to Couturat and Leau), potential use and potential users (Capuzzo), and a composite letter-plus-SVO index from a University of Hong Kong page (S877).
It also records that the boundaries shift: a language written for a fiction can leave it and be used in the real world, as Klingon and Tolkien's Elvish did, and the book asks whether Klingon should now count as a living natural language (S877).

## §4 How much language the world actually needs

The book reports Henning's volume rule: the required size and detail of lexicon and grammar follow from what the language is for (S877).
Of the classifications it surveys, this one transfers most directly to a build.

| Use | What the book reports is enough |
|---|---|
| jargon — a handful of words carrying «вкус другой культуры» | a few words plus plural rules |
| naming language — names for characters and places | no special grammar |
| a language for real communication, or for literature | far more |

Read that rule against `linguistics/naming-systems.md` (S877).
Design consequence: a setting that only needs names is not under-built, and dialogue that carries weight needs the third row, not the second.

## §5 Fictional and auxiliary languages are different contracts

The book draws the contrast on three axes: auxiliary languages aim at the widest possible body of users, are meant to reflect the world and thought of Earth's speakers, and answer a demand for equal structural simplicity; fictional languages claim no wide body of users, are meant to carry a world picture deliberately unlike ours, and are bound by no simplicity requirement (S877 pp. 16–17, 19–20).
It states the difference as a modality: "Эти языки и их создатели не «должны», а «могут»." (S877 p. 19)
It adds a genre fact with design teeth: among fictional-language makers a memorandum or manifesto telling others how a correct language must be built is unacceptable, and even the how-to literature offers options rather than constraints (S877 pp. 19–20).
It names the leading function: where auxiliary languages are built for communication, fictional languages are built for the poetic function in Jakobson's sense — attention to the message for its own sake (S877 p. 21).

## §6 The description is the language, and history can be written backwards

For the personal languages the book studies, the description comes first; it names this "первичность описания языка", the precedence of a language's description over the language itself — a word or a passive exists only once the grammar says so (S877 p. 6).
Hence its preference for the word project over grammatical description: "описывают то, что уже существует, проектирование подразумевает создание объекта" (S877 p. 6).
Change in such a language is not the drift of a speech community but a discontinuous, deliberate act by the author, or by users with the author's sanction — adding words or rules, lifting a phonotactic constraint, adding a morphophonological process, sometimes only to vary or beautify the language (S877 p. 22).
A natural language runs one way in time; an author may write a constructed language's history backwards, reconstructing stages that supposedly preceded the first invented system, or forwards, modelling later development, and may rewrite the available resources when they obstruct the story (S877 p. 22).
Design consequence: the grammar file, not the corpus of attested sentences, is the canon carrier, and a family's depth is a decision rather than a by-product.

## §7 Three languages that left the page

| Language | Built by, and for what | What the book records | Transferable lever, this entry's reading |
|---|---|---|---|
| Tolkien's Arda languages | Tolkien, credited by the book («считается») with nearly two dozen languages of his legendarium | Quenya and Sindarin carry a corpus, including a translation of the Lord's Prayer, while others survive as handfuls of names and grammar fragments | uneven depth across a family reads as real |
| Klingon | Marc Okrand for Star Trek, built on extinct Native American languages with an aim of maximal difference from Earth's languages | OVS order, no tense, no gender, no adjectives, its own script; a Klingon Language Institute from 1992, a journal with an ISSN, dictionaries, dissertations | deliberate typological distance plus an institution |
| D'ni | Richard A. Watson for the Myst games | fans assume the language already exists complete and is revealed piece by piece, with its creator running the decipherment | withholding the description as a discovery mechanic |

Pages of the three rows above in the monograph: Tolkien p. 23; Klingon pp. 24–25; D'ni p. 26 (S877).

The book's explanation for D'ni's standing is not Myst's popularity but the status the series gave its language component and the linguistic puzzle built around it (S877 pp. 26–27).
It treats Tolkien as the movement's father even while noting that constructed languages in fiction predate him (S877 pp. 22–23).
The grammatical description of Klingon above is the book's report, not re-checked against Okrand's own grammar (to-verify).

## §8 Status in the field, as the 2006 monograph reports it

It states that works treating fictional languages seriously "исчисляются единицами", against a large literature on Esperanto, Ido and Lojban (S877 pp. 11, 27).
Yaguello's *Lunatic Lovers of Language* (1985; English translation 1991) frames invention as pathology and its makers as dilettantes, and the book reports it as the hostile pole (S877 pp. 27–28).
Schnapp calls conlangers «филологами воображаемых миров» but holds invented languages to be "impoverishments of the natural languages" (S877 p. 28).
Higley, arguing against Schnapp and with Henning, holds that "конланги – это действительно модели, артефакты": nobody sails a model sailboat, nobody thinks and speaks in a conlang, though translation to and from one is possible (S877 p. 29).
The book's counters are dated and are not reused as current figures here: about 1,500 conlangs listed at langmaker.com, 773 languages with creation dates at conlang.com as of 28 July 2005, and a US language-modelling society of about 20,000 members in 1999 (S877 pp. 5, 8).

## §9 Coupling to the world bible

Hand off under `synthesis/worldbible-integration-contract.md`: this entry supplies the class distinctions, the volume rule, the description-first discipline and the authored-history switch; lore decides which class a world's language belongs to, how deep its documentation goes, and what the bible records as canon.
Nothing here rules on any world: no class assignment, no depth target and no direction of history is fixed for a setting by this entry.
