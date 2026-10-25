# RevReceiptHeader — K71-7 re-stamp design (round 72, w1)

Seat: L1Kotodama72.RevReceiptHeader (leaf; no delegation, no background jobs).
Deliverable: `/tmp/r72-castamp/receipt-ca-64da9e14.txt` (1417 bytes, sha256
`3ede8cde1f52b5e108da1364dfbc1279f8815ae3a396a0ead790435437bb9e6d`) — the L1 appends it under
`reports/round-71/telemetry/` (measures-ca.txt).

## Ground truth (K71-7 CONFIRMED, verified by hash, not by citation)

- `git cat-file blob 64da9e14:reports/round-71/accept-ca.py | sha256sum` →
  `f706aacd001ee5448ef9f32f8dc2d5bdd90839e8f3811311819fe3791fee9a3e` — matches the spotcheck
  (`corpus/lessons/round-71-verifier-spotcheck.md` :75) and the preserved previous header at
  measures-ca.txt :9. Spotcheck verified, not assumed.
- Same blob at HEAD → `1ce25fb9ade45c263ba8ddec32f4fb73492ee5f0e82ef2e501bfa975fdcd2517` — the
  counter actually named in the defective top header (measures-ca.txt :1), which first exists at
  `57e0a72`, a descendant of the stamp. Defect mechanism as filed.
- `64da9e14` = `64da9e14e5fa512c7f9c1d7695f48b6d34009b47`; `git rev-parse 64da9e14^{tree}` =
  `ff803f433b07fcbd0f768491af71c915fff5dcb3` — identical to the tree line already in BOTH headers
  of measures-ca.txt; only the counter-sha line was mis-paired.

## Frozen measurement reproduced

- Clone: `/tmp/r72-castamp/lane` (clone of the lane repo, detached at 64da9e14;
  `git status --porcelain` = 0 lines → "worktree dirty (tracked): False").
- Read the counter AT 64da9e14 first: it supports `--root` (argparse :58-60, default "."), prints
  `LEG …` lines + `ACCEPT-CA-71: PASS|FAIL`, exit 0/1. So the sanctioned path (run with
  `--root <clone>`) applies; no shell reimplementation needed.
- Ran `python3 -B reports/round-71/accept-ca.py --root /tmp/r72-castamp/lane` from the clone →
  **6/6 LEG PASS, ACCEPT-CA-71: PASS, exit=0** (V70-1..V70-5 + QUARANTINE 21/21). The lane was
  measurement-healthy at 64da9e14; K71-7 is purely a header-pairing records defect. Output embedded
  verbatim in the deliverable.

## Receipt block design (what the L1 appends)

1. Marker line declaring the round-72 append-only re-stamp with the old->new pairing
   `1ce25fb9@64da9e14 -> f706aacd@64da9e14` and "prior bytes above unchanged".
2. Corrected six-line header — all six prefixes the counter's HDR_LINES convention expects
   (`# counter sha256`, `# stamped revision`, `# evaluated revision`, `# measured revision`,
   `# tree`, `# worktree dirty`): stamped/evaluated/measured = 64da9e14, tree ff803f43…,
   counter sha256 (self) = f706aacd…, dirty False. (Assignment prescribes measured = 64da9e14;
   this re-measures at the records commit in a materialized clone, QUALITY 19 protocol.)
3. Protocol + reproduction comment lines (counter blob sha, exit 0) and the verbatim counter
   output ending in `ACCEPT-CA-71: PASS`.

Append guidance: append the file verbatim below the existing content; do NOT rewrite the defective
top header in place — the in-place rewrite is exactly the round-70 anti-pattern (`f5c845b`,
`27db4ce`) that wave-2 flagged as breaking byte preservation. The defective header stays as
preserved evidence; the appended block is the correction. Satisfies the CASTAMP leg as worded
("an appended receipt re-stamps measures-ca at 64da9e14 with its true counter sha f706aacd").

## Findings by severity

- **Blocking: none.**
- Info 1 — tally-neutrality: the 64da9e14 counter prints no PRESENT/REFUSED/UNVERIFIABLE tally
  (`rows=21 unique-ids=21 labels-ok=True`), and the 64da9e14-era verdicts table is 10/6/5
  (counted in the clone). The hand-written `(10/6/5)` in the old receipt section was true for its
  stamp; the 10/7/4 drift (K71-6) belongs to the 57e0a72 re-derivation. The re-stamp therefore
  restates no tally — importing 10/7/4 into a 64da9e14-stamped block would mis-pair a second time.
- Info 2 — `--lands` exists at the 64da9e14 counter but is parsed-not-graded; irrelevant to this run.
- Info 3 — `tools/check-receipt-seq.py` grades the worktree/HEAD counter, not the stamped one
  (wave-2 RevCounterCa :49; cited, not re-verified here), so this appended block — not the sha
  leg — is the durable evidence of the corrected pairing.

## Residual risk / verification gaps

- The round-72 grader (`reports/round-72/accept-ca.py`, CASTAMP leg) is not yet in the lane at my
  read time; I could not verify how CASTAMP is graded. The block is designed to satisfy the leg as
  literally worded and carries all six header lines should the grader reuse the header-distribution
  check. Appending the block cannot break the round-71 counter's legs (it reads only round-70
  receipts + quarantine-verdicts.md).
- The L1 performs the append; per leaf bounds I mutated nothing under the lane except this report
  file. Lane jj/git state untouched (clone is read-only on the source repo).

## Tooling

No installs (git + python3 preexisting; pacman paused host-wide — untouched). Scratch confined to
`/tmp/r72-castamp/` (clone + receipt deliverable).
