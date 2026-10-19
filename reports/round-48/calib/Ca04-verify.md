# Ca04 — over-build disposition: independent verification

- Seat: `Ca04` | role: verifier | claim: **Ca** (calibration) | round 48, loop 2, position 2
- Out: `reports/round-48/calib/Ca04-verify.md` (the only write by this seat)
- Baseline: `a01405d` (`git rev-parse --short HEAD`, 2026-10-19T19:40Z) = `reports/round-48/claims.json:7`
- Mission: verify Ca02's r47 over-build disposition row — correct class, owner, next_touch,
  every cited defect real, and a successor record rather than an edit to filed bytes.

**One-line verdict.** The defect class is **real and independently reproducible**: all nine of
R03's blocking defects (B1–B9) reproduce in the filed r47 bytes, with the exact anchors pinned
below, and the volume is **790 fenced lines** against a live culture-material maximum of **221**
(3.6×). The class is **absent from the durable defect queue** (0 rows in `defect-queue-v2.json`
or either successor) but **not unrecorded** — `LOG.md:3906` and `SCORECARD.md:901,907-908` name
it. Ca02's row landed during this seat's run and **passes every blocking gate**: correct class
(`routed-with-owner` → `carried-with-owner`), role-bearing owner, actionable next_touch, all nine
anchors real, unique id, parent and predecessor pins exact, and a new-artifact apply path (no
filed byte edited). It carries **four precision defects (F1–F2 P2, F3–F4 P3)** — none blocking —
listed in §7. The `fixed-with-evidence` class is inadmissible at assembly: the r48 C landing does
not exist yet, so a premature "fixed" row would repeat the very defect the row is about.

---

## 1. Method

I did not read R03's findings as authoritative and restate them. I opened the four filed r47
fragments and re-measured each cited line and each in-corpus anchor from the live tree at
`a01405d`. Where R03 folded several symptoms into one defect (B5 covers two cross-references,
B7 covers three update-rule statements), I verified each sub-anchor separately. Arithmetic was
recomputed by hand and by shell, not copied.

The fragments I read, with file line counts:

| Fragment | file | lines | entry body lines (fenced) |
|---|---|---:|---:|
| C01 | `reports/round-47/cov/C01-entry-a.md` | 358 | 201 (fence 85→287) |
| C02 | `reports/round-47/cov/C02-entry-b.md` | 503 | 361 (fence 40→402) |
| C03 | `reports/round-47/cov/C03-entry-c.md` | 287 | 177 (fence 72→250) |
| C04 | `reports/round-47/cov/C04-entry-header.md` | 301 | 51 (fence 111→163) |
| **total** | | **1449** | **790** |

`C01+C02+C03 = 739`; the 51-line difference is C04's head block. This reconciles the two numbers
in circulation: the claim and `LOG.md:3906` say **790** (four fenced bodies including the head),
R03 §1 says **739 body lines** (the three body fragments, head excluded). Both are correct under
their stated basis; a disposition row must say which basis it uses rather than switch silently.

## 2. Baseline facts (measured)

```
$ git rev-parse --short HEAD
a01405d
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ wc -l corpus/knowledge/culture-material/*.md   (sorted)
min 103 / median 149 / max 221   (25 files; total 3756)
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223 / missing_from_index 0 / topic_mismatch 0 / orphan_rows 0
totals_line 223 totals_ok True / footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
```

The README duplicate H1 is live exactly as Ca03/Ca05 describe (`grep -c` = **2**, lines 1 and 3);
that is the sibling claim Ca, not mine, and the sweep is green at 223 either way. My verification
must not disturb it.

## 3. B1–B9 — independent re-measurement

Severity is R03's: **B** = blocking. "Reproduced" means I re-read the cited line in the filed
fragment and re-derived the claim; I did not merely confirm that R03 wrote it.

