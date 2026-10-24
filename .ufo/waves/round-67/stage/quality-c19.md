# ScribeQualityC19 — draft `corpus/QUALITY.md` criterion 19 (stage, L1 integrates)

Axis: calibration. Scope: report-only draft; no product files changed. Append the
block below to `corpus/QUALITY.md` as item 19, after criterion 18 (the file ends at
18 today, 57 lines). Text only — the L1 writes the file.

## Draft (weave-format single item, house style of 16–18)

```markdown
19. **Receipts run at the revision they stamp, and carrier-parentage is post-records** — adds to criterion 17, which pins the revision the read-path bytes equalled; this criterion pins where the run happens, how the receipt proves it, and which legs can only exist after the records commit. Before data, every round counter takes a required lands revision (`--lands <40hex>`) and never grades whatever worktree it happens to sit in: the evaluation runs at that revision — inside a clone materialized at it, or over committed bytes read from it (`git show <lands>:<path>`) — and the receipt proves stamp and evaluation agree, carrying `# stamped revision:`, `# evaluated revision:`, `# measured revision (lane main):`, `# tree:` and `# counter sha256 (self):` with stamped == evaluated == measured and the tree equal to `git rev-parse <stamped>^{tree}`. A run whose evaluated revision differs from its stamp prints FAIL and is not a receipt; a receipt that does not exist at the lands revision is a FAIL (`unreadable`), never a skip; a receipt carrying no stamped/evaluated headers is `missing_headers`, not retroactively gradable, and a pre-protocol receipt is re-derived by hand from `git log -1 --format=%H main -- <receipt>` and `git rev-parse <carrier>^` — no header is ever written onto its original bytes. Where a round's claims land in separate commits, each receipt stamps its own claim's lands commit: an earlier claim's receipt is never re-run at a later tip to cover it, and rows a later commit adds are never graded by it (criterion 7's separability, applied to receipts). Carrier-parentage — the commit that carries a receipt has the stamped revision as its parent — cannot be a lands-time leg, because at the lands revision its own carrier does not exist yet: it is post-records evidence, graded after the records commit with `--topo`, committed as its own telemetry file, and cited by no frozen predicate (a lands-time carrier leg can only print FAIL). Limits, stated: `--topo` needs a stamped header, so a pre-protocol receipt answers `no_stamp_header`; the counter-sha leg runs only for a receipt paired with its counter and is skipped — not failed — when the `# counter sha256 (self):` line is absent (criterion 17's pin and the round's accept-ca RECEIPTS leg carry that leg); and in `--lands` mode the paired counter is resolved from the worktree with `main` as fallback, so a counter edited after lands fails the sha leg instead of passing. Check: `python3 -B tools/check-receipt-seq.py --root <repo> --lands <40hex> <receipt> [<counter>]` exits 0, and `python3 -B tools/check-receipt-seq.py --root <repo> --topo <receipt>...` exits 0 post-records (exit 1 a grading failure, exit 2 `COULD-NOT-EVALUATE`); `python3 -B tools/check-receipt-seq.py --selftest` prints `SELFTEST: 14/14`. Shown able to fail: at lane tip `b78f8b8e` (tool sha256 `3e06e502…`, observed 2026-10-24) `--selftest` prints the killer fixtures' own lines — `moved-receipt-fail SEQ-telemetry/moved.txt FAIL stamped=3b8e9248 evaluated=21db62ca measured=3b8e9248 equal=False`, `missing-headers-fail SEQ-telemetry/bare.txt FAIL missing_headers=['stamped', 'evaluated', 'measured', 'tree']`, `topo-no-carrier-fail … TOPO-telemetry/never.txt FAIL no_carrier`, `topo-wrong-parent-fail … TOPO-telemetry/wrongparent.txt FAIL carrier=85b5bc05 parent=21db62ca stamped=3b8e9248`; `--lands ad5b52b0ab5691358cd38718ab75649dc9916f9a reports/round-67/telemetry/dry-run-ca.txt` answers `SEQ-reports/round-67/telemetry/dry-run-ca.txt FAIL unreadable` then `RECEIPT-SEQ: FAIL` (exit 1) for a receipt absent at lands; `--topo` over round 66's three receipts answers `SEQ-… FAIL missing_headers=['stamped', 'evaluated']` and `TOPO-… FAIL no_stamp_header` (exit 1). The class is already on disk: round 66's committed `reports/round-66/telemetry/final-measures-ca.txt` prints `D2 FAIL bad=['reports/round-66/telemetry/final-measures-c.txt:no_carrier', …]` then `ACCEPT-CA-66: FAIL` while the same parentage re-derives green at tip, and round 65's committed `reports/round-65/telemetry/accept-ca-post-records-fail.txt` prints `RECEIPTS FAIL lands=53a60275 bad=['reports/round-65/telemetry/final-measures-c.txt:lands_stamp', …:tree', …]` then `ACCEPT-CA-65: FAIL`. Grounded in `corpus/lessons/round-66-verifier-spotcheck.md` §5 item R66-D3 ("the Ca counter's D2 leg can only print PASS after the records commit it is filed in; a receipt stamped at lands therefore always records FAIL for D2 … Either re-run post-records and commit the PASS run alongside (preserving the FAIL run), or make D2 take `--lands <hash>` and grade carrier-parentage against it explicitly") and §2 claim Ca (the receipts re-derived at tip), and in the round-65 class at `corpus/lessons/round-65.md#mistakes` R65-M9 with R65-D2 (records commit not a direct child of lands; "no retargeting after data") and the receipt `reports/round-65/telemetry/accept-ca-post-records-fail.txt`; drafted by seat ScribeQualityC19 (`.ufo/waves/round-67/w1/ScribeQualityC19.md`).
```

## Scope and compliance notes for the L1

- **Numbering/placement:** criterion 18 is the last item (`corpus/QUALITY.md`,
  57 lines); insert 19 after it, still inside the numbered list. The `19. ` must
  start a line (`^19\.\s`) — the round's accept-ca CRITERION leg matches that.
- **Round-67 CRITERION leg compatibility (observed contract, not a claim):**
  `reports/round-67/accept-ca.py:258-265` searches `(?m)^\s*19\.\s`, then requires
  `receipt`, `stamped` and `lands` (lowercased) inside the first 1200 characters
  of the item. The draft's title and first sentence carry all three. The pre-data
  control already shows the leg failing on base bytes: `CRITERION FAIL QUALITY
  criterion 19 names receipt sequencing` in
  `reports/round-67/telemetry/dry-run-ca.txt` (base `ad5b52b0`).
- **No duplication with 17:** 17 keeps the measured-revision/tree/counter-sha pin
  and the preservation of superseded bytes; 19 adds the stamped-vs-evaluated
  equality, the location of the run (materialized clone or `--lands` committed
  bytes), and the post-records-only status of carrier-parentage. If the L1 edits
  for brevity, keep both "adds to criterion 17" and the "cited by no frozen
  predicate" clause — the latter is the R66-D3 fix.
- **Per-claim lands (L1 ruling, r67):** the criterion's "each receipt stamps its
  own claim's lands commit" sentence exists so the round's C-APPEND vs Ca-D4 id
  conflict is legible as sequencing, not as a counter defect: C is graded at its
  own lands `A_c` (base + S801–S804 + S805–S828 only), Ca at `A_ca` (which adds
  the S829+ rejects). A closure that re-runs C's receipt at the final tip would
  reintroduce the conflict the ruling avoided; criterion 19 forbids exactly that
  re-run ("never re-run at a later tip to cover it"). Verified against the
  frozen counters: `accept-c.py` `NEW_IDS = S805..S828`, `EXTRA_IDS =
  {S801..S804}`, ROWS requires `c[7]=='mined'`; base carries **0** rows with
  `rejected` + `2026-10-24` (awk over `git show ad5b52b0:corpus/SOURCES.md`), so
  at `A_c` the maximum `rej_opened_today` is 4 and at `A_ca` it reaches 6+ only
  with the extra rejects — satisfiable exactly as sequenced, never jointly at
  one revision.
- **Precision kept deliberately:** the checker's own limits are named in the
  text rather than implied, so the criterion cannot be read as claiming the sha
  leg is mandatory in `check-receipt-seq.py` (it is skipped when the header is
  absent) or that `--lands` pins the counter blob (it reads the worktree first,
  `main` second; the failure direction is conservative — a moved counter fails).
  Dropping these would make the landed criterion stronger than the tool.

## Evidence observed for this draft (read-only, lane tip `b78f8b8e`)

| observation | command | output (verbatim, abridged) |
|---|---|---|
| selftest 14/14, exit 0 | `python3 -B tools/check-receipt-seq.py --selftest` | `SELFTEST: 14/14`; per-fixture `RECEIPT-SEQ: FAIL` lines quoted in the draft |
| lands-absent is FAIL | `… --root . --lands ad5b52b0ab5691358cd38718ab75649dc9916f9a reports/round-67/telemetry/dry-run-ca.txt` | `LANDS PASS lands=ad5b52b0 head=b78f8b8e moved_past=True (evaluating committed bytes at lands)` / `SEQ-…:dry-run-ca.txt FAIL unreadable` / `RECEIPT-SEQ: FAIL`, exit 1 |
| pre-protocol receipts ungradable | `… --root . --topo reports/round-66/telemetry/final-measures-{c,o,ca}.txt` | `SEQ-… FAIL missing_headers=['stamped', 'evaluated']` ×3, `TOPO-… FAIL no_stamp_header` ×3, `RECEIPT-SEQ: FAIL`, exit 1 |
| r65 class receipt | read `reports/round-65/telemetry/accept-ca-post-records-fail.txt` | `RECEIPTS FAIL lands=53a60275 bad=[…:lands_stamp, …:tree ×3]`, `ACCEPT-CA-65: FAIL` |
| r66 class receipt | read `reports/round-66/telemetry/final-measures-ca.txt` | `D2 FAIL bad=[…:no_carrier ×3]`, `ACCEPT-CA-66: FAIL` |
| tool identity | `sha256sum tools/check-receipt-seq.py`; `git ls-files --error-unmatch …` | `3e06e502e5a6653b5ded85b189c7c8e8d2ceeeb32965faa8a60066aea0d78a26`, TRACKED |

## Limits and dependencies

- The tool is tracked but may still be edited by the O seat before lands; the
  quoted selftest/`--lands`/`--topo` output is scoped to tool sha `3e06e502` at
  lane tip `b78f8b8e`. If the tool changes, only the `Shown able to fail`
  sentences need re-observation; the criterion body describes behaviour I read
  in the source (`check_headers`, `check_tree`, `check_counter_sha`,
  `check_topo`, `run`) as well as observed.
- `reports/round-67/telemetry/post-records.txt` does **not** exist yet (expected:
  claims.json files it as post-records evidence in a third lane commit). The
  draft does not cite it.
- I did not run any r67 frozen counter, did not edit product files, did not
  commit, and made no git/jj writes.
