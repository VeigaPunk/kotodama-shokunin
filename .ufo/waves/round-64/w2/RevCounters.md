# RevCounters — round-64 pre-data counter revisions

Axes: **coverage** (C), **operability** (C/O), **calibration** (Ca and evidence fidelity). I edited only the three assigned counters and this report. The frozen predicate lines in the counters were left untouched. The source tool `tools/reopen-row.py` and external substrates were not edited.

## 1. C — `reports/round-64/accept-c.py`

### Revision 2: reject teaches-copy bullets

**Diff/behavior:** RESTATE now compares the parsed bullet clause with the matching row's stripped `teaches` cell and records `teaches_copy` on exact equality. The row lookup is bound immediately after parsing the clause, before either the new guard or quote lookup; this also fixes the ordering defect reported by the parent. The docstring's stale `revision 0` stamp is corrected in the final revision header/history.

**Forcing control:** `.ufo/waves/round-64/w1/CriticClaims.md`.

**Retained pre-revision witness** (CriticClaims §4, 26 teaches-copy bullets):

```text
ROWS PASS bad=[] checked=26
REJECTS PASS bad=[] checked=6
ONEID PASS bad=[] marks=[] cited_lines=26 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=26
...
ACCEPT-C-64: FAIL
exit=1
```

**Targeted post-fix control:** `python3 -B /home/vgpnk/.cache/hyaku/kotodama-r64-w2/RevCounters/quick_controls.py` executes the counter's actual RESTATE-loop AST without running the full predicate. Output:

```text
C teaches-copy control: ['line1:S718:teaches_copy', 'line1:S718:no_novel_content_word']
C supported-noncopy control: []
```

The control now reaches RESTATE without `NameError`; the supported non-copy control stays clean.

### Revision 3: require every new citation exactly once

**Diff/behavior:** ONEID additionally requires `sorted(cited_ids) == NEW_IDS`; missing and duplicate IDs appear in its detail. Thus each of S718–S743 must be cited exactly once on an eligible single-ID entry line.

**Forcing control:** `.ufo/waves/round-64/w1/ReviewerCounterC.md` (D1).

**Retained pre-revision witness:** ReviewerCounterC §5 records the zero-citation fixture with `ONEID PASS ... cited_lines=0`, `RESTATE PASS ... lines=0`, and `ACCEPT-C-64: PASS` (exit 0).

**Targeted post-fix control** (same harness, evaluating the actual `citation_exact` AST expression):

```text
C citation zero: False
C citation all-once: True
C citation duplicate: False
```

No full C acceptance predicate was run.

## 2. Ca — `reports/round-64/accept-ca.py`, revision 2

**Diff/behavior:** NITS scopes to the canonical `## Round 64` H2 block (not an H3 or later round), finds the labeled `Round-63 numeric corrections` record, and requires its exact positive old-to-new correction line: `47 seat reports landed, not 45; W04 covers 27 duplicate-URL rows, not just S650/S651; the ACCEPT-O-63 dry run had 9 FAIL legs [optional leg list], not 6.` This retains the named values and blocks bare-token, wrong-substance, negated, unrelated-round, and phrase-only records. The initial uncommitted `a8088092…` draft's proximity matches were superseded before integration; current counter SHA-256 is `d0787979ae4e318c4a7cde4385dd2b2e36890f8e258b3733cc1a6e980533f917`.

**Forcing controls:** `.ufo/waves/round-64/w1/CriticCa.md`, `.ufo/waves/round-64/w2/CriticRevCa.md`, and `.ufo/waves/round-64/w2/RevVerifyCa.md`.

**Retained pre-revision witnesses:** CriticCa's records-only W04 append changed old-counter output from `NITS FAIL seat_reports_nit=True w04_nit=False` to `NITS PASS seat_reports_nit=True w04_nit=True`. CriticRevCa later demonstrated phrase-proximity false passes on wrong, negated, and out-of-scope numeric prose; RevVerifyCa demonstrated a phrase-only line false pass against the intermediate draft. Those intermediate outputs are not presented as results for the final bytes.

**Targeted final-byte control:** the harness evaluates the actual NITS AST block without executing the other six legs. Positive output was `((True, 'correction_record=True record_exact=True seat_reports_nit=True duplicate_url_nit=True fail_legs_nit=True'), ..., True)`. The negative matrix returned NITS `False` for bare tokens, wrong substance, negation, unrelated-round prose, phrase-only prose, same-line quoted denial, hypothetical cross-round attribution, and an out-of-region correction; each returned `correction_record=False` or `record_exact=False`. No full Ca predicate was run.

