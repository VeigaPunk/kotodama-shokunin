# CriticFreezeC — read-only timeline and provenance review

## Scope and axes

Seat: `KotodamaR61.CriticFreezeC`. Measured revision: `efbee29cd8c0872a4fb89db34c489d4a9960916c`; freeze: `2f4f8a4027912f7f6e821fc5180f279e08936174`.

Axes: **calibration**, **instrument identity/reproducibility**, **control provenance**, and **predicate/timeline integrity**. Coverage (C) and operability (O) are the claims under examination, not new claims made by this review.

The freeze-to-measure byte identity and ordering survive this attack. I found documentation/receipt-provenance inconsistencies below, not evidence of a pre-freeze full acceptance run on the actual claimed object. The existing measurement remains exactly as recorded: `reports/round-61/telemetry/final-measures.txt:16-19` records C's LOCATE 40/41 and FAIL/1; `:20-28` records O's PASS/0. No counter was run for this review, and no later diagnostic or dependency check replaces that receipt.

## Required checks

### 1. Commit sequence and frozen bytes

Executed the requested read-only commands, each under `timeout 60s`:

```text
git log --format='%h %cI %s' 942abdf4..efbee29cd8c0872a4fb89db34c489d4a9960916c

efbee29 2026-10-23T06:57:31-03:00 round-61: claim C lands the footwear entry, S652-S692 and its README index row
675d59a 2026-10-23T06:57:29-03:00 round-61: claim O lands tools/check-cited-lines.py (clause-scoping lint, R60-M6 fix)
2f4f8a4 2026-10-23T06:53:16-03:00 round-61: instruments revision 1 (freeze) forced by the pre-data control wave; control receipts and L1 re-score
78ad4b1 2026-10-23T05:26:01-03:00 round-61: separability manifest and declaration dry-run receipt (revision 0)
106df39 2026-10-23T05:24:34-03:00 round-61: instruments revision 0 (accept-c, accept-o, locator copy, claims, base list, census start)
```

```text
git diff --stat 2f4f8a4027912f7f6e821fc5180f279e08936174 efbee29cd8c0872a4fb89db34c489d4a9960916c -- reports/round-61/

[empty output]
```

Independent `git ls-tree -r` reads of both revisions returned identical blobs for the entire committed `reports/round-61/` subtree, including:

| Path | Blob at BOTH revisions |
|---|---|
| `reports/round-61/accept-c.py` | `7f79e8677c824c7dfc33c275eb6ac9db9ffab3de` |
| `reports/round-61/accept-o.py` | `e709a11f01c0f8b904a7d4350964bf9fd6f49fcd` |
| `reports/round-61/reopen-quote.py` | `e72e9368ea260be7deb6ac82c785e6f4b1f93b2a` |
| `reports/round-61/claims.json` | `391ba86510a43e3d38765a2e1b2cd7021b496737` |
| `reports/round-61/telemetry/controls-c-rescore.txt` | `e8c07091f69d218e28fb476a899c865bc84eb48e` |
| `reports/round-61/telemetry/controls-o-rescore.txt` | `ebeceea9c28b1fa8d4a86dd0d15322b5c433290b` |

Thus the counters and locator are byte-identical from freeze to measured revision. This also corroborates the identity statement in `reports/round-61/telemetry/final-measures.txt:2`. The final measurement receipt was produced after landing; its absence from those historical trees is not instrument drift.

### 2. What happened before the first full measurement

I inspected the L1 transcript, not just commit dates. For precise audit anchors, `L1JSON` below denotes this existing read-only transcript:

`/home/vgpnk/.omp/agent/sessions/-Projects-shokunin/2026-10-23T06-27-20-968Z_01a16771-4d08-7011-958e-0f9940db87a7/KotodamaR61.jsonl`

