# CriticGapPremise — round 52, attempt 1: attack on claim C (speech-surrogates entry, 227 -> 228)

Seat: KotodamaR52.CriticGapPremise (critic, leaf). Lane worktree read at `dea5ece` (base `147cfde`, declaration `d9f73c8`). Author-lane advice, never admission. No files edited other than this report. No tools installed.

## 0. Result

**The gap is real, but the declared gap evidence understates the ground that is already owned. That is a fixable defect, not a reason to reject.** No base entry owns speech surrogates as a cross-channel conlang method: there is no owner for the channel typology, for whistled speech beyond two lines, for non-drum instruments, or for ecology, social control and transmission. But `claims.json` C `gap_evidence` says the partial owners are "one to three lines each", and its topic grep only scanned `- topic:` lines. That misses three civilization entries with body-level surrogate sections. The largest, `civilizations/yoruba.md:41-58`, is an 18-line section with a table. `civilizations/fon-dahomey.md:31-43` already has the surrogacy-versus-signal table that C's planned §3 "signal-code boundary" would rebuild. If the C drafter works only from the five declared owners, the declared falsifier ("restates a partial owner's register rather than citing it one-way") will fire.

Impacted axes: coverage (primary), plus calibration (QUALITY 2), provenance and tiers (QUALITY 1 and 6) and ordinary access (QUALITY 10).

## 1. Do the declared partial owners already own speech surrogates? No. All lines below were re-read at the lane worktree.

| Location | What it actually says | Owns surrogates? |
|---|---|---|
| `culture-material/music-instrument-lexicon.md:98` | one myth-type table row: "instruments that speak", dùndún, atumpan, Lokele, cited to Carrington (1949) and Finnegan (1970) inline, with no S-ids | no; one row |
| `culture-material/music-instrument-lexicon.md:100` | the register claim "Drum and whistle speech are language phenomena, not merely music phenomena" and a pointer to phonetics | no, but **C's §1 register property must cite this line one-way rather than restate it** |
| `culture-material/music-instrument-lexicon.md:121` (not declared) | checklist item 9: "If the language is tonal, let an instrument speak (dùndún pattern)" | no; but it is the permissive seed of the "tonal implies drums" over-generalization (§3 below) |
| `culture-material/music-instrument-lexicon.md:76` (not declared) | "Bugle calls (reveille, last post) are a fixed ceremonial lexicon binding time-of-day to action" | a signal-code partial owner that C's §3 boundary must cite |
| `linguistics/phonetics-phonology.md:196-200` | listed under "Solid couplings": "Whistled speech: mountains + long-distance herding -> whistled registers (Silbo Gomero, Kuşköy, Chinantec; Meyer 2008)"; drum language "needs tonal lexicon + redundancy" | no; four lines. **Its "Solid" label is stronger than the evidence (§3)** |
| `linguistics/phonetics-phonology.md:75`, `:309-310` (not declared) | the couples mention "whistle & drum channels"; an erratum recheck of the "Silbo Gomero whistled register (UNESCO element record)" | no |
| `linguistics/orality-formulaic-language.md:114`, `:124` | "Media extensions … a 'broadcast layer' for the same formulas"; a meter-table row on drum and whistle speech | no |
| `linguistics/orality-formulaic-language.md:24`, `:128` (not declared) | the sources line (Busnel & Classe 1976); a NON-CANON example with "a drum layer that transmits muster-orders … across the steppe" | no; but `:128` is an invented example, **never evidence for relay range** |
| `linguistics/sound-symbolism.md:121` | a hook-table row pointing to music-instrument-lexicon and phonetics §7 | no |
| `linguistics/sound-symbolism.md:19` (not declared) | "`phonetics-phonology.md` — … its §7 owns whistled/drum channels" | **an explicit ownership assertion that will conflict with C once C lands** |

Ground the declaration did not list (the strongest counterexample available locally):

