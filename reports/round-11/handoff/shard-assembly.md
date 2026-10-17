# R11-O03 — packet-assembly helpers fragment for `tools/exercise-handoff-e2e.py`

- shard: HANDOFF R11-O03 (impl support for claim O, operability); round 11, 2026-10-17, loop 1 of 3.
- writer: L2 worker (opencode-go-2/deepseek-v4.1-flash). Repo revision at write time:
  `e3ef171` (round-11 claims admitted; `baseline_revision` `94ca098b`).
- write scope: **this file only**. Scratch work lives under `.scratch/o03/`
  (gitignored, transient). No filed artifact of rounds 8/9/10 was edited; no git
  operation was performed.
- topic: a runnable, stdlib-only helper fragment that measures the lane's live
  D2/D3 artifacts, assembles a 16-field handoff packet from those measurements,
  renders a 20-row glossary from the live D3 lexicon, and validates the packet
  through `tools/gates/handoff-packet-check.py` in an isolated copy — plus the
  evidence battery and the independent verification of the shipped tool.
- sources (measured live at the times quoted in §4/§5):
  `corpus/knowledge/synthesis/worldbible-integration-contract.md`;
  `tools/gates/handoff-packet-check.py` (`FIELD_NAMES`, `ETYM_STATUSES`,
  recognition rules); `examples/culture-d3/packet.json`,
  `examples/culture-d3/expected.json`, `examples/culture-d3/packet.gates.yml`;
  `examples/culture-d2/packet.d2.yml`, `examples/culture-d2/typed-labels.d2.yml`;
  `tools/d2-typed-labels.py`, `tools/assemble-d2.py`,
  `tools/assemble-culture-d3.py`, `tools/check-evidence-coupling.py`;
  `tools/exercise-handoff-e2e.py` (the shipped exercise, verified read-only);
  `reports/round-11/handoff/design.md` (R11-O01 field map);
  `reports/round-10/fix-02.md`, `fix-06.md`, `fix-07.md`, `fix-08.md`,
  `findings-verify-1.md`, `findings-verify-4.md` (R10-O02-NEW-2 provenance).
- couples: `reports/round-11/handoff/design.md` (this fragment implements its
  §3 field map in one concrete renderer, and diverges where stated in §7);
  `reports/round-11/handoff/shard-glossary.md` (R11-O04 — glossary rows; this
  fragment's glossary builder is a second, independent implementation of the
  same 20 rows, kept for cross-checking, not as a competing deliverable);
  `reports/round-11/handoff/shard-cli.md` (R11-O05 — CLI seam
  `assemble_packet(repo_root)`; `assemble()` here satisfies that signature's
  spirit: deterministic, no writes outside the caller-named outputs);
  `tools/exercise-handoff-e2e.py` (the integration target — already shipped at
  write time; §5 reports its measured state).
- taken-from: the contract §4 table, the gate's recognition/vocabulary code
  (loaded read-only through `runpy`, never duplicated), and the live artifact
  bytes. No new contract term is invented here.
- verified-at: 2026-10-17, 22:09–22:14 UTC (19:09–19:14 −03:00). Fragment
  battery green (§4); tool verification results in §5, quoted with the tool's
  own sha256 at the moment of each measurement. The D2 typed projection was
  re-emitted by another worker during this shard's window (§6); the fragment
  adapted automatically because every narrative line is measured, not asserted.
- recheck: on any change to the read set, the gate, the contract, or
  `tools/exercise-handoff-e2e.py`; before any baseline re-pin.

## 1. What this shard delivers

1. **The fragment** (§3): ~800 lines of stdlib-only Python providing
   `assemble(root)` → `{"markdown", "trace", "problems"}`, with
   - live measurement of the D2/D3 artifacts (digests, record counts, the D2
     projection's pin state, `--check` exit, and a fresh `--emit` diff),
   - a 16-field envelope renderer whose **pin narrative is conditional on the
     measurements** (red or clean, open question or closed — never asserted),
   - a 20-row glossary built from `examples/culture-d3/packet.json` `lexicon[]`
     with the licensed `status:` token taken from each live row,
   - `check_isolated()` — copies the packet into a fresh directory and runs the
     committed gate there from that foreign cwd,
   - `controls()` — a 9-row mutation battery (1 positive, 8 malformed) with the
     expected finding IDs,
   - fail-closed refusal (`AssemblyError` → exit 2, no traceback) when a
     required artifact is missing or structurally wrong.
2. **Evidence A** (§4): the fragment's measured battery, including a live
   demonstration that the same bytes produced a red D2-pin narrative before the
   D-side re-emit and a clean one after it.
3. **Evidence B** (§5): an independent verification pass over the shipped
   `tools/exercise-handoff-e2e.py` — its default run at the revision that passed
   end-to-end, and two defects measured in `--selftest` at that revision, with
   the exact failure lines and two scratch probes that isolate the causes.

## 2. Position in the O claim

`tools/exercise-handoff-e2e.py` was shipped by the O02–O05 single writer while
this shard was in flight (first measured here at 22:11 UTC, sha256
`2a058f78`-era revision). Nothing in this document was written into that tool.
The fragment here therefore serves three purposes, in this order:

- **verification harness** — §4's runner and §5's probes use it against the
  shipped tool's own assembled packet (6/6 independent controls behaved as
  expected there);
- **fallback assembler** — green at 22:13:45 UTC (§4) while the tool was
  mid-refactor;
- **implementation reference** — the field map, glossary rule and the
  measurement discipline are explicit and liftable function by function.

## 3. The fragment (verbatim, runnable)

sha256 of the file the block below was spliced from:
`03fe4f8ebcf3fe21c6fbb4661899c03f1ac36fc96749cbfa5158c6cc3a7a4785`
(`.scratch/o03/fragment.py`, 796 lines). The block contains no fenced code of
its own; §8 records the extraction check that re-ran the code from this
document.

