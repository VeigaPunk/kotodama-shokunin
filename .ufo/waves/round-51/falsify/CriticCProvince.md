# CriticCProvince — round 51 attempt 3, falsify wave

Item attacked: claim C (commit `da31d3c`). The entry is `corpus/knowledge/linguistics/sign-languages-manual-modality.md` (223 lines). I attacked it for province drift and terminology: clinical framing, education-policy and legal rulings, deficit framing, and rejected labels used outside quoted rejections. I judged §3's "therapy settings" and §13's Living-practice flag against `PROVINCE.md`.

This is an author-lane attack, not admission. I made no lane writes except this report and no installs.

## Commands run

All commands ran from the lane root and exited 0.

1. `grep -niE 'hearing loss|audiolog|implant|treatment|cure|therap|disorder|impair' <entry>` found 6 hits, at lines 29, 63, 147, 210, 211 and 215.
   - Line 63 "therapy settings" is the only clinical-frame hit.
   - Line 211 "audiological description" is the capital-D convention's own contrast term.
   - Lines 29, 147, 210 and 215 are "hearing-impaired" inside rejections.
   - Nothing matched "hearing loss", "implant", "treatment", "cure" or "disorder".
2. `grep -niE '\bmust\b|should be taught|right to|rights?\b|law requires|\blaw\b|legal|policy|recogni' <entry>` found hits at lines 12, 78, 81, 89, 95, 131, 157, 173, 209, 213 and 223.
   - "must" at lines 81, 89, 95 and 131 is a conlang-design imperative ("a conlang must choose", "movement classes must be finite").
   - Lines 12 and 223 are the scope disclaimers.
   - Line 78 reads "history, not law" and is marked `(to-verify)`.
   - Line 157 says "only if your world has a deaf-education policy story", which is fiction-side guidance.
   - Line 173 lists "law" as a genre to record.
   - Line 209 reports an attributed count ("40% legally recognised (S121)").
   - Line 213 is the Living-practice flag (judged below).
   - Nothing matched "should be taught", "right to" or "law requires". No line rules on policy or law.
3. `grep -niE 'deficien|\black|primitive|broken|\bmime\b|pantomime' <entry>` found hits at lines 3, 29, 44, 112, 120, 135, 184, 204, 206 and 215. Every hit is a rejection or a disallowed frame:
   - 29: "not signs of deficiency"
   - 44: the anti-"broken" rule, anchored at `language-contact.md:105` ("if characters call it 'broken X', write that as their prejudice"; re-read and it holds)
   - 112: "patterned, not pantomime"
   - 120: "sign is not mime"
   - 135: "never a deficient substitute"
   - 184: "the disallowed frame"
   - 204 and 206: R rows
   - 3 and 215: listed as traps
   - Nothing matched "primitive".
4. `grep -niE 'deaf-mute|\bdumb\b|hearing-impaired' <entry>` found hits at lines 29, 147, 210 and 215. All four use the labels only inside a "never" rule, an R row or a "rejected labels" sentence. No label is used as a description.
5. Extra sweep: `grep -niE 'patient|clinic|medical|disab|handicap|suffer|afflict|congenital|hereditary|gene\b|oralism|normal' <entry>`.
   - Hereditary and gene demography appears at lines 59, 70, 74, 170 and 175, all sourced to S086, S091 and S092.
   - Line 190 uses "congenital" (judged below).
   - There is no patient, disability, "suffer" or "afflict" framing.
6. `grep -nE '^\| *S0(74|…)' corpus/SOURCES.md` read rows S074–S078, S082, S086, S087, S090–S092, S120 and S121. `grep -n '^| *S122'` read S122, whose row explicitly scopes clinical and implant content out of the entry.
7. `grep -n 'Living-practice flag'` over `corpus/knowledge` found the flag in the C entry and in three culture-material siblings: `cartography-and-mapmaking.md:230`, `hunting-foraging-subsistence.md:195` and `pastoralism-animal-husbandry.md:202`.
8. `git blame -L 63,63` and `-L 213,213` both point to `da31d3c`. `grep -niE 'manual codes|classroom|therap' .ufo/waves/round-51/build/ScribeSec03Typology.md` returns line 24, the draft row: "classrooms and contact zones between signed and spoken users". The draft has no "therapy", and line 33 notes "they exist in classrooms" and stops there.
9. `curl -sL -A <browser UA> <url>` fetched each source into `/tmp/ccp`, outside the lane, and the text was extracted with an inline python strip. Results are below.

