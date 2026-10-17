# 16 CRITIC — round 7 acceptance/adversarial boundary review (first pass)

- Author-side critic evidence only. No promotion verification, no judge or
  merge authority, no source re-fetches performed. Parent measures and decides.
- State reviewed as of `2026-10-17T15:58:44-03:00`, child HEAD `30caac6`
  (= declared baseline `30caac66a2a382f1c46ba31f0c3c93da62d0762c`), worktree
  uncommitted. Same-identity resume may re-inspect the parent runner,
  `run-validation.py` and delivered artifacts after they land.
- Attacked: the F and O claims as declared in `reports/round-7/claims.json`,
  the D3 contract/data coupling, fabricated completeness, self-fulfilling
  expected values, translated-label false failures, source scope laundering,
  missing negatives, fake clearance, history rewrites, per-axis harm.

## 1. Contract data integrity — checks actually run, all PASS

| check | command (cwd = child root) | result |
|---|---|---|
| C1 baseline hashes live | `sha256sum corpus/lessons/round-6-sources/{05,03,13,09}.json reports/round-6/parent-reconciliation.json corpus/knowledge/synthesis/worldbible-integration-contract.md` | all six equal `reports/round-7/baseline.json` `reference_sha256` byte-for-byte |
| C2 source bindings vs effective reconciliation | compare `d3-contract.json` `source_bindings` + `targets.json` kinds/URLs against `reports/round-6/parent-reconciliation.json` rows | S01=R6-05-A partial/secondary-scholarly/UT hitol-20; S02=R6-03-B scoped/museum-object/Louvre; S03=R6-13-A scoped/primary/pinned capture `20231003011254`; S04=R6-13-B scoped/primary/wisdomlib doc63185; S05=R6-09-A partial/secondary-scholarly/ARTA HTTP PDF. **No scope laundering baked into the contract.** |
| C3 append-only bookkeeping | `git diff --numstat LOG.md SCORECARD.md` | LOG 65 added / 0 deleted; SCORECARD 15 added / 0 deleted — pure appends, no history rewrite |
| C4 protected-tree freeze | `git status --short` | only `M LOG.md`, `M SCORECARD.md` (allowed), untracked new round-7 paths; zero modifications under `corpus/knowledge`, `corpus/lessons/round-6-sources`, `examples/culture-d2`, old `tools/*.py`, `tools/gates` |
| C5 dispatch template conformance | `head -9 reports/round-7/prompt-template.txt` vs `~/.agents/skills/godspeed/directive.md` | single diff hunk `1d0` (the `/skill:godspeed` invocation line); remaining bytes verbatim |
| C6 SCORECARD premise of claim F | read `SCORECARD.md` round-7 section | freshness recorded as "historically the lowest non-retired axis"; no calibrated scalar invented; "no result claimed yet" correctly stated at declaration |

## 2. Landed artifacts reviewed (state at timestamp above)

### 2.1 `examples/culture-d3/components/04-language.json` — PASS on inspection

Exactly the five assigned keys. Anchors exact: L01 `pina`, L02 `suma`, L03
`talu`, L17 `nara`, L18 `salu`, L19 `mila`, L20 `kuru`. Lexicon exactly
L01–L20; four initial-p lexemes (L01/L04/L05/L06) all SC1-shift p→f in E1
(`fina/falu/fira/fuka`); ≥3 unchanged (all others). Phonology includes p and
f (union stage), `(C)V(C)`, coda subset respected by every form (`masin`,
`kalti`). Names N01–N06: I recomputed every concat from **E1** base forms —
`sumatalu`, `kilanisu`, `falulura` (L04 uses changed `falu`, correct E1
computation), `rumafira` (L05→`fira`), `amikuru`, `fukasina` — each equals
its declared `expected`; pairwise distinct; none equals a base lexeme;
display labels are English explanatory strings. Utterances U01–U07: U01
ordinary/market L01 speaks `fina`/writes `pina`; U02 ritual/hall applies the
fixed AV1 substitution to L02's E0 `suma`, written `pina`; U03/U04 (L03) have
no trigger; U05 ordinary L04 `falu/palu`; U06 ritual L02 `suma/suma`; **U07
ordinary at hall speaks `fina`** — proving no generalized taboo outside
ritual/hall. All native spellings ASCII lowercase. No real-language or
novelty claims present.

### 2.2 `examples/culture-d3/components/05-ritual.json` — PASS on inspection

