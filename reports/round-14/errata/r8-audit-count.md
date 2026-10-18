# R14-O02 — append-only round-8 harness audit-count erratum

- **Axis:** O / operability; calibration and filed-artifact integrity preserved.
- **Defect:** `R8-AUDCNT`, `reports/round-12/defects/ledger.json`, `entries[id=R8-AUDCNT]`.
- **Disposition:** **resolved-by-documentation with control**. This new round-14 note corrects the reading of the filed audit; this worker writes no earlier-round artifact.
- **Checked:** 2026-10-17T23:57:57+00:00, measurement HEAD `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff`.

## Correction and evidence

`reports/round-8/operability/audit.md:57` (§2, V1) quotes the receipt as
`"controls_passed": 12, "controls_total": 12`. For the command
`python3 tools/harness/r8_checks.py --selftest`, the correct reading is
**14 passed / 14 total**, exit **0** (control below, 2026-10-17). The correction
concerns the harness selftest, not the separate negative-control inventory in
that audit's V5.

The admission-commit receipt at
`e1694bad6ac96aca45a11ca5746582b275929355:reports/round-8/validation.json`,
`claims.O.measurement.harness_fix`, records `controls_passed=14` and
`controls_total=14`. Its stdout SHA-256 is
`25bf2315e6c2f3403a3fc9028720225284b1848f1a91e62ae3808543b0f5ce58`,
the same digest quoted in `reports/round-8/operability/audit.md:56`.
The current harness reproduces that digest and its receipt's count exactly
(command/date above). Its SHA-256,
`0fb21d8e414c2d92b3f20742817ac9d89be24b1142b1bc65b5070086aa17fbfe`,
also matches the audit's artifact table at `audit.md:19` and the admission
receipt. This is not evidence of controls added since the filed audit.

Prior finding: `reports/round-12/recount/r8-2.md:12-16` records the same command,
count discrepancy, tool hash, and stdout hash on 2026-10-17;
`reports/round-12/recount/ledger.json:123-136` retains the discrepancy as a
disposition. **Cause remains unestablished**: stale transcription is a possible
explanation, not a demonstrated cause. This erratum changes no admission,
other audit finding, or historical receipt. The round-12 ledger's filed
`routed` status remains a historical entry; round-14 integration should cite
this note as its documentation resolution.

## Reproducible control

Run from the lane root. The following command ran at the checked time above,
exited 0, and asserted the corrected count against the admission receipt and
individual control results. Its negative leg rejects the filed audit's
12/12 counter pair; its positive leg accepts the reproduced 14/14 pair.
Both legs compare in memory: no filed content is mutated. Before/after
hashes protect the audit, validation receipt, and harness; the audit and
validation receipt must also equal their admission-commit bytes.

```bash
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

revision = "e1694bad6ac96aca45a11ca5746582b275929355"
audit = Path("reports/round-8/operability/audit.md")
validation = Path("reports/round-8/validation.json")
tool = Path("tools/harness/r8_checks.py")
protected = (audit, validation, tool)
def hashes():
    return {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}
before = hashes()
filed = json.loads(subprocess.check_output(["git", "show", f"{revision}:{validation}"]))
recorded = filed["claims"]["O"]["measurement"]["harness_fix"]
old = json.loads(re.search(r'^receipt: (\{.*\})$', audit.read_text(), re.M)[1])
command = ["python3", str(tool), "--selftest"]
run = subprocess.run(command, capture_output=True, timeout=60)
assert run.returncode == 0 and not run.stderr
receipt = json.loads(run.stdout)
counts = (receipt["controls_passed"], receipt["controls_total"])
assert counts == (14, 14)
assert len(receipt["controls"]) == sum(c["passed"] is True for c in receipt["controls"]) == 14
assert receipt["selftest_passed"] is True
assert (recorded["controls_passed"], recorded["controls_total"]) == counts
stdout_sha = hashlib.sha256(run.stdout).hexdigest()
assert stdout_sha == recorded["stdout_sha256"]
assert recorded["sha256"] == before[str(tool)]
assert subprocess.check_output(["git", "show", f"{revision}:{audit}"]) == audit.read_bytes()
assert subprocess.check_output(["git", "show", f"{revision}:{validation}"]) == validation.read_bytes()
def matches(candidate):
    return (candidate["controls_passed"], candidate["controls_total"]) == counts
assert (old["controls_passed"], old["controls_total"]) == (12, 12)
assert not matches(old) and matches(receipt)
assert hashes() == before
print(json.dumps({
    "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "head": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
    "command": " ".join(command),
    "audit_count": [old["controls_passed"], old["controls_total"]],
    "filed_and_reproduced_count": list(counts),
    "exit": run.returncode,
    "stdout_sha256": stdout_sha,
    "negative_control_12_12_rejected": not matches(old),
    "positive_control_14_14_accepted": matches(receipt),
    "audit_and_validation_equal_admission_commit": True,
    "protected_sha256_unchanged": before
}, indent=2))
PY
```

Observed preservation hashes (control above, 2026-10-17):

- `reports/round-8/operability/audit.md`: `e192860a5c1d376242837d31a5ca53fab201a643b57afa005523fe795fa4d48e`.
- `reports/round-8/validation.json`: `359932a7debf6ec39f3182ac078ae3e900860efd97831f6b41bfe818b96ccfba`.
- `tools/harness/r8_checks.py`: `0fb21d8e414c2d92b3f20742817ac9d89be24b1142b1bc65b5070086aa17fbfe`.

Do not rerun `reports/round-8/run-validation.py` to check this note: it writes
the filed receipt. Use the stdout-only harness command and the read-only
comparison above. Future count citations should derive totals from the parsed
receipt and name the exact tool/output hashes rather than copy the audit's
incorrect counter pair. Fleet regressions and consolidated routed-resolution
bookkeeping belong to their assigned round-14 owners, not this erratum.
