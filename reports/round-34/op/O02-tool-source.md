- Seat: O02 | executor | claim O | date 2026-10-19 | baseline da68a6d

# O02 — `tools/harness/receipt_guard_adoption.py`, full tool source (claim O)

## Mission (verbatim from `reports/round-34/targets.json`)

> Write the FULL tool source as a fenced python block in your fragment (O01
> describes; you ship the bytes) — the integrator lands it; include `--selftest`
> and `--json` modes.

This fragment ships the complete stdlib-only instrument that claim O requires:
a receipt-write / guard-adoption census over every `reports/round-*/run-validation.py`,
with `--json`, `--sweep-repo`, `--out` and `--selftest` modes, the F-C13-1 routing
protocol per class, and the declared-hazard block that classifies the four runners
named in the F-C13-1 incident record.

## What the integrator lands

| item | value |
|---|---|
| landing path | `tools/harness/receipt_guard_adoption.py` (shared path — this seat writes only its own `out`; the integrator lands the bytes below) |
| draft bytes | `.scratch/o02/receipt_guard_adoption.py`, 1309 lines, sha256 `5858abcd0261e8176ebb285db6d80a7c36185d9a12895b4b43b75710db036544` |
| extraction | the fenced python block under "## Tool source" is the complete file; the block ends at the first line that is exactly three backticks after it. Round-trip check used by this seat (reproduces the draft byte-for-byte, see "fence round-trip" below) |
| suggested durable census | `python3 -B tools/harness/receipt_guard_adoption.py --json --out reports/round-34/op/receipt-guard-adoption-inventory.json` (exit 0) |
| imports | `argparse`, `ast`, `datetime`, `hashlib`, `json`, `os`, `re`, `sys`, `tempfile`, `pathlib` — stdlib only |
| path assumptions | `ROOT = Path(__file__).resolve().parents[2]`, the same depth convention as `tools/harness/receipt_guard.py:203` (its selftest uses the identical `parents[2]` root); the tool is cwd-independent (verified from `/tmp` with `--root`) |
| runner execution | the tool never executes a runner, never writes a filed receipt, and refuses `--out` destinations that are absolute, escaping, or named `validation.json` |

## Observed evidence at write time (2026-10-19, HEAD `da68a6d`, filed bytes untouched)

| command (against the draft bytes) | observed |
|---|---|
| `python3 -B .scratch/o02/receipt_guard_adoption.py --selftest` | exit 0, controls 38/38 passed, fixture_count 11, live runners 28 |
| `python3 -B .scratch/o02/receipt_guard_adoption.py --json` | exit 0, `runner_count` 28, `class_counts` {"guarded-refresh": 17, "unguarded-in-place": 11}, `hazard_count` 11, `census_complete` true, `gaps` [] |
| `python3 -B .scratch/o02/receipt_guard_adoption.py --sweep-repo --json` | exit 0, files scanned 244, receipt writers 27, non-runner writers 0, parse gaps 0 |
| coverage | 28/28 filed runners (28 is the filed census at `da68a6d`; `reports/round-34/run-validation.py` does not exist yet — see `reports/round-34/targets.json` shared_rules) |
| guard digest | `tools/harness/receipt_guard.py` sha256 `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1` |
| census JSON digest | `.scratch/o02/inventory.json` sha256 `ceeb8d0413e2832a8555e5a9467f016208a477fc708c7f3834bcc429a6bebf04` |
| sweep JSON digest | `.scratch/o02/sweep.json` sha256 `dcd172affb61a844dfab26d8763ca03127249252f374c41ad806175303ba6eb2` |
| selftest receipt digest | `.scratch/o02/selftest.out` sha256 `81e129ca26dcf805a3400e68ad593638ba10d5ef50ba1d82b7511032cc96c8ac` |
| landing simulation | isolated `git archive HEAD | tar -x -C .scratch/o02/simlane`, tool extracted from this fragment to `simlane/tools/harness/receipt_guard_adoption.py` (sha256 re-verified `5858abcd0261e8176ebb285db6d80a7c36185d9a12895b4b43b75710db036544`): `--selftest` exit 0 (38/38), `--json` exit 0 (runner_count 28, `class_counts` {"guarded-refresh": 17, "unguarded-in-place": 11}, `gaps` []) — the real landing depth works; the lane tree itself is never written |

Scratch is not durable evidence. The integrator re-runs the two counting commands
above; the digests here pin exactly which bytes produced the numbers in this
fragment, so a re-run that differs is detectable.

## Observed inventory — all 28 filed runners

Classes: `guarded-refresh` = an own-receipt write dominated by a guard call
(protocol: in-tree re-run refused by the guard once the receipt is committed;
`REFRESH_RECEIPTS=1` refresh belongs in an isolated clone);
`unguarded-in-place` = own-receipt write with no dominating guard call
(protocol: isolated-copy-only, F-C13-1 prevention);
`guard-referenced-only` = guard loaded/referenced but never called;
`no-receipt-write` = no in-place own-receipt write found;
`could-not-evaluate` = named census gap, never a green.

| runner | class | receipt write (line) | guard entry calls (line) | round |
|---|---|---|---|---|
| `reports/round-5/run-validation.py` | unguarded-in-place | :194 | — | 5 |
| `reports/round-6/run-validation.py` | unguarded-in-place | :336 | — | 6 |
| `reports/round-7/run-validation.py` | unguarded-in-place | :1171 | — | 7 |
| `reports/round-8/run-validation.py` | unguarded-in-place | :1486 | — | 8 |
| `reports/round-9/run-validation.py` | unguarded-in-place | :1910 | — | 9 |
| `reports/round-10/run-validation.py` | unguarded-in-place | :1054 | — | 10 |
| `reports/round-11/run-validation.py` | unguarded-in-place | :1740 | — | 11 |
| `reports/round-12/run-validation.py` | unguarded-in-place | :1071 | — | 12 |
| `reports/round-14/run-validation.py` | guarded-refresh | :717 | :420 | 14 |
| `reports/round-15/run-validation.py` | guarded-refresh | :1346 | :1044 | 15 |
| `reports/round-16/run-validation.py` | guarded-refresh | :1265 | :1005 | 16 |
| `reports/round-17/run-validation.py` | guarded-refresh | :1431 | :1124 | 17 |
| `reports/round-18/run-validation.py` | guarded-refresh | :1851 | :1518 | 18 |
| `reports/round-19/run-validation.py` | unguarded-in-place | :21 | — | 19 |
| `reports/round-20/run-validation.py` | guarded-refresh | :1485 | :1285 | 20 |
| `reports/round-21/run-validation.py` | unguarded-in-place | :1115 | — | 21 |
| `reports/round-22/run-validation.py` | guarded-refresh | :922 | :829,:911,:921 | 22 |
| `reports/round-23/run-validation.py` | guarded-refresh | :1097 | :1066,:1094 | 23 |
| `reports/round-24/run-validation.py` | guarded-refresh | :1184 | :1153,:1181 | 24 |
| `reports/round-25/run-validation.py` | guarded-refresh | :1145 | :1110,:1142 | 25 |
| `reports/round-26/run-validation.py` | guarded-refresh | :1909 | :1857,:1906 | 26 |
| `reports/round-27/run-validation.py` | guarded-refresh | :1907 | :1855,:1904 | 27 |
| `reports/round-28/run-validation.py` | guarded-refresh | :2098 | :1998,:2095 | 28 |
| `reports/round-29/run-validation.py` | unguarded-in-place | :922 | — | 29 |
| `reports/round-30/run-validation.py` | guarded-refresh | :923 | :885,:903,:922 | 30 |
| `reports/round-31/run-validation.py` | guarded-refresh | :1159 | :1120,:1139,:1158 | 31 |
| `reports/round-32/run-validation.py` | guarded-refresh | :1143 | :1104,:1123,:1142 | 32 |
| `reports/round-33/run-validation.py` | guarded-refresh | :1471 | :1443,:1459,:1470 | 33 |

`class_counts` from the tool: {"guarded-refresh": 17, "unguarded-in-place": 11}. The 17
`guarded-refresh` rows are r14–r18, r20, r22–r28, r30–r33; the 11
`unguarded-in-place` rows are r5–r12, r19, r21, r29.

## The four F-C13-1 declared hazards, classified

Declared set transcribed from `LOG.md:3556-3560` (filed bytes, never edited by
this tool or this seat); the census records agreement per row.

| runner | declared by | declared class | observed class | agrees |
|---|---|---|---|---|
| `reports/round-5/run-validation.py` | LOG.md:3556-3558 `:194` | unguarded-in-place | unguarded-in-place | yes |
| `reports/round-6/run-validation.py` | LOG.md:3556-3558 `:336` | unguarded-in-place | unguarded-in-place | yes |
| `reports/round-7/run-validation.py` | LOG.md:3556-3558 `:1171` | unguarded-in-place | unguarded-in-place | yes |
| `reports/round-26/run-validation.py` | LOG.md:3559-3560 `:90, :1909` | unguarded-in-place | guarded-refresh | **no** |

### Finding RGA-1 (r26) — declared hazard not reproduced by the bytes

`LOG.md:3559-3560` states that "the r26 runner carries the same hazard (`:90`,
`:1909`)". The live bytes at `da68a6d` show the r26 write at
`reports/round-26/run-validation.py:1909` dominated by a guard call at `:1906`
inside a `try:` at `:1905` whose `SystemExit` handler returns (fails closed), with
the guard proxy defined at `:1855-1857`. The census therefore reads r26 as
`guarded-refresh`. Observed site row:

```json
[{"guard_provider": {"call_lines": [1906], "entries": ["guard_receipt"], "kind": "try-guard", "line": 1905}, "guarded": true, "kind": "write_text", "line": 1909, "resolution": "wrapper:safe_path", "resolved": "reports/round-26/validation.json", "src": "safe_path(OUTPUT).write_text(rendered, encoding='utf-8')", "target": "safe_path(OUTPUT)"}]
```

Neither reading is a fabrication: the LOG sentence is a *characterization* of
r26's receipt-write shape, while the classification is a byte fact. This seat
files the contradiction as a new row (RGA-1) instead of editing the LOG; the
integrator/reviewers (R08 owns the F-C13-1 class check) decide whether the LOG
needs a new supersession-style note naming RGA-1. `to-verify` at integration:
whether F-C13-1's r26 clause intended "writes its own receipt in place" as a
class statement (true for all 28 runners) rather than "is unguarded" (not
reproduced).

