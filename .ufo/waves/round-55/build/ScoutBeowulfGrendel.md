# ScoutBeowulfGrendel — Grendel of Cain's kin, and what Old English *aglǣca* covers

- seat: `KotodamaR55.ScoutBeowulfGrendel` (scout, claim C ground: monsters and hybrid beings)
- round: kotodama 55 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `8eda9543e940bdc4938fad90182ee6a6fe271d0f`, claim base `f4015e70b829523ed81e14ce4279bfab0e0233e4`
- assignment: the Beowulf language coupling — what this culture calls the monstrous being, and what its word means — from an open edition with line numbers and the Bosworth-Toller entry for *aglǣca*, aimed at the design decisions named in the wave brief
- draft ids used below: `NEW-ScoutBeowulfGrendel-1` … `-3`; the L1 assigns the final `S` ids at integration

## Route summary (two works, three files)

Everything below was opened by ordinary means: plain `curl`, no browser, no challenge, no archive capture, no
access control met. Page text was decoded locally. Every quotation registered in a row, and every line quoted in
Findings, was re-checked as a substring of the fetched file after normalising whitespace, the transcription's
italic markers and its line-break spaces; all of them matched
(`/fast/scratch/hyaku/kotodama-r55/ScoutBeowulfGrendel/verify_quotes.py`). The only quotation marks around text
that is not in a source are the four English renderings flagged in the caveats (*mearc-stapa* and three others);
they are mine, and they are marked as mine.

| file | URL | route | bytes |
|---|---|---|---|
| Old English text + glossary, Harrison & Sharp 4th edn | `https://www.gutenberg.org/cache/epub/9700/pg9700.txt` | direct plain request (curl), HTTP 200 | 955837 |
| Bosworth-Toller, page 29 (lemma *ag-lǽca*) | `http://lexicon.ff.cuni.cz/html/oe_bosworthtoller/b0029.html` | direct plain request (curl), HTTP 200 | 15820 |
| Bosworth-Toller, page 30 (*ag-lǽc-wíf*, *ag-lǽcea*) | `http://lexicon.ff.cuni.cz/html/oe_bosworthtoller/b0030.html` | direct plain request (curl), HTTP 200 | 15917 |

Access date for all three: 2026-10-22. The dictionary host serves plain HTTP only: `https://lexicon.ff.cuni.cz/`
fails the TLS handshake (`error:0A000102:SSL routines::unsupported protocol`), so the pages were read over HTTP.
Nothing was circumvented. The two dictionary files are printed pages of one work, which is why they are registered
as two rows that quote different things rather than one row with split locators.

The edition's own orthography matters for every quote below: its preface states that long ash is printed `æ` and
short ash `ä`, long vowels carry a circumflex, and long diphthongs an acute on the second vowel. So `äglæca` and
`aglæca` are the same word in this text, and `wäs`/`hâten` are the edition's spellings, not typos.

---

### NEW-ScoutBeowulfGrendel-1

citation: Harrison, James A., and Robert Sharp, eds. *I. Beówulf: An Anglo-Saxon Poem. II. The Fight at Finnsburh: A Fragment*. 4th edn, revised, with notes; text and glossary on the basis of M. Heyne. Boston: Ginn & Company (copyright entry 1883). Corrected transcription, Project Gutenberg eBook #9700 (released 2006-01-01, updated 2021-04-11). Stable id: gutenberg.org/ebooks/9700.

url: https://www.gutenberg.org/cache/epub/9700/pg9700.txt

route: direct plain request (curl), HTTP 200, no challenge, 2026-10-22

kind: book

tier: A — a scholarly edition of the poem itself, with its own glossary, in a proofread transcription; authoritative for the poem's wording and for standard Beowulf line numbers. The transcription's preface states that it preserves the printed edition's editorial choices, including vowel quantities that do not match current consensus, so a claim about quantity is a claim about this edition only.

scope: what the poem says about Grendel at lines 102-113 (his name, his title, the ground he holds, his descent from Cain, the kinds that spring from Cain), the poet's statement at lines 162-163 that men do not know where the beings go, and — in the same file, not quoted as a row item — the edition's glossary, which registers *aglæca* under both a demonic sense ("of Grendel, 159, 433, 593, etc.") and a heroic one ("of Sigemund, 894", Beowulf at 1513, Beowulf and the drake at 2593). Describes Grendel's body only at three points inside the grapple (723, 727-728, 817-819), never as an inventory of parts; does not name the manuscript or its date, and is a school and college text rather than a diplomatic transcript. Line numbers are the standard ones and agree with the dictionary's `B.` citations.

