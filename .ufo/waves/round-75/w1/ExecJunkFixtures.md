# ExecJunkFixtures — round-75 junk-landing fixture generator and the do-nothing runner

Seat: `ExecJunkFixtures` (executor, leaf). Lane: `kotodama-shokunin`, base
`f556d1049fe651d3d63975600b13acd9fb686f15`. Lane HEAD at the time of writing is
that same commit. I did not commit, push, or touch the lane's git/jj state: the
two files below are the only lane writes, and every fixture repository lives in
a mktemp dir under `/fast/scratch/hyaku/kotodama-r75/ExecJunkFixtures/`.

## Files written

| path | sha256 | what it is |
|---|---|---|
| `.ufo/waves/round-75/counters/junk-fixtures.py` | `92994fe08931562de619d62674f76286464a6679758c9915663484a01b306ad9` | the generator (1654 lines, stdlib only, no network) |
| `.ufo/waves/round-75/run-controls.sh` | `1aec1c6551db8df3bfdb65e77a2cda458d0ed2b7cab3e82521d0952cda28567c` | the do-nothing-controls runner, modeled on `.ufo/waves/round-74/run-controls.sh` |

Nothing else in the lane was created or modified. `.ufo/waves/round-75/counters/README.md`,
`capture-evidence.py` and `probe-receipts/` are sibling seats' files; I read them
and did not write them.

## What the generator does

`junk-fixtures.py` materializes, per fixture, a private clone of the lane in a
fresh `mktemp -d` dir under the round-75 scratch root, checks out a reference
tree, applies exactly ONE named defect, commits it **inside the clone only**
(`git rev-parse --show-toplevel` is asserted to be the clone before every
commit), and grades the result with the round-75 counter that owns the defect
(`--root <clone> --lands <fixture-rev> --freeze <fixture-freeze>
--fleet-root /home/vgpnk/Projects/shokunin`).

It is **landing-relative**, not landing-constructing. Round 74's generator
rebuilt an intended landing from the frozen wave-1 drafts; that worked there
because the drafts were in the freeze commit. Round 75's landing is the claim-C
and claim-Ca work product and does not exist at freeze time, so this generator
takes the tree it is pointed at (`--lands`) and mutates that. That is also the
honest construction: a junk fixture is only attributable when the reference
tree is otherwise green, and the receipt prints the unmutated reference tree's
leg table next to the mutant's so a reviewer can see the delta rather than take
the attribution on trust.

The R1EXEMPT pair is the exception: G and R are built on the **freeze** tree,
because the frozen Ca leg asks for "a tree whose only SOURCES delta versus base
is a rule-2 cell edit on one pre-existing row" — building them on the landing
would add claim C's registry appends to that delta and destroy the property the
pair exists to measure.

### Fixtures (a correct counter REFUSES every one)

