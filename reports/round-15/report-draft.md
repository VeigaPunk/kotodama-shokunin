# kotodama — round 15 fleet report (DRAFT BODY — integrator finalizes)

**Scribe X04; evidence cutoff 2026-10-18T00:50Z.** This lane-local report is
an integration draft, not an acceptance receipt, an admission, or independent
promotion verification. Round 15 did **not** settle inside this seat's bounded
dependency window (15 minutes, 60-second polls, from 2026-10-18T00:27:06Z to
00:42:15Z): the handoff packet, its builder, the frozen baseline and both audit
receipts were still absent at the deadline. Everything below is attributed to
its dated, hash-bound receipt; in-flight observations are labeled as such. The
integrator supplies the settled tree, the primary receipt, LOG/SCORECARD
landing and the authorized final filing; no round-15 O/D admission is asserted
by this draft.

## Declaration and scope

Axes: **O / operability**, **D / depth**. Declaration:
`reports/round-15/claims.json`; allocation: `reports/round-15/targets.json`
(O: 10 seats across design/impl/packet/frozen/audit/review; D: 2; X: 4).
Declared baseline: `b02cfbc9468aa906f0ff8301ec643770fb2bcfd8` (the round-14
admit). Declaration revision: `c60b17c21a77182a5c1f0251e98b4ea42e563c3e`,
"round-15: declare GLM-1 claims O/D (handoff v2, uncertainty knowledge)",
observed with `git rev-parse HEAD` at 2026-10-18T00:42:13Z. These are
different metadata fields; the declaration revision must not be relabeled the
baseline.

The requested route is `zai-coding-plan/glm-5.3-flash-low` (host-pinned MAX
thinking effort), 16 workers — operator regimen loop 1, GLM round 1 of 2
(`claims.json`, 2026-10-17). That is a request, not proof of wire-model
identity, concurrency, or completion counts; no dispatch trace was available
to this seat.

This round exists because the round-12 adjacency audit **REJECT**ed the
round-11 handoff packet on semantics, not shape: the claim ledger "has no
explicit per-claim `uncertainty` dimension, and no claim-to-record/edge
relation key", and D2 coupling appeared "as one aggregate dependency edge"
(`reports/round-12/adjacency/contract.md:27-28`; verdict at
`reports/round-12/adjacency/A11-A12-handoff.md:9-15`). The shape gate had read
`fields=16/16 glossary-entries=20 findings=0` in the same audit — shape-clean
and semantic-REJECT coexist in one filed artifact
(`contract.md:9-10`). Round 13 was operator-skipped and handoff-v2 was deferred
to these GLM rounds (`SCORECARD.md:262-263`).

Only `reports/round-15/report-draft.md` and `reports/round-15/rerun.json` are
this scribe's outputs. No historical validator was invoked, no filed round-8..14
artifact was edited by this seat, and no commit or push was performed.
`PROVINCE.md` and lore's canon/acknowledgment authority remain in force; all
artifacts are NON-CANON and no real-world rights ruling is made or assumed.

## Claims — required result versus observed evidence

| claim | required result (unchanged) | assessment at this cutoff |
|---|---|---|
| O / operability | `handoff/packet-v2.yml` with per-claim `uncertainty {status, basis}` (zero boilerplate) and claim-to-record links resolving to real repo records; shape gate still 16/16 + 20/20; round-12 contract audit re-run over v2 = semantic PASS or named gaps with owner notes; durable builder with `--selftest` and a frozen `expected.json` baseline. | **Design and semantic checkers landed; the packet chain did not.** `v2-design.md` (spec + measured gate probes) and two deterministic checker modules are on disk; `packet-v2.yml`, the builder, `expected.json`, the uncertainty-audit receipt and the contract-audit re-run were missing at the deadline (`reports/round-15/rerun.json` → `dependency_wait.missing_at_deadline`). |
| D / depth | SKILL.md gains a label-uncertainty decision table (worker-drafted, orchestrator-landed), cross-referenced to the verification partition, every rule cited. | **Draft complete and runner-verified at draft level; landing pending.** The draft exists with 5 tables / 17 rule rows, all 17 cited, all three statuses covered, partition crossref present (runner D measurement, revision `f16b2637`, 00:43Z). SKILL.md was byte-unchanged through the window — landing is orchestrator work. |

Declared counting command: `python3 reports/round-15/run-validation.py`. It
has been run by this seat in `--selftest` and `--check` modes only; the
receipt-writing default mode is the parent's, and no settled round-15
validator result is asserted here.

## Operability — what landed, what did not

### Landed: the design receipt and the semantic checkers

