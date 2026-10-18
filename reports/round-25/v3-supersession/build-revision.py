#!/usr/bin/env python3
"""Round-25 O seat — build the `declared-in-r4` revision of the v3 handoff packet.

The round-23 revision `reports/round-23/wording/declared-in-r3/packet.md` is a
wording-only supersession of `reports/round-22/handoff/declared-in-r2/packet.md`.
It still carries the pre-family-clean D4 claim prose: D4-CL05/06/07/09 and the
OQ-V3-05 passenger line describe 15 holds / 1 note, three D2L-RANK holds, 13
unresolved rank items, 3 quarantine handles and 4 conflicts as D4's present
state. The round-22 family-clean repair (`reports/round-22/bleed/design.md`,
`impl.md`) removed those D2 residuals from D4 ownership; the live bytes now read
12 holds / 0 notes / 0 fails with zero D2L-RANK rows
(`examples/culture-d4/expected-holds.json`, `typed-labels.d4.yml`).

This builder is the declared-delta constructor: it derives the revision from the
r3 parent by exactly five line substitutions plus one provenance note inserted
before the first `- canon_standing:` anchor. No other byte differs. It refuses to
run if any declared old line does not occur exactly once, so the delta can never
silently drift.

    python3 reports/round-25/v3-supersession/build-revision.py            # build
    python3 reports/round-25/v3-supersession/build-revision.py --check    # verify bytes
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[3]
PARENT = "reports/round-23/wording/declared-in-r3/packet.md"
PARENT_SHA256 = "084dc5db9a8d923bb06a987b0b437bf5bfee3caac2e41cd16743da0c71499250"
REVISION_DIR = "reports/round-25/v3-supersession/declared-in-r4"
REVISION_PACKET = f"{REVISION_DIR}/packet.md"
ANCHOR = b"\n- canon_standing:"

NOTE = (
    "Revision declared-in-r4 (2026-10-18; round-25 O seat, claims R25-O11..O15) is a "
    "validator-facing claim-prose supersession of "
    "`reports/round-23/wording/declared-in-r3/packet.md` (packet_version 3.1.1, sha256 "
    "084dc5db9a8d923bb06a987b0b437bf5bfee3caac2e41cd16743da0c71499250): exactly five "
    "ledger lines are corrected to the family-clean present state measured on the live "
    "bytes — D4-CL05, D4-CL06, D4-CL07 and D4-CL09, plus the OQ-V3-05 passenger line. "
    "The round-22 family-clean D4 repair (reports/round-22/bleed/design.md, impl.md) "
    "removed three inherited D2 rank holds and one D2 rank note from D4 ownership "
    "without resolving them in D2; the pre-repair prose still reported 15 holds / 1 "
    "note / 3 D2L-RANK holds / 13 unresolved rank items / 3 quarantine handles / 4 "
    "conflicts as D4's own present state, while the delivered bytes now carry 12 holds, "
    "0 notes and 0 fails with zero D2L-RANK rows (examples/culture-d4/expected-holds.json "
    "hold 12 / note 0 / fail 0; examples/culture-d4/typed-labels.d4.yml coverage "
    "findings_total 12, conflicts 0, rank_rules_unresolved_items 0, "
    "rank_quarantine_handles 0). No claim status, row id, link, count, edge, glossary "
    "row or other ledger line is touched: the census stays 27 rows with statuses "
    "16 supported / 7 partial / 4 unresolved, the fifteen carried v2 rows are "
    "byte-identical to the v2 source, and the frozen validators stay byte-identical "
    "because this file is a claim-prose revision, not a renderer build. The "
    "packet_version field stays 3.1.1 for the same reason. The parent packet and every "
    "earlier filed packet remain filed and untouched; this revision's identity is its "
    "SHA-256, pinned in reports/round-25/v3-supersession/declared-in-r4/expected.json "
    "and re-verified byte-for-byte by "
    "reports/round-25/v3-supersession/v3-supersession-check.py. NON-CANON engineering "
    "evidence; canon standing is lore-shokunin's alone (contract §6, §8.7)."
).encode()

# (row, old line, new line) — each old line must occur exactly once in the parent.
DELTA = (
    (
        "D4-CL05",
        "| D4-CL05 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/typed-labels.d4.yml#coverage (typed_labels 74, labels_by_kind native-form 56 / translated-label 12 / borrowed-strata 6, findings_total 16, findings_hold_or_fail 15, label_findings_fail 0) and examples/culture-d4/typed-labels.d4.yml#stats (fail 0, hold 12, labels 74), re-read from the delivered bytes; the projection is the projector's own output and the check leg reports byte-identical determinism | examples/culture-d4/typed-labels.d4.yml#coverage; examples/culture-d4/typed-labels.d4.yml#labels_by_kind; examples/culture-d4/typed-labels.d4.yml#stats; examples/culture-d4/typed-labels.d4.yml#typed_labels; tools/gates/d4-typed-labels-check-gate.py | The D4 typed channel types 74 labels — 56 native-form, 12 translated-label, 6 borrowed-strata — and carries 16 findings of which 15 are hold-or-fail (12 label holds, 0 label fails); the committed projection is the projector's own deterministic output, and its check leg reports byte-identity rather than a re-derivation. |",
        "| D4-CL05 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/typed-labels.d4.yml#coverage (typed_labels 74, labels_by_kind native-form 56 / translated-label 12 / borrowed-strata 6, findings_total 12, findings_hold_or_fail 12, label_findings_hold 12, label_findings_fail 0, conflicts 0) and examples/culture-d4/typed-labels.d4.yml#typed_labels (stats fail 0, hold 12, labels 74), re-read from the delivered bytes; the projection is the projector's own output and the check leg reports byte-identical determinism | examples/culture-d4/typed-labels.d4.yml#coverage; examples/culture-d4/typed-labels.d4.yml#labels_by_kind; examples/culture-d4/typed-labels.d4.yml#stats; examples/culture-d4/typed-labels.d4.yml#typed_labels; tools/gates/d4-typed-labels-check-gate.py | The D4 typed channel types 74 labels — 56 native-form, 12 translated-label, 6 borrowed-strata — and carries 12 findings, all of them the twelve owed garment/slot form holds (12 label holds, 0 label fails, 0 conflicts); the committed projection is the projector's own deterministic output, and its check leg reports byte-identity rather than a re-derivation. |",
    ),
    (
        "D4-CL06",
        "| D4-CL06 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/expected-holds.json#counts (hold 15, note 1, fail 0) with the row list, whose holds are twelve D2L-FORM-UNRESOLVED rows keyed to each garment twice and three D2L-RANK rows, plus one D2L-RANK note for the band-keyed pair; the emitted set equals the committed file and reports/round-18/d4/holds.md reconciles the brief's six-row declaration with a documented +9 hold delta rather than absorbing it | examples/culture-d4/expected-holds.json#counts; examples/culture-d4/expected-holds.json#holds; examples/culture-d4/components/01-brief.yml#hold_set_declaration; reports/round-18/d4/holds.md | The committed D4 hold set is 15 holds, 1 note and 0 fails, pinned to the delivered bytes: twelve `D2L-FORM-UNRESOLVED` holds keyed to each garment twice (record id and slot id) and three `D2L-RANK` holds, plus one `D2L-RANK` note for the band-keyed pair; the emitted set equals the committed file, and the round-17 brief's six-row declaration is reconciled by a documented +9 hold / +1 note delta rather than absorbed or silently re-declared. |",
        "| D4-CL06 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/expected-holds.json#counts (hold 12, note 0, fail 0) with the row list, whose twelve holds are all D2L-FORM-UNRESOLVED rows keyed to each garment twice (record id and slot id) and whose D2L-RANK population is zero; the emitted set equals the committed file, and the round-18 +9 hold / +1 note delta stands as that historical generation's reconciliation (reports/round-18/d4/holds.md), superseded for D4 ownership by the round-22 family-clean repair recorded in examples/culture-d4/expected-holds.json#revision_note | examples/culture-d4/expected-holds.json#counts; examples/culture-d4/expected-holds.json#holds; examples/culture-d4/expected-holds.json#revision_note; examples/culture-d4/components/01-brief.yml#hold_set_declaration; reports/round-18/d4/holds.md | The committed D4 hold set is 12 holds, 0 notes and 0 fails, pinned to the delivered bytes: twelve `D2L-FORM-UNRESOLVED` holds keyed to each garment twice (record id and slot id), and zero `D2L-RANK` rows of either severity; the emitted set equals the committed file, the round-17 brief's six unresolved garment form slots are met by those twelve keyed holds (+6 holds / 0 notes against the declaration), and the round-18 +9 hold / +1 note delta remains the historical generation's reconciliation rather than a present D4 expectation. |",
    ),
    (
        "D4-CL07",
        "| D4-CL07 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation, six records GAR-01..GAR-06 each carrying an era block tagged E0 or E1 and a material block resolved by slot identity to a CMAT record, summary claims 6 findings 0; the same file's examples/culture-d4/typed-labels.d4.yml#reconciliation_records and examples/culture-d4/typed-labels.d4.yml#conflicts counts carry four conflicts without collapsing them | examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation; examples/culture-d4/typed-labels.d4.yml#R-MAT-RESOLVED; examples/culture-d4/typed-labels.d4.yml#reconciliation_records; examples/culture-d4/typed-labels.d4.yml#conflicts; examples/culture-d4/packet.d4.yml#materials | The D4 projection's era and material reconciliation resolves all six garment records by declared row and slot identity — each record's era block tagged in scope, each material block resolved to a `CMAT` record — with zero findings, while the reconciliation's own conflicts (4), quarantine handles (3) and reconciliation records (6) are carried as counts rather than collapsed into a cleaner ledger. |",
        "| D4-CL07 | designer interpretation | derived projection (author-side) | supported | grounding: examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation, six records GAR-01..GAR-06 each carrying an era block tagged E0 or E1 and a material block resolved by slot identity to a CMAT record, summary claims 6 findings 0; the same file's examples/culture-d4/typed-labels.d4.yml#reconciliation_records, examples/culture-d4/typed-labels.d4.yml#conflicts and examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles counts carry six reconciliation records with zero conflicts and zero quarantine handles | examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation; examples/culture-d4/typed-labels.d4.yml#R-MAT-RESOLVED; examples/culture-d4/typed-labels.d4.yml#reconciliation_records; examples/culture-d4/typed-labels.d4.yml#conflicts; examples/culture-d4/packet.d4.yml#materials | The D4 projection's era and material reconciliation resolves all six garment records by declared row and slot identity — each record's era block tagged in scope, each material block resolved to a `CMAT` record — with zero findings, and its own ledger carries six reconciliation records with zero conflicts and zero quarantine handles rather than a residual pool folded into a cleaner ledger. |",
    ),
    (
        "D4-CL09",
        "| D4-CL09 | designer interpretation | derived projection (author-side), holds open | unresolved | grounding: examples/culture-d4/typed-labels.d4.yml#rank_rules, whose act rows carry adapt_status cannot-evaluate because speech is not a gate-modelled channel, with examples/culture-d4/typed-labels.d4.yml#rank_rules_unresolved_items 13 and examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles 3 and examples/culture-d4/typed-labels.d4.yml#conflicts 4 in the same file's coverage block; open: the thirteen unresolved rank items, three quarantine handles and four conflicts are inherited D2 normalization residuals and none of them is promoted by this packet; owner: kotodama, blocking for the affected D2 rank records, not for this envelope | examples/culture-d4/typed-labels.d4.yml#rank_rules; examples/culture-d4/typed-labels.d4.yml#rank_rules_unresolved_items; examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles; examples/culture-d4/typed-labels.d4.yml#conflicts | The D4 projection re-carries D2's rank-rule adaptation rows with `adapt_status: cannot-evaluate` — speech is not a gate-modelled channel — and the packet's coverage block holds 13 unresolved rank items, 3 quarantine handles and 4 conflicts; none of them is promoted, resolved or hidden by this packet, and they are inherited D2 normalization residuals rather than D4 design debt. |",
        "| D4-CL09 | designer interpretation | derived projection (author-side), holds open | unresolved | grounding: examples/culture-d4/typed-labels.d4.yml#rank_rules, whose coverage block carries four packet-native RK rules preserved once each in the normalized and gate-projected views (rank_rules_component 4, rank_rules_normalized 4, rank_rules_gate_projected 4), with zero act rules, zero residuals, zero unresolved rank items, zero quarantine handles and zero conflicts, plus one declared skip of the D2 prose-rank adapter and residual tables; open: the thirteen unresolved rank items, three quarantine handles and four conflicts the pre-family-clean generation inherited are no longer D4-owned and were not resolved in D2, where they stay open (OQ-V2-03); owner: kotodama, blocking for the affected D2 rank records, not for this envelope | examples/culture-d4/typed-labels.d4.yml#rank_rules; examples/culture-d4/typed-labels.d4.yml#rank_rules_unresolved_items; examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles; examples/culture-d4/typed-labels.d4.yml#conflicts | The D4 rank view is packet-native and carries zero unresolved rank items, zero quarantine handles and zero conflicts: four RK rules are preserved once each in the normalized and gate-projected views, the D2 prose-rank adapter and residual tables are declared skipped rather than evaluated, and the thirteen unresolved rank items, three quarantine handles and four conflicts the pre-family-clean generation inherited stay open in D2 (OQ-V2-03) instead of being re-carried or promoted here. |",
    ),
    (
        "OQ-V3-05",
        "- OQ-V3-05: D4's inherited and own holds stay open: twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts — kotodama; blocking for the affected D2 rank records and the six garment terms, not for this envelope (unresolved claims: D4-CL09)",
        "- OQ-V3-05: D4's own holds stay open: twelve form holds, zero rank holds, zero notes and zero fails; the thirteen unresolved rank items, three quarantine handles and four conflicts recorded by the pre-family-clean generation are D2-owned residuals, removed from D4 ownership by the round-22 family-clean repair and still open in D2 (OQ-V2-03) — kotodama; blocking for the six owed D4 garment terms and the affected D2 rank records, not for this envelope (unresolved claims: D4-CL09)",
    ),
)


def sha256_of(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def build(root):
    parent_path = Path(root) / PARENT
    parent = parent_path.read_bytes()
    digest = hashlib.sha256(parent).hexdigest()
    if digest != PARENT_SHA256:
        raise SystemExit(f"{PARENT}: digest {digest} != declared parent {PARENT_SHA256}")
    revision = parent
    for row, old, new in DELTA:
        old_b, new_b = old.encode(), new.encode()
        if revision.count(old_b) != 1:
            raise SystemExit(f"{row}: declared old line occurs {revision.count(old_b)} times")
        if old_b not in parent:
            raise SystemExit(f"{row}: declared old line is not in the parent")
        revision = revision.replace(old_b, new_b, 1)
    if revision.count(ANCHOR) < 1:
        raise SystemExit("parent carries no canon_standing anchor")
    index = revision.index(ANCHOR)
    revision = revision[:index] + b"\n" + NOTE + revision[index:]
    return revision


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true",
                        help="verify the filed revision equals the declared delta")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    revision = build(root)
    target = root / REVISION_PACKET
    if args.check:
        if not target.is_file():
            raise SystemExit(f"{REVISION_PACKET}: missing")
        live = target.read_bytes()
        print(f"declared-delta rebuild: {'EQUAL' if live == revision else 'DIFFERENT'}")
        print(f"revision sha256: {hashlib.sha256(live).hexdigest()}")
        print(f"rebuilt  sha256: {hashlib.sha256(revision).hexdigest()}")
        print(f"bytes: filed {len(live)} / rebuilt {len(revision)}")
        return 0 if live == revision else 1
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(revision)
    print(f"wrote {REVISION_PACKET}")
    print(f"revision sha256: {hashlib.sha256(revision).hexdigest()}")
    print(f"bytes: parent {len(Path(root / PARENT).read_bytes())} / revision {len(revision)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
