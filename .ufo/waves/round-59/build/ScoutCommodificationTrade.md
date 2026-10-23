# ScoutCommodificationTrade — claim C source seat (change and commodification)

Round 59 (hyaku phase 4), BUILD wave, 2026-10-23. Seat: `KotodamaR59.ScoutCommodificationTrade` (leaf; no
delegation, no background jobs). Assigned S-ids: **S646, S647**. Subtopic: change and commodification —
nazar bead glassmaking, amulet markets and souvenir trade, campaigns against amulets.

Both rows are open-access journal PDFs opened by ordinary plain GET in this session (HTTP 200, no
challenge). No Wayback capture of either page exists (`archive.org/wayback/available` returned
`"archived_snapshots": {}` for both), so neither row lists one; FETCH-59 live fetch is the only URL and
it located the quote in two independent rowcheck runs.

No tools installed. Extraction used `uv run --no-project --with pypdf==5.4.0` (ephemeral env; the same
pypdf 5.4.0 path `reports/round-59/reopen-quote.py` uses for PDFs), so the quote I checked is the text
the instrument sees. No pacman, no host service touched. Scratch: `/fast/scratch/hyaku/kotodama-r59/ScoutCommodificationTrade/`.

## 1. Registry rows (11 cells, exactly as offered)

```
| S646 | Vũ Hồng Thuật, 2008, "Amulets and the Marketplace", Asian Ethnology 67(2): 237–255, Nanzan Institute for Religion and Culture — https://asianethnology.scholasticahq.com/article/149559.pdf (direct, HTTP 200, application/pdf, 287,476 bytes, 19 PDF pages; plain GET, no challenge) | paper | B | the Vietnamese paper-amulet market as observed at Hanoi ritual masters' workshops: stencilled mass production, ritual empowerment, and the prices masters charge clients; not the whole of Vietnamese popular religion | p. 251, section The changing world of amulet makers: "The ritual masters empower mass-produced amulets in their own temples and sell them to clients for from twenty thousand to fifty thousand Vnd." | Ritual specialists bless mass-produced amulets at their own altars and sell each one to a client for a set price. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S647 | Bilgen Tuncer Manzakoğlu and Saliha Türkmenoğlu Berkan, 2016, "Evil Eye Belief in Turkish Culture: Myth of Evil Eye Bead", The Turkish Online Journal of Design, Art and Communication 6(2): 193–204, DOI 10.7456/10602100/013 — https://openaccess.iku.edu.tr/bitstreams/8b0b8456-e29b-4568-b622-5859e4029189/download (direct, HTTP 200, application/pdf, 12,295,670 bytes, 12 PDF pages; plain GET, no challenge) | paper | B | the nazar bead in Turkey as a commodity and souvenir: survey evidence that it is bought as a gift and used as ornament, with the myth's naturalisation said to underlie that pervasive souvenir use; not a craft or workshop history | p. 202, Conclusions: "As the result of naturalization of myth, evil eye bead has a pervasive usage as souvenir in Turkey." | The evil eye bead has become a pervasive souvenir in Turkey as the myth was naturalised. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
```

## 2. Gate lines

- S646 — https://asianethnology.scholasticahq.com/article/149559.pdf — accessed 2026-10-23 — p. 251, section The changing world of amulet makers: “The ritual masters empower mass-produced amulets in their own temples and sell them to clients for from twenty thousand to fifty thousand Vnd.” Grounds: Ritual specialists bless mass-produced amulets at their own altars and sell each one to a client for a set price. Seat: ScoutCommodificationTrade.
- S647 — https://openaccess.iku.edu.tr/bitstreams/8b0b8456-e29b-4568-b622-5859e4029189/download — accessed 2026-10-23 — p. 202, Conclusions: “As the result of naturalization of myth, evil eye bead has a pervasive usage as souvenir in Turkey.” Grounds: The evil eye bead has become a pervasive souvenir in Turkey as the myth was naturalised. Seat: ScoutCommodificationTrade.

## 3. rowcheck output (final run, verbatim)

Command:
`cd /fast/scratch/hyaku/kotodama-r59/ScoutCommodificationTrade && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutCommodificationTrade/rows.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutCommodificationTrade/stub.md`

