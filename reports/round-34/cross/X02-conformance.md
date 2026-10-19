- Seat: X02 | critic | claim cross | date 2026-10-19 | baseline da68a6d

# X02 — conformance audit: append-only, F-C13-1 prevention, telemetry readiness

**Mission** (`reports/round-34/targets.json`, seat X02): conformance critic —
append-only discipline, F-C13-1 prevention compliance (no in-tree runner
execution anywhere in fragments), telemetry readiness.

**Audit instants:** 2026-10-19T07:06:47Z (first pass: `date -u +%Y-%m-%dT%H:%M:%SZ`),
re-verified 2026-10-19T07:07:30Z after the peer fragments listed below landed.
Repo root, lane HEAD `da68a6d705e41f369f21e8607bfaab5b54077f84`
(`git rev-parse HEAD`), env `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`.

**Method.** Read-only throughout: git state queries, per-file mtime scans, a
static AST/text census of the 28 filed runners, the guard's own CLI controls
(the guard is a tool, not a round runner — permitted), and a text scan of every
fragment that had landed. No `reports/round-*/run-validation.py` was executed,
in-tree or otherwise, by this seat. Durable output is this file only; transient
TMPDIR transients under `.scratch/` (gitignored, `.gitignore:6`) are named in §6.

**Fragments audited.** First pass (07:06–07:07Z): the 5 fragments landed by then
(below), read in full. Second pass (07:12Z): a mechanical re-scan over **all 46
fragments** landed by then (46 of the 63 enumerable seat out-paths; the other 17
are mid-flight — see `## Owed`).

| fragment (first pass) | mtime |
|---|---|
| `reports/round-34/depth/D11-preservation.md` | 04:02 |
| `reports/round-34/calib/C07-verify-survey.md` | 04:06 |
| `reports/round-34/op/O06-scribe.md` | 04:06 |
| `reports/round-34/calib/C02-receipt-json.md` | 04:07 |
| `reports/round-34/calib/C04-byte-check.md` | 04:07 |

---

## 1. Append-only discipline — VERDICT: HOLDS

| check | command | result |
|---|---|---|
| index vs HEAD | `git diff-index --quiet HEAD; echo EXIT=$?` | `EXIT=0` |
| staged rows | `git diff --cached --name-only HEAD \| wc -l` | `0` |
| worktree vs HEAD | `git diff --name-only HEAD \| wc -l` | `0` |
| untracked | `git status --porcelain` | exactly `?? reports/round-34/` |
| filed-round writes after baseline commit | `find reports/round-{5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33} -type f -newermt "2026-10-19 03:52:53" \| wc -l` | `0` |
| aggregate filed-round fingerprint | `git ls-files reports/round-{5,6,7,8..33} \| xargs sha256sum \| LC_ALL=C sort \| sha256sum` | `1713e725abbd3a73b03ff2e42a8774adcd9b8c294c458f25d4657065b126ce71` |

The fingerprint was computed independently by this seat and matches
`reports/round-34/depth/D11-preservation.md` §Evidence E exactly — the D-block's
immutability witness is reproducible by a second seat, not merely asserted. It was
recomputed a second time after the five fragments above landed: identical value.

**Why mtime, not just git.** `.gitignore:3-4` ignore `*.log` and `__pycache__/`, so
filed `…/run.log` files and stale `__pycache__` trees are *invisible* to
`git status`. A write to those would have escaped a git-only check. The mtime scan
covers them: zero filed-round file of any kind has an mtime after the baseline
commit `2026-10-19T03:52:53-03:00` (`git log -1 --format=%cI HEAD`). The one stale
artifact C04 named — `reports/round-24/__pycache__/run-validation.cpython-314.pyc` —
predates the baseline (`2026-10-18 14:05:35 -0300` per C04 §1) and is unchanged.

No fragment records writing a filed path. C04 §5 supplies the sharpest negative
control (a single appended space to a filed row changes its blob hash), which is
what makes the zero-drift result a measurement rather than a default.

## 2. F-C13-1 prevention — VERDICT: HOLDS at the audit instant

### 2.1 Independent 28-runner census (critic-side, read-only)

Static AST/text analysis (`ast.walk` for `guard_receipt` calls and receipt-write
calls, plus `grep -n`); **no runner was executed**. Population: **28 runners**,
rounds 5–12 and 14–33 — there is no `reports/round-13/run-validation.py`
(`ls reports/round-*/run-validation.py | wc -l` → `28`).

