# R9-D07 — capability-row draft: reproducible D3 culture assembly

- round: 9 (loop 1 of 3, build 2 of 4) · date: 2026-10-17 · shard: R9-D07
- status: **DRAFT ONLY — the orchestrator admits.** This shard edits no other
  file: no `SCORECARD.md`, no `SKILL.md`, no `LOG.md`, no tools, examples,
  components, gates or packet. Everything below is proposed text plus
  read-only receipts.
- claim under draft: `reports/round-9/claims.json` claim **D**, capability
  `culture-d3-acceptance` — "python3 tools/assemble-culture-d3.py --check
  exits 0 with byte-identical deterministic assembly on the delivered tree;
  python3 tools/check-evidence-coupling.py --selftest green; D3 replays
  frozen without digest drift; the capability row for reproducible D3
  culture assembly enters SCORECARD only on demonstrated run (orchestrator
  admits)."
- upstream framing: `reports/round-9/targets.json` depth R9-D07;
  `SCORECARD.md:132-136` planned bullet — "D3 packet acceptance completion
  (the unadmitted round-7 O debt, without re-dispatching round 7)".
- read revision: `git rev-parse HEAD` → `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`
  ("round-9: declare claims F/O/D"). Sibling workers edit this tree
  concurrently; every command below was run read-only by this shard, and §6
  pins the sha256 of each cited file as read.

## 1. What the row asserts — and what it must not

The row records a **capability**, not canon: deterministic, byte-reproducible
assembly of the D3 source-bounded culture drill plus an executable
evidence-coupling guard, and a computational freeze that replays clean. It is
not lore acceptance, not real-language clearance, not cultural permission and
not a universal culture validator. The packet is `canon_status: NON-CANON`,
`handoff_status: prepared-not-accepted` (`examples/culture-d3/README.md:10-12`;
`reports/round-7/d3-contract.json` `evidence.canon_status` /
`evidence.handoff_status`). The legacy naming `CROSS-HOLD` and costume `R-01`
holds are **retained, not cleared** — a green capability row must not read as
an all-gates-green claim.

## 2. LANDING-READY — SCORECARD "Capabilities" table row

Admission form (copy verbatim). **Gate condition:** the clause
*"freeze … re-pinned … replayed with no drift"* must hold at admission time;
at draft time the frozen run is red for a diagnosed, sibling-owned reason
(§5.2/§5.3) and the resolution is R9-D01/R9-D04 work. Do not land the row
while that run is red — `reports/round-9/claims.json` requires demonstrated
run, and landing a weakened row would shrink the claimed acceptance.

```markdown
| reproducible D3 culture assembly | Deterministic four-component NON-CANON drill (2 fictional eras, 20 constructed lexemes, 6 derived names, 7 utterances, 2 attributed beliefs, 4 costumes with C03's declared RR1 violation kept visible) assembles byte-identical (`--check` exit 0); stdlib evidence-coupling guard green on the committed packet (exit 0, `findings: []`) and selftest (positives 5/5, domain 16/16 across all 14 non-DATA diagnostics, malformed 4/4, frozen controls 5/5); parent-owned computational freeze of 24 input digests re-pinned after round-8 gate repairs and replayed with no drift; legacy naming CROSS-HOLD×2 + NAME-NEAR and costume R-01 holds retained, never cleared | `python3 tools/assemble-culture-d3.py --check`; `python3 tools/check-evidence-coupling.py --selftest`; `python3 reports/round-9/run-validation.py` | round 9 (declared round 7; round-7 acceptance runner exited false — `reports/round-7/validation.json`) |
```

Notes for the orchestrator on this row:

- "first working / round 9" matches the claims.json before-state: the
  round-7 O claim declared the D3 profile but its acceptance runner recorded
  `acceptance_checks_passed: false` (F-side harness error; the D3-side
  measurements in the same file were green — `reports/round-7/validation.json`
  `claims.O.measurement`).
- The parenthetical "(declared round 7; …)" mirrors the D2 row's
  "round 3; selftest supplement-opencode-1" pattern (`SCORECARD.md:46`).
