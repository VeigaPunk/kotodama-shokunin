# MutCaLedger — mutation attack on the Ca real 11-pair probe ledger (round-77 W2)

Seat: MutCaLedger (leaf, wave-2 falsifier). Attack target (named W1 artifact):
`.ufo/waves/round-77/w1/stage/ExecAdaptCa/probe-real-ledger.json` — the real
11-pair scratch probe ledger (D01–D10 ANNOTATE over real `LOG.md` lines, D11
REPAIR on real `corpus/README.md:755`) that W1's ExecAdaptCa graded with
`accept-ca.py --ledger-check` (report: `.ufo/waves/round-77/w1/ExecAdaptCa.md`,
"LEDGER-CHECK-77: PASS pairs=11"). Detector: that same `accept-ca.py`, copied
pristine into scratch, never modified — `--ledger-check` runs the same
`pair_problems()` the LEDGER leg runs (accept-ca.py:1614-1761), so per-pair
verdicts here are LEDGER-leg verdicts. Distinct from W1 MutLedgerPairs, which
attacked the DRAFT scout candidates with the round-76 counter; this seat
mutation-tests the REAL probe against the round-77 adapted counter's five
routed-defect classes.

Lane base `211f9526800906e0c585d878d265c37e5e090c15` (read-only). Scratch
`/fast/scratch/hyaku/kotodama-r77/MutCaLedger` (deleted after receipt copy).
Method: one pair mutated per ledger (verified single-field diffs), same
detector run on pristine → mutated → restored bytes.

## 0. Detector / input identity

```
sha256sum accept-ca.py probe-real-ledger.json            (scratch copies, pre-campaign)
ac2bc93d02932464f9ee43222ffe1d06dd5bf1a0e68fd38bd94e10a991489b2e  accept-ca.py
b7509d2b0980f8c5824c417a8359c8f7107d3de6236cf486ac058947915d0704  probe-real-ledger.json
```
Both byte-identical to the W1 stage sources (same command listed both copies).
Pair inventory asserted: ids D01..D11; D01–D10 `disposition=ANNOTATE`,
`stated_at` LOG.md:3/447/826/1234/1655/2036/2611/3078/3457/3787, observe/rederive
`git -C . grep -c -E '^#' 211f9526… -- LOG.md`; D11 `disposition=REPAIR`,
`stated_at corpus/README.md:755`, `expected_after 244`,
`statement_after {corpus/README.md, Total knowledge entries: ([0-9]+)\.}`.

## 1. MUTATION TABLE (one pair each; raw detector output verbatim)

Command form (cwd `/fast/scratch/hyaku/kotodama-r77/MutCaLedger`):
`python3 -B accept-ca.py --ledger-check <LEDGER>.json --root
/home/vgpnk/Projects/shokunin/kotodama-shokunin --base 211f9526… --work
/fast/scratch/hyaku/kotodama-r77/MutCaLedger/work`
(full transcript: `.ufo/waves/round-77/w2/stage/MutCaLedger/transcript.txt`)

