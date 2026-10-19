# K01 — cartography gap recheck (claim C): still unowned at HEAD 6e9a30d

- Seat: K01 | role: scout | claim: C | date 2026-10-19
- Baseline: `git rev-parse HEAD` → `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`; equals `reports/round-47/claims.json:7` `baseline_commit`.
- Worktree: `git status --porcelain` → only `?? reports/round-46/review/` and `?? reports/round-47/`; no tracked modification, no corpus delta at recheck time.
- Seed under recheck: `reports/round-44/scout/K02-gap-scout.md`, sha256 `a72fff27ee193cc12e689b5a3b485d3c0389bd4317b7810abf745ee441f335f6` (433 lines, filed round-44 bytes; not edited by this seat).
- Out path: `reports/round-47/scout/K01-gap-recheck.md` (this file).
- Mission: re-verify that the cartography gap is STILL unowned at HEAD `6e9a30d` by a fresh filename + topic-line sweep at the live 223 total; confirm it is not a carried topic by grepping all prior `reports/round-*/scout/` for `cartograph|mapmaking` proposals. Report commands and outputs.

**Verdict in one line:** the gap is **FRESH at `6e9a30d`** — 223 entries, culture-material 25, the proposed slug absent, and **0 owners by filename, topic line, header field, or H1 title**; no prior round ever claimed, drafted, or landed it. One wording caveat: `reports/round-44/scout/K02-gap-scout.md` is itself a prior-round scout file that names the gap, so the claim's literal phrase "0 prior-round proposals" is true only relative to r44 — see §6.3. This does not change the ownership verdict.

## Verdict table

| Test | Measured | Evidence |
|---|---|---|
| Total entries at HEAD | **223** | §1 |
| culture-material entries | **25** | §1 |
| Proposed slug exists | **no** | §2 |
| Filename owners | **0** | §2 |
| Topic-line owners | **0** (11 metaphor/verb hits, all dispositioned) | §3 |
| Header-field owners (`gap`/`gap filled`/`scope`/`couples`) | **0** | §4 |
| H1-title owners | **0** (2 dialect-map titles, not cartography) | §4 |
| Genuine cartographic footprint | 7 files (seed headline 9 lines; tight replay 10, incl. one false positive), all by-product or handoff | §5 |
| Prior-round *claim* proposals | **0** | §6 |
| Prior-round *scout naming* | **1** — r44 K02, the cited seed | §6 |
| Ever drafted or landed | **no** (r44 validation: C UNCHANGED, 223) | §6.2 |
| Verdict | **FRESH (ownership)**; carried-wording caveat | §6.3 |

---

## 1. Baseline measured, not asserted

