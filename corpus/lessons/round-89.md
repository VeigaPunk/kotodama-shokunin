# Round 89 — re-verifying the recheck queue and an evidentiality entry

author: kotodama lane (including its dispatched seats), 2026-11-04.
Claims: F / freshness — live re-verification of the 16 URL-bearing rows of the
registry's upcoming-recheck queue; C / coverage — a dedicated entry
`corpus/knowledge/linguistics/evidentiality-epistemic-marking.md`.
Base `42816d2533c44f1d19f38a12fc5f5040d01a2fd3`; claims, counter, executed
controls, counter selftest and its red-before land together in freeze
`1cbd0efc56edaa9394e3532fc5d8ef924f122f01`; wave spec/dispatch and the
do-nothing counter runs at the freeze (F 3/5, C 2/8) land at
`9ad00be1a48d33a4f54e1663a1d46e4590cc3438`.
`reports/round-89/claims.json` (sha256 `cd74cfc2…`) and `measure89.py`
(sha256 `6bc14bcd…`) remain unchanged after data.

## Gate

Opened sources, access 2026-11-04 (America/Sao_Paulo, −03:00). Tier scope is
the exact use, not a general certificate. No bot challenge or login was passed.

### F — re-verification of the sixteen queue rows (recheck old→new logged per row)

Every row below was fetched by ExecRecheckA/B (curl) and independently by
ReviewerRefetch (python urllib); each executor quote occurs in the
independent capture as well (`reports/round-89/rechecks/refetch-agreement.json`:
16/16). Captures and manifest: `reports/round-89/rechecks/`. The new recheck
`2027-02-03` keeps the rows' 90-day cadence counted from today (CriticClaims
finding 2c), not a longer one.