## Sources opened (access date 2026-10-22)

| Row | URL | Result | Finding |
|---|---|---|---|
| S082 | https://gupress.gallaudet.edu/Books/M/Manual-Communication | 200 | Description: "the first authoritative examination of sign systems used in the education of deaf students. Professionals, teachers, and parents…". The table of contents covers classrooms, Sign English, ASL, SEE, Signed English, Cued Speech and ch. 9 "Manual Communication With Those Who Can Hear". **No therapy setting is named.** Tier B (publisher description) and the education scope hold. The row's quote holds. It does not support "therapy settings". |
| S090 | https://makaton.org/TMC/TMC/About_Makaton/What_is_Makaton.aspx | 200 | "a unique communication programme that uses symbols (pictures), signs (gestures) and speech". No "therapy" or "speech and language" string appears (empty grep). The row holds. |
| S077 | https://www.un.org/en/observances/sign-languages-day | 200 | A/RES/72/161 "acknowledges that early access to sign language and services in sign language, including quality education available in sign language, is vital to the growth and development of the deaf individual … recognizes the importance of preserving sign languages as part of linguistic and cultural diversity". The page also carries "pidgin" and "more than 300". **The page's own photo caption reads "…to chat with his hearing-impaired brother."** The 2026 theme is "Declaring deaf people's human rights". |
| S078 | https://wfdeaf.org/resources/sign-language-rights/ | 200 | "Language and culture are inseparable, and sign language is a crucial part of deaf culture and identity", and "Each sign language has its own structure, grammar, and lexicon, equaling spoken languages in every respect". The page also says "Deaf children must have access to a national sign language from birth". The entry did not import that sentence, which is correct for the province. |
| S121 | https://wfdeaf.org/contact/faqs/ | 200 | "200+ national sign languages … only 40% … legally recognised" and "more than 70 million deaf people belong to signing deaf communities". On "deaf-mute", deaf and dumb" or hearing impaired: "These terms are not acceptable. The preferred term is 'deaf' or 'deaf people'", and WFD with IFHOH "agreed the word 'hearing-impaired' should not be used". The row holds. |
| S076 | https://nad.org/knowledge-hub/american-sign-language/community-and-culture-frequently-asked-questions/ | 200 | Q&A "What is wrong with the use of these terms 'deaf-mute,' 'deaf and dumb,' or 'hearing-impaired'?" It discusses "dumb" directly ("The term is offensive…"). The row holds. |
| S122 | https://link.springer.com/article/10.1186/1477-7517-9-16 | 200 but only a 3,038-byte script-challenge shell, so **the article text was not readable** at the row URL. | Also opened https://harmreductionjournal.biomedcentral.com/articles/10.1186/1477-7517-9-16 (200, redirected back to the same Springer shell). Then opened the PMC mirror https://pmc.ncbi.nlm.nih.gov/articles/PMC3384464/ (200): "it is common convention to use a capital 'D' when talking about communities that use a sign language as their major language, and 'd' when talking about auditory status." The convention holds via the mirror, and line 211's "audiological description" is a fair paraphrase of "auditory status". The paper's clinical content (cochlear implants, audiologists) is correctly scoped out by the row. |

## Findings

1. **Medium.** `sign-languages-manual-modality.md:63`: "classrooms, therapy settings and contact zones … (S082)".
   - **Province:** it places manual codes in a clinical setting. `PROVINCE.md:9-14` gives the lane only linguistic-cultural coupling craft, and the entry's own scope at line 12 says it "gives no clinical … ruling". The phrase is not a ruling, but it is the only clinical frame in the entry.
   - **Provenance (QUALITY criterion 1):** the cited S082 supports deaf-education classrooms only.
   - **Not from the build wave:** the scribe draft (`.ufo/waves/round-51/build/ScribeSec03Typology.md:24`) had "classrooms and contact zones". The words "therapy settings" were added at integration in `da31d3c` and no source supports them. S090, in the next cell, does not say therapy either.
   - **Smallest fix:** change the cell to "deaf-education classrooms and contact zones between signed and spoken users (S082)", or simply delete "therapy settings and".
