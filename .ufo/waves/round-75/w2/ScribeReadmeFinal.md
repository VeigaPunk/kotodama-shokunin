# ScribeReadmeFinal — round 75 (hyaku run 10), wave 2

Seat: `ScribeReadmeFinal` (leaf scribe). Lane `kotodama-shokunin`, base
`f556d1049fe651d3d63975600b13acd9fb686f15`. No product byte, no counter, no claim and no
ledger entry was edited. Three stage files are written; the L1 lands them.

Task: stage `corpus/README.md` for both claims as three separate files so each claim lands on
its own, prove the README sweep red-before → green-after, and report every README line the two
claims both touch.

Final scope is the L1's second wave-2 ruling (`KotodamaR75a2`, 2026-10-27, superseding an
earlier 4-row instruction): claim C = the three myth-symbol index rows + the
`## myth-symbol/ (32)` heading line + a `Total knowledge entries: 252.` / `Counts checked
2026-10-27` footer, nothing else; claim Ca = the two heading parentheticals + **two** heritage
index rows (the `conlang-scholarship*` rows already sit in the dated round-73 block at
`README.md:787-788`). Ca lands first, then C.

---

## 1. Deliverables

| file (under `.ufo/waves/round-75/w2/stage/corpus/`) | bytes | lines | sha256 |
|---|---|---|---|
| `README.md.c-rows` | 2164 | 3 | `44098e3745311163b22527b88a024224a17712a988bede4febe186e89a0bd684` |
| `README.md.c-footer` | 186 | 4 | `d48ae4cda2afaa050dea42840aee64b0ba3f4f58c2e7940ec5b5c2225bf6743f` |
| `README.md.ca-edits` | 2291 | 40 | `e3fa4f8d4c5f12b704c26c6c24e955c617b7ac2c82fa8566e3e1ab423a5294dd` |

Applied in order Ca → C to `git show f556d1:corpus/README.md`, the three files produce a
README of `sha256 fe352307d7f11a67c5a247fe9736f7b92032f61d4d910af940b608e283fc1229`
(831 newlines vs 822 at base; 3 lines replaced, 5 rows inserted, 4 footer lines appended).
No CRLF, no tabs in any of the three files.

### 1.1 `README.md.c-rows` — claim C, exactly 3 rows, filename order

Insert immediately after the single line beginning `` - `myth-ritual-theories.md` — `` (base
line 396, between `myth-ritual-theories.md` and `number-symbolism.md`). The section is
byte-alphabetical and the three names sort `.amend-2026-10-23.md` < `.amend-2026-10-23b.md` <
`.md` (checked with `sorted()`; stable).

```
- `narrative-structure-frameworks.amend-2026-10-23.md` — how three articles of *Communications* 8 (1966) describe a narrative — Todorov's three categories and the temporal deformation that separates discourse from history, Greimas's message readable on two isotopies at once, and Barthes's hierarchy of levels with its horizontal and vertical readings — read in the French original from the page-level transcription.
- `narrative-structure-frameworks.amend-2026-10-23b.md` — where Barthes's five codes sit — the five codes in the S/Z reading sheet's own French names (herméneutique, sémique, symbolique, proaïrétique, gnomique); a semiotician's statement that they are in part a reformulation of the levels of the 1966 Introduction, with the proairetic code a synthesis of two of those levels; and the 1966 article's own hierarchy of levels of description on the one page this file can quote — with the attribution table and the design orders that follow from it, as method, not canon.
- `narrative-structure-frameworks.md` — how narrative structure is theorised and specified as a build order for an invented culture — the structuralist premise that narrative is a formal object analysed by levels of description, carried by one Western row at the scope the Gate locates, beside the Chinese and Japanese half that is not a translation of that canon: the story/discourse split (故事 as deep structure, 话语 as surface presentation), the actantial model (行动元), the three time axes (次序, 时长, 频率), focalisation and the levels-and-voices problem (查特曼's participant grid), 起承転結 held as a completable minimal unit rather than a four-beat plot, a three-layer machine-writable description format (ストーリー, クエスト, シーン, with キャラクター as a hierarchical sub-layer), the Japanese …
```

