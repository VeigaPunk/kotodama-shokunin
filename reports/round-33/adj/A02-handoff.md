- Seat: A02 | executor | claim A | date 2026-10-19 | baseline 139e3b6

# A02 — handoff boundary re-run (current packet pair + contract cross-check)

- **Scope:** re-run the handoff packet gate on the *current* packet pair and
  cross-check the pair against `corpus/knowledge/synthesis/worldbible-integration-contract.md`.
  Read-only: no filed byte was written by this seat; every command below ran with
  `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. This is a boundary/adjacency
  verdict, not a lore disposition, canon ruling, or clearance statement.

## 1. Which pair is "current" (determined, not assumed)

The newest frozen v3 revision on disk is `reports/round-30/handoff/declared-in-r6/`
(packet.md + twin.json + expected.json + freeze.txt + run.log; `find reports -type d -name 'declared-in*'`
returns exactly six: r2, r2→declared-in, r3, r4, r5, r6).

It is *current* by the renderer's own wiring, not by mtime:

- `tools/exercise-handoff-e2e.py:1933-1934` — `V3_BASELINE_DEFAULT = "reports/round-30/handoff/declared-in-r6/expected.json"`,
  `V3_FROZEN_DIR_DEFAULT = "reports/round-30/handoff/declared-in-r6"`; the earlier rows are filed and never edited.
- `SCORECARD.md:400` (round-30 operability row) — "the v3 default chain re-pointed to declared-in-r6 after
  diagnosing the profile-row baseline drift"; `LOG.md:3428` repeats it.
- `reports/round-30/handoff/declared-in-r6/freeze.txt:1` — `frozen: 2026-10-18 by tools/exercise-handoff-e2e.py --profile v3`.

Commands and dates are inline below. The gate command shape follows the filed
convention (`reports/round-23/adjacency.md:73`; packet line `:295`): the shape gate
over the packet, from outside the repository.

## 2. Re-run results — all green

| # | command | result | at |
|---|---|---|---|
| 1 | `python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md` | exit **0** — `INFO scan: fields=16/16 glossary-entries=20 findings=0` | 2026-10-19T03:52:51Z |
| 2 | `python3 tools/gates/handoff-packet-check.py --selftest` | exit **0** — `selftest: OK — fixture findings 11 across 9 ids`; malformed inputs exit 2; CLI verified from another cwd | 03:52:51Z |
| 3 | `python3 tools/gates/handoff-packet-check.py <abs packet>` from `.scratch/a02-foreign` (foreign cwd, the filed convention) | exit **0** — same scan | 03:55:23Z |
| 4 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline reports/round-30/handoff/declared-in-r6/expected.json --quiet` | exit **0** — `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=6ced88ad…` | 03:53:11Z |
| 5 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` (default chain) | exit **0** — identical line, same packet sha256 | 03:53:11Z |
| 6 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest --quiet` | exit **0** — positive run plus **39** controls (tamper, malformed, edge-carry, m12a/m12b baseline+read-set tamper refused) | 03:53:11Z |
| 7 | `python3 -B tools/harness/packet_links.py --packet reports/round-30/handoff/declared-in-r6/twin.json --json` | exit **0** — `links_checked 105, resolved 105, findings []` | 03:53:58Z |
| 8 | `python3 -B tools/harness/packet_uncertainty.py --packet …/twin.json --require-oq --json` | exit **0** — `claims 27, findings []` | 03:53:58Z |

Frozen-pin equality re-measured by this seat (not copied from the receipt):

- packet sha256 `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` = `freeze.txt:2` = `expected.json.packet_sha256`;
- twin sha256 `6633443d70ce44ed2bb43ab58aa60a1c98e4bbc79b2f577a63181c89dc16fd4e` = `freeze.txt:3` = `expected.json.twin_sha256`;
- the gate tool's own digest is pinned in the packet's manifest and matches live bytes: `A-17 tools/gates/handoff-packet-check.py e2fa3223b2aa5738…` (`packet.md:54`) vs `sha256sum` → `e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575`.

### 2.1 Gate controls re-run by this seat (probe, not receipt)

The gate is not a rubber stamp — three tamper probes through stdin (`…- ` accepts a packet on stdin),
all fed from an in-memory edit of the filed packet, no file written:

| probe | observed |
|---|---|
| drop the `request_ref` row | exit **1**, `FINDING HO-MISSING: FAIL — required field/section 'request_ref' absent` (2026-10-19T03:54:21Z) |
| replace every `not canonized` with `kept as a working record` | exit **1**, `FINDING HO-CANON-MARKER: FAIL — no non-canon marker` (03:55:12Z) |
| rewrite the unbound-packet sentence to "This packet is canonized by the producer" | exit **1**, `FINDING HO-CANON-CLAIM: FAIL — producer-side canon certification at line 3` (03:55:12Z) |

**Honest note on two probe-design errors of mine.** I first probed by deleting the
`- canon_standing:` line and by renaming the uppercase `NON-CANON` banner; both exited **0**.
That is not a gate defect: the marker the gate requires is the phrase `not canonized`/`not yet canonized`
(`tools/gates/handoff-packet-check.py:171` `CANON_MARKER_RE`), which the packet carries in its H1
(`packet.md:1`) and its `canon_standing` line — so my probes removed strings the gate never keys on.
Recorded here because a probe that does not exercise the mechanism proves nothing. The gate's *marker scope*
is narrower than "no canon language anywhere": an uppercase `NON-CANON` banner is house style here, not a
gate-required token.

## 3. Contract cross-check (live bytes, not the packet's self-description)

Contract identity: `corpus/knowledge/synthesis/worldbible-integration-contract.md`, sha256
`5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` (re-measured 2026-10-19T03:52Z).
That digest equals both the packet's `contract_ref` cell (`packet.md:14`) and
`expected.json.cross_refs.contract_digest`; contract ID `kotodama-lore-adjacency` and revision `1.0.0` agree.
§1's re-read trigger ("on any contract revision or pinned-digest change", `:7`) is therefore **not tripped** —
no digest drift across this boundary.

| contract clause | check | verdict |
|---|---|---|
| §4 envelope — 16 required fields (`:51-70`) | independent parse of the §4 table yields exactly 16 names; the gate's `FIELD_NAMES` tuple (`tools/gates/handoff-packet-check.py:122-140`) yields the same 16; the packet supplies all 16 (10 as `\| field \| value \|` rows, 6 as section headings: `artifact_manifest`, `dependency_manifest`, `claim_ledger`, `coupling_edges`, `requested_decisions`, `validation`) | **green** |
| §4 artifact paths stay in the delivering lane's surface (`:68`) | all 58 `A-nn` manifest rows are repo-relative; **0** absolute/`..`/`~` paths; **58/58** exist on disk; **58/58** live sha256 equal the pinned digest (script re-measure, ~03:54Z) | **green** |
| §1 both-lane read still pending (`:14-16`) | packet states the bilateral same-revision read is "still pending" (`:14`) and `open_questions` OQ-V2-02 keeps it blocking-for-first-transfer (`:300`, §open_questions at `:297`); **no read record located**: `grep -rln evidence_pointer` returns only audits that *discuss* the required fields (`reports/round-11/handoff/contract-check.md`, `reports/round-15/handoff/contract-v2-audit.md`) and lane artifacts, no `lane/contract_id/revision/file_sha256/reader/read_at` record from either lane — `to-verify` in the sense that absence is a grep result, not a lore-side attestation | **green as stated** — correctly *not* represented as complete |
| §6 canon standing stays lore's (`:92-106`) | packet carries `canon_standing: not canonized` + `handoff_status: prepared-not-accepted`, and the live source agrees (`examples/culture-d3/packet.json` → `prepared-not-accepted` / `NON-CANON`, read 03:55Z) | **green** |
| §8 submission ≠ acceptance (`:124-136`) | packet says "no lore brief, no baseline bible and no receipt surface exist" (`:3`, `request_ref: none`, `baseline_bible_ref: none`); no receipt/acceptance language anywhere in the pair | **green** |
| §9 supersession preserves filed bytes (`:138-157`) | the superseded r15 predecessor is intact and digest-pinned: `reports/round-15/handoff/packet-v2-05.md` live sha256 `24f9dd39bdadf05fcd7961d3c7b63f5aadc047330ba4b25a5bc5d61d35d38d3b` = packet `A-22` pin (`:60`); `git status --porcelain reports/round-15 reports/round-20 reports/round-30` empty | **green** |
| §10/§11 contested scope + provenance cautions (`:159-187`) | packet routes lore/baseline/rights questions to `open_questions` with owners, and claims no consultation, clearance or canon certification | **green** |
| §4 `validation`/`open_questions` = checks actually run (`:66`) | §validation lists observed rows only, naming the gate line `:295`, the read set, component digests 26/26, d4 pins 8/8; §open_questions carries 10 routed rows with owners | **green** |