- S009 LOCATED recheck 90d→2027-02-03 — https://cals.info/statistics/ accessed 2026-11-04: “145 features 97.9% of all features are from WALS” — Quick numbers table still lists 1323 conlangs, 127 natlangs, 145 features and 97.9% of features from WALS, matching the census figures in teaches.
- S012 LOCATED recheck 90d→2027-02-03 — https://arxiv.org/abs/2508.06094 accessed 2026-11-04: “injecting randomness to encourage diversity and leveraging self-refinement feedback to encourage consistency in the emerging language description” — Abstract (now v4, revised 17 Apr 2026) still states the randomness-for-diversity and self-refinement-for-consistency design named in teaches.
- S020 LOCATED recheck 90d→2027-02-03 — https://arxiv.org/abs/2603.19283 accessed 2026-11-04: “identified 2,670 motif expressions of 200 different motifs across 58,450 sentences” — Abstract still gives the 2,670 expressions / 200 motifs / 58,450 sentences corpus; it also states the fine-tuned Llama3 0.85 F1 result.
- S021 LOCATED recheck 90d→2027-02-03 — https://arxiv.org/abs/2606.17350 accessed 2026-11-04: “LLM-generated narratives are consistently more similar to each other than human-written stories are” — Abstract (now v2, revised 2 Sep 2026) still states the cross-model homogeneity finding; it also reports frontier convergence and failed negative prompting/temperature mitigations.
- S031 LOCATED recheck 90d→2027-02-03 — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0287101 accessed 2026-11-04: “Of the 63 different foraging societies, 50 (79%) of the groups had documentation on women hunting” — Results still report 50 of 63 societies documenting women hunting (and 36 of 41 intentional), the figure the teaches cell carries.
- S032 LOCATED recheck 90d→2027-02-03 — https://doi.org/10.1016/j.evolhumbehav.2024.04.014 accessed 2026-11-04: “Female foragers sometimes hunt, yet gendered divisions of labor are real: a comment on Anderson et al. (2023)” — Crossref CSL-JSON for the DOI still carries the title-level counter-position (and 54 references, issued 2024-07) that is all the teaches cell claims.
- S033 LOCATED recheck 90d→2027-02-03 — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0309543 accessed 2026-11-04: “concerns were raised about the reliability and replicability of the results” — Correction notice still opens with the reliability/replicability concerns and carries the Definition of forager and Selection criteria sections named in teaches.
- S084 LOCATED recheck 90d→2027-02-03 — https://www.signwriting.org/ accessed 2026-11-04: “Sign Languages are written languages!” — Home page banner still carries the maintainer statement quoted in teaches.
- S104 LOCATED recheck 90d→2027-02-03 — https://glottolog.org/resource/languoid/id/lsfi1234 accessed 2026-11-04: “Pseudo Family: LSFic Classification open LSFic” — The page heading still names LSFic as a Glottolog 5.3 pseudo-family node (lsfi1234); the FSL/ASL children are carried only in the script-embedded classification tree, which the text conversion drops, so the quote backs existence/naming (the row anchor "Page heading") and ASL-under-LSFic is independently shown by the amer1248 JSON row below.
- S105 LOCATED recheck 90d→2027-02-03 — https://glottolog.org/resource/languoid/id/amer1248.json accessed 2026-11-04: “{"name": "LSFic", "id": "lsfi1234", "url": "https://glottolog.org/resource/languoid/id/lsfi1234"}, {"name": "ASLic", "id": "asli1244",” — The amer1248 JSON classification array runs Sign Language > L1 Sign Language > LSFic > ASLic > American Sign, so ASL lineage is through LSFic with no English node.
- S106 LOCATED recheck 90d→2027-02-03 — https://glottolog.org/resource/languoid/id/bsli1234 accessed 2026-11-04: “The BANZSL subgroup is argued by Adam Schembri and Kearsy Cormier and Trevor Johnston and David McKee and Rachel McKee and Bencie Woll (2010)” — The Comments on subclassification state the BANZSL subgroup is argued (citing Schembri et al. 2010, Johnston 2003) alongside lexicostatistical and historical evidence for BSLic.
- S107 LOCATED recheck 90d→2027-02-03 — https://glottolog.org/resource/languoid/id/banz1243.json accessed 2026-11-04: “'British Sign Language [brit1235][bfi]-l-':1,'New Zealand Sign Language [newz1236][nzs]-l-':1)'BANZSL [banz1243]':1” — The banz1243 newick field lists British Sign Language and New Zealand Sign Language (after the Auslanic clade containing Auslan) as children of BANZSL.
- S142 LOCATED recheck 90d→2027-02-03 — https://web.archive.org/web/20250331081615/https://historicbrass.org/images/hbj/hbj-2008/HBSJ_2008_JL01_002_Cheney.pdf accessed 2026-11-04: “suggesting by the lack of uniformity that their primary function was that of a memory aid for a repertoire transmitted orally from teacher to pupil” — The anchored paragraph still states the notated signals served as a memory aid for an orally transmitted teacher-to-pupil repertoire.
- S157 LOCATED recheck 90d→2027-02-03 — https://ich.unesco.org/en/RL/whistled-language-of-the-island-of-la-gomera-canary-islands-the-silbo-gomero-00172 accessed 2026-11-04: “two distinct whistles replace the five Spanish vowels, and there are four whistles for consonants” — The UNESCO summary still gives two whistles for five vowels and four for consonants (same paragraph: Castilian Spanish, more than 22,000 inhabitants, pitch/interruption; Biomes block lists Mountains).
- S163 LOCATED recheck 90d→2027-02-03 — https://ich.unesco.org/en/USL/whistled-language-00658 accessed 2026-11-04: “The practice developed as a result of the steep mountains and rugged topography of the region” — The UNESCO summary still ties the origin to steep mountains and rugged topography (same paragraph: agricultural communities outdoors, decline in practitioners and areas).
- S875 LOCATED recheck 90d→2027-02-03 — https://online.bunka.go.jp/db/heritages/search accessed 2026-11-04: “旧石器 [日本]縄文 [日本]弥生 [日本]古墳 [日本]飛鳥 [日本]奈良 [日本]平安 [日本]鎌倉 [日本]” — The live 文化財検索 form still offers the official 時代 period ladder (旧石器…令和 [日本], plus China/Korea ladders) and the 分野 domain tree used to file objects.

