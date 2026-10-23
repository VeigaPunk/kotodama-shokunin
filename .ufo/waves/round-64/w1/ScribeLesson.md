# ScribeLesson — round-64 lesson draft (claim C/O/Ca, wave 1)

Axes: **coverage** (the round's lessons must carry every opened row with its
located quote), **operability** (the draft must state commands and outcomes, not
summaries), **calibration** (mistake rows must name class · evidence ·
captured-by · fix and must not upgrade an unobserved check into a pass).

## Behavior and deliverables

- Drafted `corpus/lessons/round-64.md`, four headings modelled on
  `corpus/lessons/round-63.md` (`## Round summary`, `## Gate`, `## Mistakes`,
  `## Census and counts`), at
  `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeLesson/round-64.md`.
  **It is a scratch draft: this seat did not write `corpus/lessons/round-64.md`
  in the lane.** The full text is appended below so L1 can commit it after
  filling the TBD markers.
- Gate: one line per new registry row S718-S749 (32 lines), each carrying URL,
  `2026-10-23`, and the anchor quote copied from that row's `ROW`/`VERIFY`
  content; disposition rows S744-S749 carry their re-test output.
- Mistakes: 16 rows (R64-M1 … R64-M16), each with class, verbatim evidence
  pointer, captured-by and fix. M1/M2/M3 are the three the assignment named;
  M4-M16 were found in the w1/w2 seat reports.
- Census and counts: measured base census, staged-row histogram, and explicit
  `TBD` markers for post-land counts and acceptance results.

