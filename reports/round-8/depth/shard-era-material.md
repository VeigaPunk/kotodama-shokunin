# R8-D05 — Reconciliation shard: scoped era/material reconciliation for `tools/d2-typed-labels.py`

- worker: DEPTH R8-D05 (round 8, shard of claim D); deliverable: this file only.
- integration target: D02 owns `tools/d2-typed-labels.py` and pastes the §4 block; this shard never writes the tool file. As of 2026-10-17 ~17:31 the block is integrated there and the tool's `--selftest` passes 34/34 including this block's 29 controls (§6.9).
- date: 2026-10-17. Baseline revision for reads: `e7ca0faeb6680fa9891b907be628d9db578c28f4` (round-8 baseline; the working tree is edited by sibling workers).
- interface anchors: D01's design spec (`reports/round-8/depth/design-spec.md` §2–§3, §6, §8.1) is the verdict/class authority this block was re-aligned to after it landed; D03's parser shard (`reports/round-8/depth/shard-parser.md` §4.2–4.3) defines the typed-label schema and the parse-side checks. This shard supplies the reconciliation semantics those checks stop short of: era label systems per scope, material availability per scope, cross-scope bridges, carried flags, slot conflicts.

## 1. What problem this shard solves

The D2 packet already contains the reconciliation defects as declared, unresolved rows:

| Declaration | Location |
|---|---|
| "09 era names differ from 05/11 E0-E2 tags and 08 E1-E4 local labels; no dates or aliases guessed" | `examples/culture-d2/packet.d2.yml:3339`; `tools/assemble-d2.py:158` |
| "10 material inventory is not unioned into 11 costume-facing routes; silk/down slot conflicts remain" | `examples/culture-d2/packet.d2.yml:3342`; `tools/assemble-d2.py:161` |
| "REPORT, do not merge: 10-materials supplies the pack-ox's hair as cordage … but no down/underfleece record" (CMAT-03) | `packet.d2.yml:3172-3173` |
| "REPORT, do not merge: 10-materials has no silk record; its luxury import of the anchor era is MAT-07 lowland-broadcloth … arriving in its E4 slot = brief E2" (CMAT-08) | `packet.d2.yml:3253-3254` |
| "forbidden in E0 by construction (CMAT-06 excluded_eras, converging with 10-materials' own exclusion in the same slot under the era mapping)" | `packet.d2.yml:1964` |
| "the two luxuries must be reconciled before assembly (OQ-3)" | `packet.d2.yml:2017` |

Counts over those artifacts, 2026-10-17: `grep -n 'maps_to: null' examples/culture-d2/packet.d2.yml` → 2 (`:3172` CMAT-03, `:3253` CMAT-08); `grep -n 'excluded_eras:' examples/culture-d2/packet.d2.yml` → 2 (`:3219` CMAT-06, `:3240` CMAT-07); `grep -c 'excluded_eras' examples/culture-d2/components/11-costumes.yml examples/culture-d2/components/10-materials.yml` → 5 and 19; era label systems in play: 4 — packet tags `E0`–`E3` (`packet.d2.yml:2296-2299`), 09's emic era names with D-coordinates (`:2300-2312`), 08's `E1`–`E4` local labels (`examples/culture-d2/components/08-symbols.yml:23`), 10-materials' `E1`–`E4` (`examples/culture-d2/components/10-materials.yml:65`); 11-costumes claims `E0`×7, `E1`×2, `E2`×1 (`grep '    era: "E' examples/culture-d2/components/11-costumes.yml`).

## 2. Scoped semantics (what the code decides, and why)

1. **One scope = one era label system + one material inventory.** Every decision is local to a declared scope; the code never unions two inventories or two tag sets. Grounding: the packet's own unresolved rows above; `corpus/knowledge/synthesis/era-language-staging.md:13` (event date, stage, composition date, copy date, edition normalization are separate fields); `era-myth-language-costume-matrix.md:19-20` (etic vs emic labels; attestation vs adoption).
2. **A tag is not a name, and a name is not a tag.** A declared tag is in scope; a declared emic name (from `era_records`) resolves to its tag as a *name form* (note), keeping both labels visible; anything else holds as unmapped — never aliased, never dated. Grounding: `era-language-staging.md:108-124` ("type every label"; "keep an emic label beside an editorial label"); the packet's "no dates or aliases guessed".
3. **Identity by translation is not identity.** A material reference resolves by id, then by the inventory's own `material` key; a match only against a display label is held, not promoted. Grounding: `reports/supplement-opencode-1/22-label-representation.md:118-134` (rules 1–5: native bytes govern; label-only records hold); `costume-language-coupling-table.md:39-40` ("a modern curatorial label becomes an attested historical native word" is a reject condition); SKILL.md:186 ("translated display labels do not enter a phonotactic test").
4. **Availability is read from the material's own declaration** (`excluded_eras`, `routes[].eras`): excluded era → reject; no declared route covering the era → reject; no route list declared → nothing falsified. Grounding: `packet.d2.yml:3219`/`:3240` (CMAT-06/07 exclusions), `10-materials.yml:181-187` (MAT-07 excluded `E1`–`E3`, route `E4`); `loanword-material-dating.md:28` (manufacture/import/use are different clocks).
5. **Cross-scope only through an explicit bridge with an `era_map`.** The "E4 slot = brief E2" equivalence is *input*, never inference; a bridge without a mapping for the claimed era holds. Grounding: `packet.d2.yml:3254`; `loanword-material-dating.md:109` ("Intersect bounds only for evidence demonstrated to concern the same event"); `:60` ("Date the sense–referent pairing").
6. **Carried flags stay visible; nothing is merged or dropped.** `maps_to: null` with a declared note → note finding; `maps_to` with no bridge → hold; `maps_to` naming an absent record → hold. Grounding: `packet.d2.yml:3173`, `:3254` ("carried with the flag rather than dropped"); `assemble-d2.py:161`.
7. **Slot conflicts keep both records.** Two records declaring the same `slot` — within one scope or across a declared bridge — are both kept and flagged. Grounding: `packet.d2.yml:2017`, `:3254` (OQ-3: "either keep both luxury imports or re-letter GAR-06"); `reports/round-7/parent-reconciliation.json` (`whole_claim_rule`: scoped dispositions stay distinct from whole-claim confirmation); design spec §3.1 M1/M3 ("match by slot, never by label").
8. **Raw records are preserved; dispositions are additive.** The code mutates no input; findings ride beside the records (same discipline the round-8 F claim requires of raw worker labels: "raw worker labels preserved apart from reconciled dispositions").
9. **Mapping rows carry status and scope.** A bridge `era_map` entry is either a bare tag (confirmed by declaration) or a `{tag, status, scope, row}` row; a `to-verify` row yields a scoped HOLD that cites the row id and is never promoted. Grounding: design spec §2.1 E4/E5; `11-costumes.yml:62-65` (ERX-1..ERX-4 are `(to-verify)`, "slot-level, not label-level").
10. **Conflicting rows are the exit-2 class.** Two rows mapping one source tag to different targets raise `ReconciliationError` (design spec §2.2 `conflict` → exit 2, `D2L-DATA`) — the run stops rather than picking a winner.
11. **Slot identity across a bridge.** When a `maps_to` reference resolves to a target record and both sides declare `slot` values, a mismatch holds: identity is by slot, never by label (design spec §3.1 M1/M3).

## 3. Finding vocabulary

