# R11-D18 — negative: an owed native form dropped silently (run receipts)

- round: 11 · shard: D18 (negative examples, claim D `d2-typed-pipeline`) ·
  owner: L2 worker, kotodama-shokunin lane
- date: 2026-10-17 (UTC stamps below; local = UTC-3)
- baseline revision: `94ca098b8ab03be52ec80f6925538e5e2c0ed327`
  (`reports/round-11/claims.json:5`); working-tree HEAD at write time `e3ef171`
- assignment (verbatim): "DEPTH R11-D18 (negative): drop an owed native form
  silently; wiring must carry the hold; reports/round-11/depth/neg-18.md."
- canon: NON-CANON engineering evidence. Nothing here is a culture design, a
  canon record, a handoff or a real-world claim.
- files written by this shard: **this file only**. The drop fixtures are not
  filed as committed artifacts (the assignment names one path; the hard rule is
  literal). §7 regenerates every fixture byte from the live tree, so the
  negative is reproducible without those bytes being filed.
- scratch: `.scratch/neg18/**`; `export TMPDIR=$PWD/.scratch` preceded every
  scratch-writing command (`/tmp` is inode-exhausted on this host).
- status: **complete.** Pre-wiring receipts (§3–§4) and the wiring re-run (§6,
  against the landed `tools/typed-gate-flow.py` at 22:19–22:25Z) are both filed.
  Headline: the drop is never silent, but the landed flow catches it through the
  pinned baselines, not through an obligation-derived hold — §6 states exactly
  what fired, per injection, with hashes and stamps.

## 1. The defect, in one paragraph

In the D2 example ten costume records own a form slot that **owes** a native
form (LEX-GAR-01..10; `examples/culture-d2/components/11-costumes.yml:214-403`,
slots at `:407-416`). Their only supplied string is an English display gloss
(the `garment` field); no native bytes exist anywhere. The correct pipeline
behaviour, fixed in round 8 and re-adopted by round-11 claim D, is: the
translated label never enters the sound channel **and** the owed form is carried
as a named hold (`D2L-FORM-UNRESOLVED`, round-8 `design-spec.md` §1.3 R3, §1.5;
`reports/supplement-opencode-1/22-label-representation.md:125-135` rule 2,
controls C1/C1b at `:141`). The failure this negative exercises is the mirror of
C1b's own sentence ("the artifact is removed without clearing the real gap",
`22-label-representation.md:150-152`): **the record's display string is dropped
while the debt stands, and the flow goes silent about the debt.** A pipeline
whose hold is derived from the *label row* loses the hold when the row is
deleted; a pipeline whose hold is derived from the *slot obligation* (the
`form_slot` a record still declares) carries it. The round-8 projection
(`tools/d2-typed-labels.py`) is the former — §3 proves the silence — and the
supplement's adapter prototype (`adapter-prototype.py:71`) is the latter — §4
proves the design precedent catches it. The wiring must match the precedent.

## 2. The drop family (fixtures, byte-pinned)

All fixtures are derived from the live tree at 2026-10-17T22:05Z by
`.scratch/neg18/build-fixtures.py` (§6), byte-deterministically.

| case | artifact | mutation | sha256 |
|---|---|---|---|
| fx18a | packet copy | GAR-01 `garment` (display label) dropped; `form_slot` kept | `0ec39b63c08a50434ff84dd24fed0edaf98d03ee977b255b5747b2617fd488ad` |
| fx18b | packet copy | GAR-01 `form_slot` dropped; `garment` kept (anti-regression control) | `87802330843ceb43b50c7337a586061028fb43b9527cf7210fc8a7836e835abf` |
| fx18c | packet copy | both dropped | `06484fa33caed4870b3686df39046cae40434c2f01fd730bce40bfaf8070f766` |
| fx18d | projection copy | self-consistent drop of the GAR-01 row: label row, its hold finding and the affected counters removed; packet stays live | `2800d89c9b86e2e11472135e051a37bb3838abf4b5030f9c2da53bdabef63cbd` |