| class | count | rounds | evidence shape |
|---|---|---|---|
| adopted (guard call present) | 17 | 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33 | `runpy.run_path(tools/harness/receipt_guard.py)` (r22+) or `importlib` spec load (r14–r20), then `guard_receipt(…)` |
| unguarded (own in-place receipt write, no guard) | 11 | 5, 6, 7, 8, 9, 10, 11, 12, 19, 21, 29 | write sites cited below |

Unguarded write sites (each verified by reading the file):
r5`:194`, r6`:336`, r7`:1171`, r8`:1486`, r9`:1910`, r10`:1054`, r11`:1740`,
r12`:1071`, r19`:21`, r21`:1115`, r29`:922`.
Guard call sites for the adopted set: r14`:420`, r15`:1044`, r16`:1005`,
r17`:1124`, r18`:1518`, r20`:1285`, r22`:911,921`, r23`:1094`, r24`:1181`,
r25`:1142`, r26`:1906`, r27`:1904`, r28`:2095`, r30`:903,922`, r31`:1139,1158`,
r32`:1123,1142`, r33`:1459,1470`.

This census was produced before reading `reports/round-34/op/O06-scribe.md` §2 and
matches it row-for-row (O06: 17 adopted / 11 unguarded, same write sites). Two
independent derivations agreeing is the strongest available check on the inventory
the O block must land.

### 2.2 The absolute rule binds all 28 runners, not only the 11 unguarded ones

`tools/harness/receipt_guard.py:7-8` (docstring): *"Only the exact environment
value REFRESH_RECEIPTS=1 permits a committed receipt write."* So an adopted runner
still rewrites its filed receipt in place when that variable is set — the guard is
an accident brake, not a sandbox (`:13-14`: "Neither form is a sandbox…"). The
round's own no-in-tree-execution rule therefore applies to all 28; the adoption
class only governs *which* protocol is used off-tree (isolated copy vs guarded
refresh). An inventory that phrases adoption as "safe to run in-tree" would
misstate the guard.

### 2.3 Guard rail independently confirmed in-tree (tool CLI, not a runner)

Reproduced O06 §3 controls with my own run, proving the rail is live at these bytes:

```
$ python3 tools/harness/receipt_guard.py reports/round-5/validation.json ; echo EXIT=$?
receipt_guard: refusing overwrite path=reports/round-5/validation.json committed_sha=da68a6d… committed_blob=778c3f5e172405d73eab790b8d6fee4c3282caa0; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]
EXIT=3

$ REFRESH_RECEIPTS=1 python3 tools/harness/receipt_guard.py reports/round-5/validation.json ; echo EXIT=$?
receipt_guard: REFRESH_RECEIPTS=1 permits overwrite … [RECEIPT-GUARD-REFRESH]
EXIT=0

$ sha256sum -c .scratch/x02-before.txt    # reports/round-5/validation.json
reports/round-5/validation.json: OK
$ git status --porcelain reports/round-5/ | wc -l
0
```

`main()` (`tools/harness/receipt_guard.py:354-369`) calls `guard_receipt` and
returns — the CLI has no write path, so a control run cannot mutate a filed
receipt. Confirmed empirically above: digest unchanged, round-5 clean.

### 2.4 Fragment-level scan — no in-tree runner execution recorded anywhere

Every fragment line mentioning `run-validation.py` was classified; the mentions are
exclusively (a) `path:line` citations of filed runners as evidence,
(b) glob/ls listings, (c) `git log`/`git status` arguments, (d) guard-CLI controls,
or (e) explicit declarations that none was executed:

- `reports/round-34/depth/D11-preservation.md:16`, `:339` — "no
  `reports/round-*/run-validation.py` was executed in-tree".
- `reports/round-34/calib/C04-byte-check.md:172` — same declaration plus `:173`
  naming the isolated-copy-only protocol.
- `reports/round-34/calib/C02-receipt-json.md:418-419` — "No in-tree runner
  execution… the only executed artifact is the read-only survey script."
- `reports/round-34/op/O06-scribe.md:166`, `:174` — same, plus the isolated-clone
  precedent `reports/round-21/run-validation.py:474` (`env["REFRESH_RECEIPTS"]=1`
  inside a `.scratch` clone).
