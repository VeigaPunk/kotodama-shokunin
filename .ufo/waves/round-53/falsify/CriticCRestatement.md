# CriticCRestatement — round 53 falsify, claim C (restatement and wrong ownership)

Item attacked: `corpus/knowledge/linguistics/gesture-co-speech-pointing.md` as landed at `47ec825f11543b5ba457e21772d587b3f529e756` (lane HEAD at review time), and the 52 rows S187–S238 in `corpus/SOURCES.md` as far as they bear on duplicated authority. Claim C's falsifier includes "a non-author review finding that the entry restates a partial owner's register instead of citing it one-way".

Verdict: **the falsifier fires.** The entry restates or re-claims ground owned elsewhere in eight places, and the boundary table in section 2 contradicts the body in several of them. One source work is registered twice (S219 and S233), against the statement that the integrator merged duplicate works. PROVINCE drift is small: there is no clinical material and no animation material, but there is one neuroscience verdict row and some developmental age figures written as if they were norms.

No tools were installed.

## Checks run

- Read the whole entry (lines 1–222). Read the partial owners: `culture-material/adornment-body-codes.md:77-93`, `linguistics/sign-languages-manual-modality.md:55-70` and `:155-165`, `linguistics/numerals-and-measures.md:100-112`, `myth-symbol/direction-symbolism.md:1-12`, `:30-45` and `:88-102`, `linguistics/semantics-pragmatics.md:110-122`, `linguistics/politeness-taboo-euphemism.md:70-80`, and `PROVINCE.md`.
- Read every other in-corpus anchor that section 2 names, one line each: `linguistics/linguistic-anthropology.md:147` and `:49`, `myth-symbol/binding-speech-complex.md:108` and `:127`, `civilizations/rome.md:43`, `civilizations/byzantium.md:75`, `synthesis/symbol-lexicon-colexification.md:141`, `linguistics/conlang-methodology.md:76` and `:82`, `verification/calibration-registry.md:38`, `politeness-taboo-euphemism.md:77` and `:101`.
- Used `rg -n` on the entry to find every line that cites `numerals-and-measures.md:107`, `rome.md`, `byzantium.md`, `symbol-lexicon`, `linguistic-anthropology.md`, `binding-speech`, `direction-symbolism.md:99`, and S187–S190, and every line mentioning Bulgaria, Ghana, Morris, Ekman/Efron, and the clinical, neuroscience, age and animation terms.
- Extracted the DOI from each row S187–S238 in `corpus/SOURCES.md` and listed duplicates. Only `10.1007/s10339-012-0472-x` repeats. Read both rows, then grepped `.ufo/waves/round-53/integration-map.json` for both ids.
- No external source was re-opened. This review is about ownership inside the corpus, and every finding rests on corpus bytes.

## Findings

### F1 — medium: the build order requires a posture-and-distance gradient table, which the entry says another entry owns

- Entry `:168`: "4. Set the posture and distance gradients by rank and setting … *Artifact: posture-and-distance gradient table.*" Entry `:161` asks for "posture, distance and gesture size scaled by rank".
- Owner: `adornment-body-codes.md:80` (posture gradients are "honorific grammar") and `:83-91` (the gradient table); `:79` has Hall's proxemic bands. The entry itself hands this ground off at `:12`: "The emblem taxonomy, posture gradients and proxemic bands stay with `../culture-material/adornment-body-codes.md`".
- Fix (paste over step 4 at `:168`): `4. Set gesture rate, size and space by status pair and setting (§8); take the posture and distance gradients from `../culture-material/adornment-body-codes.md:80-91` one-way and add only the gesture-size column. *Artifact: gesture-size column keyed to the body-code gradient table.*` At `:161`, change "posture, distance and gesture size scaled by rank" to "gesture size and rate scaled by rank (posture and distance from `../culture-material/adornment-body-codes.md:82`)".

### F2 — medium: the boundary and decision rows claim the taboo sanction ("who enforces", "the institution that backs"), which the politeness entry owns

