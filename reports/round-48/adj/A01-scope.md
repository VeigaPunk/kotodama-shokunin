# A01 — scope / bleed verification (r48)

- Seat: `A01` | role: verifier | claim: **cross** | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`), equal to `reports/round-48/claims.json:7` (`"baseline_commit": "a01405d"`)
- Out path: `reports/round-48/adj/A01-scope.md` (this file)
- Non-author statement: I drafted none of the C or Ca fragments and edited no corpus byte, tool, README, round file, or telemetry record. Every judgement below is from the live bytes at the baseline; commands are in §9. I wrote only this file, plus a disposable staged README copy under `.scratch/a01/`.

**One-line verdict.** Scope is clean at the baseline: PROVINCE is accurate against the live six-partition tree, the declared corpus delta is exactly two files (one new `culture-material` entry + `corpus/README.md`), the fresh gap is still unowned and honestly low-demand, and all 64 declared out paths stay inside `reports/round-48/`. I confirm **one live contract violation** (`reports/round-48/claims.json:49` orders an in-tree `run-validation.py` that the shared rule forbids and that does not exist) and **two pre-landing one-owner gaps** the C draft must close: `agrarian-field-system-lexicon.md` is in neither boundary surface, and the 8-row boundary table lags the 21-token `- couples:` line by 13 neighbors. Neither gap is a collision today; both become bleed if the entry restates those owners.

---

## 1. Measured baseline and write surface

| Check | Command | Result |
|---|---|---|
| HEAD | `git rev-parse HEAD` | `a01405dd…` (prefix `a01405d` = claims baseline) |
| Total entries | `find corpus/knowledge -name '*.md' \| wc -l` | **223** |
| culture-material | `ls corpus/knowledge/culture-material/*.md \| wc -l` | **25** |
| Partitions | `ls corpus/knowledge/<p>/*.md \| wc -l` | civilizations 94 / culture-material 25 / linguistics 25 / myth-symbol 26 / synthesis 29 / verification 24 = 223 |
| Index | `python3 -B reports/round-28/readme/sweep.py` | `rows 223 files 223`, missing 0, topic_mismatch 0, orphan_rows 0, header_drift {}, totals 223, footer `25/26/25/29/24/94`, **exit 0** |
| README sha | `sha256sum corpus/README.md` | `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` |
| Tracked-tree delta | `git diff --stat HEAD -- corpus/ tools/ examples/ LOG.md PROVINCE.md SCORECARD.md SHONEN.md` | **empty** |
| Untracked | `git status --porcelain` | `?? reports/round-46/review/` (mtime 2026-10-19 14:48:54 −0300, before the round's 19:45Z declaration) and `?? reports/round-48/` |
| Seat outs | parse `reports/round-48/targets.json` | **64 seats, 64 unique ids, 64 unique out paths**; all under `scout/ plan/ cross/ cov/ calib/ review/ adj/ scribe/ op/`; none absolute, none with `..`, none under `corpus/`, `tools/`, or `reports/round-1..47/` |
| Partition discipline | `python3` over `wc -l` | culture-material n=25, min 103, **median 149**, **max 221**, 0 files over 250 (so the claim's “live max is 221” is correct) |

At my write cut `reports/round-48/` held only `claims.json`, `targets.json`, and `telemetry/dispatch-declared.json` (`find reports/round-48 -type f`). No seat had filed a fragment yet, so write-surface conformance is **verified for the declaration, could-not-evaluate for the 63 other seats' eventual writes** (see §8).

## 2. PROVINCE accuracy (checked line by line)

| PROVINCE claim | Live evidence | Verdict |
|---|---|---|
| Domain: linguistic-cultural worldbuilding incl. “costume & material-culture terminology” (`PROVINCE.md:3-7`) | The round's only new corpus object is a material-culture production system (survey → sheet → copy); the culture-material partition is the made-object partition | **accurate and in domain** |
| Owns the six named partitions (`:9-14`) | `ls -d corpus/knowledge/*/` → exactly the six named, in the same order, summing to 223 | **accurate** |
| Owns “this lane's own gates, source-check records, non-canon examples and reports” (`:11`) | All 64 outs under `reports/round-48/`; the only tool-side proposal is Ca05's heading control (`reports/round-48/targets.json:37`), i.e. a lane gate | **accurate** |
| Refuses canon / rights rulings / game mechanics / general research method / web publishing / prompt craft (`:16-20`) | C is a reference-and-method entry with a `- scope:` and a NON-CANON example; Ca is an index-integrity fix plus a successor record; neither contract names a canon, rights, game, chousa, kake, or kotoba surface | **accurate for this round's contract** |
| Adjacent contract path (`:22-24`) | `corpus/knowledge/synthesis/worldbible-integration-contract.md` exists (28,421 bytes) and appears in the r47 draft's couples set | **accurate** |
| “Only writes this standalone lane repository” (`:27-29`) | `git diff --stat` on tracked files is empty; the only untracked trees are reports; no sibling/world-bible path is named anywhere in `claims.json`/`targets.json` | **accurate in-repo** |

**P3 note — a path ambiguity that could mis-seat a worker.** `PROVINCE.md:27` writes the repo as `kotodama-shokunin/`, but the repository root is the outer directory of that name; there is an empty vestigial tree inside it: `kotodama-shokunin/reports/round-29/defects/` (0 files, untracked, mtime 2026-10-18 18:10). Nothing in the r48 contract points there, so this is not a violation — but a seat that reads `PROVINCE.md:27` literally could write its fragment to `kotodama-shokunin/reports/…` and pass its own out-path check by accident. Owner: integrator; next touch: a PROVINCE wording fix or removal of the empty tree in a future calibration move. Not actioned this round.

## 3. The declared corpus delta is exactly two files

`reports/round-48/claims.json:29` and `reports/round-48/claims.json:43` name only two corpus objects; `targets.json` adds none. Verified against the live tree:

| Path | Change | Proof |
|---|---|---|
| `corpus/knowledge/culture-material/cartography-and-mapmaking.md` | **A** (new; slug unused, `ls` → No such file) | `find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' \| wc -l` → **0** |
| `corpus/README.md` | **M** (row + header + totals + footer + revision block + rev-2.4 prose-vector repair) | live anchors below |

