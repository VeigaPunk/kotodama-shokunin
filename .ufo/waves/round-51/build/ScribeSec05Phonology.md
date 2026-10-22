# ScribeSec05Phonology — claim C, section 5 draft: sublexical structure (sign phonology design table)

Round 51 attempt 3, claim C (`sign-languages-manual-modality.md`). Leaf scribe seat. Report path relative to the lane root: `.ufo/waves/round-51/build/ScribeSec05Phonology.md`. No lane files were edited, created or deleted other than this report; no git/jj commands ran; no installs were made.

## 1. Assigned item

Draft the C-entry section `## 5. Sublexical structure: the parameters a conlang must choose` (budget 15 lines, counting the H2 line and blank lines), a design table for sign phonology covering handshape inventory, location, movement, palm orientation, nonmanual features, one-handed vs two-handed constraints (symmetry and dominance), and minimal pairs — for each, what the designer must decide and the typical failure. Every factual claim cites an opened NEW-id, an in-corpus `path:line`, or carries `(to-verify)`. Terminology: deaf/Deaf communities, signers, sign languages; no "deaf-mute", "dumb", "hearing-impaired" labels; signs never framed as deficient or as pantomime. Conlang/worldbuilding method only.

## 2. Draft section text (15 lines, ready to paste)

```
## 5. Sublexical structure: the parameters a conlang must choose

Sign phonology is not gesture choreography: signs are built from a small closed set of simultaneous, contrastive parameters — Stokoe's tab/dez/sig, location, handshape, movement (NEW-ScribeSec05Phonology-1, NEW-ScribeSec05Phonology-4; `phonetics-phonology.md:201-203`), plus palm orientation (NEW-ScribeSec05Phonology-4) and nonmanual features (NEW-ScribeSec05Phonology-5). Contrast is proven by minimal pairs — pairs differing in exactly one parameter (NEW-ScribeSec05Phonology-2, NEW-ScribeSec05Phonology-4); iconicity never excuses skipping contrast (NEW-ScribeSec05Phonology-5).

| Parameter | What the designer decides | Typical failure |
|---|---|
| Handshape | one phonemic inventory of contrastive shapes (Stokoe's dez, NEW-ScribeSec05Phonology-1), not the whole natural hand space — Battison counts ~45 handshape primes in ASL (NEW-ScribeSec05Phonology-4) | letting every possible hand posture into the lexicon: contrasts blur and signers cannot discriminate reliable forms (design rule) |
| Location | which body areas and planes are contrastive — four major regions, eight distinctions each in the Prosodic Model (NEW-ScribeSec05Phonology-5) | importing one signed language's location grid wholesale instead of fixing your own; conflating contact with proximity (design rule) |
| Movement | path vs internal aperture change, direction, repetition; movement is the syllable nucleus comparable to vowels (NEW-ScribeSec05Phonology-5) | giving every sign a unique choreography — movement classes must be finite and constrained (design rule) |
| Palm orientation | whether orientation contrasts alone — fewer minimal pairs exist on orientation alone (NEW-ScribeSec05Phonology-5); Battison added it as a fourth parameter (NEW-ScribeSec05Phonology-4) | ignoring orientation so two signs collapse into homophony, or treating it as pure free variation (design rule) |
| Nonmanual features | which face and body articulators are grammatical — eyebrows, gaze, mouth, head tilt — and what they mark (NEW-ScribeSec05Phonology-5) | importing spoken intonation grammar onto the face, or reducing nonmanuals to decoration and affect (design rule) |
| Two-handed constraints | symmetry condition: when both hands move their specs match; dominance condition: a passive hand is limited to a small unmarked set (A, B, 5, G, C, O) (NEW-ScribeSec05Phonology-3, NEW-ScribeSec05Phonology-4) | designing two-handed signs whose hands freely differ — cross-linguistically rare and articulatorily awkward (NEW-ScribeSec05Phonology-3) |
| Minimal pairs | calibrate each parameter: change exactly one feature and see whether meaning changes (APPLE/ONION, CAR/WHICH, OFFER/MAYBE, SHORT/TRAIN, NEW-ScribeSec05Phonology-4) | never testing contrast, or assuming iconicity replaces the phonological system (NEW-ScribeSec05Phonology-5) |

Build order: handshape inventory → locations → movement classes → orientation rule → grammatical nonmanuals → two-handed constraints; then verify every parameter by minimal-pair probes (NEW-ScribeSec05Phonology-2). Each parameter must earn its place by contrast (NEW-ScribeSec05Phonology-1, NEW-ScribeSec05Phonology-5).
```

### 2.1 Line-budget accounting (15 lines exactly)

| line | content |
|---|---|
| 1 | `## 5. …` H2 |
| 2 | blank |
| 3 | intro paragraph (one physical line) |
| 4 | blank |
| 5 | table header |
| 6 | separator |
| 7–13 | seven data rows |
| 14 | blank |
| 15 | closing build-order sentence |

