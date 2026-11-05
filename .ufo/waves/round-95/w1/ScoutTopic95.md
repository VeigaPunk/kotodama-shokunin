# ScoutTopic95 — round-95 claim C source staging (funerary lament / dirge)

Seat: ScoutTopic95. Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin.
Date: 2026-11-05. Base: 19aa4dd03dfd37b435d0b8ea5b313635d9d51592.
Stage: `.ufo/waves/round-95/w1/stage/ScoutTopic95/` (rows.md + evidence/).
Scratch: `/fast/scratch/hyaku/kotodama-r95/ScoutTopic95/` (deleted before yield).

## What I did

Read-only gap sweep of the corpus for a filename and prose owner of the funerary
lament/dirge **sung speech register**; then a source hunt across DOAJ, Crossref and
OpenAlex plus two folklore.ee site sweeps; then direct plain-`curl` fetches of every
shortlisted candidate at its publisher/OJS URL; then text extraction and single-occurrence
quote verification; then staged all captures with hashes and wrote the proposed rows.

**No production file was written.** The corpus, tools/, reports/ and every other path were
read-only for this seat. All writes are inside my stage dir plus this Report trailer.

## Gap sweep — measured, not assumed

Filename sweep over the whole corpus (rc 0):

```
find corpus -name "*lament*" -o -name "*dirge*" -o -name "*keen*" -o -name "*moirolog*" -o -name "*funerary*" | sort
-> corpus/knowledge/culture-material/funerary-material-culture.md
```

Prose sweep of the linguistics partition (rc 0):

```
grep -cniE "\b(dirge|keening|keener|eulog)" corpus/knowledge/linguistics/*.md   -> no file matches
grep -cniE "\blament" corpus/knowledge/linguistics/*.md                          -> 1 match (orality-formulaic-language.md)
```

So inside the linguistics partition the words *dirge*, *keening*, *keener* and *eulogy*
occur **nowhere**; *lament* occurs **once**, as a type-scene card in the epic inventory
(`corpus/knowledge/linguistics/orality-formulaic-language.md:66`). Across the whole corpus
*lament* appears only in eight non-linguistics files, each as a one-line scene reference.
The surface is unowned, as the frozen claim assumes.

### The three closest existing entries (for the entry's positioning)

1. `corpus/knowledge/linguistics/orality-formulaic-language.md` — owns lament as a
   type-scene card (`lullaby`/epic composition machinery). The new entry specialises that
   one card into a speech register and must not re-teach Parry–Lord.
2. `corpus/knowledge/linguistics/lullaby-child-song-formulae.md` — owns the sung register
   as a distinct modality (Kanak *parler* vs *chanter*, vocable chorus, sung-vs-spoken
   rhyme versions, refrain/apostrophe). The new entry borrows that framing for an adult
   funeral register; it must not re-teach lullaby form or child-song transmission.
3. `corpus/knowledge/culture-material/funerary-material-culture.md` — owns the death
   register and mourning economy (WORD layer with Roman office terms including
   *praefica*; the *dirge*/*requiem*/*elegy* etymology chain at `:37` and `:139`). The new
   entry owns the sung utterance itself and couples to that file.

Registry state at base (rc 0): `grep -cE '^\| S[0-9]+ ' corpus/SOURCES.md` -> **893** rows;
highest id **S969**. The frozen claim's "893 rows, highest S969" is confirmed.

## Source hunt — measured

27 query operations (25 API + 2 site), all on 2026-11-05, all by ordinary means (plain
`curl`/HTTPS, default UA, `-L`, `--max-time 30`; no browser, no challenge passed, no
login, no paywall, no TLS bypass).

| where | queries | API-reported identified | records returned & screened |
|---|---|---|---|
| DOAJ | 12 | 49 (sum of per-query totals) | 42 |
| Crossref | 5 | 1,850,342 (sum; 1 query HTTP 429) | 60 |
| OpenAlex | 8 | 14,451 | 161 |
| folklore.ee | 2 | 12 volumes/hits | 2 |
| **total** | **27** | — | **265 records screened** |

**12 candidates included** (11 tier A, 1 tier C); **253 excluded** at screening, each with a
recorded reason (topic / access-with-observed-status / scope — never title-only). A candidate
returned by several queries is counted once in the included set; the per-query inclusion
counts sum to 20 query-candidate hits.

All twelve fetches returned **HTTP 200**. Two MDPI candidates needed the publisher's own
asset host `mdpi-res.com` because `mdpi.com` returns **403**; both are recorded as
access exclusions at the `mdpi.com` route and as inclusions at the `mdpi-res.com` route.

### Rows proposed