Exactly the four assigned keys. AV1 exact fixed shape (L01→L02, E1, ritual,
hall, `constructed-rule`). B01/B02: attributed in-world speakers, directly
opposing propositions about the record-vs-voice institution, both
`truth_status: unresolved`, no narrator certification. NR1 exact:
`allowed_offsets [2,8,20]` (unique integers), `chosen_offset 8`, unit
`fictional-nights`, `constructed-not-historical`, source S03 — and nothing
attributes these numbers to Gobhila. SY01/SY02: nonempty era/audience-scoped
readings, explicit "no universal meaning" clauses, no colour key.

### 2.3 `examples/culture-d3/components/07-evidence.json` — PASS on inspection

Exactly the six assigned keys. All five `file_sha256` values equal the live
ledger bytes (verified, not copied). support_scope/kind/URL per reference
match the effective reconciliation rows (S01/S05 stay `partial-support`).
Bridge target sets exactly BR01→U01/U02, BR02→C01/C02, BR03→NR1,
BR04→O01/O04, BR05→SY01/B01; all `design-only` + `constructed-rule`.
`canon_status NON-CANON`, `handoff_status prepared-not-accepted`, screening
`unresolved`/`false` with nonempty limits, five scope_notes covering invented
genealogy, permission limit, no lore receipt, unswept names, open residuals.
Spot-traced factual content back to round-6 ledgers: BR01 IṢ-BAT/ēpta = R6-05-A
basis; BR03 ten/100/one-year = R6-13-A; BR04 §18 horn tied to garment end and
§§1–9 ground skins = R6-13-B locator; BR05 15,000–18,000 documents and the
"isolate … may not demonstrate general use" wording = R6-09-A locator/excerpt.
**No invented statistics found in any bridge mechanism.**

### 2.4 Source ledgers `10.json` (R7-F03), `11.json` (R7-F04), `12.json` (R7-F05) — PASS on inspection

Mechanical, run at 15:58: per-ledger `id/question/entry/previous_id/
source_url/source_kind` byte-equal to `targets.json` (`fixed-fields-exact:
True` ×3); all 17 schema fields present; whitespace-split excerpt lengths
27/35/36 (≤40); `result` ∈ allowed set (`scoped-support`, `scoped-support`,
`partial-support`); `accessed_at` 2026-10-17. Anti-copy discrimination: each
main `source_excerpt` differs from its round-6 counterpart's recorded excerpt
(F03 quotes §8 timings, not §14; F04 quotes §28 binding, not §1 spread; F05
quotes the page-9 paragraph). F05 is the hard case — its excerpt is
string-identical to round-6's — and it discharges the doubt with a live
receipt I verified: scratch PDF exists, 1,242,395 bytes,
`sha256sum …/round7-12-source-scribe/arta2007-001.pdf` =
`c7664821696a92d968b8000bdd9ae0b61020680023f3eb29e7bb7d59f79a59f8`, matching
the ledger's claim and the parent's round-6 hash; pdftotext page-9 slice and
full-text line numbers named; HTTP scheme preserved; result stays
`partial-support` (no upgrade laundering). Boundary discipline preserved:
F03 refuses Sanskrit conversion and pins "10/100/one year, other numbers are
analogy"; F04 keeps skin≠horn, reversible colours, footnote-mediated Kāṇva,
flags the kṛṣṇājina identification as prior scholarship, self-reports a
missing footnote [18] extraction artifact, and re-opens the Kāṇva residual
instead of closing it.

### 2.5 `examples/culture-d3/controls.json` — PASS with two flags (see §4 A7, A8)

Structure conforms: 3 positive / 16 domain / 4 malformed controls. All 14
domain diagnostics covered (contract asked ≥12, "prefer one per diagnostic" —
achieved 14/14, with TIMING doubled to include the required bool rejection).
Positive controls prove exactly the false-failure freedoms: translated
costume label replaced (stays clean), ordinary utterance place changed off
market (stays clean), belief proposition reworded (stays clean). The
DERIVATION control sets `native_form` **and** `expected` to `funalu` —
internally consistent, so it can only be caught by genuine recomputation of
concat(L02.suma, L03.talu)=`sumatalu`; it traps a checker that merely
compares the two declared fields. The RANK control flips C03 to `lawful`
(fake clearance), the ERA control sends C03 to E0 where M02 has no route,
the OBJECT control wears the ground surface, MYTH sets `world-fact`,
SYMBOL empties audience, BRIDGE asserts historical reconstruction, SCOPE
overstates S01. JSON-pointer list indices verified correct against the
component layouts.