**Row text is the staged entries' own `- topic:` block, not the w1 drafts.** All three entries
are now staged under `stage/corpus/knowledge/myth-symbol/` and **all three staged files differ
from the drafts** (`sha256`: base `f01fffcb…` vs draft `7e35ee99…`; amend-23 `6a19161b…` vs
`b07a9eb5…`; amend-23b `fa1c43c3…` vs `d03eff4d…`). Rows were re-bound to the staged bytes
after each staged file appeared: topic lengths **400 / 510 / 978** characters, one `- topic:`
match per file. The draft topics (359 / 906 / 278) and the w1 draft's 892-char variant are
superseded and must not be restored. Because `.amend-2026-10-23b.md` is in the frozen `entries`
list (`claims.json`), N = 3 → heading `(32)`, total 252, vector `32/32/40/29/24/95`; the w1
draft's N=2 arithmetic (251 / `(31)`) is superseded.

### 1.2 `README.md.c-footer` — claim C, appended at EOF

Base ends at `…counts markers, not verified facts.\n` (line 822). The file's bytes are appended
verbatim; the first byte is the single blank separator line.

```

Total knowledge entries: 252.

Counts checked 2026-10-27 from the repo root: `find corpus/knowledge -type f -name '*.md' | wc -l` (total 252 files; directory totals 32/32/40/29/24/95).
```

The `Counts checked` paragraph is the round-74 footer grammar verbatim (date, the backtick
`find … | wc -l` command, `(total N files; directory totals a/b/c/d/e/f).` on one line), and it
measures as live: the instrument parses it as the last block and grades it equal to the tree
(§3). Vector derived by partition: base `find corpus/knowledge -name '*.md'` per directory =
32 / 29 / 40 / 29 / 24 / 95 (249); myth-symbol +3 = 32; total 252; order is the instrument's
`PARTS`. No row-shaped line (`^- \`[^`]+\.md\` — ` matches 0 times), so supplemental row
attribution adds no phantom row, and no `## ` heading is added, so the H2 count is unchanged
(9, measured by `tools/check-readme-heading.py`) and the diff-scope ruling holds.

### 1.3 `README.md.ca-edits` — claim Ca: 2 heading replacements + 2 rows

Line-oriented apply spec: `#` lines are comments; each record opens with `LINE-REPLACE` or
`INSERT-AFTER`, carries verbatim payload, and closes with `END`.

| # | kind | old line / anchor (base) | payload |
|---|---|---|---|
| 1 | `LINE-REPLACE` | `## linguistics/ (30)` (line 344) | `## linguistics/ (32)` |
| 2 | `LINE-REPLACE` | `## culture-material/ (36)` (line 407) | `## culture-material/ (40)` |
| 3 | `INSERT-AFTER` | `` - `headgear-head-covering-codes.md` — `` (line 428) | 2 culture-material rows |

Every old line and anchor occurs exactly once in the base blob (checked before applying). Row
text is each file's own base-blob `- topic:` block folded by `sweep.py:topic_of()` (130 and 369
chars), inserted between `headgear-head-covering-codes.md` and
`hunting-foraging-subsistence.md` — byte-alphabetical. The two `conlang-scholarship*` files are
deliberately given no second row (see §5.1).

---

## 2. The instrument used, and why not the draft

Measurement instrument: **the worktree copy**
`reports/round-28/readme/sweep.py`, `sha256
7e0566ad1ae8ec2c5a0f10c62dc8de66abcc180ec3f7af560bceeba1601cad2b`, mtime 2026-10-27 15:11,
`python3 -m py_compile` **OK** — used on the L1's explicit instruction ("Sweep source: the
compiling file is the WORKTREE copy … drafts/sweep-fixed.py is a stale broken copy"). It is
uncommitted at this seat's start, and the seat rules say uncommitted worktree edits are not
graded; it is the measurement source here only because the L1 named it, and it must be committed
as part of Ca's landing for the L75-04 receipt to rest on committed bytes.

`.ufo/waves/round-75/drafts/sweep-fixed.py` (`sha256
6bf975a069d02aee0a10bdc06defb75a5ecc4167d9f24656b1c39aa8f4bd6399`) **does not compile**:

```
$ python3 -m py_compile .ufo/waves/round-75/drafts/sweep-fixed.py
  File ".../sweep-fixed.py", line 170
    for f in sorted(fileset - seen):
IndentationError: unexpected indent
```

The two `ghosts.extend("unassigned/…")` lines were inserted at 4-space indent inside the
`for part in sorted(sections):` body. I verified semantic equivalence of the worktree copy to a
minimal repair of the draft (same `SECTION` boundary rule, same last-footer/last-totals reads,
same supplemental attribution; differences are comments, formatting and selftest message text),
so the numbers below are the worktree instrument's own readings and agree with the repaired
draft's.

The committed base instrument (`f556d1`, `sha256 9b2ccac0…`) is retained for the red-before
half (§3.1).