Row-level caveats retained, not repaired (OTHERCELLS forbids it this round;
carry to round 90): S032's 2xx body is the Crossref CSL-JSON record reached by
`Accept` negotiation on the DOI (bare GET is a redirect stub; ScienceDirect
403) — it re-verifies only the row's stated title-level scope; S104's
FSL/ASL children live in a script tree the text capture drops (existence and
naming only; ASL-under-LSFic is shown by S105); S142's anchor quotes "used
by these hunting signals" while the PDF reads "used for" — the row URL is a
fixed 2025-03-31 Wayback snapshot, so S142 is an immutable-archive re-locate,
not drift detection; S012's anchor says "arXiv v1", the page is now v4, and
S021 is now v2; S157's Biomes block now lists three biomes; S105 is queued and
already superseded in practice by S126. No teaches cell was found false. No
row is NOT-LOCATED.

### C — sources opened for the evidentiality entry

- **S936 admit A/mined.** https://wals.info/chapter/77 — accessed 2026-11-04 — section 1 Defining the values, closing sentence before section 2: “There are no languages in the sample that have grammaticalized direct evidentials, but no grammaticalized indirect evidentials.” Grounds: chapter author's own value definitions and Map 77A counts (181/166/71 of 418); scope is the WALS sample, not world frequency. Capture reports/round-89/evidence/S936.txt.
- **S937 admit A/mined.** https://wals.info/chapter/78 — accessed 2026-11-04 — section 1, paragraph introducing example (6) Dumi: “When a language uses separate particles for evidentiality, this is very strongly correlated with coding indirect evidentiality only.” Grounds: chapter author's coding typology and Map 78A counts (131/24/65/7/10, none 181); sample-bound. Capture reports/round-89/evidence/S937.txt.
- **S938 admit A/mined.** https://lassoling.org/wp-content/uploads/2020/12/18.1-1999.pdf — accessed 2026-11-04 — SWJL 18.1 abstracts page, de Haan abstract sentence 4: “Evidentials assert the nature of the evidence for the information in the sentence, while epistemic modals evaluate the speaker's commitment for the statement.” Grounds: author's own published abstract; A only for his stated thesis, article body not read. Capture reports/round-89/evidence/S938.txt (pdftotext).
- **S939 admit A/mined.** http://www.nicolas-tournadre.net/wp-content/uploads/multimedia/2014-evidentiality.pdf — accessed 2026-11-04 — section 4, paragraph after the Gawne example: “Grammatical evidentials may serve as a very subtle tool for lying and manipulation” Grounds: authors' preprint of LTBA 37(2) with their own Tibetic field data; contested positions attributed to them. Capture reports/round-89/evidence/S939.txt (pdftotext).
- **S940 admit B/mined.** https://glossary.sil.org/term/evidentiality — accessed 2026-11-04 — Definition, first paragraph, final sentence: “Evidentiality is distinct from (epistemic) modality which concerns the speaker’s evaluation of his or her statement, for example, with regard to its certainty.” Grounds: signed glossary definition (Greed 2022); B at glossary depth only. Capture reports/round-89/evidence/S940.txt.
- **S941 reject C/rejected.** http://www.glottopedia.org/index.php/Evidentiality — accessed 2026-11-04 — Definition, first sentence: “Evidentiality is a way of marking epistemic modality, i.e. how we know something is true.” Grounds: unreferenced stub (page carries its own reference-needed block) conflating the category with epistemic modality; flip: a referenced revision citing a Turkmen grammar and stating the boundary as contested. Not cited by the entry. Capture reports/round-89/evidence/S941.txt.

Registry changes: sixteen population rows change only `recheck` 90d→2027-02-03
(lines above); S936–S941 are additions (S936–S939 A/mined, S940 B/mined, S941
C/rejected); no `status` or `used-by` cell of an old row changes. The entry
cites none of the sixteen population ids (ConnectorSiblings cross-claim guard).

**Known survivors.** Stated before data: a capture fabricated with its quote
pasted in passes F and C (`reports/round-89/controls/controls.txt`). Found by
the wave and NOT declared before data: site-chrome or title quotes over
genuine captures, shadow duplicate registry rows, any-year Wayback URLs,
capture path = graded file, NOT-LOCATED spelling variants, `export-ignore`,
off-topic or copied filler entries (ReviewerCounter H1–H4, M1–M4;
CriticClaims findings 2–3) — R89-M5/M6 below. This landing's own exposure to
each is audited in `reports/round-89/final/honest-landing-audit.json`.

