# ScoutChinaFuTalismans — claim C sources: S626, S627

Question (seat): open 2–4 sources on Chinese talismans (*fu* 符) and door protection (Daoist
talisman writing, door gods, peach wood, mirrors against evil) and offer at most two claim-C rows,
S626 and S627, aimed at design decisions a worldbuilder makes: what the object is made of, what
danger it answers, who makes or blesses it, where it is worn or placed, and what words or signs it
carries.

Axes named: **coverage** (the claim's declared axis; Chinese *fu* and door placement had no
filename owner), **verifiability** (FETCH-59: a live page that answers a plain GET, quote in body
text, site root clear of it), **usability** (each quote must carry a construction choice — a
danger model, a fixing, a material — not a definition). Kept moves: one Tang *demonic-infestation*
row (the talisman inside a diagnostic-and-expulsion kit) and one Han *wooden door talisman* row
(the sharp base that fits the object to the door). No move that harmed an axis was kept.

Method: every page below was opened in this session by an ordinary GET (`urllib`/`curl`, desktop
UA, redirects, no cookies, no challenge solving). No headless browser; no CAPTCHA, paywall,
login or bot challenge was ever met. No installs or updates were made. Working directory for
every command: `/fast/scratch/hyaku/kotodama-r59/ScoutChinaFuTalismans/`; artifacts `rows.md`,
`stub.md`, `probe.py`, `spans.py`, `m_cf4e2a.txt` (Morrison OCR), `out.txt`.

Both rows were checked with the round-59 instrument before being offered:

```
cd /fast/scratch/hyaku/kotodama-r59/ScoutChinaFuTalismans && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutChinaFuTalismans/rows.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutChinaFuTalismans/stub.md
S626 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://dao.crs.cuhk.edu.hk/Main/wp-content/uploads/2025/02/DAO1516_04.pdf | BOILER: root-clear https://dao.crs.cuhk.edu.hk/; not a title, h1 or meta label | RELEVANCE: shared=['ailme', 'demon', 'exorc', 'talis'] | TOPIC: quote_hits=2 function_words=5 page_hits=60 page_terms=31 need=1/2/3/2
S627 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://museum.sinica.edu.tw/en/collection/20/item/36/ | BOILER: root-clear https://museum.sinica.edu.tw/; not a title, h1 or meta label | RELEVANCE: shared=['door', 'sharp', 'talis'] | TOPIC: quote_hits=1 function_words=4 page_hits=8 page_terms=7 need=1/2/3/2
EXIT=0
```

The same two lines, extracted from *this* file (`grep -E '^\| S62[67] \|' … > report-rows.md`) and
run again against `stub.md`, returned the identical four-leg PASS output with `EXIT=0`, so the rows
are paste-ready exactly as written below.

---

## S626 — Tang *fu* inside an exorcistic kit: what danger it answers, who it works beside

**Registry row (11 cells, paste-ready):**

| S626 | Wei Wu, "Terrifying Demons: A Tang-Dynasty Treatment for Demonic Infestation", *Daoism: Religion, History and Society* 15 & 16 (2023/24), 119-160, Chinese University of Hong Kong Press — https://dao.crs.cuhk.edu.hk/Main/wp-content/uploads/2025/02/DAO1516_04.pdf (direct, HTTP 200, 2439068 bytes) | paper | A | the Tang iatromantic treatment the article reconstructs: divination that names the demon behind an ailment and the ritual means, talismans among them, used to expel it | printed p. 127, iatromancy paragraph (busui 卜祟): "This method aimed to identify the demons that caused the ailments and expel them through sacrifices, incantations, talismans, and other exorcistic rituals." | In the Tang treatment the article reconstructs, talismans were one instrument in an exorcistic kit that named the demon behind an ailment and drove it out. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

**Gate line:**

- S626 — https://dao.crs.cuhk.edu.hk/Main/wp-content/uploads/2025/02/DAO1516_04.pdf — accessed 2026-10-23 — printed p. 127, iatromancy paragraph (busui 卜祟): "This method aimed to identify the demons that caused the ailments and expel them through sacrifices, incantations, talismans, and other exorcistic rituals." Grounds: In the Tang treatment the article reconstructs, talismans were one instrument in an exorcistic kit that named the demon behind an ailment and drove it out. Seat: ScoutChinaFuTalismans.

**Rowcheck output:** pasted above; all four legs PASS (`quote_hits=2 page_hits=60 page_terms=31`).

**What the opened page carries (for the entry, not only the quote):**

