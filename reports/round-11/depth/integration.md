# R11-D05 — integrator: the D2 typed-pipeline wiring (claim D)

- seat: **R11-D05** (integrator; the only shard editing `tools/*`), round 11
  (loop 1 of 3, build round 4 of 4), 2026-10-17.
- assignment (verbatim): "DEPTH R11-D05 (INTEGRATOR — only shard editing
  tools/*): integrate shard fragments into the real wiring (tools/assemble-d2.py
  + adapter or equivalent per design); keep --check/--selftest green; record
  integration steps in reports/round-11/depth/integration.md."
- writes, complete list: `tools/assemble-d2-typed.py` (new, adapter — design
  §2.2), `tools/gates/typed-pipeline-gate.py` (new, the gate-shaped entry —
  design §3, D05's file), `examples/culture-d2/expected-holds.json` (new, the
  committed baseline — design §4.5), `examples/culture-d2/packet.d2.typed.yml`
  (new, the build product, `--check`-pinned), `examples/culture-d2/typed-labels.d2.yml`
  (re-emitted, §6.1), `tools/gates/frozen/round-11/**` (new generation, §5),
  `reports/round-11/depth/e2e-receipt.json` (new, §7), this file. No filed byte of
  `reports/round-{8,9,10}/**` or `tools/gates/frozen/round-{3,4}` was touched; no
  commit, no push. Two first-pass files written before `design.md` landed
  (`tools/typed-gate-flow.py`, `examples/culture-d2/typed-gate.expected.json`)
  were **retired** in the conformance pass (§1.2) — deleted, not orphaned.
- canon: NON-CANON engineering evidence. Nothing here admits a round, a
  capability or a canon fact. Exit 0 is never a clearance: typing is
  representation discipline, and every hold stays open design debt.
- clock: all stamps UTC; local is UTC-03:00. Lane HEAD: `e3ef1719…` (round-11
  declaration commit); the worktree also carried other seats' concurrent writes
  (§10.4).

## 0. Verdict

The typed-label projection is wired into the D2 gate flow **in the shape
`design.md` fixes**. One gate-shaped command over `examples/culture-d2` —
`python3 tools/gates/typed-pipeline-gate.py` — exits **0** with the pipeline's
findings equal to the committed expected set exactly (15 holds, 1 note, 0
fails), with **zero** translated labels on the own sound channel, and with a
channel differential that is exactly the ten `PHON-*` retirements and nothing
else. The frozen re-pin replays **11/11**. The D2 and D3 selftests, both
`--check` legs and both battery readings are green.

## 1. Design dependency: one minute late, then conformed

### 1.1 Poll record

`reports/round-11/depth/design.md` landed at **22:06:15Z**; this seat's last
poll (60 s cadence) was **22:05:24Z**, when the depth directory held only
`scribe.md`, `review-22.md`, `capability-draft.md`, `test-cli.md`,
`test-determinism.md`, `test-interop-d3.md` — each explicitly deferring its
wired-state sections. The integrator therefore built a first-pass wiring on
measured evidence (22:07–22:15Z), certified it (`reports/round-11/run-validation.py`
recorded **claim D: PASS** at 22:19Z), and then found `design.md` had landed.

### 1.2 Conformance pass (22:20–22:28Z)

`design.md` §2–§5 fixes names and mechanisms the first pass did not match:
the adapter is `tools/assemble-d2-typed.py` (§2.2), the entry is a gate-shaped
`tools/gates/typed-pipeline-gate.py` so `replay-frozen.py` can pin it (§3.1),
the routing mechanism is a **field move** (`garment` → `garment_gloss`; "adding
typing fields cannot exempt a string", §2.3 T1 row 6), the baseline is
`examples/culture-d2/expected-holds.json` with `where = GAR-01..GAR-10` (§4.5,
§4.4), and the freeze pins the typed run as a replay row (§5.2). The conformance
pass rebuilt the wiring to that shape and retired the first-pass files. The
first pass's independent value is kept as a cross-check: it used `compare_only`
(routing by flag) and reached the same net effect — the same ten records off the
channel, the same ten holds — which is evidence that neither mechanism relies on
the other's side effects.

### 1.3 Deliberate deviations from the design, each flagged

| # | design says | landed | why |
|---|---|---|---|
| 1 | the build product "can never rot in `examples/`" (§2.2 note 3) | `examples/culture-d2/packet.d2.typed.yml` is committed and byte-pinned by `assemble-d2-typed.py --check` | a committed, byte-compared build product makes the freeze copy verifiable and the review surface local; rot is caught by the `--check` leg (run in §8). Reviewers may weigh this against the design's rationale |
| 2 | freeze record under `tools/gates/expected/typed-pipeline/r11/` with an `expected.json` (§5.2) | `tools/gates/frozen/round-11/typed-pipeline/` with `run-receipt.json` | `tools/check-gate-battery.py` discovers every `expected.json` under its roots and fails closed on a gate outside its seven-name constant; an `expected.json` naming the new gate would flip the battery's standing reading (5 pinned / 2 uncovered) into a `BASELINE-GATE-UNKNOWN` finding. Changing the battery to bless the new gate is exactly the checker co-change (review-22 pattern C4) this round audits — refused and reported instead |
| 3 | no receipt in the design's file map | `reports/round-11/depth/e2e-receipt.json` (§7) | the round's runner (`reports/round-11/run-validation.py`) measures claim D's e2e clause from a machine-readable receipt or a `design.md` expected-holds block; the design landed too late to carry one, so the integrator landed the receipt in the runner's own vocabulary |
| 4 | — | the receipt omits `owed_native_forms` | the runner's optional owed-form check requires an owed id to appear as a hold token (head/tail), while design §4.4 keys the hold set on `(id, severity, where)` with `where = GAR-01..GAR-10`; the two vocabularies cannot both hold and the design is the authority. The owed slots stay named in the typed packet's routing rows (`label_id`, `owed_slot`), in every hold's detail, and in the gate's `L3-routing-consistency` leg |

## 2. The wiring, end to end

```
components/ (9 files in examples/culture-d2/components)
  │  tools/assemble-d2.py                     [byte-frozen: the D3 packet pins its sha]
  ▼
examples/culture-d2/packet.d2.yml             (raw packet, committed, --check green)
  │  tools/d2-typed-labels.py                 [unchanged; re-pinned, §6.1]
  ▼
examples/culture-d2/typed-labels.d2.yml       (typed projection)
  │  tools/assemble-d2-typed.py               [NEW adapter — typed labels enter here]
  ▼
examples/culture-d2/packet.d2.typed.yml       (typed packet: routing table + moved field + findings)
  │  tools/gates/typed-pipeline-gate.py       [NEW gate-shaped entry: L1-L4]
  ▼
exit 0  ⇔  findings == examples/culture-d2/expected-holds.json exactly
```

`assemble-d2.py` stays byte-frozen (`8ea6bdde…`) because its whole-file digest is
embedded as `serializer_sha256` in the D3 packet (R11-D15 Probe A measured that
any byte change reds the D3 `--check`). The integration therefore lives in the
adapter, exactly as the design's §2.1 places it.

## 3. The contract, measured

### 3.1 Adapter (`tools/assemble-d2-typed.py`, sha256 `c7e5a749…`)

`[--packet P] [--projection J] [--emit PATH] [--check [PATH]] [--selftest]`,
fail-closed as designed: assembler identity and projection freshness exit 2 (the
projector's own pipeline must reproduce the committed projection byte-for-byte,
and the projection must pin this packet's digest), coverage exits 2 (an untyped
`garment` record is a problem, a routing row for a missing record is a problem),
`--check` drift exits 1. Output: the packet's blocks plus `typed_channel` (§3.2),
`typed_assembly` (rules), `assembly` (packet/projection/adapter digests) and
`pipeline_findings` + `pipeline_counts` carried verbatim.

### 3.2 The routing table — the ten rows, exactly

Ten rows, all `translated-label / to-verify`, all `11-costumes.yml` field
`garment` → `garment_gloss`, `channel: off-sound-and-identity`, `hold:
D2L-FORM-UNRESOLVED`, each naming `label_id`/`owed_slot` `LEX-GAR-01`..`LEX-GAR-10`
for records `GAR-01`..`GAR-10`. Nothing else is routed: the 46 supplied native
forms and the 2 supplied loans stay on the checked channel, which is why the
channel differential is exactly ten lines (measured, §8).

### 3.3 Entry (`tools/gates/typed-pipeline-gate.py`, sha256 `d102fd1d…`)

`[PACKET]` (default `examples/culture-d2/packet.d2.yml`), `--selftest`, `--json`.
Legs L1 build / L2 channel / L3 holds / L4 pins (design §3.1), plus the
integration's own `L3-routing-consistency` leg (holds ↔ routing rows ↔ owed
slots, the D18 defence). Exit 0/1/2 per the design's table. stdout: the banner,
**15 `FINDING` lines** and **1 `NOTE` line** (the note is emitted as `NOTE`, so
the frozen row's `finding_count` is the design's 15), then the leg verdicts. A
typed packet handed in directly (as the frozen replay row does) is graded as the
build product: L2 reconstructs the legacy packet from the moved fields.

### 3.4 The expected hold set — every hold named (design §4.2/§4.3, verbatim)

| # | id | severity | where | source |
|---|---|---|---|---|
| 1-10 | `D2L-FORM-UNRESOLVED` | hold | `GAR-01`..`GAR-10` | the ten owed slots `LEX-GAR-01..10` (`11-costumes.yml` `form_slot`, each `(to-verify)`; `05-lexicon.yml` supplies none) |
| 11-12 | `D2L-NATIVE` | hold | `L-15`, `L-16` | supplied `sára`/`sará`: the acute accent is declared by `02-phonology.yml:73`'s own minimal pair, held for the form's owner |
| 13-15 | `D2L-RANK` | hold | `TR-04#a\|TR-06#a`, `WR-02#g\|WR-09#g`, `WR-08#g\|WR-09#g` | genuine priority gaps from the rank adapter |
| note | `D2L-RANK` | note | `SR-01#a\|SR-01#b` | band-keyed pair, pinned and **not** counted as a hold |

Fail set: **∅**. Counts `{hold: 15, note: 1, fail: 0}`. Committed at
`examples/culture-d2/expected-holds.json` (sha256 `a5dc26d5…`) together with the
packet/projection/projector pins; the gate embeds the same set as
`EXPECTED_HOLDS`/`EXPECTED_NOTES` and its `--selftest` asserts the constant
equals the file in both directions. Details are pinned too (design §4.4(3)) —
the D19 laundering channel is closed by exact `detail` comparison.

## 4. The frozen re-pin (design §5.2)

`tools/gates/frozen/round-11/` (new generation; `MANIFEST.tsv` sha256
`aad230bf…`), 11 rows: the typed-pipeline gate over the frozen build product
(exit 0, 15 findings), the five legacy gates over the typed packet, the same five
over the raw packet. The naming pair is the differential on the record: 17 → 7
findings, the ten `PHON-*` lines exactly, nothing added.

```sh
TMPDIR=/var/tmp/kotodama-r11 python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv
# REPLAY OK: 11/11 rows reproduced the recorded verdicts
```

Rows 2 and 7 reproduce `exit_code 1`: a reproduced red verdict stays red. The
round-3 generation stays **exit 2, 7/7 `gate_digest_mismatch`** — its pins name
the pre-repair gate bytes and rounds 8–9 legitimately repaired the gates
(recorded standing state, and `design.md` §5.3 says not to rewrite those pins).
The five `r9-pre` baselines still pin (battery, §8). Supporting records:
`typed-pipeline/run-receipt.json` (`kotodama-frozen-run-v1` pins: gate hash,
input digests, tool pins, hold ids, `stdout_sha256`), `run.log`, `freeze.txt`;
`expected.json` is deliberately absent there (§1.3 row 2). Re-run recipe: `TMPDIR`
must be outside the repo — `replay-frozen.py` refuses in-repo mirrors by design.

## 5. Green legs (final tree, 2026-10-17 22:27Z)

| leg | command | result |
|---|---|---|
| e2e | `python3 tools/gates/typed-pipeline-gate.py` | exit 0, 15/15 legs, 15 FINDING + 1 NOTE |
| e2e (machine) | `python3 tools/gates/typed-pipeline-gate.py --json` | exit 0, 16 findings, `translated_on_sound_channel` 0 |
| entry selftest | `… --selftest` | exit 0, 12/12 (constant==baseline, smuggle, dropped row, laundered hold, adapter drift, malformed, missing) |
| adapter | `python3 tools/assemble-d2-typed.py --check` / `--selftest` | exit 0 / 11/11 |
| assembly | `python3 tools/assemble-d2.py --check` / `--selftest` | exit 0 / 42/42 |
| projector | `python3 tools/d2-typed-labels.py --check` / `--selftest` | exit 0 / 39/39 |
| D3 interop | `python3 tools/assemble-culture-d3.py --check` / `--selftest`; `check-evidence-coupling.py --frozen` | exit 0 / 85/85; exit 0, 0 findings |
| replay | `replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` | exit 0, 11/11 reproduced |
| battery | `python3 tools/check-gate-battery.py` / `--selftest` | standing exit 2, pass 7 / fail 0, 5 pinned + 2 uncovered (unchanged), originals preserved / 28/28 |

## 6. Integration steps, in order, with evidence

### 6.1 Re-emit the stale projection (round-10 A2; design §5.1)

`typed-labels.d2.yml` recorded `assembly.packet_sha256` `8da90b07…` while the
packet hashes `e0f21509…`. Re-emitted with the owning tool:
`python3 tools/d2-typed-labels.py --emit examples/culture-d2/typed-labels.d2.yml`
(exit 1 — findings; the report is complete), then `--check` → exit 0.
`e70ba147…` → `a3aa452c…`, exactly one line changed (the pin), matching
R11-D24's prediction and `design.md` §5.1's predicted hash `a3aa452c…` exactly.

### 6.2 First-pass wiring (before design.md was found), then conformance

Built `tools/typed-gate-flow.py` (adapter+entry in one tool; `compare_only`
routing), verified it (10/10 checks, 16 findings, differential exact, frozen
replay 10/10 — the runner's 22:19Z **claim D: PASS** cites that receipt
revision), then rebuilt to the design's shape:
`tools/assemble-d2-typed.py` + `tools/gates/typed-pipeline-gate.py` +
`expected-holds.json`, field-move routing, and sent the typed-pipeline gate
through the freeze row. The first-pass files were deleted in the same pass.

### 6.3 Freeze and replay

`.scratch/d05/freeze-r11.py` (uncommitted recipe, steps in `freeze.txt`) wrote
the generation and the 11 rows; replay reproduced 11/11 (§4).

### 6.4 Receipt

`reports/round-11/depth/e2e-receipt.json` was regenerated from a fresh
`--json` run of the entry; it pins that stdout's sha256 (`19765ddf…`).

## 7. The e2e receipt — why this seat landed it

`reports/round-11/run-validation.py` measures the D e2e clause from (a) a JSON
receipt under `reports/round-11/**` with a command + expected holds, (b) a
`tools/*.py` flow exposing `--e2e`/`--flow` paired with a `design.md`
expected-holds block, or (c) an e2e command line in `design.md`. The entry is
gate-shaped (under `tools/gates/`, so (b)'s glob over `tools/*.py` does not even
see it) and `design.md` carries no expected-holds JSON block, so the receipt is
the path the runner can use. It pins: the command, exit 0, the 16 findings as
`expected_holds` and `findings`, the 10 routing rows, the three pins, the five
gate verdicts, the channel counts, and the stdout hash. **Flag for the parent:**
if a design-authored receipt or expected-holds block lands later, prefer it and
keep this file only as the integrator's evidence; the numbers are the same.

## 8. Anticipated adversarial reviews, answered

- **C2 tautological pin / C5 verdict rewrite**: the freeze row for the typed run
  pins the *pre-change* evidence too — rows 2–11 grade the raw packet (the
  before-state), so a change that moved the retained channel would break the
  replay instead of blessing itself. The recorded `exit_code 1` rows stay red.
- **C6 self-issued exemption**: the off-channel decision is read from the
  projector's kinds (an independent tool, sha-pinned), and L2 validates the
  result against the *gates' own* stdout: zero typed-run line may name a routed
  record, and the legacy-minus-typed difference must be exactly the ten
  `PHON-*` lines. The smuggle control restores a moved field and L2 fails.
- **C1 harvested expectation**: the hold set's independent groundings are (a) the
  ten `form_slot` declarations in `11-costumes.yml` (the owed slots exist in the
  component, not only in the pipeline), and (b) the channel differential (the ten
  artifacts that leave the gates' output are the same ten records the routing
  table moves). The routing-consistency leg ties holds ↔ rows ↔ slots in both
  directions; the dropped-row control proves the tie can fail.
- **Hold-set completeness**: all 15 holds + the note are emitted; the note is
  emitted as a `NOTE` line so it cannot inflate the finding count, and L3 checks
  the note set separately — a hold laundered into a note fails.
- **Circularity of the re-pin**: the freeze record is written from an observed
  run, but the expectation it is compared against is the *committed* baseline
  (§3.4) and the gate's embedded constant; the selftest asserts constant ==
  baseline in both directions, so a re-pin that quietly edited either would be
  visible as a mismatch against the other. The generation adds no `expected.json`
  under the battery's roots (§1.3 row 2).

## 9. Limits and open items

1. **Committed build product** (deviation 1): if the parent prefers the design's
   "regenerated only" rule, delete `examples/culture-d2/packet.d2.typed.yml`,
   point the legacy rows' `input`/`input_snapshot` at the frozen copy, and keep
   the adapter's `--check` against the frozen copy — no other change is needed.
2. **Freeze-record placement** (deviation 2): moving `run-receipt.json` to
   `tools/gates/expected/typed-pipeline/r11/expected.json` requires deciding
   whether `check-gate-battery.py` should learn the new gate; that is a battery
   co-change and was deliberately not taken.
3. **`--json` purity**: `--json` prints one JSON document and no human lines;
   the banner and hold lines are the non-JSON mode's (both pinned).
4. **Other seats' worktree writes, reported not absorbed**: at 22:27Z `git status`
   shows modified *filed* artifacts not written by this seat
   (`reports/round-{5,6,7,8,9}/validation.json`,
   `reports/round-10/coverage/index-update-22.md`), plus concurrent round-11
   fragments by other seats. The `typed-labels.d2.yml` rewrite (§6.1) is
   regenerated tool output, not a filed report.
5. **Nothing here is clearance, canon or handoff** (`PROVINCE.md`): the typed
   packet is a derived, non-canon gate-facing view; the holds stay owed; the
   world-bible handoff is untouched.
6. `to-verify`: whether the acceptance run should cite the human or the `--json`
   form of the entry (both exit 0; the receipt pins the JSON form).
7. **Test fragments measured the retired first-pass tool.** Several `depth/*.md`
   fragments cite `tools/typed-gate-flow.py` with line locators
   (`test-e2e.md`, `test-replay.md`, `frozen-records.md`, `repin.md`,
   `neg-17/18/19.md`, `review-20/21/22/23.md`, `scribe.md`, `capability-draft.md`,
   `test-cli.md`, `test-determinism.md`, `test-boundary.md`, `test-battery.md`,
   `test-differential.md`, `shard-*.md`) — that file existed 22:07–22:20Z and was
   retired in the conformance pass (§1.2), so those line references no longer
   resolve. The *semantics* they measured (16 findings = 15 holds + 1 note, the
   ten-artifact differential, tamper/malformed controls) are re-established on
   the landed tools and re-verified in §8; but the receipts' subject is a retired
   revision, and re-dispatching the test seats against
   `tools/assemble-d2-typed.py` + `tools/gates/typed-pipeline-gate.py` is the
   parent's call. Fragments that cite the design's names
   (`shard-gate-adapter.md`, `review-23.md`, `neg-18/19.md`) match the landed
   files.

## 10. Receipts

```sh
# 2026-10-17 22:0x-22:2xZ, lane root, TMPDIR=$PWD/.scratch unless noted
python3 tools/d2-typed-labels.py --emit examples/culture-d2/typed-labels.d2.yml   # exit 1 (findings), re-pin
python3 tools/d2-typed-labels.py --check                                          # exit 0
python3 tools/assemble-d2-typed.py --emit examples/culture-d2/packet.d2.typed.yml # exit 0, 10 routing rows
python3 tools/assemble-d2-typed.py --check                                        # exit 0
python3 tools/assemble-d2-typed.py --selftest                                     # exit 0, 11/11
python3 tools/gates/typed-pipeline-gate.py                                        # exit 0, 15/15 legs
python3 tools/gates/typed-pipeline-gate.py --json                                 # exit 0 (receipt source)
python3 tools/gates/typed-pipeline-gate.py --selftest                             # exit 0, 12/12
python3 .scratch/d05/freeze-r11.py                                                # 11 rows written
TMPDIR=/var/tmp/kotodama-r11 python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv
                                                                                  # exit 0, REPLAY OK 11/11
python3 tools/assemble-d2.py --check; python3 tools/assemble-d2.py --selftest     # 0; 42/42
python3 tools/d2-typed-labels.py --check; python3 tools/d2-typed-labels.py --selftest   # 0; 39/39
python3 tools/assemble-culture-d3.py --check; python3 tools/assemble-culture-d3.py --selftest  # 0; 85/85
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json  # 0
python3 tools/check-gate-battery.py; python3 tools/check-gate-battery.py --selftest  # standing exit 2; 28/28
python3 reports/round-11/run-validation.py                                        # see §0/§11 note
```

Digests (2026-10-17T22:27Z):

| artifact | sha256 |
|---|---|
| `tools/assemble-d2-typed.py` | `c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071` |
| `tools/gates/typed-pipeline-gate.py` | `d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d` |
| `examples/culture-d2/expected-holds.json` | `a5dc26d5b495a90e05ce42d4d8b6d08f047359c377e458f9190b1d310d6dde3a` |
| `examples/culture-d2/packet.d2.typed.yml` | `1b5010b7f449ec78755e9a8b0efea62c705af7ec5c592ceda6cf2c072dfac8a3` |
| `examples/culture-d2/typed-labels.d2.yml` (re-emitted) | `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | `aad230bfdcc1bfe4cc137339b47daf0154208b6c69225e0c0a4505ce52532063` |
| `tools/gates/frozen/round-11/typed-pipeline/run-receipt.json` | `c49ebc9e71ce870af621604bb0e00886b45ad8f4028777f202ec845ede6cc902` |
| `tools/gates/frozen/round-11/typed-pipeline/run.log` | `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606` |
| `reports/round-11/depth/e2e-receipt.json` | `4adc90a2ca4b8df0e92bf15b1b442f4d85003461dbce5bbdb5aafca058b0c095` |
| `tools/assemble-d2.py` (untouched) | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` |
| `tools/d2-typed-labels.py` (untouched) | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` |
| `examples/culture-d2/packet.d2.yml` (untouched) | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` |
| `tools/gates/naming-collision-gate.py` (untouched) | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |

## 11. Sources

Repo-relative, read/re-run 2026-10-17 22:00–22:28Z: `reports/round-11/claims.json`
(claim D), `reports/round-11/targets.json` (R11-D03..D08), `reports/round-11/depth/
design.md` (§2–§5, §7), `{scribe,capability-draft,review-22,test-interop-d3,test-cli,
test-determinism}.md` (same directory), `reports/round-8/depth/{design-spec,
skill-table-draft,test-replay}.md`, `reports/supplement-opencode-1/22-label-representation.md`,
`examples/culture-d2/{ASSEMBLY.md,components/11-costumes.yml,components/05-lexicon.yml,
components/02-phonology.yml}`, `tools/gates/naming-collision-gate.py` (`:223`,`:1148-1190`),
`tools/gates/costume-era-consistency-gate.py` (`:1109-1121`),
`corpus/knowledge/verification/gate-frozen-run-standard.md`, `PROVINCE.md`, `AGENTS.md`.
