# R11-O12..O13 — contract check: the assembled handoff packets vs the world-bible integration contract

- seat: HANDOFF R11-O12..O13 (contract checks), round 11, 2026-10-17.
- runs: this seat's executions 2026-10-17 22:05–22:17Z (19:05–19:17 -0300).
- assignment: verify the assembled packet against
  `corpus/knowledge/synthesis/worldbible-integration-contract.md` field-by-field;
  any mismatch = a finding.
- verdict summary: every assembled packet produced so far passes the envelope
  gate (16/16 fields, 20/20 glossary entries, 0 findings, exit 0). Four findings:
  the `claim_ledger` uncertainty dimension is absent in **all five** packets
  (REVIEW); all **four** shard attempts carry an artifact-count text that
  disagrees with their own manifest (REVIEW); the exercise's first revision
  crashed its `--selftest` (defect, fixed in the current revision); and a
  mid-round legitimate re-pin of `examples/culture-d2/typed-labels.d2.yml` has
  left the exercise's frozen baseline and two packet manifests stale against
  live bytes (REVIEW — the O claim's positive run is red at handoff time).

## 0. Assembled packets and revisions verified (pins measured this seat)

| id | artifact | sha256 (full) | manifest rows / envelope count text | gate (exit) |
|---|---|---|---|---|
| A1 | `reports/round-11/handoff/packet-attempt-1.md` (O06) | `289c8ca25bbebca7708f6a15fa9b9b2b7c985d9d809693c36f47dd657c383172` | 18 rows / "15 measured artifacts" (:28) | 0 (16/16, 20/20, 0) |
| A1y | `reports/round-11/handoff/packet-attempt-1.yml` (view of A1) | — | 20 glossary rows | 0 (16/16, 20/20, 0) |
| A2 | `reports/round-11/handoff/packet-attempt-2.md` (O07) | `d59053a10f155d7e66751f5a2fc8f6e15f40d807c9bfecf4778ae33cfe430d1a` | 21 rows / "19 measured artifacts" (:28) | 0 (16/16, 20/20, 0) |
| A3 | `reports/round-11/handoff/packet-attempt-3.md` (O08) | `a5f28c20165c6964229782d7e49b37ee4bfcf4d8b17ce1f7c55445c28327e82b` | 17 rows / "16 measured artifacts" (:29) | 0 (16/16, 20/20, 0) |
| A4 | `reports/round-11/handoff/packet-attempt-4.md` (O09) | `eb7eddb56d966b233b90c68c2de5eed58b8e9d8ff57acf0a7edb2dab24ce856e` | 11 rows / "12 measured artifacts" (:26) | 0 (16/16, 20/20, 0) |
| AE | exercise packet, revision A (verified copy `.scratch/o12/exercise-packet.md`) | `2a058f7858127b98592439594c55974d93e6e672a600dd2036b47e21e71c8a63` | 9 rows / per-row counts | 0 (16/16, 20/20, 0) |

Other pins: contract `corpus/knowledge/synthesis/worldbible-integration-contract.md`
sha256 `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`; gate
`tools/gates/handoff-packet-check.py` sha256
`e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575`.

**Exercise revisions (the tool was rewritten during this check):**

- **rev A** `tools/exercise-handoff-e2e.py` 67,252 B (19:07:36 -0300): baseline
  `tools/gates/expected/handoff-exercise/r11/` (`expected.json`, `packet.md`,
  `run.log`, `freeze.txt`); packet `2a058f78…` (AE above); verified PASS at
  22:09Z. **That baseline directory no longer exists** (removed after 22:15Z);
  the `packet.md` copy I checked is preserved byte-identical at
  `.scratch/o12/exercise-packet.md`.
- **rev B** 88,516 B (19:14:22 -0300) — current: CLI
  `--selftest --root --baseline --keep --json --freeze --quiet` (no `--emit`);
  baseline `reports/round-11/handoff/expected.json` (frozen 19:13:31, 21
  read-set inputs, 20 glossary ids, expects packet
  `87523e3db7ec1b5b738f9ff38952236a76c908e96edb7a1802f4c10c39338e3c`);
  `--selftest` passes (exit 0); the positive run **exits 1** on input drift
  (finding O12-F4), so rev B has not emitted a packet to verify yet.

Instrument: `.scratch/o12-contract-check.py` (scratch, not committed) — reuses
the gate's own field recognizers (`collect_fields`, `check_glossary`,
`evaluate_text`) and then applies the §4 interpretation column per field, which
the gate does not check beyond presence/non-placeholder plus five content rules.
This is kotodama-side verification only: not lore's receipt review (§8 step 5),
not a canon decision, not bible-wide consistency.

