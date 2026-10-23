# ScoutJapanPlaceNames — round 58, claim C source item (S530, S531)

Two rows offered, both tier A papers that the Geospatial Information Authority of Japan (GSI; called the Geographical Survey Institute before 2010) prepared for UNGEGN sessions. Both are served by unstats.un.org (direct plain GET, HTTP 200, application/pdf). Neither URL is in `corpus/SOURCES.md`: `grep -cF` gives 0 for `wp65-changes`, `WP22_11_29UNGEGN`, `unstats.un.org/unsd/geoinfo/ungegn/docs/25th` and `unstats.un.org/unsd/geoinfo/ungegn/docs/29th`. Live gsi.go.jp cannot be offered, because the frozen locator cannot fetch it (see `rejected:`).

Worldbuilder decisions covered:
- **S530:** who may give a merged settlement its new name and under what rule, and which sources the name is drawn from (a wider area, a natural feature, a revived old province name, a compound of characters, an auspicious word).
- **S531:** what a name is built from (a specific part plus a final generic kanji) and how outsiders mangle it (romanization loses the generic; English substitution and addition formats).

## Registry rows

| S530 | Geographical Survey Institute (Ministry of Land, Infrastructure, Transport and Tourism of Japan), 2009, "Changes in the Names of New Municipalities through Municipality Mergers in Japan", UNGEGN Twenty-fifth session (Nairobi, 5–12 May 2009), Working Paper No. 65 — https://unstats.un.org/unsd/geoinfo/ungegn/docs/25th-gegn-docs/wp%20papers/wp65-changes%20in%20names-japan.pdf (direct, HTTP 200) | paper | A | where new Japanese municipal names came from in the Meiji, Showa and Heisei mergers, and the legal rules on naming a new municipality | PDF p. 5, §5 Conclusions, item (1): "many names have been generated using names of wider areas, names that originated from natural features, or old province names" | In the Heisei mergers most new municipal names were drawn from wider areas, natural features or revived old province names. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S531 | Geospatial Information Authority of Japan (Ministry of Land, Infrastructure, Transport and Tourism), submitted by Japan, 2016, "Investigation of rules for translating Japanese geographical names into English", UNGEGN Twenty-ninth session (Bangkok, 25–29 April 2016), Working Paper No. 22/11 — https://unstats.un.org/unsd/geoinfo/ungegn/docs/29th-gegn-docs/WP/WP22_11_29UNGEGN_REPORT_JAPAN.pdf (direct, HTTP 200) | paper | A | how a Japanese natural-feature name splits into a specific part and a final generic kanji, and GSI's substitution and addition formats for English renderings | PDF p. 5, §4(1)1)(a): "Most Japanese geographical names are written in Kanji (Chinese characters), and characters that express geographical features are usually added to the end of the word." | Most Japanese place names put a kanji naming the feature type, such as mountain or river, at the end of the name. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Notes for the L1:
- **S530 quote:** this is the second clause of conclusion (1). The full sentence reads "During previous mergers, there were relatively many compound names created due to official directives; however, during the rece nt Heisei mergers, many names have been generated …". The pypdf text layer splits "rece nt", so the quote starts after the break. The "Heisei" in the teaches cell is carried by that same sentence. Section 2 also says it directly: 598 municipalities were formed by merger from 1 April 1999 to 1 January 2008; 330 kept existing names and 268 got new names.
- **Avoid broken spans:** the pypdf layer of both PDFs splits some words ("muni cipality", "ci ty", "in cluding", "g eographical"). A new quote that crosses one of these splits will fail LOCATE.
- **Page numbers:** both "PDF p. 5" values are PDF page indices checked with pypdf 5.4.0. They are not the papers' printed page numbers.
- **Table text:** the S530 Table 1 rows (for example the six towns named 'Misato', or the 26 names from rivers) are table cells. Use them only as page-carried detail in sentences, never as a quote.

## Gate lines

- S530 — https://unstats.un.org/unsd/geoinfo/ungegn/docs/25th-gegn-docs/wp%20papers/wp65-changes%20in%20names-japan.pdf — accessed 2026-10-23 — PDF p. 5, §5 Conclusions, item (1): “many names have been generated using names of wider areas, names that originated from natural features, or old province names”. Grounds: In the Heisei mergers most new municipal names were drawn from wider areas, natural features or revived old province names. Seat: ScoutJapanPlaceNames.
- S531 — https://unstats.un.org/unsd/geoinfo/ungegn/docs/29th-gegn-docs/WP/WP22_11_29UNGEGN_REPORT_JAPAN.pdf — accessed 2026-10-23 — PDF p. 5, §4(1)1)(a): “Most Japanese geographical names are written in Kanji (Chinese characters), and characters that express geographical features are usually added to the end of the word.” Grounds: Most Japanese place names put a kanji naming the feature type, such as mountain or river, at the end of the name. Seat: ScoutJapanPlaceNames.

