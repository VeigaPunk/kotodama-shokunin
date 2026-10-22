# CriticCRestatement — round 51 attempt 3, falsify wave

Seat: `KotodamaR51a3.CriticCRestatement` (critic, leaf, read-only on the lane). Author-lane attack, never admission.

## Item attacked

Claim C (axis: coverage): `corpus/knowledge/linguistics/sign-languages-manual-modality.md` at commit `da31d3c`. The attack asks three things. Does the entry restate an existing owner's register? Does it claim the gesture ownership that `culture-material/adornment-body-codes.md` section 7 holds? Is the 227th file hollow? The falsifier comes from `reports/round-51/claims.json:44`: "a non-author review finding that the entry restates an existing owner's register."

Partial owners compared: `linguistics/phonetics-phonology.md:195-205`, `culture-material/adornment-body-codes.md` section 7 (lines 77-93, plus the whole file), `linguistics/sound-symbolism.md:120-126`, `linguistics/syntax-typology.md:95-103`, `linguistics/numerals-and-measures.md:103-111`, `linguistics/writing-systems.md:15-25`, `linguistics/language-contact.md:85-110`. I also re-read every other in-corpus anchor the entry cites.

## Commands run (all read-only on the lane; experiments only in the private scratch clone directory)

1. `git log --oneline -6; git status --short; find corpus/knowledge -name '*.md' | wc -l; ls corpus/knowledge/linguistics/*.md | wc -l; wc -l <C>; git diff --stat bff83ba HEAD -- <the seven owner files>`. Exit 0.
   - The tip is `9feb69e`. The only untracked path is `.ufo/waves/round-51/`.
   - Counts: **227** knowledge files, **26** linguistics files, and the entry has **223** lines.
   - The owner-file diff since base is **empty**, so C edited no owner.