- Entry `:40`, section 2 row: "the sanction machinery stays there; this entry marks only which gestures a culture bans and who enforces the ban". Entry `:160`: "a taboo list and the institution that backs each taboo". Entry `:167`: "the sanction behind each taboo". Entry `:133`: "what the sanction is".
- Owner: `politeness-taboo-euphemism.md:76`: "Sanction gradient — a culture exposes which institution backs each taboo". "Who enforces the ban" is exactly this gradient, so the row that hands the ground off also takes it back.
- Fix: at `:40` replace "and who enforces the ban (§8)" with "; which institution backs each ban is read off the gradient at `politeness-taboo-euphemism.md:76` (§8)". At `:160` replace "and the institution that backs each taboo" with "each taboo placed on the sanction gradient at `politeness-taboo-euphemism.md:76`". At `:167` replace "and the sanction behind each taboo" with "and each taboo's rung on the `politeness-taboo-euphemism.md:76` gradient". At `:133` replace "and what the sanction is" with "and which rung of `politeness-taboo-euphemism.md:76` backs it".

### F3 — medium: the left-right polarity rule is restated, and its owner is missing from the boundary table

- Entry `:132`: "write the polarity as an institution: which hand gives, points, eats, receives and swears (`../myth-symbol/direction-symbolism.md:99`)". Entry `:135`: "decide the bodily act of the oath (which hand, which object) in the same design pass as the hand polarity".
- Owner: `direction-symbolism.md:99`: "Decide the culture's polarity, then **give it institutions**: which hand takes oaths, eats, gives and receives, salutes". Rule D2 at `:29` says the same thing. The entry copies the owner's rule almost word for word and adds only "points". Left-right polarity has no row in the section 2 one-owner table (`:32-44`), and it is missing from the partial-owner lists at `:4` and `:8` and from the scope at `:12` and `:219`. It is the only owner of claimed ground that is unlisted.
- Fix: add a row to section 2: ``| `../myth-symbol/direction-symbolism.md:92-101` | the left/right body axis: Hertz's polarity, its counterexamples, and the rule that a polarity needs institutions (which hand swears, eats, gives, receives) | the polarity and its institutions stay there; this entry adds only the pointing hand and the substitute forms a handedness taboo forces (§4, §8) |``. Replace the consequence at `:132` with: `take the culture's hand polarity and its institutions from `../myth-symbol/direction-symbolism.md:99` one-way, add the pointing hand, then design the substitute forms the taboo forces — the reported respect position and the bi-manual or right-hand forms (S220, p. 62) (design frame, **H**)`.

### F4 — medium: section 2 hands off the "category names", but section 3 defines the emblem category and gives its glosses

- Entry `:34`: "the category names, the emblem geography, the proxemic bands and the etiquette script stay there". Entry `:56` then defines Emblem ("conventionalized body movements, which have fixed meanings", S197) and gives glosses: "‘A thumbs up for “good”’ (S198, Table 3)". The "Interactive" row at `:57` covers the ground of Ekman–Friesen's *regulators*.
- Owner: `adornment-body-codes.md:79`, Ekman & Friesen (1969): "*emblems* (culture-specific gestures with dictionary meanings …), illustrators, affect displays, regulators, adaptors".
- The unqualified "thumbs up for good" gloss at `:56` also contradicts the entry's own `:198` (offensive in Sardinia and parts of Greece).
- Fix: at `:34` replace "the category names, the emblem geography" with "Ekman–Friesen's five-way taxonomy and its emblem lexicon, the emblem geography". At `:56` drop the "‘A thumbs up for “good”’ (S198, Table 3)" example, or add "— a gloss local to the sampled speakers; see §12".

### F5 — medium: the emblem-geography claims the entry handed off are restated in sections 7 and 12, and the same paper is cited under two row ids

- Bulgarian yes/no inversion: entry `:116` (S219) and `:197` (S233). Owner: `adornment-body-codes.md:92`: "nod/shake inversion reported from Bulgaria, drifting by generation". The claim is stated twice in the new entry, under two different S-ids.
- Thumbs-up geography: entry `:198`: the thumbs-up is "an offensive gesture in Sardinia (Italy) and some parts of Greece" (S234, from Morris et al. 1979). Owner: `adornment-body-codes.md:79`: "Morris et al. (1979) mapped emblem geography across Europe". Section 2 (`:34`) says "the emblem geography … stay there".
- Duplicate rows: `SOURCES.md:248` S219 and `SOURCES.md:262` S233 are both Andonova & Taylor 2012, "Nodding in dis/agreement", doi 10.1007/s10339-012-0472-x. `integration-map.json:44` maps `"NEW-ScribeSec07Quotable-5": "S219"` and `:70` maps `"NEW-ScribeSec12Calibration-4": "S233"`. This contradicts the statement that the integrator merged duplicate works. It is the only DOI that repeats in S187–S238.
- Fix: merge S233 into S219 (keep S219, add the PubMed access route as a second URL, retire S233 with a "merged into S219" note in the lane's existing supersede style), and cite S219 at `:197`. Cut `:116` to: `- **Yes and no that differ**: the Bulgarian inversion and its generational drift are `../culture-material/adornment-body-codes.md:92`; this section records only that a repertoire must state its head-yes and head-no forms (S219).` In the `:198` row, keep the S189 lines and replace the Sardinia/Greece clause with "the regional collisions Morris et al. mapped are owned at `../culture-material/adornment-body-codes.md:79`".

### F6 — medium: the couples line claims counting gestures; section 2 disclaims them and says it "cites that row once"

- Entry `:8`: "`numerals-and-measures.md` (owns finger counting, `:107`; this entry owns the gesture a counting system may ride on)". Entry `:36`: "counting gestures stay there; this entry cites that row once … and owns no numeral or counting system".
- Owner: `numerals-and-measures.md:107`: "A fictional counting gesture system should be specified like any other body code." The gesture a counting system rides on *is* that counting gesture system.
- "Cites that row once" is false: `rg` finds `numerals-and-measures.md:107` on entry lines 4, 6, 24, 36, 56, 78, 116, 139, 152 and 212.
- Fix: at `:8` replace "this entry owns the gesture a counting system may ride on" with "this entry owns only a number shown with the hands while it is said aloud (§1); the counting gesture system stays there". At `:36` replace "this entry cites that row once, for counting-as-body-code, and owns no numeral or counting system" with "this entry points to that row and owns no numeral or counting system".

### F7 — medium: section 2 gives direction-symbolism the gesture-anchoring evidence, then sections 4, 5 and 9 build on it as the entry's own ground

- Entry `:37`, the "What it owns" cell for `direction-symbolism.md:36`: "the absolute frame, with the field evidence that some speakers anchor their gestures to the world rather than to the body". Entry `:84` then states that evidence as its own row (S187, S206).
- `direction-symbolism.md:36` carries a single clause: "gestures are anchored to the world, not the body (Haviland 1993, 1998; Levinson 1997)". Pointing is the new entry's ground, so the error is in the section 2 cell, not in `:84`.
- Fix (`:37`, "What it owns" cell): `the absolute frame and its grammar; it mentions in one clause that Guugu Yimithirr gestures are world-anchored (Haviland 1993)`. Boundary cell: `frames of reference and the direction register stay there; the pointing evidence itself (S187, S206, S207) is this entry's (§5)`.

