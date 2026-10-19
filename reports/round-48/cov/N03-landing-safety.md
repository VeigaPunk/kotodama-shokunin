# N03 — landing-safety verification (claim C: the cartography landing is a two-path delta)

- Seat: `N03` | role: verifier | claim: **C** | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, run 2026-10-19) — equal to `reports/round-48/claims.json` `baseline_commit`
- Out path: `reports/round-48/cov/N03-landing-safety.md` (this file)
- Non-author statement: I drafted no entry, header, README row or sweep patch. I read filed bytes and live corpus only, and wrote this file plus a gitignored `.scratch/` simulation. The simulation runs on a `git archive` copy, so **no byte under `corpus/` was created, staged or modified by this seat**.

**Verdict.** The landing *shape* is safe and proven by simulation: the specified apply touches exactly **two corpus paths** — one new file (`A`) and `corpus/README.md` (`M`) — and the resulting 224 tree sweeps green (`exit 0`, 0 missing, 0 ghosts, 0 topic mismatches, 0 header drift, footer ok). This is **not** a post-landing certificate: at my cut the entry bytes do not exist, so entry length, header contract, couples resolution and the C03–C09 audits are `could-not-evaluate` here and belong to `V01`/`A04` after apply.

---

## 1. Baseline measured

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain -uall corpus/
(no output — corpus/ is clean at HEAD)
$ find corpus/knowledge -name '*.md' | wc -l
223
$ git ls-files corpus/knowledge | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ python3 -B reports/round-28/readme/sweep.py   # tail
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
```

Tracked count `223` equals on-disk count `223`, so the partition has no untracked or ignored `.md` in `corpus/knowledge/`; the total cannot move except by the landing.

## 2. Target-path safety — the landing is an `A`, not an `M`

Three independent absence tests at the baseline:

```
$ find corpus -iname '*carto*' | wc -l
0
$ git ls-files corpus/knowledge | grep -i carto || echo "no carto tracked"
no carto tracked
$ grep -in 'cartograph\|mapmaking' corpus/README.md | head
(no output)
$ find corpus -type l | head
(no output)
```

- The slug `corpus/knowledge/culture-material/cartography-and-mapmaking.md` is free in every partition, case-insensitively, with no symlink at the path — so the apply is a create (`A`), never an overwrite.
- `corpus/README.md` carries **zero** rows for cartography and **zero** mentions in `## Known gaps (frontier)` (section starts at `corpus/README.md:417`). The README edit therefore only *adds* a row; there is no frontier row or orphan row to delete, and no deletion hunk is expected.
- All 25 culture-material entries are mode `100644` (`git ls-files -s corpus/knowledge/culture-material/*.md | awk '{print $1}' | sort -u` → one line, `100644`) and all 25 are LF-only, no BOM, trailing newline (`for f in …; do tail -c 1` → `0a`, `head -c 3` ≠ `efbbbf`; count `LF+noBOM: 25/25`, `bad: none`; `grep -lU $'\r' … | wc -l` → `0`). The new entry must match: LF, trailing newline, no BOM.

## 3. The exact delta contract

| # | Path | Git status | What the apply must do |
|---|---|---|---|
| 1 | `corpus/knowledge/culture-material/cartography-and-mapmaking.md` | `A` (new) | whole entry body; no other corpus file created |
| 2 | `corpus/README.md` | `M` | row in the culture-material section, section count 25→26, totals 223→224, footer total+dir totals, rev 2.5 block, rev-2.4 prose-vector repair |

Simulated porcelain (`.scratch/n03-sim`, base committed, then apply):

```
== state A: applied, nothing staged ==
 M corpus/README.md
?? corpus/knowledge/culture-material/cartography-and-mapmaking.md

== state B: after `git add` of the two paths ==
M  corpus/README.md
A  corpus/knowledge/culture-material/cartography-and-mapmaking.md

== state B diffstat ==
 corpus/README.md                                       | 18 ++++++++++++++----
 .../culture-material/cartography-and-mapmaking.md      | 10 ++++++++++
 2 files changed, 24 insertions(+), 4 deletions(-)
```

Two precision notes the claim wording hides:

1. **`A` requires staging.** Before `git add`, the new file is `??` and README is ` M`. "git status shows A for the new file only" is true only of the staged view; the untracked view is `??` + ` M`. Both are A/M-class deltas with no third path.
2. **Use a path-scoped stage, not `git add -A`.** The working tree already carries `?? reports/round-46/review/R01-review.md` (11 of round-46's 12 report files are tracked at HEAD; the review file is not) plus all of `reports/round-48/`. A blanket `git add -A` would fold unrelated untracked filed work into the landing commit. The wire should be `git add corpus/README.md corpus/knowledge/culture-material/cartography-and-mapmaking.md`.

Corpus-only delta check (sim, sha256 map of every file under `corpus/` before/after):

```
corpus files with changed bytes: ['corpus/README.md', 'corpus/knowledge/culture-material/cartography-and-mapmaking.md']
corpus files added: ['corpus/knowledge/culture-material/cartography-and-mapmaking.md']
```

No third corpus file changed bytes. `git grep -n '\b223\b'` over tracked text puts the count on four `corpus/README.md` lines only — `:544` (totals), `:548` (footer), and `:10`/`:12` inside the rev-2.4 historical receipt — and every other `223` in `corpus/` is an incidental bibliographic number (e.g. `civilizations/hawaii.md:22`, `linguistics/politeness-taboo-euphemism.md:9`). **No tool, template or second index pins the total**, so no third edit is required or licensed.

## 4. Simulation — reproducible

```
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ mkdir -p .scratch/n03-sim
$ git archive a01405d corpus tools reports/round-28 | tar -x -C .scratch/n03-sim
$ python3 -B .scratch/n03_landing_sim.py
```

The script (kept under gitignored `.scratch/`, deleted by scratch cleanup) initialises a throwaway repo in the archive, commits the HEAD tree as its base, applies: one placeholder entry (with a deliberate `- topic:` and nothing else), the rev-2.5 block, `## culture-material/ (26)`, the row after the calendar row, `Total knowledge entries: 224.`, the footer vector, and the rev-2.4 vector repair.

Fidelity check: the untouched archive sweeps to `readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd`, byte-identical to the live sweep in §1 — the copy is faithful, and README bytes are unchanged between r44's baseline (`c9f4eaa`, cited in `reports/round-44/scout/K02-gap-scout.md` §1) and this baseline.

Post-landing sweep on the simulated tree:

```
parts {"civilizations": 94, "culture-material": 26, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 224 files 224
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 224 totals_ok True
footer_findings [] footer_ok True
exit 0
```

## 5. Landing invariants, with the control that catches each failure

| Invariant | Source of truth | Failure mode if violated |
|---|---|---|
| Row filename == on-disk basename | `sweep.py:129-135` | `missing_from_index` + `orphan_rows`, exit 1 |
| Row topic == the entry's joined `- topic:` text, byte for byte | `sweep.py:61`, `:74-82`, `:136-148` | `topic_mismatch` class `REWRITE`/`NO_TOPIC_FIELD`, exit 1 |
| `## culture-material/ (N)` == files on disk | `sweep.py:59`, `:149-150` | `header_drift`, exit 1 |
| `Total knowledge entries: N.` == file total | `sweep.py:62`, `:160-161`, `:191-194` | `totals_ok False`, exit 1 |
| Footer `(total N files; directory totals a/b/c/d/e/f)` in **section order** | `sweep.py:66-71`, `:166-189` | `FOOTER_TOTAL` / `FOOTER_DIR_TOTALS`, exit 1 |
| Exactly one `# ` heading in README (after Ca lands) | `grep -c '^# ' corpus/README.md` (no sweep control exists — this is the Ca05 gap) | count stays 2; Ca's own threshold fails |

Section order is the sweep's `PARTS` (`sweep.py:50-57`): linguistics, myth-symbol, culture-material, synthesis, verification, civilizations. Post-landing footer vector must read `25/26/26/29/24/94`.

## 6. Planted controls (each run in the scratch repo)

| Control | Manipulation | Observed |
|---|---|---|
| 0 | untouched HEAD archive | `exit 0`, `rows 223 files 223` |
| 1 | commit HEAD tree, no edits | `git status --porcelain` → empty |
| 2 | append " (paraphrased)" to the row topic only | `exit 1`, `topic_mismatch 1 ['culture-material/cartography-and-mapmaking.md']` |
| 3 | add row but leave header at `(25)` | `exit 1`, `header_drift {'culture-material': {'declared': 25, 'files': 26}}` |
| 4 | edit a neighbour (`myth-symbol/cosmography` entry) as well | porcelain gains a second ` M`; the sha-map delta check names it |
| 5 | Ca's dup-H1 removal first, then the C apply | `exit 0`, `rows 224 files 224`, `H1 index headings: 1`, `all '# ' headings: 1`, porcelain `M`+`A` only |
| 6 | on the 224 tree, duplicate the H1 again | `grep -c '^# '` → 2, sweep still **`exit 0`** — measured, the sweep is blind to headings |

Control 6 confirms the Ca05 gap by measurement, not by reading the code: the round's green instrument passes a duplicate-H1 index, so a heading-count control must be added (or Ca's fix verified by `grep -c`, which is what the checklist in §8 uses).

Control 5 is the composite integration case: `corpus/README.md` hunk headers after both edits are `@@ -1,6 +1,14 @@`, `@@ -8,7 +16,7 @@`, `@@ -231,13 +239,14 @@`, `@@ -541,11 +550,11 @@` — four disjoint hunks, so the two claims do not textually conflict.

