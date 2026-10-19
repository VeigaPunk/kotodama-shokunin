- Seat: O09 | verifier | claim O | date 2026-10-19 | baseline da68a6d

# O09 — routing-coverage verification (independent runner census vs O05)

## 1. Mission and dependency state

- Binding mission (`reports/round-34/targets.json:52`): "Verify O05's routing table
  covers every unguarded runner from the inventory with the correct protocol."
- **Dependency state at write time (04:0x UTC):** `ls reports/round-34/` returns only
  `claims.json`, `targets.json`, `telemetry/` — `op/O05-routing.md`,
  `op/O04-predicted-inventory.md`, `op/O02-tool-source.md`, `op/O07-verify-tool.md`,
  `op/O03-selftest.md`, `op/O08-traps.md` **do not exist yet** (all 64 seats run in
  parallel). Command: `find reports/round-34 -type f | sort`.
- Per the missing-dependency rule I executed every part that does not need O05:
  (a) built an **independent** census of every filed runner from live bytes with my
  own instrument (not O01/O02's), (b) derived the protocol rule set from guard
  semantics + the F-C13-1 incident record, (c) proved both necessity and sufficiency
  of the "unguarded ⇒ isolated-copy-only" protocol empirically, (d) reduced the
  O05 check to an exact row-for-row checklist. The row-for-row diff itself is owed
  (§8).

## 2. Instrument and method (independent of O01/O02/O04)

- Scripts (read-only, mine): `.scratch/o09/census.py` (AST scan: guard import/call
  sites, receipt-write sites), `.scratch/o09/writes.py` (every bytes-writing call with
  its unparsed target expression → `.scratch/o09/writes.json`).
- Classification axes: **(1)** does it write its *own* `validation.json` in place,
  **(2)** does it adopt `tools/harness/receipt_guard.py` **on the publish path**,
  **(3)** is its receipt committed at HEAD.
- Every class below is additionally confirmed by reading the runner's publish tail
  (not just the AST hit), and the four guarded/hazard classes are confirmed against
  live command output (§4).
- Limits (honest): static write-site + guard-call evidence; I did not attempt to prove
  runtime reachability of writes behind branches I judged dead. `r19` is a 24-line
  top-level script with no functions, so its write is unconditional. I executed no
  runner in-tree; the only runner execution anywhere in this fragment is `r5` inside
  an isolated local clone (§4.3).

## 3. Protocol rule set (what "correct protocol" means)

Derived from `tools/harness/receipt_guard.py` semantics and F-C13-1 prevention:

| Class | Condition | Required protocol | Why |
|---|---|---|---|
| U-WRITE | writes own receipt, **no** guard on the write path | **isolated-copy-only** (`git archive`/clone under `.scratch`; never in-tree) | the write is unconditional → an in-tree run rewrites a filed receipt (`receipt_guard.py` absent from the path) |
| G-COMMITTED | guard on the write path, receipt committed at HEAD | **guard-protected re-run**; refresh only under `REFRESH_RECEIPTS=1` | `receipt_guard.py:144-149` — refuses overwrite with `RECEIPT-GUARD-COMMITTED` unless `REFRESH_RECEIPTS` is exactly `1`; permits with `[RECEIPT-GUARD-REFRESH]` |
| G-UNFILED | guard on the write path, receipt **not** committed | **isolated-copy-only** (same as U-WRITE) | the guard returns normally for an uncommitted path (`receipt_guard.py:129-133`), so an in-tree run **creates** a new file inside a filed round directory with no refusal |
| NO-RECEIPT | never writes its own receipt | neither; guard class then attributed only for honesty of the inventory | n/a |

Consequence for the claim's `after_required` wording ("guarded re-run protocol for
adopted runners; isolated-copy-only for unguarded ones"): correct as far as it goes,
but **incomplete** — it must be read with G-UNFILED folded into isolated-copy-only,
otherwise `r22` would get the wrong protocol (see defect D-3).

## 4. Census result

Denominator: `ls reports/round-*/run-validation.py | wc -l` = **28** (rounds 5-12 and
14-33; rounds 1-4 and 13 have no runner). A 29th filed runner exists outside the
round glob: `reports/supplement-opencode-1/run-validation.py` (defect D-4).

### 4.1 Unguarded in-place receipt writers — 11 runners (class U-WRITE)

| Runner | receipt write site | guard anywhere in file | required protocol |
|---|---|---|---|
| r5 | `reports/round-5/run-validation.py:194` | no | isolated-copy-only |
| r6 | `reports/round-6/run-validation.py:336` | no | isolated-copy-only |
| r7 | `reports/round-7/run-validation.py:1171` | no | isolated-copy-only |
| r8 | `reports/round-8/run-validation.py:1486` (`output` bound `:1485`) | no | isolated-copy-only |
| r9 | `reports/round-9/run-validation.py:1910` (`output` bound `:1909`) | no | isolated-copy-only |
| r10 | `reports/round-10/run-validation.py:1054` (`output` bound `:1053`) | no | isolated-copy-only |
| r11 | `reports/round-11/run-validation.py:1740` (`output` bound `:1738`) | no | isolated-copy-only |
| r12 | `reports/round-12/run-validation.py:1071` (`out` bound `:1069`) | no | isolated-copy-only |
| r19 | `reports/round-19/run-validation.py:21` (top-level script) | no | isolated-copy-only |
| r21 | `reports/round-21/run-validation.py:1115` (`output` bound `:1113`) | no (its `REFRESH_RECEIPTS` use at `:474` is for *clones of other rounds*) | isolated-copy-only |
| r29 | `reports/round-29/run-validation.py:922` | no (`protection_guard` at `:629` guards *other* paths against change, not its own receipt) | isolated-copy-only |

Each of the 11 was checked for an alternate refusal mechanism and **none** exists:
`grep -c receipt_guard` = 0 and no `OUTPUT.exists()`/receipt existence check on the
write path (batch check over all 11: `receipt_guard_mention=False
exists_check_on_receipt=False`).

Documented-intent vs code gap worth recording: r5's own receipt asserts at
`reports/round-5/run-validation.py:191-193` "The previous acceptance receipt is
regenerated only in an isolated copy, never overwritten in this tree." — the runner
provides **no mechanism** for that; `:194` writes unconditionally. The discipline was
external (seat behaviour), not enforced.

### 4.2 Guarded runners — 17 runners (class G-COMMITTED, except r22)

Two adoption flavours, both fail-closed, both with the call on the publish path
immediately before the write:

| Runner | guard definition | call(s) before write | write site |
|---|---|---|---|
| r14 | `:413` `guard_preflight()` | `:708`, `:716` | `:717` |
| r15 | `:1037` | `:1337`, `:1345` | `:1346` |
| r16 | `:998` | `:1256`, `:1264` | `:1265` |
| r17 | `:1117` | `:1422`, `:1430` | `:1431` |
| r18 | `:1511` | `:1842`, `:1850` | `:1851` |
| r20 | `:1278` | `:1484` | `:1485` |
| r22 | `:827` | `:911`, `:921` | `:922` — **receipt NOT committed** (G-UNFILED) |
| r23 | `:1064` | `:1094` | `:1097` |
| r24 | `:1151` | `:1181` | `:1184` |
| r25 | `:1108` | `:1142` | `:1145` |
| r26 | `:1855` | `:1906` | `:1909` |
| r27 | `:1853` | `:1904` | `:1907` |
| r28 | `:1996` | `:2095` | `:2098` |
| r30 | `:883` | `:903`, `:922` | `:923` |
| r31 | `:1118` | `:1139`, `:1158` | `:1159` |
| r32 | `:1102` | `:1123`, `:1142` | `:1143` |
| r33 | `:1441` | `:1459`, `:1470` | `:1471` |

r14-r18/r20 load the module with `importlib.util.spec_from_file_location` and wrap the
call in `except (OSError, RuntimeError, ImportError) → RECEIPT-GUARD-UNAVAILABLE,
return 3` (`reports/round-14/run-validation.py:413-428`, tail `:707-717`).
r22-r28/r30-r33 load it with `runpy.run_path("tools/harness/receipt_guard.py")` and call
`namespace["guard_receipt"](OUTPUT, repo_root=ROOT)` (e.g.
`reports/round-26/run-validation.py:1855-1857`), with the call wrapped so a refusal
returns exit 3 (`reports/round-26/run-validation.py:1905-1909`).

**r22 is the exception:** `reports/round-22/validation.json` is absent from the working
tree *and* from git history (`git log --all -- reports/round-22/validation.json` →
empty; `git ls-files reports/round-*/validation.json | wc -l` = 27 for 28 runners).
Its guard therefore permits the write (§4.2 evidence below), and it is the only runner
whose receipt absence is a *policy*: `reports/round-22/rerun.json:13-14` records
`"round_validators_run_only_in_isolated_clones": true`,
`"live_filed_receipts_refreshed_by_x04": false`.

### 4.3 Non-runner `.py` files in `reports/` (false-positive traps for the tool)

| File | writes `validation.json`? | note |
|---|---|---|
| `reports/round-6/check-checkpoint.py:117` | no — writes `checkpoint-validation.json`; reads round-5's receipt at `:99` | naive "writes *validation*.json" matcher flags this wrongly |
| `reports/round-32/sweep-audit.py:440` | no — `validation.json` appears only inside a prose `limits` string | prose mention must not be flagged |
| `reports/round-30/verify-operability.py`, `reports/round-31/sweep-audit.py` | no (`validation.json` count 0) | clean negatives |
| `reports/supplement-opencode-1/run-validation.py:132` | **yes**, unguarded | outside the round glob; see D-4 |

## 5. Live command evidence

### 5.1 Guard refuses committed filed receipts (every guarded runner sampled)

```
$ for r in 14 20 26 32 33; do python3 tools/harness/receipt_guard.py reports/round-$r/validation.json; echo exit=$?; done
receipt_guard: refusing overwrite path=reports/round-14/validation.json committed_sha=da68a6d705e41f369f21e8607bfaab5b54077f84 committed_blob=ee49945ccf6ecfcb602f664ac6228cdba7ebd90f; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]
exit=3
... identical shape for r20 (blob 29d9efaf…), r26 (d5b94963…), r32 (cdd17ae2…), r33 (4e8089a9…)
```

This is the decisive evidence that **r26 is guarded**: its own receipt write at
`reports/round-26/run-validation.py:1909` is preceded by `guard_receipt()` at `:1906`,
and the guard's own live check refuses that exact destination with
`RECEIPT-GUARD-COMMITTED`.

### 5.2 Guard permits an uncommitted receipt path (r22)

```
$ python3 tools/harness/receipt_guard.py reports/round-22/validation.json
exit=0
```

No diagnostic, exit 0 → an in-tree `r22` run would create
`reports/round-22/validation.json` inside a filed round directory without any refusal.
This is the G-UNFILED hazard.

### 5.3 Isolated-copy protocol — necessity and sufficiency proven

```
$ git clone --quiet --no-hardlinks --local . .scratch/o09/iso/repo
$ cd .scratch/o09/iso/repo && python3 reports/round-5/run-validation.py
{"acceptance_checks_passed": false, "claims": {"F": false, "O": false}, ...}
r5-in-clone exit=1
$ sha256sum .scratch/o09/iso/repo/reports/round-5/validation.json
fe926984e8d15728c43c44b2fc4c0f60058f784aa4aa4b7c2e6aecc04a4dfeee   # was 73a66f7464ead0d99318750422256ceafac3d8c2d283f94604eb258abc1bb794
```

- **Necessity:** the unguarded runner rewrote its own filed receipt (`73a66f74…` →
  `fe926984…`) with no refusal — the U-WRITE hazard is real, not theoretical.
- **Sufficiency:** in the real repo, `sha256sum -c .scratch/o09/real-before.sha` →
  `reports/round-5/validation.json: OK`, `reports/round-26/validation.json: OK`,
  `reports/round-32/validation.json: OK`, `reports/round-22/run-validation.py: OK`;
  `git status --short -- reports/` → only `?? reports/round-34/` (this round's own dir).
  The isolated copy absorbed the whole mutation.
- **Cross-check with the filed incident record:** the digest my clone run produced,
  `fe926984…`, is byte-identical to the mutant digest filed in `LOG.md:3552` for the
  round-33 F-C13-1 incident ("r5 mutant digest `fe926984…` reproduced byte-identically
  by an isolated `git archive` run"). My independent clone run reproduces that filed
  digest exactly.
- **Routing-relevant side finding:** a naive "refresh the filed receipt" protocol for
  an unguarded runner would publish *false-red* content — on the current tree r5's
  measurement returns `acceptance_checks_passed: false` with
  `errors.F = "non-append corpus edit: ('corpus/lessons/supplement-opencode-1/sources/ottoman.json', 'OTT-06')"`.
  Historical-runners-are-baseline-bound is a **second** reason the protocol must be
  isolated-copy-only (mutation prevention is the first).

### 5.4 Canonical precedent for the isolated-clone protocol

`reports/round-21/run-validation.py:474` sets `env["REFRESH_RECEIPTS"] = "1"` **only**
inside a clone (`clone / f"reports/round-{number}/validation.json"`, `:475`), runs the
historical runner with `cwd=clone` (`:481`), and records `[RECEIPT-GUARD-REFRESH]`
presence plus before/after receipt digests (`:496-497`). Its filed limits text
(`:1106`) states the same policy. This is the filed shape O05's routing should cite.

## 6. Defects filed (against claim O's premise, and one filed record)

- **D-1 (false positive, r26).** `reports/round-34/claims.json:43` states "r26 carries
  the same hazard (:90,:1909)", and `LOG.md:3559` says "The r26 runner carries the same
  hazard (`:90`, `:1909`)". **Refuted:** `:90` is only the `OUTPUT` constant
  (`OUTPUT = f"{ROUND_DIR}/validation.json"`, `reports/round-26/run-validation.py:90`);
  the single write at `:1909` is preceded by the guard call at `:1906`, and the guard
  refuses that destination live (§5.1). r26's class is **G-COMMITTED**, protocol
  "guard-protected re-run; refresh only under `REFRESH_RECEIPTS=1`". Errata text the
  integrator may land as a NEW append-only `LOG.md` row (filed bytes are never
  edited): *"Erratum to the F-C13-1 hazard list: `reports/round-26/run-validation.py`
  is guarded (`guard_receipt()` `:1906` before the write `:1909`; live refusal
  `RECEIPT-GUARD-COMMITTED`, exit 3). The unguarded in-place writers are instead
  r5, r6, r7, r8, r9, r10, r11, r12, r19, r21, r29 (census in
  `reports/round-34/op/O09-verify-routing.md` §4.1)."*
- **D-2 (understated hazard census).** The claim names 3 unguarded hazards
  (r5/r6/r7); the live census finds **11** (§4.1). Any routing table that lists only
  the named three fails the claim's own threshold "covers 100% of filed runners".
- **D-3 (missing class, r22).** A guarded runner whose receipt is unfiled gets the
  same in-tree hazard as an unguarded one (§5.2). The routing table must therefore key
  the protocol on `guarded ∧ receipt-committed`, not on guard adoption alone.
- **D-4 (census scope).** `reports/supplement-opencode-1/run-validation.py:132` is a
  filed, unguarded in-place receipt writer outside `reports/round-*/`. The claim's
  instrument spec ("walk `reports/round-*/run-validation.py`") silently excludes it.
  Either the instrument's glob is widened or the exclusion is stated with a reason in
  the inventory; silently dropping it is a false-complete.
- **D-5 (documented intent without mechanism, r5).** `:191-193` claims isolated-copy
  discipline that `:194` does not enforce (§4.1). Worth a row in the standing
  adoption-gap debt, since it shows the 2026-10-19 in-tree breach was seat discipline
  rather than a stray command.

## 7. Checklist — what makes O05's routing table *verified* (for the integrator)

Run this literally against `reports/round-34/op/O05-routing.md` once it lands:

1. **Denominator.** Rows cover all 28 `reports/round-*/run-validation.py`
   (rounds 5-12, 14-33), and D-4 is resolved explicitly (either a 29th row for
   `reports/supplement-opencode-1/run-validation.py` or a stated scope reason).
2. **U-WRITE set = {5,6,7,8,9,10,11,12,19,21,29}**, each routed to
   **isolated-copy-only**. Any of these assigned a refresh protocol is a defect.
3. **G-COMMITTED set = 17 guarded runners minus r22** (r14,15,16,17,18,20,23,24,25,
   26,27,28,30,31,32,33), each routed to the guard-protected re-run / 
   `REFRESH_RECEIPTS=1`-only refresh protocol. Assigning isolated-copy-only here is
   *over*-broad but not harmful; assigning "refresh in-tree without the guard" is a
   defect.
4. **G-UNFILED = r22**, routed to isolated-copy-only (§5.2).
5. **The four claim-named hazards are each classified honestly** — r5/r6/r7 as
   U-WRITE, **r26 as G-COMMITTED** (D-1). A table that repeats the r26 hazard claim
   without evidence is a failure, not a pass.
6. **Per-row evidence.** Each row cites `file:line` for both the write site and the
   guard evidence; classes without a cited line are `to-verify`, not green.
7. **No false positives** on `reports/round-6/check-checkpoint.py` (writes
   `checkpoint-validation.json`), `reports/round-32/sweep-audit.py` (prose mention
   only) and `reports/round-30/verify-operability.py` / `reports/round-31/sweep-audit.py`
   (§4.3).
8. **Cross-check against O07/O04** — if the landed tool's `--json` inventory disagrees
   with §4.1/§4.2 on any runner, that disagreement is a defect to file, not to smooth
   over.

Falsifiers I would accept as defeat of this fragment: (a) a live in-tree refusal
demonstration for any of the 11 U-WRITE runners (there is no guard code for them to
run); (b) evidence that `reports/round-22/validation.json` is committed somewhere I
did not look (I searched the working tree and `git log --all`); (c) evidence that any
of the 11 writes is unreachable at runtime (I read each publish tail; `r19` has no
functions at all).

## 8. Row-for-row verification of O05 (landed after §1-§7 were written)

Target: `reports/round-34/op/O05-routing.md`. Read in full at 07:10Z on 2026-10-19 at
sha256 `487a23633106db931e6ef16cceeecc0720b3efbaaaaf449b4f831663abb71939`; the seat
re-filed it afterwards, and **§8.5 re-points this section at the current bytes,
sha256 `2ac33bc454342a3b3baf9dc481a65e9ca8b1d4fb1239c77f41764162331bfe2c`** (verified
at 07:2xZ; the 28-row census block and both rule texts are unchanged between the two
digests, so §8.1-§8.3 hold for both). O05 hit the same missing dependencies I did and
built its own
read-only census (its §2 command), so the two censuses were produced independently —
which is what makes this comparison worth anything.

### 8.1 Coverage verdict

| my §7 check | O05 evidence | verdict |
|---|---|---|
| 1. denominator = 28 round runners | `op/O05-routing.md:28,99` ("28 runners, 11 unguarded, 17 guarded") | PASS (except the supplement scope gap, V-2) |
| 2. U-WRITE set = {5,6,7,8,9,10,11,12,19,21,29} → isolated-copy-only | `op/O05-routing.md:103-117` lists exactly these 11; §3 R-B (`:211-227`) is the isolated-copy rule | PASS |
| 2a. write-site lines | O05's 11 write lines — 194, 336, 1171, 1486, 1910, 1054, 1740, 1071, 21, 1115, 922 — are **identical** to my §4.1 census (AST-derived) | PASS 11/11 |
| 3. G-COMMITTED (17 guarded minus r22) → guard-protected re-run | `op/O05-routing.md:144-164` lists the same 17; §3 R-A (`:193-209`) is the refresh rule | PASS |
| 3a. guard-call and write lines | O05's guard calls (`:420/:708/:716, :1337/:1345, :1256/:1264, :1422/:1430, :1842/:1850, :1484, :911/:921, :1094, :1181, :1142, :1906, :1904, :2095, :903/:922, :1139/:1158, :1123/:1142, :1459/:1470`) and write lines (717, 1346, 1265, 1431, 1851, 1485, 922, 1097, 1184, 1145, 1909, 1907, 2098, 923, 1159, 1143, 1471) **all match** my census | PASS 17/17 |
| 3b. two-phase vs single pre-write split | O05 `:166-170`: two-phase = r14-r18, r22, r30-r33; single = r20, r23-r28 — matches my call-site counts (r22 = `:911`+`:921`; r20 = `:1484` only) | PASS |
| 4. G-UNFILED r22 → isolated-copy-only | O05 classifies r22 "guarded" and folds it into R-A's "17 in §2.3" scope (`:193`) | **FAIL — defect V-1** |
| 5. the 4 claim-named hazards classified honestly | O05 §4 (`:240-248`) independently reclassifies r26 as adopted/guarded and keeps r5/r6/r7 as hazards, matching my §6 D-1 | PASS |
| 6. per-row evidence citations | every row carries target + write site + idiom, honest "heuristic + direct read" limits at `:294-301` | PASS |

### 8.2 Defects filed against O05

- **V-1 (protocol, blocks §7 item 4).** O05's §2.3 marks r22 `guarded` and §3 rule R-A
  is scoped to "the 17 in §2.3" (`op/O05-routing.md:193`), so r22 inherits the in-tree
  refresh protocol. Live evidence refutes that routing: the target
  `reports/round-22/validation.json` is uncommitted, so the guard permits the write
  (`tools/harness/receipt_guard.py:129-133`; observed
  `python3 tools/harness/receipt_guard.py reports/round-22/validation.json` → exit 0,
  no diagnostic). An in-tree r22 run would therefore **create a new file inside a
  filed round directory with no refusal**, and round 22's own record forbids it:
  `reports/round-22/rerun.json:13` `"round_validators_run_only_in_isolated_clones": true`.
  Correct routing: r22 is **G-UNFILED → rule R-B (isolated-copy-only)**. O05's R-A
  step 1 does describe the exit-0 branch honestly (`:200-202`) but never draws the
  routing consequence from it, and its §7 owed list does not flag r22 either.
- **V-2 (scope, blocks §7 item 1).** `grep -n supplement reports/round-34/op/O05-routing.md`
  → no match. The filed unguarded writer
  `reports/supplement-opencode-1/run-validation.py:132` is absent from O05's census,
  its routing, and its owed list. Either a 29th row or a stated exclusion is required;
  as landed, the "100 % of filed runners" threshold is met only under the narrower
  `round-*` glob, which O05 never states.
- **V-3 (internal arithmetic, minor) — FIXED in the re-filed bytes.** The
  `487a2363…` bytes said the hazard set grew by "three (r19, r21, r29) … and four
  never mentioned in the record (r8–r12 are the pre-guard block…)": the parenthetical
  names **five** pre-guard runners (r8, r9, r10, r11, r12) plus the three post-guard
  ones, so the unnamed count is **eight**, not four (3 named in `LOG.md` + 8 = 11).
  The current `2ac33bc4…` bytes read "the other eight are five pre-guard runners
  (r8–r12) and three filed *after* the guard existed (r19, r21, r29; §2.2 B5)" —
  correct; no further action.
- **V-4 (citation, no action needed).** O05 cites `LOG.md:3560` for the r26 hazard
  clause; I cited `:3559`. The sentence spans `LOG.md:3559-3560` ("The r26 runner" /
  "carries the same hazard (`:90`, `:1909`)") — both are correct readings of one
  continuous claim.

### 8.3 O05's supporting claims, independently confirmed

- B2 (r7 writes from `finally:`): `reports/round-7/run-validation.py` `try:` `:1053`,
  `finally:` `:1155`, in-place write `:1171` inside that `finally` — confirmed.
- B3 (r19 mutates rather than regenerates): `:19` `json.load(open('reports/round-19/validation.json'))`,
  `:20` field overwrite, `:21` `write_text(...indent=1...)` — confirmed.
- B4 (r5 prose vs code): confirmed — the isolation sentence is the last entry of the
  `limits` array (`:191-193`), one line above the unconditional write at `:194`.
- B5 (non-monotonic adoption): r19, r21, r29 were filed after r14 debuted the guard
  (`reports/round-14/run-validation.py:414` loads it) and still write unguarded —
  confirmed by my census (§4.1).
- Guard-semantics table (`op/O05-routing.md:177-191`): I reproduced the committed
  refusal for r14, r20, r26, r32, r33 and r29 (all exit 3, `RECEIPT-GUARD-COMMITTED`,
  blobs ee49945c…/29d9efaf…/d5b94963…/cdd17ae2…/4e8089a9…/749e6385…) and the
  uncommitted permit for `reports/round-22/validation.json` (exit 0). The
  `REFRESH_RECEIPTS=1` permission branch (O05 `:181`) also reproduces exactly:
  `REFRESH_RECEIPTS=1 python3 tools/harness/receipt_guard.py
  reports/round-33/validation.json` → exit 0,
  `receipt_guard: REFRESH_RECEIPTS=1 permits overwrite … [RECEIPT-GUARD-REFRESH]`,
  and `reports/round-33/validation.json` stayed `93b28f36…` (the guard CLI prints
  permission only; it never writes — `tools/harness/receipt_guard.py:354-369`).
- R-B's isolation form (`git archive <rev> | tar -x`) is equivalent to my executed
  `git clone --no-hardlinks --local` test; both confine the mutation to the copy, and
  my run reproduced the filed incident digest `fe926984…` (§5.3), matching
  `LOG.md:3555`'s stated precedent.

### 8.4 Net verdict on the mission

"Every unguarded runner from the inventory routed with the correct protocol" is
**verified for all 28 round runners' facts** (row-for-row agreement with an
independent census, §8.1), and **not yet verified for two things**: r22's protocol
(V-1, a real misroute under O05's own rule scope) and the supplementary runner's
inclusion (V-2). Both are cheap to fold — V-1 by moving r22 in §2.3 to the R-B side
(or by adding an explicit "unfiled receipt ⇒ R-B" clause to R-A), V-2 by one row or
one stated exclusion. Neither weakens the census; both must be recorded as errata
against `op/O05-routing.md` rather than silently inherited by the final receipt.

### 8.5 Convergence with the other censuses, and residuals (added after O04/O07 landed)

Three other fragments produced their own runner censuses between my §8 read and O05's
re-filing, so the partition is now independently replicated four times:

| census | source | result vs mine |
|---|---|---|
| O04 predicted inventory | `op/O04-predicted-inventory.md:41` `{"runners": 28, "guarded_in_place": 17, "unguarded_in_place": 11, "no_receipt_write": 0}` with 28 rows at `:44-71` | agrees on the split and on every write/guard anchor I hold (spot-checked r5/r8/r12/r14/r20/r22/r26/r29/r33) |
| O07 oracle | `op/O07-verify-tool.md:44-108` (11 unguarded + 17 adopted rows) | agrees; O07 §3.2 (`:128-138`) verifies O05's 11 unguarded rows and states it is "**not** O09's row-for-row routing verification" — i.e. that check stays with this seat |
| O06 census | `op/O06-scribe.md`, reported GREEN 28/28 in `op/O07-verify-tool.md:111-125` | agrees |
| this seat | §4.1/§4.2 | reference |

Two residuals survive that neither O04 nor O07 closes — neither overlaps V-1/V-2:
O04 records `reports/round-22/validation.json` as absent and never committed
(`op/O04-predicted-inventory.md:20-21,93-95`) yet classes r22
`guarded-in-place-write` with `hazard: false` and draws no routing consequence
(so V-1 stands unsupported-or-refuted by no one); O07 §3.2 checks only the 11
unguarded rows, not the r22 route. The supplement-runner scope gap (V-2) has since
been picked up by the O-block scribe independently of O05's bytes:
`scribe/S02-o-receipt.md:129,245` carries it by name ("out-of-glob (1) …
isolated-copy-only, and it must appear in the routing artifact or be excluded by
name with a reason"; "S02-F2 = O09 D-4").

## Owed

- `reports/round-34/op/O05-routing.md` — **verified; §8.1-§8.3 hold for both digests
  (`487a2363…` original, `2ac33bc4…` current)**, with V-3 fixed in the current bytes.
  Still owed to whoever folds O05: **V-1** (r22 belongs to R-B / needs an explicit
  "unfiled receipt ⇒ R-B" clause in R-A) and **V-2** (the supplement runner needs a
  29th row or a named exclusion). Any further re-filing needs §8 re-pointed again.
- Errata text for the F-C13-1 hazard list (D-1) — drafted in §6, landing is the
  integrator's (append-only new row; `LOG.md` and the round-33 bytes are never edited).
- `reports/round-34/op/O02-tool-source.md` — still not landed, together with the tool
  itself: `ls tools/harness/receipt_guard_adoption.py` → no such file. When both land,
  `python3 tools/harness/receipt_guard_adoption.py --json` should be diffed against
  §4.1/§4.2 (the O07 acceptance comparator, `op/O07-verify-tool.md:292-319`, is the
  ready harness for that). Closed since the first pass: O04 and O07/O06 — see §8.5.

## Citations

Paths and lines relied on (all read at tree `da68a6d`; `reports/round-34/*` is this
round's own unfiled dir):

- `reports/round-34/targets.json:52` — O09 mission.
- `reports/round-34/claims.json:41` — the four-hazard list (r5/r6/r7/r26) and the
  instrument glob `reports/round-*/run-validation.py`; `:45` — routing rule wording.
- `reports/round-34/claims.json:43` and `LOG.md:3559` — the r26 hazard assertion
  (refuted, D-1).
- `LOG.md:3548-3561` — F-C13-1 incident record; `:3552` — the `fe926984…` r5 mutant
  digest my clone run reproduced.
- `tools/harness/receipt_guard.py:144-149` (refusal + `REFRESH_RECEIPTS=1`),
  `:152-158` (`guard_receipt`), `:129-133` (uncommitted path returns normally),
  `:8` (fail-closed), `:16` (CLI).
- Unguarded write sites: `reports/round-5/run-validation.py:194` (+`:191-193` limits
  text), `reports/round-6/run-validation.py:336`, `reports/round-7/run-validation.py:1171`,
  `reports/round-8/run-validation.py:1485-1486`, `reports/round-9/run-validation.py:1909-1910`,
  `reports/round-10/run-validation.py:1053-1054`, `reports/round-11/run-validation.py:1738-1740`,
  `reports/round-12/run-validation.py:1069-1071`, `reports/round-19/run-validation.py:21`,
  `reports/round-21/run-validation.py:1113-1115`, `reports/round-29/run-validation.py:922`.
- Guarded runners: `reports/round-{14:413,708,716,717; 15:1037,1337,1345,1346;
  16:998,1256,1264,1265; 17:1117,1422,1430,1431; 18:1511,1842,1850,1851;
  20:1278,1484,1485; 22:827,911,921,922; 23:1064,1094,1097; 24:1151,1181,1184;
  25:1108,1142,1145; 26:1855,1906,1909; 27:1853,1904,1907; 28:1996,2095,2098;
  30:883,903,922,923; 31:1118,1139,1158,1159; 32:1102,1123,1142,1143;
  33:1441,1459,1470,1471}/run-validation.py.
- `reports/round-22/rerun.json:13-14` — clone-only policy; `reports/round-22/validation.json`
  absent (working tree + `git log --all`).
- `reports/round-21/run-validation.py:474-497`, `:1106` — canonical isolated-clone +
  `REFRESH_RECEIPTS=1` protocol.
- Non-runner negatives: `reports/round-6/check-checkpoint.py:99,117`,
  `reports/round-32/sweep-audit.py:440`, `reports/round-30/verify-operability.py`,
  `reports/round-31/sweep-audit.py`, `reports/supplement-opencode-1/run-validation.py:132`.

Commands run (outputs quoted in §4-§5):

- `ls reports/round-*/run-validation.py | wc -l` → 28; `find reports/round-34 -type f`
  → claims.json, targets.json, telemetry/dispatch-declared.json.
- `python3 .scratch/o09/census.py`, `python3 .scratch/o09/writes.py`
  (→ `.scratch/o09/census.json`, `.scratch/o09/writes.json`).
- `for r in 14 20 26 32 33; do python3 tools/harness/receipt_guard.py
  reports/round-$r/validation.json; done` → exit 3, `RECEIPT-GUARD-COMMITTED` each.
- `python3 tools/harness/receipt_guard.py reports/round-22/validation.json` → exit 0.
- `git clone --quiet --no-hardlinks --local . .scratch/o09/iso/repo` then
  `cd .scratch/o09/iso/repo && python3 reports/round-5/run-validation.py` → exit 1,
  clone receipt `73a66f74…` → `fe926984…`.
- `sha256sum -c .scratch/o09/real-before.sha` → all OK; `git status --short -- reports/`
  → `?? reports/round-34/` only.
- `git ls-files reports/round-*/validation.json | wc -l` → 27 (r22 absent);
  `git log --all -- reports/round-22/validation.json` → empty.
