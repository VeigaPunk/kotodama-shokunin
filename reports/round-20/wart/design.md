# R20-O01..O04 — per-family era-alias resolution: design and wart analysis

- round: 20 (operator: loop 2 of 3, build round 4 of 4; 64 workers) · shard:
  **O01..O04 (wart analysis ×4)** · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "O R20-O01..O04 (wart analysis x4): read
  tools/d2-typed-labels.py declared_era_aliases + ALIAS_COMPONENT; design the
  per-family alias resolution (d4 packets declare no era-alias rules ->
  documented skip; keep d2 behavior byte-identical); negative controls;
  reports/round-20/wart/{design,review}.md."
- date: 2026-10-18. Round-20 baseline revision
  `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d` (`reports/round-20/claims.json`);
  the live wave was uncommitted and moving while this file was written — every
  reading below carries its own revision + time.
- canon: **NON-CANON** engineering evidence. This file designs and measures; it
  admits nothing, certifies no round, and is not canon.
- writes: this file + `review.md` (same directory) + scratch under
  `.scratch/r20-o/**`. No filed byte of rounds 8–19 is edited; no git action.

## 1. The wart (the round-19 routed erratum)

**Location.** `tools/d2-typed-labels.py` (pre-fix revision `0da0015f…`):
`ALIAS_COMPONENT = "examples/culture-d2/components/12-rank-rules.yml"` at
`:2316`; `declared_era_aliases()` at `:2319` reads that component and raises
`Malformed` when it is absent; `era_alias_rows()` at `:2369` additionally reads
`examples/culture-d2/components/11-costumes.yml`; `run_pipeline()` called both
unconditionally at `:2456–2457` for **every** packet.

**Mechanism.** The projection embeds the D2 component's alias map and its two
basis strings (`era_aliases_applied`, `era_aliases_basis`, and
`era_reconciliation.basis`/`alias_rows`/`verdicts`). So a D4 run read a foreign
family's tree, and the D4 projection of record (`a59990bb…`) was built from it.

**Two harms, not one.**

1. *Hard failure in a faithful mirror.* Measured 2026-10-18 ~13:00Z, pre-fix
   snapshot `.scratch/r20-o/wart-mirror` (tool sha `0da0015f…`, tools +
   `examples/culture-d4` only):

   ```sh
   cd .scratch/r20-o/wart-mirror
   python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --json
   # exit 2
   # stderr: d2-typed-labels error: missing examples/culture-d2/components/12-rank-rules.yml; A1 cannot be recorded
   ```

   The mirror-faithfulness cost is filed in `tools/assemble-d4-typed.py:416–419`
   (sha `1ddad6a7…`): the selftest copied `examples/culture-d2` wholesale, with
   the comment "documented wart; routed".

2. *Silent foreign inheritance when the tree was present.* The pre-fix D4
   projection `a59990bb…` (read 13:02Z) resolved `era-1 -> mapped-confirmed E0`
   and `E1 shelter era -> mapped-unconfirmed ERX-1` from the **D2** components,
   while the D4 packet's own era names (`named_eras`,
   `examples/culture-d4/packet.d4.yml:1915`) were never read. The r19-pre
   baseline's read set names both D2 components
   (`tools/gates/expected/d4-typed-labels-check-gate/r19-pre/expected.json`,
   `inputs` map: `11-costumes.yml`, `12-rank-rules.yml`).

## 2. Requirements the design must satisfy

- R1 **Family resolution**: a packet's alias leg is decided by its family; a
  foreign family never reads the D2 components.
- R2 **Declared source or open skip**: a foreign family resolves the alias rules
  its own packet declares; when it declares none, the leg is *skipped in the
  open* — the skip is visible in the artifact, not silent.
- R3 **D2 byte-identity**: every D2 surface keeps its bytes — the projection,
  the `--json` document, the default CLI, the selftest, the frozen replays.
- R4 **Fail closed on malformed declarations** (A1: no silent aliasing).
- R5 **No foreign tree in mirrors**: the D4 projector run and the adapter
  selftest must pass without `examples/culture-d2`.
- R6 **Pins move as NEW rows only**: no filed round-8–19 artifact is edited; a
  re-pin is a new file/dir/baseline id.
- R7 **Counts carry command + date; every fix carries a control.**

## 3. Design

### 3.1 Family key — two candidates, one landed

