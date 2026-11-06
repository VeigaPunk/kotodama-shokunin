# ReviewerO100 — round-100 report (claim O non-author review)

Reviewed bytes: tools/check-table-support.py sha256 972cefea2b429a9d9ca3d9efc1acf3a63391e7c6ba2da576a1225fda6258b73a (at both awaited DONE markers). Full detail: .ufo/waves/round-100/w1/stage/ReviewerO100/review.md (+ counter.txt).

**Verdict: legs O0–O4 PASS. O5 FAIL at review time — L1-owned registration not yet landed (scorecard-capability-rows=0, skill-mentions=0).** First failing leg of the claim as a whole: O5; no defect in the executor-owned surface.

Numbers (command → rc):
- Frozen counter, `python3 -B reports/round-100/predispatch.py --root <lane> --work <scratch>/counter --base-rev 60010a55…` rc 1 → O0 PASS (sha above), O1 PASS 40/40 floor=24 rc=0, O2 PASS 28/28 traceback=0 rc=0, O3 PASS forged-minus-actual={(UNSUPPORTED-CELL, Yoruba, limit on the praise)} actual-minus-forged=[] forged rc 1, O4 PASS 36/36 killed 0 survived 0 broken-pattern rc=0, O5 FAIL (rows=0 mentions=0). Counter rc 1 overall from O5 + claim-C legs (C1/C4/C6/C9 — not my scope).
- Pin chains: battery sha b78176e3… == battery100.sha256 == BATTERY-SHA256 in battery100-control-base.txt and battery100-feasibility.txt; mutants sha 18dbcf3b… == mutants100.sha256 == DRIVER-SHA256 line 1 of mutation100-first.txt; pin mtime 08:47:39 predates receipt 08:48:26. Freeze commit 255d847…: `git ls-tree` shows battery100.py + pin + both receipts as blobs; 7/7 frozen files byte-match disk (`git show <rev>:<f> | sha256sum`).
- Conformance: 16 scratch fixtures, none covered by battery100 → `FIXTURE-SUMMARY cases=16 pass=16 fail=0` rc 0, tool byte-equal to frozen feasibility ref on every fixture (caption boundary, NFKD labels, STOP/short labels, path ranges/out-of-range/no-root, first-evidence-dir precedence, per-table NO-CAPTURE dedup, ragged col fallback, stemming families, exact 80-token window boundary, text mode, error channels).
- Corpus: tool vs ref over all corpus/knowledge/**/*.md with all 21 evidence dirs → `CORPUS-COMPARE files=271 disagreements=0` rc 0.
- Selftest strength: 4 branch reverts in scratch copies (window eviction, ¾ threshold, substring binding, widened caption scope) → each targeted pin fails, selftest rc 1; `REVERT-SUMMARY patches=4 proved=4` rc 0.
- Harm: `git diff --stat 60010a55… -- tools/` empty; status shows only the untracked new file; no existing tool/gate/selftest changed.
- Observation (not a defect): chmod-000 capture → rc 2 TABLE_SUPPORT_ERROR where the frozen ref would traceback; input class outside the frozen contract's enumeration, documented in the tool docstring, unexercised by battery/corpus/counter; directory-as-capture is NO-CAPTURE matching ref.

Residual: O5 must land with the L1's commit; mutation pin + first receipt are untracked (L1 is sole committer); counter reads the live tree, so post-review byte changes re-open O-legs. Tooling installed: none. Scratch deleted; nothing committed by me.