| Code | Severity | Spec verdict | Spec class | Fires when | Grounded at |
|---|---|---|---|---|---|
| `R-ERA-IN-SCOPE` | ok (disposition only) | identity | D2L-ERA | claim names a declared tag | scope tags |
| `R-ERA-NAME-FORM` | note | mapped-confirmed | D2L-ERA | claim names a declared emic era name; resolved to its tag, the `era_records` row cited | `era-language-staging.md:123-124` |
| `R-ERA-UNMAPPED` | hold | unmapped | D2L-ERA | claim names neither a tag nor a declared name of the scope (e.g. 08's `E4` in the brief's `E0`–`E3`) | `packet.d2.yml:3339` |
| `R-ERA-BRIDGE-UNMAPPED` | hold | unmapped | D2L-ERA | a bridge is declared but its `era_map` has no row for the claim's tag | `packet.d2.yml:3254` |
| `R-ERA-MAPPING-UNCONFIRMED` | hold | mapped-unconfirmed | D2L-ERA | the bridge row for the tag is `status: to-verify`; row id cited, never promoted | design spec §2.1 E5; `11-costumes.yml:62-65` |
| `R-MAT-RESOLVED` | ok (disposition only) | available | D2L-MATERIAL | reference resolves in scope and the era is covered | `10-materials.yml:181-187` |
| `R-MAT-UNRESOLVED-REF` | hold | unresolved | D2L-SCOPE | reference resolves in no declared scope | fail-closed; nothing invented |
| `R-MAT-TRANSLATED-MATCH` | hold | unresolved | D2L-SCOPE | only a display label matched | `22-label-representation.md:118-134` |
| `R-MAT-ERA-UNCHECKED` | hold | unresolved | D2L-MATERIAL | identity resolved but the era leg is unmapped / has no confirmed bridge row | fail-closed |
| `R-MAT-ERA-EXCLUDED` | reject | unavailable-by-closure | D2L-MATERIAL | `excluded_eras` or route coverage forbids the claimed (or bridged) era | `packet.d2.yml:1964`, `:3219`; design spec §3.2 M4 |
| `R-MAT-CARRIED-FLAG` | note | unresolved | D2L-MATERIAL | `maps_to: null` with a declared `maps_to_note` (kept in the ledger) | `packet.d2.yml:3172-3173`; design spec §3.1 M2 |
| `R-MAT-BRIDGE-MISSING` | hold | unresolved | D2L-SCOPE | `maps_to` declared but no bridge covers the scope | `packet.d2.yml:3254` |
| `R-MAT-CROSS-SCOPE` | note | available | D2L-MATERIAL | resolved through a declared confirmed bridge; era bridged and covered | `packet.d2.yml:3254` |
| `R-MAT-DANGLING` | hold | unresolved | D2L-SCOPE | `maps_to` names no record in the bridged target | fail-closed |
| `R-MAT-SLOT-CONFLICT` | hold | unresolved | D2L-MATERIAL | two records claim one `slot` (own scope or across a bridge) | `packet.d2.yml:2017`, `:3254` (OQ-3) |
| `R-MAT-SLOT-MISMATCH` | hold | unresolved | D2L-MATERIAL | a bridged `maps_to` target declares a different slot from the source record | design spec §3.1 M1/M3 |

Severity vocabulary follows the lane's gates (`reject` / `hold` / `note`; e.g. `tools/gates/costume-era-consistency-gate.py` header); the verdict and class columns carry the design spec's vocabulary verbatim (`D2L-ERA`, `D2L-MATERIAL`, `D2L-SCOPE` are spec §6 classes; `D2L-DATA` is raised as `ReconciliationError`). Every finding dict carries `verdict` and `class` fields, so D02 needs no second mapping table. Exit-code mapping is D02's call; §6 records the recommendation.

## 4. Implementation for D02 (self-contained; paste into `tools/d2-typed-labels.py`)

