# RevRowS702 — blind support review, row S702 (claim C, veil as garment)

Reviewer: kotodama-r63-w1-RevRowS702, 2026-10-23, rev 80d53ffde7788299b69dbb0bd0436b2b7ddddb95 (read-only; registry and entry untouched).

## Path taken (declared)

`/fast/scratch/hyaku/kotodama-r63/ScribeRowS702/` was EMPTY when I started, so per my brief I took the INDEPENDENT-search path for the same subtopic: **veil as garment (covering for head/face; modesty, mourning, marriage, sanctuary)**. The assigned scribe's transcript (history://kotodama-r63-w1-ScribeRowS702) shows their direction is Britannica `/topic/veil` → wimple → V&A; my page is a different, independent source. I pinged the scribe with my URL to prevent a duplicate. Everything below was fetched by ordinary means (curl / the round-61 base locator); the held tool `tools/reopen-row.py` was never run.

## Judged page (independent)

- Live URL: `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Veil` — 1911 Encyclopædia Britannica, Volume 27, "Veil" (Wikisource transcription; page last edited 2018-10-16). Fetched: HTTP 200, 62,766 bytes. Not in `corpus/SOURCES.md` (grep 0 hits); capture URL also 0 hits.
- Capture: `https://web.archive.org/web/20251214013341id_/https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Veil` (CDX limit=-5 statuscode:200 → five 200 captures 2022–2025; used the latest). Fetched: HTTP 200, 55,982 bytes; `<title>1911 Encyclopædia Britannica/Veil - Wikisource, the free online library</title>`; `rel="canonical" href="https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Veil"` — embedded original URL equals the live URL (QUALITY 13).

## Q1 — does the page carry the drafted quote verbatim (8–25 normalised words, body text)? YES

Drafted quote (18 normalised words): `The word is, however, chiefly used of a covering for the face and head, as worn by women.`

Canonical locator runs (base locator, never the held tool):

```
$ python3 -B reports/round-61/reopen-quote.py 'https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Veil' 'The word is, however, chiefly used of a covering for the face and head, as worn by women.'
LOCATED https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Veil
$ python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20251214013341id_/https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Veil' '…same quote…'
LOCATED https://web.archive.org/web/20251214013341id_/https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Veil
```

Located span pasted from the capture's own bytes (tags stripped, whitespace normalised) — it is the encyclopaedia's body-text definition paragraph, not a caption/alt/title/meta:

> …veils of the Jewish tabernacle, which hung before the Holy Place, and before the Most Holy Place. The word is, however, chiefly used of a covering for the face and head, as worn by women. The veiling of the face by women is a practice, among the Mohammedan rac…

## Q2 — does the capture show the same page with the quote? YES

Same title as live, canonical equals the live URL, and the quote LOCATED in the capture by the base locator (above). No bot challenge was met on either URL.

## Q3 — does the drafted entry line restate ONLY what the quote carries? YES

Drafted artifacts (for L1 assembly; I did NOT write these to the registry or entry):

- Row (11 columns verified):
  `| S702 | Veil, Wikisource (1911 Encyclopædia Britannica, Volume 27; transcription page last edited 2018-10-16) - https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Veil ; capture https://web.archive.org/web/20251214013341id_/https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Veil | book | B | 1911 Britannica's sense-history of the veil: sanctuary curtain, and chiefly the face-and-head covering worn by women (Eastern veiling, European head-dress to modern gauze) | encyclopaedia entry, opening definition: "The word is, however, chiefly used of a covering for the face and head, as worn by women." | 1911 Britannica makes veil chiefly a covering for the face and head worn by women. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |`
- Entry bullet: `- The word veil is chiefly used of a covering for the face and head worn by women (S702)`
- Gate line: `- S702 | https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Veil | 2026-10-23 | "The word is, however, chiefly used of a covering for the face and head, as worn by women."`

Machine checks (normalised lowercase, punctuation stripped): quote 18 words (8–25 ✓); bullet exactly one S-id, ends `(S702)` ✓; ≥5 content words (≥4 letters, non-stop): veil, chiefly, covering, face, head, worn, women (+word) ✓; in-quote in quote order: word→chiefly→covering→face→head→worn→women (7 ≥ 3) ✓; longest consecutive verbatim run 10 ≤ 12 ✓. Restate-only: every claim in the bullet ("chiefly used of", "covering for the face and head", "worn by women") is carried verbatim by the quote; no dates, peoples, or uses beyond the words. The teaches column and scope mention only content present on the page.

## VERDICT: SUPPORTED

For the independent page judged here, all three questions answer yes: verbatim 18-word body-text quote LOCATED on the live URL, the Wayback id_ capture of the same page carries it (canonical = live URL), and the drafted entry line restates only the quote.

## Residual risk / notes for L1

- web.archive.org flapped repeatedly this hour (curl exit 7 / URLError on first attempts; capture fetch succeeded on try 3, capture locator LOCATED on a later retry). Transient connection errors only — within the frozen retry budget; not a content NOT_LOCATED. If the LIVE leg hits this flapping, the earlier 200 captures (20250210042617, 20250429175211) are verified-digested alternates for the same page.
- URL uniqueness: my live and capture URLs are absent from SOURCES.md at 80d53ff (grep 0). Other scribes' final picks were not enumerable at review time; L1 must enforce global URL uniqueness at assembly. Collision ping sent to ScribeRowS702.
- Tier B (Wikisource transcription of a public-domain encyclopaedia) — claim C allows tier A or B; this row is in the frozen live subset, and the page is a plain stable HTML transcription with five 200 captures, i.e. robust for the locator.
- Scratch evidence: /fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-RevRowS702/ (wikisource.html, capture.html, cdx.json, extracted text).
