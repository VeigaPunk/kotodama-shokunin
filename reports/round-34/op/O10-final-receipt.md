- Seat: O10 | scribe | claim O | date 2026-10-19 | baseline da68a6d

# O10 — claim-O final receipt fold (draft)

## 1. Scope and dependency status

Mission: fold the O07/O08/O09 verdicts into the claim-O final receipt draft.

**Dependency status: every O-block peer fragment is missing at seat time.**
`ls reports/round-34/` at this seat returns only `claims.json`, `targets.json`,
`telemetry/dispatch-declared.json` — there is no `reports/round-34/op/`
directory at all (round 34 is one 64-seat batch; all peers are still in
flight). Per the missing-dependency rule this fragment therefore carries:

1. the independent ground truth the fold must adjudicate (§2), run and cited by
   this seat so the fold is not an empty skeleton;
2. the errata the fold is now obliged to record (§3) — found by this seat
   against live bytes, not inherited from any peer;
3. the adjudication criteria the missing O07/O08 verdicts must be judged by
   (§4);
4. the claim-O receipt skeleton with explicit fold slots (§5) and the routing
   table draft for O09 to verify (§6);
5. the owed paths (§Owed).

Nothing in this fragment asserts that claim O is met. The tool
`tools/harness/receipt_guard_adoption.py` does not exist at `da68a6d`
(`ls tools/harness/` → `packet_links.py`, `packet_uncertainty.py`,
`r8_checks.py`, `receipt_guard.py` only), so no adoption verdict can be
reproduced until O02's source is landed by the integrator.

## 2. Independent ground truth: 28/28 filed-runner census at da68a6d

Counting command (the runner census):

```
ls reports/round-*/run-validation.py | wc -l
```

Observed: `28` (rounds 5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33).
There is no `reports/round-13/run-validation.py`.

### 2.1 Census table

`guard` = a call that invokes `tools/harness/receipt_guard.py`'s
`guard_receipt` on the runner's own receipt; `write` = the runner's own
receipt write. Class is assigned by whether a guard call reaches the write
path *before* it, not by whether the file mentions the guard (see §4-A).

| round | own-receipt write | guard def | guard call site(s) | class |
|---|---|---|---|---|
| r5  | `reports/round-5/run-validation.py:194` `(HERE/"validation.json").write_text` | — | — | unguarded-writer |
| r6  | `reports/round-6/run-validation.py:336` | — | — | unguarded-writer |
| r7  | `reports/round-7/run-validation.py:1171` | — | — | unguarded-writer |
| r8  | `:1486` (`OUTPUT_REL` def `:99`) | — | — | unguarded-writer |
| r9  | `:1910` (def `:127`) | — | — | unguarded-writer |
| r10 | `:1054` (def `:60`) | — | — | unguarded-writer |
| r11 | `:1740` (def `:125`) | — | — | unguarded-writer |
| r12 | `:1071` (def `:18`) | — | — | unguarded-writer |
| r14 | `:717` | `:413` `guard_preflight` | `:708`, `:716` | adopted-guarded |
| r15 | `:1346` | `:1037` | `:1337`, `:1345` | adopted-guarded |
| r16 | `:1265` | `:998` | `:1256`, `:1264` | adopted-guarded |
| r17 | `:1431` | `:1117` | `:1422`, `:1430` | adopted-guarded |
| r18 | `:1851` | `:1511` | `:1842`, `:1850` | adopted-guarded |
| r19 | `:21` (write inside an inline `python3 -c` program string) | — | — | unguarded-writer (embedded-write) |
| r20 | `:1485` | `:1278` | `:1484` | adopted-guarded |
| r21 | `:1115` (def `:20`) | — | — | unguarded-writer |
| r22 | `:922` | `:827` | `:911`, `:921` | adopted-guarded + clone-precondition `:902` |
| r23 | `:1097` | `:1064` | `:1094` | adopted-guarded + clone-precondition `:1076` |
| r24 | `:1184` | `:1151` | `:1181` | adopted-guarded + clone-precondition `:1163` |
| r25 | `:1145` | `:1108` | `:1142` | adopted-guarded + clone-precondition `:1123` |
| r26 | `:1909` | `:1855` | `:1906` | adopted-guarded (**errata E1**) |
| r27 | `:1907` | `:1853` | `:1904` | adopted-guarded |
| r28 | `:2098` | `:1996` | `:2095` | adopted-guarded |
| r29 | `:922` (`safe_path(OUTPUT).write_text`) | — | — | unguarded-writer (**trap T3**) |
| r30 | `:923` | `:883` | `:903`, `:922` | adopted-guarded |
| r31 | `:1159` | `:1118` | `:1139`, `:1158` | adopted-guarded |
| r32 | `:1143` | `:1102` | `:1123`, `:1142` | adopted-guarded |
| r33 | `:1471` | `:1441` | `:1459`, `:1470` | adopted-guarded |

