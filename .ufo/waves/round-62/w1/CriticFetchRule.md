# CriticFetchRule — bounded fetch review

Scope: advisory review of D's LOCATE treatment, at assigned revision `f0173481047a93c46798f90b68d71d4f169d2642`. No claim adjudication, source reopening, counter execution, implementation edits, or second runtime invocation.

## Axes

- **Depth:** the fetch rule must describe the actual error classes and fallback behavior.
- **Operability:** bounded attempts and recovery from an isolated failure, without indefinite waiting.
- **Calibration / freshness:** distinguish a temporarily unreachable sound source from a located source; never turn fetch failure into provenance.

## Finding

**The rule protects against an isolated failed request when another eligible attempt can retrieve the quote; it does not make one transient outage episode unable to decide D.** A listed capture is an alternative route, not an independently available service. With an origin consistently blocked, Wayback remains the sole working route and one archive outage spanning the three passes still decides LOCATE.

Importantly, **403, DNS failure, and timeouts are not retried inside `fetch()`, but D retries them through its outer passes.** Saying that these classes receive no retry at all would misread the counter.

### Evidence: exact behavior

`reports/round-61/reopen-quote.py`:

- Lines 81–96: `fetch()` makes at most three attempts, with a 120-second `urlopen` timeout. Only `HTTPError` is caught for the inner retry.
- Line 90's retry set is exactly **429, 500, 502, 503, 504, 508, 520, 522, 524**. It is **not all 5xx**. For example, 501 and 521 receive one attempt per invocation, like 403.
- Lines 92–93: a digit-only Retry-After is capped at 30 seconds; other values, including HTTP-date form, use 8 seconds. There are at most two such waits per fetch invocation.
- Lines 167–175: DNS lookup also occurs in `url_refusal()`, before `fetch()`. An unsuccessful lookup becomes `unresolvable-host` and sends no HTTP request for that URL in that pass. That lookup has no explicit timeout argument.
- Lines 195–216: `locate()` tries only `urls[:4]`, continues to the next URL after a refusal, HTTP error, timeout, parsing failure, or absent quote, and succeeds when any fetched text contains the quote. Its catch records an exception's class name, not the HTTP status.

`reports/round-62/accept-d.py:265–285` calls `locator.locate()` again after **every** unsuccessful pass, regardless of failure class. It stops at the first success or after three passes. The 60-second gap is after completion of the failed pass, not a promise that pass starts are exactly 60 seconds apart.

| Result on an eligible URL | Maximum attempts in one fetch invocation | If the row remains unlocated |
| --- | --- | --- |
| HTTP 429 or one of the nine listed 5xx statuses | 3 | URL is revisited on later passes; at most 9 requests over all passes |
| HTTP 403, other 4xx, or an unlisted 5xx | 1 | URL is revisited on later passes; at most 3 requests |
| Connection failure / DNS error from urlopen / timeout | 1 | URL is revisited on later passes; at most 3 connection attempts |
| DNS refusal before fetch | 0 HTTP requests | DNS validation runs again on later passes |
| HTTP 200 but quote absent, conversion failure, or a policy refusal | No inner recovery loop for this outcome | D nevertheless repeats the row on later passes |

Thus a transient archive 403 followed by a quote-bearing 200 on pass 2 is recoverable without changing the base locator. The same holds for a one-off DNS failure or timeout. A repeated 403, repeated resolution/connection failure, repeated timeout, every URL lacking the quote, or continuing policy refusal still fails D after all passes. A successful fallback in the same pass also avoids the outer wait.

## Strongest local counterexample

The round-61 receipt `reports/round-61/telemetry/final-measures.txt:16–19` records S671 as the sole LOCATE miss, but truncates the archive result. It does **not** establish the original archive error's HTTP status. The spot-check at `corpus/lessons/round-61-verifier-spotcheck.md:48` records the live origin returning 403 and the archive returning 200 with the quote at 10:14:56Z, after the 09:58Z receipt. Section 7 item 5 explicitly warns that one capture is not a second independent source of availability.

[INFERENCE — static execution trace, not a counter run] Keep that S671-shaped topology: origin returns 403 throughout; the valid capture is temporarily returning 403 during all three pass attempts, then recovers immediately afterward. With instantaneous fixture responses, the capture is attempted at virtual seconds 0, 60 and 120 and recovers at 121. Each pass returns false; D's LOCATE fails although the quote and capture are sound. This is **one outage episode**, not three independent source defects.

