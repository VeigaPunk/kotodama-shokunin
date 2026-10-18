# R23-O01..O04 — disposition: reword D4-CL08's basis + re-pin the packet as declared-in-r3

Date: 2026-10-18. Seat: round-23 wording. NON-CANON engineering evidence; not a
lore receipt. Root cause and the routing decision are in `analysis.md`; every
control with its command and count is in `controls.md`.

## What landed (all new files, all under reports/round-23/wording/)

- `declared-in-r3/packet.md` — sha256
  `084dc5db9a8d923bb06a987b0b437bf5bfee3caac2e41cd16743da0c71499250`, 107,119
  bytes. Parent: `reports/round-22/handoff/declared-in-r2/packet.md` (3.1.1,
  sha256 `a97a0f0a0a497cb4410124607065df7686bbc7f78b4b46bdaaaa1d66ba4d1b6e`).
  Delta, proven byte-for-byte by the control
  `revision-is-parent-plus-declared-delta`: (1) exactly one phrase of the
  D4-CL08 uncertainty basis reworded — `the unchanged-foreign-path control is`
  → `the foreign-path-stability control is`; (2) a provenance note after the
  renderer paragraph declaring the supersession, the reason, and the pin. No
  claim status, link, count, edge row or other basis changes; the 27-row
  ledger parses to the same ids and the same 16/7/4 status sequence as the
  parent (control `ledger-shape-unchanged`, `statuses-unchanged`).
- `declared-in-r3/expected.json` — the new baseline pin row: `packet_sha256`
  of the revision, parent path + digest, the delta, the reason, and the
  binding contract (the `packet_sha256` key, mirroring
  `reports/round-20/handoff/expected.json`).
- `declared-in-r3/freeze.txt`, `declared-in-r3/run.log` — frozen digests,
  commands, dates, verdicts; explicitly marked as frozen by
  `wording-check.py`, not by the renderer exercise.
- `wording-check.py` — the round-23 wording successor. In an isolated clone
  under `.scratch` (isolation enforced, same rule as the round-22 adapter) it:
  verifies the frozen digests of the round-20 runner and the round-22
  `tie-break.py` adapter and refuses on drift; installs the round-22 selectors
  unmodified and rebinds only the packet-role baseline to
  `declared-in-r3/expected.json`, injecting the revision into the candidate
  set; then runs the full historical check twice — once on the old binding
  (must reproduce the D4-CL08 placeholder failure and must not gain or lose
  the two open tails) and once on the revision binding (must show zero
  placeholder findings, with any remaining failures matching the declared
  open tails only). Rounds 8-22 are snapshotted before and after and must be
  byte-identical. `--selftest` carries 28 unit controls; `--check` carries 17.
- `evidence/{selftest,check,tie-break-check}-receipt.json` — the three run
  receipts (selftest 28/28; check 17/17; the unmodified filed round-22
  `tie-break --check` reproducing the three-failure negative state at HEAD).

## Why no rule is weakened

- The frozen validators are not edited: `reports/round-20/run-validation.py`
  still reads sha256
  `2b7a252b5449415dddac2e667ed2e192df800a80173849989fa72423961646da`, the
  round-22 adapter still reads
  `2856a571da286b62b4eced7da610f5cebd46f3504bdf2f6dd8a53d60272dce0a`, and both
  digests are pinned inside `wording-check.py`, which refuses a drifted clone.
  `PLACEHOLDER_RE` is byte-identical in rounds 15/16/20.
- The controls re-exercise the frozen rule instead of trusting it: six
  placeholder fixtures (`TBD`, `see above`, `placeholder`, `copy of`, `todo`,
  standalone `unchanged`) must still match; the old D4-CL08 basis must still
  be flagged by `PLACEHOLDER_RE` and by `uncertainty_problems`; the reworded
  basis must be clean. A successor that had widened the regex could not pass
  these.
- The binding mechanism is the round-22 successor's own (baseline
  `packet_sha256` filters candidates before ranking). The pin value moves to a
  new revision row; the rule "parse the pinned packet" is applied unchanged,
  and the control `unmatched-pin-refused` proves a wrong pin still fails
  closed.

## Why the reword is inside the uncertainty grammar

The basis keeps the grammar's shape: `grounding: …` evidence language naming
files, run receipts, counts and a pinned digest — the same
status (`supported`), the same links, the same evidentiary content. `stability`
is the property the old compound named: the two controls (50/50 projector
selftest, 13/13 gate legs, stdout digest `9a69985a…` equal to the round-18
pre-generalization baseline) hold the foreign D2 path byte-stable while the D4
leg runs. No placeholder vocabulary remains in the basis; no new claims are
added; nothing is deleted.

## Result against the round-23 claim

- (a) The wording false positive is dispositioned on the preferred route:
  reword within the uncertainty grammar, packet re-pinned as a new revision
  (declared-in-r3), full successor check run with both bindings — the
  placeholder tail is gone (`positive-control-wording-tail-eliminated`,
  zero placeholder findings), the revision parses clean
  (`revision-judgments-clean-in-run`), and the census still matches the e2e
  exercise (27 rows, 16/7/4). The v3 exercise itself and the v2 frozen surface
  were already green and are untouched.
- Declared open tails (not this seat's; visible in both runs and asserted to
  be unchanged by this seat): (1) `claim D: v2 successor row not green …
  V2F-DIGEST … tools/d2-typed-labels.py` — the v2 successor row still pins the
  pre-family-clean projector digest; the re-row belongs to the round-23
  successor-pins claims (O-before (b): "combined successor pins … v2 …");
  (2) `claim D: v3 baseline reports/round-20/handoff/expected.json pins packet
  e92f5e67… but the run assembled a97a0f0a…` — the round-20 baseline pin
  predates the renderer default's move to declared-in-r2; re-pointing it is
  renderer/baseline-owner work. Both are data re-points of the same shape this
  seat demonstrates for the packet pin. They pre-exist in the negative run and
  the controls assert this seat neither created nor repaired them.

## Limits / handoff

- The renderer still renders 3.1.1 and the e2e frozen baseline still verifies
  the declared-in-r2 packet+twin pair; nothing in `tools/` or under
  `reports/round-{8..22}/` changed (zero-byte-change controls). Folding the
  reword into a future renderer revision, re-freezing that baseline, and the
  twin's basis supersession remain renderer-owner work.
- The D-axis family-clean rule for `SKILL.md` is a different seat; nothing
  here touches `SKILL.md`.
- No git commit/push was performed; LOG.md integration is the parent's.