| UTC time | Observed action | Evidence |
|---|---|---|
| 08:25:55 | Revision-0 declaration dry run; actual entry/rows and tool absent | `reports/round-61/telemetry/declaration-dry-run.txt:1-3,4-6,20-28` |
| 09:51:58 | Revision-1 C controls rescored on named independent scratch fixtures, with FLOOR=1 probe | `reports/round-61/telemetry/controls-c-rescore.txt:1-2`; `L1JSON:447-449` |
| 09:53:04 | Revision-1 O controls rescored on fake/honest control tools in a clone | `reports/round-61/telemetry/controls-o-rescore.txt:1-3` |
| 09:53:16 | Freeze commit | requested git log; `L1JSON:462-464` records its landing |
| 09:54:17 | Actual draft build and self-check starts; initial output contains draft defects | `L1JSON:486-490`; `/fast/scratch/hyaku/kotodama-r61/L1/build.py:7-12,87-108` |
| 09:56:57 | Entry/rows/index assembled; README sweep run | `L1JSON:523-527` |
| 09:57:05 | Access checker, locator `--row` for S652/S660/S662, and cited-line lint run | `L1JSON:528-530`; locator outputs three LOCATED lines |
| 09:57:29 / 09:57:31 | O / C land | requested git log |
| 09:57:40 | Full measured acceptance commands start | `L1JSON:545-547`; `reports/round-61/telemetry/final-measures.txt:1-3,20` |

**Interpretation under the actual rule:** `reports/round-61/claims.json:11` ties revision permission to the first run of **that counter on the claimed object**; `:22` makes the first **full** `accept-c.py` run at the measured revision authoritative. `reports/round-61/accept-c.py:265-269` implements the aggregate label and status. The three row-mode locator checks return LOCATED/NOT_LOCATED (`reports/round-61/reopen-quote.py:234-254`), not an `ACCEPT-C-61` aggregate. The access checker and sweep are component checks, not full C acceptance. All these pre-landing checks occurred AFTER the freeze anyway.

The build self-check goes further than the three checks named in the assignment: it imports the counter module and calls its topic/LCS/copy helpers on drafts (`build.py:7-12,92,101-108`). That is genuine partial data feedback, not blind evaluation, but it is also after the freeze, with no subsequent instrument revision. It does not establish an early freeze breach. The phrase “before any data” must not be inflated into “before any source research or component checks”; the narrower parenthetical in `claims.json:26` concerns the acceptance counter. No full acceptance run on the actual draft before the freeze appears in the inspected L1 execution history. Pre-freeze controls sharing the entry pathname in separate fixtures are not thereby the actual claimed entry and rows.

### 3. Do the revision notes name their receipts?

**Yes, literally:** `reports/round-61/claims.json:26` names `reports/round-61/telemetry/controls-c-rescore.txt`; `:36` names `reports/round-61/telemetry/controls-o-rescore.txt`. Those files and the original wave-1 control reports were included in the freeze commit. However, the two aggregate rescore files do not themselves contain the forcing case for every listed change (F1), and the C probe hash needs the qualification in F2.

## Findings: counterexample, evidence, impacted axes, smallest safe correction

### F1 — aggregate rescore references are not an exhaustive per-change provenance map

**Counterexample:** follow the receipt named by C's revision note for the NFKC/spaced-ID change, copied-URL change, or private-host change. None of `CtlCMultiId`, `CtlCCopiedRows`, or `MutCounterC` has a case in the named C rescore. Likewise the O rescore has no `CtlODoNothing/l-no-args-exit-zero` case for the new no-arguments guard.

**Evidence:**

