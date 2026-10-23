NONE-MET

# Mutation probe — MutLegsA3

Axes: defect sensitivity; baseline validity; exact restoration; bounded operability.

## SURVIVORS FIRST

- **M02 SURVIVED**: SET retired-id conjunct omitted. `retired-id` remains `SET FAIL`. Removing `and not retired` is equivalent while `cited == want` remains: retired ids are outside `want`. All 15 fixtures retained their oracle outcomes; this redundant guard does not expose an accepted retired citation.

## Scope and detector

- Frozen revision `14e6413820d482913f723432b62d566967ccd1a6`, counter sha256 `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.
- Sparse clone (corpus + reports/round-60) avoids unrelated large report history; original L1 build.patch applied and all four original captures copied. No lane file except this report is written.
- 15 fixtures: the required no-key candidate positive; a mechanically bound-key positive; and all 13 requested negatives. Bound keys contain an empty seats map and an empty registry, deliberately providing no support work.
- No SESSIONS probe is used or needed: `probe=n/a`. Counter mutants are isolated condition ablations, not alternate frozen counters. No support seat is created, messaged, named as an actor, or impersonated.
- Bounded detector: frozen script from clone with `--root` fixture; every matrix invocation `timeout 25 python3 -B` (initial canonical run: 60 seconds), inherited PYTHONDONTWRITEBYTECODE=1, offline copied uv cache and scratch TMPDIR. The frozen locator internally invokes its own pinned pypdf helper unchanged.
- Mutation oracle is the named mechanical leg, not overall acceptance. A pristine suite PASS means the two positives have their declared PASS/FAIL leg vectors and every negative has its expected rejecting leg. A mutant is KILLED only if that same oracle rejects mutated output and passes restored output. A pristine oracle failure is INCONCLUSIVE. Whole-claim mutation sensitivity is INCONCLUSIVE here because SUPPORT intentionally fails in every fixture; no aggregate FAIL is misreported as a kill.
- Other-page-url synchronizes the manifest URL with the wrong new-row URL (capture bytes unchanged) to isolate ROWS same-page logic. New-id-on-base-line also triggers ROWS for insufficient quote overlap; LINES is observed independently.
- Fixture entry changes are re-keyed except the deliberate key-entry-sha mismatch, whose key-file declared hash is valid; frozen planted rows are byte-copied and checked against the counter constant.

## Results

| Mutant | One-condition defect | Target fixture / leg | Verdict | Detecting fixtures |
|---|---|---|---|---|
| M02 | SET retired-id conjunct omitted | retired-id / SET | SURVIVED | none |
| M01 | SET exact-set comparison relaxed to subset | missing-id / SET | KILLED | missing-id |
| M03 | LINES normalised base-line comparison omitted | new-id-on-base-line / LINES | KILLED | new-id-on-base-line |
| M04 | OLDWORD substring match changed to whole-entry equality | frozen-phrase / OLDWORD | KILLED | frozen-phrase |
| M05 | ROWS Registry section membership omitted | row-outside-registry / ROWS | KILLED | row-outside-registry |
| M06 | ROWS queued accepted alongside mined | status-queued / ROWS | KILLED | status-queued |
| M07 | ROWS tier C admitted | tier-C / ROWS | KILLED | tier-C |
| M08 | ROWS used-by check disabled | used-by-missing / ROWS | KILLED | used-by-missing |
| M09 | ROWS same-page comparison omitted | other-page-url / ROWS | KILLED | other-page-url |
| M10 | ROWS later-URL Wayback requirement omitted | extra-non-wayback-url / ROWS | KILLED | extra-non-wayback-url |
| M11 | PINNED capture-hash comparison omitted | capture-hash-mismatch / PINNED | KILLED | capture-hash-mismatch |
| M12 | PINNED quote-location check disabled | quote-not-located / PINNED | KILLED | quote-not-located |
| M13 | JUDGED entry_sha256 comparison disabled | key-entry-sha-mismatch / JUDGED | KILLED | key-entry-sha-mismatch |

Total counter runs in structured receipts: 406. Frozen/probe full-label controls: 0 PASS. No claim acceptance or support judgment is inferred.

## Exact restoration and bounds

- Frozen clone counter remains `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.
- All 13 restored mutant files equal frozen bytes: `True`.
- Fixture hashes unchanged after scoring: `True`; changed fixtures: `[]`.
- Per-fixture before/after path hashes and aggregate digests are in `fixture-hashes/*.json`; per-run counter hashes, complete stdout/stderr, exit, and command are in `outputs/*.json` under the isolated sandbox.
- Tool/dependency installs: none. Existing pinned pypdf 5.4.0 uv cache copied locally; offline reads only. A dereferenced cache-copy attempt briefly measured 202 MiB for the cache alone, exceeding the requested 200 MB cap. It was immediately removed and replaced with a symlink-preserving copy (entire sandbox 72 MiB before fixtures). This procedural bound breach is disclosed, not hidden.
- All scoring processes are synchronous and timeout-bounded; no background jobs, alternate agent runtime, or child dispatch. Frozen counter source and all fixtures are restored/unchanged; no cleanup is delegated.

