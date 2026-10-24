# RevToolSeq — attack review of `tools/check-receipt-seq.py` (round 67, w1)

Lane tip `b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21`, base `ad5b52b0ab5691358cd38718ab75649dc9916f9a`
(tool absent at base: `git show BASE:tools/check-receipt-seq.py` -> "exists on disk, but not in BASE", so
the DIFF leg of claim O is honest). Tool read in full (441 ln) and exercised in synthetic git lanes under
`/tmp/r67rts` (nothing written to the lane; no git/jj writes in the lane).

Attacked by name: **moved-worktree PASS claims**, **stale receipts**, **false stamps**, **bypass of the
counter pin**, **revision-vs-object confusion**, **arg parsing collisions**, **encoding-mangled receipts**,
**selftest coverage vs code paths**.

---

## HIGH

### H1. The counter sha256 pin is optional in practice — deleting it (or mangling it) yields `RECEIPT-SEQ: PASS`
`check_headers` requires only `("stamped","evaluated","measured","tree")` (ln 137); `counter_sha` is absent
from the required list. `check_counter_sha` then skips silently when `not h["counter_sha"]` (ln 166) and emits
**no leg at all**. The docstring (ln 24-32) says every receipt "must carry all of" the five headers, and
"a receipt missing a header line is a FAIL, not a skipped check" — both false for the fifth header.

Reproduced (lane2, counter paired, sha would have to be checked):

| receipt | counter pin | verdict |
|---|---|---|
| `telemetry/nosha.txt` | header line deleted entirely | `RECEIPT-SEQ: PASS` rc=0, **no SHA leg printed** |
| `telemetry/shortsha.txt` | `# counter sha256 (self): deadbeef` (not 64hex) | `RECEIPT-SEQ: PASS` rc=0, no SHA leg |
| `telemetry/upper.txt` | correct hash in **uppercase** | `RECEIPT-SEQ: PASS` rc=0, no SHA leg |
| `telemetry/lower.txt` (control) | same hash lowercase | `SHA-... PASS` rc=0 |

So the "counter sha" half of claim O's own statement ("header equality (stamped/evaluated/measured + tree +
counter sha)") is unenforced against a forged or truncated receipt: strip/obfuscate one line and the pin
disappears while the instrument still prints PASS. This is the false-stamp class the tool exists to kill.

### H2. `--lands` is committed-bytes for the receipt text but **worktree/tip for the counter** (ln 168-171)
`check_counter_sha` ignores `--lands` entirely: `read_worktree(root, cpath)` first, then
`read_rev(root, "main", cpath)`. Neither is the lands commit. Both directions of the r66/R66-D3 defect
reproduce:

* **False FAIL at lands** (lane2: P -> A(lands, counter v1 + receipt) -> B(counter v2)):
  `--lands A telemetry/r-c.txt tools/counter-x.py`
  -> `SHA-... FAIL tools/counter-x.py recorded=71016a91 actual=05f1bee0`, rc=1, while
  `git show A:tools/counter-x.py | sha256sum` = `71016a91…` — i.e. the receipt's pin is exactly right at lands.
  A counter edited *after* lands (the normal "fix the counter in a follow-up" case) makes the frozen
  instrument print FAIL for a truthful lands receipt.
* **False PASS at lands** (lane3: lands commit A carries a receipt pinning the sha the counter will only
  have at B): `--lands A telemetry/r-c.txt tools/counter-x.py` -> `SHA-... PASS recorded=2a6fc7bb
  actual=2a6fc7bb`, rc=0, while `git show A:tools/counter-x.py | sha256sum` = `71016a91…`. The lands commit's
  own counter does not match the pin and the tool says PASS.

Scope of the divergence: it needs `--root`'s worktree/HEAD to differ from `--lands` (a clone checked out at
lands is coincidentally right, because its worktree counter *is* `counter@lands`); the moment the same
instrument is pointed at a moved worktree — the case the docstring promises to handle — the leg silently
grades the wrong bytes in both directions.

Fix shape: in lands mode hash `read_rev(root, lands, cpath)` and never fall back to the worktree; keep the
worktree read only for tip mode.

### H3. `--topo` grades the **worktree** receipt against the **committed** carrier (ln 187-196)
`check_topo` takes `h["stamped"]` from `texts`, which in non-lands mode is `read_worktree(...)`, then compares
it to `parent(git log -1 main -- <path>)`. An uncommitted edit therefore decides the verdict. Reproduced in
lane2: receipt committed with `# stamped revision: 000…0` (so the committed bytes are wrong), then only the
worktree copy rewritten to the carrier's parent:
`--topo telemetry/topo2.txt` -> `TOPO-... PASS carrier=a85a66ec parent=01c5f8fa stamped=01c5f8fa`,
`RECEIPT-SEQ: PASS`, rc=0, with `git status --porcelain` showing ` M telemetry/topo2.txt`.
Since `reports/round-67/telemetry/post-records.txt` is exactly a `--topo` product generated from a worktree,
a dirty receipt at generation time can stamp TOPO PASS on bytes that were never committed.

