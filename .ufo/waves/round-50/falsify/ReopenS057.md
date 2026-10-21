# Reopen S057 — Salzman 2004 Routledge publisher page

Seat: `KotodamaR50-2.ReopenS057-21` (leaf, read-only). Round 50 falsify wave.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes read with `git show <sha>:<path>`; no working-tree claim trusted. No clone needed, no edits, no installs.

## Verdict: **HOLDS**

The S057 row, its Gate bullet, and all three entry citations survive an independent re-open of the URL.
Two non-blocking traceability notes follow the evidence.

## 1. Row and Gate, as landed

Row — `corpus/SOURCES.md:86` (11 fields, matching the header shape at `corpus/SOURCES.md:21-22`):

```
| S057 | Salzman 2004, Pastoralists: Equality, Hierarchy, and the State, Routledge — https://www.routledge.com/Pastoralists-Equality-Hierarchy-And-The-State/Salzman/p/book/9780813338149 | book | B | the book's stated programme and chapter list only (publisher description; QUALITY criterion 6); ethnography and conclusions unread | Description ¶1 sentences 2–3; Table of Contents | political organisation (segmentary tribe, tribal chiefdom, peasant pastoralist) is an axis separate from mobility | mined | 2026-10-21 | 365d | corpus/knowledge/culture-material/pastoralism-animal-husbandry.md |
```

Gate bullet — `corpus/lessons/round-50.md:42`:

> - S057 — https://www.routledge.com/Pastoralists-Equality-Hierarchy-And-The-State/Salzman/p/book/9780813338149 — accessed 2026-10-21 — Description ¶1 sentence 2: "provides detailed analyses of divergent types of pastoral societies, including segmentary tribes, tribal chiefdoms, and peasant pastoralists". Grounds the publisher's description only (tier B, QUALITY 6). Seat: SrcGalatyJohnson.

Cohort shape: S048–S069 occupy `corpus/SOURCES.md:77-98`, contiguous, one row per id, `S057` occurs once;
Gate has 22 bullets (`grep -c '^- S0[456][0-9] — '` → 22). Status policy is explicit at
`corpus/lessons/round-50.md:58-59`: "New rows S048–S069 enter `mined` with `used-by` = …", so no
old→new in-place change was owed (`corpus/SOURCES.md:9-13` append-only rule).

## 2. URL re-opened this session

```
$ curl -sSI -A '<Chrome UA>' 'https://www.routledge.com/Pastoralists-Equality-Hierarchy-And-The-State/Salzman/p/book/9780813338149'
HTTP/2 200
date: Wed, 21 Oct 2026 16:34:29 GMT
content-type: text/html; charset=UTF-8
server: cloudflare
cf-cache-status: BYPASS
```

A GET without `-L` also returned `HTTP 200` with `url_effective` identical to the row URL — no redirect,
no paywall/bot wall on this route (166,405 bytes). Page identity: `1st Edition`, `Copyright 2004`,
`Philip Carl Salzman`, `by Routledge`, ISBN `9780813338149`, 204/208 pages (both strings appear), full
`Description` and `Table of Contents`. Matches the row's author/year/publisher/ISBN.

## 3. Quote verbatim and located

Raw-HTML substring test against the fetched bytes:

```
Q2 (Gate quote) present: True
Q3 present: True
```

- Gate quote **"provides detailed analyses of divergent types of pastoral societies, including segmentary tribes, tribal chiefdoms, and peasant pastoralists"** is an exact substring of the served HTML, including the serial comma.
- Sentence split of Description ¶1 (visible text, tags stripped):

```
S1: Drawing upon the author's extensive field research … authoritative synthesis of the varieties of pastoral life.
S2: At an ethnographic level, the concise volume provides detailed analyses of divergent types of pastoral societies,
    including segmentary tribes, tribal chiefdoms, and peasant pastoralists.
S3: At the same time, it addresses a set of substantive theoretical issues: ecological and cultural variation,
    equality and inequality, hierarchy and the basis of power, and state power and resistance.
S4: The book validates "pastoralists" as a conceptual category … subsumed by that term.
```