- `reports/round-61/claims.json:26,36` supply the change attributions and only the aggregate rescore paths.
- C's complete named rescore is `reports/round-61/telemetry/controls-c-rescore.txt:1-205`: its cases cover JunkLines, OffTopic, HonestHtml/Pdf, QuoteDump, Fabricated and EchoUrls, not the three controls above. The last case begins at `:189` and ends at `:205`.
- O's complete named rescore is `reports/round-61/telemetry/controls-o-rescore.txt:1-47`: honest, g-lookalike, keyed-c, keyed-a2, fake-selftest. Passing `noargs_exit=2` on those other tools does not rescore the known no-args mutant.
- The actual forcing evidence DOES exist and was co-committed at the freeze: `.ufo/waves/round-61/w1/CtlCMultiId.md:16-18,90-91`; `CtlCCopiedRows.md:5-9,80-81`; `MutCounterC.md:17,75,96`; `CtlODoNothing.md:5,23,43,56`.
- The later summary `corpus/lessons/round-61.md:32` says the L1 “re-scored the met fixtures” without limiting that statement to the retained subset.

**Impacted axes:** calibration and control provenance. This is NOT evidence that the revision lacked forcing controls or that `predicate_rule`'s co-commit requirement was violated: the original receipts are in the freeze. It is a defect in treating the aggregate rescore as exhaustive evidence behind each change.

**Smallest safe correction:** in the round's record-only explanation, map each change directly to the original forcing receipt above and call the aggregate rescores a subset. Do not assert an unrecorded revision-1 rejection of the omitted cases. No new acceptance run or frozen-file change is needed.

### F2 — C rescore hashes the logical probe, not the relocated file actually executed

**Counterexample:** the C rescore header identifies a FLOOR-only probe by SHA-256, but the recorded command makes another transformed file and executes that file.

**Evidence:** `reports/round-61/telemetry/controls-c-rescore.txt:1` records probe `1a741a371b34ec2e9570fd383b78c75f62ebb58669c07512a86bc780153e8ac9`, described as “FLOOR 20 -> 1 only.” A bounded `sha256sum` of the retained `/fast/scratch/hyaku/kotodama-r61/L1/accept-c-r1-probe1.py` returned exactly that digest; its `:73-74` contain FLOOR=1 and the original locator pathname. But `L1JSON:447` records:

```text
cp .../reopen-quote.py <fixture>/reports/round-61/reopen-quote.r1.py
sed 's#reports/round-61/reopen-quote.py#reports/round-61/reopen-quote.r1.py#' L1/accept-c-r1-probe1.py > <fixture>/reports/round-61/accept-c.r1p1.py
... python3 -B reports/round-61/accept-c.r1p1.py
```

The subsequent cleanup removes that executed file. Its LOCATOR value differs from the hashed template. The locator itself was copied unchanged; this is not evidence of a behavioral counter relaxation beyond FLOOR, nor drift in the measured instruments. It is a byte-provenance distinction missing from the header.

**Impacted axes:** reproducibility and calibration.

**Smallest safe correction:** annotate the record that the listed digest is the logical FLOOR-only template, disclose the locator-path relocation and same-byte locator copy, and do not call that digest the exact executed-file hash. Do not invent a historical observed checksum for the deleted derivative or rewrite the frozen receipt.

### F3 — the entry names revision-0 instruments as its verification provenance

**Counterexample:** `corpus/knowledge/culture-material/footwear-codes-terminology.md:8` says it was written on round-61 instruments `78ad4b17`, while the actual frozen instruments used for the measurement are `2f4f8a40`.

**Evidence:** the requested git log identifies `78ad4b1` as the revision-0 declaration dry run, and `2f4f8a4` as revision 1/freeze. `reports/round-61/telemetry/declaration-dry-run.txt:1` explicitly calls its instruments revision 0; `final-measures.txt:1-2` identifies the measured revision and frozen revision-1 hashes. `corpus/lessons/round-61.md:3` also correctly distinguishes these revisions.

**Impacted axes:** calibration and instrument provenance; not the observed C result.

**Smallest safe correction:** append a record-only correction naming declaration/dry-run `78ad4b17`, instrument freeze `2f4f8a40`, measured entry `efbee29c`, and the final receipt. Leave the already-measured entry bytes untouched during this review/adjudication.