Source bytes these fixtures pin against: `examples/culture-d2/packet.d2.yml`
sha256 `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643`;
`examples/culture-d2/typed-labels.d2.yml` sha256
`e70ba1477dbeb830061db6fd12516b7d902587bddae173f55a3650015d380b2f`
(`sha256sum`, 2026-10-17T22:05Z).

fx18a is the claim-bearing case: the record still declares
`form_slot: "LEX-GAR-01, the valley grade of L35 mirken (to-verify with
05-lexicon)"` (`packet.d2.yml:1850-1852` in the live file) — the debt is live
data; only its display string was removed. fx18d is the wiring-facing version:
the projection that the wired flow is meant to consume is doctored to look
internally consistent while one owed form disappears from it.

## 3. Pre-wiring receipts — both live channels are silent on fx18a

Commands (lane root, TMPDIR set; run 2026-10-17T22:05Z, tool hashes below):

```sh
python3 tools/d2-typed-labels.py --packet <fixture> --json
python3 tools/gates/naming-collision-gate.py <fixture>
python3 .scratch/neg18/probe-prototype.py     # supplement adapter prototype branch
```

| case | `d2-typed-labels.py` | legacy `naming-collision-gate.py` |
|---|---|---|
| baseline (live packet) | exit 1, holds 15, GAR-01 = `D2L-FORM-UNRESOLVED:hold`, labels 58 | exit 1, 17 FINDINGs, GAR-01 `PHON-INVENTORY: FAIL` present |
| **fx18a** | exit 1, **holds 14**, **GAR-01 = NONE** (silent), labels 57 | exit 1, 16 FINDINGs, **GAR-01 `PHON-INVENTORY` gone** (silent) |
| fx18b | exit 2, holds 15, GAR-01 = `D2L-DATA:fail` + `D2L-FORM-UNRESOLVED:hold` | GAR-01 `PHON-INVENTORY` still present |
| fx18c | exit 1, **holds 14**, **GAR-01 = NONE** (silent), labels 57 | GAR-01 `PHON-INVENTORY` gone (silent) |
| fx18d | not consumable by this tool (it only byte-compares: `--check` over fx18d → exit 1, "differs from the deterministic projection") | not consumed |

Two verbatim lines from the fx18a sweep:

```text
fx18a  typed_exit=1 holds=14 GAR-01-findings=NONE-silent | gate_exit=1 GAR01-PHON=0
fx18c  typed_exit=1 holds=14 GAR-01-findings=NONE-silent | gate_exit=1 GAR01-PHON=0
```

(`.scratch/neg18/probe-standalone.py` output, 2026-10-17T22:05:56Z.)

Sweep of every committed D2 gate over fx18a (each gate run over
`.scratch/neg18/fx18a/packet.yml`, `grep -c`, 2026-10-17T22:08Z) — the
"nothing else names the record" claim is this sweep:

| gate | exit | FINDINGs over fx18a | GAR-01 mentions |
|---|---|---|---|
| `costume-era-consistency-gate.py` | 0 | 0 | 0 |
| `lexicon-coverage-audit.py` | 0 | 0 | 0 |
| `myth-consistency-gate.py` | 0 | 0 | 0 |
| `naming-collision-gate.py` | 1 | 16 (live packet: 17) | **0** (live packet: the GAR-01 `PHON-INVENTORY` line) |
| `phonology-sanity-gate.py` | 1 | 3 (live packet: 3) | 0 |

Why the tool loses the hold: its per-costume label row is built from the
`garment` string (`tools/d2-typed-labels.py:493 def _costume_label`), and the R3
hold is emitted from that row's `label_id` (:791-796). Delete the row and the
hold disappears — the "double silence" fx18a demonstrates: the typed channel
loses the hold and the legacy channel loses the artifact FAIL, and nothing
else names the record.

## 4. The design precedent does carry it (and the current tool does not)