Residual semantic limit: this is a tightly pinned correction record, not a general natural-language truth/provenance judge. A contradictory statement elsewhere alongside an intact positive record still requires content review. NITS remains scoped to the requested canonical LOG entry; no separate SCORECARD leg was added.

## 3. O — `reports/round-64/accept-o.py`, revision 5

**Revision history and hashes:** revision 4 (`6d9c9354f0d7a9535aba4e781541b04626dd3a91791175a7d5f845c559615fa1`) contains the narrowed m5 patch with invalid indentation and inverted isolation prose. The m5 code was restructured in the pre-stamp revision-5 source (`760ddd4d6d1c0ef1f2c4d0dbd6cd5ef286be1e3b8b2fc5cded2bd6258c08f5a7`); the explicit revision-5 history/stamp amendment produces the final on-disk SHA-256 `cdee063e39e1ecdb739519f76cd878e0108d0c5c3de8a6d8cd873830a5349dab`.

**Diff/behavior:** m5 now inserts a validly indented `slashless_relative` condition at the tool's 8-space block: only nonempty relative paths without scheme/authority or a leading slash resolve against `/`. MUT runs m5 with `--only EDGE_SCHEMEREL,EDGE_SLASHLESS`, requires its pinned EDGE_SLASHLESS failure, and requires EDGE_SCHEMEREL PASS. The docstring now states the same pass/fail direction. Unknown `--only` selectors emit `ACCEPT_O_INPUT_ERROR` to stderr and exit 2 before fixture setup. The no-selector path still runs the same full leg set.

**Forcing controls:** revision 4: `.ufo/waves/round-64/w1/CriticO.md` and `.ufo/waves/round-64/w1/ReviewerCounterO2.md`. Revision 5: `.ufo/waves/round-64/w2/RevVerifyO2.md`, `.ufo/waves/round-64/w2/SupS729.md`, `.ufo/waves/round-64/w2/OReceiptFresh.md`, and the red revision-4 capture `reports/round-64/telemetry/final-measures-o-rev4.txt` (SHA-256 `fed0ded28f1dc5a3ff3dd62c739cf3e17bf8593a902474a9302b6b0131158da3`).

**Retained revision-4 failure evidence:** RevVerifyO2's full 23-leg capture on `6d9c9354…` had 22 PASS, `MUT FAIL`, `ACCEPT-O-64: FAIL`, exit 1; rebuilt m5 failed to compile because of its indentation. This remains red pre-data evidence, not an acceptance receipt.

**Post-stamp selected quick run** (not the full predicate):

```text
$ env TMPDIR=/home/vgpnk/.cache/hyaku/kotodama-r64-w2/RevCounters/tmp python3 -B reports/round-64/accept-o.py --only GEN,MUT,BOUND,EDGE_SCHEMEREL,EDGE_SLASHLESS
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
BOUND PASS bad=[] unlisted_requests=[]
EDGE_SCHEMEREL PASS rows=[('S2452', 'REFUSED', 1)] tgt_hits=0 src_hits=1 tb=False
EDGE_SLASHLESS PASS rows=[('S2551', 'LOCATED', 2)] dir_hits=1 root_hits=0 exit=0
MUT PASS bad=[] mutants=10
m5->EDGE_SCHEMEREL PASS rows=[('S2601', 'REFUSED', 1)] tgt_hits=0 src_hits=1 tb=False; EDGE_SLASHLESS FAIL rows=[('S2241', 'UNREACHABLE', 2)] dir_hits=0 root_hits=1 exit=1
ACCEPT-O-64: PASS
```

The selected invocation itself exits 0; this is not a 23-leg acceptance result. The separate post-stamp fail-closed check printed `ACCEPT_O_INPUT_ERROR unknown --only leg(s): NOSUCHLEG` and exited 2. No full O run was made on revision 5; the parent owns the post-commit 23-leg receipt.

## Verification, risks, and blockers

The targeted C/Ca harness exercised only the relevant AST blocks; the O run selected only the requested legs. No full acceptance predicate, build, lint, formatter, or external-tool check was run. LSP was unavailable in the surfaced tool set. No tools were installed or updated. The final revision-5 quick MUT is green, but its full O acceptance remains unmeasured post-revision.

**Files changed:** `reports/round-64/accept-c.py`, `reports/round-64/accept-ca.py`, `reports/round-64/accept-o.py`, `.ufo/waves/round-64/w2/RevCounters.md`.
