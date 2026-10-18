# R22-D01–D02 — exact D2 → D4 projection bleed

Date: 2026-10-18. Assignment: bleed census and source trace only. Axes: D/depth (exact owned-field provenance), O/operability (source injection and paired controls), C/calibration (determinism is not semantic isolation). The family-clean rule is in `reports/round-22/bleed/design.md` (R22-D03).

## Evidence boundary and verdict

All measurements below use the declared round-22 baseline revision `46a03257ee75dd8f685a105e47da3f45a0154172`, not mutable files from another worker's in-progress implementation. All source and projection line numbers in this report refer to that revision. Only this report and `design.md` are this seat's outputs; no source, example, filed round, validator, profile, or frozen expectation was changed.

**A11–A12's 24 D2 rank-source references are reproduced exactly. They are citation-bearing fields in the D4 projection's `rank_rules` block, not 24 rows in `typed_labels.labels`.** The latter has zero fully qualified D2 record paths, but separately misattributes every generated label's owner/component and applies D2's romanization scheme to supplied forms. The main rank bleed is embedded D2 fixture data selected unconditionally by the projector; removing the D2 examples directory cannot remove it.

The source-boundary defect was already filed as A21-D4-XF-01 in `reports/round-21/adjacency/ledger.json:93-110`; `reports/round-21/adjacency/A11-A12-handoff.md:23-29` supplies the prior census and routing. The old handoff's D4-CL09 explicitly disclosed inherited D2 residuals (`reports/round-20/handoff/packet.md:150`), so the correct claim is **filed but unfixed**, not newly undiscovered or undisclosed. Disclosure and `adapt_status: cannot-evaluate` do not satisfy D4's no-import boundary (`examples/culture-d4/components/01-brief.yml:55-75,111-121`).

Baseline SHA-256 values (command C1–C3 below, 2026-10-18T14:42:15.772158+00:00):

- `tools/d2-typed-labels.py`: `76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb`.
- `examples/culture-d4/typed-labels.d4.yml`: `cbcf997f5f38fac89b0fb1b6a6841ec42c9041a2599df44083ddefc5c22cfb4f`.
- `examples/culture-d4/packet.d4.yml`: `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3`.
- Unchanged-D2 control, `examples/culture-d2/typed-labels.d2.yml`: `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`.

## C1 — the exact A11–A12 citation census

Observed at 2026-10-18T14:40:22.194616+00:00, independently re-run at 14:42:15.772158+00:00 by the command below: **24 matching string fields, 22 distinct citation strings**, all under `$.rank_rules`. Each table path is relative to `$.rank_rules`; each citation starts with `examples/culture-d2/components/12-rank-rules.yml:`. The last column is the citation's line in baseline `examples/culture-d4/typed-labels.d4.yml`.

| Field path | Record/rank | D2 source line suffix | D4 projection line |
|---|---|---|---|
| `act_rules[0].cite` | SR-01#a | 318-329 | 335 |
| `act_rules[1].cite` | SR-01#b | 318-329 | 357 |
| `act_rules[2].cite` | SR-02#a | 330-341 | 379 |
| `act_rules[3].cite` | SR-03#a | 342-353 | 399 |
| `act_rules[4].cite` | SR-04#a | 354-365 | 419 |
| `act_rules[5].cite` | SR-05#a | 366-377 | 439 |
| `act_rules[6].cite` | SR-06#a | 378-389 | 460 |
| `act_rules[7].cite` | TR-01#a | 392-404 | 481 |
| `act_rules[8].cite` | TR-02#a | 405-417 | 503 |
| `act_rules[9].cite` | TR-03#a | 418-430 | 523 |
| `act_rules[10].cite` | TR-04#a | 431-442 | 542 |
| `act_rules[11].cite` | TR-05#a | 443-455 | 564 |
| `act_rules[12].cite` | TR-06#a | 456-468 | 584 |
| `assay_gaps[0].cite` | WR-01 | 199-211 | 603 |
| `assay_gaps[1].cite` | WR-03 | 225-237 | 608 |
| `calibration_flags[0].cite` | SR-06 | 386 | 615 |
| `calibration_flags[1].cite` | TR-05 | 451 | 620 |
| `calibration_flags[2].cite` | WR-05 | 259 | 625 |
| `entitlement_edges[0].cite` | fair-stranger | 189 | 641 |
| `entitlement_edges[1].cite` | herd-master | 171 | 647 |
| `jurisdiction_gaps[0].cite` | JU-3 | 514-520,528-533 | 780 |
| `jurisdiction_gaps[1].cite` | SR-06 | 378-389 | 785 |
| `jurisdiction_gaps[2].cite` | WR-02 | 212-224 | 790 |
| `residuals[0].cite` | WR-06#b | 264-276 | 1240 |