README insertion is mechanically correct: the culture-material section is `## culture-material/ (25)` at `:234`, its 25 rows `:236-260` are **sorted**, and `cartography-and-mapmaking.md` sorts at insertion index **5**, between `calendar-festival-systems.md` (`:240`) and `costume-semiotics.md` (`:241`). Totals: `:544` 223, `:548` vector `25/26/25/29/24/94`; 223+1 = **224**, 25+1 = **26**, and `25+26+26+29+24+94` = **224**. The rev-2.4 prose vector at `:11` sums **217** (`25+23+26+25+24+94`), confirming the defect the claim orders repaired.

**No third corpus file is proposed anywhere.** The only other write targets in the contract are under `reports/round-48/` (fragments, successor row) and, for Ca05, a `tools/` gate — neither is a corpus object.

## 4. Cross-domain bleed: the one-owner surface

### 4.1 The gap is fresh and honestly framed

- **Filename owners: 0; topic-line owners: 0.** `grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|survey map|world map|graticule)' corpus/knowledge/ | wc -l` → **0**.
- **Term counts:** `cartograph` 2 files / 2 lines; `mapmaking` 0; `portolan` 0; `graticule` 0; `theodolite` 0; `cadastr` 2 files / 2 lines. The two `cartograph` lines are the cosmography disclaimer (`:102`) and the Mesoamerican source class (`corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58`) — the r47 R03 B2 correction is the honest form (“2 files / 2 lines”, not “2 files / 3 lines” or zero body mentions).
- **Partition fit is right.** `corpus/knowledge/myth-symbol/cosmology-cosmography.md:71` says T-O diagrams are “symbolic, **not survey maps**”; `:102` says they are “symbolic devices, **not cartographic** claims”; `:27` nevertheless defines cosmography as “how the world is drawn (maps)…”. The C draft must therefore say what R03 B8 requires: cosmography owns the world-drawn content (`:27`, `:71`, `:102`); the new entry owns the surveyed, projected, reproduced sheet. Without that sentence the one-owner claim is overstated; with it, there is no bleed.
- **No symbolic-register theft.** The map is a composition register over direction/name/number/colour; `corpus/knowledge/myth-symbol/direction-symbolism.md:51` (the compass trap) and `corpus/knowledge/linguistics/naming-systems.md:70` (toponymy as archive of coups) remain the owners, per the draft's own register-of-registers rule (`reports/round-47/cov/C01-entry-a.md:145`).