The supplement's adapter prototype routes the same records by the **slot**,
not the label (`reports/supplement-opencode-1/scratch/22-label-representation/
adapter-prototype.py:71`, `if "form_slot" in rec:` → label popped from the
sound channel, `FORM-UNRESOLVED` hold appended), with its own 7/7 control
matrix green. Sweep (`.scratch/neg18/probe-prototype.py`,
2026-10-17T22:05Z; prototype sha256 `9fe01335d8bb526c08d81c92ccf3f4f2ebd5899d1f7b8e02123ae3d0b86425a8`):

| case | prototype result |
|---|---|
| baseline | `inv=0 FORM-UNRESOLVED=10 exit=1`, GAR-01 named by a hold |
| **fx18a** | `inv=0 FORM-UNRESOLVED=10 exit=1`, **GAR-01 named by a hold — caught** |
| fx18b | `inv=1 FORM-UNRESOLVED=9`, GAR-01 back on the sound channel as a FAIL (red, but via the wrong channel) |
| fx18c | `inv=0 FORM-UNRESOLVED=9`, GAR-01 named nowhere — silent there too |

So fx18a is not a hypothetical: it is the case that separates the two trigger
designs (`label_id`-carried hold vs `form_slot`-carried hold) that are both
present on disk today. Round-8's own R3 text wants the slot-carried hold —
"If the owning record supplies no `status: supplied` native/borrowed form, emit
`D2L-FORM-UNRESOLVED` HOLD — never a silent pass"
(`reports/round-8/depth/design-spec.md` §1.3 R3) — and the round-8 tool carries
the hold only through the label row, which is why the drop works on it.

## 5. Acceptance contract for the round-11 wiring (mechanism-keyed)

The wiring design landed while this shard ran: `reports/round-11/depth/design.md`
sha256 `addd0ea2ecf71871621814aa5917347ae6503d0040bcf64c31cae0f4baa69c49`
(read 2026-10-17T22:07Z). It fixes the mechanism — adapter `tools/assemble-d2-typed.py`
(checks: assembler identity, projection freshness, coverage, determinism; §2.2)
feeding `tools/gates/typed-pipeline-gate.py` (legs L1–L4; §3.1) — and its §6
table names D18's intended catches verbatim: "adapter that omits a routing row /
a hold for a `translated-label` with no supplied form → adapter coverage check
(§2.2) **and** L3 … if it got past the adapter, the hold count drops to 14 → L3
mismatch". The acceptance below keys every injection to the leg that must catch
it; per design §6's own rule, a red for an unrelated reason does not count as a
pass — the asserted line/set difference must name the dropped obligation.

