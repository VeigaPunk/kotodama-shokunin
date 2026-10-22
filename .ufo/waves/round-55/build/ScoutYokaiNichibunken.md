# ScoutYokaiNichibunken — Japanese yōkai catalogues and a Sekien holding record

Claim C source seat. Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `f4015e7`.
Scope: the Nichibunken Kaii-Yōkai Denshō Database's own statements about its scope and
method, and a national-library record of Toriyama Sekien's *Gazu hyakki yagyō* (1776), plus two
Metropolitan Museum records of Sekien and Kyōsai monster books already fetched while checking
for a 1776 holding record. Everything below was opened in this session by plain request;
`python3` was used only to read and search saved bytes, never to fetch past a block.

## Sources

### NEW-ScoutYokaiNichibunken-1

citation: International Research Center for Japanese Studies (Nichibunken), Yōkai Project Office; text signed Manami Yasui Ph.D. and Shoji Yamada Ph.D., March 2025. "Overview of the Yōkai Database" (English-language overview of the 怪異・妖怪伝承データベース / Kaii-Yōkai Denshō Database). No DOI or ISBN; page version March 2025.
url: https://www.nichibun.ac.jp/YoukaiDB/english_kaisetsu.html
route: direct plain request, HTTP 200, 30,166 bytes, full page read, no challenge served. Access date 2026-10-22.
kind: web
tier: A — the institution that builds and publishes the database states its own scope, method and glossary on its own site; authoritative for those statements, not for the content of any individual database record.
scope: what the database collects and excludes; the three-domain definition of yōkai the centre adopts; the glossary senses of yōkai, kaii, kami, oni and yūrei; the page's own dated entry count. It does not describe any single being and carries no iconography.
quotes:
- What is Yōkai Culture?, Komatsu quoted at p.12: "yōkai as incidents or phenomena, yōkai as supernatural entities or presences, and yōkai as depictions"
- Glossary, 怪異 kaii: "which were considered omens (zenchō 前兆), warnings, or punishment"
- Glossary, 鬼 oni, first paragraph: "Oni are not necessarily evil and can become a kami if worshipped (as Komatsu Kazuhiko argues)."
- Glossary, 鬼 oni, Buddhist associations, item 4: "who assist King Enma and who have ox or horse heads (gozumezu 牛頭馬頭)"
teaches: Defines yōkai across three domains, ties kaii anomalies to omens and punishment, and shows oni ranging from invisible presences to ox-headed hell wardens that may become kami.
draft sentences:
- The centre's own outline splits yōkai into incidents or phenomena, supernatural entities or presences, and depictions, so a culture's monster word may name an event or a picture as well as a creature (NEW-ScoutYokaiNichibunken-1, What is Yōkai Culture?, quoting Komatsu p.12).
- In the glossary, kaii anomalies follow cosmic unbalance or social disorder and are read as omens, warnings or punishment, which makes a monster a readable sign and not only a dangerous body (NEW-ScoutYokaiNichibunken-1, Glossary 怪異).
- The same glossary says oni are not necessarily evil and can become kami when worshipped, so the border between monster and deity is a decision about cult, not a fixed taxonomy (NEW-ScoutYokaiNichibunken-1, Glossary 鬼, first paragraph).
- Buddhist hell wardens in the oni entry assist King Enma and carry ox or horse heads, while demon-gods (kijin) protect the buddha and people, so one class holds both punishing composite bodies and guardians (NEW-ScoutYokaiNichibunken-1, Glossary 鬼, Buddhist associations).
- The page records entries as a name plus a locality — a three-legged fox in Kurosawa — so the unit of the catalogue is a named being at a place, not a species in a list (NEW-ScoutYokaiNichibunken-1, Key Features).
- It reports 3,300 records for the common name kitsune and 35,257 entries as of November 2023, so frequency belongs to the local case, while the general name gathers thousands of them (NEW-ScoutYokaiNichibunken-1, Overview of the Yōkai Database).

### NEW-ScoutYokaiNichibunken-2

