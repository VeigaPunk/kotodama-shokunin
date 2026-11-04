DRAFT — round-88 lesson fragment for L1 integration (NOT FILED).
Seat ScribeRowsLesson, kotodama round 88, 2026-11-04.
Pins: base 4956282281dac1306cfbe59523e46dde99749d75; pre-dispatch controls
0c8c733088df8c4f06770c9e714360eed7f29272; frozen claims and counter
4b76524c51e1c2f76c99eeb3b629cfac08a44a76. Two claims, distinct axes: O
(operability, capability acquisition) and D (depth, knowledge deepening).
This draft files no lesson under corpus/lessons/, edits no QUALITY entry, no
SOURCES row, no SCORECARD line and no LOG line. The Source Gate for the three
new rows is in stage/sources-rows.txt; this file supplies the Gate prose, the
mistakes, and the routed-defect dispositions.

================================================================================
## Gate
================================================================================

Own-work sources opened on 2026-11-04. The three external rows (S931 Terrain
paper, S932/S933 MacTutor pages) are Tier A/B scoped to the notation typology
only; their URLs, access dates and verbatim quotes are in
stage/ScribeRowsLesson/sources-rows.txt, and the copies are in this stage's
receipts/. No external source is cited anywhere else in this draft.

- S931 admit A/mined, scoped to the paper's own two-axis typology of numerical
  notations. Source: https://journals.openedition.org/terrain/17506 — accessed
  2026-11-04 — §"Classifying numerical notations", paragraph 7 (2018):
  「All numerical notations fall into five basic typological categories, across
  two dimensions」 (12 words). Grounds: two questions — how signs are formed
  within a power of the base, and how powers are combined into a numeral phrase
  — cross into five types. Re-open evidence: the 2025-10-23 same-page Wayback
  capture carries the same sentence. Seat: ScribeRowsLesson.
- S932 admit B/mined, scoped to the sexagesimal system's structure and its
  missing zero. Source:
  https://mathshistory.st-andrews.ac.uk/HistTopics/Babylonian_numerals/ —
  accessed 2026-11-04 — body paragraph on the empty position: 「A much more
  serious problem was the fact that there was no zero to put into an empty
  position.」 (19 words). Grounds: positional-without-a-zero is ambiguous where
  spacing cannot help. The 2026-10-13 same-page capture is byte-identical to
  the live copy. Seat: ScribeRowsLesson.
- S933 admit B/mined, scoped to the Egyptian decimal hieroglyphic numeral set.
  Source: https://mathshistory.st-andrews.ac.uk/HistTopics/Egyptian_numerals/
  — accessed 2026-11-04 — body paragraph on the numeral hieroglyphs:
  「separate symbols for one unit, one ten, one hundred, one thousand, one ten
  thousand, one hundred thousand, and one million」 (20 words). Grounds: base
  and positionality are independent design choices. The 2026-10-21 same-page
  capture is byte-identical to the live copy. Seat: ScribeRowsLesson.
- REJECT candidate A (claim-level, no S-id). The overstrong teleological
  universal claim — that numeral notations universally progress toward a perfect
  decimal positional system — is refused for the entry. Source:
  https://journals.openedition.org/terrain/17506 — accessed 2026-11-04 —
  §"Classifying numerical notations", paragraph 10 (2018): 「This avoids the
  teleological argument of Ifrah (1987) and Dehaene (1997) that sees decimal,
  positional numeration as the end-point of a developmental sequence towards
  perfection.」 and 「In fact, using this typology it is evident that there is no
  perfect system.」 Grounds: the opened source says no perfect system exists, so
  the universal claim has no support in the source being cited and the entry
  must present the typology as a classification with no summit. Flip: admit the
  universal progression claim only if a source is opened that states it as its
  own finding, and the no-perfect-system sentence is withdrawn from the entry.
  Re-test tool and verbatim output: stage/ScribeRowsLesson/receipts/reject-retest.txt
  (grep over the saved S931 bytes; both needles HIT). Seat: ScribeRowsLesson.

Search bound: three URLs opened plainly plus two DOI probes that failed; the
existing registry was grepped for the three URLs and for Chrisomalis, Ifrah and
Dehaene (no prior rows). No package adoption, no source-recheck wave, no
external non-author spot-check this round; the S931/S932/S933 rows await the
non-author re-open that QUALITY criterion 10 requires.

