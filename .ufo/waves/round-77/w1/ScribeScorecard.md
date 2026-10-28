# ScribeScorecard — round 77 wave 1

Leaf seat (no subagents, no background jobs). Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base revision for this round: `211f9526800906e0c585d878d265c37e5e090c15` (`211f952`).
This seat drafted the SCORECARD section and wrote nothing else in the lane.

## Behavior

Produced **one** artifact plus this report:

- `.ufo/waves/round-77/w1/drafts/scorecard-section.md` (38 lines, 5951 bytes) — a draft wrapper paragraph,
  `---`, then the two append-only blocks:
  - `## Axes — round 77 (2026-10-27, hyaku run 10, kotodama), author-side verdicts` — three prose
    paragraphs in the round-76 shape (**Coverage / claim C**, **Calibration / claim Ca**,
    **Depth / operability / freshness / adjacency**), the fenced `sh` counting command, the
    "Observed output:" line, the two inline `Acceptance command:` strings (C and Ca), the Evidence lines,
    the unchanged-axes line with the freshness pause cited to `.ufo/l0-questions.md:47`, and the closing
    verdict-line placeholder.
  - `## Corrections — round 77` — append-only record paragraph, then the four-column header
    `| id | old token | new token | re-derivation command |`, its `|---|---|---|---|` rule, and one
    placeholder row `<L77-NN>` for the L1 to expand from the frozen ledger.

Shape decision and its evidence:

- `SCORECARD.md` round 76 is **prose**, not the 5-column table of rounds 72–75; anchors read with
  `awk 'NR==1509 || NR==1513 || NR==1514 || NR==1540 || NR==1557 {printf "%d|%s\n", NR, substr($0,1,120)}' SCORECARD.md` →
  ```
  1509|## Corrections — round 76
  1513|| id | old token | new token | re-derivation command |
  1514|---|---|---|---|
  1540|## Axes — round 76 (2026-10-27, hyaku run 10, kotodama), author-side verdicts
  1557|Neither frozen acceptance counter passes. The source additions and ledger annotations remain recorded with their failure
  ```
  The draft reproduces that pair: heading text, prose axis paragraphs, fenced counting command + observed
  output line + inline acceptance command (round-76 lines 1542–1553), closing verdict line (line 1557),
  Corrections prose + header + rule. The round-73 accepted combined draft
  (`.ufo/waves/round-73/w2/drafts/scorecard-section.md`) supplied the precedent for the draft wrapper
  paragraph + `---` separator, which the L1 strips on paste.
- The "coverage row / calibration row / unchanged axes line" required by the seat are the three prose
  paragraphs; rounds 72–75 spell the same content as table rows, so if the L1 prefers the table, the
  mapping is 1:1 (`axis | verdict | before → after / observation | re-run command | measured evidence`).
  The draft's own preamble states this is the round-76 prose shape, and states that if Ca lands before C
  the Corrections block is appended first (as rounds 73–76 do) and that neither block binds the other's order.

Placeholder policy: every deferred value is an explicit `<L1-FILL: …>` token (25 occurrences) or the
claims' own `<C-lands>` / `<Ca-lands>` / `<freeze>`. The only measured counts without a fill marker are the
base counts, each produced by the command quoted in the draft and re-run below. Nothing in the draft is a
fabricated verdict: the claims' target (`PASS legs=N/N`) is labelled as a target, and the after-state counts
are labelled "per the claims' target".

## Before→after measurements (draft-time, base revision)

Base counts quoted in the coverage paragraph, produced by the draft's own command re-run verbatim:

```
$ for rev in 211f9526800906e0c585d878d265c37e5e090c15; do
    printf '%s knowledge=' "$rev"
    git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree -r --name-only "$rev" corpus/knowledge | grep -c '\.md$'
    printf '%s rows=' "$rev"
    git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show "$rev:corpus/SOURCES.md" | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  done
211f9526800906e0c585d878d265c37e5e090c15 knowledge=253
211f9526800906e0c585d878d265c37e5e090c15 rows=820
```

- 253 knowledge files — `git -C … ls-tree -r --name-only 211f952… corpus/knowledge | grep -c '\.md$'`.
- 820 registry rows — `git -C … show 211f952…:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`.
- newest registry row S896 (so S897/S898 are the next free ids the claims name) —
  `git -C … show 211f952…:corpus/SOURCES.md | grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' | tail -6` →
  ```
  | S891
  | S892
  | S893
  | S894
  | S895
  | S896
  ```

These agree with the DRAFT's declared before/after (`253 → 254` files, `820 → 822` rows, S897/S898));
the after values are placeholders in the draft because no C-lands commit exists yet.

## Gates (checks run, with raw output)

1. Draft structure (final file):
   ```
   $ grep -n '^## \|^\*\*\|^| id \|^|---\|^```' .ufo/waves/round-77/w1/drafts/scorecard-section.md | cut -c1-90
   11:## Axes — round 77 (2026-10-27, hyaku run 10, kotodama), author-side verdicts
   13:**Coverage / claim C — <L1-FILL: verdict at C-lands; the claims' target is `PASS legs
   15:```sh
   22:```
   26:**Calibration / claim Ca — <L1-FILL: verdict at Ca-lands; the claims' target is `PASS
   28:**Depth / operability / freshness / adjacency — unchanged; no score delta.** These fo
   32:## Corrections — round 77
   36:| id | old token | new token | re-derivation command |
   37:|---|---|---|---|
   ```
   (the closing verdict placeholder on line 30 starts with `<`, so it is outside this grep).
2. Fences balanced: `grep -c '^```' …` → `2` (one open, one close; the `sh` block is the only fence).
3. No `/tmp` in the draft: `grep -c '/tmp' …` → `0`.
4. Required tokens present exactly once unless noted:
   ```
   ## Axes — round 77 :: 1
   ## Corrections — round 77 :: 2
   reports/round-77/accept-c.py :: 1
   reports/round-77/accept-ca.py :: 2
   .ufo/l0-questions.md:47 :: 1
   | id | old token | new token | re-derivation command | :: 1
   |---|---|---|---| :: 1
   ```
   (`## Corrections — round 77` appears twice because the Axes calibration paragraph cross-references the
   block by name; `accept-ca.py` twice for the same reason.)