| key | convention source | evidence |
|---|---|---|
| **path shape** `culture-<family>` (landed) | `tools/gates/typed-pipeline-gate.py:213` `family_of` | `examples/culture-d4/packet.d4.yml` -> `d4`; a packet outside the shape keeps the D2 default |
| declared `assembly.generator` (alternative) | `tools/gates/typed-pipelines.json` note: "Matching is by the graded packet's own `assembly.generator` string, never by filename" | D2 declares `tools/assemble-d2.py` (`examples/culture-d2/packet.d2.yml:3320`), D4 `tools/assemble-culture-d4.py` (`:2345`) |

The landed implementation uses the path key. **Measured limit** (2026-10-18
13:05Z, no-D2 mirror): a D4 packet copied outside `examples/culture-d4/`
(`probe/probe-d4.yml`) falls back to the D2 leg and exits 2 with the legacy
missing-component error. Every pinned surface (packet, projection, adapter,
gate, baseline mirrors) keeps the `examples/culture-<family>/…` shape, so the
wart is closed where the claim measures it. Recommendation: keep the path key
(one convention with the gate), record the limit here, and treat the generator
as a possible secondary key in a later round — it is the string the profile
matcher already trusts.

### 3.2 Alias source for a foreign family

Precedence, all on the packet itself (`PACKET_ALIAS_KEYS`, `:2454`):

1. `era_aliases` — the D2-shaped label -> tag map;
2. `named_eras` — era-name records (`name` -> `tag`), e.g. the four D4 rows
   `the stamp era -> E0`, `the mark hand -> E1`, `the league -> E2`,
   `the cold fire (reserved) -> E3`;
3. `era_records` — the same shape, second home;
4. `era_reconciliation` — the packet's own reconciliation rows, shaped by
   `shape_reconciliation_rows` (`:2404`), so a declared `(to-verify)` row stays
   `to-verify`.

Nothing is inferred from an E-number; an undeclared label stays unmapped
(`reconcile_era`, `:839`).

**Note on the claim's parenthetical.** The round-20 claim text (and this
shard's assignment) assumed "d4 packets declare no era-alias rules". The
packet contradicts that: it declares `named_eras` (`:1915`) and `era_records`
(`:1794`). The landed leg therefore resolves the *declared* source (R2's first
branch) and records the skip only for the legs the packet does not declare —
measured: `skipped: [{"leg": "costume-era reconciliation", …}]`. The bare-skip
branch is exercised by the selftest's no-declaration control.

### 3.3 Skip semantics (visibility)

An undeclared leg yields a named `basis` line, a `skipped` row in the
projection (`era_reconciliation.skipped`), and — when nothing at all is
declared — probes of `[UNMAPPED_PROBE]`. A reader can therefore tell "no rules
declared" from "rules applied" without reading the code. This is the part of
the design that must not be dropped in any refactor.

### 3.4 Fail-closed gap (finding, see review.md F5)

`packet_alias_rows` builds tags with `str(...)`. A declared value that is not a
string (e.g. `era_aliases: {"era-9": [1, 2]}`) becomes the tag `"[1, 2]"` and is
emitted **confirmed** in `era_aliases_applied` and `alias_rows` (measured
13:04Z). Design requirement R4 says this must fail closed: validate tags with
`ERA_TAG_RE` (or refuse non-string entries) and name the refusal. Also, a
non-mapping `era_aliases` (e.g. the string `"nope"`) is silently ignored rather
than refused; the leg then resolves from `named_eras` — acceptable if the
refusal is recorded, not silent.

### 3.5 D2 branch

`family_alias_leg`'s D2 branch keeps the round-8 functions (`declared_era_aliases`
+ `era_alias_rows`) and the exact basis strings, so R3 holds by construction.
The functions stay byte-for-byte as delivered; the family split lives in the
new wrapper, not in them.

## 4. Negative controls (independent, 2026-10-18 13:00–13:07Z)

