# CriticLearningClaim — round 53 falsify: is claim C a learning claim on uncovered ground?

Item attacked: claim C (`47ec825`), `corpus/knowledge/linguistics/gesture-co-speech-pointing.md`, against the session quality bar (admitted knowledge on ground the coverage map did not hold) and QUALITY criterion 4 (usability, "No essays"). Claim base `a9cf95f`. Seat: non-author, critic, leaf. No installs. No lane files touched except this report; source copies fetched into `/fast/scratch/hyaku/kotodama-r53/falsify/CriticLearningClaim/`.

## Verdict

Claim C stands as a learning claim, but its gap statement over-claims. At the base, the corpus had no material on co-speech gesture as part of the utterance (the iconic, metaphoric and beat types), on pointing forms, on how a language's packaging of motion shapes gesture, or on gesture acquisition. The one partial exception is a single boundary row in the sign-language entry. That is real uncovered ground. The over-claim is "quotable gestures": that is Kendon's name for emblems, and emblems were already owned at the base by `adornment-body-codes.md` in its H1 title and §7. The entry also restates that owner in three places.

On usability, the entry is a tool, not an essay: it has 14 tables, a decision table, a five-step build order with named artifacts, five DR-GES rows and a worked example. But the worked example contradicts the entry's own evidence in §6, produces only one of the five artifacts it promises, and is written as a single 382-word paragraph.

A non-author closure would most likely call coverage improved, as it did for the same claim shape in rounds 51 and 52 (`SCORECARD.md`, round-51 and round-52 coverage rows). Every defect below is fixable in place. None is a tradeoff that requires rejecting the claim.

## Checks run

| Check | Command or URL | Output |
|---|---|---|
| Claim statement and gap evidence | read `reports/round-53/claims.json` | C's `gap_evidence_at_base` already names adornment §7 (lines 77–93), sign-languages `:64` and `:161`, numerals `:107` and direction-symbolism `:6` and `:36` as partial owners |
| Adornment H1 and §7 at base | `git show a9cf95f:corpus/knowledge/culture-material/adornment-body-codes.md`, lines 1 and 77–93 | The H1 ends "… Cosmetic Vocabulary, Gesture and Posture". §7 is "Gesture and posture — engineered gradients and their failure modes": the Ekman–Friesen categories, with emblems as "the conlang-adjacent category"; Morris's emblem geography; Hall's proxemics; bow, *wai*, *sampeah*, kowtow and *adoratio* gradients; emblem collisions, including the Bulgarian nod inversion (`:92`); Barrett 2019 calibration and *verso pollice* (`:93`). It has nothing on co-speech gesture types, pointing forms, speech–gesture timing or acquisition. |
| Sign-languages at base, lines 1–15 and 60–70 | same, `sign-languages-manual-modality.md` | `:4` says adornment "owns gesture and posture as body code in its title and section 7, and keeps it — this entry claims signed languages and manual codes, not gesture". `:64` is a single boundary row: co-speech gesture "conveys information but is not conventionalized and systematic the way sign is (S087)". `:66` and `:161` route emblems to adornment `:79`. So sign-languages declines co-speech gesture; it does not own it. |
| Term sweep at base | `git grep -i -E '<pattern>' a9cf95f -- corpus/knowledge` for co-speech, McNeill, Kendon, lip-point, pointing, satellite-framed, verb-framed, Talmy, Kita, Özyürek, Mehrabian, 93%, left hand, Bulgari, de Jorio, Efron, Brookes, Yupno, Liszkowski, mirror neuron | Only one co-speech hit (sign-languages `:64`). No hits for McNeill, Kendon, lip-pointing, Talmy or framing, Kita (the gesture researcher), Yupno, Liszkowski, Mehrabian or mirror neurons. "Pointing" appears only in the Masoretic-script sense, sign-language INDEX `:103`, and direction-symbolism `:6` and `:33`. Left hand: only direction-symbolism `:9` (Hertz) and `:99` and `:100`. Bulgarian nod: only adornment `:92`. |
| Heading sweep that the entry's two gap sweeps cannot see | `git grep -n -i -E '^#.*(gestur\|pointing\|kinesic\|emblem)' a9cf95f -- corpus/knowledge` | Gesture headings: `adornment-body-codes.md:1` (H1) and `:77` (§7) only. Also `siam-thai.md:129` ("Khon: costume, gesture, voice"), a performance-genre owner, not a register owner. |
| Neighbour lines the entry's §2 cites | base lines `linguistic-anthropology.md:147`, `binding-speech-complex.md:108`, `symbol-lexicon-colexification.md:141`, `rome.md:43`, `byzantium.md:75`, `direction-symbolism.md:99`, `semantics-pragmatics.md:118`, `politeness-taboo-euphemism.md:75-76` | Each line carries what §2 says it carries. Each is a one-line mention, not a register. `direction-symbolism.md:99` owns the institutional hand polarity ("which hand takes oaths, eats, gives and receives"); §8 cites it at line 132. |
| Does the acceptance tool test "uncovered ground"? | `grep -n -i -E 'gestur\|topic\|gap\|owner' reports/round-53/accept-c.py` | It does not. It tests only COUNT, ENTRY, SWEEP and the S-id legs. The learning-claim qualifier depends entirely on non-author review. |
| S211 opened | `https://pure.mpg.de/rest/items/item_60538_2/component/file_60539/content` (HTTP 200, PDF) | Printed p. 24: "the proportions of participants that produced at least one Trajectory Only gesture was higher in Turkish and Japanese as a group than in English" |
| S230 opened | `https://mcneilllab.uchicago.edu/pdfs/gesture.a_psycholinguistic_approach.cambridge.encyclop.pdf` (HTTP 200) | Offprint p. 2: "Kendon prefers the term 'quotable gesture' … Emblems or quotable gestures are culturally specific, have standard forms and significances, and vary from place to place." |
| S223 opened | `https://pure.mpg.de/rest/items/item_762562_18/component/file_1466200/content` (HTTP 200) | Printed p. 700: "taboos against left hand pointing, index-finger pointing, or pointing at people". A search for "dead", "corpse" or "grave" finds nothing. |
| S190 page | `https://www.glossa-journal.org/article/id/9705/` | HTTP 200, but the page is a 490-byte script shell. Not used; no challenge was met. |
| Entry shape | Python line scan of the entry | 222 lines; 14 tables; line 181 (§11) is one paragraph of 382 words; seat and integrator wording on lines 7, 10 and 138; "UNESCO" on line 214 |

