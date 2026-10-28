# ExecAdaptJunk — round-77 junk-landing fixtures (W1, BUILD)

Seat: leaf executor, kotodama round 77 (hyaku run 10), wave 1. Lane
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`, lane base
`211f9526800906e0c585d878d265c37e5e090c15`. No lane writes, no fleet writes, no
jj/git mutation in the lane, no subagents, no background jobs, no installs.

## Files

| path | what |
|---|---|
| `.ufo/waves/round-77/w1/stage/ExecAdaptJunk/junk-fixtures.py` | the round-77 fixture generator (adapted from `reports/round-76/counters/junk-fixtures.py`; 2475 lines — `wc -l`) |
| `.ufo/waves/round-77/w1/stage/ExecAdaptJunk/receipt.md` | fixture set, per-class red-before table, dry-run table, freeze command |
| `.ufo/waves/round-77/w1/stage/ExecAdaptJunk/redbefore-r76.txt` | raw red-before runs (round-76 counters) |
| `.ufo/waves/round-77/w1/stage/ExecAdaptJunk/redbefore.py` | the reproducible red-before driver (stdlib only) |
| `.ufo/waves/round-77/w1/stage/ExecAdaptJunk/r76-ca-lands.txt` | round-76 Ca counter at its own lands (raw) |
| `.ufo/waves/round-77/w1/stage/ExecAdaptJunk/r76-c-lands.txt` | round-76 C counter at its own lands (raw) |
| `.ufo/waves/round-77/w1/stage/ExecAdaptJunk/dryrun-round77.txt` | round-77 fixtures materialized on a SYNTHETIC config, ungraded |

No tracked lane file was created, edited or deleted: the only writes are this report
(`.ufo/waves/round-77/w1/ExecAdaptJunk.md`) and the seven artifacts under
`.ufo/waves/round-77/w1/stage/ExecAdaptJunk/`. `git -C … status --porcelain` still prints only the
two pre-existing untracked directories `.ufo/waves/round-77/` and `reports/round-77/`.

## Behaviour

The generator builds one junk landing per fixture in a private `git clone --shared` of the lane,
commits the single defect, and grades it with the round-77 counter — or, with `--no-grade` /
`--synthetic-config`, only materializes it and claims no verdict. Round-77 leg names throughout:
C-side `ENTRIES`, `EVIDENCE`, `GATE`, `FROZENCFG`, `ROWS`, `INDEX`; Ca-side `LEDGER`, `ANNOTATE`,
`APPENDONLY`, `SEPARABLE`, `R1EXEMPT`.

Fixture set (14 = 12 J + G/R; `python3 -B junk-fixtures.py --list | wc -l` → 15 lines including the
header):

| fixture | claim | expected leg (first = required red) | must-pass | mutation |
|---|---|---|---|---|
| J1 | C | ENTRIES | — | header-only stub at the frozen entry path, its row's `used-by` naming the stub |
| J2 | C | EVIDENCE (GATE reported) | — | U+2588 filler over the stored windows (measured r76 detail: the quote removed from 3 evidence files, `no row was paired verbatim`); `window-sha256`/`window-bytes` recomputed so the only failing sub-check is the quote |
| J3 | C | FROZENCFG | — | graded-tree `claims.json` shrinks claim C (last row dropped) |
| J4 | Ca | LEDGER | — | FREEZE's every `observe_cmd` = literal constant printer |
| J4b | Ca | LEDGER | — | same, evasive `import os;assert os.sep;print(str(...))` |
| J5 | Ca | ANNOTATE | — | `## Corrections — round 77` row reduced to its id |
| J6 | Ca | APPENDONLY | — | in-place edit of a frozen receipt outside the protected set |
| J7 | Ca | SEPARABLE | — | corrections row cites a claim-C lane id |
| J8 | Ca | LEDGER | — | FREEZE pair's `stated_at` moved outside the frozen allowlist, `stated_text` still present there |
| J9 | Ca | LEDGER | — | FREEZE pair's `stated_text` absent at its `stated_at` |
| J10 | Ca | LEDGER | — | FREEZE pair's `grep -E` pattern operand holds `\|`, no pattern-operand mark |
| J11 | C | INDEX | ROWS | frozen `required_sections[]` Paths/Search-log lines removed; ROWS must stay green |
| G / R | Ca | APPENDONLY green / red | — | only a rule-2 `used-by` edit / only a `teaches` edit on one pre-existing row |

