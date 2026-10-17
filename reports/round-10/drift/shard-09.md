# Drift shard 09 — SKILL.md lines 161-180 (R10-F09)

- date: 2026-10-17 (runs 21:18–21:30 UTC)
- shard: R10-F09 (freshness drift re-runner, shard 09 of 13)
- source surface: `SKILL.md` lines 161-180 (sha256 of range: `ae445dd2d5b6b08704b7ad5da7635fb8d2c187ae3073ecb3b6caa91134d5bcb8`; whole file: `2bce468db89be47db7009cce1537538e574c3897da1a6097302dc56c0351df1b`)
- baseline revision: `9dc18ec1339bffd6f81e74f1a5742464ef578749` (declared in `reports/round-10/claims.json`)
- live HEAD: `e3a1ec9435787328ac9f828f96cb6390e4916b8f`; `git diff --stat 9dc18ec..HEAD -- SKILL.md` is empty, so all verdicts below are against baseline content.
- isolation: `export TMPDIR=$PWD/.scratch`; every gate/battery/replay control ran in `git archive` exports under `.scratch/f09/` (`.scratch/f09/export-r3` = commit `c610e0a`, `.scratch/f09/export-head`, `.scratch/f09/export-ctl2`). Live tree untouched by this shard: `git status --porcelain tools/` → empty. (`corpus/README.md` shows modified in the worktree — that is the C-shard index updater's in-flight edit, not this shard.)
- scratch artifacts: `.scratch/f09/*.out` (all under the lane; nothing written outside the repo).

## What lines 161-180 contain

Last two rows of the supplement finding/response table (161-162), the `## Gates and probes` prose (164-172: exit-code map, which gates read which input kind, the seven-selftest pass + five-fixture-regeneration claim, pointer to `29-local-boundaries.md`), and the replay-tool semantics paragraphs (174-179: pin validation, exit 0/1/2 meaning incl. `snapshot_tampered`, round-3 replayable, no `expected.json` retrofit, round-4 unpinned legacy).

## Inventory: runnable commands in range

`awk 'NR>=161 && NR<=180' SKILL.md | grep -cE 'python3|--selftest|run-validation'` → `1` (output sha256 `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865`, exit 0). The single cited command is the replay at `SKILL.md:162`; the prose at 166-171 additionally invokes the gate battery. No URLs in range (`awk 'NR>=161 && NR<=180' SKILL.md | grep -cE 'https?://'` → 0), so no web access attempt was required.

## Cited paths — both resolve

| locator | cited path | observed | verdict |
|---|---|---|---|
| SKILL.md:161 | `reports/supplement-opencode-1/25-handoff-boundary.md` | exists, 14819 bytes, sha256 `90da030743fc8bc4a3fc5c3067cf1e33b1f4d800765cae415598bc3b0a1ac6e9` | current |
| SKILL.md:172 | `reports/supplement-opencode-1/29-local-boundaries.md` | exists, 22908 bytes, sha256 `c4296f182300f2069042bba2920e53afb5fddefa600d870740ef8d30c3106920` | current as a path; its §F1 wording is pre-round-8 — see DR-09-02 |

## Command re-runs

| # | command | exit | output sha256 | verdict |
|---|---|---|---|---|
| 1 | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` (live tree) | **2** | `76c00a6b80d4539a70ebe976d86600f8317b8da962a3ea6cdfcf8bace7e41f80` | **stale-documented** — see DR-09-01 |
| 2 | same, `attempt-1/MANIFEST.tsv` | **2** | `409db5ab8b68ebc3da9a8360879db71c01e58b40ea4a8311e3818efe289c8452` | stale-documented (same class) |
| 3 | same manifest, `--repo-root .scratch/f09/export-r3` (commit `c610e0a` export; all six gate hashes equal the pins) | **0** | `10b82d575006e744f06789b06e931541460aa3f6c65dde42222270e4fbed210d` | current — `REPLAY OK: 7/7 rows reproduced` (red rows 2,4,5,6 reproduced at exit=1) |
| 4 | `python3 tools/replay-frozen.py tools/gates/frozen/round-4/MANIFEST.tsv` | **2** | `1dc089cc51958f5435b2fd720a8ce8d92ddd337107f21910794b911b1624882b` | current — `manifest_unreadable`; the dir holds only 5 `.out` files, so "unpinned legacy evidence" (SKILL.md:178-179) holds |
| 5 | `python3 tools/check-gate-battery.py` (committed default) | **2** | `6fd828d32bfbde7724cfc8baea845206d8aef0a5c3a7e1b6ab9a1685286abc6e` | current — duty 1 `pass 7 / fail 0 / unevaluable 0`, originals preserved (28 files hashed before/after, modified 0); duty 2 `baseline_exit 2` (5/7 covered; myth + naming pins live only under `reports/round-9/baselines/`). Same readings as `reports/round-9/baselines/registry.md:173` |
| 6 | `python3 tools/check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines` | **0** | `c164b1e2c386c9b24f4054076964713d25934478b6e6fbb7eab2be0792a52fee` | current — 7/7 gates covered, pass 7/fail 0/unevaluable 0; the documented remedy at `registry.md:174` still works |
| 7 | `python3 tools/replay-frozen.py --selftest` | **0** | `4d6aaea127ad99737b53ce50a7378efad5562b6fa01da88e9ca8610aa604ea16` | current — `selftest: 79/79 checks passed`, incl. `snapshot-tampered → exit 2`, `gate-digest-mismatch → exit 2`, `mismatch-bytes/-exit → exit 1`, `recorded command string never executed` |
| 8 | regen control (all 7 gates, fixtures present, mtime+inode+size hash before/after each `--selftest`) in `export-ctl2` | 0 | `ca39f5fce21c5a3448db7a4cadc37f5fc74291d2db8ca5610b5ce407d332b639` | **stale-documented** (control for SKILL.md:169-170) — all seven: `selftest_exit=0 fixtures_rewritten_mtime_inode=no` |
| 9 | tamper control (append a line to phonology fixture and to `provenance/defect-empty-couples.md`, run each `--selftest`) | 0 (script) / gate exits 1 | `04edbb00af62bdcbdc45e9348d168586fbccd3f0e62d66e9e3e79008866fabab` | **stale-documented** — both gates: `SELFTEST FAIL: … diverges from the embedded constant; refusing to overwrite (delete the file to regenerate it)`, file left tampered |
| 10 | delete control (remove `phonology-sanity-gate.yml`, run `--selftest`) | 0 | `e0a9ec0d6fc2a97c9e8f321dbfcbd8c45275b0184a530b9842b8ffc1181580cd` | **stale-documented** — regenerated byte-identical: `96dfa97e87c85a5c52145d6b9aa1b16572b2906b76ee6dee1591290a7ecb7421` = committed fixture hash |

## Static claim checks in range

| locator | claim | observed | verdict |
|---|---|---|---|
| SKILL.md:166 | 0 clean / 1 findings / 2 could-not-evaluate | gate usage/docstrings and the selftest controls exercise the map (handoff selftest: fixture exit 1, clean control exit 0, malformed exit 2); per-gate map documented at `reports/round-9/baselines/registry.md:162-175` | current |
| SKILL.md:167-168 | `provenance-audit` reads corpus entries; `handoff-packet-check` reads the handoff envelope; the other five read culture packets | `tools/gates/provenance-audit.py:2-4` ("Scans corpus entry documents (not culture packets)"); `tools/gates/handoff-packet-check.py` docstring §4 (handoff envelope); usage strings `<culture-packet.yml>` in phonology:1350, lexicon:1002, myth:845, costume:1147, naming:1908 | current |
| SKILL.md:168-169 | the seven legacy selftests pass | row 5: `pass 7 / fail 0 / unevaluable 0`, originals preserved | current |
| SKILL.md:174-177 | pins validated, snapshots executed, command string never executed; exit 0/1/2 semantics incl. `snapshot_tampered` | row 7 selftest 79/79; tool docstring `tools/replay-frozen.py:1-45`; argv built as `[python3, gate, input]` (no manifest string parsed) | current |
| SKILL.md:177-178 | round-3 TSV replayable; no `expected.json` retrofit | row 3 (pinned revision replays 7/7 exit 0); `grep -n expected.json tools/replay-frozen.py` → no expected.json layout handling (only `expected_output_tampered` as a pin-failure reason) | current |

## Findings

### DR-09-01 — `SKILL.md:162` "Frozen replay exits 0 with recorded findings" no longer holds in the live tree (stale-documented)

- Locator: `SKILL.md:162` — `| Frozen replay exits 0 with recorded findings | The red verdict reproduced; the culture did not become clean | \`python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv\` |`
- Observed (21:19 UTC): exit 2, `REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch, 0 reproduced of 7 row(s)`, every row `gate_digest_mismatch` ("gate: on-disk bytes are not the pinned revision"). Cause: the round-8 in-place gate repairs (commit `e1694ba`) changed all six gate files after the round-3 pins were recorded; the pins correctly refuse edited gates. Manifest digest is unchanged (`d5337590b343c65b42fd6e55457862fa325c138ad652e59c81b887daf9971399`).
- Remediation verified here, not just cited: the commit-`c610e0a` export carries all six gate bytes exactly equal to the pins (`fb05c644…`, `63ee4ec6…`, `26d246e9…`, `29a9361c…`, `8c5afb0a…`, `4aaea6e9…`), and the live tool with `--repo-root` against it exits **0** with `7/7 rows reproduced` (row 3 above). The claim's substance ("a replay exit 0 reproduces, it does not clear the culture") is intact; only the unqualified live-tree exit-0 statement is stale.
- Already documented: `reports/round-8/rerun.json` (all 7 rows `gate_digest_mismatch`; pristine extraction replays 7/7), `reports/round-8/depth/test-replay.md` §6 (re-pin remediation; "no shard should re-bless the pins by editing the round-3 manifest in place"), `reports/round-9/d3/replay.md:118` (same 7/7 `gate_digest_mismatch` reading at round 9).
- Verdict: **stale-documented**. Proposed fix for F15-F18: qualify the row — e.g. "at the pinned revision / with pinned gate bytes" and note the live-tree fail-closed reading with the `--repo-root` export recipe; do not edit the round-3 manifest in place.

### DR-09-02 — `SKILL.md:169-170` "five regenerate their fixture files in place" describes the pre-round-8 behavior (stale-documented)

- Locator: `SKILL.md:169-170` — "The seven legacy selftests pass, but five regenerate their fixture files in place (phonology, lexicon, myth, costume, provenance)."
- Observed: current gate revisions regenerate a fixture **only when it is absent**; a present file is verified byte-for-byte and a divergent file is reported, never overwritten. `_pin_fixture` at `tools/gates/phonology-sanity-gate.py:1266`, `lexicon-coverage-audit.py:1442`, `myth-consistency-gate.py:1058`, `costume-era-consistency-gate.py:1480`, `provenance-audit.py:405` (docstring: "Regenerate a committed fixture only when absent; never overwrite."). The five gates' divergence messages exist at the same files (phonology:1350 region, lexicon:1467, myth:1083, costume:1505).
- Controls (all in `git archive HEAD` exports): with fixtures present, **no** fixture's mtime/inode/size changed across all seven selftests (row 8); a tampered phonology/provenance fixture fails loudly and is left untouched (row 9); a deleted phonology fixture is regenerated atomically and byte-identically (row 10). So neither the per-run rewrite nor the tamper-erasure the sentence implies is true today.
- Already documented: `reports/round-8/operability/neg-controls/neg-13/neg-13-report.md:142-152` — the defect (review 29 §F1), the repair (verify/refuse/regenerate-only-if-absent), and a 17/17 control (`evidence-extra-f1-postfix.txt`, all five gates `absent-regenerated PASS`). `reports/supplement-opencode-1/29-local-boundaries.md` §F1 (line 37) still states the old behavior — it is the filed finding that motivated the fix (filed-report bytes must not be rewritten; corrections are new entries).
- Residual guidance stays sound: run the battery in an isolated export; byte equality still does not prove no writes (the delete case writes, and a rewrite with identical bytes would be invisible to hashes).
- Verdict: **stale-documented**. Proposed fix for F15-F18: replace the clause with the current contract ("a present fixture is verified, a divergent one is refused and left untouched, only a missing one is regenerated atomically") and cite `neg-13-report.md` alongside `29-local-boundaries.md`.

### Boundary note

`SKILL.md:161`'s evidence path resolves (`25-handoff-boundary.md`, hash above) and the `CROSS-HOLD` row was not re-adjudicated — scope/canon standing is lore-shokunin's and outside this lane (`AGENTS.md`). Lines 181+ (gate registry table) belong to other shards and were not swept here beyond the battery rows above.

## Ledger rows (for the F14 scribe)

```json
[
  {"id": "R10-F09-01", "command": "python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv", "source_locator": "SKILL.md:162", "round10_verdict": "stale-documented", "output_sha256": "76c00a6b80d4539a70ebe976d86600f8317b8da962a3ea6cdfcf8bace7e41f80", "exit": 2, "note": "live tree: 7/7 gate_digest_mismatch; round-8 gate repairs (e1694ba) drifted the pins; documented in round-8 rerun.json, test-replay.md §6, round-9 d3/replay.md:118; fix proposed for F15-F18"},
  {"id": "R10-F09-02", "command": "python3 tools/replay-frozen.py tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv", "source_locator": "SKILL.md:162 (same class)", "round10_verdict": "stale-documented", "output_sha256": "409db5ab8b68ebc3da9a8360879db71c01e58b40ea4a8311e3818efe289c8452", "exit": 2, "note": "7/7 gate_digest_mismatch, same cause"},
  {"id": "R10-F09-03", "command": "python3 tools/replay-frozen.py .scratch/f09/export-r3/tools/gates/frozen/round-3/MANIFEST.tsv --repo-root .scratch/f09/export-r3", "source_locator": "SKILL.md:162 (remediation control)", "round10_verdict": "current", "output_sha256": "10b82d575006e744f06789b06e931541460aa3f6c65dde42222270e4fbed210d", "exit": 0, "note": "export at c610e0a has all six gate hashes equal to pins; REPLAY OK 7/7 reproduced, red rows stay red"},
  {"id": "R10-F09-04", "command": "python3 tools/replay-frozen.py tools/gates/frozen/round-4/MANIFEST.tsv", "source_locator": "SKILL.md:178-179", "round10_verdict": "current", "output_sha256": "1dc089cc51958f5435b2fd720a8ce8d92ddd337107f21910794b911b1624882b", "exit": 2, "note": "manifest_unreadable — round-4 holds only .out files, so 'unpinned legacy evidence' holds"},
  {"id": "R10-F09-05", "command": "python3 tools/check-gate-battery.py", "source_locator": "SKILL.md:168-171", "round10_verdict": "current", "output_sha256": "6fd828d32bfbde7724cfc8baea845206d8aef0a5c3a7e1b6ab9a1685286abc6e", "exit": 2, "note": "duty1 pass 7/fail 0/unevaluable 0, originals preserved; duty2 baseline_exit 2 (5/7 covered) — documented default, registry.md:173"},
  {"id": "R10-F09-06", "command": "python3 tools/check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines", "source_locator": "SKILL.md:168-171 (documented remedy)", "round10_verdict": "current", "output_sha256": "c164b1e2c386c9b24f4054076964713d25934478b6e6fbb7eab2be0792a52fee", "exit": 0, "note": "7/7 gates covered, pass 7/fail 0/unevaluable 0"},
  {"id": "R10-F09-07", "command": "for g in <7 gates>; do stat-hash fixtures; python3 tools/gates/$g.py --selftest; stat-hash again; done (export-ctl2)", "source_locator": "SKILL.md:169-170", "round10_verdict": "stale-documented", "output_sha256": "ca39f5fce21c5a3448db7a4cadc37f5fc74291d2db8ca5610b5ce407d332b639", "exit": 0, "note": "all seven: exit 0, fixtures_rewritten_mtime_inode=no — present fixtures are verified, not rewritten; claim describes pre-round-8 behavior"},
  {"id": "R10-F09-08", "command": "tamper phonology fixture + provenance/defect-empty-couples.md, run both --selftest (export-ctl2)", "source_locator": "SKILL.md:169-170", "round10_verdict": "stale-documented", "output_sha256": "04edbb00af62bdcbdc45e9348d168586fbccd3f0e62d66e9e3e79008866fabab", "exit": 1, "note": "both refuse: 'diverges from the embedded constant; refusing to overwrite'; files left tampered; evidence for DR-09-02"},
  {"id": "R10-F09-09", "command": "rm tools/gates/fixtures/phonology-sanity-gate.yml && python3 tools/gates/phonology-sanity-gate.py --selftest (export-ctl2)", "source_locator": "SKILL.md:169-170", "round10_verdict": "stale-documented", "output_sha256": "e0a9ec0d6fc2a97c9e8f321dbfcbd8c45275b0184a530b9842b8ffc1181580cd", "exit": 0, "note": "absent fixture regenerated byte-identical (96dfa97e… = committed hash); regeneration happens only when absent"},
  {"id": "R10-F09-10", "command": "python3 tools/replay-frozen.py --selftest", "source_locator": "SKILL.md:174-177", "round10_verdict": "current", "output_sha256": "4d6aaea127ad99737b53ce50a7378efad5562b6fa01da88e9ca8610aa604ea16", "exit": 0, "note": "79/79 checks; snapshot_tampered→2, gate_digest_mismatch→2, mismatch→1, recorded command string never executed"},
  {"id": "R10-F09-11", "command": "awk 'NR>=161 && NR<=180' SKILL.md | grep -cE 'python3|--selftest|run-validation'", "source_locator": "SKILL.md:161-180", "round10_verdict": "current", "output_sha256": "4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865", "exit": 0, "note": "1 runnable command cited in range (the replay at :162); no URLs"}
]
```

## Re-run recipe (for the F19 auditor)

1. `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && export TMPDIR=$PWD/.scratch`
2. `sha256sum SKILL.md` → `2bce468db89be47db7009cce1537538e574c3897da1a6097302dc56c0351df1b`; `awk 'NR>=161 && NR<=180' SKILL.md | sha256sum` → `ae445dd2d5b6b08704b7ad5da7635fb8d2c187ae3073ecb3b6caa91134d5bcb8`.
3. `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` → exit 2, 7/7 `gate_digest_mismatch` (live-tree fail-closed).
4. `mkdir -p .scratch/f09/export-r3 && git archive c610e0a | tar -x -C .scratch/f09/export-r3 && python3 tools/replay-frozen.py .scratch/f09/export-r3/tools/gates/frozen/round-3/MANIFEST.tsv --repo-root .scratch/f09/export-r3` → exit 0, `REPLAY OK: 7/7`.
5. `python3 tools/check-gate-battery.py` → exit 2 (duty 1 7/7 pass); add the three `--baselines-root` flags from row 6 → exit 0.
6. `python3 tools/replay-frozen.py --selftest` → 79/79, exit 0.
7. Fixture controls: fresh `git archive HEAD` export, then repeat rows 8-10 (mtime/inode hash before/after; tamper refusal; absent regeneration). Do not run the five writer gates' selftests in the live tree — only in exports.

Limits: this shard covers lines 161-180 only; the registry table (181+) and SCORECARD rows are other shards' surfaces. The two stale items are documented, not fixed here (F15-F18 own the fixes); filed report bytes were not rewritten. Replay exit 0 means reproduction, never clearance.
