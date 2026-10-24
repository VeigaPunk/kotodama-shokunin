# ScribeGateRecords — round 65 (gate / records skeleton)

Seat: `kotodama-r65.ScribeGateRecords`. Date: 2026-10-24. Lane base
`17c32302c6845c8f164b985a8cb312d3181c8788`. Read-only over the lane; two files written,
both under `.ufo/waves/round-65/`.

## Behavior — what landed

`.ufo/waves/round-65/stage/gate-spec.md` (13,459 bytes) is the paste-ready skeleton for
`corpus/lessons/round-65.md`, modelled on `corpus/lessons/round-64.md` `## Gate`/`## Mistakes`:

- `## Gate`: **26 lines, one per id S750–S775** in the model's four-field shape
  `- S7NN | <URL> | 2026-10-24 | <quote>`. Both variable fields are explicit `PENDING`
  tokens naming the fragment that must supply them (`rows/ScoutRowNN/row-S7NN.txt`),
  because at write time **no such fragment exists**. No URL and no quotation is
  asserted, guessed, or copied from the plan documents.
- Fill contract G1–G5 (inside the Gate section, column-0 prose) binding the filler to:
  live URL **plus** its same-page capture copied from the fragment's source cell; the
  **first** quoted span of that cell as the quote (the rule `accept-c.py:anchor_quote`
  applies, so R64-M4's cell-shape defect recurs here); access date literal
  `2026-10-24`; the round-64 D2 `NOT LOCATED —` form for a row whose own `VERIFY`
  records the failure, with QUALITY criterion 12's re-test output; exactly one line per
  id.
- `### Fill ledger`: 26-row table `id | row seat | planned topic`, derived from
  `.ufo/waves/round-65/spec-v2.json` (`ScoutRow01..13` prompts) — labelled in the file
  as **plan provenance**, not evidence.
- `### Assembly and check`: the frozen `QUOTES` leg command, the 26-line / 26-unique-id
  cross-check, and the statement that the skeleton's green is a shape result only.
- `## Mistakes`: **one row, R65-M1, class `receipt-attribution`** — the R1 class from
  `corpus/lessons/round-64-verifier-spotcheck.md` §6 item 1: evidence
  `reports/round-64/telemetry/final-measures-ca.txt` (measured revision `95c9194e…`,
  own legs false there; records landed 17 min later in `8bab271c`); captured by **none**
  (no tree-hash-of-inputs rule existed, so no leg could catch it); fix = receipts pin
  the measured revision **and** a `git rev-parse <rev>^{tree}` hash of read inputs,
  applied as leg `R1` of `reports/round-65/accept-ca.py` and generalised as **QUALITY
  criterion 17** (which does **not** exist at the base — see F2). A closing note pins
  `ScribeLessonR65`'s `R65-M1` placeholder to this same row (F3).

## Commands and outputs (all run from the lane root)

```
python3 -B tools/check-gate-quotes.py .ufo/waves/round-65/stage/gate-spec.md
  -> GATE_QUOTES: 0 findings            exit=0
grep -c '^- S7[5-7][0-9] ' .ufo/waves/round-65/stage/gate-spec.md   -> 26
grep -o '^- S7[0-9][0-9]' … | sort -u | wc -l                      -> 26
```

Negative controls (temp copies under `mktemp -d /tmp/gatectl.*`, deleted after the run;
no lane bytes touched) — the instrument is **not** vacuously green on this row shape:

```
:43 S750 words=30            GATE_QUOTES: 1 findings   exit=1   (30-word quote)
:44 S751 words=8             GATE_QUOTES: 1 findings   exit=1   (ellipsis-joined span)
```

Dependency check at the same moment:

```
ls .ufo/waves/round-65/rows/   -> total 0 (empty; dir mtime 01:08)
ls .ufo/waves/round-65/w1/     -> CriticNoHarm, ExecGateFill, ScoutBlindBase,
                                  ScoutFragRunner, ScoutReopenA/B/C, SentinelScope
```

Inputs read (read-only): `reports/round-65/claims.json`; `accept-c.py` (leg `ROWS`
190–257, `anchor_quote` 107–109, `norm_words` 92–94); `accept-ca.py` (leg `R1` 104–120,
`CRITERION` 167–170, `QUOTES` 175–180); `tools/check-gate-quotes.py` (`ROW` regex,
`gate_rows` continuation join, `scan_line`, `MAX_WORDS = 25`,
`doubled_locator`, `truncated_grounds`); `corpus/lessons/round-64.md` Gate/Mistakes;
`round-64-verifier-spotcheck.md` §2 `### Claim Ca` H1 and §6 item 1;
`reports/round-64/telemetry/final-measures-ca.txt` lines 1–6; `corpus/QUALITY.md`
(53 lines, criteria 1–16); `spec-v2.json` row-seat prompts.

## Gates — frozen predicate status

| leg | owner | status from this seat |
| --- | --- | --- |
| `ACCEPT-C-65` `ROWS` | rows + registry append | **not reachable**: 0 of 26 fragments exist; the leg reads `corpus/SOURCES.md`, so a Gate line cannot stand in for a row |
| `ACCEPT-CA-65` `QUOTES` | lesson Gate | **shape-clean, not satisfied**: the leg runs on `corpus/lessons/round-65.md`, which does not exist; my draft prints `0 findings` only because it carries no quoted span |
| `ACCEPT-CA-65` `CRITERION` | `corpus/QUALITY.md` | **cannot pass yet**: base file ends at criterion 16, leg needs a `17.` entry containing `tree hash` |
| `ACCEPT-CA-65` `R1` | receipts + repeats | outside this seat; recorded for the record |

## Touched surfaces

- `.ufo/waves/round-65/stage/gate-spec.md` (new, this seat).
- `.ufo/waves/round-65/w1/ScribeGateRecords.md` (this report).
- Nothing else. No `corpus/`, `reports/`, `tools/` byte touched; no git/jj write; no
  commit; no tool install (so no install ledger entry).

## Findings

- **F1 (dependency, blocking the Gate body).** All 26 lines are `PENDING`: `rows/` is
  empty and `corpus/SOURCES.md` still has no S750–S775 rows
  (`grep -c 'S75[0-9]\|S76[0-9]\|S77[0-5]' corpus/SOURCES.md` → `0`, exit 1). `w1/ExecGateFill.md` records the same absence, plus
  that `stage/` did not exist when it ran; `stage/gate-spec.md` now supplies the fill
  contract it lacked, so a second fill pass can start from G1–G5 rather than improvise.
- **F2 (records defect, needs an owner).** The assigned R1 fix names "QUALITY criterion
  17", but `corpus/QUALITY.md` at base has **16** numbered criteria (file ends at
  criterion 16, 53 lines). The frozen leg agrees the gap is real: `CRITERION` requires
  `^1[7-9]\.` **and** the text `tree hash`. So R1's disposition cannot close by editing
  receipts and repeats alone; a new criterion must be authored this round, and its text
  must generalise the rule beyond Ca (any receipt's read inputs).
- **F3 (id collision).** `ScribeLessonR65` was tasked to emit an `R65-M1` placeholder.
  If both drafts are pasted, the lesson carries two distinct R65-M1 rows. My row is the
  one the assignment fixes (class receipt-attribution); the skeleton says so explicitly
  and numbers further mistakes from R65-M2. L1 should delete the placeholder, not the
  row.
- **F4 (instrument scope, `QUOTES`).** For round-65 row shape, `check-gate-quotes.py`
  covers `over-cap`, `ellipsis-joined`, `html-entity` and — only if the filler adopts an
  ` — accessed <date> — ` locator — `doubled-locator`. `truncated-grounds` is inert: it
  needs a `Grounds:` field and the same-id `teaches` cell in the lesson-adjacent
  `SOURCES.md`, and round-65 Gate rows carry neither. The leg therefore does not verify
  that a Gate quote is byte-equal to its row's anchor quote; nothing in the frozen set
  does. That equality rests on the fill contract and on review, and should be named as
  review-only wherever the round claims the Gate is checked.
- **F5 (fill hazard).** `gate_rows` joins indented continuations to the preceding row
  before counting words. A note indented under a Gate row is charged to that row's
  quote cap. My notes sit at column 0 for this reason; the filler must not indent prose
  beneath a `- S7NN` line, and must not wrap a quote across an indented line.
- **F6 (quote-anchor recurrence).** `anchor_quote` takes the **first** quoted span of
  the source cell, straight or curly. Any row whose anchor cell opens with a curly
  section locator reproduces R64-M4 (`quote_words=5`, `in_order=0`). G2 puts the body
  sentence first and leaves locators unquoted.
- **F7 (Gate cannot rescue a row).** `ROWS` enforces tier `A|B`, `status=mined`,
  `opened=2026-10-24`, `recheck=180d`, `usedby` containing the entry, 8–25 quote words,
  exactly one registry row per id, unique NFKC-normalised live URL, and a capture whose
  original normalises equal to the live URL; it also rejects any new row outside
  S750–S775. A correct Gate line over a defective row is still a failing claim.
- **F8 (NOT LOCATED is not a resting state this round).** Round 64 could carry three
  NOT LOCATED lines because claim C counted 26 mined rows out of 32 ids. Round 65's
  claim is "exactly 26 mined rows S750–S775", so a D2 line means a re-open under the
  same id before closure; the id is never dropped or renumbered.
- **F9 (uncertainty, stated as such — `[INFERENCE]`).** Whether the 13 mining seats can
  locate tier-A/B sources for all 26 planned topics within the wave is unverified here;
  several planned topics (S756 Blanchard-style survey, S769 Opie, S770 Gomme) are books
  whose quotable body text may sit only in archive scans. Not tested, not claimed.

## Out of scope (not attempted, by assignment)

Filling URLs or quotes; creating `corpus/lessons/round-65.md`; appending registry rows;
editing `corpus/QUALITY.md`; running any lane counter; any commit or index write.

Report: .ufo/waves/round-65/w1/ScribeGateRecords.md
