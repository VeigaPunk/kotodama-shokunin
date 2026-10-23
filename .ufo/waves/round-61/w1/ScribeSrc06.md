# Round 61 W1 — ScribeSrc06 source report

## Behavior and coverage
Drafted five source/entry/Gate sets for claim C: two on footwear removal at Japanese home/temple and mosque prayer-hall thresholds, plus three on Indigenous North American moccasins. Each kept anchor quote was read from its source page or the public Wayback capture and returned `LOCATED` from the round-61 quote locator. Source IDs are placeholders (`S6??`) because no unique range was assigned to this seat in the provided context; the integration owner must replace them with distinct IDs in S652–S699 before use.

## Draft SOURCES rows, entry clauses, and Gate lines

### 1. Japanese genkan / temples (Nippon.com; tier B)

`| S6?? | Nippon.com, "The “Genkan”: Japan’s Traditional Entryway and Footwear Etiquette," 20 August 2024 — https://www.nippon.com/en/guide-to-japan/gu020004/ | docs | B | Japanese genkan/home threshold custom; home footwear removal also applies to ryokan inns, temples, and restaurants with tatami-floored rooms | Body text: "Japanese custom of removing footwear before entering a home. The same applies to ryokan inns, temples, and even restaurants with tatami-floored rooms" | Japanese footwear removal before home entry also applies to ryokan inns, temples, and restaurants with tatami-floored rooms. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |`

- Japan's footwear-removal custom for entering a home extends to ryokan inns, temples, and restaurants with tatami-floored rooms. (S6??)
- S6?? | https://www.nippon.com/en/guide-to-japan/gu020004/ | 2026-10-23 | "Japanese custom of removing footwear before entering a home. The same applies to ryokan inns, temples, and even restaurants with tatami-floored rooms"

### 2. Mosque prayer hall (Visit My Mosque / Muslim Council of Britain; tier A for its visitor guidance)

`| S6?? | Muslim Council of Britain, "Visitor's Guide — Visit My Mosque 2026," n.d. — https://vmm.mcb.org.uk/visiting-a-mosque-guide | docs | A | Visit My Mosque visitor guidance for shoe removal before entering a mosque prayer hall | Under "What do I wear?": "You'll be asked to remove your shoes before entering the prayer hall" | The guide asks visitors to remove shoes before entering the prayer hall. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |`

- Mosque visitors are asked to remove their shoes before entering the prayer hall. (S6??)
- S6?? | https://vmm.mcb.org.uk/visiting-a-mosque-guide | 2026-10-23 | "You'll be asked to remove your shoes before entering the prayer hall"

### 3. Oklahoma Shawnee moccasins (National Museum of the American Indian; tier A)

`| S6?? | National Museum of the American Indian, "Moccasins" (catalog no. 2/5636), n.d. — https://americanindian.si.edu/collections-search/object/NMAI_26904 ; capture https://web.archive.org/web/20250612214229id_/https://americanindian.si.edu/collections-search/object/NMAI_26904 | docs | A | Oklahoma Shawnee moccasins record with listed materials and techniques | Object name, media/materials, and techniques fields: "Object Name Moccasins Media/Materials Elk hide/skin, hide thong/babiche, paint Techniques Sewn, painted" | The catalog lists elk hide, hide thong, paint, and sewn and painted techniques for moccasins. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |`

- The moccasins are listed with elk hide, hide thong, paint, and sewn and painted techniques. (S6??)
- S6?? | https://web.archive.org/web/20250612214229id_/https://americanindian.si.edu/collections-search/object/NMAI_26904 | 2026-10-23 | "Object Name Moccasins Media/Materials Elk hide/skin, hide thong/babiche, paint Techniques Sewn, painted"

### 4. Northern Plains moccasins (Canadian Museum of History; tier A)

`| S6?? | Canadian Museum of History (legacy Civilization.ca exhibit), "Moccasins — Introduction," curator Morgan Baillargeon, n.d. — https://www.historymuseum.ca/cmc/exhibitions/aborig/mocasin/mocintre.html | docs | A | Museum exhibit describes Northern Plains moccasins as practical and stylish footwear | Body introduction: "The moccasin, the Aboriginal footwear of the Northern Plains, is no different: it is also both practical and stylish" | The exhibit describes Northern Plains moccasins as both practical and stylish footwear. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |`

- Northern Plains moccasins are both practical and stylish footwear. (S6??)
- S6?? | https://www.historymuseum.ca/cmc/exhibitions/aborig/mocasin/mocintre.html | 2026-10-23 | "The moccasin, the Aboriginal footwear of the Northern Plains, is no different: it is also both practical and stylish"

### 5. Nêhiyawak moccasins (McCord Stewart Museum; tier A for its collection caption)

`| S6?? | McCord Stewart Museum, "Indigenous Cultures" collection page, n.d. — https://www.musee-mccord-stewart.ca/en/collections/indigenous-cultures/ | docs | A | Collection-page caption identifies Nêhiyawak moccasins dated 1920 and their gift/accession | Caption: "Moccasins, Nêhiyawak, 1920. Gift of the Art Association of Montreal, ME928.8.1-2" | The caption lists Nêhiyawak moccasins dated 1920 as a gift of the Art Association of Montreal. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |`

- The caption lists Nêhiyawak moccasins dated 1920 as a gift of the Art Association of Montreal. (S6??)
- S6?? | https://www.musee-mccord-stewart.ca/en/collections/indigenous-cultures/ | 2026-10-23 | "Moccasins, Nêhiyawak, 1920. Gift of the Art Association of Montreal, ME928.8.1-2"

## Locator and registry evidence

Commands below were run with `timeout 300`; outputs and exit codes are reproduced. The five retained quotes are the outputs labelled `LOCATED` for the corresponding source rows above.