| id | source | tier | facet(s) grounded |
|---|---|---|---|
| S970 | Pärtlas 2025, *Journal of Ethnology and Folkloristics* 19(1) — Seto solo and choral funeral laments | A | antiphonal lament; speech-vs-song boundary |
| S971 | Rosenberg 2004, *Current Musicology* 78 — Corsican women's lament as cultural work | A | antiphonal lament; gendered mourning rules |
| S972 | McLaughlin 2019, *Religions* 10(4):235 — Keening the Dead | A | professional keeners; speech-vs-song |
| S973 | Williams & Ó Laoire 2024, *Religions* 15(7):879 — The Keening Woman | A | professional keeners; gendered mourning rules |
| S974 | Mzhavanadze & Scherbaum 2021, *Musicologist* 5(2) — Svan Funeral Dirges (Zär) | A | lament refrain; praise of the dead |
| S975 | Avdikos 2026, *Folklore* EJF 99 — Lament Songs Glorifying Greek Soldiers | A | praise of the dead (heroic kleos mode) |
| S976 | Katsanevaki 2017, *Musicologist* 1(1) — Modern Laments in Northwestern Greece | A | professional keeners; gendered mourning rules |
| S977 | Hytönen-Ng & Kallonen 2024, *Journal of Somaesthetics* 9(1) — Weeping out Loud | A | gendered mourning rules; speech-vs-song |
| S978 | Stepanova 2011, *Acta Baltica* 15(1) — Karelian and Lithuanian Laments | A | gendered mourning rules; formulaic grief content |
| S979 | Ermakov 2014, *Folklore* EJF 60 News in Brief — Erzya Lamentations | **C (lead only)** | professional keeners (weakly) |
| S980 | Koski 2005, *ELORE* 12(1) — Suhde vainajaan inkeriläisissä kuolinitkuissa | A | address to the dead; formulaic grief content |
| S981 | Alembi 2008, *Folklore* EJF 38 — The Abanyole Dirge | A | professional keeners (non-European); praise of the dead; gendered mourning rules |

The claim requires >= 3 qualifying rows above S969; **11 tier-A rows** are proposed.

## Quote verification

All **24** quotes verified with `bytes.count(quote) == 1` against the staged text capture,
each **<= 25 words** (word counts 4–12). Re-verification command (rc 0) is recorded in
rows.md §2 and reproduces 24/24 ok, 0 bad. Captures are staged as
`evidence/S970.pdf` + `evidence/S970.txt` … `evidence/S981.pdf` + `evidence/S981.txt`;
text renders are `pdftotext` (poppler, default layout) of the served PDF.

Manifest re-check (rc 0): all 12 rows match on PDF bytes, text bytes, PDF sha256, text
sha256 and HTTP status 200.

## Two corrections I made to my own work

1. My first search-log table reported "identified" as the returned page size. Re-parsed
   from the saved API JSON, the real API-reported totals are far larger for the fuzzy
   Crossref/OpenAlex searches (e.g. 1250496 for `professional mourners funeral song`). The
   table now reports API-reported totals and screened counts separately.
2. I first excluded Alembi (Abanyole) on scope, having read only its abstract. A second
   read of the full text shows paid performers (food, money, alcohol), a named sub-genre
   reserved for morally upright men, and praise of the deceased's virtues — it is the
   non-European professional-mourner row the first pass had left open. Promoted to S981.

## Unreachable — recorded, not papered over

23 candidate URLs with their exact observed responses are tabulated in rows.md §4. The
most consequential:

- `journal.oraltradition.org` — **connection timed out** at 30 s on three attempts
  (root, issue page, PDF). This was the single most on-point source for the
  *moirologia* / professional-mourner facet; no Oral Tradition row is proposed.
- `minpaku.repo.nii.ac.jp` (Burgenland Croatian laments) — **HTTP 503**, twice.
- `durham-repository.worktribe.com` ("Pure Corpses, Dangerous Citizens") — **HTTP 403**.
- `doiserbia.nb.rs` (two "Shaping the pain" articles) — **connection timed out** at 30 s.
- `trad-culture.ru` (Olonets Karelian prichitannye) — **HTTP 404** at the published URL.
- `degruyterbrill.com` / `degruyter.com` PDF route — **HTTP 202 with 0 bytes**
  (challenge interstitial); the same article was obtained at 200 from `sciendo.com`.
- Two DSpace handles (`10072/30483`, `1808/7785`) — **HTTP 200 but a JavaScript-only
  shell**, no article text in the served bytes.
- `opus.bath.ac.uk` PDF route — HTTP 200 but an HTML portal page, not a PDF.
- Two OpenEdition PDF routes — HTTP 200 but ~1.5 KB shells.
- Crossref `itkuviis lament refrain` — **HTTP 429**, empty body.

## Remaining unknown

No East-Asian or South-Asian professional-mourner tradition could be captured (Korean,
Turkish and South-Asian candidates were out of scope or on unreachable hosts), and the
only captured source for that facet outside Europe and Africa is a tier-C news brief
(S979). The entry should treat S979 as a lead only and should not assert a
non-European professional-mourner institution on it.

## Tooling

**No tool was installed or upgraded.** `pdftotext` (poppler) and `curl` were already
present (`/usr/bin/pdftotext`, `/usr/bin/curl`); no `fitz`/PyPDF2 fallback was needed, so
no `uv`/`pip` install and no `pacman` transaction occurred. The operator's pacman pause
was therefore not touched.

## Files written

- `.ufo/waves/round-95/w1/stage/ScoutTopic95/rows.md` (main output)
- `.ufo/waves/round-95/w1/stage/ScoutTopic95/evidence/S970.pdf` … `S981.pdf` (12 files)
- `.ufo/waves/round-95/w1/stage/ScoutTopic95/evidence/S970.txt` … `S981.txt` (12 files)
- `.ufo/waves/round-95/w1/stage/ScoutTopic95/DONE`
- `.ufo/waves/round-95/w1/ScoutTopic95.md` (this Report trailer)

No commits, pushes or mutating git/jj commands were run.
