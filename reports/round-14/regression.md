# Round 14 R01–R02 — regression verification

**Axis:** O / operability; controls also cover evidence integrity and reproducibility.
**Result:** **PASS for the assigned regression suite at the recorded tree state.** All thirteen final commands exited 0. This is regression evidence, not an independent round-admission verdict or verification of the other round-14 assignments.

## Run boundary and capture method

- Working directory for every command: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- Actual checkout: `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff` (`git rev-parse HEAD`, captured immediately before the final batch at `2026-10-17T23:59:57.069778+00:00`). The declared round-14 baseline in `claims.json` remains `926c86f8be3cc9307f8f10dce55768c290b6f94d`; these are distinct revision channels, not interchangeable labels. The final battery run includes the round-14 working-tree root fix, pinned below.
- Before scratch-capable commands: `export TMPDIR=$PWD/.scratch; export PYTHONDONTWRITEBYTECODE=1; mkdir -p "$TMPDIR"`. Fixtures and raw stream captures remained inside this lane's ignored `.scratch/` tree. No generated live packet was regenerated; only `--check`, read-only positive calls, and isolated selftests ran.
- Final batch interval: `2026-10-17T23:59:57.069778+00:00` through `2026-10-17T23:59:58.190219+00:00`. The independent commands were launched in parallel using `ThreadPoolExecutor(max_workers=13)`; each child used `subprocess.run(argv, cwd=root, capture_output=True, timeout=240)` with byte capture, not text normalization.
- Exact hashes below are `hashlib.sha256(proc.stdout).hexdigest()` and `hashlib.sha256(proc.stderr).hexdigest()` over the complete captured streams. Dates, labels, exits, and wrapper diagnostics were not mixed into those streams. All final stderr streams are empty (0 bytes), SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Raw captures and execution metadata are retained locally at `.scratch/r14-r01-r02-regression-8awlbqnr/`, with final stream names `final-<command-id>.stdout` / `.stderr` and `final-receipt.json`. This ignored scratch directory is supporting local capture, not a filed historical receipt. The durable assigned deliverable is this report.
- Battery JSON contains per-child durations and a disposable mirror path; its exact stream hash identifies this observation, not a promise that another run will print identical JSON. The typed-label `--check` stream includes the absolute projection path. Generated-artifact hashes are listed separately from command-output hashes.

## Before/after battery-root control

1. **Observed before-fix failure:** `python3 tools/check-gate-battery.py`, `2026-10-17T23:58:05.154406+00:00`–`2026-10-17T23:58:05.547627+00:00`, exited **2**. All seven gate selftests passed, but only five baselines were pinned and the uncovered gates were `myth-consistency-gate.py` and `naming-collision-gate.py`. The two findings were `BASELINE-GATE-UNCOVERED` (`.scratch/r14-r01-r02-regression-8awlbqnr/battery-default.stdout`, JSON `baselines.findings`). Exact stdout: 15,203 bytes, SHA-256 `0bcd93af02642d39eaab737868b2ee72a5ab4d33d186518bcd7e837da07c4c2e`; stderr empty. The original battery code hash was `0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1`.
2. **Diagnostic positive, not a substituted acceptance run:** `python3 tools/check-gate-battery.py --baselines-root /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/gates/expected --baselines-root /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/gates/frozen --baselines-root /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-9/baselines`, `2026-10-17T23:58:29.582964+00:00`–`2026-10-17T23:58:29.951980+00:00`, exited **0**: seven gate selftests passed; eight baselines pinned; no uncovered gate. Exact stdout: 17,368 bytes, SHA-256 `e229e08b3acbc008a2961aa846afa503be1e5ede55223d259f21c0afef06518a`; stderr empty. This establishes that the preserved baselines were available, not that the original default discovery was complete.
3. **Retained fail-closed negative after the root fix:** `python3 tools/check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen`, `2026-10-17T23:58:56.517303+00:00`–`2026-10-17T23:58:56.885227+00:00`, deliberately excluded the legacy root and still exited **2**, with exactly myth/naming uncovered and five baselines pinned. Exact stdout: 15,107 bytes, SHA-256 `8e9bc5f083d60e5fa563df0ee98bf4f7e4f92a4d132eb192a696e7dd902cac08`; stderr empty. Assertions checked the expected exit, the exact uncovered-gate list, and `originals.preserved == true`. Thus the integration did not weaken uncovered-gate rejection.
4. **Bounded dependency polling:** the default command was polled at 60-second intervals, capped at twenty attempts. The first poll, `2026-10-17T23:59:29.581110+00:00`–`2026-10-17T23:59:29.950738+00:00`, exited **0**, with the battery source SHA-256 `7aa898d627fe361517d2942a0fe2b337f15d8cdc1fcb4061b394eee60f03d574` identical before/after. Exact stdout: 17,368 bytes, SHA-256 `dc1caa6b67923613c545d36a933527749de34dd99d5b4b0be55dd4a51c5a2be8`; stderr empty. The poll stopped successfully; no background dependency task remains running.
5. **Full after-control:** the entire suite below was rerun after that green poll. The new default-root selftest emits `control CTRL-BASELINE-DEFAULT-ROOTS: exit=0 outcome=pinned ids=-` (`final-battery-selftest.stdout`), and the actual no-override battery exits 0. The root fix itself was another assignment's working-tree change; this regression worker did not edit the implementation.

