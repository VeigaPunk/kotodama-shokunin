# Scout — claim C gap premise (co-speech gesture / pointing)

Assigned item: re-run claim C's `gap_evidence_at_base` sweeps at the lane worktree, enumerate every
`corpus/knowledge` line in the gesture term family, and deliver an ownership verdict plus the
one-way citation list. Author-lane advice only; nothing here is admission, and no file outside this
report was written.

Worktree: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, HEAD `60f1d2a3d832b926e37f82b11c67496d131a1431`
(declaration commit on base `a9cf95fe47a82b516f6c2487cb76b89c3a71c493`); `git status --porcelain`
shows only the untracked `.ufo/waves/round-53/`. All line numbers below were read at that worktree.
No LSP server answers Markdown here, so the enumeration is literal `grep`/`awk` — recorded as such;
no semantic-proof claim is made from it.

## 1. Gap sweeps, re-run as declared

| Sweep (exact) | Output |
|---|---|
| `find corpus/knowledge -iname '*gestur*' -o -iname '*pointing*' -o -iname '*kinesic*'` | **0 files** |
| `grep -rliE '^- topic:.*(gestur\|pointing\|kinesic)' corpus/knowledge` | **0 files** |
| `find corpus/knowledge -name '*.md' \| wc -l` | **228** |
| `ls corpus/knowledge/linguistics/*.md \| wc -l` | **27** |

Widened sweeps (mine, so the premise is not an artefact of a narrow pattern):

| Widened sweep | Output |
|---|---|
| filename: add `*proxemic* *nonverbal* *posture* *emblem* *body*` | 2 files, both false positives: `culture-material/adornment-body-codes.md` and `culture-material/bathing-and-body-hygiene.md` (match on `*body*`) |
| topic line: `\b(gestur\w*\|kinesic\w*\|nonverbal\|non-verbal\|body language\|proxemic\w*\|posture\|pointing)` | 2 files, both on the single word **posture**: `culture-material/adornment-body-codes.md`, `culture-material/furniture-interior-lexicon.md`. Adding `sign language` brings in `linguistics/sign-languages-manual-modality.md` |
| H2 headings matching gesture/pointing/nonverbal/proxemic/posture | 2: `culture-material/adornment-body-codes.md:77`, `civilizations/siam-thai.md:129` (Khon performance, not a register owner) |
| `co-speech\|cospeech` corpus-wide | **1 line**, `linguistics/sign-languages-manual-modality.md:64` |
| `kinesic` corpus-wide | **1 line**, `sign-languages-manual-modality.md:4` (inside the sweep-command text of its own gap line, not a claim) |
| `beckon`, `lip[- ]point`, `head[- ]shake` | **0 lines** (`headshake` occurs only as a sign-language nonmanual: `sign-languages-manual-modality.md:91,:106`) |
| `mudra` | **0 lines**; the two `\bmudra` hits are the surname *Mudrak*: `civilizations/mongol.md:15,:96` |

So the declared premise holds and survives widening: **no filename owner, no topic-line owner, and no
H2 section owner of gesture or pointing anywhere in `corpus/knowledge`.**

## 2. Enumeration

Pattern `grep -rniE 'gestur[a-z]*|kinesic[a-z]*|\bbeckon[a-z]*|\bmudra[a-z]*|lip[- ]?point[a-z]*|head[- ]?shake[a-z]*|\bnod(ding|ded|s)?\b'`
returns 78 lines; drop 2 (*Mudrak*) → **76 lines in 39 files**. `pointing` returns 11 lines;
`emblem` returns **224 lines in 87 files**. Grouped below with what each file owns.

### 2a. The register / boundary cluster (the only lines that talk about gesture *as* a communicative system)

