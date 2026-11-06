# kotodama round 99 — lesson

L1 KotodamaR99 (hyaku run 15, attempt 1). Base `527df3fee305b3454446946e6779ece45456307e`; freeze
`b1b80562edfc8f6082aec74bbbf0f25e152708a8` (`reports/round-99/claims.json`, counter `reports/round-99/predispatch.py`,
battery99 + pin + v10 receipt + critic98-on-v10 receipt + forgery/feasibility controls, all in the freeze commit before
any seat ran). No earlier attempt of round 99 (`.ufo/watchdog.log` has no `lane-dead-no-report kotodama round=99`).

Claims:
- **O (operability, harm repair).** Grader v10 → v11 removes the two false-refusal surfaces the round-98 closure ruled a
  harm (Mc heading marks, F4; bare non-ASCII numeral heading, F1) and the pre-existing virama over-refusal (CriticO98b
  OK-DEVAHEAD), while every v10 refusal stays (battery99 refused=37, critic97 replay, 34 REG lines).
- **C (coverage).** `corpus/knowledge/linguistics/praise-poetry-panegyric.md`: praise poetry as an institution (singer's
  office, patronage and reward, epithet and genealogical recitation, performance order, rivalry and satire), deferring
  praise-names as formula lexicon to `orality-formulaic-language.md` §3.

## Inherited from attempt 1 (re-verified by attempt 2)

Attempt 1 (L1 `KotodamaR99`) froze the claims (`b1b80562`), dispatched w1 (12 seats, all stage dirs `DONE`) and ended
before landing (`.ufo/watchdog.log`: `lane-dead-no-report kotodama round=99`, 07:56:44). Attempt 2 (L1 `KotodamaR99a2`)
reused, after re-verification: grader v11 `717341dc…` (O0–O5 re-run by the attempt-2 L1 on the working tree before any
edit: all PASS), the entry, registry rows S1007–S1017 (census rc 0 at round end, 941 rows), the manifest and captures,
the mutation driver/pin/first receipt (sha `cf58e126…` = pin = receipt line 1), the oath repairs (ScribeOath99 support
table, each span count 1), QUALITY criterion 41 and the README row. Discarded: nothing. Not applied by attempt 1 and
applied by attempt 2: the three CriticC99 content corrections (R99-M2 below). Final measurement:
`reports/round-99/predispatch-lands.txt`.

## Controls before data (freeze commit)

| control | what it skips | counter result |
|---|---|---|
| do-nothing (`reports/round-99/predispatch-base.txt`) | all work | FAIL legs=6/16 (O0, O1, O2, O4, O6, C1, C2, C6, C7, C9 fail) |
| F-O-SHA (`reports/round-99/controls/forgery/F-O-SHA.txt`) | behaviour change (identity only) | O0 PASS; O1, O2, O4, O6 FAIL |
| F-O-LOOSE (`…/forgery/F-O-LOOSE.txt`) | protection (deletes the mark and numbering refusals) | O2 FAIL survivors=2 (CM1, CMW2); O1 FAIL |
| P-O-FEAS (`…/forgery/P-O-FEAS.txt`) | nothing (feasibility, not a candidate) | O2 PASS 0/0/37/0/9/0, O4 PASS overrefusal=0; O1 still 161/161 |

P-O-FEAS keeping 161/161 shows the v10 selftest never pinned the F1/F4 branches, which is why O1 requires one pin per
round-99 class (floor 168) and ExecGraderV11 must show each pin red when its branch is reverted.

## Mistakes

### R99-M1 — refusal widened without a benign twin on the widened set (round 98)

- Class: hardening that widens a refusal predicate (v10: Mn/Me → every category M; a new HEADING-NUMBER loop) with no
  positive control on the newly refused set. battery98 carried one benign twin (ROMANOK) and none for marks.
- Evidence: `corpus/lessons/round-98-verifier-spotcheck.md` §2 (operability harmed: F4 Mc headings, F1 `## Ⅳ.`);
  `.ufo/waves/round-98/w2/ReviewerO98b.md` F1/F4; `.ufo/waves/round-98/w2/stage/CriticO98b/attacks.md` OK-MCWORD.