Fix shape: read the graded text from the carrier blob (`git show <carrier>:<path>`), or refuse to run when
the path is dirty (`git status --porcelain -- <path>` non-empty).

---

## MEDIUM

### M1. `--lands` never binds the receipt's stamp to the lands revision — stale receipts pass
The only equality enforced is `stamped == evaluated == measured`; nothing asserts `stamped == lands`. Lane2
(lands = B, receipt stamped P, twice removed): `--lands B telemetry/r-c.txt` -> all legs PASS rc=0, and with
`--topo` also `TOPO-... PASS carrier=299e1e6f parent=4695fd95`. A receipt from any earlier round, unchanged in
the lands tree, is accepted as this round's lands evidence. The `LANDS` leg prints `moved_past` but is
hardcoded PASS (ln 232-234), so it cannot catch this. Claim O's LANDS fixture (accept-o.py ln 193-198) only
exercises the *absent-receipt* case, which is the one case that cannot be stale.

Fix shape: per-receipt leg `stamped == lands` in lands mode (or make the LANDS leg fail when any receipt's
stamp differs from lands).

### M2. `pair_args`: any second argument ending in `.py` is silently re-roled from receipt to counter (ln 113)
* `--root . telemetry/r-c.txt telemetry/helper.py` — `helper.py` is a **receipt**, but it is consumed as
  r-c's counter: it is never evaluated, no `SEQ-telemetry/helper.py` leg exists, and it produces a spurious
  `SHA-telemetry/r-c.txt FAIL ... actual=01e7ed0b`.
* Same with a header-less receipt: `telemetry/r-c.txt telemetry/bad.py` (bad.py = receipt with its sha line
  deleted) -> no leg for `bad.py`; the instrument never sees the invalid receipt.
* Position-dependent: `--root . telemetry/helper.py` alone *is* evaluated as a receipt (rc=0).
* `--root . "telemetry/r-c.txt:"` -> `ctr` is `""` -> `ctr or None` -> sha leg silently dropped, PASS rc=0
  (same silent-drop hole as H1, reached through the colon form).

The `.py` heuristic is a file-extension guess where an explicit pairing is needed; the docstring's
"`receipt:counter` pairs also accepted" is the unambiguous form and is **not** exercised by the selftest.
Also a relative path containing `:` is split at the first colon (`telemetry/r:67.txt` -> `SEQ-telemetry/r
FAIL unreadable`, i.e. a real path is truncated into a bogus one).

### M3. Selftest coverage does not reach the code paths that are broken (14/14 is true but not "every failure class")
`--selftest` prints `SELFTEST: 14/14`, rc=0 (verified). What the 14 fixtures never exercise:

| code path | exercised? |
|---|---|
| `--lands` **with a counter paired** (ln 168-171, H2) | **never** — both lands fixtures pass a receipt only |
| missing / malformed / uppercase `# counter sha256` (ln 137, 166, H1) | **never** |
| `--topo` on a dirty worktree (H3) | never |
| `receipt:counter` colon pairing (ln 110-112) | **never** — only the space form |
| receipt named `*.py` (ln 113) | never as a receipt (fixture `lands-moved-flag` passes `tools/counter-x.py` as the *receipt*, ln 338) |
| `--lands` + `--topo` combined (ln 249) | never |
| duplicate header lines / BOM / non-UTF-8 counter | never |
| repo without branch `main` (ln 229-230, 170, 241) | never |
| `read_worktree` -> `read_rev(main)` fallbacks (ln 241, 170) | never |
| `main()` exception handler -> rc=2 (ln 431-441) | never (the only rc=2s come from the explicit no-receipt/bad-lands branches) |

Also `expect("lands-moved-flag", "moved_past=True" in out)` (ln 338) asserts a substring only — rc, the
verdict, and the "receipt" identity are unchecked, so a crash after the LANDS line would still pass.

---

## LOW

### L1. No object-type check on `stamped` — a 40-hex **tree** object passes as a "revision"
`check_tree` does `rev_parse(root, f"{stamped}^{{tree}}")`, and `<tree>^{tree}` returns the tree itself, so a
tree id satisfies both the header and the tree pin: `telemetry/treeobj.txt` (all five headers set to
`1428f1be…`, a tree) -> `SEQ ... PASS`, `TREE ... PASS`, rc=0. Add `^{commit}` verification for
stamped/evaluated/measured. (`--lands` itself is guarded: a tree hash yields
`COULD-NOT-EVALUATE lands unresolvable`, rc=2, verified.)

