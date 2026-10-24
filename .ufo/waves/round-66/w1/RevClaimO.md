# RevClaimO — round 66, attack seat: claim O's boundedness premise

Scope attacked: `reports/round-66/claims.json` (O statement + `separability` block),
`reports/round-66/accept-o.py`, `tools/check-claim-separability.py` (dynamic leg, budget,
clone), and the round-66 receipts in `reports/round-66/telemetry/`.
Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base
`94209e8f80969dbac48d56c5d0e2e623635b8616`. Byte state at probe time:
`accept-o.py` sha256 `f08ff6e8…6199` (11766 B, mtime 08:35:36), tool sha256
`5c728e96…4d98`, `dry-run-o.txt` (08:26:04) stamps counter sha `681743e3…9d409`.
No tool installs were needed. Probes wrote only to `/tmp`; nothing in the lane was mutated.

## Answers to the two posed questions

**Does `--budget` cover the git_free materialization + clone time, or only the subprocess timeout?**
Neither, precisely. The deadline is armed before materialization (`_Budget` constructed at
`tools/check-claim-separability.py:762`, `_materialize` called at `:776`), so the *clock* does include
base materialization — but the deadline is only ever **read** in `take()` (`:695-710`), i.e. immediately
before a run starts. There is no enforcement during `_materialize` (`:553-559`), during the per-run
`shutil.copytree` in `_counterfactual` (`:585`), or during the per-run `git clone`/`checkout` in
`_git_counterfactual` (`:612-614`, through `_git_run` `:595-605`, which passes **no `timeout`**).
`--timeout` wraps only the acceptance child (`_run_acceptance` `:561-577`). The leg's wall bound is
therefore `budget + (copy + clone + timeout)` per in-flight task — and unbounded when a git call hangs.
Measured (probes below): a 5 s stall in `git clone` under `--budget 2` produced a **complete, non-partial
verdict at 10.06 s**; a 30 s stall never returned and had to be killed at 8 s. The budget also never
reports an overrun when `skipped == 0`: `report()` prints `SEPARABILITY_PARTIAL` only for
`skipped > 0 or unresolved` (`:830-833`).

**Can a needs_git clone still stall?** Yes, indefinitely. `_git_run` has no timeout and `--budget` cannot
interrupt a started run. This is the exact defect class R65-D4 routed (no verdict inside the round) moved
from the acceptance subprocess to the clone.

## Findings by severity

### HIGH-1 — the frozen O counter does not compile at the lane tip; its receipt is stale
`reports/round-66/accept-o.py:117` is `legs = []")"]")` followed by a duplicated block — unterminated
splice from a concurrent edit. Evidence:
```
$ python3 -c "import py_compile; py_compile.compile('reports/round-66/accept-o.py', doraise=True)"
SyntaxError: unmatched ']'   (line 117)
$ sha256sum reports/round-66/accept-o.py
f08ff6e8…760199   (mtime 2026-10-24 08:35:36)
```
`telemetry/dry-run-o.txt` stamps `681743e3…709d409` and `FIXTURES PASS … wall=6.3s` from 08:26:04, i.e.
bytes that no longer exist. Consequence: `ACCEPT-O-66: every leg … PASS` is **unevaluable from the current
lane bytes**, and any statement citing `dry-run-o.txt` as the counter's pre-data behaviour is unsupported.
The tool itself is intact (`--selftest` → 63/63, 4.3 s, sha `5c728e96…`), so the break is the counter only.
Fix: repair the splice, re-run, and pin the new counter **and tool** sha256 in the same receipt.

### HIGH-2 — the dynamic leg is not wall-bounded: budget is a start-gate and overruns are silent
Three probes against the unmodified tool (`--lane` on a throwaway git lane):

| probe | manifest | flags | observed |
|---|---|---|---|
| A | 1 git-free unit, acceptance `sleep 5` | `--budget 4 --timeout 10 --jobs 4` | `SEPARABILITY: 0 findings`, `acceptance_runs=1 skipped=0`, **rc=0, no `SEPARABILITY_PARTIAL`**, wall **5.05 s** |
| B | 1 needs_git unit, `git` shimmed to sleep 5 s on `clone` | `--budget 2 --timeout 2 --jobs 4` | rc=0, `skipped=0`, no PARTIAL, wall **10.06 s** (clone 5 s + checkout 5 s, both untimed) |
| C | same, shim sleeps 30 s | `--budget 2 --timeout 2`, outer `timeout 8` | killed at **8.00 s, rc=124** — the tool never returned |

