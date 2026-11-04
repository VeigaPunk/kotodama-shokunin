# Registry census — kotodama round 83, wave 1 (ExecRegistryCensus)

Basis: committed bytes only. Instruments, rows and evidence are read with `git show`/`git ls-tree`
at the frozen claims/counters commit `21277b089e3c64c247bb4e0fcb033abfdfa1e668`; the lane base is
`3088bd7fe2a55a123214abba7008dcddf12b301c`. No worktree byte was graded, no counter was executed,
no repository tool was run (wave rule: no build/lint/test runs while the editing wave is in flight).

## Method

- **Instruments**: every tracked path matching `reports/round-*/accept-*.py` (fnmatch), which is the
  counter class the claim names. 61 at the frozen revision. Helpers such as
  `reports/round-83/counterlib.py` are not instruments.
- **Rows**: the `## Gates and probes` table of `SKILL.md` at the same revision. Rows are the
  pipe-delimited lines between the heading and the next `## `; the header row and the dash row are
  excluded. 60 data rows. 54 parse to exactly 8 cells; 6 parse to 9 because their verdict-map cell
  carries a literal `|` inside `PASS|FAIL` (`SKILL.md:686-691`, rounds 66–67). Their entry-command
  cells are intact, so coverage is unaffected.
- **Coverage**: a counter is covered iff its repo-relative path appears in some row's entry-command
  cell (cell 3). 47 covered, 14 missing.
- **Re-derivation**: the same parse written with accept-o83's own semantics (`registry_rows` plus
  `dead_of`) reproduces 60 rows and finds **0 dead** `.py` tokens in entry-command cells at the
  frozen revision.

## Result

- `instruments`: 61 — full list in `registry-census.json`
- `rows`: 60 data rows in the table at the frozen revision
- `missing`: 14 (below)
- `proposed`: 14 rows, 8 cells each (below and in the JSON, keyed by counter path)

Missing set (round-count order):

```
reports/round-76/accept-c.py
reports/round-76/accept-ca.py
reports/round-79/accept-ca.py
reports/round-79/accept-o.py
reports/round-80/accept-d.py
reports/round-80/accept-o.py
reports/round-81/accept-c81.py
reports/round-81/accept-d81.py
reports/round-81/accept-o81.py
reports/round-82/accept-d82.py
reports/round-82/accept-o82.py
reports/round-83/accept-c83.py
reports/round-83/accept-d83.py
reports/round-83/accept-o83.py
```

## Cross-checks (all derived from committed bytes)

- The lane base `3088bd7…` holds 58 counters; the frozen revision adds exactly the three round-83
  counters (absent at base, present at freeze) → 58 + 3 = 61.
- `reports/round-83/accept-o83.py` BEFORE constants, read from its own bytes: base instruments 58 and
  a frozen 11-item base-missing set (`accept-o83.py:116-120` reads `base_instruments` and
  `base_missing`; `:164-167` builds the row-coverage need list from `base_missing` plus the three
  round-83 counters). 11 + 3 = 14, exactly this census's missing set. The two numbers describe
  different revisions and do not conflict.
- Proposed rows name each counter once, and every entry command contains its counter path, so a
  path-in-entry-command coverage check admits all 14.

## Proposed rows (copy-paste; 8 cells, no literal pipe inside any cell)

