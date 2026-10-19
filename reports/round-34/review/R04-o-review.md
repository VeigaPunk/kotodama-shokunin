- Seat: R04 | reviewer | claim O | date 2026-10-19 | baseline da68a6d

# Adversarial review — claim O (guard-adoption instrument)

Scope of what I could review: the claim premises and the measurement surface
against filed bytes, plus my own independent runner census. The instrument
itself (`tools/harness/receipt_guard_adoption.py`) and every O fragment were
**absent** from the tree when this review ran (`ls tools/harness/` → packet_links.py,
packet_uncertainty.py, r8_checks.py, receipt_guard.py; `find reports/round-34 -type f`
→ claims.json, targets.json, telemetry/dispatch-declared.json). Instrument-byte
correctness is therefore **could-not-evaluate** here and is listed under `## Owed`;
what follows is a byte-grounded census, a taxonomy that survives the traps I found,
and a falsification checklist the landed instrument must pass.

## 1. Independent census (denominator pinned to filed bytes)

Counting commands (read-only, no runner executed):

- `git ls-files 'reports/round-*/run-validation.py' | wc -l` → **28**
- `ls -d reports/round-*/ | wc -l` → **30**; `reports/round-13/` and
  `reports/round-34/` have no runner and no `validation.json`. A denominator of
  30 round directories would report a false 28/30 coverage gap; the honest
  denominator is the 28 filed runners.
- `git status --porcelain` → only `?? reports/round-34/`, so filed runner bytes
  equal HEAD (da68a6d) bytes; my digests are HEAD digests.

Per-runner digests (sha256, full) and byte sizes at da68a6d:

```
r5   13322  5fd5cb4198bdf1d01240ef13fbf6f59ae5ae18182c9afd0d865b619292f83676
r6   22976  c53f100927b8723bea25eeaa06048ace68fdfa3e763811a64e1104323e535c6e
r7   61654  c3b8418445d03bee2ba394ab6e4e4767e5ef07168c1a70dc904b3813e878c1e7
r8   67177  7eaa36789b4d71ce94ffadc93d2f5e10d6e0ca353df1c233d0ba94f29bff8369
r9   95359  8e4881309afaacc96f8f6e68f0c31041a9b2accc1c26bb1b20403f563364f5dd
r10  47178  23d6dc09002fe18c46778ac57d2c34246ab970a9371e7382950ca737d4019b0e
r11  79703  fab68287e74abc62d0681a1389bd0450d90020b65d7896ba2ab679e195acd9bd
r12  56216  2831c95c232c057361404c1860b82e88088b19c94b3ae26ec36be9e46fc6563c
r14  38729  b06bf6b12cf87377c52d245e6b1da413aab2ab17620d98dd7bc2a6ce467273b8
r15  66023  5323a8d36ada8addcbcba90e1a874e118bb7099720c345cd4974c7bed7418b67
r16  61901  295629ae128347b854759bda9d1e41b0497bc2c269267ac920146f6b5aa891d6
r17  69909  6b98abadef9951be7cfce006f339dad036f7b341cee6713ecc00be6e5f9095ec
r18  91829  01b138500ce30ad25cc8f0078110d6b2afeb9bf8ca79f5903deae3746c19bca8
r19  1868   5b27a80de1f4b11012061e7ed3e835734049661ace295b39878afd9f71454d3a
r20  74842  2b7a252b5449415dddac2e667ed2e192df800a80173849989fa72423961646da
r21  60405  938cddeed86dedf52a4904c9c6a81248d6dc719c1330d4f3b64bcd8f3be896b0
r22  52976  3af74c2b40f007c21581b037c9059512bd745d4fe8645dd9e4364818a4e463dd
r23  59458  ae897cb8d808f0c1432948154d440f9c86730685b32b91442d9714dc27692cb2
r24  63823  ba3b18a79e9b0dbbe9fae70b7bc4b27f50d670ff025b1b24cf7f14b1ac6d43ad
r25  60048  d19435251dccb738e456c01fe7fb94498c27bae7f70704a96f94ec9324ce35af
r26  99993  73297683d552b1673f2064a1a1ec76bf359f4add1bf8be4411ee77caa7f0be55
r27  93483  36b597068d59a88156090e5c179e1ab2c68fe4ce7735d7b1bb6f67d82babe08a
r28  108915 20e09ea8db7bcb306b0c8948c7b8afb62eca5e0d47f674ebfea9643f2f6add77
r29  46279  59df391b2f80260ddfefe7a72651e1c67062bf376615ba7f21a1dd5bc5cf0ece
r30  51696  2f447223ece3f48195bf4c2d7f026b37b2e5cc88924c002408f8bd663e7a3e31
r31  58950  9e01c4274c1afc0be983ba3c7610fc44212ab2d3e934f747b57ef6b9584488dc
r32  57470  6fd1b96e682fde67e85f52c01573c175ac047b014f9f1c79ad8d72c061f8e6dd
r33  75804  17ccd5af6f53c5e5ffa3a9da8e3a26ebbbb18215b3b884d1c9fe6fe28f4ea10b
```

