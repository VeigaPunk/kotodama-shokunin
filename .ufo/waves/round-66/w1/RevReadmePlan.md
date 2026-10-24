# RevReadmePlan — review of the round-66 corpus/README.md delta (claim C)

Seat: `RevReadmePlan` (L1-kotodama-r66.RevReadmePlan). Review only: no lane byte written, no
git/jj write, no tool installed. Base `94209e8f80969dbac48d56c5d0e2e623635b8616`; `git diff <base>
-- corpus/README.md` = 0 lines; `sha256(corpus/README.md)` =
`0c04517bcd485feb64b283d934db2037552f5d771449374a5a36f9cb3b26d3e7` (matches the plan's stated base
hash; working tree clean for that path).

Artifact reviewed: `.ufo/waves/round-66/stage/readme-plan.md` + `readme-plan.diff` +
`_readme-build/{README.orig.md,README.new.md,readme.diff}` (regenerated at 08:36-08:37; all
measurements below are against those current bytes), cross-checked with
`stage/entry-spec.md:72` (topic) and the committed `corpus/README.md`.

Verdict on the three asked questions: **count math right; index row carries the frozen topic text
verbatim; footer date/command match as filed** — with one MEDIUM instrument defect that the delta
passes only by working around, and one LOW records inaccuracy in the frontier bullet. Details and
residual risk below.

## Findings

### MED-1 — `accept-c.py` TOPIC leg is an order-dependent first-match, and the delta passes only because revision 2.18 writes the entry without `.md`

- Instrument: `reports/round-66/accept-c.py:318-321` selects
  `row = next(l for l in rtext.splitlines() if ENTRY.split("/")[-1] in l)` and then requires
  `tline[len("- topic:"):].strip() in row`. Any line above the index that contains
  `scent-perfume-aromatics-codes.md` captures the match.
- Demonstrated unsound on existing bytes: for the round-65 entry the first README line containing
  `games-play-sport-contests.md` is `corpus/README.md:4` (revision 2.17 prose), so the leg reads
  False even though `corpus/README.md:390` carries the exact topic. Reproduced line-for-line
  (topic length 289): `first-match PASS? False`, anchored PASS? True.
- The round-65 counter anchored the row shape instead —
  `reports/round-65/accept-c.py:449-450`, `if l.startswith("- \`games-play-sport-contests.md\`")` —
  which is immune to revision/bullet prose.
- How the reviewed delta passes: `readme-plan.md:17-18, 64-79, 90-96` and `entry-spec.md:337` require
  hunk 1 to name the entry **without** the `.md` suffix. Measured on `README.new.md`: stem hits at
  lines 4, 405 (index row), 699 (frontier bullet); first full-basename hit is 405, so
  `TOPIC PASS? True`. Negative control (`.md` re-inserted into the revision note) → `TOPIC PASS?
  False`. The plan discloses this ("The TOPIC trap, measured both ways", `readme-plan.md:64-79`,
  Finding 4) and is consistent with `entry-spec.md` §5 R1.
- Defect: revision 2.18 becomes the only one of the file's 11 explicit "entry landed
  (`` `…` ``" sentences that names the file without `.md` (measured: `grep -o 'entry landed
  (\`[^\`]*\`' corpus/README.md` → 11 matches, all ending `.md\``); the pass depends on that
  spelling. A later normalization of the block to the
  convention every prior block follows (`games-play-sport-contests.md`, `headgear-head-…md`, …) flips
  `ACCEPT-C-66` to FAIL while the index row is correct. The record is being written to dodge a
  scanner rather than the scanner being pinned to the row.
- Recommended fix (instrument, not the delta): anchor TOPIC to the index-row shape
  `^- \`<basename>\` — `, assert exactly one such row, and add a positive leg that revision 2.18
  names the file *with* `.md` (so the leg cannot be satisfied by omitting the file from the record).
  Then `entry-spec.md` §5 R1's no-`.md` requirement can be dropped.

### LOW-1 — frontier bullet misattributes a scent scope to `bathing-and-body-hygiene.md` and enumerates partial owners as if complete

- `readme-plan.md:125` / hunk 4: `` `culture-material/bathing-and-body-hygiene.md` (perfumed
  bathing) ``; the supporting census at `readme-plan.md:36` cites "`:3` scent in the bath register".
  Measured: line 3 (`- topic:` line) contains no `scent|perfume|incense|aromatic|unguent` token; the
  file's only `scent` token is `bathing-and-body-hygiene.md:7`, in a cross-reference that assigns
  "*the adorned* surface — paint, scent, hair" to `adornment-body-codes.md` and reserves the washing
  regime for itself. The bath file's own scent-adjacent content is "oil and strigil" (bath
  implements), not perfumery. The `:3` citation is wrong and the parenthetical overstates another
  entry's scope.
