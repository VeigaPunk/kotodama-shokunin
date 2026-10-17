# R10-F23 — stale items in filed reports: pins and digests superseded after filing

- seat: freshness stale-fixer (R10-F16..F19). This file is the seat's write; no
  filed report byte was rewritten — corrections are carried here, as new
  content, per the assignment.
- date: 2026-10-17 · lane: `kotodama-shokunin` · baseline `9dc18ec1…`
- live HEAD at work: `e3a1ec9` (+ worktree edits)

## Items taken from the ledger / shards

| ledger row (0-based) | locator | shard | verdict in ledger |
|---|---|---|---|
| 21 | `SKILL.md:36` via design-spec §9 | shard-02 | `stale-documented` (pin `226e1104…` vs live `621b7a33…`) |
| — (shard-14 §3.1) | `reports/round-9/baselines/registry.md:97` battery script digest | shard-14 | `stale-documented` |
| — (shard-14 §3.2) | registry §3 round-9 runner quote + failures | shard-14 | `stale-documented`, now superseded (green) |
| — (shard-14 §4) | registry §4 provenance pin file digest | shard-14 | `stale-documented` |

## Evidence (all re-measured by this seat)

- `corpus/knowledge/synthesis/era-language-staging.md` sha256
  `621b7a33c06ff15f5d179059e8ce856b7d22b51f5601787831956f4bf4a91da8`; the
  design spec's `226e1104…` is explicitly labelled pre-integration, and
  `git show e1694ba -- corpus/knowledge/synthesis/era-language-staging.md`
  inserted the three frontmatter lines that moved it (shard-02 §5).
- `tools/check-gate-battery.py` sha256
  `0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1` — the
  registry §3 quotes `9ad0ef95…`, its own referenced evidence
  (`reports/round-9/baselines/battery-extension.md:15`) already records
  `0a126b70…` as the successor (differs only in the
  `BASELINE-GATE-UNCOVERED` detail text).
- `reports/round-9/run-validation.py` sha256
  `8e4881309afaacc96f8f6e68f0c31041a9b2accc1c26bb1b20403f563364f5dd`; re-run
  exits 0 with F/O/D PASS, so registry §3's quoted `58e8fa4f…` / 13 failures
  are superseded (registry §5 item 8's hazard note is confirmed and now
  resolved for round 9).
- `tools/gates/frozen/provenance-audit/r9-pre/expected.json` sha256
  `425c74c084bb53bdf8aff8d4f143a6cbe062421e1362f234e5fe702463f95e87`; the
  registry §4 table records `ba4b2994…` — an earlier revision of the same pin
  file (mtime 17:54:17, after the registry's 17:53Z sweep). The live pin is
  valid: shard-14 recomputed all 20 `inputs` digests (20/20) and the battery
  reads it `pinned`.
- `reports/round-9/baselines/registry.md` sha256
  `cf95ba233d7924782c7f29e3f7510f58a54d8a94e17fa66fc762a458e88c8047`.

Registry §5 items re-verified by this seat where cheap: item 4 (handoff
`.expected` has no trailing newline — `wc -l` 8, 9 IDs, tail byte `G`), item 5
(`df -i /tmp` → 100% inodes, so in-lane `.scratch/` remains mandatory), item 7
(two byte-identical handoff pins, both read `pinned`, not flagged).

## Disposition: `stale-documented` (no in-place edit possible)

Reasons, per item:

- The design spec (`reports/round-8/depth/design-spec.md`) and the round-9
  registry (`reports/round-9/baselines/registry.md`) are **filed reports**;
  their bytes are frozen and are not rewritten by a later round's fixer. The
  divergences are drift-detection working as designed: the spec pinned
  pre-integration bytes, the registry swept mid-wave.
- The fixes therefore live here: quote the live digests above, or the
  registry's peer fragments (`audit-18.md:87`, `audit-20.md:121`,
  `reports/round-9/validation.json` `input_sha256`), not the superseded
  registry cells.
- No action is required on any pin: every pin file verified `pinned`; the only
  drift is in the **quoted digests** inside filed prose.

## Control (re-runnable)

- `sha256sum tools/check-gate-battery.py reports/round-9/run-validation.py tools/gates/frozen/provenance-audit/r9-pre/expected.json corpus/knowledge/synthesis/era-language-staging.md`
  → the four digests above.
- `python3 reports/round-9/run-validation.py` (in a mirror) → exit 0,
  F/O/D PASS.
- `python3 tools/check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines`
  → exit 0, 8/8 `pinned`.

## Limits

- This fragment corrects quoted digests only; it re-adjudicates no gate design
  and re-executes no baseline verdict (`verdict_replay: not-run`).
- The registry's §5 items 1/6/7 (layout, discovery, duplicate id) remain the
  orchestrator's decisions — see `fix-21.md`.

## Ledger delta (for the F14 scribe / integrator)

```json
[{"id": "R10-F23-01", "command": "git show e1694ba -- corpus/knowledge/synthesis/era-language-staging.md", "source_locator": "SKILL.md:36 (via design-spec §9)", "round10_verdict": "stale-documented", "output_sha256": "226e11049b7361d86c00e81e910a3d5982839e2e787faead0c9e9da4854152da", "exit": 0, "reason": "filed design spec pins pre-integration bytes (226e1104); live file is 621b7a33 after e1694ba inserted 3 frontmatter lines; filed bytes frozen, correction carried in fix-23.md", "fix_evidence": "reports/round-10/drift/fix-23.md"},
 {"id": "R10-F23-02", "command": "sha256sum tools/check-gate-battery.py reports/round-9/run-validation.py tools/gates/frozen/provenance-audit/r9-pre/expected.json", "source_locator": "reports/round-9/baselines/registry.md §3.1/§3.2/§4", "round10_verdict": "stale-documented", "output_sha256": "cf95ba233d7924782c7f29e3f7510f58a54d8a94e17fa66fc762a458e88c8047", "exit": 0, "reason": "registry quotes superseded digests: battery 9ad0ef95 -> live 0a126b70; runner 58e8fa4f -> live 8e488130 (now exit 0, F/O/D PASS); provenance pin ba4b2994 -> live 425c74c0 (20/20 inputs verified); all pins valid - drift is in quoted prose only", "fix_evidence": "reports/round-10/drift/fix-23.md"}]
```