```python
"""Scoped era/material reconciliation for D2 typed labels (R8-D05 shard).

One scope = one era label system + one material inventory. Every decision is
local to a declared scope; cross-scope comparisons run only through an
explicitly declared bridge with an era_map. Nothing is aliased, dated, unioned
or rewritten: findings are additive dispositions beside the raw records.

Grounded in examples/culture-d2/packet.d2.yml assembly.unresolved (:3339,
:3342), CMAT-03/CMAT-08 maps_to notes (:3172-3173, :3253-3254), GAR-04/GAR-06
era seams (:1964, :2017); corpus/knowledge/synthesis/era-language-staging.md
§1, §7; loanword-material-dating.md §2, §6; costume-language-coupling-table.md
§2; reports/supplement-opencode-1/22-label-representation.md §2;
reports/round-7/parent-reconciliation.json (scoped dispositions).

Finding codes are R-* (reconciliation), distinct from the parser's E-*/W-*.
Malformed input raises ReconciliationError; the CLI maps it to exit 2.
"""

import json
import re
import unicodedata

_ID_TOKEN = re.compile(r"(?<![A-Za-z0-9-])([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)(?![A-Za-z0-9-])")


def _declared_id(value):
    """The id token a maps_to string declares, or None.

    Packet maps_to values carry a declared id inside prose ("10-materials
    MAT-01 ewe-fleece (same slot: …)"); extraction is token-shape only — the
    lane's id convention (D03's _ID_RE) — never an alias or a guessed target.
    """
    match = _ID_TOKEN.search(value)
    return match.group(1) if match else None


R_ERA_IN_SCOPE = "R-ERA-IN-SCOPE"
R_ERA_NAME_FORM = "R-ERA-NAME-FORM"
R_ERA_UNMAPPED = "R-ERA-UNMAPPED"
R_ERA_BRIDGE_UNMAPPED = "R-ERA-BRIDGE-UNMAPPED"
R_ERA_MAPPING_UNCONFIRMED = "R-ERA-MAPPING-UNCONFIRMED"
R_MAT_RESOLVED = "R-MAT-RESOLVED"
R_MAT_UNRESOLVED = "R-MAT-UNRESOLVED-REF"
R_MAT_TRANSLATED = "R-MAT-TRANSLATED-MATCH"
R_MAT_ERA_UNCHECKED = "R-MAT-ERA-UNCHECKED"
R_MAT_ERA_EXCLUDED = "R-MAT-ERA-EXCLUDED"
R_MAT_CARRIED_FLAG = "R-MAT-CARRIED-FLAG"
R_MAT_BRIDGE_MISSING = "R-MAT-BRIDGE-MISSING"
R_MAT_CROSS_SCOPE = "R-MAT-CROSS-SCOPE"
R_MAT_DANGLING = "R-MAT-DANGLING"
R_MAT_SLOT_CONFLICT = "R-MAT-SLOT-CONFLICT"
R_MAT_SLOT_MISMATCH = "R-MAT-SLOT-MISMATCH"

SEVERITY = {
    R_ERA_IN_SCOPE: "ok", R_ERA_NAME_FORM: "note", R_ERA_UNMAPPED: "hold",
    R_ERA_BRIDGE_UNMAPPED: "hold", R_ERA_MAPPING_UNCONFIRMED: "hold",
    R_MAT_RESOLVED: "ok", R_MAT_UNRESOLVED: "hold", R_MAT_TRANSLATED: "hold",
    R_MAT_ERA_UNCHECKED: "hold", R_MAT_ERA_EXCLUDED: "reject",
    R_MAT_CARRIED_FLAG: "note", R_MAT_BRIDGE_MISSING: "hold",
    R_MAT_CROSS_SCOPE: "note", R_MAT_DANGLING: "hold",
    R_MAT_SLOT_CONFLICT: "hold", R_MAT_SLOT_MISMATCH: "hold",
}

# R8-D01 design-spec §2.2/§3.2 verdicts and §6 finding classes, carried beside
# every code so D02 can emit the contract vocabulary without a second mapping.
VERDICT = {
    R_ERA_IN_SCOPE: "identity", R_ERA_NAME_FORM: "mapped-confirmed",
    R_ERA_UNMAPPED: "unmapped", R_ERA_BRIDGE_UNMAPPED: "unmapped",
    R_ERA_MAPPING_UNCONFIRMED: "mapped-unconfirmed",
    R_MAT_RESOLVED: "available", R_MAT_CROSS_SCOPE: "available",
    R_MAT_ERA_EXCLUDED: "unavailable-by-closure",
    R_MAT_ERA_UNCHECKED: "unresolved", R_MAT_UNRESOLVED: "unresolved",
    R_MAT_TRANSLATED: "unresolved", R_MAT_CARRIED_FLAG: "unresolved",
    R_MAT_BRIDGE_MISSING: "unresolved", R_MAT_DANGLING: "unresolved",
    R_MAT_SLOT_CONFLICT: "unresolved", R_MAT_SLOT_MISMATCH: "unresolved",
}

FINDING_CLASS = {
    R_ERA_IN_SCOPE: "D2L-ERA", R_ERA_NAME_FORM: "D2L-ERA",
    R_ERA_UNMAPPED: "D2L-ERA", R_ERA_BRIDGE_UNMAPPED: "D2L-ERA",
    R_ERA_MAPPING_UNCONFIRMED: "D2L-ERA",
    R_MAT_RESOLVED: "D2L-MATERIAL", R_MAT_CROSS_SCOPE: "D2L-MATERIAL",
    R_MAT_ERA_EXCLUDED: "D2L-MATERIAL", R_MAT_ERA_UNCHECKED: "D2L-MATERIAL",
    R_MAT_CARRIED_FLAG: "D2L-MATERIAL", R_MAT_SLOT_CONFLICT: "D2L-MATERIAL",
    R_MAT_SLOT_MISMATCH: "D2L-MATERIAL",
    R_MAT_UNRESOLVED: "D2L-SCOPE", R_MAT_TRANSLATED: "D2L-SCOPE",
    R_MAT_BRIDGE_MISSING: "D2L-SCOPE", R_MAT_DANGLING: "D2L-SCOPE",
}


class ReconciliationError(ValueError):
    """Malformed input: fail closed (the CLI maps this to exit 2)."""


def _token(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ReconciliationError(f"{field}: expected a non-empty string, got {value!r}")
    return unicodedata.normalize("NFC", value.strip())


def _check_unique_ids(records, what):
    ids = []
    for record in records:
        if not isinstance(record, dict):
            raise ReconciliationError(f"{what}: every record must be a mapping")
        ids.append(_token(record.get("id"), f"{what}[].id"))
    if len(ids) != len(set(ids)):
        raise ReconciliationError(f"{what}: duplicate record ids; refusing silent deduplication")
    return ids


def _finding(code, where, detail, scope):
    return {"code": code, "where": where, "scope": scope,
            "severity": SEVERITY[code], "verdict": VERDICT[code],
            "class": FINDING_CLASS[code], "detail": detail}


def era_scope_from_packet(packet):
    """Packet era scope: tags are packet.eras; names are the declared emic
    names from packet.era_records, kept with their row ids — never guessed
    aliases, and a name-form claim cites the row that declares it."""
    if not isinstance(packet, dict):
        raise ReconciliationError("packet: expected a mapping")
    tags = packet.get("eras")
    if not isinstance(tags, list) or not tags or not all(isinstance(t, str) for t in tags):
        raise ReconciliationError("packet.eras: expected a non-empty list of era tags")
    names = {}
    for record in packet.get("era_records") or []:
        if not isinstance(record, dict):
            raise ReconciliationError("packet.era_records[]: expected mappings")
        tag, name = record.get("tag"), record.get("name")
        if not (isinstance(tag, str) and isinstance(name, str)):
            continue
        if tag not in tags:
            raise ReconciliationError(f"packet.era_records: {name!r} names undeclared tag {tag!r}")
        row = {"tag": tag, "row": record.get("id") if isinstance(record.get("id"), str) else None}
        if names.get(name) not in (None, row):
            raise ReconciliationError(f"packet.era_records: name {name!r} maps to two tags")
        names[name] = row
    return {"id": "packet-eras", "axis": "era", "tags": list(tags), "names": names}


def material_scope_from_packet(packet):
    """Packet material scope: the costume-facing inventory as delivered."""
    if not isinstance(packet, dict):
        raise ReconciliationError("packet: expected a mapping")
    records = packet.get("materials")
    if not isinstance(records, list) or not records:
        raise ReconciliationError("packet.materials: expected a non-empty record list")
    _check_unique_ids(records, "packet.materials")
    return {"id": "packet-materials", "axis": "material", "records": records}


def claims_from_packet(packet):
    """Costume records -> reconciliation claims {id, era, material_ref}."""
    claims = []
    for record in packet.get("costumes") or []:
        if not isinstance(record, dict):
            raise ReconciliationError("packet.costumes[]: expected mappings")
        rid = _token(record.get("id"), "packet.costumes[].id")
        era, ref = record.get("era"), record.get("material")
        if not isinstance(era, str) or not era.strip():
            raise ReconciliationError(f"{rid}: costume carries no era claim")
        if not isinstance(ref, str) or not ref.strip():
            raise ReconciliationError(f"{rid}: costume carries no material reference")
        claims.append({"id": rid, "era": era, "material_ref": ref})
    if not claims:
        raise ReconciliationError("packet.costumes: no costume claims to reconcile")
    _check_unique_ids(claims, "claims")
    return claims


def _prepare_scope(scope):
    if not isinstance(scope, dict):
        raise ReconciliationError("scope: expected a mapping")
    sid = _token(scope.get("id"), "scope.id")
    axis = scope.get("axis")
    if axis == "era":
        tags = scope.get("tags")
        if not isinstance(tags, list) or not tags or not all(isinstance(t, str) for t in tags):
            raise ReconciliationError(f"{sid}: era scope needs a non-empty tag list")
        names = scope.get("names") or {}
        if not isinstance(names, dict):
            raise ReconciliationError(f"{sid}: era scope names must map name -> tag or {{tag, row}}")
        normalized = {}
        for key, value in names.items():
            if not isinstance(key, str):
                raise ReconciliationError(f"{sid}: era scope names must map name -> tag or {{tag, row}}")
            if isinstance(value, str):
                normalized[key] = {"tag": value, "row": None}
            elif isinstance(value, dict) and isinstance(value.get("tag"), str):
                normalized[key] = {"tag": value["tag"], "row": value.get("row")}
            else:
                raise ReconciliationError(f"{sid}: era name {key!r} must map to a tag or a {{tag, row}} row")
        return {"id": sid, "axis": "era", "tags": list(tags), "names": normalized}
    if axis == "material":
        records = scope.get("records")
        if not isinstance(records, list) or not records:
            raise ReconciliationError(f"{sid}: material scope needs a non-empty record list")
        _check_unique_ids(records, sid)
        return {"id": sid, "axis": "material", "records": records}
    raise ReconciliationError(f"{sid}: scope axis must be 'era' or 'material'")


def _normalize_era_row(value, where):
    """One declared mapping row: a bare tag (confirmed by declaration) or a
    {tag, status, scope, row} record (design spec §2.1 E4/E5)."""
    if isinstance(value, str):
        return {"tag": value, "status": "confirmed", "scope": None, "row": None}
    if isinstance(value, dict) and isinstance(value.get("tag"), str):
        status = value.get("status", "confirmed")
        if status not in ("confirmed", "to-verify"):
            raise ReconciliationError(f"{where}: mapping status must be confirmed | to-verify")
        scope = value.get("scope")
        if scope is not None and scope not in ("slot", "label"):
            raise ReconciliationError(f"{where}: mapping scope must be slot | label")
        return {"tag": value["tag"], "status": status, "scope": scope, "row": value.get("row")}
    raise ReconciliationError(f"{where}: era mapping must be a tag or a {{tag, status, scope, row}} row")


def _prepare_bridges(bridges, material_scope):
    """Bridges whose source is this material scope; each carries its own
    target scope, an explicit era_map of declared rows, and an optional target
    era scope. Two rows mapping one source tag to different targets raise the
    spec's conflict class (exit 2, D2L-DATA)."""
    prepared = []
    seen = {}
    for bridge in bridges:
        if not isinstance(bridge, dict):
            raise ReconciliationError("bridges[]: expected mappings")
        source = _token(bridge.get("source_scope"), "bridge.source_scope")
        if source != material_scope["id"]:
            continue
        target = _prepare_scope(bridge.get("target_scope"))
        if target["axis"] != "material":
            raise ReconciliationError(f"bridge {source}: target scope must be a material scope")
        era_map = bridge.get("era_map")
        if not isinstance(era_map, dict) or not all(isinstance(k, str) for k in era_map):
            raise ReconciliationError(f"bridge {source} -> {target['id']}: era_map must map tags to rows")
        rows = {}
        for source_tag, value in era_map.items():
            row = _normalize_era_row(value, f"bridge {source} -> {target['id']} era_map[{source_tag!r}]")
            key = (source, source_tag)
            if key in seen and seen[key] != row["tag"]:
                raise ReconciliationError(
                    f"era mapping conflict for {source_tag!r} in {source}: {seen[key]!r} vs {row['tag']!r}; "
                    "exit-2 class D2L-DATA (design spec §2.2 conflict)")
            seen[key] = row["tag"]
            rows[source_tag] = row
        target_era = bridge.get("target_era_scope")
        if target_era is not None:
            target_era = _prepare_scope(target_era)
            if target_era["axis"] != "era":
                raise ReconciliationError(f"bridge {source}: target_era_scope must be an era scope")
        prepared.append({"source_scope": source, "source_records": material_scope["records"],
                         "target": target, "target_era": target_era, "era_map": rows})
    return prepared


def resolve_era(value, era_scope):
    """One era label inside ONE declared system.

    Returns (code, tag, detail): a declared tag is in scope; a declared emic
    name resolves to its tag as a name-form note; anything else is unmapped
    (hold) — never aliased, never dated (packet.d2.yml:3339).
    """
    v = _token(value, "era")
    if v in era_scope["tags"]:
        return R_ERA_IN_SCOPE, v, f"declared tag {v}"
    entry = era_scope["names"].get(v)
    if entry is not None:
        row = entry.get("row") or "<unnamed row>"
        return R_ERA_NAME_FORM, entry["tag"], (f"emic name {v!r} resolves to declared tag {entry['tag']} "
                                               f"(era_records {row}); name form, not a tag")
    return R_ERA_UNMAPPED, None, (f"{v!r} is not a tag or declared name of scope {era_scope['id']} "
                                  f"(tags={era_scope['tags']}); kept as declared, never aliased")


def _match_material(ref, scope):
    """(record, how) over ONE scope; how in {id, key, translated, missing}.

    `key` = the inventory's own material name; `translated` = a display label
    matched instead — identity by translation is not identity
    (22-label-representation.md §2) and is held, never promoted.
    """
    if isinstance(ref, dict):
        rid, name = ref.get("id"), ref.get("name")
        if rid is None and name is None:
            raise ReconciliationError("material_ref: a mapping needs 'id' or 'name'")
    elif isinstance(ref, str):
        rid, name = None, ref
    else:
        raise ReconciliationError(f"material_ref: expected a string or mapping, got {ref!r}")
    if rid is not None:
        rid = _token(rid, "material_ref.id")
        for record in scope["records"]:
            if record["id"] == rid:
                return record, "id"
    if name is not None:
        name = _token(name, "material_ref")
        for record in scope["records"]:
            key = record.get("material")
            if isinstance(key, str) and _token(key, record["id"]) == name:
                return record, "key"
        for record in scope["records"]:
            label = record.get("display_label")
            if isinstance(label, str) and _token(label, record["id"]) == name:
                return record, "translated"
    return None, "missing"


def _era_allowed(material, era):
    """(allowed, why) from the material's own exclusions and declared routes."""
    excluded = material.get("excluded_eras") or []
    if not isinstance(excluded, list) or not all(isinstance(e, str) for e in excluded):
        raise ReconciliationError(f"{material['id']}: excluded_eras must be a list of era tags")
    if era in excluded:
        return False, f"excluded_eras declares {era}"
    routes = material.get("routes")
    if routes:
        if not isinstance(routes, list):
            raise ReconciliationError(f"{material['id']}: routes must be a list")
        for route in routes:
            if not isinstance(route, dict):
                raise ReconciliationError(f"{material['id']}: routes must be mappings")
            eras = route.get("eras")
            if eras is None:
                return True, f"route {route.get('id', route.get('name', '?'))} declares no era bound"
            if not isinstance(eras, list):
                raise ReconciliationError(f"{material['id']}: route eras must be a list or absent")
            if era in eras:
                return True, f"route {route.get('id', route.get('name', '?'))} covers {era}"
        return False, f"no declared route covers {era}"
    return True, "no route list declared"


def _resolve_ref(ref, material_scope, bridges):
    """(record, how, scope_id, bridge): own scope first, then declared bridges."""
    material, how = _match_material(ref, material_scope)
    if material is not None:
        return material, how, material_scope["id"], None
    for bridge in bridges:
        material, how = _match_material(ref, bridge["target"])
        if material is not None:
            return material, how, bridge["target"]["id"], bridge
    return None, "missing", material_scope["id"], None


def reconcile_claim(claim, era_scope, material_scope, bridges=()):
    """One claim -> disposition + non-clean findings. Pure; no I/O.

    claim: {"id", "era", "material_ref"} (claims_from_packet builds these).
    """
    if not isinstance(claim, dict):
        raise ReconciliationError("claims[]: expected mappings")
    rid = _token(claim.get("id"), "claims[].id")
    findings = []

    era_code, era_tag, era_detail = resolve_era(claim.get("era"), era_scope)
    if era_code != R_ERA_IN_SCOPE:
        findings.append(_finding(era_code, rid, era_detail, era_scope["id"]))

    material, how, scope_id, bridge = _resolve_ref(claim.get("material_ref"), material_scope, bridges)
    resolved = material["id"] if material is not None else None
    if material is None:
        material_code = R_MAT_UNRESOLVED
        findings.append(_finding(material_code, rid,
                                 f"material_ref {claim.get('material_ref')!r} resolves in no declared scope "
                                 f"({material_scope['id']} or a declared bridge); a name that matches nothing is "
                                 "not invented into the inventory", material_scope["id"]))
    elif how == "translated":
        material_code = R_MAT_TRANSLATED
        findings.append(_finding(material_code, rid,
                                 f"only a display label matched {material['id']}; identity by translation is not "
                                 "identity (22-label-representation.md §2)", scope_id))
    else:
        check_era = era_tag
        if bridge is not None:
            row = bridge["era_map"].get(era_tag) if era_tag else None
            if row is None:
                check_era = None
                findings.append(_finding(R_ERA_BRIDGE_UNMAPPED, rid,
                                         f"bridge {bridge['source_scope']} -> {scope_id} declares no mapping for "
                                         f"{era_tag!r}; era compatibility not evaluated", scope_id))
            elif row["status"] != "confirmed":
                check_era = None
                findings.append(_finding(R_ERA_MAPPING_UNCONFIRMED, rid,
                                         f"bridge mapping {row['row'] or '<unnamed row>'} for {era_tag!r} is "
                                         f"to-verify (scope {row['scope'] or 'unstated'}); scoped HOLD, the row is "
                                         "never promoted (design spec §2.1 E4/E5)", scope_id))
            else:
                check_era = row["tag"]
                if bridge["target_era"] is not None and row["tag"] not in bridge["target_era"]["tags"]:
                    findings.append(_finding(R_ERA_UNMAPPED, rid,
                                             f"bridged era {row['tag']!r} is not declared in {scope_id} tags "
                                             f"{bridge['target_era']['tags']}", bridge["target_era"]["id"]))
                    check_era = None
        if check_era is None:
            material_code = R_MAT_ERA_UNCHECKED
            findings.append(_finding(material_code, rid,
                                     f"identity {material['id']} resolved, but the era leg has no declared "
                                     "mapping; compatibility held, not assumed", scope_id))
        else:
            allowed, why = _era_allowed(material, check_era)
            if not allowed:
                material_code = R_MAT_ERA_EXCLUDED
                bridged = f" (bridged {era_tag} -> {check_era})" if bridge is not None else ""
                findings.append(_finding(material_code, rid,
                                         f"{material['id']} is not available in {check_era}: {why}{bridged}",
                                         scope_id))
            elif bridge is not None:
                material_code = R_MAT_CROSS_SCOPE
                findings.append(_finding(material_code, rid,
                                         f"resolved {material['id']} across bridge {bridge['source_scope']} -> "
                                         f"{scope_id}; era {era_tag} -> {check_era}; carried as a declared "
                                         "cross-scope reference, not merged", scope_id))
            else:
                material_code = R_MAT_RESOLVED
    return {"record": rid,
            "era": {"code": era_code, "tag": era_tag},
            "material": {"code": material_code, "resolved": resolved},
            "findings": findings}


def _material_record_flags(scope, bridges):
    """Record-side flags: carried notes, missing bridges, dangling maps_to."""
    findings = []
    bridge_by_source = {b["source_scope"]: b for b in bridges}
    for material in scope["records"]:
        maps_to = material.get("maps_to")
        if maps_to is None:
            if material.get("maps_to_note"):
                findings.append(_finding(R_MAT_CARRIED_FLAG, material["id"],
                                         "carried with its declared flag; never merged or dropped",
                                         scope["id"]))
        elif isinstance(maps_to, str):
            key = _declared_id(maps_to) or maps_to
            bridge = bridge_by_source.get(scope["id"])
            if bridge is None:
                findings.append(_finding(R_MAT_BRIDGE_MISSING, material["id"],
                                         f"maps_to {maps_to!r} declares {key!r} with no bridge for scope "
                                         f"{scope['id']}; carried, not merged", scope["id"]))
            else:
                target_record = next((r for r in bridge["target"]["records"] if r["id"] == key), None)
                if target_record is None:
                    findings.append(_finding(R_MAT_DANGLING, material["id"],
                                             f"maps_to {maps_to!r} declares {key!r}, which names no record in "
                                             f"{bridge['target']['id']}", scope["id"]))
                else:
                    source_slot, target_slot = material.get("slot"), target_record.get("slot")
                    if (isinstance(source_slot, str) and isinstance(target_slot, str)
                            and source_slot != target_slot):
                        findings.append(_finding(R_MAT_SLOT_MISMATCH, material["id"],
                                                 f"maps_to {key!r} carries slot {source_slot!r} but the target "
                                                 f"declares {target_slot!r}; identity is by slot, never by label "
                                                 "(design spec §3.1 M1/M3)", scope["id"]))
        else:
            raise ReconciliationError(f"{material['id']}: maps_to must be a string or null")
    return findings


def _slot_conflicts(scopes, bridges):
    """Same-slot claims are kept as declared and flagged, within and across
    declared bridges (OQ-3: keep both luxuries or re-letter the record)."""
    findings = []
    seen = set()

    def add(record, scope_id, slot, ids):
        key = (record["id"], scope_id, slot)
        if key in seen:
            return
        seen.add(key)
        findings.append(_finding(R_MAT_SLOT_CONFLICT, record["id"],
                                 f"slot {slot!r} is claimed by {ids}; both records are kept as declared "
                                 "(OQ-3), never merged", scope_id))

    def grouped(scope):
        out = {}
        for record in scope["records"]:
            slot = record.get("slot")
            if slot is None:
                continue
            out.setdefault(_token(slot, f"{record['id']}.slot"), []).append(record)
        return out

    for scope in scopes:
        for slot, records in grouped(scope).items():
            if len(records) > 1:
                ids = [r["id"] for r in records]
                for record in records:
                    add(record, scope["id"], slot, ids)
    for bridge in bridges:
        target = bridge["target"]
        source_slots = grouped({"id": bridge["source_scope"], "records": bridge["source_records"]})
        target_slots = grouped(target)
        for slot in sorted(set(source_slots) & set(target_slots)):
            source_records, target_records = source_slots[slot], target_slots[slot]
            ids = [r["id"] for r in source_records] + [r["id"] for r in target_records]
            for record in source_records:
                add(record, bridge["source_scope"], slot, ids)
            for record in target_records:
                add(record, target["id"], slot, ids)
    return findings


def reconcile_claims(claims, era_scope, material_scope, external_scopes=(), bridges=()):
    """Core driver over declared scopes; returns a JSON-serializable result."""
    era = _prepare_scope(era_scope)
    if era["axis"] != "era":
        raise ReconciliationError(f"{era['id']}: expected an era scope")
    mat = _prepare_scope(material_scope)
    if mat["axis"] != "material":
        raise ReconciliationError(f"{mat['id']}: expected a material scope")
    externals = [_prepare_scope(s) for s in external_scopes]
    for scope in externals:
        if scope["axis"] != "material":
            raise ReconciliationError(f"{scope['id']}: external scopes must be material scopes")
    brs = _prepare_bridges(bridges, mat)
    _check_unique_ids(claims, "claims")

    results = [reconcile_claim(claim, era, mat, brs) for claim in claims]
    findings = [f for r in results for f in r["findings"]]
    scanned = set()
    for scope in [mat] + externals + [b["target"] for b in brs]:
        if scope["id"] in scanned:
            continue
        scanned.add(scope["id"])
        findings += _material_record_flags(scope, brs)
    findings += _slot_conflicts([mat] + [b["target"] for b in brs] + externals, brs)
    findings.sort(key=lambda f: (f["where"], f["code"], f["scope"], f["detail"]))
    by_severity = {}
    for f in findings:
        by_severity[f["severity"]] = by_severity.get(f["severity"], 0) + 1
    return {
        "scopes": {"era": era["id"], "material": mat["id"],
                   "bridges": [f"{b['source_scope']}->{b['target']['id']}" for b in brs]},
        "records": results,
        "findings": findings,
        "summary": {"claims": len(claims), "findings": len(findings),
                    "by_severity": dict(sorted(by_severity.items())),
                    "by_code": {code: sum(1 for f in findings if f["code"] == code)
                                for code in sorted({f["code"] for f in findings})}},
    }


def reconcile_scoped(packet, external_scopes=(), bridges=(), claims=None):
    """Packet entry: derive scopes/claims from the packet, then reconcile.

    external_scopes/bridges are declared inputs (e.g. the 10-materials E1-E4
    inventory and the E4 = brief-E2 mapping). This function never reads sibling
    component files and never infers an alias or a date.
    """
    era_scope = era_scope_from_packet(packet)
    material_scope = material_scope_from_packet(packet)
    if claims is None:
        claims = claims_from_packet(packet)
    return reconcile_claims(claims, era_scope, material_scope, external_scopes, bridges)


def _selftest_era_material():
    """Positive + malformed controls. Returns [(label, ok, detail), ...]."""
    checks = []

    def check(label, condition, detail=""):
        checks.append((label, bool(condition), detail))

    era_scope = {"id": "brief-E0-E3", "axis": "era", "tags": ["E0", "E1", "E2", "E3"],
                 "names": {"Open Grazing": "E0"}}
    material_scope = {"id": "costumes-CMAT", "axis": "material", "records": [
        {"id": "CMAT-01", "material": "wool", "slot": "state-fiber",
         "display_label": "felt display name",
         "routes": [{"id": "RT-c01", "kind": "local", "stage": "fiber", "eras": ["E0", "E1", "E2"]}]},
        {"id": "CMAT-06", "material": "lowland plant-thread cloth", "slot": "imported-cloth",
         "excluded_eras": ["E0"],
         "routes": [{"id": "RT-c06", "kind": "import", "stage": "cloth", "eras": ["E1", "E2"]}]},
        {"id": "CMAT-08", "material": "silk", "slot": "anchor-era-luxury", "maps_to": None,
         "maps_to_note": "REPORT, do not merge: 10-materials has no silk record (packet.d2.yml:3254)",
         "routes": [{"id": "RT-c08", "kind": "import", "stage": "cloth", "eras": ["E2"]}]},
        {"id": "CMAT-09", "material": "hearth-dark",
         "maps_to": "10-materials MAT-10 hearth-dark (same slot and chemistry)",
         "routes": [{"id": "RT-c09", "kind": "local", "stage": "dye", "eras": ["E1", "E2"]}]},
        {"id": "CMAT-10", "material": "bog-iron (fixture only)",
         "maps_to": "10-materials MAT-99 nowhere (fixture-only dangling target)",
         "routes": [{"id": "RT-c10", "kind": "local", "stage": "trim", "eras": ["E2"]}]},
        {"id": "CMAT-11", "material": "smoke-cured hide (fixture only)", "slot": "wind-facing-outer",
         "maps_to": "10-materials MAT-10 hearth-dark (fixture: deliberate slot mismatch)",
         "routes": [{"id": "RT-c11", "kind": "local", "stage": "garment", "eras": ["E2"]}]},
    ]}
    target = {"id": "materials-MAT", "axis": "material", "records": [
        {"id": "MAT-07", "material": "lowland-broadcloth", "slot": "anchor-era-luxury",
         "excluded_eras": ["E1", "E2", "E3"],
         "routes": [{"id": "RT-m07", "kind": "import", "stage": "cloth", "eras": ["E4"]}]},
        {"id": "MAT-10", "material": "hearth-dark", "slot": "smoke-dark",
         "routes": [{"id": "RT-m10", "kind": "local", "stage": "dye", "eras": ["E1", "E2", "E3", "E4"]}]},
    ]}
    bridge = {"source_scope": "costumes-CMAT", "target_scope": target, "era_map": {"E2": "E4"},
              "target_era_scope": {"id": "materials-eras", "axis": "era",
                                   "tags": ["E1", "E2", "E3", "E4"], "names": {}}}
    to_verify_bridge = {"source_scope": "costumes-CMAT", "target_scope": target,
                        "era_map": {"E2": {"tag": "E4", "status": "to-verify", "scope": "slot", "row": "ERX-2"}}}
    base = [{"id": "GAR-01", "era": "E0", "material_ref": "wool"},
            {"id": "GAR-04", "era": "E1", "material_ref": "lowland plant-thread cloth"}]

    def run(claims, bridges=()):
        return reconcile_claims(claims, era_scope, material_scope, bridges=list(bridges))

    def codes(result, rid):
        for record in result["records"]:
            if record["record"] == rid:
                return sorted(f["code"] for f in record["findings"])
        return None

    result = run(base, [bridge])
    check("P1 own-scope claim is clean", codes(result, "GAR-01") == [], str(codes(result, "GAR-01")))
    check("P2 in-scope route claim is clean", codes(result, "GAR-04") == [], str(codes(result, "GAR-04")))
    check("P2b carried flag fires once for CMAT-08",
          [f["where"] for f in result["findings"] if f["code"] == R_MAT_CARRIED_FLAG] == ["CMAT-08"])
    check("P2c cross-scope slot conflict flags both records",
          sorted(f["where"] for f in result["findings"] if f["code"] == R_MAT_SLOT_CONFLICT)
          == ["CMAT-08", "MAT-07"])

    excluded = run([{"id": "GAR-04-E0", "era": "E0", "material_ref": "lowland plant-thread cloth"}])
    check("P3 excluded era rejects", codes(excluded, "GAR-04-E0") == [R_MAT_ERA_EXCLUDED],
          str(codes(excluded, "GAR-04-E0")))

    foreign = run([{"id": "GAR-SY", "era": "E4", "material_ref": "wool"}])
    check("P4 foreign era label system holds",
          codes(foreign, "GAR-SY") == [R_ERA_UNMAPPED, R_MAT_ERA_UNCHECKED],
          str(codes(foreign, "GAR-SY")))

    name_form = run([{"id": "GAR-NM", "era": "Open Grazing", "material_ref": "wool"}])
    check("P5 declared emic name resolves as a name form",
          codes(name_form, "GAR-NM") == [R_ERA_NAME_FORM], str(codes(name_form, "GAR-NM")))

    missing = run([{"id": "GAR-MX", "era": "E0", "material_ref": "linen"}])
    check("P6 unresolvable reference holds", codes(missing, "GAR-MX") == [R_MAT_UNRESOLVED],
          str(codes(missing, "GAR-MX")))

    translated = run([{"id": "GAR-TR", "era": "E0", "material_ref": "felt display name"}])
    check("P7 translated-label-only match holds",
          codes(translated, "GAR-TR") == [R_MAT_TRANSLATED], str(codes(translated, "GAR-TR")))

    cross = run([{"id": "GAR-XS", "era": "E2", "material_ref": "lowland-broadcloth"}], [bridge])
    check("P8 bridged cross-scope reference notes",
          codes(cross, "GAR-XS") == [R_MAT_CROSS_SCOPE], str(codes(cross, "GAR-XS")))

    no_bridge = run([{"id": "GAR-XS", "era": "E2", "material_ref": "lowland-broadcloth"}])
    check("P9 without the bridge the same reference holds",
          codes(no_bridge, "GAR-XS") == [R_MAT_UNRESOLVED], str(codes(no_bridge, "GAR-XS")))

    empty_map = run([{"id": "GAR-XS", "era": "E2", "material_ref": "lowland-broadcloth"}],
                    [{"source_scope": "costumes-CMAT", "target_scope": target, "era_map": {}}])
    check("P10 undeclared bridge mapping holds",
          codes(empty_map, "GAR-XS") == [R_ERA_BRIDGE_UNMAPPED, R_MAT_ERA_UNCHECKED],
          str(codes(empty_map, "GAR-XS")))

    once, twice = run(base, [bridge]), run(base, [bridge])
    check("P11 deterministic output",
          json.dumps(once, sort_keys=True, ensure_ascii=False)
          == json.dumps(twice, sort_keys=True, ensure_ascii=False))

    def raises(fragment, fn):
        try:
            fn()
        except ReconciliationError as exc:
            return fragment in str(exc)
        except Exception:
            return False
        return False

    check("N1 duplicate claim ids rejected",
          raises("duplicate record ids", lambda: run(base + [dict(base[0])])))
    check("N2 non-string era rejected",
          raises("expected a non-empty string",
                 lambda: run([{"id": "X", "era": 4, "material_ref": "wool"}])))
    check("N3 bad reference type rejected",
          raises("expected a string or mapping",
                 lambda: run([{"id": "X", "era": "E0", "material_ref": 4}])))
    check("N4 tagless era scope rejected",
          raises("non-empty tag list",
                 lambda: reconcile_claims(base, {"id": "bad", "axis": "era", "tags": []}, material_scope)))
    check("N5 era scope as bridge target rejected",
          raises("material scope",
                 lambda: run(base, [{"source_scope": "costumes-CMAT", "target_scope": era_scope,
                                     "era_map": {}}])))

    packet = {
        "eras": ["E0", "E1", "E2"],
        "era_records": [{"id": "ER-01", "tag": "E0", "name": "Open Grazing"}],
        "materials": [{"id": "CMAT-06", "material": "lowland plant-thread cloth",
                       "excluded_eras": ["E0"],
                       "routes": [{"id": "RT-c06", "kind": "import", "stage": "cloth",
                                   "eras": ["E1", "E2"]}]}],
        "costumes": [{"id": "GAR-04", "era": "E0", "material": "lowland plant-thread cloth"},
                     {"id": "GAR-05", "era": "E4", "material": "lowland plant-thread cloth"}],
    }
    before = json.dumps(packet, sort_keys=True)
    packet_result = reconcile_scoped(packet)
    packet_codes = {r["record"]: sorted(f["code"] for f in r["findings"]) for r in packet_result["records"]}
    check("P12 packet entry reproduces the GAR-04 E0 exclusion",
          packet_codes["GAR-04"] == [R_MAT_ERA_EXCLUDED], str(packet_codes["GAR-04"]))
    check("P13 packet entry holds the foreign E4 label system",
          packet_codes["GAR-05"] == [R_ERA_UNMAPPED, R_MAT_ERA_UNCHECKED], str(packet_codes["GAR-05"]))
    check("P14 packet era scope carries the emic name index with its row id",
          packet_result["scopes"]["era"] == "packet-eras"
          and era_scope_from_packet(packet)["names"] == {"Open Grazing": {"tag": "E0", "row": "ER-01"}})
    check("P15 input packet untouched", json.dumps(packet, sort_keys=True) == before)

    bridged_flags = run(base, [bridge])["findings"]
    bridged_missing = [f["where"] for f in bridged_flags if f["code"] == R_MAT_BRIDGE_MISSING]
    unbridged_missing = [f["where"] for f in run(base)["findings"] if f["code"] == R_MAT_BRIDGE_MISSING]
    check("P16 declared prose maps_to resolves under a bridge (and holds without one)",
          "CMAT-09" not in bridged_missing and "CMAT-09" in unbridged_missing,
          f"bridged={bridged_missing} unbridged={unbridged_missing}")
    check("P17 prose maps_to naming an absent target dangles",
          [f["where"] for f in bridged_flags if f["code"] == R_MAT_DANGLING] == ["CMAT-10"],
          str([f["where"] for f in bridged_flags if f["code"] == R_MAT_DANGLING]))
    check("N6 non-string maps_to rejected",
          raises("maps_to must be a string or null",
                 lambda: run(base, [{"source_scope": "costumes-CMAT", "era_map": {},
                                     "target_scope": {"id": "t", "axis": "material",
                                                      "records": [{"id": "MAT-10", "material": "hearth-dark",
                                                                   "maps_to": 7}]}}])))

    unconfirmed = run([{"id": "GAR-TV", "era": "E2", "material_ref": "lowland-broadcloth"}],
                      [to_verify_bridge])
    check("P18 to-verify mapping row holds and cites its row id",
          codes(unconfirmed, "GAR-TV") == [R_ERA_MAPPING_UNCONFIRMED, R_MAT_ERA_UNCHECKED]
          and any("ERX-2" in f["detail"] for f in unconfirmed["records"][0]["findings"]),
          str(codes(unconfirmed, "GAR-TV")))
    check("P19 two rows mapping one tag differently raise the conflict class",
          raises("mapping conflict",
                 lambda: run(base, [bridge, {"source_scope": "costumes-CMAT", "target_scope": target,
                                             "era_map": {"E2": "E1"}}])))
    check("P20 bridged slot mismatch holds",
          [f["where"] for f in bridged_flags if f["code"] == R_MAT_SLOT_MISMATCH] == ["CMAT-11"],
          str([f["where"] for f in bridged_flags if f["code"] == R_MAT_SLOT_MISMATCH]))

    verdict_codes = {(f["code"], f["verdict"], f["class"])
                     for f in excluded["records"][0]["findings"] + foreign["records"][0]["findings"]}
    check("P21 findings carry the spec verdict and class vocabulary",
          (R_MAT_ERA_EXCLUDED, "unavailable-by-closure", "D2L-MATERIAL") in verdict_codes
          and (R_ERA_UNMAPPED, "unmapped", "D2L-ERA") in verdict_codes, str(sorted(verdict_codes)))
    return checks


if __name__ == "__main__":
    results = _selftest_era_material()
    for label, ok, detail in results:
        print(("PASS" if ok else "FAIL"), label, ("— " + detail) if detail else "")
    failed = [label for label, ok, _ in results if not ok]
    print(f"{len(results) - len(failed)}/{len(results)} controls pass")
    raise SystemExit(1 if failed else 0)
```

