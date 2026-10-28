# ExecCaPass — adapted Ca `--selftest` / `--ledger-check` re-run on the real 11-pair ledger (ATTACK)

Seat: wave-2 falsifier, round 77 (hyaku run 10). Lane base
`211f9526800906e0c585d878d265c37e5e090c15` (`git -C <lane> rev-parse HEAD` → that
value; `git status --porcelain` → `?? .ufo/waves/round-77/`, `?? reports/round-77/`
only, `git diff --stat` empty). Counter under test:
`.ufo/waves/round-77/w1/stage/ExecAdaptCa/accept-ca.py`, sha256
`ac2bc93d02932464f9ee43222ffe1d06dd5bf1a0e68fd38bd94e10a991489b2e` (matches the W1
report). Ledger under test: W1's `probe-real-ledger.json`, sha256
`b7509d2b0980f8c5824c417a8359c8f7107d3de6236cf486ac058947915d0704` — the only
11-pair real-base ledger W1 produced (self-labelled `"status": "SCRATCH PROBE —
not a lane file"`). Both copied into scratch; nothing was run from the lane
worktree.

Verdict, three parts:

1. **Reproduced green.** `--selftest` exits 0 with `SELFTEST: 199/199` and its
   stdout is **byte-identical** to the W1 receipt. `--ledger-check` exits 0 with
   `LEDGER-CHECK-77: PASS pairs=11` in all three invocation forms (`-C .` from
   scratch cwd, `-C <lane>`, cwd=lane/`--root .`).
2. **Red-before controls all fire.** 39 structural mutants of the same 11-pair
   ledger each exit 1 with the exact expected problem string; the unmutated
   ledger stays green (G1–G3). 45-control matrix: 45/45 as expected.
3. **That green is not evidence the ledger is valid.** The counter's own
   functions show the 11-pair ledger carries 10 *false* `observed_at_base`
   records (`1` vs real `149`), 10 pairs whose observation has nothing to do with
   their statement, and one REPAIR pair that is **not red at base** and whose two
   parses read different totals (`243` first match vs `253` last match). Graded
   with the same counter's `BASEMISMATCH` and `REPAIR` legs, this ledger is
   **FAIL** on both. `--ledger-check` checks none of those properties, and the
   claims draft's kill rule ("any ledger pair not red at base") is therefore not
   enforced by the pre-freeze build check.

## 1. Environment and scratch

```
python3 --version            → Python 3.14.8
git --version                → git version 2.56.0
scratch                      → /fast/scratch/hyaku/kotodama-r77/ExecCaPass
HYAKU_SCRATCH (selftest)     → <scratch>/work-selftest
--work (ledger-check/controls) → <scratch>/work-lc, <scratch>/work-ctl, <scratch>/work-tok
```

No tool installs (nothing needed; pacman not invoked). No git/jj mutation in the
lane or fleet repo; the counter's observations run in the throwaway base clone it
materializes under `--work`, and my independent re-derivations are read-only
`git -C <lane> show/grep`.
No fixture git repo was needed. Scratch deleted before yield.

## 2. `--selftest` (green, reproducible)

```
cd /fast/scratch/hyaku/kotodama-r77/ExecCaPass
HYAKU_SCRATCH=$PWD/work-selftest python3 -B accept-ca.py --selftest >selftest.out 2>selftest.err
EXIT=0
grep -o "SELFTEST OK: [0-9]* checks across [0-9]* scenarios" selftest.out
  → SELFTEST OK: 199 checks across 51 scenarios
grep -o "^SELFTEST: .*" selftest.out
  → SELFTEST: 199/199
wc -c selftest.out   → 9248
stderr (270 bytes):
  ERROR: --lands must be 40 hex
  ERROR: --lands <40hex>, --freeze <40hex> and --fleet-root are required
  ERROR: --freeze 0000000000000000000000000000000000000000 is not a commit in \
         /fast/scratch/hyaku/kotodama-r77/ExecCaPass/work-selftest/r77-ca-selftest-hkinmkvs/main/lane
```

