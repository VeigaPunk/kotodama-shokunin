# RevCounterO — Round 63 wave 1 counter robustness review (claim O, `reports/round-63/accept-o.py`)

Seat: `kotodama-r63-w1-RevCounterO` (leaf, no delegation). Scope: false-verdict audit of the
frozen counter `reports/round-63/accept-o.py` (731 lines; the source of every line number below)
against the claim O predicate and docstring. Mutations/demonstrations were run in PROBE copies under
`/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-RevCounterO/` (never in the lane repo).

Verdict: **the counter is broadly sound; two concrete false-PASS defects are demonstrated (REVIEW,
TIMEOUT), plus minor residual risks.** No false-FAIL defect found against a compliant tool.

---

## Findings by severity

### HIGH — REVIEW leg does not implement its own documented "open finding fails" condition (lines 705-717 vs docstring 84-88)

- Docstring (lines 87-88): "a review that records an open finding, or a missing/dead review, fails
  this leg." `claims.json` kill_rule repeats it: "a finding left open ... fails the claim."
- Code (lines 708-716) checks only file existence + substring presence of `VERDICT: NO-OPEN-HIGH-MED`;
  it never scans for open findings. A review file that contains the token **and** an explicit open
  HIGH finding passes.
- **Demonstrated (PROBE A):** fabricated `RevToolB.md` and `rev-hold-lift.md` containing the token and
  "OPEN FINDING (HIGH): scheme-relative redirect Locations are not covered by any counter fixture …"
  → leg condition `clean=True, missing=[], present=4/4` → REVIEW PASS.
- Consequence: the leg is gameable by a token-only stub, and it contradicts the counter's own frozen
  semantics. The token is also a fixed, known constant, so any file quoting it (e.g., a review that
  *discusses* the required token) passes.
- Mitigation argument (why presence + closure re-read still has value): the named review seats are
  independent processes, and the main-agent closure re-reads the reports; the token is a weak but
  non-trivial coordination marker. That does not rescue the documented semantic, which the code
  should implement (e.g., also reject bodies matching `OPEN FINDING`/`FINDING OPEN`/`residual` with
  HIGH/MED severity). Recommend the counter be revised to enforce that, or the docstring be amended
  to state presence-only (a revision is permitted only before the first full run on the claimed
  object — flag this before the control run).

### MED — TIMEOUT leg cannot distinguish a `--timeout`-governed wall budget from a fixed socket timeout (lines 663-703)

- The leg asserts only (line 698): `exit==1`, `rows == [(sid, "UNREACHABLE", 3)]`, `wall < 45`,
  no Traceback. It never verifies that the `--timeout 4` budget actually applied (no per-attempt
  timing; server-side request timestamps are recorded in `fx.times` but unused here).
- **Demonstrated (PROBE B):** a stub tool that **ignores `--timeout` entirely** and uses a fixed
  10 s per-socket timeout produced `ROW S7777 UNREACHABLE attempts=3 url=-`, exit 1, wall=30.1 s,
  no Traceback → every leg condition true → TIMEOUT PASS. Each attempt actually ran ~10 s, not the
  claimed 4 s budget.
- The base round-62 tool (`65b393e`, `FETCH_TIMEOUT = 30.0` fixed, line 104) *would* fail this leg
  (3×30 s ≈ 90 s > 45), so the leg does discriminate the base defect — but any repair that drops a
  default ≤ 14 s and never implements the flag passes. Fix suggestion: reuse the burst-spacing trick
  from DEFAULT (lines 540-542) on the stall path's timestamps (≤ ~5 s between the three requests),
  or lower the wall bound to ~16 s for 3×4 s budgets, or add a `--timeout 1` probe (wall < ~10 s).

### LOW — DEFAULT window and schedule tolerances are adequate but load-sensitive (lines 527-547)

