# ScoutR77Truth — R77 BASEMISMATCH receipts, pristine ledger, and command semantics under R78-M1 (round-79 W1)

Seat: ScoutR77Truth (leaf scout, no dispatch). Lane base `44f76d456c1b326a71ffdb381590af825cbf11be`
(= lane HEAD; `git status --porcelain -- .ufo/waves/round-77/` empty, so every artifact quoted
below is committed at base and worktree-clean). The round-77 base pinned inside the artifacts,
`211f9526800906e0c585d878d265c37e5e090c15`, is an ancestor of today's base
(`git merge-base --is-ancestor` → true). Read-only reproduction was executed today against that
pin (§4). No tool installs; no pacman; no git/jj mutation anywhere; scratch
`/fast/scratch/hyaku/kotodama-r79/ScoutR77Truth/` deleted after this report was written.

## 1. What R78-M1 actually claims (the row, verbatim)

`corpus/lessons/round-78.md:11`:

> | R78-M1 | calibration: the round-77 Ca candidate check accepted structurally valid rows whose recorded base observation did not equal the re-run observation | `.ufo/waves/round-77/w2/MutCaLedger.md:43-84`; `.ufo/waves/round-77/w2/ScoutLogPairs.md:43-70`; `.ufo/waves/round-77/w2/ExecCaPass.md:24-34` | QUALITY criterion 11 requires each claim clause and counting command be checked; round-77 W2 actually re-ran the candidate observation and found the mismatch | Require the frozen ledger to store the observed token from its exact pinned-base command and reject any pair where stated token equals that observed token; the red-before evidence is W2's executed `BASEMISMATCH` failure on the recorded 11-pair probe, not merely its structural `LEDGER-CHECK` pass. This remains a routed lesson, not a round-78 implementation claim. |

All three evidence pointers resolve on committed bytes today:
- `MutCaLedger.md:43` = the mutation table header row, `:84` = the survivor-scope closing line — the
  ledger-grammar attack (7 mutants, 6 killed, `HEAD`-in-revision-position survivor).
- `ScoutLogPairs.md:43` = `## 1. Per-pair results`, `:70` = the `pair_problems` gap sentence — the
  per-pair audit that first recorded the false observations.
- `ExecCaPass.md:24` = verdict part 3 ("That green is not evidence the ledger is valid"), `:34` =
  start of §1 Environment — the executed `BASEMISMATCH`/`REPAIR` leg receipts.

## 2. The pristine ledger (identity verified today)

Path: `.ufo/waves/round-77/w1/stage/ExecAdaptCa/probe-real-ledger.json`
(`"status": "SCRATCH PROBE — not a lane file"`, `round: 77`, `claim: "Ca"`,
`base: 211f9526800906e0c585d878d265c37e5e090c15`, 11 pairs D01–D11).

```
sha256sum probe-real-ledger.json accept-ca.py      # recomputed 2026-10-30 from lane bytes
b7509d2b0980f8c5824c417a8359c8f7107d3de6236cf486ac058947915d0704  probe-real-ledger.json
ac2bc93d02932464f9ee43222ffe1d06dd5bf1a0e68fd38bd94e10a991489b2e  accept-ca.py
```

Both equal the hashes the W1/W2 receipts recorded (`MutCaLedger.md` §0/§3; `ExecCaPass.md` §0;
`w2/stage/ExecCaPass/sha256s.txt`; the W2 stage copy `w2/stage/ExecCaPass/ledger.json` hashes
identical). Detector: the same `accept-ca.py` staged beside the ledger (never modified by W2).

Pair inventory (from the JSON itself, all 11 dumped):
- D01–D10 `disposition=ANNOTATE`, `stated_at` LOG.md:3/447/826/1234/1655/2036/2611/3078/3457/3787,
  byte-identical `observe_cmd` argv `["git","-C",".","grep","-c","-E","^#","211f9526…90c15","--","LOG.md"]`,
  `parse ":([0-9]+)$"`, `stated_parse "([0-9]+)"`, `observed_at_base "1"`, `expected_after "1"`.
