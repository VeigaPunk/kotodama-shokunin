## tools/check-finding-sets.py: exact-set comparator for attestation auditors

Grades an auditor (`--candidate`) against a case battery (`--cases`) built by
mutating a committed base packet (`--packet`). Each candidate runs as
`CANDIDATE --packet FILE --json` on an opaque file name. A case passes only on an
exact match:

- Exit code equals the case `rc`.
- `rc 2`: the text `ATTESTATION_ERROR` appears on stdout or stderr.
- Dirty cases: the set of finding ids and the set of `(id, record)` pairs equal
  the expected sets. Multiplicity is not compared.
- Clean cases: no findings, and `records` equals `records_count`.
- Malformed candidate output fails that case; it never aborts the run.

```
python3 tools/check-finding-sets.py --cases CASES.json --packet BASE.json \
    --candidate AUDITOR.py --json --work EXISTING_DIR
python3 tools/check-finding-sets.py --selftest --work EXISTING_DIR
```

- `--json` prints `{"passed", "total", "cases": [{name, passed, expected_rc, rc, reason}]}`.
  Without it, a summary and the failing reasons are printed.
- Exit `0` every case passes; `1` a case fails; `2` input or usage error (the
  error is also printed as JSON with `passed` and `total` of `0`).
- `--selftest` runs this CLI as a subprocess against an honest auditor and
  deliberate counterfeits (extra id, shotgun labels, wrong record, filename
  oracle, malformed output, candidate crash). It needs `tools/check-attestation-packet.py`,
  found through `KOTODAMA_ROOT` or by walking up from this file and the working directory.
- Scratch lives only under a temporary directory created inside `--work`.

Wrapper candidates that delegate to the honest auditor need `KOTODAMA_ROOT` set
to the repository root when they are copied out of `reports/round-88/controls/`.
Without it they cannot locate `tools/check-attestation-packet.py`, and every
clean case fails with `rc 2`.