- `reports/round-34/calib/C07-verify-survey.md` — executes only
  `reports/round-30/craft/box1-survey.py` (read-only survey) and an independent
  extractor under `.scratch/c07/`.

**Live-process check:** `ps -eo pid,etimes,cmd | grep -E "run-validation|reports/round-[0-9]+"`
at 07:06Z → no matching process. **Verdict: no violation observed.**

**Expanded re-scan at the second audit pass (2026-10-19T07:12Z).** The first pass
covered only the 5 fragments landed at 07:07Z. Re-running the scan over **all 46
landed fragments** (machine scan: 46 `.md` files; 64 lines mentioning
`run-validation.py` in an isolation/declaration context; 10 lines matching a
command shape `(python3|python|bash|sh) … reports/round-N/run-validation.py`):

| file:line | what it is |
|---|---|
| `calib/C09-final-receipt.md:398`, `cross/X01-trades.md:11`, `depth/D12-receipt.md:70`, `:216`, `:289`, `scribe/S02-o-receipt.md:234`, `scribe/S03-c-receipt.md:366` | all seven name **`reports/round-34/run-validation.py`** — this round's own runner, which does not exist yet; D12`:289` records the failed attempt (`file not found, exit 2`). Not a filed runner; nothing executed. |
| `depth/D10-repin-drafts.md:183` | `reports/round-34/handoff/declared-in-r7/` (the new revision path) — not a runner |
| `op/O06-scribe.md:267` | citation list: its own read-only census commands |
| `review/R05-o-review.md:111` | `reports/round-26/run-validation.py:1905-1909` — a `path:line` citation |

Zero lines record in-tree execution of any of the 28 filed runners. A companion
grep for write claims into filed paths (`grep -rn "wrote reports/round-\|edited
reports/round-\|patched reports/round-\|modified filed"` over all 46 fragments)
returns **no hits**. Since the round-34 runner is not yet authored, no seat could
have satisfied a counting command with it either — the three
`python3 reports/round-34/run-validation.py` legs in `claims.json` are unrunnable
by construction until the integrator lands the runner.

### 2.5 Contested filing for the integrator (independent corroboration of O06 §2.3)

`reports/round-34/claims.json` (claim O, "known hazards") and `LOG.md:3559-3560`
group `reports/round-26/run-validation.py` with the r5/r6/r7 hazards. Byte evidence
contradicts the lumping: r26 defines `guard_receipt()` at `:1855-1857` and calls it
at `:1906`, immediately before its write at `:1909`. My census reached this
independently of O06, which reached it as well. The two fields must be recorded
separately: **hazard class** (writes its own receipt in place — true for all 28)
vs **adoption class** (r26 = adopted, r5/r6/r7 = unguarded). I verify O06's
widened census: the unguarded class is **11**, not the 4 named in the claim; an
F-C13-1 routing artifact covering only "the four" leaves eight filed receipts
rewritable. `to-verify`: why `LOG.md:3559` recorded otherwise is not provable from
bytes.

## 3. Telemetry readiness — VERDICT: READY WITH GAPS (2 blockers to reconcile)

### 3.1 Field-by-field against `AGENTS.md`

`reports/round-34/telemetry/dispatch-declared.json` carries owner, self-labelled
pre-dispatch observation, `counting_command` + `counting_date`, `baseline_commit`,
and durable sources with digests. **Both declared digests verify exactly:**

```
f2b87ddb37d8def04c6479a4ac6831ebf5c07514f91efe453247b84a0f9fcff0  reports/round-34/claims.json
76d9652497c9b50ff484238e812c0597195db752786913cb7a6201b4b19eea1d  reports/round-34/targets.json
```

Requested-vs-observed separation is honest: the record declares itself a
declaration and defers launches/completions/failures/concurrency/actual route to a
separate observed record (`"observation"` field), and marks
`closing_snapshot: "open-at-seat-close"` per `AGENTS.md` "Close what you open".
No counter is reported as an inferred zero. Compliant so far.

### 3.2 BLOCKER — the declared seat count exceeds the enumerated seats (64 vs 63)

