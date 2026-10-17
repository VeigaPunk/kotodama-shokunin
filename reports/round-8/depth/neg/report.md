# R8-D12 — Negative examples: two malformed D2 label packets (run receipts)

- round: 8 · shard: D12 (negative examples) · owner: L2 worker, kotodama-shokunin lane
- date: 2026-10-17 (UTC)
- baseline revision: `e7ca0faeb6680fa9891b907be628d9db578c28f4` (`reports/round-8/claims.json:5`)
- canon: NON-CANON test fixtures. Nothing here is a culture design, a canon
  record, a handoff or a real-world claim.
- tool under test: `tools/d2-typed-labels.py`. The shard ran against the
  integrated `--packet` build; the receipt in §3 was taken at sha256
  `3548185cd9c10c01523f872930feb407fb9dca58e7d854c295e3a77b0a7a703e`
  (2026-10-17T20:30:16Z), the build that also passed `--selftest` (exit 0) and
  evaluated the live packet (exit 1) at 20:30:10Z. D02 was editing the tool
  throughout this shard (eleven digests observed, §5); the runner prints the
  digest it actually ran, so re-running re-pins the receipt.
- files written by this shard:
  - `reports/round-8/depth/neg/packet-12a.unterminated-label-window.yml`
  - `reports/round-8/depth/neg/packet-12b.anchor-in-label-text.yml`
  - `reports/round-8/depth/neg/run-negatives.sh`
  - `reports/round-8/depth/neg/report.md` (this file)

## 1. The two malformed packets

Each packet is a small typed-label packet in the strict-loader subset of
`reports/round-8/depth/shard-parser.md` §4, with one clean control label and one
label record carrying the single defect.

| Case | Fixture (path, sha256) | Single defect | Expected code | Observed diagnostic (stdout) |
|---|---|---|---|---|
| neg-12a | `packet-12a.unterminated-label-window.yml` `3c00d4c5bbb8051194d6a94c553e4ba739811dc5e2337d7db1899119c15f5efa` | LBL-N12A-02's `era_window: [E0, E2` is left open | `P-UNTERMINATED-FLOW`, exit 2 | `FINDING D2L-DATA: [fail] <path> — flow sequence not closed` |
| neg-12b | `packet-12b.anchor-in-label-text.yml` `e8ddc9c71c47fd71e5777b8ada58ef6e6709206468cb61eea37a31b36ac15812` | LBL-N12B-02's `text: *the-transit-coat` uses an alias | `P-ANCHOR-TAG`, exit 2 | `FINDING D2L-DATA: [fail] <path> — anchor, alias or tag is outside the accepted subset` |

The two failure classes are distinct (an unterminated flow collection versus a
forbidden anchor/alias), both are label-level defects, and both sit in the
loader stage that runs before any pipeline capability — so the refusal is
unaffected by the rank/reconciliation churn the tool was undergoing (§5).

## 2. How the tool is run against them

The integrated tool reads one packet (`--packet PATH`, default the live D2
packet) through the strict loader of `shard-parser.md` §4.1; malformed input
returns exit 2 with a `D2L-DATA` finding and a stable message.

```sh
python3 tools/d2-typed-labels.py --packet reports/round-8/depth/neg/packet-12a.unterminated-label-window.yml
python3 tools/d2-typed-labels.py --json  --packet reports/round-8/depth/neg/packet-12b.anchor-in-label-text.yml
```

The runner does both, twice per case, plus the live packet as the positive
control:

```sh
sh reports/round-8/depth/neg/run-negatives.sh
```

## 3. Receipt — verbatim runner output, 2026-10-17T20:30:16Z, exit 0

```text
R8-D12 negative controls — tools/d2-typed-labels.py (integrated --packet interface)
date: 2026-10-17T20:30:16Z
tool: /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/d2-typed-labels.py
tool sha256: 3548185cd9c10c01523f872930feb407fb9dca58e7d854c295e3a77b0a7a703e

positive control (live packet): exit 1 (want 0 or 1, never 2), traceback: none

== case neg-12a-unterminated-label-window ==
fixture:        /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-8/depth/neg/packet-12a.unterminated-label-window.yml
fixture sha256: 3c00d4c5bbb8051194d6a94c553e4ba739811dc5e2337d7db1899119c15f5efa
expected:       P-UNTERMINATED-FLOW, exit 2
malformed run: exit 2 and 2 (want 2/2), --json exit 2, traceback: none
stdout (byte-identical across both runs):
  FINDING D2L-DATA: [fail] /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-8/depth/neg/packet-12a.unterminated-label-window.yml — flow sequence not closed
json finding: {"exit_code": 2, "findings": [{"code": "P-UNTERMINATED-FLOW", "detail": "flow sequence not closed", "id": "D2L-DATA", "severity": "fail", "where": "...packet-12a.unterminated-label-window.yml"}], "ok": false, "packet": "...packet-12a.unterminated-label-window.yml", "stats": {"fail": 1, "hold": 0, "labels": 0}}
repaired twin: exit 2 on a different diagnostic (tool state, noted): d2-typed-labels error: packet.materials: expected a non-empty record list

== case neg-12b-anchor-in-label-text ==
fixture:        /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-8/depth/neg/packet-12b.anchor-in-label-text.yml
fixture sha256: e8ddc9c71c47fd71e5777b8ada58ef6e6709206468cb61eea37a31b36ac15812
expected:       P-ANCHOR-TAG, exit 2
malformed run: exit 2 and 2 (want 2/2), --json exit 2, traceback: none
stdout (byte-identical across both runs):
  FINDING D2L-DATA: [fail] /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-8/depth/neg/packet-12b.anchor-in-label-text.yml — anchor, alias or tag is outside the accepted subset
json finding: {"exit_code": 2, "findings": [{"code": "P-ANCHOR-TAG", "detail": "anchor, alias or tag is outside the accepted subset", "id": "D2L-DATA", "severity": "fail", "where": "...packet-12b.anchor-in-label-text.yml"}], "ok": false, "packet": "...packet-12b.anchor-in-label-text.yml", "stats": {"fail": 1, "hold": 0, "labels": 0}}
repaired twin: exit 2 on a different diagnostic (tool state, noted): d2-typed-labels error: packet.materials: expected a non-empty record list

result: 2/2 negative controls refused with exit 2, stable P-* diagnostics, no tracebacks
```

