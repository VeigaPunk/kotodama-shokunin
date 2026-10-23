# ScoutWitchMarks — claim C source report (round 59, 2026-10-23)

Sub-assignment: apotropaic marks in buildings — ritual protection marks (daisy wheels, VV/Marian
marks) at thresholds, doorways and chimneys; heritage bodies.
S-ids offered: **S620, S621**. Both rows print LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS.

Method: ordinary GETs only (`curl`, python `urllib` with the round-59 instrument's own user
agent, and `rowcheck.py`/`reopen-quote.py`), no browser, no challenge or access control passed.
Both offered pages were opened **live** in this session; each row's Wayback capture is of the same
page, from the same URL, and was checked separately as the FETCH-59 fallback.

Why not Historic England: every Historic England URL refused a plain GET with HTTP 403 (own
user agent and `curl` alike), so no row rests on that host — a capture of a page I could not open
live is not something I will list (see rejected, verbatim). The heritage bodies that did serve
plain GETs are the two offered.

## Rows

| S620 | Agecroft Hall & Gardens (Richmond, Virginia), "Apotropaic Mark", museum blog post in the English History series, signed "Agecroft Hall", undated (records the daisy wheel found in 2016 by dendrochronologist Dr Ian Tyers in the Great Parlour panelling) — https://www.agecrofthall.org/single-post/apotropaic-mark (direct, HTTP 200, 160412 bytes); capture https://web.archive.org/web/20250805115319id_/https://www.agecrofthall.org/single-post/apotropaic-mark | docs | B | a museum's own reading of one house's mark and of why such marks gather at openings; the general placement statement is the museum's synthesis of the secondary literature it cites, not fieldwork (tier note: B) | body paragraph after the Daemonologie passage: "apotropaic marks are usually found where there is an opening through which evil could easily enter—doors, windows, and fireplaces" | Protective marks cluster at doors, windows and fireplaces, the openings through which evil was thought to enter a house. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S621 | Provan Hall (Glasgow), "Exhibitions" page, section "Witches' Marks" by Lauren McCarthy, Collections and Engagement Assistant — https://www.provanhall.org/exhibitions (direct, HTTP 200, 229010 bytes); capture https://web.archive.org/web/20260509153310id_/https://www.provanhall.org/exhibitions | docs | B | a heritage venue's exhibition text on the marks inside its own 17th-century entrance archway: what witches' marks are made of, where they sit, and how they are told apart from masons' marks (tier note: B, venue staff writing an exhibition blog) | § Witches’ Marks, third paragraph: "Witches’ marks were a common form of ritual protection in which symbols or patterns were carved into the stonework or woodwork of historic buildings." | Witches' marks are carved symbols and lines cut into stone or timber as a standing ritual defence of a historic building. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

Anchor-quote hygiene: S620's quote is the main clause (20 words) of a 27-word sentence, quoted
from the first word after its participial opener; S621's is a complete 24-word sentence. Both are
body prose, not headings, captions, list items or meta text; neither page's `<title>`/`<h1>`/meta
carries them (BOILER root-clear on both). Every URL after the first in each source cell is a
Wayback capture of that same page (same-page rule); no DOI, landing page or second copy is in
either cell.


Capture verification (FETCH-59 fallback, both checked this session outside the rowcheck run so the
live URL stays the first locator):

- S620 capture `20250805115319` serves HTML (1,361,730 bytes); the quote locates in it, `hits=21
  terms=14` — same page, same metrics as the live body.
- S621 capture `20260509153310` serves HTML (213,341 bytes); the quote locates, `hits=43 terms=27`,
  identical to the live page's TOPIC metrics.
- Warning for other seats: the nearest Provan Hall capture by the availability API, `20260513004439`,
  is served raw gzip (`1f 8b` magic) by the `id_` form, which the instrument's text pipeline does
  not decode, so that capture cannot locate anything and was replaced by the May capture above.
  Check the first two bytes of any `id_` capture before listing it.

## Gate lines

- S620 — https://www.agecrofthall.org/single-post/apotropaic-mark — accessed 2026-10-23 — body paragraph after the Daemonologie passage: “apotropaic marks are usually found where there is an opening through which evil could easily enter—doors, windows, and fireplaces”. Grounds: Protective marks cluster at doors, windows and fireplaces, the openings through which evil was thought to enter a house. Seat: ScoutWitchMarks.
- S621 — https://www.provanhall.org/exhibitions — accessed 2026-10-23 — § Witches’ Marks, third paragraph: “Witches’ marks were a common form of ritual protection in which symbols or patterns were carved into the stonework or woodwork of historic buildings.”. Grounds: Witches' marks are carved symbols and lines cut into stone or timber as a standing ritual defence of a historic building. Seat: ScoutWitchMarks.