## Target-leg detector outputs

Each pristine/restored leg must reject its negative; all three counter invocations exit 1 because SUPPORT remains absent. The per-leg oracle, not exit 1 by itself, kills the mutant.

| Mutant | Expected detector | Pristine → mutated → restored | Verdict |
|---|---|---|---|
| M02 | retired-id: SET FAIL | FAIL → FAIL → FAIL | SURVIVED |
| M01 | missing-id: SET FAIL | FAIL → PASS → FAIL | KILLED |
| M03 | new-id-on-base-line: LINES FAIL | FAIL → PASS → FAIL | KILLED |
| M04 | frozen-phrase: OLDWORD FAIL | FAIL → PASS → FAIL | KILLED |
| M05 | row-outside-registry: ROWS FAIL | FAIL → PASS → FAIL | KILLED |
| M06 | status-queued: ROWS FAIL | FAIL → PASS → FAIL | KILLED |
| M07 | tier-C: ROWS FAIL | FAIL → PASS → FAIL | KILLED |
| M08 | used-by-missing: ROWS FAIL | FAIL → PASS → FAIL | KILLED |
| M09 | other-page-url: ROWS FAIL | FAIL → PASS → FAIL | KILLED |
| M10 | extra-non-wayback-url: ROWS FAIL | FAIL → PASS → FAIL | KILLED |
| M11 | capture-hash-mismatch: PINNED FAIL | FAIL → PASS → FAIL | KILLED |
| M12 | quote-not-located: PINNED FAIL | FAIL → PASS → FAIL | KILLED |
| M13 | key-entry-sha-mismatch: JUDGED FAIL | FAIL → PASS → FAIL | KILLED |

## Exact mutant diffs and before/after hashes

Every mutant changes exactly one source line. Pristine and restored sha256 for each: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

### M01
Mutated sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
```diff
@@ line 400 @@
-    legs.append(("SET", cited == want and not retired,
+    legs.append(("SET", set(cited) <= set(want) and not retired,
```

### M02
Mutated sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
```diff
@@ line 400 @@
-    legs.append(("SET", cited == want and not retired,
+    legs.append(("SET", cited == want,
```

### M03
Mutated sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
```diff
@@ line 412 @@
-        if len(hits) != 1 or hits[0] in base_lines or bare(hits[0]) in base_bare:
+        if len(hits) != 1 or hits[0] in base_lines:
```

### M04
Mutated sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
```diff
@@ line 416 @@
-    old_hits = [p for p in OLD_PHRASES if " " + p + " " in norm_entry]
+    old_hits = [p for p in OLD_PHRASES if " " + p + " " == norm_entry]
```

### M05
Mutated sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
```diff
@@ line 432 @@
-        if count.get(sid, 0) != 1 or not cells or len(cells) < 13 or not in_registry.get(sid):
+        if count.get(sid, 0) != 1 or not cells or len(cells) < 13:
```

### M06
Mutated sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
```diff
@@ line 438 @@
-        if cells[8].strip() != "mined":
+        if cells[8].strip() not in ("mined", "queued"):
```