quotes:
- lines 102-104, the naming and the ground: "wäs se grimma gäst Grendel hâten, mære mearc-stapa, se þe môras heóld, fen and fästen; fîfel-cynnes eard"
- line 107, the kin and the vengeance: "In Caines cynne þone cwealm gewräc"
- lines 111-113, the kinds that spring from him: "Þanon untydras ealle onwôcon, eotenas and ylfe and orcnêas, swylce gigantas"
- lines 162-163, the limit of knowledge: "mistige môras; men ne cunnon, hwyder hel-rûnan hwyrftum scrîðað"

teaches: The poem fixes Grendel by a title and a terrain, derives him and all monster kinds from Cain, and leaves his paths beyond what men know.

draft sentences:
- Name the being's address before its anatomy: the poet's title for Grendel is *mære mearc-stapa*, and what he holds is *môras*, fen and *fästen*, called the *eard* of the *fîfel*-kin, so the monster's country is marsh, fen and fastness (NEW-ScoutBeowulfGrendel-1, lines 102-104).
- Ground the monster in a genealogy rather than a habitat: the poem says the killing was avenged "In Caines cynne", and Grendel's line runs back to Cain (NEW-ScoutBeowulfGrendel-1, line 107).
- Let one ancestor yield many kinds: from Cain "untydras ealle onwôcon", *eotenas* and *ylfe* and *orcnêas* and *gigantas*, so a bestiary can open as a family tree whose branches are species, and the list can set native names beside a Latin-shaped one in a single line (NEW-ScoutBeowulfGrendel-1, lines 111-113).
- Write the edge of the survey as the monster's country, and write ignorance as the fact: he holds the misty moors, and "men ne cunnon" — men do not know — where the *hel-rûnan* glide in their turnings (NEW-ScoutBeowulfGrendel-1, lines 162-163).
- Compose the body out of what it does in contact, not out of borrowed parts: the poem gives Grendel a hand that bursts the hall door, eyes that give light like fire, and a shoulder where the sinews spring and the bone-locks burst, and never a whole shape (NEW-ScoutBeowulfGrendel-1, lines 723, 727-728, 817-819).
- Decide whether the being acts on its own or as an instrument: Grendel comes from the moor "godes yrre bär", bearing God's wrath, so the poem makes the devourer an executioner before it makes him a character (NEW-ScoutBeowulfGrendel-1, line 711).

---

### NEW-ScoutBeowulfGrendel-2

citation: Bosworth, Joseph, and T. Northcote Toller. *An Anglo-Saxon Dictionary*, 1898, page 29, lemma *ag-lǽca*. Online edition by the Germanic Lexicon Project, served at lexicon.ff.cuni.cz; page generated 2021-03-13. Stable id: lexicon.ff.cuni.cz/html/oe_bosworthtoller/b0029.html.

url: http://lexicon.ff.cuni.cz/html/oe_bosworthtoller/b0029.html

route: direct plain request (curl), HTTP 200, no challenge, 2026-10-22

kind: book

tier: A — the standard nineteenth-century dictionary, primary for its own glosses and citations, and the work the edition in row 1 cites in its notes as Toller-Bosw.; but it is an 1898 work in a volunteer-corrected transcription, so any contentious reading should be checked against a page image. Tier A for what this dictionary records, not for current etymology.

scope: the lemma *ag-lǽca* as printed on page 29: its variant spellings (*ag-lǽca*, *-lǽcea*, *-léca*; *ah-*, *æg-*, *æc-*), the English gloss that runs wretch, miscreant, monster and fierce combatant together, the Latin pair *monstrum* and *bellator immanis*, the bracketed etymology from *ag-lác* "misery", and the first citation (B. 739, Grendel). Also the preceding lemma *ag-lác* on the same page, which defines the base noun. Does not distinguish poetic from prose usage, gives no date for the word, and does not argue the senses; the lemma continues onto page 30.

