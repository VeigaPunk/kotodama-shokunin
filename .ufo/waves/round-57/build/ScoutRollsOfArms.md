# ScoutRollsOfArms — round 57 C sources (medieval rolls of arms: Zürich Armorial, Armorial de Gelre)

Two sources opened by ordinary GET this session (plain curl / urllib, no headless browser, no challenge met): the e-codices record of the Zürich Armorial (Schweizerisches Nationalmuseum, AG 2760) and the KBR OPAC record of the Armorial de Gelre (Ms. 15652-56). All ten quotes live-located with the round's locator, output pasted verbatim below. Lane freshness confirmed before fetching: `grep -n -i -E 'e-codices|kbr|gelre|wappenrolle' corpus/SOURCES.md` prints no row naming either URL or host/path (only unrelated `bl.uk`/`britishmuseum` rows match "british"), so both ids are fresh for the FRESH leg. No collision with sibling seats' scope observed in the build directory as of writing.

Locator runs (pasted verbatim):

```
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.e-codices.unifr.ch/en/list/one/snm/AG002760' 'The Zurich armorial on parchment is one of the most important and most unusual documents of medieval heraldry.'
LOCATED https://www.e-codices.unifr.ch/en/list/one/snm/AG002760
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.e-codices.unifr.ch/en/list/one/snm/AG002760' 'it depicts 559 coats of arms, each shield decorated with a crest, of high and lower nobility from Northern Switzerland, Southern Germany and Western Austria'
LOCATED https://www.e-codices.unifr.ch/en/list/one/snm/AG002760
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.e-codices.unifr.ch/en/list/one/snm/AG002760' 'Names are given next to each shield. In addition there are 28 flags of German bishoprics and monasteries.'
LOCATED https://www.e-codices.unifr.ch/en/list/one/snm/AG002760
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.e-codices.unifr.ch/en/list/one/snm/AG002760' 'It can be dated to the period between 1330 and 1345.'
LOCATED https://www.e-codices.unifr.ch/en/list/one/snm/AG002760
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.e-codices.unifr.ch/en/list/one/snm/AG002760' 'Parchment · 1 f. · 12 x 400 cm · Area of Lake Constance · around 1330-1345'
LOCATED https://www.e-codices.unifr.ch/en/list/one/snm/AG002760
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.e-codices.unifr.ch/en/list/one/snm/AG002760' 'The missing fourth part should have contained another 109 coats of arms, which are known from a late 18th century copy'
LOCATED https://www.e-codices.unifr.ch/en/list/one/snm/AG002760
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56' 'Convolute, consisting of two main sections, I (f. 1-25, the so-called Brabant and Holland section, dated c. 1403-1404)'
LOCATED https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56' 'the so-called original Gelre section, dated c. 1393-1402'
LOCATED https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56' 'f. 122r [Drawing of the herald Gelre, Claes Heynen]'
LOCATED https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56' 'large quantity of coloured heraldic coats of arms ; 21.9 x 14.2 cm'
LOCATED https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56
```

### NEW-ScoutRollsOfArms-1
citation: Schweizerisches Nationalmuseum, Zürich, "Zürich Armorial" (shelfmark AG 2760), e-codices manuscript record, persistent id 10.5076/e-codices-snm-AG002760 (record page current 2026-10-22)
url: https://www.e-codices.unifr.ch/en/list/one/snm/AG002760
route: direct GET (HTTP 200, text/html, 86,760 bytes)
kind: record
tier: A — the holding museum's own catalogue record on the standard Swiss manuscript platform, giving caption, dating and a full physical description
scope: what a roll of arms is and carries — four sewn parchment parts, c. 1330-1345, Lake Constance region; 559 coats of arms with crests of high and lower nobility; names beside shields; 28 flags of German bishoprics and monasteries; incompleteness known only through a late 18th-century copy; not blazon vocabulary, cadency or granting law
quotes:
- loc-1: "The Zurich armorial on parchment is one of the most important and most unusual documents of medieval heraldry."
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.e-codices.unifr.ch/en/list/one/snm/AG002760' 'The Zurich armorial on parchment is one of the most important and most unusual documents of medieval heraldry.'` → `LOCATED https://www.e-codices.unifr.ch/en/list/one/snm/AG002760`
- loc-2: "it depicts 559 coats of arms, each shield decorated with a crest, of high and lower nobility from Northern Switzerland, Southern Germany and Western Austria"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.e-codices.unifr.ch/en/list/one/snm/AG002760' 'it depicts 559 coats of arms, each shield decorated with a crest, of high and lower nobility from Northern Switzerland, Southern Germany and Western Austria'` → `LOCATED https://www.e-codices.unifr.ch/en/list/one/snm/AG002760`
- loc-3: "Names are given next to each shield. In addition there are 28 flags of German bishoprics and monasteries."
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.e-codices.unifr.ch/en/list/one/snm/AG002760' 'Names are given next to each shield. In addition there are 28 flags of German bishoprics and monasteries.'` → `LOCATED https://www.e-codices.unifr.ch/en/list/one/snm/AG002760`
- loc-4: "It can be dated to the period between 1330 and 1345."
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.e-codices.unifr.ch/en/list/one/snm/AG002760' 'It can be dated to the period between 1330 and 1345.'` → `LOCATED https://www.e-codices.unifr.ch/en/list/one/snm/AG002760`
- loc-5: "Parchment · 1 f. · 12 x 400 cm · Area of Lake Constance · around 1330-1345"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.e-codices.unifr.ch/en/list/one/snm/AG002760' 'Parchment · 1 f. · 12 x 400 cm · Area of Lake Constance · around 1330-1345'` → `LOCATED https://www.e-codices.unifr.ch/en/list/one/snm/AG002760`
- loc-6: "The missing fourth part should have contained another 109 coats of arms, which are known from a late 18th century copy"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://www.e-codices.unifr.ch/en/list/one/snm/AG002760' 'The missing fourth part should have contained another 109 coats of arms, which are known from a late 18th century copy'` → `LOCATED https://www.e-codices.unifr.ch/en/list/one/snm/AG002760`
teaches: A roll of arms is a dated physical register — one long parchment listing hundreds of named shields and crests across a whole nobility, not a single family's monument.
draft sentences:
- A roll of arms is a physical, datable object rather than an abstract system: the Zurich armorial is a parchment roll of four parts (caption: 12 x 400 cm, thirteen sewn leaves per the description), assigned to the area of Lake Constance and dated to the period between 1330 and 1345 (NEW-ScoutRollsOfArms-1, loc-4).
- A roll inventories a whole status group at once — it depicts 559 coats of arms, each shield decorated with a crest, of high and lower nobility from Northern Switzerland, Southern Germany and Western Austria — so the entry can present arms as a shared regional vocabulary, not one house's property (NEW-ScoutRollsOfArms-1, loc-2).
- The pairing of image and label is the identification mechanism: names are given next to each shield, so a design is anchored to a person or line and can be checked against rivals in the same list (NEW-ScoutRollsOfArms-1, loc-3).
- Marks ride on more than shields: the same roll carries 28 flags of German bishoprics and monasteries, showing ecclesiastical institutions bearing arms on banners, a design lever for worldbuilders arming churches and abbeys (NEW-ScoutRollsOfArms-1, loc-3).
- Counts quoted from armorials need a hedge: the record states the armorial is incomplete and its missing fourth part is known only from a late 18th-century copy, so headline totals (559) mix present and reconstructed arms — an outsider's over-read to flag in the entry (NEW-ScoutRollsOfArms-1, loc-6).
Next: the record also notes the workmanship recalls the Codex Manesse and names later owners (Grimm, the Antiquarische Gesellschaft) if the entry wants provenance.

