# R8-D18 — scribe: frozen-manifest records for `d2-typed-labels` + SCORECARD capability-row draft

- round: 8 (loop 1 of 3, build round 1 of 4) · shard: D18 (scribe) · 2026-10-17
- baseline revision: `e7ca0faeb6680fa9891b907be628d9db578c28f4` (declared in `reports/round-8/claims.json`)
- measurement tree HEAD: `cf338a713060f274269cdacb18cdc0085bb06aeb`
- writes: this file only. Frozen records and the SCORECARD row below are **drafts**;
  the orchestrator lands/admits them. No tool, example, SCORECARD or LOG edit here.
- canon: NON-CANON engineering evidence. A freeze pins bytes and verdicts, never
  design quality, scholarship or lore standing.

Status: **complete for this shard's scope** (last stamp `2026-10-17T20:26:38Z`). The
tool `tools/d2-typed-labels.py` (D02) landed at `20:19Z` and settled green at
`20:23:04Z` (worktree revision sha256 `623b5b1f2f9f50b3e306975b4107b5f70122e86e7d7b41aeca21bcb5a7979b03`,
stable through `20:25Z`); §4's pin values are filled from that revision and §5's
capability row carries the demonstrated run. **D02 kept editing after the pin:**
`f0110e39…` at `20:26:04Z`, then `5d87d346…` at `20:26:13Z` where the tool was a
broken intermediate (`--selftest` `RecursionError`, `--check` `NameError:
rank_adapter_view` traceback) — so the on-disk tool at this shard's handoff is
**not** the green revision, and the orchestrator must re-run the pin commands at
integration and re-pin (§6.1). The green revision's artifact
(`820b7535…`) stayed byte-unchanged throughout the churn. The pin is a
**worktree** revision — the integration commit hash is `to-verify` until then.

## 1. Measurement environment and concurrency

```sh
git rev-parse HEAD && git status --porcelain && date -u +%FT%TZ
```

Observed `2026-10-17T20:17:12Z`:

```
cf338a713060f274269cdacb18cdc0085bb06aeb
 M tools/gates/costume-era-consistency-gate.py
 M tools/gates/lexicon-coverage-audit.py
 M tools/gates/myth-consistency-gate.py
 M tools/gates/naming-collision-gate.py
 M tools/gates/phonology-sanity-gate.py
?? corpus/lessons/round-8.md
?? reports/round-8/depth/
?? reports/round-8/freshness/
?? reports/round-8/operability/
?? tools/harness/
```

- The five modified gates are concurrent O-shard repairs of the legacy
  parser/selftest defects (claim O). They are not this shard's files and are not
  modified here. Their digests move while this shard measures; every digest below
  names its observation stamp.
- **Environment constraint:** `/tmp` inode exhaustion during this window
  (`df -i /tmp` → `1048576 1048576 100%`). Any run whose temp directory lands in
  `/tmp` can fail with `ENOSPC`; all isolated runs below redirect `TMPDIR` to
  `$HOME/.cache/scribe-r8-probe/mirror-tmp` (a path outside the replay root,
  which matters — see §3.2).

## 2. Record format decision — what a replayable record for this capability can be

`tools/replay-frozen.py` whitelists only `*.py` files directly under `tools/gates`
(`gate_path()`, `tools/replay-frozen.py:131-140`). A manifest row naming
`tools/d2-typed-labels.py` is therefore refused **before** any digest check or
execution. Probe receipt (`2026-10-17T20:16Z`; probe manifest written outside the
repo at `$HOME/.cache/scribe-r8-probe/MANIFEST.probe.tsv`, one row naming
`tools/d2-typed-labels.py` with the D2 packet as input):

```sh
python3 tools/replay-frozen.py "$HOME/.cache/scribe-r8-probe/MANIFEST.probe.tsv"
```

```
ROW 2 could-not-evaluate reason=gate_not_whitelisted gate=tools/d2-typed-labels.py ... launched=no
  detail: gate: only *.py files directly under tools/gates are replayable: 'tools/d2-typed-labels.py'
REPLAY COULD-NOT-EVALUATE: 1 could-not-evaluate, 0 mismatch, 0 reproduced of 1 row(s)
exit=2
```

