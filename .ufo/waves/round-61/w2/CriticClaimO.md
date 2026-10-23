# CriticClaimO — round 61 wave 2

## Scope, axis, and fixed result

Seat: `KotodamaR61.CriticClaimO`. Axis: **operability**, specifically the reusable cited-line CLI added at `tools/check-cited-lines.py`. Calibration, truthful provenance, and policy/tool agreement are constraints on that axis, not additional claimed gains.

Read-only review of the shipped source, O's declaration/counter, all `CtlO*.md` receipts, `MutCounterO.md`, the revision-1 rescore, adjacent tools, and the relevant lessons/policy. No counter, fixture, selftest, or other runtime was executed. Existing results were treated as evidence, not rerun for confirmation.

The measured result is fixed: `reports/round-61/telemetry/final-measures.txt:20-28` records **ACCEPT-O-61: PASS**, exit 0, at `efbee29cd8c0872a4fb89db34c489d4a9960916c`, counter SHA-256 `5f1530a485d307544ccbde94a8c1f80b3f9d5360b7c8a4966259174e3d3bb99d`. This report neither changes that result nor makes an admission/canonical judgment.

## Review conclusion

**O names a defensible new operability surface, not a numerical improvement or a second award for an old prose rule. However, the explanation that both surviving controls are simply correct tools is false for CtlOKeyed a2.** Its generic fallback parses correctly, but its production-shaped path deliberately skips reading the corpus and returns stale embedded findings. The fake-selftest fixture is different: its retained lint behavior is real, while the selftest authenticity obligation was removed from the acceptance statement before measurement.

The strongest concrete correction is to the round's explanation of the surviving a2 control, not to the frozen verdict. A second scope correction is needed where QUALITY 15 treats this two-shape lint as a complete heading/clause-scoping check.

## 1. Is the axis named by the changed surface?

**Yes.** `reports/round-61/claims.json:30-44` names `operability`, the capability `clause-scoping lint for cited lines`, and the new executable path. Its contract is operational: findings, recursive Markdown traversal, clean input, input errors, standalone execution outside the lane, and exit codes. It does not define an operability score of 603, 26, or six green legs.

- The **603** REAL findings are a pinned regression corpus, not 603 repaired lines or a quality/coverage increase. The tool does not repair them.
- The shipped implementation genuinely scans supplied inputs: `scan_line` derives findings from the line (`tools/check-cited-lines.py:53-61`); `scan_file`, `walk_markdown`, and `collect` open files and traverse supplied paths (`:64-109`); `main` reports those results (`:112-136`). No embedded corpus-result branch or counter import is visible in the reviewed source.
- The build receipt `.ufo/waves/round-61/w1/ExecLintTool.md:40-82,84-150` separately records real selftest comparisons and generic scanning evidence. Those are attributed build receipts, not additional checks run by this reviewer or substitutes for the final measurement.

**Scope limit:** shipping the lint is not evidence that packet construction now uses it. `claims.json:42` explicitly leaves subsequent packet use review-only. The round-60 failure joined three entry lines for S612, not just one multi-ID line (`corpus/lessons/round-60-verifier-spotcheck.md:117-122,145`). A line-shape checker alone cannot certify that a later packet selects exactly one supported clause.

## 2. Strongest surviving control: CtlOKeyed a2 is a work-skipping shortcut

### Counterexample and evidence

The **unchanged a2 fixture still passes revision 1**: `reports/round-61/telemetry/controls-o-rescore.txt:30-38` gives all six legs PASS, exit 0, fixture SHA prefix `cfbcb3322d7d2cc2`.

The fixture source remains available at `/fast/scratch/hyaku/kotodama-r61/CtlOKeyed/tool_a2.py`:

- `:7-8` fixes `FILES = 235` and begins the embedded finding table.
- `:617-618` selects the special branch whenever the normalized argument ends in `corpus/knowledge`.
- `:663-673` checks only that the path exists, then emits findings from `BLOB` and adds the fixed file count. It never opens that directory's contents.
- `:674-681` uses the real generic parser only on other paths.

