- Seat: S02 | scribe | claim O | date 2026-10-19 | baseline da68a6d

# S02 — final operability receipt (claim O), rev 4 — post-review fold

Cut 2026-10-19T07:22Z. Rev 1 (07:08Z, `op/O06` only) → rev 2 (07:15Z, + scouts/
planners/reviewers) → rev 3 (07:18Z, + O01/O03/O04/O05/O07/O09) → rev 4 folds
**`op/O08-traps.md`**, the last O fragment to land. The only O-block path still
missing is **`op/O02-tool-source.md`**: the tool bytes were never delivered, so
`tools/harness/receipt_guard_adoption.py` does not exist and the instrument legs
stay `could-not-evaluate` (§6). This revision is the claim-O receipt; a later
hand re-cuts it if O02 lands (never rewrites this revision).

## 0. Verdict summary at this cut

| leg | verdict | basis |
|---|---|---|
| adoption census (ground truth the tool must reproduce) | **complete** — 28/28 rows, 17 adopted / 11 unguarded, plus a 29th out-of-glob writer | ten independent derivations, zero divergence (§1) |
| claim premise (`claims.json:42` four hazards) | **harmed** — r26 is not a hazard; the class is 11, not 4; the surface is 29, not 28 | §1.4-§1.5; O07-D1/D2, O08 F1, O09 D-1/D-2/D-4, R04 §4, R05 D-O-1/D-O-4 |
| routing rules | **verified at row level, with 2 standing defects in the delivered artifact + 1 digest drift** | O09 §8 (verified at O05 sha256 `487a2363…`; delivered O05 is `2ac33bc4…`, defects persist — §4.2) |
| trap resistance of the (unlanded) instrument | **specified and replayable, unmeasured** — O08's traps, expectations and replay script are durable; the tool they police does not exist | O08 §1-§5; §5 below |
| instrument correctness / selftest adequacy | **could-not-evaluate** — bytes absent | `op/O02-tool-source.md` never landed; `ls tools/harness/` has no instrument |
| operability axis for round 34 | **not verified** — `after_required` (`claims.json:45`) unmet | §3, §6 |

## 1. Census — ten independent derivations, no divergence

Census-building seats: O05 §2, O06 §2, O07 §2 (oracle `oracle.tsv` sha256
`9252d043…`), O08 §6 (`honest_probe.py`), O09 §4, O10 §2, K03 §3, R04 §2, R05
§1, X02 §2.1, plus this seat (`.scratch/s02-census.json` sha256 `eb9effc6…`).
All agree on the partition and every write anchor; R05's §7 snippet re-run here
prints `TOTAL 28 ADOPTED 17 UNGUARDED 11`.

### 1.1 Adopted — 17 (guard call on the publish path, before the write)

| runner | guard def / loader | call(s) | write | variant |
|---|---|---|---|---|
| r14 | :413 importlib | :420, :708, :716 | :717 | dual |
| r15 | :1037 importlib | :1044, :1337, :1345 | :1346 | dual |
| r16 | :998 importlib | :1005, :1256, :1264 | :1265 | dual |
| r17 | :1117 importlib | :1124, :1422, :1430 | :1431 | dual |
| r18 | :1511 importlib | :1518, :1842, :1850 | :1851 | dual |
| r20 | :1278 importlib | :1285, :1484 | :1485 | publish-only |
| r22 | :827 runpy | :911, :921 | :922 | dual, **receipt unfiled** |
| r23 | :1064 runpy | :1094 | :1097 | publish-only |
| r24 | :1151 runpy | :1181 | :1184 | publish-only |
| r25 | :1108 runpy | :1142 | :1145 | publish-only |
| r26 | :1855 runpy | :1906 | :1909 | publish-only; S02-F1 |
| r27 | :1853 runpy | :1904 | :1907 | publish-only |
| r28 | :1996 runpy | :2095 | :2098 | publish-only |
| r30 | :883 runpy | :903, :922 | :923 | dual |
| r31 | :1118 runpy | :1139, :1158 | :1159 | dual |
| r32 | :1102 runpy | :1123, :1142 | :1143 | dual |
| r33 | :1441 runpy | :1459, :1470 | :1471 | dual |