The three stderr lines are the selftest's deliberate CLI-error probes (its
`cli-errors` scenario, accept-ca.py:3809-3816). Receipt-integrity check:

```
diff -u .ufo/waves/round-77/w1/stage/ExecAdaptCa/selftest-ca.txt <scratch>/selftest.out
  → no output (SELFTEST_RECEIPT_BYTE_IDENTICAL)
diff -u .ufo/waves/round-77/w1/stage/ExecAdaptCa/selftest-ca.err <scratch>/selftest.err
  → differs on ONE line only: the scratch path (…/ExecAdaptCa/r77-ca-selftest-5ikjmjfc/… vs
    …/ExecCaPass/work-selftest/r77-ca-selftest-hkinmkvs/…)
```

The selftest's internal build-check controls are real but narrow
(accept-ca.py:3819-3834): `ledger-check pass` on the selftest's own ledger, and
`ledger-check fail` on a mutant whose only change is
`pairs[0]["stated_text"] = "row A01 entries: 9."` — i.e. a
stated-text-presence mutant, nothing about redness or observation fidelity.

## 3. `--ledger-check` green, three forms

```
LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
BASE=211f9526800906e0c585d878d265c37e5e090c15
python3 -B accept-ca.py --ledger-check ledger.json --root $LANE --base $BASE \
        --work $PWD/work-lc            # cwd = scratch, ledger declares `-C .`
  → LEDGER-CHECK-77: PASS pairs=11   EXIT=0   stderr empty
```

| form | command | raw result |
|---|---|---|
| G1 `-C .`, cwd=scratch | as above | `LEDGER-CHECK-77: PASS pairs=11`, exit 0 |
| G2 `-C <lane>` (+ lane rederive) | ledger rewritten so every `git -C .` → `git -C $LANE` and every rederive likewise | `LEDGER-CHECK-77: PASS pairs=11`, exit 0 |
| G3 cwd=lane, `--root .` | `cd $LANE && … --root .` | `LEDGER-CHECK-77: PASS pairs=11`, exit 0 |

Refusals on the same path (extra runs, not part of the 45-control matrix):

```
--ledger-check without --base   → "ERROR: --ledger-check needs --base <40hex>",   exit 2
no --work, no $HYAKU_SCRATCH, no $TMPDIR
  → "LEDGER-CHECK-77: FAIL (refused: no scratch root: pass --work, or set
     $HYAKU_SCRATCH (preferred) or $TMPDIR; this counter never invents the
     system temp dir)", exit 2
grep -n "/tmp" accept-ca.py | wc -l   → 0
```

## 4. Red-before control matrix (39 red + 3 baseline green + 3 admitted-green)

Driver `controls.py` (stdout → `controls-summary.txt`, one JSON + stdout/stderr
per run under `controls/`). Each red control mutates a deep copy of the same
11-pair ledger, expects exit 1 **and** the named problem string; each green
control expects exit 0.

```
SUMMARY 45/45 controls as expected
```

Baseline (expected green, observed green):

| id | mutation | exit | verdict line |
|---|---|---|---|
| G1 | none, cwd=scratch, `-C .` | 0 | `LEDGER-CHECK-77: PASS pairs=11` |
| G2 | none, `-C <lane>` form | 0 | `LEDGER-CHECK-77: PASS pairs=11` |
| G3 | none, cwd=lane, `--root .` | 0 | `LEDGER-CHECK-77: PASS pairs=11` |

Red controls (expected and observed exit 1; problem lines verbatim, prefix
`LEDGER-CHECK-77: FAIL pairs=11 problems=N` on every one):

