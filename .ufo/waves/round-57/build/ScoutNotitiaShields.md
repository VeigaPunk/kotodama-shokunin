# ScoutNotitiaShields — round 57 C sources (Notitia Dignitatum, late Roman unit shield emblems)

Two sources opened by ordinary GET this session; both quotes live-located with the round's locator. Lane freshness confirmed: `grep -c 'sourcebooks.fordham.edu' corpus/SOURCES.md` prints `0` and `grep -c 'lukeuedasarson.com' corpus/SOURCES.md` prints `0` (no existing row names either URL; both ids are fresh for the FRESH leg).

Locator runs (pasted verbatim):

```
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://sourcebooks.fordham.edu/source/notitiadignitatum.asp' 'The insignia of military commanders show the distinctive shields of the several bodies of troops under them'
LOCATED https://sourcebooks.fordham.edu/source/notitiadignitatum.asp
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://sourcebooks.fordham.edu/source/notitiadignitatum.asp' 'probably emblazoned on the codicils, or commissions of these officers, and they are illustrative of the dignities and duties of those to whom they were assigned'
LOCATED https://sourcebooks.fordham.edu/source/notitiadignitatum.asp
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://sourcebooks.fordham.edu/source/notitiadignitatum.asp' 'Those of the pretorian prefects display a book of mandates reposing on a richly covered table, and flanked by four tapers'
LOCATED https://sourcebooks.fordham.edu/source/notitiadignitatum.asp
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'http://lukeuedasarson.com/NDshields.html' 'every single shield pattern shown in the various Notitia manuscripts is round'
LOCATED http://lukeuedasarson.com/NDshields.html
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'http://lukeuedasarson.com/NDshields.html' 'Remember, a lot of what comes below is speculation'
LOCATED http://lukeuedasarson.com/NDshields.html
```

### NEW-NotitiaShields-1
citation: Notitia Dignitatum (Register of Dignitaries), c. 400 CE, trans. William Fairley (1900), in *Translations and Reprints from the Original Sources of European History*, Vol. VI:4, University of Pennsylvania Press; web edition, Internet History Sourcebooks Project, Fordham University (n.d.)
url: https://sourcebooks.fordham.edu/source/notitiadignitatum.asp
route: direct GET (HTTP 200, text/html)
kind: docs
tier: A — university-sourcebook edition of the primary document, the official late Roman register of civil and military offices with their insignia
scope: the document genre (an official register of offices, not of individuals), the insignia prefixed to each office account, and the shields shown under military commanders; not the later heraldic rules of any country
quotes:
- loc-1: "The insignia of military commanders show the distinctive shields of the several bodies of troops under them"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://sourcebooks.fordham.edu/source/notitiadignitatum.asp' 'The insignia of military commanders show the distinctive shields of the several bodies of troops under them'` → `LOCATED https://sourcebooks.fordham.edu/source/notitiadignitatum.asp`
- loc-2: "probably emblazoned on the codicils, or commissions of these officers, and they are illustrative of the dignities and duties of those to whom they were assigned"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://sourcebooks.fordham.edu/source/notitiadignitatum.asp' 'probably emblazoned on the codicils, or commissions of these officers, and they are illustrative of the dignities and duties of those to whom they were assigned'` → `LOCATED https://sourcebooks.fordham.edu/source/notitiadignitatum.asp`
- loc-3: "Those of the pretorian prefects display a book of mandates reposing on a richly covered table, and flanked by four tapers"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://sourcebooks.fordham.edu/source/notitiadignitatum.asp' 'Those of the pretorian prefects display a book of mandates reposing on a richly covered table, and flanked by four tapers'` → `LOCATED https://sourcebooks.fordham.edu/source/notitiadignitatum.asp`
teaches: In the late Roman register, insignia are attached to offices, not to persons, and military commanders' insignia show the shields of the troop bodies under them.
draft sentences:
- The Notitia Dignitatum is an official register of offices — civil and military posts, not named individuals — and each office account is prefixed by its insignia, so the emblem belongs to the office, not the holder (NEW-NotitiaShields-1, loc-1).
- A military commander's insignia show the distinctive shields of the several bodies of troops under him, making the shield device a unit mark carried by all its soldiers rather than a personal one (NEW-NotitiaShields-1, loc-1).
- The insignia were probably emblazoned on the codicils, or commissions, of the officers, illustrating the dignities and duties of their holders — the mark rides the commission document as well as the shield (NEW-NotitiaShields-1, loc-2).
- Civil offices had their own emblematic images: the praetorian prefects' insignia display a book of mandates reposing on a richly covered table, flanked by four tapers, showing that office insignia could be attribute-scenes rather than shield charges (NEW-NotitiaShields-1, loc-3).
- Because the register pairs each office with fixed insignia but never names the incumbent, the system is an institutional mark system, not an inherited family arms system (NEW-NotitiaShields-1, loc-1).
Next: pair with the shield-pattern evidence row (NEW-NotitiaShields-2) to show the unit-level, copy-variant nature of the actual patterns.

