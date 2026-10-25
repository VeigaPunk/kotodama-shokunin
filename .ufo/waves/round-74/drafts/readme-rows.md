# corpus/README.md patch spec — round 74, claim C `INDEX` leg

- **seat:** `ScribeReadmeIndex` (leaf). **lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- **pinned base:** `f7104cbce186bc2e1522abf0cfd619cc834628bb` (`git rev-parse HEAD`).
- **`corpus/README.md` at base:** `sha256 52fd7536e1bf41ff019115e7c9e37eb15fb64e44d06c5f299fdcc7443a433d91`,
  777 lines. **Not edited by this seat.**
- **authority for the row bodies:** the two final entry drafts, read at
  `22:03:36` / `22:04:19` on 2026-10-25:
  `.ufo/waves/round-74/drafts/worldbuilding-setting-practice.amend-2026-10-23.md` and
  `.../worldbuilding-setting-practice.md`. Their `- topic:` lines are the single
  authority; every byte below was produced by the filed sweep's own
  `topic_of()` (`reports/round-28/readme/sweep.py`, sha256 `9b2ccac0…cdd3`),
  never typed by hand.
- **graded leg (this file is built to satisfy it):** `INDEX` — exactly one row
  per adopted entry in the culture-material section, body = the entry's own
  `- topic:` text verbatim under the `` - `name.md` — `` prefix; the **last**
  `Counts checked` footer's total = `find corpus/knowledge -type f -name '*.md' | wc -l`
  (249 at lands) with the per-directory vector equal to the six partition counts;
  older footers byte-identical.

**Three edits, one file, append/insert only** — no existing byte is edited,
re-ordered or deleted: (a) two rows inserted inside `## culture-material/`, after
base line `:444`; (b) one Known-gaps bullet inserted after base line `:730`;
(c) one footer block appended at EOF (after base `:777`).

⚠ **The previous version of this file is stale.** Its amendment row read
"…and the **schedule on which he releases the world's rules** to the reader…";
the entry was rewritten at `22:03:36` and its `- topic:` now reads "…and the
**tolerance he states for when a serial releases the world's rules**…". The rows
in §1 are re-derived from the current bytes. Re-derive again at landing (§1.3).

---

## 1. (a) The two index rows

### 1.1 Exact text (paste verbatim, one physical line each)

```
- `worldbuilding-setting-practice.amend-2026-10-23.md` — the build order one Chinese web-fiction author reports using for a world-view, the derivation discipline that order implies, and the tolerance he states for when a serial releases the world's rules — recorded as his practice, with the interviewers' framing separated from his answers.
- `worldbuilding-setting-practice.md` — the Japanese practitioner craft of specifying a setting, framed against a Russian-language monograph's account of constructed worlds: a five-step build order, a four-layer causal chain from environment to individual experience, five elements a setting must supply, the five sections and four fields of the settings note, two sub-sheets (a country, a magic or technology system), and the single-source discipline that keeps a long work consistent
```

Shape facts (measured): prefix `` - `name.md` — ``; em dash U+2014 with one
space either side; one physical line each; row 1 is 341 characters / 345 bytes
and ends with the entry's own full stop, row 2 is 485 characters / 487 bytes and
takes no added full stop (its `- topic:` has none).

### 1.2 Insertion point (verified at base with `grep -n`)

| fact | command | base output |
|---|---|---|
| last row of the culture-material section | `grep -n '^- `writing-media-surface-economy.md`' corpus/README.md` | `444:` |
| the next heading (section end) | `grep -n '^## synthesis/ (29)$' corpus/README.md` | `445:` |
| section heading (left stale on purpose) | `grep -n '^## culture-material/ (36)$' corpus/README.md` | `407:` |

**Insert after line `:444`**, i.e. between `writing-media-surface-economy.md`
and `## synthesis/ (29)`. Both rows stay inside the section, which is what the
`INDEX` leg reads (`README_SECTION_RE` / `README_ROW_RE` are section-scoped).

*Ordering note (measured, not asserted):* strict filename order would put the
pair **before** `writing-media-surface-economy.md` (`wo` < `wr`), i.e. after
`:443` (`warrior-material-culture.md`). The instruction places them after the
last existing row; the graded instrument is order-agnostic (`reports/round-28/readme/sweep.py`
collects rows and compares sets — verified: the round-74 'simulation reports
`topic_mismatch 0` and 1 row per entry either way). If the lander prefers strict
filename order, insert after `:443` and swap the two rows' relative order is
irrelevant; nothing measured changes.