### M07
Mutated sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
```diff
@@ line 440 @@
-        if cells[4].strip() not in ("A", "B"):
+        if cells[4].strip() not in ("A", "B", "C"):
```

### M08
Mutated sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
```diff
@@ line 442 @@
-        if ENTRY not in [u.strip() for u in re.split(r"[,;]", cells[11])]:
+        if False and ENTRY not in [u.strip() for u in re.split(r"[,;]", cells[11])]:
```

### M09
Mutated sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
```diff
@@ line 456 @@
-        if not urls or not old_urls or page_of(urls[0], locator) != page_of(old_urls[0], locator):
+        if not urls or not old_urls:
```

### M10
Mutated sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
```diff
@@ line 458 @@
-        elif any(page_of(u, locator) != page_of(urls[0], locator) or not u.startswith("https://web.archive.org/web/")
+        elif any(page_of(u, locator) != page_of(urls[0], locator)
```

### M11
Mutated sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
```diff
@@ line 479 @@
-        if not item.get("file") or not os.path.isfile(path) or sha(path) != item.get("sha256"):
+        if not item.get("file") or not os.path.isfile(path):
```

### M12
Mutated sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
```diff
@@ line 492 @@
-        if not locator.locate_in(text, quote):
+        if False and not locator.locate_in(text, quote):
```

### M13
Mutated sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
```diff
@@ line 507 @@
-        if key.get("entry_sha256") != entry_sha:
+        if False and key.get("entry_sha256") != entry_sha:
```

## Fixture restoration digests

The scorer checked every file hash against its setup manifest after all runs; all 15 file maps matched.

| Fixture | Before and after tree sha256 (equal) |
|---|---|
| positive-no-key | 2cd76b5e3bd6abc544a3fc9fb12e272eb6645e8ad3007aba34343578443c90c5 |
| positive-bound-key | d278f3777ed9233c8615e144ae82a926fb33adc1753c683000b2ef895177e53f |
| missing-id | 892a4e414a3e1420d0ca3444a333e72f78c711add6b146a5bde0642cdfbc829a |
| retired-id | 7647c323ee36e18b23d2a3c18ec100ad04f118535645bbcdb07dbe0c2ce3fff2 |
| new-id-on-base-line | c3e3b15f20f81d8ad08a8accacf1a26cf8843d86fe3c2db68e9d45527e12a01f |
| frozen-phrase | 4f465fb3a300c15245eb956c63dce49d90239c76a82c84e762911e11ede2072e |
| row-outside-registry | 6829ec4dd72301687d4a98709d44f6fcb3e73e747c3d248062385938327b60ad |
| status-queued | baba9721037d3a6047efdfc954325d62b1ce7efb851b4ad3ca7ac4719116afa9 |
| tier-C | 7928e0c862a18d2cd3794d5d26c9054b0ab3b6f1a87aba6e07b39c3f19af0621 |
| used-by-missing | 41cd50f5835b4f8b7d90d461a4be55ca195f9a22bc1beb6c1bc1d61470714012 |
| other-page-url | 1cda4cf9c59a97352d53e6dca4961d0199590a5df07fb640531bf9ea1ba21b94 |
| extra-non-wayback-url | 7090aeb270ac0cb97ced114fdaca7696f5e53bf5f0fac8f469387ab527c2aedb |
| capture-hash-mismatch | 0ea751e216a9719004579fffed47702b25142146000b8e15834da4d934e5f001 |
| quote-not-located | fc579220cbb717f0a7cff3f3275ec3878fcadd1df159432b00aa2a8982aaecdf |
| key-entry-sha-mismatch | 72c3437c60df5acbb022b04d7420781e26ec4a77eae5b4be31507533591bee5d |

Artifact identities: candidate entry and sandbox entry both `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0`; input build.patch `e37abc6d6403a26ecaeb8aa6434dba3d3ffd02775a7e53ce9d1c8090a9ef2d61`. Final measured sandbox footprint: **97 MiB**, below the cap after correcting the disclosed transient cache-copy breach.