================================================================================
## What the two frozen claims add, and what they do not
================================================================================

O's frozen predicate is a finite exact-set discrimination over one committed
13-case battery and four committed counterfeits. Measured at the freeze
revision with the frozen counter (receipts/measure88-O-at-freeze.json), the five
score legs already read honest 13/13, constant-pass 3, shotgun-all-labels 4,
extra-id 4, filename-only 0 — every score leg passes — while the three
battery legs fail because tools/check-finding-sets.py does not exist at any
revision yet (git log --all over that path returns nothing). 6 of 9 legs pass
at the freeze revision; the claim is therefore NOT met at the freeze, and this
draft does not assert that it is met anywhere.

The counter's own docstring says "filename-oracle 1" while its EXPECT table
says 0 and the frozen claims say 0; the measured value is 0. That is a
comment/code drift inside a frozen file, reported here and not edited.

D's frozen predicate is a section, a table, three cited and mined rows, and
2500 bytes of growth. On a scratch git fixture carrying the drafted section and
the three drafted rows, the frozen counter returns rc=0 with all 7 legs passed
(receipts/measure88-D-on-fixture.json). That is a fixture measurement of draft
bytes; the lane tree at 4b76524c still has no 4b heading, no S931-S933 and
zero growth, and the D claim reads 1/7 at the base revision
(receipts/measure88-D-at-base.json).

================================================================================
## Mistakes
================================================================================

| id | class | evidence | captured-by | fix or retained limit |
|---|---|---|---|---|
| R88-M1 | vacuous — a membership check cannot see a set difference | R87-C1 (membership semantics in the inherited counter) against the committed pre-dispatch controls | QUALITY 11/19/23/34 | The round-88 controls answer R87-C1 with the exact-set comparator and a 13th case. Measured on the frozen counter: shotgun-all-labels 4/13, extra-id 4/13, filename-only 0/13, honest 13/13 (receipts/measure88-O-at-freeze.json). The counterfeits now fail on set equality rather than on filename shape alone. This is the finite discrimination the O claim asserts, and nothing wider. |
| R88-M2 | vacuous — a transport selftest that passes on a crashed child | the frozen counter's own `--selftest`, re-run this round | QUALITY 34 (already filed, binding from round 88); new criterion 35 drafted by another seat | The frozen `measure88.py --selftest` exits 0 and prints three checks all `passed: true`, but its nominal exact-accepted positive child exits 1 with a FileNotFoundError traceback — it treats a JSON body as a pathname — and the extra-id check is assigned success independently of the observed outcome. Measured here: `python3 -B reports/round-88/probe-counter-selftest.py --work <dir>` prints `false_green: true`, `child_rc: 1`, `suite_rc: 0` and exits 1 (receipts/probe-counter-selftest.json). This is a false green in the frozen instrument's own transport layer, not in the domain comparator. The frozen counter is NOT repaired and NOT re-scored here; the finding is disclosed so that the `battery-selftest:exit` leg is read as a transport fact only, never as evidence that a production comparator's selftest is sound. |
| R88-M3 | stale premise — the inherited counter was said to be the one at fault | reports/round-88/pre-dispatch.json, inherited_r87_counter | QUALITY 17/19/23 | The pre-dispatch receipt records the inherited counter accepting shotgun-all-labels, extra-id and filename-only at 12/12 each while the honest auditor also scored 12/12 — that is the red-before evidence. It is not a claim that the inherited counter was re-scored; the inherited counter's bytes are unchanged. |
| R88-M4 | vacuous — a finite set of forgeries is not anti-forgery proof | author's own probes this round, receipts/probe-refusal-and-null.json, probe3.py, probe5.py, probe6.py | QUALITY 34 (already filed, binding from round 88) | Four further forgeries were built and scored against the frozen counter and are recorded as limits, not as kills of the claim. (a) An always-red tool and a blanket-refusal tool each score 0/13. (b) A findings:null tool scores 0/13 with no traceback — the frozen counter's evaluate() treats a non-list findings value as an empty list, so the malformed-output case fails closed instead of crashing the counter. (c) A case-name-keyed oracle scores 0/13 because the counter writes opaque case filenames. (d) A content-hash memorizing oracle that carries the full expected (rc, ids, records) table for every case payload scores 13/13 — a memorizing forgery passes a battery whose cases are fixed and enumerable. QUALITY 34 already says random filenames alone do not defeat content memorization; this round measured that gap on the round-88 battery itself. The O claim's bounds already exclude arbitrary-forgery resistance, so no claim is broken; the gap is a bound, stated. |
| R88-M5 | stale premise — a source quote does not certify the claim built on it | S931 paragraph 10 read directly in the saved bytes | QUALITY 33 | The teleological universal claim is refused on the source's own sentence, and the re-test output (grep over the saved bytes, both needles HIT) is carried in the Gate line rather than asserted. |
| R88-M6 | scope — the notation typology is method, not history | S931, S932, S933 row scopes as drafted | QUALITY 1/2/5 | The rows carry A/B scoped to what each source states; the entry section says method and reference, not canon, and does not decide what was true of any historical notation system. writing-systems.md keeps ownership of scripts. |
| R88-M7 | underived — a citation list that carries no S-id | the numerals entry as it stands | QUALITY 15 | The proposed section cites S931/S932/S933 only in prose lines and never inside a table row; `tools/check-cited-lines.py` on the section returns 0 findings, rc=0. The pre-existing header's citation list is unchanged. |

