- Seat: O04 | executor | claim O | date 2026-10-19 | baseline da68a6d

Predicted inventory for `tools/harness/receipt_guard_adoption.py` (claim O). Produced by
my own read-only analysis of the filed runner bytes; the landed tool must reproduce
this content (label strings may be renamed by O01/O02 — the required content is the
per-runner `receipt_write.in_place` / `guard.adopted` booleans and the derived class).

## Method

- Census (AST + grep via `python3 - <<'PY'` heredocs, no files written outside this
  fragment): every `reports/round-*/run-validation.py` (28 files), per file:
  write-call scan (`write_text`/`write_bytes`/`json.dump`/`os.replace`/`rename`/`copy*`)
  resolving local aliases of the round's own receipt path, plus a scan of embedded
  script string constants (needed for round-19); guard scan for calls to
  `guard_receipt()`/`round_runner_main()`/`guard_preflight()` and for the
  `receipt_guard.py` load site (`importlib.util.spec_from_file_location` or
  `runpy.run_path`).
- Runner set: rounds 5–12, 14–33; rounds 1–4 and 13 carry no runner
  (`ls reports/round-*/run-validation.py | wc -l` → 28).
- Filed receipts: 27; `reports/round-22/validation.json` does not exist and has never
  been committed (`git log --all -- reports/round-22/validation.json` → empty output).
- Working tree at `da68a6d` is clean on the F-C13-1 paths
  (`git status --short reports/round-5/validation.json reports/round-6/validation.json reports/round-7/validation.json reports/round-22/ reports/round-26/` → empty).

## Predicted inventory JSON

Predicted schema (top-level): `tool`, `baseline_commit`, `census_command`, `counts`,
`runners[]`, `known_hazards[]`. Per runner: `round`, `path`, `sha256` (classified bytes),
`receipt_write {in_place, sites[{line, expr}]}`, `guard {adopted, mechanism, load_site,
call_sites, pre_publish_call_site}`, `class`, `hazard`.

Class vocabulary (predicted): `guarded-in-place-write` (adopted guard + in-place receipt
write), `unguarded-in-place-write` (hazard), `no-receipt-write` (clean),
`not-a-runner` (out of census scope; selftest fixture only).