Pristine/restored matrix: 15 pristine cases, 195 mutant cases, 195 restored cases, plus one initial canonical candidate run = **406 total**. All 15 pristine oracles and all 195 restored oracles passed. Twelve mutants were detected; the retired-conjunct omission survived through redundancy.

Reproduction: `timeout 50 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/probe.py pristine`; per-mutant phase `mutated M##` then exact restore and `restored M##`. Saved `mutation-evidence.json` contains the one-line changes to reapply in a separate disposable copy; current mutant paths contain restored frozen bytes.

## Frozen and restored control receipts

RECEIPT MutLegsA3/restored-M01-capture-hash-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M01-extra-non-wayback-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M01-frozen-phrase counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=OLDWORD,SUPPORT
RECEIPT MutLegsA3/restored-M01-key-entry-sha-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M01-missing-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M01-new-id-on-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M01-other-page-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M01-positive-bound-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT MutLegsA3/restored-M01-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M01-quote-not-located counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M01-retired-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M01-row-outside-registry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M01-status-queued counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M01-tier-C counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M01-used-by-missing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M02-capture-hash-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M02-extra-non-wayback-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M02-frozen-phrase counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=OLDWORD,SUPPORT
RECEIPT MutLegsA3/restored-M02-key-entry-sha-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M02-missing-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M02-new-id-on-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M02-other-page-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M02-positive-bound-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT MutLegsA3/restored-M02-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M02-quote-not-located counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M02-retired-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M02-row-outside-registry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M02-status-queued counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M02-tier-C counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M02-used-by-missing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M03-capture-hash-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M03-extra-non-wayback-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M03-frozen-phrase counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=OLDWORD,SUPPORT
RECEIPT MutLegsA3/restored-M03-key-entry-sha-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M03-missing-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M03-new-id-on-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M03-other-page-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M03-positive-bound-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT MutLegsA3/restored-M03-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M03-quote-not-located counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M03-retired-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M03-row-outside-registry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M03-status-queued counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M03-tier-C counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M03-used-by-missing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M04-capture-hash-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M04-extra-non-wayback-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M04-frozen-phrase counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=OLDWORD,SUPPORT
RECEIPT MutLegsA3/restored-M04-key-entry-sha-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M04-missing-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M04-new-id-on-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M04-other-page-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M04-positive-bound-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT MutLegsA3/restored-M04-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M04-quote-not-located counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M04-retired-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M04-row-outside-registry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M04-status-queued counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M04-tier-C counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M04-used-by-missing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M05-capture-hash-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M05-extra-non-wayback-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M05-frozen-phrase counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=OLDWORD,SUPPORT
RECEIPT MutLegsA3/restored-M05-key-entry-sha-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M05-missing-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M05-new-id-on-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M05-other-page-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M05-positive-bound-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT MutLegsA3/restored-M05-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M05-quote-not-located counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M05-retired-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M05-row-outside-registry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M05-status-queued counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M05-tier-C counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M05-used-by-missing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M06-capture-hash-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M06-extra-non-wayback-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M06-frozen-phrase counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=OLDWORD,SUPPORT
RECEIPT MutLegsA3/restored-M06-key-entry-sha-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M06-missing-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M06-new-id-on-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M06-other-page-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M06-positive-bound-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT MutLegsA3/restored-M06-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M06-quote-not-located counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M06-retired-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M06-row-outside-registry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M06-status-queued counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M06-tier-C counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M06-used-by-missing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M07-capture-hash-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M07-extra-non-wayback-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M07-frozen-phrase counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=OLDWORD,SUPPORT
RECEIPT MutLegsA3/restored-M07-key-entry-sha-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M07-missing-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M07-new-id-on-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M07-other-page-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M07-positive-bound-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT MutLegsA3/restored-M07-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M07-quote-not-located counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M07-retired-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M07-row-outside-registry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M07-status-queued counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M07-tier-C counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M07-used-by-missing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M08-capture-hash-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M08-extra-non-wayback-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M08-frozen-phrase counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=OLDWORD,SUPPORT
RECEIPT MutLegsA3/restored-M08-key-entry-sha-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M08-missing-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M08-new-id-on-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M08-other-page-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M08-positive-bound-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT MutLegsA3/restored-M08-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M08-quote-not-located counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M08-retired-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M08-row-outside-registry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M08-status-queued counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M08-tier-C counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M08-used-by-missing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M09-capture-hash-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M09-extra-non-wayback-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M09-frozen-phrase counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=OLDWORD,SUPPORT
RECEIPT MutLegsA3/restored-M09-key-entry-sha-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M09-missing-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M09-new-id-on-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M09-other-page-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M09-positive-bound-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT MutLegsA3/restored-M09-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M09-quote-not-located counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M09-retired-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M09-row-outside-registry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M09-status-queued counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M09-tier-C counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M09-used-by-missing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M10-capture-hash-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M10-extra-non-wayback-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M10-frozen-phrase counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=OLDWORD,SUPPORT
RECEIPT MutLegsA3/restored-M10-key-entry-sha-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M10-missing-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M10-new-id-on-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M10-other-page-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M10-positive-bound-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT MutLegsA3/restored-M10-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M10-quote-not-located counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M10-retired-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M10-row-outside-registry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M10-status-queued counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M10-tier-C counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M10-used-by-missing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M11-capture-hash-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M11-extra-non-wayback-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M11-frozen-phrase counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=OLDWORD,SUPPORT
RECEIPT MutLegsA3/restored-M11-key-entry-sha-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M11-missing-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M11-new-id-on-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M11-other-page-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M11-positive-bound-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT MutLegsA3/restored-M11-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M11-quote-not-located counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M11-retired-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M11-row-outside-registry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M11-status-queued counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M11-tier-C counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M11-used-by-missing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M12-capture-hash-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M12-extra-non-wayback-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M12-frozen-phrase counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=OLDWORD,SUPPORT
RECEIPT MutLegsA3/restored-M12-key-entry-sha-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M12-missing-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M12-new-id-on-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M12-other-page-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M12-positive-bound-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT MutLegsA3/restored-M12-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M12-quote-not-located counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M12-retired-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M12-row-outside-registry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M12-status-queued counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M12-tier-C counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M12-used-by-missing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M13-capture-hash-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M13-extra-non-wayback-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M13-frozen-phrase counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=OLDWORD,SUPPORT
RECEIPT MutLegsA3/restored-M13-key-entry-sha-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M13-missing-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M13-new-id-on-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M13-other-page-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M13-positive-bound-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT MutLegsA3/restored-M13-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/restored-M13-quote-not-located counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/restored-M13-retired-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/restored-M13-row-outside-registry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M13-status-queued counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M13-tier-C counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/restored-M13-used-by-missing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/initial-canonical-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/pristine-capture-hash-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/pristine-extra-non-wayback-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/pristine-frozen-phrase counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=OLDWORD,SUPPORT
RECEIPT MutLegsA3/pristine-key-entry-sha-mismatch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/pristine-missing-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/pristine-new-id-on-base-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=LINES,ROWS,SUPPORT
RECEIPT MutLegsA3/pristine-other-page-url counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/pristine-positive-bound-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SUPPORT
RECEIPT MutLegsA3/pristine-positive-no-key counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=JUDGED,SUPPORT
RECEIPT MutLegsA3/pristine-quote-not-located counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=PINNED,SUPPORT
RECEIPT MutLegsA3/pristine-retired-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SUPPORT
RECEIPT MutLegsA3/pristine-row-outside-registry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/pristine-status-queued counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/pristine-tier-C counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT
RECEIPT MutLegsA3/pristine-used-by-missing counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=ROWS,SUPPORT

