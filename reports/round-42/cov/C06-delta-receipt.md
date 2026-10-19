- Seat: C06 | executor (claim C) | README rev-2.4 delta draft + coverage receipt draft | date 2026-10-19 | baseline ac47c78

# C06 — `corpus/README.md` revision-2.4 delta draft + claim-C coverage receipt draft

**Assignment** (`reports/round-42/targets.json` → `seats[id=C06]`, verbatim): *"README rev 2.4 delta
draft (myth-symbol 27, totals 224, vector 25/23/27/25/24/94, 4 rows in filename order) + receipt
draft."* Out path: this file only. Binding shared rules read at `reports/round-42/targets.json:4-9`;
claim C read at `reports/round-42/claims.json:19-24`; this seat's obligations read at
`reports/round-42/plan/P01-plan.md` §2.3 and X00's constraints at
`reports/round-42/cross/X00-connector.md` §C4 + §3 (integration order, step 3/7c).

**Status: DRAFT — integrator-applied.** This seat wrote **zero** bytes outside this file and the
disposable scratch under `.scratch/c06/`: no corpus entry, no README byte, no tool byte, no filed-round
byte. No `reports/round-*/run-validation.py` was executed anywhere (absolute rule,
`reports/round-42/targets.json:8`). Every *before* figure below is this seat's own measurement at the
pinned state (§2); every *after* figure is either the declared target or a mechanically generated value
from the tested generator (§5), and the sweep reading that certifies the landing is **measured at
close, never predicted** (§8 — the `readme-prediction-vs-delivery` rule,
`reports/round-37/op/defect-queue.json:242-251`).

**The mission's declared vector is wrong — finding D1, corroborated four times independently.**
The mission instructs the delta to write the footer vector `25/23/27/25/24/94`. That literal **sums to
218**, not the 224 the same sentence declares, and its third slot is **culture-material**, not
myth-symbol. The README's footer vector is read in the README's own section order
(`linguistics, myth-symbol, culture-material, synthesis, verification, civilizations`;
`reports/round-28/readme/sweep.py:50-57` `PARTS`, confirmed live by the sweep's `footer_live.order`).
The correct rev-2.4 vector is **`25/27/25/29/24/94`** (sum 224). Four other seats derived the same
correction independently: C08 (`reports/round-42/cov/C08-verify.md` §5, **FINDING D1**, S2 severity,
with a measured red/green/negative-control table), P01 (`reports/round-42/plan/P01-plan.md` §2.3),
X01 (`reports/round-42/cross/X01-trades.md` T7), X00 (`reports/round-42/cross/X00-connector.md`
**C4**, which binds this seat: *"C06 must use `25/27/25/29/24/94`"*). This delta therefore drafts the
corrected vector and records the mission literal as a defect of the round's own binding text, never
applied to a landed byte.

**What landed at this seat's cut** (poll window 16:0x–17:0xZ): scouts K01/K02, the O block
(O01–O12), X00/X01/X02, P01, S01/S02, R01/R02, A01, Ca01, C05/C07/C08 — and **all four entry
fences** (C01–C04), with C01 and C04 both landing after this seat's first write. The four fragments
carry **five fenced drafts over three distinct topics**, with two measured collisions (§7):

| seat | declared slug | topic | status |
|---|---|---|---|
| C01 (block 0) | `mineral-stone-symbolism.md` | lithic register | **deliverable** |
| C01 (block 1) | `purity-pollution-codes.md` | purity/pollution | **marked SPARE, not this seat's deliverable** |
| C02 | `purity-pollution-systems.md` | purity/pollution | deliverable |
| C03 | `sacred-topography-pilgrimage.md` | place register | deliverable |
| C04 | `mineral-stone-symbolism.md` | lithic register | deliverable |

So: **D2** — C01's spare and C02 both draft purity; **D4** — C01's deliverable and C04 both declare
`mineral-stone-symbolism.md`, the *same filename*. Three of four seats' deliverable topics are
distinct (mineral, purity, place); the fourth distinct slot is unresolved (§7, §Owed). The full
23→27 arithmetic is proven end-to-end with a labeled candidate probe in the unresolved slot (§5.4).

---

## 1. The invariant the delta must satisfy (measured, not assumed)

An index row is ``- `<file>.md` — <text>`` where `<text>` is the entry's own `- topic:` head-block
text with continuation lines space-joined to one line. That is what the lane's index instrument
measures (`reports/round-28/readme/sweep.py:60` `ROW_RE`, `:61` `TOPIC_RE`, `:74-79` `topic_of`;
selftest control "continuation lines space-joined", 12/12). This seat re-verified the contract
against **three existing myth-symbol entries** — `trickster.md`, `plant-symbolism.md`,
`animal-symbolism.md` — by regenerating each row from the entry's own `- topic:` and byte-comparing it
to the live README row: **all three MATCH** (command in §2.2).

Instrument `reports/round-28/readme/sweep.py`: sha256
`9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3` (identical to the r39 and r40
pins); `--selftest` **12/12** (`python3 -B reports/round-28/readme/sweep.py --selftest` →
`selftest: 12/12 checks passed`, run this seat 2026-10-19); read-only in live mode per its own
docstring (`sweep.py:28-30` — "no code path that writes inside the lane").

Baseline reading at authoring (all legs green, measured this seat 2026-10-19 at HEAD `ac47c78`):

```
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 23,
       "synthesis": 29, "verification": 24}
rows 220 files 220; missing_from_index 0; topic_mismatch 0; orphan_rows 0; header_drift {}
totals_line 220 totals_ok True
footer total 220, dir_totals [25, 23, 25, 29, 24, 94]; footer_ok True; exit 0
readme_sha256 d2eed26b30e8e62189d95446dae7d5503b6c6a398bb8e77348f878c947a5ac4f
```

K02 measured the identical census independently (`reports/round-42/scout/K02-myth-gaps.md` §1:
`ls corpus/knowledge/myth-symbol/*.md | wc -l` → 23, footer vector `25/23/25/29/24/94`), P01 states
it at plan time (`reports/round-42/plan/P01-plan.md` §0.8), and S01 records it
(`reports/round-42/scribe/S01-integration-draft.md:76-77`). Four fragments, one reading.

## 2. Before state — measured (claim-C receipt, counting commands)

`git rev-parse HEAD` → `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4` (== the declared baseline
`ac47c78`, `reports/round-42/claims.json:7`). `git status --porcelain` → `?? reports/round-42/` only:
the corpus tree is byte-identical to HEAD for every path measured here.

### 2.1 Counting command 1 (verbatim, `reports/round-42/claims.json:23`)

```sh
$ ls corpus/knowledge/myth-symbol/*.md | wc -l
23
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
25
23
25
29
24
94
$ find corpus/knowledge -name "*.md" -type f | wc -l
220
```

The loop order is the README footer vector's order (`corpus/README.md:536` =
`25/23/25/29/24/94`, linguistics-first), so the after vector is **25/27/25/29/24/94** — same string
in the census loop's order; writing the mission's literal `25/23/27/25/24/94` would name the wrong
partition and fail the sweep (§6).

