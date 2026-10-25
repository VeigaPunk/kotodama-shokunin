# Reviewer: Claim C expansion-trend crosscheck (round 71, wave 1)

Seat: `L1Kotodama71.ReviewerTrendClaimCrosscheck` (leaf). Scope: countability of
claim C's expansion count; coverage-map ground truth; post-entry README
reconciliation requirements and exact commands. Read-only measurement; no
mutations, no subagent dispatch. All measurements at lane HEAD `b694afd6`
(worktree has untracked wave reports only; no corpus/SOURCES/README edits
pending).

## 1. What "expansion trend" counts (definition)

`/home/vgpnk/Projects/shokunin/CORPUS.md` rule 4 (line 123-125):

> "**Expansion is knowledge, not rows.** The expansion trend counts admitted
> `knowledge/` entries whose `source:` cites a `mined` row on uncovered
> coverage-map ground. There is no row quota…"

Round-70 verifier spot-check (`corpus/lessons/round-70-verifier-spotcheck.md:116`,
V70-4) applies the same definition: registry growth without an admitted
`knowledge/` entry is *not* expansion.

Claim C is exactly this shape: one new admitted `corpus/knowledge/culture-material/`
entry, sourcing ≥12 new SOURCES rows (status `mined`, `used-by` = entry), on a
coverage-map ground where the lane previously held no dance/performance/movement
owner. Its countability therefore hinges on the three instruments: inventory
file counts, registry row count, and the entry-level cited-lines lint.

## 2. Verified coverage-map ground truth (current tree)

| check | command (run from lane root) | measured result |
|---|---|---|
| corpus total | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `totals.files = 242`, exit 0 |
| partition files | `find corpus/knowledge/culture-material -maxdepth 1 -type f \| wc -l` | 35 |
| partition md counts | `find corpus/knowledge/<p> -maxdepth 1 -type f -name '*.md' \| wc -l` | civilizations 95, linguistics 30, culture-material 35, myth-symbol 29, synthesis 29, verification 24 (sum 242) |
| registry rows | `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` | 784 |
| README totals line | `corpus/README.md:723` | `Total knowledge entries: 242.` |
| README footer | `corpus/README.md:725-727` | `Counts checked 2026-10-24 … (total 242 files; directory totals 30/29/35/29/24/95)` |
| README sections | `grep -nE '^## [a-z-]+/ \([0-9]+\)' corpus/README.md` | linguistics (30), myth-symbol (29), culture-material **(34)**, synthesis (29), verification (24), civilizations (95) |
| dance filename owner | `find corpus/knowledge/culture-material -maxdepth 1 -type f -name '*danc*'` | 0 |
| dance row in README | `grep -c 'dance-performance-movement' corpus/README.md` | 0 |
| dedicated dance topic row | `grep -nE '^- topic:.*(danc|choreograph|movement culture)' corpus/knowledge/culture-material/*.md` | 1 hit — see §3 |

**Verdict:** the coverage map lists 242 entries / 35 culture-material files and
has no dance/performance/movement row or filename owner. Claim C's `before`
leg (culture-material 35, corpus 242, registry 784) matches the measured state.

## 3. Two findings on the "uncovered ground" sweep

**Finding 1 — the before-grep as written prints one topic-line hit (false
positive, not an owner).** The claim's sweep command
`grep -rniE '^- topic:.*(danc|choreograph|movement culture)' corpus/knowledge/culture-material/*.md`
matches `corpus/knowledge/culture-material/funerary-material-culture.md:4`
(its `- topic:` line). Byte-level probe: the only match is `danc` as the
substring of **"avoidance"** (`danc` ⊂ `avoidance`) in
`…the death register: avoidance terms, rite terms, office terms, monument terms…`
(`choreograph` 0, `movement culture` 0). The hit also exists at the freeze
revision (`git show b94a543c:…/funerary-material-culture.md` → same line 4).
So the claim prose "sweep command … prints no … topic-line owner" is literally
false on the base tree, though substantively correct: no file *owns* the
dance/performance/movement register (funerary owns the death register; the
match is a substring artifact of an unword-bounded regex). This does not affect
any counting leg (the `counting_command` never runs this grep), but the sweep
text should be word-bounded (e.g. `\bdanc(e|ing|es|ed)?\b` / `\bchoreograph\b`
/ `\bmovement culture\b`) or re-worded before the receipt is cited.

**Finding 2 — the README is *already* sweep-red at base: stale `## culture-material/ (34)` header.**
`python3 reports/round-28/readme/sweep.py` currently **exits 1** with exactly one
finding: `header_drift {'culture-material': {'declared': 34, 'files': 35}}`.
All other legs are green: `rows 242 files 242`, `missing_from_index 0`,
`topic_mismatch 0`, `orphan_rows 0`, `totals_ok True`, `footer_ok True`.
The stale header exists at the freeze commit `b94a543c` too (README line 398:
`## culture-material/ (34)`), i.e. revision 2.20's prose "moved 34 → 35" was
never applied to the header byte. Any landing must therefore also bump the
header (34 → 36) or the post-entry sweep cannot exit 0. `python3 tools/check-readme-revisions.py`
exits 0 today (findings 0; one advisory `REVISION-ORPHAN` at lines 214/225,
carried residual, warning-only).