| Line | What the file owns |
|---|---|
| `linguistics/sign-languages-manual-modality.md:64` | the boundary row: `co-speech gesture (boundary)`, speakers alongside speech (S079), "picked up with the spoken language", "every speaker; no community boundary", "conveys information but is not conventionalized and systematic the way sign is (S087)" — **the only place in the corpus where co-speech gesture is named as a category** |
| `sign-languages-manual-modality.md:37` | boundary-table row: `adornment-body-codes.md:79` owns "gesture and posture as body codes: emblems with dictionary meanings, illustrators, proxemic bands"; "emblems and etiquette stay there" |
| `sign-languages-manual-modality.md:161` | "Sign is not gesture-code: emblems and proxemics stay at `adornment-body-codes.md:79`" |
| `sign-languages-manual-modality.md:25` | test failure "an emblem repertoire: fixed gestural glosses with dictionary meanings" |
| `sign-languages-manual-modality.md:29` | "how far spatial grammar is gestural is debated (S075, **C**)" — the gesture/seam line, owned here |
| `sign-languages-manual-modality.md:66` | "gesture, homesign and sign languages differ by conventionalization and systematicity (S087)" |
| `sign-languages-manual-modality.md:83` | "Sign phonology is not gesture choreography" |
| `sign-languages-manual-modality.md:112` | "hearing silent gesturers" in the iconicity study (S101) |
| `sign-languages-manual-modality.md:205` | calibration: "C for 'sign has gestural components'" |
| `culture-material/adornment-body-codes.md:79` | Ekman & Friesen (1969) emblems/illustrators/affect displays/regulators/adaptors; Morris et al. (1979) emblem geography; Hall (1966) proxemic bands; "these four labels are enough to script any fictional etiquette" |

### 2b. Deixis, frames of reference, pointing

| Line | What the file owns |
|---|---|
| `linguistics/semantics-pragmatics.md:113` | H2 §6 "Deixis: the anchored words" — the register owner of deixis |
| `semantics-pragmatics.md:115` | Bühler origo; Levinson 1983 taxonomy (person/spatial/temporal/discourse/social); Silverstein shifters |
| `semantics-pragmatics.md:117` | frames of reference (Levinson 2003); absolute frame with Guugu Yimithirr cardinal description |
| `semantics-pragmatics.md:118` | temporal deixis: Aymara past-in-front/future-behind (Núñez & Sweetser 2006); Mandarin vertical time (Boroditsky 2001 vs Chen 2007) |
| `semantics-pragmatics.md:119` | deictic projection (Fillmore 1997) |
| `semantics-pragmatics.md:135` | relativity calibration: "obligatory marking shapes habitual attention while speaking" (Slobin 1996; Lucy 1992; Gumperz & Levinson 1996) |
| `myth-symbol/direction-symbolism.md:6` | Haviland (1993) "Anchoring, iconicity, and orientation in Guugu Yimithirr pointing gestures" — the pointing citation on file |
| `direction-symbolism.md:28` | "describe where something is without pointing" as the frame test |
| `direction-symbolism.md:34-36` | intrinsic/relative/absolute rows; `:36` "gestures are anchored to the world, not the body (Haviland 1993, 1998; Levinson 1997)" |
| `linguistics/sign-languages-manual-modality.md:103` | "Referential loci and pointing": INDEX localizes a referent in signing space — pointing *inside* a signed language |
| `civilizations/israel-ancient-hebrew.md:116` | **false friend**: "Masoretic pointing" = vocalization diacritics, not a body act. A grep-based claim that "pointing is covered" would be wrong here |

### 2c. Etiquette, posture, oratory, politeness

| Line | What the file owns |
|---|---|
| `adornment-body-codes.md:1` | title includes "Gesture and Posture" |
| `adornment-body-codes.md:77` | H2 §7 "Gesture and posture — engineered gradients and their failure modes" |
| `adornment-body-codes.md:80` | bow degrees, Thai *wai*, Khmer *sampeah*, kowtow; "posture gradients are honorific grammar" |
| `adornment-body-codes.md:81` | *proskynesis*, Callisthenes, Macartney, Liutprand, *immixtio manuum* |
| `adornment-body-codes.md:82-91` | the gradient table (bow / wai / sampeah / kowtow / adoratio / homage) |
| `adornment-body-codes.md:92` | failure modes: *moutza* emblem collision, nod/shake inversion, Bede/Japanese finger counting, gaze and silence |
| `adornment-body-codes.md:93` | Barrett et al. (2019) on Ekman's universals; Juvenal *verso pollice* as unrecoverable gesture evidence |
| `civilizations/byzantium.md:75` | *proskynēsis*: "gesture alone does not identify worship" |
| `civilizations/byzantium.md:178` | "define image, recipient, permitted gesture, and competent authority" |
| `civilizations/rome.md:43`, `:112` | Quintilian *actio*: tunic, stripe, folds, gesture and speech progress (11.3.137–149) |
| `civilizations/siam-thai.md:114`, `:129`, `:135` | Khon costume/gesture/voice as a performance register |
| `culture-material/furniture-interior-lexicon.md:53`, `:113` | posture (sitting, servant posture) as interior-design consequence |
| `linguistics/linguistic-anthropology.md:147` | "registers license dress and gesture (oath regalia, mourning-silence garb, initiate masks)" |