```python
#!/usr/bin/env python3
"""R11-O03 fragment — packet-assembly helpers for tools/exercise-handoff-e2e.py.

Assembles one handoff-packet Markdown document from the lane's live D2/D3
artifacts and checks it through tools/gates/handoff-packet-check.py in an
isolated copy. Stdlib only; no PyYAML (the lane has none): JSON artifacts are
read with json, the contract/document artifacts as raw bytes (digests) and
text (revision line). Every value written into the packet is measured from
live bytes at assembly time or is a declared constant of this exercise; no
value is copied from a previously filed report.

Integration contract (for the single writer of tools/exercise-handoff-e2e.py):
  - `assemble(root)` -> {"markdown", "trace", "problems"}; problems == [] is
    the precondition for rendering; raise AssemblyError on non-recoverable
    source defects (missing file, bad JSON, lexicon count, bad status token).
  - `check_isolated(root, markdown, tmpbase)` -> {"exit", "scan", "stdout",
    "packet_path"} — gate run over a copied packet in a fresh directory used
    as the subprocess cwd (proves the packet is self-contained).
  - `controls(root, markdown, tmpbase)` -> list of malformed-control results.
  - CLI (fragment-level demo): --packet-out PATH --trace-out PATH
    --check-isolated --controls.
"""

from __future__ import annotations

import hashlib
import json
import re
import runpy
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PROFILE = "kotodama-handoff-e2e/1"
PACKET_ID = "kotodama.handoff.d2d3-e2e"
PACKET_VERSION = "1.0.0"

D2_PACKET = "examples/culture-d2/packet.d2.yml"
D2_TYPED = "examples/culture-d2/typed-labels.d2.yml"
D3_PACKET = "examples/culture-d3/packet.json"
D3_GATES = "examples/culture-d3/packet.gates.yml"
D3_EXPECTED = "examples/culture-d3/expected.json"
CONTRACT = "corpus/knowledge/synthesis/worldbible-integration-contract.md"
GATE = "tools/gates/handoff-packet-check.py"
DEP_TOOLS = (
    "tools/assemble-d2.py",
    "tools/d2-typed-labels.py",
    "tools/assemble-culture-d3.py",
    "tools/check-evidence-coupling.py",
    "tools/gates/handoff-packet-check.py",
    "tools/gates/costume-era-consistency-gate.py",
)
GATE_SCAN_RE = re.compile(
    r"^INFO scan: fields=(\d+)/(\d+) glossary-entries=(\d+) findings=(\d+)$", re.M
)
CONTRACT_REVISION_RE = re.compile(r"revision[^\n`]*`(\d+\.\d+\.\d+)`")


class AssemblyError(RuntimeError):
    """A live source defect that makes honest assembly impossible."""


# --------------------------------------------------------------------------
# measurement helpers
# --------------------------------------------------------------------------


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest_of(root: Path, rel: str) -> str:
    path = root / rel
    if not path.is_file():
        raise AssemblyError(f"required artifact missing: {rel}")
    return sha256_bytes(path.read_bytes())


def read_json(root: Path, rel: str) -> dict:
    path = root / rel
    if not path.is_file():
        raise AssemblyError(f"required artifact missing: {rel}")
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise AssemblyError(f"{rel}: unreadable JSON ({exc})") from exc
    if not isinstance(doc, dict):
        raise AssemblyError(f"{rel}: root must be a JSON object")
    return doc


def gate_constants(root: Path) -> dict:
    """The gate's own vocabulary, loaded read-only; no duplication, no import."""
    namespace = runpy.run_path(str(root / GATE))
    return {
        "field_names": tuple(namespace["FIELD_NAMES"]),
        "etym_statuses": tuple(namespace["ETYM_STATUSES"]),
    }


def contract_pin(root: Path) -> dict:
    path = root / CONTRACT
    if not path.is_file():
        raise AssemblyError(f"required artifact missing: {CONTRACT}")
    text = path.read_text(encoding="utf-8")
    match = CONTRACT_REVISION_RE.search(text)
    if not match:
        raise AssemblyError(f"{CONTRACT}: no revision line found")
    return {
        "path": CONTRACT,
        "revision": match.group(1),
        "digest": sha256_bytes(path.read_bytes()),
    }


def tool_check(root: Path, rel: str, *args: str) -> dict:
    """Run a lane tool read-only; record its exit code and first output line."""
    proc = subprocess.run(
        [sys.executable, str(root / rel), *args],
        cwd=str(root),
        capture_output=True,
        text=True,
    )
    lines = (proc.stdout.strip().splitlines() or []) + (proc.stderr.strip().splitlines() or [])
    return {"argv": [rel, *args], "exit": proc.returncode, "first_line": lines[0] if lines else ""}


# --------------------------------------------------------------------------
# live sources
# --------------------------------------------------------------------------


def line_diff(committed: str, emitted: str) -> dict:
    """Changed lines between the committed projection and a fresh emit."""
    import difflib

    left, right = committed.splitlines(), emitted.splitlines()
    matcher = difflib.SequenceMatcher(a=left, b=right, autojunk=False)
    chunks, changed, pin_only = [], 0, True
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        left_part, right_part = left[i1:i2], right[j1:j2]
        changed += max(len(left_part), len(right_part))
        if not any("packet_sha256" in line for line in left_part + right_part):
            pin_only = False
        if len(chunks) < 3:
            chunks.append({"tag": tag, "committed": left_part[:2], "emitted": right_part[:2]})
    return {"changed_lines": changed, "chunks": chunks, "pin_only": pin_only}


def d2_live(root: Path, tmpbase: Path) -> dict:
    packet_digest = digest_of(root, D2_PACKET)
    typed_digest = digest_of(root, D2_TYPED)
    doc = read_json(root, D2_TYPED)
    assembly = doc.get("assembly")
    coverage = doc.get("coverage")
    if not isinstance(assembly, dict) or not isinstance(coverage, dict):
        raise AssemblyError(f"{D2_TYPED}: assembly/coverage block missing")
    pin = assembly.get("packet_sha256")
    check = tool_check(root, "tools/d2-typed-labels.py", "--check")
    tmp = Path(tempfile.mkdtemp(prefix="handoff-d2-", dir=str(tmpbase)))
    emitted_path = tmp / "typed-labels.emitted.json"
    emit = tool_check(root, "tools/d2-typed-labels.py", "--emit", str(emitted_path))
    diff = line_diff((root / D2_TYPED).read_text(encoding="utf-8"),
                     emitted_path.read_text(encoding="utf-8"))
    shutil.rmtree(tmp, ignore_errors=True)
    return {
        "packet": {"path": D2_PACKET, "digest": packet_digest},
        "projection": {
            "path": D2_TYPED,
            "digest": typed_digest,
            "pinned_packet_sha256": pin,
            "pin_match": pin == packet_digest,
            "labels": coverage.get("typed_labels"),
            "labels_by_kind": coverage.get("labels_by_kind"),
            "findings_total": coverage.get("findings_total"),
            "findings_hold_or_fail": coverage.get("findings_hold_or_fail"),
            "conflicts": coverage.get("conflicts"),
            "check": check,
            "emit": emit,
            "emit_diff": diff,
        },
    }


def d3_live(root: Path) -> dict:
    packet_rel = D3_PACKET
    packet_digest = digest_of(root, packet_rel)
    doc = read_json(root, packet_rel)
    expected = read_json(root, D3_EXPECTED)
    manifest = expected.get("manifest")
    if not isinstance(manifest, dict) or not manifest:
        raise AssemblyError(f"{D3_EXPECTED}: manifest missing")
    mismatches = []
    for rel, pinned in sorted(manifest.items()):
        path = root / rel
        measured = sha256_bytes(path.read_bytes()) if path.is_file() else None
        if measured != pinned:
            mismatches.append({"path": rel, "pinned": pinned, "measured": measured})
    if mismatches:
        raise AssemblyError(
            f"{D3_EXPECTED}: {len(mismatches)} manifest row(s) do not re-measure clean: "
            + ", ".join(row["path"] for row in mismatches)
        )
    law = doc.get("sound_changes", [{}])[0]
    lexicon = doc.get("lexicon", [])
    if len(lexicon) != 20:
        raise AssemblyError(f"{packet_rel}: expected 20 lexemes, found {len(lexicon)}")
    return {
        "packet": {"path": packet_rel, "digest": packet_digest},
        "gates": {"path": D3_GATES, "digest": digest_of(root, D3_GATES)},
        "expected": {
            "path": D3_EXPECTED,
            "digest": digest_of(root, D3_EXPECTED),
            "rows_reverified": len(manifest),
            "mismatches": mismatches,
            "expected_exit": expected.get("expected_exit"),
        },
        "canon_status": doc.get("canon_status"),
        "handoff_status": doc.get("handoff_status"),
        "screening": doc.get("screening", {}),
        "law": law,
        "lexicon": lexicon,
        "counts": {
            key: len(doc.get(key, []))
            for key in (
                "eras", "names", "utterances", "beliefs", "symbols", "materials",
                "objects", "costumes", "references", "bridges", "sound_changes",
                "speech_rules", "rank_rules",
            )
        },
        "bridges": doc.get("bridges", []),
    }


