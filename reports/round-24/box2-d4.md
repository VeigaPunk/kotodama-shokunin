# Round 24 — Box 2b review: D4 chain + handoff v3 — NON-AUTHOR VERIFICATION

- Reviewer: round-24 swarm seat (box-2b reviewer). **Non-author**: this seat
  authored none of the lane's artifacts, tools, or LOG entries under review.
- Date: 2026-10-18. Tree state at review: head `8fbcee9` ("round-24: declare
  GLM-2 claims C/O/D") on round-24 baseline `b5d9844` (round-23 admit);
  working tree clean before the review; no commit, no push; scratch confined
  to `.scratch/r24-box2b/` with `TMPDIR=$PWD/.scratch` exported before every
  scratch-writing command. No filed round-8..23 byte was modified.
- Scope: SHONEN box 2 ("at least one end-to-end domain task executed and
  logged in LOG.md") — the D4 + handoff portion, re-executed live per the
  round-20/21 evidence pointers named in the assignment: the D4 typed-pipeline
  gate 19/19 and the handoff e2e v3 profile.
- Canon standing: NON-CANON engineering evidence. Green gates verify
  structure, not canon or truth of claims (PROVINCE.md; the round-22 receipt
  limits, `reports/round-22/bleed/verification.json:605-609`).

## 0. Verdict

**verified-with-conditions.** The D4 chain and the handoff v3 profile execute
green at the round-24 head, and every live digest matches the newest filed
receipts byte-for-byte. Box 2's "executed and logged" requirement holds for
this portion. One condition: the admitted round-20 LOG entry misquotes the
link count ("102/102" vs the filed and live 105/105) — a dated erratum or
disposition by the integrator is owed (this seat did not edit LOG.md).

## 1. Executed live by this seat (commands, expected, observed)

Scratch evidence: `.scratch/r24-box2b/{gate-d4.out,gate-d4.err,e2e-v3.json,e2e-v3.err,battery.out}`.

| # | Command | Expected (filed pointer) | Observed live | Match |
|---|---------|--------------------------|---------------|-------|
| 1 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit 0, `summary: 19/19 legs passed` (recount `reports/round-21/recount/r18-1.md:4-7`; receipt `reports/round-22/bleed/verification.json:9-28`) | exit 0; `summary: 19/19 legs passed`; 12 `FINDING D2L-FORM-UNRESOLVED` holds, 0 NOTE; stdout 2,198 bytes, sha256 `b064da286d2dd02904788fc3fe4f3bd97fe7e88bbcac657cee114d0a607100bd`; stderr empty | **yes — stdout byte-identical to the round-22 filed receipt** (`verification.json:24` records the same sha256) |
| 2 | same gate with the declared-pipeline flags (`--assembler tools/assemble-culture-d4.py --projection examples/culture-d4/typed-labels.d4.yml --expected examples/culture-d4/expected-holds.json`, per `reports/round-21/recount/ledger.json:782`) | exit 0, 19/19 | exit 0; `summary: 19/19 legs passed` | yes |
| 3 | `python3 tools/exercise-handoff-e2e.py --profile v3 --keep .scratch/r24-box2b/packet-dir --json` | exit 0; fields=16/16, glossary=20/20, findings=0, links=105/105, claims=27, census 16/7/4, v2_subset=equal, alias_leg=landed (`reports/round-21/adjacency/A11-A12-handoff.md:41`; receipt `reports/round-22/bleed/verification.json:217-242`) | exit 0; all 16 receipt checks OK; `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=a97a0f0a0a497cb4410124607065df7686bbc7f78b4b46bdaaaa1d66ba4d1b6e`; 58 read-set files preserved | **yes — packet sha256 byte-identical to the round-22 filed receipt** (`verification.json:237-241`); the `--keep` dir was not materialized by the tool (isolated temp copy used; gate ran over the isolated copy, `gate-exit: exit 0`) |
| 4 | `python3 tools/exercise-handoff-e2e.py --profile v2 --quiet` | exit 0 (round-20 claim D: "v2 paths unchanged and green"; receipt `verification.json:266-287`) | exit 0; `handoff-v2: exit=0 claims=15 links=50/50 drift=named(tools/harness/packet_links.py round-16)` | yes |
| 5 | `python3 tools/assemble-culture-d4.py --check` | exit 0, byte-identical deterministic assembly (round-20 `run.log` d4 leg) | exit 0; `packet.d4.yml: byte-identical deterministic assembly` | yes |
| 6 | `python3 tools/assemble-d4-typed.py --check` | exit 0, byte-identical typed packet (round-20 `run.log` d4 leg) | exit 0; `examples/culture-d4/packet.d4.typed.yml: byte-identical deterministic typed packet` | yes |
| 7 | `python3 tools/d2-typed-labels.py --selftest` | 163/163 (r22 correction, LOG.md:3318-3321; receipt `verification.json:136-154`) | exit 0; `selftest: 163/163 checks passed` | yes |
| 8 | `python3 tools/assemble-d4-typed.py --selftest` | 12/12 (round-20 `run.log`; receipt `verification.json:74-95`) | exit 0; `selftest: 12/12 checks passed` | yes |
| 9 | `python3 tools/gates/typed-pipeline-gate.py --selftest` / `--selftest-generalized` | 12/12 and 14/14 (receipt `verification.json:177-215`) | exit 0; `selftest: 12/12` / `selftest-generalized: 14/14` | yes |
| 10 | `python3 tools/check-gate-battery.py` | exit 0, pass 7 / fail 0 (receipt `verification.json:289-306`) | exit 0; `summary: battery_exit 0, pass 7, fail 0, unevaluable 0`; originals preserved (0 modified) | yes |

The gate's 12 live FINDINGs are all `D2L-FORM-UNRESOLVED [hold]` rows for
GAR-01..06 / LEX-GAR-01..06 (no supplied native/borrowed form) — exactly the
`d4_form_hold_records` list and the `d4_findings_by_severity {fail 0, hold
12, note 0}` census filed in `reports/round-22/bleed/verification.json:330-348`.

Round-20 claim D's contract leg is also satisfied on the filed bytes:
`reports/round-20/handoff/audit-v3.md:194` — "Verdict: PASS-with-named-minors
on the audited build", i.e. "pass-with-named-gaps or better".

## 2. Log verification (box 2's "logged" requirement)

- **Round 11 (original e2e, D2/D3):** LOG.md:3010-3020 — O leg verified:
  "packet assembled from live D2/D3 artifacts, 16/16 fields + 20/20 glossary
  entries, handoff gate green in isolation". (The round was rejected on its
  F claim; the e2e evidence itself stands and was later superseded by v2/v3.)
- **Round 20 (e2e v3 with D4):** LOG.md:3273-3284 — "D (verified): handoff
  e2e v3"; evidence `reports/round-20/validation.json` acceptance true;
  `claims/D/measurement/v3_scan/links` records 105 (both sides).
- **Round 21 (contract re-verify):** LOG.md:3286-3296 — "A (verified):
  handoff v3 contract green on the current pair"; backed by
  `reports/round-21/adjacency/A11-A12-handoff.md:41-45` (16/16 fields, 20/20
  glossary, 0 findings, 105/105 links, 27 claims, census 16/7/4) and
  `reports/round-21/adjacency/province.md:15` (re-measured, PROVINCE
  accurate).
- **Round 22 correction (append-only):** LOG.md:3312-3324 — family-clean
  implementation present; projector `2819f687…`; "selftest 163/163, live D4
  holds 12/0/0" — all three numbers reproduce live in this review (rows 1,
  7 of the table).