Consequences for the frozen-manifest record of the new capability:

1. The capability **cannot** be recorded in the round-3-style `MANIFEST.tsv` schema
   unless the tool lives under `tools/gates/` (it does not — claim D names
   `tools/d2-typed-labels.py`) or `replay-frozen.py` gains a whitelist extension
   (outside this shard's authority; **reported, not absorbed**).
2. The applicable lane shape is the frozen-run standard's `expected.json`
   (`corpus/knowledge/verification/gate-frozen-run-standard.md` §4, schema
   `kotodama-frozen-run-v1`), whose check is digest verification plus
   deterministic re-execution of the pinned tool over the pinned input — the same
   shape `examples/culture-d3/expected.json` already uses for its guard.
3. The claim's literal replay leg — "replays frozen (`python3 tools/replay-frozen.py`)
   without digest drift" — is the round-3 gate manifest over the D2 packet, and is
   measured separately in §3.

## 3. Frozen record R8-D2T-FR1 — D2 packet frozen-replay leg (measured)

### 3.1 Durable receipt: the committed revision replays 7/7

At the committed revision, with the gates taken from HEAD (`git show HEAD:...`,
phonology gate digest `fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655`
= the manifest pin) in an isolated root, and the committed round-3 baselines:

```sh
S="$HOME/.cache/scribe-r8-probe/head-root"          # HEAD gate bytes + committed frozen/round-3
TMPDIR="$HOME/.cache/scribe-r8-probe/mirror-tmp" python3 tools/replay-frozen.py \
  tools/gates/frozen/round-3/MANIFEST.tsv --repo-root "$S"
TMPDIR=... python3 tools/replay-frozen.py tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv \
  --repo-root "$S" --json
```

Observed `2026-10-17T20:16Z`: **both manifests `REPLAY OK: 7/7 rows reproduced the
recorded verdicts`, exit 0**, every row `bytes=match` (round-3: rows 2–8; JSON
summary `{'rows': 7, 'reproduced': 7, 'mismatch': 0, 'could_not_evaluate': 0, 'exit': 0}`).
This is the digest-drift statement for the packet leg: **no snapshot drift at the
pinned revision** — reproduced red verdicts stay red, which is the standard's
contract, not a design PASS.

### 3.2 Live-worktree observation during the O-shard repairs

Same manifest, live worktree, `2026-10-17T20:17:21Z`:

```
{'rows': 7, 'reproduced': 2, 'mismatch': 0, 'could_not_evaluate': 5, 'exit': 2}
row 2 gate_digest_mismatch tools/gates/phonology-sanity-gate.py
row 3 gate_digest_mismatch tools/gates/lexicon-coverage-audit.py
row 4 gate_digest_mismatch tools/gates/myth-consistency-gate.py
row 5 gate_digest_mismatch tools/gates/costume-era-consistency-gate.py
row 6 gate_digest_mismatch tools/gates/naming-collision-gate.py
```

Earlier in the same window the same command read 6/7 + one `gate_digest_mismatch`
(only phonology dirty at `20:14Z`); the count tracks the in-flight repairs, so a
re-run may legitimately differ until integration commits.

### 3.3 Digest table (stamped) and the consequence to decide

| item | value | stamp/source |
|---|---|---|
| round-3 `MANIFEST.tsv` | `d5337590b343c65b42fd6e55457862fa325c138ad652e59c81b887daf9971399` | `sha256sum` 2026-10-17 |
| round-3 attempt-1 `MANIFEST.tsv` | `613e59452bf76422e85ce4586cc00b85588e03b974a67e3ad1897f589f7b06a1` | `sha256sum` 2026-10-17 |
| frozen packet snapshot (pin) | `54be6319e4907d20c8239555e3f79fcb9bb6b36d102a30a6beabf34b146459f4` | manifest `input_sha256`; re-verified |
| live packet `examples/culture-d2/packet.d2.yml` | `8da90b0788f86fd19babc67958715c8c16cb90a98e13572380b1c1892622b81e` | `sha256sum` 20:17Z; equals HEAD |
| phonology gate: pin / HEAD / worktree | `fb05c644…` / `fb05c644…` / `17773f3f…` | `sha256sum`, `git show HEAD:` |
| other gate pins vs worktree (20:17Z) | lexicon `63ee4ec6…`→`bf43122d…`; myth `26d246e9…`→`5c9fc2ee…`; costume `29a9361c…`→`20735a9c…`; naming `8c5afb0a…`→`ab98fe1a…`; provenance `4aaea6e9…` unchanged | `sha256sum` |

- In **every** observation, no row read `snapshot_tampered` and no row read
  `replay_mismatch`: the committed input copies still match their pins. What moved
  is the gate revisions under the pins — exactly the case the frozen-run standard
  maps to `gate_revised` → could-not-evaluate → "re-freeze under the new revision;
  never compare across an unnamed one" (§6.2).
- **Orchestrator decision, flagged not absorbed:** once the O repairs commit, rows
  2–6 of the round-3 baselines will read `gate_digest_mismatch` persistently. Either
  (a) freeze a new baseline for the repaired gate revisions (new baseline id; the
  standard forbids rewriting existing ones) — the scribe can supply the digest rows
  on request — or (b) report the round-3 rows as historical under named revisions.
  Either way the claim's "without digest drift" clause should be read as: the frozen
  snapshots show no drift; gate-revision rows are could-not-evaluate, not drift.

## 4. Frozen record R8-D2T-FR2 — capability freeze record (draft; pinned to the last green tool revision)

Draft in the frozen-run standard's `expected.json` field vocabulary, adapted for a
non-gate tool (`tool`/`tool_sha256` in place of `gate`/`gate_sha256`). All verdict
values below are measured (stamps in §4.1); the only remaining `to-verify` fields
are named inside the record and in §6.1.

```json
{
  "schema": "kotodama-frozen-run-v1 (draft, adapted: tool instead of gate)",
  "tool": "tools/d2-typed-labels.py",
  "tool_sha256": "623b5b1f2f9f50b3e306975b4107b5f70122e86e7d7b41aeca21bcb5a7979b03",
  "revision": "worktree revision of 2026-10-17T20:23:04Z–20:24:33Z; HEAD was cf338a713060f274269cdacb18cdc0085bb06aeb with the tool untracked; the integration commit hash is to-verify until the orchestrator commits",
  "frozen_at": "2026-10-17T20:24:33Z",
  "frozen_by": "round 8, shard D18 (scribe); tool owner D02",
  "inputs": {
    "examples/culture-d2/packet.d2.yml": "8da90b0788f86fd19babc67958715c8c16cb90a98e13572380b1c1892622b81e",
    "tools/assemble-d2.py": "8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d",
    "examples/culture-d2/components/12-rank-rules.yml": "28696a5a70404984fbf1a453f66c9e7618e318ebf93f25bce461fdb7dfcd35a3",
    "examples/culture-d2/components/11-costumes.yml": "b6e2c5c29cc5d68900d6cde5a8487e64f27d85ecb3d2bd7f3f5beb1113483f22",
    "examples/culture-d2/components/05-lexicon.yml": "9bdcb8d895be0592047260361c4c12493569e7d38318b3508a5bde314d87abdf",
    "examples/culture-d2/components/02-phonology.yml": "23500df0f97a43c8800e3a678df6928f476254e56ff844fabe0c71829ecbb538"
  },
  "artifact": {
    "path": "examples/culture-d2/typed-labels.d2.yml",
    "sha256": "820b75352fb0f20d3a76b523b202e6b8d4a8668f84a85f3fb78ebabb6422f778",
    "bytes": 68643,
    "observed_shape": "5 declared kinds, 94 label records, 3 executable + 18 held rank rules, 2004 lines"
  },
  "expected": {
    "selftest": {"exit": 0, "checks": "32/32", "stdout_sha256": "4818583d55e9e4691e2978c5f43ec2366f6edd463a89868f60ddf66bd5a24642"},
    "check": {"exit": 0, "stdout": "examples/culture-d2/typed-labels.d2.yml: byte-identical deterministic build"},
    "report": {"exit": 0, "findings": 41, "finding_ids": {"TL-01": 10, "RR-01": 18, "RR-02": 3, "RC-01": 4, "RC-03": 1, "RC-04": 2, "PR-01": 3}, "stdout_sha256": "421c9173b1ed5dd36cd3700f14fc34bf03e14cd63c30953421cef8d27c7c801d"},
    "costume_gate_over_artifact": {"exit": 0, "findings": 0, "gate_worktree_sha256": "to-verify (measured sha16 6be04578fc219949 at 20:24Z; the gate was under concurrent O-shard repair)"}
  },
  "replay": {
    "command": "python3 tools/d2-typed-labels.py --check  (read-only drift check; the default run builds examples/culture-d2/typed-labels.d2.yml from the fixed component tree — no positional input argument exists)",
    "deterministic_reexecution": "isolated mirror rebuild 2026-10-17T20:24Z: exit 0, wrote 68643 bytes, sha256 820b7535… == the lane artifact (byte-identical); --selftest stdout sha256 identical across two consecutive runs",
    "replay_frozen": "not applicable to this tool path (gate_not_whitelisted, §2); the packet leg replays via tools/gates/frozen/round-3/MANIFEST.tsv (§3)"
  },
  "limits": "Pins bytes and a verdict only: not design quality, not a real-world etymology check, not canon, not lore acceptance. The 41 report findings are holds/reported conditions at this revision, not a design PASS; exit 0 on --report is the tool's measured semantics (only --check distinguishes drift with exit 1 and errors with exit 2).",
  "post_pin_churn": "D02 edited on after the pin: 2026-10-17T20:26:04Z sha16 f0110e391d476a5e; 20:26:13Z sha256 5d87d34683d63fe56d0f3f214693d52e7affabd4a1f750761424cc509024686c with --selftest exit 1 (RecursionError), --check exit 1 (NameError traceback), --report exit 2. The artifact sha256 820b7535… stayed unchanged through the churn. RE-PIN AT INTEGRATION: re-run the four commands in this record on the integrated tool revision before citing any value here."
}
```

Component digests cited above were measured by the D15 docs shard at
`2026-10-17T20:14:37Z` (`reports/round-8/depth/docs.md` §2.3) and re-used here
read-only; the packet and assembler digests were re-measured by this shard.
`--selftest`/`--report` stdout hashes are this shard's measurements
(`2026-10-17T20:24:00Z`, scratch copies under `$HOME/.cache/scribe-r8-probe/`).

### 4.1 Landing log (stamped observations; tool owner D02 iterating)

- `2026-10-17T20:19Z` — `tools/d2-typed-labels.py` landed (60029 bytes); real
  CLI is `[--check | --report | --selftest]` with no positional argument (this
  supersedes the docstring draft in `docs.md` §3, which D15 itself marked
  draft-pending-interface). Default run builds
  `examples/culture-d2/typed-labels.d2.yml` (68223 bytes / 1973 lines, sha256
  `08de5a88ff93b42c59909ee04d028eda9526800b6955ca58db89dd33225479dd`,
  mtime 17:19).
- First full run against the real tree: **exit 2** —
  `d2-typed-labels error: materials[CMAT-06].maps_to is unreadable: '10-materials
  MAT-05 lowland-plant-cloth (same slot) — note the convergent exclusions: …'`;
  `--report` and `--check` and `--selftest` all exited 2/1 at that revision.
- `2026-10-17T20:20:02Z–20:22:03Z` — watcher ticks (30 s cadence) show the tool
  file changing on every tick (sha16 `080a3b2f…`, `13e82857…`, `429191fd…`,
  `3f733e0a…`, `da86132e…`) with `--check` exit 1 and `--selftest` exit 1
  throughout: D02 is actively repairing the tool, and the on-disk artifact above
  is **stale relative to the current tool revision**. No pin is taken from a
  moving revision; the final pinned values were filled into the §4 record when
  the tool settled (next bullets).
- The on-disk artifact's interim shape (from the 17:19 build, stamped above):
  5 declared kinds (`native-form`, `translated-label`, `borrowed-strata`,
  `fictional-coordinate`, `descriptive-gloss`), 94 label records, era/material
  reconciliation sections, `rank_rule_adapter` with 3 `executable` + 18 `held`
  of 21 prose rules, and findings with ids `TL-nn` — whereas the design spec
  (`reports/round-8/depth/design-spec.md` §6) normatively names `D2L-*` ids.
  The settled revision (next bullet) keeps the same shape and the `TL-01`/`RC-*`/
  `RR-*`/`PR-01` id vocabulary; recorded as an observed spec-vs-build divergence
  at this stamp, not a finding (the spec itself says it is reconciled against the
  build by D02; id alignment is D02's call).
- `2026-10-17T20:23:04Z` — **settled green** at tool sha256
  `623b5b1f2f9f50b3e306975b4107b5f70122e86e7d7b41aeca21bcb5a7979b03`:
  `--selftest` exit 0 with `32/32 checks passed` (identical stdout across two
  consecutive runs), `--check` exit 0 (`byte-identical deterministic build`),
  `--report` exit 0 with 41 findings (holds: TL-01 ×10, RR-01 ×18, RR-02 ×3,
  RC-01 ×4, RC-03 ×1, RC-04 ×2, PR-01 ×3), artifact rebuilt to
  `820b75352fb0f20d3a76b523b202e6b8d4a8668f84a85f3fb78ebabb6422f778`
  (68643 bytes, 2004 lines). Stability re-checked at `20:24:33Z`: tool and
  artifact digests unchanged (~90 s quiet). The isolated-mirror rebuild (§4
  `deterministic_reexecution`) reproduced the artifact byte-identically.
  This is the revision §4's record pins. The sha16 values in the previous
  bullet (`097a23a3…` reached `--check` 0 first) are superseded churn, retained
  for the landing history only.
- `2026-10-17T20:26:04Z–20:26:38Z` — **churn resumed after the pin**: sha16
  `f0110e391d476a5e` at `20:26:04Z`, then sha256
  `5d87d34683d63fe56d0f3f214693d52e7affabd4a1f750761424cc509024686c` at
  `20:26:13Z` where the tool was a broken intermediate — `--selftest` exit 1
  with `RecursionError: maximum recursion depth exceeded`, `--check` exit 1 with
  a `NameError: name 'rank_adapter_view' is not defined` traceback, `--report`
  exit 2. Measured `2026-10-17T20:26:13Z`; the artifact sha256 `820b7535…` stayed
  unchanged. Consequence, flagged to the orchestrator: the pin above is the
  last measured **green** revision, not the current worktree state; re-run the
  record's commands at integration and re-pin before citing any value.
- `2026-10-17T20:27:53Z` (final check) — tool sha16 `61b61eb430a4b60e`,
  `--selftest` exit 1: the churn was still red at this shard's handoff. The
  artifact sha256 remained `820b75352fb0f20d…` (unchanged since `20:23Z`).

Placement options for the orchestrator (scribe does not write these files):
(a) `examples/culture-d2/expected.json`-style manifest verified by a tool
`--frozen` mode — **the shipped CLI has no `--frozen` mode** (measured
`2026-10-17T20:24Z`: `usage: d2-typed-labels.py [-h] [--check | --report | --selftest]`),
so this option would require D02 to add a flag first — the D3 precedent is
(`python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json`);
(b) the frozen-run standard's `expected.json` under a new capability directory with
the digest+re-execution check run by the round-8 acceptance harness (the §4 record
is already in this shape and needs only to be landed as a file);
(c) `tools/gates/frozen/round-8/` is **not** applicable for this tool (§2).

## 5. SCORECARD capability-row draft (draft only — orchestrator admits)

Intended landing surface: `SCORECARD.md` §Capabilities table (columns
`name | demonstrated behavior | command / evidence | first working`). Row text as
it would be pasted, with the honest admission state:

```markdown
| typed label handling (D2) | Types D2 translated-label / native-form / borrowed-strata records (plus two declared kinds) before any inventory or etymology check; scoped era/material reconciliation with explicit refusals of the two forbidden merges; executable rank-rule adapter (3 executable / 18 held of 21 prose rules); malformed-input and refusal controls in the isolated selftest | `python3 tools/d2-typed-labels.py --selftest` (32/32, exit 0); `--check` (exit 0, byte-identical build); `--report` (exit 0, 41 holds); artifact `examples/culture-d2/typed-labels.d2.yml` sha256 `820b7535…`; frozen record `reports/round-8/depth/scribe.md` §4; acceptance `python3 reports/round-8/run-validation.py` | round 8 (draft — orchestrator admits) |
```

- Before-state (claim D, `reports/round-8/claims.json`): "No typed
  translated-label/native-form handling: D2 packet assembly has no typed-label
  schema, no scoped era/material reconciliation, and no executable rank-rule
  adapter (SCORECARD Planned debt)." The recorded motivating defect: the naming
  gate reads the English `garment` text as a pronounceable name
  (`examples/culture-d2/ASSEMBLY.md:94`;
  `reports/supplement-opencode-1/22-label-representation.md` §1, §3; 10 ×
  `PHON-INVENTORY FAIL`), and packet `unresolved` carries "12 prose rank rules are
  not translated into executable rank_rules; R-checks are unevaluated"
  (`examples/culture-d2/packet.d2.yml:3341`).
- The row enters SCORECARD **only on demonstrated run** (claim D's own rule), and
  the demonstrated run is measured at the settled revision (§4.1, `20:23:04Z`):
  selftest `32/32` exit 0 with a stable stdout digest; `--check` exit 0
  byte-identical; `--report` exit 0 with 41 holds (the honest reading — holds are
  not a design PASS); isolated-mirror rebuild byte-identical. The round-8
  acceptance harness (`reports/round-8/run-validation.py`, O15) remains the
  counting command, and admission is the orchestrator's.
- This draft claims no new capability, no canon, no promotion.

## 6. Limits, `to-verify`, polling record

1. **Landing history.** `tools/d2-typed-labels.py` (D02) was absent at first
   write (`20:17Z`), landed at `20:19Z`, churned through several revisions
   (interim landing log §4.1), settled green at `20:23:04Z`, and churned again
   from `20:26:04Z` (broken intermediate at `5d87d346…`, §4.1); polling ran per
   round rules (60 s cadence from `20:12Z`, well inside the 20-minute cap). The
   record pins only the last measured green revision; every earlier sha16 is
   retained as landing history and marked superseded. What remains `to-verify`:
   **re-pin at integration** (the tool may be at a newer revision — re-run the
   record's commands before citing any value), the integration commit hash (the
   pin is a worktree revision), the full costume-gate digest for the
   gate-over-artifact row (sha16 `6be04578fc219949` at `20:24Z`, gate under
   concurrent repair), and the `D2L-*`-vs-`TL-*` finding-id alignment (observed
   divergence, D02's call — §4.1).
2. **No capability, no acceptance, no canon claimed here.** The D verdict belongs
   to `reports/round-8/run-validation.py` (O15) and the orchestrator's admission.
3. **Concurrency caveat.** Sibling shards edited the tree throughout the
   measurement window (five gates dirty, untracked round-8 paths). Every digest and
   reading above names its stamp; re-runs after integration may legitimately differ
   where sibling repairs land.
4. **Out of province, reported not absorbed:** the replay-frozen whitelist
   limitation (§2), the post-repair round-3 row consequence (§3.3), the placement
   choice (§4) and SCORECARD admission (§5) are orchestrator/integration decisions.
5. **Environment:** `/tmp` inode exhaustion during the window forced `TMPDIR`
   redirection for all isolated runs; the mirror must sit **outside** the replay
   root or `replay-frozen` refuses it (`mirror_unsafe`, observed at 20:16Z before
   the redirect — the tool's own fail-closed control, not a defect).

FILES: reports/round-8/depth/scribe.md | SUMMARY: D18 scribe — frozen-manifest records for `d2-typed-labels` (replay leg: committed revision replays round-3 manifests 7/7 exit 0 in an isolated root, no snapshot drift; live worktree reads 5 × gate_digest_mismatch from concurrent O-shard gate repairs; tool-path rows refused by replay-frozen as `gate_not_whitelisted`) and a draft SCORECARD capability row, pinned to the last green tool revision `623b5b1f…` (selftest 32/32, check exit 0, report 41 holds, artifact `820b7535…` rebuilt byte-identically) with re-pin-at-integration required because D02 resumed editing after the pin.
