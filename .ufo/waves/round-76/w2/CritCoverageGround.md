# CritCoverageGround — C ground and coverage

## Verdict

**The substance supports a coverage move; the frozen ACCEPT-C result is not a reliable reason to reject that substance.** At base, the new standards-level calendar compilation/publication topic is absent from `corpus/knowledge`, and the landed amendment adds concrete material on GB/T 33661-2017. The claimed final counts are correct relative to base: 252→253 knowledge `.md` files and 817→820 registry rows. Important qualification: the three registry rows and two extra SOURCES.md prose lines were already in the frozen tree, so the final row count is not evidence that C landing itself added those rows. The strict frozen ROWS leg flags the two prose additions as non-row lines; this is a counter/scope defect, not missing coverage.

## Ground and novelty

- Frozen claim C correctly scopes its negative to `corpus/knowledge` and explicitly distinguishes historical lesson mentions: `reports/round-76/claims.json:39-41` (frozen at `df0f0309d61e5485bb17035d3f8791b1e6a11d40`). The committed base receipt independently records zero matches, exit 1, for `GB/T 33661`, GMW article URL, and openstd record URL within `corpus/knowledge`: `reports/round-76/telemetry/gap-sweep.txt:1-22`.
- Do not generalize that result to all `corpus`: the broader base grep finds historical notes in `corpus/lessons/round-68.md` and `round-69.md`. `w1/ScoutCoverageSweep.md:9-23` documents those hits and confirms the scoped knowledge/registry sweep is empty. Those lesson notes are not knowledge entries.
- The grounded gap is substantive, not merely the standard's identifier: the base calendar entry covers generic intercalation and calendar politics, while the amendment states the modern standard's month anchor, computation model/precision, publication contents, and drafting authority (`corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md:9-14,18-30`). It separately records the registry as identity metadata rather than clause text and the archive's era-name/start-year table as an instrument (`:32-38`; sources/provenance `:3-7`). The existing era-periodization material is not evidence that this particular archival table was already covered; the W1 coverage comparison says it held era-name rules but no archival table (`w1/ScoutCoverageSweep.md:50-57`).

## Counts and timing

- Base counts are independently recorded as 252 knowledge files and 817 SOURCES rows (`w1/ExecGapSweep.md:30-46`). Direct tree counts at base `98c486b` and C landing `722e69ff6361aadf148cb46acbf6ac8fd147f59a` were 252 and 253 `.md` files. The landed README indexes the new amendment and changes `culture-material` 40→41 (`corpus/README.md:410,416`); its footer records 252 then 253 (`:830-835`).
- The landed registry has three rows S894-S896, making 820 total, and the C source set/candidate mapping is frozen at `claims.json:41-58`; the rows are at `corpus/SOURCES.md:849-851`.
- **Timing caveat:** all three rows, the `## Paths` bullet, and the round-76 search-log paragraph were already present at freeze `df0f0309`; `git diff 98c486b..df0f0309 -- corpus/SOURCES.md` adds them. The freeze→C-landing diff does not modify `corpus/SOURCES.md`. So 817→820 is a valid base-to-final-state count, but these registry/prose changes are pre-freeze, not changes introduced by the C landing. The actual post-freeze coverage delta is the new knowledge amendment (plus its index/lesson material).

## Why ACCEPT-C fails, and smallest safe correction

The frozen ROWS implementation says every non-row line added in the base-to-lands SOURCES diff fails (`reports/round-76/accept-c.py:1529-1533`). At freeze, the control receipt already reports exactly the two non-row lines now present at landing—the `calendar-standard design` Paths bullet and the `State-standard calendar compilation` search-log paragraph—as `registry line added outside the frozen row_set` (`reports/round-76/telemetry/controls-c.txt:28-31`). Those lines remain in the landing tree at `corpus/SOURCES.md:854,902`. Therefore the frozen ROWS leg necessarily remains red at C landing even after the entry cites the rows; it rejects pre-existing, non-row SOURCES documentation rather than disproving the entry's coverage.

**Smallest safe correction for a future frozen counter:** compare the exact row-line multiset against the frozen row set, but require non-row SOURCES content to be unchanged from freeze to lands (or explicitly freeze/allow these two lines). This preserves the strict row set and protects unrelated registry prose without treating valid pre-data documentation as a failed source row. Claims/counters are frozen here; no changes were made.

No counter, build, test, linter, or formatter was run for this review. No tool was installed.