## Findings

### F1 — medium: the gap statement claims "quotable gestures" as unowned, but the base owned them as emblems

- Entry lines 3 and 4. Line 4 says "no file in the corpus owns co-speech gesture, pointing or quotable gestures as a register"; line 3's topic includes "emblem repertoires", and §7 (line 110) is titled "Quotable gestures and emblem repertoires".
- Source: S230, offprint p. 2: "Emblems or quotable gestures are culturally specific, have standard forms and significances, and vary from place to place." The two terms name one category.
- Base owner: `adornment-body-codes.md:1` (H1: "Gesture and Posture"), `:77` and `:79` ("*emblems* (culture-specific gestures with dictionary meanings — the conlang-adjacent category)"). The base sign-languages entry, `:4`, records that adornment "owns gesture and posture as body code in its title and section 7".
- Why the two gap sweeps return 0: they read filenames and `- topic:` lines only. They cannot see an H1 title or a section heading, so they cannot fail on the actual owner. That makes the "uncovered" clause unable to fail, the case QUALITY criterion 11 targets. The predecessor entry disclosed this blind spot; this entry's gap line does not.
- Impacted axis: coverage. The claimed new ground is larger than the real new ground.
- Fix, paste-ready, replacing line 4's first sentence: `- gap filled: no file in the corpus owns co-speech gesture or pointing as a register. Quotable gestures — Kendon's term for emblems (S230) — are owned as body code by \`culture-material/adornment-body-codes.md\` in its H1 title and §7 (\`:1\`, \`:77-93\`); this entry takes only how an emblem repertoire is documented and who may use it (§7). Heading sweep \`git grep -n -i -E '^#.*gestur' -- corpus/knowledge\` → 2 lines, both in adornment-body-codes.md (\`:1\`, \`:77\`).` Then keep the two existing sweeps. On line 3, replace `emblem repertoires` with `how emblem repertoires are documented and licensed`.