*Do not repeat round 73's mistake:* the round-73 rows were appended in a
trailing `## Round 73 additions` block **outside** any `## <part>/ (N)` section,
so the section-scoped instrument still reports `conlang-scholarship.md` and
`conlang-scholarship.amend-2026-10-23.md` as **missing** (and as `orphan_rows`
attributed to `civilizations`). Rows belong inside the section. For the same
reason the appended block in §2 carries **no row-shaped line**.

### 1.3 Re-derivation command (run at landing over the landed entries)

```sh
python3 -B - <<'PY'
import importlib.util
spec = importlib.util.spec_from_file_location('sweep', 'reports/round-28/readme/sweep.py')
sw = importlib.util.module_from_spec(spec); spec.loader.exec_module(sw)
for f in ['corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md',
          'corpus/knowledge/culture-material/worldbuilding-setting-practice.md']:
    print('- `%s` — %s' % (f.rsplit('/', 1)[1], sw.topic_of(f)))
PY
```

If that output differs from §1.1 by even one character, the entry moved after
this draft: paste the command's output, not §1.1.

---

## 2. (b) The appended footer block (exact text, at EOF after base `:777`)

Shape copied from the file's existing last footer (`:775` `Total knowledge
entries:` + `:777` `Counts checked …` single-line form), with the totals on the
same `Counts checked` line so that any "last footer" reader — line-scoped or
block-scoped — sees the total and the vector.

```
## Round 74 landing (appended 2026-10-25, hyaku run 7)

Two culture-material files landed (claim C; assimilation of the shokuknow
`merge/kotodama` worldbuilding-setting-practice theme):
`worldbuilding-setting-practice.md` and
`worldbuilding-setting-practice.amend-2026-10-23.md`. Their rows are in the
`## culture-material/` section above, each carrying its entry's own `- topic:`
text verbatim under the `` - `name.md` — `` prefix (this block deliberately
carries no row-shaped line, so no row is attributed outside a partition). The
`## culture-material/ (36)` heading is left as filed and named as stale: the
live directory holds 40 files and the section 38 rows. Registry: 804 -> 808
rows (four new rows, S881-S884 by the round-74 document map, used-by exactly the
two files above; census receipts under `reports/round-74/telemetry/`). Two
culture-material files remain unindexed and are named rather than claimed
closed: `heritage-taxonomy-models.md` and
`heritage-taxonomy-models.amend-2026-10-24-r13.md`.

Total knowledge entries: 249.

Counts checked 2026-10-25 from the repo root: `find corpus/knowledge -type f -name '*.md' | wc -l` (total 249 files; directory totals 32/29/40/29/24/95).
The two older footers above (the pre-round-73 reading and the round-73 landing
reading) are kept byte-identical as the dated record they were; this block is
the live reading, and `reports/round-28/readme/sweep.py` still parses the first
one, so its own totals legs stay red until a successor instrument names the
authoritative footer. The inventory command
`python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
counts markers, not verified facts.
```

Numbers in the block are substituted at lands, never asserted here: `249` =
`find` at lands, and `32/29/40/29/24/95` = the six partition counts at lands
(base `32/29/38/29/24/95` measured by `find` per partition, `+2` culture-material).

---

## 3. (c) The Known-gaps append

