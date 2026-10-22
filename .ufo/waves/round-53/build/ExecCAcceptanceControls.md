# ExecCAcceptanceControls — round 53, claim C acceptance controls

**Seat:** `KotodamaR53.ExecCAcceptanceControls` (executor, leaf)
**Date:** 2026-10-22
**Assigned item:** build the acceptance controls for claim C (coverage: one new
knowledge entry, `corpus/knowledge/linguistics/gesture-co-speech-pointing.md`,
knowledge files 228 → 229) and record, for every control, the printed lines and
the exit code of `python3 -B reports/round-53/accept-c.py`.
**Judged axis:** coverage.
**Scope note:** sandbox only. The lane repo was not edited except for this report
file. No subagent was spawned. No tool was installed (nothing needed installing).

---

## 1. Sandbox

- Path: `/fast/scratch/hyaku/kotodama-r53/ExecCAcceptanceControls`
- Command:
  `git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r53/ExecCAcceptanceControls && git -C /fast/scratch/hyaku/kotodama-r53/ExecCAcceptanceControls checkout -q 60f1d2a3d832b926e37f82b11c67496d131a1431`
- `git rev-parse HEAD` → `60f1d2a3d832b926e37f82b11c67496d131a1431`
  (`60f1d2a round-53: declaration — claim D (depth, repair-first: speech-surrogates
  routed defects, d-count OPEN 18 -> 0) and claim C (coverage, learning and sourced:
  gesture entry, 228 -> 229); separability manifest; dry-run receipt`).
- The claim's own base is `a9cf95f` (the commit before the declaration); the
  declaration commit `60f1d2a` adds only `claims.json`,
  `separability-manifest.json` and the telemetry receipt, so the knowledge tree and
  `corpus/SOURCES.md` are identical at both. Measured: `find corpus/knowledge -name
  '*.md' | wc -l` → 228 in the sandbox and in the lane worktree; `## linguistics/
  (27)`, `Total knowledge entries: 228.`, footer `(total 228 files; directory totals
  27/26/28/29/24/94).` at `corpus/README.md:242`, `:614`, `:618`.
- Control trees (each a copy of the sandbox with `.git` removed, each mutated by a
  script in `/fast/scratch/hyaku/kotodama-r53/`):
  `ctrl-a … ctrl-f` (the six assigned controls), `ctrl-f2`,
  `diag-full … diag-dup-row`, `edge-f2clean`, `edge-norow`, `edge-pipe`,
  `edge-nosid`, `edge-lowid`, `edge-place`, `edge-stray`, `edge-short`,
  `edge-prose`, `edge-bare`, `edge-notopic`, `edge-rev`, `edge-order`.
  Builder scripts: `mk_control.py`, `mk_diag.py`, `mk_edge.py`, `mk_place.py`,
  `mk_stray.py`, `mk_short.py`, `mk_prose.py`, `mk_rev.py`, `mk_notopic.py`,
  `mk_multiline.py`. Consolidated transcript: `controls-transcript.txt`.

## 2. The instrument under test

`reports/round-53/accept-c.py` (read at the sandbox, line numbers from that file):

- `ENTRY = "corpus/knowledge/linguistics/gesture-co-speech-pointing.md"` (line 22)
- `TOTAL = 229` (line 23), `FIRST_SID = 187` (line 24)
- **COUNT** (line 34) — recursive `os.walk` over `corpus/knowledge` counting every
  `.md`, must be exactly 229.
- **ENTRY** (line 37) — the file exists.
- **SWEEP** (lines 39–51) — runs `python3 -B reports/round-28/readme/sweep.py` as a
  **subprocess with no pipe**, so the sweep's own exit code is read; additionally
  requires the printed `rows 229 files 229` and `missing_from_index 0`.
- **SIDS** (lines 53–79) — every `S\d{3}` in the entry must be ≥ S187, must have a
  `corpus/SOURCES.md` row with ≥ 12 pipe-split cells, must have `status` (`cells[8]`)
  equal to `mined`, and must have the entry path in `used-by` (`cells[11]`). At
  least one S-id must be cited.

Base run (sandbox at `60f1d2a`), matching
`reports/round-53/telemetry/declaration-dry-run.txt` byte for byte:

```
COUNT FAIL knowledge_files=228 required=229
ENTRY FAIL corpus/knowledge/linguistics/gesture-co-speech-pointing.md
SWEEP FAIL exit=0 rows 228 files 229 missing_from_index 0 []
SIDS FAIL cited=0 bad=['entry absent']
EXIT=1
```

## 3. The six assigned controls — printed lines and exit codes

