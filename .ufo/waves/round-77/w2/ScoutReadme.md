# W2 falsification — ScoutReadme: README integration after the C target

Round 77, wave 2, attack-only. Target W1 artifact:
`.ufo/waves/round-77/w1/stage/ScoutReadmeIndex/readme-plan.md` (the "README
integration plan"), graded against the staged counter
`.ufo/waves/round-77/w1/stage/ExecAdaptC/accept-c.py` (INDEX leg at
`leg_index`, lines 1708–1906) and the surviving instrument
`reports/round-28/readme/sweep.py`. Base `211f9526800906e0c585d878d265c37e5e090c15`.
Probe transcript: `.ufo/waves/round-77/w2/stage/ScoutReadme/leg-index-probes.txt`
(fixture at `/fast/scratch/hyaku/kotodama-r77/ScoutReadme`, deleted before yield).

## Verdict

The plan's **diff shape is correct and counter-verified**: one index row inside
`## linguistics/`, heading `(32)` → `(33)`, one footer block appended at EOF.
Applying exactly that shape to a materialized base + the W1 draft entry passes
`leg_index` (`lands: PASS … 6 section(s), linguistics=33, last footer
total=254 vector=33/32/41/29/24/95`). But three named claims in the plan are
wrong, two of them load-bearing.

## Recalculated counts — CONFIRMED

`git ls-tree --name-only 211f95… corpus/knowledge/<d>/ | grep -c '\.md$'`:
linguistics 32, myth-symbol 32, culture-material 41, synthesis 29,
verification 24, civilizations 95; recursive total 253; zero `.md` files
outside the six partition dirs (`ls-tree -r` anti-grep: none); no partition
subdir nesting (linguistics depth-1 == recursive == 32). Post-landing (+1
linguistics file): **total 254, vector 33/32/41/29/24/95**, README section
order — matches the plan's footer verbatim. `sweep.py` run at base confirms
the same live vector: `footer_live {"total": 253, "dir_totals":
[32,32,41,29,24,95]}`, exit 0.

## FINDING 1 — the plan's "exact index row line" is STALE (will fail INDEX if copied)

readme-plan.md:29 prescribes the row body "two things the naming entry could
not say before. First, that a Chinese naming system is a *late cultural
acquisition* …" sourced to the STAGED file
(`shokuknow/merge/kotodama/.../naming-systems.amend-2026-10-23.md` lines
10–14, a `- topic:` folded across five lines, space-joined). Byte check:
`staged joined == plan row body: True` — the plan copied the staged file's
folded topic verbatim.

But claim C lands a REWRITE. The W1 draft
(`.ufo/waves/round-77/w1/drafts/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`
line 11) carries a different, single-line `- topic:` ("two things the base
entry could not say — that a Chinese naming system is a *late acquisition*…").
`draft topic == plan row body: False`. `leg_index` compares the row body to
`_entry_topic` of the LANDED file (accept-c.py:1760-1778). Fixture mutant
`m_plan-stale-row` (plan's literal row + draft entry): **LEG FAIL INDEX —
"index row is not the entry's `- topic:` text verbatim"**.

Correction for L1: derive the row body at land time from the landed file's
`- topic:` line — never from the plan's quoted text, and never from the staged
file. The plan's own prerequisite (topic folded to ONE physical line) already
holds in the draft (line 11 is 441 bytes on one line; `_entry_topic` reads
only the `topic:` line, continuation lines invisible).

## FINDING 2 — "sweep.py parses the FIRST footer" is FALSE (repaired in r75)

The plan (line 75-76) and the preserved README text (base L822-826) both say
`reports/round-28/readme/sweep.py` "still parses the first" footer, so its
totals legs "stay red". Both claims are inverted against the code:

- Base `sweep.py:113-118`: `matches = list(FOOTER_RE.finditer(text)); m =
  matches[-1]` — parses the **LAST** footer. History: at authoring (3b13a2f)
  it used `FOOTER_RE.search` (first); commit `012e8d3` ("round-75 … repaired
  last-footer sweep") flipped it to `matches[-1]` and loosened FOOTER_RE for
  single-line footers. The README sentence and the plan note predate/ignore
  that repair. The draft lesson (round-77.md:86,96) repeats the stale claim —
  it will fossilize the error if landed unedited.
- Empirical: `python3 reports/round-28/readme/sweep.py` at the base worktree
  → `footer {"date": "2026-10-27", "total": 253, "dir_totals":
  [32,32,41,29,24,95]}`, `footer_ok True`, `totals_line 253 totals_ok True`,
  **exit 0** — the legs are GREEN at base, not "already red". Selftest 14/14.

The real sweep limitation (invert of the stated one): sweep.py reads ONLY the
last `Counts checked` footer and the last `Total knowledge entries:` line;
superseded middle footers are invisible to it, and the counter's INDEX only
grades the last footer's numbers (older blocks are byte-preserved but
number-blind). So an inaccurate NEW footer WOULD fail sweep.py, and the dated
older footers keep their stale numbers by design — that is the convention:
footers are append-only dated records, superseded never corrected; each new
block names itself "the live reading" (base L822-826). Date field: neither
instrument grades it — INDEX ignores the date entirely (probes
`m_footer-old-date`, `m_footer-bad-datefmt`: PASS), sweep.py captures but
never compares it. Convention only: `Counts checked YYYY-MM-DD` = landing
date, 2026-10-27 as planned.

## FINDING 3 — heading `(32)`→`(33)` is REQUIRED; the draft lesson's "left as filed" fails

The plan correctly overrides round-73/74 doctrine: INDEX grades every `##
part/ (N)` heading against live `os.walk` counts (accept-c.py:1780-1785).
Mutant `m_stale-heading` (heading left `(32)`): **LEG FAIL INDEX —
"linguistics heading (32) != the 33 live .md files"**. The draft lesson
`w1/drafts/corpus/lessons/round-77.md:86` tells L1 the opposite — "`##
linguistics/ (32)` is named stale and left as filed — append-only" — and its
"Routed to the L1" item 3 leaves it open. If the lesson text ships as the
operational record, it documents a landing that INDEX must fail. The plan's
position (edit the parenthetical in place; only the count, line shape `##
linguistics/ (33)` matching `^## ([a-z-]+)/ \((\d+)\)\s*$`) is the verified
one; the exemption set covers the replaced heading line on both sides
(accept-c.py:1858-1860 added, :1874-1876 removed).

## FINDING 4 — COMBINED (Ca) needs the owned_inplace DICT record, not the skeleton's bare string

The in-place heading edit also walks through `accept-ca.py`'s COMBINED leg:
`leg_appendonly` diffs base..lands on every changed file; a changed README
line must sit in REPAIR `stated_at` lines or `c_exempt_lines`, the latter
populated only by `owned_inplace`/`readme_exemptions` records that are dicts
`{path, base_line|line, base_text, after_text}` (accept-ca.py:962-971,
2124-2135, 2646+). `claims-C.skeleton.json` freezes
`"owned_inplace": ["corpus/README.md"]` — a bare string, dropped by the
`isinstance(x, dict)` filter, leaving the heading change unexempted →
COMBINED red. The Ca selftest encodes exactly this ("readme-exemption-no-line"
expects `"carries no line number"`). Required frozen record: `{"path":
"corpus/README.md", "base_line": 344, "base_text": "## linguistics/ (32)",
"after_text": "## linguistics/ (33)"}` — the same line number exists in both
trees because the row insert lands at L356, after 344. The plan never names
this record; ScribeReport does ("the COMBINED README exemption carries its
required line number").

## Footer mechanics — verified behavior the plan under-specifies

Five base `Counts checked` blocks (counter-parsed: multi-line blocks at
L757-768, L800-801, L821-828, single-line L832, L836). `leg_index` requires
them preserved byte-identically AS A SUBSEQUENCE and the LAST lands block to
carry `(total 254 …; …totals 33/32/41/29/24/95)` — so the new block MUST be
the final `Counts checked` line in the file, and MUST start a new
blank-separated block (mutant `m_no-blank-v2`, merging `Total` into the old
block: FAIL "not preserved byte-identically"). Exemption geometry
(accept-c.py:1828-1844) tolerates ≥1 blank line before `Total` and a
contiguous `Total`+`Counts` block (mutant `m_no-blank-v3`: PASS); what fails
is a blank line between `Counts` and its continuation or any extra `## `/prose
line (mutant `m_trailing-section`: FAIL on three legs).

Measured escape hatches (counter-limitations, all PASS probes — plan does not
violate any, but L1 should know the leg is thinner than its leg text):
- `Total knowledge entries: 254.` line is ungraded by INDEX
  (`m_total-line-absent` PASS); only sweep.py's `TOTALS_RE`/`totals[-1]` and
  convention grade it — keep it.
- A non-blank line appended contiguously after the last `Counts checked` line
  is silently exempted (`m_junk-after-footer` PASS); a second `(total …)` clause
  after the true one is ignored — `README_FOOTER_RE.search` takes the FIRST
  match only (probe: `(was: total 999…)` + true clause → total 254).
- A row-shaped line for a BASE filename anywhere in the file is exempt and
  unpositioned (`m_ghost-row-base-file` PASS) — only adopted entries' rows are
  position-graded. Harmless here; do not rely on the leg to catch stray rows.
- Alphabetical row placement is convention, not graded: row must sit inside
  the linguistics section span (L344-heading to `## myth-symbol`), nothing
  finer. Plan slot (after `morphological-typology.md`, before
  `naming-systems.md`, L355/356) is correct; amend-before-base ordering
  matches the `worldbuilding-setting-practice.amend-…` precedent L451-452.
- Row-shape is brittle exactly as the plan warns: `- \`name.md\` — ` prefix
  with a literal em dash, topic verbatim, no trailing space
  (`m_row-trailing-space`: FAIL).

## Commands (evidence)

- `git -C <lane> ls-tree --name-only 211f95… corpus/knowledge/<d>/ | grep -c
  '\.md$'` → 32/32/41/29/24/95; `-r` total 253; anti-grep strays: none.
- `git show 211f95…:corpus/README.md` → 836 lines; `^## ` partition headings
  at 344/376/410/453/485/511; footer stack 755-836; `naming` rows 356/474/500.
- `python3 reports/round-28/readme/sweep.py` → exit 0 (output above);
  `--selftest` → 14/14.
- Fixture: `git archive 211f95…` materialized at scratch, plan diff applied,
  `importlib` load of `w1/stage/ExecAdaptC/accept-c.py`, `leg_index` against
  control + 15 mutants — full transcript in
  `w2/stage/ScoutReadme/leg-index-probes.txt`. Control `lands: PASS` at
  `required_sections` also satisfied (two appended SOURCES.md lines matched
  both frozen patterns in the earlier full-cfg run: `1 adopted row(s), 2
  required section(s)`).
- Topic provenance: space-join of staged file lines 10-14 == plan row body;
  `!=` draft entry line-11 topic.

## Remaining unknowns / for L1

- Frozen `claims.json` `owned_inplace` shape at freeze (dict vs bare string)
  — decides COMBINED, see Finding 4.
- Whether the landed entry's `- topic:` changes again before lands — the row
  must be re-derived at land time regardless.
- Ca's REPAIR pairs may not touch README line 344 (`_c_appended_line`);
  everything else in README is fair game for Ca but a REPAIR `stated_at` on
  344 is refused.

No installs (python3 3.x + git present; RULES.md read, pacman untouched).
Fixture scratch `/fast/scratch/hyaku/kotodama-r77/ScoutReadme` deleted.
