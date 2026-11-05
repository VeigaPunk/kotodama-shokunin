# ExecMirrorGate — staged mirror pre-check, round 90 (claim C)

## Mirror provenance

```
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin archive --format=tar \
    d0b6f2a7f9cc36272682749a9b047b739406f0c8 | tar -x -C <scratch>/mirror
```

Observed at d0b6f2a7: `corpus/knowledge` = 261 `.md` files, `corpus/knowledge/linguistics`
= 34 files, `corpus/SOURCES.md` = 865 registry rows, no `corpus/lessons/round-90.md`,
no `reports/round-90/evidence/`. That matches claims.json C.before (865 rows, 34
linguistics files, entry absent). Base registry copied separately:

```
git show 6b0b86e45ae902331aca75863db380f2991458c4:corpus/SOURCES.md   # 865 rows, 1039150 B
```

Tool identities at the lane (identical at d0b6f2a7 and at c0c628d8):

| tool | sha256 (first 24) |
|---|---|
| tools/check-advance-evidence.py | 121888f08a81ad87675863cf (equals claims.json O.tool_sha256) |
| tools/check-corpus-index.py | 8d57afd0801e9ea78b6f95ab |
| tools/check-row-fragments.py | 9fe025fea321abf5718cb137 |

Python 3.14.8. No tool installed or upgraded this seat; no pacman transaction attempted.

## Packet state: ScribeEntry's landing is ABSENT

At the time of every leg below, `.ufo/waves/round-90/w1/stage/ScribeEntry/` held one
empty directory `evidence/` and **0 files** (`find … -type f | wc -l` → `0`). There is
no `entry.md`, `rows.md`, `gates.md`, no capture and no manifest to overlay. Nothing
was fabricated to stand in for it.

## What was exercised on REAL bytes (the d0b6f2a7 mirror)

- `check-corpus-index.py --root <mirror>` → `CORPUS-INDEX: OK files=261 rows=261 findings=0`, rc 0.
- `sources-census.sh validate --file <mirror>/corpus/SOURCES.md` → rc 0, final line
  `file ok …/mirror/corpus/SOURCES.md` (W04 duplicate-url warnings only).
- `check-row-fragments.py` (lane default rows dir) → `FRAG: 0 finding(s) in 26 file(s)`, rc 0.
- `check-advance-evidence.py entry …` → rc 2, `ADVANCE-EVIDENCE_ERROR: unreadable
  …/corpus/knowledge/linguistics/petitionary-and-votive-formulae.md: No such file or directory`.

## What is FIXTURE-ONLY, and exactly which legs were not exercised on real bytes

The six entry-mode legs **ENTRY, SHAPE, TOPIC, NEWIDS, GATE, CAPTURE** were not exercised
on real landing bytes. On real bytes ENTRY was exercised only as the rc-2 refusal above.
APPENDONLY was not exercised against a real lands commit (measure90.py reads git
revisions; no lands revision exists).

Instead the legs ran against the grader's own `--selftest` positive-entry fixture
(`SELFTEST PASS 67/67`, case `positive entry: rc=0`), relocated to the claim's entry path
with its citations re-pointed from S010–S012 to synthetic rows S942–S944 and the rows'
`used-by` re-pointed to the C entry. Two fixture states were used:

1. `fixture-mirror` — the fixture's own 5-row registry and lesson. Fixture thresholds
   (`--min-bytes 1200 --min-headings 4 --min-topic-overlap 8`) → `ENTRY-EVIDENCE: PASS legs=6/6`,
   rc 0. This proves the CLI path and the mirror layout, nothing about the claim's text.
2. `scale2` — a full copy of the mirror with three synthetic rows S942–S944 inserted
   **inside** `## Registry` after S941, a lesson with three gate lines, three captures and a
   manifest, plus the four README moves. Run at the claim's real thresholds against the real
   865-row base registry → `ENTRY-EVIDENCE: FAIL legs=4/6 failed=ENTRY,TOPIC`
   (`1377 bytes < 12000`; `entry shares 7 content words with the declared topic < 10`).
   Those two failures are properties of the 1377-byte fixture text, not of the landing
   shape: SHAPE, NEWIDS, GATE and CAPTURE pass at real registry scale with 868 rows.

The synthetic S942–S944 rows and captures are labelled fixture text inside the captures
("Fixture text, not a fetched page") and are **not evidence** for claim C.

## Facts L1 needs that the fixture run established

- Registry rows appended at end-of-file (after `## Paths`) are refused:
  `file E12 S942 row outside Registry section`, census rc 1. Rows must be inserted inside
  the `## Registry` table (lines 26–897 at base; S941 is the last row at line 897).
- Adding the entry file without the README moves yields exactly five findings:
  `CORPUS-INDEX: FINDINGS files=262 rows=261 findings=5 ids=FOOTER_DIR_TOTALS,FOOTER_TOTAL,HEADER_DRIFT,MISSING_ROW,TOTALS_DRIFT`, rc 1. With the row (topic verbatim from
  the entry's `- topic:` line), `## linguistics/ (34)→(35)`, `Total knowledge entries: 261→262`
  and `(total 261 files; directory totals 34/36/43/29/24/95)→(total 262 files; directory totals 35/36/43/29/24/95)`
  it becomes `CORPUS-INDEX: OK files=262 rows=262 findings=0`, rc 0.
- `check-row-fragments.py` does **not** read `corpus/SOURCES.md`. It walks `--rows DIR` and
  scans only files named `row-*.txt` containing `ROW:` labelled lines, and it is hard-wired
  to `ENTRY = corpus/knowledge/culture-material/games-play-sport-contests.md` and
  `EXPECTED_OPENED = 2026-10-24`. Pointed at the round-90 stage dir it prints
  `FRAG: 0 finding(s) in 0 file(s)` — a vacuous pass, not a check of this round's rows.
- Entry mode's GATE does not compare the quote against the row's `teaches` cell and does not
  call `surface_error`, so a gate quote that merely echoes `teaches` passes GATE, and a
  Wayback surface whose stamp predates the round is not refused by entry mode (it fails GATE
  only if the gate line omits the row's archive URL). Those two round-89 classes are refused
  in **advance** mode only; the independent re-fetch seats are the defence for C.
- SHAPE flags a sentence only when it repeats **more than twice** (`worst > 2`); two
  occurrences pass.

## Scoping

Mirror and probes lived only in `/fast/scratch/hyaku/kotodama-r90/ExecMirrorGate/`
(removed before yield). Nothing under `corpus/`, `tools/`, `reports/`, `SCORECARD.md`,
`LOG.md`, `SKILL.md` or `PROVINCE.md` was written; no git/jj mutation anywhere.
