- Seat: O01 | executor | O | date 2026-10-19 | baseline 456674d

## Template draft

The following is the complete proposed `templates/round-runner-template.py`. It is a starter shape, not a runnable acceptance test until a round author implements `measure()` with that round's checks.

```python
#!/usr/bin/env python3
"""Starter shape for a per-round acceptance runner."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import runpy
import sys

RUNNER_PATH = Path(__file__).resolve()
# 1. Runners installed at reports/round-N/run-validation.py derive the repository
# root from their location, so invocation does not depend on the caller's directory.
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = RUNNER_PATH.parent
ROUND = int(ROUND_DIR.name.removeprefix("round-"))
RUNNER = RUNNER_PATH.relative_to(ROOT).as_posix()
OUTPUT = ROUND_DIR / "validation.json"
COMMAND = f"python3 {RUNNER}"


def measure() -> dict:
    """Implement checks for this round and return a receipt measurement mapping.

    The mapping must include acceptance_checks_passed (bool), claims, failures,
    named_findings (list[str]), limits (list[str]), and may include input_sha256.
    named_findings and limits must describe this round's measured facts and
    verification limits, not inherited text from an earlier round.
    """
    raise NotImplementedError("replace measure() with this round's acceptance checks")


def make_receipt(measurement: dict) -> dict:
    if not isinstance(measurement, dict):
        raise TypeError("measure() must return a dict")
    if not isinstance(measurement.get("acceptance_checks_passed"), bool):
        raise ValueError("acceptance_checks_passed must be a bool")
    for key in ("named_findings", "limits"):
        values = measurement.get(key)
        if not isinstance(values, list) or any(
            not isinstance(value, str) or not value.strip() for value in values
        ):
            raise ValueError(f"{key} must be a list of non-empty strings")

    runner_sha256 = hashlib.sha256(RUNNER_PATH.read_bytes()).hexdigest()
    # 4. read_bytes() either yields the actual runner digest or raises; never
    # publish a receipt with a null/missing runner_sha256.
    receipt = dict(measurement)
    inputs = receipt.get("input_sha256", {})
    if not isinstance(inputs, dict):
        raise ValueError("input_sha256 must be a dict when supplied")
    receipt.update({
        "round": ROUND,
        "runner": RUNNER,
        "runner_sha256": runner_sha256,
        "counting_command": COMMAND,
        "date": dt.date.today().isoformat(),
        "measured_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    })
    receipt["input_sha256"] = dict(inputs)
    receipt["input_sha256"][RUNNER] = runner_sha256
    return receipt


def guard_receipt() -> None:
    guard = runpy.run_path(str(ROOT / "tools/harness/receipt_guard.py"))
    guard["guard_receipt"](OUTPUT, repo_root=ROOT)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="print the measured receipt without writing it")
    args = parser.parse_args(argv)

    receipt = make_receipt(measure())
    rendered = json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.check:
        sys.stdout.write(rendered)
        return 0

    # 3. The guard must succeed immediately before the only receipt write.
    guard_receipt()
    OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"receipt: {RUNNER.rsplit('/', 1)[0]}/validation.json")
    print(f"acceptance_checks_passed: {receipt['acceptance_checks_passed']}")
    return 0 if receipt["acceptance_checks_passed"] else 1


# 2. Never mutate the process working directory; resolve repository paths from ROOT.
# 5. Implement measure() with current-round named_findings and limits, never copied
#    forward from a prior receipt.
if __name__ == "__main__":
    sys.exit(main())
```

## Owed

- None for this seat's draft. The `measure()` hook is intentionally unimplemented and must be completed for each consuming round.

## Citations

- `reports/round-41/claims.json:13-18` — required template shape and five contract points.
- `reports/round-41/targets.json:41-45` — O01's assigned output and mission.
- `reports/round-40/run-validation.py:5,197-208,227-247` — relative `ROOT`, runner digest and round-specific receipt fields, guarded publish path, and `--check` behavior in the reference runner.
- `reports/round-33/run-validation.py:22-29` — relative root/path setup precedent.
- `tools/harness/receipt_guard.py:4-15` — guard call contract and callback limitation.
- `reports/round-40/validation.json:129-143` — `limits`, `named_findings`, runner path, and measured runner hash fields in the reference receipt.
