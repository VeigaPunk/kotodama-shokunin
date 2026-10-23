# ScoutMesopotamiaPazuzu — claim C source report (round 59, 2026-10-23)

Sub-assignment: Mesopotamian protective figures and amulets — Pazuzu heads and plaques
against Lamashtu, protection of mothers and infants.
S-ids offered: S602, S603. Two rows, both LOCATE/BOILER/RELEVANCE/TOPIC PASS.

Method: ordinary GETs only (`curl` and `urllib.request`, desktop UA, no cookies), no browser,
no challenge circumvention. Both PDFs were opened live in this session and read via the
round-59 `reopen-quote.py`/`rowcheck.py` text pipeline (pypdf 5.4.0 via `uv run`); the one
Wayback capture listed for each row is of the same page I opened live.

## Rows

| S602 | Heeßel, Nils P. 2007, "Pazuzu," Iconography of Deities and Demons in the Ancient Near East (IDD), Electronic Pre-Publication, University of Zurich, last revision 10 December 2007 — https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf (direct plain request, HTTP 200, application/pdf, 197,505 bytes); capture https://web.archive.org/web/20210303023053id_/https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf | paper | B | the iconography, materials, forms and protective use of Pazuzu images in the first millennium BCE | §I Introduction: "P. served particularly as the antagonist of the baby-snatching demon →Lamashtu, and was a favourite amulet of pregnant women and young mothers." | Pazuzu was favoured as an amulet by pregnant women and young mothers because he opposed the baby-snatching demon Lamashtu. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S603 | Said, Miriam 2020, "Radiance and the Power of Erasure in an Obsidian Lamaštu Amulet," Metropolitan Museum Journal 55 (2020): 100–109 — https://resources.metmuseum.org/resources/metpublications/pdf/Said_Metropolitan_Museum_Journal_v_55_2020.pdf (direct plain request, HTTP 200, application/pdf, 16,579,613 bytes); capture https://web.archive.org/web/20240703133613id_/https://resources.metmuseum.org/resources/metpublications/pdf/Said_Metropolitan_Museum_Journal_v_55_2020.pdf | paper | A | how a Lamaštu amulet protects: image, incantation and material | p. 101: "This amulet, small enough to fit in the palm of one’s hand, provides protection from the Mesopotamian demon Lamaštu." | A palm-sized amulet provides protection against the Mesopotamian demon Lamashtu. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

## Gate lines

- S602 — https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf — accessed 2026-10-23 — §I Introduction: “P. served particularly as the antagonist of the baby-snatching demon →Lamashtu, and was a favourite amulet of pregnant women and young mothers.”. Grounds: Pazuzu was favoured as an amulet by pregnant women and young mothers because he opposed the baby-snatching demon Lamashtu. Seat: ScoutMesopotamiaPazuzu.
- S603 — https://resources.metmuseum.org/resources/metpublications/pdf/Said_Metropolitan_Museum_Journal_v_55_2020.pdf — accessed 2026-10-23 — p. 101: “This amulet, small enough to fit in the palm of one’s hand, provides protection from the Mesopotamian demon Lamaštu.”. Grounds: A palm-sized amulet provides protection against the Mesopotamian demon Lamashtu. Seat: ScoutMesopotamiaPazuzu.

## rowcheck output (verbatim)

```
$ cd /fast/scratch/hyaku/kotodama-r59/ScoutMesopotamiaPazuzu && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutMesopotamiaPazuzu/rows.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutMesopotamiaPazuzu/stub.md
S602 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf | BOILER: root-clear https://www.religionswissenschaft.uzh.ch/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'baby', 'demon', 'favou', 'lamas', 'mothe'] | TOPIC: quote_hits=1 function_words=6 page_hits=37 page_terms=56 need=1/2/3/2
S603 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://resources.metmuseum.org/resources/metpublications/pdf/Said_Metropolitan_Museum_Journal_v_55_2020.pdf | BOILER: root-clear https://resources.metmuseum.org/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'demon', 'mesop', 'palm', 'prote', 'provi'] | TOPIC: quote_hits=1 function_words=6 page_hits=107 page_terms=99 need=1/2/3/2
```

## draft sentences

S602 (Heeßel, IDD "Pazuzu"):

- In first-millennium Mesopotamia the demoness Lamashtu who snatched babies was answered by Pazuzu: his image became the favourite amulet of pregnant women and young mothers (S602).
- A worldbuilder assigning a protective object to a named danger can note that pregnant women and young mothers favoured the amulet against the baby-snatching demon: the image of Pazuzu (S602).

S603 (Said, Metropolitan Museum Journal 55):

- The demon named beside a protective object is the threat it answers: a palm-sized amulet provides protection from Lamashtu, the Mesopotamian demon (S603).
- A palm-sized amulet could itself provide protection from the demon Lamashtu, so a worldbuilder's protective object may be tiny enough to keep close in the hand (S603).