## 5. Execution receipt (the block above was run, not just written)

Extracted and executed on 2026-10-17 from this file (no file written outside the repo; the block is piped to `python3 -` as `__main__`):

```text
awk '/^```python$/{f=1;next} /^```$/{f=0} f' reports/round-8/depth/shard-era-material.md | python3 -
```

Observed output (exit 0), verbatim:

```text
PASS P1 own-scope claim is clean — []
PASS P2 in-scope route claim is clean — []
PASS P2b carried flag fires once for CMAT-08 
PASS P2c cross-scope slot conflict flags both records 
PASS P3 excluded era rejects — ['R-MAT-ERA-EXCLUDED']
PASS P4 foreign era label system holds — ['R-ERA-UNMAPPED', 'R-MAT-ERA-UNCHECKED']
PASS P5 declared emic name resolves as a name form — ['R-ERA-NAME-FORM']
PASS P6 unresolvable reference holds — ['R-MAT-UNRESOLVED-REF']
PASS P7 translated-label-only match holds — ['R-MAT-TRANSLATED-MATCH']
PASS P8 bridged cross-scope reference notes — ['R-MAT-CROSS-SCOPE']
PASS P9 without the bridge the same reference holds — ['R-MAT-UNRESOLVED-REF']
PASS P10 undeclared bridge mapping holds — ['R-ERA-BRIDGE-UNMAPPED', 'R-MAT-ERA-UNCHECKED']
PASS P11 deterministic output 
PASS N1 duplicate claim ids rejected 
PASS N2 non-string era rejected 
PASS N3 bad reference type rejected 
PASS N4 tagless era scope rejected 
PASS N5 era scope as bridge target rejected 
PASS P12 packet entry reproduces the GAR-04 E0 exclusion — ['R-MAT-ERA-EXCLUDED']
PASS P13 packet entry holds the foreign E4 label system — ['R-ERA-UNMAPPED', 'R-MAT-ERA-UNCHECKED']
PASS P14 packet era scope carries the emic name index with its row id 
PASS P15 input packet untouched 
PASS P16 declared prose maps_to resolves under a bridge (and holds without one) — bridged=[] unbridged=['CMAT-09', 'CMAT-10', 'CMAT-11']
PASS P17 prose maps_to naming an absent target dangles — ['CMAT-10']
PASS N6 non-string maps_to rejected 
PASS P18 to-verify mapping row holds and cites its row id — ['R-ERA-MAPPING-UNCONFIRMED', 'R-MAT-ERA-UNCHECKED']
PASS P19 two rows mapping one tag differently raise the conflict class 
PASS P20 bridged slot mismatch holds — ['CMAT-11']
PASS P21 findings carry the spec verdict and class vocabulary — [('R-ERA-UNMAPPED', 'unmapped', 'D2L-ERA'), ('R-MAT-ERA-EXCLUDED', 'unavailable-by-closure', 'D2L-MATERIAL'), ('R-MAT-ERA-UNCHECKED', 'unresolved', 'D2L-MATERIAL')]
29/29 controls pass
```