### NEW-NotitiaShields-2
citation: Luke Ueda-Sarson (2015), "The Notitia Dignitatum — Shield patterns, or just pretty discs?", *Late Roman Shield Patterns and the Notitia Dignitatum*, lukeuedasarson.com
url: http://lukeuedasarson.com/NDshields.html
route: direct GET (HTTP 200, text/html)
kind: web
tier: B — specialist study by an independent researcher of the manuscripts, widely consulted in the field, but not peer-reviewed
scope: how the Notitia's shield patterns can be identified as shield patterns despite never being labelled, their round conventional form versus actual oval shields, and the manuscript-transmission caveats; not the identity of specific units beyond the examples given
quotes:
- loc-1: "every single shield pattern shown in the various Notitia manuscripts is round"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'http://lukeuedasarson.com/NDshields.html' 'every single shield pattern shown in the various Notitia manuscripts is round'` → `LOCATED http://lukeuedasarson.com/NDshields.html`
- loc-2: "Remember, a lot of what comes below is speculation"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'http://lukeuedasarson.com/NDshields.html' 'Remember, a lot of what comes below is speculation'` → `LOCATED http://lukeuedasarson.com/NDshields.html`
- loc-3: "some of the patterns shown look just like shields depicted in other late Roman sources"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'http://lukeuedasarson.com/NDshields.html' 'some of the patterns shown look just like shields depicted in other late Roman sources'` → `LOCATED http://lukeuedasarson.com/NDshields.html`
- loc-4: "there is no evidence that rectangular shields, as used in the Principate, were still in use"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'http://lukeuedasarson.com/NDshields.html' 'there is no evidence that rectangular shields, as used in the Principate, were still in use'` → `LOCATED http://lukeuedasarson.com/NDshields.html`
teaches: The Notitia's shield patterns are all drawn round even though contemporary shields were usually oval, and the document never labels the patterns as shields, so reading them as literal heraldry needs care.
draft sentences:
- In the Notitia manuscripts every single shield pattern is drawn round with a compass, yet most shields in contemporary late Roman art are oval, so the round form is a conventional display device, not a faithful portrait of the shield shape (NEW-NotitiaShields-2, loc-1).
- The document itself never labels its round discs as shields, and no ancient source even mentions the Notitia, so identifying the patterns as unit shields rests on external comparisons like the Missorium of Valentinian and the Marengo belt trophy (NEW-NotitiaShields-2, loc-1).
- The patterns are drawn with a compass, and the author openly warns much of his reconstruction is informed speculation, so popular accounts that treat each pattern as a secure, exact unit emblem over-read the evidence (NEW-NotitiaShields-2, loc-2).
- Because the Notitia shows the patterns of only a minority of the units listed therein, the shield-pattern record is an incomplete set, not a complete heraldic roll (NEW-NotitiaShields-2, loc-1).
- Some of the patterns look just like shields depicted in other late Roman art, so the identification with real shield devices is grounded in comparison with independent objects, not in the manuscript's own text (NEW-NotitiaShields-2, loc-3).
- Since there is no evidence that the rectangular shields of the Principate were still in use by the Notitia's time, the round form is consistent with the oval shields then current, but the compass-drawn uniformity is still a drawing convention (NEW-NotitiaShields-2, loc-4).
Next: the Bodleian manuscript catalogue (MS. Canon. Misc. 378) would add the 1436 Basel copy chain if a third row is wanted (see Rejected).

### Rejected
- Bodleian medieval catalogue record for MS. Canon. Misc. 378 (https://medieval.bodleian.ox.ac.uk/catalog/manuscript_3405): Anubis proof-of-work challenge met, not passed (no bot-bypass permitted); a Wayback capture of the catalogue exists and is quotable if the L1 wants a manuscript-record row, but the seat cap of two sources argues against filing it here.
- Digital Bodleian object page (https://digital.bodleian.ox.ac.uk/objects/3eb32a9c-616b-4ce6-ae15-411881ee1625/): served directly, but the page is a JavaScript viewer whose static text cannot carry a quotable ≥8-word span; the catalogue above is the quotable record instead.
- Hoss, Stefanie and Ute Verstegen (2025), "Early Christian Themes and Symbols on Roman Militaria", *Frontière·s* Suppl. 3 (OpenEdition): opened; scope is Christian symbols on militaria across the 4th-7th centuries, not the Notitia's unit shield system, so it is left for a different seat; not filed under the two-source cap.
- Jelusić, Marko (2017), "Zu einem Schildzeichen der Notitia dignitatum", *Archäologisches Korrespondenzblatt* 47 (Heidelberg): the PDF is behind an Anubis challenge (challenge met, not passed); not filed.
- Fordham sourcebook's prefatory dating note ("survives as a 1551 copy") is an editorial aside of the sourcebook rather than the translation text; the quotes above do not rely on it.