---

## 3. Measurements

Method: for each state, `git -C <lane> archive f556d1 | tar -x -C $T`; the instrument copied to
`$T/reports/round-28/readme/sweep.py` (and the committed base instrument to
`$T/reports/round-28/readme/sweep-base.py`); the stage files applied to `$T/corpus/README.md` by
anchor; entry files copied from `stage/corpus/knowledge/myth-symbol/` (staged bytes, not drafts)
for the C states. Every tree is rebuilt from the stage files alone. Scratch trees under
`/fast/scratch/hyaku/kotodama-r75/ScribeReadmeFinal/` (deleted before yield).

| state | exit | rows / files | missing | mismatch | ghosts | drift | totals | footer | `--selftest` |
|---|---|---|---|---|---|---|---|---|---|
| base `f556d1` | **1** | 247 / 249 | 2 heritage | 0 | 0 | linguistics 30/32, culture-material 36/40 | 249 ok | r74 block ok | FAIL (live leg) |
| Ca only (2 headings + 2 rows) | **0** | 249 / 249 | 0 | 0 | 0 | {} | 249 ok | r74 block ok | **14/14** |
| C only (3 rows + heading + footer) | **1** | 250 / 252 | 2 heritage | 0 | 0 | 2 partitions | 252 ok | ok | FAIL (live leg) |
| **Ca then C — the landing** | **0** | **252 / 252** | 0 | 0 | 0 | {} | 252 ok | `2026-10-27` 252 `[32,32,40,29,24,95]` ok | **14/14** |

Verbatim render at base (exit 1):

```
parts {"civilizations": 95, "culture-material": 40, "linguistics": 32, "myth-symbol": 29, "synthesis": 29, "verification": 24}
rows 247 files 249
missing_from_index 2 ['culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md', 'culture-material/heritage-taxonomy-models.md']
topic_mismatch 0 []
orphan_rows 0 []
header_drift {'culture-material': {'declared': 36, 'files': 40}, 'linguistics': {'declared': 30, 'files': 32}}
totals_line 249 totals_ok True
footer {"date": "2026-10-25", "command": "find corpus/knowledge -type f -name '*.md' | wc -l", "total": 249, "dir_totals": [32, 29, 40, 29, 24, 95]}
footer_live {"total": 249, "dir_totals": [32, 29, 40, 29, 24, 95], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 0531f7a3d16bee20329c9b042eb865be13bb6c54e4e5a158a2f864f3eae3708e
```

Verbatim render after Ca's edits alone (exit 0 — and every graded leg already green, because no
file lands with Ca: the two headings stop drifting and the two heritage rows close the only
missing pair):

```
parts {"civilizations": 95, "culture-material": 40, "linguistics": 32, "myth-symbol": 29, "synthesis": 29, "verification": 24}
rows 249 files 249
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 249 totals_ok True
footer {"date": "2026-10-25", "command": "find corpus/knowledge -type f -name '*.md' | wc -l", "total": 249, "dir_totals": [32, 29, 40, 29, 24, 95]}
footer_findings [] footer_ok True
readme_sha256 1d541fb2f2d0c95ef39000fc3e7a9c95ce46122fdb45f631a1ed9502d4703c4d
```

Verbatim render after both landings (exit 0, `--selftest 14/14 checks passed`):

```
parts {"civilizations": 95, "culture-material": 40, "linguistics": 32, "myth-symbol": 32, "synthesis": 29, "verification": 24}
rows 252 files 252
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 252 totals_ok True
footer {"date": "2026-10-27", "command": "find corpus/knowledge -type f -name '*.md' | wc -l", "total": 252, "dir_totals": [32, 32, 40, 29, 24, 95]}
footer_live {"total": 252, "dir_totals": [32, 32, 40, 29, 24, 95], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 fe352307d7f11a67c5a247fe9736f7b92032f61d4d910af940b608e283fc1229
```

### 3.1 The repair is load-bearing — red-before with the committed instrument

The committed `f556d1` instrument on the same landed tree still exits **1**:

```
rows 252 files 252
missing_from_index 2 ['linguistics/conlang-scholarship.amend-2026-10-23.md', 'linguistics/conlang-scholarship.md']
orphan_rows 2 ['civilizations/conlang-scholarship.amend-2026-10-23.md', 'civilizations/conlang-scholarship.md']
header_drift {}
totals_line 243 totals_ok False
footer {"date": "2026-10-25", …, "total": 243, "dir_totals": [30, 29, 36, 29, 95]}
```

