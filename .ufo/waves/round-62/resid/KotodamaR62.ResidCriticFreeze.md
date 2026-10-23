VERDICT KotodamaR62.ResidCriticFreeze: MIXED

## Axes and review boundary

- **Depth (D):** factual assertions and their source-scoped support in the four footwear lines.
- **Operability (O):** the newly runnable row re-opener and its specified behavior.
- **Calibration:** identity of the frozen instruments, first-run provenance, and accuracy of control-credit claims.
- **Coverage, freshness, adjacency:** boundary axes; this audit does not infer their improvement from counter scores.

Read-only review at `a2c5caa59b2d67ce35e53d6ce0217030a66cdd48`, using `/fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone`. No acceptance counter, product tool, locator, test, live request, judge, or additional agent runtime was executed by this seat. Historical counter outputs below are attributed receipts, not my reruns. This is a critique, not an admission decision.

**Results:** (a) HOLDS through the measured revision; (b) consistent with all inspected first-run evidence, with no prohibited build-seat counter run found; (c) MIXED under the assignment's stronger requirement that *every change* have an exercised forcing control receipt; (d) the D/depth and O/operability names fit the changed surfaces, subject to the explicitly bounded predicates and substantive review. No high-severity freeze breach was demonstrated.

## Ranked finding

### 1. MEDIUM — not every revision-1 change has an exercised forcing control receipt

**Counterexample to the provenance claim.** Revision 1 adds O's default-registry-path test, default exit/summary checks, and stricter ERR prefix/both-stream checks. The cited reports justify those changes by source inspection or explicitly unexecuted counterexamples. The committed rescore matrix has no isolated missing-default-registry, wrong-default-exit/summary, bad-error-prefix, or stdout-traceback control demonstrating those particular changes. Its positive runs exercise the new checks, but a positive PASS is not evidence that a defective implementation is rejected by the added guard.

This is narrower than saying revision 1 had no controls: the revision commit contains many real, strong control receipts. It is also **not** evidence that the product fails or that a counter changed after freeze. `claims.json:10` requires each revision to be committed with the control receipt that forced it; the whole revision does carry such receipts. What cannot be certified is the assignment's stronger per-change proposition, or a description of every hunk as an experimentally forced repair.

**Evidence and commands.** I inspected the complete counter delta with:

```sh
timeout 30s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone diff --no-ext-diff --no-textconv --unified=3 f0173481 e6a61e82 -- reports/round-62/accept-d.py reports/round-62/accept-o.py
```

The changed code is at final `accept-o.py:419-434` (default registry), `:468-470` (default exit/summary), `:481-487` (ERR), and `:275-286,488-494` (process-group/cleanup hardening). The per-change evidence map below covers the remaining hunks.

The following are the complete substantive contents of the relevant inspected report range, `.ufo/waves/round-62/w1/CriticClaims.md:54-67` (source inspection, **not an executed control**):

> ### 3. High — O's DEFAULT leg accepts the wrong default exit and cannot establish the promised retry schedule
>
> **Counterexample.** **[INFERENCE; not scored here]** A tool that behaves correctly for explicit flags but returns exit 0 after printing the expected default DEAD row still satisfies DEFAULT. So does one that issues nine DEAD requests without three 60-second-separated passes, then delays until the permitted wall-time interval. Both skip a specifically promised default behavior while leaving the other runs unchanged.
>
> **Evidence.** `accept-o.py:364-371` captures `code4`, but DEFAULT uses only parsed row, wall time 100–600 seconds and total hits 9. It neither checks `code4 == 1` nor the default summary, nor timestamps/spacing of requests. EXIT (`:338-348`) checks different, explicit `--passes 3 --gap 0` invocations. The tool contract promises exit 1 for a non-LOCATED row and three passes with gap 60 (`:22-40`).
>
> Two further cheap omissions are accepted by the current checks:
>
> - A tool may print `url=-` for every match: `parse()` (`:240-246`) discards the captured URL entirely.
> - A tool may require `--registry` and omit its default `corpus/SOURCES.md` behavior: all valid, private, default-retry and error invocations supply `--registry` (`:311,346,359,368,375-380`). The DEFAULT leg tests retry defaults, not the registry default.
>
> **Impacted axes.** Operability and calibration. These are checks missing for already stated behavior, not requests for additional product scope.
>
> **Smallest safe correction.** Before data, check default exit and summary; record server timestamps and test the promised schedule with an appropriate scheduling tolerance; retain and compare verdict URLs; add one copied-tree call with a real `corpus/SOURCES.md` and no `--registry`. Keep the default-registry test distinct from retry defaults. I requested existing control evidence from CtlODefault; no published result was available during this review, so none is claimed.

