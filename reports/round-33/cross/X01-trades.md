- Seat: X01 | critic (cross-claim trade hunter) | claim cross | date 2026-10-19 | baseline 139e3b6

# X01 — cross-claim trade hunt (O × C × A)

Mission: collisions between claims O / C / A (same file proposals, contradictory
instructions), pin drift across claims, and any axis-harm pathway; verdict per
pair.

## 0. Method, independence and limits

- At this seat's reads (2026-10-19, ~03:55Z) **no sibling fragment had landed**:
  `reports/round-33/{op,calib,adj,review,scribe,cross}/` were all empty
  (`ls -la reports/round-33/*/`, output empty). Every verdict below is therefore
  derived from `claims.json` + `targets.json` + the filed artifacts the claims
  name — not from fragment content. Verdicts that depend on K01, K03, O02, C14 or
  X00 are marked **provisional** and owed (see `## Owed`).
- Every command below is read-only. No filed byte was written by this seat; the
  only write is this file.
- Commands run (exact, dated 2026-10-19):

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse HEAD                              # 139e3b662900557afe54f632b468619593dc9fcb
git status --porcelain                          # " M LOG.md", "?? REGIMEN.md", "?? reports/round-33/"
git ls-files | wc -l                            # 2655
python3 -B reports/round-25/audit/c31-lessons-index-audit.py            # exit 1; C31 + C34b FAIL; 2 findings
python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest # SELFTEST OK: 28/28
find corpus/lessons -maxdepth 1 -name '*.md' | wc -l                    # 33
find corpus/lessons -mindepth 2 -type f | wc -l                         # 146
find corpus/lessons -mindepth 1 -maxdepth 1 -type d | wc -l             # 9
sha256sum SKILL.md corpus/lessons/README.md
python3 -B reports/round-30/craft/box1-survey.py  # exit 0; named 28 / resolvable 28; skill sha 79fe91d3…
python3 -c "import json,glob,os; [print(f) for f in sorted(glob.glob('reports/round-*/availability*.json')) if json.load(open(f)).get('state')=='open-at-seat-close' and os.path.exists(os.path.join('reports',f.split('/')[1],'validation.json')) and not os.path.exists(os.path.join('reports',f.split('/')[1],'telemetry','closing-snapshot.json'))]"
```

## 1. Verified greens (checked, no trade found)

| check | evidence | verdict |
|---|---|---|
| No duplicate seat `out` paths (64 seats, 64 distinct outs) | `python3` over `reports/round-33/targets.json` → `duplicate outs: []`; dir histogram calib 18 / adj 17 / op 11 / review 8 / cross 5 / scribe 5 | green |
| Every seat carries a claim token; declared claims are exactly O/C/A on three distinct axes | `reports/round-33/targets.json:12-84`; `reports/round-33/claims.json:16,20,39,52` | green |
| Claim A's declared before-number reproduces: tracked paths = 2655 at baseline | `git ls-files \| wc -l` → 2655 (`claims.json:57`) | green |
| Scope delta at this read is exactly the three entries claim A's threshold allows | `git status --porcelain` → ` M LOG.md`, `?? REGIMEN.md`, `?? reports/round-33/` (`claims.json:63`) | green |
| Claim O's declared before-state reproduces exactly | c31 audit exit 1: `C31_index_rows_eq_files` FAIL, `C34b_prose_arithmetic` FAIL, findings `C31-1` = the 7 files round-26..32, `C34-2` stated [26,26] vs measured [26,33] (`claims.json:25`) | green |
| SKILL.md live bytes still match the r32 box-1 reading sha `79fe91d3…` | `sha256sum SKILL.md` → `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d`; dossier `reports/round-32/dossier-d11-shonen-boxes.md:49-51` | green (pre-edit) |

## 2. Trades and axis-harm pathways

### X01-T1 — C × SCORECARD/LOG: the "12" is not enumerable from the dossier (calibration harm) — **provisional on K03**

- The dossier's own Decision 4 table carries **exactly 9 debt rows**, not 12:
  `reports/round-32/dossier-d13-operator-decisions.md:128-138` (rows: 12 D4
  garment holds; `head2`; RL-3 ceiling; box-1 citation conditions 2-4; cold-run
  N1/N4/N5/N7; lore-owned bilateral read + L0 digest; numeric rubric; devin
  could-not-evaluate; r18 adapter supersession).
- The number 12 exists only in filed prose that names no counting rule:
  `SCORECARD.md:443-445` ("12 standing open items in the dossier") and
  `LOG.md:3512-3514` (same phrase). No filed artifact enumerates the 12 rows.
- At least four defensible arithmetics reach 12 from the same source material:
  (a) split the cold-run row into N1/N4/N5/N7 → 9−1+4 = **12**;
  (b) 9 + the three box-4 standing readings 3a/3b/3c (`dossier-d11-shonen-boxes.md:208`) = **12**;
  (c) split box-1 into conditions 2/3/4 → 9−1+3 = **11** (does *not* reach 12);
  (d) split box-1 (+2) and lore-owned (+1) → **12**.
- Consequence: claim C's after_required — "rows == K03's canonicalized 12
  (cross-checked against SCORECARD's '12')" (`claims.json:46`) — is only a
  cross-check if K03 files the counting rule (its mission does require "record
  how you counted", `targets.json:15`). Without a filed rule, a 12-row ledger is
  a count-match by construction; the "cross-check" is unfalsifiable and a green
  C13 receipt would not mean what it says.
- Required of K03/C13: file the counting rule as an explicit derivation
  (`9 table rows + which splits`) with a falsifier — e.g. a control that shows a
  9-row or 13-row enumeration failing the same rule. Owner: K03 (rule), C13
  (consistency), R05 (adversarial). Axis at risk: calibration.

### X01-T2 — O × its own threshold: C31+C34b green does not imply honest prose (false-green pathway)

- The c31 tool re-derives **only two** prose statements: `Rows: **N**` (queue)
  and `**Rows: N. Files: N.**` (table) — `reports/round-25/audit/c31-lessons-index-audit.py:293-317`.
- The README carries at least six further count-bearing statements that no check
  reads: `:6` ("26 at the final stamp"), `:35` (selftest "26/26"), `:39-40`
  ("26"), `:97`, `:140`, `:207-212` (queue rows 49; owner classes path 37 /
  role token 12), `:256-257` ("146 files under nine directories", "26 `*.md`"),
  `:285` ("26/26 in-memory checks"). Live measurement today: 33 `*.md`, 146
  files under 9 dirs, selftest **28/28** (`--selftest` output).
- So the round's threshold ("C31/C34b PASS + findings == 0", `claims.json:37`)
  can be satisfied by a README that still asserts "26 at the final stamp" and
  "146 files / nine directories" without re-measurement. The after_required
  wording is stronger than the threshold ("prose arithmetic states 33",
  `claims.json:29`); the threshold is the weaker, checkable half.
- Note `:285` is **already stale at HEAD**: it says 26/26 in-memory checks while
  the tool's own selftest is 28/28 (`c31-lessons-index-audit.py:336-338`,
  README `:338` records 28/28 in Revision 2). It passes because nothing reads it.
- Required of O02/O06/R02: O02's delta must enumerate every count-bearing
  sentence (not only the two regex-checked ones), and O06 should carry a control
  of the class "stale count in unchecked prose stays green" so the integrator
  knows the coverage limit by name rather than by omission. Owner: O02, O06,
  R02. Axis at risk: operability (green that hides false prose) and calibration.

### X01-T3 — C × AGENTS.md × r31 jinii: SKILL.md has competing edit anchors, one of them unowned and already superseded

- `AGENTS.md:42` is a **dangling heading with no body**:
  `### 2.2 \`SKILL.md\` — append one item to "## Checklist (executable where a tool exists)" (after :534)`
  — the file ends there (`tail -20 AGENTS.md`). Its text is verbatim the r31
  jinii patch draft's section heading, `reports/round-31/jinii/draft.md:37`.
