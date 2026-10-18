# R19-D09 — LOG.md integration draft (paste-ready, must be re-measured before pasting)

- round: 19 (operator: loop 2 of 3, build round 3 of 4; `reports/round-19/claims.json`,
  provider `hyper/deepseek-v4.1-flash` per the operator substitution). Lane:
  `kotodama-shokunin`.
- seat **R19-D09** (integration drafts). Assignment (verbatim): "D R19-D08..D10
  (lessons + integration): corpus/lessons/round-19.md draft; LOG/SCORECARD
  integration drafts; fragment ledger."
- date: 2026-10-18 (stamps UTC). Baseline revision
  `e5718945a1ab0a0c3db955338d2cae77d68fd348` (round-18 admit); declare
  `169c616613899f7ba86b8fb58ed808bdfd4b5ccd`.
- canon: **NON-CANON integration draft.** Draft text for `LOG.md`; it edits no byte
  of `LOG.md`, `SCORECARD.md`, `corpus/**`, `tools/**`, `examples/**`, or any filed
  round-8..18 artifact. The parent owns placement, wording and admission. Per
  `AGENTS.md`: "During a parallel wave, workers write only their assigned evidence
  fragments; the parent integrates them into LOG.md after the batch."
- writes: this file, plus gitignored scratch under `.scratch/`. No commit, no push.
- **Every digest and count below is a read-time pin of a live wave.** Re-measure on
  the settled tree before pasting. This seat does not run
  `reports/round-19/run-validation.py` (round-14 guard: a counting command can
  itself be a writer).

## 0. State of this draft

The round is **live and unclosed** at this seat's read. `reports/round-19` grew
2 → 16 → 25 → **32** files between 11:32:27Z and 11:37:21Z; the worktree was dirty
throughout (`M tools/check-gate-battery.py`, whose digest moved
`53b1913a…` → `72d6e011…`). This draft therefore carries the **measured state and
the open findings**, not an admission line; the admission line is a placeholder.

## 1. Draft LOG.md entry (paste-ready skeleton)

```markdown
## 2026-10-18 — Round 19 <ADMIT/REJECT — parent fills> (loop 2, build 3 of 4; D4 craft knowledge, thin-partition wave, D4 battery integration)

- **Trigger:** regimen; claims D/C/O in `reports/round-19/claims.json`; baseline
  `e571894`; <completed>/64 completed; <integrator acts>.
- **D (depth):** SKILL.md gains the D4-derived decision-table subsection (slot-label
  routing model; derivation-replay discipline) + the D4 lesson entry in
  `corpus/lessons/`; <verdict>.
- **C (coverage):** >=8 new sourced entries across verification + synthesis
  (>=3 each); verification 15 -> <n>, synthesis 24 -> <n>; `corpus/README.md`
  reconciled; <verdict>.
- **O (operability):** battery default covers the D4 gates (7 structural + 2 D4 =
  9/9) with selftest controls; D4 expected.json baselines committed under the
  standard layout; battery + craft + typed/assembly selftests green; <verdict>.
- **Integrator acts:** <parent fills — see §3 open findings>.
- **Evidence:** `reports/round-19/validation.json` acceptance <true/false>.
```

## 2. Measured state the parent should paste from (read-time, 2026-10-18)

### 2.1 Round shape