Three sibling seats reach the same conclusion independently, which is why this
row should not be read as one seat's parse artefact: `O04-predicted-inventory.md`
`known_hazards` records round 26 as `measured_class: guarded-in-place-write`,
`agrees: false`; `.scratch/o08-traps/EXPECTATIONS.json` control `R-adopted-r26`
requires `class: adopted` with `guard_call: 1906`, `write: 1909`; and
`O03-selftest.md` §2 expects r26 `guarded`.

### Finding RGA-2 — the unguarded set is eleven runners, not three

Beyond r5/r6/r7, eight filed runners write their own receipt without a dominating
guard call: r8 (`:1486`), r9 (`:1910`), r10 (`:1054`), r11 (`:1740`), r12
(`:1071`), r19 (`:21`, inside a subprocess script string), r21 (`:1115`; its only
guard-adjacent reference is `REFRESH_RECEIPTS=1`, which its isolated-clone code
sets for *other* runners), r29 (`:922`). Ten of the eleven unguarded runners
(r5–r12, r19, r29) contain no reference to the receipt guard at all; r21 is the
eleventh and the only one whose file mentions the refresh flag. r29 is the
notable row because guard adoption began at r14 and r29 still writes its receipt
with no guard call — a runner filed after the guard existed, still outside its
protection. Claim O's threshold asks that "the four known hazards" be classified;
this census classifies all eleven.

Full findings JSON:

```json
[
  {
    "detail": "F-C13-1 (LOG.md:3559-3560) names :90, :1909 as carrying the same unguarded in-place hazard; the live bytes classify as guarded-refresh",
    "evidence": [
      "reports/round-26/run-validation.py:1909",
      "reports/round-26/run-validation.py:1857 (guard call)",
      "reports/round-26/run-validation.py:1906 (guard call)"
    ],
    "id": "RGA-1-round-26",
    "kind": "declared-hazard-mismatch",
    "owner": "integrator (round 34) — filed LOG.md bytes are not edited; this row is the new-record correction",
    "runner": "reports/round-26/run-validation.py"
  },
  {
    "detail": "8 runner(s) write their own receipt without a dominating guard call and are not in the F-C13-1 declared set",
    "evidence": [
      "reports/round-8/run-validation.py",
      "reports/round-9/run-validation.py",
      "reports/round-10/run-validation.py",
      "reports/round-11/run-validation.py",
      "reports/round-12/run-validation.py",
      "reports/round-19/run-validation.py",
      "reports/round-21/run-validation.py",
      "reports/round-29/run-validation.py"
    ],
    "id": "RGA-2",
    "kind": "undeclared-unguarded-writer",
    "owner": "integrator (round 34) — routing row per runner below",
    "runner": null
  }
]
```

### Repo sweep (`--sweep-repo`) — no non-runner writes a filed receipt

244 `.py` files under `reports/` and `tools/` (skipping `.git`, `.scratch`,
`__pycache__`) scan with zero parse gaps; 27 of them have a resolved write to
some `reports/round-<N>/validation.json`, and all 27 are runners (the 28th,
r19, writes only through its embedded script string and is covered by the
census). So the F-C13-1 routing surface is exactly the runner set: no tool,
sweep audit or auxiliary script in the tree writes a filed receipt.

## Design decisions a reviewer should attack

- **Constant-chain resolution, not literal matching.** The receipt target is
  resolved through `ROUND_DIR`/`OUTPUT`/`OUTPUT_REL`/`HERE`/`ROOT` assignment
  chains, `safe_path(...)`/`Path(...)`/`str(...)` wrappers, `f-strings`,
  `parents[N]` and `__file__`; a write counts only when the resolved path equals
  that runner's own `reports/round-<N>/validation.json`. The write lines of the
  alias form name no path at all (`r8:1486` `output.write_text(...)`,
  `r12:1071` `out.write_text(...)`, `r26:1909`/`r32:1143`
  `safe_path(OUTPUT).write_text(...)`), so a detector that matched the literal
  `validation.json` inside the write expression would read those runners as
  `no-receipt-write` — a false green this tool must not produce.
- **Dominance, not proximity.** A guard call is a provider only when it is an
  earlier statement in the same block as the write, when it is a `try:` whose
  body is guard calls and whose handlers all terminate, or when it is a call to
  a local proxy/preflight function that reaches a guard entry point. Calls
  nested in an `if` are recorded as `flag-gated guard calls (do not dominate)`.
  A guard imported/loaded but never called cannot green a row: it lands in
  `guard-referenced-only`.
- **Embedded script strings are re-parsed.** A string literal that mentions
  `validation.json` and parses as Python is analyzed with the same write-site
  rule at an offset line, which is how r19 (`:21`, kind
  `embedded:write_text`) is caught while its `json.load(open(...))` read at
  `:19` is not.
- **Gaps are labelled, never laundered.** An unparsable or unreadable runner is
  `could-not-evaluate` with a named reason and makes the census exit 1; a hazard
  row does not change the exit code (hazards are the finding, not a failure).
  Unresolved write targets whose text mentions receipt/output/validation make a
  row `could-not-evaluate` rather than `no-receipt-write`.
- **Unknown scope, stated.** Static analysis cannot see runtime aliasing,
  helper-mediated writes, or `json.dump` to a handle obtained elsewhere; the
  recognized idioms are listed in the tool's `limits` and in its docstring.

## Selftest controls (38/38 green at write time)

Fixtures are synthetic runners under a disposable `.scratch` tree; live controls
re-read filed bytes read-only.

| control | result |
|---|---|
| `fixture-round-41-guarded-refresh` | pass |
| `fixture-round-42-guarded-refresh` | pass |
| `fixture-round-43-guarded-refresh` | pass |
| `fixture-round-44-unguarded-in-place` | pass |
| `fixture-round-45-guard-referenced-only` | pass |
| `fixture-round-46-unguarded-in-place` | pass |
| `fixture-round-47-guarded-refresh` | pass |
| `fixture-round-48-unguarded-in-place` | pass |
| `fixture-round-49-no-receipt-write` | pass |
| `fixture-round-50-could-not-evaluate` | pass |
| `fixture-round-51-unguarded-in-place` | pass |
| `fixture-census-covers-every-runner` | pass |
| `fixture-non-runner-writer-absent` | pass |
| `fixture-guarded-runners-not-flagged` | pass |
| `fixture-foreign-writes-not-flagged` | pass |
| `fixture-flag-gated-guard-not-adopted` | pass |
| `fixture-syntax-error-is-a-gap` | pass |
| `fixture-embedded-write-line` | pass |
| `fixture-deterministic` | pass |
| `live-round-5-unguarded-in-place` | pass |
| `live-round-6-unguarded-in-place` | pass |
| `live-round-7-unguarded-in-place` | pass |
| `live-round-8-unguarded-in-place` | pass |
| `live-round-9-unguarded-in-place` | pass |
| `live-round-10-unguarded-in-place` | pass |
| `live-round-11-unguarded-in-place` | pass |
| `live-round-12-unguarded-in-place` | pass |
| `live-round-19-unguarded-in-place` | pass |
| `live-round-21-unguarded-in-place` | pass |
| `live-round-29-unguarded-in-place` | pass |
| `live-round-32-guarded-refresh` | pass |
| `live-round-33-guarded-refresh` | pass |
| `live-r26-guard-call-precedes-write` | pass |
| `live-r19-embedded-receipt-write` | pass |
| `live-runner-census-floor` | pass |
| `live-declared-hazard-four-classified` | pass |
| `live-findings-recorded` | pass |
| `live-guard-digest` | pass |

The claim's required negatives are covered by
`fixture-guarded-runners-not-flagged` (no false hazard flag on any guarded
fixture), `fixture-foreign-writes-not-flagged` (`reports/round-49` writes a
scratch fixture and round-41's receipt and is still `no-receipt-write`), and
`fixture-non-runner-writer-absent` (a non-runner `.py` writing
`reports/round-41/validation.json` produces no census row). `fixture-flag-gated-guard-not-adopted`,
`fixture-embedded-write-line`, `fixture-syntax-error-is-a-gap`,
`fixture-deterministic`, `live-r19-embedded-receipt-write` and
`live-r26-guard-call-precedes-write` cover the adversarial shapes.

## Independent method check (this seat, different technique)

A regex/line-scan implementation (`.scratch/o02/verify_independent.py`, no AST)
resolved each runner's receipt path from its constant lines and listed write-verb
lines touching it. Result: **27/28 rows identical** to the tool; the single
mismatch is the independent scan over-flagging r21 `:472` (it writes a clone copy
of the round-18 runner inside `.scratch`) and `:845` (`claims_path`), because its
alias transitivity is name-based; the tool's AST resolution keeps only `:1115`.
Tail of that diff:

```
reports/round-8/run-validation.py            independent=[1486]             tool=[1486]            OK
reports/round-9/run-validation.py            independent=[1910]             tool=[1910]            OK

rows=28 mismatches=1
```

## Cross-seat reconciliation (siblings landed after this seat started)

Timing matters for how the verifier fragments should be read: O08 filed at 04:13
and O07 at 04:20, while these bytes landed at 04:24. O07 says so in its own
words — "the tool that can be run today is not O02's (`op/O02-tool-source.md`
never landed; no `--selftest`/`--json` exists anywhere — §3.5)" — so O07 and O08
verified **O01's scratch core**, not this tool. This seat closed that gap by
running the draft tool against the siblings' durable fixtures. Three checks:

### 1. O04's predicted inventory — the parity leg, 28/28

