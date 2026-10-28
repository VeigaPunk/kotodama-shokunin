# ExecAdaptJunk — round-77 junk-landing fixtures, receipt

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, round 77 (hyaku run 10), wave 1.
Lane base for this round: `211f9526800906e0c585d878d265c37e5e090c15`.
Operator date: 2026-10-27. Seat: leaf; no subagents, no background jobs, no lane writes.

## What this receipt is

Three artifacts, three different kinds of evidence, never mixed:

| artifact | what it is | what it may be cited for |
|---|---|---|
| `junk-fixtures.py` | the round-77 fixture generator (adapted from `reports/round-76/counters/junk-fixtures.py`) | the fixture set, its expected legs, its mutations |
| `redbefore-r76.txt` (+ `redbefore.py`, `r76-ca-lands.txt`, `r76-c-lands.txt`) | round-76 counter runs on round-76 trees carrying the same defect classes | the r76 verdict per class — measured, quoted verbatim |
| `dryrun-round77.txt` | round-77 fixtures materialized on the lane base with a SYNTHETIC round-77 config, **not graded** | that each mutation applies and what it changes — never a verdict |

Round-77 counters do not exist yet, so **no round-77 verdict is claimed anywhere in this
receipt**. Evidence of that absence, run in the lane at 2026-10-27:

```
$ find reports/round-77 .ufo/waves/round-77 -maxdepth 1 -type f | sort
.ufo/waves/round-77/build-w1.py
.ufo/waves/round-77/CLAIMS-DRAFT.md
.ufo/waves/round-77/w1.ready
.ufo/waves/round-77/w1.ready.dispatched
$ ls reports/round-77/
telemetry
```

## The fixture set (round-77 leg names)

`python3 -B junk-fixtures.py --list` — 12 J-fixtures plus the R1EXEMPT pair:

| fixture | claim | expected leg(s) | must pass | class |
|---|---|---|---|---|
| J1 | C | ENTRIES | — | header-only stub entry at the frozen entry path, its row's `used-by` naming the stub |
| J2 | C | EVIDENCE (GATE reported) | — | the Gate admit quote is absent from every stored evidence window; the window sha256 still recomputes |
| J3 | C | FROZENCFG | — | the graded tree's `claims.json` shrinks claim C (last row dropped) |
| J4 | Ca | LEDGER | — | the FREEZE's every `observe_cmd` is a literal constant printer |
| J4b | Ca | LEDGER | — | the same, evasive (`import os;assert os.sep;print(str(...))`) |
| J5 | Ca | ANNOTATE | — | a `## Corrections — round 77` row names only its id |
| J6 | Ca | APPENDONLY | — | a frozen receipt outside every protected set is edited in place |
| J7 | Ca | SEPARABLE | — | a Ca corrections row cites a claim-C lane id |
| J8 | Ca | LEDGER | — | a FREEZE pair's `stated_at` is outside the frozen allowlist (r76-routed L76-13) |
| J9 | Ca | LEDGER | — | a FREEZE pair's `stated_text` is absent at its `stated_at` (r76-routed L76-19) |
| J10 | Ca | LEDGER | — | a FREEZE pair's `grep -E` pattern operand carries an escaped pipe, unmarked (r76-routed argv class) |
| J11 | C | INDEX | ROWS | NEGATIVE: the frozen `required_sections[]` Paths/Search-log lines are removed; ROWS must stay green |
| G | Ca | (APPENDONLY green) | — | only a rule-2 `used-by` cell edit on one pre-existing row |
| R | Ca | (APPENDONLY red) | — | only a non-rule-2 `teaches` cell edit on the same row |

Semantics of an expected leg list, as implemented in `_expectation()`:
`expected_legs[0]` MUST be red (the leg the fixture exists to reach); further names are legs the
same defect may also reach and are printed but not required; `must_pass` legs must be green.

## Red-before: the round-76 counter's verdict on the same classes

Command (round-76 Ca counter; the C counter takes `--work` and no `--combined`):

```
python3 -B reports/round-76/accept-ca.py --root <fixture clone> --lands <fixture lands> \
  --freeze <fixture freeze> --fleet-root /home/vgpnk/Projects/shokunin \
  --combined <fixture lands> --main <fixture lands> \
  --work /fast/scratch/hyaku/kotodama-r77/ExecAdaptJunk/redbefore-work
python3 -B reports/round-76/accept-c.py --root <fixture clone> --lands <fixture lands> \
  --freeze df0f0309d61e5485bb17035d3f8791b1e6a11d40 \
  --fleet-root /home/vgpnk/Projects/shokunin --work <scratch>
```

Round-76 references used: freeze `df0f0309d61e5485bb17035d3f8791b1e6a11d40`,
Ca lands `a43ed807ea38b5fc5a7875a839d576cea73aba7c`, C lands `c792ea50f1cfba2b56c16a0f5102b2877fd2eefd`.