`MutCounterO.md:168-170` expressly introduces its remaining robustness findings as read-only source/fixture findings, not additional mutation probes or observed frozen acceptance. Its `:219` calls stdout traceback/prefix escape an inference; `:225-226` calls descendant survival an inference and says no full timeout/leak scenario was induced. The reserved-port and malformed-markup changes have actual diagnostics (`:175`, `:189-195`); do not incorrectly group those with wholly unobserved scenarios.

**Strongest local check against treating all revision-1 changes as detector-only fixes.** The caption widening changes the contract itself: an honest revision-0 tool passes the old counter and fails the new counter solely on the newly defined thumbnail/gallery classes. These are complete historical outputs, not my execution:

Original command recorded at `CtlONoRetry.md:24-30`, with cwd its scratch clone:

```sh
timeout 900 env TMPDIR=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoRetry/tmp_<case> PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-62/accept-o.py; echo exit=$?
```

Original honest output (`CtlONoRetry.md:227-246`):

```text
=== CASE honest (canonical, clone slot, no --root)
bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  reports/round-62/accept-o.py
052628ffd0599455929d5c27bd4f498dac8fdaf233b1f2ae8a4f8044b15a1164  tools/reopen-row.py
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S3508', 'REFUSED', 0), ('S7057', 'REFUSED', 0), ('S8376', 'REFUSED', 0)]
DEFAULT PASS rows=[('S8004', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

Rescore command/output (`telemetry/controls-rescore.txt:300-313`):

```text
## CtlONoRetry-honest
$ python3 -B accept-o.py (revision 1, sha256 a222a156b95e0f716f0304c85bc38c2eb395f5dad5c9b4810476a87237ca8ba9)
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=53 wrong=4 ["CAP_CLASS_GALLERY:S8355:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_CLASS_THUMB:S1821:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_CLASS_THUMB:S3158:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_CLASS_GALLERY:S4327:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]"] summary_ok=False exit=1
ORDER PASS printed=53 expected=53 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S5331', 'REFUSED', 0), ('S6470', 'REFUSED', 0), ('S2473', 'REFUSED', 0)]
DEFAULT PASS rows=[('S6948', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
RECEIPT L1-rescore/CtlONoRetry-honest counter-sha256=a222a156b95e0f716f0304c85bc38c2eb395f5dad5c9b4810476a87237ca8ba9 rev=revision-1 frozen=FAIL exit=1 stopped-by=GEN
```

`CtlONoArchive.md:230-251` independently identifies the same distinction: widening `caption` to `caption`/`thumbnail`/`gallery` is a contract change, not an implementation hole under revision 0. The final claims and counter disclose the widened rule. This is therefore not a demonstrated concealed goalpost move or product regression; it is a pre-data semantic revision whose provenance must not be misrepresented as killing a revision-0 work-skipping control.

**Impacted axes:** calibration of control provenance; operability evidence for the added error/default/lifecycle checks. No demonstrated depth harm follows.

**Smallest safe correction:** preserve the frozen counters and first-run receipts. Describe which changes were control-forced, diagnostic-backed, static-only, or deliberate contract changes. If genuinely pre-data forcing receipts exist, cite those original receipts; do not create new runs and backdate their evidentiary role. Otherwise record the per-change control-evidence gap honestly. Whether that gap is fatal under the canonical claim-sizing rule is for the Rust judge/operator, not this seat. New post-data tests cannot retroactively establish pre-data control provenance.

## (a) Complete commit range and freeze integrity — HOLDS

Clone/checkout command used (all foreground and timeout-capped):

```sh
timeout 20s mkdir -p /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze && timeout 120s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone && timeout 30s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone checkout -q a2c5caa59b2d67ce35e53d6ce0217030a66cdd48
```

Output: empty; command completed.

The range is exclusive of `f0173481` and inclusive of the measured revision. Command and complete stdout:

```sh
timeout 30s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone log --reverse --format='COMMIT %H%nAUTHOR %aI%nCOMMITTER %cI%nSUBJECT %s' --name-status f0173481..a2c5caa59b2d67ce35e53d6ce0217030a66cdd48
```

```text
COMMIT e6a61e8225bc4ab2a394e14f96a92021c03d9f03
AUTHOR 2026-10-23T09:04:21-03:00
COMMITTER 2026-10-23T09:04:21-03:00
SUBJECT round-62: instruments revision 1 (before any data) forced by the wave-1 control receipts; LOCATE paired control; L1 re-score receipts; wave-1 spec, registry and 37 seat reports

A	.ufo/waves/round-62/gen-w1.py
A	.ufo/waves/round-62/w1-spec.json
A	.ufo/waves/round-62/w1/ConnectSiblings.md
A	.ufo/waves/round-62/w1/CriticClaims.md
A	.ufo/waves/round-62/w1/CriticFetchRule.md
A	.ufo/waves/round-62/w1/CtlDCaptureShapes.md
A	.ufo/waves/round-62/w1/CtlDDeadEcho.md
A	.ufo/waves/round-62/w1/CtlDDeleteMove.md
A	.ufo/waves/round-62/w1/CtlDDoNothing.md
A	.ufo/waves/round-62/w1/CtlDFabricated.md
A	.ufo/waves/round-62/w1/CtlDHonest.md
A	.ufo/waves/round-62/w1/CtlDInputs.md
A	.ufo/waves/round-62/w1/CtlDJunkTokens.md
A	.ufo/waves/round-62/w1/CtlDMarkOnly.md
A	.ufo/waves/round-62/w1/CtlDOffTopicRow.md
A	.ufo/waves/round-62/w1/CtlDQuoteDump.md
A	.ufo/waves/round-62/w1/CtlDRegistryEdits.md
A	.ufo/waves/round-62/w1/CtlOAlwaysLocated.md
A	.ufo/waves/round-62/w1/CtlODefault.md
A	.ufo/waves/round-62/w1/CtlODoNothing.md
A	.ufo/waves/round-62/w1/CtlOHonestRef.md
A	.ufo/waves/round-62/w1/CtlOKeyed.md
A	.ufo/waves/round-62/w1/CtlONoArchive.md
A	.ufo/waves/round-62/w1/CtlONoRetry.md
A	.ufo/waves/round-62/w1/CtlOOrderErr.md
A	.ufo/waves/round-62/w1/CtlORawSubstring.md
A	.ufo/waves/round-62/w1/CtlOUnbounded.md
A	.ufo/waves/round-62/w1/ExecReopenTool.md
A	.ufo/waves/round-62/w1/MutCounterD.md
A	.ufo/waves/round-62/w1/MutCounterO.md
A	.ufo/waves/round-62/w1/ReviewDryRun.md
A	.ufo/waves/round-62/w1/ScoutCaptionRows.md
A	.ufo/waves/round-62/w1/ScribeHedgeOpen.md
A	.ufo/waves/round-62/w1/ScribeHeelCaption.md
A	.ufo/waves/round-62/w1/ScribeIntake.md
A	.ufo/waves/round-62/w1/ScribeMistakes.md
A	.ufo/waves/round-62/w1/ScribeQuality16.md
A	.ufo/waves/round-62/w1/ScribeTalariaMW.md
A	.ufo/waves/round-62/w1/ScribeTalariaRef.md
A	.ufo/waves/round-62/w1/swarm-registry.json
M	reports/round-62/accept-d.py
M	reports/round-62/accept-o.py
A	reports/round-62/locate-control.py
A	reports/round-62/telemetry/controls-rescore.txt
A	reports/round-62/telemetry/locate-control.txt
COMMIT 9143fc442c209f6fd832bc7bf53ef5c0cd161ea1
AUTHOR 2026-10-23T09:04:21-03:00
COMMITTER 2026-10-23T09:04:42-03:00
SUBJECT round-62: freeze — claims and separability manifest at revision 1, revision-1 declaration dry-run

M	reports/round-62/claims.json
M	reports/round-62/separability-manifest.json
A	reports/round-62/telemetry/declaration-dry-run-rev1.txt
COMMIT e605603c1ea6b005c3bc2ad8ba1939bc75e8acd5
AUTHOR 2026-10-23T09:04:51-03:00
COMMITTER 2026-10-23T09:04:51-03:00
SUBJECT round-62: claim O — tools/reopen-row.py (bounded row re-opener with archived fallback and caption verdict; built by seat ExecReopenTool)

A	tools/reopen-row.py
COMMIT a2c5caa59b2d67ce35e53d6ce0217030a66cdd48
AUTHOR 2026-10-23T09:05:04-03:00
COMMITTER 2026-10-23T09:05:04-03:00
SUBJECT round-62: claim D — footwear lines 63/74/75/93 repaired in place (open list, caption attribution, hedge, talaria on S693); S693 registered; S687 used-by -> —

M	corpus/SOURCES.md
M	corpus/knowledge/culture-material/footwear-codes-terminology.md
```

Only `e6a61e82` changes the two counters in that range. After `9143fc44`, only O's product file and D's two product files change. The freeze commit changes the declaration/manifest and adds the dry-run receipt, not either counter.

Identity command and complete stdout:

```sh
timeout 30s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone rev-parse 9143fc44:reports/round-62/accept-d.py a2c5caa59b2d67ce35e53d6ce0217030a66cdd48:reports/round-62/accept-d.py 9143fc44:reports/round-62/accept-o.py a2c5caa59b2d67ce35e53d6ce0217030a66cdd48:reports/round-62/accept-o.py && timeout 20s sha256sum /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone/reports/round-62/accept-d.py /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone/reports/round-62/accept-o.py
```

```text
e4dd304d80f7767b9c8915de1418425c89348955
e4dd304d80f7767b9c8915de1418425c89348955
be8a01d8197683662a26ccac08d701562e6e4670
be8a01d8197683662a26ccac08d701562e6e4670
0f60162532192c8e66054df1f6ce82edd6633e4413414810bd1fe1a188847f3a  /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone/reports/round-62/accept-d.py
a222a156b95e0f716f0304c85bc38c2eb395f5dad5c9b4810476a87237ca8ba9  /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone/reports/round-62/accept-o.py
```

Those SHA-256 values match `claims.json:246-247` and the supplied final-measures header. Thus no counter substitution between freeze and measured object is visible in Git.

**Severity:** informational / attempted freeze falsification did not succeed. **Impacted axes:** calibration, verification provenance. **Smallest correction:** none to these frozen bytes; retain their identities in the eventual filed evidence.

## (b) First runs on the claimed objects — no earlier prohibited run found

### Build-seat audit

I read each requested report in the pinned clone, including both `ScribeTalaria*.md` files, rather than treating a text match for `ACCEPT` as execution:

| Report | Observed execution / explicit limit | Earlier claimed-object counter run? |
|---|---|---|
| `ExecReopenTool.md:19-24,69-150,152-189` | Own selftest, independently authored `contract_probe.py`, and direct live tool run on S665/S671. Explicitly says `accept-o.py` was not run against the build. | None recorded. The independent probe is earlier behavioral evidence, not an invocation of the reserved counter. |
| `ScribeTalariaMW.md:45-66` | Two round-61 base-locator calls, live and archive, for the Merriam-Webster candidate. Explicitly no ACCEPT-D run. | None recorded. |
| `ScribeTalariaRef.md:28-49` | Two base-locator calls for Cambridge's candidate, live and archive. Explicitly no ACCEPT-D counter. | None recorded. |
| `ScribeHedgeOpen.md:9-19,25-56` | Two base-locator calls and manual LINK/COPY arithmetic. Explicitly not an ACCEPT-D run and other legs unexercised. | None recorded. |
| `ScribeHeelCaption.md:30-36,56-73` | Three base-locator calls and inferred manual arithmetic. Says only those locator invocations ran; no `accept-d.py`, ACCESS/LINT, or bounded row locator. | None recorded. |

The wave-1 build brief in `w1-spec.json:207` expressly prohibits `ExecReopenTool` from running `accept-o.py` on its tool while requiring its selftest and direct live run. Consequently the mandated direct live observation is not itself evidence of a forbidden reserved-counter run. The earlier independent harness is openly disclosed, not hidden. Whether a broader interpretation of “any seat has scored” should encompass such development probes is a canonical interpretation question; it is not proof that the specifically forbidden counter ran.

I also searched all committed wave-1 reports and round-62 report artifacts for the landed new source URL, exact new line-93 wording, exact new caption/attribution wording, and the build hash. The exact-string grep used was:

```text
pattern: dictionary\.com/browse/talaria|Talaria are the wings or winged sandals worn|A Bata Shoe Museum image caption says|According to the BBC article|1aeb175bce9203f8273ac6b1280f05642480df281e5dc9845c3280d0cd00797f
paths: <clone>/.ufo/waves/round-62/w1 ; <clone>/reports/round-62
```

Complete match set: only `ExecReopenTool.md:12`, its delivered build SHA-256. No final D wording/URL match was returned. This is a bounded search of recorded artifacts, not proof that an unrecorded execution is impossible.

The D positive controls are not the landed D object: `CtlDHonest.md:26-56` uses a Gutenberg/Smith row and different four-line wording; `CtlDMarkOnly.md:49-68` uses World History Encyclopedia; `CtlDCaptureShapes.md:23-60` uses Wikipedia. Their use of the fixture id S693 must not be confused with the later Dictionary.com S693 object. The O honest controls are independently authored stand-ins, not the build tool (`CtlOHonestRef.md:18` reports SHA-256 `03aa4c4c57d3c6d31f783bb27bc60e67e5978b9cc472837533e286ed5c3c59b7`).

The candidate identity command and complete stdout were:

```sh
timeout 20s sha256sum /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone/tools/reopen-row.py /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone/corpus/knowledge/culture-material/footwear-codes-terminology.md /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone/corpus/SOURCES.md
```

```text
21e2d7679a65dc81c89e4905e268b00199caa5f0b3b400caa58da5f7f614b803  /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone/tools/reopen-row.py
0dd8a644b4c27d4a46d3bebe4fd52ce21fb038d3b56164b1113a702599084b79  /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone/corpus/knowledge/culture-material/footwear-codes-terminology.md
9183b40083b59429edece68d8560eb58aa9fc1cfa1a25d0fefc9c67906505dec  /fast/scratch/hyaku/kotodama-r62/resid/ResidCriticFreeze/clone/corpus/SOURCES.md
```

The initial executor build hash differs from the landed tool hash; I do not assert it landed byte-unchanged. The actual counter identities and measured revision, not the builder's earlier selftest, bind the final receipt.

### Timeline and authoritative receipt

- Revision-0 dry-run at `10:51:06Z`: D has `differ=[]`, no S693, and O has no tool (`declaration-dry-run.txt`). These are do-nothing controls, not claimed-object runs.
- Revision-1 rescore header: `12:04:05Z`, independent fixture clones (`controls-rescore.txt:1-4`).
- Instrument commit: `12:04:21Z`.
- Revision-1 declaration dry-run: `12:04:37Z`; again D has `differ=[]`, no new row, O absent (`declaration-dry-run-rev1.txt:1-33`).
- Freeze commit: `12:04:42Z`.
- O product commit: `12:04:51Z`; D product commit: `12:05:04Z`.
- Supplied authoritative receipt starts `12:05:13Z`; D finishes `12:05:14Z`, O finishes `12:07:44Z`.

Complete supplied receipt, read from `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-62/telemetry/final-measures.txt:1-36` (the receipt is produced after the measured product tip and was read from the lane, not misrepresented as a blob in the measured clone):

```text
# round-62 final measures: the first and sole authoritative runs of each frozen counter on its claimed object
# measured revision: a2c5caa59b2d67ce35e53d6ce0217030a66cdd48 (lane main = origin per jj-lane.sh state: state branch=main local=a2c5caa59b2d67ce35e53d6ce0217030a66cdd48 remote=a2c5caa59b2d67ce35e53d6ce0217030a66cdd48 ahead=0 behind=0 head=detached tracked=0 untracked=1 )
# counters: accept-d.py 0f60162532192c8e66054df1f6ce82edd6633e4413414810bd1fe1a188847f3a, accept-o.py a222a156b95e0f716f0304c85bc38c2eb395f5dad5c9b4810476a87237ca8ba9 (frozen at 9143fc44); started 2026-10-23T12:05:13Z
$ python3 -B reports/round-62/accept-d.py
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
KEEP PASS bad=[]
FRESH PASS reused=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T12:05Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
# finished 2026-10-23T12:05:14Z
$ python3 -B reports/round-62/accept-o.py
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=53 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=53 expected=53 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S1893', 'REFUSED', 0), ('S6592', 'REFUSED', 0), ('S7009', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1750', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
# finished 2026-10-23T12:07:44Z
```

**Severity:** informational; no earlier prohibited counter run is established by the inspected records. **Impacted axis:** calibration. **Smallest correction:** preserve this first-run attribution; do not label earlier locator probes or stand-in controls as data runs, and do not claim this artifact audit proves absence of every possible unrecorded execution.

## (c) Per-change evidence map

All wave-1 report paths in this table are beneath `.ufo/waves/round-62/w1/`; rescore ranges are in `reports/round-62/telemetry/controls-rescore.txt`.

| Revision-1 change | Local evidence | Assessment |
|---|---|---|
| D SET/APPEND read bytes without universal-newline translation | `MutCounterD.md:7-11,114-135,212-228`: CR on unrelated line 1 survives SET; byte oracle detects it | Exercised **leg-level** forcing witness; full D still FAIL, not a whole-control survivor |
| D NOMARK clause shape/comment/bracket restrictions; OPEN/HEDGE/CAPTION/LINK/COPY operate on the clause | `CtlDMarkOnly.md:32-47`; rescore `116-202` | Whole-predicate old survivors and new rejection receipts; well backed |
| D KEEP >=60% retained base content | `CtlDJunkTokens.md:39-48,149-170`; rescore `182-202` includes a KEEP failure on the parenthetical-mark specimen | Original token-salad **leg** survivor, not a full PASS; no exact junk rescore is in the matrix |
| D FRESH URL disjointness/canonicalization | `CtlDRegistryEdits.md:13-19,39-40,55-58`; rescore `226-246` | Literal reuse is exercised and stopped at FRESH; the full normalization equivalence space is not exhaustively tested |
| D SOLE footwear TOPIC rule | `CtlDOffTopicRow.md:8-13,80-138`; rescore `204-224` | Located Hermes-spaceplane full survivor stopped solely by SOLE |
| D ROWS same-page/past-dated capture shape | `CtlDCaptureShapes.md:62-88`; `CtlDFabricated.md:10-16`; rescore `6-70,94-114` | Exercised malformed-capture survivors and new rejection receipts |
| D ROWS capture within first-four-URL budget | `CriticFetchRule.md:55,66` | Static, explicitly unexecuted boundary construction; no such five-URL case in the rescore matrix |
| D APPEND malformed inserted S-prefixed rows | `CtlDRegistryEdits.md:36,42,55`; rescore `248-268` | Original all-PASS calibration exposes S650b. Rescore rejects APPEND but starts with unrelated base failures too; do not call that isolated mutant killing |
| D LOCATE loop factored into `locate_row` and new paired control | `CriticFetchRule.md:53,57-68`; `telemetry/locate-control.txt:1-20`; declaration dry-run `37-45` | Actual recovery/exhaustion/absence/first-success/fallback/DNS control receipt, plus PASSES=1 sensitivity witness |
| O ORDER repeated arguments | `CtlOOrderErr.md:16,24-27`; rescore `315-343` | Old deduplication full survivor; caption-adjusted honest-reference mutant fails ORDER alone |
| O GEN matched URL comparison | `CtlOUnbounded.md:96-102`; rescore `360-373` | Old url=- full survivor; new GEN rejects |
| O BOUND stop after live BODY match | `CtlOUnbounded.md:22-30,43-74`; rescore `390-403` | c5 full survivor; new BODY_THEN_ARCHIVE catches extra request |
| O BOUND unlisted fixture paths | `CtlOUnbounded.md:40,56-76`; rescore `375-388` | c11 full survivor; new BOUND reports `/__aux_overfetch` |
| O DEFAULT burst timing and upper/lower bounds; per-attempt 4-10s waits | `CtlODefault.md:10-38`; `CtlONoRetry.md:55-105`; rescore `285-298,405-448` | Real old schedule survivors and new isolated timing failures; well backed |
| O DEFAULT exit and summary | `CriticClaims.md:54-67`; `MutCounterO.md:207-213` | Source-backed inference; no isolated exercised forcing receipt found |
| O EXIT default registry path | `CriticClaims.md:60-67` | Source-backed inference; positives exercise it, but no defective-default-path control receipt found |
| O DEAD_PORT reservation | `MutCounterO.md:172-178` | Actual immediate-rebind diagnostic; not a full counter race-failure receipt |
| O balanced BODY_SPLIT markup | `MutCounterO.md:187-197` | Actual deterministic malformed-markup diagnostic; not an observed wrong text verdict |
| O deterministic caption attributes and caption id class | `MutCounterO.md:199-205` | Attribute-set diagnostic plus definite source coverage gap; no attribute-specific bad tool was scored there |
| O ERR anchored prefix and traceback inspection on both streams | `MutCounterO.md:215-219` | Explicit inference, not an exercised escape/forcing receipt |
| O owned process groups and nested cleanup | `MutCounterO.md:221-226` | Explicit inference; no timeout/leak scenario induced |
| O thumbnail/gallery caption semantics and corresponding classes | `ExecReopenTool.md:152-183`; `CtlONoArchive.md:230-251`; rescore `300-313,345-358` | Direct live observation and measured rejection of old honest controls. A disclosed contract revision, not proof those old controls violated revision 0 |
| Declaration's added clause mapping/revision notes; lowest-axis clarification | `CriticClaims.md:81-104`, final `claims.json:239-249` | Explanatory/provenance changes; they do not create measured improvement or establish a lowest-axis waiver |
| Separability manifest base d42ffb89 -> e6a61e82 | `CriticClaims.md:69-79`; `declaration-dry-run-rev1.txt:34-36`; freeze diff | Source/tree-backed harness correction. The prelanding dry-run still stops at the absent O product, not a dynamic separability PASS. D's content BASE remains d42ffb89 |

The table separates an old full-predicate survivor, a leg-level witness, a diagnostic, an inference, and a semantic revision. Combining them all under “controls forced every change” loses precisely the provenance distinction this seat was assigned to attack.

## (d) Axis naming and claim sizing — names fit; no broader result follows

Authority read: `/home/vgpnk/Projects/shokunin/.ufo/prompts/kotodama-round-62.md:343-365`, especially `:361-365`; fleet/canonical `AXES.md:9-16,20-23`; canonical `LEARNING.md:31-35,84-90`.

**Strongest axis-misfit hypothesis:** D merely re-scores held rules on new rows, and O merely renames the old locator. The actual committed deltas contradict that as a complete description:

- `a2c5caa5` changes the actual knowledge assertions: line 63 reopens the country list; line 74 scopes the assertion to the museum caption; line 75 restores attribution/“we have”; line 93 changes “winged leather boots” to the new sourced lexical wings/winged-sandals assertion. These are not just scorecard edits or another LINK score. Depth expressly includes cited verifiable detail. Quality is also the **trend** served by depth, not an alternative expertise axis that automatically excludes all substantive corrections from depth. This supports the *name*, not a semantic PASS on the wording.
- `e605603c` adds `tools/reopen-row.py`, absent at the instrument base and in both declaration dry-runs. The old `reports/round-61/reopen-quote.py` existed, so the novelty must be bounded configurable reopening and body/caption behavior in a durable lane tool, not invention of quote location itself. This is a runnable-artifact surface, appropriately operability, not depth by fixture count.
- D's “each” ranges over four named lines and a finite new-id block; O's acceptance ranges over the generated local fixture and named default/error/order calls. Their PASS labels do not establish all possible page, network, DNS, privacy or semantic-support behavior. `claims.json` expressly retains live O behavior and D semantic support/body provenance as review-only. The final O fixture reports 53 GEN rows; the count is not itself the acquired capability.
- The do-nothing before-state cannot meet either declared target: revision-1 declaration dry-run has D `differ=[]`, S687/no S693 and final FAIL; O has no tool and final FAIL. These are committed at the freeze, before either product commit.
- The manifest baseline correction does not relabel D's historical content comparison; counterfactual instrument base e6a61e82 and content base d42ffb89 serve different purposes.

**Remaining limitation, not a new axis-name defect:** `claims.json:239` now honestly says freshness is historically lowest and paused, no next-lowest ranking is established, and a ranking/waiver is the operator's call. Correctly naming D and O does not discharge the separate lowest-axis obligation or prove saturation. No such waiver is inferred here.

**Severity:** informational / no categorical axis misnaming established. **Impacted axes:** depth, operability, calibration. **Smallest safe correction:** retain surface-specific language; do not promote mechanical D PASS to whole-entry admission, O fixture PASS to universal live correctness, a registry row count to depth/coverage, or the unresolved lowest-axis note to a waiver.

## Execution accounting

- Only tools already present were used; installs/updates: **none**.
- Git writes were confined to creating/checking out this seat's permitted sandbox clone. All subsequent Git use was read-only there; nothing changed in the lane/fleet Git or jj state.
- All shell processes were foreground, timeout-capped at 120 seconds or less, and completed. No background job, service, child runtime, or process tree was left running.
- The only lane write by this seat is this write-once report. No source, counter, claim, receipt, or peer-owned report was edited.
