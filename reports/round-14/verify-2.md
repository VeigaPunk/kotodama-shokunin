# R14-V02 — independent tracker SHA-differential verification

- Axis: O / operability; non-regression constraints: filed-row integrity and calibrated historical/current readings.
- Result: **PASS — applied-with-control, append-only erratum**.
- Verified at **2026-10-18T00:00:21.798792+00:00**; HEAD `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff`.
- Applied fix: `reports/round-14/fix-tracker-pointer.md`; correction source: `reports/round-12/defects/fix-09.md:35-50`.

## Independent command and receipt

Executed the actual fix report's sole shell control, rather than relying on its printed PASS. This reproducible wrapper creates no file and invokes no round validator:

```sh
export TMPDIR="$PWD/.scratch"
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
import datetime, hashlib, re, subprocess
from pathlib import Path
path = Path('reports/round-14/fix-tracker-pointer.md')
text = path.read_text()
blocks = re.findall(r'^```(?:sh|bash)\n(.*?)^```', text, re.M | re.S)
assert len(blocks) == 1
print('independent_verifier_date=' + datetime.datetime.now(datetime.timezone.utc).isoformat())
print('control_source=' + path.as_posix())
print('control_source_sha256=' + hashlib.sha256(path.read_bytes()).hexdigest())
result = subprocess.run(['bash'], input=blocks[0], capture_output=True, text=True, timeout=90)
print(result.stdout, end='')
print(result.stderr, end='')
print('control_exit=' + str(result.returncode))
raise SystemExit(result.returncode)
PY
```

Observed exit **0**, `status: PASS`; source report SHA-256 `dd1d2c9f95c094493e4dee48898417b2a023fb135787d374051ad57e4a6d1028`. All following counts/digests come from that dated command:

- Whole tracker before: `5a0ca3de9a058de2b8e772f5f2af0bd5302a04957764e3639938f00ba496effc`.
- Whole tracker after: `4b983ae9237dda1b46fba59fac2ce8731a1a924ae9672925757bcc4ebc30def2`.
- Raw findings array: **24 original rows, 34,978 UTF-8 bytes**; before and after SHA-256 both `e61727782a4cd57475fb9fb72ffaf2e503443c93206c6f7f017c1468d7c74d9c`.
- Removing only the new trailing `errata` member and its JSON separator reconstructs **every original tracker byte**, including whitespace. All original fields remain equal to the fixed revision's values.
- Historical `final_state.verify_files`: **3** basenames. Effective `errata[id=R14-O03].final_state.verify_files`: **4**, equal to all **4** existing `findings-verify-*.md` basenames, with no missing or extra item. The added effective pointer is `findings-verify-3.md`.
- The round-12 source correction is byte-identical to its filed revision.
- Negative controls passed: an omitted verifier is rejected, a nonexistent extra verifier is rejected, and mutation of an original finding row is rejected (**3/3**).

## Interpretation and limits

The whole tracker SHA-256 **must differ** because a new key was appended. Calling the whole file unchanged would be false. The differential proves that its original findings and other filed bytes were preserved, and that the new erratum resolves the missing effective verifier pointer. Consumers must apply that erratum; the historical `final_state` list deliberately remains unchanged. This verifier wrote only this evidence file and did not rewrite any filed receipt.