| injection | drop sits in | must be caught by (design leg) | asserted difference |
|---|---|---|---|
| I1 — adapter omits the GAR-01 routing row | adapter output (build product) | §2.2 coverage (`routed ≠ typed off-channel`) → exit 2; fallback L2 (a typed-run line still names an off-channel record) | coverage line naming GAR-01, or a typed-run sound/identity line naming GAR-01 |
| I2 — adapter keeps the row, omits or downgrades its hold | adapter output | L3 (hold count 14 ≠ 15, or a note appearing in the hold set) → exit 1 | hold-set difference naming GAR-01 |
| fx18a — `garment` dropped, `form_slot` kept | packet input | freshness (`d2-typed-labels.py --check` no longer reproduces) → exit 2, or L3 (hold 14) → exit 1 — **never exit 0** | refusal naming the non-reproducing projection or the missing GAR-01 hold |
| fx18d — GAR-01 row+hold+counter drop, internally consistent | projection input | freshness (byte-compare) → exit 2 | freshness line naming the projection |
| fx18b — `form_slot` dropped, `garment` kept | packet input | non-silent refusal (the round-8 tool's `D2L-DATA`/exit 2 is the floor) | any refusal naming GAR-01; never a pass |
| fx18c — both dropped | packet input | completeness only — outside this negative's claim (§8) | — |

Reading of the claim: for fx18a/fx18d the *weakest acceptable* outcome is a
fail-closed refusal that names the dropped obligation or the artifact that fails
to reproduce (exit 2, design §3.2 could-not-evaluate). Exit 0 with 9 GAR holds —
or a typed run whose only GAR-01 line is a sound-channel artifact — is the
escaped defect this negative exists to catch. I1/I2 are adapter-boundary
injections rather than filed fixtures (the build product is generated inside the
gate's temp mirror, design §3.1 L1) and are stated here as the black-box
equivalent of the design's own D18 sentence: they are `to-verify` until the
wiring exists to run them, and the run receipt must record which leg actually
fired.

The assembler shard's landed fragment (`reports/round-11/depth/shard-assembler.md`
sha256 `ddd7ede619007ef6946588cb0fed5410a242218d8a3a18f0c23b5e589ec27725`,
read 2026-10-17T22:11Z) sharpens the expected diagnostics with its own scratch
receipts (`:153-157`): a non-assembly packet is refused with "is not
assemble-d2.py's deterministic assembly" (the fx18a catch, since the packet is a
build product of the components and hand-edits to it cannot pass identity); a
hand-edited projection is refused with "is not reproduced byte-for-byte by
tools/d2-typed-labels.py" (the fx18d catch). The same fragment states honestly
(`:42`) that its coverage "row set == typed off-channel set" comparison is true
by construction, so the load-bearing teeth are identity, freshness,
field-presence and L3 — the chain this negative asserts, with each line naming
the dropped obligation. The holds shard's fragment
(`reports/round-11/depth/shard-holds.md`
sha256 `8efb4c31f302d8ac715a7b0c8c99fc1b7991e3fed2bc1af2bba70a00659bb8b5`,
read 2026-10-17T22:14Z) independently re-derived the same 15-hold/1-note/0-fail
set from the live projector and states the D18 signature directly: "dropping one
drops the count to 14" (`:89`) — the fx18a/fx18d refusal exists precisely so that
count can never quietly become 14. One residual the chain leaves open is named
here, not absorbed: a projector-side drop that re-pins the projection and edits
nothing else falls to L3's hold count (14 ≠ 15), and a drop that *also* re-pins
the expected-holds baseline is the circularity attack owned by D22/D23.

**Landed outcome (22:19–22:25Z, §6 has the receipts):** the flow landed as
`tools/typed-gate-flow.py` with no `--projection` adapter leg, so the "freshness"
row above never existed as such; fx18a/fx18c are refused by the *pinned-expectation*
comparisons (`hold-set-equal — observed 15 findings, expected 16` and the pins),
with every substantive check passing — i.e. the flow refuses the drop but does
not carry the hold for it. ov1/ov2 rows were added by the landed flow's own
`--typed-override` surface; their outcomes are in §6's table. The acceptance
*meaning* is unchanged: a run that returns 0, or silently short of the GAR-01
hold without naming the difference, is the escaped defect.


## 6. Wiring re-run — receipts against the landed flow

The wiring landed under different names than `design.md` planned: **`tools/typed-gate-flow.py`**
(sha256 `5758e315593bb818dbf38c3c3ed7f79eb9ea555955331fadab4b50b2faa92075`,
19:18 −0300), with the projection re-pinned (`examples/culture-d2/typed-labels.d2.yml`
`a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`,
`--check` exit 0) and committed artifacts `packet.d2.typed.yml`,
`typed-gate.expected.json`, `tools/gates/frozen/round-11/`. `tools/assemble-d2-typed.py`
and `tools/gates/typed-pipeline-gate.py` were never created; the flow derives the
typed packet in-process from the live packet + projector run
(`tools/typed-gate-flow.py:294-345`) and has no `--projection` input. The two
commands my window polled for therefore never existed — the naming mismatch is
recorded here rather than treated as absence.