(Lines with no detail argument end in a single space, as printed; reproduced here byte-faithfully inside the fence.)

Determinism double-check (two invocations, stdout hashed and compared):

```text
awk '/^```python$/{f=1;next} /^```$/{f=0} f' reports/round-8/depth/shard-era-material.md | python3 - | sha256sum   (run twice)
```

Observed, 2026-10-17: run 1 and run 2 both `f4fd8300f523e71419d744d957e27fed8a97b830b2133d52858cb9eb0a47cdca  -` → identical. Evidence files read for this shard, with digests at read time (`sha256sum` prefix): `examples/culture-d2/packet.d2.yml` `8da90b0788f86fd1…`, `tools/assemble-d2.py` `8ea6bdde9514ee96…`, `SKILL.md` `ca940f4d87295260…`, `reports/supplement-opencode-1/22-label-representation.md` `5493b3f7a4c8e1b0…`.

Real-packet run (both variants; writes nothing), verbatim:

```text
python3 - <<'PY'
import re, pathlib, runpy, json
root = pathlib.Path('.').resolve()
ns = {}
src = re.findall(r'```python\n(.*?)```', (root/'reports/round-8/depth/shard-era-material.md').read_text(encoding='utf-8'), re.S)
exec(compile('\n'.join(src).replace('if __name__ == "__main__":', 'if False:'), 'd05.py', 'exec'), ns)
gate = runpy.run_path(str(root/'tools/gates/costume-era-consistency-gate.py'))
packet = gate['parse_packet']((root/'examples/culture-d2/packet.d2.yml').read_text(encoding='utf-8'))
print(json.dumps(ns['reconcile_scoped'](packet)['summary'], sort_keys=True))
comp = gate['parse_packet']((root/'examples/culture-d2/components/10-materials.yml').read_text(encoding='utf-8'))
target = {"id": "10-materials", "axis": "material", "records": comp['materials']}
bridge = {"source_scope": "packet-materials", "target_scope": target, "era_map": {}}
print(json.dumps(ns['reconcile_scoped'](packet, external_scopes=[target], bridges=[bridge])['summary'], sort_keys=True))
PY
```

