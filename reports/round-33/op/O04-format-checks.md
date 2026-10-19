- Seat: O04 | executor | claim O | date 2026-10-19 | baseline 139e3b6

# O04 — format-class verification of the seven round-26..32 lessons (C33 leg)

Mission: classify each of the 7 unindexed lesson files per `corpus/lessons/README.md` §3
taxonomy from live bytes, flag any class outside the documented three, and check the
round-25 audit tool's selftest still covers the classes present.

## 0. Method — the tool's own classifier, not a re-implementation

`classify()` and `contract_lines()` were loaded from the filed tool by path and called
on the live file texts (`importlib.util.spec_from_file_location` over
`reports/round-25/audit/c31-lessons-index-audit.py`), so the class labels below are the
labels the C31/C33 census itself will report — no second classifier to disagree with it.

Baseline reproduced at the round-33 tree before any measurement:

```
$ git rev-parse HEAD            -> 139e3b662900557afe54f632b468619593dc9fcb
$ git ls-files | wc -l          -> 2655
$ python3 -B reports/round-25/audit/c31-lessons-index-audit.py            -> exit 1
  lesson files: 33 / index rows: 26 / formats {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}
  FAIL C31_index_rows_eq_files ; PASS C32 ; PASS C33_formats_documented ; PASS C34 ; PASS C34c ; FAIL C34b
  findings: 2 — C31-1 unindexed-file ['round-26.md'..'round-32.md'] ; C34-2 prose-arithmetic-drift {stated [26,26], measured [26,33]}
$ python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest -> exit 0, SELFTEST OK: 28/28
```

## 1. Classification of the 7 files (live bytes, tool's classifier)

| file | class | `## Gate` at | `### Rule` | contract | bytes | lines | sha8 |
|---|---|---|---|---|---|---|---|
| `corpus/lessons/round-26.md` | gate-keeper | :11 | :15 | 4/4 | 60054 | 222 | cae06660 |
| `corpus/lessons/round-27.md` | gate-keeper | :11 | :15 | 4/4 | 54972 | 203 | f15e285b |
| `corpus/lessons/round-28.md` | gate-keeper | :11 | :15 | 4/4 | 50419 | 145 | dd832ff7 |
| `corpus/lessons/round-29.md` | gate-keeper | :9 | :13 | **3/4** | 17847 | 118 | b6765d33 |
| `corpus/lessons/round-30.md` | gate-keeper | :9 | :13 | **3/4** | 30665 | 181 | 56e77835 |
| `corpus/lessons/round-31.md` | gate-keeper | :11 | :15 | 4/4 | 16637 | 73 | 8870bbdd |
| `corpus/lessons/round-32.md` | gate-keeper | :11 | :15 | 4/4 | 12879 | 66 | 8aacfc2b |

- **7/7 gate-keeper.** Every one carries an exact `## Gate` line (`^## Gate$`) and none
  carries `## Fragment index` — measured, not inferred: `gate_exact=True, frag_exact=False`
  for all seven.
- **Rounds 29 and 30 are 3/4**: their contract set is `source:`, `verified-at:`, `scope:`
  — **`recheck:` is absent** from the live bytes. They join round 16 as the partition's
  only no-`recheck:` files. The other five are 4/4.
- `bytes`/`lines`/`sha8` are measured here for the class leg only. The §2 row **pin** cells
  are another seat's leg — re-measure before writing them; do not inherit this column.

## 2. Answer: no class outside the documented three

Partition histogram after the seven files, measured over all 33 `*.md` files:
**gate-keeper 21 / fragment-index 5 / plain 7 = 33**. Classes present = the three
documented in §3 (`corpus/lessons/README.md:111-142`). Zero files fall outside them, so
the C33 "documented formats" condition is satisfiable by the current taxonomy with no
fourth class invented.

Checks that back the "no fourth class" claim, run over the whole partition:

- All 5 fragment-index files (rounds 8–12) carry an exact `## Gate` as well, so §3's
  definition ("the gate-keeper survey **plus** a `## Fragment index` section") holds for
  every live instance of that class — no counter-example.
- **Zero fence false-positives**: no exact `## Gate` / `## Fragment index` line in any of
  the 33 files sits inside a fenced code block (probe over all 33: 0 hits). The
  classifier's line-anchored regex therefore has no live misread on this partition.

### Named finding F1 — §3's sub-shape sentence does not name the H2 variant

The seven files are gate-keeper in **two** sub-shapes, measured by heading level:

| sub-shape | files | per-axis sections | `### Rule` line |
|---|---|---|---|
| `### Rule` + **H3** per-axis sections | rounds 21–23 (3/3/2), 25, **26, 27, 28** (3/3/3) | `^### [DOCA] — ` | `:15` / `:15` / `:15` |
| `### Rule` + **H2** per-axis sections | **rounds 29, 30, 31, 32** (3/3/3/1) | `^## [DOCA] — ` | `:13` / `:13` / `:15` / `:15` |

