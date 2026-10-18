# Round 24 — Box 2a verification: D2→D3 chain (non-author verifier)

- Verifier: round-24 swarm seat (GLM-5.3-flash-low, host-pinned MAX); authored
  none of the lane's artifacts. Date: 2026-10-18. Baseline per
  `reports/round-24/claims.json`: `b5d9844`.
- Assignment: independently execute the D2→D3 segment of SHONEN box 2 per
  SKILL.md/LOG pointers (assemblers `--check`, typed gate, handoff exercise
  v2) and confirm the logged end-to-end tasks exist and are reproducible.
- Method: every command below was run from the SKILL.md/LOG instructions
  alone; TMPDIR pointed at `.scratch`; no git commits. Every `--check`/
  selftest/positive run below left the repo tree unmodified except where a
  finding says otherwise (Finding F-1, restored in full).

## 1. Executed chain legs (command → exit → observed result)

D2 leg:

| # | Command | Exit | Observed |
|---|---|---|---|
| 1 | `python3 tools/assemble-d2.py --check` | 0 | `packet.d2.yml: byte-identical deterministic assembly` |
| 2 | `python3 tools/assemble-d2.py --selftest` | 0 | 42/42 checks; "no file outside the temporary directory touched" |
| 3 | `python3 tools/gates/typed-pipeline-gate.py` (flagless, default packet) | 0 | 16/16 legs ok (`L1-*` ×6, `L2-channel`, `L3-*` ×8, `L4-pins`); emitted set = frozen expected set: 10× `D2L-FORM-UNRESOLVED` (GAR-01…GAR-10), 2× `D2L-NATIVE` hold (L-15/L-16 diacritic), 3× `D2L-RANK` hold + 1 note; banner repeats every hold stays open design debt |
| 4 | `python3 tools/d2-typed-labels.py --packet examples/culture-d2/packet.d2.yml --check examples/culture-d2/typed-labels.d2.yml` | 0 | `typed-labels.d2.yml: byte-identical deterministic projection` (named packet+artifact pair, per the SKILL named-inputs row) |
| 5 | `python3 tools/d2-typed-labels.py --selftest` | 0 | 163/163 checks (shard control matrices, loader/parser malformed cases, live-packet typing, CLI emit/check/tamper) |
| 6 | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` | 2 | 7/7 rows `could-not-evaluate reason=gate_digest_mismatch` — exactly the documented live-tree verdict (SKILL.md "Using the evidence" frozen-replay row; `reports/round-10/drift/fix-18.md`); the freeze artifacts exist and the reader executes them |

D3 leg:

| # | Command | Exit | Observed |
|---|---|---|---|
| 7 | `python3 tools/assemble-culture-d3.py --check` | 0 | `packet.json` AND `packet.gates.yml`: both byte-identical deterministic |
| 8 | `python3 tools/assemble-culture-d3.py --selftest` | 0 | 85/85 checks incl. real naming gate (CROSS-HOLD, no PHON/DERIV FAIL) and real costume gate (R-01 note, no R-02) run read-only |
| 9 | `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` | 0 | counts.total=0, findings [] — supplied model consistent with the frozen pin |
| 10 | `python3 tools/check-evidence-coupling.py --selftest` | 0 | `selftest_passed: true` |
| 11 | `python3 tools/gates/naming-collision-gate.py examples/culture-d3/packet.gates.yml` | 1 (expected red) | 2× `CROSS-HOLD` HOLD (real-language sweep not performed; no priority language/community named) + `NAME-NEAR` REVIEW (E0 vs E1, 1 edit) — the exact findings SKILL.md's D3 replay checklist step 3 says must stay visible |
| 12 | `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d3/packet.gates.yml` | 1 (expected red) | `R-01 [note] C03` declared plant-cloth violation kept visible |
| 13 | `python3 tools/gates/handoff-packet-check.py examples/culture-d3/handoff.md` | 0 | `fields=16/16 glossary-entries=20 findings=0` |

Handoff exercise v2:

| # | Command | Exit | Observed |
|---|---|---|---|
| 14 | `python3 tools/exercise-handoff-e2e.py --profile v2 --quiet` | 0 | `handoff-v2: exit=0 claims=15 links=50/50 drift=named(tools/harness/packet_links.py round-16)` |
| 15 | `python3 tools/exercise-handoff-e2e.py --profile v2 --selftest` | 0 | links leg 50/50 resolved; links-digests leg 2 named round-16 drift rows (tools/d2-typed-labels.py, tools/harness/packet_links.py), no other findings |

## 2. Logged-task existence check (LOG.md pointers)

| Logged entry | Pointer | Confirmed artifact |
|---|---|---|
| LOG.md:1967–1986 — round 3 D2 end-to-end build ("SHONEN box 2 evidence") | frozen under `tools/gates/frozen/round-3/` | MANIFEST.tsv present, 7 sha-pinned rows; replayed as leg 6 |
| LOG.md:2706–2760 — round 7 D3 source-bounded culture assembly | `reports/round-7/d3-contract.json`, assembler + coupling guard "actually exercised through CLI" | `examples/culture-d3/{packet.json,packet.gates.yml,expected.json,handoff.md}`, `tools/assemble-culture-d3.py`, `tools/check-evidence-coupling.py` all present and exercised as legs 7–13 |
| LOG.md:3015–3018 — round 11 O: `tools/exercise-handoff-e2e.py` from live D2/D3 artifacts | tool present | v2 profile exercised as legs 14–15 |
| LOG.md:3195–3206 — round 15 O: handoff packet v2 (uncertainty dimension + claim-to-record links; validators 19/19 + 31/31) | `reports/round-15/handoff/` surfaces | v2 positive run reproduces: claims=15, links 50/50 |

## 3. Findings

**F-1 (operability hazard — named as a box-3 condition candidate).
`reports/round-7/run-validation.py` executes on any invocation, including
`--help`, and rewrites the filed `reports/round-7/validation.json` in place.**
Measured this session: a `--help` invocation ran the full validation and
modified exactly one line of the filed receipt (the inventory failure string's
knowledge totals: 189→199 files). The receipt was restored byte-identical from
git (`git checkout -- reports/round-7/validation.json`; `git status` clean
after). SKILL.md's D3 replay checklist step 5 tells a reader to run this
command in the live tree, so a cold-run seat following SKILL.md literally will
clobber a filed artifact. The D2→D3 chain legs above are unaffected — no other
command in §1 writes any repo file (selftests state and showed
temporary-directory-only writes; `git status` confirmed a clean tree after the
batch).

**F-2 (the round-7 acceptance aggregate is not reproducible as a pass
post-round; per-leg commands are).** The accidental re-run's receipt reads
`acceptance_checks_passed: false`: `F_passed: false` (round-7's F claim counts
source ledgers newly created during round 7; a later tree has none new — by
design) and the preservation leg now records 199 knowledge files vs the 189
frozen at round 7 (tree growth recorded as drift vs the round-7 baseline).
`O_passed: true` (guards: positive 5/5, domain 16/16, malformed controls ran).
Consequence for box 2: D2→D3 reproducibility is grounded in the per-leg
commands of §1, not in re-running `reports/round-7/run-validation.py` today.

**F-3 (documented red, not a break).** The round-3 frozen replay is
could-not-evaluate in the live tree (leg 6) because the round-8 admission
commit revised the pinned gate bytes; SKILL.md documents this exact verdict
and the isolated-tree restoration procedure. Confirmed the freeze artifacts
exist and behave as documented.

## 4. Verdict — box 2a (D2→D3 segment of SHONEN box 2)

**Verified.** The chain exists, is logged with resolving pointers, and every
executable leg reproduces from SKILL.md/LOG instructions alone with the logged
verdicts: assemblers byte-identical (D2; D3 both derived outputs), typed gate
16/16 legs with the emitted hold set equal to the frozen expected set,
163/163 + 42/42 + 85/85 selftests, D3 coupling gate green against its frozen
pin, legacy D3 gates red at exactly the severity SKILL.md says to keep,
handoff envelope 16/16 + 20/20, handoff exercise v2 green with its named
drift rows. Conditions to carry (not defects in this segment): F-1 (acceptance
runner overwrites its filed receipt on any invocation — recommend recording as
a box-3 cold-run condition) and F-2 (round-7 acceptance aggregate red
post-round by design).

Scope note: this seat covered D2→D3 only; D4 and the full handoff leg of box 2
are sibling seats' scope (`reports/round-24/box2-d4.md`). No git commits made;
only this file written.