quotes:
- lemma *ag-lǽca*, the English and Latin gloss: "A miserable being, wretch, miscreant, monster, fierce combatant; miser, perditus, monstrum, bellator immanis"
- lemma *ag-lǽca*, first citation, B. 739: "Ne ðæt se aglǽca yldan þohte nor did the wretch [Grendel] mean to delay that"
- lemma *ag-lǽca*, bracketed etymology: "ag-lác, -lǽc misery; a the m. of personal noun"
- lemma *ag-lác*, the base noun: "Misery, grief, trouble, vexation, sorrow, torment; miseria, dolor, tribulatio, molestia, tristitia, cruciatus"

teaches: Bosworth-Toller glosses *aglǽca* as wretch, miscreant, monster and fierce combatant at once, and derives it from a base noun meaning misery and torment.

draft sentences:
- Decide whether the word for the being is a verdict or a measure of force: one lemma glosses *aglǽca* as "wretch, miscreant, monster, fierce combatant", and gives *monstrum* and *bellator immanis* as its Latin pair, so the dictionary itself will not choose between criminal and champion (NEW-ScoutBeowulfGrendel-2, lemma ag-lǽca, English and Latin gloss).
- Build the name on what the being does to people rather than on what it looks like: the lemma's etymology runs back to *ag-lác*, glossed "Misery, grief, trouble, vexation, sorrow, torment", and the personal noun is formed from it (NEW-ScoutBeowulfGrendel-2, lemma ag-lǽca, bracketed etymology).
- Expect the word to appear in action, not in description: the lemma's first citation is Grendel refusing to delay, quoted with its own English rendering and cited to B. 739 (NEW-ScoutBeowulfGrendel-2, lemma ag-lǽca, first citation).
- Fix one spelling of your term and keep it: the headword itself is printed with three endings and three initial forms, so the dictionary treats the word family as unstable and the worldbuilder must choose which form is canonical (NEW-ScoutBeowulfGrendel-2, lemma ag-lǽca, headword).

---

### NEW-ScoutBeowulfGrendel-3

citation: Bosworth, Joseph, and T. Northcote Toller. *An Anglo-Saxon Dictionary*, 1898, page 30, lemmata *ag-lǽc-wíf* and *ag-lǽcea* (tail of *ag-lǽca*). Online edition by the Germanic Lexicon Project, served at lexicon.ff.cuni.cz; page generated 2021-03-13. Stable id: lexicon.ff.cuni.cz/html/oe_bosworthtoller/b0030.html.

url: http://lexicon.ff.cuni.cz/html/oe_bosworthtoller/b0030.html

route: direct plain request (curl), HTTP 200, no challenge, 2026-10-22

kind: book

tier: A — same work and same transcription as row 2; primary for the printed lemma and its citations. The transcription splits *aglǽc-wíf* and *aglǽcea* with a space where the printed page breaks or spaces a syllable, which is a transcription artefact and is quoted as printed.

scope: the feminine *aglǽc-wíf* and its Grendel's-mother citation (B. 1259), the reduced lemma *ag-lǽcea* whose citations run B. 2520, 2557 and 2592 — that is, Beowulf's dragon fight — and the tail of the *ag-lǽca* lemma on the same page. Supports the dictionary's coinage of a feminine for Grendel's mother and its application of the word to the dragon; gives no argument for either and no translation of the Beowulf passages.

quotes:
- lemma *ag-lǽc-wíf*, the English and Latin gloss: "A wretch of a woman, vile crone; monstrum mu-lieris, mulier perniciosa"
- lemma *ag-lǽc-wíf*, the citation: "Grendles módor, ides, aglǽ c-wíf Grendel's mother, the woman, vile crone. Beo. Th. 2522 ; B. 1259."
- lemma *ag-lǽcea*, the citations: "Wið ðam aglǽ cean against the wretch, Beo. Th. 5033; B. 2520: 5107; B. 2557: 5177; B. 2592."

teaches: A separate feminine noun, *aglǽc-wíf*, names Grendel's mother a vile crone, and the dictionary's citations run the same word through the dragon fight.