- That instruction was **already executed differently**: the jinii checklist item
  landed at `SKILL.md:713-715` (end of file), not after `:534`. Live bytes:
  `:522` heading, items `:524-534`, `## Corpus map` at `:536`, jinii item at
  `:713-715`. `reports/round-32/final-dossier.md:48` cites the jinii item as
  `SKILL.md:710-715` — a 3-line drift at HEAD (the item starts at :713).
- No round-33 seat owns a SKILL.md append (`targets.json:12-84`: no mission
  names one). Claim C does propose SKILL.md edits: the three box-1 citation
  pointer fixes, targets pinned at `SKILL.md:486/:488` (stale loanword pointers,
  content at corpus `:63`/`:59`) and `SKILL.md:501/:128` (contract-`:183`
  mis-cite) — `reports/round-32/final-dossier.md:46`,
  `dossier-d11-shonen-boxes.md:53-56`, `claims.json:46`, `targets.json:44`.
- Harm pathway: if the integrator "completes" `AGENTS.md:42` by appending a
  second checklist item after `:534`, (a) the jinii rule is duplicated, (b) every
  line anchor in the box-1 citation set (`:486/:488/:501/:534/:713`) shifts, and
  (c) the r32 dossier's citations silently become wrong. Conversely, if C14's
  pointer fixes land, the same anchors shift for the dossier's readings.