### L2. sha256 is taken over decoded-then-re-encoded bytes, not file bytes (ln 72-78, 169, 175)
`read_worktree` decodes `utf-8`/`replace`; `actual = hashlib.sha256(blob.encode("utf-8"))`. A counter
containing one non-UTF-8 byte fails the pin: `tools/counter-latin.py` raw sha `29755b63…` vs tool-computed
`0102b4bf…`, receipt recording the true sha -> `SHA ... FAIL`. Same lossy decode for `git show` output.
Binary/latin-1 counters or a `.gitattributes`-normalized counter would trip this.

### L3. Hardcoded `main` (ln 170, 188, 229-230, 241)
In a repo without `main` the LANDS leg prints `LANDS PASS lands=1b653de8 head=none moved_past=False` — it
reports "not moved" when it cannot see the branch at all, and the tip-mode fallbacks are dead. A clone made
detached or with `--single-branch` on a differently named default branch silently loses the moved-past
signal.

### L4. Broken `--root` is graded as a predicate failure, not COULD-NOT-EVALUATE
`--root /tmp/r67rts/nope telemetry/r-c.txt` -> `SEQ ... FAIL unreadable`, rc=1. The contract reserves rc=2
for un-evaluable inputs; a clone that failed to materialize will be read as a genuine FAIL.

### L5. Duplicate header blocks: first match wins, no consistency check (ln 89-93)
A receipt carrying a correct block first and a contradictory block second (stamped/evaluated/measured to a
later rev, tree `ff…ff`) -> all legs PASS using the first block; the second block is invisible. Any other
reader (or a human) taking the last occurrence would disagree with the instrument.

---

## Verified clean (attacked, did not break)

* **Receipt text at `--lands` really is `git show <lands>:<path>`** (ln 236): a receipt committed only in a
  later commit is `unreadable` at lands (selftest `lands-absent-is-fail`, `lands-read-committed`); the moved
  worktree copy is not consulted. Only the counter leg (H2) breaks the claim.
* **CRLF receipts and CRLF counters**: both fully clean. Receipt with `\r\n` + matching counter -> all three
  legs PASS rc=0; CRLF counter file whose receipt records the raw sha -> `SHA ... PASS`. (`\s*$` before the
  MULTILINE `$` absorbs `\r`.)
* **UTF-8 BOM**: the BOM-mangled sha line degrades into H1 (silent pin drop -> PASS); the *verdict* failure is
  H1's, not a separate encoding bug. A receipt whose only headers are on a BOM'd first line fails closed.
* `--lands` argument shape: non-40hex or unresolvable -> rc=2 `COULD-NOT-EVALUATE`; a tree hash is rejected
  by `^{commit}`.
* `--selftest` exits 0 and prints `SELFTEST: 14/14`; the count itself is honest (14 `expect()` calls).

---

## Residual risk / verification gaps

* I did not run any accept-*.py or the real r67 receipts in a materialized clone (ExecCounterSmokeO /
  CriticReceiptDiscipline own that). **None of this round's frozen predicates can be flipped by H1-H3**: the
  only accept-script calls into the tool are accept-o.py ln 193-198 (`--lands` **without** a counter, on an
  absent receipt — so the counter leg never runs) and ln 204-221 (`--topo` on a clean fixture worktree), plus
  accept-ca.py ln 251 (`--selftest` only; Ca's SEQ leg is a **source-text** grep — `--lands` presence,
  header strings, `mv_rev == lands` — not a behavioural check) and the separately generated post-records
  artifact. Latent != benign: the tool is committed as the round's reusable instrument, and a later round
  invoking the documented `[receipt] [counter]` form under `--lands` inherits H2 silently.
* H2's divergence is **conditional on the `--root` worktree/HEAD differing from `--lands`** — i.e. exactly
  the shape claim O advertises handling ("a fixture repo whose main moved past lands"). A clone checked out
  at lands has worktree counter == counter@lands, so H2 is benign *in that shape*; the dry-run receipts show
  the real runs use `.scratch/eval-base`-style scratch roots, so the guard has to be the code, not the habit.
* Parent resolution (per-claim lands separation A_r -> A_c -> A_ca) makes M1 sharper, not moot: three
  different lands revisions mean a receipt legal at A_c is stale at A_ca, and `--lands` currently cannot tell
  them apart (no `stamped == lands` leg). Implementing M1's one-line per-receipt leg is what makes the
  separation auditable by the instrument instead of by hand.
* `post-records.txt` does not exist yet at the lane tip, so H3's real-world impact could not be measured.
* The five `mut-o` mutants were not audited for kill-map correctness (RevCounterO's item); note that mutants
  mut1/mut3/mut5 target legs this review shows the selftest never pairs with `--lands`, so mutant kudos do
  not cover H2/H1.
* No tool installed or upgraded (python3 + git only, pacman paused per the 2026-10-20 guard).

Report: .ufo/waves/round-67/w1/RevToolSeq.md
Scratch lanes: /tmp/r67rts/lane1, lane2, lane3, nomain (throwaway, outside the lane)