So `claims.json`'s "`--budget` bounds the whole dynamic leg" is false as written; the tool's own docstring
is honest ("a run not yet started when the budget is exhausted is SKIPPED", `:43`). Note the shim matches
the clone *destination* path (`/tmp/claim-separability-clone-*`) too, which is how probe B got two sleeps —
that is itself evidence that both git calls in `_git_counterfactual` are outside every timeout.
Steady-state cost is small, so this is a stall/contention risk, not a routine one: base tree is 6098 files
/ 131,526,547 B; `git clone --shared --no-checkout` 0.01 s, `checkout --detach base` 0.46 s (141 MB, 6124
files) on this host, warm.
Fix (any one): give `_git_run`/copytree a deadline derived from the remaining budget; print
`SEPARABILITY_OVERRUN wall=… budget=…` when `skipped == 0` but wall > budget; or weaken the claim statement
to the start-gate semantics it actually implements.

### HIGH-3 — O is `needs_git: false` but its counter requires git; it can never pass `base+O.lands`
`accept-o.py`'s DIFF leg runs `git -C <root> diff BASE -- tools/check-claim-separability.py`. The git-free
counterfactual is `_materialize` + `shutil.copytree` (`:553-590`) — **no `.git`**, and the MUT leg needs
`.ufo/waves/round-66/stage/mut-o/*.py` under `--root .`, which a file-land overlay cannot create (see
HIGH-4). Reproduced on a real base-bytes tree with current-disk O lands copied in:
```
has .git: False
mut dir present: False
git -C . diff 94209e8f… -- tools/check-claim-separability.py
  -> rc=1  "error: Could not access '94209e8f…'"
```
Every run fails, no sibling overlay supplies a repo, so `_acceptance_findings` emits
`SEPARABILITY_DEPENDENCY O-><base> … and no declared unit's lands repairs it` (`:735-738`) — a class
`claims.json` explicitly declares a real defect. Minimal repair that also fixes HIGH-4: set
`O.needs_git: true` **and** list the four mutant files (not the directory) as lands; then the clone is a
repo at base and MUT's inputs exist. Add a `needs_git` boundedness leg (HIGH-2 probe B/C shape) — the O
predicate has none, so the mechanism its own `check` command will rely on is untested.

### HIGH-4 — the frozen manifest is not loadable as written
Two independent input errors, both exit 2 before any leg:
- `separability.manifest_units` is the wrong top-level key: `_parse_manifest` requires `claims`
  (`MANIFEST_KEYS`), so transcribing the block literally gives `SEPARABILITY_INPUT_ERROR manifest is
  missing claims`.
- `O.lands` (in the claims block **and** in `manifest_units`) contains
  `.ufo/waves/round-66/stage/mut-o/`; land paths must be canonical files. Reproduced on a synthetic lane:
  `SEPARABILITY_INPUT_ERROR claims[0].lands[0] is not canonical (empty, '.' or '..' component): 'sub/'`.
So the frozen `separability.check` command has no valid input until the manifest is rewritten; the
`expected_findings` list (only `Ca->REC`) is also incomplete against HIGH-3.

### MED-1 — O's declared internal bound (180 s) exceeds the separator's per-run cap (120 s)
`accept-o.py`'s FIXTURES leg passes iff total wall `< 180` s; the frozen `check` command uses
`--timeout 120`, and `_run_acceptance` scores a timeout as a failure (`:567`) → false
`O-><base>/O->…` dependency. Any run in the 120–180 s window is a PASS for the counter and a FAIL for the
separator. Measured today (6.3 s receipt, 4.3 s selftest) this is latent, not live.
Related structural cost: the git-free phase is fully joined (`_run_unit_tasks` at `:784`) **before** the
git phase starts (`:796`), so `--jobs 4` never overlaps O with C/Ca; wall = O_leg + max(C leg, Ca leg), and
a slow O leg spends the shared 300 s budget before C and Ca start, turning them into
`SEPARABILITY_UNRESOLVED`. Round-66's allocation is exactly one git-free unit (O) plus two needs_git units
(C, Ca), and no predicate leg exercises that shape.