`reports/round-15/handoff/v2-design.md` (R15-O01) is the O-design receipt: it
fixes the `{status: supported|partial|unresolved, basis}` carrier with a
mandatory basis grammar (`grounding:` / `restriction:` / `open:` + `owner:`),
the claim-to-record link grammar (`artifact_id#selector`, JSON key paths,
line anchors, tokens), the per-edge `claim` column that dissolves the D2
aggregate row, the v2 field-by-field delta (MAJOR version bump under contract
§9), the builder contract with stable `V2-*` codes and a ten-control selftest
matrix, and the expected re-audit verdict with the three owner-noted
remainders (bilateral acknowledgment; round-8 L0 digest question; missing
kotodama-side §1 read record) (§2–§7). Its gate probes are measured, not
argued: a placeholder basis cell (`unknown`) and an off-vocabulary status
token (`tentative`) both exit 0 through the shape gate — the measured
justification for builder-side semantic checks (§8, probes D/E); a canon-verb
basis cell correctly trips `HO-CANON-CLAIM` (probe C1).

Two deterministic checker modules landed under `tools/harness/`:

- `packet_links.py` — resolves `path`, `path#token`, `path:LINE` links,
  rejects repo escapes and aggregate edge targets (`E-TARGET-UNKNOWN`).
  `--selftest` → exit 0, "17 checks passed (path/token/line specs, symlink
  escape, record index, aggregate rejection)" at 00:36Z (revision `b8fee76b…`)
  and again at 00:44Z (revision `3fa03b2e…`).
- `packet_uncertainty.py` — validates per-claim
  `uncertainty: {status ∈ supported|partial|unresolved, basis}`, rejects
  boilerplate/short/duplicate bases, deterministic `U-*` findings. Its
  selftest was **red on every revision observed**: raw `ValueError` crash on
  `2e9dd1a5…` (~00:35Z), three named control failures after the owner's first
  fix (~00:38Z), and `FAIL negative fixture X14: expected ['U-BASIS-SHORT',
  'U-BASIS-RESTATES'], got ['U-BASIS-SHORT', 'U-BASIS-RESTATES',
  'U-BASIS-NO-GROUNDING']` on `a000cb3d…` at 00:44Z. Owner-active module; the
  red state is a named gap for the parent, recorded with commands and dates in
  `reports/round-15/rerun.json` → `preliminary_observations`.

### Missing at the deadline: the packet chain

`reports/round-15/handoff/` contained only `v2-design.md` through 00:42:15Z:
no `packet-v2.yml`, no builder (design names `tools/build-handoff-v2.py`,
§6), no `expected.json`, no uncertainty-audit receipt, no contract-audit
re-run artifact. The runner therefore cannot measure claims end-to-end yet.

### Independent runs on the in-flight runner

`reports/round-15/run-validation.py` was revised by its owner at least five
times during the window. Progression, each hash-bound in `rerun.json`:
`422f1dd5…` selftest 26 controls exit 0 (00:36Z) → `d4761425…` 30/30 (00:38Z)
→ `11ec4aef…` selftest crash `KeyError: 'links'` at `run-validation.py:1187`
(00:42:13Z) → `f16b2637…` selftest **37/37 exit 0** and `--check` executing
cleanly (00:43-44Z). On `f16b2637…`, `--check` (no receipt written) returns
exit 1 with claim **D passed** and claim O failing on exactly the four missing
integration artifacts quoted in `rerun.json` → `final_available_runner_runs`
(packet, audit receipt, gate run, builder). That is the honest blocked state —
not a defect of landed evidence, and not an acceptance.

### Regression battery and preservation (the no-axis-harm control)

`python3 .scratch/x04-battery.py`, 2026-10-18T00:42:13-20Z, `TMPDIR=
$PWD/.scratch`, `REFRESH_RECEIPTS` unset: all **13** round-14 regression
commands exit 0 (battery/craft/D2/D3 typed pipeline; per-command stdout
hashes retained in `rerun.json`). An 836-file snapshot over
`reports/round-8..14`, `tools/`, `corpus/knowledge/{synthesis,verification}`,
SKILL/SCORECARD/LOG/PROVINCE and the round-15 declarations is **identical
before and after** (manifest `9fef109f…` both sides); the five filed receipts
`reports/round-8..12/validation.json` are byte-unchanged and match round-14's
filed initial-receipt control; `git diff --check` exit 0; no tracked file
modified or staged.

One measurement honesty note: the default battery's stdout is **not
byte-stable run-to-run** — three consecutive runs at ~00:47Z produced three
different stdout hashes, all exit 0, with no baseline-root file changed
(`rerun.json` → `battery_stdout_stability_probe`). Single-run stdout hashes
for this command are per-run records, not reproducibility pins. No fix was
attempted (outside write scope); any future freshness measurement that
re-includes this command inherits exactly the threshold question round 11
failed (`SCORECARD.md:199-220`), and freshness axis-move claims remain paused
by operator ruling.

## Depth — the uncertainty decision table, drafted not landed