## 3. Explicitly UNREVIEWED — absent at 2026-10-17T15:58:44-03:00

(Superseded in part by the same-turn delta in §8: 08.json, 09.json,
06-material.json, handoff.md, README.md and worker reports 01/15 landed
~16:03 and are reviewed there. The two tools, packet, packet.gates.yml,
expected.json and run-validation.py were still absent at 16:03 and remain
unreviewed.)

No green, no prediction, no assumed pass for any of these:

- `corpus/lessons/round-7-sources/08.json` (R7-F01, UT Hittite) — no ledger,
  no scratch dir observed; worker output not yet observable.
- `corpus/lessons/round-7-sources/09.json` (R7-F02, Louvre) — absent, but
  scratch `reports/supplement-opencode-1/scratch/round7-09-source-scout/`
  exists → in flight; ledger unreviewed.
- `examples/culture-d3/components/06-material.json` — absent.
- `tools/check-evidence-coupling.py`, `tools/assemble-culture-d3.py` — absent;
  every O-claim runtime property is unverifiable until they land.
- `examples/culture-d3/packet.json`, `packet.gates.yml`, `expected.json`,
  `handoff.md`, `README.md` — absent.
- `reports/round-7/run-validation.py` and any parent re-fetch receipts —
  absent; the F thresholds ≥2 parent re-fetches are unmeasurable.
- Worker reports `01-plan-review.md` … `15-implementation-review.md` — absent.
- SCORECARD round-7 result rows — correctly not yet claimed.

## 4. Attack vectors — caught, missing, or contract gap

- **A1 Source scope laundering** — caught at three layers: contract bindings
  match effective reconciliation (C2); 07-evidence scopes equal the rows and
  the D3-SCOPE control overstates S01; F05 declined to upgrade R6-09-A.
  Residual risk: guard must also catch a *valid-enum* wrong scope (see A7).
- **A2 Copied-excerpt laundering (F)** — F05's string-identical-to-round-6
  excerpt shows string difference cannot be the acceptance test. Binary rule
  below (F-A5) accepts identity **only** with a live-retrieval receipt
  (fresh timestamp + verifiable artifact hash), rejects copy-without-fetch.
- **A3 Fabricated completeness** — claim thresholds (20 lexemes, ≥12
  controls, ≥3 entries…) must be counted from bytes by `run-validation.py`,
  never asserted. No validator exists yet; O-A10 forces a mutation test
  proving the counter is input-derived.
- **A4 Self-fulfilling expected values** — controls were written while the
  checker did not exist (controls landed 15:58; checker still absent), so
  expectations could not be read off the implementation; contract also fixes
  diagnostic IDs in `d3-contract.json`. Enforcement is O-A4 (expectation
  tamper must fail the selftest) — not yet runnable.
- **A5 Fake clearance** — screening resolution has **no dedicated
  diagnostic** in `d3-contract.json` and **no control** in controls.json. A
  packet with `screening.status:'resolved'` / `real_language_sweep_performed:
  true` may currently exit 0. This is the round's one live missing-negative
  gap (contract-level, not worker-13's fault). Parent fix without weakening:
  map the flip to `D3-SCOPE` (or `D3-CANON`) exit 1 and add one control.
- **A6 Translated-label false failures** — guarded by the positive label
  control + `d3-contract.json` "translated labels never tested" diagnostics
  rule + my read of 04-language (labels are English strings separate from
  every native form). O-A7 makes it executable once the guard exists.
- **A7 D3-SCOPE control enum ambiguity (false-failure risk)** — control
  `domain-D3-SCOPE-reference-scope-overstates-reconciliation` sets
  `support_scope:'full-support'`, which is not a declared schema value. A
  checker that enum-validates first would exit 2 `D3-DATA`, failing the
  control's expected exit 1. Fix on the control side (no diagnostic
  weakened): use a valid but overstating value, `scoped-support` (S01's row
  is `partial-support`). Selftest will expose this either way; reconcile
  before measuring O.
- **A8 Optional CANON half** — D3-CANON also covers "handoff claiming
  acceptance", but no control flips `handoff_status`. Threshold already met
  (≥12); recommended second control: `handoff_status:'accepted'` →
  `D3-CANON`. Same for flipping S03 `source_url` to an unpinned snapshot
  (the exact R6-13-A raw-worker error class) → `D3-SCOPE`.
