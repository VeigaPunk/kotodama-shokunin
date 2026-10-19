- Seat: D08 | executor | claim D | date 2026-10-19 | baseline da68a6d

# D08 — links + uncertainty legs over the packet draft

## Verdict (read this first)

Both legs are **green** on a renderer-produced draft twin, at the same claim/link
shape as live: `packet_uncertainty.py --require-oq` → exit 0, `claims=27`,
`findings=[]`; `packet_links.py --repo-root <repo>` → exit 0, `105/105` links
resolved, `findings=[]`.

**But the legs cannot fix claim D's `after_required`.** Measured this seat:
re-rendering the packet from the current D2/D3/D4 artifacts reproduces the filed
r6 bytes **byte-identically** (`packet_sha256 6ced88ad…`, `twin_sha256
6633443d…`, `packet.md` and `twin.json` `cmp`-equal). The stale figures are not
derived from live artifacts at all: the twelve D4 claim rows are carried
**verbatim from a filed round-20 file**, `reports/round-20/handoff/claims-map.md`
(read live via `CLAIMS_MAP`, `tools/exercise-handoff-e2e.py:184`, parsed at
`:2289-2307`, extended into the ledger at `:2604`), and `OQ-V3-05`'s stale text is
**hardcoded** in the tool at `tools/exercise-handoff-e2e.py:3524-3531`. A move of
the renderer default to a new directory would therefore re-pin a **byte-identical
duplicate** of r6 while every stale number survives. What must move is the
*input*, not the default — options and before/after drafts in §6.

## 0. Dependency state (why the leg inputs are mine)

`depth/D05-packet-draft.md` (and every other D-block fragment except
`depth/D11-preservation.md`) was **absent** at seat time:
`find reports/round-34 -type f` → `claims.json`, `targets.json`,
`telemetry/dispatch-declared.json`, `depth/D11-preservation.md` only
(04:03 local). Per the missing-dependency rule I built the leg inputs myself from
live bytes rather than wait:

1. `.scratch/d08/declared-in-r7/` = a fresh renderer freeze —
   `python3 tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch/d08/declared-in-r7`
   → exit 0, `froze .scratch/d08/declared-in-r7: packet sha256 6ced88ad…`; it also
   printed `no tracked value changed since the previous freeze`. Wrote only under
   `.scratch/` (outside the tree deliverables); **no filed byte touched**.
2. `reports/round-30/handoff/declared-in-r6/twin.json` (filed pair) as the
   control.

Draft vs filed r6 (`cmp` per file): `packet.md` IDENTICAL, `twin.json`
IDENTICAL, `run.log` IDENTICAL; `freeze.txt` differs only in the date line and
the `re-frozen … / no tracked value changed …` line (:1, :8); `expected.json`
differs only in `frozen_at` (`2026-10-18`→`2026-10-19`, :100) and
`baseline_digest` (`714b41fc…`→`c2dd169b…`, :3). The two twins hash equal:
`6633443d70ce44ed2bb43ab58aa60a1c98e4bbc79b2f577a63181c89dc16fd4e`.

## 1. Leg results (draft twin)

| leg | command (exact) | exit | payload |
|---|---|---|---|
| uncertainty | `python3 -B tools/harness/packet_uncertainty.py --packet .scratch/d08/declared-in-r7/twin.json --require-oq --json` | 0 | `{'tool': 'tools/harness/packet_uncertainty.py', 'claims': 27}`, `findings: []` |
| links (digests) | `python3 -B tools/harness/packet_links.py --packet …/twin.json --repo-root $PWD --json` | 0 | `links_checked: 105, resolved: 105`, `findings: []` |
| links (`--no-digests`) | same + `--no-digests` | 0 | `links_checked: 105, resolved: 105` |
| control (filed r6 twin) | both commands against `reports/round-30/handoff/declared-in-r6/twin.json` | 0/0 | `claims 27`, `findings []`; `105/105` |

These are the exact invocations the tool's own semantics leg uses
(`tools/exercise-handoff-e2e.py:3730-3742`, tuples at `:3731-3732`: `("uncertainty", UNCERTAINTY_TOOL,
["--require-oq"])`, `("links", LINKS_TOOL, ["--repo-root", str(self.root)])`),
so the seat result and the e2e leg are the same measurement.

