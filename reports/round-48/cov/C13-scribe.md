# C13 — C-claim scribe: the assembled cartography evidence chain (integration-ready)

- Seat: `C13` | role: scribe | claim: **C** (coverage) | round 48, loop 2, position 2
- Out path: `reports/round-48/cov/C13-scribe.md` (this file)
- Baseline: HEAD `a01405d` (`git rev-parse --short HEAD`, 2026-10-19) = `reports/round-48/claims.json` → `baseline_commit: "a01405d"`
- **Assembly window note (honest record).** My first pass at this seat ran before any sibling fragment existed (`reports/round-48/cov/` did not exist; only `claims.json`, `targets.json`, `telemetry/`). By the time I assembled, 50+ fragments were filed. This file is the **reconciliation of the filed bytes**, not a restatement of my first-pass placeholder. The placeholder draft I staged earlier is discarded; the canonical source is now **C02's head + C01's body**, both filed under `reports/round-48/cov/`.

**One-line verdict.** The C chain assembles to a **239-line entry** (23-line head from `C02-header.md` + 215-line body from `C01-entry.md`) that is **within the ~250 ceiling**, lands as **A** on a free slug, fixes every R03 B1–B9 defect on its actual bytes, and **sweeps green on a staged 224 tree** (`224 == 224`, 0 missing/ghosts/mismatch/drift, footer `25/26/26/29/24/94`). Four pre-apply patch classes remain (the blocking agrarian row, two mandated couples tokens, three header/provenance fixes, and the shelf reconciliation) and **no non-author audit of the assembled 239 lines exists yet** — that is the gate before apply.

## 1. Live state measured at `a01405d`

All commands from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