| ID | Cited anchor | What the filed bytes actually say (short quote) | Independent check | Verdict |
|---|---|---|---|---|
| **B1** | `C02-entry-b.md:98` | "0.2 mm on a 1:50,000 sheet claims about 10 m of ground; if the survey closed at 200 m, the drawing asserts **ten times** the available precision" | `0.2 mm × 50,000 = 10,000 mm = 10 m`; `200 / 10 = 20` | **REPRODUCED** — the error is 20×, not 10× |
| **B2** | `C04-entry-header.md:115` | gap statement: "`grep -rli 'cartograph' …` → **2 files / 3 lines**, all by-product or disclaimer (`cosmology-cosmography.md:71,:102`; `mesoamerica-primary-sources.md:58`)" | `grep -rni 'cartograph' corpus/knowledge/` → **2 lines, 2 files**; `sed -n '71p' cosmology-cosmography.md \| grep -c cartograph` → **0** (`:71` says "Mappa Mundi" / "survey maps") | **REPRODUCED** — "3 lines" is wrong; `:71` is not a `cartograph` hit |
| **B3** | `C02-entry-b.md:36` and `:501` | "The quoted phrase is **not in the file**. … It appears to be a corruption of … 'a map is an archive of renamings'"; `:501` instructs C06 to "correct or drop" the quote | `grep -n 'archive of coups' corpus/knowledge/linguistics/naming-systems.md` → `70: … Every renaming is datable; a map is an archive of coups.` | **REPRODUCED** — the accusation is false; applying C02's "fix" would corrupt a correct citation |
| **B4** | `C02-entry-b.md:248`; audit row `:421` | "workshop ladder … (`craft-artisan-lexicon.md:44`; the guild ladder is at `:3`)"; audit row: "`:44` \| workshop ladder table … \| real" | `sed -n '44p' craft-artisan-lexicon.md` → `\| Steel (Japan) \| **tamahagane** …`; ladder header `:54`, systems `:56-63`, design rule `:65` | **REPRODUCED** — body and audit row are both miscited; the audit's "real" verdict is a false verification |
| **B5** | `C03-entry-c.md:79`; `:184` | `:79` "the typology in **§1–3**"; `:184` "the typology in **§2**" | C01 `:109` = §2 (five-condition test); `:234` = §4; `:238` = §4.1 (eight forms) | **REPRODUCED** — both references point at the wrong section; target is §4.1 |
| **B6** | `C01-entry-a.md:298` | "**Provenance/charter (§9)** should cite `mesoamerica-primary-sources.md:58`" | C02 headers: `:278` = `## 8. Provenance and charter`; `:347` = `## 9. The container-name fossil` | **REPRODUCED** — the handoff sends provenance to the fossil section |
| **B7** | `C03-entry-c.md:123`, `:137`, `:150` | `:123` "re-survey after **any storm that breaches a dike**"; `:137` "re-survey after **every breach, not every levy year**"; `:150` table "after a dike breach, **per levy year**" | C14 independently fails the same three lines as F-1 (`reports/round-47/cov/C14-example.md:78,92,206`) | **REPRODUCED** — three incompatible statements of one rule |
| **B8** | `C01-entry-a.md:90`; boundary row `:96` | `:90` "No entry owns the **made map**"; `:96` row cites `:71`, `:102`, `:133` only | live `cosmology-cosmography.md:27`: "Cosmography = … **how the world is drawn (maps)**, named …, walked …, and built" | **REPRODUCED** — the competing definition is live and undisposed |
| **B9** | `C03-entry-c.md:95-103` | table headed "Minimum credible build **per form**" with **5** form rows: itinerary, cadastral, portolan, chorographic, cosmographic | C01 §4.1 `:238-249` lists **8** forms (`awk` count of the table = 10 pipe lines = header + separator + 8 rows) | **REPRODUCED** — "per form" covers 5 of 8; celestial, thematic, lienzo are missing |

### 3.1 Arithmetic recomputed

| Expression | Value | Used where |
|---|---|---|
| `0.2 × 50,000` | 10,000 mm = 10 m | B1 ground precision |
| `200 / 10` | **20** (not 10) | B1 |
| `790 / 221` | 3.575 ≈ **3.6×** partition max | class volume |
| `790 / 149` | 5.302 ≈ **5.3×** median | class volume |
| `201 + 361 + 177 + 51` | **790** | assembled entry |
| `201 + 361 + 177` | **739** | body excluding head |
| `28 + 26 + 25 + 29 + 24 + 94` (sweep parts) | **226** ≠ 223 | **not a live defect** — the sweep reads parts `{civilizations 94, culture-material 25, linguistics 25, myth-symbol 26, synthesis 29, verification 24}` = 223. The `25/23/26/25/24/94` figures in R03 §8 are the *rev-2.4 prose vector* defect that C10 repairs, not the live sweep |

That last row matters for my seat: a disposition row must not cite "226" as a live count. The live
sweep prints 223; the prose vector in the README is the separate Ca/C10 repair.

