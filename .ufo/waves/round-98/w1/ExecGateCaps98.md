# ExecGateCaps98 — Gate capture-file checker (round-97 closure routed defect 3)

## Usage

```
python3 -B tools/check-gate-captures.py <lesson.md> <evidence-dir>
python3 -B tools/check-gate-captures.py --selftest --work <existing-dir>
```

Input: a lesson path and an evidence dir. Parses markdown table rows under the
lesson `## Gate` section (from `## Gate` to the next `## ` heading) that carry
an S-id (first cell `S\d+`), a sha256 token (full 64-hex, or the round-97
legacy truncated 16-hex + ellipsis form), and a capture-file cell (header
column named `capture file`, case-insensitive, bare file name resolved under
the evidence dir). Stdlib only; honors TMPDIR and never writes/reads /tmp
except via the resolved tempfile dir for the refuse-temp guard; no hardcoded
/tmp.

## Finding names

- `ROW <id> OK <file>` — named file exists and its sha256 matches the row hash
  (exact for 64-hex; prefix match for truncated legacy tokens).
- `ROW <id> CAPTURE-MISSING -` — no `capture file` header column, or the row's
  cell is empty.
- `ROW <id> CAPTURE-ABSENT <file>` — the named file does not exist under the
  evidence dir (a path with `/` or `\` is also absent: bare basename required).
- `ROW <id> SHA-MISMATCH <file>` — the file exists but its sha256 differs from
  the row hash (exact for 64-hex; prefix for truncated tokens). In particular
  the round-97 S993 case: row hash is the PDF's, named file is the `.txt` →
  SHA-MISMATCH.
- Summary: `GATE-CAPTURES: <k> finding(s) in <m> row(s)` (k = non-OK rows).
- Error: `GATE_CAPTURES_ERROR: <reason>` on stderr, exit 2, no traceback — on
  usage error, missing lesson, missing evidence dir, invalid UTF-8, or no
  `## Gate` section. Exit 0 iff 0 findings, 1 iff any finding.

## Selftest

Requires `--work <existing-dir>` outside the resolved tempfile dir (refused
otherwise). Fixtures built under `<work>/check-gate-captures-selftest/`,
removed after. Cases (13): clean row; missing column; absent file; sha
mismatch; S993 pdf-vs-txt mismatch; S993 pdf clean; truncated legacy row
(counted, CAPTURE-MISSING); invalid UTF-8 (rc 2, named error, no traceback);
no Gate section (rc 2); missing evidence dir (rc 2); no args (rc 2);
refuse-tmp-work (rc 2); empty capture cell.

```
SELFTEST PASS 13/13
```

saved at `.ufo/waves/round-98/w1/stage/ExecGateCaps98/selftest.txt`
(sha256 56ba4cfb8c1bc9fbb361858d1efca7c810a25836b25d0e43395b3ecb4126166a).

## Round-97 run

`python3 -B tools/check-gate-captures.py corpus/lessons/round-97.md
reports/round-97/evidence` → rc 1 (expected: findings, round 97 had no
capture-file column). Output (saved at
`.ufo/waves/round-98/w1/stage/ExecGateCaps98/r97-run.txt`):

```
ROW S985 CAPTURE-MISSING -
ROW S986 CAPTURE-MISSING -
ROW S987 CAPTURE-MISSING -
ROW S988 CAPTURE-MISSING -
ROW S989 CAPTURE-MISSING -
ROW S990 CAPTURE-MISSING -
ROW S991 CAPTURE-MISSING -
ROW S992 CAPTURE-MISSING -
ROW S993 CAPTURE-MISSING -
GATE-CAPTURES: 9 finding(s) in 9 row(s)
```

Cross-check: round-96 lesson + evidence → rc 1, 10 CAPTURE-MISSING rows
S975–S984 (same no-capture-column shape). The checker reports the missing
column, not the (correct) underlying hashes, which is the defect-3 shape.

## Commands with rc

- `python3 -B tools/check-gate-captures.py --selftest --work /fast/scratch/hyaku/kotodama-r98/ExecGateCaps98/selftest` → rc 0, `SELFTEST PASS 13/13`.
- `python3 -B tools/check-gate-captures.py corpus/lessons/round-97.md reports/round-97/evidence` → rc 1, 9 CAPTURE-MISSING / 9 rows.
- `python3 -B tools/check-gate-captures.py corpus/lessons/round-96.md reports/round-96/evidence` → rc 1, 10 CAPTURE-MISSING / 10 rows.
- `sha256sum tools/check-gate-captures.py` → `1bea70ee1da0dd1a8b5555657cc905771809734dcafbaac45103544029019a98`.
- `rm -rf /fast/scratch/hyaku/kotodama-r98/ExecGateCaps98` → rc done, dir removed.

## Files

- Tool: `tools/check-gate-captures.py`
  (sha256 1bea70ee1da0dd1a8b5555657cc905771809734dcafbaac45103544029019a98)
- `selftest.txt`, `r97-run.txt`, `DONE` (tool sha256) in
  `.ufo/waves/round-98/w1/stage/ExecGateCaps98/`.

## Tooling authorization

None installed or upgraded (python3 stdlib only, already present).

**Report:** write your scoped findings to .ufo/waves/round-98/w1/ExecGateCaps98.md