Hashes and verdicts, each stamped (`sha256sum`, lane root, `TMPDIR=$PWD/.scratch`):

| stamp (UTC) | `tools/typed-gate-flow.py` | committed typed packet | verdict of the live pair |
|---|---|---|---|
| 22:19:xx | `5758e315…` | `e8a83445…` (then committed) | **exit 0, 10/10** — 15 holds + 1 note, sound channel off=GAR-01..10 on=0 |
| 22:25:21 | `5758e315…` | `1b5010b7f449ec78755e9a8b0efea62c705af7ec5c592ceda6cf2c072dfac8a3` | **exit 1, 9/10** — `FAIL typed-packet-pinned — derived typed packet differs from examples/culture-d2/packet.d2.typed.yml` (derivation hashes `e8a83445…`, carries `typed_view`; the committed file carries `schema: kotodama-typed-packet-v1` + `typed_channel` rows + `adapter_sha256 c7e5a749…` — two shapes / two generators). Reported to the parent as a live integration inconsistency, not absorbed. |

Fixture runs (same tool sha; fixture hashes in §2; `python3 tools/typed-gate-flow.py --packet <fixture>`):

| injection | exit | catching checks (verbatim) | substantive catch (non-pin)? | is the GAR-01 hold carried? |
|---|---|---|---|---|
| **fx18a** | 1 | `FAIL typed-packet-pinned`; `FAIL hold-set-equal — observed 15 findings, expected 16`; `FAIL expected-pins`; `FAIL expected-delta-match`; `FAIL expected-file-current` | **no** — `no-untyped-records`, `sound-channel-clean`, `differential-exact`, `owed-slots-crosscheck` all pass | **no** — the flow's own finding set has 14 holds; GAR-01 is named nowhere (`off=GAR-02..GAR-10`, `untyped=none`) |
| fx18b | 1 | `FINDING D2L-DATA: [fail] GAR-01 — costume label carries no label_id for its form slot` + GAR-01 hold; pins also fail | yes (named `D2L-DATA`) | yes |
| fx18c | 1 | same shape as fx18a (`observed 15 findings, expected 16`) | **no** | **no** |
| **ov1** — committed typed packet with GAR-01's `typed_channel` row deleted **and** the gloss restored onto the checked field, via `--typed-override` | 1 | `FAIL sound-channel-clean — PHON artifacts naming translated labels: [… GAR-01 'winter valley coat …']`; `FAIL differential-exact — removed 9, off-records 10`; pins | **yes** (channel + differential) | holds ride from the derivation (15) |
| **ov2** — the same row deletion but the gloss left (off-channel in effect, undeclared) | 1 | `FAIL expected-pins`; `FAIL expected-file-current` (8/10) | **no** — channel, differential, hold-set and owed-slots checks all pass | yes (from the derivation) |

What the receipts establish, stated without overclaiming:

1. **The drop is never silent in the landed flow.** Every fx18a-family run exits 1
   and names a difference; the round-8 double silence (§3) is gone.
2. **The hold is not carried for fx18a.** The flow's finding set is derived from
   the projector's label row (`typed-gate-flow.py:144-190` routes records the
   projector typed; a costume record with neither a typed label nor a `garment`
   is neither off-channel nor flagged `untyped`), so deleting the gloss deletes
   the hold — and every *substantive* check is blind to that (differential,
   sound-channel, owed-slots and untyped checks all pass) because they compare
   the derivation against itself. The refusal comes from the pinned baselines
   (`expected-holds` inequality 15≠16 and the two pins). That matches design §6's
   D18 line ("the hold count drops to 14 → L3 mismatch"), but the caught object
   is the mismatch against the frozen baseline, not the live obligation.
3. **Consequence, reported not absorbed:** a change that drops the owed form and
   re-pins the expectation and typed packet in the same move would leave the flow
   green at 14 holds — the circularity attack owned by D22/D23. The dropped-gloss
   fixture is the executable instance of that risk; `.scratch/neg18/wired-*.out`
   holds the receipts.