### 3.2 Citation anchors verified in the live corpus

| Anchor | Live content | Matches the defect description? |
|---|---|---|
| `naming-systems.md:70` | ends "Every renaming is datable; a map is an archive of coups." | yes — B3's quote exists verbatim |
| `craft-artisan-lexicon.md:44` | `\| Steel (Japan) \| tamahagane …` | yes — not a ladder row |
| `craft-artisan-lexicon.md:54-65` | `:54` header; `:56-63` seven systems; `:65` design rule | yes — the ladder |
| `cosmology-cosmography.md:27` | "how the world is drawn (maps)" | yes — the undisposed competing definition |
| `cosmology-cosmography.md:71` | "T-O diagrams are symbolic, not survey maps" | yes — but contains no token `cartograph` |
| `cosmology-cosmography.md:102` | "T-O diagrams are symbolic devices, not cartographic claims" | yes — the one `cartograph` hit |

## 4. Is the class a real defect class, and where does it live?

The class, stated without inflation: **a draft that violates the partition's length discipline and
whose self-audit certifies defects — arithmetic, citation anchors, cross-references, worked-example
consistency — that an independent reviewer then falsifies.** Evidence: volume 790 vs 221 (3.6×);
B1 arithmetic; B2 a count its own command cannot produce; B3 a false accusation against correct
bytes; B4 an audit row that certifies a miscite as "real"; B5/B6/B7/B8/B9.

**Already recorded, but not dispositioned:**

| Record | Line | What it says |
|---|---|---|
| `LOG.md` | `:3906` | "the assembled entry is 790 lines vs live partition max 221 with 9 blocking defects (R03 B1-B9 …)" |
| `SCORECARD.md` | `:901` | coverage "unchanged (claim C BLOCKED) … 790 lines vs live partition max 221 with 9 blocking defects" |
| `SCORECARD.md` | `:907-908` | "the coverage-over-build defect (790-line entry, 3.6× partition max — the stale-premises class one level up, now a build-quality miss)" |
| `reports/round-47/cross/Q01-final-gate.md` | `:16,106,108` | "790 lines / 739 body … 3.6× the longest existing entry, 5.3× the median"; "Do not land the 790-line assembly" |
| `reports/round-47/validation.json` | `claims.C` | verdict `unchanged-blocked`; measurement `{total:223, culture_material:25, cartography_landed:false}` |

**Not in the durable queue:**

```
$ grep -c -iE 'over-build|overbuild|790|volume|partition band|length discipline' \
    reports/round-40/op/defect-queue-v2.json
0
$ grep -c … reports/round-47/calib/queue-successor-r47.json
0
$ grep -c … reports/round-43/calib/defect-queue-v2-successor-r43.json
2      # both are incidental line refs (LOG.md:3758, SCORECARD.md:790), not an over-build row
```

Parent queue census: **38 rows** = 28 `carried-with-owner` + 10 `fixed-with-evidence`; ids include
`R36-README-DUPLICATE-HEADING` (the Ca sibling's target) but nothing for build quality. The r47
successor carries 3 rows (`r43-stale-premises`, `r44-resolver-hyphen-after-blank`,
`manifest-ledger-two-schema-evolution`); none is this class. So the queue is the right home and
the row is genuinely missing — but the origin must cite the existing LOG/SCORECARD/Q01 records.

**Class boundary (must not be inflated):**

- **One round, one claim.** Incidence is r47 C only. `SCORECARD.md:907-908`'s "stale-premises class
  one level up" is an analogy, not a second instance; no r42/r44 over-build finding exists in
  `reports/round-4[0-6]/` (grep → 0 hits). Ca02's `incidence.indicative_to_verify` lists r42/r44
  only as whole-fragment lengths (538, 485) explicitly marked not-entry-body; I verified those line
  counts but they are not incidence and the row does not count them.
- **Nine blocking defects, not more.** B7 already absorbs C14 F-1/F-2. Volume (R03 P2-3) is the
  class's defining property, not a tenth blocking defect. P2-1..P2-7 outside B7 are should-fix,
  not blocking.
- **Not a telemetry deviation.** The queue's own practice (`defect-queue-v2.json:8`) excludes
  telemetry; this is a rule breach (length discipline + false audit certification), so it is a row.

**Correct class at assembly: `routed-with-owner`** (v2 equivalent `carried-with-owner`). No fix
can be claimed until the r48 C landing exists and the audits re-run on the landed bytes.
`fixed-with-evidence` is available only to a **new** closing row filed afterwards with pasted
output — never by editing Ca02's row.

**Owner/naming that survives:** "integrator-of-record (landing gate) + r48 C claim (right-sized
drafter)". Naming a round instead of a role (e.g. "r48") is not an owner; naming only the drafter
lets the landing gate off.