Design decisions these rows can carry in the entry: what danger the object answers (Lamashtu,
who preyed on babies), who it protects (pregnant women, young mothers), how a demon's image
protects (the antagonist logic — Pazuzu, himself a feared wind demon, set against Lamashtu;
her own image on an amulet that imprisons and expels her), what the object is (small heads;
a palm-sized obsidian plaque with image on one side and cuneiform incantation on the other),
and the words it carries (the Met amulet's incised incantation). Both pages are scholarly
secondary sources held on institutional hosts, readable in full by a plain GET.

## rejected

Opened and not offered, with reason and verbatim tool output:

- http://oracc.museum.upenn.edu/amgg/listofdeities/pazuzu/ and .../lamashtu/ — ORACC Ancient
  Mesopotamian Gods and Goddesses entries (University of Pennsylvania), the ideal university
  source for this subtopic. Rejected: the http URL 302-redirects to https, and https fails
  TLS verification for curl and for the locator's `urllib` fetcher alike. Verbatim:
  `urllib: URLError <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed:
  unable to get local issuer certificate` on all three requests.
- https://archeologie.culture.gouv.fr/orient-cuneiforme/en/pazuzu-and-fight-against-forces-evil
  and /demons-and-genii-mesopotamia — French Ministry of Culture "Orient cunéiforme" heritage
  pages. Rejected: the whole host answered HTTP 503 on three tries this session (verbatim:
  `HTTP/2 503`, 51,729-byte error page), so the pages were never opened.
- https://collections.mfa.org/objects/163646 — MFA Boston object record ("Pazuzu was an
  Assyrian-Babylonian demonic being..."). Rejected: the host answered `202` with a zero-byte
  body (bot challenge held open); the record was never served. Verbatim: `202 0 text/html`.
- https://collections.louvre.fr/en/ark:/53355/cl010120485 — Louvre collections record
  "amulette" (Pazuzu accroupi). Opened live (HTTP 200, 55,796 bytes). Rejected: the record's
  description is JavaScript-rendered; the served text holds only title fields and a
  bibliography — no curatorial sentence to anchor a quote.
- https://www.bible-orient-museum.ch/fr/musee/collections/index/amulettes.html — BIBLE+ORIENT
  Museum (University of Fribourg) "Amulettes" collection page. Opened live (HTTP 200, 37,501
  bytes). Rejected: the page is French-language, so no quote carries the English CHARM/GUARD
  stems TOPIC requires; it is also about the museum's Egyptian amulet collection, off the
  Mesopotamian subtopic.
- https://art.thewalters.org/search/?q=pazuzu — Walters Art Museum. Opened (HTTP 200, 411,199
  bytes); the search holds no Pazuzu/Lamashtu objects (zero hits). Rejected: no object to open.
- https://harvardartmuseums.org/collections?q=pazuzu and
  https://www.clevelandart.org/art/collection/search?search=pazuzu — both HTTP 200 but
  JavaScript shells: no object links or object text in the served HTML; no record could be
  opened. Rejected.
- https://artsanddivinityfacultyjournal.wp.st-andrews.ac.uk/files/2022/10/A-surprising-gap_-The-usage-of-Pazuzu-and-Lamashtu-amulets-in-Mesopotamian-birthing-practices.pdf
  — Arts & Divinity Faculty Journal, University of St Andrews, "A surprising gap: The usage of
  Pazuzu and Lamashtu amulets in Mesopotamian birthing practices." Opened (HTTP 200,
  application/pdf, 439,983 bytes; text read: 12 pages, ~23,400 chars; windows=133,
  terms=168). Rejected on authority, not mechanics: a student-run journal; the two offered
  rows cover the same ground with the stronger IDD reference and the peer-reviewed
  Metropolitan Museum Journal article. Usable backup if a third Mesopotamian row is wanted.
- Hosts refused before any page could be opened (no content read): `https://www.mfa.org/search`
  403 5622; `https://www.penn.museum/collections/object/100000` 403 961 and
  `https://www.penn.museum/collections/search?searchTerm=pazuzu` 403 961;
  `https://artgallery.yale.edu/collections/search?edan_q=pazuzu` 403 5723;
  `https://toledomuseum.org/amulet` 403 5542; `https://www.dia.org/art/collection/search?keyword=pazuzu`
  404 40708 (search path moved, no object opened); `https://www.imj.org.il/en/collections/search?query=pazuzu`
  timeout (curl exit: 000, 0 bytes); `https://collectionapi.metmuseum.org/public/collection/v1/search?q=pazuzu`
  410 438 (search endpoint gone).

Tooling: no installs this session (uv + system pypdf tooling already present).

Scratch files (rows, entry stub, fetched pages, scoring helper) are under
/fast/scratch/hyaku/kotodama-r59/ScoutMesopotamiaPazuzu/.