## rowcheck output (verbatim)

```
$ cd /fast/scratch/hyaku/kotodama-r59/ScoutWitchMarks && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutWitchMarks/rows.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutWitchMarks/stub.md
S620 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.agecrofthall.org/single-post/apotropaic-mark | BOILER: root-clear https://www.agecrofthall.org/; not a title, h1 or meta label | RELEVANCE: shared=['door', 'enter', 'evil', 'firep', 'mark', 'openi'] | TOPIC: quote_hits=2 function_words=5 page_hits=21 page_terms=14 need=1/2/3/2
S621 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.provanhall.org/exhibitions | BOILER: root-clear https://www.provanhall.org/; not a title, h1 or meta label | RELEVANCE: shared=['build', 'carve', 'histo', 'mark', 'ritua', 'stone'] | TOPIC: quote_hits=2 function_words=7 page_hits=43 page_terms=27 need=1/2/3/2
```

(A first run with an earlier anchor cell died on S621 `LOCATE: quote under 8 words` because a
second pair of double quotes — the section name — preceded the real quote in the anchor cell, and
a second run died on `RELEVANCE: teaches-copies-quote` for a six-word run of the anchor; both were
fixed in the row, not in the instrument. The output above is the final state of `rows.md`/`stub.md`.)

## draft sentences

S620 (Agecroft Hall, museum blog on the Great Parlour daisy wheel):

- Apotropaic marks gather at the openings a building cannot close, the doors, windows and fireplaces through which evil was thought to enter (S620).
- The reasoning is entry: because evil could easily come in at an opening, the mark is put where it can meet that entry (S620).

S621 (Provan Hall, "Witches' Marks" exhibition text):

- The protection is carved into stonework or woodwork, so it belongs to the building rather than to a person (S621).
- Carving symbols and patterns into the fabric was a common form of ritual protection, not a rare private act (S621).

## What these rows carry for the entry (design decisions)

Quote-borne (safe for the entry):

