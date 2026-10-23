# ScoutBGNPrinciples — round 58, claim C (S504, S505)

Seat: KotodamaR58A2.ScoutBGNPrinciples. Accessed 2026-10-23. Both offered rows are on www.usgs.gov (live official pages, HTTP 200, fetched with urllib/curl using the locator's desktop User-Agent string; no cookies, no challenge). Neither URL is in `corpus/SOURCES.md` (`grep -c -F` = 0 for both; `usgs.gov` has 0 hits in it at all).

**Key finding for the L1:** the BGN Principles, Policies, and Procedures PDF states the three asked-for rules verbatim (local usage, five-year commemorative wait, wilderness), but it is hosted on `d9-wret.s3.us-west-2.amazonaws.com`, whose root returns HTTP 403. That fails BOILER, so no row from it can pass (checker output under `rejected:`). On the usgs.gov HTML pages, the local-usage and five-year sentences have no place word within 3 words of "name", so they fail TOPIC. The two rows I'm offering cover the same design ground, "who may give or change a name and under what rule": a rule that names can be changed but never removed, and the board's rule that let politics freeze a renaming.

## S504

(1) Registry row

| S504 | U.S. Board on Geographic Names (U.S. Geological Survey), n.d., Guidance on Name Proposals — https://www.usgs.gov/us-board-on-geographic-names/guidance-name-proposals (direct, HTTP 200) | docs | A | official US naming-authority rule that an officially named feature can be renamed but never made nameless again | §8 Can a feature be unnamed?: "Once named, a feature in the Geographic Names Information System (GNIS) can never be “unnamed”, only changed to another name." | A feature that has received an official name may later be changed to a new name but never returned to having none. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

(2) Gate line

- S504 — https://www.usgs.gov/us-board-on-geographic-names/guidance-name-proposals — accessed 2026-10-23 — §8 Can a feature be unnamed?: “Once named, a feature in the Geographic Names Information System (GNIS) can never be “unnamed”, only changed to another name.” Grounds: A feature that has received an official name may later be changed to a new name but never returned to having none. Seat: ScoutBGNPrinciples.

(4) draft sentences:
- Under the U.S. Board on Geographic Names, a feature once named in the Geographic Names Information System can never be unnamed again; its official name can only be changed to another name (S504).
- A worldbuilder can take this as a rule for an official register: an official name may be changed to a new name, but a named feature never goes back to having no name (S504).

Same-page context a reviewer will see (§8 continues): "Geographic names are very often well-established on maps, documents, signs, and websites, and to remove them without a compelling reason may lead to confusion." §2 adds that changing a name only to restore historical usage is not, by itself, a reason to change it.

Alternate anchor for S504 (same URL; passes all four legs, output below). Use it instead, never as well:
`§8 Can a feature be unnamed?: "Geographic names are very often well-established on maps, documents, signs, and websites, and to remove them without a compelling reason may lead to confusion."` teaches: `Official place names spread across maps, signs and documents, so the naming board avoids removing them without strong justification.`

## S505

(1) Registry row

| S505 | U.S. Geological Survey, 2015 (September 1), Old Name Officially Returns to Nation's Highest Peak — https://www.usgs.gov/news/featured-story/old-name-officially-returns-nations-highest-peak (direct, HTTP 200) | web | A | how the US naming board's no-pending-legislation policy let congressional politics stall the McKinley-Denali renaming | § An impasse with Congress and the Board: "the BGN adopted a policy in the 1960s that it would not consider geographic name issues that were the subject of pending congressional legislation" | From the 1960s the federal naming board refused to rule on any geographic name dispute while Congress had a bill pending about it. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

(2) Gate line

- S505 — https://www.usgs.gov/news/featured-story/old-name-officially-returns-nations-highest-peak — accessed 2026-10-23 — § An impasse with Congress and the Board: “the BGN adopted a policy in the 1960s that it would not consider geographic name issues that were the subject of pending congressional legislation”. Grounds: From the 1960s the federal naming board refused to rule on any geographic name dispute while Congress had a bill pending about it. Seat: ScoutBGNPrinciples.

The quote is the main clause of the page sentence "In order to distance itself from political considerations, the BGN adopted a policy … pending congressional legislation, a policy later endorsed by the Secretary of the Interior in 1981." The full sentence is 32 words, above the 25-word cap.

(4) draft sentences:
- In the 1960s the U.S. Board on Geographic Names adopted a policy of not considering any geographic name issue that was the subject of pending congressional legislation, to keep clear of politics (S505).
- That rule let politics freeze a name: from 1977 to 2015 the Ohio congressional delegation kept introducing bills to keep the name Mount McKinley, which left the board's consideration of the name Denali pending indefinitely (S505).
- The geographic name dispute set a commemorative name against an older one: a prospector named the mountain after William McKinley in 1896, while Denali is the English spelling of its Athabascan name; a 2015 Secretarial Order made Denali official in federal records (S505).

All three are carried by the page (sections "Mount McKinley, the name", "A name before time", "An impasse with Congress and the Board", and the lead). **Caveat:** the page is dated 1 September 2015 and reports the name as of then. I did not open any source in this session for later changes. [INFERENCE] The federal name was changed back to Mount McKinley in 2025. Keep entry sentences in the past tense and tied to 2015, and don't state the current official name from this row.

Alternate anchors for S505 (same URL; each passes all four legs, output below). Use one instead, never as well:
- `§ A name before time: "The word Denali is the accepted English spelling of an Athabascan name for the mountain, meaning “the tall one.”"` teaches: `Denali is the standard English rendering of the mountain's Athabascan name, which means the tall one.` (endonym and romanized spelling)
- `§ Denali goes to the U.S. Board: "The Alaska State Board on Geographic Names, acting under state authority, made the name Denali official for state use in 1975."` teaches: `Alaska's own state naming board adopted Denali officially for state purposes in 1975, decades before federal recognition.` (state and federal naming authorities disagreeing)

Passing alternate from a different URL. It can replace either slot but must not be added as a third row:
`| S505 | U.S. Geological Survey, Water Resources Division, 1999, Commemorative naming in the United States (Fact Sheet 158-99, doi:10.3133/fs15899) — https://www.usgs.gov/publications/commemorative-naming-united-states (direct, HTTP 200) | docs | A | settlers' commemorative naming of natural features | abstract: "Naming rivers, mountains, and valleys after individuals was one way settlers marked the land" | Settlers claimed land by giving rivers, mountains and valleys the names of individual people. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |`. Its page margins are thin (page_hits=6, page_terms=2, function_words=3), so it is weaker against a reviewer than the Denali row.

## (3) rowcheck output

Offered rows (`/fast/scratch/hyaku/kotodama-r58/ScoutBGNPrinciples/rows.md`):

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutBGNPrinciples/rows.md
S504 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.usgs.gov/us-board-on-geographic-names/guidance-name-proposals | BOILER: root-clear https://www.usgs.gov/; not a title, h1 or meta label | RELEVANCE: shared=['chang', 'featu', 'name'] | TOPIC: quote_hits=1 function_words=5 page_hits=41 page_terms=36 need=1/2/3/2
S505 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.usgs.gov/news/featured-story/old-name-officially-returns-nations-highest-peak | BOILER: root-clear https://www.usgs.gov/; not a title, h1 or meta label | RELEVANCE: shared=['1960', 'congr', 'geogr', 'name', 'pendi'] | TOPIC: quote_hits=1 function_words=6 page_hits=37 page_terms=21 need=1/2/3/2
exit=0
```

Alternates (`alts.md`):

```
S504 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.usgs.gov/us-board-on-geographic-names/guidance-name-proposals | BOILER: root-clear https://www.usgs.gov/; not a title, h1 or meta label | RELEVANCE: shared=['docum', 'maps', 'name', 'remov', 'sign'] | TOPIC: quote_hits=1 function_words=5 page_hits=41 page_terms=36 need=1/2/3/2
S505 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.usgs.gov/news/featured-story/old-name-officially-returns-nations-highest-peak | BOILER: root-clear https://www.usgs.gov/; not a title, h1 or meta label | RELEVANCE: shared=['athab', 'denal', 'engli', 'mount', 'name', 'tall'] | TOPIC: quote_hits=1 function_words=5 page_hits=37 page_terms=21 need=1/2/3/2
S505 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.usgs.gov/news/featured-story/old-name-officially-returns-nations-highest-peak | BOILER: root-clear https://www.usgs.gov/; not a title, h1 or meta label | RELEVANCE: shared=['1975', 'alask', 'board', 'denal', 'offic', 'state'] | TOPIC: quote_hits=1 function_words=4 page_hits=37 page_terms=21 need=1/2/3/2
exit=0
```

The fact-sheet alternate and the rejected candidates (`rejects.md`):

```
S504 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.usgs.gov/faqs/how-can-i-name-unnamed-natural-feature | BOILER: root-clear https://www.usgs.gov/; not a title, h1 or meta label | RELEVANCE: shared=['accep', 'local', 'prese', 'usage'] | TOPIC: quote_hits=0 function_words=4 page_hits=110 page_terms=92 need=1/2/3/2
S504 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.usgs.gov/faqs/how-can-i-propose-a-name-change-a-natural-feature | BOILER: root-clear https://www.usgs.gov/; not a title, h1 or meta label | RELEVANCE: shared=['name', 'year'] | TOPIC: quote_hits=0 function_words=7 page_hits=101 page_terms=80 need=1/2/3/2
S504 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC FAIL | LOCATE: https://www.usgs.gov/us-board-on-geographic-names/guidance-name-proposals | BOILER: root-clear https://www.usgs.gov/; not a title, h1 or meta label | RELEVANCE: shared=['comme', 'name', 'year'] | TOPIC: quote_hits=0 function_words=5 page_hits=41 page_terms=36 need=1/2/3/2
S505 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.usgs.gov/publications/commemorative-naming-united-states | BOILER: root-clear https://www.usgs.gov/; not a title, h1 or meta label | RELEVANCE: shared=['indiv', 'land', 'mount', 'river', 'settl', 'valle'] | TOPIC: quote_hits=1 function_words=3 page_hits=6 page_terms=2 need=1/2/3/2
S505 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/DNC_PPP.pdf quote-absent | BOILER: not-located | RELEVANCE: shared=['domes', 'polic', 'princ', 'proce'] | TOPIC: quote_hits=2 not-located
exit=1
```

The real Principle II sentence from the PDF (`pdftest.md`):

```
S505 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/DNC_PPP.pdf | BOILER: root-unfetchable https://d9-wret.s3.us-west-2.amazonaws.com/ HTTPError | RELEVANCE: shared=['geogr', 'local', 'name', 'offic', 'prefe'] | TOPIC: quote_hits=1 function_words=7 page_hits=298 page_terms=231 need=1/2/3/2
exit=1
```

## (5) rejected:

- https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/DNC_PPP.pdf (BGN DNC Principles, Policies, and Procedures; HTTP 200, application/pdf, 917192 bytes): this is the best primary source, but it fails BOILER because the bucket root cannot be fetched. `curl` output: `S3 root: 403 application/xml`. The rowcheck output for its Principle II sentence is above. The text I opened, for the L1's own understanding only (not citable this round): Principle II "The underlying principle of the BGN for establishing official geographic names and their applications is recognition of present-day local usage or preferences."; Policy III Sec. 1 "The BGN will only accept proposals for names that are intended to honor a person or persons deceased at least five years."; Policy IV Sec. 1 "The BGN will not approve proposed names for unnamed features within wilderness areas, including unpublished names in local use, unless an overriding need can be demonstrated by the proponent."; Policy IV preamble "Placenames in a wilderness area might diminish the sense of discovery that those who visit ought to be able to experience." (The `rejects.md` PDF line used a title-page string that pypdf did not reproduce, hence `quote-absent` there.)
- https://www.usgs.gov/faqs/how-can-i-name-unnamed-natural-feature: the local-usage sentence "The primary naming principle is based on present day local usage and acceptance." fails TOPIC (`quote_hits=0`, output above). The page also repeats the same text as the name-change FAQ.
- https://www.usgs.gov/faqs/how-can-i-propose-a-name-change-a-natural-feature: the five-year sentence fails TOPIC (`quote_hits=0`, output above). Its other body text duplicates the unnamed-feature FAQ.
- Guidance page §6, the commemorative sentence "Commemorative names are possible, but the individual must have been deceased for at least five years." fails TOPIC (`quote_hits=0`, output above). The same page's §3 wilderness rule is a list item, which the row rules forbid.
- https://www.usgs.gov/us-board-on-geographic-names/domestic-names: not offered. The DNC-responsibility sentence runs past 25 words, and "Place names within the United States and its dependent areas … are the responsibility of the Domestic Names Committee" is a banner repeated on every BGN section page (Guidance repeats it), so it is section boilerplate. Not tested with rowcheck.
- https://www.usgs.gov/us-board-on-geographic-names: an overview and link hub; I only read its links (to the PPP PDF and bylaws on the same S3 host). No body claim fits.
- https://www.usgs.gov/us-board-on-geographic-names/geographic-names-faqs: a list of truncated FAQ teasers, not body prose.
- https://www.usgs.gov/us-board-on-geographic-names/instructions-geographic-names-proposal-submissions: form-filling instructions (Feature ID lookup, scope questions). No principle sentence.
- https://www.usgs.gov/publications/commemorative-naming-united-states: passes, and is kept above as a cross-URL alternate. Not offered as a row because the cap is 2 rows and the Denali row covers renaming politics, which is in the claim's scope list.
- First fetch attempts: plain `curl -A "Mozilla/5.0"` got a CloudFront `403 ERROR … Request blocked.` on three usgs.gov URLs. The same URLs return 200 with the locator's ordinary full desktop User-Agent string (`Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0`). There was no challenge, cookie or login, and the frozen locator uses the same string.

Sources opened: 11 pages/files in total. The brief allowed 1 to 3 sources; to find usable ones I had to open the FAQ, guidance and news pages. Two are offered and the rest are listed above.

## installs:

None. pypdf 5.4.0 was used only through the instrument's own ephemeral `uv run --with pypdf==5.4.0`, with no tool install.
