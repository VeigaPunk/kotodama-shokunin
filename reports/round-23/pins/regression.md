# R23-O11..O12 — regression sweep (initial + closing)

**Operational regression verdict: GREEN post-pins.** Battery, craft, every runnable typed/assembly selftest and production check, the d2/d4 gates, handoff v2/v3, and the projector suites all pass after the round-23 successor pins landed, and the new `round-23/repin-d2` frozen generation replays 11/11. The only nonzero matrix legs are four historical frozen-manifest controls and one historical-evidence leg (`tie-break --check`), both documented below and never rewritten. This is a regression measurement, not round acceptance, canon clearance, or a claim that historical manifests exit zero.

## Isolation, revision and evidence

- Observation date: **2026-10-18**. Times are **UTC−03:00**; each table row's time is its command start, not a claimed completion time.
- Before scratch-writing commands: `export TMPDIR=$PWD/.scratch; export PYTHONDONTWRITEBYTECODE=1` from the lane root.
- Driver: `python3 .scratch/r23-o11-o12-regression/sweep.py <phase>`. Each phase creates a real Git clone under `.scratch/r23-o11-o12-regression/<phase>/repo`, overlays the measured live working-tree bytes plus manifest-referenced ignored receipts, and runs the whole matrix inside the clone with per-command TMPDIR roots. Every result row records argv, dated start/end, exit, and stream SHA-256. No round validator was executed by this seat, in the live lane or otherwise.
- Binding: lane `HEAD=7b181a52eb74319e5e5c40cdb1f0a1a1dc652079` (round-23 declare commit); declared baseline `0e81d9d99514631d6717e1ff354d5a5a759aa980` (`reports/round-23/claims.json:5`). The report measures the uncommitted integration overlay, not an assertion that HEAD contains it.
- Raw evidence: `.scratch/r23-o11-o12-regression/{initial,closing}/{snapshot,source-manifest,results}.json` and per-command `*.stdout.txt` / `*.stderr.txt`. The filed evidence is this report alone; no shared bookkeeping or source file is this seat's write.

## Initial sweep (R23-O11) — pre-pin binding

- `python3 .scratch/r23-o11-o12-regression/sweep.py initial`, clone/snapshot started **12:10:38**, matrix completed **12:11:16**. Snapshot: **1,902** inputs, manifest SHA-256 `8ee31cc086c23e6c47990a3973ec85b25028c3a1cbe50e877c9734bedfe28b22`, `source_drift_after_copy: []`.
- Matrix: **40** commands, **36** exit-zero, **4** nonzero — all four historical frozen-manifest controls (below). Battery: 7/7 structural selftests, fail 0 / unevaluable 0, **19/19** baselines pinned; `--selftest` **35/35**. Craft: **10/10** tamper + **18/18** CLI; full check audits 7 / mechanical 11 / derivations 9 / approx-runner 37; census 7 = 5 supported / 2 unresolved / 0 contradicted. Assembly selftests d2 **42/42**, d2-typed **11/11**, d3 **85/85**, d4 **81/81**, d4-typed **12/12**; all production `--check` outputs byte-identical. Projector `--selftest` **163/163** (d4 label gate delegates the same suite); typed-pipeline **12/12**, generalized **14/14**; D2 gate **16/16** legs, D4 gate **19/19** legs. Handoff v2: claims 15, links **50/50**, drift named (round-16 rows only); v3 selftest exit 0; v3: fields **16/16**, glossary **20/20**, findings 0, links **105/105**, claims 27, statuses 16/7/4, packet sha `a97a0f0a…`. Harness: coupling selftest + D3 check zero findings; packet_links **38**; packet_uncertainty **19**; replay-frozen selftest **79/79**. Prior successors reproduced: round-18/repin-d2 11/11, round-20/repin-d2 11/11, round-22/d4-repin 3/3.
- Wording tail pre-disposition (12:19:28, against the initial clone): `python3 reports/round-22/fixes/tie-break.py --root .scratch/r23-o11-o12-regression/initial/repo --selftest` → exit 0, **23/23** controls; full `--check` → exit **1** on the documented `PLACEHOLDER_RE` false positive — the round-22 open tail, exactly as routed, not a new regression.
- Preservation: `clone_copied_paths_changed: []`, `source_changes_since_snapshot: []`, **1,271** locked historical paths with `locked_paths_changed: []` (12:11:16).