So L75-04's pair is genuinely red-before / green-after, and green requires all four repair
mechanisms: partition end at any level-2 heading, the **last** `Counts checked` block, the
**last** `Total knowledge entries:` line, and supplemental row attribution to the unique
partition holding the basename. Without the last two the new footer cannot green the totals or
footer legs; without the first two the round-73 block's two rows stay mis-attributed to
`civilizations` (that is the `orphan_rows 2` above, and the reason the two conlang files read as
missing).

### 3.2 Controls on the landed tree

- `tools/check-readme-heading.py --readme corpus/README.md`: exit 0, `findings 0`,
  `headings {"1": 1, "2": 9}` — identical to base (the ruled footer adds no heading).
- `tools/check-readme-revisions.py --readme corpus/README.md`: exit 0, `findings 0`,
  `warnings 1 REVISION-ORPHAN lines=[225, 236]` — the same pre-existing warning base carries.
- Row ↔ topic binding, all seven rows, `hits=1` each: `ROWS-BOUND: PASS` (topic lengths
  400/510/978 for claim C; 280/354 for the two conlang rows that bind to the round-73 block's
  lines; 130/369 for the two heritage rows).
- Final headings and landed line numbers: `linguistics (32)` @344, `myth-symbol (32)` @376,
  `culture-material (40)` @410, `synthesis (29)` @452, `verification (24)` @484,
  `civilizations (95)` @510. Total row-shaped lines 252 = files.

---

## 4. Every README line the two claims both touch

Computed by `difflib.SequenceMatcher` over base → Ca-only and base → C-only, in base line
numbers:

| claim | base lines replaced | inserted rows (after base line) | appended |
|---|---|---|---|
| Ca | **344** `## linguistics/ (30)`, **407** `## culture-material/ (36)` | after **428** (`headgear-head-covering-codes.md`) ×2 | — |
| C | **376** `## myth-symbol/ (29)` | after **396** (`myth-ritual-theories.md`) ×3 | after base EOF (line 823) ×4 |
| **intersection** | **∅** | **∅** | — |

**No README line is edited by both claims.** Every changed line has exactly one owner and the
insertions sit in three different partitions, so the stage files cannot conflict line-wise. The
overlap that matters is contractual:

1. **Both claims change `corpus/README.md`**, so each counter's APPENDONLY-class leg must exempt
   the sibling's lines (claims.json: "Each counter names the sibling claim's lines in its frozen
   exemptions (R1) so a combined tree grades green"). Ca's leg must accept, at the combined tree:
   C's heading line 376 (claim C's `owned_inplace`: `base_line 376`, `base_text "## myth-symbol/
   (29)"`, `after_text "## myth-symbol/ (32)"`), C's three myth-symbol rows, and C's four
   appended footer lines. C's leg must accept Ca's lines 344 and 407 and Ca's two rows. Neither
   set is a subset of the other, so a one-sided exemption cannot work.
2. **C's footer asserts Ca's numbers.** Two of the six entries in the C-owned vector — position 1
   `32` (linguistics) and position 3 `40` (culture-material) — are exactly Ca's two
   `expected_after` tokens (pairs L75-02 / L75-03). The footer is C-owned and only true on a
   tree where Ca's heading repairs are present; C-only measures exit 1.
3. **Order matters: Ca first, then C.** Ca replaces 344/407 in place and inserts rows at 428
   without moving either heading (measured: Ca-only headings stay at 344 and 407). C then
   replaces 376 and inserts three rows at 396, which shifts culture-material's heading from base
   407 to landed 410. Landing C first would leave a transiently red tree and move the line
   numbers Ca's pairs cite.
4. **Both must be in the tree at once for a green reading.** Ca-only is green only because no
   file lands with it; the combined tree is the one the round grades.

---

## 5. Findings

