# R11-D04 — gate reader adapter shard (fragment): the read side of the typed pipeline

- seat: **R11-D04** (gate adapter shard), round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17.
- assignment (verbatim): "DEPTH R11-D04 (gate adapter shard): gate reader adapter accepting the
  typed packet; fragment reports/round-11/depth/shard-gate-adapter.md."
- writes: this file only, plus in-lane scratch under `.scratch/d04/**`. No file under `tools/`,
  `examples/`, `corpus/` or `reports/round-{5,6,7,8,9,10}/**` is written or edited by this seat.
  No commit, no push.
- canon: NON-CANON engineering evidence. Nothing here admits a round, a capability or a canon fact;
  the owed garment forms are lore-shokunin's (`PROVINCE.md`).
- status: **COMPLETE** against the landed design (`reports/round-11/depth/design.md`, 2026-10-17
  19:06 local = 22:06Z). The module is exercised end-to-end over live artifacts; the design's
  §2.2 adapter output and §3 read-side contract are both implemented in the fragment (§4 notes the
  one interface extension and the single-writer seam).

## 0. What this shard delivers

One module (fragment, §2) with two readers over the round-8 typed projection:

| reader | entry | contract |
|---|---|---|
| projection view | `read_projection(projection_path, packet_path=None)` | labels routed into `sound_channel` / `off_channel`; `named_holds` (recorded + synthesized); provenance (`stale` vs the live packet) |
| typed packet, design §2.2/§2.3 | `ChannelView(projection, packet)` + `typed_packet_bytes(...)` + `read_typed_packet(typed, projection, packet)` | routing table (one row per off-channel/held record), coverage checks, field moves (`garment` → `garment_gloss`), assembly pins, pipeline finding set; fail-closed read-back |

Routing rules implemented (design §2.3, shipped three-kind contract of
`tools/d2-typed-labels.py:414-418`): a supplied `native-form`/`borrowed-strata` keeps its checked
field; a `translated-label` (or a sound kind without supplied bytes) moves off the sound/identity
channel and carries `D2L-FORM-UNRESOLVED` when a slot is owed; an unknown kind is refused
(`A-KIND`), never guessed onto a channel. A hold the routing requires but the projection failed to
record is **synthesized** with `"synthesized": true` — this is the adapter-side answer to design
§8 item 3 (the projector is silent for a declared sound kind without bytes; the deviation must be
visible, never silently patched).

Fail-closed codes: `A-DATA` (malformed root / missing fields / unknown status or severity),
`A-KIND` (unknown kind), `A-COVERAGE` (routing table ≠ projection routing; a routed record absent
from the packet; a sound record routed), `A-STALE` (projection pin ≠ live packet bytes — a hard
error, never a warning, design §2.2), `A-CHANNEL` (checked field still present / off-channel field
missing on a routed record), `A-HOLD` (a required hold not carried in the typed packet), `A-IO`.
Exit semantics: 0 = ok; 1 = `--check` byte mismatch; 2 = could-not-evaluate.

## 1. Evidence summary (all 2026-10-17, lane root, `TMPDIR=$PWD/.scratch`, HEAD `e3ef1719`)

