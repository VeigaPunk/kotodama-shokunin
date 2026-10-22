# ReviewExistingRows — claim D no-harm pass over the 11 existing §2 rows

Seat: `KotodamaR51a3.ReviewExistingRows` (leaf, read-only; report file is the only lane file written).
Round 51 attempt 3, 2026-10-22. All corpus bytes read at the lane worktree, which equals base `bff83ba65bf9559af4d7567e81703059667a0005`.
**Tooling: none installed** (pacman transactions paused host-wide; no install was needed). No LSP server exists for
corpus markdown data files, so every check below is a byte-level `read` of the cited line plus claim D's counter —
no lsp/diagnostics mode was available or applicable.

## Verdict: HOLD — the 11 existing rows are sound; no anchor correction is required

All 19 `path:line` anchors in rows `:31`–`:40` resolve at base, and every item in each row's **What it owns** cell is
carried by the line(s) that row cites. Row `:41` (`civilizations/`) carries a directory anchor, which resolves and
whose ownership cell is true of the directory's contents (round-50 finding F8, still open, cosmetic not causal).
Claim D's counter reproduces the declared before-state:

```
$ python3 -B reports/round-51/boundary-count.py
rows=11 resolved=11 distinct=11        # exit 0
```

The counter's grammar (read in full) accepts `dir/` as a resolving target, so the `civilizations/` row counts as
resolved; `distinct=11` = 10 neighbour files + 1 directory. **D must keep all 11 neighbours and may keep every
existing anchor byte-for-byte.**

## Table shape (exact lines)

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (204 lines): `## 2. One-owner boundary` at `:27`,
blank `:28`, header `| Neighbour (anchor) | What it owns | This entry's boundary |` at `:29`, separator `:30`,
**11 data rows `:31`–`:41`**. (The assignment's "lines 29-41" spans separator through last row.)

## Row-by-row verification (quote → judgment)

All quotes verbatim from the cited neighbour at base; line numbers re-counted against multi-line raw reads and
cross-checked against round-50's independent quotes (its "What HOLDS" §1 proved these neighbour files
byte-identical `4ad2683`→`1c779e4`; my reads are the evidence for the current base).

1. **`:31` `agrarian-field-system-lexicon.md:56,:62`** — owns "parcel, plough, manure contract; the agropastoral
   calendar and routes". `:56` (heavy-plough open field row): "plough team (the critical scarce input), communal
   herding after harvest | … | strips in furlongs, common pasture rights, manor court" → parcel tenure + plough ✓.
   `:62` (agropastoral row): "| agropastoral | fields + pasture + transhumance routes | ploughing peak plus herd
   calendar; manure contracts | … | manure-for-stubble exchange | fold, transhumance, stubble-right |" → manure
   contract, agropastoral calendar and routes ✓. **Supported.**
2. **`:32` `hunting-foraging-subsistence.md:36,:116`** — owns "wild acquisition; meat-for-crops at a farming edge
   `(to-verify)`". `:36`: "1. **Wild source** — the organism or material is not planted, herded or owned as a
   standing crop" ✓. `:116`: "- **Meat as currency** — meat-for-crops exchange with farming neighbours is a design
   possibility `(to-verify)`; … the forager edge of that trade is this entry's, the market register stays at
   `trade-economy-lexicon.md:3`" ✓ — the cell's `(to-verify)` mirrors the line's own hedge (round-50 F9's fix,
   applied). **Supported.**
3. **`:33` `cuisine-food-lexicon.md:67,:81,:152`** — owns "yogurt lineages, milk+meat law, Harris's cow economics
   (contested)". `:67`: "| Bacteria+lactobacilli | kimchi …, sauerkraut, yogurt lineages, idli/dosa batters | …" ✓.
   `:81`: "| Mixing rules | milk + meat separation (Ex 23:19 "kid in its mother's milk", ×3 in Torah); separate
   dishes; waiting times | …" ✓. `:152`: "- Harris's materialist taboos (pig economics, cow economics) — contested
   by culturalists; strongest case is the pig, weakest the cow." ✓. **Supported.** Residual note: the substantive
   cattle clause ("cattle are worth more alive (traction, milk, dung) than dead") sits at `cuisine-food-lexicon.md:86`,
   unanchored since the round-50 fix; the cell as worded needs only `:152`.
4. **`:34` `transport-mobility-lexicon.md:92,:95`** — owns "route class; draught capacity, load figures, harness and
   feed vocabulary". `:92`: "| Route class | track, paved road, causeway, canal, sea lane, relay corridor | …" ✓.
   `:95`: "| Draft | human porterage, ox, horse/mule, camelid, dog, wind | load figure + daily distance + terrain
   law; harness and feed vocabulary | …" ✓. The third column's "not a second load/feed vocabulary" states the feed
   split round-50 F3 asked for. **Supported.**
