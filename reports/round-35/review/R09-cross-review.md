- Seat: R09 | reviewer | claim cross | date 2026-10-19 | baseline 4a7aede

# R09 — cross-claim review: the lessons-partition census and the inventory marker counts

**Mission** (`reports/round-35/targets.json:457-461`, seat R09): "Third cross-claim
reviewer: the new corpus entries' effect on the lessons/README census (33-file
partition) and the inventory marker counts — any counting command the integrator
must update beyond corpus/README.md." Out path `reports/round-35/review/R09-cross-review.md`.
The README side of that question is handed to this leg by C11 (`cov/C11-readme-delta.md:422-426`:
"`reports/round-35/review/R09-cross-review.md` owns 'any counting command the
integrator must update beyond corpus/README.md'"; C11 confirms at `:424-426` that the
only live documents carrying a `Total knowledge entries` line are `corpus/README.md:469,473`
and the append-only `LOG.md`).

**Method and boundaries.** Every reading below was taken at HEAD
`4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` from the lane root.
The two falsifier experiments ran on isolated `git archive HEAD` extractions under
`.scratch/r09/copy` and `.scratch/r09/clean` — **no `reports/round-*/run-validation.py`
was executed anywhere** (F-C13-1), and no byte outside `reports/round-35/review/` was
written by this seat. Both instruments used are read-only by their own construction:
`reports/round-25/audit/c31-lessons-index-audit.py` (writes nothing, `:18`) and
`reports/round-28/readme/sweep.py` (writes only inside `--selftest` synthetic trees;
no in-tree `open(...,"w")` exists outside them, grep `open(` at `:241-257,395`).
The ten entry drafts (`cov/C01..C10`) and `plan/P01-c-plan.md` were **not on disk** when
this seat opened; **eight** drafts (`C01`, `C02`, `C03`, `C05`, `C06`, `C07`, `C08`,
`C10`) landed while the review ran and are measured in §2.6, and the remaining two
(`C04`, `C09`) are recorded under `## Owed`. Every peer-fragment reading below names its
own line numbers as re-measured at this seat's cut; those seats were still writing, so
their line numbers can move while the cited text does not.

**Tree state at this cut:** `git status --porcelain corpus/` → **empty**, and the live
census still reads 21/19/18/29/20/94 = 201, so §2.1's *before* numbers are live readings
of the tree, not a reconstruction. Nothing from claim C is landed: the ten entries exist
only as drafts in `reports/round-35/cov/`, which is why §2.6 is a projection from fenced
draft bytes and §3 row 1's command remains the authority for the after-reading.

## 1. Leg 1 — the `corpus/lessons/` 33-file partition is invariant under claim C (measured)

### 1.1 What the partition census is

The partition is exactly `corpus/lessons/*.md`, one level deep, and the README is part
of it (`reports/round-25/audit/c31-lessons-index-audit.py:35-36` `LESSONS`/`INDEX`,
`:95-101` "The partition is `corpus/lessons/*.md` exactly as the round-25 runner globs
it … which includes this README"). The counting commands are declared at
`corpus/lessons/README.md:40-41`:

```sh
ls corpus/lessons/*.md | wc -l                                          # 33 (2026-10-19)
find corpus/lessons -maxdepth 1 -name '*.md' | wc -l                    # 33 (same set)
```

and the census is machine-checked by the §1 tool's `C34b` prose-arithmetic leg, which
re-derives the file's own stated row and lesson counts (`corpus/lessons/README.md:53`,
`:105-106`, `:153-159`; checks listed at `:47-54`).

### 1.2 Before reading (clean archive copy of HEAD)

```
$ python3 -B reports/round-25/audit/c31-lessons-index-audit.py
lesson files:  33
index rows:    33
queue rows:    78
formats:       {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}
  PASS C31_index_rows_eq_files
  PASS C32_owners_resolve
  PASS C33_formats_documented
  PASS C34_pins_rederived
  PASS C34c_shape_cells_rederived
  PASS C34b_prose_arithmetic
findings:      0
exit=0
```

