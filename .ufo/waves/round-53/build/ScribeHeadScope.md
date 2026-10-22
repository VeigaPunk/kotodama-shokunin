# ScribeHeadScope — Claim C, entry `gesture-co-speech-pointing.md`: eight-field head, `## 13. Recheck`, `## 14. Scope`

- Seat: `KotodamaR53.ScribeHeadScope` (leaf; no delegation, no background jobs, no swarms).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, branch `main`, jj-colocated.
- Lane HEAD read 2026-10-22: `60f1d2a3d832b926e37f82b11c67496d131a1431` (the round-53 declaration commit). Claim base `a9cf95fe47a82b516f6c2487cb76b89c3a71c493`.
- The only file this seat wrote is this report. No entry file, no README edit, no `corpus/SOURCES.md` row, no `corpus/lessons/round-53.md` line, no git or jj command. Scratch copies live under `/tmp/r53src` (sources) and `/tmp/r53check` (a throwaway copy of `corpus/knowledge` with the draft head pasted in, outside the lane).
- Axis: coverage. Milestone: round 53, claim C (new entry `corpus/knowledge/linguistics/gesture-co-speech-pointing.md`, 228 → 229).

## 0. Result

- The eight-field head is drafted and **measured**: both gap sweeps were re-run by this seat at the lane worktree and again on a `git archive` extract of the claim base; both return **0** at both commits, so the gap premise is fresh at base and at HEAD.
- `- topic:` is **one line, 366 characters** of topic text (378 with the `- topic: ` prefix), so the README index row copies it verbatim under the sweep's byte-equality rule and stays under the 400-character ceiling this seat was given. It carries the register words the contract's freshness probes look for as whole words — gesture, co-speech, pointing, quotable, emblem, kinesic.
- `## 13. Recheck` is drafted at **8 lines** (H2 + blank + 5 table lines + blank) and `## 14. Scope` at **8 lines** (H2 + blank + 3 paragraphs + blank + Handoff + blank). Both are inside budget; the Scope paragraph carries the required `Handoff: lore-shokunin owns …` sentence.
- The head names the four partial owners with live anchors, cites every one of them one-way, and rests nothing on them: `adornment-body-codes.md:77-93`, `sign-languages-manual-modality.md:64` and `:161`, `numerals-and-measures.md:107`, `direction-symbolism.md:6` and `:36`.
- Three external rows were opened by this seat by ordinary means only (plain `curl` with a browser user-agent, public copies): **Haviland 1993**, **Cooperrider 2023**, **Abner & Cooperrider 2015**. Registry row drafts and Gate lines are in §3; the Haviland row merges with the space-time seat's (§3.1).
- **The head carries no literal `S###` token on purpose.** The external rows it names are given by their draft ids — `NEW-ScribeSec05SpaceTime-1` (the merged Haviland 1993 row, see §3.1), `NEW-ScribeHeadScope-2` (Cooperrider 2023), `NEW-ScribeHeadScope-3` (Abner & Cooperrider 2015) and `NEW-ScribeSec07Quotable-2` (the emblem review). The L1 renumbers them at integration; the substitution map is in §4.4 item 1, and it must be done, because `reports/round-53/accept-c.py` reads the **entry text** and fails its SIDS leg if the entry cites no `S###` id at all.

## 1. Axes

| axis | state | evidence |
|---|---|---|
| coverage | head, §13 and §14 drafted inside the stated budgets; both gap sweeps measured at base and at HEAD; four partial owners named with anchors | §2, §4 |
| operability | head key order, topic-line length, couples tokens and §-references checked mechanically on a scratch copy; the couples resolver returns 7/7 `direct` | §4 |
| calibration | §13 names what must be re-opened before a figure, a verdict or a living practice's status is repeated; no heritage-policy, clinical or legal ruling anywhere in the draft; no community exoticized | §3, §4 |

## 2. Gap sweeps, re-run by this seat (2026-10-22)

Both trees measured: **HEAD** = the lane worktree at `60f1d2a`; **base** = `git archive a9cf95f | tar -x` into `/tmp/r53base`. `git diff --name-only a9cf95f..60f1d2a` lists only `reports/round-53/` files, so the corpus bytes are identical at the two commits and the sweeps must agree.

