# ExecMirrorGate — staged-mirror pre-check of claim C (round 90)

Seat: leaf executor, lane kotodama-shokunin. Stage:
`.ufo/waves/round-90/w1/stage/ExecMirrorGate/` (`notes.md`, `legs.md`, `legs-run.log`,
`receipts/`; the real-bytes run refused at rc 2 before the tool could write a receipt, so
no `entry-receipt.txt` exists and the refusal text is in `legs-run.log`).

## What was built

A staged mirror of the lane at `d0b6f2a7f9cc36272682749a9b047b739406f0c8`
(`git archive --format=tar … | tar -x`), plus the base registry from
`6b0b86e45ae902331aca75863db380f2991458c4:corpus/SOURCES.md` (865 rows, 1039150 B).
Mirror facts at d0b6f2a7: 261 knowledge files, 34 linguistics files, 865 registry rows,
no `corpus/lessons/round-90.md`, no `reports/round-90/evidence/` — equal to
claims.json C.before. Tools at d0b6f2a7 and at c0c628d8 are byte-identical;
`tools/check-advance-evidence.py` sha256 `121888f08a81ad87…` equals claims.json
O.tool_sha256.

## Blocker for the real overlay

`<stage>/ScribeEntry/` contains one empty `evidence/` directory and **0 files** at every
check during this seat. There was no `entry.md`, `rows.md`, `gates.md`, capture or
manifest to overlay, so the mirror pre-check is **fixture-only** (declared as such in
`notes.md`). Nothing was fabricated to impersonate the packet.

## Legs

Real bytes (mirror at d0b6f2a7):

- `check-advance-evidence.py entry …` → rc 2,
  `ADVANCE-EVIDENCE_ERROR: unreadable <mirror>/corpus/knowledge/linguistics/petitionary-and-votive-formulae.md: No such file or directory`.
- `check-corpus-index.py --root <mirror>` → `CORPUS-INDEX: OK files=261 rows=261 findings=0`, rc 0.
- `sources-census.sh validate --file <mirror>/corpus/SOURCES.md` → rc 0, `file ok …/corpus/SOURCES.md` (W04 warnings only).
- `check-row-fragments.py` → `FRAG: 0 finding(s) in 26 file(s)`, rc 0 — but this tool never
  reads `SOURCES.md`: it walks `--rows DIR` for `row-*.txt` with `ROW:` labels and is pinned to
  round-65 (`ENTRY = …games-play-sport-contests.md`, `EXPECTED_OPENED = 2026-10-24`). Over the
  round-90 stage dir it prints `FRAG: 0 finding(s) in 0 file(s)`, a vacuous pass.

Fixture-only (grader's own `--selftest` positive-entry fixture, relocated to the C path,
citations re-pointed to synthetic S942–S944, `used-by` re-pointed to the entry):

- At the fixture's own thresholds: `ENTRY-EVIDENCE: PASS legs=6/6`, rc 0.
- Full rehearsal at real registry scale (868 rows, three synthetic rows inside `## Registry`,
  lesson gates, captures, manifest, README moves) with the claim's exact thresholds:
  `ENTRY-EVIDENCE: FAIL legs=4/6 failed=ENTRY,TOPIC` — `1377 bytes < 12000` and
  `entry shares 7 content words with the declared topic < 10`. Both failures are properties of
  the 1377-byte fixture text; SHAPE, NEWIDS, GATE and CAPTURE pass at real scale.
- INDEX on the rehearsal: `CORPUS-INDEX: OK files=262 rows=262 findings=0`, rc 0.
- APPENDONLY (rehearsal, grader's own parser): `base rows 865 lands rows 868 dup [] changed [] removed [] new ['S942','S943','S944']`, all three `tier A status mined opened 2026-11-04`.
- CENSUS on the rehearsal: rc 0, no line naming S942–S944.

Controls that fired (each one line in `legs.md` with the exact text): entry added without
README moves → `findings=5 ids=FOOTER_DIR_TOTALS,FOOTER_TOTAL,HEADER_DRIFT,MISSING_ROW,TOTALS_DRIFT`;
rows appended after `## Paths` → `E12 S942 row outside Registry section`; capture set to a
graded file → `capture outside reports/round-90/evidence: corpus/lessons/round-90.md`;
quote absent from capture → `quote absent from capture`; archive-stamped row with a gate line
naming the live URL → `gate line does not name the row url`.

## Top three fixes for L1 before landing

1. Insert the new rows **inside `## Registry`** (census E12 otherwise) and leave every one of
   the 865 base rows cell-identical — the counter's APPENDONLY compares them all.
2. Move the README's four coupled numbers with the row: row text equal to the entry's
   `- topic:` line verbatim, `## linguistics/ (34)→(35)`, `Total knowledge entries: 261→262`,
   footer `(total 261 files; directory totals 34/36/43/29/24/95)` → `(total 262 files; directory totals 35/36/43/29/24/95)`.
3. Bind each gate line to the row's registry URL verbatim (archive URL if the row cites one),
   the access date 2026-11-04 and a 20-char/≤25-word quote that occurs in a capture confined
   to `reports/round-90/evidence/`, non-graded, with manifest `sha256`, 2xx `http_status` and a
   `fetched_at` local ISO instant dated 2026-11-04.

## Risks carried forward

- Entry mode has no self-quote check (`gate quote == teaches cell` passes GATE and CAPTURE)
  and never calls `surface_error`, so a Wayback stamp that predates the round is not refused
  by claim C's grader mode; those round-89 classes are refused in **advance** mode only. The
  independent re-fetch seats and the reviewer/critic are the defence for C.
- SHAPE flags repetition only above two occurrences (`worst > 2`).
- The real ENTRY/SHAPE/TOPIC/NEWIDS/GATE/CAPTURE legs and APPENDONLY remain unexercised on
  landing bytes until ScribeEntry's packet exists; APPENDONLY additionally needs a real lands
  revision (measure90.py reads git revisions).

## Scoping

Wrote only `.ufo/waves/round-90/w1/stage/ExecMirrorGate/**` and this report. No production
file, no fleet-repo file, no sibling lane, no shokuknow path, no git/jj mutation, no commit.
Scratch `/fast/scratch/hyaku/kotodama-r90/ExecMirrorGate/` deleted before yield. No tool
installed or upgraded (pacman paused; nothing needed).

Observed, not caused by this seat: `reports/round-90/base-surface.txt` gained 17 lines at
20:32:28 during the wave (`git diff --stat` → `17 +++++++++++++++++`), and
`reports/round-90/before-state.txt` is untracked; both belong to sibling seats. This seat
passed no path under `reports/` to any tool and wrote nothing outside its stage and this
report.
