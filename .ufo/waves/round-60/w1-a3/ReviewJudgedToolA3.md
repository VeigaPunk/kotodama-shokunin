HOLDS
CONTROL-MET: NONE

Review: tools/check-judged-object.py (R60-M1 mistake fix) at revision 5
`14e6413820d482913f723432b62d566967ccd1a6`, run from a sandbox clone
(`env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE -u GIT_OBJECT_DIRECTORY git clone -q
--no-hardlinks`, checkout at the rev). Tool bytes: lane worktree == rev-5 blob,
sha256 `4f25376d3c74cf50ba5850f0bc3bd2c15c6f42fe1d1a7d822bf8a9d888adcc55`
(committed, mode 100755, no worktree drift). Key bytes: lane worktree ==
rev-5 blob `af510aa9`, sha256 `cbf653a1aea1607dbdaa2384cfb59242d937ff441552b4db750e3b5196e6ff1c`.
No tool installs; stdlib only; python3 -B with PYTHONDONTWRITEBYTECODE=1.

## Verdict

The fix is operative and calibrated. The recorded r59 invocation reproduces the
telemetry byte-for-byte: it FAILs (exit 1) on round 59's own bytes — the key's
`entry_sha256` `556ddb27…` vs the entry that landed at `d45985b2` `4e1bef48…`,
with exactly the post-verdict narrowing S602 S616 S623 S643 (47 judged ids from
`key.seats` vs 43 cited at the rev). PASS on an unchanged entry is shown twice:
selftest case 1 and a real-bytes run of the landed `d45985b2` entry with an
honest key (43 ids, sha of the landed bytes) → `JUDGED_OBJECT: PASS`, exit 0.

## Evidence (full outputs, sandbox clone at 14e64138)

### 1. `--selftest` on committed tool

```
$ python3 -B tools/check-judged-object.py --selftest
selftest ok unchanged-entry -> PASS
selftest ok one-word-changed -> FAIL
selftest ok row-line-removed -> FAIL with S602 listed
selftest ok missing-key -> exit 2
exit=0
```

### 2. Recorded r59 command — FAIL on r59's own bytes

```
$ python3 -B tools/check-judged-object.py --key .ufo/waves/round-59/support/planted-key.json --repo . --rev d45985b2 --entry corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
JUDGED_KEY: .ufo/waves/round-59/support/planted-key.json
JUDGED_REPO: .
JUDGED_REV: d45985b2
JUDGED_ENTRY: corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
JUDGED_SHA256_KEY: 556ddb27c7e8066ab5b13bb4b1c1f58be118daa13651c1d030574561a10dcf19
JUDGED_SHA256_AT_REV: 4e1bef48db9cbab07bb218f3b586ff2cc2e5f3b9e923f5ccb603c0afcc9e9d3d
JUDGED_ID_SOURCE: key.seats
JUDGED_IDS_COUNT_JUDGED: 47
JUDGED_IDS_COUNT_AT_REV: 43
JUDGED_NARROWED_IDS: S602 S616 S623 S643
JUDGED_WIDENED_IDS: (none)
JUDGED_NOTE: the entry at d45985b2 is not the judged object; the judged object was changed after it was judged
JUDGED_OBJECT: FAIL
exit=1
```

Independent cross-check of the reported hash and narrowing:

```
$ git cat-file blob d45985b2:corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md | sha256sum
4e1bef48db9cbab07bb218f3b586ff2cc2e5f3b9e923f5ccb603c0afcc9e9d3d  -
$ git cat-file blob d45985b2:... | grep -cE '\bS602\b|\bS616\b|\bS623\b|\bS643\b'
0
$ git cat-file -t 556ddb27c7e8066ab5b13bb4b1c1f58be118daa13651c1d030574561a10dcf19
fatal: Not a valid object name 556ddb27…   (the as-reviewed 47-row bytes were
                                             never committed — the r59 defect
                                             shape itself)
```

Output matches `reports/round-60/telemetry/judged-object-r59.txt` verbatim.

### 3. PASS on an unchanged entry (real landed bytes)

Sandbox key `unchanged-key.json` = honest key for the d45985b2 landed bytes
(`entry_sha256` = the committed blob's sha, `cited_ids` = the 43 ids extracted
from those bytes — built by
`/fast/scratch/hyaku/kotodama-r60a3/ReviewJudgedToolA3/make-unchanged-key.py`):