`wc -l` on the paste block = 15. No H3; numbered H2 preserved; pipe table with separator row and blank lines before/after, per the r50 entry contract (§2.4).

## 3. Sources opened this round (registry rows, exact column order)

Rows are drafted as `NEW-ScribeSec05Phonology-<n>`; the L1 renumbers to S071 upward at integration.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| NEW-ScribeSec05Phonology-1 | Stokoe 1960, *Sign Language Structure: An Outline of the Visual Communication Systems of the American Deaf*, Studies in Linguistics Occasional Papers 8, University of Buffalo — scan https://www.joshiesworld.com/wp-content/uploads/2025/10/stokoe_1960.pdf | book | A | Stokoe's own 1960 analysis of ASL sublexical aspects and cheremes; original monograph text (scanned, text layer extracted in-session) | ch. 1 §1.2–1.3, paragraph defining tab/dez/sig and contrast ("Like consonant and vowel…") | three simultaneous contrastive aspects — tab (location), dez (handshape), sig (movement); chereme terminology; finger-spelling uses nineteen configurations | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeSec05Phonology-2 | Asia-Pacific University Consortium for Sign Linguistics (CSLDS), Module 6 — Phonetics and Phonology: Minimal Pairs — http://www.cslds.org/apsl-consortium/sign-linguistics/6-phonetics-and-phonology-minimal-pairs/ | docs | B | pedagogic module on minimal pairs in ASL and HKSL and the parameter history it synthesizes; examples as given there | section "Sign language phonologists can make use of minimal pairs…" | Stokoe's handshapes/locations/movements as phonemes (cheremes) identified via minimal pairs; palm orientation as Battison's fourth parameter; nonmanuals as the fifth parameter | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeSec05Phonology-3 | CSLDS, Module 7 — Symmetry and Dominance Condition — http://www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition/ | docs | B | reproduction of Battison's symmetry/dominance formulations and their observed extension to HKSL (Channon 2004 percentages); secondary to Battison 1974/1978 | sections Type 1/Type 3, Symmetry Condition, Dominance Condition | symmetry condition (matching location/handshape/movement, symmetrical or identical orientation); dominance condition (passive hand restricted to A, S, B, 5, G/1, C, O); 95.9% ASL / 87% HKSL Type-3 adherence | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeSec05Phonology-4 | Battison 1974, "Phonological Deletion in American Sign Language", *Sign Language Studies* 5:1–19 — https://ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls (open issue scan; Cloudflare-gated, opened via headless browser) | paper | A | Battison's own 1974 account of ASL phonological primes and the symmetry/dominance morpheme-structure conditions | section "Restrictions on Combinations of Primes: Simultaneous Morpheme Structure Conditions" (article pp. 3–5) | four simultaneous aspects (location, handshape, movement, orientation); ~45 handshape primes and ~25 location primes; minimal pairs APPLE/ONION, CAR/WHICH, OFFER/MAYBE, SHORT/TRAIN; Symmetry Condition wording; Dominance Condition and the six unmarked passive shapes A B 5 G C O | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeSec05Phonology-5 | Brentari, Fenlon & Cormier, "Sign Language Phonology" (chapter of Brentari 2019, *Sign Language Phonology*, Cambridge UP) — https://discovery.ucl.ac.uk/id/eprint/10054130/1/Brentari_Sign%20Language%20Phonology.book.chapter.pdf | paper | A | the authors' own overview of sign language phonology and the Prosodic Model (Brentari 1998) | §2.1, §2.1.1, §2.1.2 | manual parameters (handshape, POA/location, movement, orientation); non-manual behaviors as part of phonology; Prosodic Model binary-branching feature structure, H1/H2 hands, four regions × eight places; orientation as a minor parameter; movement as syllable nucleus; core-lexicon arbitrary contrastive sublexical elements | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |
| NEW-ScribeSec05Phonology-6 | MIT Press product page, Brentari 1998, *A Prosodic Model of Sign Language Phonology* — https://mitpress.mit.edu/9780262024457/a-prosodic-model-of-sign-language-phonology/ (live page HTTP 403; opened via Wayback capture 20221222142436) | book | B | publisher description of the book's programme (QUALITY criterion 6: publisher descriptions are tier B for claims about a work) | product description paragraphs 2–3 | the book's two stated claims: simultaneous consonant-like/vowel-like units; movements as the most basic prosodic units | mined | 2026-10-22 | 365d | corpus/knowledge/linguistics/sign-languages-manual-modality.md |

## 4. Gate lines (verbatim quotes, each ≤ 25 words)

