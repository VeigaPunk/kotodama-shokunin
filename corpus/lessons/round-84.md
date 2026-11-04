# Round 84 — kotodama (Linux/omp host, 2026-11-04)

Base `81499ee45b5751d388fefc78583810878de01ecd` (lane tip at round open); freeze
`7e6ee2f8f7b54dbeecf42cfe96050e533a86a6e2` (r2: claims.json, the shared counter
library and the two counters; revisions r0 `3ca2cf28` and r1 `e160a72e` recorded in
`reports/round-84/counter-revisions.md` with their red-befores). One v1 wave of 12
seats (2 scout, 3 executor, 2 scribe, 1 connector, 1 reviewer, 1 critic,
1 mutation-tester, 1 sentinel; the L1 holds the canonical planner seat). Claims
frozen before any claim artifact landed; r2 landed two minutes after the wave was
dispatched (mistake R84-M4), so the spawned seats read the r1 context and every
verdict below is graded at r2 by the L1.

Two claims: **D** (depth — witchcraft and sorcery as an accusation institution,
four rows opened this round) and **O** (operability, capability acquisition — the
ordered sound-law applier with its committed example). The lowest-scoring
non-retired axis is freshness; its move is paused by the open round-11 L0 question
(`.ufo/l0-questions.md` line 47: "Freshness axis-move claims are paused until
ruled"), so the round works depth and operability and claims no freshness move.

## Gate

Every row below was opened by plain HTTP GET on 2026-11-04; the binding fetch
receipts are `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/S91[4-8].txt` and the
source scout's independent second reading is
`.ufo/waves/round-84/w1/stage/ScoutSourcesWitch/`. URLs, access dates, locators
and the located quote are given per row (QUALITY 31(iii)); raw/folded counts are
against the served bytes.

- **ADMITTED — S914, EB11 "Witchcraft" (N. W. Thomas), tier B.**
  `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Witchcraft`,
  accessed 2026-11-04 (HTTP 200, 98968 bytes, sha256 `68511af9…0ef4`, revision
  15556864). Locator: pp. 755–758, "Further Development", p. 758. Quote, 18 words:
  「by a strange perversion these admissions, wrung from their victims by rack or
  thumb-screw, were described as voluntary」 raw 0 / folded 1 (line wrap).
  Calibration: 1911; it does not mention the 1735 repeal, so the entry's repeal
  sentence does not cite this row. Its 2008-10-06 capture predates the
  transcription and does not contain the quoted text.
- **ADMITTED — S915, Howard Williams, *The Superstitions of Witchcraft* (1865),
  tier B.** `https://www.gutenberg.org/cache/epub/22822/pg22822.txt`, accessed
  2026-11-04 (HTTP 200, 450230 bytes, sha256 `88407510…03c4`; capture 2026-09-29,
  450230 bytes, byte-identical). Locators: Part II ch. I (age and sex of the
  accused), Part II ch. II (the earliest English trial; the De Spencers and John
  of Nottingham), Part III ch. I (the Ennemoser abstract of the criminal code).
  Quote, 17 words: 「The arrest might take place on the simple rumour of a witch
  being found somewhere, without any previous denunciation.」 raw 0 / folded 1
  (line wrap). Calibration: an 1865 Protestant-progress narrative quoting
  Ennemoser at second hand; rule detail is a lead to the 1489 text.
- **ADMITTED — S916, the Bull of Innocent VIII (1484), tier A.**
  `https://en.wikisource.org/wiki/Malleus_Maleficarum/The_Bull_of_Innocent_VIII`,
  accessed 2026-11-04 (HTTP 200, 73365 bytes, sha256 `cc7b7d31…b322`, revision
  14260824). Locator: the empowerment clause, printed p. xlv. Quote, 17 words:
  「the aforesaid Inquisitors be empowered to proceed to the just correction,
  imprisonment, and punishment of any persons」 raw 1 / folded 1. No capture
  exists (CDX exact query returned no rows); the Malleus landing page is front
  matter only and the Part subpages 404, so this row's scope stops at the warrant.
- **ADMITTED — S917, Charles W. Upham, *Salem Witchcraft* (1867), tier B.**
  `https://www.gutenberg.org/cache/epub/17845/pg17845.txt`, accessed 2026-11-04
  (HTTP 200, 1801648 bytes, sha256 `925e3634…9539`; capture 2026-09-05,
  1801648 bytes, byte-identical). Locators: vol. I p. 433 (Godfrey's defamation
  actions, 1659), vol. I pp. 350–351 (the Sinclair retraction; the starving
  woman's confession), vol. I pp. 407–408 (spectral proof and the evidence
  menu). Quote, 14 words: 「soon after, he commenced actions in the County Court
  for defamation against his accusers」 raw 0 / folded 1 (line wrap).
  Calibration: an 1867 antiquarian history printing court documents in old
  spelling; the narrator's judgments are his own.
- **REJECTED — S918, EB11 "Sorcery", tier C.** `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Sorcery`,
  accessed 2026-11-04 (HTTP 200, 60730 bytes, sha256 `2c4092db…`; body at the
  p. 431 proofread page). Quote, 21 words: 「SORCERY, magic, enchantment,
  witchcraft; the use of supposed supernatural powers by the agency of evil
  spirits called forth by spells, incantations」 raw 0 / folded 1 (the headword
  sits inside an inline bold tag). Reason: the article is a printed 71-word
  dictionary stub, definition only — zero accusation/trial/torture/evidence/law
  vocabulary. Flip: a full EB11 article body transcribed at the same URL.
- **CARRIED, used-by extended — 21 already-registered rows the entry cites:**
  S280, S295, S297, S349, S350, S381, S382, S403, S605, S610, S621, S622, S644,
  S645, S854, S901, S902, S903, S905, S909, S912. Only their last cell changed
  (old `…` → `…, corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md`);
  no other cell moved. Every one of the entry's 25 distinct cited ids resolves in
  the registry at the lands (L1 check, `stage/L1/l1-checks.txt`).
- **L1 re-grade.** The four mined rows and the rejection were re-read by the L1
  from the full served bytes before landing; the 19 anchor spans the reviewer
  checked were re-located with 0 misses. The stale r1 freeze in the seat prompt
  is recorded as R84-M4; no verdict uses it.

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R84-M1 | **a body probe that read absence from its own stripper** — I concluded that EB11 "Sorcery" served no article body from a 2,765-character visible-text window plus a literal phrase grep. The body is present, complete, at raw offset 45,999 (452 characters): the served HTML injects the unexpanded Proofreadpage payload mid-word and splits the first clause with `</b>`/`&amp;c.`, so the stripped window ended before the body and the phrase could not match raw | my extraction (`stage/L1/sources/fetch-summary.json`, S915 60,730 bytes) versus the folded read of the same bytes: `SORCERY, magic, enchantment, witchcraft` raw 0 / folded 1; the scout's independent read in `stage/ScoutSourcesWitch/S915.txt` and `second-reading.md` | the source scout's independent second reading (the R82-M3 rule), not my own check | the stub is recorded as S918 rejected with reason and flip ("printed 71-word dictionary stub, definition only"); the candidate rule is now a raw+folded count over the full body, never over a window |
| R84-M2 | **a frozen shape marker that graded an implementation detail** — claim O's `shape_markers` required the literal `SOUNDLAW_ERROR:` in the tool source, but a conforming tool keeps the label in a constant and prints `"%s: %s"`, so the marker would have failed a correct tool | grade at freeze r1: `.ufo/waves/round-84/w1/stage/L1/fixture-o.txt` (`TOOL FAIL ... missing=['SOUNDLAW_ERROR:']` while SELFTEST/DEMO/NEGATIVE/REGISTRY pass) versus the r2 grade (`TOOL PASS`) | the L1's fixture landing, built before the wave was dispatched | r2 relaxes the marker to `SOUNDLAW_ERROR`; `reports/round-84/counter-revisions.md` r2 records the red-before |
| R84-M3 | **a frozen contract whose CLI spelling disagreed with its counter** — the wave context named a `selftest` subcommand while the counter invoked `--selftest`; a tool built to the context would have failed SELFTEST | the reference implementation run (`apply-sound-laws.py --selftest` → argparse error) versus the accepted `--selftest` alias after the fix | the L1's reference implementation, written from the frozen contract before dispatch | the tool accepts `--selftest` (alias `selftest`) and the wave context now spells the flag; no claim artifact had landed |
| R84-M4 | **a freeze revision landed after the wave was dispatched** — r2 (`10:31:06`) changed the `SOUNDLAW_ERROR` marker two minutes after `.ready.dispatched` (`10:28:24`), so every seat read the r1 context and any seat receipt naming `--freeze e160a72e` is stale on `FROZENCFG`; the draft revision note called r2 "pre-dispatch" | `.ufo/waves/round-84/w1.ready.dispatched` (10:28:24) vs `git log` r1 `e160a72e` 10:28:17 and r2 `7e6ee2f8` 10:31:06; sentinel finding §2; critic item 1 | the sentinel's scope probe, after the wave | `reports/round-84/counter-revisions.md` r2 is corrected to "pre-data, POST-dispatch" and says which receipts are stale; every verdict is graded at r2 and every cited receipt re-graded by the L1 |
| R84-M5 | **a before-state clause that overstated absence** — claim O's before-text said no committed tool applies ordered sound laws to a lexicon, but `tools/check-craft-exercise.py:45-75` already applies four hardcoded laws (`law_l1`–`law_l4`) inside a bounded exercise checker; the true before is "no general rule-set-driven applier with an external rules file, traces and an arbitrary lexicon" | `tools/check-craft-exercise.py:45-75`; `stage/ConnectorOverlap/overlap.md` §1; `CriticClaims.md` item 4 | the critic seat and the connector independently | the report's before→after table states the narrower true before and keeps the after-state; from r85 a before-state names the nearest existing capability and why it is not the after-state |
| R84-M6 | **counter legs with less kill power than their prose** — `SOURCED` does not check that a cited id exists in the registry (r83's `unknown` clause was dropped), `ROWS` grades only cells 7/8/10 (source/anchor/teaches unread), and `DEMO` runs one input so a tool that copies `expected.tsv` and prints a canned trace passes 8/8 | `CriticClaims.md` items 5–7; `MutationTester.md` §"copy-cheat" and `stage/MutationTester/matrix.json` | the critic and the mutation tester, before any claim landed | recorded as a named limit; the L1 adds a held-out-input check (`stage/L1/heldout.*`) that a copy-cheat fails; the frozen counter amendment is routed to round 85 and cannot change this round's verdict |
| R84-M7 | **a junk mutant that named the wrong expected leg** — the `anchor-two-ids` mutant added a second S-id to one anchor bullet; the ANCHORS leg skips that bullet and its floor still holds (43 >= 20), so it passed, while LINT reported `MULTI-ID`. The battery expected ANCHORS and reported `2/3` | `reports/round-84/telemetry/junk-d84.txt` (first run) versus `junk-d84-r3.txt` (`PASS 3/3`) | the L1's junk run at the D lands | the battery's expectation is LINT, the leg that actually catches it; the named limit (ANCHORS tolerates one malformed bullet above its floor) is recorded in `reports/round-84/counter-revisions.md` r3. The grading legs did not change |