- Window 100-600 s vs worst-case compliant run ≈ 118-170 s (2 gap intervals × 55-75 s + 2 burst
  intervals × 4-10 s + service). Lower bound has ~2-4 s effective margin; a pathological host that
  stretches a single request past 15 s breaks the `55 <= gap <= 75` check (line 542) → false FAIL.
  Local loopback makes this unlikely; acceptable. Note only.

### LOW — TRUNC pad margins are thin at the random-word minimum (lines 323-330, 650-651; cap line 161)

- `pad = (12 words + ". ") * 70000`; minimum word length 4 → 61 B/iter → 4,270,000 B vs cap
  4,194,304 B (margin 75,696 B, ~1.8%). Verified both TRUNC_FAR (quote offset > cap) and
  TRUNC_NEAR (quote inside first bytes) hold for all random word lengths. Correct today, but any
  tightening (e.g., `words(11)`, cap growth) silently breaks the leg; worth a comment or a fixed-size
  pad.

### INFO — REDIRECT two-server setup is sound (no 127.0.0.1 resolution ambiguity; lines 568-596)

- The source `fx` and target `fx2` differ **only by port** (both bind 127.0.0.1). "Authority
  differs" for any correct host+port comparison; a host-only comparison (the defect the repair must
  close) would fetch the target → `hits_target=1` → leg FAIL. No DNS/IDNA/IPv6 ambiguity exists on
  127.0.0.1. The leg genuinely detects the base tool's auto-follow (would print LOCATED attempts=2).
  Scheme-relative Location, userinfo-host, IPv6-literal and IDNA forms are review-only per claims.json
  — correctly not in fixtures.

### INFO — GEN's REDIRECT_LOOP l1=3/l2=2 is deterministic, not overfit (lines 144, 316-320)

- Trace under the stated rule ("at most 5 requests per chain; a redirect received on the 5th
  response ends the URL as fatal"): req1 live(302)→req2 other(303)→req3 live(302)→req4 other(303)→
  req5 live(302) = fatal ⇒ l1=3, l2=2, attempts=5. Every compliant tool hits exactly this
  interleaving; deviating tools (cap<5, 303-not-followed, cross-authority refusal even under
  --allow-private) fail the leg as intended.

### INFO — INDEP forbidden strings (lines 398-399) — no current false-FAIL, one forward risk

- `grep -cE 'reports/|accept-o|round-63|Fixture|REOPEN_HOSTS' tools/reopen-row.py` at current lane
  head = 0; the tool text contains none of them. 'Fixture' is case-sensitive, so the tool's own
  "--selftest built-in offline fixtures" wording (lowercase) is safe. Only risk: a *repair* that
  annotates "round-63" or "reports/…" in a docstring/comment would false-FAIL the leg; the repair
  draft must keep those strings out (worth a note to the executor).

### INFO — ERR "no-id" pins exit 2 for an empty id list (lines 551-552); consistent with the docstring's "round-62 behaviour unchanged" framing — a deliberate contract pin, not a defect.

---

## Residual risk / verification gaps

1. REVIEW leg semantic gap (HIGH) is the only finding that can pass a *materially wrong* gate; it is
   partially compensated by the named independent seats and the closure's re-read, but the counter
   should be fixed or its docstring amended before the first full run.
2. TIMEOUT false-PASS (MED) lets a flag-ignoring-but-bounded repair pass claim O item 5; the LIVE/
   closure behaviour on real rows is explicitly out of scope (review-only) and will not catch it
   either.
3. No false-FAIL found for a compliant tool: INDEP strings absent, pad margins positive,
   schedule/window tolerances hold, redirect authority comparison unambiguous.
4. Verification gaps: I did not run the full counter end-to-end (it requires the repaired tool and
   the four REVIEW artifacts; the control receipt run belongs to the Ctl/Mut seats at the measured
   revision). All findings are derived from static reading of the counter source plus isolated
   PROBE executions reproducing the exact leg assertions (probe_A_review.py, probe_B_timeout.py in
   scratch; both reproduced the relevant accept-o.py lines verbatim).