The JSON block of `reports/round-34/op/O04-predicted-inventory.md` was parsed and
compared per runner against this tool's `--json` output: receipt-write anchors
(including r19's `embedded:17 (file line 21)`) and the `guard.adopted` boolean.
Result: **0 mismatches on 28/28 rows**; predicted counts
`{"runners": 28, "guarded_in_place": 17, "unguarded_in_place": 11}` equal this
tool's class counts under the label mapping O04 explicitly permits ("label
strings may be renamed by O01/O02"): `guarded-refresh` ≡
`guarded-in-place-write`, `unguarded-in-place` ≡ `unguarded-in-place-write`,
`no-receipt-write` ≡ `no-receipt-write`. O04's independent census also carries
the r26 disagreement as `agrees: false` (see Finding RGA-1).

### 2. O08's trap tree — every expectation satisfied

Run: `python3 -B <draft> --json --root .scratch/o08-traps/tree` (durable trap
tree from `EXPECTATIONS.json`; no filed byte involved).

| id | fixture | O08 expected | this tool | satisfied |
|---|---|---|---|---|
| T1 | `reports/round-901` | `referenced-not-called` / `unguarded-write` | `guard-referenced-only` (write `:59`) | yes — no forbidden green |
| T2 | `reports/round-902` | `conditional-guard`, default path unguarded | `unguarded-in-place` (write `:63`; reasons name the flag-gated calls `:61, :28`) | yes |
| T3 | `reports/round-903` | `unguarded-write` via `os.replace` | `guard-referenced-only` (write `:57`, the `os.replace` destination) | yes |
| C+ | `reports/round-904` | `adopted`, forbidden hazard flag | `guarded-refresh`, `hazard: false` (write `:56`; guard calls `:30, :49, :55`) | yes |
| C− | `tools/cache-export.py` | out of inventory | absent from the census (4 runner rows only) | yes |
| R-unguarded | `reports/round-5` | `unguarded-write`, write `:194` | `unguarded-in-place`, `:194` | yes |
| R-adopted-r26 | `reports/round-26` | `adopted`, guard `:1906`, write `:1909` | `guarded-refresh`, provider `try-guard` call `:1906` | yes |
| R-adopted-r32 | `reports/round-32` | `adopted`, guard `:1123`,`:1142`, write `:1143` | `guarded-refresh`, guarded `:1143` | yes |
| R-embedded-write | `reports/round-19` | `unguarded-write`, embedded program `:5` | `unguarded-in-place`, `embedded:write_text` at `:21` | yes |

O07 reported that the core it tested answers **7 of O03's 12 fixtures correctly,
with three false greens on a real hazard shape** (O07-D5…D7). Against O08's
traps, the flag-gated and referenced-not-called shapes — the ones a mention/
import/def-presence heuristic greens — are the two this tool reports as hazards
with named evidence, and the canonical adopted control is not flagged.

### 3. O03's fixture corpus — 11/11 semantically correct plus the out-of-scope control

The fixture generator `.scratch/o03-fixtures.py` was executed with its working
directory moved into a private copy (`.scratch/o02/o03fixtmp`), so the sibling's
own staging tree was not touched; the tool then ran with
`--root <private>/.scratch/o03-fixtures/tree`.

| id | fixture | O03 expected class | this tool | reading |
|---|---|---|---|---|
| F01 | round-91 | `guarded` | `guarded-refresh` (write `:13`) | match |
| F02 | round-92 | `guarded` | `guarded-refresh` (write `:9`) | match |
| F03 | round-93 | `guard-defined-not-called` | `unguarded-in-place` (write `:9`) | match as hazard: guard calls exist only inside the definition, no provider dominates |
| F04 | round-94 | `guard-after-write` | `unguarded-in-place` (write `:10`) | match: only backward dominance counts |
| F05 | round-95 | `unguarded` | `unguarded-in-place` (write `:7`) | match |
| F06 | round-96 | `unguarded` | `unguarded-in-place` (write `:12`) | match |
| F07 | round-97 | `unguarded` | `unguarded-in-place` (write `:9`) | match (receiver-alias form) |
| F08 | round-98 | `clean-no-receipt-write` | `no-receipt-write`, `hazard: false` | match |
| F09 | round-99 | `embedded-write-suspect` | `unguarded-in-place`, embedded site at script line `:6` | match as hazard, and *resolved* rather than suspected |
| F10 | `tools/notes-writer.py` | absent from inventory | absent (11 runner rows, none `tools/`) | match |
| F11 | round-100 | `unguarded` via `os.replace(temp, target)` | `unguarded-in-place` (write `:10`) | match |
| F12 | round-101 | `writes-other-round-receipt` | `no-receipt-write`, `hazard: false` | match: own-receipt scope excludes a foreign round's receipt |

The three bespoke O03 labels (`guard-defined-not-called`, `guard-after-write`,
`embedded-write-suspect`) are non-green in both vocabularies; this tool collapses
them into `unguarded-in-place` with per-site evidence, which is the stricter
reading (a hazard, never a green).

### Integration consequence

Two candidate byte sets exist for `tools/harness/receipt_guard_adoption.py`: this
fragment's tool (38/38 own controls, O03 fixtures and O08 traps satisfied, O04
parity 28/28) and O01's scratch core (O04 parity confirmed by O07, but 4/12 on
O03's fixtures with three false greens). The integrator decides; if O01's core
lands instead of these bytes, O07's defects D5–D7 remain open against it.

## Discipline check (this seat)

- No `reports/round-*/run-validation.py` was executed by this seat or by the
  tool (F-C13-1 prevention): the instruments read text/AST only. The commands
  used are `grep`, `sed`, `ls`, `sha256sum`, `git status`, `python3 -B` on
  `.scratch/o02/*.py` (own drafts) — the drafted tool never spawns a subprocess.
- Fence round-trip: re-extracting the fenced block from this fragment yields
  sha256 `5858abcd0261e8176ebb285db6d80a7c36185d9a12895b4b43b75710db036544`, identical to the draft bytes measured by the commands above.
- Filed bytes untouched: `git status --short` shows only `?? reports/round-34/`
  and zero rows for `reports/round-1..33`, `corpus/lessons`, `tools/gates/frozen`
  (`git rev-parse HEAD` = `da68a6d705e41f369f21e8607bfaab5b54077f84`).
- No commit, no push, no install, no network; only `reports/round-34/op/` written.
- `py_compile` clean; census re-run from `/tmp` with `--root` gives identical
  counts (cwd independence).

## Tool source (complete file, 1309 lines)

