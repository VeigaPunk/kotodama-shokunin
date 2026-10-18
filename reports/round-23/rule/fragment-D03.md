# R23-D03 — integration, r25 commitment, citation audit (draft pass)

- Seat: D R23-D03 (rule drafter 3 of 3). Date: 2026-10-18.
- Axes: operability (integration placement, new-row discipline), depth
  (commitment wording that cannot be read as a retroactive pass).
- Scope: draft contribution only; no SKILL.md, LOG, SCORECARD, or filed-round
  writes. Consolidated output: `reports/round-23/rule/skill-draft.md` §0, §2,
  §3.

## Contribution

**Placement.** `SKILL.md` after the "Derivation replay" section (ends `:242`),
before `## Error patterns` (`:244`) — anchors verified by
`grep -n '^### Derivation replay\|^## Error patterns'` (2026-10-18). This
matches the superseded round-22 proposal's neighborhood
(`reports/round-22/bleed/skill-rule-draft.md:6`) and completes the
typed-pipeline block's arc: typing → routing → replay → **ownership**.

**Style conformance.** The subsection follows the file's house pattern (%
`### Title — subtitle`; authorities paragraph with executable/design
authorities; a cited table; "Thresholds and cautions that are part of the
rule:" with T1-T4 + cautions), mirroring the Slot-label routing and Derivation
replay sections (`SKILL.md:131-242`).

**Round-25 commitment wording.** The D claim requires the commitment in the
rule itself. Wording binds it to filed records only: round 22's rejection and
routing (`LOG.md:3298-3309`; `reports/round-22/routed-resolution.json`
R21-ALIAS-COERCION, R21-MTIME-TIE-BREAK), what already landed at the round-23
baseline `0e81d9d` (projector `2819f687…`; live D4 projection/typed
packet/expected holds; profile `repin_history[2]`; frozen `d4-repin`
generation — each digest-verified 2026-10-18), and the three named tails:
(1) handoff v3 claim-map supersession (`reports/round-22/bleed/repin.md:26-37`:
D4-CL05/06/07/09 and OQ-V3-05 still describe removed rank passengers);
(2) PLACEHOLDER_RE validator-wording disposition
(`routed-resolution.json` R21-MTIME-TIE-BREAK); (3) any combined-source
successor row not landed under round 23's O claim
(`reports/round-23/claims.json` O). The closing sentence forbids reading any
of it as retroactively green and forbids rewriting filed historical wording
(`corpus/lessons/round-22.md:19`).

**Citation audit.** The full ledger is `reports/round-23/rule/skill-draft.md`
§3: every citation in the subsection was opened at its stated revision or
path on 2026-10-18 (`git show <rev>:<path> | sed -n`, `grep -n`, `sha256sum`,
`python3 -c` JSON reads). The round-21 anchors were independently re-opened:
`A21-D4-XF-01` at `reports/round-21/adjacency/ledger.json:93-110`; the prior
census and the 14:01:09Z deterministic-pass/14:05:45Z census contrast at
`reports/round-21/adjacency/A11-A12-handoff.md:23-29,39-47`.

## Review findings

- **F1 (supersession, not duplication).**
  `reports/round-22/bleed/skill-rule-draft.md` (R22-D08) proposed the same
  placement with prospective controls; it predates the landed implementation
  and is superseded by this draft. It remains filed round-22 evidence — never
  edit it; the new draft is the integration source.
- **F2 (orchestrator do/don't).** Do: lift §1 verbatim after `SKILL.md:242`;
  keep every citation; record the landing in LOG as the parent's entry. Don't:
  edit `LOG.md:3298-3309` or any filed round 8-22 artifact; claim handoff v3
  correct-wording or the full historical check green in the same landing (both
  are r25 tails); rerun historical validators in the live tree (isolated
  clone + `TMPDIR` per the frozen-run standard).
- **F3 (claim-decomposition check).** Round-23 claims D requires exactly:
  rule statement ✓ (paragraph 1), injection-point warning ✓ (paragraph 2,
  "unconditional D2 build_payload" verified at `46a03257…:2613`), paired
  controls ✓ (seven-row table), r25 commitment ✓ (closing paragraph), every
  row cited ✓ (§3 ledger). No element of the D claim is unaddressed; nothing
  outside it was added to SKILL.md's draft text.
- **F4 (worker/orchestrator boundary).** Per `AGENTS.md`, during a wave
  workers write only assigned evidence fragments; the orchestrator integrates
  and owns the round verdict via the declared counting command
  (`python3 reports/round-23/run-validation.py`). This fragment makes no
  promotion claim.

Status: draft pass complete; placement and commitment ready for
orchestrator landing.