Every adopted row has a guard call strictly before its write; max gap 3 lines
(O07 §2.2).

### 1.2 Unguarded — 11 round runners, all with committed receipts

r5 `:194` · r6 `:336` · r7 `:1171-1173` · r8 `:1486` (`OUTPUT_REL` :99) · r9
`:1910` (:127) · r10 `:1054` (:60) · r11 `:1740` (:125) · r12 `:1071` (`out =
ROOT / OUTPUT` :1069) · r19 `:21` (**inside a `python -c` string**; file 24
lines) · r21 `:1115` (:20) · r29 `:922` (`safe_path(OUTPUT)`, :23).
`grep -c receipt_guard` = 0 in all eleven; no alternate refusal mechanism exists
(O09 §4.1).

### 1.3 The 29th writer — outside every `round-*` glob (S02-F2 ≡ O09 D-4)

`reports/supplement-opencode-1/run-validation.py:132`
`(HERE / "validation.json").write_text(...)`, zero guard references, receipt
committed at HEAD (`e8509d5e…`; runner `6f42e61c…`). `find . -name
run-validation.py` → 29 hits. O09 §4.3/D-4 reached this independently; R04 §5
and R05 F15 assert a 28-runner surface and are errated here. Under the claim's
`reports/round-*` glob, "100% of filed runners" is met **only if the exclusion is
stated by name**.

### 1.4 The four named hazards: 3 confirmed, 1 falsified, 8 omitted

Confirmed r5/r6/r7. **Falsified r26**: `:90` is the `OUTPUT` constant; `:1909`
is preceded by the call at `:1906` (`SystemExit` → return code at :1907-1908,
so the write is unreachable on refusal), demonstrated live by O09 §5.1
(`RECEIPT-GUARD-COMMITTED`, exit 3, `committed_blob=d5b94963…`). r26's residual
exposure is the stale lessons-README pin (r26:97) — a *staleness* class. Omitted:
r8, r9, r10, r11, r12, r19, r21, r29 — and `supplement-opencode-1` (§1.3).

## 2. F-C13-1 prevention controls (executed, not copied)

- `python3 -B tools/harness/receipt_guard.py --selftest` → 45/45, exit 0 (this
  seat; reproduced by O06 §3, O07 §3.4, X02 §2.3).
- CLI refusal on r5 → exit 3 `[RECEIPT-GUARD-COMMITTED]`, `committed_blob=778c3f5e…`;
  in-process `runpy` refusal → exit 3; digest `73a66f74…` unchanged; `git status
  --porcelain reports/round-5/` empty. O09 extended the refusal sample to r14,
  r20, r26, r32, r33 (all exit 3) and proved the uncommitted permit for r22
  (exit 0) — the basis of the G-UNFILED class (§4.1).
- **Live isolation proof (O09 §5.3, executed):** an isolated `git clone
  --no-hardlinks --local` run of r5 rewrote only the clone's receipt
  (`73a66f74…` → `fe926984…`), byte-identical to the mutant digest filed in
  `LOG.md:3552` for the round-33 incident.
- **Preservation replay (O08 §1, dry-run executed):** `replay.sh` re-digests
  every receipt in its isolated copy before/after a tool run and fails closed
  (exit 91) on any change; the dry run against a missing tool printed
  `PRESERVATION-OK … tool exit 2`.
- This seat's unguarded-mechanism control is scratch-only
  (`.scratch/s02-clobber-demo/`, `diff` exit 1). No filed runner was executed
  in-tree by any seat this round.

## 3. Before → after (claim O)

- **before:** hazard mechanism in prose only (`LOG.md:3548-3566`); hazard set
  named as 4 with r26 mis-classified; no instrument; no recorded count of
  unguarded writers. Measured extent: 11 round runners + 1 supplement runner,
  all committed.
- **after_required (`claims.json:45`):** durable tool, selftest green, JSON
  inventory covering every runner with adoption class and hazards classified,
  plus a routing receipt.