## 2. Class table (my adjudication; each row cited to bytes)

Class definitions I hold the instrument to:

- **adopted** — a guard entry point is actually invoked on the receipt-write
  path, before the write, in a branch reachable without `--check`.
- **unguarded** — the runner writes its own `validation.json` and no such call exists.
- **could-not-evaluate** — the runner's write path cannot be resolved confidently.
  Never a guessed class.

| round | class | self-receipt write | guard invocation site(s) |
|---|---|---|---|
| r5 | unguarded | `:194` `(HERE / "validation.json").write_text(...)` | — |
| r6 | unguarded | `:336` | — |
| r7 | unguarded | `:1171` | — (`guard_positive_and_selftest` `:1111`, `guard_foreign_cwd_no_writes` `:1120` are claim-O battery fixtures, not receipt guards) |
| r8 | unguarded | `:1486` (`OUTPUT_REL` `:99`) | — |
| r9 | unguarded | `:1910` (`OUTPUT_REL` `:127`) | — |
| r10 | unguarded | `:1054` (`OUTPUT_REL` `:60`) | — |
| r11 | unguarded | `:1740` (`OUTPUT_REL` `:125`) | — |
| r12 | unguarded | `:1071` (`out`, path from `OUTPUT` `:18`) | — |
| r14 | adopted | `:717` | `guard_preflight()` `:708`, `:716`; wrapper loads guard via importlib `:413-420` |
| r15 | adopted | `:1346` | `:1337`, `:1345`; wrapper `:1038` |
| r16 | adopted | `:1265` | `:1256`, `:1264`; wrapper `:999` |
| r17 | adopted | `:1431` | `:1422`, `:1430`; wrapper `:1118` |
| r18 | adopted | `:1851` | `:1842`, `:1850`; wrapper `:1512` |
| r19 | unguarded | `:21`, **embedded in a triple-quoted `-c` program** (`:5`-`:23`) | — |
| r20 | adopted | `:1485` | `guard_preflight()` `:1484` (pre-write only); wrapper `:1278-1290` |
| r21 | unguarded | `:1115` (`OUTPUT` `:20`) | — (`env["REFRESH_RECEIPTS"] = "1"` `:474` is set for **isolated clone runs of historical runners**, not for its own write) |
| r22 | adopted | `:922` | `:911` (pre-measure), `:921` (pre-write); wrapper `:827-829` |
| r23 | adopted | `:1097` | `:1094`; wrapper `:1064-1066` (runpy) |
| r24 | adopted | `:1184` | `:1181`; wrapper `:1151` |
| r25 | adopted | `:1145` | `:1142`; wrapper `:1108` |
| r26 | adopted | `:1909` | `:1906`; wrapper `:1855-1857` (runpy) |
| r27 | adopted | `:1907` | `:1904`; wrapper `:1853` |
| r28 | adopted | `:2098` | `:2095`; wrapper `:1996` |
| r29 | unguarded | `:922` | — (`protection_guard` `:779` is a `git status`/`git diff` filed-tree check, def `:629-641`, not a receipt guard) |
| r30 | adopted | `:923` | `:903` (pre-measure), `:922`; wrapper `:883` |
| r31 | adopted | `:1159` | `:1139` (pre-measure), `:1158`; wrapper `:1118` |
| r32 | adopted | `:1143` | `:1123` (pre-measure), `:1142`; wrapper `:1102-1104` |
| r33 | adopted | `:1471` | `:1459` (pre-measure), `:1470`; wrapper `:1441` |

