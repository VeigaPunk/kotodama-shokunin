# ScribeQualityC19 — criterion 19 draft (round 67, W1)

Seat: scribe (build/scribe, draft-only). Lane: kotodama-shokunin, base
`ad5b52b0ab5691358cd38718ab75649dc9916f9a`, observed at lane tip `b78f8b8e`
(read-only). Report path: `.ufo/waves/round-67/w1/ScribeQualityC19.md`
Report: .ufo/waves/round-67/w1/ScribeQualityC19.md

## Behavior (deliverable)

Drafted `corpus/QUALITY.md` criterion 19 as text only, at the path the item
names: `.ufo/waves/round-67/stage/quality-c19.md`. The item is a single
paragraph line (4724 chars) in the house style of criteria 16–18: bold title +
em-dash, "adds to criterion 17", body prose, `Check:` with exact argv,
`Shown able to fail:` with verbatim observed lines, `Grounded in:` with the
lesson sections, "drafted by seat".

Content of the criterion, as drafted:

1. Every round counter takes a **required** `--lands <40hex>`; evaluation runs
   at that revision — inside a clone materialized at it, or over committed
   bytes read from it (`git show <lands>:<path>`) — never on a worktree that
   may have moved past the stamp.
2. The receipt carries `# stamped revision:`, `# evaluated revision:`,
   `# measured revision (lane main):`, `# tree:`, `# counter sha256 (self):`,
   with stamped == evaluated == measured and tree == `git rev-parse
   <stamped>^{tree}`; stamp≠evaluated prints FAIL and is not a receipt; a
   receipt absent at lands is FAIL `unreadable`, never a skip; a receipt with no
   stamped/evaluated headers is `missing_headers` and is not retroactively
   gradable (re-derived by hand from `git log -1 --format=%H main -- <receipt>`
   and `git rev-parse <carrier>^`, never by writing headers onto its bytes).