| source | value |
|---|---|
| `reports/round-34/targets.json:3` `"seat_count": 64` | 64 |
| `reports/round-34/claims.json:13` `"requested_workers": 64` | 64 |
| `python3 -c "json.load(open('reports/round-34/targets.json'))"` → `len(d['seats'])` | **63** |
| unique seat ids / duplicates / id gaps | 63 / none / none |
| id inventory | K1-4, P1-2, X0-4, D1-20, O1-10, C1-9, R1-8, S1-5 |
| `grep -o '"id":' reports/round-34/targets.json \| wc -l` | 63 |
| the declaration's own `seat_composition` string, summed | 4+2+1+16+4+10+9+8+4+5 = **63** |

The file has exactly one seat-bearing key (`"seats"`), so there is no hidden 64th
entry. Precedent: **round 33 declared 64 and contained 64**
(`reports/round-33/targets.json` → `seat_count` 64, `len(seats)` 64), so this is a
round-34-specific discrepancy, not a standing convention.

Conformance consequence: the round's rule is *"Dispatch exactly ONE batched
AgentSwarm per round at the declared size"* (`REGIMEN.md` per-round contract). The
observed record and the closing snapshot must therefore state the breach
explicitly — either naming the missing seat or recording the enumeration as 63 —
rather than reporting `64/64 queued`. Inheriting "64" into `observed_launches`
would overstate the batch on record. Owner: integrator (observed/close records);
the declaration itself is not to be edited in place (`AGENTS.md`: corrections are
new snapshots, never rewrites).

**Convergent finding, not a lone reading.** Two other seats reached the same
measurement independently during this wave:
`reports/round-34/scribe/S05-telemetry-draft.md` §2 (its own census command →
`sum 63`, `seat_count 64 seats 63 ids_unique 63 out_unique 63`, with the same
census over round 33 returning `seat_count 64 seats 64`) and
`reports/round-34/depth/D14-scribe.md:174-177` (same discrepancy, `to-verify`
owner: orchestrator). S05 §1 F3 also reproduces the declaration digest
`53e2bb01…` that §3.4 pins. Three independent derivations of one defect; this
section is the conformance-side framing of it, and §4 item 1 is the routing.

### 3.3 GAP — no availability sample, no `inputs/` snapshot yet

`ls reports/round-34/telemetry/` → only `dispatch-declared.json`. Round 33's
convention (the pattern the closing snapshot must follow) is
`reports/round-33/telemetry/{dispatch-declared.json, observed-dispatch.json,
availability-close-33.json, inputs/{claims.json,targets.json}}` plus
`r25-28-devin-reading-errata.json`. Owed for round 34, post-batch: the observed
record, at least one availability sample, and the redacted inputs snapshot that
makes the declared digests reproducible after scratch cleanup.

### 3.4 Closing-snapshot digest pin (critic-side close-time reference)

`AGENTS.md` requires the closing snapshot to name the record it closes and that
record's SHA-256 at close time. Reference digest measured now, at audit instant
2026-10-19T07:07Z:

```
53e2bb01071a3f97ae015ed7259d6539c5e281fc6a2a2699ff7168d7837dff44  reports/round-34/telemetry/dispatch-declared.json
```

If that value differs at close time, the declaration was edited in place and the
closure is non-conformant. The closing snapshot is additionally gated on
`reports/round-34/validation.json`, which cannot exist until
`reports/round-34/run-validation.py` is authored and run in its isolated copy —
the runner does not exist yet (`ls reports/round-34/` shows no runner), so no seat
can have executed it.

## 4. Conformance items for the integrator (ordered)

1. **Reconcile 64 vs 63** in `observed-dispatch.json` and
   `availability-close-34.json`; name the missing seat or record the enumeration as
   63. Do not inherit 64 (`§3.2`).
2. **File the observed record + availability sample + `inputs/` snapshot** under
   `reports/round-34/telemetry/`, per the round-33 pattern (`§3.3`).
3. **Digest-pin the closing snapshot** to
   `dispatch-declared.json` = `53e2bb01…` (or record a new row if it changed)
   (`§3.4`).
4. **Split hazard class from adoption class** in the O inventory, and correct the
   r26 entry — r26 is *adopted*, contrary to `claims.json` and `LOG.md:3559`
   (`§2.5`). Land the correction as a new `LOG.md` row (O06 §6.2 has a draft); the
   census is 11 unguarded, not 4.
5. **Re-run §5's audit after the last fragment lands**, then again after the
   integrator's shared-file edits (renderer defaults, SCORECARD, LOG, MANIFEST).
   The filed-surface checks (§1) must stay at 0 rows and the fingerprint at
   `1713e725…`.