Commands run from the lane root on 2026-10-19 (`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

```text
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git log -1 --format='%ci %s'
2026-10-19 14:46:42 -0300 round-46: loop-1 retrospective — 9 admitted / 4 honest-stops / 1 skipped (argon); defects + provider amendments carried to loop 2
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
```

Per-partition vector and arithmetic:

```text
civilizations    94
culture-material 25
linguistics      25
myth-symbol      26
synthesis        29
verification     24
sum              223
```

Read-only index sweep (its only writes are disposable `.scratch` mirrors for planted controls, `reports/round-28/readme/sweep.py:257,397`):

```text
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_live {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
```

Independent inventory agrees:

```text
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
"totals": { "files": 223, ... }
"read_only": true
```

The `readme_sha256` is the same digest K02 read at `c9f4eaa` (`reports/round-44/scout/K02-gap-scout.md:47`), so the index has not changed between the seed's baseline and this recheck.

## 2. Filename ownership: 0

Exact K02 ownership pattern, re-run at `6e9a30d`:

```text
$ find corpus/knowledge \( -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' \) -type f | wc -l
0

$ find corpus/knowledge -name 'cartography*' -o -name '*mapmaking*' | wc -l
0

$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access 'corpus/knowledge/culture-material/cartography-and-mapmaking.md': No such file or directory
```

A deliberately broader family sweep (`*map*`, `*chart*`, `*atlas*`, `*itinerar*`, `*topograph*`, `*survey*`) returns three basenames, all false positives:

| Basename | Why it is not an owner | Re-read at HEAD |
|---|---|---|
| `synthesis/dialect-faction-map-workflow.md` | "Map" is a verb — map dialect features onto networks; its `- topic:` is a lect workflow | `:2` |
| `myth-symbol/sacred-topography-pilgrimage.md` | `*topograph*` is the **place register** (holy sites, routes), not map production; nearest neighbour, §5 | `:3-5` |
| `myth-symbol/sacred-kingship-mythic-charter.md` | `*chart*` matches inside "charter" | — |

No corpus basename carries the domain vocabulary.

## 3. Topic-line ownership: 0

Exact K02 pattern, re-run at `6e9a30d`:

```text
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|itinerar|survey|topograph|\bmap\b|\bcharts?\b)' corpus/knowledge --include='*.md' | wc -l
11
```

The same eleven hits as `K02-gap-scout.md:122-136`; every one is a metaphor, a verb, or a different sense of "survey":

| Entry:line | The hit | Disposition |
|---|---|---|
| `linguistics/sound-symbolism.md:3` | "the three-way **map** (arbitrariness / iconicity / systematicity)" | metaphor — a conceptual schema |
| `linguistics/dialect-register-consistency.md:3` | "a built **dialect map**'s internal consistency" | metaphor — a lect inventory |
| `linguistics/sacred-registers-liturgical-language.md:3` | "how ritual events **map** to the competences" | verb |
| `myth-symbol/number-symbolism.md:3` | "a variance **survey**" | statistical sense |
| `myth-symbol/purity-pollution-boundary-systems.md:4` | "purity is … a **boundary map**" | metaphor — that entry's master claim |
| `myth-symbol/sacred-topography-pilgrimage.md:5` | "sacred-geography **mapping** … as a diagram: radial, quartered, linear-corridor, or archipelago" | **nearest neighbour**; owns the sacred place register and route, not the survey→sheet chain (§5) |
| `culture-material/ritual-garments.md:3` | "the b.Arakhin 16a **atonement map**" | metaphor |
| `synthesis/dialect-faction-map-workflow.md:2` | "**Map** dialect features … onto travel networks" | verb |
| `civilizations/finnic-sami.md:3` | "gákti as an **identity map**" | metaphor |
| `civilizations/mesoamerica-primary-sources.md:3` | "a reference **map** for the four Mesoamerican bases" | metaphor |
| `civilizations/africa-primary-sources.md:2` | "a bounded **source map**" | metaphor |

**No entry names mapmaking as its subject.** 11 hits, 0 owners.

## 4. Header-field and title ownership: 0

No entry's `- gap:`, `- gap filled:`, `- scope:`, or `- couples:` field names cartography/mapmaking/portolan/survey maps:

```text
$ grep -rniE '^- (gap|gap filled|scope|couples):.*(cartograph|mapmak|map-mak|survey map|portolan)' corpus/knowledge --include='*.md'
(no output; exit 1)
```

H1 title check:

```text
$ grep -rniE '^# .*(cartograph|mapmak|map-making|\bmap\b|\bmaps\b|survey|portolan|atlas|itinerar)' corpus/knowledge --include='*.md'
corpus/knowledge/linguistics/dialect-register-consistency.md:1:# Lect formation and drift mechanics: ... what a built dialect map must not contradict
corpus/knowledge/synthesis/dialect-faction-map-workflow.md:1:# Dialect–Faction Map Workflow: Geography, Registers, and Social Boundaries
```

Both titles are dialect/lect workflows, not cartography. 0 title-level owners.

## 5. Demand footprint at HEAD (measured, with the small numbers stated)

Term-level counts, re-measured at `6e9a30d` with `grep -riF` over `corpus/knowledge/**/*.md`:

| Term | Files | Lines |
|---|---|---|
| `cartograph` | 2 | 2 |
| `mapmaking` | 0 | 0 |
| `portolan` | 0 | 0 |
| `cadastral` | 2 | 2 |
| `mappa` | 2 | 2 |
| `survey map` | 1 | 1 |
| `compass rose` | 1 | 1 |
| `graticule` | 0 | 0 |
| `theodolite` | 0 | 0 |
| `lienzo` | 1 | 4 |

File:line hits (tight pattern plus the seed's navigation/timekeeping rows), all re-read live:

| Entry:line | What it says | Why it is not ownership |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md:71` | "Hereford Mappa Mundi c. 1300; T-O diagrams are symbolic, **not survey maps** (§10)" | The partition's own disclaimer of the survey-map register |
| `myth-symbol/cosmology-cosmography.md:102` | "T-O diagrams are symbolic devices, **not cartographic** claims" | Same disclaimer in the flat-earth calibration |
| `civilizations/mesoamerica-primary-sources.md:58` | "Lienzos and **cartographic histories** … cloth maps/migration-conquest accounts" | Owns the source-survival/provenance class; one inventory row (supporting: `:28`, `:42`, `:46`) |
| `civilizations/japan-medieval-sengoku.md:157` | "a neat Edo **cadastral map** must not be treated as a direct Sengoku map" | A periodization caution |
| `culture-material/architecture-settlement-lexicon.md:95` | "surveyed with the **groma** … The grid is **cadastral**: a state that measures land builds this city" | Owns the built city plan; the survey step is a handoff |
| `myth-symbol/direction-symbolism.md:26` | "never as a **compass rose** with a legend" | Explicitly disclaims the map convention; `:51` owns the true-vs-magnetic "compass trap" |
| `civilizations/polynesia-navigation.md:52,60,63` | "**horizon compass**, ordered **steering-star** sequence, … **latitude/landfall** clue"; "a mental bearing framework, **not a chart**" | Owns navigation operations |
| `culture-material/timekeeping-instruments.md:50` | "longitude at sea" | One cell in a timekeeping table |

**The genuine footprint is seven files** (`K02-gap-scout.md:151-162`, reproduced file-for-file at HEAD); every occurrence above is a by-product or explicit handoff, and none is an owner.

Two inherited number notes, both count-preserving, from re-measuring the seed's §3.4 at HEAD:

- `cartograph` really is **2 files / 2 lines**, but they are `cosmology-cosmography.md:102` and `mesoamerica-primary-sources.md:58` — not `:71` as the seed's parenthetical says (`:71` says "survey maps"; the string `cartograph` is absent there).
- `mappa` really is **2 files / 2 lines**, but the second is `mineral-stone-symbolism.md:9` (`Mappae Clavicula`, a workshop-recipe title — a false positive), not `cosmology-cosmography.md:102` as the seed's parenthetical says. The seed's `cadastral` (2/2), `lienzo` (1/4), `survey map` (1/1), and `compass rose` (1/1) attributions reproduce exactly.
- The seed's headline "7 files / 9 lines" is not a single-regex count: replaying its tight pattern returns **10 lines in 6 files** (the extra is the `Mappae Clavicula` false positive), and that pattern does not catch the Polynesia/timekeeping prose the seed's own table counts. The stable facts are the **seven-file set** and the by-product disposition; the exact line count is probe-dependent.

The demand is low in raw mentions and is stated rather than hidden: this is a named-but-unbuilt register, the same structural shape as the r42 lithic gap — the partition's own method file draws a distinction and leaves one side unowned. The distinction is `cosmology-cosmography.md:71/:102`: symbolic world diagrams are owned; survey maps are explicitly not. The corpus owns every adjacent production system (writing surfaces, instruments, measurement, route maintenance) but never the map that combines them.

## 6. Prior-round audit and carried-topic adjudication

### 6.1 Commands

All existing round directories except this round and r44 (the seed round):

```text
$ dirs=$(ls -d reports/round-*/ | grep -vE 'round-(44|47)/$'); echo "$dirs" | wc -l
40
$ grep -rniE 'cartograph|mapmak|map-mak' $dirs
(no output; grep_exit=1 — zero hits)
```

The 40 scanned directories are rounds 5–43 plus round 46. Round 45 does not exist (`ls: cannot access 'reports/round-45': No such file or directory`); rounds 1–4 have no report directories (the earliest is `reports/round-5/`). The r44 round was checked separately and is the only one with hits.

All scout directories, including r47:

```text
$ find reports -maxdepth 2 -type d -name scout | wc -l
13
$ grep -rliE 'cartograph|mapmak|map-mak' reports/round-*/scout/
reports/round-44/scout/K02-gap-scout.md
```

Outside the seed and this round's own declarations (`reports/round-47/claims.json`, `targets.json`, `telemetry/dispatch-declared.json`), the only prior-round **proposal** is r44 K02; the other r44 files that mention it (`cross/X01-trades.md`, `cov/C05-collision.md`, `cov/C06-scribe.md`, `adj/A01-scope.md`, `review/R01-review.md`, `review/R02-review.md`, `scribe/S01-integration-draft.md`, `validation.json`) are all downstream discussions of that seed, not independent proposals. Round 46 (the loop-1 retrospective) has zero cartography hits and does not claim a coverage gap (`reports/round-46/claims.json:26,39,53` are boundary/append-only/ledger audits).

### 6.2 What is on file

- `reports/round-44/scout/K02-gap-scout.md:85` — candidate screen: cartography **"not named in any registry; 7 global report hits, none a proposal"**, verdict SELECTED.
- `reports/round-44/scout/K02-gap-scout.md:207` — "the gap is fresh at HEAD `c9f4eaa` and is not carried from any prior round."
- `reports/round-44/scout/K02-gap-scout.md:218-220` — recommended slug `cartography-and-mapmaking.md`, sort position between `calendar-festival-systems.md` and `costume-semiotics.md`, culture-material 25 → 26, total 223 → 224.
- `reports/round-44/validation.json:9` — "C: UNCHANGED — total 223 (no landing) … the fresh gap (cartography, K02) has no entry body. No corpus delta; coverage holds at 223."
- `reports/round-44/validation.json:88` — "cartography is fresh but undrafted."
- `reports/round-44/claims.json:39` — the r44 claim was **generic** ("a gap with NO current owner … verified by a fresh absence sweep at the 223 total"); it did not name cartography. The drafted r44 candidate was dream/vision/trance.

So across the whole history: cartography is named exactly once in a prior-round scout (r44 K02), never in a prior claim, never drafted as an entry body, never landed.

### 6.3 Adjudication — "unowned" is clean; "0 prior-round proposals" needs precise wording

Two senses of "carried" are in play, and the record should not conflate them:

1. **Ownership sense (the operative freshness test).** Zero owners and zero prior landings/drafts. **Green.** The seed's measured result reproduces at a new HEAD with identical term counts and an identical README digest.
2. **Literal registry sense.** K02's own screen defines a candidate as carried if "any prior round's scout/gap/plan registry already named it" (`K02-gap-scout.md:66`). At r44, "prior" meant rounds 1–43 and the answer was 0. At r47, r44 K02 is a prior-round scout file that names cartography. Therefore `claims.json:26` ("no prior-round proposal") and the threshold's "confirmed 0 prior-round proposals" are **literally false at r47** unless they are read as "no proposal before r44 K02." The count is: **0 prior-round claim proposals; 1 prior-round scout naming (r44 K02, the cited seed).**

Why this is materially different from the r44 dream failure class: dream was named r42 K02 R2 and then re-proposed at r44 *with a full draft*, despite K02 screening it "carried — reject" (`K02-gap-scout.md:78`). Cartography was named once, selected as the fresh candidate, never claimed, never drafted, never landed. The failure mode the round rule targets — re-proposing a rejected/carried topic without new measurement — does not apply, and this seat has re-measured at a new HEAD rather than inheriting the r44 numbers.

**Recommendation to the integrator/reviewers (advisory, not a corpus blocker):** record the provenance as "no cartography proposal before r44 K02; r44 K02 is the cited seed and was never drafted or landed." If the strict K02 §2 definition is applied at r47, then the round should name r44 K02 as an explicit provenance exception (the same kind of named exception r44 was asked to record for dream), not claim "0 prior-round proposals" without qualification. Either formulation leaves the ownership verdict and the landing eligible.

## 7. Landing-path collision check

```text
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
No such file or directory

$ ls corpus/knowledge/culture-material/*.md | wc -l
25

$ ls -1 corpus/knowledge/culture-material/*.md | xargs -n1 basename | sort | nl
5  calendar-festival-systems.md
6  costume-semiotics.md
7  craft-artisan-lexicon.md
```

With the proposed entry inserted, the verified order is `calendar-festival-systems.md` (5), `cartography-and-mapmaking.md` (6), `costume-semiotics.md` (7). The file is new, so the landing is an **A** (add), not an **M** (modify); no existing entry is overwritten. Partition effect: culture-material 25 → 26, total 223 → 224, partition sum `94+26+25+26+29+24 = 224`.

README state at HEAD (the C09 seat owns the edit; this is the collision/count confirmation only):

- `corpus/README.md:5` — `revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19)`.
- `corpus/README.md:548` — `(total 223 files; directory totals 25/26/25/29/24/94).`
- `corpus/README.md:10-11` — rev-2.4 prose says "the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**". Arithmetic: `25+23+26+25+24+94 = 217`, not 223. The counts footer is correct at 223. This confirms the pre-existing prose-vector defect the C claim says rev 2.5 must repair; the repaired prose vector must sum 224 after the landing. This seat did not edit README.

## 8. Machine-readable verdict

```json
{
  "seat": "K01",
  "claim": "C",
  "head": "6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe",
  "baseline_commit_matches": true,
  "total_md": 223,
  "partition_counts": {
    "civilizations": 94,
    "culture-material": 25,
    "linguistics": 25,
    "myth-symbol": 26,
    "synthesis": 29,
    "verification": 24
  },
  "proposed_slug": "corpus/knowledge/culture-material/cartography-and-mapmaking.md",
  "slug_absent": true,
  "filename_owners": 0,
  "topic_line_owners": 0,
  "header_field_owners": 0,
  "h1_title_owners": 0,
  "genuine_footprint_files": 7,
  "genuine_footprint_lines_seed_headline": 9,
  "genuine_footprint_lines_k01_tight_replay": 10,
  "k01_replay_extra_hit": "mineral-stone-symbolism.md:9 (Mappae Clavicula — false positive, not cartography)",
  "prior_round_claim_proposals": 0,
  "prior_round_scout_namings": 1,
  "prior_round_scout_naming_path": "reports/round-44/scout/K02-gap-scout.md",
  "prior_draft_or_landing": false,
  "landing_class": "A",
  "landing_effect": {"total": [223, 224], "culture_material": [25, 26]},
  "verdict": "FRESH-OWNERSHIP",
  "caveat": "literal '0 prior-round proposals' holds only relative to r44; r44 K02 is the cited, never-landed seed"
}
```

## 9. Command transcript (trimmed, all at HEAD 6e9a30d, 2026-10-19)

```text
$ git rev-parse HEAD                                      -> 6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git status --porcelain                                  -> ?? reports/round-46/review/ ; ?? reports/round-47/
$ find corpus/knowledge -name '*.md' | wc -l              -> 223
$ ls corpus/knowledge/culture-material/*.md | wc -l       -> 25
$ python3 -B reports/round-28/readme/sweep.py             -> rows 223 files 223; totals_ok True; footer_ok True; exit 0
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
                                                          -> totals.files 223; read_only true
$ find corpus/knowledge \( -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' \) -type f | wc -l
                                                          -> 0
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
                                                          -> No such file or directory
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|itinerar|survey|topograph|\bmap\b|\bcharts?\b)' corpus/knowledge --include='*.md' | wc -l
                                                          -> 11 (all metaphor/verb, table §3)
$ grep -rniE '^- (gap|gap filled|scope|couples):.*(cartograph|mapmak|map-mak|survey map|portolan)' corpus/knowledge --include='*.md'
                                                          -> no output; exit 1
$ grep -rniE '^# .*(cartograph|mapmak|map-making|\bmap\b|\bmaps\b|survey|portolan|atlas|itinerar)' corpus/knowledge --include='*.md'
                                                          -> 2 dialect-map titles; 0 cartography
$ grep -riF '<term>' corpus/knowledge --include='*.md'    -> term counts table §5 (counts reproduce K02 §3.4; two parenthetical line attributions in the seed are off — §5 notes)
$ grep -rniE '(cartograph|mapmak|portolan|cadastr|mappae|mappa mundi|surveyor|theodolit|compass rose|graticule|hereford mappa|lienzos?|stick chart|star chart|world map|drawn map)' corpus/knowledge --include='*.md'
                                                          -> 10 lines in 6 files; the extra over the seed's 9 is mineral-stone:9 "Mappae Clavicula" (false positive); seven-file footprint comes from the union with polynesia/timekeeping probes; table §5
$ dirs=$(ls -d reports/round-*/ | grep -vE 'round-(44|47)/$'); grep -rniE 'cartograph|mapmak|map-mak' $dirs
                                                          -> 0 hits; grep_exit=1; 40 dirs (rounds 5-43, 46)
$ grep -rliE 'cartograph|mapmak|map-mak' reports/round-*/scout/
                                                          -> reports/round-44/scout/K02-gap-scout.md only
$ python3 -c "print(sum([25,23,26,25,24,94]), sum([25,26,25,29,24,94]))"
                                                          -> 217 223 (prose-vector defect confirmed)
```

## 10. Limits and ownership of open items

- No network was used; no external source was inspected. The K02 tiered source shelf (Harley & Woodward, Harley 1989, Wood, Monmonier, Jacob, Ptolemy, Campbell, Kain & Baigent, Mundy, Boone, Pickles, Snyder, Dilke) is **not** audited here — that belongs to K02's seed extract and C06/C12.
- This seat measured ownership and landed state only. Post-landing confirmation (224, sweep green, no second owner) belongs to C05/V01; the README edit belongs to C09/W02.
- The demand footprint is a mention census, not a quality judgment; the "named-but-unbuilt, low raw demand" characterization is inherited from the seed's own honest framing (`K02-gap-scout.md:179,363`) and reproduced at HEAD.
- Rounds 1–4 have no report directories; their contents are reachable only through K02 §3.6's registry list (r19 gaps, r35, r39, r40, r42, r43), which this seat re-scanned as part of the 40 existing round dirs.
- Owed by this seat: none. Advisory only: state the r44 K02 provenance precisely in the integration record (see §6.3) rather than claiming "0 prior-round proposals" unqualified.
