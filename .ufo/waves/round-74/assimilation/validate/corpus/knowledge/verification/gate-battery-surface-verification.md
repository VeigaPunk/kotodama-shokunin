# Gate battery surface — what the isolated battery measures, and what it does not cover

- topic: The verification procedure for reading the **gate battery** (`tools/check-gate-battery.py`) as evidence: it runs the seven legacy gate selftests inside a disposable mirror, measures that the live gates tree is preserved, and validates every committed `expected.json` baseline against its digest pins — but it is not a run of the gates over the lane's artifacts, and it does not cover gates outside its seven-name constant. Covers the exit-code semantics (0/1/2), the mirror/originals measurement, baseline discovery, and the coverage statement a battery reading must carry. Method and lane policy only; canon belongs to lore-shokunin.
- gap filled: `gate-frozen-run-standard.md` states the two-evidences clause and the frozen-run layout, but no entry states what the **battery** actually covers — its isolated-mirror construction, its originals-preserved measurement, its baseline-discovery contract, and the fact that a gate outside its fixed seven-name constant is out of its surface. Absence sweep 2026-10-18: `grep -rln "check-gate-battery\|gate battery\|battery_exit" corpus/knowledge/` → 0 files.
- sources:
  - KTD-GB-S-0001 — `tools/check-gate-battery.py` module docstring and exit-code block: two duties (gate selftests in an isolated mirror; committed-baseline validation), the exit semantics `0` all selftests pass + originals preserved + every baseline pinned + all seven gates covered, `1` a genuine selftest failure, `2` could-not-evaluate (missing file, copy mismatch, live tree changed, launch error, timeout, abnormal exit, or any baseline finding), and the conservative exit-1 rule (an exit-1 child without recognizable failure evidence is read as a crash, exit 2).
  - KTD-GB-S-0002 — measured this round, 2026-10-18, lane root, `export TMPDIR=$PWD/.scratch`: `python3 tools/check-gate-battery.py` → exit 0, `summary {"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}`, `originals {"added": 0, "deleted": 0, "modified": 0, "files_hashed_before": 28, "files_hashed_after": 28, "preserved": true}`, `mirror {"removed": true}`.
  - KTD-GB-S-0003 — `tools/check-gate-battery.py` baseline-check docstring: it discovers every committed `expected.json` under the default roots (`tools/gates/expected/`, `tools/gates/frozen/`, `reports/round-9/baselines/`), verifies every declared input digest against the snapshot bytes inside the baseline, the `gate_sha256` pin against the live gate script, the declared gate against the seven-name constant, and the shape of the `expected` verdict block; a baseline is **never re-executed** here.
  - KTD-GB-S-0004 — `tools/gates/frozen/round-18/README.md` §"Rows": the constraint that a frozen receipt for the D4 family is deliberately **not** named `expected.json`, because `check-gate-battery.py` “discovers every `expected.json` under its baseline roots and fails closed on a gate outside its seven-name constant”. The battery's coverage boundary, stated by the round that hit it.
  - KTD-GB-S-0005 — `corpus/knowledge/verification/gate-frozen-run-standard.md` §1 (which gates owe a frozen run; a probe is never registered), §4 (digest pins), §6 (class mapping: `snapshot_tampered`, `gate_revised`, `unpinned (legacy)`, `pinned`). Supplies the baseline vocabulary the battery deliberately reuses.
  - KTD-GB-S-0006 — `corpus/knowledge/verification/verification-independence-anti-circularity.md` §1 (independence is a property of failure sources) and §4 (control sensitivity: what would make this green red). The reason the battery's originals-preserved measurement and its mirror matter: a selftest that writes into the live tree is a different failure source than one that cannot.
  - KTD-GB-S-0007 — Yue Jia and Mark Harman (2011), “An Analysis and Survey of the Development of Mutation Testing,” *IEEE Transactions on Software Engineering* 37(5): 649–678, [doi:10.1109/TSE.2010.62](https://doi.org/10.1109/TSE.2010.62). A control's worth is whether a planted defect can fail it; cited as a design rule for reading a battery that reports both green selftests and could-not-evaluate rows.
  - KTD-GB-S-0008 — Dijkstra, Edsger W. (1972), “The Humble Programmer,” *Communications of the ACM* 15(10): 859–866, doi:10.1145/355604.361591. A green run shows the presence, never the absence, of defects — the battery's `pass: 7` is bounded evidence.
- calibration: battery reading is this lane's house policy, not a published standard; Jia–Harman (a survey of a contested technique) and Dijkstra are cited as design rules for controls, never as laws; the battery counts are a point-in-time measurement, not a coverage claim about the lane's gates.
- couples: verification — `gate-frozen-run-standard.md`, `verification-independence-anti-circularity.md`, `verification-method-overview.md`, `provenance-audit-ledger-format.md`; synthesis — `../synthesis/generated-artifact-lifecycle.md`, `../synthesis/finding-disposition-workflow.md`; tooling — `tools/check-gate-battery.py`, `tools/replay-frozen.py`, `tools/gates/expected/`, `tools/gates/frozen/`, `tools/gates/*.py`; siblings — lore-shokunin owns canon; chousa-shokunin owns general research method.
- source: the battery tool's own docstring and this round's run of it; the coverage boundary is cited from the round-18 README that hit it. The battery reading rules are this lane's house method, not findings attributed to the cited works.
- verified-at: 2026-10-18 — re-measured at HEAD `169c616`, lane root, `export TMPDIR=$PWD/.scratch`: `python3 tools/check-gate-battery.py` → exit 0, `pass 7 / fail 0 / unevaluable 0`, originals preserved (28 files hashed before and after, 0 modified/added/deleted), mirror removed. Header fields and cross-reference targets checked for resolution; all cited repo paths exist. The battery's own baseline checks are reported as the tool reports them, not re-derived.
- recheck: whenever `tools/check-gate-battery.py`, the seven-name gate constant, a baseline root, or a gate selftest changes; before quoting `pass: 7` as coverage of the lane's gates; and whenever the D4 family is added to the battery's surface (corrections are new entries, never rewrites).

## 1. What this entry licenses

- A **reading of one instrument**, not a verification of the lane's gates. The battery answers two questions: do the seven legacy selftests pass in isolation, and are the committed baselines still pinned? It answers nothing about whether a gate's verdict over a live artifact is correct.
- The battery is a **coverage statement as much as a check**: `pass: 7` names exactly seven gates, and a gate outside that constant is outside the battery's surface by construction.
- A battery green is **lane-local engineering evidence**: these selftests passed in a mirror and these baselines are pinned at this revision — nothing about design quality or canon.

## 2. What the battery measures

| duty | construction | what a green reading asserts | what it does not assert |
|---|---|---|---|
| gate selftests | the seven `tools/gates/*.py` scripts and their fixture tree are copied into a disposable mirror; each child runs `[sys.executable, <resolved gate path>, "--selftest"]` with `shell=False`, never on a live path | all seven `--selftest` runs exit 0, in isolation | that any gate's verdict over a real artifact is correct |
| originals preserved | the live gates tree is snapshotted before and after (per-file sha256 **and** the path set) | 0 modified, 0 added, 0 deleted under the live gates tree | absence of writes — a rewrite with identical bytes passes (the tool says so) |
| baseline validation | every committed `expected.json` under the default roots is discovered and its pins checked: declared input digests vs the snapshot bytes, `gate_sha256` vs the live gate, the gate vs the seven-name constant, the `expected` block's shape | every discovered baseline is `pinned` | that the recorded verdict is *correct* — a baseline is never re-executed here |

Measured (2026-10-18): `pass 7`, `fail 0`, `unevaluable 0`, originals preserved,
mirror removed, exit 0.

## 3. Exit-code semantics — three readings, not two

| exit | reading | what a reader must not do |
|---|---|---|
| 0 | all seven selftests green, tree preserved, every baseline pinned, all seven gates covered | read it as “the gates are verified” or “the lane's gates are all covered” |
| 1 | at least one selftest exited 1 **and** printed recognizable stable failure evidence (`SELFTEST FAIL`, `FAIL <token>`, `failed: <token>`) | treat a bare nonzero as a genuine finding |
| 2 | could-not-evaluate: missing file, copy mismatch, live tree changed, launch error, timeout, abnormal exit, a crash-shaped exit 1, or **any** baseline finding (tamper, revision, unpinned, uncovered gate) | read a tampered baseline as a silent pass |

The exit-1 rule is deliberately conservative: five of the seven legacy gates
assert with bare `assert`, so a genuine selftest failure in those gates is
crash-shaped and classifies as exit 2, not 1. The battery still reports a
nonzero, not-green result either way; it only refuses to vouch for which kind.
A reader that equates “exit 2” with “infrastructure noise” inverts the tool's
design.

## 4. Coverage boundary — the seven-name constant

- The gate list is a **fixed constant** in `tools/check-gate-battery.py`; nothing
  is ever executed from a manifest and no shell string is built.
- Consequence measured by the round-18 D4 work: a frozen receipt for the D4
  family is deliberately **not** named `expected.json`, because the battery
  discovers every `expected.json` under its roots and fails closed on a gate
  outside its seven-name constant (`tools/gates/frozen/round-18/README.md`).
- Therefore a battery green **does not** cover `tools/gates/d4-typed-labels-check-gate.py`
  or `tools/gates/d4-assembly-check-gate.py`. Those legs carry their own evidence
  (a selftest for the typed-labels gate, measured 39/39; frozen rows in
  `tools/gates/frozen/round-18/MANIFEST.tsv`), and the assembly gate's missing
  selftest is an open obligation (`generated-artifact-roundtrip-verification.md` §6).
- A coverage claim must name the constant's contents, not just the pass count.

## 5. Reviewer checklist

1. Record the battery's `summary`, `originals` and `mirror` blocks, not only the exit code.
2. State the seven gates the constant names and check that any gate you care about is among them.
3. Confirm every baseline reading is `pinned`; a `unpinned (legacy)`, `gate_revised` or `snapshot_tampered` reading is a finding, not noise.
4. Do not quote `pass: 7` as coverage of the lane's gates without the §4 boundary statement.
5. Re-run at a named revision; a battery reading without a revision is unreproducible.

## 6. Decision record — the battery-reading rules this entry adopts

1. **Adopted:** the battery is read as a **surface statement** — seven named selftests in isolation plus baseline-pin validation — never as verification of any gate's verdict over a live artifact (§1–§2). Consequence: a battery green cannot be cited as gate coverage.
2. **Adopted:** exit 2 is a could-not-evaluate, not a failure and not noise; a baseline finding forces it (§3). Consequence: a tampered or unpinned baseline is never a silent pass.
3. **Adopted:** the originals-preserved measurement is per-file sha256 **and** path set, and is reported as “no writes with changed bytes”, never as “no writes” (§2). Consequence: the tool's own limitation is carried into the reading.
4. **Adopted:** a coverage claim names the seven-name constant and any gate outside it (§4). Consequence: the D4 legs are reported as outside the battery and must carry their own evidence.
5. **Rejected:** equating `pass: 7` with “all the lane's gates are covered”. Reason: the constant is a boundary by construction, and the round-18 D4 receipt exists precisely because the boundary bit.
6. **Open (to-verify):** whether the D4 family should join the battery's constant, and if so how the constant's growth is itself controlled (a growing constant silently changes what “7/7” means). Owner: this lane's O axis; not disposed here.