6. **Do not phrase the adoption instrument as a permission to run filed runners
   in-tree** — the guard permits in-place writes under `REFRESH_RECEIPTS=1`
   (`§2.2`); the absolute rule stands for all 28 runners.

## 5. Re-audit procedure (verbatim, read-only, no runner executed)

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1

# 1. append-only
git diff-index --quiet HEAD; echo "diff-index EXIT=$?"      # expect EXIT=0
git status --porcelain                                       # expect only '?? reports/round-34/'
find reports/round-{5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33} \
  -type f -newermt "$(git log -1 --format=%cI HEAD)" | wc -l   # expect 0
git ls-files $(for i in 5 6 7 $(seq 8 33); do echo reports/round-$i; done) \
  | xargs sha256sum | LC_ALL=C sort | sha256sum                 # expect 1713e725abbd3a73b03ff2e42a8774adcd9b8c294c458f25d4657065b126ce71

# 2. F-C13-1
ps -eo pid,cmd | grep -E "run-validation" | grep -v grep | wc -l   # expect 0
grep -rn "python3 reports/round-[0-9]*/run-validation.py" reports/round-34/  # read-only mentions only

# 3. telemetry
sha256sum reports/round-34/telemetry/dispatch-declared.json   # compare to 53e2bb01…
python3 -c "import json;d=json.load(open('reports/round-34/targets.json'));print(d['seat_count'],len(d['seats']))"
```

**Limit of this audit (stated, not hidden).** The §1 evidence detects any content
change and any write to a filed file, including gitignored ones, and §2.4 detects
recorded executions. It cannot prove the *absence* of an in-tree execution of one
of the 17 adopted runners under `REFRESH_RECEIPTS=1` if that execution's receipt
bytes happened to be reproduced identically — no disk artifact would differ. For
that class the evidence is the fragments' own declarations plus the guard's
refusal path (§2.3). The 11 unguarded runners are fully covered, because any
execution rewrites their receipt and would move its mtime.

## 6. Transient artifacts (declared, no durable value)

TMPDIR scratch files created by this seat, all under the gitignored `.scratch/`:
`.scratch/x02-census.json` (first-pass census), `.scratch/x02-files.txt` (1909-path
listing), `.scratch/x02-before.txt` (digest pre-image for the guard control). No
file outside `.scratch/` and this fragment was written.

## Owed

| owed path / item | owner | why |
|---|---|---|
| `reports/round-34/cross/X00-connector.md` | X00 | not landed at either audit pass — cross-claim consistency is X00's, not audited here |
| 17 unlanded seat fragments (second-pass census) | the seat owners | **X00, D05, D06, D09, D13, D15, D17, D19, D20, O02, O08, R01, R06, R07, R08, X03, S01** — measured by comparing `targets.json` out-paths against `find reports/round-34 -type f`: 46 of 63 landed |
| O-block inventory tool `tools/harness/receipt_guard_adoption.py` | O02/O01 (landed by integrator) | absent at both passes (`ls tools/harness/` → no such file), so §2.1's census stands as the reference inventory the landed tool must reproduce; O01/O03/O04/O05/O07/O09/O10 fragments have since landed and their inventories should be diffed against §2.1 |
| re-scan of the 17 unlanded fragments for §2.4 | integrator (or follow-up critic) | the fragment scan can only cover landed files; run §5's step 2 after the batch closes |
| observed-dispatch + availability-close-34 + `inputs/` snapshot | integrator | §3.3; cannot be produced by a seat mid-batch |
| 64-vs-63 reconciliation | integrator | §3.2; requires the native batch result. Now corroborated by S05 §2 and D14:174-177 — route it as a round-level defect, not a wording nit |
| `LOG.md` errata row (r26 class) + SCORECARD row | integrator | shared bookkeeping is never written by seats (`AGENTS.md`); `scribe/S02-o-receipt.md:252` records S02 accepting §2.5 |

## Citations

- `reports/round-34/targets.json:3` (`seat_count: 64`), `:4` (dispatch rule), `:5-12`
  (shared rules), seat X02 object (mission/out), seat out-path column
- `reports/round-34/claims.json:13` (`requested_workers: 64`), `:41-51` (claim O
  text, before, after_required, counting commands, thresholds), `:54-65` (claim C)
- `reports/round-34/telemetry/dispatch-declared.json` (digests `f2b87ddb…`,
  `76d96524…`, `seat_composition`, `closing_snapshot: open-at-seat-close`)
- `reports/round-33/telemetry/dispatch-declared.json`, `observed-dispatch.json`,
  `availability-close-33.json`, `inputs/claims.json`, `inputs/targets.json`
  (the closing-snapshot convention)
- `reports/round-33/targets.json` (64 declared / 64 enumerated — the comparison case)
- `REGIMEN.md` (per-round contract: one batched AgentSwarm at declared size;
  no fabricated sources; halt rules)
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/AGENTS.md` (append-only, telemetry
  snapshot fields, close-what-you-open, null-not-zero counters)