Two measurements sharpen what is actually new, against a tempting over-read:

- The per-axis heading form itself is **not** new. H3 per-axis sections (`^### [DOCA] — `)
  occur in 17 files, including the older gate-keepers rounds 14 (3), 15 (2), 17–19 (3 each)
  and 20 (6). The discriminator for §3's "newer shape" is the `### Rule` heading, which
  occurs in exactly **11** files: rounds 21–23, 25, 26, 27, 28, 29, 30, 31, 32.
- The **H2** per-axis form (`^## [DOCA] — `) occurs in **only four files in the whole
  partition — rounds 29, 30, 31, 32** — so it is genuinely new at round 29, introduced by
  this batch of seven.

§3 (README:119-122) describes only "rounds 21–23 carry the newer `### Rule` +
per-axis-section shape" — it does not distinguish the heading level, and rounds 29–32
introduce the H2 form (`round-29.md:17`, `round-30.md:17`, `round-31.md:19`,
`round-32.md:19`). This is a **documentation** gap, not a class violation: both variants
classify `gate-keeper` (verified by running the tool's `classify()` over minimal probes of
both sub-shapes → `gate-keeper`, see §4).

Marker vocabulary, measured on the same bytes: `Opening <axis> reading:` occurs **0 times**
in all seven files, and no file carries an `Admitted`/`Rejected` line — so §3's "with no
marker vocabulary" holds for the seven in the marker sense. Substring residues exist and
must not be miscounted as markers: `spot-check` ×4 in round-26 (`round-26.md:29`, `:155`,
`:168` — prose about spot-checks), `**Opening status:**` at `round-30.md:107` and
`round-31.md:62`, and "Opening readings only" at `round-32.md:51`.

## 3. Selftest coverage of the classes present

Classes present = 3. Selftest class controls = 4, and they cover all three plus the
precedence rule and the prose negative (`--selftest`, exit 0, 28/28):

| control (selftest label) | covers |
|---|---|
| `gate-keeper class` | gate-keeper |
| `fragment-index wins over gate-keeper` | fragment-index **and** its precedence over gate-keeper |
| `plain class` | plain |
| `prose Gate heading is not a gate section` | the `^## Gate$` anchor's tail (`## Gate candidates` must stay plain) |