3. Carrier-parentage (carrier's parent == stamped revision) is **post-records
   evidence only**: graded after the records commit with `--topo`, committed as
   its own telemetry file, and cited by no frozen predicate — at lands its own
   carrier does not exist, so a lands-time carrier leg can only print FAIL.
4. `Limits, stated:` `--topo` needs a stamped header (`no_stamp_header`
   otherwise); the counter-sha leg is skipped — not failed — when the sha
   header is absent; `--lands` resolves the paired counter from the worktree
   with `main` as fallback (conservative: a counter moved after lands fails).
5. `Check:` `python3 -B tools/check-receipt-seq.py --root <repo> --lands <40hex>
   <receipt> [<counter>]` exits 0; `--topo` exits 0 post-records (1 grading
   failure, 2 `COULD-NOT-EVALUATE`); `--selftest` prints `SELFTEST: 14/14`.
6. `Grounded in` `corpus/lessons/round-66-verifier-spotcheck.md` §5 item
   **R66-D3** (quoted: the D2 leg "can only print PASS after the records
   commit it is filed in"; fix = re-run post-records preserving the FAIL run,
   or make D2 take `--lands` and grade carrier-parentage explicitly) and §2
   claim Ca; and the round-65 class: `corpus/lessons/round-65.md#mistakes`
   R65-M9 + R65-D2 ("no retargeting after data") with the committed receipt
   `reports/round-65/telemetry/accept-ca-post-records-fail.txt`. The
   `accept-ca-post-records-fail.txt` class is named in the `Shown able to fail`
   sentence with its verbatim `RECEIPTS FAIL lands=53a60275 …`
   `ACCEPT-CA-65: FAIL`.

Added after the L1's per-claim-lands ruling (r67, in-wave): the criterion body
now also says "Where a round's claims land in separate commits, each receipt
stamps its own claim's lands commit: an earlier claim's receipt is never re-run
at a later tip to cover it, and rows a later commit adds are never graded by
it". This is what makes the round's C-APPEND vs Ca-D4 id conflict survive as
sequencing rather than as a counter defect (see finding 7). Re-simulated the
accept-ca CRITERION window after the edit: `^19\.\s` matches, `receipt` at
char 6, `lands` at 341, `stamped` at 637 — all inside 1200.

## Gates (all read-only; nothing executed as a product verification)

| command | observed |
|---|---|
| `python3 -B tools/check-receipt-seq.py --selftest` | `SELFTEST: 14/14`, exit 0; killer fixtures print `moved-receipt-fail … FAIL stamped=3b8e9248 evaluated=21db62ca measured=3b8e9248 equal=False`, `missing-headers-fail … missing_headers=['stamped', 'evaluated', 'measured', 'tree']`, `topo-no-carrier-fail … FAIL no_carrier`, `topo-wrong-parent-fail … FAIL carrier=85b5bc05 parent=21db62ca stamped=3b8e9248` |
| `… --root . --lands ad5b52b0ab5691358cd38718ab75649dc9916f9a reports/round-67/telemetry/dry-run-ca.txt` | `LANDS PASS lands=ad5b52b0 head=b78f8b8e moved_past=True (evaluating committed bytes at lands)`; `SEQ-…:dry-run-ca.txt FAIL unreadable`; `RECEIPT-SEQ: FAIL`, exit 1 |
| `… --root . --topo reports/round-66/telemetry/final-measures-{c,o,ca}.txt` | `SEQ-… FAIL missing_headers=['stamped', 'evaluated']` ×3; `TOPO-… FAIL no_stamp_header` ×3; `RECEIPT-SEQ: FAIL`, exit 1 |
| `… --root . reports/round-65/telemetry/final-measures-ca.txt reports/round-65/accept-ca.py` | `SEQ-… FAIL missing_headers=['stamped', 'evaluated', 'tree']`; `SHA-… PASS recorded=550c89a4 actual=550c89a4`; `RECEIPT-SEQ: FAIL`, exit 1 |
| `sha256sum tools/check-receipt-seq.py`; `git ls-files --error-unmatch …` | `3e06e502e5a6653b5ded85b189c7c8e8d2ceeeb32965faa8a60066aea0d78a26`, TRACKED |
| simulation of `reports/round-67/accept-ca.py:258-265` over the draft | `^19\.\s` matched; `receipt`, `stamped`, `lands` all inside the 1200-char window; item is 1 line |

The draft's `Shown able to fail` sentence quotes only observed output; the
observation is scoped to tool sha `3e06e502` at tip `b78f8b8e`.

## Touched surfaces

- Wrote `.ufo/waves/round-67/stage/quality-c19.md` (draft, 8960 bytes).
- Wrote `.ufo/waves/round-67/w1/ScribeQualityC19.md` (this report).
- No product file, no `corpus/QUALITY.md`, no counter, no tool, no test, no
  commit, no git/jj write, no push. No tool installed or upgraded.
- Read-only reads: `corpus/QUALITY.md`, `corpus/lessons/round-6{5,6}*.md`,
  `reports/round-67/claims.json`, `reports/round-67/accept-ca.py`,
  `reports/round-67/telemetry/{dry-run-ca,controls-ca}.txt`,
  `reports/round-6{5,6}/telemetry/*`, `tools/check-receipt-seq.py`,
  `.ufo/waves/round-62/w1/ScribeQuality16.md` (style).

## Findings for the L1 / attacking seats

1. **Draft is CRITERION-leg compatible.** Simulated the accept-ca leg's own
   regex and keyword window over the drafted item: PASS-shaped. The base control
   already shows the leg failing without the item (`CRITERION FAIL QUALITY
   criterion 19 names receipt sequencing`,
   `reports/round-67/telemetry/dry-run-ca.txt`), so the leg has a demonstrated
   red at base and will go green only when the text lands. Any L1 shortening
   must keep `receipt`/`stamped`/`lands` inside the first 1200 chars — the title
   alone does not carry "stamped"; the header names do.
2. **`--topo` cannot grade round 66's receipts as they stand.** They carry
   `# measured revision (lane main):`, `# tree:`, `# counter sha256 (self):` but
   no `# stamped revision:` / `# evaluated revision:`, so the raw tool answers
   `missing_headers` / `no_stamp_header`. The O claim's R66 leg therefore can
   only run on a header-bearing *derived* copy (`reports/round-67/accept-o.py`
   builds synthetic receipts at lines 193–229). Criterion 19 forbids writing
   headers onto a receipt's original bytes; if the O receipt does use a
   synthesized copy, it must be labelled a derived fixture (or the parentage
   line derived by hand as in `round-66-verifier-spotcheck.md` §2) so the pass
   is not read as the r66 receipts themselves grading green. This is the one
   place the claim and the criterion could be made to disagree.
3. **`check-receipt-seq.py --lands` does not pin the counter blob at lands.**
   `check_counter_sha` (`tools/check-receipt-seq.py:160-178`) resolves the
   paired counter with `read_worktree(root, cpath)` first (`:168`) and
   `read_rev(root, "main", cpath)` second, while the receipt itself is read with
   `read_rev(root, lands, rpath)`. Direction is safe (a counter edited after
   lands fails the SHA leg), but it is not "committed bytes at lands" for the
   counter. Criterion 19 names this as a stated limit; if the O seat wants the
   strict reading, `check_counter_sha` should take the lands revision. Either
   way the landed criterion must not be stronger than the tool (it currently is
   not).
4. **`check_headers` does not require the counter-sha header.** The missing
   list is `("stamped", "evaluated", "measured", "tree")`
   (`tools/check-receipt-seq.py:137-138`); a receipt omitting
   `# counter sha256 (self):` passes the SEQ leg, and the SHA leg is skipped
   when unpaired or header-absent. Criterion 17's pin plus the accept-ca
   RECEIPTS leg carry that leg; criterion 19 says so explicitly. Worth an O-seat
   decision, not a blocker.
5. **`reports/round-67/telemetry/post-records.txt` is absent** (expected per
   claims.json: post-records evidence in a third lane commit). The draft cites
   it nowhere; when it lands, its own stamped==evaluated equality is review-only
   by hand (no hash of its own carrier can exist before it is committed) —
   consistent with criterion 19's "cited by no frozen predicate" clause.
6. **Criterion 19 does not supersede 17** and must not absorb it: 17 keeps the
   measured-revision/tree/counter-sha pin and byte preservation; 19 adds
   stamped-vs-evaluated equality, the location of the run, and the
   post-records-only status of carrier-parentage. If the L1 trims, keep
   "adds to criterion 17" and the "cited by no frozen predicate" clause — the
   latter is the entire R66-D3 fix.

7. **C-APPEND vs Ca-D4 id conflict — verified, and resolved by per-claim lands
   (L1 ruling), not by counter revision.** CriticFrontier's F1 is correct on the
   frozen bytes and I re-derived it independently: `reports/round-67/accept-c.py`
   sets `NEW_IDS = S805..S828` and `EXTRA_IDS = {S801..S804}`, APPEND bounds
   `allowed_new = NEW_IDS | EXTRA_IDS` (`:357-358`), and ROWS requires every
   NEW_ID `status == mined` (`:267`); `accept-ca.py` D4 requires
   `rej_opened_today >= len(R66_REJECTS)+2 = 6` (`:226,235`) while base carries
   **0** rows with `status=rejected & opened=2026-10-24` (awk over
   `git show ad5b52b0:corpus/SOURCES.md`), and APPEND's immutable clause fixes
   cell 8 (`opened`) for base rows (`:369`), so no in-place re-dating can count.
   Maximum dated rejects at one revision without an id outside
   `NEW_IDS|EXTRA_IDS` is therefore 4 < 6 — jointly unsatisfiable at a single
   revision, as stated. The L1's ruling (A_r → A_c → A_ca; C's receipt run at
   `A_c`, Ca's at `A_ca`) makes both predicates hold at their own lands: at
   `A_c` the appended set is exactly `EXTRA_IDS|NEW_IDS` (APPEND PASS, no
   dated-reject requirement in C), at `A_ca` dated rejects reach 6+ (D4 PASS,
   no APPEND leg in Ca). The criterion-19 clause "each receipt stamps its own
   claim's lands commit … never re-run at a later tip" is what keeps this
   honest; a closure that re-graded C at the final tip would resurrect the
   conflict. Residual notes: (a) each receipt's carrier must still be a direct
   child of *its own* lands for `--topo` (three lands, not one), (b) claim C's
   statement arithmetic "724 -> 752" and Ca's ">=2 further rejects" (=> 756 at
   `A_ca`) remain text-inconsistent in `claims.json`; fixed only if the L1
   re-aligns the statement — no counter reads total row count, so no leg is
   affected. The frozen instruments contain no cross-counter satisfiability
   check (the SEQ leg checks `--lands`/headers/equality, not arithmetic), which
   is why the conflict had to be caught by attack seats.

## Out of scope (not done, by design)

- No edit to `corpus/QUALITY.md`, `corpus/SOURCES.md`, counters, tools, lesson,
  LOG/SCORECARD; no claim, matter, or judgment; no commit/push/jj writes.
- No r67 frozen counter run (C/O/Ca receipts are the executors' and Ca's
  evidence, not mine); no mutation-fixture adjudication
  (`.ufo/waves/round-67/stage/mut-o/` belongs to claim O's MUT leg).
- Nothing in this report upgrades a draft into a landed criterion: criterion 19
  is *text drafted and leg-simulated only*, not landed bytes.

## Artifacts

- Draft: `.ufo/waves/round-67/stage/quality-c19.md`
- Report: `.ufo/waves/round-67/w1/ScribeQualityC19.md`