- Article identity as printed on p. 119: 《道教研究學報：宗教、歷史與社會》第十五、十六期 (2023/24), *Daoism:
  Religion, History and Society*, Nos. 15 & 16, pp. 119–160; running feet carry "Copyrighted
  Material of The Chinese University of Hong Kong Press".
- The abstract opens on epidemics as "a constant threat to the well-being of people in medieval
  China" and on ritual therapy as one response, traced back to the "magical recipes" among the
  Mawangdui medical manuscripts; in the Sui (581–618) and Tang (618–907) dynasties, the Imperial
  Medical Office (Taiyi shu 太醫署) "established an official role with the title 'Erudite of
  Exorcism' (zhoujin boshi 咒禁博士)", a master teacher of incantations of interdiction.
- The quoted passage sits in the article's account of iatromancy (busui 卜祟), "a method of
  divination and related techniques used to diagnose and treat illnesses"; the sentence's own
  teaching is that diagnosis (which demon) precedes expulsion (sacrifice, incantation, talisman).
- Materials and substrate, and the makers' craft, appear elsewhere on the same page and are
  **not** in my quote: a talisman written "on a cake (gao 糕) instead of on paper, the usual
  carrier of talismans in medieval China", with the article's note on the 糕/高 homophone (note 52,
  reporting Ch'en Hsiang-ch'un); "talismanic medicines" swallowed so that "the malaria demons
  should conceal their traces"; and a Tang poem (Han Yu 韓愈, 768–824, *I Reprimand the Malaria
  Demon*, 譴瘧鬼) whose line reads "The Master of Talismans plays with his knife and brush;
  cinnabar and ink splatter this way and that" — the *fu* master as a distinct ritual specialist
  alongside the physician, the moxa master and the curser.
- The article also studies a named talisman text, *The True Talisman of the White Numen*, its three
  *juan* and disputed authorship — a lead on "how words and scripts become protective", not used
  in this row.

**Draft sentences (2, each ending with the id):**

- Where an ailment was read as a demon's work, the talisman entered a ritual that named the demon
  and drove it out with sacrifice and incantation (S626).
- The talisman is one instrument among several in that treatment, working beside sacrifice and
  exorcistic ritual rather than alone (S626).

---

## S627 — Han wooden talisman: the shape that fits it to the door

**Registry row (11 cells, paste-ready):**

| S627 | Museum of the Institute of History and Philology, Academia Sinica, "Wooden Talismans" (Han dynasty, 206 B.C.–A.D. 220; item nos. 377.3/155.10/163.1/66.3, Edsen-gol), collection record — https://museum.sinica.edu.tw/en/collection/20/item/36/ (direct, HTTP 200, 55323 bytes); capture https://web.archive.org/web/20260209080847id_/https://museum.sinica.edu.tw/en/collection/20/item/36/ | docs | A | the museum's own record of these Han wooden talismans: the purpose it states against evil spirits and the sharp base that fits them to a door | Collection → Wooden Talismans, description sentence 2: "The bottom of the talisman is sharp so it can be fitted onto the door." | A sharp base is what fits the talisman onto the door, so the object's shape answers its doorway placement. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

**Gate line:**

- S627 — https://museum.sinica.edu.tw/en/collection/20/item/36/ — accessed 2026-10-23 — Collection → Wooden Talismans, description sentence 2: "The bottom of the talisman is sharp so it can be fitted onto the door." Grounds: A sharp base is what fits the talisman onto the door, so the object's shape answers its doorway placement. Seat: ScoutChinaFuTalismans.

**Rowcheck output:** pasted above; all four legs PASS (`page_hits=8 page_terms=7`).

**What the opened page carries (for the entry, not only the quote):**

- The record sits under "Collection → Han Dynasty Wooden Slips from Edsen-gol"; item no.
  377.3/155.10/163.1/66.3; period "Han dynasty (206 B.C.-A.D.220)"; materials "Wood"; dimensions
  for 66.3 "Length 21.5, width 3.6, thickness 1.76 cm" (155.10: 16.5 × 2.2 × 1.76 cm; 163.1:
  length 17.1 cm).
- Findspots: "A35 Taralingin-durbeljin (66.3), A21/A22 Bukhen-torei (155.10/163.1), P9 Borotsonch
  (377.3), Edsen-gol, Inner Mong[olia]" — archaeological objects, not souvenir-shop pieces.
- The first description sentence, which I did not quote, states the danger class and the object's
  look: "The Han used these ferocious looking talismans to avoid evil spirits and hexes."
