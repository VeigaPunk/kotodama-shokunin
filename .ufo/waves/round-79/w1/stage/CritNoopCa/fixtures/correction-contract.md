# Ca correction record — assumed contract (for ExecCaCounter / ScribeClaims alignment)

One correction record per mismatch, landing as an append-only record (exact lane
path is L1's choice; the round-79 telemetry dir is the natural home). Shape:

```json
{
  "id": "S884",
  "receipt": "reports/round-78/telemetry/census-end.txt",
  "receipt_sha256": "<sha256 of the committed receipt bytes at measured_revision>",
  "measured_revision": "4b255745dea45a45d88b17e3c3fea4cdb6700cf7",
  "old_token": "<S884 used-by token exactly as it appears in the committed receipt line>",
  "actual_token": "<S884 used-by cell exactly as it appears in corpus/SOURCES.md at measured_revision>"
}
```

A correction flips the frozen counter's `unresolved` from 1 to 0 only if every
binding below is re-derived from committed bytes (`git show <rev>:<path>`), never
from worktree or from the correction's own prose:

1. RECEIPT-UNCHANGED — the receipt bytes at `--lands` equal the receipt bytes at
   the freeze commit (append-only; in-place repair of the drifted line is the
   changed-receipt cheat and must fail).
2. RECEIPT-DIGEST — `receipt_sha256` equals the sha256 of the committed receipt
   bytes at `measured_revision`.
3. REVISION — `measured_revision` is the 40-hex commit the receipt was read at,
   and it is an ancestor of `--lands` on the first-parent chain (it is the
   round-78 census commit `4b255745dea45a45d88b17e3c3fea4cdb6700cf7`, not the
   lane base and not HEAD).
4. OLD-TOKEN — `old_token` equals the token in the committed receipt's S884 line
   (`reports/round-78/telemetry/census-end.txt:33` at the measured revision).
5. ACTUAL-TOKEN — `actual_token` equals the S884 used-by cell of
   `corpus/SOURCES.md` at `measured_revision`, and differs from `old_token`.

Baseline (no correction lands): the counter re-derives mismatch=1 from the
committed receipt vs the committed registry and reports unresolved=1.

Presence-only predicate (the vacuous shape this seat attacks): "a correction
record mentioning S884 with a non-empty actual_token exists." It binds nothing
and is passed by payloads J-CA1..J-CA5 in `junk-corrections.json`.