### 4.2 The boundary table lags the couples line by 13 neighbors

At r47, the authoritative boundary table has **8 rows** (`reports/round-47/cov/C01-entry-a.md:96-103`) while the header's `- couples:` line carries **21 paths** (`reports/round-47/cov/C04-entry-header.md:159`). All 8 table paths appear in couples; **13 coupled neighbors have no boundary row**: `calibration-registry`, `craft-artisan-lexicon`, `era-material-scoped-reconciliation`, `japan-medieval-sengoku`, `material-culture-inference-method`, `myth-consistency-gate`, `polynesia-navigation`, `real-world-inspiration-boundaries`, `timekeeping-instruments`, `trade-economy-lexicon`, `vessel-container-lexicon`, `worldbible-integration-contract`, `writing-systems`.

Three of these are prose-level bleed risks, not bookkeeping:

- **`agrarian-field-system-lexicon.md` — in neither surface.** It owns the field system's four institutions (parcel, implement, water, claim) and the work-unit land measures *jugerum/morgen/acre/hide/carucate* (`:4`, `:122`). The cadastral form is one of the entry's eight core forms, so an undispositioned cadastral section would restate a second owner's parcel/tenure vocabulary. This is the sharpest gap I found and it is **not** in R03's four-row list.
- **`timekeeping-instruments.md`** — coupled (`:50` “longitude at sea”) but not tabled. It owns the five instrument families including the astrolabe/nocturnal (`:3`). The survey chain uses those instruments; the entry must own only the *positional step and the coordinate problem*, not the instrument typology, resolution, or failure modes.
- **`vessel-container-lexicon.md`** (`:115`, containers as documents and chronometers) and **`material-culture-inference-method.md`** (`:69` perishability, `:76` anti-determinism guard) — coupled but not tabled. The map case/roll/archive and the “the map caused the state” claim are exactly the places a draft drifts into those owners.

R03 and C08 already owe two more rows from both surfaces: **`trade-economy-lexicon.md`** (metrology and split-object authentication, `:3`, `:17`, `:92`, `:121`; C08 P1-3) and **`myth-symbol/celestial-symbolism-calendars.md`** (planets `:53`, constellations `:70`, sky-to-calendar `:136`; C08 P1-4). One other body-cited path is missing from couples: `linguistics/numerals-and-measures.md` is cited twice in C01 (C01:145) but is absent from the 21 tokens — however that entry itself hands metrology to trade-economy (`corpus/knowledge/linguistics/numerals-and-measures.md:27`, `:35`), so the correct fix is the trade-economy row plus a one-clause note that the scale bar's unit is cited, not coined; a separate numerals row is optional.

### 4.3 Integration-ready boundary rows (fenced; each path and line verified by me at a01405d)

```markdown
| `culture-material/agrarian-field-system-lexicon.md` | the field system's four institutions — parcel, implement, water, claim — and the work-unit land measures *jugerum/morgen/acre/hide/carucate* (`:4`, `:122`) | the **cadastral sheet** as a produced document and the parcel unit it declares; this entry cites the agrarian measure vocabulary and does not restate tenure or land-measure etymology |
| `culture-material/timekeeping-instruments.md` | the five instrument families and the day they measure (`:3`), including the astrolabe and nocturnal, and "longitude at sea" (`:50`) | the **survey instrument as a step** in the map-production chain, and the coordinate problem the sheet inherits; this entry does not restate instrument typology, resolution or failure modes |
| `culture-material/vessel-container-lexicon.md` | containers as documents and as chronometers (`:115`) | the **map case, roll and archive chest** as storage, and what storage does to a map's survival; cited, not re-owned |
| `culture-material/material-culture-inference-method.md` | the inference ladder, the perishability constraint (`:69`) and the anti-determinism guard (`:76`) | the **survival and "the map caused the state"** claims — applied here, not restated |
| `myth-symbol/celestial-symbolism-calendars.md` | sky objects and planets-as-gods (`:53`), constellations and asterisms (`:70`), sky-to-calendar machinery (`:136`) | the **star chart as a produced document**; this entry does not restate the sky typology or the calendar mechanics |
| `myth-symbol/sacred-kingship-mythic-charter.md` | the eight legitimation channels and the regalia as found title-deed (`:3`) | the **legal-vs-mythic charter of a territorial map**; the map's warrant is cited to that entry's channels, not re-derived |
```