The existing behavioral witness is decisive: `.ufo/waves/round-61/w1/CtlOKeyed.md:101-108` records an **existing empty `corpus/knowledge`** with zero entries. a2 nevertheless exits 1 and prints `CITED-LINES: 603 finding(s) in 235 file(s)`. Under the declared scan contract, that empty directory instead requires no findings, zero files, and exit 0. This witness was not rerun here.

Thus a2 is not merely an unconventional but correct implementation. Changing the bytes under a routine production path can leave its output unchanged. Having a correct parser for other paths does not cure the faulty selected branch.

### Why revision 1 still accepts it

`reports/round-61/accept-o.py:169-186` tests generic behavior under random fixture names, while `:195-209` always tests REAL against the same frozen base and the same logical argument `corpus/knowledge`. Copying the tool outside the lane prevents the old relative counter import, but does not remove an embedded table. The fixture therefore does real parsing for GEN/CLEAN/ERR and skips precisely the corpus read that REAL purports to exercise.

The literal finite revision-1 predicate accepts it; this is not evidence that the measured production tool contains the shortcut. It **is** a surviving negative control against extrapolating that predicate into general-purpose corpus scanning.

### Impacted axis and smallest safe correction

**Impacted:** operability/calibration and truthful reporting.

`corpus/lessons/round-61.md:43` says a2 and the fake-selftest fixture still pass “because their parsers are correct.” That conflates two materially different survivors. The smallest safe records correction is:

> The fake-selftest fixture retains correct lint behavior after selftest authenticity became review-only. CtlOKeyed a2 still passes revision 1 despite an embedded REAL-result branch; its generic fallback is correct, but the tool is wrong when `corpus/knowledge` changes. This remains a calibration residual, not evidence against the shipped implementation or a change to O's measured PASS.

For a **future pre-data** instrument, reuse the already demonstrated empty-directory witness at that same logical path, and require output to change when a new cited Markdown line is added there. A same-bytes/different-root-name comparison would additionally expose path-keyed behavior. Do not amend or rerun this round's frozen claim to erase the survivor.

## 3. The fake-selftest survivor is not the same shortcut

`controls-o-rescore.txt:39-47` records revision-1 PASS for `/fast/scratch/hyaku/kotodama-r61/CtlOSelftest/a-fake-selftest.py`, SHA prefix `2bbb6367ca545fd6`.

Its source `:14-53` actually extracts distinct IDs, walks supplied paths, reads UTF-8 files, reports findings/counts, and returns the required scan/error exits. Only `selftest()` at `:56-58` is a print-only `selftest 10/10` followed by return 0. The original control isolates that substitution (`CtlOSelftest.md:15-23,39-43`).

Revision 1 deliberately stopped crediting that footer: `claims.json:36,42` and `accept-o.py:19-20,158-160` make selftest review-only and TOOL existence-only. Therefore this fixture's continued PASS does **not** demonstrate skipping a retained acceptance obligation. It still performs the retained lint work. It also cannot honestly be called a tool with ten executed selftests: that self-report remains false.

There is a wording residue: the incorporated Tool contract still says `--selftest` “runs its own cases” (`accept-o.py:16`). The report should explicitly distinguish that advertised/review-only behavior from what the acceptance predicate establishes. The shipped tool contains real comparisons (`tools/check-cited-lines.py:188-278`); the fake fixture's survival does not establish that the shipped selftest is fake.

The other prominent revision-0 survivors were actually stopped: the boundary-blind parser fails GEN/CLEAN (`controls-o-rescore.txt:12-20`), and keyed-c fails INDEP plus standalone execution (`:21-29`). Do not carry revision-0 CONTROL-MET labels forward as though those two still passed revision 1.

## 4. Is O re-scoring an already-held executable rule?

**No equivalent executable lint was found in the searched local tools; the prose repair already existed.**