### F4 — locator usage examples invoke the old round's instrument

**Counterexample:** following the round-61 locator's documented example actually runs `reports/round-57/reopen-quote.py`, not the frozen round-61 copy.

**Evidence:** `reports/round-61/reopen-quote.py:4-5` name round 57 for both URL/quote and `--row` examples, despite `:2` identifying revision-1 additions in the round-61 copy. `reports/round-61/accept-c.py:74` correctly names the round-61 locator. The actual pre-landing commands in `L1JSON:528` also used round 61.

**Impacted axes:** reproducibility and provenance. This stale example did not change the observed measurement or its byte identity.

**Smallest safe correction:** give the correct round-61 invocations in the closing record/erratum; do not silently edit the frozen locator to repair historical usage text.

### F5 — “first and only counter runs” overstates the later execution history

**Counterexample:** after the authoritative measurement, the declared separability checker executes both acceptance commands again in temporary copies.

**Evidence:** `SCORECARD.md:1164` describes the final-measures receipt as “first and only counter runs on the claimed objects.” But `reports/round-61/telemetry/separability.txt:1` explicitly says its dynamic leg reruns each acceptance, and `:5` records `acceptance_runs=2`; its stamp is 10:02:00Z, after the 09:57:40Z measurement. `L1JSON:596-598` records the command and result. The separability receipt explicitly preserves the first C verdict as authoritative.

**Impacted axes:** calibration and execution provenance. This is NOT evidence of rerunning to seek a replacement PASS, or of a second authoritative claim receipt. The later runs are dependency checks in copies.

**Smallest safe correction:** say “first and sole authoritative claim-measurement receipt,” and separately disclose the later declared dependency-check executions. Keep C's original FAIL and O's original PASS unchanged.

### F6 — freeze-baseline FAIL labels are presented without a freeze-baseline receipt

**Counterexample:** `SCORECARD.md:58,1168-1169` attribute baseline `ACCEPT-*-61 FAIL` results to the revision-1 freeze, but the committed pre-landing absent-object receipt is explicitly revision 0, not revision 1.

**Evidence:** `reports/round-61/telemetry/declaration-dry-run.txt:1` names revision `106df397...` and “instruments revision 0”; `:3-28` contains those baseline results. The revision-1 receipts contain independent populated controls, not a run on the absent-object freeze tree (`controls-c-rescore.txt:1-2`, `controls-o-rescore.txt:1-3`). The inspected L1 sequence lands the freeze, builds the real object, and then performs its first full acceptance run; I found no retained full absent-object acceptance receipt for `2f4f8a40`.

**Impacted axes:** calibration and measured-versus-inferred provenance. [INFERENCE] Revision 1 would also reject the freeze tree because its claimed lands are absent. That expectation is not the same as an observed revision-1 baseline run, and the record should distinguish them.

**Smallest safe correction:** identify the observed before-value as the revision-0 declaration dry run, and label the revision-1 absent-land before-value as inferred if it is retained. Do not manufacture a historical receipt or rerun C now to fill that gap.

## Explicit tradeoff, not an undisclosed fix

O's selftest clause was removed before data, not made independently verified: `reports/round-61/claims.json:36,42` disclose that choice, and `controls-o-rescore.txt:30-47` still shows keyed-a2 and fake-selftest passing. Describing this as removal of a weak proxy is accurate; describing it as a killed fake-selftest control would not be. Whether the narrowed obligation is acceptable belongs to the canonical judge, not this critic. I make no admission or rejection decision.

## Execution bounds

Read-only repository/history inspection and bounded foreground git/checksum commands only. No `accept-c.py`, other acceptance counter, locator, build, test, linter, browser, external runtime, source fetch, git/jj write, install, update, delegation, or background job was invoked by this seat. All processes started by this seat completed; none remains to kill. No files were written except this single report, in this one write call. Tool installs/updates: none.