```
S646 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://asianethnology.scholasticahq.com/article/149559.pdf | BOILER: root-clear https://asianethnology.scholasticahq.com/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'clien', 'mass', 'produ', 'ritua', 'sell'] | TOPIC: quote_hits=1 function_words=7 page_hits=240 page_terms=220 need=1/2/3/2
S647 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://openaccess.iku.edu.tr/bitstreams/8b0b8456-e29b-4568-b622-5859e4029189/download | BOILER: root-clear https://openaccess.iku.edu.tr/; not a title, h1 or meta label | RELEVANCE: shared=['bead', 'evil', 'myth', 'natur', 'perva', 'souve'] | TOPIC: quote_hits=1 function_words=5 page_hits=89 page_terms=189 need=1/2/3/2
EXIT=0
```

(An earlier run with `6(2): 193–203` in S647's source cell printed the same four PASS legs for both rows
and `EXIT=0`; only the printed page range was corrected to 193–204, checked against the page headers
`Communication 193 … Communication 204`.)

## 4. Draft sentences

S646 (Vietnam; two sentences, both carried by the quote — masters empower and sell, with the price range):

- In Vietnam, ritual masters empower mass-produced paper amulets in their own temples and then sell them to clients at twenty to fifty thousand Vnd each (S646).
- The sale runs through the master himself: he empowers the mass-produced amulets at his own altar and passes them to a client at a set price (S646).

