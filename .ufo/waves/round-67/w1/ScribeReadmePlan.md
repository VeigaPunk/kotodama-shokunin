# ScribeReadmePlan — corpus/README.md index row for the r67 medicine entry

Seat: `L1-kotodama-r67.ScribeReadmePlan` (scribe, claim C). Time-boxed leaf; no
subagents, no repo writes outside `.ufo/waves/round-67/`.
Artifact: `.ufo/waves/round-67/stage/readme-row.txt` (draft + instructions).
No product file was modified; nothing was staged, committed, or pushed; no jj/git
write was run; no tool was installed.

## Behavior delivered

`stage/readme-row.txt` contains, in ready-to-integrate form:

1. The index row, one physical line, in the README's measured grammar
   `- \`medicine-healing-codes.md\` — <topic>` (backticked basename, space EM
   DASH space), plus the topic text it proposes (742 chars).
2. Insertion point: after the `material-culture-inference-method.md` row
   (README line 403), before `music-instrument-lexicon.md` (line 404); the two
   are adjacent, so the new row becomes line 404. Alphabetical sort verified
   (`mate` < `medi` < `musi`).
3. Exactly three count edits, each with before/after text:
   - line 381 `## culture-material/ (33)` → `(34)`
   - line 703 `Total knowledge entries: 240.` → `241.`
   - line 707 `(total 240 files; directory totals 30/29/33/29/24/95).` →
     `(total 241 files; directory totals 30/29/34/29/24/95).`
     (six dir totals are in the README's own section order: linguistics 30,
     myth-symbol 29, culture-material 33→34, synthesis 29, verification 24,
     civilizations 95.)
4. A drafted `revision: 2.19` header block (2.16–2.18 precedent), with the
   registry row-count clause deliberately omitted (not measured by this seat;
   2.17 is the precedent for omitting it).
5. An optional `## Known gaps (frontier)` bullet template, gated on every clause
   being true at integration.
6. Verification commands and expected sweep output.

## Gates / claims touched

Claim C legs `TOPIC` and `SWEEP` (`reports/round-67/accept-c.py:419-431`;
`reports/round-28/readme/sweep.py`). `SWEEP` is the binding leg: it requires
rows == files, header counts == disk, totals line == disk, and the footer's
total + six directory totals == disk, and it compares the row text to the
entry's `- topic:` head-block text (continuations space-joined) with equality.
`TOPIC` is weaker: it substring-tests the first physical `- topic:` line inside
the first `- ` line containing the basename.

## Evidence (measured, not asserted)

Baseline, live lane, read-only:
`python3 -B reports/round-28/readme/sweep.py` → exit 0, `rows 240 files 240`,
parts `{"civilizations": 95, "culture-material": 33, "linguistics": 30,
"myth-symbol": 29, "synthesis": 29, "verification": 24}`, `totals_line 240
totals_ok True`, `footer {"total": 240, "dir_totals": [30,29,33,29,24,95]}`,
`footer_ok True`, `readme_sha256 f6e0cb87…252ce`.

Applied simulation (in-memory README copy + temp knowledge tree whose
culture-material files are symlinks plus a stub entry carrying the proposed
topic; `sweep()` imported as a module with `root_override`):
`ok True`, `rows 241 files 241`, culture-material 34, `missing 0`, `orphans 0`,
`topic_mismatch 0`, `header_drift {}`, `totals_ok True`, `footer_ok True`,
`footer_live {"total": 241, "dir_totals": [30, 29, 34, 29, 24, 95]}`;
culture-material rows 34, sorted True, new row index 21, neighbors
`material-culture-inference-method.md` < `medicine-healing-codes.md` <
`music-instrument-lexicon.md`.

Negative control — full-path row exactly as the wave prompt words it
(`- corpus/knowledge/culture-material/medicine-healing-codes.md — …`):
sweep `ok False`, `missing ['culture-material/medicine-healing-codes.md']`,
`orphans []`. The line is invisible to `ROW_RE`, so it manifests as a MISSING
row, not a ghost → SWEEP fails → ACCEPT-C-67 fails.

Negative control — one-character topic drift (`healer-role` → `healer role`):
`ok False`, one `topic_mismatch` of class `REWRITE`. This is the leg that pins
row ↔ entry byte equality; `TOPIC` alone (prefix substring) would not catch it.