## rowcheck output

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutJapanPlaceNames/rows.md` (exit 0):

```
S530 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://unstats.un.org/unsd/geoinfo/ungegn/docs/25th-gegn-docs/wp%20papers/wp65-changes%20in%20names-japan.pdf | BOILER: root-clear https://unstats.un.org/; not a title, h1 or meta label | RELEVANCE: shared=['area', 'featu', 'name', 'natur', 'provi', 'wider'] | TOPIC: quote_hits=1 function_words=5 page_hits=19 page_terms=5 need=1/2/3/2
S531 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://unstats.un.org/unsd/geoinfo/ungegn/docs/29th-gegn-docs/WP/WP22_11_29UNGEGN_REPORT_JAPAN.pdf | BOILER: root-clear https://unstats.un.org/; not a title, h1 or meta label | RELEVANCE: shared=['featu', 'japan', 'kanji', 'name'] | TOPIC: quote_hits=1 function_words=7 page_hits=41 page_terms=36 need=1/2/3/2
exit=0
```

The draft run has no `--entry`, so it does not exercise RELEVANCE legs (c) and (d). The L1 should rerun with `--entry corpus/knowledge/linguistics/toponymy-place-names.md` after landing.

## draft sentences

S530:
- When Japan's Heisei mergers (from 1999) left 268 merged municipalities needing new names, most of those names were drawn from wider areas such as a county, from natural features (rivers above all), or from revived old province names (S530).
- The paper sorts those new municipal names into six origins: names of a wider area, names from natural features, old province names, compound names, names with pleasant connotations such as Sakura or Midori, and others (S530).
- Earlier, in the Meiji mergers of 1889, many compound names were made by taking one Chinese character from each merging village. Tsudanuma joins characters from Yatsu, Kuguta and Saginuma. In the Heisei mergers, by contrast, names from wider areas, natural features and old province names prevailed (S530).
- Japanese law leaves a new municipal name largely to the municipality itself. A change is made by bylaw after consulting the prefectural governor, and a 1970 notification asks that a new city name not match an existing city's, so wider areas, natural features or old province names are local choices, not rules (S530).

S531:
- Most Japanese geographical names are written in kanji, with a final character naming the feature type. Fujisan (富士山) splits into the specific part Fuji and the generic 山 san, "mountain", and Tonegawa splits into Tone and the river kanji 川 (S531).
- GSI's English rules replace the kanji for the geographical feature at the end of the name with an English word (the substitution format: Mt. Fuji, Tone River). When a name is unified and cannot be split, they keep the whole Japanese name and add the English word (the addition format: Mt. Tateyama, Arakawa River) (S531).
- GSI counts more than 80% of Japanese mountain names ending in the standard kanji 山 or 岳, and more than 240 different kanji at the end of mountain names in its geographical names database (S531).
- Romanization alone hides the generic from outsiders. A foreign visitor who does not know that san can mean mountain may not see that Fujisan names a mountain, which is why GSI's rules render the end-of-name feature kanji as an English word (S531).

## rejected:

- **https://www.gsi.go.jp/ENGLISH/, https://www.gsi.go.jp/ENGLISH/page_e30233.html, https://www.gsi.go.jp/kihonjohochousa/gazetteer.html:** live GSI cannot be fetched by ordinary means. The server needs TLS legacy renegotiation, which OpenSSL refuses, and the frozen locator (`reopen-quote.py` `fetch`, urllib) hits the same error, so any live gsi.go.jp row fails LOCATE. I did not work around this. Output:
  - `curl -sSL -v https://www.gsi.go.jp/ENGLISH/`: `* TLS connect error: error:0A000152:SSL routines::unsafe legacy renegotiation disabled` / `curl: (35) TLS connect error: error:0A000152:SSL routines::unsafe legacy renegotiation disabled` (`curl -w '%{http_code}'` printed `000` for all three URLs).
  - `python3 urllib.request.urlopen('https://www.gsi.go.jp/ENGLISH/')`: `ERR <urlopen error [SSL: UNSAFE_LEGACY_RENEGOTIATION_DISABLED] unsafe legacy renegotiation disabled (_ssl.c:1082)>`.
  - `http://www.gsi.go.jp/ENGLISH/` returns `301` to the https host, so it fails the same way.
- **Leads not opened:** these appeared only as search-result snippets and were not offered. web1.gsi.go.jp committee PDFs 000106924.pdf and 000106945.pdf (Japanese text, so they would fail TOPIC's English stem sets; the same host is likely to have the same TLS problem [INFERENCE]); unstats GEGN.2/2023/65 and GEGN.2/2025/22 CRP.22 (Japan country reports on standardisation and on kanji in the names database); www.ksc.kwansei.ac.jp, uub.jp, sankei.com and nanyanen.jp pages on hiragana municipal names (Japanese text, student or hobby pages, or a news site; not tier A or B for TOPIC in English).

installs: none.
