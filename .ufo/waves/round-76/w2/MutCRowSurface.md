# MutCRowSurface — Round 76 W2

## Verdict

**Coverage gap / ROWS scope is over-broad.** The frozen counter's ROWS selftests exercise row additions, removals, edits, and row shape, but do not exercise allowed append-only text in `corpus/SOURCES.md`'s `## Paths` or `## Search log` sections. The ROWS implementation compares all file lines and rejects every added nonblank non-row line, so those valid section appends are mislabeled as registry-row failures.

## Evidence (frozen C landing `722e69ff6361aadf148cb46acbf6ac8fd147f59a`)

- `reports/round-76/accept-c.py:1515-1533` states ROWS is about the registry diff, but its R1 wording treats every added non-row line as a failure.
- `reports/round-76/accept-c.py:1584-1605` implements that rule over all lines of `corpus/SOURCES.md`; lines 1588-1605 compute whole-file added/removed lines and flag non-row additions. `parse_rows` at `:385-391` also scans every line, without restricting parsing to `## Registry`.
- The frozen counter selftest table at `reports/round-76/accept-c.py:5893-5908` has row mutations (`row_extra`, removed/edited pre-existing rows, shape/used-by/quote defects, duplicate-document/base-document, tier-C-only support), but no Paths/Search-log append case.
- Committed selftest receipt `reports/round-76/telemetry/selftest-c.txt:19-33` reports those row mutations killed as `LEG FAIL ROWS`; it contains no append-permission case.
- Frozen C claim text `reports/round-76/claims.json:156` scopes the ROWS contract to registry rows (exact frozen row set, removals, row content and pre-existing rows). The source-file contract at frozen `corpus/SOURCES.md:9-12` is append-only, and the sections are explicitly titled `## Paths` at `:853` and `## Search log` at `:890`.
- The frozen do-nothing control's final ROWS output is `reports/round-76/telemetry/controls-c.txt:30-31`. Its first two reported “registry line added outside the frozen row_set” are actually the `## Paths` line `- calendar-standard design — S896 → S895 → S894: ...` and the `## Search log` line `**State-standard calendar compilation (round 76).** ...`; both are append-only prose, not registry rows. The remaining failures (missing entry and orphan rows) independently make this control correctly red, so the two prose diagnostics are not evidence of a row-contract violation.

## Concrete distinguishing cases (code-derived; not run)

1. **Allowed append pair:** preserve the frozen/base registry rows and the exact added `S894`–`S896` registry rows, then append the actual round-76 Paths line and Search-log paragraph above. Expected ROWS result: PASS; these are section appendages, not row changes. Current whole-file R1 logic would fail both additions at `accept-c.py:1598-1605`.
2. **Registry-row extra:** with the same clean row-only state, add an extra row-shaped record under `## Registry` outside frozen `row_set`. Expected ROWS result: FAIL (already represented by `row_extra`; `selftest-c.txt:19`).
3. **Pre-existing registry-row change/removal:** modify or remove one prior registry row while retaining allowed Paths/Search-log appends. Expected ROWS result: FAIL (existing `row_pre_existing_edited` / `row_removed_pre_existing`, `selftest-c.txt:20-21`).
4. **Section-boundary decoy:** add a row-shaped `| S… |` line under `## Paths` or `## Search log`, with no corresponding `## Registry` row. Expected ROWS result: it must not count as a registry-row addition; only actual registry-section row mutations should affect ROWS. The current file-wide `parse_rows`/line-diff scope does not make that distinction.

These cases isolate permitted append-only prose from registry-row-only invariants without relaxing checks on actual added, changed, removed, malformed, duplicate, or misused registry rows. No tests or runtime checks were run; this is a code-and-committed-output review only.