Every run below is `python3 -B reports/round-53/accept-c.py` with the sandbox root
as the working directory. The exit code is the instrument's own.

### (a) the claim-C landing shape — expect exit 0

State built: the synthetic entry at
`corpus/knowledge/linguistics/gesture-co-speech-pointing.md` with a `- topic:`
line; a mined `| S187 |` row in `corpus/SOURCES.md` whose used-by names the entry;
the README index row; `## linguistics/ (28)`; `Total knowledge entries: 229.`; the
footer at `(total 229 files; directory totals 28/26/28/29/24/94).`

```
COUNT PASS knowledge_files=229 required=229
ENTRY PASS corpus/knowledge/linguistics/gesture-co-speech-pointing.md
SWEEP PASS exit=0 rows 229 files 229 missing_from_index 0 []
SIDS PASS cited=1 bad=[]
EXIT=0
```

**Exit 0 as expected.**

### (b) as (a), README index row removed — expect exit 1, SWEEP FAIL, missing_from_index 1

```
COUNT PASS knowledge_files=229 required=229
ENTRY PASS corpus/knowledge/linguistics/gesture-co-speech-pointing.md
SWEEP FAIL exit=1 rows 228 files 229 missing_from_index 1 ['linguistics/gesture-co-speech-pointing.md']
SIDS PASS cited=1 bad=[]
EXIT=1
```

**Exit 1 as expected**, with the missing index row named exactly.
`reports/round-28/readme/sweep.py` run directly on the same tree prints
`missing_from_index 1 ['linguistics/gesture-co-speech-pointing.md']` and exits 1.

### (c) the entry cites S186 (below 187) — expect exit 1

```
COUNT PASS knowledge_files=229 required=229
ENTRY PASS corpus/knowledge/linguistics/gesture-co-speech-pointing.md
SWEEP PASS exit=0 rows 229 files 229 missing_from_index 0 []
SIDS FAIL cited=1 bad=['S186:below-S187']
EXIT=1
```

**Exit 1 as expected.** A variant that cites S186 *and* S187 gives
`SIDS FAIL cited=2 bad=['S186:below-S187']` — the floor is applied to every cited
id, not only to the first.

### (d) the cited row is `queued` — expect exit 1

```
COUNT PASS knowledge_files=229 required=229
ENTRY PASS corpus/knowledge/linguistics/gesture-co-speech-pointing.md
SWEEP PASS exit=0 rows 229 files 229 missing_from_index 0 []
SIDS FAIL cited=1 bad=['S187:status-queued']
EXIT=1
```

**Exit 1 as expected.**

### (e) the cited row's used-by does not name the entry — expect exit 1

```
COUNT PASS knowledge_files=229 required=229
ENTRY PASS corpus/knowledge/linguistics/gesture-co-speech-pointing.md
SWEEP PASS exit=0 rows 229 files 229 missing_from_index 0 []
SIDS FAIL cited=1 bad=['S187:used-by']
EXIT=1
```

**Exit 1 as expected.** Two used-by variants fail the same way: the cell set to
`—` (control e) and the cell naming the entry by bare filename only
(`gesture-co-speech-pointing.md`, probe `edge-bare`). The check is a substring test
for the exact repo-relative path `corpus/knowledge/linguistics/gesture-co-speech-pointing.md`
(`accept-c.py:75`), so the full path with the `corpus/knowledge/` prefix is required.

### (f) a second new file, so the count is 230 — expect exit 1

```
COUNT FAIL knowledge_files=230 required=229
ENTRY PASS corpus/knowledge/linguistics/gesture-co-speech-pointing.md
SWEEP FAIL exit=1 rows 229 files 230 missing_from_index 1 ['linguistics/second-gesture-fixture.md']
SIDS PASS cited=1 bad=[]
EXIT=1
```

**Exit 1 as expected.** In this build the README was left at 229, so both COUNT and
SWEEP fail. The cleaner build — the second file indexed and the README made
internally consistent at 230 (`edge-f2clean`) — isolates the count leg:

```
COUNT FAIL knowledge_files=230 required=229
ENTRY PASS corpus/knowledge/linguistics/gesture-co-speech-pointing.md
SWEEP FAIL exit=0 rows 230 files 230 missing_from_index 0 []
SIDS PASS cited=1 bad=[]
EXIT=1
```

The sweep itself is green there (exit 0, no missing rows, footer consistent); only
the hard-coded `TOTAL = 229` in `accept-c.py` fails it. This is the exact state the
L1 should avoid landing.

## 4. Any leg that passes when it should fail

**None.** All six assigned controls behave as specified: (a) exits 0 and (b)–(f)
exit 1, each for the stated reason. No leg was observed to pass while its defect
was present.