The partition is `act_rules=13 + assay_gaps=2 + calibration_flags=3 + entitlement_edges=2 + jurisdiction_gaps=3 + residuals=1 = 24`. The duplicated citation strings are the two SR-01 acts and the SR-06 act/jurisdiction-gap pair; counting unique citation strings would therefore understate A11–A12's reference-occurrence census.

### What that literal count omits

The same dated C1 census finds **28** string fields containing `examples/culture-d2/` anywhere in the projection. Besides the 24 rank-source fields:

- `rank_rules.quarantine[0].cite` → `examples/culture-d2/packet.d2.yml:2007` (GAR-06, projection line 1221).
- `rank_rules.quarantine[1].cite` → `examples/culture-d2/components/11-costumes.yml:102` (WI-2, line 1227).
- `rank_rules.quarantine[2].cite` → `examples/culture-d2/components/11-costumes.yml:103-107` (WI-3..WI-7, line 1233).
- `era_reconciliation.basis[1]` (line 165) says the D2 costume component **is not read** for D4. This is explanatory negative provenance, not an imported D2 record; a broad substring ban would mistake it for a source binding.

Another **14** rank-provenance string fields omit the family prefix but still name D2's component:

- Five `rank_rules.gate_rank_rules[*].cite` fields, for WR-02#g / WR-03#g / WR-04#g / WR-08#g / WR-09#g, read `12-rank-rules.yml:212, :225, :238, :290, :303`, respectively (projection lines 663, 688, 712, 736, 758).
- Nine `rank_rules.normalized_rules[*].source.component` fields, for WR-01..WR-09, all read `12-rank-rules.yml`; the adjacent `source.line` values are 199, 212, 225, 238, 251, 264, 277, 290, 303 (projection lines 830-833 through 1207-1210).

Thus there are **41 D2 rank-provenance reference-bearing fields** when full rank/costume/packet citations and these short component references are combined: 24 + 3 + 14. This is a broader, explicitly defined field census, not a replacement for the filed 24-reference metric. The explanatory basis line is excluded from the 41.

The rank ledger carries actual D2 dress-law content, not only stale path labels: Valley Moot statutes, herd-master/fair-stranger ranks, lowland-plant-cloth/hem-cords/mast-sash properties, storm-law recitation and archive cords. Its `garment_refs` include GAR-07/GAR-08 and `property.slot_ref` includes CMAT-06, outside D4's delivered garment/material sets. `normalized_rules` has nine D2 WR records; `gate_rank_rules` has five projected records; `act_rules` has thirteen emitted acts for twelve SR/TR source rules, because SR-01 splits into two. The projection's component coverage is the D2 total of 21, whereas C2 reads four D4 RK records directly from the packet.

## C2 — exactly which typed labels are affected

The dated C1/C2 command below measures **74 labels**: 12 translated-label, 56 native-form, six borrowed-strata. **Zero label rows contain a fully qualified `examples/culture-d2/` path.** Do not call the 24 rank citations 24 contaminated typed-label rows.