- Required: (i) the integrator/operator dispositions `AGENTS.md:42` as a stale
  leftover from r31 (it is not a round-33 seat deliverable) — this is a
  shared-file change, so it must be drafted, never applied by a seat; (ii) A09
  lists the SKILL.md anchor set as pin-cascade exposure; (iii) C14's drafts must
  be expressed as **content-anchored** (quote the cited text) rather than
  line-number-only, so application cannot mis-target after any other SKILL edit.
  Owner: integrator, A09, C14, R06.

### X01-T4 — O × filed bytes: the falsifier-mismatch fix cannot be an in-place edit — **provisional on K01**

- The debt phrase exists in exactly two filed places, both read-only for seats:
  `SCORECARD.md:443-444` and `LOG.md:3512-3514` ("the falsifier audit's filename
  mismatch (substance 5/5)"). Neither the dossiers nor any round-33 target names
  the mismatched filename (grep for `falsifier` across `reports/round-3{0,1,2}`,
  `LOG.md`, `SCORECARD.md`: the only "falsifier audit" hits are those two lines).
- Best-supported referent found by this seat (K01 owns confirmation): the r31
  jin'i-ryu telemetry-closure audit — `reports/round-31/jinii/analysis.md` +
  `draft.md` (+ an unpinned third file `patch-draft.md`), digest-pinned at
  `reports/round-31/validation.json:1055-1056`, runner constants at
  `reports/round-31/run-validation.py:34-35`, cited as `jinii/analysis.md` in
  `LOG.md:3450` and `reports/round-31/report-draft.md:34`.
- Caution for the ledger row: "(substance 5/5)" is **not** a 5-of-5 quality
  score. The phrase matches the jinii census "5/5 modern availability records …
  0/5 closings ever executed" (`reports/round-31/jinii/analysis.md:59,80,90,128`;
  `reports/round-31/report-draft.md:34`). A ledger row that records "substance
  5/5" as a substance verdict would be a misreading of filed bytes.
- Consequence for O05: because the mismatch lives in filed bytes, the only
  compliant disposition is **carried-with-owner+reason**, or a bounded fix
  expressed as a *new* file/row (forward errata). A fix draft that edits
  `SCORECARD.md` or `LOG.md` in place is a filed-bytes violation and must be
  refused by the integrator (`claims.json:30,50`; `targets.json:7`).
- Required of O05: state the disposition class explicitly, name the searched
  paths, and (if carried) give owner + reason + next touch. Owner: O05, R02.

### X01-T5 — A × O × C: content-level pin drift (no digest pin, but two bound readings)

- No frozen baseline pins SKILL.md or `corpus/lessons/README.md` bytes: grep of
  `tools/gates/frozen/*/MANIFEST.tsv` and `tools/gates/frozen/*/*/MANIFEST.tsv`
  for `SKILL.md|lessons/README` → zero rows; `tools/gates/frozen/handoff-packet-check/r9-pre/freeze.txt:2,110,119`
  mentions SKILL.md only in prose notes; `tools/gates/argot-derivation-gate.py:4`
  cites a SKILL.md section title in its docstring (spec citation, not a digest).
- But two **content readings bound to bytes** exist and both are in the r32
  admission record:
  1. box-1 inventory: "28/28 resolvable, exit 0 at SKILL sha `79fe91d3…`"
     (`dossier-d11-shonen-boxes.md:44-52,205`; `final-dossier.md:46`;
     `SCORECARD.md:431-433` depth row). Live re-run today reproduces it exactly:
     `python3 -B reports/round-30/craft/box1-survey.py` → exit 0, named 28 /
     resolvable 28, `skill_sha256: 79fe91d3…`. Note the survey tool only prints
     (`reports/round-30/craft/box1-survey.py:11`), so it is a safe re-pin control.
     Also note the tool's own recorded r30 json still carries the *pre-r31* sha
     `83b0a78a…` (`reports/round-30/craft/box1-landed-survey.json`), i.e. the
     pin lives in the dossier, not in the tool's output file.
  2. lessons index digest: the c31 receipt pins `index_sha256 = ee2a15df…`
     (`reports/round-25/audit/c31-lessons-receipt.json:18,27`), which is
     revision 1; live README is `ec7469da…` (29 059 B / 346 lines) — the C35
     revision-2 digest recorded at `corpus/lessons/C35-C36.md:25`. A pin check
     that compares live bytes to `ee2a15df…` will read a false mismatch.