Totals: **17 adopted** (r14-r18, r20, r22-r28, r30-r33), **11 unguarded**
(r5-r12, r19, r21, r29), 0 could-not-evaluate. 17 + 11 = 28 = the filed runner
count. Two-guard variant (pre-measure + pre-write): 10 runners (r14-r18, r22,
r30-r33). Pre-write-only variant: 7 (r20, r23-r28). An inventory that does not
record this variant loses real information about the adopted set.

## 3. Taxonomy soundness — the traps, with my own false negative on record

**(a) Two spellings of the same adoption.** r14-r18 and r20 wrap the guard as
`guard_preflight()`, loading `tools/harness/receipt_guard.py` through
`importlib.util.spec_from_file_location` (r14:414, r15:1038, r16:999, r17:1118,
r18:1512, r20:1279) and calling `module.guard_receipt(ROOT / OUTPUT, repo_root=ROOT)`
(r14:420, r20:1285). r22-r33 wrap it as a local `guard_receipt()` that calls
`runpy.run_path("tools/harness/receipt_guard.py")` and then
`namespace["guard_receipt"](OUTPUT, repo_root=ROOT)` (r23:1064-1066, r26:1855-1857,
r32:1102-1104). My **first** probe keyed on the call spelling `guard_receipt()`
and returned only 11 adopted, silently mis-classifying the six `guard_preflight`
runners as unguarded. That is a false-negative of exactly the class the
instrument must not make; the corrected probe (AST walk resolving any callee
whose body reaches the guard's `guard_receipt` entry point) returns 17. Recorded
here as calibration evidence, not hidden.

**(b) Shape without the call.** `reports/round-29/run-validation.py:919-922` is
byte-comparable to the adopted template's publish tail —
`if args.check: print(...)` / `else: safe_path(OUTPUT).write_text(rendered, ...)` —
with the guard call **omitted**. Any classifier that recognises adoption by the
`--check`/`safe_path(OUTPUT)` shape greens r29; it must be red.

**(c) Write invisible to AST.** `reports/round-19/run-validation.py:21` is the only
self-receipt write in that file and it lives inside the triple-quoted program
passed to `subprocess.run([sys.executable, "-c", """..."""])` (`:5`-`:23`). My AST
pass counted **0** `write_text` calls in r19; a text scan of all string constants
counts 1. An AST-only detector returns r19 "clean".

**(d) Literal-path coverage is 10/28.** The literal string
`reports/round-N/validation.json` appears in only 10 runners (r7-r11, r17, r19,
r20, r33). r5/r6 build `HERE / "validation.json"`; r8-r11 write through
`OUTPUT_REL`; r12/r21/r26/r29 write through
`OUTPUT = f"{ROUND_DIR}/validation.json"`. A literal-grep inventory misses 18 of 28.

**(e) Over-collection.** r5 contains 4 `write_text` calls and 1 `write_bytes`
(`:134`, `:136`, `:152`, `:194`, plus `write_bytes` at `:135`; the first four are
fixture/tamper controls); r18 contains 11 `write_text` calls, 10 of them controls
(`:275`, `:410`, `:817`, `:835`, `:854`, `:1798`, `:1800`, `:1802`, `:1804`,
`:1807`). A detector that reports "any write" as an in-place receipt write falsely
flags control scaffolding. Only
the write whose target resolves to the runner's own `reports/round-N/validation.json`
is the hazard.

**(f) Adoption is a code property, not a receipt-existence property.**
`reports/round-22/validation.json` is **absent** from HEAD (verified
`git cat-file -e HEAD:reports/round-22/validation.json` fails; every other
runner's receipt is present). r22's guard is still adopted and still correct for
the first-publication case. Classifying by "receipt committed in HEAD → hazard"
would flip r22's meaning as soon as it is filed.

**(g) Guard wrapper semantics are faithful in both spellings.** The wrappers call
the guard's `guard_receipt` (receipt_guard.py:152-158), which raises
`SystemExit(3)`; the `except Exception` in r14:421 and r20:1286 does not intercept
`SystemExit` (it derives from `BaseException`), and r20 re-raises `SystemExit(3)`
explicitly at `:1289`. The `if not args.check:` order in r22:910-911 / r32:1122-1123
means `--check` runs (the mode used by the gate battery) never invoke the guard and
never write — correct, and the instrument must not read the `--check` early-return
as an unreachable-guard defect.

## 4. Claim-premise falsification (one hit)

The claim's `before` says: *"r26 carries the same hazard (`:90`, `:1909`)"*
(inherited from the LOG.md F-C13-1 record, `LOG.md:3548` ff., which cites
`reports/round-26/run-validation.py:90` and `:1909`).

- `:90` is `OUTPUT = f"{ROUND_DIR}/validation.json"` — a path constant, not a write.
- `:1909` is `safe_path(OUTPUT).write_text(rendered, encoding="utf-8")` inside the
  `else` branch at `:1904`, **immediately preceded** by `guard_receipt()` at
  `:1906` (wrapper def `:1855-1857`).
- `reports/round-26/validation.json` **is** in HEAD, so that guard call refuses
  the in-place rewrite with exit 3 unless `REFRESH_RECEIPTS=1` — the r5/r6/r7
  clobber is not available to r26 through its runner.

So r26 belongs in **adopted**, not in the hazard set. If the landed inventory
carries r26 as an unguarded/hazard row it is wrong, and the routing receipt would
route r26 to isolated-copy-only for no reason. The LOG's own supersession note
gives r26 a *different* exposure — the stale lessons-README pin
(`README_BASELINE_BLOB = a3187055…`, r26:97) that makes a re-run go **red** — and
that is a staleness class, to be recorded in its own field, never merged into the
clobber class.

The other three named hazards verify exactly: r5:194, r6:336, r7:1171 are
unguarded self-writes (`LOG.md:3556-3558`), and all three receipts are in HEAD.

## 5. Inventory completeness

- Claim-named hazards: 4 (r5, r6, r7, r26) → **3 verified, 1 falsified** (§4).
- The instrument's `after_required` demands "the inventory JSON names every
  `reports/round-*/run-validation.py` with its adoption class". My census supplies
  the expected row set: 28 rows, 17 adopted / 11 unguarded, with the write site and
  guard sites above. Diff the landed JSON against §2 row-for-row.
- The unguarded set is **11**, not 3. r8-r12, r19, r21, r29 are one in-tree
  invocation away from the same breach the round-33 incident recorded; the routing
  draft must cover all 11, not the four named rows.
- Additional surface checked so the instrument's scope is honest:
  `reports/round-6/check-checkpoint.py:117` writes `checkpoint-validation.json` —
  a differently-named artifact, **not** a filed receipt; it must not be flagged.
  `reports/round-30/verify-operability.py` (`:233`, `:257`, `:339`, `:348`, `:465`,
  `:467`), `reports/round-31/sweep-audit.py` (`:259`, `:285`) and
  `reports/round-32/sweep-audit.py` (`:397`, `:445`) write only inside their own
  round directories under names other than `validation.json`; no `tools/**` writer
  of any `validation.json` exists (`grep -rn "validation\.json" tools/ --include=*.py`
  filtered for write/dump/replace → empty). The 28 runners are the whole in-tree
  receipt-write surface.

## 6. Falsification checklist for the landed instrument

Each item is a control the instrument must pass; expected answer and the byte
evidence I will re-check are given. Any wrong answer is a defect, not a nuance.

1. r32 → adopted (r32:1123, :1142, :1143). Baseline positive.
2. r14 → adopted (r14:708, :716, :717) — **wrapper spelling**. A classifier that
   only knows `guard_receipt()` fails here.
3. r20 → adopted, and recorded as pre-write-only (r20:1484, :1485).
4. r29 → unguarded (r29:922) despite the adopted-shape tail at :919-922.
5. r19 → unguarded (r19:21, embedded program) — an AST-only detector fails here.
6. r26 → adopted (r26:1906, :1909); the instrument must **not** reproduce the
   filed LOG's r26 hazard expectation.
7. r5 → unguarded with the write cited at `:194`, not at its other 4 write_text
   sites (`:134`, `:136`, `:152`).
8. r22 → adopted although `reports/round-22/validation.json` is absent from HEAD.
9. `reports/round-6/check-checkpoint.py` → absent from the inventory; its
   `checkpoint-validation.json` write is not a filed-receipt write.
10. Denominators reported as counts, not ratios over round directories: runners
    found 28/28, round directories 30, rounds without runners named (r13, r34).

Selftest-spec defect to fix before the bytes land: the claim's declared controls
make the "positive" (r32 recognised adopted) and the first "negative" (a guarded
runner not flagged) the **same object**. The control set needs at least one
positive from each spelling family (r32 for the runpy/`guard_receipt` family, r14
or r20 for the importlib/`guard_preflight` family) plus the r29 shape-control, the
r19 embedded-write control, and the r26 counter-expectation control. A selftest
built only from one spelling family can be all-green while the instrument is
wrong on six field runners — which is the exact failure mode §3(a) documents.

## 7. Verdicts available to me now

- Census and taxonomy evidence: **complete** (28/28 runners, digest-pinned, byte-cited).
- Claim premise "known hazards r5/r6/r7 + r26": **harmed** — r26 is a false hazard;
  the true unguarded set is 11 and the claim understates it by 8.
- Instrument correctness, selftest adequacy, routing coverage: **could-not-evaluate**
  (bytes absent) — recorded as owed, with §6 as the acceptance test and §2 as the
  expected inventory.
- No axis verdict is offered here; per REGIMEN.md the round's axes are judged on
  the delivered revision, and the delivered revision for claim O does not exist yet.

## Owed

- `reports/round-34/op/O01-impl.md`, `O02-tool-source.md`, `O03-selftest.md`,
  `O04-predicted-inventory.md`, `O05-routing.md`, `O06-scribe.md` — absent at
  review time.
- `reports/round-34/op/O07-verify-tool.md`, `O08-traps.md`, `O09-verify-routing.md`,
  `O10-final-receipt.md` — absent at review time.
- `reports/round-34/plan/P02-oc-plan.md`, `reports/round-34/scout/K03-guard-pattern.md`
  — absent at review time.
- `tools/harness/receipt_guard_adoption.py` + its inventory JSON — integrator-applied;
  §6 is the acceptance test, §2 the expected rows.
- Re-review of the instrument bytes against §6 (§3(a) fail mode included) is owed to
  the integrator once O02's source lands; my instrument-byte verdict is
  could-not-evaluate, not green.

## Citations

- `reports/round-34/claims.json` (claim O `before`/`after_required`/`thresholds`,
  `non_goals`), `reports/round-34/targets.json` (seat R04; O-seat out paths).
- `REGIMEN.md` (per-round contract; land-and-measure-on-delivered-revision rule).
- `LOG.md:3548` ff., hazard lines `LOG.md:3556-3558` (F-C13-1 record).
- `tools/harness/receipt_guard.py:152-158`, `:161-168` (guard entry points),
  `:36` (`TOOL` constant).
- `reports/round-5/run-validation.py:194`; `reports/round-6/run-validation.py:336`;
  `reports/round-7/run-validation.py:1111`, `:1120`, `:1171`;
  `reports/round-8/run-validation.py:99`, `:1485-1486`;
  `reports/round-9/run-validation.py:127`, `:1909-1910`;
  `reports/round-10/run-validation.py:60`, `:1053-1054`;
  `reports/round-11/run-validation.py:125`, `:1738-1740`;
  `reports/round-12/run-validation.py:18`, `:1069-1071`.
- `reports/round-14/run-validation.py:25`, `:413-425`, `:708`, `:716-717`;
  `reports/round-15/run-validation.py:44`, `:1038`, `:1337`, `:1345-1346`;
  `reports/round-16/run-validation.py:57`, `:999`, `:1256`, `:1264-1265`;
  `reports/round-17/run-validation.py:68`, `:1118`, `:1422`, `:1430-1431`;
  `reports/round-18/run-validation.py:67`, `:1512`, `:1842`, `:1850-1851`;
  `reports/round-20/run-validation.py:57`, `:1278-1290`, `:1484-1485`.
- `reports/round-19/run-validation.py:5-23`, `:21`.
- `reports/round-21/run-validation.py:20`, `:474`, `:1113-1115`.
- `reports/round-22/run-validation.py:827-829`, `:910-911`, `:921-922`;
  `reports/round-23/run-validation.py:1064-1066`, `:1093-1097`;
  `reports/round-24/run-validation.py:1151`, `:1181-1184`;
  `reports/round-25/run-validation.py:1108`, `:1142-1145`;
  `reports/round-26/run-validation.py:90`, `:97`, `:1855-1857`, `:1902-1909`;
  `reports/round-27/run-validation.py:1853`, `:1904-1907`;
  `reports/round-28/run-validation.py:1996`, `:2095-2098`.
- `reports/round-29/run-validation.py:23`, `:27-29`, `:629-641`, `:779`, `:919-922`.
- `reports/round-30/run-validation.py:883`, `:903`, `:922-923`;
  `reports/round-31/run-validation.py:1118`, `:1139`, `:1158-1159`;
  `reports/round-32/run-validation.py:1102-1104`, `:1122-1123`, `:1142-1143`;
  `reports/round-33/run-validation.py:1441`, `:1459`, `:1470-1471`.
- `reports/round-6/check-checkpoint.py:117`;
  `reports/round-30/verify-operability.py:233,257,339,348,465,467`;
  `reports/round-31/sweep-audit.py:259,285`; `reports/round-32/sweep-audit.py:397,445`.
- Commands run (read-only): `git ls-files 'reports/round-*/run-validation.py' | wc -l`;
  `ls -d reports/round-*/ | wc -l`; `git status --porcelain`;
  `git cat-file -e HEAD:reports/round-<N>/validation.json` for n=5..33 except 13;
  `python3 -B` AST/regex census over the 28 runners (byte counts + sha256);
  `grep -rn "validation\.json" tools/ --include=*.py` (write-filtered) → empty;
  `python3 -B` string-constant scan for embedded `write_text` (r19 → 1);
  digest self-check of this fragment's 28 census rows against live bytes
  (28/28 matched, 0 mismatches).
  No `reports/round-*/run-validation.py` was executed (F-C13-1 rule). Durable
  writes by this seat: `reports/round-34/review/R04-o-review.md` only; one
  transient scratch census dump at `.scratch/r04-census-raw.json`.
