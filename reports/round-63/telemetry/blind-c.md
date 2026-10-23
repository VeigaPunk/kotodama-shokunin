# Round 63 blind-support re-verification — S712, S713, S714, S715 (blind-c)

Date: 2026-10-23. Scope: re-open each row's live URL by ordinary means, verify the
anchor quote verbatim in body text, verify the capture URL shows the same page with
the quote. Rows as landed in `corpus/SOURCES.md` lines 765–768; knowledge file
`corpus/knowledge/culture-material/headgear-head-covering-codes.md`.

Method: `curl` (multiple UA/header profiles) for live pages; `read` tool for
archive.org `id_` raw captures (permitted transport while egress intermittent; no
capture transport failed). Verbatim match = char-for-char substring of body text.

No tools installed or upgraded (used existing curl/python3; nothing to record under
the 2026-10-19 tooling directive).

---

## S712 — "Wimple," Encyclopaedia Britannica

- Live: https://www.britannica.com/topic/wimple
- Capture: https://web.archive.org/web/20260211225215id_/https://www.britannica.com/topic/wimple
- Anchor quote (row): `The wimple, usually made of fine white linen or silk, framed the face and covered the neck`

**Live span (verbatim, sentence continues past the quoted prefix):**
> The wimple originally was adopted as a chin veil by Western women after the crusaders brought back from the Near East such fashions as the veil of the Muslim woman. The wimple, usually made of fine white linen or silk, framed the face and covered the neck and sometimes part of the bosom.

**Capture span (same sentence, capture 2026-02-11):**
> The wimple, usually made of fine white linen or silk, framed the face and covered the neck and sometimes part of the bosom.

Same page: capture canonical `https://www.britannica.com/topic/wimple`, title
"Wimple | Veil, Head Covering, Scarf | Britannica", byline Britannica Editors —
identical to live identity.

Transport failures met (not passed, named): direct `curl` to live returned **403**
(Britannica bot block, 5.5 KB challenge body, quote absent); quote verified live via
the `read` tool's native fetch of the same URL (200). Both are ordinary means; the
403 did not contaminate evidence.

**Verdict: SUPPORTED** — quote verbatim in live body and in capture; same page.

---

## S713 — Karina Reddy, "1920-1929," Fashion History Timeline (FIT)

- Live: https://fashionhistory.fitnyc.edu/1920-1929/
- Capture: https://web.archive.org/web/20200828090928id_/https://fashionhistory.fitnyc.edu/1920-1929/
- Anchor quote (row): `the brimless cloche hats that were popular during the twenties`

**Live span (verbatim, curl 200, 259 KB):**
> They were feminine and romantic, like the pastel dress designed by Lanvin in 1922, accessorized with a straw hat itself removed from the brimless cloche hats that were popular during the twenties (Fig. 5).

**Capture span (verbatim, capture 2020-08-28):**
> They were feminine and romantic, like the pastel dress designed by Lanvin in 1922, accessorized with a straw hat itself removed from the brimless cloche hats that were popular during the twenties (Fig. 5).

Same page: capture canonical `https://fashionhistory.fitnyc.edu/1920-1929/`, byline
"Posted by Karina Reddy | Last updated Aug 18, 2020 | Published on May 11, 2018" —
matches row attribution (Karina Reddy, 2018, updated 2020) and live identity.

Transport failures: none (live curl 200 first try; capture read clean).

**Verdict: SUPPORTED** — quote verbatim in live body and in capture; same page.

---

## S714 — "Shako," Dictionary.com Unabridged (Random House)

- Live: https://www.dictionary.com/browse/shako
- Capture: https://web.archive.org/web/20240810035735id_/https://www.dictionary.com/browse/shako
- Anchor quote (row): `a military cap in the form of a cylinder or truncated cone, with a visor and a plume or pompon`