2. **Low.** `sign-languages-manual-modality.md:215`: "'deaf-mute', 'dumb' and 'hearing-impaired' are rejected labels … (S077, S078, S121)".
   - S077 is a counterexample for that clause: the UN page itself calls a boy "hearing-impaired" in its photo caption. S078 says nothing about labels.
   - **Smallest fix:** cite the label clause to (S121, S076) and keep S077 and S078 for the "plural, not universal" clauses. Alternatively, move "(S121, S076)" to follow "hearing-impaired" rejected labels.
3. **Low.** `sign-languages-manual-modality.md:147`: the §9 terminology line has no citation.
   - **Smallest fix:** append "(S121, S076)".
4. **Low.** `sign-languages-manual-modality.md:213`, the Living-practice flag. Judged against `PROVINCE.md`:
   - Each attributed statement holds at its source: S077's resolution text, S121's >70 million figure, and S078's "inseparable".
   - The flag makes no lane ruling. `PROVINCE.md:16-20` refuses "real-world rights/attribution rulings on reference works", and the flag relays rather than rules.
   - Its closing sentence ("write fictional communities like theirs, never as them") matches the sibling pattern (`hunting-foraging-subsistence.md:195`, `pastoralism-animal-husbandry.md:202`).
   - The drift risk is the imperative "State rights as those bodies state them". It is the only sentence in the entry that tells the reader to write rights content. None of the three sibling flags carries rights or development advocacy, and the round's context bars rights rulings.
   - The paraphrase "vital to deaf people's development" also cuts the resolution's "including quality education available in sign language". That cut keeps education policy out and is acceptable.
   - **Smallest fix:** replace "State rights as those bodies state them;" with "attribute any rights or status statement to the body that makes it; this lane rules on neither (`PROVINCE.md:16-20`);".
5. **Low.** `sign-languages-manual-modality.md:190`: "congenital deafness concentrated in two kindreds (S086)".
   - S086's row supports "high (often hereditary) deafness", and "congenital" is a medical term the cited row does not carry. The line sits inside the NON-CANON example, so the risk is minimal.
   - **Smallest fix:** change "congenital" to "hereditary".
6. **Low (outside the strict province axis, noted for the Calibration critic).** `sign-languages-manual-modality.md:78`: the lever "the hearing majority's ideology sets status and schooling choices" is an uncited causal claim with no **H** label. Unlike §3, §9 and §11, §4 has no line saying uncited cells are heuristics.
   - **Smallest fix:** append "(design frame, **H**)" to the cell.

## Checks that passed

- No clinical vocabulary beyond line 63. Line 211's "audiological" is the cited convention's own contrast term (S122, which the PMC mirror supports).
- No education-policy or legal ruling. Every "must" is a conlang-design imperative.
- No deficit framing outside rejections.
- No rejected label used descriptively.
- S078's "Deaf children must have access…" and the UN's CRPD obligation wording were left out of the entry. That keeps it inside the province.

## Unrun checks

- I did not re-open S081, S086, S087, S091 or S092. They are outside this seat's terminology scope and other seats own those re-opens.
- I did not run the claim counter (`find … | wc -l`) or `sweep.py`. RerunCCount owns those.
- S122 could not be read at its registered URL (script-challenge shell); it was verified only through the PMC mirror.

## Verdict

**HOLDS-WITH-FIXES.** C stays within the province. It makes no clinical, education-policy, legal or rights ruling, and its rejected labels and deficit frames appear only as rejections.

One medium defect must be fixed: line 63's "therapy settings", which no source supports and which brings in a clinical frame. Four low wording and citation fixes follow at lines 215, 147, 213 and 190, plus the line 78 calibration note. None of them changes the claim's count or its ownership.
