# ScoutLiveryBadges — Claim C source scout (KotodamaR57)

Seat: livery badges and collars as marks of affinity rather than lineage. Godspeed axes: (a) coverage of badge names, bearers, placement, transfer and rank, (b) source quality (holding-museum records with live-located quotes), (c) freshness. Two sources reported; all six quotes below were LOCATED by the round locator. Exact source URLs were absent from `corpus/SOURCES.md` when checked. Tools installed: none.

---

### NEW-ScoutLiveryBadges-1

citation: The British Museum (n.d.), Collection Online record, “Dunstable Swan Jewel” (museum number 1966,0703.1; curator’s comments cite Hinton 2005 and Marks & Williamson 2003).
url: https://web.archive.org/web/20251024134950id_/https://www.britishmuseum.org/collection/object/H_1966-0703-1
route: Wayback capture 20251024134950 (`id_`), plain GET HTTP 200 (159,930 bytes); the live British Museum URL returned HTTP 403 with a “Just a moment” challenge (challenge met, not passed).
kind: record (museum object catalogue record)
tier: A — official holding-museum record; object details are catalogued by the Museum, and the curator’s comments identify their cited interpretation sources.
scope: The object’s livery-badge classification and crowned-swan form; the coronet as a Lancastrian sign; the White Hart Jewel as a rich livery badge worn by Richard; the swan’s adoption from the Bohun family into Lancastrian use.
quotes:
- B1: “The jewel provides an excellent example of the richest form of livery badge, which may be seen in the White Hart Jewel worn by Richard”
  LOCATED https://web.archive.org/web/20251024134950id_/https://www.britishmuseum.org/collection/object/H_1966-0703-1
- B2: “The coronet round its neck helps to identify it as a Lancastrian emblem”
  LOCATED https://web.archive.org/web/20251024134950id_/https://www.britishmuseum.org/collection/object/H_1966-0703-1
- B3: “The swan was the badge of the Bohun family and was adopted by Henry of Lancaster, son of John of Gaunt”
  LOCATED https://web.archive.org/web/20251024134950id_/https://www.britishmuseum.org/collection/object/H_1966-0703-1
teaches: A crowned swan could serve as a Lancastrian livery emblem, while the same museum record treats Richard’s White Hart Jewel as a rich livery badge.
draft sentences:
- Use a coronet as an allegiance cue on a swan badge: the Museum says the coronet identifies it as a Lancastrian emblem (NEW-ScoutLiveryBadges-1, B2).
- Treat Richard’s White Hart as a wearable livery badge, not only a family device: the Museum calls the White Hart Jewel a rich badge worn by Richard (NEW-ScoutLiveryBadges-1, B1).
- Allow a badge to change dynastic use: the Museum says the swan was the Bohun family badge and was adopted by Henry of Lancaster (NEW-ScoutLiveryBadges-1, B3).

---

### NEW-ScoutLiveryBadges-2

citation: London Museum (n.d.), “Collar of Esses,” Collection Online record, Object ID A295 (Late Medieval, 15th century).
url: https://www.londonmuseum.org.uk/collections/v/object-37465/collar-of-esses/
route: Direct plain GET, HTTP 200 (`text/html`, 159,776 bytes); opened in this session.
kind: record (museum object catalogue record)
tier: A — official holding-museum record for a surviving badge and its catalogue description.
scope: The S-link Collar of Esses as a badge form; Lancastrian kings’ grants of silver or gold collars to chief supporters; similar pewter badges worn by less-favoured supporters.
quotes:
- L1: “Pewter badge in the form of collar of SS”
  LOCATED https://www.londonmuseum.org.uk/collections/v/object-37465/collar-of-esses/
- L2: “The Lancastrian kings Henry IV, Henry V and Henry VI gave their chief supporters silver or gold collars made up of links”
  LOCATED https://www.londonmuseum.org.uk/collections/v/object-37465/collar-of-esses/
- L3: “in the form of the letter S. Less favoured supporters wore similarly shaped pewter badges”
  LOCATED https://www.londonmuseum.org.uk/collections/v/object-37465/collar-of-esses/
teaches: Lancastrian collars of S-links were rank-coded: chief supporters received silver or gold collars, while less-favoured supporters wore similar pewter badges.
draft sentences:
- Name the S-link device as a Collar of SS or Esses; this museum object is a pewter badge in that form (NEW-ScoutLiveryBadges-2, L1).
- Make patronage visible in material: the Museum says Lancastrian kings gave silver or gold collars to their chief supporters (NEW-ScoutLiveryBadges-2, L2).
- Let less-favoured supporters wear a lower-cost version with the same shape: the Museum describes their pewter badges as similarly shaped (NEW-ScoutLiveryBadges-2, L3).

---

### Rejected

- V&A Explore the Collections API record O374477 (accession M.14-1989), opened by ordinary GET; its summary describes retainers’ badges, their wear on a person or horse harness, and parliamentary suppression. Not filed: it is general context rather than one of the two specific badge/collar records selected for this source limit.
- Fordham University’s “Livery Badge” page in the Medieval London Objects exhibit, opened by ordinary GET; it gives general context on material and household rank. Not filed: secondary exhibit rather than a holding-museum object record, and less specific than the two selected records.
- Southampton eprints PDF `https://eprints.soton.ac.uk/464130/1/751865.pdf`: attempted as a possible source, but the direct download timed out after a partial response and the Wayback download returned only a 1 MiB partial file; no content was relied on.
- BM brooch-placement wording was visible in the fetched record, but repeated locator requests failed with transient `HTTPError`/`URLError`; omitted rather than offered as an unlocated quote.