Two arms of the instrument are worth stating explicitly, because they show the legs
are not vacuous:

- **The SWEEP leg is genuinely red-able.** It reads the sweep's own exit code
  (no pipe), so every README defect the sweep measures turns the leg red:
  - index row removed → `SWEEP FAIL exit=1 … missing_from_index 1 [...]`
  - section header left at 27 → `SWEEP FAIL exit=1`, and the sweep prints
    `header_drift {'linguistics': {'declared': 27, 'files': 28}}`
  - totals line left at 228 → `SWEEP FAIL exit=1`, sweep prints
    `totals_line 228 totals_ok False`
  - counts footer left at 228 → `SWEEP FAIL exit=1`, sweep prints
    `footer_findings [{"class": "FOOTER_TOTAL", "declared": 228, "live": 229, ...},
    {"class": "FOOTER_DIR_TOTALS", "declared": [27, 26, 28, 29, 24, 94],
    "live": [28, 26, 28, 29, 24, 94], ...}]`
  - index row topic paraphrased instead of byte-equal → `SWEEP FAIL exit=1`, sweep
    prints `topic_mismatch 1 ['linguistics/gesture-co-speech-pointing.md']`
  - the entry has no `- topic:` line at all → `SWEEP FAIL exit=1`, sweep prints
    `topic_mismatch 1 [...]` (class `NO_TOPIC_FIELD`)
- **The SIDS leg is genuinely red-able on each of its four conditions.** Below the
  floor → `S186:below-S187`; no registry row → `S187:no-row` (probe `edge-norow`);
  status not `mined` → `S187:status-queued`; used-by without the entry path →
  `S187:used-by`. An entry citing no S-id at all → `SIDS FAIL cited=0 bad=['no S-id cited']`.

One weakness found in `accept-c.py` itself, reported for the L1's judgement (not a
change made here):

- **A malformed registry row can produce a misleading reason.** `accept-c.py:63`
  splits each `| S\d{3} ` line on `|` and reads `cells[8]` and `cells[11]`. A row
  with an unescaped `|` inside a cell shifts every later cell, so the leg reports
  the wrong cause: the `edge-pipe` build (a `|` added inside the anchor cell)
  printed `SIDS FAIL cited=1 bad=['S187:status-gesture is part of the utterance and
  carries meaning that speech does not; gesture and speech form a single system']` —
  the status cell had been shifted into the teaches cell. The build still **exits
  1**, so the acceptance is still red; only the reason string is wrong. Separately,
  `tools/check-source-access.py` refuses such a row outright
  (`ACCESS_INPUT_ERROR row S187 at line 217 has 12 cells, not 11`, exit 2), so a
  row that malformed would be caught by the corpus's own checker anyway. A short
  row (10 cells) is likewise refused by that checker (`has 10 cells, not 11`).
- **The SIDS leg does not check that the S-id row is in the `## Registry` table.**
  Moving the `| S187 |` row to the end of `corpus/SOURCES.md`, outside the table,
  still gives `SIDS PASS` and exit 0 (probe `edge-place`), because the leg scans
  every `| S\d{3} ` line in the file. The corpus's own contract requires the row to
  live in the Registry table; the acceptance does not enforce it. Advice: put the
  row in the Registry table, appended after S186 (the current last row,
  `corpus/SOURCES.md:215`), and let the table keep its 11-column shape.
- **COUNT and the sweep count different sets.** COUNT walks `corpus/knowledge`
  recursively; the sweep counts only the six part directories
  (`sweep.py:PARTS`). A stray `.md` directly under `corpus/knowledge/` (outside
  every part directory) is invisible to the sweep but trips COUNT: probe
  `edge-stray` printed `COUNT FAIL knowledge_files=230 required=229` with
  `SWEEP PASS exit=0 rows 229 files 229`. Nothing is missed, but the two legs are
  complementary, not redundant — both must be read.

## 5. Exactly which README edits `sweep.py` needs for the C landing

Read from `reports/round-28/readme/sweep.py` and measured one edit at a time
(probe trees `diag-*`; each was the (a) tree with exactly one edit reverted). Four
edits in `corpus/README.md`, all four required:

1. **Index row** — a row
   `- \`gesture-co-speech-pointing.md\` — <topic>` inside the `## linguistics/`
   section, whose topic text is **byte-equal** to the entry's own `- topic:`
   head-block text. `sweep.py:topic_of` reads the entry's topic block and
   space-joins its continuation lines, so a multi-line `- topic:` in the entry
   must be rendered as one line in the README (probe `edge-multiline`: a wrapped
   entry topic with a space-joined README row passes, `topic_mismatch 0`).
   Missing → `missing_from_index 1 ['linguistics/gesture-co-speech-pointing.md']`.
   Paraphrased → `topic_mismatch 1 [...]`.