### 2.2 Class totals

- **adopted-guarded: 17** — r14, r15, r16, r17, r18, r20, r22, r23, r24, r25,
  r26, r27, r28, r30, r31, r32, r33.
- **unguarded-writer: 11** — r5, r6, r7, r8, r9, r10, r11, r12, r19, r21, r29.
- **17 + 11 = 28** — every filed runner writes its own receipt; the
  `non-writer` class is empty, so it cannot serve as a live negative control
  and must be supplied as a fixture (see §4-B).
- **clone-precondition subset: 4** — r22:902, r23:1076, r24:1163, r25:1123 all
  open with `if ".scratch" not in ROOT.parts or not (ROOT / ".git").is_dir():`
  → `could-not-evaluate`, `return 2`. The other 13 adopted-guarded runners do
  not gate on the clone at all (r26:1879 only checks `(ROOT/".git").is_dir()`).

### 2.3 Guard wiring idioms (three distinct patterns the instrument must match)

- `importlib` style (r14, r15, r16, r17, r18, r20): `guard_preflight()` loads
  the module via `importlib.util.spec_from_file_location` and calls
  `module.guard_receipt(ROOT / OUTPUT, repo_root=ROOT)`
  (`reports/round-14/run-validation.py:413-425` is the template).
- `runpy` style (r22, r23, r24, r25, r26, r27, r28, r30, r31, r32, r33):
  `namespace = runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))`
  then `namespace["guard_receipt"](OUTPUT, repo_root=ROOT)`
  (`reports/round-32/run-validation.py:1102-1104` is the template).
- no guard (the 11 above).

Both adopted idioms call the guard **twice** in the modern shape (once before
`measure()` and once immediately before the write — r32:1123 then r32:1142);
r20 is the exception with a single call site (:1484) in the write path.

### 2.4 Runner digests (routing set + errata subject)

`sha256sum reports/round-*/run-validation.py` (full output reproduced by that
command); the 11 unguarded runners and r26:

| round | sha256 |
|---|---|
| r5  | `5fd5cb4198bdf1d01240ef13fbf6f59ae5ae18182c9afd0d865b619292f83676` |
| r6  | `c53f100927b8723bea25eeaa06048ace68fdfa3e763811a64e1104323e535c6e` |
| r7  | `c3b8418445d03bee2ba394ab6e4e4767e5ef07168c1a70dc904b3813e878c1e7` |
| r8  | `7eaa36789b4d71ce94ffadc93d2f5e10d6e0ca353df1c233d0ba94f29bff8369` |
| r9  | `8e4881309afaacc96f8f6e68f0c31041a9b2accc1c26bb1b20403f563364f5dd` |
| r10 | `23d6dc09002fe18c46778ac57d2c34246ab970a9371e7382950ca737d4019b0e` |
| r11 | `fab68287e74abc62d0681a1389bd0450d90020b65d7896ba2ab679e195acd9bd` |
| r12 | `2831c95c232c057361404c1860b82e88088b19c94b3ae26ec36be9e46fc6563c` |
| r19 | `5b27a80de1f4b11012061e7ed3e835734049661ace295b39878afd9f71454d3a` |
| r21 | `938cddeed86dedf52a4904c9c6a81248d6dc719c1330d4f3b64bcd8f3be896b0` |
| r29 | `59df391b2f80260ddfefe7a72651e1c67062bf376615ba7f21a1dd5bc5cf0ece` |
| r26 | `73297683d552b1673f2064a1a1ec76bf359f4add1bf8be4411ee77caa7f0be55` |

