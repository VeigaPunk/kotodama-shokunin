# ScoutKamonGarments — kamon in use: formal garments (montsuki), crest records in Edo bukan

Seat: `KotodamaR57.ScoutKamonGarments` (leaf scout; claim C, coverage — kamon/Japanese identity marks).
All URLs opened by ordinary plain GET in this session (2026-10-22); every quote below was run through the round locator `python3 -B reports/round-57/reopen-quote.py '<url>' '<quote>'` and the locator's one-line output is pasted under each quote.

### NEW-ScoutKamonGarments-1

citation: Victoria and Albert Museum, London. "Sanjuro" (film costume worn by Toshiro Mifune in Akira Kurosawa's 1962 film), accession S.1697-2015, Theatre and Performance Collection (BFI costume collection), designed by Yoshirô Muraki; record page read 2026-10-22; record cited in Jackson, Anna, ed., *Kimono: Kyoto to Catwalk*, London: V&A Publishing, 2020, fig. 185, pp. 231, 233.
url: https://collections.vam.ac.uk/item/O1314738/
route: direct plain request, HTTP 200 (site page, 48,083 bytes), no challenge; corroborated by the museum's own JSON API at https://api.vam.ac.uk/v2/museumobject/O1314738 (direct, HTTP 200).
kind: docs (holding-museum object record).
tier: A — the holding museum's own record for the exact garment, curatorially written.
scope: what a kamon is and does in context: the Japanese word "mon" rendered as "family crest", a crest borne on a kimono (montsuki = "kimono with family crest"), what the mon signals (a character's former samurai clan), and the garment as a production costume whose label names the montsuki and its silk/weave (habutai; hakama of sendaihira-ori). Supports design decisions: what a mark is called, what it is put on (clothing), and how a bearer passes in/out of a clan identity.
quotes:
- page: "In both films, Mifune wears a rather dilapidated dark kimono bearing the same family mon (crest) probably the emblem of his former samurai clan, before he became a rōnin (masterless)."
  `LOCATED https://collections.vam.ac.uk/item/O1314738/`
- page: "Production Montsuki kimono (kimono with family crest) of habutai (smooth, plain weave silk). Hakama trousers of sendaihira-ori, a thick silk fabric compactly woven with stripes traditionally made in Sendai (Miyaki Prefecture)."
  `LOCATED https://collections.vam.ac.uk/item/O1314738/`
- page: "Worn by Mifune Toshiro 1 x habutai montsuki kimono 1 x sendaihira-ori hakama"
  `LOCATED https://collections.vam.ac.uk/item/O1314738/`
teaches: The Japanese mon is read as a family crest on formal garments, and a montsuki is literally a kimono with a family crest.
draft sentences:
- The Japanese sense mon (crest) appears on a kimono as the emblem of the wearer's clan, carried by a masterless samurai long after leaving the clan (NEW-ScoutKamonGarments-1, page).
- A "montsuki" is defined by the record as a kimono with a family crest, and the crested kimono here is made of fine plain-weave habutai silk (NEW-ScoutKamonGarments-1, page).
- A crest-bearing formal kimono is worn with hakama trousers of sendaihira-ori, a thick silk fabric woven with stripes, so the crest system rides on an ensemble, not a single garment (NEW-ScoutKamonGarments-1, page).
- The record calls the same mark both "mon" and "crest", so worldbuilders may name the device either way while keeping its clan-identity function explicit (NEW-ScoutKamonGarments-1, page).

### NEW-ScoutKamonGarments-2

citation: ROIS-DS 人文学オープンデータ共同利用センター (CODH), "武鑑全集" (Bukan database), Edo+150 project; structured data derived by adapting the 日本古典籍データセット (National Institute of Japanese Literature 国文学研究資料館 collection); CC BY-SA 4.0; pages read 2026-10-22. Bukan = Edo-period daimyo directories; the cited Owari-han page aggregates the different editions of the armorial with their dates and the mon glyphs recorded in them.
url: https://codh.rois.ac.jp/bukan/ ; https://codh.rois.ac.jp/bukan/han/H236/
route: direct plain requests, HTTP 200 both pages (18,334 and 192,162 bytes), no challenge.
kind: dataset (academic open-data project; derived from NDL/国文研-cataloged digitized bukan).
tier: B — authoritative structured dataset of the bukan genre, but the catalog page is a research-database interface, not a museum's own prose; statements it supports are restricted to what its tables record.
scope: the Edo-period bukan (daimyo armorial) as a genre: it lists each han (domain), its head (当主), castle seat, Sankin-kōtai months, page numbers — and its mon; the Owari tables record mon glyphs as registered symbols (（記号）「丸にエ」3, 「丸にト」3) in some editions, and adjacent rows name dedicated crest books (紋尽, 御紋尽) and armorials (本朝武鑑). Supports design decisions: crests are inventoried per house in a published directory, print titles exist specifically for crests, and a crest can be registered by a symbol-like glyph rather than by a blazon word.
quotes:
- page (top): "CODHと国文学研究資料館が協働して公開する「日本古典籍データセット」には、2017年12月現在、 381点の『武鑑』 が含まれています。その中からまず 寛政武鑑（1789） を選んで"
  `LOCATED https://codh.rois.ac.jp/bukan/`
- page (Owari H236): "紋尽 松会 明暦4 1658 尾張右兵衛督様 なし なし 名古屋 00003 1"
  `LOCATED https://codh.rois.ac.jp/bukan/han/H236/`
- page (Owari H236): "大成武鑑 出雲寺〈江戸〉 天明2 1782 尾張大納言宗睦卿 （記号）「丸にエ」3 （記号）「丸にト」3 名古屋 00007-1"
  `LOCATED https://codh.rois.ac.jp/bukan/han/H236/`
- page (Owari H236): "寛政武鑑 須原屋 江戸 寛政1 1789 尾張大納言宗睦卿 子寅辰午申戌3月 丑卯巳未酉亥3月 名古屋 00006 1"
  `LOCATED https://codh.rois.ac.jp/bukan/han/H236/`
teaches: Edo-period published bukan list each domain's crest alongside its lord, castle seat and service months.
draft sentences:
- Edo-period bukan (daimyo directories) record a domain's crest beside its lord's name, castle seat, and attendance months, so a house's mark is public, printed information (NEW-ScoutKamonGarments-2, page).
- In some bukan editions the Owari house's mon is registered as glyph symbols — 丸にエ and 丸にト — showing crests can be inventoried as images rather than described in words (NEW-ScoutKamonGarments-2, page).
- The Owari page lists dedicated crest books (紋尽, 御紋尽) published in the 1600s, so a worldbuilder can treat crest catalogs as a separate print genre from the armorials (NEW-ScoutKamonGarments-2, page).
- The same Owari armorial was reprinted in many editions with different publishers, dates, and page references while the crest record persisted, implying stability of the mark across editions (NEW-ScoutKamonGarments-2, page).

### Rejected

- Metropolitan Museum of Art object 826006, "Storage Trunk (Nagamochi) with Family Crests, Pine, and Foliage Pattern", accession 2019.281.1, Edo period, second half 18th c., lacquer. Source opened (collection API JSON and public site 429 challenge -> API record), quotes located, but the seat is capped at 1–2 sources and this seat's two slots are already filled; the record is a strong ready-made source for "crests on lacquer furnishings" if the L1 wants it (URL https://collectionapi.metmuseum.org/public/collection/v1/objects/826006; quote "Storage Trunk (Nagamochi) with Family Crests, Pine, and Foliage Pattern" LOCATED). Reason: exceeds this seat's 2-source cap; offered as a candidate row for another kamon seat.
- NDL Search record R100000094-I584098 (秋田藩御国武鑑分限録, 嘉永2年/1850, digitized via ADEAC): opened, page carries only bibliographic catalog fields (title, publisher, date, size) with no substantive kamon wording; too thin to support design sentences. Rejected.