### 1.3 Falsifier A — adding a knowledge entry cannot move it

A fabricated probe entry was added to the copy at
`corpus/knowledge/culture-material/zzz-r09-probe.md` (probe bytes, cites nothing):

```
c31 exit=0
index_rows 33 lesson_files 33 queue_rows 78 findings []
files 202 raw_lines 718 marker_occurrences 656 files_with_marker 136
```

The lessons census is byte-for-byte unchanged (33/33/78, findings `[]`, exit 0) while
the knowledge-side inventory moves on all four legs. This is the answer to the first
half of the mission: **claim C's ten new `corpus/knowledge/**` files have no effect on
the lessons/README 33-file partition, and no lessons-partition counting command needs
an update because of them.**

### 1.4 Falsifier B — what *would* move it, and the exact diagnostics

The same copy with one probe lesson file added at `corpus/lessons/round-35.md`:

```
c31 exit=1   (text mode)
findings [
 {"id": "C31-1", "class": "unindexed-file", "detail": ["round-35.md"]},
 {"id": "C34-2", "class": "prose-arithmetic-drift",
  "detail": {"table_rows_vs_files": {"stated": [33, 33], "measured": [33, 34]}}}]
```

So the partition is keyed to lesson files only. Consequence for the integrator: the
lane's habit is one lesson per round (rounds 26–32 each landed one; the last is
`corpus/lessons/round-32.md`, and rounds 33–34 landed none — `ls corpus/lessons/*.md`
→ 33). If a round-35 lesson lands, then in addition to the two diagnostics above the
README's §2 row count, §3 histogram, §4 queue and the `:40-41` annotations must be
revised **as a new revision block, never in place** (`corpus/lessons/README.md:352-355`,
`:447-448`), and the C34b check re-run — that is the round-33 revision-3 precedent
(`corpus/lessons/README.md:398-448`, counting command at `:416-425`).

### 1.5 Exit-code trap in the census tool (operability-relevant)

`reports/round-25/audit/c31-lessons-index-audit.py:446-447` returns `0`
**unconditionally** under `--json`, while text mode carries the verdict
(`:460` `return 0 if not res["findings"] else 1`). Measured on the same copy in the
same state (probe lesson present): text mode `exit=1`, `--json` `exit=0`. A caller who
reads only the JSON exit code reads a false green; the round-33 convention "must exit 0
with `findings: 0`" (`corpus/lessons/README.md:416-425`) is a **text-mode** reading.
The integrator should file the close-time census reading in text mode (or read the JSON
`findings` array, not its exit code).

### 1.6 Why this leg is cross-claim, not lessons-only

The same partition is on two other claims' surfaces, and §1.2 is the shared reading:
claim O's renderer pins four `corpus/lessons/round-6-sources/*.json` files as read-set
members (`tools/exercise-handoff-e2e.py:131-136` `SOURCE_LEDGERS`, in the counted
`V1_READ_SET` at `:462-471`, count-checked at `:1349-1350` `E2E-COUNT`), and claim A's
audit lists `corpus/lessons/README.md` as a touched surface
(`reports/round-35/review/R06-a-review.md:44,62-79`; `reports/round-35/adj/A09-receipt.md`;
`reports/round-35/scribe/S03-a-receipt.md:38,69`). Claim C writes neither.

## 2. Leg 2 — the inventory marker counts: before measured, partial after measured from the landed drafts

### 2.1 Before (measured live at `4a7aede`, both in-tree and in the clean copy)

`python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`:

| metric | value |
|---|---|
| `files` | **201** |
| `lines` | 36 395 |
| `raw_lines` | **717** |
| `raw_occurrences` | **731** |
| `ci_occurrences` | 733 |
| `case_variant_occurrences` | 2 |
| `marker_occurrences` | **655** (bare **621** + detailed **34**) |
| `marker_lines` | **650** |
| `files_with_marker` | **135** |
| `files_with_any_mark` | 147 |
| `unparenthesized_occurrences` | 78 |
| `class_totals` | substantive-flag-candidate 563 / policy-use-mention 37 / needs-review 133 |
| `skipped` | `[]` |

Metric definitions are the tool's own (`tools/source-audit-inventory.py:22-45`), the
totals keys at `:233-239`; `--selftest` is fixture-constant-based (`:385-407`) and
therefore **cannot** be broken by claim C — measured `SELFTEST PASS … exit=0`.

### 2.2 What a coverage wave does to these numbers — measured precedents

| wave | new entries | `to-verify` occurrences carried by the new entries |
|---|---|---|
| round 10 (`94ca098`) | 10 | **78** (`git show 94ca098:<path> \| grep -c -i 'to-verify'`, per file: 3/12/23/12/11/4/0/7/4/2) |
| round 19 (`caf1bea`) | 10 | **28** (11/4/1/1/2/1/1/4/2/1) |
| round 28 (`3b13a2f`) | 1 | **0** (`corpus/knowledge/linguistics/register-lexicon-ceilings.md`) |

