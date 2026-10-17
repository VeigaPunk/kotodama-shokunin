# kotodama — round 11 report (DRAFT BODY — orchestrator finalizes)

> **Scribe X04 draft.** Assembled 2026-10-17 from the fragments landed by
> **22:12Z (19:12 local)** — the wave was still writing when this draft was
> assembled, so every count below carries its source and time, and the
> acceptance numbers are the last receipt's, not a settled tree's. The
> orchestrator finalizes, re-runs the counting command on the settled tree,
> adds the carrying work commit and the admission verdicts, and files this at
> `.ufo/reports/round-11/kotodama.md`. Nothing here is an admission.

Loop 1 of 3, build round 4 of 4 — operator regimen (3 loops × 7 rounds, lane
rounds 8–28). Declared baseline
`94ca098b8ab03be52ec80f6925538e5e2c0ed327` (`reports/round-11/claims.json`);
declaration commit `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7`
("round-11: declare claims D/O/F (typed pipeline, handoff e2e, ledger
recheck)", 18:58:56 −03:00). Cross-revision sweep (scribe, 22:04Z):
`git diff --stat 94ca098..e3ef171` touches only
`reports/round-11/{claims,targets}.json` (111 insertions, 0 deletions); the
committed artifact tree is identical at baseline and declaration.

**Model.** 64 workers requested on `opencode-go-2/deepseek-v4.1-flash`
(`claims.json`); no round-11 availability-attempt record exists at this
refresh (round-10's three 402 records — keys -3/-4/-5 unprovisioned — remain
`reports/round-10/availability-attempt-{1,2,3}.json`; SCORECARD "Planned"
records the rotation as keys 1/2 only).

## Work performed

**Depth (claim D, capability `d2-typed-pipeline`).** Claim D's *before* state
is measured by six independent fragments plus this scribe's own re-run:

- The legacy checked channel pronounces the ten English garment labels:
  `tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml`
  exits 1 with **10 × `PHON-INVENTORY: FAIL`**, exactly `GAR-01`…`GAR-10`
  (`depth/capability-draft.md` §2.1; residual text
  `reports/round-8/depth/skill-table-draft.md:299-303`).
- The typed projection is standalone: `tools/d2-typed-labels.py --json` exits 1
  with `stats {labels: 58, hold: 15, note: 1, fail: 0}` and 16 findings —
  `D2L-FORM-UNRESOLVED` ×10 (`LEX-GAR-01..10`), `D2L-NATIVE` ×2 (`sára`,
  `sará`), `R-RANK-CONFLICT` ×4 (3 hold + 1 note). Scribe re-run 22:09Z
  (`.scratch/x04-typed.json`); worktree status unchanged by the run.
- `tools/d2-typed-labels.py --check` exits 1: the committed projection's
  `assembly.packet_sha256` (`8da90b07…`) no longer matches the committed packet
  (`e0f21509…`) — the round-8 admit commit regenerated the packet without
  re-emitting the artifact; the body differs by that one line
  (`depth/capability-draft.md` §2.3, git table).
- The frozen replay is red on the live tree — `tools/replay-frozen.py
  tools/gates/frozen/round-3/MANIFEST.tsv` exits 2, 7/7 `gate_digest_mismatch`
  (`depth/capability-draft.md` §2.4) — and `depth/frozen-records.md` (D25)
  sweeps every frozen surface: legacy round-3 manifests RED-could-not-evaluate,
  round-4 outputs carry no manifest, the five `r9-pre` baselines and the d3
  guard freeze GREEN-pinned, the typed projection covered by **no** frozen
  surface, `tools/gates/frozen/README.md` index **absent** (standing gap).
  No round-11 re-pin generation existed at 22:02Z.
- Determinism holds pre-wiring: two consecutive D2 assemblies byte-identical
  across an isolated copy, `PYTHONHASHSEED` 0/1/random, `LC_ALL=C`, mtime touch
  (`depth/test-determinism.md`, D11, PASS with the wired-entry caveat).