### 2.2 Counting command 2 (verbatim, `reports/round-42/claims.json:23`)

```sh
$ python3 -B reports/round-28/readme/sweep.py
# exit 0; readings quoted in §1; readme_sha256 d2eed26b30e8e62189d95446dae7d5503b6c6a398bb8e77348f878c947a5ac4f
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
# exit 0; schema kotodama-source-audit-inventory/1, "read_only": true; totals.files 220
#         (per-directory derivation: [25, 23, 25, 29, 24, 94])
$ python3 -B reports/round-28/readme/sweep.py --selftest
# selftest: 12/12 checks passed; exit 0
```

Row-contract verification (this seat's own command, three entries):

```sh
$ python3 -B - <<'PY'
# regenerate each row from the entry's own `- topic:` and byte-compare to the live README row
import re
TOPIC_RE = re.compile(r"^- topic:(.*?)(?=\n- \w)", re.M | re.S)
for f in ["trickster.md","plant-symbolism.md","animal-symbolism.md"]:
    t = open(f"corpus/knowledge/myth-symbol/{f}", encoding="utf-8").read()
    row = " ".join(TOPIC_RE.search(t).group(1).split())
    rd = open("corpus/README.md", encoding="utf-8").read()
    rm = re.search(r"^- `"+re.escape(f)+r"` — (.*)$", rd, re.M)
    print(f, "MATCH" if rm and rm.group(1)==row else "MISMATCH")
PY
trickster.md MATCH row_chars 574
plant-symbolism.md MATCH row_chars 1197
animal-symbolism.md MATCH row_chars 771
```

The inventory counts markers, not verified facts (`corpus/README.md:537`); a marker count is not a
quality score. Entry quality is C05/C07/C08/R01's evidence; this receipt owns **counts and their
reconciliation** only.

### 2.3 State pins (the before state is recoverable from git alone)

| pin | value | command |
|---|---|---|
| baseline commit | `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4` | `git rev-parse HEAD` |
| corpus tree object | `55d7c8907c054074445904d1ec902adfc8767ba1` | `git rev-parse HEAD:corpus/knowledge` |
| pinned path-manifest digest | `47711c3ef1ec0aa854b2cd45607fa9c25abbf72333d193b7f7784798abcdc0c0` | `git ls-tree -r --name-only 55d7c890… \| sort \| sha256sum` |
| live manifest digest (same value) | `47711c3ef1ec0aa854b2cd45607fa9c25abbf72333d193b7f7784798abcdc0c0` | `find corpus/knowledge -name '*.md' -type f \| sort \| sed 's\|^corpus/knowledge/\|\|' \| sha256sum` |
| `corpus/README.md` digest | `d2eed26b30e8e62189d95446dae7d5503b6c6a398bb8e77348f878c947a5ac4f` | `sha256sum corpus/README.md` |
| README size | 563 lines / 137,411 bytes | `wc -lc corpus/README.md` |
| sweep instrument digest | `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3` | `sha256sum reports/round-28/readme/sweep.py` |
| this seat's generator digest | `eab092e0e706a45fdd7d852b5f9bbbdf13bb077c0b99686c8b5450f28aeafff1` | `sha256sum .scratch/c06/readme-delta.py` (139 lines) |

The two manifest digests agreeing is the measurement that the before state is exactly the baseline
commit's corpus. §8's A7 leg reads `new 0 / removed 0` against this pin at the before state
(observed, §8.1) — the pin is real, not decorative.

## 3. Line map of the pinned README (all edits reference these)

| line | content (pinned bytes) |
|---|---|
| 1, 3 | `# kotodama-shokunin corpus index` — **duplicated H1, carried defect** (`R36-README-DUPLICATE-HEADING`, `reports/round-37/op/defect-queue.json:103-131`) — **not touched by this delta** |
| 5–13 | `revision: 2.3 — Round-40 linguistics-partition expansion (2026-10-19): four …` block |
| 15, 33, 35 | rev 2.2 block / duplicated `revision: 2.0` opening line — **carried defects** — **not touched** |
| 168 / 196 / 222 / 249 / 281 / 308 | section headers `## linguistics/ (25)` / `## myth-symbol/ (23)` / `## culture-material/ (25)` / `## synthesis/ (29)` / `## verification/ (24)` / `## civilizations/ (94)` |
| 197 | blank line after the myth-symbol header |
| 198–220 | the 23 myth-symbol rows, filename-sorted (198 `animal-symbolism.md` … 220 `trickster.md`) |
| 405 | `## Known gaps (frontier)` — no round-42 bullet added by this delta |
| 532 | `Total knowledge entries: 220.` |
| 534 | `Counts checked 2026-10-19 from the repo root:` — date already current; **no edit** |
| 535 | the inventory command line — **no edit** |
| 536 | `(total 220 files; directory totals 25/23/25/29/24/94).` |
| 537 | `The inventory counts markers, not verified facts.` — **no edit** |
| 538–546 | superseded-reading paragraph, ends `…with the ten round-35 entries.` |
| 547–563 | dated `Index rows …` paragraphs (round-10 / round-19 / round-20 / round-35; 563 is the file's last line, ending `…partition counts 21/23/24/29/20/94).`) |

`wc -l` reports 563 (no trailing newline); the `split("\n")` view has 564 elements, the last empty.

## 4. Byte-exact, name-independent edits (apply in this order; rows in §5 land in the same motion)

### E1 — new revision block (insert between line 3 and line 5)

before (lines 3–5):

```
# kotodama-shokunin corpus index

revision: 2.3 — Round-40 linguistics-partition expansion (2026-10-19): four
```

after (lines 3–6):

```
# kotodama-shokunin corpus index

revision: 2.4 — Round-42 myth-symbol-partition expansion landing (2026-10-19): the four
```

The full block is drafted in §7 with ⟨…⟩ slots filled at integration time. Insertion goes **after the
blank line following the duplicated H1 (line 3) and before `revision: 2.3`** — the exact position
rev 2.3 itself took above rev 2.2 (pinned lines 3–5), with one blank line separating the new block
from the rev-2.3 block. The duplicated-H1 and duplicated-rev-2.0-line defects are inserted around,
never repaired here (P01 §3 collision control; the r39 X00-7 precedent).

### E2 — myth-symbol section header (line 196)

```
-## myth-symbol/ (23)
+## myth-symbol/ (27)
```

### E3 — totals line (line 532)

```
-Total knowledge entries: 220.
+Total knowledge entries: 224.
```

### E4 — counts footer (line 536 only)

```
-(total 220 files; directory totals 25/23/25/29/24/94).
+(total 224 files; directory totals 25/27/25/29/24/94).
```

Lines 534 (date — already 2026-10-19) and 535 (command) are unchanged; the sweep's footer leg
compares the declared total and six directory totals against the live tree and does not parse the
date, but the block remains an honest present-tense claim only if re-measured at landing — §8's
post-apply sweep is that re-measurement. **This is the line the mission's literal vector would get
wrong** (§6, D1).

### E5 — new dated index paragraph (append after line 563, the current last line)

```
Index rows re-measured 2026-10-19 at HEAD `⟨sha⟩` after the round-42 wave
(224 rows vs 224 files; the four new rows above added to the myth-symbol section;
0 missing, 0 ghosts, 0 duplicate rows, 0 header drift, 0 topic mismatches; partition
counts 25/27/25/29/24/94).
```

⟨sha⟩ and the reading are **measured at close** (the landing commit and the post-apply sweep); if the
sweep is not green, E5 is not written. Precedent for the shape: the round-35 paragraph at
`corpus/README.md:560-563`.

**Deliberately not in this delta:** (a) any edit to the superseded-reading paragraph (:538–546).
Revision 2.0 appended its move there; revisions 2.1–2.3 did not (their moves live only in their
blocks, :5–46). This delta follows the **most recent landing precedent (rev 2.3)** and records the
move in the §7 block only; if the integrator prefers the rev-2.0 style, the optional append after
line 546 is `Revision 2.4 moved the totals 220 → 224 and \`## myth-symbol/\` 23 → 27 with the four
round-42 entries.` — one decision, either reading sweeps green. (b) A new `## Known gaps (frontier)`
bullet — revisions 1.7–2.3 added none; the round-42 coverage record belongs to this receipt and S01's
dossier, not the index. (c) Any repair of the carried H1/rev-2.0 duplication defects (see E1).
(d) **No edit of any existing row** — the 23 myth-symbol rows stay byte-identical; the delta only
inserts.

## 5. The four row insertions (name-dependent — rule + tested generator, not guessed bytes)

**Rule.** Each new row is ``- `<file>.md` — <entry's own continuation-joined `- topic:` text>``
inserted where `<file>.md` sorts (ASCII) among the section's rows. Existing rows are filename-sorted
today (verified in §1's sweep: `orphan_rows 0`, and structurally in the synthetic check, §5.3).

**Final-filename authority (X00 §3 step 1/7c):** the integrator fixes the final filename set and
C06's rows are re-derived mechanically from the **landed bytes** at apply time — the generator (§5.1)
emits each row from the entry file itself, so the landing equality is whatever the landed bytes say,
never this draft's table. The anchors below are the generator's own staged dry-run output, not hand
arithmetic.

### 5.1 Generator (tested; integrator places it, e.g. `reports/round-42/readme/readme-delta.py`)

Read-only unless `--apply` names a path. This is the round-40 C06 generator
(`reports/round-40/cov/C06-delta-receipt.md` §5.1), itself the round-39 C06 generator, narrowed to the
myth-symbol partition; totals/footer always computed over all six partitions. The exact tested bytes
were written this seat to `.scratch/c06/readme-delta.py` (disposable; source is r39 §5.1 with the
docstring, default `--parts ["myth-symbol"]`, and nothing else changed — 3-line diff). Invocation:

```sh
python3 readme-delta.py                     # text report
python3 readme-delta.py --json              # machine delta
python3 readme-delta.py --apply OUT.md      # write reconciled copy to OUT.md
python3 readme-delta.py --root ROOT         # dry-run against a staged tree
```

`--apply` writes only the path given and only the three mechanical families (header, rows,
totals/footer line). E1/E5's prose is **not** written by it — apply those by hand from §4/§7 so the
prose is authored, not templated (the r35 placeholder lesson, `SCORECARD.md:681-684` via r39's X00).
**Apply-order rules** (measured in the r35 synthetic run, inherited unchanged): one global bottom-up
pass over the whole file for all row insertions; on a shared anchor, larger `merged_index` first; a
row that sorts first in a section inserts at header line + 1. Entries land **before** the README delta
in one motion, or the tree sits in an intermediate red state (expected reds: entries-without-rows = 4
`missing_from_index`; rows-without-entries = 4 ghosts — X00 §3 step 7c).

### 5.2 Anchors — all four landed fences, and the two slug collisions (measured, final poll)

The generator run read-only against the pinned README, with the landed fences staged under their
declared names, emits (index order):

| fragment / block | declared path | sorts | insert after line | after row |
|---|---|---|---|---|
| `C01-entry-1.md` block 0 (deliverable) | `mineral-stone-symbolism.md` | after `hero-journey-variants.md` | **210** | `hero-journey-variants.md` |
| `C04-entry-4.md` block 0 | `mineral-stone-symbolism.md` | after `hero-journey-variants.md` | **210** (shared) | `hero-journey-variants.md` |
| `C01-entry-1.md` block 1 (SPARE) | `purity-pollution-codes.md` | after `plant-symbolism.md` | **216** | `plant-symbolism.md` |
| `C02-entry-2.md` block 0 | `purity-pollution-systems.md` | after `plant-symbolism.md` | **216** (shared) | `plant-symbolism.md` |
| `C03-entry-3.md` block 0 | `sacred-topography-pilgrimage.md` | after `sacred-kingship-mythic-charter.md` | **218** | `sacred-kingship-mythic-charter.md` |

Three anchors (210, 216, 218) serve five drafts: **two slug collisions** — the mineral pair on
anchor 210 (D4) and the purity pair on anchor 216 (D2), each a shared-anchor case in which the row
with the larger `merged_index` lands second in the bottom-up pass. Only **one slug per collision** may
land; the losers' rows must never reach the index. The **distinct slug set** therefore has at most
three members from these five drafts (mineral, purity, place), leaving one of the four rev-2.4 slots
open — which is why the §5.4 probe is still needed to prove the 23→27 arithmetic.

### 5.3 Acceptance of the generator itself (measured end-to-end this seat)

Synthetic lane `.scratch/c06/synthlane/` (copy of the live README + all 220 real entries + **4 probe
myth-symbol entries** with multi-line `- topic:` heads, chosen to cover the hard cases:
`aaa-probe-first.md` first-in-section; `myth-symbol-probe-aaa.md` / `-bbb.md` an adjacent pair
sharing one anchor; `zzz-probe-tail.md` last-in-section; a redirected sweep copy
`.scratch/c06/sweep-applied.py` with only its `LANE` constant re-pointed, the r35/r39 C11/C06
method):

- generator on the **live** tree: 0 missing rows, totals/footer before == after — **no-op** (the
  reader is calibrated);
- generator on the synthetic lane: 4 rows emitted, anchors exactly **197 / 213 / 213 / 220** —
  first-in-section, shared-anchor pair, and tail all hit;
- `--apply` to a clean copy → redirected sweep on the applied copy: **224 rows vs 224 files,
  0 missing, 0 ghosts, 0 topic mismatches, 0 header drift, totals_line 224 totals_ok True,
  footer total 224 / [25, 27, 25, 29, 24, 94] footer_ok True, exit 0**;
- negative controls, all observed on the applied copy: deleting one applied row → exit 1,
  `missing_from_index 1 ['myth-symbol/zzz-probe-tail.md']`; reverting the totals line to 220 →
  exit 1, `totals_line 220 totals_ok False`; reverting the footer vector to the before-value
  `25/23/25/29/24/94` → exit 1, `FOOTER_DIR_TOTALS declared [25,23,25,29,24,94] live [25,27,25,29,24,94]`.

### 5.4 Full-target dry-run (the 23→27 arithmetic proven, not asserted)

**Run A — the three real distinct slugs + one labeled CANDIDATE probe** in the unresolved fourth slot
(K02's R2 name `dream-vision-trance.md`, disposable probe topic text — not any seat's bytes), the
generator reads the full target (23 + 4 = 27; 220 + 4 = 224). Measured output this seat:

```
readme d2eed26b30e8 live_counts {'linguistics': 25, 'myth-symbol': 27, 'culture-material': 25, 'synthesis': 29, 'verification': 24, 'civilizations': 94}
myth-symbol      declared 23 rows 23 live 27  header '## myth-symbol/ (23)' -> '## myth-symbol/ (27)'  ghosts []
   + dream-vision-trance.md                       insert after line 207  (after divination-omen-systems.md) row_chars=185  [CANDIDATE]
   + mineral-stone-symbolism.md                   insert after line 210  (after hero-journey-variants.md) row_chars=2110
   + purity-pollution-systems.md                  insert after line 216  (after plant-symbolism.md) row_chars=2091
   + sacred-topography-pilgrimage.md              insert after line 218  (after sacred-kingship-mythic-charter.md) row_chars=1603
totals Total knowledge entries: 220. -> Total knowledge entries: 224.
footer (total 220 files; directory totals 25/23/25/29/24/94). -> (total 224 files; directory totals 25/27/25/29/24/94).
```

**Run B — the five landed drafts as-is** (three landed slugs, one of them a collision pair counted
once): staged = `mineral-stone-symbolism.md` (C04's block), `purity-pollution-systems.md` (C02),
`sacred-topography-pilgrimage.md` (C03). Measured:

```
myth-symbol      declared 23 rows 23 live 26  header '## myth-symbol/ (23)' -> '## myth-symbol/ (26)'  ghosts []
   + mineral-stone-symbolism.md                   insert after line 210  (after hero-journey-variants.md) row_chars=2110
   + purity-pollution-systems.md                  insert after line 216  (after plant-symbolism.md) row_chars=2091
   + sacred-topography-pilgrimage.md              insert after line 218  (after sacred-kingship-mythic-charter.md) row_chars=1603
totals Total knowledge entries: 220. -> Total knowledge entries: 223.
footer (total 220 files; directory totals 25/23/25/29/24/94). -> (total 223 files; directory totals 25/26/25/29/24/94).
```

**Honest reading of these dry-runs.** Run A proves the **arithmetic** (header 27, totals 224, vector
`25/27/25/29/24/94`) and the **insertion geometry** for the anchors; Run B is the honest count of what
the five landed drafts actually supply — **26 files / 223**, because the drafts collapse to three
distinct slugs (§7 D2/D4) and the round needs four. Neither run is a valid landing set on its own: Run
A's fourth slot is a probe, Run B is one entry short. **Run A was also applied to a copy and swept
green**: `rows 224 files 224`, 0 missing, 0 ghosts, 0 topic mismatches, 0 header drift, totals_line
224, footer `[25, 27, 25, 29, 24, 94]`, exit 0 — so the four-row target is reachable, not just
computable. Whichever set the integrator fixes, the generator re-emits each row from the landed bytes
at apply time. The candidate line exists only to prove the arithmetic — a candidate's bytes and name
must never reach the index (the r39 staging-name lesson,
`reports/round-39/cov/C06-delta-receipt.md:628-631`).

## 6. FINDING D1 — the mission's footer vector is arithmetically wrong (this seat's derivation)

**Statement.** `reports/round-42/targets.json` → `seats[id=C06].mission` declares the delta as
*"myth-symbol 27, totals 224, vector 25/23/27/25/24/94, 4 rows in filename order"*. The literal
vector is internally inconsistent with its own total and names the wrong partition.

**Evidence 1 — arithmetic.** The vector is read in README section order
(`linguistics, myth-symbol, culture-material, synthesis, verification, civilizations`;
`sweep.py:50-57`, confirmed live by `footer_live.order`):

- `25/23/27/25/24/94` sums to **218**; the same sentence declares totals **224**. Sum mismatch.
- slot 3 is **culture-material**, so the literal moves culture-material 25 → 27 and leaves myth-symbol
  at 23 — contradicting the same sentence's *"myth-symbol 27"*.
- the section-order-correct vector is **`25/27/25/29/24/94`**, which sums to **224**.

**Evidence 2 — measured on the generator.** This seat's synthetic applied copy (224 files) swept with
the corrected vector reads green (`footer_ok True`, exit 0); the negative control reverting the footer
to `25/23/25/29/24/94` reads **exit 1** with `FOOTER_DIR_TOTALS declared [25,23,25,29,24,94] live
[25,27,25,29,24,94]`. So the instrument does flag the mission's literal — it is a real rejection, not
an instrument that never fires.

**Corroboration (four independent derivations).** C08 `reports/round-42/cov/C08-verify.md` §5
(FINDING D1, S2, with its own red/green/control table over a 224-file synthetic tree); P01
`reports/round-42/plan/P01-plan.md` §2.3 (`25/27/25/29/24/94`); X01
`reports/round-42/cross/X01-trades.md` T7; X00 `reports/round-42/cross/X00-connector.md` C4, which
binds this seat to the corrected vector.

**Disposition taken by this seat.** Draft the corrected vector `25/27/25/29/24/94` (E4/§7); record the
mission literal as a defect of the round's binding text; **never** apply it to a landed byte. The
post-apply sweep reading remains the integrator's to measure — this seat's readings are on synthetic
trees, never a delivered revision.

## 7. The four landed fences (byte-pinned), the two slug collisions, and the slot state

The row bytes below are **derived from the landed draft fences** (the fence's own `- topic:`,
continuation-joined) at the fragment digests pinned here. They are a cross-check for the integrator,
not a substitute for the generator: the landing equality is whatever the landed bytes say at apply
time, and §8's post-apply sweep is what certifies it. C01's fragment carries **two** fenced blocks —
block 0 the deliverable, block 1 a **marked SPARE** (its own `:21` and `:285`: *"The integrator must
not land both"*).

| fragment / block | whole sha256 | fence sha256 | declared path | row sha256 | row chars |
|---|---|---|---|---|---|
| `C01-entry-1.md` block 0 (deliverable) | `b7140ce069ee5538…` | `6999a9123578bf8f…` | `myth-symbol/mineral-stone-symbolism.md` | `522e5ae5b83c78f8…` | 1370 |
| `C01-entry-1.md` block 1 (SPARE) | `b7140ce069ee5538…` | `5ba3a9fb1ac92d4a…` | `myth-symbol/purity-pollution-codes.md` | `40352909f5e02042…` | 1232 |
| `C02-entry-2.md` block 0 | `474c7fac52f4f6ef…` | `2d184a2159b4412e…` | `myth-symbol/purity-pollution-systems.md` | `5102fb21aa45c558…` | 2091 |
| `C03-entry-3.md` block 0 | `d7daa54b313233ed…` | `9659ac41d2baad17…` | `myth-symbol/sacred-topography-pilgrimage.md` | `6a3062834e5e8ab9…` | 1603 |
| `C04-entry-4.md` block 0 | `2b8eb533dbfc0a89…` | `072d1f1a18de5010…` | `myth-symbol/mineral-stone-symbolism.md` | `125fc4ffed95401d…` | 2110 |

**As-read snapshot: 2026-10-19T16:07Z.** The digests above are the bytes as of that stamp, re-measured
after C03 and C04 were each amended during this seat's verification pass (C03's whole digest moved
`e0f4067f278c7ff9…` → `d7daa54b313233ed…`; C04's `27d80129acc19424…` → `b2d828c9b9da5b4f…` →
`2b8eb533dbfc0a89…`, its row 2417 → 2110 chars). **C04's fence and row bytes were stable across those
amendments while its prose changed** — the row reading survives, the whole-file digest does not, which
is exactly why both are pinned. **Any further amendment to a fragment voids the corresponding row
reading above**; the generator re-derives the row from whatever bytes are landed at apply time, so the
reconciliation is mechanical regardless. This is why the receipt pins digests rather than trusting a
single read of a live tree.

**FINDING D2 — the purity slot: C01's SPARE and C02 both draft the purity/pollution topic.** C01's
spare declares `purity-pollution-codes.md`; C02 declares `purity-pollution-systems.md`; both are the
**purity/pollution complex** and both sort into the **same index slot** (anchor 216, after
`plant-symbolism.md`, before `ritual-liminality.md`, §5.2), so at most one can land. C01 itself
anticipates this: its header (`:1`) names the purity draft a *"marked spare"* and its `:21` reads
*"The purity draft is retained as a spare (section 6), not deleted … The integrator must not land
both."* K02's R4 section (`reports/round-42/scout/K02-myth-gaps.md` §R4) independently **recommends
C02's draft** and *"does not commission a second purity entry."*

**FINDING D4 — the mineral slot: C01's deliverable and C04 declare the *same filename*.** Both
declare `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` — the **lithic register**, K02's R1
— and both fence a full entry under it (C01 block 0, 54,731 B; C04, 61,715 B). This is a **harder**
collision than D2: not merely the same topic but the **same path**, so at most one file can exist
there. Neither fragment names the other as a spare: C04's `:21` and C01's `:3` both claim the slug as
their deliverable, and C04's disjointness section (`:9-19`) still lists C01 as holding
`purity-pollution-codes.md` — i.e. **C04 was written before C01's reassignment landed** and could not
have known. The two mineral drafts are therefore *independent* realizations of one slot.

**The reassignment that produced D4 is visible in the bytes.** This seat's first read of C01 (16:2xZ)
declared `purity-pollution-codes.md` as its deliverable (`C01-entry-1.md:3`, digest then
`da1272a11b9639bb…`). C01 was subsequently amended (digest now `b7140ce069ee5538…`): its deliverable
became `mineral-stone-symbolism.md` and the purity bytes were demoted to a fenced spare. So D2 and D4
are the two halves of one wave-level allocation failure — two seats converged on purity first, then
two converged on mineral.

**FINDING D3 — a softer overlap: C03's topic is K02's R3 domain.** C03 declared
`sacred-topography-pilgrimage.md` — *"the place register … the holy-site typology … pilgrimage"* —
which is K02's R3 recommendation domain (`pilgrimage-sacred-geography.md`). The **slugs differ and
sort into different slots** (C03 at anchor 218), so this is **not** a slug collision like D2/D4 — but
it is a **topic overlap**: if C03 lands, K02's R3 is satisfied and must not also be commissioned.

**This seat's disposition:** both slug collisions are **routed, not resolved** — the final filename
set is X00's/the integrator's (`reports/round-42/cross/X00-connector.md` §3 step 1/7c). This delta
drafts **no row** for any colliding slug, because writing one would presuppose the integrator's choice
and the losers' rows must never reach the index. The generator re-emits each surviving row from the
landed bytes at apply time.

**Filename/allocation state at cut — one of four slots is unresolved.** The five drafts supply three
distinct slugs (mineral, purity, place); a valid four-entry set needs a fourth distinct topic. K02's
**R2** (`dream-vision-trance.md`, after `divination-omen-systems.md`) is the only remaining ranked
candidate that collides with none of the five drafts; K02's R3 is subsumed by C03 (D3) and R1 is
contested by D4. If the integrator instead re-slots one of the two losing drafts (C01's spare purity
is explicitly offered for re-slotting at `C01-entry-1.md:21`), that is a fourth distinct topic too —
but it must not be the *same* topic as the winner of its own collision. Either way §5.4's probe
proves the arithmetic and the generator re-derives the real rows.

## 8. Receipt — after-state assertion block and its negative control

### 8.1 The block (read-only; runs from the lane root; `PIN` is §2.3's tree object)

```python
python3 - <<'PY'
import pathlib, re, subprocess, json
PARTS=['linguistics','myth-symbol','culture-material','synthesis','verification','civilizations']
TARGET={'linguistics':25,'myth-symbol':27,'culture-material':25,'synthesis':29,'verification':24,'civilizations':94}
PIN='55d7c8907c054074445904d1ec902adfc8767ba1'
fails=[]
def chk(leg, ok, detail):
    print(('PASS ' if ok else 'FAIL ')+leg+' :: '+detail)
    if not ok: fails.append(leg)
live={p:len(sorted(pathlib.Path(f'corpus/knowledge/{p}').glob('*.md'))) for p in PARTS}
chk('A1_census_counts', live==TARGET, f'live {live} target {TARGET}')
out=subprocess.run(['python3','-B','tools/source-audit-inventory.py','--json','--summary','--root','corpus/knowledge'],capture_output=True,text=True)
inv=json.loads(out.stdout)
chk('A2_inventory_total', inv['totals']['files']==224, f"totals.files {inv['totals']['files']} target 224 (exit {out.returncode})")
rd=pathlib.Path('corpus/README.md').read_text()
hdr={m.group(1):int(m.group(2)) for m in re.finditer(r'^## (linguistics|myth-symbol|culture-material|synthesis|verification|civilizations)/ \((\d+)\)$', rd, re.M)}
chk('A3_readme_headers', hdr==TARGET, f'headers {hdr}')
tot=[l for l in rd.splitlines() if l.startswith('Total knowledge entries')][0]
chk('A4_readme_total', tot=='Total knowledge entries: 224.', tot)
footline=[l for l in rd.splitlines() if re.match(r'^\(total \d+ files; directory totals ', l)]
chk('A5_readme_footer', any('(total 224 files; directory totals 25/27/25/29/24/94)' in l for l in footline), f'footer now: {footline[0] if footline else "absent"}')
rows={}
for p in PARTS:
    m=re.search(r'^## '+re.escape(p)+r'/ \(\d+\)\n(.*?)(?=^## )', rd, re.M|re.S)
    rows[p]=len(re.findall(r'^- `[^`]+\.md` — ', m.group(1), re.M))
chk('A6_rows_eq_files', rows==live, f'rows {rows} == files {live}')
pinned=set('corpus/knowledge/'+l for l in subprocess.run(['git','ls-tree','-r','--name-only',PIN],capture_output=True,text=True).stdout.split('\n') if l)
liveset=set(f'corpus/knowledge/{p}/{f.name}' for p in PARTS for f in pathlib.Path(f'corpus/knowledge/{p}').glob('*.md'))
new=sorted(liveset-pinned); gone=sorted(pinned-liveset)
chk('A7_delta_4_files', len(new)==4 and not gone and all('/myth-symbol/' in n for n in new), f'new {len(new)} removed {len(gone)}')
for n in new: print('  + '+n)
print('VERDICT', 'GREEN' if not fails else 'RED legs '+str(fails))
PY
```

**Negative control — observed at the before state (this seat's run, 2026-10-19, 16:0xZ):**

```
FAIL A1_census_counts :: live {'linguistics': 25, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 24, 'civilizations': 94} target {'linguistics': 25, 'myth-symbol': 27, 'culture-material': 25, 'synthesis': 29, 'verification': 24, 'civilizations': 94}
FAIL A2_inventory_total :: totals.files 220 target 224 (exit 0)
FAIL A3_readme_headers :: headers {'linguistics': 25, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 24, 'civilizations': 94}
FAIL A4_readme_total :: Total knowledge entries: 220.
FAIL A5_readme_footer :: footer now: (total 220 files; directory totals 25/23/25/29/24/94).
PASS A6_rows_eq_files :: rows {'linguistics': 25, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 24, 'civilizations': 94} == files {'linguistics': 25, 'myth-symbol': 23, 'culture-material': 25, 'synthesis': 29, 'verification': 24, 'civilizations': 94}
FAIL A7_delta_4_files :: new 0 removed 0
VERDICT RED legs ['A1_census_counts', 'A2_inventory_total', 'A3_readme_headers', 'A4_readme_total', 'A5_readme_footer', 'A7_delta_4_files']
```

**Positive control — the same block on the clean applied synthetic lane** (proves GREEN is reachable,
so a later RED is informative):

```
PASS A1_census_counts / A2_inventory_total / A3_readme_headers / A4_readme_total / A5_readme_footer / A6_rows_eq_files / A7_delta_4_files
  + corpus/knowledge/myth-symbol/aaa-probe-first.md
  + corpus/knowledge/myth-symbol/myth-symbol-probe-aaa.md
  + corpus/knowledge/myth-symbol/myth-symbol-probe-bbb.md
  + corpus/knowledge/myth-symbol/zzz-probe-tail.md
VERDICT GREEN
```

Readings: (a) every after-leg **fails at the before state**, so a later GREEN is informative, not
green-by-construction; (b) A6 is an equality *invariant* — green now, required to stay green after;
(c) A7 read `new 0 / removed 0` at the before state, the positive proof that the §2.3 pin matches the
live tree. The block shells out only to `git ls-tree` and the read-only inventory tool; it writes
nothing. It counts rows — it does **not** compare row text with `- topic:` bytes; that verbatim leg is
§1's sweep and §5.3's applied-copy reading, and a count-only green must never be quoted as index-text
reconciliation (the r19 lesson, `corpus/README.md:95-101`).

### 8.2 The integrator's acceptance sequence (claim C thresholds, `reports/round-42/claims.json:24`)

1. C05's audit over all four drafts lands, clean or defect-listed (audit leg — C05/C07/C08/R01's
   evidence). X00's chain is C05 → C06's final filename set → apply.
2. **Resolve the D2 and D4 slug collisions and pick the fourth distinct topic (§7)**; fix the four
   filenames; apply the four entries, then E1–E5 + the four generated rows in one motion. The five
   landed drafts supply only three distinct slugs (Run B, §5.4) — the fourth entry is the
   integrator's/the wave's call (K02's R2, or a re-slotted loser, §7).
3. `python3 -B reports/round-28/readme/sweep.py` → **must** read `rows 224 files 224`,
   `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`,
   `totals_line 224 totals_ok True`, footer `{total 224, dir_totals [25, 27, 25, 29, 24, 94]}`,
   `footer_ok True`, exit 0. `ls corpus/knowledge/myth-symbol/*.md | wc -l` → **27**.
4. Diff the landed README against this draft before trusting the sweep (the r35 apply left
   placeholder lines the sweep then caught; the r36 staged prediction diverged from the delivered
   digest — r39 X00-3's reason, inherited).
5. Re-run §8.1's block → VERDICT GREEN; fill §7's ⟨…⟩ and write E5 with the landing sha.
6. Inventory cross-check: `python3 -B tools/source-audit-inventory.py --json --summary --root
   corpus/knowledge` → `totals.files 224`.
7. Confirm the landed slug set has **four distinct names** before the sweep — the five drafts offer
   three (§5.2/§7); landing a collision pair produces two rows on one slot and a duplicated topic.

Until step 3/5 read green on the landed tree, **no after-count in this fragment may be quoted as
measured** — every after value here is target or generated, never landed.

## 9. Limits and cross-fragment consistency

- All before figures are point-in-time at `ac47c78` with a byte-clean corpus tree; any landing
  invalidates §2 until re-measured (the §2.3 pins make the before state recoverable from git alone).
  The §7 row bytes are draft-derived: if an executor fragment is amended before landing, the pinned
  fence digests detect it and the generator re-emits the row mechanically. **This already happened
  once**: C01 was amended mid-round (its digest moved `da1272a11b9639bb…` → `b7140ce069ee5538…`), which
  is what produced D4 (§7). Any fragment read here is pinned by digest for exactly that reason.
- This receipt certifies **counts and their reconciliation** — never entry quality, source
  resolvability, or canon status (`corpus/README.md:537`; the audit is C05/C08's, the adversarial
  fabrication hunt is R01's, the admission verdict is the integrator's per `REGIMEN.md:41-43`).
- The census command globs only `*.md` at each partition's top level; the inventory and
  `find -type f` legs are the wider nets and agree at 220.
- No `reports/round-*/run-validation.py` was executed anywhere by this seat (absolute rule,
  `reports/round-42/targets.json:8`). The round's close-time runner is the integrator's artifact;
  `REGIMEN.md:57`'s exit-0-at-close requirement stands regardless of this fragment.
- Cross-fragment readings, no divergence found on the **corrected** vector: X00 C4, C08 D1, P01 §2.3,
  X01 T7, K02 §1, S01 §4, C02 §Owed all state `25/27/25/29/24/94`. **No divergence remains.** An
  earlier draft of this fragment recorded S01 as still carrying the mission literal at `:272`; S01 was
  revised during this seat's window and now catches the defect explicitly — *"The C06 mission's vector
  bytes are arithmetically wrong; use `25/27/25/29/24/94`"*
  (`reports/round-42/scribe/S01-integration-draft.md:318-320`), with the literal quoted only as the
  wrong figure (`:319`, `:504`, `:609`). C02's fragment independently prints the correction at
  `reports/round-42/cov/C02-entry-2.md:220-221`. Six seats converged on one corrected vector.
- **The topic-allocation shortfall is the main limit.** The five landed drafts collapse to three
  distinct slugs (§7 D2/D4), so the landed set is one entry short of the four the round needs; the
  delta's arithmetic (23→27, 220→224, vector) is proven end-to-end (§5.4 Run A, applied green) but the
  *allocation* is not, and resolving it is the integrator's call, not this seat's.

## Addendum — fragment-landing timeline (this seat's polls, all 2026-10-19)

- ≤15:57Z: `reports/round-42/` held claims, targets, telemetry, op/O09 only (O09's own `:8-16`
  records every claim-O output absent at its cut — independent corroboration of the batch timing).
- ~16:0xZ poll: cov/ appeared with C02, C08; K01, P01, O03, O04, O06–O10, A01, Ca01, S01, S02.
- ~16:2xZ poll: cov/ = C01, C02, C07, C08; X00, X01, X02 landed; O01/O02/O05/O11/O12 landed; K02
  landed. C01 then declared `purity-pollution-codes.md` (digest `da1272a11b9639bb…`) — the reading
  this seat's first draft recorded.
- ~16:3xZ poll: C03 landed (`sacred-topography-pilgrimage.md`); C01/C02 still the purity pair; C04
  absent — D2 measured on the C01/C02 pair.
- ~17:0xZ poll (final): **C01 amended** (digest `b7140ce069ee5538…`) — deliverable reassigned to
  `mineral-stone-symbolism.md`, purity demoted to a marked spare; **C04 landed** the same slug. So D4
  was created by the amendment and measured here; all four fences now present.
- All §1–§8 measurements predate or ignore the landing-boundary state; the §2.3 pins keep the before
  state recoverable from git alone regardless of what lands later.

## Owed

- `reports/round-42/cov/C04-entry-4.md` — **landed** (~17:0xZ), after this seat's first write; folded in
  at §5.2/§7. Its fence (stable at `072d1f1a18de5010…`) declares `mineral-stone-symbolism.md`, the
  same path C01's amended deliverable claims — that is D4 (§7). Its prose was amended again during this
  seat's verification pass (whole digest `27d80129acc19424…` → `b2d828c9b9da5b4f…` →
  `2b8eb533dbfc0a89…`), so only the fence/row digests are trustworthy for it. No row is drafted here.
- `reports/round-42/cov/C01-entry-1.md` — **amended mid-round** (digest `da1272a11b9639bb…` →
  `b7140ce069ee5538…`). Its first reading (16:2xZ) declared `purity-pollution-codes.md`; its current
  bytes declare `mineral-stone-symbolism.md` as deliverable with the purity draft demoted to a marked
  spare. Any earlier reading of this fragment is void; §7 pins the current digest.
- **The D2/D4 slug-collision dispositions (§7)** — **D2**: which of C01's spare
  `purity-pollution-codes.md` or C02's `purity-pollution-systems.md` lands (X00/the integrator owns it;
  K02 recommends C02's draft). **D4**: which of C01's deliverable `mineral-stone-symbolism.md` or
  C04's same-named entry lands — the *same path*, so exactly one can exist. No row for any colliding
  slug is drafted here until those choices are made.
- **The fourth distinct topic (§7)** — the five landed drafts supply only three distinct slugs
  (mineral, purity, place), so a valid four-entry set needs a fourth. K02's R2
  (`dream-vision-trance.md`) is the only ranked candidate colliding with none of the five; C01
  explicitly offers its spare purity draft for re-slotting (`C01-entry-1.md:21`), which is an option
  only if it is *not* the same topic as the purity winner. This seat does not decide it.
- **The D3 overlap disposition (§7)** — C03's `sacred-topography-pilgrimage.md` covers K02's R3
  pilgrimage/place domain; if C03 lands, K02's R3 (`pilgrimage-sacred-geography.md`) must not also be
  commissioned. Softer than D2/D4 (different slugs, different slots), recorded so the integrator does
  not land two place/pilgrimage entries.
- `reports/round-42/cov/C05-audit.md` — the audit leg of claim C's threshold ("audits 4/4 PASS",
  `reports/round-42/claims.json:22`); **still absent at this seat's final poll** (C07/C08 landed but the
  C05 audit itself is the primary leg). Apply gate: entries land only after C05 is clean or its defects
  are filed (X00 chain).
- The integrator's application of §4/§5/§7 to `corpus/README.md` + the four entries, then the §8.2
  sequence (post-apply sweep + GREEN §8.1 + diff-vs-draft). Nothing is landed until then.
- `reports/round-42/run-validation.py` — required by `REGIMEN.md:57` at close; integrator-authored,
  isolated-copy execution only (the r39 isolation-replay protocol; never in-tree).

## Citations

- `reports/round-42/claims.json:7` (baseline `ac47c78`), `:9` (axes), `:19-24` (claim C: `:21`
  before, `:22` after_required, `:23` counting commands, `:24` thresholds), `:26-27` (non_goals)
- `reports/round-42/targets.json:4-9` (shared rules; `:8` the ABSOLUTE runner ban), `seats[id=C06]`
  (mission + out path, the vector literal that is D1)
- `REGIMEN.md:27-30` (per-round contract), `:41-43` (admit rule), `:57` (close-time runner)
- `reports/round-42/plan/P01-plan.md` §0.8 (baseline census), §2.3 (the rev-2.4 delta: header 23→27,
  totals 220→224, vector `25/27/25/29/24/94`, 4 rows filename order), §2.1 (fallback if K02 late),
  §3 (integration order + collision risks)
- `reports/round-42/scout/K02-myth-gaps.md` §1 (baseline + green index), §2 (23-entry topic table),
  §3 (absence sweeps), §R1–R4 (the four recommendations; **R4** the purity-slot disposition and the
  recommendation to admit C02's draft), §filenames (sort positions)
- `reports/round-42/cross/X00-connector.md` §1 (write-path matrix: `corpus/README.md` rev 2.4 = C06
  delta block only, row bytes byte-equal to the landed `- topic:`), §C4 (**the binding correction**:
  C06 must use `25/27/25/29/24/94`), §3 (integration order, steps 1/3/7c), §4 (peer reconciliation)
- `reports/round-42/cov/C08-verify.md` §2.3 (row contract + insertion geometry), §5 (**FINDING D1**,
  S2, with the red/green/negative-control table), §3 (lot draw C02/C03)
- `reports/round-42/cross/X01-trades.md` T7 (the vector defect); `reports/round-42/scribe/S01-integration-draft.md:76-77`
  (baseline census), `:318-320` (**S01's own correction**: "The C06 mission's vector bytes are
  arithmetically wrong; use `25/27/25/29/24/94`"), `:503-504` and `:609-610` (the corrected target
  state, with the mission literal quoted only as the wrong figure)
- Landed executor fragments (digests in §7): `reports/round-42/cov/C01-entry-1.md:3` (now declared
  `mineral-stone-symbolism.md`; `:21` the spare note), `C02-entry-2.md:9` (declared
  `purity-pollution-systems.md`), `:220-221` (C02's own D1 correction), `C03-entry-3.md:9` (declared
  `sacred-topography-pilgrimage.md`), `C04-entry-4.md:5` (declared `mineral-stone-symbolism.md`; `:23`
  its filename section)
- `corpus/README.md` pinned bytes: `:1,3` (duplicated H1), `:5-13` (rev 2.3), `:15,33,35` (carried
  defects), `:168,196,222,249,281,308` (headers), `:197` (blank), `:198-220` (23 rows), `:405`,
  `:532` (totals), `:534-537` (counts footer block), `:538-546` (superseded paragraph), `:547-563`
  (dated index paragraphs; 563 last). Read at sha256
  `d2eed26b30e8e62189d95446dae7d5503b6c6a398bb8e77348f878c947a5ac4f` (563 lines / 137,411 bytes)
- `reports/round-28/readme/sweep.py:28-30` (read-only docstring), `:45-57` (LANE/README/KNOWLEDGE
  constants + `PARTS` section order), `:60,61,74-79` (row/topic contract), `:76,257,284,397,421` (the
  only `open()` sites — writes confined to selftest synthetic trees); instrument sha256
  `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`; row contract pinned by r39 C06
  (`reports/round-39/cov/C06-delta-receipt.md:30-38,237-377,394-414`)
- Filed precedent: `reports/round-40/cov/C06-delta-receipt.md` §1–§8 (the r40 delta, its generator and
  its vector order rule at `:93-95`), `reports/round-35/cov/C11-readme-delta.md` (generator ancestor),
  `reports/round-37/op/defect-queue.json:242-251` (`readme-prediction-vs-delivery`), `:103-131`
  (`R36-README-DUPLICATE-HEADING`), `SCORECARD.md:681-684` (r35 placeholder root cause)
- Commands run (2026-10-19, lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`,
  HEAD `ac47c78`): `git rev-parse HEAD`; `git status --porcelain`; `git rev-parse
  HEAD:corpus/knowledge`; `git ls-tree -r --name-only 55d7c890… | sort | sha256sum`; `find
  corpus/knowledge -name '*.md' -type f | sort | sed 's|^corpus/knowledge/||' | sha256sum`;
  `sha256sum corpus/README.md reports/round-28/readme/sweep.py`; `wc -lc corpus/README.md`;
  `grep -n '^## \|Total knowledge entries\|^Counts checked\|^(total '` corpus/README.md; the
  `claims.json:23` census loop + myth-symbol-only count + `find | wc -l` (§2.1); `python3 -B
  tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → totals.files 220
  (exit 0); `python3 -B reports/round-28/readme/sweep.py` → green 220/220 exit 0; `--selftest` →
  12/12; the three-entry row-contract check (§2.2, 3/3 MATCH); generator no-op on the live tree;
  synthetic 4-probe rig: anchors 197/213/213/220, `--apply` + redirected sweep 224/224 exit 0, three
  negative controls exit 1 (`missing_from_index 1`; `totals_ok False`; `FOOTER_DIR_TOTALS`);
  the §8.1 A-block at the before state (RED, §8.1 output) and on the clean applied lane (GREEN);
  fence/row digest extraction (§7 values) over all five fenced drafts; §5.4 Run A (3 real slugs +
  probe) generator dry-run + `--apply` + redirected sweep → **224/224 exit 0**, and Run B (the three
  distinct landed slugs) → **26 files / 223**; sort-position probes for the candidate slugs;
  `ls`/`find` polls of `reports/round-42/**` (Addendum timestamps)
- Scratch (disposable, not evidence): `.scratch/c06/readme-delta.py` (source = r39 §5.1, 3-line
  diff), `.scratch/c06/synth/`, `.scratch/c06/synthlane/`, `.scratch/c06/appliedlane/`,
  `.scratch/c06/sweep-synth.py`, `.scratch/c06/sweep-applied.py`, `.scratch/c06/ablock.py`,
  `.scratch/c06/neg{1,2,3}.md`