citation: International Research Center for Japanese Studies (Nichibunken). 怪異・妖怪伝承データベース「概要」 (outline page of the Kaii-Yōkai Denshō Database), undated page, data counts stated as of April 2023, copyright notice 2002–. No author line.
url: https://www.nichibun.ac.jp/YoukaiDB/gaiyou.html
route: direct plain request, HTTP 200, 24,579 bytes, full page read. Access date 2026-10-22.
kind: web
tier: A — the database's own method statement, published by the institution that runs it; authoritative for the cataloguing rules it states and for its own dated count.
scope: the database's stated purpose, its source bibliographies, what it excludes, and the rules by which a being is named and grouped. Useful for a worldbuilder deciding what a bestiary may coin and when two local names count as one being. Gives no being-level descriptions.
quotes:
- 凡例【呼称】, opening sentence: "原則として、貼り付け事例からそのままの呼称を記入した"
- 凡例【呼称】, the sentence on naming: "カード作成者による命名はしないことを原則とした。"
- 利用【代表的な怪異・妖怪の呼称からの検索】: "「カッパ」「ガッパ」などの、語法による表記のゆらぎがあっても同じ怪異・妖怪として検索することができる"
- 利用【代表的な怪異・妖怪の呼称からの検索】, following sentence: "「カワタロウ」「エンコ」のように表記が大きく異なる場合は、「カッパ」には含めていない。"
teaches: Records how a folklore database names beings — designation copied verbatim, no naming by the cataloguer, a stated threshold for merging variants — and what it omits by principle.
draft sentences:
- The outline says each designation is copied as it stands from the source card and that the card-maker's naming is refused, so a bestiary that coins monster names is doing something this folklore record does not do (NEW-ScoutYokaiNichibunken-2, 凡例【呼称】).
- Kappa and gappa are searched as one being because the difference is only orthographic, while kawatarō and enko stay outside kappa because their names differ too far, so the identity of a being is a stated rule with a threshold rather than a fact (NEW-ScoutYokaiNichibunken-2, 利用【代表的な怪異・妖怪の呼称からの検索】).
- The corpus excludes mukashi banashi by principle and gathers cases from the early modern period to the present, so the genre boundary decides what a world's bestiary may treat as testimony (NEW-ScoutYokaiNichibunken-2, 収録データ).
- The outline gives 35,255 cases as of April 2023, so any count of a being or a name is a dated snapshot of a growing file rather than a property of the tradition (NEW-ScoutYokaiNichibunken-2, 収録データ).

### NEW-ScoutYokaiNichibunken-3

citation: National Diet Library, NDL Search record 畫圖百鬼夜行 3巻, author 鳥山石燕豐房 [画], publishers 出雲寺和泉椽 : 遠州屋弥七, 安永5 [1776], 22.2 × 16.0 cm, supplied through CiNii Books; DOI 10.20730/300103729 to the National Institute of Japanese Literature 国書データベース. Record ID R100000136-I1971149384742718736.
url: https://ndlsearch.ndl.go.jp/books/R100000136-I1971149384742718736
route: direct plain request, HTTP 200, 254,231 bytes, full record read. DOI resolved 2026-10-22: HTTP 302 to https://kokusho.nijl.ac.jp/biblio/300103729 (HTTP 200, a JavaScript shell) and its IIIF manifest at https://kokusho.nijl.ac.jp/biblio/300103729/manifest (HTTP 200, application/json), whose attribution line names 専修大学図書館 and 国文学研究資料館. The record page bytes ship an AWS WAF challenge script but the record text is served in the plain response; no challenge was met or needed. Access date 2026-10-22.
kind: book
tier: A — a national library catalogue record of the 1776 edition, transcribed from the copy, including the book's own colophon, preface and postscript wording; authoritative for publication data, collation and paratext dates, not for reading the pictures.
scope: the 1776 edition's imprint, size, part structure, paratext dates, title source and alternative title, and the fact that the described copy is a later impression. Says nothing about which beings the book depicts.
quotes:
- 一般注記: "前偏隂: [2], 7丁, 前偏陽: [1], 11丁, 前偏風: [1], 8, [1]丁"
- 一般注記, colophon note: "刊記に「安永五丙申春」「御書房 出雲寺和泉椽開版 書林 遠州屋弥七」とあり"
- 一般注記, title note: "本タイトルは題簽より (「畫圖」は角書)"
- 一般注記, postscript note: "前偏風に「きのとの未の秋菊月 於月窗下 石燕自跋」あり"
teaches: Gives the 1776 edition's imprint and collation — three parts labelled 隂, 陽 and 風, a title taken from the title slip, a later impression, paratexts dated 1775.
draft sentences:
- The national library records the book as three volumes of 22.2 × 16.0 cm issued by the two houses named in the colophon, a small picture-book format rather than a folio or a scroll (NEW-ScoutYokaiNichibunken-3, 出版事項 and 大きさ).
- Its notes split the work into parts labelled 隂, 陽 and 風 with separate sheet counts, so the bestiary is ordered by named sections rather than by alphabet, region or being-type label (NEW-ScoutYokaiNichibunken-3, 一般注記).
- The title is taken from the title slip with "gazu" set as a corner title, and the Kokusho sōmokuroku gives the alternative title Ehon hyakki yagyō, so one book travels under several names a canon must choose between (NEW-ScoutYokaiNichibunken-3, 一般注記).
- The copy is a later impression, and its framing predates the spring 1776 colophon: a preface dated the winter of the 乙未 year and Sekien's own postscript in the wind part dated the autumn of that year (NEW-ScoutYokaiNichibunken-3, 一般注記).