| command | base `a9cf95f` | HEAD `60f1d2a` |
|---|---|---|
| `find corpus/knowledge -iname '*gestur*' -o -iname '*pointing*' -o -iname '*kinesic*' \| wc -l` | **0** | **0** |
| `grep -rliE '^- topic:.*(gestur\|pointing\|kinesic)' corpus/knowledge \| wc -l` | **0** | **0** |
| `find corpus/knowledge -name '*.md' \| wc -l` | **228** | **228** |
| `ls corpus/knowledge/linguistics/*.md \| wc -l` | **27** | **27** |

The filename sweep was run with the claim's own spelling (no parentheses around the `-o` chain) and parenthesised; both give **0**.

Partial owners re-read at HEAD on 2026-10-22 (each anchor re-read, not recalled):

| anchor | what the line carries |
|---|---|
| `corpus/knowledge/culture-material/adornment-body-codes.md:77` | `## 7. Gesture and posture — engineered gradients and their failure modes` — the section that owns the emblem taxonomy, posture and bow gradients |
| `…/adornment-body-codes.md:79` | the toolkit bullet: Ekman and Friesen's emblems, Morris et al. (1979) emblem geography, Hall (1966) proxemic bands |
| `…/adornment-body-codes.md:82` | `- **Gradient table**:` and the bow / *wai* / *sampeah* / *kowtow* / *adoratio* / homage rows |
| `…/adornment-body-codes.md:93` | the calibration bullet (Ekman's universal-basic-emotions program contested) |
| `corpus/knowledge/linguistics/sign-languages-manual-modality.md:64` | the `co-speech gesture (boundary)` row: "conveys information but is not conventionalized and systematic the way sign is" |
| `…/sign-languages-manual-modality.md:161` | "Sign is not gesture-code: emblems and proxemics stay at `adornment-body-codes.md:79`" |
| `corpus/knowledge/linguistics/numerals-and-measures.md:107` | the finger-counting bullet: counting gesture is culturally patterned, not universal |
| `corpus/knowledge/myth-symbol/direction-symbolism.md:6` | the Haviland 1993 bibliographic record for Guugu Yimithirr pointing |
| `…/direction-symbolism.md:36` | the absolute-frame bullet: "gestures are anchored to the world, not the body (Haviland 1993, 1998; Levinson 1997)" |
| `…/direction-symbolism.md:42-44` | `- Decision table (frame → consequences):` and the `| Frame chosen | What must be true of the world | What breaks if ignored |` rows |
| `corpus/knowledge/linguistics/politeness-taboo-euphemism.md:75-76` | the taboo domain inventory and the sanction gradient (supernatural dread → kin ridicule → reputation → legal censor) |
| `corpus/knowledge/linguistics/semantics-pragmatics.md:115-120` | the deictic *origo* and taxonomy, the frames of reference paragraph, the deixis spec for a culture |
| `corpus/knowledge/verification/calibration-registry.md:35-39` | the R / C / B / H / T status vocabulary |

## 3. Sources opened this round by ordinary means (registry row drafts and Gate lines)

No headless browser, no captcha solving, no paywall or login bypass, no challenge passed. Routes: plain `curl` with a browser user-agent; one Wayback capture where the live publisher route served a bot-challenge page (see §3.4).

Column order per `corpus/SOURCES.md` registry header (`| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`). The L1 renumbers the ids at integration (S187 upward). `used-by` on every row is `corpus/knowledge/linguistics/gesture-co-speech-pointing.md`; `status` is `mined`; `opened` is `2026-10-22`.

### 3.1 Row drafts

| draft id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| NEW-ScribeHeadScope-1 — **merge into the space-time seat's Haviland row** | Haviland, John B. 1993, "Anchoring, Iconicity, and Orientation in Guugu Yimithirr Pointing Gestures", *Journal of Linguistic Anthropology* 3(1): 3–45, doi 10.1525/jlin.1993.3.1.3 — author's own PDF copy — https://pages.ucsd.edu/~jhaviland/Publications/jlin.1993.3.1.3.Anchoring.pdf | paper | A | the pointing gestures of Guugu Yimithirr speakers at Hopevale, Queensland, and the anchoring of gesture in the cardinal system, as the author analyses them; not other Australian languages | Abstract, printed p. 3; the section "It's Not Polite to Point", printed p. 17 | "use inflected forms of four cardinal direction words in all talk about location and motion"; "pointing gestures can have interactional significance deriving from the fact that they are silent, and hence selectively covert, replacements for spoken referring expressions" | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/gesture-co-speech-pointing.md |
| NEW-ScribeHeadScope-2 | Cooperrider, Kensy 2023, "Fifteen ways of looking at a pointing gesture", *Public Journal of Semiotics* 10(2): 40–84, doi 10.37693/pjos.2023.10.25120 — published PDF — https://journals.lub.lu.se/pjos/article/download/25120/22365 | paper | B | the survey's own framing of pointing and the pointing-taboo literature it reports; the taboo examples are reported from other studies, not primary data of this article | Abstract, printed p. 40; §2.6 "A widespread taboo", printed pp. 52–53 | "an intentional movement, often of the hand, by which one person tries to direct another’s attention toward something"; "In parts of Africa, pointing with the left hand is taboo, as the left side is associated with toileting and other profane functions."; "Blust (2021) reported cases of it from 124 cultural communities, spread widely across the globe." | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/gesture-co-speech-pointing.md |
| NEW-ScribeHeadScope-3 | Abner, Natasha; Cooperrider, Kensy 2015, "Gesture for Linguists: A Handy Primer", *Language and Linguistics Compass* 9(11): 437–451, doi 10.1111/lnc3.12168 — PMC author manuscript — https://pmc.ncbi.nlm.nih.gov/articles/PMC4721265/ | paper | B | the primer's own framing and typology for linguists, the speech-gesture integration claims it states, and the field's own caution about cross-linguistic variation; not primary field data | §3.2 "Semantic integration of speech and gesture"; §4 "Variation in gesture across languages and cultures" (PMC author manuscript, unpaginated) | "speech is categorical and discrete, whereas gesture is gradient and analog"; "there is, unfortunately, no entrenched typological tradition in the field of gesture studies, as there is for the field of linguistics"; "An obvious place where we find such variation is in emblems" | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/gesture-co-speech-pointing.md |

Tier notes for the L1 and the critic: **NEW-ScribeHeadScope-2** and **NEW-ScribeHeadScope-3** are surveys, so tier B by the `SOURCES.md` rule ("B — strong secondary (expert write-up with reproducible detail, survey, textbook)"), and their scope cells say so; the same treatment the lane gave S051 and S129. **NEW-ScribeHeadScope-1** is the author's own copy of the published article and is tier A for its exact scope (one community's pointing gestures, as the author analyses them), and the scope cell says what it does not cover. `tools/check-source-access.py` scans the `source`, `anchor` and `teaches` cells for bypass wording; the three rows above contain no such wording and the challenge note is kept out of the row cells for NEW-ScribeHeadScope-1 to -3 because those three were opened directly.