- `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.nippon.com/en/guide-to-japan/gu020004/' 'Japanese custom of removing footwear before entering a home. The same applies to ryokan inns, temples, and even restaurants with tatami-floored rooms'` → `LOCATED https://www.nippon.com/en/guide-to-japan/gu020004/`; exit 0.
- `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://vmm.mcb.org.uk/visiting-a-mosque-guide' "You'll be asked to remove your shoes before entering the prayer hall"` → `LOCATED https://vmm.mcb.org.uk/visiting-a-mosque-guide`; exit 0.
- `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://web.archive.org/web/20250612214229id_/https://americanindian.si.edu/collections-search/object/NMAI_26904' 'Object Name Moccasins Media/Materials Elk hide/skin, hide thong/babiche, paint Techniques Sewn, painted'` → `LOCATED https://web.archive.org/web/20250612214229id_/https://americanindian.si.edu/collections-search/object/NMAI_26904`; exit 0.
- `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.historymuseum.ca/cmc/exhibitions/aborig/mocasin/mocintre.html' 'The moccasin, the Aboriginal footwear of the Northern Plains, is no different: it is also both practical and stylish'` → `LOCATED https://www.historymuseum.ca/cmc/exhibitions/aborig/mocasin/mocintre.html`; exit 0.
- `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.musee-mccord-stewart.ca/en/collections/indigenous-cultures/' 'Moccasins, Nêhiyawak, 1920. Gift of the Art Association of Montreal, ME928.8.1-2'` → `LOCATED https://www.musee-mccord-stewart.ca/en/collections/indigenous-cultures/`; exit 0.

Other quote attempts, not used in the five drafts:

- `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.nippon.com/en/japan-glances/jg00129/' 'At the entrances of hot springs and sentō public bathhouses, shrines and temples, and Japanese restaurants where diners sit on the floor, shoes come off'` → `NOT_LOCATED https://www.nippon.com/en/japan-glances/jg00129/ quote-absent`; exit 1. The follow-up quote was located: `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.nippon.com/en/japan-glances/jg00129/' 'shoes come off at the entrances of hot springs and sentō public bathhouses shrines and temples'` → `LOCATED https://www.nippon.com/en/japan-glances/jg00129/`; exit 0. This page was not retained because the genkan article's selected quote already covers temples.
- `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://vmm.mcb.org.uk/visiting-a-mosque-guide' 'You will be asked to remove your shoes before entering the prayer hall easy to slip off shoes help'` → `NOT_LOCATED https://vmm.mcb.org.uk/visiting-a-mosque-guide quote-absent`; exit 1. A normalized wording attempt then located the page, and the final exact anchor quote above was independently run and located.
- `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.musee-mccord-stewart.ca/en/blog/a-fascinating-pair-of-boots/' 'However, these goods were only a small part of their commercial activity as they manufactured moccasins, snowshoes, and boots on an almost industrial scale'` → `LOCATED https://www.musee-mccord-stewart.ca/en/blog/a-fascinating-pair-of-boots/`; exit 0. This extra McCord page was not retained; the collection caption was the more direct object record for the selected three-source Indigenous subtopic set.

Registry search: `functions.grep` over `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`, pattern `nippon.com/en/guide-to-japan/gu020004|nippon.com/en/japan-glances/jg00129|vmm.mcb.org.uk/visiting-a-mosque-guide|americanindian.si.edu/collections-search/object/NMAI_26904|historymuseum.ca/cmc/exhibitions/aborig/mocasin/mocintre.html|musee-mccord-stewart.ca/en/collections/indigenous-cultures|musee-mccord-stewart.ca/en/blog/a-fascinating-pair-of-boots` → `No matches found`.

NMAI live-page access: `read` on `https://americanindian.si.edu/collections-search/object/NMAI_26904` and the Smithsonian catalog mirror `https://collections.si.edu/search/detail/edanmdm:nmai_26904` both failed with HTTP 403. The ordinary Wayback availability request was `timeout 300 curl -s 'https://archive.org/wayback/available?url=https://americanindian.si.edu/collections-search/object/NMAI_26904'`; stdout: `{"url": "https://americanindian.si.edu/collections-search/object/NMAI_26904", "archived_snapshots": {"closest": {"status": "200", "available": true, "url": "http://web.archive.org/web/20250612214229/https://americanindian.si.edu/collections-search/object/NMAI_26904", "timestamp": "20250612214229"}}}`. The HTTPS `id_` capture was read and the locator returned `LOCATED` as shown above. No CAPTCHA, paywall, or bot challenge was observed or passed; the live 403 is recorded as an access failure, not as a verified challenge.

## Gates, touched surfaces, and limits

- Source-level gates evidenced here: all five kept quotes located; one combined registry grep found no matching existing host/path; all proposed rows set `mined`, `2026-10-23`, `180d`, and the specified used-by path. These are draft records only.
- `ACCEPT-C-61` was not run; neither the entry, `SOURCES.md`, `corpus/README.md`, nor acceptance counters were modified. No build, test, or source-access checker was run by this scribe.
- Opened pages: three candidates for footwear-removal (two retained) and four museum pages/endpoints for Indigenous moccasins (three retained; the extra McCord blog was opened and not retained). This is one page above the 1–3 source target for the Indigenous subtopic; the retained source set stays within the three-source limit.
- Source discovery used web-search results as leads; all kept quotations and metadata were checked on page text via `read` or the public Wayback capture and were independently located by the ordinary quote locator. No browser or challenge bypass was used.
- No tools installed or updated. No delegation, background job, git/jj write, or product-file write was made. The only write is this report.

## Artifact

- `.ufo/waves/round-61/w1/ScribeSrc06.md`
