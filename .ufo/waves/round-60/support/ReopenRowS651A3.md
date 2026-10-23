HOLDS

S651 at `47f27bd0cb0bea219f21cd731c2eb0fe71f7f626` is the V&A object record for Amulet Box (ga'u), item O87367. The listed live URL returns the pinned bytes, the anchor quote locates in that page and not in the Physical description field, the first URL is the same page as S643, and every clause of the entry line is carried by the summary sentence. No Wayback URL is listed on the row, so there was no listed capture to fetch. No tools installed.

## Row (frozen)

`corpus/SOURCES.md:606`

| cell | text |
|---|---|
| source | Victoria and Albert Museum, London, object record "Amulet Box (ga'u)", made in Tibet, 1800-1850, silver, brass and coral, no author or publication date on the record — https://collections.vam.ac.uk/item/O87367/ (direct plain GET, HTTP 200, 46,556 bytes, accessed 2026-10-23; no live challenge) |
| kind | docs |
| tier | A |
| scope | this V&A record's description of one ga'u/amulet case holding prayers and blessed or holy objects believed to protect its wearer; not evidence of efficacy or that the objects alone protect |
| anchor | summary description paragraph beneath the object title, after its opening words This amulet case or ga'u of silver and coral (not the Physical description catalogue field): "was used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil." |
| teaches | supersedes S643 — the V&A record describes this amulet case or ga'u as used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil |
| status | mined |
| opened | 2026-10-23 |
| recheck | 2027-10-23 |
| used-by | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

S643 (`corpus/SOURCES.md:598`) first URL is the same string: `https://collections.vam.ac.uk/item/O87367/`. No other http(s) URL is in either source cell. `page_of` of both is `collections.vam.ac.uk/item/o87367`.

## Fetch and bytes

Live plain GET (desktop Firefox UA, redirects allowed, no cookies): `HTTP/2 200`, `content-type: text/html`, `content-length: 46556`, `date: Fri, 23 Oct 2026 07:52:35 GMT`, `last-modified: Thu, 06 Aug 2026 20:26:16 GMT`. Body is the object record (title, summary, catalogue fields). No challenge, login, or interstitial.

`sha256` of the live body, of `reports/round-60/captures/S651.bin`, and of `captures/manifest.json` key `S651` are the same: `8e4cf0198005310cc619f48830658bcd1fe2ddda8bdba64d5c86e98128f67c79`. Length 46556. `cmp` exit 0. Manifest also records `http: 200`, `content_type: text/html`, `url: https://collections.vam.ac.uk/item/O87367/`, `fetched_at: 2026-10-23T05:37:03Z`.

Access note matches what was fetched. The pin's HTML contains zero `Wayback` / `archive.org` strings.

## Quote

`python3 -B reports/round-60/reopen-quote.py --row S651` printed `LOCATED https://collections.vam.ac.uk/item/O87367/` and exited 0. The same locator's `locate_in` on the pinned file (`content_type` text/html) is true. Normalised quote length is 18 words.

The quote is the text of `div.object-page__summary` (class `b-object-details__summary`), the paragraph under `h1.object-page__title`, and it is repeated in the catalogue row whose name cell is `Summary`:

> This amulet case or ga'u of silver and coral, was used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil.

A comma sits between "coral" and "was". The anchor's opening words stop before that comma; the quoted span starts at "was". Both are on the page.

The Physical description field is a different sentence, which is why the anchor excludes it:

> An amulet box or ga'u used to contain rolled prayers and blessed or holy objects believed to protect the wearer against evil.

"contain" / "against evil" are not the quote. "hold" / "from evil" are.

## Tier, scope, access, identification

Tier A is the rubric's "primary or authoritative for that scope (… official docs …)". Kind `docs`. The scope is this record's description of this one object, not Tibetan practice at large and not efficacy. The V&A catalogue is the authority for what that record says. Scope's limit ("not evidence of efficacy or that the objects alone protect") matches the page: protection is "believed", and the things held are "rolled prayers and blessed or holy objects" together, not the objects alone and not the metal shell. The frozen over-reach phrase "credited to those contents rather than to the metal shell" is absent from scope, anchor, teaches, and the entry line. Teaches opens `supersedes S643 —` and is not S643's teaches.

On the page, against the source cell: title `Amulet Box (ga'u)`; `1800-1850 (made)`; Place of origin `Tibet (made)`; Materials and techniques `Silver, brass and coral` (also the gallery label for Museum no. 02805(IS)); Artist/Maker `Unknown`; no author byline. `Record created December 15, 2003` is a catalogue stamp, not a publication imprint, so "no author or publication date" still fits. The summary sentence says "of silver and coral" and omits brass; brass is in the materials field the source cell cites, not in the quote.

## Same page as S643

First URLs are character-identical and both `page_of` to `collections.vam.ac.uk/item/o87367`. The live response is a single `200` (no redirect to another item). The record's own URL field is `https://collections.vam.ac.uk/item/O87367/amulet-box-gau-amulet-box-unknown/`, the same item id. S643's anchor sentence is the Physical description sentence, which is on this page. Later-URL rule does not apply: S651 lists no second URL.

## Entry line

`corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:70` at `47f27bd0cb0bea219f21cd731c2eb0fe71f7f626` (only citation of S651 in that file):

`- Ga'u as container: the V&A record describes this amulet case or ga'u as used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil (S651). **B**`

Carrying sentence: "This amulet case or ga'u of silver and coral, was used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil."

| clause | result |
|---|---|
| Ga'u as container | CARRIED. The page says "amulet case or ga'u" that "was used to hold" those things. It does not use the word "container"; case + hold carry the clause. It does not say the shell protects, and it does not say the objects alone protect. |
| the V&A record describes this amulet case or ga'u | CARRIED. This page is that V&A record and the sentence begins "This amulet case or ga'u". |
| as used to hold rolled prayers | CARRIED. Same sentence: "was used to hold rolled prayers". |
| and blessed or holy objects | CARRIED. Same sentence: "and blessed or holy objects". |
| believed to protect the wearer from evil | CARRIED. Same sentence, "from evil", not the Physical description's "against evil". |

Shared content words between the quote and that line (locator-normalised, length ≥ 4, not the counter's stopwords): believed, blessed, evil, hold, holy, objects, prayers, protect, rolled, used, wearer (11, threshold 6). **B** matches the entry's own key ("carried by the cited row at its stated strength"): the line reports what the record says, and "believed" is the record's word, kept in the clause rather than upgraded to efficacy.

## Commands and full output

```
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 47f27bd0cb0bea219f21cd731c2eb0fe71f7f626:corpus/SOURCES.md | grep -n '^| S651 '
```

```
606:| S651 | Victoria and Albert Museum, London, object record "Amulet Box (ga'u)", made in Tibet, 1800-1850, silver, brass and coral, no author or publication date on the record — https://collections.vam.ac.uk/item/O87367/ (direct plain GET, HTTP 200, 46,556 bytes, accessed 2026-10-23; no live challenge) | docs | A | this V&A record's description of one ga'u/amulet case holding prayers and blessed or holy objects believed to protect its wearer; not evidence of efficacy or that the objects alone protect | summary description paragraph beneath the object title, after its opening words This amulet case or ga'u of silver and coral (not the Physical description catalogue field): "was used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil." | supersedes S643 — the V&A record describes this amulet case or ga'u as used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
```

```
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 47f27bd0cb0bea219f21cd731c2eb0fe71f7f626:corpus/SOURCES.md | grep -n '^| S643 '
```

```
598:| S643 | Victoria and Albert Museum, London, object record "Amulet Box (ga'u)", made in Tibet, 1800-1850, silver, brass and coral, no author or publication date on the record — https://collections.vam.ac.uk/item/O87367/ (direct, HTTP 200, 46,556 bytes) | docs | A | the record's own description of what a body-worn amulet box contains and what its contents are believed to do; not a claim about efficacy | Physical description, first sentence: "An amulet box or ga'u used to contain rolled prayers and blessed or holy objects believed to protect the wearer against evil." | A ga'u is a box holding rolled prayers and sanctified items, and the protection against evil is credited to those contents rather than to the metal shell. | rejected | 2026-10-23 | 2027-10-23 | — |
```

```
sha256sum /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-60/captures/S651.bin
wc -c /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-60/captures/S651.bin
```

```
8e4cf0198005310cc619f48830658bcd1fe2ddda8bdba64d5c86e98128f67c79  /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-60/captures/S651.bin
46556 /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-60/captures/S651.bin
```

Manifest `S651`: `{"bytes": 46556, "content_type": "text/html", "fetched_at": "2026-10-23T05:37:03Z", "file": "S651.bin", "http": 200, "sha256": "8e4cf0198005310cc619f48830658bcd1fe2ddda8bdba64d5c86e98128f67c79", "url": "https://collections.vam.ac.uk/item/O87367/"}`.

```
curl -sS -D headers.txt -o live.html -A 'Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0' -L --max-redirs 5 --max-time 60 'https://collections.vam.ac.uk/item/O87367/'
sha256sum live.html
```

```
CURL_EXIT:0
HTTP/2 200
server: nginx
date: Fri, 23 Oct 2026 07:52:35 GMT
content-type: text/html
content-length: 46556
last-modified: Thu, 06 Aug 2026 20:26:16 GMT
etag: "b5dc-65866b32f8d34"
accept-ranges: bytes
cache-control: max-age=3600
expires: Fri, 23 Oct 2026 08:52:35 GMT
vary: Accept-Encoding
link: <http://schema.org/CreativeWork> ; rel="type"
8e4cf0198005310cc619f48830658bcd1fe2ddda8bdba64d5c86e98128f67c79  live.html
CMP_EXIT:0
```

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && PYTHONDONTWRITEBYTECODE=1 timeout 120 python3 -B reports/round-60/reopen-quote.py --row S651
```

```
LOCATED https://collections.vam.ac.uk/item/O87367/
EXIT:0
```

Visible text of the live body (script and style skipped), the object portion:

```
Amulet Box (ga'u) | Unknown | V&A Explore The Collections
On display
V&A South Kensington
The Himalayas and South-East Asia, Room 47a
Amulet Box (ga'u)
Amulet Box
1800-1850 (made)
Artist/Maker
Unknown
Place of origin
Tibet (made)
This amulet case or ga'u of silver and coral, was used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil. This type of round amulet box was most popular among the nomads of north east Tibet. Such boxes were worn suspended on a strap or sash across the shoulder or around the waist when travelling.
Object details
Category
India Museum
Object type
Amulet box
Ga'u
Title
Amulet Box (ga'u)
Materials and techniques
Silver, brass and coral
Brief description
A round silver amulet box set with a central coral with radiating geometrical decoration on its front.
Physical description
An amulet box or ga'u used to contain rolled prayers and blessed or holy objects believed to protect the wearer against evil.
Gallery label
(14/06/2011)
Three Amulet Cases (Ga’u)
1800–79
Amulet cases were used to hold holy objects or written prayers, believed to protect the wearer from evil. ...
Silver, brass and coral
Museum no. 02805(IS)
Summary
This amulet case or ga'u of silver and coral, was used to hold rolled prayers and blessed or holy objects believed to protect the wearer from evil. This type of round amulet box was most popular among the nomads of north east Tibet. Such boxes were worn suspended on a strap or sash across the shoulder or around the waist when travelling.
Collection
South & South East Asia Collection
Accession number
02805(IS)
Record created
December 15, 2003
Record URL
https://collections.vam.ac.uk/item/O87367/amulet-box-gau-amulet-box-unknown/
```

HTML hits: the "was used to hold" sentence is in `div.object-page__summary` and again under the cell named `Summary`. The "used to contain … against evil" sentence is only under the cell named `Physical description`. Counts in the raw body: `from evil` 3, `against evil` 1, `rolled prayers` 3, `Wayback` 0, `archive.org` 0.

Pin locator check:

```
pin_sha 8e4cf0198005310cc619f48830658bcd1fe2ddda8bdba64d5c86e98128f67c79
live_sha 8e4cf0198005310cc619f48830658bcd1fe2ddda8bdba64d5c86e98128f67c79
pin_len 46556 live_len 46556 equal True
quote_words 18
locate_in_pin True
summary_hold True
physical_contain True
opening True
urls_S651 ['https://collections.vam.ac.uk/item/O87367/']
urls_S643 ['https://collections.vam.ac.uk/item/O87367/']
page_of_S651 ['collections.vam.ac.uk/item/o87367']
page_of_S643 ['collections.vam.ac.uk/item/o87367']
first_url_equal True
shared_content_words ['believed', 'blessed', 'evil', 'hold', 'holy', 'objects', 'prayers', 'protect', 'rolled', 'used', 'wearer'] count 11
old_phrase_in_scope_anchor_teaches_entry False
teaches_opens True
```

Entry citation check: `git grep -F S651` at `47f27bd0` in `corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md` returns only line 70, the line quoted above.