**Duplicate-work warning (read before filing).** Haviland 1993 is already proposed by the space-time seat as its `NEW-ScribeSec05SpaceTime-1`, provisionally S187, with the anchor "If one is talking about going to the beach and the beach is east, one points east" (printed p. 12). **One row per work is the lane's rule**, so the L1 must file a single Haviland 1993 row that carries both anchors: the space-time seat's p. 12 beach-east sentence and this seat's abstract (printed p. 3) and "It's Not Polite to Point" (printed p. 17). This seat's draft row above is therefore a **row-draft, not a second row**: widen the anchor cell of the merged row instead of filing twice. The same caution applies to Cooper et al. 2018, which the quotable-gesture and build seats both name — the critic's list (`CriticSourceTiers.md:49`) already says the merged row must exist once.

**What the two survey rows may and may not carry.** The Cooperrider 2023 row is tier B and its scope cell says the taboo examples are reported from other studies. Under the critic's rule (a review is A only for the author's own scheme and B for every study it reports), the working definition in its abstract is Cooperrider's own wording and the taboos are not; the row as drafted is filed B throughout, which is the safe direction. If §8 wants a taboo as evidence, it must cite it as reported in the review (Blust 2021 and others) and not present the "124 cultural communities" figure as the review's own census — the row's `teaches` cell and the Gate line in §3.2 already say so. The Abner & Cooperrider 2015 row is tier B for the same reason: it is a primer for linguists, and its statement that gesture has no entrenched typological tradition is a survey-level caution, which §13 repeats as a recheck trigger rather than as a finding.

### 3.2 Gate lines for the round-53 lesson `## Gate`