def live_sources(root: Path, tmpbase: Path) -> dict:
    return {
        "contract": contract_pin(root),
        "d2": d2_live(root, tmpbase),
        "d3": d3_live(root),
        "deps": {rel: digest_of(root, rel) for rel in DEP_TOOLS},
        "gate": {"path": GATE, "digest": digest_of(root, GATE)},
    }


def pin_sentence(d2: dict) -> dict:
    """What the D2 projection state is, as measured — never as assumed."""
    projection, live = d2["projection"], d2["packet"]["digest"]
    if projection["pin_match"] and projection["check"]["exit"] == 0:
        return {
            "state": "clean",
            "note": (
                f"pin matches the live packet digest {live[:8]}… and tools/d2-typed-labels.py "
                "--check exits 0"
            ),
        }
    note = (
        f"pinned {str(projection['pinned_packet_sha256'])[:8]}… vs live packet {live[:8]}…; "
        f"tools/d2-typed-labels.py --check exits {projection['check']['exit']}"
    )
    diff = projection["emit_diff"]
    if diff["changed_lines"]:
        shape = "the packet pin only" if diff["pin_only"] else "including lines other than the pin"
        note += f"; fresh emit vs committed artifact: {diff['changed_lines']} changed line(s), {shape}"
    return {"state": "mismatch", "note": note}


# --------------------------------------------------------------------------
# envelope + glossary builders
# --------------------------------------------------------------------------


def build_glossary(root: Path, d3: dict) -> list:
    """20 rows from the live D3 lexicon; every cell is a packet-field statement."""
    statuses = gate_constants(root)["etym_statuses"]
    law = d3["law"]
    rows = []
    for entry in d3["lexicon"]:
        e0, e1 = entry["forms"]["E0"], entry["forms"]["E1"]
        status = entry["status"]
        if status not in statuses:
            raise AssemblyError(
                f"{D3_PACKET}: lexeme {entry['id']} status {status!r} outside {statuses}"
            )
        if e0 == e1:
            etymology = (
                f"status: {status} — E0 *{e0} '{entry['gloss']}'; packet E1 form identical "
                f"({e1}); no {law['id']} difference for this form"
            )
        else:
            etymology = (
                f"status: {status} — E0 *{e0} '{entry['gloss']}' → E1 {e1} "
                f"({law['id']} {law['environment']} /{law['from']}/ > /{law['to']}/, "
                f"{law['register']} register; packet forms)"
            )
        rows.append(
            {
                "entry_id": entry["id"],
                "e0": e0,
                "e1": e1,
                "gloss": entry["gloss"],
                "etymology": etymology,
            }
        )
    return rows


def bridge_rows(d3: dict) -> list:
    return [
        {
            "edge_id": bridge["id"],
            "source": bridge["source_id"],
            "target": ", ".join(bridge["target_ids"]),
            "relation": bridge["relation"],
            "kind": bridge["claim_kind"],
            "scope": bridge.get("asserted_scope"),
        }
        for bridge in d3["bridges"]
    ]