- what a mark is made *in*: cut into stonework or woodwork of the building itself, not worn on the body (S621).
- what danger it answers: evil that "could easily enter" at an opening; witches (S620's page, S621's quote where marks repel "evil spirits" in the page's following sentence).
- where it is placed: at doors, windows and fireplaces — the openings of a house (S620); at the entry/threshold of a building (S621's page, following sentence).
- that the practice was common rather than exceptional (S621).

Page-borne but outside the quoted span (usable only as page-level colour, not as row support):

- Provan Hall: the marks inside its 17th-century stone archway, the argument against reading them as masons' marks (cruder lines, consistent placement at entry points), the Marian V/M reading tied to the Reformation, taper burn marks on timber, and continuous practice "until the early 1800s" (S621 page).
- Agecroft Hall: mantels as the commonest spot, overlapping repeats, scorch marks added to the daisy wheel, hexafoils under floorboards near doors/windows/fireplaces, and marks painted on plaster or embroidered on textiles (S620 page).

**Do not** turn either row into a universal: S620's generalisation is an American museum's summary
about English houses, S621 is one Scottish venue's exhibition text about UK buildings. Neither
supports "all pre-modern societies marked their thresholds".

## rejected

Opened (or attempted) and not offered, with the tool's own output where a tool result is the reason:

- https://historicengland.org.uk/whats-new/features/discovering-witches-marks/what-are-witches-marks/ — Historic England's own feature page; would have been the first-choice heritage-agency row. Refused a plain GET, so never opened live and therefore no capture listed (wave rule: never save a capture of a page you could not open live; and this host answered 403). Verbatim (`curl -sS -o /dev/null -w '%{http_code} %{size_download} %{content_type}'`): `403 5776 text/html; charset=UTF-8  https://historicengland.org.uk/whats-new/features/discovering-witches-marks/what-are-witches-marks/`.
- https://historicengland.org.uk/whats-new/features/discovering-witches-marks/types-of-marks/ — same 403. Verbatim: `403 5709 text/html; charset=UTF-8`. Its Wayback capture (`20260920210925`) did fetch, but the live page could not be opened, so it is not offered.
- https://historicengland.org.uk/whats-new/features/discovering-witches-marks/public-response/ — same 403. Verbatim: `403 5755 text/html; charset=UTF-8`.
- https://historicengland.org.uk/whats-new/news/help-hunt-for-witches-marks/ — same 403. Verbatim: `403 5680 text/html; charset=UTF-8`. The instrument's own fetch agrees: `ERR HTTPError HTTP Error 403: Forbidden`.
- https://www.nationaltrust.org.uk/discover/history/warding-off-evil-with-witch-marks — National Trust; the request was rewritten to a WAF interstitial, no article text served. Verbatim: `200 2263 https://static.nationaltrust.org.uk/waf/waf.html?_event_transid=8ab69b862311828acc539a5540b062c23ceadf598d8d3616e33b9db9c2f1dd38` (Content-Length 2263 = `waf.html`).
- https://www.shakespeare.org.uk/explore-shakespeare/blogs/witch-markings-magic-old-buildings/ — Shakespeare Birthplace Trust blog by Historic England's Nick Molyneux. Opened live (HTTP 200, 76848 bytes) and read in full; has good placement prose ("the location of the marks and objects is often near entrances and exits from the building, particular doorways and hearths") and a witch-bottle-under-hearth-stone sentence. Rejected on TOPIC: the page carries only **one** DISCIPLINE term in body text (the single word "apotropaic"; its "Witch Markings" is a title), so TOPIC would fail. Verbatim from my scorer: `page_hits 4 page_terms 1`.
- https://www.wessexarch.co.uk/apotropaic-marks-bath-abbey — Wessex Archaeology, "Apotropaic Marks in Bath Abbey" (31.10.18, by Bob Davis, Senior Heritage Consultant). Opened live (HTTP 200, 9662 chars of text) and read: daisy wheels on the stone door jamb of the Vestry, a knot on a stair-turret doorway, and James VI's "by any opening which air may enter" reasoning. Its cleanest quote ("Apotropaic marks were used to protect buildings from evil spirits and witches; the word comes from the Greek term ‘apotropaios’ meaning ‘averting evil’.") passes the legs (`quote_hits=3`). Not offered on the two-row budget: it is the reserve row if a reviewer rejects S620 or S621, and its passing sentence is a definition where the two offered sentences carry placement and material. Page metrics: `page_hits=19 page_terms=11`.
- https://shura.shu.ac.uk/26362/1/036_FT392.pdf — David Clarke, "Marks of the Witch: Britain's ritual protection symbols", Fortean Times 392 (2020): 36–43, SHURA published version. Opened and read (28,807 chars; `page_hits=78 page_terms=61`). Rejected: a popular magazine article (tier B at best), and the passages that fit my subtopic best are damaged in the served text — the chimney sentence reads "Chimneys and ﬁ replaces were also focal points…" (ligature + broken word), and the placement sentence ("Liminal zones were seen as vulnerable…therefore hearths, windows and doors required special treatment") carries no CHARM word at all, so the anchor would either be corrupt or fail TOPIC.
- https://www.apotropaios.co.uk/ — Brian Hoggard's research site. Opened (6,588 chars, `hits=19 terms=26`) but the page is a navigation/link hub (Hidden Charms conference lists, shop, survey links); no continuous body paragraph to anchor.
- https://ritualprotectionmarks.com/ — research site front page. Opened (19,368 chars, `hits=30 terms=22`). Its one substantive sentence is the site's mission blurb, which is also the page's own description/meta text — a BOILER risk rather than a body claim.
- https://www.svbrg.org.uk/witch.php — Suffolk Building Recording Group "Witch marks". Opened (4,717 chars, `hits=12 terms=6`); the body is a bulleted list of mark types (hexafoil, VV, taper burn), and list items cannot carry an anchor quote.
- https://www.tudorhouse.org.uk/2022/04/tudor-house-worcester-witch-mark-rediscovered/ — Tudor House museum (Worcester) news post on a daisy wheel found in its café area. Opened (6,928 chars, `hits=15 terms=13`). Not offered on the two-row budget; its cleanest sentence ("Despite their name, witch marks may have very little to do with witches or witch craft.") states the name/function gap that S621's page states at length, and S621's quote is fuller body text.
- Host probes that produced no candidate row: https://www.english-heritage.org.uk/ `403 5492`, https://cadw.gov.wales/ `403 55276`, https://www.le.ac.uk/ `403 5477` (all refused plain GETs); https://www.historicenvironment.scot/ `200 138032` and https://www.visitchurches.org.uk/ `200 92900` served plain GETs but I found no page on apotropaic marks there within the assignment's subtopic before the row budget was filled.

## Out of bounds / not done

- No lane file other than this report was created or edited; scratch work is under
  `/fast/scratch/hyaku/kotodama-r59/ScoutWitchMarks/` (`rows.md`, `stub.md`, page texts, probes).
- No installs, no pacman, no git/jj writes; read-only `git status` only.