- Captured-by: none. battery98 counted refusals; mutation98 killed only weakening mutants, never widening ones.
- Fix: battery99's six benign controls (MCOK1, MCOK2, VISOK1, DEVAOK1, NUMOK1, NUMOK2) and counter leg O4 (a
  non-author's benign set, critic98) are frozen before any v11 byte, and mutation99 must carry widening mutants. Shown
  able to fail: `reports/round-99/controls/battery99-control-v10.txt` not-clean=6; `predispatch-base.txt` O4 FAIL
  overrefusal=2; F-O-LOOSE shows the repair cannot be bought by deleting protection (O2 FAIL survivors=2).
- QUALITY criterion 41 (below).

### R99-M2 — a table cell and a setting word outran their captures while every C leg passed (round 99, attempt 1)

- Class: summary-table cell and scene-setting noun written from memory of the case rather than from the capture; the
  frozen legs bind quotes and row cells (C7), not table prose, so they cannot see it.
- Evidence: `.ufo/waves/round-99/w1/CriticC99.md` items 1–3 — §7 Yoruba limit cell "titles are public property, so any
  drummer who knows them can assemble the praise" (`public property` 0 in S1007 and S1009); §6 "At a contemporary Xhosa
  rally … (S1008)" (word-bounded `rally` 0 in S1008, a conference performance); `civilizations/yoruba.md:78-92` and
  `germanic-norse.md:72-90` restated without deferral.
- Captured-by: none (C1–C9 PASS on the defective bytes, `stage/ReviewerC99/counter.txt`).
- Fix (repair, not yet a gate): §6 line reworded to "a contemporary Xhosa performance before a conference audience";
  the Yoruba cell replaced by the corpus's own sourced line (`civilizations/yoruba.md:83`, "an epithet can recall danger,
  contested reputation"), with deferrals to `yoruba.md:78-92` and `germanic-norse.md:72-90` under the table. Check:
  `grep -c 'public property\|Xhosa rally' corpus/knowledge/linguistics/praise-poetry-panegyric.md` → 0 (was 2 at
  attempt-1 bytes). Not counted as a captured-by fix: no gate fails on the old bytes yet. Routed to round 100: a
  table-cell support check over §-tables whose caption claims recorded cases.

## Gate

Every new row S1007–S1017 was opened by ScoutSources99 and re-opened by ExecRegistry99. The L1 also re-opened every row on 2026-11-06: `reports/round-99/l1-reopen/results.json` (HTTP 200 and quote count 1 for 11/11). Quotes below are counted on the named shipped capture; the L1 receipt records fresh-byte digests, HTTP/rc and counts; shipped captures remain under `reports/round-99/evidence/`.