### MED-2 — the JOBS leg is vacuous
`accept-o.py` lane 2 declares `S` **without** acceptance, so only one dynamic unit exists; `--jobs 1` and
`--jobs 4` cannot differ, and `_run_unit_tasks` bypasses the pool entirely for `len(tasks) == 1`
(`:811-812`). The tool's selftest "bound: `--jobs` leaves the verdict unchanged" scenario has the same
shape (S has no acceptance). Neither control exercises two concurrent dynamic runs — the mechanism the
claim advertises. Recommend a two-acceptance-unit fixture (they are cheap) with a shared append-only
ordering assertion.

### MED-3 — MUT's input sits outside the land set the separator can materialize
`accept-o.py` requires exactly the four pinned mutant names and marks any other `.py` as `unpinned`; the
directory currently holds exactly those four plus `__pycache__/`. Because O lands a *directory* the
separator rejects (HIGH-4), MUT cannot run in a counterfactual at all; and once individual files are
landed, a stray `.py` from any seat flips MUT to FAIL. Land the four files and treat extras as a churn
finding, not a test result.

### LOW-1 — exit 2 is shared by honest PARTIAL and unusable input
`EXIT_INPUT = 2` is returned for `InputError`, `Unevaluated`, and for any partial verdict (`report`
`:836-838`, `main` `:1428-1440`). A caller of the frozen check command cannot separate "bounded out of
budget" from "manifest is wrong" by exit status; only the stdout marker distinguishes them. Since Ca D4's
leg demands a *complete* verdict with no partial (`dry-run-ca.txt`: `D4 FAIL complete verdict + run count,
no partial`), the D4 receipt is contingent on the whole dynamic leg finishing inside 300 s — including the
serialized O phase above. A distinct exit code for PARTIAL would make the class machine-checkable.

### LOW-2 — receipt chain does not pin the tool bytes
`controls-o.txt` pins the base tool sha `5764ea2…`, `dry-run-o.txt` pins only the counter sha; no round-66
receipt pins the tool sha the selftest ran against (today `5c728e96…`). With the counter and tool both being
edited during the wave (HIGH-1), the final receipt should cite `counter_sha256=` and `tool_sha256=` in the
same block.

## Residual risk
- Probe B/C use a PATH-shimmed `git` to simulate a stall; they prove the absence of a timeout, not a
  measured FS hang. Warm-cache costs here are sub-second (131 MB / 6098 files), so cold-cache or
  `--jobs 4` contention inflation is unmeasured.
- No LFS smudge path at base (0 `.gitattributes` files in `git ls-tree -r base`), although the lane's git
  config carries `filter.lfs.*`; a future LFS-tracked land would make `checkout` network-dependent inside
  an untimed `_git_run`.
- `accept-o.py` was mid-edit during this seat; the SyntaxError is a snapshot (08:35:36) and may be
  transient churn, but the receipt/bytes mismatch is not.

## Verification gaps (what I ran / did not run)
Ran: `--selftest` on current tool bytes (63/63, 4.3 s); probes A/B/C above; synthetic-lane canonical-land
probe (exit 2); git-free base+O.lands tree (no `.git`, no mut dir, DIFF rc=1); clone/checkout timings and
base tree census; `py_compile` on the counter (SyntaxError); read of `_Budget`, `_evaluate`, `_run_tasks`,
`report`, `_git_run`, `_git_counterfactual`, `_counterfactual`, `_load_units`.
Did not run: the frozen check command end-to-end with the three real counters (C and Ca lands absent at
probe time; the O counter does not compile); any measurement with three concurrent dynamic units; a real
(non-shimmed) clone stall. `lsp` is not exposed in this seat's toolset (only `ast_edit`/`debug` devices), so
caller/definition checks above are code-path reads with exact line citations, not grep-as-proof.
