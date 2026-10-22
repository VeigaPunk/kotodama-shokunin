# CriticClaimD — round 53, attack on claim D's design (depth, repair-first)

- Seat: `KotodamaR53.CriticClaimD` (critic, leaf). Wrote only this file in the lane. Scratch work in `/tmp/critd/` (copies of the entry and `corpus/SOURCES.md`, plus one `git clone --shared` at `60f1d2a` for the separability run). No lane file was edited, and no git or jj write was run in the lane.
- Read in full: `reports/round-53/claims.json`, `reports/round-53/d-count.py`, `corpus/lessons/round-52-verifier-spotcheck.md`, the D entry, and the round-52 seat tables `ScribeSec08Ecology.md:84-91` and `ScribeSec14Calibration.md:36-47`. Peer report read: `.ufo/waves/round-53/build/ScribeDFragments.md`.
- Lane state observed: HEAD `60f1d2a` (the declaration). The entry is byte-identical at `a9cf95f` and `60f1d2a` (`git diff --stat` is empty). At my first run the counter printed `OPEN 18`, `SID_BAD 0 [] cited 50`, exit 1. Later in this session the worktree carried **uncommitted D edits** (8 lines: 105, 106, 107, 113, 174, 177, 179, 181), and the counter printed `OPEN 6` (OVER1–OVER6 open), `SID_BAD 0 [] cited 50`. The "Landed lines" section below attacks those bytes.
- Tool installs: none.

## Axes

| axis | how D can move it | how D can harm it |
|---|---|---|
| depth (citation correctness) | stable ids replace draft fragments; right rows carry each quote; over-reads are cut to what the page says | a phrase leg is reworded around rather than repaired; a supported detail or quote is deleted; a fragment is dropped and its detail loses its only support |
| calibration (registry truth) | not claimed | a row's `used-by` names the entry after its last cite is removed; registry `teaches` cells keep the over-read that the entry drops |
| separability | none | D's repair rests on a C row (S187 and up), C's `SOURCES.md` bytes, a C seat's draft id, or the round-53 lesson |

## Result in one paragraph

Claim D's statement is exactly the counter's predicate, and the counter is honest about its limit (`d-count.py:18-19`; `claims.json` `method_not_statement`). But the predicate is easy to satisfy without repair. **A single scratch rewrite that keeps all six over-reads, and keeps all ten fragments in disguised forms, prints `OPEN 0`, `SID_BAD 0` and exit 0** (scratch `evade`, below). Three further defects come from re-opened pages, not from the counter:

- **OVER6 is a mis-routed item.** "primitive peoples" *is* on S181's page, so the counter forces deletion of a verbatim, supported quote.
- **Two registry rows already carry the over-read wording** (S147 and S151 `teaches` cells), so an evasive rewording would look row-backed.
- **The landed line 113 cites the right row but still over-reads it.** S159 says the language "is about to lose its communication function"; the entry says it "lost its daily function".

Closing D therefore needs per-instance review evidence (below), not the counter's zero.

## 1. Phrase legs: rewordings that reach 0 and keep the over-read

Re-opened this session by plain `curl` (no challenge served; Dictionary.com loads a reCAPTCHA v3 script but served the content):

- S135: PDF p. 7 of 17, the paragraph opening "In tonal languages, the possibility of transmitting complex sentences": "in tonal languages with low informational load on spoken pitch, whistled sentences are more formulaic and therefore more predictable". The PDF names no Hmong country ("Laos" 0 hits; "Thailand" only for Akha; "United States" only in an author affiliation). sha256 `2302a811…`.
- S147: printed p. 839, §2.3 column 2: "The occlusive [p] is expressed mainly with this process and is therefore very similar to [k] in whistles." [b] is named only as sharing the labial glottal compensation. sha256 `f38dd216…`.
- S151: Description block: "David Yetman and Mark Sicoli elicit spoken and whistled Chinantec from children in San Pedro Sochiápam". Nothing on age of learning. sha256 `f6959235…`.
- S181: Collins noun sense, as served: "a means of communication between primitive peoples over large areas, as by drum beats". Random House sense 1 carries "natives of a jungle or bush region". sha256 `b19b9a03…`.