**The design landed and names the expected hold set.**
`reports/round-11/depth/design.md` (D01–D02, 19:06:11) fixes the contract:
**15 holds** (10 `D2L-FORM-UNRESOLVED` GAR-01..10; 2 `D2L-NATIVE` L-15/L-16;
3 `D2L-RANK` TR-04#a|TR-06#a, WR-02#g|WR-09#g, WR-08#g|WR-09#g) + **1 note**
(`D2L-RANK` SR-01#a|SR-01#b, excluded) + **fail set ∅**; comparison key
`(id, severity, where)` as a set with pinned `detail` strings (§4.2–4.4);
committed baseline to be `examples/culture-d2/expected-holds.json` (§4.5);
the routing adapter is a **new** module `tools/assemble-d2-typed.py` (§2.2) —
so `tools/assemble-d2.py` stays byte-frozen; freeze mechanics §5 (projection
re-pin predicted `a3aa452c…`; new generation `tools/gates/expected/typed-pipeline/r11/`
+ `tools/gates/frozen/round-11/MANIFEST.tsv`; old pins untouched; circularity
guard §5.2). Independent hand derivation by D21 (`depth/review-21.md` §2)
arrives at the same 15 holds + 1 note + 0 fails.

**Reviewers found real gaps the wiring must close** (adversarial, pre-landing):
D02 (`depth/design-review.md`, last written 19:10:52) — nine findings,
high-severity among them: DR-01 a second disjoint hold population (9
nested-only `R-MAT-BRIDGE-MISSING`) that the merged finding list never carries;
DR-02 one document reporting two severity accounts
(`coverage.label_findings_fail: 2` vs `stats.fail: 0`); DR-03 the round-8
spec's hold set is five holds short of live; DR-06 the claim's "exits 0 with
findings exactly equal" contradicts lane exit conventions (producer/judge must
be named); DR-07 the live sound-channel mechanisms are silent, so a wiring can
drop artifacts *and* holds with no finding; DR-09 (out-of-lane) filed artifacts
modified in the worktree (Hazard 1). D21 (`depth/review-21.md`) — F1 the
projector's own selftest does **not** pin the hold set: five one-line mutations
(including one that empties it: M4 → `exit 0, ok: true, hold 0`) all still pass
39/39; F2 the 9 nested holds; F3 `maps_to: null` loads as the string `'null'`,
a 2-element severity divergence (7 holds + 2 notes intended vs 9 holds
computed); F4 counters contradict the finding list; F5 the known stale pin.
The landed design does not name the second (nested) population DR-01/F2
measured — see Open item 3.

Landed depth fragments (all `reports/round-11/depth/`): `scribe.md` (D26),
`review-22.md` (D22 circularity audit: six self-blessing patterns C1–C6 and a
21-artifact pre-change digest table), `capability-draft.md` (D24 row draft +
candidate readings A/B), `test-cli.md` (D14), `test-interop-d3.md` (D15),
`test-determinism.md` (D11), `design.md` (D01–D02), `design-review.md` (D02),
`frozen-records.md` (D25), `neg-18.md` (D18), `neg-17.md` (D17),
`review-21.md` (D21), `review-23.md` (D23), `shard-holds.md`,
`shard-gate-adapter.md`, `test-boundary.md`; D03–D10 scratch activity in
`.scratch/D03`…`d09`. **Not landed by the refresh:** the wired e2e and its JSON
receipt, the D19 negative, capability-row final, and any round-11 manifest —
the design fixes the shape, the implementation lands after this draft's stamp.
`tools/` carried no D wiring at 22:04Z; only `tools/exercise-handoff-e2e.py`
(claim O) is new.

**Operability (claim O, capability `handoff-e2e-exercise`).** The exercise
landed and I verified it myself: `python3 tools/exercise-handoff-e2e.py`
(sha `38d1cba429d98af7…`, 67,252 B, mtime 19:07:36) exits **0** at 22:09Z —
`PASS — fields=16/16 glossary-entries=20 findings=0`, all eleven checks OK
(declared-expectations, frozen-input 5 digests, preflight 16 fields + non-canon
marker + no-floating-version, gate-exit 0 from an isolated foreign cwd,
gate-scan, gate-findings none, frozen-packet sha `2a058f78…`, frozen fields,
frozen glossary, `contract-crossref kotodama-lore-adjacency 1.0.0
sha256:5f4c02bf…`, component-digests 13/13). The frozen baseline
`tools/gates/expected/handoff-exercise/` exists; X02's adjacency census
independently records "the exercise now passes 16/16, 20/20 from a seat run"
and the new packet's `not canonized` discipline. The X03 receipt's O leg
records the plain run as exit 0. **The selftest is broken at this snapshot:**
`--selftest` exits 1 with
`AssertionError: ["evaluated: cannot hash examples/culture-d2/components/02-phonology.yml: [Errno 2] …"]`
— the selftest's own fixture tree omits a component it then hashes (verified by
this scribe at 22:10Z, tool sha unchanged since the runner's read). The
receipt's O failures are: selftest exit 1, traceback, no named positive /
malformed controls, and "output never references handoff-packet-check" (the
exercise's own output names the gate only as "gate-exit/gate-scan").
Fragments landed: `handoff/design.md` (O01, 28,270 B),
`handoff/shard-glossary.md` (O04 fragment, explicitly "lift into
tools/exercise-handoff-e2e.py"), `packet-attempt-1.md`/`.yml` (O06 attempt 1 —
"this envelope exit 0 fields=16/16 glossary-entries=20", prepared-not-accepted),
`packet-attempt-2.md`, `handoff/tamper-control.sh`, and O17 audit scratch
(`.scratch/o17-*.json`: 40 D2 records / 20 D3 entries / 20 glossary rows,
placeholder audit, contract crossref). O16–O18 reviewer fragments had not
landed.

**Freshness (claim F, lowest axis).** At 22:12Z receipt coverage is **complete:
192 receipts, ledger rows 0–191** — **149 stable / 43 unstable = 77.6%**
(scribe count over `reports/round-11/recheck/row-*.json`), far below the
declared ≥95%. The X03 runner's latest receipt (19:09:44 local, runner sha
`97958223cd64…`) measured an earlier snapshot — **117 rows / 93 stable / 24
unstable = 0.795**, threshold 0.95, `passed: False` — and the runner has since
been edited twice (on-disk sha `248bcb31a8a9…` at 19:11:20), so that receipt is
stale relative to the runner. The runner also flags receipt-level defects:
rows 067–069 carry no 64-hex `new_hash` (prose descriptions of multi-command
controls that cannot be re-run 1:1), row-101 self-contradicts (`stable: false`
but `new_hash == prior_hash`), and several drift causes do not use the licensed
class tokens. Cause classes orbit three named heads — **environmental**
(random mkdtemp/mirror tokens, absolute-path resolution, `repo_root` embedding),
**legitimate change** (round-10 admit commit's SKILL.md edit; corpus 179→189),
and **defect** (unreproducible battery stdout; the ledger's own prose rows;
transcription losses). Method per receipt: full-tree mirror (`tar` copy
excluding `.git/.scratch/__pycache__`), hash = sha256(stdout then stderr),
protocol inherited from `reports/round-10/drift/shard-10.md`. This scribe
independently re-ran two receipts (rows 92, 72) and reproduced hash and exit
exactly. `recheck/audit.md` (F11) and `recheck/summary.json` (F12) had **not
landed** (the runner lists both as missing dependencies).

**Scribe/audit (X01–X04).** X02's adjacency/connector fragment landed
(`reports/round-11/adjacency.md`, 20,094 B, 19:11) with four findings: **A**
(six filed receipts rewritten by in-flight recheck runs — mechanism proven to
code: each runner writes its own `OUTPUT_REL` report path, rows **102, 113,
114, 120, 129, 130, 131, 132, 147, 170–173**, attributed to F06/F07 executing
their rows in the live root; recommendation: restore all six paths from
committed blobs and keep the recheck receipts as filed, recording the
side-effect class so "hash-stable" is never read as "tree unchanged"); **B**
(the round-10 fragment appended after filing, +67/−1, mtimes 19:00:36 and
19:01:18, writer active in-lane 19:00–19:01); **C** (PROVINCE mapping holds; no
ownership absorption); **D** (lore boundary clean; the round-8 contract-digest
L0 item remains open). X03's acceptance runner landed and ran:
`reports/round-11/run-validation.py` (19:08:30, edited 19:10:47 and 19:11:20)
→ `reports/round-11/validation.json` (19:09:44 local) with
`acceptance_checks_passed: False`, **25 failures** (D 5 / F 15 / O 5). X01's
lessons fragment had **not landed** anywhere visible at the refresh. X04 is
this draft.

## Landed changes (refresh 22:12Z)

- `reports/round-11/depth/` — 14+ fragments (D01–D02 design, design-review,
  D11, D14, D15, D17, D18, D21, D22, D23, D24, D25, D26, shard-holds,
  shard-gate-adapter, test-boundary).
- `reports/round-11/handoff/` — design.md, shard-glossary.md,
  packet-attempt-1.{md,yml}, packet-attempt-2.md, tamper-control.sh.
- `reports/round-11/recheck/` — 192 row receipts (complete ledger coverage).
- `reports/round-11/adjacency.md` — X02 fragment.
- `reports/round-11/run-validation.py` + `validation.json` — X03 runner and
  receipt.
- `tools/exercise-handoff-e2e.py` — new, untracked (claim O tool).
- `tools/gates/expected/handoff-exercise/` — new frozen baseline for the
  exercise (untracked).
- `reports/round-11/{claims,targets}.json` — declaration (committed).
- No `corpus/` change; `SKILL.md`/`SCORECARD.md` untouched by round 11 at the
  refresh; no sibling-repo writes (fleet root `git status` clean, 22:10Z;
  X02 concurs).

## Before → after measurements

Counting command (declared): `python3 reports/round-11/run-validation.py`;
`python3 tools/assemble-d2.py --check` (claim D leg). Latest receipt
**`reports/round-11/validation.json` (19:09:44 local, runner sha
`97958223cd64…`): `acceptance_checks_passed: False`, 25 failures** (D 5, F 15,
O 5). The runner was edited twice after that receipt, so the next run
supersedes these numbers.

| claim | runner verdict (19:09:44) | before (verified) → after (snapshot) |
|---|---|---|
| D / depth | **passed = false**, 5 failures (`--check` exit 1; selftest controls 0/1; battery default-root exit 2; no e2e JSON receipt; no round-11 manifest) | 10 PHON FAILs + standalone projection + stale pin + red replay → **design + reviewers + tests landed; no wiring, no adapter, no re-pin yet**; green legs unchanged (assembler `--check` exit 0; d3 `--check` exit 0; coupling `--frozen` exit 0/0 findings; selftests 42/42, 39/39, 85/85, 16/16+5/5; three-root battery exit 0 pass 7 fail 0) |
| O / operability | **passed = false**, 5 failures (selftest exit 1 + traceback + no named controls; output never references handoff-packet-check); plain run recorded exit **0** | no e2e exercise → **exercise RUNS CLEAN** (scribe-verified 22:09Z: exit 0, 16/16 fields, 20/20 glossary, gate findings 0, contract crossref, 13/13 digests; frozen baseline present) — **selftest still broken** (fixture missing `02-phonology.yml`) |
| F / freshness | **passed = false**, 15 failures (incl. `stability 0.795 < required 0.95`, non-hash rows 067–069, row-101 self-contradiction, unlicensed-cause rows, audit/summary absent) | 192 un-rechecked rows → **192 receipts, 149 stable / 43 unstable = 77.6%** (scribe count 22:12Z); every unstable row carries a cause, but ≥95% is not met on the complete set |

## Known integration hazards

1. **Filed bytes rewritten in the worktree, by the recheck runs themselves
   (X02 Finding A + six-file list; three reviewers flagged it independently).**
   ` M reports/round-10/coverage/index-update-22.md` (+67/−1 per X02's census,
   mtimes 19:00:36 / 19:01:18 — X02 Finding B) and filed receipts rewritten
   19:01:53–19:03:07: `reports/round-5/validation.json` (−361 lines net: F
   measurement block gone), `reports/round-6/validation.json` (−421),
   `reports/round-7/validation.json`, `reports/round-8/validation.json`,
   `reports/round-9/validation.json`, `reports/round-6/checkpoint-validation.json`
   (dirty earlier in the window, clean again at the scribe's 22:11Z read).
   Mechanism is code-level, not inferred: each `run-validation.py` writes its
   own `OUTPUT_REL` report path, so a 1:1 re-run of those ledger rows
   regenerates a *filed* document while the receipt's measured channel still
   reads stable. X02's recommendation: restore the six paths from committed
   blobs before close, keep the F receipts as filed, and have F12's summary
   record the side-effect class + row list (102, 113, 114, 120, 129, 130, 131,
   132, 147, 170–173). Orchestrator's call.
2. **`tools/assemble-d2.py` is a cross-path chokepoint.** Any byte change to
   it turns `assemble-culture-d3.py --check` red (whole-file
   `serializer_sha256`; probe A). The design routes around it (new adapter
   module), but any late edit to that file requires the full d3 re-pin chain
   (`packet.json` + `expected.json` pins; text digests in `handoff.md`,
   `README.md`, r9-pre manifest) — `depth/test-interop-d3.md` §4.
3. **Claim F's ≥95% clause is failing on the complete set** (77.6% scribe /
   79.5% runner) and structurally cannot pass while rows like the battery,
   `source-audit-inventory` and the prose-control rows are counted as unstable
   — 10 `source-audit-inventory` rows, 16 `run-validation` rows, 14
   `replay-frozen` rows are environment-bound or self-rewriting. The
   orchestrator must decide the counting rule (scope, normalised evidence, or
   documented exception) or admit the claim false as written.
4. **O exercise selftest defect** (fixture omits `02-phonology.yml` before
   hashing it): the exercise's own positive/malformed controls cannot run until
   fixed; the normal run is green, so the failure is in the harness, not the
   pipeline.
5. **Design vs reviewer divergence on the hold population** (DR-01/F2/F3):
   the design's contract covers the top-level findings channel (15+1+0); a
   second computed population (9 nested `R-MAT-BRIDGE-MISSING`, of which 2 may
   belong as notes per round-8's shard receipt) is not named by the design. If
   the wiring carries it, the merged set changes by +9 — that must be a named
   change, never absorbed as "expected all along".
6. **`.scratch/` prune loss** (21:59:52Z) — the round-10 c22 instrument's
   receipts are gone; its filed fragment's §9 re-statement stands (Hazard 1).
7. **`/tmp` inode exhaustion** — environment-level and live; all observers used
   in-lane `.scratch/`.
8. **Battery default-root exit 2** remains the standing state (two gates lack
   default-root baselines); the three-root invocation (frozen + expected +
   round-9 roots) reads exit 0, pass 7, fail 0 — that is the claim-relevant
   reading. The runner's D failure list includes the default-root battery;
   resolve as a counting-rule question, not a regression.

## SHONEN skeleton

- [ ] SKILL.md real decision tables/error patterns/cited sources — no
  round-11 patch landed (typed-label table is round 8's).
- [~] At least one end-to-end domain task executed and logged — the O exercise
  runs clean end-to-end (scribe-verified); the D wiring is not visible yet.
- [~] Instructions executable without oral context — X03's runner exists and
  runs; its receipt currently reads acceptance False.
- [x] No cross-domain bleed — no sibling-repo writes; filed-byte edits are
  in-lane but recorded (Hazard 1, X02 Findings A/B).

## Open items for the orchestrator

1. **This is a mid-wave draft.** Re-assemble the D and F sections from the
   settled fragments — especially the wired e2e receipt, the round-11 manifest,
   the D19 negative, and F11/F12 — and re-run the runner on the settled tree.
2. **All three claims read `passed: false` on the latest receipt.** Do not file
   the round as admitted without a fresh run; the runner itself was edited
   after its receipt.
3. **Decide the F counting rule** (Hazard 3) before F12 writes the summary;
   fix or exempt rows 067–069 and resolve row-101's self-contradiction.
4. **Decide Hazard 1** — X02's recommendation is concrete (restore the six
   paths; record the class; keep receipts as filed).
5. **O selftest repair** (Hazard 4) — until then the exercise's control matrix
   is unproven even though the positive run is green.
6. **Design vs DR-01** (Hazard 5): name whether the nested hold population is
   in scope for "findings exactly equal to the expected hold set".
7. Confirm the D22 circularity review closes with the re-pin not self-blessing
   (old-generation digests unchanged; checker digests unchanged or
   co-change-controlled) and that the freeze record is not authored by the
   step that decides the expectation.

FILES: reports/round-11/report-draft.md
SUMMARY: X04 report scribe — draft body assembled from landed fragments.