```
$ python3 -B tools/check-judged-object.py --key /fast/scratch/hyaku/kotodama-r60a3/ReviewJudgedToolA3/unchanged-key.json --repo . --rev d45985b2 --entry corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
JUDGED_KEY: /fast/scratch/hyaku/kotodama-r60a3/ReviewJudgedToolA3/unchanged-key.json
JUDGED_REPO: .
JUDGED_REV: d45985b2
JUDGED_ENTRY: corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
JUDGED_SHA256_KEY: 4e1bef48db9cbab07bb218f3b586ff2cc2e5f3b9e923f5ccb603c0afcc9e9d3d
JUDGED_SHA256_AT_REV: 4e1bef48db9cbab07bb218f3b586ff2cc2e5f3b9e923f5ccb603c0afcc9e9d3d
JUDGED_ID_SOURCE: key.cited_ids
JUDGED_IDS_COUNT_JUDGED: 43
JUDGED_IDS_COUNT_AT_REV: 43
JUDGED_NARROWED_IDS: (none)
JUDGED_WIDENED_IDS: (none)
JUDGED_OBJECT: PASS
exit=0
```

### 4. Mutation: hash comparison inverted once → selftest catches it

Diff of the sandbox copy (one line, line 296 of `evaluate`):

```
-    same = rev_sha == key_sha
+    same = rev_sha != key_sha  # MUTATION: inverted comparison
```

```
$ python3 -B /fast/scratch/hyaku/kotodama-r60a3/ReviewJudgedToolA3/mutated/check-judged-object.py --selftest
selftest FAIL unchanged-entry: rc=1
JUDGED_KEY: /tmp/judged-object-selftest-c208xq8a/repo/planted-key.json
JUDGED_REPO: /tmp/judged-object-selftest-c208xq8a/repo
JUDGED_REV: 9de7532e1f44194ce7268b367c7717404c6831de
JUDGED_ENTRY: corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
JUDGED_SHA256_KEY: 1a3899823fa0e2f1643769e1f0c5918c546372053eb7687906d26cf25a84279f
JUDGED_SHA256_AT_REV: 1a3899823fa0e2f1643769e1f0c5918c546372053eb7687906d26cf25a84279f
JUDGED_ID_SOURCE: key.cited_ids
JUDGED_IDS_COUNT_JUDGED: 2
JUDGED_IDS_COUNT_AT_REV: 2
JUDGED_NARROWED_IDS: (none)
JUDGED_WIDENED_IDS: (none)
JUDGED_NOTE: the entry at 9de7532e1f44194ce7268b367c7717404c6831de is not the judged object; the judged object was changed after it was judged
JUDGED_OBJECT: FAIL

selftest FAIL one-word-changed: rc=0
JUDGED_KEY: /tmp/judged-object-selftest-c208xq8a/repo/planted-key.json
JUDGED_REPO: /tmp/judged-object-selftest-c208xq8a/repo
JUDGED_REV: f5c2aab28c78dddc1cca89cdf1567857a14378b6
JUDGED_ENTRY: corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
JUDGED_SHA256_KEY: 1a3899823fa0e2f1643769e1f0c5918c546372053eb7687906d26cf25a84279f
JUDGED_SHA256_AT_REV: 4a2e1cf0056a4b3f8bd1a7dd897e818a876cd02d2adbe65e6f0119c85e808fff
JUDGED_ID_SOURCE: key.cited_ids
JUDGED_IDS_COUNT_JUDGED: 2
JUDGED_IDS_COUNT_AT_REV: 2
JUDGED_NARROWED_IDS: (none)
JUDGED_WIDENED_IDS: (none)
JUDGED_OBJECT: PASS

selftest FAIL row-removed: rc=0
JUDGED_KEY: /tmp/judged-object-selftest-c208xq8a/repo/planted-key.json
JUDGED_REPO: /tmp/judged-object-selftest-c208xq8a/repo
JUDGED_REV: 6a0d7b0212a59663663a1596706c6519a6e923ef
JUDGED_ENTRY: corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
JUDGED_SHA256_KEY: 1a3899823fa0e2f1643769e1f0c5918c546372053eb7687906d26cf25a84279f
JUDGED_SHA256_AT_REV: c72ae74e13a1095b5d60d17bcbaa2cdbb5f65d835888d97e34451cdefd8ae91a
JUDGED_ID_SOURCE: key.cited_ids
JUDGED_IDS_COUNT_JUDGED: 2
JUDGED_IDS_COUNT_AT_REV: 1
JUDGED_NARROWED_IDS: S602
JUDGED_WIDENED_IDS: (none)
JUDGED_OBJECT: PASS

selftest ok missing-key -> exit 2
exit=1
```