```json
{
  "tool": "tools/harness/receipt_guard_adoption.py",
  "baseline_commit": "da68a6d",
  "census_command": "grep -l 'validation.json' reports/round-*/run-validation.py",
  "counts": {"runners": 28, "guarded_in_place": 17, "unguarded_in_place": 11,
             "no_receipt_write": 0, "not_a_runner": 0},
  "runners": [
    {"round": 5,  "path": "reports/round-5/run-validation.py",  "sha256": "5fd5cb4198bdf1d01240ef13fbf6f59ae5ae18182c9afd0d865b619292f83676", "receipt_write": {"in_place": true, "sites": [{"line": 194, "expr": "HERE / 'validation.json'"}]}, "guard": {"adopted": false, "mechanism": null, "load_site": null, "call_sites": [], "pre_publish_call_site": null}, "class": "unguarded-in-place-write", "hazard": true},
    {"round": 6,  "path": "reports/round-6/run-validation.py",  "sha256": "c53f100927b8723bea25eeaa06048ace68fdfa3e763811a64e1104323e535c6e", "receipt_write": {"in_place": true, "sites": [{"line": 336, "expr": "HERE / 'validation.json'"}]}, "guard": {"adopted": false, "mechanism": null, "load_site": null, "call_sites": [], "pre_publish_call_site": null}, "class": "unguarded-in-place-write", "hazard": true},
    {"round": 7,  "path": "reports/round-7/run-validation.py",  "sha256": "c3b8418445d03bee2ba394ab6e4e4767e5ef07168c1a70dc904b3813e878c1e7", "receipt_write": {"in_place": true, "sites": [{"line": 1171, "expr": "HERE / 'validation.json'"}]}, "guard": {"adopted": false, "mechanism": null, "load_site": null, "call_sites": [], "pre_publish_call_site": null}, "class": "unguarded-in-place-write", "hazard": true},
    {"round": 8,  "path": "reports/round-8/run-validation.py",  "sha256": "7eaa36789b4d71ce94ffadc93d2f5e10d6e0ca353df1c233d0ba94f29bff8369", "receipt_write": {"in_place": true, "sites": [{"line": 1486, "expr": "output = ROOT / OUTPUT_REL; output.write_text(...)"}]}, "guard": {"adopted": false, "mechanism": null, "load_site": null, "call_sites": [], "pre_publish_call_site": null}, "class": "unguarded-in-place-write", "hazard": true},
    {"round": 9,  "path": "reports/round-9/run-validation.py",  "sha256": "8e4881309afaacc96f8f6e68f0c31041a9b2accc1c26bb1b20403f563364f5dd", "receipt_write": {"in_place": true, "sites": [{"line": 1910, "expr": "output = ROOT / OUTPUT_REL; output.write_text(...)"}]}, "guard": {"adopted": false, "mechanism": null, "load_site": null, "call_sites": [], "pre_publish_call_site": null}, "class": "unguarded-in-place-write", "hazard": true},
    {"round": 10, "path": "reports/round-10/run-validation.py", "sha256": "23d6dc09002fe18c46778ac57d2c34246ab970a9371e7382950ca737d4019b0e", "receipt_write": {"in_place": true, "sites": [{"line": 1054, "expr": "output = ROOT / OUTPUT_REL; output.write_text(...)"}]}, "guard": {"adopted": false, "mechanism": null, "load_site": null, "call_sites": [], "pre_publish_call_site": null}, "class": "unguarded-in-place-write", "hazard": true},
    {"round": 11, "path": "reports/round-11/run-validation.py", "sha256": "fab68287e74abc62d0681a1389bd0450d90020b65d7896ba2ab679e195acd9bd", "receipt_write": {"in_place": true, "sites": [{"line": 1740, "expr": "output = ROOT / OUTPUT_REL; output.write_text(...)"}]}, "guard": {"adopted": false, "mechanism": null, "load_site": null, "call_sites": [], "pre_publish_call_site": null}, "class": "unguarded-in-place-write", "hazard": true},
    {"round": 12, "path": "reports/round-12/run-validation.py", "sha256": "2831c95c232c057361404c1860b82e88088b19c94b3ae26ec36be9e46fc6563c", "receipt_write": {"in_place": true, "sites": [{"line": 1071, "expr": "out = ROOT / OUTPUT; out.write_text(...)"}]}, "guard": {"adopted": false, "mechanism": null, "load_site": null, "call_sites": [], "pre_publish_call_site": null}, "class": "unguarded-in-place-write", "hazard": true},
    {"round": 14, "path": "reports/round-14/run-validation.py", "sha256": "b06bf6b12cf87377c52d245e6b1da413aab2ab17620d98dd7bc2a6ce467273b8", "receipt_write": {"in_place": true, "sites": [{"line": 717, "expr": "ROOT / OUTPUT"}]}, "guard": {"adopted": true, "mechanism": "importlib.util.spec_from_file_location(:414) + module.guard_receipt(:420)", "load_site": 414, "call_sites": [420, 708, 716], "pre_publish_call_site": 716}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 15, "path": "reports/round-15/run-validation.py", "sha256": "5323a8d36ada8addcbcba90e1a874e118bb7099720c345cd4974c7bed7418b67", "receipt_write": {"in_place": true, "sites": [{"line": 1346, "expr": "ROOT / OUTPUT"}]}, "guard": {"adopted": true, "mechanism": "importlib.util.spec_from_file_location(:1038) + module.guard_receipt(:1044)", "load_site": 1038, "call_sites": [1044, 1337, 1345], "pre_publish_call_site": 1345}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 16, "path": "reports/round-16/run-validation.py", "sha256": "295629ae128347b854759bda9d1e41b0497bc2c269267ac920146f6b5aa891d6", "receipt_write": {"in_place": true, "sites": [{"line": 1265, "expr": "ROOT / OUTPUT"}]}, "guard": {"adopted": true, "mechanism": "importlib.util.spec_from_file_location(:999) + module.guard_receipt(:1005)", "load_site": 999, "call_sites": [1005, 1256, 1264], "pre_publish_call_site": 1264}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 17, "path": "reports/round-17/run-validation.py", "sha256": "6b98abadef9951be7cfce006f339dad036f7b341cee6713ecc00be6e5f9095ec", "receipt_write": {"in_place": true, "sites": [{"line": 1431, "expr": "ROOT / OUTPUT"}]}, "guard": {"adopted": true, "mechanism": "importlib.util.spec_from_file_location(:1118) + module.guard_receipt(:1124)", "load_site": 1118, "call_sites": [1124, 1422, 1430], "pre_publish_call_site": 1430}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 18, "path": "reports/round-18/run-validation.py", "sha256": "01b138500ce30ad25cc8f0078110d6b2afeb9bf8ca79f5903deae3746c19bca8", "receipt_write": {"in_place": true, "sites": [{"line": 1851, "expr": "ROOT / OUTPUT"}]}, "guard": {"adopted": true, "mechanism": "importlib.util.spec_from_file_location(:1512) + module.guard_receipt(:1518)", "load_site": 1512, "call_sites": [1518, 1842, 1850], "pre_publish_call_site": 1850}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 19, "path": "reports/round-19/run-validation.py", "sha256": "5b27a80de1f4b11012061e7ed3e835734049661ace295b39878afd9f71454d3a", "receipt_write": {"in_place": true, "sites": [{"line": "embedded:17 (file line 21)", "expr": "pathlib.Path('reports/round-19/validation.json').write_text(...) inside the -c script string"}]}, "guard": {"adopted": false, "mechanism": null, "load_site": null, "call_sites": [], "pre_publish_call_site": null}, "class": "unguarded-in-place-write", "hazard": true},
    {"round": 20, "path": "reports/round-20/run-validation.py", "sha256": "2b7a252b5449415dddac2e667ed2e192df800a80173849989fa72423961646da", "receipt_write": {"in_place": true, "sites": [{"line": 1485, "expr": "ROOT / OUTPUT"}]}, "guard": {"adopted": true, "mechanism": "importlib.util.spec_from_file_location(:1279) + module.guard_receipt(:1285)", "load_site": 1279, "call_sites": [1285, 1484], "pre_publish_call_site": 1484}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 21, "path": "reports/round-21/run-validation.py", "sha256": "938cddeed86dedf52a4904c9c6a81248d6dc719c1330d4f3b64bcd8f3be896b0", "receipt_write": {"in_place": true, "sites": [{"line": 1115, "expr": "output = ROOT / OUTPUT; output.write_text(...)"}]}, "guard": {"adopted": false, "mechanism": null, "load_site": null, "call_sites": [], "pre_publish_call_site": null, "refresh_env_note": "REFRESH_RECEIPTS=1 set at :474 only for historical runners executed in .scratch clones; :472 rewrites the clone's runner bytes, not filed bytes"}, "class": "unguarded-in-place-write", "hazard": true},
    {"round": 22, "path": "reports/round-22/run-validation.py", "sha256": "3af74c2b40f007c21581b037c9059512bd745d4fe8645dd9e4364818a4e463dd", "receipt_write": {"in_place": true, "sites": [{"line": 922, "expr": "safe_path(OUTPUT)"}]}, "guard": {"adopted": true, "mechanism": "runpy.run_path(:828) + namespace['guard_receipt'](OUTPUT)(:829)", "load_site": 828, "call_sites": [911, 921], "pre_publish_call_site": 921}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 23, "path": "reports/round-23/run-validation.py", "sha256": "ae897cb8d808f0c1432948154d440f9c86730685b32b91442d9714dc27692cb2", "receipt_write": {"in_place": true, "sites": [{"line": 1097, "expr": "safe_path(OUTPUT)"}]}, "guard": {"adopted": true, "mechanism": "runpy.run_path(:1065) + namespace['guard_receipt'](OUTPUT)(:1066)", "load_site": 1065, "call_sites": [1094], "pre_publish_call_site": 1094}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 24, "path": "reports/round-24/run-validation.py", "sha256": "ba3b18a79e9b0dbbe9fae70b7bc4b27f50d670ff025b1b24cf7f14b1ac6d43ad", "receipt_write": {"in_place": true, "sites": [{"line": 1184, "expr": "safe_path(OUTPUT)"}]}, "guard": {"adopted": true, "mechanism": "runpy.run_path(:1152) + namespace['guard_receipt'](OUTPUT)(:1153)", "load_site": 1152, "call_sites": [1181], "pre_publish_call_site": 1181}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 25, "path": "reports/round-25/run-validation.py", "sha256": "d19435251dccb738e456c01fe7fb94498c27bae7f70704a96f94ec9324ce35af", "receipt_write": {"in_place": true, "sites": [{"line": 1145, "expr": "safe_path(OUTPUT)"}]}, "guard": {"adopted": true, "mechanism": "runpy.run_path(:1109) + namespace['guard_receipt'](OUTPUT)(:1110)", "load_site": 1109, "call_sites": [1142], "pre_publish_call_site": 1142}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 26, "path": "reports/round-26/run-validation.py", "sha256": "73297683d552b1673f2064a1a1ec76bf359f4add1bf8be4411ee77caa7f0be55", "receipt_write": {"in_place": true, "sites": [{"line": 1909, "expr": "safe_path(OUTPUT)"}]}, "guard": {"adopted": true, "mechanism": "runpy.run_path(:1856) + namespace['guard_receipt'](OUTPUT)(:1857)", "load_site": 1856, "call_sites": [1906], "pre_publish_call_site": 1906}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 27, "path": "reports/round-27/run-validation.py", "sha256": "36b597068d59a88156090e5c179e1ab2c68fe4ce7735d7b1bb6f67d82babe08a", "receipt_write": {"in_place": true, "sites": [{"line": 1907, "expr": "safe_path(OUTPUT)"}]}, "guard": {"adopted": true, "mechanism": "runpy.run_path(:1854) + namespace['guard_receipt'](OUTPUT)(:1855)", "load_site": 1854, "call_sites": [1904], "pre_publish_call_site": 1904}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 28, "path": "reports/round-28/run-validation.py", "sha256": "20e09ea8db7bcb306b0c8948c7b8afb62eca5e0d47f674ebfea9643f2f6add77", "receipt_write": {"in_place": true, "sites": [{"line": 2098, "expr": "safe_path(OUTPUT)"}]}, "guard": {"adopted": true, "mechanism": "runpy.run_path(:1997) + namespace['guard_receipt'](OUTPUT)(:1998)", "load_site": 1997, "call_sites": [2095], "pre_publish_call_site": 2095}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 29, "path": "reports/round-29/run-validation.py", "sha256": "59df391b2f80260ddfefe7a72651e1c67062bf376615ba7f21a1dd5bc5cf0ece", "receipt_write": {"in_place": true, "sites": [{"line": 922, "expr": "safe_path(OUTPUT)"}]}, "guard": {"adopted": false, "mechanism": null, "load_site": null, "call_sites": [], "pre_publish_call_site": null}, "class": "unguarded-in-place-write", "hazard": true},
    {"round": 30, "path": "reports/round-30/run-validation.py", "sha256": "2f447223ece3f48195bf4c2d7f026b37b2e5cc88924c002408f8bd663e7a3e31", "receipt_write": {"in_place": true, "sites": [{"line": 923, "expr": "safe_path(OUTPUT)"}]}, "guard": {"adopted": true, "mechanism": "runpy.run_path(:884) + namespace['guard_receipt'](OUTPUT)(:885)", "load_site": 884, "call_sites": [903, 922], "pre_publish_call_site": 922}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 31, "path": "reports/round-31/run-validation.py", "sha256": "9e01c4274c1afc0be983ba3c7610fc44212ab2d3e934f747b57ef6b9584488dc", "receipt_write": {"in_place": true, "sites": [{"line": 1159, "expr": "safe_path(OUTPUT)"}]}, "guard": {"adopted": true, "mechanism": "runpy.run_path(:1119) + namespace['guard_receipt'](OUTPUT)(:1120)", "load_site": 1119, "call_sites": [1139, 1158], "pre_publish_call_site": 1158}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 32, "path": "reports/round-32/run-validation.py", "sha256": "6fd1b96e682fde67e85f52c01573c175ac047b014f9f1c79ad8d72c061f8e6dd", "receipt_write": {"in_place": true, "sites": [{"line": 1143, "expr": "safe_path(OUTPUT)"}]}, "guard": {"adopted": true, "mechanism": "runpy.run_path(:1103) + namespace['guard_receipt'](OUTPUT)(:1104)", "load_site": 1103, "call_sites": [1123, 1142], "pre_publish_call_site": 1142}, "class": "guarded-in-place-write", "hazard": false},
    {"round": 33, "path": "reports/round-33/run-validation.py", "sha256": "17ccd5af6f53c5e5ffa3a9da8e3a26ebbbb18215b3b884d1c9fe6fe28f4ea10b", "receipt_write": {"in_place": true, "sites": [{"line": 1471, "expr": "safe_path(OUTPUT)"}]}, "guard": {"adopted": true, "mechanism": "runpy.run_path(:1442) + namespace['guard_receipt'](OUTPUT)(:1443)", "load_site": 1442, "call_sites": [1459, 1470], "pre_publish_call_site": 1470}, "class": "guarded-in-place-write", "hazard": false}
  ],
  "known_hazards": [
    {"round": 5,  "claimed": "claims.json:41 hazard list", "measured_class": "unguarded-in-place-write", "agrees": true},
    {"round": 6,  "claimed": "claims.json:41 hazard list", "measured_class": "unguarded-in-place-write", "agrees": true},
    {"round": 7,  "claimed": "claims.json:41 hazard list", "measured_class": "unguarded-in-place-write", "agrees": true},
    {"round": 26, "claimed": "claims.json:41,:43 + LOG.md:3559-3560 ('same hazard', ':90',':1909')", "measured_class": "guarded-in-place-write", "agrees": false}
  ]
}
```

