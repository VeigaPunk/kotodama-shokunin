- Seat: D16 | executor | D | 2026-10-19 | baseline da68a6d

# D16 — second spare build seat: gap-fill across the D block

## 0. Gap audit and what this seat filled

At my dispatch time **no D-block fragment had landed** — `reports/round-34/depth/` did
not exist, and `find reports/round-34 -name 'D*.md'` returned nothing (command
output, 2026-10-19). Every D seat (D01–D20) therefore ran with its declared
dependencies (K01 scout, K02 repin census, P01 plan) absent.

So the largest unfilled gap is **the block's shared dependency**: the live-bytes
census and the precise stale set that D03/D04/D05/D07/D13/D18/D20 all consume and
that D02 needs in order to render anything correct. I filled that, and while
measuring it I found a **blocking defect in claim D's declared fix path** (§4) that
no seat's mission text names.

I did not attempt D01/D02/D05's deliverables (layout, rendered packet bytes, full
draft) — those are other seats' `out` paths.

**Status update (§7):** ten fragments landed after my dispatch and before my close
(D01–D04, D08, D10–D12, D14, D18). §4 is therefore convergent rather than novel —
D01, D02, D08 and D12 reached the same root cause independently — and §7 records what
that convergence changes: D10's 21-row census still omits the `CLAIMS_MAP` re-point,
and three seats propose three different names for the same new file. §0's "no fragment
had landed" describes my dispatch moment only.

## 1. Live-bytes census (durable; every value re-measured at da68a6d)

Command: `python3 -c` reads of the two live artifacts, plus `sha256sum` (all
commands listed in §8). Live numbers, with citations:

| quantity | live value | source |
|---|---|---|
| `typed_labels` | **82** | `examples/culture-d4/typed-labels.d4.yml:46` |
| `labels_by_kind.native-form` | **64** | `examples/culture-d4/typed-labels.d4.yml:37` |
| `labels_by_kind.translated-label` | **12** | `examples/culture-d4/typed-labels.d4.yml:38` |
| `labels_by_kind.borrowed-strata` | **6** | `examples/culture-d4/typed-labels.d4.yml:36` |
| `findings_total` | **12** | `examples/culture-d4/typed-labels.d4.yml:32` |
| `findings_hold_or_fail` | **12** | `examples/culture-d4/typed-labels.d4.yml:31` |
| `label_findings_hold` / `label_findings_fail` | **12** / **0** | `examples/culture-d4/typed-labels.d4.yml:34` / `:33` |
| `conflicts` | **0** | `examples/culture-d4/typed-labels.d4.yml:30` |
| `rank_quarantine_handles` | **0** | `examples/culture-d4/typed-labels.d4.yml:40` |
| `rank_rules_unresolved_items` | **0** | `examples/culture-d4/typed-labels.d4.yml:44` |
| `reconciliation_records` | **6** | `examples/culture-d4/typed-labels.d4.yml:45` |
| `typed_labels.stats` (nested) | `{"fail": 0, "hold": 12, "labels": 82}` | `examples/culture-d4/typed-labels.d4.yml:2865-2869` |
| `expected-holds.json#counts` | `{"hold": 12, "note": 0, "fail": 0}` | `examples/culture-d4/expected-holds.json:46-50` |
| hold rows | 12 rows, **all** `D2L-FORM-UNRESOLVED`, all severity `hold`; `notes` = `[]` (len 0) | `examples/culture-d4/expected-holds.json:51+` |
| `era_material_reconciliation.summary` | `{"by_code": {}, "by_severity": {}, "claims": 6, "findings": 0}` | `examples/culture-d4/typed-labels.d4.yml` (parsed) |
| `era_reconciliation.alias_rows` | **4** (E0–E3, all `confirmed`) | `examples/culture-d4/typed-labels.d4.yml` (parsed) |
| top-level `findings[]` | len **12**, severity `hold` ×12, id `D2L-FORM-UNRESOLVED` ×12 | `examples/culture-d4/typed-labels.d4.yml` (parsed) |

Live artifact digests (`sha256sum`, measured):