Round-77 adaptations of the round-76 machinery, each driven by a measured round-76 outcome:

* **Leg names** come from the round-77 tables (the module docstring lists them and `--selftest`
  asserts every fixture's expected legs belong to them).
* **`OWN_FREEZE` = {J4, J4b, J8, J9, J10}.** `LEDGER` reads the contract at the freeze, so a
  lands-only ledger edit can only reach `FROZENCFG`; these fixtures therefore commit the defective
  ledger as their own freeze and hang an empty landing off it (`<freeze>` a strict ancestor of
  `<lands>`).
* **Frozen `stated_at` allowlist** (`LOG.md`, `SCORECARD.md`, `corpus/lessons/round-75.md`,
  `corpus/lessons/round-76.md`; `corpus/README.md` excluded as REPAIR-only) and the
  **pattern-operand clause** are implemented as helpers (`stated_at_allowlist()`,
  `pattern_operand_defect()`), not as ad-hoc string checks.
* **`required_sections[]`** is read from the frozen claim C in both shapes
  (`{path, section|match}` dicts and bare headings) and drives J11.
* **Counter argv**: both claims get `--work`; Ca additionally gets the counter's required
  `--combined` (CLI `--combined`, default = the fixture's own landing) and `--main`.
* **No-op guard**: `build()` compares seeded-file bytes before and after the mutation and raises
  `committed no byte change beyond the seeded config`. This is what caught J3's fixed truncation.
* **Expectation semantics**: `expected_legs[0]` must be red, further names are reported
  (also-expected), `must_pass` legs must be green; the CLI exits 2 if any fixture is unmatched.
* Removed from the round-76 file as dead or superseded: `J4c` (shell string), `J4m` (min-pairs),
  `J4f` (folded into J4/J4b as `OWN_FREEZE`), the teaches-cell `J7` (the class survives as `R`),
  the line-removal `J10` and the typed-receipt `J9` (not in this wave's assigned set), and
  `j10_candidates()`.

## Evidence (each number with the command that produced it)

Round-77 counters do not exist at this point of the round — `find reports/round-77 .ufo/waves/round-77
-maxdepth 1 -type f | sort` lists only `build-w1.py`, `CLAIMS-DRAFT.md`, `w1.ready*`, and
`reports/round-77/` holds `telemetry` alone. **No round-77 verdict is claimed.**

### Red-before, round-76 counter at its own landings

```
$ python3 -B reports/round-76/accept-ca.py --root . --lands a43ed807ea38b5fc5a7875a839d576cea73aba7c \
  --freeze df0f0309d61e5485bb17035d3f8791b1e6a11d40 --fleet-root /home/vgpnk/Projects/shokunin \
  --combined 722e69ff6361aadf148cb46acbf6ac8fd147f59a --main a43ed807ea38b5fc5a7875a839d576cea73aba7c \
  --work /fast/scratch/hyaku/kotodama-r77/ExecAdaptJunk/work-ca
ACCEPT-CA-76: FAIL legs=5/12                      (exit 1, 20 s)
LEG FAIL LEDGER  problems=2 ["L76-13: ANNOTATE stated_at path corpus/knowledge/myth-symbol/narrative-structure-frameworks.md is not one of the frozen append-only files …", 'L76-19: stated_text not found in corpus/lessons/round-75.md at base']
LEG FAIL ANNOTATE  unannotated=3 ["L76-19(rederive not executable: git grep path operand 'chars=' does not exist in the clone)", "L76-20(rederive not executable: … '98c486bdb4650ba5b8e651d332910e8ee60ad121' …)", "L76-21(…)"]
```

```
$ python3 -B reports/round-76/accept-c.py --root . --lands c792ea50f1cfba2b56c16a0f5102b2877fd2eefd \
  --freeze df0f0309d61e5485bb17035d3f8791b1e6a11d40 --fleet-root /home/vgpnk/Projects/shokunin \
  --work /fast/scratch/hyaku/kotodama-r77/ExecAdaptJunk/work-c
ACCEPT-C-76: FAIL legs=11/13                      (exit 1, 2 s)
LEG FAIL ROWS  registry line added outside the frozen row_set: '- calendar-standard design — S896 → S895 → S894: start with '; registry line added outside the frozen row_set: '**State-standard calendar compilation (round 76).** Question'
```

### Red-before per round-77 class (fixture commits + verdicts in `redbefore-r76.txt`)

| r77 fixture | r76 verdict | the leg |
|---|---|---|
| J1 | `ACCEPT-C-76: FAIL legs=7/13` | `LEG FAIL ENTRIES` |
| J2 | `ACCEPT-C-76: FAIL legs=10/13` | `LEG FAIL EVIDENCE`, `LEG PASS GATE` |
| J3 | `ACCEPT-C-76: FAIL legs=10/13` | `LEG FAIL FROZENCFG` |
| J4 | `ACCEPT-CA-76: FAIL legs=4/12` | `LEG FAIL LEDGER` |
| J4b | `ACCEPT-CA-76: FAIL legs=4/12` | `LEG FAIL LEDGER` |
| J5 | `ACCEPT-CA-76: FAIL legs=5/12` | `LEG FAIL ANNOTATE` |
| J6 | `ACCEPT-CA-76: FAIL legs=4/12` | `LEG FAIL APPENDONLY` |
| J7 | `ACCEPT-CA-76: FAIL legs=5/12` | `LEG FAIL SEPARABLE` |
| J8 | `ACCEPT-CA-76: FAIL legs=5/12` | `LEG FAIL LEDGER  problems=1 [L76-13 out-of-allowlist stated_at]` |
| J9 | `ACCEPT-CA-76: FAIL legs=6/12` | `LEG FAIL LEDGER  problems=1 [L76-19 stated_text not found]` |
| J10 | `ACCEPT-CA-76: FAIL legs=6/12` | **`LEG PASS LEDGER  pairs=19 min=10 source=freeze`** — r76 accepts the escaped-pipe operand |
| J11 | `ACCEPT-C-76: FAIL legs=12/13` | `LEG PASS ROWS` with the required lines removed (and `LEG FAIL ROWS` at r76's own landing, above) |

Fixture commits seen by those runs (scratch clones, deleted on yield; `lands` unless an own freeze
is named): J1 `e217952fa44b`, J2 `80255bd4d6b0`, J3 `132464d45a68`, J4 `7d2b045d0317` (freeze
`8a8b558119b3`), J4b `8a6d3eda0934` (freeze `47f1d04c54d0`), J5 `23f169a02775`, J6 `e3ec1cd19fce`,
J7 `5cff9b0462b2`, J8 `5b6cac13d553` (freeze `e937256a9d14`), J9 `dc6ced82af3e` (freeze
`bc54b2ef063a`), J10 `61930cf13b36` (freeze `eea7917c823a`), J11 `fc64504d0fd8`; the full argv for
each is in `redbefore-r76.txt`.

### Round-77 materialization (dry run, ungraded)

```
$ python3 -B junk-fixtures.py --run --freeze 211f9526800906e0c585d878d265c37e5e090c15 \
  --base 211f9526800906e0c585d878d265c37e5e090c15 --lands 211f9526800906e0c585d878d265c37e5e090c15 \
  --synthetic-config --work /fast/scratch/hyaku/kotodama-r77/ExecAdaptJunk/dryrun --out dryrun-round77.txt
```

10 of 14 fixtures materialized: J3 `0f3a343030f9` (lands), J4 `5914a78958a4` (freeze `bde356c10241`), J4b `91a113c18b79` (freeze `3386ff90f3bf`), J6 `510d1a7ce792`, J7 `ec0eb917f510`, J8 `6096fda16baf` (freeze `1f935392425b`), J9 `2555b2ff4466` (freeze `b2f388ff1b36`), J10 `d76f1dc7049b` (freeze `83f7892e2754`), G `8e736f97a5c8`, R `cdbc607c149c` — 10 — `grep -c '^lands:' stage/ExecAdaptJunk/dryrun-round77.txt`.
4 are freeze-gated with an explicit reason: J1 `no registry row S897 in the tree`, J2 `no evidence
file for the adopted rows ['S897','S898']`, J5 `SCORECARD carries no '## Corrections — round 77'
section`, J11 `corpus/SOURCES.md carries no line matching '- naming-systems design — S897'` — 4 —
`grep -c '^error: FixtureError' stage/ExecAdaptJunk/dryrun-round77.txt`. Every dry-run row prints
`graded: no (dry run: no verdict is claimed)` and the seeds it wrote as `(SYNTHETIC)`.

```
$ python3 -B junk-fixtures.py --selftest
SELFTEST: PASS
```

## Findings worth routing

1. **The round-76 fixture generator never passed `--combined`**, which the round-76 Ca counter
   makes mandatory: grading any Ca fixture with it returns `exit: 2` and `ACCEPT-CA-76: FAIL
   legs=0/12` with no `LEG` line. Measured: one 1.1 s run of
   `reports/round-76/counters/junk-fixtures.py --run --freeze df0f0309… --lands a43ed807… --only J5`
   printed `exit: 2`, `verdict: ACCEPT-CA-76: FAIL legs=0/12`, `red-legs: (none)`. The round-77
   generator passes `--combined`/`--main`/`--work` itself (`_counter_extra()`).
2. **J10 is a measured round-76 blind spot**: `observe_problem()` skips the shell-metacharacter
   check for `grep` pattern operands entirely, so `grep -c -E 'zzz\|zzz' corpus/SOURCES.md` passes
   `LEDGER` with `problems` empty. The round-77 clause the draft adds is the only thing that
   refuses it; `pattern_operand_defect()` is the reference implementation and `--selftest` covers
   refused / marked / plain.
3. **J11 is a measured round-76 false positive**: `ROWS` counts any added non-row line as
   out-of-set, so the two required Paths/Search-log lines fail it at the round-76 landing; the same
   tree minus those two lines passes `ROWS` with the row append untouched (`ACCEPT-C-76: FAIL
   legs=12/13`, only `COLLCHECK` red).
4. **The round-76 J1 shape cannot be reused**: it required two frozen entries; round 77 adopts ONE
   entry, so J1 now stubs the single entry and points its row's `used-by` at the stub.
5. **J3 must be a delta, not a shape**: "keep two rows and one entry" is a no-op on a claim that
   already holds two rows and one entry; the mutation now drops the last row (and a surplus entry),
   and the no-op guard would refuse the silent version.

## Risks / open items for the L1

* **No round-77 verdict exists yet.** The fixtures are ungraded against the round-77 counters; the
  freeze-time run is `reports/round-77/junk-fixtures.py --run --freeze … --lands … --base …
  --combined … --work … --out-dir reports/round-77/fixtures` (in `receipt.md`). Exit 0 = every
  expectation met.
* **Four fixtures need the landed tree** (J1, J2, J5, J11): mount them on the C landing (rows,
  evidence, required lines) and the Ca landing (corrections section), not on the freeze.
* **Assumed contract shapes** the generator reads from the frozen files: `claims[].row_set[]`
  (`id`, `document`), `claims[].required_sections[]` (`path` + `section`/`match`), `ledger.pairs[]`
  (`stated_at`, `stated_text`, `observe_cmd`, `expected_after`, `disposition`) and an optional
  `pattern_operand` mark on a pair. If the frozen ledger names the mark differently, add the key to
  `PATTERN_MARK_KEYS` (one line).
* **The APPENDONLY protected set is derived by `protected_set(77)`** (LOG.md, SCORECARD.md, lessons
  76/75, corpus/QUALITY.md, SHONEN.md, reports/round-76 and round-75 config). If the frozen Ca
  clause freezes a different list, J6's "outside the protected set" choice and the `G`/`R` pair
  must be re-aimed; the function is the single place to change.
* **G/R (R1EXEMPT) red-before was not re-measured** against the round-76 counter in this wave (the
  round-76 generator ships both halves). Reported as unrun.
* The dry-run commit hashes are scratch-clone hashes; the clones were removed on yield, so they are
  traceability ids, not reproducible references.

Tooling: nothing installed, nothing upgraded (no pacman, no uv/npx/binary installs). Scratch used
`/fast/scratch/hyaku/kotodama-r77/ExecAdaptJunk/` and was deleted before yield; fixtures and
receipts were copied into the wave dir first.