(The `json finding` lines are elided at the absolute `where`/`packet` paths only;
the runner prints them in full.)

## 4. What each requirement got, and how it was checked

| Requirement | Receipt |
|---|---|
| exit 2 on both malformed packets | 2 runs per case, all four exits = 2, plus `--json` exit 2 (§3) |
| diagnostics stable | `cmp -s` on the two stdout and the two stderr captures per case: byte-identical (§3) |
| no tracebacks | runner greps stdout+stderr of every run for `Traceback`; none in §3, and none in the candidate-mutation probe sweep (`grep -l "Traceback" <captures>` → no matches, 2026-10-17) |
| rejection is caused by the defect, not the packet's shape | repaired twins (the same fixture with the single defect repaired) are no longer refused with the expected code: they get past the loader to the pipeline, where they stop on a *different* error because a minimal packet carries no `materials` block (§3, twin lines) — the loader refusal is the defect's, not the packet's |
| the refusal claims nothing else | the malformed runs print exactly one `D2L-DATA` finding and nothing to stderr (asserted; §3) |
| positive control | the live packet at the same digest exits 1 (never 2), no traceback (§3) |

## 5. Tool state during this shard (reported, not absorbed)

D02 rewrote `tools/d2-typed-labels.py` from the component-tree build to the
integrated `--packet` build while this shard ran. Eleven distinct digests were
observed during the shard (from the pre-rewrite `9fdb81e8…` to the green
`3548185cd9c1…`); the receipts that matter are pinned by digest. The
two defect classes in §1–§3 held at every digest they were run against: as
scratch candidates at `56c0db14` and `664cf81a`, and as the shipped fixtures at
`61b61eb4`, `6a80ffe4` and `8e4f9bef`. The tool's own pipeline did not always
hold:

- **`--selftest` was not green at several digests.** At `56c0db14` and
  `3adbdeb7` it ended in `RecursionError: maximum recursion depth exceeded`
  (the integrated `selftest()` reaches `selftest_rank_block`, which is an alias
  of `selftest` itself). At `11e23ca9` it failed with `missing
  examples/culture-d2/components/12-rank-rules.yml; A1 cannot be recorded` and a
  `FileNotFoundError` for a temp projection. Commands:
  `python3 tools/d2-typed-labels.py --selftest`.
- **A packet-level traceback existed at `56c0db14`.** D13's fixture
  (`packet-13.era-material-scope.yml`, sha256 `4b7ae4ec…`), whose `form_slot` is
  `"LEX-R13-01 (to-verify with the lexicon owner)"`, hit
  `AttributeError: 'NoneType' object has no attribute 'group'` in
  `_costume_label` (`slot_id = _SLOT_RE.search(slot).group(0) …`) — exit 1 with a
  traceback instead of a stable diagnostic. At `3adbdeb7` the same fixture
  evaluated cleanly (exit 1) and its intended defect is detected
  (`FINDING D2L-MATERIAL: [reject] GAR-R13-02 — CMAT-13-02 is not available in
  E0`), so the crash was fixed during the shard.
- **The live packet was refused (exit 2) at `61b61eb4` and `6a80ffe4`** with
  `D2L-DATA` rule-shape findings (`eras present without era_aliases_applied
  (A1)`), i.e. the tool could not evaluate its own default packet at those
  digests. At `8e4f9bef` and `11e23ca9` it exits 1 again.

The build turned green at `3548185cd9c1` (20:30:10Z: `--selftest` exit 0, live
packet exit 1) and was still green at the last digest observed, `e9209f28`
(20:31:22Z: live packet exit 1, both negative controls pass, runner exit 0).
The mid-flight states above are reported so the parent can read the receipts
that precede them with the right weight.

These are D02/O-axis matters; this shard reports them with digests and commands
rather than editing the tool.

- **Shared /tmp is inode-exhausted** (`df -i /tmp` → `1048576 1048576 0 100%`,
  2026-10-17, 64-worker wave), so the runner's temp-file helper falls back to
  `$HOME/.cache` when `${TMPDIR:-/tmp}` cannot host a file.

## 6. Limits

- The receipt is pinned to a digest because the tool was a moving target. Re-run
  `sh reports/round-8/depth/neg/run-negatives.sh` after D02 stops editing; it
  prints the digest it ran and fails loudly on any regression.
- The fixtures are minimal packets. Their repaired twins stop on
  `packet.materials: expected a non-empty record list` — a minimal packet is not
  a full evaluation packet; that is why the twins are notes, not assertions.
- `reports/round-8/run-validation.py` (the F/O harness) was not run here; the
  D-axis counting command in `claims.json` names it for the parent.
