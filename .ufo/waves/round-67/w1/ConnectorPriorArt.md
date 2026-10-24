# ConnectorPriorArt — receipt / stamp / lands prior art

Seat: ConnectorPriorArt. Lane tip read-only. No tool installed. No code written.
Base named by the round: `ad5b52b0ab5691358cd38718ab75649dc9916f9a`.
Subject: `tools/check-receipt-seq.py` (claim O). Defect class it extracts: R66-D3 in `corpus/lessons/round-66-verifier-spotcheck.md` §5 item 3 — a lands-time `git log -1 main -- <receipt>` cannot see the records commit that carries the receipt.

`# stamped revision` / `# evaluated revision` / `# counter sha256 (self)` are parsed only in `tools/check-receipt-seq.py` (lines 56–60, 131–145, 179–197). No other file under `tools/` matches those headers.

## Table

Columns L / T / E are the three things this tool adds. **L** = evaluate at a caller-named lands revision by reading that commit's blob (`git show` / `cat-file`), never the worktree. **T** = carrier-parentage: `git log -1 main -- <receipt>` exists and its parent equals the stamped revision. **E** = require `# stamped` == `# evaluated` == `# measured` (plus the tree and counter-sha headers).

| tool | what it already verifies | L | T | E |
|---|---|---|---|---|
| `tools/check-receipt-seq.py` | The new checker. Default mode: five headers, stamped==evaluated==measured (`check_headers` 131–145), recorded tree == `stamped^{tree}` (148–157), paired counter sha (160–176). `--lands`: `git show <lands>:<receipt>` (80–82, 235–236) and a `moved_past` flag that is hardcoded PASS (232–234). `--topo`: carrier parent == stamped (179–197). Selftest prints `14/14` (14 `expect` calls, 321–422). | yes, receipt text only | yes, post-records, `main` only | yes |
| `tools/check-claim-separability.py` | Landed-byte separability. Unit `tree` is a commit or the explicit token `WORKTREE`; land blobs come from one `git cat-file --batch` (docstring 73–74, `Objects` ~163–198, absence at the named tree is `InputError` ~285). Dynamic leg overlays those lands onto `base` (`git clone --shared` only when `needs_git`). Overlap of the same path is a finding, not a dependency. No receipt header, no stamp equality, no `git log` parent. | partial: commit-scoped land blobs, but the commit is the unit's `tree`, and `WORKTREE` is a legal mode | no | no |
| `tools/harness/receipt_guard.py` | Write preflight. `ls-tree` blob presence of the destination at HEAD and every `refs/heads/*` + `refs/remotes/*` (144–158, 205–229). Refuses overwrite unless `REFRESH_RECEIPTS=1` (exit 3). `landed_ref` is a remote-tracking holder, not a lands hash and not a parent. Scrubs every `GIT_*` (56–59). Does not read receipt text. | no (presence at refs, not "bytes at --lands") | no | no |
| `tools/harness/receipt_guard_adoption.py` | AST inventory: which round runners call `guard_receipt` / `round_runner_main` before writing their own receipt. No git read of a lands commit. | no | no | no |
| `tools/harness/round_runner_conformance.py` | Static audit of runners in rounds 34–40: guard call dominates the `validation.json` write; reads the on-disk receipt for a findings/limits signature (docstring line 2, `GUARD_NAMES` line 23). Never executes a runner. No stamp headers. | no | no | no |
| `tools/harness/claims-freshness.py` | Premise re-derivation at `baseline_commit` via `git ls-tree -r -z` + `git cat-file --batch`. Docstring 49–58: "The worktree is never read. There is deliberately no worktree mode" — an r43 worktree fallback would have passed the stale claim this gate exists to catch. `--at` may name another commit only. Scrubs `GIT_*` (118–121). Probes are declared `before` clauses, not receipt headers. | yes, as a pattern (named commit, no worktree), not applied to receipt stamps | no | no |
| `tools/harness/r8_checks.py` | `receipt_identity` (110–125) is a tuple of spotcheck fields (row id, url, kind, locator, excerpt) for the round-7 parent leg. "Parent" here is the round-7 reconciliation, not `carrier^ == stamped`. | no | no (name collision only) | no |
| `tools/replay-frozen.py` | Replays a frozen `MANIFEST.tsv`: verifies `gate_sha256` / `input_sha256` / `output_sha256` before launch, copies the snapshot into an out-of-repo mirror, runs `[python3, tools/gates/<gate>.py, <input>]`, compares exit, `^FINDING ` count, and output bytes (docstring 13–29). Refuses `..`, symlinks, in-repo mirrors. The `command` column is never executed. No git log, no stamp header. | no (snapshot file copy, not `git show <lands>:`) | no | no |
| `tools/check-gate-battery.py` | Discovers committed `expected.json` under `tools/gates/expected/`, `tools/gates/frozen/`, and legacy `reports/round-9/baselines/`. Checks input digests, `gate_sha256` against the live script, registered-gate set, verdict-block shape (18–32). Explicitly does not re-execute: "the comparison is the baseline's own re-run receipt." | no | no | no |
| `tools/check-judged-object.py` | `git cat-file blob <rev>:<entry>` (code 107; docstring says `git show`) vs the packet key's `entry_sha256`. Catches post-verdict narrowing of the judged entry. Not a receipt-header check. | partial: committed bytes at a caller rev, for the entry, not for a stamp header | no | no |
| `tools/check-readme-revisions.py` | `^revision:` label uniqueness / stub / order on `corpus/README.md`. Selftest resolves a pinned commit with `git cat-file -e` and `git show <base>:corpus/README.md` (277–294) and scrubs `GIT_*` like receipt_guard (236–239). Its `receipt()` (229–232) is sha256 of the README text it just graded. | partial: one pinned path, README labels, not lands receipts | no | no |
| `tools/gates/*.py` (12 live) | `argot-derivation-gate.py`, `costume-era-consistency-gate.py`, `d4-assembly-check-gate.py`, `d4-typed-labels-check-gate.py`, `handoff-packet-check.py`, `lexicon-coverage-audit.py`, `myth-consistency-gate.py`, `naming-collision-gate.py`, `phonology-sanity-gate.py`, `provenance-audit.py`, `register-law-gate.py`, `typed-pipeline-gate.py`. Grade culture packets or corpus provenance. The two D4 adapters and `typed-pipeline-gate.py` exist so `replay-frozen.py` can launch `python3 tools/gates/<gate>.py <input>`. `tools/gates/frozen/**/freeze-receipt.json` and `MANIFEST.tsv` are data those tools consume, not a second sequencer. Copies under `tools/gates/frozen/**/inputs/tools/replay-frozen.py` are snapshots of the live replayer. Lore "stamp" strings inside expected packets are not verifiers. | no | no | no |

