# R14-V01 — independent default battery verification

- Axis: O / operability; controls: fail-closed baseline discovery and filed-byte preservation.
- Result: **PASS — default run 7/7 gate selftests, exit 0**, with all seven gates baseline-covered.
- Applied fix: `reports/round-14/fix-battery-roots.md`; tested source SHA-256 `7aa898d627fe361517d2942a0fe2b337f15d8cdc1fcb4061b394eee60f03d574`.
- Observed HEAD: `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff`; declared baseline remains `926c86f8be3cc9307f8f10dce55768c290b6f94d`.

## Independent before/after control

Both observations used the real command **without any `--baselines-root` override**:

```sh
export TMPDIR="$PWD/.scratch"
export PYTHONDONTWRITEBYTECODE=1
mkdir -p "$TMPDIR"
python3 tools/check-gate-battery.py
```

The command's complete stdout was captured in memory with `subprocess.run(..., capture_output=True, text=True)`, parsed as JSON, and SHA-256 hashed; no historical validator was executed.

- **Before: 2026-10-17T23:57:44.444998+00:00**, exit **2**. JSON `summary`: pass **7**, fail **0**, unevaluable **0**. JSON `baselines.summary`: **5 baselines, 5 pinned**, myth and naming uncovered. Both emitted `BASELINE-GATE-UNCOVERED`. Stdout SHA-256 `f5e229f80ff395a066876ea793315bc440474b89eb2ddd175421d16307b84f9f`.
- **After: 2026-10-18T00:02:01.577773+00:00**, exit **0**. JSON `summary`: pass **7**, fail **0**, unevaluable **0**. JSON `baselines.summary`: **8 baselines, 8 pinned, 0 unevaluable**, all **7/7 distinct gates covered**, no uncovered gates, no baseline findings. Stdout SHA-256 `94863e0ddebc1a050b06b00ac687b6d65c752da613e6f0720d4f45c1718a72b7`.
- The after-run JSON `baselines.roots` discovers **2** files under `tools/gates/expected`, **3** under `tools/gates/frozen`, and **3** under `reports/round-9/baselines`. These are baseline-record counts, not eight distinct gates.
- Both runs' JSON `originals` report **28 files before and after**, `preserved: true`, and **0 modified / 0 added / 0 deleted**. Both disposable battery mirrors were removed. Counts above come from the dated real command's JSON fields.

## Independent negative and preservation controls

At **2026-10-18T00:02:27.848986+00:00**, independently extracted and executed the four control blocks for the in-memory root regression, explicit old-root negative, copied-baseline tamper, and preservation from `fix-battery-roots.md`. Source-report SHA-256 at execution: `664554e3f977fc9b051156c50bdd71cb752658823bde03e6b74e1ea78b3600ad`.

Reproduction of the exact tested control blocks:

```sh
export TMPDIR="$PWD/.scratch"
export PYTHONDONTWRITEBYTECODE=1
mkdir -p "$TMPDIR"
python3 - <<'PY'
import re, subprocess
from pathlib import Path
blocks = re.findall(r'^```(?:sh|bash)\n(.*?)^```',
    Path('reports/round-14/fix-battery-roots.md').read_text(), re.M | re.S)
assert len(blocks) == 6
for index in (2, 3, 4, 5):
    result = subprocess.run(['bash'], input=blocks[index], text=True, timeout=120)
    assert result.returncode == (2 if index == 3 else 0)
PY
```

Observed controls, from that dated execution:

- Removing the legacy root **in memory** makes the new discovery selftest return **1**, with the named `CTRL-BASELINE-DEFAULT-ROOTS did not discover every required root` failure. The enclosing negative-control harness exits **0** after asserting that rejection.
- `python3 tools/check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen` still exits **2**: seven selftests pass, five baselines are pinned, and exactly myth/naming remain uncovered. The explicit-override path has not been weakened into a silent pass.
- The copied-tree myth-snapshot tamper is rejected by the **default CLI**, exit **2**, with `BASELINE-TAMPERED`: **8 discovered, 7 pinned, 1 snapshot_tampered**, while the seven gate selftests still pass. Only disposable `.scratch` copies are changed.
- Baseline preservation control exits **0**: **114 tracked files** equal their committed bytes; **123 total live baseline files**, including **9 pre-existing ignored advisory `run.log` files**, match full-tree manifest `fc011128689349af9f00b0927a9d2474c5cfd5856bc7341f68a714ed862c53c7`.
- The independent post-fix regression batch at **2026-10-18T00:02:26.469254+00:00** runs `python3 tools/check-gate-battery.py --selftest`, exit **0**, stdout `SELFTEST OK 29/29 controls behaved as expected`; full stdout SHA-256 `2812a3270ce97583eaa9a7a16f78f95c60e703b00076fd2fc95f0802783442c2`.

## Limits

This verifies default discovery, gate selftest exits, baseline digests/revision pins, and preservation. The battery explicitly reports `verdict_replay: not-run`; pinned baselines are not fresh historical-verdict replays. Adding the preserved round-9 root is a documented layout compatibility exception, not a claim that those old paths now satisfy the standard layout. This verifier did not change the implementation, baseline bytes, or any filed receipt.