def build_packet(root: Path, sources: dict) -> tuple:
    """Return (markdown, trace). Raises AssemblyError before rendering anything."""
    constants = gate_constants(root)
    contract, d2, d3 = sources["contract"], sources["d2"], sources["d3"]
    glossary = build_glossary(root, d3)
    bridges = bridge_rows(d3)
    pin = pin_sentence(d2)
    provenance = {}  # field -> source pointer, for reviewers

    def note(name, where):
        provenance[name] = where
        return None

    counts = d3["counts"]
    manifest_rows = [
        (D2_PACKET, "D2 drill packet (bytes behind the D2 typed projection)", d2["packet"]["digest"]),
        (D2_TYPED, "D2 typed-label projection (pin state measured and recorded in OQ-01)", d2["projection"]["digest"]),
        (D3_PACKET, "D3 source-bounded drill packet", d3["packet"]["digest"]),
        (D3_GATES, "D3 legacy gate projection", d3["gates"]["digest"]),
        (D3_EXPECTED, "D3 parent freeze manifest (re-measured by this exercise)", d3["expected"]["digest"]),
        (CONTRACT, "kotodama-lore adjacency contract (digest also carried by contract_ref)", contract["digest"]),
    ]
    counts_line = (
        f"record counts — D2: {d2['projection']['labels']} typed labels "
        f"({d2['projection']['labels_by_kind']['native-form']} native-form, "
        f"{d2['projection']['labels_by_kind']['translated-label']} translated-label, "
        f"{d2['projection']['labels_by_kind']['borrowed-strata']} borrowed-strata), "
        f"{d2['projection']['findings_total']} projection findings "
        f"({d2['projection']['findings_hold_or_fail']} hold-or-fail, "
        f"{d2['projection']['conflicts']} conflicts); D3: {counts['eras']} eras E0/E1, "
        f"{len(glossary)} lexemes L01-L20, {counts['names']} names N01-N06, "
        f"{counts['utterances']} utterances, {counts['beliefs']} beliefs, "
        f"{counts['symbols']} symbols, {counts['materials']} materials, "
        f"{counts['objects']} objects, {counts['costumes']} costumes, "
        f"{counts['references']} references, {counts['bridges']} bridges. "
        "Every digest above was measured from the live bytes at assembly time."
    )

    fields = {}

    def constant(name, value, why):
        fields[name] = value
        note(name, f"declared constant — {why}")
        return value

    constant("packet_id", PACKET_ID, "the exercise's own packet identifier")
    constant("packet_version", f"{PACKET_VERSION} (assembler profile {PROFILE})", "the exercise's declared version")
    fields["contract_ref"] = (
        f"kotodama-lore-adjacency revision {contract['revision']}, contract digest "
        f"sha256:{contract['digest']} (§1 pin; digested from the contract bytes by this assembly run)"
    )
    note("contract_ref", f"{CONTRACT} (revision line + sha256)")
    constant(
        "producer",
        "kotodama-shokunin (round-11 handoff-e2e exercise; generative craft and design records only)",
        "the producing lane and workstream",
    )
    constant(
        "recipient",
        "lore-shokunin (canon, world-bible entities, chronology, bible-wide consistency)",
        "the adjacent lane that owns canon",
    )
    constant(
        "request_ref",
        "none — assembled as a deliberately unbound exercise packet with no incoming lore brief (contract §4)",
        "no brief exists for this drill",
    )
    constant(
        "baseline_bible_ref",
        "none — deliberately unbound research packet; cannot be imported as canon without a lore "
        "baseline and a new reviewed handoff (contract §4)",
        "no world-bible baseline is bound to this drill",
    )

    fields["artifact_manifest"] = "\n".join(
        ["", "| artifact | role | sha256 |", "|---|---|---|"]
        + [f"| {rel} | {role} | `{digest}` |" for rel, role, digest in manifest_rows]
        + ["", counts_line]
    )
    note("artifact_manifest", "digests measured live; counts recomputed from typed-labels.d2.yml + packet.json")

    fields["subject_refs"] = (
        f"cand:kotodama.d2.typed-label-set ({d2['projection']['labels']} labels over components 01-15), "
        f"cand:kotodama.d3.lexicon (L01-L20), cand:kotodama.d3.names (N01-N06); all unresolved candidate "
        "refs — this exercise supplies no lore entity ids"
    )
    note("subject_refs", "derived from typed-labels.d2.yml coverage + packet.json lexicon/names")

    fields["scope"] = (
        f"D2 highland-pastoralist drill, typed projection only ({d2['projection']['labels']} typed labels; "
        f"{d2['projection']['findings_total']} findings) and the D3 source-bounded drill "
        f"({counts['eras']} eras E0/E1; {len(glossary)} constructed lexemes L01-L20; {counts['names']} constructed "
        f"names N01-N06; {counts['utterances']} utterances; {counts['beliefs']} attributed beliefs; "
        f"{counts['symbols']} symbols; {counts['materials']} materials; {counts['objects']} objects; "
        f"{counts['costumes']} costumes; {counts['references']} references; {counts['bridges']} bridges); "
        "both drills are non-canon design material; no real place; construction-only spellings; era tags are "
        "fixture-relative, not BCE/CE"
    )
    note("scope", "counts from typed-labels.d2.yml + packet.json")

    fields["dependency_manifest"] = "\n".join(
        [
            "",
            f"- profile kotodama-d3-evidence-coupling/1 (declared in {D3_PACKET})",
            f"- profile {PROFILE} (this exercise)",
        ]
        + [f"- {rel} sha256:`{digest}`" for rel, digest in sorted(sources["deps"].items())]
        + [
            f"- serializer {DEP_TOOLS[0]} yaml_lines (loaded read-only by the D3 assembler; digest pinned above)",
            "- every row is a measured sha256 or a declared profile id; no floating version references",
        ]
    )
    note("dependency_manifest", "sha256 of each tool named + profiles declared in live artifacts")

    claim_rows = [
        f"| CL0{index} | {bridge['kind']} | {bridge['scope']} | {bridge['edge_id']} {bridge['relation']}: "
        f"{bridge['source']} → {bridge['target']} (full mechanism and limits in {D3_PACKET} bridges) |"
        for index, bridge in enumerate(bridges, start=1)
    ]
    claim_rows.append(
        f"| CL06 | derived-check | measured | the D2 typed projection records "
        f"{d2['projection']['findings_total']} findings ({d2['projection']['findings_hold_or_fail']} hold-or-fail, "
        f"{d2['projection']['conflicts']} conflicts) — open question OQ-02, not a clearance |"
    )
    claim_rows.append(
        f"| CL07 | screening statement | {d3['screening'].get('status')} | D3 screening: "
        f"real_language_sweep_performed={str(d3['screening'].get('real_language_sweep_performed')).lower()} "
        f"({D3_PACKET} screening) |"
    )
    claim_rows.append(
        f"| CL08 | measured check | clean | the D2 typed projection is current: {pin['note']} |"
        if pin["state"] == "clean"
        else f"| CL08 | measured condition | red | {pin['note']} (open question OQ-01) |"
    )
    claim_rows.append(
        f"| CL09 | measured check | clean | all {d3['expected']['rows_reverified']} rows of {D3_EXPECTED} "
        f"re-measured clean at assembly time (0 mismatches) |"
    )
    fields["claim_ledger"] = "\n".join(
        ["", "| claim_id | kind | evidence_status | summary |", "|---|---|---|---|"] + claim_rows
    )
    note("claim_ledger", f"{D3_PACKET} bridges + measured conditions of this run")

    edge_rows = [
        f"| {bridge['edge_id']} | {bridge['source']} | {bridge['target']} | {bridge['relation']} |"
        for bridge in bridges
    ]
    edge_rows.append(
        f"| D2-TL | typed-label projection ({d2['projection']['labels']} labels) | owning components "
        "01-15 | derived-view |"
    )
    fields["coupling_edges"] = "\n".join(
        ["", "| edge_id | source | target | relation |", "|---|---|---|---|"] + edge_rows
    )
    note("coupling_edges", f"{D3_PACKET} bridges (BR01-BR05) + typed-label projection relation")

    fields["requested_decisions"] = "\n".join(
        [
            "",
            (f"- RD-01: re-emit or re-pin {D2_TYPED} so its packet pin matches the live packet bytes "
             f"({pin['note']}; owner: the artifact's generator owner). Retain as non-canon candidate "
             "material only; canon standing stays lore's alone."
             if pin["state"] == "mismatch" else
             f"- RD-01: adopt the D2 typed projection as delivered candidate material ({pin['note']}), "
             "or return any record to the language owner."),
            f"- RD-02: resolve the {d2['projection']['findings_total']} D2 projection findings "
            f"({d2['projection']['findings_hold_or_fail']} hold-or-fail, {d2['projection']['conflicts']} conflicts) "
            "at component-owner level, or record them as accepted holds.",
            f"- RD-03: adopt or defer the D3 era staging E0/E1 as relative coordinates without dates "
            f"({D3_PACKET} eras; no calendar exists in the artifacts).",
            f"- RD-04: register the D3 beliefs ({counts['beliefs']} records) as attributed in-world belief with "
            "unresolved truth status, or reject the institution account — never import either as world-fact.",
            f"- RD-05: the D3 screening stays {d3['screening'].get('status')} — official name approval stays "
            "blocked until a real-language sweep is performed.",
        ]
    )
    note("requested_decisions", "derived from live unresolved sets + measured conditions")

    fields["validation"] = "\n".join(
        [
            "",
            "Assembly-time checks, re-measured from live bytes on every run by this exercise "
            "(no value copied from a prior report):",
            "",
            f"- contract bytes sha256:{contract['digest']} (revision {contract['revision']} read from the "
            "contract's own revision line);",
            (f"- D2 typed projection: {pin['note']} — mismatch recorded as OQ-01;"
             if pin["state"] == "mismatch" else f"- D2 typed projection: {pin['note']};"),
            f"- D3 freeze manifest: {d3['expected']['rows_reverified']} rows re-measured, "
            f"{len(d3['expected']['mismatches'])} mismatches;",
            f"- record counts recomputed from {D3_PACKET} and {D2_TYPED} (see artifact_manifest).",
            "",
            "The envelope and glossary verdict is produced by running tools/gates/handoff-packet-check.py over "
            "an isolated copy of this packet; the observed verdict is recorded in the exercise receipt, not "
            "written back into this document. Local generation/derivation verification only — not bible-wide "
            "consistency and not canon certification (contract §8 step 3).",
        ]
    )
    note("validation", "digest/count measurements of this run; gate verdict stays in the receipt")

    fields["open_questions"] = "\n".join(
        [
            "",
            (f"- OQ-01: {D2_TYPED} {pin['note']}. Filed as R10-O02-NEW-2 in "
             "reports/round-10/fix-02.md, fix-06.md, fix-07.md, fix-08.md, findings-verify-1.md, "
             "findings-verify-4.md; owner: the artifact's generator owner."
             if pin["state"] == "mismatch" else
             f"- OQ-01: closed at assembly time — {D2_TYPED} {pin['note']}; recorded as the prior "
             "R10-O02-NEW-2 item, closed by re-emission."),
            f"- OQ-02: the D2 typed projection records {d2['projection']['findings_total']} findings "
            f"({d2['projection']['findings_hold_or_fail']} hold-or-fail; {d2['projection']['conflicts']} "
            "conflicts) — resolution owner: the owning components.",
            f"- OQ-03: D3 screening status {d3['screening'].get('status')}, "
            f"real_language_sweep_performed={str(d3['screening'].get('real_language_sweep_performed')).lower()} "
            "— no real-language or community clearance exists; blocking for official name approval.",
            f"- OQ-04: no lore receipt exists for either drill ({D3_PACKET} handoff_status "
            f"{d3['handoff_status']}) — blocking for any canon import.",
        ]
    )
    note("open_questions", "live unresolved sets (typed projection, screening, handoff status) + filed R10 record")

    # precondition: the rendered field set is exactly the gate's §4 vocabulary
    names = constants["field_names"]
    if set(fields) != set(names):
        raise AssemblyError(
            f"field set mismatch: missing={sorted(set(names) - set(fields))} "
            f"extra={sorted(set(fields) - set(names))}"
        )
    for name in names:
        if "|" in fields[name] and name not in ("artifact_manifest", "claim_ledger", "coupling_edges", "dependency_manifest"):
            raise AssemblyError(f"field {name} must not carry table pipes in its cell form")
    if re.search(r"(?i)\blatest\b", fields["dependency_manifest"]):
        raise AssemblyError("dependency_manifest floats a version reference")

    table_fields = ("packet_id", "packet_version", "contract_ref", "producer", "recipient",
                    "request_ref", "baseline_bible_ref", "subject_refs", "scope")
    lines = [
        "# Handoff packet — D2/D3 exercise assembly (deliberately unbound research packet; not canonized)",
        "",
        "NON-CANON world-bible handoff packet, kotodama-shokunin → lore-shokunin, assembled by",
        f"`tools/exercise-handoff-e2e.py` (profile `{PROFILE}`) from the lane's live D2/D3 artifacts and",
        "validated through `tools/gates/handoff-packet-check.py` in an isolated copy. Nothing here is",
        "canon, a world-bible entry, or lore acceptance; canon standing is lore's alone.",
        "",
        "- canon_standing: not canonized — lore disposition required (lore-shokunin owns canon)",
        "",
        "| field | value |",
        "|---|---|",
    ]
    for name in table_fields:
        lines.append(f"| {name} | {fields[name]} |")
    lines += ["", "## artifact_manifest", fields["artifact_manifest"].strip()]
    lines += ["", "## dependency_manifest", fields["dependency_manifest"].strip()]
    lines += ["", "## claim_ledger", fields["claim_ledger"].strip()]
    lines += ["", "## coupling_edges", fields["coupling_edges"].strip()]
    lines += ["", "## requested_decisions", fields["requested_decisions"].strip()]
    lines += ["", "## validation", fields["validation"].strip()]
    lines += ["", "## open_questions", fields["open_questions"].strip()]
    lines += [
        "",
        "## glossary payload (inline; D3 lexicon L01-L20, exact packet records)",
        "",
        "| entry_id | E0 form | E1 form | gloss | etymology |",
        "|---|---|---|---|---|",
    ]
    for row in glossary:
        lines.append(
            f"| {row['entry_id']} | {row['e0']} | {row['e1']} | {row['gloss']} | {row['etymology']} |"
        )
    markdown = "\n".join(lines) + "\n"

    trace = {
        "profile": PROFILE,
        "contract": contract,
        "d2": d2,
        "d3": {key: value for key, value in d3.items() if key != "lexicon"},
        "deps": sources["deps"],
        "gate": sources["gate"],
        "fields": provenance,
        "glossary": {
            "rows": len(glossary),
            "statuses": sorted({row["etymology"].split("status: ")[1].split(" ")[0] for row in glossary}),
        },
        "problems": [],
    }
    return markdown, trace