```
| accept-c-76 | gate | `python3 -B reports/round-76/accept-c.py --root . --lands <40-hex> --freeze <40-hex> [--fleet-root <fleet>]` | Output ends `ACCEPT-C-76: PASS legs=13/13` (exit 0) or `: FAIL legs=<n>/13` (exit 1, n = passing legs); a refusal prints `ACCEPT-C-76: FAIL legs=0/13 (refused: …)` and exits 2 on a missing or non-40-hex `--lands`/`--freeze`, an unreadable or unusable frozen claims.json, `lands` equal to the frozen base, or LEGCOUNT (`reports/round-76/accept-c.py:6622`, `:6623`, `:6473`, `:6539-6542`) | `--selftest` (fixture repos built in the scratch root, never the system temp dir; prints `SELFTEST: n/m`) (`reports/round-76/accept-c.py:6528-6537`, `:6342`) | frozen `reports/round-76/claims.json` claim C (candidate entry paths and admit flags, min_admitted, base counts 817 registry rows and 252 knowledge files at `reports/round-76/accept-c.py:11`, by-document map path+sha256, legs[]); `scripts/sources-census.sh`; `_SFX_*` path literals at `:4704-4718` are selftest fixtures | read-only against the repo; materialises and builds selftest fixtures in a scratch mkdtemp, never the system temp directory (`reports/round-76/accept-c.py:6591-6620`) | kotodama-shokunin |
| accept-ca-76 | gate | `python3 -B reports/round-76/accept-ca.py --root . --lands <40-hex> --freeze <40-hex> --fleet-root <fleet> --combined <40-hex> --work <dir>` | Output ends `ACCEPT-CA-76: PASS legs=12/12` (exit 0) or `: FAIL legs=<n>/12` (exit 1); a refusal prints `ACCEPT-CA-76: FAIL legs=0/12 (refused: …)` and exits 2 on no scratch root, a missing `--combined`, a missing `--lands`/`--freeze`/`--fleet-root`, a non-40-hex revision, LEGCOUNT, `lands` equal to the frozen claims base, or `freeze == lands` with every leg green (`reports/round-76/accept-ca.py:2823`, `:2825`, `:2675`, `:3744-3747`, `:2820-2822`) | `--selftest` (self-contained; prints `SELFTEST: n/m`) (`reports/round-76/accept-ca.py:3739-3743`, `:3700`) | frozen `reports/round-76/ledger.json` and `reports/round-76/claims.json` (read at freeze; base `98c486bd…` at `reports/round-76/accept-ca.py:7`); committed receipts under `reports/round-76/telemetry/`; `SCORECARD.md` (`:246-249`, `:3137-3173`) | read-only against the repo; grades in a `--work` scratch clone; the selftest writes only its fixture lane (`reports/round-76/accept-ca.py:2736-2815`) | kotodama-shokunin |
| accept-ca-79 | gate | `python3 -B reports/round-79/accept-ca.py --root . --lands <40-hex> --freeze <40-hex> --work <existing-dir>` | Output ends `ACCEPT-CA-79: PASS legs=7/7` (exit 0) or `: FAIL legs=<n>/7` (exit 1); a refusal prints `ACCEPT-CA-79: FAIL legs=0/7 (refused: …)` and exits 2 on a non-40-hex or non-commit revision, unreadable frozen config, LEGCOUNT, `lands` equal to the frozen base, or off-first-parent history (`reports/round-79/accept-ca.py:435-436`, `:442`, `:692-696`) | `--selftest --work <existing-dir> [--keep]` (prints `SELFTEST: n/m`) (`reports/round-79/accept-ca.py:648-656`) | frozen `reports/round-79/claims.json` claim Ca (object `census_correction`); measured round-78 revision `4b255745…` at `reports/round-79/accept-ca.py:7`; receipt `reports/round-78/telemetry/census-end.txt`; corrections dir `reports/round-79/corrections/` (`:467-469`) | read-only against the repo; writes its verdict record `<work>/accept-ca-79-<lands12>.txt` and selftest log `<work>/selftest-ca79.txt` (`reports/round-79/accept-ca.py:439`, `:656`) | kotodama-shokunin |
| accept-o-79 | gate | `python3 -B reports/round-79/accept-o.py --root . --lands <40-hex> --freeze <40-hex> --work <existing-dir>` | Output ends `ACCEPT-O-79: PASS legs=10/10` (exit 0) or `: FAIL legs=<n>/10` (exit 1); a refusal prints `ACCEPT-O-79: FAIL legs=0/10 (refused: …)` and exits 2 on missing flags, a non-existent `--work`, a non-40-hex or non-commit revision, unreadable frozen config, LEGCOUNT, `lands` equal to the frozen base, or off-first-parent freeze/base (`reports/round-79/accept-o.py:556-558`, `:564`, `:708-714`, `:682-705`) | `--selftest --work <existing-dir> [--keep]` (prints `SELFTEST-O79: PASS` or `FAIL`) (`reports/round-79/accept-o.py:677-681`, `:660`) | frozen `reports/round-79/claims.json` claim O (object `guard`): tool path+sha256, red/green ledger paths, refusal dir, fixture base, allowed paths; graded stub `reports/round-79/counters/junk-stub-tool.py` (`reports/round-79/accept-o.py:379`); the `red.json`/`green.json`/`refusals/` literals at `:600-612` are the selftest fixture's cfg, not graded pins | read-only against the repo; writes its verdict record and the extracted guard under `--work`; selftest scratch under `--work` (`reports/round-79/accept-o.py:523`, `:561`) | kotodama-shokunin |
| accept-d-80 | gate | `python3 -B reports/round-80/accept-d.py --root . --lands <40-hex> --freeze <40-hex> --work <existing-dir>` | Output ends `ACCEPT-D-80: PASS legs=7/7` (exit 0) or `: FAIL legs=<n>/7` (exit 1); a refusal prints `ACCEPT-D-80: FAIL legs=0/7 (refused: …)` and exits 2 on missing flags, a non-existent `--work`, non-40-hex or non-commit revisions, unreadable frozen config, LEGCOUNT, `lands` equal to the frozen base, or off-first-parent history (`reports/round-80/accept-d.py:406-408`, `:414`, `:607-613`, `:581-604`). A lint-tool sha256 mismatch at lands is a LINT leg failure (exit 1), not a refusal (`:248-251`). | `--selftest --work <existing-dir> [--keep]` (prints `SELFTEST-D80: PASS` or `FAIL`) (`reports/round-80/accept-d.py:576-580`, `:559`) | frozen `reports/round-80/claims.json` claim D (object `entry80`); entry `corpus/knowledge/culture-material/maritime-seafaring-lexicon.md` and rows S898/S899/S900 at `reports/round-80/accept-d.py:4-5`; `tools/check-cited-lines.py` sha256 pin (`:7-9`) | read-only against the repo; writes `<work>/accept-d-80-<lands12>.txt`; extracts the lint tool into scratch (`reports/round-80/accept-d.py:411`, `:253`) | kotodama-shokunin |
| accept-o-80 | gate | `python3 -B reports/round-80/accept-o.py --root . --lands <40-hex> --freeze <40-hex> --work <existing-dir>` | Output ends `ACCEPT-O-80: PASS legs=10/10` (exit 0) or `: FAIL legs=<n>/10` (exit 1); a refusal prints `ACCEPT-O-80: FAIL legs=0/10 (refused: …)` and exits 2 on missing flags, a non-existent `--work`, non-40-hex or non-commit revisions, unreadable frozen config, LEGCOUNT, `lands` equal to the frozen base, or off-first-parent (`reports/round-80/accept-o.py:586-588`, `:594`, `:739-745`, `:713-736`) | `--selftest --work <existing-dir> [--keep]` (prints `SELFTEST-O80: PASS` or `FAIL`) (`reports/round-80/accept-o.py:708-712`, `:691`) | frozen `reports/round-80/claims.json` claim O (object `guard80`); fixtures `reports/round-80/fixtures/red.json`, `green.json`, `refusals/`; `reports/round-80/counter-revisions.md`; stub `reports/round-79/counters/junk-stub-tool.py` (`reports/round-80/accept-o.py:80`, `:631-636`) | read-only against the repo; writes `<work>/accept-o-80-<lands12>.txt`; extracts the guard into scratch (`reports/round-80/accept-o.py:591`, `:553`) | kotodama-shokunin |
| accept-c-81 | gate | `python3 -B reports/round-81/accept-c81.py --root . --fleet <fleet> --lands <40-hex> --freeze <40-hex> --work <existing-dir>` | Output ends `ACCEPT-C-81: PASS legs=6/6` (exit 0) or `: FAIL legs=<n>/6` (exit 1); a refusal prints `ACCEPT-C-81: FAIL legs=0/<n> (refused: …)` and exits 2 on missing or invalid flags (all five are argparse-required), ancestry violations, or an incomplete frozen config (`reports/round-81/accept-c81.py:249-251`, `:127-148`, `:64-69`) | `--selftest --work <existing-dir>` (prints `SELFTEST-C81: PASS` or `FAIL (n checks; counter sha256 …)`) (`reports/round-81/accept-c81.py:385-392`, `:379`) | frozen `reports/round-81/claims.json` claim C: tool path+sha256+size bounds+markers, expected red orphan set and summary, red receipt and dispositions paths, allowed paths (`reports/round-81/accept-c81.py:81`, `:141-144`) | read-only against the repo; extracts the lands checker into `--work`; selftest builds fixtures under `--work` (`reports/round-81/accept-c81.py:189-191`, `:272-366`) | kotodama-shokunin |
| accept-d-81 | gate | `python3 -B reports/round-81/accept-d81.py --root . --lands <40-hex> --freeze <40-hex> --work <existing-dir>` | Output ends `ACCEPT-D-81: PASS legs=7/7` (exit 0) or `: FAIL legs=<n>/7` (exit 1); a refusal prints `ACCEPT-D-81: FAIL legs=0/<n> (refused: …)` and exits 2 on missing or invalid flags, ancestry violations, or an incomplete frozen config (`reports/round-81/accept-d81.py:282-284`, `:127-148`, `:65-69`) | `--selftest --work <existing-dir>` (prints `SELFTEST-D81: PASS` or `FAIL (n checks; counter sha256 …)`) (`reports/round-81/accept-d81.py:430-436`, `:423`) | frozen `reports/round-81/claims.json` claim D: entry pin, rows S901/S902/S903 with opened 2026-11-01, capture records, couples targets, `tools/check-cited-lines.py` pin (`reports/round-81/accept-d81.py:10-11`, `:348`) | read-only against the repo; materialises lands bytes into `--work`; selftest fixtures under `--work` (`reports/round-81/accept-d81.py:197-202`) | kotodama-shokunin |
| accept-o-81 | gate | `python3 -B reports/round-81/accept-o81.py --root . --lands <40-hex> --freeze <40-hex> --work <existing-dir>` | Output ends `ACCEPT-O-81: PASS legs=6/6` (exit 0) or `: FAIL legs=<n>/6` (exit 1); a refusal prints `ACCEPT-O-81: FAIL legs=0/<n> (refused: …)` and exits 2 on missing or invalid flags, ancestry violations, LEGCOUNT, or an incomplete frozen config (`reports/round-81/accept-o81.py:269-271`, `:139-165`, `:67-71`) | `--selftest --work <existing-dir>` (prints `SELFTEST-O81: PASS` or `FAIL (n checks; counter sha256 …)`; the graded SELFTEST leg reads the committed receipt `reports/round-81/telemetry/selftest-o81.txt`) (`reports/round-81/accept-o81.py:383-389`, `:376`, `:35`) | frozen `reports/round-81/claims.json` claim O: generator and builder path+sha256+size+markers, old revision, allowed paths; committed selftest receipt `reports/round-81/telemetry/selftest-o81.txt` (`reports/round-81/accept-o81.py:35`); the generator is extracted as `w2-mutants.py` (`:207`); `absent.py` literals at `:300-305` are selftest fixture cfg | read-only against the repo; materialises lands bytes into `--work`; selftest fixtures under `--work` (`reports/round-81/accept-o81.py:202-232`) | kotodama-shokunin |
| accept-d-82 | gate | `python3 -B reports/round-82/accept-d82.py --root . --lands <40-hex> --freeze <40-hex> --work <existing-dir>` | Output ends `ACCEPT-D-82: PASS legs=8/8` (exit 0) or `: FAIL legs=<n>/8` (exit 1); a refusal prints `ACCEPT-D-82: FAIL legs=0/<n> (refused: …)` and exits 2 on missing or invalid flags, a do-nothing or non-commit lands, ancestry violations, LEGCOUNT, or an incomplete frozen config (`reports/round-82/accept-d82.py:341-343`, `:147-166`, `:71-75`) | `--selftest [--work <dir>]` (work auto-mkdtemp when omitted; prints `SELFTEST-D82: PASS` or `FAIL (n checks)`) (`reports/round-82/accept-d82.py:528-538`, `:524`) | frozen `reports/round-82/claims.json` claim D: entry pin, mined rows S904/S905/S906 plus the rejected row, rowcount 827 -> >= 831 (`reports/round-82/accept-d82.py:10-15`), capture records under `reports/round-82/evidence/` (`:423`) | read-only against the repo; materialises lands bytes into `--work`; selftest fixtures under `--work` (`reports/round-82/accept-d82.py:220-225`) | kotodama-shokunin |
| accept-o-82 | gate | `python3 -B reports/round-82/accept-o82.py --root . --lands <40-hex> --freeze <40-hex> --work <existing-dir>` | Output ends `ACCEPT-O-82: PASS legs=7/7` (exit 0) or `: FAIL legs=<n>/7` (exit 1); a refusal prints `ACCEPT-O-82: FAIL legs=0/<n> (refused: …)` and exits 2 on missing or invalid flags, a do-nothing or non-commit lands, ancestry violations, LEGCOUNT, or an incomplete frozen config (`reports/round-82/accept-o82.py:435-437`, `:205-221`, `:75-79`) | `--selftest [--work <dir>]` (work auto-mkdtemp when omitted; prints `SELFTEST-O82: PASS` or `FAIL (n checks)`) (`reports/round-82/accept-o82.py:667-677`, `:663`) | frozen `reports/round-82/claims.json` claim O: `tools/check-sources-recheck.py` shape markers, frozen registry blob, as-of dates, selftest floor (`reports/round-82/accept-o82.py:41`) | read-only against the repo; runs the lands tool over a materialised tree in `--work`; selftest fixtures under `--work` (`reports/round-82/accept-o82.py:262-289`) | kotodama-shokunin |
| accept-c-83 | gate | `python3 -B reports/round-83/accept-c83.py --root . --lands <40-hex> --freeze <40-hex> --work <existing-dir> [--junk]` | Output ends `ACCEPT-C-83: PASS legs=9/9` (exit 0) or `: FAIL legs=<n>/9` (exit 1); a refusal prints `ACCEPT-C-83: FAIL legs=0/9 (refused: …)` and exits 2 on a non-40-hex revision, a missing `--work` directory, LEGCOUNT, `lands` equal to the frozen base, freeze not an ancestor of lands, or lands not an ancestor of the branch tip (`reports/round-83/counterlib.py:149-157`, `:160-162`, `reports/round-83/accept-c83.py:219-237`) | — (no `--selftest`; passing it is an argparse error, exit 2; `--junk` runs the mutation battery and prints `JUNK-C-83: PASS n/n`) (`reports/round-83/accept-c83.py:211-215`, `:205`) | frozen `reports/round-83/claims.json` claim C: criterion file+marker+markers, record path+min bytes+hash set, erratum path+markers, supersede prefix+markers+superseded id, checker path+selftest floor+shape markers+summary regex, own and foreign paths (`reports/round-83/accept-c83.py:31`, `:105-176`) | read-only against the repo; materialises into `<work>/tree` and builds junk clones under `--work`; never writes inside the lane repo (`reports/round-83/counterlib.py:7`, `:79-95`) | kotodama-shokunin |
| accept-d-83 | gate | `python3 -B reports/round-83/accept-d83.py --root . --lands <40-hex> --freeze <40-hex> --work <existing-dir> [--junk]` | Output ends `ACCEPT-D-83: PASS legs=9/9` (exit 0) or `: FAIL legs=<n>/9` (exit 1); a refusal prints `ACCEPT-D-83: FAIL legs=0/9 (refused: …)` and exits 2 on a non-40-hex revision, a missing `--work` directory, LEGCOUNT, `lands` equal to the frozen base, freeze not an ancestor of lands, or lands not an ancestor of the branch tip (`reports/round-83/counterlib.py:149-157`, `:160-162`, `reports/round-83/accept-d83.py:248-266`) | — (no `--selftest`; passing it is an argparse error, exit 2; `--junk` runs the mutation battery and prints `JUNK-D-83: PASS n/n`) (`reports/round-83/accept-d83.py:240-244`, `:234`) | frozen `reports/round-83/claims.json` claim D: entry path, base 256 knowledge files and 832 registry rows, header markers, section/decision-row/anchor floors, new row ids, opened date, own and foreign paths (`reports/round-83/accept-d83.py:137-139`, `:144-166`) | read-only against the repo; materialises into `<work>/tree` and builds junk clones under `--work`; never writes inside the lane repo (`reports/round-83/counterlib.py:7`, `:79-95`) | kotodama-shokunin |
| accept-o-83 | gate | `python3 -B reports/round-83/accept-o83.py --root . --lands <40-hex> --freeze <40-hex> --work <existing-dir> [--junk]` | Output ends `ACCEPT-O-83: PASS legs=8/8` (exit 0) or `: FAIL legs=<n>/8` (exit 1); a refusal prints `ACCEPT-O-83: FAIL legs=0/8 (refused: …)` and exits 2 on a non-40-hex revision, a missing `--work` directory, LEGCOUNT, `lands` equal to the frozen base, freeze not an ancestor of lands, or lands not an ancestor of the branch tip (`reports/round-83/counterlib.py:149-157`, `:160-162`, `reports/round-83/accept-o83.py:253-271`) | — (no `--selftest`; passing it is an argparse error, exit 2; `--junk` runs the mutation battery and prints `JUNK-O-83: PASS n/n`) (`reports/round-83/accept-o83.py:245-249`, `:239`) | frozen `reports/round-83/claims.json` claim O: tool path and shape markers, base instruments 58 with the 11-item base-missing set, selftest floor, summary regex, min instruments/rows, own and foreign paths (`reports/round-83/accept-o83.py:33`, `:146-167`) | read-only against the repo; materialises into `<work>/tree` and builds junk clones under `--work`; never writes inside the lane repo (`reports/round-83/counterlib.py:7`, `:79-95`) | kotodama-shokunin |
```

