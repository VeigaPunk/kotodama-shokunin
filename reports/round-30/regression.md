# R30-O13 — full current regression sweep

**Verdict: NOT GREEN — 37/40 current commands passed.** Three parent-owned integration dependencies remain. The measured current tree is stable during the final sweep, and all protected historical paths are preserved; neither fact converts the three nonzero commands into passes.

Date: **2026-10-18**. Final matrix window: **22:06:48–22:07:27 UTC**. Driver and counting command:

```sh
export TMPDIR="$PWD/.scratch" PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-30/verify-operability.py --selftest
python3 -B reports/round-30/verify-operability.py --wait 180
```

The verifier selftest passed **7/7**, exit 0. The second command ran a bounded dependency watch with 60-second polling, then published `regression.json` and `operability-verification.json`, exit 1. Every child command, start/end timestamp, actual exit, full output and stdout/stderr SHA-256 is durable in those receipts. The tool's **40 current-command** denominator is distinct from **41 actual commands**: the immutable R28 sweep selftest is separately measured as a historical supersession control, not silently labelled green.

## Current commands that pass

The final `regression.json` shows exit 0 for all of these groups, **37 commands total** (counted by the driver on 2026-10-18):

- Battery classifier/registration selftest: **44/44 controls**.
- Craft positive and selftest; packet-links and uncertainty selftests.
- D2 source and typed assembly checks and their selftests.
- D3 deterministic assembly, its selftest, evidence-coupling positive and selftest.
- D4 source and typed assembly checks and their selftests; D4 projection and both actual adapter-gate input CLIs.
- Typed projector selftest and D2 projection check.
- Typed-pipeline regular and generalized selftests; D2, D4 source and D4 typed positive runs. D4 source reports **20/20** legs and typed reports **17/17**.
- Argot selftest and D4 positive; delivered law **clean** positive.
- V2 handoff positive and selftest; V3 handoff **selftest**, which freezes/replays its own disposable fixture.
- Frozen-replay and pin-repoint selftests; ceiling instrument and its selftest.

The flagless D4 assembly adapter is exercised by its supported packet argument. Its nonexistent `--selftest` is not invented as a test leg. Seven structural gate selftests are already executed in the default battery; baseline coverage is a separate counter.

## The three current reds — exact causes and owners

1. **`battery`, exit 2.** Seven structural legs pass; **19/19** discovered baselines are pinned; ten gates are registered, but coverage is **9/10** and exactly `register-law-gate.py` is uncovered. Owner: orchestrator/default-root baseline integration after the speaker gate settles. Registration is functioning and fails closed. The independent nine-baseline omission control reproduces precisely this result. Do not borrow a temporary extra baseline root as proof that the default invocation is fixed.
2. **`law-selftest`, exit 1, 29/33.** The old `bool(base)` condition rejects the newly finding-free packet; its three broad first-field mutations hit earlier QREG identity rows instead of the law block. The separate tokenless law-row mutation still returns exit 0 with unchanged finding lines. Owner: orchestrator, applying the verified report-only candidate in `fixes/speaker-tamper.md`. Neither a candidate nor the older green ID-bearing selftest closes this delivered tail.
3. **`handoff-v3`, exit 1.** A non-quiet real run confirms `E2E-DIGEST`: six read-set inputs changed since the default baseline—brief component, lexicon component, hold file, raw packet, projection and typed packet. The conventional hold-file pointers are now correct, and the v3 selftest passes. Owner: orchestrator, landing a new durable baseline generation and routing the default regression to it. The packet owner's green explicit fresh-baseline replay is compatibility evidence, not a fresh default pin. Never rewrite the old freeze or suppress input-digest checks.

All values above are taken from the dated driver's JSON fields or the separately executed `python3 -B tools/exercise-handoff-e2e.py --profile v3` diagnostic run on **2026-10-18**. The latter returned exit 1 with six named `FAIL input-digest` lines and `E2E-DIGEST`.

## Historical row — retain its red verdict

`TMPDIR=/var/tmp python3 -B reports/round-28/sweep/sweep.py --selftest` returns **exit 1**, final control summary **11/12**, with only `r28-generation-replays-green` false. Its old R28 generation is now superseded by the QREG amendment; the report and frozen inputs are protected and must not be changed to force a modern green result. This row is retained in `regression.json:historical_controls` with its actual output and failed-control list. It is **not** counted as an exit-zero command or a current regression pass.

An earlier in-flight observation also had `hold-walker-finds-the-committed-hold-set` false while the owner tried a successor-only path. The final conventional-path repair removes that second failure. The historical classifier recognizes only these explicitly enumerated supersession readings; a crash or unrelated failed control remains unevaluable, not an expected pass.

## Preservation and temporal scope

- **No final source drift:** `source_drift: []` in both final receipts. Inputs are SHA-256 bound across tools, active profiles/baselines, D2/D3/D4 artifacts, the telemetry evidence and fix fragments; a moving input invalidates the result.
- **Protected reports/frozen generations:** **1,764** tracked paths for rounds 8–29 match declared baseline `87bfc9956f0fc60e6821fe53b622d0043e28be10` in bytes and mode before and after. No protected status rows; no differences; protected manifest SHA-256 `c3bc68dd9c1f1e5bd875e873e543abb59cfa39d32a7860e6a0700b1dc76f9884`. Command/date: the driver above, **2026-10-18**. Endpoint sampling cannot exclude an intervening write-and-restore.
- The initial in-flight **32/40 exit-zero** observation is retained unchanged in `regression-initial.json`. Its old denominator includes the historical R28 row and lacks the later generalized selftest. It is not silently compared to the final 40-current-command inventory.
- No historical acceptance runner or receipt-writing historical gate-test runner was launched. No original fixture, shared source, corpus entry or historical artifact was edited by this seat. Ordinary control copies were under `.scratch`; mirror-safety legs alone used `/var/tmp` and removed their temporary roots. No commit or push.

## Integration finish line

Land the speaker candidate, freeze the new default law baseline, and land/route the new default v3 baseline. Then rerun `python3 -B reports/round-30/verify-operability.py` and the round counting command on settled bytes. Update the two documented routes only after their actual delivered controls pass. `verify.md` and `routed-resolution.json` preserve the present blocked state and exact owner handoff; **this report is not a full-green or round-admission claim**.
