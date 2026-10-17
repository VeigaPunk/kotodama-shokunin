# R11-D26 — scribe: fragment ledger tying all depth evidence (claim D, `d2-typed-pipeline`)

- seat: **R11-D26** (scribe, claim D), round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D26 (scribe): fragment ledger tying all depth evidence; reports/round-11/depth/scribe.md."
- writes: this file only (plus in-lane scratch under `.scratch/D26-*`). No commit, no push, no earlier-round artifact byte touched; `reports/round-{8,9,10}/**` are filed and read-only here.
- canon: NON-CANON engineering evidence. Nothing here admits a round, a capability, or a canon fact.
- status: **COMPLETE for the wave window 22:00–22:19Z** — every depth fragment on disk at the 22:18:02Z close is read and tied (§3); claim-D e2e legs independently verified by this seat (§4); `test-holdset`/`review-20` had **not** landed at close (D10's equality receipts live in `test-e2e.md` T1–T4); the counting command was run by this seat at 22:17:43Z → **claim D PASS** (O PASS, F FAIL; §4).

## 0. Method and clock

- Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. All scratch under `export TMPDIR=$PWD/.scratch` (confirmed before every scratch-writing command); `/tmp` unused.
- The ledger ties the round-11 depth evidence: for each shard R11-D01..D25 the fragment path, sha256, the command(s) that produced its load-bearing claim, and my own independent re-run where runnable. Claim D's counting command legs (`python3 reports/round-11/run-validation.py`; `python3 tools/assemble-d2.py --check`) are captured as they become available.
- Timestamps are UTC (`date -u +%FT%TZ`); local is UTC-3.

## 1. Baseline receipts (pre-fragment, captured by this seat)

### 1.1 Standing green legs

```sh
export TMPDIR=$PWD/.scratch
python3 tools/assemble-d2.py --check     # exit 0 — "packet.d2.yml: byte-identical deterministic assembly"   (22:00:41Z)
python3 tools/d2-typed-labels.py --selftest > .scratch/D26-typed-selftest.txt 2>&1   # exit 0 — "selftest: 39/39 checks passed"  (22:00:41Z)
python3 tools/assemble-culture-d3.py --check > .scratch/D26-d3check.txt 2>&1          # exit 0 — both artifacts byte-identical  (22:01Z)
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json > .scratch/D26-d3frozen2.txt 2>&1
                                                                                      # exit 0, findings 0  (22:01Z)
python3 tools/check-gate-battery.py > .scratch/D26-battery.txt 2>&1                    # exit 2 — battery_exit 2, pass 7, fail 0, unevaluable 0; single 28-file tree preserved  (22:01Z)
```

The battery's exit 2 with 7 pass / 0 fail is the standing state (the two gates without a default-root baseline); it matches the round-9/10 receipts and is not by itself a failure signal. The claim-D acceptance form for the battery is its selftest (`--selftest`), run in §4 once the integrator's wiring lands.

### 1.2 Known-red or at-risk legs at wave start

- `python3 tools/d2-typed-labels.py --check` → **exit 1** at 22:00Z: "examples/culture-d2/typed-labels.d2.yml differs from the deterministic projection" (`.scratch/D26-typed-check.txt`). This is the round-10 A2 observation, live: the committed artifact's `assembly.packet_sha256` records `8da90b07…` while the committed packet hashes `e0f21509…` (`sha256sum examples/culture-d2/packet.d2.yml` 22:00Z). Cause is on record (round-8 admit commit `e1694ba` re-pinned the packet; artifact not re-emitted); whether round-11's wiring re-emits the artifact is the D claim's business. The **selftest** is green (39/39) either way.
- D2 typed projection snapshot pre-wave: `python3 tools/d2-typed-labels.py --json` → exit 1 (findings, report complete); stats `{labels: 58, hold: 15, note: 1, fail: 0}`; finding ids ×count: `D2L-FORM-UNRESOLVED` ×10, `D2L-NATIVE` ×1, `D2L-RANK` ×4 — snapshot in `.scratch/D26-typed-json.json`.
- `d2-typed-labels` artifact hash at wave start: `e70ba1477dbeb830061db6fd12516b7d902587bddae173f55a3650015d380b2f` (22:00Z).
- Tool hashes at wave start: `tools/assemble-d2.py` `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d`; `tools/d2-typed-labels.py` `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`.

## 2. Depth shard map (R11-D01..D26)

(from `reports/round-11/targets.json`; fragments fill in as they land)

| shard | target | expected fragment | status |
|---|---|---|---|
| D01..D02 | typed-pipeline wiring design; expected hold set for `examples/culture-d2` | `depth/design.md` | pending |
| D03..D08 | implementation: assembler consumption, gate reader adapter, holds mapping, projection validator, CLI entry, frozen re-pin | `depth/impl-*.md` / tool edits | pending |
| D09..D16 | tests: e2e positive, hold-set equality, legacy-vs-typed differential, determinism, replay-frozen, boundary/malformed, CLI negatives, d3 interop, battery | `depth/test-*.md` | pending |
| D17..D19 | negative examples (smuggled translated label; dropped owed form; laundered hold) | `depth/neg*` | pending |
| D20..D23 | adversarial reviewers: vs design spec; hold-set completeness; circularity of re-pin | `depth/review-*.md` | pending |
| D24..D25 | capability-row draft; frozen-manifest records | `depth/*.md` | pending |
| D26 | this fragment ledger | `depth/scribe.md` | this file |

## 3. Fragment ledger (fills as fragments land)

### 3.1 Fragment table (sha256 stamp 2026-10-17T22:10:22Z; fragments are live — final hashes at admission)

| shard | fragment | sha256 (22:10:22Z) | load-bearing evidence (command → observed, from the fragment; my independent check marked ⟦IC⟧) | status |
|---|---|---|---|---|
| D01 | `design.md` | `addd0ea2ecf71871621814aa5917347ae6503d0040bcf64c31cae0f4baa69c49` | wiring design: adapter `tools/assemble-d2-typed.py` + gate `tools/gates/typed-pipeline-gate.py` (L1–L4); **expected hold set = 15 holds + 1 note, fail ∅** (§4.2); routing experiment: all ten `garment`→`garment_gloss` → naming gate 17→7 findings, `PHON-INVENTORY` 10→0, other 4 gates byte-unchanged (§1.3) | landed |
| D02 | `design-review.md` | `a3b0dc0a0fc7c36641fce07a62b16be3cdd8ef8c844399e39d6e8822d2e4b953` | 9 adversarial findings DR-01..DR-09 (second hold population; severity-account contradiction; spec 5 holds short; silent-channel mechanisms; exit-convention conflict); written pre-design so reconciliation **V1 = to-verify** | landed |
| D06 | `shard-holds.md` | `aa69d7627cdeedfc425aba98fc222e04b269e7059c9c9e3c11f3f3db39e0131c` | `grep -c "TL-01\|TL-02" tools/d2-typed-labels.py` = **0** → live vocabulary `D2L-*`; TL-01 → `D2L-FORM-UNRESOLVED` exact 1:1 exchange (10 PHON FAIL ↔ 10 named holds, same records); F-D06-1 (R5 no-bytes silent), F-D06-2 (kindless `KeyError` CLI traceback); §4.3 carries ready-to-land `expected-holds.json` | landed |
| D11 | `test-determinism.md` | `bcdf339734605d8ce22ae11fecf18b08b48df085cfb9e57525bbe73bfb957e23` | P1–P7: packet `e0f21509…` + fresh projection `a3aa452c…` byte-identical across copy/cwd/`PYTHONHASHSEED`/locale/mtime probes; gate stdout + exits constant; only red = stale pin; wired-chain divergence `to-verify` | landed |
| D13 | `test-boundary.md` | `233158bf5c9ded15433c2cd932ab3492a54aa94eb39b395ee761a0b6e8a97d0f` | 29 single-mutation cases + 14 CLI-mode probes: 10/10 loader classes give exit-2 stables; **F1 kindless → `KeyError: 'kind'` traceback at :2497**; F2 silent-drop shapes; F3 dup keys last-wins; F4 `null` reads as the string `"null"`; F5 `[fail]`-scope findings exit 1; F6 `--emit` writes-and-exits-2 | landed, post-wiring pending |
| D14 | `test-cli.md` | `511aed8ab4c9480c575b68350fc5099ff5fdc8367a75072977967f92a725808f` | 17 CLI cases (pass 16 / fail 1 = row 11 known drift), 8 wrong-packet cases all exit 2, 0 tracebacks; documented exit contract 0/1/2 | landed, post-wiring pending |
| D15 | `test-interop-d3.md` | `6f7e6214adcfb301067da5b3845d4c8430c8d3277a002331a1531eddb2181d6` | d3 7/7 ledger rows hash-stable; **Probe A: any byte edit to `tools/assemble-d2.py` → d3 `--check` exit 1** (embedded `serializer_sha256`); Probe D: d3 re-pin chain = `packet.json` **and** `examples/culture-d3/expected.json` ⟦IC: `packet.json:199` = sha256 of `assemble-d2.py`; d3 `--check` exit 0; frozen leg exit 0/0 findings⟧ | landed |
| D18 | `neg-18.md` | `6ee492f68dbc6a5c6cc7cc7f423a8b5533bf6fef3c6755ad7840b1de9a57f5de` | negative "owed form dropped silently": projector's hold derives from the label row → deleting the row loses the hold (silent); supplement prototype derives from slot obligation → catches it; wiring re-run pending | landed (pre-wiring) |
| D21 | `review-21.md` | `a3fbd605a4d9dd445deae89ac5ac0d39ed3226979fac2a23cd3adc7dc9363d8f` | hand-derived hold set independently = 15 holds + 1 note (matches design §4.2 item for item); F1 `--selftest` cannot fail on hold-set damage (5 mutations incl. empty set → 39/39); F2 9 nested `R-MAT-BRIDGE-MISSING` holds computed but never merged; F3 `maps_to: null` read as `'null'` severity divergence; F4 counters contradict findings; F5 known pin; F6 filed-artifact edits | landed |
| D22 | `review-22.md` | `487c1638bec7e78889fc7608bc59660fb3d74191ea14a899e768b1aae166133b` | circularity audit C1–C6 threat model + pre-change digest table (20 artifacts); verdict sections pending impl | in progress (skeleton at read) |
| D23 | `review-23.md` | `26a32488aba129ea6abe7ef36483090345747822863f1424dbc3d88b8b473f10` | SKILL.md label-typing region vs live tool: 3 behavioral promises fail measurement, 11 citations unresolvable (S1–S3 class); F1 corroborated; §6 post-wiring pending | landed (pre-wiring phase) |
| D24 | `capability-draft.md` | `fd1f41e241b833a0e02b0efa5964723d696ce67e7f97e74fe055f0f5aca46032` | before-state: naming gate 10 `PHON-INVENTORY` FAILs on GAR-01..10 (stdout `ebc8850d…`) ⟦IC: exact match⟧; typed `--json` `880d0e45…` 15 holds/1 note ⟦IC: exact match⟧; `--check` one-line drift; replay live exit 2 7/7; row settled once c1–c6 verify | live-editing (grew 18→25 KB during read) |
| D25 | `frozen-records.md` | `2eb4b22a860337584d2505833cdf602117f7eb8daec40be3a160224a78c47261` | inventory of every frozen surface: 2 legacy manifests (RED c-n-e by design), 8 `expected.json` r9-pre (GREEN), d3 guard freeze (GREEN), round-4 no-manifest, **no re-pin generation exists**, `tools/gates/frozen/README.md` absent; FR-1..FR-7 open items; green-verification protocol §7 | landed |
| D26 | `scribe.md` (this) | `8c8dd85e431ff7397ad8e29884579a079e0e23ee4cbd88fbd312e38d079f5a01` (as of 22:10:22Z, pre-§3 write) | this ledger | in progress |

Not yet landed at the 22:10:22Z stamp (named for the parent): `impl` fragments for D03/D04/D05/D07/D08 **and their artifacts** (`tools/assemble-d2-typed.py`, `tools/gates/typed-pipeline-gate.py`, `examples/culture-d2/expected-holds.json`, `tools/gates/expected/typed-pipeline/r11/**`, `tools/gates/frozen/round-11/MANIFEST.tsv` — none present in `ls` sweeps at 22:10Z), tests D09 (e2e), D10 (hold-set equality), D12 (differential), D16 (battery), negatives D17/D19, review D20, and `reports/round-11/run-validation.py` (claim D's counting command; absent at every poll through 22:10Z).

### 3.2 Cross-fragment ties (agreements, tensions, residuals)

**Agreements (three independent derivations converge on the hold set).** `design.md` §4.2 (D01), `review-21.md` §0/§2 (D21, hand derivation), `shard-holds.md` §4 (D06, re-derivation) and my own `--json` snapshot (`.scratch/D26-typed-json.json`, `880d0e45…`, stats `{hold: 15, note: 1, fail: 0}`; ids `D2L-FORM-UNRESOLVED`×10 `GAR-01..10`, `D2L-NATIVE`×2 `L-15`,`L-16`, `D2L-RANK`×4 with `SR-01#a|SR-01#b` the note) all name the **same 15 holds + 1 note**, same `where`s. The before-state is likewise single-valued across fragments: naming gate exit 1 with exactly ten `PHON-INVENTORY` lines on `GAR-01..GAR-10` (design §1.1; capability §2.1; D11 §4; D14 §1.2; my re-run stdout `ebc8850d08ec1b7e32616cbca9092ba66f3b6f148a61515a033e6bed6fa66f4b` — byte-equal to both fragments' cited hash).

**Agreements (the style-drift finding).** `d2-typed-labels.py --check` exit 1 with exactly one differing line (`assembly.packet_sha256`: `8da90b07…` vs `e0f21509…`) is measured identically by capability §2.3, D11 §5 (`diff`, one line), D14 §4, D25 §5, R21 F5 and my §1.2 — disposition on record (round-8 admit `e1694ba` re-pinned the packet; artifact not re-emitted); repair is the D wiring's.

**Tension 1 — the finding set is channel-dependent (R21 F2/F3 vs design §3.1 L3).** A second reconciliation channel computes **9 `R-MAT-BRIDGE-MISSING` holds that never reach the merged finding list**, and 2 of them are classed `hold` where the round-8 receipt said `note` (`maps_to: null` read as the string `'null'`, `11-costumes.yml:138,189`). Design's L3 compares "the whole pipeline finding set"; R21 §5 requires the wiring to disposition the +9/−2 explicitly, or the set choice becomes the laundering channel review-22's C-patterns describe. This ledger carries the tension as an open decision item, not a resolved fact.

**Tension 2 — the d3 serializer pin constrains the wiring's file choice (D15 Probe A vs design §2.1).** `examples/culture-d3/packet.json:199` embeds `serializer_sha256` = whole-file hash of `tools/assemble-d2.py` (⟦IC verified: `packet.json:199` `8ea6bdde…` == `sha256sum tools/assemble-d2.py`⟧), so any byte edit to that file reds d3 `--check` even if functionally inert. Design's adapter route keeps `assemble-d2.py` unchanged (§2.1 "[unchanged]", §7 "no shard edits … `tools/assemble-d2.py`"), which satisfies D15's condition; if the integrator instead edits it, the d3 re-pin chain (Probe D) must be executed. No contradiction today — the constraint is the reason the adapter exists.

**Tension 3 — the projector's silent classes vs SKILL.md claims (D23 F1, D06 F-D06-1, design §8.3).** A sound kind declared with no bytes yields no projector finding (design-spec R5 unmet), and a kindless typed record crashes the CLI with a raw `KeyError` traceback (D13 F1, D06 F-D06-2). The design orders the adapter to inject the hold and report the deviation; the ledger records that post-wiring these CLIs and SKILL.md claims must be re-read on the **wired** surface, not inherited from the projector's green selftest.

**Residual — the selftest cannot see hold-set damage (R21 F1).** Five one-line mutations, including an empty hold set, all pass `--selftest` 39/39 exit 0. Therefore the claim's "findings == expected hold set" cannot be carried by the tool's own control matrix; it must live in the wired e2e (design L3 / R21 §5.3). This ledger treats the e2e runner's existence as load-bearing for claim D.

### 3.3 This seat's independent re-runs (all `TMPDIR=$PWD/.scratch`, 2026-10-17)

| command (lane root) | stamp | observed |
|---|---|---|
| `python3 tools/assemble-d2.py --check` | 22:00:41Z | exit 0, "byte-identical deterministic assembly" |
| `python3 tools/d2-typed-labels.py --selftest` | 22:00:41Z | exit 0, 39/39 (`.scratch/D26-typed-selftest.txt`) |
| `python3 tools/d2-typed-labels.py --check` | 22:00:41Z | exit 1 — stale pin, one line (`.scratch/D26-typed-check.txt`) |
| `python3 tools/d2-typed-labels.py --json` | 22:01Z | exit 1; 16 findings; stats `{hold: 15, note: 1, fail: 0}`; stdout sha256 `880d0e45…` |
| `python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml` | 22:02Z | exit 1; 10 `PHON-INVENTORY` lines on exactly `GAR-01..GAR-10`; stdout `ebc8850d…` |
| `python3 tools/assemble-d2.py --selftest` | 22:04Z | exit 0, 42/42 (`.scratch/D26-asm-selftest.txt`) |
| `python3 tools/assemble-culture-d3.py --check` | 22:01Z | exit 0, both artifacts byte-identical |
| `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` | 22:01Z | exit 0, `findings: 0` (packet positional required; my first invocation was malformed and exited 2 — recorded, §1.1) |
| `sha256sum` pins: `packet.json:199` `serializer_sha256` vs `tools/assemble-d2.py` | 22:04Z | equal (`8ea6bdde…`) — D15 Probe A premise verified cheaply |
| `python3 tools/check-gate-battery.py` | 22:01Z | exit 2; `{pass: 7, fail: 0, unevaluable: 0}`, 28-file tree preserved; standing coverage state |

### 3.4 Wave additions, 22:10–22:19Z (implementation, tests, receipts; hashes at 22:18:02Z)

New fragments (paths under `reports/round-11/depth/` unless noted):

| shard | fragment | sha256 (22:18:02Z) | tie |
|---|---|---|---|
| D03 | `shard-assembler.md` | `13ac65ab3eb3f0c2fdda8f7d11812f62420aab37561667a33beccc52ed180d2f` | offline adapter fragment `assemble-d2-typed.py` (`3f67af66…`, 450 lines) delivered for the integrator; **no `tools/assemble-d2-typed.py` landed** — the contract is realized by D05's `typed-gate-flow.py`; mirror selftest 22/22 |
| D04 | `shard-gate-adapter.md` | `edda9de1ea96cb9d2e3e086f8e62492c0658447391d98e996174644131bebf89` | read-side adapter module `a0564683…`; fail-closed codes `A-DATA/A-KIND/A-COVERAGE/A-STALE/A-CHANNEL/A-HOLD`; a required hold the projection omits is **synthesized** with `"synthesized": true` (the adapter-side answer to design §8 item 3 / review-23 F1) |
| D05 | `e2e-receipt.json` | `3b71ac7d846085392261cf56f5323485324f26238bb303a82dbbb8423f4d9249` | machine-readable receipt: `claim D`, `command "python3 tools/typed-gate-flow.py --e2e --json"` (flag alias verified by me at `tools/typed-gate-flow.py:775`), 10/10 checks `true`, `exit_code 0`, expected set + findings embedded, `frozen_manifest tools/gates/frozen/round-11/MANIFEST.tsv` |
| D07 | `shard-validator.md` | `f330c3509bf6825990c27a2dc572a0f328ba198191bd0fa094c6cd9fb3191918` | pre-gate validator block `8e329024…`, 42/42 controls; projector-derived `expected-holds-v1.json` `815bfc6f…` (hold 15 / note 1 / fail 0); live defect reported (stale pin, fixed during the wave) |
| D08 | `repin.md` | `cca6895f2b22918099d68fd3aaaede245981ca65cfadd2dafe599169dcc54202` | re-pin mechanics PROVEN on isolated mirrors: round-3 manifests re-pinned `pin-only` into candidate generations (verdicts byte-identical, replay 7/7 exit 0); r9-pre baselines re-pinnable; wired round-11 generation 10 rows, replay 10/10 (my own run §4) |
| D09 | `test-e2e.md` | `b8fc5a162ebe311ba842be3c8334c577c9637c3f4fc3c28d2a098bd77ee12956` | e2e GREEN: exit 0, 10/10 checks, stdout `d236e8e2…`, 15 `[hold]` + 1 `[note]`; four-key equality harness T1–T4 PASS; replay in-repo-TMPDIR caveat (§5.7); **D10's equality receipt lives here** (no separate `test-holdset.md` landed) |
| D12 | `test-differential.md` | `91a6b280ee8bf93984d75be9ceda68f5a4ff7962d86142fcea6b50e72457ebe0` | legacy-vs-typed differential over the five gates: exactly the ten `PHON-INVENTORY` removals, 0 added, retained lines byte-identical |
| D16 | `test-battery.md` | `8ddaa6e6ab1fc8649940225ec95bdf991ebd7ef6fbc985e9db1c07a91795e98c` | battery selftest 28/28 exit 0 ×2, stdout `8b1fdd6f…` **byte-equal to round-10 ledger rows 100/106/112/122/161**; 3-root full run exit 0, 8/8 pinned, 7/7 covered; default-roots exit 2 unchanged (standing coverage gap); control: foreign `expected.json` under a scanned root → `BASELINE-GATE-UNKNOWN` |
| D17 | `neg-17.md` | `9253cdc553ad68816fa0d47ee0a0f3ce6cd7b415487b1c6fcf73617b8411ec50` | negative: translated label smuggled onto the sound channel — caught (its own receipt) |
| D19 | `neg-19.md` | `fd3d487e37a1dd5c93bf91a1f738da0e4f9370737311efe6d3b90754aa013f37` | negative: a hold laundered as clean — caught (its own receipt) |

Updated fragments (live edits during the window; final hashes at admission): `design-review.md` `c5003dc9…` (was 29 023 B at 22:07 → 42 710 B), `frozen-records.md` `59902a04…`, `capability-draft.md` `eb567192…`, `shard-holds.md` `8efb4c31…`, `neg-18.md` `a6039a57…`, `review-21.md` `3b22e463…`, `review-23.md` `171f7843…`; `design.md` unchanged `addd0ea2…`; `review-22.md` unchanged `487c1638…` since 22:03 — **its §3–§5 (fragments reviewed / findings by pattern / falsification runs) remained placeholders at close**; `review-20.md` never landed.

Implementation artifact state at close (my `sha256sum`, 22:18:02Z):

| artifact | sha256 | note |
|---|---|---|
| `tools/typed-gate-flow.py` | `a7e1224fb85ce2c1a5f880c50a2c71f9392be1fc4059801a45dc7727b04f63ec` | integrator D05's tool; **live** during the window: `f3b417bb…` (22:12) → `ae55e6fa…` (22:14) → `a7e1224f…` (22:18) |
| `examples/culture-d2/packet.d2.typed.yml` | `e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb` | committed typed packet (build product gates read) |
| `examples/culture-d2/typed-gate.expected.json` | `7ed597317b32b238d880af0a602fcbfa1ffd92608008879f049db9fd02aa03aa` | expected set; moved `e962849a…` → `7ed59731…` during the window |
| `examples/culture-d2/typed-labels.d2.yml` | `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` | **re-pinned**; equals design §5.1's prediction exactly; `--check` exit 0 |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | `4ddb911ced45288533b8f3dadc76a339b966f31611351a9b86645349d5904376` | 10 rows = 5 gates × {typed `e8a83445…`, raw `e0f21509…`} |
| `tools/assemble-d2.py` | `8ea6bdde…` **unchanged** | d3 serializer constraint (§3.2 Tension 2) satisfied |
| `tools/d2-typed-labels.py` | `0da0015f…` **unchanged** | projector untouched |

## 4. Claim-D end-to-end legs (to fill at integration)

## 4. Claim-D end-to-end legs — measured by this seat (runs 22:00–22:19Z, `TMPDIR=$PWD/.scratch` unless noted)

| claim D clause (`reports/round-11/claims.json`) | command (mine) | result (stamp, capture) |
|---|---|---|
| e2e over `examples/culture-d2` exits 0; findings == expected hold set | `python3 tools/typed-gate-flow.py` | **exit 0**, `summary: 10/10 checks passed`, `findings: 16 (hold 15, note 1)` (22:14:15Z, `.scratch/D26-e2e2.txt`); `--json` → exit 0, `ok: true` (22:15Z, `.scratch/D26-e2e.json`) |
| translated labels never on the sound channel | `python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.typed.yml` | exit 1 (retained `NAME-NEAR`×6 + `CROSS-HOLD`×1), **0 `PHON-INVENTORY` lines** (22:19Z, `.scratch/D26-naming-typed.txt`); flow's own `differential-exact`: 10 removed, 0 added, retained identical |
| owed native forms carried as named holds (not PHON artifacts) | `--json` finding set; flow `owed-slots-crosscheck` | ten `D2L-FORM-UNRESOLVED` holds on `GAR-01..GAR-10` ↔ `LEX-GAR-01..LEX-GAR-10`; check `ok` |
| frozen replay re-pinned and green | `TMPDIR=$HOME/.cache/kotodama-d26-tmp python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` | **exit 0, `REPLAY OK: 10/10 rows reproduced`** (22:14:42Z, `.scratch/D26-replay11b.txt`); the same command under the standing in-repo TMPDIR exits 2 `mirror_unsafe` ×10 (recorded; environmental, §5.3) |
| projection re-pinned | `python3 tools/d2-typed-labels.py --check` | **exit 0**, byte-identical deterministic projection (22:14:15Z); artifact `a3aa452c…` = design §5.1's prediction exactly |
| assembler still regenerates byte-identically | `python3 tools/assemble-d2.py --check` | exit 0 (22:15:09Z) |
| d2/d3 selftests + battery remain green | `d2-typed-labels.py --selftest` **39/39**; `assemble-d2.py --selftest` **42/42**; `check-gate-battery.py --selftest` **28/28**; `assemble-culture-d3.py --check` exit 0; `check-evidence-coupling.py … --frozen` exit 0 / findings 0 | all green (22:15:09Z, `.scratch/D26-*`); battery full run still exit 2 with `pass 7 / fail 0` (standing coverage state, §1.1) |
| counting command | `python3 reports/round-11/run-validation.py` | **claim D: PASS**; claim O: PASS; claim F: FAIL (all failures in `recheck/`); `acceptance_checks_passed: False` driven by F only (22:17:43Z, `.scratch/D26-runner.txt`). This run rewrote `reports/round-11/validation.json` (`fe5f8538…`) — the parent regenerates it at admission; the prior receipt (`cfc61df8…`, 22:09:44Z) was a stale pre-wiring snapshot whose D/O failures are outdated |

Equality basis: the flow compares against `examples/culture-d2/typed-gate.expected.json` (moved `e962849a…` → `7ed59731…` during the window; the flow's `expected-file-current` re-derives it, and `--check` re-evidences byte-identical derivation at the read revision). D09's T1–T4 harness and `e2e-receipt.json` carry the four-key equality (id/severity/where + counts) — read, not re-implemented, by this seat.

## 5. Limits and open items

1. **Live revision churn.** `tools/typed-gate-flow.py` moved `f3b417bb…` → `ae55e6fa…` → `a7e1224f…` during this ledger's window and `examples/culture-d2/typed-gate.expected.json` moved `e962849a…` → `7ed59731…`; fragments were still being edited while read. Every hash here names its stamp (close at 22:18:02Z); the admission re-read is the parent's. The §4 legs hold for the bytes named there only.
2. **`repin.md` timestamp anomaly.** It cites receipts stamped `22:16Z`/`22:21Z` while its own mtime is `19:14:05-03` (= 22:14:05Z) — stamps ahead of wall clock. Flagged `to-verify`; its load-bearing round-11 replay claim was independently reproduced by me (10/10, §4), so no claim of mine rests on the anomalous stamps.
3. **In-repo `TMPDIR` replay refusal.** `replay-frozen.py` refuses a mirror root inside the repo (`mirror_unsafe`); D09 and I both hit this with the lane's standing `.scratch` TMPDIR. The green replay reading requires an out-of-repo temp root (mine: `$HOME/.cache/kotodama-d26-tmp`). Admission runs must use an out-of-repo TMPDIR or the replay leg will read red for environmental reasons.
4. **Open decision carried, not resolved — review-21 F2/F3.** A second reconciliation channel computes 9 holds (`R-MAT-BRIDGE-MISSING`) that never reach the merged finding list, and 2 `maps_to: null` records are read as the string `'null'`. No landed fragment disposes the +9/−2 explicitly; the wired equality is over the merged 15+1 set. `to-verify` for the parent (self-blessing risk per review-22's C-patterns).
5. **review-22 (circularity) unfinished.** Its §3–§5 verdict sections remained placeholders at close (`487c1638…` unchanged since 22:03). The circularity question the design's §5.2 guard addresses was not independently answered within this window.
6. **Not re-run by me:** the fragments' own long receipts (D03/D04/D07/D08 mirror batteries, D12 harness, D17/D19 controls, D16's 3-root battery) are cited, not re-executed; my independent runs are exactly those in §1, §3.3, §3.4-listed spot checks and §4. The counting command was run once (22:17:43Z); the authoritative admission run is the parent's.
7. This ledger ties evidence; it adjudicates nothing — not wiring honesty, not canon, not rights (out of province, `PROVINCE.md`).

## 6. Adjacent observations (reported, not absorbed)

- **F (freshness) red at 22:17:43Z:** `recheck/` held 195 files; runner failures: rows 174/187 not 1:1 with the ledger commands, row-047 `stable=True` but hashes differ, stability 0.788 < 0.95, `summary.json unstable=43 != receipts' 40`. F seats were still landing; the admission run is authoritative.
- **O (operability) PASS at 22:17:43Z:** `tools/exercise-handoff-e2e.py` (67 252 B) and `reports/round-11/handoff/{expected.json,packet-attempt-1.*,shard-glossary.md}` present; not my claim.
- **`reports/round-11/validation.json` regenerated by my counting-command run** (22:17:43Z, `fe5f8538…`); the receipt it replaced (`cfc61df8…`, 22:09:44Z) carried pre-wiring D/O failures now outdated. Regeneratable at admission.
- **Filed earlier-round artifacts modified in the worktree** (review-21 F6 lists seven: `reports/round-{5,6,7,8,9}/validation*.json`, `reports/round-6/checkpoint-validation.json`, `reports/round-10/coverage/index-update-22.md`; combined diffstat `127 insertions, 881 deletions`). I touched none; for the sweep owner.
- **SKILL.md staleness** (review-23 S1–S3, 11 unresolvable citations): the orchestrator's edit; reported, not absorbed.
- **Late arrivals after the 22:18Z close (read, added):** `review-20.md` landed 22:21:44Z, sha `9aa67e002d641be60b20f751ddac79de66a71cf6618bb47be7cba5310d77f6ad` — verdict: the wiring satisfies design.md's substance and the claim's outcome (e2e exit 0 / 10/10; 15 holds + 1 note; zero PHON naming off-channel records; stale pin closed at design §5.1's bytes; replay 10/10; claim D PASS in its isolated copy at 22:18:35Z), plus **10 divergences for parent disposition** (F1 one tool not two; F3 `--check` blindness; F6 frozen location vs battery; F10 hold `where` canonicalization material; rest bookkeeping) — no divergence makes the claim's `after_required` legs false as measured. `tools/typed-gate-flow.py` moved once more (`a7e1224f…` → `5758e315…` by 22:21Z) — admission re-read required. No `test-holdset.md` ever landed; D02/design-review and D21 review-21 carry hold-set review, D09's T1–T4 the equality receipts.

## Receipts

```sh
# 2026-10-17 22:00–22:02Z, lane repo root, TMPDIR=$PWD/.scratch
python3 tools/assemble-d2.py --check                     # exit 0
python3 tools/d2-typed-labels.py --selftest              # exit 0, 39/39
python3 tools/d2-typed-labels.py --check                 # exit 1 (A2 drift, §1.2) — resolved in the wave: now exit 0
python3 tools/d2-typed-labels.py --json                  # exit 1; hold 15, note 1, fail 0
python3 tools/assemble-culture-d3.py --check             # exit 0
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json  # exit 0, findings 0
python3 tools/check-gate-battery.py                      # exit 2; pass 7, fail 0
sha256sum tools/assemble-d2.py tools/d2-typed-labels.py examples/culture-d2/packet.d2.yml examples/culture-d2/typed-labels.d2.yml
```

```sh
# 2026-10-17 22:10–22:19Z, closing window (TMPDIR=$PWD/.scratch unless noted)
python3 tools/typed-gate-flow.py            # 22:14:15Z exit 0; 10/10 checks; findings 16 (15 hold, 1 note)
python3 tools/typed-gate-flow.py --selftest # 22:14Z exit 0; 14/14 checks
python3 tools/typed-gate-flow.py --check    # 22:14Z exit 0; byte-identical derivation
python3 tools/d2-typed-labels.py --check    # 22:14:15Z exit 0 (re-pin a3aa452c…)
python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.typed.yml  # 22:19Z exit 1; 0 PHON-INVENTORY
TMPDIR=$HOME/.cache/kotodama-d26-tmp python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv  # 22:14:42Z exit 0; 10/10
python3 tools/assemble-d2.py --check && python3 tools/assemble-culture-d3.py --check   # 22:15Z exit 0 both
python3 tools/d2-typed-labels.py --selftest; python3 tools/assemble-d2.py --selftest; python3 tools/check-gate-battery.py --selftest  # 39/39, 42/42, 28/28 — exit 0 each
python3 reports/round-11/run-validation.py  # 22:17:43Z; claim D: PASS; claim O: PASS; claim F: FAIL
```

FILES: reports/round-11/depth/scribe.md
SUMMARY: R11-D26 — fragment ledger ties all 25 depth fragments (hashes stamped 22:18:02Z) to claim D's clauses; live-tree legs independently verified (e2e exit 0 10/10 with findings 16 = 15 holds + 1 note, projection re-pinned `a3aa452c…`, zero `PHON-INVENTORY` on the typed packet, round-11 replay 10/10, selftests 39/39+42/42+28/28) and the counting command reads claim D PASS / O PASS / F FAIL at 22:17:43Z; open items: review-22 verdict sections, review-20, and the R21 F2/F3 +9/−2 disposition.