Not verifiers of this class, so not rows: `tools/check-readme-heading.py` `receipt()` (sha256 of a local README, no rev); `tools/harness/packet_links.py` `verify_manifest_digests` (live worktree sha256 vs a manifest pin).

## What check-receipt-seq adds

1. **Lands-evaluated receipt reads.** `--lands <40hex>` loads each receipt with `git show <lands>:<path>` (80–82, 235–236). A missing blob is `unreadable` FAIL, not a skip (131–134; selftest `lands-absent-is-fail` / `lands-read-committed`). `main` moving past lands is reported `moved_past=True` and the LANDS line is forced PASS (232–234). Separability and claims-freshness already read blobs at a named commit; neither parses a receipt, and neither has this flag. receipt_guard's `ls-tree` only answers "is a blob at this path on some ref."
2. **Topo carrier-parentage.** `--topo` runs `git log -1 --format=%H main -- <receipt>` and requires `carrier^ == stamped` (188–197). Absent carrier is FAIL (`topo-no-carrier-fail`), wrong parent is FAIL (`topo-wrong-parent-fail`). No sibling does this. r8's "parent" is a different predicate. The r66 Ca D2 leg lived in `reports/round-66/accept-ca.py`, not under `tools/`.
3. **Stamped/evaluated/measured equality.** All five headers required; missing is FAIL not skip; `stamped == evaluated == measured` (131–145), plus tree pin and, when a counter path is paired, counter sha. No sibling parses those lines.

## Contradiction (not a score)

The docstring (lines 13–17, 44–45) says `--lands` reads are committed bytes and `moved_past` never changes the verdict. `check_counter_sha` (168–170) always hashes `read_worktree` first, then `git show main:<counter>`, and `run` never passes the lands rev into that function (221–247). A dirty counter therefore changes the SHA leg while `--lands` is set. That is the fallback `claims-freshness.py` lines 49–58 forbids, and the opposite of separability's tree-scoped `cat-file`.

