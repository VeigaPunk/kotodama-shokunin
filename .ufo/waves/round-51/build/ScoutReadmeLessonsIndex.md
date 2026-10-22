# ScoutReadmeLessonsIndex — records and index mechanics (round 51, attempt 3)

Seat: `KotodamaR51a3.ScoutReadmeLessonsIndex` (leaf; no dispatch, no installs, no tool changes).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` at base `bff83ba` (worktree clean except
`?? .ufo/waves/round-51/`; `git rev-parse HEAD` = `1f97472aefdd40c150cddcfb7d5d7acff12b6a2b`).
Every line number below is the base-worktree line. Both files re-read at the base bytes:
`corpus/README.md` sha256 `3ea247db…`, 621 lines; `corpus/lessons/README.md` sha256 `62f91a93…`,
504 lines.

Method note: all rehearsals ran on throwaway mirror trees under `/tmp` (a copy of the lane's
`corpus/README.md` + symlinked `corpus/knowledge/*.md`, and a full lane mirror with a **copy** of
`corpus/lessons/`), never in the lane. Every leg was rehearsed green and then broken on purpose to
show it fails. The lane itself was never edited by a rehearsal except one disclosed accident,
reverted byte-exact (see §5).

---

## 1. `corpus/README.md` — indexing `corpus/knowledge/linguistics/sign-languages-manual-modality.md`

Six edits, all in one file. Line anchors are base lines; apply top-down.

| # | anchor (base line) | old bytes | new bytes |
|---|---|---|---|
| 1 | after line 1 (`# kotodama-shokunin corpus index`) + blank line 2, above line 3 | — | insert the revision-2.8 block, §1.1 |
| 2 | 220 | `## linguistics/ (25)` | `## linguistics/ (26)` |
| 3 | between 239 and 240 | — | insert the entry's index row, §1.2 |
| 4 | 590 | `Total knowledge entries: 226.` | `Total knowledge entries: 227.` |
| 5 | 592 | `Counts checked 2026-10-21 from the repo root:` | `Counts checked 2026-10-22 from the repo root:` |
| 6 | 594 | `(total 226 files; directory totals 25/26/28/29/24/94).` | `(total 227 files; directory totals 26/26/28/29/24/94).` |

Line 593 (the backticked command `python3 tools/source-audit-inventory.py --json --summary --root
corpus/knowledge`) is unchanged: the footer's command leg is a regex match, not an execution
(`reports/round-28/readme/sweep.py:56-61`), and the round-50 footer already carries the date
`2026-10-21` only in the date field.

### 1.1 Revision line format and placement (paste-ready)

The block goes at the top of the file, directly under the H1 and its blank line, and is separated
from `revision: 2.7` (base line 3) by exactly one blank line. Format is the house shape: a
`revision: X.Y — <title> (YYYY-MM-DD):` first line whose body continues on following lines —
never a bare label line, because `tools/check-readme-revisions.py` fails a label whose next line is
blank (`REVISION-STUB`, `tools/check-readme-revisions.py:137-147`) and requires non-increasing
numeric labels top-to-bottom (`REVISION-ORDER`, `:149-162`). 2.8 above 2.7 satisfies both.

```text
revision: 2.8 — Round-51 linguistics landing (2026-10-22): one linguistics entry
landed (`sign-languages-manual-modality.md`, sign languages and other manual
communication systems as conlang and worldbuilding method), its row added in
filename order between `semantics-pragmatics.md` and
`sociolinguistics-registers.md` with the entry's `- topic:` text byte-equal;
`## linguistics/` moved 25 → **26**, totals line 226 → **227**, footer vector
`25/26/28/29/24/94` → `26/26/28/29/24/94`. The routed rev-1.9
`REVISION-ORPHAN` residual is carried, not repaired. Re-measured with
`python3 reports/round-28/readme/sweep.py`: 227 rows vs 227 files, exit 0.
```

Re-measure paragraph convention (matches 2.7): the closing sentence names the measuring command
with the repo-root-relative path and states `227 rows vs 227 files, exit 0`. If the C entry's title
differs from the phrase above, substitute it; do not restate a number you have not measured.

### 1.2 The index row — format is derived, not authored

Row grammar: `- \`<file>.md\` — <topic>` on **one physical line**
(`ROW_RE`, `reports/round-28/readme/sweep.py:48`). The topic text must be **byte-equal** to
`sweep.topic_of()` of the entry: the entry's `- topic:` head-block field with its continuation
lines stripped and space-joined (`:64-72`). A changed word, a trailing space or a doubled inner
space each produce `topic_mismatch` and exit 1 (rehearsed, §1.4 N1–N3).

Insertion point: filename order inside `## linguistics/`, i.e. after
`- \`semantics-pragmatics.md\` — …` (base line 239) and before
`- \`sociolinguistics-registers.md\` — …` (base line 240). Ordering is convention only — the sweep
does **not** check row order (rehearsed N7: a row moved to the end of the section still exits 0),
so the round-50 finding stands.

Derive the row line with the sweep tool's own function (this exact command was rehearsed; it emits
a line byte-identical to the row that passed):

```sh
python3 -B -c 'import sys; sys.path.insert(0, "reports/round-28/readme"); from sweep import topic_of; print("- \x60sign-languages-manual-modality.md\x60 \u2014 " + topic_of("corpus/knowledge/linguistics/sign-languages-manual-modality.md"))'
```

Do **not** hand-type the backticks inside a double-quoted shell string: `sh` command-substitutes
them (rehearsed failure: `sign-languages-manual-modality.md: command not found`).

**Head-field hazard (measured).** `TOPIC_RE` is `^- topic:(.*?)(?=\n- \w)` with `re.S`
(`sweep.py:50`): the topic field only ends at the next head-block key line. The entry contract's
eight-field head supplies that (the model entries put `- sources:`/`- verified-at:`/`- recheck:`/
`- couples:` after `- topic:`). Rehearsed control: an entry whose head carries **only** `- topic:`
sweeps to `topic_mismatch 1` / exit 1, because the capture then runs on into the body. So the C
entry must keep at least one further `- key:` line under `- topic:`.

### 1.3 Base-state outputs (run at the worktree, before landing)

```text
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 28, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 226 files 226
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 226 totals_ok True
footer {"date": "2026-10-21", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 226, "dir_totals": [25, 26, 28, 29, 24, 94]}
footer_live {"total": 226, "dir_totals": [25, 26, 28, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 3ea247db6ae3719f1391a45072f3169b756a5e756d8cec609efa46ffa675d78c
exit 0

$ python3 -B tools/check-readme-revisions.py
readme /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/README.md
sha256 3ea247db6ae3719f1391a45072f3169b756a5e756d8cec609efa46ffa675d78c
revision_lines [3, 14, 35, 47, 59, 69, 78, 87, 114, 134, 146, 166, 192, 202]
labels ["2.7", "2.6", "2.5", "2.4", "2.3", "2.2", "2.1", "2.0", "1.8", "1.7", "1.6", "1.5", "1.4", "1.3"]
findings 0
warnings 1
  REVISION-ORPHAN lines=[101, 112] unheaded paragraph inside revisions span (starts 'round-28 C entry landed (`linguistics/register-lexicon-ceili')
exit 0

$ python3 -B tools/check-readme-heading.py
readme /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/README.md
sha256 3ea247db6ae3719f1391a45072f3169b756a5e756d8cec609efa46ffa675d78c
h1_lines [1]
headings {"1": 1, "2": 7}
findings 0
exit 0
```

The rev-1.9 `REVISION-ORPHAN` warning is advisory: it is not counted in `ok`
(`tools/check-readme-revisions.py:164-203`) and the round-50 revision block already carries it as
carried, not repaired. Landing 2.8 shifts it to `lines=[111, 122]` and keeps `findings 0`,
`warnings 1` (rehearsed).

### 1.4 Rehearsal result and controls

Applying edits 1–6 to a `/tmp` mirror (with a stand-in `sign-languages-manual-modality.md` whose
`- topic:` line was the row text) gives:

```text
rows 227 files 227
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []   header_drift {}
totals_line 227 totals_ok True
footer {"date": "2026-10-22", ..., "total": 227, "dir_totals": [26, 26, 28, 29, 24, 94]}
footer_findings [] footer_ok True      exit 0
$ tools/check-readme-revisions.py --readme <mirror>   labels ["2.8","2.7",...]  findings 0  warnings 1  exit 0
$ tools/check-readme-heading.py  --readme <mirror>    headings {"1":1,"2":7}  findings 0  exit 0
```

| control | result |
|---|---|
| N1 one word changed in the row | exit 1, `topic_mismatch 1` |
| N2 trailing space on the row | exit 1, `topic_mismatch 1` |
| N3 doubled inner space | exit 1, `topic_mismatch 1` |
| N4 header left at `(25)` | exit 1, `header_drift {'linguistics': {'declared': 25, 'files': 26}}` |
| N5 totals line left at 226 | exit 1, `totals_ok False` |
| N6 footer vector left at `25/…` | exit 1, `FOOTER_DIR_TOTALS declared [25,…] live [26,…]` |
| N7 row out of filename order | exit 0 — order is not enforced (convention only) |
| N8 `- topic:` as the entry's only head field | exit 1, `topic_mismatch 1` |

After the landing the README is 632 lines (from 621) and the sweep must read `227 rows vs 227
files`, footer `227` / `26/26/28/29/24/94`.

---

## 2. `corpus/lessons/README.md` — indexing a new `corpus/lessons/round-51.md`

The file is machine-read by `reports/round-25/audit/c31-lessons-index-audit.py` (six checks,
`C31`–`C34c`). Four edits:

| # | anchor (base line) | change |
|---|---|---|
| 1 | after 107 (the `round-50-verifier-spotcheck.md` row, last data row) | insert the round-51 row, §2.1 |
| 2 | 109 | `**Rows: 37. Files: 37.**` → `**Rows: 38. Files: 38.**` |
| 3 | 258–263 (queue arithmetic bullet) | `Of the 37 index rows` → `Of the 38 index rows`; `the seven that carry none` → `the eight that carry none`; add `` `round-51.md` `` to the list |
| 4 | after 504 (foot) | append `## Revision 7 — round-51 lesson row (2026-10-22)`, §2.3 |

### 2.1 The §2 row (paste-ready template)

```text
| `corpus/lessons/round-51.md` | gate-keeper | 4/4 | none (no Q ids) | `reports/round-51/claims.json` | bytes=<B> lines=<L> sha8=<8hex> |
```

- cell 2 `format` must equal the audit's classifier: `gate-keeper` iff the lesson carries a line
  exactly `## Gate` (`c31-lessons-index-audit.py:59-66`), else `fragment-index` if it carries
  `## Fragment index`, else `plain`. Rehearsed both ways (N6/N7 below).
- cell 3 `contract` must equal the count of `source:` / `verified-at:` / `recheck:` / `scope:`
  line-start anchors present in the lesson (`:68-79`). The round-50 head carries all four → `4/4`.
- cell 6 (`pin`): `bytes` = file size, `lines` = `len(text.splitlines())`, `sha8` = first 8 hex of
  the file's sha256. Measure with either:

```sh
python3 -B -c "import hashlib,sys; b=open(sys.argv[1],'rb').read(); print('bytes',len(b),'lines',len(b.decode().splitlines()),'sha8',hashlib.sha256(b).hexdigest()[:8])" corpus/lessons/round-51.md
python3 -B reports/round-25/audit/c31-lessons-index-audit.py --json > /tmp/r51pin.json && python3 -c 'import json; r=[x for x in json.load(open("/tmp/r51pin.json"))["live"] if x["file"]=="round-51.md"][0]; print("bytes=%d lines=%d sha8=%s format=%s contract=%d/4" % (r["bytes"], r["lines"], r["sha8"], r["format"], len(r["contract_lines"])))'
```

Both were run against a stand-in lesson and agree. Pin the **filed** bytes: a pin on moving bytes
is not a pin (round-22 craft rule Q-22-3) and a stale pin is `C34-1 pin-drift`, exit 1 (N1).

### 2.2 Machine-read prose cells (why edits 2 and 3 are not optional)

`C34b` reads exactly two shapes: the **first** `Rows: **<n>**` in the file (queue-row count, line
258) and the **last** `**Rows: <n>. Files: <n>.**` (table/file counts, line 109)
(`c31-lessons-index-audit.py:270-296`). Therefore:

- never restate the bold table form with a dated value later in the file — a later
  `**Rows: 37. Files: 37.**` would win the last-match read and fail `C34b`; the revision blocks
  correctly use the slash form (`33/33`, `36/36`) instead;
- if the round-51 lesson introduces Q ids, add their §4 queue rows and bump line 258's count
  (and the "30 carry at least one question" figure) in the same edit; with no Q ids the queue stays
  at 78 and only the index-row count moves.

### 2.3 Revision convention at the foot

Superseding edits land as a **new `## Revision N — <title> (<date>)` block appended at the foot**,
never as an in-place rewrite of a filed row's provenance claims
(`corpus/lessons/README.md:358-361` and the closing rule restated at `:453-455`). Machine-read
count cells (line 109) are the documented exception: revisions 3, 4, 5 and 6
corrected them in place and recorded that in their block. Draft block, paste-ready:

```text
## Revision 7 — round-51 lesson row (2026-10-22)

Adds one §2 row for `round-51.md`, pinned from the live bytes by
`reports/round-25/audit/c31-lessons-index-audit.py --json`. §2's count line is
38/38; the queue still has 78 rows and eight indexed files carry no question.
Live histogram: gate-keeper 24, fragment-index 5, plain 9 (38 files total);
earlier histogram prose is dated history. Re-run
`python3 -B reports/round-25/audit/c31-lessons-index-audit.py` for the verdict.
```

Adjust the queue/histogram figures if the lesson carries Q ids or is not a gate-keeper file. The
`§3` histogram prose (`corpus/lessons/README.md:126-163`, histogram arithmetic at `:157-163`) and
the `§5` subdirectory counts are dated history by the precedent of revisions 4–6; the live figures
belong in the revision block.

### 2.4 Base-state output (run at the worktree, before landing)

```text
$ python3 -B reports/round-25/audit/c31-lessons-index-audit.py
index present: True
lesson files:  37
index rows:    37
queue rows:    78
formats:       {'gate-keeper': 23, 'fragment-index': 5, 'plain': 9}
  PASS C31_index_rows_eq_files
  PASS C32_owners_resolve
  PASS C33_formats_documented
  PASS C34_pins_rederived
  PASS C34c_shape_cells_rederived
  PASS C34b_prose_arithmetic
findings:      0
exit 0
```

### 2.5 Rehearsal result and controls

On a `/tmp` lane mirror with a copy of `corpus/lessons/` plus a stand-in `round-51.md`
(4 contract lines, `## Gate`, `## Mistakes` table, `## Frontier`; pin `bytes=1005 lines=26
sha8=42ccc40e`), edits 1–4 give:

```text
lesson files: 38   index rows: 38   queue rows: 78
formats: {'gate-keeper': 24, 'fragment-index': 5, 'plain': 9}
all six checks PASS        findings: 0        exit 0
```

| control | result |
|---|---|
| N1 wrong `sha8` in the pin cell | exit 1, `C34-1 pin-drift: [('round-51.md','sha8','00000000','42ccc40e')]` |
| N2 `format` cell `plain` for a `## Gate` file | exit 1, `C34-3 shape-cell-drift` |
| N3 `contract` cell `3/4` for a 4/4 file | exit 1, `C34-3 shape-cell-drift` |
| N4 count line left at 37/37 | exit 1, `C34-2 prose-arithmetic-drift {'stated': [37,37], 'measured': [38,38]}` |
| N5 row omitted | exit 1, `C31-1 unindexed-file: ['round-51.md']` + `C34-2` |
| N6 lesson written without `## Gate`, row declared `plain` | exit 0 (correct pairing) |
| N7 lesson without `## Gate`, row declared `gate-keeper` | exit 1, `C34-3 ('round-51.md','format','gate-keeper','plain')` |

`C32` resolves queue owners as live lane paths, `operator`/`parent`/`lore-shokunin`/`integrator`,
or a `round-N` token whose `reports/round-N/` exists (`:150-168`). Any new Q row must carry such an
owner; `reports/round-51/` exists, so a `round-51` token would resolve.

---

## 3. `corpus/lessons/round-50.md` head and section shape (template for round-51.md)

Head, byte-exact in shape (round-50.md:1-7; each contract line is one physical line and must start
at column 1 — the audit anchors on `^source:`, `^verified-at:`, `^recheck:`, `^scope:`):

```text
# Round 50 — lesson (kotodama, hyaku phase 2)
<blank>
source: `reports/round-50/claims.json` (declaration); `reports/round-50/validation.json` (acceptance receipt); `.ufo/waves/round-50/` (wave specs, registries and seat reports); the URLs opened in `## Gate`
verified-at: 2026-10-21 — lane `main`, base `4ad2683`; Gate rows opened the same day by round-50 build seats and re-checked by the integrator where noted
recheck: whenever a `corpus/SOURCES.md` row's `status`, `recheck` or `used-by` changes (log old→new in that round's lesson), and on the per-row `recheck` cadences
scope: the round-50 record — Gate evidence for SOURCES S048–S069, the outside spot-check intake, mined mistakes and frontier; it admits nothing and certifies no verdict
<blank>
<opening prose paragraph: round, coordinator, claims with their lands, where the verdicts live>
```

Section order after the head (round-50.md section map):

| line | section | shape |
|---|---|---|
| 9–16 | opening prose | coordinator, claims `**C**/**O**/**Ca**` with lands, pointer to `validation.json`/`SCORECARD.md`/`LOG.md` |
| 17 | `## Spot-check intake (<round> outside verifier)` | prose: what the outside record adjudicated and the disposition |
| 27 | `## Gate` | one lead-in sentence naming the row range, date and seats; then one bullet per row |
| 57 | `## Status and used-by change log` | prose: new rows' `status`/`used-by`, any supersession, the `corpus/SOURCES.md` preamble pointer old→new, and an explicit "no existing row changed" sentence |
| 66 | `## Mistakes` | pipe table, header `\| id \| class \| evidence pointer \| captured-by \| fix \|` + separator `\|---\|---\|---\|---\|---\|`, one row per mistake |
| 74 | `## Frontier` | bullets: carried items, leads (not registered), with the owning report/command |
| 81+ | `## Falsify wave (…)`, `### Corrections to the Mistakes rows above (append-only)`, `### Carried (falsify findings not repaired this round)`, `### Final review reconciliation (same round)` | post-landing appends; the second `## Mistakes`-shaped table at `:98-99` carries post-landing ids |

Gate bullet form (round-50.md:32-56) — keep one bullet per S-row, one line each:

```text
- S048 — https://www.fao.org/4/y2647e/y2647e02.htm — accessed 2026-10-21 — §Classifying pastoral systems: "there is little or no impetus to herd animals". Grounds the register's conditions, typology, species count and stage-ladder refutation. Seats: ScribeSec01Register, ScribeSec11Decision, ScoutCalibrationRegistry; integrator re-fetch.
```

`- S<NNN> — <URL> — accessed <YYYY-MM-DD>[ via Wayback <stamp> (<reason>)] — <location>: "<quote ≤25 words>". <what it grounds>. Seat: <SeatName>[, …].`

Mistakes row form (round-50.md:70, one line per cell row):

```text
| R50-M1 | <class: what went wrong, in one clause> | `<evidence path>:<lines>`; `.ufo/waves/round-50/build/<Seat>.md` | <captured-by, or "none at the time"> | <fix landed, or "none at the time"; state the control that fails with the fix reverted> |
```

Source-change log content that round-51 must mirror (`round-50.md:59-64`): which new rows entered
which status with which `used-by`; any in-place change to an existing row's `status`/`recheck`/
`used-by` logged old→new; and the `corpus/SOURCES.md` preamble pointer. That pointer is at
`corpus/SOURCES.md:8` and currently reads
`` `lessons/round-49.md` for S001–S047, `lessons/round-50.md` for S048–S070 `` — round 51 extends
it with `` `lessons/round-51.md` for S071–S<last> `` (the L1 renumbers the ids). The lesson must
also carry `## Gate` bullets for exactly those rows: the lesson is the registry's declared Gate
holder, and claim C must not cite `corpus/lessons/round-51.md` (claims.json `must_not_cite`), so
the Gate bullets and the C entry must stay textually separate.

---

## 4. Result

All three assigned items are answered with the exact edits, anchors and paste-ready text above, and
every leg was rehearsed to green on a throwaway mirror and broken on purpose (13 controls, all
behaved as documented). Nothing in the lane was changed by this seat other than the incident in §5.

## 5. Incident disclosure (author-lane, self-reported)

During the first rehearsal I built a `/tmp` mirror in which `corpus/lessons/README.md` was a
**symlink** to the lane file; the mirror write therefore passed through the link and overwrote
`corpus/lessons/README.md` in the lane with a rehearsal version (one §2 row for a stand-in
`round-51.md`, the 38/38 count line, the queue-arithmetic prose, and a `## Revision 7` block). I
detected it on the next read, reverted all four changes by surgical edits (no git write command was
run), and verified restoration: `git diff -- corpus/lessons/README.md` is empty,
`git status --porcelain` shows only `?? .ufo/waves/round-51/`, and the file's sha256 is back to the
base value `62f91a93818f8b5ebddeed8ecf278a3caf2296ff34c014b8183f05249fbae18d` (504 lines). Later
rehearsals used copies, never symlinks, with a `/tmp`-containment assertion before every write. The
L1 should treat the incident as closed but is asked to confirm the file's hash independently if the
round's discipline requires it.

## 6. Unrun checks and limits

- No build/lint/test of the round's own artifacts was run (not this seat's assignment): the two
  counters and three controls were run only in their base state and against throwaway mirrors.
- The rehearsal used a stand-in entry and a stand-in lesson, so the final numbers
  (`bytes/lines/sha8`, the entry's `- topic:` text) must be re-derived from the filed bytes with
  the §2.1 commands; the row text in §1.2 is a derivation recipe, not the literal line, because the
  C seat has not written the entry's `- topic:` yet.
- Not checked here (out of scope, flagged for the L1): whether `corpus/README.md`'s new revision
  label should be `2.8` if a sibling seat also lands a revision this round; whether the round-51
  lesson should also close a lessons-README Q id (e.g. Q-28-1/Q-30-2/Q-32-5 carry lesson-index
  coverage items).
- No tool was installed or upgraded; no package manager was invoked.
