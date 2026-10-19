# C04 — citation-anchor verification (claim C)

- Seat: `C04` | role: verifier | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19); `git status --porcelain` → `?? reports/round-46/review/`, `?? reports/round-48/` only
- Out path: `reports/round-48/cov/C04-citations.md` (this file)
- Read cut 1 (16:40 UTC): no C01/C02 draft fragment existed under `reports/round-48/` (`find reports/round-48 -type f` → `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`)
- Read cut 2 (19:44 UTC): `cov/C01-entry.md` (227-line fenced entry) and `cov/C02-header.md` (23-line fenced head block) exist; both are audited in §8. The assembled/landed entry still does not exist.

**One-line judgment.** The **citation baseline PASSES**: 55 anchor rows (56 line citations; README `:1` and `:3` share a row) across 16 in-repo files resolve at `a01405d`, every one to the content the seed/r47 review attributes to it, and 0 semantic mismatches. **C02's head block PASSES** (16/16 explicit refs, 19/19 couples, topic byte-equal to the K44 seed). **C01's body PASSES with two WARN-level anchor-precision findings and 0 HARD** (44/44 refs resolve; every arithmetic step recomputes; two calibration rows cite a line adjacent to, not containing, the words attached to it — §8.3). The two head blocks **disagree**, so the assembled entry is not yet determined (§8.4). I confirm all three r47 citation defects against live bytes (B2 count, B3 false accusation, B4 ladder) and add three new anchor-precision findings the draft must not reproduce: the writing-media **cost ladder is `:67-75`, not `:73`** (that is rung 3 alone), **`:81` is the survivor's-ledger heading**, not its content (`:83-95`), and **`:71` vs `:102`** carry different claims at cosmography (symbolic-not-survey vs flat-earth/Russell).

---

## 1. Method

For every anchor a right-sized cartography entry can inherit from `reports/round-44/scout/K02-gap-scout.md` §3.4/§3.5/§4.4 and from the r47 verified set in `reports/round-47/review/R03-c-content.md` §3.1/§4.2, I printed the **exact live line** at `a01405d` (`sed -n '<n>p'`), compared it to the proposition the citing text attaches to it, and ran verbatim `grep -c` tests for quoted phrases. No anchor below is carried from a prior round's assertion; each was re-read at this HEAD.

Two reference points are binding:

- `corpus/QUALITY.md:5-8` — every factual claim carries a checkable citation; unverifiable claims are marked `(to-verify)` inline, never laundered.
- `corpus/knowledge/verification/to-verify-triage-protocol.md:15` — the mark attaches "to the smallest uncertain proposition, not to a whole culture or bibliography."

The verification is line-exact, not file-exact: r47's B4 was a file-correct/line-wrong citation (`:44` is in the right file but is the steel row), and this seat's whole purpose is to catch that class.

## 2. Verified anchor set (55 anchor rows / 56 line citations, 0 mismatches)

Prefixes are verbatim; `…` marks my truncation, not the file's bytes. Three rows are explicitly marked `[summary]` where a byte prefix would be meaningless (a duplicate-heading pair, a two-row span, and a clause map).

