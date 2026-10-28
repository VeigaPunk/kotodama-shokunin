# MutCMapSurface — COLLCHECK redirect-alias probe

**Verdict:** On the frozen map and current counter, omitting the full S938 redirect URL from S895 does **not** survive as a false green: COLLCHECK rejects the map URL. This specific mutant was not run; the conclusion is from committed-source analysis. The selftest suite does not include a dedicated control for this map-URL-versus-row-URL condition, so its kill is not independently protected by a mutation case.

## Evidence

- Frozen map `.ufo/waves/round-76/assimilation/id-renumber-map.json` at `df0f030` lines 603–610 maps S938 to S895 and gives the full `https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=...` URL.
- Committed `corpus/SOURCES.md` at `df0f030`, line 850, gives S895's live `newGbInfo` URL and its Wayback capture, but records the redirect only as prose (`showGb?type=online redirects here by HTTP 302`), not as a full URL token. `reports/round-76/accept-c.py:262` defines URL extraction as full `http(s)://...` tokens; `:457-471` extracts those tokens and compares paths (exact/containment, with `%20` folding), not HTTP redirect equivalence. The showGb and newGbInfo paths therefore do not match.
- `reports/round-76/accept-c.py:3605-3631` reads the frozen map, and for S895 checks each staged map URL against URLs extracted from its landed source cell. A nonmatching map URL adds `map record S938 -> S895 names a document the row does not: ...` (lines 3623–3631). This explains the alias-related COLLCHECK failure; the committed lesson `corpus/lessons/round-76.md:89` says the final C receipt's ROWS/COLLCHECK checks expose the mismatch between the exact source-row set and the map's showGb alias.
- The committed `reports/round-76/telemetry/selftest-c.txt:73-79` lists seven COLLCHECK mutants, none testing a map-record URL that the row's source cell omits. `map_sha_mismatch` at line 82 tests FROZENCFG pin integrity, not this map-to-row join.

## Future control

Add a COLLCHECK selftest fixture that keeps the frozen S938→S895 map record/pin intact and removes the **full** showGb URL from S895's source cell (leave only newGbInfo and the archive URL); assert `LEG FAIL COLLCHECK` with the S938→S895 document-mismatch diagnostic. Include a positive control with the full showGb URL present so the requirement is explicit. This control should exercise the source cell itself, not merely alter the alias prose.

**Probe record:** No source mutation or detector run was performed (the assignment forbids edits/tests); no before/after mutation hashes or actual detector output exist. Also, `reports/round-76/telemetry/measures-c.txt` is absent from the cited C-landing tree, so this report relies on the committed lesson's failure characterization rather than claiming a literal receipt line.
