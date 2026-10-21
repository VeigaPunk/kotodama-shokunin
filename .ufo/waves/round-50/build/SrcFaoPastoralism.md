# SrcFaoPastoralism — frontier source opening for claim C (pastoralism / animal husbandry)

Assigned item: open the FAO Pastoralist Knowledge Hub for real, quote its definition/scope of
pastoralism with a located verbatim quote, and return a SOURCES candidate (URL, kind, tier with
reason, scope, teaching, recheck). Author-lane advice only, never admission. Leaf seat: no
subagents, no installs, no edits to lane files.

## Result

**Opened and quotable. Three FAO pages fetched live this session (2026-10-21), all HTTP 200, no
login, no download.** Primary candidate = the IYRP 2026 feature story (carries the definition);
one corroborating row = the Hub home ("Key facts"); one optional row = the Hub priority-areas page.
L1 assigns ids from S048 upward; I use `S048c` / `S049c` / `S050c` as placeholders only.

---

## Candidate 1 (PRIMARY) — FAO IYRP 2026 feature story

Ready-to-paste row (11 columns, matching `corpus/SOURCES.md:28` header order
`id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by`):

```
| S048c | FAO, Everything you ever wanted to know about rangelands and pastoralists (International Year of Rangelands and Pastoralists 2026 feature story) — https://www.fao.org/newsroom/story/everything-you-ever-wanted-to-know-about-rangelands-and-pastoralists/en | docs | B | FAO's definition of pastoralists and its scope framing of pastoralism (livelihood, cultural heritage, rangeland stewardship), plus the headline herd/country/population estimates it asserts — institutional estimates with no dataset cited on the page | feature story dated 09/04/2026, numbered basics "3. Who calls rangelands home?" paragraphs 1–2 and "4. Why are rangelands and pastoralists important?" paragraph 2 | defines pastoralists as people whose livelihoods mainly rely on domesticated and semi-domesticated animals grazing on rangelands; lists the herd species (sheep, goats, cattle, camelids, yaks, horses, reindeer, buffaloes, ~1 billion animals, >75% of countries); makes strategic seasonal mobility the core adaptation and frames pastoralism as cultural heritage, not only a livelihood | queued | 2026-10-21 | 365d | corpus/knowledge/culture-material/pastoralism-animal-husbandry.md |
```

**Located verbatim quotes (each ≤25 words):**

- Definition — section **"3. Who calls rangelands home?"**, paragraph 1, **second** sentence
  (rendered line 78 begins "Enter the pastoralists, the true guardians of rangelands."):
  > "Pastoralists are people whose livelihoods mainly rely on domesticated and semi-domesticated animals that graze on rangelands."
  (16 words.)
- Herd scope — same section, paragraph 1, **third** sentence:
  > "Worldwide, they herd about 1 billion animals, including sheep, goats, cattle, camelids, yaks, horses, reindeer or buffaloes."
  (18 words.)
