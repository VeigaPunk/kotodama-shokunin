# RevCensus — round79 W1 recon/review: census start/end reproducibility, end-receipt stamp requirements, S884 warning semantics

Seat: RevCensus (reviewer, leaf — no dispatch). Lane base: `44f76d456c1b326a71ffdb381590af825cbf11be`.
Scope: bounded W1 item only — census start/end reproducibility, end receipt stamp requirements, S884 warning
semantics. Raw probe outputs and diffs: `.ufo/waves/round-79/w1/stage/RevCensus/receipts/`.
All observations below were executed by this seat; hashes quoted from measured bytes, not restated from other
reports. No lane/fleet file was modified; probes were read-only; scratch removed after receipts were copied.

## Inputs read

- `.ufo/waves/round-79/CLAIMS-DRAFT.md` (O + Ca candidates; pre-freeze disposition), `corpus/QUALITY.md` (criteria 17/19 receipts-pin-revision bar, 25/26 freeze constants), `.ufo/waves/round-79/w1/spec.json` (seat prompt).
- `scripts/sources-census.sh` (fleet, 806 lines; validate-mode parser, `usedby_findings`, main dispatch).
- `reports/round-77|78|79/telemetry/census-*.txt`, `reports/round-79/telemetry/census-start-meta.json`, `reports/round-79/telemetry/baseline-census-mismatch.json`.
- `corpus/lessons/round-78.md`, `corpus/lessons/round-78-verifier-spotcheck.md` (routed defect 2), `LOG.md` round-78 entry, `SCORECARD.md` `## Corrections` conventions (rounds 73–76), `SHONEN.md:6`.

## Probe protocol (read-only; TMPDIR honored under scratch)

- P1 live: re-ran the receipt command verbatim on the current fleet/lane worktree.
- P2: scratch fleet clone with lane checked out at base `44f76d45` (toplevel asserted before any git operation).
- P3: scratch fleet clone with lane checked out at `4b255745` (round-78 commit named by `baseline-census-mismatch.json`).
- Tool version: `scripts/sources-census.sh` sha256 `3fb72615…4e30` (35466 B), fleet HEAD `73ff6ac3`; emit line 670 emits tab-separated TSV, identical at fleet commits `f47ad6ba` and `6a1dd8ce` (pre-date round-78 capture).
- Exit codes: P1=0, P2=0, P3=0. Full hashes: `stage/RevCensus/receipts/hash-manifest.txt`.

## Verified baseline facts

1. `census-start-meta.json` is internally consistent: `receipt_sha256` = measured sha256 of committed `reports/round-79/telemetry/census-start.txt` (`a9e9e4a1…`); `registry_sha256` (`51b18f1c…`) = measured sha256 of `git show 44f76d45:corpus/SOURCES.md` = measured sha256 of the current worktree registry file; `revision` = base.
2. P1 output is **byte-identical** to committed round-79 `census-start.txt` (cmp clean, same sha256 `a9e9e4a1…`): the round-79 start receipt reproduces exactly over the current worktree.
3. P2 body reproduces the committed round-79 start receipt with only the final `ok` line differing (absolute registry path: scratch vs live). The 32 warning lines are byte-identical. So the receipt body is a pure function of committed registry bytes; only the `ok` line is worktree-path-dependent.
4. Round-78 start vs end committed receipts differ in exactly one line (`diff` → `33c33`): the S884 W01 token — `…amend-2026-10-23.md` (start) vs `…amend-2026-10-24-r13.md` (end).
5. P3 body (census re-run at `4b255745`) matches the committed registry token `…amend-2026-10-23.md` at every row; committed round-78 `census-start.txt` is content-correct at its commit.
6. `baseline-census-mismatch.json` bindings all verify against committed bytes: `receipt_sha256` `05b5011a…` = measured sha256 of committed round-78 `census-end.txt`; `actual_used_by` = measured field 12 of `git show 4b255745:corpus/SOURCES.md` S884 row; `reported_used_by` = measured token on committed `census-end.txt` line 33; `revision` `4b255745…` is the round-78 commit.
7. `worldbuilding-setting-practice.amend-2026-10-24-r13` appears in **no** committed revision of `corpus/SOURCES.md` (`git grep` over all 1243 commits: not found), and the path was never added in any commit (`git log --all --diff-filter=AD`: empty). The only `*.amend-2026-10-24-r13.md` on disk is `heritage-taxonomy-models.…`, a different row's target.
8. W01 semantics confirmed from source (`row_pass`, line 670): a tier-C `mined` row with used-by ≠ `—` prints the **verbatim trimmed used-by cell** (field 12, whole cell, comma-list intact); warnings never set the findings flag. Separately, `usedby_findings` (E11) checks on-disk existence of each mined row's used-by path; any E11 suppresses the `ok` line and forces exit 1.