Sort and anchor checks: `grep -n '^- \`material-culture-inference-method.md\`|^-
\`music-instrument-lexicon.md\`' corpus/README.md` → 403 and 404; the three
count anchors each occur exactly once (`\b33\b|\b240\b` hits only lines 8, 9,
381, 703, 707 — lines 8–9 are revision 2.18's own history and must not change).

## Findings

1. **The prompt's row format is not the README grammar.** Writing the row with
   the full path makes it unparseable, not merely mistyped: sweep then reports
   the file as missing from the index (measured above). The in-file convention
   (backticked basename, single line) is the only form that satisfies both
   counters. The draft follows the convention, not the prompt's shorthand.
2. **Dependency: the entry file does not exist yet, so no topic text is
   frozen.** `corpus/knowledge/culture-material/medicine-healing-codes.md` is
   absent; `stage/entry-spec.md` (ScribeEntrySpec) is also absent at report
   time; `rows/` holds only ScoutGapMed and ScoutRow11. The row's topic is
   therefore a **proposal**. The integration contract is: the entry's head
   block carries `- topic:` + the proposed string (wrapping allowed; sweep
   joins continuations), OR the row is regenerated from whatever `- topic:`
   the entry lands with. The row is derived from the entry, never the reverse —
   editing the entry to match a README draft inverts provenance.
3. **`TOPIC` is weaker than `SWEEP` and can pass on a prefix.** Because it reads
   only the first physical `- topic:` line, a wrapped entry topic passes TOPIC
   by substring even if the row's tail is wrong. Do not use TOPIC alone as the
   equality evidence; the sweep `REWRITE` class is the measured binding check.
4. **Count edits are exactly three lines and are day-stable.** The check date
   `2026-10-24` needs no change (landing is the same day). Revision 2.18's
   historical `32 → **33**` / `239 → **240**` at lines 8–9 record the previous
   move and must stay; no other `33`/`240` token exists to collide.
5. **First-match shadowing in `TOPIC`.** The leg takes the first `- ` line
   containing the basename. The index row (line 404) precedes the optional
   Known-gaps bullet (~line 700), so the row wins; never add a `- ` line naming
   the file above line 404 (the drafted revision block does not).
6. **Registry row count in the revision block is unmeasured here.** The draft
   omits the `registry moved … rows` clause rather than guessing 776+N; if
   integration wants it, measure the registry at the lands tree first (2.17
   precedent supports omission).

## Out of scope (not done by this seat)

Writing the entry; registry rows S805–S828 / dispositions; lesson and gate rows;
applying the README row, count edits, revision block, or Known-gaps bullet;
commit/integration; running the counters against a clone. All are L1 steps.
No verification beyond the read-only sweep and the in-memory simulation was run.

## Artifact paths

- `.ufo/waves/round-67/stage/readme-row.txt` — the row + all edit instructions
  + measured simulation/negative-control record.
- `.ufo/waves/round-67/w1/ScribeReadmePlan.md` — this report.

Report: .ufo/waves/round-67/w1/ScribeReadmePlan.md

## Addendum — C-APPEND / Ca-D4 id conflict (raised mid-flight, resolved)

`L1-kotodama-r67.CriticFrontier` alerted that claim C's `APPEND` leg and claim
Ca's `D4` leg look jointly unsatisfiable. Code-level confirmation from the
frozen counters (read, not modified):

- `reports/round-67/accept-c.py:67-70`: `NEW_IDS = S805..S828`,
  `EXTRA_IDS = {S801..S804}`; the `APPEND` leg fails on any appended id outside
  that union (`extra_ids`), and `ROWS` requires every new id to carry
  `status mined` — so a rejected row cannot ride S805-S828.
- `reports/round-67/accept-ca.py:68`: `R66_REJECTS = [S801..S804]`; `D4`
  requires `rej_opened_today >= len(R66_REJECTS) + 2`, counting only rows with
  `status rejected` and opened `2026-10-24` — i.e. >=2 rejects beyond S801-S804,
  which as new ids would be `extra_ids` in C's APPEND.
- `claims.json` C statement prices the registry at `724 -> 752` (S805-S828 plus
  the S801-S804 dispositions); Ca's >=2 additional today-dated rejects push the
  registry to 754+ at Ca's lands.

**L1 ruling (received 2026-10-24, no counter/claims revision): per-claim lands
separation — A_r (S801-S804 dispositions) < A_c (claim C; only S805-S828 append
over base) < A_ca (claim Ca; carries the S829+ reject rows and the round-67
lesson). Claim C's receipt runs at its own lands commit A_c, so APPEND never
sees the later rejects; D4 evaluates at A_ca. `QUOTES` capture-group fix already
applied separately.**

Impact on this deliverable: none, and it confirms two choices already made.

- `corpus/README.md` is in claim C's lands list, not Ca's, so the row and the
  three count edits land at A_c and are evaluated by C's `SWEEP` there.
- The drafted `revision: 2.19` block names no registry row total (finding 6
  above), so it stays true at A_c and at A_ca; the optional Known-gaps bullet
  cites only the claim-frozen "24 new registry rows S805-S828", also true at
  both. Do not add a registry total to either when integrating.