| leg | command | reading |
|---|---|---|
| selftest | `python3 .scratch/d04/gate-reader-adapter.py --selftest` | **32/32 checks passed** (P1 fixture routing + R4; P2 live hold set; N1–N8 malformed/laundering; T1–T9 typed-packet cycle, coverage, smuggled-field and no-typed_findings controls; synthetic stale-pin control) |
| live projection view | `… --projection examples/culture-d2/typed-labels.d2.yml --packet examples/culture-d2/packet.d2.yml` | labels 58 (46 native / 10 translated / 2 borrowed) — sound 48, off 10, holds 15, synthesized 0; `provenance: stale=False` (D07's re-pin landed 2026-10-17 22:14Z; the committed projection is now sha `a3aa452c…`) |
| emit cycle | `… --projection examples/culture-d2/typed-labels.d2.yml --packet examples/culture-d2/packet.d2.yml --emit .scratch/d04/packet.d2.typed.yml` | wrote 159499 bytes, `typed_channel` rows 10, exit 0 |
| check | `… --check .scratch/d04/packet.d2.typed.yml` | "byte-identical deterministic typed packet", exit 0 |
| read-back | `python3 .scratch/d04/typed-packet-readback.py` | 10 routes (GAR-01..10, channel `off-sound-and-identity`, hold `D2L-FORM-UNRESOLVED`), 48 sound records, 15 holds; exit 0 |
| stale refusal | `… --projection examples/culture-d2/typed-labels.d2.yml --emit …` at 22:10Z (pre-re-pin), and the synthetic zeroed-pin control in the selftest | 22:10Z on the committed file: `could-not-evaluate [A-STALE]: projection pins packet 8da90b07… but the live packet hashes e0f21509…`, exit 2. Since the re-pin the live file is fresh; the mechanism stays covered by the synthetic control (T4) |
| determinism | two `--json` runs; two builds | byte-identical (`view-live-a.json` sha `0dfdf8d7…`, emitted payload equal on rebuild) |
| consumer differential | five real gates over the emitted typed packet vs the legacy packet | naming gate: legacy 17 lines → typed 7 lines; the diff is **exactly** the ten GAR `PHON-INVENTORY` FAILs (`7,16d6`); phonology `1ce5f0cd…`, lexicon/myth/costume byte-identical (empty) |
| lift-sim | module copied into a `tools/`-shaped scratch dir | selftest green; `--holds` output identical (`18ec7837…`) |
| cross-implementation | `read_typed_packet(.scratch/D03/repo4/out/packet.d2.typed.yml, …, typed-labels.r11.yml, packet.d2.yml)` | **accepted**: D03's independently built emission (sha `7782485b…`) yields the same 10 routes, 48 sound records, 15 holds; their rows matched this reader's expected rows field-for-field on first contact — the only divergence was the `typed_findings` key (T9) |

The naming-gate typed stdout sha256 `feb6488127f115f986bf7602c0b074ce911c951751e5e2c63e32e5d23bb52bd9`
equals the design's independently produced all-routed stdout (design §1.3) — two different packets
(this fragment's emitted packet, sha `5347a682…`, and D01's scratch packet) yield the same gate
reading. The differential is corroboration of design L2 pre-integration, not the D09–D16 suite.

## 2. The module (verbatim, lift-ready fragment)

Target per design §7: `tools/assemble-d2-typed.py` (single writer D03/D04). The module imports the
frozen `parse_packet` (costume gate) and `yaml_lines` (assembler) read-only via `runpy` — it never
re-implements them, and `tools/assemble-d2.py` stays byte-frozen for the d3 pins (D15 §4).

```python
#!/usr/bin/env python3
"""gate-reader-adapter — R11-D04 fragment: read-side contract for the typed D2 packet.

A gate (or the D2 flow driver) reads the typed projection emitted by
`tools/d2-typed-labels.py --emit` through this adapter instead of re-deriving
label routing from the legacy packet:

  sound_channel  the ONLY records a gate may submit to a sound/identity test:
                 kind in {native-form, borrowed-strata} AND status supplied
  off_channel    translated-label records (never sound-tested); the shipped
                 tool's three kinds are mirrored exactly — an unknown kind is
                 refused (A-KIND), never guessed onto either channel
  named_holds    the hold set the gate must carry instead of manufacturing
                 representation artifacts (the ten GAR `PHON-INVENTORY` FAILs
                 of the frozen round-4 run are exactly this class)
  findings       pass-through of the projection's finding list, normalized
  provenance     the projection's recorded packet pin vs the live packet

Fail-closed: malformed root, missing/invalid required fields, unknown
kind/status/severity, or a supplied sound record without text -> TypedPacketError
with a stable `A-*` code and no traceback (a calling gate maps this to its
could-not-evaluate exit). A hold the routing requires but the projection does
not record is synthesized with `synthesized: true` — an off-channel record can
never be laundered into a silent pass.

Determinism: sorted output, LF, no timestamps, no host paths; read-only over
the projection and the packet (it never rewrites either).

Usage (stdout; exit 0 = view built, 2 = could-not-evaluate):
    python3 gate-reader-adapter.py --projection PATH [--packet PATH]
    python3 gate-reader-adapter.py --projection PATH --holds
    python3 gate-reader-adapter.py --projection PATH --json
    python3 gate-reader-adapter.py --selftest
"""

import argparse
import hashlib
import json
from pathlib import Path
import runpy
import sys

# ---------------------------------------------------------------------------
# Contract constants — mirror tools/d2-typed-labels.py:414-418 exactly
# ---------------------------------------------------------------------------

KINDS = ("translated-label", "native-form", "borrowed-strata")
SOUND_KINDS = ("native-form", "borrowed-strata")
OFF_KINDS = ("translated-label",)
STATUSES = ("supplied", "to-verify", "absent")
SEVERITIES = ("hold", "note", "fail")

# Design-spec §8.1 proposes a five-kind superset (fictional-coordinate,
# descriptive-gloss) that "must never enter the sound channel". The shipped
# tool ships three (KINDS above). The adapter refuses both unknowns
# (A-KIND) rather than guess a channel; if D01/D02 adopts the superset,
# extend KINDS and OFF_KINDS here in one place.
PROPOSED_EXTRA_KINDS = ("fictional-coordinate", "descriptive-gloss")

HOLD_FORM_UNRESOLVED = "D2L-FORM-UNRESOLVED"

REQUIRED_FIELDS = ("id", "owner", "kind", "status")


class TypedPacketError(ValueError):
    """Fail-closed read error; `code` is a stable A-* diagnostic, no traceback."""

    def __init__(self, code, detail):
        self.code = code
        self.detail = detail
        super().__init__(f"{code}: {detail}")


def _is_str(value):
    return isinstance(value, str) and bool(value)


def _load_projection(path):
    text = Path(path).read_text(encoding="utf-8")
    try:
        doc = json.loads(text)
    except json.JSONDecodeError as exc:
        raise TypedPacketError("A-DATA", f"projection is not one JSON document: {exc}") from exc
    if not isinstance(doc, dict):
        raise TypedPacketError("A-DATA", "projection root is not a mapping")
    block = doc.get("typed_labels")
    if not isinstance(block, dict) or not isinstance(block.get("labels"), list):
        raise TypedPacketError("A-DATA", "typed_labels.labels is missing or not a list")
    return doc


def _label(raw, index):
    if not isinstance(raw, dict):
        raise TypedPacketError("A-DATA", f"labels[{index}] is not a mapping")
    where = raw.get("id") if _is_str(raw.get("id")) else f"labels[{index}]"
    for field in REQUIRED_FIELDS:
        if not _is_str(raw.get(field)):
            raise TypedPacketError("A-DATA", f"{where}: required field {field!r} is missing")
    kind, status = raw["kind"], raw["status"]
    if kind not in KINDS:
        extra = " (design-spec §8.1 superset kind not adopted by the shipped tool)" \
            if kind in PROPOSED_EXTRA_KINDS else ""
        raise TypedPacketError("A-KIND", f"{where}: kind {kind!r} is not one of {KINDS}{extra}")
    if status not in STATUSES:
        raise TypedPacketError("A-DATA", f"{where}: status {status!r} is not one of {STATUSES}")
    if kind in SOUND_KINDS and status == "supplied" and not _is_str(raw.get("text")):
        raise TypedPacketError("A-DATA", f"{where}: supplied sound record carries no text")
    return dict(raw)


def _findings(doc):
    raw = doc.get("findings") or []
    if not isinstance(raw, list):
        raise TypedPacketError("A-DATA", "findings is not a list")
    out = []
    for index, item in enumerate(raw):
        if not isinstance(item, dict):
            raise TypedPacketError("A-DATA", f"findings[{index}] is not a mapping")
        severity = item.get("severity")
        if severity not in SEVERITIES:
            raise TypedPacketError("A-DATA", f"findings[{index}]: severity {severity!r} is not one of {SEVERITIES}")
        if not _is_str(item.get("code")) or item.get("where") is None \
                or not isinstance(item.get("where"), (str, int)):
            raise TypedPacketError("A-DATA", f"findings[{index}]: code/where missing")
        out.append(dict(item))
    return out


class TypedPacketView:
    """Read-only routed view of one typed projection."""

    def __init__(self, labels, findings, doc, packet_path=None):
        self._labels = tuple(labels)
        self._findings = tuple(findings)
        self._doc = doc
        self.sound_channel = tuple(
            label for label in self._labels
            if label["kind"] in SOUND_KINDS and label["status"] == "supplied"
        )
        self.off_channel = tuple(label for label in self._labels if label["kind"] in OFF_KINDS)
        self.named_holds = self._named_holds()
        self.provenance = self._provenance(packet_path)

    # -- routing -----------------------------------------------------------

    def _supplied_keys(self):
        return {
            (label["owner"], label.get("label_id") or label["id"])
            for label in self.sound_channel
        }

    def _named_holds(self):
        """The projection's holds, plus every hold the routing requires but
        the projection failed to record (`synthesized: true`)."""
        holds = [dict(item) for item in self._findings if item.get("severity") == "hold"]
        recorded = {(item["code"], str(item["where"])) for item in holds}
        supplied = self._supplied_keys()
        for label in self._labels:
            owed = (
                label["kind"] in OFF_KINDS and label["status"] == "supplied"
                or label["kind"] in SOUND_KINDS and label["status"] != "supplied"
            )
            if not owed:
                continue
            key = (label["owner"], label.get("label_id") or label["id"])
            if label["kind"] in OFF_KINDS and key in supplied:
                continue  # R4: the supplied native form governs; no hold owed
            marker = (HOLD_FORM_UNRESOLVED, label["id"])
            if marker in recorded:
                continue
            holds.append({
                "code": HOLD_FORM_UNRESOLVED,
                "where": label["id"],
                "detail": "synthesized by the adapter: owed-form hold missing from the projection",
                "severity": "hold",
                "synthesized": True,
            })
            recorded.add(marker)
        return tuple(sorted(holds, key=lambda item: (item["code"], str(item["where"]))))

    def hold_set(self):
        """Canonical, comparable hold set: sorted `code:where` keys."""
        seen = set()
        for item in self.named_holds:
            seen.add(f"{item['code']}:{item['where']}")
        return tuple(sorted(seen))

    def hold_set_diff(self, expected):
        """Compare the observed hold set with a declared expected set.

        `expected` is an iterable of `"code:where"` strings or `{code, where}`
        mappings. Returns {expected, observed, missing, surplus, equal}.
        """
        exp = set()
        for item in expected:
            if _is_str(item):
                exp.add(item)
            elif isinstance(item, dict):
                exp.add(f"{item['code']}:{item['where']}")
            else:
                raise TypedPacketError("A-DATA", f"expected hold entry {item!r} is not a string or mapping")
        obs = set(self.hold_set())
        return {
            "expected": len(exp), "observed": len(obs),
            "missing": sorted(exp - obs), "surplus": sorted(obs - exp),
            "equal": exp == obs,
        }

    def stats(self):
        counts = {kind: 0 for kind in KINDS}
        for label in self._labels:
            counts[label["kind"]] += 1
        return {
            "labels": len(self._labels),
            "by_kind": counts,
            "sound_channel": len(self.sound_channel),
            "off_channel": len(self.off_channel),
            "holds": len(self.named_holds),
            "synthesized_holds": sum(1 for item in self.named_holds if item.get("synthesized")),
        }

    def _provenance(self, packet_path):
        assembly = self._doc.get("assembly") or {}
        out = {
            "generator": (self._doc.get("generator") if _is_str(self._doc.get("generator")) else None),
            "packet": assembly.get("packet"),
            "packet_sha256": assembly.get("packet_sha256"),
            "live_packet_sha256": None,
            "stale": None,
        }
        if packet_path is not None:
            live = hashlib.sha256(Path(packet_path).read_bytes()).hexdigest()
            out["live_packet_sha256"] = live
            out["stale"] = live != out["packet_sha256"]
        return out

    def as_dict(self):
        return {
            "stats": self.stats(),
            "hold_set": list(self.hold_set()),
            "named_holds": [dict(item) for item in self.named_holds],
            "sound_channel": [dict(item) for item in self.sound_channel],
            "off_channel": [dict(item) for item in self.off_channel],
            "findings": [dict(item) for item in self._findings],
            "provenance": self.provenance,
        }


def read_projection(projection_path, packet_path=None):
    """Projection reader entry: projection path -> TypedPacketView (fail-closed)."""
    doc = _load_projection(projection_path)
    labels = [_label(raw, index) for index, raw in enumerate(doc["typed_labels"]["labels"])]
    findings = _findings(doc)
    return TypedPacketView(labels, findings, doc, packet_path=packet_path)


# ---------------------------------------------------------------------------
# typed packet — design.md §2.2/§2.3 (emit side and gate read side)
# ---------------------------------------------------------------------------

# owner -> (packet block, the field the record used to be checked on)
FIELD_MAP = {
    "11-costumes": ("costumes", "garment"),
    "05-lexicon": ("lexicon", "term"),
    "13-naming": ("names", "name"),
}
OFF_FIELD_SUFFIX = "_gloss"
CHANNEL_OFF = "off-sound-and-identity"


def _import_readonly(name, leaf):
    """Import one callable from a frozen tool via runpy; never re-implement."""
    ns = runpy.run_path(str(_repo_root() / name))
    return ns[leaf]


def load_packet(path):
    """Parse the gate-facing packet with the costume gate's own reader."""
    parse = _import_readonly("tools/gates/costume-era-consistency-gate.py", "parse_packet")
    malformed = _import_readonly("tools/gates/costume-era-consistency-gate.py", "Malformed")
    try:
        doc = parse(Path(path).read_text(encoding="utf-8"))
    except malformed as exc:
        raise TypedPacketError("A-DATA", f"packet is outside the declared subset: {exc}") from exc
    if not isinstance(doc, dict):
        raise TypedPacketError("A-DATA", "packet root is not a mapping")
    return doc


def _yaml_payload(doc):
    lines = _import_readonly("tools/assemble-d2.py", "yaml_lines")
    return ("\n".join(lines(doc)) + "\n").encode("utf-8")


def _section_records(packet, block):
    section = packet.get(block)
    return section if isinstance(section, list) else []


class ChannelView:
    """Projection + packet -> the routing table (design §2.3) and its holds."""

    def __init__(self, projection_path, packet_path):
        self._doc = _load_projection(projection_path)
        self._packet_path = Path(packet_path)
        self.packet = load_packet(packet_path)
        live = hashlib.sha256(self._packet_path.read_bytes()).hexdigest()
        pinned = (self._doc.get("assembly") or {}).get("packet_sha256")
        if pinned != live:
            raise TypedPacketError(
                "A-STALE", f"projection pins packet {pinned} but the live packet hashes {live} "
                           "(re-pin the projection before wiring; design §2.2)")
        self._labels = tuple(_label(raw, i) for i, raw in enumerate(self._doc["typed_labels"]["labels"]))
        self._findings = _findings(self._doc)
        self.sound = tuple(l for l in self._labels
                           if l["kind"] in SOUND_KINDS and l["status"] == "supplied")
        self.off = tuple(l for l in self._labels if l["kind"] in OFF_KINDS)
        self.held = tuple(l for l in self._labels
                          if l["kind"] in SOUND_KINDS and l["status"] != "supplied")
        self.routes = self._routes()
        self.named_holds = self._named_holds()
        self.check_coverage()

    # -- routing (design §2.3) --------------------------------------------

    def _owned_field(self, label):
        owner = label["owner"]
        if owner not in FIELD_MAP:
            raise TypedPacketError("A-DATA", f"{label['id']}: owner {owner!r} has no declared routing field")
        return FIELD_MAP[owner]

    def _routes(self):
        rows = []
        for label in self.off + self.held:
            block, field = self._owned_field(label)
            held_owner = label["kind"] in OFF_KINDS
            key = (label["owner"], label.get("label_id") or label["id"])
            owed = not held_owner or key not in {
                (l["owner"], l.get("label_id") or l["id"]) for l in self.sound}
            rows.append({
                "record": label["id"],
                "kind": label["kind"],
                "label_id": label.get("label_id"),
                "owner": label["owner"],
                "source_field": field,
                "off_channel_field": field + OFF_FIELD_SUFFIX,
                "channel": CHANNEL_OFF,
                "hold": HOLD_FORM_UNRESOLVED if owed else None,
                "_block": block,
            })
        rows.sort(key=lambda r: r["record"])
        seen = set()
        for row in rows:
            if row["record"] in seen:
                raise TypedPacketError("A-COVERAGE", f"duplicate routing row for {row['record']}")
            seen.add(row["record"])
        return tuple(rows)

    # -- holds (same contract as the projection view) ----------------------

    def _named_holds(self):
        holds = [dict(item) for item in self._findings if item.get("severity") == "hold"]
        recorded = {(item["code"], str(item["where"])) for item in holds}
        for row in self.routes:
            if not row["hold"]:
                continue
            marker = (row["hold"], row["record"])
            if marker in recorded:
                continue
            holds.append({
                "code": row["hold"],
                "where": row["record"],
                "detail": "synthesized by the adapter: owed-form hold missing from the projection",
                "severity": "hold",
                "synthesized": True,
            })
            recorded.add(marker)
        return tuple(sorted(holds, key=lambda item: (item["code"], str(item["where"]))))

    def hold_set(self):
        return tuple(sorted({f"{item['code']}:{item['where']}" for item in self.named_holds}))

    def hold_set_diff(self, expected):
        exp = set()
        for item in expected:
            exp.add(item if _is_str(item) else f"{item['code']}:{item['where']}")
        obs = set(self.hold_set())
        return {"expected": len(exp), "observed": len(obs),
                "missing": sorted(exp - obs), "surplus": sorted(obs - exp), "equal": exp == obs}

    # -- coverage ----------------------------------------------------------

    def check_coverage(self):
        """Every routed record exists in the packet; every off-channel record
        has exactly one row; no sound record is routed (design §2.2)."""
        ids = set()
        for block in ("costumes", "lexicon", "names"):
            for entry in _section_records(self.packet, block):
                if isinstance(entry, dict) and _is_str(entry.get("id")):
                    ids.add(entry["id"])
        for row in self.routes:
            if row["record"] not in ids:
                raise TypedPacketError("A-COVERAGE",
                                       f"routing row {row['record']} names a record the packet does not carry")
        routed = {row["record"] for row in self.routes}
        for label in self.off + self.held:
            if label["id"] not in routed:
                raise TypedPacketError("A-COVERAGE", f"{label['id']}: no routing row")
        for label in self.sound:
            if label["id"] in routed:
                raise TypedPacketError("A-COVERAGE", f"{label['id']}: supplied sound record routed off-channel")
        return True

    def typed_packet_doc(self, adapter_sha256):
        """The derived packet (design §2.2): packet blocks + typed_channel +
        assembly pins. The source packet object is never mutated."""
        doc = {key: value for key, value in self.packet.items() if key != "assembly"}
        routed = {}
        for row in self.routes:
            routed.setdefault(row["_block"], {})[row["record"]] = row
        for block, rows_by_id in routed.items():
            entries = []
            for entry in _section_records(self.packet, block):
                if isinstance(entry, dict) and entry.get("id") in rows_by_id:
                    row = rows_by_id[entry["id"]]
                    entry = dict(entry)
                    entry[row["off_channel_field"]] = entry.pop(row["source_field"], None)
                entries.append(entry)
            doc[block] = entries
        doc["typed_channel"] = [{key: value for key, value in row.items() if not key.startswith("_")}
                                for row in self.routes]
        doc["typed_findings"] = [dict(item) for item in self.named_holds]
        doc["assembly"] = {
            "packet": str(self._doc.get("assembly", {}).get("packet") or "examples/culture-d2/packet.d2.yml"),
            "packet_sha256": self._doc.get("assembly", {}).get("packet_sha256"),
            "projection_sha256": "",
            "adapter_sha256": adapter_sha256,
        }
        return doc

    def typed_packet_bytes(self, adapter_sha256, projection_path):
        doc = self.typed_packet_doc(adapter_sha256)
        doc["assembly"]["projection_sha256"] = hashlib.sha256(Path(projection_path).read_bytes()).hexdigest()
        return _yaml_payload(doc)


def read_typed_packet(packet_typed_path, projection_path, packet_path):
    """Gate read side (design §3): accept the typed packet, verify pins,
    coverage and field moves against the live projection and packet; return
    the routing rows, the kept sound set and the hold set (fail-closed)."""
    parse = _import_readonly("tools/gates/costume-era-consistency-gate.py", "parse_packet")
    malformed = _import_readonly("tools/gates/costume-era-consistency-gate.py", "Malformed")
    try:
        doc = parse(Path(packet_typed_path).read_text(encoding="utf-8"))
    except malformed as exc:
        raise TypedPacketError("A-DATA", f"typed packet is outside the declared subset: {exc}") from exc
    if not isinstance(doc, dict):
        raise TypedPacketError("A-DATA", "typed packet root is not a mapping")
    rows = doc.get("typed_channel")
    if not isinstance(rows, list) or not rows:
        raise TypedPacketError("A-DATA", "typed_channel is missing or empty")
    assembly = doc.get("assembly")
    if not isinstance(assembly, dict):
        raise TypedPacketError("A-DATA", "assembly pins are missing")
    live_packet = hashlib.sha256(Path(packet_path).read_bytes()).hexdigest()
    live_projection = hashlib.sha256(Path(projection_path).read_bytes()).hexdigest()
    if assembly.get("packet_sha256") != live_packet:
        raise TypedPacketError("A-STALE", "typed packet pins a different packet sha256")
    if assembly.get("projection_sha256") != live_projection:
        raise TypedPacketError("A-STALE", "typed packet pins a different projection sha256")

    view = ChannelView(projection_path, packet_path)
    expected = [{key: value for key, value in row.items() if not key.startswith("_")} for row in view.routes]
    got = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise TypedPacketError("A-DATA", f"typed_channel[{index}] is not a mapping")
        missing = [key for key in ("record", "kind", "label_id", "owner", "source_field",
                                   "off_channel_field", "channel", "hold") if key not in row]
        if missing:
            raise TypedPacketError("A-DATA", f"typed_channel[{index}]: fields missing {missing}")
        got.append({key: row[key] for key in
                    ("record", "kind", "label_id", "owner", "source_field",
                     "off_channel_field", "channel", "hold")})
    if got != expected:
        missing = [r["record"] for r in expected if r not in got]
        extra = [r["record"] for r in got if r not in expected]
        raise TypedPacketError("A-COVERAGE", f"typed_channel differs from the projection routing: "
                                             f"missing {missing}, extra {extra}")

    for row in rows:
        entry = next((e for e in _section_records(doc, FIELD_MAP[row["owner"]][0])
                      if isinstance(e, dict) and e.get("id") == row["record"]), None)
        if entry is None:
            raise TypedPacketError("A-COVERAGE", f"{row['record']}: routed record absent from the typed packet")
        if row["source_field"] in entry:
            raise TypedPacketError("A-CHANNEL", f"{row['record']}: checked field {row['source_field']!r} still present")
        if row["off_channel_field"] not in entry:
            raise TypedPacketError("A-CHANNEL", f"{row['record']}: off-channel field {row['off_channel_field']!r} missing")

    findings = doc.get("typed_findings")
    if findings is None:
        # D03's assemble-d2-typed.py follows design §2.2 literally and carries no
        # typed_findings block; fall back to the projection's own finding set, so
        # the read side accepts both packet forms (cross-check 2026-10-17 22:13Z).
        findings = [dict(item) for item in view.named_holds]
    if not isinstance(findings, list):
        raise TypedPacketError("A-DATA", "typed_findings is present but not a list")
    carried = {(item.get("code"), str(item.get("where"))) for item in findings
               if item.get("severity") == "hold"}
    for item in view.named_holds:
        if (item["code"], str(item["where"])) not in carried:
            raise TypedPacketError("A-HOLD", f"hold {item['code']}:{item['where']} not carried in the typed packet")
    return {
        "routes": got,
        "sound": [dict(l) for l in view.sound],
        "holds": [dict(item) for item in view.named_holds],
        "hold_set": list(view.hold_set()),
        "assembly": dict(assembly),
    }


# ---------------------------------------------------------------------------
# selftest — positive + malformed controls, scratch-confined
# ---------------------------------------------------------------------------

def _positive_projection():
    return {
        "generator": "selftest",
        "assembly": {"packet": "fixture.yml", "packet_sha256": "0" * 64},
        "typed_labels": {"labels": [
            {"id": "L-01", "owner": "05-lexicon", "kind": "native-form",
             "status": "supplied", "text": "ir", "label_id": None},
            {"id": "L-26", "owner": "05-lexicon", "kind": "borrowed-strata",
             "status": "supplied", "text": "kas", "label_id": None},
            {"id": "GAR-01", "owner": "11-costumes", "kind": "translated-label",
             "status": "supplied", "text": "winter valley coat", "label_id": "LEX-GAR-01"},
            {"id": "GAR-04", "owner": "11-costumes", "kind": "translated-label",
             "status": "supplied", "text": "lowland-cloth coat", "label_id": "LEX-GAR-04"},
            {"id": "LEX-GAR-04", "owner": "11-costumes", "kind": "native-form",
             "status": "supplied", "text": "ravin", "label_id": "LEX-GAR-04"},
            {"id": "L-15", "owner": "05-lexicon", "kind": "native-form",
             "status": "to-verify", "text": None, "label_id": None},
        ]},
        "findings": [
            {"code": "D2L-FORM-UNRESOLVED", "where": "GAR-01", "severity": "hold",
             "detail": "label_id LEX-GAR-01 has no supplied native/borrowed form"},
            {"code": "D2L-FORM-UNRESOLVED", "where": "L-15", "severity": "hold",
             "detail": "declared sound kind with no supplied bytes"},
        ],
    }


def _repo_root():
    for parent in Path(__file__).resolve().parents:
        if (parent / "examples/culture-d2/typed-labels.d2.yml").exists():
            return parent
    return Path.cwd()


def selftest():
    import tempfile

    passed, failures = 0, []

    def ck(name, cond, detail=""):
        nonlocal passed
        if cond:
            passed += 1
        else:
            failures.append(f"{name}: {detail}")

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        root = _repo_root()
        live = root / "examples/culture-d2/typed-labels.d2.yml"
        packet = root / "examples/culture-d2/packet.d2.yml"

        # P1 positive fixture: routing, R4 (native governs), hold synthesis off
        fixture = tmp / "positive.json"
        fixture.write_text(json.dumps(_positive_projection()), encoding="utf-8")
        view = read_projection(fixture)
        ck("P1 sound channel is exactly the three supplied sound records (R4 native LEX-GAR-04 governs)",
           sorted(l["id"] for l in view.sound_channel) == ["L-01", "L-26", "LEX-GAR-04"],
           [l["id"] for l in view.sound_channel])
        ck("P1 off channel is the two translated labels",
           sorted(l["id"] for l in view.off_channel) == ["GAR-01", "GAR-04"], "")
        ck("P1 holds equal the recorded two (GAR-01 owed; L-15 bytes owed)",
           view.hold_set() == ("D2L-FORM-UNRESOLVED:GAR-01", "D2L-FORM-UNRESOLVED:L-15"),
           view.hold_set())
        ck("P1 R4: GAR-04 carries no hold (native form supplied)",
           not any(item["where"] == "GAR-04" for item in view.named_holds), "")
        ck("P1 no synthesized holds in a complete projection",
           view.stats()["synthesized_holds"] == 0, "")

        # P2 live projection: frozen observed hold set and channel invariants
        view = read_projection(live, packet_path=packet)
        observed = view.hold_set()
        ck("P2 live labels 58 (46 native / 10 translated / 2 borrowed)",
           view.stats()["labels"] == 58 and view.stats()["by_kind"] ==
           {"native-form": 46, "translated-label": 10, "borrowed-strata": 2}, view.stats())
        ck("P2 sound channel carries no off-channel record",
           all(l["kind"] in SOUND_KINDS for l in view.sound_channel), "")
        ck("P2 ten GAR holds present",
           sum(1 for key in observed if key.startswith("D2L-FORM-UNRESOLVED:GAR-")) == 10, observed)
        ck("P2 hold set has 15 entries", len(observed) == 15, len(observed))
        ck("P2 provenance staleness is computed against the live packet bytes",
           view.provenance["live_packet_sha256"] == hashlib.sha256(packet.read_bytes()).hexdigest()
           and view.provenance["stale"] ==
           (view.provenance["packet_sha256"] != view.provenance["live_packet_sha256"]),
           view.provenance)

        # N1 not JSON
        bad = tmp / "n1.yml"
        bad.write_text("[not json", encoding="utf-8")
        try:
            read_projection(bad)
            failures.append("N1 non-JSON: no error")
        except TypedPacketError as exc:
            ck("N1 non-JSON refused with A-DATA", exc.code == "A-DATA", exc.code)

        # N2 missing typed_labels
        bad = tmp / "n2.json"
        bad.write_text(json.dumps({"findings": []}), encoding="utf-8")
        try:
            read_projection(bad)
            failures.append("N2 missing typed_labels: no error")
        except TypedPacketError as exc:
            ck("N2 missing typed_labels refused with A-DATA", exc.code == "A-DATA", exc.code)

        # N3 unknown kind (proposed superset kind) — never routed to sound
        doc = _positive_projection()
        doc["typed_labels"]["labels"].append(
            {"id": "E0-tag", "owner": "09-eras", "kind": "fictional-coordinate",
             "status": "supplied", "text": "Open Grazing", "label_id": None})
        bad = tmp / "n3.json"
        bad.write_text(json.dumps(doc), encoding="utf-8")
        try:
            read_projection(bad)
            failures.append("N3 unknown kind: no error")
        except TypedPacketError as exc:
            ck("N3 unknown kind refused with A-KIND", exc.code == "A-KIND", exc.code)

        # N4 supplied sound record without text
        doc = _positive_projection()
        doc["typed_labels"]["labels"][0]["text"] = None
        bad = tmp / "n4.json"
        bad.write_text(json.dumps(doc), encoding="utf-8")
        try:
            read_projection(bad)
            failures.append("N4 sound without text: no error")
        except TypedPacketError as exc:
            ck("N4 supplied sound without text refused with A-DATA", exc.code == "A-DATA", exc.code)

        # N5 unknown severity
        doc = _positive_projection()
        doc["findings"][0]["severity"] = "warning"
        bad = tmp / "n5.json"
        bad.write_text(json.dumps(doc), encoding="utf-8")
        try:
            read_projection(bad)
            failures.append("N5 unknown severity: no error")
        except TypedPacketError as exc:
            ck("N5 unknown severity refused with A-DATA", exc.code == "A-DATA", exc.code)

        # N6 hold laundering: owed form, hold dropped from the projection
        doc = _positive_projection()
        doc["findings"] = [f for f in doc["findings"] if f["where"] != "GAR-01"]
        bad = tmp / "n6.json"
        bad.write_text(json.dumps(doc), encoding="utf-8")
        view = read_projection(bad)
        synth = [item for item in view.named_holds if item.get("synthesized")]
        ck("N6 dropped owed-form hold is re-synthesized",
           [item["where"] for item in synth] == ["GAR-01"], view.hold_set())
        ck("N6 synthesized hold is visible as synthesized",
           all(item.get("synthesized") is True for item in synth), "")

        # N7 held-slot hold laundering: to-verify sound record, hold dropped
        doc = _positive_projection()
        doc["findings"] = [f for f in doc["findings"] if f["where"] != "L-15"]
        bad = tmp / "n7.json"
        bad.write_text(json.dumps(doc), encoding="utf-8")
        view = read_projection(bad)
        ck("N7 dropped bytes-owed hold is re-synthesized",
           "D2L-FORM-UNRESOLVED:L-15" in view.hold_set(), view.hold_set())

        # N8 hold_set_diff is exact
        doc = _positive_projection()
        bad = tmp / "n8.json"
        bad.write_text(json.dumps(doc), encoding="utf-8")
        view = read_projection(bad)
        good = view.hold_set_diff(["D2L-FORM-UNRESOLVED:GAR-01", "D2L-FORM-UNRESOLVED:L-15"])
        miss = view.hold_set_diff(["D2L-FORM-UNRESOLVED:GAR-01"])
        ck("N8 diff equal on exact set, surplus visible on a short expected set",
           good["equal"] and not miss["equal"]
           and miss["surplus"] == ["D2L-FORM-UNRESOLVED:L-15"] and miss["missing"] == [], miss)

        # T1 typed-packet cycle: mechanical re-pin (design §5.1), emit, read back
        fresh_doc = json.loads(live.read_text(encoding="utf-8"))
        fresh_doc["assembly"]["packet_sha256"] = hashlib.sha256(packet.read_bytes()).hexdigest()
        fresh = tmp / "projection-fresh.json"
        fresh.write_text(json.dumps(fresh_doc), encoding="utf-8")
        chan = ChannelView(fresh, packet)
        ck("T1 routing table is exactly the ten GAR rows, all off-channel",
           [r["record"] for r in chan.routes] == [f"GAR-{i:02d}" for i in range(1, 11)]
           and all(r["channel"] == CHANNEL_OFF for r in chan.routes),
           [r["record"] for r in chan.routes])
        ck("T1 every routed row holds D2L-FORM-UNRESOLVED",
           all(r["hold"] == HOLD_FORM_UNRESOLVED for r in chan.routes), "")
        ck("T1 adapter hold set is the frozen fifteen", len(chan.hold_set()) == 15, chan.hold_set())

        emitted = tmp / "packet.d2.typed.yml"
        payload = chan.typed_packet_bytes(adapter_sha256(), fresh)
        emitted.write_bytes(payload)
        ck("T2 typed packet build is byte-deterministic",
           payload == chan.typed_packet_bytes(adapter_sha256(), fresh), "")

        got = read_typed_packet(emitted, fresh, packet)
        ck("T3 read-back carries 10 routes, 15 holds, 48 sound records",
           (len(got["routes"]), len(got["holds"]), len(got["sound"])) == (10, 15, 48),
           (len(got["routes"]), len(got["holds"]), len(got["sound"])))
        typed_doc = load_packet(emitted)
        moved = all(
            isinstance(e, dict) and "garment" not in e and "garment_gloss" in e
            for e in typed_doc["costumes"] if e.get("id", "").startswith("GAR-"))
        ck("T3 checked field garment moved to garment_gloss on all ten", moved, "")

        # T4 stale pin is a hard error, never a warning (design §2.2). The
        # committed projection is fresh since D07's re-pin (2026-10-17 22:14Z),
        # so the control is synthetic: pin the projection to a wrong packet hash.
        stale_doc = json.loads(live.read_text(encoding="utf-8"))
        stale_doc["assembly"]["packet_sha256"] = "0" * 64
        stale_projection = tmp / "projection-stale.json"
        stale_projection.write_text(json.dumps(stale_doc), encoding="utf-8")
        try:
            ChannelView(stale_projection, packet)
            failures.append("T4 stale projection pin: no error")
        except TypedPacketError as exc:
            ck("T4 stale projection pin refused with A-STALE", exc.code == "A-STALE", exc.code)
        ck("T4 the committed projection is fresh at this read (D07 re-pin landed)",
           ChannelView(live, packet) is not None, "")

        base = load_packet(emitted)

        def mutated(name, fn):
            doc = json.loads(json.dumps(base))
            fn(doc)
            path = tmp / name
            path.write_bytes(_yaml_payload(doc))
            return path

        def expect(name, path, code):
            try:
                read_typed_packet(path, fresh, packet)
                failures.append(f"{name}: no error")
            except TypedPacketError as exc:
                ck(f"{name} refused with {code}", exc.code == code, exc.code)

        # T5 duplicate routing row
        expect("T5 duplicate routing row", mutated(
            "t5.yml", lambda d: d["typed_channel"].append(dict(d["typed_channel"][0]))), "A-COVERAGE")
        # T6 dropped routing row
        expect("T6 dropped routing row", mutated(
            "t6.yml", lambda d: d["typed_channel"].pop(0)), "A-COVERAGE")
        # T7 hold laundered out of the typed packet
        expect("T7 laundered hold", mutated(
            "t7.yml", lambda d: d.__setitem__("typed_findings", [
                f for f in d["typed_findings"] if f.get("where") != "GAR-01"])), "A-HOLD")
        # T8 checked field smuggled back onto the routed record
        def smuggled(d):
            for e in d["costumes"]:
                if e.get("id") == "GAR-01":
                    e["garment"] = e.get("garment_gloss")
        expect("T8 checked field smuggled back", mutated("t8.yml", smuggled), "A-CHANNEL")

        # T9 packet without typed_findings (D03's emission form) still reads
        path = mutated("t9.yml", lambda d: d.pop("typed_findings"))
        got = read_typed_packet(path, fresh, packet)
        ck("T9 packet without typed_findings falls back to the projection finding set",
           len(got["holds"]) == 15 and len(got["routes"]) == 10,
           (len(got["holds"]), len(got["routes"])))

    if failures:
        for failure in failures:
            print(f"selftest FAIL: {failure}", file=sys.stderr)
        print(f"selftest: {passed}/{passed + len(failures)} checks passed", file=sys.stderr)
        return 1
    print(f"selftest: {passed}/{passed} checks passed — positive (fixture routing, R4, live "
          "hold set, channel invariants, stale-pin provenance, typed-packet emit/read cycle) "
          "plus malformed, laundering and routing-coverage controls; no file outside the "
          "temporary directory touched")
    return 0


def adapter_sha256():
    """Self-digest, so a freeze row's gate hash transitively pins this file."""
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--projection", help="path to typed-labels.d2.yml (the typed projection)")
    parser.add_argument("--packet", help="live packet path")
    parser.add_argument("--emit", metavar="PATH",
                        help="write the typed packet (build product; use a scratch/mirror path)")
    parser.add_argument("--check", nargs="?", const="", metavar="PATH",
                        help="compare the typed packet bytes without writing")
    parser.add_argument("--holds", action="store_true", help="print the named hold set, one key per line")
    parser.add_argument("--json", action="store_true", help="print the projection view as one JSON document")
    parser.add_argument("--selftest", "--self-test", action="store_true", dest="selftest")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()
    if not args.projection:
        parser.error("--projection PATH is required (or use --selftest)")
    try:
        if args.emit or args.check is not None:
            if not args.packet:
                parser.error("--packet PATH is required with --emit/--check")
            chan = ChannelView(args.projection, args.packet)
            payload = chan.typed_packet_bytes(adapter_sha256(), args.projection)
            if args.emit:
                Path(args.emit).write_bytes(payload)
                print(f"wrote {args.emit} ({len(payload)} bytes, typed_channel rows {len(chan.routes)})")
                return 0
            if not args.check:
                parser.error("--check needs a PATH")
            if Path(args.check).read_bytes() != payload:
                print(f"{args.check} differs from the deterministic typed packet", file=sys.stderr)
                return 1
            print(f"{args.check}: byte-identical deterministic typed packet")
            return 0
        view = read_projection(args.projection, packet_path=args.packet)
    except (TypedPacketError, OSError) as exc:
        code = exc.code if isinstance(exc, TypedPacketError) else "A-IO"
        print(f"could-not-evaluate [{code}]: {exc}", file=sys.stderr)
        return 2
    if args.holds:
        for key in view.hold_set():
            print(key)
        return 0
    if args.json:
        print(json.dumps(view.as_dict(), ensure_ascii=False, indent=1, sort_keys=True))
        return 0
    stats = view.stats()
    print(f"labels {stats['labels']} ({stats['by_kind']}) — sound {stats['sound_channel']}, "
          f"off {stats['off_channel']}, holds {stats['holds']} "
          f"(synthesized {stats['synthesized_holds']})")
    if view.provenance["stale"] is not None:
        print(f"provenance: stale={view.provenance['stale']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## 3. Live hold set observed (the design §4.2 fifteen, independently reproduced)

```
D2L-FORM-UNRESOLVED:GAR-01 … D2L-FORM-UNRESOLVED:GAR-10   (10 rows, the wired GAR labels)
D2L-NATIVE:L-15, D2L-NATIVE:L-16                          (carried unchanged from round 8)
R-RANK-CONFLICT:TR-04#a|TR-06#a, WR-02#g|WR-09#g, WR-08#g|WR-09#g
```

`hold_set_diff` consumes either `"code:where"` strings or `{code, where}` mappings, so the D06
baseline (`expected-holds.json`, `{id, severity, where, detail}` records) can be compared directly:
build the expected list as `f"{h['id']}:{h['where']}"`. The excluded note
(`D2L-RANK:SR-01#a|SR-01#b`, severity `note`) stays in `findings` and is excluded from
`named_holds` / `hold_set`.

## 4. Interface notes for the integrator (D03/D05/D06 and the design)

1. **Seam.** `read_typed_packet` is the gate's read side (design §3 legs L1–L4); `ChannelView` +
   `typed_packet_bytes` are the adapter output side (design §2.2). The integrator can lift the whole
   module into `tools/assemble-d2-typed.py`, or split it: read side into
   `tools/gates/typed-pipeline-gate.py` (D05).
2. **Findings carriage, reconciled with D03 (cross-check 2026-10-17 22:13Z):** D03's
   `assemble-d2-typed.py` follows design §2.2 literally and emits **no** `typed_findings` block; this
   module's emit adds one (design §3.1 L3 reads the finding set "from the typed run"). The read side
   accepts both forms: when `typed_findings` is absent it falls back to the projection's own finding
   set (control T9). Cross-contact result: D03's emission (sha `7782485b…`) was accepted as-is by
   `read_typed_packet` — 10 routes / 48 sound / 15 holds — with their routing rows matching this
   reader's expected rows field-for-field; only the extra key differed. Decision for the integrator:
   carry or drop `typed_findings`; nothing else separates the two fragments on the read contract.
3. **`hold: null`** marks a routed record that owes no hold (R4: a supplied native form governs).
   For `examples/culture-d2` all ten rows carry `D2L-FORM-UNRESOLVED`.
4. **`assembly.adapter_sha256`** is the module's self-digest (`adapter_sha256()`), so a freeze row's
   gate hash pins the emitting file transitively (design §5.2's circularity concern is D20's).
5. **Synthesized holds** (`"synthesized": true`) are the design §8.3 requirement: report the
   projector deviation, never patch it silently. Controls N6/N7/T-series prove hold laundering is
   caught at both reader levels.
6. **Re-pin order** (design §5.1): D07's re-pin **landed** during this shard's run (2026-10-17
   22:14Z): the committed projection is now sha `a3aa452c…`, pin `e0f21509…`, and `ChannelView`
   accepts it. Three independent bytes agree: the committed file, the live emission
   (`.scratch/R11-D03/typed-labels.live.yml`), and D03's copy
   (`.scratch/D03/repo4/examples/culture-d2/typed-labels.r11.yml`) — all `a3aa452c…`.

## 5. Limits, not claimed, and to-verify

- **Not the shipped integration.** No file under `tools/` or `examples/` was written by this shard;
  the module is a fragment and the single writer (D03/integrator) owns the shipped file, its
  `--help` surface and its exit-code documentation (D14/P2).
- **Not the e2e acceptance.** The five-gate differential and the emit/read cycle are pre-integration
  corroboration; the claim's L2/L3/L4 legs, the frozen re-pin (D07), the new frozen revision (D08)
  and the e2e hold-set equality (D09–D16) remain theirs.
- **Stand-in resolved** (2026-10-17 22:14Z): D07's canonical re-pin landed, and the committed
  projection byte-matches the two independent scratch emissions (`a3aa452c…`, §4.6); no leg of the
  evidence table now depends on a scratch stand-in. Digests here name their observation
  (2026-10-17 22:02–22:15Z, HEAD `e3ef1719`).
- **Design-adjacent observation (reported, not absorbed):** the naming gate still exits 1 after
  routing (6 `NAME-NEAR` + 1 `CROSS-HOLD`); any leg keyed off its exit code must key off finding
  classes instead — the design already says this (§8 item 2); this fragment confirms it live.
- **Out of province:** canon status of the ten owed forms, and whether a real project licenses an
  English gloss as an in-world name — lore's business, untouched here.

## Receipts

```sh
# 2026-10-17 22:02–22:15Z, lane root, TMPDIR=$PWD/.scratch, HEAD e3ef1719c123ab4fb83ed94e033961dd61a2e8c7
python3 .scratch/d04/gate-reader-adapter.py --selftest                                  # 32/32, exit 0
python3 .scratch/d04/gate-reader-adapter.py --projection examples/culture-d2/typed-labels.d2.yml \
    --packet examples/culture-d2/packet.d2.yml                                          # sound 48, off 10, holds 15, stale=False
python3 .scratch/d04/gate-reader-adapter.py --projection examples/culture-d2/typed-labels.d2.yml --holds   # sha 18ec7837…
python3 .scratch/d04/consumer-demo.py                                                   # consumer contract OK
python3 .scratch/d04/gate-reader-adapter.py --projection examples/culture-d2/typed-labels.d2.yml \
    --packet examples/culture-d2/packet.d2.yml --emit .scratch/d04/packet.d2.typed.yml  # 159499 bytes, 10 rows
python3 .scratch/d04/gate-reader-adapter.py --projection examples/culture-d2/typed-labels.d2.yml \
    --packet examples/culture-d2/packet.d2.yml --check .scratch/d04/packet.d2.typed.yml # byte-identical
python3 .scratch/d04/typed-packet-readback.py                                           # 10 routes / 48 sound / 15 holds
# historical (pre-re-pin, 22:10Z) — the committed file pinned 8da90b07… against live e0f21509…:
python3 .scratch/d04/gate-reader-adapter.py --projection examples/culture-d2/typed-labels.d2.yml \
    --packet examples/culture-d2/packet.d2.yml --emit .scratch/d04/should-fail.yml      # A-STALE, exit 2
for g in naming-collision-gate phonology-sanity-gate lexicon-coverage-audit \
         myth-consistency-gate costume-era-consistency-gate; do
  python3 tools/gates/$g.py .scratch/d04/packet.d2.typed.yml ; done                     # differential = the ten PHON lines
# cross-implementation read of D03's emission (their adapter, sha 95ac9d05… self-pinned)
python3 -c 'import runpy; ns=runpy.run_path(".scratch/d04/gate-reader-adapter.py");
ns["read_typed_packet"](".scratch/D03/repo4/out/packet.d2.typed.yml",
    ".scratch/D03/repo4/examples/culture-d2/typed-labels.r11.yml",
    ".scratch/D03/repo4/examples/culture-d2/packet.d2.yml")'                          # accepted: 10/48/15
sha256sum .scratch/d04/gate-reader-adapter.py .scratch/d04/packet.d2.typed.yml \
    .scratch/d04/typed-naming-collision-gate.out .scratch/d04/readback.out              # b5a770be… / 5347a682… / feb64881… / d0a4228b…
```

Artifact digests at this stamp: adapter fragment
`b5a770beabe25f8e42a2293144e916f69cbe20269c0ea6b0ee739cec92891f09` (856 lines, 40700 bytes, sha
re-read after the state-agnostic control edits and re-spliced into §2 verbatim — verified by
extracting the fenced block and comparing bytes); emitted typed packet
`5347a682eee3667c8d6fa224ff2597a5ec5c1a45a41bffea797325f2ea608ad9`; committed projection
`a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` (post-re-pin; pre-re-pin it was
`e70ba147…`); live packet `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643`. The
fragment's own sha256 is listed in the D26 fragment ledger, not here (self-reference would churn).