================================================================================
## Routed defects: disposition of every R87 item
================================================================================

Nothing here is claimed fixed without a receipt. Each line states what the
round-88 bytes actually show.

| item | disposition at round 88 | evidence |
|---|---|---|
| R87-C1 (counter accepts expected-id membership) | ADDRESSED for the new comparator only. The frozen round-88 counter compares the finding-id set and the (id, record) pairs for equality, and the 13th case is a two-id case a membership check cannot pass. The four committed counterfeits now score 3/4/4/0 instead of 12/12. The frozen round-87 counter is NOT repaired and NOT re-scored: its bytes are unchanged, as R87-C1 itself required. | reports/round-88/pre-dispatch.json inherited_r87_counter (12/12 each) vs receipts/measure88-O-at-freeze.json (4/4/0) |
| R87-C2 (total=12 literal in the TOOL_ABSENT branch) | ADDRESSED in the new counter. measure88.py has no TOOL_ABSENT branch; a missing input returns INPUTS_ABSENT with rc=2 and no total literal. The frozen round-87 file keeps its literal, unchanged. | `measure88.py --root . --base 000…0 --lands 000…0 --claim O` returns {"finding": "INPUTS_ABSENT"} rc=2, no total field |
| R87-C3 (S929's 13-word quote prefix drops the supporting clause) | NOT ADDRESSED and NOT IN THIS SEAT'S SCOPE. S929 is a row in corpus/SOURCES.md and the correction is a superseding row plus a sweep of the lesson and the row; this seat proposes no S-id beyond S931-S933 and files no rows. Still open. | corpus/SOURCES.md S929 line; corpus/lessons/round-87.md Gate |
| R87-C4 (LOG binding names a counter selftest the LOG does not contain) | OPEN, fleet-level. LOG.md still contains zero occurrences of "measure87" or "counter-selftest" (measured `grep -c` = 0). The binding belongs to the round-88 LOG entry, which this seat does not write. | grep -c over /home/vgpnk/Projects/shokunin/LOG.md → 0 |
| R87-C5 (census receipts carry a hand-written revision) | ADDRESSED for the round-88 receipts. reports/round-88/census-start.json has keys scope/command/rc/stdout/stderr and NO revision key; its scope string says "worktree census before source integration", so the receipt no longer claims a revision it cannot derive. The frozen round-87 receipts keep their hand-written field, unchanged. | reports/round-88/census-start.json (no revision key) |
| R87-C6 ("attack3/10" rests on an unrecorded counting rule) | ADDRESSED for round 88 by not repeating the form. The round-88 wave registry (.ufo/waves/round-88/w1/swarm-registry.json) names all twelve members with their roles, so any count is re-derivable from a named list. The round-87 wave-summary.json is history and is not rewritten. | .ufo/waves/round-88/w1/swarm-registry.json members list |
| R87-C7 (SHONEN.md box 2's pointer swap and legend deletion undisclosed) | OPEN, unchanged, and not this seat's surface. kotodama-shokunin/SHONEN.md still names the round-87 artifacts in box 2 and still says the filename/label forgeries survive and the malformed-output debt remains. Nothing in this round's measured bytes removes that statement, so it stays as written; a round-88 SHONEN update is L1's to make or decline. | kotodama-shokunin/SHONEN.md box 2 |
| R87-C8 (report precision: "both lane commits" while four are cited; rows conflated with physical lines; SHONEN bullets spanning two lines) | ADDRESSED IN FORM for this seat's own outputs: every receipt here names the exact revision, file and byte count it measured, and no bullet spans lines for this seat's artifacts. This does not retro-fix the round-87 report text, which is history. | this stage's receipts, each carrying revision + path + rc |
| R87-C9 (untracked .ufo/waves/round-79/w1-results.json in the lane) | OPEN, unchanged. git status at 4b76524c still lists it as untracked, alongside this round's own untracked .ufo/waves/round-88/ tree. It is orchestrator scratch from a stale round-79 dispatch, not lane work; L1 decides attribute-and-commit or remove. This seat neither committed nor removed it. | git status --porcelain at 4b76524c |
| R86-C1 (numeric 0–10 mapping and the lowest-axis debt) | CARRIED UNCHANGED. No numeric 0–10 score is asserted anywhere in this round. Freshness remains the historically lowest axis, paused by the open round-11 L0 question; no waiver is invented. The frozen claims' lowest_axis field says the same. | reports/round-88/claims.json lowest_axis |
| R86-C2 (empty decision-cell and duplicate-source-ID counter debts) | NOT REPAIRED BY ROUND 88. The round-88 counter grades finding sets on a packet; it adds no decision-cell leg and no duplicate-source-ID leg. R85-C2 remains partial. | reports/round-88/measure88.py (no decision-cell or source-id leg) |
| R86-C3 (prefreeze ordering) | SATISFIED FOR ROUND 88 BY COMMIT ORDER, and this round re-used the round-87 controls rather than freezing new ones. 0c8c7330 (controls, cases, pre-dispatch receipts) is an ancestor of 4b76524c (claims + counter): `git merge-base --is-ancestor 0c8c7330 4b76524c` exits 0. The base 49562822 is an ancestor of the controls commit (exit 0), so the controls land after the base they are measured against and before the freeze. As in round 87, "before declaration" means commit order, not execution time; no receipt here carries a wall clock. | git merge-base --is-ancestor, both directions |
| R86-C4 (canonical L2 planner conflict with the validator prohibition) | DISCLOSED, NOT RESOLVED. L1 holds the planner seat for this round; the formal planner-policy conflict is retained, not waived, and this seat claims no exception to it. | round-88 dispatch instructions |
| R86-C5 (cited-record red on unchanged non-author r84 scratch references) | OPEN, unchanged. The lane does not rewrite verifier-authored history; this seat wrote nothing under .ufo/waves/round-84 and ran tools/check-cited-records.py not at all. | no lane edit made |
| R86-C6 (S925/S926 same-page Wayback coverage unresolved after 429/403) | OPEN for S925/S926, unchanged — and this round's own rows are the contrast case: S931's nearest capture (20260223185515) is an Anubis bot-check page, so the anchor was taken from the 2025-10-23 same-page capture instead, which carries the quoted sentences; S932/S933 have byte-identical same-page captures. The new rows therefore name a capture that carries the quote, and the older unresolved pair is not retro-fixed. | receipts/terrain-wayback-20251023013631.html; the 20260223185515 capture body is the Anubis interstitial |

================================================================================
## Limits of this draft
================================================================================

- No canon, no historical certification, no quality score, no lowest-axis
  number.
- The three rows and the section are drafts for L1. Nothing here is landed.
- The O claim is not met at the freeze revision and this draft does not
  assert that it is met at any revision; the missing comparator
  tools/check-finding-sets.py is the lands-side deliverable of another seat.
- The three new rows are opened but not independently re-opened by a non-author;
  criterion 10's spot-check remains owed.
- Chrisomalis 2004 and 2010, Ifrah 1987 and Dehaene 1997 were not opened
  (Cambridge Core answered HTTP 429 for both DOI targets on 2026-11-04), so no
  row or sentence in this draft depends on their text beyond naming the
  position S931 itself names and rejects.
- No tools were installed or upgraded. No production file, fleet-root tracked
  file or sibling stage was written. No git or jj mutation was made.