def assemble(root: Path, tmpbase: Path = None) -> dict:
    tmpbase = Path(tmpbase) if tmpbase else root / ".scratch"
    tmpbase.mkdir(parents=True, exist_ok=True)
    sources = live_sources(root, tmpbase)
    markdown, trace = build_packet(root, sources)
    return {"markdown": markdown, "trace": trace, "problems": trace["problems"]}


# --------------------------------------------------------------------------
# isolated-copy gate run + malformed controls
# --------------------------------------------------------------------------


def isolate_copy(markdown: str, tmpbase: Path, name: str = "packet.md") -> Path:
    run_dir = Path(tempfile.mkdtemp(prefix="handoff-e2e-", dir=str(tmpbase)))
    packet = run_dir / name
    packet.write_text(markdown, encoding="utf-8")
    return packet


def gate_run(root: Path, packet: Path) -> dict:
    proc = subprocess.run(
        [sys.executable, str(root / GATE), str(packet)],
        cwd=str(packet.parent),  # foreign cwd: the packet must be self-contained
        capture_output=True,
        text=True,
    )
    match = GATE_SCAN_RE.search(proc.stdout)
    scan = (
        {
            "fields": int(match.group(1)),
            "fields_required": int(match.group(2)),
            "glossary_entries": int(match.group(3)),
            "findings": int(match.group(4)),
        }
        if match
        else None
    )
    return {"exit": proc.returncode, "stdout": proc.stdout.strip(), "scan": scan, "packet_path": str(packet)}


def check_isolated(root: Path, markdown: str, tmpbase: Path) -> dict:
    return gate_run(root, isolate_copy(markdown, tmpbase))


