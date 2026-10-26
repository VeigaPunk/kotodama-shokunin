# ExecLegIndex — round-75 WAVE 2: claim-C `INDEX` leg (built + attacked)

Seat: `ExecLegIndex` (leaf executor, no delegation, no subagents, no background jobs).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, claim base `f556d1049fe651d3d63975600b13acd9fb686f15`.
Piece: `.ufo/waves/round-75/w2/parts/leg-index.py` — `leg_index`, `_readme_sections`,
`_footer_blocks`, `_entry_topic`, `_md_count` (the four template helpers keep their
contract-assigned names; my extra helpers are prefixed `_index_`).
Nothing else was written: no lane file, no fleet file, no claims/ledger edit, no counter edit, no
commit, no `git add`/`checkout`/`stash` — read-only `git show`/`git ls-tree`/`git diff` and one
`git clone --shared` into my own scratch. No tool was installed or upgraded (python3 stdlib +
git + tar sufficed; pacman not used).

**sha256 of my part file:**
`ac7848f35955c38f2c53a1fa08c6de5fc3608a4d82b07ce68424fbd009a66a07`

## 1. The leg text as read (frozen in `reports/round-75/claims.json`, claim C, `legs[-1]`)

> INDEX: corpus/README.md at `<lands>` has exactly one index row per adopted entry in the
> myth-symbol section, each entry's own `` - `topic:` `` text verbatim under the
> `` - `name.md` — `` prefix, the myth-symbol heading equals the live partition count (32), the
> last 'Counts checked' footer's total equals the live file count with the per-directory vector
> 32/32/40/29/24/95; every base footer block is preserved byte-identical and in order (the new
> footer is a new appended block); README lines changed, removed or added outside {the three
> adopted index rows, the myth-symbol heading, the appended footer block (`Total knowledge
> entries: N.` and its `Counts checked` paragraph), partition-heading lines whose only change is
> the count parenthetical (claim Ca's), index rows naming a knowledge file that exists at base
> (claim Ca's index-gap rows)} fail, and an added row-shaped `| S-id |` line fails

The **SHONEN.md:6 clause was removed from this leg by the L1 during this wave** (message at
16:53: SHONEN.md is claim Ca's, C never grades it). `leg_index` never reads SHONEN.md. The final
leg text (re-read at 16:5x) is the one quoted above, including the README diff-scope sentence and
the Ca index-gap-row exemption, which the earlier draft lacked and which I asked for (see §8).

## 2. What each clause compiles to

| clause | implementation |
|---|---|
| one index row per adopted entry, in the myth-symbol section | `README_ROW_RE` over every lands README line; per `cfg["entries"]` basename exactly one hit anywhere in the file, and that hit's 0-based line index inside `_readme_sections()`'s myth-symbol span |
| own `- topic:` text verbatim under the prefix | `_entry_topic(mat, path)` = first `- topic:` in the pre-`## ` header block, stripped; README body **not** stripped and compared with `==` |
| myth-symbol heading equals the live partition count | heading count from `README_SECTION_RE` vs `_md_count(mat, corpus/knowledge/myth-symbol)` |
| last footer total = live file count, vector 32/32/40/29/24/95 | `_footer_blocks()[-1]` → `README_FOOTER_RE`; total == `_md_count(mat, corpus/knowledge)`; vector == the frozen tuple **and** == the live per-partition counts in README section order; README must declare exactly six partitions |
| every base footer block preserved byte-identical and in order | the base footer-block sequence must be a prefix of the lands sequence |
| README lines changed/removed/added outside the set | ordered line embedding (no diff algorithm): greedy walk of base lines into lands lines; a base line must match unless it is a partition-count heading whose part still exists at lands; a lands line must match unless it is exempt |
| exemptions | (a) the last `Counts checked` block: that line, its paragraph to its last non-blank line, the `Total knowledge entries: N.` line and the blank separator(s); (b) partition rows-heading lines whose text occurs more often at lands than at base (count-parenthetical replacements); (c) row lines for an adopted entry basename or for a knowledge basename present at base, again only when their text is over-represented at lands |
| appended row-shaped `| S-id |` | `ROW_SHAPED_LINE_RE` on any over-represented lands line → explicit FAIL |
| ghost/inadmissible rows | any over-represented row line naming neither an adopted entry nor a knowledge file present at base → explicit FAIL |

No shared helper from `part-cfg.py` is called and none is redefined; the leg reads only
`ctx["mat"]`, `ctx["mat_base"]` and `cfg["entries"]` (`_index_*` private helpers only). No
network, no scratch, no subprocess.

## 3. Ambiguities and how I resolved them (also recorded in the part's header comment)

- **R1 live counts** — "live partition count" / "live file count" are counted from the graded
  tree (`mat`), never from README and never from the lane worktree.
- **R2 "exactly one"** — read as round 74 read the identical culture-material wording: one row
  for the basename anywhere in README (r74 `MutIndexLeg` M8 was killed by global uniqueness),
  and that row inside the myth-symbol section. A duplicate in a trailing block therefore reds
  (mutant M2).
- **R3 verbatim** — the README body is compared byte-for-byte (no `strip()`), so a trailing
  space on a row fails. This closes the r74 F2/M10 survivor, which r74's strip()-lenient compare
  let through.
- **R4 older footers** — every base footer block, in order (base sequence is a lands prefix).
  This closes r74 F1/M7b: the immediately-preceding live footer was exempt under r74's `[:-1]`
  loop; here rewriting the round-74 footer in place fails twice (older-footer compare and the
  embedding, mutant M14).
- **R5 appended footer block** — the last `Counts checked` line, its paragraph through the last
  non-blank line, and the `Total knowledge entries: N.` line with the blank separator(s) around
  it. The base file's own footers are multi-line paragraphs ending in prose, so the block's prose
  lines belong to it. Both drafted shapes pass (three-line variant A and one-line variant B —
  §5). An appended section heading or extra prose paragraph fails (mutant M12).
- **R6 vector** — six `## <part>/ (N)` partitions in README section order; the footer vector must
  equal the frozen `32/32/40/29/24/95` **and** the live per-partition counts. The live-vector
  half can only fire when the tree departs from the frozen partition plan, in which case the
  footer would be stating an untrue directory reading.
- **R7 no diff algorithm** — an ordered embedding walk instead of LCS/difflib. I first built an
  LCS, then a patience-anchored LCS; both mis-classified the README's repeated lines (the
  appended footer repeats the previous footer's closing `python3 -B …` / `counts markers …`
  lines, and the file is full of blank lines), reporting preserved lines as added, i.e. a false
  red on the true landing. The embedding walk has no such ambiguity, and it still rejects
  rewrites, moves and deletions.
- **Ca lands first** — the L1 stated claim Ca lands before claim C, so C's tree carries Ca's four
  index-gap rows and the `## linguistics/` and `## culture-material/` heading repairs; the frozen
  leg exempts both. The row exemption is "over-represented text naming a base knowledge file",
  not "naming a base file", because Ca's four rows are byte-identical to the round-73 block's
  rows (ScribeReadmeIndex F4) and a plain name test would have made the *preserved* rows
  skippable, desynchronising the walk.
- **SHONEN.md:6** — dropped by the L1 mid-wave; not implemented, not read.

## 4. Test setup (real execution, my scratch only)

`S=/fast/scratch/hyaku/kotodama-r75/ExecLegIndex` (deleted before yield).

1. `git clone --quiet --shared <lane> $S/mock`; `git rev-parse --show-toplevel` = `$S/mock`;
   `git checkout --detach f556d104…`. Clone, not a worktree, so the lane's index is untouched.
2. Copied the three UNLANDED entry drafts to `corpus/knowledge/myth-symbol/`
   (`narrative-structure-frameworks{,.amend-2026-10-23,.amend-2026-10-23b}.md`) → 252 `.md` files,
   myth-symbol 32.
3. README landing **as claim C's tree will carry it after Ca**: three myth-symbol rows derived
   mechanically from the landed entries' own first `- topic:` lines (never hand-typed), inserted
   after the `myth-ritual-theories.md` row; `## myth-symbol/ (29)` → `(32)`; Ca's two heading
   repairs `(30)`→`(32)` / `(36)`→`(40)`; Ca's four index-gap rows in their sections (topics
   derived from the base entries); appended `Total knowledge entries: 252.` + a `Counts checked
   2026-10-27 … (total 252 files; directory totals 32/32/40/29/24/95).` paragraph ending with the
   same two closing lines the base footer uses.
   The nine registry rows and the probe captures were **not** needed: this leg reads no registry
   row, no evidence file and no lesson (it grades README + the knowledge tree + the entries'
   topic lines only).
4. Committed in the mock (fixture identity via `-c user.name/-c user.email` on the one commit),
   lands `ca2c3e6426aba9b52d2f5e9fc5961ee85a4688f2`; `mat` = `git archive <lands> | tar -x`,
   `mat_base` = `git archive f556d10 | tar -x`.
5. Harness execs PART-A (lines 1-509 of the fixed counter, split at `# --- PART B ---`) and my
   part into one namespace and calls `leg_index` with a hand-built ctx: `root`, `lands`, `mat`,
   `mat_base`, `cfg={"entries":[3 paths]}`, `fleet_root`, `scratch`. `part-cfg.py` was not used —
   this leg consumes only `cfg["entries"]`; the hand-built cfg is a faithful subset of the contract
   dict. `python3 -B -m py_compile` on PART-A + my part: rc 0; both files contain no top-level
   code other than definitions.

## 5. Positive and mutant table (all executed)

`POSITIVE` = the full claim-C landing above. Each mutant is that tree with one byte-level change
(same `mat_base`); `DO-NOTHING` = `mat == mat_base`.

| # | tree | expected | got | INDEX's first reason (verbatim, truncated) |
|---|---|---|---|---|
| 0 | POSITIVE (Ca-then-C landing) | PASS | **PASS** | `6 section(s), myth-symbol=32, last footer total=252 vector=32/32/40/29/24/95, 3 adopted row(s), 822 base / 838 lands line(s), 21 exempt line(s)` |
| 1 | M1 wrong topic (body gets a leading `the `) | FAIL | FAIL | `narrative-structure-frameworks.md index row is not the entry's `- topic:` text verbatim` |
| 2 | M2 duplicate row (second copy of the amend row) | FAIL | FAIL | `narrative-structure-frameworks.amend-2026-10-23.md has 2 index rows in corpus/README.md (want exactly one)` |
| 3 | M3 stale heading (`(32)`→`(29)`) | FAIL | FAIL | `myth-symbol heading (29) != the 32 live .md files in corpus/knowledge/myth-symbol` |
| 4 | M4 footer total `252`→`251` | FAIL | FAIL | `last footer total 251 != the 252 .md files at lands` |
| 5 | M5 older footer edited (round-74 `(total 249 …)`→`248`) | FAIL | FAIL | `an older `Counts checked` footer is not preserved byte-identically: 'Counts checked 2026-10-25 from the repo root: `find corpus/k'` |
| 6 | M6 unrelated line edited (a linguistics row's text) | FAIL | FAIL | `README line 374 removed/edited outside the exemption set: '- `writing-systems.md` — Script typology …'` |
| 7 | M7 added `\| S885 \| … \|` row-shaped line in the myth section | FAIL | FAIL | `README line 400 is a row-shaped registry line (this file never asserts registry rows): '\| S885 \| Barthes \| …'` |
| 8 | M8 amend row moved into `## culture-material/` | FAIL | FAIL | `narrative-structure-frameworks.amend-2026-10-23.md index row is not inside the myth-symbol section` |
| 9 | M9 trailing space on the base entry's row | FAIL | FAIL | `narrative-structure-frameworks.md index row is not the entry's `- topic:` text verbatim` |
| 10 | M10 vector swapped `32/32/…`→`29/32/…` | FAIL | FAIL | `last footer vector 29/32/40/29/24/95 != the frozen 32/32/40/29/24/95` |
| 11 | M11 ghost row (`narrative-structure-frameworks-ghost.md`) | FAIL | FAIL | `README line 400 adds an index row for 'narrative-structure-frameworks-ghost.md', which is neither a frozen adopted entry nor a knowledge file existing at base` |
| 12 | M12 drafted-style `## Round 75 landing …` heading + prose before the footer | FAIL | FAIL | `README line 831 added outside the exemption set: '## Round 75 landing (appended 2026-10-27, hyaku run 10)'` |
| 13 | M13 unrelated README line deleted | FAIL | FAIL | `README line 764 removed/edited outside the exemption set: 'Index rows checked 2026-10-17 by the round-10 R10-C21 sweep (189 rows vs 189'` |
| 14 | M14 round-74 footer rewritten in place (closes r74 F1/M7b) | FAIL | FAIL | `an older `Counts checked` footer is not preserved byte-identically …; README line 815 removed/edited outside the exemption set` |
| 15 | DO-NOTHING `mat == mat_base` (base lands) | FAIL | FAIL | `corpus/knowledge/myth-symbol/narrative-structure-frameworks.md has no non-empty `- topic:` header line; … has 0 index rows (want exactly one); …` |
| 16 | POSITIVE variant B (one-line footer, no `Total knowledge entries:` line) | PASS | **PASS** | `6 section(s), myth-symbol=32, last footer total=252 vector=32/32/40/29/24/95, 3 adopted row(s), 822 base / 831 lands line(s), 14 exempt line(s)` |

`MISMATCHES 0` across the table (the driver compares want vs got). The same tree also reds at
`lands == <freeze>` (entries absent → `_entry_topic` None, zero rows), which is the do-nothing
control the claim names for FROZENCFG-green/data-red.

Mutants 1-15 each violate a distinct sentence of the frozen leg text except M13 (an edit to
unrelated prose) and M14 (the footer-preservation sentence), which test the diff-scope and R4.

## 6. What this leg does **not** grade (limits, so nobody over-reads a PASS)

- **`Total knowledge entries: N.`** is exempt as part of the appended block but its number is not
  checked by the wording (only the last `Counts checked` footer's total and vector are). A landing
  whose totals line is wrong beside a correct footer would pass INDEX. Cheap pre-freeze fix if the
  L1 wants it: one sentence in the leg text.
- **Non-adopted rows that name a base knowledge file** (the Ca exemption) are not otherwise
  graded here — a Ca row placed in the wrong section passes INDEX; Ca's own legs own that.
- **Row order** inside the myth-symbol section is unconstrained (same as r74 `MutIndexLeg` F3;
  the wording imposes no order).
- **Topic shape**: the leg takes the *first* pre-body `- topic:` value, single physical line,
  stripped. The three landed drafts carry single-line topics (906 / 359 / … characters) and the
  base entry's second `- topic:` sits in its Part-2 block after a `## ` heading, so it is never
  reached; a landing that folds the topic over several lines would have to fold the README body
  identically, and this leg does not fold. Drafts satisfy it.
- **Bare/absolute URL checks, evidence, Gate, registry** belong to the sibling legs; INDEX reads
  none of them.

## 7. Coordination

One message to `KotodamaR75a2` (L1) with the three interface points found while building:
(1) the frozen leg text then lacked the README diff scope my seat spec and PART-A H4 required;
(2) the staged landing appended a `## Round 75 landing …` heading + prose, which the scope clause
rejects — the L1 answered that C's landing is rows + heading + footer only and told the scribe to
drop the block; (3) "older footers byte-identical" is enforced over every base footer block
(prefix semantics), closing r74 F1. The L1's answer also added the Ca index-gap-row exemption and
removed the SHONEN clause; the part implements the resulting text. No other peer was contacted;
no `agent://all`.

## 8. Files, evidence, cleanup

- Written: `.ufo/waves/round-75/w2/parts/leg-index.py`
  (`sha256 ac7848f35955c38f2c53a1fa08c6de5fc3608a4d82b07ce68424fbd009a66a07`, 312 lines,
  definitions only, `py_compile` clean when concatenated with PART A) and this report.
- Retained evidence: the table in §5 is the run output; the mock lands revision
  `ca2c3e6426aba9b52d2f5e9fc5961ee85a4688f2`, base `f556d1049fe651d3d63975600b13acd9fb686f15`,
  and the measured positive detail string in row 0 (822 base / 838 lands lines, 21 exempt,
  total 252, vector 32/32/40/29/24/95).
- Scratch `$S` (mock clone, materialized trees, mutants, harness, compiled assembly) deleted
  before yield; nothing under `/tmp` is cited.
