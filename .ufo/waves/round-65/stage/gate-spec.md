# Gate / `## Mistakes` skeleton — `corpus/lessons/round-65.md`

Seat: `kotodama-r65.ScribeGateRecords` (scribe, round 65 v2 wave, 2026-10-24).
Lane base: `17c32302c6845c8f164b985a8cb312d3181c8788`. This file is a **draft under
`.ufo/waves/round-65/`**; the L1 reviews it, integrates it and is the only committer.
Everything above the `## Gate` heading is seat meta and is **not** part of the lesson:
copy from `## Gate` down.

What this file is, and what it is not (role boundary):

- It is the **shape** of the two lesson sections, anchored to the frozen counter and
  the round-64 model. It is not evidence that any row exists.
- No URL and no quote below is asserted. Both are `PENDING` tokens keyed to the row
  fragment that must supply them. At the time of writing,
  `.ufo/waves/round-65/rows/` holds **no** `row-<SID>.txt` for S750–S775 (the 13
  `ScoutRow01..13` mining seats were dispatched in this wave and had not landed), so
  filling any line from this seat would be fabrication. `ExecGateFill`
  (`.ufo/waves/round-65/stage/lesson-gate.md`, quote byte-equal to each fragment) and
  the L1 are the seats that copy real bytes in.
- The frozen `QUOTES` leg of `reports/round-65/accept-ca.py` runs
  `tools/check-gate-quotes.py corpus/lessons/round-65.md` and requires exit 0 with
  `0 finding`. This skeleton is checker-clean **because it carries no quoted span at
  all** — that is a format result, never a support result. A green run over a filled
  Gate is what the leg is for.

Inputs read for this draft (read-only): `reports/round-65/claims.json`; the three
frozen counters `reports/round-65/accept-c.py`, `accept-ca.py`, `accept-o.py`;
`.ufo/waves/round-65/spec-v2.json` (the plan: per-id topics and the 13 row seats);
`corpus/lessons/round-64.md` `## Gate`/`## Mistakes` (the model);
`corpus/lessons/round-64-verifier-spotcheck.md` §2 (`### Claim Ca`, H1), §6 item 1;
`corpus/QUALITY.md` (16 criteria at the base — criterion 17 does not exist yet);
`reports/round-64/telemetry/final-measures-ca.txt` lines 1–6; `tools/check-gate-quotes.py`.

## Gate

Rows opened this round (S750–S775, one line per id, the id set frozen by
`reports/round-65/claims.json` claim C). Each line's URL, capture and quote are copied
from that id's own `row-<SID>.txt` fragment — the source cell the L1 appends to
`corpus/SOURCES.md` — and are **not** restated from any plan document. Lines still
carrying `PENDING` are unfilled, and an unfilled Gate is an incomplete Gate, reported
as such.

- S750 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow01/row-S750.txt | 2026-10-24 | QUOTE-PENDING row-S750.txt, 8-25 words
- S751 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow01/row-S751.txt | 2026-10-24 | QUOTE-PENDING row-S751.txt, 8-25 words
- S752 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow02/row-S752.txt | 2026-10-24 | QUOTE-PENDING row-S752.txt, 8-25 words
- S753 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow02/row-S753.txt | 2026-10-24 | QUOTE-PENDING row-S753.txt, 8-25 words
- S754 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow03/row-S754.txt | 2026-10-24 | QUOTE-PENDING row-S754.txt, 8-25 words
- S755 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow03/row-S755.txt | 2026-10-24 | QUOTE-PENDING row-S755.txt, 8-25 words
- S756 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow04/row-S756.txt | 2026-10-24 | QUOTE-PENDING row-S756.txt, 8-25 words
- S757 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow04/row-S757.txt | 2026-10-24 | QUOTE-PENDING row-S757.txt, 8-25 words
- S758 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow05/row-S758.txt | 2026-10-24 | QUOTE-PENDING row-S758.txt, 8-25 words
- S759 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow05/row-S759.txt | 2026-10-24 | QUOTE-PENDING row-S759.txt, 8-25 words
- S760 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow06/row-S760.txt | 2026-10-24 | QUOTE-PENDING row-S760.txt, 8-25 words
- S761 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow06/row-S761.txt | 2026-10-24 | QUOTE-PENDING row-S761.txt, 8-25 words
- S762 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow07/row-S762.txt | 2026-10-24 | QUOTE-PENDING row-S762.txt, 8-25 words
- S763 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow07/row-S763.txt | 2026-10-24 | QUOTE-PENDING row-S763.txt, 8-25 words
- S764 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow08/row-S764.txt | 2026-10-24 | QUOTE-PENDING row-S764.txt, 8-25 words
- S765 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow08/row-S765.txt | 2026-10-24 | QUOTE-PENDING row-S765.txt, 8-25 words
- S766 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow09/row-S766.txt | 2026-10-24 | QUOTE-PENDING row-S766.txt, 8-25 words
- S767 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow09/row-S767.txt | 2026-10-24 | QUOTE-PENDING row-S767.txt, 8-25 words
- S768 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow10/row-S768.txt | 2026-10-24 | QUOTE-PENDING row-S768.txt, 8-25 words
- S769 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow10/row-S769.txt | 2026-10-24 | QUOTE-PENDING row-S769.txt, 8-25 words
- S770 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow11/row-S770.txt | 2026-10-24 | QUOTE-PENDING row-S770.txt, 8-25 words
- S771 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow11/row-S771.txt | 2026-10-24 | QUOTE-PENDING row-S771.txt, 8-25 words
- S772 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow12/row-S772.txt | 2026-10-24 | QUOTE-PENDING row-S772.txt, 8-25 words
- S773 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow12/row-S773.txt | 2026-10-24 | QUOTE-PENDING row-S773.txt, 8-25 words
- S774 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow13/row-S774.txt | 2026-10-24 | QUOTE-PENDING row-S774.txt, 8-25 words
- S775 | URL-PENDING .ufo/waves/round-65/rows/ScoutRow13/row-S775.txt | 2026-10-24 | QUOTE-PENDING row-S775.txt, 8-25 words