4. **fx18d's planned surface does not exist.** The doctored-projection fixture was
   built for `assemble-d2-typed.py --projection`; the landed flow re-derives the
   projection in-process, so a doctored committed projection file is not consumed
   (the committed projection participates only inside the committed typed packet,
   which is itself pin-compared). The fixture stays in §2 for the design's
   adapter contract; against the landed flow it is inert by construction.

Reproduce the re-run:

```sh
export TMPDIR=$PWD/.scratch
python3 .scratch/neg18/build-fixtures.py
for c in fx18a fx18b fx18c; do python3 tools/typed-gate-flow.py --packet .scratch/neg18/$c/packet.yml; echo "$c exit=$?"; done
python3 tools/typed-gate-flow.py --typed-override .scratch/neg18/ov1-row-dropped-gloss-back.yml
python3 tools/typed-gate-flow.py --typed-override .scratch/neg18/ov2-row-dropped.yml
python3 tools/typed-gate-flow.py        # live pair — 10/10 at the 22:19Z stamp
```


## 7. Reproduction

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
python3 .scratch/neg18/build-fixtures.py     # prints the §2 sha256 table
python3 .scratch/neg18/probe-standalone.py   # §3 table
python3 .scratch/neg18/probe-prototype.py    # §4 table
```

The builder (`.scratch/neg18/build-fixtures.py`) reads
`examples/culture-d2/packet.d2.yml` and `examples/culture-d2/typed-labels.d2.yml`
(hashes in §2) and writes only under `.scratch/neg18/`. Its packet mutations
remove exactly the named YAML line(s) from the GAR-01 record block (asserted
per line; the GAR-01 block is the span from `id: "GAR-01"` to `id: "GAR-02"`).
The projection mutation parses the JSON document, removes the GAR-01 label row,
its `findings[]` entry and decrements `coverage.{typed_labels,
findings_hold_or_fail, findings_total, label_findings_hold}` and
`typed_labels.stats.labels`, then re-serializes (`sort_keys=True`, LF) — a
drop that is internally consistent, so only a packet cross-check can catch it.

## 8. Limits and open items (report, not absorbed)

- **Tool under test / hashes at receipt time** (2026-10-17T22:05Z, `sha256sum`):
  `tools/d2-typed-labels.py` `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`
  (`--selftest` exit 0, 39/39 checks); `tools/gates/naming-collision-gate.py`
  `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d`;
  `tools/assemble-d2.py` `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d`
  (`--check` exit 0, "byte-identical deterministic assembly");
  `tools/gates/frozen/round-4/naming-collision-gate.out`
  `4d70252bdf7745dea76af07b41a94560b5789ff278cdbb5af4bf6924688bb19e`
  (contains the 10 baseline `PHON-INVENTORY` lines); prototype and
  `22-label-representation.md` hashes in §4/Receipts. Peers edit this tree
  concurrently; every digest names its stamp.
- **fx18c's expectation is weaker by design.** With both the label and the slot
  pointer gone, no representation channel can know the record owed a form; the
  only catch is a schema-completeness check (`assemble-d2.py:134` requires
  `garment` on costume records — but that check runs on the build path over
  components, not over an arbitrary packet file). Landed outcome (§6): fx18c is
  in fact caught, but like fx18a only by the pinned expectations.
- **fx18d's projection surface did not land.** The fixture targets the design's
  `assemble-d2-typed.py --projection` contract; the landed flow
  (`tools/typed-gate-flow.py`) re-derives the projection in-process and has no
  projection input, so the doctored-projection file is not consumed and its
  fixture is inert against the landed flow by construction (§6.4). The
  projection did get re-pinned (`a3aa452c…`, `--check` exit 0), so the round-10
  A2 staleness this bullet used to carry is resolved at this stamp.
- **Reported, not absorbed — live integration inconsistency at 22:25Z.** The
  committed `examples/culture-d2/packet.d2.typed.yml`
  (`1b5010b7…`, `schema: kotodama-typed-packet-v1` + `typed_channel` rows +
  `adapter_sha256 c7e5a749…`) is not the document the flow derives (`e8a83445…`,
  `typed_view` shape), so the live pair fails `typed-packet-pinned` (9/10) at
  22:25Z, after passing 10/10 at the 22:19Z stamp with the earlier committed
  bytes. Two generators, two shapes: the D03 adapter fragment's output and the
  D05 flow's derivation need one owner. This is integration debt for D05/D08,
  reported here because this shard's injections were measured against both
  states.
- **Reported, not absorbed — negative file location.** `design.md` §7 assigns
  "negative controls under `reports/round-11/depth/neg/**`"; this dispatch named
  exactly `reports/round-11/depth/neg-18.md`, and the hard rule is literal, so
  the fixtures live in `.scratch/neg18/**` and are reproducible from §7. If the
  integrator wants the committed-fixture layout, filing `fx18a`/`fx18d` under
  `depth/neg/` is a copy of §7's builder output, not a re-derivation.
- **Adjacency:** the adapter-prototype and the `22-label-representation.md`
  controls are supplement-opencode-1 material, used here as design precedent
  and cited by path; this shard changes no supplement byte.

## Receipts

```sh
# 2026-10-17T22:05Z, lane repo root, TMPDIR=$PWD/.scratch
python3 .scratch/neg18/build-fixtures.py
python3 .scratch/neg18/probe-standalone.py
python3 .scratch/neg18/probe-prototype.py
python3 tools/d2-typed-labels.py --selftest            # exit 0, 39/39
python3 tools/assemble-d2.py --check                   # exit 0
sha256sum tools/d2-typed-labels.py tools/gates/naming-collision-gate.py \
  tools/assemble-d2.py examples/culture-d2/packet.d2.yml \
  examples/culture-d2/typed-labels.d2.yml \
  reports/supplement-opencode-1/scratch/22-label-representation/adapter-prototype.py \
  tools/gates/frozen/round-4/naming-collision-gate.out
```

```sh
# 2026-10-17T22:19–22:26Z, wiring re-run receipts (full outputs in .scratch/neg18/wired-*.out)
python3 tools/typed-gate-flow.py                        # live: 10/10 @22:19Z; 9/10 @22:25Z (typed-packet-pinned)
python3 tools/typed-gate-flow.py --packet .scratch/neg18/fx18a/packet.yml   # exit 1, 15 vs 16 findings
python3 tools/typed-gate-flow.py --packet .scratch/neg18/fx18b/packet.yml   # exit 1, GAR-01 D2L-DATA + hold
python3 tools/typed-gate-flow.py --packet .scratch/neg18/fx18c/packet.yml   # exit 1, 15 vs 16 findings
python3 tools/typed-gate-flow.py --typed-override .scratch/neg18/ov1-row-dropped-gloss-back.yml  # exit 1
python3 tools/typed-gate-flow.py --typed-override .scratch/neg18/ov2-row-dropped.yml             # exit 1
sha256sum tools/typed-gate-flow.py examples/culture-d2/packet.d2.typed.yml \
  examples/culture-d2/typed-gate.expected.json examples/culture-d2/typed-labels.d2.yml
# typed-gate-flow.py 5758e315… | packet 1b5010b7… (22:24Z emit; e8a83445… was the flow's derivation hash)
# typed-gate.expected.json 7ed597317b32b238d880af0a602fcbfa1ffd92608008879f049db9fd02aa03aa
# typed-labels.d2.yml a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43
```

Cited precedent hashes: `22-label-representation.md`
`5493b3f7a4c8e1b056ca0cdc7112c84e9ce43b6cb89ef47926bc88bdeacb3364`;
adapter prototype `9fe01335d8bb526c08d81c92ccf3f4f2ebd5899d1f7b8e02123ae3d0b86425a8`
(both read 2026-10-17T22:05Z).
