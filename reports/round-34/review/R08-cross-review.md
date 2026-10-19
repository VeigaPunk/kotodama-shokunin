- Seat: R08 | reviewer | cross | date 2026-10-19 | baseline da68a6d

# R08 — cross-claim review: D packet prose ↔ C SKILL anchors; O inventory ↔ D build (F-C13-1 class)

**Window:** 2026-10-19T06:5xZ–07:1xZ, repo root, HEAD `da68a6d`
(`git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`), env
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. Every command below was
read-only in the durable tree; the only files I wrote are this fragment and
`.scratch/r08-skill-old.md` (a `git show 139e3b6:SKILL.md` dump used for the
difflib map). No runner was executed in-tree by this seat; no shared file was
edited.

**Verdict in three lines.**

1. **Leg A (D prose ↔ C anchors): no cross-reference drift exists** between the
   packet surface and the SKILL/anchor surface — the packet prose cites SKILL.md
   zero times (§1.1), and the one cross-reference the r33 edits touched (the
   contract digest in `examples/`) was *repaired* by da68a6d rather than broken
   (§1.2). The reissue obligation is confined to A09's R1–R8 rows, and my
   independent shift map reproduces K04 §5 and C03 §1 row-for-row (§1.3–1.5).
2. **Leg B (O inventory ↔ D build / F-C13-1): the round's own surfaces are
   clean** — D's build path executes no runner (§2.1), no tool subprocesses a
   runner (§2.2), and the worktree has zero modified filed bytes (§2.5) — but
   the tree contains **two pre-existing import-level, in-tree executions of
   filed runners** (§2.3) that the claim-O class vocabulary (O04 §"Class
   vocabulary") does not cover, so a clean adoption inventory must not be read
   as F-C13-1 clearance (§2.4).
3. **One filed claim/bytes conflict must be dispositioned**: `claims.json:41,:43`
   lists r26 as a hazard; the bytes make r26 *guarded* (§2.6). O04/O05/R04 and
   my own independent read all say guarded.

## 1. Leg A — D's packet prose vs C's SKILL anchors

### 1.1 Zero SKILL.md / line-anchor references on the packet surface (measured)

```
grep -n "SKILL" reports/round-30/handoff/declared-in-r6/packet.md   → 0 hits
grep -c "SKILL" reports/round-30/handoff/declared-in-r6/twin.json   → 0
grep -noE "[A-Za-z0-9_./-]+\.(md|py|json|yml|txt):[0-9]+(-[0-9]+)?" packet.md → 0 hits
```

So the r33 SKILL.md edits cannot have drifted any packet prose: there is no
coupling edge to drift. Two consequences the integrator should carry:

- The `declared-in-r7` draft (D05) should stay anchor-free like its predecessor;
  if any D seat *adds* a `SKILL.md:NNN` citation to the new packet, that
  citation becomes a new cross-claim surface and C03's reissue table must map it
  (my grep of `reports/round-34/depth/*` found no such addition at this stamp).
- The packet's own staleness is *internal* (claim-ledger rows vs manifest rows),
  which is exactly claim D's subject — independently confirmed in §1.7.

### 1.2 The only cross-reference r33 moved: the contract digest — repaired, not broken

- The packet pins `sha256:5f4c02bfc4e6…` at `reports/round-30/handoff/declared-in-r6/packet.md:14`
  and `:39` (A-01), and `expected.json.inputs["corpus/knowledge/synthesis/worldbible-integration-contract.md"]`
  carries the same value.
- Live bytes agree: `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md`
  → `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`.
- The contract file itself has not changed since round 8
  (`git log --oneline -3 -- corpus/knowledge/synthesis/worldbible-integration-contract.md`
  → newest `e1694ba`).
- da68a6d *changed the stale citations*: `examples/culture-d3/README.md:104`,
  `examples/culture-d3/handoff.md:27,:74`, `examples/handoff-packet.sample.md:21`,
  `examples/handoff-packet.sample.yml:45,:78` went `50c4c2f2…` →
  `5f4c02bf…` (`git show da68a6d --` those paths). Those files are **not** in the
  packet read set (A-05's own row text: "handoff/README deliberately excluded";
  the manifest's D3 rows are packet.json, packet.gates.yml, controls.json,
  expected.json, components/04–07), so no re-pin is owed and the packet was
  already citing the live value. Round 33 closed a drift; it did not open one.

### 1.3 The SKILL.md shift map — my independent measurement agrees with K04 and C03

Method: `difflib.SequenceMatcher(autojunk=False)` between `git show 139e3b6:SKILL.md`
(715 lines) and `SKILL.md` (732 lines). Non-equal opcodes, verbatim:

```
replace old 128  new 128        replace old 479  new 479
replace old 481  new 481        replace old 483  new 483
replace old 486  new 486        replace old 488  new 488
replace old 491  new 491        replace old 501  new 501
replace old 584      → new 584-586      (+2)
replace old 694-697  → new 696-700      (+3)
replace old 699-700  → new 702-705      (+5)
replace old 704      → new 709-720      (+16)
replace old 714-715  → new 730-732      (+17)
```

Spot-checks by address (`sed`): old `:47`→`:47`; `:128` in-place rewrite;
`:149`,`:183`,`:522`,`:534`,`:535`,`:536` unchanged; `:660`→`:662`
(`## Source-bounded culture drill — D3 (round 7)`); `:710`→`:726`; `:713`→`:729`;
`:714-715`→`:730-732`. K04 §5 ("584 +2; 694–697→696–700 +3; 699–700→702–705 +5;
704→709–720 +16; 714–715→730–732 +17") and C03 §1 ("eight same-line rewrites at
`:128,:479,:481,:483,:486,:488,:491,:501`; five insertion hunks with cumulative
deltas +2,+3,+5,+16,+17") are **row-for-row identical to mine** — three
independent seats, two independent methods (mine and K04's difflib; C03's
`git diff -U0` hunk reading). No defect.

### 1.4 `AGENTS.md:42` was deleted, not shifted — three-way agreement

`wc -l AGENTS.md` → 40; `grep -n ":534\|Checklist (executable\|SKILL.md" AGENTS.md`
→ 0 hits; da68a6d removed the closing fence and the
``### 2.2 `SKILL.md` — append one item … (after :534)`` instruction
(`git show da68a6d -- AGENTS.md` → 2 deletions). K04-F3 and P02 §R5 both record
"removed"; C03 §1 calls it "the one retirement". My leg-A conclusion: **A09-F3's
subject no longer exists in the tree** — the reissue row (C03 R5, P02 R5) must
read *removed at da68a6d*, and C04's byte-check has nothing to preserve for it.
No live surface now carries a SKILL.md line-number instruction
(`AGENTS.md` has no `SKILL.md` mention at all), so R5's remaining exposure is the
filed lesson citations (frozen bytes; superseded readings only).

### 1.5 Cross-check of the C-block's own anchor claims

- P02 §R5 anchor rows (`:522/:534/:536` hold; `:660→:662`; `:710→:726`;
  `:713-715→:729-732`; AGENTS excised) — each value equals my §1.3 measurement.
- C03 §2 R5 row points at its §3 table (30 rows, verifier failures 0) — a
  structure my map supports; C03's R6 row (`README.md:97→:105`, `:207→:254`) is
  outside my mission and I did not re-measure it (`to-verify` against a future
  read, owner C08).
- **No C-side claim mis-states a SKILL anchor**: I found no reissue row whose
  "new" address contradicts the map in §1.3.

### 1.6 Re-pin census cross-check (leg-A spillover into D's cascade)

`grep -rln "declared-in-r6" .` (excluding `.git/`, `.scratch/`) → **18 files**.
Classification by my reading: **2 live code pins** (`tools/exercise-handoff-e2e.py:1933-1934`),
**2 historical ledger rows** (`SCORECARD.md:400`, `LOG.md:3428` — append-only,
never edited), **14 filed-round rows** (`reports/round-30/**` incl. the pair's own
`packet.md:295`, `reports/round-31/scope.md:55`, `reports/round-33/**`). D10 §1
(21 rows, incl. derived aliases at `:3185`/`:4561`/`:4149`/`:4172` and the
`to-verify` MANIFEST.json row) is consistent with this and adds the derived
sites; I confirm D10's one-line census result: exactly one live pinning surface,
and it is the integrator-only `:1933-1934`. R02's independent pass is the
second vote.

### 1.7 Independent reproduction of claim D's live column (bytes, not fragments)

Measured directly from delivered bytes (no yaml module on this host; the file
parses as JSON):

| quantity | live value | source |
|---|---|---|
| `typed_labels` | **82** | `examples/culture-d4/typed-labels.d4.yml:29` `coverage` |
| `labels_by_kind` | native-form **64** / translated-label **12** / borrowed-strata **6** | same block |
| `findings_total` / `findings_hold_or_fail` / `label_findings_fail` | **12 / 12 / 0** | same block |
| `rank_rules_unresolved_items` / `rank_quarantine_handles` / `conflicts` | **0 / 0 / 0** | same block |
| `reconciliation_records` | 6 | same block |
| `typed_labels.stats` | `{fail 0, hold 12, labels 82}` | nested key (the `#stats` link target) |
| `expected-holds.json.counts` | **hold 12 / note 0 / fail 0**, 12 rows, all `D2L-FORM-UNRESOLVED` | `examples/culture-d4/expected-holds.json` |

This matches `claims.json:27` (live column) and D18 §`typed_labels`/`rank_quarantine_handles`.
It also confirms the packet's **internal contradiction**: `packet.md:285` already
carries the live values ("82 labels (64 native-form / 12 translated-label / 6
borrowed-strata), 12 findings (12 hold-or-fail), 0 unresolved rank items, 0
quarantine handles; hold set 12 holds / 0 note") while `:148-152` and `:307`
carry the stale ones — exactly the "self-contradiction" `claims.json:28` names.

**D2 must not be swept by symmetry (guards D03's warning).** Live D2 is
`typed_labels 58 (46/10/2)`, `findings_total 16 / hold_or_fail 15`,
`rank_rules_unresolved_items 13`, `rank_quarantine_handles 3`, `conflicts 4`,
`reconciliation_records 10` (`examples/culture-d2/typed-labels.d2.yml:29` block).
The strings `13 unresolved rank items` (packet `:49,:130,:284,:301`) and
`3 quarantine handles / 4 conflicts` are therefore **correct for D2 and wrong
only for D4**; D03 `:143,:159` already states this. A literal "replace every
13/3/4" edit would be a false edit — flagged as the highest-risk mechanical
error in the D rewrite.

**Twin carries the stale prose too.** `grep -o` census over
`reports/round-30/handoff/declared-in-r6/twin.json` → 11 matches of 7 stale
patterns (`types 74 labels` ×1, `56 native-form` ×1, `16 findings of which 15` ×1,
`15 holds, 1 note` ×1, `conflicts (4)` ×1, `three quarantine handles` ×2,
`13 unresolved rank items` ×4 — of which 2 are the *live* D2 rows). The twin is
the input to `tools/harness/packet_uncertainty.py` / `packet_links.py`, so the
r7 revision must regenerate the twin, not only `packet.md`; a packet-only rewrite
would leave the semantic twin stale while every gate stays green.

## 2. Leg B — O inventory vs D's build; the F-C13-1 class check

### 2.1 D's build path executes no runner

- The v3 leg commands are assemblers/gates/selftests only:
  `tools/exercise-handoff-e2e.py:3543-3546` → `assemble-culture-d4.py --check`,
  `assemble-d4-typed.py --check`, `d2-typed-labels.py --selftest`,
  `assemble-d4-typed.py --selftest`.
- `grep -n "run-validation" tools/exercise-handoff-e2e.py` → **0 hits**; its 11
  `subprocess.run` sites (`:443, :1359, :1648, :1815, :1857, :3458, :3700, :3737,
  :4183, :4350, :4369`) invoke the shape gate, the two harness validators, the
  legs above, or the tool itself, and the gate/harness calls move into isolated
  temp cwds (`cwd=str(isolated)`/`cwd=str(workdir)`).
- `grep -rn "run-validation" --include=*.py tools/` → only
  `tools/harness/r8_checks.py` prose/constant (`:10, :43, :67`). No tool
  subprocesses a runner.

### 2.2 Worktree state — the round's own F-C13-1 record is clean

`git status --porcelain` → `?? reports/round-34/` at every read (06:5xZ–07:1xZ).
Zero tracked file modified, so no filed `validation.json`, no filed runner, and
no shared file has been rewritten by any seat so far. (D11's preservation proof
covers the D claim's own surfaces; this line covers the whole tree.)

### 2.3 Two in-tree import-level executions of filed runners exist in the tree (named)

Neither is a subprocess and neither rewrites a receipt, but both execute a filed
runner's module body **from the live tree**, which is the letter of the F-C13-1
ban ("never execute any reports/round-*/run-validation.py in-tree — isolated
copies only"):

| # | surface | mechanism | called by | module-body effect (AST) |
|---|---|---|---|---|
| 1 | `tools/harness/r8_checks.py:273-286` | `spec_from_file_location(ROOT/"reports/round-7/run-validation.py")` + `spec.loader.exec_module` | `round7_measure` at `:378`, `:411` (`--selftest`) and `--measure` | `reports/round-7/run-validation.py`: only constants/`Path(__file__)`/`sorted`/f-strings plus `if __name__ == "__main__":` at `:1191` — no write at import |
| 2 | `reports/round-23/run-validation.py:341-348` | `spec_from_file_location(safe_path("reports/round-20/run-validation.py"))` + `exec_module` | `load_frozen_runner()` called at `:542` | `reports/round-20/run-validation.py`: constants/regexes only plus `if __name__ == "__main__":` at `:1497` — no write at import |

Mitigations measured: r8_checks sets `sys.dont_write_bytecode = True` around the
import (`:277-282`), so no `__pycache__` residue; r8_checks contains no write
calls at all; r23's own docstring (`:22`) restricts its sanctioned mode to a
`.scratch` clone, and because `ROOT = Path(__file__).resolve().parents[2]`
(`:46`) the clone run imports the round-20 **copy**, not the live file.

Consequences for this round (named, not absorbed):

- **R08-F3:** running `python3 tools/harness/r8_checks.py --selftest|--measure`
  in-tree *is* an in-tree execution of `reports/round-7/run-validation.py`. It is
  receipt-safe today only because r7's module level is inert. No seat may quote
  that command as "no runner executed", and the round's F-C13-1 statement must
  distinguish *receipt-writing execution* (none) from *module execution* (two
  surfaces, both pre-existing).
- **R08-F4:** the O instrument's class vocabulary (O04: `guarded-in-place-write`,
  `unguarded-in-place-write`, `no-receipt-write`, `not-a-runner`) has **no axis
  for "executes another filed runner"**, so its clean/adopted verdicts are
  receipt-write verdicts only. A grep of the O block and the reviews at this
  stamp (`grep -rn "r8_checks\|round-20/run-validation\|exec_module\|import.*runner"`
  over `review/*.md`, `op/*.md`) found these surfaces named only as ordinary tool
  paths (e.g. `R04-o-review.md:9`, `O03-selftest.md:48`), never as execution
  events. If the landed tool gains an `executes_filed_runner` field, both rows
  above are its live true rows; otherwise the instrument should record
  `could-not-evaluate` for the execution axis rather than imply "none exist".

### 2.4 Taxonomy-gap detail for the O verifiers

The 28-runner census itself (mine: `ls reports/round-*/run-validation.py | wc -l`
→ 28, rounds 5–12, 14–33, matching O04 §Method) is right; the gap is only that
"does it publish a receipt safely" and "does anything execute it in-tree" are
different questions. Both live execution surfaces belong to runners in the
`guarded-in-place-write` class on the receipt axis (r7 unguarded, r20 guarded),
so a routing table keyed only by the receipt class would still produce the right
run-protocol guidance — by luck, not by coverage.

### 2.5 The O/D interaction is nil in the other direction

D's cascade touches `tools/exercise-handoff-e2e.py` (a tool, not a runner) and
adds new files under `reports/round-34/`; the re-point cannot change any
runner's adoption class, and `expected.json`'s read set excludes the renderer
itself (58 inputs, renderer absent — D10 §2). O's inventory is therefore
unaffected by D landing, and D's re-point is unaffected by O's tool. Answering
the X00 mission's question for the integrator: **no runner's class moves**.

### 2.6 Filed conflict: r26 is guarded, not a hazard (independent third reading)

`claims.json:41,:43` (echoing LOG `:3559-3560`) lists r26 with the r5/r6/r7
hazards. Bytes: `reports/round-26/run-validation.py:1856-1857` loads
`tools/harness/receipt_guard.py` via `runpy.run_path` and calls
`namespace["guard_receipt"](OUTPUT, repo_root=ROOT)`; `:1906-1909` calls
`guard_receipt()` inside `try/except SystemExit` on the publish path and only
then `safe_path(OUTPUT).write_text(...)`. `:90` is merely the `OUTPUT` constant.
Measured class: `guarded-in-place-write`. O04 §"Contested reading", O05 §3.1 and
R04 `:168-181` reach the same conclusion; my read is a third independent vote.
**The round must disposition this** — the claim's hazard list cannot silently
shrink: either the round-34 record files a supersession row naming r26
reclassified (owner: integrator, with O05's routing text as the reason), or the
verifiers show why the guarded reading is wrong. Two claims-side texts that need
the row if it lands: `claims.json:41` ("Known hazards to classify") and
`claims.json:51` (thresholds) — neither is a filed byte (round-34 files are this
round's own declaration), but the change must be visible in the receipt chain,
not an in-place rewrite of the round's own record after the fact.

## 3. Named findings and dispositions

| id | finding | class | owner | evidence |
|---|---|---|---|---|
| **R08-F1** | `claims.json:41,:43` lists r26 as a hazard; bytes show guarded. Disposition row owed; the hazard set is r5/r6/r7 (+ the inventory's other measured unguarded rows). | claim/bytes conflict | integrator + O07/O09 | §2.6; `reports/round-26/run-validation.py:1856-1857,1906-1909`; O04 "Contested reading"; R04 `:168-181` |
| **R08-F2** | The `declared-in-r7` packet must regenerate **twin.json** as well as `packet.md` (11 stale-text matches in the r6 twin; the gate judges are twin-fed). A packet-only rewrite passes some gates while leaving the semantic twin stale. | build-completeness | D05/D06 + integrator | §1.7; `grep -o` census over `reports/round-30/handoff/declared-in-r6/twin.json` |
| **R08-F3** | `tools/harness/r8_checks.py:273-286` executes `reports/round-7/run-validation.py`'s module **in-tree** on `--selftest`/`--measure`; no seat may run it and then assert "no runner executed". Inert today (r7 module body has no writes; `:1191` guard). | F-C13-1 letter-class | integrator + verifiers | §2.3 |
| **R08-F4** | The O instrument's taxonomy lacks an execution axis; its `--json` clean/adopted verdicts must not be quoted as F-C13-1 clearance. Second live instance: `reports/round-23/run-validation.py:341-348` → round-20 runner (clone-scoped when run as documented). | taxonomy gap | O02/O07/O08 + integrator | §2.3–2.4 |
| **R08-F5** | Cross-claim drift: **none** — packet prose has zero SKILL.md/line-anchor citations, and the r33 edits repaired (not broke) the contract-digest cross-reference in `examples/`. C03/P02 anchor rows match my independent difflib map (three-way agreement with K04 §5). | no-defect verdict (recorded) | integrator | §1.1–1.5 |
| **R08-F6** | `AGENTS.md:42` is deleted (not shifted); the reissue must say "removed at da68a6d" and C04 has no byte to preserve for it. | reissue correctness | C03/C08 + integrator | §1.4 |
| **R08-F7** | Live-number risk: the D rewrite must not sweep `13/3/4` across D2 rows — D2's live values are 13 unresolved / 3 quarantine / 4 conflicts; only D4's are 0/0/0. D03 `:143,:159` already guards this; flagged as the likeliest mechanical error. | false-edit hazard | D03/D18/D20 + integrator | §1.7 |

## 4. Cheap re-run list for the integrator at close (my checks, re-runnable)

```sh
# leg A: no new coupling between D's packet and C's anchors
grep -n "SKILL" reports/round-34/handoff/declared-in-r7/packet.md reports/round-34/handoff/declared-in-r7/twin.json   # expect 0
# leg A: shift-map spot checks
grep -n "^## Source-bounded culture drill — D3 (round 7)" SKILL.md          # 662
sed -n '729,732p' SKILL.md; wc -l AGENTS.md; grep -c "SKILL.md" AGENTS.md   # r31 item; 40; 0
# leg B: no runner subprocess anywhere live
grep -rn "run-validation" --include=*.py tools/ | grep -v r8_checks.py      # expect 0
git status --porcelain                                                       # expect only ?? reports/round-34/
# leg B: the two import-level surfaces still exist and are still inert
grep -n "exec_module" tools/harness/r8_checks.py reports/round-23/run-validation.py
# §1.7 live numbers
python3 -c "import json;c=json.load(open('examples/culture-d4/typed-labels.d4.yml'))['coverage'];print(c['typed_labels'],c['labels_by_kind'],c['findings_total'],c['rank_rules_unresolved_items'],c['rank_quarantine_handles'],c['conflicts'])"
python3 -c "import json;print(json.load(open('examples/culture-d4/expected-holds.json'))['counts'])"
```

## Owed

My mission's own dependencies are all landed and were read: `scout/K04-anchor-census.md`,
`depth/D10-repin-drafts.md`, `depth/D03-ledger-rows.md`, `calib/C03-anchor-reissue.md`,
`op/O04-predicted-inventory.md`, `op/O05-routing.md`, `review/R04-o-review.md`,
`plan/P02-oc-plan.md`. What I could **not** verify, with owners:

- `reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json,freeze.txt,run.log}`
  — **do not exist yet** at this stamp (`find reports/round-34 -type f` → no
  `handoff/` entries; D05/D02 drafts only). R08-F2 (twin regeneration) and §1.1's
  "stay anchor-free" are therefore conditions on bytes I could not read; the
  integrator/verifier must re-run §4 leg A after the revision lands and reject
  the round if the twin or packet gains a stale pattern or a SKILL.md anchor.
- `reports/round-34/depth/D05-packet-draft.md`, `depth/D06-twin-expected.md`,
  `depth/D09-freeze-design.md`, `depth/D13-negatives.md`, `depth/D17-verify-gates.md`,
  `depth/D19-verify-repin.md`, `depth/D20-verify-preservation.md`,
  `op/O02-tool-source.md`, `op/O08-traps.md`, `calib/C07-verify-survey.md`→landed,
  `calib/C08-verify-reissue.md`→landed — of these, still **absent** at my listing:
  D05, D06, D09, D13, D17, D19, D20, O02, O08. R08-F2/F4's tool-side halves
  (does the landed tool carry an execution axis? does the frozen r7 row appear in
  its JSON?) are verifiable only once `op/O02-tool-source.md` lands.
- `reports/round-34/run-validation.py` — not written; the round's acceptance legs
  cannot be checked here. Its F-C13-1 leg, if it exists, should include §2.3's
  two import surfaces as *named pre-existing exceptions*, not as failures of
  this round.
- r26 disposition (R08-F1) — the row's text and location are the integrator's
  decision; I only measured that the filed claim and the filed bytes disagree.

## Citations

Files read (all at `da68a6d`, 2026-10-19):

- `reports/round-34/{claims.json (esp. :24-34, :41-43, :51), targets.json (R08 row + shared_rules)}`,
  `scout/K04-anchor-census.md`, `depth/D03-ledger-rows.md`, `depth/D10-repin-drafts.md`,
  `calib/C03-anchor-reissue.md`, `op/O04-predicted-inventory.md`, `op/O05-routing.md`,
  `review/R04-o-review.md`, `plan/P02-oc-plan.md`, `op/O03-selftest.md`, `op/O01-impl.md`
- `reports/round-30/handoff/declared-in-r6/{packet.md (:1-160, :274-335), expected.json, twin.json, freeze.txt}`
- `reports/round-7/run-validation.py` (:54-94, :1191), `reports/round-20/run-validation.py` (:52-97, :1497),
  `reports/round-23/run-validation.py` (:22, :46, :220-227, :341-355, :542),
  `reports/round-26/run-validation.py` (:90, :1856-1857, :1906-1909),
  `reports/round-12/run-validation.py` (:492-508 — recorded command strings only, no execution)
- `tools/harness/r8_checks.py` (:10, :43, :57, :64-67, :273-286, :378, :411, :558, :585-591, :609-610),
  `tools/harness/receipt_guard.py` (:35, :144-152, :161),
  `tools/exercise-handoff-e2e.py` (:38-39, :107, :443, :1359, :1648, :1815, :1857, :1933-1934, :3185, :3456-3458, :3543-3546, :3700, :3737, :4149, :4172, :4183, :4350, :4369, :4561)
- `examples/culture-d4/typed-labels.d4.yml` (:29 coverage block, `typed_labels.stats`),
  `examples/culture-d4/expected-holds.json`, `examples/culture-d2/typed-labels.d2.yml` (:29 block),
  `corpus/knowledge/synthesis/worldbible-integration-contract.md` (digest + `git log`),
  `examples/culture-d3/{README.md,handoff.md}`, `examples/handoff-packet.sample.{md,yml}` (via `git show da68a6d`)
- `SKILL.md` (:31-536, :584-586, :662, :690-732), `AGENTS.md` (40 lines, 0 `SKILL.md` hits),
  `reports/round-33/adj/A09-pins.md` (R1-R8, findings)

Commands (2026-10-19, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, repo root):

- `git rev-parse HEAD` → `da68a6d…`; `git status --porcelain` → `?? reports/round-34/`;
  `git show --stat da68a6d`; `git show da68a6d -- AGENTS.md examples/culture-d3/{README.md,handoff.md} examples/handoff-packet.sample.{md,yml}`;
  `git log --oneline -3 -- corpus/knowledge/synthesis/worldbible-integration-contract.md`
- `grep -n "SKILL" …/packet.md` → 0; `grep -c "SKILL" …/twin.json` → 0;
  `grep -noE "[A-Za-z0-9_./-]+\.(md|py|json|yml|txt):[0-9]+(-[0-9]+)?" …/packet.md` → 0;
  `grep -o "types 74 labels|56 native-form|16 findings of which 15|15 holds, 1 note|conflicts \(4\)|13 unresolved rank items|three quarantine handles" …/twin.json | sort | uniq -c`
- python one-liner verifying all 59 `artifact_manifest` rows' sha256 against live bytes → 58 match, 1 (A-GLOSS, inline pseudopath) not-a-file
- python `difflib.SequenceMatcher(autojunk=False)` over `git show 139e3b6:SKILL.md` vs `SKILL.md` (opcode list in §1.3);
  `sed -n '47p;128p;149p;183p;486p;488p;501p;522p;534,536p;660p;713,715p;716,732p' SKILL.md`;
  `grep -n "^## " SKILL.md`
- python AST scans of module-level effects for `reports/round-7/run-validation.py` and `reports/round-20/run-validation.py`;
  `for f in $(grep -ln exec_module reports/round-*/run-validation.py); do grep -n -B8 exec_module "$f"; done`;
  `grep -rn "runpy.run_path|spec_from_file_location|run-validation" reports/round-*/run-validation.py`
- `ls reports/round-*/run-validation.py | wc -l` → 28; `grep -rn "run-validation" --include=*.py tools/`;
  `sed -n '260,330p' tools/harness/r8_checks.py`; `grep -n "dont_write_bytecode" tools/harness/r8_checks.py`;
  `grep -n "write_text|write_bytes|open(" tools/harness/r8_checks.py` → 0
- `for ln in 443 1359 …; do sed -n "$((ln-6)),$((ln+3))p" tools/exercise-handoff-e2e.py; done`;
  `grep -n "run-validation" tools/exercise-handoff-e2e.py` → 0
- `python3 -c` JSON parses of `examples/culture-d4/{typed-labels.d4.yml,expected-holds.json}`,
  `examples/culture-d2/typed-labels.d2.yml`, `reports/round-30/handoff/declared-in-r6/expected.json`
- `grep -rln "declared-in-r6" .` (excluding `.git/`, `.scratch/`) → 18 files;
  `grep -rn "declared-in-r6" --include=* .` (spot classification)
- `ls -la tools/harness/`; `grep -n "^def |^class |REFRESH" tools/harness/receipt_guard.py`
- `sed -n '1850,1860p;1900,1912p' reports/round-26/run-validation.py`;
  `sed -n '210,236p;335,362p' reports/round-23/run-validation.py`
- `find reports/round-34 -type f | sort` (twice: 06:5xZ and 07:1xZ); `date -u` → 2026-10-19T07:12:54Z
