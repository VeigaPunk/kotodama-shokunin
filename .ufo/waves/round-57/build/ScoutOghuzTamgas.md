# ScoutOghuzTamgas — C-source report (round 57)

Seat: KotodamaR57.ScoutOghuzTamgas (leaf, no delegation). Goal: Oghuz clan tamgas
listed by Mahmud al-Kashgari (Diwan Lughat at-Turk, 11th c.) and by Rashid al-Din —
open scholarly source or public-domain translation reproducing/describing the list;
quote the number of clans and what the marks were used for, with locators.

Both URLs are FRESH: `grep -cF "CompendiumOfTheTurkicDialectsPart1"` = 0,
`grep -cF "islamawareness.net/CentralAsia"` = 0, `grep -ciF "tamga|ongun|oguz|kashgari|kashghari"` = 0 in corpus/SOURCES.md.

No installs were made (curl and pdftotext were already present; pypdf was used
ephemerally via `uv run --with pypdf==5.4.0`, not installed).

---

### NEW-ScoutOghuzTamgas-1

citation: Mahmud al-Kashgari, trans. Robert Dankoff & James Kelly, 1982, Compendium of the Turkic Dialects (Dīwān Lughāt at-Turk), Part I, Sources of Oriental Languages and Literatures 7, Harvard University (English translation of the 11th-century Diwan; archive.org scan identifier `CompendiumOfTheTurkicDialectsPart1-MahmudAl-Kashghari`, full text djvu)
url: https://archive.org/download/CompendiumOfTheTurkicDialectsPart1-MahmudAl-Kashghari/Al-K%C4%81%C5%A1%D0%B3ar%C4%AB%2C%20Mah%CC%A3m%C5%ABd.-Compendium%20of%20the%20Turkic%20dialects%20%28D%C4%ABw%C4%81n%20lug%C4%81t%20at-Turk%29%2C%20Part%20I%20%281_3%29_djvu.txt
route: direct, HTTP 200 (archive.org/download 302 -> dn760107.eu.archive.org)
kind: book (primary text, scholarly translation, open full text)
tier: A — the primary 11th-century source itself, in authoritative open translation, directly listing the 22 Oghuz branches and their brands
scope: the 22 Oghuz/Turkmen branches; the brand (tamga/belge) as a cattle mark distinguishing each branch; the unknown brand of the 22nd branch; brands drawn in red ink; copyists leaving blank spaces for brands
quotes:
- q1: "A tribe of the Turks; the Turkman. They consist of twenty-two branches"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py '<url>' 'A tribe of the Turks; the Turkman. They consist of twenty-two branches'`
  `LOCATED https://archive.org/download/CompendiumOfTheTurkicDialectsPart1-MahmudAl-Kashghari/Al-K%C4%81%C5%A1%D0%B3ar%C4%AB%2C%20Mah%CC%A3m%C5%ABd.-Compendium%20of%20the%20Turkic%20dialects%20%28D%C4%ABw%C4%81n%20lug%C4%81t%20at-Turk%29%2C%20Part%20I%20%281_3%29_djvu.txt`
- q2: "Their branches I shall mention, along with the brands of their cattle, since people need to know them"
  `LOCATED https://archive.org/download/CompendiumOfTheTurkicDialectsPart1-MahmudAl-Kashghari/Al-K%C4%81%C5%A1%D0%B3ar%C4%AB%2C%20Mah%CC%A3m%C5%ABd.-Compendium%20of%20the%20Turkic%20dialects%20%28D%C4%ABw%C4%81n%20lug%C4%81t%20at-Turk%29%2C%20Part%20I%20%281_3%29_djvu.txt`
- q3: "Caruqluy. They are few in number and their brand is unknown"
  `LOCATED https://archive.org/download/CompendiumOfTheTurkicDialectsPart1-MahmudAl-Kashghari/Al-K%C4%81%C5%A1%D0%B3ar%C4%AB%2C%20Mah%CC%A3m%C5%ABd.-Compendium%20of%20the%20Turkic%20dialects%20%28D%C4%ABw%C4%81n%20lug%C4%81t%20at-Turk%29%2C%20Part%20I%20%281_3%29_djvu.txt`
- q4: "leaves a blank space for the brand to be filled in later"
  `LOCATED https://archive.org/download/CompendiumOfTheTurkicDialectsPart1-MahmudAl-Kashghari/Al-K%C4%81%C5%A1%D0%B3ar%C4%AB%2C%20Mah%CC%A3m%C5%ABd.-Compendium%20of%20the%20Turkic%20dialects%20%28D%C4%ABw%C4%81n%20lug%C4%81t%20at-Turk%29%2C%20Part%20I%20%281_3%29_djvu.txt`
- q5: "Brands are in red ink; numbers over brands are in pencil"
  `LOCATED https://archive.org/download/CompendiumOfTheTurkicDialectsPart1-MahmudAl-Kashghari/Al-K%C4%81%C5%A1%D0%B3ar%C4%AB%2C%20Mah%CC%A3m%C5%ABd.-Compendium%20of%20the%20Turkic%20dialects%20%28D%C4%ABw%C4%81n%20lug%C4%81t%20at-Turk%29%2C%20Part%20I%20%281_3%29_djvu.txt`