`reports/round-15/knowledge/uncertainty-table-draft.md` (R15-D01) follows the
R8 worker-draft / orchestrator-lands pattern and contains: the three-status
table with necessary conditions, required basis forms and forbidden moves
(§3), the claim-to-record link rule ("a dead pointer is a defect of the same
class as an absent basis", §3), per-claim-kind basis requirements
cross-referenced to contract §6 (§4), eleven anti-patterns each with its
control (§5), a LANDING-READY block for SKILL.md (§6), lane-local boundaries
(§7), and sha256-pinned read-set bytes (§8). Its vocabulary is taken from the
round declaration (`reports/round-15/claims.json:14`) and the lane's triage
protocol; it flags the not-yet-landed packet as an explicit `to-verify`
against the O worker rather than assuming the v2 shape (§8, open dependency).

Independent measurement through the round-15 runner on `f16b2637…`
(00:43Z): 5 tables, 17 rule rows, **17/17 cited** to corpus paths or
round-12/15 artifacts, statuses `supported|partial|unresolved` all covered,
verification-partition crossref present, draft dated. Claim D passes at draft
level. The declared D after-state — the table inside `SKILL.md` — had **not**
happened: SKILL.md is byte-unchanged through the window, and landing it is
explicitly the orchestrator's move (draft §6).

## Other axes, boundaries, and scope

No coverage or freshness claim is declared in round 15. No canon assignment,
lore acceptance, cultural clearance or real-world rights ruling is claimed by
any artifact this report cites; the packet design keeps bilateral
acknowledgment and the round-8 L0 digest question (`50c4c2f2…` premise stale
vs the operational `5f4c02bf…`) as owner-noted open questions, blocking first
transfer only (`v2-design.md` §7) — the same items the round-12 audit left
open (`contract.md:20,40-42`). The contract digest re-measured by this seat
on 2026-10-17 matches the operational pin:
`5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`
(`sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md`).

`reports/round-15/scope.md` (SCRIBE X02) records: fleet root **dirty with one
pre-dispatch stray** (`baseline-analyze.txt`, a 105-byte stderr capture;
owner note filed, left in place — this seat has no fleet-root cleanup
authority); filed rounds 8–14 untouched (three dated controls, all zero); and
PROVINCE.md accurate with no round-15 edit indicated. Both are that seat's
attributed observations, not independent checks re-performed by this scribe.

An untracked `corpus/lessons/round-15.md` appeared during the window (another
seat's fragment); it is outside this seat's write scope and was not inspected
beyond its git-status line.

## Evidence commands (all 2026-10-18 UTC, in-lane, `TMPDIR=$PWD/.scratch`)

```sh
# dependency watch (read-only; duplicate-watcher disclosure in rerun.json)
python3 .scratch/x04-watch.py            # 60s polls, 00:27:06Z–00:42:15Z
# runner runs (no receipt written)
python3 reports/round-15/run-validation.py --selftest
python3 reports/round-15/run-validation.py --check
# semantic checkers
python3 tools/harness/packet_uncertainty.py --selftest   # RED, see rerun.json
python3 tools/harness/packet_links.py --selftest         # 17/17
# regression + preservation battery (13 children + before/after manifests)
python3 .scratch/x04-battery.py
# battery stdout determinism probe (3 runs, 3 hashes, all exit 0)
for i in 1 2 3; do python3 tools/check-gate-battery.py | sha256sum; done
# contract digest re-measure (2026-10-17)
sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md
```

Scratch payloads: `.scratch/x04-rerun-measurements.json` (full battery),
`.scratch/x04-r15-check-full.out` (check receipt content),
`.scratch/x04-dependency-watch.jsonl` (poll series). Scratch is gitignored and
not a deliverable.

## Integrator closeout dependencies

1. Land the O-chain in the design's declared order (`v2-design.md` §9):
   `packet-v2.yml` → builder with `--selftest` → frozen `expected.json` only
   after packet bytes stop moving → uncertainty-audit receipt → contract-audit
   re-run over v2. Do not relabel the two content findings closed before the
   re-audit artifact exists.
2. Resolve the `packet_uncertainty.py` selftest red (X14, `a000cb3d…`) before
   the runner consumes it; keep the earlier red observations on record rather
   than rewriting them.
3. Land the D table into SKILL.md from the draft's §6 block, then re-run the
   D measurement so the landed bytes (not the draft) carry the verdict.
4. After integration settles: run
   `python3 reports/round-15/run-validation.py` through its authorized owner
   to publish the primary receipt, then obtain the independent post-settle
   rerun this record could not perform; decide axis verdicts only then.
5. Preserve rounds 8–14 byte-for-byte (append-only corrections land as new
   records); do not run historical validators in the live tree and do not use
   `REFRESH_RECEIPTS` to bypass the guard.
6. Supply the dispatch/availability evidence for the 16-worker zai batch —
   the request in `claims.json` is not a trace — and reconcile the
   battery-stdout instability observation into any future freshness threshold
   decision before un-pausing that axis.

No `[x]` promotion marker is awarded by this author. The named promotion-gate
process of `SHONEN.md` requires a non-author verifier; nothing here claims
loop-1 completion, handoff acceptance, or lore receipt.