### 2d. Ritual/iconographic mentions (gesture as a depicted or prescribed detail, no register claim)

`civilizations/` one or two lines each, all in the same shape — a scene or object check that lists
gesture among the co-present channels: `aegean-minoan-mycenaean.md:117` (trees/pillars/gestures on
seals); `amazonia-tupi-guarani.md:81,:173` (institutional gestures); `anatolia-hittite.md:126`
(protective embrace is "not a private portrait of an everyday interpersonal gesture");
`australia-aboriginal.md:58` (song, speech, gesture not interchangeable containers);
`egypt-ancient.md:147` (titulary, deity, costume, gesture jointly identify the scene);
`finnic-sami.md:85` (referent recognized through melody/word/voice/gesture); `germanic-norse.md:154`
(complete contents/gestures not recoverable); `greece-classical.md:120` (clothing, carried objects
and gesture work as a bundle); `igbo.md:81` (vocatives, repetition, gesture, response);
`india-mughal.md:160,:181` (dress, gesture, political speech in one scene model);
`india-vedic.md:74,:135,:175` (mantra couples wording with gesture; "constrained gesture/speech");
`israel-ancient-hebrew.md:109,:117` (gesture rules distinguish setting; name-magic matrix includes
gesture); `japan-edo.md:122` (read gestures as part of the sheet); `java-majapahit.md:112`
(posture/eyes/voice/dress/gesture as converging codes); `khmer-angkor.md:34` (relief gesture);
`maori.md:123` (performance grid includes gesture); `persia-achaemenid.md:134` (controlled gesture in
court relief); `thrace-dacia.md:111,:158` (feast sequence includes gesture);
`hawaii.md:130,:154` ("a universal hand-gesture dictionary is inferred where lineage/context is
needed"; gestures not established).

### 2e. Lexical, metaphorical, or phonetic uses (not gestures at all — do not count as coverage)

`synthesis/multi-culture-creole-workshop.md:24` ("repair by gesture" in jargon formation);
`synthesis/taboo-euphemism-lifecycle.md:186` ("removed emblem, altered oath gesture");
`synthesis/symbol-lexicon-colexification.md:35,:141` ("oath gesture");
`synthesis/religion-language-co-evolution.md:114,:159` (gesture as one component of a rite);
`synthesis/deity-name-derivation-pipeline.md:167` (matched on unrelated morphology);
`myth-symbol/flood-traditions.md:97` ("Landing gesture" — a narrative landing);
`linguistics/sound-symbolism.md:29` (the *mouth* gesture of articulation);
`culture-material/material-culture-inference-method.md:7` (Leroi-Gourhan, *Gesture and Speech*, a book
title); `culture-material/architecture-settlement-lexicon.md:40,:141` (gasshō-zukuri "joined-hands";
"name roofs from gesture, animal, or body"); `culture-material/dress-through-eras.md:105` (idiom).

### 2f. `emblem`, 224 lines in 87 files — measured sense split

`emblem` is polysemous in this corpus and is **not** evidence about gesture:

- **5 lines use the Ekman–Friesen (gestural) sense**: `adornment-body-codes.md:79`;
  `sign-languages-manual-modality.md:25,:37,:64,:161`. All five are boundary statements.
- 51 lines carry heraldic/visual co-text (royal, dynasty, motif, seal, banner, badge, insignia,
  regalia, coat of arms); 167 carry neither gesture nor heraldic co-text and are visual/symbolic in
  the corpus's dominant usage (e.g. `civilizations/akan.md:87-91` adinkra names,
  `civilizations/fon-dahomey.md:118-148` palace emblems, `civilizations/zimbabwe-shona.md` 13 lines,
  `civilizations/egypt-ancient.md:94-96` ankh/djed/wedjat sign-values).
- Top emblem files: `civilizations/zimbabwe-shona.md` 13, `civilizations/fon-dahomey.md` 12,
  `linguistics/sign-languages-manual-modality.md` 7 (all boundary), `verification/*` 6 each.

No `emblem` line anywhere claims a register of quotable gesture; the emblem *taxonomy* exists only at
`adornment-body-codes.md:79` and the emblem *geography* only at `:79` (Morris et al. 1979).

## 3. Verdict

**Is there a current owner of co-speech gesture or pointing as a register? No.**