```python
#!/usr/bin/env python3
"""Receipt-guard adoption inventory over every filed round runner (F-C13-1).

F-C13-1 (``LOG.md:3548-3567``) recorded that ``reports/round-{5,6,7}/``
``validation.json`` were rewritten in the working tree during the round-33 wave
and restored byte-exact; the mechanism was a **guard-adoption gap**: historical
runners write their own receipt in place and never call
``tools/harness/receipt_guard.py`` (round 14 onward defines the guard). This
instrument turns that prose into a re-runnable census. For every
``reports/round-*/run-validation.py`` it records, with ``path:line`` evidence:

- every in-place write whose target statically resolves to that runner's own
  receipt: ``write_text`` / ``write_bytes`` / ``open`` in a write mode /
  ``os.replace`` / ``os.rename`` / ``shutil.move`` / ``Path.replace``, plus
  receipt writes embedded inside subprocess script strings (the round-19 shape);
- whether the runner loads and calls the guard — a direct entry-point call, a
  ``module.guard_receipt(...)`` / ``namespace["guard_receipt"](...)`` call, or a
  local proxy/preflight function that calls it — and whether such a call
  dominates the receipt write in the same statement block. A ``try:`` whose
  handlers all terminate (``return`` / ``raise`` / ``break`` / ``continue``)
  counts as dominating; a flag-gated call does not;
- an adoption class (``guarded-refresh`` / ``unguarded-in-place`` /
  ``guard-referenced-only`` / ``no-receipt-write`` / ``could-not-evaluate``)
  and the F-C13-1 routing protocol that class implies.

The census is static analysis only: this tool never executes a runner, never
writes into a filed round, and pins each row with the runner's ``sha256`` at
read time. Unknowns are ``could-not-evaluate`` rows with a named reason — the
tool has no green path for a mechanism it cannot resolve.

Exit status: 0 when the census is complete (every runner parsed, no
``could-not-evaluate`` row); 1 when a row is a gap (still printed in full);
2 on usage or IO error. A hazard row does not change the exit status: the
hazards are the census's findings, not its failure.

CLI: receipt_guard_adoption.py [--json] [--out PATH] [--root DIR]
    receipt_guard_adoption.py --sweep-repo [--json]
    receipt_guard_adoption.py --selftest
"""

from __future__ import annotations

import argparse
import ast
import datetime as dt
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

TOOL = "tools/harness/receipt_guard_adoption.py"
SCHEMA = "receipt-guard-adoption/1"
ROOT = Path(__file__).resolve().parents[2]
GUARD_TOOL = "tools/harness/receipt_guard.py"
RUNNER_GLOB = "reports/round-*/run-validation.py"
RUNNER_RE = re.compile(r"^reports/round-(?P<round>\d+)/run-validation\.py$")
SWEEP_ROOTS = ("reports", "tools")
SKIP_DIRS = {".git", ".scratch", "__pycache__", ".mypy_cache", ".pytest_cache"}
GUARD_ENTRIES = ("guard_receipt", "round_runner_main")
RECEIPT_NAME = "validation.json"
WRITE_METHODS = ("write_text", "write_bytes")
OPEN_METHODS = ("open",)
MOVE_DOTTED = ("os.replace", "os.rename", "shutil.move")
WRITE_MODES = ("w", "a", "x", "+")
RESOLVE_ATTRS = ("resolve", "absolute", "expanduser")
# F-C13-1's declared hazards, transcribed from LOG.md:3556-3560. The census
# records agreement per row and never edits this baseline.
DECLARED_HAZARDS = (
    ("reports/round-5/run-validation.py", "LOG.md:3556-3558", ":194"),
    ("reports/round-6/run-validation.py", "LOG.md:3556-3558", ":336"),
    ("reports/round-7/run-validation.py", "LOG.md:3556-3558", ":1171"),
    ("reports/round-26/run-validation.py", "LOG.md:3559-3560", ":90, :1909"),
)
CLASS_PROTOCOL = {
    "guarded-refresh": (
        "guard-adopted: in-tree re-run is refused by the guard once the receipt "
        "is committed (REFRESH_RECEIPTS=1 is the only override); refresh runs "
        "belong in an isolated clone under the lane's .scratch"),
    "unguarded-in-place": (
        "isolated-copy-only: never execute in-tree; work from a git archive or "
        "clone under .scratch (F-C13-1 prevention)"),
    "guard-referenced-only": (
        "isolated-copy-only: the guard is referenced but no call guards its own "
        "receipt write; never execute in-tree"),
    "no-receipt-write": (
        "no in-place write to the runner's own receipt was found; other writes "
        "remain possible — read the row's write evidence before running it"),
    "could-not-evaluate": (
        "manual review required: the census could not resolve this runner's "
        "receipt write or guard status; no protocol is inferred"),
}
CONTROL_LIVE = (
    ("reports/round-5/run-validation.py", "unguarded-in-place", 194),
    ("reports/round-6/run-validation.py", "unguarded-in-place", 336),
    ("reports/round-7/run-validation.py", "unguarded-in-place", 1171),
    ("reports/round-8/run-validation.py", "unguarded-in-place", 1486),
    ("reports/round-9/run-validation.py", "unguarded-in-place", 1910),
    ("reports/round-10/run-validation.py", "unguarded-in-place", 1054),
    ("reports/round-11/run-validation.py", "unguarded-in-place", 1740),
    ("reports/round-12/run-validation.py", "unguarded-in-place", 1071),
    ("reports/round-19/run-validation.py", "unguarded-in-place", 21),
    ("reports/round-21/run-validation.py", "unguarded-in-place", 1115),
    ("reports/round-29/run-validation.py", "unguarded-in-place", 922),
    ("reports/round-32/run-validation.py", "guarded-refresh", 1143),
    ("reports/round-33/run-validation.py", "guarded-refresh", 1471),
)
RECEIPT_PATH_RE = re.compile(r"[A-Za-z0-9_./-]*validation\.json")
EMBEDDED_WRITE_RE = re.compile(r"\.write_text\(|\.write_bytes\(|\bopen\(|json\.dump\(")
UNRESOLVED_HINTS = ("validation", "receipt", "output")


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 16), b""):
            digest.update(block)
    return digest.hexdigest()


def _clip(text, limit=160):
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


# --------------------------------------------------------------- resolution


def _strip_slashes(value):
    while "//" in value:
        value = value.replace("//", "/")
    return value.strip("/") if value not in ("", "/") else ""


class Resolver:
    """Static, best-effort resolution of path-ish expressions to repo-relative text.

    ``resolved`` is ``None`` whenever the expression cannot be resolved; callers
    must treat that as unknown, never as a negative match.
    """

    def __init__(self, runner_rel):
        self.runner_rel = runner_rel
        self.runner_dir = str(Path(runner_rel).parent).replace(os.sep, "/")
        self.consts = {}

    def collect(self, tree, depth=6):
        for node in self._assigns(tree):
            if isinstance(node, ast.Assign):
                targets = [t.id for t in node.targets if isinstance(t, ast.Name)]
                value_node = node.value
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                targets = [node.target.id]
                value_node = node.value
            else:
                continue
            if value_node is None:
                continue
            value, _kind = self.resolve(value_node, depth=depth - 1)
            for name in targets:
                self.consts[name] = (ast.unparse(value_node), value)

    @staticmethod
    def _assigns(tree):
        found = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
                found.append(node)
        return sorted(found, key=lambda n: (n.lineno, n.col_offset))

    def resolve(self, node, depth=6):
        if node is None or depth < 0:
            return None, "unresolved"
        if isinstance(node, ast.Constant):
            if isinstance(node.value, str):
                return _strip_slashes(node.value), "literal"
            return None, "unresolved"
        if isinstance(node, ast.JoinedStr):
            parts = []
            for piece in node.values:
                if isinstance(piece, ast.Constant) and isinstance(piece.value, str):
                    parts.append(piece.value)
                    continue
                if isinstance(piece, ast.FormattedValue):
                    value, kind = self.resolve(piece.value, depth=depth - 1)
                    if value is None or kind == "unresolved":
                        return None, "unresolved"
                    parts.append(value)
                    continue
                return None, "unresolved"
            return _strip_slashes("".join(parts)), "fstring"
        if isinstance(node, ast.BinOp):
            left, left_kind = self.resolve(node.left, depth=depth - 1)
            right, right_kind = self.resolve(node.right, depth=depth - 1)
            if isinstance(node.op, ast.Add):
                if left is None or right is None:
                    return None, "unresolved"
                return _strip_slashes(left + right), "concat"
            if isinstance(node.op, ast.Div):
                if left is None or right is None:
                    return None, "unresolved"
                return _strip_slashes(f"{left}/{right}"), "join"
            return None, "unresolved"
        if isinstance(node, ast.Name):
            if node.id == "__file__":
                return self.runner_rel, "runner-file"
            if node.id in ("ROOT", "REPO_ROOT", "ROOT_DIR"):
                return "", "root-name"
            entry = self.consts.get(node.id)
            if entry is None:
                return None, "unresolved"
            return entry[1], "const"
        if isinstance(node, ast.Attribute):
            return self._attribute(node, depth)
        if isinstance(node, ast.Call):
            return self._call(node, depth)
        return None, "unresolved"

    def _attribute(self, node, depth):
        if node.attr == "parent" or node.attr == "parents":
            base, kind = self.resolve(node.value, depth=depth - 1)
            if base is None:
                return None, "unresolved"
            if node.attr == "parent":
                return self._drop(base, 1), f"{kind}.parent"
            return None, "unresolved"
        if node.attr in RESOLVE_ATTRS:
            return self.resolve(node.value, depth)
        return None, "unresolved"

    def _call(self, node, depth):
        func = node.func
        if isinstance(func, ast.Attribute) and func.attr in RESOLVE_ATTRS:
            return self.resolve(func.value, depth)
        if isinstance(func, ast.Attribute) and func.attr == "parents":
            return None, "unresolved"
        if isinstance(func, ast.Attribute) and func.attr == "Path" and node.args:
            return self.resolve(node.args[0], depth=depth - 1)
        if isinstance(func, ast.Attribute) and func.attr == "join":
            parts = [self.resolve(arg, depth=depth - 1)[0] for arg in node.args]
            if any(part is None for part in parts):
                return None, "unresolved"
            return _strip_slashes("/".join(parts)), "os.path.join"
        if isinstance(func, ast.Subscript):
            # Path(...).parents[N]
            base, kind = self.resolve(func.value, depth=depth - 1)
            index = func.slice
            if base is not None and isinstance(index, ast.Constant) and isinstance(index.value, int):
                return self._drop(base, index.value + 1), "parents[index]"
            return None, "unresolved"
        if isinstance(func, ast.Name):
            if func.id == "Path":
                if not node.args:
                    return None, "unresolved"
                return self.resolve(node.args[0], depth=depth - 1)
            if func.id in ("str", "repr"):
                if not node.args:
                    return None, "unresolved"
                return self.resolve(node.args[0], depth=depth - 1)
            if func.id == "getattr" and len(node.args) >= 2:
                return None, "unresolved"
            if node.args:
                inner, kind = self.resolve(node.args[0], depth=depth - 1)
                if inner is not None:
                    return inner, f"wrapper:{func.id}"
            return None, "unresolved"
        return None, "unresolved"

    @staticmethod
    def _drop(value, count):
        parts = [part for part in _strip_slashes(value).split("/") if part]
        if count >= len(parts):
            return ""
        return "/".join(parts[: len(parts) - count])


# ----------------------------------------------------------------- evidence


class NodeMaps:
    """Parent links and statement-list membership for dominance walking."""

    LIST_ATTRS = ("body", "orelse", "finalbody", "handlers")

    def __init__(self, tree):
        self.parent = {}
        self.lists = {}
        for node in ast.walk(tree):
            for child in ast.iter_child_nodes(node):
                self.parent.setdefault(id(child), (node, None))
            for attr in self.LIST_ATTRS:
                value = getattr(node, attr, None)
                if isinstance(value, list):
                    statements = [child for child in value if isinstance(child, ast.stmt)]
                    if statements:
                        self.lists[(id(node), attr)] = statements
                    for child in value:
                        self.parent[id(child)] = (node, attr)
        self.parent[id(tree)] = None

    def chain(self, node):
        """Statement lists from the node's innermost list outward, with index."""
        chain = []
        current = node
        while True:
            entry = self.parent.get(id(current))
            if entry is None:
                break
            owner, attr = entry
            if attr is not None:
                statements = self.lists.get((id(owner), attr), [])
                index = next((i for i, s in enumerate(statements) if s is current), None)
                if index is not None:
                    chain.append((statements, index))
            current = owner
        return chain


def _dotted(node):
    try:
        return ast.unparse(node)
    except Exception:  # pragma: no cover - ast.unparse is total in practice
        return "?"


def _guard_entry(func):
    """Recognize the guard's callable shapes: name, ``module.x``, ``ns["x"]``."""
    if isinstance(func, ast.Name) and func.id in GUARD_ENTRIES:
        return f"call:{func.id}", func.id
    if isinstance(func, ast.Attribute) and func.attr in GUARD_ENTRIES:
        return f"call:{_dotted(func)}", func.attr
    if isinstance(func, ast.Subscript) and isinstance(func.slice, ast.Constant):
        if isinstance(func.slice.value, str) and func.slice.value in GUARD_ENTRIES:
            return f"subscript:{_dotted(func)}", func.slice.value
    return None


def _is_guard_call(node, proxies, consts, depth=2):
    if not isinstance(node, ast.Call):
        return None
    entry = _guard_entry(node.func)
    if entry:
        return entry
    func = node.func
    if isinstance(func, ast.Name):
        definition = proxies.get(func.id)
        if definition is not None and _function_calls_guard(definition, proxies, depth - 1):
            return f"proxy:{func.id}", func.id
    return None


def _function_calls_guard(definition, proxies, depth=2):
    if depth < 0:
        return False
    for node in ast.walk(definition):
        if isinstance(node, ast.Call) and _guard_entry(node.func):
            return True
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            nested = proxies.get(node.func.id)
            if nested is not None and nested is not definition and _function_calls_guard(nested, proxies, depth - 1):
                return True
    return False


def _terminates(statements):
    for statement in reversed(statements):
        if isinstance(statement, (ast.Return, ast.Raise, ast.Break, ast.Continue)):
            return True
        if isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call):
            if isinstance(statement.value.func, ast.Name) and statement.value.func.id == "exit":
                return True
        return False
    return False


def _try_provider(statement, proxies, consts):
    """A ``try:`` whose body is guard calls and whose handlers all terminate."""
    if not isinstance(statement, ast.Try) or not statement.body:
        return None
    providers = [_is_guard_call(s.value, proxies, consts) for s in statement.body
                 if isinstance(s, ast.Expr)]
    if len(providers) != len(statement.body) or not all(providers):
        return None
    for handler in statement.handlers:
        if not handler.body or not _terminates(handler.body):
            return None
    return {"line": statement.lineno, "kind": "try-guard",
            "entries": [entry[1] for entry in providers],
            "call_lines": [s.lineno for s in statement.body]}


def _statement_provider(statement, proxies, consts):
    if isinstance(statement, ast.Expr):
        found = _is_guard_call(statement.value, proxies, consts)
        if found:
            return {"line": statement.lineno, "kind": found[0], "entries": [found[1]]}
        return None
    return _try_provider(statement, proxies, consts)


def _conditional_guard_calls(node, proxies, consts, found, depth=0):
    """Guard calls nested inside non-dominating statement kinds (flag gates)."""
    if depth > 3:
        return
    for attr in ("body", "orelse", "finalbody"):
        for child in getattr(node, attr, None) or []:
            if isinstance(child, ast.Expr):
                entry = _is_guard_call(child.value, proxies, consts)
                if entry:
                    found.append({"line": child.lineno, "kind": entry[0]})
            if isinstance(child, ast.If):
                _conditional_guard_calls(child, proxies, consts, found, depth + 1)


def _dominating_provider(chain, proxies, consts, conditional):
    for body, index in chain:
        for statement in reversed(body[:index]):
            provider = _statement_provider(statement, proxies, consts)
            if provider:
                return provider
            _conditional_guard_calls(statement, proxies, consts, conditional)
    return None


def write_sites(tree, resolver, runner_rel, own_receipt):
    """AST write sites whose destination resolves to the runner's own receipt."""
    sites = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        kind = None
        target = None
        if isinstance(func, ast.Attribute) and func.attr in WRITE_METHODS:
            kind, target = func.attr, func.value
        elif isinstance(func, ast.Attribute) and func.attr in OPEN_METHODS:
            mode = node.args[1] if len(node.args) > 1 else None
            for keyword in node.keywords:
                if keyword.arg == "mode":
                    mode = keyword.value
            if isinstance(mode, ast.Constant) and isinstance(mode.value, str):
                if any(flag in mode.value for flag in WRITE_MODES):
                    kind, target = "open(write)", func.value
        elif isinstance(func, ast.Name) and func.id in OPEN_METHODS:
            mode = node.args[1] if len(node.args) > 1 else None
            for keyword in node.keywords:
                if keyword.arg == "mode":
                    mode = keyword.value
            if isinstance(mode, ast.Constant) and isinstance(mode.value, str) \
                    and any(flag in mode.value for flag in WRITE_MODES):
                kind, target = "open(write)", node.args[0] if node.args else None
        elif isinstance(func, ast.Attribute) and _dotted(func) in MOVE_DOTTED:
            if len(node.args) >= 2:
                kind, target = _dotted(func), node.args[1]
        elif isinstance(func, ast.Attribute) and func.attr == "replace" and node.args:
            receiver, _kind = resolver.resolve(func.value)
            if receiver is not None:
                kind, target = "Path.replace", node.args[0]
        if kind is None or target is None:
            continue
        resolved, how = resolver.resolve(target)
        if resolved != own_receipt:
            continue
        sites.append({"line": node.lineno, "kind": kind,
                      "target": _clip(ast.unparse(target)),
                      "resolved": resolved, "resolution": how,
                      "src": _clip(ast.unparse(node)), "_node": node})
    return sorted(sites, key=lambda row: row["line"])


def embedded_write_sites(tree, own_receipt, runner_rel):
    """Receipt writes hidden inside string literals (subprocess script shape).

    A literal that parses as Python is analyzed with the same write-site rule,
    so a read (``open(PATH)`` / ``read_text``) inside a script is not a site;
    the reported line is the file line of the embedded statement.
    """
    sites, opaque = [], []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Constant) or not isinstance(node.value, str):
            continue
        text = node.value
        if RECEIPT_NAME not in text:
            continue
        try:
            inner = ast.parse(text)
        except SyntaxError:
            if EMBEDDED_WRITE_RE.search(text) and RECEIPT_PATH_RE.search(text):
                opaque.append({"literal_line": node.lineno,
                               "reason": "literal mentions a write verb and "
                                         "validation.json but does not parse as Python"})
            continue
        resolver = Resolver(runner_rel)
        resolver.collect(inner)
        for site in write_sites(inner, resolver, runner_rel, own_receipt):
            site.pop("_node", None)
            site["kind"] = "embedded:" + site["kind"]
            site["literal_line"] = node.lineno
            site["line"] = node.lineno + site["line"] - 1
            site["resolution"] = "embedded-script"
            sites.append(site)
    seen = set()
    unique = []
    for site in sorted(sites, key=lambda row: row["line"]):
        key = (site["line"], site["kind"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(site)
    return unique, opaque


def guard_evidence(tree, resolver):
    loads, calls, refresh = [], [], []
    proxies = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if "receipt_guard" in node.value and RECEIPT_NAME not in node.value:
                loads.append({"line": node.lineno, "form": "guard-path-string",
                              "detail": _clip(node.value)})
            if node.value == "REFRESH_RECEIPTS":
                refresh.append({"line": node.lineno, "form": "refresh-env-string"})
        if isinstance(node, ast.Name) and node.id == "REFRESH_RECEIPTS":
            refresh.append({"line": node.lineno, "form": "refresh-env-name"})
        if isinstance(node, ast.Import):
            for alias in node.names:
                if "receipt_guard" in alias.name:
                    loads.append({"line": node.lineno, "form": "import",
                                  "detail": alias.name})
        if isinstance(node, ast.ImportFrom) and node.module and "receipt_guard" in node.module:
            loads.append({"line": node.lineno, "form": "from-import",
                          "detail": f"{node.module}:{','.join(a.name for a in node.names)}"})
        if isinstance(node, ast.Call):
            entry = _guard_entry(node.func)
            if entry:
                receipt_arg = None
                if node.args:
                    receipt_arg, _how = resolver.resolve(node.args[0])
                calls.append({"line": node.lineno, "form": entry[0],
                              "detail": _clip(ast.unparse(node)),
                              "receipt_arg": receipt_arg})
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            proxies[node.name] = node
    proxy_rows = []
    for name, definition in sorted(proxies.items()):
        guard_lines = [child.lineno for child in ast.walk(definition)
                       if isinstance(child, ast.Call) and _guard_entry(child.func)]
        if guard_lines:
            proxy_rows.append({"name": name, "line": definition.lineno,
                               "guard_call_lines": sorted(guard_lines)})
    loads.sort(key=lambda row: (row["line"], row["form"]))
    calls.sort(key=lambda row: row["line"])
    refresh = sorted({(row["line"], row["form"]): row for row in refresh}.values(),
                     key=lambda row: row["line"])
    return {"loads": loads, "calls": calls, "refresh_references": refresh,
            "proxy_defs": proxy_rows}


def analyze(rel, text):
    row = {"runner": rel, "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
           "lines": text.count("\n") + 1}
    match = RUNNER_RE.match(rel)
    round_number = int(match.group("round")) if match else None
    row["round"] = round_number
    own_receipt = f"reports/round-{round_number}/{RECEIPT_NAME}" if round_number else None
    row["receipt"] = own_receipt
    try:
        tree = ast.parse(text)
    except SyntaxError as error:
        row.update({"parse": "error", "parse_error": f"{error.msg} (line {error.lineno})",
                    "class": "could-not-evaluate", "hazard": None,
                    "route": CLASS_PROTOCOL["could-not-evaluate"],
                    "receipt_writes": [], "embedded_receipt_writes": [],
                    "guard": {"loads": [], "calls": [], "refresh_references": [], "proxy_defs": []},
                    "reasons": [f"could-not-evaluate: unparsable source "
                                f"({error.msg} at line {error.lineno})"]})
        return row
    row["parse"] = "ok"
    resolver = Resolver(rel)
    resolver.collect(tree)
    guard = guard_evidence(tree, resolver)
    sites = write_sites(tree, resolver, rel, own_receipt)
    embedded, embedded_opaque = embedded_write_sites(tree, own_receipt, rel)
    maps = NodeMaps(tree)
    proxies = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            proxies[node.name] = node
    conditional = []
    for site in sites:
        node = site.pop("_node", None)
        provider = None
        if node is not None:
            provider = _dominating_provider(maps.chain(node), proxies, resolver, conditional)
        site["guarded"] = provider is not None
        site["guard_provider"] = provider
    for site in embedded:
        site["guarded"] = False
        site["guard_provider"] = None
        site["note"] = ("receipt write embedded in a subprocess script string; "
                        "no in-file guard call can dominate it")
    # Writes whose destination text smells like the receipt but does not resolve.
    unresolved = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        target = None
        if isinstance(func, ast.Attribute) and func.attr in WRITE_METHODS:
            target = func.value
        elif isinstance(func, ast.Name) and func.id == "open" and node.args:
            target = node.args[0]
        if target is None:
            continue
        resolved, _how = resolver.resolve(target)
        if resolved is not None:
            continue
        text_target = _dotted(target).lower()
        if any(hint in text_target for hint in UNRESOLVED_HINTS):
            unresolved.append({"line": node.lineno, "target": _clip(_dotted(target))})
    row["receipt_writes"] = sites
    row["embedded_receipt_writes"] = embedded
    row["embedded_unparsed_literals"] = embedded_opaque
    row["guard"] = guard
    row["unresolved_write_targets"] = unresolved
    write_count = len(sites) + len(embedded)
    reasons = []
    if not write_count:
        if unresolved:
            row["class"] = "could-not-evaluate"
            row["hazard"] = None
            reasons.append("could-not-evaluate: write targets referencing "
                           "receipt/output-like names do not resolve: "
                           + ", ".join(f":{item['line']}" for item in unresolved))
        else:
            row["class"] = "no-receipt-write"
            row["hazard"] = False
            reasons.append("no in-place write to the runner's own receipt "
                           f"({own_receipt}) was found")
    elif all(site["guarded"] for site in sites) and not embedded:
        row["class"] = "guarded-refresh"
        row["hazard"] = False
        reasons.append("every resolved receipt write is dominated by a guard call "
                       f"({', '.join(':' + str(site['guard_provider']['line']) for site in sites)})")
        if guard["calls"]:
            reasons.append("guard entry calls at "
                           + ", ".join(':' + str(call["line"]) for call in guard["calls"]))
    else:
        if not guard["calls"] and guard["loads"]:
            row["class"] = "guard-referenced-only"
            row["hazard"] = True
            reasons.append("guard loaded/referenced but never called in this file")
        else:
            row["class"] = "unguarded-in-place"
            row["hazard"] = True
        if embedded:
            reasons.append("receipt write embedded in a script string: "
                           + ", ".join(':' + str(site["line"]) for site in embedded))
        if not guard["calls"] and not guard["loads"] and not guard["refresh_references"]:
            reasons.append("no guard reference of any kind in this file")
        elif not guard["calls"] and guard["loads"]:
            reasons.append("guard loaded but no guard entry call found")
        elif not guard["calls"]:
            reasons.append("only REFRESH_RECEIPTS references, which gate other "
                           "runners' refresh runs, not this runner's own write")
        else:
            unguarded = [site for site in sites if not site["guarded"]]
            reasons.append("guard call exists but does not dominate the write: "
                           + ", ".join(':' + str(site["line"]) for site in unguarded or sites))
        if conditional:
            reasons.append("flag-gated guard calls (do not dominate): "
                           + ", ".join(':' + str(item["line"]) for item in conditional))
    if row["hazard"] is True and unresolved:
        reasons.append("unresolved receipt-like write targets are also present: "
                       + ", ".join(f":{item['line']}" for item in unresolved))
    row["route"] = CLASS_PROTOCOL[row["class"]]
    row["reasons"] = reasons
    return row


# ------------------------------------------------------------------- census


def runner_paths(root):
    return sorted(
        (path for path in root.glob(RUNNER_GLOB) if RUNNER_RE.match(
            path.relative_to(root).as_posix())),
        key=lambda path: int(RUNNER_RE.match(path.relative_to(root).as_posix()).group("round")))


def census(root):
    rows = []
    for path in runner_paths(root):
        rel = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            rows.append({"runner": rel, "round": int(RUNNER_RE.match(rel).group("round")),
                         "parse": "error", "parse_error": f"{type(error).__name__}: {error}",
                         "class": "could-not-evaluate", "hazard": None,
                         "route": CLASS_PROTOCOL["could-not-evaluate"],
                         "receipt_writes": [], "embedded_receipt_writes": [],
                         "guard": {"loads": [], "calls": [], "refresh_references": [],
                                   "proxy_defs": []},
                         "reasons": [f"could-not-evaluate: unreadable ({error})"]})
            continue
        rows.append(analyze(rel, text))
    by_path = {row["runner"]: row for row in rows}
    class_counts = {}
    for row in rows:
        class_counts[row["class"]] = class_counts.get(row["class"], 0) + 1
    declared_rows = []
    for path, source, declared_lines in DECLARED_HAZARDS:
        row = by_path.get(path)
        observed = row["class"] if row else None
        declared_rows.append({
            "runner": path, "declared_by": source, "declared_lines": declared_lines,
            "declared_class": "unguarded-in-place",
            "observed_class": observed,
            "agrees": observed == "unguarded-in-place",
            "evidence": [] if row is None else (
                [f"{path}:{site['line']}" for site in row["receipt_writes"]]
                + [f"{path}:{call['line']} (guard call)"
                   for call in row["guard"]["calls"]])})
    findings = []
    for declared in declared_rows:
        if not declared["agrees"]:
            findings.append({
                "id": f"RGA-1-{Path(declared['runner']).parts[1]}",
                "kind": "declared-hazard-mismatch",
                "runner": declared["runner"],
                "detail": (f"F-C13-1 ({declared['declared_by']}) names "
                           f"{declared['declared_lines']} as carrying the same "
                           f"unguarded in-place hazard; the live bytes classify as "
                           f"{declared['observed_class']}"),
                "evidence": declared["evidence"],
                "owner": "integrator (round 34) — filed LOG.md bytes are not edited; "
                         "this row is the new-record correction"})
    undeclared = [row["runner"] for row in rows
                  if row["hazard"] is True
                  and row["runner"] not in {item[0] for item in DECLARED_HAZARDS}]
    if undeclared:
        findings.append({
            "id": "RGA-2",
            "kind": "undeclared-unguarded-writer",
            "runner": None,
            "detail": (f"{len(undeclared)} runner(s) write their own receipt without "
                       "a dominating guard call and are not in the F-C13-1 declared set"),
            "evidence": undeclared,
            "owner": "integrator (round 34) — routing row per runner below"})
    gaps = [row["runner"] for row in rows if row["class"] == "could-not-evaluate"]
    guard_path = root / GUARD_TOOL
    report = {
        "tool": TOOL,
        "schema": SCHEMA,
        "mode": "runner-census",
        "root": str(root),
        "date": dt.date.today().isoformat(),
        "glob": RUNNER_GLOB,
        "runner_count": len(rows),
        "class_counts": dict(sorted(class_counts.items())),
        "hazard_count": sum(1 for row in rows if row["hazard"] is True),
        "census_complete": not gaps,
        "gaps": gaps,
        "guard_tool": {
            "path": GUARD_TOOL,
            "sha256": sha256_file(guard_path) if guard_path.is_file() else None,
            "present": guard_path.is_file()},
        "declared_hazards": declared_rows,
        "findings": findings,
        "protocols": CLASS_PROTOCOL,
        "runners": rows,
        "limits": [
            "Static AST/text analysis at read time, not execution: a runner's "
            "runtime behaviour, aliasing beyond the resolved constant map, or a "
            "write performed by a helper it calls can differ from this census, "
            "which is why could-not-evaluate rows are never greened.",
            "Recognized write idioms are write_text/write_bytes, open() in a "
            "write mode, os.replace/os.rename/shutil.move, Path.replace with a "
            "resolvable receiver, and receipt writes embedded in string "
            "literals; other publication idioms are recorded only when their "
            "destination resolves.",
            "Row digests pin the bytes read during this census, not HEAD at "
            "commit time; re-run after any landing that touches a runner.",
            "This tool executes no round runner and writes no filed receipt; "
            "--out refuses absolute paths, path escapes, and validation.json "
            "destinations.",
        ],
    }
    return report


def sweep_repo(root):
    rows = []
    scanned = 0
    for base in SWEEP_ROOTS:
        for path in sorted((root / base).rglob("*.py")):
            rel = path.relative_to(root).as_posix()
            if any(part in SKIP_DIRS for part in Path(rel).parts):
                continue
            scanned += 1
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError) as error:
                rows.append({"path": rel, "parse": "error",
                             "parse_error": f"{type(error).__name__}: {error}",
                             "kind": "runner" if RUNNER_RE.match(rel) else "non-runner",
                             "receipt_writes": []})
                continue
            resolver = Resolver(rel)
            try:
                tree = ast.parse(text)
            except SyntaxError as error:
                rows.append({"path": rel, "parse": "error",
                             "parse_error": f"{error.msg} (line {error.lineno})",
                             "kind": "runner" if RUNNER_RE.match(rel) else "non-runner",
                             "receipt_writes": []})
                continue
            resolver.collect(tree)
            writes = []
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                func = node.func
                target = None
                kind = None
                if isinstance(func, ast.Attribute) and func.attr in WRITE_METHODS:
                    kind, target = func.attr, func.value
                elif isinstance(func, ast.Attribute) and _dotted(func) in MOVE_DOTTED:
                    if len(node.args) >= 2:
                        kind, target = _dotted(func), node.args[1]
                if target is None:
                    continue
                resolved, _how = resolver.resolve(target)
                if resolved and re.match(r"^reports/round-\d+/validation\.json$", resolved):
                    writes.append({"line": node.lineno, "kind": kind,
                                   "target": _clip(ast.unparse(target)),
                                   "resolved": resolved,
                                   "src": _clip(ast.unparse(node))})
            if writes:
                rows.append({"path": rel, "parse": "ok",
                             "kind": "runner" if RUNNER_RE.match(rel) else "non-runner",
                             "receipt_writes": sorted(writes, key=lambda row: row["line"])})
    complete = not any(row["parse"] == "error" for row in rows)
    return {"tool": TOOL, "schema": SCHEMA, "mode": "repo-sweep",
            "root": str(root), "date": dt.date.today().isoformat(),
            "files_scanned": scanned,
            "writers": [row for row in rows if row["receipt_writes"]],
            "parse_gaps": [row for row in rows if row["parse"] == "error"],
            "sweep_complete": complete,
            "limits": [
                "Same static discipline as the runner census for AST-visible "
                "writes; unlike the census, the sweep does not re-parse embedded "
                "script strings, so a receipt write hidden inside a string "
                "literal in a non-runner file would not appear here.",
                "The writers list includes runners (see the census for adoption "
                "classes) and any non-runner row is listed with kind=non-runner.",
            ]}


# ------------------------------------------------------------------ selftest

FIXTURES = {
    "reports/round-41/run-validation.py": '''\
import runpy
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = "reports/round-41"
OUTPUT = f"{ROUND_DIR}/validation.json"


def guard_receipt():
    namespace = runpy.run_path(str(ROOT / "tools/harness/receipt_guard.py"))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def safe_path(relative):
    return ROOT / relative


def main(check=False):
    rendered = "{}\\n"
    if check:
        print(rendered, end="")
    else:
        guard_receipt()
        safe_path(OUTPUT).write_text(rendered, encoding="utf-8")
    return 0
''',
    "reports/round-42/run-validation.py": '''\
import importlib.util
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
GUARD = "tools/harness/receipt_guard.py"
OUTPUT = "reports/round-42/validation.json"


def guard_preflight():
    spec = importlib.util.spec_from_file_location("fixture_guard", ROOT / GUARD)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.guard_receipt(ROOT / OUTPUT, repo_root=ROOT)


def main(check=False):
    if check:
        print("{}")
    else:
        guard_preflight()
        (ROOT / OUTPUT).write_text("{}\\n", encoding="utf-8")
    return 0
''',
    "reports/round-43/run-validation.py": '''\
import runpy
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "reports/round-43/validation.json"


def guard_receipt():
    namespace = runpy.run_path(str(ROOT / "tools/harness/receipt_guard.py"))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def safe_path(relative):
    return ROOT / relative


def main(check=False):
    if check:
        print("{}")
    else:
        try:
            guard_receipt()
        except SystemExit as error:
            return error.code if isinstance(error.code, int) else 3
        safe_path(OUTPUT).write_text("{}\\n", encoding="utf-8")
    return 0
''',
    "reports/round-44/run-validation.py": '''\
from pathlib import Path
HERE = Path(__file__).resolve().parent


def main():
    (HERE / "validation.json").write_text("{}\\n", encoding="utf-8")
    return 0
''',
    "reports/round-45/run-validation.py": '''\
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.harness.receipt_guard import guard_receipt  # noqa: F401  (imported, never called)
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "reports/round-45/validation.json"


def main():
    (ROOT / OUTPUT).write_text("{}\\n", encoding="utf-8")
    return 0
''',
    "reports/round-46/run-validation.py": '''\
import runpy
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "reports/round-46/validation.json"


def guard_receipt():
    namespace = runpy.run_path(str(ROOT / "tools/harness/receipt_guard.py"))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def main(audit=False):
    if audit:
        guard_receipt()
    (ROOT / OUTPUT).write_text("{}\\n", encoding="utf-8")
    return 0
''',
    "reports/round-47/run-validation.py": '''\
import os
import runpy
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "reports/round-47/validation.json"


def guard_receipt():
    namespace = runpy.run_path(str(ROOT / "tools/harness/receipt_guard.py"))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def main():
    guard_receipt()
    temporary = ROOT / ".scratch/fixture-47.json"
    temporary.write_text("{}\\n", encoding="utf-8")
    os.replace(temporary, ROOT / OUTPUT)
    return 0
''',
    "reports/round-48/run-validation.py": '''\
import os
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = "reports/round-48/validation.json"


def main():
    temporary = ROOT / ".scratch/fixture-48.json"
    temporary.write_text("{}\\n", encoding="utf-8")
    os.replace(temporary, ROOT / OUTPUT)
    return 0
''',
    "reports/round-49/run-validation.py": '''\
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]


def main():
    (ROOT / ".scratch/fixture-49.json").write_text("{}\\n", encoding="utf-8")
    (ROOT / "reports/round-41/validation.json").write_text("{}\\n", encoding="utf-8")
    return 0
''',
    "reports/round-50/run-validation.py": "def main(:\n    pass\n",
    "reports/round-51/run-validation.py": '''\
import subprocess
import sys
result = subprocess.run([sys.executable, "-c", """
import json, pathlib
v = json.load(open('reports/round-51/validation.json'))
pathlib.Path('reports/round-51/validation.json').write_text(json.dumps(v, indent=1))
print('acceptance:', True)
"""], capture_output=True, text=True)
print(result.stdout.strip())
''',
    "tools/fixture-helper.py": '''\
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]


def main():
    (ROOT / "reports/round-41/validation.json").write_text("{}\\n", encoding="utf-8")
''',
}

FIXTURE_RUNNERS = tuple(rel for rel in FIXTURES if RUNNER_RE.match(rel))

FIXTURE_EXPECTED = {
    "reports/round-41/run-validation.py": "guarded-refresh",
    "reports/round-42/run-validation.py": "guarded-refresh",
    "reports/round-43/run-validation.py": "guarded-refresh",
    "reports/round-44/run-validation.py": "unguarded-in-place",
    "reports/round-45/run-validation.py": "guard-referenced-only",
    "reports/round-46/run-validation.py": "unguarded-in-place",
    "reports/round-47/run-validation.py": "guarded-refresh",
    "reports/round-48/run-validation.py": "unguarded-in-place",
    "reports/round-49/run-validation.py": "no-receipt-write",
    "reports/round-50/run-validation.py": "could-not-evaluate",
    "reports/round-51/run-validation.py": "unguarded-in-place",
}


def _fixture_control(rows, rel, expected_class, controls, note=""):
    row = rows.get(rel)
    passed = row is not None and row["class"] == expected_class
    if expected_class == "guarded-refresh":
        passed = passed and row.get("hazard") is False
    if expected_class in ("unguarded-in-place", "guard-referenced-only"):
        passed = passed and row.get("hazard") is True
    if expected_class == "no-receipt-write":
        passed = passed and row.get("hazard") is False
    controls.append({"control": f"fixture-{Path(rel).parts[1]}-{expected_class}",
                     "passed": bool(passed), "expected_class": expected_class,
                     "observed_class": row["class"] if row else None, "note": note})


def selftest():
    controls = []
    scratch = ROOT / ".scratch"
    scratch.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="rga-", dir=scratch) as temporary:
        fixture_root = Path(temporary) / "repo"
        for rel, text in FIXTURES.items():
            path = fixture_root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        report = census(fixture_root)
        rows = {row["runner"]: row for row in report["runners"]}
        for rel, expected_class in FIXTURE_EXPECTED.items():
            _fixture_control(rows, rel, expected_class, controls)
        controls.append({
            "control": "fixture-census-covers-every-runner",
            "passed": sorted(rows) == sorted(FIXTURE_RUNNERS),
            "expected": sorted(FIXTURE_RUNNERS), "observed": sorted(rows)})
        controls.append({
            "control": "fixture-non-runner-writer-absent",
            "passed": "tools/fixture-helper.py" not in rows
            and all(row["runner"] != "tools/fixture-helper.py" for row in report["runners"]),
            "note": "a non-runner .py writing reports/round-41/validation.json is not a runner row"})
        controls.append({
            "control": "fixture-guarded-runners-not-flagged",
            "passed": all(rows[rel]["hazard"] is False
                          for rel in ("reports/round-41/run-validation.py",
                                      "reports/round-42/run-validation.py",
                                      "reports/round-43/run-validation.py",
                                      "reports/round-47/run-validation.py")),
            "note": "no false hazard flag on any guarded fixture"})
        controls.append({
            "control": "fixture-foreign-writes-not-flagged",
            "passed": rows["reports/round-49/run-validation.py"]["hazard"] is False
            and not rows["reports/round-49/run-validation.py"]["receipt_writes"],
            "note": "scratch-fixture and other-round writes are not own-receipt writes"})
        controls.append({
            "control": "fixture-flag-gated-guard-not-adopted",
            "passed": rows["reports/round-46/run-validation.py"]["class"] != "guarded-refresh"
            and any("flag-gated" in reason
                    for reason in rows["reports/round-46/run-validation.py"]["reasons"]),
            "note": "a guard call under an unset flag does not dominate the write"})
        controls.append({
            "control": "fixture-syntax-error-is-a-gap",
            "passed": report["census_complete"] is False
            and rows["reports/round-50/run-validation.py"]["class"] == "could-not-evaluate",
            "note": "an unparsable runner is a census gap, never a green"})
        controls.append({
            "control": "fixture-embedded-write-line",
            "passed": bool(
                [site for site in rows["reports/round-51/run-validation.py"]["embedded_receipt_writes"]
                 if site["line"] == 6 and site["kind"] == "embedded:write_text"]
                and not [site for site in rows["reports/round-51/run-validation.py"]
                         ["embedded_receipt_writes"] if site["kind"] == "embedded:open"]),
            "note": "the embedded write is located at its script line (fixture :6) and "
                    "the json.load(open(...)) read is not a site"})
        again = census(fixture_root)
        strip = lambda payload: json.dumps(  # noqa: E731
            {key: value for key, value in payload.items()
             if key not in ("date", "root")}, sort_keys=True)
        controls.append({"control": "fixture-deterministic",
                         "passed": strip(report) == strip(again),
                         "note": "same tree, same census"})

    live = census(ROOT)
    live_rows = {row["runner"]: row for row in live["runners"]}
    for rel, expected_class, line in CONTROL_LIVE:
        row = live_rows.get(rel)
        observed = row["class"] if row else None
        write_lines = [] if row is None else [site["line"] for site in row["receipt_writes"]]
        passed = observed == expected_class and (line in write_lines or line in
                                                 [site["line"] for site in
                                                  row.get("embedded_receipt_writes", [])]) \
            if row else False
        controls.append({"control": f"live-{Path(rel).parts[1]}-{expected_class}",
                         "passed": bool(passed), "expected_class": expected_class,
                         "observed_class": observed, "expected_write_line": line,
                         "observed_write_lines": write_lines})
    r26 = live_rows.get("reports/round-26/run-validation.py")
    provider = r26["receipt_writes"][0]["guard_provider"] if (r26 and r26["receipt_writes"]) else None
    controls.append({
        "control": "live-r26-guard-call-precedes-write",
        "passed": bool(r26 and r26["class"] == "guarded-refresh" and r26["hazard"] is False
                       and r26["receipt_writes"] and r26["receipt_writes"][0]["guarded"] is True
                       and provider and provider.get("kind") == "try-guard"
                       and provider.get("call_lines") == [1906]),
        "note": ("F-C13-1 (LOG.md:3559-3560) names r26 as carrying the unguarded "
                 "hazard; the bytes show the guard call at :1906 dominating the "
                 ":1909 write — recorded as finding RGA-1-r26, filed bytes not edited"),
        "observed": None if r26 is None else {
            "class": r26["class"],
            "write": r26["receipt_writes"][0]["line"] if r26["receipt_writes"] else None,
            "provider": r26["receipt_writes"][0]["guard_provider"]
            if r26["receipt_writes"] else None}})
    r19 = live_rows.get("reports/round-19/run-validation.py")
    controls.append({
        "control": "live-r19-embedded-receipt-write",
        "passed": bool(r19 and r19["class"] == "unguarded-in-place"
                       and [site for site in r19["embedded_receipt_writes"]
                            if site["line"] == 21 and site["kind"] == "embedded:write_text"]
                       and not [site for site in r19["embedded_receipt_writes"]
                                if site["kind"] == "embedded:open"]),
        "note": "the r19 receipt write lives inside a subprocess script string at :21; "
                "the open(...) read at :19 is not a site",
        "observed": None if r19 is None else [site["line"] for site in
                                              r19["embedded_receipt_writes"]]})
    controls.append({
        "control": "live-runner-census-floor",
        "passed": live["runner_count"] >= 28,
        "observed": live["runner_count"],
        "note": "28 runners were filed at baseline da68a6d; later rounds may add more"})
    controls.append({
        "control": "live-declared-hazard-four-classified",
        "passed": all(row["observed_class"] is not None for row in live["declared_hazards"]),
        "observed": [{"runner": row["runner"], "observed": row["observed_class"],
                      "agrees": row["agrees"]} for row in live["declared_hazards"]]})
    controls.append({
        "control": "live-findings-recorded",
        "passed": any(finding["kind"] == "declared-hazard-mismatch"
                      for finding in live["findings"])
        and any(finding["kind"] == "undeclared-unguarded-writer"
                for finding in live["findings"]),
        "observed": [finding["id"] for finding in live["findings"]]})
    controls.append({
        "control": "live-guard-digest",
        "passed": bool(live["guard_tool"]["sha256"]),
        "observed": live["guard_tool"]["sha256"]})
    passed = sum(1 for control in controls if control["passed"])
    receipt = {
        "tool": TOOL,
        "command": f"python3 {TOOL} --selftest",
        "date": dt.date.today().isoformat(),
        "fixture_count": len(FIXTURE_EXPECTED),
        "live_runner_count": live["runner_count"],
        "live_class_counts": live["class_counts"],
        "live_findings": [finding["id"] for finding in live["findings"]],
        "controls": controls,
        "controls_passed": passed,
        "controls_total": len(controls),
        "selftest_passed": passed == len(controls),
        "limits": [
            "Fixtures are synthetic runners under a disposable in-repo .scratch "
            "directory; no filed runner is executed and no filed byte is written.",
            "The live controls read filed bytes only; they assert the census's "
            "deterministic reading, including the r26 byte fact that disagrees "
            "with the F-C13-1 parenthetical (finding RGA-1-r26).",
        ],
    }
    return receipt


# ----------------------------------------------------------------------- cli


def render_text(report):
    lines = [f"{report['tool']}  mode={report['mode']}  date={report['date']}"]
    if report["mode"] == "runner-census":
        lines.append(f"{'class':<22}{'runner':<46}{'write':<10}guard")
        for row in report["runners"]:
            write_lines = ",".join(':' + str(site["line"]) for site in
                                   (row["receipt_writes"] + row.get("embedded_receipt_writes", [])))
            guard_lines = ",".join(':' + str(call["line"]) for call in row["guard"]["calls"])
            lines.append(f"{row['class']:<22}{row['runner']:<46}"
                         f"{write_lines or '-':<10}{guard_lines or '-'}")
        lines.append("class_counts: " + " ".join(
            f"{name}={count}" for name, count in report["class_counts"].items()))
        lines.append(f"hazard_count: {report['hazard_count']}  "
                     f"census_complete: {report['census_complete']}")
        for finding in report["findings"]:
            lines.append(f"finding {finding['id']}: {finding['detail']}")
    else:
        for row in report["writers"]:
            lines.append(f"{row['kind']:<12}{row['path']}")
            for write in row["receipt_writes"]:
                lines.append(f"    :{write['line']} {write['kind']} -> {write['resolved']}")
        lines.append(f"writers: {len(report['writers'])}  "
                     f"parse_gaps: {len(report['parse_gaps'])}  "
                     f"sweep_complete: {report['sweep_complete']}")
    return "\n".join(lines) + "\n"


def _safe_out(root, candidate):
    path = Path(candidate)
    if path.is_absolute() or ".." in path.parts or ".git" in path.parts:
        raise SystemExit(f"{TOOL}: --out must be a repo-relative path: {candidate}")
    if path.name == RECEIPT_NAME:
        raise SystemExit(f"{TOOL}: refusing to write a receipt path: {candidate}")
    return root / path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true",
                        help="print the census JSON on stdout")
    parser.add_argument("--out", metavar="PATH",
                        help="write the census JSON to a repo-relative path")
    parser.add_argument("--root", type=Path, default=ROOT,
                        help="repository root to census (default: this lane)")
    parser.add_argument("--sweep-repo", action="store_true",
                        help="census every .py under reports/ and tools/ for "
                             "filed-receipt writes, runners and non-runners alike")
    parser.add_argument("--selftest", action="store_true",
                        help="run fixture and live-bytes controls; prints a control receipt")
    args = parser.parse_args(argv)
    if args.selftest:
        if args.json or args.out or args.sweep_repo or args.root != ROOT:
            parser.error("--selftest takes no other arguments")
        receipt = selftest()
        sys.stdout.write(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        return 0 if receipt["selftest_passed"] else 1
    root = args.root.resolve()
    if not root.is_dir():
        print(f"{TOOL}: root is not a directory: {root}", file=sys.stderr)
        return 2
    report = sweep_repo(root) if args.sweep_repo else census(root)
    rendered = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.out:
        destination = _safe_out(root, args.out)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(rendered, encoding="utf-8")
    if args.json:
        sys.stdout.write(rendered)
    else:
        sys.stdout.write(render_text(report))
    complete = report["census_complete"] if not args.sweep_repo else report["sweep_complete"]
    return 0 if complete else 1


if __name__ == "__main__":
    sys.exit(main())
```

