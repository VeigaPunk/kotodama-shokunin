# R14-V04 — independent regression-suite verification

- Axis: O / operability; non-regression constraints: reproducibility, held design debt, and filed-receipt preservation.
- Result: **PASS — 18/18 independent regression invocations exited 0**, with empty stderr. The separate real default-battery run is verified in `verify-1.md`.
- Main batch: **2026-10-18T00:02:26.469254+00:00** through approximately **00:02:27.8Z**; supplemental typed-pipeline batch: **2026-10-18T00:05:04.715529+00:00** through approximately **00:05:07.8Z**.
- HEAD: `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff`; declared baseline remains `926c86f8be3cc9307f8f10dce55768c290b6f94d`. Tested working-tree executable pins are listed below.

## Execution and capture

Before scratch-capable commands: `export TMPDIR="$PWD/.scratch"; export PYTHONDONTWRITEBYTECODE=1; mkdir -p "$TMPDIR"`. Ran the commands below with `subprocess.run(argv, capture_output=True, timeout=180)` from the lane root, concurrently with `ThreadPoolExecutor`. Captured raw stdout/stderr bytes in memory, calculated `hashlib.sha256(result.stdout).hexdigest()`, and measured each executable's SHA-256 before and after its call. No source changed during its measured invocation. No live historical round validator was executed, and no output was emitted into filed packet paths.

All quoted output below is from this verifier's corresponding command stdout, not copied from another worker's report. Dates apply to each item in its named batch. No attempt was made to sum unlike control/check families into a single domain-quality count.

## Main batch — 2026-10-18T00:02:26Z

Every command in this section exited **0**.

1. `python3 tools/check-gate-battery.py --selftest` — `SELFTEST OK 29/29 controls behaved as expected`, including `CTRL-BASELINE-DEFAULT-ROOTS`. stdout SHA-256 `2812a3270ce97583eaa9a7a16f78f95c60e703b00076fd2fc95f0802783442c2`.
2. `python3 tools/check-craft-exercise.py --selftest` — `SELFTEST OK 10/10 tamper cases detected`; `CLI-SELFTEST OK 18/18 cases passed`. stdout SHA-256 `77d408e10a494fa58fcaa5872d7ad20b6daaa9c5725329d1a0ae65ab8f0e7d32`.
3. `python3 tools/d2-typed-labels.py --selftest` — `selftest: 39/39 checks passed`, including real fixture emit/check/tamper, malformed input, and typed/held channel cases. stdout SHA-256 `7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252`.
4. `python3 tools/assemble-d2.py --selftest` — `selftest: 42/42 checks passed`, including fixture assembly/check/tamper and malformed/missing/duplicate/shape controls. stdout SHA-256 `a81294c0347660d9b46952146bac967fc80c79c9d629d7f34e69d0411bec0336`.
5. `python3 tools/assemble-culture-d3.py --selftest` — `selftest: 85/85 checks passed`; real naming and costume gates ran read-only. stdout SHA-256 `91a0653948d48a10f6bd84af7adb3dd4cda3b25e8a15a77a3bf2cd92a4deac2b`.
6. `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` — `OK all checks passed (audits=7, mech_cases=11, derivations=9, approx_checks_runner=37)`. The runner explicitly labels 37 approximate. stdout SHA-256 `18128adfc703fd268ec70684f35a2a05b3257faf4b31add8f21b3313ad4a2650`.
7. `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json --report reports/supplement-opencode-1/32-craft-exercise.md` — same clean result, additionally checking the filed report contract; this option reads the report. stdout SHA-256 `18128adfc703fd268ec70684f35a2a05b3257faf4b31add8f21b3313ad4a2650`.
8. `python3 tools/d2-typed-labels.py --check` — `examples/culture-d2/typed-labels.d2.yml` is a `byte-identical deterministic projection`. stdout SHA-256 `17064af53c48304def6b2a5f5c80c10161182b5715678a61d6d5b0d80e1ef427`; the complete stream includes the lane's absolute path.
9. `python3 tools/assemble-d2.py --check` — `packet.d2.yml: byte-identical deterministic assembly`. stdout SHA-256 `2fa0c8c197459f549de2f0822b8895477e27dcce38def75e18346ba6d672e386`.
10. `python3 tools/assemble-culture-d3.py --check` — both `packet.json` and `packet.gates.yml` are byte-identical deterministic assemblies. stdout SHA-256 `e20620fabdf285323c021ae11cad32b1ece58a28d59dd74f7df237578ffb560a`.
11. `python3 tools/check-evidence-coupling.py --selftest` — JSON `selftest_passed: true`, all **32 executed result objects** passed: five positive, sixteen domain, four malformed, five frozen, and two usage cases. stdout SHA-256 `cf62bc50e303b793b6b930c83a5ddd7d462c39cc39fef133385db830c1d380ce`.
12. `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` — actual committed packet evaluates with `exit: 0`, `findings: []`, `counts.total: 0`. stdout SHA-256 `e282a0688498034144fb376ab43884c8607133bd6deaab763150d789b113669d`.
13. `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` — actual committed freeze evaluates with `exit: 0`, no findings; this is separate from the selftest's synthetic frozen controls. stdout SHA-256 `e282a0688498034144fb376ab43884c8607133bd6deaab763150d789b113669d`.
14. `python3 tools/harness/receipt_guard.py --selftest` — JSON `selftest_passed: true`, **45/45 controls passed**, including committed-receipt refusal and explicit-refresh cases in disposable in-lane fixtures. stdout SHA-256 `34b11ed308c88f747457fcbf2b49c47b9f16f8827f23047d04db24fc80f33284`.

