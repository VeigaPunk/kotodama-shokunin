# R21-O15 — final R20 receipt-to-runner binding

- **Disposition:** closed for the final R20 receipt; the earlier index warning describes an intermediate receipt.
- **Finding:** `reports/round-20/fragment-index-x24.md` §Conformance observations records that an earlier green receipt bound to a superseded runner. That is valid for its cited snapshot, but should not be carried forward as the final state without checking the later receipt.
- **Control:** on 2026-10-18 this worker ran:

  ```sh
  sha256sum reports/round-20/run-validation.py reports/round-20/validation.json
  stat -c '%n %y' reports/round-20/run-validation.py reports/round-20/validation.json
  date -I
  ```

  The live runner SHA-256 matches the `runner_sha256` field in the final `reports/round-20/validation.json`; the receipt timestamp is later than the runner timestamp. The command did not execute the historical runner.
- **Bounded action:** treat the final receipt as runner-bound and retain the earlier observation as an intermediate-state note. Do not rewrite either R20 artifact.
- **Limit:** a matching digest proves byte binding only; it does not independently establish the correctness of the runner's measurements.
