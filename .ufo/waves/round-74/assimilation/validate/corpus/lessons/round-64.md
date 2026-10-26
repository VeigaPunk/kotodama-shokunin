# Round 64 — 2026-10-23 (hyaku run 5, L1 KotodamaR64)

## Round summary

Three claims, base revision `ff30a205c8d23b35f1ac533740121a955a9fda96`
(declaration commit `097c21d`). C (coverage, sourced): a new linguistics entry
`corpus/knowledge/linguistics/language-socialization-and-acquisition.md`
— language socialization and acquisition as culturally organized participation —
supported by 26 new registry rows S718-S743, plus six disposition rows
S744-S749 that carry the round-63 closure's routed defect 7 (rejected
candidates kept as rows with reason and flip). Predicate ACCEPT-C-64: every leg
of `reports/round-64/accept-c.py` prints PASS. O (operability, counter
hardening): `reports/round-64/accept-o.py` pins the seven redirect-edge
properties the round-63 residual CtlORedirectEdge measured unpinned plus a
DRIP fixture separating a wall budget from a per-socket timeout; the unchanged
`tools/reopen-row.py` must pass all of them and each of ten byte-patched mutants
must fail its pinned leg. Predicate ACCEPT-O-64: every leg prints PASS.
Ca (calibration, bookkeeping): the round-63 closure's routed defects 1, 2, 3, 4,
8, 9 and 10 repaired; predicate ACCEPT-CA-64: every leg of
`reports/round-64/accept-ca.py` prints PASS.

Attempt history is part of the record. The inherited attempt-1 state, as read
from its own artifacts, was: working-copy counter revisions and O receipts
uncommitted (`accept-c.py` and `accept-ca.py` modified, `accept-o.py` untracked;
`.ufo/waves/round-64/w2/B2ScribeLesson.md` finding 1,
`.ufo/waves/round-64/w1/RevengerCounter.md` §0), and 30 of 32 row contributions
staged (`.ufo/waves/round-64/stage/report.txt`: `S723 MISSING`, `S740 MISSING`).
Wave 1 re-dispatched the dead row seats; both rows landed and `check-rows.py`
then printed `CHECK-ROWS: 32/32 clean`. Wave 2 falsified and repaired the
remaining rows and revised the three counters. This lesson is assembled by the
wave-2 LessonFinal seat from the wave-1 draft
(`/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeLesson/round-64.md`), the
wave-1 Gate fragment (`.ufo/waves/round-64/w1/ScribeGateQuotes.md`) and the
final staged row artifacts. TBD markers are retained only where the evidence
does not yet exist: final census-end counts, final ACCEPT results, and measured
revisions.

## Gate (rows opened this round; each quote is the anchor quote of that row's own
final `row.txt` artifact, and each disposition row carries its ordinary
re-open/status evidence verbatim. The three rows whose wording could not be
located on the cited URL are annotated as NOT LOCATED rather than presented as
located quotations, per `.ufo/waves/round-64/w1/ScribeGateQuotes.md` D2.)