```
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182  examples/culture-d4/packet.d4.typed.yml
6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb  reports/round-30/handoff/declared-in-r6/packet.md
6633443d70ce44ed2bb43ab58aa60a1c98e4bbc79b2f577a63181c89dc16fd4e  reports/round-30/handoff/declared-in-r6/twin.json
ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0  reports/round-30/handoff/declared-in-r6/expected.json
6fe70c0c2b3a03ee82181a4906dc9670f73424c54efddec8fc632d213cca5d59  reports/round-30/handoff/declared-in-r6/freeze.txt
```

**Anchor-precision note for D04/D06/D20**: the `#stats` anchor used by
D4-CL05/06 resolves to a **nested** key, `typed_labels.stats`
(`:2865`, four spaces of indent inside the `typed_labels` block that closes at
`:2870`) — there is no top-level `stats`. A rewritten citation should say
`typed_labels.d4.yml#typed_labels.stats` rather than `#stats`.

## 2. The stale set is exactly 13 mismatches, and it must be **row-scoped**

Measured against the live values in §1, the current default pair asserts, inside
**D4-scoped rows only**:

```
reports/round-30/handoff/declared-in-r6/packet.md:148 [D4-CL05] typed_labels asserted=74 live=82
reports/round-30/handoff/declared-in-r6/packet.md:148 [D4-CL05] native-form asserted=56 live=64
reports/round-30/handoff/declared-in-r6/packet.md:148 [D4-CL05] findings_total asserted=16 live=12
reports/round-30/handoff/declared-in-r6/packet.md:148 [D4-CL05] findings_hold_or_fail asserted=15 live=12
reports/round-30/handoff/declared-in-r6/packet.md:148 [D4-CL05] stats.labels asserted=74 live=82   (×2 occurrences in the cell)
reports/round-30/handoff/declared-in-r6/packet.md:149 [D4-CL06] holds.hold asserted=15 live=12
reports/round-30/handoff/declared-in-r6/packet.md:149 [D4-CL06] holds.note asserted=1 live=0
reports/round-30/handoff/declared-in-r6/packet.md:150 [D4-CL07] conflicts asserted=4 live=0
reports/round-30/handoff/declared-in-r6/packet.md:150 [D4-CL07] rank_quarantine_handles asserted=3 live=0
reports/round-30/handoff/declared-in-r6/packet.md:152 [D4-CL09] conflicts asserted=4 live=0
reports/round-30/handoff/declared-in-r6/packet.md:152 [D4-CL09] rank_quarantine_handles asserted=3 live=0
reports/round-30/handoff/declared-in-r6/packet.md:152 [D4-CL09] rank_rules_unresolved_items asserted=13 live=0
```

This reproduces `reports/round-33/adj/A02-handoff.md:102-105` item for item and
extends it: A02 does not name the `stats.labels 74`, which sits in the **same cell**
as the *fresh* `hold 12` (`packet.md:148`). That mixed cell is worth noting for
D03: the replacement must fix `labels 74` → `82` while leaving `fail 0, hold 12`
untouched.

**The scoping rule (this is the trap).** The identical digits are legitimate
elsewhere in the same file. `examples/culture-d2/typed-labels.d2.yml` live reads
`typed_labels 58`, `native-form 46`, `findings_total 16`, `findings_hold_or_fail 15`,
`conflicts 4`, `rank_quarantine_handles 3`, `rank_rules_unresolved_items 13`
(`:46,:37,:32,:31,:30,:40,:44`) — so `packet.md:129` (D2-CL01: 58/46/16/15) and
`packet.md:266` (RD-D2-01: "58 labels, 15 holds") are **fresh, not stale**.
I verified this before filing: an un-scoped token scan over a freshly-repaired
packet produces **17 false positives**, 8 of them on D2-scoped rows
(`:129,:130,:301` and a decision-table row at `:284`). Any audit that is not
row-scoped will "fix" correct D2 numbers. See §5 control 3.

One rewrite is *not* a digit swap: in `D4-CL09` and `OQ-V3-05` the figures
13 / 3 / 4 are attributed to **D4's own coverage block**, which reads 0 / 0 / 0;
those three figures actually belong to the D2 projection and are already routed
correctly by `OQ-V2-03` (`packet.md:303`). The replacement text must re-attribute
them, not merely renumber them.

## 3. Twin parity: the twin is stale in exactly the same rows