```text
corpus/knowledge/myth-symbol/cosmology-cosmography.md
  :27   - **Cosmology** = the culture's tier-1 account of world structure and origin … **Cosmography** = the projected, inhabited version: how the world is drawn (maps) …
  :71   | Medieval Christian: T-O | east at top, Jerusalem center, three continents split by the T of waters | … Hereford Mappa Mundi c. 1300; T-O diagrams are symbolic, not survey maps (§10) | …
  :102  - Calibration: "everyone before Columbus believed in a flat earth" is a 19th-century fabrication (Russell 1991); … T-O diagrams are symbolic devices, not cartographic claims. …
  :133  - Toponyms are cosmographic claims: Teotihuacan glossed as "place where one becomes a god" … A fictional map is a set of etymological arguments — hand the derivation table to naming-systems.

corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md
  :5    - topic: the place register … the **route as rite** … sacred-geography mapping (a culture's holy sites as a diagram: radial, quartered, linear-corridor, or archipelago) …
  :69   - **The three route types.** (a) **Fixed itinerary** … (b) **Votive ramble** … (c) **Circuit / circumambulation** …
  :124  4. **Pick the route type** (§4: fixed itinerary, votive ramble, or circuit) and lay the stages.
  :167-168  - Egeria, *Itinerarium* … ; Petrarch, *Itinerarium ad sepulchrum domini* (`to-verify`); Ibn Jubayr, *Riḥla* and Ibn Baṭṭūṭa, *Riḥla* — translations … (`to-verify`).

corpus/knowledge/myth-symbol/direction-symbolism.md
  :51   - **The compass trap**: an abstract north requires deciding *which* north — true or magnetic — and their difference (declination) is latitude- and era-dependent. …

corpus/knowledge/culture-material/architecture-settlement-lexicon.md
  :95   - **Roman**: **castrum** grid → **cardo** … surveyed with the **groma**; … The grid is cadastral: a state that *measures land* builds this city.
  :97   - **Chinese**: the *Kao Gong Ji* … prescribes the ideal capital — nine li square … **Feng shui** 風水 … **form school** … vs **compass school** (**luopan** instrument …)
  :101  - **Design levers**: (a) give every planner culture an **instrument + founding rite + claim word** (groma/plough/pomerium; luopan/siting/kanyu; khittat allotment); …

corpus/knowledge/culture-material/writing-media-surface-economy.md
  :3    - topic: What a culture writes on, priced … the seven surface families … **a medium is three prices wearing a script's clothes** …
  :48   | **palm leaf / bark / cloth** | leaf cut, boiled, dried, smoothed; bark beaten; cloth sized | …
  :62   - **Consequence for the lexicon**: the sign-name vocabulary is usually a *tool* vocabulary … A culture that changes tools keeps the old names (the fossil) …
  :66   - **The claim**: for most of history the binding constraint on writing is not knowing the script, it is affording the surface. …
  :67   - **The ladder, from expensive to cheap, with what each rung buys:**
  :69   | rung | surface | who writes on it | register and genre it carries |
  :71   | 1 | stone, metal | the state, the temple, the lineage | the monumental register …
  :73   | 3 | papyrus (coarse), paper (early), cloth | the office and the merchant | the account, the contract, the register, the ledger |
  :75   | 5 | sherd, wall, slate, scrap | anyone, including the poor and the learning child | the ephemeral …
  :78   - **The two-way error to avoid**: (a) reading the expensive corpus as the culture's mind, when it is the culture's *budget*; … Cheapness widens the *base*, it does not redistribute the *authority*.
  :81   ## 5. The survivor's ledger — what the medium does to the future's evidence

corpus/knowledge/civilizations/mesoamerica-primary-sources.md
  :28     - [LIEN] Universidad Francisco Marroquín, [Quauhquechollan original versus digital restoration] … Inspected 2026-10-17; a current room-level Puebla location is not established here.
  :58   | Lienzos and cartographic histories (Quauhquechollan, Tlaxcala, Coixtlahuaca) | Cloth maps/migration-conquest accounts | … the copy chain is the evidence …

corpus/knowledge/culture-material/transport-mobility-lexicon.md
  :28   - **Craft rule**: a route is only real if someone maintains it. … If your fictional road has no maintenance clause, it is a description, not an institution.
  :35   - **Inca Qhapaq Ñan**: ~40,000 km, UNESCO World Heritage 2014; … the road starts at Cusco and radiates to the four *suyus*, so the network is a cosmogram with a logistics function. …
  :117  | DR-TR-02 | Require a maintenance clause (labor obligation, calendar rite, or tax) for every named route and bridge | … | adopted — no route ships without its upkeep rule |

corpus/knowledge/linguistics/naming-systems.md
  :40   - Onomastics splits by what is named: **anthroponymy** (persons), **toponymy** (places), **theonymy** (gods), and the transit layer … **name taboo and name magic** …
  :70   - **Critical toponymy** (Rose-Redwood, Alderman & Azaryahu 2010): naming is inscription of power; the street grid is a city-text. … Every renaming is datable; a map is an archive of coups.
  :97   | Korea (Joseon) | royal personal name avoided (국휘) … | ruler-name taboo as dynasty-spanning typography |

corpus/knowledge/civilizations/polynesia-navigation.md
  :52   - Distinguish **horizon compass**, **ordered steering-star sequence**, **large sky mnemonic**, and **latitude/landfall clue**; these are related operations, not synonyms.
  :63   | Kāpeʻa / Southern Cross | Cross observation contributes to southern direction and latitude assessment | …
  :72   - Different latitudes alter rising/setting bearings and visible sky; seasonal availability and changing course … 
  :74   - **Fictional application:** define a sky, latitude range, route, seasonal window, and cue-failure scenario …

corpus/knowledge/culture-material/timekeeping-instruments.md
  :50   | the minute | escapement clock, pendulum | medical dosing, meeting times, precise military orders | longitude at sea |

corpus/knowledge/civilizations/japan-medieval-sengoku.md
  :157  - Defensive approaches, commercial districts, temples, and residences can influence place naming, but a neat Edo cadastral map must not be treated as a direct Sengoku map.

corpus/knowledge/culture-material/craft-artisan-lexicon.md
  :3    - topic: the workshop as a speech community … (3) workshop organization across seven systems (Lehrling–Geselle–Meister …; London apprentice→journeyman→freedom→livery …)
  :44   | Steel (Japan) | **tamahagane** 玉鋼 "ball/jewel-steel" (tatara bloom); … — quality judged partly by its smell (Robinson 1961) |
  :54   | System | Apprentice | Journeyman | Master | Entry rite / mechanism |
  :56   | Germanic guild | Lehrling (learner) | **Geselle** "hall-companion" … | Meister | the **Meisterstück** masterpiece + feast + fees …
  :63   | (non-guild models) | Roman collegia: no formal ladder … — Benin: hereditary palace ateliers under the oba | …
  :65   - Design rule: pick a rung system and then break it deliberately — the masterpiece you can *buy your way around* …

corpus/knowledge/verification/calibration-registry.md
  :33-39  | Code | Calibration status | Permitted use / stop rule | … R / C / B / H / T rows (T = mark `(to-verify)` inline at the exact dependency)

corpus/QUALITY.md
  :5-20   [summary] Provenance (:5-8), Calibration (:9-12), Coupling (:13-15), Usability (:16-17), Canon hygiene (:18-20)

corpus/README.md
  :1,:3   [summary] "# kotodama-shokunin corpus index" twice (duplicate H1; `grep -c` = 2)
  :5      revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
  :11     the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**. …   [annotation: sums 217 — the rev-2.4 prose defect]
  :234    ## culture-material/ (25)
  :240-241  [summary] row `calendar-festival-systems.md`, then row `costume-semiotics.md` (cartography sorts between: "cal…" < "car…" < "cos…")
  :544    Total knowledge entries: 223.
  :548    (total 223 files; directory totals 25/26/25/29/24/94).

corpus/knowledge/synthesis/dialect-faction-map-workflow.md
  :2    - topic: … (lect workflow, not cartography)
  :3    - sources:
  :40   - **Register ledger:** `register_id | activity | speaker/addressee roles | access/training | repertoire | sanctions | exceptions | era`.
```

