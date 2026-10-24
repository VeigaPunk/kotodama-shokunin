# ScribeLessonDraft — round-67 lesson skeleton

Seat: scribe, r67 v2 wave (build). Deliverable:
`.ufo/waves/round-67/stage/lesson-draft.md`.

## Behavior

Wrote `.ufo/waves/round-67/stage/lesson-draft.md` (316 lines, 21.4K) as a
draft, not a filed lesson. Shape mirrors `corpus/lessons/round-66.md`:

- `# Round 67 - 2026-10-24 (hyaku run 5, L1 KotodamaR67)`.
- `## Round summary`: names all three claims with their frozen predicates
  (C = medicine entry + S805-S828, O = `tools/check-receipt-seq.py`, Ca =
  R66-D1..D5 dispositions), each R66-D1..D5 disposition with the artifact
  that carries it, the receipt-discipline paragraph (REQUIRED `--lands`,
  stamped/evaluated/measured + tree + counter sha256, STAMP equality,
  materialized-clone evaluation, parentage post-records), the Ca leg-name
  mapping (frozen `D3` leg = R66-D4 ledger, `D4` leg = R66-D5 rejects), and a
  wave-note slot for dead-seat accounting.
- `## Gate (rows opened this round; each quote is the anchor quote of that
  row's own final `row-*.txt` artifact, verbatim)`: 24 rows S805-S828 - S825
  and S826 filled verbatim from `.ufo/waves/round-67/rows/ScoutRow11/
  row-S825.txt` / `row-S826.txt` anchor cells (16 and 13 words), the other 22
  marked MISSING with the frozen `ROW_TOPICS` annotation; plus a `###
  Rejected rows` subsection for S801-S804 (r66 dispositions) and S829-S832
  (this round's rejects), all marked MISSING where no row file exists.
- `## Mistakes`: R67-M1 = the mined r66 receipt-sequencing class (the
  FAIL-recorded counter that held at tip) plus R67-M2..M5 grounded in
  evidence already on disk / peer reports, R67-M6 wave-planning placeholder
  for absent fragments, R67-M7 the C-APPEND vs Ca-D4 id-bound conflict
  recorded with L1's per-claim lands resolution (A_r -> A_c -> A_ca), and
  R67-M8 a generic placeholder for attack-seat findings.
- A closing HTML comment holds the integration checklist (fill MISSING lines,
  re-run the quote checker to 0 findings, keep >=20 ids, fill the wave note,
  lesson must be complete at lands because C's lands array contains it).

Nothing was invented: no URL or quote was written that is not copied from a
row fragment, and every count in the prose was re-derived read-only.

## Gates run by this seat (read-only, exhaustive list)

1. `python3 -B tools/check-gate-quotes.py .ufo/waves/round-67/stage/lesson-draft.md`
   -> `GATE_QUOTES: 0 findings`, exit 0. (Run on my own artifact to confirm
   the shape constraint the Ca QUOTES leg imposes; not a product check.)
2. Id census on the draft: `{'S'+x for x in re.findall(r"\bS(8[0-2]\d)\b", t)}`
   -> 24 of S805-S828, and the current counter expression
   `re.findall(r"\b(S8[0-2]\d)\b", t)` -> 24. The **rev0** expression in
   `accept-ca.py:272` -> 0 (finding F1; fixed pre-data after this seat's
   alert, counter now ` M` in the worktree, sha256
   `5382ffed6f6cbbec4d62bebd5131d2e1bb2d5b6ff621de32dec916010543653c`
   versus rev0 `5e8915ac...` recorded in `telemetry/dry-run-ca.txt`).
3. `len(splitlines()) = 312 > 10`; H2 headings exactly
   `['## Round summary', "## Gate (...)", '## Mistakes']`.
4. Base counts re-derived read-only at `ad5b52b0`:
   `git show ad5b52b0:corpus/SOURCES.md | grep -cE '^\| *S[0-9]+'` -> 724;
   `git ls-tree -r --name-only ad5b52b0 -- corpus/knowledge | grep -c '\.md$'`
   -> 240; culture-material -> 33; `grep -cE '^\| *S80[1-4] '` on the
   worktree registry -> 0 (S801-S804 vacant, so the Ca reject ids are free).
5. Read-only git parentage (grounds R67-M1):
   `git log -1 --format='%H %P' 4589ebdd` -> `4589ebdd ... 65fe8572...`;
   `53a60275` parent `3b1b5a67`; lane tip `b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21`
   ("round-67: declaration + instruments ..."), one commit past base
   `ad5b52b0ab5691358cd38718ab75649dc9916f9a`.
6. Pre-state evidence observed, not rerun: `reports/round-67/telemetry/
   census-start.txt` ends `EXIT=1` with 23 `E12` lines (S776, S779-S800) and
   `E11 S753 missing used-by -`; `reports/round-66/telemetry/
   final-measures-ca.txt` carries `D2 FAIL bad=[...:no_carrier ...]` and
   `# measured revision (lane main): 65fe8572...` with no stamped header.
7. `reports/round-67/telemetry/dry-run-ca.txt` observed: base run
   `D1 FAIL bad=['manifest_absent']`, `D2 FAIL`, `D3 FAIL`, `D4 FAIL`,
   `SEQ FAIL`, `CRITERION FAIL`, `QUOTES FAIL exit=2 gate_ids=0 clean=True`.

Not run: the three counters, `--selftest`, any build of the entry, any
network fetch. No mutation of the lane, jj state, or Git index; no commits.

## Findings

- **F1 (high, instrument regression — fixed pre-data).**
  `reports/round-67/accept-ca.py:272-276` (rev0):

  ```python
  gate_ids = set(re.findall(r"\bS(8[0-2]\d)\b", lesson_text)) & {
      f"S{n}" for n in range(805, 829)}
  ```

  `re.findall` with a capture group returns `'805'`, not `'S805'`; the
  intersection with `{'S805', ..., 'S828'}` is empty for every possible
  lesson text. Reproduced: the rev0 expression on
  `corpus/lessons/round-66.md` (which names S779-S800) returns 0;
  `re.findall(r"\b(S8[0-2]\d)\b", ...)` on this skeleton returns 24.
  Consequence: the `QUOTES` leg was unpassable, so `ACCEPT-CA-67` could never
  print PASS regardless of the lesson. The r66 counter did not have this
  defect (`reports/round-66/accept-ca.py:190` counts matches directly:
  `set(re.findall(r"\bS(77[6-9]|7[89]\d|800)\b", lesson_text))`, no
  intersection), so this was a **regression introduced by the r67 rewrite**
  — the same class the round exists to eliminate. Status: L1 applied the fix
  pre-data (`re.findall(r"\b(S8[0-2]\d)\b", ...)`); the file is ` M` in the
  worktree with sha256 `5382ffed...53653c` versus rev0 `5e8915ac...` in
  `telemetry/dry-run-ca.txt`, so the re-frozen control run must supersede
  that receipt. I did not edit the counter (product/judge code).
- **F2 (conflict, corrected for staleness — quoted verbatim).** The 12.4K
  version of `.ufo/waves/round-67/stage/gate-rows.md` (12:37Z) asserted in its
  finding F2: "so the same placeholders would give `gate_ids=24` and the leg
  `QUOTES` would pass." The rev0 reproduction in F1 contradicted that (0 by
  construction). The current 18,064-byte version (09:43) has rewritten F2
  after the L1 fix: it now says `accept-ca.py:272-276` "(after the L1's
  capture-group fix) counts `(S8[0-2]\d)` ids anywhere in the lesson text
  (`gate_ids >= 20`), not quoted Gate rows ... A Gate of 24 "MISSING" lines
  would pass the leg with zero anchored quotes." That residual concern is
  correct and is the r66 ScribeGateRows item-7 class: the id census is not a
  quote census. `ExecCounterSmokeCa` finding F4 (`clean=True` text) remains
  as first observed. No counter change is proposed here; the defense is the
  fill plus a non-author re-open of every quote (RevGateQuotes).