### NEW-ScoutRollsOfArms-2
citation: Koninklijke Bibliotheek van België (KBR), Brussels, "Wapenboek Gelre : Ms. 15652-56" (compiler: Gelre, fl. 1334-1372; illuminators Herman Maelwael, fl. 1373-1397, and Willem Maelwael, fl. 1386-1395), OPAC manuscript record, opened 2026-10-22
url: https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56
route: direct GET (HTTP 200, text/html, 236,531 bytes; the same record also serves with `?_lg=en-GB`)
kind: record
tier: A — the holding library's own catalogue record, giving the manuscript's dated sections, collation, attribution and place
scope: how a great armorial is organised and attributed — two dated sections in one convolute (Brabant and Holland c. 1403-1404; original Gelre c. 1393-1402), bibliographic address [Low Countries: Gelre (Nijmegen?)], [1390-1415], collation with coloured coats of arms, compiler identified as the herald Gelre (Claes Heynen); not the content of any individual blazon
quotes:
- loc-1: "Convolute, consisting of two main sections, I (f. 1-25, the so-called Brabant and Holland section, dated c. 1403-1404)"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56' 'Convolute, consisting of two main sections, I (f. 1-25, the so-called Brabant and Holland section, dated c. 1403-1404)'` → `LOCATED https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56`
- loc-2: "the so-called original Gelre section, dated c. 1393-1402"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56' 'the so-called original Gelre section, dated c. 1393-1402'` → `LOCATED https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56`
- loc-3: "f. 122r [Drawing of the herald Gelre, Claes Heynen]"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56' 'f. 122r [Drawing of the herald Gelre, Claes Heynen]'` → `LOCATED https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56`
- loc-4: "large quantity of coloured heraldic coats of arms ; 21.9 x 14.2 cm"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56' 'large quantity of coloured heraldic coats of arms ; 21.9 x 14.2 cm'` → `LOCATED https://opac.kbr.be/Library/doc/SYRACUSE/16995818/wapenboek-gelre-ms-15652-56`
teaches: A major armorial is a compiled, portable book assembled by a named herald in dated regional sections, evidence that arms were a working reference profession.
draft sentences:
- An armorial can grow as a compiled book with separately dated parts: KBR's record describes the Gelre manuscript as a convolute of two main sections, a Brabant and Holland section (f. 1-25) dated c. 1403-1404 and the original Gelre section (f. 26-111) dated c. 1393-1402, followed by added material on f. 112-124 (NEW-ScoutRollsOfArms-2, loc-1).
- The record dates the core section c. 1393-1402 while giving the whole book a broader bibliographic address, [Low Countries: Gelre (Nijmegen?)], [1390-1415] — a model for how entries should carry hedges a catalogue itself makes (NEW-ScoutRollsOfArms-2, loc-2).
- The trade has named professionals: the compiler is catalogued as Gelre (fl. 1334-1372), and the record locates at f. 122r a drawing of the herald Gelre, Claes Heynen, a self-depiction placing the roll's maker inside his own book (NEW-ScoutRollsOfArms-2, loc-3).
- The object is a handheld reference, not a wall monument: the collation records (ii) + 124 + (ii) folios with a large quantity of coloured heraldic coats of arms at 21.9 x 14.2 cm (NEW-ScoutRollsOfArms-2, loc-4).
- Together the dated sections imply arms were collected region by region and re-bound later — a worldbuilder can mirror this by letting in-world armorials accumulate additions from different decades (NEW-ScoutRollsOfArms-2, loc-1).
Next: Wikimedia Commons carries a full Gelre leaf gallery by folio if the entry needs a quotable image source, but the OPAC record is the citable dating authority.

### Rejected
(none — both opened sources filed above; no Wayback captures were needed as both pages served directly to plain GET)