Per-file verification result: **16/16 files present (14 under `corpus/knowledge/`, plus `corpus/QUALITY.md` and `corpus/README.md`); 55/55 anchor rows line-exact; 0 semantic mismatches.**

Digests pin what I read (`sha256sum`, `a01405d`):

```text
165f292b95852459842900a091c6a40e1cd39b209b8fe2d84e62ecad6266ed2e  myth-symbol/cosmology-cosmography.md
241113b5a1259b04de889ebc458736ab8860e015b9afa9f74479bcc8bc165459  myth-symbol/sacred-topography-pilgrimage.md
5a6ef38fdec92e6db552cdd4e3d5f264cb19fb105d7881676ab73d86d3a35426  myth-symbol/direction-symbolism.md
9af04e751206c32bc1ca38a73ef16a27a3e2e4a696454dd1bb5e22ed27bada9f  culture-material/architecture-settlement-lexicon.md
f039e6e120ed050ff16adebc0ad5cd9cff7965337799fe7cbc725ba0823d4601  culture-material/writing-media-surface-economy.md
d04d8913e704961533d123857d87c93d8cfc25b89c854b1f6c3f5bcf1d0db530  civilizations/mesoamerica-primary-sources.md
86e5f9520e07e3ebb5d518183bb273d1ee8c22cca9c3ef1d35cf8fcef6d5aa70  culture-material/transport-mobility-lexicon.md
d972a1d65e7a8fba34f44e1cd57019c175a8ed24671ef95f3e0ea3d1ed9ffb3d  linguistics/naming-systems.md
fd678d82fcc5134f5c5c0a65b15106b35cabe67bfd935d45df4fa16524f30288  culture-material/craft-artisan-lexicon.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd  corpus/README.md
6aab8800986f37ca26a23ac8a0e3563e2dcb9f62975eb1c05e4a78d2b56f7bca  corpus/QUALITY.md
```