Reproduction recipe for the whole census (read-only, no runner executed):

```
for f in $(ls reports/round-*/run-validation.py | sort -t- -k2 -n); do
  n=$(echo $f | sed 's|reports/round-\([0-9]*\)/.*|\1|')
  echo "r$n guardcalls=$(grep -cE 'guard_receipt\s*\(|round_runner_main\s*\(' $f) \
writes=$(grep -nE 'OUTPUT\)?\.write_text|validation\.json\)\.write_text' $f | wc -l) \
clone=$(grep -c '\.scratch" not in' $f)"
done
```

## 3. Errata the fold must record

### E1 — r26 is guarded; the round-33 LOG's "same hazard" line is wrong as a class statement

`LOG.md:3559-3560` states: *"The r26 runner carries the same hazard (`:90`,
`:1909`)"*. Live bytes at `da68a6d`:

- `reports/round-26/run-validation.py:90` `OUTPUT = f"{ROUND_DIR}/validation.json"`
  where `:87` `ROOT = Path(__file__).resolve().parents[2]` and `:88`
  `ROUND_DIR = "reports/round-26"` → the receipt is the repo's own filed
  `reports/round-26/validation.json`.
- `:1855` `def guard_receipt():` … `:1857`
  `namespace["guard_receipt"](OUTPUT, repo_root=ROOT)`.
- `:1905-1909`:
  ```
  else:
      try:
          guard_receipt()
      except SystemExit as error:
          return error.code if isinstance(error.code, int) else 3
      safe_path(OUTPUT).write_text(rendered, encoding="utf-8")
  ```
  The guard is called on the write path immediately before the write, and a
  guard refusal (`SystemExit(3)`, or any non-int code → 3) returns **without
  writing**.

`reports/round-26/validation.json` is committed at HEAD —
`git ls-tree HEAD reports/round-26/validation.json` → `100644 blob d5b94963566c9b3ab5b41150201ce51a1f42ab36` —
so an in-tree run of r26 would be refused by the guard (exit 3, receipt
untouched) unless `REFRESH_RECEIPTS=1` is explicitly set. That is the
**opposite** failure mode from r5/r6/r7, whose `(HERE / "validation.json").write_text(...)`
at `:194` / `:336` / `:1171` overwrites unconditionally. The citation set
`:90`,`:1909` names the receipt's declaration and its write while omitting the
guard two lines above `:1909`.

**Consequence for claim O:** r26 must be classified `adopted-guarded`
(in-place writer, guard adopted, no clone precondition), not grouped with the
r5/r6/r7 unguarded class. The ABSOLUTE no-in-tree-execution rule still covers
r26 uniformly — this errata changes its *routing*, not its prohibition.

**Consequence for the record:** `LOG.md` is append-only; a new supersession row
carrying this correction is owed (§Owed), not an in-place edit of
`LOG.md:3559-3560`. The parent also owns correcting
`reports/round-34/claims.json` claim-O `before.gap`, which repeats the
mischaracterisation ("r26 carries the same hazard (:90,:1909)") — the integrator
holds that file's bytes, not this seat.

### E2 — the claim-O hazard set is incomplete as a routing set: 11 unguarded runners, not 4

The claim text names "r5/r6/r7 … and r26". The census (§2) finds **11**
unguarded in-place writers: r5, r6, r7, r8, r9, r10, r11, r12, r19, r21, r29.
The threshold "the four named hazards classified" is still satisfiable, but the
*routing artifact* required by claim O ("a receipt draft names the routing")
must cover all 11 or it will under-route seven unknown-hazard runners. O09's
verification mission is precisely this coverage check; the routing-set size to
verify against is **11**, not 4.

### E3 — r19's write is invisible to a body-AST scan

`reports/round-19/run-validation.py:5-23` runs its entire measurement inside a
`subprocess.run([sys.executable, "-c", """…"""])` string; the receipt write is
line `:21` **inside that string**:
`pathlib.Path('reports/round-19/validation.json').write_text(json.dumps(v,indent=1,ensure_ascii=False))`.
An AST walk of the runner's own body finds no write call at all, so a
body-AST-only instrument would file r19 as `clean` — a false green on a
confirmed hazard (round-33 LOG's mechanism line cites r5/r6/r7 as the writers
actually observed during the incident; r19 is the same hazard class by
inspection). Any instrument whose `unguarded-writer` set omits r19 must be
filed as a defect, not accepted.