## Closing sweep (R23-O12) — post-pin

- Pin settle: the round-23 wave landed continuously (frozen/round-23 at **12:16:17**; the six `reports/round-23/pins/*.md` rows at **12:23:41**; wording revision + validator evidence by **12:28:36**; `run-validation.py` still being edited by its owner at **12:30:04**). A 60 s settle watcher reached its 15-minute bound without two quiet polls; the closing sweep proceeded at **12:30:59** because every pin-relevant surface was stable and the drift instrumentation can see any under-matrix movement. Pre-snapshot digest check (12:30:4x): the six watched tool/pins sources (`typed-pipelines.json`, `exercise-handoff-e2e.py`, `d2-typed-labels.py`, both typed assemblers, `typed-pipeline-gate.py`) are byte-identical to the initial sweep.
- `python3 .scratch/r23-o11-o12-regression/sweep.py closing`, clone/snapshot started **12:30:59**, matrix completed **12:31:45**. Snapshot: **1,951** inputs, manifest SHA-256 `22e85aefc12142c661e00d7ad2ae6d7a17ff70820897b4d78349042ef19ea57f`, `source_drift_after_copy: []`.
- Matrix: **45** commands, **38** exit-zero, **7** nonzero — four historical frozen controls, one historical-evidence leg, and two wording-leg invocation refusals superseded by corrected green runs (below).

### Current commands — all exit 0 (12:31:00–12:31:02)

| Group | Measured result (command + date: driver above, 2026-10-18) |
|---|---|
| Battery | 7/7 structural selftests, fail 0 / unevaluable 0, **19/19** baselines pinned; `--selftest` **35/35** |
| Craft | **10/10** + **18/18** selftests; full check 7 audits / 11 mech / 9 derivations / 37 approx; census unchanged (5/2/0, 6+1 blocked) |
| Assembly | d2 **42/42**, d2-typed **11/11**, d3 **85/85**, d4 **81/81**, d4-typed **12/12**; all seven production `--check` outputs byte-identical |
| Projector / d4 gate | `--selftest` **163/163** (both entries); D2/D4 `--check` byte-identical; typed-pipeline **12/12**, generalized **14/14**; D2 **16/16** legs; D4 **19/19** legs; d4 assembly gate byte-identical |
| Handoff | v2 exit 0, claims 15, links **50/50**, named drift only; v3 selftest exit 0; v3 exit 0, fields **16/16**, glossary **20/20**, findings 0, links **105/105**, v2 subset equal, packet sha `a97a0f0a…` (same bytes as pre-pin) |
| Harness | coupling selftest + D3 packet zero findings; packet_links **38**; packet_uncertainty **19**; replay-frozen selftest **79/79** |
| Selector control | `tie-break.py --root . --selftest` exit 0, **23/23** controls (12:31:02) |

### New round-23 successor pins — replayed green

`python3 tools/replay-frozen.py tools/gates/frozen/round-23/repin-d2/MANIFEST.tsv --json` (2026-10-18, 12:31:02): exit 0, **11/11** recorded verdicts reproduced, zero mismatch / could-not-evaluate. Manifest SHA-256 `8f8184665102561e5962ae65de1685f56e3af2148e649b5eb0015cc4dece9002`. The earlier generations still reproduce on the same run: round-18/repin-d2 **11/11**, round-20/repin-d2 **11/11**, round-22/d4-repin **3/3**.

### Wording tail (R23-O01..O04 closure) — green with a documented driver correction

