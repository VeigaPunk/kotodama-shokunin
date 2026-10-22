# ExecGateFixtures — Round 55

Axes: operability and calibration.

## Deliverables

Scratch files (all under `/fast/scratch/hyaku/kotodama-r55/ExecGateFixtures/`):

- `fixtures-r55.md`: lesson-shaped `## Gate` fixture with 17 rows, S901–S917. It contains flagged candidates and controls for doubled locators, truncated grounds, hard-wrapped quotes, guillemets, inter-span ellipsis and `* ` bullets. Controls include single-quoted section locators without a repeated quote, a quote equal to an unquoted heading word, grounds ending in `p.`, `e.g.` and a full stop, an internal hyphen, ellipses at the start/end of one span, and a literal `* ` in ordinary row content.
- `expect.tsv`: S-id and class/`none` for every fixture row.
- `run-fixtures.py`: stdlib-only runner. It checks the finding summary, exit status and output format; checks each expected finding detail and absence controls; flags any findings for an unlisted S-id; and prints per-row `MATCH`/`MISMATCH`.

## Baseline run evidence

Run 1 (before the runner cleanup edit):

```text
python3 -B /fast/scratch/hyaku/kotodama-r55/ExecGateFixtures/run-fixtures.py /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py; printf 'EXIT CODE: %s\n' "$?"
```

```text
MISMATCH S901 expected=doubled-locator got=none
MATCH S902 expected=no finding got=none
MATCH S903 expected=no finding got=none
MISMATCH S904 expected=truncated-grounds got=none
MATCH S905 expected=no finding got=none
MATCH S906 expected=no finding got=none
MATCH S907 expected=no finding got=none
MISMATCH S908 expected=words=26 got=none
MATCH S909 expected=no finding got=none
MISMATCH S910 expected=words=26 got=none
MATCH S911 expected=no finding got=none
MISMATCH S912 expected=words=22 got=none
MATCH S913 expected=no finding got=none
MATCH S914 expected=no finding got=none
MISMATCH S915 expected=words=26 got=none
MATCH S916 expected=no finding got=none
MATCH S917 expected=no finding got=none
FIXTURES: 11/17 match; checker=/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py
EXIT CODE: 1
```

Run 2 (after the runner cleanup edit):

```text
python3 -B /fast/scratch/hyaku/kotodama-r55/ExecGateFixtures/run-fixtures.py /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py; printf 'EXIT CODE: %s\n' "$?"
```

```text
MISMATCH S901 expected=doubled-locator got=none
MATCH S902 expected=no finding got=none
MATCH S903 expected=no finding got=none
MISMATCH S904 expected=truncated-grounds got=none
MATCH S905 expected=no finding got=none
MATCH S906 expected=no finding got=none
MATCH S907 expected=no finding got=none
MISMATCH S908 expected=words=26 got=none
MATCH S909 expected=no finding got=none
MISMATCH S910 expected=words=26 got=none
MATCH S911 expected=no finding got=none
MISMATCH S912 expected=words=22 got=none
MATCH S913 expected=no finding got=none
MATCH S914 expected=no finding got=none
MISMATCH S915 expected=words=26 got=none
MATCH S916 expected=no finding got=none
MATCH S917 expected=no finding got=none
FIXTURES: 11/17 match; checker=/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py
EXIT CODE: 1
```


Run 3 (after the fixture match-count edit):

```text
python3 -B /fast/scratch/hyaku/kotodama-r55/ExecGateFixtures/run-fixtures.py /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py; printf 'EXIT CODE: %s\n' "$?"
```

```text
MISMATCH S901 expected=doubled-locator got=none
MATCH S902 expected=no finding got=none
MATCH S903 expected=no finding got=none
MISMATCH S904 expected=truncated-grounds got=none
MATCH S905 expected=no finding got=none
MATCH S906 expected=no finding got=none
MATCH S907 expected=no finding got=none
MISMATCH S908 expected=words=26 got=none
MATCH S909 expected=no finding got=none
MISMATCH S910 expected=words=26 got=none
MATCH S911 expected=no finding got=none
MISMATCH S912 expected=words=22 got=none
MATCH S913 expected=no finding got=none
MATCH S914 expected=no finding got=none
MISMATCH S915 expected=words=26 got=none
MATCH S916 expected=no finding got=none
MATCH S917 expected=no finding got=none
FIXTURES: 11/17 match; checker=/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py
EXIT CODE: 1
```

The two new classes both mismatch against the base checker (S901 and S904), as expected. The four carried-shape red cases also mismatch against the base checker (S908, S910, S912, S915). The 11 controls match. Run 3 is the final runner version.