| r77 fixture | r76 tree carrying the same class | r76 verdict (verbatim line) | the leg |
|---|---|---|---|
| J1 | frozen entry replaced by a 10-line header, `S894.used-by` → the stub | `ACCEPT-C-76: FAIL legs=7/13` | `LEG FAIL ENTRIES` |
| J2 | U+2588 filler over the stored windows (measured detail: `the Gate quote removed from the stored window of 3 evidence file(s) (no row was paired verbatim)`) | `ACCEPT-C-76: FAIL legs=10/13` | `LEG FAIL EVIDENCE`; `LEG PASS GATE` |
| J3 | graded-tree `claims.json` shrunk (`reports/round-76/counters/junk-fixtures.py` J3) | `ACCEPT-C-76: FAIL legs=10/13` | `LEG FAIL FROZENCFG` |
| J4 | frozen ledger, every `observe_cmd` literal (r76 J4f) | `ACCEPT-CA-76: FAIL legs=4/12` | `LEG FAIL LEDGER` |
| J4b | frozen ledger, evasive printer | `ACCEPT-CA-76: FAIL legs=4/12` | `LEG FAIL LEDGER` |
| J5 | `Corrections — round 76` row for L76-01 reduced to `\| L76-01 \|` | `ACCEPT-CA-76: FAIL legs=5/12` | `LEG FAIL ANNOTATE` |
| J6 | r76's selected receipt `reports/round-74/telemetry/accept-ca-73-at-lands.txt` edited in place (`legs=9/9` → `legs=9/10`) | `ACCEPT-CA-76: FAIL legs=4/12` | `LEG FAIL APPENDONLY` |
| J7 | corrections row citing claim-C lane id (r76 J8) | `ACCEPT-CA-76: FAIL legs=5/12` | `LEG FAIL SEPARABLE` |
| J8 | r76 frozen ledger with L76-19 made verbatim; L76-13's out-of-allowlist `stated_at` is the only problem left | `ACCEPT-CA-76: FAIL legs=5/12` | `LEG FAIL LEDGER  pairs=20 min=10 source=freeze problems=1 ["L76-13: ANNOTATE stated_at path corpus/knowledge/myth-symbol/narrative-structure-frameworks.md is not one of the frozen append-only files ['LOG.md', 'SCORECARD.md', 'corpus/lessons/round-75.md', …"]` |
| J9 | r76 frozen ledger with L76-13 removed; L76-19's absent `stated_text` is the only problem left | `ACCEPT-CA-76: FAIL legs=6/12` | `LEG FAIL LEDGER  pairs=19 min=10 source=freeze problems=1 ['L76-19: stated_text not found in corpus/lessons/round-75.md at base']` |
| J10 | clean r76 ledger; `observe_cmd = grep -c -E 'zzz\|zzz' corpus/SOURCES.md`, expected `0` | `ACCEPT-CA-76: FAIL legs=6/12` | **`LEG PASS LEDGER  pairs=19 min=10 source=freeze`** — the r76 guard accepts it |
| J11 | r76 C landing with its 2 required Paths/Search-log lines removed (rows untouched) | `ACCEPT-C-76: FAIL legs=12/13` | `LEG PASS ROWS` (and at r76's own landing, with the lines: `LEG FAIL ROWS   registry line added outside the frozen row_set: '- calendar-standard design — S896 → S895 → S894: …'; registry line added outside the frozen row_set: '**State-standard calendar compilation (round 76).** Question…'`) |

Two readings matter for the freeze:

1. **J10 is a measured blind spot, not a red leg.** The round-76 counter refuses interpreters,
   shell strings and non-allowlisted binaries, but it skips the shell-metacharacter check on a
   `grep` pattern operand wholesale, so `grep -c -E 'zzz\|zzz'` passes `LEDGER` with no problem
   reported. The round-77 clause ("no `grep -E` pattern operand holds a backtick or escaped pipe
   unless marked pattern-operand") is what J10 exercises; `pattern_operand_defect()` in the
   generator is the reference implementation of that clause.
2. **J11 is a measured false positive.** The r76 `ROWS` leg counts every added non-row line as
   "outside the frozen row_set", so the two REQUIRED Paths/Search-log lines fail it at r76's own
   landing; removing those two lines and nothing else makes `ROWS` pass while the row append is
   untouched. Round 77 scopes `ROWS` to `| S### |` lines inside the frozen `row_set` and moves the
   required lines to `required_sections[]`/INDEX; J11 is the negative control for exactly that.

The G/R (R1EXEMPT) pair was **not** re-measured against the round-76 counter in this wave; the
round-76 generator ships both halves and they were exercised there. Reported as unrun here.

## Dry run: the round-77 fixtures materialize

Synthetic config only (a round-77-SHAPED `reports/round-77/{claims,ledger}.json` written into the
fixture tree, labelled `SYNTHETIC` in every row's `seeded-config:` line). No counter ran; the CLI
returns 0 and every row says `graded: no`.

```
$ python3 -B junk-fixtures.py --run \
    --freeze 211f9526800906e0c585d878d265c37e5e090c15 \
    --base   211f9526800906e0c585d878d265c37e5e090c15 \
    --lands  211f9526800906e0c585d878d265c37e5e090c15 \
    --synthetic-config --work /fast/scratch/hyaku/kotodama-r77/ExecAdaptJunk/dryrun \
    --out dryrun-round77.txt
```

| fixture | fixture commit (scratch clone) | own freeze | defect path(s), synthetic seeds excluded | state |
|---|---|---|---|---|
| J1 | — | — | — | gated: `no registry row S897 in the tree (the stub entry cannot be paired with a row)` |
| J2 | — | — | — | gated: `no evidence file for the adopted rows ['S897', 'S898']` |
| J3 | `0f3a343030f9` | no (base) | `reports/round-77/claims.json` | materialized; shrink = 1 row, 1 entry |
| J4 | `5914a78958a4` | `bde356c10241` | `reports/round-77/ledger.json` | materialized; every `observe_cmd` a literal printer |
| J4b | `91a113c18b79` | `3386ff90f3bf` | `reports/round-77/ledger.json` | materialized; every `observe_cmd` the evasive printer |
| J5 | — | — | — | gated: SCORECARD carries no `## Corrections — round 77` section |
| J6 | `510d1a7ce792` | no (base) | `reports/round-75/telemetry/measures-ca.txt` | materialized |
| J7 | `ec0eb917f510` | no (base) | `SCORECARD.md` | materialized; corrections row cites a claim-C id |
| J8 | `6096fda16baf` | `1f935392425b` | `reports/round-77/ledger.json`, `corpus/lessons/round-74.md` | materialized; `stated_at` outside the allowlist |
| J9 | `2555b2ff4466` | `b2f388ff1b36` | `reports/round-77/ledger.json` | materialized; `stated_text` marker added |
| J10 | `d76f1dc7049b` | `83f7892e2754` | `reports/round-77/ledger.json` | materialized; escaped-pipe `-E` operand, unmarked |
| J11 | — | — | — | gated: `corpus/SOURCES.md carries no line matching '- naming-systems design — S897'` |
| G | `8e736f97a5c8` | no (base) | `corpus/SOURCES.md` | materialized; rule-2 cell only |
| R | `cdbc607c149c` | no (base) | `corpus/SOURCES.md` | materialized; teaches cell only |

Every fixture commit listed above lives in a scratch clone that this seat deleted on yield; the
hashes are recorded for traceability and are reproducible only by re-running the generator, which
picks its synthetic lines from the lane tree's own allowlisted files.

The generator refuses a no-op mutation: `build()` compares the seeded files' bytes before and after
the mutation and raises `committed no byte change beyond the seeded config` when the only delta is
the seed. J3's shrink was rewritten as a delta (drop the last row / last surplus entry) for that
reason: on the round-77 contract (one entry, two rows) a fixed "keep two rows and one entry"
truncation would have been a silent no-op.

## The command the L1 runs at the freeze

```
python3 -B reports/round-77/junk-fixtures.py --run \
  --freeze <round-77 freeze> \
  --lands  <round-77 C-lands>  \
  --base   <round-77 claim base> \
  --combined <the tree carrying BOTH landings> \
  --work /fast/scratch/hyaku/kotodama-r77/junk-fixtures \
  --out-dir reports/round-77/fixtures
```

Exit code: `0` when every fixture's expectation is met (its named leg red, J11's ROWS green),
`2` when any fixture is unmatched or could not be materialized. The table prints, per fixture, the
counter argv, exit code, the full `LEG` table, the baseline legs, `newly-red`, the expected/required
leg verdicts and `as-expected:`.

Counter argv the generator passes itself (round-77 shapes): `--root/--lands/--freeze/--fleet-root`
plus `--work` for both claims, and `--combined/--main` for claim Ca — because the round-77 Ca
counter refuses to run without `--combined` (the round-76 generator never passed it, so every Ca
fixture it graded at r76 lands was refused with `legs=0/12`).

## Generator self-test

```
$ python3 -B junk-fixtures.py --selftest
SELFTEST: PASS
```

Cases: registry cell splitting with escaped pipes, the constant-printer rewrites, correction-row
stub/append, Gate quote extraction, evidence-window parsing, NFKC folding, round-derived paths, the
frozen `stated_at` allowlist (and that it excludes `corpus/README.md`), the pattern-operand clause
(refused / marked / plain, index computation), `required_sections[]` in both shapes, section spans,
that every fixture's expected legs belong to the round-77 leg tables, and the expectation evaluator
(required-red, must-pass-green, empty leg table).