Anchor: insert **after base line `:730`** (the `- Round 65 adds
\`games-play-sport-contests.md\` …` bullet, the section's last line), before the
blank line and the `:732` footer. Verified by
`grep -n '^- Round 65 adds' corpus/README.md` → `730:`.

```
- Round 74 adds the culture-material entry `worldbuilding-setting-practice.md`
  (the Japanese practitioner craft of specifying a setting: a five-step build
  order, a four-layer causal chain from environment to individual experience,
  five elements a setting must supply, the settings note's five sections and
  four fields, and two sub-sheets) and its amendment
  `worldbuilding-setting-practice.amend-2026-10-23.md` (one Chinese web-fiction
  author's build order, the derivation discipline it implies, and the tolerance
  he states for when a serial releases the world's rules). At the pinned base
  `f7104cb` the theme had 0 filename owners and 0 registry rows naming the
  theme's venues. Partial one-way owners remain
  `synthesis/coupling-model.md`, `synthesis/consistency-verification-checklist.md`,
  `synthesis/worldbible-integration-contract.md`,
  `culture-material/cartography-and-mapmaking.md` and
  `linguistics/naming-systems.md`; the entries cite them without restating them,
  and neither entry claims a universal build order or any world's canon.
```

The 0-owner / 0-row clause and the five partial-owner paths are this seat's
measurements at base (see §5), not a quotation of the gap-sweep draft. Keep
whatever the lander re-derives; if the counts move, the bullet moves with them.

---

## 4. Check script — `grep`/`find` one-liners, before → after

Run from the repo root. `BEFORE` = pinned base `f7104cb`. `AFTER` = the lands
tree. Every `AFTER` value below was measured on a simulated lands tree (§5), not
predicted.

```sh
# 1. files on disk
find corpus/knowledge -type f -name '*.md' | wc -l
# BEFORE 247   AFTER 249

# 2. per-partition vector (six lines, canonical order)
for d in linguistics myth-symbol culture-material synthesis verification civilizations; do
  find corpus/knowledge/$d -maxdepth 1 -name '*.md' -type f | wc -l; done
# BEFORE 32 29 38 29 24 95   AFTER 32 29 40 29 24 95

# 3. the two rows exist exactly once each
grep -c '^- `worldbuilding-setting-practice.md` — ' corpus/README.md
# BEFORE 0   AFTER 1
grep -c '^- `worldbuilding-setting-practice.amend-2026-10-23.md` — ' corpus/README.md
# BEFORE 0   AFTER 1

# 4. the rows sit inside the culture-material section (heading unchanged at :407)
grep -n '^## culture-material/' corpus/README.md
# BEFORE 407:## culture-material/ (36)   AFTER 407:## culture-material/ (36)

# 5. the new footer's tokens exist exactly once; the older ones still exactly once
grep -c '^Total knowledge entries: 249\.$' corpus/README.md
# BEFORE 0   AFTER 1
grep -c '(total 249 files; directory totals 32/29/40/29/24/95)' corpus/README.md
# BEFORE 0   AFTER 1
grep -c '^Total knowledge entries: 243\.$' corpus/README.md
# BEFORE 1   AFTER 1     (byte-identical: untouched)
grep -c '^Total knowledge entries: 247\.$' corpus/README.md
# BEFORE 1   AFTER 1     (byte-identical: untouched)
grep -c '(total 243 files; directory totals 30/29/36/29/24/95)\.$' corpus/README.md
# BEFORE 1   AFTER 1
grep -c 'Counts checked 2026-10-25 from the repo root: .*total 247 files; directory totals 32/29/38/29/24/95' corpus/README.md
# BEFORE 1   AFTER 1

# 6. three footers, in file order; the LAST one is the live reading
grep -n '^Counts checked ' corpus/README.md
# BEFORE 734, 777   AFTER 751, 794, 815
#   (the older two shift down by the 15 known-gaps lines inserted above them;
#    their text is unchanged — that is what "byte-identical" means here, not
#    "same line number"; the new EOF line is the last one)
grep '^Counts checked ' corpus/README.md
# the last printed line must contain: (total 249 files; directory totals 32/29/40/29/24/95).

# 7. the appended block adds no row-shaped line (so no orphan rows)
grep -cE '^- `[a-z0-9.-]+\.md` — ' corpus/README.md
# BEFORE 245   AFTER 247      (+2 = exactly the two new rows)
# (the bare pattern '^- `' counts 246 / 248: it also catches the Known-gaps
#  bullet `- \`python3 tools/replay-frozen.py …\`` at :627, which is not a row)
```

Beyond the `grep`/`find` list, because `grep` cannot prove **byte** equality
between a row and its entry's `- topic:` text: run §1.3 and diff its output
against the two rows in the file (any difference is the `REWRITE` class the
sweep names).

---

## 5. Simulation receipts (measured, 2026-10-25)

Simulated lands = the lane's `corpus/knowledge` copied to
`/tmp/ScribeReadmeIndex/r74/knowledge` (247 files) + the two entry drafts copied
into `culture-material/` (249 files) + this patch applied to the README bytes
(script `/tmp/ScribeReadmeIndex/r74_patch.py`, scratch only). Measured by the
filed sweep and by the `INDEX` predicates:

```
files on disk: 249
sweep: parts {"civilizations": 95, "culture-material": 40, "linguistics": 32,
              "myth-symbol": 29, "synthesis": 29, "verification": 24}
       rows 247 files 249
       missing_from_index 4  (heritage-taxonomy-models.md + its .amend-2026-10-24-r13,
                              conlang-scholarship.md + its .amend-2026-10-23)
       orphan_rows 2         (the two round-73 rows in the trailing block)
       topic_mismatch 0
       header_drift {"culture-material": {"declared": 36, "files": 40},
                     "linguistics": {"declared": 30, "files": 32}}
       totals_line 243       (the sweep parses the FIRST footer — see §6.1)
       readme_sha256 0531f7a3d16bee20329c9b042eb865be13bb6c54e4e5a158a2f864f3eae3708e

INDEX predicates:
  worldbuilding-setting-practice.md              rows: 1  verbatim: True
  worldbuilding-setting-practice.amend-…-23.md   rows: 1  verbatim: True
  culture-material rows 38 / files 40
  Counts-checked lines: 3 ; last footer total 249 ; vector 32/29/40/29/24/95
  live per-dir: 32/29/40/29/24/95
  older tokens present exactly once each:
    'Total knowledge entries: 243.' / 'Total knowledge entries: 247.'
    '(total 243 files; directory totals 30/29/36/29/24/95).' / '(total 247 … 32/29/38/29/24/95'
```

Controls run on the same simulation (the green must be able to fail) — `C0` is the
unmodified patch and the sweep's `ok False` is expected, since the sweep is not
the `INDEX` instrument:

| control | perturbation | measured |
|---|---|---|
| C0 | none | sweep `ok False` (missing 4, rows 247); `INDEX` predicates all green |
| C1 | amendment row paraphrased | sweep names `culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` in `topic_mismatch` (`REWRITE`) |
| C2 | base row deleted | `missing_from_index` grows 4 → 5, rows 247 → 246 |
| C3 | footer vector perturbed to `32/29/38/…` | sweep unchanged (it parses the first footer), but the last-footer predicate reads `249 32/29/38/29/24/95` — i.e. the predicate fails on the perturbed bytes |
| C4 | the two rows swapped | no finding of any kind (order-agnostic, as stated in §1.2) |

---

## 6. Hazards the lander must not trip on

1. **Two footers, two instruments.** `reports/round-28/readme/sweep.py` parses
   the **first** `Counts checked` block (`FOOTER_RE`, `re.search`) and the first
   `Total knowledge entries:` line, so it will report `FOOTER_TOTAL 243 vs 249`
   and `totals_ok False` at lands no matter what this patch does. The `INDEX` leg
   is defined against the **last** footer. Both statements can be true at once;
   do not "fix" the sweep by editing the older footer, and do not claim the sweep
   is green.
2. **Stale headings stay stale.** `## culture-material/ (36)` and
   `## linguistics/ (30)` are false at base and remain false at lands. This spec
   does not edit them (append-only landing, round-73 precedent) and names them in
   the appended block instead. Editing a heading in place would be a rewrite of
   filed history; if the round wants the headers true, that is a separate,
   explicitly authorized repair.
3. **Four files stay unindexed after this patch** (the two
   `heritage-taxonomy-models` files, the two round-73 `conlang-scholarship`
   files — the latter present but outside any partition section). The `INDEX` leg
   grades only the round-74 entries, so this does not fail it; the appended block
   names the deficit rather than claiming the index is complete.
4. **The entries can still move.** The amendment's `- topic:` changed at
   `22:03:36`, after the previous draft was written. Re-derive (§1.3) and paste
   the command's output.
5. **Do not put rows in the appended block.** A row-shaped line outside a
   `## <part>/ (N)` section is exactly what makes the two round-73 rows invisible
   to the section parser (§1.2).

---

## 7. What this seat did not do

- Did not edit `corpus/README.md`, either entry, `corpus/SOURCES.md`,
  `reports/round-74/claims.json` or any other file outside the two paths named in
  the assignment; no commit, no index operation, no dispatch, no message.
- Did not run `reports/round-74/accept-c.py` (absent: only
  `.ufo/waves/round-74/counters/accept-c.py` exists, a draft that defines
  `README_SECTION_RE`/`README_ROW_RE` but has no `INDEX` implementation yet).
- Did not adopt, judge or re-score any source or entry; the registry count
  `804 -> 808` in §2 is the claim's own ROWS leg (four rows S881-S884), quoted as
  plan, not measured by this seat.
- Scratch: `/tmp/ScribeReadmeIndex/r74_patch.py`, `/tmp/ScribeReadmeIndex/r74/`
  (copy of `corpus/knowledge` at 249 files, patched `README.md`).