"Sentence 2" is therefore accurate; the Gate quote is the predicate of that sentence.
`Table of Contents` is present verbatim (`Preface -- Introduction -- Agency and Adaptation -- Equality and
Anarchy -- Hierarchical Image and Reality -- Accommodation and Resistance to the State -- … -- Appendix`).
The row's anchor `Description ¶1 sentences 2–3; Table of Contents` is honest: sentence 3 is also present
verbatim (the `equality and inequality, hierarchy and the basis of power, and state power and resistance`
string occurs in the raw HTML).

## 4. Tier and scope under QUALITY criterion 6

`corpus/QUALITY.md:29` (criterion 6): "publisher descriptions and abstracts are tier B for substantive
claims about a work, even when accurate; reserve tier A for sources primary or authoritative for the
exact scope."

The row claims exactly `B`, and its scope is bounded to "the book's stated programme and chapter list
only (publisher description …); ethnography and conclusions unread". That is precisely the criterion-6
case: publisher description, not the author's text, no A claim, no book-body claim. No calibration
overreach. The land-build seat report (`1c779e4:.ufo/waves/round-50/build/SrcGalatyJohnson.md` §3) records
the same B rationale and the failed alternate routes; the report is tracked in the landed commit.

## 5. Citation-by-citation audit of the entry

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` mentions S057 at three lines
(`git show 1c779e4:<entry> | grep -n 'S057'`):

| line | sentence | supported by what was read? |
|---|---|---|
| 7 | shelf list: `S057 Salzman 2004 (publisher description)` | **Yes.** Page is Routledge's 2004 product page; only its description/ToC were used. |
| 53 | "Political organisation is a **second axis**, not a mobility row: segmentary tribes, tribal chiefdoms and peasant pastoralists (S057). Do not merge the two axes." | **Yes, with an inference marker.** The three type labels are verbatim on the page (Q2); their political-organisation character is carried by the book's own title (*Equality, Hierarchy, And The State*) and ToC (`Equality and Anarchy`, `Hierarchical Image and Reality`, `Accommodation and Resistance to the State`), which sit apart from `Agency and Adaptation`. The page itself never uses the words "mobility" or "axis" — see note N2. |
| 187 | calibration bank: "The publisher's summary of a book is the book's argument — B, S057 is a description only (QUALITY criterion 6) — cite programme and scope, not conclusions" | **Yes.** Accurate self-description of the row's tier and limit; consistent with `QUALITY.md:29`. |

No other sentence in the entry repeats the S057 claim uncited: `grep -n 'segmentary\|chiefdom\|peasant\|second axis\|two axes\|political organ'` returns only line 53.

## 6. Notes (non-blocking)

- **N1 — Gate carries Q1 only, while the row anchor names sentences 2–3.** Sentence 3 is on the page verbatim and is quoted as Q2 in the landed seat report (`SrcGalatyJohnson.md` §4, "Description, paragraph 1, sentence 3"), but the Gate bullet at `lessons/round-50.md:42` reproduces only sentence 2. The SOURCES header only requires each Gate bullet to hold "each row's URL, access date and verbatim quote" (`corpus/SOURCES.md:9`), so this conforms; if the lane wants the Gate to mirror the full anchor, smallest fix is to append Q2 ("ecological and cultural variation, equality and inequality, hierarchy and the basis of power, and state power and resistance") to the S057 bullet, or narrow the anchor to "Description ¶1 sentence 2".
- **N2 — "not a mobility row" is the lane's classification, not a quoted source sentence.** The page's own words are "divergent types of pastoral societies, including …"; the separation from mobility is a reading of the labels plus title/ToC. That is within a tier-B programme scope and is not a claim about the book's conclusions, but an adversarially strict revision could mark it explicitly (e.g. "labels are political/settlement positions, not mobility terms — lane reading") in `teaches` or the entry. No contradicted fact found.

## 7. Adjacent observation (outside this seat's verdict)

`reports/round-50/validation.json` is named as the round receipt but is not in the landed commit:
`git ls-tree -r --name-only 1c779e4 -- reports/round-50` returns 10 files (`claims.json`,
`run-validation.py`, `jj-colocation-probe.py`, three `separability/` files, four `telemetry/` files)
and no `validation.json`, while the path exists on disk. Recorded only because the ticket names
it; the O/Ca seats own that item.

## 8. Bounds honoured

Read-only: no lane file edited, no git index/jj state touched, no mutating git/jj command, no clone, no
background jobs, no delegation. Tool installs: none (pacman paused; nothing needed). Only temp artifact
`/tmp/s057.html` (166 KB) was created and was deleted after the checks.