| # | mutation | observed problem line |
|---|---|---|
| R01 | `stated_text` → `SEAT-CTRL absent text 0xdeadbeef` | `D01: stated_text not found in LOG.md at base` |
| R02 | `stated_at` `LOG.md:3`→`LOG.md:447` | `D01: stated_text is in LOG.md but NOT on line 447` |
| R03 | ANNOTATE site → `corpus/README.md:755` | `D01: stated_at path corpus/README.md is not in the frozen ANNOTATE allowlist ['LOG.md', 'SCORECARD.md', 'corpus/lessons/round-75.md', 'corpus/lessons/round-76.md']` |
| R04 | ANNOTATE site → `SKILL.md:1` | same allowlist refusal (path `SKILL.md`) |
| R05 | `stated_at` `fleet:LOG.md:3` | `D01: stated_at='fleet:LOG.md:3' is not a lane path:line (the round-77 allowlist is lane-only)` |
| R06 | `stated_at` `LOG.md:999999` | `D01: stated_at LOG.md:999999 beyond EOF (4349 lines)` |
| R07 | `stated_at` `corpus/nope-not-a-file.md:3` | allowlist refusal + `stated_at path corpus/nope-not-a-file.md absent at base` |
| R08 | REPAIR site → `LOG.md:3` | `D11: stated_at path LOG.md is not in the frozen REPAIR allowlist ['corpus/README.md', 'SKILL.md', 'SHONEN.md']` (+ `stated token cannot be derived`) |
| R09 | drop REPAIR `statement_after` | `D11: REPAIR without a statement_after object (the frozen REPAIR sentence names it)` |
| R10 | `statement_after.path` → `LOG.md` | `D11: REPAIR statement_after path LOG.md is not one of the frozen mutable files [...]` |
| R11 | `statement_after.parse` `"Total knowledge"` (no group) | `D11: statement_after.parse has no capture group` |
| R12 | `observe_cmd` as shell string | `D01: observe_cmd observe_cmd is a shell string, not an argv list` |
| R13 | drop `-C .` from git argv | ``D01: observe_cmd git argv must open with `-C <dir>`: the round-76 `git <sub> ... <rev> ...` form without -C is refused`` |
| R14 | `git -C . push origin main` | `D01: observe_cmd git subcommand 'push' not in the read-only allowlist [...]` |
| R15 | 40-hex moved after `--` | `D01: observe_cmd git grep path operand '211f9526…' does not exist in the clone` |
| R16 | append `X=1` operand | `D01: observe_cmd git grep path operand 'X=1' is a bare name=value assignment (refused)` |
| R17 | append an escaped-pipe operand as an extra argv element | `D01: observe_cmd shell construct …` (verbatim below) |
| R18 | rederive path operand `` `x` `` | ``D01: rederive shell construct '`' in argv element '`x`'`` |
| R19 | `python3 -c print(1)` | `D01: observe_cmd interpreter/constant-printer binary 'python3' is refused (H2)` |
| R20 | `echo 1` | `D01: observe_cmd argv[0] 'echo' not in the observe allowlist ['git','grep','wc','sha256sum','ls','cat','head','tail','cut'] (the echo/printf/interpreter channels are closed)` |
| R21 | unknown binary | same allowlist refusal for `seat-ctrl-no-such-binary` |
| R22 | drop `parse` | `D01: parse missing (a compiling regex with a capture group, or count-presence, is required)` |
| R23 | `parse` `^#` (no group) | `D01: parse has no capture group` + 2 `does not parse at base (parse-miss)` |
| R24 | `parse` `([0-9]` | `D01: parse does not compile: missing ), unterminated subpattern at position 0` (+2 parse-miss) |
| R25 | `expected_after` `""` | `D01: expected_after is not a non-empty string` |
| R26 | git-grep absence observation, `expected_after "1"` | `D01: absence-observation pair (base count 0, expected_after '1')` |
| R27 | `stated_parse` `ZZZ([0-9]+)` | `D01: stated token cannot be derived from stated_text` |
| R28 | `stated_text` `""` | `D01: empty stated_text` + `stated token cannot be derived` |
| R29 | `D02.id` → `D01` | `D01: duplicate id` |
| R30 | 9 pairs | `pairs=9 < the 10-pair floor` |
| R31 | disposition `APPEND` | `D01: disposition='APPEND'` |
| R32 | revision `0`*40 | `D01: observe_cmd git operand 000…0 is not an object of the clone (dead pin)` |
| R33 | `round` 76 | `round=76 != 77` |
| R34 | `claim` `C` | `claim='C'` |
| R35 | ledger `base` `0`*40 | `base='000…0' != --base 211f9526…` |
| R36 | empty argv element | `D01: observe_cmd observe_cmd element is not a non-empty string` |
| R37 | `observe_cmd` object | `D01: observe_cmd observe_cmd is not a non-empty argv list` |
| R38 | grep path `/etc/passwd` | `D01: observe_cmd grep file operand '/etc/passwd' does not exist in the clone` |
| R39 | revision `main` | `D01: observe_cmd git grep revision operand 'main' is a mutable ref (pin a 40-hex or HEAD)` |