| fixture | claim | expected failing leg(s) | defect |
|---|---|---|---|
| `J1` | C | `ENTRIES` | two header-only stub entries at the frozen entry paths, with the matching registry rows' `used-by` naming the stubs |
| `J2` | C | `EVIDENCE` | the Gate admit quote is absent from every stored evidence window, while the window keeps its character count and its `window-sha256`/`window-bytes` still recompute |
| `J3` | C | `FROZENCFG` | the graded tree's `claims.json` shrinks claim C to two rows and one entry |
| `J4` | Ca | `FROZENCFG` (+`LEDGER` if the tree's ledger were read) | every `observe_cmd` in the graded tree's ledger constant-prints `expected_after` (literal `python3 -c print(...)` / `echo`) |
| `J4b` | Ca | ditto | the evasive constant printer `python3 -c "import os;assert os.sep;print(str(...))"` — passes a naive argv guard, reads no clone byte |
| `J4c` | Ca | ditto | `observe_cmd` is one shell string carrying `\|`, not an argv |
| `J4m` | Ca | ditto | the ledger carries 2 pairs, below the frozen minimum of 10 |
| `J4f` | Ca | `LEDGER` | the **frozen** ledger itself constant-prints `expected_after` (the fixture's own commit is the freeze) |
| `J5` | Ca | `ANNOTATE`/`NOSTUB` | a `## Corrections — round 75` row names only its id |
| `J6` | Ca | `APPENDONLY` | in-place edit of a frozen receipt outside every protected set |
| `J7` | Ca | `APPENDONLY` | a non-rule-2 (`teaches`) cell edit smuggled beside a rule-2 (`used-by`) edit on the same pre-existing row |
| `J8` | Ca | `SEPARABLE` | a byte in the Ca read set (a Corrections row naming a pair id) cites the claim-C lane id `S885` |
| `J9` | Ca | `RECEIPTS`/`STAMP` | a receipt typed by hand: the stdout was never produced by a run, the counter sha256 is zeroed, and stamped/evaluated/measured name three different revisions |
| `J10` | Ca | `APPENDONLY` | a line is **removed** from a protected file (`corpus/lessons/round-73.md`) |

### The R1EXEMPT pair

| fixture | expectation | defect |
|---|---|---|
| `G` | APPENDONLY **green**, every other leg unchanged | only the `used-by` cell (a rule-2 cell) of one pre-existing row is edited |
| `R` | APPENDONLY **red**, every other leg unchanged | only the `teaches` cell (not a rule-2 cell) of the same pre-existing row is edited |

Both are built on the freeze tree, both edit the same pre-existing row, and the
receipts are written after both halves are graded so each prints the legs that
differ from its counterpart. Receipt grammar `r1exempt-green.txt` /
`r1exempt-red.txt` (one per run, in `--out-dir`):

```
# r1exempt-<green|red>.txt — round-75 R1EXEMPT fixture <G|R>
# claim: Ca   leg under test: APPENDONLY   expectation: <GREEN|RED>
# generated: <UTC>            # fixture: <G|R> — <description>
# mutation: <the exact edit as a sentence>
# freeze: <40hex>             # base: <40hex>
# reference-lands: <40hex>    # fixture-lands: <40hex>   # tree: <40hex>
# counter: <the exact argv>
# changed-paths: corpus/SOURCES.md
# edited-row: S001            # edited-cell: used-by (index 11, rule-2 cell: yes)
# old-cell: <verbatim>        # new-cell: <verbatim>
# sources-delta-vs-base: 1  1  corpus/SOURCES.md
# sources-changed-lines-vs-base: 30
# sources-delta-is-one-changed-line: yes
exit: <n>
ACCEPT-CA-75: <PASS|FAIL> legs=<n>/<m>
LEG PASS|FAIL <name>          (every leg the counter printed)
# baseline-legs: <leg=PASS|FAIL, ...>
# counterpart-fixture: <R|G>  # counterpart-appendonly: <True|False>
# legs-differing-from-counterpart: <legs>
appendonly: <PASS|FAIL|NOT-REPORTED>
other-legs-unchanged: <yes|no>
verdict: <AS-EXPECTED|UNEXPECTED>
```

`# edited-row`, `# edited-cell` (with the 1-based cell index and whether the
cell is a rule-2 cell), `# old-cell` and `# new-cell` are there so
**ExecCaCounter can re-derive the fixture without my scratch dir**: the recipe
is (freeze, base, row id, cell index, old text, new text), and the receipt
records the resulting tree id so a re-derivation can be compared byte-for-byte.
`# legs-differing-from-counterpart` is the sharpest single line of the pair: it
must be exactly `APPENDONLY`.

## The runner

`.ufo/waves/round-75/run-controls.sh <freeze> [base]` runs the two do-nothing
controls per claim and writes `reports/round-75/telemetry/controls-c.txt` and
`controls-ca.txt`, exactly in round-74's shape: control 1 is `lands == <freeze>`
(the legal ancestor relation, no data landed) and control 2 is
`lands == <base>` (the counter must REFUSE). Base defaults to
`f556d1049fe651d3d63975600b13acd9fb686f15`.

It resolves the counter at `reports/round-75/<name>` first and falls back to
`.ufo/waves/round-75/counters/<name>` (the two places a counter can live, per
the round-74 precedent where the freeze installed a copy under `reports/`),
`cd`s to the lane root so the relative `--root .` is unambiguous, and refuses
loudly if neither counter exists. A third argument `--junk <landing-rev>`
additionally runs the generator and splits its output at the
`===== SECTION C|Ca =====` markers into `junk-c.txt` / `junk-ca.txt`.

**I did not run the controls.** Per the seat spec they are the L1's to run at
freeze. The script is `sh -n` clean and executable.

## Evidence — what I actually ran

The round-75 counters do not exist yet (seats `ExecCCounter` / `ExecCaCounter`
were still writing them while I worked), so I could not grade against them.
I did not leave that untested. I ran two things:

**(1) the generator's own selftest** (helpers only, no counter, no clone):

```
$ python3 -B .ufo/waves/round-75/counters/junk-fixtures.py --selftest
SELFTEST: PASS
```

It covers: cell splitting with an escaped pipe; the three constant-printer
shapes; the correction-row stub and append (including that appending keeps the
existing rows intact); Gate-quote extraction from an admitted row and the
refusal of a refused row; the evidence-window parser; and the counter's NFKC
whitespace fold.

**(2) a mechanical proxy run against the round-74 counter.** The generator's
round-path constants were repointed at round 74 (`reports/round-74/claims.json`,
`reports/round-74/ledger.json`, `corpus/lessons/round-74.md`,
`reports/round-74/evidence`, `reports/round-74/telemetry`,
`reports/round-74/accept-c{a,}.py`), the freeze/base/lands were set to round
74's (`00c408a0…` / `f7104cb…` / `f556d10…`), and every fixture was built,
semantically asserted, and graded. Harness:
`/fast/scratch/hyaku/kotodama-r75/ExecJunkFixtures/proxy_check.py` (deleted with
the scratch dir; the recipe is reproduced below).

```
J1     PASS counter=ACCEPT-C-74: FAIL legs=9/13
J2     PASS counter=ACCEPT-C-74: FAIL legs=12/13
J3     PASS counter=ACCEPT-C-74: FAIL legs=12/13
J4     PASS counter=ACCEPT-CA-74: FAIL legs=9/11
J4b    PASS counter=ACCEPT-CA-74: FAIL legs=9/11
J4c    PASS counter=ACCEPT-CA-74: FAIL legs=9/11
J4m    PASS counter=ACCEPT-CA-74: FAIL legs=9/11
J4f    PASS counter=ACCEPT-CA-74: FAIL legs=10/11
J5     PASS counter=ACCEPT-CA-74: FAIL legs=8/11
J6     PASS counter=ACCEPT-CA-74: FAIL legs=10/11
J7     PASS counter=ACCEPT-CA-74: FAIL legs=10/11
J8     PASS counter=ACCEPT-CA-74: FAIL legs=9/11
J9     PASS counter=ACCEPT-CA-74: FAIL legs=10/11
J10    PASS counter=ACCEPT-CA-74: FAIL legs=10/11
G      PASS counter=ACCEPT-CA-74: FAIL legs=6/11
R      PASS counter=ACCEPT-CA-74: FAIL legs=6/11

PROXY: 16/16 fixtures behaved as designed
```

Each `PASS` means the counter produced a verdict, the verdict was not `PASS`,
and the fixture's own semantic assertion held (the stub entries really are
header-only; the S001 used-by/téaches cells really are the only changed bytes;
the SOURCES delta really is one line; the window digest really recomputes; the
frozen ledger really differs from the pristine one; …).

## Findings

**F1 (HIGH — affects the round-75 Ca counter).** J4's expectation in the seat
list is `LEDGER`, but a ledger edited in the **graded tree** cannot make the
LEDGER leg red. The frozen Ca FROZENCFG leg says the ledger is read from
`git show <freeze>:reports/round-75/ledger.json`, never from the graded tree,
so the mutation lands on FROZENCFG (byte difference) and LEDGER stays green.
Measured, against the round-74 counter:

```
J4   LEG PASS LEDGER … LEG FAIL FROZENCFG      red=('APPENDONLY','FROZENCFG')
J4f  LEG FAIL LEDGER … LEG PASS FROZENCFG      red=(…'LEDGER'…)
```

`J4f` is the fixture that reaches the LEDGER clause: it puts the constant
printers in the fixture's **own freeze commit**, so the counter reads them.
Both are in the generator with their honest expected-leg sets; the round-75
counter should be checked against both, and the frozen do-nothing-control
sentence for Ca should name `J4f` if it wants the allowlist clause exercised
at all.

**F2 (HIGH — a vacuity hole the round-75 EVIDENCE leg must not inherit).** The
round-74 EVIDENCE leg guards its quote check with
`if window is None or not window.strip(): continue`. My first J2 wrote the
window over with ideographic spaces; because `.strip()` treats U+3000 as
whitespace, the window became "empty", the quote check was **skipped**, and the
junk landing graded `ACCEPT-C-74: PASS legs=13/13`. That is a junk landing the
counter accepted — exactly the class these fixtures exist to catch. The
generator now uses U+2588 (a non-whitespace block) and the fixture is red
again. **The round-75 counter must either drop that `continue` or treat a
stored window that is all-whitespace as a failure**, otherwise a landing can
blank every window and pass EVIDENCE.

**F3 (MED — round-74 counter, inherited risk).** `accept-ca.py`'s LOSERS: the
same blank-window hole is reachable through `visible-chars` too — a
`whole-document` file whose window is blanked to the same character count keeps
`len(window) == visible-chars` and is skipped. Same fix as F2.

**F4 (LOW — measurement note).** The Ca counter creates its own clones under
`/tmp` (`clone=/tmp/r74-ca-…`). With the other wave-1 seats running
concurrently, three fixtures transiently reported `NO-VERDICT` (empty stdout)
and then passed on re-run with nothing changed. Anything that reads these
receipts should treat `NO-VERDICT`/`TIMEOUT` as "no verdict", never as "caught"
— the generator now says so explicitly (`TIMEOUT` is its own verdict string and
the receipt's `accepted:` line only reads `no` for a non-`PASS` verdict).

**F5 (LOW — observation about the R1 pair against round 74).** Under the
round-74 counter, **both** G and R are APPENDONLY-red (G's used-by edit is
"corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [30]"), so
`legs-differing-from-counterpart` is empty there. That is the defect R1 fixes,
and it is the red-before half of the pair: against the round-75 counter G must
go green and the line must read exactly `APPENDONLY`. If it does not, the
exemption is not working, and the receipt shows it in one line.

**F6 (LOW).** J1 needs the registry rows for the frozen `row_set` to exist in
the reference tree, J5 needs the `## Corrections — round 75` section, and J2
needs evidence files for the adopted rows. Before the landing these are absent,
so `--lands <freeze>` reports those fixtures as `error: … (no verdict was
produced)` rather than manufacturing a verdict. That is deliberate: a fixture
that cannot be materialized must not report a catch. Run the sweep with
`--lands <landing>` for attributable results, and read the `newly-red` column
to see which legs this round's tree actually moved.

## How to run it

```sh
# at freeze: the do-nothing controls (§ the L1's step)
.ufo/waves/round-75/run-controls.sh <freeze>

# after the landing: the junk sweep, split into the two telemetry receipts
.ufo/waves/round-75/run-controls.sh <freeze> <base> --junk <landing-rev>

# or directly, one fixture at a time
python3 -B .ufo/waves/round-75/counters/junk-fixtures.py \
    --run --freeze <freeze> --base <base> --lands <landing-rev> \
    --out-dir reports/round-75/telemetry --out reports/round-75/telemetry/junk-r75-run.txt
python3 -B .ufo/waves/round-75/counters/junk-fixtures.py --list
python3 -B .ufo/waves/round-75/counters/junk-fixtures.py --only G,R ...
```

Exit status: `0` if the counter refused every junk landing, `2` if any junk
landing was ACCEPTED (the sweep prints `# ACCEPTED JUNK LANDINGS: <names>`), so
the runner's `--junk` step fails loudly when a counter regresses.

Library API (for a counter's own selftest — `importlib.util` by path, since the
file name carries a hyphen):

```python
spec = importlib.util.spec_from_file_location(
    "junk_fixtures", "<lane>/.ufo/waves/round-75/counters/junk-fixtures.py")
jf = importlib.util.module_from_spec(spec); spec.loader.exec_module(jf)
fx = jf.build("J3", freeze=<40hex>, lands=<40hex>, base=<40hex>,
              workroot="/fast/scratch/hyaku/kotodama-r75/ExecJunkFixtures")
try:    res = jf.run_counter(fx.repo, jf._counter_path(fx.repo, jf.C_COUNTER_CANDIDATES),
                             fx.rev, fx.freeze)
finally: jf.cleanup(fx)
```

## Blockers and gaps

- **The round-75 counters do not exist yet.** Grading evidence above is
  mechanical-only (round-74 proxy). The moment `reports/round-75/accept-c.py`
  and `accept-ca.py` exist, re-running
  `--run --freeze <freeze> --base <base> --lands <landing>` is the real test.
- **The freeze commit does not exist yet.** Everything is parameterised on
  `--freeze`; I did not create a commit (only the L1 commits).
- **F1 and F2 should reach `ExecCaCounter` / `ExecCCounter` before they finish.**
  F2 in particular is a counter bug that lets a junk landing pass.
- Tool installs: none. No `pacman`, no network fetches, no new dependencies —
  the generator is stdlib-only by construction.

## Scratch

Everything lived under
`/fast/scratch/hyaku/kotodama-r75/ExecJunkFixtures/` (mirrors, fixture clones,
the proxy harness, the CLI smoke run). It is deleted before this seat yields;
the receipts that matter are (a) the generator and runner above, and (b) the
`r1exempt-*.txt` grammar, which the generator re-emits on demand.