| Measurement | Command | Result |
|---|---|---|
| Total entries | `find corpus/knowledge -name '*.md' \| wc -l` | **223** |
| culture-material | `ls corpus/knowledge/culture-material/*.md \| wc -l` | **25** |
| Partition vector | per-partition `ls … \| wc -l` | **25 / 26 / 25 / 29 / 24 / 94** (sums 223) |
| Gap: filename owners | `find … -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' \| wc -l` | **0** |
| Gap: topic-line owners | `grep -rniE '^- *topic:.*(cartograph\|mapmak\|portolan\|cadastr\|…)' corpus/knowledge/ \| wc -l` | **0** |
| `cartograph` body hits | `grep -rni 'cartograph' corpus/knowledge/` | **2 lines / 2 files** (`cosmology-cosmography.md:102`, `mesoamerica-primary-sources.md:58`); `:71` is the survey-map disclaimer and does **not** contain the token |
| `mapmaking` / `portolan` / `graticule` / `theodolite` | per-term `grep -rli … \| wc -l` | **0 files each** |
| Entry-length band | `wc -l corpus/knowledge/culture-material/*.md \| sort -n` | **min 103 / median 149 / max 221** (n 25) |
| README sweep at HEAD | `python3 -B reports/round-28/readme/sweep.py` | 223==223; 0 missing/ghosts/mismatch/drift; footer 25/26/25/29/24/94; exit 0 |
| README H1 count | `grep -c '^# kotodama-shokunin corpus index' corpus/README.md` | **2** (lines 1 and 3; Ca's defect, untouched here) |

**Gap re-verified unowned, not carried** — the r47 B2 lesson is applied in the filed head: line counts and file counts are stated separately and `:71` is excluded from the token count.

**README anchors (pre-edit):** rev 2.4 `:5`; vector defect `:11`; `## culture-material/ (25)` `:234`; calendar row `:240`; costume row `:241`; totals `:544`; footer `:546-548`.

## 2. Assembly decision — C02 head + C01 body, spliced at `## 1.`

| Source | Location | Lines | Why this source |
|---|---|---:|---|
| Head | `reports/round-48/cov/C02-header.md`, fenced `markdown` block in §2 | **23** | The only head with all **8 fields** including `- source:`; `- topic:` is **byte-equal to the r44 seed** (766 chars, sha256 `bc7274f4…`), independently checked by C16; 11 sha256 pins reproduced by C18; 19/19 couples resolve (C09) |
| Body | `reports/round-48/cov/C01-entry.md`, fenced block from `## 1.` to end | **215** | The right-sized body: 14 H2, 81 table rows, 6 `(to-verify)` marks in the body (12 more in the head = 18 merged), 8/8 form rows, one worked-example rule |
| **Merged** | `C02 head` + blank + `C01 body` | **239** | 37,592 bytes, sha256 `d1de5db512de1ab2fb526012ac83ec67e7f3105e7aaf934302e16f2f2522a3d1` |

- **Why not C01's embedded head:** it lacks `- source:` (7 fields, not 8) and its topic line is **1045 chars**, not the 766-char seed, so it would fail C16's byte-equality and C10's row generator.
- **Why not my first-pass candidate:** written before the C01/C02 bytes existed; 181 lines but a different topic and a different section skeleton. Superseded — do not apply it.
- **Do not concatenate the component drafts.** `M01-example.md` (27-line example), `M02-calibration.md` (32-line bank) and `E01-boundary.md` (39-line table) are **component sources for patching**, not additional sections: C01's body already integrates §11 (example), §12 (calibration) and §2 (boundary). Appending them would duplicate three sections and blow the length budget. Use M01/M02/E01 only to replace or patch the corresponding C01 section.
- **Length judgment:** 239 ≤ ~250 (claim ceiling). Read against the partition discipline: **body 215 ≤ the 221 partition maximum**, and head 23 is inside the 7–42 header band C02 measured (`C02-header.md` §3.1). The 239 total is 18 above the partition max only because the head is multi-line; the body is at the partition's own length.

## 3. Evidence chain — filed fragment, status, and what it actually audited

| Link | Fragment | Status / scope | Note |
|---|---|---|---|
| Right-sized spec | `scout/K01-rightsized-spec.md` | filed | spec-level; C09 found an arithmetic mislabel in it ("Nineteen" for 21 files) |
| Head block | `cov/C02-header.md` | filed, **patches needed** | audited by C09 (couples) and C18 (provenance) |
| Entry body | `cov/C01-entry.md` | filed | producer self-audit; **no non-author audit of these bytes yet** |
| Arithmetic | `cov/C03-arithmetic.md` | filed, **read cut predates the draft** | audits r47 values (B1/B2/N1–N3), not C01's bytes |
| Citations | `cov/C04-citations.md` | filed, **read cut predates the draft** | audits 55 inherited anchors at `a01405d` (baseline PASS), not C01's bytes |
| Length/structure | `cov/C05-length-contract.md` | **not filed** | C17 covers the r47-vs-right-sized skeleton |
| Freshness/collision | `cov/C06-collision.md` | filed, pre-draft | 0 owners, slug free, lands **A** |
| Boundary | `cov/C07-boundary.md` | filed, r47 + spec | **U1 blocking: agrarian row missing**; O1 `:27` persists into the spec |
| Shelf | `cov/C08-shelf.md` | filed, r47/pre-draft | 21/21 in-corpus, 18/18 external marked |
| Couples | `cov/C09-couples.md` | filed, **audits C02's field** | 19/19 resolve; **P2: 2 mandated tokens absent** (celestial-symbolism, sacred-kingship) |
| README rev 2.5 | `cov/C10-readme.md` | filed, staged green | canonical README diff; row generated from the 766-char topic |
| Sweep | `cov/C11-sweep.md` | filed | **136-line fixture**, not the merged entry — a fixture-green, not a delivery |
| Worked example | `cov/C14-example.md` | filed, pre-draft | acceptance contract, not a verdict on C01's §11 |
| Neighbours | `cov/C15-neighbors.md` | filed, r47 | seven seed neighbours dispositioned |
| Topic | `cov/C16-topic.md` | filed, audits C02 | 766-char seed byte-equality PASS |
| Structure | `cov/C17-structure.md` | filed, r47 | 15 H2 / 44 H3 / 240 rows / 790 lines in r47 |
| Provenance | `cov/C18-provenance.md` | filed, audited C02 + M02 | PASS with **P1–P6 carry-forward fixes** |
| Boundary author | `cov/E01-boundary.md` | filed | integration-ready boundary block |
| Register fit | `cov/E02-register.md` | filed | PASS; culture-material, not myth-symbol |
| Content quality | `cov/C12-content.md` | filed, **read cut predates C01's body** | components judged "real, not filler"; whole-entry depth = `could-not-evaluate` (C12 §1, §5) |
| Example / calibration / method | `cov/M01`, `M02`, `M03` | filed | component drafts; **patch sources only, not additive** |
| Landing wire | `cov/W01-landing-spec.md` | filed | must be read against this file's §2/§4 |
| Post-landing | `cov/V01-post-landing.md` | staged only | not a post-apply census |
| Non-author reviews | `review/R01`, `R02`, `R04` | filed | **no R03 (C-content) filing** |

## 4. Pre-apply patches — what must change before the integrator lands

**P1 — blocking (boundary under-claim).** C07's U1: the boundary table does not name `culture-material/agrarian-field-system-lexicon.md`, which owns the PARCEL and CLAIM institutions, tenure/boundary words and work-unit land measures (`:4`, `:42`, `:114`, `:122-125`). Add E01/C07's fenced row (C07 §6.3) to the 12-row table.

**P1 — mandated (couples completeness).** C09's P2: the `- couples:` field carries 19 tokens but omits two R03-mandated neighbours. Add, with the cross-partition prefix:
- `../myth-symbol/celestial-symbolism-calendars.md`
- `../myth-symbol/sacred-kingship-mythic-charter.md`
Corrected field = 21/21 direct, delta +21/+21 (C09 §4.1). No resolver failure today; the omission is silent.

**P2 — header/provenance (C18 §7).**
1. Fix the one-line-off `claims.json:6` citation to `:7` (P4).
2. Fix the couples count prose (18/19) to the measured 21 after the patch (P5).
3. State the topic digest convention: sha256 over the line **including its LF** (P6).
4. Shelf reconciliation (C18 P1–P3): do not call in-corpus-registered Boone/Needham "external"; add Mundy, al-Idrisi, Needham (Tier A), Boone (Tier A) if the surviving body cites them; cite Needham's registration at `cosmology-cosmography.md:12`, not `:100`.

**P2 — no action:** C16's topic check passes on C02 as filed (766 chars, seed byte-equal). If any patch edits the topic, regenerate the README row with C10's generator and re-run the sweep.

**Gate — non-author body audit.** C03, C04, C14 and E02 all state their read cut predates the draft; C12 recorded `could-not-evaluate` for whole-entry depth for the same reason (`C12-content.md` §1, §5); C09/C18 audited only the head. The assembled 239 lines have **producer-side self-audit only**. R03 (or an equivalent non-author) must review the merged bytes before the round claims "audits PASS".

## 5. Independent verification of the assembled bytes (this seat)

**Dimensions:** 239 lines; 37,592 bytes; 1 H1; 14 H2; 81 table rows; 18 `(to-verify)` marks; 8/8 head fields.

**Arithmetic ledger (every computed value re-derived):**

| Expression | Result | Where |
|---|---|---|
| `0.2 mm × 5,000` | **1 m** | §3 error budget |
| `0.2 mm × 2,500` | **0.5 m** | §3 |
| `0.2 mm × 24,000` | **4.8 m** | §5 scale |
| `0.2 mm × 50,000` | **10 m** | §5 |
| `0.2 mm × 250,000` | **50 m** | §5 |
| `tan(1′) × 10,000 m` | **2.909 m ≈ 2.9 m** | §3 angular work |
| `200 m / 10 m` | **20×** — the r47 B1 fix | §3 |
| `1% × 100 paces × 0.75 m` | **0.75 m** | §3 |
| `710 m × 710 m` | **504,100 m² ≈ 50 ha** | §4 centuria |
| `1 cm × 50,000` / `× 250,000` | **500 m** / **2.5 km** | §5 scale bar |
| `25+26+25+29+24+94` | **223** | live partition / footer |
| `25+23+26+25+24+94` | **217** | rev-2.4 defect (repaired) |
| `25+26+26+29+24+94` | **224** | rev-2.5 destination |

**Citation ledger:** 42 distinct `.md` references in the merged entry; **39/39 in-corpus references resolve** across **23 distinct files**; 0 ambiguous basenames, 0 out-of-range line windows. The three non-corpus refs are the entry itself, `K02-gap-scout.md` (a report), and `README.md` (the index).

**Verbatim quote checks (7/7 PASS at `a01405d`):** `cosmology-cosmography.md:27` ("how the world is drawn (maps), named (toponyms), walked (processions, pilgrimage), and built (cities, temples)"), `:71` ("T-O diagrams are symbolic, not survey maps"), `:102` ("not cartographic claims"); `transport-mobility-lexicon.md:28` ("a route is only real if someone maintains it"); `naming-systems.md:70` ("a map is an archive of coups"); `craft-artisan-lexicon.md:54` (ladder header) and `:65` ("Design rule").

**R03 B1–B9 on the assembled bytes:**

| Defect | Status | Evidence on the merged bytes |
|---|---|---|
| B1 arithmetic | **fixed** | `200 m / 10 m = 20×`; no "ten times" string (grep 0) |
| B2 gap count | **fixed** | "2 lines in 2 files"; `:71` excluded as a `cartograph` hit |
| B3 false accusation | **fixed** | `naming-systems.md:70` quoted verbatim; no "not in the file" claim |
| B4 ladder miscite | **fixed** | `:54-65` cited; `:44` not used as the ladder |
| B5 cross-refs | **fixed** | only `§3` and `§5` referenced (line 231), both correct |
| B6 handoff ref | **fixed** | scope names the handoff, not a wrong section |
| B7 example rule | **fixed** | one "Update rule (stated once)" in §11; no competing formulation |
| B8 `:27` over-claim | **fixed** | gap sentence + boundary row quote `:27` and assign world-picture vs sheet |
| B9 5-of-8 forms | **fixed** | §4 table has 8 data rows |

**No forbidden r47 strings:** `five roles` 0, `six load-bearing` 0, `ten times` 0.

## 6. README rev 2.5 — canonical diff is C10's

Adopt `reports/round-48/cov/C10-readme.md` §3 (patch A) as the README edit. It makes exactly the six required changes: rev-2.5 block before rev 2.4; rev-2.4 vector repair (`25/23/26/25/24/94` → `25/26/25/29/24/94`); section header 25→26; row between `calendar-festival-systems.md` and `costume-semiotics.md` generated from the 766-char topic; totals 223→224; footer `(total 224 files; directory totals 25/26/26/29/24/94)`.

Two independent staged receipts agree on the sweep, differing only in the rev-2.5 prose wording:
- C10: `rows 224 files 224`, `ok True`, `readme_sha256 5767d3c4…`
- This seat (merged entry): `rows 224 files 224`, `ok True`, `readme_sha256 7088ec9a…`

The integrator should apply **C10's** exact bytes; the row must be regenerated if the topic changes (C10 §3.2 gives the generator).

## 7. Staged 224 sweep — receipt for the merged entry

Method: copy `corpus/knowledge/` → `.scratch/c13/tree2/`; add the 239-line merged entry; rebuild the README from `a01405d` with the six edits; call `sweep()` with `root_override` (read-only; no in-tree run).

```
parts {"civilizations": 94, "culture-material": 26, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 224 files 224
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 224 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 224, "dir_totals": [25, 26, 26, 29, 24, 94]}
footer_live {"total": 224, "dir_totals": [25, 26, 26, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 7088ec9a51183063f285891afef57b1b1f9ffac28dbb56e3a3319ebdf6a29e5c
OK = True
```

**This is a staged prediction, not a delivery certificate.** The only certificate is the post-apply sweep on the real tree at the apply-time HEAD. C11's green is a 136-line fixture and does not stand in for this.

## 8. Apply order, residuals, and claim status

1. Patch the head (2 couples tokens; P4/P5/P6) and the body (agrarian row; shelf reconciliation).
2. Confirm the topic is unchanged (766 chars, seed byte-equal); otherwise regenerate the README row.
3. Apply C10's README patch A.
4. Run the post-apply `python3 -B reports/round-28/readme/sweep.py` → must read `rows 224 files 224`, exit 0.
5. Run the post-landing census (V01/F01): 224 total, culture-material 26, README rev 2.5, H1 count unaffected by C, footer vector 224.
6. **Do not claim "audits PASS"** until a non-author reviews the merged 239 lines. Current audit status: head audited (C09/C18), body producer-only (C01), r47 defects independently re-checked here.

**Residuals / not verified:**
- External editions and pages: all `(to-verify)`; no network.
- The freshness gate: C FRESH is recorded in `claims.json`; not re-run by this seat.
- C07 U1 (agrarian) is **open** on the assembled table; C09 P2 is **open** on the field.
- C18's P1–P3 shelf reconciliation is **open** (Tier A vs external, missing Mundy/al-Idrisi/Needham/Boone rows).
- Ca's H1 removal shifts README lines by −2; anchor by content.
- If any other corpus change lands first, re-stage and re-run.

## 9. Write surface and commands

- **Durable write:** this file only — `reports/round-48/cov/C13-scribe.md`.
- **Disposable staging:** `.scratch/c13/` (tree copies, merged entry, staged READMEs). No `corpus/**`, `tools/**`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged.
- No git commit/push, no install, no network. No `reports/round-*/run-validation.py` executed in-tree. No re-freeze of `declared-in-r7`. No packet-surface change.

**Commands (abridged, lane root, 2026-10-19):**

```
git rev-parse --short HEAD                                   → a01405d
find corpus/knowledge -name '*.md' | wc -l                   → 223
ls corpus/knowledge/culture-material/*.md | wc -l            → 25
find … -iname '*cartograph*' … | wc -l                       → 0
grep -rni 'cartograph' corpus/knowledge/                     → 2 lines / 2 files
python3 -B reports/round-28/readme/sweep.py                  → 223==223, exit 0
python3 (C02 head + C01 body splice, `## 1.`)                → 239 lines, sha d1de5db5…
python3 (anchor resolver, 42 refs)                           → 39/39 in-corpus resolve; 0 ambiguous; 0 out-of-range
python3 (staged sweep, merged entry)                         → 224==224, ok True
```
