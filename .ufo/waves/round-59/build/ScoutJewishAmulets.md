# ScoutJewishAmulets — round 59, claim C source seat

Seat: `KotodamaR59.ScoutJewishAmulets`. Claim C (coverage), subtopic **Jewish protective objects and texts** (mezuzah; childbirth amulets; written amulets). Assigned ids: S610, S611 only. Opened 2026-10-23 by ordinary GETs. Scratch: `/fast/scratch/hyaku/kotodama-r59/KotodamaR59.ScoutJewishAmulets/`. Tool installs: none.

Both offered rows locate on their live URL; each also lists one Wayback capture of the same page as a second URL (captures independently verified to contain the quote and to carry the same CHARM-GUARD density). No row depends on the capture.

## Rows (11 cells each)

| S610 | Greenberg, Blu. n.d. (page metadata: last modified 2026-06-29). "Why Jews Hang a Mezuzah on the Doorpost". My Jewish Learning (educational publisher). — https://www.myjewishlearning.com/article/mezuzah/ (direct, HTTP 200, 75,656 bytes, text/html); capture https://web.archive.org/web/20260724023450id_/https://www.myjewishlearning.com/article/mezuzah/ | docs | B | how one Jewish teaching text frames the mezuzah: doorpost placement, the hand-lettered klaf and its case, the Shaddai lettering, covenant sign versus amulet status, and the explicit denial that it protects. (tier note: B — an editorially published educational article by a named author, not a holding institution's object record.) | section Is the Mezuzah an Amulet?: "the mezuzah sometimes has been accorded the status of amulet, a magical charm." | Popular custom has sometimes classed the mezuzah as an amulet, a magical charm. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S611 | Posen Library of Jewish Culture and Civilization, vol. 5 (entry for an object in the William Gross Collection; artist unknown; ca. 1725). "Amulet for Woman in Childbirth (Germany)". Posen Library (scholarly anthology series). — https://www.posenlibrary.com/entry/amulet-woman-childbirth-germany (direct, HTTP 200, 15,932 bytes, text/html); capture https://web.archive.org/web/20260710083718id_/https://www.posenlibrary.com/entry/amulet-woman-childbirth-germany | docs | B | one printed German birth amulet (ca. 1725): its parchment support, woodcut Hebrew months, zodiac-framed central panel and inscription banishing Lilith, as the anthology describes the object. (tier note: B — a scholarly anthology's commentary on a photographed collection object; secondary text, though published in a reference series.) | object description, first paragraph: "The main panel, framed by images of the zodiac, features an inscription banishing the demon Lilith, who, according to folklore, was Adam’s first wife." | A protection amulet sets its banishing inscription inside a frame of zodiac images, naming Lilith as the demon to expel. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

## Gate

- S610 — https://www.myjewishlearning.com/article/mezuzah/ — accessed 2026-10-23 — section Is the Mezuzah an Amulet?: “the mezuzah sometimes has been accorded the status of amulet, a magical charm.” Grounds: Popular custom has sometimes classed the mezuzah as an amulet, a magical charm. Seat: KotodamaR59.ScoutJewishAmulets.
- S611 — https://www.posenlibrary.com/entry/amulet-woman-childbirth-germany — accessed 2026-10-23 — object description, first paragraph: “The main panel, framed by images of the zodiac, features an inscription banishing the demon Lilith, who, according to folklore, was Adam’s first wife.” Grounds: A protection amulet sets its banishing inscription inside a frame of zodiac images, naming Lilith as the demon to expel. Seat: KotodamaR59.ScoutJewishAmulets.

## rowcheck output (verbatim)

```
S610 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.myjewishlearning.com/article/mezuzah/ | BOILER: root-clear https://www.myjewishlearning.com/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'charm', 'magic', 'mezuz', 'somet'] | TOPIC: quote_hits=2 function_words=4 page_hits=6 page_terms=54 need=1/2/3/2
S611 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.posenlibrary.com/entry/amulet-woman-childbirth-germany | BOILER: root-clear https://www.posenlibrary.com/; not a title, h1 or meta label | RELEVANCE: shared=['banis', 'demon', 'frame', 'image', 'inscr', 'lilit'] | TOPIC: quote_hits=1 function_words=6 page_hits=14 page_terms=13 need=1/2/3/2
```

Command run (from the scratch directory, absolute paths as required):

```
timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py \
  --draft /fast/scratch/hyaku/kotodama-r59/KotodamaR59.ScoutJewishAmulets/rows.md \
  --entry /fast/scratch/hyaku/kotodama-r59/KotodamaR59.ScoutJewishAmulets/stub.md
```

## Draft entry sentences

S610 (mezuzah / threshold):
- Some Jews have treated the mezuzah as an amulet, a magical charm, even while the tradition's own teaching denies that it protects (S610).
- The mezuzah stays a doorpost sign of the covenant where popular custom reads the same object as a protective device (S610).

