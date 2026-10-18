# R29-O09 — derived-packet false red in the typed-pipeline gate

- Date: 2026-10-18.
- Status: **closed in the delivered gate; current controls green.** This note records the verified disposition; no gate source was changed in R29.

## Defect and bounded correction

R25 reproduced a false red when the gate graded its own derived D4 packet: the old legacy rebuild doubled backslash escaping, manufacturing `DERIV-REPLAY` findings, while the routing reader treated the string `"null"` as a present owed slot. The R25 correction grades a typed packet against its declared, digest-checked source; when no declared source exists, it uses the rebuild only with a round-trip fidelity check and refuses unfaithful input instead of reporting a manufactured content failure. One shared null-ish predicate is used for routing fields.

Historical before/after evidence is in `reports/round-25/gate-input/verify.md` §§1–4. Its measured pre-fix command on 2026-10-18 was `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` (14/16, including eight false `DERIV-REPLAY` lines); the R25 control matrix on the same date measured source 19/19, typed D4 16/16, missing/stale declared-source refusals, and a 19/19 selftest. These historical values are not substituted for the current remeasurement below.

## Independent current control

At **2026-10-18 17:59:16−03:00**, with `TMPDIR=$PWD/.scratch`, I ran:

- `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → exit 0, **20/20** legs.
- `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` → exit 0, **17/17** legs.

The totals differ from R25 because later delivered legs were added; they are not treated as a mismatch. At **2026-10-18 17:59:18−03:00**, `python3 tools/gates/typed-pipeline-gate.py --selftest` → exit 0, **19/19** controls, including the null-ish and declared-source controls.

## Disposition

Retain the fix as delivered. The source/derived positive checks and missing/stale-source negative checks discriminate the intended behavior. No historical freeze or report was edited; any future gate change requires a successor measurement and new pin rows.