- If the orchestrator prefers the round-8 addendum style, the same row can
  land under "Capabilities addendum (round 9)"; the columns are identical.

## 3. LANDING-READY — round-9 axes table row (depth)

```markdown
| depth | improved (claim D, capability `culture-d3-acceptance`) | Round-7 D3 acceptance never completed (`reports/round-7/validation.json` acceptance false; F-side harness collision) although D3's own measurements were green → on the round-9 tree: `--check` byte-identical exit 0; assembler selftest 85/85; guard selftest green (positives 5/5, domain 16/16, malformed 4/4, frozen 5/5); guard positive run exit 0/`findings: []`; input freeze re-pinned after round-8 input changes and replay clean; no SKILL.md change needed (round-7 D3 gate table + replay checklist already present and accurate) | `python3 reports/round-9/run-validation.py`; `python3 tools/assemble-culture-d3.py --check`; `python3 tools/check-evidence-coupling.py --selftest` | `reports/round-9/d3/*`, `reports/round-9/validation.json` claims.D |
```

The "freeze re-pinned … replay clean" clause carries the same gate condition
as §2. The frozen-control sub-counts (tampered-digest / unknown-entry /
bool-expected×2 → exit 2 `D3-SNAPSHOT`) come from the guard selftest, which
passed at draft time; the *committed-packet* frozen run is the red surface.

## 4. SKILL.md position — no change this round

Recommendation: **no `SKILL.md` edit is required for this admission.**
Round 7 already landed the D3 surface:

- the two D3 gate rows (assembly drift, evidence coupling) with entry
  commands, verdict maps, selftests and pinned-value cells
  (`SKILL.md:239` heading, rows `:250-251`);
- the earlier eight-row condition/decision table and the five-step "D3
  replay checklist" (`SKILL.md:253-262` and `:264-284`).

Nothing in that text asserts or denies admission, so admitting the capability
leaves it accurate. This shard performed a read-only check that no stale
admission marker exists:

```sh
grep -n "unadmitted\|not admitted\|unclaimed" SKILL.md
# (exit 1: no output — SKILL.md carries no admission-status text for D3)
```

If the orchestrator nonetheless wants a SKILL touch, the minimal honest
addition is none; a status line belongs in `SCORECARD.md`, which owns
admission verdicts.

## 5. Live receipts (commands, outputs, date)

All commands run **2026-10-17** by this shard from
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`, read-only, at HEAD
`a7bb205`. Times are local (-03), matching `stat` output.

### 5.1 Green surfaces

| # | command | exit | observed |
|---|---|---:|---|
| 1 | `python3 tools/assemble-culture-d3.py --check` | 0 | `packet.json: byte-identical deterministic assembly; packet.gates.yml: byte-identical deterministic assembly` |
| 2 | `python3 tools/assemble-culture-d3.py --selftest` | 0 | `selftest: 85/85 checks passed` — fixture CLI assemble/`--check`/determinism/tamper plus fail-closed missing/invalid-JSON/invalid-UTF8/wrong-root/unexpected-key/missing-key/collision/wrong-type/below-minimum/serializer-absent controls; real naming gate (CROSS-HOLD, no PHON/DERIV FAIL) and real costume gate (R-01 note, no R-02) run read-only |
| 3 | `python3 tools/check-evidence-coupling.py --selftest` | 0 | JSON `selftest_passed: true`; positives 5/5 (repo-cwd, foreign-cwd, translated-costume-label / ordinary-utterance-place / belief-proposition-reword stay clean); domain 16/16 (all 14 non-DATA diagnostics); malformed 4/4; frozen 5/5 (good exit 0; tampered-digest, unknown-manifest-entry, bool-expected ×2 → exit 2 `D3-SNAPSHOT`) |
| 4 | `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` | 0 | `{"counts":{"total":0},"exit":0,"findings":[],"profile":"kotodama-d3-evidence-coupling/1"}` |
| 5 | `python3 tools/assemble-d2.py --check` (interop touch) | 0 | `packet.d2.yml: byte-identical deterministic assembly` — this shard's read-only runs did not disturb the round-8 D2 baseline (full interop verdict is R9-D06's) |

### 5.2 The one red surface — committed freeze drift (measured, not hidden)

| # | command | exit | observed |
|---|---|---:|---|
| 6 | `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` | **2** | exactly 3 findings, all `D3-SNAPSHOT` "manifest digest mismatch" |

The three drifted pins (declared vs actual, full sha256):

```text
corpus/knowledge/synthesis/worldbible-integration-contract.md
  declared 50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1
  actual   5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069
tools/gates/costume-era-consistency-gate.py
  declared 29a9361c7b96a354c41a3994e3459a951ce0a43425b3984d6506b3e5b3a43f03
  actual   e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f
tools/gates/naming-collision-gate.py
  declared 8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526
  actual   d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
```

Independent recomputation of all 24 pinned digests (inline
`json`+`hashlib` loop over `expected.json["manifest"]`, command in §6.1):
**21 match / 3 mismatch of 24** — the three above and nothing else.

Cause chain (diagnostic material for R9-D01/R9-D04; this shard does not
prescribe the fix):

- `examples/culture-d3/expected.json` mtime `2026-10-17 16:36:50 -03`.
- The three drifted inputs were last changed in round-8 commit
  `e1694bad6ac96aca45a11ca5746582b275929355` (`2026-10-17T17:44:17-03:00`,
  "round-8: admit F/O/D — freshness receipts, harness+gate repairs,
  d2-typed-labels"); `git show --stat` on that commit: contract `+3`,
  costume gate `+73`, naming gate `+236`.
- The round-7 freeze therefore predates legitimate round-8 **input-side**
  repairs. The D3 tools themselves did **not** drift: the sha256 of
  `tools/assemble-culture-d3.py` and `tools/check-evidence-coupling.py`
  measured at draft time equal the round-7 README pins (§6.2), and the
  guard's `--check`/positive/selftest surfaces are green (receipts 1–4).
- `examples/culture-d3/README.md` (Reproduce section) states the governing
  rule: "refresh the computational freeze (expected.json) only after that
  re-verification — later input edits invalidate the existing snapshot
  before any verdict." A re-pin without a re-verification receipt would be
  the circularity D09/D10 are chartered to catch; the guard is unchanged and
  its packet verdict is exit 0/`findings: []` (receipt 4), so the
  re-verification material exists — the D04 owner decides how to record it.

Draft-time consequence: acceptance surface 3 of claim D ("D3 replays frozen
without digest drift") is **not yet satisfied**, and the §2/§3 rows must not
land until R9-D01 (diagnosis) and R9-D04 (replay) close it.

### 5.3 Legacy surfaces (expected holds, fresh run)

| command | exit | observed |
|---|---:|---|
| `python3 tools/gates/naming-collision-gate.py examples/culture-d3/packet.gates.yml` | 1 | exactly CROSS-HOLD ×2 (unresolved real-language sweep; no priority language/community named) + one NAME-NEAR REVIEW (`E0` vs `E1`, recall-oriented); no phonology FAIL, no derivation FAIL |
| `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d3/packet.gates.yml` | 1 | exactly one finding: `R-01 [note]` C03 declared RR1 violation kept visible; no R-02 |
| `python3 tools/gates/handoff-packet-check.py examples/culture-d3/handoff.md` | 0 | `fields=16/16 glossary-entries=20 findings=0` |

These exits 1 are the contract's expected outcomes
(`reports/round-7/d3-contract.json` `legacy_projection`: CROSS-HOLD expected,
not cleared; C03's R-01 retained), not failures of the capability.

## 6. Pinned state at draft time

### 6.1 The digest-recompute command (re-runnable by the orchestrator)

```sh
python3 - <<'EOF'
import json, hashlib, pathlib
d = json.load(open('examples/culture-d3/expected.json'))
inputs = d['manifest']
ok = bad = 0
for path, digest in sorted(inputs.items()):
    a = hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
    if a == digest: ok += 1
    else:
        bad += 1
        print(f'DRIFT {path}\n  declared {digest}\n  actual   {a}')
print(f'match={ok} mismatch={bad} total={ok+bad}')
EOF
# 2026-10-17 output: match=21 mismatch=3 total=24 (the three rows in §5.2)
```

### 6.2 sha256 of cited files as read (2026-10-17)

| file | sha256 | vs round-7 README pin |
|---|---|---|
| `examples/culture-d3/expected.json` | `74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080` | matches (freeze itself unchanged; its inputs drifted) |
| `examples/culture-d3/packet.json` | `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829` | matches |
| `examples/culture-d3/packet.gates.yml` | `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425` | matches |
| `tools/assemble-culture-d3.py` | `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014` | matches |
| `tools/check-evidence-coupling.py` | `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` | matches |
| `examples/culture-d3/handoff.md` | `0d8d660bf9797d1c15da477f96ded75553a8d2ca7f04f75aa86a8a65e28fd2fc` | documentation surface, outside the computational freeze |
| `examples/culture-d3/README.md` | `d0f62ad7472ef04176130ad4b9e732cf8ae1b61db9efa6da787dac19a3929aa4` | documentation surface, outside the computational freeze |

Dependency state: at this shard's start `reports/round-9/d3/` did **not**
exist and `reports/round-9/run-validation.py` did **not** exist (`ls`
receipts, 2026-10-17 ~20:49Z). Siblings landed during the run and were
read-cross-checked before seal: **R9-D01** `check-diagnosis.md` measured the
same 21/24-match manifest and the same three drifts, ruled them legitimate
and verdict-preserving round-8 input changes, and flagged the re-pin as a
cross-shard/orchestrator act, not absorbed; **R9-D02** `determinism.md`
reproduced the same packet/projection pins by double regeneration plus a
13-probe matrix; **R9-D03** `evidence-coupling.md` and **R9-D06**
`interop.md` agree with §5.1/§6.2; **R9-D08** `docs.md` records the docs
leg. Still in flight at seal: R9-D04 (frozen replay resolution), R9-D05,
D11, D12, and `reports/round-9/run-validation.py`. When R9-D04 lands, the
orchestrator should substitute its actual replay receipt in §2/§3.

## 7. Admission checklist (for the orchestrator)

1. **Freeze surface green (the only currently blocked requirement).**
   R9-D04's replay receipt shows no digest drift, or the accepted resolution
   recorded with its re-verification evidence. Until then, do not land §2/§3.
2. **Runner green.** `python3 reports/round-9/run-validation.py` exists,
   exits 0, and its `validation.json` carries `claims.D` passing; R9-D12's
   ledger fragment agrees.
3. **Row text.** Copy §2 verbatim into `SCORECARD.md` (or the round-9
   addendum table), and §3 into the round-9 axes table. Set "first working"
   in the same admission commit; do not back-date it.
4. **No weakening.** If any D3 acceptance surface stays red, admission does
   not happen this round: `reports/round-9/claims.json` D says the row enters
   SCORECARD "only on demonstrated run". A row without the freeze clause
   would misstate the claim.
5. **SKILL.md:** no edit required (§4). LOG entry is the orchestrator's, per
   `AGENTS.md`.

## 8. Limits

- This shard ran read-only commands only; it did not regenerate any packet,
  freeze, projection or gate output, and wrote exactly this one file.
- The row describes measured behavior at the digests in §6.2 and nothing
  more: not canon, not lore acceptance, not real-language clearance, not
  cultural permission, not arbitrary malformed-schema safety. The guard is
  bounded to the D3 profile it names.
- The frozen replay at draft time is red (§5.2); this draft reports that
  rather than hiding it, and the red state is the exact debt the claim's
  third acceptance clause names.
- Green selftests prove the committed control sets pass; they do not certify
  D3 content beyond the declared bounded profile.