- Mobility mechanism — same section, **paragraph 2** (verbatim fragment, the ellipsis is my cut, not the page's):
  > "By moving their herds strategically according to seasonal conditions and forage availability"
  (13 words.)
- Culture framing — section **"4. Why are rangelands and pastoralists important?"**, paragraph 2, final sentence:
  > "Pastoralism is not only a livelihood but also a cultural heritage."
  (12 words.)
- Mobility as policy object — section **"5. How can we support them?"**, paragraph 1:
  > "Their strategic and adaptive mobility help regenerate rangelands and wildlife habitats."
  (11 words.)

**Tier: B — reason.** Per `corpus/QUALITY.md` criterion 6 (`:24-29`), A is reserved for sources
primary or authoritative for the exact scope. FAO is authoritative for *its own* policy framing —
so A would only be defensible if the row's scope were narrowed to "what FAO's pastoralism framing
says". The page is an institutional advocacy explainer, not primary ethnography, and it asserts
headline figures (1 billion animals, >75% of countries, two billion people dependent) **without a
dataset citation on the page**; those numbers need a dataset row (FAO STAT / the Hub's own
"Economics of pastoralism in Argentina, Chad and Mongolia" study) before the entry restates them as
fact. B is therefore the honest tier, and the entry should carry the figures as "FAO institutional
estimate, dataset not cited on page" in its calibration bank.

**Kind: `docs`** — precedent S001 (Glottolog "About" page) is the registry's institutional-web-page
kind; `community` is reserved for non-institutional community resources (ARAS, S047), and FAO is an
intergovernmental publisher, not a community archive.

**What it teaches the entry, by section.** The new entry's sections should follow the sibling
contract (hunting `:25-203`, cartography `:25-237`; 8-field head order = topic, gap filled, sources,
couples, source, verified-at, recheck, scope — confirmed at
`corpus/knowledge/culture-material/cartography-and-mapmaking.md:3-23`):

| Entry section | What this row supplies | What it must NOT be made to say |
|---|---|---|
| §1 register property (herd as the production unit, not the field) | the etic definition boundary: livestock on rangeland, semi-domesticated included; herds as the unit of production and property | it is not a definition of "nomadism" — the page's definition covers settled agropastoralists and ranchers too (it lists "pastoralists, small-scale herders, ranchers and farmers" separately in basic 2) |
| §2 one-owner boundary | the seam list (below) | — |
| §5 mobility / seasonal round | strategic mobility as the adaptation to variable forage: move, let vegetation recover, reduce pressure on soils and water (quotes 3 and 5) | the page gives no typology (nomadic / transhumant / agropastoral / sedentary); the entry must supply or source that typology elsewhere |
| §6–7 herd composition, products, wealth | sheep, goats, cattle, camelids, yaks, horses, reindeer, buffaloes as the species set; meat, milk, fibre, hides as outputs (basic 4) | ~1 billion animals / >75% of countries are unsourced-on-page institutional estimates — calibrate |
| §8 tenure / commons | rangelands as commonly held grazing land; "customary governance" named (basic 5) | the page gives no tenure typology; use `agrarian-field-system-lexicon.md:120` (tenure words) and the Hub priority-areas row for the mobility-legislation fact |
| §10–12 calibration / build order | the "living example of livelihoods and nature coexisting" framing is *advocacy* — flag it as such on first use, never as a neutral finding | do not import the stewardship claim as an established ecological result; it is FAO's framing |

**Recheck: 365d** — the story is a dated (09/04/2026), static feature page tied to IYRP 2026; the
2026 campaign will make it stale-adjacent but its definitional text is not a churning page.

---

## Candidate 2 (corroborating, cite only if the entry needs the culture-system framing)

```
| S049c | FAO, Pastoralist Knowledge Hub (home) — https://www.fao.org/pastoralist-knowledge-hub/en | docs | B | FAO's institutional self-description of the Hub and its "Key facts" scope statements about pastoralism — livelihood and cultural system, local and indigenous knowledge, strategic mobility, customary rangeland management | home page, "Key facts" carousel captions (second and fourth captions); "Why a Hub?" paragraph | frames pastoralism as a livelihood and a cultural system tied to its natural environment, with pastoralists holding local and indigenous knowledge; lists strategic mobility and customary/community-based rangeland management as defining practices | queued | 2026-10-21 | 180d | corpus/knowledge/culture-material/pastoralism-animal-husbandry.md |
```

Located verbatim quote — home page, **"Key facts"** carousel, second caption:
> "Pastoralism is a livelihood and a cultural system closely linked to its natural environment. Pastoralists possess a wealth of local and indigenous knowledge"
(23 words across two sentences, verbatim.)

Why B: identical reasoning to candidate 1 (institutional framing, advocacy register, no primary
data). Why 180d: the Hub home is a news carousel (IYRP 2026 items) and will churn faster than the
story. If L1 registers only one FAO row, register candidate 1; candidate 2 is optional and its
"cultural system" sentence is the one line the culture-material entry actually needs from it.

## Candidate 3 (optional — mobility governance, probably lore-side not entry-side)

```
| S050c | FAO, Pastoralist Knowledge Hub — Priority areas — https://www.fao.org/pastoralist-knowledge-hub/what-we-do/priority-areas/en | docs | B | FAO's stated priority areas for pastoralism, including livestock mobility legislation, transhumance committees and rangeland tenure | page body, opening paragraph and numbered priority 2 | names the scale ("several hundred million" pastoralists) and the governance instruments: VGGT, Technical Guide 6, legislating for livestock mobility, national/regional/local transhumance committees | queued | 2026-10-21 | 180d | — |
```

Located verbatim quote — opening paragraph, first clause:
> "Pastoralists, a collective of several hundred million globally, are vital to the economies of the world's drylands, mountains, and cold regions"
(21 words.)

**Recommendation: do not cite candidate 3 in the culture-material entry.** Its content is policy
and governance (transhumance committees, VGGT, tenure legislation), which belongs to the lore/
polity side, and the entry's `- used-by:` should stay honest. Register it only if a later entry
needs the mobility-governance instrument list; the "several hundred million" figure is also
uncited-on-page and would need the same calibration as candidate 1's figures. It is recorded here
because I opened it and it is real, not because the entry needs it.

---

## Seams the entry must respect (observed this session)

Each of these is a line I actually read in the lane at `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
(this check-out is at the round-50 base context; line numbers as read now):

- `corpus/knowledge/linguistics/semantic-fields-lexicon-building.md:70` — pastoral wealth vocabulary
  (herd-age, herd-colour, herd-condition) already owned as a *lexicon* field; `:105` the
  "steppe pastoral" culture-type bundle. The new entry owns the production system, not the words.
- `corpus/knowledge/myth-symbol/animal-symbolism.md:73` — Nuer "cattle of money" (Evans-Pritchard
  1940) as social idiom; `:110` the Mongol five-livestock wealth-language. The myth-symbol owner
  keeps the idiom; the new entry keeps herd management, breed choice and property.
- `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md:120` — land tenure and the
  words it makes (crop-side); the pastoral entry's tenure section must cite and not restate it.
- `corpus/knowledge/culture-material/transport-mobility-lexicon.md:62` — "the draft layer — harness,
  saddle, stirrup" owns the riding/draft kit; the pastoral entry owns *why* the herd moves
  (forage, season, water), not the vehicle hardware.
- `corpus/knowledge/culture-material/hunting-foraging-subsistence.md:94-110` — owns the
  residential/logistical mobility dial for foragers (Binford S040). The pastoral entry's mobility
  section should *contrast* (herd-led movement, no residential mapping-on) rather than reuse the
  table.
- `corpus/knowledge/culture-material/cuisine-food-lexicon.md:3` — owns food as a cultural system
  (the meal); `:62` (§4 fermentation as heritage) is the seam for dairy processing. The new entry
  stops at the herd's products (milk, meat, fibre, hides); cuisine owns the dish and the ferment.
  (I first wrote `:56` — that line is the famine-foods table row, not the meal-ownership line;
  corrected by reading `:56-57` directly. Use `:3`/`:62`.)
- `corpus/knowledge/culture-material/calendar-festival-systems.md:79` — the civil/ritual calendar;
  the pastoral seasonal round is production-side only.
- `corpus/knowledge/linguistics/phonetics-phonology.md:197` — "mountains + long-distance herding →
  whistled registers" already uses herding as an *explanation* for a phonological register; the new
  entry should not claim that causation as its own finding without a source.

Gap premise re-checked read-only this seat with the exact commands:
`find corpus/knowledge -iname '*pastoral*' | wc -l` → **0**; `-iname '*husband*'` → **0**;
`-iname '*herd*'` → **0**. The topic grep
`grep -rniE '^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/ | wc -l`
→ **1**, and that one hit is a **substring false positive**: `herd` inside "sherd" at
`corpus/knowledge/culture-material/writing-media-surface-economy.md:3` ("sherd, wall, pot,
body"). With the claim's declared `"mode": "word"` (`\bherd\b`) the register is genuinely unowned —
but L1 should know the literal evidence command in `reports/round-50/claims.json` yields 1, not 0,
so if a reviewer runs it verbatim it will look like a contradiction. Suggested fix when the claim
is touched: add `\b` in that `evidence_command` (`(pastoral|herd|husbandr|transhuman|livestock)\b`
does not fix "sherd" — use `\b(pastoral|herd|husbandr|transhuman|livestock)\b`). Do not change the
before-check's semantic expectation; only make its printed command agree with it.

Also verified: the two load-bearing quotes were re-grepped against the **live** pages after being
written into this report — the story definition at rendered **line 78** and the Hub "Key facts"
caption at rendered **line 177** — byte-for-byte identical to the quotes above.

## Unrun checks / gaps (honest)

- **No dataset row opened.** The herd/population figures on candidates 1–3 remain
  "institutional estimate, no dataset cited on page". If the entry states any percentage or count,
  it needs either a calibration flag or a real dataset row (FAO STAT, or the Hub's
  "Economics of pastoralism in Argentina, Chad and Mongolia", https://www.fao.org/documents/card/en/c/cb1271en
  — card seen, not opened, so it is a lead, not a source).
- **No ethnographic primary source opened this seat** (e.g. Evans-Pritchard on the Nuer,
  Barth on nomads). The entry will need at least one for its transhumance typology; that is the
  next frontier opening, not something I can claim from these pages.
- I did not run the entry sweeps, `readme/sweep.py`, or any gate — not my assignment, and the
  source seat must not touch lane files.
- `corpus/lessons/round-50.md` **does not exist yet** (`ls` → no such file). The round's `## Gate`
  must therefore be created by the lesson scribe and must log candidate 1's URL, access date
  2026-10-21 and the 16-word definition quote — the registry rule at `corpus/SOURCES.md:7-10`
  requires every row's quote to live in the round lesson's `## Gate`. My quotes above are the
  verbatim text to paste; do not paraphrase them.
- No tool installed; no pacman/npm/uv transaction. No credentials, no live-process probing.

## Handoff to L1

1. Assign ids ≥ S048 to candidates 1 (mandatory) and optionally 2; candidate 3 only if a
   governance entry will cite it.
2. Set `status` `queued` now; flip to `mined` and fill `used-by` when claim C's entry lands and
   cites it (in-place `status`/`used-by` changes are allowed by `SOURCES.md:8-10`, logged old→new
   in the round lesson).
3. Paste the located quotes into the round-50 lesson `## Gate` before or with the registry row.
4. Entry-side calibration wording: "FAO (2026), institutional estimate, dataset not cited on page"
   for every number; the definitional sentence is FAO's framing, citable as such at tier B.