**next_touch:** r48 C: land one entry at `<=~250` lines (live band 103–221, median 149); re-run
the arithmetic, citation-anchor, length and worked-example legs on the **landed** bytes; then file
a new `fixed-with-evidence` row quoting the audit output.

## 5. Gates Ca02's row must pass (V1–V12)

Run these against the row with `python3 -B` and shell only; no in-tree runner.

| Gate | Check | Pass condition |
|---|---|---|
| **V1 artifact** | the row is a **new** file under `reports/round-48/calib/` (successor JSON or a fenced object) | new path only |
| **V2 parent pin** | `sha256sum reports/round-40/op/defect-queue-v2.json` | `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` |
| **V3 predecessor pin** | `sha256sum reports/round-47/calib/queue-successor-r47.json` | `9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58` |
| **V4 schema** | parse the JSON | `schema == "kotodama-defect-queue-successor-v1"`, `round == 48`, `baseline_commit == "a01405d"` |
| **V5 id** | row id not already used | unique vs the 38 parent ids + the 3 r47 successor ids |
| **V6 origin** | cites R03 B1–B9 **and** `LOG.md:3906`, `SCORECARD.md:901,907-908`, `Q01-final-gate.md:16,106,108` | no "nowhere recorded" claim |
| **V7 class** | `class == "routed-with-owner"`, `v2_class_equivalent == "carried-with-owner"` | not `fixed-with-evidence` |
| **V8 owner** | role-bearing, both drafter and landing gate | not a bare round number |
| **V9 next_touch** | names the length discipline (`<=~250`; live max 221/median 149) and the re-run audits | actionable, no "should work" |
| **V10 evidence** | all nine anchors present: `C02:98`; `C04:115`; `C02:36`+`:501`; `C02:248`+`:421`; `C03:79`+`:184`; `C01:298`; `C03:123`+`:137`+`:150`; `C01:90`+`:96`; `C03:95-103` | none missing, none invented |
| **V11 self-clean** | the row's own citations do not repeat B3 (it must not say "archive of coups" is absent) and do not cite 226 as a live total | passes the same test it is about |
| **V12 successor-not-edit** | `git status --porcelain` shows no `M` on `reports/round-40/op/defect-queue-v2.json`, `reports/round-47/**`, or `corpus/**` | only new r48 bytes |

V7 and V11 are the two that a plausible-but-wrong row will fail: a "fixed" class is premature, and
a row about unverified citations is exactly where a miscite is least excusable.

## 6. Successor-not-edit verification (measured)

```
$ sha256sum reports/round-40/op/defect-queue-v2.json
dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907
$ sha256sum reports/round-47/calib/queue-successor-r47.json
9508b6aaf04bdb5c69fd263dfa6693037e2ab66b9773b369c6393f14b1fece58
$ sha256sum reports/round-43/calib/defect-queue-v2-successor-r43.json
77f9d63ea41dad49f176e4ada75abeb4330730c6525405982a5b88f6df7dad38
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/
```

The parent digest matches the pin carried by both prior successors; the r47 successor digest
matches `reports/round-47/validation.json` `claims.Ca.measurement.successor_sha256`; no tracked
file is modified. A new r48 successor under `reports/round-48/calib/` is therefore an append, not
an edit. If Ca02 instead proposes to edit `queue-successor-r47.json`, that is a **fail** (V12).

## 7. Ca02 row — direct verification (landed mid-run)

`reports/round-48/calib/Ca02-overbuild.md` appeared at 2026-10-19T19:40:49Z (mtime
`2026-10-19 16:40:49 -0300`). I extracted its fenced
JSON and re-ran §5 against the bytes, plus every measurement it reports.

**Gate results: 11 PASS, 1 PARTIAL (V6), 0 FAIL. No blocking gate fails.**