- **Round 23 (current baseline):** LOG.md:3326+ — family-clean projection
  rule landed in SKILL.md; the round-24 tree reviewed here sits on that
  baseline.

The chain D2 -> D3 -> D4 -> handoff is thus both **executable now** (table
above, at the round-24 head) and **logged** (rounds 11, 20, 21, 22-correction,
with filed receipts that this seat's live digests reproduce byte-for-byte).

## 3. Findings (named; none blocks the box)

- **F1 (condition): LOG.md:3278 misquotes the link count.** The admitted
  round-20 entry says "102/102 links"; every filed artifact and the live
  rerun say 105/105: `reports/round-20/handoff/run.log:4`
  (`packet_links.py exit 0 (105/105 links resolved)`),
  `reports/round-20/validation.json` (`v3_scan/links = [105, 105]`),
  `reports/round-21/adjacency/A11-A12-handoff.md:41,45`, and this seat's live
  run (table row 3). A transcription erratum in an append-only LOG entry.
  Condition: the integrator files a dated erratum or disposition (per the
  round-22 correction precedent, LOG.md:3312). This seat did not edit LOG.md.
- **F2 (note, no action): the round-21 recount's byte-pin for the D4 gate is
  revision-specific and no longer reproduces byte-wise at head.** Recount
  `r18-1.md` pins 2,508 stdout bytes / sha `f7630ddb…` / 15 FINDING + 1 NOTE
  at the round-18/21 state; live at round-24 head: 2,198 bytes / sha
  `b064da28…` / 12 FINDING + 0 NOTE. This is expected drift, not silent
  staleness: the recount itself ran the byte-identity leg per-revision
  (`recount/audit.md:19`), the projection transition mechanism is documented
  with positive/negative replay controls in
  `reports/round-22/fixes/r18-supersession.md` (historical row 1/2 with exit 1
  at the successor revision; named successor row 2/2), and the new census is
  filed with a receipt this seat reproduces exactly
  (`reports/round-22/bleed/verification.json:24,330-348`). The gate verdict
  itself (exit 0, 19/19) is unchanged across all filed states.
- **F3 (note): 12 open GAR form holds remain design findings** on the D4
  packet (six owed garment forms). They do not fail the gate, are named in
  the receipt limits ("Green gates do not clear the six owed garment forms",
  `verification.json:607`), and predate this round. Recorded so the promotion
  dossier does not read the 19/19 as a content clearance.

## 4. Not covered by this box-2b verdict

- The D2 -> D3 leg detail, box 1 (SKILL.md tables), box 3 (cold-run), box 4
  (cross-domain bleed) — other seats.
- Canon/acceptance standing of any packet claim: kotodama hands off systems;
  lore-shokunin records and verifies them (PROVINCE.md; contract at
  `corpus/knowledge/synthesis/worldbible-integration-contract.md`).