**Independent spot-check:** pending outside closure. Dispatched seats and L1
are the lane, not non-author verifiers. No promotion box becomes `[x]`.
Assimilation: none; no considerthese directory in this lane.

## Understanding and trial

F is the first round that consumes the round-82 recheck auditor's queue: at
base `RECHECK-QUEUE: 0 due / 20 upcoming / 16 on-release / 859 rows`; the four
own-work repo-path rows (S859, S860, S929, S934) are not live surfaces. All
sixteen URL rows were still locatable on 2026-11-04; three surfaces had moved
(two arXiv revisions, one UNESCO metadata block) without contradicting their
rows. ScoutOverlap: these rows are 10–16 days old and several were re-opened by
earlier closures, so F is a short-interval liveness check, not drift repair.

C: at base the lane held evidentiality as sub-sections — `semantics-pragmatics.md`
§4 (lines 66–82, inventory-size effects, Willett hierarchy, a 3×5 table) and
`syntax-typology.md` §4 (a sizing table) — not merely the "scattered
sub-bullets" the frozen surface text says (R89-M4). The new entry adds what
those sections lack: WALS 77A value counts with sample bounds, the 78A coding
axis and its particle/indirect generalisation, the evidential/epistemic
boundary recorded as contested (de Haan vs Tournadre & LaPolla), access and
egophoric marking with the anticipation rule, areal spread, and a NON-CANON
design; it couples back to both sections instead of copying them (8-word
shingle overlap 0 with five neighbouring entries). Registry had no
evidentiality or WALS chapter row at base.

## Mistakes

| id | class | evidence | captured-by | fix or retained limit |
|---|---|---|---|---|
| R89-M1 | vacuous (prior round, repaired prospectively) | R88-V2 / R88-M2: `measure88.py --selftest` exit0 while its positive child exits1 on FileNotFoundError (`reports/round-88/counter-selftest-false-green.json`). r89: `measure89.py` selftest accepts the clean positive only on `ACCEPT-<c>-89: PASS legs=N/N` in child stdout with empty stderr (measure89.py:513), each negative only on observed rc1 plus `LEG FAIL <leg>` (:517), and keeps every child's stdout/stderr (`counter-selftest.txt.json`, 21 rows); `counter-selftest.txt` PASS 21/21 | QUALITY35, QUALITY23 | Fixed in the r89 counter at freeze, before dispatch. Red-before `reports/round-89/selftest-redbefore.txt`: BACKED forced true (mutant sha256 `80a8aa56…`) → selftest FAIL 18/21, exit1, bumponly/wrongquote/badurl BAD; ScribeLesson reproduced the same mutant hash and the same 18/21 exit1 (`.ufo/waves/round-89/w1/stage/ScribeLesson/receipts/redbefore-repro.txt`). Limits: the red-before mutates one leg only; the other legs' ability to fail rests on their negative scenarios, not on mutants; the mutant bytes are not committed (reproducible from the one-string substitution). `measure88.py` stays a historical false green. |
| R89-M2 | reference-drift (prior round, located this round) | r88 `controls/extra-id.py:11` and `controls/shotgun-all-labels.py:12`: `ROOT = KOTODAMA_ROOT or Path(__file__).resolve().parents[2]`; for `reports/round-88/controls/<c>.py`, `parents[2]` is `<lane>/reports`, so the fallback names `<lane>/reports/tools/check-attestation-packet.py`, which does not exist. Without the variable both controls score 0/13 (case rc2 `can't open file`) in the lane worktree and in a shared clone at base; with `KOTODAMA_ROOT=<lane>` extra-id scores 4/13 (`.ufo/waves/round-89/w1/stage/ScribeLesson/receipts/r88v3-controls-noenv.txt`) | R88-V3 (non-author closure); cause located by ScribeLesson | R88-V3 called the variable undocumented; it is in fact mandatory, because the fallback can never resolve a tree root. SKILL's r88 note ("otherwise depend on the live working tree or fail their fallback path") is half right: only the failure branch happens. Control bytes stay frozen; documentation notes under R88-V3 below. constant-pass and filename-only read neither the variable nor the fallback. |
| R89-M3 | reference-drift (this round) | `claims.json` `separability` names `reports/round-89/separability89.py`, absent at freeze `1cbd0efc` and dispatch `9ad00be1` (CriticClaims 5; ScribeLesson) | QUALITY7/9 | Separability is not a frozen leg. The script lands post-dispatch, labelled as such, with deterministic overlay commits reproducible from committed revisions (`reports/round-89/final/separability.json`). |
| R89-M4 | calibration (this round) | `claims.json` C `surface`: "only scattered sub-bullets"; `git show 42816d25:corpus/knowledge/linguistics/semantics-pragmatics.md` has heading `## 4. Evidentiality and mirativity` (line 66) and syntax-typology.md §4 a sizing table (ScoutOverlap a; CriticClaims 3) | none | The before-state of a coverage claim quotes `grep -rn -i '^## .*<topic>' corpus/knowledge` at base. Able to fail: at base that grep prints the semantics-pragmatics §4 heading, contradicting the frozen surface sentence. QUALITY36 binds round 90. The frozen text is not amended; the report rates C's surface as contested. |
| R89-M5 | survivor (this round) | MutationCounter: 10/41 non-equivalent mutants killed by the selftest, 2/41 by the controls | QUALITY11, QUALITY35 (met in form only) | QUALITY36: one negative per sub-check and a committed mutation-score receipt before dispatch. Round-89 frozen counter unchanged. |
| R89-M6 | survivor (this round) | ReviewerCounter H1–H4, M1–M4 and CriticClaims 2–3: committed fixtures pass F 5/5 or C 8/8 without teaching-bound quotes, with shadow rows, any-year Wayback, capture = graded file, or off-topic/copied filler | QUALITY34 | Declared bound was too narrow (forged capture only). This landing is audited against every listed class in `reports/round-89/final/honest-landing-audit.json`; QUALITY36 binds successors. |
| R89-M7 | governance (this round) | `.ufo/l0-questions.md` kotodama round-11 line ends "Freshness axis-move claims are paused until ruled"; claims.json says F "does not depend on" it (CriticClaims 1; ScoutOverlap b) | none | The pause text covers the claim class, not only the drift threshold. F is reported as measured with admission left to the closure/operator, and an L0 question asks whether live source re-verification falls inside the pause. |