## Final command results and exact stdout hashes

Every item below carries its own command and UTC start timestamp on **2026-10-17**. All exits are **0**, with the empty stderr digest declared above. Quoted result text comes from the named final stdout capture.

1. **`battery-selftest`** — `python3 tools/check-gate-battery.py --selftest`
   Started `2026-10-17T23:59:57.071008+00:00`; finished `2026-10-17T23:59:58.176399+00:00`.
   Result: `SELFTEST OK 29/29 controls behaved as expected` (`final-battery-selftest.stdout`). Includes default-root discovery, uncovered/missing/malformed/tampered baseline controls, child crash-versus-finding classification, and live-tree path/hash-difference controls.
   stdout: **2,366 bytes**, SHA-256 `2812a3270ce97583eaa9a7a16f78f95c60e703b00076fd2fc95f0802783442c2`.

2. **`battery-default`** — `python3 tools/check-gate-battery.py`
   Started `2026-10-17T23:59:57.071216+00:00`; finished `2026-10-17T23:59:57.462041+00:00`.
   Result: seven gate selftests passed, zero failed/unevaluable; eight baselines pinned; `gates_uncovered: []`; baseline findings empty. The default roots contain two expected-root baselines, three frozen-root baselines, and three preserved round-9-root baselines (`final-battery-default.stdout`, JSON `summary`, `baselines.summary`, `baselines.roots`). Original gate scripts/fixtures: 28 files before and after, zero added/deleted/modified, `preserved: true` (JSON `originals`).
   stdout: **17,368 bytes**, SHA-256 `081da02d276d573aa9f8e147df1a5716da1855a24c5f73bb1ee95dd8095ff9d9`.

3. **`craft-selftest`** — `python3 tools/check-craft-exercise.py --selftest`
   Started `2026-10-17T23:59:57.071386+00:00`; finished `2026-10-17T23:59:57.526055+00:00`.
   Result: `SELFTEST OK 10/10 tamper cases detected` and `CLI-SELFTEST OK 18/18 cases passed` (`final-craft-selftest.stdout`). Controls exercise real positive, domain-finding, malformed/usage, wrong-shape, conflicting-mode, and foreign-working-directory CLI calls.
   stdout: **75 bytes**, SHA-256 `77d408e10a494fa58fcaa5872d7ad20b6daaa9c5725329d1a0ae65ab8f0e7d32`.

4. **`craft-positive`** — `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json`
   Started `2026-10-17T23:59:57.071513+00:00`; finished `2026-10-17T23:59:57.096178+00:00`.
   Result: `OK all checks passed (audits=7, mech_cases=11, derivations=9, approx_checks_runner=37)` (`final-craft-positive.stdout`). The runner labels 37 approximate; it is not an independently exact check denominator.
   stdout: **87 bytes**, SHA-256 `18128adfc703fd268ec70684f35a2a05b3257faf4b31add8f21b3313ad4a2650`.

5. **`craft-report-positive`** — `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json --report reports/supplement-opencode-1/32-craft-exercise.md`
   Started `2026-10-17T23:59:57.071853+00:00`; finished `2026-10-17T23:59:57.101336+00:00`.
   Result: the same clean seven-audit, eleven-mechanism-case, nine-derivation call, additionally checking the committed report headings (`final-craft-report-positive.stdout`).
   stdout: **87 bytes**, SHA-256 `18128adfc703fd268ec70684f35a2a05b3257faf4b31add8f21b3313ad4a2650`.

6. **`d2-typed-labels-selftest`** — `python3 tools/d2-typed-labels.py --selftest`
   Started `2026-10-17T23:59:57.072199+00:00`; finished `2026-10-17T23:59:57.626468+00:00`.
   Result: `selftest: 39/39 checks passed` (`final-d2-typed-labels-selftest.stdout:40`). Real emit/check/tamper calls run in a disposable mirror, including byte drift exit 1, restored output exit 0, malformed packet exit 2, typed native-versus-translated handling, and held unresolved mappings/forms.
   stdout: **2,354 bytes**, SHA-256 `7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252`.

