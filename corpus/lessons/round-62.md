# Round 62 lesson — footwear line repairs (claim D) and the bounded row re-opener (claim O)

Lane base `d42ffb89`. Instruments revision 0 `f0173481`; revision 1 `e6a61e82`; freeze `9143fc44`; O landed `e605603c`; D landed `a2c5caa5` (measured revision); receipt `reports/round-62/telemetry/final-measures.txt` (`25b44b8a`).

## Spot-check intake (round-61 outside verifier, `corpus/lessons/round-61-verifier-spotcheck.md` §7)

Drafted by seat ScribeIntake (`.ufo/waves/round-62/w1/ScribeIntake.md`); dispositions updated with the measured result.

| §7 defect | disposition | evidence | what round 62 does |
|---|---|---|---|
| 1. footwear lines S692 (63), S665 (74), S666 (75), S687 (93) | fixed by claim D | `reports/round-62/telemetry/final-measures.txt` (ACCEPT-D-62 PASS at `a2c5caa5`) | line 63 keeps the open list "Belgium, etc."; line 74 names the Bata Shoe Museum image caption; line 75 keeps "we have" and names the BBC article; line 93 cites the new tier-B row S693 (Dictionary.com, talaria) instead of tier-C S687. The repair is in a new commit; round-61 receipts, verdicts and rows are unchanged |
| 2. S655/S658/S681 `kind` cells edited in place | recorded (note below) | `git diff efbee29c ae8e393e -- corpus/SOURCES.md` | appended note in `## Status and used-by change log`; this round ran the census on the landing tree before the landing commit (exit 0) |
| 3. LOG/SCORECARD say R61-M1..M6; the lesson has M1..M7 | corrected by appended rows | `corpus/lessons/round-61.md:108-114` (seven rows) | correction rows appended to `SCORECARD.md` (round-61 calibration) and `LOG.md` (round-62 entry); filed text not rewritten |
| 4. `accept-o.py` (round 61) compares findings as sets | applied to this round's counter | `reports/round-62/accept-o.py` ORDER leg | ORDER compares the printed ROW id sequence with the argument list, including repeated ids (revision 1, CtlOOrderErr) |
| 5. QUALITY 13 lacks a transient-error treatment with its own control | fixed | `reports/round-62/locate-control.py`, `reports/round-62/telemetry/locate-control.txt`; QUALITY criterion 16 | D's live leg declares three passes 60 s apart over the base locator's three attempts per URL and a same-page capture per row; its paired recovery/exhaustion control passes on revision 1 and fails on a PASSES = 1 copy |

## Pre-data control wave and revision 1

Wave 1 (37 seats, `.ufo/waves/round-62/w1/`) scored revision 0 (`f0173481`). Controls that met it, each forcing a revision-1 change before any data (re-score receipts `reports/round-62/telemetry/controls-rescore.txt`, 24 receipts):

- CtlDMarkOnly: hidden HTML comments / parentheticals kept all four original assertions with an honest S693, full PASS → NOMARK reads `- <clause> (S###)`, refuses comments, brackets, daggers, asterisks; the line legs read the clause only.
- CtlDJunkTokens: five-content-word token salad passed every line leg → KEEP (60% of base content words on 63/74/75).
- CtlDRegistryEdits: S693 reusing S688's URL, full PASS; `| S650b |` inserted unseen → FRESH; APPEND refuses malformed S-rows.
- CtlDCaptureShapes, CtlDFabricated fxB: different-page, bare and future captures passed ROWS → same-page, past-dated capture within the locator's four-URL budget (CriticFetchRule named the budget).
- CtlDOffTopicRow: a located Hermes-spaceplane row, full PASS → SOLE adds round 61's footwear TOPIC rule.
- MutCounterD: a CR on line 1 passed SET → SET and APPEND read bytes.
- CtlOOrderErr: a de-duplicating tool, full PASS → ORDER repeats ids.
- CtlODefault, CtlONoRetry caseC, CriticClaims finding 3: 200 s gap, 60 s attempt wait, no attempt wait passed DEFAULT → DEFAULT checks exit, summary and the request schedule (attempts 4-10 s apart, bursts 55-75 s apart).
- CtlOUnbounded c5, c10, c11: fetching every URL after a match, `url=-`, an unlisted request → class BODY_THEN_ARCHIVE, unlisted-path check, `url=` compared.
- ExecReopenTool live run: S665's quote sits in `<p class="thumbnail-description">` → caption elements include `thumbnail`/`gallery` classes and ids.
- MutCounterO: reserved dead port, balanced BODY_SPLIT, all caption attributes, anchored REOPEN_ERROR, process-group kill.