## Gates (exact commands and outcomes)

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
$ python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows
... S749 OK
CHECK-ROWS: 32/32 clean
exit=0
```

```
$ awk -F'|' '/^\|[[:space:]]*S[0-9]+[[:space:]]*\|/ {c++} END{print c}' corpus/SOURCES.md
643
$ awk -F'|' '/^\|[[:space:]]*S[0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++; s=$9; gsub(/[[:space:]]/,"",s); m[s]++} END{...}' corpus/SOURCES.md
tier A=406 tier B=228 tier C=9
status mined=567 status queued=57 status rejected=19
$ find corpus/knowledge -name '*.md' | wc -l      -> 237
$ ls corpus/knowledge/linguistics/*.md | wc -l    -> 29
$ git diff --quiet ff30a205c8d23b35f1ac533740121a955a9fda96 -- corpus/SOURCES.md
(exit 0 — registry unchanged vs base)
```

Staged-row histogram, computed from the 32 `row.txt` files with the counter's
own cell split:

```
rows: 32   tier: {'A': 18, 'B': 13, 'C': 1}   status: {'mined': 26, 'queued': 3, 'rejected': 3}
```

Quote-length check over all 32 anchors using the counter's normaliser (NFKC,
casefold, `\W_` -> space): min 9 (S718), max 25 (S737); every row inside 8-25.
That script is `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeLesson/` scratch
only; the gate block it produced is `gate-block.txt` beside the draft.

Census receipts read, not rerun: `reports/round-64/telemetry/census-wave1.txt`
(exit 0, 29 census lines byte-identical to
`reports/round-63/telemetry/census-end.txt`, plus two `#` header lines) and
`reports/round-64/telemetry/census-start.txt`. `reports/round-64/telemetry/`
holds only: census-start, census-wave1, dry-run-c, dry-run-ca,
dry-run-o-baseline-copy, dry-run-o, final-measures-o.

## Findings

1. **Both dead rows landed during this seat.** `ScribeRowS723` and
   `ScribeRowS740` were absent when the assignment was handed out and are
   present now (`S723` written 23:04 by ExecRowS723, `S740` written 23:15 by
   ExecRowS740). `check-rows.py` moved from the inherited 30/32 to
   `CHECK-ROWS: 32/32 clean` (exit 0). The draft records the S723/S740 death as
   R64-M3 and keeps no TBD for them.
2. **S740 is anchored on an archive capture, not the live page.** The live UC
   Press URL returned HTTP 403 with a Cloudflare "Just a moment…" interstitial
   (the seat's `ACCESS` line records both the block and the CDX full-body
   captures); the quoted sentence is located on capture `20210414114152`. The
   Gate line says exactly that. No challenge was passed.
3. **S726's `VERIFY: LOCATED` is not reproducible today** (eric.ed.gov resets
   the locator's pinned Firefox UA; `.ufo/waves/round-64/w2/B2ReviewRowS726.md`).
   The Gate carries the row's quote and a row note saying so; the LIVE leg does
   not probe S726.
4. **Three disposition rows carry wording that does not locate** (S744
   `NOT_LOCATED … quote-absent`, S745 `NOT_LOCATED … HTTPError`, S747 403 with
   no article). The Gate prints them as *tested wording* and never as located
   quotations — a located-quote claim for those rows would be false.
5. **Defects recorded from the seniority of seat reports, not repaired here**:
   the `accept-o.py` mutant-exclusivity overstatement (m5 also fails
   EDGE_SCHEMEREL, `.ufo/waves/round-64/w1/CriticO.md` O-PIN-01); the Ca NITS
   vacuity (a records-only append holding only the token `W04` flips NITS to
   PASS, `.ufo/waves/round-64/w1/CriticCa.md` §1); the missing declared O lands
   `mut-o.txt`/`edge-o.txt`/`control-o.txt`
   (`.ufo/waves/round-64/w1/ReviewerOReceipt.md` check 2 — re-verified absent by
   this seat's `ls` of `reports/round-64/telemetry/`); the S718/S729 duplicate
   work (`.ufo/waves/round-64/w1/ReviewerRegistry.md` F2); the stale
   `stage/bullets.json` (19 keys, missing S721/S723/S727/S733/S740/S741/S743).
   Each is a mistake row in the draft with its proposed pre-data fix. **No
   frozen counter leg was edited or weakened by this seat.**
6. **The O receipt is complete in the working tree but unbound.** At authoring
   time `reports/round-64/telemetry/final-measures-o.txt` (23:17, 2986 bytes)
   ends `MUT PASS bad=[] mutants=10`, `ACCEPT-O-64: PASS`, `exit=0` over 23 legs,
   yet carries no measured-revision line and no counter sha256 (an earlier 22:49
   copy was a 22-leg partial). The draft records this in R64-M8 and files the
   acceptance result as a working-tree observation, not a committed one.

## Touched surfaces

- Scratch (only): `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeLesson/`
  — `round-64.md` (the lesson draft) and `gate-block.txt` (the generated gate
  lines).
- Lane: this report only, `.ufo/waves/round-64/w1/ScribeLesson.md`.
- Not touched: `corpus/` (no lesson, no registry, no entry), any counter,
  `LOG.md`, `SCORECARD.md`, the git/jj index, the fleet repo, sibling repos.
  No commit, no push, no deploy.

## Artifacts and tooling

- `.ufo/waves/round-64/w1/ScribeLesson.md` — this report (lane; untracked).
- `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeLesson/round-64.md` — the
  lesson draft (scratch; 307 lines; byte-identical to the copy embedded below).
- `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ScribeLesson/gate-block.txt` — the
  generated 32-line Gate fragment.
- Tooling: none installed or upgraded. Used system `python3`, `awk`, `git`
  (read-only) and `diff`. No pacman transaction was attempted.

## Out of scope / blocked work

- Filling the TBD markers (post-land registry/entry counts, final census, the
  three acceptance results, entry bytes and README index row) — L1's job from
  committed evidence; this seat has no committed evidence for them.
- Repairing defects 5 above (claims.json text, Ca NITS scope, mut-o/edge-o/
  control-o ownership, S718/S729 duplication, stale bullets.json) — recorded,
  not enacted.
- Re-fetching sources for the Gate: the quotes are copied from row artifacts and
  checked against each row's own `VERIFY`/`TEST` lines; independent re-opening
  belongs to the reviewer/support seats and is cited, not repeated.
- No tool was installed or upgraded (nothing needed; system `python3`, `awk`,
  `git` read-only). Pacman guard observed.

## Lesson draft (full text, for L1 to commit)

# Round 64 — 2026-10-23 (hyaku run 5, L1 KotodamaR64)

## Round summary

Three claims, base revision `ff30a205c8d23b35f1ac533740121a955a9fda96`
(declaration commit `097c21d`). C (coverage, sourced): a new linguistics
entry `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`
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
This wave re-dispatched the dead row seats (both rows landed, and
`check-rows.py` then printed `CHECK-ROWS: 32/32 clean`). This lesson is authored
by the wave-1 ScribeLesson seat; the counts and acceptance results below are
left as TBD markers for L1 to fill from committed evidence.

## Gate (rows opened this round; each quote copied from its row artifact's own
`ROW`/`VERIFY` content, and each disposition row carries its ordinary
re-open/status evidence verbatim. This seat copied and re-checked the artifacts;
it did not re-fetch the sources — where a `VERIFY` line is not reproducible today
the row note after the list says so.)

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
- S729 | https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518 | 2026-10-23 | "with the Lebanese mothers using more IDS Utterances per Minute across both Registers than the American mothers"
- S730 | https://www.psych.mcgill.ca/perpg/fac/genesee/HDBK%20BFLA%20FINAL.pdf | 2026-10-23 | "This chapter focuses on the simultaneous acquisition of two languages from birth, or what is generally referred to as bilingual first language acquisition (BFLA)."
- S731 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8608171/ | 2026-10-23 | "the results from the current study indicated that children's diagnosis did not have an effect on the frequency of intrasentential code-switching."
- S732 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5966288/ | 2026-10-23 | "bilingual children in immigrant households sometimes avoid using the family’s heritage language in favor of the majority language"
- S733 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709/ | 2026-10-23 | "High phonological neighborhood density and lexical frequency promoted sign acquisition, even after controlling for iconicity."
- S734 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2614655/ | 2026-10-23 | "The results are consistent with the suggestion that children learn general storytelling skills from adult models."
- S735 | https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf | 2026-10-23 | "The teacher, through her questions and comments, tries to help the children structure and focus their discourse."
- S736 | https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.665092/full | 2026-10-23 | "created stories with the assistance of their caregivers and siblings"
- S737 | https://eric.ed.gov/?id=ED149852 | 2026-10-23 | "A sample was considered an example of verbal play if it incorporated an observable manipulation of the sound, semantics and/or syntax of the language."
- S738 | https://eprints.bbk.ac.uk/id/eprint/47679/3/47679.pdf | 2026-10-23 | "in relation to experts’ advice, as they were explicitly instructed not to introduce the language immediately after meeting the children"
- S739 | https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf | 2026-10-23 | "Parents can use various terms of address to children depending on situational contexts."
- S740 | https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early | 2026-10-23 | "These overgeneralizations suggest that children are not just memorizing the forms in their input, but also generating novel forms from a rule." [located on the same-page archive capture `20210414114152`; the live URL answered HTTP 403 with a Cloudflare interstitial, recorded as met and not passed]
- S741 | https://www.scielo.br/j/edur/a/GNcMNkFdczHjJxRzwL6ctBK/?lang=en | 2026-10-23 | "We know it’s ugly because people tell us it’s ugly."
- S742 | https://files.eric.ed.gov/fulltext/EJ1271032.pdf | 2026-10-23 | "Time was taken every morning so greetings would become what her students did routinely, and that they would be expected from each other."
- S743 | https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3267/2956/3857 | 2026-10-23 | "Since this construction has a register specification as “child-directed,”"
- S744 | https://www.dictionary.com/browse/ushanka | 2026-10-23 | tested wording (disposition rejected; NOT located on the cited URL): "a traditional Russian fur cap with earflaps that can be tied up on top" — re-test 200 https://www.dictionary.com/browse/khanka?q=ushanka&noredirect=true&mismatchType=misspelling / NOT_LOCATED https://www.dictionary.com/browse/ushanka quote-absent
- S745 | https://www.merriam-webster.com/dictionary/tiara | 2026-10-23 | tested wording (disposition rejected; NOT located on the cited URL): "a decorative jeweled or flowered headband or semicircle for formal wear" — re-test 403 https://www.merriam-webster.com/dictionary/tiara / NOT_LOCATED https://www.merriam-webster.com/dictionary/tiara HTTPError
- S746 | https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447 | 2026-10-23 | tested wording (disposition queued; located): "Smith-Corona owner's handbook, manual typewriters. 38 p. Add. ti: Owner's handbook for manual typewriters" — re-test 200 https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447 / LOCATED https://en.wikisource.org/wiki/Page%3A1977_Books_and_Pamphlets_July-Dec.djvu/447
- S747 | https://www.britannica.com/topic/mortarboard | 2026-10-23 | tested wording (disposition rejected; NOT located on the cited URL): "Britannica’s Mortarboard page as evidence for mortarboard use in academic dress" — re-test 403 https://www.britannica.com/topic/mortarboard / not applicable
- S748 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html | 2026-10-23 | tested wording (disposition queued; located): "Among the honorary crowns bestowed by the Romans for military achievements" — re-test 200 https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html / LOCATED https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html
- S749 | https://en.wikipedia.org/wiki/List_of_headgear | 2026-10-23 | tested wording (disposition queued; located): "Headgear is worn for many purposes, including protection against the elements, decoration, or for religious or cultural reasons, including social conventions." — re-test 200 https://en.wikipedia.org/wiki/List_of_headgear / LOCATED https://en.wikipedia.org/wiki/List_of_headgear

Row notes on the Gate, in the order the rows appear:

- S726 — the row's `VERIFY: LOCATED` line is **not** reproducible today: the
  locator's pinned Firefox UA is reset by eric.ed.gov, while a plain GET and the
  same-page capture both serve the quoted abstract claim
  (`.ufo/waves/round-64/w2/B2ReviewRowS726.md`). The quote above is the row's
  content; the LIVE leg does not probe S726 (frozen subset S718, S723, S728,
  S733, S738, S743).
- S719, S738, S739, S742 — these rows were repaired before this lesson was
  drafted because the anchor cell quoted a section label ahead of the body
  sentence, and the counter extracts the first quoted span
  (`.ufo/waves/round-64/w2/B2FixS719.md`, `B2FixS738.md`, `B2FixS739.md`,
  `B2FixS742.md`). The quotes above are the repaired body sentences.
- Length check over all 32 gate quotes with the counter's own normaliser
  (NFKC, casefold, `\W_` -> space): the range is 9 words (S718) to 25 words
  (S737); S719, S720 and S730 sit at 24. Every row is inside the counter's
  8-25 window.

Three disposition rows carry wording that the re-test could **not** locate on
the cited URL (S744 `NOT_LOCATED … quote-absent`, S745 `NOT_LOCATED …
HTTPError`, S747 `403` with no retrievable article). Those three are printed
above as the *tested* wording, not as located quotations; their grounds and
flips are what the rows assert. The other three disposition rows (S746, S748,
S749) located their wording on the cited URL and are therefore recorded as
queued candidates, because the round-63 rejection ground no longer holds.

## Mistakes

- R64-M1 (class: landing). Attempt-1 dispatched the build waves before the
  pre-dispatch receipts and the counter revisions were committed; the counters
  therefore existed only as working-copy bytes when the wave started. Evidence:
  `.ufo/waves/round-64/w2/B2ScribeLesson.md` finding 1 (the round-64 counter
  scripts are absent from the declared commit), and
  `.ufo/waves/round-64/w1/RevengerCounter.md` §0 (`git ls-tree HEAD
  reports/round-64/` holds accept-c rev0, accept-ca rev0 and claims.json but no
  accept-o.py at all). Captured by: QUALITY criterion 9 (dry runs checked both
  ways, receipt committed with the declaration). Fix: commit the frozen
  counters and their pre-dispatch receipts with the declaration, then dispatch;
  a wave must never start against counters that exist only in the worktree.
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
  of 26 mined rows could not be met. Evidence: `.ufo/waves/round-64/stage/report.txt`
  ("S723 MISSING", "S740 MISSING") and the inherited 30/32 reading of
  `.ufo/waves/round-64/check-rows.py`. Captured by: `check-rows.py` MISSING
  lines, and the ROWS/APPEND/LIVE legs of `accept-c.py` (LIVE's frozen subset
  contains S723). Fix: a wave needs a re-dispatch path for a dead row seat that
  lands the row artifact itself, not only a report; the gap was closed in
  wave 1 by ExecRowS723 and ExecRowS740, after which `check-rows.py` printed
  `CHECK-ROWS: 32/32 clean`.
- R64-M4 (class: counter-parsing shape). The counter extracts the **first**
  quoted span of a row's anchor cell, so a curly-quoted section locator ahead
  of the body sentence becomes the "quote": S719 yielded 5 words
  (`quote_words=5 in_order=0`), S738 `in_order=0`, S742 3 words
  (`quote_words=3 in_order=0`), S739 `in_order=2`. The sourcing was sound in
  every case; only the cell shape was wrong. Evidence:
  `.ufo/waves/round-64/w2/B2ReviewRowS719.md`, `B2ReviewRowS738.md`,
  `B2ReviewRowS742.md`, and the `PROBLEMS` lines of
  `.ufo/waves/round-64/stage/report.txt`. Captured by: the ROWS and RESTATE
  legs of `accept-c.py` and `check-rows.py`. Fix: put the body sentence in
  plain double quotes first and leave the locator unquoted
  (`.ufo/waves/round-64/w2/B2FixS719.md`, `B2FixS738.md`, `B2FixS739.md`,
  `B2FixS742.md`).
- R64-M5 (class: duplicate work under different URLs). S718 and S729 are the
  same paper (Farran, Lee, Yoo & Oller 2016, PLOS ONE 11(3):e0151518) reached
  through two different live URLs, with the same finding and the same Results
  sentence quoted twice in two phrasings. The LINK leg counts registry lines
  containing a URL string, so a work-level duplicate cannot fail it. Evidence:
  `.ufo/waves/round-64/w1/ReviewerRegistry.md` F2. Captured by: ReviewerRegistry
  (review-only; no counter leg sees work identity). Fix: keep one row per work
  and re-scope or replace the other with a genuinely distinct source; until
  then the 26-row statement buys 25 distinct sources.
- R64-M6 (class: stale assembly input). `.ufo/waves/round-64/stage/bullets.json`
  is a second content authority that is older than the row set: it holds 19
  keys and lacks S721, S723, S727, S733, S740, S741 and S743, and its S738,
  S739 and S742 clauses
  do not match the anchors those rows now carry. Evidence:
  `.ufo/waves/round-64/w1/CriticEntrySweep.md` CE4/CE5 and
  `.ufo/waves/round-64/w1/ConnectorOverlap.md` ("bullets 19 missing ids
  [...]"). Captured by: the RESTATE leg of `accept-c.py` at integration
  (staged wording supplies too few in-order quote words). Fix: derive the
  entry's claim lines from the current row artifacts; do not reuse an inherited
  JSON as the assembly input.
- R64-M7 (class: bullet overreach past the quote). Three claim lines state
  more than their anchor supports: S719 drops the quote's own "(with the
  aforementioned caveats)" and asserts a flat infant preference; S737's
  bullet invents a "worldbuilding" outcome the abstract never claims; S735
  turns the teacher's attempt to help into successful scaffolding the source
  expressly allows to fail. Evidence: `.ufo/waves/round-64/w1/ReviewSupportA.md`
  D1, `.ufo/waves/round-64/w2/B2ReviewRowS737.md`,
  `.ufo/waves/round-64/w1/CriticEntrySweep.md` CE2/CE3. Captured by: the blind
  support reviewers (review-only — RESTATE counts words and cannot see the
  overreach). Fix: keep the caveat the source states, or narrow the clause to
  what the quotation carries.
- R64-M8 (class: instrument and receipt identity). The claim-O counter's
  docstring still reads "revision 0" while its inline comments name revisions
  1, 3 and 4, and the declared commit does not contain the counter at all.
  The receipt was also observably partial for most of the wave: at 22:49
  `reports/round-64/telemetry/final-measures-o.txt` was an 1818-byte, 22-leg
  file that ended before MUT, with no verdict line and no exit code (read by
  ReviewerOReceipt). The copy present at authoring time (23:17, 2986 bytes) is
  complete — 23 legs, `MUT PASS … mutants=10`, `ACCEPT-O-64: PASS`, `exit=0` —
  but it still carries no measured-revision line and no counter sha256, so it
  cannot be bound to a revision or to `accept-o.py`'s bytes. Evidence:
  `.ufo/waves/round-64/w1/ConnectorOverlap.md` (counter stamp),
  `.ufo/waves/round-64/w1/RevengerCounter.md` §0,
  `.ufo/waves/round-64/w1/ReviewerOReceipt.md` checks 1 and 4. Captured by: the
  receipt reviewers. Fix: a receipt carries the measured revision and the
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
  and ReviewerOReceipt. Fix: pre-data claim-text revision to what the counter
  proves (each mutant fails its pinned leg), or a full-leg exclusivity leg —
  without weakening the EDGE assertions.
- R64-M10 (class: control vacuity in the calibration counter). The Ca NITS
  leg searches the whole canonical log for the substrings `45`, `47`, `W04`
  and `27`; an appended records-only paragraph containing only the token
  `W04` turns NITS FAIL into PASS with no numeric correction and no
  dependency sentence present. The inherited `dry-run-ca.txt` also prints six
  legs, omitting REVNAMES, so it cannot be cited as seven observed failures.
  Evidence: `.ufo/waves/round-64/w1/CriticCa.md` §1 (before/after runs pasted
  verbatim) and `.ufo/waves/round-64/w1/RevengerCounter.md` §0. Captured by:
  CriticCa's executed records-only control. Fix: scope each NITS check to the
  named round-63 correction and require each old->new association in its own
  context, with the base-plus-generic-token append as a forcing NITS-FAIL
  control.
- R64-M11 (class: declared land unowned). `reports/round-64/claims.json`
  names `telemetry/mut-o.txt`, `telemetry/edge-o.txt` and
  `telemetry/control-o.txt` as O lands, but no live seat was tasked to write
  them and none exist in the tree. Evidence:
  `.ufo/waves/round-64/w1/ReviewerOReceipt.md` check 2. Captured by:
  ReviewerOReceipt. Fix: every declared land needs an owning seat and a
  receipt, or the declaration is corrected before close.
- R64-M12 (class: asserted enactment without enactment). Root `LOG.md` records
  the S687 `mined -> queued` flip as enacted by this round's claim-C land while
  `corpus/SOURCES.md` still carries `mined`; the census's only W03 warning is
  that same row. Evidence: `.ufo/waves/round-64/w1/ScoutLessonRecon.md` item 1
  and `.ufo/waves/round-64/w1/CriticCa.md` §C. Captured by: the APPEND leg of
  `accept-c.py`, which requires S687's status cell to be `queued` in the
  registry. Fix: the registry edit is the enactment; the log may only say
  "selected" until the row lands.
- R64-M13 (class: metadata range read as two citations). The entry skeleton's
  metadata line `- source: S718–S743 ...` carries two registered ids, which
  `tools/check-cited-lines.py` reports as MULTI-ID and `accept-c.py`'s ONEID
  leg checks. Evidence: `.ufo/waves/round-64/w2/B2ExecEntry.md` (one
  `MULTI-ID` finding on line 4) and `.ufo/waves/round-64/w1/CriticEntrySweep.md`
  CE1. Captured by: ONEID plus `tools/check-cited-lines.py`. Fix: refer to the
  round's rows in prose without an id range on a cited line; concrete ids
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
  `B2FixS742.md`, and the S740 `ACCESS` line. Captured by: the LIVE leg's
  three-reopen budget and the same-page capture fallback; the row-level
  `ACCESS` notes. Fix: record the challenge as met and not passed, route to
  the archived capture, and treat a 429 as transient rather than as absence.
- R64-M15 (class: scope wider than the anchored evidence, and tier
  inflation). S721's scope names turn-taking while its quote defines only
  proto-conversation; S739's anchor is the paper's introduction citing Aledo
  (2018), a secondhand general claim, yet the scope claims the paper's own
  Sleman findings at tier A; S747's anchor holds fabricated meta-text rather
  than a quotation; S749 uses kind `community` where the one prior Wikipedia
  row uses `docs`. Evidence: `.ufo/waves/round-64/w1/ReviewerRegistry.md`
  F3-F7, `.ufo/waves/round-64/w1/ReviewSupportC.md` (S739 locator nit). Captured
  by: ReviewerRegistry (review-only). Fix: re-anchor or narrow the scope, and
  set the tier the quoted evidence actually supports.
- R64-M16 (class: locator label wrong, sourcing sound). S722's row places its
  quote under "Section A Continuous Vocabulary Spurt", but the live article
  carries that passage under "New Directions and Next Steps"; the quotation
  itself is verbatim in the body. Evidence:
  `.ufo/waves/round-64/w1/ReviewSupportA.md` D3. Captured by: ReviewSupportA.
  Fix: correct the locator string; a wrong locator is a provenance defect even
  when the quote is right.

## Census and counts

Census at wave 1 (`reports/round-64/telemetry/census-wave1.txt`, exit 0): the
29 census lines are byte-identical to the round-63 end census
(`reports/round-63/telemetry/census-end.txt`); the wave-1 file adds two `#`
header lines carrying the command and the exit code. Content: 27 W04
duplicate-URL rows, 1 W03 row (`S687` mined but unused), 0 W01, 0 W02, 0
E-codes; lane line `kotodama ok`. Manual counts over
`corpus/SOURCES.md` at the base: 643 rows, 0 malformed rows, tiers A=406 B=228
C=9, statuses mined=567 queued=57 rejected=19, no duplicate ids, no enum
violations or tier inflation.

Staged contribution set (`.ufo/waves/round-64/rows/`, read at authoring time):
32 rows — S718-S743 mined plus S744-S749 dispositions — with tiers A=18 B=13
C=1 and statuses mined=26 rejected=3 queued=3;
`.ufo/waves/round-64/check-rows.py` printed `CHECK-ROWS: 32/32 clean` (exit 0)
once the two dead seats' rows landed.

TBD — to be filled by L1 from committed evidence:

- registry rows after the land: TBD (target 675 = 643 + 26 mined + 6
  dispositions; the S687 `mined -> queued` flip moves one row between status
  buckets)
- corpus entries: TBD (237 -> 238) and linguistics entries: TBD (29 -> 30)
- tier and status histograms after the land: TBD
- census receipts: TBD (start and end, both with the exit code)
- ACCEPT-C-64, ACCEPT-O-64, ACCEPT-CA-64 results: TBD
- entry bytes and README index row: TBD

Observed at authoring time, in the uncommitted working tree only — recorded
here as a working-tree observation, not as a committed acceptance result:
`reports/round-64/telemetry/final-measures-o.txt` (23:17) ends
`ACCEPT-O-64: PASS` / `exit=0` with 23 legs and `MUT PASS bad=[] mutants=10`.
`reports/round-64/telemetry/census-wave1.txt` is the wave-1 census (exit 0).
`corpus/SOURCES.md` is still byte-identical to the base (643 rows), so no
post-land census exists yet.