- The same collection lists a sibling type, "Wooden Gangmao : Amulets", which is a lead on the
  named Han apotropaic pendant (剛卯) but was not opened as a separate page.
- The quoted sentence is the second sentence of the description paragraph under the object's
  heading, not a caption, table cell or metadata field (BOILER: not title, h1 or meta; not on the
  site root).

**Draft sentences (2, each ending with the id):**

- A door talisman's form is a fixing decision: its base is sharp so the talisman can be fitted onto
  the door itself (S627).
- Because the base is sharp, the talisman can be fitted onto the door, which makes the object's
  shape part of its placement (S627).

---

## Checked and not offered (opened, or attempted and refused)

1. **Christine Mollier, "Talismans" (HAL deposit hal-03094639)** — refused by a bot challenge, not
   opened. `curl` reported `200 text/html; charset=utf-8 12566`; the body begins
   `<title>Making sure you&#39;re not a bot!</title>` (Anubis challenge). The instrument saw
   `HTTP 200 12566 bytes text/html; charset=utf-8 textlen=1522 DISCIPLINE=0 [] windows=0`. A
   challenge that must be met is exactly what QUALITY criterion 10 forbids, so this otherwise ideal
   overview of *fu* (paper, wood, metal, pottery supports) is left as a lead only; FETCH-59 would
   also fail it as an error.