Both harness selftests are green on the live bytes:
`packet_links.py --selftest` → `38 checks passed`, exit 0;
`packet_uncertainty.py --selftest` → `19 checks passed`, exit 0.

Whole-exercise leg (claim D's counting command) on the live tree:
`python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` →
`handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=6ced88ad…`, exit 0.

## 2. 27-claim shape parity with live

| surface | value | source of truth |
|---|---|---|
| claim rows | 27 = 15 v2 + 12 D4 | twin `claim_ledger` 27; `reports/round-15/handoff/packet-v2-05.yml:345-505` (15 `claim_id`s read live); `reports/round-20/handoff/claims-map.md` (12 `D4-CL\d\d` headings, `tools/exercise-handoff-e2e.py:2286` regex, `:2294` count check) |
| claim ids | exact, ordered list matches frozen `claim_ids` | e2e check `frozen-claims: 27 claim ids match the baseline`; `expected.json` `claim_ids` |
| statuses | `supported 16 / partial 7 / unresolved 4` | `v3_status_census` (`tools/exercise-handoff-e2e.py:3432-3434`); e2e leg `uncertainty-census: claims=27 statuses=16/7/4` |
| unresolved rows | `D2-CL02, CL13, D4-CL09, D4-CL12` | twin `claim_ledger` |
| OQ routing (require-oq) | every unresolved row referenced: `D2-CL02`←`OQ-V2-03`, `CL13`←`OQ-V2-01`, `D4-CL09`←`OQ-V3-05`, `D4-CL12`←`OQ-V3-06` | twin `open_questions` (10 rows: `OQ-V2-01..07`, `OQ-V3-04..06`); leg exit 0 |
| links | 105 link specs = Σ per-claim `links` (3+3+5+6+2+6+3+3+2+3+3+3+3+3+2 + 3+6+5+4+5+4+5+7+4+6+3+3) over 88 coupling edges and a 58-row artifact manifest | twin; leg `105/105` |
| structure | `claim_ledger` rows carry `claim_id, claim_kind, evidence_status, links, statement, uncertainty{status,basis}` | twin row keys; `packet_uncertainty.py:41` `REQUIRED_UNCERTAINTY_KEYS` |

So: **shape parity with live holds exactly**; what does *not* hold is the numeric
content of four D4 rows and one OQ row (§5).

## 3. Controls — what each leg actually bites on

Fixtures written under `.scratch/d08/ctl/` (twin copies, one mutation each); both
legs run on each.

| control | mutation | uncertainty | links | reading |
|---|---|---|---|---|
| ctl1 dangling selector | `D4-CL07.links[0]` → `…#no-such-key-here` | exit 0, `[]` | **exit 1, `L-TOKEN-MISSING`, 104/105** | the links leg is live, not vacuous |
| ctl2 orphaned unresolved | `OQ-V3-05.unresolved_claims` → `—` | **exit 1, `U-OQ-UNROUTED`** | exit 0, `[]` | `--require-oq` bites on routing loss |
| ctl3 injected stale number | `D4-CL05` basis `typed_labels 74` → `typed_labels 999` | **exit 0, `[]`** | **exit 0, `105/105`, `[]`** | numeric staleness is invisible to BOTH legs |
| ctl4 off-vocabulary status | `D4-CL03.uncertainty.status` → `probably-true` | **exit 1, `U-STATUS-VOCAB`** | exit 0 | status vocabulary enforced |

ctl3 is the honest limit of this seat's evidence, and it also holds for the real
bytes: the draft twin **already carries** `typed_labels 74` where live is `82` and
both legs are green (§5). The links leg re-measures the 58 manifest digests
against live bytes (`tools/harness/packet_links.py:99-127`, finding class
`M-DIGEST-MISMATCH`), but a claim's *basis prose* is not a digest-backed
artifact — nothing in either harness reads the numbers inside it. The negative
control therefore also names the class D13 must own: **semantic-stale prose behind
a resolving selector is a class neither the gate nor these two legs can catch.**

## 4. Leg spec for the round-34 validator (draft for S04)

```
# claim-D semantic legs (all three must exit 0 on the delivered pair)
python3 tools/harness/packet_uncertainty.py --packet <frozen-dir>/twin.json --require-oq --json
    # assert claims == 27, findings == []
python3 tools/harness/packet_links.py   --packet <frozen-dir>/twin.json --repo-root . --json
    # assert links_checked == resolved == 105, findings == []
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
    # assert exit 0 and the summary line's packet_sha256 == <frozen-dir>/freeze.txt:2
```
Add one **content** leg the semantic legs cannot supply (else the round can pass
while §5's figures stay stale):
```
python3 reports/round-34/check-live-figures.py   # or grep -c on the delivered packet.md
    # assert 0 occurrences of: "typed_labels 74", "native-form 56", "findings_total 16",
    # "findings_hold_or_fail 15", "hold 15, note 1", "conflicts (4)", "quarantine handles (3)",
    # "13 unresolved rank items", "rank_quarantine_handles 3", "rank_rules_unresolved_items 13"
```

## 5. Live-figure census — what is stale and where it comes from

Live values, all from the delivered bytes (line numbers are real lines):

- `examples/culture-d4/typed-labels.d4.yml:29-47` (`#coverage`): `conflicts 0` (:30),
  `findings_hold_or_fail 12` (:31), `findings_total 12` (:32), `label_findings_fail 0` (:33),
  `label_findings_hold 12` (:34), `labels_by_kind` borrowed-strata 6 / native-form 64 /
  translated-label 12 (:36-38), `rank_quarantine_handles 0` (:40),
  `rank_rules_unresolved_items 0` (:44), `reconciliation_records 6` (:45), `typed_labels 82` (:46).
- `examples/culture-d4/typed-labels.d4.yml:2865-2869` (`#stats`): `fail 0, hold 12, labels 82`.
- `examples/culture-d4/expected-holds.json:46-49` (`#counts`): `hold 12, note 0, fail 0`;
  `holds` = 12 rows, all `("D2L-FORM-UNRESOLVED","hold")` (e.g. `where: GAR-01`,
  `detail: "label_id LEX-GAR-01 has no supplied native/borrowed form"`), `notes` = 0 rows.
- D2 rows are **live-correct** (checked, not assumed): `examples/culture-d2/typed-labels.d2.yml:30,40,44,45,46`
  → `conflicts 4`, `rank_quarantine_handles 3`, `rank_rules_unresolved_items 13`,
  `reconciliation_records 10`, `typed_labels 58`; `:31-38` → `findings_total 16`,
  `findings_hold_or_fail 15`, native-form 46 / translated-label 10 / borrowed-strata 2.
  These are just what `D2-CL01`/`D2-CL02` prose states, so the v2-subset equality leg
  (`expected.json.v2_subset_digest ad35c860acf3b452…`) is **not** an obstacle to the fix.

Stale occurrences in the draft bytes (all four claim cells are also in the packet
prose at the same lines — `reports/round-30/handoff/declared-in-r6/packet.md:148,149,150,152,307`,
byte-identical to the draft):

| location | figure in draft | live | live source |
|---|---|---|---|
| `D4-CL05` statement+basis | `typed_labels 74` (×2 incl. `#stats … labels 74`) | 82 | `typed-labels.d4.yml:46`, `:2868` |
| `D4-CL05` | `native-form 56` | 64 | `:37` |
| `D4-CL05` | `findings_total 16` / `carries 16 findings` | 12 | `:32` |
| `D4-CL05` | `findings_hold_or_fail 15` / `15 are hold-or-fail` | 12 | `:31` |
| `D4-CL06` statement+basis | `hold 15` / `15 holds` | 12 | `expected-holds.json:47` |
| `D4-CL06` | `note 1` / `1 note` | 0 | `:48` |
| `D4-CL06` | `three D2L-RANK holds, plus one D2L-RANK note` | 0 rank holds, 0 notes | `:51+` (12 rows, all `D2L-FORM-UNRESOLVED`) |
| `D4-CL06` statement | `+9 hold / +1 note delta` vs the brief's six-row declaration | arithmetic on cited counts: 6 declared (`reports/round-18/d4/holds.md:221` `hold_set_declaration (6/0/0)`) → 12 delivered ⇒ **+6 hold / +0 note** (the +9/+1 is what `holds.md:40` recorded before the hold set moved) — `to-verify` by D03: I read the ends, not a filed re-derivation |
| `D4-CL07` statement+basis | `conflicts (4)` / `four conflicts` | 0 | `:30` |
| `D4-CL07` | `quarantine handles (3)` | 0 | `:40` |
| `D4-CL09` statement+basis | `13 unresolved rank items` / `thirteen` | 0 | `:44` |
| `D4-CL09` | `3 quarantine handles` / `three` | 0 | `:40` |
| `D4-CL09` | `4 conflicts` / `four` | 0 | `:30` |
| `OQ-V3-05` (tool constant) | `three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts` | 0 rank holds, 0 notes, 0 rank items, 0 quarantine, 0 conflicts | as above |
| `D4-CL04` basis | `five slots owe a native-form`, `LEX-GAR-06 … borrowed-strata` | slot-ownership prose, not covered by any leg I ran | `to-verify` (D03/D13) — not claimed either way |

The six figures `claims.json` names in `before.stale_numbers` (74/56/16/15, conflicts 4,
quarantine 3) are all reproduced above; the census adds `hold 15→12`, `note 1→0`,
`rank items 13→0`, `labels 74→82`, `D4-CL07`'s parenthesised pair and the OQ row.

### Provenance chain (why re-render alone cannot fix this)

1. `tools/exercise-handoff-e2e.py:184` `CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"`.
2. `:2289-2307` `v3_parse_claims_map` reads that file, requires exactly 12 rows
   (`:2294`), and pulls `statement`/`u.basis`/`links` from it (`:2303-2307`).
3. `:2566` the manifest states it outright: `CLAIMS_MAP: "the twelve D4 claim rows as filed; this packet carries them verbatim"`.
4. `:2604` `rows.extend(dict(row) for row in d4_rows)` → those rows (statement + basis verbatim) are the ledger and the packet's D4 table.
5. The stale bytes are in that filed file: `reports/round-20/handoff/claims-map.md:104` (`typed_labels 74, … native-form 56, findings_total 16, findings_hold_or_fail 15 … labels 74`), `:116` (`hold 15, note 1, fail 0 … three D2L-RANK rows, plus one D2L-RANK note`), `:127` (`counts carry four conflicts`), `:158` (`rank_rules_unresolved_items 13 … rank_quarantine_handles 3 … conflicts 4`). The file is **filed** (round 20, allowed posture: supersede-by-new-file), digest `4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8` — the same digest `expected.json.inputs` pins.
6. `OQ-V3-05` is not read from any file: it is built in code at `:3524-3531`.
7. Consequence, measured: `--freeze` from live bytes reproduces `packet.md`/`twin.json` byte-identically (seat log §0), because every input to the prose is unchanged. **Regeneration is not a fix; the input must move.**

The rowwise evidence that only prose is stale: the packet's own manifest rows already
agree with live (`packet.md:49` `A-11 … 58 labels, 16 findings, 13 unresolved rank …`
is the **D2** row and is correct; `packet.md:68-69` D2/D3 rows), while the D4 cells at
`:148-152` do not — the same self-contradiction `reports/round-33/adj/A10-receipt.md:50`
(A02-H1) filed.

## 6. Drafted shared-file changes (integrator applies; seats never edit shared files)

Two surfaces, both in `tools/exercise-handoff-e2e.py`. Option A (recommended: a new
filed input, no prose hardcoded in the tool) and Option B (in-tool correction layer).

**Surface 1 — the D4 row source.**

BEFORE (`tools/exercise-handoff-e2e.py:184`):
```
CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"
```
AFTER (Option A):
```
CLAIMS_MAP = "reports/round-34/handoff/claims-map-v3-r7.md"
```
The new file must keep the exact shape the parser requires — 12 headings matching
`^### (D4-CL\d\d) — (.+?) — (.+?) — \`([a-z]+)\`$` (`:2286`), each with
`- **statement:**`, `- **u.basis:**`, `- **links:**` bullets (`:2303-2307`) — and
carry the four rewritten cells (`D4-CL05`, `D4-CL06`, `D4-CL07`, `D4-CL09`) with the
live figures of §5. Because `CLAIMS_MAP` is in `V3_READ_SET` (`:1957`), the new file's
digest enters `expected.json.inputs` automatically and the old `4b1b9a35…` row leaves
it — that removal is a **declared supersession row**, not an edit: the filed
`claims-map.md` keeps its bytes. Also update the four in-tool docstring/manifest
strings that name the old path: `:34`, `:57`, `:2290`, `:2700`.

Option B (same effect, worse shape — prose numbers live in code):
```
# after `self.d4_rows = v3_parse_claims_map(root)` (`:3511`)
D4_BASIS_SUPERSESSIONS = { "D4-CL05": <live text>, "D4-CL06": …, "D4-CL07": …, "D4-CL09": … }
self.d4_rows = [ {**row, **D4_BASIS_SUPERSESSIONS.get(row["claim_id"], {})} for row in self.d4_rows ]
```
Do not do both. Either way the filed round-20 file is left untouched.

**Surface 2 — the OQ row.**

BEFORE (`tools/exercise-handoff-e2e.py:3524-3531`, bytes as filed):
```
                "id": "OQ-V3-05",
                "question": (
                    "D4's inherited and own holds stay open: twelve form holds + three rank holds + one "
                    "note, thirteen unresolved rank items, three quarantine handles and four conflicts — "
                    "kotodama; blocking for the affected D2 rank records and the six garment terms, not for "
                    "this envelope"
                ),
                "unresolved_claims": "D4-CL09",
```
AFTER (live figures; keeps id, shape and the `D4-CL09` routing the require-oq leg needs):
```
                "id": "OQ-V3-05",
                "question": (
                    "D4's inherited and own holds stay open: twelve form holds, no rank holds and no notes, "
                    "zero unresolved rank items, zero quarantine handles and zero conflicts — kotodama; "
                    "blocking for the affected D2 rank records and the six garment terms, not for this "
                    "envelope"
                ),
                "unresolved_claims": "D4-CL09",
```

Both surfaces change prose that feeds `field_digests` (`claim_ledger`,
`open_questions`) and the packet/twin digests of any later freeze — expected, and the
reason r7 is a **new** revision rather than an in-place edit. `expected.json` for r7
will then differ from r6 in more than `frozen_at`/`baseline_digest` (the only two
fields that differ today).

## 7. What these legs prove, and what they do not

Proved (exit-0 evidence above): 27 claim rows at live shape; every claim carries the
uncertainty grammar with a non-boilerplate, individually reasoned basis; the four
`unresolved` rows are routed to open questions under `--require-oq`; all 105 link
specs resolve against live bytes and the 58 manifest digests re-measure equal; the
links/uncertainty/gate legs agree on the draft pair and on the filed r6 pair.

Not proved, by construction (ctl3): that any number inside the basis/statement prose
equals a live value. Neither harness reads those numbers, and the digest leg covers
only manifest rows. The delivered r7 packet can be **fully green on every semantic
leg and still carry `typed_labels 74`** — which is exactly today's r6 state.

## 8. Cross-check with the D fragments that landed mid-run, and a correction to D02's flag

D02/D03/D04/D12/D18 landed under `reports/round-34/depth/` while this seat ran. Two
of them independently reached §5's blocker — D02 (`depth/D02-render.md:71`: "byte-identical
output carrying the same stale digits … cannot be produced by render or default-move
alone") and D12 (`depth/D12-receipt.md:97-110,172-175`) — so the provenance finding is
measured by three seats, not one. D03 (`depth/D03-ledger-rows.md:88`+) has already drafted
the corrected D4-CL05 cell with exactly the live figures of §5, so §6 Option A and D03's
rows compose: D03 supplies the 12-row replacement text, the integrator lands it as the new
claims-map file and re-points `CLAIMS_MAP`.

D02 also raised a flag **at this seat** (`depth/D02-render.md:163`): it reads `D4-CL05`'s
`#stats` link cell as a dangling anchor the links leg missed. Measured, the flag does not
hold, and the reason is worth recording:

- `"stats"` is a live key of the cited file: `grep -n '"stats"'
  examples/culture-d4/typed-labels.d4.yml` → `2865:    "stats": {` (one hit). The cell is
  not dangling.
- Renaming that one token to a string absent from the file (`#pipeline_counts`) turns the
  leg red exactly as designed: exit 1, `L-TOKEN-MISSING` on
  `examples/culture-d4/typed-labels.d4.yml#pipeline_counts`, `104/105`
  (ctl5, `.scratch/d08/ctl/ctl5-renamed-token.json`).
- D02's methodological point survives, narrowed: for non-JSON artifacts the resolver uses a
  **word-boundary match in the file's bytes** (`tools/harness/packet_links.py:17-18`), so a
  `#token` on a `.yml`/`.md` artifact proves "this word occurs in this file", not "this key
  path exists". A word that appears only in prose would resolve. That is a named limit of
  the links leg (hand to D13/R01), not a defect in the r6/r7 pair.
- The real defect at that cell is the ctl3 class, not the link: the `#stats` **value prose**
  of `D4-CL05` says `labels 74` where the live block at `:2865-2869` says `labels 82`.

## Owed

- `reports/round-34/depth/D05-packet-draft.md` — did not exist at seat time (§0). My
  legs ran against a renderer-produced draft twin (byte-identical to r6). **If D05's
  draft differs in any byte from the renderer's output, both legs must be re-run on
  that draft**; the commands are in §4. Nothing else in this fragment depends on D05.
- `reports/round-34/handoff/claims-map-v3-r7.md` (Option A) or the in-tool
  substitution (Option B) — the shared-file change drafted in §6 is **not landed**;
  until the integrator lands one of them, the r7 pair will be a byte-identical
  duplicate of r6 and claim D's `after_required` ("every claim-ledger/OQ number equal
  to a measured live value") is unmet. Owner: integrator (shared-file rule).

## Citations

- `tools/exercise-handoff-e2e.py:184` (`CLAIMS_MAP`), `:1933-1934` (`V3_BASELINE_DEFAULT`/`V3_FROZEN_DIR_DEFAULT` = declared-in-r6), `:1957` (`CLAIMS_MAP` in `V3_READ_SET`), `:2286` (`D4_ROW_RE`), `:2289-2307` (`v3_parse_claims_map`), `:2566` ("carried them verbatim"), `:2604` (rows extended), `:3432-3434` (`v3_status_census`), `:3524-3531` (hardcoded `OQ-V3-05`), `:3734-3739` (leg invocations `--require-oq`, `--repo-root`), `:3978-4003` (`v3_freeze`, refuse-if-red)
- `tools/harness/packet_uncertainty.py:63` (`REQUIRED_UNCERTAINTY_KEYS`), `:141-241` (finding classes incl. `U-OQ-UNROUTED`), `:556-586` (CLI)
- `tools/harness/packet_links.py:39-40` (CLI), `:99-127` (`verify_manifest_digests`, `M-DIGEST-MISMATCH`)
- `examples/culture-d4/typed-labels.d4.yml:29-47`, `:2865-2869`
- `examples/culture-d4/expected-holds.json:46-49`, `:51+` (12 `D2L-FORM-UNRESOLVED` hold rows, 0 note rows)
- `examples/culture-d2/typed-labels.d2.yml:30-46`
- `reports/round-20/handoff/claims-map.md:104,116,127,158` (stale bytes), digest `4b1b9a35…`
- `reports/round-30/handoff/declared-in-r6/{packet.md:148-152,307; twin.json; expected.json:3,100,169; freeze.txt:1,8; run.log}`
- `reports/round-15/handoff/packet-v2-05.yml:345-505` (15 v2 rows)
- `reports/round-18/d4/holds.md:40,221` (`+9 hold / +1 note`, `hold_set_declaration (6/0/0)`)
- `reports/round-33/adj/A10-receipt.md:50` (A02-H1 filing)
- Commands: `python3 tools/exercise-handoff-e2e.py --profile v3`, `… --profile v3 --quiet`, `… --profile v3 --freeze .scratch/d08/declared-in-r7`, `python3 -B tools/harness/packet_uncertainty.py --packet <twin> --require-oq --json`, `python3 -B tools/harness/packet_links.py --packet <twin> --repo-root $PWD --json [--no-digests]`, both `--selftest`s, `cmp`/`diff` over the two pair directories, `sha256sum` of the twins, and the four `.scratch/d08/ctl/*` control runs
- Paths written by this seat: `reports/round-34/depth/D08-links-uncertainty.md`; scratch only: `.scratch/d08/{declared-in-r7/,ctl/,unc-draft.json,links-draft.json}`
