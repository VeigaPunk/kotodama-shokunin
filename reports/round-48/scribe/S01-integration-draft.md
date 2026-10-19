# S01 — round-48 integration draft (C + Ca)

- Seat: `S01` | role: scribe | claim: **cross** | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19) = `reports/round-48/claims.json:7` (`"baseline_commit": "a01405d"`). No drift: `git rev-list --count a01405d..HEAD` → 0.
- Out path: `reports/round-48/scribe/S01-integration-draft.md` (this file; only write).
- Observation cut: **2026-10-19T19:52Z** (`date -u`). **All 64 declared seats filed**, including `R03` (content review) at 19:52Z and `C05`/`Q01` after this seat's first pass. Fragments were revised during the wave; §5 records the moving-fragment hazard and every citation below was re-read at this cut.
- Non-author statement: I drafted no C or Ca fragment and edited no corpus, tool, README, queue, or filed-round byte. All scratch work is under `.scratch/s01/`.

---

## 0. Integration verdict

| claim | verdict at this cut | why |
|---|---|---|
| **C — coverage** | **NOT LANDING-READY; do not apply** | Three independent gates say so on the bytes: `C05` **FAIL as assembled** (W01's join = 251 lines / 2 H1s); `R03` **depth PASS, landing FAIL** (blocking D1 definition contradiction, D2 two heads, D3 shelf gap); `Q01` **NOT CERTIFIED**. A 239-line route-B assembly exists and stages green, but it needs ~8 lines of fixes and audits re-run on the final bytes. Coverage stays **223**. |
| **Ca — calibration** | **README half PASS-staged; disposition half NOT FILEABLE** | Six stagings agree on `d407260d…` / 573 lines / H1 1 / sweep green. `Q01` files five blocking disposition defects (`Q-Ca1..Q-Ca5`): double-counted class rows, three successor drafts, an undispositioned second duplicate, five control drafts, a forbidden counting command. Nothing is applied. |
| **Round** | **`rejected-honest-stop` on C; Ca `improved` only if its disposition half is fixed and applied** | REGIMEN: admit only when every claim verifies. `Q01` records "no move recordable". Do not average the C shortfall into an accept (r47 precedent). |
| **Freshness declaration** | **`to-verify`, not "fresh"** | The candidates/overlay exist only in `.scratch`; filed claims alone return `could-not-evaluate`; filed claims + used overlay return malformed/exit 2. Only a reconstructed overlay reproduces the declared verdicts (`O04`). The Ca probe is vacuous (counts files, not headings) and the O red is a probe artefact (`Q-R2`). |

No axis is harmed on disk: `git status --porcelain` shows only `?? reports/round-46/review/` and `?? reports/round-48/`; `git status --porcelain -- corpus/ tools/` is empty; corpus holds at 223 / culture-material 25; README sha `7c788a1d…`.

---

## 1. Fragment ledger at the cut

All 64 seats filed. Material revisions during the wave: `C13` withdrew its first-pass 181-line candidate and now endorses C02+C01; `C01`'s fragment file was revised while its fence stayed stable; `W01` was rewritten (492 lines). This is the r47 "audits pinned to superseded bytes" hazard in a new form — see §5.

| group | filed |
|---|---|
| scouts/plan/connectors | `K01`, `K02`, `P01`, `X00`, `X01`, `X02`, `X04`, `X05`, `N01` |
| C chain | `C01`, `C02`, `C03`, `C04`, `C05`, `C06`, `C07`, `C08`, `C09`, `C10`, `C11`, `C12`, `C13`, `C14`, `C15`, `C16`, `C17`, `E01`, `E02`, `M01`, `M02`, `N03`, `V01`, `W01`, `D01`, `F01`, `A02`, `R03` |
| Ca chain | `Ca01`, `Ca02`, `Ca03`, `Ca04`, `Ca05`, `Ca06`, `Ca07`, `W02`, `N02` |
| reviews/critics/adjacency | `R01`, `R02`, `R04`, `A01`, `A03`, `A04` |
| scribes/op/final gate | `S01`, `S02`, `S03`, `O03`, `O04`, `Q01` |

---

## 2. Baseline measured this seat

| Measurement | Command | Result |
|---|---|---|
| total / partition | `find corpus/knowledge -name '*.md' \| wc -l`; per-partition `ls` | **223**; 94/25/25/26/29/24 |
| culture-material length | `wc -l corpus/knowledge/culture-material/*.md` | min **103** / median **149** / max **221** (n=25) |
| sweep | `python3 -B reports/round-28/readme/sweep.py` | `rows 223 files 223`, 0 missing / 0 mismatch / 0 orphan, `totals_ok True`, `footer_ok True`, `readme_sha256 7c788a1d…`, exit 0 |
| sweep selftest | `--selftest` | `12/12 checks passed`; **no heading leg** (`grep -i 'heading\|h1'` → no match) |
| README | `wc -l`; `sha256sum` | 575 lines; `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` |
| duplicate H1 | `grep -n '^# ' corpus/README.md` | lines **1** and **3**; `grep -c` → 2 |
| second duplicate | `grep -o '^revision: [0-9.]*' \| sort \| uniq -c` | `2 revision: 2.0` — orphaned at **`:42`/`:44`**; out of claim scope but flagged by `K02`, `F01`, `X01`, `X05`, `Q-Ca3` |
| cartography owners | filename + topic probes | **0** filenames, **0** topic lines; slug absent |
| demand counts | `grep -rli` / `grep -rni` per token | `cartograph` 2 files / 2 lines; `mapmaking` `portolan` `graticule` `theodolite` 0; `cadastr` 2/2 |
| queue parent | `sha256sum reports/round-40/op/defect-queue-v2.json` | `dfc9265d…` (38 rows; unchanged) |
| r47 successor | `sha256sum reports/round-47/calib/queue-successor-r47.json` | `9508b6aa…`; 3 rows; **0 over-build rows** |

---

## 3. Claim C — assembly and audit status

### 3.1 Premise: PASS

Freshness/collision is independently established at `a01405d`: `K01` (fresh sweep), `C06` (0 owners, slug free, no case/dir variant, lands as **A**), `A02` (no file-level second owner), `R01`/`R02`/`X04` (baseline identity), `R03` §7 ("the gap is real and fresh … the demand is stated honestly as low"). The premise is not the problem; the bytes are.

### 3.2 The assembly question is settled — route B, 239 lines

`C05`, `R03` and the rewritten `C13` converge on one shape: **C02's 23-line head + a blank + C01's body from `## 1.` (215 lines) = 239 lines**.

| artifact | lines | sha256 | authority |
|---|---:|---|---|
| C01 complete fence (head + body) | **227** | `2a66774974b80d9be2659a9e0e09a265114631c21189eae506acba5edfbdb3ca` | `R03` §1 |
| C01 body from `## 1.` | **215** | `771f136566d9c4bb1821de90936a0d8c1e3bce4f88b09939cb9c0d025578792f` | `R03` §1 |
| C02 head fence | **23** | `4692a3347faf8efbdfcd8b3b362d6812ca7c7a1abc439ca644b6d13dc1feea38` | `R03` §1 |
| **C02 head + blank + C01 body** | **239** | `3538bb3efdab2d13ad13f7f41fb2fd271cc6f52da73e61495e1bc8c6a5381be1` | `R03` §1; `C13` §8 |
| W01's "join whole fences" | **251** | — | `C05` §1: two H1s, seven duplicated fields — **not landable** |

My own splice without the separator measured 238; the canonical 239 includes the blank between head and body. **Pin the extraction convention** before citing any digest: `C05` and `C17`/`E02` already report C01 as 227/`2a667749…` and 228/`e5255657…` on a fence-inclusion frame (`Q01` §3). C13's first-pass 181-line candidate is **withdrawn by its author** (C13 now says "the placeholder draft I staged earlier is discarded; the canonical source is now C02's head + C01's body"), so route C in C05's table is no longer a live option.

**Why route B:** it preserves the 766-char seed topic, so `C16`'s byte-equality, `C09`'s 19/19 couples result and the README recipes in `C10`/`W01`/`D01` remain valid. Route A (C01 complete, 227→228) forces a new README row from C01's 1,045-char topic and invalidates every staged README prediction; `R02` staged it and measured `topic_mismatch 1`.

### 3.3 Length: compliant, but a new partition maximum

- 239 ≤ 250 (claim gate). Live band 103–221 → **239 is a new maximum (+8.1%)**, 1.60× the median.
- `R03` calls the right-sizing "decisive" versus r47; `C05` says route B "passes every structural leg except the worked-example DR gap." The eight-line fix pass moves it to ~245–247, still ≤250.
- `X02` H6: the 250 ceiling has **no measured provenance** (it comes from r47's inline 100–260 checker at `reports/round-47/cov/C07-contract-audit.md:354`); state the live band, not 250, as the discipline.
- The r47 comparison, once: **790 fenced lines = 51 head + 739 body**, 3.57× the max, 5.30× the median (`reports/round-47/cross/Q01-final-gate.md:87,106`; `R01-48-08`).

### 3.4 Blocking items in the 239-line assembly

| id | finding | evidence | fix (size) |
|---|---|---|---|
| **D1** | **Definition contradicts typology**: §1's condition 1 requires a traversable ground index and calls the star chart "another register's sheet", while §2/§4/the topic line list `celestial/star chart` and `cosmographic/world diagram` among the eight forms; the itinerary row has the same ambiguity. No other filed seat caught this. | `R03` §3 D1 (`C01-entry.md:93,99,110,149-150,73,141`) | make condition 1 a **referent space** (terrestrial or celestial); drop the star-chart failure clause; change "an itinerary" → "an itinerary **list**"; keep the cosmogram as a boundary form — ~3 lines |
| **D2** | **Two heads, three topics, red sweep**: C01's head says the heads "must agree byte-for-byte" but has a 1,045-char topic vs C02's 766; landing C01's head with C10's row produces `topic_mismatch 1`. C01's field set is 7 fields, no `- source:`, `gap filled` before `topic`. | `R03` §3 D2; `R02` §9.2; `C04` §8.4; `C17` §7 | strip C01's head; apply C02's 23-line head verbatim; start body at `## 1.` |
| **D3** | **Shelf does not cover the body**: C02's ten-item shelf omits Mundy 1996, al-Idrisi, Needham, Russell 1991, all cited by the body; C02's `- source:` then falsely says "the shelf above". | `R03` §3 D3 (`C02-header.md:129,131`; `C01-entry.md:76,276-280`) | add one grouped shelf line: "Mundy (1996); Needham (1959) vol. 3; al-Idrisi (1154); Russell (1991, carried in-corpus at `corpus/knowledge/myth-symbol/cosmology-cosmography.md:102`) — `(to-verify)`" |
| **U1** | **Agrarian under-claim**: C01 §2's 12-row table omits `agrarian-field-system-lexicon.md` (parcel/claim institutions, tenure words, land measures). | `C07` U1 (blocking); `A01` §1; `C13` §8 ("C07 U1 is open"); `E01` row 8 supplies the row (`:42`, `:45`) | add E01's row + a couples token (1 line + 1 token) |
| **DR gap** | C01's §11 cites **0** `DR-CM-*` ids; C14 W4/W5 treat zero rule tokens as blocking. C14's PASS certifies M01's 27-line example, **not** C01's 25-line example. | `C05` §6; `C14:112-113`; `R03` P3-6 | tag the example's moves with `DR-CM-01..06` (1–2 lines); state which example lands and re-run C14 |
| **self-ref** | `- sources:` says "transcript in `## Self-audit` below the fence" — a reference to text absent from the landed file. | `C01-entry.md:75`; `Q01` decision 3 | remove the clause |
| **couples** | C02's 19 tokens resolve; C01's 14 resolve; neither set includes both body-owned neighbours (celestial, sacred-kingship) plus agrarian. | `C09` P2; `R03` P3-5; `C13` §8 | add the two mandated tokens (+ agrarian if not in the chosen set) and re-run the resolver |

### 3.5 Audit status on the 239-line assembly

| leg | result | covers the final bytes? |
|---|---|---|
| freshness / collision | PASS (`C06`, `K01`, `A02`) | yes for ownership |
| header / couples | PASS, 19/19 direct (`C09`, `C16`) | yes for C02's head |
| arithmetic | r47 audit PASS + constants (`C03`); `R03` recomputed the body's arithmetic | body arithmetic yes; re-run on final bytes still owed |
| citations | baseline 55 anchors PASS (`C04`); body anchors re-read by `R03` | re-run on final bytes (C04-W1/W2 open) |
| length / contract | **FAIL as assembled** (`C05`) | re-run post-fix |
| content | **depth PASS, landing FAIL** (`R03`) | re-run after D1/D3 fixes |
| boundary | O1 closed; U1 **open** (`C07`, `E01`, `C13`) | add agrarian row |
| shelf | 2 blocking defects on r47 bytes (`C08`); D3 open (`R03`, `C12-F3`, `C18`) | fix the grouped line |
| example | gate defined; r47 fails five (`C14`); C14's PASS is M01's, not C01's | tag + re-run |
| register fit | PASS 4/5 (`E02`) | clause fit only |
| structure | r47 15 H2/44 H3/240 rows; C01 14 H2/0 H3/81 rows (`C17`, `R03`) | yes for structure |
| final gate | **NOT CERTIFIED** (`Q01`) | gate verdict |

### 3.6 C acceptance gates

1. Route B pinned at one digest + extraction convention (239 expected; record the post-fix number).
2. D1, D2, D3, U1, DR gap, self-ref and couples fixes applied.
3. `wc -l` ≤250 (post-fix ~245–247 expected); `V01` leg-3 note accepted for >221.
4. Exactly one H1, one `- topic:` (766-char seed), all eight head fields; row↔topic byte-equal.
5. C03, C04, C05, C08, C12, C14, E02, C09 and **R03** re-run on the final bytes.
6. Post-apply: total **224**, culture-material **26**, sweep `rows 224 files 224`, footer `25/26/26/29/24/94` = 224, exit 0; `git status` = one `A` + README `M`.
7. If any gate is unmet: **do not land**; record C `unchanged` and hand the fixed assembly + audit re-runs to the next round.

---

## 4. Claim Ca — landing contract

### 4.1 Defect verified

`corpus/README.md:1` and `:3` are byte-identical H1s; `grep -c '^# '` = 2; the sweep is heading-blind (`Ca01` §3, `Ca03`, `X05`, `R04`). The second duplicate `revision: 2.0` block at `:42`/`:44` is live and **undispositioned** (`Q-Ca3`); it is out of scope but must become a queue row.

### 4.2 Deletion variant — pin exactly one

| variant | edit | lines | sha256 | sponsors |
|---|---|---:|---|---|
| **A** | delete line 3 only | 574 | `84e16f566e170ac4be9d7f01d90ca1743640d36c899d9c81808c5dc8c0065633` | `Ca07` (recommends A) |
| **B** | delete lines 3–4 (H1 + blank) | 573 | `d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079` | `Ca01`, `Ca03`, `X05`, `W02`, `Q01` §5 |

I reproduced both shas byte-for-byte. **Recommend B**: single-blank spacing, six stagings agree, `Q01` lists `d407260d…`. A is the outlier. Both are sweep-neutral. The post-apply `readme_sha256` + H1 count are the only certificates.

### 4.3 Anchor shift

B shifts every later README anchor by **−2**: header `234→232`, calendar row `240→238`, costume row `241→239`, total `544→542`, footer `548→546`, rev-2.4 block `5→3`. A shifts by **−1**. A frozen C patch fails on a post-Ca tree (`W01` §4.5: 3 hunks ignored). **Apply both README edits in one content-anchored buffer**; re-derive anchors from the buffer.

### 4.4 Queue successor — one canonical id, not three drafts

`Q-Ca1`/`Q-Ca2` and `N02` leg 4: `r47-entry-overbuild-defect-class` (Ca02) and `r48-entry-quality-not-gated` (Ca06) both own the r47 over-build class, each counts incidence 1, each names the other as alias/instance; `W02` adds a third id (`r47-overbuilt-entry-draft`) and closes `R36` as `fixed-with-evidence` **before the fix is applied**. Filed as drafted this double-counts the class and claims a fix that does not exist.

Required `reports/round-48/calib/queue-successor-r48.json` (new file; parent `dfc9265d…` pinned, never edited):

1. `R36-README-DUPLICATE-HEADING` → **`fixed-with-evidence` only after apply**, with pre/post `grep -c` (2→1), post-apply README sha, sweep output, H1 control output. Parent row: `reports/round-40/op/defect-queue-v2.json:112` (`carried-with-owner`).
2. **One** over-build class row, canonical id `r48-entry-quality-not-gated` (Ca06), **`routed-with-owner`**, with Ca02's id folded as `instance_of` and W02's id as an alias in `reason`. It must say "no durable queue row exists", **not** "nowhere recorded" (`LOG.md:3906`, `SCORECARD.md:901,907-908` name it; `Ca04`).
3. A new row for the `revision: 2.0` duplicate at `:42`/`:44` — `routed-with-owner`, with byte-identity evidence (`Q-Ca3`).

The over-build row cites `790 = 51 head + 739 body`, the live 103–149–221 band, and every B1–B9 anchor. A `fixed-with-evidence` claim now would repeat the defect it describes (`Ca04`, `N02` leg 3).

### 4.5 Heading control — five drafts, one instrument

`reports/round-28/readme/sweep.py` is a filed artifact; editing `reports/round-1..47/**` is forbidden, so the claim's "added to the sweep" branch is **inadmissible** (`R04` F-2, `R01-48-06`; my grep: no heading leg). `Q-Ca4` counts **five** control drafts across five paths; none is applied. Pin **Ca05's** `tools/check-readme-heading.py` (244 lines, stdlib, read-only; 8/8 selftest; red `H1-COUNT lines=[1,3]` live, green `h1_lines [1]` on the 573-line copy), create it, run its selftest, run it red-before/green-after on the same path.

### 4.6 Ca acceptance gates

1. `grep -c '^# ' corpus/README.md` → **1**; exact-title count → **1**.
2. Diff = exactly the chosen deletion (A one line; B two lines) — no other heading, row, revision block, totals line or footer byte changed (`Ca07` legs 1–8; `Ca03`).
3. Sweep exit 0 after; if C also lands, `rows 224 files 224`, footer `25/26/26/29/24/94`.
4. One heading control exists, exits 0 post-apply; no write to `reports/round-28/`.
5. Queue successor filed with the three rows above, parent pinned, no premature `fixed` on the over-build class; `R36` closed only with post-apply evidence.
6. Recorded act: LOG append + SCORECARD row (integrator only).
7. Post-apply README `readme_sha256` recorded as the certificate.

---

## 5. Conflicts, errata, and moving-fragment hazards

| # | item | measured state | required action |
|---|---|---|---|
| 1 | README deletion variant | A `84e16f56`/574 vs B `d407260d`/573, both verified | pin one; B recommended |
| 2 | Entry byte source | A 227→228; B **239**; C withdrawn | pin B; C13's 181-line placeholder is discarded |
| 3 | Assembly rule | W01's "join whole fences" = 251 lines / 2 H1s | change to strip C01's head (W01 §3.2) |
| 4 | Extraction convention | C01 227 vs 228; `2a667749…` vs `e5255657…`; 238 vs 239 | pin fence-inclusive/exclusive + separator before citing any digest |
| 5 | Moving fragments | C13 rewritten (200 lines); W01 rewritten (492 lines); C01 file revised while its fence stayed stable; Ca06 observed at three digests | every verdict must name the digest it read; **do not reuse a line citation taken before the rewrite** |
| 6 | Over-build row id | three drafts, two ids | one canonical id + alias/instance (`N02`) |
| 7 | Heading control | five drafts, none applied | pin Ca05's tool |
| 8 | Topic line | C02 766 = seed; C01 1,045; C13 1,094–1,095 | choose B; README row must equal the seed |
| 9 | Couples set | 19 (C02) / 21 (K01) / 14 (C01) | pin the assembled header's set; re-run resolver |
| 10 | `targets.json` C10 "= 224" | rev-2.4 repair sums **223**; rev-2.5 sums **224** | record erratum; two lines, two sums (`R01-48-02`) |
| 11 | Freshness declaration | filed claims → could-not-evaluate; used overlay → exit 2; reconstructed overlay reproduces verdicts; Ca probe vacuous; O red is probe artefact | file overlay + JSON + a correction note in a **new** telemetry file; mark `to-verify` (`Q-R1`, `Q-R2`, `Q-R5`) |
| 12 | Declaration timestamp | `19:45:00Z` declared; mtimes `19:36–19:37Z`; ~370 s ahead of the system clock at sampling | do not cite as a measurement time (`Q-R3`) |
| 13 | `reports/round-48/claims.json:49` | in-tree `run-validation.py` — forbidden and nonexistent | author the runner; replay in isolated `git archive`; no in-tree execution |
| 14 | Staged shas | C10 `5767d3c4…`; D01 `4db8ecaf…`; C13 `7088ec9a…`; C11 fixture | none is a certificate; post-apply sweep is |
| 15 | `790` vs `739` | 790 = 51 head + 739 body | use the decomposition once (`R01-48-08`) |

---

## 6. Apply order (single wire)

1. **Pin route B** (C02 head + blank + C01 body, 239 lines), its digest and extraction convention; file the assembled artifact.
2. **Apply the eight-line fix pass**: D1 (3 lines), D2 (strip head), D3 (1 shelf line), U1 (agrarian row + token), DR tags (1–2 lines), self-ref removal, couples additions.
3. **Re-run the audits on those bytes**: C03, C04, C05, C08, C12, C14, E02, C09, **R03**. Abort on any blocking finding.
4. **Stage the README**: Ca variant B first, then C's rev-2.5 edits by content anchor; re-derive anchors after −2; run the sweep on a staged 224 tree and the H1 control.
5. **Apply atomically**: one new corpus entry (`A`) + `corpus/README.md` (`M`). Then live: 224 / 26 / sweep 224==224 / H1 = 1 / `git status` only those two corpus paths.
6. **Run V01's nine legs + F01's five numbers + A04's write-surface census + N03's landing safety** on the applied tree.
7. **File one queue successor** (three rows) and **one** heading-control tool; run their selftests.
8. **Close**: `validation.json`, telemetry closing snapshot (append-only; names the record it closes + its sha), SHONEN, SCORECARD row, LOG append.
9. **If step 3 or 5 fails**: stop. File C `unchanged`, Ca `improved` only if its disposition half is fixed and applied; round `rejected-honest-stop`.

---

## 7. Per-axis verdict candidates

| axis | candidate | condition required | status at cut |
|---|---|---|---|
| **coverage** | `unchanged` now; `improved` only if the fixed 239-line assembly lands | 224 / 26; sweep green; entry ≤250; audits on final bytes incl. R03; D1/D3/U1 closed | `could-not-evaluate` — C05 FAIL, R03 landing FAIL, Q01 not certified |
| **calibration** | `improved` only if Ca's README half and disposition half both land | H1 2→1; sweep green; R36 closed post-apply; one over-build row `routed-with-owner`; one control exits 0 | `could-not-evaluate` — README PASS-staged, disposition not fileable |
| depth | unchanged | no depth claim; `R03`'s depth PASS is a content judgement, not a depth axis-move | unchanged |
| operability | unchanged (or unclaimed observation if the heading tool lands) | new `tools/` control with selftest | unchanged |
| freshness | unchanged | pause in force; declaration `to-verify` | unchanged |
| adjacency | unchanged | A01/A02/A04 show no bleed and no corpus write; file-level one-owner | unchanged |

If Ca lands only the README fix (no queue/control), the Ca claim does **not** verify: record `unchanged` or `unprovable-but-better` only with a named non-author reviewer, and do not admit.

---

## 8. SHONEN

`S03` owns the paste-ready block: all four boxes are `[~]` carried, **no `[x]`**, no box moves this round (`S03` §0; `SHONEN.md` sha `7999d09b6b8e6f891947390207f171987bf662fb2bd91b2d1c7719ae1cf765ce`, untouched). `Q-R4` adds: box 2's chain leg and box 4's no-bleed leg remain `could-not-evaluate`. Do not claim `[x]` without a named non-author verifier (`SHONEN.md:10-11`).

---

## 9. Absent / `could-not-evaluate`

- No seat is absent. What remains absent: `reports/round-48/run-validation.py`, `reports/round-48/validation.json`, the telemetry observed-dispatch and availability-close files.
- The applied landing: target path absent; README H1 count still 2; census 223.
- The freshness overlay, candidates and JSON under `telemetry/` — only `.scratch` bytes exist.
- A staged sweep of the **fixed** route-B assembly (C13's 239-line stage is on the pre-fix bytes; C11 is a 136-line fixture; D01 is a prediction keyed to a different rev-2.5 wording).

---

## 10. Commands and write surface

```
$ git rev-parse HEAD                                    # a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l            # 223
$ ls corpus/knowledge/culture-material/*.md | wc -l     # 25
$ wc -l corpus/knowledge/culture-material/*.md          # 3756 total; min 103 / median 149 / max 221
$ python3 -B reports/round-28/readme/sweep.py           # rows 223 files 223 ... exit 0
$ python3 -B reports/round-28/readme/sweep.py --selftest# 12/12 checks passed
$ grep -c '^# ' corpus/README.md                        # 2
$ grep -o '^revision: [0-9.]*' corpus/README.md | sort | uniq -c   # 2 revision: 2.0
$ sha256sum corpus/README.md                            # 7c788a1d...
$ sha256sum reports/round-40/op/defect-queue-v2.json    # dfc9265d...
$ sha256sum reports/round-47/calib/queue-successor-r47.json  # 9508b6aa...
$ grep -n 'R36-README-DUPLICATE-HEADING' reports/round-40/op/defect-queue-v2.json  # :112
$ python3 (extract C01 fence; C02 fence; assemble)      # C01 227; C02 head 23; route B 239 (C05/R03/C13)
$ python3 (delete README line 3 / lines 3-4)            # 574 84e16f56... / 573 d407260d...
$ python3 -c "print(25+23+25+29+24+94, 25+23+26+25+24+94, 25+26+25+29+24+94, 25+26+26+29+24+94)"
                                                        # 220 217 223 224
```

**Write surface:** this file only, plus disposable `.scratch/s01/` probes. No `corpus/**` byte was written or staged; no `tools/**`, `LOG.md`, `SCORECARD.md`, `SHONEN.md`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet path was touched. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed.
