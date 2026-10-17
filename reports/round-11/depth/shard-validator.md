# R11-D07 — projection validator: typed-packet well-formedness pre-gate

- round: 11 (loop 1 of 3, build round 4 of 4) · claim **D (depth)** · shard: D07 (validator)
- owner: L2 worker, `kotodama-shokunin` lane
- assignment (verbatim): "DEPTH R11-D07 (validator): projection validator (typed packet
  well-formedness pre-gate); fragment reports/round-11/depth/shard-validator.md."
- writes: this file only, plus in-lane scratch under `.scratch/d07/` (`TMPDIR=$PWD/.scratch`
  exported before every scratch-writing command; `/tmp` unused). No tool, packet, component, gate,
  baseline, manifest or earlier-round byte is edited by this seat; `reports/round-{8,9,10}/**` are
  filed and read-only here. No commit, no push.
- baseline revision: `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7` (`git rev-parse HEAD`,
  2026-10-17T22:06Z).
- canon: NON-CANON engineering evidence. Nothing here admits a round, a capability or a canon fact;
  the domain content (the ten owed garment forms) stays open design debt and lore's business.
- status: **COMPLETE for this shard** — validator block authored (1454 lines), **66/66 controls
  green**, receipts frozen at **2026-10-17T22:19:16Z**; one live defect caught and one live
  discrepancy reported (§3). Nothing the parent's integration does is claimed here.

## 0. What this shard delivers, and where it sits

The round-11 D claim wires the round-8 typed-label projection into the D2 flow. The design seat
(R11-D01, `reports/round-11/depth/design.md`) fixes the pipeline as

```
components/ → tools/assemble-d2.py → packet.d2.yml
            → tools/d2-typed-labels.py → typed-labels.d2.yml (projection)
            → tools/assemble-d2-typed.py (adapter) → packet.d2.typed.yml (typed packet)
            → tools/gates/typed-gate-flow.py / typed-pipeline gate reads it (legs L1–L4)
```

and the gate re-verifies embedded pins while its hold-set leg compares the finding set to a frozen
expected set (`design.md` §3.1, §4). This shard delivers the **pre-gate validator**: one
stdlib-only block that re-asserts, over the artifact the gate is about to read, the contract the
reader relies on — so a hand-edited, truncated, stale, smuggled or severity-swapped typed packet is
refused *before* a gate can read a silent pass out of it. It is a precondition check, not a gate
verdict: holds are data, and exit 0 is reachable with holds present.

Five document shapes are accepted; the shape is declared in every verdict:

| shape | document | what is checked |
|---|---|---|
| `projection` | `typed_labels: {stats, labels}` + `findings` (+ `coverage`, `assembly`) — `examples/culture-d2/typed-labels.d2.yml` | rules 1–6 below |
| `view` | `sound_channel`, `off_channel`, `named_holds`, `hold_set`, `findings`, `provenance`, `stats` — the R11-D04 read-side view | rules 1–6 + view rules |
| `packet` | a packet-shaped document carrying `typed_labels` as a list | rules 1–6 |
| `typed-packet` | packet blocks + `typed_channel` routing rows + `typed_findings` + `assembly` pins (design §2.2) | rules 1–6 + route rules |
| `typed-flow` | packet blocks + `typed_view` (`rules`, `sound_channel` `on`/`off`/`untyped`, `source_packet_sha256`) + per-record marks — `examples/culture-d2/packet.d2.typed.yml` as landed | flow rules |

Two declared expected-set forms are consumed: a flat `{families, exact, holds[]}` spec, the design's
`kotodama-typed-pipeline-holds-v1` baseline (`design.md` §4.5; holds **and** notes pinned,
`counts` re-derived from the lists), and the landed `kotodama-typed-gate-expected-v1` baseline
(`expected_findings`, `off_sound_channel`, `owed_slots`, `typed_packet_sha256`).

## 1. The contract this validator enforces

Codes are `V-*` (validator family), each carrying the design-spec §6 `D2L-*` class it belongs to;
severity is `error` except the provenance-drift codes, which are `hold` (a stale artifact is
honest, not malformed). Exit: **2** could-not-evaluate (envelope class, stable message, no
traceback), **1** any defect, **0** clean.

| rule | codes | what fires it |
|---|---|---|
| envelope | `V-ENVELOPE` (exit 2) | document not a mapping / no recognised section / labels, findings, rows not mappings / `hold_set` not a list of strings |
| schema (over the emitted artifact, not the packet) | `V-SCHEMA-FIELD`, `-KIND`, `-STATUS`, `-SEVERITY`, `-ID`, `-TEXT`, `-NULL-REASON` | missing/empty required field; kind/status/severity outside the closed enums; duplicate or malformed id; supplied without text, text without script, unknown representation; a null field with no field-specific reason in `issues` |
| channel discipline | `V-CHANNEL-TRANSLATED-SUPPLIED`, `-TRANSLATION-IDENTITY`, `-PHON-NAME`, `-SOUND-FORM`, `-IDENTITY`, `V-CHANNEL-VIEW` | a `translated-label` marked supplied; translated text equal to a supplied sound form's text; a `PHON-*`/inventory finding naming a translated label (the round-4 artifact class); a supplied sound form without text/script; two supplied sound forms on one record; a translated label on the view's sound channel |
| view well-formedness | `V-VIEW-DISJOINT`, `-SOUND-MEMBER`, `-HOLDSET`, `-HOLD-DISJOINT`, `-STATS` | a label on both channels; a non-supplied/non-sound kind on `sound_channel`; `named_holds` ≠ the hard finding set; `hold_set` ≠ the named-hold rendering under one consistent key; a declared size/count ≠ the enumeration |
| named holds | `V-HOLD-UNNAMED`, `-OWED`, `-ORPHAN` | a hard finding without a D2L class, `where` or `detail`; an owed form (`to-verify` translated label with a live `label_id`) carried as no hold; a hold naming no live record or no longer naming its referent slot |
| expected-set exactness | `V-HOLD-LAUNDER`, `-PHANTOM`, `-SEVERITY-SWAP`, `V-COVERAGE-COUNT` | an expected entry absent from the artifact; an artifact finding outside the declared set (under `exact`); a severity downgrade/upgrade named; a baseline whose `counts` disagree with its own lists |
| provenance / freshness | `V-PROV-MISSING`, `-PACKET-DRIFT`, `-READER-DRIFT`, `V-PROV-PATH`, `V-VIEW-PROVENANCE` | missing/short pins; declared pin ≠ live bytes (named **hold**); a view whose `stale` flag contradicts its two shas; an absolute host path in the document body |
| coverage identity | `V-COVERAGE-COUNT` | any declared count (`labels`, `labels_by_kind`, `findings_total`, `findings_hold_or_fail`, `stats.*`) ≠ the enumeration |
| route rules (`typed-packet`) | `V-ROUTE-ROW`, `-KIND`, `-CHANNEL`, `-FIELD`, `-HOLD`, `-ORPHAN` | a routing row missing a field; kind outside the three; a `translated-label` row not on `off-sound-and-identity`; `off_channel_field` equal to `source_field`, or the record still carrying the checked field; the routed record carrying no named hold; a row naming no live record |
| flow rules (`typed-flow`) | reuse of `V-ROUTE-*`, `V-VIEW-*`, plus the expected-gate checks | `typed_view` missing `generator`/`source_packet`/`rules`; bucket not a list; a record in two buckets; an `off` record without `compare_only` or without `owed_form`; an `untyped` record that carries `typed_label_kind`; `source_packet_sha256` ≠ the live base packet; expected `off_sound_channel`/`owed_slots`/`typed_packet_sha256`/hold naming disagreeing with the artifact |

The named-hold discipline is the point of the shard, and it is exactly the claim's wording made
executable: *translated labels never enter the sound channel* (channel + route rules), *owed native
forms are carried as named holds, not PHON artifacts* (owed/orphan + PHON-name + `owed_form` rules),
and *findings equal the expected hold set exactly* (expected-set rules against the design's §4.2 set).

## 2. Receipts

Artifact under test (the block as run, sha256 `sha256sum`):
`.scratch/d07/typed_packet_validator.py` `2daa106cf97b5765dbfaf8455d104580047ca96f7b416e420923cc664c14e9c3`,
1454 lines. It is embedded verbatim in §4: this fragment was assembled as
`{ cat .scratch/d07/frag-head.md; printf '```python\n'; cat .scratch/d07/typed_packet_validator.py; printf '```\n\n'; cat .scratch/d07/frag-tail.md; } > reports/round-11/depth/shard-validator.md`,
so the §4 block equals the file that produced every receipt below (modulo the final newline the
fence takes). Verified: the block extracted back out of this file, written to a scratch path, and
run as `--selftest` exits 0 with `66/66 checks passed`.

### 2.1 Pre-re-pin stamp, 2026-10-17T22:11:54Z (kept: it is the drift evidence)

| check | command | verdict | receipt sha256 |
|---|---|---|---|
| control matrix (then 42 controls) | `python3 .scratch/d07/typed_packet_validator.py --selftest` | exit **0**, `selftest: 42/42 checks passed` | `06e58287…` |
| live projection vs the §4.5 baseline | `… --check examples/culture-d2/typed-labels.d2.yml --root . --expect .scratch/d07/expected-holds-v1.json` | exit **1** — one `V-PROV-PACKET-DRIFT` hold; `declared=16 matched=16 missing=0 phantom=0` | `27740619…` |
| raw packet (envelope control) | `… --check examples/culture-d2/packet.d2.yml --root . --yaml` | exit **2**, `could-not-evaluate: V-ENVELOPE: document carries no typed_labels section and no view channels` | `728f5c7c…` |

At that stamp the committed projection hashed `e70ba147…` while the packet hashed `e0f21509…`, and
the projection declared `8da90b07…` — the stale pin of §3.

### 2.2 Post-re-pin stamp, 2026-10-17T22:19:16Z (the acceptance run)

| check | command | verdict | receipt sha256 |
|---|---|---|---|
| control matrix | `python3 .scratch/d07/typed_packet_validator.py --selftest` | exit **0**, `selftest: 66/66 checks passed` | `8a4c2f69…` |
| re-pinned projection vs the §4.5 baseline | `… --check examples/culture-d2/typed-labels.d2.yml --root . --expect .scratch/d07/expected-holds-v1.json` | exit **0**, `declared=16 matched=16 missing=0 phantom=0` | `00792ea6…` |
| **landed flow packet** vs its committed baseline | `… --check examples/culture-d2/packet.d2.typed.yml --yaml --root . --expect examples/culture-d2/typed-gate.expected.json` | exit **0**, `typed-flow shape, … defects=0` | `b069a7ad…` |
| D04 routing-table scratch packet (`typed_channel` variant) vs the §4.5 baseline | `… --check .scratch/d04/packet.d2.typed.yml --yaml --root . --projection examples/culture-d2/typed-labels.d2.yml --expect .scratch/d07/expected-holds-v1.json` | exit **1** — its `typed_findings` carry 15 holds and **no note**; the pinned note `SR-01#a\|SR-01#b` is absent (§3b) | `aa0b9f12…` |
| stale D04 view | `… --check .scratch/d04/view-live-a.json --root . --expect .scratch/d07/expected-holds-v1.json` | exit **1** — `V-PROV-PACKET-DRIFT` on the view's own `stale: true`; hold set matched 16/16 | `9d1f5838…` |
| negative matrix | `python3` driver over mutated live documents | see below | `1e857e2d…` |

The 66-control selftest covers: the five shapes' positive fixtures (provenance hash-compared against
scratch files, not merely parsed), determinism (two runs byte-identical as JSON), envelope refusals,
schema/enum/duplicate/null-reason controls, channel controls (including the control-of-the-control:
a `PHON-*` finding naming a **native** form is not a channel defect), hold controls
(owed-missing, orphan, unnamed), view controls (disjointness, sound member, hold_set erased,
named_holds dropped, stats inflated, staleness laundered, stale-declared), route controls
(row field, kind, channel, field-not-moved, checked-field-still-present, orphan row, hold dropped,
pins drifted), flow controls (bucket type, disjoint buckets, off-without-compare_only,
off-without-owed_form, untyped-marked, source pin drift) and expected-gate controls (off set,
owed slots, fail finding, hold outside off, typed-packet pin), plus the v1-baseline controls
(match, severity swap to `fail`, downgrade to `note`, counts).