## 4. Countability assessment of claim C's expansion count

- The three counters are deterministic, read-only, and currently
  self-consistent (242 / 35 / 784) with the README totals line (242) and the
  footer vector `30/29/35/29/24/95` (PARTS order linguistics, myth-symbol,
  culture-material, synthesis, verification, civilizations).
- Post-entry deltas: inventory `totals.files` 242 → 243; culture-material
  partition 35 → 36; registry 784 → ≥ 796 (784 + ≥12 new rows); find count
  35 → 36. `tools/check-cited-lines.py` on the entry must exit 0 — i.e. the
  entry must contain **no line carrying ≥2 distinct S-ids and no line starting
  with `|` that contains any S-id** (`MULTI-ID` / `TABLE-ID` findings → exit 1).
- `tools/source-audit-inventory.py` scans `<root>/**/*.md` recursively; the
  partitions are flat today, so find-count == inventory partition count.
- No count drift, integer mismatch, or double-counting risk found in the
  instruments themselves. The count will be correct if (a) exactly one new
  `.md` lands in culture-material, (b) ≥12 new registry rows are opened this
  round with status `mined` and `used-by` listing the entry, (c) every used-by
  path exists, and (d) the entry passes check-cited-lines.

## 5. Predicted post-entry README reconciliation requirements

1. **Index row added in filename order** — between
   `cuisine-food-lexicon.md` and `dress-through-eras.md` (sorted listing).
   Row format `- \`dance-performance-movement-codes.md\` — <topic>` with the
   entry's own `- topic:` text **byte-equal** (sweep `topic_mismatch` leg).
2. **Section header** `## culture-material/ (34)` → `## culture-material/ (36)`
   (fixes the inherited drift in the same edit).
3. **Totals line** `Total knowledge entries: 242.` → `243.`
4. **Counts footer** `(total 242 files; directory totals 30/29/35/29/24/95)` →
   `(total 243 files; directory totals 30/29/36/29/24/95)` (same command text,
   date updated).
5. **New revision block** `revision: 2.21 — Round-71 culture-material landing …`
   appended at the top, above 2.20 (append-only record convention; older blocks
   untouched). Label must be unique and numerically ordered (check-readme-revisions).
6. Optional but conventional: a round-71 bullet in the `## Known gaps (frontier)`
   landing-bullets area.
7. **Sweep exit 0** and revisions check exit 0 after the edits.

## 6. Exact commands a README reconciliation must run

From `kotodama-shokunin/` root:

```sh
# 1. inventory (source of totals; JSON form used by the claim)
python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
#    expect totals.files=243; culture-material prefix count=36

# 2. partition file count (cross-check)
find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l
#    expect 36

# 3. README index+footer sweep (THE reconciliation gate; must exit 0)
python3 reports/round-28/readme/sweep.py
#    expect: header_drift {} ; rows 243 files 243 ; missing_from_index 0 ;
#    topic_mismatch 0 ; orphanan_rows 0 ; totals_ok True ; footer_ok True

# 4. revision-label control (exit 0; warnings advisory)
python3 tools/check-readme-revisions.py

# 5. claim C counting command (after landing)
python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l
grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md
python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/dance-performance-movement-codes.md
#    expect culture-material=36, corpus=243, registry>=796, check-cited-lines exit 0

# 6. uncovered-ground sweeps (recorded in the entry's `- gap filled:` line)
find corpus/knowledge/culture-material -maxdepth 1 -type f -name '*danc*'
grep -rniE '^- topic:.*(danc|choreograph|movement culture)' corpus/knowledge/culture-material/*.md
#    NOTE: exact output of the second grep is 1 hit (funerary:4, "danc" ⊂ "avoidance");
#    use a word-bounded pattern if the claim text requires "prints nothing".

# 7. NOHARM diff (append-only confirmation)
git diff --stat
#    expect exactly: new entry + new SOURCES rows + README appends +
#    lesson/scorecard/log appends.
```

## 7. Verdict

Claim C's expansion count is **countably correct as instrumented** (deterministic
counters, consistent baseline 242/35/784, clean 1/1/≥12 deltas). Two defects
precede and constrain the landing: (a) the base README is already sweep-red
(stale `(34)` header) and must be fixed in the landing or the post-entry sweep
cannot exit 0; (b) the claim's uncovered-ground grep over-matches
(`danc` ⊂ "avoidance" in funerary:4 at base), so the "sweep command prints no
topic-line owner" sentence is literally false — re-word or word-bound the
pattern. Neither affects the counting legs; both should be recorded in the
round's lesson.