- **Co-speech gesture**: exactly one line names it (`sign-languages-manual-modality.md:64`) and that
  line explicitly *disclaims* it — it is a boundary row in a table whose subject is sign languages,
  with "every speaker; no community boundary" as its design consequence. No gap line, no topic line,
  no section, and no source row in `corpus/SOURCES.md` is dedicated to it: the registry's
  gesture-adjacent rows (S075, S079, S081, S101, S124) all sit under the sign-languages entry.
- **Pointing**: no owner. It appears (i) inside a signed language as INDEX (`sign-lang:103`),
  (ii) as a citation title and as a frame consequence (`direction-symbolism.md:6`, `:28`, `:36`),
  (iii) as the plain-language gloss of a frame test (`semantics-pragmatics.md:117` mentions absolute
  description, not pointing). No line treats pointing itself — index finger, chin point, lip point,
  gaze point, whole-hand point — as a system with conventions, addressees, or sanctions.
- **The nearest thing to an owner is `adornment-body-codes.md` §7 (`:77-93`)**, which owns *body code
  and etiquette*: the Ekman–Friesen category names, emblem geography, proxemic bands, honorific
  posture gradients, and the emblem/nod-shake/finger-counting failure cases. That is the emblem and
  etiquette slice. It states no claim that gesture co-occurs with and is part of speech, says nothing
  about pointing, frames, or time lines, and its own framing is "script any fictional etiquette".
- The register-level owners of the *adjacent* systems are `semantics-pragmatics.md` §6 for deixis,
  frames of reference and temporal deixis, and `direction-symbolism.md` §2 for the frame typology.
  Between them they own everything C's planned §5 would otherwise be tempted to say.

So claim C's coverage premise is sound: the ground is uncovered, and it is uncovered *next to* two
files that own its two hardest sub-topics.

## 4. Partial owners C must cite one-way (never restate)

Ordered by restatement risk. The brief listed the first four; **the fifth is a scout addition and is
the highest risk of the set.**

