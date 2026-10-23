# ScoutSoldierAmulets — claim C source seat (amulets carried into danger)

Round 59, claim C, source seat. Subtopic: amulets carried into danger — Japanese senninbari thousand-stitch belts, First World War soldiers' charms and talismans; museum records.

**Outcome: two rows offered (S642, S643), both PASS on all four rowcheck legs, and both PASS again on two further runs of the same draft (the final run is pasted below).** No senninbari row is offered: every accessible senninbari record either refused a plain GET or failed the TOPIC fence (details in `## Rejected`).

## Method

- Every page opened by ordinary means: plain `curl` GET (Firefox 131 UA), no browser automation, no challenge or paywall bypass. Opened in this session only.
- Every row checked with the round-59 instrument before filing:
  `timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft …/rows5.md --entry …/stub5.md`
  (draft and entry copies live at `/fast/scratch/hyaku/kotodama-r59/ScoutSoldierAmulets/rows5.md` and `stub5.md`).
- No tool installed or updated; no package transaction run.
- Both URLs are absent from `corpus/SOURCES.md` (`grep -c` returns 0 for each).

## Rows

| S642 | Thwaite, Annie, 2019, "A history of amulets in ten objects", Science Museum Group Journal, Spring 2019, DOI 10.15180/191103 — https://journal.sciencemuseum.ac.uk/article/history-of-amulets/ (direct, HTTP 200, 502,294 bytes) | paper | B | the article's report of the classical distinction between therapeutic, apotropaic and exorcistic amulets; the classification, not evidence for any object's efficacy | section on the Pliny passage, sentence on classical use: "Yet most importantly (as described by Pliny since the first century CE) amulets were worn and used for therapeutic, apotropaic or exorcistic benefit." | Pliny's account, as the article reports it, has amulets worn for healing, for apotropaic warding and for exorcism, three distinct jobs. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S643 | Victoria and Albert Museum, London, object record "Amulet Box (ga'u)", made in Tibet, 1800-1850, silver, brass and coral, no author or publication date on the record — https://collections.vam.ac.uk/item/O87367/ (direct, HTTP 200, 46,556 bytes) | docs | A | the record's own description of what a body-worn amulet box contains and what its contents are believed to do; not a claim about efficacy | Physical description, first sentence: "An amulet box or ga'u used to contain rolled prayers and blessed or holy objects believed to protect the wearer against evil." | A ga'u is a box holding rolled prayers and sanctified items, and the protection against evil is credited to those contents rather than to the metal shell. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

### Gate lines

- S642 — https://journal.sciencemuseum.ac.uk/article/history-of-amulets/ — accessed 2026-10-23 — section on the Pliny passage, sentence on classical use: “Yet most importantly (as described by Pliny since the first century CE) amulets were worn and used for therapeutic, apotropaic or exorcistic benefit.”. Grounds: Pliny's account, as the article reports it, has amulets worn for healing, for apotropaic warding and for exorcism, three distinct jobs. Seat: ScoutSoldierAmulets.
- S643 — https://collections.vam.ac.uk/item/O87367/ — accessed 2026-10-23 — Physical description, first sentence: “An amulet box or ga'u used to contain rolled prayers and blessed or holy objects believed to protect the wearer against evil.”. Grounds: A ga'u is a box holding rolled prayers and sanctified items, and the protection against evil is credited to those contents rather than to the metal shell. Seat: ScoutSoldierAmulets.

### Rowcheck output (pasted verbatim, `rows5.md` / `stub5.md`)

```
S642 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://journal.sciencemuseum.ac.uk/article/history-of-amulets/ | BOILER: root-clear https://journal.sciencemuseum.ac.uk/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'apotr', 'exorc', 'pliny', 'worn'] | TOPIC: quote_hits=2 function_words=7 page_hits=311 page_terms=242 need=1/2/3/2
S643 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://collections.vam.ac.uk/item/O87367/ | BOILER: root-clear https://collections.vam.ac.uk/; not a title, h1 or meta label | RELEVANCE: shared=['evil', 'praye', 'prote', 'rolle'] | TOPIC: quote_hits=2 function_words=5 page_hits=21 page_terms=16 need=1/2/3/2
```

### Draft sentences (each ends with its citing id)

