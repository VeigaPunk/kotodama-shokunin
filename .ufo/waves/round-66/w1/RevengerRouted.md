# RevengerRouted — ROUTED-INTENT (claim Ca): §5 operative sentences vs declared legs

seat: L1-kotodama-r66.RevengerRouted · 2026-10-24 · milestone r66-v2 · judged on: calibration

Method: source of truth is `corpus/lessons/round-65-verifier-spotcheck.md` §5 **alone** (lines 76–79).
Compared against the declared legs in `reports/round-66/claims.json` (lines 80–85) and the
enforcing code in `reports/round-66/accept-ca.py`. Verdict per defect: satisfies / over-reaches
(edits filed bytes) / misses. Pre-data honesty cross-checked against
`reports/round-66/telemetry/dry-run-ca.txt` + `controls-ca.txt`.

---

## R65-D1 — verdict: **satisfies** (with one bypass surface, below)

Operative sentence (lesson:76):
> "repair S753's source cell — re-capture the Penn Museum PDF (or cite a live-resolving
> mirror/DOI); today neither the live URL nor the committed capture returns the quoted bytes."

Declared leg (claims.json:80): receipt records live 200 pdf + quote verbatim + fresh capture
replay; games entry cites S776 exactly once for the mancala bullet, S753 zero times.
Implementation (accept-ca.py:88-106): checks `"200"`, `"application/pdf"`, the hardcoded mancala
QUOTE, capture ts `20261024111013`, and `S776` in the receipt; counts `\((S776|S753)\)` in
`corpus/knowledge/culture-material/games-play-sport-contests.md` (must be 1 / 0).

- Takes the routing's live-resolving-alternative branch (S776 fresh capture as supersession) and
  additionally repairs the *consumer* (the entry that carried the dead anchor) — coherent with the
  routing's goal that the quoted bytes resolve; not over-reach: no round-65 filed byte is edited.
- Base dry-run (`dry-run-ca.txt`) shows `s753_citations=1` at base — the supersession target is
  real, the leg is data-sensitive, and the control honestly fails all legs at 94209e8f.

Bypass surface (attack, unresolved by this leg): the leg never reads `corpus/SOURCES.md`, so
S753's own source cell may stay untouched (404 URL + dead capture `20250926172224`) while D1
prints PASS. Claim C's registry legs cover S776's row shape but nothing pins S753's disposition.
Secondary weaknesses: `"200" not in d1` is a bare substring (any number matches); the receipt is
self-authored text — a false stamp passes; the capture's *replay* is asserted in the receipt and
never re-derived by any leg.

## R65-D2 — verdict: **satisfies**

Operative sentence (lesson:77):
> "receipt sequencing — records commits must be direct children of the lands commit they receipt
> (criterion 17 already covers the leg; the process ordering is what failed). Consider making the
> receipt leg's expected lands hash the actual parent at run time."

Declared leg (claims.json:81). Implementation (accept-ca.py:108-142): for each round-66
`final-measures-{c,o,ca}.txt`, extracts the stamped `measured revision`, resolves the carrier via
`git log -1 --format=%H main -- <receipt>`, requires `git rev-parse carrier^ == stamped`, and
resolves `stamped^{tree}` against the receipt's `tree:` line plus the counter's current sha256
against the receipt's `counter sha256 (self):` line.

- This is exactly the round-65 failure mode (receipts stamped `3b1b5a67` carried by a commit whose
  parent was `53a60275`/`29d0b0fc`): parent==stamped FAILs on any interposed commit.
- The routing's "actual parent at run time" suggestion, taken literally, would be vacuous (actual
  parent always equals itself). The implementation chose the non-vacuous strict form — correct
  generalization. Counter-sha is checked against the *current* counter bytes, killing stale
  receipts produced by an older counter. No history rewrite, no round-65 byte edits — forward-only
  dispositioning, as the routing demands ("the process ordering is what failed").

## R65-D3 — verdict: **misses** (partial: last-error clause declared but unimplemented)

Operative sentence (lesson:78):
> "dispatch the L2 wave or record the refused/errored dispatch evidence — a prepared taskcall does
> not satisfy the ≥8 batched-seat floor; retain per-seat last-error text for dead seats."