7. **`d2-typed-labels-check`** — `python3 tools/d2-typed-labels.py --check`
   Started `2026-10-17T23:59:57.072289+00:00`; finished `2026-10-17T23:59:57.143094+00:00`.
   Result: the committed `typed-labels.d2.yml` is a `byte-identical deterministic projection` (`final-d2-typed-labels-check.stdout:1`). This is byte identity, not clearance of the projection's HOLD/domain findings.
   stdout: **129 bytes**, SHA-256 `17064af53c48304def6b2a5f5c80c10161182b5715678a61d6d5b0d80e1ef427`.

8. **`assemble-d2-selftest`** — `python3 tools/assemble-d2.py --selftest`
   Started `2026-10-17T23:59:57.072414+00:00`; finished `2026-10-17T23:59:57.610280+00:00`.
   Result: `selftest: 42/42 checks passed` (`final-assemble-d2-selftest.stdout:1`), covering real fixture CLI assembly/check, deterministic bytes, tamper/restore, missing/malformed/incomplete/duplicate-ID/duplicate-key/empty/wrong-wrapper cases.
   stdout: **225 bytes**, SHA-256 `a81294c0347660d9b46952146bac967fc80c79c9d629d7f34e69d0411bec0336`.

9. **`assemble-d2-check`** — `python3 tools/assemble-d2.py --check`
   Started `2026-10-17T23:59:57.072485+00:00`; finished `2026-10-17T23:59:57.126292+00:00`.
   Result: `packet.d2.yml: byte-identical deterministic assembly` (`final-assemble-d2-check.stdout:1`).
   stdout: **53 bytes**, SHA-256 `2fa0c8c197459f549de2f0822b8895477e27dcce38def75e18346ba6d672e386`.

10. **`assemble-d3-selftest`** — `python3 tools/assemble-culture-d3.py --selftest`
    Started `2026-10-17T23:59:57.072790+00:00`; finished `2026-10-17T23:59:57.740429+00:00`.
    Result: `selftest: 85/85 checks passed` (`final-assemble-d3-selftest.stdout:1`). The real naming gate retained `CROSS-HOLD` without native phonotactic/derivation FAIL; the real costume gate retained the `R-01` violation note without `R-02`. Fixture assembly/check/determinism/tamper and missing/invalid/type/key/collision/minimum/serializer controls all passed. Expected underlying gate exit 1 is preserved, not represented as cultural clearance.
    stdout: **402 bytes**, SHA-256 `91a0653948d48a10f6bd84af7adb3dd4cda3b25e8a15a77a3bf2cd92a4deac2b`.

11. **`assemble-d3-check`** — `python3 tools/assemble-culture-d3.py --check`
    Started `2026-10-17T23:59:57.072942+00:00`; finished `2026-10-17T23:59:57.109028+00:00`.
    Result: both `packet.json` and `packet.gates.yml` are `byte-identical deterministic assembly` (`final-assemble-d3-check.stdout:1`).
    stdout: **108 bytes**, SHA-256 `e20620fabdf285323c021ae11cad32b1ece58a28d59dd74f7df237578ffb560a`.

12. **`evidence-coupling-selftest`** — `python3 tools/check-evidence-coupling.py --selftest`
    Started `2026-10-17T23:59:57.072849+00:00`; finished `2026-10-17T23:59:57.976090+00:00`.
    Result: `selftest_passed: true`, no missing inputs, no failed results; five positive, sixteen domain, four malformed, five frozen-snapshot controls passed. The JSON `results` additionally records two usage controls: **32 executed results**, all passed (`final-evidence-coupling-selftest.stdout`, `results` and per-kind counters). This is not merely the thirty entries in the four named counter families.
    stdout: **5,541 bytes**, SHA-256 `cf62bc50e303b793b6b930c83a5ddd7d462c39cc39fef133385db830c1d380ce`.

13. **`evidence-coupling-positive`** — `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json`
    Started `2026-10-17T23:59:57.073078+00:00`; finished `2026-10-17T23:59:57.101469+00:00`.
    Result: actual committed D3 packet evaluated with JSON `exit: 0`, `findings: []`, `counts.total: 0` (`final-evidence-coupling-positive.stdout`).
    stdout: **116 bytes**, SHA-256 `e282a0688498034144fb376ab43884c8607133bd6deaab763150d789b113669d`.

## Source and generated-artifact pins

For the final batch dated `2026-10-17T23:59:57.069778+00:00`–`2026-10-17T23:59:58.190219+00:00`, source hashes were measured with `hashlib.sha256((root / argv[1]).read_bytes()).hexdigest()` immediately before and after every command. All pairs matched. These pins distinguish the actual working-tree tool bytes from the declared baseline revision:

```text
7aa898d627fe361517d2942a0fe2b337f15d8cdc1fcb4061b394eee60f03d574  tools/check-gate-battery.py
b5b890b4b9c9953be5ed5f5453a2b60bc9c856616b0a5b28cb2b5bca6ffdf7b5  tools/check-craft-exercise.py
0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802  tools/d2-typed-labels.py
8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d  tools/assemble-d2.py
ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014  tools/assemble-culture-d3.py
849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e  tools/check-evidence-coupling.py
```

Generated-file SHA-256 values were measured in both initial/final input snapshots using `hashlib.sha256(path.read_bytes()).hexdigest()`, on `2026-10-17`; all four were unchanged. The actual `--check` calls above verify their expected assembly/projection bytes, not only their existence:

```text
e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643  examples/culture-d2/packet.d2.yml
a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43  examples/culture-d2/typed-labels.d2.yml
bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829  examples/culture-d3/packet.json
306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425  examples/culture-d3/packet.gates.yml
```

## Historical-receipt preservation control

No `reports/round-{8,9,10,11,12}/run-validation.py` was invoked. The historical receipt-writer root cause is not tested by rerunning those unsafe writers in the live lane. Receipt-guard implementation/selftest and round-14 admission validation are separate assignments.

Before and after the final batch (`2026-10-17T23:59:57.069778+00:00`–`2026-10-17T23:59:58.190219+00:00`), enumerated tracked historical paths with:

```sh
git ls-files -z -- reports/round-8 reports/round-9 reports/round-10 reports/round-11 reports/round-12
```

For each returned path, read bytes and computed SHA-256; the aggregate is `sha256(json.dumps(path_to_digest, sort_keys=True, separators=(',', ':')).encode()).hexdigest()`. **609 paths** were present at each sample; the changed-path list was empty. Before and after aggregate SHA-256 both equal:

```text
9dc665409ec7b8ec351b57ee8644e5a96f04dc81d812f5dc6d3f1a443d4b036e
```

The initial batch at `2026-10-17T23:58:05.153535+00:00`–`2026-10-17T23:58:06.270951+00:00` had the same 609-path before/after aggregate and no changed paths. This demonstrates sampled byte/path preservation, not absence of identical-byte rewrites or unrelated workers' intervening temporary changes.

Individual validation-receipt SHA-256 values from the final snapshot (same date/interval and hashing command above):

```text
359932a7debf6ec39f3182ac078ae3e900860efd97831f6b41bfe818b96ccfba  reports/round-8/validation.json
036f84278c4817901413d97839ceba78aa8a367f91579de7505c92800611e418  reports/round-9/validation.json
e8571db918b2c3237256342bd95f241be5661a96019e460990c7d1fe2fc32f94  reports/round-10/validation.json
b5a7841dd427885c599d8a3ca01d5e5bb96470239fab38e52cd7d4d0bba0cab6  reports/round-11/validation.json
773183b2d800c7c19e18b5dba09eb7e9a83e27f621560e6cdd79122baad9af5d  reports/round-12/validation.json
```

The final tracked-input preservation control additionally enumerated:

```sh
git ls-files -z -- tools examples corpus/lessons/round-6-sources reports/supplement-opencode-1/32-craft-exercise.md reports/round-9/baselines
```

Using the same path-to-digest aggregation during the final dated interval yielded **215 paths** before and after, no changed paths, and matching SHA-256 `63ef852c5e380ff6b76a7533d2a57b2e861ba943e2e17ca25651073901ede79e`. This is a tracked-input snapshot; untracked round-14 guard/report files are not included and are not assigned-suite input pins.

## Scope and integration limits

- The default battery verifies baseline input digests, gate revision pins, schema, and coverage, plus isolated gate selftest exits. Its own JSON states `verdict_replay: not-run`; this report does not turn pinned baselines into a fresh historical-verdict replay.
- Historical states, unfilled form/mapping slots, unscreened native forms, and D3's NON-CANON/prepared-not-accepted status were not changed. Byte-identical generated output is not a lore acceptance receipt or a real-language/community clearance.
- The shared lane was under concurrent round-14 work. `git status --short` after the final batch showed other assignments' implementation/document changes (including a round-10 tracker erratum); this report does not attribute those writes to this worker or claim a clean shared working tree. The tracked historical bytes matched at the recorded batch boundaries; the integrator still owns append-only conformance of other workers' changes.
- This worker's durable write is only `reports/round-14/regression.md`; no historical artifact, tool implementation, shared LOG/SCORECARD, or packet was edited. No commit or push was made.
- If a tested tool, gate, baseline input, component, or packet changes after these pins, rerun these read-only commands with lane-confined scratch and remeasure historical-path hashes. Do not refresh a filed historical `validation.json` to update this report.