2. **Section header** — `## linguistics/ (27)` → `## linguistics/ (28)`
   (`corpus/README.md:242`). Otherwise
   `header_drift {'linguistics': {'declared': 27, 'files': 28}}`.
3. **Totals line** — `Total knowledge entries: 228.` → `Total knowledge entries: 229.`
   (`corpus/README.md:614`). Otherwise `totals_line 228 totals_ok False`.
4. **Counts footer** — `(total 228 files; directory totals 27/26/28/29/24/94).` →
   `(total 229 files; directory totals 28/26/28/29/24/94).`
   (`corpus/README.md:618`, inside the `Counts checked 2026-10-22 from the repo
   root:` block). The six directory totals follow `sweep.py:PARTS` order —
   `linguistics, myth-symbol, culture-material, synthesis, verification,
   civilizations` — so linguistics is the first number. Otherwise
   `footer_findings [{"class": "FOOTER_TOTAL", ...}, {"class": "FOOTER_DIR_TOTALS", ...}]`.

With all four edits the direct sweep run is clean:
`rows 229 files 229 / missing_from_index 0 [] / topic_mismatch 0 [] /
orphan_rows 0 [] / header_drift {} / totals_line 229 totals_ok True /
footer_findings [] footer_ok True`, sweep exit 0.

Two lane conventions the acceptance does **not** measure but the corpus's own
checkers do:

- **Row order.** The index row's position is not checked by `sweep.py` (probe
  `edge-order`: the row placed at the end of the `## linguistics/` section still
  gives `SWEEP PASS`, exit 0). The lane convention is filename order, so
  `gesture-co-speech-pointing.md` goes between `historical-linguistics.md` and
  `kinship-terminology.md` (the current rows at `corpus/README.md:246` and `:247`).
- **Revision label.** `tools/check-readme-revisions.py` wants a `revision:` label
  for the landing. Probe `edge-rev` added a `revision: 3.0` block at the top of the
  README; the checker then reports `findings 0` with the same single pre-existing
  `REVISION-ORPHAN` warning as at base (an unheaded round-28 paragraph inside the
  revisions span, unrelated to this landing). `tools/check-readme-heading.py` also
  reports `findings 0`.

## 6. What the L1's landing must produce, in one list

1. `corpus/knowledge/linguistics/gesture-co-speech-pointing.md` — one file, with a
   `- topic:` head-block line (the sweep reads it; without it the row topic cannot
   match) and at least one `S\d{3}` at or above S187.
2. `corpus/SOURCES.md` — new registry row(s) `| S187 |` (and up) inside the
   `## Registry` table, appended after S186 (`:215`), each with exactly 11 pipe
   cells, `status` = `mined`, and `used-by` naming
   `corpus/knowledge/linguistics/gesture-co-speech-pointing.md`. Note the SOURCES
   contract says `mined` means "cited by the paths in `used-by`", so the row's
   status and the entry's citation must be written together.
3. `corpus/README.md` — the four edits of §5.

With those, `python3 -B reports/round-53/accept-c.py` exits 0 and prints four
PASS lines; any one of them missing prints the corresponding FAIL and exits 1.

## 7. Unrun checks and open items

- **Not run here:** the round-53 landing itself, `reports/round-53/dry-run.py`,
  `reports/round-53/claims-agree.py`, `tools/check-claim-separability.py`, and the
  D-side counter `reports/round-53/d-count.py`. Those belong to the integration
  wave; this seat was scoped to the C acceptance controls and to sandbox trees.
- **Not verified here:** that the S187+ ids the L1 assigns at integration are the
  right ones. The ids in this report are synthetic fixtures standing for "an id at
  or above S187"; the real id set is the L1's to assign.
- **Not verified here:** the content of any source behind S187+. No source was
  opened for this seat; the `| S187 |` row in the control trees is a synthetic
  fixture, not a reading receipt, and it does not appear in any lane file.
- The lane worktree at the time of writing already carries claim D landed
  (`374ae5a round-53: claim D — …`); the lane knowledge count is 228 and the
  gesture entry does not exist in the lane, so the (a) tree is not the lane state.

## 8. Files written

- This report: `.ufo/waves/round-53/build/ExecCAcceptanceControls.md`.
- Nothing else in the lane. All control trees, builder scripts and the transcript
  live under `/fast/scratch/hyaku/kotodama-r53/` (sandbox), outside the lane.