2. Grep tool with the negated glob `!**/sign-languages-manual-modality.md` over `corpus/knowledge` returned "No matches found". That result is false, because `sound-symbolism.md:124` contains "signed languages". I treated it as a tool artefact and re-ran the probe with `rg` (command 3).
3. `rg -n -i -w --glob '!linguistics/sign-languages-manual-modality.md' -e 'sign languages?' -e 'signed languages?' -e 'sign-language' -e homesign -e 'fingerspell\w*' -e Stokoe -e Nicaraguan -e deaf -e 'International Sign' -e 'manual code' -e 'signers?' -e 'Plains Indian' corpus/knowledge`. Exit 0.
   - Outside C, the only hits are `phonetics-phonology.md:201-202`, `syntax-typology.md:99`, `sound-symbolism.md:14` (bibliography) and `:124`.
   - `civilizations/lakota-plains.md:3,:27` also match, but only through "Plains Indian Ledger Art", which is not sign.
   - (The glob does not exclude the C file itself, so C's own lines also print. I ignored them.)
4. Word 4-, 5- and 6-gram overlap (a read-only python3 script printing to stdout) between C and each owner span. Exit 0.

   | Owner span | Shared 4-grams | Shared 6-grams | Where the shared grams sit in C |
   |---|---|---|---|
   | phonetics-phonology.md:195-205 | 7 (13.5% of owner) | 5 | C:42, a §2 quote-back of :201 |
   | adornment-body-codes.md §7 | **0** | **0** | — (also 0 against the whole file) |
   | sound-symbolism.md:120-126 | 11 (14.9%) | 9 | C:47, a §2 quote-back of :124 |
   | syntax-typology.md:95-103 | 2 (1.0%) | 0 | C:4, C:38, head and §2 quote-backs |
   | numerals-and-measures.md:103-111 | 0 | 0 | — |
   | writing-systems.md:15-25 | 0 | 0 | — ("not writing proper" is a 3-gram, at C:4, :41, :173) |
   | language-contact.md:85-110 | 6 (1.5%) | 3 | C:44, a §2 quote-back of :105 |

   I confirmed the locations with `rg -n -o` (exit 0). Every shared phrase sits on a one-way §2 or head citation line of that owner. No body section from §3 to §13 shares a 4-gram with any owner.
5. Probes for content the entry promises but does not develop. I grepped C (word-bounded, case-insensitive) for `numeral|numerals|number|counting|diglossi\w*|interpret\w*|revival|revive\w*|broken|creole|pidgin|layering|simultaneous|register(s)`. Exit 0. The results are in the findings below.
6. Gesture-vocabulary probe on C: `emblem|illustrator|proxemic|posture|etiquette|gesture|co-speech|kinesic`. 18 lines matched. Every emblem, posture and proxemics mention hands off to `adornment-body-codes.md:79` (C:25, :37, :66, :160, :219). The exceptions are §3 C:64 and §1 C:29, covered in findings 1 and 2.
7. Integrity checks:
   - **52** distinct S-ids are cited (S071-S122). Every one has a `corpus/SOURCES.md` row whose used-by cell names the entry; the loop printed no MISSING and no no-used-by.
   - The README index row is at `corpus/README.md:251`.
   - A forbidden-name probe for `round-51|boundary-count|lessons/` in C found no match (exit 1, the expected result).
   - Calibration marks in C: 10 `(to-verify)` and 18 heuristic labels.
8. `rg -l '^## [0-9]+\. Scope'` over corpus/knowledge found 33 files, so a closing Scope section that repeats the head scope line is the lane's convention, not padding. Only 4 files have a numbered Recheck section.
9. Scratch work, in `/fast/scratch/hyaku/kotodama-r51a3-falsify/CriticCRestatement` (I checked its realpath first):
   - `curl` of S087 returned http=200, 343100 bytes; `pdftotext -layout` read it.
   - `curl` of S079 returned http=200, 58024 bytes; I stripped the HTML to text and searched it.

Unrun: `python3 -B reports/round-28/readme/sweep.py`, which belongs to the RerunCCount seat. I did not audit any S-row other than S079 and S087.

## Sources opened (access date 2026-10-22)

- **S079** — https://voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement/
  - The cursor WebFetch attempt failed with "Error: Fetch timed out while retrieving content". `curl` then returned http 200.
  - The Resilience section holds up: the children's gestures "are structured like the early communication systems that children develop when exposed to conventional language".
  - The Hearing Gesture section says gestures "often convey substantive, task-related information".
  - The page never says that co-speech gesture "is not a conventional system". The word "conventional" appears 4 times, all in the homesign section. "Universal", "all speakers" and "co-speech" each appear 0 times.
  - Tier A for the homesign scope holds. The row's located quote about co-speech gesture is the row author's gloss, not page text.
- **S087** — https://linguistics.stonybrook.edu/faculty/mark.aronoff/files/Emerging%20sign%20languages.pdf (Meir, Sandler, Padden and Aronoff 2010, author manuscript)
  - Lines 134-143 of the text extraction (the introduction): "we assume a distinction between gesture, homesign, and sign language … Gesture and sign language are distinguished primarily by conventionalization and systematicity … However, the distinction is not categorical but gradient." The "gradient" sentence is about homesign versus sign language.
  - Lines 176-181 (ABSL origin): "Since the children were deaf, they used gestures. Some of the gestures were already being used in the community…"
  - The words "hierarchy", "raw material" and "build on" do not appear.
  - Tier A and the typology scope hold.

## Findings

1. **Medium — §3 makes a second, broader claim about gesture that contradicts the owner and outruns its source.**
   - Pointer: `sign-languages-manual-modality.md:64`, the "gesture boundary" row: "all speakers, co-speech (S079) | universal among speakers (S079) | unbounded; no shared convention | information-bearing but not a conventional system (S079)".
   - The row is labelled "gesture" without qualification, yet it says gesture has "no shared convention". `adornment-body-codes.md:79` holds *emblems*, "culture-specific gestures with dictionary meanings", which are conventional gestures. C's own §1 (C:25) uses that conventional emblem repertoire as its fail case.
   - So C's §3 states a different and wider truth about gesture than its owner, which makes it a duplicate authority on what gesture is.
   - S079 does not carry "universal among speakers" or "not a conventional system" (see Sources above).
   - Smallest fix: relabel the row "co-speech gesture (boundary; emblems stay at `adornment-body-codes.md:79`)". Drop "universal among speakers" and "no shared convention". Cite the conventionalization distinction to S087 at the introduction (pdftotext lines 134-136) rather than to S079.
   - This is a fixable defect, not a fatal one. C nowhere claims emblems, posture or proxemics, and its n-gram overlap with adornment is zero.
2. **Medium — §1 sets a design rule that contradicts the entry's own sourced evidence.**
   - Pointer: `sign-languages-manual-modality.md:29`: "a worldbuilder writes the register's grammar first and lets gesture borrow from it, never the reverse (design heuristic, **H**)".
   - The entry's own sourced lines say the opposite. C:64 calls gesture "the raw material sign systems build on (S087)". C:126 says NSL cohorts "turned early gestural signing into a linguistic system". S087 at pdftotext lines 176-181 has ABSL begin from gestures "already being used in the community".
   - Smallest fix: replace "never the reverse" with "community gesture may seed signs (S087); write the grammar before the lexicon borrows from gesture".
3. **Medium — the §2 boundary table promises content that no body section develops.**
   - These rows say a topic "is designed here" or "is applied here", but the word-bounded probes find no body text for them:
     - C:39 "numeral morphology inside signed systems is designed here". The only hit for `numeral|counting` in C is that line.
     - C:49 "signed registers and deaf-hearing diglossic arrangements are applied cases here". `diglossi\w*` has its only hit there.
     - C:45 "their loss and revival are applied here". §4 C:79 covers loss, but `revival` has its only hit at C:45.
     - C:44 "the same anti-'broken' rule are applied here". `broken` has its only hit at C:44.
     - C:8, the couples line, says "interpreting between signed and spoken languages is one live case". The only related hit is C:156 "meeting/interpreting register".
   - Because the entry names these as owned territory but leaves it empty, it is not hollow overall, but it is hollow at these five seams.
   - Smallest fix: either add one sourced sentence each in §3, §4, §6 and §10, or narrow each cell to "the machinery stays there; not developed here".
4. **Low — §3 overreaches its source on the gradient claim.**
   - Pointer: `sign-languages-manual-modality.md:66`: "gesture, homesign and sign languages form a gradient, not a hierarchy (S087)".
   - S087 applies "not categorical but gradient" to homesign versus sign language. It separates gesture from sign by conventionalization, and it contains no "hierarchy" wording.
   - Smallest fix: "homesign and sign languages form a gradient (S087); gesture differs from both by conventionalization (S087)".
5. **Low — internal calibration mismatch.**
   - Pointer: `sign-languages-manual-modality.md:46` marks "restricted manual registers in silence-bound communities" as `(to-verify)`, while §9 at C:141 sources monastic signs to S112, which is bounded.
   - Smallest fix: cite S112 in C:46 and drop the `(to-verify)` mark there.
6. **Low — the entry repeats its own terminology rule.**
   - The "never deaf-mute / hearing-impaired" rule appears four times: C:29, :147, :210 and :215. This repeats the entry, not an owner, so it does not trigger the falsifier.
   - Smallest fix: keep the §13 row at C:210, which is the sourced one (S121, S076), and delete the sentences at C:29 and C:147.
7. **Low — the evidence for one anchor is thin.**
   - Pointer: C:27 cites `writing-systems.md:11` for "a writing system: a secondary notation of a language". Line 11 is Daniels's classification rule ("which linguistic unit one basic sign encodes"). It implies writing encodes linguistic units but does not say "secondary".
   - Smallest fix: re-anchor to `writing-systems.md:11` with the cell reworded as "a script encodes units of another language".

## Restatement and hollowness: the strongest counterexamples I tested

- **Paraphrase of an owner:** not found.
  - The owners' sign content totals five lines: `phonetics-phonology.md:201-203`, `syntax-typology.md:99`, `sound-symbolism.md:124`, plus `language-contact.md:105` as a general rule. C's overlap with those lines sits only on §2 and head citation lines.
  - The body (Stokoe/Battison parameters, the village/deaf-community/emerging/homesign typology, community ecology, grammar in space, alternate sign languages, fingerspelling and notation, and calibration) has no counterpart in the corpus. Corpus-wide `rg` shows no other file that holds it.
  - The five owner files are byte-unchanged since base.
- **Gesture ownership grab:** not found as a claim.
  - The head (C:4), the scope line (C:12), §2 (C:37), §3 (C:66), §10 (C:160), §14 (C:219) and §15 (C:223) all hand emblems, posture and proxemics to `adornment-body-codes.md:79`, and the n-gram overlap with adornment is 0.
  - The real defect is finding 1: the unqualified "gesture" row states a rival and wider proposition about gesture.
- **Hollow 227th file:** no.
  - The entry has 15 sections and 52 registered sources, each with the entry in its used-by cell.
  - Its tables carry located claims, with 10 `(to-verify)` marks and 18 labelled heuristics.
  - Hollowness is confined to the five §2 seams in finding 3.

Impacted axis: coverage. Finding 1 also touches the duplicate-authority rule at the adornment seam.

## Verdict

**HOLDS-WITH-FIXES.** No section restates an existing owner's register, so the falsifier at `claims.json:44` is not triggered. Findings 1-3 are medium-severity defects that can be fixed within the entry. Findings 4-7 are low.

Tools installed: none.