| # | mutant (pair, field, change) | expected | raw output (problems lines) | exit | verdict |
|---|---|---|---|---|---|
| baseline | probe-real-ledger.json (pristine) | PASS 11 | `LEDGER-CHECK-77: PASS pairs=11` | 0 | baseline green — mutants judgeable |
| a | D01 `stated_text` `+ " (mutated)"` → absent at site | LEDGER red on D01 | `LEDGER-CHECK-77: FAIL pairs=11 problems=1` / `D01: stated_text not found in LOG.md at base` | 1 | KILLED (L76-19 class) |
| b1 | D02 `stated_at` `LOG.md:447` → `corpus/QUALITY.md:1` (base file, not in ANNOTATE_ALLOW) | allowlist red on D02 | `FAIL pairs=11 problems=2` / `D02: stated_at path corpus/QUALITY.md is not in the frozen ANNOTATE allowlist ['LOG.md', 'SCORECARD.md', 'corpus/lessons/round-75.md', 'corpus/lessons/round-76.md']` / `D02: stated_text not found in corpus/QUALITY.md at base` | 1 | KILLED (L76-13 class; 2nd red is the same pair's site re-check, expected) |
| b2 | D11 `stated_at` `corpus/README.md:755` → `LOG.md:3` (not in REPAIR_MUTABLE) | allowlist red on D11 | `FAIL pairs=11 problems=2` / `D11: stated_at path LOG.md is not in the frozen REPAIR allowlist ['corpus/README.md', 'SKILL.md', 'SHONEN.md']` / `D11: stated_text not found in LOG.md at base` | 1 | KILLED (disposition-specific allowlists hold on both dispositions) |
| c1 | D03 `observe_cmd` → `["python3","-c","print('1')"]` | interpreter refused | `FAIL pairs=11 problems=1` / `D03: observe_cmd interpreter/constant-printer binary 'python3' is refused (H2)` | 1 | KILLED |
| c2 | D04 `observe_cmd` → `["echo","1"]` | constant-printer channel closed | `FAIL pairs=11 problems=1` / `D04: observe_cmd argv[0] 'echo' not in the observe allowlist ['git', 'grep', 'wc', 'sha256sum', 'ls', 'cat', 'head', 'tail', 'cut'] (the echo/printf/interpreter channels are closed)` | 1 | KILLED |
| d | D05 `observe_cmd` append bare operand `chars=1200` | bare name=value refused | `FAIL pairs=11 problems=1` / `D05: observe_cmd git grep path operand 'chars=1200' is a bare name=value assignment (refused)` | 1 | KILLED |
| e2 | D06 `rederive` rev `211f9526…` → `main` | mutable-ref red on D06 | `FAIL pairs=11 problems=1` / `D06: rederive git grep revision operand 'main' is a mutable ref (pin a 40-hex or HEAD)` | 1 | KILLED |
| e1 | D07 `rederive` rev `211f9526…` → `HEAD` | mutable-ref red (draft: "immutable 40-hex revision in revision position") | `LEDGER-CHECK-77: PASS pairs=11` | 0 | **SURVIVED — coverage finding** |

Every killed mutant reds ONLY the mutated pair (1 problem; b1/b2 emit 2 problems,
both tagged with the mutated pair id); the other 10 pairs stay green in every run.

## 2. Survivor analysis (e1: `HEAD` in revision position) — coverage finding

- Mutation: D07's `rederive` `git -C . grep -c -E '^#' 211f9526… -- LOG.md` →
  `... '^#' HEAD -- LOG.md` (single field; all other 10 pairs and D07's other
  fields byte-identical, verified by JSON diff).
- Observed: `LEDGER-CHECK-77: PASS pairs=11`, exit 0. The rederive still
  executes and parses to the same token, so even the exec half of the check
  stays green.
- Code path: `REV_NAMES = ("HEAD", "HEAD^", "HEAD~1", "@")` (accept-ca.py:1070);
  `_git_rev_problem` returns None for any REV_NAMES token (1073-1083);
  `_mutable_ref` excludes REV_NAMES (1085-1092); role parsers print
  "(pin a 40-hex or HEAD)" (1204, 1240). Only non-REV_NAMES mutable-shaped
  tokens (e.g. `main`) are refused.
- Contract delta: CLAIMS-DRAFT Ca names the routed defect as "immutable 40-hex
  revision in revision position"; the enforced grammar accepts the mutable ref
  `HEAD` (and `HEAD^`, `HEAD~1`, `@`) there. This is a finding that the stated
  invariant is stronger than the enforced check — a coverage gap, NOT a
  contract change; the counter remains the spec.
- Bounded scope note: at `--ledger-check` (and LEDGER-leg) time this is
  observationally harmless — `materialize()` checks the base clone out
  detached at base and asserts `HEAD == base` (accept-ca.py:622-642), so a
  HEAD-pinned rederive still reads base bytes and matches
  `observed_at_base`. The exposure is semantic: a HEAD pin does not name an
  immutable revision the way the draft sentence requires, so the frozen
  sentence's guarantee is carried by the clone procedure, not by the pair
  grammar. Downstream lands-time re-derivations were NOT run by this seat
  (no lands tree exists in W2; reported as unrun, per W1's precedent).
- Suggestion to the freeze owner (advisory only): either narrow the draft
  sentence to match the enforced rule ("40-hex or HEAD; branch/tag names
  refused") or extend `_git_rev_problem` to refuse REV_NAMES in ledger pairs.
  Not changed by this seat.

## 3. Restoration evidence

```
[10] python3 -B accept-ca.py --ledger-check probe-real-ledger.json --root /home/vgpnk/Projects/shokunin/kotodama-shokunin --base 211f9526800906e0c585d878d265c37e5e090c15 --work /fast/scratch/hyaku/kotodama-r77/MutCaLedger/work
LEDGER-CHECK-77: PASS pairs=11
exit=0
sha256sum probe-real-ledger.json accept-ca.py <w1 stage copies of both>
b7509d2b0980f8c5824c417a8359c8f7107d3de6236cf486ac058947915d0704  probe-real-ledger.json   (pre == post)
ac2bc93d02932464f9ee43222ffe1d06dd5bf1a0e68fd38bd94e10a991489b2e  accept-ca.py             (pre == post)
b7509d2b0980f8c5824c417a8359c8f7107d3de6236cf486ac058947915d0704  w1/.../probe-real-ledger.json
ac2bc93d02932464f9ee43222ffe1d06dd5bf1a0e68fd38bd94e10a991489b2e  w1/.../accept-ca.py
```
Mutations never touched the wave-dir sources; mutants were fresh scratch bytes
(hashes in `stage/MutCaLedger/transcript.txt`, copies staged). Single-field
diffs verified programmatically for all 8 mutants (each exactly one
(id, field, before, after) tuple; meta round/claim/base and 11-pair inventory
unchanged).

## 4. Outcomes for the seat item

- "stated_text absent" → KILLED on the real probe (D01).
- "wrong allowlist path" → KILLED on both dispositions (D02 ANNOTATE, D11 REPAIR).
- "interpreter/constant-printer argv" → KILLED both halves (D03 python3 -c, D04 echo).
- "bare name=value operand" → KILLED (D05 `chars=1200` path operand).
- "mutable revision" → branch-name form KILLED (D06 `main`); `HEAD` form
  SURVIVED (D07) — coverage finding §2.
- "real 11-pair probe passes" → confirmed: baseline and restored-control runs
  `LEDGER-CHECK-77: PASS pairs=11`, exit 0, bytes unchanged.

## 5. Scope notes

- No lane/fleet file outside `.ufo/waves/round-77/w2/MutCaLedger.md` and
  `.ufo/waves/round-77/w2/stage/MutCaLedger/` was written; lane git/jj/index
  untouched (the detector only `git clone --no-checkout`s the lane read-only
  into scratch and asserts `rev-parse HEAD == base`).
- Fixture repos: none created by this seat (the detector materializes its own
  throwaway base clones under `--work`); all git access read-only.
- Unrun (reported as unrun): graded ACCEPT-CA-77 legs beyond the pair grammar
  (BASEMISMATCH, REPAIR, …) — no lands/freeze tree exists in W2; the e1
  survivor's lands-time behavior is cited from accept-ca.py lines, not executed.
- No tool installs; pacman never invoked; no background jobs; no task
  dispatch. Scratch `/fast/scratch/hyaku/kotodama-r77/MutCaLedger` deleted
  after the receipts above were copied into the stage dir.