## Assertions the landed tool must reproduce

1. 28 runners: 17 `guarded-in-place-write`, 11 `unguarded-in-place-write`,
   0 `no-receipt-write` on live bytes (the clean class exists only as an O03 fixture).
2. Every guarded runner calls the guard on the default publish path at the line
   immediately above its receipt write (max gap 1 line): r14 :716/:717, r15
   :1345/:1346, r16 :1264/:1265, r17 :1430/:1431, r18 :1850/:1851, r20 :1484/:1485,
   r22 :921/:922, r23 :1094/:1097, r24 :1181/:1184, r25 :1142/:1145, r26 :1906/:1909,
   r27 :1904/:1907, r28 :2095/:2098, r30 :922/:923, r31 :1158/:1159, r32 :1142/:1143,
   r33 :1470/:1471. r22/r30/r31/r32/r33 add a second, pre-flight call under
   `if not args.check`; r23–r28 wrap the call in `try/except SystemExit`.
3. 27 filed receipts; `reports/round-22/validation.json` is absent and has never been
   committed, although the r22 runner would write it (`git log --all` → empty;
   `reports/round-22/run-validation.py:922`).
4. Worktree clean at `da68a6d` on the F-C13-1 surfaces.

## Contested reading (reported, not absorbed)

`reports/round-34/claims.json:41,:43` and `LOG.md:3559-3560` state that r26 "carries
the same hazard (:90, :1909)". The bytes do not support the hazard reading:
`reports/round-26/run-validation.py:1856` loads `tools/harness/receipt_guard.py`,
`:1906` calls `guard_receipt()` inside `try/except SystemExit` on the publish path, and
only then `:1909` writes the receipt. `:90` is merely the `OUTPUT` constant
(`reports/round-26/run-validation.py:90`). Measured class: `guarded-in-place-write`,
`hazard: false`; routing for r26 belongs to the guarded refresh protocol, not
isolated-copy-only. One of the two readings must win: either the filed LOG record is
corrected by a new supersession row, or my classification is wrong and the verifiers
must show why. This seat reports the discrepancy rather than editing the claim or the
filed LOG.