With these six plus C08's `trade-economy` row, the table reaches 15 rows, covering every *content* owner among the 21 coupled paths. The eight that would remain couples-only are `writing-systems`, `polynesia-navigation`, `japan-medieval-sengoku`, `calibration-registry`, `myth-consistency-gate`, `real-world-inspiration-boundaries`, `worldbible-integration-contract`, and `era-material-scoped-reconciliation`; the first three are genuine content edges (script/media bias, navigation-vs-chart, an era caveat) and should each get a one-line non-collision note in the entry, while the last five are handoff or calibration pointers. The right-sized entry can hold 15 rows plus three notes: that is well inside its ~250-line budget, and the r47 over-build was prose duplication, not table density (R03 §2.3).

## 5. Ca scope: index integrity, successor, control

### 5.1 The README fix is a live-index repair, not a rewrite of filed bytes

`corpus/README.md:1` and `:3` are byte-identical H1s (`grep -c '^# kotodama-shokunin corpus index'` → **2**). I staged the edit in `.scratch/a01/` (never in `corpus/`) by deleting line 3 only:

```
575 -> 574 lines; H1 count 2 -> 1
python3 -B reports/round-28/readme/sweep.py --readme .scratch/a01/README-no-dup-h1.md
rows 223 files 223; missing 0; topic_mismatch 0; orphan_rows 0; totals 223; footer 25/26/25/29/24/94; exit 0
```

So the removal is index-safe. Two scope constraints on the exact edit:

- **Leave no silent rewrite of a dated record.** `corpus/README.md:550-553` establishes the house practice for a wrong historical reading: “Superseded reading, **preserved as the dated record it was**”. The rev-2.4 prose at `:11` is such a record. The rev-2.5 edit should *annotate and supersede* it (e.g. an inline “corrected in rev 2.5: this vector was misstated; measured `25/26/25/29/24/94` = 223”), not silently replace the historical text. The claim's word “repaired” is acceptable only in that annotated form.
- **State the blank-line variant.** Deleting line 3 alone leaves two consecutive blank lines (staged lines 2-3). That is cosmetic and the sweep is green either way; Ca01 must say whether it removes line 3 alone or line 3 plus one blank, and Ca03 must verify the chosen bytes.

### 5.2 Ca05 must not patch the filed sweep

`reports/round-28/readme/sweep.py` is tracked and sits under the immutable `reports/round-1..47/**` prefix (`reports/round-48/targets.json:6`). The sweep has **no H1 check** (`grep -n "startswith(\"# \")\|H1\|title"` → no hits; its header controls only check `## <partition>/ (n)` counts). Therefore the heading control must be a **new** `tools/harness/readme-heading-count.py` (or a documented gate), never an in-place patch to the round-28 instrument. It should assert **both** that the H1 count is 1 **and** that the surviving H1 is at line 1: a count-only control would pass a README whose only title sits at line 3, which is not the defect's fix.

### 5.3 The over-build disposition is a successor record, not a parent edit