5. **`:35` `trade-economy-lexicon.md:69`** — owns "cattle-root money words". `:69`: "| fee, pecuniary | Gmc
   \**fehu*, Lat. *pecūnia* < *pecus* 'cattle' | PIE \**peḳu-* 'movable wealth = cattle' (Watkins); cf. Nuer cattle
   as the idiom of all value (Evans-Pritchard 1940) |" ✓. **Supported.**
6. **`:36` `textile-technology.md:22,:27`** — owns "fibre-to-cloth chain; worsted/woollen fork". `:22` (wool row):
   "| wool | *Ovis aries* | shear → wash (suint/urine, lanolin) → card or comb → spin | …" ✓. `:27`: "- **Wool
   technology is the fork that matters**: combed long-staple = **worsted** …; carded short-staple = **woolen** …" ✓.
   **Supported** (round-50 F2's inversion is fixed: `:27` now evidences the neighbour's fork, not this entry's
   fleece selection — the word "fleece selection" no longer occurs in the entry).
7. **`:37` `semantic-fields-lexicon-building.md:70,:105`** — owns "the pastoral vocabulary field and the steppe
   field-bundle". `:70`: "- Pastoral wealth vocabulary (herd-age, herd-color, herd-condition terms) indexes property
   systems; reconstructable PIE horse/wheel/pastoral vocabulary …" ✓. `:105`: "| steppe pastoral | subsistence (herd
   wealth), kin (clan), war (raid), landscape (pasture) | sea/coast terms (note the gap) |" ✓. **Supported.**
8. **`:38` `fire-fuel-light.md:37`** — owns "dung as fuel versus manure". `:37`: "| Dried dung | the herds' output,
   and therefore the fields' | a hot, fast, smoky fire | a real trade-off against manure; fuel-poor pastoral
   cultures pay for it in soil |" ✓. **Supported.** Wording residual: the cited line already grants the source ("the
   herds' output"); the third column's "the herd as dung source" is substantively exercised in this entry at `:95`
   ("Dung | any herd | one dung per season: fuel or field") and §11 step 1, so the boundary is real — the overlap is
   phrasing, not a competing ownership claim.
9. **`:39` `animal-symbolism.md:73,:110`** — owns "the herd's signs; the livestock-as-wealth idiom (Nuer cattle,
   Mongol five livestock)". `:73`: "| Nuer "cattle of money" | Evans-Pritchard 1940 | cattle as social idiom — names,
   songs, bridewealth; not primarily food | …" ✓. `:110`: "- **Faunal economy writes the idiom:** the Mongol five
   livestock (horse, cattle, camel, sheep, goat) structure wealth-language; Nuer cattle structure
   personhood-language (§5). …" ✓. **Supported.**
10. **`:40` `sacred-kingship-mythic-charter.md:65`** — owns "the shepherd-king office". `:65` (delegation row): "the
    ruler is the god's tenant, servant, or shepherd — an office, not a person | Mesopotamian kingship: the king as
    *sipa*, shepherd, with his rule audited by omens and the gods' assembly (Jacobsen 1976; Frankfort 1948) | …" ✓.
    **Supported.**
11. **`:41` `civilizations/` regional entries** — owns "Mongol, Turkic, Scythian, Sámi, Diné, Inca cases and their
    warnings". Directory verified: all six named files exist under `corpus/knowledge/civilizations/` (`mongol.md`,
    `turkic-steppe.md`, `scythian-saka.md`, `finnic-sami.md`, `dine-navajo.md`, `inca.md`; globs re-run this
    session). Warning lines spot-checked at base: `scythian-saka.md:70` "Do not equate pastoralism with total
    absence of farming: even Herodotus distinguishes farming and nomadic Scythians"; `turkic-steppe.md:148` "Do not
    make pastoral production synonymous with economic isolation."; `inca.md:128` ""all wool, all alpaca" is too
    simple"; `mongol.md:40` "This is a working periodization, not a ladder from "primitive nomad" to
    "civilization." Mobile pastoralism, urban production, and documentary administration can coexist." **Ownership
    cell supported at directory level.** The row's *anchor shape* is the one standing defect (below).

## Defects

1. **Rows `:31`–`:40`: none.** No wrong line, no misdirected anchor, no unsupported ownership item. No corrected
   anchors to issue; D should keep these rows byte-for-byte.