| Gate | Result | Evidence |
|---|---|---|
| V1 new artifact | **PASS** | fenced JSON with apply path `reports/round-48/calib/queue-successor-r48.json`; "never an in-place edit" (`Ca02:79`) |
| V2 parent pin | **PASS** | `dfc9265d…` at `Ca02:89`; my `sha256sum` identical |
| V3 predecessor pin | **PASS** | `9508b6aa…`, `rows: 3`, `over_build_row_present: false` (`Ca02:91-96`); my grep of its ids confirms no over-build row |
| V4 schema | **PASS** | parses; `schema`/`round 48`/`baseline_commit a01405d` |
| V5 id unique | **PASS** | `r47-entry-overbuild-defect-class`; no collision against the 38 parent + 3 r47 ids (41 checked) |
| V6 origin | **PARTIAL — F1** | cites R03, R01, validation, C11, the four fragments; omits the existing LOG/SCORECARD/Q01 records |
| V7 class | **PASS** | `routed-with-owner` / `carried-with-owner`; not prematurely fixed |
| V8 owner | **PASS** | "r48 C drafter … + r48 integrator (entry-quality acceptance)" — both roles |
| V9 next_touch | **PASS** | names 103–221 band, `<=~250` tolerance, fence extraction, the B1–B9 re-checks, and a NEW closing row |
| V10 evidence | **PASS** | all nine anchors present and real (§3); no invented anchor |
| V11 self-clean | **PASS** | states the `:70` quote is verbatim (does not repeat B3); no 226-as-live total |
| V12 successor-not-edit | **PASS** | parent and r47 successor digests unchanged; `git status` shows no `M` |

**Its numbers reproduce exactly** (my fence extraction over the four fragments):

```
lines 790 | words 20123 | chars 127942 | H2 15 | table rows 240 | (to-verify) 51
body  739 | words 17601 | chars 106997 | (to-verify) 29
```

That matches `Ca02:37-38` digit for digit and reconciles with R03 (`:96`) and R01 (`:88-92`). All
seven digests the row pins match the live files (R03 `7e3e0880…`, R01 `196328de…`, validation
`17f8f1d4…`, C11 `4637ab10…`, cosmology `165f292b…`, naming `d972a1d6…`, craft `fd678d82…`). The
`incidence.indicative_to_verify` line counts reproduce (`reports/round-42/cov/C01-entry-1.md` = 538;
`reports/round-44/cov/C01-entry-draft.md` = 485). Its C11 `854` FAIL and C07 `100 <= len <= 260`
band both re-read correctly at `C11:67-78` and `C07:354`.

### 7.1 Precision defects (non-blocking)

| ID | Sev | Location | Finding | Fix |
|---|---|---|---|---|
| **F1** | P2 | `Ca02:108` (origin) | The class is **already named** at `LOG.md:3906`, `SCORECARD.md:901,907-908`, and `Q01-final-gate.md:16,106,108`; the origin cites none of them. It does not claim otherwise, so this is incompleteness, not falsehood — but a disposition row should show that only the *queue* row was missing. | Append one sentence to `origin` naming those four records. |
| **F2** | P2 | `Ca02:8,18,112` | "no audit ran on the assembled bytes" is **overstated**. C11 assembled the draft and ran C07's extracted checker on it, producing `FAIL length in partition band: 854 lines` (`C11:67-78`); what never ran on assembled bytes were the **content** audits (C06/C07/C08/C12/C13/C14 on final bytes — R03:248). | Narrow the claim to "no content audit ran on the assembled bytes; one length leg did (C11)". The class thesis survives. |
| **F3** | P3 | `Ca02:161` (census_note) | "parent 38 + r47 successor 3 + this row 1 = 42 … all three artifacts" is arithmetically right for the three named files but silently excludes `defect-queue-v2-successor-r43.json` (4 rows); summing every successor-line artifact gives 46. | Say "the three artifacts named here" or include r43 explicitly. |
| **F4** | P3 | `Ca02:23,138` | The printed `grep -rln 'partition band\|length in partition' tools/` is a BRE with a literal `\|`, so it searches for the literal string and its zero is not discriminating. I re-measured both alternatives separately (0 and 0), so the conclusion is true; only the shown command is weak evidence. | Use `grep -rlnE 'partition band\|length in partition\|length in partition band' tools/`. |

None of F1–F4 touches the row's class, owner, next_touch, or defect evidence. The row is
**admissible as filed with F1/F2 corrected**; F2 is the one I would fix before integration because
the row's subject is unverified claims.