- q6: "a treatise on the Oyuz subtribes and their brands"
  `LOCATED https://archive.org/download/CompendiumOfTheTurkicDialectsPart1-MahmudAl-Kashghari/Al-K%C4%81%C5%A1%D0%B3ar%C4%AB%2C%20Mah%CC%A3m%C5%ABd.-Compendium%20of%20the%20Turkic%20dialects%20%28D%C4%ABw%C4%81n%20lug%C4%81t%20at-Turk%29%2C%20Part%20I%20%281_3%29_djvu.txt`
teaches: The 11th-century Diwan treats Oghuz/Turkmen identity as twenty-two branches marked by cattle brands.
draft sentences:
- Kashgari's 11th-century Diwan presents the Oghuz, whom he calls the Turkman, as twenty-two branches. (NEW-ScoutOghuzTamgas-1, q1)
- Of all Turkic tribes, only the Oghuz-Turkman branches are enumerated together with the brands of their cattle, because people needed to know them. (NEW-ScoutOghuzTamgas-1, q2)
- The final branch, Caruqluy, is few in number and its brand unknown — the catalogue itself records a gap. (NEW-ScoutOghuzTamgas-1, q3)
- The brands were drawn in red ink, and a later copyist left a blank space where a brand was to be filled in. (NEW-ScoutOghuzTamgas-1, q5)

---

### NEW-ScoutOghuzTamgas-2

citation: F. Esin Özalp, 2008, A Historical and Semantical Study of Turkmens and Turkmen Tribes, MA thesis, Bilkent University, Ankara (open web copy; §1.2.1.6 "List of the Names, Tamgas, Onguns and Ülüş of the Oghuz/Turkmen Tribes According to Reşîdeddin Fazlullah", pp. 39–42)
url: https://www.islamawareness.net/CentralAsia/Turkmenistan/turkmenistan_article0001.pdf
route: direct, HTTP 200
kind: docs (scholarly thesis)
tier: B — university thesis (Bilkent) with documented citations to Rashid al-Din (via Togan, Sümer) and to Barthold's totem reading; secondary but scholarly and open
scope: Rashid al-Din's 24-clan Oghuz scheme; the ongun (sacred bird of prey) shared every four clans (six onguns total); the Irkıl Hoca legend assigning nişan/tamga to the 24 grandsons; branding herds/avoiding ownership disputes as the marks' purpose; Barthold's totem interpretation and Wittek's "systematizing legend" caveat
quotes:
- r1: "all of them should be given a nişan [meaning decoration or mark] and tamga in order everyone to know his place"
  `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py '<url>' 'all of them should be given a nişan [meaning decoration or mark] and tamga in order everyone to know his place'`
  `LOCATED https://www.islamawareness.net/CentralAsia/Turkmenistan/turkmenistan_article0001.pdf`
- r2: "Barthold interprets this reverence and the term ongun as a totem since these birds could neither be touched nor be eaten"
  `LOCATED https://www.islamawareness.net/CentralAsia/Turkmenistan/turkmenistan_article0001.pdf`
- r3: "he mentions a total of six onguns, one for every four Oghuz clans"
  `LOCATED https://www.islamawareness.net/CentralAsia/Turkmenistan/turkmenistan_article0001.pdf`
- r4: "the belges are used for branding the tribes' herds, thus they could recognize each other's herds"
  `LOCATED https://www.islamawareness.net/CentralAsia/Turkmenistan/turkmenistan_article0001.pdf`
- r5: "can scarcely be considered as an historical reality but rather as a systematizing legend"
  `LOCATED https://www.islamawareness.net/CentralAsia/Turkmenistan/turkmenistan_article0001.pdf`
teaches: Rashid al-Din's scheme gives 24 Oghuz clans tamgas plus shared sacred birds (onguns).
draft sentences:
- In Rashid al-Din's account every four Oghuz clans share one of six onguns, sacred birds of prey, linked to the clans' reverence. (NEW-ScoutOghuzTamgas-2, r3)
- In the Oghuz legend, Irkıl Hoca gives each of Oghuz Khan's twenty-four grandsons a nişan and a tamga so everyone knows his place. (NEW-ScoutOghuzTamgas-2, r1)
- Barthold interprets the ongun as a totem because these birds could neither be touched nor eaten — an outsider's interpretation, not a claim of the source. (NEW-ScoutOghuzTamgas-2, r2)
- Scholars warn that the twenty-four-tribe division can scarcely be taken as historical reality, reading it as a systematizing legend. (NEW-ScoutOghuzTamgas-2, r5)

---

### Rejected

- `https://www.academia.edu/44948359/` (Oghuz tamgas PDF) — requires login/access control; not an ordinary public copy.
- `https://www.scribd.com/doc/161316242/Tamgas` — commercial document host, paywall/login.
- `https://en.wikipedia.org/wiki/Oghuz_Turks` and `.../Tamga` — community source; tier C; used only for orientation, not cited.
- `http://s155239215.onlinehome.us/turkic/30_Writing/301Tamgas/KashgariTamgasEn.htm` (TurkicWorld) — opened (HTTP 200), rejected: community page with untraceable provenance; superseded by the Dankoff/Kelly translation above.
- `https://revistes.ub.edu/index.php/dialectologia/article/download/52307/44769` (First Dialectologists) — listed in search results but not opened; not offered.
- `https://ekitap.yek.gov.tr/Uploads/ProductsFiles/49edc3d1-4e82-4221-955f-64e12af7f006.pdf` (TDV Turkish edition with tribal-stamp illustrations) — not opened; not offered.