## 7. Findings and hazards for the integrator

**F1 — the rev-2.4 prose vector is internally inconsistent, and the obvious repair is wrong.** `corpus/README.md:11-12` reads `the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**` while the same sentence says `223` and `:12` says `223 rows vs 223 files`. Measured sums: `25/23/26/25/24/94` = **217**; the r42 landing it describes is `25/26/25/29/24/94` = **223**; the post-landing vector is `25/26/26/29/24/94` = **224**. So the rev-2.4 "after" vector has three wrong fields (myth-symbol 23, culture-material 26, synthesis 25) and must be repaired to **`25/26/25/29/24/94`** — *not* to the post-landing `25/26/26/29/24/94`, which would misdescribe round 42 (culture-material was 25 then). The rev-2.3 line at `:20` (`21/23/25/29/24/94 → 25/23/25/29/24/94`, sums 220) is correct and must not be touched.

**F2 — heading state depends on apply order.** If C's README edit lands alone, the file still has two `# kotodama-shokunin corpus index` headings (`corpus/README.md:1` and `:3`), and Ca's `grep -c` → 1 threshold is unmet. Apply Ca's one-line removal **before or in the same commit as** C's rev-2.5 block; after both, `grep -c '^# ' corpus/README.md` = 1 (control 5). Verification of Ca must therefore run on the post-integration file, not on C's draft.

**F3 — staging discipline.** Pre-existing `?? reports/round-46/review/R01-review.md`; stage only the two corpus paths (§3 note 2). `reports/round-48/**` stays untracked until the round close, and `LOG.md` (append-only, `AGENTS.md`) is bookkeeping outside the "two corpus files" claim — the repo delta is `corpus/README.md` + the new entry + the round's report tree + the LOG append, not two repo files.

**F4 — `A` vs `??` wording.** Record the porcelain at the moment it is captured; do not write "A" for an unstaged create.

**F5 — "gap re-verified unowned at landing" is not the same as "at declaration".** The landing gate must re-run the three absence tests in §2 against the tree it applies to; a collision introduced by another seat's apply between declaration and landing would show as a second new corpus file, which the delta check in §3 catches.

## 8. Pre-apply and post-apply checklist (read-only, copy-paste)

Before apply:

```
find corpus -iname '*carto*' | wc -l                 # expect 0
grep -in 'cartograph\|mapmaking' corpus/README.md    # expect no output
git status --porcelain -uall corpus/                 # expect empty
```

After apply:

```
git status --porcelain -uall corpus/                 # expect exactly:
                                                     #  M corpus/README.md
                                                     # ?? corpus/knowledge/culture-material/cartography-and-mapmaking.md
wc -l corpus/knowledge/culture-material/cartography-and-mapmaking.md   # <= ~250 (partition max 221, median 149)
find corpus/knowledge -name '*.md' | wc -l           # 224
ls corpus/knowledge/culture-material/*.md | wc -l    # 26
grep -c '^# ' corpus/README.md                       # 1 after Ca
python3 -B reports/round-28/readme/sweep.py          # exit 0, rows 224 files 224, all legs 0
```

Partition length context for the `<= ~250` threshold (measured, `wc -l`): culture-material median **149**, min **103** (`textile-technology.md`), max **221** (`funerary-material-culture.md`). r47's 790-line draft was 3.6× the partition max; a right-sized entry at or below 250 is inside precedent.

## 9. Could-not-evaluate

- The entry's actual bytes: line count, required head keys (`- topic:`, `- sources:`, `- couples:`, `- verified-at:`, `- recheck:` — measured present in 25/25 culture-material entries; `- gap:` in 5/25, so it is variable rather than universal), couples resolution and the C03–C09 audits. The fragments were not filed at my cut; `V01`/`A04` own the post-apply measurement.
- Post-apply porcelain on the real tree and the post-apply sweep exit — only the simulation is available to me; the delivered sweep is the certificate (`D01`/`V01`).
- Whether the integrator's apply will be textual (`Edit`) or whole-file write: the simulation proves the *target state*; write mechanics can still introduce a BOM, CRLF or a missing trailing newline, which §2's byte checks catch post-apply.

## 10. Commands run (all from the lane root)

`git rev-parse HEAD`; `git status --porcelain -uall`; `git ls-files …`; `find corpus …`; `grep -in`; `wc -l`; `python3 -B reports/round-28/readme/sweep.py` (live, read-only; its writes are confined to temp mirrors, `sweep.py:257,397`); `git archive a01405d corpus tools reports/round-28 | tar -x -C .scratch/n03-sim`; `python3 -B .scratch/n03_landing_sim.py` (git init + apply + sweep + six controls, inside `.scratch/`); `python3 -c "…sum(map(int, v.split('/')))"` for every vector above.