- **A9 History rewrites** — none observed (C3/C4). Keep H-A2/H-A3 as the
  round-end gate; LOG/SCORECARD must stay delete-free through final commit.
- **A10 Per-axis harm** — depth/coverage untouched so far (no
  `corpus/knowledge` diffs); adjacency's D2 twenty findings and round-6
  residuals are explicitly preserved by 07-evidence scope_notes and F04's
  reopened residual. H-A4 reruns round-6 acceptance in isolation at close.
- **A11 Word-cap counting ambiguity (nit)** — ledger 11 self-counts its
  excerpt at 34 words; whitespace `split()` gives 35 (the bare ellipsis
  token). Compliant either way, but `run-validation.py` should declare its
  counting method (recommend whitespace split) to avoid disputes. Same for
  11's `additional_excerpts` (footnote quotes >40 words): the cap is a
  `source_excerpt` field rule; validators must count **only** that field so
  extra apparatus never inflates passage counts (round-6
  no-optional-field-shape-inflation rule).
- **A12 Names-distinctness softness (nit)** — contract says "mutually
  distinct beyond trivial near similarities", which is not binary. Concrete
  rule the guard should implement: pairwise string inequality AND ≥2
  differing character positions AND no name equals any lexeme form or its
  concat alias. N01–N06 pass trivially today.

## 5. Binary acceptance checks for the parent (each PASS/FAIL, no judgment calls)

Freshness claim F:

- **F-A1 exactly five fixed audits** — `ls corpus/lessons/round-7-sources/`
  == `{08,09,10,11,12}.json` and nothing else; each file one JSON object
  whose `assignment`-style fixed ids are exactly R7-F01…R7-F05. Any sixth
  file or missing id → FAIL.
- **F-A2 schema + fixed fields** — for each ledger: all 17 required fields
  present; `id/question/entry/previous_id/source_url/source_kind` byte-equal
  to its `targets.json` target; `result` ∈ {scoped-support,
  partial-support, contradicted, unresolved}. (Command pattern already
  proven on 10/11/12; rerun over all five.)
- **F-A3 excerpt cap** — `len(l['source_excerpt'].split()) <= 40` for every
  ledger, with the counting method stated in `run-validation.py` output.
- **F-A4 bibliographic exclusion** — each counted passage has
  `retrieved_passage==true` AND `directly_relevant_nonbibliographic==true`;
  for R7-F02 specifically the excerpt/locator must contain object
  material/technique/dating field text (e.g. linen/weave/pleat/dynasty
  strings), not bibliography or accession-only identity.