2. **Wellcome Collection, "Medical talisman for gestation and puerperium (Chinese MS)"** — attempt
   refused: `FAIL HTTPError: HTTP Error 405: Not Allowed`
   (https://wellcomecollection.org/works/eptge8s5). A 405 is a FETCH-59 error class.
3. **The Met, Heilbrunn essay "Daoism and Daoist Art"** — refused: `429 34228`
   (https://www.metmuseum.org/toah/hd/daoi/hd_daoi.htm). Site-wide refusal for this host; the Met's
   "Paper Talisman with Paired Military Door Gods" (search 63908) was therefore never opened either,
   so it is not cited.
4. **The British Museum, collection object page** — refused: `403 5521`
   (https://www.britishmuseum.org/collection/object/A_1880-0709-0-1).
5. **Smithsonian National Museum of Asian Art** — refused: `403 46349`
   (https://asia.si.edu/learn/); `https://www.si.edu/` also `403 46394`.
6. **Brooklyn Museum** — refused: `429 34229` (https://www.brooklynmuseum.org/).
7. **Nelson-Atkins, "Door God" (object 7222)** — opened attempt timed out:
   `FAIL URLError: <urlopen error timed out>`
   (https://art.nelson-atkins.org/objects/7222/door-god).
8. **Harvard Art Museums, "Door God: General Qin Qiong" (object 206261)** — opened, not offered:
   `HTTP 200 122434 bytes text/html; charset=utf-8 textlen=6072 DISCIPLINE=0 [] windows=0`. A
   door-god record with no charm/talisman vocabulary anywhere on the page cannot pass TOPIC
   (`page_terms=0`).
9. **Royal Asiatic Society, "Chinese door gods"** — opened, not offered:
   `HTTP 200 61514 bytes text/html; charset=UTF-8 textlen=4389 DISCIPLINE=0 [] windows=0`.
   Same failure: curatorial text about prints, no `talism*`/`charm*`/`amulet*` term.
10. **Asian Art Museum, "Door gods Yuchi Gong and Qin Qiong" (object 14426)** — opened attempt
    returned a shell, not a record: `HTTP 202 0 bytes text/html; charset=UTF-8 textlen=0
    DISCIPLINE=0 [] windows=0` (https://searchcollection.asianart.org/objects/14426/door-gods-yuchi-gong-and-qin-qiong).
    The eMuseum host shields its records; `https://asianart.org/` answered `403 5477`.
11. **UBC open library, "God of the Gate, Protector of the Door: Door Gods (Menshen)"** — refused by
    a bot challenge: the media URL answered `200 text/html 21987 bytes` and the item page
    (`https://open.library.ubc.ca/collections/ubctheses/831/items/1.0088908`, `200 21915 bytes`)
    serves a TSPD challenge script (`window["bobcmn"] = "1011101010101020…"`). Not opened, not
    cited, though it is the best door-god thesis lead for a later round.
12. **china.org.cn, "Opening the Door to Ancient Tradition"** — opened, not offered:
    `HTTP 200 21725 bytes text/html; charset=UTF-8 textlen=10991 DISCIPLINE=0 [] windows=0`
    (http://www.china.org.cn/english/LI-e/26590.htm). It carries the Shen Tu / Yu Lei peach-wood
    story but no discipline term and no CHARM-GUARD window, so it cannot be a TOPIC row.
13. **"The Changing Functions of the Door Gods in China" (chr.ewaoa.com PDF)** — opened, not
    offered: `HTTP 200 500304 bytes application/pdf textlen=20308 DISCIPLINE=3 ['charms']
    windows=0`. A page with zero CHARM-GUARD windows fails `page_hits >= 3` outright.
14. **Columbia University, Asia for Educators, "The Lunar New Year: Rituals and Legends"** —
    opened, not offered: `HTTP 200 38195 bytes text/html; charset=UTF-8 textlen=28931
    DISCIPLINE=0 [] windows=0`. It states that door-god prints were affixed "to guard against evil
    spirits or ghosts", but the page never uses a charm/talisman term, so `page_terms=0`. Two
    sibling pages were checked too: `cosmos/prb/earthly.htm` `DISCIPLINE=0 [] windows=1` and
    `cosmos/prb/whatis.htm` `DISCIPLINE=0 [] windows=0`.
15. **MDPI *Arts* 15(3):59, "Divine Talisman Writing"** — refused: `403 399`
    (https://www.mdpi.com/2076-0752/15/3/59).
16. **Shih-shan Susan Huang, "Daoist Seals Part 1"** — refused: `403 2321`
    (https://shihshansusanhuang.com/wp-content/uploads/2020/07/bb863-2017a_huang_daoist-seals-part-1-activation-and-fashioning.pdf).
17. **Penn Museum, "Talisman 29-96-728C" (Guangzhou)** — refused: `FAIL HTTPError: HTTP Error 403:
    Forbidden` (https://www.penn.museum/collections/object/129488).
18. **Science Museum Group, "Amuletic Board, China, 1801-1900" (A18987)** — opened, not offered:
    `HTTP 200 33949 bytes text/html; charset=utf-8 textlen=9205 DISCIPLINE=2 ['amulet','amuletic']
    windows=7`. The two body sentences that carry the door point have no CHARM word at all —
    `window_hits=0` for both "Wooden plaque, called a joss-board, carved in low relief, hung on the
    door to prevent the entry of devils, China, 1800s" (21 words) and "This board is known as a
    joss-board and is hung on doors to prevent the entry of devils and evils spirits." (21 words) —
    and the page's only charm terms sit in the title and metadata. A second fetch of the same object
    page then returned `HTTP Error 429: Too Many Requests`, and the collection search returned
    `HTTP Error 429: Too Many Requests` for `?q=talisman+china`, `?q=charm+china` and
    `?q=door+god+china`: the host is also a FETCH-59 risk.
19. **John Robert Morrison 1832, "Some Account of Charms, Talismans, and Felicitous Appendages worn
    about the person, or hung up in houses, &c. used by the Chinese", *Transactions of the Royal
    Asiatic Society* vol. 3** — opened in full text (`https://archive.org/download/transactionsofro03asia/transactionsofro03asia_djvu.txt`,
    `200 text/plain; charset=utf-8 1710569` bytes, read from the scratch copy `m_cf4e2a.txt`). Not
    offered, and this one hurts: it is a primary 1832 source and it carries exactly my subtopic —
    "Taou foo, the “ Peach charm,” consists of a sprig of peach blossoms, which, on the first day of
    the first moon, is placed in some districts at the head of the door of every house, to drive away
    demons and malignant spirits." (43 words), and "Koo-tung king, “ The old brass mirror,” is a
    charm which is supposed to possess the virtue of immediately healing any who have become mad by
    the sight of a spirit or demon…" (44 words). Both exceed the 25-word quote cap, and both return
    `window_hits=0` under the instrument (the charm word and the guard word are more than three
    words apart), so neither can be a TOPIC quote even trimmed. The only 10–25-word sentence on the
    page that does carry a window is a numbered list item — "A kind of talisman, worn generally
    about the person, but sometimes also hung up on the walls of houses." (19 words) — which the row
    rules exclude ("never a … list item"). Held as the best next lead for a round whose quote budget
    can reach a longer clause; I would not defend a trimmed peach quote to a blind reviewer.
20. **Stephen Jones, "Yinyang: Household Daoists of North China and Their Rituals" (DAO 3)** —
    opened, not offered only because of the two-row cap: `HTTP 200 1499302 bytes application/pdf
    textlen=131925 DISCIPLINE=5 ['talisman','talismans'] windows=7`
    (https://dao.crs.cuhk.edu.hk/Main/wp-content/uploads/2018/08/DAO3_03_JonesYY.pdf). Its one
    window sentence — "Daoists also depict fu 符 talismans and write the ritual documents required,
    including the tomb tile." — is about who makes the *fu*, a strong next row for "who makes or
    blesses it".
21. **web.archive.org (the S627 capture)** — the Wayback availability API reports the snapshot
    `status: 200, available: true` for timestamp 20260209080847, but this host could not read it:
    `FAIL HTTPError: HTTP Error 429: Too Many Requests` on two attempts 45 s apart. The capture is
    listed as a FETCH-59 fallback only because the live page is first and passes; it is the same
    page, not a second source.

---

## Confidence, cautions and remaining unknowns

- **Confidence: high mechanically** (instrument PASS, run above, `EXIT=0`) and **high on content
  for S626** (the quote was read in its paragraph at printed p. 127, and its neighbours were read
  too). **Medium-high for S627**: the quote is a complete description sentence in a museum record,
  but the record is short — its evidential weight is the museum's own statement about its own
  objects, which is what the tier-A scope says.
- **S626 is a PDF.** The quote was located through the instrument's own `pypdf 5.4.0` extraction
  path, which is what acceptance runs; the chosen sentence extracted cleanly (no hyphen or ligature
  damage, no interleaved footnote marker). Verified swap-ins if the L1 prefers a different emphasis,
  each `locate True` and inside the same page: "The talisman should be written on a cake (gao 糕)
  instead of on paper, the usual carrier of talismans in medieval China." (22 words, 2 windows, 6
  function words — but it sits in note 52, so it is not body text) and "Once the talismanic
  medicines enter the five viscera, the malaria demons should conceal their traces." (15 words, 1
  window, exactly 2 function words — the floor, so do not shorten it).
- **S627 swap-in:** "The Han used these ferocious looking talismans to avoid evil spirits and hexes."
  (13 words, 1 window, 3 function words, `locate True`) states the danger class instead of the
  fixing. If the entry wants both "what it is" and "where it goes", the second sentence (mine) is the
  one that cannot be recovered from the first, which is why I kept it.
- **Tier note for S626:** A for the article's own argument, not for the Tang sources it reports;
  the cake note is explicitly attributed to Ch'en Hsiang-ch'un's study, and the poem line to Han Yu,
  so anything built on those must say "as the article reports". Peer review is not asserted on the
  page; what is observed is a university-press journal article with a volume, year and page range.
- **Tier note for S627:** A scoped to "the museum's own record". "The Han used these ferocious
  looking talismans to avoid evil spirits and hexes" is the museum's curatorial generalization, not
  an excavation report; the entry should attribute it to the museum's catalogue, not to Han
  testimony.
- **Host freshness:** `dao.crs.cuhk.edu.hk` and `museum.sinica.edu.tw` appear **0** times in
  `corpus/SOURCES.md` (`grep -c` returned 0 for each), so both rows land on fresh hosts for DISTINCT.
- **Coverage limits of this seat (state them in the entry's handoff, do not paper over them):** the
  two rows give the entry (a) the *danger model* behind a *fu* — a named demon causing an ailment,
  expelled by a ritual kit in which the talisman is one instrument — and (b) *placement and form* —
  a wooden talisman cut with a sharp base to be fitted onto a door. They do **not** cover: peach wood
  as a material choice, door gods (*menshen*) and their prints, bagua mirrors, the script/inscription
  itself (which characters and why), the priest or ritual master as maker and seller, or
  commodification. Leads on record, unopened or unusable here: Morrison 1832 (peach charm, brass
  mirror — quote-length blocked), Jones (household Daoists who write *fu*), the Academia Sinica
  sibling record "Wooden Gangmao: Amulets", and the Met's "Paper Talisman with Paired Military Door
  Gods" (refused 429).
- **Unknowns:** (a) whether these Edsen-gol pieces are *gangmao* 剛卯, *taofu* 桃符 or another type —
  the record's own heading says only "Wooden Talismans" and the text I read does not name the
  inscribed characters, so the entry must not name a type; (b) the capture was never read (429), so
  its content is unverified beyond the availability API; (c) whether a blind reviewer will treat a
  one-paragraph museum description as sufficient body text — I judge yes, because the sentence is a
  full declarative about the object's fixing, not a label.