draft sentences:
- Coin the female as its own noun rather than as the male with a suffix of convenience: the dictionary has *aglǽc-wíf*, glossed "A wretch of a woman, vile crone", and cites it for Grendel's mother at B. 1259 (NEW-ScoutBeowulfGrendel-3, lemma ag-lǽc-wíf).
- Notice that the gloss itself judges: "vile crone" is the dictionary's English, not the poem's, so a bestiary that translates its own terms is already making a moral claim (NEW-ScoutBeowulfGrendel-3, lemma ag-lǽc-wíf).
- Let the hero and the monster share the word if you want the fight to be a meeting of like powers: the same page cites *aglǽcean* at B. 2520, 2557 and 2592, the dragon fight in which Beowulf is one of the pair (NEW-ScoutBeowulfGrendel-3, lemma ag-lǽcea, citations).

---

## Findings for the entry's design decisions

Observed lines below are from the two works opened above, with line numbers; inference is marked.

| design decision | what these texts show | evidence |
|---|---|---|
| what the culture calls the being and what the word means | Grendel is named and titled in one breath: *grimma gäst*, then *mære mearc-stapa*. The word applied to him, *aglǣca*, is glossed by the dictionary as "wretch, miscreant, monster, fierce combatant" and by the edition's own glossary under two senses, "evil spirit, demon, a demon-like being" (Grendel, 159, 433, 593) and "great hero, mighty warrior" (Sigemund, 894; Beowulf, 1513; Beowulf and the drake, 2593) | row 1, lines 102-104 and glossary; row 2, gloss |
| how its body is composed | No inventory of parts and no composite anatomy. Outside the fight the being is carried by substances and roles: *atol äglæca* (159), *deorc deáð-scûa*, rendered here as dark death-shadow (160), *heoro-wearh hetelîc* (1268). Only inside the grapple are there body facts, and they are three: a hand laid on the door so that it bursts (723), eyes giving light like fire (727-728), and a shoulder where the sinews spring and the bone-locks burst (817-819) | row 1 |
| where it lives relative to the known world | A named terrain at the edge of settlement — *môras*, fen and *fästen*, the *eard* of the *fîfel*-kin (102-105) — and then an explicit refusal to locate it: "men ne cunnon" where the *hel-rûnan* go (162-163). The mother's country is water: *wäter-egesan*, "cealde streámas" (1261-1262) | row 1 |
| whether it warns, guards, punishes, teaches or devours | It devours by count, "þritig þegna" (122-123), and it executes: it comes "godes yrre bär", bearing God's wrath (711). Its raids push the Danes to vow at heathen shrines, which the narrator calls *hæðenra hyht* and condemns (175-183) — the monster is the occasion of a religious error the poet is warning against | row 1 |
| who records or depicts it, and in what kind of book or object | The recording is a hall performance: "þær wäs hearpan swêg" and "swutol sang scôpes" (89-90) — the monster is defined against the sound it interrupts at 99-102, "ôð þät ân ongan fyrene fremman, feónd on helle". No object or manuscript is described in the text | row 1 |
| what changes across periods | Two nineteenth-century witnesses already record the double sense. Bosworth-Toller's 1898 gloss pairs "monster" with "fierce combatant" in a single lemma; Harrison & Sharp's glossary (4th edn) separates the senses by referent and by line number, giving Grendel, the drake, Sigemund and Beowulf. [INFERENCE] The modern editorial debate over *aglǣca* therefore inherits a lexicographic ambiguity rather than inventing one; what changed is that the poem's own use for a hero became a problem to explain | rows 2 and 3; row 1, glossary |

### Opened in the same files, quoted here, not registered as row items

All from `pg9700.txt` (row 1), verified as substrings; each is available to the entry as evidence of the same row.

