# ScribeLessonDraft — round 66, scribe seat: lesson body skeleton

Wrote `.ufo/waves/round-66/stage/lesson-draft.md` (286 lines) — the round-66
lesson body skeleton for `corpus/lessons/round-66.md`. Read-only elsewhere; no
product code, registry, entry, counter, judge or lane jj/Git state touched. No
tool installs or upgrades were needed (nothing installed; no pacman transaction).

## What the draft contains

- `# Round 66 lesson ... — DRAFT body` + a draft banner that states the file is
  not a claim record and that no routed defect is asserted fixed.
- `## Round summary` stub: base `94209e8f…`, the three frozen claims and their
  predicates verbatim in substance from `reports/round-66/claims.json`; attempt
  history / census / counts deliberately left to integration (inventing them
  would be worse than the gap).
- `## Gate` **preamble only** (rows S777-S800, one anchor quote per row from that
  row's own fragment, 2026-10-24, <=25 words, capture cells carry `https://`
  per R65-M3, `- verified-at:` names rows without a range token per R65-M4) plus
  the **S776 supersession** paragraph: S776 supersedes S753 for the games entry's
  mancala bullet; S753's live URL was an HTML shell at closure and its committed
  capture `20250926172224` replays 404; S776 carries the live PDF + fresh capture
  `20261024111013`. The paragraph explicitly records the supersession as
  **designed, not evidenced**, and defers the row line to `stage/s776-gate.md`.
- `## Mistakes` — ten `R66-Mn` bullets in the ordered shape
  **class -> evidence pointer -> captured-by -> fix**, seeded from
  `corpus/lessons/round-65.md` `## Mistakes` (M1/M3/M4/M6/M7/M8/M9 classes) and
  from routed defects D1->M8, D2->M7, D3->M9, D4->M10. Every fix clause is
  "to be dispositioned by <artifact/instrument>" (14 occurrences of that phrase;
  the only "fixed" token is the disclaimer).
- `## Routed defects (round-65 closure, §5)` — one paragraph per R65-D1..D4:
  the closure's own words, the declared round-66 instrument, the evidence state
  read at draft time, and the exact artifact that must disposition it.

## Evidence read (provenance)

| source | what it gave |
|---|---|
| `corpus/lessons/round-65.md` | M1-M9 text, Gate-line shape, S753 anchor quote (not re-typed into the draft) |
| `corpus/lessons/round-65-verifier-spotcheck.md` | §1 defects 1-4, §3 S753/S771/S765 rows, §5 routed defects D1-D4 (operative sentences) |
| `reports/round-66/claims.json` | claim C/O/Ca statements, predicates, legs, review_only |
| `reports/round-66/accept-ca.py` (39-188) | exact leg bodies: D1 receipt strings (`200`, `application/pdf`, quote, `20261024111013`, `S776`; games entry `(S776)` once / `(S753)` zero), D2 ancestry+tree+sha, D3 named-vs-existing >=8, D4 `SEPARABILITY: N findings` + `acceptance_runs=` and no `PARTIAL`, CRITERION 18, QUOTES 0-findings + >=25 ids S776-S800 |
| `reports/round-66/telemetry/s753-recapture.txt` | live `status=200 content-type=application/pdf`; PDF 1.6 fetch; **empty CDX section**; old capture `status=000`; no quote line |
| `reports/round-66/telemetry/seat-evidence.txt` | seed: 64 expected seat paths, per-seat status lines deferred, no last-error text yet |
| `reports/round-66/telemetry/dry-run-{c,o,ca}.txt`, `controls-{c,o,ca}.txt` | red pre-data output preserved (`ACCEPT-CA-66: FAIL`, D1-D4 all FAIL at base); O dry-run SELFTEST 63/63, DIFF 428, OPTIONS, BOUND exit=2 partial; base tool sha `5764ea27…` control |
| `tools/check-claim-separability.py` | option surface `--jobs/--budget/--max-runs/--static-only` present (help 63-65, docstring 38-47) |
| `tools/check-gate-quotes.py` (docstring) | Gate-section scoping, 25-word run cap, `truncated-grounds` / `doubled-locator` / `html-entity` classes |
| `corpus/SOURCES.md` | S753 row (B, mined, cite cell, source cell with the 20250926172224 capture); registry rows 701; **no S776 row exists at base** |
| `corpus/knowledge/culture-material/games-play-sport-contests.md` | line 23 still cites `(S753)`; no `(S776)` |
| `corpus/QUALITY.md` | numbered criteria end at **17**; no criterion 18 exists |