NONE-MET on revision 0: CtlDDoNothing, CtlDDeleteMove, CtlDQuoteDump, CtlDDeadEcho, CtlDInputs, CtlODoNothing, CtlOAlwaysLocated, CtlORawSubstring, CtlOKeyed (GEN/BOUND), CtlONoArchive. Honest positives PASS under revision 1: CtlDMarkOnly honest-positive, CtlDCaptureShapes pristine-positive, CtlOHonestRef (updated to the revision-1 caption rule by its own seat). Declared residuals (`claims.json` `known_residuals_after_controls`): lexical legs cannot see a reversed meaning (review-only, residual reviewers); INDEP is a string check; requests to other hosts are not observable by BOUND.

## Gate

New row opened this round (accessed 2026-10-23 by the L1 after the scribes' candidates; LOCATED live and in the capture by `reports/round-61/reopen-quote.py`):

- S693 | https://www.dictionary.com/browse/talaria (capture https://web.archive.org/web/20240529024530id_/https://www.dictionary.com/browse/talaria) | 2026-10-23 | "the wings or winged sandals on the feet of Hermes, or Mercury."

Rejects (not registered):

- Merriam-Webster `talaria` (ScribeTalariaMW, tier A candidate): the live page refuses ordinary requests. Re-test (QUALITY 12): `curl -s -o /dev/null -w '%{http_code}' -A 'Mozilla/5.0 …Firefox/131.0' https://www.merriam-webster.com/dictionary/talaria` → `403` (L1, 2026-10-23); locator `NOT_LOCATED https://www.merriam-webster.com/dictionary/talaria HTTPError` (`.ufo/waves/round-62/w1/ScribeTalariaMW.md:49`). The row would rest on its capture alone while Wayback answered the locator's user agent with 429 (CtlDFabricated), so the live-readable Dictionary.com page was preferred.
- Cambridge Museum of Classical Archaeology, Farnese Hermes cast (ScribeTalariaRef): the quote "This statue of Hermes, the Greek messenger god, identified by his winged sandals" does not name talaria, so it cannot carry line 93's term; its capture also failed the locator (`NOT_LOCATED … URLError`, `.ufo/waves/round-62/w1/ScribeTalariaRef.md:41`).
- BBC News, "Why did men stop wearing high heels?" (ScribeHeelCaption option B, drafted as S695): not registered; line 74 is repaired by naming S665's caption, so a second heel row was not needed this round. A body-text candidate for a later round.
- Collins and Britannica `talaria`: `403` to an ordinary request (L1 curl, 2026-10-23); not used.

## Status and used-by change log

- S687 used-by: `corpus/knowledge/culture-material/footwear-codes-terminology.md` → `—` (line 93 now cites S693; census W01 becomes W03 "mined but unused"; status unchanged).
- Appended note (round-61 §7 item 2): S655, S658 and S681 `kind` cells were changed in place `news` → `docs` between `efbee29c` and `ae8e393e` with no superseding rows (round-61 R61-M7). Recorded here; the cells are not edited again.

## Mistakes

| id | class | evidence | captured-by | fix (shown able to fail) |
|---|---|---|---|---|
| R62-M1 | routed review defects left unmarked in the entry after review | `corpus/lessons/round-61-verifier-spotcheck.md:114`; entry lines 63, 74, 75, 93 at `efbee29c` | none | repair or mark a routed line in the round that routes it; witness F1 (`.ufo/waves/round-62/w1/ScribeMistakes.md`) prints `UNMARKED_ROUTED_LINES: 63 S692, 74 S665, 75 S666, 93 S687`, exit 1, on round-61 bytes; repaired here by claim D |
| R62-M2 | a LOG/SCORECARD mistake range stated before the lesson closed | `LOG.md:4139`; `corpus/lessons/round-61.md:108-114` | none | derive the range from the lesson table at filing; witness F2 prints `MISTAKE_RANGE_MISMATCH: LOG=R61-M1..M6; lesson=R61-M1..M7; rows=7`, exit 1; this round's LOG and SCORECARD ranges were written from `grep -c '^| R62-M' corpus/lessons/round-62.md` |
| R62-M3 | in-place `kind` edits after landing (R58-M6, R61-M7 repeat) | spot-check §4; `git diff efbee29c ae8e393e -- corpus/SOURCES.md` | SOURCES header rule (no tool) | run the census on the landing tree before the landing commit; witness F3 fails on the three cells; this round's census ran before `a2c5caa5` (exit 0) |
| R62-M4 | a revision-0 counter written without the negative fixtures its own claim names (12 controls met revision 0) | `reports/round-62/telemetry/controls-rescore.txt`; this lesson `## Pre-data control wave` | the pre-data control wave (worked as designed) | name, for each leg, the cheapest shortcut it must stop before writing it; shown able to fail: every listed CONTROL-MET fixture passes revision 0 and fails revision 1 (receipts) |
| R62-M5 | wave-1 seats ran past the settle deadline | CtlDHonest, CtlONoRetry cancelled at ~12:00Z after 66 min (both had written reports); CtlONoArchive and CtlOUnbounded ran 60-64 min | settle-deadline rule (Contract) | size multi-run control items (each counter run ~150 s, LOCATE passes ~2-3 min) to fit a 25-minute box or split by fixture; witness: `.ufo/waves/round-62/w1/swarm-registry.json` |

## Known defects routed to round 63
- `tools/reopen-row.py` (ResidToolSecurity, ResidRerunO): HIGH — redirects are followed without re-running the private-host refusal (a public URL redirecting to 127.0.0.1, ::1 or 10.x is fetched without `--allow-private`); MEDIUM — `attempts=` undercounts redirect hops; MEDIUM — a malformed URL (`:99999` port, `[::1` bracket) prints a ValueError traceback, against the contract; LOW — 100.64.0.0/10 not refused, silent 4 MiB truncation, gzip bodies read as ABSENT, no per-row deadline. The measured tool stays as landed (`e605603c`); fix in round 63 under a new frozen predicate with a redirect-to-private control.
- Line 75 nit (ResidLine75): the clause drops "from" ("is a … bowl" vs the page's "is from a … bowl"); meaning unchanged.
- S693 `kind` is `docs` while S692 (same publisher) is `book` (ResidLine93S693, LOW); left as filed (no in-place kind edit; R62-M3).

- Census W03 S687 (mined, unused): decide whether S687 stays a lead row or is filed `queued` by a status change logged old→new.
- ScoutCaptionRows (`.ufo/waves/round-62/w1/ScoutCaptionRows.md`) lists caption/label-only rows on footwear lines 58, 70, 72, 78 (S673, S661, S663, S677) and S161 in the speech-surrogates entry: re-open with `tools/reopen-row.py` and re-scope or replace.
- Run `tools/reopen-row.py` over the footwear block S652-S693 and record each verdict (CAPTION_ONLY and UNREACHABLE rows first), freshness pause permitting.

## Residual falsify call (8 seats, `.ufo/waves/round-62/resid/`)

- ResidRerunD: HOLDS — accept-d.py 16/16 PASS on an independent clone at `a2c5caa5`, byte-identical to the receipt except the LOCATE timestamp; locate-control 6/6; counters at `a2c5caa5` byte-identical to the freeze `9143fc44`; only `final-measures.txt` landed after the measured revision.
- ResidRerunO: HOLDS — accept-o.py PASS twice on fresh random fixtures, selftest 32/32; contract gaps the fixture cannot see listed above (redirects, attempts undercount, truncation, gzip).
- ResidLine63, ResidLine74, ResidLine75, ResidLine93S693: SUPPORTED / HOLDS — each line restates only its page (63 open list verbatim; 74 the quote sits in `data-img-description` and `<p class="thumbnail-description">`, `reopen-row.py` prints `ROW S665 CAPTION_ONLY`; 75 hedge and BBC attribution; 93 S693's quote is definition body text, capture same page, 2024-05-29).
- ResidCriticFreeze: MIXED — freeze integrity holds and no earlier counter run on a claimed object was found; but not every revision-1 hunk has an exercised forcing control (see Errata).
- ResidToolSecurity: MIXED — the redirect SSRF and traceback defects above.

## Errata

- `## Pre-data control wave and revision 1` above presents every revision-1 change as forced by a control. Exactly: O's default-registry EXIT call, DEFAULT's exit/summary check and ERR's anchored prefix and both-stream traceback check were forced by source inspection (CriticClaims finding 3, MutCounterO findings 6-7), not by an executed control; the committed re-score has no isolated control for those three guards (ResidCriticFreeze finding 1). The revision as a whole carries its receipts (`controls-rescore.txt`).

## Outcome

Author-side: ACCEPT-D-62 PASS and ACCEPT-O-62 PASS on their first runs at `a2c5caa5` (`final-measures.txt`), reproduced by ResidRerunD and ResidRerunO; the four repaired lines judged SUPPORTED by one-line reviewers. The landed tool carries a HIGH review finding (redirect SSRF) outside its frozen predicate, routed to round 63. Non-author verification is the hyaku closure's.