## Detection requirements and trap predictions (for O07/O08)

- r19's receipt write lives inside the `-c` script string at file line 21 (embedded
  line 17), not in the outer file's AST as a direct write. Predicted class:
  `unguarded-in-place-write`. A tool that misses it may not report it `no-receipt-write`
  (false negative → a missing hazard row); either scan embedded script text or record
  `could-not-evaluate` for r19.
- r21 sets `REFRESH_RECEIPTS=1` at :474, but only for historical runners executed in
  `.scratch` clones; its own receipt write at :1115 is unguarded. The tool must not read
  the mere presence of the REFRESH token as adoption. r14's `REFRESH_RECEIPTS`
  occurrences (:439, :445) are audit text checks, not adoption either.
- Trap predictions: (a) guard imported but never called →
  `unguarded-in-place-write`, with `load_site` set and `call_sites` empty;
  (b) guard called only under a flag (e.g. `--refresh`) → `unguarded-in-place-write`
  for the default publish path, `adopted: false`, with the conditional call recorded
  (live anchor for the correct pattern: the pre-publish call is unconditional in the
  `else:` branch of every guarded runner); (c) receipt write via
  `os.replace(tmp, OUT)` → `in_place: true`, class follows guard presence; zero live
  runners use `replace`/`rename` on a receipt path (grep-verified), so this leg has
  fixture-only coverage and must never return clean when undetectable.