The 14 selftest expects never pair a counter under `--lands`. `lands-moved-flag` (337–338) passes `tools/counter-x.py` *as the receipt* and asserts only that the flag string appears. `sha-mismatch-fail` (396–399) is default mode (worktree). So `14/14` does not pin lands-scoped sha.

`reports/round-67/accept-o.py` line 166 and `reports/round-67/accept-ca.py` line 254 both require the literal `14/14`. Adding an `expect()` fails O's SELFTEST and Ca's SEQ together.

Residual, not this move: `git()` (63–66) copies `os.environ` and does not strip `GIT_DIR` / `GIT_WORK_TREE` / `GIT_OBJECT_DIRECTORY`. receipt_guard, claims-freshness, check-readme-revisions, and separability all scrub those. An inherited `GIT_DIR` can make `git show <lands>:<path>` read another object store. Also, `read_rev` decodes with `utf-8` replace and the sha leg re-encodes (174); accept-o hashes the counter with raw `rb` bytes (`accept-o.py` line 104). ASCII counters hide both.

## Proposed move (one)

**Under `--lands`, hash the counter blob at that commit, and pin it inside the existing `lands-moved-flag` expect so the count stays 14.**

In `check_counter_sha`, when a lands rev was supplied, sha256 the raw `git cat-file blob <lands>:<counter>` (the primitive `check-judged-object.py` line 107 and separability's batch reader already use). Do not call `read_worktree`. Do not fall back to `main`. Missing blob → `counter_absent` FAIL. Default mode (no `--lands`) keeps the worktree-then-main read so `sha-mismatch-fail` and `moved-receipt-fail` stay red.

Pin without a 15th check: in `fixture_repo`, commit a well-formed receipt `telemetry/at-lands.txt` in the *lands* commit (counter sha of `tools/counter-x.py` at that commit). Leave `telemetry/r-c.txt` for the records commit so `lands-absent-is-fail` still sees it missing. Widen the single `lands-moved-flag` expect to run `--lands <lands> telemetry/at-lands.txt tools/counter-x.py`, then rewrite the worktree counter, run again, and require both runs `SHA-` PASS and `moved_past=True`. One `expect` call; stdout still `14/14`.

## Axes

- Operability: improves. The lands path's committed-bytes claim becomes true for the counter pin, which is the leg that can still see a moved worktree. O's frozen SELFTEST string is unchanged if the expect count stays 14. ACCEPT-O's LANDS leg uses its own fixture and does not pair a counter (`accept-o.py` 194–198); it does not depend on the worktree fallback.
- Calibration: not harmed, provided no 15th `expect`. Ca SEQ greps `14/14` and does not assert worktree-sha-under-`--lands`. A new expect() would fail Ca; this move refuses that.
- Coverage: untouched. No corpus entry, no registry row.

## Risks

- Putting `r-c.txt` into the lands commit would flip `lands-absent-is-fail`. The new receipt must be a different path.
- `lands-moved-flag` today does not check exit code, because grading `counter-x.py` as a receipt is a missing-headers FAIL. After the argv change the expect must tolerate header PASS; do not require the old missing-headers behavior on that call.
- Raw `cat-file` vs utf-8 roundtrip: a non-UTF-8 counter would start matching accept-o's binary hash and stop matching the current encode path. Lane counters are Python source. Still hash raw bytes so the two cannot diverge later.
- `GIT_*` scrub is deliberately not in this move. Shipping only the sha fix leaves the inherited-`GIT_DIR` hole open.
- Do not relax topo to `merge-base --is-ancestor`. R66-D3's achieved predicate, and ACCEPT-O R66 (`accept-o.py` 262–288), is parent equality against `main`. Softening it would make a non-child carrier PASS and harm the operability claim.

## Verification (for the integrator; not run here)

1. `python3 -B tools/check-receipt-seq.py --selftest` exits 0 and the last line is `SELFTEST: 14/14`.
2. In that same run, `lands-moved-flag` detail shows `SHA-` PASS after the worktree counter differs from the lands blob.
3. `lands-absent-is-fail` and `lands-read-committed` still FAIL with `unreadable`.
4. `sha-mismatch-fail` still FAIL in default mode (worktree hash).
5. No edit to `accept-o.py` or `accept-ca.py` is required for the `14/14` pins. If a 15th expect is added instead, both counters must change in the same commit or O and Ca go red together.