The r47 over-build class is genuinely undispositioned: `grep -n 'over-build\|790' reports/round-40/op/defect-queue-v2.json reports/round-43/calib/defect-queue-v2-successor-r43.json` → no row; the only mentions are `reports/round-47/review/R03-c-content.md:8,188,196` and the r48 declaration. The correct shape is a **new** successor file with the parent pinned by sha (the r43 successor's own convention: `schema`, `parent`, `parent_sha256_at_assembly`, `rows`), citing R03 B1-B9 (R03:188-196), the 739-body-line measurement (`R03:96`), and the failed validation state (`reports/round-47/validation.json`, `"acceptance_checks_passed": false`). Editing `reports/round-40/op/defect-queue-v2.json` or the r43 successor in place would violate the filed-bytes rule and destroy the pinned-sha guarantee.

## 6. Violations register

| ID | Severity | Finding | Evidence | Fix / owner |
|---|---|---|---|---|
| **V1** | **Blocking for Ca verification** | The Ca claim's third counting command orders an in-tree round-runner, directly contradicting the round's own ABSOLUTE rule, and the file does not exist. | `reports/round-48/claims.json:49` `"python3 reports/round-48/run-validation.py"` vs `reports/round-48/targets.json:8` “ABSOLUTE: never run reports/round-*/run-validation.py in-tree”; `ls reports/round-48/run-validation.py` → No such file | Replace with: `grep -c …` (already :47), `python3 -B reports/round-28/readme/sweep.py` (already :48), and “read the integrator-filed `reports/round-48/validation.json` **after** the parent runs it”. Integrator corrects the declaration; no seat executes it. |
| **V2** | Pre-landing (coverage/adjacency) | Boundary table 8 rows vs 21 couples tokens; `agrarian-field-system-lexicon` in neither surface; `timekeeping`/`vessel`/`material-culture-inference` coupled but untabled. | §4.2; `reports/round-47/cov/C01-entry-a.md:96-103`; `reports/round-47/cov/C04-entry-header.md:159`; `agrarian:4,122`; `timekeeping:3,50`; `vessel:115`; `inference:69,76` | Apply §4.3 rows (C-drafters/integrator). Not a collision today; becomes bleed if the entry restates those owners. |
| **V3** | Pre-apply (calibration honesty) | A silent in-place “repair” of the rev-2.4 vector would falsify a dated record, contrary to the README's own superseded-reading practice. | `corpus/README.md:11` (sums 217); `:550-553` | Annotate and supersede in the rev-2.5 block; do not silently rewrite `:11`. Ca01/Ca03. |
| **V4** | Pre-apply (scope of instrument) | A heading control patched into `reports/round-28/readme/sweep.py` would edit filed bytes; a count-only assertion would pass a title-at-line-3 file. | `git ls-files --error-unmatch reports/round-28/readme/sweep.py` → tracked; no H1 logic in the file; `reports/round-48/targets.json:6` | New `tools/harness/` check; assert count 1 **and** H1 at line 1. Ca05. |
| **V5** | Note (evidence discipline) | `reports/round-48/claims.json` requires “audits PASS”, but the r47 failure was precisely certifying from staged/pre-fix bytes. | `reports/round-47/review/R03-c-content.md:233-262`; `reports/round-47/validation.json` | The delivery certificate must be the **post-apply** sweep on the live tree, not a staged prediction; every verifier must name the tree it measured. |
| **V6** | Note (PROVINCE wording) | `PROVINCE.md:27` names `kotodama-shokunin/` while the repo root is the outer directory; an empty `kotodama-shokunin/reports/round-29/defects/` exists. | §2; 0 files under it | Integrator; future calibration move. No r48 action. |
| **V7** | Note (rights boundary) | The entry's proposed indigenous-cartography calibration must stay a cited calibration row, not a rights/attribution adjudication. | `PROVINCE.md:17`; r44 seed §4.5; r47 R03 §4.1 | C-drafters: cite published scholarship, mark `(to-verify)`, no ruling. |

No other violations: no canon recording, no game-mechanics or research-method surface, no packet/example change (`examples/` untouched; sha `adfd7895…` / `751be044…` unchanged), no `tools/gates/frozen/**` proposal, no re-freeze, no seat out path outside `reports/round-48/`, no `corpus/` staging.

## 7. Axis verdicts from the scope seat

- **Coverage: no harm, +1 genuine if V2 is fixed.** The gap is verified fresh (0 filename owners, 0 topic owners) and honestly low-demand (`cartograph` 2/2; `mapmaking`/`portolan`/`graticule`/`theodolite` 0). The entry's partition and slug are correct and the landing is an **A**, not an **M**. Scope harm would arise only if the cadastral or survey sections restate agrarian/timekeeping owners — a table row fixes that before landing.
- **Calibration: no harm if V3/V4 are honoured.** The README fix is surgical and index-safe (verified on a staged copy), the queue successor is the right instrument for the over-build class, and the heading control belongs in a new gate.
- **Adjacency: PASS-with-fixes.** PROVINCE is accurate; the only corpus delta is the declared two files; the one-owner risk is confined to the boundary table, which the right-sized draft can carry.

## 8. What I did not verify (`to-verify`)

- **The 63 other seats' eventual writes.** None had filed at my cut; only `reports/round-48/claims.json`, `reports/round-48/targets.json`, and `reports/round-48/telemetry/dispatch-declared.json` existed. A03/A04 own the close-time census.
- **Writes outside the repo.** `git status` shows no tracked change and no untracked path outside reports; sibling repos, the world bible and `.ufo` are outside this repo and outside my read surface, so “no outside write” is **not** claimed.
- **The r48 validation run.** `reports/round-48/validation.json` does not exist and no seat may run the in-tree runner (V1). I did not create or run one.
- **The final C bytes.** No r48 C fragment existed at my cut; §4.2–4.3 is a check of the r47 boundary surfaces the right-sized draft inherits. Whether the r48 draft actually adds the rows is C05/C15/A02's post-draft check.
- **External sources.** Not read; every external edition/page in the shelf remains `(to-verify)` (no network at seat time).
- **Long-run stability of the gap.** Verified at `a01405d` only; the landing-time re-check is C06/A02/V01's job.

## 9. Commands and write-surface statement

All commands run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ for p in civilizations culture-material linguistics myth-symbol synthesis verification; do
    printf '%-16s %s\n' "$p" "$(ls corpus/knowledge/$p/*.md | wc -l)"; done
civilizations 94 / culture-material 25 / linguistics 25 / myth-symbol 26 / synthesis 29 / verification 24
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223; missing 0; topic_mismatch 0; orphan_rows 0; header_drift {}; totals 223; footer 25/26/25/29/24/94; exit 0
$ sha256sum corpus/README.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ git diff --stat HEAD -- corpus/ tools/ examples/ LOG.md PROVINCE.md SCORECARD.md SHONEN.md
(empty)
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|survey map|world map|graticule)' corpus/knowledge/ | wc -l
0
$ for t in cartograph mapmaking portolan graticule theodolite cadastr; do printf '%s files=%s lines=%s\n' "$t" "$(grep -rli "$t" corpus/knowledge/ | wc -l)" "$(grep -rni "$t" corpus/knowledge/ | wc -l)"; done
cartograph 2/2; mapmaking 0/0; portolan 0/0; graticule 0/0; theodolite 0/0; cadastr 2/2
$ python3 (culture-material wc -l)
n 25; min 103; median 149; max 221; over-250 []
$ python3 (staged dup-H1 removal -> .scratch/a01/README-no-dup-h1.md)
575 -> 574 lines; H1 2 -> 1
$ python3 -B reports/round-28/readme/sweep.py --readme .scratch/a01/README-no-dup-h1.md
rows 223 files 223; totals 223; footer 25/26/25/29/24/94; exit 0
$ python3 (r47 surface diff)
couples 21 basenames; table 8; in couples not table 13; in table not couples 0
$ ls reports/round-48/run-validation.py
ls: cannot access 'reports/round-48/run-validation.py': No such file or directory
$ find reports/round-48 -type f
reports/round-48/claims.json
reports/round-48/targets.json
reports/round-48/telemetry/dispatch-declared.json
```

**Write surface:** this file only — `reports/round-48/adj/A01-scope.md` — plus the disposable `.scratch/a01/README-no-dup-h1.md` staged copy. No `corpus/**`, `tools/**`, `examples/**`, `LOG.md`, `PROVINCE.md`, `SCORECARD.md`, `SHONEN.md`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed.
