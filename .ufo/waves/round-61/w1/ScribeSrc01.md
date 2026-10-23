# Round 61 W1 — ScribeSrc01 source findings

## Axes and outcome

- **Coverage:** drafted three opened source rows and one entry bullet per kept source across the two assigned footwear topics. Areni-1 has one kept source; Fort Rock sandals have two.
- **Operability:** no lint-tool or counter work in this source seat.
- All three kept sources were fetched live through ordinary GETs and each final quote was located by the round-61 locator. No access challenge was met or routed around; no capture is needed for a kept source.
- Proposed IDs are S652–S654. The source registry did not contain these IDs or the kept URLs when checked. Draft rows and bullets below are report-only; no product file was changed.

## Subtopic 1 — Areni-1 cave leather shoe

### Draft SOURCES row

| S652 | First Direct Evidence of Chalcolithic Footwear from the Near Eastern Highlands, Ron Pinhasi et al., PLOS ONE (2010) — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010984 | paper | A | Areni-1 leather shoe stuffing and grass material | Abstract "The shoe was stuffed with loose, unfastened grass (Poaceae) without clear orientation." | The shoe was stuffed with loose, unfastened grass without clear orientation. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

### Draft entry bullet

- The shoe was stuffed with loose grass without clear orientation. (S652)

### Gate line

- S652 | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010984 | 2026-10-23 | "The shoe was stuffed with loose, unfastened grass (Poaceae) without clear orientation."

### Locator evidence

Final quote command and full output:

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010984' 'The shoe was stuffed with loose, unfastened grass (Poaceae) without clear orientation.'; echo exit=$?
LOCATED https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010984
exit=0
```

An earlier quote from the same open-access paper's introduction did not locate and was dropped; this is not the Gate quote:

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010984' 'In 2008, a leather shoe (3,653–3,627 cal. BC) was discovered at Areni-1 Cave, Vayots Dzor province, Armenia.'; echo exit=$?
NOT_LOCATED https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010984 quote-absent
exit=1
```

The successful quote is from the abstract and includes the footwear term “shoe.” PLOS ONE identifies the 2010 article as open access and peer reviewed. The row is scoped to the original paper's Areni-1 shoe description, not a broader claim about all footwear.

## Subtopic 2 — Fort Rock sagebrush-bark sandals

### Draft SOURCES rows

| S653 | Great Basin Sandals, Museum of Natural and Cultural History, University of Oregon — https://mnch.uoregon.edu/collections-galleries/great-basin-sandals | docs | A | Museum gallery description of Great Basin sandal materials | Gallery body "well-preserved sandals woven from sagebrush bark and other fibers" | Sandals are woven from sagebrush bark and other fibers. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |
| S654 | Fort Rock Sandals, Thomas J. Connolly, Oregon Encyclopedia, Portland State University and Oregon Historical Society (published 2014-04-30; updated 2025-10-02) — https://www.oregonencyclopedia.org/articles/fort_rock_sandals/ | docs | B | Fort Rock sandal tie construction at the sole and heel | Tie-system paragraph "The tie system involves a series of interlocking loops fixed to the edge of the sole near the heel." | Fort Rock sandal tie systems use interlocking loops fixed to the sole edge near the heel. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/footwear-codes-terminology.md |

### Draft entry bullets

- Sandals were woven from sagebrush bark and other fibers. (S653)
- Interlocking loops at the sole edge near the heel formed the tie system. (S654)

### Gate lines

- S653 | https://mnch.uoregon.edu/collections-galleries/great-basin-sandals | 2026-10-23 | "well-preserved sandals woven from sagebrush bark and other fibers"
- S654 | https://www.oregonencyclopedia.org/articles/fort_rock_sandals/ | 2026-10-23 | "The tie system involves a series of interlocking loops fixed to the edge of the sole near the heel."

### Locator evidence

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://mnch.uoregon.edu/collections-galleries/great-basin-sandals' 'well-preserved sandals woven from sagebrush bark and other fibers'; echo exit=$?
LOCATED https://mnch.uoregon.edu/collections-galleries/great-basin-sandals
exit=0
```

```text
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py 'https://www.oregonencyclopedia.org/articles/fort_rock_sandals/' 'The tie system involves a series of interlocking loops fixed to the edge of the sole near the heel.'; echo exit=$?
LOCATED https://www.oregonencyclopedia.org/articles/fort_rock_sandals/
exit=0
```

The MNCH gallery is the museum's own collection page; its body describes sagebrush-bark sandals and its image captions identify Fort Rock sandal specimens. The Oregon Encyclopedia entry is by Thomas J. Connolly and gives tie construction detail. Both final quotes contain footwear-lexicon terms (“sandals” and “sole”).

## Registry checks

URL host+path checks against `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md` used `functions.grep`; each returned the literal output shown:

```text
pattern: journals\.plos\.org/plosone/article\?id=10\.1371/journal\.pone\.0010984
No matches found
pattern: mnch\.uoregon\.edu/collections-galleries/great-basin-sandals
No matches found
pattern: oregonencyclopedia\.org/articles/fort_rock_sandals
No matches found
pattern: S65[234]
No matches found
```

## Leads, limits, gates, and touched surfaces

- A University of Oregon exhibit page was also opened as a candidate; `read` showed “archaeologist Luther Cressman uncovered 10,000-year-old sagebrush bark sandals.” Its live locator returned `LOCATED https://mnch.uoregon.edu/exhibits/oregon-where-past-present` (exit 0). It was not kept because the MNCH Great Basin collection gallery is the more directly scoped collection source and the Oregon Encyclopedia adds independent construction detail.
- Other exploratory URLs for Smithsonian Magazine, University College Cork, The Guardian, BBC, NPR, and Live Science returned HTTP 404 and were not kept. The Smithsonian Wayback availability request returned `archived_snapshots: {}`. A plain Bing RSS request returned an unrelated WhatsApp Web item; it was ignored. No bot challenge, paywall, or login was encountered on any kept source.
- Only one locatable source was kept for Areni-1 despite the two-source aim. It is the original open-access research paper; the attempted alternate outlet links did not yield an accessible source. The other topic has two kept sources.
- The entry and source rows are drafts only; this seat did not append `SOURCES.md`, create the knowledge entry, edit `corpus/README.md`, or run ACCEPT-C/ACCEPT-O. No claim-wide PASS is asserted. Claim C still requires the complete 20+ row entry and all frozen legs.
- No packages were installed. No code, tests, counters, or other product files were changed. The only file written by this seat is this scoped report.

**Artifact:** `/home/vgpnk/Projects/shokunin/.ufo/waves/round-61/w1/ScribeSrc01.md`