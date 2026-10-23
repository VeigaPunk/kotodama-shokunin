# ScoutIrishLogainm — claim C source item (Irish placenames, logainm.ie)

Seat: KotodamaR58A2.ScoutIrishLogainm. S-ids: S524, S525. Accessed 2026-10-23 by plain `curl` (UA `Mozilla/5.0`) and by `reports/round-58/rowcheck.py`'s own fetch. Neither URL is in `corpus/SOURCES.md`: `grep -F 'logainm.ie' corpus/SOURCES.md` prints nothing.

Publisher: logainm.ie, the Placenames Database of Ireland. Its `/en/about/about-project` page says the project disseminates "the State's toponymic data", run by Fiontar & Scoil na Gaeilge (DCU) for the Placenames Branch (Government of Ireland), so I treat it as tier A (official or institutional). The featured themes are signed essays by Branch and Gaois researchers.

## Rows

| S524 | Conchubhar Ó Crualaoich & Aindí Mac Giolla Chomhghaill (logainm.ie, Placenames Database of Ireland: Placenames Branch with Gaois, DCU), 2026-09-07, featured theme "Briars, cranks and Strawberryhill" — https://www.logainm.ie/en/themes/187 (direct, HTTP 200) | web | A | official Irish name versus English half-translation of an Irish village name | theme body, Driseachán paragraph: "An Driseachán, with the article, is the official name of the village in County Galway known in English by the half-translation Brierfield" | An Irish village can carry an official Irish name while its English name is only a half-translation of that Irish form. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S525 | Conchubhar Ó Crualaoich, Aindí Mac Giolla Chomhghaill & Justin Ó Gliasáin (logainm.ie, Placenames Database of Ireland: Placenames Branch with Gaois, DCU), 2026-10-06, featured theme "Mountoven / Cnocán an Bhácúis" — https://www.logainm.ie/en/themes/206 (direct, HTTP 200) | web | A | a later English name layered over an older Irish townland name | theme body, Mountbell paragraph: "The English name Mountbell is a much later addition to that area’s toponomy, a reference to the Big House that sits in this townland." | In an Irish townland, an English name like Mountbell can be a much later layer referring to the local Big House. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

## Gate lines

- S524 — https://www.logainm.ie/en/themes/187 — accessed 2026-10-23 — theme body, Driseachán paragraph: “An Driseachán, with the article, is the official name of the village in County Galway known in English by the half-translation Brierfield”. Grounds: An Irish village can carry an official Irish name while its English name is only a half-translation of that Irish form. Seat: ScoutIrishLogainm.
- S525 — https://www.logainm.ie/en/themes/206 — accessed 2026-10-23 — theme body, Mountbell paragraph: “The English name Mountbell is a much later addition to that area’s toponomy, a reference to the Big House that sits in this townland.” Grounds: In an Irish townland, an English name like Mountbell can be a much later layer referring to the local Big House. Seat: ScoutIrishLogainm.

## rowcheck output

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutIrishLogainm/rows.md`

```
S524 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.logainm.ie/en/themes/187 | BOILER: root-clear https://www.logainm.ie/; not a title, h1 or meta label | RELEVANCE: shared=['engli', 'half', 'name', 'offic', 'trans', 'villa'] | TOPIC: quote_hits=1 function_words=7 page_hits=5 page_terms=48 need=1/2/3/2
S525 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.logainm.ie/en/themes/206 | BOILER: root-clear https://www.logainm.ie/; not a title, h1 or meta label | RELEVANCE: shared=['engli', 'house', 'later', 'mount', 'name', 'refer'] | TOPIC: quote_hits=2 function_words=7 page_hits=5 page_terms=61 need=1/2/3/2
exit=0
```

**S525 BOILER risk (the L1 needs to know this).** Right now the logainm.ie home page (`https://www.logainm.ie/en/`) shows a truncated preview of featured theme 206. The preview stops exactly at "...the hill of the burning’. The Englis", one sentence before the S525 quote begins. So BOILER passes today by a single sentence. If the site lengthens its preview, or a later verifier re-runs while 206 is still featured with a longer cut, S525 would fail BOILER. Once a newer theme replaces 206 on the home page, the risk goes away. A pre-checked fallback row for the same S-id, from a theme not previewed on the home page, is given below. It is not a third offered row: swap it in only if S525 fails BOILER.

Fallback for S525 (checked):

| S525 | Conchubhar Ó Crualaoich & Justin Ó Gliasáin (logainm.ie, Placenames Database of Ireland: Placenames Branch with Gaois, DCU), 2026-09-01, featured theme "Shesheraghmore / An tSeisreach Mhór" — https://www.logainm.ie/en/themes/205 (direct, HTTP 200) | web | A | English townland names that translate Irish originals | theme body, Middleplough paragraph: "placenames such as Middleplough don’t appear to be a feature of English toponomy" | Townland names of the Middleplough type are not typical of English toponomy, so such English forms likely translate Irish originals. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

```
S525 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.logainm.ie/en/themes/205 | BOILER: root-clear https://www.logainm.ie/; not a title, h1 or meta label | RELEVANCE: shared=['engli', 'middl', 'topon'] | TOPIC: quote_hits=1 function_words=5 page_hits=5 page_terms=53 need=1/2/3/2
exit=0
```