## Every structured run: full stdout and exit

### mutated/M01/capture-hash-mismatch
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M01/extra-non-wayback-url
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M01/frozen-phrase
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M01/key-entry-sha-mismatch
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M01/missing-id
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET PASS cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M01/new-id-on-base-line
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M01/other-page-url
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M01/positive-bound-key
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M01/positive-no-key
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M01/quote-not-located
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M01/retired-id
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M01/row-outside-registry
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M01/status-queued
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M01/tier-C
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M01/used-by-missing
counter-sha256: `edd49a3ee5809bd54676da1b98031333f9dcd8956a514d39e190bc7880eb2691`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/capture-hash-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/extra-non-wayback-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/frozen-phrase
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/key-entry-sha-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/missing-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/new-id-on-base-line
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/other-page-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/positive-bound-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/quote-not-located
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/retired-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/row-outside-registry
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/status-queued
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/tier-C
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M01/used-by-missing
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M01.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/capture-hash-mismatch
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/extra-non-wayback-url
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/frozen-phrase
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/key-entry-sha-mismatch
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/missing-id
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/new-id-on-base-line
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/other-page-url
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/positive-bound-key
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/positive-no-key
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/quote-not-located
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/retired-id
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/row-outside-registry
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/status-queued
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/tier-C
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M02/used-by-missing
counter-sha256: `b0b2c503b89298ee38bff1058239e83f9e16af33c3f8d443873fd5c0c5aab2e9`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/capture-hash-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/extra-non-wayback-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/frozen-phrase
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/key-entry-sha-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/missing-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/new-id-on-base-line
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/other-page-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/positive-bound-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/quote-not-located
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/retired-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/row-outside-registry
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/status-queued
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/tier-C
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M02/used-by-missing
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M02.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/capture-hash-mismatch
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/extra-non-wayback-url
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/frozen-phrase
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/key-entry-sha-mismatch
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/missing-id
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/new-id-on-base-line
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/other-page-url
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/positive-bound-key
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/positive-no-key
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/quote-not-located
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/retired-id
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/row-outside-registry
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/status-queued
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/tier-C
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M03/used-by-missing
counter-sha256: `b828ff45dea6309c5f337760eeca4079a3fac66526c3256af2a4b3152d3a7095`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/capture-hash-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/extra-non-wayback-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/frozen-phrase
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/key-entry-sha-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/missing-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/new-id-on-base-line
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/other-page-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/positive-bound-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/quote-not-located
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/retired-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/row-outside-registry
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/status-queued
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/tier-C
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M03/used-by-missing
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M03.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/capture-hash-mismatch
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/extra-non-wayback-url
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/frozen-phrase
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/key-entry-sha-mismatch
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/missing-id
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/new-id-on-base-line
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/other-page-url
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/positive-bound-key
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/positive-no-key
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/quote-not-located
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/retired-id
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/row-outside-registry
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/status-queued
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/tier-C
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M04/used-by-missing
counter-sha256: `6dd52676039682dd4398380a364928e21485b1db9f76b93c1aa231a7d9640bec`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/capture-hash-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/extra-non-wayback-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/frozen-phrase
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/key-entry-sha-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/missing-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/new-id-on-base-line
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/other-page-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/positive-bound-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/quote-not-located
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/retired-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/row-outside-registry
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/status-queued
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/tier-C
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M04/used-by-missing
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M04.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/capture-hash-mismatch
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/extra-non-wayback-url
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/frozen-phrase
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/key-entry-sha-mismatch
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/missing-id
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/new-id-on-base-line
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/other-page-url
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/positive-bound-key
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/positive-no-key
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/quote-not-located
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/retired-id
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/row-outside-registry
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/status-queued
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/tier-C
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M05/used-by-missing
counter-sha256: `3d87f5be07193ca31c319cf3440bf743dc1ed1e4aee2edc8d57f8c8d2f3b4d9f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/capture-hash-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/extra-non-wayback-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/frozen-phrase
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/key-entry-sha-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/missing-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/new-id-on-base-line
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/other-page-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/positive-bound-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/quote-not-located
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/retired-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/row-outside-registry
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/status-queued
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/tier-C
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M05/used-by-missing
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M05.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/capture-hash-mismatch
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/extra-non-wayback-url
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/frozen-phrase
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/key-entry-sha-mismatch
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/missing-id
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/new-id-on-base-line
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/other-page-url
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/positive-bound-key
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/positive-no-key
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/quote-not-located
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/retired-id
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/row-outside-registry
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/status-queued
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/tier-C
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M06/used-by-missing
counter-sha256: `0778bcd6795f979533c4d61f48f0de225c637b14e321e8114f7ced271fd0c61c`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/capture-hash-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/extra-non-wayback-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/frozen-phrase
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/key-entry-sha-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/missing-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/new-id-on-base-line
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/other-page-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/positive-bound-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/quote-not-located
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/retired-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/row-outside-registry
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/status-queued
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/tier-C
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M06/used-by-missing
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M06.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/capture-hash-mismatch
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/extra-non-wayback-url
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/frozen-phrase
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/key-entry-sha-mismatch
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/missing-id
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/new-id-on-base-line
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/other-page-url
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/positive-bound-key
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/positive-no-key
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/quote-not-located
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/retired-id
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/row-outside-registry
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/status-queued
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/tier-C
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M07/used-by-missing
counter-sha256: `5772569cecc2030837597eb598a20287d960b9783d3376e631823c82b267f1de`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/capture-hash-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/extra-non-wayback-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/frozen-phrase
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/key-entry-sha-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/missing-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/new-id-on-base-line
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/other-page-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/positive-bound-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/quote-not-located
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/retired-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/row-outside-registry
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/status-queued
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/tier-C
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M07/used-by-missing
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M07.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/capture-hash-mismatch
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/extra-non-wayback-url
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/frozen-phrase
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/key-entry-sha-mismatch
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/missing-id
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/new-id-on-base-line
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/other-page-url
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/positive-bound-key
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/positive-no-key
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/quote-not-located
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/retired-id
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/row-outside-registry
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/status-queued
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/tier-C
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M08/used-by-missing
counter-sha256: `ffbfaf0162cd9432ffe8faa6119c7b3d85e816900c791959a297334186a42e2f`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/capture-hash-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/extra-non-wayback-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/frozen-phrase
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/key-entry-sha-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/missing-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/new-id-on-base-line
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/other-page-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/positive-bound-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/quote-not-located
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/retired-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/row-outside-registry
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/status-queued
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/tier-C
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M08/used-by-missing
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M08.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/capture-hash-mismatch
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/extra-non-wayback-url
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/frozen-phrase
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/key-entry-sha-mismatch
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/missing-id
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/new-id-on-base-line
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/other-page-url
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/positive-bound-key
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/positive-no-key
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/quote-not-located
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/retired-id
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/row-outside-registry
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/status-queued
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/tier-C
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M09/used-by-missing
counter-sha256: `c501ba9ab0df35d8258e0a5bd0525fd769f26b20f79a1fea19ed6c8e55a900a1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/capture-hash-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/extra-non-wayback-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/frozen-phrase
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/key-entry-sha-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/missing-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/new-id-on-base-line
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/other-page-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/positive-bound-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/quote-not-located
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/retired-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/row-outside-registry
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/status-queued
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/tier-C
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M09/used-by-missing
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M09.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/capture-hash-mismatch
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/extra-non-wayback-url
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/frozen-phrase
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/key-entry-sha-mismatch
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/missing-id
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/new-id-on-base-line
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/other-page-url
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/positive-bound-key
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/positive-no-key
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/quote-not-located
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/retired-id
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/row-outside-registry
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/status-queued
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/tier-C
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M10/used-by-missing
counter-sha256: `0cc1df8959d5a6350bab2bbca09bcd24c40ce6a023209b1717fcfb1ae3a95fd0`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/capture-hash-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/extra-non-wayback-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/frozen-phrase
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/key-entry-sha-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/missing-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/new-id-on-base-line
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/other-page-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/positive-bound-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/quote-not-located
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/retired-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/row-outside-registry
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/status-queued
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/tier-C
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M10/used-by-missing
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M10.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/capture-hash-mismatch
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/extra-non-wayback-url
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/frozen-phrase
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/key-entry-sha-mismatch
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/missing-id
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/new-id-on-base-line
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/other-page-url
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/positive-bound-key
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/positive-no-key
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/quote-not-located
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/retired-id
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/row-outside-registry
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/status-queued
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/tier-C
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M11/used-by-missing
counter-sha256: `1072cdefca644bac3ab77781ede1c67c1db4320185340a288e0d509ee3106584`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/capture-hash-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/extra-non-wayback-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/frozen-phrase
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/key-entry-sha-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/missing-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/new-id-on-base-line
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/other-page-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/positive-bound-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/quote-not-located
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/retired-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/row-outside-registry
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/status-queued
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/tier-C
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M11/used-by-missing
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M11.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/capture-hash-mismatch
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/extra-non-wayback-url
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/frozen-phrase
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/key-entry-sha-mismatch
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/missing-id
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/new-id-on-base-line
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/other-page-url
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/positive-bound-key
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/positive-no-key
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/quote-not-located
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/retired-id
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/row-outside-registry
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/status-queued
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/tier-C
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M12/used-by-missing
counter-sha256: `810083f25e34e69f0edb813ce738912cd8df588fdcdf7ab0da8631b05236edd1`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/capture-hash-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/extra-non-wayback-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/frozen-phrase
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/key-entry-sha-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/missing-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/new-id-on-base-line
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/other-page-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/positive-bound-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/quote-not-located
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/retired-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/row-outside-registry
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/status-queued
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/tier-C
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M12/used-by-missing
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M12.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/capture-hash-mismatch
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/extra-non-wayback-url
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/frozen-phrase
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/key-entry-sha-mismatch
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/missing-id
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/new-id-on-base-line
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/other-page-url
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/positive-bound-key
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/positive-no-key
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/quote-not-located
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/retired-id
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/row-outside-registry
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/status-queued
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/tier-C
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### mutated/M13/used-by-missing
counter-sha256: `69a643a140d2d2ba87c7c783f9c7d5b231657be6c7adb7e1c5e92bf4cde5e4e4`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/capture-hash-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/extra-non-wayback-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/frozen-phrase
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/key-entry-sha-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/missing-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/new-id-on-base-line
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/other-page-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/positive-bound-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/quote-not-located
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/retired-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/row-outside-registry
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/status-queued
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/tier-C
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### restored/M13/used-by-missing
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/mutants/M13.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### initial-canonical/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 60 env PYTHONDONTWRITEBYTECODE=1 UV_CACHE_DIR=/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/uv-cache UV_OFFLINE=true UV_PYTHON_DOWNLOADS=never TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/tmp python3 -B reports/round-60/accept-d.py`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### pristine/capture-hash-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/capture-hash-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:capture-missing-or-hash']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### pristine/extra-non-wayback-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/extra-non-wayback-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:extra-url-not-a-capture-of-the-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### pristine/frozen-phrase
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/frozen-phrase`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed']
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### pristine/key-entry-sha-mismatch
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/key-entry-sha-mismatch`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=000000000000 landed=0073da7ed7e0
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### pristine/missing-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/missing-id`
```text
SET FAIL cited=46 want=47 missing=['S600'] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### pristine/new-id-on-base-line
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/new-id-on-base-line`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=1 base_line=True']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:line-shares-3-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### pristine/other-page-url
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/other-page-url`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:not-same-page']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### pristine/positive-bound-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-bound-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### pristine/positive-no-key
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/positive-no-key`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```
### pristine/quote-not-located
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/quote-not-located`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### pristine/retired-id
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/retired-id`
```text
SET FAIL cited=48 want=47 missing=[] extra=['S602'] retired_cited=['S602']
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S602:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### pristine/row-outside-registry
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/row-outside-registry`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=1 registry=False']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### pristine/status-queued
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/status-queued`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:status=queued']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### pristine/tier-C
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/tier-C`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:tier=C']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```
### pristine/used-by-missing
counter-sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`
cwd: `/fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone`
command: `timeout 25 python3 -B /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/MutLegsA3/fixtures/used-by-missing`
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:used-by']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[]
ACCEPT-D-60: FAIL
exit=1
```

## Restoration hashes

```json
{
  "M01": "b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc",
  "M02": "b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc",
  "M03": "b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc",
  "M04": "b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc",
  "M05": "b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc",
  "M06": "b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc",
  "M07": "b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc",
  "M08": "b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc",
  "M09": "b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc",
  "M10": "b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc",
  "M11": "b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc",
  "M12": "b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc",
  "M13": "b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc"
}
```