## 4. Adjudication criteria for the missing O07/O08 verdicts

The fold cannot accept an O07/O08 verdict that does not test these five
predicates; each is derived from a live byte above.

- **A — mention ≠ adoption.** `grep -c receipt_guard` is not a classifier. r26
  mentions the guard 4× (`:1856`, `:1857`, `:199`, `:1855`) *and* adopts it;
  r25 contains `("receipt-guard-selftest", ("tools/harness/receipt_guard.py", "--selftest"))`
  at `:173` in its command inventory; r14 strings the token in its own checks
  at `:439`, `:445`. The instrument must key on a call whose guard applies to
  the runner's **own receipt path**, not on the token's presence.
- **B — the `non-writer` negative must be a fixture.** No filed runner is a
  non-writer (§2.2), so the required negative "a non-runner writing JSON is NOT
  flagged" cannot be demonstrated from the tree; a `.scratch` fixture is
  mandatory, plus a second fixture for "writes JSON but not a receipt".
- **C — fixture writes are false-positive bait.** r7 writes
  `scratch / f"positive-{index}.json"` at `:687` and `scratch / "expected.json"`
  at `:761`; r16 writes `clean_path.write_text(...)` at `:658`; r17 writes
  `(base / "expected-holds.json")` at `:1391`; r18 writes
  `(base_dir / "packet.d4.typed.yml")` at `:1807`. A detector that flags "any
  JSON write" will file four false positives against runners whose receipt
  write is correctly guarded.
- **D — idiom is not evidence.** r29 uses the *identical* modern line
  `safe_path(OUTPUT).write_text(rendered, encoding="utf-8")` at `:922` as the
  guarded r32 `:1143`, with no guard call anywhere in the file. Any classifier
  that infers adoption from the `rendered`/`safe_path` idiom calls r29 adopted
  → false green. r29 is the natural near-miss negative.
- **E — three guard idioms.** §2.3: `importlib` (`guard_preflight`),
  `runpy` (`namespace["guard_receipt"]`), and the direct
  `round_runner_main(...)` helper (used by none of the 28 filed runners — see
  `tools/harness/receipt_guard.py:161`, available but unadopted). A detector
  keyed only on `guard_receipt` misses any future `round_runner_main` adopter;
  the taxonomy should record all three.

## 5. Claim-O final receipt draft (skeleton; fold slots open)

### 5.1 Guard efficacy leg (evidence landed by this seat, not owed)

Ran at `da68a6d` (a tool selftest, **not** a round runner — F-C13-1 respected):

```
python3 -B tools/harness/receipt_guard.py --selftest    # exit 0
```

Observed (captured to `.scratch/o10/guard-selftest.json`,
sha256 `56a8d80295d388c48d1318bb3812ff0846ac3c6629be8113661af4ef2636e97a`;
scratch-only — the command above reproduces it):

```
tool tools/harness/receipt_guard.py
date 2026-10-19
passed 45 / 45   selftest_passed True
failed: []
```

The control set includes `committed-refused` (exit 3, bytes unchanged),
`committed-refresh-allowed` (`REFRESH_RECEIPTS=1` → exit 0),
seven non-exact `REFRESH_RECEIPTS` values refused, and
`staged-dirty-committed-refused`
(`tools/harness/receipt_guard.py:240-254`). This is the evidence that makes
"adopted-guarded" a *fail-closed* class rather than a notational one: a
guarded runner cannot rewrite a committed receipt without the explicit env
var. It does **not** cover r5-r12/r19/r21/r29.

### 5.2 Before → after (claim O), as the receipt must state it

- **before:** F-C13-1's mechanism is recorded in prose only
  (`LOG.md:3556-3562`); the hazard set named in prose is 4 runners and is
  mis-classified for r26 (E1); no instrument exists; the live count of
  unguarded in-place writers is 11 (§2.2) and is not recorded anywhere in the
  tree.
