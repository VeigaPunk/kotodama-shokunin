# Locator recon

**Observed command results** (run from `/home/vgpnk/Projects/shokunin/kotodama-shokunin`):

- `python3 -B reports/round-61/reopen-quote.py --row S718` → `LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC4794163/` (exit 0).
- `python3 -B reports/round-61/reopen-quote.py --row S729` → `LOCATED https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0326569` (exit 0; 1.77 s reported).
- `python3 -B reports/round-61/reopen-quote.py --row S744` → `NOT_LOCATED https://www.dictionary.com/browse/ushanka quote-absent` (exit 1; 1.01 s reported; no traceback).

**Retry-budget assessment:** For these sampled URLs, LIVE's three attempts spaced 20 seconds apart are adequate: both expected live citations located on the first invocation, and the rejected row returned the expected non-location promptly. This is sample evidence, not evidence that the budget withstands future rate limiting or transient errors. The pinned locator documents an individual fetch timeout of 120 s and retries HTTP 429/selected 5xx/508 up to three times, honoring numeric `Retry-After` up to 30 s (otherwise 8 s); `reports/round-65/accept-c.py` also runs up to three locator invocations with 20-second gaps. Thus 20 seconds is not a hard per-fetch timeout or a guarantee that every transient recovery fits between invocations.

Evidence: `reports/round-61/reopen-quote.py` lines 7–9, 81–96; `reports/round-65/accept-c.py` lines 43–46 and 424–437. The command output itself contains no evidence of retries or rate limits.