- D11 `disposition=REPAIR`, `stated_at corpus/README.md:755`, stated_text
  `Total knowledge entries: 243.`, `observe_cmd ["grep","-o","-E","Total knowledge entries: [0-9]+","corpus/README.md"]`,
  `parse "entries: ([0-9]+)"`, `stated_parse "Total knowledge entries: ([0-9]+)\."`,
  `observed_at_base` **absent (null)**, `expected_after "244"`.

## 3. The exact executed BASEMISMATCH receipts (what "executed" means here)

Two receipts on committed bytes carry the executed failure:

**(a) `reports`-grade leg run — `w2/stage/ExecCaPass/graded-legs.txt` (verbatim, whole file):**

```
LEG FAIL BASEMISMATCH
     red=10 min=10 ids=['D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09', 'D10'] green-at-base=['D11'] unobserved/miss=["D01:recorded-observed-at-base='1'!='149'", … (all ten) … "D10:recorded-observed-at-base='1'!='149'"]
BASEMISMATCH_PASSED=False
LEG FAIL REPAIR
     green=[] red=["D11(statement='253' truth='243')"]
REPAIR_PASSED=False
```

Produced by the preserved driver `w2/stage/ExecCaPass/graded-legs.py`, which imports the staged
counter and calls its own `evaluate_pairs`/`leg_basemismatch`/`leg_repair` with
`base = lands = <lane>@211f9526` — i.e. the counter's graded-leg code paths, executed, not
narrated. Companion receipts: `token-evidence.txt` (per-pair tokens via the counter's own
`stated_token`/`observed_token`/`pair_problems`; final line
`RED_AT_BASE 10/11 ; RECORDED_MATCHES_OBSERVED 0/11`) and `verify-base.txt` (raw-git
re-derivation, `rc=0` for all 11 argv).

**(b) Independent audit — `.ufo/waves/round-77/w2/ScoutLogPairs.md` (per-pair table, lines 43–70).**
Key rows: every D01–D10 `recorded observed_at_base "1"` vs actual observed token `"149"`
(`recorded = actual?` → **NO** ×10); D11 `stated 243 / observed 243`, **NO — green at base**.

The structural counter-state that made this possible — `--ledger-check` (grammar-only) green on
the same bytes: `w1/stage/ExecAdaptCa/ledger-check-real-base.txt` /
`ledger-check-real-base-laneC.txt` → `LEDGER-CHECK-77: PASS pairs=11`, exit 0 (also re-run by W2
in three invocation forms, `ExecCaPass.md` §3 G1–G3).

### Counter semantics the receipts rest on (staged `accept-ca.py`, sha `ac2bc93d…`)

`pair_problems()` — the recorded observation is checked for **type only**, never against execution
(`:1712-1714`):

```python
rec = pair.get("observed_at_base")
if rec is not None and not isinstance(rec, str):
    problems.append("%s: observed_at_base is not a string" % tag)
```

`leg_basemismatch()` — the graded leg that catches it (`:1849-1880`): red/green by
`norm(tok) != norm(obs)` (stated vs live observed), then separately

```python
rec = pair.get("observed_at_base")
if isinstance(rec, str):
    lead = (rec.split() or [""])[0]
    if norm(lead) != norm(obs):
        misses.append("%s:recorded-observed-at-base=%r!=%r" % (pid, scrub(rec[:40], cfg), scrub(obs[:40], cfg)))
...
passed = (not unobservable) and (not green) and (not misses) and len(red) >= min_pairs
```

