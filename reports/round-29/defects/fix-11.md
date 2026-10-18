# R29-O11 — missing machine twin for the r4 supersession

- Date: 2026-10-18.
- Status: **closed by a generated, pinned successor row.**

## Defect and correction

The R25 `declared-in-r4` revision carried corrected claim prose but no machine twin. The R26 owner generated the twin from the filed packet using the renderer's projection logic and placed it under `reports/round-26/remainders/r4-twin/`; the R25 revision remains packet-only and unchanged. A checker tests derivation, compatibility with prior twins, corrected content, and preservation. This is a bounded artifact-shape correction, not a renderer rewrite.

The R26 disposition report, `reports/round-26/remainders/r4-twin.md` §§2–5, records `python3 reports/round-26/remainders/r4-twin/verify-twin.py --root .scratch/r26-o29-vc --frozen-root .scratch/r26-o29-frozen --source-root .scratch/r26-o29-clone --check` → exit 0, **24/24** controls on 2026-10-18. The checker required isolated clones. Its controls include byte-for-byte rebuilding of two predecessor twins and a stale-prose positive/negative control.

## Independent current pin check

At **2026-10-18 18:02:53−03:00**, with `TMPDIR=$PWD/.scratch`, I ran a read-only Python SHA-256 comparison of `reports/round-26/remainders/r4-twin/twin.json` against `twin_sha256` in its `expected.json`. The computed digest was `1874efbc1a6f892d035e47bbfbb8ca228622b26fd622a002ee822594a5420b95`; it matched the declared pin. The file size was **103,975 bytes**, from the same dated command. This rechecks identity, not full derivation; the isolated 24-control check above is the derivation evidence.

## Disposition

Retain the R26 twin as a new row and leave R25 bytes alone. No additional source change is needed for this bounded gap.