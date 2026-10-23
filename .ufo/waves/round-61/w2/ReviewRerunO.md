# ReviewRerunO — independent re-measure of claim O (ACCEPT-O-61)

Seat: KotodamaR61.ReviewRerunO (wave 2, falsify). Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin, measured revision `efbee29cd8c0872a4fb89db34c489d4a9960916c`. Sandbox: /fast/scratch/hyaku/kotodama-r61/w2/ReviewRerunO/ (`clone/` checkout of the measured rev, `base/` = `git archive 942abdf4 corpus/knowledge`).

## Verdict

No actionable finding. ACCEPT-O-61 PASS reproduced 5/5 independent runs; counter and tool hashes match the frozen values; the R60-M6 amulets line is genuinely reported by the tool on both the checkout corpus and the base archive. The PASS in `reports/round-61/telemetry/final-measures.txt` is honest and reproducible.

## Method

1. `git clone --no-checkout` lane repo → sandbox `clone/`; `git checkout efbee29cd8c0872a4fb89db34c489d4a9960916c`; `rev-parse HEAD` = `efbee29cd8c0872a4fb89db34c489d4a9960916c` (confirmed).
2. sha256 checks (at measured HEAD, before any run):
   - `reports/round-61/accept-o.py` = `5f1530a485d307544ccbde94a8c1f80b3f9d5360b7c8a4966259174e3d3bb99d` — **matches** required value.
   - `tools/check-cited-lines.py` = `a9b0fbd5809b3764b2309cd8a82625c75ca1d6dd7c498309387050312078804a` — **matches** required value.
3. `timeout 600 python3 -B reports/round-61/accept-o.py; echo exit=$?` × 5 in clone (full outputs below). Total wall time 2.85 s.
4. `python3 -B tools/check-cited-lines.py corpus/knowledge` in clone → `MULTI-ID corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:95 S612,S613` present (the R60-M6 line), summary `CITED-LINES: 603 finding(s) in 236 file(s)`, exit 1.
5. Same tool over the counter's REAL-leg source (`git archive 942abdf4 corpus/knowledge` extracted under sandbox `base/`) → `MULTI-ID base/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:95 S612,S613` — identical line number and ids.
6. Read the counter (`accept-o.py`, 219 lines) and the tool (`check-cited-lines.py`, 287 lines) fully enough to audit semantics.

## Full run outputs (verbatim, 5/5)

```
===== RUN 1 =====
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN PASS exit=1 want=86 got=86 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 86 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
===== RUN 2 =====
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN PASS exit=1 want=86 got=86 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 86 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
===== RUN 3 =====
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN PASS exit=1 want=92 got=92 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 92 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
===== RUN 4 =====
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN PASS exit=1 want=90 got=90 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 90 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
===== RUN 5 =====
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN PASS exit=1 want=76 got=76 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 76 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```

Non-PASS runs: **none** (5/5 `ACCEPT-O-61: PASS`, `exit=0`).

## Falsification attempted

- **Fixture memorization**: rejected. GEN/CLEAN/ERR legs seed from `os.urandom(16)` each run — GEN `want` varied 86/86/92/90/76 across runs while still matching `got` exactly, so the tool is being re-tested on fresh random trees, not replaying canned output.
- **Tool special-casing**: rejected by source audit. `scan_line` implements the generic rule (`\bS\d{3,}\b`, distinct ids sorted numerically, MULTI-ID iff ≥2, TABLE-ID iff ≥1 on `lstrip().startswith("|")`); no mention of `amulets`, `S612`, `S613`, `S` constants, or path names anywhere; INDEP additionally confirms no `reports/`, `accept-o`, `round-61` strings.
- **Reference-vs-tool correlated oracle**: the counter's `reference()` is the same *semantics* re-implemented independently (same regex, same predicates). The discriminator legs are real: `lookalike` generator emits `X{t}`, `{t}x`, `S<2-digit>`, `{t}_`, `{t.lower()}` which exercise `\b` boundary behavior; the GEN tree plants a `.txt` file carrying a multi-id line that the tool must ignore (any `.txt` scan → `extra>0` → GEN FAIL). Both held across 5 runs.
- **Frozen-corpus integrity**: REAL leg derives the reference from `git archive 942abdf4 corpus/knowledge` (content-addressed, cannot drift with checkout), requires `r60_line_in_reference=True` **and** `got == want` with zero extra/unparsed output, and the tool runs from a tempdir copy so in-place mutation cannot affect it.
- **Summary/format drift**: `parse()` routes every non-matching stdout line into `bad` and requires it empty; exact `CITED-LINES: N finding(s) in M file(s)` counts enforced for both GEN (want/files computed independently) and CLEAN (`0 finding(s) in 1 file(s)` literally).
- **Error-path honesty**: ERR requires exit 2 + `CITED_LINES_ERROR` on stderr for missing path, invalid-UTF-8 file, and zero args — all three verified every run, and reproduced manually (running the tool on a nonexistent root arg gave `CITED_LINES_ERROR`, exit 2).

## Findings by severity

None. No defect, dishonesty, or measurement artifact found in scope.

## Residual risk / verification gaps

- INDEP is a lexical string check; a sufficiently motivated tool could hide provenance differently — mitigated by my full read of the tool's core logic (lines 53–137): generic linter, no hidden branches.
- 5 runs ≈ 5 random GEN trees (~80–95 findings each). A rare tool bug on an ungenerated line shape could survive; the generator's 8 line kinds cover the contract's dimensions, so residual risk is low but nonzero.
- `reference()` and the tool share spec semantics by construction; a *spec-level* misreading (e.g., whether a 2-id table row should double-report) is consistent between them and cannot be falsified from inside this contract — it is the contract.
- Counter runtime is dominated by `git archive`/small trees; 600 s timeout is far from binding (observed ≈0.5 s/run).

## Environment / housekeeping

- Python: system `python3` (Arch), `-B` as specified; no installs performed; pacman untouched per pause.
- No git writes in the lane or fleet repos; all git ops confined to sandbox clone with `GIT_DIR`/`GIT_WORK_TREE`/`GIT_INDEX_FILE` unset. `accept-c.py` never executed.
- All processes finished synchronously (nothing left running); counter tempdirs self-clean; sandbox artifacts confined to `/fast/scratch/hyaku/kotodama-r61/w2/ReviewRerunO/`.