Their generated provenance is nevertheless D2-specific:

| Label IDs | Rows | Wrong owner/source in D4 projection | Actual D4 owner |
|---|---|---|---|
| GAR-01..GAR-06 | 6 | owner `11-costumes`, source `11-costumes.yml` | `09-costumes` / `09-costumes.yml` |
| LEX-GAR-01..LEX-GAR-06 | 6 | owner and source `11-costumes` | `09-costumes` / `09-costumes.yml` (or precise packet block) |
| L-01..L-54 | 54 | owner `05-lexicon`, source `05-lexicon.yml` | `04-lexicon` / `04-lexicon.yml` |
| NM-01..NM-08 | 8 | owner `13-naming`, source `13-naming.yml` | `05-naming` / `05-naming.yml` |

All 74 owner/component attributions are stale. The 62 supplied native/borrowed label rows (L-01..L-54 and NM-01..NM-08) use `scheme: d2-roman`; the twelve translated/null-slot labels use null schemes with reasons. D4 actually declares `orthography.scheme: D4-roman-1 (lowercase ASCII; length as double vowels; diphthongs ai/au; no diacritics)` (`examples/culture-d4/components/03-orthography.yml:38-53` and the parsed packet). A lowercase `d4-roman` substitution would be an invented scheme, not the declaration.

C2 independently compares every non-null label text with the D4 packet: **68 exact matches, six null owed-slot labels, no text mismatch**. Thus this census proves wrong projection ownership/scheme metadata, not that D4's supplied label texts were copied from D2. L-49..L-54 are D4's declared linguistic borrowed strata and keep their packet borrow ledgers; that is unrelated to the unintended D2 fixture import.

C2 reads `packet.rank_rules` as exactly `RK-01, RK-02, RK-03, RK-04`, all `effect: permit`. Their four properties are local hide, the shoulder town stamp, the maker's stamp, and imported salt-road cloth. They come from `examples/culture-d4/components/09-costumes.yml:133-137`; none is the D2 WR/SR/TR system.

## D02 — where the projector injects foreign ownership and data

At the pinned source revision:

1. `tools/d2-typed-labels.py:925` defines `C12` as the fully qualified D2 rank-rule source. Lines 927-1003 define D2 rank/rite tokens and GAR-specific rank resolutions. `N()` at lines 1016-1028 gives every normalized rule the short component `12-rank-rules.yml`.
2. `NORMALIZED` at lines 1033-1104 embeds the D2 WR data. `ACT_RULES` (1106-1157), `RESIDUALS` (1158-1160), `CALIBRATION_FLAGS` (1161-1165), `ENTITLEMENT_EDGES` (1166-1169), `QUARANTINE` (1170-1177), `CONFLICT_TRIAGE` (1178-1187), `JURISDICTION_GAPS` (1188-1192), and `ASSAY_GAPS` (1193-1196) embed the other foreign rows and citation suffixes. `COMPONENT_RULE_IDS` at line 1197 declares the 21-rule D2 census; it is not derived from D4's packet.
3. `project_to_gate()` at lines 1199-1224 produces short citations from each normalized D2 source, using D2-only value/effect mappings. `build_payload()` at 1235-1258 packages those globals and derives the coverage/unresolved totals, with **no packet/family argument**.
4. `run_pipeline()` calls `parse_typed_labels(packet)` at line 2601 and **unconditionally calls `build_payload()` at line 2613**, before the separate `family_alias_leg(packet_path, packet)` at line 2614. The already-local alias leg then annotates the foreign rank ledger with D4's alias basis. Its existence does not make the rank rows D4-local.
5. `conflicts(ledger['gate_rank_rules'])` / `act_conflicts(ledger['act_rules'])` at lines 2630-2637 generate three hold findings and one note using D2 triage. Lines 2655-2663 copy their D2 counts into D4 coverage. Lines 2677-2679 hard-code D2 `name`/`canon` metadata (visible at D4 projection lines 28/329), and line 2685 emits the foreign ledger as the D4 projection's unqualified `rank_rules` field.
6. Label metadata is a distinct hard-coded path: `_costume_label` at 493-514 sets `11-costumes`; `_form_slot_label` at 517-537 takes the same owner from `project_labels` line 624. `_lexicon_label` at 540-579 sets `05-lexicon`/`d2-roman`; `_name_label` at 582-602 sets `13-naming`/`d2-roman`. The text values themselves come from the passed packet. A family-aware fix must also preserve the costume slot-ID requirement currently guarded by the literal owner `11-costumes` in `validate_labels` line 763.