| leg | regex (`d-count.py:32-37`) | evasions that print 0 and keep the over-read (each run in scratch `evade` or by regex inspection) | what the closure needs to tell repair from evasion |
|---|---|---|---|
| OVER1 | `force fixed formulas` | "forces fixed formulas" (run); "force formulaic messages"; "require fixed formulas"; a no-break space or zero-width character inside the phrase | the cell no longer states a causal or forced link from the Suruí tone count to fixed formulas; the wording is no stronger than "more formulaic and therefore more predictable" (S135 PDF p. 7) |
| OVER2 | `\(Laos, Thailand, United States\) \(S135\)` | "(Laos, Thailand and the United States) (S135)" (run); "(… United States; S135)"; adding a second id "(S135; S141)". S141 (Morrison 1998) does name Laos, Thailand and California, but **for the qeej, not whistled speech**, so "(S135; S141)" would be a scope over-read that looks row-backed | any Hmong country list left in the whistled-tonal row is on the page of a row about *whistled* Hmong (S144's list on line 78 is "Laos, Thailand, French Guiana" and needs its own page check); otherwise the list is cut |
| OVER3 | `/b/[^|]*merg\w* with /k/` | "/p/ and /b/ approaching /k/" (run). **This is the wording of S147's own `teaches` cell** ("lip-locked /p/, /b/ approach /k/"), so the over-read survives in the registry and launders an evasion. Also "[b]", "fall together with /k/", "close to /k/" | line 76 attributes the [k]-likeness to [p] only (S147 p. 839); no form of /b/ or [b] plus merge, approach, similar or close to /k/ remains |
| OVER4 | `learned young` | "transmitted young" (run). **This is the wording of S151's own `teaches` cell** ("the register is transmitted young"). Also "learnt young", "acquired in childhood", "learned early" | line 79 states only that the deposit was elicited from village children (S151), or marks the age claim `(to-verify)` |
| OVER5 | `in Akan \(Ghana\) practice` | "in Akan practice (Ghana)" (run); "in Ghanaian Akan practice"; "in Akan court practice" | line 121 names one drummer's appointment as one biography (S165's own `teaches` cell already says "not the wider Akan institution"); no Akan-wide generalisation remains |
| OVER6 | `primitive peoples` | a no-break space (run); "primitive people"; curly-quote split | **no repair is owed: the sub-quote is on S181's page (Collins sense, quoted above).** The round-52 closure's finding (`round-52-verifier-spotcheck.md:81`) does not hold on today's page. The counter forces either deleting a correct verbatim quote (a depth loss) or an evasion |

Fragment leg, same scratch run: `; -6`, `,-12`, `,− 5` (U+2212 minus), `, –2` (U+2013 en dash) and `; NEW-ScribeSec08Ecology-6` all escape `, -[0-9]+\b`. Wholesale deletion (`drop` run) zeroes FRAG too. The `NEW-<Seat>-<n>` form is the one C is told to use, so a D line can carry a seat draft id and still count 0.

Scratch receipts (`python3 -B reports/round-53/d-count.py --root /tmp/critd/<run>`):

| run | edit | OPEN | SID_BAD | exit |
|---|---|---|---|---|
| `evade` | all evasions above, plus S163's decline claim moved to line 105 | 0 | 0 | 0 |
| `faithful` | each fragment mapped exactly to its seat draft row, nothing else | 7 (OVER1–6, WROW2) | 0 | 1 |
| `drop` | every `, -N` deleted | 8 (OVER1–6, WROW1, WROW2) | 0 | 1 |
| `s187` | line 174 cites a fake S187 whose `used-by` names both entries | 17 | 0 (cited 51) | 1 |

## 2. WROW1 and WROW2: is "absent = open" right, and can they be gamed?

"Absent = open" is right. It blocks the cheapest evasion, deleting the quote, and so protects depth (a missing "working their farms" or "mobile phone" line counts 1).

Ways to game or break the legs:

- **Line level, not clause level.** WROW1 passes if "S162" appears anywhere on the line, including against the wrong clause (for example "(S159; S162)" at the end of a two-clause cell). It is also a bare substring test (`d-count.py:67`), so "S1620" passes.
- **WROW2 sees only lines containing `mobile phone`** (`d-count.py:69`). The `evade` run kept "mobile phones arrived (S159)" on line 113 and moved "handsets ended the whistle's daily use there (S163)" to line 105. The leg passes while the wrong-row attribution survives.
- **WROW2 conflicts with D's own method.** The faithful map of line 113's seat draft is `NEW-ScribeSec08Ecology-3, -4` = **(S163, S159)** (`ScribeSec08Ecology.md:41`, `:86-87`). The `faithful` run leaves WROW2 open. ScribeDFragments' "option B" ("lost its daily function (S163) once mobile phones arrived (S159)") also keeps S163 on the line, so the leg counts it open. To close the leg, S163 must leave line 113.
- **The counter cannot see an orphaned row.** S163 was cited only on line 113. Removing it would leave `corpus/SOURCES.md` row S163's `used-by` naming the entry with no cite (false provenance in C's land). SID_BAD checks only cited-to-row, not row-to-cited. In the landed worktree S163 moved to line 105 with a new quote, so the reverse check is clean ("50 rows name the entry, 0 uncited"). That rescue is a new claim, verified below.
- **The docstring says "S159 alone" but the predicate allows other ids** (`d-count.py:11` against `:70`). This is a documentation slip only.

## 3. Is the statement exactly the counter's predicate?

The measured part matches. The statement asserts only "prints OPEN 0 and SID_BAD 0", and `method_not_statement` concedes that support is a review question. Two parts are wider or wrong:

- **The gloss is wrong for one of 18.** "6 over-read phrases" includes OVER6, which is not an over-read on today's page (§1). The base value is true as a count (18 routed instances), but the claim's description of what was repaired overstates by one. The closure should say "17 repaired, 1 routed in error and explained".
- **The falsifier is wider than the counter, which is safe but unenforced by D's argv.** "A cited S-id from S187 upward" is not tested by `d-count.py`: the `s187` run prints `SID_BAD 0`. It is caught only by the separability checker's static export leg (see §5). The review clauses ("states something its cited row's page does not carry"; "a fragment was dropped where its source detail lost all support") have no instrument at all.

## 4. Is D a depth move, and can it harm depth?

Yes, it is depth: stable ids, right rows and right-strength claims on existing content. It harms depth if:

- **OVER6 is executed as routed.** It deletes a verbatim quote that S181 carries. The smallest safe form keeps the fact without the routed string, for example: `senses frame non-Western people as "natives of a jungle", and Collins defines it as communication between peoples it calls primitive (S181)`. Record it as "routed in error, explained", not as "repaired".
- **Fragments are dropped instead of mapped.** On the base line 177 (`, -6` = S176, "single-word messages expand into conventionalised set phrases") the fragment was the only support for "adds formulaic redundancy". S179 (Akinbo) teaches tone only.
- **Over-reads are cut, not re-scoped.** Deleting the Akan, Chinantec or Hmong examples outright loses evidence that a narrower wording keeps (drafts below).
- **Registry and entry are left disagreeing.** After a correct repair, S147's and S151's `teaches` cells still state the over-reads the entry dropped. That is a duplicate authority in C's land (`SOURCES.md`). It is not D's to fix, but it must be routed, or the next integrator will re-import the over-read from the row.

## 5. Separability: ways D can silently depend on C

Run on a `git clone --shared` scratch at `60f1d2a`, with stubs for absent lands. D's entry cited S187, named `corpus/lessons/round-53.md`, and cited "Kendon 2004 via NEW-ScribeGesture-3". `python3 -B tools/check-claim-separability.py reports/round-53/separability-manifest.json --lane <scratch> --root <scratch>` gave:

- `SEPARABILITY_DEPENDENCY D->C via export '\bS(18[7-9]|19[0-9]|2[0-9][0-9])\b' matched …:174`: caught.
- `SEPARABILITY_DEPENDENCY D->REC via land path 'corpus/lessons/round-53.md' named at …:181`: caught. But the checker's docstring (`tools/check-claim-separability.py:20`) says "claims may depend on [records]". A judge reading the docstring could wave a D->REC finding through. For D, `must_not_cite` makes it a breach.
- **Not caught:** a C source cited by author-year or URL without an S-id, and a C seat's `NEW-<Seat>-<n>` draft id. Neither matches the export regex, and SID_BAD ignores both.

Other silent couplings:

- **D's `used-by` truth lives in C's land.** D removed S163 from line 113. Any `used-by` correction (or S147 and S151 `teaches` fixes) can only ride in `corpus/SOURCES.md`, which C lands. D's acceptance reads `SOURCES.md` (`d-count.py:50-55`), so C's integration edits to rows S157–S186 can flip D's SID_BAD.
- **The gate is not D's instrument.** The draft-id gate `tools/check-draft-ids.py` is a REC land. If it shares the `, -[0-9]+` regex it inherits every §1 blind spot. It must not be offered as D's evidence.
- **The lesson must not certify D.** The mined mistake ("bare draft-id fragments left at integration") is C's and REC's frontier. If the lesson quotes D's repaired lines as its proof, it must not be cited back from D.

## Landed lines (uncommitted worktree, read during this session)

| line | landed change | verdict |
|---|---|---|
| 105 | adds `UNESCO ties the practice to terrain that "required the local population to find an alternative way to communicate across long distances" (S163)` | **supported, but a new claim.** The quote is verbatim in Wayback capture `20261004145450id_` of `https://ich.unesco.org/en/usl/whistled-language-00658` (HTTP 200). It keeps S163's `used-by` true. The round-52 closure says S163's live page served a captcha; check that row S163 records "challenge met, not passed" (QUALITY criterion 10), as S186 now does for S157 |
| 106 | `(S159)` for the shepherds quote, `(S162)` for "working their farms" | correct; matches the seat map and ScribeDFragments' re-opened S162 printed p. 152 |
| 107 | `(S160, S162)` | correct per map (`NEW-ScribeSec08Ecology-6` = S162) |
| 113 | `lost its daily function once mobile phones arrived (S159)` | **right row, residual over-read.** S159 (Wayback `20201217075537id_` of `36234-EN.doc`, sha256 `85b777c9…`, §2 "Need for urgent safeguarding"): "Today, however, it is about to lose its communication function." The entry states a completed loss. Smallest correction: `as the Turkish whistled language, which its nomination file says "is about to lose its communication function" since mobile phones spread (S159)`. This does not change the counter |
| 174 | `documented for named communities and instruments (S179, S174); that most tonal languages have none is (to-verify)` | improves depth: drops "small set", which S174 ("found all around the world on a wide variety of instruments") pushed against, and marks the unsupported half |
| 177 | `encodes tone and rhythm, not segments (S179, S139), and leans on stock phrases whose extra length makes them identifiable (S152)` | **departs from the declared method** (fragments -5, -6, -7 = S174, S176, S175 were not mapped; three different rows now carry a reworded claim). Support looks adequate from the row cells (S139 rhythm; S152 "stereotyped phrases whose extra length raises identifiability"), and no row is orphaned (S174, S175 and S176 are still cited on lines 170–174 and 181). The report must record it as a rewrite, not a fragment mapping |
| 179 | `-12` (S180) dropped and S180 not added | departs from method ("dropped where the S-id is already on the line" is false here); support holds through S183 (Decision 12.COM: parent-child transmission, 2017 inscription) |
| 181 | `(S173, S157)`, `(S173, S180)` | correct per map |
| 54, 76, 79, 121, 176 | unchanged; OVER1–OVER6 still open | see the drafts below |

Drafts for the open phrase legs (each reaches 0 by repair, not evasion; paste into the named cell):

- Line 54, reach cell: `Same whistle physics, but a rich tone system (Chinantec) allows unpredictable sentences, while with two level tones (Suruí) whistled sentences are "more formulaic and therefore more predictable" (S135)`. Example cell: `Chinantec (Oaxaca, Mexico); Hmong (S135)`; the country list stays on line 78 under S144.
- Line 76, drops cell: `band overlap between vowels, and lip-locked [p], which comes out "very similar to [k] in whistles" (S147)`.
- Line 79, terrain cell: `Oaxaca; the archive deposit holds spoken and whistled Chinantec elicited from children of the village (S151); the age of learning is (to-verify)`.
- Line 121: replace `in Akan (Ghana) practice a master drummer is` with `in Ghana one Akan master drummer, Kwaku Kwaakye Obeng, was`, keeping the S165 quote and citation.
- Line 176: `senses frame non-Western people as "natives of a jungle", and Collins defines it as communication between peoples it calls primitive (S181)`, recorded as "routed in error, explained" (§4).

