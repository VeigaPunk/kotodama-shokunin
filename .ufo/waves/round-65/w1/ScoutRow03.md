# ScoutRow03 — S754/S755

Opened exactly the two assigned drafts:
- `.ufo/waves/round-65/rows/ScoutRow03/row-S754.txt`
- `.ufo/waves/round-65/rows/ScoutRow03/row-S755.txt`

## Source evidence

- **S754 — UNESCO Intangible Cultural Heritage, “Tugging rituals and games” (element 01080), A / docs.** The live URL returned HTTP 200 with no redirect on 2026-10-24, but curl received the TSPD human-verification challenge rather than the page text; the live-body quote check is therefore **N**. The row’s Wayback capture `20170513200455` returned HTTP 200 and its body contains the quoted two-team rope-pulling sentence. That capture also identifies Cambodia, the Philippines, the Republic of Korea and Viet Nam, and states inscription in 2015. Quote/body and country/date evidence are from the official UNESCO page capture, not an inference from search snippets. The source URL and capture original are identical, with no query.
- **S755 — Harvard Art Museums, “Knucklebone” (object 1978.495.46), A / docs.** The exact live URL returned HTTP 200 after two redirects to `https://harvardartmuseums.org/collections/object/280367` on 2026-10-24. The quoted sentence is present in the live page’s Published Catalogue Text, as well as the `20201026193552` capture (HTTP 200). The same catalogue text says sets of bones often occur in Greek graves and cautions that metal replicas could serve as votives or weights as well as game pieces. The selected teaching text preserves those qualifications. Live URL and capture original match exactly, with no query.

The bullets are drafts: S754 contains in-order quote terms `teams → end → rope`; S755 contains `Astragaloi → gaming → pieces`. Their shared teaching-cell vocabulary is limited and neither is a near-copy. No claim is made that each metal astragalus was used for gaming; the Harvard catalogue explicitly allows other functions.

## URL uniqueness grep outputs

- `https://ich.unesco.org/en/RL/tugging-rituals-and-games-01080`: `corpus/SOURCES.md` — **No matches found**. Grep across every round-65 row fragment returned only `rows/ScoutRow03/row-S754.txt` (the expected direct URL and capture original on that row); no other fragment matched.
- `https://www.harvardartmuseums.org/art/280367`: `corpus/SOURCES.md` — **No matches found**. Grep across every round-65 row fragment returned only `rows/ScoutRow03/row-S755.txt` (the expected direct URL and capture original on that row); no other fragment matched.

Both URLs also had no matches in the registry or row fragments before these drafts were written.

## Rejected candidate / remaining limit

`rows/ScoutRow03/rejects.txt` records the ICHCAP Courier article: curl returned HTTP 200 and the live body described the joint nomination, but CDX returned no exact-query capture for its article route, so it cannot satisfy the required capture pair. Flip: an exact-query Wayback capture with the article body becomes available. The remaining uncertainty for S754 is limited to the current live body, which remains blocked by TSPD; the quote is supported by the readable official archived body and that limitation is explicit in the row.
