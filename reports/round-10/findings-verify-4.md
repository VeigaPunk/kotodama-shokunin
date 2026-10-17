# R10-O13 — verifier: O08 (idx 6, 14) and O09 (idx 7, 15)

- seat: **R10-O13** (findings verifier #4), round 10 (loop 1 of 3, build round 3 of 4), 2026-10-17
- assignment (verbatim): "FINDINGS R10-O13 (verifier): O08+O09. reports/round-10/findings-verify-4.md."
- write scope: **this file only**. No tracker row, fixer fragment, tool, pin, packet, corpus or SCORECARD byte was written by this seat. Scratch: in-lane `.scratch/r10o13/` (`export TMPDIR=$PWD/.scratch` before every scratch-writing command; `/tmp` never used). No commit made.
- worktree at verification: HEAD `e3a1ec9435787328ac9f828f96cb6390e4916b8f` + untracked `.scratch/`; declared round-10 baseline `9dc18ec1339bffd6f81e74f1a5742464ef578749`. All commands below ran from the lane root on 2026-10-17, verification window 21:26Z–21:39Z (UTC).
- method: read both fixer fragments in full, then **re-ran every control they cite** on the live tree and re-measured every digest/token independently; where the fixer's quoted output and my observed output differ, the difference is reported, not smoothed.
- canon: NON-CANON engineering evidence. Nothing here adjudicates canon, real-world rights, or game mechanics.

## 0. Rows verified, and how the seat→row mapping was established

| fixer | fragment (sha256 at read) | tracker rows verified |
|---|---|---|
| R10-O08 | `reports/round-10/fix-08.md` (`dc5ff728…41b`) | **idx 6** = R9-D09 S2 (green-by-construction surfaces) · **idx 14** = R8-D17 F-D17-2 (vocabulary) |
| R10-O09 | `reports/round-10/fix-09.md` (`bda245f3…217`) | **idx 7** = R9-D09 S3 (superset matcher) · **idx 15** = R8-D17 F-D17-3 (layer reference shape) |

The mapping is not assumed. Both fragments state their assignment verbatim (fix-08.md:5 "tracker
indices 6 and 14"; fix-09.md:4 "tracker indices 7 and 15, and every row beyond 15"), and O09's own
control script states it again (`.scratch/r10o09-superset-census.py:2` — "R10-O09 control for
tracker idx 7"). This matches the formula O11 established for the sibling seats (`O(2+j) → idx j,
j+8`, 0-based; `reports/round-10/findings-verify-2.md` §0): O08 (j=6) → 6, 14; O09 (j=7) → 7, 15.
Tracker read at my close (21:37Z): sha256 `151217d7…b5ff`; non-pending rows
`[0, 1, 3, 5, 6, 8, 9, 11, 13, 14]` — **O08's two rows are written; O09's two rows are not**
(§5.1).

## 1. O08 — idx 6 (R9-D09 S2), claimed `wont-fix` + control: **VERIFIED**

Claim shape: both items of S2 are by-construction properties, not defects; the condition they
impose ("no acceptance summary may cite frozen 5/5 / selftest_passed for the frozen-replay leg")
is verified honored; the proposal manifest was never committed.

| # | O08's claim | my independent re-run (2026-10-17) | verdict |
|---|---|---|---|
| 1 | guard `--selftest` exit 0; `frozen_checks 5/5`; 32/32 result rows | `python3 tools/check-evidence-coupling.py --selftest` → exit 0; `selftest_passed: true`; positives 5/5, domain 16/16, malformed 4/4, frozen 5/5; 32 result rows, all passed | match |
| 2 | pre-re-pin freeze stays red under a green selftest | `git show 9dc18ec^:examples/culture-d3/expected.json` → sha256 `74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080` (= S1's pre-refresh token); `--frozen` against it → **exit 2**, counts `{"D3-SNAPSHOT": 3, "total": 3}` | match |
| 3 | current committed freeze green through its own channel | `--frozen examples/culture-d3/expected.json` → exit 0, `counts {"total": 0}`, `findings: []` | match |
| 4 | (a) is by design: the selftest builds its frozen cases from live bytes | code read `tools/check-evidence-coupling.py:1866-1900` — `good_manifest` = selftest packet digest + live component digests at run time, written to tmp, then one digest flipped for `frozen-tampered-digest`; the committed `expected.json` is never in the read-set | match |
| 5 | condition honored in the acceptance chain | `reports/round-9/validation.json` `claims.D.measurement.frozen_replay` = argv `[… --frozen …]`, exit 0, `drift_paths: []`, `finding_ids: []`; `SCORECARD.md:142` evidence command is `python3 reports/round-9/run-validation.py`; `reports/round-9/d3/capability-draft.md:64` cites "frozen 5/5" inside the selftest breakdown with the re-pin + replay cited separately — O08's nuance is accurate | match |
| 6 | (b) proposal never committed | `grep -rn '70affb9d' reports/ tools/` (non-scratch) → 0 hits; `ls tools/gates/frozen/` → `round-3`, `round-4`, per-gate baselines only — no D3 projection manifest; the conditional ("if the orchestrator commits…") does not fire | match |

**Disposition judgment.** `wont-fix` with a documented reason is the correct shape for a
by-construction surface: the control battery (runs 1+2) demonstrates the exact independence the
finding demanded — a green selftest coexisting with a red frozen surface — and run 3 shows the
committed leg's evidence is the `--frozen` run itself. No defect remains to fix; the condition is
kept in the tracker record as a standing constraint. Row 6 field check: `wont-fix` matches the
runner's `DOCUMENTED_LABELS`, `reason` 1132 chars, `control` present.

## 2. O08 — idx 14 (R8-D17 F-D17-2), claimed `fixed-with-control`: **VERIFIED**

Claim shape: the vocabulary divergence (spec `supplied | to-verify | absent` + `D2L-*` hold ids
vs the old `declared`/`unresolved` + `TL-01`) was closed by the round-8 rewrite; the fix is in the
**admitted** bytes, not only the worktree.

| # | O08's claim | my independent re-run | verdict |
|---|---|---|---|
| 1 | `--selftest` 39/39 exit 0 | `python3 tools/d2-typed-labels.py --selftest` → exit 0, "39/39 checks passed" | match |
| 2 | status vocabulary `supplied 48 / to-verify 18 / confirmed 4`; zero `declared`/`unresolved`; zero `TL-01`; `D2L-FORM-UNRESOLVED` ×20; `D2L-` ×37 | my own `re` counts over the committed artifact: `{"supplied": 48, "to-verify": 18, "confirmed": 4}`, `"declared"` 0, `"unresolved"` 0, `TL-01` 0, `D2L-FORM-UNRESOLVED` 20, `grep -c 'D2L-'` 37 | match |
| 3 | the GAR-01..10 case carries the spec's code | `--json` report holds `D2L-FORM-UNRESOLVED` on `LEX-GAR-01..10` (`design-spec.md:236` expects exactly `D2L-FORM-UNRESOLVED` HOLD ×10) | match |
| 4 | fresh emit vs committed artifact differ only in `packet_sha256` | `python3 tools/d2-typed-labels.py --emit .scratch/r10o13-emit.yml` → exit 1 (holds present); `diff` vs artifact = **exactly one line** (`packet_sha256` e0f21509… vs 8da90b07…) | match |
| 5 | fix is in admitted bytes | `git show e1694ba:tools/d2-typed-labels.py` sha256 = `0da0015f…c802` = live tool; `git show e1694ba:examples/culture-d2/typed-labels.d2.yml` sha256 = `e70ba147…380b2f` = live artifact; the tool value also equals `reports/round-8/validation.json`'s measurement | match |

Grounding: `design-spec.md:116` (`status: supplied # supplied | to-verify | absent`), `:236`
(GAR-01..10 → `to-verify`, `D2L-FORM-UNRESOLVED` HOLD ×10). The `confirmed` ×4 are the
era-mapping rows (`design-spec.md:264-268`, `confirmed | to-verify`), not label statuses —
O08's reading is correct.

**Adjacent known red, independently confirmed as pre-existing (not this row, not a round-10
regression):** `tools/d2-typed-labels.py --check` exits 1 on one stale provenance line
(`packet_sha256: 8da90b07…` while the live packet hashes `e0f21509…`). At the admission commit
`e1694ba` the artifact already embedded `8da90b07…` while `packet.d2.yml` already hashed
`e0f21509…` — i.e. the staleness exists at admission itself (documented: `reports/round-9/d3/interop.md:137`, fix-08.md §2.2). Verified, left standing.

## 3. O09 — idx 7 (R9-D09 S3), claimed `wont-fix` + control: **VERIFIED (with one quote discrepancy)**

Claim shape: superset semantics of the control matcher confirmed by a count-aware re-drive of all
16 domain controls through the shipped CLI; the guard is not the fixer's write scope; the source's
recommendation (b) — record subset semantics as the accepted standard — adopted with the census as
the standing exactness check.

| # | O09's claim | my independent re-run | verdict |
|---|---|---|---|
| 1 | filed census harness sha256 `d6fdb84…d55` | `sha256sum .scratch/r10o09-superset-census.py` → `d6fdb84fcfa34c0eb616de35440c10b17aa6a4c87377a7e268552dd3ff5ded55` | match |
| 2 | re-drive: 16 controls; 5 differ; 1 extra distinct id (`D3-BRIDGE`), 4 multiplicity-only | my run of the filed harness (set semantics): **15 exact, 1 superset** (`domain-D3-REFERENCE-bridge-target-unknown-record` → extras `D3-BRIDGE`), 0 missing; my independent multiset census: `REFERENCE 1→{REFERENCE 1, BRIDGE 1}`, `NATIVE 1→3`, `DERIVATION 1→2`, `OBJECT 1→2`, `ERA 1→2` — exactly R9-D09's §3 table and O09's refinement | match |
| 3 | the census can fail: bogus expectations flagged 16/16 | filed harness self-test → "bogus expectations flagged = 16/16" | match |
| 4 | subset semantics in `run_case`; controls.json untouched | code read `tools/check-evidence-coupling.py:1677,1703-1705` (fail only on `missing`); `controls.json` sha256 `f00ccf7a…ae70` = its own `expected.json` manifest entry (editing it would have broken the re-pinned freeze) | match |

**Quote discrepancy (evidence hygiene, substance unaffected).** fix-09.md §2's quoted output block
("multiset-exact=11 multiset-differing=5", dict-form lines) is **not the output of the filed
harness**, which uses set semantics and prints tuple lines ending "superset=1". The multiset
numbers come from an unfiled variant. I reproduced the multiset substance independently (row 2
above), so the disposition stands; a re-runner must not expect the filed script to print the quoted
block verbatim.

**Disposition judgment.** `wont-fix` is correct: the matcher lives in a file outside the fixer's
write scope, the acceptance legs do not rely on exact verdicts (the frozen leg compares declared
digests and `finding_ids: []`), and the source's own alternative remedy (b) is adopted with a
failing-capable census attached. Residual (stated by O09, confirmed by me): an over-firing guard
regression would keep the selftest green and be visible only in the census.

## 4. O09 — idx 15 (R8-D17 F-D17-3), claimed `fixed-with-control`: **VERIFIED**

Claim shape: the current tool emits `borrow.layer_ref` and resolves it against the packet's
declared layers with a fail path; the stage-derived inline `donor_layer` is gone; two mutation
controls fire `D2L-BORROW`.

| # | O09's claim | my independent re-run | verdict |
|---|---|---|---|
| 1 | `layer_ref` built and resolved against packet layers, with fail path | code read `tools/d2-typed-labels.py:569` (`"layer_ref": layer_name`), `:701-704` (`layers.get(layer_ref)`, fail path "does not resolve to a declared layer"); `grep -c donor_layer` tool → **0** | match |
| 2 | artifact carries the resolved reference on `kas` | artifact `typed-labels.d2.yml:2409` `"layer_ref": "Salt-road trade layer"`; L-26 borrow block carries `"donor_form": "gas"`, `"substitutions": {bh:p, dh:t, sh:s, g:k}`, `"text": "kas"`; `donor_layer` 0 in artifact; packet declares the layer at `packet.d2.yml:2539-2552` | match |
| 3 | control 1: rename the layer in a scratch copy → `D2L-BORROW` fail | my scratch copy `.scratch/r10o13/mut-layer.yml` (layers[0].name renamed once) → `--packet … --json` exit 1, `D2L-BORROW` "layer_ref 'Salt-road trade layer' does not resolve to a declared layer", where `L-26`, severity `fail` | match |
| 4 | control 2: declare `g: "t"` instead of `g: "k"` → derivation check fails | `.scratch/r10o13/mut-subs.yml` → exit 1, `D2L-BORROW` "substitutions derive 'tas' from donor 'gas', not 'kas'", where `L-26` | match |
| 5 | unmutated packet emits no `D2L-BORROW` | `--json` → exit 1, `Counter({'D2L-FORM-UNRESOLVED': 10, 'D2L-RANK': 4, 'D2L-NATIVE': 2})`, zero `D2L-BORROW` | match (see naming note) |

**Naming note (substance unaffected).** O09's quoted unmutated counter says `R-RANK-CONFLICT` ×4;
the live emitted id is `D2L-RANK` (`R-RANK-CONFLICT` is the internal name, aliased to `D2L-RANK`
at `tools/d2-typed-labels.py:2253`; the four rank findings carry details `act-collision` ×2 and
`R-05-class` ×2). The count (4) and the no-BORROW conclusion are correct.

**Disposition judgment.** `fixed-with-control` verified: both spec §1.4 B1 requirements (field name
`layer_ref`; resolution against a declared packet `layers` block) now exist and fail closed, and
both controls demonstrably fire. Corroboration only, not a disposition of another row: the same
artifact block (`donor_form` + `substitutions` + the derivation control) is evidence toward
F-D17-1 (idx 8, another fixer's row).

## 5. Cross-cutting observations (reported, not absorbed)

### 5.1 Tracker integration state

- O08's rows 6 and 14 are written into `findings-tracker.json` (read-time sha `151217d7…b5ff`)
  and satisfy the runner's field rules when I re-applied them inline (`run-validation.py:753-800`):
  idx 6 = `wont-fix` + `reason` 1132 chars + `control`; idx 14 = `fixed-with-control` + `control`
  text containing `python3` / `39/39`.
- **O09's rows 7 and 15 are not in the tracker** — fix-09.md §7 carries ready-to-paste rows
  (O09's stated write scope excluded the shared tracker). The dispositions and controls themselves
  are verified above; only the write is outstanding for the scribe (R10-O14 / X04).
- Integration hazard found by simulation, not by running the runner (which writes X03's
  `validation.json`): of §7's proposed rows, idx 7's `control` string passes the runner's
  evidence rule (via the `16/16` token), but **idx 15's and idx 18-23's `control` strings
  ("reports/round-10/fix-09.md §3 …", "…§6.x") do not** — the path-with-suffix does not resolve
  and no `python3 | exit N | sha256 | \d+/\d+` token is present, so `fixed_without_control` would
  flag them (`run-validation.py:764-779`, simulated over the literal strings). The integrator
  should use the bare path or include a matching token. Reported, not absorbed.

### 5.2 No-regression sweep (my runs, 21:33–21:39Z)

| check | result |
|---|---|
| `tools/d2-typed-labels.py --selftest` | exit 0, 39/39 |
| `tools/assemble-d2.py --check` | exit 0, byte-identical |
| `tools/assemble-culture-d3.py --check` | exit 0, byte-identical |
| `tools/check-evidence-coupling.py --selftest` | exit 0, 32/32 rows |
| `tools/check-evidence-coupling.py --frozen examples/culture-d3/expected.json` | exit 0, `findings: []` |
| `tools/d2-typed-labels.py --check` | exit 1 — **pre-existing at `e1694ba`** (§2); documented, not a regression |
| `tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` | exit 2, 7 × could-not-evaluate (`gate_digest_mismatch`) — the documented residual of tracker idx 0/1 (other fixers' rows), unchanged by O08/O09 |

## 6. Limits

- I verified only O08's and O09's rows (idx 6, 7, 14, 15) plus the specific claims and byproducts
  cited above. §7's rows 16-23 were not verified here (integration-compliance spot-check only).
- The fixes behind idx 14 and idx 15 landed in round 8; this verification checks the *delivered
  revision* and the *dispositions*, not the intermediate rewrite history (`623b5b1f → e9209f28`),
  which is cited from filed round-8 receipts.
- Verdicts are pinned to these hashes (my reads): tool `0da0015f…`, artifact `e70ba147…`, packet
  `e0f21509…`, `expected.json` `562b76cb…`, `controls.json` `f00ccf7a…`, guard `849494b0…`, census
  script `d6fdb84…`. A later edit to any cited file invalidates the corresponding row and requires
  a re-run.
- The tracker is a shared surface written concurrently by other seats; my read-time sha is a
  snapshot, and the pending/non-pending list may have moved after 21:37Z.
- Out of province and not assessed: any canon decision, real-world rights, or game mechanics.

## 7. Reproduction

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
# idx 6 — selftest vs frozen independence
python3 tools/check-evidence-coupling.py --selftest                       # exit 0, 32/32
git show 9dc18ec^:examples/culture-d3/expected.json > .scratch/r10o13/pre-repin.json
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
        --frozen .scratch/r10o13/pre-repin.json                           # exit 2, 3×D3-SNAPSHOT
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
        --frozen examples/culture-d3/expected.json                        # exit 0, []
# idx 14 — vocabulary on the admitted bytes
python3 tools/d2-typed-labels.py --selftest                               # 39/39
python3 tools/d2-typed-labels.py --emit .scratch/r10o13/emit.yml          # exit 1 (holds)
diff .scratch/r10o13/emit.yml examples/culture-d2/typed-labels.d2.yml     # one line: packet_sha256
git show e1694ba:tools/d2-typed-labels.py | sha256sum                     # 0da0015f…
git show e1694ba:examples/culture-d2/typed-labels.d2.yml | sha256sum      # e70ba147…
# idx 7 — count-aware census (my copy of O09's harness, ROOT-patched, under .scratch/r10o13/)
python3 .scratch/r10o13/census.py                                         # 15 exact, 1 superset, 0 missing; self-test 16/16
# idx 15 — layer_ref mutation controls
python3 - <<'PY'
s = open("examples/culture-d2/packet.d2.yml").read()
open(".scratch/r10o13/mut-layer.yml","w").write(s.replace('name: "Salt-road trade layer"','name: "Salt-road trade layer (renamed)"',1))
open(".scratch/r10o13/mut-subs.yml","w").write(s.replace('g: "k"','g: "t"',1))
PY
python3 tools/d2-typed-labels.py --packet .scratch/r10o13/mut-layer.yml --json   # D2L-BORROW, where L-26
python3 tools/d2-typed-labels.py --packet .scratch/r10o13/mut-subs.yml  --json   # D2L-BORROW "…derive 'tas'…not 'kas'"
```

FILES: reports/round-10/findings-verify-4.md | SUMMARY: Verifier R10-O13 re-ran every control in fix-08.md and fix-09.md — all four dispositions **verified**: idx 6 (R9-S2) `wont-fix` reason validated (selftest builds its frozen cases from live bytes; pre-re-pin freeze 74496aa8 stays red 3×D3-SNAPSHOT under a green selftest; proposal manifest never committed; condition honored by the `--frozen` evidence channel) and idx 14 (F-D17-2) `fixed-with-control` reproduced (admitted tool 0da0015f / artifact e70ba147; vocabulary supplied 48 / to-verify 18, zero declared/TL-01, D2L-FORM-UNRESOLVED ×20); idx 7 (R9-S3) `wont-fix` + census reproduced (15 exact / 1 superset extra D3-BRIDGE / 0 missing; multiset deltas NATIVE×3, DERIVATION×2, OBJECT×2, ERA×2; self-test 16/16) and idx 15 (F-D17-3) `fixed-with-control` reproduced (both mutation controls fire D2L-BORROW at L-26; donor_layer gone) — with two reported items: O09's tracker rows 7/15 are still unwritten (ready-to-paste §7; §7's control strings for idx 15/18-23 would fail the runner's evidence rule as written) and two minor quote discrepancies (unfiled multiset census variant; R-RANK-CONFLICT vs emitted D2L-RANK); no previously green check regresses.