The secondary propagation is real: `tools/assemble-d4-typed.py:276-288` copies projection findings into the typed packet. Removing full D2 citations alone would leave the three D2 rank holds and one D2 rank note unless their source calculations are also family-selected. The inherited four findings are `SR-01#a|SR-01#b` (note), `TR-04#a|TR-06#a`, `WR-02#g|WR-09#g`, and `WR-08#g|WR-09#g` (holds). C1 measures the severity census; their exact rows remain in baseline `findings` at projection lines 294-321.

## C3 — controls establish hard-coded contamination

On 2026-10-18T14:40:59.230415+00:00, repeated in the combined run at 14:42:15.772158+00:00, two in-memory baseline helper probes passed:

- Positive source trace: `build_payload()` equals the entire filed D4 `rank_rules` object after removing only `era_aliases_applied` and `era_aliases_basis`, which the family alias leg adds later.
- Negative dependency control: replace that helper namespace's `load_packet_file` with a raising sentinel; `build_payload()` still returns that exact same D2 ledger and its 24 rank-source references. No disk reader is needed to inject the constants.

These are **2/2 helper probes**, not a projector/gate/validator pass and not the proposed fixed-source regression suite. They explain why the existing baseline D4 mirror check (`tools/d2-typed-labels.py:3061-3100`) can reproduce the bleed without a D2 examples tree. The D4 deterministic check recorded by A11–A12 on 2026-10-18T14:01:09Z (`python3 tools/gates/d4-typed-labels-check-gate.py`, exit 0) verifies byte equality, not family-clean record provenance.

## Reproducible combined C1/C2/C3 command and result

Executed from the lane repo on **2026-10-18T14:42:15.772158+00:00**, exit **0**. It reads baseline Git objects, executes existing helper definitions in memory, and writes no scratch files, fixtures, imports/bytecode, or validator outputs. `TMPDIR` is still explicitly set before the command. No round validator was run.

