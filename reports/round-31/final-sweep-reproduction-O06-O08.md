# R31-O06..O08 — the final sweep ×3: independent three-pass reproduction of the O11 manifest

- **Seat:** R31-O06..O08 (final sweep ×3 legs), round 31, loop 3 regimen
  close-out, claim **O** `operability`.
- **Date:** 2026-10-18. Lane HEAD at every pass:
  `e8d2d0dadd3ccd1fbb7481793cfaf9bcd761826c`; tracked tree clean at HEAD.
  Untracked sibling round-31 artifacts exist; the only one entering the
  reproduced surface is the scribe's `r31-post` frozen generation (leg
  `replay-r31-post`), which the scribe's own manifest names.
- **Division of labor inside the O lane:** the scribe seat R31-O11 already
  filed the consolidated deliverable `reports/round-31/final-sweep.md` plus
  `reports/round-31/sweep/` (runner, receipt, `commands.txt`, the fresh
  `r31-post` frozen generation). Those are sibling bytes — this seat did not
  touch them. This fragment is the NEW-file evidence for the ×3 legs of the
  assignment: three independent passes over the *whole* recorded surface,
  every exit and digest compared against the scribe's recorded values.
- **Machine receipt:** `.scratch/round-31-o-sweep/reproduction-receipt-203110.json` (raw per-command rows, 3 passes;
  sha256 `65e8470bb60a89fd00f17edf71a123148476a7392685e5a796f3b8774dbb9990`), plus this
  seat's own independent 51-leg matrix receipt `.scratch/round-31-o-sweep/sweep-receipt-202325.json`
  (sha256 `7862a41e04e8e125c8c5288e627e4c3da6b4ef40778c90d2bea2b74545c9137f`).

## Method

`3` sequential passes over all 63 recorded receipt rows
(50 green-surface rows + 13 filed-red control rows) of
`reports/round-31/sweep/sweep-receipt.json` as filed (sha256
`38ada3b6b3553131195a04efe48bb261dda46a0a9a3874ccfb335a8b8d5dcbb1`, receipt HEAD
`e8d2d0dadd3ccd1fbb7481793cfaf9bcd761826c`). Each command re-executed exactly as
recorded (`python3 -B …`, repo root, `PYTHONDONTWRITEBYTECODE=1`) with the
row's own recorded tmpdir policy — `.scratch` for scratch legs,
`/var/tmp/kotodama-r31-sweep` for the mirror-safety replay rows. Per pass
and row: exit code, stdout SHA-256, stderr byte count, elapsed seconds.
Runner: `.scratch/round-31-o-sweep/reproduce-scribe.py` (outside the repo
tree; sha256 `a9412a1072b298c41b90c02b94f298c4a1e498a4e2f5f7820b3fdcc1f9277de2`).

Provenance note: the scribe rewrote the receipt at 23:25:46Z (a post-md
re-run; the md §6 footer therefore quotes the pre-rewrite digest
`c794d6a5169d7c5b…`, stale against the filed bytes). This seat's comparison
is against the filed post-rewrite bytes; the per-row recorded digests are
identical across the rewrite except the two volatile rows' timing fields.

## Result

- **Green-surface rows: 50/50 exit 0 in all 3 passes — 100% green, deterministically.**
- **Control rows: 13/13 at their recorded expected codes in all 3 passes** (filed-red generations stay filed-red;
  reproduction is not clearance).
- **stdout digest identical to the recorded digest in all passes: 48/50 green rows + 13/13 control rows = 61/63 rows.** stderr was 0 bytes on every row of every pass.
- 48/50 green rows are even byte-stable across
  passes with no normalization. The digest deltas vs the recorded receipt
  are confined to the two known-volatile families, below.

### Rows whose stdout digest differs from the recorded one (volatile class)

| row | exits | observed stdout sha256 (pass 3) | recorded stdout sha256 | volatile field |
|---|---|---|---|---|
| battery | 0/0/0 | `30fbf1adfc2182c7…` | `5e5727078bd50c14…` | per-gate `"seconds": <float>` timing fields |
| pin-repoint-selftest | 0/0/0 | `386b5521b62f5372…` | `a0c2b34b6e3afa9a…` | embedded `"date": "<ISO-8601>"` snapshot timestamp |

Evidence that the deltas are timing-only and not behavior: back-to-back
runs of the same commands on this seat produced byte-identical output
except for those fields (battery per-gate `seconds`, pin-repoint `date`),
and with those fields normalized the three passes converge to one digest
(`sweep-receipt` normalized hashes: 51/51 stable ×3). The round-31 auditors
independently filed the same two volatile families as F1 (`battery`) and
F2 (`pin-repoint-selftest`) in `sweep-audit-O09O10.md`. Exit codes match the
recorded receipt on every pass of every row.

## The independent seat matrix (beyond the manifest)

Before reproducing the manifest, this seat ran its own 3-pass matrix of
51 legs (adds: `typed-pipeline-gate` on the d2 **typed** packet,
`source-audit-inventory.py --selftest`, `--json --summary` without
`--root`, and the r28 sweep selftest as a hygiene leg): **51/51 exit 0 ×3,
all normalized output hashes stable ×3; 48/51 byte-stable even raw** (the
three exceptions are the volatile class above plus
`source-audit-inventory --selftest`, whose temp-dir random suffix is
normalized). Receipt: `.scratch/round-31-o-sweep/sweep-receipt-202325.json`.

### One deterministic red outside the manifest, diagnosed and superseded

`python3 -B reports/round-28/sweep/sweep.py --selftest` (filed round-28
artifact) exited 1 ×3 on this seat: control `r28-generation-replays-green`
reads `mismatch ×4` because its pinned `r28-post` generation was superseded
4/4 by the round-30 QREG landing (typed-pipeline-gate refuses the pinned
packet snapshots: `FAIL L1-assembler: packet bytes … are not the assembler's
deterministic assembly`). Direct runs of all four gates on the current
packets are green. This is the pin-cascade class the r28 sweep itself
predicted; the scribe seat's successor generation
`reports/round-31/sweep/frozen/r31-post/` (replay `REPLAY OK: 4/4`, row
`replay-r31-post`) supplies the missing successors — but the filed round-28
selftest still asserts the old generation and therefore stays red until the
parent lands a successor selftest or files a disposition. Filed artifact,
immutable; documented, not counted in the green denominator. Neither the
scribe's §3 control table nor the O09/O10 audit matrix covers this selftest
leg; this fragment is its round-31 disposition record.

## Reproduce

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
# the scribe manifest, re-runnable from the recorded commands alone:
cat reports/round-31/sweep/commands.txt   # execute each line; mirror-safety
                                          # replay rows: TMPDIR=/var/tmp/kotodama-r31-sweep
# this seat's three-pass comparison against the recorded receipt:
python3 -B .scratch/round-31-o-sweep/reproduce-scribe.py
```

## Write boundary

Only `reports/round-31/final-sweep-reproduction-O06-O08.md` (this file) was
written inside the repo; runner and receipts live in `.scratch/` (git-ignored).
No filed round-8..30 byte, no sibling round-31 artifact, no shared tool was
edited. No git commit, no push.