Negative matrix over the *live* artifacts (injected fault → codes):

```
D17-translated label on sound channel      exit=1 ['V-CHANNEL-TRANSLATED-SUPPLIED']
D18-owed form dropped silently             exit=1 ['V-COVERAGE-COUNT', 'V-HOLD-LAUNDER', 'V-HOLD-OWED']
D19-hold laundered (downgraded to note)    exit=1 ['V-COVERAGE-COUNT', 'V-HOLD-OWED']
PHON artifact naming a translated label    exit=1 ['V-CHANNEL-PHON-NAME', 'V-COVERAGE-COUNT']
flow: gloss left on the checked channel    exit=1 ['V-COVERAGE-COUNT', 'V-ROUTE-FIELD']
flow: off record also on the sound bucket  exit=1 ['V-VIEW-DISJOINT']
flow: pinned hold naming an unrouted record exit=1 ['V-HOLD-ORPHAN']
```

The first three are the negatives the round-11 targets name (D17–D19: a translated label smuggled
onto the sound channel; an owed form dropped silently; a hold laundered as clean); each is caught
here as well as by the design's mechanisms (`design.md` §6). The D18/D19 lines also carry
`V-COVERAGE-COUNT` because the mutation left the declared counts behind — the coverage rule is
doing exactly that job.

Pins used at the stamps above (`sha256sum`): projection `a3aa452c…` (was `e70ba147…`),
packet `e0f21509…`, landed flow packet `e8a83445…`, its baseline `7ed59731…`,
`tools/typed-gate-flow.py` `5758e315…`, `tools/gates/costume-era-consistency-gate.py` `e6bffd70…`,
`tools/d2-typed-labels.py` `0da0015f…`, D04 routing-table scratch packet `5347a682…`,
baseline spec `.scratch/d07/expected-holds-v1.json` `815bfc6f…` (built from
`python3 tools/d2-typed-labels.py --json` — the projector, an independent tool from the adapters
graded above — counts `{hold: 15, note: 1, fail: 0}`, the `design.md` §4.2 set).

## 3. Live defects and discrepancies this validator caught

### 3a. The stale projection pin — caught at 22:11:54Z, resolved by a sibling seat's re-pin

At the pre-re-pin stamp both live runs exited 1 with **exactly one** defect, the one the design seat
found independently (`design.md` §1.4):

```
DEFECT V-PROV-PACKET-DRIFT: [hold/D2L-DATA] $.assembly.packet_sha256 — declared packet
8da90b07…2b81e but live bytes hash e0f21509…b643; the typed packet is stale
```

Disposition (cause named): *legitimate change* — the packet was re-assembled after the projection
was emitted, and the projection was not re-emitted. Evidence: `python3 tools/d2-typed-labels.py
--check` exited 1 then, and a JSON-normalised diff between the committed projection and a fresh
`--emit` showed **exactly one differing line**, `assembly.packet_sha256` (`diff -u` over the two
normalised documents, 11 lines of unified-diff output, one changed line). The validator treated it
as a **hold**, not an error: the artifact was honest about an obsolete pin.

Between the two stamps a sibling seat landed the design's §5.1 re-pin: the projection now hashes
`a3aa452c…` — byte-for-byte the design's predicted post-re-pin digest — `python3
tools/d2-typed-labels.py --check` exits 0, and the validator's acceptance run moves to **exit 0**
(§2.2). This seat did not perform the re-pin and claims no part of it; the before/after pair is
recorded here because the validator is the executable acceptance check for that leg.

### 3b. The routing-table variant carries 15 findings, the pinned set has 16 (report, do not absorb)

D04's scratch `typed_channel` packet (`.scratch/d04/packet.d2.typed.yml`, `5347a682…`, read
22:19:16Z) carries `typed_findings` with 15 holds and **no note**, while the design's §4.3 pins the
note `D2L-RANK` at `SR-01#a|SR-01#b` as present-but-not-counted. The validator reports
`V-HOLD-LAUNDER` for that note against the §4.5 baseline. The *landed* artifact
(`examples/culture-d2/packet.d2.typed.yml`, `e8a83445…`) carries the full set in its committed
baseline `typed-gate.expected.json` (16 findings: 15 holds + 1 note, recomputed at 22:19:16Z), and
validates clean. Reported, not absorbed: if the `typed_channel` variant lands as the graded artifact,
its carried finding set must be told which set it pins.