## R88 routed-defect dispositions

| item | disposition / pointer |
|---|---|
| R88-V1 | Both r89 declared counters carry `--work <existing-dir>` (`claims.json` F/C `counter`; SCORECARD round-89 plan "Both declared commands carry `--work` (R88-V1)"). The r88 `claims.json` D `counter` still omits it (verified: `reports/round-88/claims.json` line 34) and stays frozen; the SCORECARD round-88 D row says "same counter with `--claim D`", i.e. inherits the O row's `--work`. Proposed appended SCORECARD note: "R88-V1: the round-88 D counter as declared in `reports/round-88/claims.json` exits 2 without `--work`; the valid command is `python3 -B reports/round-88/measure88.py --root <clone> --base 4956282281dac1306cfbe59523e46dde99749d75 --lands <lands> --claim D --work <existing-dir>`, the frozen declaration is not edited." |
| R88-V2 | Repaired prospectively in the r89 counter: R89-M1. QUALITY35 binds and is met at freeze; `measure88.py` not retrofitted. |
| R88-V3 | Verified and sharpened: R89-M2. Proposed text appended to the SKILL `finding-set-comparator` row's pinned-values cell (column 6; keeps 8 cells, adds no path to the entry-command cell that `tools/check-gate-registry.py` scans): `; control candidates reports/round-88/controls/shotgun-all-labels.py and extra-id.py resolve the honest auditor only through KOTODAMA_ROOT=<lane root or committed clone> — their parents[2] fallback is <lane>/reports, so without the variable they score 0/13 with case rc2, not 4/13; constant-pass.py and filename-only.py need nothing`. Proposed appended SCORECARD note (round-89 axes section, not an edit of the r88 row): "R88-V3: the round-88 counterfeit controls shotgun-all-labels and extra-id require `KOTODAMA_ROOT` set to the lane root or a committed clone when scored by `tools/check-finding-sets.py` or `measure88.py`; their `parents[2]` fallback resolves to `reports/`, so a run without it reports 0/13 (an environment miss), not a discrimination result. Receipt: `.ufo/waves/round-89/w1/stage/ScribeLesson/receipts/r88v3-controls-noenv.txt`." |
| R88-V4 | r89 wave registry (`.ufo/waves/round-89/w1/swarm-registry.json`, 11 seats) names four canonical attack seats — ReviewerRefetch, ReviewerCounter (reviewer), CriticClaims (critic), MutationCounter (mutation-tester) — 4/11; no sentinel. All four delivered reports (`.ufo/waves/round-89/w1/{ReviewerRefetch,ReviewerCounter,CriticClaims,MutationCounter}.md`); no attack seat died. |
| R88-V5 | R89-M3. `reports/round-89/separability89.py` (ExecSeparability, authored after dispatch, not a frozen leg) builds deterministic overlay commits (fixed identity and dates) from the committed freeze and lands, records per-file sha256 and the full procedure, and its rerun reproduces the same overlay trees; receipt `reports/round-89/final/separability.json`. |
| R88-V6 | No action: `.ufo/waves/round-79/w1-results.json` is not cited by any r89 claim, control or receipt (no `round-79` reference under `reports/round-89/` or in `spec-v1.json` at `9ad00be1`). |
| R88-V7 | Inherited debts remain open and are not closed by this round: formal L2-planner conflict (L1 holds the planner seat; the validator rejects planner as a swarm role), numeric/lowest-axis mapping (R86-C1), full cited-record red from non-author r84, round-51/round-69 L0 questions. F is a freshness axis move although the lane's own round-11 L0 line says freshness axis-move claims are paused until ruled (R89-M7); an L0 question asks for the ruling. |