So `red=10 ≥ min=10` is necessary but not sufficient: the ten recorded-vs-live misses and the one
green-at-base pair each fail the leg independently. This is exactly why R78-M1's fix says the
frozen ledger must "store the observed token from its exact pinned-base command" — at
`--ledger-check` time nothing enforces that, and D11 shows the second half ("reject any pair where
stated token equals that observed token") is likewise unenforced pre-freeze.

## 4. Read-only reproduction against the pinned base (executed today, 2026-10-30)

Scratch copies of the pristine bytes (`sha256` equal to §2), probes run from
`/fast/scratch/hyaku/kotodama-r79/ScoutR77Truth/`; lane untouched (post-run hashes of the two
stage files unchanged; no lane write anywhere):

```
--- PROBE A: ledger observe_cmd argv (D01-D10), retarget `-C .`→`-C <lane>`, rev pinned
$ git -C <lane> grep -c -E '^#' 211f9526800906e0c585d878d265c37e5e090c15 -- LOG.md
211f9526800906e0c585d878d265c37e5e090c15:LOG.md:149        exit=0
  → parse ":([0-9]+)$" → "149" ≠ recorded "1" ≠ any stated token except D05's prose "1"

--- PROBE B: D11 observation on committed bytes at the pin (git show | grep, no worktree read)
$ git -C <lane> show 211f9526…90c15:corpus/README.md | grep -o -E 'Total knowledge entries: [0-9]+'
Total knowledge entries: 243 … 247 … 249 … 252 … 253        exit=0
$ … | grep -n 'Total knowledge entries'
755:…243.  798:…247.  819:…249.  830:…252.  834:…253.
  → re.search first match = 243 == stated 243 (green at base); true footer 253 at :834

--- PROBE C: counter --ledger-check on pristine bytes
$ python3 -B accept-ca.py --ledger-check probe-real-ledger.json --root <lane> \
    --base 211f9526…90c15 --work <scratch>/work-lc
LEDGER-CHECK-77: PASS pairs=11                              exit=0

--- PROBE D: graded legs re-run via preserved graded-legs.py (scratch copy + stage ledger.json,
    whose sha256 equals the W1 probe's)
LEG FAIL BASEMISMATCH … red=10 … green-at-base=['D11'] unobserved/miss=[D01..D10
     "recorded-observed-at-base='1'!='149'"] … BASEMISMATCH_PASSED=False
LEG FAIL REPAIR … red=["D11(statement='253' truth='243')"]  REPAIR_PASSED=False
```

Probes C and D reproduce the recorded receipts **byte-identically** (D output = §3(a) verbatim).
Tools: Python 3.14.8, git 2.56.0 (pre-existing; no installs).

## 5. The distinction R78-M1 turns on: recorded-observation mismatch vs stated==truth vacuity

**Class 1 — recorded `observed_at_base` ≠ executed observation (D01–D10; the R78-M1 headline).**
The ledger *asserts* a base observation that was never the command's output: every D01–D10 records
`"observed_at_base": "1"` while the pair's own pinned-base argv returns `149`
(`w2/stage/ExecCaPass/token-evidence.txt`: `RECORDED_MATCHES_OBSERVED 0/11`; graded receipt:
`recorded-observed-at-base='1'!='149'` ×10). The structural check accepts it because it grades
only `isinstance(rec, str)`; the graded leg rejects it via the `misses` clause. The *semantic*
redness of these pairs (stated ≠ observed, e.g. D01 `2026` vs `149`) is nonetheless genuine and
independently re-derived today (PROBE A) — ScoutLogPairs §4 judges them "salvageable by wiring:
replace each `observed_at_base` with the real observed token `"149"`". D05 is the provenance
smoking gun: its stated token (scraped from prose) is `"1"`, cosmetically equal to the fabricated
recorded `"1"` — consistent with a hand-set/greppless value, not an executed observation.

**Class 2 — stated==truth vacuity (D11; the fix's second clause).**
D11's `observe_cmd` re-reads the very line the pair states: `grep -o` over
`corpus/README.md` emits five totals, `parse "entries: ([0-9]+)"` takes `re.search`'s **first**
match `243`, which equals the stated token `243` from `:755` — the pair cannot register a
mismatch under any base (circular self-observation; green-at-base → kill rule
"any ledger pair not red at base" fires). Its `observed_at_base` is absent (null) — structurally
tolerated, semantically "the author never observed this pair" (ScoutLogPairs §2). The real footer
truth at the pin is `:834 → 253`, so even the stated line is a stale per-section snapshot —
`LEG FAIL REPAIR … D11(statement='253' truth='243')` shows the pair's two parses can never agree.
Structural-vacuity cousins that `--ledger-check` also passes (ExecCaPass §4 admitted-green
controls, all `LEDGER-CHECK-77: PASS pairs=11`): V01 (11 clones of one pair), V02 (every
`observed_at_base="999"` fabricated), V03 (11 identical REPAIR clones) — receipt files under
`w2/stage/ExecCaPass/controls/`.

In short: **Class 1 = a recorded observation that lies about execution (real mismatch, false
record); Class 2 = an observation that cannot disagree with the statement (vacuous pair, no
mismatch possible).** R78-M1's one fix sentence targets both halves; the executed
`BASEMISMATCH` failure on the 11-pair probe (§3a) is the red-before evidence for both, while
`LEDGER-CHECK-77: PASS pairs=11` alone would have certified neither.

## 6. Three representative pairs (concrete, quoted)

| pair | fields (from pristine ledger JSON) | executed truth at pin `211f9526…` | receipt quote | pointer |
|---|---|---|---|---|
| **D01** (Class 1) | `ANNOTATE`, `stated_at LOG.md:3`, stated `## 2026-10-17 — mint (round 0)`, `stated_parse ([0-9]+)`→`2026`, argv `git -C . grep -c -E '^#' 211f9526… -- LOG.md`, `parse :([0-9]+)$`, `observed_at_base "1"` | argv → `211f9526…:LOG.md:149` (exit 0; re-run today, PROBE A) | `D01:recorded-observed-at-base='1'!='149'` (graded-legs.txt); `D01 … stated='2026' observed='149' recorded_ob='1' … pair_problems=0` (token-evidence.txt) | `w2/stage/ExecCaPass/graded-legs.txt`; `token-evidence.txt`; `ScoutLogPairs.md:43-52` |
| **D05** (Class 1, provenance) | `ANNOTATE`, `stated_at LOG.md:1655`, stated prose contains `…not applicable…`, `stated_parse ([0-9]+)`→`1`, same argv, `observed_at_base "1"`, `expected_after "1"` | argv → `…:LOG.md:149` (PROBE A) | `D05 ANNOTATE stated='1' observed='149' recorded_ob='1' expected='1' red_at_base=True pair_problems=0`; `recorded-observed-at-base='1'!='149'` — stated token coincides with the fabricated record, betraying a never-executed value | `w2/stage/ExecCaPass/token-evidence.txt:5`; `ScoutLogPairs.md` §2 ("expected_after:'1' … same off-by-misreading") |
| **D11** (Class 2) | `REPAIR`, `stated_at corpus/README.md:755`, stated `Total knowledge entries: 243.`, argv `grep -o -E 'Total knowledge entries: [0-9]+' corpus/README.md`, `parse entries: ([0-9]+)`, `observed_at_base` null, `expected_after "244"` | five matches 243/247/249/252/253 on committed bytes at pin (PROBE B); first match 243 == stated 243; footer truth `:834 → 253` | `green-at-base=['D11']` (graded-legs.txt); `LEG FAIL REPAIR … red=["D11(statement='253' truth='243')"]`; `D11 REPAIR stated='243' observed='243' … red_at_base=False` | `w2/stage/ExecCaPass/graded-legs.txt`; `token-evidence.txt:11`; `ScoutLogPairs.md:54-70` |

## 7. Adjacent finding (in-scope, one line)

MutCaLedger's mutant e1 (D07 `rederive` rev `211f9526…` → `HEAD`) **survived**
(`LEDGER-CHECK-77: PASS pairs=11`): the enforced grammar accepts `HEAD`/`HEAD^`/`HEAD~1`/`@` in
revision position (`REV_NAMES`, staged `accept-ca.py:1070`), so the draft's "immutable 40-hex"
invariant is carried by `materialize()`'s detached-at-base assert, not by the pair grammar —
harmless at ledger-check time, a coverage gap in the contract sentence (MutCaLedger.md §2, lines
43-84 of the R78-M1 pointer).

## 8. Scope / evidence discipline

- Observed (this seat, today): §2 hashes, §4 probe outputs, §3 file contents, pointer-range
  resolutions (§1), clean `git status`/`git diff` over `.ufo/waves/round-77/`, base ancestry.
- Read from receipts (not re-executed): W2's original scratch paths/deletion, the 39-mutant
  control matrix details, W1's `ExecAdaptCa.md` claims.
- Not run (stated as unrun): any lands-domain leg (no lands/freeze tree exists in round-79 W1);
  nothing in this report modifies lane, fleet, or any sibling receipt.
- R77-vs-R78-M1 chain: R78-M1's "recorded base observation did not equal the re-run observation"
  is evidenced precisely by §3(a) `recorded-observed-at-base='1'!='149'` ×10 plus D11's
  `green-at-base` — both re-derived today on pinned, committed, hash-verified bytes.