### NEW-ScoutYokaiNichibunken-4

citation: Metropolitan Museum of Art, New York. "One Hundred Monsters Ancient and Modern (Hyakki shūi) 百鬼拾遺", Toriyama Sekien 鳥山石燕 (Japanese, 1712–1788), 1781 spring (An'ei 10), accession 2013.803, Asian Art, classification Illustrated Books. Collection API record for object 78693, metadata date 2025-03-06.
url: https://collectionapi.metmuseum.org/public/collection/v1/objects/78693
route: direct plain request to the Met Collection API, HTTP 200, application/json, 5,294 bytes, full record read. The public page https://www.metmuseum.org/art/collection/search/78693 answered a plain request with HTTP 429 and was not read. Access date 2026-10-22.
kind: record
tier: A — the holding museum's own catalogue data for the object; authoritative for its fields and index terms, and silent on anything it does not field.
scope: the physical format, date and title forms of one Sekien monster book, and the museum's index terms for it. No curatorial essay, no statement about the beings drawn and no mention of the 1776 volume.
quotes:
- medium field: "Set of three woodblock printed books bound as one volume; ink on paper"
- objectDate field: "1781, spring (An'ei 10)"
- title field, first form: "One Hundred Monsters Ancient and Modern (Hyakki shūi) 百鬼拾遺"
- dimensions field: "8 7/8 × 6 5/16 in. (22.5 × 16 cm)"
teaches: Records a Sekien monster book as three woodblock books bound as one 22.5 × 16 cm volume dated 1781, with competing title forms and index terms for animals and houses.
draft sentences:
- The Met describes the object as three woodblock printed books bound as one volume of 22.5 × 16 cm, so the unit of this bestiary is a bound set of pictures, not a scroll or a single print (NEW-ScoutYokaiNichibunken-4, medium and dimensions).
- The museum dates it to spring 1781 and files it under Illustrated Books, so the monster book enters the collection as a book rather than as a painting or a single print (NEW-ScoutYokaiNichibunken-4, objectDate and classification).
- Its title field carries three forms — Hyakki shūi, Konjaku hyakki shūi and Hyakki yagyō shūi — so museum and library titles diverge for one work and a canon has to pick one (NEW-ScoutYokaiNichibunken-4, title).
- The museum indexes the volume under crabs, snails and houses, so its pictures take in animals and buildings, not only human-shaped monsters (NEW-ScoutYokaiNichibunken-4, tags).

### NEW-ScoutYokaiNichibunken-5

citation: Metropolitan Museum of Art, New York. "Kyōsai's Pictures of One Hundred Demons (Kyōsai hyakki gadan) 暁斎百鬼画談", Kawanabe Kyōsai 河鍋暁斎 (1831–1889), 1890 with the first edition published posthumously in 1889, accession 2013.767, Meiji period, classification Illustrated Books. Collection API record for object 78669.
url: https://collectionapi.metmuseum.org/public/collection/v1/objects/78669
route: direct plain request to the Met Collection API, HTTP 200, application/json, full record read; the public page at metmuseum.org was rate-limited (HTTP 429) earlier and not read. Access date 2026-10-22.
kind: record
tier: A — the holding museum's own catalogue data for the object; authoritative for its fields and index terms only.
scope: one later monster book's date, edition note, binding, period and index terms — evidence that the bestiary format continues after Sekien with a different binding and vocabulary.
quotes:
- title field: "Kyōsai’s Pictures of One Hundred Demons (Kyōsai hyakki gadan) 暁斎百鬼画談"
- objectDate field: "1890 (first edition published posthumously in 1889)"
- medium field: "Woodblock printed book (orihon, accordion-style); ink and color on paper"
teaches: Records a later monster picture book, Kyōsai's, dated 1890 after a posthumous 1889 first edition, bound accordion-style and indexed under mythical creatures and demons.
draft sentences:
- The Met holds a monster picture book by Kyōsai dated 1890, with the first edition published posthumously in 1889, so the bestiary outlives its author and its date must name the edition (NEW-ScoutYokaiNichibunken-5, objectDate).
- Its binding is orihon, accordion-style, where the Sekien volume is described as three woodblock books bound as one, so the physical form of the monster book changes across the century (NEW-ScoutYokaiNichibunken-5, medium).
- The museum indexes this book under mythical creatures and demons rather than the 1781 volume's crabs, snails and houses, so the cataloguing vocabulary itself shifts across the century (NEW-ScoutYokaiNichibunken-5, tags).

## Findings for the L1

1. **Counts are dated snapshots, and they disagree.** The English overview says 35,257 entries
   as of November 2023; the Japanese outline says 35,255 as of April 2023; the live search page
   (https://www.nichibun.ac.jp/YoukaiDB/search.html, read this session) prints 35,307 and is
   undated. Quote any count with its date and page, and never average them.
2. **Same name, different counts across pages.** The English page reports 3,300 records for
   kitsune; the search page's shortcut list reports about 3,700, then tengu about 1,300, kappa
   about 1,100, tanuki about 1,000, hebi about 960, daija about 800, yūrei about 690, oni about
   670, tatari about 650, hinotama about 530, yamanokami about 490, mujina about 460. These are
   record counts, not being counts, and the two pages were written at different times.
3. **The naming rule is the strongest design material here.** The database refuses cataloguer
   coinage, copies designations verbatim, merges orthographic variants only within a stated
   threshold (kappa/gappa yes; kawatarō/enko no). An entry that asks "what does this culture call
   the being" can cite this as a working method, not just a fact.
4. **Genre boundary.** Nichibunken omits mukashi banashi by principle, and the English overview
   calls the excluded works those widely regarded as fictional; what remains is reports, essays
   and oral accounts from the early modern period on. That makes it a legend and experience-report
   file, complementary to the TMI/ATU rows (S013, S016) rather than a duplicate of them.
5. **Order of the 1776 book.** The record gives three parts labelled 隂, 陽, 風 with sheet counts
   ([2]+7, [1]+11, [1]+8+[1]). [INFERENCE] The labels are cosmological rather than thematic and
   nothing I opened states the assignment principle; do not claim the book groups beings by
   yin/yang. Unresolved.
6. **Format continuity.** 22.2 × 16.0 cm (NDL, 1776) against 22.5 × 16 cm (Met, 1781) is
   effectively one format across the two Sekien volumes, both in the same small picture-book size.
7. **Title instability.** 畫圖百鬼夜行 / 画図百鬼夜行; Kokusho sōmokuroku alternative 絵本百鬼夜行;
   Met's 1781 volume carries 百鬼拾遺, 今昔百鬼拾遺 and 百鬼夜行拾遺. A canon section must choose one
   title per work and record the others as variants.
8. **Later period.** Kyōsai 1890 (posthumous 1889 first edition) is a Meiji monster picture book in
   orihon binding, indexed under mythical creatures and demons — a usable period-change datum for
   "what changes across periods".
9. **What these rows cannot carry.** No source opened here says Sekien invented these beings, none
   gives a restriction, vow or taboo rule for a being, and the Met records contain no curatorial
   text. Sacred or restricted beings must be supported by another seat's community or heritage-body
   source, not by these rows.
10. **Access notes that belong in the row cells.** The NDL record page ships an AWS WAF challenge
    script yet served its full record to a plain request; nothing was bypassed. The Met object
    pages returned HTTP 429, so the API record is the opened artifact. No tool was installed or
    upgraded this session.

## unopened

- https://library.si.edu/digital-library/book/gazuhyakkiyagyo1tori — Smithsonian Libraries record of a digitized *Gazu hyakki yagyō* (1805 printing, "1st published 1776. Cf. Colophon"); connection timed out three times (25 s, 40 s, 60 s) from this host. Its Internet Archive metadata record was read instead only to locate the object, and is not filed as a row because I did not read the holding library's own record.
- https://blog.library.si.edu/blog/2016/10/14/toriyama-sekiens-spooky-parade/ — HTTP 403 to a plain request.
- https://www.britishmuseum.org/collection/search?keyword=gazu+hyakki+yagyo — HTTP 403.
- https://collections.mfa.org/search/objects/*/hyakki — HTTP 403.
- https://cir.nii.ac.jp/crid/1971149384742718736 — HTTP 202 with an empty body.
- https://kokusho.nijl.ac.jp/biblio/300103729 — served a 4,869-byte JavaScript shell with no record text; only its IIIF manifest answered, which I used for the attribution line.
- https://www.nichibun.ac.jp/YoukaiDB/ — a 6,404-byte frame shell with no prose; its search page was read but not filed as its own row.
- https://www.nichibun.ac.jp/YoukaiDB/kwaii.html and …/seisaku.html — fetched (HTTP 200) but not read in depth; not filed.
- Metropolitan Museum collection search API v1 — retired 2026-10-01 with a message naming v1.1; not a source, only an access note.