Verdict: **the selftest still covers every class present.** Three named coverage limits,
each with an executable probe (tool's `classify()` called on minimal strings):

1. `# X\n## Fragment index\n` (no `## Gate`) → `fragment-index`, although §3 defines the
   class as gate-keeper **plus** that section. No live instance today (all 5 carry
   `## Gate`), so this is a latent misread, not a present defect.
2. `# X\n\`\`\`\n## Gate\n\`\`\`\n` → `gate-keeper`: a fenced marker would be counted. Zero
   live instances (§2), so latent only.
3. No control for the `### Rule` / per-axis sub-shapes that 11 live files now carry (rounds
   21–23, 25–32); both probe forms classify `gate-keeper` correctly, so the behaviour is
   right — the control is simply absent. The selftest is also entirely synthetic: it
   contains no live-file control.

### Named finding F2 — C33 cannot catch a stale histogram; this census is that measurement

The tool's C33 leg is a **substring** check, not a count: it declares a format documented
if its name appears anywhere in the README text
(`reports/round-25/audit/c31-lessons-index-audit.py:229-235`,
`if name in idx["text"]`), then tests `live_formats.issubset(declared_formats)`. It
therefore passes while §3's histograms say gate-keeper **14** and the measurement says
**21**. The only arithmetic C34b re-derives is two regex surfaces — `Rows: **N**`
(tool:297-298) and `**Rows: N. Files: M.**` (tool:299-300) — so §3's class counts and its
contract-line sentence are **hand-verified surfaces**. The numbers in §5 are that
hand-measurement, supplied so the integrator's §3 revision is not written from the stale
prose.

## 4. Measured facts the §2 row edit must satisfy (C34c re-derives both cells)

C34c compares `cells[1]` (format) and `cells[2]` (contract) against the live measurement
(tool:272-288). For the seven new rows the required cells are:

| row file | `format` cell | `contract` cell |
|---|---|---|
| `round-26.md`, `round-27.md`, `round-28.md`, `round-31.md`, `round-32.md` | `gate-keeper` | `4/4` |
| `round-29.md`, `round-30.md` | `gate-keeper` | `3/4` |

Cross-check against the sibling fragments that landed while this seat ran (independent
measurements, not inheritance):

- `reports/round-33/op/K02-lessons-census.md:82-90` derives the same class for all seven
  files with the same `## Gate` / `### Rule` line numbers (`:11`/`:15` ×5, `:9`/`:13` ×2),
  and its §4 contract table agrees cell-for-cell. Independent agreement on the C34c cells.
- `reports/round-33/op/O01-row-drafts.md:55-61` drafts the rows with exactly these cells
  (`gate-keeper`; `4/4` ×5, `3/4` ×2) — three separate measurements, one answer.
- Neither sibling records the **H2 vs H3** per-axis split (§2 F1): K02's table keys only on
  `### Rule`, so the one thing rounds 29–32 introduce partition-wide is invisible to it.

Integration hazard, cited from the tool rather than guessed: C34b reads the **first**
`Rows: **N**` match in the file (`stated.setdefault("queue", []).append(...)`, then
`stated["queue"][0]`, tool:297-298 and 303-305). Any new `Rows: **N**` line placed above
§4's queue-arithmetic line would shadow the queue count and turn C34b red for the wrong
reason. C34b's table regex additionally requires the exact shape
`**Rows: <n>. Files: <n>.**` (README:97 currently states 26/26; the C-claim's target is
33/33) — the class numbers in §5 must not be written in either of those two shapes.

## 5. Draft §3 text for the integrator (draft only — this seat writes no shared file)

Before → after, with the measured counts. Nothing below was applied; the lessons README is
the integrator's edit surface.

1. `corpus/lessons/README.md:118` — `**14 files.**` → `**21 files.**`
2. `corpus/lessons/README.md:120-122` — append to the sub-shape sentence: rounds 21–23 and
   25–28 carry the `### Rule` + H3 per-axis-section shape; rounds 29–32 carry the
   `### Rule` + H2 per-axis-section shape; no file in rounds 26–32 carries the
   `Opening <axis> reading:` form or `Admitted`/`Rejected` lines (measured 0/7).
3. `corpus/lessons/README.md:134-137` — `**rounds 17–23 carry 4/4**` → `**rounds 17–23,
   25–28 and 31–32 carry 4/4**` (13 files); the 3/4 enumeration gains **rounds 29, 30**
   (15 files). Round 16's outlier sentence (README:140-142) should name rounds 29 and 30 as
   the other no-`recheck:` files — inside the gate-keeper class, unlike round 16.
4. `corpus/lessons/README.md:138-140` — histogram arithmetic: `gate-keeper **14** = the 13
   filed plus the round-25 lesson` → `gate-keeper **21** = the 13 filed plus the round-25
   lesson plus rounds 26–32`; `Total 26 = the runner's file set` → `Total 33`.

Measured partition-wide contract histogram backing item 3: 0/4 = 5 files (README + rounds
1–4), 3/4 = 15 files, 4/4 = 13 files.

## 6. Boundary

Read-only leg. Files opened: the 33 `corpus/lessons/*.md` files and the filed round-25
tool (imported, not modified). No write outside `reports/round-33/op/O04-format-checks.md`;
no shared file edited; no commit, no push, no install, no network. No filed round byte
touched.

## Owed

- none. The class leg is complete on the current tree; §5's drafts are for the integrator.
- Re-measure trigger: any later write to `corpus/lessons/README.md` or to a
  `corpus/lessons/round-*.md` byte invalidates §1/§2/§5 counts — they bind to the stamps in
  §0 (baseline `139e3b6`, worktree as measured 2026-10-19).

## Citations

- `reports/round-33/targets.json` — O04 seat object (`mission`, `out`), `shared_rules`.
- `reports/round-33/claims.json:19-37` — claim O, lessons leg, counting commands, thresholds.
- `reports/round-33/op/K02-lessons-census.md:82-90` (class table), `:105-115` (contract table) — sibling independent measurement, cross-checked in §4.
- `reports/round-33/op/O01-row-drafts.md:55-61` — drafted §2 rows; format/contract cells agree with §4.
- `corpus/lessons/README.md:111-142` — §3 the three census formats, histograms, contract-line sentence; `:97` — `Rows: 26. Files: 26.`
- `reports/round-25/audit/c31-lessons-index-audit.py:47-54` — `FORMAT_MARKERS`; `:72-78` — `classify()`; `:81-89` — `contract_lines()`; `:229-243` — C33 substring check; `:272-288` — C34c shape-cell re-derivation; `:293-317` — C34b prose arithmetic; `:337-432` — selftest controls.
- Commands (all with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, cwd repo root):
  - `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` → exit 0, `SELFTEST OK: 28/28`
  - `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 1, findings C31-1 (7 files) + C34-2 `{stated [26,26], measured [26,33]}`, C33 PASS
  - `git rev-parse HEAD` → `139e3b662900557afe54f632b468619593dc9fcb`; `git ls-files | wc -l` → 2655
  - inline `python3 -B -c` probes (this fragment §1/§2/§3/§4): tool `classify()`/`contract_lines()` over the 7 files and over all 33 files; heading-level and marker-vocabulary scans; fence scan; 12 synthetic classify() probes.
- File:line for the seven (from the heading scan): `round-26.md:11,15,19,84,124`; `round-27.md:11,15,19,90,127`; `round-28.md:11,15,19,52,62`; `round-29.md:9,13,17,85,93`; `round-30.md:9,13,17,83,91`; `round-31.md:11,15,19,34,40`; `round-32.md:11,15,19`.