- **F-A5 fresh fetch, not copy** — per ledger PASS iff `accessed_at` ≥
  2026-10-17 AND (main excerpt differs from the round-6 counterpart's
  recorded excerpt OR a live receipt verifies: for F05,
  `sha256sum reports/supplement-opencode-1/scratch/round7-12-source-scribe/arta2007-001.pdf`
  equals the ledger's claimed hash). Copy without receipt → FAIL; identity
  with receipt → PASS (prevents both laundering and false failure).
- **F-A6 entry spread** — distinct `entry` values over ledgers passing F-A4
  ≥ 3. **State now: 2 of 3 (india-vedic, persia-achaemenid) — FAILS until
  08 or 09 lands retrieved.** Do not admit F on today's counts.
- **F-A7 parent re-fetches** — parent receipt artifact names ≥2 distinct
  reference_ids with dated receipts. Absent → unmeasured.
- **F-A8 no residual closure** — no round-7 ledger or parent artifact
  declares the fifteen round-5 residuals or round-6 unresolved rows closed;
  grep for closure language must come up empty (F04's ledger re-opens one —
  correct direction).

Operability claim O (all require the absent tools; until then O is
unmeasured, not failing):

- **O-A1 positive** — `python3 tools/check-evidence-coupling.py
  examples/culture-d3/packet.json` → exit 0, stdout JSON `findings:[]`.
- **O-A2 negatives** — `--selftest` → exit 0, `selftest_passed:true`,
  `domain_controls ≥ 12`, `malformed_controls ≥ 4`, every control's actual
  exit and emitted id equal to its expectation (16 domain controls currently
  specified; zero mismatches tolerated).
- **O-A3 malformed hygiene** — all four malformed controls exit 2 with
  stderr containing no `Traceback`.
- **O-A4 anti-self-fulfillment** — in an isolated copy, swap one control's
  `expected_ids` (e.g. RANK→ERA) → `--selftest` must FAIL
  (`selftest_passed:false`). If it still passes, expectations are decorative
  → FAIL. Additionally, a plain packet run must not read `controls.json`/
  `expected.json` (rename them away in isolation → O-A1 result unchanged).
- **O-A5 frozen tamper** — append one byte to a copy of packet.json, run
  `--frozen` → exit 2 with `D3-SNAPSHOT`, no traceback; restore → exit 0.
- **O-A6 no input writes** — sha256 of packet.json and controls.json before
  vs after every guard invocation → identical.
- **O-A7 label freedom** — positive control A1 (translated label) stays
  exit 0; the same glyph mutation applied to a `native_form` exits 1
  `D3-NATIVE`. Both directions must hold.
- **O-A8 assembler determinism** — two runs produce byte-identical
  packet.json (equal sha256); `--check` 0/1/2 on equal/mutated/missing
  component; generated packet contains no timestamp or absolute path
  (grep `20\d\d-|/home/` → empty).
- **O-A9 declared violation retained** — positive packet keeps C03 as
  declared violation AND exits 0; the RANK control (C03 flipped lawful)
  exits 1 `D3-RANK`; legacy projection keeps costume R-01 exit 1, naming
  CROSS-HOLD exit 1, handoff structurally passing, not canonized. Any path
  that turns C03 "clean" → FAIL (that is the C03 history-rewrite vector).
- **O-A10 counter is input-derived** — in an isolated copy delete one
  lexeme from a component, re-assemble, rerun `run-validation.py` → the
  lexeme count reads 19 and validation reports failure. A validator whose
  counts never move → fabricated completeness → FAIL.
- **O-A11 screening/clearance gate (after A5 fix)** — packet with
  `screening.status:'resolved'` or `real_language_sweep_performed:true` →
  exit 1 (parent-chosen diagnostic, recorded before measurement). If no
  such control/diagnostic exists, O's "no fake clearance" property is
  unenforced → flag, not silently pass.
- **O-A12 separability** — in an isolated export with
  `corpus/lessons/round-7-sources/` removed, all O commands still behave
  identically (O uses committed round-6 evidence only).

Per-axis harm gate (round end):

- **H-A1 protected freeze** — `git diff 30caac6 -- corpus/knowledge
  corpus/lessons/round-6-sources examples/culture-d2
  examples/handoff-packet.sample.md examples/handoff-packet.sample.yml
  tools/assemble-d2.py tools/check-craft-exercise.py
  tools/check-gate-battery.py tools/replay-frozen.py
  tools/source-audit-inventory.py tools/gates reports/round-5
  reports/round-6` → empty output.
- **H-A2 append-only** — `git diff 30caac6 --numstat LOG.md SCORECARD.md`
  → deleted column 0 for both, at final commit too.
- **H-A3 D2 preservation** — round-6 acceptance rerun on delivered old
  surfaces in an isolated copy: craft 10/10 domain + 18/18 CLI, battery
  10/10, both round-3 manifests 7/7, D2 twenty findings intact, recorded in
  `reports/round-7/validation.json` regression section.
- **H-A4 reconciliation immutability** — `sha256sum
  reports/round-6/parent-reconciliation.json` still `1b9b1671…` at close
  (verified today; re-verify at round end).

## 6. Honest claim status at review time

- **F**: 3 of 5 ledgers landed, all individually clean; passages ≥3 met
  (3 distinct: Gobhila §8, ŚB §28+footnote 9, ARTA page 9); entries 2 of
  required ≥3; parent re-fetch receipts absent. **F is NOT verifiable
  today** and must not be reported as passing on current counts.
- **O**: all components except 06-material landed look conformant;
  controls exceed thresholds with strong anti-self-fulfillment design;
  the capability itself (guard, assembler, packet, frozen mode, legacy
  holds) is unmeasured — no tool or packet bytes exist yet. One contract
  gap (A5) and one control fix (A7) should be resolved by the parent
  before measurement.
- **No axis harm observed**; harm gates H-A1…H-A4 all green at first pass.

## 7. Limits

Author-side adversarial review of declared claims, contract data and landed
bytes only. I fetched no sources; hash equality of scratch artifacts is
reproduction of recorded claims, not independent web verification. Component
reviews are static inspections against `d3-contract.json`, not executions —
several O-A checks exist precisely because static conformance cannot prove
runtime behavior. Absent artifacts are marked unreviewed, never presumed
green or red. Parent owns measurement, reconciliation of A5/A7, integration,
commit and the round report.

## 8. Same-turn delta addendum (state 16:03–16:10-03:00)

The swarm kept landing while this report was written. Everything below was
inspected before turn end; nothing was predicted.

### 8.1 Newly reviewed — all PASS on inspection

- **`corpus/lessons/round-7-sources/08.json` (R7-F01)** — fixed fields exact
  (mechanical), 20-word excerpt, `accessed_at` 2026-10-17. Content: keeps
  IṢ-BAT/ēpta separation and copy-horizon-vs-cult-provenance as two distinct
  layers, and adds a genuinely new passage (DUTU-us gloss "probably Istānus,
  from the name of the Hattic Sungod Estan") explicitly flagged as not quoted
  in R6-05-A — the strongest anti-copy form: new content, not a re-worded
  old string. Result stays `partial-support` and the limits answer the
  question's negative half verbatim: no Hattic non-IE/genealogy leg is
  supported, "of Hattic origin" is myth/cult provenance not language
  genealogy, "probably" is the authors' conjecture, gloss-layout flattening
  disclosed. No upgrade laundering.
- **`corpus/lessons/round-7-sources/09.json` (R7-F02)** — fixed fields exact,
  35-word excerpt as bracketed field transcriptions (exactly what the fixed
  question demands), bibliography rows explicitly excluded from the passage
  (F-A4 satisfied in content). Live receipt verifiable: parallel curl
  timeout-then-HTTP-200 documented; raw HTML at
  `reports/supplement-opencode-1/scratch/round7-09-source-scout/louvre-e12026.html`
  with field line numbers. Museum caveat preserved, ambiguous carousel span
  disclosed and **not used**. Result stays `scoped-support`.
- **`examples/culture-d3/components/06-material.json`** — exactly the five
  assigned keys. Eras E0/E1 relative-only; M02 `available_from E1` with
  routes `[[E1]]` and **no E0 route** (contract demand); gate names exactly
  felt/plant-cloth/horn; O01 ground-surface `worn:false`, O02/O03/O04 worn
  true; C01–C04 exactly per anchors (L17 nara / L18 salu / L19 mila /
  L20 kuru), costume material_id matches its object, **C03 keeps
  `claimed_status:'violation'`** with import provenance agreeing M02, RR1 in
  exact legacy-gate shape (`prohibit`/plant-cloth/visitor/empty exempt).
  Native costume forms distinct from all N names; labels marked translated.
- **`examples/culture-d3/handoff.md` + `README.md`** — the fabricated-
  completeness attack finds nothing: manifest digests are measured for
  existing bytes only, D3-byte rows say "absent at scribe time — digest to be
  computed at assembly", validation section says NOTHING executed and no
  outcome pre-announced, `prepared-not-accepted` / not canonized throughout,
  no lore receipt, no clearance. Exactly the discipline the contract's
  "no invented hashes or validation outcomes" requires.
- **`reports/round-7/01-plan-review.md`** — read-only planner report whose
  G1 (legacy projection must map gate_name **value** into legacy `name`/
  `material` keys, else C03's expected R-01 red silently becomes green)
  is a true cross-surface false-green vector; it corroborates and sharpens
  my O-A9: reviewer must assert the C03 legacy row is exactly
  `{garment: mila, material: plant-cloth, wearer_rank: visitor, rite:
  assembly, era: E1}`. Its G2 (unowned counting command) matches my F/O
  requirement that `run-validation.py` exist and be input-derived (O-A10).
- **`reports/round-7/15-implementation-review.md`** — independent static
  review reaching the same component verdicts as my §§2.1–2.3 and controls
  census; adds two verified false-failure traps: raw 05.json audit
  `source_kind` is `repository-scholarly` while the effective R6-05-A row is
  `secondary-scholarly`, and raw 13.json R6-13-A `source_url` is a wildcard
  archive URL while the effective row pins `20231003011254`. Landed
  07-evidence.json carries the **effective** values (I verified), so the
  traps bite only if the guard compares packet references against raw
  ledger fields instead of the embedded effective rows.

### 8.2 Updated honest claim status

- **F mechanicals now fully green across all five ledgers**: exactly five
  files 08–12, fixed fields byte-exact, all 17 schema fields, excerpts
  20/35/27/35/36 words, results ∈ allowed set and each equal to its
  effective round-6 disposition, `accessed_at` 2026-10-17, entry spread
  **4 distinct entries ≥ 3**, distinct substantive passages ≥ 3 (new-content
  passages in F01/F03/F04/F05, field transcriptions in F02). **F-A7 (≥2
  dated parent re-fetch receipts) is still unmeasured — no receipt artifact
  or `run-validation.py` exists — so F must still not be admitted yet.**
- **O unchanged**: both tools, packet.json, packet.gates.yml and
  expected.json remain absent at 16:03; every O-A check stays unrun.
  Land-and-resume sequencing per dispatch-plan is correct; do not fabricate
  runtime results.
- **No axis harm**; H-A1/H-A2/H-A4 re-verified green at 16:03 (`git status`
  unchanged in kind: appends + untracked new paths only).

### 8.3 Additional acceptance check raised by the delta

- **O-A13 (guard must judge against effective rows, not raw ledgers)** —
  a packet reference tuple carrying the effective R6-05-A kind
  (`secondary-scholarly`) and the effective pinned R6-13-A URL must PASS;
  the guard implements this by embedding the five effective
  kind/URL/scope rows (from the baseline-committed reconciliation bytes,
  hash-pinned), never by re-reading raw ledger fields. False-failure test:
  correct packet exits 0 despite raw-vs-effective divergence; laundering
  test remains the existing D3-SCOPE control. Recommended companion control
  for worker 13: flip S03 `source_url` to the wildcard
  `https://web.archive.org/web/2023/...` form → expect exit 1 `D3-SCOPE`.
- Worker 01's G1 adds a concrete O-A9 sub-assertion (exact C03 legacy row
  quoted above); worker 15's S05 locator note (page-9 override) is prose-
  level only and correctly does not enter the reference tuple.

## 9. Same-identity continuation — F rederivation, prompt-fidelity
reconstruction, receipt audit (state 2026-10-17 16:26-03:00)

Parent landed `native-request-binding.json`, `dispatch.json`,
`parent-source-spotchecks.json`, `parent-reconciliation.json`,
`integration-attempts.json`. Everything below is independently rederived
from saved bytes; no network calls were made; the in-progress
`run-validation.py` (agent-490) is explicitly **not reviewed** here, and no
admission or promotion verdict is given.

### 9.1 Prompt-fidelity defect — reconstruction confirms exactly one replacement

Reconstruction from `dispatch-plan.json` (`description/items/model/
subagent_type`), `prompt-template.txt` (planned template) and the single
documented `old→new` step-6 replacement in `native-request-binding.json`,
serialized per the binding's rule
(`json.dumps(args, sort_keys=True, separators=(',',':'), ensure_ascii=False)`,
UTF-8, sha256):

- planned  → `4733dffea5b06ee953326d73e35949aa6578695e476f3dee4385b2945b02451c` (reproduced exactly)
- actual   → `9f46d717352a1c8f7f428bbf4c7af48733676b287a6a16253a6e8ffe68e1676f` (reproduced exactly)

The one replacement therefore fully accounts for the planned→actual
difference; the binding's `all_other_arguments_match:true` is consistent
with my reconstruction. Verdict stated carefully: the quoted fleet contract
in the actual dispatch was **not byte-verbatim at step 6** — a real
prompt-fidelity conformance defect, recorded as such (`saved_request_
matches_host_request:false`, `saved_template_matches_actual:false`), with
semantic retention explicitly NOT treated as repair and no retrospective
equality fabricated. This record makes no claim about upstream wire-model
identity or runtime concurrency; it binds an observed host event only.
Corroboration: this worker's own received assignment text carries the
"new" step-6 wording, consistent with the actual template being sent.

### 9.2 F metrics — independently rederived (commands in-file, deterministic)

| metric | rederived value | threshold |
|---|---|---|
| fixed-target bindings exact (id/question/entry/previous_id/source_url/source_kind vs `targets.json`) | 5/5 True | 5 exact |
| ledger files present | exactly `08…12.json` | exactly 5 |
| eligible mains (retrieved ∧ nonbibliographic ∧ kind ∈ mains-allowed ∧ ≤40 tokens) | 5/5 | ≥3 distinct passages |
| distinct eligible main keys (URL + NFKC/casefold/ws-normalized locator + excerpt) | **5** | ≥3 |
| distinct entries | **4** (anatolia-hittite, egypt-ancient, india-vedic, persia-achaemenid) | ≥3 |
| main whitespace tokens F01–F05 | 20 / 35 / 27 / 35 / 36 | ≤40 each |
| parent distinct successful re-fetch URLs (P01 UT, P02 Louvre) | **2** | ≥2 |
| scope labels vs effective R6 dispositions | partial/scoped/scoped/scoped/partial — all equal, zero upgrades | conservative |

Notes: F04's raw excerpt is 35 whitespace tokens; the ledger prose says 34 —
`parent-reconciliation.json` row R7-F04 records exactly this discrepancy and
counts the raw tokens. My earlier nit A11 is thereby already reconciled by
the parent; `run-validation.py` must encode whitespace-split counting
(reconciliation `count_key` excludes `additional_excerpts`, bibliography and
search snippets). Reconciliation `whole_claim_rule` keeps rechecks distinct
from compound resolution; `drift_observation` is bounded (no bytewise
certification); fifteen round-5 and round-6 residuals stay open. With
parent receipts landed, every declared F threshold now has a satisfied
rederived count **pending the acceptance runner** — still no F admission
from this critic.

### 9.3 Receipt audit against the four named failure classes — none found

- **Bibliography/extra-quote counting:** P02 explicitly excludes
  bibliography rows from content; count_key excludes `additional_excerpts`
  (F04's >40-token footnote apparatus cannot inflate the count); pipes in
  P02's excerpt are declared separators, not prose. PASS.
- **Compound-claim promotion:** all five dispositions equal their raw
  worker `result` and the effective R6 rows; P01 keeps copy-horizon and
  cult-provenance separate; R7-F05 states download success ≠ new discovery.
  No partial→scoped or scoped→whole movement anywhere. PASS.
- **Source access fiction:** both parent checks say "Actual parent native
  FetchURL", claim no fabricated wall timestamps, and date from the actual
  turn; worker-side receipts remain independently checkable (F05 scratch
  PDF hash verified by me in §2.4; F02 raw HTML in git-ignored scratch).
  PASS.
- **Broken scope:** spotchecks cover exactly the two fixed URLs of
  assignments 08/09, none beyond the five fixed targets;
  `counting_rule` explicitly disclaims that all five worker retrievals
  were independently repeated. PASS.

### 9.4 Static notes on newly landed D3 artifacts (no runtime verdicts)

- Guard present: `sha256sum tools/check-evidence-coupling.py` =
  `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` —
  matches the parent's quoted current hash. Strict-integer frozen-exit fix
  is in progress (I05); parent final replays pending; I do not review the
  runner or re-run the guard.
- `controls.json` (16:17 revision, sha256 `f00ccf7aac931fb2…`): still
  3 positive / 16 domain / 4 malformed; my A7 is fixed — the invalid
  `full-support` value is gone, replaced by
  `domain-D3-SCOPE-reference-scope-laundered-to-scoped` (valid-enum
  laundering); my A5 is fixed — `domain-D3-SCOPE-screening-sweep-flag-faked`
  now covers fake clearance. Integration-attempts I01/I02 document these as
  independent, implementation-derived corrections with worker-run CLI
  results (selftest 3/16/4/3 passing); runtime confirmation belongs to the
  parent's replay.
- `packet.json` static scan: 0 `/home/` hits, 0 ISO-timestamp hits —
  consistent with the contract's no-timestamp/no-absolute-path rule
  (determinism still requires the assembler run, not this grep).

### 9.5 Open items at close of this continuation

1. `run-validation.py` in progress (agent-490) — unreviewed by instruction;
   must implement O-A10 (input-derived counters) and whitespace-split cap
   counting before any F/O measurement is quoted.
2. `expected.json` not yet created — every `--frozen` acceptance check
   (O-A5) is unrun.
3. I04 assembler fixture-fidelity (coda vs `coda_subset`) in progress —
   real defect, no fixed result claimed.
4. I06 scribe handoff/README intentionally stale (draft rows may differ
   from actual packet) — resume pending; parent acceptance must compare
   content against the packet, per my §3 discipline.
5. I07 round-6 regression must run from a BASE-pinned private export, and
   be reported as old-surface regression only, not round-7 acceptance.
6. Prompt-fidelity conformance defect (§9.1) stays on the defect ledger —
   no redispatch, no retroactive verbatim claim.
7. No admission/promotion/clearance verdict is made or implied anywhere in
   this report.