**Adjacency verdict for the handoff boundary: PASS with one named content finding (§4).**
Zero unfiled bleed; nothing in the pair claims canon, clearance, or acceptance; the boundary the contract
describes (kotodama proposes and traces, lore dispositions) is intact on the live bytes.

## 4. Finding A02-H1 (named, measured, routed — not absorbed)

**The current default pair is shape-green and semantically stale.** `declared-in-r6` pins the live D4 bytes
in its manifest and then describes *older* D4 numbers in its claim ledger and open questions — the pair
contradicts itself and contradicts the live artifacts.

Measured at 2026-10-19T03:53-03:56Z:

| surface | r6 packet says | live bytes say |
|---|---|---|
| `packet.md:148` D4-CL05 | "typed_labels 74, labels_by_kind native-form 56 / translated-label 12 / borrowed-strata 6, findings_total 16, findings_hold_or_fail 15" | `examples/culture-d4/typed-labels.d4.yml#coverage` → typed_labels **82**, native-form **64** / 12 / 6, findings_total **12**, findings_hold_or_fail **12** |
| `packet.md:149` D4-CL06 | `expected-holds.json#counts (hold 15, note 1, fail 0)` | `expected-holds.json#counts` → `{'hold': 12, 'note': 0, 'fail': 0}` |
| `packet.md:150` D4-CL07 | conflicts (4), quarantine handles (3) | coverage → conflicts **0**, rank_quarantine_handles **0** (reconciliation_records 6 ✓) |
| `packet.md:152` D4-CL09 | `rank_rules_unresolved_items 13`, `rank_quarantine_handles 3`, `conflicts 4` | coverage → **0 / 0 / 0** |
| `packet.md:307` OQ-V3-05 | "twelve form holds + three rank holds + one note, thirteen unresolved rank items, three quarantine handles and four conflicts" | hold 12 / note 0; 0 / 0 / 0 as above |
| `packet.md:68` A-30 manifest row (same file) | "82 labels (64 native-form / 12 translated-label / 6 borrowed-strata), 12 findings, 0 unresolved rank items, 4 era-alias rows" | **agrees with live bytes** (`alias_rows` = 4 rows ER-01..ER-04, verified) |
| `packet.md:69` A-31 manifest row | "12 holds / 0 note / 0 fail" | **agrees with live bytes** |

The twin carries the same stale statements: `twin.json` has exactly **1** `OQ-V3-05` row whose question text repeats the stale counts, and the phrase `thirteen unresolved rank items` occurs **2** times in the twin (the OQ row and the `D4-CL09` grounding/statement), so the machine-judged twin is stale in the same places as the Markdown.

**Why every green check missed it.** The gate is shape-only: it checks envelope fields, marker, canon wording,
glossary vocabulary and digest *presence* (`tools/gates/handoff-packet-check.py:53-68`); the link resolver
checks that `path#token` targets exist, not that quoted numbers match; the e2e claim checks are vocabulary and
count checks over the rows. So 16/16 + 105/105 + 27 claims are all consistent with stale prose. This is the
same class already on record: R22-O12-SEM-1 (`reports/round-22/fixes/regression-completed.md:136`),
the hard-coded literal diagnosis (`corpus/lessons/round-25.md:82-85`; `tools/exercise-handoff-e2e.py:3524-3531`
is the `OQ-V3-05` literal, whose question text is a hard-coded string, not a read of the live artifacts;
claim map source `:184` = `reports/round-20/handoff/claims-map.md`), and the round-32 dossier's standing item
"r18 D4-adapter baseline supersession semantics (pins green, content ages)"
(`reports/round-32/dossier-d13-operator-decisions.md:138`; `reports/round-31/final-sweep.md:189`).
A02-H1 is the concrete, currently-measurable instance of that item at the handoff boundary.

**Why r5/r6 are not the round-25 fix.** `reports/round-25/v3-supersession/declared-in-r4/packet.md` carries
`hold 12, note 0` (one of the corrections), but it was never wired as the default (r25 lesson, same lines);
r5 and r6 were regenerated by the renderer from the hard-coded literals and therefore re-carry `hold 15, note 1`
— the r4 correction does not appear in the default chain. Measured: `grep -o 'hold 12, note 0'` → 1 hit in r4,
0 hits in r5/r6; `hold 15, note 1` → 1 hit in r2/r5/r6, 0 in r4.