Commands run (none re-executed for decoration):
`python3 -B tools/check-gate-quotes.py .ufo/waves/round-66/stage/lesson-draft.md`
-> `GATE_QUOTES: 0 findings`, exit 0 (smoke on the draft only — NOT the
integrated lesson's `QUOTES` leg); `grep -cE '^\| *S[0-9]{3,} *\|' corpus/SOURCES.md`
-> 701; `git cat-file -e 94209e8f:reports/round-66/telemetry/s753-recapture.txt`
-> absent in base (the whole `telemetry/` dir is untracked worktree content);
`grep -oE 'S(77[6-9]|7[89][0-9]|800)'` over the draft -> only S776/S777/S800.

## Findings for the integration (dependencies and risks)

1. **No row fragments exist.** `.ufo/waves/round-66/rows/` contains only an empty
   `ScoutRow03/` directory at draft time — no `row-S###.txt`. So no anchor could
   be re-opened, and `stage/gate-rows.md` has nothing to quote from. The Gate
   rows for S777-S800 are therefore a hard dependency on seats that have not
   landed; a Gate quote typed from a seat's prose summary would be the R65-M1
   false-anchor class.
2. **`QUOTES` leg arithmetic.** `accept-ca.py` QUOTES needs >=25 distinct ids in
   S776-S800 plus 0 `check-gate-quotes.py` findings on the integrated lesson. My
   draft names 3 of them (S776/S777/S800); the remaining 22 must come from real
   Gate rows. Adding an id list purely to satisfy the regex would be a false
   stamp — flagged in the draft's integration notes, not done.
3. **S753 recapture receipt is incomplete against the D1 leg.** It has the live
   200/pdf and a PDF fetch, but: CDX section empty, old capture `status=000`, no
   verbatim-quote line, no `20261024111013`, no `S776`. The frozen claim asserts
   the fresh capture "replays byte-exact"; no receipt on disk shows that yet.
   D1 is therefore *undispositioned*, and the draft says so.
4. **Capture encoding class applies to the S776 repair.** The round-65 spot-check
   admitted S771 only after gzip decompression, and R65-M6 recorded the same
   class; a raw-byte replay of `20261024111013` may report quote-absent. The D1
   receipt should record the decoded or byte-exact replay explicitly.
5. **QUALITY criterion 18 is absent** (file ends at 17), so claim Ca's
   `CRITERION` leg fails at draft time independent of the lesson.
6. **D2/D3/D4 have no measurement yet**: no `final-measures-*.txt`, no
   `separability-real.txt`, and `seat-evidence.txt` is a seed whose 64 named
   paths mostly do not exist (`w1/` holds `swarm-registry.json`,
   `ScoutPartialOwners.md` and two scratch trees). The draft records each as
   undispositioned with the leg that decides it.
7. **`telemetry/` is untracked.** All round-66 telemetry read here is worktree
   content outside base `94209e8f`; the D1/D2/D3/D4 legs read committed bytes at
   closure, so these receipts must be committed by the records commit.

## Out of scope (not done, by assignment)

- Did not write `stage/gate-rows.md` or `stage/s776-gate.md` (sibling seats own
  those); did not create `corpus/lessons/round-66.md` or the scent entry.
- Did not edit `corpus/lessons/round-65.md`, the spot-check, `QUALITY.md`,
  `SOURCES.md`, counters or tools.
- Did not run any `ACCEPT-*` counter end-to-end, any network fetch, or any
  git/jj write; no claim verdict is asserted from this seat.

Report: .ufo/waves/round-66/w1/ScribeLessonDraft.md