- **after (owed, pending O02 → integrator landing):**
  `tools/harness/receipt_guard_adoption.py --selftest` N/N green;
  `--json` emitting a 28-row inventory whose classes equal §2.1 row-for-row;
  O05's routing table covering all 11 unguarded runners; the r26 errata row.

### 5.3 Fold slots (each is blocked until its dependency lands)

| slot | source the fold must merge | status |
|---|---|---|
| O07 verdict | `reports/round-34/op/O07-verify-tool.md` — selftest N/N, `--json` vs O04 predicted inventory row-for-row | **owed** |
| O08 verdict | `reports/round-34/op/O08-traps.md` — three trap runners (guard imported but not called; guard called only under a flag; write via `os.replace`) honest or `could-not-evaluate` | **owed** |
| O09 verdict | `reports/round-34/op/O09-verify-routing.md` — routing covers every unguarded runner (verify against the 11-row set, §6) | **owed** |
| tool source | `reports/round-34/op/O02-tool-source.md` (bytes the integrator lands) | **owed** |
| predicted inventory | `reports/round-34/op/O04-predicted-inventory.md` (parity target for O07) | **owed** |
| routing table | `reports/round-34/op/O05-routing.md` (verified by O09) | **owed** |
| adoption-gap row | `reports/round-34/op/O05-routing.md` SCORECARD debt row | **owed** |

Until O02's bytes are in the tree, **no** adoption claim is reproducible; the
fold must not accept a verdict whose tool bytes are absent, and must record
`could-not-evaluate` for that leg rather than inferring from this fragment's
census (which classifies the *runners*, not the *instrument*).

### 5.4 Defects this seat files

- **D-O10-1** (documentation errata, not a peer defect): `LOG.md:3559-3560`
  and `claims.json` claim-O `before.gap` mis-classify r26 (E1). No filed byte
  repaired; supersession row owed.
- **D-O10-2** (coverage gap in the claim baseline): the hazard set is 11, not
  4 (E2).
- **D-O10-3** (instrument acceptance criterion): a body-AST-only detector
  cannot see r19 (E3); the instrument must be shown to flag r19 or the O07
  verdict is a measured false green.
- No defect is filed against O07/O08/O09 — their fragments do not exist yet,
  and absence is recorded as `owed`, never as failure.

## 6. Routing table draft (for O09 to verify)

Protocol assignment per claim O thresholds, with the census as the row source:

| protocol | runners | count | basis |
|---|---|---|---|
| isolated-copy-only (`git archive` → `.scratch/round-34/…`; never in-tree) | r5, r6, r7, r8, r9, r10, r11, r12, r19, r21, r29 | 11 | unguarded own-receipt write — an in-tree run silently rewrites a filed receipt (the F-C13-1 mechanism) |
| guarded refresh protocol in an isolated clone (`REFRESH_RECEIPTS=1`) | r14, r15, r16, r17, r18, r20, r22, r23, r24, r25, r26, r27, r28, r30, r31, r32, r33 | 17 | guard call on the write path; refusal proven by `receipt_guard.py --selftest` 45/45 |
| uniform prohibition (overrides both rows) | all 28 | 28 | REGIMEN/targets ABSOLUTE rule: no in-tree execution of any filed runner, guarded or not |

Note the two rows are *routing* classes under the standing prohibition, not
permissions: the guarded row names the protocol permitted **inside a clone**.
The 13 guarded runners without the clone precondition (r14-r18, r20, r26-r28,
r30-r33) rely on the guard alone for their receipt and on nothing at all for
their other side effects — the instrument's inventory should carry that as an
orthogonal column, and O09's coverage check should confirm every one of the 11
unguarded rows appears.

## Owed

- `reports/round-34/op/O07-verify-tool.md` (O07 verdict → §5.3 slot 1)
- `reports/round-34/op/O08-traps.md` (O08 verdict → §5.3 slot 2)
- `reports/round-34/op/O09-verify-routing.md` (O09 verdict → §5.3 slot 3)
- `reports/round-34/op/O02-tool-source.md` (tool bytes; integrator lands
  `tools/harness/receipt_guard_adoption.py` — §5.3 slot 4)
- `reports/round-34/op/O04-predicted-inventory.md` (parity target)
- `reports/round-34/op/O05-routing.md` (routing table + SCORECARD debt row)
- `reports/round-34/op/O01-impl.md`, `O03-selftest.md`, `O06-scribe.md`
  (upstream context for the fold)