- Consequence: any SKILL.md edit this round (C14's drafts) or README edit (O's
  rows) **moves a byte-bound reading** the r32 record relies on. A09 must list
  both rows and name the re-measure commands (box1-survey re-run; c31 `--json`
  receipt re-derivation); the integrator should land the re-measurement in the
  same pass as the edit, or record it as a carried reading. Owner: A09, R08,
  integrator. Axis at risk: adjacency (pin honesty) and calibration.

### X01-T6 — A07/A11-A13 × filed runners: re-runs must not clobber filed receipts

- `reports/round-25/run-validation.py` refuses to run outside an isolated clone
  under the lane's `.scratch` (`:1125-1128`, returns 2 "could-not-evaluate") and
  writes `reports/round-25/validation.json` (`:83`, `:1145`) only after
  `guard_receipt()` (`:1107-1109` → `tools/harness/receipt_guard.py`, refuses a
  committed-receipt overwrite unless `REFRESH_RECEIPTS=1`).
- Therefore any round-33 claim of the form "filed runner X now passes at HEAD"
  (e.g. for round 25's lessons leg after O's fix) is only obtainable in an
  isolated clone, and no seat may run a filed runner in-tree. The r32 runner
  states the same discipline for its own replay legs
  (`reports/round-32/run-validation.py:970-976`).
- Cross-claim linkage worth stating: at HEAD, round-25's lessons leg would fail
  on the same 7 orphans (`:860-930` checks orphans/phantom dynamically; no
  hardcoded 26 outside a selftest fixture at `:1009`), and O's fix is the
  precondition for it to be green again. That is a **re-measurement**, never a
  repair of filed bytes.
- Required: A07/A11-A13 either use `--check`-style dry paths or an isolated
  clone, and must not write any `reports/round-2x/validation.json`. Owner: A07,
  A11-A13, R07.

### X01-T7 — C × verification ownership: the ledger path has no seat owner

- Claim C's after_required puts the ledger at
  `reports/round-33/calib/open-items-ledger.json` (`claims.json:42,46`), but no
  seat's `out` is that path (`targets.json:45` C15 drafts
  `calib/C15-ledger-draft.json`); likewise `adj/audit-assembled.md` and
  `reports/round-33/run-validation.py` are owned by no seat (checked over
  `targets.json`). C's and A's counting command is that runner (`claims.json:48,61`).
- Consequence: claim C's and claim A's verification depends on
  integrator-only assembly steps. That is allowed by the round contract, but the
  honesty record must say so — the ledger row count cannot be verified by any
  seat fragment alone, and a green `run-validation.py` is an integrator claim.
- Required: S04's validation-leg spec and X04's honesty census must name these
  three integrator-owned artifacts explicitly, so no fragment claims seat-level
  verification of them. Owner: S04, X04, integrator.

### X01-T8 — cross-cutting (adjacent to X02/S05, flagged not absorbed): the r31 jinii rule is red at HEAD and cannot see round-33's own record

- Running the rule's own audit command verbatim (`SKILL.md:713-715`) prints
  **5 rows** at HEAD: `reports/round-{19,25,26,27,28}/availability.json` — the
  five retroactive closings were never executed, consistent with the r31 census
  "0/5 closings ever executed" (`reports/round-31/jinii/analysis.md:59,128`).
  The rule's success criterion is "must print nothing".
- Round-33's own telemetry record is `reports/round-33/telemetry/dispatch-declared.json`
  (`"closing_snapshot": "open-at-seat-close: …"`). It (a) has no `state` field
  and (b) does not match the audit's `reports/round-*/availability*.json` glob —
  so the round's own open record is **invisible** to the rule's mechanical audit,
  while `AGENTS.md` ("Close what you open") makes a closing snapshot a condition
  of LOG admission.
- Relevance to this round's claims: the five owed closings are **not** in the
  dossier's Decision 4 table (9 rows, T1) and are therefore not among the 12 —
  yet they are live-red at HEAD. A C ledger that reports 12/12 dispositioned is
  green while a 13th known standing debt with a red audit goes unledgered.
- Required: S05's telemetry draft names the r33 record's finalization path, and
  X02's conformance pass decides whether the closing snapshot is owed at close;
  claim C's ledger should either include the five-closing debt as a named
  adjacent item or state why it is out of scope. Owner: S05, X02, C13,
  integrator. Not absorbed: this seat files the observation, not the disposition.

## 3. Per-pair verdict table

