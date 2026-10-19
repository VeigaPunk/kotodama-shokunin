# O01 — append-only ledger census (claim O, operability)

Read-only audit. For each closed round dir, post-landing modification/deletion
commit count via `git log --diff-filter=MD -- <dir>`:

| round | landing commit | post-landing M/D commits |
|---|---|---|
| 33 | da68a6d | 0 |
| 34 | 4a7aede | 0 |
| 35 | ce103bf | 0 |
| 36 | 57c8409 | 0 |
| 37 | fa90c77 | 0 |
| 38 | dfb0719 | 0 |
| 39 | fd55e1f | 0 |
| 40 | 13a1657 | **2** (see below) |
| 41 | ac47c78 | 0 |
| 42 | 7ceff59 | 0 |
| 43 | c9f4eaa | 0 |
| 44 | 1dfb87f | (current round excluded — self) |

## The two r40 modification commits — both recorded supersessions, not corruption

- `456674d` "round-40: final receipt refresh … supersedes 8b7b4508" — the
  authorized `REFRESH_RECEIPTS=1` closing-snapshot refresh; M on
  `reports/round-40/validation.json`, `run-validation.py`, `op/defect-queue-v2.json`.
- `ac47c78` (round-41's commit) touched `reports/round-40/op/defect-queue-v2.json`
  in place — the documented r41 amendment flipping N7 + r39-runner-root-regression
  to `fixed-with-evidence` and appending `r41_update` (recorded by r42 O08 and the
  r43 queue successor, which pins the parent sha `dfc9265d…` to detect further drift).

Neither is a filed-byte rewrite of a closed finding; both are recorded
supersession/amendment acts consistent with the append-only ledger's
correction-via-successor rule, though the in-place `defect-queue-v2.json` edit is
the known soft spot the successor-pin mechanism now guards.

## Receipt integrity — every round's validation.json present + committed

33 `da68a6d` verdict True · 34 `4a7aede` True · 35 `ce103bf` True · 36 `57c8409`
False · 37 `fa90c77` True · 38 `dfb0719` True · 39 `fd55e1f` True · 40 `456674d`
True · 41 `ac47c78` True · 42 `7ceff59` False · 43 `c9f4eaa` rejected-honest-stop ·
44 `1dfb87f` rejected-honest-stop. All 12 receipts present, committed, parse clean.

Verdict: claim O verified — append-only holds (the two r40 edits are recorded
supersessions); all 12 receipts intact; working tree clean; local-first explained
(unpushed commits are the operator's pending push, not a violation).