Note: fill contract for every line above (a filler that cannot satisfy all five rules
leaves the line `PENDING` and reports it — it does not approximate):
G1. URL field = the live URL exactly as it stands in the fragment's `ROW=` source cell,
  followed by that cell's same-page capture in parentheses, the round-64 shape
  (live URL, then capture in parentheses). This is the text the L1 appends to
  `corpus/SOURCES.md`, so the Gate and the registry stay byte-equal on both URLs.
G2. Quote field = the **first** quoted span of the same source cell, in straight double
  quotes, byte-equal to the fragment; 8–25 words under the `ROWS` leg's normaliser
  (`accept-c.py`: NFKC, casefold, non-word -> space). The first quoted span is the
  anchor — put the body sentence first and leave any section locator unquoted
  (round-64 mistake R64-M4, same counter rule).
G3. Access date = literal `2026-10-24` on every line; the `ROWS` leg rejects any row
  whose `opened` cell is a different date, so a line dated otherwise cannot be right.
G4. A row whose own `VERIFY`/`TEST2` records the failure keeps its Gate line in the D2
  form the round-64 Gate used: the words `NOT LOCATED —` plus the tested wording
  labelled as a candidate, never as a located quotation. Because claim C counts
  exactly 26 mined rows, such a line is a defect to re-open under the same id
  (QUALITY criterion 12: the re-test tool and its verbatim output go on the line) —
  not an acceptable resting state, and the id is never dropped or renumbered.
G5. One line per id, and one registry row per id: `ROWS` fails on
  `rows != 1`, so a duplicate id is a Gate defect even when both lines look right.

### Fill ledger (plan provenance — ids, seats, planned topics)

Sources: `.ufo/waves/round-65/spec-v2.json` (`ScoutRow01`..`ScoutRow13` prompts) and
`reports/round-65/claims.json`. The topics are the **plan's** assignment; a row that
lands on a different but in-scope source rewrites its own line, not this table.

| id | row seat | planned topic (from the wave plan) |
| --- | --- | --- |
| S750 | ScoutRow01 | Culin 1907 Games of the North American Indians — classification and ethnographic scope |
| S751 | ScoutRow01 | the Royal Game of Ur — race game, royal cemetery context, rules reconstruction |
| S752 | ScoutRow02 | senet — Egyptian funerary board game, tomb context |
| S753 | ScoutRow02 | the mancala family — Africa/Asia distribution, sowing gameplay |
| S754 | ScoutRow03 | tug of war and team contests as intangible heritage (UNESCO nomination) |
| S755 | ScoutRow03 | astragaloi / knucklebones in Greek and Roman gaming |
| S756 | ScoutRow04 | anthropology of sport — sport as cultural institution |
| S757 | ScoutRow04 | Huizinga, Homo Ludens — play as constitutive of culture |
| S758 | ScoutRow05 | Caillois, Man, Play and Games — paidia/ludus, six categories |
| S759 | ScoutRow05 | Sutton-Smith, The Ambiguity of Play — rhetorics of play |
| S760 | ScoutRow06 | ancient Olympic Games — festival context, rules |
| S761 | ScoutRow06 | Mesoamerican ballgame — courts, equipment, political/ritual role |
| S762 | ScoutRow07 | rubber and the solid ball in Mesoamerican play — material evidence |
| S763 | ScoutRow07 | tafl / hnefatafl — Norse board game family, rules reconstruction |
| S764 | ScoutRow08 | go / weiqi origins and early transmission |
| S765 | ScoutRow08 | chaturanga and Silk Road transmission of chess |
| S766 | ScoutRow09 | history of playing cards — museum collection scholarship |
| S767 | ScoutRow09 | archaeology of dice — earliest dice, gaming in early states |
| S768 | ScoutRow10 | teetotum / dreidel spinning-top gambling toys |
| S769 | ScoutRow10 | Opie, Lore and Language of Schoolchildren — playground games |
| S770 | ScoutRow11 | Alice Gomme, Traditional Games — singing and ring games |
| S771 | ScoutRow11 | lacrosse and First Nations stick games |
| S772 | ScoutRow12 | sumo as ritual sport |
| S773 | ScoutRow12 | patolli — Mesoamerican race/betting game |
| S774 | ScoutRow13 | kubb, skittles / ninepins — northern-European throwing-target family |
| S775 | ScoutRow13 | board games across the ancient world — survey |