- Driver wiring error, preserved: the two in-matrix legs `wording-check.py --root . --selftest|--check` exited **2** at 12:31:02 with `--root must be an isolated clone with .git under the lane's .scratch` — the validator correctly refuses a self-referential root (same isolation discipline as the round-22 nested-clone replays). Captured as `.scratch/r23-o11-o12-regression/closing/wording-{selftest,check}.*` matrix receipts; not counted as passes.
- Corrected runs with the owner's own invocation pattern (runner = live-lane bytes, root = closing clone), 2026-10-18:
  - `python3 reports/round-23/wording/wording-check.py --root .scratch/r23-o11-o12-regression/closing/repo --selftest` (**12:32:54**) → exit 0, **28/28** controls: the frozen `PLACEHOLDER_RE` is byte-identical and still flags standalone `unchanged` and the old D4-CL08 basis, while the reworded r3 basis is clean — no placeholder alternative weakened. Revision pin `084dc5db9a8d923bb06a987b0b437bf5bfee3caac2e41cd16743da0c71499250`.
  - `python3 reports/round-23/wording/wording-check.py --root .scratch/r23-o11-o12-regression/closing/repo --check` (**12:34:19**) → exit 0, **17/17** controls, `wording_tail_eliminated: true`: the full historical check runs green against the reworded `declared-in-r3` revision (`expected.json` sha `737e54842fffa68d07f2e05370e5618a85fd50e4d9be639429ea14a0e75f01ff`).
- Historical evidence stays historical: `tie-break.py --root . --check` in the closing clone exits **1** (12:31:02) on the frozen round-20 packet's D4-CL08 placeholder reading plus the stale round-20 v2 row (`V2F-DIGEST: tools/d2-typed-labels.py`), with `filed_rounds_8_21_changes: []`. The filed round-20 validator is not claimed to pass; the r3 revision supersedes only the successor-facing reading.

### Historical negative controls — explicitly nonzero, never rewritten

All nonzero frozen replays (`python3 tools/replay-frozen.py <manifest> --json`, 2026-10-18, 12:31:02): `round-11` exit 2 (10/11, obsolete gate pin refuses pre-launch), `round-18` exit 1 (1/2, replay_mismatch on the superseded D4 projection), `round-3` and `round-3/attempt-1` exit 2 (0/7 each, obsolete gate pins). These four account for every remaining nonzero; nothing current failed.

## Before/after controls and preservation

- **Before (12:10:38) → after (12:30:59):** every current-command result identical (same selftest counts, same leg counts, same byte-identity verdicts, same handoff packet sha `a97a0f0a…`); the only matrix delta is the added round-23 manifest (green) and the wording legs (green after correction). The pins landed without regressing any measured command. One pinned D2 input changed between the sweeps by the pin owners: `examples/culture-d2/expected-holds.json` gained a `supersedes_pins` key at **12:14:41** (counts unchanged 15 hold / 1 note / 0 fail); the initial sweep measured the pre-change bytes green and the closing sweep the post-change bytes green, so the update is itself covered by the matrix.
- Closing preservation: `clone_copied_paths_changed: []`; **1,271** locked historical paths (rounds 8–22 reports + pre-round-23 frozen generations) with `locked_paths_changed: []` (12:31:45); live-vs-snapshot drift is exactly `reports/round-23/run-validation.py` — the validator owner's concurrent edit, a file this seat never executes.
- Post-run clone re-verification (12:35:13): recomputing all **1,951** copied digests in the closing clone gives **zero** drift after the matrix and the corrected wording runs.
- Protected-baseline inventory (12:15:54, `git ls-tree -rz 0e81d9d99514631d6717e1ff354d5a5a759aa980 -- reports/round-{8..22} tools/gates/frozen/round-{3..22}` + per-path Git-blob recomputation): **1,201**/1,201 compared, **1** differs — `reports/round-22/fixes/regression.md`, the uncommitted round-22 closing edit already present at seat start (first `git status`, before any sweep). No seat wrote to it; nothing added, nothing missing.
- No filed round-8–22 artifact, old frozen manifest, shared LOG/SCORECARD/SKILL, or source tool was edited by this seat. No commit or push. This seat's only filed write is this report.

## Limits

- Regression reproduction is not round acceptance: the closing matrix proves the delivered pins/validator bytes behave as recorded on the measured working tree at `HEAD=7b181a5…`; it does not adjudicate the O/D claims (that is `python3 reports/round-23/run-validation.py`, run by the parent in an isolated clone).
- The two wording legs were corrected out-of-matrix after a driver mis-wiring; both mis-invocations and corrections are preserved with digests above, so the green wording result can be audited end-to-end.
- `run-validation.py` changed once during the closing matrix (outside the matrix's executed set); if the final validator differs again, the parent's counting run re-binds it — this report's green set does not depend on that file.
- The historical nonzero manifests remain historical evidence; "all current commands green" is a statement about the live tree and the round-8–22 successor generations, not about rounds 3/11/18.