| Location | Content | Consequence for C |
|---|---|---|
| `civilizations/yoruba.md:41-58` | dùndún surrogate modes DT-D, DT-P, DS and D-DR (Durojaye et al. 2021); "do not model it as universally intelligible Morse code" (`:46`); one-to-many melody-to-utterance mapping (`:47`, Abiodun 2014); coupling chain (`:58`) | C's §5 and §6 must cite these one-way. Re-tabulating DT-D through D-DR, or restating the "not Morse code" rule, is restatement |
| `civilizations/fon-dahomey.md:31-43` | a table of speech surrogacy, conventional signal, ritual or dance music and royal praise, with what carries meaning and what verification is needed (`:37-42`); "Tone without consonants and vowels is not automatically a lossless message channel" (`:44`) | **this is C's planned signal-code boundary at single-culture scope.** C extends it across channels and cites it; it does not rebuild it |
| `civilizations/akan.md:28`, `:58` | McPherson & Obiri-Yeboah (ACAL 53 abstract): the atumpan encodes only H and L, downstepped H is played as plain H, and tone/note mismatches occur | cite one-way for the encoding-loss example in §6 |
| `linguistics/sign-languages-manual-modality.md:61`, `:135-146` | alternate sign languages used "where speech is impractical or disallowed"; occupational signing in noise (`:144`); design rule "set the trigger first" (`:146`) | C's §1 diagnostic and §7 ecology overlap the trigger logic. Cite one-way. These lines are **not** among D's changed lines (83, 87, 90, 92, 93), so they are citable under C's `must_not_cite` |
| `culture-material/transport-mobility-lexicon.md:27` | the "clock" quantity: how long a message takes, with courier relays | any message-speed or relay claim in C defers to this owner |
| `linguistics/language-shift-obsolescence-revival.md:3` | owns shift, vitality frameworks (GIDS, UNESCO, EGIDS) and revival | C's §9 "decline" stays at design mechanism and hands vitality and revival frameworks to this owner |

Sibling lanes: `rg -il 'whistled (speech|language)|talking drum|speech surrogate|drum language|silbo'` across `*/corpus` and `*/knowledge` outside kotodama gives 0 files. `audio-shokunin/PROVINCE.md` owns game-audio production and measurement, not language. No fleet duplicate exists.

Verdict on question (1): the gap holds. The ground C may claim as new is the cross-channel typology, whistled speech, the non-drum instruments, ecology, social control, transmission and perception, plus the decision table. Drum speech is already partly owned at single-culture scope by yoruba, fon-dahomey and akan.

## 2. Does it fit the province, or drift into acoustics, ethnomusicology or heritage policy?

It fits `PROVINCE.md:3-7` (conlang design; the coupling of word and world), provided the entry stays on one question: which features of a conlang's spoken form survive in a given channel, and who controls that channel. Drift points:

| Drift | Where C would cross the line | Owner, or why it is refused | Guard |
|---|---|---|---|
| Acoustics | measured bands (Hz, kHz), decibel levels, formant-transposition physics, range tables in km | `audio-shokunin` measures sound; this lane does not | state acoustics only as a design constraint ("whistles carry pitch and timing, so segmental contrasts must map onto them"), sourced, with no measurement tables |
| Ethnomusicology and organology | Hornbostel–Sachs classification of the instruments, repertoire catalogues, performance analysis | `music-instrument-lexicon.md:9-28` owns organology | name instrument classes by channel property (pitch-bearing, rhythm-only, two-pitch), not by the H-S decimal; cite music-instrument-lexicon for classification |
| Heritage policy | "should be taught / safeguarded", school-mandate recommendations, UNESCO inscription as an endorsement | refused by `PROVINCE.md` (the assignment's "never … heritage-policy rulings"); vitality frameworks belong to `language-shift-obsolescence-revival.md` | UNESCO appears only as a cited dossier statement ("UNESCO's 2009 inscription states …"), never as a recommendation or as tier A for linguistic facts |
| Living practice | reproducing a real community's drum or whistle phrases as craft material | `yoruba.md:7` "this is not an initiation manual"; `fon-dahomey.md:35` warns against transplanting one community's drum vocabulary | the NON-CANON example uses an invented language only; real phrases are quoted only as cited evidence |
| Canon and game mechanics | "the world has a drum network"; a whistle-code stealth mechanic | lore-shokunin (canon) and game-dev (mechanics), per `PROVINCE.md:16-20` | Scope ends in `Handoff: lore-shokunin owns …`; no mechanics |

## 3. Claims that are dangerous to over-generalize. Sources opened 2026-10-22 by plain request.

| Hazard | Evidence | Required status and handling |
|---|---|---|
| "Bush telegraph" range and speed | `https://en.wikipedia.org/wiki/Talking_drum`, body paragraph naming dùndún, atumpan and fontomfrom: "They send messages up to distances of 20 miles (32 km), where other drummers relay them, quickly spreading news. [citation needed]". The same page also says "4–5 miles" | Tier C lead with its own "citation needed" tag, so it can never be sole support. Any range or relay-speed number needs an opened non-C source with its conditions, or `(to-verify)`. "Bush telegraph" appears only as a flagged colonial-era trope (R or C). Speed belongs to `transport-mobility-lexicon.md:27`. `orality-formulaic-language.md:128` is NON-CANON and not evidence |
| Whistled range | `https://en.wikipedia.org/wiki/Whistled_language`, "Characteristics" section: "typically 1–2 kilometres … but up to 5 km … in mountains and less in reverberating forests" | B at most, conditional on terrain; never a bare number |
| Number of whistled languages | same page, lead: "Speakers of more than 80 languages have been found to practice various degrees of whistled speech, most of them in rugged topography or dense forests" | Counts depend on the definition (a whistled register of a language versus a whistled language; leaf or flute courtship whistling is listed on the same page) and on the date. State it as "reported, dated, definition-scoped" with the counting source named. Never a single universal figure; tier C cannot carry it |
| Guanche origin of Silbo | `https://en.wikipedia.org/wiki/Silbo_Gomero`, "History": "it is assumed that their phonological system must have been simple enough …"; "It was used by the island's original inhabitants, the Guanches"; the 16th-century adaptation is tagged "[citation needed]". UNESCO's element record (below) says only "Some local variations even point to their origin" | Status C or T. **Never attribute a Guanche origin to UNESCO**, which does not assert it. Never state it as fact |
| Heritage-dossier superlatives | `https://ich.unesco.org/en/RL/whistled-language-of-the-island-of-la-gomera-canary-islands-the-silbo-gomero-00172`, description paragraph 1: "it is the only whistled language in the world that is fully developed and practised by a large community (more than 22,000 inhabitants)"; also "With practice, whistlers can convey any message"; "two distinct whistles replace the five Spanish vowels, and there are four whistles for consonants"; "Taught in schools since 1999" | Tier B for "what the 2009 dossier states", never tier A for typology. The inventory counts are contested: the Wikipedia whistled-language page reports analyses ranging from four to nine consonants, depending on elicitation method, so they are status C. "Any message" conflicts with the intelligibility studies on the same page, so it is never stated as a property. The school fact is dossier-cited, with no policy inference |
| "Every tonal culture drums" / "drums need tone" | `music-instrument-lexicon.md:121` (permissive); `phonetics-phonology.md:199-200` "needs tonal lexicon". Seifart et al. 2018 (Bora), abstract via Europe PMC PMC5936885: "Many drum communication systems around the world transmit information by emulating tonal and rhythmic patterns of spoken languages in sequences of drumbeats." | Neither direction is a law. Bora encodes rhythm (vowel-to-vowel intervals) as well as tone, and it is Amazonian, which also refutes "drum language is African". Whistled Silbo encodes non-tonal Spanish (UNESCO above). [INFERENCE] Most tone-language communities have no instrument surrogate, so tone is an enabling condition, not a trigger. Status B with the scope named |
| Ecological determinism | `phonetics-phonology.md:196-198` files whistled speech under "Solid couplings: mountains + long-distance herding". The Wikipedia lead gives "rugged topography or dense forests" | C must bound this as a tendency (B) and name the forest case. Citing phonetics one-way while silently contradicting it leaves two authorities in disagreement, so C's Recheck must name the divergence and the lesson must route a repair |
| Lossless or "Morse code" channel | already owned: `yoruba.md:46`, `fon-dahomey.md:44`, `akan.md:58` | cite; do not restate. A table cell saying "any message" or "lossless" must not appear unflagged |
| Secret or deception anecdotes; classical continuity | Wikipedia whistled-language page: "Stories are told of farmers in Aas …"; Xenophon's Mossynoeci placed in "the same area" as Kuşköy | anecdote, not evidence. No claim of continuity from antiquity to Kuşköy |
| Horns, reed pipes, jaw harps, xylophones, gongs | no base owner, and the thinnest evidence of the whole typology | each row needs an opened source this round, or it is marked T and carries no design rule. Do not fill cells from tier-C pages |

Access trap found this session: `https://royalsocietypublishing.org/doi/10.1098/rsos.170354` and `https://doi.org/10.1098/rsos.170354` both return HTTP 403 with "Just a moment" and `challenge-platform`. That is the same class of barrier that sank S094. The ordinary route is Europe PMC: `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5936885/fullTextXML` returns HTTP 200. Any row for this paper must name the PMC route.

## 4. What would make the 228 count hollow?

The counter (`find corpus/knowledge -name '*.md' | wc -l`) measures files, not owned knowledge. The count is hollow if any of the following holds:

1. **Restated ground.** The drum sections re-tabulate yoruba, fon-dahomey or akan material, or §1 restates `music-instrument-lexicon.md:100`. The file is new; the knowledge is not.
2. **Placeholder typology.** The planned non-drum instrument rows (horns, reed pipes, jaw harps, xylophones, gongs) rest only on `(to-verify)` marks or tier-C rows. Then the coverage claim for "other instrument-borne speech" is a scaffold.
3. **Tier inflation.** The S134+ rows are mostly Wikipedia (tier C) or abstracts (tier B) carrying substantive claims, so there is no admitted claim with real support (QUALITY 1, 6; `SOURCES.md` header).
4. **Access-tainted rows.** A row opened through a challenge is cited (QUALITY 10). Note the checker's blind spot: `tools/check-source-access.py:32-33` flags only the words `headless`, `bypass` and `solved … captcha/challenge` in the row text. A row that silently omits its route passes. Exit 0 is necessary, not sufficient.
5. **Two owners after landing.** `sound-symbolism.md:19` will still say phonetics §7 "owns whistled/drum channels", and `phonetics-phonology.md:196-198` will still call the coupling "Solid". Future probes would route to the wrong owner. This does not falsify the count, but it is a coverage-integrity defect that must be routed.
6. **Contract shells.** Fewer than 15 boundary rows, no `DR-SRG-` records, a NON-CANON example built from a real community's phrases, or a calibration bank without R/C/B/H/T codes. `DR-SRG` has 0 hits in `corpus` and `reports` at base, so the prefix is free.
7. **Index or registry drift.** README totals, the linguistics heading (26 -> 27), the sweep footer, and `used-by` cells not naming the entry.

## 5. Must-not list for the C drafter and integrator

1. Must not re-tabulate dùndún modes DT-D, DT-P, DS or D-DR, the atumpan H/L loss, or the fon-dahomey surrogacy-versus-signal table. Cite `yoruba.md:41-58`, `akan.md:58` and `fon-dahomey.md:37-44` one-way.
2. Must not restate `music-instrument-lexicon.md:100` as its own register claim. Cite it, then state what the new entry adds (the cross-channel test).
3. Must not cite `sign-languages-manual-modality.md:83`, `:87`, `:90`, `:92` or `:93` (D's changed lines), `corpus/lessons/round-52.md`, or any S-id below S134.
4. Must not state a range, relay speed or language count without a dated, conditioned, non-C source; otherwise `(to-verify)`.
5. Must not assert a Guanche origin, and must not attribute one to UNESCO.
6. Must not use the UNESCO dossier as tier A for phoneme inventories or typology, and must not repeat "only fully developed whistled language" or "any message" as fact.
7. Must not state "tonal implies drums" or "drums require tone" as law. Must not frame drum language as African only (Bora, PMC5936885).
8. Must not call whistled speech an ecological law; bound it as B, with the forest case.
9. Must not make heritage-policy recommendations (safeguarding, schooling mandates) or restate vitality frameworks; hand those to `language-shift-obsolescence-revival.md`.
10. Must not include measured acoustics tables (Hz, dB, km), and must not reclassify instruments with Hornbostel–Sachs (hand to `music-instrument-lexicon.md`).
11. Must not reuse a real community's drum or whistle phrases in the NON-CANON example.
12. Must not cite any row whose URL was opened through a challenge. Route Royal Society papers through PMC.
13. Must not let a typology row carry a design rule when its only support is `(to-verify)` or tier C.
14. Must not edit `sound-symbolism.md` or `phonetics-phonology.md`: they are not in C's lands, and changing the lands after declaration breaks QUALITY 7 and 9. Route the ownership pointer and the "Solid" label as defects instead.

## 6. Concrete falsifiers for wave 2 (run in the integrator's clone; all read-only)

Let `E=corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`. Pipes inside the table's commands are escaped for Markdown: turn every `\|` back into `|` before running a command, or ripgrep will read it as a literal pipe.

| # | Check | Command | Fails if |
|---|---|---|---|
| F1 | count | `find corpus/knowledge -name '*.md' \| wc -l` | not 228 |
| F2 | length | `wc -l < $E` | above 250 |
| F3 | unlisted owners cited | `rg -o 'civilizations/(yoruba\|fon-dahomey\|akan)\.md:[0-9]+' $E \| sort -u` | fewer than 3 distinct files |
| F4 | other boundary owners | `rg -c 'sign-languages-manual-modality\.md:(61\|13[5-9]\|14[0-6])\|transport-mobility-lexicon\.md:27\|language-shift-obsolescence-revival\.md\|music-instrument-lexicon\.md:(76\|100\|121)\|sound-symbolism\.md:(19\|121)\|phonetics-phonology\.md:19[6-9]' $E` | any of these owners absent from the §2 table |
| F5 | D-line guard | `rg -n 'sign-languages-manual-modality\.md:(83\|87\|90\|92\|93)\b' $E` | any hit |
| F6 | restatement probe | `rg -n 'DT-D\|DT-P\|D-DR\|downstepped\|gun-gun\|Morse' $E` | a hit without a `yoruba.md:`, `akan.md:` or `fon-dahomey.md:` citation on the same line |
| F7 | 8-word shingle overlap | in memory: lowercase, strip punctuation, build 8-word shingles of `$E` and of each owner (yoruba.md, fon-dahomey.md, akan.md, music-instrument-lexicon.md, phonetics-phonology.md, orality-formulaic-language.md, sound-symbolism.md, sign-languages-manual-modality.md) | any shared 8-gram outside a quotation or path |
| F8 | S-id floor and registry | `rg -o 'S[0-9]{3}' $E \| sort -u`, then look each id up in `corpus/SOURCES.md` | any id below S134, missing, status not `mined`, or `used-by` not naming `$E` |
| F9 | tier-C sole support | for each line of `$E` that cites S-ids, collect the tiers of those rows | any factual line whose only cited rows are tier C |
| F10 | access, checker leg | `python3 -B tools/check-source-access.py` | not exit 0 |
| F11 | access, fresh-route leg (covers the checker's blind spot) | for each new row URL: `curl -sL -A <ua> -o p -w '%{http_code}'` from a fresh shell, then `rg -i 'challenge-platform\|Just a moment\|captcha' p` | non-200 or a challenge marker on the URL as recorded, unless the row names an ordinary route (Wayback, PMC) that returns 200 |
| F12 | quote in bytes | for each new row, the 25-word-or-shorter quote must appear verbatim in the plain-fetched text at the recorded location | absent, or over 25 words |
| F13 | Guanche | `rg -n -i 'guanche' $E` | a hit without status C or T, or with `(to-verify)` missing, or attributed to UNESCO |
| F14 | numbers | `rg -n -i '[0-9]+ ?(km\|kilomet\|miles?)\b\|more than (70\|80)\|bush telegraph' $E` | a hit without a conditioned non-C source or `(to-verify)`; "bush telegraph" not flagged as a trope |
| F15 | universals | `rg -n -i 'any message\|lossless\|every tonal\|all tonal\|only whistled language\|always\b' $E` | an unflagged hit |
| F16 | province | `rg -n -i 'should be (preserved\|protected\|taught\|safeguarded)\|\bHz\b\|kHz\|\bdB\b\|Hornbostel' $E` | any policy recommendation, measurement table or reclassification |
| F17 | canon | `rg -n 'Handoff: lore-shokunin owns' $E`; the NON-CANON paragraph is checked for real-language phrases | handoff missing, or a real community's phrase used as craft material |
| F18 | contract | ReviewEntryContract §2.9 Part A checker (head order, single H1 with em dash, zero H3, numbered H2s ending Recheck then Scope); `rg -c '^\| DR-SRG-' $E`; boundary rows 15 or more | any failure, zero DR rows, or fewer than 15 boundary rows |
| F19 | separability | `python3 -B tools/check-claim-separability.py reports/round-52/separability-manifest.json`; `rg -n 'lessons/round-52' $E` | not exit 0, or any hit |
| F20 | index | `python3 -B reports/round-28/readme/sweep.py`; `rg -n '^## linguistics/ \(27\)\|Total knowledge entries: 228' corpus/README.md` | not rows 228 files 228, `topic_mismatch 0`, `footer_ok True`, or headings stale |
| F21 | owner conflict, record leg | `rg -n 'owns whistled/drum' corpus/knowledge/linguistics/sound-symbolism.md` | still 1 hit after landing with no routed-defect line in the round lesson |

## 7. Smallest safe corrections (all within C's declared lands, plus the lesson as a record)

1. Extend C's §2 boundary table to the owners in §1 of this report. Twelve or more are new rows, which also meets the 15-row contract with real owners rather than padding.
2. In §3 (signal-code boundary), start from `fon-dahomey.md:37-44` and `music-instrument-lexicon.md:76`. C's new content is the cross-channel test, not the single-culture table.
3. In §5 (drummed speech), support cross-cultural claims with rows opened this round (for example Bora via PMC5936885). Dùndún and atumpan details are citations only.
4. In §7 (ecology), use status B with the forest case. Name the divergence from `phonetics-phonology.md:196-198` in §13 (Recheck).
5. Keep §9 (transmission) at design mechanism and hand vitality and revival to `language-shift-obsolescence-revival.md`.
6. Record in the round lesson (not in `claims.json`, which is declared): the gap-evidence wording "one to three lines each" was false for `yoruba.md:41-58`; the topic-only grep missed body sections; and two routed defects, the ownership pointer at `sound-symbolism.md:19` and the "Solid couplings" label at `phonetics-phonology.md:196`.

Fixable or rejectable: everything above is fixable before landing. The canonical judge must reject if any of the following holds: F1, F5, F8, F10 or F19 fails; a cited row was opened through a challenge (F11); or F6 or F7 shows re-tabulation of an owner's table.

## 8. Unrun checks and limits

- C has not landed, so F1–F21 were not run against an entry. At base: count 227; README `## linguistics/ (26)` at `corpus/README.md:231`, `Total knowledge entries: 227.` at `:602`; `DR-SRG` 0 hits.
- The sources quoted in §3 were opened this session by plain `curl`. The three Wikipedia pages are tier-C leads only. UNESCO is tier B for dossier statements. The Seifart et al. 2018 abstract was read via Europe PMC (abstract only; tier B for claims about the work). None of these is registered; they are leads for wave-2 scouts.
- Carrington (1949), Meyer (2008, 2015), Busnel & Classe (1976) and Rialland (2005) were not opened this session.
- The "most tone-language communities lack instrument surrogates" line is marked [INFERENCE] and is unsourced.
- Tooling: none installed or updated.