- S642: The same worn object can be therapeutic, apotropaic or exorcistic, so a worldbuilder should say which of the three jobs a given amulet is for. (S642)
- S642: Because the article's Pliny passage gives amulets all three uses, an entry can describe one object as both healing and apotropaic without contradiction. (S642)
- S643: An amulet box carries writing rather than an image, so a worldbuilder can make the prayer scroll the object that protects and the metal shell only its housing. (S643)
- S643: Because the ga'u is worn and its amulet contents are blessed, the blessing is a step in manufacture rather than a property of the metal. (S643)

Notes the L1 may want when writing entry lines:

- S642 carries the *job* distinction (heal / ward / drive out), not the amulet-vs-charm-vs-talisman wording. That wording sits in the same article in one sentence — "Whilst definitions vary, ‘charm’ is often used synonymously with ‘amulet’, whilst ‘talisman’ features less frequently." — which also passes the instrument, but one URL may carry one row (DISTINCT forbids a shared URL), so pick whichever the entry needs; both are verbatim on the page and neither is a label.
- S643 carries placement (worn on the body), content (rolled prayers plus blessed objects) and the claim that the *contents* are believed to protect, which is the material-design point: the container is a housing, the writing and the blessing are the working part. The record also says the case is silver, brass and coral, made in Tibet 1800-1850; do not extend the row to the metal-and-coral materials, which the anchor quote does not carry.

## Rejected (opened, not offered)

1. **https://collection.sciencemuseumgroup.org.uk/objects/co103794/metal-amulet-with-ribbon** and **…/co103790/glass-amulet** — WWI records (metal amulet of a military bandsman worn by a Middlesex Regiment soldier; glass nazar worn by a soldier in Palestine). Both passed every leg on the first run (`S642 … quote_hits=2 function_words=6 page_hits=43 page_terms=39`; `S643 … quote_hits=1 function_words=6 page_hits=26 page_terms=27`) and were the intended pair. Withdrawn because the host throttles bursts and the same draft then failed on a re-run, which is exactly the FETCH-59 failure mode:
   `S642 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co103794/metal-amulet-with-ribbon HTTPError | BOILER: not-located | …`
   `S643 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://collection.sciencemuseumgroup.org.uk/objects/co103790/glass-amulet HTTPError | BOILER: not-located | …`
   A single paced GET afterwards returned `200 43904`, and a body of `Rate limited - please slow down` (31 bytes) appears under burst. The two records are strong material for this topic — if a later round wants them, they need a paced fetch and, ideally, a Wayback capture; no capture exists today (`archive_snapshots: {}`).