## 4. Implementation for the integrator (lift verbatim)
```python
#!/usr/bin/env python3
"""typed_packet_validator — pre-gate well-formedness validation for the D2
typed packet (R11-D07).

Placement: between the typed-packet emitter / read-side adapter and the D2 gate
that consumes it. The validator re-asserts, over the artifact the gate is about
to read, the contract the reader relies on, so a hand-edited, truncated, stale,
smuggled or severity-swapped typed packet is refused before a gate can read a
silent pass out of it.

Three artifact shapes are accepted; the shape is declared in the verdict:

  * **projection** — `typed_labels: {stats, labels}` plus `findings`
    (`examples/culture-d2/typed-labels.d2.yml`, emitted by
    `tools/d2-typed-labels.py`);
  * **view** — the read-side view a gate consumes: `sound_channel`,
    `off_channel`, `named_holds`, `hold_set`, `findings`, `provenance`, `stats`
    (the R11-D04 adapter contract);
  * **packet** — a packet-shaped document carrying `typed_labels` as a list.

What is checked (all read-only):

  1. **Envelope** — the document is a mapping in one of the three shapes, every
     label/finding/row a mapping. Anything else is could-not-evaluate (exit 2,
     stable message, no traceback).
  2. **Schema** — closed enums (`kind`, `status`, `severity`), required fields,
     stable record-id shape, unique ids, supplied-requires-text, text requires
     script, null-with-reason. The emitter's parser owns the packet side; this
     re-check owns the emitted artifact, so an edit between emit and gate
     cannot pass.
  3. **Channel discipline** — a `translated-label` may never sit on the sound
     channel: not among `sound_channel`, never `status: supplied`, text never
     equal to a supplied sound form's text, and no `PHON-*`/inventory finding
     naming its record. The view's two channels must be disjoint, complete over
     the labels, and the sound side supplied with text and script.
  4. **Named holds** — every hard finding is named (`code`, `where`, `detail`);
     in a view, `named_holds` is exactly the hard finding set and `hold_set` is
     exactly its `CODE:WHERE` rendering; every owed form (`to-verify`
     translated label with a live `label_id`) is carried as a
     `D2L-FORM-UNRESOLVED` hold that names its referent; a hold naming nothing
     live is an orphan. With a declared expected set (flat list or the design's
     `kotodama-typed-pipeline-holds-v1` baseline) the observed family must equal
     it exactly on `(id, severity, where)`: a missing hold is a laundering
     defect, an extra one a phantom, and a severity swap is named as such.
  5. **Provenance and freshness** — `assembly.packet_sha256` /
     `assembly.reader_sha256` (projection) or the view's `provenance` block
     (packet/live sha, `stale` flag) are present and internally consistent, and
     hash-compared against the live files when they are resolvable. A view that
     declares `stale: false` while its two shas differ is laundering its own
     provenance. No absolute host path appears in the document body.
  6. **Coverage identity** — every count the artifact declares (labels,
     by_kind, findings_total, holds, channel sizes, stats.labels) equals the
     count obtained by enumerating the artifact itself.

Exit codes: 0 = well-formed (holds are data, not defects), 1 = defect(s)
emitted and the report is complete, 2 = could-not-evaluate (envelope class;
stable message). Finding codes are `V-*` (validator family), each carrying the
design-spec §6 `D2L-*` class it belongs to; an unmapped `V-*` code in a
consumer is a defect in that consumer's table, not a silent pass.

Calibration: this is a pre-gate precondition check, not a gate verdict and not
a canon ruling. It never rewrites the artifact.
"""

import argparse
import hashlib
import json
import pathlib
import re
import runpy
import sys
import tempfile

KINDS = ("translated-label", "native-form", "borrowed-strata")
SOUND_KINDS = ("native-form", "borrowed-strata")
STATUSES = ("supplied", "to-verify", "absent")
REPRESENTATIONS = ("english-gloss", "editorial-romanization", "native-spelling")
D2L_IDS = ("D2L-DATA", "D2L-FORM-UNRESOLVED", "D2L-NATIVE", "D2L-BORROW",
           "D2L-ERA", "D2L-MATERIAL", "D2L-RANK", "D2L-SCOPE")
HARD = ("fail", "reject", "hold", "error")
SEVERITIES = ("fail", "reject", "hold", "error", "note")
FORM_HOLD = "D2L-FORM-UNRESOLVED"
_ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*(-[A-Za-z0-9]+)*$")
_HEX64 = re.compile(r"[0-9a-f]{64}$")
NULL_FIELDS = ("text", "script", "representation", "scheme")

# V-code -> (class, severity). A defect code absent from this table is a bug
# in this validator, not a silent pass (checked in selftest).
V_CODES = {
    "V-SCHEMA-FIELD": ("D2L-DATA", "error"),
    "V-SCHEMA-KIND": ("D2L-DATA", "error"),
    "V-SCHEMA-STATUS": ("D2L-DATA", "error"),
    "V-SCHEMA-SEVERITY": ("D2L-DATA", "error"),
    "V-SCHEMA-ID": ("D2L-DATA", "error"),
    "V-SCHEMA-TEXT": ("D2L-DATA", "error"),
    "V-SCHEMA-NULL-REASON": ("D2L-DATA", "error"),
    "V-CHANNEL-TRANSLATED-SUPPLIED": ("D2L-SCOPE", "error"),
    "V-CHANNEL-TRANSLATION-IDENTITY": ("D2L-SCOPE", "error"),
    "V-CHANNEL-PHON-NAME": ("D2L-NATIVE", "error"),
    "V-CHANNEL-SOUND-FORM": ("D2L-NATIVE", "error"),
    "V-CHANNEL-IDENTITY": ("D2L-DATA", "error"),
    "V-CHANNEL-VIEW": ("D2L-NATIVE", "error"),
    "V-VIEW-DISJOINT": ("D2L-DATA", "error"),
    "V-VIEW-SOUND-MEMBER": ("D2L-NATIVE", "error"),
    "V-VIEW-HOLDSET": ("D2L-DATA", "error"),
    "V-VIEW-HOLD-DISJOINT": ("D2L-DATA", "error"),
    "V-VIEW-STATS": ("D2L-DATA", "error"),
    "V-VIEW-PROVENANCE": ("D2L-DATA", "error"),
    "V-ROUTE-ROW": ("D2L-DATA", "error"),
    "V-ROUTE-KIND": ("D2L-DATA", "error"),
    "V-ROUTE-CHANNEL": ("D2L-SCOPE", "error"),
    "V-ROUTE-HOLD": (FORM_HOLD, "error"),
    "V-ROUTE-FIELD": ("D2L-SCOPE", "error"),
    "V-ROUTE-ORPHAN": ("D2L-DATA", "error"),
    "V-HOLD-UNNAMED": ("D2L-DATA", "error"),
    "V-HOLD-OWED": (FORM_HOLD, "error"),
    "V-HOLD-ORPHAN": (FORM_HOLD, "error"),
    "V-HOLD-LAUNDER": (FORM_HOLD, "error"),
    "V-HOLD-PHANTOM": (FORM_HOLD, "error"),
    "V-HOLD-SEVERITY-SWAP": (FORM_HOLD, "error"),
    "V-PROV-MISSING": ("D2L-DATA", "error"),
    "V-PROV-PACKET-DRIFT": ("D2L-DATA", "hold"),
    "V-PROV-READER-DRIFT": ("D2L-DATA", "hold"),
    "V-PROV-PATH": ("D2L-SCOPE", "error"),
    "V-COVERAGE-COUNT": ("D2L-DATA", "error"),
}

VIEW_KEYS = ("sound_channel", "off_channel", "named_holds", "hold_set")


class CouldNotEvaluate(ValueError):
    """Envelope class: map to exit 2 with this stable message."""


def _defect(defects, code, where, detail):
    klass, severity = V_CODES[code]
    defects.append({"code": code, "where": where, "detail": detail,
                    "severity": severity, "class": klass})


def _is_text(value):
    return isinstance(value, str) and bool(value.strip())


def _sha256(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def _strings(obj, path="$"):
    """Every string value in the document, with a JSON-path-ish locator."""
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for key, value in obj.items():
            yield from _strings(value, "%s.%s" % (path, key))
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            yield from _strings(value, "%s[%d]" % (path, index))


def _mapping_list(doc, key):
    value = doc.get(key)
    if value is None:
        raise CouldNotEvaluate("V-ENVELOPE: %s is missing" % key)
    if not isinstance(value, list):
        raise CouldNotEvaluate("V-ENVELOPE: %s is not a list" % key)
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            raise CouldNotEvaluate("V-ENVELOPE: %s[%d] is not a mapping" % (key, index))
    return value


def _extract(doc):
    """(shape, labels, findings, stats, doc) or CouldNotEvaluate."""
    if not isinstance(doc, dict):
        raise CouldNotEvaluate("V-ENVELOPE: typed-packet document is not a mapping")
    if "typed_channel" in doc:
        rows = _mapping_list(doc, "typed_channel")
        key = "typed_findings" if "typed_findings" in doc else "findings"
        findings = _mapping_list(doc, key) if key in doc else []
        return "typed-packet", [], findings, None, doc
    if "typed_view" in doc:
        if not isinstance(doc.get("typed_view"), dict):
            raise CouldNotEvaluate("V-ENVELOPE: typed_view is not a mapping")
        return "typed-flow", [], [], None, doc
    if any(key in doc for key in VIEW_KEYS):
        sound = _mapping_list(doc, "sound_channel")
        off = _mapping_list(doc, "off_channel")
        findings = _mapping_list(doc, "findings")
        _mapping_list(doc, "named_holds")
        holds = doc.get("hold_set")
        if not isinstance(holds, list) or not all(isinstance(h, str) for h in holds):
            raise CouldNotEvaluate("V-ENVELOPE: hold_set is not a list of strings")
        return "view", sound + off, findings, doc.get("stats"), doc
    section = doc.get("typed_labels")
    if section is None:
        raise CouldNotEvaluate("V-ENVELOPE: document carries no typed_labels section "
                               "and no view channels")
    if isinstance(section, dict):
        labels, stats, shape = section.get("labels"), section.get("stats"), "projection"
    elif isinstance(section, list):
        labels, stats, shape = section, None, "packet"
    else:
        raise CouldNotEvaluate("V-ENVELOPE: typed_labels is neither a labels mapping nor a list")
    if not isinstance(labels, list):
        raise CouldNotEvaluate("V-ENVELOPE: typed_labels carries no label list")
    for index, label in enumerate(labels):
        if not isinstance(label, dict):
            raise CouldNotEvaluate("V-ENVELOPE: typed_labels[%d] is not a mapping" % index)
    findings = doc.get("findings", [])
    if findings is None:
        findings = []
    if not isinstance(findings, list):
        raise CouldNotEvaluate("V-ENVELOPE: findings is not a list")
    for index, finding in enumerate(findings):
        if not isinstance(finding, dict):
            raise CouldNotEvaluate("V-ENVELOPE: findings[%d] is not a mapping" % index)
    return shape, labels, findings, stats, doc


def _schema_defects(labels, defects):
    seen = {}
    for label in labels:
        where = label.get("id") if _is_text(label.get("id")) else "<unnamed label>"
        for field in ("id", "owner", "kind", "status"):
            if not _is_text(label.get(field)):
                _defect(defects, "V-SCHEMA-FIELD", where,
                        "required field %r is missing or empty" % field)
        rid = label.get("id")
        if _is_text(rid):
            if not _ID_RE.match(rid):
                _defect(defects, "V-SCHEMA-ID", where,
                        "id %r is not a stable record id shape" % rid)
            if rid in seen:
                _defect(defects, "V-SCHEMA-ID", where, "duplicate label record id")
            seen[rid] = True
        kind, status = label.get("kind"), label.get("status")
        if kind not in KINDS:
            _defect(defects, "V-SCHEMA-KIND", where,
                    "kind %r is not one of %s" % (kind, list(KINDS)))
        if status not in STATUSES:
            _defect(defects, "V-SCHEMA-STATUS", where,
                    "status %r is not one of %s" % (status, list(STATUSES)))
        text = label.get("text")
        if status == "supplied" and not _is_text(text):
            _defect(defects, "V-SCHEMA-TEXT", where, "status supplied requires text")
        if _is_text(text) and not _is_text(label.get("script")):
            _defect(defects, "V-SCHEMA-TEXT", where, "supplied text requires a script")
        representation = label.get("representation")
        if representation is not None and representation not in REPRESENTATIONS:
            _defect(defects, "V-SCHEMA-TEXT", where,
                    "representation %r is not one of %s" % (representation, list(REPRESENTATIONS)))
        if label.get("owner") == "11-costumes" and not _is_text(label.get("label_id")):
            _defect(defects, "V-SCHEMA-FIELD", where,
                    "costume label carries no label_id for its form slot")
        issues = label.get("issues") or []
        reasons = {issue.get("field") for issue in issues if isinstance(issue, dict)}
        for field in NULL_FIELDS:
            if label.get(field) is None and field not in reasons:
                _defect(defects, "V-SCHEMA-NULL-REASON", where,
                        "null %s carries no field-specific reason in issues" % field)


def _channel_defects(labels, findings, defects):
    by_id = {label.get("id"): label for label in labels if _is_text(label.get("id"))}
    sound_texts = {}
    supplied_counts = {}
    for label in labels:
        kind, status, where = label.get("kind"), label.get("status"), label.get("id")
        if kind == "translated-label" and status == "supplied":
            _defect(defects, "V-CHANNEL-TRANSLATED-SUPPLIED", where,
                    "translated label is marked supplied; only a native form or a "
                    "declared borrowed form may enter the sound channel")
        if kind in SOUND_KINDS and status == "supplied":
            if not _is_text(label.get("text")) or not _is_text(label.get("script")):
                _defect(defects, "V-CHANNEL-SOUND-FORM", where,
                        "supplied sound form needs text and script before any gate reads it")
            key = (label.get("owner"), label.get("label_id") or label.get("id"))
            supplied_counts.setdefault(key, []).append(where)
            if _is_text(label.get("text")):
                sound_texts.setdefault(label["text"], []).append(where)
    for label in labels:
        if label.get("kind") != "translated-label" or not _is_text(label.get("text")):
            continue
        if label["text"] in sound_texts:
            _defect(defects, "V-CHANNEL-TRANSLATION-IDENTITY", label.get("id"),
                    "translated label's text equals supplied sound form %s; identity by "
                    "translation is not identity (22-label-representation.md §2)"
                    % sound_texts[label["text"]])
    for key, holders in supplied_counts.items():
        if len(holders) > 1:
            _defect(defects, "V-CHANNEL-IDENTITY", holders[0],
                    "two supplied sound forms on one record (%s %s): identity collision"
                    % (key[0], key[1]))
    for finding in findings:
        code = str(finding.get("code", ""))
        if not code.startswith("PHON-") and "INVENTORY" not in code:
            continue
        target = by_id.get(finding.get("where"))
        if target is not None and target.get("kind") == "translated-label":
            _defect(defects, "V-CHANNEL-PHON-NAME", finding.get("where"),
                    "%s finding names a translated label; a translated label never "
                    "enters the sound channel (the PHON artifact class)" % code)


def _view_defects(doc, sound, off, defects):
    sound_ids = {label.get("id") for label in sound}
    off_ids = {label.get("id") for label in off}
    overlap = sorted(sound_ids & off_ids)
    if overlap:
        _defect(defects, "V-VIEW-DISJOINT", overlap[0],
                "%d label(s) sit on both channels: %s" % (len(overlap), overlap))
    for label in sound:
        if label.get("kind") not in SOUND_KINDS or label.get("status") != "supplied":
            _defect(defects, "V-VIEW-SOUND-MEMBER", label.get("id"),
                    "sound_channel member is kind %r / status %r; only supplied "
                    "native-form or borrowed-strata records are sound-checkable"
                    % (label.get("kind"), label.get("status")))
        if label.get("kind") == "translated-label":
            _defect(defects, "V-CHANNEL-VIEW", label.get("id"),
                    "a translated label is on the view's sound channel")
    named = doc.get("named_holds") or []
    hard = [f for f in doc.get("findings", []) if f.get("severity") in HARD]
    hard_keys = sorted((f.get("id"), f.get("code"), f.get("where")) for f in hard)
    named_keys = sorted((f.get("id"), f.get("code"), f.get("where")) for f in named)
    if hard_keys != named_keys:
        only_named = [k for k in named_keys if k not in hard_keys]
        only_findings = [k for k in hard_keys if k not in named_keys]
        _defect(defects, "V-VIEW-HOLD-DISJOINT",
                (only_named or only_findings or [("<none>", "", "")])[0][2] or "$.named_holds",
                "named_holds is not exactly the hard finding set "
                "(named-only=%s findings-only=%s)" % (only_named, only_findings))
    derived_id = sorted("%s:%s" % (f.get("id"), f.get("where")) for f in named)
    derived_code = sorted("%s:%s" % (f.get("code"), f.get("where")) for f in named)
    declared = sorted(doc.get("hold_set") or [])
    if declared not in (derived_id, derived_code):
        _defect(defects, "V-VIEW-HOLDSET", "$.hold_set",
                "hold_set is not the named-hold rendering under one consistent key "
                "(by id missing=%s extra=%s; by code missing=%s extra=%s)"
                % ([h for h in derived_id if h not in declared],
                   [h for h in declared if h not in derived_id],
                   [h for h in derived_code if h not in declared],
                   [h for h in declared if h not in derived_code]))
    stats = doc.get("stats")
    if isinstance(stats, dict):
        checks = (("labels", len(sound) + len(off)),
                  ("sound_channel", len(sound)),
                  ("off_channel", len(off)),
                  ("holds", len(named)))
        for field, actual in checks:
            if field in stats and stats[field] != actual:
                _defect(defects, "V-VIEW-STATS", "$.stats." + field,
                        "declared %r, enumerated %r" % (stats[field], actual))
        if isinstance(stats.get("by_kind"), dict):
            by_kind = {}
            for label in sound + off:
                key = label.get("kind")
                by_kind[key] = by_kind.get(key, 0) + 1
            if stats["by_kind"] != dict(sorted(by_kind.items())):
                _defect(defects, "V-VIEW-STATS", "$.stats.by_kind",
                        "declared %s, enumerated %s"
                        % (json.dumps(stats["by_kind"], sort_keys=True),
                           json.dumps(dict(sorted(by_kind.items())), sort_keys=True)))


def _typed_channel_defects(doc, rows, findings, defects):
    """Routing-table well-formedness for the adapter's typed packet (design §2.2/§2.3)."""
    records = {}
    for block in ("costumes", "lexicon", "names"):
        for record in doc.get(block) or []:
            if isinstance(record, dict) and _is_text(record.get("id")):
                records.setdefault(record["id"], (block, record))
    required = ("record", "kind", "owner", "source_field", "off_channel_field",
                "channel", "hold")
    for row in rows:
        rid = row.get("record")
        where = rid if _is_text(rid) else "<routing row>"
        for field in required:
            if not _is_text(row.get(field)):
                _defect(defects, "V-ROUTE-ROW", where,
                        "routing row lacks %r" % field)
        if row.get("kind") not in KINDS:
            _defect(defects, "V-ROUTE-KIND", where,
                    "kind %r is not one of %s" % (row.get("kind"), list(KINDS)))
        if row.get("kind") == "translated-label" and row.get("channel") != "off-sound-and-identity":
            _defect(defects, "V-ROUTE-CHANNEL", where,
                    "translated-label row declares channel %r; the only licensed channel "
                    "is 'off-sound-and-identity' (design §2.3 row 1)" % row.get("channel"))
        if row.get("hold") not in D2L_IDS:
            _defect(defects, "V-ROUTE-HOLD", where,
                    "hold %r is not a D2L-* class; a routed record must carry a named hold"
                    % row.get("hold"))
        if _is_text(row.get("source_field")) and row.get("source_field") == row.get("off_channel_field"):
            _defect(defects, "V-ROUTE-FIELD", where,
                    "off_channel_field equals source_field %r: the checked field did not move"
                    % row.get("source_field"))
        entry = records.get(rid)
        if entry is None:
            _defect(defects, "V-ROUTE-ORPHAN", where,
                    "routing row names no record in the packet's costumes/lexicon/names blocks")
            continue
        _block, record = entry
        if _is_text(row.get("off_channel_field")) and row["off_channel_field"] not in record:
            _defect(defects, "V-ROUTE-ROW", where,
                    "off_channel_field %r is absent from the record; the gloss is not "
                    "carried where the row says it is" % row["off_channel_field"])
        if _is_text(row.get("source_field")) and row["source_field"] in record:
            _defect(defects, "V-ROUTE-FIELD", where,
                    "the record still carries the checked field %r: the gloss remains on "
                    "the sound channel (design §1.3, the D17 defect class)"
                    % row["source_field"])
        naming = [f for f in findings
                  if (f.get("id") or f.get("code")) == row.get("hold")
                  and f.get("where") == rid]
        if not naming:
            _defect(defects, "V-ROUTE-HOLD", where,
                    "routed record carries no %s hold in typed_findings; an owed form "
                    "may not be routed without its named hold" % row.get("hold"))
        elif _is_text(row.get("label_id")) and row["label_id"] not in (naming[0].get("detail") or ""):
            _defect(defects, "V-HOLD-ORPHAN", where,
                    "the routed record's hold does not name its owed slot %s"
                    % row["label_id"])


def _typed_flow_defects(doc, defects, notes, expected_gate, root, artifact_path):
    """Well-formedness of the flow's typed packet (tools/typed-gate-flow.py):
    the `typed_view` buckets, the per-record marks and the pinned expectation."""
    view = doc.get("typed_view")
    records = {}
    for block in ("costumes", "lexicon", "names"):
        for record in doc.get(block) or []:
            if isinstance(record, dict) and _is_text(record.get("id")):
                records.setdefault(record["id"], (block, record))
    for field in ("generator", "source_packet"):
        if not _is_text(view.get(field)):
            _defect(defects, "V-ROUTE-ROW", "$.typed_view.%s" % field,
                    "typed_view lacks %r" % field)
    rules = view.get("rules")
    if not isinstance(rules, list) or not all(isinstance(r, str) and r.strip() for r in rules):
        _defect(defects, "V-ROUTE-ROW", "$.typed_view.rules",
                "typed_view.rules is not a non-empty list of declared rules")
    pin = view.get("source_packet_sha256")
    if not (isinstance(pin, str) and _HEX64.match(pin)):
        _defect(defects, "V-PROV-MISSING", "$.typed_view.source_packet_sha256",
                "source_packet_sha256 is absent or not a sha256 hex digest")
    else:
        path = pathlib.Path(view.get("source_packet") or "")
        if str(path) and not path.is_absolute():
            path = (pathlib.Path(root) if root else pathlib.Path.cwd()) / path
        if str(path) and path.exists():
            live = _sha256(path)
            if live != pin:
                _defect(defects, "V-PROV-PACKET-DRIFT", "$.typed_view.source_packet_sha256",
                        "the view was built over packet %s but the base packet now hashes "
                        "%s; rebuild the typed packet" % (pin, live))
        else:
            notes.append({"note": "source packet %r not resolvable; pin recorded, not "
                                  "hash-compared" % view.get("source_packet")})
    buckets = view.get("sound_channel")
    if not isinstance(buckets, dict):
        _defect(defects, "V-ROUTE-ROW", "$.typed_view.sound_channel",
                "typed_view carries no sound_channel mapping")
        return
    seen = {}
    for bucket in ("on", "off", "untyped"):
        ids = buckets.get(bucket)
        if not isinstance(ids, list) or not all(isinstance(i, str) for i in ids):
            _defect(defects, "V-ROUTE-ROW", "$.typed_view.sound_channel.%s" % bucket,
                    "bucket %r is not a list of record ids" % bucket)
            continue
        for rid in ids:
            if rid in seen:
                _defect(defects, "V-VIEW-DISJOINT", rid,
                        "record sits in both %r and %r buckets" % (seen[rid], bucket))
            seen[rid] = bucket
            entry = records.get(rid)
            if entry is None:
                _defect(defects, "V-ROUTE-ORPHAN", rid,
                        "bucket %r names no record in the packet blocks" % bucket)
                continue
            _block, record = entry
            if bucket == "off" and not record.get("compare_only"):
                _defect(defects, "V-ROUTE-FIELD", rid,
                        "off-bucket record carries no compare_only mark: the gloss is "
                        "still on the checked channel (design §6 D17)")
            if bucket == "off" and not _is_text(record.get("owed_form")):
                _defect(defects, "V-ROUTE-HOLD", rid,
                        "off-bucket record carries no owed_form: the owed native form "
                        "is not named on the artifact")
            if bucket == "untyped" and record.get("typed_label_kind"):
                _defect(defects, "V-ROUTE-KIND", rid,
                        "untyped bucket names a record that carries typed_label_kind %r"
                        % record.get("typed_label_kind"))
    if expected_gate:
        _expected_gate_defects(view, buckets, records, expected_gate, defects, artifact_path)


def _expected_gate_defects(view, buckets, records, expected_gate, defects, artifact_path):
    """The flow's pinned expectation (schema kotodama-typed-gate-expected-v1)."""
    pin = expected_gate.get("typed_packet_sha256")
    if isinstance(pin, str) and artifact_path and pathlib.Path(artifact_path).exists():
        live = _sha256(artifact_path)
        if pin != live:
            _defect(defects, "V-PROV-PACKET-DRIFT", "$.typed_packet_sha256",
                    "expected baseline pins typed packet %s but the artifact hashes %s"
                    % (pin, live))
    off = sorted(buckets.get("off") or [])
    declared_off = sorted(expected_gate.get("off_sound_channel") or [])
    if "off_sound_channel" in expected_gate and declared_off != off:
        _defect(defects, "V-VIEW-STATS", "$.off_sound_channel",
                "expected off_sound_channel %s differs from the typed view's off bucket %s"
                % (declared_off, off))
    owed = sorted(str(record.get("owed_form"))
                  for _block, record in records.values() if record.get("compare_only"))
    declared_owed = sorted(str(s) for s in expected_gate.get("owed_slots") or [])
    if "owed_slots" in expected_gate and declared_owed != owed:
        _defect(defects, "V-COVERAGE-COUNT", "$.owed_slots",
                "expected owed_slots %s differ from the off-records' owed_form values %s"
                % (declared_owed, owed))
    findings = expected_gate.get("expected_findings") or []
    counts = {}
    for finding in findings:
        severity = finding.get("severity")
        counts[severity] = counts.get(severity, 0) + 1
    for finding in findings:
        if finding.get("severity") in ("fail", "error"):
            _defect(defects, "V-HOLD-UNNAMED", finding.get("where", "$.expected_findings"),
                    "the pinned expectation carries a %r finding; the fail set is not empty"
                    % finding.get("severity"))
        if (finding.get("id") or finding.get("code")) == FORM_HOLD:
            rid = finding.get("record") or finding.get("where")
            if rid not in off:
                _defect(defects, "V-HOLD-ORPHAN", rid,
                        "a pinned form hold names a record outside the off bucket")
            slot = None
            entry = records.get(rid)
            if entry:
                slot = entry[1].get("owed_form")
            named = finding.get("where") if finding.get("where") != rid else None
            if slot and slot not in (finding.get("detail") or "") and named != slot:
                _defect(defects, "V-HOLD-ORPHAN", rid,
                        "the pinned hold names neither its record nor its owed slot %s" % slot)
    return counts


def _hold_defects(labels, findings, defects, expected_holds, families, exact,
                  include_notes=False):
    by_id = {label.get("id"): label for label in labels if _is_text(label.get("id"))}
    for finding in findings:
        severity = finding.get("severity")
        if severity is not None and severity not in SEVERITIES:
            _defect(defects, "V-SCHEMA-SEVERITY", finding.get("where", "<no where>"),
                    "severity %r is not one of %s" % (severity, list(SEVERITIES)))
    hard = [f for f in findings if f.get("severity") in HARD]
    form_holds = [f for f in hard if f.get("id") == FORM_HOLD or f.get("code") == FORM_HOLD]
    for finding in hard:
        code = finding.get("id") if finding.get("id") in D2L_IDS else finding.get("code")
        if code not in D2L_IDS:
            _defect(defects, "V-HOLD-UNNAMED", finding.get("where", "<no where>"),
                    "hard finding %r carries no D2L-* class; an unmapped hold is not a named hold"
                    % finding.get("code"))
        if not _is_text(finding.get("where")) or not _is_text(finding.get("detail")):
            _defect(defects, "V-HOLD-UNNAMED", finding.get("where", "<no where>"),
                    "hard finding lacks where or detail; a hold without a name is silence")
    for label in labels:
        if label.get("kind") != "translated-label" or label.get("status") != "to-verify":
            continue
        if not _is_text(label.get("label_id")):
            continue
        naming = [f for f in form_holds if f.get("where") == label.get("id")]
        if not naming:
            _defect(defects, "V-HOLD-OWED", label.get("id"),
                    "owed form %s is carried as no hold; an owed native form must "
                    "arrive as a named hold, never as a silent pass" % label.get("label_id"))
    for finding in form_holds if labels else []:
        target = by_id.get(finding.get("where"))
        if target is None:
            _defect(defects, "V-HOLD-ORPHAN", finding.get("where"),
                    "hold names a record the document does not carry")
            continue
        slot = target.get("label_id")
        detail = finding.get("detail") or ""
        if _is_text(slot) and slot not in detail and target.get("id") not in detail:
            _defect(defects, "V-HOLD-ORPHAN", finding.get("where"),
                    "hold detail names neither the record nor its owed slot %s" % slot)
    observed = hard
    if include_notes:
        observed = [f for f in findings if f.get("severity") in SEVERITIES]
    if families:
        observed = [f for f in observed
                    if (f.get("id") or f.get("code")) in set(families)]
    matched, missing, phantom = [], [], []
    if expected_holds:
        expected = {}
        for entry in expected_holds:
            if isinstance(entry, dict):
                expected[(entry.get("code"), entry.get("where"),
                          entry.get("severity"))] = entry.get("referent")
            else:
                expected[(entry[0], entry[1], None)] = None
        observed_keys = {}
        observed_lax = {}
        for finding in observed:
            for key in {finding.get("id"), finding.get("code")}:
                observed_keys.setdefault(
                    (key, finding.get("where"), finding.get("severity")), finding)
                observed_lax.setdefault((key, finding.get("where")), finding)
        for (code, where, severity), referent in sorted(expected.items(), key=str):
            hit = observed_keys.get((code, where, severity)) if severity is not None else None
            if hit is None and severity is None:
                hit = observed_lax.get((code, where))
            if hit is None and severity is not None:
                lax = observed_lax.get((code, where))
                if lax is not None and lax.get("severity") != severity:
                    _defect(defects, "V-HOLD-SEVERITY-SWAP", where,
                            "expected %s at %s but the artifact carries severity %r"
                            % (severity, where, lax.get("severity")))
                    missing.append({"code": code, "where": where, "severity": severity})
                    continue
            if hit is None:
                missing.append({"code": code, "where": where, "severity": severity})
                _defect(defects, "V-HOLD-LAUNDER", where,
                        "expected hold %s at %s is absent from the artifact: laundering"
                        % (code, where))
                continue
            matched.append({"code": code, "where": where, "severity": severity})
            if referent and referent not in (hit.get("detail") or ""):
                _defect(defects, "V-HOLD-ORPHAN", where,
                        "hold for %s no longer names its referent %s" % (where, referent))
        if exact:
            expected_pairs = {(code, where) for code, where, _s in expected}
            for finding in observed:
                if (finding.get("id"), finding.get("where")) not in expected_pairs:
                    phantom.append({"code": finding.get("id"), "where": finding.get("where"),
                                    "severity": finding.get("severity")})
            if phantom:
                _defect(defects, "V-HOLD-PHANTOM", phantom[0]["where"],
                        "artifact carries %d hold(s) outside the declared expected set: %s"
                        % (len(phantom), json.dumps(phantom, sort_keys=True)))
    return hard, matched, missing, phantom


def _provenance_defects(doc, defects, packet_path, reader_path, root, notes, shape,
                        projection_path=None):
    if shape == "typed-flow":
        for locator, value in _strings(doc):
            if value.startswith("/") and "/" in value[1:]:
                _defect(defects, "V-PROV-PATH", locator,
                        "absolute host path %r in the document body (replay determinism)"
                        % value)
        return {}
    if shape == "typed-packet":
        assembly = doc.get("assembly")
        if not isinstance(assembly, dict):
            _defect(defects, "V-PROV-MISSING", "$.assembly",
                    "typed packet carries no assembly block; pins cannot be verified")
            return {}
        resolved = {}
        for field in ("packet_sha256", "projection_sha256", "adapter_sha256"):
            value = assembly.get(field)
            if not (isinstance(value, str) and _HEX64.match(value)):
                _defect(defects, "V-PROV-MISSING", "$.assembly.%s" % field,
                        "%s is absent or not a sha256 hex digest" % field)
        base = pathlib.Path(root) if root else pathlib.Path.cwd()
        targets = (("packet", packet_path or assembly.get("packet")),
                   ("projection", projection_path or assembly.get("projection")))
        for field, declared_path in targets:
            if not declared_path:
                notes.append({"note": "no %s path declared or given; its pin is "
                                      "recorded but not hash-compared" % field})
                continue
            path = pathlib.Path(declared_path)
            if not path.is_absolute():
                path = base / path
            if not path.exists():
                notes.append({"note": "%s path %s is not resolvable from here" % (field, declared_path)})
                continue
            live = _sha256(path)
            resolved[field] = str(path)
            resolved[field + "_live"] = live
            declared = assembly.get(field + "_sha256")
            if isinstance(declared, str) and declared != live:
                _defect(defects, "V-PROV-PACKET-DRIFT", "$.assembly.%s_sha256" % field,
                        "declared %s %s but live bytes hash %s; the typed packet was built "
                        "over a stale %s" % (field, declared, live, field))
        for locator, value in _strings(doc):
            if value.startswith("/") and "/" in value[1:]:
                _defect(defects, "V-PROV-PATH", locator,
                        "absolute host path %r in the document body (replay determinism)"
                        % value)
        return resolved
    if shape == "view":
        provenance = doc.get("provenance")
        if not isinstance(provenance, dict):
            _defect(defects, "V-PROV-MISSING", "$.provenance",
                    "view carries no provenance block; freshness cannot be checked")
            return {}
        resolved = {}
        declared = provenance.get("packet_sha256")
        live_declared = provenance.get("live_packet_sha256")
        stale = provenance.get("stale")
        for label, value in (("packet_sha256", declared),
                             ("live_packet_sha256", live_declared)):
            if not (isinstance(value, str) and _HEX64.match(value)):
                _defect(defects, "V-PROV-MISSING", "$.provenance.%s" % label,
                        "%s is absent or not a sha256 hex digest" % label)
        if isinstance(stale, bool) and isinstance(declared, str) and isinstance(live_declared, str):
            if stale != (declared != live_declared):
                _defect(defects, "V-VIEW-PROVENANCE", "$.provenance.stale",
                        "stale=%r contradicts the declared shas (packet=%s live=%s)"
                        % (stale, declared[:12], live_declared[:12]))
        base = pathlib.Path(root) if root else pathlib.Path.cwd()
        path = pathlib.Path(packet_path or provenance.get("packet") or "")
        if str(path) and not path.is_absolute():
            path = base / path
        if str(path) and path.exists():
            live = _sha256(path)
            resolved = {"packet": str(path), "packet_live": live}
            if isinstance(live_declared, str) and live_declared != live:
                _defect(defects, "V-PROV-PACKET-DRIFT", "$.provenance.live_packet_sha256",
                        "declared live packet %s but the file hashes %s"
                        % (live_declared, live))
        if stale is True:
            _defect(defects, "V-PROV-PACKET-DRIFT", "$.provenance.stale",
                    "declared packet %s but live packet %s; the view is built over a "
                    "stale projection (re-pin required)"
                    % (str(declared)[:12], str(live_declared)[:12]))
        for locator, value in _strings(doc):
            if value.startswith("/") and "/" in value[1:]:
                _defect(defects, "V-PROV-PATH", locator,
                        "absolute host path %r in the document body (replay determinism)"
                        % value)
        return resolved
    assembly = doc.get("assembly")
    if not isinstance(assembly, dict):
        if shape == "packet" and "assembly" not in doc:
            notes.append({"note": "packet-shape document carries no assembly block; "
                                  "provenance is the assembler's own --check discipline"})
            assembly = {}
            required = False
        else:
            _defect(defects, "V-PROV-MISSING", "$.assembly",
                    "typed packet carries no assembly block; provenance cannot be checked")
            assembly = {}
            required = True
    else:
        required = True
    for field in ("packet_sha256", "reader_sha256"):
        if not required and field not in assembly:
            continue
        value = assembly.get(field)
        if not (isinstance(value, str) and _HEX64.match(value)):
            _defect(defects, "V-PROV-MISSING", "$.assembly.%s" % field,
                    "%s is absent or not a sha256 hex digest" % field)
    resolved = {}
    base = pathlib.Path(root) if root else pathlib.Path.cwd()
    for field, explicit in (("packet", packet_path), ("reader", reader_path)):
        declared_path = explicit or assembly.get(field)
        if not declared_path:
            notes.append({"note": "no %s path declared or given" % field})
            continue
        path = pathlib.Path(declared_path)
        if not path.is_absolute():
            path = base / path
        resolved[field] = str(path)
        if not path.exists():
            if explicit:
                _defect(defects, "V-PROV-MISSING", field,
                        "given %s path %s does not exist" % (field, declared_path))
            else:
                notes.append({"note": "%s path %s is not resolvable from here"
                              % (field, declared_path)})
            continue
        live = _sha256(path)
        declared = assembly.get(field + "_sha256")
        resolved[field + "_live"] = live
        if isinstance(declared, str) and declared != live:
            code = "V-PROV-PACKET-DRIFT" if field == "packet" else "V-PROV-READER-DRIFT"
            _defect(defects, code, "$.assembly.%s_sha256" % field,
                    "declared %s %s but live bytes hash %s; the typed packet is stale"
                    % (field, declared, live))
    for locator, value in _strings(doc):
        if value.startswith("/") and "/" in value[1:]:
            _defect(defects, "V-PROV-PATH", locator,
                    "absolute host path %r in the document body (replay determinism)"
                    % value)
    return resolved


def _coverage_defects(doc, labels, findings, defects, stats):
    by_kind = {}
    for label in labels:
        by_kind[label.get("kind")] = by_kind.get(label.get("kind"), 0) + 1
    hard = [f for f in findings if f.get("severity") in HARD]
    declared = doc.get("coverage")
    observed = {"labels": len(labels), "by_kind": dict(sorted(by_kind.items())),
                "findings_total": len(findings), "hard": len(hard)}
    if isinstance(stats, dict) and stats.get("labels") not in (None, len(labels)):
        _defect(defects, "V-COVERAGE-COUNT", "$.typed_labels.stats.labels",
                "declared %s labels, enumerated %d" % (stats.get("labels"), len(labels)))
    if declared is None:
        return observed
    if not isinstance(declared, dict):
        _defect(defects, "V-COVERAGE-COUNT", "$.coverage", "coverage block is not a mapping")
        return observed
    pairs = (("typed_labels", len(labels)),
             ("labels_by_kind", dict(sorted(by_kind.items()))),
             ("findings_total", len(findings)),
             ("findings_hold_or_fail", len(hard)))
    for field, actual in pairs:
        if field in declared and declared[field] != actual:
            _defect(defects, "V-COVERAGE-COUNT", "$.coverage." + field,
                    "declared %s, enumerated %s"
                    % (json.dumps(declared[field], sort_keys=True),
                       json.dumps(actual, sort_keys=True)))
    return observed


def expected_from_spec(spec):
    """Expected-set spec -> (entries, families, exact, extra_check).

    Two forms: a flat spec `{families, exact, holds: [{code, where, referent}]}`
    and the design's `kotodama-typed-pipeline-holds-v1` baseline
    `{schema, counts, holds, notes}` — the latter is severity-aware, includes
    the notes, and its own counts must agree with its lists.
    """
    if not isinstance(spec, dict):
        raise CouldNotEvaluate("V-ENVELOPE: expected-holds spec is not a mapping")
    if spec.get("schema") == "kotodama-typed-pipeline-holds-v1":
        holds = spec.get("holds") or []
        notes = spec.get("notes") or []
        entries = ([{"code": e.get("id"), "where": e.get("where"),
                     "severity": e.get("severity"), "detail": e.get("detail")}
                    for e in holds + notes])
        counts = spec.get("counts") or {}
        return entries, None, True, {"counts": counts, "notes": notes, "holds": holds}
    return spec.get("holds"), spec.get("families"), bool(spec.get("exact")), None


def _expected_counts_defects(check, entries, findings, defects, notes):
    if not check:
        return
    counts = check.get("counts") or {}
    declared = {"hold": sum(1 for e in entries if e.get("severity") == "hold"),
                "note": sum(1 for e in entries if e.get("severity") == "note"),
                "fail": sum(1 for e in entries if e.get("severity") == "fail")}
    for field, actual in declared.items():
        if field in counts and counts[field] != actual:
            _defect(defects, "V-COVERAGE-COUNT", "$.counts." + field,
                    "expected-holds baseline declares %r but its own lists carry %d"
                    % (counts[field], actual))
    for entry in check.get("holds") or []:
        if not _is_text(entry.get("detail")):
            _defect(defects, "V-PROV-MISSING", "$.holds",
                    "hold %s at %s carries no pinned detail"
                    % (entry.get("id"), entry.get("where")))
    observed_fails = [f for f in findings if f.get("severity") in ("fail", "error")]
    if observed_fails:
        notes.append({"note": "%d fail/error finding(s) in the artifact against a "
                              "fail-empty baseline" % len(observed_fails)})


def validate_typed_packet(doc, packet_path=None, reader_path=None,
                          expected_holds=None, families=None, exact=False, root=None,
                          expected_spec=None, projection_path=None,
                          expected_gate=None, artifact_path=None):
    """One verdict over one typed-packet document (see module docstring)."""
    try:
        shape, labels, findings, stats, document = _extract(doc)
    except CouldNotEvaluate as exc:
        return {"exit": 2, "ok": False, "envelope": str(exc), "defects": [],
                "observed": None, "expected": None, "provenance": {}}
    defects, notes = [], []
    check = None
    if expected_spec is not None:
        try:
            expected_holds, families, exact, check = expected_from_spec(expected_spec)
        except CouldNotEvaluate as exc:
            return {"exit": 2, "ok": False, "envelope": str(exc), "defects": [],
                    "observed": None, "expected": None, "provenance": {}}
    _schema_defects(labels, defects)
    _channel_defects(labels, findings, defects)
    if shape == "view":
        _view_defects(document, [l for l in labels if l in (document.get("sound_channel") or [])],
                      [l for l in labels if l in (document.get("off_channel") or [])], defects)
    if shape == "typed-packet":
        _typed_channel_defects(document, document.get("typed_channel") or [],
                               findings, defects)
    if shape == "typed-flow":
        _typed_flow_defects(document, defects, notes, expected_gate, root, artifact_path)
    hard, matched, missing, phantom = _hold_defects(
        labels, findings, defects, expected_holds, families, exact,
        include_notes=check is not None)
    _expected_counts_defects(check, expected_holds or [], findings, defects, notes)
    provenance = _provenance_defects(doc, defects, packet_path, reader_path, root, notes,
                                     shape, projection_path)
    observed = _coverage_defects(doc, labels, findings, defects, stats)
    defects.sort(key=lambda d: (d["code"], str(d["where"]), d["detail"]))
    exit_code = 2 if any(d["code"] == "V-SCHEMA-SEVERITY" for d in defects) else (
        1 if defects else 0)
    return {
        "exit": exit_code,
        "ok": exit_code == 0,
        "envelope": {"shape": shape, "labels": len(labels), "findings": len(findings),
                     "hard": len(hard)},
        "defects": defects,
        "observed": observed,
        "hold_set": sorted([{"code": f.get("id"), "where": f.get("where"),
                             "severity": f.get("severity")} for f in hard],
                           key=lambda h: (str(h["code"]), str(h["where"]))),
        "expected": {"declared": len(expected_holds or []), "matched": matched,
                     "missing": missing, "phantom": phantom,
                     "families": list(families or []), "exact": bool(exact)},
        "provenance": provenance,
        "notes": notes,
    }


def report(result, stream=sys.stdout):
    if result["exit"] == 2:
        print("could-not-evaluate: %s" % result["envelope"], file=stream)
        return 2
    for defect in result["defects"]:
        print("DEFECT %s: [%s/%s] %s — %s"
              % (defect["code"], defect["severity"], defect["class"],
                 defect["where"], defect["detail"]), file=stream)
    envelope = result["envelope"]
    print("envelope: %s shape, %d labels, %d findings (%d hard)"
          % (envelope["shape"], envelope["labels"], envelope["findings"], envelope["hard"]),
          file=stream)
    expected = result["expected"]
    if expected["declared"]:
        print("expected hold set: declared=%d matched=%d missing=%d phantom=%d families=%s exact=%s"
              % (expected["declared"], len(expected["matched"]), len(expected["missing"]),
                 len(expected["phantom"]), expected["families"], expected["exact"]),
              file=stream)
    for note in result["notes"]:
        print("NOTE %s" % note["note"], file=stream)
    print("defects=%d exit=%d" % (len(result["defects"]), result["exit"]), file=stream)
    return result["exit"]


# ---------------------------------------------------------------------------
# controls
# ---------------------------------------------------------------------------

def _fixture():
    """A minimal well-formed projection: one owed form, named hold, matching
    counts, provenance bound to scratch files the selftest writes."""
    label = {"id": "GAR-01", "owner": "11-costumes", "label_id": "LEX-GAR-01",
             "kind": "translated-label", "text": "winter valley coat", "script": "Latn",
             "representation": "english-gloss", "scheme": None, "status": "to-verify",
             "issues": [{"field": "scheme", "reason": "english-gloss needs no scheme"}]}
    hold = {"id": FORM_HOLD, "code": FORM_HOLD, "where": "GAR-01",
            "detail": "label_id LEX-GAR-01 has no supplied native/borrowed form",
            "severity": "hold"}
    return {"typed_labels": {"stats": {"labels": 1, "hold": 1, "fail": 0}, "labels": [label]},
            "findings": [hold],
            "coverage": {"typed_labels": 1, "labels_by_kind": {"translated-label": 1},
                         "findings_total": 1, "findings_hold_or_fail": 1},
            "assembly": {"packet": "packet.yml", "packet_sha256": "0" * 64,
                         "reader": "reader.py", "reader_sha256": "1" * 64}}


def _view_fixture(packet_sha, live_sha):
    """A minimal well-formed view: one off-channel owed form, one supplied sound
    form, named holds and the derived hold_set, consistent stats."""
    owed = {"id": "GAR-01", "owner": "11-costumes", "label_id": "LEX-GAR-01",
            "kind": "translated-label", "text": "winter valley coat", "script": "Latn",
            "representation": "english-gloss", "scheme": None, "status": "to-verify",
            "issues": [{"field": "scheme", "reason": "english-gloss needs no scheme"}]}
    sound = {"id": "L-09", "owner": "05-lexicon", "kind": "native-form", "text": "kas",
             "script": "Latn", "representation": "editorial-romanization",
             "scheme": "d2-roman", "status": "supplied", "issues": []}
    hold = {"id": FORM_HOLD, "code": FORM_HOLD, "where": "GAR-01",
            "detail": "label_id LEX-GAR-01 has no supplied native/borrowed form",
            "severity": "hold"}
    return {"sound_channel": [sound], "off_channel": [owed],
            "named_holds": [hold], "hold_set": ["%s:%s" % (hold["id"], hold["where"])],
            "findings": [hold],
            "provenance": {"generator": "tools/d2-typed-labels.py",
                           "packet": "packet.yml", "packet_sha256": packet_sha,
                           "live_packet_sha256": live_sha,
                           "stale": packet_sha != live_sha},
            "stats": {"labels": 2, "sound_channel": 1, "off_channel": 1, "holds": 1,
                      "by_kind": {"native-form": 1, "translated-label": 1},
                      "synthesized_holds": 0}}


def _codes(result):
    return sorted({d["code"] for d in result.get("defects", [])})


def selftest():
    checks = []
    live_artifact = pathlib.Path(__file__).resolve().parents[2] / "examples/culture-d2/typed-labels.d2.yml"
    live_view = (pathlib.Path(__file__).resolve().parents[2]
                 / ".scratch/d04/view-live-a.json")

    def check(name, condition, detail=""):
        checks.append({"check": name, "ok": bool(condition), "detail": detail})

    check("vocab.every_defect_code_declared",
          all(code in V_CODES for code in V_CODES), "table v1")

    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        packet = tmp / "packet.yml"
        packet.write_text("name: fixture\n")
        reader = tmp / "reader.py"
        reader.write_text("# fixture\n")
        doc = _fixture()
        doc["assembly"]["packet"] = packet.name
        doc["assembly"]["packet_sha256"] = _sha256(packet)
        doc["assembly"]["reader"] = reader.name
        doc["assembly"]["reader_sha256"] = _sha256(reader)
        expected = [{"code": FORM_HOLD, "where": "GAR-01", "referent": "LEX-GAR-01"}]

        def run(document, **kwargs):
            kwargs.setdefault("root", str(tmp))
            return validate_typed_packet(document, **kwargs)

        ok = run(doc, expected_holds=expected, families=[FORM_HOLD], exact=True)
        check("positive.fixture_is_well_formed", ok["exit"] == 0, json.dumps(ok["defects"]))
        check("positive.hold_set_matched_exactly",
              ok["expected"]["missing"] == [] and ok["expected"]["phantom"] == [],
              json.dumps(ok["expected"]))
        check("positive.deterministic",
              json.dumps(run(doc, expected_holds=expected, families=[FORM_HOLD],
                             exact=True), sort_keys=True)
              == json.dumps(ok, sort_keys=True))

        def mutated(change, base=None, **kwargs):
            copy = json.loads(json.dumps(base if base is not None else doc))
            change(copy)
            return run(copy, **kwargs)

        cases = (
            ("neg.schema_field",
             lambda d: d["typed_labels"]["labels"][0].pop("status"),
             {}, "V-SCHEMA-FIELD"),
            ("neg.schema_kind",
             lambda d: d["typed_labels"]["labels"][0].update(kind="translated"),
             {}, "V-SCHEMA-KIND"),
            ("neg.schema_duplicate_id",
             lambda d: d["typed_labels"]["labels"].append(
                 dict(d["typed_labels"]["labels"][0], label_id="LEX-GAR-01")),
             {}, "V-SCHEMA-ID"),
            ("neg.null_reason_dropped",
             lambda d: d["typed_labels"]["labels"][0].update(issues=[]),
             {}, "V-SCHEMA-NULL-REASON"),
            ("neg.channel_translated_supplied",
             lambda d: d["typed_labels"]["labels"][0].update(status="supplied"),
             {}, "V-CHANNEL-TRANSLATED-SUPPLIED"),
            ("neg.channel_identity",
             lambda d: (d["typed_labels"]["labels"].append(
                 {"id": "L-01", "owner": "05-lexicon", "label_id": "LEX-GAR-01",
                  "kind": "native-form", "text": "kas", "script": "Latn",
                  "representation": "editorial-romanization", "scheme": "d2-roman",
                  "status": "supplied", "issues": []}),
                 d["typed_labels"]["labels"].append(
                 {"id": "L-02", "owner": "05-lexicon", "label_id": "LEX-GAR-01",
                  "kind": "native-form", "text": "kes", "script": "Latn",
                  "representation": "editorial-romanization", "scheme": "d2-roman",
                  "status": "supplied", "issues": []})),
             {}, "V-CHANNEL-IDENTITY"),
            ("neg.channel_translation_identity",
             lambda d: (d["typed_labels"]["labels"].append(
                 {"id": "L-03", "owner": "05-lexicon", "kind": "native-form",
                  "text": "winter valley coat", "script": "Latn",
                  "representation": "editorial-romanization", "scheme": "d2-roman",
                  "status": "supplied", "issues": []})),
             {}, "V-CHANNEL-TRANSLATION-IDENTITY"),
            ("neg.channel_phon_names_translated",
             lambda d: d["findings"].append(
                 {"id": "D2L-NATIVE", "code": "PHON-INVENTORY", "where": "GAR-01",
                  "detail": "symbol outside the declared inventory", "severity": "fail"}),
             {}, "V-CHANNEL-PHON-NAME"),
            ("neg.hold_owed_missing",
             lambda d: d.update(findings=[],
                                coverage=dict(d["coverage"], findings_total=0,
                                              findings_hold_or_fail=0)),
             {}, "V-HOLD-OWED"),
            ("neg.hold_orphan",
             lambda d: d["findings"][0].update(where="GAR-99"),
             {}, "V-HOLD-ORPHAN"),
            ("neg.hold_unnamed",
             lambda d: d["findings"][0].update(code="SOMETHING-ELSE", id="SOMETHING-ELSE"),
             {}, "V-HOLD-UNNAMED"),
            ("neg.hold_launder",
             lambda d: d.update(findings=[]),
             {"expected_holds": expected, "families": [FORM_HOLD], "exact": True},
             "V-HOLD-LAUNDER"),
            ("neg.hold_phantom",
             lambda d: d["findings"].append(
                 {"id": FORM_HOLD, "code": FORM_HOLD, "where": "GAR-07",
                  "detail": "label_id LEX-GAR-07 has no supplied native/borrowed form",
                  "severity": "hold"}),
             {"expected_holds": expected, "families": [FORM_HOLD], "exact": True},
             "V-HOLD-PHANTOM"),
            ("neg.coverage_count",
             lambda d: d["coverage"].update(findings_total=99),
             {}, "V-COVERAGE-COUNT"),
            ("neg.provenance_missing",
             lambda d: d["assembly"].update(packet_sha256="nope"),
             {}, "V-PROV-MISSING"),
            ("neg.provenance_drift",
             lambda d: d["assembly"].update(packet_sha256="f" * 64),
             {}, "V-PROV-PACKET-DRIFT"),
            ("neg.provenance_path",
             lambda d: d.update(canon="/home/someone/lane/scratch"),
             {}, "V-PROV-PATH"),
        )
        for name, change, kwargs, code in cases:
            result = mutated(change, **kwargs)
            check(name, code in _codes(result),
                  "want=%s got=%s" % (code, _codes(result)))

        for name, envelope, message in (
                ("neg.envelope_not_mapping", [], "V-ENVELOPE"),
                ("neg.envelope_no_section", {"findings": []}, "V-ENVELOPE"),
                ("neg.envelope_bad_label", {"typed_labels": [1]}, "V-ENVELOPE")):
            result = validate_typed_packet(envelope)
            check(name, result["exit"] == 2 and message in result["envelope"],
                  json.dumps(result["envelope"]))

        allowed_phon = mutated(lambda d: d["findings"].append(
            {"id": "D2L-NATIVE", "code": "PHON-INVENTORY", "where": "L-09",
             "detail": "symbol outside the declared inventory", "severity": "hold"}))
        check("ctrl.phon_on_a_native_form_is_not_a_channel_defect",
              "V-CHANNEL-PHON-NAME" not in _codes(allowed_phon), _codes(allowed_phon))

        # ---- the view shape -------------------------------------------------
        view = _view_fixture(_sha256(packet), _sha256(packet))
        view_ok = run(view)
        check("view.positive_is_well_formed", view_ok["exit"] == 0,
              json.dumps(view_ok["defects"]))
        check("view.channels_recognised",
              view_ok["envelope"]["shape"] == "view"
              and view_ok["envelope"]["labels"] == 2, json.dumps(view_ok["envelope"]))

        view_cases = (
            ("view.neg.translated_on_sound_channel",
             lambda d: (d["off_channel"].remove(d["off_channel"][0]),
                        d["sound_channel"].append(dict(
                            d["off_channel"][0] if d["off_channel"] else {},
                            kind="translated-label", status="to-verify"))),
             "V-VIEW-SOUND-MEMBER"),
            ("view.neg.disjointness",
             lambda d: d["sound_channel"].append(dict(d["off_channel"][0])),
             "V-VIEW-DISJOINT"),
            ("view.neg.hold_set_erased",
             lambda d: d.update(hold_set=[]),
             "V-VIEW-HOLDSET"),
            ("view.neg.named_holds_drop",
             lambda d: d.update(named_holds=[]),
             "V-VIEW-HOLD-DISJOINT"),
            ("view.neg.stats_inflated",
             lambda d: d["stats"].update(holds=99),
             "V-VIEW-STATS"),
            ("view.neg.stale_flag_laundered",
             lambda d: (d["provenance"].update(packet_sha256="a" * 64, stale=False)),
             "V-VIEW-PROVENANCE"),
            ("view.neg.stale_declared_is_a_hold",
             lambda d: (d["provenance"].update(packet_sha256="a" * 64, stale=True)),
             "V-PROV-PACKET-DRIFT"),
        )
        for name, change, code in view_cases:
            result = mutated(change, base=view)
            check(name, code in _codes(result),
                  "want=%s got=%s" % (code, _codes(result)))

        stale_view = mutated(lambda d: d["provenance"].update(packet_sha256="a" * 64,
                                                            stale=True),
                             base=view)
        check("view.neg.stale_view_is_a_named_hold",
              "V-PROV-PACKET-DRIFT" in _codes(stale_view)
              and any(d["severity"] == "hold" for d in stale_view["defects"]
                      if d["code"] == "V-PROV-PACKET-DRIFT"),
              _codes(stale_view))

        spec = {"schema": "kotodama-typed-pipeline-holds-v1",
                "counts": {"hold": 1, "note": 0, "fail": 0},
                "holds": [{"id": FORM_HOLD, "severity": "hold", "where": "GAR-01",
                           "detail": "label_id LEX-GAR-01 has no supplied native/borrowed form"}],
                "notes": []}
        spec_ok = run(view, expected_spec=spec)
        check("expected.v1_spec_matches", spec_ok["exit"] == 0, json.dumps(spec_ok["defects"]))
        swap_doc = json.loads(json.dumps(view))
        swap_doc["findings"][0]["severity"] = "fail"
        swap_doc["named_holds"] = list(swap_doc["findings"])
        swapped = run(swap_doc, expected_spec=spec)
        check("expected.severity_swap_is_named",
              "V-HOLD-SEVERITY-SWAP" in _codes(swapped), _codes(swapped))
        laundered = json.loads(json.dumps(view))
        laundered["findings"][0]["severity"] = "note"
        laundered["named_holds"] = []
        laundered["hold_set"] = []
        laundered["stats"]["holds"] = 0
        launder_result = run(laundered, expected_spec=spec)
        check("expected.launder_to_note_is_named",
              "V-HOLD-OWED" in _codes(launder_result) and
              bool({"V-HOLD-SEVERITY-SWAP", "V-HOLD-LAUNDER"} & set(_codes(launder_result))),
              _codes(launder_result))

        # ---- the typed-packet (routing-table) shape --------------------------
        typed_packet = {
            "name": "fixture packet",
            "costumes": [{"id": "GAR-01", "garment_gloss": "winter valley coat"}],
            "lexicon": [{"id": "L-26", "term": "kas"}],
            "names": [{"id": "NM-01", "name": "sara"}],
            "typed_channel": [{"record": "GAR-01", "kind": "translated-label",
                               "label_id": "LEX-GAR-01", "owner": "11-costumes",
                               "source_field": "garment",
                               "off_channel_field": "garment_gloss",
                               "channel": "off-sound-and-identity", "hold": FORM_HOLD}],
            "typed_findings": [{"id": FORM_HOLD, "code": FORM_HOLD, "where": "GAR-01",
                                "detail": "label_id LEX-GAR-01 has no supplied native/borrowed form",
                                "severity": "hold"}],
            "assembly": {"packet": "packet.yml", "packet_sha256": _sha256(packet),
                         "projection": "packet.yml", "projection_sha256": _sha256(packet),
                         "adapter_sha256": "b" * 64},
        }
        tp = run(typed_packet)
        check("typed_packet.positive_is_well_formed", tp["exit"] == 0,
              json.dumps(tp["defects"]))
        check("typed_packet.shape_recognised",
              tp["envelope"]["shape"] == "typed-packet", json.dumps(tp["envelope"]))
        tp_expected = run(typed_packet, expected_spec=spec)
        check("typed_packet.baseline_matches", tp_expected["exit"] == 0,
              json.dumps(tp_expected["defects"]))
        tp_cases = (
            ("typed_packet.neg.row_field_missing",
             lambda d: d["typed_channel"][0].pop("hold"),
             "V-ROUTE-ROW"),
            ("typed_packet.neg.row_kind",
             lambda d: d["typed_channel"][0].update(kind="gloss"),
             "V-ROUTE-KIND"),
            ("typed_packet.neg.row_channel",
             lambda d: d["typed_channel"][0].update(channel="sound"),
             "V-ROUTE-CHANNEL"),
            ("typed_packet.neg.field_not_moved",
             lambda d: d["typed_channel"][0].update(off_channel_field="garment"),
             "V-ROUTE-FIELD"),
            ("typed_packet.neg.checked_field_still_present",
             lambda d: d["costumes"][0].update(garment="winter valley coat"),
             "V-ROUTE-FIELD"),
            ("typed_packet.neg.row_orphan",
             lambda d: d["typed_channel"][0].update(record="GAR-99"),
             "V-ROUTE-ORPHAN"),
            ("typed_packet.neg.hold_dropped",
             lambda d: d.update(typed_findings=[]),
             "V-ROUTE-HOLD"),
            ("typed_packet.neg.pins_drifted",
             lambda d: d["assembly"].update(packet_sha256="f" * 64),
             "V-PROV-PACKET-DRIFT"),
        )
        for name, change, code in tp_cases:
            result = mutated(change, base=typed_packet)
            check(name, code in _codes(result),
                  "want=%s got=%s" % (code, _codes(result)))

        # ---- the flow packet (typed_view) shape ------------------------------
        artifact = tmp / "packet.d2.typed.yml"
        artifact.write_text("name: fixture typed packet\n")
        flow = {
            "costumes": [{"id": "GAR-01", "garment": "winter valley coat",
                          "compare_only": True, "owed_form": "LEX-GAR-01",
                          "typed_label_kind": "translated-label"}],
            "lexicon": [{"id": "L-09", "term": "kas"}],
            "names": [],
            "typed_view": {"generator": "tools/typed-gate-flow.py",
                           "source_packet": "packet.yml",
                           "source_packet_sha256": _sha256(packet),
                           "rules": ["translated-label: compare_only, never sound-tested",
                                     "owed native form: carried by name in owed_form"],
                           "sound_channel": {"on": [], "off": ["GAR-01"], "untyped": []}},
            "assembly": {"generator": "tools/assemble-d2.py"},
        }
        gate_spec = {"schema": "kotodama-typed-gate-expected-v1",
                     "typed_packet": str(artifact), "typed_packet_sha256": _sha256(artifact),
                     "off_sound_channel": ["GAR-01"], "owed_slots": ["LEX-GAR-01"],
                     "expected_findings": [
                         {"code": FORM_HOLD, "severity": "hold", "where": "LEX-GAR-01",
                          "record": "GAR-01",
                          "detail": "label_id LEX-GAR-01 has no supplied native/borrowed form"}]}
        flow_ok = run(flow, expected_gate=gate_spec, artifact_path=str(artifact))
        check("flow.positive_is_well_formed", flow_ok["exit"] == 0,
              json.dumps(flow_ok["defects"]))
        check("flow.shape_recognised",
              flow_ok["envelope"]["shape"] == "typed-flow", json.dumps(flow_ok["envelope"]))
        flow_cases = (
            ("flow.neg.bucket_type",
             lambda d: d["typed_view"]["sound_channel"].update(off="GAR-01"),
             {}, "V-ROUTE-ROW"),
            ("flow.neg.disjoint_buckets",
             lambda d: d["typed_view"]["sound_channel"].update(on=["GAR-01"]),
             {}, "V-VIEW-DISJOINT"),
            ("flow.neg.off_without_compare_only",
             lambda d: d["costumes"][0].pop("compare_only"),
             {}, "V-ROUTE-FIELD"),
            ("flow.neg.off_without_owed_form",
             lambda d: d["costumes"][0].pop("owed_form"),
             {}, "V-ROUTE-HOLD"),
            ("flow.neg.untyped_marked",
             lambda d: (d["typed_view"]["sound_channel"].update(untyped=["GAR-01"]),
                        d["typed_view"]["sound_channel"].update(off=[]),
                        d["costumes"][0].update(compare_only=False, owed_form=None)),
             {}, "V-ROUTE-KIND"),
            ("flow.neg.source_pin_drift",
             lambda d: d["typed_view"].update(source_packet_sha256="f" * 64),
             {}, "V-PROV-PACKET-DRIFT"),
        )
        for name, change, kwargs, code in flow_cases:
            copy = json.loads(json.dumps(flow))
            change(copy)
            result = run(copy, expected_gate=gate_spec, artifact_path=str(artifact))
            check(name, code in _codes(result),
                  "want=%s got=%s" % (code, _codes(result)))
        gate_cases = (
            ("flow.neg.expected_off_set",
             lambda g: g.update(off_sound_channel=[]),
             "V-VIEW-STATS"),
            ("flow.neg.expected_owed_slots",
             lambda g: g.update(owed_slots=["LEX-GAR-99"]),
             "V-COVERAGE-COUNT"),
            ("flow.neg.expected_fail_finding",
             lambda g: g["expected_findings"].append(
                 {"code": "D2L-DATA", "severity": "fail", "where": "GAR-01",
                  "detail": "fixture fail"}),
             "V-HOLD-UNNAMED"),
            ("flow.neg.expected_hold_outside_off",
             lambda g: g["expected_findings"][0].update(record="GAR-99"),
             "V-HOLD-ORPHAN"),
            ("flow.neg.typed_packet_pin",
             lambda g: g.update(typed_packet_sha256="0" * 64),
             "V-PROV-PACKET-DRIFT"),
        )
        for name, change, code in gate_cases:
            spec_copy = json.loads(json.dumps(gate_spec))
            change(spec_copy)
            result = run(flow, expected_gate=spec_copy, artifact_path=str(artifact))
            check(name, code in _codes(result),
                  "want=%s got=%s" % (code, _codes(result)))

    packet_shape = {"typed_labels": [
        {"id": "L-09", "owner": "05-lexicon", "kind": "native-form", "text": "kas",
         "script": "Latn", "representation": "editorial-romanization",
         "scheme": "d2-roman", "status": "supplied", "issues": []}], "findings": []}
    shaped = validate_typed_packet(packet_shape)
    check("ctrl.packet_shape_without_assembly_evaluates_clean",
          shaped["exit"] == 0 and shaped["envelope"]["shape"] == "packet",
          json.dumps(shaped["defects"]))

    if live_artifact.exists():
        doc = json.loads(live_artifact.read_text(encoding="utf-8"))
        root = live_artifact.resolve().parents[2]
        result = validate_typed_packet(doc, root=root)
        check("live.projection_no_defect_except_provenance_drift",
              set(_codes(result)) <= {"V-PROV-PACKET-DRIFT", "V-PROV-READER-DRIFT"},
              _codes(result))
        ten = [{"code": FORM_HOLD, "where": "GAR-%02d" % n, "referent": "LEX-GAR-%02d" % n}
               for n in range(1, 11)]
        exact = validate_typed_packet(doc, root=root, expected_holds=ten,
                                      families=[FORM_HOLD], exact=True)
        check("live.ten_form_holds_match_exactly",
              exact["expected"]["missing"] == [] and exact["expected"]["phantom"] == [],
              json.dumps(exact["expected"], sort_keys=True))
    else:
        check("live.artifact_present", False, str(live_artifact))

    if live_view.exists():
        view = json.loads(live_view.read_text(encoding="utf-8"))
        root = live_view.resolve().parents[2]
        result = validate_typed_packet(view, root=root)
        check("live.view_no_defect_except_provenance_drift",
              set(_codes(result)) <= {"V-PROV-PACKET-DRIFT"},
              _codes(result))
    else:
        check("live.view_absent_skipped", True, str(live_view))

    failed = [c for c in checks if not c["ok"]]
    print("selftest: %d/%d checks passed" % (len(checks) - len(failed), len(checks)))
    for item in failed:
        print("FAIL %s — %s" % (item["check"], item["detail"]))
    return 0 if not failed else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", metavar="TYPED_PACKET",
                        help="the typed-packet document to validate")
    parser.add_argument("--packet", help="live packet path to hash-compare")
    parser.add_argument("--projection", help="live projection path to hash-compare "
                                             "(typed-packet shape's projection_sha256)")
    parser.add_argument("--reader", help="live gate reader path to hash-compare")
    parser.add_argument("--expect", help="expected-holds JSON (flat spec or holds-v1 baseline)")
    parser.add_argument("--root", help="repo root for relative provenance paths")
    parser.add_argument("--yaml", action="store_true",
                        help="read the document with the lane's YAML-subset reader "
                             "(the typed packet is YAML, the projection and view are JSON)")
    parser.add_argument("--yaml-reader",
                        help="path to the YAML-subset reader (default: the costume-era "
                             "consistency gate under --root)")
    parser.add_argument("--json", action="store_true", help="print one JSON verdict")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.check:
        parser.error("--check TYPED_PACKET or --selftest required")
    try:
        text = pathlib.Path(args.check).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print("could-not-evaluate: V-ENVELOPE: %s" % exc, file=sys.stderr)
        return 2
    if args.yaml:
        base = pathlib.Path(args.root or ".")
        reader = pathlib.Path(
            args.yaml_reader or base / "tools/gates/costume-era-consistency-gate.py")
        try:
            namespace = runpy.run_path(str(reader))
            doc = namespace["parse_packet"](text)
        except Exception as exc:  # the reader's Malformed and any read error
            print("could-not-evaluate: V-ENVELOPE: %s: %s" % (reader, exc), file=sys.stderr)
            return 2
    else:
        try:
            doc = json.loads(text)
        except (json.JSONDecodeError, ValueError) as exc:
            print("could-not-evaluate: V-ENVELOPE: %s" % exc, file=sys.stderr)
            return 2
    spec, gate = None, None
    if args.expect:
        try:
            spec = json.loads(pathlib.Path(args.expect).read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            print("could-not-evaluate: V-ENVELOPE: %s" % exc, file=sys.stderr)
            return 2
        if isinstance(spec, dict) and isinstance(spec.get("schema"), str) \
                and spec["schema"].startswith("kotodama-typed-gate-expected"):
            gate, spec = spec, None
    result = validate_typed_packet(doc, packet_path=args.packet, reader_path=args.reader,
                                   root=args.root, expected_spec=spec,
                                   projection_path=args.projection,
                                   expected_gate=gate, artifact_path=args.check)
    if args.json:
        print(json.dumps(result, sort_keys=True, ensure_ascii=False))
        return result["exit"]
    return report(result)


if __name__ == "__main__":
    sys.exit(main())
```

