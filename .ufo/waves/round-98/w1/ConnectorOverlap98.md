# ConnectorOverlap98 — Report (round 98 w1)

Scoped findings for the toasts and drinking-speech formulae surface. Full detail, owner table and the
connector move: `.ufo/waves/round-98/w1/stage/ConnectorOverlap98/overlap.md` (11413 B).

## Verdict

- **No sibling claims the surface.** Term scan `(?i)\b(toast|drink|feast|banquet|libation|hospitality|ritual|ceremony|oath)s?\b` over all 21 sibling PROVINCE.md → 0 matches (grep tool "No matches found", rc-equiv 1); over all 19 existing SKILL.md → matches only in kotodama's own SKILL.md and in mado (:139,:154,:571,:581) / mori (:497,:515) where "ritual" names config/re-pin procedures, not culture surfaces.
- **Boundaries to respect (2):** lore-shokunin — canon (whether a people toasts, who presides, refusal cost; kotodama PROVINCE.md:16-17 hands off); chousa-shokunin — research method (source hierarchy, citation chaining; refused at PROVINCE.md:19). Both are standing lane contracts, unchanged by a new lane-internal entry.
- **Contested scope: 0** items routed to the L1 (limit 3).
- **In-lane boundaries (9 assigned files, one sentence each in §3 of overlap.md):** the cup to `vessel-container-lexicon.md`, the feast frame to `cuisine-food-lexicon.md`, bond/breach/penalty and the shared-cup seal to `guest-right-hospitality-law.md`, binding-formula grammar to `oath-blessing-curse-formulae.md`, boast-vow contests to `verbal-duelling-ritual-insult.md`, votive-pledge edges to `petitionary-and-votive-formulae.md`, arrival/parting cups to `greeting-leave-taking-formulae.md`, occasion placement to `calendar-festival-systems.md`, rite classification to `ritual-liminality.md`.
- **Neighbor beyond the nine:** `death-afterlife-eschatology.md:41,:100` owns libation-to-the-dead inside the ancestor-offering economy (measured this seat); the toast entry should point that facet one-way.

## Numbers with commands and rc

1. `ls -d /home/vgpnk/Projects/shokunin/*-shokunin/PROVINCE.md` → 21 lanes, exit=0 (supervised proc ListProvinces, pid 201484, exit=0).
2. Glob `*-shokunin/SKILL.md` → 19 files; audio-shokunin and game-dev-2d-shokunin publish none (README Domain lines read instead).
3. PROVINCE term scan (21 files, gitignore=false) → 0 matches, rc-equiv 1.
4. SKILL term scan (19 files, gitignore=false) → 3 files with "ritual"-only procedure senses, rc 0.
5. Domain/Owns/Refuses extraction (21 PROVINCE.md) → 20 files matched; tsukuroi-shokunin/PROVINCE.md read directly (:1–33 of 573).
6. In-lane sweep, grep over `kotodama-shokunin/corpus/knowledge`, pattern `(?i)\b(toast|wassail|bragafull|toastmaster|health-drinking|libation)\w*` → 4 files, 7 lines: ainu.md:109; funerary-material-culture.md:8; vessel-container-lexicon.md:5,:36,:38; death-afterlife-eschatology.md:41,:100. Zero toast-family matches — consistent with the frozen claim C before-census in `reports/round-98/claims.json`.
7. Tooling installed: none.

## Reproducibility note

Sibling lane repos are excluded from whole-root grep traversals when gitignore=true (control scan returned only fleet-root files); all sibling scans here ran with gitignore=false. The grep tool reports matches rather than integer exit codes; "0 matches" is its "No matches found" verdict. No frozen file (claims.json, predispatch.py, predispatch-base.txt, controls/) was read-modify-touched; reads only. Nothing committed.

## Connector move (bounded)

Give the new entry a one-way partial-owner table (modeled on guest-right-hospitality-law §1) that splits on the established oath/binding-speech line: the entry owns the words and sequence of the drinking rite and returns cup, feast, bond, formula grammar, boast contest, votive edge and funerary libation to their owners. Pre-wires C8 owners=0 and avoids the round-97 copied-boundary-prose defect (294 → 35 shared 8-grams); verification after landing: C8 sweep rerun plus 8-gram distance against guest-right and oath entries.
