# Round 65 claims wording audit

Reviewed the current `reports/round-65/claims.json`, the counters, base dry-runs/controls, and the round-64 `exactness-sweep-o.txt`. Verdicts apply to the statement sentences, not the frozen predicates.

## C — qualified pass; census provenance incomplete

The core after-state is concrete: IDs S750–S775 are an explicit 26-row range, and `accept-c.py` checks row tier/status/opened/used-by, citation counts, and the appended registry delta (`APPEND`, lines 376–384: base count + 26; the base dry-run/control show 675 → 701). I independently counted 238 knowledge Markdown files and 31 under `culture-material` at the pinned base; once the named single file is added, 239/32 is derivable. The current word-bounded filename query is a useful correction to the earlier substring query, whose incidental matches the statement names as `display` and `transport`.

Two clauses still lack a reproducible leg/receipt. First, `0 topic-line owners` has no definition or query in the statement, and `accept-c.py` does not inspect base ownership. Second, the statement says `end census exit 0` without naming a census command or receipt; the frozen telemetry currently has `census-start.txt`, not an end-census result, and `SWEEP` checks exit/topic-row, not an end-census receipt or those absolute corpus totals. The counts are arithmetically recoverable after the one-file diff, but they are not acceptance-pinned values.

**Smallest safe wording fix:** in the statement correction, define the topic-line-owner census (base revision + exact matching rule/query), and cite the committed end-census receipt/command for `239/32` and exit 0. If no end receipt is to land, state only that the base tree counts are 238/31 and the accepted single-file addition implies 239/32; drop the unreferenced end-census assertion.

## O — round-64 exactness wording repaired; one new overclaim remains

The round-64 failure is accurately avoided by saying every mutant fails **at least** its pinned leg. `exactness-sweep-o.txt` directly contradicts the old “exactly” statement: m1 pins only `EDGE_SCHEMEREL` but fails `EDGE_USERINFO` and `EDGE_HTTPS` too (lines 6–10); m2 pins `EDGE_USERINFO` but also fails `EDGE_MALTARG` (lines 19–24). The current MUTEX expectation table enumerates all ten mutants and these full m1/m2 failure sets (`accept-o.py`, lines 1154–1164), so the updated table/receipt can make that outcome re-derivable. “m1 +… / m2 +…” is understandable in context but would be clearer as full sets (m1 = `EDGE_SCHEMEREL`, `EDGE_USERINFO`, `EDGE_HTTPS`; m2 = `EDGE_USERINFO`, `EDGE_MALTARG`). Likewise, clarify that the RESTATE threshold is 80% of the **clause’s** content tokens found in order in the teaches cell, not 80% of the teaches cell.

**Blocking wording defect in the current revision:** it says round-65 `accept-ca` has “every R-leg binding exact bytes rather than global tokens, so the keying class cannot recur.” That is not true of the current counter: R3 still checks path strings anywhere in `LOG.md` plus a marker anywhere in `SCORECARD.md` (`accept-ca.py` lines 220–224), and R6 checks only two strings anywhere in the lesson (lines 255–258). These are substring-presence checks, not exact-byte/field bindings; an unrelated occurrence can satisfy them. This is exactly the kind of global-token shortcut the sentence declares impossible.

**Smallest safe wording fix:** replace that assertion with “round-65 `accept-ca` separates the seven dispositions into R1–R7 legs; R3/R6 remain presence checks,” and do not claim the keying class cannot recur. Retain “at least” and disclose the full m1/m2 failing sets. Also keep the final exactness-sweep claim conditional on the committed `exactness-sweep-o65.txt`; the base dry-run records it as not yet committed.

## Ca — partial; “each by one counting leg over committed bytes” overstates the evidence

The seven routed IDs are explicitly enumerated and map to R1–R7 legs; R2 append-only and R4’s parsed O predicate value have concrete checks. However the universal “all dispositioned … each by one counting leg over committed bytes” is not established as written:

- `accept-ca.py` reads most records with ordinary `open()` (`read`, lines 106–110), without requiring a clean checkout or reading those records from a pinned commit. A passing run can therefore score worktree bytes, not necessarily committed bytes.
- R1 checks the original receipt SHA **label** and requires a marker plus selected distinctive lines below it (`_preserved_block_ok`, lines 119–146); it never hashes the preserved block and compares that digest to the original. Thus a truncated/altered block retaining those lines can pass while “the original bytes preserved” is false. Its repeat check also establishes the corrected revision token near each R1 marker, not full correction text.
- R4 now parses the O claim and checks the exact predicate string, but the correction matcher checks only the “at least” phrase and `EDGE_USERINFO`/`EDGE_MALTARG`; it does not require `EDGE_HTTPS` or tie the extras to m1/m2 (`lines 226–242`). The filed-report erratum is also asserted in the sentence but is not read by R1 or another leg.
- The live `accept-ca.py` adds a `RECEIPTS` leg (lines 288–320), but the Ca `legs` array in `claims.json` still lists only R1–R7, CRITERION, QUOTES.

**Smallest safe wording fix:** do not describe all these details as established “by one counting leg over committed bytes.” Either cite separate byte-level evidence for the original receipt block, filed-report erratum, and exact R4 correction, and pin the checkout/commit being measured, or narrow the statement to what the legs actually check (R1 stamp/hash/manifest plus required original lines; R4 exact predicate value plus listed correction substrings; other legs as named). Update the enumerated leg list to include `RECEIPTS` if that remains part of the frozen run.