| pair | verdict | basis |
|---|---|---|
| O × C | **trade (low)** — different files (O: `corpus/lessons/README.md`; C: SKILL.md drafts + ledger), but C's SKILL.md drafts share the file that `AGENTS.md:42` targets, and both claims feed the same `run-validation.py`; no direct write collision | T3, T7 |
| O × A | **trade (medium)** — A's scope watch + pin-cascade must absorb O's README rewrite: the index digest `ee2a15df…`/`ec7469da…` moves and no seat owns the re-measure | T5 |
| C × A | **trade (medium)** — C's SKILL.md pointer fixes move the `79fe91d3…` box-1 pin the r32 dossier binds; A09 is the owner of that cascade | T3, T5 |
| O × its own threshold | **harm pathway** — C31+C34b green is compatible with six stale count statements | T2 |
| C × SCORECARD/LOG | **harm pathway** — "12" has no filed counting rule; cross-check is unverifiable as written | T1 |
| C × filed bytes | **harm pathway (blocked)** — the only compliant falsifier disposition is carried/forward-errata; an in-place SCORECARD/LOG fix must be refused | T4 |
| A × filed runners | **harm pathway (operability)** — in-tree re-runs of filed runners are refused by design and would clobber receipts if forced | T6 |
| cross × telemetry | **standing red** — the r31 jinii audit prints 5 rows at HEAD; r33's own record is out of its glob | T8 |

No pair verdict above is "contradictory instructions" in the strict sense (two
seats ordered to write one path): the 64 declared `out` paths are disjoint
(§1). The collisions are all at the *shared-file* and *shared-reading* layer,
which is where this round's integrator must be careful.

## 4. Integration-order recommendation (from the trade set)

1. Apply the **README reconciliation** (O) first, then re-derive the c31 `--json`
   receipt, because O changes the index digest every later reading would inherit.
2. Only then apply the **SKILL.md pointer drafts** (C14), content-anchored, and
   immediately re-run `python3 -B reports/round-30/craft/box1-survey.py` (exit 0,
   28/28) as the box-1 re-pin control.
3. Do **not** act on `AGENTS.md:42`; record it as a stale r31 leftover (T3).
4. Re-run any filed runner only in an isolated clone; never in-tree (T6).
5. Assemble `calib/open-items-ledger.json` and `adj/audit-assembled.md` as
   integrator artifacts and say so in the validation receipt (T7).

## 5. Reconciliation with X00 (landed at 2026-10-19T04:01Z, after this seat's §1-§4 draft)

`reports/round-33/cross/X00-connector.md` landed while this fragment was being
written. Read in full at `04:0xZ`; reconciliation, not re-derivation:

- **Agreements (independently reached, same evidence).** No duplicate `out`
  paths / 64 distinct outs (X00 §1, this §1); zero frozen-pin exposure for
  README and SKILL.md (X00 §3, this T5 — same grep targets, same conclusion);
  C34b's blind spot (X00 §2 "R7" lists `:6-7, :35, :39-40, :118/:124/:127,
  :140, :204, :257, :285, :294`; this T2 lists `:6, :35, :39-40, :97, :140,
  :207-212, :256-257, :285`) — the union of the two lists is the honest set O02
  must enumerate, and X00's `:118/:124/:127` (§3 histogram 14/5/7) and `:294`
  ("the 24 filed lessons") are additions this fragment accepts. Live README
  digest and size agree (`ec7469da…`, 29 059 B / 346 lines).
- **Corroboration with a filed origin (upgrade to X01-T3).** The `AGENTS.md:42`
  residue is not a new discovery: it is filed as **F-X16-1** at
  `corpus/lessons/round-32.md:32` and open as **Q-32-2** at
  `corpus/lessons/round-32.md:56` ("excise `AGENTS.md:40-42` as a logged
  change"), with **F-X16-2 / Q-32-3** (`:33`, `:57`) already recording that the
  SKILL checklist item missed its verified anchor by 179 lines. T3's required
  action should therefore be read as *consume the filed disposition* (owner
  parent/operator), not as a fresh finding; the round-33 integrator must not
  invent a second disposition.
- **Upgrade to X01-T8.** The same lesson files the jinii audit defect as
  **F-X16-3 / Q-32-1** (`corpus/lessons/round-32.md:55`): the recorded
  falsification condition "has fired instrumentally; re-key the `SKILL.md:715`
  audit to the landed snapshot convention (`closes_record` + `closes_sha256`)
  or reword the clause — new recorded change, never in-place." This matches
  this seat's re-run (5 rows printed at HEAD; 0/5 `closing-snapshot.json`
  exist). T8's owner line is therefore parent/operator (Q-32-1), and any
  round-33 record shape that should be visible to that audit must use the
  landed snapshot convention or be filed as a named limitation.
- **One divergence (X00 is wrong; this seat re-measured).** X00 §3 item 2
  reports the in-tree refusal as "**exit 0**". Measured now:
  `python3 reports/round-25/run-validation.py` →
  `could-not-evaluate: run round validators only in an isolated Git clone under
  the lane's .scratch`, **EXIT=2**, and `reports/round-25/validation.json` mtime
  unchanged (Oct 18 14:58 — no clobber). The code path is `return 2`
  (`reports/round-25/run-validation.py:1125-1128`). A11-A13/R07 must use 2, not
  0; a could-not-evaluate recorded as a clean exit is exactly the class this
  lane's honesty rules exist to prevent.
