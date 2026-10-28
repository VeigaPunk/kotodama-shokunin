# MutCaLedgerSurface — Ca ledger parser, L76-19/20/21

**Verdict:** L76-20 and L76-21 are not observed parser failures: their `git grep` argv forms conform to the parser and produced the frozen expected short hashes. L76-19's observed failure is a statement anchoring mismatch, not command grammar. A clean future fixture must distinguish argv grammar acceptance from successful statement-line anchoring and from token extraction/semantic meaning; do not conflate a line mismatch with command rejection.

## Evidence

- Frozen configuration is `df0f0309d61e5485bb17035d3f8791b1e6a11d40`; the lane's L1 receipt `.ufo/waves/round-76/w1/stage/L1/freeze-ca-control-ledger-redbefore.txt:37-43` records the three pairs and exact failure. Its LEDGER problems are L76-13 class membership and `L76-19: stated_text not found in corpus/lessons/round-75.md at base`; no L76-20/21 parser complaint appears. It records base/lands observation values: L76-19 `2020`, L76-20 `20b571d7`, L76-21 `e0560649`.
- The frozen correction draft `.ufo/waves/round-76/w1/drafts/scorecard-corrections.md:29-31` gives the exact argv:
  - 19: `git grep -h -E '^window: chars=' <base> -- reports/round-75/evidence/S892.txt`
  - 20: `git grep -h -o -E '^sha256: [0-9a-f]{8}' <base> -- reports/round-75/evidence/S885.txt`
  - 21: same SHA pattern for `S887.txt`.
  The discrepancy on L76-19 is the filed `stated_at=corpus/lessons/round-75.md:48`; the cited statement text is not found on that base line according to the receipt, so LEDGER rejects before any question about the command's parse.
- Parser source `.ufo/waves/round-76/w1/stage/ExecAdaptCa/accept-ca.py:1031-1075` defines git-grep role parsing: recognize option arguments (`-e`/`-f`), take first bare argument as pattern, recognize pinned revision, then require paths and resolve them in clone. The commands' `-h`, `-E`, `-o` are flags; the anchored regex is the first bare pattern; full base hash is a recognized pinned revision; `--` introduces a resolvable path. Thus all three fit this implemented grammar. `.ufo/waves/round-76/w1/stage/ExecAdaptCa/accept-ca.py:1192-1229` shows the static/dynamic guard invokes this path and validates operands; grep regex metacharacters remain pattern data via `_grep_pattern_indices`.
- The frozen correction rows establish the intended observations; L76-20/21 extract only the first eight digest hex characters, and the receipt confirms those exact observed values. This establishes acceptance/output, not that short digests identify content uniquely or that digest is the right claimed subject.

## Precise fixture distinction

A future clean fixture should preserve each command as an argv array and use a committed base clone with the exact referenced path. It should report separate assertions: (1) `observe_problem(..., clone)` accepts the argv (grammar + operand resolution); (2) command exits successfully and stdout is exactly the intended output; (3) ledger's captured `stated_text` is actually present at the declared base path/line; and (4) the declared parse captures the intended complete claim token. Include a valid anchored `git grep` control and a deliberately wrong `stated_at` line using the *same valid argv*, expecting only statement anchoring to fail. For L76-20/21 additionally distinguish “short digest prefix differs” from any claim of full digest/content identity. Do not label L76-19 as a parser grammar defect or L76-20/21 as failures based on the L76-19 anchor error.

No tests or edits performed; no tools installed. Report is the only written artifact.