## 1. Gate and exercise runs — recorded verdicts

| # | run | command | result |
|---|---|---|---|
| 1 | A1 direct | `python3 tools/gates/handoff-packet-check.py reports/round-11/handoff/packet-attempt-1.md` | `fields=16/16 glossary-entries=20 findings=0`, exit 0 |
| 2 | A1 isolated copy | copy at `.scratch/o12/isolated/packet.md`, gate run from that foreign cwd | same scan, exit 0 |
| 3 | A1y | `… packet-attempt-1.yml` | same scan, exit 0 |
| 4 | A2/A3/A4 direct | per file | same scan, exit 0 each |
| 5 | AE frozen copy | `… tools/gates/expected/handoff-exercise/r11/packet.md` (path since removed) | same scan, exit 0 |
| 6 | exercise rev A (22:09Z) | `python3 tools/exercise-handoff-e2e.py --emit …` | `PASS — fields=16/16 glossary-entries=20 findings=0`; frozen-packet digest matched; exit 0 |
| 7 | gate selftest | `python3 tools/gates/handoff-packet-check.py --selftest` | `selftest: OK …`, exit 0 |
| 8 | exercise rev A after the 22:13:43Z re-pin | `python3 tools/exercise-handoff-e2e.py` | **FAIL, exit 1** — `FAIL input-digest: examples/culture-d2/typed-labels.d2.yml: frozen e70ba1477dbe… live a3aa452cd5ae…` |
| 9 | exercise rev A selftest | `python3 tools/exercise-handoff-e2e.py --selftest` | **exit 1**, uncaught AssertionError (O12-F3; fixed in rev B) |
| 10 | exercise rev B selftest (22:16Z) | `python3 tools/exercise-handoff-e2e.py --selftest` | **exit 0** — positive + malformed + tamper + hazard controls all reported; F3 closed |
| 11 | exercise rev B positive (22:16Z) | `python3 tools/exercise-handoff-e2e.py --json` | **exit 1**, `code: E2E-DIGEST`, `verdict: 1 read-set file(s) changed since the baseline was frozen: examples/culture-d2/typed-labels.d2.yml` |

## 2. Field-by-field §4 verification (contract §4 table, contract lines 53–66)

Observed values cited from A1 (`reports/round-11/handoff/packet-attempt-1.md`)
and AE (`2a058f78…`, lines per the rev-A frozen copy).

| field | §4 required content | A1 | AE | verdict |
|---|---|---|---|---|
| `packet_id` | stable packet identifier | `kotodama.handoff.r11-o06.d3-live-bytes` (:21) | `kotodama.handoff.d2-d3-exercise` (:10) | pass |
| `packet_version` | immutable release; revised bytes → new version | `0.1.0-draft` + revised-bytes rule (:22) | `1.0.0-exercise` (:11) | pass |
| `contract_ref` | ID, revision, digest acknowledged by both lanes | ID `kotodama-lore-adjacency`, rev `1.0.0`, digest `5f4c02bf…` = live bytes (:23) | same, re-measured at assembly (:12) | pass (§3.1) |
| `producer` | kotodama author | shard R11-O06 named (:24) | exercise named (:13) | pass |
| `recipient` | lore recipient | `lore-shokunin` (:25) | same (:14) | pass |
| `request_ref` | scoped brief/request pointer | `none` + no-brief declaration (:26) | same (:15) | pass |
| `baseline_bible_ref` | bible revision/digest; `none` only for a deliberately unbound packet | `none` + "deliberately unbound research packet" (:27) | same (:16) | pass |
| `artifact_manifest` | IDs, paths, versions, digests, record counts; exact delivered bytes | 18 rows, all verified; count text wrong — O12-F2 | 9 rows, versions + per-row records, verified at 22:09Z; typed-labels row now stale — O12-F4 | pass with O12-F2/F4 |
| `subject_refs` | lore IDs else namespaced candidate IDs, explicitly unresolved | `cand:kotodama.d3.*`, unresolved, none guessed (:29) | 5 candidate refs with counts, unresolved (:17) | pass |
| `scope` | culture/group, region, variety, script, register, era per record | group/eras/lexicon named; "no real place" = declared region absence (:30; §5) | per-record-set scope table incl. region column | pass |
| `dependency_manifest` | exact versions/prerequisites; no floating `latest` | profile, SC1/AV1/NR1/RR1, serializer digest, no floating `latest` (:31) | sources digest-pinned, rules/assemblers named | pass |
| `claim_ledger` | statement, claim kind, provenance, evidence status, uncertainty, relation to other records | `claim_id\|kind\|evidence_status\|summary`, 13 rows; **no uncertainty dimension** (2/13 tokens) — O12-F1 | `claim_id\|kind\|evidence_status\|statement\|provenance`, 10 rows; **no uncertainty dimension** (3/10 tokens) — O12-F1 | **finding (REVIEW)** |
| `coupling_edges` | typed source→target relations, applicability, justification | BR01–BR05 (`method-transfer` ×4, `analogy`), `design-only`, limits (:33) | bridges typed, scope + provenance | pass |
| `requested_decisions` | per-record accept/defer/reject, alternatives, blockers, partial-acceptance | RD-01–RD-08; accept ≠ canonize (:34) | decisions from live records | pass |
| `validation` | checks actually run with inputs/results | observed runs inline, incl. `this envelope exit 0 fields=16/16` (:35) — reproduced as run #1 | six checks with inputs/results; gate verdict by pointer to the frozen run log | pass (AE advisory, §5) |
| `open_questions` | unresolved issues, responsible lane, blocking status | OQ-R11-A1-01…07 (:36) | OQ-01…05 with lanes/blocking | pass |

