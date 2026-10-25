
## Post-wave update

### Round 74 (2026-10-25) — `INDEX` leg: README patch spec rewritten

Assigned by the L1 follow-up: claim C now carries a graded `INDEX` leg
(`reports/round-74/claims.json`; `.ufo/waves/round-74/w1/RevClaimsFidelity.md` F7),
and `.ufo/waves/round-74/drafts/readme-rows.md` had to be rewritten as an exact
patch spec. **Delivered**; `corpus/README.md` again **not** edited (measured
before and after: `sha256 52fd7536…433d91`, `git diff --stat` empty).

- **Base:** `f7104cbce186bc2e1522abf0cfd619cc834628bb`. `find corpus/knowledge
  -type f -name '*.md' | wc -l` = **247**; per-partition **32/29/38/29/24/95**;
  README 777 lines, two footers (`:732`/`:734` reading 243, `:775`/`:777` reading 247).
- **(a) rows** — derived by the filed sweep's `topic_of()` from the two final
  entry drafts (read `22:03:36` / `22:04:19`), inserted **after base line `:444`**
  (`grep -n '^- `writing-media-surface-economy.md`'` → `444:`), inside the
  `## culture-material/` section, 341 and 485 characters, one physical line each.
  The previous draft's amendment row was **stale**: the entry was rewritten at
  `22:03:36` and its `- topic:` now says "the tolerance he states for when a
  serial releases the world's rules" where the old draft said "the schedule on
  which he releases … to the reader". Re-derived, not patched.
- **(b) footer** — one block appended at EOF after base `:777`, in the existing
  last-footer shape: `Total knowledge entries: 249.` plus one
  `` Counts checked 2026-10-25 from the repo root: `find …` (total 249 files;
  directory totals 32/29/40/29/24/95). `` line, so any last-footer reader —
  line- or block-scoped — sees both tokens. Older footers untouched (each old token still occurs exactly
  once).
- **(c) Known-gaps** — one bullet inserted after base `:730` (the round-65
  bullet, `grep -n '^- Round 65 adds'` → `730:`), in the round-64..67 shape, with
  the 0-owner / 0-registry-row pre-state measured at base (`find
  corpus/knowledge -iname '*worldbuilding*'` → 0, `*setting-practice*` → 0,
  `grep -cE 'litmemo\.com|tuduku\.space|chinawriter\.com\.cn' corpus/SOURCES.md`
  → 0) and the five partial-owner paths existence-checked.
- **Check script** — a `grep`/`find`-only one-liner list with BEFORE (measured at
  base) and AFTER (measured on the simulation) values, plus the honest exclusion
  of the bare prefix pattern `^- ` (which also catches the Known-gaps bullet
  beginning `` - `python3 tools/replay-frozen.py …` `` at `:627`).

**Measured on a simulated lands tree** (`/tmp/ScribeReadmeIndex/r74`: 247
committed files + the two entry drafts = 249; scratch script `r74_patch.py`):
`INDEX` predicates all green — 1 row per adopted entry, body verbatim `True` for
both; last footer total `249`, vector `32/29/40/29/24/95` = live per-dir; older
footer tokens each still once. Sweep on the same bytes: `rows 247 files 249`,
`missing_from_index 4`, `orphan_rows 2`, `topic_mismatch 0`,
`header_drift {culture-material 36 vs 40, linguistics 30 vs 32}`,
`totals_line 243` — the sweep parses the **first** footer, so it stays red by
construction and is not the `INDEX` instrument. Controls: paraphrase → `REWRITE`
named; delete → `missing` 4→5; perturb the new vector → last-footer predicate
reads the perturbed value; swap the two rows → no finding (order-agnostic).

**Hazards recorded for the lander:** the round-73 rows were appended in a
trailing `## Round 73 additions` block **outside** any partition section, so the
section-scoped instrument still counts them as missing and as `orphan_rows`
attributed to `civilizations` — this spec therefore inserts no row-shaped line in
the appended block; the stale `## culture-material/ (36)` / `## linguistics/ (30)`
headings stay as filed and are named, not silently fixed; four files remain
unindexed after this patch and are named in the block.

Boundaries honoured again: no edit to `corpus/README.md`, the entries, the
registry, `claims.json`, `SCORECARD.md`, `LOG.md`, `SKILL.md` or any other path;
no commit, no dispatch, **no message to `KotodamaR74` or any other seat**; did not
run `reports/round-74/accept-c.py` (absent; only the draft counter
`.ufo/waves/round-74/counters/accept-c.py` exists, and it defines
`README_SECTION_RE`/`README_ROW_RE` but no `INDEX` implementation). No tool
installed, no network fetch.
