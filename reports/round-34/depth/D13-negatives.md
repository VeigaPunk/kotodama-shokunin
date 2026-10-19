- Seat: D13 | executor | claim D | date 2026-10-19 | baseline da68a6d

# D13 — negative controls for claim D

Mission: (a) a deliberately stale figure in a draft packet is caught by the
audit method; (b) the OLD pair still gates green, and name the
semantic-stale class the method catches that the gate cannot.

Verdict: both controls pass. The gate returns a **byte-identical verdict on
all six control drafts** while the audit separates them exactly, and the
filed r30/`declared-in-r6` pair is green on every leg of the v3 chain
(gate 16/16, e2e exit 0, links 105/105) while carrying **17 stale figures**.

## 1. Control (b) — the OLD pair still gates green, three ways

Method = the audit legs defined in §4, run over a verbatim copy of the
filed bytes at `.scratch/D13/base.md` (bytes 105,584; sha256
`6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` — equal
to the filed packet per `sha256sum` and to `freeze.txt`'s `packet_sha256`).

```
$ python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md
INFO scan: fields=16/16 glossary-entries=20 findings=0          # exit 0

$ python3 tools/exercise-handoff-e2e.py --profile v3 --quiet    # exit 0
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb

$ python3 tools/harness/packet_links.py --repo-root "$PWD" --links <the 38 D4-row anchors>
links=38 resolved=38 findings=0                                  # exit 0
```

The e2e run's `packet_sha256` equals `freeze.txt`'s pinned value, so the run
judged the filed bytes and nothing else. Every leg is green over a ledger
whose figures are 17× stale: the run is a **shape** result, not a content
result.

### The stale set (leg 1 over `base.md`, exit 1)

`AUDIT scan: value-rows=24 ok=7 stale=17 anchors=38 without-position=1
not-evaluated=24`

| row | field | packet | live | source |
|---|---|---|---|---|
| D4-CL05 | coverage.typed_labels | 74 | 82 | typed-labels.d4.yml |
| D4-CL05 | coverage.labels_by_kind.native-form | 56 | 64 | typed-labels.d4.yml |
| D4-CL05 | coverage.findings_total | 16 | 12 | typed-labels.d4.yml |
| D4-CL05 | coverage.findings_hold_or_fail | 15 | 12 | typed-labels.d4.yml |
| D4-CL05 | typed_labels.stats.labels | 74 | 82 | typed-labels.d4.yml |
| D4-CL06 | counts.hold | 15 | 12 | expected-holds.json |
| D4-CL06 | counts.note | 1 | 0 | expected-holds.json |
| D4-CL07 | coverage.conflicts | 4 | 0 | typed-labels.d4.yml |
| D4-CL07 | coverage.rank_quarantine_handles | 3 | 0 | typed-labels.d4.yml |
| D4-CL09 | coverage.rank_rules_unresolved_items | 13 | 0 | typed-labels.d4.yml |
| D4-CL09 | coverage.rank_quarantine_handles | 3 | 0 | typed-labels.d4.yml |
| D4-CL09 | coverage.conflicts | 4 | 0 | typed-labels.d4.yml |
| OQ-V3-05 | counts.rank_holds (D2L-RANK) | 3 | 0 | expected-holds.json |
| OQ-V3-05 | counts.note | 1 | 0 | expected-holds.json |
| OQ-V3-05 | coverage.rank_rules_unresolved_items | 13 | 0 | typed-labels.d4.yml |
| OQ-V3-05 | coverage.rank_quarantine_handles | 3 | 0 | typed-labels.d4.yml |
| OQ-V3-05 | coverage.conflicts | 4 | 0 | typed-labels.d4.yml |

The 7 OK rows are the control against over-flagging:
`translated-label 12`, `borrowed-strata 6`, `label_findings_fail 0`,
`stats.fail 0`, `stats.hold 12`, `counts.fail 0`,
`reconciliation_records 6` all match live and are **not** reported.

Live values read at HEAD (`git rev-parse HEAD` = da68a6d):
`examples/culture-d4/typed-labels.d4.yml` coverage — `conflicts 0` (:30),
`findings_hold_or_fail 12` (:31), `findings_total 12` (:32),
`label_findings_fail 0` (:33), `label_findings_hold 12` (:34),
`labels_by_kind` borrowed-strata 6 / native-form 64 / translated-label 12
(:36-38), `rank_quarantine_handles 0` (:40),
`rank_rules_unresolved_items 0` (:44), `reconciliation_records 6` (:45),
`typed_labels 82` (:46), nested `typed_labels.stats = {fail 0, hold 12,
labels 82}` (:2865); `examples/culture-d4/expected-holds.json#counts =
{hold 12, note 0, fail 0}` with all 12 holds carrying
`id: D2L-FORM-UNRESOLVED` and zero `D2L-RANK` rows.

## 2. The class the gate cannot see: **carried-forward ledger figures**

The gate judges the packet *document* and opens exactly one file — its
argument (`tools/gates/handoff-packet-check.py:881`). Its only
digest-shaped check is a *presence* test
(`tools/gates/handoff-packet-check.py:537-545`: `if not
DIGEST_RE.search(manifest["value"])`), and the file computes no hash at all
(`grep -n "hashlib\|sha256"` matches only fixture literals at :625-636,
:759, :785). So no figure in a claim cell, and no digest, is ever compared
with the bytes it names.

The v3 chain does not close that gap either. `v3_manifest_rows`
(`tools/exercise-handoff-e2e.py:2476`) re-derives manifest rows and their
digests from live bytes **at build time**, and the link/uncertainty legs
judge the tool's own freshly built twin
(`tools/exercise-handoff-e2e.py:3738`), so both are green by construction.
The ledger *numbers*, however, are not derived at all: the twelve D4 claim
rows are parsed from the **filed round-20** claims map
(`tools/exercise-handoff-e2e.py:184` `CLAIMS_MAP =
reports/round-20/handoff/claims-map.md`; `:2286-2320`
`v3_parse_claims_map`) and carried verbatim into the v3 ledger
(`:2599-2604` `v3_build_claim_rows`, "the 15 v2 rows carried verbatim + the
12 D4 rows").

That is the class — and its provenance is checkable: `reports/round-20/
handoff/claims-map.md:99` states "The D4 typed channel types 74 labels — 56
native-form, 12 …", and 74/56/16 were the live D4 values at the round-20
commit (`git show 35b6797:examples/culture-d4/typed-labels.d4.yml` → typed
82→74, native-form 56, findings_total 16; `git show
35b6797:examples/culture-d4/expected-holds.json` → counts 15/1/0). By the
round-30 commit (`git show 11df1fd:…typed-labels.d4.yml` → 82/64/12;
expected-holds 12/0/0) the source had been regenerated, but the packet
frozen that same round still carried the round-20 figures.

Three sub-classes follow, all invisible to the gate:

1. **Carried-forward figure** — true at the cited source's earlier
   generation, false at HEAD. Only value equality finds these (the 17 rows
   above). Nothing structural distinguishes them.
2. **Self-contradiction inside one document** — the packet's manifest row
   `A-30` (`packet.md:68`) states "82 labels (64 native-form / 12
   translated-label / 6 borrowed-strata), 12 findings" with the live digest
   `c23b0ab5…`, while its own ledger row (`packet.md:148`) states 74/56/16/15
   in the same file. A document-level consistency check would catch this;
   the gate does not attempt one.
3. **Anchor naming no document position** — `examples/culture-d4/
   typed-labels.d4.yml#R-MAT-RESOLVED` is cited by `packet.md:150`, but in
   the live bytes that token is never a key: it appears only as a string
   value (`"code": "R-MAT-RESOLVED"`, :58, :70, :82, :94, :106, :118). The
   filed resolver still says `ok`:

   ```
   $ python3 tools/harness/packet_links.py --repo-root "$PWD" \
       --links 'examples/culture-d4/typed-labels.d4.yml#R-MAT-RESOLVED'
   links=1 resolved=1 findings=0
   ```

   Because `_text_contains` (`tools/harness/packet_links.py:155-166`)
   applies the JSON key/string walk only when `path.suffix == ".json"`
   (:159) and otherwise falls through to a bare word-boundary regex
   (:164-166). For the D4 `.yml` sources, "names a key" and "names a
   string value" are the same verdict. Same for `#stats`, which moved from
   top level to the nested `typed_labels.stats` (:2865).

So the named class is: **carried-forward ledger figures — claim-row numbers
copied from an earlier filed generation whose cited source has since been
regenerated — plus their anchor shadows; no leg of the v3 chain compares a
claim figure, or a packet-declared digest, with live bytes.**

## 3. Control (a) — a deliberately stale figure in a draft is caught

Discrimination matrix, six drafts built from the filed bytes (recipes in
§4); gate and audit run over each (`--root` = repo root, HEAD da68a6d):

| draft (`.scratch/D13/`) | what changed vs the filed packet | gate | audit |
|---|---|---|---|
| `base.md` | nothing (verbatim copy) | exit 0, 16/16, findings=0 | **exit 1** — 17 stale, 1 anchor without position |
| `live.md` | all 17 figures rewritten live | exit 0, 16/16, findings=0 | exit 1 — 0 stale, 1 anchor without position |
| `live-pos.md` | `live.md` + the positionless anchor re-pointed | exit 0, 16/16, findings=0 | **exit 0** — 0 stale, 0 without position |
| `tampered.md` | `live-pos.md` + one figure flipped back (cell only) | exit 0, 16/16, findings=0 | **exit 1** — exactly 1 stale |
| `tampered-coherent.md` | `live-pos.md` + one figure flipped in cell **and** prose | exit 0, 16/16, findings=0 | **exit 1** — exactly 1 stale |
| `digestmut.md` | `live-pos.md` + one hex char of the two pinned `c23b0ab5…` digests | exit 0, 16/16, findings=0 | exit 0 — 0 stale |

Draft sha256: `base` 6ced88ad…f0bb, `live` ff738d04…2ca0, `live-pos`
0d116ddf…61f1, `tampered` 68aaae19…aaffa, `tampered-coherent` fc94f3c8…4f4e,
`digestmut` 3eae1acc…17de.

The tamper is exactly the D4-CL05 grounding cell flipping 82 → 74
(`typed_labels 82, labels_by_kind native-form 64` →
`typed_labels 74, labels_by_kind native-form 64`), and the tampered draft's verdict is:

```
$ python3 .scratch/D13/claim_number_audit.py .scratch/D13/tampered.md --root .
AUDIT D4-CL05 coverage.typed_labels packet=74 live=82 STALE [examples/culture-d4/typed-labels.d4.yml#coverage.typed_labels]
AUDIT scan: value-rows=24 ok=23 stale=1 anchors=37 without-position=0 not-evaluated=24
```

`tampered.md` is the r6 packet's own disease reproduced deliberately, and
the audit isolates it to exactly one row — the 23 untouched rows stay OK, so
the detection is not a blanket failure. `tampered-coherent.md` matters
because its cell and its prose agree (both 74): there is no
self-contradiction for a reviewer to notice, yet the audit still flags it
against live bytes — which is precisely what the gate cannot do.

`digestmut.md` is the honest boundary note: neither the gate nor the audit
re-measures a digest **as declared in the packet document**, so a corrupted
pin is invisible to both (the `digestmut` audit is green because its figures
are). Any claim-D receipt should not represent the digest pin as
independently re-measured at packet level.

### The two legs disagree on what a valid anchor is

My first re-point attempt used the literal dotted path, and the filed
resolver rejects it — dotted selectors are only walked for `.json`
(`tools/harness/packet_links.py:143-153` `_json_contains`,
`:77-95` `_json_path_get`):

```
$ python3 tools/harness/packet_links.py --repo-root "$PWD" \
    --links 'examples/culture-d4/typed-labels.d4.yml#typed_labels.stats,examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation.records'
L-TOKEN-MISSING [examples/culture-d4/typed-labels.d4.yml#typed_labels.stats] token 'typed_labels.stats' not found in examples/culture-d4/typed-labels.d4.yml
L-TOKEN-MISSING [examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation.records] token 'era_material_reconciliation.records' not found in examples/culture-d4/typed-labels.d4.yml
links=2 resolved=0 findings=2
```

So a landable re-point must be a **bare token that occurs in the bytes**
*and* names the block the figure comes from. Both probes that satisfy both
legs are confirmed:

```
$ ... --links 'examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation'   → resolved=1 findings=0
$ ... --links 'examples/culture-d4/typed-labels.d4.yml#typed_labels'                  → resolved=1 findings=0
```

`live-pos.md` uses those two tokens and is green on both legs
(links=37 resolved=37 findings=0 on its 37 unique D4 anchors).

## 4. The instrument and the control recipes (DRAFT — integrator lands)

Nothing in this fragment edits a shared file. If the lane wants the audit
durable, the integrator creates `tools/harness/claim_number_audit.py` from
the source below (mirrors the round-25 audit-tool shape: stdlib only,
read-only, deterministic, exit 0/1/2). The runner path is scratch-only, so
the source is carried here.

Reported table = the two legs over the D4 claim rows. Leg 1 reads each figure
from the packet cell and compares it with the live value by key path; leg 2
classifies every cited `path#token` as `KEY-TL` / `KEY-PATH` / `NESTED-KEY`
/ `VALUE-ONLY` / `MISSING`, with `VALUE-ONLY` and `MISSING` failing the run
and real-YAML sources the stdlib cannot parse recorded as
`NOT-EVALUATED-YAML` (counted apart, never as a pass — 24 such anchors here,
all `examples/culture-d4/packet.d4.yml` and one `components/01-brief.yml`).

```python
#!/usr/bin/env python3
"""claim-number audit — the semantic-staleness control for handoff packets.

Where `tools/gates/handoff-packet-check.py` judges the packet *document*
(field presence, digest shape, glossary etymology status) and
`tools/harness/packet_links.py` judges that each cited `path#token` *matches
bytes somewhere* in the cited file, this instrument judges the third thing
neither does: does the figure the claim row states **equal the value the
cited source holds now**.

Two legs per run:

  leg 1 value equality — for each assertion row, read the number out of the
    packet's claim cell and compare it with the live value read from the
    cited source by key path;
  leg 2 anchor class — every `path#token` cited by a D4 claim row is
    classified against the live bytes: `KEY-TL` (names a top-level key),
    `KEY-PATH` (a dotted path that resolves), `NESTED-KEY` (a key, but not
    top-level — the citation's positional assumption moved), `VALUE-ONLY`
    (appears only inside a string value, never as a key) or `MISSING`.
    Only `VALUE-ONLY` and `MISSING` fail the run: those tokens name no
    document position at all, while `tools/harness/packet_links.py:155-166`
    resolves `.yml` tokens by bare word-boundary regex over the raw text,
    so neither it nor the gate can tell `VALUE-ONLY` from `KEY-TL`.

Exit 0 when every value row is OK and no anchor is VALUE-ONLY/MISSING;
1 when any row is STALE or any anchor is VALUE-ONLY/MISSING; 2 on IO errors.

Usage: claim_number_audit.py <packet.md> [--root REPO] [--json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROW_RE = re.compile(r"^(\| D4-CL\d\d \||- OQ-V3-\d\d:)")
ANCHOR_RE = re.compile(r"([A-Za-z0-9_./-]+\.(?:yml|json))#([A-Za-z0-9_.-]+)")
NUM_WORDS = {
    "no": 0, "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20,
}

# (row_id, field, packet regex, source path, live key path[, capture group])
ROWS = (
    ("D4-CL05", "coverage.typed_labels", r"typed_labels (\d+)",
     "examples/culture-d4/typed-labels.d4.yml", "coverage.typed_labels"),
    ("D4-CL05", "coverage.labels_by_kind.native-form",
     r"native-form (\d+)", "examples/culture-d4/typed-labels.d4.yml",
     "coverage.labels_by_kind.native-form"),
    ("D4-CL05", "coverage.labels_by_kind.translated-label",
     r"translated-label (\d+)", "examples/culture-d4/typed-labels.d4.yml",
     "coverage.labels_by_kind.translated-label"),
    ("D4-CL05", "coverage.labels_by_kind.borrowed-strata",
     r"borrowed-strata (\d+)", "examples/culture-d4/typed-labels.d4.yml",
     "coverage.labels_by_kind.borrowed-strata"),
    ("D4-CL05", "coverage.findings_total", r"findings_total (\d+)",
     "examples/culture-d4/typed-labels.d4.yml", "coverage.findings_total"),
    ("D4-CL05", "coverage.findings_hold_or_fail",
     r"findings_hold_or_fail (\d+)", "examples/culture-d4/typed-labels.d4.yml",
     "coverage.findings_hold_or_fail"),
    ("D4-CL05", "coverage.label_findings_fail",
     r"label_findings_fail (\d+)", "examples/culture-d4/typed-labels.d4.yml",
     "coverage.label_findings_fail"),
    ("D4-CL05", "stats.fail", r"\(fail (\d+), hold (\d+), labels (\d+)\)",
     "examples/culture-d4/typed-labels.d4.yml", "typed_labels.stats.fail", 1),
    ("D4-CL05", "stats.hold", r"\(fail (\d+), hold (\d+), labels (\d+)\)",
     "examples/culture-d4/typed-labels.d4.yml", "typed_labels.stats.hold", 2),
    ("D4-CL05", "stats.labels", r"\(fail (\d+), hold (\d+), labels (\d+)\)",
     "examples/culture-d4/typed-labels.d4.yml", "typed_labels.stats.labels", 3),
    ("D4-CL06", "counts.hold", r"#counts \(hold (\d+), note (\d+), fail (\d+)\)",
     "examples/culture-d4/expected-holds.json", "counts.hold", 1),
    ("D4-CL06", "counts.note", r"#counts \(hold (\d+), note (\d+), fail (\d+)\)",
     "examples/culture-d4/expected-holds.json", "counts.note", 2),
    ("D4-CL06", "counts.fail", r"#counts \(hold (\d+), note (\d+), fail (\d+)\)",
     "examples/culture-d4/expected-holds.json", "counts.fail", 3),
    ("D4-CL07", "coverage.conflicts", r"conflicts \((\d+)\)",
     "examples/culture-d4/typed-labels.d4.yml", "coverage.conflicts"),
    ("D4-CL07", "coverage.rank_quarantine_handles",
     r"quarantine handles \((\d+)\)", "examples/culture-d4/typed-labels.d4.yml",
     "coverage.rank_quarantine_handles"),
    ("D4-CL07", "coverage.reconciliation_records",
     r"reconciliation records \((\d+)\)", "examples/culture-d4/typed-labels.d4.yml",
     "coverage.reconciliation_records"),
    ("D4-CL09", "coverage.rank_rules_unresolved_items",
     r"rank_rules_unresolved_items (\d+)", "examples/culture-d4/typed-labels.d4.yml",
     "coverage.rank_rules_unresolved_items"),
    ("D4-CL09", "coverage.rank_quarantine_handles",
     r"rank_quarantine_handles (\d+)", "examples/culture-d4/typed-labels.d4.yml",
     "coverage.rank_quarantine_handles"),
    ("D4-CL09", "coverage.conflicts", r"conflicts (\d+)",
     "examples/culture-d4/typed-labels.d4.yml", "coverage.conflicts"),
    ("OQ-V3-05", "counts.rank_holds", r"(\w+) rank holds",
     "examples/culture-d4/expected-holds.json", "holds_by_id.D2L-RANK", 1),
    ("OQ-V3-05", "counts.note", r"rank holds \+ (\w+) note",
     "examples/culture-d4/expected-holds.json", "counts.note", 1),
    ("OQ-V3-05", "coverage.rank_rules_unresolved_items",
     r"(\w+) unresolved rank items", "examples/culture-d4/typed-labels.d4.yml",
     "coverage.rank_rules_unresolved_items", 1),
    ("OQ-V3-05", "coverage.rank_quarantine_handles",
     r"(\w+) quarantine handles", "examples/culture-d4/typed-labels.d4.yml",
     "coverage.rank_quarantine_handles", 1),
    ("OQ-V3-05", "coverage.conflicts", r"and (\w+) conflicts",
     "examples/culture-d4/typed-labels.d4.yml", "coverage.conflicts", 1),
)


def load_json(root, rel):
    return json.loads((Path(root) / rel).read_text(encoding="utf-8"))


def _keys_at_depth(node, depth=0, out=None):
    out = {} if out is None else out
    if isinstance(node, dict):
        for key, value in node.items():
            out.setdefault(key, depth)
            _keys_at_depth(value, depth + 1, out)
    elif isinstance(node, list):
        for value in node:
            _keys_at_depth(value, depth + 1, out)
    return out


def resolve(obj, key_path):
    if key_path.startswith("holds_by_id."):
        wanted = key_path.split(".", 1)[1]
        return sum(1 for h in obj["holds"] if h.get("id") == wanted)
    node = obj
    for part in key_path.split("."):
        node = node[part]
    return node


def classify(obj, raw, token):
    if "." in token:
        try:
            resolve(obj, token)
            return "KEY-PATH"
        except (KeyError, TypeError):
            pass
    keys = _keys_at_depth(obj)
    if token in keys:
        return "KEY-TL" if keys[token] == 0 else "NESTED-KEY"
    if re.search(r"(?<![A-Za-z0-9_-])" + re.escape(token) + r"(?![A-Za-z0-9_-])", raw):
        return "VALUE-ONLY"
    return "MISSING"


def as_int(token):
    return int(token) if token.isdigit() else NUM_WORDS.get(token.lower())


def row_lines(text):
    out = {}
    for line in text.splitlines():
        if ROW_RE.match(line):
            key = re.match(r"^(?:\| (D4-CL\d\d) \||- (OQ-V3-\d\d):)", line)
            out.setdefault(key.group(1) or key.group(2), []).append(line)
    return out


def audit(root, packet_path):
    text = Path(packet_path).read_text(encoding="utf-8")
    lines = row_lines(text)
    records, stale, anchors_bad = [], 0, 0
    caches, raws = {}, {}
    for row in ROWS:
        claim, field, pattern, source, key_path = row[:5]
        group = row[5] if len(row) > 5 else 1
        if source not in caches:
            caches[source] = load_json(root, source)
            raws[source] = (Path(root) / source).read_text(encoding="utf-8")
        hits = [h for h in (re.search(pattern, line) for line in lines.get(claim, [])) if h]
        if not hits:
            records.append({"row": claim, "field": field, "verdict": "CELL-ABSENT",
                            "packet": None, "live": None, "source": source,
                            "key_path": key_path})
            stale += 1
            continue
        packet_value = as_int(hits[0].group(group))
        live_value = resolve(caches[source], key_path)
        verdict = "OK" if packet_value == live_value else "STALE"
        if verdict == "STALE":
            stale += 1
        records.append({"row": claim, "field": field, "verdict": verdict,
                        "packet": packet_value, "live": live_value,
                        "source": source, "key_path": key_path})
    seen = set()
    for line in text.splitlines():
        if not ROW_RE.match(line):
            continue
        for match in ANCHOR_RE.finditer(line):
            spec = match.group(1) + "#" + match.group(2)
            if spec in seen:
                continue
            seen.add(spec)
            source, token = match.group(1), match.group(2)
            if source not in caches and (Path(root) / source).suffix == ".json":
                caches[source] = load_json(root, source)
            if source not in raws:
                raws[source] = (Path(root) / source).read_text(encoding="utf-8")
            if source in caches:
                verdict = classify(caches[source], raws[source], token)
            else:
                # real YAML the stdlib cannot parse: leg 2 is recorded as
                # not-evaluated for this source rather than guessed — the
                # count is printed apart and never counted as a pass.
                verdict = "NOT-EVALUATED-YAML"
            if verdict in ("VALUE-ONLY", "MISSING"):
                anchors_bad += 1
            records.append({"row": line[:12], "field": "anchor:" + token,
                            "verdict": verdict, "packet": None, "live": None,
                            "source": spec, "key_path": token})
    return records, stale, anchors_bad


def main(argv=None):
    parser = argparse.ArgumentParser(description="claim-number audit")
    parser.add_argument("packet")
    parser.add_argument("--root", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    records, stale, anchors_bad = audit(args.root, args.packet)
    rows = [r for r in records if not r["field"].startswith("anchor:")]
    anchors = [r for r in records if r["field"].startswith("anchor:")]
    unevaluated = [r for r in anchors if r["verdict"] == "NOT-EVALUATED-YAML"]
    if args.json:
        print(json.dumps({"records": records, "stale": stale,
                          "anchors_without_position": anchors_bad,
                          "anchors_not_evaluated": len(unevaluated)},
                         indent=1, sort_keys=True))
    else:
        for rec in records:
            if rec["field"].startswith("anchor:"):
                print(f"AUDIT anchor {rec['source']} {rec['verdict']}")
            elif rec["verdict"] == "OK":
                print(f"AUDIT {rec['row']} {rec['field']} packet={rec['packet']} "
                      f"live={rec['live']} OK")
            else:
                print(f"AUDIT {rec['row']} {rec['field']} packet={rec['packet']} "
                      f"live={rec['live']} {rec['verdict']} "
                      f"[{rec['source']}#{rec['key_path']}]")
        ok = sum(1 for r in rows if r["verdict"] == "OK")
        print(f"AUDIT scan: value-rows={len(rows)} ok={ok} stale={len(rows) - ok} "
              f"anchors={len(anchors)} without-position={anchors_bad} "
              f"not-evaluated={len(unevaluated)}")
    return 1 if (stale or anchors_bad) else 0


if __name__ == "__main__":
    sys.exit(main())
```

Selftest shape the integrator should add before landing: (positive) `base.md`
→ exit 1 with `stale=17`; (negative, no false positive) `live-pos.md` →
exit 0; (negative, no blanket failure) `tampered.md` → exit 1 with
`stale=1` and 23 OK rows. All three are reproducible from §4's recipes.

### Control recipes (reproducible from the filed bytes)

`base.md` = byte copy of `reports/round-30/handoff/declared-in-r6/packet.md`.
`live.md` = `base.md` with each of these 14 pairs applied exactly once
(each asserted `count == 1`):

1. `(typed_labels 74, labels_by_kind native-form 56 / translated-label 12 / borrowed-strata 6, findings_total 16, findings_hold_or_fail 15, label_findings_fail 0)` → `(typed_labels 82, labels_by_kind native-form 64 / … findings_total 12, findings_hold_or_fail 12, label_findings_fail 0)`
2. `typed-labels.d4.yml#stats (fail 0, hold 12, labels 74)` → `typed-labels.d4.yml#typed_labels (fail 0, hold 12, labels 82)`
3. `The D4 typed channel types 74 labels — 56 native-form, 12 translated-label, 6 borrowed-strata — and carries 16 findings of which 15 are hold-or-fail` → `… types 82 labels — 64 native-form, … carries 12 findings of which 12 are hold-or-fail`
4. `expected-holds.json#counts (hold 15, note 1, fail 0)` → `(hold 12, note 0, fail 0)`
5. `The committed D4 hold set is 15 holds, 1 note and 0 fails` → `… 12 holds, 0 notes and 0 fails`
6. `twelve D2L-FORM-UNRESOLVED holds … and three D2L-RANK holds, plus one D2L-RANK note for the band-keyed pair` → `… , with no D2L-RANK holds or notes`
7. `the reconciliation's own conflicts (4), quarantine handles (3) and reconciliation records (6)` → `conflicts (0), quarantine handles (0) and reconciliation records (6)`
8. `counts carry four conflicts without collapsing them` → `counts carry zero conflicts …`
9. `rank_rules_unresolved_items 13` → `rank_rules_unresolved_items 0`
10. `rank_quarantine_handles 3` → `rank_quarantine_handles 0`
11. `typed-labels.d4.yml#conflicts 4 in the same file's coverage block` → `#conflicts 0 …`
12. `open: the thirteen unresolved rank items, three quarantine handles and four conflicts are inherited` → `open: zero unresolved rank items, zero quarantine handles and zero conflicts are inherited`
13. `coverage block holds 13 unresolved rank items, 3 quarantine handles and 4 conflicts` → `… 0 … 0 … 0 …`
14. `twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts` → `twelve form holds + no rank holds + no note, zero unresolved rank items, zero quarantine handles and zero conflicts`

`live-pos.md` = `live.md` with `typed-labels.d4.yml#R-MAT-RESOLVED` →
`typed-labels.d4.yml#era_material_reconciliation` (once).
`tampered.md` = `live-pos.md` with `(typed_labels 82, labels_by_kind
native-form 64` → `(typed_labels 74, labels_by_kind native-form 64` (once).
`tampered-coherent.md` = `live-pos.md` with that pair **plus** `The D4 typed
channel types 82 labels` → `The D4 typed channel types 74 labels`.
`digestmut.md` = `live-pos.md` with the two occurrences of
`c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e` → `…f82f`.

The generator that applies them is `.scratch/D13/build_controls.py` (scratch
only; the pairs above are the whole recipe, so the drafts can be rebuilt
after scratch cleanup).

## 5. Findings the D block should carry forward

- **D03/D04 anchor constraint (binding on the rewrite).** A re-pointed D4
  anchor must be a bare token present in the `.yml` bytes *and* meaningful:
  `#typed_labels` and `#era_material_reconciliation` satisfy both legs; the
  dotted forms `#typed_labels.stats` / `#era_material_reconciliation.records`
  satisfy the audit but **fail** the filed link leg (`L-TOKEN-MISSING`).
  Whatever D05 lands must be re-run through `packet_links.py` — a draft that
  is value-correct but dotted-anchored is not landable.
- **`#stats` is a positional shift, not just a value error.** The r20 file
  had `stats` at top level; live it is nested at `typed_labels.stats`
  (`examples/culture-d4/typed-labels.d4.yml:2865`). The r6 row's citation
  therefore resolves by word match while naming a different position than
  the row's sibling citations imply.
- **Only 17 of the 24 audited figures are stale — the rewrite must not be
  wider than the finding.** `D4-CL05`'s `translated-label 12`,
  `borrowed-strata 6`, `label_findings_fail 0`, `stats.fail 0`,
  `stats.hold 12`, `D4-CL06`'s `fail 0` and `D4-CL07`'s
  `reconciliation_records 6` already equal live and stay untouched; a
  blanket renumber would introduce *new* staleness.
- **No leg re-measures the packet's own declared digests.** `digestmut.md`
  proof above. If claim D's receipt says "freeze.txt pins packet_sha256",
  that is a claim about the *build output*, not about any check of the
  packet's manifest column.
- **The staleness is D4-specific, and the same packet shows it.** This
  packet's own D2 row says its source was "coverage block re-read live
  2026-10-18 by JSON read — typed_labels 58 (native-form 46, translated-label
  10, borrowed-strata 2)" (`packet.md:129`), and its D2 facts block carries
  "58 typed labels (46 native-form / 10 translated-label / 2
  borrowed-strata), 16 findings (15 hold-or-fail), 13 unresolved rank items,
  3 quarantine handles, 4 conflicts, 10 reconciliation records"
  (`packet.md:284`). Every one of those figures is **live-accurate** against
  `examples/culture-d2/typed-labels.d2.yml` coverage (typed_labels 58,
  findings_total 16, findings_hold_or_fail 15, labels_by_kind native-form 46
  / translated-label 10 / borrowed-strata 2, conflicts 4,
  rank_rules_unresolved_items 13, rank_quarantine_handles 3,
  reconciliation_records 10) — I audited `D2-CL01`'s typed_labels 58 and
  findings_total 16 by direct read and the rest by coverage read. So one
  family was re-read at freeze time and the other was carried from the filed
  round-20 map (`tools/exercise-handoff-e2e.py:184`): the defect is the
  carry, not the packet's whole method. Verification of the remaining v2 rows
  stays with D18/R01; D03's fragment independently asserts the same D2
  live-accuracy (`reports/round-34/depth/D03-ledger-rows.md:159`).

## 6. Byte-preservation control

```
$ git status --porcelain reports/
?? reports/round-34/
```

Only the round-34 assignment directory is untracked; no `reports/round-1..33`
file is modified by any run in this seat. `reports/round-30/handoff/
declared-in-r6/packet.md` still hashes `6ced88ad…f0bb` and `twin.json`
`6633443d…fd4e`, matching `freeze.txt:2-3`. No filed runner was executed:
the only runner-adjacent invocation was
`tools/exercise-handoff-e2e.py --profile v3 --quiet` (a tool, not a
`reports/round-*/run-validation.py`), run without `--freeze`, which writes
only into its isolated temp directory
(`tools/exercise-handoff-e2e.py:441-442`, `:1354-1355`).

## Owed

- `reports/round-34/depth/D05-packet-draft.md` (the D05 draft packet) — my
  control (a) was exercised on six drafts built from the filed r6 bytes
  rather than on D05's actual draft, because D05 had not landed when this
  seat ran. When D05 lands, the integrator (or D17/D18/D20) can apply §4's
  method to it: run the instrument extracted from §4 over that draft with
  `--root .` and expect exit 0 with `stale=0`, `without-position=0`; any
  non-zero exit is a defect the gate will not report. The shipped bytes are
  already verified against this control set: the source extracted from §4's
  fence reproduces `base` → exit 1 with `stale=17`, `live-pos` → exit 0,
  `tampered` → exit 1 with `stale=1`.
- `reports/round-34/depth/D11-preservation.md` — my §6 is an independent
  measurement, not the claim-D receipt's preservation leg (D11 owns it).
- No shared file was edited; §4's instrument and recipes are drafts for the
  integrator.

## Citations

- `reports/round-30/handoff/declared-in-r6/packet.md:68` (A-30 manifest row,
  live figures + live digest) vs `:148`,`:149`,`:150`,`:151`,`:307` (stale
  ledger/OQ figures) — read at HEAD da68a6d; whole-file sha256
  `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb`.
- `reports/round-30/handoff/declared-in-r6/freeze.txt:2-3` (packet_sha256 /
  twin_sha256), `:4` (gate verdict), `:6` (links 105/105).
- `reports/round-30/handoff/declared-in-r6/expected.json` (baseline: claims
  27, `d2_typed_labels` 58, `d4_typed_labels`, counts).
- `examples/culture-d4/typed-labels.d4.yml:29-46` (coverage block),
  `:2865` (nested `typed_labels.stats`), `:58,:70,:82,:94,:106,:118`
  (`"code": "R-MAT-RESOLVED"` as a value only), `:48,:50` (enclosing
  `era_material_reconciliation.records`).
- `examples/culture-d4/expected-holds.json` — `counts {hold 12, note 0,
  fail 0}`; 12 holds all `id: D2L-FORM-UNRESOLVED`, zero `D2L-RANK`; empty
  `notes`.
- `tools/gates/handoff-packet-check.py:537-545` (manifest digest leg —
  presence only), `:881` (the only packet read), `:1-30` (docstring: "judges
  the packet document, not the truth of its contents"); no hash computation
  in the file (`grep -n "hashlib\|sha256"` matches only fixture literals at
  :625-636, :759, :785).
- `tools/harness/packet_links.py:77-95` (`_json_path_get`), `:143-153`
  (`_json_contains`), `:155-166` (`_text_contains`: `.json` branch at :159,
  word-boundary fallback at :164-166), `:1-40` (docstring: word-boundary
  match in any other text file).
- `tools/exercise-handoff-e2e.py:184` (`CLAIMS_MAP =
  reports/round-20/handoff/claims-map.md`), `:2286` (`D4_ROW_RE`), `:2289`
  (`v3_parse_claims_map`), `:2476` (`v3_manifest_rows`), `:2599`+
  (`v3_build_claim_rows`), `:1933-1934` (renderer defaults,
  `reports/round-30/handoff/declared-in-r6/expected.json` /
  `…/declared-in-r6`), `:3738` (link/uncertainty legs fed the twin),
  `:441-442`,`:1354-1355` (isolated temp writes).
- `reports/round-20/handoff/claims-map.md:99` ("The D4 typed channel types 74
  labels — 56 native-form, 12 …").
- `git show 35b6797:examples/culture-d4/typed-labels.d4.yml` (74/56/16) and
  `git show 35b6797:examples/culture-d4/expected-holds.json` (15/1/0);
  `git show 11df1fd:examples/culture-d4/typed-labels.d4.yml` (82/64/12);
  `git log --oneline -1` = `da68a6d`.
- Commands run (all in `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
  `TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1`):
  `python3 tools/gates/handoff-packet-check.py <packet>` over the filed pair
  and the six drafts; `python3 tools/exercise-handoff-e2e.py --profile v3
  --quiet`; `python3 tools/harness/packet_links.py --repo-root "$PWD"
  --links <specs>` (38-anchor batch, four single-spec probes, the two
  dotted-token probes); `python3 .scratch/D13/claim_number_audit.py
  <draft> --root .` over the six drafts; `python3
  .scratch/D13/build_controls.py`; `sha256sum` over the r6 directory;
  `git status --porcelain reports/`.