S647 (Turkey; two sentences, both carried by the quote — souvenir use is pervasive and explained by the
myth's naturalisation):

- In Turkey the evil eye bead's use as a souvenir is pervasive, a sign that the myth of the bead has become naturalised (S647).
- Naturalisation of the myth is what lets the evil eye bead pass into everyday souvenir use in Turkey (S647).

Design points these rows serve for a worldbuilder: who blesses and who sells a protective object, and at
what price (S646); what happens to the same object when belief thins into a naturalised cultural symbol
that travels as a gift and souvenir (S647). Materials/placement/writing are not what these two rows
support and should be cited to other seats' rows.

## 5. Rejected (every source opened and not offered, with the tool's output)

- **British Museum collection record, `amulet; pilgrim souvenir` W_2012-6006-15** — https://www.britishmuseum.org/collection/object/W_2012-6006-15 — the exact fit for "souvenir trade", but the site refused a plain GET. Verbatim: `403 5560` (curl status/size), then `page_hits=0 page_terms=0 chars=58`. FETCH-59 would skip it every run, so it cannot carry a row.
- **Yılmaz Irmak 2022, “Cam Sanatından Bir Folklorik Objeye: Nazar Boncuğu / From Art Glass to Folkloric Object: Evil Eye Talisman”, Kahramanmaraş Sütçü İmam Üniversitesi Sosyal Bilimler Dergisi 19(3): 1377–1384** — https://dergipark.org.tr/tr/download/article-file/2816218 — opened, 960,630 bytes, PDF; the body is Turkish (only the title and a Turkish abstract), so any quote would be Turkish and would not carry an English entry sentence for the blind reviewers. Verbatim page check: `hits 15 terms 123`; the opening text is `Cam Sanatından Bir Folklorik Objeye: Nazar Boncuğu` with `Öz:` following. Its §"Kültür Turizmi" is the exact glassmaking/tourism material, but not quotable in English here — a lead for a Turkish-reading seat, not a row.
- **Elżbieta Wiącek, “Old Symbol in Contemporary Culture. Turkish Evil Eye Bead — from Ancient Amulets to Commercial Gifts”, Jagiellonian University repository copy** — https://ruj.uj.edu.pl/server/api/core/bitstreams/74c71f44-df04-4be5-9036-dc0e4b788f9c/content — opened, HTTP 200, 790,018 bytes, 10 pages, English, and on-subtopic (souvenir, Coca-Cola glocalisation). Rejected because its commerce sentences carry no CHARM-GUARD window: the best one, `it is one of the most popular souvenirs offered to tourists from abroad, as well as a traditional gift given to visitors coming to Turkey.`, measures `window_hits = 0 words = 25`, and a scan of the whole file for 10–25-word window-bearing sentences printed only the header line `===== wiacek.txt` with no sentence. TOPIC would fail at `quote_hits=0`.
- **London Museum blog, “Medieval pilgrim shell tokens & St James' Way”** — https://www.londonmuseum.org.uk/blog/medieval-pilgrim-shell-tokens-and-st-james-way/ — opened, HTTP 200, 173,148 bytes. It holds one excellent window sentence, `More than just a souvenir, the badges became a physical focus for the devotion of medieval pilgrims, and could act like a protective religious amulet.`, but the page carries too few of the field's terms for TOPIC. Verbatim: `page_hits=3 page_terms=1 chars=51583`.
- **London Museum collection record, Ampulla (object-37220)** — https://www.londonmuseum.org.uk/collections/v/object-37220/ampulla/ — opened, HTTP 200, 169,596 bytes; the served text did not carry the record's descriptive prose in a form that meets TOPIC. Verbatim: `page_hits=0 page_terms=0 chars=47597`.
- **British Art Studies 6, “Pilgrim Souvenir: Ampulla of Thomas Becket”** — https://britishartstudies.ac.uk/issues/06/ampulla-souvenir/ — opened, HTTP 200, 100,923 bytes; the page serves article chrome and the body text carries no amulet vocabulary. Verbatim counts on the served text: `amulet 0`, `talism 0`, `apotrop 0`, `evil eye 0`, `charm 0`; scan `page_hits=0 page_terms=0 chars=34744`.
- **Ventura, Popper-Giveon and Abu Rabia, “Materialized Beliefs: ‘Industrialized’ Islamic Amulets”, Visual Ethnography 3(2)** — https://vejournal.org/index.php/vejournal/article/download/58/67 — opened, `200 99698 text/html; charset=UTF-8`; the URL resolves to the journal home page, not the article: `<title>Visual Ethnography &#8211; Journal of Anthropology</title>`.
- **Annie Thwaite, “A history of amulets in ten objects”, Science Museum Group Journal 11 (2019), DOI 10.15180/191103** — https://journal.sciencemuseum.ac.uk/article/history-of-amulets/ — opened, HTTP 200, 502,294 bytes, dense enough for TOPIC (`page_hits=311 page_terms=242 chars=295114`), but off this seat's subtopic and with no commerce sentence at all: `grep -c -i "souvenir\|sold\|sell"` on its text printed `0`. Its subject is the healing/classification history of amulets, not their sale or reform.
- **John T. Giordano, “Sacred Commodities”, Prajñā Vihāra (Assumption University)** — https://auojs.au.edu/index.php/PrajnaVihara/article/download/1278/1137 — the fetch never completed: the job ran to its 300 s cap and was killed, its output stopping at the header line `== prajna https://auojs.au.edu/index.php/PrajnaVihara/article/download/1278/1137` with no status and no file. A URL whose fetch hangs is skipped by FETCH-59, so it was dropped rather than retried for a row.

## 6. Findings, confidence, unknowns

Observed (opened in this session):

- S646 grounds: ritual masters buy stencilled amulets at the New Year in bundles of two to three hundred
  for 2,000–2,500 Vnd, empower them in their own temples, and sell them to clients for 20,000–50,000 Vnd
  (p. 251). The article also records the state campaign ("during the anti-superstition campaigns in 1957
  and 1958, anyone who performed a ritual was criticized", p. 244) and the 1986 revival.
- S647 grounds: the paper's survey reports the bead bought as a gift (`%34`), ornament placement
  ("jewelers for personal use as ornament"), manufacturer expansion of the market, and the Conclusions
  sentence used as the quote. It is a design/semiotics survey, not an ethnography of glassmaking.

Inference: [INFERENCE] S647's quote is the paper's own summary of its survey; the "pervasive ... souvenir"
claim rests on that survey (n≈20 participants plus a wider questionnaire), so the entry should not
generalise it beyond Turkey. S646's price figures are one fieldwork site (Hanoi and Bắc Ninh) around
2000–2004, not a national market.

Unresolved gaps the L1 must respect:

1. **The campaign point is not quotable from either row.** The Vietnamese anti-superstition sentence has
   no CHARM-GUARD window and is not the row quote; do not cite S646 for "state campaigns against
   amulets" in an entry sentence, because the blind reviewer judges the row's quote, not the page.
2. **No nazar glassmaking quote landed.** The Turkish glassmaking material I could open in English
   (Wiącek) lacks a window-bearing commerce sentence; the Turkish dergipark article has it but in
   Turkish. A glassmaking row needs another seat or a Turkish-reading check.
3. **Tier B judgment call:** S647's venue (TOJDAC) is a peer-reviewed open-access design journal of
   modest standing; the row is used for a survey finding, not for domain authority.
4. S646/S647 give no material, colour, inscription or placement system — those belong to other seats'
   rows; keep the entry's material/placement sentences off these two ids.