## 3. Verbatim quote tests

Every phrase below was tested with `grep -c` against the cited line (for the absence test at the last row, against the whole file); count 1 = present, 0 = absent.

| Phrase | Anchor | Count | Note for the draft |
|---|---|---:|---|
| `symbolic, not survey maps` | `cosmology-cosmography.md:71` | 1 | safe as a verbatim quote |
| `not cartographic` | `cosmology-cosmography.md:102` | 1 | safe; full phrase is "not cartographic claims" |
| `how the world is drawn (maps)` | `cosmology-cosmography.md:27` | 1 | the competing cosmography sentence; quote it, do not deny it |
| `compass trap` | `direction-symbolism.md:51` | 1 | safe |
| `a route is only real if someone maintains it` | `transport-mobility-lexicon.md:28` | 1 | safe |
| `The grid is cadastral` | `architecture-settlement-lexicon.md:95` | 1 | safe |
| `archive of coups` | `naming-systems.md:70` | **1** | **present** — r47 B3 confirmed |
| `archive of renamings` | `naming-systems.md` (any line) | **0** | **absent** — do not "correct" `coups` to this |

**r47 B3, re-confirmed live.** `grep -n 'archive of coups' corpus/knowledge/linguistics/naming-systems.md` → `70:… Every renaming is datable; a map is an archive of coups.` The quoted phrase is exact. Any draft or audit that replaces it with "archive of renamings" corrupts a correct citation. This is the single highest-risk recurrence in the citation class: a verifier's "correction" being the defect.

## 4. Miscite ledger — confirmed and new

### 4.1 Confirmed from r47 (all still live at `a01405d`)

| ID | Defect | Live measurement | Correct anchor / value |
|---|---|---|---|
| **B2** | gap count "2 files / 3 lines" is unreproducible | `grep -rli 'cartograph' corpus/knowledge/` = **2**; `grep -rni 'cartograph'` = **2** (`cosmology-cosmography.md:102`, `mesoamerica-primary-sources.md:58`) | **2 files / 2 lines**; `:71` is a "Mappa Mundi / survey maps" disclaimer and contains **no** `cartograph` token |
| **B3** | false accusation that `archive of coups` is not in the file | `grep -c 'archive of coups' naming-systems.md` = **1** at `:70` | keep `coups`; do not apply the "renamings" correction |
| **B4** | workshop ladder cited at `craft-artisan-lexicon.md:44` | `:44` = `\| Steel (Japan) \| **tamahagane** …`; ladder header `:54`, systems `:56-63`, design rule `:65` | cite **`:54-65`**; use `:44` only for material grading |

