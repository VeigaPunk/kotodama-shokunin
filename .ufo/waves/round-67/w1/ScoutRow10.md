# ScoutRow10 — claim C rows S823 + S824 (medicine/healing register)

## Opened rows

- **S823** — Medieval European surgical guilds / barber-surgeons. Source: Charles E Bagwell, "'Respectful Image': Revenge of the Barber Surgeon," *Annals of Surgery* 241(6) (2005): 872–878, doi 10.1097/01.sla.0000165185.88634.d0 — https://pmc.ncbi.nlm.nih.gov/articles/PMC1357167/ (tier A peer-reviewed journal, open access). Anchor: "the Barber's Company was organized in 1308 and established by ordinance in 1376" — the medieval guild spine (1308 organization, 1376 ordinance, 1365 Fellowship of Surgeons, 1540 Henry VIII charter uniting barbers and surgeons as the RCS forerunner). Wayback 20250206032558id_ verified HTTP 200.
- **S824** — African healing systems, sangoma/nganga. Source: Chateau, Gqaleni, Aldous & Dlova, "A qualitative study on traditional healers' perceptions and management of epidermolysis bullosa," *Health SA Gesondheid* 28 (2023): 2266, doi 10.4102/hsag.v28i0.2266 — https://pmc.ncbi.nlm.nih.gov/articles/PMC10476505/ (tier A peer-reviewed, AOSIS open access). Anchor: "isangoma [diviner], inyanga [herbalist] and umthandazi [faith healer]" — the source's explicit three-type typology of KwaZulu-Natal traditional health practitioners; ancestor-connection practice (impepho, bones, candles, prayer). Wayback 20250223010348id_ verified HTTP 200.

## Evidence

- Both live URLs curl HTTP 200 (Sat 24 Oct 2026 12:38 UTC), single fetch, no redirects, no paywall; PMC bodies gzip (need --compressed). Quotes verified verbatim in page body text (S824's isiZulu terms are wrapped in `<em>` tags, so the contiguous quote reads with markup between words).
- Uniqueness: neither URL appears in corpus/SOURCES.md (no PMC1357167/PMC10476505 hits); r67 rows/ tree so far only holds ScoutRow11 (S825/S826, different PMC article) — no collision. Hosts: pmc.ncbi.nlm.nih.gov for both; S824's distinct normalized URL keeps LINK safe.
- Row files validate: 11 cells each, kind `paper`, tier `A`, status `mined`, opened 2026-10-24, used-by corpus/knowledge/culture-material/medicine-healing-codes.md, scope 58 chars, teaches 235/237 chars, anchor quotes 13 and 8 body words.
- Bullets drafted inside each row file with >=3 in-order quote content words ("Barber's Company organized established ordinance"; "isangoma inyanga umthandazi healer"), novel content words ("preceded"/"merger", "KwaZulu-Natal"/"practitioners"/"callings"), and <80% in-order teaches coverage.

## Rejects filed (rows/ScoutRow10/rejects.txt)

publishing.rcseng.ac.uk licensing article (403 Cloudflare), ajol.info indilinga/116423 (202 empty x2), metmuseum.org toah/afhe (429), britishmuseum.org term x35485 (403), europepmc MED/12482784 (403), PMC10781813 Münster practice journal (German-only body — no English guild anchor), PMC1035819 17th-c German barber-surgeon (scan stub, no body text).

## Post-write coordination note

CriticFrontier's C-APPEND vs Ca-D4 id conflict (S829+ today-dated rejects required by Ca D4 but outside accept-c.py's NEW_IDS∪EXTRA_IDS bound) was independently confirmed against the frozen counters. Parent L1 ruled: no counter revision — per-claim lands separation, C evaluated at its own lands commit A_c (S805-S828 append only), Ca at later A_ca carrying the S829+ reject rows. My S823/S824 rows sit inside S805-S828 and are unaffected.

## Notes for integrator

- Both rows are PMC-hosted; if HOSTS leg needs more distinct hosts, either could swap, but the assigned topics' best curl-verifiable scholarly sources were both on PMC. The rcseng.ac.uk history page (HTTP 200, official body) is a viable alternate S823 host if host diversity is tight — verified live, quote "was a trade guild and a London Livery Company that apprenticed and examined trainees" — but it is early-modern-leaning; the Bagwell paper is the stronger medieval source.
- No tooling installed or upgraded this run (pacman guard respected; curl/python3 sufficient).

Report: .ufo/waves/round-67/w1/ScoutRow10.md