R17 verbatim (`controls/R17-escaped-pipe.out`):

```
LEDGER-CHECK-77: FAIL pairs=11 problems=1
     D01: observe_cmd shell construct '|' in argv element 'a\|b'
```

Admitted-green controls (mutants the build check **passes** — the coverage gaps,
not counter defects by its own stated scope):

| id | mutation | exit | verdict |
|---|---|---|---|
| V01 | 11 clones of D01 (same `stated_at`, same `stated_text`, same `observe_cmd`, distinct ids) | 0 | `LEDGER-CHECK-77: PASS pairs=11` |
| V02 | every pair `observed_at_base="999"`, `expected_after="999"` (fabricated) | 0 | `LEDGER-CHECK-77: PASS pairs=11` |
| V03 | 11 clones of D11 (identical REPAIR pair, distinct ids) | 0 | `LEDGER-CHECK-77: PASS pairs=11` |

Every mutant is a deep copy: `ledger.json` itself was never modified
(sha256 `b7509d2b…`, identical to the W1 file), and G1–G3 run the unmutated
ledger in the same driver, so no red is a stale-scratch artifact.

## 5. Falsification of the "real selected 11-pair ledger"

### 5.1 The 11 pairs, as the counter sees them

`token-evidence.py` imports the counter, calls its own `stated_token` /
`observed_token` / `pair_problems` against the lane at base
(`CTX.fleet_root=None`, `RUN_STATE.work` set). Raw output (`token-evidence.txt`):

```
D01 ANNOTATE stated='2026' observed='149' recorded_ob='1' expected='1' red_at_base=True  pair_problems=0
D02 ANNOTATE stated='2026' observed='149' recorded_ob='1' expected='1' red_at_base=True  pair_problems=0
D03 ANNOTATE stated='2026' observed='149' recorded_ob='1' expected='1' red_at_base=True  pair_problems=0
D04 ANNOTATE stated='386'  observed='149' recorded_ob='1' expected='1' red_at_base=True  pair_problems=0
D05 ANNOTATE stated='1'    observed='149' recorded_ob='1' expected='1' red_at_base=True  pair_problems=0
D06 ANNOTATE stated='03'   observed='149' recorded_ob='1' expected='1' red_at_base=True  pair_problems=0
D07 ANNOTATE stated='18'   observed='149' recorded_ob='1' expected='1' red_at_base=True  pair_problems=0
D08 ANNOTATE stated='0'    observed='149' recorded_ob='1' expected='1' red_at_base=True  pair_problems=0
D09 ANNOTATE stated='19'   observed='149' recorded_ob='1' expected='1' red_at_base=True  pair_problems=0
D10 ANNOTATE stated='40'   observed='149' recorded_ob='1' expected='1' red_at_base=True  pair_problems=0
D11 REPAIR   stated='243'  observed='243' recorded_ob=None expected='244' red_at_base=False pair_problems=0
RED_AT_BASE 10/11 ; RECORDED_MATCHES_OBSERVED 0/11
```