### 4.2 New precision findings (my seat; not in R03's list)

| ID | Finding | Evidence | Correct anchor |
|---|---|---|---|
| **C04-1** | The writing-media **cost ladder** cannot be cited as `:73`; that line is **rung 3 only** ("papyrus (coarse), paper (early), cloth"). | `:67` is the ladder lead-in, `:69` the table header, `:71-75` rungs 1-5. | **`:67-75`** for the ladder; `:73` only for the third rung. |
| **C04-2** | `writing-media-surface-economy.md:81` is the **section heading** "The survivor's ledger", not the ledger. A citation like ":81 lists fired clay…" is a heading/content mismatch. | `:83` the rule, `:86-95` the survivor table (fired clay `:88`, paper `:95`). | **`:81-95`** for the section; `:88` / `:95` for a row. |
| **C04-3** | `cosmology-cosmography.md:71` carries three distinct claims at one line number: the T-O row, "Hereford Mappa Mundi c. 1300", and the "symbolic, not survey maps" disclaimer. A draft citing `:71` for the *flat-earth* claim is off by one; that is `:102`. | `sed -n '71p'` vs `'102p'`; token matrix below. | `:71` = symbolic-not-survey + Mappa Mundi; `:102` = flat-earth fabrication + Russell 1991. |

Token matrix for C04-3:

| Token | `:71` | `:102` |
|---|---:|---:|
| `Mappa Mundi` | 1 | 0 |
| `survey maps` | 1 | 0 |
| `cartograph` | 0 | 1 |

## 5. Draft checker (run this against the assembled fenced body)

The integrator should run this on the assembled draft before applying it. It resolves every backticked `path:line(-line)` and flags a quoted phrase that does not occur inside the cited range. `HARD` = do not apply; `WARN` = human adjudicates (the quote may legitimately be a paraphrase).

```python
#!/usr/bin/env python3
"""C04 citation-anchor check. Usage: python3 c04-check.py <draft.md> [--strict]"""
import os, re, sys

CIT = re.compile(r'`((?:corpus/)?(?:[\w.-]+/)*[\w.-]+\.md):(\d+)(?:-(\d+))?`')
QUOTE = re.compile(r'"([^"\n]{12,})"')

def resolve(tok):
    return tok if tok.startswith('corpus/') else os.path.join('corpus/knowledge', tok)

def main(path, strict=False):
    text = open(path, encoding='utf-8').read()
    lines = text.split('\n')
    rows = []
    for m in CIT.finditer(text):
        tok, a = m.group(1), int(m.group(2))
        b = int(m.group(3) or a)
        p = resolve(tok)
        if not os.path.isfile(p):
            rows.append((m.group(0), 'HARD', 'file missing')); continue
        body = open(p, encoding='utf-8').read().split('\n')
        if not (1 <= a <= b <= len(body)):
            rows.append((m.group(0), 'HARD', f'range {a}-{b} vs {len(body)} lines')); continue
        seg = '\n'.join(body[a-1:b])
        src_line = lines[text[:m.start()].count('\n')]
        bad = [q for q in QUOTE.findall(src_line) if q not in seg]
        rows.append((m.group(0), 'WARN' if bad else 'OK',
                     ('quote not in range: ' + repr(bad)) if bad else ''))
    for r in rows:
        print('\t'.join(r))
    hard = sum(r[1] == 'HARD' for r in rows)
    warn = sum(r[1] == 'WARN' for r in rows)
    print(f'{len(rows)} refs; {len(rows)-hard-warn} OK; {warn} WARN; {hard} HARD')
    return 1 if hard or (strict and warn) else 0

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    sys.exit(main(args[0], '--strict' in sys.argv))
```

Sanity-tested at this seat on a fixture piped to the exact source above: it returns `OK` for `cosmology-cosmography.md:71` ("symbolic, not survey maps"), `WARN` for `naming-systems.md:70` ("archive of renamings"), `HARD` for a missing file and for `direction-symbolism.md:9999` (file has 203 lines), and `OK` for the range `craft-artisan-lexicon.md:54-65`.