**Disposition (this seat files it; it does not repair it).** Routed to the packet/renderer owner
(round-25 claim-O successor / round-33 claim-O integrator), because the only correct fix is a **new**
packet revision built from live bytes (contract §9: filed r2/r4/r5/r6 bytes stay frozen; corrections are new
rows), plus a renderer that reads the numbers from the live artifacts rather than a literal. Blocking status:
non-blocking for the envelope's shape and for any transfer (the packet is explicitly unbound and
`prepared-not-accepted`), blocking for reading D4-CL05/06/07/09 or OQ-V3-05 as current evidence.
No canon/clearance consequence: the stale numbers are design-debt counts, not canon claims.

## 5. Limits

- This seat ran the gate on the live tree and on a foreign cwd; the isolated-copy variant inside a clone is
  exercised by the e2e replay (row 4 above, exit 0) — I did not build a separate clone.
- I did not re-run the D4 assembler/gate legs beyond what the e2e replay covers; their pins are verified
  by the packet's own run log and the round-31 sweep, not re-derived here.
- `reports/round-33/adj/` was empty when I wrote this (no K04 method-scout fragment yet); this fragment is
  self-contained and depends on no round-33 sibling.
- The r6 pair's status as "current" is by renderer default + SCORECARD/LOG records; if the integrator
  re-points the default during round 33, this verdict applies to the r6 bytes named here and must be re-run.

## Owed: none

## Citations

- `reports/round-30/handoff/declared-in-r6/packet.md:1,3,14,54,60,68,69,148,149,150,152,279-295,297,300,307`
- `reports/round-30/handoff/declared-in-r6/{expected.json,freeze.txt,run.log,twin.json}`
- `tools/exercise-handoff-e2e.py:184,1933-1934,3524-3531`
- `tools/gates/handoff-packet-check.py:53-68,122-140,171,484-491,562-567,574`
- `tools/harness/packet_links.py`, `tools/harness/packet_uncertainty.py` (runs above)
- `corpus/knowledge/synthesis/worldbible-integration-contract.md:7,11-19,51-70,92-106,124-136,138-157,159-187`
- `PROVINCE.md:22-26`; `SCORECARD.md:400`; `LOG.md:3428`
- `reports/round-25/v3-supersession/declared-in-r4/packet.md`; `corpus/lessons/round-25.md:82-85`
- `reports/round-22/fixes/regression-completed.md:136`; `reports/round-32/dossier-d13-operator-decisions.md:138`; `reports/round-31/final-sweep.md:189`
- `reports/round-23/adjacency.md:73`; `reports/round-21/adjacency/A11-A12-handoff.md:41-50`
- commands (all 2026-10-19, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  `date -u '+AUDIT_UTC=%Y-%m-%dT%H:%M:%SZ'`; `python3 tools/gates/handoff-packet-check.py <r6 packet.md>`;
  `… --selftest`; the same gate from `.scratch/a02-foreign`; `python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline …/declared-in-r6/expected.json --quiet`;
  `… --profile v3 --quiet`; `… --profile v3 --selftest --quiet`;
  `python3 -B tools/harness/packet_links.py --packet …/twin.json --json`;
  `python3 -B tools/harness/packet_uncertainty.py --packet …/twin.json --require-oq --json`;
  three stdin tamper probes (`HO-MISSING`, `HO-CANON-MARKER`, `HO-CANON-CLAIM`);
  `sha256sum` over the contract, packet, twin, gate and the 58 manifest paths;
  `python3 -c` reads of `examples/culture-d4/{typed-labels.d4.yml,expected-holds.json}`,
  `examples/culture-d3/packet.json`, `reports/round-30/handoff/declared-in-r6/twin.json`;
  `git status --porcelain reports/round-15 reports/round-20 reports/round-30` (empty);
  `find reports -maxdepth 4 -type d -name 'declared-in*'`; `grep -o` revision comparisons across r2/r4/r5/r6.

FILES: reports/round-33/adj/A02-handoff.md | SUMMARY: handoff boundary re-run on the current pair
(`declared-in-r6`) is green (gate exit 0, 16/16 fields, 20 glossary, 0 findings; selftest + 39-control e2e +
105/105 links + 27 claims; contract digest 5f4c02bf… matches the packet's `contract_ref`), with three tamper
controls red as designed; one named finding filed — the default pair's D4-CL05/06/07/09 and OQ-V3-05 prose is
pre-family-clean and contradicts its own manifest rows and live bytes (routed to the packet/renderer owner;
fix = a new revision, never an edit of filed r2/r4/r5/r6 bytes).