- False-positive controls available from live bytes (must not be flagged as receipt
  writes): `reports/round-21/run-validation.py:845` (`.scratch` claims file),
  `reports/round-21/run-validation.py:472` (clone runner bytes),
  `reports/round-26/run-validation.py:831,:842` (fixture packets),
  `reports/round-8/run-validation.py:1230` (write inside an isolated copy).
- Cross-round references are reads only: `reports/round-6/run-validation.py:283` (r5's
  runner executed inside a disposable copy), `reports/round-7/run-validation.py:1016`,
  `reports/round-12/run-validation.py:463,:860`, `reports/round-24/run-validation.py:1051`.
  No runner writes another round's receipt; no `os.replace`/`rename` targets a receipt
  path in any of the 28 files.

## Owed

- `## Owed: none` for my own deliverable. Dependency note: `op/O01-impl.md`,
  `op/O02-tool-source.md`, `scout/K03-guard-pattern.md`, and `plan/P02-oc-plan.md` did
  not exist at write time, so my schema/label vocabulary is a prediction, not a
  reconciliation with theirs. O07 should compare the landed tool's `--json` against
  this fragment row-for-row on `receipt_write.in_place`, `guard.adopted`, `class`,
  `hazard`, and the `known_hazards` r26 divergence.

## Citations