```
- S1xx (L1 assigns) — https://pages.ucsd.edu/~jhaviland/Publications/jlin.1993.3.1.3.Anchoring.pdf — accessed 2026-10-22 — Abstract, printed p. 3: "use inflected forms of four cardinal direction words in all talk about location and motion". Grounds: the frame side of a pointing default — Guugu Yimithirr speakers anchor talk about place in cardinal terms. Seat: ScribeHeadScope.
- S1xx (L1 assigns) — https://pages.ucsd.edu/~jhaviland/Publications/jlin.1993.3.1.3.Anchoring.pdf — accessed 2026-10-22 — printed p. 17, the section "It's Not Polite to Point": "pointing gestures can have interactional significance deriving from the fact that they are silent, and hence selectively covert, replacements for spoken referring expressions". Grounds: pointing is not neutral decoration; it carries social weight, which the §8 social-control section must calibrate.
- S1xx (L1 assigns) — https://journals.lub.lu.se/pjos/article/download/25120/22365 — accessed 2026-10-22 — Abstract, printed p. 40: "an intentional movement, often of the hand, by which one person tries to direct another’s attention toward something". Grounds: the working definition of pointing the entry builds on, in the survey's own words.
- S1xx (L1 assigns) — https://journals.lub.lu.se/pjos/article/download/25120/22365 — accessed 2026-10-22 — §2.6 "A widespread taboo", printed p. 52: "In parts of Africa, pointing with the left hand is taboo, as the left side is associated with toileting and other profane functions.". Grounds: a pointing taboo with a named place, so §8 can name a community and a town instead of "some cultures forbid pointing".
- S1xx (L1 assigns) — https://journals.lub.lu.se/pjos/article/download/25120/22365 — accessed 2026-10-22 — printed p. 53: "Blust (2021) reported cases of it from 124 cultural communities, spread widely across the globe.". Grounds: the scale of the rainbow-pointing taboo, reported by the survey from Blust (2021) — the count belongs to Blust, not to this row, and the §10 decision table must not present it as the survey's own census.
- S1xx (L1 assigns) — https://pmc.ncbi.nlm.nih.gov/articles/PMC4721265/ — accessed 2026-10-22 — §3.2 "Semantic integration of speech and gesture": "speech is categorical and discrete, whereas gesture is gradient and analog". Grounds: why the two channels carry different information — the rule behind §6 (language shapes gesture).
- S1xx (L1 assigns) — https://pmc.ncbi.nlm.nih.gov/articles/PMC4721265/ — accessed 2026-10-22 — §4 "Variation in gesture across languages and cultures": "there is, unfortunately, no entrenched typological tradition in the field of gesture studies, as there is for the field of linguistics". Grounds: the calibration that gesture has no WALS-style typology yet, so the entry's typologies are design heuristics (**H**), not established cross-cultural patterns.
- S1xx (L1 assigns) — https://pmc.ncbi.nlm.nih.gov/articles/PMC4721265/ — accessed 2026-10-22 — §4 "Variation in gesture across languages and cultures": "An obvious place where we find such variation is in emblems". Grounds: emblems are where cultural variation is most documented, which is why §7 points at the emblem review rather than restating the partial owner.
```

### 3.3 Opened and not filed

