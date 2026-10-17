# R10-F13 — drift shard 13: SCORECARD.md re-run commands, second half (lines 105–210)

Date: 2026-10-17. Worker: R10-F13 (drift shard 13). Lane: kotodama-shokunin.
Revision at run: `e3a1ec9435787328ac9f828f96cb6390e4916b8f` (`git rev-parse HEAD`).

Method notes (deviations stated, not hidden):

- `export TMPDIR=$PWD/.scratch/drift-shard13` for every scratch-writing command
  (in-lane; `/tmp` remains inode-exhausted).
- The two round validators always write their receipt to a fixed filed path
  (`reports/round-8/validation.json`, `reports/round-9/validation.json`). To avoid
  rewriting filed report bytes, both were re-executed with the module-level
  `OUTPUT_REL` redirected into `.scratch/drift-shard13/` (importlib load +
  `mod.OUTPUT_REL = ".scratch/drift-shard13/<file>"` before `mod.main()`).
  Code executed is byte-identical to the cited file; only the receipt destination
  differs. Filed bytes were not touched by this shard.
- `output_sha256` is sha256 over captured stdout; stderr was empty
  (`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`) for every row.
- Raw stdout/stderr captures and fresh receipts: `.scratch/drift-shard13/`
  (`out-<label>.txt`, `err-<label>.txt`, `r8-validation.json`, `r9-validation.json`).

## 1. Ledger rows (SCORECARD.md lines 105–210)

| # | command | source locator | exit | stdout sha256 (16) | verdict |
|---|---|---|---|---|---|
| 13-01 | `python3 tools/d2-typed-labels.py --selftest` | SCORECARD.md:112, 128 | 0 | `7231139c5b060898` | current |
| 13-02 | `python3 tools/assemble-d2.py --check` | SCORECARD.md:112 | 0 | `2fa0c8c197459f54` | current |
| 13-03 | `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | SCORECARD.md:113, 143 | 0 | `c83dac8f8bab0fea` | current |
| 13-04 | `python3 tools/check-gate-battery.py --selftest` | SCORECARD.md:114, 144 | 0 | `8b1fdd6f2d316ef2` | current |
| 13-05 | `python3 reports/round-8/run-validation.py` (pre-fix runner `ed65b88`, sha `7eaa36789b4d71ce`) | SCORECARD.md:114–116 | **1** | `b2fb989333a06f0c` | **stale** at observation time (S13-1) |
| 13-11 | `python3 reports/round-8/run-validation.py` (post-fix runner `7921b4f`, sha `d78da29fdacc75d4`, sibling repair 18:32:28) | SCORECARD.md:114–116 | 0 | `4d300b24a04ff44a` | **stale-fixed**, verified here (S13-1) |
| 13-06 | `python3 reports/round-9/run-validation.py` | SCORECARD.md:133, 142, 144, 145 | 0 | `4d300b24a04ff44a` | current (note O13-2) |
| 13-07 | `python3 tools/assemble-culture-d3.py --check` | SCORECARD.md:142, 158 | 0 | `e20620fabdf28532` | current |
| 13-08 | round-5 routing reproduce one-liner (`python3 -c 'import json; …'`, verbatim from line 201) | SCORECARD.md:201 | 0 | `19b98ffbe56449bd` | current |
| 13-09 | `git status` scope read (SCORECARD.md:117); ran as `git status --porcelain -- . ':!/.scratch'` | SCORECARD.md:117 | 0 | `a3f92351e7679c3f` | current (state note O13-1) |
| 13-10 | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --json` (supporting evidence for 13-05, not itself a SCORECARD citation) | tools/replay-frozen.py usage cited SKILL.md:162/190 | 2 | `cbde6c5e17c7f77e` | current (exit 2 is its designed refusal on a drifted live tree) |

Full hashes:

```
13-01 7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252
13-02 2fa0c8c197459f549de2f0822b8895477e27dcce38def75e18346ba6d672e386
13-03 c83dac8f8bab0feaa55b853a43a96562d0ccb9dd6477d24b995d2331577d5c02
13-04 8b1fdd6f2d316ef20ac3ebe23695a81626358084dd8535816116fd71a3fd9e28
13-05 b2fb989333a06f0c095731fcb5e77e7843b442a14d41156f9fee4f37bc66781e
13-06 4d300b24a04ff44afdb89c6944174ad8f71056667fd0e5f2044266010943b2f5
13-07 e20620fabdf285323c021ae11cad32b1ece58a28d59dd74f7df237578ffb560a
13-08 19b98ffbe56449bd5fc410674ad6f0d5c4914c8182d37da4f3398c7d1b627bff
13-09 a3f92351e7679c3f89476c93a5e89c8bce6600561abb1b64fcb3955cf3cee75c
13-10 cbde6c5e17c7f77e6bcf2f57d1359af1a6ef41c6c201c0b11687ad18daeab528
13-11 4d300b24a04ff44afdb89c6944174ad8f71056667fd0e5f2044266010943b2f5
```

Note on 13-11's hash: it is textually identical to 13-06's because both commands
print the same four lines (`claim F: PASS` / `claim O: PASS` / `claim D: PASS` /
`acceptance_checks_passed: True`); the collision is expected, not a copy error.
The distinguishing evidence for 13-11 is the receipt
`.scratch/drift-shard13/r8-validation-postfix.json`.

### Claim-vs-observed checks (rows that still pass)

- 13-01: stdout tail `selftest: 39/39 checks passed …` — matches the round-8
  claim "selftest 39/39" (SCORECARD.md:112).
- 13-02: `packet.d2.yml: byte-identical deterministic assembly` — matches.
- 13-03: 179 files; partition totals `civilizations 94, culture-material 16,
  linguistics 16, myth-symbol 16, synthesis 24, verification 13` — matches
  "179 knowledge entries, same six partitions" (SCORECARD.md:113, 143) and the
  round-5 partition line 16/16/16/24/13/94.
- 13-04: `SELFTEST OK 28/28 controls behaved as expected`. The round-8 text
  ("battery 10/10 … controls", SCORECARD.md:114) is a subset of the current
  28-control selftest after the round-9 baseline extension — superseded count,
  not a contradiction.
- 13-06: `claim F: PASS / claim O: PASS / claim D: PASS / acceptance_checks_passed: True`
  (fresh receipt `.scratch/drift-shard13/r9-validation.json`, sha256
  `a4c009261b069f80947a6d701232bd4abd1007bbf419d93c6bfdb1068f6522bb`). Matches
  "round-9 run-validation exits 0" (SCORECARD.md:133).
- 13-07: `packet.json: byte-identical …; packet.gates.yml: byte-identical …` — matches.
- 13-08: prints `16 0 0` then `16 16 1` — matches the routing-history text
  ("16 requested, zero launched, zero completed"; one executed batch, 16/16).
- 13-09: at run time the tree carried sibling-worker writes (see O13-1); the
  scope read itself is exit 0 and no out-of-lane path was written by this shard.

### File/glob citations in lines 105–210 (existence + sha256, read-only)