Recursive tool searches covered `MULTI-ID`, `TABLE-ID`, clause-scoping/cited-line terms, S-id regexes, and distinct-ID threshold patterns; direct gate/harness searches covered citation/table-row checks. The only matching MULTI-ID/TABLE-ID implementation found was the new tool. Relevant adjacent authorities were read rather than inferred from filenames:

- `tools/check-draft-ids.py:11-37,118-150` detects unresolved draft tokens/fragments, not two registered IDs or cited table rows. Its own negative controls deliberately accept ID ranges (`:231-232`).
- `tools/check-judged-object.py:4-33,245-246,253-320` compares frozen entry bytes and whole-entry ID sets; it does not enforce citation cardinality per line.
- `tools/check-gate-quotes.py:15-20,101-104` operates on lesson Gate rows/quotes, not this arbitrary knowledge-line rule.
- `tools/source-audit-inventory.py:2-20` inventories uncertainty markers.
- `tools/gates/provenance-audit.py:4-23` checks headers/calibration apparatus, not these citation shapes.

The old authority is explicit: `corpus/lessons/round-60.md:56` routes one-ID-per-line or clause-scoped packets and calls for a lint in round 61. Implementing that routed prose repair as a reusable standalone CLI is a real operability change. It is not newly discovered sourcing knowledge, repaired historical corpus content, or improved semantic discernment. The current search and historical control receipts support that distinction; no historical git-tree comparison was performed by this seat.

## 5. Policy overclaim: a clean lint is not complete clause scoping

**Counterexample [INFERENCE, source-level; not executed]:** a file containing `# Footwear (S652)` produces no finding under `scan_line`: there is only one distinct ID and the line does not begin with `|`. Yet `corpus/QUALITY.md:47` forbids any cited heading and presents this tool's exit 0 as its check. Similarly, two independent assertions with one S-id on one bullet are invisible to the two implemented shape conditions.

**Evidence:** `tools/check-cited-lines.py:53-61`; O's intentionally narrower finding contract at `accept-o.py:7-16`; QUALITY 15 at `corpus/QUALITY.md:47`.

**Impacted:** operability/policy-tool agreement. This is not a failure of O's frozen two-shape contract. It is a fixable overstatement in the surrounding rule if exit 0 is presented as sufficient proof of no cited headings or one supported clause. The smallest safe correction now is to label those unimplemented checks as separate review obligations and describe O as a multi-ID/leading-pipe-table lint. Any expanded heading detector belongs to a later declared contract, with controls, not a post-measure change to this predicate. Actual clause support remains review work.

## 6. What the mutation receipts establish

`MutCounterO.md:3,17-34` reports six selected **revision-0 counter mutants** killed: exact GEN set, GEN cardinality, GEN summary, REAL completeness, error diagnostics, and table-reference coverage. Those are useful sensitivity controls, not saturation of the tool's specification or proof that all work-skipping shortcuts are rejected. The report itself limits its scope (`:686`). The unchanged a2 PASS on revision 1 is direct contrary evidence to that stronger extrapolation.

Other retained source-level limits include set parsing that discards output order/multiplicity (`accept-o.py:89-99`) and REAL not checking its parsed summary (`:202-209`). These corroborate the need to say precisely what the predicate measured; they do not authorize revising it now.

## Bounds and handoff

Only this report was written in the lane, once, at its assigned absolute path. No code, claims, counter, policy, lesson, corpus, sibling report, fleet file, or scratch fixture was changed. No processes/background jobs, delegation, external fetching, runtime invocation, installs, or updates were started; no process tree remains to kill. No verification was exercised by this seat beyond reading/searching existing evidence. No blocker.

**Bottom line:** retain the measured O PASS and recognize the new CLI surface, but record a2 as a genuine surviving corpus-read shortcut, not an entirely correct tool; distinguish the harmless-to-the-retained-predicate fake-selftest survivor; and do not credit this narrow lint with complete packet/heading/clause support enforcement.