The historical observations prove failure at one instant and success later. They do not establish recovery within two minutes, nor prove an outage lasted the entire intervening interval. Therefore the new policy could have rescued S671, but the available evidence cannot establish that it would have.

This residual is an explicitly bounded availability tradeoff, not a reason to admit an unlocated row. No finite retry schedule guarantees recovery from an arbitrarily long transient episode.

## Smallest safe pre-data correction

1. **Keep the existing three-pass algorithm and fail-closed predicate for the stated isolated-error goal.** The code already revisits 403/DNS/timeout outcomes. Adding inner retries for those classes is not necessary to prevent one recoverable failed transaction from deciding the row, and adds waiting/traffic. No local evidence selects a better numerical pass count or gap.
2. **Correct the declaration's shorthand** in the counter docstring and `claims.json` fetch treatment: replace “429/5xx” with the exact retry set, and say that unsuccessful rows are retried across passes regardless of class. State the guarantee as “bounded recovery opportunities,” not immunity to a transient outage. This removes a fixable depth/calibration defect without weakening acceptance or changing runtime behavior.
3. **Require a D-specific paired recovery/exhaustion control before data.** O's offline tool controls are not evidence that D's different locator/pass policy works. Do not switch D to the new O tool: that would change the declared instrument and conflate the two claims.

One additional fallback edge is mechanically visible: `accept-d.py:213–224` accepts a capture anywhere after a live URL, but the base locator ignores URLs after the fourth. A row with four live URLs followed by its only capture satisfies that ROWS URL check while never trying the capture. For the prescribed two-URL row this does not arise. If the gate is intended to guarantee usable fallback for every row it accepts, the smallest tightening is to require at least one capture index below 4 (in addition to the existing live-before-capture rule), rather than expanding the frozen locator's URL budget. This is a fixable row-validation mismatch, not an argument for waiving LOCATE. Same-page capture provenance remains a separate row-contract requirement; a listed URL alone proves neither availability nor provenance.

## Controls that would discriminate the issue

These are control specifications, **not executed receipts**. Run only against a clone at the assigned revision, with an explicitly labelled PROBE harness if interception requires changing counter code; retain its diff. Stub ordinary request responses, public-address DNS results and a virtual clock rather than relying on real outages. Preserve the real locator and outer-pass decisions.

- **Recoverable 403:** origin always 403; archive returns 403, then a quote-bearing 200. Expected trace: two passes, one 60-second inter-pass wait, origin requested twice and archive twice; location succeeds.
- **Recoverable DNS:** archive's first DNS validation fails, then resolves publicly and returns the quote. Expected: another pass, no archive HTTP request on the failed lookup, then location succeeds.
- **Recoverable timeout:** archive times out once, then returns the quote on the next pass. Expected: no inner timeout retry, but recovery on pass 2.
- **Inner retry calibration:** archive returns 503 three times and then a quote-bearing 200. Expected: first pass exhausts three archive requests; second pass locates on its first archive request. Pair with 503 throughout: nine archive requests, three passes, no location.
- **Outage spans allowance:** origin and archive return 403 on all three passes, with archive recovery available only after the last scheduled attempt. Expected: exactly three requests to each URL, two inter-pass waits, no location. A result claiming location here would demonstrate an unsafe fetch-error allowance. Failure here demonstrates why the absolute outage-immunity wording is untenable, not a defect in the stated bounded predicate.
- **Capture outside budget:** four nonlocating live URLs followed by a valid quote-bearing capture. Expected under current code: ROWS' URL condition accepts; the fifth URL receives zero requests; LOCATE cannot recover through it. This control would justify the one-guard ROWS tightening if L1 requires the fallback guarantee for all accepted URL lists.

A paired successful-recovery / exhausted-failure control is essential: the existing declared D dead-host/echo negative alone cannot distinguish a genuine recovery policy from a locator that simply never retries. The frozen first-run kill rule must remain unchanged after any claimed-object measurement.

## Review evidence and boundaries

Read first: round-62 claims and round-61 spot-check section 7. Inspected the fetch, URL refusal, fallback and LOCATE call paths; no live requests or counter tests were run, and no CONTROL-MET/NONE-MET receipt is asserted.

Read-only SHA-256 commands confirmed the inspected files match the assigned revision's bytes:

- `accept-d.py`: `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4`.
- `reopen-quote.py`: `39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390`.

Every shell command used a timeout of at most 30 seconds; no background process or runtime was started. Scratch directory prepared: `/fast/scratch/hyaku/kotodama-r62/CriticFetchRule/`; no fixtures were executed or written. No tools installed. This report is the only lane write.