S611 (childbirth amulet / printed word and picture):
- A printed amulet from Germany, made about 1725 for a woman in childbirth, sets its zodiac-framed banishing of Lilith among woodcuts of the Hebrew months (S611).
- The birth amulet's protection is written: its central panel banishes Lilith, Adam's mythical first wife, by inscription (S611).

Both pairs share ≥2 content stems with the quote and the teaches cell (rowcheck RELEVANCE PASS above). Nothing in them goes beyond the opened pages: S610's page says the mezuzah is fixed to the doorpost, calls it a sign and reminder of the Covenant, states that popular custom accorded it amulet status, and then denies it is meant to be a protective device; S611's page dates the object ca. 1725, calls it "meant as protection for a woman in childbirth", describes woodcuts of the Hebrew months and the zodiac-framed panel with the Lilith-banishing inscription, and its View Source block says "Amulet printed on parchment from Germany".

## Rejected / opened and not offered

Live-host results are the status-line curl reported (`<status> <bytes>`); page scores are `window_hits` and `DISCIPLINE.findall` from the frozen `reports/round-59/rowcheck.py` run against the saved body.

- **YIVO Encyclopedia, "Amulets"** — https://www.yivoencyclopedia.org/article.aspx/Amulets — `200 643`; body is a JavaScript shell, `<noscript>You need to enable JavaScript to run this app.</noscript>`. No server-rendered text; rejected.
- **Jewish Women's Archive, "Amulets"** — https://jwa.org/encyclopedia/article/amulets — `403 118` (challenge met, not passed); rejected.
- **Met Heilbrunn essay URL tried** — https://www.metmuseum.org/toah/hd/amlt/hd_amlt.htm — `429 34223`; the live essay is Islamic-world amulets, outside this subtopic; rejected.
- **The Jewish Museum (NY), "Childbirth Amulet" 8344** — https://collections.thejewishmuseum.org/collection/8344-childbirth-amulet — `200 91410`; visible text is record fields only (Object Name, Place Made, Date, Medium, Dimensions, Credit Line, Tags), no curatorial description; 4 hits / 3 terms but no quotable prose sentence; rejected.
- **The Jewish Museum (NY), "Birth Amulet" 27899** — https://collections.thejewishmuseum.org/collection/27899-birth-amulet — `200 90702`; same metadata-only page; rejected.
- **Cambridge Digital Library, MS-TS-K-00001-00168** — https://cudl.lib.cam.ac.uk/view/MS-TS-K-00001-00168 — `200 23909`; 3 hits / 4 terms. Its whole description is one 38-word sentence ("An elaborate amulet to protect Sitt al-Faras … from their enemies and give him charm and grace in her eyes."); no 10–25-word full sentence or clause isolating the protective claim; rejected for quote fit.
- **CUDL MS-TS-K-00001-00150** — https://cudl.lib.cam.ac.uk/view/MS-TS-K-00001-00150 — `200 25804`; description is a name-and-purpose catalogue list ("Recto: amulet for Aaron Mukārim b. Najūm, to give him charm and grace …"), no single ≤25-word sentence; rejected for quote fit.
- **CUDL MS-TS-K-00001-00053** — https://cudl.lib.cam.ac.uk/view/MS-TS-K-00001-00053 — `200 23398`; 3 hits / 3 terms; description "A generic amulet to facilitate childbirth, with quotations from Exodus 11:8 and Psalms 142:8." is a viable 15-word sentence, not offered only because the two S-ids went to the mezuzah and the richer dated object (14 hits / 13 terms). Viable alternate if another seat needs a CUDL row.
- **Oxford Jewish Heritage, "Inventory of Judaica and Hebraica"** — https://www.oxfordjewishheritage.co.uk/inventory-of-judaica-and-hebraica/ — `200 282754`; 23 hits / 33 terms. Content is excellent for the topic (glass-tube mezuzah with inscribed parchment roll; copper case with sliding lid inscribed Shaddai and holes for fixing to the doorpost; lead amulets "for protection of boys against the Evil-eye"; amulets "worn … by Russian Jews in London"), but every candidate quote is a numbered inventory list item, which the row rules exclude ("never a heading, title, list item, caption fragment or table cell"); rejected on form, not topic. Worth re-opening in a later round if the list-item exclusion ever allows catalogue entries.
- **JewishArts.org, Francesco Spagnolo, "A Mezuzah at the White House? Sounds Crazy"** — https://jewisharts.org/curations/a-mezuzah-at-the-white-house-sounds-crazy/ — `200 202538`; 2 hits / 14 terms → TOPIC would fail (`page_hits` 2 < 3); rejected.
- **HUC / Heller Museum, "The Mezuzah Message at the Heller Museum"** — https://huc.edu/news/the-mezuzah-message-at-the-heller-museum/ — `200 311650`; 2 hits / 21 terms → TOPIC fail; rejected.
- **Museo Ebraico di Lecce, "Mezuza"** — https://www.museoebraicolecce.com/en/mezuza/ — `200 134408`; 0 hits / 5 terms → TOPIC fail; rejected.
- **Toledo Museum of Art, "Unlock the Power of Protection"** — https://toledomuseum.org/amulet — `403 5584`; rejected.
- **Encyclopaedia Britannica, "Mezuzah"** — https://www.britannica.com/topic/mezuzah — `403 3247`; rejected.
- **Museum of Jewish Heritage search** — https://mjhnyc.org/?s=mezuzah — `403 3109`; rejected.
- **British Library, Zsofi Buda, "The Tree of Knowledge: magic spells from a Jewish potion book"** — https://www.bl.uk/stories/blogs/posts/the-tree-of-knowledge-magic-spells-from-a-jewish-potion-book — `200 36047`; 17 hits / 7 terms. Topic is right (a 16th-century Hebrew magic book with "many amulets providing protection against illnesses like nose bleed, fever, and ear ache"), but the protective clause is a lowercase mid-sentence fragment inside a 44-word sentence, and the only short window sentence ("The very first entry is an amulet against fever:") ends in a colon and is not a sentence; rejected for quote fit.
- **Trachtenberg, *Jewish Magic and Superstition*, ch. 10 "Amulets", Internet Sacred Text Archive** — https://sacred-texts.com/jud/jms/jms12.htm — `200 64536`; 114 hits / 154 terms, the richest body read this seat. Rejected because the site footer states "Copyright © 2026 Evinity Publishing INC. All rights reserved." with no stated permission for the 1939 book — a third-party re-upload of an in-copyright work, not an ordinary copy (QUALITY criterion 10); the host is also already used by S318.
- **Cambridge University Library, Fragment of the Month July 2010** — https://www.lib.cam.ac.uk/collections/departments/taylor-schechter-genizah-research-unit/fragment-month/fragment-month-13-0 — `200 62586`; 7 hits / 3 terms; the body is about how practitioners compiled incantations, not about a protective object's design; the only candidate quote is off-topic; rejected.
- **V&A Collection API, `q=mezuzah`** — https://api.vam.ac.uk/v2/objects/search?q=mezuzah — `200 864`; `"record_count":1` (O114322, a 2001 mezuzah by Mila Griebel). Fields only, no curatorial prose; not offered.
- **British Museum H_2011-8031-1 ("amulet")** — live https://www.britishmuseum.org/collection/object/H_2011-8031-1 returned `403 5536`; Wayback availability returned `{"closest": {"status": "200", ... "timestamp": "20260207002557", ...}}`. Not offered: the live URL fails and the row budget was filled by two 200-serving sources.
- **British Museum H_1945-1009-1 ("pendant; mezuzah; amulet; scroll")** — Wayback availability returned `{"archived_snapshots": {}}` (no capture), and the capture attempt returned `404 2104`; live host already `403`; not offered.
- **Posen Library, "Amulet for the Protection of Women and Newborn Children"** — https://www.posenlibrary.com/entry/amulet-protection-women-and-newborn-children — `200 15614`; 6 hits / 5 terms; its 21-word sentence "Amulets were crafted to protect pregnant women and newborn children from the powers of the evil Lilith, Adam’s mythical first wife." is a strong alternate, not offered only because the dated German object entry carries more design detail.
- **Posen Library, "Amulet against Disease and the Evil Eye"** — https://www.posenlibrary.com/entry/amulet-against-disease-and-evil-eye — `200 16930`; 20 hits / 26 terms; 25-word sentence naming Bunyana bint Yaman and the scribe who wrote other amulets is a strong alternate (written-amulet / named-client / maker evidence), not offered for the same row-budget reason and to avoid a second row from the same host.

## Notes for the L1

- The two offered rows are from different hosts (myjewishlearning.com, posenlibrary.com), both non-reserved, both fresh to `corpus/SOURCES.md` (grep count 0 each), both live-200 at rowcheck time.
- S610's anchor is a 13-word clause cut from a longer sentence (the article's own paragraph continues "Not only in medieval cultures…"). The entry's counter-position sentence ("not meant to be a protective device, nor lack thereof a source of direct punishment") is on the same page but is not the quoted anchor; do not attribute a denial of protection to the quote alone.
- S611's anchor is a full 24-word sentence. The page's licensing notice blocks image download but the text is served openly; the object is credited "Courtesy GFC Trust / William L. Gross" and published in Posen Library vol. 5.
- If the L1 needs a mezuzah *material/placement* quote rather than the status debate, the Oxford Jewish Heritage inventory is the strongest body found (23 windows / 33 terms) but is list-shaped; CUDL MS-TS-K-00001-00053 is the fallback for a written-childbirth-amulet row.