**F1 (resolved by the L1; recorded because it was measured).** An earlier wave-2 instruction set
Ca's row set to four rows (adding `conlang-scholarship.md` and its `amend-2026-10-23` a second
time). Measured with that set: `rows 251 / files 249` at Ca-only and `254 / 252` at Ca+C — exit 0
and every graded leg green (`duplicate_rows` is reported, not graded), but the instrument's own
live selftest leg (`rows == files`) grades FAIL. Ledger L75-02's `why` names the intended reading
("The two conlang-scholarship rows remain in the dated round-73 footer block; the round-75 sweep
repair recognizes that block as linguistics rows rather than duplicating them in the section"),
and L75-04's `why` names only the two heritage rows, so the L1 reverted to two. The staged file
carries two; the four-row variant is not shipped.

**F2 (resolved; report the provenance).** `drafts/sweep-fixed.py` is a stale, non-compiling copy
(§2). The L1 named the worktree copy as the sweep source and it compiles; every number in §3 is
that file's. Since the seat rules do not grade uncommitted worktree edits, the worktree file must
be committed with Ca's landing or the receipt cites bytes that never landed.

**F3 (finding; the ruled footer retires a cross-claim sentence).** The earlier draft footer prose
named Ca's pairs and the heritage rows — the only place the two claims' *prose* met. The ruled
footer is counts-only, so the README no longer states the Ca repair; Ca's ledger rows and
`SCORECARD ## Corrections — round 75` must carry that statement instead. In the counts footer
only the two vector entries of §4.2 are Ca-attributable.

**F4 (finding; binding is live).** All three entries were staged late in the seat, all three
differ from the w1 drafts, and the rows were re-bound to the staged bytes. A stale binding is
caught, not hidden: binding 23b to the draft while the staged copy was present measured
`topic_mismatch 1 ['myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md']`, exit 1.
Re-check the three `- topic:` lines against the staged entries at freeze time.

**F5 (finding; w1 arithmetic superseded).** `drafts/readme-rows.md` §2.3/§2.3a assumed N=2
(251 / heading `(31)`) with the 23b row conditional. The frozen `entries` list has three files →
N=3: 252 / `(32)` / `32/32/40/29/24/95`. The draft's row *shape* is right; its N and its 23b
conditionality are not.

**F6 (limit, stated).** `accept-c.py` and `accept-ca.py` do not exist at this seat
(`reports/round-75/` holds `claims.json`, `ledger.json`, an empty `telemetry/`), so no leg of
either counter is claimed. What is claimed is measured: exit code and full render of
`reports/round-28/readme/sweep.py` at base, Ca-only, C-only and both, plus `--selftest`, plus the
two `tools/check-readme-*.py` controls. Nothing here asserts that either counter's own legs pass.

---

## 6. Touched surfaces

- Created: `stage/corpus/README.md.c-rows`, `stage/corpus/README.md.c-footer`,
  `stage/corpus/README.md.ca-edits` (under `.ufo/waves/round-75/w2/`), and this report.
- Scratch: `/fast/scratch/hyaku/kotodama-r75/ScribeReadmeFinal/` (variant trees, instrument
  copies, applier, row bindings) — deleted before yield. That directory was deleted once during
  the seat by another process; it was rebuilt from the lane and the stage files, and every number
  reproduced identically afterwards (the landed README digests before and after the wipe match:
  `fe352307…`).
- Read-only: the lane's git objects (`git show`, `git ls-tree`, `git diff --shortstat`,
  `git grep`), `claims.json`, `ledger.json`, the w1 report and draft, the staged entries, the
  worktree `reports/round-28/readme/sweep.py`, and `tools/check-readme-{heading,revisions}.py`.
- Not touched: `corpus/README.md` or any other product file, `corpus/SOURCES.md`,
  `corpus/knowledge/**`, `reports/round-28/readme/sweep.py`, `SHONEN.md`, `SKILL.md`,
  `SCORECARD.md`, `LOG.md`, `corpus/QUALITY.md`, `claims.json`, `ledger.json`, `.ufo/state`,
  `.ufo/watchdog.log`, the fleet repo, every sibling lane, and the lane's git/jj state and index
  (read-only git only). One `cd /tmp` in a read-only `git ls-tree` call wrote nothing.

## 7. Installs

None. python3 stdlib plus the lane's own instruments sufficed; no tool was installed, upgraded or
removed, and no package manager was invoked.

## 8. Landing checklist for the L1

1. Land `README.md.ca-edits` first (2 headings + 2 heritage rows), then `README.md.c-rows` +
   `README.md.c-footer` (3 rows after the `myth-ritual-theories.md` row, then the heading line,
   then the footer bytes at EOF).
2. Commit the worktree `reports/round-28/readme/sweep.py` (`7e0566ad…`) with Ca, so L75-04's
   green-after receipt cites committed bytes; do not ship `drafts/sweep-fixed.py`.
3. Expect, at the combined tree: sweep exit 0, `rows 252 files 252`, footer
   `2026-10-27 252 [32,32,40,29,24,95]`, `--selftest 14/14`, README `sha256 fe352307…`.
4. Re-check the three C row strings against the staged `- topic:` lines at freeze; they were
   bound to the staged bytes as they stood at 2026-10-27 16:58, and the entry scribes may still
   revise.