| id | URL | access | tier | status | located quote (≤25 words) | capture file | capture sha256 |
|---|---|---|---|---|---|---|---|
| S1007 | https://archive.org/download/80204dff-c8a9-4155-a539-7ee980102875/80204dff-c8a9-4155-a539-7ee980102875_djvu.txt | 2026-11-06 | B | mined | “In return the ruler acknowledges their praise by gifts or money which are often given publicly.” (16 words; count 1; body of S1007.txt) | S1007.txt | `73df25c214bd03c2a36784c9d7faef3adaeb265b8ef1a7566713493a09f892b8` |
| S1008 | https://journal.oraltradition.org/wp-content/uploads/files/articles/3iii/6_opland.pdf | 2026-11-06 | A | mined | “it is his duty to greet Lord with a royal praise name” (12 words; count 1; body of S1008.txt) | S1008.txt | `112fdd45b5e24828fc9df0410e265c8801a909bfef0ae661f9654a1bdd64d3e9` |
| S1009 | https://journal.oraltradition.org/wp-content/uploads/files/articles/20ii/Barber.pdf | 2026-11-06 | A | mined | “Obscurity in praise poetry could be deployed for political reasons.” (10 words; count 1; body of S1009.txt) | S1009.txt | `3f704d182cd42e6777adae87104a03c343318762ec3227ad089a8580d43a1215` |
| S1010 | https://journal.oraltradition.org/wp-content/uploads/files/articles/16i/Groenewald.pdf | 2026-11-06 | A | mined | “The praise poem for kings and chiefs has also been adapted to serve the trade union movement” (17 words; count 1; body of S1010.txt) | S1010.txt | `9012091306dcb31614f0d47a95870f984af3324690b6f2827bc2fe588f7e73d0` |
| S1011 | https://www.journal.oraltradition.org/wp-content/uploads/files/articles/10i/8_kaschula.pdf | 2026-11-06 | A | mined | “directed at the Chief, decrying what was unworthy, praising what was worthy” (12 words; count 1; body of S1011.txt) | S1011.txt | `499cd45fbdc4f5e42a4310afd43e93d97e8069be7e0e64c8e18d3e84cd2462f8` |
| S1012 | https://www.gutenberg.org/cache/epub/10717/pg10717.txt | 2026-11-06 | A | mined | “Yet praise is overtaken of distaste, wherewith is no justice, but from covetous men it cometh” (16 words; count 1; body of S1012.txt) | S1012.txt | `d8823d133ebb59059827379baca2af38ba5e36209d3d7fd553c0f5976dde5074` |
| S1013 | https://www.gutenberg.org/files/9842/9842-h/9842-h.htm | 2026-11-06 | A | mined | “A more choice act of mine will be To celebrate thy praise in song” (14 words; count 1; body of S1013.txt) | S1013.txt | `594b3caeb20232af055530e36f153da090317bb7bb955469497e7b6c5a449753` |
| S1014 | https://archive.org/stream/book-3-purananuru/BOOK3-Purananuru_djvu.txt | 2026-11-06 | B | mined | “The main themes found in Purananuuru are praise of the ruler, patronage, heroism in battles” (15 words; count 1; body of S1014.txt) | S1014.txt | `2042577c69e571c1ac0be78a9872612a50d365f3ad8b5e05e0709b80f87a0591` |
| S1015 | https://journals.uni-goettingen.de/wom/article/download/2303/1986/5234 | 2026-11-06 | B | mined | “the praise-singing function is by far the most obvious and audible manifestation” (12 words; count 1; body of S1015.txt) | S1015.txt | `6b50724cf0bc32dcb7fa41376b446fb23224ac118a0da6ac29321188617a5be2` |
| S1016 | https://www.asnc.cam.ac.uk/resources/mpvp/wp-content/uploads/2013/02/Introduction-to-Skaldic-Poetry_Debbie-Potts.pdf | 2026-11-06 | B | mined | “There certainly was money in poetry for the skald; court poets would receive generous rewards” (15 words; count 1; body of S1016.txt) | S1016.txt | `e72c8e13d55cd152439aba2fca541885f9e4b9b23a64452e5e538264ac5e4bb3` |
| S1017 | https://mural.maynoothuniversity.ie/id/eprint/19500/1/Kavanagh%20Emer%20Signs%20and%20Wonders.pdf | 2026-11-06 | B | mined | “a poet should not satirize or over-praise a subject, as the fili depended on the wealth of his patron” (19 words; count 1; body of S1017.txt) | S1017.txt | `4a54f3a8cb9600f98810af0217e83b0a1d5090773f48b73673192b097aa9d63c` |

All eleven rows: absent → mined, recheck 180d, used-by `corpus/knowledge/linguistics/praise-poetry-panegyric.md`. No old status/recheck/used-by changed. No row added then superseded.

Rejected candidates (ScoutSources99 `candidates.md` §Rejects; full opened-candidate list and per-attempt records in `candidates.json`):
- C6, Encyclopaedia Iranica court-poetry entry: access reason, HTTP 403 Cloudflare wall, 3 article attempts and 1 PDF-endpoint attempt; flip: an openly served mirror or open scholarly study. No bypass.
- C8, Skaldic Project introduction: access reason, 3 attempts with curl rc 28 / HTTP 000, 0 bytes; flip: a successful ordinary fetch or printed open volume. Potts (S1016) supplies the bounded introduction instead.
- C14, Gourlay on northern Nigerian trumpets: scope reason, HTTP 200 but the praise-patronage passage is a short aside in an organological study; flip: a dedicated account of Hausa maroka patron exchange opened at source. This rejects the proposed row scope, not the accuracy of its isolated quote.

Search: 14 queries, 14 opened candidates, 11 admitted, 3 rejected; stop rationale: the admitted set covers the praise singer's office, audience, patronage/reward, epithets, genealogy, satire and rivalry across African, Welsh, Greek, Tamil, Norse and Irish examples. `ScoutSources99/candidates.md` preserves the query strings and exclusions. No claim to exhaustive comparative coverage.

Outside discernment spot-check: pending the orchestrator's non-author closure; dispatched seats are still this lane, so their agreement is not outside admission.

Assimilation: none (no shokuknow package adopted). `considerthese/` is absent. No operator-lesson files were present under `corpus/lessons/operator-*.md`.
