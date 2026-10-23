# ScoutMedievalCharms — claim C source seat (S618, S619)

Round 59, BUILD wave, claim C (coverage): subtopic *medieval European textual charms and amulets
— written charms, birth girdles, Anglo-Saxon charm texts, saints' names as protection*.
Both assigned ids used: S618, S619. No delegation, no background jobs, no installs (nothing needed;
`curl`, `python3` and the frozen instruments sufficed). All scratch work under
`/fast/scratch/hyaku/kotodama-r59/ScoutMedievalCharms/`.

Aim: two rows that each answer a design question a worldbuilder actually asks — what the object is
made of, who makes or lends it, where it is worn or placed, what danger it answers, and how words
themselves become the protection.

## Rows (11 cells each, for corpus/SOURCES.md)

```
| S618 | University of Cambridge, 2021 (research news published 10 March 2021), ‘Medieval birthing girdle parchment was worn during labour, study suggests’, University of Cambridge website — https://www.cam.ac.uk/research/news/medieval-birthing-girdle-parchment-was-worn-during-labour-study-suggests (direct plain GET, HTTP 200, 142,514 bytes); capture https://web.archive.org/web/20260906032215id_/https://www.cam.ac.uk/research/news/medieval-birthing-girdle-parchment-was-worn-during-labour-study-suggests | docs | B | how English birth girdles were made, lent out and suppressed as a class of protective text | article body, paragraph beginning ‘Made from materials such as silk, paper and parchment’: "inscribed with prayers and invocations for safe delivery, birthing girdles were one of the most common spiritual charms loaned out by monasteries to their parishioners" | Parchment or silk girdles carried prayers for safe delivery as spiritual charms that monasteries loaned to parishioners, so the lending house decided who could borrow a protective text. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S619 | Grendon, Felix. 1909. The Anglo-Saxon Charms. New York, offprint from the Journal of American Folklore 22 (1909); copy digitised by the University of Toronto (PIMS), Internet Archive item anglosaxoncharms00gren, plain text of the scan — https://archive.org/download/anglosaxoncharms00gren/anglosaxoncharms00gren_djvu.txt (direct plain GET, HTTP 200, 394,072 bytes) | book | B | Anglo-Saxon charm recipes as instructions for amulets of writing, herb and stone, and where each was placed | section D (Amulet Charms), second paragraph, p. 135 of the scan: "In five of the printed D charms, the amulet consists of a writing containing mysterious words, letters, and other symbols" | Anglo-Saxon charm recipes treat a written formula of mysterious words and letters as the amulet itself, so the copied text, not a herb or a stone, carries the protection. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
```

## Gate lines

- S618 — https://www.cam.ac.uk/research/news/medieval-birthing-girdle-parchment-was-worn-during-labour-study-suggests — accessed 2026-10-23 — article body, paragraph beginning ‘Made from materials such as silk, paper and parchment’: “inscribed with prayers and invocations for safe delivery, birthing girdles were one of the most common spiritual charms loaned out by monasteries to their parishioners”. Grounds: Parchment or silk girdles carried prayers for safe delivery as spiritual charms that monasteries loaned to parishioners, so the lending house decided who could borrow a protective text. Seat: ScoutMedievalCharms.
- S619 — https://archive.org/download/anglosaxoncharms00gren/anglosaxoncharms00gren_djvu.txt — accessed 2026-10-23 — section D (Amulet Charms), second paragraph, p. 135 of the scan: “In five of the printed D charms, the amulet consists of a writing containing mysterious words, letters, and other symbols”. Grounds: Anglo-Saxon charm recipes treat a written formula of mysterious words and letters as the amulet itself, so the copied text, not a herb or a stone, carries the protection. Seat: ScoutMedievalCharms.

## Frozen checker output (verbatim)

```
$ cd /fast/scratch/hyaku/kotodama-r59/ScoutMedievalCharms && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutMedievalCharms/rows.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutMedievalCharms/stub.md
S618 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.cam.ac.uk/research/news/medieval-birthing-girdle-parchment-was-worn-during-labour-study-suggests | BOILER: root-clear https://www.cam.ac.uk/; not a title, h1 or meta label | RELEVANCE: shared=['charm', 'deliv', 'girdl', 'loane', 'monas', 'paris'] | TOPIC: quote_hits=1 function_words=9 page_hits=4 page_terms=3 need=1/2/3/2
S619 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://archive.org/download/anglosaxoncharms00gren/anglosaxoncharms00gren_djvu.txt | BOILER: root-clear https://archive.org/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'charm', 'lette', 'myste', 'word'] | TOPIC: quote_hits=2 function_words=5 page_hits=126 page_terms=493 need=1/2/3/2
EXIT 0
```

A near-identical earlier run (before the two extra draft sentences were added) also exited 0; the
rows themselves were not changed after the first pass. Duplicate check:
`grep -nF -e 'anglosaxoncharms00gren' -e 'cam.ac.uk/research/news/medieval-birthing' corpus/SOURCES.md`
returned no lines — neither URL is already in the registry.

## Draft sentences (entry side, 3–4 per row)

S618:

1. A birth girdle is a long narrow parchment or silk roll, inscribed with prayers and worn wrapped around the body, so its material and its format are part of the charm (S618).
2. Monasteries owned these girdles and loaned them to parishioners, so the religious house that held a protective text also decided who could borrow it (S618).
3. Talismanic girdles were destroyed at the Dissolution of the Monasteries, yet women used them secretly into the early seventeenth century, so a ban on a protective object can drive it underground rather than end it (S618).
4. The girdle prayers name saints tied to women and childbirth, so a protective text can work by listing holy names rather than by asking for one single outcome (S618).

S619:

1. In the Anglo-Saxon charm texts an amulet can be a writing, a slip carrying mysterious words, letters and symbols rather than a herb or a stone (S619).
2. Charm recipes prescribe where the writing goes, at the neck, on the left breast, in the left shoe, under the heel or under the right foot, so placement is a step of the recipe (S619).
3. Where the written formula is itself the amulet, the recipe needs only parchment or wax to write on, so copying the words is the act that makes the protection (S619).
4. The same corpus sets herbs and stones carried on the person beside writings tucked into a shoe, so a tradition can offer several carriers for one danger (S619).

Each sentence is carried either by its row's quote or by body text of the opened page
(S618: silk/paper/parchment materials, long-and-narrow format, wearing like a belt, Dissolution
1536, ban by bishops and use into the early seventeenth century, prayers referencing saints tied to
women and childbirth. S619: parchment and wax as the named writing surfaces, herbs/stones/writings
as the three carriers, the placement list at neck, left breast, left shoe, heel, right foot, and
the D-11 farm/shield/evil-spirits recipe).

## Rejected / opened but not offered

- https://wellcomecollection.org/stories/protecting-body-and-soul-in-medieval-childbirth — HTTP 405 to an ordinary desktop-UA GET (twice) and to a bare `curl` UA; the page is the ideal curatorial essay on MS.632 but the host refuses the request. Verbatim: `HTTP 405 2131` (both attempts; saved 2,131-byte error body).
- https://journal.oraltradition.org/wp-content/uploads/files/articles/14ii/14_2_complete.pdf (Olsan 1999, *The Inscription of Charms in Anglo-Saxon Manuscripts*, open-access journal PDF) — no connection from this host. Verbatim: `curl: (28) Failed to connect to journal.oraltradition.org:443 after 134043 ms: Could not connect to server` / `HTTP 000 0`.
- https://www.bl.uk/collection-items/the-lacnunga — redirects away from the item page to the site home; the served page is not the charm page. Verbatim: `HTTP 200 231063 https://www.bl.uk/stories`.
- https://blogs.bl.uk/digitisedmanuscripts/2011/10/the-lacnunga.html — the blog moved; the redirect target is a 404. Verbatim: `HTTP 404 391 https://blogs-archive.bl.uk/digitisedmanuscripts/2011/10/the-lacnunga.html`.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12818004/ — opened, HTTP 200, 197,144 bytes: Taylor, Heather A. 2025, “‘An experiment pervyd for a thynge y lost’: ‘Non-medical’ Charms and experimenta in Medieval Medical Manuscripts”, *Social History of Medicine* 38(4), `DOI 10.1093/shm/hkae053`, PMC full text. Not offered as a row because its only 10–25-word full sentences that carry a charm window are narrow — “British Library, Additional MS 33996, for example, explains how to make an amulet to wear on the body during intercourse.” and “The instructions suggest that the efficacy of the amulet can be tested by suspending it on a tree to make it bear fruit.” — while its strongest design sentence on the childbirth textual amulet runs 34 words and cannot be quoted whole. Held as the spare for S619 if acceptance judges a scanned OCR text too fragile.
- https://kar.kent.ac.uk/54689/ — opened, HTTP 200, 28,993 bytes: Arthur, Ciaran 2016 PhD thesis, *The Liturgy of ‘Charms’ in Anglo-Saxon England*. Not offered: the abstract is about the definition of *galdor* and the manuscript context of liturgy, not about a protective object's material, making or placement, and contains no 10–25-word sentence carrying a charm-protection point.

Unopened leads (not counted as sources, recorded so the L1 does not re-walk them):
the Cambridge repository PDF of the proteomic study behind S618, and Wellcome MS.632 object pages —
both reachable in principle, neither opened in this session.

## Risk notes for the L1 / acceptance

- S618's quote is 25 words (the wave ceiling) and begins mid-sentence after a comma; it is running
  prose, not a heading or list item, and it is the only span on that page inside the word band that
  carries a CHARM–GUARD window. If a reviewer objects to a subordinate clause, drop to the 19-word
  clause “birthing girdles were one of the most common spiritual charms loaned out by monasteries to
  their parishioners”, which also locates and keeps RELEVANCE, or swap S618 for the Taylor 2025 PMC
  row above.
- S618's listed Wayback capture is a genuine capture of the same page but the archive serves it
  gzip-encoded (verified: `file` reports “gzip compressed data”; decompressed to 141,347 bytes it
  contains the quoted sentence). The checker's plain fetch would read the compressed bytes, so the
  row's LOCATE rests on the live URL; listing the capture cannot hurt but cannot rescue a live
  failure either.
- S619 has no Wayback capture of the `.txt` (availability API returned `{"archived_snapshots": {}}`
  and the CDX prefix query `[]`), so the archive.org download is its only URL and its FETCH-59 risk
  is that single host. It answered 200 in 3.5 s here. The quote crosses an OCR line-end hyphen
  (`con-` at end of line, `taining` next), which the locator joins; the same hyphen join is what the
  acceptance run will rely on.