- Integrator-side: the §3-E1 supersession row appended to `LOG.md` (append-only,
  no in-place edit of `:3559-3560`) and the claim-O `before.gap` correction in
  `reports/round-34/claims.json`
- Final receipt fold: §5 becomes
  `reports/round-34/op/O10-final-receipt.md`'s claim-O receipt once slots 1-3
  are filled; this fragment is that document's draft body.

## Citations

Paths and lines relied on (all read at `da68a6d`):

- `reports/round-34/claims.json` (claim O text, `before.gap`, thresholds)
- `reports/round-34/targets.json` (seat O10 mission/out; shared_rules)
- `REGIMEN.md:34-50`, `:60-69`
- `LOG.md:3548-3567` (F-C13-1 incident record; `:3556-3560` mechanism lines)
- `logs`: `git log --oneline -- reports/round-26/run-validation.py` → single
  commit `4f09c99`; `git log --oneline -- reports/round-5,6,7/run-validation.py`
- `git ls-tree HEAD reports/round-26/validation.json` → blob `d5b94963…`
- `tools/harness/receipt_guard.py:152-168` (`guard_receipt`,
  `round_runner_main`), `:240-254` (committed-refused / refresh controls),
  `:201-351` (selftest)
- `reports/round-14/run-validation.py:413-425` (importlib template), `:716-717`
- `reports/round-15/run-validation.py:1037`, `:1345-1346`
- `reports/round-16/run-validation.py:998`, `:658` (fixture write), `:1264-1265`
- `reports/round-17/run-validation.py:1117`, `:1391` (fixture write), `:1430-1431`
- `reports/round-18/run-validation.py:1511`, `:1807` (fixture write), `:1850-1851`
- `reports/round-19/run-validation.py:5-23` (inline `-c` program; write at `:21`)
- `reports/round-20/run-validation.py:1278`, `:1484-1485`
- `reports/round-21/run-validation.py:20`, `:474`, `:760` (path filter, not a
  clone precondition), `:1115`
- `reports/round-22/run-validation.py:827`, `:902`, `:911`, `:921-922`
- `reports/round-23/run-validation.py:1064`, `:1076`, `:1094-1097`
- `reports/round-24/run-validation.py:1151`, `:1163`, `:1181-1184`
- `reports/round-25/run-validation.py:173`, `:1108`, `:1123`, `:1142-1145`
- `reports/round-26/run-validation.py:87-90`, `:1855-1857`, `:1879`, `:1901-1915`
- `reports/round-27/run-validation.py:1853`, `:1904-1907`
- `reports/round-28/run-validation.py:1996`, `:2095-2098`
- `reports/round-29/run-validation.py:922`
- `reports/round-30/run-validation.py:883`, `:903`, `:922-923`
- `reports/round-31/run-validation.py:1118`, `:1139`, `:1158-1159`
- `reports/round-32/run-validation.py:1102-1104`, `:1123`, `:1142-1143`
- `reports/round-33/run-validation.py:1441`, `:1459`, `:1470-1471`
- `reports/round-5/run-validation.py:194`
- `reports/round-6/run-validation.py:336`
- `reports/round-7/run-validation.py:687`, `:761` (fixture writes), `:1171`
- `reports/round-8/run-validation.py:99`, `:1486`
- `reports/round-9/run-validation.py:127`, `:1910`
- `reports/round-10/run-validation.py:60`, `:1054`
- `reports/round-11/run-validation.py:125`, `:1740`
- `reports/round-12/run-validation.py:18`, `:1071`
- Commands run:
  - `ls reports/round-*/run-validation.py | wc -l` → `28`
  - `sha256sum reports/round-*/run-validation.py` (digests in §2.4)
  - `python3 -B tools/harness/receipt_guard.py --selftest` → exit 0, 45/45
  - `git ls-tree HEAD reports/round-{5,26,32}/validation.json`
  - `python3 -B .scratch/o10/census2.py` (census script, scratch-sha
    `1d0ee486790c3c9fd95dd57c5315f3e5a9274e69aeeda5156731d38ae6781641`;
    scratch-only — the table in §2.1 is the durable reproduction)
