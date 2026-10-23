# ScoutChildBirthProtection — claim C source report (round 59, 2026-10-23)

Sub-assignment: protection of mothers, infants and children — coral, red threads, bells,
childbirth amulets and cradle charms across traditions; museum records.
S-ids offered: S640, S641. Two rows, both LOCATE/BOILER/RELEVANCE/TOPIC PASS.

Method: ordinary GETs only (`curl` + the round-59 `rowcheck.py` / `reopen-quote.py` text
pipeline), no browser, no challenge circumvention. Both pages were opened live in this session;
the one Wayback capture listed is of a page I opened live and captured from the same URL.

## Rows

| S640 | Jewish Women's Archive, Deborah Dash Moore and Dory Fox, 2021, "From the Archive: Amulet for the Protection of Pregnant Women and Newborn Children" — https://jwa.org/blog/fromthearchive/archive-amulet-protection-pregnant-women-and-newborn-children (direct, HTTP 200, 78059 bytes) | docs | B | birth amulets from Kerala used against infertility and infant death | body paragraph after the heading What we found: "This elaborately detailed amulet from Kerala, Kochi was used to guard against both infertility and infant death." | Birth amulets from Kerala guarded women against infertility and against the death of an infant. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S641 | Pitt Rivers Museum, University of Oxford, "Small Blessings: Horned Hand, Corsica", object 1985.52.2, transferred from the Wellcome Institute in 1985; undated web page — https://web.prm.ox.ac.uk/amulets/index.php/protection-2/ (direct, HTTP 200, 17704 bytes); capture https://web.archive.org/web/20230603205800id_/https://web.prm.ox.ac.uk/amulets/index.php/protection-2/ | docs | A | coral horned-hand amulets and the Evil Eye's victims | body paragraph, after the object's accession line: "horned hand amulets are thought to be of ancient Italian origin and are worn as protection against the harmful glance of the Evil Eye" | Horned-hand amulets were worn to turn the Evil Eye's gaze aside so that its harmful force missed the wearer. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

## Gate lines

- S640 — https://jwa.org/blog/fromthearchive/archive-amulet-protection-pregnant-women-and-newborn-children — accessed 2026-10-23 — body paragraph after the heading What we found: “This elaborately detailed amulet from Kerala, Kochi was used to guard against both infertility and infant death.”. Grounds: Birth amulets from Kerala guarded women against infertility and against the death of an infant. Seat: ScoutChildBirthProtection.
- S641 — https://web.prm.ox.ac.uk/amulets/index.php/protection-2/ — accessed 2026-10-23 — body paragraph, after the object's accession line: “horned hand amulets are thought to be of ancient Italian origin and are worn as protection against the harmful glance of the Evil Eye”. Grounds: Horned-hand amulets were worn to turn the Evil Eye's gaze aside so that its harmful force missed the wearer. Seat: ScoutChildBirthProtection.

## rowcheck output (verbatim)

```
$ cd /fast/scratch/hyaku/kotodama-r59/ScoutChildBirthProtection && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutChildBirthProtection/rows.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutChildBirthProtection/stub.md
S640 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://jwa.org/blog/fromthearchive/archive-amulet-protection-pregnant-women-and-newborn-children | BOILER: root-clear https://jwa.org/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'death', 'guard', 'infan', 'infer', 'keral'] | TOPIC: quote_hits=1 function_words=5 page_hits=14 page_terms=16 need=1/2/3/2
S641 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://web.prm.ox.ac.uk/amulets/index.php/protection-2/ | BOILER: root-clear https://web.prm.ox.ac.uk/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'evil', 'hand', 'harmf', 'horne', 'worn'] | TOPIC: quote_hits=1 function_words=7 page_hits=3 page_terms=7 need=1/2/3/2
```

## draft sentences