5. Freshness-pause citation resolves at the fleet root, exactly as the seat specifies:
   ```
   $ sed -n '47p' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md | grep -o 'Freshness axis-move claims are paused until ruled.'
   Freshness axis-move claims are paused until ruled.
   ```
   The row is `kotodama | round-11 | drift-recheck threshold calibration: …` — the open r11 L0 row.
6. Placeholder count: `grep -o 'L1-FILL' … | wc -l` → `25`.

## Findings

- **F1 — the C counter's argv is not in the claims.** CLAIMS-DRAFT names `reports/round-77/accept-c.py`
  and its leg set but prints no command line (the Ca command is printed verbatim). `reports/round-77/`
  at draft time holds only `telemetry/` (`ls reports/round-77/` → `telemetry`; `ls reports/round-77/telemetry/`
  → `census-start.txt`), so no parser could be read. The draft therefore carries the round-76 C argv
  (`--root . --lands <C-lands> --freeze <freeze> --fleet-root … --work …`) and says so inline
  ("inherited pending the frozen round-77 parser"). The L1 should pin the r77 argv when the counter freezes;
  round 73's draft offered an extra `--census-sh /home/vgpnk/Projects/shokunin/scripts/sources-census.sh`,
  so the CLI has drifted across rounds and a silent copy is a real risk.
- **F2 — leg-list hygiene.** The claims' C leg list holds `LEDGELIST?` with a literal question mark while
  the Ca list holds a plain `LEDGELIST`; both say "exact set frozen with the counter". The draft preserves
  the `?` and states the conditional, but the final section must drop the `?` or the leg name once the
  frozen counters' tables are read (the R76-M3 leg-list class the round cites).
- **F3 — the start census receipt carries no row count.** CLAIMS-DRAFT's frontier line says
  `reports/round-77/telemetry/census-start.txt` (exit 0, 820 rows). The committed file is 33 lines
  (`wc -l reports/round-77/telemetry/census-start.txt` → `33`) of W04 duplicate-URL and W01 tier-C lines
  ending `kotodama<TAB>ok<TAB>/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`;
  `grep -n '820\|rows' reports/round-77/telemetry/census-start.txt` prints nothing (`exit=1`) — no row
  count. 820 is true by my independent measurement above, but the receipt does not evidence it, so the
  draft cites the receipt as "start receipt" only and does not attribute 820 to it.
- **F4 — `.ufo/l0-questions.md` is not a lane file.** `ls .ufo/l0-questions.md` in the lane →
  `No such file or directory`; the file lives at the fleet root (`/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`).
  The draft uses the seat's citation `.ufo/l0-questions.md:47` verbatim; a reader resolving it against the
  lane will not find it.
- **F5 — section order.** SCORECARD files `## Corrections — round NN` before `## Axes — round NN` for
  rounds 73–76 (anchors: 1509 before 1540; 1468 before 1501; 1436 before 1455; 1409 before 1426). The
  seat names the Axes block first and the draft follows that order, with the preamble telling the L1 to
  append Corrections first if Ca lands first. Both internal block shapes are round-76's.
- **F6 — base/claims consistency.** The claims' after-state (`253 → 254` knowledge files, `820 → 822` rows,
  document map `row_set`, one admitted entry `corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`)
  is consistent with the base measured here; the draft encodes the targets only as labelled placeholders.

## Unrun checks (reported as unrun)

- The two acceptance counters: `reports/round-77/accept-c.py` and `reports/round-77/accept-ca.py` do not
  exist at draft time (only `reports/round-77/telemetry/` is present), so neither command was executed and
  neither `ACCEPT-C-77` nor `ACCEPT-CA-77` line is quoted anywhere in the draft.
- No C-lands, Ca-lands, freeze or ledger exists yet, so no placeholder was resolved and no verdict written.
- The draft was not pasted into `SCORECARD.md` (out of this seat's write scope).

## Touched surfaces

- Wrote: `.ufo/waves/round-77/w1/drafts/scorecard-section.md`, `.ufo/waves/round-77/w1/ScribeScorecard.md`.
- Created the directory `.ufo/waves/round-77/w1/drafts/` (did not exist).
- No scratch dir created (no clone, fetch or fixture was needed; every read was `git -C <lane> show` /
  `ls-tree` / `ls` and `grep` against the lane or the fleet-root `.ufo/l0-questions.md`). No tool installs.
  No writes to the fleet repo, sibling lanes, `.ufo/state`, `SCORECARD.md`, `LOG.md`, `SKILL.md`, `SHONEN.md`,
  `corpus/**`, `reports/round-76/**`, `reports/round-77/**`, `CLAIMS-DRAFT.md`, git index or jj state.
- Out of scope, untouched: the counters, `claims.json`/`ledger.json`, the census, the lands themselves.
