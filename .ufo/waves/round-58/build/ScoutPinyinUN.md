# ScoutPinyinUN — claim C source item: romanization of Chinese place names (Pinyin, UN)

Seat: KotodamaR58A2.ScoutPinyinUN. S-ids: S532, S533. Both rows print LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS under `reports/round-58/rowcheck.py --draft` (output below). Neither URL is in `corpus/SOURCES.md` (`grep -cF -e 'RES_UN_E_updated' -e 'wg5.cshtml' corpus/SOURCES.md` → `0`), and neither appears in any sibling report under `.ufo/waves/round-58/build/` at time of writing. The sibling ScoutRomanizationSystems uses `arhiiv.eki.ee/wgrs/*` pages (including `rom1_zh.htm`), so I left those alone.

Distinctness note for the L1: both rows are on host `unstats.un.org`. They are different pages carrying different points, but they count as one host toward DISTINCT's 10-host floor.

## (1) Registry rows

| S532 | United Nations Conferences on the Standardization of Geographical Names (compiled by Natural Resources Canada for the UN), 2018, Resolutions adopted at the eleven United Nations Conferences on the Standardization of Geographical Names 1967-2017 — https://unstats.un.org/unsd/ungegn/conferences/documents/RES_UN_E_updated_1-11_CONF.pdf (direct, HTTP 200) | record | A | UN 1977 resolution III/8 adopting Pinyin as the international romanization of Chinese geographical names | Resolution III/8 (Romanization of Chinese geographical names), operative clause, PDF p. 87: "that the Chinese Phonetic Alphabet (Pinyin) be adopted as the international system for the romanization of Chinese geographical names" | The third UN naming conference recommended Pinyin, China's own phonetic alphabet, as the one international way to romanize Chinese geographical names. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S533 | United Nations Statistics Division / UNGEGN, n.d. (live 2026), Working Group on Romanization Systems — https://unstats.un.org/unsd/ungegn/working_groups/wg5.cshtml (direct, HTTP 200) | docs | A | who proposes and who agrees UN romanization systems for geographical names | Mandate paragraph, sentence 1 (clause after the semicolon): "the systems are for application to geographical names and should be proposed by a (donor) country" | A UN romanization scheme for geographical names must begin as a proposal put forward by the donor country itself. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Page context I opened, for the L1 and the SUPPORT reviewers:
- **S532**: the full III/8 text (PDF pp. 86–87) has three preamble clauses before the operative one. The first recognizes that the Scheme for a Chinese Phonetic Alphabet "is China's official Roman alphabet scheme" and that Chinese rules for transliterating place names "have been drawn up in China". The second notes the scheme "is linguistically sound" and that a Gazetteer of Chinese Geographical Names in Chinese Phonetic Spelling was published. The third considers adoption "through a suitable transitional period". The page prints the operative line as `Recommends; that the Chinese ...`; the quote starts at `that` so the stray semicolon stays out. Ten years earlier, resolution I/15 (1967, PDF pp. 82–83) only asked the future expert group to "consider the suitability" of China's system. So the decision was staged over two conferences.
- **S533**: the full mandate sentence reads "The basic mandate of the Working Group is to consider and reach agreement on a single romanization system for each non-Roman writing system; the systems are for application to geographical names and should be proposed by a (donor) country." The same paragraph adds: "New systems are referred to the United Nations Group of Experts on Geographical Names for endorsement and are then passed to ECOSOC for resolution and vote before becoming a United Nations standard." The page's status table lists Chinese, version 4.0, 2013-09-24, among the 30 UN-recommended systems.

## (2) Gate lines

- S532 — https://unstats.un.org/unsd/ungegn/conferences/documents/RES_UN_E_updated_1-11_CONF.pdf — accessed 2026-10-23 — Resolution III/8, operative clause, PDF p. 87: “that the Chinese Phonetic Alphabet (Pinyin) be adopted as the international system for the romanization of Chinese geographical names”. Grounds: The third UN naming conference recommended Pinyin, China's own phonetic alphabet, as the one international way to romanize Chinese geographical names. Seat: ScoutPinyinUN.
- S533 — https://unstats.un.org/unsd/ungegn/working_groups/wg5.cshtml — accessed 2026-10-23 — Mandate paragraph, sentence 1: “the systems are for application to geographical names and should be proposed by a (donor) country”. Grounds: A UN romanization scheme for geographical names must begin as a proposal put forward by the donor country itself. Seat: ScoutPinyinUN.

