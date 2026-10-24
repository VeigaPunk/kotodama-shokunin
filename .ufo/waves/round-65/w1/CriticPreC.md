# CriticPreC — claim C pre-data review

## Verdict

**BLOCKER — the frozen C predicate does not measure every clause of its claim.** In particular, none of FILE/ROWS/ONEID/RESTATE/HOSTS/LINK/APPEND/NOHARM/SWEEP/LIVE checks the stated base-corpus “0 filename owners / 0 topic-line owners”; `accept-c.py` also never runs the claim’s “end census”. SWEEP runs the R28 README sweep, which checks current index/file consistency, not those omitted assertions. A passing ACCEPT-C-65 therefore cannot establish those parts of the statement.

The counter does prevent a completely source-less, dead-URL construction from passing: ROWS requires URL/capture-shaped fields and LIVE reopens six anchors. But a padded stub plus 26 syntactically plausible rows can pass with real anchors only for the six sampled rows and invented/unsupported data for the other twenty. The `review_only_global` text acknowledges blind per-row support, but that review is not part of the frozen ACCEPT-C-65 predicate.

## Do-nothing control: per-leg walk

Assume a stub is shaped to satisfy FILE, rows are appended without disturbing the base registry, and the README/index are kept consistent. “Invented” below means invented provenance/content, not necessarily a URL-free row.

| Leg | Result for the control | Evidence / limit |
|---|---|---|
| FILE | **Survives** | Only checks existence, line/H1/H2/H3 bounds, and a `- topic:` line (`accept-c.py:174-187`). It does not assess substance. |
| ROWS | **Survives if syntactically dressed; fails if truly URL-free** | Enforces 26 named IDs, 11 cells, A/B and `mined` labels, date/recheck/used-by strings, quote length, a live-URL string, and a same-normalized-URL Wayback capture (`:209-257`). It does not fetch the archive or verify tier, mined status, quote provenance, or that the archive capture is genuine. Missing URL/capture fails. |
| ONEID | **Fails for an uncited stub; survives with 26 padded citations** | Requires each new ID exactly once and a clean cited-lines lint (`:259-284`). The lint detects multi-ID/table-ID lines; it does not validate the cited source. |
| RESTATE | **Survives if bullets are mechanically tailored; vacuous-pass if no new citations** | Only iterates new-ID citation lines and checks shape, token overlap, novelty, copy-run, and teaches-cell near-copy thresholds (`:286-341`). Fabricated quote/teaches cells can be chosen to satisfy these checks. |
| HOSTS | **Survives with a non-placeholder host** | Blocks only the listed placeholder hosts (`:343-355`); it is not a reachability or source-quality check. |
| LINK | **Survives if URLs are unique and confined to their row** | Checks raw URL occurrence and entry absence (`:357-367`); query-aware duplicate detection is in ROWS. Neither proves the URL is a source for the claim. |
| APPEND | **Survives if the base is preserved and exactly 26 rows are added** | Checks base-row multiplicity and the +26 count (`:369-377`), not row truth. |
| NOHARM | **Survives if the only `corpus/knowledge` diff is the new entry** | Checks the path set of the BASE-to-main diff (`:379-384`), not whether the new entry is substantive. SOURCES/README changes are outside this path filter. |
| SWEEP | **Survives if the stub topic and README/index/counts are consistent** | Calls the sweep and checks the new README topic row (`:386-403`). The sweep measures repository consistency, not knowledge quality or the frozen base-owner claim. |
| LIVE | **Fails if all six anchors are actually sourceless; can pass with only six real anchors** | The frozen set is S750/S755/S760/S765/S770/S775 (`:78-79`, `:405-440`). The pinned locator fetches URLs and requires the anchor text to occur in fetched live/archive content (`reopen-quote.py:195-216`). If those six anchors locate, the other 20 are not reopened. |

Thus a literal URL-free/fake-all-26 control fails ROWS and LIVE (and a no-citation stub fails ONEID). A stronger counterexample is 26 invented rows with compliant URL/archive strings and fabricated metadata/teaches fields, plus an entry with 26 tailored citations, where the six frozen IDs point to pages that really contain their anchors. That construction can pass all ten legs while twenty rows remain unverified by LIVE. It refutes “ACCEPT-C-65 alone proves 26 mined/sourced rows,” not the narrower claim that the six sampled anchors were located.

## Universal-clause audit

- **Enumerated:** “every leg” maps to the ten named legs; the implementation appends a result for each and returns success only when `all(legs)` (`:168-172`, `:442-444`). S750–S775 are explicitly generated and iterated; ONEID checks exact-once citations. “All base registry lines preserved” is checked by comparing base-line multiplicities (`:369-377`).
- **Not enumerated / not measured:** the claim’s zero base filename/topic-line owners has no leg. `NOHARM` is not a substitute: it checks only the current diff path set. The claim’s “end census exit 0” is also not invoked; SWEEP invokes `reports/round-28/readme/sweep.py`, a different measurement. The statement’s 238→239 / 31→32 counts are not explicitly asserted by accept-c.py (SWEEP requires internally consistent measured counts, not those stated values).
- **Substantive “each” is only mechanical:** ROWS checks that every expected row carries the words `A`/`B`, `mined`, and the entry path, but not that those labels/provenance are true. LIVE is not an enumeration of all 26.

**Smallest safe correction:** before treating ACCEPT-C-65 as proof of the full statement, add explicit frozen-base owner checks and the specified end-census check (or remove those assertions from the claim); require source/location review for all 26, not only six, or narrow the claim to the measured subset. These changes require a pre-data refreeze under the frozen-predicate rule; I did not edit the counter or claim.

## Sizing

**Reachable, exactly at capacity:** 13 scouts × 2 rows = 26, matching the fixed target. There is no slack: one absent or rejected row makes the target unreachable unless another scout supplies a replacement or someone exceeds two. The target is feasible, but operationally brittle; reserve fallback capacity if two valid rows per seat are not guaranteed.

## LIVE subset: host concentration

**Yes, attackable in principle; actual concentration is not knowable pre-data.** `LIVE_IDS` is fixed by ID spacing, while ROWS only deduplicates normalized URLs (which ignore query/fragment) and HOSTS only rejects placeholder domains. No leg asserts host dispersion. Six distinct page paths on one permitted host can therefore all locate and pass LIVE, despite being a common-mode availability/source sample. The locator does reject certain search/echo/private hosts, but does not require independent hosts.

**Smallest safe correction:** freeze a host-diverse LIVE set and assert a minimum number of distinct hosts (or explicitly limit LIVE’s meaning to six page checks on potentially correlated hosts). This mitigates the sample-bias risk; it does not replace checking/reviewing the other 20 rows.

## Pre-data control receipt caveat

`telemetry/controls-c.txt` control 2 correctly shows ROWS failing the S751/S752 query-only duplicate (`S752:norm_dup_of=S751`). Its RESTATE leg fails too, but the displayed first S750 reason is `in_order=2`, not the new `teaches_nearcopy` reason; the receipt truncates the bad list to eight and its note says the near-copy-first demonstration is on another fixture. **If this receipt is being used as the sole proof that revision 1 closes the routed near-copy bypass, that proof is not isolated by this control.** The near-copy code exists at `accept-c.py:332-340`; this is a control-evidence limitation, not a claim that the code path is absent. The separate targeted fixture/receipt would need to be consulted to discharge that point.

Impacted axis: **coverage (C)**. Host concentration is a sampling/operability limitation on what LIVE establishes; no other claim axis reviewed.

Report: .ufo/waves/round-65/w1/CriticPreC.md