```bash
export TMPDIR=$PWD/.scratch; export PYTHONDONTWRITEBYTECODE=1; python3 - <<'PY'
from collections import Counter
from datetime import datetime, timezone
import copy, hashlib, json, pathlib, subprocess
rev='46a03257ee75dd8f685a105e47da3f45a0154172'
def blob(p): return subprocess.check_output(['git','show',f'{rev}:{p}'])
def leaves(v,p='$'):
    if isinstance(v,dict):
        for k,x in v.items(): yield from leaves(x,f'{p}.{k}')
    elif isinstance(v,list):
        for i,x in enumerate(v): yield from leaves(x,f'{p}[{i}]')
    elif isinstance(v,str): yield p,v
p=json.loads(blob('examples/culture-d4/typed-labels.d4.yml'))
ranksrc='examples/culture-d2/components/12-rank-rules.yml'
hits=[(k,v) for k,v in leaves(p) if ranksrc in v]
full=[(k,v) for k,v in leaves(p) if 'examples/culture-d2/' in v]
short=[(k,v) for k,v in leaves(p['rank_rules']) if '12-rank-rules.yml' in v and ranksrc not in v]
labels=p['typed_labels']['labels']
print('date',datetime.now(timezone.utc).isoformat(),'revision',rev)
for path in ('tools/d2-typed-labels.py','examples/culture-d2/typed-labels.d2.yml','examples/culture-d4/typed-labels.d4.yml','examples/culture-d4/packet.d4.yml'):
    print('sha256',path,hashlib.sha256(blob(path)).hexdigest())
print('rank-citations',len(hits),'unique-strings',len(set(v for _,v in hits)))
print('groups',dict(Counter(k.split('.')[2].split('[')[0] for k,_ in hits)))
print('full-D2-path-fields',len(full),'short-rank-source-fields',len(short))
print('labels',len(labels),'kinds',dict(Counter(x['kind'] for x in labels)))
print('label-D2-path-rows',sum(any('examples/culture-d2/' in s for _,s in leaves(x)) for x in labels))
print('owners',dict(Counter(x['owner'] for x in labels)))
print('components',dict(Counter(x['source']['component'] for x in labels)))
print('schemes',dict(Counter(x.get('scheme') for x in labels)))
print('rank-arrays',{k:len(v) for k,v in p['rank_rules'].items() if isinstance(v,list)})
print('rank-findings',dict(Counter(x['severity'] for x in p['findings'] if x['id']=='D2L-RANK')))
gate='tools/gates/costume-era-consistency-gate.py'
g={'__name__':'bleed_census_reader','__file__':str(pathlib.Path(gate).resolve())}
exec(compile(blob(gate),f'{rev}:{gate}','exec'),g)
packet=g['parse_packet'](blob('examples/culture-d4/packet.d4.yml').decode())
print('packet-ranks',len(packet['rank_rules']),[x['id'] for x in packet['rank_rules']],dict(Counter(x['effect'] for x in packet['rank_rules'])))
lookup={x['id']:x[field] for block,field in (('costumes','garment'),('lexicon','term'),('names','name')) for x in packet[block]}
print('packet-text-matches',sum(x['id'] in lookup and x['text']==lookup[x['id']] for x in labels),'null-owed-slots',sum(x['id'].startswith('LEX-GAR-') and x['text'] is None for x in labels))
print('packet-scheme',packet['orthography']['scheme'])
source='tools/d2-typed-labels.py'
s={'__name__':'bleed_census_projector','__file__':str(pathlib.Path(source).resolve())}
exec(compile(blob(source),f'{rev}:{source}','exec'),s)
expected=copy.deepcopy(p['rank_rules'])
for k in ('era_aliases_applied','era_aliases_basis'): expected.pop(k)
assert s['build_payload']()==expected
s['load_packet_file']=lambda *a,**kw: (_ for _ in ()).throw(AssertionError('disk loader forbidden'))
assert s['build_payload']()==expected
print('helper-controls 2/2: constant-ledger equals D4; disabling disk loader leaves it unchanged')
PY
```

Key output: `rank-citations 24 unique-strings 22`; groups `13/2/3/2/3/1`; full-D2-path fields 28; short rank-source fields 14; labels 74 with zero label D2-path rows; owner counts `12/54/8`; scheme counts `null=12,d2-roman=62`; D4 packet rank rows four, all permit; packet-text matches 68 and null owed slots six; helper controls 2/2.

The exact table above was checked against the baseline serialized JSON and the source constants. Commands for additional row-level inspection are read-only: walk the same `hits` list and print each `(field path, citation)`; for the displayed row identity, index its enclosing `rank_rules` array and use `id`, `rule`, or `rank` as applicable. This does not require a validator or a mutable regenerated projection.

## Handoff limitation

This seat characterizes the defect and supplies a rule/control contract; the implementation, new re-pins, consumer updates and final green gates belong to their assigned writers. The proposed fix must not be represented as resolving D2's historical rank debts or filling D4's six owed terms. Existing filed rounds remain unchanged; new measurements must name the post-fix revision/digests and their command/date. No canon, lore acceptance, real-world truth, or permission/clearance inference follows from this engineering repair.