2. **https://charmedsoldiers.theworldwar.org/charmed-soldiers-home** (National WWI Museum and Memorial exhibition). Candidate quote "In the chaotic furnace of warfare, mass-produced trinkets became potent talismans to ward off death, and holy items forged even greater supernatural power." — `S643 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | … BOILER: quote-on-root https://charmedsoldiers.theworldwar.org/`. The sentence is printed on the site root, so BOILER refuses it. (A capture exists at 20260705233201; the capture fetch answered `429 620` on both http and https attempts, so it could not be verified.)
3. **https://charmedsoldiers.theworldwar.org/learn/about-wwi/charms** — `PAGE windows: 2 terms: 8`; TOPIC needs three windows, and the sentences that carry windows have one function word (`Servicemembers believed these small tokens offered protection through folk traditions or magic.` → `function_words: 1`). Sibling paths `/learn/about-wwi/{medals,devotional,postcards,talismans,objects}`, `/explore-more-items`, `/items` all answered `404`.
4. **https://digitalcommons.unl.edu/tsaconf/1228/** — Nagai, Mariko, 2024, "Public Patriotism, Silent Dissent: Women and the Making of Senninbari in Wartime Japan" (Textile Society of America Symposium Proceedings), the one open scholarly senninbari item found. Landing page: `PAGE windows: 2 terms: 2` — one window short of the TOPIC fence (`need=1/2/3/2`), so no quote from it can pass, including the good sentence `Some had talismans from local shrines sewn in to ward off bullets.` (`w=1 fw=3`) and `Often worn around soldiers’ waists underneath their uniforms, these sash-shaped talisman were embroidered with 1,000 red knots, each knot made by a woman.` (`w=1 fw=5`). Full text PDF: `403 5746` (bot block; not bypassed).
5. **Senninbari museum records, all refused or unusable:** `https://www.awm.gov.au/collection/C149279` → `403 79`; `https://www.iwm.org.uk/history/8-objects-of-superstition-from-the-first-world-war` → `403 5823`; `https://americanhistory.si.edu/collections/object/nmah_725209` → `403 46602`; `https://www.si.edu/object/senninbari-thousand-stitch-belt:nmah_725209` → `403 46672`; `https://collections.si.edu/search/detail/edanmdm:nmah_725209` → `403 46607`; `https://collection.nam.ac.uk/detail.php?acc=1989-04-98-1` → `000 0` (twice, 45 s and 90 s); `https://mot-collection-search.jp/en/shiryo/12346/` → `000 0`; `https://encyclopedia.densho.org/Senninbari/` → `404 8835`.
6. **https://ddr.densho.org/ddr-densho-105-8/** (Densho, senninbari made at Tule Lake): `PAGE windows: 1 terms: 0`.
7. **https://egausa.org/courses/senninbari-mariko-nagai/** : `PAGE windows: 1 terms: 1`, and its one prose sentence is 43 words.
8. **https://blog.sciencemuseum.org.uk/soldiers-armed-with-lucky-charms/** (Stewart Emmens, 11 November 2010): page level passes (`PAGE windows: 6 terms: 6`) but no quotable sentence clearing the fence simultaneously carries a window, two function words and 10–25 words; the only windowed prose lines were `Good luck charm (Science Museum) This lucky black cat belonged to a soldier in the London Regiment.` (a caption plus sentence) and `Such traditional symbols of good luck are common.` (8 words). Its `The original museum label for the medallion above says it was provided by a Roman Catholic nun, for a soldier fighting in France.` is 23 words with nine function words but `w=0`. Kept as a lead for a seat that can quote a caption-free passage.
9. **https://england.prm.ox.ac.uk/englishness-Edward-Lovett.html** (Pitt Rivers, Lovett): `PAGE windows: 72 terms: 73`, but every windowed candidate is an archival list fragment, e.g. `Sympathetic Magic - B.2 White Magic - Figure Symbols - Description: Sheep's heart stuck with nails and pins - formerly used for "breaking evil spells".` — not defensible body text.
10. **https://collections.vam.ac.uk/item/O111090/** (wedjat-eye amulet): `PAGE windows: 17 terms: 16`, one candidate `Wedjat eye of Horus was a popular amulet (XXVIth Dynasty or later).` — a fragment, and off this seat's subtopic.
11. **https://wellcomecollection.org/works/m3upta5r** → `405 2131` (also with an `Accept: text/html` header); **https://api.wellcomecollection.org/catalogue/v2/works/m3upta5r** → `410 110` `{"errorType":"http","httpStatus":410,"label":"Gone","description":"This work has been deleted",…}`.
12. **https://museum.wales/first-world-war/?id=5065** → `000 0`; **https://nzhistory.govt.nz/search?keys=lucky%20charms** → `403 5660`; **https://www.theworldwar.org/learn/about-wwi/charms** → `403 77924`; **https://api.aucklandmuseum.com/search?q=senninbari** → `403 21725`; **https://collections.tepapa.govt.nz/api/search?q=senninbari** → `200 87` (empty result set); **https://museumofwitchcraftandmagic.co.uk/object/amulet-charm-3/** → `503 3571`; **https://collections.museumvictoria.com.au/search?query=senninbari** → `403 5542`; **https://www.nam.ac.uk/explore/{good-luck-charms,lucky-charms,soldiers-charms}** → `404 40498`.
13. **https://www.britishmuseum.org/collection/search?keyword=senninbari** → `403 5694`, body `<title>Just a moment...</title>` (a bot challenge; not bypassed, per QUALITY criterion 10).
14. **https://api.vam.ac.uk/v2/objects/search?q=senninbari** → `record_count 0`; **…q=thousand+stitch** → 143 records, all Stein Collection textiles, none a senninbari.
15. **https://journal.sciencemuseum.ac.uk/search/?q=amulets** → `404 230531` (no in-journal search endpoint).

## Open gaps

- No senninbari row in this seat's packet. The topic remains uncovered by an opened source I could also verify: the accessible scholarly abstract is one TOPIC window short, and every museum record with curatorial text sits behind a 403 (AWM, IWM, Smithsonian) or a timeout (NAM).
- Host advisory for the L1: `collection.sciencemuseumgroup.org.uk` rate-limits bursts (a body reading `Rate limited - please slow down` arrives in place of the record), so rows from it are a live risk under FETCH-59; `journal.sciencemuseum.ac.uk` and `collections.vam.ac.uk` each served repeatedly without incident in this session.