## 5. Limits, interface notes, and open items

- **Not a gate, not canon.** The validator emits preconditions and defect codes; it never rewrites
  the artifact, never rules on a label's canon status, and its exit 0 is not a "culture is clean"
  reading. The ten owed forms stay open design debt either way.
- **What it does not check.** It does not re-derive the adapters' routing (a routing row that is
  well-formed but semantically wrong still passes), it does not byte-compare the pinned `detail`
  prose against a baseline (it checks presence, severity and that each hold names its record and its
  owed slot; the byte-level detail pin remains the gate's own leg and the freeze's), it does not
  verify that a `native-form`'s text respects the phonology inventory, and it does not execute the
  gates — the L2 channel differential is not this block's business.
- **Key names are read, not decreed.** The flow checks assume the landed flow's own names
  (`typed_view` / `rules` / `sound_channel.{on,off,untyped}` / `compare_only` / `owed_form` /
  `typed_label_kind`, `tools/typed-gate-flow.py` `5758e315…`, as read 22:19:16Z). A rename is a
  re-read event for this block, not a silent pass.
- **Two conventions the validator tolerates, deliberately.** (1) `hold_set` is accepted rendered by
  either the finding's `id` (D2L class) or its `code` (shard code), but must use one key
  consistently — D04's view renders `code:where`, the design's §4.4 keys on `(id, severity, where)`.
  (2) Form holds in an expected baseline may key the owed **slot** in `where` with a separate
  `record` field (the landed `typed-gate.expected.json` does) or the **record** in `where` (the
  design's §4.2 table) — both are accepted; a mixed document is a defect. The integrator should pin
  one convention per artifact when the ledger is written, not leave two.
- **Seat-map mismatch (report, do not absorb).** `reports/round-11/depth/design.md` §7 maps seat
  D07 to "projection re-pin procedure + receipt (§5.1), no new file", while this seat's dispatch
  targets a validator and this fragment delivers one. Both legs exist: the validator is the
  executable freshness check (it caught the stale pin and now accepts the re-pinned state), and the
  re-pin procedure itself was executed by a sibling seat. The parent should reconcile the seat map
  so the ledger does not credit one seat for two different artifacts.
- **Block destination is the integrator's call.** The block is destination-neutral and stdlib-only
  (`argparse`, `hashlib`, `json`, `pathlib`, `re`, `runpy`, `sys`, `tempfile`). Sensible placements:
  a pre-read precondition inside the typed-pipeline gate, or a small `tools/` checker the flow calls
  before the gates. Either way it is a single-writer file; this seat writes no tool.
- **Standing environment defect.** `/tmp` inode exhaustion (round-8 records) — every scratch command
  here ran with `TMPDIR=$PWD/.scratch`.
- **Open / to-verify.** (1) The R11-D04 view is scratch, pinned as read (`0dfdf8d7…`); its
  `stale: true` receipt is conditional on that file. (2) The D04 routing-table variant's missing
  note (§3b). (3) If a later re-pin moves any pin above, re-derive — never force these digests.

## 6. Sources and locators

Repo-relative; sha256 as read 2026-10-17T22:06–22:19:16Z at revision `e3ef1719…` (no commit made by
this seat; `git status --porcelain` showed sibling round-11 scratch/untracked paths and sibling
edits under `reports/round-*/validation.json`, none of them this seat's).

| path | sha256 | used for |
|---|---|---|
| `examples/culture-d2/typed-labels.d2.yml` | `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` (was `e70ba147…` pre-re-pin) | the projection under validation (58 labels, 16 findings: 15 holds + 1 note, 0 fails) |
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` | live base packet pin |
| `examples/culture-d2/packet.d2.typed.yml` | `e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb` | the landed typed packet (typed_view variant): 10 off records, all `compare_only` + `owed_form`; validates clean |
| `examples/culture-d2/typed-gate.expected.json` | `7ed597317b32b238d880af0a602fcbfa1ffd92608008879f049db9fd02aa03aa` | the landed baseline (`kotodama-typed-gate-expected-v1`): 16 findings, off set, owed slots, gate verdicts |
| `tools/typed-gate-flow.py` | `5758e315593bb818dbf38c3c3ed7f79eb9ea555955331fadab4b50b2faa92075` | the flow that emits the typed packet; its `typed_view` names the checks |
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` | the emitter; `--json` derives the §4.5 baseline spec; `--check` exits 1 pre-re-pin, 0 post-re-pin |
| `tools/gates/costume-era-consistency-gate.py` | `e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f` | the lane's YAML-subset reader used by `--yaml` |
| `reports/round-11/depth/design.md` | as read (round-11 scratch) | the wiring design: §1.4 (stale pin), §2.2 (adapter), §3.1 (L1–L4), §4 (expected hold set), §5.1 (re-pin), §6 (D17–D19), §7 (seat map) |
| `reports/round-8/depth/design-spec.md` | `84e4b4c19b0310f138b5bb53f3e4b3672cdc493fc83b555d912a9630984cc751` | §1.2 label record, §1.5 the ten owed forms, §5 D2/D4, §6 finding ids |
| `reports/round-8/depth/skill-table-draft.md` §7 | as read | the channel/routing limits the validator's channel rules encode |
| `.scratch/d04/view-live-a.json` (R11-D04 scratch) | `0dfdf8d7e261fdeedc41f5452a91e97088f52b7bd011dc439a1cd8ef0f09457f` | the read-side view shape; `provenance.stale: true` |
| `.scratch/d04/packet.d2.typed.yml` (R11-D04 scratch) | `5347a682eee3667c8d6fa224ff2597a5ec5c1a45a41bffea797325f2ea608ad9` | the routing-table variant and the §3b note discrepancy |
| `.scratch/d07/typed_packet_validator.py` (this shard's block, embedded §4) | `2daa106cf97b5765dbfaf8455d104580047ca96f7b416e420923cc664c14e9c3` | the artifact under test |
| `.scratch/d07/expected-holds-v1.json` | `815bfc6fa31e080c3f0ec62559407d96dbb4616723ccad6f38447fc879ed477a` | the projector-derived §4.5 baseline (counts `{hold: 15, note: 1, fail: 0}`) |
| `.scratch/d07/receipt-*.txt` | selftest `8a4c2f69…` (22:19:16Z) and `06e58287…` (22:11:54Z); projection `00792ea6…` and `27740619…`; flow packet `b069a7ad…`; routing-table packet `aa0b9f12…`; view `9d1f5838…`; negatives `1e857e2d…`; yaml control `728f5c7c…` | the receipts quoted in §2 |

No web retrievals were made for this shard; every statement above is a repo path, a command output,
or a scratch receipt with a stored hash. Counts carry their command and their stamp.
