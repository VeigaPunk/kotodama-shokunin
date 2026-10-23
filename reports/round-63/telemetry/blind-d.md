# Round 63 blind support — seat blind-d

Scope: re-open live URLs by ordinary means and verify capture agreement for rows S716, S717, S701, S709 (corpus/SOURCES.md, headgear-head-covering-codes batch). `tools/reopen-row.py` not used on live URLs (per seat constraints). Fetches: `curl -sSL` with a Firefox UA from this workstation, 2026-10-23.

**Transport failures met (named):**
1. Britannica live pages (S701, S717) return **HTTP 403 "Just a moment…"** (Cloudflare bot wall) to plain `curl`. Retried via the `read` URL-reader transport; both pages opened (HTTP 200) and their reader-extracted body text was used for the verbatim live check. Reader output preserves the exact characters of both quotes (no dash/quote/hyphen substitutions found).
2. Archive.org `id_` replays serve the original response bytes **including the original `Content-Encoding`** (gzip/brotli). A first capture fetch stored compressed bytes that read as garbage; re-fetched with `curl --compressed`, which decoded cleanly. No content discrepancy was involved — purely a transport decoding step.

---

## S701 — "Tuareg," Encyclopaedia Britannica — **SUPPORTED**

- Live: https://www.britannica.com/topic/Tuareg — `curl` → 403; via reader transport → 200. Page shows "Britannica Editors", "Last updated Oct. 15, 2026" (matches row's updated 2026-10-15). Anchor quote appears verbatim in article body (fourth paragraph):
  > …iron lances, and leather shields. **Adult males traditionally wore a blue veil in the presence of women, strangers, and in-laws, but that practice began to be abandoned with urbanization.** The Tuareg have preserved a peculiar script…
- Capture: https://web.archive.org/web/20261012061346id_/https://www.britannica.com/topic/Tuareg — 200, `<title>Tuareg | People & History | Britannica</title>`, canonical `https://www.britannica.com/topic/Tuareg` (same page as live). Same paragraph verbatim:
  > "Adult males traditionally wore a blue veil in the presence of women, strangers, and in-laws, but that practice began to be abandoned with urbanization."
- Note: capture stamp 2026-10-12 predates the 2026-10-15 update shown on today's live page; the anchor sentence is present in both versions.

## S709 — "Hat (kufi)," Birmingham Museum of Art — **SUPPORTED**

- Live: https://www.artsbma.org/collection/hat-kufi/ — `curl` → 200, `<title>Hat (kufi) | Birmingham Museum of Art</title>`. Quote verbatim in the Provenance field:
  > …memory of James A. Clarke, AFI.427.2010 Work Type hat … **Provenance Purchased by the donor and her husband from the hat-maker in 1967 in Ogbomosho, Nigeria** See More of the Collection…
- Capture: https://web.archive.org/web/20230330120744id_/https://www.artsbma.org/collection/hat-kufi/ — 200, same title and canonical `https://www.artsbma.org/collection/hat-kufi/` (same page as live). Same provenance line verbatim:
  > "Purchased by the donor and her husband from the hat-maker in 1967 in Ogbomosho, Nigeria"
- Note: capture stamp 2023-03-30 predates the row's "page modified 2026-05-20"; the anchor provenance sentence is identical in both.

## S716 — Forces News, "The bearskin…" — **SUPPORTED**

- Live: https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know — `curl` → 200, `<title>The bearskin: Everything you need to know about the iconic ceremonial headwear</title>`. Quote verbatim after the who-wears-it passage:
  > …the Drum Major of the Band of the Royal Highland Fusiliers wears one on parade. **The bearskin is only worn as part of full dress.** St Patrick's Day parade led by Irish Guards Pipes…
- Capture: https://web.archive.org/web/20260812000554id_/https://www.forcesnews.com/technology/uniform/bearskin-everything-you-need-know — 200, same title and canonical (same page as live). Identical sentence verbatim:
  > "The bearskin is only worn as part of full dress."

## S717 — "Fez," Encyclopaedia Britannica — **SUPPORTED**

- Live: https://www.britannica.com/topic/fez — `curl` → 403; via reader transport → 200. Page shows "The Information Architects of Encyclopaedia Britannica", "Last updated July 22, 2026" (matches row's updated 2026-07-22), and is the **Quick Summary** page — the row already bounds its claim to that summary ("bounded summary support"); note the page itself labels the summary AI-created from Britannica articles. Anchor quote verbatim in the Quick Summary body:
  > **A fez is a brimless, cylindrical or cone-shaped hat with a flat top, typically made of red felt and often adorned with a tassel.** It is traditionally worn by men in eastern Mediterranean countries.
- Capture: https://web.archive.org/web/20260818053727id_/https://www.britannica.com/topic/fez — 200, `<title>Fez | hat | Britannica</title>`, canonical `https://www.britannica.com/topic/fez` (same page as live). Same sentence verbatim inside the `answer-content` block:
  > "A fez is a brimless, cylindrical or cone-shaped hat with a flat top, typically made of red felt and often adorned with a tassel."

---

## Summary

| Row | Live verbatim | Capture verbatim | Same page (title/canonical) | Verdict |
|---|---|---|---|---|
| S701 | yes (reader transport; curl 403) | yes | yes | SUPPORTED |
| S709 | yes (curl 200) | yes | yes | SUPPORTED |
| S716 | yes (curl 200) | yes | yes | SUPPORTED |
| S717 | yes (reader transport; curl 403) | yes | yes | SUPPORTED |

Residual risk: verbatim matching for the two reader-transport pages was done on reader-extracted text (tag-stripped), not raw HTML — the 403 bot wall prevents raw-HTML comparison of the live Britannica pages; the archive captures provide the raw-HTML-level confirmation. No tools installed or upgraded for this seat.