### F8 — low: two owners are named for frames of reference

- Entry `:8` names `semantics-pragmatics.md` as owning "deixis and frames of reference in grammar, `:115-120`" and `direction-symbolism.md` as owning "frames of reference and the direction register". Entry `:12` and `:219` give frames of reference to direction-symbolism only. Both owners do carry Levinson 2003 (`semantics-pragmatics.md:117`, `direction-symbolism.md:32-36`), so the corpus already has a split. The entry should state that split one way rather than name two owners.
- Fix: at `:12` and `:219` change "frames of reference, cardinal directions and the frame table stay with `../myth-symbol/direction-symbolism.md`" to "frames of reference as a symbolic register, cardinal directions and the frame table stay with `../myth-symbol/direction-symbolism.md`; frames of reference in deictic grammar stay with `semantics-pragmatics.md:117`".

### F9 — low: section 2 rows name owners the body never cites

- Entry `:43` (rome.md:43, "cites it once, as a trained-gesture example"), `:44` (byzantium.md:75, "cites it once … (§8)") and `:42` (symbol-lexicon-colexification.md:141, "(§7)") appear only in section 2: `rg` finds no other line citing them. `:39` (linguistic-anthropology.md:147, "(§6)") is likewise cited only in section 2; the other linguistic-anthropology citation, at `:93`, is to `:49`. `:41` points binding-speech to "(§7)", but the only body citation is in §8 at `:135`.
- These rows describe uses that do not exist, which pads the one-owner table and gives false provenance for sections 6, 7 and 8.
- Fix: delete rows `:42`, `:43`, `:44` and `:39`, or add the use each one promises. Change "(§7)" to "(§8)" at `:41`.

### F10 — low: integration residue and head under-reporting in corpus text