Observed:

```text
{"by_code": {"R-MAT-BRIDGE-MISSING": 7, "R-MAT-CARRIED-FLAG": 2}, "by_severity": {"hold": 7, "note": 2}, "claims": 10, "findings": 9}
{"by_code": {"R-MAT-CARRIED-FLAG": 2}, "by_severity": {"note": 2}, "claims": 10, "findings": 2}
```

## 6. Integration notes for D02

1. **Placement.** Paste §4 after D03's `label_parser.py` block. The block is self-contained: stdlib only (`json`, `unicodedata`), no I/O, no module-level side effects besides constants; `_selftest_era_material()` is the hook for `--selftest` (wire its result list into the tool's control report; a `False` entry must fail the selftest).
2. **Entry points.** `reconcile_scoped(packet, external_scopes=(), bridges=(), claims=None)` is the packet-level call (D03's `parse_typed_labels` output is *not* required — claims are derived from `packet["costumes"]`; if D02 prefers labels, pass `claims=` built from `referent_id`/`era_window`/`material_ids`). `reconcile_claims(...)` is the pure core for synthetic controls.
3. **Exit mapping (recommendation).** `ReconciliationError` → exit 2 (could-not-evaluate, same class as the parser's `P-*`). Any `R-*` finding line → exit 1, matching the lane's gate precedent ("0 clean: no finding lines printed; 1 findings: one or more FINDING lines printed (any severity)" — `tools/gates/costume-era-consistency-gate.py` docstring). Notes must print, not vanish: the carried flags are the packet's own declared debt.
4. **Vocabulary vs D03 and vs the spec.** D03 emits `E-*`/`W-*` with `where`/`detail`/`severity` (error|warning); this shard emits `R-*` with `where`/`scope`/`detail`/`severity` (reject|hold|note) **plus** `verdict` and `class` carrying the design spec's vocabulary verbatim (`identity` / `mapped-confirmed` / `mapped-unconfirmed` / `unmapped`; `available` / `unavailable-by-closure` / `unresolved`; `D2L-ERA` / `D2L-MATERIAL` / `D2L-SCOPE`). The spec's §8.1 records the id delta and asks D02 to declare one mapping table — this shard pre-declares it per finding, so no second table is needed for the `R-*` class; the `E-*`/`W-*`/`TL-*` ids still need the spec's own mapping. `where` is the same shape (record id) in all three families, so the lists concatenate.
5. **`slot` field.** Slot conflicts and slot-identity checks are keyed on a `slot` field that the design spec requires (§3.1 M1/M3: "match by slot, never by label", citing `11-costumes.yml:110-114`) but the real packet does **not** yet declare on its material records (checked: `grep -c '^    slot:' examples/culture-d2/packet.d2.yml` → 0 on 2026-10-17). The OQ-3 luxuries (CMAT-08 silk vs MAT-07 lowland-broadcloth) are the motivating case; until the field is declared by the component owner, the conflict surfaces only through the `maps_to`/`maps_to_note` rows and this shard's fixture. Adding `slot` to the component is a corpus-owner decision, not this shard's.
6. **Bridges are declared inputs.** For the real packet, the only bridge worth declaring is the 10-materials scope with `E2 -> E4` (per `packet.d2.yml:3254`); D02 must not auto-generate it. If the tool ships without external scopes, `maps_to` references correctly surface as `R-MAT-BRIDGE-MISSING` holds rather than silently passing. A bridge `era_map` entry may be a bare tag or a `{tag, status, scope, row}` row (ERX-style); a `to-verify` row holds with the row id cited.
7. **Rank adapter (D04).** The scope objects (`era_scope`, `material_scope`, bridge dicts) are plain dicts and can be reused by D04's adapter to scope rank-rule eras/materials the same way; no coupling is forced.
8. **D03's strict loader fails on the real packet (observed while smoke-testing this shard; D03's §6 already flags that its loader was never run on the full file).** Loading `examples/culture-d2/packet.d2.yml` with D03's `load_packet_file` returns `packet=None` with `P-UNTERMINATED-FLOW, line 82: "content '-' is not a mapping line"` — line 82 is a bare `-` sequence item followed by an indented mapping block, a form the packet uses throughout (`grep -c '^  -$'` → 138 and `grep -c '^    -$'` → 35 on 2026-10-17; the first bare dash is at line 82, inside `derivation_rules`). Consequence: `parse_typed_labels` never runs on the real packet and D02 cannot ship `--packet examples/culture-d2/packet.d2.yml` on D03's loader alone. The real-packet receipts below used the costume gate's tolerant subset parser (`tools/gates/costume-era-consistency-gate.py:330 parse_packet`) read-only instead; fixing D03's loader is D03/D02's call, not this shard's.
9. **Integration cross-check (read-only; D02 owns the tool file).** As of 2026-10-17 ~17:31 local, `tools/d2-typed-labels.py` has this block integrated (`_selftest_era_material` verbatim, `R_MAT_SLOT_MISMATCH` and `R_ERA_MAPPING_UNCONFIRMED` present, `R_ERA_EXCLUDED` absent as in §3, provenance line citing `reports/round-8/depth/shard-era-material.md (R8-D05)`), and `python3 tools/d2-typed-labels.py --selftest` exits 0 with `34/34` checks, including `ok era/material block: its own controls pass (29)`. The design spec's §8.1 recorded a `RecursionError` crash at 20:25Z; that state no longer holds on the bytes read here. Re-verify before the acceptance run — D02 edits the file concurrently.

## 7. Limits and open items

- **Interface alignment with D01 — landed and applied.** D01's design spec (`reports/round-8/depth/design-spec.md`) landed after this shard's first draft; §2/§3 and the block in §4 were re-aligned to it: mapping rows with `status`/`scope`/row id (spec §2.1 E4/E5), the conflict → exit-2 class (§2.2), slot identity (§3.1 M1/M3), and the spec's verdict vocabulary carried per finding (§6 classes `D2L-ERA`/`D2L-MATERIAL`/`D2L-SCOPE`; `D2L-DATA` raised as `ReconciliationError`). The spec's §8.1 records the id delta (`R-*` vs `D2L-*`) and asks D02 to declare a mapping table; this shard pre-declares it inside each finding. Interfaces otherwise remain aligned to D03's landed schema (`LABEL_KINDS`, `referent_id`, `era_window`, `material_ids`, `E-LABEL-*`) and the packet's real field names.
- **Real-packet receipt (run 2026-10-17, gate subset parser, block from §4 loaded read-only).** Unbridged: `{"by_code": {"R-MAT-BRIDGE-MISSING": 7, "R-MAT-CARRIED-FLAG": 2}, "by_severity": {"hold": 7, "note": 2}, "claims": 10, "findings": 9}` — the 7 holds are CMAT-01/02/04/05/06/07/09 (each `maps_to` declares an id but no bridge is supplied), the 2 notes are CMAT-03/CMAT-08 (declared carried flags); no era findings (all 10 costume eras are `E0`–`E2` tags). Bridged (external scope = the 22 `MAT-*` records of `examples/culture-d2/components/10-materials.yml`, `era_map: {}`): `{"by_code": {"R-MAT-CARRIED-FLAG": 2}, "claims": 10, "findings": 2}` — all 7 declared cross-references resolve to existing target records (no `R-MAT-DANGLING`), leaving exactly the packet's own two carried flags. This turns `assembly.unresolved`'s "10 material inventory is not unioned into 11 costume-facing routes" into an executable check: with a declared bridge the union is *verified* reference-by-reference, without one every cross-reference holds.
- **Slot checks are inert on the real packet** until `slot` is declared by the component owner (§6.5): the OQ-3 silk/broadcloth conflict is visible in the notes but not yet machine-keyed, and `R-MAT-SLOT-MISMATCH` fires only in the fixture.
- **Severity thresholds are design conventions** (lane gate vocabulary), not historical laws; no corpus or canon file was edited by this shard, and no sibling or world-bible file was read as writable.
- **`to-verify`**: the exact bridging of 10-materials' `E4` to the brief's `E2` remains a declared design choice owned by the component authors (`packet.d2.yml:3254`; ERX-1..ERX-4 stay `(to-verify)` per `11-costumes.yml:62-65`); this shard only makes the choice executable — and holds it — when supplied.