| reading | value | command / stamp |
|---|---|---|
| declare commit | `169c616613899f7ba86b8fb58ed808bdfd4b5ccd` | `git rev-parse HEAD`, 11:32:27Z |
| baseline (HEAD's parent) | `e5718945a1ab0a0c3db955338d2cae77d68fd348` | `git log --format='%h %cI %s' -3` |
| `reports/round-19` file count | 2 (11:32:27Z) → 16 (11:34:26Z) → 25 (11:35:51Z) → **32 (11:37:21Z)** | `find reports/round-19 -type f \| wc -l` |
| worktree | dirty: `M tools/check-gate-battery.py` + untracked round-19 files | `git status --porcelain` |
| declared worker allocation | D-knowledge 10 + C-authors 10 + C-reviewers 8 + O-battery 12 + O-baselines 8 + auditors 6 + X 10 = **64** | `reports/round-19/targets.json:5-13` |

### 2.2 Claim D — depth (D4 craft codification)

| reading | value | command / stamp |
|---|---|---|
| D4 typed packet committed | `examples/culture-d4/packet.d4.typed.yml` sha256 `f63ed531…`, 89554 B, tracked at `e571894` | `sha256sum`, 11:32Z |
| routing rows on the typed packet | exactly **12** (`GAR-01..06` + `LEX-GAR-01..06`); garment rows `owed_slot: null`; slot rows `owed_slot` = own slot id | regex read of the `typed_channel:` block, 11:33Z |
| gate over `packet.d4.yml` (round-18 D input) | exit **0**, `summary: 19/19 legs passed`, gate `04ad4bb4…` | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`, 11:32Z |
| gate over `packet.d4.typed.yml` | exit **1**, `summary: 14/16 legs passed`, `FAIL L3-routing-consistency` | same command, other input, 11:32Z; re-measured 11:36Z |
| D4 adapter digest | `tools/assemble-d4-typed.py` sha256 `087846719041db0b…`, committed at `e571894`, worktree clean | `sha256sum`, 11:32Z |
| D4 adapter selftest | exit **1** (red) | `python3 tools/assemble-d4-typed.py --selftest`, 11:32Z; re-measured 11:36Z |
| expected-holds artifact | `examples/culture-d4/expected-holds.json` sha256 `09490a27…`, 15 holds / 1 note / 0 fails, no reconciliation pointer inside | `sha256sum`; `reports/round-18/d4/holds.md` §2-§3 |
| register-scoped slot class | absent: `D4L-REGISTER` / `#plain` → 0 occurrences across all three D4 artifacts; `REGISTER` in the projector → 0 | `grep -c`, 11:36Z |
| `SKILL.md` D4 content | **0** D4 mentions; digest `e8d238a6…` | `grep -c -i "d4" SKILL.md`, 11:37Z |
| D4 lesson entry | `reports/round-19/integration/d4-lessons-entry.md` (this seat) — **not** `corpus/lessons/round-19.md` (peer X21's survey; see §3.5) | — |

### 2.3 Claim C — coverage (thin partitions)

| reading | before (claims.json) | 11:32:27Z | 11:34:26Z | 11:35:51Z | 11:37:21Z | command |
|---|---:|---:|---:|---:|---:|---|
| verification partition | 15 | 15 | 17 | 20 | **20** | `ls corpus/knowledge/verification \| wc -l` |
| synthesis partition | 24 | 24 | 24 | 24 | **28** | `ls corpus/knowledge/synthesis \| wc -l` |
| civilizations partition | 94 | 94 | 94 | 94 | 94 | `ls corpus/knowledge/civilizations \| wc -l` |

Net movement observed: verification **+5**, synthesis **+4** — on track for the
claim's >=8 new entries with >=3 each, **but re-measure on the settled tree** (the
counters were still moving at the last stamp). `corpus/README.md` still read
`revision: 1.3` / "Total knowledge entries: 189" at 11:37Z (digest `9df4b7c5…`),
so the README reconciliation lags the content it indexes. The gap registry is
`reports/round-19/gaps.md` (10 declared gaps, `R19-C11..C20`); entries
`reports/round-19/entries/R19-C11..C15.md` had landed by 11:35Z.

### 2.4 Claim O — operability (D4 battery integration)

| reading | value | command / stamp |
|---|---|---|
| battery default run | exit **0**, `summary {pass: 7, fail: 0, unevaluable: 0}` (duty-1 selftests = the seven structural gates) | `TMPDIR=/var/tmp/k19c python3 tools/check-gate-battery.py`, 11:37Z |
| battery baseline duty | exit **0**, `coverage 9/9`, `gates_registered 9`, `gates_uncovered []`, `baselines_found 17`, `pinned 17` | same run |
| D4 baseline dirs | `tools/gates/expected/d4-{assembly,typed-labels}-check-gate/r19-pre/expected.json` (untracked at 11:37Z; landed 11:33:26–11:33:50Z) | `git status --porcelain`; battery report |
| battery file | digest moved `7aa898d6…` → `53b1913a…` → `72d6e011…` inside the window | `sha256sum`, 11:37Z |
| D4 thin gates | `d4-typed-labels-check-gate.py` `05f99629…`; `d4-assembly-check-gate.py` `df1a364b…` | `sha256sum`, 11:32Z |
| D4 gate self-tests | **none ship**: `d4-assembly-check-gate.py --selftest` → exit 2 (the flag is read as an input path); `d4-typed-labels-check-gate.py --selftest` → exit 0 but forwards to the peer's own selftest (39/39) | peer survey X21, 11:35Z |
| named selftest set | gate 12/12; craft green; `assemble-culture-d4.py --selftest` 81/81; **`assemble-d4-typed.py --selftest` red** | 11:32–11:37Z |

**The claim's O `before`-text is superseded by the round's own artifacts:** the D4
baselines landed inside the census window, so the battery's baseline duty already
reads 9/9 (measured, not declared). What remains unmet is the selftest duty: the
battery runs exactly the seven structural gates' selftests, no D4 gate ships one,
and the D4 adapter's selftest is red.

## 3. Open findings routed to the parent (not adjudicated here)

1. **L19-D08-1 — the D4 adapter's own selftest is red at HEAD.**
   `python3 tools/assemble-d4-typed.py --selftest` exits 1 at adapter sha256
   `08784671…`. Two visible defects: the selftest mirror never copies
   `tools/assemble-d2.py` (`tools/assemble-d4-typed.py:405-409`), and the slot-label
   fixture (`:467-477`) routes 0 rows because the slot lookup keys on the raw
   `form_slot` string (`:199-200`). Round-18's `validation.json` never ran this
   selftest, so claim O's "all typed/assembly selftests green" is an open round-19
   obligation. Independently corroborated by the peer survey (4/11 at `08784671…`).
2. **L19-D08-2 — the gate over the *typed* packet fails `L3-routing-consistency`.**
   Exit 1, 14/16 at gate `04ad4bb4…`; the same gate over `packet.d4.yml` is 19/19.
   Candidate readings: the routing-set comparison counts the six explicit
   `owed_slot: null` cells, or the adapter should omit the key on garment rows. This
   bears directly on the O axis's proposed "record the round-18 pending row"
   deliverable: that row's input is this typed packet, and freezing it now would
   pin a **red** verdict.
3. **Design debt carried, not repaired: the register-scoped slot class is
   unbuilt.** Design §Δ1 (`reports/round-17/d4/design-brief.md:254-275`) requires a
   second routing class (on-channel, slot-inadmissible quote forms,
   `D4L-REGISTER-UNRESOLVED`); the delivered artifacts carry zero occurrences and
   the projector has no engine path. Recorded as debt in
   `reports/round-19/integration/d4-lessons-entry.md` lesson 6.
4. **The expected-holds authority question remains open.** The artifact equals the
   gate's own output and carries no reconciliation pointer; the reconciliation
   lives in `reports/round-18/d4/holds.md`. Round-18's lesson 4 recorded the same
   question undecided; this round inherits it.
5. **A dispatch collision on `corpus/lessons/round-19.md`.** This seat (R19-D08) and
   peer seat **X21** were both assigned that path. X21's gate-keeper survey landed
   there (~11:33Z; digest `df4de597…` at 11:37Z) and superseded this seat's
   20 260-byte draft. This seat did **not** write the path again (a second write
   would race X21). The D4 craft entry is preserved as
   `reports/round-19/integration/d4-lessons-entry.md`; X21's own survey states the
   D claim's lesson entry "must land as a different path or name its owner". **The
   parent decides** the final placement (`corpus/lessons/round-19-d4.md`, a merge
   into X21's survey, or a drop).

## 4. What the parent must do before pasting

1. Re-run the §2 tables on the settled tree; replace every `<placeholder>`.
2. Read `reports/round-19/validation.json` (written only by
   `python3 reports/round-19/run-validation.py`) and paste its acceptance value.
3. Reconcile `reports/round-19/integration/fragment-ledger.md` against the settled
   `reports/round-19/**` tree (the ledger is a read-time census).
4. Decide the five open findings' dispositions (repair in-round, route to round 20,
   or record as debt) and say which in the entry's **Integrator acts** line.
5. Resolve the `corpus/lessons/round-19.md` ownership collision (§3.5).
6. Keep the append-only form: a new entry appended to `LOG.md`; never edit a filed
   entry.