- `:138`: "the article's publisher abstract is already drafted by ScribeSec04Pointing". This is a private seat id in a corpus entry. Fix: delete the clause, or replace it with "(S205 carries the publisher's catalogue record)".
- `:7`: "the integrator assigns the row ids at integration and every id the entry then cites is at or above the round-53 floor". `:10`: "Not claimed: … the assigned `S###` ids". Both are pre-integration seat text, now stale. Fix: replace them with "external rows S187–S238, registered this round".
- `:7`, `:9` and `:13` list only S187–S190 as the external shelf, but the body cites up to S238. `:7` names S188 as "the pointing survey and the taboos it reports", yet S188 is cited only in the head and the recheck table (lines 7, 9, 11, 213). The body's taboo claims rest on S202, S205, S220–S224, not on S188. Fix: name the S187–S238 range, and either cite S188 where its content is used or drop the "and the taboos it reports" attribution.
- `:214`: "the community or UNESCO page itself … no such page was opened this round". No UNESCO material exists in this entry; the text appears carried over from another entry. Fix: replace "the community or UNESCO page itself" with "the cited row's page itself".

### F11 — low: the Aymara temporal claim and its calibration also sit in the semantics entry

- Entry `:87` and `:201` restate the Aymara past-front, future-behind finding, citing S208 (Núñez & Sweetser 2006). `semantics-pragmatics.md:118` already carries it from the same paper, with the owner's caution "Treat as flavor, not cognition-forcing". The entry does point there one-way, and the gesture data is legitimately its own, so this is only a mild double verdict.
- Fix: at `:201` append "consistent with the owner's caution at `semantics-pragmatics.md:118`".

## PROVINCE fit

`PROVINCE.md` owns linguistic-cultural worldbuilding method. Its refusals list canon, rights rulings, game mechanics, general source-research method, publishing and prompt craft.

- **Animation:** none. The only mention is the handoff at `:12` and `:219` ("gesture animation in a game to the game-dev lanes"). No defect found.
- **Clinical:** none in substance. `:204` and `:220` disclaim clinical rulings. The only clinical word is inside the S238 quote at `:202` ("patient, brain-stimulation, and brain-imaging studies"). No defect found.
- **Neuroscience — low to medium, drift:** `:202` gives "Mirror neurons explain gesture" a **C** status. That is a verdict on a neuroscience mechanism, built from a cognitive-neuroscience review (S238), and it is outside the lane's ground. Fix: replace the row with `| A gesture needs a neural explanation | out of lane | ground a gesture in a community's habit and who teaches it (§9); this lane grades no neural mechanism. Typical failure: a gesture justified by neuroscience instead of by a community's habit |`, and drop S238 from the used-by cell, or retire the row.
- **Developmental norms — medium, drift:** `:147` ("preverbal pointing, around 12 months"; "by 10–14 months"), `:148` ("a gesture for an object '3.0 months' on average before the word"), `:169` ("infants point before they speak in every culture tested") and `:177` ("infants under a year are said to be exempt from pointing rules, untested"). These read as developmental milestones. Three problems:
  - `:169` turns seven sampled sites into "every culture tested" with no bound.
  - `:177`'s "said to be exempt" has no source.
  - The design column needs only the *order* (point, then word, then two words).

  Fix: in the first column at `:147` and `:148`, replace the month figures with the order ("preverbal pointing", "gesture before the word"). Keep the ages only inside the quoted source cells, followed by "(sampled sites and ages, not a norm)". At `:169` write "in all seven sites S223 sampled". At `:177` delete "infants under a year are said to be exempt from pointing rules, untested (to-verify)".
- **Scope promise:** `:12` and `:218` say the entry covers how gesture is "learned and lost". Section 9 has no loss material, and loss is where clinical drift (aphasia) would enter. Fix: change it to "learned and carried across languages".

## Summary for the judge

The falsifier for claim C fires. The four sharpest restatements are F1, F2, F3 and F5: the posture gradients, the taboo sanction, the left-right polarity rule, and the emblem geography. In each, the entry hands the register off in section 2 or in its scope and then states it again in the body. F5 also shows that the integration map did not merge one duplicate work (S219 = S233). Every fix above is a wording change or a row merge, so none of them breaks the 229-file count. The S219/S233 merge does change the cited-id set that `accept-c.py` checks, so the integrator should re-run `python3 -B reports/round-53/accept-c.py` after merging.