So the after-side of every marker metric is a function of the ten drafted bytes, and the
plausible band for a ten-entry wave is +0 to +78 occurrences (both extremes measured).
**The integrator must re-measure, not assume the totals hold**: claim C's own
`after_required` permits in-file marks ("every citation resolves or is marked
`to-verify` in-file", `reports/round-35/claims.json:29`).

### 2.3 Where the after-numbers must be filed

* `corpus/README.md:471-474` — the counts footer names the inventory command but quotes
  **file totals only** (`(total 201 files; directory totals 21/19/18/29/20/94)`), plus
  the standing caveat "The inventory counts markers, not verified facts" (`:474`). The
  README delta therefore owes no marker number (C11 owns the file-total edits,
  `cov/C11-readme-delta.md:400-413`).
* The round-35 **SCORECARD** row and **LOG** entry are the record sites that will quote
  marker numbers, and the precedent is to quote them with the command: `SCORECARD.md:34`
  ("592 raw marker-bearing lines, 598 raw occurrences" with the inventory command),
  `SCORECARD.md:16` ("A raw file or marker count is not a quality score"). Both are
  parent-owned and append-only; this seat writes neither.

### 2.4 Negative result — no stale present-tense marker claim exists to repair

Repo-wide grep for the live marker totals (`655`, `621`, `650`, `717`, `731`, `733`)
over `*.md`/`*.json`/`*.py`, excluding filed rounds 1–34, returns **zero live
present-tense claims**; the matches are unrelated numerals (dates, leaf numbers, page
ranges). The only live document carrying a corpus total at all is `corpus/README.md`
(C11's reading, `cov/C11-readme-delta.md:424-426`), and it carries file counts, not
marker counts. This leg's answer to "beyond corpus/README.md" is therefore: **no stale
number to fix, one instrument to re-run, and two new record sites that must carry
freshly measured numbers.**

### 2.5 Dated readings that must not be "corrected"

Four live corpus entries carry partition totals or denominators as *dated, pinned*
readings, and the convention is stated in the first of them ("a header count is always
a point-in-time reading and is re-measured before quoting"):

* `corpus/knowledge/verification/verification-independence-anti-circularity.md:17`
  (`totals.files=181` / `183` at 21:33:25Z),
* `corpus/knowledge/verification/header-conformance-readings.md:61` (per-partition
  Reading-A remainders 19/94, 16/16, 16/16, 13/13, 0/16, 0/24),
* `corpus/knowledge/myth-symbol/divination-omen-systems.md:27,37` (myth-symbol before-state
  `16`, with its in-entry `ls corpus/knowledge/myth-symbol/ | wc -l` command),
* `corpus/knowledge/culture-material/vessel-container-lexicon.md:11` (culture-material
  "16 committed files" before-state).

After claim C these denominators are two waves stale. They are dated readings inside
filed corpus entries, not live claims: the integrator must not rewrite them, and the ten
new entries should state their own before-state counts in the same dated shape (the
authors' precedent above) rather than as present-tense totals.

### 2.6 Partial after-side, measured from the drafts that had landed at this cut

Eight of the ten entry drafts landed while this review ran (`cov/C01-entry-1.md`,
`C02-entry-2.md`, `C03-entry-3.md`, `C05-entry-5.md`, `C06-entry-6.md`,
`C07-entry-7.md`, `C08-entry-8.md`, `C10-entry-10.md`; `C04` and `C09` still absent).
Their **entry bytes** — the fenced blocks carrying a `- topic:` head line, i.e. what the
integrator applies to `corpus/knowledge/` — were parsed and counted:

| draft | entry blocks | raw `to-verify` | R1 markers (bare + detailed) | R2 markers (bare + detailed) | file sha8 at R2 |
|---|---|---|---|---|---|
| `C01-entry-1.md` | 1 | 42 | 0 (0 + 0) | **42 (42 + 0)** | `4e4c355e` |
| `C02-entry-2.md` | 1 | 38 | 20 (12 + 8) | 20 (12 + 8) | `6746faf3` |
| `C03-entry-3.md` | 1 | 24 | 20 (18 + 2) | 20 (18 + 2) | `82af002e` |
| `C05-entry-5.md` | 1 | 31 | 5 (5 + 0) | 5 (5 + 0) | `d6f930b2` |
| `C06-entry-6.md` | 1 | 39 | 1 (1 + 0) | 1 (1 + 0) | `5558ace8` |
| `C07-entry-7.md` | 1 | 15 | 4 (3 + 1) | 4 (3 + 1) | `ce88156a` |
| `C08-entry-8.md` | 1 | 61 | 6 (6 + 0) | 6 (6 + 0) | `2540bc2a` |
| `C10-entry-10.md` | 1 | 28 | 22 (5 + 17) | 22 (5 + 17) | `f7ab0971` |
| **eight drafts** | 8 | **278** | **78 (50 + 28)** | **120 (92 + 28)** | — |

**The drafts moved between the two readings.** R1 was taken when the review reached
§2.6; R2 a few minutes later. Only `C01` changed: its author rewrote the entry so that all
42 of its raw mentions became parenthesized `(to-verify)` marks (0 → 42), moving the
eight-draft marker total 78 → 120 while the raw total stayed at 278. Both readings are
recorded as dated readings of live bytes, per the lane's rule that a superseded reading is
preserved, not overwritten (`corpus/lessons/README.md:213` Q-22-3: "successor pins must
bind final bytes; a pin on moving bytes is not a pin").

Projection if these eight land byte-identical at R2 (§2.1's command re-run on the landed
tree):

| metric | before | projected after eight (R2) |
|---|---|---|
| `files` | 201 | 209 |
| `raw_occurrences` | 731 | **1 009** |
| `marker_occurrences` | 655 | **775** (bare 713, detailed 62) |
| `unparenthesized_occurrences` | 78 | **236** |

The split still matters more than the magnitude: of the +278 raw occurrences,
+158 are **unparenthesized** (fetch flags and policy prose in the `verified-at` lines —
C01's own header declares that pattern, "an explicit `to-verify` fetch flag in the entry's
own `verified-at` line and §8") and +120 are parenthesized marks, so the
`needs-review` / `policy-use-mention` classes move on the larger share and the
substantive `(to-verify)` class on the smaller. That is exactly the distinction
`corpus/README.md:474`'s caveat protects: a rising raw count is not rising uncertainty,
and a rising marker count is not a quality score (`SCORECARD.md:16`).

Three reading hazards for whoever re-measures:

1. **Fence shape.** Five of the eight drafts fence their entry bytes with **four**
   backticks — C01 `:42-262`, C03 `:35-237`, C05 `:67-211`, C08 `:81-286`, C10 `:26-333` —
   and three with three: C02 `:15-195`, C06 `:26-200`, C07 `:41-242`. A
   three-backtick-only parse therefore reads **zero** entry blocks for five of the eight;
   the count above handles both widths (four-backtick first, then three-backtick over the
   remainder).
2. **Draft ≠ landed bytes, and the drafts are live.** The R1→R2 delta above is the
   evidence: a projection taken from a draft is a pin on moving bytes. The integrator must
   re-measure on the **landed** tree (after the drafts freeze and `C04`/`C09` arrive)
   before quoting any after-number; the projection is a bound, not the after-reading, and
   §3 row 1's command is the authority.

## 3. The deliverable — counting commands the integrator must run/update beyond `corpus/README.md`

| # | command | status under claim C | evidence |
|---|---|---|---|
| 1 | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` (`claims.json:32`) | command unchanged; **consumer numbers move** (`files` 201→211; every marker metric re-measured); `--selftest` unaffected | `tools/source-audit-inventory.py:22-45,233-239,385-407`; measured 201/717/655/650/135 and `SELFTEST PASS exit=0`; before-leg already filed by `cov/C15-receipt.md:69` (reading) and `:136` (after-target row) |
| 2 | `python3 -B reports/round-28/readme/sweep.py` (add `--json` for a receipt) | **not in `claims.json`'s counting-command list (`:31-33`)** — the integrator must add it; it is the only instrument that reads the README's rows, section headers, totals line **and counts footer** | baseline measured green by this seat: `ok True`, `rows 201 files 201`, `missing []`, `header_drift {}`, `totals_line 201`, `totals_ok True`, `footer_ok True`, `exit=0`; `--selftest` 12/12; instrument internals `:59-61,66,74-79,92,108,140,394-401`; negative control measured below |
| 3 | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (text mode) | run at close to file the partition reading; **33 stays 33** for claim C | §1.2–1.4; exit-code trap §1.5 |
| 4 | `ls corpus/lessons/*.md \| wc -l`; `find corpus/lessons -maxdepth 1 -name '*.md' \| wc -l` (`corpus/lessons/README.md:40-41`) | **no update owed** for claim C; the `# 33 (2026-10-19)` annotations move only with a new revision block if a lesson lands | §1.3 |
| 5 | the r7 chain's read-set count/digest leg (`python3 -B tools/exercise-handoff-e2e.py --profile v3 …`) | **no update owed**; its five corpus members (1 knowledge + 4 lessons, digests in `reports/round-34/handoff/declared-in-r7/expected.json` `inputs`) are untouched by claim C — the r7 exit-0 regression leg claim O already requires doubles as claim C's cross-claim digest control | **source-read by this seat, not executed**: `tools/exercise-handoff-e2e.py:118,131-136,462-471,1349-1350`; `expected.json` `inputs["corpus/knowledge/synthesis/worldbible-integration-contract.md"] = 5f4c02bf…`, four `corpus/lessons/round-6-sources/*.json` |

Negative list (measured, so the integrator does not have to re-hunt): no tool, gate or
battery hardcodes the partition vector or the corpus totals — `tools/gates/expected/` is
keyed by per-gate baseline ids, the `corpus/knowledge` hits under `tools/gates/frozen/**`
are per-file provenance receipts with digests, `SCORECARD.md` rows are per-round
historical, and `MINT.md`/`PROVINCE.md`/`README.md`/`SHONEN.md` carry no corpus counts
(grep 2026-10-19). Round 34's box-1 re-survey counts `SKILL.md` citation rows, not corpus
entries (`reports/round-34/craft/box1-resurvey-durable.json` keys: `skill_lines 732`,
`named_in_skill 28`, `rows[28]`), so claim C does not interact with it.

**Negative control for command 2** (run in `.scratch/r09/copy`, one unreconciled probe
entry added, README untouched): `exit=1`, `missing_from_index 1
['culture-material/zzz-r09-probe.md']`, `header_drift {'culture-material': {'declared':
18, 'files': 19}}`, `totals_ok False`, `footer_findings [FOOTER_TOTAL {declared 201, live
202}, FOOTER_DIR_TOTALS …]`, `footer_ok False`. The instrument fails loudly on exactly the
half-reconciled state claim C's landing produces, so a green run after integration is a
real reading, not a green-by-construction self-test.

### 3.1 F-R09-1 — a peer citation that does not resolve (correction, not a method defect)

C11's method section cites `reports/round-28/readme/sweep.py:21 (ROW_RE), :22 (TOPIC_RE)`
(`cov/C11-readme-delta.md:22-24`, its span at this cut — C11 grew from 460 to 489 lines
while this review ran, moving its own pointer from `:14-15` to `:22-24`). Measured at
`4a7aede`, the cited sweep lines are docstring text;
the regexes are `SECTION_RE :59`, `ROW_RE :60`, `TOPIC_RE :61` (and `FOOTER_RE :66`). The
method C11 describes is unaffected — the row/topic equality it builds on is real
(`:74-79` `topic_of`, `:92` row parse, `:108` footer parse, `:140` equality test) — but
the two line pointers are off by ~39 lines and should be corrected in the applied
revision note so a reader can re-derive the invariant. Filed per the round rule that a
source citation which does not resolve is reported, never inherited.

## 4. Environment hazard measured during this review (operational note for the integrator)

`/tmp` on this host is a 16 GB tmpfs at 80 % with the user's write quota exhausted:
two receipt writes to `/tmp` came back **empty with exit 120** and
`OSError: [Errno 122] Disk quota exceeded` (`df -h /tmp` → `tmpfs 16G 13G 3.1G 80%`;
a bare `tempfile.NamedTemporaryFile(dir='/tmp')` write raises the same error). A seat
that files a receipt to `/tmp` can produce an empty artifact that reads like a tool
failure. Receipts must go under `.scratch/` or `reports/round-35/`.

## 5. Verdicts

| leg | verdict | basis |
|---|---|---|
| lessons/README 33-file partition | **unchanged** by claim C (provable) | §1.2–1.4, both falsifiers executed |
| inventory marker counts | **before measured; partial after-side measured twice from the eight landed drafts (R1→R2 moved: 78 → 120 markers)** (§2.6); full after-reading owed | §2.1–2.2, §2.6 |
| counting commands beyond `corpus/README.md` | **delivered** | §3, five rows + negative list + one executed negative control |

## Owed

- `reports/round-35/plan/P01-c-plan.md` — absent at this cut; names the ten entry topics.
- `reports/round-35/cov/C04-entry-4.md`, `C09-entry-9.md` — two of the ten drafted entry
  bytes absent at this cut, so §2.6's projection covers eight entries only. The integrator
  re-runs §2.1's command on the landed tree and files the after-numbers in the
  SCORECARD/LOG round record.
- `reports/round-35/run-validation.py` — claim C's counting command 3 (`claims.json:33`);
  absent at this cut (C15 also owes it, `cov/C15-receipt.md:116`).
- The after-state re-measurement of both legs (§1.2 census reading and §2.1 inventory
  totals) is integrator-only: it requires the landed tree.

## Citations

Paths:lines read or cited: `reports/round-35/targets.json:457-461`;
`reports/round-35/claims.json:21-35` (esp. `:29,:31-33`);
`reports/round-35/cov/C11-readme-delta.md:22-24` (the F-R09-1 non-resolving pair),`:400-426`;
`reports/round-35/cov/C15-receipt.md:69,116,136`;
`reports/round-35/cov/C01-entry-1.md:42-262`; `C02-entry-2.md:15-195`;
`C03-entry-3.md:35-237`; `C05-entry-5.md:67-211`; `C06-entry-6.md:26-200`;
`C07-entry-7.md:41-242`; `C08-entry-8.md:81-286`; `C10-entry-10.md:26-333`
(entry-byte fences counted in §2.6);
`reports/round-35/review/R06-a-review.md:44,62-79`;
`reports/round-35/scribe/S03-a-receipt.md:38,69`;
`reports/round-35/adj/A09-receipt.md:51,70`;
`corpus/lessons/README.md:40-41,47-54,105-106,153-159,213,352-355,398-448`;
`corpus/README.md:469,471-474`;
`reports/round-25/audit/c31-lessons-index-audit.py:18,35-36,95-101,446-447,460`;
`reports/round-28/readme/sweep.py:59-61,66,74-79,92,108,140,241-257,394-401,420,427`;
`tools/source-audit-inventory.py:22-45,233-239,385-407`;
`tools/exercise-handoff-e2e.py:118,131-136,462-471,1349-1350`;
`reports/round-34/handoff/declared-in-r7/expected.json` (`inputs`, 58 members);
`reports/round-34/craft/box1-resurvey-durable.json`;
`corpus/knowledge/verification/verification-independence-anti-circularity.md:17`;
`corpus/knowledge/verification/header-conformance-readings.md:61`;
`corpus/knowledge/myth-symbol/divination-omen-systems.md:27,37`;
`corpus/knowledge/culture-material/vessel-container-lexicon.md:11`;
`SCORECARD.md:16,34`.

Line numbers inside peer round-35 fragments were re-measured at this seat's cut
(2026-10-19); those seats were still writing, so their fragments' line numbers can move
between readings — the cited text, not the number, is the binding reference.

Commands run (all from the lane root, `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`, HEAD `4a7aede`; falsifier runs inside
`.scratch/r09/{clean,copy}`, extracted with `git archive HEAD | tar -x`):

- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → 33 files / 33 rows /
  78 queue rows / formats `{'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}` /
  6 PASS / `findings: 0`, exit 0 (receipt `.scratch/r09/receipts/c31-clean.txt`).
- `python3 -B reports/round-28/readme/sweep.py --json` → `ok True`, `rows 201 files 201`,
  `totals_line 201`, `totals_ok True`, `footer_ok True`, exit 0
  (receipt `.scratch/r09/receipts/sweep-clean.json`).
- `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
  → totals in §2.1; `python3 -B tools/source-audit-inventory.py --selftest` → PASS, exit 0.
- falsifier A: `printf '# probe entry …\n' > corpus/knowledge/culture-material/zzz-r09-probe.md`
  in the copy → c31 exit 0 / 33/33/78 / `findings []`; inventory `files 202 raw_lines 718
  marker_occurrences 656 files_with_marker 136`.
- falsifier B: `printf '# round-35 probe lesson …\n' > corpus/lessons/round-35.md` in the
  copy → c31 text `exit=1` with `C31-1 unindexed-file ['round-35.md']` and `C34-2
  prose-arithmetic-drift {stated [33,33], measured [33,34]}`; `--json` `exit=0` (trap §1.5).
- negative control for command 2: `python3 -B reports/round-28/readme/sweep.py` in the copy
  with the probe entry present → exit 1, `missing_from_index 1`, `header_drift
  {'culture-material': {'declared': 18, 'files': 19}}`, `FOOTER_TOTAL`/`FOOTER_DIR_TOTALS`,
  `totals_ok False`, `footer_ok False`.
- `for c in 94ca098 caf1bea 3b13a2f; do git show --diff-filter=A --name-only --pretty=format: $c | grep '^corpus/knowledge' | while read f; do printf "%s %s\n" "$(git show $c:$f | grep -c -i 'to-verify')" "$f"; done; done`
  → §2.2 precedent table (78 / 28 / 0).
- `df -h /tmp`; `python3 -B -c "import tempfile; …dir='/tmp'…"` → §4 quota evidence.