## Owed

- **Landing (integrator):** write the fenced bytes above to
  `tools/harness/receipt_guard_adoption.py`, then run
  `python3 -B tools/harness/receipt_guard_adoption.py --selftest` (expect exit 0,
  38/38) and
  `python3 -B tools/harness/receipt_guard_adoption.py --json --out
  reports/round-34/op/receipt-guard-adoption-inventory.json` (expect exit 0).
  Verify the landed file's sha256 against `5858abcd0261e8176ebb285db6d80a7c36185d9a12895b4b43b75710db036544`; if the integrator applies
  any edit, the digests in this fragment no longer describe the landed bytes.
- **Verifier coverage of these bytes (owed, integration-time):** O07 and O08
  filed before this fragment landed and therefore judged O01's scratch core, not
  these bytes (`O07-verify-tool.md` §3.5 states O02's tool never landed). The
  cross-seat reconciliation above is **author-side** evidence: this seat ran its
  own tool over O08's durable trap tree and O03's fixture corpus and against
  O04's predicted inventory. A cleaner close is a verifier seat re-running
  `O07-verify-tool.md`'s mission against the landed bytes; the replay surface is
  `.scratch/o08-traps/` (EXPECTATIONS.json) plus `.scratch/o03-fixtures.py`.
- **Which bytes land:** `op/O07-verify-tool.md` defects D5–D7 (false greens on
  the guard-defined-not-called shape) are open against O01's core; this tool's
  control set reports that shape as `unguarded-in-place`/`guard-referenced-only`
  with named evidence. The integrator owns the choice.
- **Parallel-seat scratch inventories:** sibling scratch artifacts under
  `.scratch/o01/`, `.scratch/o03-fixtures/` and `.scratch/o08-traps/` are live
  or ephemeral, not durable evidence; the census of record is the landed tool's
  `--json` output, and this fragment's observed table is its pinned reading at
  `da68a6d`.
- **Routing consumer:** O05's routing table can be generated from the
  `unguarded-in-place` rows (11 runners) and the `route` field per row; if O05's
  routing was derived from a different census (O04's or O01's), the row sets
  agree per the parity check above — only the class labels differ.

## Citations

- `reports/round-34/targets.json` — seat O02 `mission`/`out`, `shared_rules`
  (boundary, F-C13-1 rule, missing-dependency rule, citation rule).
- `reports/round-34/claims.json` — claim O `after_required` (tool durable,
  selftest green, inventory 100% of runners, routing receipt) and
  `counting_commands` (`--selftest`, `--json`, `reports/round-34/run-validation.py`).
- `REGIMEN.md` — per-round contract, no-forced-pass rule, scope limits.
- `AGENTS.md` — telemetry/evidence discipline, no-fabrication rule.
- `LOG.md:3548-3567` — F-C13-1 incident record: mechanism lines (`:3556-3558`
  r5/r6/r7 runner lines, `:3559-3560` r26 clause), prevention rule.
- `reports/round-33/adj/A12-verify-a04-a06.md:107` — "a guard-adoption gap, not a
  guard-behaviour defect"; `reports/round-33/adj/A15-audit-draft.md:207-218` —
  A03-F1 event record; `SCORECARD.md:595` — standing guard-adoption debt.
- `tools/harness/receipt_guard.py:1-29` (contract: only `REFRESH_RECEIPTS=1`
  permits a committed-receipt overwrite), `:152`,`:161` (entry points),
  `:201-203` (`selftest_receipt` and its `parents[2]` scratch root).
- Filed runners read (read-only) for the census: `reports/round-{5,6,7,8,9,10,11,12,14,…,33}/run-validation.py`;
  key lines: r5`:194`, r6`:336`, r7`:1171`, r8`:1485-1486`, r9`:1909-1910`,
  r10`:1053-1054`, r11`:1738-1740`, r12`:1069-1071`, r19`:5-22`, r21`:20`,`:1115`,
  r26`:1855-1857`,`:1905-1909`, r29`:922`, r32`:1142-1143`, r33`:1470-1471`.
- Commands run (all read-only, from the lane root unless noted):
  `python3 -B .scratch/o02/receipt_guard_adoption.py --selftest` (exit 0, 38/38);
  `python3 -B .scratch/o02/receipt_guard_adoption.py --json` (exit 0);
  `python3 -B .scratch/o02/receipt_guard_adoption.py --sweep-repo --json` (exit 0);
  `python3 -B .scratch/o02/verify_independent.py . .scratch/o02/inventory.json`
  (27/28 identical, r21 over-flag explained);
  `python3 -B <draft> --json --root .scratch/o08-traps/tree` vs
  `.scratch/o08-traps/EXPECTATIONS.json` (9/9 expectations satisfied);
  `runpy` of `.scratch/o03-fixtures.py` with cwd `.scratch/o02/o03fixtmp`
  (private staging) then `python3 -B <draft> --json --root
  <private>/.scratch/o03-fixtures/tree` vs `O03-selftest.md` §2 (11/11 semantic
  match + F10 absent);
  parse of `reports/round-34/op/O04-predicted-inventory.md`'s JSON block vs
  `--json` output (28/28 rows, 0 mismatches);
  `python3 -m py_compile .scratch/o02/receipt_guard_adoption.py`;
  `python3 -B <draft> --json --root <lane>` from `/tmp`;
  `git archive HEAD | tar -x -C .scratch/o02/simlane` then the extracted tool's
  `--selftest`/`--json` in that isolated copy (landing simulation, exit 0 both);
  `ls reports/round-*/run-validation.py | wc -l` = 28;
  `git status --short` (only `?? reports/round-34/`); `git rev-parse HEAD` = `da68a6d…`.
- Draft artifact digests: tool `5858abcd0261e8176ebb285db6d80a7c36185d9a12895b4b43b75710db036544`, inventory `ceeb8d0413e2832a8555e5a9467f016208a477fc708c7f3834bcc429a6bebf04`,
  sweep `dcd172affb61a844dfab26d8763ca03127249252f374c41ad806175303ba6eb2`, selftest `81e129ca26dcf805a3400e68ad593638ba10d5ef50ba1d82b7511032cc96c8ac`, crosscheck `ba985f405e69d127333195b91af6c21d3f6b8ed3a733c4b78e589ddb869b4ff8`
  (all under `.scratch/o02/`, none durable).