| cited path | status | sha256 (16) |
|---|---|---|
| `reports/round-8/validation.json` | exists (unmodified vs HEAD) | `359932a7debf6ec3` |
| `reports/round-8/rerun.json` | exists | `6b963298d3c4cf26` |
| `reports/round-8/operability/battery-rerun.json` | exists (line 114's bare `battery-rerun.json`; runner constant `BATTERY_RERUN_REL` resolves to this path, reports/round-8/run-validation.py:85) | `—` |
| `reports/round-8/metadata/m0*.md` | 11 fragments (m01–m11); an `m0*` glob shows only 9 — the claim "11 shard fragments" is correct on full listing | — |
| `reports/round-8/freshness/R8-F*-receipt.{json,md}` | 15 json + 15 md | — |
| `reports/round-8/freshness/reconciliation.json`, `audit.md` | exist | `204ec38aa413b185`, `a736d03b58a8156e` |
| `reports/round-8/adjacency.md` | exists | `644311ec10d503da` |
| `examples/culture-d2/typed-labels.d2.yml` | exists | `e70ba1477dbeb830` |
| `reports/round-9/freshness/reconciliation.json` | exists | `cfbf21b885690c71` |
| `reports/round-9/d3/replay.md` | exists | `4e96ae8f6a9e61fb` |
| `reports/round-9/adjacency.md` | exists | `5d7d3269a97a1f1e` |
| `reports/round-9/baselines/registry.md` | exists (rows re-verification is shard 12's scope) | `cf95ba233d792478` |
| `reports/round-5/dispatch.json`, `availability-attempt-1.json`, `native-request-binding.json` | exist | `efb7c314a1045491`, `28dd606da95f6ef5`, `c92e74a888938804` |

Web-only citations: none. `sed -n '105,210p' SCORECARD.md | grep -n http` →
no URLs in the second half; no access attempt to document.

## 2. Stale item S13-1 — round-8 acceptance no longer reproduces (D leg)

**Claim under test:** SCORECARD.md:103–105 ("Acceptance:
`python3 reports/round-8/run-validation.py` exits 0 … `reports/round-8/validation.json`")
and SCORECARD.md:114 ("round-3 manifests reproduce 7/7 isolated").

**Observed now:** exit 1.

```
claim F: PASS
claim O: PASS
claim D: FAIL
  - no D2 frozen replay without digest drift: no round-8 manifest reproduced in
    the live tree and the isolated pinned-revision replay did not reproduce
    every row ({"rows": 7, "reproduced": 0, "mismatch": 0,
    "could_not_evaluate": 7, "exit": 2})
```

F and O legs still pass; the failure is scoped to the D replay leg.

**Independent reproduction** (not via the runner):

```
$ python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --json   # exit 2
all 7 rows: status "could-not-evaluate", reason "gate_digest_mismatch",
detail: "gate: on-disk bytes are not the pinned revision:
         tools/gates/phonology-sanity-gate.py"
```

**Root cause (pin-match matrix, computed by comparing each manifest-pinned gate
sha256 against `git show <rev>:<gate>`):**

| gate (7 rows, 6 distinct scripts) | pin (round 3) | c610e0a r3 | cf338a7 r8-declare | e1694ba r8-admit | 9dc18ec r9-admit | HEAD e3a1ec9 |
|---|---|---|---|---|---|---|
| phonology / lexicon / myth / costume / naming / provenance gates | matches c610e0a | MATCH | MATCH | **DIFF** | DIFF | DIFF |

The round-3 manifest pins gate scripts as of round 3. Round 8's own operability
repairs changed the gate bytes, and that change landed in the round-8 admit
commit `e1694ba`. The round-8 receipt was produced while HEAD still carried the
round-3 gate bytes — its isolated replay restores gates via `git show HEAD:<gate>`
("gates_restored_from_head": 7) and recorded `reproduced: 7, exit: 0`
(HEAD-filed receipt `reports/round-8/validation.json`, claims.D.replay_frozen
`accepted: isolated-pinned-revisions`). Committing the repair invalidated the
acceptance; round 9's runner applies a softer rule to its own leg
("byte-identical to HEAD or documented reason", `reports/round-9/run-validation.py`
thresholds block) and never re-runs round 8's acceptance, so the regression was
never noticed.

**Fix landed during this shard's run (by a sibling R10 worker, not by R10-F13),
and was verified here.** At 18:32:28 `reports/round-8/run-validation.py` was
modified in-tree (`git diff --stat` = 48 insertions / 14 deletions; new sha256
`d78da29fdacc75d425e21c21fa2d299d…`; the pre-fix file is `ed65b88`, sha
`7eaa36789b4d71ce…`, which had matched its filed receipt). The patch adds
`gate_blob_for_pin()`: for each manifest gate pin it walks `git log -- <gate>`
and restores the revision whose blob sha256 matches the pin, instead of
assuming HEAD still carries it. Independent verification by R10-F13 (redirected
receipt, post-fix runner):

```
$ python3 reports/round-8/run-validation.py    # exit 0
claim F: PASS / claim O: PASS / claim D: PASS / acceptance_checks_passed: True
claims.D.replay_frozen: accepted "isolated-pinned-revisions",
isolated {"rows": 7, "reproduced": 7, "mismatch": 0, "could_not_evaluate": 0, "exit": 0},
live_reference still {"reproduced": 0, "could_not_evaluate": 7}  # by design: the live tree has drifted
receipt: .scratch/drift-shard13/r8-validation-postfix.json
```

The repair resolves real pinned bytes from history rather than relaxing the
digest check, and the live-tree leg remains red as designed — so this is a
legitimate fix, not a check bypass. SCORECARD.md:114's text ("round-3 manifests
reproduce 7/7 isolated") is once again true of the current tree, with the
isolation now by revision resolution.

Remaining dispositions if the fix is rejected by review (options, not decisions):
1. New manifest revision re-pinning the gate digests with a documented reason
   (never rewrite `tools/gates/frozen/round-3/MANIFEST.tsv` bytes in place).
2. Document the round-8 D acceptance as point-in-time at `cf338a7`, superseded
   by round 8's own repair at `e1694ba`, as a correction entry (SCORECARD
   corrections are new text, not rewrites of filed report bytes).

Note the plural in the old wording: only one manifest exists today
(`find tools/gates/frozen -maxdepth 2 -name 'MANIFEST*'` → round-3/MANIFEST.tsv
only); the round-8 runner replays that single manifest.

## 3. Observations (recorded, not defects of the SCORECARD text)

**O13-1 — sibling workers rewrote filed receipts in the lane tree.**
At 18:26:58 `reports/round-9/validation.json` was overwritten (mtime
18:26:58.398944507, byte-identical mtime to `.scratch/r10f14/rv9.out` — F14 ran
the validator directly). At 18:27:32 `reports/round-5/validation.json` was
overwritten (mtime 18:27:32.746906697 == `.scratch/f11/rv.out` — F11);
F11 later restored the original bytes (current file = 23928 bytes, mtime
18:29:29.558, sha `78444f4cca7497da` = HEAD bytes). At this shard's close,
`git status --porcelain` still shows ` M reports/round-9/validation.json`
(4 insertions / 14 deletions vs HEAD, HEAD sha `036f84278c481790`, on-disk sha
`dc1d14466d27ccf8`). This shard's runs used the redirected-receipt method and
did not write these paths. Suggested for X04's ledger-consistency audit.

**O13-2 — round-9 battery stdout digests are not run-reproducible; the verdict is.**
Three runs of `python3 reports/round-9/run-validation.py` all exit 0 with
`acceptance_checks_passed: True`, but the recorded battery `stdout_sha256`
pair differs every time: HEAD-filed `25906f6f…`/`201e6eec…`, sibling run
18:26:58 `a4f97f86…`/`787a13d3…`, this shard's run 18:27:59
`d7ed0dcc…`/`4ec62808…` (the third digest `16b6644c…` is stable). The
digests embed tree state (e.g. `git status` lines), so they cannot be used as
byte-level drift detectors across tree states; the exit/verdict is the stable
part. Affects how F14/F19 should compare round-9 evidence.

## 4. Machine-readable rows (for F14's ledger merge)

```json
[
 {"command":"python3 tools/d2-typed-labels.py --selftest","source_locator":"SCORECARD.md:112,128","round10_verdict":"current","output_sha256":"7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252","exit":0},
 {"command":"python3 tools/assemble-d2.py --check","source_locator":"SCORECARD.md:112","round10_verdict":"current","output_sha256":"2fa0c8c197459f549de2f0822b8895477e27dcce38def75e18346ba6d672e386","exit":0},
 {"command":"python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge","source_locator":"SCORECARD.md:113,143","round10_verdict":"current","output_sha256":"c83dac8f8bab0feaa55b853a43a96562d0ccb9dd6477d24b995d2331577d5c02","exit":0},
 {"command":"python3 tools/check-gate-battery.py --selftest","source_locator":"SCORECARD.md:114,144","round10_verdict":"current","output_sha256":"8b1fdd6f2d316ef20ac3ebe23695a81626358084dd8535816116fd71a3fd9e28","exit":0},
 {"command":"python3 reports/round-8/run-validation.py","source_locator":"SCORECARD.md:114,115,116","round10_verdict":"stale-fixed","output_sha256":"b2fb989333a06f0c095731fcb5e77e7843b442a14d41156f9fee4f37bc66781e","exit":1,"note":"pre-fix observation (runner sha 7eaa36789b4d71ce); stale item S13-1"},
 {"command":"python3 reports/round-8/run-validation.py","source_locator":"SCORECARD.md:114,115,116","round10_verdict":"stale-fixed","output_sha256":"4d300b24a04ff44afdb89c6944174ad8f71056667fd0e5f2044266010943b2f5","exit":0,"note":"post-fix verification (runner sha d78da29fdacc75d4, sibling repair 18:32:28); receipt .scratch/drift-shard13/r8-validation-postfix.json"},
 {"command":"python3 reports/round-9/run-validation.py","source_locator":"SCORECARD.md:133,142,144,145","round10_verdict":"current","output_sha256":"4d300b24a04ff44afdb89c6944174ad8f71056667fd0e5f2044266010943b2f5","exit":0},
 {"command":"python3 tools/assemble-culture-d3.py --check","source_locator":"SCORECARD.md:142,158","round10_verdict":"current","output_sha256":"e20620fabdf285323c021ae11cad32b1ece58a28d59dd74f7df237578ffb560a","exit":0},
 {"command":"python3 -c 'import json; a=json.load(open(\"reports/round-5/availability-attempt-1.json\")); d=json.load(open(\"reports/round-5/dispatch.json\")); print(a[\"requested_workers\"],a[\"launched_workers\"],a[\"completed_workers\"]); print(d[\"workers\"],d[\"completed\"],d[\"actual_executed_batches_after_authorization\"])'","source_locator":"SCORECARD.md:201","round10_verdict":"current","output_sha256":"19b98ffbe56449bd5fc410674ad6f0d5c4914c8182d37da4f3398c7d1b627bff","exit":0},
 {"command":"git status --porcelain -- . ':!/.scratch'","source_locator":"SCORECARD.md:117","round10_verdict":"current","output_sha256":"a3f92351e7679c3f89476c93a5e89c8bce6600561abb1b64fcb3955cf3cee75c","exit":0},
 {"command":"python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --json","source_locator":"supporting evidence for SCORECARD.md:114","round10_verdict":"current","output_sha256":"cbde6c5e17c7f77e6bcf2f57d1359af1a6ef41c6c201c0b11687ad18daeab528","exit":2,"note":"exit 2 is the tool's designed refusal on a drifted live tree (7/7 gate_digest_mismatch); supporting evidence for S13-1"}
]
```

## 5. Limits

- These are execution/verdict re-checks, not truth or authenticity audits.
- 13-05/13-06 were executed with the receipt path redirected (method note above);
  every other row ran exactly as cited.
- stdout digests are sha256 of captured stdout; they are stable for the tool
  commands but, per O13-2, not for the round-9 runner's battery legs.
- S13-1 was observed stale (round-8 acceptance exit 1), then repaired in-tree by
  a sibling R10 worker at 18:32:28 and independently verified here (exit 0,
  7/7 reproduced, `.scratch/drift-shard13/r8-validation-postfix.json`); no filed
  report bytes were modified by this shard.