- `LOG.md:3548-3566` (F-C13-1 incident record; `:3559-3560` the r26 sentence)
- `tools/harness/receipt_guard.py:7-8`, `:13-14` (docstring: REFRESH_RECEIPTS only
  path; not a sandbox), `:152-158` (`guard_receipt`), `:354-369` (`main`, no write)
- `.gitignore:3-4` (`*.log`, `__pycache__/`), `:6` (`.scratch/`)
- Fragment evidence read: `reports/round-34/depth/D11-preservation.md` (Evidence A-F,
  fingerprint `1713e725…`, closing re-check), `reports/round-34/op/O06-scribe.md`
  §2.1/§2.2/§2.3/§3/§6, `reports/round-34/calib/C04-byte-check.md` §1/§5,
  `reports/round-34/calib/C07-verify-survey.md` §1/§3/§5,
  `reports/round-34/calib/C02-receipt-json.md:418-419`
- Per-runner write sites: r5`:194`, r6`:336`, r7`:1171`, r8`:1486`, r9`:1910`,
  r10`:1054`, r11`:1740`, r12`:1071`, r19`:21`, r21`:1115`, r29`:922`; guard call
  sites as listed in §2.1; `reports/round-26/run-validation.py:1855-1857,1906,1909`;
  `reports/round-21/run-validation.py:474,1106` (isolated-clone refresh precedent)
- Commands run (all read-only, at `da68a6d`): `git rev-parse HEAD`;
  `git log -1 --format='%cI' da68a6d`; `git diff-index --quiet HEAD`;
  `git diff --cached --stat`; `git diff --stat da68a6d`; `git status --porcelain`;
  `git status --porcelain --ignored`; `git ls-files 'reports/round-*/validation.json'`
  (27 tracked receipts); `git ls-files <round-5..33>` → 1909 paths; `xargs sha256sum`
  + `LC_ALL=C sort | sha256sum` → `1713e725…` (twice);
  `find reports/round-<5..33> -type f -newermt "2026-10-19 03:52:53"` → 0;
  `find reports/round-34 -type f`;
  `stat -c '%y'` on round-33/round-34 telemetry; `find . -newermt "2026-10-19 03:57"
  -type f` → only round-34 paths; `ps -eo pid,etimes,cmd | grep run-validation` → 0;
  the AST census python heredoc (28 rows, 17 guarded / 11 unguarded);
  `grep -n "receipt_guard\|guard_receipt\|REFRESH_RECEIPTS"` over all 28 runners;
  the per-round `grep -nE "write_text|json.dump"` write-site extraction;
  `python3 tools/harness/receipt_guard.py --selftest`-adjacent controls:
  `python3 tools/harness/receipt_guard.py reports/round-5/validation.json` → exit 3
  `[RECEIPT-GUARD-COMMITTED]`; `REFRESH_RECEIPTS=1 …` → exit 0
  `[RECEIPT-GUARD-REFRESH]`; `sha256sum -c` → `OK`; `git status --porcelain
  reports/round-5/` → 0 rows; `sha256sum reports/round-34/claims.json
  reports/round-34/targets.json` → `f2b87ddb…` / `76d96524…`;
  `sha256sum reports/round-34/telemetry/dispatch-declared.json` → `53e2bb01…`;
  `python3 -c` seat-count enumeration → `64 63`; `grep -o '"id":' | wc -l` → 63;
  `sha256sum reports/round-30/handoff/declared-in-r6/{packet.md,expected.json}` →
  `6ced88ad…` / `ea1e2927…` (freeze.txt agreement spot-check);
  `grep -n "run-validation\.py"` over every landed fragment