- Line 89-90, the hall-song frame: "þær wäs hearpan swêg" / "swutol sang scôpes".
- Lines 99-100, the hall-joy before the interruption: "Swâ þâ driht-guman dreámum lifdon".
- Lines 100-102, the interruption itself: "eádiglîce, ôð þät ân ongan fyrene fremman, feónd on helle".
- Lines 122-123, the count: "and on räste genam þritig þegna".
- Lines 159-160, the epithets: "atol äglæca êhtende wäs" / "deorc deáð-scûa".
- Lines 175-183, the heathen shrines: "Hwîlum hie gehêton ät härg-trafum" and "Swylc wäs þeáw hyra, hæðenra hyht".
- Lines 1260-1262, the mother's water: "ides aglæc-wîf yrmðe gemunde" / "se þe wäter-egesan wunian scolde, cealde streámas".
- Line 723, the hand and the door: "syððan he hire folmum hrân".
- Lines 727-728, the eyes: "him of eágum stôd lîge gelîcost leóht unfäger".
- Lines 817-819, the shoulder: "him on eaxle wearð syn-dolh sweotol, seonowe onsprungon burston bân-locan".
- Line 1268, the compound for Grendel: "heoro-wearh hetelîc".
- Line 711, the wrath: "Grendel gongan, godes yrre bär".
- Glossary, s.v. *aglæca*, sense 1: "evil spirit, demon, a demon-like being" (of Grendel, 159, 433, 593) — the transcription marks italics with underscores, which are omitted here.
- Glossary, s.v. *aglæca*, sense 2: "great hero, mighty warrior" (of Sigemund, 894).
- Glossary, s.v. *aglæc-wîf*: "demon, devil, in the form of a woman" (of Grendel's mother, 1260).
- Glossary, s.v. *aglæca*, the etymology it offers: from Gothic *aglo* "trouble" and Old Norse *agi* "terror" plus *lâc* "gift, sport", "= bringer of trouble". This is the edition's etymology, not the dictionary's; the two do not quite agree and the entry should not blend them.
- Poem lines where the word is used, from the text itself: 159 (Grendel), 433 (Grendel), 556 (a sea-beast Beowulf spears — "þät ic aglæcan orde geræhte"), 894 (Sigemund — "Häfde aglæca elne gegongen"), 2593 (Beowulf and the dragon — "þät þâ aglæcean hy eft gemêtton").

### Caveats the L1 should carry into the rows or the entry

- Do not translate *mearc-stapa*. The edition prints it as a compound and its glossary entry was not opened for this word, so any English ("boundary-stepper" and the like) is the scout's rendering, not a cited gloss. The entry can say the poem's title for Grendel is *mære mearc-stapa* and that he "held the moors", which is what the lines say.
- *fîfel-cynnes eard* and *untydras* are likewise rendered by me as "the land of the *fîfel*-kin" and "misbegotten broods"; the words are quoted in the original and no dictionary entry for *fîfel* or *untyd* was opened.
- The dictionary is 1898 and its English glosses are its own translations ("vile crone"). A sentence that says the poem calls Grendel's mother "a vile crone" is false; the poem calls her *ides aglæc-wîf*, and the crone is the dictionary's English.
- Each citation in the dictionary is printed twice: `Beo. Th.` and `B.`. [INFERENCE] `Th.` is the older Thorkelin numbering and `B.` the modern line numbers, judging by the abbreviations and by the numbers themselves, which run at roughly twice the modern value; the page itself does not gloss the abbreviations. Only `B.` agrees with the edition in row 1, so quote `B.` numbers in the entry.
- Two typographic artefacts in the transcription should not be reproduced as if they were spelling: *aglǽ c-wíf* and *aglǽ cean* carry a space from the printed page; *æ-acute;* in the raw HTML is the encoder's marker for ǽ.
- Nothing opened here supports any claim about Grendel's shape, his mother's body, or the dragon's anatomy beyond the hand, the eyes, the shoulder and the epithets quoted; the poem describes what a body does far more than how it is built, which is itself the finding.

## Not run

No lane command was run: this is a read-only scouting seat, the entry does not exist yet, and
`python3 -B reports/round-55/accept-c.py` would only re-measure the base. No file in the lane was created or
modified except this report. No tool was installed or upgraded (nothing was needed; `curl` and `python3` only).

unopened: Gummere's translation, Project Gutenberg eBook #981 (`https://www.gutenberg.org/cache/epub/981/pg981.txt`,
fetched, HTTP 200, 170898 bytes) — inspected and dropped, because its text carries no line numbers, so it cannot
supply the line locators the entry needs, and its renderings of *aglǣca* are a translator's choices rather than
lexicography; the modern online Bosworth-Toller at `https://bosworthtoller.com/` — the search page and entry-id
pages were fetched (170–183 KB each) but the entries are rendered client-side and no dictionary text appears in
the served HTML, so nothing could be read or quoted by ordinary request and no browser was used;
Klaeber's edition and the Dictionary of Old English — not attempted, since both are behind print or subscription
and the assignment's budget was met by an open edition plus an open dictionary.