## Findings

### HIGH-1 — round-78 `census-end.txt` is irreproducible from any committed lane state (routed defect 2 confirmed and sharpened)

- The recorded S884 token `…/worldbuilding-setting-practice.amend-2026-10-24-r13.md` cannot be re-derived from committed bytes at `4b255745` (P3), at base, or at any of 1243 commits (fact 7). The receipt carries **no revision stamp, no registry hash, no tree hash** — only `Command:`/`Exit: 0` headers — so nothing on the receipt itself discloses what worktree it measured.
- Sharper than the routed defect's text: by the script's own semantics (fact 8), the end receipt's combination (W01 printing the r13 token **and** trailing `kotodama ok` **and** `Exit: 0`) is only producible when `$dir/corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md` **existed on disk** at capture time — a never-committed amend file that was removed before commit `4b255745`. The receipt therefore measures an uncommitted worktree state; "uncommitted/regressed working-tree state at capture time" (verifier spot-check wording) is the right class, with the regression visible only because the token was committed nowhere.
- Impact on Ca: the frozen counter's "mismatch=1 at base" leg must re-derive the token from `git show <measured-rev>:corpus/SOURCES.md` field 12 (yielding `…10-23.md`), never from the receipt; the receipt digest binding (`05b5011a…`) is what makes a "changed receipt" control fail. Both bindings are available and verified (facts 6, 7).

### MEDIUM-2 — committed round-78 receipts are not raw tool output: whitespace-folded bodies

- Committed round-78 receipts contain **0 tab characters** in 35 lines (space-separated body); the tool has emitted tab-separated TSV at every fleet revision checked (line 670 identical at `f47ad6ba` and `6a1dd8ce`, both pre-dating round-78 capture). Round-77 and round-79 committed `census-start.txt` are raw TSV (33 tabs / 33 lines).
- Consequence: exact-byte reproduction of round-78 receipts is impossible; only whitespace-normalized comparison works (P3 vs committed start: identical after normalization). Any round-79 acceptance command that diffs a fresh census against committed round-78 bytes must normalize field separators, or the check fails for reasons unrelated to the S884 defect. Recommendation for the W1 freeze: declare the normalization (e.g. `tr -s ' \t' ' '`) in the receipt/counter command rather than discovering it in W2.

### MEDIUM-3 — end-receipt stamp requirements for round-79 (what the new `census-end` must carry so HIGH-1 cannot recur undetected)

Grounded in QUALITY 17 (receipts pin measured revision and tree hash of read inputs; disclose moving worktree), 19 (evaluation runs at the stamped revision; receipt proves stamp and evaluation agree), and the observed failure mode. The round-79 start sidecar `census-start-meta.json` is a step up from round-78 (revision + registry sha256 + receipt sha256, all verified consistent), but for the round-79 **end** receipt the following are required, in the receipt or a meta sidecar bound to it by the receipt's sha256:

1. `# stamped revision:` the 40-hex commit the measured worktree claimed to equal, plus `git rev-parse <rev>^{tree}` tree hash (QUALITY 17/19 header set as used by this lane's counters).
2. Registry read-path proof: sha256 of `git show <stamped-rev>:corpus/SOURCES.md`, compared to the sha256 of the file actually read (worktree file), and **worktree-cleanliness disclosure** (`git status --porcelain` empty for the tracked tree, or an explicit dirty-tree statement). The registry hash alone does not exclude a dirty tree in other files; the HIGH-1 failure mode was exactly a dirty-tree capture.
3. Tool pin: the census script is fleet-tracked, **outside lane revision control**; stamp its sha256 (`3fb72615…` at capture) or fleet blob id, else a fleet-side script edit silently invalidates cross-round receipt comparison and no lane receipt can show it.
4. The stamp must be bound to the receipt bytes (receipt sha256 in the meta) and the receipt must be reproducible from the stamped revision (P2/P3 show body-reproduction works when the tree is clean).

### LOW-4 — S884 warning semantics, restated for the correction's wording (so "each clause load-bearing" holds)

- W01 is a **non-failing** hygiene warning (tier-C mined row still carrying a used-by path): it never changes exit status, and the `ok` line still prints. The warning token is the registry cell content verbatim (trimmed outer whitespace only), not a path existence check. Existence is E11's job (mined rows only), which is failing and exit-1.
- Therefore: "S884 used-by token" in every Ca clause, the correction row, and the counter means **field 12 of the S884 registry row at the named revision, trimmed**, exactly as printed after `used-by=`. A correction row binding original receipt digest (`05b5011a…`), measured revision (`4b255745…`), old token (`…amend-2026-10-24-r13.md`), actual token (`…amend-2026-10-23.md`) has all four values verified against committed bytes by this seat (fact 6). The correction must land append-only (SCORECARD `## Corrections — round N` table convention; do-not-rewrite is what makes the APPENDONLY/changed-receipt controls meaningful), and SHONEN.md:6 cites only registry counts + census exit 0 — no used-by tokens — so this mismatch is evidence-record repair, matching the draft's pre-freeze disposition that Ca needs a genuine SCORECARD/SHONEN self-assessment mismatch to be admitted (none found in my scope; L1/freeze owns that call).

## Residual risk and verification gaps

- The dirty-worktree diagnosis (never-committed amend file existed at end capture) is an inference from the script's E11/exit semantics + observed receipt bytes; the pre-commit worktree state itself is unobservable now. It is the minimal explanation consistent with all measured bytes.
- I did not re-run `sources-census.sh selftest` (out of scope: no build/lint unless asked); the parse semantics cited are from reading the committed script at the pinned fleet version.
- Whitespace folding of round-78 receipts: when/where the fold happened is not recoverable from committed bytes; only its existence is measured (0 tabs vs tool's TSV).
- The round-79 end receipt does not exist yet (no claim data landed); MEDIUM-3 is a requirement set for L1/integration, not a check of an existing artifact.
- Tool installs: none (no installs or updates performed; pacman untouched).
- Concurrency note: while this report was being finalized, a sibling seat added an uncommitted S897 row to
  the worktree `corpus/SOURCES.md` (12:44, after all probes at 12:41–12:43); every hash quoted here binds
  committed bytes at `44f76d45` / `4b255745` or probe outputs preserved under `stage/RevCensus/receipts/`,
  and P1's byte-identity was measured against the then-clean worktree.

## Evidence index (stage)

- `receipts/probe-live-validate.txt` — P1 raw output (byte-identical to committed r79 start receipt).
- `receipts/probe-base-at-44f76d45-validate.txt`, `receipts/probe-r78-at-4b255745-validate.txt` — P2/P3 raw outputs.
- `receipts/normalized-body-diffs.txt` — whitespace-normalized body diffs (P3 vs r78 start/end; P2 vs r79 start).
- `receipts/diff-committed-r78-start-vs-end.txt` — the single-line S884 delta (committed, line 33).
- `receipts/diff-probe-r78-vs-committed-census-{start,end}.txt`, `receipts/diff-probe-base-vs-committed-r79-census-start.txt` — raw (unnormalized) diffs incl. tab/space divergence.
- `receipts/hash-manifest.txt` — commands, exits, tool version, all quoted hashes.