### F2 — high: the worked example teaches the opposite of §6's evidence

- Entry line 181 (§11) says the language "marks motion in the verb rather than in an adverb, which frees the hand from carrying the path", and later "§6 keeps path in the verb, so the accompanying hand is free to mark attitude instead of direction".
- Source: S211 (Kita and Özyürek 2003), printed p. 24: "the proportions of participants that produced at least one Trajectory Only gesture was higher in Turkish and Japanese as a group than in English". Speakers of languages that put path in the verb gesture path more on its own, not less. The entry's own §6 says the same: line 100 says "Two clauses mean two gestures, not one sweep", and line 105 says gesture fits "the semantic encoding of the event rather than compensate" (S213) and "Do not use gesture to carry what the lexicon refuses to carry".
- S230, cited for this sentence, supports only the general point that gesture differences trace in part to Talmy's S-type versus V-type contrast. It does not support "frees the hand".
- Impacted axes: coverage (a worked example that contradicts its own decision rule is not usable knowledge) and calibration.
- Fix, paste-ready. Replace `which frees the hand from carrying the path` with `so, like Turkish and Japanese speakers, whose separate manner and path clauses come with more Trajectory Only and Manner Only gestures (S211; §6), a Vellmark speaker's hand draws the path on its own, apart from the manner`. Replace `§6 keeps path in the verb, so the accompanying hand is free to mark attitude instead of direction` with `§6 keeps path in the verb, so the hand draws the path alone, in true uphill or downhill bearings, never as one English-style sweep blending path and manner`.

### F3 — medium: the worked example's pointing choice is credited to a source that does not carry it

- Entry line 181 (§11, §4 step) says "a finger-free point suits a people whose bearings are never relative (S203)".
- Source: S203 (Enfield 2001) is about the form, focus restriction and register of lip-pointing in Laos. Its registry row, at the anchors pp. 186–207, does not link lip-pointing to absolute frames. The entry's own absolute-frame evidence points with the hand: S187, p. 12, "If one is talking about going to the beach and the beach is east, one points east" (entry line 84).
- Fix, paste-ready. Replace `so a finger-free point suits a people whose bearings are never relative (S203)` with `a design choice (**H**): the absolute frame does not require it, since Guugu Yimithirr speakers point with the hand in true bearings (S187)`.

### F4 — medium: the worked example produces one of the five artifacts the build order promises

- Entry lines 165–169 (§10 build order) name five artifacts. Step 3, line 167, says "every gesture glossed, the domain it covers, and the sanction behind each taboo".
- §11's only output (lines 183–187) is a three-row table with two columns, gesture and gloss: no domain, no sanction, and no pointing-and-gaze, gradient or acquisition sheet. Line 181 sets a taboo on "the promise gesture", but no row is glossed as a promise. All the rest of the worked example is the one 382-word paragraph on line 181. That is the essay form criterion 4 rules out, in the one place a worldbuilder copies from.
- Impacted axis: coverage (usability).
- Fix, paste-ready: split line 181 into one bullet per §10 step, keeping its sentences, and replace the table with:

```markdown
| Vellmark gesture (invented) | Gloss (English) | Domain | Who may use it, and the sanction |
|---|---|---|---|
| palm turned up, held out flat | "give it to me" | exchange | anyone, to an equal or a junior (design frame, **H**) |
| index finger to the lips, then to the listener | "I say this to you only" | secrecy | adults (design frame, **H**) |
| closed fist at the shoulder, twice | "I swear it" — the promise gesture of the §8 taboo | oath | never toward an elder; the sanction is social, not legal (`politeness-taboo-euphemism.md:76`) |
```

### F5 — medium: DR-GES-04 cites S223 for a taboo it does not report

- Entry line 176 (DR-GES-04 trigger): "the culture forbids pointing at people, at the dead, or with one hand (S223)".
- Source: S223, printed p. 700: "taboos against left hand pointing, index-finger pointing, or pointing at people". The opened PDF has no "dead", "corpse" or "grave". Its p. 708 adds the rainbow, not the dead.
- Fix, paste-ready: `the culture forbids pointing at people, with the index finger, or with the left hand (S223, p. 700)`.

### F6 — medium: the entry restates the emblem owner it says it cites one way