S640 (Jewish Women's Archive, Kerala birth amulet):

- A detailed amulet from Kerala, Kochi guarded a woman against infertility and against the death of an infant (S640).
- The same tradition wrote birth amulets on parchment with passages and names of angels, folded them small enough to carry, and tied them to a baby's crib or on a cord worn at the neck (S640).

S641 (Pitt Rivers Museum, coral horned hand from Corsica):

- A horned-hand amulet cut from coral at Ajaccio in Corsica was worn so that its bright surface would draw the Evil Eye's look away from the wearer (S641).
- The museum lists mother-of-pearl, silver, gold, amber and lava as alternative materials for the same horned-hand form, and names children and domestic animals as those most at risk (S641).
- Because the glance was blamed on excessive admiration or envy, any striking ornament could serve as the counter-charm (S641).

Design decisions these rows can carry in the entry: what the object is made of (vellum/parchment
and ink; coral and its substitutes mother-of-pearl, silver, gold, amber, lava), what danger it
answers (infertility, infant death, Lilith, the Evil Eye's glance blamed on envy and excessive
admiration), where it is worn or placed (cord at the neck, tied to a crib, folded to be carried;
worn on the body), who it protects (pregnant women, newborns, children, domestic animals), and who
makes it (a scribe writing Hebrew, Aramaic and Ladino; a carver of horned hands).

## rejected

Opened and not offered, with reason and verbatim tool output:

- https://www.brooklynmuseum.org/objects/4119 — Brooklyn Museum, "Amulet of a Birth God" (Taweret). Would have been the best Egyptian childbirth row, but the live page was throttled on both attempts and so was never opened; no capture may vouch for a page I could not open live (FETCH-59 / ordinary-means rule). Verbatim: `https://www.brooklynmuseum.org/objects/4119 429 34229` (second attempt identical: `429 34229`).
- https://www.metmuseum.org/toah/hd/tali/hd_tali.htm — Met Heilbrunn essay on amulets and talismans. Verbatim: `https://www.metmuseum.org/toah/hd/tali/hd_tali.htm 429 34217`. Rejected: never opened live.
- https://artuk.org/discover/artworks/portrait-of-a-child-with-a-coral-necklace-45321 — Art UK, "Portrait of a Child with a Coral Necklace" (Jan Claesz., 1636, Bowes Museum). Rejected: blocked. Verbatim: `https://artuk.org/discover/artworks/portrait-of-a-child-with-a-coral-necklace-45321 403 118`.
- https://wellcomecollection.org/articles/Yb8lqRAAACMAjGvH — Wellcome Collection article. Rejected: the host refuses plain GETs. Verbatim: `https://wellcomecollection.org/articles/Yb8lqRAAACMAjGvH 405 2131`.
- https://collection.sciencemuseumgroup.org.uk/search?q=amulet+child — Science Museum Group collection search. Rejected: blocked. Verbatim: `https://collection.sciencemuseumgroup.org.uk/search?q=amulet+child 403 919`.
- https://palmuseum.org/en/collections/collections/coral-necklace-0 — "Coral necklace" record (Red Sea coral, amber and beads). Rejected: redirects away from the record. Verbatim: `https://palmuseum.org/en/collections/collections/coral-necklace-0 307 1331`.
- https://collections.vam.ac.uk/item/O383260/amulet-unknown/ — V&A, group of six amulets on a ring (Bavaria, 1750–1799; silver, enamel, onyx, horn, shell, coral). Opened, HTTP 200, 50555 bytes; its curatorial sentence "Although the Catholic Church was opposed to the pagan nature of many amulets, it was powerless to prevent their use." passes the mechanical legs (page_hits=16, page_terms=17). Rejected on assignment scope, not mechanics: the passing quote teaches religious reform and the survival of amulet use, not the protection of mothers and infants, and my two-row budget went to the two child-focused rows. Worth a row in a later round on the reform/continuity design decision; the page is live and stable.
- https://web.prm.ox.ac.uk/amulets/index.php/protection/index.html — Pitt Rivers "Small Blessings: Luck and Protection" section landing page (HTTP 200, 15422 bytes; page_hits=4, page_terms=4). Rejected: a one-paragraph gallery introduction ("Worn on the body or placed at home with other treasured possessions...") without an object-level claim; the object page S641 carries the same site's curatorial detail.
- https://www.prm.ox.ac.uk/collections-online — Pitt Rivers Collections Online (HTTP 200, 153552 bytes). Rejected: a search interface; no object text served at the URL.
- https://www.sciencemuseumgroup.org.uk/ — Science Museum Group homepage (HTTP 200, 56869 bytes). Rejected: no object record; opened only as a host probe.

Not offered for the same reason, though opened: the roots https://jwa.org/ and https://web.prm.ox.ac.uk/
were fetched only as BOILER controls for the two rows.

## notes, confidence, unknowns

- Both quotes are body prose in the page markup, checked in the raw HTML: S640 sits in a `<p>`
  under a bold "What we found" sub-heading; S641 sits in a body `<div>` after the object's
  accession line, not in a caption, heading, list item or table cell.
- S640 has no Wayback snapshot (the availability API returned `"archived_snapshots": {}`), so the
  row lists the live URL only. The host answered 200 on every request this session.
- S641's capture `20230603205800` is of the exact live URL and serves the same 17704 bytes; the
  quote locates in the capture as well, so a live failure at acceptance falls back cleanly.
- S641's page carries exactly the minimum three CHARM-GUARD windows; the quote itself carries one
  (the word "amulets" is both a CHARM and a GUARD stem). It is a live, stable project site, but it
  is the thinnest of the two rows.
- S640 is tier B (archive blog essay by two named historians, illustrated with a Posen Library
  object); S641 is tier A (University of Oxford museum record). Neither URL nor quote is shared
  with any earlier SOURCES row, and neither host appears in corpus/SOURCES.md.
- No source opened here covers bells or cradle charms outside Jewish practice, and no source
  covers red thread that also serves a child-protection point without a throttled host; those
  remain open for other seats.
- No installs or updates were made; nothing was left running.