| # | control | command (scratch mirrors, tool sha as noted) | measured | verdict |
|---|---|---|---|---|
| N1 | d2 packet, component missing | no-D2 mirror, d2 packet | exit 2, `missing examples/culture-d2/components/12-rank-rules.yml; A1 cannot be recorded` | legacy text preserved |
| N2 | d2 component present, `era_aliases` block removed | `.scratch/r20-o/d2-noalias` | exit 2, `declares no era_aliases map (A1)` | legacy fail-closed |
| N3 | foreign packet declaring nothing | selftest control "a packet declaring no alias rules is skipped, never aliased" (50/50 run) | `aliases {}`, `rows []`, both legs in `skipped`, probes `[UNMAPPED_PROBE]` | skip in the open |
| N4a | non-mapping `era_aliases` (`"nope"`) | D4 packet + appended key | exit 1 (holds), resolves `named_eras`; the malformed key is not reported | gap -> F5 |
| N4b | malformed tag value `[1, 2]` | D4 packet + appended key | exit 1, `era_aliases_applied {'era-9': '[1, 2]'}`, row `confirmed` | **fail-open -> F5** |
| N4c | valid declared map `{"era-9": "E1"}` | D4 packet + appended key | applied; basis names the packet's own `era_aliases` | declared source works |
| N5 | foreign label `E9 no such label` | probes in every run | `unmapped` (never identity-by-number) | A1 holds |
| N6 | read set of the D4 run, no-D2 mirror | `sys.addaudithook('open')` probe | 0 opens containing `culture-d2`; only `examples/culture-d4/packet.d4.yml` | wart closed |
| N7 | non-conforming path | D4 packet under `probe/` | exit 2, legacy D2 error | limit -> F6 |
| N8 | adapter selftest without the copytree | scratch copy of `assemble-d4-typed.py`, copytree lines removed | 12/12 checks passed | removal is safe |
| N9 | D2 gate level | `python3 tools/gates/typed-pipeline-gate.py` / `--selftest-generalized` | 16/16 legs; 14/14 checks | D2 byte-identity at the gate |
| N10 | determinism | two builds + `--check` | `--check` exit 0 on the regenerated projection | deterministic |

## 5. Byte-identity proof (R3, measured 13:02–13:04Z)

- `python3 tools/d2-typed-labels.py --packet examples/culture-d2/packet.d2.yml --emit <scratch>` → `cmp` clean against the committed `examples/culture-d2/typed-labels.d2.yml` (sha `a3aa452c…`).
- `--json` document byte-identical to the pre-edit tool's document.
- `--selftest` → 50/50 (the round-8 matrices plus the new family controls).
- default gate 16/16; `--selftest-generalized` 14/14.

## 6. Re-pin cascade (NEW rows only; state at 13:07:39Z)

| surface | before | after / state | home |
|---|---|---|---|
| `examples/culture-d4/typed-labels.d4.yml` | `a59990bb…` | `cbcf997f…`, `--check` exit 0 | in place (uncommitted) |
| `tools/gates/typed-pipelines.json` | projection `a59990bb…`, adapter `null` | projection `cbcf997f…`, adapter `1ddad6a7…` | in place (sha `7b67e370…`) |
| `examples/culture-d4/expected-holds.json` | projector `0da0015f…`, projection `a59990bb…` | **stale** at review time | open |
| `tools/gates/expected/d4-typed-labels-check-gate/r20-post/` | r19-pre (read set named the D2 components) | new baseline id; inputs = packet + projector `76536a92…` + reader + projection `cbcf997f…` — **no D2 components** | landed |
| `examples/culture-d4/packet.d4.typed.yml` | carries no pin keys in `assembly:` | **runner expects pins** — open (F3) | open |
| `tools/assemble-d4-typed.py` | copytree of `examples/culture-d2` at `:416–419` | **still present** — open (F1) | open |
| round-20 re-pin row home | — | runner looks under `reports/round-20/repin/**` or `tools/gates/frozen/round-20/**`; neither exists | open (F4) |

## 7. Limits / open items

- The family key is the path shape (F6); a D4 packet outside the convention
  falls back to the D2 leg.
- The malformed-tag coercion (F5) is the one place the leg can apply a tag the
  grammar does not accept.
- `d3-projector-probe` is informational in the round runner: the projector over
  `examples/culture-d3/packet.gates.yml` exits 2 with a named parse error
  (`packet.materials[].id: expected a non-empty string, got None`), unchanged by
  this work; the green d3 leg is `tools/assemble-culture-d3.py --check` (exit 0).
- The frozen round-18 `repin-d2` manifest replays 11/11 and the round-11
  manifest 10/11 (row 1 was already could-not-evaluate pre-round-20), so the D2
  replay surfaces stay green under the projector edit.

## 8. Reproduction block

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
# the wart, pre-fix snapshot
(cd .scratch/r20-o/wart-mirror && python3 tools/d2-typed-labels.py \
   --packet examples/culture-d4/packet.d4.yml --json)   # exit 2, legacy error
# the fix, live revision
python3 tools/d2-typed-labels.py --selftest                          # 50/50
python3 tools/d2-typed-labels.py --check                             # d2, byte-identical
python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml \
   --check examples/culture-d4/typed-labels.d4.yml                   # exit 0
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml  # 19/19
python3 tools/assemble-d4-typed.py --selftest                        # 12/12
python3 reports/round-20/run-validation.py --check                   # read-only acceptance
```