No other checks were run. No tools were installed.

## Final `run-fixtures.py` source

```python
#!/usr/bin/env python3
"""Compare Gate fixture findings with the adjacent expect.tsv (stdlib only)."""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIXTURE = ROOT / "fixtures-r55.md"
EXPECT = ROOT / "expect.tsv"
FINDING = re.compile(r"^.+:\d+\s+(S\d+)\s+(.+)$")
SUMMARY = re.compile(r"^GATE_QUOTES: (\d+) findings$")
EXPECTED_DETAILS = {
    "doubled-locator": "doubled-locator",
    "truncated-grounds": "truncated-grounds",
    "hard-wrapped quote": "words=26",
    "guillemets": "words=26",
    "inter-span ellipsis": "words=22",
    "* bullet": "words=26",
}


def load_expectations(path):
    rows = []
    seen = set()
    with path.open(encoding="utf-8") as handle:
        header = handle.readline().rstrip("\n")
        if header != "S-id\tclass":
            raise ValueError("expect.tsv must start with 'S-id<TAB>class'")
        for number, raw in enumerate(handle, 2):
            line = raw.rstrip("\n")
            if not line:
                continue
            fields = line.split("\t")
            if len(fields) != 2 or not re.fullmatch(r"S\d+", fields[0]):
                raise ValueError("expect.tsv:%d must contain S-id<TAB>class" % number)
            sid, expected = fields
            if sid in seen:
                raise ValueError("expect.tsv:%d repeats %s" % (number, sid))
            if expected != "none" and expected not in EXPECTED_DETAILS:
                raise ValueError("expect.tsv:%d has unknown class %r" % (number, expected))
            seen.add(sid)
            rows.append((sid, expected))
    if not rows:
        raise ValueError("expect.tsv contains no fixture rows")
    return rows


def run_checker(checker):
    result = subprocess.run(
        [sys.executable, str(checker), str(FIXTURE)],
        capture_output=True, text=True, check=False)
    findings = {}
    summary_count = None
    malformed = []
    for line in result.stdout.splitlines():
        summary = SUMMARY.fullmatch(line)
        if summary:
            if summary_count is not None:
                malformed.append("duplicate summary")
            summary_count = int(summary.group(1))
            continue
        finding = FINDING.fullmatch(line)
        if finding:
            findings.setdefault(finding.group(1), []).append(finding.group(2))
        else:
            malformed.append("unrecognized stdout: %r" % line)
    if summary_count is None:
        malformed.append("missing GATE_QUOTES summary")
    elif summary_count != sum(map(len, findings.values())):
        malformed.append("summary says %d findings; parsed %d" % (
            summary_count, sum(map(len, findings.values()))))
    if result.stderr:
        malformed.append("checker wrote to stderr: %s" % result.stderr.strip())
    if result.returncode not in (0, 1):
        malformed.append("checker exited %d" % result.returncode)
    elif result.returncode != (1 if summary_count else 0):
        malformed.append("exit code disagrees with finding summary")
    if malformed:
        raise RuntimeError("; ".join(malformed))
    return findings


def main(argv):
    if len(argv) != 2:
        print("usage: run-fixtures.py CHECKER.py", file=sys.stderr)
        return 2
    checker = Path(argv[1]).expanduser().resolve()
    try:
        expected = load_expectations(EXPECT)
        findings = run_checker(checker)
    except (OSError, ValueError, RuntimeError) as exc:
        print("FIXTURE_ERROR: %s" % exc, file=sys.stderr)
        return 2

    failures = 0
    matches = 0
    for sid, expected_class in expected:
        details = findings.get(sid, [])
        if expected_class == "none":
            matched = not details
            wanted = "no finding"
        else:
            wanted_detail = EXPECTED_DETAILS[expected_class]
            matched = wanted_detail in details
            wanted = wanted_detail
        status = "MATCH" if matched else "MISMATCH"
        if not matched:
            failures += 1
        else:
            matches += 1
        observed = ",".join(details) if details else "none"
        print("%s %s expected=%s got=%s" % (status, sid, wanted, observed))
    expected_ids = {sid for sid, _ in expected}
    for sid in sorted(set(findings) - expected_ids):
        failures += 1
        print("MISMATCH %s expected=no fixture row got=%s" % (
            sid, ",".join(findings[sid])))

    print("FIXTURES: %d/%d match; checker=%s" % (
        matches, len(expected), checker))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

## Risks and blockers

The fixture expectation schema pins the two new classes by exact details and pins escape cases to their expected `words=26`/`words=22` detail. The baseline run confirms those expected rows are presently absent; the future checker needs to honor those details. No blockers.