## (3) rowcheck output

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutPinyinUN/rows.md` (final run, with the final teaches cells):

```
S532 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://unstats.un.org/unsd/ungegn/conferences/documents/RES_UN_E_updated_1-11_CONF.pdf | BOILER: root-clear https://unstats.un.org/; not a title, h1 or meta label | RELEVANCE: shared=['alpha', 'chine', 'geogr', 'inter', 'name', 'phone'] | TOPIC: quote_hits=1 function_words=6 page_hits=1316 page_terms=1155 need=1/2/3/2
S533 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://unstats.un.org/unsd/ungegn/working_groups/wg5.cshtml | BOILER: root-clear https://unstats.un.org/; not a title, h1 or meta label | RELEVANCE: shared=['count', 'donor', 'geogr', 'name', 'propo'] | TOPIC: quote_hits=1 function_words=8 page_hits=18 page_terms=17 need=1/2/3/2
exit=0
```

Two earlier runs failed, and the failures matter for the L1:
- **Locator quotes.** The first draft quoted the resolution title inside the S532 locator. That gave `LOCATE: quote under 8 words`, because the checker takes the anchor's *first* double-quoted span. The fix was to drop the quotes from the locator. Keep locators free of double quotes.
- **Transient PDF fetch.** One run gave `S532 ... TOPIC FAIL | TOPIC: quote_hits=1 page-unfetchable URLError`, a transient fetch failure on the 1.2 MB PDF. It passed again on an immediate rerun (above). The acceptance run may need a retry if unstats is slow.

## (4) draft sentences

S532:
- In 1977 the third UN conference on geographical names recommended that Pinyin, the Chinese Phonetic Alphabet, be adopted as the single international system for romanizing Chinese geographical names (S532).
- The resolution's preamble grounds the choice in Pinyin being China's own official phonetic alphabet, so the international romanization of Chinese place names follows the spelling China itself uses (S532).
- For a worldbuilder, this is a design rule: the international spelling of a place name can be settled by adopting the name-owning country's own romanization system instead of an outsider's (S532).

S533:
- UNGEGN's Working Group on Romanization Systems deals with systems for application to geographical names, and each such system should be proposed by the donor country whose script it romanizes (S533).
- The proposal therefore starts with the country that owns the names. The Working Group then considers it and seeks agreement before the system can become a UN standard for those geographical names (S533).
- A worldbuilder can mirror this: an invented script gets one agreed romanization for its geographical names, and the donor country that writes in that script proposes it (S533).

## (5) rejected

- https://unstats.un.org/unsd/ungegn/pubs/documents/3rd%20UNCSGN%20Report%20Athens%201977.pdf — guessed path for the 1977 conference report; `404 text/html 1245`.
- https://unstats.un.org/UNSD/ungegn/wg4.html and https://unstats.un.org/unsd/ungegn/wg4.html — guessed paths; both `404 text/html 1245`.
- https://unstats.un.org/unsd/ungegn/wg/romanization/ — `404 1245`.
- https://unstats.un.org/unsd/ungegn/conferences/ — HTTP 200. An index of conference pages and document links with no body sentence to quote. I used it only to find the resolutions PDF.
- https://unstats.un.org/unsd/geoinfo/UNGEGN/ungegnConf3.html — HTTP 200, the 1977 conference document list. Its Pinyin items ("Proposal for a resolution on the romanization of Chinese geographical names E/CONF.69/C.IV/L.1", "Rules for spelling Chinese place names with the Chinese phonetic alphabet E/CONF.69/L.118") are list or table entries, not sentences, so they fail the row rules.
- https://www.eki.ee/wgrs/ (redirects to https://arhiiv.eki.ee/wgrs/) — HTTP 200. It is the archived WGRS site ("Since May 2023 this web site is an archive ... will not be updated"), the sibling ScoutRomanizationSystems already uses it, and the live unstats page (S533) supersedes it.
- https://arhiiv.eki.ee/wgrs/rom1_zh.pdf — HTTP 200, the WGRS status report for Chinese (v4.0, 2013). It has a good sentence: "The United Nations conference approved the Scheme for a Chinese Phonetic Alphabet (Pinyin) in 1977 (III/8) for the romanization of Chinese geographical names." I did not offer it for three reasons. It repeats S532's point. The sibling ScoutRomanizationSystems uses the same report as `rom1_zh.htm`. And by my reading of the two-page `pdftotext` text, it holds only two NAMING-PLACE windows (the title and that sentence), below PAGE_HITS 3. That count is [INFERENCE]: I did not run rowcheck on it.
- https://arhiiv.eki.ee/wgrs/rom1_zh.htm — fetched (HTTP 200) only to check whether an HTML twin existed. It is the sibling's row, so I did not read it further.
- https://unstats.un.org/unsd/ungegn/sessions/2nd_session_2021/documents/GEGN.2_2021_93_CRP93_15_WGRSreport.pdf — HTTP 200, the 2021 WGRS report. It has no Pinyin content: `grep -n -i 'pinyin\|chin'` on its `pdftotext` output matched only "machine transliteration" (line 97: `innovative methods to be used for romanization, such as machine transliteration, and that it`).
- https://unstats.un.org/unsd/ungegn/sessions/2nd_session_2021/documents/GEGN.2_2021_CRP114_15_China.pdf — HTTP 200, China's 2021 paper. It is Chinese-language only and covers Chinese-character rendering of *Japanese* place names (specific and generic elements, Ainu names). That is a different topic from Pinyin, and it has no English sentence to quote. Lead only: it shows China rendering generic elements by meaning and specific elements by character or sound.
- https://unstats.un.org/unsd/ungegn/sessions/2019-new-york-ungegn-1st-session/documents/GEGN.2_2019_11_CRP.11_WG_Romanization_Systems-full-report.pdf — HTTP 200, but only 25,351 bytes, and `grep -n -i 'pinyin\|chinese'` on its `pdftotext` output printed nothing.
- https://unstats.un.org/unsd/ungegn/working_groups/wg4.cshtml — HTTP 200 (50,907 bytes). I probed it while looking for the WGRS page and did not read it: the WGRS page is `wg5`.

installs: none. pdftotext (`/usr/bin/pdftotext`) and the checker's own `uv run --with pypdf==5.4.0` were already present. Scratch: `/fast/scratch/hyaku/kotodama-r58/ScoutPinyinUN/` (downloads plus `rows.md`); no processes left running.