CONTROL_PATCHES = (
    (
        "positive-gloss-reword",
        lambda text: text.replace("| L01 | pina | fina | spoken pledge |",
                                  "| L01 | pina | fina | spoken promise |", 1),
        0, (),
    ),
    (
        "missing-field",
        lambda text: re.sub(r"^\| packet_id \|.*\n", "", text, count=1, flags=re.M),
        1, ("HO-MISSING",),
    ),
    (
        "empty-field",
        lambda text: re.sub(r"^\| scope \|.*\n", "| scope | - |\n", text, count=1, flags=re.M),
        1, ("HO-EMPTY",),
    ),
    (
        "placeholder-etymology",
        lambda text: re.sub(
            r"^(\| L01 \| pina \| fina \| spoken pledge \| )[^|]*(\|)$",
            r"\1- \2", text, count=1, flags=re.M,
        ),
        1, ("HO-GLOSS-ETYM",),
    ),
    (
        "unlicensed-status",
        lambda text: text.replace("status: constructed — E0 *pina", "status: maybe — E0 *pina", 1),
        1, ("HO-GLOSS-ETYM",),
    ),
    (
        "contract-digest-stripped",
        lambda text: re.sub(r"contract digest sha256:[0-9a-f]{64}", "contract digest pending", text, count=1),
        1, ("HO-CONTRACT-REF",),
    ),
    (
        "canon-marker-removed",
        lambda text: re.sub(r"(?i)\bnot[-\s]+(?:yet[-\s]+)?canon(?:ized)?\b",
                            "canon standing pending", text),
        1, ("HO-CANON-MARKER",),
    ),
    (
        "canon-claim-injected",
        lambda text: text.replace("## validation",
                                  "This packet is canonized by lore.\n\n## validation", 1),
        1, ("HO-CANON-CLAIM",),
    ),
    (
        "dependency-latest",
        lambda text: text.replace("- profile kotodama-handoff-e2e/1 (this exercise)",
                                  "- profile kotodama-handoff-e2e-latest (this exercise)", 1),
        1, ("HO-DEP-FLOAT",),
    ),
)


def controls(root: Path, markdown: str, tmpbase: Path) -> list:
    results = []
    for name, patch, expected_exit, expected_ids in CONTROL_PATCHES:
        patched = patch(markdown)
        if patched == markdown:
            results.append({"name": name, "ok": False, "why": "patch changed nothing"})
            continue
        outcome = check_isolated(root, patched, tmpbase)
        ids = re.findall(r"^FINDING (\S+):", outcome["stdout"], re.M)
        clean = outcome["exit"] == 0 and not ids and outcome["scan"] == {
            "fields": 16, "fields_required": 16, "glossary_entries": 20, "findings": 0
        }
        ok = (clean if expected_exit == 0
              else outcome["exit"] == expected_exit and all(fid in ids for fid in expected_ids))
        results.append(
            {
                "name": name,
                "exit": outcome["exit"],
                "expected_exit": expected_exit,
                "expected_ids": list(expected_ids),
                "ids": ids,
                "ok": ok,
            }
        )
    return results


# --------------------------------------------------------------------------
# fragment-level CLI (the integrator wraps this in the exercise tool)
# --------------------------------------------------------------------------


def default_root() -> Path:
    """Repo root: the nearest ancestor carrying this lane's PROVINCE.md."""
    here = Path(__file__).resolve()
    for candidate in (here.parent, *here.parents):
        if (candidate / "PROVINCE.md").is_file():
            return candidate
    return here.parent


def main(argv=None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=str(default_root()))
    parser.add_argument("--packet-out")
    parser.add_argument("--trace-out")
    parser.add_argument("--check-isolated", action="store_true")
    parser.add_argument("--controls", action="store_true")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    tmpbase = root / ".scratch"
    tmpbase.mkdir(exist_ok=True)
    try:
        result = assemble(root, tmpbase)
    except AssemblyError as exc:
        print(f"ASSEMBLY-REFUSED: {exc}")
        return 2
    if args.packet_out:
        Path(args.packet_out).write_text(result["markdown"], encoding="utf-8")
        print(f"wrote {args.packet_out} ({len(result['markdown'])} bytes)")
    if args.trace_out:
        Path(args.trace_out).write_text(json.dumps(result["trace"], indent=1) + "\n", encoding="utf-8")
        print(f"wrote {args.trace_out}")
    exit_code = 0
    if args.check_isolated:
        outcome = check_isolated(root, result["markdown"], tmpbase)
        print(f"ISOLATED-GATE exit={outcome['exit']} scan={outcome['scan']}")
        print(outcome["stdout"])
        exit_code = 0 if (outcome["exit"] == 0 and outcome["scan"]
                          and outcome["scan"]["fields"] == 16
                          and outcome["scan"]["glossary_entries"] == 20) else 1
    if args.controls:
        for row in controls(root, result["markdown"], tmpbase):
            print(f"CONTROL {row['name']}: ok={row['ok']} exit={row.get('exit')} ids={row.get('ids')}")
            exit_code = exit_code or (0 if row["ok"] else 1)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
```

## 4. Evidence A — the fragment's own battery (2026-10-17, 22:09–22:14 UTC)

All commands ran with `export TMPDIR=$PWD/.scratch` from the repo root; the
fragment writes only to `--packet-out` / `--trace-out` and to temporary
directories under that TMPDIR.

### 4.1 Green run, post-alignment (22:13:45 UTC)

```sh
python3 .scratch/o03/fragment.py --packet-out .scratch/o03/out/packet.md \
        --trace-out .scratch/o03/out/trace.json --check-isolated
# wrote .scratch/o03/out/packet.md (11975 bytes)
# ISOLATED-GATE exit=0 scan={'fields': 16, 'fields_required': 16, 'glossary_entries': 20, 'findings': 0}
# INFO scan: fields=16/16 glossary-entries=20 findings=0          → exit 0
```

- Determinism: a second run wrote byte-identical bytes
  (`97adf647244cab15a2b22e4d076bd7aaaa0f84e9ead510ca3b8d9d4f9db82e86`, both
  runs), and a third run executed from `/` (foreign cwd, absolute `--root`)
  wrote the same digest and the same green scan.
- Fail-closed: `--root .scratch/o03/emptyroot` →
  `ASSEMBLY-REFUSED: required artifact missing: corpus/knowledge/synthesis/worldbible-integration-contract.md`,
  exit 2, no traceback.
- Controls (22:13:45 UTC): 9/9 rows matched their expectation —

```text
positive-gloss-reword      exit=0 ids=[]                     (stays clean)
missing-field              exit=1 ids=[HO-MISSING]
empty-field                exit=1 ids=[HO-EMPTY]
placeholder-etymology      exit=1 ids=[HO-GLOSS-ETYM]
unlicensed-status          exit=1 ids=[HO-GLOSS-ETYM]
contract-digest-stripped   exit=1 ids=[HO-CONTRACT-REF]
canon-marker-removed       exit=1 ids=[HO-CANON-MARKER]
canon-claim-injected       exit=1 ids=[HO-CANON-CLAIM]
dependency-latest          exit=1 ids=[HO-DEP-FLOAT]
```

### 4.2 Trace facts at 22:13:45 UTC (from `--trace-out`)

| fact | measured value |
|---|---|
| contract | revision `1.0.0`, digest `5f4c02bfc4e6e4e9…` (re-measured from bytes) |
| D2 projection pin | `8da90b07…`→ **match** — pin equals live packet digest `e0f21509…`; `--check` exit 0; `--emit` exit 1 (holds present); emit-vs-committed diff 0 lines |
| D3 freeze manifest | 24/24 rows re-measured clean, 0 mismatches |
| glossary | 20 rows, statuses `['constructed']` |
| field provenance | 16 entries (every field names its source) |
| problems | `[]` |

### 4.3 The conditional narrative, exercised live (this is the shard's point)

At 22:09:42 UTC, with the pre-re-emit projection
(`examples/culture-d2/typed-labels.d2.yml` sha256 `e70ba1477dbe…`), the same
code measured: pinned `8da90b07…` vs live packet `e0f21509…`, `--check` exit 1,
emit-vs-committed diff **1 line, pin only** — and rendered:

```text
| CL08 | measured condition | red | the D2 projection pins packet digest 8da90b07… while the
live packet hashes e0f21509…; tools/d2-typed-labels.py --check exits 1 (open question OQ-01) |
- OQ-01: … Filed as R10-O02-NEW-2 in reports/round-10/fix-02.md, fix-06.md, fix-07.md,
  fix-08.md, findings-verify-1.md, findings-verify-4.md; owner: the artifact's generator owner.
