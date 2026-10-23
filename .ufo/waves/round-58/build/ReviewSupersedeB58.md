# ReviewSupersedeB58 — round 58 records: superseding rows S428, S433, S438

Seat: ReviewSupersedeB58 (reviewer, leaf). Axis: calibration. Ids assigned: S563, S564, S565.
Sources re-opened 2026-10-23 by plain `curl` GETs (desktop UA, `-L`), and every anchor
re-tested with the frozen instrument
`python3 -B reports/round-58/reopen-quote.py '<url>' '<quote>'`. Served sizes equal the
rows' recorded sizes. Nothing written except this report. No installs.

## Verdicts on the routed findings

### S428 — **DISAGREE** (finding is false; no superseding row owed — S563 not used)

Routed defect (round-57-verifier-spotcheck.md §5 item 4; lessons/round-57.md:119,133):
"anchor quotes 1 and 4 split by OCR hyphenation, do not locate" — the reviewer's note says
"garments" ≠ "gar ments" → MISS.

The frozen instrument's docstring and `locate()` join a hyphen (or not-sign) at a line end
before matching: `fidal-\nlgos` → `fidallgos`. The served OCR's `gar-`/`ments` and
`distinfraish-`/`ing` therefore match; the reviewer apparently normalised the hyphen away
to a space without the join. Empirical result, all four anchors, live today:

```
== q1 ==
LOCATED https://archive.org/download/transactionsasi26japagoog/transactionsasi26japagoog_djvu.txt
== q4 ==
LOCATED https://archive.org/download/transactionsasi26japagoog/transactionsasi26japagoog_djvu.txt
== q2 ==
LOCATED https://archive.org/download/transactionsasi26japagoog/transactionsasi26japagoog_djvu.txt
== q3 ==
LOCATED https://archive.org/download/transactionsasi26japagoog/transactionsasi26japagoog_djvu.txt
== alt-q4 ==
LOCATED https://archive.org/download/transactionsasi26japagoog/transactionsasi26japagoog_djvu.txt
```