- **F3 (predicate-vs-intent, inherited from `ExecCounterSmokeCa` F6).** Ca
  leg `D4` requires `rej_opened_today >= len(R66_REJECTS) + 2` (six rejected
  rows opened 2026-10-24), while the Ca claim text says only "S801-S804 +
  >=2 new"; `new_rejects` is computed and unused. If S801-S804 are restored
  with an older opened date, D4 is unpassable. Draft mitigation: every
  rejected Gate row carries 2026-10-24.
- **F4 (stamp-vs-worktree hole, attested by peers; not rerun here).**
  `MutEntryClass` M9 (uncommitted tier flip, worktree != lands) prints
  `STAMP PASS ... dirty_tracked=True`; `RevCounterC` finding F1 asks that
  STAMP include an empty `git status --porcelain`. A receipt can therefore
  be stamped at lands over uncommitted bytes unless the runner obeys the
  materialized-clone protocol.
- **F5 (citation-shape hole, attested by `MutEntryClass`).** ONEID counts
  only `\((S\d{3,})\)` over the whole entry: a bare foreign id (`see S099`,
  M5) and an extra fabricated bullet with no citation (M10) both PASS;
  duplicate citations are caught only by the count (M6). The lesson draft
  routes this as R67-M4.
- **F6 (build lag, not a defect — resolved late).** At draft time
  `.ufo/waves/round-67/rows/` held only `ScoutGapMed/gap.md`,
  `ScoutRow11/row-S825.txt`, `row-S826.txt`, `rejects.txt`: 22 of 24 opened
  rows had no fragment, so 22 Gate lines could not be filled without
  fabrication. By 09:43 fragments had arrived for S809-S820 and S821-S826
  (plus the S829-S832 reject lines) per the current
  `stage/gate-rows.md` finding F1, and four rows (S807, S808, S827, S828)
  were still absent; that file also warns S805's `teaches` cell was rewritten
  between two reads, so every filled Gate line is a snapshot the L1 must
  re-run at integration. The lesson draft therefore keeps MISSING markers and
  a merge instruction instead of duplicating the sibling's lines.
