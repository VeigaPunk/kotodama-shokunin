# Round-24 SKILL audit 1 — "Gates and probes" registry, executable claims re-run

- Auditor: round-24 swarm seat, **non-author** of every lane artifact audited here.
- Date: 2026-10-18. Audit baseline: committed HEAD `8fbcee9f` ("round-24: declare GLM-2
  claims C/O/D"); claims.json `baseline_revision` was the round-23 baseline `b5d9844`.
- Scope: every executable claim in `SKILL.md` section `## Gates and probes`
  (SKILL.md:461-519 at HEAD) — the 12-row registry table (rows at SKILL.md:490-501)
  plus the surrounding prose claims. The D3-section gate table (SKILL.md:555-558) is
  outside this section; it was run anyway as cross-coverage (Appendix A).
- Method: registry entry commands run in the **live tree** with a `git status`
  snapshot taken before and after every batch (live tree byte-unchanged by all runs
  below unless stated). Selftests and destructive probes run in an isolated export
  (`.scratch/r24-gates/export-a`, tools/+examples/ copy). Every fix-adjacent claim
  was probed with its negative control, not taken from tool output alone.
- Environment: Python 3.14.7, `/usr/bin/python3`.

## 1. Registry rows (SKILL.md:490-501)

Verdicts: **CURRENT** = re-produced as the row claims; **STALE** = observed behavior
contradicts the row = finding. Exit codes are the command's own.

| # | Row (SKILL.md line) | Claim re-run | Command → observed | Verdict | Evidence |
|---|---|---|---|---|---|
| 1 | phonology-sanity-gate (:490) | entry on a culture packet, verdict map; selftest in isolated export; fixtures at stated paths; write scope | `phonology-sanity-gate.py examples/culture-d2/packet.d2.yml` → exit 1, 3 `A-NEUTRAL` REVIEW findings; `--selftest` → exit 0 "15/15 planted finding IDs present; 29 control cases passed" | CURRENT | fixtures `tools/gates/fixtures/phonology-sanity-gate.{yml,expected}` exist; write-scope probe row W-1 below |
| 2 | lexicon-coverage-audit (:491) | same claim set | entry → exit 0 (clean on current packet); `--selftest` → exit 0 "14/14 checks passed" | CURRENT | probe W-2 |
| 3 | myth-consistency-gate (:492) | same claim set | entry → exit 0 on current packet (round-3 pin had exit 1 — packet bytes evolved, see O-1); `--selftest` → exit 0, planted MC-* IDs, "clean control exit 0" | CURRENT | probe W-3 |
| 4 | costume-era-consistency-gate (:493) | same claim set | entry → exit 0 on current packet; `--selftest` → exit 0 "10/10 checks passed; fixture exit 1 with 21 planted finding IDs" | CURRENT | probe W-4 |
| 5 | naming-collision-gate (:494) | entry, verdict map, read-only selftest | entry → exit 1: `PHON-INVENTORY` FAIL ×3 (GAR-08/09/10) + `CROSS-HOLD` HOLD — findings+hold, not clean; `--selftest` → exit 0 "12 findings across 11 ids … malformed inputs exit 2" | CURRENT | live guard clean (read-only); fixtures exist  (evidence: re-measured live 2026-10-18; commands in audit-gates.md §3) |
| 6 | provenance-audit (:495) | reads corpus entries; selftest in isolated export; fixture dir `tools/gates/fixtures/provenance/`; write scope | `provenance-audit.py corpus/knowledge/verification/to-verify-triage-protocol.md` → exit 0, "13 mark(s) on 13 line(s), findings=0"; on `fixtures/provenance/good-entry.md` → exit 0; `--selftest` → exit 0 "7 fixture file(s) … exit 1 on the defect tree, exit 0 on the clean entry, exit 2 on a missing path" | CURRENT | probe W-5; defect fixtures present in `tools/gates/fixtures/provenance/` |
| 7 | handoff-packet-check (:496) | reads the Markdown handoff envelope; selftest; read-only | `handoff-packet-check.py examples/handoff-packet.sample.md` → exit 0 "fields=16/16 glossary-entries=20 findings=0"; `--selftest` → exit 0 "11 findings across 9 ids … CLI verified from another cwd" | CURRENT | live guard clean |
| 8 | frozen-replay (:497) | `replay-frozen.py <MANIFEST.tsv>` verdict map (0 reproduced / 1 mismatch / 2 could-not-evaluate); selftest; auto-cleaned scratch only | `--selftest` → exit 0 **79/79 checks passed** (incl. `bad-header: manifest_malformed` and "gate not launched" — pins validated, command string never executed); live round-3 replay → exit 2, 7/7 `gate_digest_mismatch`; restored-pins replay → exit 0, 7/7 "reproduced" (P-4 below) | CURRENT | both halves of the exit map observed in this audit |
| 9 | uncertainty-inventory (:498) | `source-audit-inventory.py --json` → 0 inventory, 2 could-not-evaluate; selftest; read-only | `--json` → exit 0, inventory JSON emitted; `--selftest` → exit 0 "exact counts, policy/substantive split, **no-write and determinism** checks, missing-root, empty-root and non-UTF-8 exit-code controls" | CURRENT | live guard clean on `--json` |
| 10 | D2 assembly drift (:499) | `assemble-d2.py --check` → 0 byte-identical; selftest; check read-only | `--check` → exit 0 "packet.d2.yml: byte-identical deterministic assembly"; `--selftest` → exit 0 "42/42 checks passed — fixture CLI assemble/--check/tamper … **no file outside the temporary directory touched**" | CURRENT | default (regenerating) mode intentionally not run against the live committed packet; its behavior is covered by the selftest's temp-dir assemble/tamper controls |
| 11 | contrastive craft example (:500) | entry on committed example → 0 checks pass; `--selftest` (committed example + isolated subprocess controls, foreign cwd); `--counts` = declared audit-count block; read-only incl. `--report <existing-report.md>` | entry → exit 0 "OK all checks passed (audits=7, mech_cases=11, derivations=9, approx_checks_runner=37)"; `--counts` → exit 0; `--selftest` (full tree) → "SELFTEST OK 10/10 tamper cases detected; CLI-SELFTEST OK 18/18 cases passed" | CURRENT | note O-4: in a tools/+examples-only export the selftest fails its `positive-report` leg because it reads the committed `reports/supplement-opencode-1/32-craft-exercise.md` — "committed example" includes that report; not a defect |
| 12 | isolated legacy selftest battery (SKILL.md:501) | fixed (F3, dated 2026-10-18, audit-fixes.md — control): committed default now exits **0**; the prior exit-**2** reading with `BASELINE-GATE-UNCOVERED` for **myth and naming**, pins "live under `reports/round-9/baselines/`", "add that root via `--baselines-root` to reach 0" | default `check-gate-battery.py` → **exit 0** (summary `pass=7 fail=0 unevaluable=0`; duty 2 discovered **19 baseline rows, every one `pinned`/gate-sha match, 0 uncovered**, across roots `tools/gates/expected` (6 files), `tools/gates/frozen` (10), `reports/round-9/baselines` (3) — myth and naming included); `--baselines-root reports/round-9/baselines` → **exit 2** `BASELINE-GATE-UNCOVERED` (roots REPLACED → only 3 rows discovered; the frozen/expected-root gates become uncovered; duty 1 still 7/7) | **STALE — finding F-1** | `.scratch/r24-gates/battery-default.json`, `battery-root.json`; mechanism `tools/check-gate-battery.py:100` ("--baselines-root replaces the default baseline roots for one run") and `:148-152` (`BASELINE_ROOTS` includes `reports/round-9/baselines`) |

## 2. Prose claims in the section

| ID | Claim (SKILL.md lines) | Re-run | Verdict | Evidence |
|---|---|---|---|---|
| P-1 | "The seven legacy selftests pass" (:466) | all seven selftests in the isolated export | **CURRENT** — 7/7 exit 0: phonology (15/15+29 controls), lexicon (14/14), myth (planted MC-* IDs), costume (10/10), naming (12 findings/11 ids), provenance (7 fixture files), handoff (11 findings/9 ids) | export run log, §1 rows 1-7  (evidence: re-measured live 2026-10-18; commands in audit-gates.md §3) |
| P-2 | "five of them write only inside their own fixture directories: a present fixture is verified byte-for-byte, a divergent one is refused and left untouched, and only a missing one is regenerated atomically (phonology, lexicon, myth, costume, provenance)" (:466-470) | 5×3 probe matrix, fresh copy per gate: (a) present fixture, (b) one byte flipped, (c) fixture deleted | **CURRENT** — all 15 cells as claimed: present exit 0 + bytes unchanged; divergent exit 1 + bytes untouched; missing → regenerated and **byte-equal to the committed fixture** | probe results: `probe-phon/lex/myth/cost/prov present_exit=0 present_unchanged=yes divergent_exit=1 divergent_untouched=yes missing_exit=0 missing_regenerated byte-equal-to-committed`  (evidence: re-measured live 2026-10-18; commands in audit-gates.md §3) |
| P-3 | replay "validates SHA-256 pins and executes snapshots, never the manifest command string"; exit map incl. `snapshot_tampered` (:476-480) | selftest; both round-3 replays | **CURRENT** — selftest 79/79 includes `gate not launched` on a malformed manifest (command string never executed) and tamper classes; live/restored runs exercise exit 2 and exit 0 legs | §1 row 8; P-4  (evidence: re-measured live 2026-10-18; commands in audit-gates.md §3) |
| P-4 | "measured 2026-10-17, the live tree reads exit 2 with 7/7 `gate_digest_mismatch` because the round-8 admission commit (`e1694ba`) revised every gate file the pins name — restore those files from `291c714` and the same manifest reproduces 7/7, exit 0" (:481-485) | (a) live round-3 replay; (b) isolated copy with the 6 pinned gate files restored from `291c714` (restored shas match the manifest `gate_sha256` pins), replay | **CURRENT** (re-measured 2026-10-18) — (a) exit 2, 7/7 `gate_digest_mismatch`, 0 reproduced; (b) exit 0, "7/7 rows reproduced the recorded verdicts". Note O-2: the pins name 6 distinct gates (provenance twice); `handoff-packet-check.py` is not among them and does not exist at `291c714` — the prose wording ("every gate file the pins name") stays exact | replay stdout both runs; manifest `tools/gates/frozen/round-3/MANIFEST.tsv` |
| P-5 | round-5 acceptance "re-runnable with `python3 reports/round-5/run-validation.py`; it records the two declared claims and writes its own validation receipt" (:516-519) | ran it in the live tree | **CURRENT as worded, with drift observation O-5** — it runs, records the two claims (F, O) and rewrites `reports/round-5/validation.json` (byte-different: both recorded claims now **error** — F "non-append corpus edit … ottoman.json OTT-06"; O = the same round-3 `gate_digest_mismatch` exit-2 of P-4a). Historical-acceptance-vs-current-tree drift, not a wording staleness; restored the receipt after the run | command output (errors block); `reports/round-5/run-validation.py:194` writes only `HERE/validation.json` |
| P-6 | verdict map "0 clean / 1 findings / 2 could-not-evaluate"; "provenance-audit reads corpus entries; handoff-packet-check reads the Markdown handoff envelope; the other five read culture packets" (:462-465) | observed across §1 runs + selftest-asserted exit-2 classes | **CURRENT** — 0 and 1 legs observed on real packets; 2 legs asserted by selftests (malformed/missing inputs, non-UTF-8, missing root) and observed on replay/battery failure classes | §1  (evidence: re-measured live 2026-10-18; commands in audit-gates.md §3) |

## 3. Findings

**F-1 (STALE — the one finding). `SKILL.md:501` battery row is inverted against current tool behavior.**
Claimed: committed default exits 2 (`BASELINE-GATE-UNCOVERED` for myth and naming) and adding
`--baselines-root reports/round-9/baselines` reaches 0.
Observed (both commands run 2026-10-18, HEAD `8fbcee9f`):
- `python3 tools/check-gate-battery.py` → **exit 0**; 7/7 selftests; 19/19 baseline rows `pinned`
  with gate-sha match, 0 uncovered; roots = `tools/gates/expected` + `tools/gates/frozen` +
  `reports/round-9/baselines` (`tools/check-gate-battery.py:148-152`) — myth and naming pins are
  already inside the default roots.
- `python3 tools/check-gate-battery.py --baselines-root reports/round-9/baselines` → **exit 2**
  with `BASELINE-GATE-UNCOVERED`; `--baselines-root` **replaces** the roots for one run
  (`tools/check-gate-battery.py:100`), leaving only 3 discovered rows, so the frozen/expected-root
  gates go uncovered. Duty 1 still passes (7/7).
Disposition note (non-author): a dated correction of exactly this row is already present in the
working tree during this audit window (uncommitted SKILL.md edit by the round-24 D seat, citing
`:100`/`:151` with controls in `reports/round-24/audit-fixes.md`). My independent measurements
corroborate that fix; this audit's baseline verdict is against committed HEAD, where the row is
stale. The `reports/round-9/baselines/registry.md` §5 item 6 pointer remains valid.

**O-1 (observation, not staleness).** On the *current* `examples/culture-d2/packet.d2.yml`,
lexicon/myth/costume exit 0 while the round-3 manifest pins exit 1/1/0 against its pinned input
snapshot — the packet evolved since round 3; the gates' verdict mapping is intact and the replay
pins the old bytes by design (P-4). No registry claim is contradicted.

**O-2 (observation).** The round-3 manifest's 7 rows name 6 distinct gates;
`handoff-packet-check.py` is absent at `291c714`. The prose sentence "revised every gate file the
pins name" remains exactly true; recorded so a future reader does not expect 7 distinct gate
files in the restore control.

**O-3 (observation, hygiene).** During this audit window, parallel round-24 seats concurrently
modified the working tree: SKILL.md (D-seat fixes incl. F-1's row), `reports/round-7/validation.json`
(regenerated by a seat running `reports/round-7/run-validation.py` — its receipt now records
"historical knowledge totals changed: files 189→199"), and new `reports/round-24/box*.md` files.
None of these are this seat's writes; none were touched by this seat. This seat's only live-tree
write was the P-5 re-run of the round-5 validator, whose rewritten `reports/round-5/validation.json`
was restored to HEAD bytes immediately after.

**O-4 (isolation note).** The craft selftest's `positive-report` control reads the committed
`reports/supplement-opencode-1/32-craft-exercise.md`; a tools/+examples-only export fails that leg
(exit 1, "cannot read report"). SKILL.md's "committed example" wording already covers it; future
cold-run seats should selftest in a tree that includes `reports/supplement-opencode-1/`.

**O-5 (drift observation).** A fresh round-5 acceptance run no longer passes its own recorded
claims (F and O both error, see P-5): the corpus file `ottoman.json` (`OTT-06`) has a non-append
edit relative to the round-5 record, and the round-3 replay leg now exits 2 in the live tree
(which P-4 shows is the documented, expected live-tree state). The SKILL.md wording about the
validator remains true; the *content* divergence is worth the parent's eye when reading
`reports/round-5/validation.json`.

## Appendix A — cross-coverage: D3-section gate table (SKILL.md:555-558, outside assigned section)

| Row | Command | Observed | Verdict |
|---|---|---|---|
| D3 assembly drift (:557) | `assemble-culture-d3.py --check` → exit 0; `--selftest` → exit 0 | CURRENT |
| D3 evidence coupling (:558) | `check-evidence-coupling.py examples/culture-d3/packet.json` → exit 0; `--selftest` → exit 0 | CURRENT |

## Appendix B — raw exit-code ledger (commands as run)

```
# live tree (git-status guard: clean before/after every batch)
phonology-sanity-gate.py examples/culture-d2/packet.d2.yml      -> 1
lexicon-coverage-audit.py examples/culture-d2/packet.d2.yml     -> 0
myth-consistency-gate.py examples/culture-d2/packet.d2.yml      -> 0
costume-era-consistency-gate.py examples/culture-d2/packet.d2.yml -> 0
naming-collision-gate.py examples/culture-d2/packet.d2.yml      -> 1
handoff-packet-check.py examples/handoff-packet.sample.md       -> 0
provenance-audit.py corpus/knowledge/verification/to-verify-triage-protocol.md -> 0
provenance-audit.py tools/gates/fixtures/provenance/good-entry.md -> 0
source-audit-inventory.py --json                                -> 0
assemble-d2.py --check                                          -> 0
check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json -> 0
  (… --counts)                                                  -> 0
check-gate-battery.py                                           -> 0   [F-1: row claims 2]
check-gate-battery.py --baselines-root reports/round-9/baselines -> 2  [F-1: row claims 0]
replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv (live) -> 2  (7/7 gate_digest_mismatch)
reports/round-5/run-validation.py                               -> ran; receipt rewritten, restored
# isolated export (.scratch/r24-gates)
7 legacy gate --selftest                                        -> 0 ×7
replay-frozen.py --selftest                                     -> 0 (79/79)
source-audit-inventory.py --selftest                            -> 0
assemble-d2.py --selftest                                       -> 0 (42/42)
check-craft-exercise.py --selftest (full tree)                  -> 0 (10/10 + 18/18)
check-gate-battery.py --selftest                                -> 0 (35/35)
write-scope probes (5 gates × present/divergent/missing)        -> as P-2
replay-frozen.py round-3 MANIFEST (gates restored from 291c714) -> 0 (7/7 reproduced)
# appendix A
assemble-culture-d3.py --check / --selftest                     -> 0 / 0
check-evidence-coupling.py examples/culture-d3/packet.json / --selftest -> 0 / 0
```