Declared leg (claims.json:82): "…with per-seat status **and last-error text for dead seats**".
The counter's own docstring promises it (accept-ca.py:19-20: "dead seats carry a last-error line").
Implementation (accept-ca.py:144-153): requires ≥8 `.ufo/waves/round-66/*.md` paths named in
`telemetry/seat-evidence.txt`, all existing on disk (`os.path.isfile`), named==existing, plus one
case-insensitive match of `(seat|report|status)` anywhere in the receipt.

- What is enforced: the ≥8 floor via existing round-scoped seat reports — a real proxy for
  dispatch this round (this wave did dispatch; files exist).
- What is missed: **no code path inspects last-error text or dead seats at all.** A receipt listing
  8 live seats and 3 dead seats with no error lines passes; the `(seat|report|status)` regex is a
  any-word-anywhere shortcut, not a status-line check. The declared instrument (claims.json:82)
  and the enforcement (accept-ca.py:144-153) diverge — the exact false-stamp surface this round
  exists to close. Second gap: the routing's disjunct branch "or record the refused/errored
  dispatch evidence" has no implementation (moot while the wave dispatches, but the instrument
  would hard-fail an honestly refused dispatch instead of accepting its evidence).

## R65-D4 — verdict: **satisfies**

Operative sentence (lesson:79):
> "bound `check-claim-separability.py` so it returns a verdict inside a round, or replace it — a
> 600 s timeout leaves separability permanently unverified."

Declared leg (claims.json:83). Implementation (accept-ca.py:156-161): `telemetry/separability-real.txt`
must contain `^SEPARABILITY: \d+ findings$` and `acceptance_runs=\d+` and must NOT contain
"PARTIAL" anywhere.

- Satisfies the records half of the routing's disjunction: this round's real manifest run returned
  a *complete* verdict inside the round, evidenced by committed bytes. The tool-bounding
  capability itself is claim O's subject (claims.json:36-45 legs BOUND/STATIC/MAXRUNS/MUT), so Ca
  correctly does not double-duty it; demanding a non-partial verdict here is a stricter, honest
  calibration assertion, not over-reach (no filed byte of round-65 is touched).
- Residual (attack): "produced inside the bounded run" is not evidenced by the receipt — no
  duration/budget stamp is checked, so a receipt from an unbounded run is indistinguishable. A
  `budget=`/elapsed field checked against the receipt would close it.

Non-D1..D4 legs (CRITERION claims.json:84 / accept-ca.py:163-168; QUOTES claims.json:85 /
accept-ca.py:170-180) are additions beyond the four routed defects, in the safe direction (extra
legs only make PASS harder; they append QUALITY criterion 18 and a new round-66 lesson, editing no
round-65 bytes). One weakness noted: QUOTES counts ids `S776-S800` anywhere in the lesson file,
not inside its `## Gate` section (accept-ca.py:172-176) — the docstring's "Gate names the round's
ids" is under-checked.

---

## Summary

| defect | verdict | key evidence |
|---|---|---|
| R65-D1 | satisfies (bypass surface noted) | lesson:76 · claims.json:80 · accept-ca.py:88-106 |
| R65-D2 | satisfies | lesson:77 · claims.json:81 · accept-ca.py:108-142 |
| R65-D3 | **misses (partial)** — last-error clause unimplemented | lesson:78 · claims.json:82 · accept-ca.py:19-20 vs :144-153 |
| R65-D4 | satisfies | lesson:79 · claims.json:83 · accept-ca.py:156-161 |

No defect's disposition over-reaches: no leg requires editing round-65 filed bytes; D2 constrains
only round-66 receipts' ancestry. Pre-data controls honest (dry-run-ca.txt: all six legs FAIL at
base 94209e8f; controls-ca.txt records the do-nothing control). Fix for D3 is one clause: fail D3
when a seat's status is dead/errored and no last-error line follows it.

Tooling directive record: no tools installed or upgraded (none needed; read-only analysis).
Time-box: returned inside budget; dependencies: none blocking — L1 note: D3's declared/enforced
divergence should be fixed before ACCEPT-CA-66 is stamped, else the counter blesses the exact
round-65 dead-seat disclosure failure it was routed to prevent.