- **F7 (draft-time lane state).** `main` is `b78f8b8e` (declaration +
  instruments), not the frozen base `ad5b52b0`; `.ufo/waves/round-66/` is
  still untracked, which is exactly R66-D1's undurable-evidence state — the
  committed manifest is the only durable carrier of that tree.
  `reports/round-67/dispositions/r66-wave-evidence-manifest.txt` now exists
  on disk (13,735 bytes, 201 INCLUDE/EXCLUDE lines).
- **F8 (id-bound vs records — raised by `CriticFrontier`, resolved by L1 as
  per-claim lands separation; no counter revision).**
  `reports/round-67/accept-c.py`'s APPEND leg computes
  `allowed_new = set(NEW_IDS) | EXTRA_IDS` (S805-S828 ∪ S801-S804) and fails
  on any appended id outside it (`:357`, `extra=...`), while
  `accept-ca.py`'s D4 leg requires six `status=rejected` rows with
  `opened == 2026-10-24` (S801-S804 + >=2, `new_rejects` computed and
  unused). Appending S829-S832 at the commit C is evaluated at therefore
  prints `APPEND FAIL extra=['S829', ...]`; claims.json's own arithmetic
  (`724 -> 752 = 728 + 24`) excludes those ids. L1 resolution: per-claim
  lands separation — A_r carries S801-S804 with the r66 dispositions and
  lands first, A_c is C's own lands commit (registry 752, only S805-S828
  appended), A_ca is Ca's later lands commit carrying S829+ and the lesson;
  each counter runs in a materialized clone at its own lands with
  evaluated == stamped. The draft records this at R67-M7 and states the
  sequencing in the C arithmetic and the R66-D5 disposition; the bound stays
  `NEW_IDS ∪ EXTRA_IDS`. Attributed: I read the two legs and the claims
  arithmetic; I did not run the counters.

## Touched surfaces

- Wrote: `.ufo/waves/round-67/stage/lesson-draft.md`,
  `.ufo/waves/round-67/w1/ScribeLessonDraft.md`.
- Read-only: `corpus/lessons/round-66.md`, `corpus/lessons/round-65.md`,
  `corpus/lessons/round-66-verifier-spotcheck.md`,
  `reports/round-67/{claims.json,accept-c.py,accept-o.py,accept-ca.py}`,
  `reports/round-67/telemetry/*`, `reports/round-66/telemetry/
  final-measures-ca.txt`, `reports/round-65/telemetry/
  accept-ca-post-records-fail.txt`, `.ufo/waves/round-67/{gen-spec.py,
  stage/gate-rows.md (both versions), rows/**, w1/{swarm-registry.json,
  MutEntryClass.md, RevCounterC.md, ExecCounterSmokeCa.md,
  CriticFrontier.md}}`, `reports/round-67/dispositions/
  r66-wave-evidence-manifest.txt`, `tools/check-gate-quotes.py`,
  `git log/show/ls-tree/rev-parse`.

## Out of scope (owned elsewhere)

- `corpus/lessons/round-67.md` itself (L1 integration);
  `stage/gate-rows.md` (ScribeGateRows); LOG/SCORECARD/QUALITY/README drafts
  (sibling scribes); the entry text and registry rows (scouts/L1); any
  revision of the three counters or `tools/check-receipt-seq.py`;
  `reports/round-67/dispositions/r66-wave-evidence-manifest.txt`.

## Tooling

No installs or upgrades this seat (pacman paused; nothing needed).

Report: .ufo/waves/round-67/w1/ScribeLessonDraft.md