**Duplicate-row risk.** `Ca02:172` already anticipates r48 Ca06's combined process-defect row and
requires one canonical id with the other as alias. I confirm the risk is real — Ca06's mission
covers the same build-quality class plus stale premises — and the row's handling is correct: cite
`r47-entry-overbuild-defect-class` as the entry-quality member, never count two rows.

## 8. What I did not verify

- **The r48 C draft and landing** — other seats; no entry file exists at `a01405d`
  (`ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` → absent). My V7 ruling
  rests on that absence, so the row's `routed-with-owner` class is correct at this cut and would
  only change if a landing appears before the integrator files.
- **The nine repairs** — I verified the defects, not their fixes. B7 in particular needs the C14
  example audit re-run on the r48 assembled section; that is the C drafter's obligation.
- **Whether a durable entry-quality control lands** — Ca02's `proposed_control` is explicitly
  "proposed - not landed" (`:137-141`); no tool check exists (`grep` 0). Whether the integrator
  adopts it is out of my scope.
- **Ca06's combined row** — not filed at my cut; I verified Ca02's dedupe *instruction*, not the
  future Ca06 bytes.
- **External sources** in the r47 shelf — irrelevant to a disposition row and already marked
  `(to-verify)` by the draft.

## 9. Commands and write surface

All from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```
git rev-parse --short HEAD                                  -> a01405d
find corpus/knowledge -name '*.md' | wc -l                  -> 223
ls corpus/knowledge/culture-material/*.md | wc -l           -> 25
wc -l corpus/knowledge/culture-material/*.md | sort -n      -> min 103 / median 149 / max 221
python3 -B reports/round-28/readme/sweep.py                 -> 223==223, green
grep -n 'asserts ten times' reports/round-47/cov/C02-entry-b.md          -> :98
grep -rni 'cartograph' corpus/knowledge/                    -> 2 lines, 2 files
sed -n '71p' corpus/knowledge/myth-symbol/cosmology-cosmography.md | grep -c cartograph -> 0
grep -n 'archive of coups' corpus/knowledge/linguistics/naming-systems.md -> :70 (present)
sed -n '44p' corpus/knowledge/culture-material/craft-artisan-lexicon.md  -> Steel (Japan)
grep -n -iE 'apprentice|journeyman|masterpiece' …craft-artisan-lexicon.md -> :54,:56-63,:65
grep -n '^## ' reports/round-47/cov/C02-entry-b.md         -> :278 §8, :347 §9
grep -n '^| update' reports/round-47/cov/C03-entry-c.md    -> :150
sed -n '238,249p' reports/round-47/cov/C01-entry-a.md      -> eight form rows
sha256sum reports/round-40/op/defect-queue-v2.json         -> dfc9265d…
sha256sum reports/round-47/calib/queue-successor-r47.json  -> 9508b6aa…
python3 (fence extraction C01–C04)                          -> 201+361+177+51 = 790; 739 body
grep -c -iE 'over-build|overbuild|790|volume|partition band' <queue + successors> -> 0 / 0 / 2 incidental
git status --porcelain                                     -> only ?? reports/round-46/review/, ?? reports/round-48/
# Ca02 row verification (after it landed):
python3 (extract fenced JSON from Ca02-overbuild.md)       -> parse OK; 1 row, 9 findings, 5 gates, 6 reclass gates
python3 (id collision vs parent 38 + r47 successor 3)      -> False
python3 (fence extraction, word/char/table/to-verify)      -> 790/20123/127942/240/51; body 739/17601/106997/29
sha256sum <R03 R01 validation C11 cosmology naming craft>  -> all seven cited digests match
wc -l reports/round-42/cov/C01-entry-1.md reports/round-44/cov/C01-entry-draft.md -> 538, 485
grep -n 'LOG.md|SCORECARD.md|Q01-final-gate' Ca02-overbuild.md -> no hits (F1)
grep -rlnE 'partition band|length in partition' tools/     -> 0 (F4 conclusion holds)
```

**Write surface:** this file only —
`reports/round-48/calib/Ca04-verify.md`. I read but did not modify
`reports/round-48/calib/Ca02-overbuild.md`; F1–F4 are patch instructions for its author or the
integrator, not edits. No `corpus/**`, `tools/**`, `LOG.md`, `SCORECARD.md`,
`reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged.
No git commit/push, no install, no network, no `reports/round-*/run-validation.py` execution, no
`.scratch` artifact required by this analysis.