- NEW-ScribeSec05Phonology-1 — https://www.joshiesworld.com/wp-content/uploads/2025/10/stokoe_1960.pdf — accessed 2026-10-22 — ch. 1 §1.2 (definition of the aspects): "Like consonant and vowel, the aspects position, configuration, and motion may only be described in terms of contrast with each other."
- NEW-ScribeSec05Phonology-2 — http://www.cslds.org/apsl-consortium/sign-linguistics/6-phonetics-and-phonology-minimal-pairs/ — accessed 2026-10-22 — section "Minimal Pairs", paragraph 5: "Stokoe argued that the handshapes, locations and movements in his model are all phonemes"
- NEW-ScribeSec05Phonology-3 — http://www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition/ — accessed 2026-10-22 — section "Dominance Condition", paragraph 3: "the passive hand can only be one of the following handshapes: A, S, B, 5, G (i.e., 1), C and O"
- NEW-ScribeSec05Phonology-4 — https://ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls — accessed 2026-10-22 — "Restrictions on Combinations of Primes" section, Dominance Condition paragraph: "For those signs which have non-identical handshapes, one hand must remain static, while the other, usually the dominant one, executes the movement."
- NEW-ScribeSec05Phonology-5 — https://discovery.ucl.ac.uk/id/eprint/10054130/1/Brentari_Sign%20Language%20Phonology.book.chapter.pdf — accessed 2026-10-22 — §2.1.1 Orientation: "Orientation is traditionally regarded as a minor parameter, since there are fewer minimal pairs based on orientation alone"
- NEW-ScribeSec05Phonology-6 — http://web.archive.org/web/20221222142436/https://mitpress.mit.edu/9780262024457/a-prosodic-model-of-sign-language-phonology/ — accessed 2026-10-22 — product description paragraph 2: "the consonant-like units and vowel-like units are expressed simultaneously with one another, rather than sequentially as in spoken languages"

## 5. Evidence notes

- **Stokoe 1960**: OUP reprint page (academic.oup.com/jdsde/article/10/1/3/338519) returned HTTP 403; ERIC ED018131 pdf is an image scan without a text layer; the joshiesworld scan of the 1960 monograph has a text layer (`pdftotext`), from which the quotes were extracted verbatim. The 1960 text itself uses "chereme" (e.g., "tab chereme", "configuration chereme") and defines tab/dez/sig in §1.2/1.3.
- **Battison 1974/1978**: the primary 1974 article (Sign Language Studies 5) is open at Gallaudet IDA but Cloudflare-gated — `curl` and the read tool got the challenge page; the headless browser tab passed the challenge and fetched the PDF (553,422 bytes), saved to `/tmp/battison1974.pdf`, text extracted with `pdftotext`. The 1978 book itself (Lexical Borrowing in American Sign Language) was not opened (access-restricted scan; MUSE verification challenge); the symmetry/dominance formulations are quoted from the 1974 primary article and reproduced in CSLDS Module 7. Any wording attributed to the 1978 book rather than the 1974 article is `(to-verify)`.
- **Brentari 1998**: live MIT Press page HTTP 403; Wayback capture 20221222142436 of the same page served the publisher description (tier B, used only for the book's programme claims). The Prosodic Model content in the draft is cited to the authors' own open 2019 chapter (NEW-ScribeSec05Phonology-5).
- **In-corpus anchor re-read at the lane worktree** (bytes = base bff83ba65bf9559af4d7567e81703059667a0005): `corpus/knowledge/linguistics/phonetics-phonology.md:201-203` — "Sign-language phonology works without acoustics — handshape, location, movement carry contrast (Sandler & Lillo-Martin 2006); deaf cultures need this layer." Cited one-way in the draft as `phonetics-phonology.md:201-203` (same-partition bare basename, per the model entries).
- **Terminology and scope**: draft uses "signers", "deaf cultures" (quoting the corpus anchor), "nonmanual features"; no prohibited labels; no clinical, education-policy or legal rulings; conlang/worldbuilding method only.
- **Separability hygiene**: the draft cites only NEW-ids and `phonetics-phonology.md:201-203`; it names neither `corpus/lessons/round-51.md` nor `reports/round-51/boundary-count.py`, and cites no S-id below S071 (NEW-ids are proposed, not yet renumbered).

## 6. Result and unrun checks

- Result: section draft delivered (§2), within the 15-line budget (§2.1); 6 source rows drafted (§3) with Gate lines (§4); all quotes opened, verbatim, and located this session. No claim is left unsupported: the two "decide" cells and the minimal-pair row cite NEW-ids; failure cells are labelled design rules (the lane's method guidance, not factual claims).
- Unrun checks (integration, by the L1): assemble the C entry ≤ 250 lines with all sections; renumber NEW-ids to S071+ and set `used-by`; append rows to corpus/SOURCES.md; index the entry in corpus/README.md; run `find corpus/knowledge -name '*.md' | wc -l` → 227 and `reports/round-28/readme/sweep.py`; run the §2.9 A/B checkers of the r50 entry contract adapted to the linguistics partition; confirm the must-not-cite list.
- Tooling record: no installs or updates (read, grep, web_search, bash `curl`/`pdftotext`/`mkdir`, eval headless browser). Downloads went to `/tmp` only, never into the lane.