## Interface constraints for `tools/check-gate-registry.py` (derived from accept-o83 checks)

- Summary line shape: `GATE-REGISTRY: 0 missing / <r> registered / <i> instruments / 0 dead`, groups
  read in that order as missing, registered, instruments, dead (`reports/round-83/accept-o83.py:144-148`;
  the canned-shape fixture at `:226-231` prints the same spelling).
- `--json` must carry lists `instruments`, `missing`, `dead` and the counts `registered`, `rows`
  (`accept-o83.py:153-160`, `:226-231`); the graded comparisons require `sorted(instruments)` to
  equal the lands instrument set exactly, `missing == []`, `dead == []`.
- `registered` must be at least the number of data rows in `## Gates and probes`, because o83 grades
  `reg >= len(rows) - 1` over a parse that includes the header row (`accept-o83.py:139-160`,
  `:43-63`). At the expected lands table (60 + 14 = 74 data rows) that means `registered >= 74`. The
  claim line's `<r>` is therefore 74 at the expected end state, and `<i>` is 61.

## Peer reconciliation (worktree state, measured; frozen object remains the census basis)

`ScribeRegistryRows` inserted 14 rows into the worktree `SKILL.md`; the additions are the same 14
names as this census's missing set (only the within-block order of the three round-83 rows differs —
no coverage effect). Measured on the worktree with this census's rules:

- instruments: **61**; table data rows: **74**; missing: **0**; dead `.py` tokens in entry-command
  cells: **0**.

That is exactly the after-state the claim's line needs (`0 missing / 74 registered / 61 instruments /
0 dead`, subject to the tool's own count). Two derivation differences surfaced in the cross-read, both
resolved toward the committed code:

1. `accept-d-80`: the docstring lists a lint-tool sha256 mismatch as an exit-2 refusal, but the code
   grades it as a `LINT` leg failure (`reports/round-80/accept-d.py:248-251`); the proposed verdict
   cell has been corrected to say so.
2. `accept-o-79` / `accept-o-81`: the `red.json`/`green.json`/`refusals/` and `absent.py` path
   literals sit in the selftest fixture builders (`_st_fixture_repo` / `selftest`), not in the graded
   legs; the proposed pinned-values cells now name the frozen config pins and mark those literals as
   selftest-only. `ScribeRegistryRows`' Finding 2 reports the same distinction.

`ScribeRegistryRows` Finding 5 records that the three round-83 counters were revised in the worktree
after the freeze (loop-variable fixes in `missing_of`/`rows_leg`, tool materialisation, a `None`
guard, `C.NoOp` in the junk battery). The defect measured below is against the **frozen** bytes and
stands there; the worktree revision already carries the fix, so the fixed counter bytes (not the
frozen ones) must be what lands if claim O is to be graded green by its own counter.

## Defect and risk register

1. **accept-o83.py cannot reach exit 0 as frozen (leg defect, not a row-description problem).**
   `registry_rows()` appends `(cells, lineno)` (`reports/round-83/accept-o83.py:62`) while
   `missing_of()` (`:67`) and `rows_leg()` (`:166`) test `p in c[2]` behind `len(c) > 2`. A two-tuple
   never satisfies that guard, so both functions classify **every** instrument as missing. Measured
   on the frozen `SKILL.md` with those exact semantics: 61/61 reported missing instead of 14/61, and
   every prepared row path reported absent. Consequences: the REGISTRY leg (`:139-160`) and the ROWS
   leg (`:164-167`) can never pass, so the counter cannot exit 0; two of its three `--junk` trials
   (`rows-dropped`, `canned-tool`, `:235-237`) pass vacuously because the target leg is already red.
   `dead_of()` (`:70-77`) unpacks tuples correctly, so DEAD is unaffected. The row proposed above is
   still the correct registry entry (8 legs, 0/1/2 exits, exact files); I do not amend the counter.
   **L1 decision needed**: land the revised counter (the worktree fix reported by
   `ScribeRegistryRows`), or grade claim O with this defect recorded. Claim O's after-state line is
   unaffected; only whether the frozen o83 can grade it green is.
2. Six existing rows (rounds 66–67, `SKILL.md:686-691`) are not 8-cell parseable because of a literal
   `|` in the verdict-map cell. Entry-command coverage is unaffected. A strict registry tool should
   split on `|` and require at least 3 cells (as o83 does), not exactly 8; the 14 proposed rows avoid
   `|` everywhere.
3. `reports/round-76/accept-c.py:6381-6395` lists the leg name `INDEX` twice (13 entries total) and
   has no SEPARABLE leg; its printed denominator is 13. The row records 13 legs, which is what the
   counter prints. Flagged for calibration; not a blocker.
4. The three round-83 counters have no `--selftest`; their `--junk` battery is a mutation test, not a
   self-test, so the rows state `—` for the self-test cell, matching the house wording used by
   `accept-c-71` and `accept-ca-71` (rows 698–699).
5. `accept-c-76` and `accept-ca-76` selftests refuse to run when no scratch root exists rather than
   writing under the system temporary directory (`accept-c.py:6531-6537`, `accept-ca.py:3739-3743`);
   the self-test and write-scope cells state this.

## Authoritative reading (R82-M3)

`ScribeRows`' fetch receipts bind the registry rows; `ScoutSources`' reading is the independent
second reading. This census is a third, purely byte-derived reading of the frozen commit. If either
seat's byte count or quote differs from the numbers above — 61 instruments, 60 data rows, 47 covered,
14 missing, and the file:line evidence quoted per row — the difference must be reported and
reconciled against the committed bytes at `21277b0…`, never silently resolved. No such disagreement
exists in the material available to me: the claim-D source receipts and this census count different
objects (sources vs counter rows), and the registry-row seat's counts agree (60 → 74 data rows).

## Limits

- Static description only: the counters were not executed, so verdict maps quote declared code paths
  (format strings, return sites, argparse) rather than observed runs.
- Coverage is the claim's substring test on the entry-command cell; a counter named only in another
  cell does not count.
- Absolute paths are deliberately absent from this file and the JSON (QUALITY 31); every citation is
  repo-relative.