Independent re-derivation (`verify-base.py`, raw `git` only, no counter import):

```
D01..D10: on_line=True (stated_text present at the named line, all 11)
D11:      on_line=True, stated='243' observed='243' → red_base=False
git -C $LANE grep -c -E '^#' $BASE -- LOG.md
  → 211f9526800906e0c585d878d265c37e5e090c15:LOG.md:149
```

Facts, therefore:

- **All ten recorded `observed_at_base` values are false.** Every D01–D10 pair
  records `"observed_at_base": "1"`; the command in those pairs returns `149`
  (the count of `^#` lines in `LOG.md` at base). `expected_after` is likewise
  `"1"`. The build check passes because `pair_problems` never compares
  `expected_after`/`observed_at_base` to the execution result (only the type of
  `observed_at_base` is graded, accept-ca.py:1713-1714; `expected_after` only has
  to be a non-empty string, :1643-1644).
- **The ten ANNOTATE pairs are one observation wearing ten ids.** All ten carry
  byte-identical `observe_cmd`, `parse`, `expected_after` and `rederive`; they
  differ only in `stated_at`/`stated_text`. Their "red at base" is syntactic:
  `stated_parse "([0-9]+)"` scrapes an arbitrary number out of the prose line
  (`2026`, `386`, `1`, `03`, `18`, `0`, `19`, `40`), which then differs from the
  `^#`-count token `149`. No pair's observation bears on its statement.
- **D11 is not red at base, and its two parses disagree.** `stated_text` is
  README line 755 `Total knowledge entries: 243.` and the "observation" is
  `grep -o -E "Total knowledge entries: [0-9]+" corpus/README.md` — the same line
  it quotes, so `stated == observed == 243`. Moreover README carries five such
  lines at base:

```
git -C $LANE show $BASE:corpus/README.md | grep -n "Total knowledge entries"
755:Total knowledge entries: 243.
798:Total knowledge entries: 247.
819:Total knowledge entries: 249.
830:Total knowledge entries: 252.
834:Total knowledge entries: 253.
```

  `parse "entries: ([0-9]+)"` uses `re.search` → **first** match = `243`;
  `statement_after.parse "Total knowledge entries: ([0-9]+)\."` uses the **last**
  match of the lands text → `253`. The two sides of the same REPAIR pair can
  never agree. Line 755 is a dated historical snapshot ("Counts checked
  2026-10-25 … total 243 files"); the current total is line 834 = 253, so
  `expected_after: "244"` is not the measured post-state either.

### 5.2 The same ledger under the counter's own graded legs

`graded-legs.py` calls the counter's `evaluate_pairs` +
`leg_basemismatch` + `leg_repair` with `base = lands = <lane>@211f9526`
(raw `graded-legs.txt`):

```
LEG FAIL BASEMISMATCH
     red=10 min=10 ids=['D01','D02','D03','D04','D05','D06','D07','D08','D09','D10'] \
     green-at-base=['D11'] \
     unobserved/miss=["D01:recorded-observed-at-base='1'!='149'", … (all ten) …]
LEG FAIL REPAIR
     green=[] red=["D11(statement='253' truth='243')"]
```

`leg_basemismatch` passes only if there is no green-at-base pair, no miss and
`len(red) >= min_pairs` (accept-ca.py:1873-1874); `leg_repair` reds a pair whose
statement token ≠ observed token (:1924-1930). So the ledger that `--ledger-check`
certifies **FAILS** two graded legs. The BASEMISMATCH half is lands-independent
(it reads base only); the REPAIR half was measured with `lands == base`, and its
first-vs-last parse conflict is a property of the pair, not of the lands tree.

### 5.3 Scope of the build check (accept-ca.py:3904-3969, read directly)

`run_ledger_check` grades: ledger `round`/`claim`/`base`, the 10-pair floor,
duplicate **ids**, and `pair_problems(...)` per pair. It does **not** grade:
`expected_after`/`observed_at_base` fidelity (V02), statement/observation
uniqueness (V01/V03), redness at base (D11, and trivially the scraping pairs), or
whether the ledger file is committed. Its docstring is accurate for LEDGER
("a ledger that passes here cannot fail the LEDGER leg for a defect this check
could see") — but the claims draft's kill rule is broader: "any ledger pair not
red at base" fails claim Ca (`CLAIMS-DRAFT.md:33`), and the draft requires
"≥10 unique pairs" (:29). Neither clause is enforced by the build check, and the
named 11-pair ledger violates both.

## 6. Receipts (all under `.ufo/waves/round-77/w2/stage/ExecCaPass/`)

| file | content |
|---|---|
| `selftest.out` (9248 B), `selftest.err` (270 B) | `--selftest` stdout/stderr, exit 0 |
| `w1-selftest-receipt.txt` | byte-identical copy of the W1 `selftest-ca.txt` (diff empty) |
| `lc-cwdscratch.out`/`.err` | `LEDGER-CHECK-77: PASS pairs=11`, empty stderr |
| `ledger.json` | byte-identical copy of W1 `probe-real-ledger.json` (`diff -q` empty) |
| `controls-summary.txt` | 45-run matrix, `SUMMARY 45/45 controls as expected`, per-run verdict lines |
| `controls/<id>.{json,out,err}` | 45 mutated ledgers + their raw stdout/stderr (V/R/G ids as above) |
| `verify-base.py`/`.txt` | independent `git show`/`git grep` re-derivation of all 11 pairs |
| `token-evidence.py`/`.txt` | counter-function stated/observed table, `RED_AT_BASE 10/11 ; RECORDED_MATCHES_OBSERVED 0/11` |
| `graded-legs.py`/`.txt` | BASEMISMATCH/REPAIR legs on the same ledger (both FAIL) |
| `sha256s.txt` | counter `ac2bc93d…`, ledger `b7509d2b…`, `controls-summary.txt` `ef90d2bd…`, `selftest.out` `a1e70ead…` |

## 7. Risks / notes for the L1

- The W1 sentence "`LEDGER-CHECK-77: PASS pairs=11`" is reproducible but must not
  be quoted as evidence that the paired ledger is valid. Freezing an 11-pair
  ledger shaped like the probe fails BASEMISMATCH (ten recorded observations
  `1` ≠ `149`) and REPAIR (D11 first/last-match conflict) at grading time.
- Build-check hardening candidates (not implemented here; outside this seat):
  compare `observed_at_base`/`expected_after` to the executed observation and
  refuse `stated == observed` for both dispositions — that would make V02 and D11
  red at build time; reject duplicate `(stated_at, observe_cmd)` pairs for the
  "unique pairs" clause.
- If a REPAIR pair targets `corpus/README.md`, its `parse` must be anchored to
  the intended totals line (five matches exist at base; first-match vs last-match
  parse choices disagree). Line 755 is a dated snapshot and must not be repaired.
- Selftest coverage is real (199 checks / 51 scenarios, byte-identical receipt)
  but its only `--ledger-check` red control is a stated-text-presence mutant, so
  the green of the build check is self-validated only for that class.
- Scratch `/fast/scratch/hyaku/kotodama-r77/ExecCaPass` deleted before yield. No
  production file, corpus, LOG/SCORECARD/SKILL/SHONEN, or `reports/` file was
  written; lane `git status` shows only the pre-existing untracked
  `.ufo/waves/round-77/` and `reports/round-77/` trees and `git diff --stat` is
  empty.

Report: .ufo/waves/round-77/w2/ExecCaPass.md