### Assembly and check

- After fill, the section is checked by the frozen leg:
  `python3 -B tools/check-gate-quotes.py corpus/lessons/round-65.md` must exit 0 with
  `0 finding` (the `QUOTES` leg of `reports/round-65/accept-ca.py`). The same tool over
  this skeleton, which asserts no quotation, prints `0 finding` and proves only that
  the row shape is readable.
- `truncated-grounds` cannot fire for round 65: it compares a row's `Grounds:` text
  with the `teaches` cell of the `SOURCES.md` beside the lesson, and round-65 rows
  carry no `Grounds:` field. The plain `- S### | URL | date | quote` shape therefore
  never enters that class; `over-cap`, `ellipsis-joined`, `doubled-locator` and
  `html-entity` all do, and the fill contract above is written to keep them at zero.
- Counting cross-check for the filler: 26 lines, ids S750..S775 with no gap and no
  repeat — `grep -c '^- S7[5-7][0-9] ' corpus/lessons/round-65.md` must print 26 and
  `grep -o '^- S7[0-9][0-9]' | sort -u | wc -l` must print 26.

## Mistakes

One row this round, the R1 class the round-64 verifier spot-check routed
(`corpus/lessons/round-64-verifier-spotcheck.md` §6 item 1). It is filed as the
round-65 lesson's first mistake id; the closed-form ids after it belong to the L1.

- R65-M1 (class: receipt-attribution). The round-64 Ca receipt
  `reports/round-64/telemetry/final-measures-ca.txt` stamped
  `measured revision: 95c9194ef938e1338b2af894086a46e8b8677ee2` (line 2) while its own
  legs fail at that revision: the spot-check's H1 records
  `git show 95c9194e:LOG.md | grep -c '## Round 64'` -> 0 and the same for the
  `SCORECARD.md` round-63 corrections, the records having landed 17 minutes later in
  `8bab271c` (00:28:55 run vs 00:45:02 commit). The run was taken over a worktree with
  uncommitted records, and the receipt names the counter's own sha256 but nothing about
  the bytes the counter **read**, so its verdict could not be attributed to any
  revision — an independent replay reproduces its detail strings at `8bab271c`. This
  is a records defect, not a measurement defect: the seven legs were true of the tree
  that was read, and false of the revision the receipt named. Evidence:
  `reports/round-64/telemetry/final-measures-ca.txt` lines 1–6 (`measured revision`,
  `counter sha256`, `command`, `date`), and
  `corpus/lessons/round-64-verifier-spotcheck.md` §2 (`### Claim Ca`, H1) with §6 item
  1 (R1, HIGH, records-only). Captured by: **none** — the protocol had no
  tree-hash-of-inputs rule, so no leg compared a receipt's declared inputs against the
  tree it read; the mismatch surfaced post-hoc in the spot-check, and the round-64
  counters could not have caught it. Fix: every receipt pins the measured revision
  **and** a git tree hash of its read inputs (`git rev-parse <rev>^{tree}`), and the
  counting leg rejects a receipt whose tree hash is missing or whose run was taken over
  a dirty worktree that it does not declare — first applied as leg `R1` of
  `reports/round-65/accept-ca.py`. Generalised as **QUALITY criterion 17**, added to
  `corpus/QUALITY.md` this round: at the base that file ends at criterion 16, and leg
  `CRITERION` of `reports/round-65/accept-ca.py` requires a new `17.` entry whose text
  carries `tree hash`, so the criterion and the leg cannot drift apart.

Note: R65-M1 above is the row `ScribeLessonR65`'s skeleton leaves as an `R65-M1`
placeholder. Emit **one** R65-M1 — this row, unchanged — and number any further
round-65 mistakes from R65-M2.