## Settlement

One v1 wave (`kotodama-r89-v1`), 11 seats: 3 executor (ExecRecheckA,
ExecRecheckB, ExecSeparability), 2 scribe (ScribeEvidentiality, ScribeLesson),
1 scout (ScoutOverlap), 1 connector (ConnectorSiblings), 2 reviewer
(ReviewerRefetch, ReviewerCounter), 1 critic (CriticClaims), 1
mutation-tester (MutationCounter); attack 4/11. All eleven delivered reports;
no seat died, none replaced, no residual call. L1 holds planning.
Measured results are appended below after landing, not invented here.

First measurement at lands `590c20671f38dff203fdd879235fd61b61a9aff7`: F
FAIL 4/5 — BACKED `S105: quote absent from capture`
(`reports/round-89/final/lands-F-first.txt`). Cause: the S104 line's trailing
prose named S105, so the counter's first LOCATED line for S105 was S104's,
carrying S104's quote. Fix in the records only: that prose now says "the
amer1248 JSON row". The frozen counter, claims and every capture are
unchanged; the final F measurement below is at the corrected lands.

Final measurement at lands `aac9cca80d12077eb3026b202c835c0d6135bc08`: frozen `measure89.py` rc0 PASS 5/5 for
F (ADVANCED 16, BACKED 16/16, DISPOSED, OTHERCELLS) and rc0 PASS 8/8 for C
(ENTRY 19901 B/10 headings, TABLE 5×6, NEWIDS S936–S940, GATE, CAPTURE,
INDEX tool rc0, APPENDONLY) — `reports/round-89/final/lands-{F,C}.txt`.
Separability overlays PASS 5/5 and 8/8 (`final/separability.json`). Audit of
the wave's survivor classes on this landing: no duplicate ids, captures only
under the round dirs, full local ISO fetch times, no NOT-LOCATED variants, no
`.gitattributes`, entry cites no population id, re-fetch agreement 16/16;
one archive-backed row (S142, its own fixed snapshot) and one title-scope
quote (S032) remain as stated (`final/honest-landing-audit.json`). Registry
859→865, census exit 0 both ends, recheck queue 20→4 upcoming. WAVE-DONE
received before the report; seat table in `.ufo/waves/round-89/w1-results.json`.