| # | Anchor | What it owns | C must not restate |
|---|---|---|---|
| 1 | `culture-material/adornment-body-codes.md:77-93` | emblems/illustrators/regulators/adaptors (Ekman & Friesen 1969), emblem geography (Morris et al. 1979), proxemic bands (Hall 1966), bow/wai/sampeah/kowtow/*adoratio*/homage gradients, *moutza*, nod/shake inversion, finger counting, Barrett et al. 2019 critique, Juvenal *verso pollice* | the category names as a taxonomy; any gradient table; the *moutza* and nod/shake cases; the finger-counting cases; the Ekman-universals critique; the *verso pollice* lesson |
| 2 | `linguistics/semantics-pragmatics.md:113-121`, `:135` | deixis taxonomy and origo, frames of reference (Levinson 2003), **temporal deixis including Aymara past-in-front and Mandarin vertical time**, deictic projection, the relativity calibration | any frame typology restatement; the Aymara/Mandarin time result as a finding; the relativity calibration sentence |
| 3 | `myth-symbol/direction-symbolism.md:6,:28,:34-36` | the frame-of-reference test, Guugu Yimithirr absolute frame, the Haviland 1993/1998 + Levinson 1997 citation chain, "gestures anchored to the world, not the body" | the frame typology; the Guugu Yimithirr evidence as a direction-register result; the "without pointing" test |
| 4 | `linguistics/sign-languages-manual-modality.md:64,:161` (with `:25,:29,:37,:66,:83,:91,:103,:106,:112,:205`) | co-speech gesture as the *boundary* row of the manual modality; sign-vs-gesture by conventionalization and systematicity; INDEX/pointing inside a signed language; nonmanual negation; "how far spatial grammar is gestural is debated (C)" | the sign/gesture boundary argument; the conventionalization-and-systematicity test; sign-space pointing as if it were everyday pointing; the S075 debate as a finding |
| 5 | **scout addition** `linguistics/semantics-pragmatics.md:118` (same file as #2 but a distinct claim) | Aymara "known past in front, unknown future behind" (Núñez & Sweetser 2006) and Mandarin vertical time (Boroditsky 2001 vs Chen 2007) | the time-line result itself. C's §5 may only own the *gesture-production* side: who points where while speaking, whether the axis is body-anchored or field-anchored, what a hearer reads off it — and must cite `semantics-pragmatics.md:118` for the deixis claim. Núñez & Sweetser's evidence *is* gesture data, so the seam is genuinely narrow |
| 6 | `linguistics/numerals-and-measures.md:107` | finger counting as culturally patterned counting technology (direction, start finger, thumb as counter or folder) | any counting-gesture content, including "same gesture different meaning" |
| 7 | `linguistics/linguistic-anthropology.md:147` | "registers license dress and gesture" — the register/costume coupling | the coupling claim itself; cite it and add only what is gesture-specific |
| 8 | `culture-material/architecture-settlement-lexicon.md:40,:141` | gesture-named architecture (gasshō "joined-hands"), "name roofs from gesture, animal, or body" | the body-lexicon-to-craft-lexicon naming lever |
| 9 | `civilizations/byzantium.md:75` | *proskynēsis*: "gesture alone does not identify worship" | the point that a posture is ambiguous without institution. Good one-way citation for C §8 |
| 10 | `civilizations/rome.md:43,:112` | Quintilian *actio* — trained gesture as elite self-presentation | the oratorical-gesture set as a design option; cite and move on |

Also worth a boundary row although not an owner of gesture: `culture-material/material-culture-inference-method.md:7`
(Leroi-Gourhan, *Gesture and Speech*) and `linguistics/politeness-taboo-euphemism.md:55-58` (honorific
systems as grammar — nearest neighbour to C §8's politeness content).

## 5. Lines the C entry would restate — flags

Ranked by how easy the slip is. Each is a plausible sentence in the planned sections.

1. **`adornment-body-codes.md:77-93` (planned §3, §7, §8).** The whole of planned §3 ("gesture types
   and what each carries") is the Ekman–Friesen list at `:79`; planned §7 ("quotable gestures and
   emblem repertoires") is `:79` + `:92`; planned §8 ("taboos, politeness, hand and status") is
   `:80-91`. **If C re-tabulates emblems/illustrators/regulators/adaptors, or re-lists bow/wai/
   kowtow, it restates this file and fails its own falsifier.** C's defensible new ground in §3 is
   the *co-speech* consequence: which categories co-occur with speech, what each contributes to the
   utterance, and how a conlanger encodes them in a lexicon of gesture — not the taxonomy itself.
2. **`semantics-pragmatics.md:118` (planned §5).** "Gesture in space and time (frames of reference,
   time lines)" names exactly what `:117-118` owns. C's §5 must cite both lines and restrict itself
   to the bodily realization: pointing axis, body-anchored vs field-anchored time, the gesture
   evidence that the *time* claim rests on, and what a worldbuilder writes into a scene. Restating
   Aymara/Mandarin as C's own finding is the clean falsifier hit.
3. **`direction-symbolism.md:34-36` (planned §5).** Any intrinsic/relative/absolute table is owned
   there; C must not reproduce the three-row typology or the Guugu Yimithirr compass-maintenance
   point. Cite `:36` for "gestures anchored to the world, not the body" and build only the gesture
   register on top.
4. **`sign-languages-manual-modality.md:64,:66` (planned §1, §2).** C's §1 "gesture is part of the
   utterance" must not become "gesture is a language" or re-run the conventionalization/systematicity
   comparison — that comparison is sign-language §3's boundary row. Quote it one-way, then take the
   other side of the seam: co-speech gesture is systematic without being a community language.
5. **`sign-languages-manual-modality.md:103` (planned §4).** INDEX/pointing in signing space is a
   signed-language fact. C's §4 must not absorb it: cite `:103` and keep everyday pointing
   (index/chin/lip/gaze/whole-hand, pointing at persons and its taboos) as C's ground.
6. **`numerals-and-measures.md:107` (planned §3 or §6).** Any "counting gestures differ by culture"
   sentence is that file's. Cite it; do not give examples.
7. **`linguistic-anthropology.md:147` (planned §2 or §8).** "Registers license dress and gesture" is
   a one-line coupling C should cite rather than paraphrase.
8. **`architecture-settlement-lexicon.md:141` (planned §6, "language shapes gesture" — the reverse
   direction).** The gasshō case is *gesture shaping lexicon*, owned there. C §6 is the other arrow
   (what a language packages, its speakers' hands follow); do not use gasshō as an example, or if
   used, cite `:141`.

No line in the corpus restates C's own planned §6 (language shapes gesture), §9 (acquisition and
learning), or §10 (decision table). Those are genuinely unowned ground.

## 6. Landing constraints for C, measured

From `reports/round-53/accept-c.py` and `reports/round-28/readme/sweep.py` (read at this worktree):

- `SIDS` leg extracts `\bS\d{3}\b` from the whole entry text and requires, for each: id ≥ S187, a
  `corpus/SOURCES.md` row, `status` cell exactly `mined`, and the entry path present in `used-by`.
  `SOURCES.md` currently holds **186 rows**, last `S186` (`corpus/SOURCES.md:215`), so every new row
  is new ground. The gesture-adjacent rows that already exist (S075, S079, S081, S101, S124, and
  S127's duplicate of S079) are **below S187 and cannot be cited**, even where they are on point —
  C needs fresh rows for its own evidence, and must not write any `S0xx` token anywhere in the entry.
- `SWEEP` leg runs `sweep.py` with cwd = root and reads its *own* exit code, requiring
  `rows 229 files 229` and `missing_from_index 0`. `sweep.py` checks (i) the section header
  `## linguistics/ (N)` — currently `corpus/README.md:242` reads `(27)` and must become `(28)`;
  (ii) each index row's gloss **byte-equal to the entry's `- topic:` line**, so the row is the topic
  text, not a free description; (iii) the `Total knowledge entries: 229.` line; (iv) the dated
  counts footer `(total 229 files; directory totals a/b/c/d/e/f)`, whose `linguistics` slot moves
  27 → 28; (v) no ghosts, duplicates, or header drift.
- `COUNT` leg is a plain `os.walk` of `corpus/knowledge` for `*.md` = 229.
- Contract shape for the entry itself: `.ufo/waves/round-50/build/ReviewEntryContract.md` §2 — eight
  head fields in the exact order `topic, gap filled, sources, couples, source, verified-at, recheck,
  scope`; numbered H2s from 1 with `Recheck` then `Scope` last; zero H3; every domain section with a
  pipe table; calibration bank statuses from `verification/calibration-registry.md:35-39`
  (R/C/B/H/T); `DR-GES-01…` decision-record IDs; `**NON-CANON.**` worked example; ≤ 230 lines by the
  claim, ≤ 250 by the contract.
- Seats write draft ids exactly `NEW-<SeatName>-<n>`; the entry must contain **zero** bare `, -N`
  fragments (that is D's defect class, and `tools/check-draft-ids.py` is the instrument).

## 7. Incidental findings (for the L1, not part of C)

- **Fragment count is 10, not 11.** Round 52's lesson (`corpus/lessons/round-52-verifier-spotcheck.md:133`)
  says "all 11 `, -N` draft-id fragments"; the file holds **10** tokens on 7 lines —
  `106:, -6`, `107:, -6`, `113:, -4`, `174:, -5`, `177:, -5,-6,-7`, `179:, -12`, `181:, -12,-2`
  (`grep -oE ', -[0-9]+'`). Claim D's stated 10 matches the file; the lesson's 11 does not. Worth a
  line in the round-53 lesson's Mistakes if D's counter is graded against the 10.
- **Two ready-made false positives for any future gesture sweep**: `israel-ancient-hebrew.md:116`
  ("Masoretic pointing", vocalization) and `civilizations/mongol.md:15,:96` (*Mudrak*, a surname).
  A naive `grep -i pointing` reports coverage that does not exist; a naive `grep -i mudra` likewise.
- `sign-languages-manual-modality.md:4` already contains a sweep command naming `gestur`, `kinesic`,
  `nonverbal` and `proxemic` and asserting **0** results at its own base `bff83ba`. That gives C a
  reproducible precedent and an honest wording for its `- gap filled:` line — but C must re-run the
  sweep at its own landing bytes, not copy the round-28 result (contract §2.3 field 2).

## 8. Confidence and unrun checks

- High confidence (measured, re-run at HEAD): the three declared sweeps and their zero/false-positive
  results; the corpus-wide singleton status of `co-speech` (1 line) and `kinesic` (1 line, in command
  text); the emblem sense split (5 gestural-sense lines, 224 total); the anchor line numbers in §4.
- Inference, not measurement: the classification of the 167 residual `emblem` lines as
  visual/symbolic — taken from co-text and from the corpus's dominant usage, not from reading all 167.
- Not run, deliberately: `reports/round-53/accept-c.py` (no entry exists, COUNT would fail by design);
  `reports/round-53/d-count.py` (claim D's instrument, outside this ticket); no external source was
  opened — every S187+ row and its 25-word verbatim quote is the drafting seats' work, and nothing
  here pre-judges a row's tier.