(q1 = `they took their origin … at Kiy6to`; q4 = `the only place where the
distinfraishing mark … breast plate`; q2 = `The embroidered patterns alluded to were
generally circular`; q3 = `No snch thing as a coat-of-arms proper … in the country`;
alt-q4 = the reviewer's suggested `crests and badges are the only Heraldic insignia here
known` — it also locates, but is not needed.)

Consistent with the landing's "40/42" receipt: the two non-locating rows that day were
other rows (S452 was a Wayback HTTPError; the reviewer "evidently" guessed S428 — the
guess was wrong). Note the reviewer's proposed fix, `distinfraish-ing`, also locates (it
matches the unjoined text), so both forms are acceptable to the instrument; neither cell
needs correction.

Exact fix: **none**. The four quotes are verbatim-as-served; scope, teaches, status and
used-by check out (scope cell is complete at 949 chars; teaches is carried by the page;
the row is cited at heraldry-emblems-identity-marks.md:61,82,135 so `mined` is right).
Residual noted by the reviewer — "page 4"/"page 2" labels unverifiable against a
flat djvu stream — remains a gap, not a defect; a future superseding row MAY relabel
locators to `served text:` but nothing obliges it. The debt line for S428 in
lessons/round-57.md:133 is discharged by this verdict; the records erratum should
record that the premise was falsified by the instrument itself.

### S433 — **AGREE** (locator label false; superseding row S564 below)

The served page (`en.maiask.ru/data/documents/13_YatsenkoRogozhinskiiENG.htm`, HTTP 200,
18,744 bytes — equal to the row) never prints the word `abstract` (case-insensitive count:
0). The row's own access note says it is "the publisher's per-article record page". Both
anchor quotes locate verbatim:

```
== q1 ==
LOCATED https://en.maiask.ru/data/documents/13_YatsenkoRogozhinskiiENG.htm
== q2 ==
LOCATED https://en.maiask.ru/data/documents/13_YatsenkoRogozhinskiiENG.htm
```

(q1 = `In the Tagar Great Salbyk Barrow tamgas of late time, similar to Sarmatian ones,
were depicted in narrow stripes along the edges.`; q2 = `The single important finds with
tamgas associated with Olbia and Panticapaeum are analyzed also.`)

Exact fix: superseding row with locator `record page:` (both quotes), all other content
cells unchanged, status `mined` (the superseded row is cited at entry :100; used-by
inherited). Companion records item for the integrator: entry :100 reads "(S433, abstract
page)" — same false label in the prose; fix to "(S433, record page)" or drop the label.
(Entry :100's "(S434, abstract)" is fine — that PDF prints an abstract.)

### S438 — **AGREE** (teaches drops the source's hedge; superseding row S565 below)

The served page (`ag.colorado.gov/brands/about-brands`, HTTP 200, 91,391 bytes — equal to
the row) prints `Formed by Colorado’s livestock industry in approximately 1865, when
Colorado was still a territory`; the string `since 1865` occurs nowhere on the page (the
only `since`-adjacent text is `Became a state agency in 1903`). The teaches cell's
"recorded brands since 1865" drops the hedge. All four anchor quotes locate verbatim:

```
== Formed by Colorado’s livestock industry in approximately 1865, when Colorado was still a territory
LOCATED https://ag.colorado.gov/brands/about-brands
== Research, record and administer Colorado’s approximately 30,000 registered livestock brands
LOCATED https://ag.colorado.gov/brands/about-brands
== Inspect livestock and verify ownership before (i) any change of ownership, whether by sale or gift, (ii) transport over 75 miles within Colorado
LOCATED https://ag.colorado.gov/brands/about-brands
== The Brand Board and Brand Inspection Division are 100% cash funded by fees and assessments paid by Colorado’s livestock industries
LOCATED https://ag.colorado.gov/brands/about-brands
```

Exact fix: superseding row; teaches opens `supersedes S438 — ` and re-hedges to
"approximately 1865"; scope cell hedged the same way (`(approximately 1865, still a
territory)`); status `mined`, used-by inherited (cited at entry :58 and :125). Entry
checks: :58 already hedges ("about 1865") — fine; :125's table cell "1865 to now" is
unhedged — optional one-word fix "about 1865 to now" for the integrator.

## Rows

Format: 11 cells; `teaches` opens `supersedes S### — `; status `mined` because each
superseded row is cited by the same entry; opened 2026-10-23, recheck 2027-10-23.

| S563 | — | not used: the routed S428 defect ("quotes do not locate") is falsified by the frozen instrument; see verdict above | — | — | — | — | — | — | — | — |

| S564 | S. A. Yatsenko & A. E. Rogozhinskii, 2021, "Some Notes on the Tamga-Signs of Sarmatians and Their Neighbours", Materials in Archaeology and History of Ancient and Medieval Black Sea Region (MAIASP) no. 13, pp. 733–767, DOI 10.53737/2713-2021.2021.56.17.023. — https://en.maiask.ru/data/documents/13_YatsenkoRogozhinskiiENG.htm (direct, HTTP 200 (content-type text/html, 18744 bytes again on re-open 2026-10-23; the publisher's per-article record page)) | paper | A | Sarmatian tamgas as inherited group marks; where they appear (Central Asian prototype mirrors-pendants, Great Salbyk Barrow stone stripes, Bayte III temple walls, a Minguriuk stele, Roman officers' harness and belts, single finds at Olbia and Panticapaeum); mark choice tracking trade; outsider adoption as "Sarmatian fashion" | record page: "In the Tagar Great Salbyk Barrow tamgas of late time, similar to Sarmatian ones, were depicted in narrow stripes along the edges."; record page: "The single important finds with tamgas associated with Olbia and Panticapaeum are analyzed also." | supersedes S433 — Sarmatian tamgas were group marks applied to temple walls, barrow stones, stelae, Roman cavalry gear and Greek-city finds, tracing trade and borrowed fashion across the steppe. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md |

| S565 | Colorado Department of Agriculture, Brand Board / Brand Inspection Division. "About Brands." Denver, CO: ag.colorado.gov (state agency page). Accessed 2026-10-22; re-opened 2026-10-23 (HTTP 200, 91,391 bytes again); stable id: https://ag.colorado.gov/brands/about-brands — https://ag.colorado.gov/brands/about-brands (direct, HTTP 200 (curl, plain GET)) | docs | A | origin of Colorado's Brand Board (approximately 1865, still a territory); the division records and administers ~30,000 registered livestock brands; inspection triggers (change of ownership, transport over 75 miles, out-of-state); fee funding; theft deterrence and ownership evidence | served text: "Formed by Colorado’s livestock industry in approximately 1865, when Colorado was still a territory"; served text: "Research, record and administer Colorado’s approximately 30,000 registered livestock brands"; served text: "Inspect livestock and verify ownership before (i) any change of ownership, whether by sale or gift, (ii) transport over 75 miles within Colorado"; served text: "The Brand Board and Brand Inspection Division are 100% cash funded by fees and assessments paid by Colorado’s livestock industries" | supersedes S438 — Colorado's Brand Board has recorded brands since approximately 1865 and verifies ownership by inspection around movement and sale. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md |

## Gate lines

- S564 — https://en.maiask.ru/data/documents/13_YatsenkoRogozhinskiiENG.htm — accessed 2026-10-23 — record page: “In the Tagar Great Salbyk Barrow tamgas of late time, similar to Sarmatian ones, were depicted in narrow stripes along the edges.”. Grounds: supersedes S433 — Sarmatian tamgas were group marks applied to temple walls, barrow stones, stelae, Roman cavalry gear and Greek-city finds, tracing trade and borrowed fashion across the steppe. Seat: ReviewSupersedeB58.
- S565 — https://ag.colorado.gov/brands/about-brands — accessed 2026-10-23 — served text: “Formed by Colorado’s livestock industry in approximately 1865, when Colorado was still a territory”. Grounds: supersedes S438 — Colorado's Brand Board has recorded brands since approximately 1865 and verifies ownership by inspection around movement and sale. Seat: ReviewSupersedeB58.

## draft sentences

S564 (re-point of entry :100):
- In the Great Salbyk barrow, late Sarmatian-like tamgas run "in narrow stripes along the edges" (S564).
- The record page also notes single finds with tamgas at Olbia and Panticapaeum (S564).

S565 (entry :58 already hedges; :125 optional):
- Colorado administers about 30,000 brands through a board its livestock industry formed about 1865 (S565).
- The Brand Board and Brand Inspection Division are funded entirely by fees paid by Colorado's livestock industries (S565).

## rejected

None beyond the verdicts: every source named in my assignment was opened and is
accounted for above (S428 re-opened and cleared; no replacement source needed).

## residual risk / notes for the integrator

- S428's "page 4"/"page 2" locators remain unverifiable on a flat OCR stream (gap, not defect).
- The round-57 reopen seat's scratch normaliser lacked the instrument's line-end hyphen
  join; any further hand-normalisation should be done by `reopen-quote.py` itself.
- If the integrator prefers `queued` for superseding rows (the S481-S491 precedent files
  them `queued`/`—` used-by), that precedent conflicts with this dispatch's explicit rule
  ("`mined` with the same used-by when the superseded row is cited"); I follow the dispatch.
- Sibling seats own S421, S413, S417, S440, S445, S452, S453 (ids S560-S562, S566+);
  no overlap.

installs: none.