## Supplemental typed-pipeline batch — 2026-10-18T00:05:04Z

Every command in this section exited **0**.

15. `python3 tools/assemble-d2-typed.py --selftest` — `selftest: 11/11 checks passed`, including fixture build/check/tamper, stale projection, coverage-gap, and malformed-packet cases. stdout SHA-256 `00303b77249831604f6b0a8bb086771c8e65db4c7948a52ac25aa746bf5d8015`.
16. `python3 tools/assemble-d2-typed.py --check` — `examples/culture-d2/packet.d2.typed.yml: byte-identical deterministic typed packet`. stdout SHA-256 `e3b16d3bae56cce5760cbde277716263636a4d9fad83c5c5f2f9a05b181bc924`.
17. `python3 tools/gates/typed-pipeline-gate.py --selftest` — `selftest: 12/12 checks passed`, including actual mirrored legs, channel smuggling, dropped routing rows, laundered holds, adapter drift, malformed and missing packets. stdout SHA-256 `22ce048a6528808848c737944e77dfddd370ca93f90757602eb99c0a3e640ddc`.
18. `python3 tools/gates/typed-pipeline-gate.py --json` — `ok: true`, `exit_code: 0`; **15 holds and 1 note remain**, zero FAIL. The banner explicitly defines exit 0 as equality with the frozen expected hold set, not design clearance. stdout SHA-256 `19765ddf2c36a7db5d71bd262079d6164b24f6222d9df83d0cefdeaeb8f47e62`.

## Executable pins and historical-byte control

Executable SHA-256 values measured before/after their dated commands:

```text
7aa898d627fe361517d2942a0fe2b337f15d8cdc1fcb4061b394eee60f03d574  tools/check-gate-battery.py
b5b890b4b9c9953be5ed5f5453a2b60bc9c856616b0a5b28cb2b5bca6ffdf7b5  tools/check-craft-exercise.py
0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802  tools/d2-typed-labels.py
8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d  tools/assemble-d2.py
ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014  tools/assemble-culture-d3.py
849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e  tools/check-evidence-coupling.py
d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1  tools/harness/receipt_guard.py
c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071  tools/assemble-d2-typed.py
d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d  tools/gates/typed-pipeline-gate.py
```

Immediately before and after the main batch, enumerated historical tracked paths with `git ls-files -z -- reports/round-8 reports/round-9 reports/round-10 reports/round-11 reports/round-12`, then hashed each file. Both snapshots contained **609 paths**, the changed-path list was empty, and both `sha256(json.dumps(path_to_sha256, sort_keys=True, separators=(',', ':')).encode())` values were `c282786384caf2887d454ba52aabb4446cbeb03f71f1f99c335866c4e78adab8` (same main-batch date). This proves preservation across that execution interval, not a globally clean concurrent tree. Other assignments subsequently revised their permitted new ledger entry; those changes are not silently folded into the main-batch sentinel. `verify-3.md` separately compares the final allowed append targets to the fixed baseline and reconstructs every original byte.

## Limits

Regression green does not erase the typed packet's HOLD debt, attest canon, promote SHONEN marks, or establish a round-wide admission. The guard's own output limits it to cooperative preflight/two-phase checks, not race-proof publication or a sandbox against arbitrary callback writes. Legacy rounds remain unmodified and unsafe to invoke directly in the live lane. The parent owns the round-14 acceptance receipt and all shared integration files. This verifier writes only this assigned report; scratch test data remained in the lane.
