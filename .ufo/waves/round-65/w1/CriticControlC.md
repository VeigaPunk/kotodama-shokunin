# Claim C do-nothing control — CriticControlC

## Counterexample and assumptions

Static walk of the frozen `reports/round-65/accept-c.py`; no control fixture or acceptance command was run. I read “26 bullets, no rows” literally as 26 ID-free bullets, plus 26 appended, otherwise well-formed registry rows. To isolate the proposed shortcut, assume the stub meets `FILE`'s mechanical shape, the 26 live URLs are unique and non-placeholder, and each capture has the expected Wayback syntax but its original URL fails `norm_url` equality. The prompt does not specify README edits, hosts/URL uniqueness, row anchors, or whether bullets carry IDs; conditional cases are called out below.

| Leg | Result for the stated control | Basis / qualification |
|---|---|---|
| FILE | **PASS** (if stub has one H1, a `- topic:` line, no H3, <=16 H2, <=250 lines) | Lines 174–186 check only file shape and presence, not whether the entry teaches anything or has sources. |
| ROWS | **FAIL** | Lines 238–253 reject each validly parsed capture whose original URL does not `norm_url`-match the live URL (`capture_original_mismatch`). Invented `teaches` values are not independently vetted here. |
| ONEID | **FAIL** for ID-free bullets | Lines 264–284 see zero entry citations, so `citation_exact` is false and all S750–S775 are missing. Registry rows do not count as entry citations. The citation linter can still be clean with no cited lines. If the bullets actually carry one S-ID apiece, ONEID can instead **PASS** on syntax/count alone; it does not establish provenance. |
| RESTATE | **PASS, vacuously**, for ID-free bullets | Lines 286–341 iterate only `cited`; with none, `restate_bad=[]` and the leg passes with `lines=0`. This is the clearest leg-level false green for a source-less stub. If IDs are present, result depends on bullet/anchor/teaches text; fabricated inputs can be engineered to satisfy these lexical tests. |
| HOSTS | **PASS** if the live hosts are outside the hard-coded placeholder list | Lines 343–355 only filter a small list of hostnames; neither capture identity nor source authenticity is checked. |
| LINK | **PASS** with the assumed unique live URLs, each appearing once in its registry row and not in the entry | Lines 357–367 check exact live-URL occurrences and entry leakage, not capture/live equivalence. That mismatch is checked by ROWS, so LINK passing is not a bypass of the combined predicate. |
| APPEND | **PASS** if the 26 rows are appended and all base registry rows remain verbatim | Lines 369–377 count rows and check the base-line multiset; they do not assess row evidence. |
| NOHARM | **PASS** if the only `corpus/knowledge` change from base to `main` is the new entry | Lines 379–384 check changed paths, not the entry's substance. This leg ignores the registry and `corpus/README.md`. |
| SWEEP | **FAIL** if only the two described artifacts are added and README is untouched; otherwise conditional | Lines 386–403 require the sweep to reconcile files/index/counts and require the README row to carry the entry topic verbatim. Updating that index/footer lets an empty stub pass this structural check. |
| LIVE | **Indeterminate from the stated facts** | The locator hash check passes if the pinned locator is unchanged. Lines 418–440 then require LOCATED for six IDs and perform network fetches. The locator reads the anchor quote and tries source-cell URLs (round-61 `reopen-quote.py:195–216,226–253`); a mismatched capture alone does not force failure if the live URL locates the quote. No quote/response evidence was specified, so a definite LIVE result cannot be claimed. |

**Aggregate:** ACCEPT-C cannot pass this control: ROWS fails on the capture mismatch, and ONEID fails under the literal ID-free reading. If README is not updated, SWEEP also fails. The outcome remains FAIL even in the alternative where bullets cite all 26 IDs and the README is made consistent. The standalone RESTATE PASS is misleading/vacuous, but does not make the overall predicate green because ONEID is an independent completeness gate.

## Evidence and residual interpretation

- The frozen claims list FILE/ROWS/ONEID/RESTATE/HOSTS/LINK/APPEND/NOHARM/SWEEP/LIVE as the C legs (`reports/round-65/claims.json:14–16`).
- The acceptance docstring describes ROWS capture identity and RESTATE's “every entry line citing” rule (`accept-c.py:13–46`); implementation confirms ROWS compares the capture original at `:238–253`, while RESTATE's empty loop returns PASS at `:286–341`.
- The pre-wave `controls-c.txt` only records a RESTATE near-copy / query-twin control, not this no-citation vacuity (`reports/round-65/telemetry/controls-c.txt:8–25`).
- This control does not test whether invented quotes/teaches are faithful to real sources; the frozen claim explicitly leaves per-row support and sentence support review-only (`claims.json:23–27,90–92`). Do not treat passing structural legs as provenance proof.

## Impact and smallest safe correction

**Impacted axis:** C / coverage, specifically the diagnostic strength of RESTATE—not the overall accept result for this control. The narrow correction, if a standalone RESTATE PASS is meant to assert that work occurred, is to label zero cited lines as non-applicable/failing that leg (or require its expected citation set); retain ONEID as the sole citation-completeness authority. No change is needed to reject this particular control: ROWS already fails the stipulated capture mismatch and ONEID catches the ID-free stub.