- `reports/round-34/claims.json:41,:43,:45,:51` (claim O mission, hazard list, thresholds)
- `reports/round-34/targets.json:47` (seat O04)
- `REGIMEN.md` per-round contract; `AGENTS.md` operating rules
- `LOG.md:3548-3564` (F-C13-1 incident record, r26 sentence at :3559-3560)
- `tools/harness/receipt_guard.py:35` (`REFRESH_ENV = "REFRESH_RECEIPTS"`), `:144-149`
  (committed-receipt refusal), `:152-168` (`guard_receipt` / `round_runner_main`)
- Commands: `ls reports/round-*/run-validation.py | wc -l` → 28;
  `ls reports/round-*/validation.json | wc -l` → 27;
  `git log --all -- reports/round-22/validation.json` → empty;
  `git status --short reports/round-5/validation.json reports/round-6/validation.json
  reports/round-7/validation.json reports/round-22/ reports/round-26/` → empty;
  sha256 census over the 28 runner files (digests inline above)
- Per-runner evidence lines cited inline: r5:194; r6:336; r7:1171; r8:99,1486; r9:127,1910;
  r10:60,1054; r11:125,1740; r12:18,1071; r14:414,420,708,716,717; r15:1038,1044,1337,1345,1346;
  r16:999,1005,1256,1264,1265; r17:1118,1124,1422,1430,1431; r18:1512,1518,1842,1850,1851;
  r19:19,21 (embedded lines 15,17); r20:1279,1285,1484,1485; r21:472,474,845,1115;
  r22:828,829,911,921,922; r23:1065,1066,1094,1097; r24:1051,1152,1153,1181,1184;
  r25:1109,1110,1142,1145; r26:90,831,842,1856,1857,1906,1909; r27:1854,1855,1904,1907;
  r28:1997,1998,2095,2098; r29:922; r30:884,885,903,922,923; r31:1119,1120,1139,1158,1159;
  r32:1103,1104,1123,1142,1143; r33:1442,1443,1459,1470,1471