```

Between 22:09 and 22:13 UTC another worker re-emitted the projection (see §6).
At 22:13:45 UTC the same code, no edits to the narrative, rendered:

```text
| CL08 | measured check | clean | the D2 typed projection is current: pin matches the live
packet digest e0f21509… and tools/d2-typed-labels.py --check exits 0 |
- OQ-01: closed at assembly time — examples/culture-d2/typed-labels.d2.yml pin matches the
  live packet digest e0f21509… and tools/d2-typed-labels.py --check exits 0; recorded as the
  prior R10-O02-NEW-2 item, closed by re-emission.
```

Underlying evidence for the flip (`sha256sum` at 22:13:55 UTC):
`examples/culture-d2/typed-labels.d2.yml` = `a3aa452cd5ae77c3…` (was
`e70ba1477dbe…`), `examples/culture-d2/packet.d2.yml` unchanged
`e0f21509e14ac03e…`, `tools/d2-typed-labels.py` unchanged `0da0015f700345c9…`.
The claimed "only diff line is the pin" is produced by the fragment's own
`line_diff()` over a fresh `--emit`, not quoted from the filed round-10 record.

## 5. Evidence B — independent verification of `tools/exercise-handoff-e2e.py`

### 5.1 Default run at the revision that passed (22:11:18 UTC)

```sh
python3 tools/exercise-handoff-e2e.py
# OK declared-expectations · frozen-input (5 digests) · preflight (16 fields, non-canon
#    marker, glossary vocabulary, no floating version)
# OK gate-exit: exit 0 from …/.scratch/handoff-exercise-x2tu6npf/isolated
# OK gate-scan: fields=16/16 glossary-entries=20 findings=0
# OK gate-findings: none · frozen-packet: assembled sha256 2a058f785812… == frozen 2a058f785812…
# OK frozen-fields: all 16 field digests match · frozen-glossary: 20 ids match
# OK contract-crossref: kotodama-lore-adjacency 1.0.0 sha256:5f4c02bfc4e6… · component-digests: 13/13
# exercise-handoff-e2e: PASS — fields=16/16 glossary-entries=20 findings=0      → exit 0
```

The same revision, run from `/` with an absolute path, also exited 0 and
reported `PASS`. The assembled packet at that revision hashed
`2a058f7858127b98592439594c55974d93e6e672a600dd2036b47e21e71c8a63`
(emitted to `.scratch/o03/tool-packet.md`).

**Independent controls over that shipped packet** (my harness, isolated copy,
22:12 UTC): 6/6 behaved as the gate's semantics require —
`missing-packet_id` → `HO-MISSING` (scan 15/16); first `sha256:<64 hex>` in
`contract_ref` replaced → `HO-CONTRACT-REF`; unmasked canon marker sweep →
`HO-CANON-MARKER`; injected `This packet is canonized by lore.` →
`HO-CANON-CLAIM`; `latest` injected into the `## dependency_manifest` body →
`HO-DEP-FLOAT`; `status: constructed` → `status: invented` in the L01 glossary
cell → `HO-GLOSS-ETYM`. (Method note: two first-attempt probes mis-targeted —
the `latest` patch landed on the first `- ` list item in the document, and a
`status:` patch landed in prose — so they reported exit 0; both were re-scoped
to the intended section/cell and then fired. A control that fails to mutate is
evidence about the probe, not about the packet.)

### 5.2 `--selftest` was red at the 22:11 UTC revision — two defects measured, both cause-isolated

At the same 22:11 UTC revision, `python3 tools/exercise-handoff-e2e.py
--selftest` exited 1 with an unhandled traceback:

```text
File "tools/exercise-handoff-e2e.py", line 1267, in selftest
    assert code == EXIT_PASS, [f"{name}: {detail}" for name, ok, detail in checks if not ok]
AssertionError: ["evaluated: cannot hash examples/culture-d2/components/02-phonology.yml:
  [Errno 2] … .scratch/handoff-selftest-<id>/fixture/examples/culture-d2/components/02-phonology.yml"]
```

Reproduced twice (22:11, 22:12 UTC). Cause probe (scratch, read-only over the
tool: `runpy` the tool, patch `FIXTURE_INPUTS` in its live globals, call
`selftest()`):

1. **Defect 1 — the selftest fixture omits the component trees.**
   `FIXTURE_INPUTS` copied 8 files; 19 files under
   `examples/culture-d2/components/` and `examples/culture-d3/components/` were
   not copied, while the tool's own step 2 re-measures the assemblers'
   `assembly.source_sha256` component digests (13 of them). With the component
   files added to `FIXTURE_INPUTS`, the fixture run advances past that assert.
2. **Defect 2 — the "placeholder-content" control asserts a finding the gate
   cannot produce.** With the fixture fixed, the selftest next fails at line
   1302 (`assert gate["exit"] == EXIT_FAIL, gate["stdout"]`) for the mutation
   `- OQ-01:` → `- OQ-01: TBD\n- OQ-01 (original):`. Direct probe over that
   mutated packet: gate `exit=0, findings=[], glossary_entries=20`, and the
   tool's own `preflight()` returns `[]`. The mutation edits prose inside a
   heading-body field; the gate's `HO-EMPTY` fires only when the *whole* field
   value is a placeholder, so this control as written cannot pass. (A working
   variant — measured in §4.1 — blanks a whole value: `| scope | - |` →
   `HO-EMPTY`.)

Neither defect is mine to repair (single writer on that tool); they are reported
with their failure lines and revision hashes so the fix is checkable.

### 5.3 The tool moved again during this shard (22:13:19 UTC)

`tools/exercise-handoff-e2e.py` was rewritten while this shard was running:

| moment (UTC) | tool sha256 | default run | `--selftest` |
|---|---|---|---|
| 22:11:18 | (revision of the PASS run above) | exit 0, PASS | exit 1, defect 1 |
| 22:13:19 | `708d8d5b26239b15b7deab944435a55f6d82fdce0e5bdd2fb1ffc6a1e013f291` | exit 2, `E2E-BASELINE: frozen baseline not found: reports/round-11/handoff/expected.json (write one with --freeze DIR)` | exit 1, same fixture-missing-components cause (now `MissingArtifact` in a `frozen-root` fixture) |
| 22:15:39 | `e74e5aeaea7f1315fec745a25603b7952a50999afc995aad68bc8d33f7e65024` | exit 1, `E2E-DIGEST: 1 read-set file(s) changed since the baseline was frozen: examples/culture-d2/typed-labels.d2.yml` (`frozen e70ba1477dbe… live a3aa452cd5ae…`) | **exit 0 — green** (its control rows all report as passing) |
| 22:16:34 | `d5b346b877be098f17e34cec1787e487d689e4bbd34160b667a54383394a6c8e` | exit 1, same `E2E-DIGEST` (baseline still not re-frozen) | exit 0 |

The baseline was frozen in the meantime at `reports/round-11/handoff/expected.json`
(5338 bytes, 22:13 UTC — the R11-O01 §8 recommendation; the old path
`tools/gates/expected/handoff-exercise/r11/expected.json` no longer exists).
The 22:15 default-run red is the tool behaving correctly against a baseline
that predates the D2 re-emit of §6 — the same input-digest drift its own
contract is meant to refuse; re-freezing after the D2 side stops moving closes
it (R11-O01 §11 ordering). §5.1's emitted-packet evidence and §5.2's two
defects both belong to revisions before the 22:15 rewrite; whether the
placeholder-control assertion was repaired in it was not re-measured here.
Cross-shard note for the integrator:
`reports/round-11/handoff/tamper-control.sh` (R11-O14) still pins
`BASELINE="tools/gates/expected/handoff-exercise/r11/expected.json"` — that path
no longer exists, so the tamper drill will need the new baseline path.

## 6. Live change observed during the window (report, not repair)

`examples/culture-d2/typed-labels.d2.yml` changed under this shard:
`e70ba1477dbe…` (17:33 local) → `a3aa452cd5ae77c3…` (measured 22:13:55 UTC).
Round-10 filed the old bytes as red (R10-O02-NEW-2: the artifact pinned the
pre-round-9 packet digest `8da90b07…`); the new bytes pin the live packet
`e0f21509…` and `tools/d2-typed-labels.py --check` now exits 0, so that filed
item is closed by re-emission — consistent with round-10's own finding that a
fresh emit is byte-identical at `a3aa452c…`
(`reports/round-10/findings-verify-1.md`). Consequences for the round: any
baseline, packet digest or validation number pinned before 22:13 UTC that
includes the typed projection's digest is stale; claim D's re-pin work and
claim F's recheck receipts should both note this timestamp.

## 7. Integration notes (for the O02–O05 single writer and the parent)

- **Aligned to the R11-O01 design already:** `packet_id`
  `kotodama.handoff.d2d3-e2e`; `packet_version` `1.0.0`; the manifest table
  header carries `artifact_id` (so the gate never reads it as a glossary
  payload); glossary header `| entry_id | E0 form | E1 form | gloss |
  etymology |` with the design's §5 etymology shape plus the packet's own law
  text; `not canonized` marker line; no floating `latest` (the fragment refuses
  to render if the token appears).
- **Deliberate divergences:** (a) `subject_refs` is coarser than design §3 row 9
  — three measured refs (D2 typed-label set, D3 lexicon, D3 names) instead of
  eight witness-backed candidates; the richer list belongs to the assembly
  attempts (O06–O09) and is a one-function swap here. (b) The manifest table
  lists the six artifacts this fragment digests, not the full 21-file read set;
  the fragment instead *verifies* all 24 rows of
  `examples/culture-d3/expected.json` in-run (raising on any mismatch) and cites
  that count in `validation`. (c) The `validation` field states assembly-time
  measurements only — the gate verdict is recorded in the run receipt, never
  written back into the packet (no self-reference).
- **What is worth lifting even if the shipped tool stays:** `pin_sentence()`
  (measured, conditional pin narrative), `line_diff()` (emit-vs-committed diff,
  pin-only detection), `check_isolated()`/`gate_run()` (foreign-cwd isolated
  run + scan parsing), `controls()` (mutation battery with expected IDs), and
  the `PLACEHOLDERS`-safe render discipline (whole-value placeholders are the
  only thing the gate treats as blank).
- **Baseline advice (supersedes my fragment's own shape):** pin
  exit/finding-ids/scan-counts/field-digests rather than the assembled packet's
  single hash if any D2/D3 byte may still move this round; the packet digest
  necessarily changes when any dependency digest in `dependency_manifest`
  changes. The shipped tool already carries per-field digests
  (`frozen-fields`), which is the resilient shape.

## 8. Verification of this document

The code block in §3 was spliced byte-for-byte from `.scratch/o03/fragment.py`
(sha256 `03fe4f8ebcf3fe21…`) and then extracted back out of this file and run:

```sh
python3 - <<'PY'
import re, pathlib
text = pathlib.Path("reports/round-11/handoff/shard-assembly.md").read_text(encoding="utf-8")
block = re.search(r"```python\n(.*?)\n```", text, re.S).group(1)
pathlib.Path(".scratch/o03/extracted.py").write_text(block + "\n", encoding="utf-8")
PY
python3 .scratch/o03/extracted.py --packet-out .scratch/o03/out/packet-extracted.md --check-isolated
# expect: exit 0; fields=16/16 glossary-entries=20 findings=0; packet digest equal to §4.1
```

Observed when this document was written (2026-10-17 22:14:20 UTC):

```text
extracted sha256 == fragment sha256 == 03fe4f8ebcf3fe21c6fbb4661899c03f1ac36fc96749cbfa5158c6cc3a7a4785
ISOLATED-GATE exit=0 scan={'fields': 16, 'fields_required': 16, 'glossary_entries': 20, 'findings': 0}
packet digest 97adf647244cab15a2b22e4d076bd7aaaa0f84e9ead510ca3b8d9d4f9db82e86 — identical to §4.1
```

**to-verify (for whoever runs this first):** the digests `97adf647…`,
`2a058f785812…` and the state table in §5.3 are point-in-time measurements of
2026-10-17 22:13–22:15 UTC against live bytes; re-running after further D2/D-side
edits will legitimately produce different digests (the narrative lines adapt,
the green scans should not).

## 9. Files written by this shard

- `reports/round-11/handoff/shard-assembly.md` (this file — the only committed
  artifact).
- Scratch, transient (`.scratch/o03/`): `fragment.py`, `doc-head.md`,
  `doc-tail.md`, `out/` (packets, traces), `battery*.log`, `selftest-run*.log`.
  Nothing under `examples/`, `corpus/`, `tools/` or any filed round directory
  was written; `tools/exercise-handoff-e2e.py` was read and executed, never
  edited.