`reports/round-30/handoff/declared-in-r6/twin.json` yields the **same 13
mismatches** in `claim_ledger` rows `D4-CL05`, `D4-CL06`, `D4-CL07`, `D4-CL09`
(e.g. `D4-CL05.statement` = "types 74 labels — 56 native-form … 16 findings of
which 15 are hold-or-fail"; `D4-CL09.uncertainty.basis` = "…unresolved rank items
13 … quarantine_handles 3 … conflicts 4"). `twin.json` carries a 27-row
`claim_ledger`, matching A02's 27-claim count. The twin is built from the same row
objects as the Markdown (`tools/exercise-handoff-e2e.py:2621`), so one fix covers both.

## 4. BLOCKING: claim D's declared fix path cannot clear the staleness

`after_required` says the new revision "regenerates the packet from the current
D2/D3/D4 artifacts". Measured, that does not work — and the reason is exact.

The renderer does **not** derive the twelve D4 claim rows from the live artifacts.
It copies them out of a **filed** file:

- `tools/exercise-handoff-e2e.py:184` — `CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"`
- `tools/exercise-handoff-e2e.py:2289-2294` — `v3_parse_claims_map()` reads that path and
  requires exactly 12 `### D4-CLnn` rows, then takes each row's `statement`,
  `u.basis` and `links` **verbatim** (`:2299-2307`; no numeric substitution anywhere).
- That file is filed round-20 bytes (clean at HEAD, last touched by commit `35b6797`)
  and carries the stale text at `:104` (D4-CL05: `typed_labels 74 … native-form 56 …
  findings_total 16, findings_hold_or_fail 15 … labels 74`), `:116` (D4-CL06:
  `hold 15, note 1, fail 0`), `:124` (D4-CL07: `conflicts (4), quarantine`), `:154`
  and `:158` (D4-CL09: 13 / 3 / 4).

Empirical proof — I rendered the packet in an **isolated `git archive` copy** (never
in-tree, defaults untouched, no `--freeze` inside the repo):

```
$ git archive HEAD | tar -x -C .scratch/d16/iso
$ cd .scratch/d16/iso && python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --freeze .../freezeout
froze .../freezeout: packet sha256 6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb
$ diff -q .scratch/d16/freezeout/packet.md reports/round-30/handoff/declared-in-r6/packet.md
(diff: none — byte-identical)
$ python3 -B .scratch/d16/d4_stale_audit.py .scratch/d16/freezeout/packet.md
STALE: 13 D4-scoped mismatches        # identical list to §2
```

**A fresh render today, from today's live artifacts, reproduces the filed r6 packet
byte for byte — all 13 stale figures inclusive.** So the packet is stale by
construction, and re-pinning the default pair to a re-rendered revision would
reproduce exactly the defect claim D exists to close.

`OQ-V3-05` has a **second, independent** stale source: it is a hard-coded literal in
the renderer, not read from the claims map —
`tools/exercise-handoff-e2e.py:3524-3531` (the only occurrence of "twelve form holds
+ three rank holds + one" in the tree). `CLAIMS_MAP:251` carries a differently-worded
copy of the same stale row.

### Consequence and the required fix surface (drafted for the integrator)

The only path to a live-accurate `declared-in-r7` is a **new claims map + re-point +
literal rewrite**, applied by the integrator — the same class of shared-file change as
the `:1933-1934` defaults, drafted here and never applied by me:

| # | surface | before | after |
|---|---|---|---|
| A | `tools/exercise-handoff-e2e.py:184` | `CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"` | `CLAIMS_MAP = "reports/round-34/handoff/claims-map.md"` |
| B | new file `reports/round-34/handoff/claims-map.md` | (does not exist) | the 12 D4 rows, same `### D4-CLnn — kind — status — \`state\`` header shape, with every number from §1; old r20 rows named **superseded**, never edited |
| C | `tools/exercise-handoff-e2e.py:2290` docstring | `"""The twelve D4 rows as filed in reports/round-20/handoff/claims-map.md."""` | re-pointed to the new path |
| D | `tools/exercise-handoff-e2e.py:2699-2700` intro literal | `…the twelve D4 rows are carried from \`reports/round-20/handoff/claims-map.md\`.` | new path (emits `packet.md:3`) |
| E | `tools/exercise-handoff-e2e.py:3524-3531` `OQ-V3-05` literal | `"D4's inherited and own holds stay open: twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts — kotodama; blocking for the affected D2 rank records and the six garment terms, not for this envelope"` | `"D4's own projection carries twelve form holds and zero rank holds, zero notes, zero unresolved rank items, zero quarantine handles and zero conflicts; the thirteen unresolved rank items, three quarantine handles and four conflicts are D2 normalization residuals, recorded under OQ-V2-03 and not re-attributed to D4 — kotodama; blocking for the affected D2 rank records and the six garment terms, not for this envelope"` (candidate; D04 owns the wording) |
| F | `tools/exercise-handoff-e2e.py:29-34` module docstring | names the r20 path | documentation only; re-point for consistency |

Note the cascade A causes (all re-derived automatically by the renderer's f-strings,
so no other hand edits): the manifest row `A-57` (`packet.md:95`, digest + size), the
`:113` digest line, and the §claims prose (`:2934` uses `f"{CLAIMS_MAP}"`); plus the
read-set count of 58 files and `freeze.txt`'s "read set: 58 files" if the file count
changes.

**Cross-refs for the integrator:** this surface is *not* in D10's mission text (which
scopes to K02's census of `declared-in-r6` pins), and K02's grep structurally cannot
find it — `CLAIMS_MAP` pins **round-20**, not r6. Whoever owns the re-pin cascade must
take A–E as **additional new rows**; D10's mission deserves this appended.

## 5. The audit instrument and its controls

D13's negative control (a) needs "your audit method" and D20 needs the stale-figure
scan; neither had a tool. Here is the runnable one — it reads live truth from the
delivered bytes, never from the packet, and exit-codes 0 clean / 1 stale / 2 usage:

```python
#!/usr/bin/env python3
"""D4 stale-figure audit (D16 gap-fill, round 34).  Row-scoped: only D4-scoped rows
are checked, because the same digits are legitimately fresh in D2-scoped rows."""
import json, re, sys
D4_LABELS = "examples/culture-d4/typed-labels.d4.yml"
D4_HOLDS  = "examples/culture-d4/expected-holds.json"

def live_values(root):
    labels = json.load(open(root + "/" + D4_LABELS))
    holds  = json.load(open(root + "/" + D4_HOLDS))
    cov, stats = labels["coverage"], labels["typed_labels"]["stats"]   # nested anchor
    em = labels["era_material_reconciliation"]["summary"]
    return {"typed_labels": cov["typed_labels"],
            "native-form": cov["labels_by_kind"]["native-form"],
            "findings_total": cov["findings_total"],
            "findings_hold_or_fail": cov["findings_hold_or_fail"],
            "stats.labels": stats["labels"],
            "holds.hold": holds["counts"]["hold"],
            "holds.note": holds["counts"]["note"],
            "conflicts": cov["conflicts"],
            "rank_quarantine_handles": cov["rank_quarantine_handles"],
            "rank_rules_unresolved_items": cov["rank_rules_unresolved_items"],
            "reconciliation_records": cov["reconciliation_records"],
            "era_material_claims": em["claims"]}

PROBES = [("typed_labels", r"typed_labels (\d+)"),
          ("native-form", r"native-form (\d+)"),
          ("findings_total", r"findings_total (\d+)"),
          ("findings_hold_or_fail", r"findings_hold_or_fail (\d+)"),
          ("holds.hold", r"hold (\d+)"),
          ("holds.note", r"note (\d+)"),
          ("conflicts", r"conflicts \(?(\d+)\)?"),
          ("rank_quarantine_handles", r"quarantine handles \(?(\d+)\)?"),
          ("rank_quarantine_handles", r"rank_quarantine_handles (\d+)"),
          ("rank_rules_unresolved_items", r"rank_rules_unresolved_items (\d+)"),
          ("stats.labels", r"labels (\d+)")]

def audit(text, live, label):
    out = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if not (re.match(r"\s*\|?\s*(D4-CL\d\d)\s*\|", line)
                or re.match(r"\s*-\s*(OQ-V3-\d\d):", line)
                or '"claim_id": "D4-CL' in line):
            continue
        row = next(iter(re.findall(r"(D4-CL\d\d|OQ-V3-\d\d)", line)), None)
        for key, pat in PROBES:
            for got in re.findall(pat, line):
                if key in live and int(got) != int(live[key]):
                    out.append((label, lineno, row, key, int(got), int(live[key])))
    return out

def main(argv):
    if len(argv) < 2:
        print("usage: d4_stale_audit.py <packet.md|twin.json> [...]", file=sys.stderr); return 2
    live, allf = live_values("."), []
    for path in argv[1:]:
        text = open(path, encoding="utf-8").read()
        if path.endswith(".json"):
            doc = json.loads(text)
            for row in doc.get("claim_ledger", []):
                if str(row.get("claim_id", "")).startswith("D4-CL"):
                    allf += audit(json.dumps(row), live, path + ":" + row["claim_id"])
            for q in doc.get("open_questions", []):
                if str(q.get("id", "")).startswith("OQ-V3"):
                    allf += audit(json.dumps(q), live, path + ":" + q["id"])
        else:
            allf += audit(text, live, path)
    if not allf:
        print("CLEAN: no D4-scoped row asserts a value that differs from live bytes"); return 0
    print("STALE: %d D4-scoped mismatches" % len(allf))
    for label, lineno, row, key, got, want in allf:
        print("  %s:%s [%s] %s asserted=%s live=%s" % (label, lineno, row, key, got, want))
    return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

Controls, all run 2026-10-19 (`cd` repo root; `export TMPDIR=$PWD/.scratch`):

| control | command | observed |
|---|---|---|
| 1 — positive on the live pair | `python3 -B d4_stale_audit.py reports/round-30/handoff/declared-in-r6/packet.md` | `STALE: 13 D4-scoped mismatches`, exit **1** (§2 list) |
| 2 — twin leg | `… declared-in-r6/twin.json` | `STALE: 13`, exit **1**, same rows |
| 3 — **clean reachable**: all D4 rows rewritten to live values in `.scratch` | `… packet-repaired.md` | `CLEAN: no D4-scoped row asserts a value that differs from live bytes`, exit **0** |
| 4 — **single-figure sensitivity**: one `typed_labels 82` → `74` in the cleaned copy | `… packet-injected.md` | `STALE: 2` (both `typed_labels` and `stats.labels` in `D4-CL05`), exit **1** |
| 5 — **scoping false-positive demo** (negative control for the *method*) | un-scoped token scan over the cleaned copy | **17 false positives**, 8 on D2-scoped rows (`:129,:130,:301`) and 1 decision-table row (`:284`) |
| 6 — filed-revision sweep | all four filed pairs | every revision `md=STALE: 13 twin=STALE: 13` |

Control 6's finding is worth carrying: the count is **13 in every filed generation**
(`reports/round-22/handoff/declared-in`, `-r2`, `reports/round-26/handoff/declared-in-r5`,
`reports/round-30/handoff/declared-in-r6`). Meanwhile each pair's own
`expected.json#counts` already reads `d4_holds 12` — including r1 and r2 — while the
paired packet asserts `hold 15, note 1`. So the packet's D4 hold text has never
matched its own baseline, and `d4_typed_labels` moved 74 → 82 in `expected.json` at r5
while the r5 and r6 packets kept asserting 74. **The staleness lives in the
renderer's inputs (claims map + literal), not in the baseline**, which is why a
baseline-only re-pin cannot repair it. (Whether r1/r2 were fresh against the
*thens*–live bytes is `to-verify`; my measurement is against today's delivered bytes.)

## 6. Byte-preservation of my own work

```
$ git status --porcelain
?? reports/round-34/
$ git diff --stat HEAD -- reports/ examples/ tools/ SCORECARD.md LOG.md
(empty)
```

No filed round byte, no `corpus/lessons`, no `tools/gates/frozen/**`, no shared file
was touched. All renders ran inside `.scratch/d16/iso` (an isolated `git archive`)
with output to `.scratch/d16/freezeout`; the in-tree renderer defaults at
`:1933-1934` are untouched. I executed no `reports/round-*/run-validation.py`.

## 7. Reconciliation with the fragments that landed after my dispatch

While I worked, D01–D04, D08, D10–D12, D14 and D18 landed. §4 is therefore
**convergent, not novel** — which upgrades it from one seat's reading to a
cross-seat result, and sharpens what is still missing.

- **The root cause was found independently by four seats.** D01 `:143-149` (surface
  table + its own before/after at `:163-168`), D02 `:140-142` ("route A / route B"),
  D08 `:175-212`, D12 `:16,:172`, and me at §4. Four independent measurements agree:
  the twelve D4 rows are copied verbatim from filed `reports/round-20/handoff/claims-map.md`
  (`CLAIMS_MAP`, renderer `:184`, parse at `:2289-2314`), and `OQ-V3-05` is a renderer
  literal (`:3524-3531`).
- **D02 `:39-46` independently reproduced my render finding** — its `--freeze` render
  is byte-identical to the filed r6 packet (`6ced88ad…`, `6633443d…`), and its `:71`
  states the same binding consequence I prove in §4. Two isolated renders, same sha.
- **The remaining gap is D10's census, and it is exact.** D10's §1 census has **21
  rows** and mentions `CLAIMS_MAP`/`claims-map` **0 times** (`grep -c` → `0`). D10 is
  the seat whose mission owns "every other pinning surface", and its own `Owed` records
  that K02 was absent so §1 is its stand-in. So a cascade applied from D10's Draft A
  alone — the two `:1933-1934` defaults — reproduces the defect claim D exists to
  close, per §4 and D02 `:71`. **The integrator must fold §4 rows A–E into the cascade
  before applying it.** I did not edit D10's fragment (not my `out` path).
- **Naming divergence the integrator must resolve, not merge.** Three seats name three
  different paths for the same new file: D01 `:150,:164,:262`
  → `reports/round-34/handoff/claims-map-v3-next.md`; D08 `:203`
  → `reports/round-34/handoff/claims-map-v3-r7.md`; my §4 row B
  → `reports/round-34/handoff/claims-map.md`. Only one can be written, and the
  `CLAIMS_MAP` constant, the new file's own path, and D05's assembler must all agree.
  This is a decision for the integrator/P01 — recorded here, not absorbed.
- **D03 landed stronger than my §2, and it exposes a limit of my instrument.** D03
  `:138` found a **semantic** staleness my numeric scan cannot see: the packet's
  `D4-CL09` basis asserts the rank act rows "carry `adapt_status` cannot-evaluate
  because speech is not a gate-modelled channel". I verified this independently: live
  `rank_rules.act_rules` is `[]`, `cannot-evaluate` occurs **0×** in the D4 projection
  and **19×** in the D2 projection, all **8** D4 `adapt_status` values are
  `executable`, and `rank_rules.skipped` records "packet-native rank rules only; no
  foreign fixture data is imported". **Honest limitation:** my §5 tool reports `CLEAN`
  on a numerically-repaired packet that still carries that stale sentence (measured:
  the repaired control copy still contains `cannot-evaluate`, and the tool exits 0 on
  it). The tool closes the numeric class only; D03/D20 must cover the semantic class,
  and D20's "zero stale figures" check is not by itself sufficient for claim D's
  threshold, which reads "zero stale figures … audited against live bytes".
- D03 `:19-31` independently reports the same live values as my §1 (82/64, `stats
  0/12/82` at `:2866-2868`), and its `:68-71` replacement table matches my §2
  stale set row for row. Two independent censuses, no disagreement.

## Owed

1. **The new claims map file** (§4 row B; name to be decided per the §7 divergence) —
   the 12 live-accurate D4 rows. I supplied the surface, the shape and every live value;
   authoring it is D03/D05's content and the integrator's to land. **Without it, claim
   D's `after_required` cannot be met by the declared path.**
2. **D10's §1 census must gain the `CLAIMS_MAP` re-point row** (§7: 21 rows, 0
   mentions). D10's fragment is not mine to edit; the integrator folds §4 rows A–E in.
   K02's `declared-in-r6` grep structurally cannot supply it (`CLAIMS_MAP` pins r20).
3. **A path decision for the new claims map** — three seats propose three names (§7).
4. **The semantic-stale class D03 owns** (`D4-CL09` "cannot-evaluate") is outside my
   §5 tool's coverage; `OQ-V3-05`'s rewrite (E) should not silently re-import the same
   "speech is not a gate-modelled channel" rationale.
5. **`reports/round-34/depth/D*-*.md` still absent at my close**: D05, D06, D09, D13,
   D15, D17, D19, D20 (D07 landed after §7 was drafted, so it is no longer in this
   list — its gate result is D07's to report, not mine). My §1 census and §5 tool are
   built to be consumed by them — D13's control (a) can reuse §5 controls 4–5 verbatim,
   and D20 should run §5 over the D05 draft (expected `CLEAN`, exit 0) **and** re-check
   the semantic class.
6. **Whether the A02-H1 item closes in this round** is the integrator's verdict, not
   mine — §5 now makes the numeric half falsifiable.

## Citations

Paths read (all at baseline `da68a6d`):
- `REGIMEN.md`; `reports/round-34/claims.json`; `reports/round-34/targets.json` (seat D16; D01–D20 missions; `shared_rules`)
- `examples/culture-d4/typed-labels.d4.yml` (`:29-46` coverage, `:2865-2869` nested stats, `:297-299` label_kinds)
- `examples/culture-d4/expected-holds.json` (`:46-50` counts; `:51+` rows)
- `examples/culture-d2/typed-labels.d2.yml` (`:29-46` coverage) — the scoping control
- `reports/round-30/handoff/declared-in-r6/{packet.md,twin.json,expected.json,freeze.txt}`
  (`packet.md:3,:68-69,:95,:113,:125,:129-130,:148-152,:266,:303,:307`)
- `reports/round-22/handoff/declared-in/`, `reports/round-22/handoff/declared-in-r2/`,
  `reports/round-26/handoff/declared-in-r5/` — `{packet.md,twin.json,expected.json}`
- `reports/round-20/handoff/claims-map.md` (`:97,:104,:107,:116,:119,:124,:150,:154,:158,:251`)
- `reports/round-33/adj/A02-handoff.md` (`:33-46,:79-85,:92-136`) — A02-H1
- `tools/exercise-handoff-e2e.py` (`:28-36,:184,:1957,:2286-2314,:2554,:2566,:2599,:2621,:2694-2703,:2865-2883,:2930-2938,:3127-3147,:3498-3545,:4063-4064`)
- `tools/gates/handoff-packet-check.py` (gate CLI + `--selftest`)
- Landed sibling fragments read in §7: `reports/round-34/depth/D01-layout.md`
  (`:126,:143-144,:149-150,:163-168,:238,:262,:283-292`), `D02-render.md`
  (`:39-46,:71,:87-89,:115-118,:140-142,:159,:181-183`), `D03-ledger-rows.md`
  (`:13-31,:68-71,:88,:94,:110,:132,:138,:155`), `D04-oq-glossary.md`
  (`:47,:51,:56,:131,:151,:165,:270`), `D08-links-uncertainty.md`
  (`:17-18,:75,:175-180,:199-212`), `D10-repin-drafts.md` (`:33-55` census rows 1–21,
  `Owed`), `D12-receipt.md` (`:16,:172`)

Commands run (all read-only against the repo; renders isolated):
- `sha256sum` over the eight files in §1
- `python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md` → `exit 0`, `INFO scan: fields=16/16 glossary-entries=20 findings=0`
- `python3 tools/gates/handoff-packet-check.py --selftest` → `exit 0`, `selftest: OK — fixture findings 11 across 9 ids`
- `git archive HEAD | tar -x -C .scratch/d16/iso`; in the copy: `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --freeze .scratch/d16/freezeout` → `exit 0`, `packet sha256 6ced88ad009f…`
- `diff -q .scratch/d16/freezeout/packet.md reports/round-30/handoff/declared-in-r6/packet.md` → identical
- `python3 -B .scratch/d16/d4_stale_audit.py <path>` over 8 targets (controls 1–6)
- §7 verifications: `grep -c -i 'claims.map\|CLAIMS_MAP' reports/round-34/depth/D10-repin-drafts.md` → `0`; `grep -c '^| [0-9]' …D10-repin-drafts.md` → `21`; `grep -rn 'claims-map-v3-next\|claims-map-v3-r7' reports/round-34/depth/*.md`; D4/D2 `cannot-evaluate` counts and `rank_rules.act_rules`/`adapt_status`/`skipped` reads (live JSON parse, D4 `0×` vs D2 `19×`, 8× `executable`)
- `git status --porcelain`, `git diff --stat HEAD -- reports/ examples/ tools/ SCORECARD.md LOG.md`, `git log --oneline -1 -- reports/round-20/handoff/claims-map.md`
- `git status --porcelain`, `git diff --stat HEAD -- reports/ examples/ tools/ SCORECARD.md LOG.md`, `git log --oneline -1 -- reports/round-20/handoff/claims-map.md`
