# ScoutEgyptAmulets — claim C source seat (S600, S601)

Subtopic: ancient Egyptian amulets — wedjat (eye of Horus), scarabs, mummy-wrapping amulets; museum/university records.
Installs: none. Scratch: `/fast/scratch/hyaku/kotodama-r59/ScoutEgyptAmulets/` (drafts, fetched bodies, analyzer).
Both rows verified with the round-59 instrument, final text, exit 0.

## (1) Registry rows

| S600 | Digital Egypt for Universities, University College London, "Amulets", teaching page on Egyptian burial customs, page footer "Copyright © 2002 University College London" — https://www.ucl.ac.uk/museums-static/digitalegypt/burialcustoms/amuletsindex.html (direct, HTTP 403, 5,591 bytes, Cloudflare "Just a moment..." interstitial; challenge met and not passed, so the page was read from its Wayback capture); capture https://web.archive.org/web/20141126174231id_/http://www.ucl.ac.uk/museums-static/digitalegypt/burialcustoms/amuletsindex.html (Wayback replay, HTTP 200, 11,240 bytes) | docs | B | the Egyptological definition of an amulet as worn protection, and why the term is restricted to unambiguous religious adornment | body, first paragraph: "Amulets are items worn to protect their wearer by their religious associations, a religious equivalent to armour." | UCL's Digital Egypt page defines an amulet as worn protection whose force comes from religious association. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S601 | The Metropolitan Museum of Art, "Wedjat eye amulet", Third Intermediate Period or later, 1076–664 B.C., object record 566845, Department of Egyptian Art — https://www.metmuseum.org/art/collection/search/566845 (direct, HTTP 200 to the checker's plain GET, which served the object text; this seat's curl attempts got HTTP 429, 34,218 bytes, Vercel Security Checkpoint); capture https://web.archive.org/web/20250125005512id_/https://www.metmuseum.org/art/collection/search/566845 (Wayback replay, HTTP 200, 212,855 bytes) | docs | A | the wedjat-eye amulet's protective and regenerative function in the Met's object text | object text: "An amulet in this shape was thought to protect its wearer and to transfer the power of regeneration onto him or her." | The Met's record says a wedjat-eye amulet of this form guarded its wearer and carried regenerative power. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

## (2) Gate lines

- S600 — https://www.ucl.ac.uk/museums-static/digitalegypt/burialcustoms/amuletsindex.html — accessed 2026-10-23 — body, first paragraph: “Amulets are items worn to protect their wearer by their religious associations, a religious equivalent to armour.”. Grounds: UCL's Digital Egypt page defines an amulet as worn protection whose force comes from religious association. Seat: ScoutEgyptAmulets.
- S601 — https://www.metmuseum.org/art/collection/search/566845 — accessed 2026-10-23 — object text: “An amulet in this shape was thought to protect its wearer and to transfer the power of regeneration onto him or her.”. Grounds: The Met's record says a wedjat-eye amulet of this form guarded its wearer and carried regenerative power. Seat: ScoutEgyptAmulets.

## (3) Rowcheck output (final rows.md + stub.md)

```
S600 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://web.archive.org/web/20141126174231id_/http://www.ucl.ac.uk/museums-static/digitalegypt/burialcustoms/amuletsindex.html | BOILER: root-clear https://web.archive.org/web/20141126174231/http://www.ucl.ac.uk/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'assoc', 'prote', 'relig', 'worn'] | TOPIC: quote_hits=1 function_words=5 page_hits=41 page_terms=38 need=1/2/3/2
S601 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.metmuseum.org/art/collection/search/566845 | BOILER: root-clear https://www.metmuseum.org/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'power', 'regen', 'weare'] | TOPIC: quote_hits=1 function_words=10 page_hits=13 page_terms=14 need=1/2/3/2
EXIT 0
```

Command: `cd /fast/scratch/hyaku/kotodama-r59/ScoutEgyptAmulets && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutEgyptAmulets/rows.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutEgyptAmulets/stub.md`

## (4) Draft entry sentences

S600:
- Amulets are worn objects whose protective force comes from religious association, the UCL Digital Egypt page explains (S600).
- Egyptology reserves the word amulet for bodily adornments of unambiguous religious character, even though jewellery is likely to have a protective, amuletic function (S600).

