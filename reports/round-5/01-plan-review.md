# 01 — Plan review: causal separation, falsifiability, unresolved-row coupling trace, regression and adapter debts

- role: 01 PLANNER + CONNECTOR (author-side planning evidence; **not** an admission decision, no SHONEN, no canon, no rank, no commit)
- baseline revision: `1ccb2b7119039d8026ad1d004f20427623838b94`; at write time `git log -1` == baseline and `git diff 1ccb2b7..HEAD -- tools/` is empty — nothing is committed since baseline
- inputs read: `reports/round-5/flash-claims.json`, `reports/round-5/flash-authorization.json`, `SCORECARD.md`, `tools/check-craft-exercise.py` (working-tree copy), `reports/supplement-opencode-1/29-local-boundaries.md`; debt context from sibling reviews `26-parser-controls.md`, `30-mutation-evidence.md`, `22-label-representation.md` and the prior `01-plan-review.md`
- I redefined no declared target: everything in §3–§6 is an evidence requirement or regression pin **on top of** the two declared claims.

## 0. Vintage warning (measured, load-bearing)

The working tree carries **uncommitted in-flight sibling work**: `M tools/check-craft-exercise.py`,
`M LOG.md`, `M SCORECARD.md`, untracked `tools/check-gate-battery.py`, `reports/round-5/14-source-review.md`
(`git status --porcelain`). The craft checker changed **under this review mid-run**: my first Read saw a
`main()` with bare `path = argv[1]` and no CLI-error strings; minutes later the same working-tree file
printed `CLI-ERROR CRAFT-CLI-*` lines. Consequences: (i) every before→after for claim O must be measured
from `git show 1ccb2b7:<path>` bytes, never the live tree; (ii) the in-flight battery and the CLI
hardening are sibling deliverables this review does **not** assess or execute (29's discipline).

## 1. Baseline facts I established (re-executed, not quoted)

| # | Measurement | Observed |
|---|---|---|
| B1 | six malformed controls vs **baseline bytes** of the craft checker (`git show 1ccb2b7:…` to /tmp) | all six: `exit=1`, `Traceback` present; distinct classes — no-arg `IndexError`; missing file `FileNotFoundError`; malformed JSON `JSONDecodeError`; non-UTF-8 `UnicodeDecodeError`; root list `AttributeError: 'list' object has no attribute 'get'`; `--report` without value `IndexError` → claim O's "before" is accurate at baseline |
| B2 | craft selftest, working tree (in-flight) | `SELFTEST OK 10/10 tamper cases detected` + `CLI-SELFTEST OK 11/11 cases passed`, exit 0 — the 10-mutation before-state is preserved, plus unreviewed new CLI cases |
| B3 | presence checks | `tools/check-gate-battery.py` exists (untracked, in-flight); `reports/round-5/run-validation.py` **absent**; `reports/round-5/parent-source-spotchecks.json` **absent**; `corpus/lessons/round-5-sources/` **absent** |
| B4 | both round-3 replays, in-flight tree | `REPLAY OK: 7/7 rows reproduced` exit 0 for `frozen/round-3/MANIFEST.tsv` **and** `attempt-1/MANIFEST.tsv`; provenance rows print `bytes=match` (the replay reconstructs the recorded invocation convention) — the current green side of O's replay regression |
| B5 | unresolved-row census over `corpus/lessons/supplement-opencode-1/sources/{ottoman,slavs,sogdian,tibet,turkic,mesoamerica,color,kinship,orality,phonetics,registers}.json` | **exactly 20** unresolved rows (ottoman 1, slavs 2, sogdian 1, tibet 2, turkic 2, mesoamerica 4, color 2, kinship 2, orality 1, phonetics 1, registers 2) → claim F's "before" is accurate; the 20 IDs are enumerated in §3 |
| B6 | craft `--counts` on `examples/supplement-opencode-1/sound-change-vs-taboo.json` | exit 0 |

## 2. Causal separation of claims F and O

1. **Distinct axes.** F = freshness (the lane's historically lowest axis, as the contract requires);
   O = operability. Structurally conformant: one claim per axis, each with its own falsifiable
   before→after, and the befores are measured on disjoint artifacts (B1 tool behavior vs B5 ledger census).
2. **Disjoint write surfaces.** F owns `corpus/lessons/round-5-sources/NN.json` +
   `reports/round-5/{parent-source-spotchecks,validation}.json`; O owns `tools/check-gate-battery.py`
   and the CLI hardening of `tools/check-craft-exercise.py` (a tools file, not in O's protected list:
   `tools/gates/*.py`, frozen bytes, exercise, D2 packet). No file is claimed by both.
3. **Failure independence.** F's failure mode (blocked retrieval → row stays `unresolved`) and O's
   (CLI/battery defects) have no causal path between them; neither after_required references the
   other's artifacts.
4. **Cross-harm paths checked, closed if boundaries hold.**
   - O's battery must run the seven gate selftests **in a copied tree**: five of seven gates rewrite
     their committed fixtures in place with truncating `open(...,"w")` (29 F1, line-cited). A live-tree
     run would violate O's own no-harm (original gate/fixture bytes unchanged) — detectable via
     `git status --porcelain tools/gates/` and fixture digests after a run (regression R1).
   - F's parent-only corpus errata cannot invalidate O's replays: replay-frozen grades committed
     **snapshots**, and B4 shows byte-exact reproduction including both provenance rows. Errata must
     stay out of `tools/gates/frozen/` entirely; then no F write reaches any O input.
   - **The one shared seam:** `python3 reports/round-5/run-validation.py` appears both as F's only
     counting command and as the last of O's counting commands, and the file does not exist yet (B3).
     The validator must be **per-claim**: it must report F and O independently so that measuring O
     does not causally require F's ledgers, and vice versa. An all-or-nothing exit would couple the
     two claims' verification through shared bookkeeping. This is a harness requirement, not a target
     change.
5. **Bookkeeping shape (connector note).** A lane report lands last and must cite the commit hash of
   the child-repo work; nothing is committed yet (B0 header). The parent owns the commit, then
   `reports/round-5/kotodama.md`, then report+push. Worker reviews (including this file) are
   author-side evidence, never the admission.

## 3. Claim F (freshness) — falsifiability requirements and the 20-row coupling trace

Declared: ≥10 distinct original unresolved rows rechecked; ≥3 newly retrieved directly relevant
passages with locator + short excerpt; parent independently re-fetches ≥3 before admission; scope
preserved; failed retrieval ≠ confirmation. Evidence on top of that (guards, not substitutes):

- **F1 distinctness.** "Distinct" = distinct `(previous_ledger, previous_id)` pairs against the 20
  originals below; two workers rechecking one row count once. The validator should flag any
  `previous_id` not matching the original ledger IDs exactly (ID drift = invention).
- **F2 pinned entry hashes.** `entry_sha256_before` must hash the **baseline-revision** bytes
  (`git show 1ccb2b7:<entry>`), not the working tree, so rows stay mutually consistent if the parent
  appends errata mid-batch.
- **F3 "newly retrieved".** A passage quoted from a source the original row **already retrieved**
  must not count. Three rows are retrieved-full-text-yet-unresolved precisely because a *different
  named target* was not reached: ORALITY-05 (Lord djvu in hand; Harvard print + Parry catalogue not),
  SR-REG-04 (ANU text in hand; NIKL count not), SR-REG-07 (Haviland PDF in hand; Dixon 1971/1980 not).
  Spot-check should compare `source_url` against the original row's.
- **F4 verdict consistency.** `supported`/`contradicted` require `retrieved_passage: true` + non-empty
  `source_excerpt` ≤40 words; failed retrieval stays `unresolved`; landing/record pages, DOIs and
  catalogue metadata are locators, not content confirmation (the original rows already model this —
  e.g. OTT-06's "snippets deliberately not treated as confirmation").
- **F5 partial vs whole-claim.** Preserve the original claim scope verbatim. Example: OTT-06 can only
  resolve against Quataert's own note 45; a secondary restating the disagreement is partial support and
  the row stays unresolved as a whole claim. Same shape for TURK-06 (needs an *ancient witness* for the
  name Asena) and meso-15 (one 1782 notation does not date every compilation component).
- **F6 parent spot-check visibility.** `parent-source-spotchecks.json` should record which original
  rows the ≥3 re-fetched passages belong to and their URLs, so concentration (all three on one row)
  is visible even though the claim text does not require spread.

The 20 original rows, with the language/myth/era/dress coupling each recheck must carry in
`coupling_implication`:

| original id (ledger) | systems | coupling implication | resolution would move |
|---|---|---|---|
| OTT-06 (ottoman) | era+dress | conflicting decree dates 1725/1726/1727 bound era stratification of women's dress regulation; a single-year pin would be over-precision | era label of Ottoman dress-law rules |
| S09-07 (slavs) | language+myth+dress | unidentified lexeme `nožnici` must not silently become the Rod/rožanicy deity or a garment; the costume row "scissors initiate a kinship rite" hangs on it; retrieved cognates (nožnice/ножницы) support a *scissors* reading only | myth attribution + costume-rite row stay unattributed — the densest triple-coupling row |
| S09-08 (slavs) | myth | Ivanits 1989 (Rod/rožanicy folklore synthesis) unreached (IA 401); entry's myth statements unrechecked downstream | source base of the myth discussion |
| SOG-29 (sogdian) | myth+language | pantheon identity (Nana/Nanai, Wēšparkar): image, attributes, spelling, etymology open; iconographic borrowing ≠ theological equivalence | pantheon rows stay to-verify |
| TIB-A12 (tibet) | era+myth | Golden Urn per-succession use open against case evidence (Oidtmann 2018); the 2011 institutional statement is partisan | era marker for the succession ritual |
| TIB-A16 (tibet) | myth+era | Third Karmapa Rangjung Dorje (1284–1339) as institutionalization of the multi-life narrative; publisher-blocked | recognition-history dating |
| TURK-06 (turkic) | language+myth | Ashina = dynastic/clan designation; she-wolf "Asena" stays a modern retelling until an ancient witness for the personal name is produced; the mythic name must not retroject onto the clan name | naming discipline for the wolf-myth figure |
| TURK-07 (turkic) | language | Clauson's *kut* semantic range (favor→fortune→happiness; soul/life-force in some languages) known only via a bibliography citation | lexicon/naming semantics |
| meso-13 (mesoamerica) | era+dress | codex support dates 991–1147 (ABA) vs 1159–1261 (Soxhlet+ABA) are treatment-dependent, not painting dates; depicted-costume era placement shifts with them | era placement of codex costume depictions |
| meso-14 | era+dress | Madrid codex "Late Postclassic, probably second half of the 15th c." is a study estimate, not a colophon | era label of depicted costume |
| meso-15 | era+myth | Chumayel compilation 1775–1800 vs one 1782 signed notation; the notation does not date every component of the myth compilation | era marker of the myth compilation |
| meso-16 | era+dress | Bonampak dedication 791 CE anchors the garment-ensemble minimum-evidence rule (depicted scene + material evidence) — the direct era↔dress rule input | the minimum-evidence rule's date anchor |
| COL-06 (color) | language | statutory 青 wording (青色の灯火) behind ao-shingō; blue/green lexical-category boundary case; extraction truncated at Article 1 | color-term lexical claim |
| COL-07 | language+era | 四十八茶百鼠 is figurative ("many", not a count) and a later label of the traditional-colour literature, not a located Edo document | nomenclature dating discipline |
| KIN-A07 (kinship) | language | kin terms as linguistic/psychological categories (Kroeber 1909, Lowie 1917); Murdock's correlations moderate, not deterministic | kinship-theory framing |
| KIN-A08 | language | "Saisiyat took ~68 kin terms from Hakka"; DOI 404 including a same-prefix control DOI — infrastructure failure, not verdict evidence | borrowing-count claim |
| ORALITY-05 (orality) | language | 12,323-line single performance of the *Meho* (Lord's own count); later print + Parry catalogue unreached | performance-scale figure |
| PHON-A11 (phonetics) | language | entry cites Blasi et al. 2019 twice with disagreeing venues (Science 366 vs 363:eaav3218) — a bibliographic conflict inside one entry's sources block | parent-only errata candidate |
| SR-REG-04 (registers) | language | Korean sentence-final speech levels "seven classical, four to six alive" — both numbers open; NIKL's own count unchecked | register-count claim |
| SR-REG-07 | language | jalnguy as "a complete replacement lexicon" via Haviland attributing Dixon (1971); Dyirbal primaries unreached; an avoidance register couples lexicon to kin relations | replacement-register claim |

Tally: era-touching 8; myth 7; dress 5 (OTT-06, S09-07, meso-13/14/16); language 12; **11 of 20 are
multi-system** (≥2 of the four). Densest coupling rows for the batch's ≥1 coupling-audit requirement:
**S09-07** (language↔myth↔dress) and **meso-16** (era↔dress rule). Naming candidates is connector
evidence; choosing rows stays with the SOURCE workers and the parent.

Feasibility (route classes read off the original rows' own `access_limit` texts — not new fetches, no
verdict implied): plausible open routes — meso-13 (Radiocarbon/Cambridge is an OA venue; the 429 was a
rate limit → retry), ORALITY-05 (Parry Collection finding aid / archive.org copies of the Harvard
print), SR-REG-07 (Dixon 1972/1980 scans), SR-REG-04 (NIKL official pages), PHON-A11 (Europe
PMC/Crossref-class alternatives to the 403'd routes), COL-06 (e-Gov current-domain law API with the
correct current identifier, or the official PDF). Likely to stay `unresolved` on access: TIB-A16,
KIN-A08, COL-07 (bot wall; no-workaround policy), SOG-29, S09-08, TURK-07, OTT-06, TIB-A12, KIN-A07
(retry possible), meso-14/15/16 publisher blocks unless an open mirror resolves.

## 4. Claim O (operability) — falsifiability requirements

Declared before is confirmed at baseline bytes (B1: six distinct exceptions, exit 1, traceback each).
Evidence requirements on top of the declared targets:

- **O1 six controls.** Each must exit **2** with a stable diagnostic ID and zero traceback; run each
  control twice and diff — stability means identical diagnostics across runs (a bare message that
  embeds a changing path is acceptable only if the ID token is stable).
- **O2 trichotomy preserved.** exit 0 clean / exit 1 genuine findings / exit 2 CLI-IO must stay
  distinct; a hardening (or wrapper) that maps findings onto 2, or CLI errors onto 1, fails
  "preserve genuine finding exit1".
- **O3 five preserved behaviors, each with an exact command:** genuine-finding exit 1 (checker against
  a genuinely flawed *copy* of the exercise, not the shipped bytes); real positive example
  (`sound-change-vs-taboo.json` exits 0); `--counts` (exit 0, same count keys); optional `--report`
  read (accepted, headings enforced); ten mutation detections (`--selftest` reports 10/10 with the ten
  stable IDs — a refactor that drops one tamper case is caught by the count).
- **O4 battery isolation is observable, not asserted:** (i) output names all seven gates; (ii) after a
  full battery run, `git status --porcelain tools/gates/` is empty and fixture digests are unchanged —
  non-vacuous because five gates DO rewrite fixtures when run live (29 F1); (iii) a negative control
  tampers a fixture/input **inside the battery's copy** and the battery reports a stable-ID failure;
  nothing is tampered in the live tree.
- **O5 stable-ID controls.** Positive and negative control outputs must carry greppable ID tokens, not
  bare exit codes.
- **O6 replay regression.** Both manifests reproduce 7/7 before and after the change (B4 is the
  current green side, byte-exact including provenance via the invocation convention).
- **O7 no-harm byte pins.** `tools/gates/*.py`, `tools/gates/frozen/**`, the exercise JSON and the D2
  packet digests unchanged. The wrapper must not edit the gates (e.g. no sed of `open(...,"w")` into
  read-only) — "a safe wrapper does not make the five legacy selftests themselves read-only"; the byte
  pins enforce exactly that.
- **O8 scope boundary vs review 26.** Claim O covers craft-CLI robustness only. The five packet gates'
  parser divergences (unterminated flow silently closed D1; duplicate-key last-wins D2; anchor/tag
  guessing D3; boolean re-rendering D4; tab-indent quadrifurcation D5; RecursionError/traceback D6-D7;
  ReDoS D8) are NOT round-5 targets — `tools/gates/*.py` is frozen by no-harm — and must not be
  reported as fixed by round 5; conversely the six craft controls must not be described as closing the
  review-26 register. SCORECARD's "add isolated negative controls" line stays open.
- **O9 prerequisite.** `reports/round-5/run-validation.py` does not exist (B3) yet is the final O
  counting command and F's only one. Parent-owned; must be landed and **deterministic** (two
  consecutive runs over the unchanged tree → identical output) and per-claim (§2.4c) before admission
  measurement.

## 5. Typed-adapter debts (named, not landed; none redefined as a round-5 target)

From SCORECARD Planned + reviews 22 and 29:

- **T1 native/translation form typing.** Ten PHON-INVENTORY findings grade English garment labels
  against D2 phonotactics; the gate reads only `garment` (no `native_form`/`form_kind`) — prototype
  wrapper with 7/7 controls in scratch 22; landing points `naming-collision-gate.py:614-618` and the
  assembler projection. **Not landable in round 5** (no-harm freezes `tools/gates/*.py`): it must
  remain a stated debt, not absorbed into claim O.
- **T2 executable rank-rule adapter.** Rank rules exist in prose only (SCORECARD Planned).
- **T3 scoped era/material reconciliation.** Costume-era G-ERA findings couple era↔dress/material/rank;
  era tags E0–E3 are additionally indexed as *name forms* (6 NAME-NEAR — second representation class,
  22 §3).
- **T4 assembler projection drops typing.** `assemble-d2.py:113` requires only
  (id, garment, material, wearer_rank, rite, era) from costumes; any future adapter must include the
  projection or the packet loses the typing even if components carry it.
- **T5 parser fidelity adjacent debt.** Naive `_scalar` quoting, no differential test against a
  conforming YAML parser (29 F5) — boundary honesty for any future T1 landing.
- Report-language guard: "a green partial schema check is not whole-culture verification" (SCORECARD);
  none of T1–T5 may be cited as round-5 landed work.

## 6. Regression-check register (ranked)

| # | Regression | Check |
|---|---|---|
| R1 | fixture rewrite by writer gates (29 F1) | post-battery `git status --porcelain tools/gates/` empty; fixture digests unchanged |
| R2 | gate bytes vs round-3 manifest pins | sha256 of all `tools/gates/*.py` unchanged; any change is `gate_revised` (exit 2), reported not smoothed (30 §4#4) |
| R3 | frozen bytes | `tools/gates/frozen/` clean; both replays 7/7 before/after any tool change |
| R4 | craft behavior set | O3's five commands stay green; ten-mutation count stays 10/10 |
| R5 | historical ledger immutability (F no-harm) | `corpus/lessons/supplement-opencode-1/sources/*.json` byte-identical; `previous_id` strings match originals verbatim |
| R6 | marker hygiene | worker writes add no `to-verify` markers to `corpus/knowledge/` (parent errata excepted; any delta reported with unit + command) |
| R7 | D2/exercise/packet digests | unchanged (O no-harm); `assemble-d2.py --check` stays green |
| R8 | validator determinism | `run-validation.py` output identical across two runs; per-claim separation per §2.4 |

## 7. Limits of this review

- Read-only except this file: no code, corpus, LOG, SCORECARD, gate, or frozen artifact touched; no
  provider/config/credential reads; no delegation; no commits; scratch limited to two /tmp files,
  deleted.
- I judged only baseline bytes (via `git show`) and existence/absence of in-flight files. The untracked
  battery and the hardened checker were **not** reviewed or executed beyond the incidental B2/B4
  measurements taken before their in-flight status was established; their owners carry that evidence.
- I produced no round-5 audit rows and no new source retrievals; the §3 feasibility table is route
  classes from the original rows' own access-limit texts, not new fetches.
- No admission recommendation and no axis verdicts: the parent judges all six axes; nothing here marks
  SHONEN, promotes a rank, redefines a declared target, or makes canon decisions.