Harness summary, all five packets (22:05–22:15Z): A1 15/16, A2 14/16, A3 15/16,
A4 15/16, AE 15/16. The recurring flag is `claim_ledger` (O12-F1); A2's extra
flag is a keyword miss in this seat's `variety` check while its scope row names
fictional stages and loan layers (waived, §5). The gate's own count (16/16)
agrees with all five; it differs from this seat only on the O12-F1 dimension.

## 3. Contract cross-references beyond the envelope

### 3.1 `contract_ref` digest resolution (§1, §4)

All five packets pin `5f4c02bf…` = sha256 of the contract's live bytes
(`sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md`,
2026-10-17). That is the post-round-8 revision (`e1694ba`); the superseded
`50c4c2f2…` pin in filed round-7/9 artifacts is a known, dispositioned drift
(`reports/round-9/d3/check-diagnosis.md`) and is **not repeated** — A1–A4 name
the supersession explicitly. Bilateral same-revision read is declared pending
in all five (§1 satisfied as far as a producer can); no kotodama-side §1 read
record (`lane, contract_id, revision, file_sha256, reader, read_at,
evidence_pointer`) exists in the repo (`corpus/lessons/round-2-adjacency.md:76`).

### 3.2 §6/§8.7 canon standing

All five packets carry a `not canonized` marker and no producer-issued canon
certification (gate checks HO-CANON-MARKER/HO-CANON-CLAIM green, runs #1–#5);
AE carries the live D3 status `prepared-not-accepted`.

### 3.3 "exact delivered bytes" (§4) — manifest digests re-measured

Re-hash of every path+digest manifest row against the live file it names
(2026-10-17, 22:09Z and 22:15Z):

- A1: **18/18 match**. A4: **11/11 match**. AE: 9/9 matched at 22:09Z; now
  **8/9** — the typed-labels row is stale (O12-F4).
- A2: **20/21** (typed-labels stale). A3: **16/17** (same).
- AE's tool self-digest `38d1cba4…` = live `tools/exercise-handoff-e2e.py`
  as of rev A; rev B has different bytes (88,516 B) and was not in rev A's read
  set.

### 3.4 Glossary payload (§4/§5 + `glossary-registry-format.md` §§2, 4)

All five packets: 20 rows, ids `L01`–`L20`, every etymology carries a licensed
status (`constructed`). Cross-check against the live D3 packet
(`examples/culture-d3/packet.json`, sha `bdf635ce…`): 20/20 ids match the live
lexicon and every gloss row matches its live record (0 mismatches) — live
content, not placeholders.

### 3.5 Freeze (§9-adjacent)

- AE rev A: frozen before review at 22:08Z — `expected.json` carried
  `packet_sha256 2a058f78…`, 16 per-field digests, 20 glossary ids, 5 input
  digests, 4 tool digests; `freeze.txt` declared the expectations fixed before
  the run; the 22:09Z emission reproduced the frozen digest exactly. That
  directory has since been removed; the freeze is invalidated by O12-F4.
- Rev B: baseline now `reports/round-11/handoff/expected.json` (frozen
  19:13:31 -0300, i.e. 22:13:31Z), 21 read-set inputs, 20 glossary ids, expects
  packet `87523e3d…`; it was frozen **12 seconds before** the typed-labels
  re-pin (22:13:43Z) and therefore already disagrees with live bytes — the
  positive run exits 1.

## 4. Findings

### O12-F1 — `claim_ledger` carries no uncertainty dimension (REVIEW; all five packets)

Contract §4 requires "uncertainty" among the claim-ledger content dimensions;
the committed sample implements this as an explicit per-claim `uncertainty:`
field (13/13 claims, `examples/handoff-packet.sample.yml:203–252`). Measured
2026-10-17:

| packet | ledger header | rows | rows with any uncertainty token |
|---|---|---|---|
| A1 (:88) | `claim_id \| kind \| evidence_status \| summary` | 13 | 2 (`CL06`, `CL13`) |
| A2 (:79) | `claim_id \| kind \| evidence_status \| summary` | 10 | 3 |
| A3 (:74) | `claim_id \| kind \| system \| evidence_status \| summary` | 12 | 4 |
| A4 (:68) | `claim_id \| kind \| evidence_status \| summary` | 6 | 1 |
| AE (:66) | `claim_id \| kind \| evidence_status \| statement \| provenance` | 10 | 3 |

No packet carries an `uncertainty` column or per-claim uncertainty field.
Command: `python3 .scratch/o12-contract-check.py <packet>` → `claim_ledger | no
uncertainty dimension (uncertainty column=False; rows with uncertainty tokens
2/13)` etc. The gate cannot see this: all five exit 0. Severity REVIEW: the
dimension is absent as a field, so most claims carry no uncertainty statement at
all; fix shape = an `uncertainty` column/field per claim (as the sample has), or
a stated per-row carrier.

### O12-F2 — artifact-count text disagrees with the manifest table (REVIEW; A1–A4)

Each attempt's `artifact_manifest` envelope value states a count that differs
from its own manifest section (counted by this seat, 2026-10-17):

| packet | count text | manifest rows | delta |
|---|---|---|---|
| A1 | "15 measured artifacts" (:28) | 18 | −3 |
| A2 | "19 measured artifacts" (:28) | 21 | −2 |
| A3 | "16 measured artifacts" (:29) | 17 | −1 |
| A4 | "12 measured artifacts" (:26) | 11 | +1 |

No delivered byte is misidentified (every path+digest row verified), so this is
a text/consistency defect in the envelope summary, not a bytes defect. It
matters because §4 asks the field to identify "record counts" of the delivered
bytes. AE is unaffected (per-row counts, no total text).

### O12-F3 — exercise `--selftest` crash (DEFECT; fixed in the current revision)

On exercise rev A (67,252 B, 19:07:36) the selftest crashed, reproduced three
times (transcript `.scratch/o12/selftest-transcript.txt`), exit 1:

```
AssertionError: ["evaluated: cannot hash examples/culture-d2/components/02-phonology.yml:
[Errno 2] No such file or directory: '…/.scratch/handoff-selftest-fx25nic9/fixture/examples/culture-d2/components/02-phonology.yml'"]
```

Cause: rev A's fixture copied `FIXTURE_INPUTS = SOURCES + (GATE,
tools/assemble-d2.py, tools/assemble-culture-d3.py)` (`:1232`) but the exercise
also hashes the D2 assembler's declared component digests (9 D2 components incl.
`02-phonology.yml`, live sha256 `23500df0f97a43c8…`), which were not copied —
a fixture omission, not an assembly defect (the live-tree positive run passed,
run #6). **Status at handoff: closed by the writer's rev B (run #10, exit 0,
controls reported).** Recorded here because the claim's control was not
delivered at the time it was checked; this seat wrote no tool bytes.

### O12-F4 — mid-round re-pin of `typed-labels.d2.yml` leaves the frozen baseline and two manifests stale (REVIEW; owner O02..O05 / O14..O15)

At **22:13:43Z** the live `examples/culture-d2/typed-labels.d2.yml` changed
(`git status`: ` M`; one-line diff: `assembly.packet_sha256` `8da90b07…` →
`e0f21509…`, correcting the projection's stale packet pin to the live packet
digest `e0f21509…` = `sha256sum examples/culture-d2/packet.d2.yml`). This is the
D claim's deliberate re-pin — predicted and recorded by that shard
(`reports/round-11/depth/capability-draft.md` c7/§3, `…/repin.md`,
`…/frozen-records.md:200`; post-re-pin bytes
`a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`) — so the
change is legitimate in itself. Measured consequences:

- AE rev A baseline (frozen 22:08Z, expects `e70ba147…`) and rev B baseline
  (frozen 22:13:31Z, 12 s before the re-pin) both disagree with live bytes: the
  exercise exits 1 with `FAIL input-digest` / `E2E-DIGEST` (runs #8, #11).
- Manifest rows for that file in A2 and A3 declare `e70ba147…` → stale against
  live `a3aa452cd5ae…`; AE's row likewise. A1 and A4 do not include the file and
  remain fully digest-consistent.
- Contract §9 ("changing a referenced file invalidates that delivery's digest
  even if its filename stays unchanged") applies: the affected deliveries need a
  new `packet_version`/re-assembly, and the exercise baseline needs re-freezing
  against settled bytes — that is the O-owner's action. This seat touched no
  tool, baseline or packet byte.

Until re-freeze/re-assembly, the O claim's e2e counting command does not exit 0
on the live tree (it exited 0 at 22:09Z, before the re-pin; 22:16Z state:
exit 1).

## 5. Candidate mismatches considered and waived (reasons)

- **A1 `scope` "no real place" (no region value).** §4 asks for region per
  record; a deliberately unbound drill cannot name a canon region (lore owns
  it), and the field declares the absence explicitly — admissible under §11
  ("unknowns are not blank cells"). Not counted.
- **A2 scope keyword miss.** A2's scope row names fictional stages, lexicon and
  loan layers; this seat's harness keyword list missed "variety" there — harness
  strictness, not a packet defect.
- **AE `validation` by pointer.** The section gives the checks that ran with
  inputs/results and points to the frozen run log for the gate verdict.
  Self-validation cannot embed its own post-hoc verdict without self-reference;
  the log was committed adjacent (`run.log`). Admissible, advisory.
- **A1y (YAML view) content score.** The gate accepts it 16/16/20/0; the content
  harness is calibrated for the delivered Markdown packet and reads the yml's
  pointer-style rows as absent dimensions — harness limitation, not a defect.
- **Stale `50c4c2f2…` contract pin in filed round-7/9 artifacts.** Not present
  in any round-11 packet (§3.1); dispositioned in round 9. Not re-reported.

## 6. Limits / to-verify

- Not verified (outside a kotodama-side check): whether lore read the contract
  or issues a receipt (§8.5); whether ledger claims are true — this check judges
  envelope conformance and reference resolution, not content truth.
- The pins in §0 are the exact bytes checked. The O workstream was actively
  revising during this check (rev A → rev B at 22:14:22Z; baseline relocated
  22:13–22:15Z; AE rev-A frozen directory removed). Rev B has not emitted a
  packet because its read set is red (O12-F4); when it does, the new packet
  needs its own pass through this check.
- `to-verify`: no kotodama-side §1 read record exists
  (`grep -rln 'evidence_pointer'` → round-2 provisional text, round-8 negatives,
  the contract itself); the pending status is declared consistently in all five
  packets but the record remains unwritten.

## 7. Reproduction

```bash
export TMPDIR=$PWD/.scratch
# gate runs (§1)
for f in reports/round-11/handoff/packet-attempt-{1,2,3,4}.md; do
  python3 tools/gates/handoff-packet-check.py "$f"; done
python3 tools/gates/handoff-packet-check.py reports/round-11/handoff/packet-attempt-1.yml
python3 tools/gates/handoff-packet-check.py --selftest
# the exercise (rev B CLI): selftest green, positive red until re-freeze
python3 tools/exercise-handoff-e2e.py --selftest      # exit 0
python3 tools/exercise-handoff-e2e.py --json          # exit 1 E2E-DIGEST (O12-F4)
# field-by-field content check (scratch instrument; JSON table + SUMMARY_LINE)
for f in reports/round-11/handoff/packet-attempt-*.md; do
  python3 .scratch/o12-contract-check.py "$f"; done
python3 .scratch/o12-contract-check.py .scratch/o12/exercise-packet.md
```

Written by this seat: **this file only**
(`reports/round-11/handoff/contract-check.md`); scratch evidence under
`.scratch/o12/` (gitignored): `exercise-packet.md` (rev-A packet copy),
`selftest-transcript.txt` (rev-A F3), `isolated/` (gate isolated-copy run),
`o12-contract-check.py` (instrument). No filed artifact of earlier rounds and no
other round-11 file was modified.