**Known limitation.** For compressed multi-refs such as `path.md:3,:73,:78`, the regex resolves only the first number after the filename. The 44 refs in C01's body were audited with a separate multi-ref parser that carries the current filename across `:N` tokens; run both if the assembled body uses the compressed form.

## 6. Pass conditions for the C draft (my leg)

- **PASS** requires: every backticked `path:line` in the assembled body resolves (checker `HARD` = 0); every verbatim quote is present at the cited line; ranges point at the whole object cited (ladder `:54-65`, cost ladder `:67-75`, survivor's ledger `:81-95`); no `cartograph` count other than 2 files / 2 lines; no claim anchored to `:71` for flat-earth content.
- **A `WARN` is not automatically a fail** — a paraphrase should be marked as paraphrase, not quoted.
- **Automatic fail on recurrence:** quoting `archive of renamings`; citing `craft-artisan-lexicon.md:44` as the ladder; citing `writing-media-surface-economy.md:73` as the ladder; citing `cosmology-cosmography.md:71` as a `cartograph` hit.
- At read cut 1 (16:40 UTC) no draft existed; at read cut 2 (19:44 UTC) C01 and C02 exist and are audited in §8. The assembled/landed entry still does not exist, so the final leg remains **`could-not-evaluate` on assembled bytes** and **PASS on the anchor baseline + both filed fragments (C01 with two WARNs, §8.3)**. Run §5 on the assembled body before applying it.

## 7. What I did not verify

- **The draft's own citations, beyond the two fragments audited in §8.** C01's body and C02's header were audited; the body assembly (whether C01's fence, C02's fence, or a merge) was not determined at my cut. The checker in §5 is the instrument for the final bytes.
- **External bibliographic detail.** No network at seat time; every Tier-B edition/page in K02 §4.4 stays `(to-verify)`. I checked only that no draft presented it as inspected — vacuous at this cut.
- **Semantic fitness of each anchor** beyond "the line says what the citing text attributes to it." Whether a section *should* be cited is the content reviewer's call (R03/C12), not mine.
- **README apply arithmetic** (`223→224`, vector `25/26/26/29/24/94`) — C10/C11 and N01 own it; I verified only the live anchor lines `:234`, `:240-241`, `:544`, `:548` and that `25+26+25+29+24+94 = 223` (recomputed).
- **The couples-token resolution** (C09/A02). My table covers only file content at `path:line`, not the `- couples:` namespace form.

## 8. Post-cut audit of the filed drafts (read cut 2)

### 8.1 C02 header (`cov/C02-header.md`) — PASS

| Check | Result |
|---|---|
| Fenced head block | 23 lines exactly (`splitlines`), one physical line per field |
| Explicit `path:line` refs | **16/16 resolve** at `a01405d` (basename and repo-relative both) |
| Field set/order | `topic, gap filled, sources, couples, source, verified-at, recheck, scope` — 8 fields, contract-complete |
| `couples:` tokens | **19/19** resolve relative to `corpus/knowledge/culture-material/` |
| `- topic:` vs K44 seed | **byte-equal**; value sha256 `bc7274f411cc6977032ab2754ebff19def4a1f5240fe5882624fc76e744f4495` |
| Seed-line digest claim | C02 states `9424fb81c22fe8c9a468d75aa291e1b5943a268b8699320915de52d7bda3459a`; this reproduces **only with the trailing newline included**. Without it the digest is `a42926b1d0fe5ac5d608bb4ebd8e16873b3ed2f43a74c34392f0e4d5632496f8`. Note for the README row: copy the value, not the digest. |
| `- gap filled:` counts | 2 files / 2 lines for `cartograph`, `:71` correctly excluded as a `survey map` disclaimer; `mapmaking`/`portolan`/`graticule`/`theodolite` = 0 |
| Citations to reports | `reports/round-48/claims.json:21-24` (the `declared_after_freshness_gate` block) and `reports/round-44/validation.json:9` (the failures string containing "the fresh gap (cartography, K02) has no entry body") both resolve verbatim |
| Colophon claims | `reports/round-45/` absent (confirmed); `reports/round-46/` cartography hits = 0 (confirmed) |

### 8.2 C01 body (`cov/C01-entry.md`) — PASS, 0 HARD, 2 WARN

| Check | Result |
|---|---|
| Fenced entry | **227 lines** (`splitlines`; 228 when split on `\n` because the fence text ends with a newline), 215 body lines after the 11-line head block — matches C01's own count |
| Fenced-block sha256 | `2a66774974b80d9be2659a9e0e09a265114631c21189eae506acba5edfbdb3ca` — **matches** C01's claim exactly (recomputed on the extracted bytes) |
| Distinct `path:line` refs | **44/44 resolve** (multi-line forms `:3,:73,:78`, `:5,:69`, ranges `:54-65`, `:35-39` included) |
| Verbatim quotes | `naming-systems.md:70` "a map is an archive of coups" present; `cosmology-cosmography.md:27` "how the world is drawn (maps)" present; `:71` "symbolic, not survey maps" present; `:102` "not cartographic claims" present; `transport:28` maintenance rule present; `architecture:95` "surveyed with the groma"/"The grid is cadastral" present |
| B2/B3/B4 recurrence | none: 2 files / 2 lines; `coups` kept verbatim; ladder cited `:54-65` and `:44` explicitly excluded |
| Arithmetic (recomputed, all correct) | 1% × 100 paces × 0.75 m = 0.75 m; 0.2 mm × 5,000 = 1 m; 0.2 mm × 2,500 = 0.5 m; 1 arcmin at 10 km = 2.909 m; 0.2 mm × 50,000 = 10 m and 200/10 = **20×**; 111.3 km × cos 60° = 55.65 km; sec 60° = 2 and 1:1,000,000 → 1:500,000; 0.2 mm × 24,000/50,000/250,000 = 4.8/10/50 m; 1 cm × 50,000 = 500 m, ×250,000 = 2.5 km; 360/32 = 11.25°; 2,400 × 0.296 = 710.4 m and 710.4² ≈ 50.5 ha |

### 8.3 The two WARN-level anchor-precision findings in C01's body

Neither is a factual error; each is the r47 class of "right file, adjacent line," and each is a one-token fix.

| ID | Where | Finding | Fix |
|---|---|---|---|
| **C04-W1** | §12 calibration, flat-earth row: "T-O diagrams are symbolic, not survey maps (`cosmology-cosmography.md:102`; Russell 1991)" | The phrase "symbolic, not survey maps" is live **only at `:71`**. `:102` says "symbolic devices, not cartographic claims" (verified: phrase count at `:102` = 0, at `:71` = 1). The row is semantically true but the anchor does not contain the quoted wording. | cite **`:71,:102`** (or use `:102`'s own wording) |
| **C04-W2** | §12 calibration, rarity row: "rarity is a cost-and-warrant effect (`writing-media-surface-economy.md:73-78`)" | `:73` is **rung 3 only**; the cost ladder is `:67-75` and the authority rule is `:78`. The range clips the ladder's head. | cite **`:67-78`** |

Both of C01's other uses of this file are correct: the `- sources:` line calls `:73` the "register/ledger tier" (accurate), and `:78` is quoted as a rule ("cheapness widens the base, not the authority" — paraphrase, correctly unquoted).

### 8.4 Cross-fragment conflict: the two head blocks are not the same entry

C01's fenced block includes its own head block "so this file is independently loadable"; C02 files a different one. They cannot both be applied, and the divergence is at the anchor the sweep enforces.

| Field | C01 (`cov/C01-entry.md`) | C02 (`cov/C02-header.md`) | Conflict |
|---|---|---|---|
| H1 | "the survey-to-sheet register: the map as an argument about space, its forms, its silences, and the trade that makes it authoritative" | "the map as an argument about space: the survey chain, projection and scale, symbol grammar, reproduction, and the map's silences" | different strings |
| `- topic:` | 1,045 chars, sha256 `23d94f4122d6ab88dfb00e4422d59c53b5a4e76052c41cf275b28fd26a638a79` | 766 chars, sha256 `bc7274f411cc6977032ab2754ebff19def4a1f5240fe5882624fc76e744f4495` (**= the K44 seed value**) | **not byte-equal** |
| `- gap filled:` | 942 chars | 2,643 chars | different text, both measured |
| Fields | `gap filled, topic, sources, couples, verified-at, recheck, scope` (7) | `topic, gap filled, sources, couples, source, verified-at, recheck, scope` (8) | **C01 has no `- source:`** |
| Field order | `gap filled` first | `topic` first | different |

**Consequence, and it is a citation consequence, not a style one:** the sweep compares the README row text to the entry's `- topic:` value exactly (`reports/round-28/readme/sweep.py:139-140`). The README row must be copied from whichever head block is applied. Only C02's topic is byte-equal to the r44 K44 seed; C01's is a different, longer string. The integrator must **choose one head block and use its `- topic:` verbatim** — do not merge fields, and do not copy C01's topic into a README row built from C02's block (or vice versa). My citation leg does not decide which; it records that the choice determines the README row bytes.

### 8.5 Verdict after the post-cut audit

- **C02 head block:** PASS on citations and couples.
- **C01 body:** PASS on citations (0 HARD, 44/44 resolve) and on recomputed arithmetic; two WARN anchor fixes (C04-W1, C04-W2) before apply.
- **Assembly:** blocked on the head-block choice (§8.4), not on a citation defect.
- **Not re-audited:** C03/C05/C06/C07/C08/C09/C14/C15/M02/X00 and later fragments; their citations are their own seats' to certify. My §5 checker is the instrument for the final assembled body.

## 9. Commands and write surface

All commands run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```text
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ grep -rli 'cartograph' corpus/knowledge/ | wc -l
2
$ grep -rni 'cartograph' corpus/knowledge/ | wc -l
2
$ for t in mapmaking portolan graticule theodolite; do grep -rli "$t" corpus/knowledge/ | wc -l; done
0 0 0 0
$ grep -rni 'cadastr' corpus/knowledge/ | wc -l
2
$ grep -c 'archive of coups' corpus/knowledge/linguistics/naming-systems.md
1
$ grep -c 'archive of renamings' corpus/knowledge/linguistics/naming-systems.md
0
$ sed -n '44p' corpus/knowledge/culture-material/craft-artisan-lexicon.md
| Steel (Japan) | **tamahagane** 玉鋼 "ball/jewel-steel" (tatara bloom); ...
$ grep -n '| System | Apprentice' corpus/knowledge/culture-material/craft-artisan-lexicon.md
54:| System | Apprentice | Journeyman | Master | Entry rite / mechanism |
$ sed -n '67p;73p' corpus/knowledge/culture-material/writing-media-surface-economy.md
- **The ladder, from expensive to cheap, with what each rung buys:**
| 3 | papyrus (coarse), paper (early), cloth | the office and the merchant | the account, the contract, the register, the ledger |
$ sed -n '81p' corpus/knowledge/culture-material/writing-media-surface-economy.md
## 5. The survivor's ledger — what the medium does to the future's evidence
$ python3 -B reports/round-28/readme/sweep.py | tail -2
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
```

**Write surface:** this file only — `reports/round-48/cov/C04-citations.md`. No `corpus/**`, `tools/**`, `reports/round-1..47/**`, `tools/gates/frozen/**` or fleet `.ufo/**` byte was edited or staged; no git commit/push, no install, no network; `run-validation.py` was not executed. `git status --porcelain` at my write cut showed only the pre-existing untracked `reports/round-46/review/` and `reports/round-48/`.