- Omitted `incense` owners (files containing `incense`, word-bounded): `civilizations/arabia-pre-
  islamic.md:122` ("incense/spice commerce", the closest partial owner of the entry's trade-route
  clause), `civilizations/maya-classic.md` (*ch'aaj*, blood-or-incense), `civilizations/
  zapotec-mixtec.md` (incense pouch in a costume inventory), `myth-symbol/
  death-afterlife-eschatology.md` (incense as a transfer medium). The bullet lists seven files with
  no "e.g." qualifier and reads exhaustive.
- Fix: drop the bathing parenthetical or re-word to "oil and strigil in the bath (`:3`, `:7`)";
  add `civilizations/arabia-pre-islamic.md:122`, or mark the list non-exhaustive. (The deliberate
  exclusion of `craft-artisan-lexicon.md` — four *nioi* hits — is correct and stays.)

### INFO-1 — footer `Counts checked` date/command: matches, with two stated caveats

- Date `2026-10-24` (`corpus/README.md:695`) is the round's declared date and today's measurement
  date: correct as filed. It is not machine-validated (the sweep parses the date but does not judge
  it; `accept-c.py` never reads it). If integration crosses local midnight, the footer must be
  re-dated with the re-measure.
- Command unchanged (`:696`). Re-ran both modes: `--json --summary` reports `totals.files 239` at
  base and `240` on a post-landing tree (paths included); the six per-directory counts are printed
  directly only in text mode, alphabetically (`civilizations 95, culture-material 33, linguistics 30,
  myth-symbol 29, synthesis 29, verification 24`). The README's parenthetical is in **section**
  order (`linguistics…civilizations`) — that order is the README convention and is pinned by the
  sweep's footer leg, not by the command's output order. Hence the vector is reproducible but not
  printed in that order by the named invocation; keep `reports/round-28/readme/sweep.py` as the
  reverify (it prints `footer_live {"total": 240, "dir_totals": [30, 29, 33, 29, 24, 95], "order":
  [...]}`). No change required.

### INFO-2 — the plan's end-state self-check is not re-runnable from the filed artifacts (delta itself is sound)

`stage/_readme-build/tree/` no longer exists, so the plan's `ok True rows 240 files 240 …` line
cannot be replayed as filed. Independently reproduced with a copied 239-file `corpus/knowledge` plus
a stub `scent-perfume-aromatics-codes.md` whose `- topic:` is the row payload, swept with
`reports/round-28/readme/sweep.py`'s own `sweep(readme_text, root_override=…)`:

    ok True | parts culture-material 33 | rows 240 files 240 | totals_line 240
    footer_ok True | footer {"date": "2026-10-24", "total": 240, "dir_totals": [30,29,33,29,24,95]}
    topic_mismatch [] | orphan_rows [] | header_drift {}

Against the unmodified live tree the same README reads `ok False`, `rows 240 files 239`,
`orphan_rows ['culture-material/scent-perfume-aromatics-codes.md']`,
`header_drift {'culture-material': {'declared': 33, 'files': 32}}`, `FOOTER_TOTAL 240 vs 239` and
`FOOTER_DIR_TOTALS [30,29,33,29,24,95] vs [30,29,32,29,24,95]` — exactly the plan's stated
pre-landing residual, i.e. the only missing byte is the entry itself.

## Verified correct (measured, not asserted)

| Check | Measurement |
|---|---|
| Culture-material count math 32 → 33 | live `ls corpus/knowledge/culture-material/*.md` = 32; header `corpus/README.md:373` is a single occurrence of `(32)`; post-landing sweep declares 33 with 33 files |
| Corpus count 239 → 240 | parts 30/29/32/29/24/95 = 239 now; 30/29/**33**/29/24/95 = 240 after; `Total knowledge entries:` only at `:693`; date/vector line at `:697`; the only other `239` in the file is the historical revision 2.17 record (`:10`), correctly untouched |
| Index row placement | filename sort puts `scent-perfume-aromatics-codes.md` between `ritual-garments.md` (`corpus/README.md:398`) and `sumptuary-law-rank-display.md` (`:399`) — confirmed by sorted neighbour probe; row emitted at `README.new.md:405` between them |
| Row text verbatim | plan row payload == `entry-spec.md:72` payload, 367 chars, byte-equal (compared with the sweep's own normalization); `ROW_RE` shape `` - `name.md` — text `` (U+2014, one space each side) matches `reports/round-28/readme/sweep.py:60` |
| Diff integrity | plan embeds exactly 1 diff block, byte-identical to `readme-plan.diff` (12218 chars, 4 hunks); `git apply --check` exit 0; `patch -p1` on a copy of the committed README reproduces `README.new.md` byte-identically (`cmp`) |
| README gates on the new file | `tools/check-readme-revisions.py --readme <new>` findings 0 (1 carried `REVISION-ORPHAN` at lines 195/206, pre-existing); `tools/check-readme-heading.py --readme <new>` findings 0; labels `2.18 … 1.3` non-increasing |
| Base census claim | claim C's command on the base prints `0` filename owners |
| Footer total re-derivation | inventory on post-landing tree: `totals.files = 240`, `INFO directory culture-material: files=33` |

No other count-bearing line in `corpus/README.md` needs to move: the only other `239`/`32`
occurrences are dated historical revision/superseded text (`:10`, `:700`, and the 2.16/2.11 blocks),
which must stay as written.

## Residual risk / verification gaps

1. The entry file does not exist yet. Row↔entry equality is asserted against `entry-spec.md:72` and
   will be re-checked by `sweep.py` at integration. If the builder's `- topic:` differs, the plan's
   TOPIC-SYNC snippet (`readme-plan.md:165-176`) must run; it rewrites exactly one row and leaves
   the revision note alone (I read it, did not execute its write path inside the lane).
2. MED-1 is latent, not active: with hunk 1 as filed, `ACCEPT-C-66`'s TOPIC leg measures True. The
   risk is a later "convention repair" of revision 2.18; if the L1 keeps the no-`.md` spelling, the
   load-bearing note should be carried into the round's records (lesson/telemetry), not only this
   stage draft.
3. "0 whole-register topic owners" in the revision note and frontier bullet is a judgment of the
   same class as claim C's support statement; only the filename census is machine-checked.
4. Frontier-bullet owner list is selective by design; see LOW-1 for the two concrete defects
   (unsupported bathing scope, omitted `arabia-pre-islamic` incense-commerce mention).

Tools installed/updated this seat: none.

Report: .ufo/waves/round-66/w1/RevReadmePlan.md