- S718 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4794163/ | 2026-10-23 | "Lebanese mothers, compared to American mothers, produced more IDS"
- S719 | https://pure.mpg.de/rest/items/item_1094677/component/file_1703379/content | 2026-10-23 | "The evidence summarized in Section 3 revealed that infants attend preferentially to IDS, and in particular to IDS-like prosody (with the aforementioned caveats)."
- S720 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5421641/ | 2026-10-23 | "only in items deemed to be words or to contain canonical syllables that may have made them sound like words with language-specific shapes"
- S721 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9271548/ | 2026-10-23 | "Proto-conversation can be described as a structured, nonlinguistic vocal exchange between infants and their peers or adults"
- S722 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/ | 2026-10-23 | "emphasizes the importance of domain-general processes like novelty, attention, statistical learning, association, competition, and parallel learning"
- S723 | https://www.nottingham.ac.uk/helm/dev-test/ncc_work_in_progress/language_0-5/page_eleven.html | 2026-10-23 | "In overextension, children use a simple word to refer to many different things."
- S724 | https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/11-7-syntax-in-early-utterances/ | 2026-10-23 | "containing mostly content words like nouns and verbs, with few function words and few inflectional morphemes."
- S725 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4450887/ | 2026-10-23 | "typically developing children were more likely to imitate a maternal use of a grammatical morpheme following a corrective recast"
- S726 | https://eric.ed.gov/?id=ED252065 | 2026-10-23 | "the process of acquiring language is deeply affected by the process of becoming a competent member of a society"
- S727 | https://www.cambridge.org/core/journals/language-in-society/article/abs/talking-to-children-in-western-samoa/FCDE86B99916AE58E2870E2A65A852F4 | 2026-10-23 | "organization of turn-taking and procedures for clarification and interpretation are linked to beliefs and expectations"
- S728 | https://press-files.anu.edu.au/downloads/press/n9994/pdf/ch08.pdf | 2026-10-23 | "Kaluli mothers use elema ‘say it like this’ to prompt the children to correct"
- S729 | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0326569 | 2026-10-23 | "Questions, Imperatives, Reading, Singing, Comfort, and Vocal Play were more frequent in the IDS register compared to the ADS register."
- S730 | https://www.psych.mcgill.ca/perpg/fac/genesee/HDBK%20BFLA%20FINAL.pdf | 2026-10-23 | "This chapter focuses on the simultaneous acquisition of two languages from birth, or what is generally referred to as bilingual first language acquisition (BFLA)."
- S731 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/ | 2026-10-23 | "the results from the current study indicated that children's diagnosis did not have an effect on the frequency of intrasentential code-switching."
- S732 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/ | 2026-10-23 | "bilingual children in immigrant households sometimes avoid using the family’s heritage language in favor of the majority language"
- S733 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/ | 2026-10-23 | "High phonological neighborhood density and lexical frequency promoted sign acquisition, even after controlling for iconicity."
- S734 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2614655/ | 2026-10-23 | "The results are consistent with the suggestion that children learn general storytelling skills from adult models."
- S735 | https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf | 2026-10-23 | "The teacher, through her questions and comments, tries to help the children structure and focus their discourse."
- S736 | https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.665092/full | 2026-10-23 | "created stories with the assistance of their caregivers and siblings"
- S737 | https://eric.ed.gov/?id=ED149852 | 2026-10-23 | "A sample was considered an example of verbal play if it incorporated an observable manipulation of the sound, semantics and/or syntax of the language."
- S738 | https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf | 2026-10-23 | "in relation to experts’ advice, as they were explicitly instructed not to introduce the language immediately after meeting the children"
- S739 | https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf | 2026-10-23 | "Based on the data obtained, urban parents in Sleman, Yogyakarta used various forms of address when interacting with their children."
- S740 | https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early (capture https://web.archive.org/web/20210414114152id_/https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early) | 2026-10-23 | "These overgeneralizations suggest that children are not just memorizing the forms in their input, but also generating novel forms from a rule."
- S741 | https://www.scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en | 2026-10-23 | "We know it’s ugly because people tell us it’s ugly."
- S742 | https://files.eric.ed.gov/fulltext/EJ1271032.pdf | 2026-10-23 | "Time was taken every morning so greetings would become what her students did routinely, and that they would be expected from each other."
- S743 | https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857 | 2026-10-23 | "Since this construction has a register specification as “child-directed,”"
- S744 | https://www.dictionary.com/browse/ushanka | 2026-10-23 | NOT LOCATED — tested wording (candidate, not a located quotation): "a traditional Russian fur cap with earflaps that can be tied up on top" — re-test 200 https://www.dictionary.com/browse/khanka?q=ushanka&noredirect=true&mismatchType=misspelling / NOT_LOCATED https://www.dictionary.com/browse/ushanka quote-absent
- S745 | https://www.merriam-webster.com/dictionary/tiara | 2026-10-23 | NOT LOCATED — tested wording (candidate, not a located quotation): "a decorative jeweled or flowered headband or semicircle for formal wear" — re-test 403 https://www.merriam-webster.com/dictionary/tiara / NOT_LOCATED https://www.merriam-webster.com/dictionary/tiara HTTPError
- S746 | https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447 | 2026-10-23 | "Smith-Corona owner's handbook, manual typewriters. 38 p. Add. ti: Owner's handbook for manual typewriters"
- S747 | https://www.britannica.com/topic/mortarboard | 2026-10-23 | NOT LOCATED — the row's anchor names an intended locator and records the failed fetch; it carries no quotation, and none is asserted here — re-test 403 https://www.britannica.com/topic/mortarboard / not applicable
- S748 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html | 2026-10-23 | "Among the honorary crowns bestowed by the Romans for military achievements"
- S749 | https://en.wikipedia.org/wiki/List_of_headgear | 2026-10-23 | "Headgear is worn for many purposes, including protection against the elements, decoration, or for religious or cultural reasons, including social conventions."

Disposition re-open evidence for the six disposition rows (verbatim from each
row's own `TEST` / `TEST2` lines, as the claim-C counter's REJECTS leg
requires the ordinary re-open/status evidence to be recorded in the round-64
lesson Gate):

S744 (rejected) re-open evidence — TEST: 200 https://www.dictionary.com/browse/khanka?q=ushanka&noredirect=true&mismatchType=misspelling ; TEST2: NOT_LOCATED https://www.dictionary.com/browse/ushanka quote-absent
S745 (rejected) re-open evidence — TEST: 403 https://www.merriam-webster.com/dictionary/tiara ; TEST2: NOT_LOCATED https://www.merriam-webster.com/dictionary/tiara HTTPError
S746 (queued) re-open evidence — TEST: 200 https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447 ; TEST2: LOCATED https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447
S747 (rejected) re-open evidence — TEST: 403 https://www.britannica.com/topic/mortarboard ; TEST2: not applicable
S748 (queued) re-open evidence — TEST: 200 https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html ; TEST2: LOCATED https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html
S749 (queued) re-open evidence — TEST: 200 https://en.wikipedia.org/wiki/List_of_headgear ; TEST2: LOCATED https://en.wikipedia.org/wiki/List_of_headgear

Row notes on the Gate, in the order the rows appear:

Note: S744, S745, S747 — **NOT LOCATED**, per the D2 form: their own rows record the
  failure (`TEST:`/`TEST2:` evidence above). S744's tested wording is printed
  above as the *candidate* wording the row tested, not as a located quotation;
  S745's likewise; S747's anchor carries no quotation at all after its
  wave-2 repair (`.ufo/waves/round-64/w2/FixRowS747.md`), so its line asserts
  no wording. The other three disposition rows (S746, S748, S749) located their
  wording on the cited URL and are therefore queued candidates, because the
  round-63 rejection ground no longer holds.
Note: S726 — the row's `VERIFY: LOCATED` line is not reproducible with the locator's
  pinned Firefox UA (eric.ed.gov resets it); a plain GET and the same-page
  capture both serve the quoted abstract claim
  (`.ufo/waves/round-64/w2/B2ReviewRowS726.md`). The quote above is the row's
  content; the LIVE leg does not probe S726 (frozen subset S718, S723, S728,
  S733, S738, S743).
Note: S729 — **re-sourced** in wave 2. The row was Farran, Lee, Yoo & Oller 2016
  (PLOS ONE 11(3):e0151518), the same paper as S718 through a second host; it
  now cites Neer, Brahmbhatt, Walsh & Warlaumont 2025 (PLOS ONE 20(6):e0326569)
  with its own located quote and same-page capture
  (`.ufo/waves/round-64/w2/ReSourceS729.md`). The duplicate-work defect (R64-M5)
  is therefore closed for this pair.
Note: S719, S722, S728, S735, S739, S742 — repaired in wave 2: the caveat is kept
  (S719), the locator names the right section (S722), the secondary account
  stays attributed (S728), the teacher's attempt is not reported as success
  (S735), the anchor is the paper's own Results sentence rather than its
  secondhand introduction (S739), and the one-classroom setting is retained
  (S742). Reports: `.ufo/waves/round-64/w2/FixRowS719.md`,
  `FixRowS722.md`, `FixRowS735.md`, `FixRowS739.md`,
  `FixRowsS728S742.md`.
Note: live re-verification of the 29 rows whose evidence asserts `LOCATED` was
  carried out independently in wave 2: **29/29 located, `mismatched=none`** —
  25 in the live body, and 4 (S726, S727, S737, S740) in the row's own
  same-page archive capture because the live host refused the request
  (`http=000`, `http=429`, `http=000`, `http=403` respectively)
  (`.ufo/waves/round-64/w2/GateFinal.md`, GF-6). S735's quote is
  located under the locator's canonical `pypdf 5.4.0` extractor, not under
  `pdftotext`, which inserts line breaks mid-phrase — the same extraction
  difference the wave-1 fragment recorded (`.ufo/waves/round-64/w1/ScribeGateQuotes.md`
  D5). The three NOT LOCATED rows are the three disposition rows whose own
  rows record the failure; no other row in this Gate is unlocated.
- Length check over all 32 gate quotes with the counter's own normaliser
  (NFKC, casefold, `\W_` -> space), run over the final row artifacts: the range
  is 9 words (S718) to 24 words (S730, S737); every row is inside the counter's
  8-25 window, and the two annotated candidate wordings (S744 14 words, S745
  11 words) are inside the lane's 25-word Gate cap.

## Mistakes

- R64-M1 (class: landing). Attempt-1 dispatched the build waves before the
  pre-dispatch receipts and the counter revisions were committed; the counters
  therefore existed only as working-copy bytes when the wave started. Evidence:
  `.ufo/waves/round-64/w2/B2ScribeLesson.md` finding 1 (the round-64 counter
  scripts are absent from the declared commit), and
  `.ufo/waves/round-64/w1/RevengerCounter.md` §0 (`git ls-tree HEAD
  reports/round-64/` holds accept-c rev0, accept-ca rev0 and claims.json but no
  accept-o.py at all). Wave-2 status: **still open.** All three counters remain
  uncommitted working-copy bytes (`accept-o.py` is still untracked; the others
  are unstaged modifications), and the wave-2 revisions were made in the same
  uncommitted state (`.ufo/waves/round-64/w2/RevCounters.md`). Captured by:
  QUALITY criterion 9 (dry runs checked both ways, receipt committed with the
  declaration). Fix: commit the frozen counters and their pre-dispatch receipts
  with the declaration, then dispatch; a wave must never start against counters
  that exist only in the worktree.
- R64-M2 (class: attribution). The round-63 entry in `corpus/LOG.md` claimed
  that round-62 closure items 5-6 were recorded in R63-M2. R63-M2 is about
  stale instrument pins in a live wave; the r62 items 5-6 are elsewhere.
  Evidence: `.ufo/waves/round-64/w2/B2ExecCaRepair.md` (the correction is
  quoted in the lane's copy: "The prior claim that r62 closure items 5–6 were
  recorded in R63-M2 was incorrect"). Captured by: the CANONLOG leg of
  `reports/round-64/accept-ca.py`, which requires the canonical log to carry
  the round-64 entry and the dispositions. Fix: name the canonical file
  (root `LOG.md`) explicitly, treat `corpus/LOG.md` as the stray round-63 log,
  and keep r62 items 5-7 in the round-64 entry instead of misfiling them under
  an earlier round's mistake id.
- R64-M3 (class: dead seats block assembly). Two row seats (S723
  overextension/underextension, S740 honorifics and keigo) died without
  writing `row.txt`, so 30 of 32 declared rows existed and claim C's statement
  of 26 mined rows could not be met. Evidence:
  `.ufo/waves/round-64/stage/report.txt` ("S723 MISSING", "S740 MISSING") and
  the inherited 30/32 reading of `.ufo/waves/round-64/check-rows.py`.
  Captured by: `check-rows.py` MISSING lines, and the ROWS/APPEND/LIVE legs of
  `accept-c.py` (LIVE's frozen subset contains S723). Wave-2 status: closed.
  Both rows landed in wave 1 (ExecRowS723, ExecRowS740) and the final staged
  set reads `CHECK-ROWS: 32/32 clean` (exit 0) as of the wave-2 assembly. Fix
  (standing): a wave needs a re-dispatch path for a dead row seat that lands
  the row artifact itself, not only a report.
- R64-M4 (class: counter-parsing shape). The counter extracts the **first**
  quoted span of a row's anchor cell, so a curly-quoted section locator ahead
  of the body sentence becomes the "quote": S719 yielded 5 words
  (`quote_words=5 in_order=0`), S738 `in_order=0`, S742 3 words
  (`quote_words=3 in_order=0`), S739 `in_order=2`. The sourcing was sound in
  every case; only the cell shape was wrong. Evidence:
  `.ufo/waves/round-64/w2/B2ReviewRowS719.md`, `B2ReviewRowS738.md`,
  `B2ReviewRowS742.md`, and the `PROBLEMS` lines of
  `.ufo/waves/round-64/stage/report.txt`. Captured by: the ROWS and RESTATE
  legs of `accept-c.py` and `check-rows.py`. Wave-2 status: closed for the
  four rows (the repaired rows put the body sentence in plain double quotes
  first and leave the locator unquoted: `.ufo/waves/round-64/w2/FixRowS719.md`,
  `B2FixS738.md`, `B2FixS739.md`, `B2FixS742.md`). Fix (standing): keep the
  body sentence in plain double quotes first and leave the locator unquoted.
- R64-M5 (class: duplicate work under different URLs). S718 and S729 were the
  same paper (Farran, Lee, Yoo & Oller 2016, PLOS ONE 11(3):e0151518) reached
  through two different live URLs, with the same finding and the same Results
  sentence quoted twice in two phrasings. The LINK leg counts registry lines
  containing a URL string, so a work-level duplicate cannot fail it. Evidence:
  `.ufo/waves/round-64/w1/ReviewerRegistry.md` F2. Captured by: ReviewerRegistry
  (review-only; no counter leg sees work identity). Wave-2 status: **closed.**
  S729 was re-sourced to Neer et al. 2025 (PLOS ONE 20(6):e0326569) with its
  own located quote and capture (`.ufo/waves/round-64/w2/ReSourceS729.md`);
  the overlap connector independently confirmed the two rows are now distinct
  works and warned that the entry must not certify the same comparison twice
  (`.ufo/waves/round-64/w2/OverlapRe.md`). Fix (standing): keep one row per
  work and re-scope or replace the other with a genuinely distinct source.
- R64-M6 (class: stale assembly input). `.ufo/waves/round-64/stage/bullets.json`
  is a second content authority that is older than the row set: it holds 19
  keys and lacks S721, S723, S727, S733, S740, S741 and S743, and its S738,
  S739 and S742 clauses do not match the anchors those rows now carry. Evidence:
  `.ufo/waves/round-64/w1/CriticEntrySweep.md` CE4/CE5 and
  `.ufo/waves/round-64/w1/ConnectorOverlap.md` ("bullets 19 missing ids
  [...]"). Captured by: the RESTATE leg of `accept-c.py` at integration
  (staged wording supplies too few in-order quote words). Wave-2 status:
  **still open**, and now sharper: the stale artifacts still contradict the
  repaired rows (`stage/report.txt:39` still says `S739 PROBLEMS in_order=2`
  against the current anchor; `stage/bullets.json` still carries the
  superseded S739 bullet) — `.ufo/waves/round-64/w2/SupS739.md`. The wave-2
  assembler `.ufo/waves/round-64/integrate-w2.py` reads the row files, not this
  JSON. Fix: assemble from the current row artifacts (via `integrate-w2.py`),
  and treat `stage/bullets.json` and `stage/report.txt` as dead inputs.
- R64-M7 (class: bullet overreach past the quote). Three claim lines state
  more than their anchor supports: S719 drops the quote's own "(with the
  aforementioned caveats)" and asserts a flat infant preference; S737's
  bullet invents a "worldbuilding" outcome the abstract never claims; S735
  turns the teacher's attempt to help into successful scaffolding the source
  expressly allows to fail. Evidence: `.ufo/waves/round-64/w1/ReviewSupportA.md`
  D1, `.ufo/waves/round-64/w2/B2ReviewRowS737.md`,
  `.ufo/waves/round-64/w1/CriticEntrySweep.md` CE2/CE3. Captured by: the blind
  support reviewers (review-only — RESTATE counts words and cannot see the
  overreach). Wave-2 status: closed for S719 and S735 (bullets rewritten to
  keep the caveat and to report the teacher's attempt, not success:
  `.ufo/waves/round-64/w2/FixRowS719.md`, `FixRowS735.md`, re-verified SUPPORTED
  in `.ufo/waves/round-64/w2/SupS735.md`); the S728 attribution and S742
  single-classroom bound were repaired in the same pass
  (`.ufo/waves/round-64/w2/FixRowsS728S742.md`). Fix (standing): keep the
  caveat the source states, or narrow the clause to what the quotation carries.
- R64-M8 (class: instrument and receipt identity). The claim-O counter's
  docstring still read "revision 0" while its inline comments named revisions
  1, 3 and 4, and the declared commit did not contain the counter at all. The
  receipt was also observably partial for most of the wave: at 22:49
  `reports/round-64/telemetry/final-measures-o.txt` was an 1818-byte, 22-leg
  file that ended before MUT, with no verdict line and no exit code (read by
  ReviewerOReceipt). The copy present at authoring time (23:17, 2986 bytes) is
  complete — 23 legs, `MUT PASS … mutants=10`, `ACCEPT-O-64: PASS`, `exit=0` —
  but it still carries no measured-revision line and no counter sha256, so it
  cannot be bound to a revision or to `accept-o.py`'s bytes. Evidence:
  `.ufo/waves/round-64/w1/ConnectorOverlap.md` (counter stamp),
  `.ufo/waves/round-64/w1/RevengerCounter.md` §0,
  `.ufo/waves/round-64/w1/ReviewerOReceipt.md` checks 1 and 4. Captured by: the
  receipt reviewers. Wave-2 status: **partly closed.** The wave-1 executor
  installed a headered, complete 23-leg receipt naming the measured revision,
  the counter sha256 and the tool sha256, and added the three missing declared
  lands `mut-o.txt`, `edge-o.txt`, `control-o.txt`
  (`.ufo/waves/round-64/w1/ExecCounterO.md`); all three counters now carry
  honest revision stamps in their docstrings (C revision 3, Ca revision 2, O
  revision 4). The counters themselves are still uncommitted (R64-M1), and the
  receipts on disk still bind revision-3 bytes, not the revision-4 bytes now in
  the worktree. Fix (standing): a receipt carries the measured revision and the
  counter's sha256 (the round-61 convention), and the counter's header states
  the revision its body implements; a partial run must never be left at the
  receipt path.
- R64-M9 (class: claim text overstates what the counter measures). O declares
  that each of the ten mutants fails **exactly** its pinned leg, but the MUT leg
  launches each mutant with `--only` its pins, so a failure set equal to the
  pins is a property of the selection, not a measurement of exclusivity; m5
  additionally fails EDGE_SCHEMEREL. Evidence:
  `.ufo/waves/round-64/w1/CriticO.md` O-PIN-01 and
  `.ufo/waves/round-64/w1/ReviewerOReceipt.md` check 4. Captured by: CriticO
  and ReviewerOReceipt. Wave-2 status: **partly closed, and the claim text is
  still not repaired.** Revision 4 narrowed the m5 mutation to nonempty
  relative paths only and made the paired run require EDGE_SCHEMEREL to PASS
  while EDGE_SLASHLESS FAILs (`.ufo/waves/round-64/w2/RevCounters.md`), which
  removes the known collateral failure; but `claims.json` still says "exactly
  their pinned leg" (`.ufo/waves/round-64/w2/CriticClaimsJson.md` CJ5), m8 is
  pinned to two legs (GEN+BOUND), and the MUT loop still measures only pinned
  legs, so exclusivity is still not measured for the other nine mutants.
  **Wave-2 closure of the measurement, not of the claim text:** an independent
  EDGE-leg sweep on the repaired bytes (`reports/round-64/telemetry/exactness-sweep-o.txt`,
  sha256 `429d5684…`) shows the claim sentence is not merely unmeasured but
  **false** for two more mutants: m1 (pinned EDGE_SCHEMEREL only) also fails
  EDGE_USERINFO and EDGE_HTTPS, and m2 (pinned EDGE_USERINFO) also fails
  EDGE_MALTARG. So "ten byte-patched mutants each fail exactly their pinned
  leg" is false for at least three of the ten over the EDGE set. The repaired
  bytes pass the frozen predicate (23/23, `ACCEPT-O-64: PASS`, exit 0, receipt
  `reports/round-64/telemetry/final-measures-o-rev4-760ddd4d.txt`); the
  sentence above the predicate does not. The receipt's own scope caveat says
  the same thing: "MUT verifies each mutant FAILs its PINNED leg; it does not
  verify exclusivity". Fix
  (standing): pre-data claim-text revision to what the counter proves (each
  mutant fails its pinned leg), or a full-leg exclusivity leg — without
  weakening the EDGE assertions.
- R64-M10 (class: control vacuity in the calibration counter). The Ca NITS
  leg searched the whole canonical log for the substrings `45`, `47`, `W04`
  and `27`; an appended records-only paragraph containing only the token
  `W04` turned NITS FAIL into PASS with no numeric correction and no
  dependency sentence present. The inherited `dry-run-ca.txt` also prints six
  legs, omitting REVNAMES, so it cannot be cited as seven observed failures.
  Evidence: `.ufo/waves/round-64/w1/CriticCa.md` §1 (before/after runs pasted
  verbatim) and `.ufo/waves/round-64/w1/RevengerCounter.md` §0. Captured by:
  CriticCa's executed records-only control. Wave-2 status: **closed on the
  measured bytes.** Revision 2 scopes NITS to the canonical `## Round 64` LOG
  entry and requires the three contextual old→new associations
  (`47 seat reports landed, not 45`; `W04 covers 27 duplicate-URL rows, not
  just S650/S651`; `ACCEPT-O-63 dry run had 9 FAIL legs … not 6`)
  (`.ufo/waves/round-64/w2/RevCounters.md`). Re-measured at this assembly on
  counter sha256 `7319ff4b9c7eb2cd23f866eb4db62d469a539b8dd99b8326fb6bae8f1cb0d4c5`:
  the base tree still fails all seven legs; a records-only append carrying
  bare tokens `47 / 27 / 9 / W04` and no correction now prints
  `NITS FAIL correction_record=False …`, as does a broader generic-prose
  append. Fix (standing): scope each NITS check to the named round-63
  correction and require each old->new association in its own context, with
  the base-plus-generic-token append as a forcing NITS-FAIL control.
- R64-M11 (class: declared land unowned). `reports/round-64/claims.json`
  names `telemetry/mut-o.txt`, `telemetry/edge-o.txt` and
  `telemetry/control-o.txt` as O lands, but no live seat was tasked to write
  them and none exist in the tree. Evidence:
  `.ufo/waves/round-64/w1/ReviewerOReceipt.md` check 2. Captured by:
  ReviewerOReceipt. Wave-2 status: **closed.** All three receipts were
  produced by the wave-1 executor and audited in wave 2
  (`.ufo/waves/round-64/w2/CriticReceipts.md`, which confirms all ten named
  receipt files exist, the four declared O receipts among them). Fix
  (standing): every declared land needs an owning seat and a receipt, or the
  declaration is corrected before close.
- R64-M12 (class: asserted enactment without enactment). Root `LOG.md` records
  the S687 `mined -> queued` flip as enacted by this round's claim-C land while
  `corpus/SOURCES.md` still carries `mined`; the census's only W03 warning is
  that same row. Evidence: `.ufo/waves/round-64/w1/ScoutLessonRecon.md` item 1
  and `.ufo/waves/round-64/w1/CriticCa.md` §C. Captured by: the APPEND leg of
  `accept-c.py`, which requires S687's status cell to be `queued` in the
  registry. Wave-2 status: **closed in the worktree, open in the index.** The
  registry file on disk now carries `queued` at line 642 (a one-cell diff
  against base `ff30a205`), the base and the git index still carry `mined`, and
  the wave-2 assembler copies existing registry lines and never rewrites
  S687 — so only the commit path keeps the flip
  (`.ufo/waves/round-64/w2/FrontierAudit.md`). Fix (standing): the registry
  edit is the enactment; the log may only say "selected" until the row lands.
- R64-M13 (class: metadata range read as two citations). The entry skeleton's
  metadata line `- source: S718–S743 ...` carries two registered ids, which
  `tools/check-cited-lines.py` reports as MULTI-ID and `accept-c.py`'s ONEID
  leg checks. Evidence: `.ufo/waves/round-64/w2/B2ExecEntry.md` (one
  `MULTI-ID` finding on line 4) and `.ufo/waves/round-64/w1/CriticEntrySweep.md`
  CE1. Captured by: ONEID plus `tools/check-cited-lines.py`. Wave-2 status:
  still open — the entry file itself does not exist yet, so the metadata line
  is still unwritten; and the revision-3 ONEID leg now additionally requires
  every one of S718-S743 to be cited exactly once
  (`.ufo/waves/round-64/w2/RevCounters.md`, forcing control
  `.ufo/waves/round-64/w1/ReviewerCounterC.md` D1), which makes the
  id-free-wording fix mandatory rather than optional. Fix (standing): refer to
  the round's rows in prose without an id range on a cited line; concrete ids
  belong only on their own claim lines.
- R64-M14 (class: environmental access). Several sources refused the
  locator's pinned client string or the plain request on the day: eric.ed.gov
  reset the locator's Firefox UA (S726's `VERIFY: LOCATED` line is not
  reproducible today), PMC served a recaptcha interstitial to a later live
  fetch of S718, the Wayback availability API returned HTTP 429 to several
  seats, and the UC Press article behind S740 answered HTTP 403 with a
  challenge interstitial (its row is anchored on the archived capture, whose
  CDX records carry full bodies). Evidence:
  `.ufo/waves/round-64/w2/B2ReviewRowS726.md`,
  `.ufo/waves/round-64/w1/ReviewSupportD.md` note 1,
  `.ufo/waves/round-64/w2/B2FixS719.md`, `B2FixS738.md`, `B2FixS739.md`,
  `B2FixS742.md`, and the S740 `ACCESS` line. Wave-2 status: still open as a
  standing condition — the safety re-scan re-measured S740's live URL at 403
  and its capture at 200 (`.ufo/waves/round-64/w2/UrlSafetyFinal.md` F2).
  Fix (standing): record the challenge as met and not passed, route to the
  archived capture, and treat a 429 as transient rather than as absence.
- R64-M15 (class: scope wider than the anchored evidence, and tier
  inflation). S721's scope names turn-taking while its quote defines only
  proto-conversation; S739's anchor is the paper's introduction citing Aledo
  (2018), a secondhand general claim, yet the scope claims the paper's own
  Sleman findings at tier A; S747's anchor holds fabricated meta-text rather
  than a quotation; S749 uses kind `community` where the one prior Wikipedia
  row uses `docs`. Evidence: `.ufo/waves/round-64/w1/ReviewerRegistry.md`
  F3-F7, `.ufo/waves/round-64/w1/ReviewSupportC.md` (S739 locator nit).
  Captured by: ReviewerRegistry (review-only). Wave-2 status: **partly
  closed.** S739 was re-anchored to the paper's own Results sentence (tier A
  then supported, confirmed SUPPORTED in
  `.ufo/waves/round-64/w2/SupS739.md`); S747's anchor no longer presents
  invented wording (`.ufo/waves/round-64/w2/FixRowS747.md`); S749's `community`
  kind and S721's scope remain as filed. Still open: the final-row critic
  found three tier inflations and two over-long teaches cells the wave-2
  repair seats did not cover — S721 tier A on a secondary definition, S726
  tier A on an ERIC abstract, S737 tier A on an ERIC abstract, and the teaches
  cells of S723 (44 words) and S740 (45 words) against the ≤25-word rule
  (`.ufo/waves/round-64/w2/CriticRowsFinal.md` RF1-RF5). Fix (standing):
  re-anchor or narrow the scope, and set the tier the quoted evidence actually
  supports.
- R64-M16 (class: locator label wrong, sourcing sound). S722's row places its
  quote under "Section A Continuous Vocabulary Spurt", but the live article
  carries that passage under "New Directions and Next Steps"; the quotation
  itself is verbatim in the body. Evidence:
  `.ufo/waves/round-64/w1/ReviewSupportA.md` D3. Captured by: ReviewSupportA.
  Wave-2 status: **closed.** The locator string was corrected to "New
  Directions and Next Steps, paragraph 35" and the quote re-located on the live
  article (`.ufo/waves/round-64/w2/FixRowS722.md`). Fix (standing): a wrong
  locator is a provenance defect even when the quote is right.
- R64-M17 (class: receipt integrity — the forcing receipt does not exist and
  the receipt on disk is a killed run's fragment). The O counter's own revision
  history names the rev1/rev2 forcing receipt as
  `reports/round-64/telemetry/final-measures-o.txt` at counter sha256
  `bb0c74a486ae53ebc9a09787670020b69a03ef373df68f04fee8a30a827bf280`, but
  that file on disk was an 1818-byte, 22-leg fragment with no MUT section, no
  `ACCEPT-O-64:` verdict line and no `exit=` line — the leftover of an earlier
  run that was killed mid-leg, at a different destination and an earlier
  mtime than the wave-1 executor's own run, so it cannot be that run's
  output. The cited `bb0c74a4…` measurement is therefore not reconstructible
  from the lane, and the file's own name was in use as the canonical O receipt
  while carrying none of the revision it claimed. Evidence:
  `.ufo/waves/round-64/w1/ReviewerCounterO2.md` M3 and LOW-2 (the two
  `dry-run-o` files are byte-identical duplicates of one payload, sha256
  `635a16b0…`), `.ufo/waves/round-64/w1/ReviewerOReceipt.md` check 1 and
  defect 2 (the 22:49 partial "left by an earlier killed run"), and
  `.ufo/waves/round-64/w1/ExecCounterO.md` §7 finding 3 ("the rev1/rev2 forcing
  receipt is not reconstructible and should be recorded as missing"). Captured
  by: ReviewerCounterO2 M3, ReviewerOReceipt, and the wave-2 receipt audit
  (`.ufo/waves/round-64/w2/CriticReceipts.md` R1-R3, which also records that
  `dry-run-ca.txt` prints six legs against seven declared and therefore cannot
  be cited as seven observed failures). Fix (standing): a forcing receipt is
  evidence of the revision that forced it and must exist before the revision
  is declared; name a missing forcing receipt as missing rather than citing a
  path that holds a different run's output; never leave an aborted or
  selected-leg run at a canonical receipt path, and never cite a selected-leg
  run (`--only …`) as an all-legs acceptance result.
  **Wave-2 extension of the same class — one label, two byte streams.** The O
  counter's docstring label stayed "revision 4" across two different byte
  streams: sha `6d9c9354…` (m5 mutant not valid Python — MUT FAIL, 22/23) and
  sha `760ddd4d…` (repaired — 23/23 PASS). Two receipts therefore carry the
  same label "revision 4", one green and one red. The green receipt's own
  header says so explicitly ("NOTE ON LABEL … cite this file by the counter
  sha above, not by the label"). The lesson records the same discipline: a
  revision label is a name, the counter's sha256 is the identity, and a
  receipt must be cited by the bytes it measured.
- R64-M18 (class: revision landed but its own instrument is broken). The O
  counter's revision 4 (m5 narrowed to nonempty relative paths only; unknown
  `--only` selectors exit 2) landed in the worktree, and the selector half
  works — `--only NOSUCHLEG` now prints `ACCEPT_O_INPUT_ERROR unknown --only
  leg(s): NOSUCHLEG` and exits 2. The mutation half does not: rev4's m5
  replacement text is indented one level too deep for the tool's `follow()`
  body, so the patched mutant is not valid Python
  (`IndentationError: unexpected indent`, line 605 of the rebuilt mutant). The
  mutant therefore dies before producing rows, the paired
  `EDGE_SCHEMEREL,EDGE_SLASHLESS` run reports `EDGE_SCHEMEREL FAIL rows=[]`,
  the rev4 isolation check fails, and MUT FAILs. Evidence: the mutant rebuilt
  from the counter's own `MUTANTS` table (ast-parsed, single exact replace)
  is sha256 `795b8d196eec4b64344b39338bf73a3cc6a73c075671702d4b963959a6e6ecb6`
  and fails `python3 -m py_compile`; the live `--only MUT` run on the landed
  bytes prints `MUT FAIL bad=["m5:EDGE_SCHEMEREL isolation=…"] mutants=10` and
  `ACCEPT-O-64: FAIL`, exit 1. Independently reported by
  `.ufo/waves/round-64/w2/RevVerifyO2.md` with the same mutant hash; that seat
  also filed the full 23-leg falsification capture at
  `reports/round-64/telemetry/final-measures-o-rev4.txt` (22 PASS, MUT FAIL,
  `ACCEPT-O-64: FAIL`, exit 1; header names the counter sha `6d9c9354…`
  unchanged before and after the run, the tool sha `c0f10a84…`, the measured
  revision and the run window, and labels itself pre-data falsification
  evidence, not an acceptance receipt) and validated the dedented m5 (sha
  `804c9473…`) separately: with the corrected indentation it yields
  EDGE_SCHEMEREL PASS and EDGE_SLASHLESS FAIL, the behaviour the revision
  intends. Captured
  by: the counter's own MUT leg. Fix: dedent the replacement's `if`/`else` to
  the surrounding block's indentation; a revision's forcing control must be
  re-run against the revision's own bytes before the revision is declared
  good, and the rev4 docstring's sentence ("requires the former to FAIL and
  the latter to PASS") is inverted relative to the code, which requires
  EDGE_SCHEMEREL to PASS. Wave-2 follow-up: a further edit of the same
  revision landed during this assembly (counter sha
  `760ddd4d6d1c0ef1f2c4d0dbd6cd5ef286be1e3b8b2fc5cded2bd6258c08f5a7`, still
  docstring "revision 4"): the m5 replacement is now dedented and the mutant
  rebuilt from it compiles (`m5` sha
  `f04dc0029ed89fc35abd36564907ab2e47c1b44ca0baed4b7528327b5de3e710`), and
  the docstring sentence is corrected to "requires the former to PASS and the
  latter to FAIL"). **Measured after that edit:** a `--only MUT` run on
  counter sha `760ddd4d…` prints `MUT PASS bad=[] mutants=10` with m5's kill
  evidence showing the intended isolation — `m5->EDGE_SCHEMEREL PASS
  rows=[('S2187','REFUSED',1)] … ; EDGE_SLASHLESS FAIL rows=[('S2022',
  'UNREACHABLE',2)] dir_hits=0 root_hits=1 exit=1` — and the verdict line
  `ACCEPT-O-64: PASS`, exit 0; the full 23-leg run on the same bytes prints
  23/23 PASS and `ACCEPT-O-64: PASS`, exit 0, filed at
  `reports/round-64/telemetry/final-measures-o-rev4-760ddd4d.txt`
  (sha256 `fd91552a1d4c83d298fe75a94f8d85dd278f9ae447b40fdc7547564750780f0c`).
  The lesson's general lesson is unchanged: a revision is not good because its
  diff looks right; it is good when its own forcing control is re-run against
  its own bytes — and the first revision-4 bytes were not good in exactly that
  way. (Two receipts now carry the same label "revision 4", one red and one
  green: R64-M17.)
- R64-M19 (class: the acceptance leg reads a ref the wave does not own). The
  claim-C counter's NOHARM leg computes
  `git diff --name-only ff30a205 main -- corpus/knowledge` and requires the
  result to be exactly the new entry's path. The entry landed in the working
  tree during this assembly (81 lines, 7686 bytes, one H1, ten H2, README row
  carrying the topic verbatim), so every content leg passes — FILE, ROWS (26),
  REJECTS (6), ONEID (`citations_exactly_once=True missing=[] duplicates=[]`,
  26 cited lines), RESTATE (26 lines), HOSTS, LINK, APPEND
  (`s687_queued=True base=643 measured=675 +32=True`), SWEEP, and LIVE for the
  frozen subset S718, S723, S728, S733, S738, S743 — but the diff is empty
  because the new file is still untracked (`??` in git status) and the ref
  `main` is the declaration commit `097c21d`. The verdict is therefore
  `ACCEPT-C-64: FAIL`, exit 1, with NOHARM the single failing leg
  (`NOHARM FAIL diff=[]`). Evidence: the run's own output at assembly time,
  and `git rev-parse main` = `097c21d0eba5023cfd38b767fb41d59409eef125` =
  the declaration commit. Captured by: the NOHARM leg itself. Fix: commit the
  land before scoring the counter, and record in the lesson that a working
  tree land cannot satisfy a diff-based leg; this is the same class as R64-M1
  (counters and lands must exist as committed bytes before a wave's evidence
  is measured) and is recorded here because it was observed live.

## Census and counts

Census receipts on disk at assembly time: `reports/round-64/telemetry/census-start.txt`
(29 lines) and `reports/round-64/telemetry/census-wave1.txt` (31 lines: the 29
census lines plus two `#` header lines carrying the command and exit code 0).
Content of both: 27 W04 duplicate-URL rows, 1 W03 row (`S687` mined but
unused), 0 W01, 0 W02, 0 E-codes; lane line `kotodama ok`. A **census-end
receipt does not exist yet** — TBD.

Registry `corpus/SOURCES.md` as measured at assembly time: **675 rows**, 0
malformed rows, tiers **A=421 B=244 C=10**, statuses **mined=592 queued=61
rejected=22**, no duplicate ids, no enum violations or tier inflation. The
land landed during this assembly: the count moved from the base 643 (tiers
A=406 B=228 C=9, statuses mined=566 queued=58 rejected=19) to 675 by exactly
+32 rows (26 mined S718-S743 plus six disposition rows S744-S749). The staged
row set in `.ufo/waves/round-64/rows/` reads tiers A=15 B=16 C=1, kinds
paper=21 book=5 docs=5 community=1, statuses mined=26 rejected=3 queued=3, and
`.ufo/waves/round-64/check-rows.py` printed `CHECK-ROWS: 32/32 clean` (exit 0).

The entry `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`
now exists: **81 lines, 7686 bytes**, one H1, ten H2, no H3, a `- topic:` line,
and a README row carrying that topic verbatim. The corpus now holds **238**
knowledge entries, of which **30** are linguistics. The wave-2 frontier audit
measured 0 filename owners and 0 topic-line owners of the topic before the
land (`.ufo/waves/round-64/w2/FrontierAudit.md`).

Final results — filled by L1 from committed evidence (measured revision
`95c9194ef938e1338b2af894086a46e8b8677ee2`, the round-64 claim-C land; parent
`6f3e0b24f1992d2d3d6ee96cfb1591f387418dc7`):

- census receipts: end census `reports/round-64/telemetry/census-end.txt`
  prints `kotodama ok` with **exit 0** (2026-10-24); registry **675 rows**
  (A=421 B=244 C=10; mined=592 queued=61 rejected=22); start census
  `census-start.txt`/`census-wave1.txt` printed 643 rows, exit 0.
- ACCEPT-C-64, ACCEPT-O-64, ACCEPT-CA-64 results: **all three PASS** at
  `95c9194e` — C 11/11 (`final-measures-c.txt`, NOHARM `diff=[entry]`, LIVE
  subset 6/6), O 23/23 (`final-measures-o.txt`, counter rev5, MUT green with
  m5 isolation `EDGE_SCHEMEREL PASS / EDGE_SLASHLESS FAIL`), Ca 7/7
  (`final-measures-ca.txt`). Exit 0 each.
- measured revisions of the three counters and of every receipt: final
  counter shas C `979050ce…` (rev3), O `cdee063e…` (rev5), Ca `d0787979…`
  (rev2); receipt → revision map: final-measures-c.txt → 95c9194e;
  final-measures-o.txt → 95c9194e (counter cdee063e, tool c0f10a84 byte-equal
  to base ff30a205); final-measures-ca.txt → 95c9194e; census-end.txt →
  95c9194e; controls-c.txt → control run in a scratch copy (stub FAILs
  ROWS/RESTATE/ONEID/APPEND, exit 1); red receipts preserved:
  final-measures-o-rev4.txt (FAIL, m5 IndentationError) and the rev3/rev5
  named variants.

Working-tree observations at assembly time, recorded as observations and not as
acceptance results:

- `reports/round-64/accept-c.py` sha256
  `979050ce21fa01758c075745b08bf3ecf7d6e73baad543a1df83f666ecc5de2b`
  (docstring "revision 3"): a full run after the land prints FILE PASS
  (81 lines, h1=1, h2=10, h3=0, topic=True), ROWS PASS (26 checked),
  REJECTS PASS (6 checked), ONEID PASS with `citations_exactly_once=True
  missing=[] duplicates=[]` and `cited_lines=26`, RESTATE PASS (26 lines),
  HOSTS PASS, LINK PASS, APPEND PASS (`s687_queued=True base=643
  measured=675 +32=True`), SWEEP PASS (`topic_row=True`), LIVE PASS for the
  frozen subset S718, S723, S728, S733, S738, S743 — and **NOHARM FAIL
  `diff=[]`**, so the verdict is `ACCEPT-C-64: FAIL`, exit 1. The NOHARM leg
  compares `git diff --name-only ff30a205 main -- corpus/knowledge` against the
  single new entry; the entry exists in the worktree but is not committed on
  `main` (it is still `??` in git status), so the diff is empty. This is a
  commit-state observation, not a defect of the landed content: the leg passes
  once the entry is committed on `main`.
- `reports/round-64/accept-ca.py` sha256
  `d0787979ae4e318c4a7cde4385dd2b2e36890f8e258b3733cc1a6e980533f917`
  (docstring "revision 2"): a full run prints all seven legs PASS and
  `ACCEPT-CA-64: PASS`, exit 0 — against uncommitted `LOG.md`, `SCORECARD.md`,
  `corpus/LOG.md` and an untracked `reports/round-63/telemetry/revisions.txt`,
  so this PASS is not bound to committed bytes and must be re-run post-commit.
  Re-measured forcing controls on these bytes: the base tree still fails all
  seven legs, and both records-only appends (bare tokens `47 / 27 / 9 / W04`
  without a correction; and a broader generic-prose append) now print
  `NITS FAIL correction_record=False record_exact=False …`, so the revision-2
  NITS no longer flips on a generic append. The leg now also requires the
  correction record to match the affirmative sentence exactly (`record_exact`).
  (An earlier revision-2 byte set was briefly non-runnable during the
  revision pass — `NameError: name 'r64_log' is not defined` at
  `accept-ca.py:157` — recorded here as a mid-revision observation, not as a
  defect of the delivered file. The earlier byte set
  `7319ff4b9c7eb2cd23f866eb4db62d469a539b8dd99b8326fb6bae8f1cb0d4c5` showed
  the same control outcome.)
- `reports/round-64/accept-o.py` — the counter bytes moved twice during this
  assembly, both times inside revision 4. On sha `6d9c9354…` the full 23-leg
  run printed 22 PASS legs and **MUT FAIL** (`bad=["m5:EDGE_SCHEMEREL
  isolation=…"]`), so the verdict was `ACCEPT-O-64: FAIL`, exit 1 — the
  revision-4 m5 mutant was not valid Python (R64-M18); that falsification
  capture is filed at `reports/round-64/telemetry/final-measures-o-rev4.txt`
  (4203 B; header names the counter sha `6d9c9354…`, the tool sha
  `c0f10a84…`, the measured revision and the run window, and labels itself
  "pre-data falsification evidence, NOT an acceptance receipt"). The current
  bytes are sha `760ddd4d6d1c0ef1f2c4d0dbd6cd5ef286be1e3b8b2fc5cded2bd6258c08f5a7`
  (docstring "revision 4"), whose m5 replacement is dedented and whose
  rebuilt mutant compiles (sha `f04dc002…`); `--only NOSUCHLEG` on this
  revision exits 2 with `ACCEPT_O_INPUT_ERROR`. **The all-legs 23-leg
  acceptance measurement on these bytes exists**:
  `reports/round-64/telemetry/final-measures-o-rev4-760ddd4d.txt` (sha256
  `fd91552a1d4c83d298fe75a94f8d85dd278f9ae447b40fdc7547564750780f0c`) records
  23/23 legs PASS, `MUT PASS bad=[] mutants=10`, `ACCEPT-O-64: PASS`, exit 0,
  with a header naming the counter sha `760ddd4d…` (unchanged before and after
  the run), the tool sha `c0f10a84…`, the measured revision, the run window
  and — explicitly — the note that the docstring label is still "revision 4"
  although the earlier revision-4-label bytes failed; the receipt must be
  cited by the counter sha, not by the label. Two caveats travel with that
  receipt: it is a working-tree measurement against uncommitted counter bytes,
  and its own scope caveat states that MUT verifies each mutant FAILs its
  pinned leg but not exclusivity (R64-M9, R64-M17).
  `reports/round-64/telemetry/final-measures-o.txt` (3847 B) remains the
  complete **revision-3** receipt: 23 legs in declared order, all PASS, the
  full ten-mutant kill list, `ACCEPT-O-64: PASS`, `exit=0`, header naming
  measured revision `b7d22703…`, counter sha `c27a9fef…`, tool sha
  `c0f10a84…`. It is evidence for revision 3 only and must not be cited as a
  revision-4 measurement.

Correction (round 65, R6): R64-M12's “closed in the worktree, open in the index” status sentence is a pre-land snapshot. The S687 `mined -> queued` flip was committed in `95c9194ef938e1338b2af894086a46e8b8677ee2`; at that revision the flip is committed, not open in the index.
