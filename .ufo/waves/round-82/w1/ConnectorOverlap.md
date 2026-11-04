# ConnectorOverlap — r82 w1 report (claims O + D, cross-axis overlap)

Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `c285b2afb19d4b64320e18df1f55e426bf2d0b0c` (read-only
throughout: `git -C <lane> show|grep|ls-tree <base>`, fleet scripts invoked over a **scratch copy** of the base
blob). Axes worked: **adjacency** (overlap map + one-way pointers) and **coverage** (every named surface, plus
two surfaces nobody had: the fleet `overdue` implementation and the README index drift). No network access, no
fetches, no installs. No lane file, jj/git state, or fleet path written.

Artifact: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ConnectorOverlap/overlap.md`
(24-file classification table, the coupling table, the O consumer scan, the move).

## 1. Claim D — overlap verdict

No knowledge file owns guest-right as an institution. Broad sweep (`guest|hospitality|hospit|xenia|
suppliant|supplication`, ci, `corpus/knowledge/`): **35 files**; topic-line owners: **3**, of which one
(`medicine-healing-codes.md`) is the *hospital* homograph; `^- gap filled:` owners: **0**; the exact
institution words `xenia|hospitium|guest-friend|theoxeny`: **0 files / 0 lines**. This agrees with ScoutGap
(15 files / 27 lines on its narrower pattern; mine is a superset — the reconciliation is written into
`overlap.md` §0 so two honest numbers are not read as a defect).

Classification, in the form the entry needs for `- gap filled:` / `- couples:` (full quotes in `overlap.md` §1):

- **owns** — `cuisine-food-lexicon.md:95,138,170` (salt/bread token + loyalty lexemes: "The guest-host bond is
  lexicalized as *taste*"); `sacred-topography-pilgrimage.md:92` (visitor **access law**: who may enter, when,
  in what state); `architecture-settlement-lexicon.md:30,57,124,125` (threshold furniture, guest court,
  drip-line as legal strip); `orality-formulaic-language.md:66` (arrival type-scene beat order);
  `register-strata-attestation.md:88,136,206` (`QREG-08` the guest's charge — "binds at the gate; may not write
  the roll", `not-rollable`); `myth-folktale-genres.md:55` (ATU 750–849 "God/saint-in-disguise hospitality
  tests"); `synthesis/conlang-blueprint-template.md:126` (lexicon slots **091:guest / 092:host**, and its T1
  test sentence at `:85` is a guest arrival).
- **mentions** — `ritual-liminality.md:21` ("safe-conduct (the guest's token)"); `naming-systems.md:106`
  ("renaming = rebirth/sanctuary"); `number-symbolism.md:118` (**calibration hazard**: "'Loki the 13th guest'
  origin of the 13 taboo: modern reconstruction" — do not use thirteen-at-table as ancient evidence);
  `purity-pollution-boundary-systems.md:33,73` (*pharmakos*); `sacred-kingship-mythic-charter.md:111,159`
  (stranger-**king**); `furniture-interior-lexicon.md:69` (the guest's bed as legal object);
  `civilizations/{pacific-northwest,ainu,celts,thrace-dacia,arabia-pre-islamic,greece-classical}.md` (real-world
  cases; thrace-dacia `:111` owns the host/guest comparison *method*, `:105` warns against conflation);
  `creation-myths-taxonomy.md:49` (the unbuilt hook "guest-right owed to the muskrat's kin").
- **hands off (0 hits)** — `binding-speech-complex.md` (nearest `:138` "hostages and sureties"; `:127` oath
  ring), `politeness-taboo-euphemism.md` (nearest `:57` the **bystander axis**), `synthesis/coupling-model.md`
  (nearest `:77` scene-scale brief), all three measured with `grep -ci` = 0.

Couplings to declare one-way (who owns / what the entry returns) are tabulated in `overlap.md` §2, and the
sibling-claim report is there: the natural absorbers would be greece-classical (*xenia* as a case),
register-strata (the charge), cuisine (the token); canon stays lore-shokunin's.

## 2. Claim O — existing `recheck`-cell consumers (defects included)

Sweep: `git grep -ln 'recheck' <base> -- tools/ 'reports/round-*/accept-*.py'` + `tools/*.py` (V-list in
`overlap.md` §8). Verdict per hit is in `overlap.md` §5; the load-bearing findings:

- **No lane tool computes a due date** (`timedelta|datetime` appears in `tools/*.py` only in
  `exercise-handoff-e2e.py`). `check-row-fragments.py:131` binds `_recheck` and ignores it;
  `check-supersession-settlement.py:90` destructures and ignores; `check-source-access.py:106` carries it in a
  header literal. Zero overlap with the new arithmetic, zero contradiction inside `tools/`.
- **But the fleet already implements it.** `scripts/sources-census.sh` mode `overdue` (`:675-686`):
  `due = opened + N days` for `NNd`, ISO date = itself, symbolic cadences never overdue, printing
  `overdue <id> <N>d recheck=… opened=…` plus one `cadence` line per cadenced row. Ran it on a scratch copy of
  the base registry: `--today 2026-11-04` → exit 0, **673 cadence / 0 overdue**; `--today 2027-05-03` → exit 1,
  **673 cadence / 267 overdue**; `census` → `rows 827`; `validate` → **0 E09**. So claim O's honesty frame is
  *contract conformance + error discipline + quiet in-lane output*, **not** a new fleet capability (defect
  D-O4). Its real delta: one summary line, `DUE <id> <iso-date>` (dates, not days-past), exit 2 on malformed
  input, `on-release` as the only exempt token, and an `--window` band the fleet script has no analogue for.
- **Defects (reported, not repaired).** D-O1 row-grammar split: frozen census and `check-source-access.py`
  match `^\|` (0 indents), while the contract and the fleet selftest (`:287`, widths 0–3) accept 1–3 — base has
  0 indented rows, so numbers agree today only. D-O2 vocabulary split: fleet `symbolic()` =
  `^[A-Za-z][A-Za-z0-9 _-]*$` and `RECHECK_RE` in `reports/round-73/accept-c.py:147` accept `annual`/
  `quarterly`; `round-75/76` dropped the ISO branch; the round contract accepts only `on-release` → a
  census-green `annual` is recheck-fatal. D-O3 no status filter: contract-correct, but 37 `rejected` + 58
  `queued` rows are counted (at 2027-10-24 the queue is 813/827). D-O5 nothing checks that an entry's
  `- recheck:` prose equals its rows' cadence cells.
- **Ready-made oracle** (mine, independently reproduced by ScoutRegistry's parser and by the fleet script):
  `RECHECK-QUEUE: 0 due / 18 upcoming / 14 on-release / 827 rows` at `--as-of 2026-11-04 --window 90`; 267 due
  at 2027-05-03. Registry census: 827 rows, all 11 cells, 0 indented, 0 malformed; cadence 659 `NNd`
  (392×365d, 249×180d, 18×90d) + 154 ISO (42×2027-10-22, 112×2027-10-23) + 14 `on-release`; all 154 ISO cells
  equal `opened+365` exactly (0 divergence). The queue is a **cliff** (0/18 → 25/242 → 267/0 → 267/540 →
  695/118) because `opened` spans only 2026-10-19…11-01: `due = 0` today is correct, and the DUE branch has no
  real-data exercise at the base as-of date.

## 3. Surfaces nobody else had

- **S907 has an in-lane positive control.** S903 (round 81) opened the **same Wikisource 1911 EB slug family**
  by plain `curl -sL`: HTTP 200, 87230 bytes, article prose (`reports/round-81/evidence/S903.txt`). The planned
  reject ("plain fetch returns the Wikibase scaffold") therefore needs the canonical-slug probe **plus** the
  S903 slug re-run as control in the same session/UA, and the reject reason must name the artifact (QUALITY
  21/22/24/27). S905↔S320 duplicate-document finding reproduced (S320 = Bellows Poetic Edda, Gutenberg
  #73533, full text, scoped Völuspá + Grimnismol 39). S904/S906 clean.
- **README index drift (coverage).** At base: 255 files (95/42/32/33/29/24) but index rows missing for
  `myth-symbol/ordeal-judicial-proof-rituals.md` (r81) and `culture-material/maritime-seafaring-lexicon.md`;
  headings read `## myth-symbol/ (32)` and `## culture-material/ (41)`; footer "total 253". The guest-right
  landing must reckon **255 → 256** and `## myth-symbol/ 32 → 34`, or state that it inherits the drift.
  No seat in this wave owns README — that is the one coverage hole I could name but not fill.

## 4. Proposed move (one, bounded)

Declare **one cadence value for the round** — `180d` on all four rows, and the entry header in the existing
house form (`- recheck: 180 days, per row (`corpus/SOURCES.md` recheck cells).`, the exact string five entries
already use) — then have the **L1, post-merge, outside both claims' acceptance** run one invariant:
`check-sources-recheck.py --as-of 2026-11-04 --window 90` → `0 due / 18 upcoming / 14 on-release / 831 rows`,
and `--as-of 2027-05-03` → `271 due` with `DUE S904…S907 2027-05-03` present; the fleet
`scripts/sources-census.sh overdue <lane> --today 2027-05-03` must agree (271 rows; 267 on base). This gives
the tool the only real-data DUE exercise the round can cheaply create, and makes the entry's prose horizon and
its rows' cells one checked value (closes D-O5).

Risks: `365d` instead of `180d` keeps 267 and demonstrates nothing — declare the value before either seat
writes; `S907` is `rejected` and will appear in the DUE list (contract-correct per D-O3) unless it is given
`on-release`, which shifts the count to 270 and must then be stated; the merged-tree run must stay out of
`accept-o*` or QUALITY 7 separability breaks; if a critic presses D-O4, the two-implementation agreement
(0 and 267/271) is the answer.

Axes: operability and adjacency improve; coverage improves by naming the README hole; calibration untouched
(no new claims, no canon). Nothing harmed.

## 5. Files written

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ConnectorOverlap/overlap.md`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ConnectorOverlap/receipts/`
  — `od-2026-11-04.txt`, `od-2027-05-03.txt`, `census.txt`, `validate.txt` (fleet cross-check raw output)
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/ConnectorOverlap.md` (this file)

Scratch `/fast/scratch/hyaku/kotodama-r82/ConnectorOverlap/` removed after the receipts were copied.
Tool installs: none.
