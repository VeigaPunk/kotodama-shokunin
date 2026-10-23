# ScoutDerogatoryNames — round 58, claim C source item (S506, S507)

Scope: removal of derogatory US place names — Secretarial Orders 3404/3405 (2021), the 2022 replacement of names containing sq___, the Advisory Committee on Reconciliation in Place Names. Two sources opened and offered, both official doi.gov press releases (live, HTTP 200, carrying an "ARCHIVED content" banner but served on the live site, not Wayback). `grep -F 'doi.gov' corpus/SOURCES.md` and `grep -F 'usgs.gov' corpus/SOURCES.md` both return nothing, so neither URL is in the registry.

Worldbuilder design decisions these rows feed: **who may give or change a name and under what rule** (a national naming authority; executive orders over it; Tribal consultation; case-by-case proponent process vs systematic committee review) and **derogatory-name removal as a renaming policy** (term declared derogatory, then every feature carrying it renamed; precedents 1962 and 1974; populated places treated more cautiously).

## (1) Registry rows

| S506 | U.S. Department of the Interior, 2021, Secretary Haaland Takes Action to Remove Derogatory Names from Federal Lands (press release, 19 November 2021) — https://www.doi.gov/pressreleases/secretary-haaland-takes-action-remove-derogatory-names-federal-lands (direct, HTTP 200) | web | A | US federal naming authority (Board on Geographic Names) and Secretarial Orders 3404/3405 on derogatory place names | para. 1: "ordered the Board on Geographic Names – the federal body tasked with naming geographic places – to implement procedures to remove the term from federal usage" | In the United States the Board on Geographic Names is the federal body that names geographic places, and it was ordered to strip a slur term from federal usage. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S507 | U.S. Department of the Interior, 2022, Interior Department Completes Removal of ‘Sq___’ from Federal Use (press release, 8 September 2022) — https://www.doi.gov/pressreleases/interior-department-completes-removal-sq-federal-use (direct, HTTP 200) | web | A | the 2022 replacement of names containing sq___ on nearly 650 US geographic features | para. 1: "the Board on Geographic Names (BGN) has voted on the final replacement names for nearly 650 geographic features featuring the word sq___" | In 2022 the federal naming board approved replacement names for roughly 650 geographic features that had carried the slur sq___, completing the change. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Notes for the L1:
- S506 quote is a clause (24 words) of the body sentence "She also declared “squaw” to be a derogatory term and ordered the Board on Geographic Names – …". The en dashes are on the page and are dropped by the locator's normalisation.
- S507 quote is a clause (22 words) of the first body paragraph. The page's meta description has a near-copy ("Interior today announced the Board on Geographic Names has voted on …") **without** "(BGN)"; the offered quote includes "(BGN)", which only the body carries, and BOILER's label check passed (output below). If the L1 trims "(BGN)" the quote would match the meta description and fail BOILER — keep it.
- The S507 title on the page reads “Sq___” with curly quotes; I wrote ‘Sq___’ in the source cell to keep straight double quotes out of every cell except the anchor.

## (2) Gate lines

- S506 — https://www.doi.gov/pressreleases/secretary-haaland-takes-action-remove-derogatory-names-federal-lands — accessed 2026-10-23 — para. 1: “ordered the Board on Geographic Names – the federal body tasked with naming geographic places – to implement procedures to remove the term from federal usage”. Grounds: In the United States the Board on Geographic Names is the federal body that names geographic places, and it was ordered to strip a slur term from federal usage. Seat: ScoutDerogatoryNames.
- S507 — https://www.doi.gov/pressreleases/interior-department-completes-removal-sq-federal-use — accessed 2026-10-23 — para. 1: “the Board on Geographic Names (BGN) has voted on the final replacement names for nearly 650 geographic features featuring the word sq___”. Grounds: In 2022 the federal naming board approved replacement names for roughly 650 geographic features that had carried the slur sq___, completing the change. Seat: ScoutDerogatoryNames.

## (3) rowcheck output

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutDerogatoryNames/rows.md` (exit 0):

```
S506 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.doi.gov/pressreleases/secretary-haaland-takes-action-remove-derogatory-names-federal-lands | BOILER: root-clear https://www.doi.gov/; not a title, h1 or meta label | RELEVANCE: shared=['board', 'body', 'feder', 'geogr', 'name', 'order'] | TOPIC: quote_hits=2 function_words=5 page_hits=17 page_terms=13 need=1/2/3/2
S507 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.doi.gov/pressreleases/interior-department-completes-removal-sq-federal-use | BOILER: root-clear https://www.doi.gov/; not a title, h1 or meta label | RELEVANCE: shared=['board', 'featu', 'geogr', 'name', 'repla'] | TOPIC: quote_hits=1 function_words=3 page_hits=5 page_terms=5 need=1/2/3/2
```

(Run without `--entry`, so RELEVANCE (c)/(d) are not yet checked; each draft sentence below reuses at least two content words of both the quote and the teaches cell.)

## (4) draft sentences

S506:
- In the United States the federal body tasked with naming geographic places is the Board on Geographic Names, set up by Executive Order in 1890 to keep geographic name usage uniform throughout the federal government (S506).
- A naming authority can be ordered to remove a term outright: in 2021 the Secretary of the Interior declared one slur derogatory and ordered the Board on Geographic Names to remove the term from federal usage, with Secretarial Order 3404 creating a task force to find replacement names and requiring it to engage in Tribal consultation (S506).
- The Board's ordinary process acts case by case and puts the onus on proponents to identify an offensive name and suggest a replacement, so a federal name change can take years; Secretarial Order 3405 therefore created the Advisory Committee on Reconciliation in Place Names to review and recommend changes to other derogatory geographic names systematically (S506).
- The order had precedents: in 1962 the Secretary of the Interior identified the N-word as derogatory and directed the Board on Geographic Names to develop a policy to eliminate its use, and in 1974 the Board removed a pejorative term for Japanese from federal usage (S506).

S507:
- In September 2022 the Board on Geographic Names voted the final replacement names for nearly 650 geographic features featuring the word sq___, effective immediately for federal use (S507).
- The task force received more than 1,000 public recommendations and several hundred more from nearly 70 Tribal governments, and had to weigh several proposals for the same feature, features crossing Tribal, federal and state jurisdictions, and inconsistent spelling of Native language names (S507).
- Seven unincorporated populated places were held back for additional review by local communities before their replacement names were decided, and the public may still propose name changes for any geographic features through the regular Board process (S507).

## (5) rejected

- https://www.doi.gov/priorities/reconciliation-place-names — guessed URL; `curl -sL -w '%{http_code}'` printed `404` (42537-byte not-found page). Not offered.
- https://www.doi.gov/priorities/reconciliation-place-names/advisory-committee — guessed URL; `curl` printed `404`. Not offered.
- https://www.usgs.gov/us-board-on-geographic-names/derogatory-names — guessed URL; `curl` printed `404` (85433-byte not-found page). Not offered.

Open gap: no live official page dedicated to the Advisory Committee on Reconciliation in Place Names was reached; the committee is carried only through S506 (its creation under Order 3405 and its membership) and the S507 mention ("Next steps on the status of that Committee will be announced"). Its later status, including any 2025 disbanding, was not found and is not claimed.

## installs:

none.
