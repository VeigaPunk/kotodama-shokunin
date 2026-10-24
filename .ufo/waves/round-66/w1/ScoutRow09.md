# ScoutRow09 — r66 row-opening (S793, S794)

## Deliverables
- `.ufo/waves/round-66/rows/ScoutRow09/row-S793.txt` — ambergris/perfume row
- `.ufo/waves/round-66/rows/ScoutRow09/row-S794.txt` — court perfume / perfumers' guild at Versailles row
- `.ufo/waves/round-66/rows/ScoutRow09/rejects.txt` — 3 evaluated non-used candidates

## Findings (observed)

**S793** → Natural History Museum (London) "What is ambergris?" (Emily Osterloff, museum Discover article).
- Live: `https://www.nhm.ac.uk/discover/what-is-ambergris.html` — curl 200, no redirect, 254,761 bytes fetched 2026-10-24.
- Anchor quote verified verbatim in body: "For hundreds of years, perfumers have categorised the quality of ambergris according to its colour" (plus supporting lines on ambrein as fixative, white varieties finest, synthetic replacement).
- Wayback: `20261013203536` snapshot available via availability API, id_ form used.
- Tier: B (museum institutional article, not peer-reviewed). Kind: `docs` per registry vocabulary (kind inventory: docs/paper/book/dataset/community/spec/tool).
- Uniqueness: `nhm.ac.uk` absent from corpus/SOURCES.md and .ufo wave dirs — no collision.

**S794** → Centre de recherche du château de Versailles thesis project page "Les parfumeurs privilégiés, fournisseurs de la cour de Versailles (XVIIe–XVIIIe siècles)" (Alice Camus, dir. Lucien Bély, Sorbonne; CIFRE w/ Guerlain).
- Live: `https://www.chateauversailles-recherche.fr/article964.html` — curl 200, no redirect, 51,511 bytes.
- Anchor quote verified verbatim: "les gantiers-parfumeurs fabriquent les gants parfumés, dont le succès est à son apogée à la cour de Louis XIV" — states the glover→perfumer trade takeover, monopoly, and apex at Louis XIV's court.
- Wayback: `20260608021222` snapshot available, id_ form used.
- Tier: B (institutional museum research-centre page, not peer-reviewed). French-language source; quote kept verbatim.

## Inference / cautions
- Both rows claim tier B, not A: neither source is peer-reviewed; both are official institutional bodies (national museum; château research centre), consistent with prior-wave museum-row practice.
- `en.chateauversailles.fr/.../perfumer-garden` (the more famous court-perfume page) was REJECTED for S794: no guild mention + zero wayback captures; details in rejects.txt.
- 1656 nuance recorded: scholarly phrasing is that Louis XIV *renewed/confirmed/enlarged* the glover-perfumer statutes (March 1656, registered 13 May), not founded the guild — from Encyclopédie "PARFUMEUR" via search; the CRCV row teaches the monopoly/court relationship rather than a founding date. ScribeEntrySpec may want this distinction for the entry's accuracy.
- Note on S793 scope: the item phrased "Amber/ambergris"; NHM covers ambergris specifically (fossil amber ≠ perfumery "amber" accord). If the entry needs fossil-amber-as-resin, that would need a second source — flagging, not expanding scope.

## Tooling
- No installs/updates performed; curl + python3 stdlib sufficient. Pacman pause observed (guard in force).

## Remaining unknowns
- None blocking: both rows fully verified (live + capture + verbatim quote).
