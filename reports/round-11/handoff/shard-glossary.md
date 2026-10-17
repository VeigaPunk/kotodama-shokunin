# R11-O04 shard — glossary builder (20 entries from live lexicon content)

- shard: HANDOFF R11-O04, impl support for claims O (operability) under targets O02–O09; round 11, 2026-10-17.
- repo revision at write time: `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7` (round-11 claims' `baseline_revision`: `94ca098b8ab03be52ec80f6925538e5e2c0ed327`).
- files written by this shard: **this file only**. Scratch work lives under `.scratch/o04/` (gitignored, transient; every artifact the integrator needs is inline here).
- status: fragment runs and is verified against the shipped gate; **integrator action required** — lift the functions below into `tools/exercise-handoff-e2e.py` (single writer, O02–O05). Nothing here is a committed tool.
- what this shard is not: not the exercise, not the 16-field envelope, not `expected.json`, not a canon artifact. It supplies the glossary payload builder and its evidence.

## 1. Position in the O-claim

The O claim needs a packet assembled from live D2/D3 artifacts with `20/20 glossary entries populated from actual D2/D3 content`. This shard supplies exactly that component: a builder that reads the **live assembled artifacts** (`examples/culture-d2/packet.d2.yml`, `examples/culture-d3/packet.json`), selects 20 records by a declared deterministic rule, and renders the glossary table in the shape the committed sample uses (`| entry_id | term | gloss | etymology |`), which `tools/gates/handoff-packet-check.py` recognises as a glossary payload.

The builder never invents a form, gloss, or derivation: it copies `term`/`native_form`, `gloss`, `class`, `etymology`, `route`/`layer`/`loan_layer`/`donor_form`, `construction`/`bases`, `stage`, and the D3 `status`/`forms` fields from the live records and appends the source citation. No `demo:`-namespace ID is emitted (glossary-registry-format.md §1), and no real-world claim is made or imported.

## 2. Live sources and their state at verification time

| source | role | sha256 (measured 2026-10-17, this run) |
|---|---|---|
| `examples/culture-d2/packet.d2.yml` | live D2 assembled packet; `lexicon:` block, 40 records `L-01`–`L-40` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` |
| `examples/culture-d3/packet.json` | live D3 assembled packet; `lexicon:` block, 20 records `L01`–`L20` | `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829` |
| `examples/culture-d3/components/04-language.json` | the D3 component the packet's lexemes derive from (cited inside each D3 row) | `fee4ad61a6aa9ca524c627a04ddbe61653a4058261aadf352f3b16a63b4dacfa` |
| `examples/handoff-packet.sample.md` | committed 16-field envelope used as the swap host for verification | `4e24bd3b887cf148155d89855d3c9eb842d3e325a4fa4302fccaa6c9d23dd712` |

Both live artifacts are current: `tools/assemble-d2.py --check` and `tools/assemble-culture-d3.py --check` report byte-identical deterministic assembly (transcript §6). Record counts are copied from the parsed live blocks, not from documentation: D2 40 records, D3 20 records (this run).

## 3. The fragment (lift into `tools/exercise-handoff-e2e.py`)

Authored and executed as `.scratch/o04/frag_glossary.py`; reproduced verbatim. It reuses the lane's established YAML-subset idiom (`runpy` of the costume gate's `parse_packet`); PyYAML is not importable in this environment, so the fragment does not depend on it. `ROOT` is computed as `Path(__file__).resolve().parents[2]` for the scratch location — the integrator must change it to the tool's own root computation when lifting.

```python
#!/usr/bin/env python3
"""HANDOFF R11-O04 fragment — glossary builder (20 entries from live lexicon content).

Shard deliverable for the R11-O02..O05 exercise (tools/exercise-handoff-e2e.py).
The integrator lifts `load_d2_lexicon`, `load_d3_lexicon`, `build_rows`,
`render_table` and `SELECTIONS` into the exercise; nothing here is a new tool.

Reads the live assembled D2/D3 artifacts only:
  examples/culture-d2/packet.d2.yml   (assembled by tools/assemble-d2.py)
  examples/culture-d3/packet.json     (assembled by tools/assemble-culture-d3.py)
YAML-subset parsing reuses the lane idiom (runpy of the costume gate reader);
no PyYAML is imported because the environment has none.

Run:  python3 .scratch/o04/frag_glossary.py --emit <outdir>
"""

import argparse
import hashlib
import json
import re
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D2_PACKET = ROOT / "examples/culture-d2/packet.d2.yml"
D3_PACKET = ROOT / "examples/culture-d3/packet.json"
YAML_READER = ROOT / "tools/gates/costume-era-consistency-gate.py"

TABLE_HEADER = "| entry_id | term | gloss | etymology |\n|---|---|---|---|"

# The gate's licensed etymology-status vocabulary (glossary-registry-format.md §4):
# attested / reconstructed / constructed / contested / unknown.
LICENSED = ("attested", "reconstructed", "constructed", "contested", "unknown")


def load_d2_lexicon(path=D2_PACKET):
    """Live D2 assembled packet's lexicon block, via the gate's block reader."""
    namespace = runpy.run_path(str(YAML_READER))
    packet = namespace["parse_packet"](Path(path).read_text(encoding="utf-8"))
    records = packet.get("lexicon")
    if not isinstance(records, list) or not records:
        raise ValueError(f"{path}: no usable lexicon records")
    return records


def load_d3_lexicon(path=D3_PACKET):
    """Live D3 assembled packet's lexicon block (plain JSON)."""
    packet = json.loads(Path(path).read_text(encoding="utf-8"))
    records = packet.get("lexicon")
    if not isinstance(records, list) or not records:
        raise ValueError(f"{path}: no usable lexicon records")
    return records


def _cell(text):
    """One markdown table cell: no pipes, no newlines, whitespace collapsed."""
    return re.sub(r"\s+", " ", str(text)).replace("|", "/").strip()


# ---------------------------------------------------------------------------
# D2 row builder — status derived from the live record's own route/layer fields,
# never from its `evidence` label (design evidence is not etymology status).
# ---------------------------------------------------------------------------


def _d2_status(record):
    route = record.get("route")
    if route == "lexicalized":
        # L-32 tolsa: live sense_note says the suffix is one "no living speaker
        # can gloss" and the literal reading "is not recoverable".
        return "unknown"
    return "constructed"


def _d2_chain(record):
    route = record.get("route")
    stage = record.get("stage", "?")
    if route == "loan":
        layer = record.get("loan_layer", "undeclared layer")
        donor = record.get("donor_form", "undeclared donor form")
        return f"{stage} loan into the {layer} (donor form {donor}; donor stage reserved, substitutions per the packet layers block)"
    if route in ("derived", "compound"):
        construction = record.get("construction", "undeclared construction")
        bases = " + ".join(record.get("bases") or [])
        return f"{stage} {construction} on {bases}"
    if route == "lexicalized":
        return f"{stage} fossilised circumlocution (route lexicalized, no living gloss)"
    return f"route root at {stage} ({record.get('layer', 'layer undeclared')} layer)"


def build_d2_rows(records):
    """One row per selected D2 record; keeps the live text, adds source citation."""
    rows = []
    for record in records:
        etymology = _cell(record.get("etymology", ""))
        cell = (
            f"status: {_d2_status(record)} — {_cell(_d2_chain(record))}; {etymology}; "
            f"design record {D2_PACKET.relative_to(ROOT)} {record['id']} (live assembled packet)"
        )
        rows.append(
            {
                "entry_id": record["id"],
                "term": _cell(record["term"]),
                "gloss": _cell(f"{record['gloss']}; {record.get('class', 'form')}"),
                "etymology": cell,
            }
        )
    return rows


# ---------------------------------------------------------------------------
# D3 row builder — the live record carries an explicit constructed `status`
# and its own E0/E1 form mapping; both are used verbatim.
# ---------------------------------------------------------------------------


def build_d3_rows(records):
    rows = []
    for record in records:
        forms = record.get("forms") or {}
        e0 = forms.get(record.get("available_from", "E0"))
        e1 = forms.get("E1")
        if e0 is None:
            e0 = record.get("native_form", "?")
        if e1 is None:
            e1 = e0
        stage_note = (
            f"stage forms {e0} (E0) → {e1} (E1), the record's own forms block"
            if e0 != e1
            else f"stage forms unchanged E0/E1 ({e0})"
        )
        status = record.get("status", "unknown")
        cell = (
            f"status: {_cell(status)} — native constructed form; {stage_note}; "
            f"design record examples/culture-d3/components/04-language.json {record['id']} (live assembled packet)"
        )
        rows.append(
            {
                "entry_id": record["id"],
                "term": _cell(record["native_form"]),
                "gloss": _cell(record["gloss"]),
                "etymology": cell,
            }
        )
    return rows


# ---------------------------------------------------------------------------
# Selection rules — declared, deterministic, loud on mismatch.
# ---------------------------------------------------------------------------


def select_first(records, count=20):
    if len(records) < count:
        raise ValueError(f"selection needs {count} records, source has {len(records)}")
    return records[:count]


def select_stratified(records, per_field=2):
    """per_field records per field, fields in first-appearance order, artifact order within a field."""
    order = []
    buckets = {}
    for record in records:
        field = record.get("field", "unfielded")
        if field not in buckets:
            buckets[field] = []
            order.append(field)
        buckets[field].append(record)
    if per_field * len(order) != 20:
        raise ValueError(f"stratified selection yields {per_field * len(order)} over {len(order)} fields, not 20")
    picked = []
    for index in range(per_field):
        for field in order:
            if index < len(buckets[field]):
                picked.append(buckets[field][index])
    if len(picked) != 20:
        raise ValueError(f"stratified selection produced {len(picked)} rows, not 20")
    return picked


SELECTIONS = {
    "d2-first-20": lambda: build_d2_rows(select_first(load_d2_lexicon())),
    "d2-stratified-20": lambda: build_d2_rows(select_stratified(load_d2_lexicon())),
    "d3-all-20": lambda: build_d3_rows(load_d3_lexicon()),
}


def render_table(rows):
    lines = [TABLE_HEADER]
    for row in rows:
        lines.append(f"| {row['entry_id']} | {row['term']} | {row['gloss']} | {row['etymology']} |")
    return "\n".join(lines) + "\n"


def check_licensed(rows):
    """Local guard: every cell names a licensed status token."""
    bad = []
    for row in rows:
        match = re.search(r"(?i)\bstatus\s*[:=]\s*`?\*?([A-Za-z_-]+)", row["etymology"])
        token = match.group(1).lower() if match else "?"
        if token not in LICENSED:
            bad.append((row["entry_id"], token))
    return bad


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit")
    parser.add_argument("--selection", choices=sorted(SELECTIONS), default=None)
    args = parser.parse_args(argv)
    names = [args.selection] if args.selection else sorted(SELECTIONS)
    outdir = Path(args.emit) if args.emit else None
    if outdir:
        outdir.mkdir(parents=True, exist_ok=True)
    for name in names:
        rows = SELECTIONS[name]()
        bad = check_licensed(rows)
        if bad:
            raise SystemExit(f"{name}: unlicensed status tokens {bad}")
        table = render_table(rows)
        digest = hashlib.sha256(table.encode("utf-8")).hexdigest()
        print(f"{name}: rows={len(rows)} sha256={digest}")
        if outdir:
            (outdir / f"glossary-{name}.md").write_text(table, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

Selection presets (declared, deterministic, loud on mismatch):

| preset | rule | applies to |
|---|---|---|
| `d3-all-20` | all 20 live D3 lexicon records, ID order | a D3-scoped packet; 20 records = 20 entries |
| `d2-stratified-20` | 2 records per field, fields in first-appearance order, artifact order within a field (= 10 fields × 2 = 20) | a D2-scoped packet; covers every field the live lexicon populates |
| `d2-first-20` | first 20 records in artifact order (`L-01`–`L-20`) | fallback / differential |

The builder raises rather than silently emitting a short table: `select_stratified` asserts the field count makes exactly 20, `select_first` asserts enough records, and `check_licensed` rejects any row whose cell does not name a licensed status token (`attested` / `reconstructed` / `constructed` / `contested` / `unknown`, glossary-registry-format.md §4).

**Recommended default**: `d2-stratified-20` for a D2 packet (single-culture scope per contract §4; all ten lexicon fields represented), `d3-all-20` for a D3 packet. Composing a mixed D2+D3 glossary in one packet is *not* recommended: the contract's `scope` field is per culture/group, and the two drills are separate cultures — do not merge their lexicons into one payload without a design decision from O01.

Status derivation (the honest part — no laundering):

- D2 records have no `etymology.status` field. The fragment assigns `constructed` to every route except `lexicalized`; the lexicalized record (`L-32 tolsa`) is assigned **`unknown`**, because its live `sense_note` states the suffix is one "no living speaker can gloss" and "the literal reading is not recoverable". The live `evidence:` label (`design-choice` / `attested-comparator`) is deliberately **not** used as an etymology status: design evidence is not etymology status.
- Loan rows (`L-26`, `L-27`) carry `layer: loan`, `loan_layer`, and `donor_form` from the live record; the donor stage is left as the live packet leaves it (`reserved`), so no contact claim is strengthened.
- D3 rows use the live record's own `status` field verbatim plus its own `forms` block for the E0/E1 note; the fragment adds no sound-law claim.

## 4. Emission A — `d2-stratified-20` (recommended for a D2 packet)

20 entries, drawn from `examples/culture-d2/packet.d2.yml` (live, digest above). Table sha256 (of the exact markdown bytes in the emitted file) is recorded in §7.

| entry_id | term | gloss | etymology |
|---|---|---|---|
| L-01 | ir | breath (the soul-carrier of a person); noun | status: constructed — route root at E0 (native layer); underived D2 root; ritual speech pairs ir with su (wind) — the one designed colexification of this packet, unchecked against CLICS3 until a check is run (to-verify); design record examples/culture-d2/packet.d2.yml L-01 (live assembled packet) |
| L-04 | las | lineage (the pasture-holding patrilineal descent group); noun | status: constructed — route root at E0 (native layer); underived D2 root; the lineage is the property-holding unit of pasture rights, which is the social fact the terminology is chosen from (no universal chief, no assembly of witnesses); design record examples/culture-d2/packet.d2.yml L-04 (live assembled packet) |
| L-08 | su | wind; noun | status: constructed — route root at E0 (native layer); underived D2 root; wind is the medium of the breath and the carrier of news, oath and death, and every slope-wind word is built on it; design record examples/culture-d2/packet.d2.yml L-08 (live assembled packet) |
| L-13 | bel | the heights (the upper country, the summer side); noun | status: constructed — route root at E0 (native layer); underived D2 root; the upper pole of the transhumance cycle and the base of the whole vertical set; design record examples/culture-d2/packet.d2.yml L-13 (live assembled packet) |
| L-18 | ral | flock animal (a head of smallstock; the counting unit of wealth); noun | status: constructed — route root at E0 (native layer); underived; the generic-level term of the folk-biological hierarchy and the unit in which herds, tolls and bride-wealth are counted; design record examples/culture-d2/packet.d2.yml L-18 (live assembled packet) |
| L-25 | kor | tally-cord (a hanging line whose knots record herd counts and pasture claims); noun | status: constructed — route root at E0 (native layer); underived; a counting-technology unit read by knot height — RG-01 governs the geometry (height encodes magnitude or register, never ownership), and the cord counts rather than binds; design record examples/culture-d2/packet.d2.yml L-25 (live assembled packet) |
| L-29 | wal | oath, the sworn word; noun | status: constructed — route root at E0 (native layer); underived; an oath is sworn against the herd and in the moving air, which is what the compound suwal later makes explicit — the obligation is held, not tied; design record examples/culture-d2/packet.d2.yml L-29 (live assembled packet) |
| L-34 | mir | fleece, wool (on the animal or off it); noun | status: constructed — route root at E0 (native layer); underived; the fiber word of a wool-exporting culture, which is why the costume field borrows nothing here; design record examples/culture-d2/packet.d2.yml L-34 (live assembled packet) |
| L-36 | lasin | lineage head (the elder who keeps the pasture tally and speaks the lineage herd count at the fair); noun | status: constructed — E0 AGENT on las; las (lineage) plus AGENT; authority is a task held by an elder and not an inherited title, which is the segmentary pattern and not a chiefdom; design record examples/culture-d2/packet.d2.yml L-36 (live assembled packet) |
| L-38 | gen | raid, herd-taking (the sanctioned raid to recover stolen animals, not a war of conquest); noun | status: constructed — route root at E0 (native layer); underived; raiding vocabulary indexes force organisation, and D2 has no standing army — one word carries the whole institution; design record examples/culture-d2/packet.d2.yml L-38 (live assembled packet) |
| L-02 | nel | hand and forearm, one term (no separate word for the forearm or the wrist); noun | status: constructed — route root at E0 (native layer); underived D2 root; the partition covers hand and forearm as one working segment (the milking grip) — the single anomalous partition this body field is allowed; design record examples/culture-d2/packet.d2.yml L-02 (live assembled packet) |
| L-05 | wen | father; noun | status: constructed — route root at E0 (native layer); underived; the everyday reference and address term of the father line; design record examples/culture-d2/packet.d2.yml L-05 (live assembled packet) |
| L-09 | hur | storm (the wind that takes animals and flattens the summer camp); noun | status: constructed — route root at E0 (native layer); underived; the storm is an agent with a law, which is why the storm-breath hurir is the oath-keeper of this packet; design record examples/culture-d2/packet.d2.yml L-09 (live assembled packet) |
| L-14 | tol | the low ground (the valley floor, the winter side); noun | status: constructed — route root at E0 (native layer); underived D2 root; the lower pole, paired with bel — the two roots together are how this culture says where anything is, and no body-part frame is used for it; design record examples/culture-d2/packet.d2.yml L-14 (live assembled packet) |
| L-19 | nir | sheep; noun | status: constructed — route root at E0 (native layer); underived; the wool animal, named at the generic level below ral; design record examples/culture-d2/packet.d2.yml L-19 (live assembled packet) |
| L-26 | kas | the written tally-sheet demanded at the salt fair (a debt record); noun | status: constructed — E1 loan into the Salt-road trade layer (donor form gas; donor stage reserved, substitutions per the packet layers block); loan from the lowland trade partner, donor gas (the written tally), devoiced g to k on entry; the referent arrives with the salt road, which is why the word and the sheet share a date; design record examples/culture-d2/packet.d2.yml L-26 (live assembled packet) |
| L-30 | belir | the upper breath (the sky-wind that carries the soul at death); noun | status: constructed — E0 SPIRIT on bel; bel (the heights) plus SPIRIT; the sacred stratum of the wind spine — the breath goes up, and the upslope wind belsu is felt to carry it; design record examples/culture-d2/packet.d2.yml L-30 (live assembled packet) |
| L-35 | mirken | wool cloak (the felted wrap worn at both pastures); noun | status: constructed — E0 GARMENT on mir; mir plus GARMENT; worn through the ascent and against the storm wind, which is why the record carries both axes — one garment floor term is enough for this stage, and the full route is costume-side (CP-09); design record examples/culture-d2/packet.d2.yml L-35 (live assembled packet) |
| L-37 | belin | the vanguard herder (the one who opens the summer pasture each season; a task-rank, not a title); noun | status: constructed — E0 AGENT on bel; bel (the heights) plus AGENT; whoever goes up first holds the season for the rest, so the rank is read off the ascent order; design record examples/culture-d2/packet.d2.yml L-37 (live assembled packet) |
| L-39 | genra | the raiding ground (the disputed pasture at the pass where raids arrive); noun | status: constructed — E0 LOC on gen; gen plus LOC; the pasture beside the pass is both the toll site and the raid ground, which is the coupling this field exists for; design record examples/culture-d2/packet.d2.yml L-39 (live assembled packet) |

## 5. Emission B — `d3-all-20`

20 entries = the whole live D3 lexicon; rows cite `examples/culture-d3/components/04-language.json` (the component the packet's lexemes derive from) and were read through `examples/culture-d3/packet.json`.

| entry_id | term | gloss | etymology |
|---|---|---|---|
| L01 | pina | spoken pledge | status: constructed — native constructed form; stage forms pina (E0) → fina (E1), the record's own forms block; design record examples/culture-d3/components/04-language.json L01 (live assembled packet) |
| L02 | suma | hearth invocation | status: constructed — native constructed form; stage forms unchanged E0/E1 (suma); design record examples/culture-d3/components/04-language.json L02 (live assembled packet) |
| L03 | talu | record line | status: constructed — native constructed form; stage forms unchanged E0/E1 (talu); design record examples/culture-d3/components/04-language.json L03 (live assembled packet) |
| L04 | palu | boundary token | status: constructed — native constructed form; stage forms palu (E0) → falu (E1), the record's own forms block; design record examples/culture-d3/components/04-language.json L04 (live assembled packet) |
| L05 | pira | witness mark | status: constructed — native constructed form; stage forms pira (E0) → fira (E1), the record's own forms block; design record examples/culture-d3/components/04-language.json L05 (live assembled packet) |
| L06 | puka | gate announcement | status: constructed — native constructed form; stage forms puka (E0) → fuka (E1), the record's own forms block; design record examples/culture-d3/components/04-language.json L06 (live assembled packet) |
| L07 | tana | thread count | status: constructed — native constructed form; stage forms unchanged E0/E1 (tana); design record examples/culture-d3/components/04-language.json L07 (live assembled packet) |
| L08 | kila | measured fold | status: constructed — native constructed form; stage forms unchanged E0/E1 (kila); design record examples/culture-d3/components/04-language.json L08 (live assembled packet) |
| L09 | ruma | assembly seat | status: constructed — native constructed form; stage forms unchanged E0/E1 (ruma); design record examples/culture-d3/components/04-language.json L09 (live assembled packet) |
| L10 | masin | marker cord | status: constructed — native constructed form; stage forms unchanged E0/E1 (masin); design record examples/culture-d3/components/04-language.json L10 (live assembled packet) |
| L11 | nisu | night tally | status: constructed — native constructed form; stage forms unchanged E0/E1 (nisu); design record examples/culture-d3/components/04-language.json L11 (live assembled packet) |
| L12 | lura | hall passage | status: constructed — native constructed form; stage forms unchanged E0/E1 (lura); design record examples/culture-d3/components/04-language.json L12 (live assembled packet) |
| L13 | sina | visitor sign | status: constructed — native constructed form; stage forms unchanged E0/E1 (sina); design record examples/culture-d3/components/04-language.json L13 (live assembled packet) |
| L14 | kalti | weft edge | status: constructed — native constructed form; stage forms unchanged E0/E1 (kalti); design record examples/culture-d3/components/04-language.json L14 (live assembled packet) |
| L15 | rusi | appointed token | status: constructed — native constructed form; stage forms unchanged E0/E1 (rusi); design record examples/culture-d3/components/04-language.json L15 (live assembled packet) |
| L16 | ami | settlement | status: constructed — native constructed form; stage forms unchanged E0/E1 (ami); design record examples/culture-d3/components/04-language.json L16 (live assembled packet) |
| L17 | nara | felt work-wrap | status: constructed — native constructed form; stage forms unchanged E0/E1 (nara); design record examples/culture-d3/components/04-language.json L17 (live assembled packet) |
| L18 | salu | plain work-wrap | status: constructed — native constructed form; stage forms unchanged E0/E1 (salu); design record examples/culture-d3/components/04-language.json L18 (live assembled packet) |
| L19 | mila | assembly robe | status: constructed — native constructed form; stage forms unchanged E0/E1 (mila); design record examples/culture-d3/components/04-language.json L19 (live assembled packet) |
| L20 | kuru | horn rank-clasp | status: constructed — native constructed form; stage forms unchanged E0/E1 (kuru); design record examples/culture-d3/components/04-language.json L20 (live assembled packet) |

## 6. Verification transcript (real runs, 2026-10-17, this checkout)

The method: take the committed sample packet (a 16-field envelope that already passes the gate), split it at its glossary table, substitute the candidate table, and run the shipped gate on the recomposed packet in place. This isolates the glossary payload — the only variable — and exercises the real `check_glossary` / `HO-GLOSS-ETYM` path.

$ /usr/bin/python3 tools/assemble-d2.py --check
(exit 0)
packet.d2.yml: byte-identical deterministic assembly

$ /usr/bin/python3 tools/assemble-culture-d3.py --check
(exit 0)
packet.json: byte-identical deterministic assembly; packet.gates.yml: byte-identical deterministic assembly

$ /usr/bin/python3 .scratch/o04/frag_glossary.py --emit .scratch/o04
(exit 0)
d2-first-20: rows=20 sha256=b2970b43197b5c0e23d429f7914bcca700cdb497a723130beb8c8fecadd1cec9
d2-stratified-20: rows=20 sha256=2cd5e3521083bcbaa3123e23693ea2bddb5f23c6f7230007a9e91adbfb682f36
d3-all-20: rows=20 sha256=56a070ec0e885ec791af8e97f3e2ec5914f7b00e264bea43e3028b75adaa3b19

$ /usr/bin/python3 .scratch/o04/verify_swap.py
(exit 0)
sample split: head=9450 tail=1 bytes
d2-first-20: exit=0 CLEAN | INFO scan: fields=16/16 glossary-entries=20 findings=0
d2-stratified-20: exit=0 CLEAN | INFO scan: fields=16/16 glossary-entries=20 findings=0
d3-all-20: exit=0 CLEAN | INFO scan: fields=16/16 glossary-entries=20 findings=0
control empty-cell: exit=1 HO-GLOSS-ETYM=1
    FINDING HO-GLOSS-ETYM: FAIL — glossary entry L-01 carries no etymology text; an explicit `unknown` with a reason is valid, an empty cell is not (glossary-registry-format.md §4)
control placeholder-cell: exit=1 HO-GLOSS-ETYM=1
    FINDING HO-GLOSS-ETYM: FAIL — glossary entry L-01 carries no etymology text; an explicit `unknown` with a reason is valid, an empty cell is not (glossary-registry-format.md §4)
control unlicensed-status: exit=1 HO-GLOSS-ETYM=1
    FINDING HO-GLOSS-ETYM: FAIL — glossary entry L-01 states etymology status 'borrowed', outside the licensed vocabulary attested, reconstructed, constructed, contested, unknown (glossary-registry-format.md §4)
control dropped-entries: exit=0 HO-GLOSS-ETYM=0

$ /usr/bin/python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md
(exit 0)
INFO scan: fields=16/16 glossary-entries=20 findings=0

Reading of the transcript:

- all three emissions: `exit=0`, `INFO scan: fields=16/16 glossary-entries=20 findings=0` — 16/16 envelope fields and 20/20 glossary entries with zero findings.
- control `empty-cell` and control `placeholder-cell`: exit 1 with one `HO-GLOSS-ETYM` finding each — the check is live, not vacuous.
- control `unlicensed-status` (`status: borrowed`): exit 1, message names the licensed vocabulary — the status vocabulary check bites.
- control `dropped-entries` (ten rows deleted): exit 0 — **the gate does not enforce an entry count**. The `20/20` requirement is therefore *not* gate-enforced and must be asserted by the exercise itself (count the rendered rows against the design's declared count); this shard's builder always emits exactly 20 by construction, and returns the row count so the exercise can assert it.
- the recomposed D2 packet differs from the sample in exactly 1 diff hunk / 41 changed lines (the 20 sample rows replaced) — the glossary table region only.

## 7. Frozen pins for O14/O15 (`expected.json`)

The exercise's frozen baseline should pin both the source digests and the emitted table digest, so a drift in either is caught:

```json
{
 "sources": {
  "examples/culture-d2/packet.d2.yml": "e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643",
  "examples/culture-d3/packet.json": "bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829",
  "examples/culture-d3/components/04-language.json": "fee4ad61a6aa9ca524c627a04ddbe61653a4058261aadf352f3b16a63b4dacfa",
  "examples/handoff-packet.sample.md": "4e24bd3b887cf148155d89855d3c9eb842d3e325a4fa4302fccaa6c9d23dd712"
 },
 "fragment": {
  ".scratch/o04/frag_glossary.py": "bcc75953d17a5d87c7eadef7c9785ac4ce432fb658e9e944683a1fb00eb0e10e"
 },
 "tables": {
  "d2-stratified-20": "2cd5e3521083bcbaa3123e23693ea2bddb5f23c6f7230007a9e91adbfb682f36",
  "d3-all-20": "56a070ec0e885ec791af8e97f3e2ec5914f7b00e264bea43e3028b75adaa3b19",
  "d2-first-20": "b2970b43197b5c0e23d429f7914bcca700cdb497a723130beb8c8fecadd1cec9"
 }
}
```

`d2-first-20` and `d3-all-20` rows are also available (hashes above) as differential fixtures; `d2-first-20`'s rows are `L-01`–`L-20` in artifact order and its cells use the same builder paths as Emission A.

## 8. What this establishes, and its limits

Establishes (each with the command in §6):

- a 20-entry glossary **can be assembled from live D2 and D3 lexicon content** with no placeholder, no fabricated etymology, and every cell naming a licensed status — verified by the shipped gate at 16/16 + 20/20 + 0 findings, with three malformed controls firing.
- provenance is inside every row (source path + record ID) and the sources are byte-pinned and `--check`-fresh.

Limits / `to-verify`:

- **the gate cannot tell a native form from a translated label** — it checks only that the etymology cell is present and names a licensed status. This builder cannot leak a translated label through the `term` column (it copies the live `term`/`native_form` field only, never the English gloss), but that is a property of the builder, not something the gate verifies. The O16–O18 reviewers should check the rendered terms against the live records themselves: the D3 projection's `assembly.legacy_projection.trace` carries `term_projected` (e.g. `L01 → fina`) for lexemes and `display_label` for costumes and names — a reviewer should confirm neither value can reach the term column, and that no English display label appears in any `term` cell of §4/§5.
- D2 row count assertion: D2's live packet has 40 records and the A-04 coverage floors are unmet by design (component `05-lexicon.yml` declares the delta); a 20-entry payload is a **sample**, not the coverage claim, and the exercise must not present it as coverage.
- the fragment's D2 status assignment (`constructed`, plus `unknown` for `L-32`) is this lane's reading of the live records, not a record-level field; if the design (O01) wants per-record statuses carried into the artifacts themselves, that is a component change (owner: the D2 component's author), not something this shard may do.
- the D3 `gloss` cells are bare glosses without a part-of-speech suffix (the live D3 records carry no `class`); the sample's style uses `; noun`. If O01 wants a uniform column style, the fix is in the fragment's `build_d3_rows` (one line), not in the data.
- the *envelope* (16 fields) exercised here is the committed sample's envelope, not the exercise's own; assembling the real envelope from live D2/D3 artifacts is O01/O06–O13 work. This shard claims only the glossary payload and its gate behaviour.

## 9. Handoff notes to the single writer (O02–O05)

- hook points: `load_d2_lexicon`, `load_d3_lexicon`, `build_d2_rows`, `build_d3_rows`, `select_first`, `select_stratified`, `render_table`, `check_licensed`, `SELECTIONS`. `build_*_rows` return dicts (`entry_id`, `term`, `gloss`, `etymology`); `render_table` returns the full markdown table including the header row; `select_*` take the parsed record list so the exercise can inject fixtures.
- the exercise should assert `len(rows) == 20` from the builder's own return value (the gate will not), and should compare the rendered table bytes against the frozen digest in §7.
- keep the `TMPDIR=$PWD/.scratch` convention when the exercise writes isolated copies (operator rule; `/tmp` is inode-exhausted).
- if the design chooses a different source or ordering, only `SELECTIONS` changes; the row builders and the licensed-status guard stay valid.
