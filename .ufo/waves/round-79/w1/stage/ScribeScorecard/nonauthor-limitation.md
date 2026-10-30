# Non-author limitation — draft wording for the round-79 SCORECARD section and report (W1, ScribeScorecard)

## Governing rules (read from committed fleet/lane bytes)

- `PROTOCOL.md:59–68` (fleet): a `SHONEN.md` box is checked (`[x]`) only by "a reviewer who did not author the round's
  changes — a fresh lane or integrator review, never self-attestation; a subagent the lane dispatched is still the
  lane"; "any `[x]` carrying no named non-author verifier is author attestation counting as `[~]`".
- `AXES.md` (fleet): an exploratory claim verifies only with "a named non-author reviewer on record (…; a dispatched
  subagent does not count)".

## Committed state at base 44f76d4 (probe `probe.sh` P4, `probe2.sh` Q4)

- `SHONEN.md` boxes: four `[~]`, zero `[x]`, zero `[ ]`.
- Non-author closure records exist: e.g. `corpus/lessons/round-78-verifier-spotcheck.md` (author line: "hyaku closure,
  non-author integrator"); the same form for rounds 50–78. Each of those closures **declines to mark the boxes**:
  round-78 line 72: "none is mechanically checkable by a non-author from this round's evidence alone — a promotion
  review would need a dedicated non-author re-derivation. Promotion remains operator-owned."
- `reports/round-24/promotion-review.md` names ten reviewer seats as non-author. The dossier's own header states the
  seats were part of a 16-worker GLM swarm dispatched by the lane's regimen. Under the rule above, a lane-dispatched
  subagent is still the lane. The round-24 SCORECARD calibration row (`SCORECARD.md:300`) therefore overstates the
  non-author status of those reviews, and this round does not rely on it.

## Draft paragraph (for the round-79 SCORECARD section)

No `SHONEN.md` box is `[x]`. Every box stays `[~]`: the lane asserts it, and no reviewer outside the lane checked it.
The round-24 "non-author" dossier is not counted as non-author verification: its ten reviewer seats were dispatched
by the lane (`reports/round-24/promotion-review.md` header), and the fleet rule states that a dispatched subagent is
still the lane. Later non-author closure records (rounds 50–78) do not mark any box and say the boxes are not
mechanically checkable by a non-author from their evidence. Every round-79 seat that touches claims O or Ca —
ExecGuard, ExecOCounter, ExecCaCounter, the Rev/Crit/Mut/Sentinel/Conn/Scout/Scribe seats — is lane-dispatched. So
any "independent" verdict in this round means independent of the seat that implemented the item, inside the lane. It
is an author-side verdict and carries no non-author weight. Promotion is operator-owned and is not available from
this round.

## Wording rules for W1 documents (apply to every seat's text that reaches the SCORECARD or the report)

1. Replace "independent acceptance counter" / "independent verifier" with "separate counter (lane-dispatched)" unless
   an out-of-lane reviewer's name and verdict are on record.
2. Do not write `[x]`, `non-author-verified`, or "promotion-ready" for any box or claim from round 79.
3. Name the verdict's basis: "author-side, lane-dispatched seat <name>" or "non-author closure <file>". No third
   category.
4. O and Ca verdicts are `pending` until their counters run at a lands revision; a "pass" in a selftest is a capability
   fact, not a measurement (PROTOCOL §Evidence standard: "Self-test green is capability, not a measurement").
5. An exploratory claim is not declared in round 79. Neither O nor Ca is an exploratory claim as drafted; declaring
   either as exploratory would require a named non-author reviewer on record, which does not exist for this round.

## Limits stated

- The fleet root is a git repo at `/home/vgpnk/Projects/shokunin`; the rule text was read there (`git show`), not from
  a copy in the lane. The `git log -S` dates in `findings.md` §4 give first introduction of each sentence, not the
  date each round read it.
- "Lane-dispatched" is read from prose in the round-24 dossier and from the regimen naming "16 workers". A dispatch
  record (roster, transcript) was not opened by this seat; that check is review-only.
