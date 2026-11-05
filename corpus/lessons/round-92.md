# Round 92 — grader v3 routed-survivor repairs and an ideophones entry

author: kotodama lane, 2026-11-05.
Base: `21350361500aa000b90f91082bf9d7295a9c24cd`. Freeze: `066b9728fc64e78735769c4740d05c1000d31a3b` (claims, counter, mutants, stub and receipts frozen there).
Claims O (operability) and C (coverage) are exactly as frozen in `reports/round-92/claims.json`.
Freshness remains paused by unresolved L0 round-11 (`.ufo/l0-questions.md`, kotodama | round-11) and round-89. The lowest-axis duty is neither met nor waived; no admission is asserted on that procedural gap.

## Gate

Sources opened by plain HTTP on 2026-11-05 (ordinary requests, `curl/8.7.1` UA; no browser, no challenge passing; automation: none). Raw response bodies, the fetched PDFs and their extracted text, sha256 and access instants are in `reports/round-92/evidence/manifest.json`. Quotes below are whitespace-normalized spans of those captured bytes, verified by re-running the frozen tool's own normalization on the committed captures.

Search method (PRISMA-inspired): DOAJ article API, query `ideophone`, 20 results screened; OpenAlex (HTTP 429), Semantic Scholar (HTTP 429 twice), arXiv API (HTTP 200, two tangential hits), PMC search page (HTTP 200, JS shell, no results in the HTML), langsci-press catalog (HTTP 404). Identified 20 / screened 20 / included 4 / excluded 16. Included (4): the four entries above. Excluded (16), as read from the DOAJ records: Lulubo phonology (1987) and its duplicate OJS record; a French study of vocalic alternation in ideophones (Signifiances, 2020); a Zulu lexicographic treatment (2011); an Arusa Maasai ideophone study (2022, DOI front door, not fetched); Mandarin AB vividness ratings (2024); Korean vowel phonotactics (2023); literary interjections in Uirtus (2025); a comics adaptation of libretto texts (2024); Siamese musical instruments (2024); Persian onomatopoeias (2023); Mofolo’s Chaka style study (2013); iconic hand gestures from ideophones (2025, DOI front door, not fetched); an Arabic sound-meaning article (2019); Awetí motion events (2015); Japanese pain descriptions (2025, Cambridge front door, not fetched).

- S957 admit A/mined. https://typologyatcrossroads.unibo.it/article/view/19369 — accessed 2026-11-05 — body: “whether or not ideophones make up a clear-cut word class in different languages”
- S958 admit A/mined. https://typologyatcrossroads.unibo.it/article/view/16393 — accessed 2026-11-05 — body: “do they constitute a word class on their own, or should they be subsumed under another word class”
- S959 admit A/mined. https://typologyatcrossroads.unibo.it/article/view/16466 — accessed 2026-11-05 — body: “complex predicates consisting of an invariant coverb followed by an inflecting light verb, most commonly the verb alä ‘say’”
- S960 admit A/mined. https://www.frontiersin.org/articles/10.3389/flang.2026.1785036/full — accessed 2026-11-05 — body: “Sound-symbolic effects have been claimed to facilitate word learning, because of the motivated relationship between form and meaning”

Locators: S957 special-issue introduction, abstract; S958 article abstract; S959 article abstract; S960 article abstract, opening sentence (body text, not navigation). The S960 quote was read in the extracted abstract; the HTML capture carries site chrome only outside the abstract block.

No row was rejected this round. The taste evidence is the search-log inclusion boundary above (16 exclusions with reasons).

Registry delta (census before → after, `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`, both rc 0): 880 → 884 rows; A 518 → 522; mined 773 → 777; no base row removed, re-dated or cell-changed (`git diff --numstat 21350361 <lands> -- corpus/SOURCES.md` adds rows only). New used-by paths: `corpus/knowledge/linguistics/ideophones-mimetics.md` for S957–S960.

## Corrections to round 91

Statements that stand as filed; corrections are new entries:

