# Handoff packet v3 — the D4 third drill in the claim ledger (R20-D01..D04)

- topic: The design of handoff packet **v3** and of the exercise surface that
  renders it — extending the round-15 v2 envelope (`reports/round-15/handoff/
  packet-v2-05.{md,yml}`) with the **D4 furnace-league drill** as a third
  source: twelve D4 claims enter the ledger with the v2 uncertainty dimension
  `{status, basis}`, every D4 claim links into `examples/culture-d4/` records
  and the round-18 D4 receipts, and the round-19 routed wart (the projector's
  era-alias leg requiring the D2 alias component even for D4 packets) is
  carried as one typed, owner-routed unresolved claim until the round-20 **O**
  seat's per-family resolution lands. This document is a spec for the packet,
  impl, freeze and audit seats of R20-D; it renders no packet byte and edits no
  tool.
- sources: `reports/round-15/handoff/v2-design.md` (the v2 spec this design
  extends: §2 uncertainty schema, §3 link grammar, §5 field delta, §6 builder
  and control matrix); `reports/round-15/handoff/packet-v2-05.yml` +
  `.md` (the audited v2 bytes: 16 claims, statuses 8 supported / 5 partial /
  2 unresolved, 34 atomic edges, 27 manifest rows) and
  `reports/round-15/handoff/expected.json` (the v2 baseline: profile
  `kotodama-handoff-v2/1`, `links 50/50`, census 15 claims);
  `reports/round-15/handoff/contract-v2-audit.md` (the audit protocol and its
  named remainders, which §7 re-runs over v3);
  `tools/exercise-handoff-e2e.py` (the round-11 exercise: read set, field map,
  preflight, baseline and tamper controls — the surface v3 extends);
  `tools/harness/packet_uncertainty.py` and `tools/harness/packet_links.py`
  (the v2 semantic validators, whose measured behaviour §8 records);
  `examples/culture-d4/` (`packet.d4.yml`, `typed-labels.d4.yml`,
  `packet.d4.typed.yml`, `expected-holds.json`, `brief.md`, `ASSEMBLY.md`,
  `components/01-brief.yml` … `12-provenance.yml`);
  `reports/round-18/d4/` (`holds.md`, `determinism.md`, `manifest.md`,
  `replay.md`, `gate-runs-1..4.md`, `interop-1..3.md`, `review-1..4.md`,
  `neg-1..3.md`); `reports/round-19/validation.json` (the wart's routing note);
  `tools/assemble-d4-typed.py` (the selftest mirror comment that copies the D2
  tree — the wart's location); `tools/check-gate-battery.py`
  (`REGISTERED_GATE_NAMES`: nine gates, duty 2).
- couples: D-seats own `reports/round-20/handoff/claims-map.md` (the rows this
  design fixes) and `uncertainty-plan.md` (the status plan); the packet seat
  renders `packet-v3-*.{md,yml}` from §2–§5; the impl seat extends
  `tools/exercise-handoff-e2e.py` per §6; the freeze seat pins the v3 baseline
  per §6; the audit seat re-runs §7; the **O** seat's per-family alias
  resolution is the only writer of the evidence that flips D4-CL08 (§4); the
  orchestrator lands LOG.md.
- taken-from: the v2 design's own schema, grammar and control shapes; the D4
  artifacts' measured bytes; the round-18/19 receipts; the round-19 routed
  wart note. No new contract term is invented here, and no D4 fact is asserted
  that §8 did not measure.
- verified-at: 2026-10-18 (stamps UTC), lane root
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, baseline revision
  `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d` (round-20 declare). §8 records the
  commands and observed results: D4 record counts re-read from bytes, the
  12-claim uncertainty fixture run through `tools/harness/packet_uncertainty.py`
  (exit 0, `claims=12 findings=[]`), 46/46 filed link specs plus the 18
  coverage-map record ids resolved by `tools/harness/packet_links.py` (exit 0),
  and five negative controls that each fire their stable code.
- recheck: on any change to `examples/culture-d4/**` bytes, to the D4 tools or
  gates, to the two harness validators, to the contract, or to the round-18 D4
  receipts this design cites; before the v3 packet bytes are frozen; before
  the §7 audit re-run; and when the O seat lands the per-family alias
  resolution (§4).

## 0. Scope and out-of-province

v3 is **additive**: the v2 packet, its baseline and `frozen-verify.py` are
filed round-15 bytes and stay untouched (`reports/round-15/handoff/**` is
read-only for every R20-D seat). v3 renders a **new** packet from the same live
bytes plus the D4 read set, and the exercise keeps the round-11 (v1) path and
the v2 path green — the D claim's own wording: "v2 paths unchanged and green".
Corrections to this design are new files, never in-place rewrites.

Out of province, as in v2: canon standing and any import ruling
(lore-shokunin); rights, permission and publication (operator); general
research method (chousa); the D2 `12-rank-rules.yml` component's own bytes
(that file is the O seat's subject, read-only here). `uncertainty.status` stays
kotodama-side support language: per `corpus/knowledge/verification/
provenance-audit-ledger-format.md` §1 it never means improved, accepted,
import-ready or canon.

## 1. The v2 state being extended (measured, §8)

| v2 fact | measured value | source |
|---|---|---|
| packet | `kotodama.handoff.d2d3-e2e.v2.build05` @ `2.0.0` | `packet-v2-05.yml` |
| ledger | 15 claims: 8 supported / 5 partial / 2 unresolved | `expected.json` census; `contract-v2-audit.md` |
| links | 50/50 resolved; 34 atomic coupling edges | `expected.json` links block |
| manifest | 27 rows (26 file-backed + 1 inline glossary) | `contract-v2-audit.md` §4 table |
| gate scan | exit 0, `fields=16/16 glossary-entries=20 findings=0` | `expected.json` |
| baseline | profile `kotodama-handoff-v2/1`, frozen 2026-10-17 | `expected.json` |

D4 is now fully gate-verified (round 19, 19/19) and carries its own committed
hold set, projection and receipts — none of which any handoff packet has ever
carried. v3 closes that depth gap without moving a v2 byte.

## 2. The D4 claim set (rows in `claims-map.md`; statuses planned in `uncertainty-plan.md`)

Twelve claims, ids `D4-CL01`…`D4-CL12` (the `D2-CL01` naming precedent), each
typed per contract §6, each carrying `uncertainty: {status, basis}` in the v2
grammar (`grounding:` always; `restriction:` iff `partial`; `open:` + `owner:`
iff `unresolved`), each with ≥1 link that resolves into `examples/culture-d4/`
records or the round-18 receipts.

| id | kind | evidence_status | uncertainty | one-line claim (full wording in `claims-map.md`) |
|---|---|---|---|---|
| D4-CL01 | designer interpretation | invented | `supported` | the drill is a non-canon fourth example culture with twelve authored inputs; no real-world community, language or tradition described |
| D4-CL02 | generative rule | invented | `supported` | eras staged E0–E3 as ER-01…ER-04 with E3 reserved and unoccupied; seams declared per record; no dates |
| D4-CL03 | generative rule | invented | `supported` | rank is furnace right: RK-01…RK-04 declare authority/jurisdiction/eras/property/effect and the permitted wearer ranks the garments cite |
| D4-CL04 | generative rule | invented | `partial` | every garment GAR-01…GAR-06 owes its term through an unfilled `LEX-GAR-0n` slot; the gloss is a translated label off the sound channel; the sixth slot's owed kind is conditional |
| D4-CL05 | designer interpretation | derived projection (author-side) | `supported` | the typed channel: 74 labels (56/12/6), 16 findings with 15 hold-or-fail, projection byte-identical |
| D4-CL06 | designer interpretation | derived projection (author-side) | `supported` | the committed hold set: 15 holds / 1 note / 0 fails, twelve form holds keyed twice + three rank holds; the brief's six-row declaration reconciled by a named +9 delta |
| D4-CL07 | designer interpretation | derived projection (author-side) | `supported` | era/material reconciliation: six records resolved by declared row and slot identity, zero findings, conflicts carried not collapsed |
| D4-CL08 | designer interpretation | derived projection (author-side) | `supported` | the D4 packet declares no legacy alias handles; the alias leg now resolves family-local with an explicit documented skip — landed and measured (§4); pre-flip form `unresolved` retained in `claims-map.md` |
| D4-CL09 | designer interpretation | derived projection (author-side), holds open | `unresolved` | the D4 projection re-carries D2's rank-rule adaptation rows as `cannot-evaluate` with 13 unresolved items, 3 quarantine handles, 4 conflicts — none promoted |
| D4-CL10 | designer interpretation | invented | `partial` | the loan ledger is complete as declared while donor stage, fibre and donor speech stay unmodelled/`(to-verify)`; no real donor language named |
| D4-CL11 | screening statement | invented | `supported` | no real-language sweep, community consultation or rights ruling performed or claimed; comparators are repo corpus entries; the clearance question is routed, not carried by the status |
| D4-CL12 | candidate world-fact | candidate world-fact | `unresolved` | the D4 culture rides as namespaced candidates only; no baseline, entity keys or receipt surface exist |

Census after v3 (**landed branch — the live state**, §4): **27 claims — 16
supported / 7 partial / 4 unresolved** (v2's 8/5/2 plus D4's 8/2/2). If the O
seat's alias bytes are reverted, the pre-flip census returns — 15 supported /
7 partial / 5 unresolved, D4-CL08 `unresolved` (`uncertainty-plan.md` §3
declares both and requires the packet's `validation` to name which one it
measured). The v2 rows are carried verbatim, not re-typed: §6's
subset-equality control asserts it.

Hard rules for the packet seat (all measured against the live tools in §8):

1. No D4 claim promotes a hold: the twelve form holds, the three rank holds,
   the note, the 13 unresolved rank items and the four conflicts stay open in
   `open_questions` where they are unresolved.
2. No D4 claim asserts the wart is closed without the O evidence named in §4;
   the claim's status is a function of that evidence, not of the round's
   intent.
3. No D4 claim asserts a real-world referent, a date, a clearance or a canon
   standing. The drill's own provenance rows are the model.
4. The glossary payload stays the D3-derived 20 rows (v2's A-GLOSS row): no D4
   lexicon row enters it, so the gate scan stays `20/20`. The D4 lexicon is
   carried by claim links and the manifest record index instead.

## 3. Field-map delta vs the round-15 v2 design (v2-design.md §5 is the base)

| field | v2 (round 15) | v3 delta |
|---|---|---|
| `packet_id` | `kotodama.handoff.d2d3-e2e.v2.buildNN` | `kotodama.handoff.d2d3d4-e2e.v3.buildNN`; the supersedes clause names `packet-v2-05.*` as the earlier keyed build that stays filed and green (contract §9 supersedes discipline) |
| `packet_version` | `2.0.0` | `3.0.0`: the consumer-facing ledger gains a third source's rows and the manifest gains D4 rows — additive, but a consumer that pins the v2 census or manifest count is broken by it, so the major bump is declared and the delta is named in-packet |
| `contract_ref` | contract `1.0.0` digest `5f4c02bf…`, bilateral read pending | unchanged wording and digest; the pending bilateral read stays stated (OQ-V3-01) |
| `producer` / `recipient` / `request_ref` / `baseline_bible_ref` | exercise wording, deliberately unbound | unchanged in kind; the producer line names the v3 exercise revision and the D2/D3/D4 triple drill |
| `artifact_manifest` | 27 rows (26 file-backed + 1 inline) | adds the D4 read set (below) as new `A-nn` rows with live digests, sizes and per-row record counts; the A-GLOSS row is unchanged and stays D3-derived; the `record_ids` index gains the D4 families |
| `subject_refs` | 8 namespaced candidates (D3 + D2) | adds D4 candidates only in the same `cand:kotodama.d4.*` form, each with an in-repo witness (e.g. the culture itself, the furnace-right institution, the E0–E2 era stages, the garment-slot debt); all stay unresolved — no lore entity id is guessed |
| `scope` | two drills, no real place or dates | three drills: the D4 block names the fictional basin league, its isolate speech with one unmodelled sister variety, its fixture-relative E0–E3 stages, 54 lexemes, 6 garments each owing a slot, and restates the unscreened-ASCII status; the "no real place and no dates" rule is unchanged |
| `dependency_manifest` | D2/D3 tools and records with digests | adds the D4 tools (`tools/assemble-culture-d4.py`, `tools/assemble-d4-typed.py`), the two D4 gates (`tools/gates/d4-typed-labels-check-gate.py`, `tools/gates/d4-assembly-check-gate.py`), the two harness validators (already pinned in v2) and the D4 record ids the claims name; every pin is a digest or an exact record id — nothing floats on `latest` |
| `claim_ledger` | 15 rows (D2 ×2, D3 ×13) | 27 rows: the 15 v2 rows carried verbatim + `D4-CL01…D4-CL12` with the same seven-column shape (`claim_id \| kind \| evidence_status \| uncertainty_status \| uncertainty_basis \| links \| statement`) |
| `coupling_edges` | 34 atomic rows (BR01–BR05 + D2E-01..29) | adds the D4 edge families, one atomic row per live relation, each with `target_ids`, `limits`/`applicability` and the `claims` back-link: costume→slot (6), costume→material_ref (6), rank rule→wearer ranks (4), era→costume seam (4), borrowed-strata label→layer (6), name→formation/bases, symbol→era/register, festival/rite→calendar, contact→route. Counts are re-measured from bytes at build time, never copied from this table |
| `requested_decisions` | 10 rows (RD-01..08, RD-D2-01..02) | adds `RD-D4-01…RD-D4-05`: the sixth slot's delivery route (lexicon decision), the E3 reserved stratum (keep reserved / occupy / defer), the furnace-right rank set as candidate material, the loan donor stage (leave unmodelled / model / defer), the D4 baseline question; each with alternatives and a blocker naming the open claim |
| `validation` | 9 rows, commands + observed | adds the D4 legs: `tools/assemble-culture-d4.py --check`, `tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check <projection>`, the two D4 gates, `tools/assemble-d4-typed.py --emit/--check`, the expected-holds equality, the battery `9/9`, and the two v3 controls (v2-subset equality; the §4 alias evidence) — each with command and observed result, dated |
| `open_questions` | 7 rows (OQ-V2-01..07) | carried forward + `OQ-V3-*` naming every unresolved D4 claim with its lane and blocking status (§4, §9); `--require-oq` must stay at zero findings |

## 4. The era-alias leg: how v3 carries the round-19 wart

The wart (round-19 routing note, `reports/round-19/validation.json` notes
field): *the projector's era-alias leg requires the D2 alias component even for
D4 packets*. Its two measured locations:

- `examples/culture-d4/typed-labels.d4.yml` `era_reconciliation.basis` names
  `examples/culture-d2/components/12-rank-rules.yml era_aliases (A1)` as the
  alias source for the D4 projection;
- `tools/assemble-d4-typed.py:416` copies `examples/culture-d2` into the
  selftest mirror with the comment "the projector's era-alias leg requires the
  D2 alias component even for D4 packets (documented wart; routed) — the
  mirror must be faithful".

The O claim requires the alias component to resolve per packet family
(`d2` → the D2 rank-rules component; `d4` → a D4-declared alias source **or a
documented skip when the packet declares no era-alias rules**), with the D2
path byte-identical and the pins updated as new rows. The D4 packet declares no
legacy handles of its own — its delivered era values are already canonical
E0–E3 tags (`packet.d4.yml#era_tags`, `#era_records`), so the honest D4
outcome is the documented skip, and `era_reconciliation.basis` should stop
naming a foreign family's component.

**D4-CL08 is the one claim whose status is a function of another seat's
evidence.** The design fixes the decision rule; the packet seat applies it:

| live evidence at build time | D4-CL08 status | basis shape |
|---|---|---|
| the per-family resolution has **not** landed (basis still names the D2 component, mirror still copies the D2 tree) | `unresolved` | `grounding:` the two measured locations above; `open:` the per-family alias resolution has not landed, so the D4 packet cannot assert its alias leg is family-local; `owner:` kotodama O seat — blocking for this claim only |
| the resolution has landed: a `d4` run of the projector/adapter exits 0 **without** `examples/culture-d2` present in its mirror, and the projection's `era_reconciliation.basis` names the D4 packet's own era tags or an explicit documented skip | `supported` | `grounding:` the per-family resolution code path + the D4-side basis + the mirror-without-D2 run (command and observed result recorded in `validation`); `restriction:` not required unless the skip itself is conditional |

Controls for the flip (every fix carries a control): (a) the O evidence must be
a **run**, not a statement — a command, its exit code and its observed output,
recorded in the packet's `validation`; (b) the negative control is the same run
with the D2 tree restored — it must still exit 0 (the fix must not make the d2
path depend on the d4 tree); (c) the D2 path must stay byte-identical
(`tools/d2-typed-labels.py --selftest` — 39/39 at the round-18 revision,
measured **50/50** live — and the D2 gate's pinned outputs), because
`d2-typed-labels.py` is byte-pinned by several surfaces and any change re-pins
as a **new row**, never an in-place edit; (d) if the O seat lands a D4-declared
alias source instead of a skip, the basis must name that source's file and its
declaration — "no aliases" is a claim about the packet's bytes, not about the
tool's convenience.

**Measured landing (2026-10-18, during this filing).** The flip condition is
met on the live tree: the projection's `era_reconciliation.basis` names the D4
packet's own `named_eras` plus an explicit documented skip ("the packet
declares no reconciliation rows (the D2 leg's … is not read for family d4)"),
with `alias_rows` falling 10 → 4; `tools/assemble-d4-typed.py --selftest`
builds a mirror that copies only `examples/culture-d4` and exits 0 with
`12/12 checks passed`; and the D2 control is byte-identical —
`tools/d2-typed-labels.py --selftest` exit 0 `50/50`, and
`tools/gates/typed-pipeline-gate.py examples/culture-d2/packet.d2.typed.yml`
exit 0 `13/13 legs` with stdout sha256
`9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606`, equal to
the round-18 pre-generalization baseline. Caveats the packet seat must carry:
the O bytes were **uncommitted working-tree edits** at measurement time (HEAD
`caf1beac…`), so re-run these legs on the pinned revision before freezing; the
negative control (b) and the O claim's own gate-set receipts are still owed by
the O seat; and the flip is symmetric — a revert of the O bytes re-flips
D4-CL08 and the census.

If the flip happens mid-wave, the packet seat re-renders; if it happens after
the v3 baseline is frozen, the re-typed row is a **new** baseline row with the
reason recorded — the v3 freeze discipline of `corpus/knowledge/verification/
gate-frozen-run-standard.md` applies unchanged.

## 5. Serialization and the gate

- Markdown surface is the gate-facing serialization (contract §4 default), with
  the machine twin carrying native `uncertainty:` objects and `links:` lists —
  exactly the v2 split. Target: `python3 tools/gates/handoff-packet-check.py
  reports/round-20/handoff/packet-v3-*.md` → exit 0,
  `fields=16/16 glossary-entries=20 findings=0`.
- The glossary payload is the D3-derived 20-row block carried unchanged from
  v2 (A-GLOSS row, same source bytes). No D4 glossary row is added (§2 rule 4).
- All round-11/15 recognition hazards carry over unchanged: exact `## field_name`
  headings; no heading text containing a field token; the
  `canon_standing: not canonized` marker line; no unnegated `latest` in
  `dependency_manifest`; and no basis/status cell in a span that trips the
  canon-verb traps (`certifies/establishes/grants/awards … canon`,
  `this packet … is/constitutes … canon`, `canonized by/in lore`) — the v2
  design measured those traps reaching basis cells (probes C1/C2). The twelve
  D4 bases in `claims-map.md` are written to stay clear of them; the packet
  seat re-checks with the gate before freezing.
- `links:` specs use the v2 grammar (`path#token`), every spec in
  `claims-map.md` is written fully qualified (no `#token` shorthand), and every
  token is a literal that appears in the named file (§8 resolved the 46 filed
  specs and the 18 coverage-map record ids).
  Line anchors (`path:Lnnn`) are permitted but discouraged for D4 rows: the D4
  packet is generated, so a rebuild moves lines — prefer record-id tokens.

## 6. The v3 exercise surface (spec for the impl and freeze seats)

```
python3 tools/exercise-handoff-e2e.py                      # v1 path (round-11 baseline) — unchanged
python3 tools/exercise-handoff-e2e.py --profile v2         # v2 path (round-15 baseline) — unchanged
python3 tools/exercise-handoff-e2e.py --profile v3         # assemble -> link checks -> uncertainty -> gate -> v3 baseline
python3 tools/exercise-handoff-e2e.py --profile v3 --selftest
python3 tools/exercise-handoff-e2e.py --profile v3 --root DIR --baseline PATH
```

- Profiles select the read set, the packet identity and the baseline; the
  default stays the v1 profile so the filed round-11 path is not re-pointed.
  The v2 profile delegates to the round-15 surfaces (`packet-v2-05.*`,
  `expected.json`, `tools/harness/packet_{uncertainty,links}.py`) and asserts
  they are unchanged.
- v3 read set = the v2 read set **plus**: the twelve `examples/culture-d4/
  components/*.yml`, `examples/culture-d4/{brief.md,packet.d4.yml,
  typed-labels.d4.yml,packet.d4.typed.yml,expected-holds.json,ASSEMBLY.md}`,
  the two D4 tools, the two D4 gates, and the round-18 receipts the claims
  ground in (`holds.md`, `determinism.md`, `manifest.md`, `replay.md`).
  Each new file is an `A-nn` manifest row with a live digest; the read-set
  snapshot-before/after preservation check extends to it.
- v3 asserts, in this order: (1) read-set digests match the frozen v3 baseline;
  (2) preflight (16 fields, non-canon marker, licensed glossary vocabulary, no
  floating version); (3) **v2-subset equality** — the 15 v2 claim rows
  (id, kind, evidence_status, status, basis, links) parsed out of the v3
  ledger are identical to the v2 packet's rows after whitespace normalization
  (any drift is `E2E-DIGEST`, and the v2 packet bytes are additionally
  digest-pinned); (4) D4 links resolve (`packet_links.py`, exit 0);
  (5) uncertainty census equals the declared 27 claims / 16 / 7 / 4 in the
  landed branch (or 27 / 15 / 7 / 5 if the O bytes are reverted) with
  `--require-oq` exit 0; (6) the shape gate over the isolated copy
  (exit 0, `16/16 + 20/20 + 0`); (7) the frozen packet digest and glossary id
  set; (8) preservation (no read-set file changed while the run ran).
- Exit codes and stable codes extend the existing families: `E2E-DIGEST`,
  `E2E-COUNT`, `E2E-GATE`, `E2E-SCAN`, plus `E2E-UNC` (uncertainty findings)
  and `E2E-LINK` (link findings); `E2E-ARTIFACT` / `E2E-BASELINE` / `E2E-DATA`
  keep their meanings. No traceback on any path.
- `--selftest` control matrix (each mutation expects its stable code; every
  control is a copy, never the live tree):

| control | mutation | expected |
|---|---|---|
| positive | none | exit 0; `16/16 + 20/20 + 0`; links all resolve; census 27/16/7/4 in the landed branch (or 27/15/7/5 pre-flip) |
| m1 | drop one D4 claim row | `E2E-COUNT` (census) |
| m2 | D4 status token `tentative` | `E2E-UNC` |
| m3 | duplicate a D4 basis | `E2E-UNC` |
| m4 | `partial` row without `restriction:` | `E2E-UNC` |
| m5 | `unresolved` row without `owner:` or without an OQ reference | `E2E-UNC` (with `--require-oq`) |
| m6 | D4 link selector `packet.d4.yml#ER-99` | `E2E-LINK` |
| m7 | D4 link to a file outside the v3 read set | `E2E-LINK` / `E2E-DIGEST` |
| m8 | re-type one v2 row (e.g. change a v2 basis) | `E2E-DIGEST` (subset equality) |
| m9 | add a D4 glossary row | `E2E-SCAN` (glossary count ≠ 20) |
| m10 | basis cell tripping the canon-verb trap | gate exit 1 → `E2E-GATE` |
| m11 | D4-CL08 typed `supported` with a basis lacking the §4 run witness (the landed form's own guard) | `E2E-UNC` — the design's rule 2, enforced by the packet's validation cross-check |
| m12 | digest tamper in an isolated copy | `E2E-DIGEST` |
| isolation / preservation | foreign cwd; read-set digests before/after | identical result / unchanged |

- Baseline siting: the v3 baseline is a **new** file under
  `reports/round-20/handoff/` (never under `tools/gates/expected/**` or
  `tools/gates/frozen/**` — the battery reads every `expected.json` under those
  roots and a non-gate baseline there is an `UNKNOWN` exit-2). It pins: profile,
  packet sha256s, gate scan + stdout digest, the uncertainty census, the link
  resolution counts, the v2-subset equality result, the D4 alias evidence state
  (landed / not landed), and an `inputs` digest map over the full v3 read set.
- One stable summary line for `reports/round-20/run-validation.py`, e.g.
  `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=<n>/<n>
  claims=27 statuses=16/7/4 v2_subset=equal alias_leg=<landed|open>
  packet_sha256=<…>`.

## 7. What the round-15-style contract audit should find over v3

Expected verdict: **semantic PASS on the v2 findings and on the new D4 rows**
— every claim typed, every basis unique, witness-resolvable and
clause-complete; every D4 link resolving into `examples/culture-d4/` records;
every edge atomic with per-edge applicability and a claim back-link. Expected
**remaining gaps, named with owners** (the claim's alternative branch):

1. bilateral same-revision read of contract `1.0.0` still pending — owner lore
   + both lanes; blocks first transfer only (OQ-V3-01);
2. round-8 L0 contract-digest question (`50c4c2f2…` premise vs `5f4c02bf…`) —
   owner integrator/lore, non-blocking (OQ-V3-02);
3. no kotodama-side §1 read record yet — owner kotodama orchestrator (OQ-V3-03);
4. **the round-19 alias wart — landed, to be verified**: the O seat's
   per-family resolution is present on the live tree and was measured here
   (§4, §8.10: the D4-side skip, the mirror-without-D2 run, the byte-identical
   D2 control). The audit should **verify the landing** on the pinned revision
   rather than record an open remainder, and should demand the O seat's
   negative control (the same run with the D2 tree restored) and its own
   gate-set receipt; if the O bytes were reverted, D4-CL08 re-flips to
   `unresolved` and `OQ-V3-04` re-opens as a new build (OQ-V3-04, closed);
5. D4's own residuals (12 form holds + 3 rank holds + 1 note; 13 unresolved
   rank items; 4 conflicts) carried open in the packet, not resolved by it
   (OQ-V3-05);
6. the D4 culture's baseline/entity-key question for lore (OQ-V3-06).

## 8. Design evidence (commands and observed results, 2026-10-18)

```sh
export TMPDIR=$PWD/.scratch            # lane rule, before every scratch write
python3 .scratch/r20d/…                # scratch measurement scripts (gitignored)
python3 tools/harness/packet_links.py --links "<filed specs (46 pre-flip, 48 post-flip) + 18 coverage ids>"   # §8.2
python3 tools/harness/packet_uncertainty.py --claims-json .scratch/r20d/claims-postflip.json --json
```

1. **D4 inventory** (re-read from bytes; `.scratch/r20d/d4-inventory.txt`):
   `packet.d4.yml` delivers 153 distinct namespaced record ids over 22 families
   — lexicon 54, names 8, pantheon 6, symbols 8, costumes 6, materials 5,
   rank_rules 4, era records 4 + 4 tags, form_slots 6, provenance 9, festivals
   6, rites 4, motifs 4, narratives 3, roles 6, calendar 1, contact 2, routes
   3, cross-culture review 3, cloth sources 2, layers 2, constructions 3 — plus
   14 contract rules `RG-01..RG-14`. Pair counts: 6 costumes carry a
   `form_slot`, 6 carry a `material_ref`, 4 rank rules carry `wearer_ranks`,
   4 era records carry `costume_seam`. Digests: `packet.d4.yml`
   `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3`;
   `typed-labels.d4.yml`
   `a59990bbfe5a8992ffa6e67e9b3e43e7ff477df9fc754e5af92b6f40d23fe11d`;
   `packet.d4.typed.yml`
   `f63ed5315f6889f8c411b4dda2e69d43b05ce4fc6152f941a2b36bb1d7a13ebe`;
   `expected-holds.json`
   `09490a2756d123ebbc2023be89fc01c95ec2f8cc7e6df42ecc5b8cd438058e98`.
2. **Link witnesses** — two measurements, both live. (a) The 48-spec draft
   list this design was built from, resolved by
   `tools/harness/packet_links.py --links "<list>"` → exit 0,
   `links=48 resolved=48 findings=0`. (b) The union of the link lines **as
   filed** in `claims-map.md` (46 unique specs, re-extracted from the markdown)
   → exit 0, `links=46 resolved=46 findings=0`; and the 18 record-id specs the
   coverage map cites (`#L-49`, `#NM-01`, `#SYM-01`, `#FES-01`, `#RIT-01`,
   `#CAL-01`, `#RT-01`, `#PAN-01`, `#CC-01`, `#CS-01`, `#CX-01`, `#MOT-01`,
   `#MYTH-01`, `#ROL-01`, `#CMAT-01`, `#RG-01`, `#ER-02`,
   `typed-labels.d4.yml#findings_total`) → exit 0, `links=18 resolved=18
   findings=0` (commands recorded in `review.md` §2).
3. **Claim grammar** — the twelve rows **as written in `claims-map.md`** were
   re-extracted from the markdown (statement, kind, evidence status, status,
   basis, links) and run through `tools/harness/packet_uncertainty.py
   --claims-json … --json` → exit 0, `claims=12 findings=[]`. Five negative
   controls fired their stable codes: duplicate basis → `U-BASIS-DUPLICATE`;
   `partial` without `restriction:` → `U-BASIS-NO-RESTRICTION`; `unresolved`
   without `owner:` → `U-BASIS-NO-OWNER`; status `tentative` →
   `U-STATUS-VOCAB`; basis `grounding: unknown` → `U-BASIS-SHORT`.
4. **Link negative control** — `… --links "packet.d4.yml#ER-99,
   typed-labels.d4.yml#no_such_block, expected-holds.json#counts"` → exit 1,
   two `L-TOKEN-MISSING` findings and the third spec `ok` — the design's
   witnesses are real and the resolver discriminates.
5. **D4 typed-channel counts** — read from `typed-labels.d4.yml`:
   `coverage` = typed_labels 74, labels_by_kind 56/12/6, findings_total 16,
   findings_hold_or_fail 15, label_findings_fail 0, label_findings_hold 12,
   rank_rules_unresolved_items 13, rank_quarantine_handles 3, conflicts 4,
   reconciliation_records 6; `typed_labels.stats` = `{fail: 0, hold: 12,
   labels: 74}`; label rows: 74, statuses supplied 62 / to-verify 12;
   13 `act_rules` all `adapt_status: cannot-evaluate`. `expected-holds.json`:
   `counts {hold: 15, note: 1, fail: 0}`, by id `D2L-FORM-UNRESOLVED` ×12,
   `D2L-RANK` ×3, one `D2L-RANK` note at `SR-01#a|SR-01#b`.
6. **The brief's declaration** — `components/01-brief.yml`
   `contract.hold_set_declaration` names six holds, `counts {hold: 6, note: 0,
   fail: 0}`, with acceptance criterion `A-07` requiring the typed pipeline's
   finding set to equal it; the measured emitted set is 15/1/0 — the +9 hold /
   +1 note delta is the reconciliation `reports/round-18/d4/holds.md`
   dispositions (cited by D4-CL06).
7. **The wart's locations, pre-flip and landed** — pre-flip (measured
   earlier the same day): `typed-labels.d4.yml` `era_reconciliation.basis[0]` =
   `examples/culture-d2/components/12-rank-rules.yml era_aliases (A1)`, and the
   `tools/assemble-d4-typed.py` selftest copied `examples/culture-d2` with the
   wart comment (line 416 in the then-delivered bytes); round-19's routing note
   is `reports/round-19/validation.json` `notes`. Landed (measured after the O
   seat's edits, §4): the basis names `examples/culture-d4/packet.d4.yml
   named_eras (A1)` plus the explicit skip, `alias_rows` 10 → 4, and the
   adapter's selftest mirror copies only `examples/culture-d4`.
8. **The three `(to-verify)` packet lines** — `packet.d4.yml` lines 957
   (`donor_stage`), 1557 (`composition`/fibre), 2266 (`donor` speech stage),
   all marked unmodelled — the witnesses D4-CL10's restriction names.
9. **Battery surface** — `tools/check-gate-battery.py` declares
   `REGISTERED_GATE_NAMES` = seven structural gates + the two D4 adapters
   (nine; duty 2), so v3's validation can cite a default run of `9/9`.
10. **Flip measurements (2026-10-18, after the O edits)** —
    `python3 tools/assemble-d4-typed.py --selftest` → exit 0, `12/12 checks
    passed` in a mirror without the D2 tree;
    `python3 tools/d2-typed-labels.py --selftest` → exit 0, `50/50 checks
    passed`; `python3 tools/gates/typed-pipeline-gate.py
    examples/culture-d2/packet.d2.typed.yml` → exit 0, `13/13 legs passed`,
    stdout sha256 `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606`
    (equal to the round-18 pre-generalization baseline);
    `git status --porcelain examples/culture-d2/` → empty. The twelve rows were
    then re-extracted from the updated `claims-map.md` and re-validated:
    `claims=12 findings=[]`, census 8 supported / 2 partial / 2 unresolved, and
    the 48 unique link specs resolved `48/48` (`review.md` §2 row 19).

## 9. Ordering, open items, to-verify for the owners

- **Ordering**: this design → D-seats fix `claims-map.md`/`uncertainty-plan.md`
  → O seat lands the per-family alias resolution (or does not; D4-CL08's rule
  decides) → packet seat renders `packet-v3-*` and records `validation` rows
  with live commands → impl seat extends `tools/exercise-handoff-e2e.py` per §6
  → freeze seat pins the v3 baseline after the packet bytes stop moving
  (single writer; re-pin only as a new row with a recorded reason) → audit seat
  re-runs §7 → orchestrator lands LOG.md. If `examples/culture-d4/**` or the D4
  tools move mid-round, freeze only after they stop; a moved D4 byte re-pins as
  a new row, never an in-place edit.
- `to-verify` (packet/impl seats): the live D4 pair counts and record-id total
  at build time (never copied from §8); whether `run-validation.py` wants the
  new codes verbatim or a reduced exit code; whether the v3 packet should carry
  the round-18 receipts as manifest rows or as claim links only (this design
  proposes links for the receipts, rows for the delivered artifacts and tools —
  the packet seat may narrow it, naming the reason in `validation`).
- Non-blocking, kotodama-owned: none new. The v2 OQ items carry forward with
  their lanes and blocking status unchanged, and the D4 items are the three
  unresolved claims' own questions (§4, §7).
- This file's footprint: `reports/round-20/handoff/design.md` plus gitignored
  scratch under `.scratch/r20d/`. No filed round-8..19 artifact, corpus file,
  tool, packet or sibling path was written.
