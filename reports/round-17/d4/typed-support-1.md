# R17-D18 — typed-packet derivation for the D4 culture (typed support, seat 1)

- round: 17 (operator loop 2 of 3, build round 1 of 4; 64 declared workers,
  `opencode-go/deepseek-v4.1-flash`) · shard: **D18** (typed support: typed-packet
  derivation), claim **D `culture-d4-assembly`**.
- assignment (verbatim): "D4 R17-D18..D19 (typed support): typed-packet derivation
  + hold-set documentation; D4 expected-holds.json fragment;
  reports/round-17/d4/typed-support-{1,2}.md."
- date: 2026-10-18 (stamps local UTC-3; UTC where stated). Reference revision
  `9b49a4a0fca6ceeab917d401945358fdedeb7e11` (round-17 declare); baseline
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (round-16 admit).
- canon: NON-CANON engineering evidence. Nothing here is a culture design, a canon
  record, a handoff, or a real-world clearance/rights statement.
- writes: **this file only** plus in-lane scratch under `.scratch/r17d18/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command; `/tmp`
  untouched). No tool, gate, packet, projection, component, baseline or
  earlier-round byte is edited by this seat; `reports/round-{8..16}/**` and
  `tools/gates/{frozen,expected}/**` are filed and read-only here. No commit, no
  push.
- status: **derivation contract complete and measured; the D4 instance (§6) is
  filled from the landed design brief and component drafts, with the derivation
  receipts to land when the D4 tree does** (dependency record §7). The contract
  in §5 is what the D4 typed derivation must satisfy; §6 binds it to the D4
  design; §8 carries the interface findings the D4 build must resolve.

## 0. Verdict

1. **The D2 typed chain is green today and is the pattern D4 must replicate**, but
   it is **culture-bound in three load-bearing places** (§4): the projector's
   costume-slot regex is the literal `LEX-GAR-[0-9]{2}` (a foreign prefix crashes
   it with a raw `AttributeError`), its rank and era-alias legs read D2's
   components at module level (a packet declaring zero rank rules still emits D2's
   `D2L-RANK` findings), and the adapter's assembler-identity leg calls
   `assemble-d2.py`'s build (a one-byte-changed packet copy is refused, exit 2).
2. **Therefore D4's typed derivation must be D4-bound** — either a D4 projector /
   adapter pair, or a generalized derivation whose assembler-identity leg calls
   `assemble-culture-d4.py`'s own build. A D4 derivation that reuses
   `tools/d2-typed-labels.py` unmodified would import D2's rank findings into
   D4's finding set (measured, §4.2).
3. **The derivation contract (§5) is fixed here**: artifact names (the canonical
   D2 names with a `d4` suffix, matching the round-17 counting contract), the
   fail-closed legs, the routing-row rules, determinism and the pin block. The
   D4 instance (§6) is completed from the delivered tree.

## 1. What the derivation is

Claim D requires `examples/culture-d4/` "built end-to-end through the typed
pipeline: brief -> 12 components -> typed labels -> assembled packet -> gate with
findings exactly equal to D4's named hold set". The typed-packet derivation is the
middle of that chain:

```
examples/culture-d4/components/*  (12 components + brief)
   │  tools/assemble-culture-d4.py                      [O claim; NOT this seat]
   ▼
examples/culture-d4/packet.d4.yml            legacy gate-facing packet
   │  <D4 typed-label projector>                       [derivation step 1]
   ▼
examples/culture-d4/typed-labels.d4.yml      typed-label projection
   │  <D4 typed-packet adapter>                        [derivation step 2]
   ▼
examples/culture-d4/packet.d4.typed.yml      typed packet (schema
   │                                          kotodama-typed-packet-v1)
   ▼
<D4 typed-pipeline gate>  →  findings == examples/culture-d4/expected-holds.json
```

The canonical artifact names above are the ones the round-17 counting contract
looks for first (`reports/round-17/scope.md:102-107`: "the canonical D2 names with
a `d4` suffix are what it looks for first"; the expected hold set carries schema
`kotodama-typed-pipeline-holds-v1`). The D2 analogue is
`examples/culture-d2/{packet.d2.yml, typed-labels.d2.yml, packet.d2.typed.yml,
expected-holds.json}` with the chain `assemble-d2.py` → `d2-typed-labels.py` →
`assemble-d2-typed.py` → `gates/typed-pipeline-gate.py`.

Steps 1 and 2 are the derivation this seat specifies; the assembler (O claim) and
the gate belong to other seats. The exact tool that performs steps 1–2 for D4 is
the open interface item (§5.7, §8).

## 2. The D2 typed chain, measured green at this stamp

All commands cwd = lane root, `TMPDIR=$PWD/.scratch`, 2026-10-18. Tool pins
(sha256, `sha256sum`):

| tool | sha256 |
|---|---|
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` |
| `tools/assemble-d2-typed.py` | `c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071` |
| `tools/gates/typed-pipeline-gate.py` | `d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d` |
| `tools/assemble-d2.py` | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` |
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` |
| `examples/culture-d2/typed-labels.d2.yml` | `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` |
| `examples/culture-d2/packet.d2.typed.yml` | `1b5010b7f449ec78755e9a8b0efea62c705af7ec5c592ceda6cf2c072dfac8a3` |

| leg | command | observed |
|---|---|---|
| projector selftest | `python3 tools/d2-typed-labels.py --selftest` | exit 0 — 39/39 checks passed |
| projector `--check` | `python3 tools/d2-typed-labels.py --check` | exit 0 — byte-identical deterministic projection |
| adapter `--check` | `python3 tools/assemble-d2-typed.py --check` | exit 0 — byte-identical deterministic typed packet |
| typed-pipeline gate | `python3 tools/gates/typed-pipeline-gate.py` | exit 0 — 16/16 legs; 15 holds + 1 note, 0 fails |
| gate selftest | `python3 tools/gates/typed-pipeline-gate.py --selftest` | exit 0 — 12/12 checks passed |

The derivation semantics the D4 instance must reproduce (D2 shape): the projector
types every form-bearing record into `native-form` / `translated-label` /
`borrowed-strata`; the adapter moves each `translated-label` record's checked
field `garment` → `garment_gloss`, appends one `typed_channel` routing row per
routed record, and carries the projector's finding set verbatim under
`pipeline_findings` with `pipeline_counts`; `assembly` pins
`packet_sha256`/`projection_sha256`/`adapter_sha256`
(`tools/assemble-d2-typed.py:160-244`).

## 3. What carries over for D4 — and what does not

Measured on scratch copies (`.scratch/r17d18/`, 2026-10-18), never on repo bytes:

| # | experiment | command (scratch) | observed |
|---|---|---|---|
| P1 | projector accepts a packet path override | `python3 tools/d2-typed-labels.py --packet .scratch/r17d18/packet-copy.yml --emit .scratch/r17d18/typed-copy.yml` | exit 1 (findings); projection written; `--check` on it exits 1 because the emitted bytes differ from the committed D2 projection in **exactly 2 lines**: `assembly.packet` and `canon` (both record the packet path). The projection embeds the packet path — a D4 projection must be emitted from the canonical D4 path. |
| P2 | adapter accepts `--packet/--projection/--emit` overrides | `python3 tools/assemble-d2-typed.py --packet .scratch/r17d18/packet-copy.yml --projection .scratch/r17d18/typed-copy.yml --emit .scratch/r17d18/typed-packet-copy.yml` | exit 0 — "Wrote … (160597 bytes, 10 routing row(s))". The adapter is path-generic; only its input checks bind it. |
| P3 | adapter refuses a packet that is not `assemble-d2.py`'s build | same command with `.scratch/r17d18/packet-mod.yml` (one word changed inside a garment gloss) | exit 2 — `FAIL assembler_identity: packet bytes are not assemble-d2.py's deterministic assembly (0bd2defbfa75 vs e0f21509e14a)`. This is the leg that binds the adapter to D2's components. |
| P4 | projector crashes on a foreign costume slot prefix | `python3 tools/d2-typed-labels.py --packet .scratch/r17d18/probe-d4.yml --json` (`form_slot: "LEX-COS-01"`) | exit 1 with raw traceback — `AttributeError: 'NoneType' object has no attribute 'group'` at `tools/d2-typed-labels.py:498`; `_SLOT_RE = re.compile(r"LEX-GAR-[0-9]{2}")` (`:449`) does not match, so `.search(...)` is `None`. A stable exit-2 diagnostic is the tool's own contract; this is a defect, reported not repaired. |
| P5 | projector emits D2 rank findings for a packet with no rank rules | `python3 tools/d2-typed-labels.py --packet .scratch/r17d18/probe-d4-min.yml --json` (minimal packet: eras E0/E1, 8-consonant inventory, one material, two costumes, one lexicon record, one name) | exit 2, `stats {fail: 1, hold: 7, labels: 4, note: 1}` — the finding set includes **D2's rank findings**: `D2L-RANK` holds `TR-04#a\|TR-06#a`, `WR-02#g\|WR-09#g`, `WR-08#g\|WR-09#g` and note `SR-01#a\|SR-01#b`. Mechanism: `build_payload()` (`:1235`) reads module constants lifted from D2's `12-rank-rules.yml`; `declared_era_aliases()` (`:2319`) reads `examples/culture-d2/components/12-rank-rules.yml`. |
| P6 | packet schema the projector requires | P5 fixtures | exit 2 with stable messages for a packet missing `eras` ("packet.eras: expected a non-empty list of era tags"), missing `materials` ("packet.materials: expected a non-empty record list"), or a costume missing `era`/`material` ("costume carries no era claim" / "no material reference"). These blocks are mandatory for any D4 packet that goes through this projector family. |

Reading: P1/P2 show the projector and adapter CLIs are path-generic; P3/P4/P5
show the semantics are not. **A D4 derivation must not reuse
`tools/d2-typed-labels.py` unmodified** unless D4 deliberately adopts the D2
conventions (the `LEX-GAR-` slot prefix and D2's rank findings — the second is
not acceptable for a fresh culture's hold set).

## 4. Culture-boundness inventory (the D4 derivation must replace or bind each)

| # | binding | location | consequence for D4 |
|---|---|---|---|
| B1 | costume slot regex `LEX-GAR-[0-9]{2}` | `tools/d2-typed-labels.py:449`, used at `:498` | a D4 slot id with any other prefix crashes the projector (P4). Either D4 slots use the literal `LEX-GAR-NN` shape, or the D4 projector generalizes the pattern (e.g. per-culture prefix) — with a stable exit-2 refusal for an unmatched slot, never a traceback. |
| B2 | rank adapter reads D2 constants | `build_payload()` `:1235-1259`, `NORMALIZED`/`ACT_RULES`/`RESIDUALS`/`COMPONENT_RULE_IDS` | D2's `D2L-RANK` findings would enter D4's finding set (P5). A D4 projector must either omit the rank leg or bind it to D4's own rank component. |
| B3 | era aliases read D2's component | `declared_era_aliases()` `:2319`, `era_alias_rows()` `:2369` | D2's alias map is used for D4's era reconciliation; harmless only if D4 declares no alias-dependent rows, otherwise wrong. |
| B4 | adapter assembler-identity → `assemble-d2.py` | `tools/assemble-d2-typed.py:63`, `SERIALIZER = ROOT/"tools/assemble-d2.py"` | a D4 packet is refused (P3). The D4 adapter's identity leg must call `assemble-culture-d4.py`'s own build (the O claim's tool) — never re-implement it. |
| B5 | gate constants | `tools/gates/typed-pipeline-gate.py`: `EXPECTED_HOLDS`, `EXPECTED_NOTES`, `EXPECTED_COUNTS`, `PROJECTION_DEFAULT`, `EXPECTED_HOLDS_PATH` (all D2) | the D4 gate must be D4-bound (or parameterized); the D2 gate's selftest asserts its constant equals D2's committed `expected-holds.json` both directions (`:74-88`) — the same discipline must hold for D4. |
| B6 | prose fields | projector `canon`/`assembly.packet` (P1); adapter `typed_assembly.generator` | cosmetic for gates; a D4 projection should say D4, not "D2 design drill". |
| B7 | explicit `typed_labels` pass-through | `project_labels()` `:605` | available to D4 as the hand-authored channel (controls/tests), unchanged. |
| B8 | strict loader | `load_packet_strict` (R8-D03 §4.1) | culture-neutral; the D4 packet must stay inside the closed YAML subset (no anchors/tags/tabs; `|` block scalars refused — D2's own components work around this by block extraction). |

## 5. The D4 derivation contract (fixed by this seat)

### 5.1 Artifacts and names

| artifact | path (canonical) | producer |
|---|---|---|
| legacy packet | `examples/culture-d4/packet.d4.yml` | `tools/assemble-culture-d4.py` (O claim) |
| typed-label projection | `examples/culture-d4/typed-labels.d4.yml` | derivation step 1 (D4-bound projector) |
| typed packet | `examples/culture-d4/packet.d4.typed.yml` | derivation step 2 (D4-bound adapter) |
| expected hold set | `examples/culture-d4/expected-holds.json` | this seat's fragment `reports/round-17/d4/expected-holds.fragment.json` (§ typed-support-2.md), landed by the integrator |

### 5.2 Fail-closed legs (adapter, mirroring the D2 design §2.2)

| check | rule | on failure |
|---|---|---|
| assembler identity | packet bytes equal `assemble-culture-d4.py`'s own deterministic build (call its build path; never re-implement) | exit 2 |
| projection freshness | the projection pins this packet's sha256 and the D4 projector reproduces it byte-for-byte | exit 2 |
| coverage | every record the D4 projector types off-channel has exactly one routing row; every routed record exists in the packet; no routing row names an untyped record | exit 2 |
| determinism | two consecutive builds byte-identical; `--check` compares bytes without writing | exit 1 on drift |

### 5.3 Typed packet shape

Schema `kotodama-typed-packet-v1`; the packet's blocks plus:

- `typed_channel`: one row per off-channel record — `record`, `kind`,
  `label_id`, `owner`, `source_field`, `off_channel_field`,
  `channel: off-sound-and-identity`, `hold: D4L-FORM-UNRESOLVED`, `owed_slot`;
- `pipeline_findings` / `pipeline_counts`: the D4 projector's finding set and
  counts, carried verbatim (the gate reads holds from the typed packet);
- `assembly`: `packet_sha256`, `projection_sha256`, `adapter_sha256` (the
  adapter's own digest, so a frozen row's gate hash pins it transitively);
- `typed_assembly`: generator + the routing rules actually applied.

### 5.4 Anti-laundering rules (carried from the D2 design §3.2)

Exit 0 from the D4 gate must mean "the emitted findings equal the frozen expected
hold set", never "the culture is clean". The gate must print the holds verbatim,
and the expected set must be compared **exactly** (key `(id, severity, where)` as a
set, counts and detail strings pinned; a hold downgraded to a note, renamed,
dropped, or an unpinned note appearing is a mismatch). The D2 gate's banner
wording and its 12-control selftest are the template.

### 5.5 The finding-class vocabulary

D4 findings reuse the `D2L-*` class vocabulary only where the D2 contract classes
apply (`reports/round-8/depth/design-spec.md` §6). The D4 analogue of
`D2L-FORM-UNRESOLVED` is `D4L-FORM-UNRESOLVED` (this seat's naming, per the
`D2L-*` pattern); other classes follow the same substitution (`D4L-NATIVE`,
`D4L-RANK`, `D4L-DATA`, `D4L-SCOPE`, `D4L-MATERIAL`, `D4L-BORROW`). **The exact
id set is pinned in typed-support-2.md §2** and must match the delivered
`expected-holds.json` in both directions (round-17 counting contract D2/D8).

### 5.6 Determinism and pins

Two fresh derivation builds must be byte-identical to each other and to the
delivered bytes; `--check` must exit 0 against the delivered tree; the `assembly`
pin block must re-verify against the bytes read (round-17 counting contract D3).
The D4 derivation must not touch `tools/d2-typed-labels.py`,
`tools/assemble-d2.py`, `tools/assemble-d2-typed.py`, `tools/assemble-culture-d3.py`,
`examples/culture-d2/**`, `examples/culture-d3/**` (claim D's "d2/d3 untouched and
green" leg).

### 5.7 Open interface item (reported, not absorbed)

At this stamp **no D4-bound derivation tool exists** in `tools/`: the assembler
`tools/assemble-culture-d4.py` landed at 06:33 local (its docstring fixes the
`assemble()` callable as the build path the D4 adapter's assembler-identity leg
must call), but neither `tools/d4-typed-labels.py` nor
`tools/assemble-d4-typed.py` exists yet (sweep: `ls tools/ | grep -i "d4\|typed"`,
2026-10-18 06:35 → the D2 typed tools plus `assemble-culture-d4.py` only;
`reports/round-17/scope.md:89-93` records `examples/culture-d4/` and the
assembler as expected-absent pre-dispatch artifacts). The D4 derivation therefore
requires one of: (a) a D4 projector + adapter pair (the brief's §9.1 route), (b)
a parameterized projector/adapter whose culture binding is an explicit input
(paths + slot pattern + rank-component source), or (c) a decision by the design
seats that D4 adopts D2's slot-prefix convention — which still leaves B2/B3/B5
(rank/alias/gate) to bind. This seat does not write the tools (write scope); the
interface above is the contract they must satisfy.

## 6. The D4 instance (filled from the landed design brief)

The D4 design brief landed at 2026-10-18 06:26 local:
`reports/round-17/d4/design-brief.md` (R17-D01; sha256
`a5fdc84dfe3f98e92068e2737f6447c9adec82ff669914b3e22963ee8447e78f`
(`sha256sum` 2026-10-18 06:34); the brief was edited in flight — the earlier
as-read at 06:31 was `091e7aa9…`; a re-read event if the file changes again). It fixes the culture ("the weigh-court quote register", §2),
the 12-component registry (§5), the typed-pipeline deltas Δ1–Δ8 (§6), the
candidate hold set (§7.1) and the artifact contract (§9). This section binds the
derivation contract to that design.

### 6.1 The culture, and the two routing classes (Δ1)

D4 is a settled grain-and-orchard plain culture whose towns run weigh-courts;
brokers bind prices in a taught quote register (argot). The typed-pipeline delta
that makes D4 worth building is **two routing classes in one packet**
(`design-brief.md:255-275`):

| class | record set | checked field | channel | hold | brief anchor |
|---|---|---|---|---|---|
| 1 — gloss rows | goods/measure glosses with owed slots, `GD-01..GD-06` | moved off-channel (`off_channel_field: <field>_gloss`) | `off-sound-and-identity` | `D4L-FORM-UNRESOLVED` | §6 Δ1, §7.1 row 1 |
| 2 — register rows | argot loans supplied and checked in the quote slot; plain doublet owed, `AL-01#plain..AL-06#plain` | **stays on channel** (`off_channel_field: null`) | `on-sound-and-identity` | `D4L-REGISTER-UNRESOLVED` | §6 Δ1 (`:264-265`), §7.1 row 2 |

Class 2 is the new state: on-channel but slot-inadmissible — a `register` field
must not move a form off the sound channel, just as a typing field may not exempt
a string (§6 Δ1, re-reading the round-8 T1 discipline).

### 6.2 The derivation chain and pins (brief §9.1–9.3)

| artifact | path | producer | pins (brief §9.2) |
|---|---|---|---|
| legacy packet | `examples/culture-d4/packet.d4.yml` | `tools/assemble-culture-d4.py` (O claim) | component digests + assembler self-digest |
| typed-label projection | `examples/culture-d4/typed-labels.d4.yml` | `tools/d4-typed-labels.py` (D2's projector pattern) | `packet_sha256` + projector self-digest |
| typed packet | `examples/culture-d4/packet.d4.typed.yml` | `tools/assemble-d4-typed.py` | packet, projection, adapter, assembler |
| expected hold set | `examples/culture-d4/expected-holds.json` | hold-set seat fragment → integrator (typed-support-2.md) | packet, projection, projector, adapter |

The brief's recommended interface (D2's names with a `d4` suffix) matches the
round-17 counting contract's first-look names (§5.1 above).

### 6.3 What the round-17 runner will execute (measured against `reports/round-17/run-validation.py`)

| leg | runner behavior | consequence for the derivation |
|---|---|---|
| discovery | `d4_discovery()` scans `examples/culture-d4/`; requires packet, typed, projection, expected, brief + ≥12 components (`:495-502`) | all five artifacts must exist under `examples/culture-d4/`; the expected file is discovered **only there** (`reports/round-17/d4/` is design-docs territory) |
| assembler determinism | `tools/assemble-culture-d4.py --check` must exit 0 (`:572-578`) | the assembler is the O claim's tool |
| adapter determinism | runs `[adapter, "--packet", P, "--projection", J, "--emit", T]` twice; both exit 0, byte-identical to each other and to the delivered typed packet (`:579-601`) | the D4 adapter must support exactly that CLI and be a pure function of packet+projection |
| adapter identity | `adapter_for()` matches the typed packet's `assembly.adapter_sha256` against `tools/*.py` with "assemble" in the name (`:461-473`) | the adapter must be a `tools/` file (e.g. `tools/assemble-d4-typed.py`), not scratch |
| typed interop | strict-parses under the projector's loader; schema `kotodama-typed-packet-v1`; ≥1 `typed_channel` row; pins re-verify (`:508-517`, `:640-663`) | the typed packet carries the D2 typed keys + the D4 routing rows |
| gates | five culture gates over the D4 packet must exit ∈ {0,1} (`:664-672`) | no exit 2 / traceback on the D4 packet |
| design-doc naming | hold ids and `where`s from the expected file must appear in the round-17 design docs (`:706-733`) | the brief §7.1 + typed-support-2.md both name them |

### 6.4 The D4L-* vocabulary and the projector legs the engine does not carry

The D2 engine (`tools/d2-typed-labels.py`) implements the label leg, the
scoped era/material reconciliation and the (D2-bound) rank leg. The brief's D4
deltas require additional legs the engine has never carried:

- **register leg (Δ1 class 2)** — `registers` / `doublets` packet keys →
  `D4L-REGISTER-UNRESOLVED` holds at `<slot>#plain`; no engine code produces this
  id today (`grep -c "D4L-\|REGISTER" tools/d2-typed-labels.py` → 0, 2026-10-18);
- **argot-derivation check (Δ3)** — `derived_from` + `derivation` (`head2`,
  `reverse`) between two records of the same packet → `D4L-ARGOT-DERIV` in
  controls only;
- **register-era check (Δ5)** — a quote form claimed pre-E3 → `D4L-ERA`;
- **rank property kinds `register` / `speech-act` (Δ6)** → `D4L-RANK` holds
  `RG-05#a|RG-07#a`, `RG-06#a|RG-09#a` + note `RG-08#a|RG-08#b`;
- **material route hold (Δ7)** → `D4L-MATERIAL` at `SM-03`.

The D4 projector must add these legs (or bind them explicitly); a projector that
only wraps the engine emits neither the register holds nor the D4L ids, and the
runner's hold-set equality leg fails. The D17 draft
(`.scratch/r17d17/d4-typed-labels.py`, read 2026-10-18 06:29) wraps the engine's
label + reconciliation legs and **omits** the rank leg (recorded in its own
`rank_leg` note) — correct on F-D18-2, but the D4-specific legs above are not in
it yet.

### 6.5 Status

At this stamp `examples/culture-d4/` does not exist. Landed: the design brief
(06:26, edited in flight), the design companions (`design-costume.md`,
`design-language.md`, `design-myth-era.md`), five component drafts
(`reports/round-17/d4/components/01-brief.yml` … `05-naming.yml`, 06:28-06:35)
and the assembler `tools/assemble-culture-d4.py` (06:33); in flight: the D17
projector draft and the D20 expected-holds generator
(`.scratch/d20/make-expected-holds.py`). The derivation receipts (hashes +
exits) land when the tree and the derivation tools do; this section is the
contract they must satisfy. Every pin above is as-read at its stated time — a
re-read event if a byte moves.

## 7. Dependency record

- Wave start (lane state): `examples/culture-d4/` absent,
  `reports/round-17/d4/` empty, `tools/assemble-culture-d4.py` absent —
  consistent with `reports/round-17/scope.md:89-93` (2026-10-18).
- Poll cadence: 60 s, lane root, from 06:15 local. Landings observed: the D4
  design brief `reports/round-17/d4/design-brief.md` at 06:26 local (sha256
  `a5fdc84d…` as-read 06:34; edited in flight, earlier `091e7aa9…` at 06:31);
  the round-17 runner
  `reports/round-17/run-validation.py` at 06:27; the D4 assembler
  `tools/assemble-culture-d4.py` at 06:33; sibling drafts in flight at
  06:28-06:33 (`.scratch/r17d17/d4-typed-labels.py`,
  `.scratch/d20/make-expected-holds.py`). The sibling integrator poll
  (`.scratch/d25/poll.log`) still shows `tree_files=0 tool=0 packet_outputs=0`
  through 2026-10-18T09:28Z.
- At this stamp `examples/culture-d4/` and `tools/assemble-culture-d4.py` still
  do not exist; the D4 components are being drafted under
  `reports/round-17/d4/components/` (`01-brief.yml` present, 06:28). The
  derivation receipts (projector/adapter hashes + exits) land when the tree
  does; §6.5 names the re-read points.

## 8. Findings for the D4 build (evidence-first)

- **F-D18-1 — the projector's costume-slot regex is D2-literal and crashes on a
  foreign prefix.** `_SLOT_RE = re.compile(r"LEX-GAR-[0-9]{2}")`
  (`tools/d2-typed-labels.py:449`); `_costume_label` calls
  `_SLOT_RE.search(slot).group(0)` with no `None` guard (`:498`). Receipt P4.
  **Live risk for D4**: the D17 projector draft reuses the engine's
  `parse_typed_labels` verbatim (`.scratch/r17d17/d4-typed-labels.py:1-31`,
  read 2026-10-18 06:29), so a D4 costume whose `form_slot` does not contain
  `LEX-GAR-NN` crashes the derivation (exit 1, traceback) instead of producing
  the `GD-0N` gloss holds. Disposition for the D4 projector: generalize the slot
  pattern (or require the D4 components to declare a matching slot shape) and
  refuse an unmatched slot with a stable exit-2 `D4L-DATA` finding. (D2 is
  untouched; this is a report, not a repair.)
- **F-D18-2 — the projector's rank/alias legs are D2-component-bound.** Receipt
  P5: a packet with no rank rules emits D2's three rank holds + one note.
  Disposition: the D4 projector must bind the rank leg to D4's rank component or
  omit it; a D4 derivation that shows `D2L-RANK` in its finding set is
  mis-bound. (The D17 draft omits the rank leg and records the omission in its
  `rank_leg` note — the correct shape; the D4 rank holds then come from the D4
  leg the brief Δ6 requires, not from the engine.)
- **F-D18-3 — the adapter's assembler-identity leg is D2-bound.** Receipt P3.
  Disposition: the D4 adapter's identity leg must call
  `assemble-culture-d4.py`'s build.
- **F-D18-4 — packet schema requirements measured** (P6): `eras` non-empty tag
  list, `materials` non-empty record list, every costume with `era` + `material`,
  otherwise stable exit-2 refusals. The D4 brief/components must carry these
  blocks for any projector-family derivation. Independent corroboration: the
  round-17 negative seat hit the same requirement and recorded it verbatim —
  "A fourth, minimal packet was attempted and abandoned: `--packet` runs the
  full reconciliation projection, which requires the complete packet shape
  (`d2-typed-labels error: packet.materials: expected a non-empty record list`)"
  (`reports/round-17/tests/neg-3.md`, §2, 2026-10-18).
- **F-D18-5 — the projection embeds the packet path** (P1, 2 lines:
  `assembly.packet`, `canon`). A D4 projection emitted from a scratch path is not
  byte-stable against one emitted from the canonical path; emit from
  `examples/culture-d4/` only.
- **F-D18-6 — the runner's routing-consistency leg contradicts the brief's
  two-class design unless the register rows stay out of `typed_channel`.** The
  runner equates the `FORM-UNRESOLVED` hold `where`s with **all**
  `typed_channel` records (`reports/round-17/run-validation.py:556-560`:
  `owed = {…id.endswith("FORM-UNRESOLVED")…}` vs `off_records = {row.record…}`).
  The brief's class-2 register rows (`channel: on-sound-and-identity`,
  `off_channel_field: null`, records `AL-01..AL-06`, `design-brief.md:255-275`)
  would be counted as off-channel records, so `off_records` = {AL-01..06} ∪
  {GD-01..06} ≠ `owed` = {GD-01..06} → the D leg fails on a design-conformant
  packet. Options, none taken by this seat: (a) the D4 adapter carries class-2
  rows under a distinct key (e.g. `typed_register`) so `typed_channel` holds
  only off-channel rows; (b) the runner filters routing rows by
  `channel == off-sound-and-identity` (its own constant vocabulary) or by the
  `FORM-UNRESOLVED` id suffix before comparing. This is an interface decision
  for the design/tool seats and the runner's author (X02), reported with the
  exact lines so the choice is explicit, never a silent adaptation.
- **F-D18-7 — the runner pins `projector_sha256` to the D2 projector, not D4's.**
  `run-validation.py:557-566` compares the expected file's `projector_sha256`
  against `PROJECTOR = "tools/d2-typed-labels.py"` (`:82-83`), while the brief's
  D4 projector is `tools/d4-typed-labels.py` (`design-brief.md:481`). A
  correctly pinned D4 projector would therefore fail the pin leg; the runner
  skips non-string pins (`if not isinstance(declared, str): continue`). Options:
  omit `projector_sha256` from the D4 expected file and pin the D4 projector
  under a distinct key (e.g. `d4_projector_sha256`), or amend the runner. The
  D20 expected-holds generator already omits the key for exactly this reason
  (`.scratch/d20/make-expected-holds.py` docstring, read 2026-10-18 06:28) —
  independent corroboration of the conflict.
- **F-D18-8 — the adapter must be a `tools/` file whose build reproduces the
  delivered typed packet.** The runner discovers the adapter by matching the
  typed packet's `assembly.adapter_sha256` against `tools/*.py` files whose name
  contains "assemble" (`run-validation.py:461-473`) and then requires two fresh
  `--packet/--projection/--emit` builds to be byte-identical to the delivered
  typed packet (`:579-601`). A scratch-only adapter, or one whose emitted bytes
  differ by a path/date field, cannot satisfy the leg.
- **F-D18-9 — the design-doc naming leg matches each hold `where` individually;
  range notation leaves tokens unnamed.** `id_boundary` is a per-token
  boundary regex (`run-validation.py:172-173`) and the D8 leg collects every
  `where` from the expected file and requires each to appear in the round-17
  design docs (`:706-733`). Measured 2026-10-18: with the brief's and this
  seat's range notation (`AL-01#plain`..`AL-06#plain`), the tokens
  `AL-02#plain`, `AL-03#plain`, `AL-04#plain`, `AL-05#plain` appeared in **zero**
  design docs (`grep -l -- "<token>" reports/round-17/d4/*.md reports/round-17/*.md
  | wc -l` → 0 for each), so a correct delivered expected file would fail D8 on
  four tokens. Fix applied in this seat's write scope: typed-support-2.md §4 now
  enumerates all 17 `where`s (and the note `where`) individually; re-measured
  → every token ≥1 file. The design seats' own docs should do the same, or the
  runner's leg should expand ranges.

## 9. Limits and handoff

- **What this fragment vouches for.** The D2 chain's green state (dated receipts),
  the culture-boundness measurements P1–P6, the derivation contract §5, and the
  D4 instance §6 as bound to the landed design brief. It does **not** vouch for
  the D4 tools (none landed at this stamp), the components, or the hold-set
  instance (typed-support-2.md carries the named set; the delivered file is
  derived from the typed packet).
- **Adjacent observations (reported, not absorbed).** (1) The runner/design
  conflicts F-D18-6/F-D18-7 are the two legs most likely to decide the D claim's
  outcome; they are interface decisions for the design/tool seats and the
  runner's author, and this seat neither edits the runner nor the adapter.
  (2) At this stamp no D4 tree exists; the D17 projector draft and D20
  expected-holds generator are in flight (`.scratch/r17d17/`, `.scratch/d20/`,
  read 2026-10-18 06:28-06:29).
- **Out of province (report, never absorb).** Canon status of D4's records, the
  culture's real-world referents and any clearance question are lore questions
  (`PROVINCE.md`).