1. Round-91 `O.before` named `reports/round-91/controls/before-v1-entry.txt`, produced post-freeze (R91-M6). Unchanged here.
2. The round-91 spot-check §6 routed defects are addressed under claim O: D4 (mutation receipt header prints a hardcoded clean rc) is repaired in the round-92 `mutants.py` (the header carries the clean run's own rc and first line); D5 (no counter leg asserts the mutation receipt) is the new MUTRECEIPT leg; W3 (a short row aborts the counter) is repaired as a leg FAIL (APPENDONLY, malformed row). The frozen round-91 bytes are not edited.
3. Round-91 routed defect 4 (seven entry-mode counterfeit classes pass v2) and defect 5 (six mutation survivor gaps) are repaired or partly repaired as listed under R92-M2 and R92-M8.

## Work performed and verdicts (author-side; non-author closure pending)

- O, operability: grader v3 (`tools/check-advance-evidence.py`, sha `905be2fe…`) refuses the seven routed round-91 counterfeits on their named legs (`reports/round-92/controls/after-v3-refusals.txt`), keeps the compliant control green, and passes its own selftest 89/89 with 21 named refusals. The mutation pass kills 60/60. The stub control is refused by OKCOUNT (34 ok lines) and kills 0/60.
- C, coverage: `corpus/knowledge/linguistics/ideophones-mimetics.md` (28814 B, 12 `##` sections, a 23-row table with 5 columns, the six sub-topic phrases spanning ten heading/table surfaces) over S957–S960, with gate lines, captures and manifest entries; index 264/264 rc 0.

## Mistakes

| id | class | evidence | captured-by | fix or retained limit |
|---|---|---|---|---|
| R92-M1 | vacuous | the first do-nothing control for claim O was named `at-freeze-O-do-nothing.txt` and it reads PASS 8/8 at the freeze — the freeze carries the instrument itself, so a freeze-revision run grades the claimed work as already present (`reports/round-92/controls/at-freeze-O-instrument.txt`; ExecControls confirms rc 0) | §9 claim sizing (a do-nothing control must skip the claimed work) and QUALITY 11 | renamed to `at-freeze-O-instrument.txt` (instrument-present, not no-work). The no-work control is `reports/round-92/controls/at-base-O-refused.txt`: lands = frozen base → rc 2 `MEASURE92_ERROR: --lands equals the frozen base`. A base landing cannot pass. |
| R92-M2 | survivor | CriticClaims91 seven counterfeits passed the frozen v2 grader rc 0 (`.ufo/waves/round-91/w1/stage/CriticClaims91/attacks.md` findings 1–6 + the shared-capture clause of 3) | QUALITY36 (v2 bounds named the residual) | v3 refuses all seven on named legs (`before-v2-counterfeits.txt` 7/7 rc 0; `after-v3-refusals.txt` 7/7 rc 1 on APPENDONLY, UNIQUENESS, CAPTURE, GATE, TOPIC; G0 green both). ExecBeforeV2 replayed both receipts byte-identical (14/14 V-lines, 2/2 G0). |
| R92-M3 | input-shape | the first two mutation runs crashed with `FileNotFoundError` on a missing `--work` directory (a traceback, not a refusal) | QUALITY 9 (an input-shape error fails the declaration, not the round) | retained limit: `mutants.py` still crashes on a missing `--work` (no refusal path); runs re-issued with `mkdir -p`; no instrument or data changed between the attempts. Routed to round 93. |
| R92-M4 | fixture-defect | V12 (manifest url unbound, shared capture) was initially red under v2 for an incidental cause: the second capture write overwrote the first row's capture, so v2 refused on quote absence | criterion 11 (each clause must fail for its named reason) | the builder writes each shared capture once; the rerun shows v2 PASS 7/7 (defect present) and v3 refusing each on the named leg. |
| R92-M5 | fixture-defect | the V2 heading-stuffing fixture first failed v2 on SHAPE (repeated filler) and ENTRY (too few headings), not on the routed cause | criterion 11 | rebuilt with distinct filler sentences and ≥4 headings; the routed cause is isolated (v2 PASS 8/8, v3 refuses on TOPIC). |
| R92-M6 | multi-id lines | the ScribeEntry draft carried four cited lines with two or more S-ids and an empty `- sources:` header (`grep` lint before landing; the claim's entry mode does not run `check-cited-lines.py`, so the frozen C predicate could not see it) | QUALITY 15 (captured by the lint, not by the C predicate) | fixed by the scribe seat (one id per line; header lists the four sources one per line). Routed to round 93: the C predicate should run `tools/check-cited-lines.py` as a leg. |
| R92-M7 | survivor (O) | CriticClaims92 ran 21 new counterfeits against frozen v3: **16 survive rc 0** — URL variants that the normalizer does not equate (scheme swap, `www.` host, `?ref=` query, path case: A2c–A2f); an entry copy with a trailing newline (A3b); three single-word headings carrying the phrases (A4a); lesson-channel variants (A5d–A5f); and six new classes (A6a–A6f). One counterfeit (A6g) crashes with an unhandled `AttributeError` (rc 1 without a named refusal). | the round's own critic seat, after the freeze | frozen, not repaired (the tool is sha256-pinned by the claim). O's bounds state that completeness is not claimed; O's frozen predicate verifies (21 named refusals, 60/60 mutants, stub refused). These 16 + the A6g crash are routed to round 93 with the smallest corrections in `.ufo/waves/round-92/w1/stage/CriticClaims92/corrections.md`. |
| R92-M8 | selftest gap | MutationTesterV3's gap hunt (10 scratch mutants outside the frozen 60): 9 survive the v3 selftest — README graded-list entries (`manifest`, `entry`, `lands`, `lesson` removed from the byte-copy list), the `..` traversal arm of `capture_error`, the FETCH_RE offset, the fetch-date arm, the capture-dir slash arm and the norm_url port-strip arm (`.ufo/waves/round-92/w1/MutationTesterV3.md`) | QUALITY 23 (a selftest must pin each arm) | not in the frozen predicate; retained limit; routed to round 93 as selftest additions with a red-before for each arm. The frozen 60 are all killed, so O's kill rule is not failed by these. |
| R92-M9 | calibration (frozen text) | `reports/round-92/claims.json` `O.before` states the base tool has "none of the twelve new refusal case names (12/21 named refusals)". Measured: the v2 selftest source (`git show 21350361:tools/check-advance-evidence.py`, sha 88597a66) contains 9 of the 21 names; its selftest passes 77/77 and prints no name for the 12 new cases. The frozen sentence is wrong on the count (9, not 12), and it is not edited. | QUALITY 9 (declared figures are re-derived from committed bytes before dispatch) | erratum recorded here; the O predicate and its counter are unaffected (the predicate tests v3, not this before-description). |
| R92-M10 | survivor-class (lesson gate) | authorial quoted spans in the entry bind to no capture: `does my language have ideophones` (ReviewerEntry F-1) and two in §7, `this happened` and `this was caused`; one common word, `strongly`, collides with S958's own gloss. A bare span-collision sweep therefore cannot decide mis-citation (ScribeEntry-22 sweep, `.ufo/waves/round-92/w1/ScribeEntry.md`). | QUALITY 11 (a sweep must name what it can and cannot decide) | recorded; the non-author closure judges authorial prose, not span collisions; routed to round 93 as a QUALITY criterion that separates authorial quotes from source quotes. |

## Quarantine

Assimilation: no package adoption this round. The round-91 quarantine verdicts stand unchanged (21 rows: LOCATED 3, PARTIAL 3, ABSENT 10, UNREACHABLE 3, UNVERIFIABLE 2). The id-collision guard at round 91 found 98 collisions between the lane registry (880) and the staged package; no renumber has landed and none is attempted here (scratch-only work, operator-gated). `considerthese/` is absent in this lane.

## Understanding and trial

The entry separates three things the register does not: the typological class of ideophones (S957 names the open question whether they form a clear-cut class), their grammar where a language makes them productive (Kambaata, S958; the Amharic say-verb predicate, S959), and the acquisition question for sound-symbolic effects (S960, a Spanish-learning sample with insensitivity in younger children). The adjacent owner `sound-symbolism.md` keeps token-level symbolism; the entry defers to it in §12. The design procedure in §10 and the decision tables in §11 were NOT independently checked rule by rule this round; that check is left to the non-author closure, and the rules that go beyond the cited sources are the author's design choices.

Outside non-author spot-check: pending. ReviewerEntry-5 (wave 1) reviewed the entry against the frozen C clauses (9/9 floors) and QUALITY criteria 1–5 (5/5) with three LOW findings (F-1 an authorial quoted span, F-2 an ASCII/curly apostrophe mismatch in S959's title, F-3 a title span shared by S958 and S959); none is a frozen-clause failure. Dispatched seats are still the lane; no SHONEN box becomes [x].

## Corrections (after landing, append-only)

1. The sentence at line 59 ("the entry defers to it") overstates the boundary. The
   connector seat (`.ufo/waves/round-92/w1/stage/ConnectorOverlap/overlap-scan.md`) found a
   real contested overlap: `corpus/knowledge/linguistics/sound-symbolism.md` §6 (lines
   99–111) already holds an ideophone word-class definition, a grammar profile, reduplication,
   the Japanese giongo/gitaigo system and a five-step ideophone register design procedure.
   The new entry therefore re-states part of the same ground; the counter's coverage leg
   measures only filename ownership (0 owners at base) and does not see this. Contested
   scope is reported, not absorbed: the operator is asked to arbitrate through
   `.ufo/l0-questions.md` (kotodama | round-92). The expansion verdict in SCORECARD is
   qualified accordingly.
2. The wave settled with all ten seats returning results and none dead. Its
   freeze-review seat (`ReviewerFreeze-2`, `.ufo/waves/round-92/w1/ReviewerFreeze.md`) reported
   D3: an intermittent `SELFTEST FAIL 88/89` on the `capture byte-copies the base registry` case
   in its own runs during a 10:27–10:54 window. The lane could not reproduce it: 12 sequential
   fresh-directory runs, 4 concurrent runs on one `--work` directory and 4 concurrent runs on
   separate directories all printed `SELFTEST PASS 89/89`. The cause is not identified; it is
   routed to round 93 with the reviewer's captured outputs
   (`.ufo/waves/round-92/w1/stage/ReviewerFreeze/evidence/`). O's measured run at lands passed.