(The rowcheck run above used the fallback with the authors written as "Ó Crualaoich & Mac Giolla Chomhghaill". The page signs it "(Conchubhar Ó Crualaoich & Justin Ó Gliasáin)", which is corrected in the row above. The source cell is not part of any leg except URL extraction.) The fallback quote is a clause cut from a 34-word sentence. The page then says "in which case we can be reasonably confident that it is indeed a translation from Irish in this instance". A reviewer reading the full sentence will see the teaches cell supported, but the quote alone carries only the "not typical of English toponomy" half.

## draft sentences

S524:
- Irish place names can split by language: the Galway village whose official name is An Driseachán, "briary place", is known in English by the half-translation Brierfield (S524).
- A half-translation keeps only part of the Irish name in English, so a village's official Irish name and its English name stop matching word for word (S524).
- The Placenames Database of Ireland pairs each official Irish form with its English form, as with An Driseachán and Brierfield. The same page shows an Irish suffix at work: -óg/-eog usually marks a diminutive, but in names it can mean a place abounding in something, as in Driseog, anglicized Drishoge (S524).

S525:
- Irish townland names stratify by language layer: the townland whose original Irish name was Cnoc an Loiscreáin now carries the English name Mountbell, a much later addition that refers to the Big House in the townland (S525).
- A later English name need not translate the Irish one: Mountbell refers to the Big House, not to the corn-singeing place that the Irish name Cnoc an Loiscreáin describes (S525).
- Tottenhamgreen in Wexford is likewise a later English name. It contains the surname of the family who acquired the townland after a Cromwellian grant, laid over an original Irish name, Baile an Loiscreáin (S525).

Fallback S525 (only if swapped in):
- Some English townland names are translations of Irish ones: the page judges Middleplough in Tipperary a likely translation of An tSeisreach Láir, because names of that type are not a feature of English toponomy (S525).

Use for the worldbuilder (an inference from these pages, not a quoted claim): give a conquered or settled place an official native name plus an outsider name. The outsider name can be a half-translation (Brierfield), a full translation (Milltown for Baile an Mhuilinn, theme 206), or an unrelated later estate name (Mountbell). Each choice tells the reader a different story about contact.

## rejected

- https://www.logainm.ie/en/ — site root. BOILER cannot use the root, and it carries the featured-theme preview.
- https://www.logainm.ie/en/about — index page, 45 words of body text, no sentence with a naming-place window.
- https://www.logainm.ie/en/glossary — the elements (baile, cill, dún...) are list and table cells with glosses, never sentences, so they are barred by the row rules.
- https://www.logainm.ie/en/glossary/14-baile — served HTTP 200, but my tag-stripped text had 0 lines over 60 characters (`wc -w glossary_14-baile.txt` → `0`). There is no body sentence to quote.
- https://www.logainm.ie/en/resources — a listing of resource blurbs, no windowed sentence.
- https://www.logainm.ie/en/about/placenames-branch — best "who gives the name" content: the Branch determines Irish versions, which get legal status through a placenames order by the Minister under the Official Languages Act 2003. But the key sentence is 27 words, and "placenames" stems to PLACE only, not NAMING, so it has no window. My enumeration script (rowcheck's `window_hits` over sentences of 40 words or fewer) printed no candidate for this page: `##### about_placenames-branch.txt pagehits 3 terms 13` with no lines under it.
- https://www.logainm.ie/en/about/placenames-committee — Placenames Committee appointed July 2024 under the Official Languages Act 2021, advising the Minister. No windowed sentence: `##### about_placenames-committee.txt pagehits 2 terms 16` with no lines under it.
- https://www.logainm.ie/en/about/name-acceptability — the only windowed sentences are category definitions with no main verb, so they are not full clauses. Script output: `[23] Placenames or geographical names whose official, legal Irish versions are specified in various Placenames Orders in accordance with the Official Languages Act 2003.`
- https://www.logainm.ie/en/about/about-project — used only for publisher status. No windowed sentence.
- https://www.logainm.ie/en/about/sources — Ordnance Survey history (OS established in Ireland in 1824, first survey completed in 1846, O'Donovan employed). Its only windowed sentence is merged with a heading: `[31] A note regarding editorial work carried out on the collection The methodology used by the Placenames Branch ... has changed over time.` Page `pagehits 1` in my text.
- https://www.logainm.ie/en/themes/193 (Púca in placenames) — the best Ordnance Survey anglicisation and folk-etymology content, e.g. "Of course the standard anglicized spelling was chosen in 1839 precisely in order to reflect that supposed derivation." That sentence has no NAMING stem, so it fails TOPIC. The windowed sentences don't teach the point: `[29] ... the identification of the púca in townland names and other toponyms.`, `[14] We can almost certainly count the townland name Pollaphuca ( logainm.ie # 43687 ) in Co.` (a fragment), and `[18] Roscommon as another example, even though research has not been completed on the townland names of that county.` It is also currently featured on the home page.
- https://www.logainm.ie/en/themes/186, /188, /189, /190, /191, /192 — script output: 186 `[20] ... Irish personal name Méarán (see placenamesni.org )` and `[34]` (over 25 words); 188 to 192 `pagehits 1`, below PAGE_HITS 3, with no windowed sentence.
- https://www.logainm.ie/en/themes (index) — it concatenates the theme bodies and its content rotates. The individual theme URLs are the stable ones.
- https://www.gov.ie/en/department-of-rural-and-community-development-and-the-gaeltacht/organisation-information/the-placenames-branch/ and https://www.gov.ie/en/publication/placenames-branch/ — `curl` returned `gov 403` / `403`. That is access control, so per QUALITY criterion 10 I did not try to get around it.

## installs:

None.