S601:
- Worn as an amulet, the wedjat eye was believed to guard its wearer and to carry regenerative power (S601).
- The Met identifies this wedjat eye as the healed eye of Horus, among the most popular amulets in ancient Egypt (S601).

## (5) Rejected

- https://www.metmuseum.org/essays/egyptian-amulets (Isabel Stünkel, “Ancient Egyptian Amulets”, Heilbrunn Timeline, 2019). Opened and read from capture `20250805040628id_` (the stored payload is gzip; my test decompressed it). Direct request `429 34219`. Viable but not offered: two rows only, so the slots went to a definition page (UCL) and an object record (Met); the essay's wedjat material duplicates S601. Analyzer output: `TEXTWORDS 1771`, `PAGE_HITS 80`, `TERMS 82`.
- https://www.metmuseum.org/toah/hd/amulets/hd_amulets.htm — wrong/legacy path, `429 34227`; Wayback availability returned `{"url": "https://www.metmuseum.org/toah/hd/amulets/hd_amulets.htm", "archived_snapshots": {}}`.
- https://www.ucl.ac.uk/museums-static/digitalegypt/amulets/index.html — wrong path, `403 5556`; Wayback availability `{"archived_snapshots": {}}`.
- British Museum EA29440 (heart amulet with Book of the Dead 30B): live 403; capture `20250905022001` was throttled on my fetches and its read text had no 10–25-word sentence carrying a CHARM-GUARD window (description sentences run 32–44 words). Analyzer: `hits 9 terms 9`, no candidate sentence printed. EA7876 likewise `hits 1 terms 12`; its only windowed sentence is 40 words.
- https://www.liverpoolmuseums.org.uk/artifact/heart-scarab-8 — HTTP 200, 6,182 bytes, but TOPIC page floor missed: `PAGE_HITS 1 TERMS 6` (need 3 windows).
- https://www.brooklynmuseum.org/opencollection/objects/3124 — `429 34217`.
- https://www.artic.edu/artworks/150740 — `403 5438`.
- https://clevelandart.org/art/1980.13 — `308 15` redirect to https://www.clevelandart.org/art/1980.13.
- https://art.thewalters.org/detail/32127/ — `500 3617`.
- https://www.penn.museum/collections/ — `403 961`.
- https://australian.museum/learn/cultures/international-collection/egyptian/ — `404 131219`.
- https://www.fitzmuseum.cam.ac.uk/ — `503 11523`.
- https://collections.mfa.org/ — `403 118`.
- https://escholarship.org/content/qt13v7v5gd/qt13v7v5gd.pdf (UEE “Scarab”, Cooney 2008) — `403 919 text/html`; body begins `ERROR: The request could not be satisfied` … `Request blocked.`; the item page also `403 919`.
- https://journals.openedition.org/pallas/2166?lang=en — `200 5217 text/html`, probed only, not read; no row drafted from it.
- https://revistas.usp.br/marenostrum/en/article/view/174233 — the probe returned no status line (request did not complete within its timeout); not read.

## Risks / notes for L1

- Encoding trap: `id_` plays the archived bytes verbatim. Some Met/UCL captures are stored gzip, and the instrument's fetch does not decompress, so an id_ capture can fail LOCATE while a plain replay succeeds. Both offered captures were re-fetched with the instrument's own urllib path and are identity HTML that locates the quote (UCL 20141126174231: 11,240 bytes; Met 20250125005512: 212,855 bytes). Met id_ 20241109052441 is gzip and was rejected for that reason.
- S601 live URL answered 200 to the instrument's plain GET on both verification runs but 429 to curl; the listed capture is the tested fallback, and BOILER's capture root (`web/20250125005512/https://www.metmuseum.org/`) answered 200. S600's live URL is a Cloudflare interstitial (403) and is never the locating URL; its capture and capture root both answer 200.
- Host diversity: ucl.ac.uk and metmuseum.org — no URL and no quote is shared with any existing corpus/SOURCES.md row (checked: no hits for `566845`, `essays/egyptian-amulets`, `museums-static/digitalegypt`, `wedjat`).
