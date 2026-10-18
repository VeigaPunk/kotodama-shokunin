# R23-O01..O04 — controls

Date: 2026-10-18. Every count below carries its command and date. Raw
receipts: `evidence/selftest-receipt.json`, `evidence/check-receipt.json`,
`evidence/tie-break-check-receipt.json`. All runs used an isolated clone
(`.scratch/r23-wording/clone`, HEAD `7b181a52eb74319e5e5c40cdb1f0a1a1dc652079`,
created with `git clone --shared --quiet .`), `TMPDIR=$PWD/.scratch`,
`PYTHONDONTWRITEBYTECODE=1`. No historical validator was executed against the
live worktree.

## A. Rule intact — the frozen placeholder rule still bites (selftest, 28/28)

Command: `python3 reports/round-23/wording/wording-check.py --root
.scratch/r23-wording/clone --selftest --receipt .scratch/r23-wording/selftest.json`
→ **exit 0, 28/28 controls passed**, 2026-10-18 (~12:24 local).

- `frozen-placeholder-re-unchanged` — the round-20 module's `PLACEHOLDER_RE`
  pattern and flags equal the filed round-15/16/20 definition, byte for byte.
- `placeholder-still-caught:*` (6) — `review pending, see above`, `this basis
  is TBD`, `placeholder row`, `copy of the v2 row`, `todo: fill`, `the D2
  output is unchanged` — all still match. The rule's full vocabulary,
  including the standalone word `unchanged`, is intact.
- `old-basis-triggers-frozen-rule`, `old-judgment-flags-placeholder` — the
  parent packet's D4-CL08 basis, parsed by the frozen `parse_ledger_rows`,
  still matches and still yields the `placeholder basis` problem: the false
  positive is reproducible at the rule level, not just in a stale log.
- `new-basis-clean-under-frozen-rule`, `revision-judgments-clean` — the
  reworded revision's D4-CL08 basis matches nothing, and no row of the
  revision's ledger yields any judgment problem.
- `ledger-shape-unchanged`, `statuses-unchanged` — parent and revision parse
  to the same 27 claim ids in the same order with the same statuses
  (16 supported / 7 partial / 4 unresolved).
- `revision-is-parent-plus-declared-delta` — the revision bytes reconstruct
  exactly from the parent bytes by the declared one-phrase reword plus the
  provenance note (`parent.count(old phrase) == 1`, revision contains the new
  phrase once, the old phrase zero times, and `unchanged-foreign-path` only
  inside the note): no other byte differs.
- `revision-pin-matches-live-bytes` — `declared-in-r3/expected.json` pins
  `084dc5db9a8d923bb06a987b0b437bf5bfee3caac2e41cd16743da0c71499250`, the
  live revision's actual sha256.
- `frozen-runner-digest-pinned`, `round22-adapter-digest-pinned`,
  `clone-matches-live:*` (3) — the round-20 runner and the round-22 adapter
  read exactly their pinned digests in both the live tree and the clone; a
  drifted clone is refused before any run.
- Binding-mechanism controls (4) — `binding-selects-pinned-packet`,
  `binding-follows-repin`, `unmatched-pin-refused`, `audit-role-ignores-pin`,
  `outside-candidate-refused`: the pin filters candidates, follows a re-pin,
  fails closed on an unmatched or malformed pin, and the audit role is
  unaffected.
- `installed-selectors-use-successor-paths`,
  `installed-measure-d-has-no-mtime-lookup`,
  `wrapper-binding-reaches-revision-baseline` — after installation, the
  transformed `measure_d` references the successor selector names, contains no
  `st_mtime` lookup anywhere in its code tree (the round-22 determinism
  property), and the wrapper resolves the revision through the new baseline.

## B. Negative reproduction — the filed round-22 command, unmodified

Command: `python3 reports/round-22/fixes/tie-break.py --root
.scratch/r23-wording/clone --check` → **exit 1**, 2026-10-18
15:22:49Z–15:23:30Z, receipt `evidence/tie-break-check-receipt.json`.

Exactly three failures, at HEAD:

1. `claim D: v2 successor row not green: reports/round-20/wart/
   expected-v2-07-r20.json exit 2 — V2F-DIGEST: 1 pinned file(s) changed …
   tools/d2-typed-labels.py` — open tail (successor-pins seat).
2. `claim D: packet reports/round-20/handoff/packet.md claim D4-CL08:
   placeholder basis: '…unchanged-foreign-path control…'` — **the tail this
   seat dispositions**.
3. `claim D: v3 baseline reports/round-20/handoff/expected.json pins packet
   e92f5e67… but the run assembled a97a0f0a…` — open tail (renderer/baseline
   owner).

`filed_rounds_8_21_changes: []` — the run itself changed nothing.

## C. Successor check — the disposition (17/17)

Command: `python3 reports/round-23/wording/wording-check.py --root
.scratch/r23-wording/clone --check --receipt
reports/round-23/wording/evidence/check-receipt.json` → **exit 0, 17/17
controls passed**, 2026-10-18 15:24:18Z–15:26:35Z.

- Negative run (old binding, no injection):
  `negative-control-reproduces-false-positive` — the D4-CL08
  `placeholder basis` failure naming `unchanged-foreign-path` reproduces;
  `negative-control-binds-filed-packet` — the parsed packet is still
  `reports/round-20/handoff/packet.md`; `open-tails-pre-exist-negative-run-
  and-are-not-adapter-caused` — exactly the two declared open tails, no more.
- Positive run (declared-in-r3 binding):
  `positive-control-wording-tail-eliminated` — **zero placeholder findings**
  in the full check; `positive-control-remaining-failures-are-declared-open-
  tails-only` — every remaining failure matches the two declared open-tail
  prefixes and nothing else (undeclared_failures: none);
  `positive-control-parses-revision` — the parsed packet is
  `reports/round-23/wording/declared-in-r3/packet.md`, 27 rows;
  `revision-judgments-clean-in-run` — no judgment problem on any row;
  `census-still-matches-exercise` — packet census equals the e2e v3 exercise
  census (claims=27, statuses 16/7/4).
- Freeze: `filed-rounds-8-22-unchanged` — the rounds 8-22 snapshot is
  byte-identical before and after both full-check runs (changed: none).
- Digest pins re-verified inside the same run (`verify_tree` controls): the
  frozen runner, the frozen adapter, the parent packet, and the revision pin
  all match the live tree and the clone.

## D. Live-tree hygiene

- `git status --porcelain` shows this seat's writes confined to
  `reports/round-23/wording/**` plus the pre-existing sibling modification to
  `reports/round-22/fixes/regression.md` (not this seat's; untouched).
- Rounds 8-22: no file created, modified or removed by this seat (corroborated
  by the in-run snapshot control and by both receipts' zero-change fields).
- `sha256sum reports/round-20/run-validation.py
  reports/round-22/fixes/tie-break.py` (2026-10-18, after all runs) →
  `2b7a252b…46da`, `2856a571…ce0a` — unchanged, equal to the round-20/round-22
  filed pins.
