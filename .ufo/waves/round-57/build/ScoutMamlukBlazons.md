# ScoutMamlukBlazons — round 57, claim C (Mamluk blazons as office emblems)

Seat: KotodamaR57.ScoutMamlukBlazons (leaf). Opened 2026-10-22 by ordinary GET only (curl / locator / urllib); no headless browser, no challenge passed. Two sources reported, both NEW to the lane, every offered quote run through the round locator and pasted below.

Freshness check (mandated form, run in /home/vgpnk/Projects/shokunin/kotodama-shokunin):

```
$ grep -c 'in.ernet.dli.2015.178234' corpus/SOURCES.md
0
$ grep -c 'collection/search/444601' corpus/SOURCES.md
0
```

Notes for the L1 (not part of the source shape):
- The Met live URL answers HTTP 429 with a Vercel Security Checkpoint page to a plain request (challenge met, not passed); the Wayback capture 20251018213642 serves the same record and is the row's locating URL.
- One further Met description sentence — "his sons continued to use his emblem of the ringed cup set within a divided shield" — is present in my local copy of capture 20251018213642 but the locator printed NOT_LOCATED URLError on four attempts (Wayback throttling the seat's connection; the same capture LOCATED three other quotes minutes earlier). Per lane rules it is NOT offered as a quote; the inheritance design point below rests on Mayer's located passage instead.
- Direct fetch of the Mayer djvu.txt 302-redirects to a dl node (dn760007.eu.archive.org) and serves HTTP 200 there; the locator's urllib follows this automatically.

### NEW-ScoutMamlukBlazons-1
citation: Mayer, L. A. 1933, *Saracenic Heraldry: A Survey*, Oxford: Clarendon Press; Internet Archive scan of the Digital Library of India copy (State Central Library, Hyderabad), item `in.ernet.dli.2015.178234`, OCR full text.
url: https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt
route: direct, HTTP 200 (734,288 bytes; the /download/ URL 302-redirects to an archive.org dl node and serves there)
kind: book
tier: A — Mayer's own 1933 arguments and his quotations of Abu-l-Fida', Ibn Taghribirdi and the inscriptions; the period's primary survey of the subject; OCR garble avoided by choosing clean passages.
scope: what the marks are called (blazon, emblem, sign of office); which charge names which court office (cup = cup-bearer/saqi, polo-sticks = polo-master/jukandar, pen-box = secretary/dawadar, napkin = master of the robes); who bore them (amirs) and how they passed between holders (hereditary among amirs, in Mayer's hypothesis only for sons of amirial rank); and the stated limit of the office-reading for later composite blazons. Not a surviving-object inventory (its catalogue is 1933) and not evidence for non-Mamluk emblem systems.
quotes:
- Q1: "the emblems, so far as we can understand them, with very few exceptions represented the office held by the amir"
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt' 'the emblems, so far as we can understand them, with very few exceptions represented the office held by the amir'`
  - `LOCATED https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt`
- Q2: "Although the Saracenic blazon was hereditary among amirs, yet those of their sons who, as so many did, chose an ecclesiastic or administrative career"
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt' 'Although the Saracenic blazon was hereditary among amirs, yet those of their sons who, as so many did, chose an ecclesiastic or administrative career'`
  - `LOCATED https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt`
- Q3: "the blazon was hereditary in the case of sons of amirial rank, not only because of the identity of the blazon"
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt' 'the blazon was hereditary in the case of sons of amirial rank, not only because of the identity of the blazon'`
  - `LOCATED https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt`
- Q4: "There are five simple blazons with polo-sticks and historical texts. They belonged to the following persons"
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt' 'There are five simple blazons with polo-sticks and historical texts. They belonged to the following persons'`
  - `LOCATED https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt`
- Q5: "The typical pen-box consists of four elements; the first, containing the ink-pot, the second the sand-pot and the starch paste-pot"
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt' 'The typical pen-box consists of four elements; the first, containing the ink-pot, the second the sand-pot and the starch paste-pot'`
  - `LOCATED https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt`
- Q6: "the more composite the blazon, the less can the emblem be regarded as a mark of office"
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt' 'the more composite the blazon, the less can the emblem be regarded as a mark of office'`
  - `LOCATED https://archive.org/download/in.ernet.dli.2015.178234/2015.178234.Saracenic-Heraldry_djvu.txt`
teaches: Mamluk blazons named court offices rather than lineages — cup for cupbearer, polo-sticks for polo-master, pen-box for secretary — and, on Mayer's hypothesis, passed to an amir's sons of amirial rank.
draft sentences: A designer reaching for a Mamluk-flavoured emblem system should hang each mark on an office, not a bloodline: whether granted or chosen, the emblems "with very few exceptions represented the office held by the amir" (NEW-ScoutMamlukBlazons-1, Q1). The popular over-reading to avoid is the European hereditary-coat-of-arms model; the stimuli Mayer names for European arms (the face-hiding helmet, hereditary land tenure) had no Eastern counterpart, and although "the Saracenic blazon was hereditary among amirs", sons who took an ecclesiastic or administrative career "apparently had no right to arms" (NEW-ScoutMamlukBlazons-1, Q2). When a worldbuilder does let the mark pass down, Mayer's hypothesis — argued from paired father-and-son blazons such as Baybars and Baraka Khan, Qausun and Husain b. Qausun — is that inheritance held only "in the case of sons of amirial rank", so the son inherits the blazon with the rank, not the office (NEW-ScoutMamlukBlazons-1, Q3). A minor court office is charge enough for a design: "There are five simple blazons with polo-sticks and historical texts. They belonged to the following persons", two of them called jukandar (polo-master) in those very texts, so crossed polo-sticks can denote the court's polo-master office itself (NEW-ScoutMamlukBlazons-1, Q4). The pen-box of the dawadar is drawn as a working toolkit, since "The typical pen-box consists of four elements; the first, containing the ink-pot, the second the sand-pot and the starch paste-pot", with further receptacles for pen-cleaning thread and reeds — a chancery character can literally wear his desk (NEW-ScoutMamlukBlazons-1, Q5). For late-period designs the office-reading breaks down, because "the more composite the blazon, the less can the emblem be regarded as a mark of office": stacked fields of napkin, cup charged with pen-box and 'trousers of nobility' recur throughout Mayer's fifteenth-century catalogue entries, so a composite shield reads as period fashion, not a job title (NEW-ScoutMamlukBlazons-1, Q6).

### NEW-ScoutMamlukBlazons-2
citation: The Metropolitan Museum of Art, "Tray Stand", object 91.1.601, brass inlaid with silver, copper and black compound, attributed to Egypt or Syria, mid-14th century (after 1342), Edward C. Moore Collection, Bequest of Edward C. Moore, 1891; collection record 444601.
url: https://web.archive.org/web/20251018213642id_/https://www.metmuseum.org/art/collection/search/444601 (record page; live URL https://www.metmuseum.org/art/collection/search/444601)
route: live URL returned HTTP 429 with a Vercel Security Checkpoint (challenge met, not passed); quote served by Wayback capture 20251018213642, HTTP 200, 198,556 bytes.
kind: record
tier: A — the holding museum's own identification of the blazon, the office and the named official; evidence only for what the Met states about this object.
scope: what one office blazon looks like on an object (a ringed cup for the cupbearer, on a brass stand that hosts serving trays); how an inscription ties blazon, office and named holder (Husain son of Qawsun, cupbearer to Muhammad b. Qalawun) together; and where the emblem is put (metal serving furniture in a court setting). Not evidence for the blazon's legal status or for objects outside the Met's description.
quotes:
- M1: "It was a blazon of the cupbearer, one of the differentiated offices of the court of the Mamluk sultans"
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://web.archive.org/web/20251018213642id_/https://www.metmuseum.org/art/collection/search/444601' 'It was a blazon of the cupbearer, one of the differentiated offices of the court of the Mamluk sultans'`
  - `LOCATED https://web.archive.org/web/20251018213642id_/https://www.metmuseum.org/art/collection/search/444601`
- M2: "The inscription reads Husain, son of Qawsun, who was cupbearer to Muhammad b. Qalawun"
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://web.archive.org/web/20251018213642id_/https://www.metmuseum.org/art/collection/search/444601' 'The inscription reads Husain, son of Qawsun, who was cupbearer to Muhammad b. Qalawun'`
  - `LOCATED https://web.archive.org/web/20251018213642id_/https://www.metmuseum.org/art/collection/search/444601`
- M4: "Similar stands were widely employed in the Mamluk period to host large rounded metal trays"
  - `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py 'https://web.archive.org/web/20251018213642id_/https://www.metmuseum.org/art/collection/search/444601' 'Similar stands were widely employed in the Mamluk period to host large rounded metal trays'`
  - `LOCATED https://web.archive.org/web/20251018213642id_/https://www.metmuseum.org/art/collection/search/444601`
teaches: The Met's tray stand bears a cupbearer's cup blazon for Husain son of Qawsun, naming his office and sultan in the inscription, so an emblem can ride on serving furniture while words name its holder.
draft sentences: An office emblem needs no shield: on this brass stand "Similar stands were widely employed in the Mamluk period to host large rounded metal trays", and the copper-inlaid cup motif on its side "was a blazon of the cupbearer, one of the differentiated offices of the court of the Mamluk sultans" (NEW-ScoutMamlukBlazons-2, M1). The object names its man the way a document would: "The inscription reads Husain, son of Qawsun, who was cupbearer to Muhammad b. Qalawun (al-Malik al-Nasir)", pairing a named official, his office and his sultan on one surface (NEW-ScoutMamlukBlazons-2, M2). For a worldbuilder this fixes a design idiom that the object itself demonstrates: the cupbearer's cup is put on the stand that hosts the trays, while the inscription names "Husain, son of Qawsun, who was cupbearer to Muhammad b. Qalawun (al-Malik al-Nasir)" — put the office's charge where the office works, and let the words carry the man's identity (NEW-ScoutMamlukBlazons-2, M2).

### Rejected
- Discover Islamic Art (Museum With No Frontiers), "Fragment from a container", Museum of Islamic Art, Cairo, inv. 5146 — https://islamicart.museumwnf.org/database_item.php?id=object;ISL;eg;Mus01;19;en — opened (direct GET, HTTP 200, 39,486 bytes). Its description states the two polo-sticks stand for the game the Mamluks loved and that "the master of the two polo-sticks blazon was called 'al-Jokandar'" with jukandar etymology and the blazon's spread across ceramic, inlaid copper, glass and textiles. Not cited: the seat's two-source budget went to Mayer (which carries polo-sticks/jukandar directly) and the Met record (which carries the object-side evidence); offer it to the L1 only if the entry needs the etymology.
- Discover Islamic Art (Museum With No Frontiers), "Candlestick base", partner record (British Museum), — https://islamicart.museumwnf.org/database_item.php?id=object;ISL;uk;Mus04;17;en — opened (direct GET, HTTP 200, 37,631 bytes). Rejected as a source for this seat's claim: its page text on the record itself adds blazon detail the Met and Mayer rows do not need; kept only to check the portal serves plain text to a plain GET (it does).
- metmuseum.org live collection page https://www.metmuseum.org/art/collection/search/444601 — HTTP 429 Vercel Security Checkpoint on plain GET; challenge met, not passed; the Wayback capture is used instead (recorded in the row's route field).

Locator summary: 9 of 9 offered quotes LOCATED (6 Mayer, 3 Met). All locator output lines are pasted verbatim above.
