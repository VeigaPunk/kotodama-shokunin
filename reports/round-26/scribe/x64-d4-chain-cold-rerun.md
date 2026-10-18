# Round 26 — SCRIBE X64 — independent cold re-run of the D4 chain post-register

- **Seat:** SCRIBE X64, round 26. Claim **D / depth** (register stratum in D4), cold re-run leg; supporting evidence for **O / operability**.
- **Assignment (verbatim):** "SCRIBE X64: independent cold re-run of the D4 chain post-register."
- **Date:** 2026-10-18. Commands run with `python3` 3.14.7; `export TMPDIR=$PWD/.scratch` before every scratch-writing command; scratch under `.scratch/x64/` (gitignored).
- **Baseline binding:** declared baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b` (`reports/round-26/claims.json:5`); lane HEAD at the cold run `1ad491a1a4b0aef9ebdc1861dfb8237727503825`.
- **Write scope:** this fragment only, plus `.scratch/x64/`. No tool, packet, pin, validator or shared-bookkeeping edit; no Git mutation, commit or push; no filed round-8–25 byte written. This seat authored none of the artifacts it re-runs.
- **Method:** every execution happens inside an isolated `git clone --shared` of the lane under `.scratch/x64/`, never in the lane worktree, so a re-run cannot move the tree it measures.

## 0. Headline

The D4 chain is **operationally green and byte-deterministic** at the revision measured, and it **fails closed** on all 12 negative controls this seat authored.

**The register stratum had not landed at this seat's close.** The pre-register state is recorded in full below so the D-seat's post-register re-run has a baseline to compare against; §4 states the delta the parent must re-measure once the forms land.

## 1. The chain as re-run

The D4 chain is the three build products plus their graders:

```
examples/culture-d4/components/*.yml  (12 inputs)
  -> tools/assemble-culture-d4.py      -> packet.d4.yml
  -> tools/d2-typed-labels.py          -> typed-labels.d4.yml      (projection)
  -> tools/assemble-d4-typed.py        -> packet.d4.typed.yml      (adapter)
  -> tools/gates/typed-pipeline-gate.py   (L1..L4 + L3b-argot)
  -> tools/gates/d4-typed-labels-check-gate.py
  -> tools/gates/argot-derivation-gate.py (sibling, invoked by the typed gate)
```

## 1b. The register stratum's design probes, re-executed cold

The D-seat landed `reports/round-26/register/{design,forms,rules}.md` during this seat's window — **design only**. The packet is unchanged: no `registers:` block, `derived_pairs=0`. What *can* be re-executed cold is the design's own probe set, which is where its numbers live. This seat rebuilt each probe independently from the delivered packet plus the design's own record rows, and reproduced the published numbers exactly:

| probe | what it is | published | this seat, cold | agree |
|---|---|---|---|---|
| `probe.yml` | delivered packet + the 8 register rows, `lengthen` undeclared | `derived_pairs=8 rule_holds=6`, exit 1 | `derived_pairs=8 rule_holds=6`, exit 1 | **yes** |
| `probe-rule2.yml` | same + the `LENGTHEN` pattern/output rule declared | `rule_holds=0`, exit 0 | `rule_holds=0`, exit 0 | **yes** |
| `probe-rule2-bad.yml` | `RF-06` mutated so the chain no longer yields it | `violations=1`, `D4L-ARGOT-DERIV` | `violations=1`, `D4L-ARGOT-DERIV` | **yes** |
| `probe-rule2-nopair.yml` | rule declared with no `pattern`/`output` | `D4L-ARGOT-RULE` HOLD | `rule_holds=6`, exit 1 | **yes** |
| `probe-bad.yml` | `RF-02` `kit`→`kat` | `D4L-ARGOT-DERIV` fires | `violations=1` | **yes** |
| `ctrl-early-era.yml` | a `stamp` form dated E0 | design says **no finding** (era unimplemented) | exit 1, `violations=0` — no era finding | **yes** |

**X64-F4 (design/measurement hazard, found cold).** The gate resolves a declared derivation operation against the packet's rule **ids by exact string** (`argot-derivation-gate.py:506` `if op in rules`, with `packet_rules` keying on the raw `id` at `:373` — no case-folding, unlike the layer index at `:259`). The design ships the rule as `id: LENGTHEN` and the records as `derivation: {op: LENGTHEN, …}`, so it is self-consistent and its probes reproduce. But the same design's prose (`rules.md:41-42`) states the operation as lowercase `lengthen`, and a consumer who follows the prose writes `op: lengthen` against `id: LENGTHEN` — measured: `rule_holds=6`, exit 1, six spurious HOLDs on **correct** derivations. The rule-id match is case-sensitive while the sibling layer-register match is not. The landing seat must keep the two spellings identical; a future round could case-fold the rule lookup to remove the trap.

## 2. Pre-register cold run — every step, with exit and legs

| command | exit | legs | tool sha256 (16) |
|---|---:|---:|---|
| `python3 tools/assemble-culture-d4.py --check` | 0 | — | 943f487ba991d45d |
| `python3 tools/assemble-culture-d4.py --selftest` | 0 | — | 943f487ba991d45d |
| `python3 tools/d2-typed-labels.py --selftest` | 0 | 163/163 | 2819f68769dfc0b5 |
| `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | 0 | — | 2819f68769dfc0b5 |
| `python3 tools/assemble-d4-typed.py --selftest` | 0 | 12/12 | 92f5460bcc34ffbb |
| `python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml` | 0 | — | 92f5460bcc34ffbb |
| `python3 tools/gates/typed-pipeline-gate.py --selftest` | 0 | 19/19 | b749ad07cf171027 |
| `python3 tools/gates/typed-pipeline-gate.py --selftest-generalized` | 0 | 16/16 | b749ad07cf171027 |
| `python3 tools/gates/typed-pipeline-gate.py` | 0 | 16/16 | b749ad07cf171027 |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | 20/20 | b749ad07cf171027 |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | 0 | 17/17 | b749ad07cf171027 |
| `python3 tools/gates/d4-typed-labels-check-gate.py` | 0 | — | 05f99629d870280c |
| `python3 tools/gates/d4-typed-labels-check-gate.py --selftest` | 0 | 163/163 | 05f99629d870280c |
| `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | 0 | — | df1a364b3970365c |
| `python3 tools/gates/argot-derivation-gate.py --selftest` | 0 | — | 5b5abe7865ed906c |
| `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | 0 | — | 5b5abe7865ed906c |
| `python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` | 1 | — | d9e4e8f4f93a21b3 |
| `python3 tools/gates/phonology-sanity-gate.py examples/culture-d4/packet.d4.yml` | 1 | — | d5fe087ffb2342e5 |
| `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d4/packet.d4.yml` | 0 | — | e6bffd7020c0b116 |
| `python3 tools/gates/lexicon-coverage-audit.py examples/culture-d4/packet.d4.yml` | 0 | — | 2c4dd39702a15ea3 |
| `python3 tools/gates/myth-consistency-gate.py examples/culture-d4/packet.d4.yml` | 0 | — | 5368b13542cd4b8a |
| `python3 tools/gates/provenance-audit.py examples/culture-d4/packet.d4.yml` | 2 | — | 8a96aaf4ccd14ef4 |

**Pins measured at this revision** (`sha256`, full digests):

| path | sha256 |
|---|---|
| `examples/culture-d4/components/01-brief.yml` | `a2bc3111b8e936d2aa78feca86b871996455cc98d7d639f3825a88df8a1c056f` |
| `examples/culture-d4/components/04-lexicon.yml` | `74c2561b7c875c7c98708c589002b85b7989fc64bafa6abf794210401c69a9a5` |
| `examples/culture-d4/expected-holds.json` | `3826ba68d705b3c379b2a12737c14075d9095a1ba2aa2eb525de1851a9ecd2f7` |
| `examples/culture-d4/packet.d4.typed.yml` | `ffece0feb52c5b0b8ae6b0f8c1848d6220ad2dc2b36b1faac6385d62f4bfd84e` |
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` |
| `examples/culture-d4/typed-labels.d4.yml` | `60b526b0b3d07141875d20c472451cdf6658f61936d39fe18af4f3d981981092` |
| `tools/assemble-culture-d4.py` | `943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2` |
| `tools/assemble-d4-typed.py` | `92f5460bcc34ffbb43a771504d213d23aafd818b39c7017c823a363e99063fd0` |
| `tools/d2-typed-labels.py` | `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` |
| `tools/gates/argot-derivation-gate.py` | `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211` |
| `tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` |
| `tools/gates/typed-pipelines.json` | `396f4678133ad3223752c27d7153fdff06945abfa49137a307e10ef6e29b44d0` |

**Determinism and no-write (control for the table above).** Two fresh copies produced byte-identical products: assembler `True`, projector `True`, adapter `True`. Regeneration matched the committed bytes for all three artefacts: `{'examples/culture-d4/packet.d4.typed.yml': True, 'examples/culture-d4/packet.d4.yml': True, 'examples/culture-d4/typed-labels.d4.yml': True}`. The five read-only entries (`--check` ×3, gate ×2) left every artefact byte-identical: `unchanged=True`, changed=`[]`.

## 3. Negative controls — the chain's teeth

A green run proves nothing unless the chain can also say no. Each control mutates exactly one input inside its own clone copy and records whether the chain refuses.

| # | control | mutation | command | exit | expected | bites |
|---|---|---|---|---:|---|---|
| 1 | `packet-byte-tamper` | replaced 'registers' in packet.d4.yml | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 2 | [1, 2] | **True** |
| 2 | `expected-holds-tamper` | replaced '"hold": 12' in expected-holds.json | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 2 | [1, 2] | **True** |
| 3 | `projection-stale` | appended to typed-labels.d4.yml | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 2 | [1, 2] | **True** |
| 4 | `pipeline-pin-stale` | replaced '"sha256": "943f487ba991d45d369eb8fb6e9bb686046df165424d101cfa2670f79bb844b2"' in typed-pipelines.json | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 2 | [1, 2] | **True** |
| 5 | `adapter-drift` | appended to packet.d4.typed.yml | `python3 tools/assemble-d4-typed.py --check examples/culture-d4/packet.d4.typed.yml` | 1 | [1] | **True** |
| 6 | `assembly-drift` | appended to packet.d4.yml | `python3 tools/assemble-culture-d4.py --check` | 1 | [1] | **True** |
| 7 | `argot-violating-form` | inserted a lexicon row at line 190 of 04-lexicon.yml | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | 1 | [1] | **True** |
| 8 | `argot-clean-positive` | inserted a lexicon row at line 190 of 04-lexicon.yml | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | 0 | [0] | **True** |
| 9 | `thirteenth-component-refused` | wrote zz-argot.yml | `python3 tools/assemble-culture-d4.py` | 2 | [2] | **True** |
| 10 | `corrupt-packet-input` | wrote packet.d4.yml | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | 2 | [2] | **True** |
| 11 | `register-violation-propagates` | inserted a lexicon row at line 190 of 04-lexicon.yml | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 2 | [1, 2] | **True** |
| 12 | `register-clean-propagates` | inserted a lexicon row at line 190 of 04-lexicon.yml | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 2 | [1, 2] | **True** |

**12/12 bite.** A control that does not bite is a finding, not a pass.

## 4. The register domain at this seat's close — the delta the D-seat must move

**The register stratum had not landed when this fragment was written.** Two independent structural facts fix the pre-register state:

- **No `registers:` block in the packet.** The assembler's `PACKET_KEYS` allowlist (`tools/assemble-culture-d4.py:71`) names `registers` as a mergeable block and its own selftest fixture ships a `06-register-contract.yml` declaring one (`:462-472`), but the delivered `packet.d4.yml` carries no `registers:` top-level block at all. The register *stratum* exists as a concept in the tooling and nowhere in the delivered packet.
- **No derivation pair on any register-scoped form.** The argot gate's own coverage line is the register-domain census:

```
coverage: examples/culture-d4/packet.d4.yml records=156 register_scoped=6 derived_pairs=0 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
```

Read against claim D's `after_required`, the state at this stamp is:

| claim-D requirement | state at this stamp |
|---|---|
| components declare register-scoped forms with machine-readable derivation rules (`head2`/`reverse` or designed equivalents) | **not landed** — no `registers:` block, no `derived_from`/`derivation` pair (`derived_pairs=0`) |
| the packet regenerates deterministically | **green** — §2 determinism control; a rebuilt packet is byte-comparable against this baseline |
| typed labels classify the register forms per the label-typing table | **not landed** — the six register-scoped lexical forms are pre-existing trade/craft loans, not new typed labels |
| the argot leg REPLAYS the register derivations and finds them clean | **green over an empty domain** — `violations=0` with `derived_pairs=0`; the leg has teeth (§3 control 7) but nothing to replay |
| the D4 typed gate passes with the hold set updated and named | **green, hold set unchanged** — 12 holds / 0 notes / 0 fails; a register landing that changes the finding set must re-pin `expected-holds.json` **as a new row** |
| the round-17 forecast marked delivered with the delta closed | **open** — this is the round-26 D claim's own work |

**The exact re-run recipe for the post-register state** (this seat's harness, ready to execute):

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git clone --quiet --no-hardlinks --shared . .scratch/x64/clone-post
python3 .scratch/x64/chain-cold-run.py --root .scratch/x64/clone-post \
    --out .scratch/x64/post-register-chain.json \
    --scratch .scratch/x64/scratch-post --jobs 6
python3 .scratch/x64/chain-controls.py --root .scratch/x64/clone-post \
    --out .scratch/x64/post-register-controls.json --scratch .scratch/x64/ctl-post
python3 .scratch/x64/chain-delta.py \
    --before .scratch/x64/pre-register-chain.json \
    --after .scratch/x64/post-register-chain.json \
    --out .scratch/x64/delta.json
```

### 4b. The round's own counting command, run cold

The runner's entry point landed during this seat's window and the runner was then revised again; this seat measured **two** revisions cold, in isolated clones. Both are recorded because the movement is itself evidence.

```
$ python3 reports/round-26/run-validation.py --check

snapshot 1  runner_sha256 7e9b4457d0ec61c7d1fca75396023eec22df8bac580e16824fb9796cda3e70ed
            exit 1; acceptance_checks_passed: False
            claim D False (5)   claim O False (1)   claim C False (17)

snapshot 2  runner_sha256 fe6671a211d09c3c9af818a8204ff8366bf3b772420bafb94ad77d9854282480
            exit 1; acceptance_checks_passed: False
            claim D False (4)   claim O True (0)    claim C True (0)
            protected filed artifacts: passed True, 0 differences (both snapshots)
```

Between the snapshots the O and C claims went green as their seats landed their work; **claim D did not move in substance** — it fails on the same missing stratum at both revisions. Claim D's four failures at snapshot 2, in the runner's own words:

- the D4 contract's `lexicon.record_fields` do not declare the derivation relation
- the register-scoped derivation domain is still empty (`derived_pairs=0`)
- the argot gate replays an empty domain
- the typed projection carries no label for any delivered derivation pair

**This is the independent confirmation of §1b's design-only verdict**: the design landed, the data did not. The runner also confirms the filed-round surface is intact (1,328 protected paths, 0 differences) at both snapshots — so claim D's red is an honest red, not drift.

## 5. Findings for the parent

**X64-F1 (instrument, this seat's own — named, not hidden).** The stdout of `tools/d2-typed-labels.py --selftest` (and therefore `d4-typed-labels-check-gate.py --selftest`) **embeds the absolute path of the tree it runs in** — the leg `boundary control: foreign label component '<root>/…'`. Two cold runs in two clones produced identical leg counts (163/163) and different stdout digests. Any consumer comparing selftest stdout *digests* across roots will see a spurious difference; compare leg counts, or normalise the path, not the digest. Not a chain defect and not a claim-D blocker.

**X64-F2 (class mismatch, pre-existing).** `tools/gates/provenance-audit.py` over `examples/culture-d4/packet.d4.yml` exits 2 with `CANNOT-EVALUATE: … not a corpus entry document (no Markdown heading, no header line)`. The tool grades corpus Markdown, not a YAML packet; invoking it on the packet is a caller error, not a chain break. Recorded so the red is not misread as a regression. It is not in the D4 chain proper and this seat did not include it in the pass/fail set.

**X64-F3 (guard observed, worth keeping).** Adding a thirteenth component file to `examples/culture-d4/components/` is refused by the assembler: `assembly error: component collision: 'lexicon' is declared differently by …/04-lexicon.yml and …/zz-argot.yml; refusing to override` (exit 2). The registry is closed at 12 files by construction; a D-seat that adds register forms must add them **inside** an existing component, not as a new file.

**X64-F5 (the counting command's own state mid-window).** `reports/round-26/run-validation.py` existed for part of this seat's window as a **partial file**: 904 lines, parses cleanly, but it carries no `argparse` block and no `if __name__ == "__main__"` entry point, so `python3 reports/round-26/run-validation.py --check` exits 0 and prints **nothing at all** — measured in an isolated clone, both stdout and stderr empty. A silent exit 0 from a counting command is the most dangerous possible reading: it is indistinguishable from a green acceptance to any caller that only checks the exit code. This is a **mid-wave state**, not a defect to fix here — the runner's entry point had not landed when this seat measured — but the parent must not accept the round on an exit code alone until the runner prints a receipt. **A runner that prints nothing has measured nothing.**

**X64-F6 (superseding note on X64-F5).** The runner's entry point landed later in the same window; `reports/round-26/run-validation.py` now runs and prints a full JSON receipt (§4b, `runner_sha256 7e9b4457…`, exit 1, `acceptance_checks_passed: False`). X64-F5 is therefore **closed as a mid-wave state**, and the trap it names — an exit code with no output — did not reach the round's close. It is kept in this record because the silent-0 window was real and a caller that sampled it would have been misled; the durable lesson is the one already stated: **a counting command must be read by its receipt, never by its exit code**.

## 6. Limits

- This is a **re-run record**, not round acceptance. The parent owns the verdict and must re-run the round-26 counting command on the final settled tree.
- The tree moved during this seat's window (round-26 surfaces grew from 2 to 78 tracked-content paths). Every number above binds to the stated receipt and revision; a number without its receipt is not a measurement.
- Path-embedded stdout (F1) is the one place where a digest is not comparable across roots; all other digests were compared within a single root.
- NON-CANON engineering evidence. No source-freshness certification, real-world rights clearance, lore acceptance or promotion is claimed. No commit, no push, no shared bookkeeping, no filed-round write by this seat.

## 7. Reproduce

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git clone --quiet --no-hardlinks --shared . .scratch/x64/clone
python3 .scratch/x64/chain-cold-run.py \
    --root .scratch/x64/clone --out .scratch/x64/chain.json \
    --scratch .scratch/x64/scratch --jobs 6
python3 .scratch/x64/chain-controls.py \
    --root .scratch/x64/clone --out .scratch/x64/controls.json \
    --scratch .scratch/x64/ctl
```

---

*Receipts: `.scratch/x64/{pre-register-chain.json,pre-register-controls.json}`. Fragment written 2026-10-18.*