**Live span (verbatim, curl 200, 89 KB; the row quote is the American noun sense,
rendered in `<li class="item-definition">/<p class="txt-variant-label-short">` under
the "American" tab):**
> a military cap in the form of a cylinder or truncated cone, with a visor and a plume or pompon.

**Capture span (verbatim, capture 2024-08-10, same noun-sense list item):**
> 1. a military cap in the form of a cylinder or truncated cone, with a visor and a plume or pompon.

Same page: live title `SHAKO Definition &amp; Meaning | Dictionary.com`; capture
canonical `https://www.dictionary.com/browse/shako`, title "SHAKO Definition &
Meaning | Dictionary.com". Capture meta-description carries the same definition
sentence.

Transport failures: none (live curl 200 first try; capture read clean — its raw HTML
is JS-heavy, but the rendered content includes the full definition body).

**Verdict: SUPPORTED** — quote verbatim in live body and in capture; same page.

---

## S715 — "Escaramuza Dress," Smithsonian Institution (NMAH)

- Live: https://www.si.edu/exhibitions/escaramuza-dress:event-exhib-6579
- Capture: https://web.archive.org/web/20250429051926id_/https://www.si.edu/exhibitions/escaramuza-dress:event-exhib-6579
- Anchor quote (row): `Girls also don the emblematic sombrero charro, a broad-brimmed hat designed to provide relief from the blistering heat of the U.S.-Mexico borderlands.`

**Live span (verbatim, final paragraph of the exhibit description):**
> Skirts must cover the horse's haunches and allow the team to perform dangerous maneuverers at high speeds while riding sidesaddle. Girls also don the emblematic sombrero charro, a broad-brimmed hat designed to provide relief from the blistering heat of the U.S.-Mexico borderlands.

**Capture span (verbatim, capture 2025-04-29, same paragraph):**
> Girls also don the emblematic sombrero charro, a broad-brimmed hat designed to provide relief from the blistering heat of the U.S.-Mexico borderlands.

Same page: capture canonical
`https://www.si.edu/exhibitions/escaramuza-dress%3Aevent-exhib-6579`, title
"Escaramuza Dress | Smithsonian Institution", run dates "September 17, 2021 –
January 4, 2022" — matches row attribution (2021–2022 exhibition, NMAH) and live
identity.

Transport failures met (not passed, named): live `curl` with Firefox UA → **403**
Cloudflare challenge (challenge/cloudflare/Enable-JavaScript markers, quote absent);
live `curl` with curl UA → **403** (same challenge); `read` tool native fetch →
**HTTP 522**. Succeeded on fourth profile: `curl --http2` with Chrome UA + full
browser headers → **200**, quote present; `read` content-negotiation (text/markdown)
of the live URL also returned the page with the quote. Egress intermittent but not
blocking.

**Verdict: SUPPORTED** — quote verbatim in live body and in capture; same page.

---

## Summary

| Row | Live quote verbatim | Capture quote verbatim | Same page | Verdict |
|-----|---------------------|------------------------|-----------|---------|
| S712 | yes (via read; curl 403) | yes | yes | **SUPPORTED** |
| S713 | yes (curl 200) | yes | yes | **SUPPORTED** |
| S714 | yes (curl 200) | yes | yes | **SUPPORTED** |
| S715 | yes (4th transport profile; 3 failures named) | yes | yes | **SUPPORTED** |

Residual notes: (1) S712's row quote is a verbatim prefix of a longer sentence that
continues "and sometimes part of the bosom." — support claim unaffected. (2) S713's
knowledge-file line 42 says cloche hats "remained popular accessories throughout the
twenties," slightly stronger than the quoted span ("popular during the twenties"),
but the row's own claim field ("names brimless cloche hats as popular 1920s
accessories") is directly supported, and the same page states "The cloche hat became
an extremely popular accessory." (3) S714's capture raw HTML is a JS-shell; the
rendered extraction used here does include the definition body, and the live body
occurrence was confirmed in the item-definition markup.