2. **`:41` — directory anchor (round-50 F8, still open at base; LOW for D).** The row resolves and its cell is true,
   but it is the only row where the header's "(anchor)" promise is a directory, so it cannot be audited line-wise.
   Fix is optional for D and keeps the neighbour (allowed under "corrections … only where the current anchor is
   wrong" — the anchor is not *wrong*, merely unlined): cite the six case lines round-50 proposed, all re-verified
   at base by this seat — `civilizations/mongol.md:40`, `turkic-steppe.md:148,:193,:194`, `scythian-saka.md:70`,
   `finnic-sami.md:140,:150`, `dine-navajo.md:125`, `inca.md:128`. Leaving the row as-is does **not** falsify D
   (the counter accepts `dir/`; the neighbour is kept).
3. **Cell-vocabulary residue (round-50 F4 tail, not an anchor defect):** "shearing season" (row `:36`) still occurs
   exactly once in the entry — in the §2 cell (grep: only `:36` hits; §6 `:93`-`:94` carries flock management
   "living animals, shorn or plucked" but no season). If the D author touches that row, either drop the phrase or
   add the season to §6; otherwise harmless.

## Comparison with round-50 `.ufo/waves/round-50/falsify/ReviewSec02.md` (verdict was PARTIAL)

| Finding | Status at base `bff83ba` |
|---|---|
| F1 cuisine mis-anchor (`:67,:86` → milk+meat at `:81`, contest at `:152`) | **Closed.** Row now `:67,:81,:152`; all three verified above; cell reworded so `:152` suffices. `:86` (the cattle clause) is now uncited — content note only. |
| F2 textile anchor inversion (`:27` supported this entry's half) | **Closed.** `:22,:27`; cell matches the lines; "fleece selection" dropped from the entry. |
| F3 transport (`:95` carried no "route class"; feed-vocabulary collision) | **Closed.** `:92,:95` with reordered cell; third column now says "not a second load/feed vocabulary". |
| F4 six third-column boundaries never developed | **Mostly closed.** Body now carries dairy (`:88`-`:95` region), dung source (`:95`, §11 step 1), riding/pack breeding (§4), herd composition (§3-§4). Residue: "shearing season" still cell-only (defect 3). |
| F5 no lead sentence; header drift vs contract (`ReviewEntryContract.md:62`); "15 or more" rows | **Still open** (`:28` blank; header still `Neighbour (anchor)…What it owns`; 11 rows). D's growth to 15 closes the row-count half automatically; the lead sentence and header wording are the D author's or a later round's call — outside this seat's row-level scope. |
| F6 missing market row; seven never-cited candidate neighbours | **Still open** — belongs to D's *new* rows, not the existing 11. Note for the D author: the entry's scope/§15 still promise a market hand-off; §2's trade row is `:69`-only and `trade-economy-lexicon.md:3` (the market register owner per `hunting-foraging-subsistence.md:116`) is a live candidate for one of the four new rows (body-level `:3` citation count not re-run at base). |
| F7 agrarian "stubble grazing" mis-anchor; third-column calendar collision; water/tenure under-claim | **Largely closed.** "Stubble grazing" is gone from §2 (grep: only §3 `:54`); the cell now attributes the agropastoral calendar and routes to the neighbour and the third column states the split ("cite that calendar … not a second calendar owner"). Residual: `agrarian-field-system-lexicon.md:33` ("owns parcel, implement, water, rotation … and tenure") is still uncited and the cell still names neither water nor tenure — an under-claim, not a false claim. |
| F8 `civilizations/` row unanchored | **Still open** (defect 2 above). Round-50's proposed line set re-verified at base. |
| F9 hunting row lacked the anchor's `(to-verify)` hedge | **Closed.** Row `:32` now carries `(to-verify)`, matching `:116`'s own marker. |

## No-harm checks for claim D

- Counter before-state reproduced: `rows=11 resolved=11 distinct=11`, exit 0 (matches `claims.json` `before`).
- None of the 11 rows cites the claim-C entry path or any S-id from S071 upward (the §2 rows cite no S-ids at all).
- The 11 neighbours are exactly: agrarian-field-system-lexicon, hunting-foraging-subsistence, cuisine-food-lexicon,
  transport-mobility-lexicon, trade-economy-lexicon, textile-technology, semantic-fields-lexicon-building,
  fire-fuel-light, animal-symbolism, sacred-kingship-mythic-charter, `civilizations/`. Keeping them verbatim is
  compatible with every round-50 finding still open.
- I did not read or use `reports/round-51/calibration/` (held prior-attempt material) and did not touch any lane
  file except this report; no git/jj state command was run.

## Residual risk and verification gaps

- Ownership was checked against the **cited lines** (the seat's contract), not against every line of the ten
  neighbour files — a neighbour may own a concept at a line the table does not cite (the same scope limit round-50
  declared; F1/F3/F7 were instances of that class). Under-claims (F7's water/tenure) are reported, not hunted
  exhaustively.
- `mongol.md:40` was re-counted precisely (the coexist bullet is at `:40`; my first narrow read mis-rendered a
  leading blank) — the entry's citations at `pastoralism-animal-husbandry.md:6,:51,:177` are correct as written.
- The four new D rows and C's entry are other seats' scope; nothing here pre-judges them.

Author-lane advice, not admission.
