# Round 24 — box-3 cold-run conditions list (COLD-RUN 4, condition scribe)

- **Seat:** COLD-RUN 4 (condition scribe), O-cold-run lane, round 24.
- **Date:** 2026-10-18.
- **Non-author statement:** this seat authored none of the lane's artifacts
  prior to this file; no other round-24 seat's filed report was read.
- **Scope:** what a future executor still needs **beyond the four cold-run
  files** (SKILL.md, AGENTS.md, PROVINCE.md, SHONEN.md) to execute the
  SKILL.md executable checklist end-to-end, with severity per condition.
- **Method:** first-hand execution of every leg in an isolated export of the
  tree at round-24 baseline work state (`.scratch/cold-run-4/tree/`, tar of
  the working tree minus `.git`, `.scratch`, `.ufo`, `__pycache__`;
  `TMPDIR` pointed at the repo's `.scratch`). The real repo was not modified
  by any leg. Raw logs: `.scratch/logs/*.log` (scratch is gitignored and
  disposable; measured outputs are therefore quoted inline below).

## Severity definitions

- **blocker** — a declared leg cannot be executed at all from the four files.
- **major** — the leg executes but the four files set a wrong expectation, so
  an honest executor can record a false verdict (false red or false green).
- **minor** — friction or ambiguity resolvable by plain discovery (`ls`,
  reading the named manifest), with no plausible false verdict.

## A. Verified-executable baseline (what the four files alone got right)

Measured 2026-10-18, Python 3.14.7. Exit codes are the tools' own.

| Leg (command as executed) | Exit | Note |
|---|---|---|
| `phonology-sanity-gate.py examples/culture-d2/packet.d2.yml` | 1 | A-NEUTRAL REVIEWs — documented steady state (SKILL.md "Using the evidence" row 1) |
| `lexicon-coverage-audit.py` / `myth-consistency-gate.py` / `costume-era-consistency-gate.py` (same packet) | 0 / 0 / 0 | clean |
| `naming-collision-gate.py` (same packet) | 1 | PHON-INVENTORY on `GAR-*` (the documented 10/10 class) + CROSS-HOLD — documented steady state |
| `handoff-packet-check.py examples/handoff-packet.sample.md` | 0 | fields 16/16, glossary 20, findings 0 |
| `provenance-audit.py corpus/knowledge/linguistics` | 0 | files=19, marks=76, findings=0 |
| `source-audit-inventory.py --json` / `--selftest` | 0 / 0 | |
| `check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` / `--selftest` | 0 / 0 | audits=7, mech=11, derivations=9 |
| `assemble-culture-d3.py --check` / `--selftest` | 0 / 0 | byte-identical |
| `check-evidence-coupling.py examples/culture-d3/packet.json` (plain and `--frozen examples/culture-d3/expected.json`) / `--selftest` | 0 / 0 / 0 | |
| `naming-collision-gate.py` + `costume-era-consistency-gate.py` on `examples/culture-d3/packet.gates.yml` | 1 / 1 | exactly the SKILL-documented expected reds (CROSS-HOLDs; C03 R-01 note) |
| `handoff-packet-check.py examples/culture-d3/handoff.md` | 0 | |
| `assemble-d2.py --check` / `--selftest` | 0 / 0 | byte-identical |
| `d2-typed-labels.py --selftest` | 0 | **163/163 checks passed** — matches the SKILL.md claim |
| `typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | **19/19 legs** — the documented canonical green |
| `assemble-d4-typed.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/packet.d4.typed.yml` | 0 | byte-identical typed packet |
| `replay-frozen.py tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` | 0 | 3/3 rows reproduced |
| `replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root <live tree>` | 2 | 7/7 `gate_digest_mismatch` — exactly the state SKILL.md:480-486 documents |
| round-3 replay after restoring the pinned gates | 0 | **7/7 rows reproduced**; restored bytes hash-matched all six manifest pins (`291c714` recipe, see C5) |
| `check-gate-battery.py` duty 1 (seven selftests, copied dirs) | pass 7/7 | originals hash-preserved (30/30) |
| `handoff-packet-check.py --selftest`, `naming-collision-gate.py --selftest`, `replay-frozen.py --selftest` | 0 / 0 / 0 | |

Environment positive: every tool is stdlib-only python3 (no PyYAML or other
third-party imports — `grep 'import yaml' tools/` → none); nothing to
install. No environment condition.

## B. Conditions — needs beyond the four files

### C1 — major: the battery row in SKILL.md is stale and its documented remedy now inverts the verdict

SKILL.md:501 states the battery's "committed default currently exits 2 with
`BASELINE-GATE-UNCOVERED` for myth and naming, whose pins live under
`reports/round-9/baselines/`; add that root via `--baselines-root` to reach
0". Measured today:

- Default `python3 tools/check-gate-battery.py` → **exit 0** (duty 1: 7/7;
  duty 2: 19 baseline rows across three roots — `tools/gates/expected`,
  `tools/gates/frozen`, **and already `reports/round-9/baselines`**).
- The documented remedy `--baselines-root reports/round-9/baselines/` →
  **exit 2**: the flag *replaces* the default roots
  (`tools/check-gate-battery.py:100` "``--baselines-root`` replaces the
  default baseline roots for one run"; `:1332`), uncovering the other four
  gates (`BASELINE-GATE-UNCOVERED`), i.e. following the row's instruction
  produces the failure the row says it cures.

**Condition:** a future executor needs the correction (default exit 0 is the
healthy state; do not apply the `--baselines-root` remedy to "reach 0") —
via a SKILL.md row fix or a dated erratum. Without it, an honest cold runner
following the four files misreads a healthy tree as broken (or a broken one
as healthy).

### C2 — major: the D4 gate's input artifact is never named, and the wrong choice yields a plausible false red

No line in the four files says which artifact `typed-pipeline-gate.py`
consumes. Measured:

- `typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → exit 0,
  **19/19 legs** (canonical green).
- `typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` → exit 1,
  **14/16 legs** with realistic-looking failures: `L2-channel` with eight
  `DERIV-REPLAY` FAILs (`NM-01`…`NM-08`, "rule 'CX-01' does not apply to
  stem …") and `L3-routing-consistency` with six `null` routing rows.

The typed artifact is the chain's *output*, not a gate input; feeding it
back produces a red that looks exactly like a genuine finding. **Condition:**
the executor needs the one-line convention (the gate grades the source
packet `packet.d4.yml`; `packet.d4.typed.yml` is the derived artifact) in
SKILL.md, or box-3 evidence risks recording a false break.

### C3 — major: the round-5/6/7 acceptance scripts exit 1 on the current tree, and SKILL.md's imperative wording implies they should pass

Measured (receipts in `.scratch/logs/runval-r{5,6,7}.log`):

- `reports/round-5/run-validation.py` → exit 1: its O leg embeds the
  round-3 frozen replay "expected 0, got 2 … gate_digest_mismatch" — the
  live-tree state SKILL.md itself documents as expected (:480-486), but the
  script's acceptance cannot pass on a live tree.
- `reports/round-6/run-validation.py` → exit 1: `"error": "entry prefix
  lost: corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md"` — the
  script pins round-6-era byte prefixes of corpus files
  (`reports/round-6/run-validation.py:242`,
  `require((ROOT / relative).read_bytes().startswith(pinned(BASE, relative)))`)
  and the corpus has legitimately grown since (appended errata), so the
  round-6 invariant is structurally unre-publishable on today's tree.
- `reports/round-7/run-validation.py` → exit 1: `failure[0]` "historical
  knowledge totals changed" (files 199 / raw_lines 717 …), `failure[1]`
  "wrong rejection for duplicate-parent-receipt-does-not-inflate: parent
  check identity collision", `failure[2]` cascade from the round-6
  acceptance (its embedded rerun errored on `"historical file changed:
  .gitignore"`).

SKILL.md:541-544 says "Re-run this round's receipt/count/preservation
checks with `python3 reports/round-6/run-validation.py`" and SKILL.md:587-590
"Run `python3 reports/round-7/run-validation.py` for the original F/O
thresholds" — imperative wording that sets a pass expectation. **Condition:**
the executor needs a dated erratum stating the expected live-tree results of
these three scripts (exit 1 each, with the reasons above) so historical
invariants are not misread as current breaks. Distinguishing context lives
in round-10 drift records, outside the four files.

### C4 — major: the round-5/6/7 scripts overwrite filed, tracked receipts in place, and the four files never say where they write

In the isolated export, running the three scripts rewrote
`reports/round-5/validation.json`, `reports/round-6/validation.json`,
`reports/round-7/validation.json` — all three are git-tracked filed
artifacts (`git ls-files` confirms), and each diverged from its `HEAD` bytes
after one run ("CHANGED by run", diff against `git show HEAD:`). Executed in
the real tree, an executor following SKILL.md's re-run wording silently
replaces filed historical receipts — the exact class the lane's round-23
conformance adjudication ruled out (filed bytes preserved; new results go to
new files). **Condition:** the executor needs the instruction (run these in
a disposable copy, or restore the receipts afterwards) plus the fact of the
write target; SKILL.md:517-519 says only "it writes its own validation
receipt". *Control:* this seat's runs were performed in
`.scratch/cold-run-4/tree/`, so the real receipts are untouched.

### C5 — minor: reproducing the round-3 restored-tree replay needs git history, and "isolated repo export" is never defined

The restore recipe pointer IS in-file (SKILL.md:482-484: restore the pinned
gates from `291c714`; details in `reports/round-10/drift/fix-18.md`), and it
works: restoring the six manifest-named gates from `291c714` hash-matched
all six pins (MATCH on 6/6), and the replay then reproduced **7/7 rows,
exit 0**. But the mechanics need (a) `.git` history in the working tree
(`git show 291c714:tools/gates/<gate>.py`) and (b) knowing that "isolated
repo export" (SKILL.md:470) must retain that history — a plain tree export
(the natural reading, and what this seat first built) cannot execute the
leg and has no in-file fallback. **Condition:** define "isolated repo
export" as a history-retaining copy (clone/worktree), or accept that this
diagnostic leg is out of scope for `.git`-less executors. Severity minor
because the live-tree expectation (exit 2, 7/7 mismatch) is already
documented in-file, so no false verdict arises — only an incomplete
reproduction.

### C6 — minor: per-gate input paths are not named; discovery is by directory listing only

The four files name no packet for the five culture-packet gates, no sample
for `handoff-packet-check`, and no corpus root for `provenance-audit`. All
were resolvable by plain `ls` (`examples/culture-d2/packet.d2.yml`,
`examples/culture-d3/packet.gates.yml`, `examples/culture-d3/handoff.md`,
`examples/handoff-packet.sample.md`, `corpus/knowledge/linguistics`), and
the resulting red verdicts are interpreted in-file (error-patterns table,
"Using the evidence"). No false-verdict risk found — friction only.

### C7 — minor: D3 replay step 2's "snapshot mode" clause has no executable referent

Step 2 (SKILL.md:575-579) says to run "the positive guard, independent
control selftest and frozen command" and that "Snapshot mode verifies every
listed input digest" — but no round-7 frozen manifest exists
(`tools/gates/frozen/` holds round-3, 4, 11, 18, 20, 22, 23 only), so the
snapshot clause cannot be executed as written. The nearest declared
executable is the gates-table's frozen option
(`check-evidence-coupling.py … --frozen examples/culture-d3/expected.json`),
measured exit 0. **Condition:** the executor must settle for the
`--frozen` option; wording should either name the intended manifest or drop
the snapshot clause for D3.

### C8 — minor: cosmetic fence damage in SKILL.md

Stray fence markers at SKILL.md:129 (a lone ````````), :154 and :217 (lone
` ``` `), and a leftover integration comment at :352
(`<!-- END R23-D SKILL SUBSECTION -->`). No execution impact on any leg;
renderers may mis-nest the fenced tables. Content staleness itself is the
D-seat audit's lane; recorded here only as executor-facing friction.

## C. Box-3 verdict input (decision stays operator-owned)

The SKILL.md executable checklist **executed end-to-end first-hand**: every
declared leg ran, the documented steady-state reds reproduced exactly, the
163/163 selftest, 19/19 D4 gate, 3/3 d4-repin replay, and 7/7 restored
round-3 replay all matched their in-file claims. Reading: **executable,
verified-with-conditions**, with the major conditions C1–C4 named for repair
or dated erratum before the box can be checked clean; minors C5–C8 are
friction, not verdict-changers.