The same mutant on the real r59 case wrongly returns `JUDGED_OBJECT: PASS`
(exit 0) for the narrowed entry — exactly the false-PASS class R60-M1 exists to
kill — and the selftest exposes it on all three verdict-bearing cases.

## Findings (severity order)

None blocking. The committed tool does what the predicate needs: reads
`<rev>:<entry>` via `git cat-file blob` only (read-only git, env cleaned of
`GIT_*`), compares full 64-hex sha256 (`SHA_RE` anchored `^[0-9a-f]{64}$`), and
reports the id narrowing/widening when a judged id set is knowable.

- LOW-1 — selftest blind to comparator weakening that preserves fixture
  verdicts. A first mutation `rev_sha[:16] == key_sha[:16]` (truncated
  comparison) passed all four selftest cases, exit 0:

  ```
  $ python3 -B .../mutated/check-judged-object.py --selftest   # [:16] mutant
  selftest ok unchanged-entry -> PASS
  selftest ok one-word-changed -> FAIL
  selftest ok row-line-removed -> FAIL with S602 listed
  selftest ok missing-key -> exit 2
  exit=0
  ```

  The selftest asserts verdicts and printed hashes, not that the comparison is
  full-length. Any equality-preserving-but-weakened comparator passes. Impact:
  low — a 16-hex-prefix comparator still fails on every real-world post-verdict
  edit (sha256 avalanche); it would only pass under a crafted 64-bit-prefix
  collision. If selftest is treated as the gate for tool changes, a cheap
  hardening is a fixture pair sharing a long prefix or a source-assertion that
  `evaluate` compares the full digest. The inverted/constant mutants that would
  produce wrong verdicts ARE caught (see §4).

- LOW-2 — selftest exercises only the `key.cited_ids` id-source path.
  `key.seats` (the r59 key shape), `key.rows`, `--judged-rev`, the
  widening-note branch and the `same-and-widening` note are untested in
  selftest. The real r59 invocation covers `key.seats` end-to-end (evidence §2),
  so coverage exists in practice; the gap is only in the self-contained
  selftest.

- LOW-3 — cosmetic: when no judged id set is resolvable, `JUDGED_ID_SOURCE:
  none` prints `JUDGED_IDS_COUNT_JUDGED: 0`, which reads as "zero judged ids"
  rather than "unknown". Documented behaviour; the sha verdict is unaffected.

## Residual risk / verification gaps

- A real-bytes r59 PASS case is impossible: the as-reviewed object
  `556ddb27…` is absent from the object store (never committed — the r59
  failure itself). PASS-on-unchanged is instead demonstrated on (a) the
  selftest fixture and (b) the actual landed `d45985b2` entry bytes under an
  honest key. No stronger real-bytes PASS exists to run.
- `_relativise` cuts absolute paths at `/corpus/`; a non-repo absolute path
  containing that marker resolves to a repo-relative path — but the tool only
  ever reads committed blobs via `git cat-file`, so this can redirect which
  committed blob is checked, never read the filesystem. Input failures still
  surface as exit 2.
- Input errors print `JUDGED_OBJECT: FAIL` on stdout with exit 2 (verified in
  selftest case 4); consumers must discriminate on exit code, as the docstring
  states.

## Control receipt (frozen counter at revision 5, honest claim base)

```
$ cd clone && timeout 600 python3 -B reports/round-60/accept-d.py; echo exit=$?
SET FAIL cited=43 want=47 missing=['S648', 'S649', 'S650', 'S651'] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=0 base_line=False', 'S649:lines=0 base_line=False', 'S650:lines=0 base_line=False', 'S651:lines=0 base_line=False']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=0 registry=None', 'S649:rows=0 registry=None', 'S650:rows=0 registry=None', 'S651:rows=0 registry=None']
PINNED FAIL bad=['manifest:FileNotFoundError', 'S648:no-row-or-manifest', 'S649:no-row-or-manifest', 'S650:no-row-or-manifest', 'S651:no-row-or-manifest']
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```

RECEIPT ReviewJudgedToolA3/claim-base counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,LINES,ROWS,PINNED,JUDGED,SUPPORT

This is the honest base state (no skip-the-work fixture run): it matches the
declared `before` line exactly — SET, LINES, ROWS, PINNED, JUDGED, SUPPORT FAIL
with OLDWORD PASS.

Instals: none. All work under `/fast/scratch/hyaku/kotodama-r60a3/ReviewJudgedToolA3/`
(clone, mutated copy, fixtures); lane worktree untouched.