- **Two X00 constraints this fragment adopts into its per-pair verdicts.**
  (a) X00's "R6" pipe-escaping rule (`reports/round-25/audit/c31-lessons-index-audit.py:138-149`;
  live `Q-20-3` example): any new r26-r32 queue row containing a literal `|`
  must escape it `\|` or C32 fails — a constraint on O02's queue rows that T2
  did not state. (b) X00 §3 item 4: `reports/round-26/audit/x63-lessons-audit.py:357`
  hard-codes `len(files) == 26` (verified: line 357 reads exactly that), so its
  selftest is red by construction at 33 files — **no round-33 seat may cite x63
  as a green lessons control**; this belongs in the op/ reviewers' checklist.
  X00's naming-collision note (a filed `reports/round-26/zzz-lessons-index-revision-3.md`
  already owns "revision 3") is likewise adopted as a constraint on O02's block
  heading.
- **No contradictions found between X00's collision matrix and this seat's
  per-pair verdict table** other than the exit-code divergence above; X00's
  sequencing (§4) and this seat's integration order (§4) agree on O-then-C
  ordering and on treating `run-validation.py`, the ledger and the assembled
  audit as integrator artifacts.

## 6. Post-landing reconciliation and self-corrections (K01/K03/O05/C14/A09 landed ~04:0xZ)

The wave's fragments landed while this section was being written; read at
`04:1xZ`. Two of this seat's §2 findings must be **corrected by this seat**,
not defended:

- **T4 corrected (my search scope was too narrow).** The full record of the
  "falsifier audit's filename mismatch" is filed at
  `corpus/lessons/round-32.md:36` (section heading), `:41` (F-X16-3, the
  mismatch in full) and `:55` (Q-32-1), located by K01
  (`reports/round-33/op/K01-falsifier-scout.md:3-12`). My §2-T4 sentence "the
  debt phrase exists in exactly two filed places" is **withdrawn**: my grep
  covered `reports/round-3{0,1,2}`, `LOG.md`, `SCORECARD.md`, `SKILL.md` but
  **not `corpus/lessons/`**, where the lesson names the mismatch completely.
  My provisional referent was directionally right (the r31 jinii/telemetry
  audit) but wrong in mechanism: the mismatch is the audit's predicate
  requiring a file literally named `telemetry/closing-snapshot.json` while the
  landed snapshots are `telemetry/availability-close-<N>.json`. My T4
  *consequence* stands and is confirmed by O05's own boundary
  (`reports/round-33/op/O05-falsifier-disposition.md:262`: "no filed-byte
  rewrites"; D-2/D-3/D-4 carried, D-1 fixed by draft).
- **T8 corrected (my "0/5 closings" reading was pre-landing).** The five
  closings **did land**: verified now —
  `reports/round-{19,25,26,27,28}/telemetry/availability-close-{19,25,26,27,28}.json`,
  5 files, each keyed `closes` + `closes_sha256` (read on all five; e.g.
  `reports/round-19/telemetry/availability-close-19.json` →
  `closes: reports/round-19/availability.json`, `closes_sha256: fa9588db…`).
  My sentence "the five retroactive closings were never executed" — taken from
  the pre-landing r31 census — is **withdrawn**. The audit's 5-row output is an
  **instrumental false-fire** (F-X16-3): `find reports corpus tools -name
  closing-snapshot.json` → no matches. The corrected residual item is sharper
  than my original: round-33's own record
  (`reports/round-33/telemetry/dispatch-declared.json`, no `state` field) is
  outside **both** the old predicate and the proposed re-keyed predicate
  (O05's NEW form keys on `closes` + `closes_sha256` over
  `availability-close-*.json`), so S05 must file the r33 record in a shape the
  landed convention can see, and X02 must rule on the closing snapshot at
  close. Owner: S05, X02, integrator.
- **T1 resolved in substance, residual narrowed.** K03 filed the counting rule
  (`reports/round-33/calib/K03-open-items.md:37-43`): the adopted convention is
  exactly this seat's option (d) — expand box-1 conditions 2/3/4 into 3 rows and
  lore-owned into 2, keep the cold-run set as one row → 12 — with the honest
  caveat that "12" is **reconstructed, not quoted** and that the numeral also
  collides with the "12 D4 garment-form holds" count (`:45-52`). My T1
  requirement ("file the counting rule as an explicit derivation") is
  **satisfied**. Residual: the C ledger must carry K03's reconstructed-not-quoted
  caveat rather than present 12 as a filed count, and C13/R05 should verify the
  membership (K03's §3 boundary calls already exclude Decisions 1-3 and the
  box-2 duplicates — the falsifier-checkable boundary T1 asked for).
- **NEW X01-T9 — O × C on SKILL.md: two claims now edit the same file.**
  O05's D-1 drafts a fix to the audit predicate at `SKILL.md:715`
  (`op/O05-falsifier-disposition.md:221`), and C14 drafts fixes at
  `SKILL.md:128, 213, 479, 481, 483, 485, 486, 488, 490, 491, 501, 701-704`
  (`calib/C14-fix-drafts.md:491`, anchored to sha `79fe91d3…`). A09's
  pin-cascade carries the C14 exposure and the box-1 re-survey obligation
  (`adj/A09-pins.md:39-40,83,90,110`) but **has no O05 row** (`grep -n "O05"
  reports/round-33/adj/A09-pins.md` → no hits). Required: (i) the integrator
  applies both edit sets in **one pass**, content-anchored — O05's draft quotes
  the predicate line and the landed keys, C14 cites the sha plus line numbers,
  so both survive only if applied before any other SKILL.md change; (ii) after
  the pass, re-derive the anchor set (`:47/:128/:149/:183/:486/:488/:501/:534/
  :713-715`) and file a **new** box-1 survey receipt (`python3 -B
  reports/round-30/craft/box1-survey.py`; `named_in_skill` may move off 28);
  (iii) A09/R08 owe an explicit O05 row in the pin-cascade table. Owner:
  integrator, A09, R08.
- **Key-name conflict adjudicated (this seat, live bytes).** K01 quotes the
  filed lesson's convention key as `closes_record`; O05's D-3 says the live key
  is `closes`. Verified on all five snapshots: the live key is **`closes`**
  (plus `closes_sha256`). K01's quote is faithful to the filed lesson prose,
  which is itself the inaccurate artifact — exactly O05's D-3 carry. No fragment
  is at fault; the ledger/receipt should cite the live key, and any re-keyed
  audit must use `closes`, not `closes_record`.
- **T6 reinforced by O05's D-4**: `reports/round-31/run-validation.py:780` is
  keyed to the exact filename `availability-close-<round>.json` — a second
  instance of the same name-keyed-instrument defect class as the SKILL.md:715
  predicate. T6's rule ("re-runs must not clobber filed receipts; name-keyed
  instruments are not substantive checks") now has two live examples.

## Owed

- `reports/round-33/op/K01-falsifier-scout.md` — **landed; reconciled in §6**.
  K01 located the mismatch (F-X16-3 at `corpus/lessons/round-32.md:36,41,55`),
  which supersedes this seat's provisional T4 referent and forces the T4 and T8
  corrections recorded above. No further reconciliation owed on this path.
  Original provisional note, retained for provenance: this seat ran an
  independent bounded search (grep `falsifier` over `reports/round-3{0,1,2}`,
  `LOG.md`, `SCORECARD.md`, `SKILL.md`; existence tests on four candidate paths,
  all MISSING) and filed the best-supported referent, not a confirmation.
- `reports/round-33/calib/K03-open-items.md` — **landed; reconciled in §6**
  (K03 adopted this seat's option (d) and filed the reconstructed-not-quoted
  caveat). Residual: C13/R05 verify membership; the ledger carries the caveat.
- `reports/round-33/cross/X00-connector.md` — **landed at 2026-10-19T04:01Z
  and reconciled in §5** (agreements, one verified divergence: X00's in-tree
  refusal exit code is 2, not 0; two adopted constraints: R6 pipe-escaping and
  the x63 hard-coded-26 trap). Remaining owed: the integrator should carry §5's
  union of unchecked README counts into O02/R02.
- `reports/round-33/op/O02-readme-delta.md`, `reports/round-33/calib/C14-fix-drafts.md`
  — **both landed ~04:0xZ**. C14 reconciled in §6 (content-anchored drafts at
  `:491`, sha-pinned; T9's dual-claim SKILL.md collision). O02 not read line-by-line
  by this seat before close: the remaining owed check is R02's — O02 must cover
  the union of unchecked count statements (§2-T2 + §5's X00 additions), which
  this seat could not confirm after the fragment landed.
- `reports/round-33/adj/A09-pins.md` — **landed; §6 adopts it** (E3 box-1
  re-survey, E4 line anchors) and adds the gap it does not cover: **no O05 row**
  for the second SKILL.md edit set (X01-T9). Owner: A09/R08/integrator.
- `reports/round-33/op/O05-falsifier-disposition.md` — **landed; §6 adopts it**
  (D-1 fixed-by-draft, D-2/D-3/D-4 carried; boundary line refuses filed-byte
  rewrites, satisfying T4's red line).

## Citations

- `reports/round-33/claims.json:9-15` (dispatch), `:16` (axes), `:20-38` (claim O),
  `:39-51` (claim C), `:52-64` (claim A), `:66-71` (non-goals)
- `reports/round-33/targets.json:5-11` (shared rules), `:13-16` (K01-K04), `:22-26` (O01-O05),
  `:44-45` (C14, C15), `:48-57` (A01-A09), `:74` (X01)
- `reports/round-33/telemetry/dispatch-declared.json` (`closing_snapshot: open-at-seat-close`)
- `REGIMEN.md:25-50` (per-round contract), `:60-69` (scope)
- `SCORECARD.md:431-433` (r32 depth row), `:441-445` (r32 admission + routed debt), `:447+`
- `LOG.md:3446-3455` (r31 jinii entry), `:3505-3517` (regimen-2 opening entry incl. standing inputs)
- `reports/round-32/dossier-d13-operator-decisions.md:123-138` (Decision 4, 9 rows), `:140-151` (method)
- `reports/round-32/dossier-d11-shonen-boxes.md:44-56` (box-1 conditions), `:199-208` (summary table)
- `reports/round-32/final-dossier.md:44-49` (box table; box-1 fix targets; jinii `SKILL.md:710-715` cite)
- `reports/round-32/dossier-d12-capability-inventory.md:55` (jinii capability row), `:97`
- `reports/round-32/run-validation.py:970-981` (replay discipline)
- `corpus/lessons/README.md:1-6, 31-40, 97, 140, 144, 202-212, 234-257, 279-305, 307-346`
- `reports/round-25/audit/c31-lessons-index-audit.py:293-317` (C34b), `:336-429` (selftest)
- `reports/round-25/audit/c31-lessons-receipt.json:18,27` (`index_sha256 ee2a15df…`)
- `reports/round-25/run-validation.py:83, 88-89, 860-930, 1107-1128, 1145`
- `corpus/lessons/C35-C36.md:25` (README rev-2 digest `ec7469da…`, 29 059 B / 346 lines)
- `AGENTS.md:42` (dangling SKILL.md heading) and the file tail ("Close what you open" bullet)
- `SKILL.md:486,488,501` (box-1 stale pointers per dossier), `:522-536` (checklist + Corpus map), `:713-715` (jinii item)
- `reports/round-31/jinii/draft.md:18,37,147,154,165`; `reports/round-31/jinii/analysis.md:59,80,90,128`
- `reports/round-31/run-validation.py:34-35, 827-900`; `reports/round-31/validation.json:1055-1056`
- `reports/round-31/report-draft.md:34`
- `reports/round-30/craft/box1-survey.py:11` (prints only) + its run output; `reports/round-30/craft/box1-landed-survey.json`
- `tools/gates/frozen/handoff-packet-check/r9-pre/freeze.txt:2,110,119`; `tools/gates/argot-derivation-gate.py:4`
- `tools/harness/receipt_guard.py:7,16,35-36,148`
- §5-§6 additions: `reports/round-33/cross/X00-connector.md:62-205,271`;
  `reports/round-33/op/K01-falsifier-scout.md:3-12`; `reports/round-33/calib/K03-open-items.md:37-52,75-90`;
  `reports/round-33/op/O05-falsifier-disposition.md:221-224,262`;
  `reports/round-33/calib/C14-fix-drafts.md:491`; `reports/round-33/adj/A09-pins.md:39-40,71-73,83,90,110,149`;
  `corpus/lessons/round-32.md:31-36,41,55-57`; `corpus/lessons/round-31.md` (F-X16 citations via K01);
  `reports/round-{19,25,26,27,28}/telemetry/availability-close-{19,25,26,27,28}.json` (keys `closes` + `closes_sha256`);
  `reports/round-26/audit/x63-lessons-audit.py:357`; `reports/round-31/run-validation.py:780`;
  `reports/round-25/audit/c31-lessons-index-audit.py:138-149` (R6 pipe parsing)
- Commands and outputs listed in §0 (all run 2026-10-19 at baseline `139e3b6`),
  plus §6's verifications: `ls reports/round-*/telemetry/`,
  `find reports corpus tools -name 'closing-snapshot.json'` (no matches),
  `python3 reports/round-25/run-validation.py` (EXIT=2, receipt mtime unchanged)