- **at this cut: not achieved.** The inventory *content* exists five ways (O04's
  predicted JSON, O05's routing, O06/O07/O08/O09/O10's censuses, this receipt);
  the tool that must emit it does not exist (§6).

## 4. Routing receipt (integrator applies)

### 4.1 Rules (as the delivered evidence supports them, not as claimed)

| class | condition | protocol |
|---|---|---|
| U-WRITE (11) | writes its own committed receipt, no guard call on the write path | **isolated-copy-only** — necessity and sufficiency proven by O09 §5.3 |
| G-COMMITTED (16) | guard call on the write path **and** receipt committed | guard-protected re-run; refresh only under an explicitly exported `REFRESH_RECEIPTS=1`; the guard refuses otherwise |
| G-UNFILED (r22) | guard call present, receipt **not** committed (never filed: `git log --all -- reports/round-22/validation.json` → empty) | **isolated-copy-only** — the guard returns normally for an uncommitted path (guard `:129-133`; live exit 0), so an in-tree run creates a new file inside a filed round dir with no refusal; round 22's own record forbids it (`reports/round-22/rerun.json:13`) |
| out-of-glob (1) | `reports/supplement-opencode-1/run-validation.py` | isolated-copy-only; must appear in the artifact or be excluded **by name with a reason** |
| uniform prohibition | all 29 | no in-tree execution of any filed runner; adoption class selects the off-tree protocol, never a permission (`tools/harness/receipt_guard.py:7-8,13-15`; X02 §4 item 6) |

Caveats to carry, not repair: **guard-bypass-by-exported-override** (an already
exported `REFRESH_RECEIPTS=1` disarms every guarded runner; `reports/round-21/run-validation.py:474`
is the in-tree export precedent, inside clones) and **publish-only adopters**
(r20, r23-r28 guard the write only).

### 4.2 Standing defects against the delivered routing artifact

`op/O05-routing.md` was verified by O09 §8 at sha256 `487a2363…`; the delivered
file hashes **`2ac33bc4…`** — verified revision ≠ delivered revision. Re-checked
by this seat against the delivered bytes; both defects persist:

- **O05-V-1 (r22 misroute).** R-A is scoped to "the 17 in §2.3"
  (`O05-routing.md:193`), which includes r22, so r22 inherits the in-tree
  refresh protocol; the artifact documents the uncommitted-target exit-0 branch
  (`:200-203`) without drawing the routing consequence. Correct routing: r22 →
  isolated-copy-only.
- **O05-V-2 (scope gap).** `grep -ni supplement reports/round-34/op/O05-routing.md`
  → no match; the 29th writer is absent from census, routing and owed list.
- **O05-V-3 (count wording).** `:249-253` says "four never mentioned in the
  record" while naming five pre-guard runners (r8-r12) plus post-guard r19/r21/r29;
  the unnamed count is 8 (3 named in `LOG.md` + 8 = 11).