## Falsifiers wave 2 must run on the landed lines

1. **Counter:** `python3 -B reports/round-53/d-count.py` → `OPEN 0`, `SID_BAD 0`, exit 0.
2. **Normalised fragment sweep** on lines added since `a9cf95f` (`git diff -U0 a9cf95fe -- <entry> | grep '^+'`). Zero hits are required for: a dash-like character (`-`, U+2010–U+2015, U+2212) followed by digits before `)`, `,` or `;`; `NEW-`; and `[,;(]\s*-\s?\d`.
3. **Hidden-character sweep:** zero new U+00A0, U+200B–U+200D, U+2060 or U+FEFF in the entry.
4. **Widened phrase sweep** after NFKC normalisation and whitespace collapse. Each pattern must have 0 hits, or the hit must be shown on the cited page:
   - `forc\w*\s+(fixed\s+)?formul`
   - `Laos,?\s+Thailand,?\s+(and\s+)?(the\s+)?United States` (line 58's hit under S141 is supported for the qeej; line 54's is not)
   - `[\[/]b[\]/][^|]{0,60}(merg|approach|similar|close|fall)\w*[^|]{0,30}[\[/]k[\]/]`
   - `(learn|transmit|acquir|taught)\w*\s+(young|early|in childhood)`
   - `Akan[^|.;]{0,40}(practice|institution|custom|tradition)`
   - `primitive\W+peoples?` (allowed only as an exact S181 quote, if the L1 keeps it)
   At the base worktree each pattern hits exactly the routed line (and line 58), so the patterns are calibrated.
5. **Per-instance support table, from a non-author reviewer.** For each of the 18 instances: before text, after text, cited row, and the verbatim carrying sentence with its location on the re-opened page (S135 PDF p. 7; S147 p. 839; S151 Description block; S159 §2; S162 printed p. 152; S165 "About"; S181 Collins sense). An instance without a quote fails.
6. **Reverse provenance:** every `SOURCES.md` row whose `used-by` names the entry is still cited by it (currently 50 of 50), and no `teaches` cell of a row the entry cites states a wording the entry dropped as an over-read (currently S147 and S151 fail; route to the SOURCES land).
7. **Ceiling and separability:** `python3 -B tools/check-claim-separability.py reports/round-53/separability-manifest.json` with no D->C and no D->REC finding. Also grep D's added lines for author-year or URL citations that resolve to no row S001–S186.
8. **Method conformance:** each mapped fragment equals its seat draft row (Ecology -4 = S159, -6 = S162, -3 = S163; Calibration -2 = S157, -5 = S174, -6 = S176, -7 = S175, -12 = S180). Each deviation (currently lines 177 and 179) is listed with the reason and the row that now carries the detail.
9. **Red control:** on a scratch copy of the landed tree, re-insert one routed string (for example `learned young`). The counter must show `OPEN 1`, exit 1. Re-insert one disguised form (for example `transmitted young`) and record that the counter stays 0, so the closure knows the review in falsifiers 4 and 5 is load-bearing.

## Smallest safe corrections

- Keep the counter as declared (it is frozen). Add falsifiers 2–6 to the wave-2 review receipt, and name OVER6 in the closure as routed in error.
- Before commit, fix the line 113 tense over-read ("is about to lose"). Land the five phrase drafts above, or equivalents that pass falsifiers 4 and 5.
- Route to the SOURCES land (C or REC, not D): correct the S147 and S151 `teaches` cells; confirm S163's access note; fix S159's anchor label ("§D Brief textual description" is not a heading in the document, per ScribeDFragments §7).

## Unrun checks

- I did not run `accept-c.py`, `dry-run.py` or `claims-agree.py` (lane gates; out of scope).
- I did not re-open S144, S152, S164, S165, S174, S175, S176 or S179 pages. My line-174 and line-177 verdicts rest on the registry cells and on ScribeDFragments' quotes.
- I did not check S140's page for the Hmong countries: its HTML loads by script, and plain curl returned no text body.
- The landed-line verdicts apply to the uncommitted worktree as read this session. The bytes may change before commit, so re-run falsifiers 1–9 on the commit.
