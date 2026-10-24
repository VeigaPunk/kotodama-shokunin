# ScoutGapScent — claim-C gap verification at base `94209e8f80969dbac48d56c5d0e2e623635b8616`

Lane working-tree HEAD == base (jj-colocated; `git rev-parse HEAD` → `94209e8f…8616`), so working-tree greps measure the same tree as the frozen base.

## 1) Filename census at base — expect 0, got 0

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && git ls-tree -r --name-only 94209e8f80969dbac48d56c5d0e2e623635b8616 -- corpus/knowledge | grep -ciE '(^|[^a-z])(scent|perfume|aromatic|incense|fragran|cosmetic|unguent)([^a-z]|$)'
0
```
(grep exits 1 on zero matches — count is authoritative.) **No file in any of the six partitions owns the register by name.** Corpus is 239 `.md` files, culture-material partition 32 — consistent with claim's 239→240 / 32→33.

## 2) Topic-line sweep — every owner, disambiguated

Naive sweep (as briefed):
```
$ grep -rniE '^-?\s*topic\s*:.*(scent|perfume|aromatic|incense|fragran|cosmetic|unguent|odor|smell)' corpus/knowledge/
7 matches in 7 files:
  civilizations/vietnam.md:2        — FALSE POSITIVE: "Austroasiatic descent" (substring 'scent' inside 'descent')
  linguistics/kinship-terminology.md:3 — FALSE POSITIVE: "descent" ×12
  myth-symbol/sacred-kingship-mythic-charter.md:3 — FALSE POSITIVE: "divine descent" ×5
  culture-material/adornment-body-codes.md:3   — real hit: 'cosmetic'
  culture-material/craft-artisan-lexicon.md:3  — real hit (fragrance/scent/smell in body §119)
  culture-material/timekeeping-instruments.md:3 — real hit: 'incense'
  culture-material/vessel-container-lexicon.md:3 — real hit: 'cosmetic'/'perfume'
```

True partial owners (word-boundary verified, `\b[a-z]*(scent|perfume?|aromatic|incense|fragran|cosmetic|unguent|odor|smell)[a-z]*\b` minus `*descent*`):

| File | Scope of mention | Partial scope? |
|---|---|---|
| `culture-material/adornment-body-codes.md` (21 tokens) | §70–75,110: cosmetic as a *body-code column* — kohl/galena palettes, Ovid *Medicamina*, *cerussa*/*fucus*, four-strata cosmetic lexicon (material/tool/occasion/moral slur). Owns the body-substrate end; scent is absent. | YES — grooming/paint, not the aromatics register |
| `culture-material/timekeeping-instruments.md` (5) | topic + §2 FIRE family: "calibrated candle, lamp and incense measures" — incense only as burn-rate fuel for clocks. | YES — measurement use, not aromatic/ritual code |
| `culture-material/vessel-container-lexicon.md` (7) | topic "ritual/cosmetic/funerary extensions"; §38 containers for unguents/perfume; §158 cosmetic inventory row. | YES — the container, not the contents |
| `culture-material/craft-artisan-lexicon.md` (5) | §119: "a temper line's mist is its *scent* (nioi)" + 'fragrance'/'smell' — sensory-borrowing metaphor for steel quality. | YES — metaphor only |
| `civilizations/vietnam.md` (1 real token) | :165 "rather than cosmetic…" incidental adjective. | incidental |

Body-text census across all 239 entries: 63 files carry ≥1 real token (top: adornment 21, celts 15, fire-fuel-light 8, carthage 8, vessel 7, islamic-caliphate 7, funerary 6, timekeeping 5, craft 5) — **all incidental or adjacent-scope; no topic line claims the scent/perfume/aromatics register and no file names it.** `fire-fuel-light.md`, `bathing-and-body-hygiene.md`, `funerary-material-culture.md`, `islamic-caliphate-arabic.md`, `celts.md`, `carthage.md` are adjacency evidence, not owners.

## 3) Sibling-lane ownership — none

```
$ grep -rliE 'perfum|incense|aromatic|scent' /home/vgpnk/Projects/shokunin/lore-shokunin /home/vgpnk/Projects/shokunin/chousa-shokunin 2>/dev/null | head -5
lore-shokunin/corpus/fixtures/r87-myth-cluster/inspiration-note.md
lore-shokunin/corpus/fixtures/r93-m2-kojiki-cluster/README.md
lore-shokunin/corpus/knowledge/reference-ledger.md
lore-shokunin/corpus/knowledge/r94-cross-myth-design-comparison.md
lore-shokunin/corpus/SOURCES.md
```
Word-boundary re-scan of every match outside `.ufo/`: **all hits are the substring 'scent' inside 'descent'** (incl. chousa's two `.ufo` files: `r29/falsify/MutQuoteMap/receipt-mutant.json`, `r33/w2/ProbeNestedOnly33.md`). Zero true scent/incense/perfume/aromatic tokens in either sibling lane — no sibling owns or even documents the register; lore handoff is a clean open target.

## Registry tail (for the 24-row append S777–S800)

`corpus/SOURCES.md`: 701 `| S` rows, max id **S775** (S776 is the declared games-entry re-point in NOHARM). Rows are 11 cells: `| Snnn | citation+live+archive URLs | type | tier A/B | scope | anchor quote | teaches | mined | opened | review window | used-by |`. Next free ids: S777–S800 — exactly the claim's allocation. New rows need live URL + same-page `web.archive.org` capture (or explicit no-capture reason), ≥10 distinct normalized hosts, each cited exactly once by the entry.

## Build order for `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` (5 lines)

1. **Register map** — H1 + `- topic:` block; partition the register into five classes: sacred/ritual incense (fumigation, offering, temple protocol), personal fragrance & cosmetics (unguents, perfumed oils, body scent), trade/materials (resin/incense-route commodities, aromatics as cargo), timekeeping/measurement (incense clocks, burn-rate units), social codes (scent as rank, hospitality, taboo, gift).
2. **Source-grounded bullets by class** — mine registry S777–S800 (24 rows, tier A/B, ≥10 hosts, opened 2026-10-24, used-by this entry); each bullet cites exactly one S-id once, keeps ≥3 in-order anchor words, <80% teaches coverage, ≥1 novel word; ≥1 row per class, sacred/ritual and trade/materials heaviest.
3. **Cross-cultural patterns** — the recurring isomorphisms (smoke rising = message to the above; scent invisible-yet-detectable = presence/rank marker; aromatics = high value-per-weight long-distance cargo; burn-rate = cheap timer) stated as method, not canon.
4. **Design protocol + calibration + one-way pointing** — a fill-the-table protocol per culture; recheck/to-verify list per house rule; `- couples:` and inline pointers one-way to partial owners (adornment owns the body, vessel owns the container, timekeeping owns the FIRE clock, craft owns the metaphor — this entry owns the register itself).
5. **Lore handoff** — closing handoff section (what fiction may take, nothing canon-deciding), `- verified-at:` discipline lines, and the `corpus/README.md` index row quoting `- topic:` verbatim (TOPIC leg).