- **Digest drift.** Any fold of O09 §8 must be re-pointed at `2ac33bc4…` or the
  verification re-run (O09 §9's own instruction).

## 5. Instrument acceptance spec (binding when the tool lands)

Adopted from R05 §5 (F1-F15), R04 §6 (ten-item checklist), O07 §5.1/§5.4 and
now **O08 §2** (trap expectations) — with this seat's two additions.

- **O08 trap battery** (conjunct with the filed runners): T1 (`round-901`,
  guard imported never called) → unguarded-write, never adopted/clean; T2
  (`round-902`, guard only under `--guarded`) → unguarded on the default path;
  T3 (`round-903`, `os.replace(staging, output)`) → unguarded-write, never
  clean/no-write; C+ (`round-904`, canonical runpy adoption) → adopted; C−
  (`tools/cache-export.py`, non-runner JSON writer) → not a runner row; plus
  R5 → unguarded, R26 → **adopted**, R19 → unguarded (embedded program). A
  verdict of adopted/clean on T1/T2/T3, or unguarded on r26, is a filed defect,
  not a nuance. `could-not-evaluate` with a named reason is acceptable for
  T2/T3/R19; a wrong green is not.
- **O08 replay + preservation**: `bash .scratch/o08-traps/replay.sh <tool>`
  (re-cutable from O08 §1-§4 after scratch cleanup) must report the §2 verdicts
  and `PRESERVATION-OK` — a tool that executes scanned runners is caught by the
  exit-91 fail-closed digest guard.
- **O07 §5.1/§5.4**: 28/28 coverage; partition exactly 17/11; write anchors
  equal to the oracle (r19 `:21`, not `:19`); `--selftest` covering the r32
  shape, an adopted runner not flagged, a non-runner writing JSON not flagged,
  and an r21-shape runner (mentions `REFRESH_RECEIPTS`, no guard call) flagged
  unguarded; `--json` symptoms map to O07-D1/D3a-d/D2.
- **O08 F3/F4/F5/F7 (new, folded)**: a call lexically inside the
  `def guard_receipt()` wrapper is **not** adoption (the real wrappers at r26
  :1857 / r32 :1104 contain such inner calls — O08's own first probe produced
  this exact wrong green); rename-into-place must resolve the *second*
  argument of `os.replace`; registration strings (r26:199) are not adoption;
  `protection_guard` (r29 `:779`, `:629-641`) is not receipt-guard adoption.
- **R05 F16 (this seat)**: alias resolution fixture — `out = ROOT / OUTPUT` +
  `out.write_text(...)` (r12 :1069-1071; also r8-r11, r21) → unguarded-writer;
  five filed runners depend on it.
- **R05 F17 (this seat, amending F15)**: declare the denominator — `round-*`
  glob → `inventory_len == 28` **plus** an explicit `out_of_scope` row for
  `reports/supplement-opencode-1/`, or a wider walk → 29 rows. A bare `28`
  without a scope statement is not acceptable (R04 §5 is the counter-example).
- **Thresholds**: `claims.json:51` is one-sided and its "four named hazards"
  clause is falsified — both need integrator rewording before any selftest can
  be counted green (R05 D-O-5, O07 §5.2).

## 6. Counting-command ledger (`claims.json:46-50`)

| command | status 07:22Z | evidence |
|---|---|---|
| `python3 tools/harness/receipt_guard_adoption.py --selftest` | **could-not-evaluate** — tool absent | `ls tools/harness/` → `packet_links.py packet_uncertainty.py r8_checks.py receipt_guard.py` |
| `python3 tools/harness/receipt_guard_adoption.py --json` | **could-not-evaluate** — tool absent | same; O07 §3.3 scanned every landed fragment for a tool block → zero hits |
| `python3 reports/round-34/run-validation.py` | **absent by design** | `find reports/round-34 -type f` |

Expected on landing: 28 in-glob rows, 17/11 partition, anchors per §1.1-§1.2,
hazards = 3 confirmed + r26 adopted, plus the §1.3 scope decision. Durable
parity targets: `op/O04-predicted-inventory.md` (per-row JSON, aliases resolved,
r19 marked embedded), O07's `oracle.tsv` (`9252d043…`), O08's
`.scratch/o08-traps/EXPECTATIONS.json` + probe results.

## 7. Post-review fold — verdicts

| input | fold verdict |
|---|---|
| `op/O01-impl.md`, `op/O03-selftest.md` | **accepted as design**; their control lists are superseded in practice by O07 §5.1 / O08 §2 / R05 F1-F15 (which add the r21-shape, wrapper-inner-call, `os.replace` and alias controls) |
| `op/O04-predicted-inventory.md` | **accepted** — landed after O07's polls, so O07's row-for-row diff against it is now runnable and owed; its class vocabulary is compatible with §1 |
| `op/O05-routing.md` (delivered `2ac33bc4…`) | **accepted with §4.2 defects standing** (V-1, V-2, V-3 + digest drift) |
| `op/O06-scribe.md` §2 | **accepted**; its r14 call site `:715` is errated to `:716` (O07-D4; this seat's census agrees — calls at :420, :708, :716) |
| `op/O07-verify-tool.md` | **accepted** — oracle green vs O06 (28/28, 0 defects) and O05 (11/11 anchors); tool legs `could-not-evaluate`; D1/D2 = S02-F1/F2; D3/D4 folded into §5 |
| `op/O08-traps.md` | **accepted** — trap battery + replay adopted as binding (§5); F1-F7 corroborate the census and add four detection requirements; its own first-probe wrong green (F3) is recorded as calibration evidence; §6 leaves r22's unfiled receipt `to-verify` (resolved by O09 D-3/§4.2 — the reason is round 22's clone-only policy, `reports/round-22/rerun.json:13`) |
| `op/O09-verify-routing.md` | **accepted** — 28/28 fact-level verification, executed isolation proof, V-1/V-2/V-3 folded; its §8 pinned to a superseded O05 digest (recorded, not smoothed) |
| `op/O10-final-receipt.md` | **accepted** — E1-E3, D-O10-1..3 folded; its routing draft needs the r22 G-UNFILED row and the §1.3 scope row |
| `scout/K03`, `plan/P02`, `review/R04`, `review/R05`, `cross/X02` | **accepted** as folded in rev 2 §7; R04 §5 and R05 F15's 28-runner surface claim are errated by §1.3 |
| `op/O02-tool-source.md` | **owed, not reviewed** — absence is `could-not-evaluate`, never failure |

## 8. Honesty and limits

- No axis verdict is stated for operability: the deliverable does not exist, so
  `improved` would be unverifiable; the claim is **not verified** and its premise
  is **harmed** as written. The round's validator and the integrator own the
  disposition.
- The census is a static classification of filed bytes at da68a6d, asserting what
  each runner *can* do, not what any run did. The only runner executions recorded
  in this fold are isolated-copy ones (O09 §5.3 r5-in-clone; O08 never ran a
  runner), permitted by `targets.json:9`.
- Ten derivations agreeing is strong evidence, not proof: five of them had to
  self-correct a first-pass false negative (r19 embedded write; the r12/r8-r11/r21
  alias; the r14-r20 `guard_preflight` spelling; the wrapper-inner-call green) —
  documented by R04 §3(a), R05 §2, O07 §1, O08 §7 F3 and this seat. The fixture
  battery and the replay script are what make the corrections durable.
- `to-verify`: why `LOG.md:3559` classified r26 as a hazard; whether O05 was
  re-filed to address V-1/V-2 (the digest moved, the defects did not); whether
  the instrument's authors knew about the embedded-write and out-of-glob classes;
  r19's runtime in-place semantics (O08 §9) and round 22's unfiled receipt (now
  explained by its clone-only policy).
- This seat wrote exactly one file, this one, across all four revisions. No filed
  round byte, `LOG.md`, `SCORECARD.md`, `AGENTS.md`, `corpus/`, `tools/` or
  `.ufo/` path was written; no state-mutating git command; no network; no install;
  no filed runner executed. Scratch: `.scratch/s02-census.py`,
  `.scratch/s02-census.json`, `.scratch/s02-clobber-demo/`.

## Owed

| owed path / item | owner | why |
|---|---|---|
| `reports/round-34/op/O02-tool-source.md` | O02 | the only O fragment still missing — without bytes the instrument cannot be landed or evaluated |
| tool landing at `tools/harness/receipt_guard_adoption.py` + inventory JSON (`reports/round-34/op/receipt-guard-adoption.json`, per P02 §1.5b) | integrator | the claim-O deliverable; acceptance spec §5 |
| re-run of O07 §5.3's comparator (tool `--selftest` + `--json` vs `oracle.tsv` `9252d043…` and `op/O04-predicted-inventory.md`) | integrator / later verifier | runnable the moment O02 lands; defect map O07 §5.4 |
| `bash .scratch/o08-traps/replay.sh <tool>` + verdict check against O08 §2/`EXPECTATIONS.json` | integrator / later verifier | trap-level acceptance; re-cutable from O08 §1-§4 after scratch cleanup |
| re-point or re-run of O09 §8 against O05's delivered digest `2ac33bc4…`; fold V-1/V-2/V-3 | integrator | verified revision ≠ delivered revision |
| scope decision for `reports/supplement-opencode-1/run-validation.py` (29th row or named exclusion) | integrator | S02-F2 = O09 D-4 |
| `LOG.md` errata row (r26 class; drafts at O06 §6.2, O09 §6 D-1), SCORECARD standing-debt row sized 11 (O07 §7.2), `claims.json:42`/`:51` corrections | integrator | shared bookkeeping and filed bytes are not seat-editable |
| final re-cut of this receipt once O02 lands | integrator / later scribe | new revision, never an edit of rev 4 |

## Citations

- `reports/round-34/claims.json:41,:42,:43,:45,:46-50,:51`; `targets.json:5-12,:44-53,:80`; `REGIMEN.md:25-50,:60-69`; `AGENTS.md`
- `LOG.md:3548-3566` (`:3551-3553` incident window/restoration, `:3552` the `fe926984…` digest, `:3557-3560` mechanism + r26 sentence, `:3565-3566` standing debt)
- `tools/harness/receipt_guard.py` (373 lines, sha256 `d2297da4…`): `:7-8,:13-15,:35,:129-133,:144-149,:152-168,:354-371`
- census anchors §1.1/§1.2 over `reports/round-{5..12,14..33}/run-validation.py`; r26 `:90,:97,:1855-1857,:1905-1909`; r32 `:1102-1104,:1123,:1142-1143`; r29 `:629-641,:779,:922`; r22 `:827,:911,:921,:922` + `reports/round-22/rerun.json:13`
- S02-F2 ≡ O09 D-4: `reports/supplement-opencode-1/run-validation.py:132` (`6f42e61c…`), receipt in HEAD (`e8509d5e…`), `find . -name run-validation.py` → 29
- folded fragments: `op/O01-impl.md`; `op/O03-selftest.md`; `op/O04-predicted-inventory.md`; `op/O05-routing.md` (:85, :154, :166, :193, :200-203, :249-253) sha256 `2ac33bc4…`; `op/O06-scribe.md` :73-74; `op/O07-verify-tool.md` §1-§7; `op/O08-traps.md` §1-§9 (traps T1-T3/C+/C−, F1-F7); `op/O09-verify-routing.md` §3-§9; `op/O10-final-receipt.md` §2-§6; `scout/K03-guard-pattern.md`; `plan/P02-oc-plan.md:16-:205`; `review/R04-o-review.md`; `review/R05-o-review.md`; `cross/X02-conformance.md` §2.1-§2.5, §4
- commands run by this seat (read-only, 2026-10-19T07:0x-07:22Z): `git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`; `git status --porcelain` → `?? reports/round-34/`; `ls -1 reports/round-*/run-validation.py` (28); `python3 -B .scratch/s02-census.py`; `sha256sum reports/round-*/run-validation.py`; `python3 -B tools/harness/receipt_guard.py --selftest` → 45/45 exit 0; guard CLI refusal on r5 → exit 3; in-process `runpy` refusal → exit 3; `sha256sum reports/round-5/validation.json` → `73a66f74…` unchanged; scratch clobber demo `diff` exit 1; `find . -name run-validation.py`; `grep -c receipt_guard reports/supplement-opencode-1/run-validation.py` → 0; `git cat-file -e HEAD:reports/supplement-opencode-1/validation.json` → PRESENT; `git log --all -- reports/round-22/validation.json` → empty; `git ls-files 'reports/round-*/validation.json' | wc -l` → 27; `find reports -mindepth 3 -name '*.py' | wc -l` → 158; `grep -ni supplement reports/round-34/op/O05-routing.md` → no match; `sha256sum reports/round-34/op/O05-routing.md` → `2ac33bc4…`; R05 §7 snippet re-run → `TOTAL 28 ADOPTED 17 UNGUARDED 11`; `python3 -V` → 3.14.7