- Wikipedia, "Gesture" (https://en.wikipedia.org/wiki/Gesture, fetched through the reader's Wikipedia API on 2026-10-22): a tertiary encyclopedia page. Not filed as a supporting row — the lane's precedent is S178, where a Wikipedia row was kept only as a rejected lead. The entry must not cite it.
- `https://hal.science/hal-00378850/document` (Tellier, "The development of gesture") returned an HTML page, not a PDF, to a plain request; nothing was read from it, so it is unopened and supports no claim.

### 3.4 Access note on a row this seat does not own

`https://www.glossa-journal.org/article/id/9705/` and `https://www.glossa-journal.org/article/9705/galley/33692/download/` both served an Anubis bot-challenge page ("Making sure you're not a bot!") to a plain request on 2026-10-22; this seat did not get past it and read the article from the Wayback capture of the same URL instead, an ordinary copy. The quotable-gesture seat reports reading the live article page on its own route with HTTP 200 and no challenge. Both observations stand, the row is that seat's (`NEW-ScribeSec07Quotable-2`), and this seat adds nothing to it. If the L1 writes the access note into the row, it should say which route was clean and should avoid the words `bypass`, `passed` and `get past` near the word `challenge`: `tools/check-source-access.py` matches those combinations whatever precedes them (`BYPASS.search("HTTP 403 — not bypassed")` returns True), so a negated access note in a `mined` row still flags the row as unopened.

## 4. Draft text ready to paste

### 4.1 The opening block (line 1 = H1, line 2 = blank, then the eight head fields in order)

```markdown
# Gesture in speech — co-speech gesture, pointing and quotable gestures as a conlang and worldbuilding method: what the hands carry, what the frame fixes, and where a designer decides

- topic: co-speech gesture, pointing and quotable gestures as a conlang and worldbuilding method — gesture as part of the utterance, what each gesture type carries, pointing in space and time, what a language packages into its speakers' hands, emblem repertoires, the social control of gesture, acquisition, and the calibration traps of reading kinesics as a universal script
- gap filled: no file in the corpus owns co-speech gesture, pointing or quotable gestures as a register. Filename sweep `find corpus/knowledge -iname '*gestur*' -o -iname '*pointing*' -o -iname '*kinesic*' | wc -l` → **0**; topic sweep `grep -rliE '^- topic:.*(gestur|pointing|kinesic)' corpus/knowledge | wc -l` → **0**; both run 2026-10-22 at the lane worktree (HEAD `60f1d2a`, corpus bytes identical to claim base `a9cf95f`). Partial owners, cited one-way in §2 and never restated: `culture-material/adornment-body-codes.md:77-93` (emblem taxonomy after Ekman and Friesen 1969, Morris 1979 emblem geography, Hall's proxemic bands, bow and *wai* gradients, nod/shake inversion), `linguistics/sign-languages-manual-modality.md:64` and `:161` (co-speech gesture as the manual modality's boundary row), `linguistics/numerals-and-measures.md:107` (finger counting), `myth-symbol/direction-symbolism.md:6` and `:36` (Guugu Yimithirr absolute directions; Haviland 1993 on pointing).
- sources:
  - In-corpus anchors (`corpus/knowledge/`-relative `path:line`, each re-read at the lane worktree on 2026-10-22 at HEAD `60f1d2a`): `culture-material/adornment-body-codes.md:77-93`; `linguistics/sign-languages-manual-modality.md:64`, `:161`; `linguistics/numerals-and-measures.md:107`; `myth-symbol/direction-symbolism.md:6`, `:36`, `:42-44`; `linguistics/politeness-taboo-euphemism.md:75-76`; `linguistics/semantics-pragmatics.md:115-120`; `verification/calibration-registry.md:35-39`.
  - External shelf — **opened this round (2026-10-22) by ordinary means only** (plain requests and public copies; no row was reached past an access control), registered in `corpus/SOURCES.md` as this round's new rows above the last base row, each row carrying its URL, access date, tier scope, anchor and a located quote in the registry itself: the Guugu Yimithirr pointing evidence (Haviland 1993, NEW-ScribeSec05SpaceTime-1, the merged row), the pointing survey and the taboos it reports (Cooperrider 2023, NEW-ScribeHeadScope-2), the linguist's primer on gesture types, speech-gesture integration and cross-cultural variation (Abner & Cooperrider 2015, NEW-ScribeHeadScope-3), and the emblem and quotable-gesture review the quotable-gesture seat filed this round (NEW-ScribeSec07Quotable-2); the integrator assigns the row ids at integration and every id the entry then cites is at or above the round-53 floor.
- couples: linguistics — `sign-languages-manual-modality.md` (owns the manual modality and the co-speech gesture boundary row, `:64` and `:161`; this entry owns co-speech gesture as its own register); linguistics — `numerals-and-measures.md` (owns finger counting, `:107`; this entry owns the gesture a counting system may ride on); linguistics — `semantics-pragmatics.md` (owns deixis and frames of reference in grammar, `:115-120`; this entry owns the bodily half of deixis); linguistics — `politeness-taboo-euphemism.md` (owns the taboo domain inventory and the sanction gradient, `:75-76`; this entry owns gesture-side taboos and politeness); culture-material — `../culture-material/adornment-body-codes.md` (owns the emblem taxonomy, posture gradients and proxemic bands, `:77-93`; this entry owns co-speech gesture and pointing); myth-symbol — `../myth-symbol/direction-symbolism.md` (owns frames of reference and the direction register, `:6`, `:36`, `:42-44`; this entry owns the pointing that lands in that frame); verification — `../verification/calibration-registry.md` (status codes, `:35-39`); lore-shokunin (canon handoff, §14).
- source: lane-side authority is the in-corpus anchor list above plus the external rows opened this round and registered in `corpus/SOURCES.md` above the last base row (Haviland 1993, NEW-ScribeSec05SpaceTime-1; Cooperrider 2023, NEW-ScribeHeadScope-2; Abner & Cooperrider 2015, NEW-ScribeHeadScope-3), each carrying its URL, access date 2026-10-22 and tier scope. Design method: fix the language's frame of reference and its speech first, then decide what the hands add, then fix the pointing form, the quotable repertoire and the taboos behind them.
- verified-at: 2026-10-22 — written against the lane worktree at HEAD `60f1d2a3d832b926e37f82b11c67496d131a1431` (claim base `a9cf95f`; the corpus tree is byte-identical at the two commits); pre-entry `find corpus/knowledge -name '*.md' | wc -l` → **228**, `ls corpus/knowledge/linguistics/*.md | wc -l` → **27**; the two gap sweeps are recorded in the gap-filled field; the post-entry counts (**229** and **28**) and the README sweep render line are the integrator's to record at landing, where `python3 -B reports/round-53/accept-c.py` re-runs `find corpus/knowledge -name '*.md' | wc -l` and `python3 -B reports/round-28/readme/sweep.py`. Not claimed: the post-entry counts, the README sweep render line, the assigned `S###` ids, and any gate run against the landed entry are not claimed here — this seat measured only the pre-entry state and the two gap sweeps.
- recheck: see §13; re-run the two gap sweeps in the head before adding co-speech gesture material elsewhere; re-open every cited external row before repeating a number from it (NEW-ScribeSec05SpaceTime-1, NEW-ScribeHeadScope-2, NEW-ScribeHeadScope-3); re-read each partial-owner anchor before re-drawing a seam; and re-open the emblem row (NEW-ScribeSec07Quotable-2) before an inventory count is repeated in a world document.
- scope: reference method and lane policy for the linguistics partition: co-speech gesture, pointing and quotable gestures as a conlang and worldbuilding method — what a gesture carries beside the words, what each gesture type does, pointing in space and time, what a language packages into its speakers' hands, emblem repertoires, the social control of gesture, and how gesture is learned and lost. The emblem taxonomy, posture gradients and proxemic bands stay with `../culture-material/adornment-body-codes.md`; the manual modality and the sign-versus-gesture boundary stay with `sign-languages-manual-modality.md`; finger counting stays with `numerals-and-measures.md`; frames of reference, cardinal directions and the frame table stay with `../myth-symbol/direction-symbolism.md`; the animation of gesture in a game goes to the game-dev lanes; canon to lore-shokunin (§14).
```

### 4.2 `## 13. Recheck` — 8 lines including the H2 line and the blank lines

```markdown
## 13. Recheck

| Trigger | What to re-open first |
|---|---|
| adding co-speech gesture material anywhere else | the two gap sweeps in the head, then the partial-owner anchors: `../culture-material/adornment-body-codes.md:79`, `:82`; `sign-languages-manual-modality.md:64`, `:161`; `numerals-and-measures.md:107`; `../myth-symbol/direction-symbolism.md:36`, `:44` |
| repeating a figure or a count | the external row behind it — NEW-ScribeSec05SpaceTime-1 (one community's own fieldwork), NEW-ScribeHeadScope-2 (a review reporting others' findings), NEW-ScribeHeadScope-3 (a primer's caution that gesture has no entrenched typological tradition), NEW-ScribeSec07Quotable-2 (emblem inventories and their documentation limits) |
| repeating a §12 verdict, or a living practice's status | the calibration rows behind the verdict, and the community or UNESCO page itself before the quote; no such page was opened this round, so any such claim carries `(to-verify)` |

```

Line count: 1 `## 13. Recheck`, 2 blank, 3 table header, 4 separator, 5–7 the three rows, 8 blank. **Eight lines.**

### 4.3 `## 14. Scope` — 8 lines including the H2 line and the blank lines

```markdown
## 14. Scope

Reference method and lane policy for the linguistics partition. This entry owns co-speech gesture, pointing and quotable gestures as a conlang and worldbuilding method: what a gesture carries beside the words, what each gesture type does, pointing in space and time, what a language packages into its speakers' hands, emblem repertoires, the social control of gesture, and how gesture is learned and lost.
It hands the emblem taxonomy, the posture and bow gradients and the proxemic bands to `../culture-material/adornment-body-codes.md` (`:79`, `:82`); the manual modality, homesign and contact-sign boundary to `sign-languages-manual-modality.md` (`:64`, `:161`); finger counting to `numerals-and-measures.md` (`:107`); frames of reference, cardinal directions and the frame table to `../myth-symbol/direction-symbolism.md` (`:36`, `:44`); gesture animation in a game to the game-dev lanes; and canon to lore-shokunin.
It names communities and languages precisely, forbids no practice, and rules on no clinical, legal or heritage-policy question; a fictional culture borrows mechanisms, never a community's identity.

Handoff: lore-shokunin owns whether a gesture, a pointing form or an emblem exists in a world, who may use it and what it means there; this entry ends at the design record, the calibration bank and the worked example, and never decides canon.
```

Line count: 1 `## 14. Scope`, 2 blank, 3–5 the three paragraphs, 6 blank, 7 the Handoff paragraph, 8 blank. **Eight lines.**

### 4.4 What the L1 must change when pasting

1. **Renumber the draft ids.** Replace `NEW-ScribeSec05SpaceTime-1`, `NEW-ScribeHeadScope-2`, `NEW-ScribeHeadScope-3` and `NEW-ScribeSec07Quotable-2` with the `S###` ids the L1 assigns (S187 upward), in the head's two fields and in §13's third table row. (This seat's own draft row for Haviland 1993, `NEW-ScribeHeadScope-1` below, is merged into the space-time seat's Haviland row — one row per work — so it is not a separate substitution.) Two gates make this mandatory, not cosmetic: `reports/round-53/accept-c.py` reads the **entry text** and fails its SIDS leg ("no S-id cited") while the head still carries only draft ids, and `tools/check-draft-ids.py` (the round-53 mined-mistake repair) reports every surviving `NEW-<SeatName>-<n>` token as a finding. On a scratch copy with the four tokens replaced by `S187`–`S190`, `check-draft-ids.py` prints `DRAFT_IDS: 0 findings`.
2. **Write the id range into `- source:`** in the model's style ("rows S187–S2xx"), naming only rows that exist and are `mined` with `used-by` = `corpus/knowledge/linguistics/gesture-co-speech-pointing.md`. Do not name a range endpoint that is not a row.
2b. **Renumber entry-wide, not only in this seat's fields.** Every seat's section text also carries `NEW-<SeatName>-<n>` draft ids; the substitution must cover the whole entry, and `tools/check-draft-ids.py` must report 0 findings on the landed file. This is the round-52 mined mistake (bare `-N` fragments left in a landed entry) and it is the same failure this round's claim D repairs.
3. **Copy `- topic:` into the README index row byte for byte.** The topic text is 366 characters:

```
co-speech gesture, pointing and quotable gestures as a conlang and worldbuilding method — gesture as part of the utterance, what each gesture type carries, pointing in space and time, what a language packages into its speakers' hands, emblem repertoires, the social control of gesture, acquisition, and the calibration traps of reading kinesics as a universal script
```

The row goes in `corpus/README.md` under `## linguistics/ (27)` → `(28)`, alphabetically between `dialect-register-consistency.md` and `historical-linguistics.md`; the totals line becomes 229 and the footer `(total 229 files; directory totals 28/26/28/29/24/94)`.

## 5. Checks run on the draft (read-only, scratch copy outside the lane)

The draft head and the two closing sections were pasted into a throwaway copy of `corpus/knowledge` at `/tmp/r53check` and checked with the lane's own tools and the contract's checker:

| check | command | result |
|---|---|---|
| head key order, single topic line, single couples line, H2 numbering, no H3, no placeholder word, §-reference bound, pipe-table present | the round-50 contract's Part A checker, re-run on the scratch draft | head keys in the order `topic, gap filled, sources, couples, source, verified-at, recheck, scope`; exactly one `- topic:` and one `- couples:`; no `TODO`/`TBD`/`placeholder`/`scaffold`/`MVP`; no §-reference above 14; the "no Calibration H2" and "no **NON-CANON**" findings are expected on this partial file, because §11–§12 belong to other seats |
| couples tokens resolve | `python3 -B tools/harness/basename-couples-resolver.py <scratch draft>` | 7 tokens, **7 `direct`**, 0 unresolved, 0 ambiguous, 0 fallback |
| couples tokens resolve (older extractor) | `python3 -B tools/harness/couples-reference-extractor.py <scratch draft>` | same 7 tokens, all `direct`, exit 0 |
| provenance gate | `python3 -B tools/gates/provenance-audit.py <scratch draft>` | exit 0, `findings=0`; 1 `(to-verify)` mark reported as inventory |
| topic byte-equality with the README row | the sweep's own `topic_of()` on the scratch draft | topic extracted as one line, 366 characters, no continuation lines to join; the six probe words gesture / co-speech / pointing / quotable / emblem / kinesic are all present |
| line budgets | manual count of the pasted blocks | §13 = 8 lines, §14 = 8 lines |
| draft-id fragments (the round-53 mined mistake) | `python3 -B tools/check-draft-ids.py --root /tmp/r53check corpus/knowledge/linguistics/gesture-co-speech-pointing.md` | 15 `DRAFT_ID` findings (F1), from four distinct draft tokens — `NEW-ScribeSec05SpaceTime-1` ×4, `NEW-ScribeHeadScope-2` ×4, `NEW-ScribeHeadScope-3` ×4, `NEW-ScribeSec07Quotable-2` ×3 — and no F2/F3 fragment. On a copy with those four tokens replaced by `S187`–`S190`, the same command prints **`DRAFT_IDS: 0 findings`** and exits 0, so the renumbering in §4.4 item 1 leaves no `-N` fragment behind |
| no `S###` token in the head as drafted | `grep -o 'S[0-9][0-9][0-9]'` on the scratch draft | none; the head names the shelf by draft id only, so no wrong id can land (see §4.4) |

## 6. Out of scope for this seat

Sections 1–12 of the entry, the decision record, the calibration bank, the worked example, the README row and footer, the `corpus/SOURCES.md` rows themselves and the round-53 lesson belong to the other seats and to the L1. This seat drafted only the opening block, §13 and §14, and opened three sources for the head and the closing sections.

## 7. Unrun checks and limits

- **The entry does not exist**, so no lane gate was run against a landed file. The checks in §5 ran against a scratch copy under `/tmp/r53check`, never against the lane. `python3 -B reports/round-28/readme/sweep.py`, `python3 -B reports/round-53/accept-c.py` and `python3 -B tools/check-source-access.py` must be run once at integration, on the landed tree.
- The **8-line counts are hand counts** of the pasted blocks, not script output; the blank line that separates §13 from §14 is counted inside §13, and the trailing blank inside §14. If the integrator counts the separator differently, both blocks drop by one line and stay inside budget.
- The **S-id range is unknown to this seat**; it is the L1's to assign. The head deliberately names no `S###` token so that no wrong id can land in the entry (see §4.4 item 1).
- **Abner & Cooperrider 2015** was read as the PMC author manuscript (unpaginated), so its row anchors by section heading, not by printed page; the published pagination is 437–451 and was not visible in the copy read.
- **Cooperrider 2023**'s taboo examples and the "124 cultural communities" figure belong to the studies it reports (Blust 2021 and others); the row is tier B and its scope cell says so. Nothing in the head or the closing sections presents that count as the survey's own census.
- The **Tellier HAL PDF** was not obtained, and the **Wikipedia "Gesture" page** is a tertiary lead only; neither supports any claim in the draft.
- **No heritage, clinical or legal question is ruled on** anywhere in the draft, and no community is exoticized: the only communities named are Guugu Yimithirr speakers at Hopevale, Queensland, and the "parts of Africa" of the survey's left-hand taboo report, both with a named source and a named place.

## 8. Tooling record

- **No installs and no updates.** Every tool used was already present on the host: system `python3`, `curl`, `pdftotext` (poppler), `grep`, `sed`, `git` (read-only: `rev-parse`, `log`, `diff --name-only`, `archive`, `show`). No package transaction was run; the host's pacman transactions are paused, and no install was needed.
- Downloads and scratch trees live under `/tmp/r53src` and `/tmp/r53check`, outside the lane and outside the fleet repo. Nothing was written inside `/home/vgpnk/Projects/shokunin/kotodama-shokunin` except this report.