- Line 116 (§7, "Yes and no that differ") and line 197 (§12, "Nodding means yes everywhere") both restate the Bulgarian nod inversion that base `adornment-body-codes.md:92` already carries ("nod/shake inversion reported from Bulgaria"). That is two copies of one owned fact.
- Line 198 (§12, thumbs-up) restates Morris et al. 1979 emblem geography ("an offensive gesture in Sardinia (Italy) and some parts of Greece", S234 "as that paper reports from Morris et al. 1979"). Base `adornment-body-codes.md:79` owns this ("Morris et al. (1979) mapped emblem geography across Europe"), and the entry's own §2 (line 34) says "the emblem geography … stay there".
- Claim C's falsifier explicitly includes "the entry restates a partial owner's register instead of citing it one-way".
- Fix, paste-ready.
  - Line 116 becomes: `- **Yes and no that differ**: the head-movement inversion is a body-code collision owned at \`../culture-material/adornment-body-codes.md:92\`; this entry adds only the opened study and its calibration row (§12, S219, S233).`
  - Line 198: delete `the “thumbs-up” gesture is “an offensive gesture in Sardinia (Italy) and some parts of Greece” (S234, as that paper reports from Morris et al. 1979),` and keep the S189 clauses.

### F7 — low: authoring-process wording left in a corpus entry

- Line 138: "the article's publisher abstract is already drafted by ScribeSec04Pointing" names a private seat.
- Line 7: "the integrator assigns the row ids at integration and every id the entry then cites is at or above the round-53 floor".
- Line 10: "Not claimed: … the assigned `S###` ids … this seat measured only the pre-entry state" is stale after landing.
- Lines 7, 9, 11 and 213 list only S187–S190 as the entry's sources, although the body cites S191–S238.
- Line 214 tells the reader to re-open "the community or UNESCO page", wording carried over from the speech-surrogates template, where UNESCO was relevant.
- Fix, paste-ready.
  - Line 138: delete `, and the article's publisher abstract is already drafted by ScribeSec04Pointing`.
  - Line 7: replace the integrator clause with `rows S187–S238`.
  - Lines 9, 11 and 213: replace `(S187, S188, S189)` and the four-row list with `S187–S238`.
  - Line 10: replace the "Not claimed" sentence with `post-entry counts 229 and 28 (README sweep and accept-c.py at landing, \`47ec825\`)`.
  - Line 214: replace `community or UNESCO page` with `community's own published page`.

## Strongest case against C, and why it fails

The strongest counterexample is that a gesture register already existed at the base. Adornment's H1 says "Gesture and Posture", its §7 calls emblems "the conlang-adjacent category", and the predecessor entry explicitly ceded gesture to adornment. The new entry's own topic claims "quotable gestures" and "emblem repertoires", which are the same category (S230, p. 2).

That ownership covers only the emblem, posture and proxemics part. Adornment §7 has 17 lines, all about etiquette gradients and emblem collisions. On the rest the base corpus is empty: co-speech gesture types, pointing forms and their communities (Yupno, Lao, Arrernte, Ghana), framing effects on gesture (Kita and Özyürek; Özyürek et al.), gesture time lines (Yupno, the English and Hebrew script direction), and acquisition and second-language transfer. The term sweeps above found no base hits for any of them. Roughly §1, §3 (all rows but the emblem row), §4, §5, §6, §8 and §9 are new ground. The emblem overlap is limited to §7, two rows of §12 and §10 build step 4.

So C is a learning claim, provided F1 narrows the gap statement to the ground the base did not hold.

## Would a non-author closure call the expansion "improved"?

Most likely yes, for coverage. The count, sweep and S-id legs are mechanical, and the same claim shape was called improved in rounds 51 and 52. The risks are F2 (a worked example whose central rule contradicts the entry's own §6) and F6 (restatement, which is a named falsifier clause). Land F2 and F6, plus F1 to narrow the gap statement, before the closure reads the entry.

The verdict should also say that "learning claim on uncovered ground" was established by review only, because `accept-c.py` does not test it (see Checks run).

Impacted axes: coverage (F1, F2, F4, F6), calibration (F2, F3, F5), and operability of the entry as a worldbuilding tool (F4).
