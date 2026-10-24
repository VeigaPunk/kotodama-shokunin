# ScoutRow07 — ROW-OPENING, claim C (S789, S790)

Opened exactly two registry rows as assigned. Drafts are at
`.ufo/waves/round-66/rows/ScoutRow07/row-S789.txt` and
`.ufo/waves/round-66/rows/ScoutRow07/row-S790.txt`; rejects at
`.ufo/waves/round-66/rows/ScoutRow07/rejects.txt`.

## S789 — attar of roses production (OBSERVED)

- Source: Angelova, Dobreva, Mileva et al. 2022, "The Anti-Genotoxic Activity of
  Wastewaters Produced after Water-Steam Distillation of Bulgarian Rosa damascena
  Mill. and Rosa alba L. Essential Oils", *Applied Sciences* 12(7):3677 —
  peer-reviewed, CC BY, PMC full text. Tier **A** (primary paper), kind `paper`.
- Live `https://pmc.ncbi.nlm.nih.gov/articles/PMC8951631/` → HTTP 200, 0 redirects,
  249,918 bytes, 2026-10-24. No login/paywall/rate-limit.
- Anchor quote (16 words, verbatim in body, §1 Introduction):
  "More than 3000 kg of rose flowers produce 1 kg of rose oil by water distillation."
  Bulgarian-context passages corroborated in body: "The locality where the
  production of essential oils takes place in Bulgaria is the so-called 'Valley of
  Roses' near Kazanlak"; "Industrial production of rose essential oil is mainly
  based on water steam distillation from fresh rose flowers followed by cohobating
  or concentration in which the initial distillate undergoes multiple
  redistillation"; semi-industrial processing line at IRAP Kazanlak.
- Capture: Wayback `20250415135912id_` replayed HTTP 200, quote present in
  captured bytes; original URL query-aware-normalizes equal to live (no query).
- Caveat (INFERENCE→state): the paper's declared aim is genotoxicity of the
  wastewaters; the production detail is Methods/Introduction framing. Accurate
  but one step removed from a dedicated attar-industry review — the ideal
  Kovacheva et al. 2010 review was unreachable (see rejects).
- Unique vs `corpus/SOURCES.md` (grep: `PMC8951631` absent; `ncbi` rows use other
  PMCIDs) and vs sibling wave fragments (ScoutRow09 uses nhm.ac.uk +
  chateauversailles-recherche.fr; gap.md lists no PMC).

## S790 — scented gloves / Renaissance perfumed leather (OBSERVED)

- Source: Victoria and Albert Museum, "Pair of gloves", accession T.225&A-1968,
  England 1660s — holding museum's own object record. Tier **A**, kind `docs`
  (precedent: S252/S253/S260 museum object records are `docs`).
- Live `https://collections.vam.ac.uk/item/O78794/pair-of-gloves-unknown/` →
  HTTP 200, 0 redirects, 52,730 bytes, 2026-10-24. No limits; JSON mirror
  `api.vam.ac.uk/v2/museumobject/O78794` also 200.
- Anchor quote (20 words, verbatim in Ownership & Use block):
  "Recipes for scenting gloves survive from the 17th century using ingredients
  such as musk, ambergris, floral extracts and aromatic spices."
  Object framing in same record: "gloves were often perfumed", "pair of brown
  doeskin gloves, England, 1660s; embroidered with silver and silver-gilt
  thread".
- Capture: Wayback `20260108224147id_` replayed HTTP 200, quote present;
  normalized-equal to live URL.
- Caveat: pair is 1660s (post-Renaissance stricto sensu); the record documents
  the *period practice*, not that this pair retains scent. Row scope/wording
  says exactly that. Met 222226 ("may originally have been perfumed", early
  17th c.) is the fallback object if the entry needs a looser date; held in
  reserve since each row needs a unique URL and one row only was assigned.

## Predicate-conformance self-check (exercised locally, not the gate)

Both rows: 11 cells; kind ∈ enum; tier A; status `mined`; opened `2026-10-24`;
recheck `180d`; used-by = the scent entry. Quote 8–25 words ✓ (16, 20). Scope
≤60 ch ✓ (50, 59). Teaches ≤240 ch ✓ (187, 151). Bullets validated against the
frozen `content_words`/in-order logic in `reports/round-66/accept-c.py`: S789
bullet has 3 in-order quote words (rose, flowers, produce), teaches-coverage
0.00, 3 novel words; S790 has 5 in-order words (scenting, musk, ambergris,
floral, extracts), coverage 0.00, 3 novel words; longest copied run ≤3 words.
Hosts: pmc.ncbi.nlm.nih.gov + collections.vam.ac.uk — both distinct from every
base registry host I checked and from ScoutRow09's two hosts.

## Rejects (in rejects.txt)

- tandfonline Kovacheva 2010 — HTTP 403; ideal topically-central source,
  flip = De Gruyter DOI mirror serving full text.
- Springer "Oil Rose (Rosa damascena)" chapter PDF — unverified within
  time-box; flip = open PDF, confirm 3.5–4 t/kg sentence verbatim.

## Tooling

No installs needed; curl + python3 already present. CDX endpoint returned
connection errors on one query; the Wayback `availability` API answered
instead — noted as an intermittent CDX reachability issue, not data.

## Remaining unknowns / handoff notes

- If a later seat's row needs the Kazanlak-industrial-process claim more
  centrally, S789 could be superseded by a dedicated industry review once a
  resolvable full text exists (Kovacheva 2010 or ScienceDirect S0926669022006677).
- Met pair (222226) and FIT/Glove Collection Trust pages remain unopened
  alternates for the scenting-practice leg.
