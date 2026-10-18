# R15-O10 — reviewer: coupling dissolution + gate/builder/audit evidence chain

- seat: **R15-O10** (reviewer, claim O, round 15 — operator regimen loop 1, GLM round 1 of 2), 2026-10-17 local (-03:00); window 21:24–22:05 local = 2026-10-18T00:24–01:05Z.
- assignment (verbatim): "O R15-O09..O10 (reviewers): adversarial — boilerplate basis = finding; dangling link = finding; aggregated coupling surviving = finding; reports/round-15/handoff/review-<n>.md."
- write scope: **this file only** (plus in-lane scratch `.scratch/r15-review/`; `TMPDIR=$PWD/.scratch` set before every scratch-writing command). No tool, packet, corpus, or filed round-8–14 byte was written; no git operation; no canon, rank, or real-world rights claim. All artifacts reviewed are NON-CANON.
- tree at review: HEAD `c60b17c`, all round-15 work untracked.
- review pin: **`packet-v2-05.md` sha256 `24f9dd39bdadf05fcd7961d3c7b63f5aadc047330ba4b25a5bc5d61d35d38d3b`, `packet-v2-05.yml` sha256 `39cf4d53b02a1a9026e3a9a302cd1031d1b6a55fc2b8ea9d7b7eb877fa1dfcd6`, both mtime 21:55:57 -0300.** The packet iterated at 21:47 and 21:52 inside the window; findings below are against the stamped bytes. If the digests no longer match the tree, re-run §4 before recording any verdict.
- sibling file: ledger-semantics detail (uncertainty/boilerplate/dangling-link) is in `review-9.md`; this file covers the coupling question and the evidence chain, and repeats only what is needed to stand alone.

## 1. Verdict — the assigned criterion

**Aggregated coupling did not survive in the stamped packet (PASS at packet level). One aggregate-coupling detector bypass exists in the harness (F10-1). Two chain elements required by the O claim have not landed (F10-2, F10-3) — this seat therefore cannot record the round-level O claim as proven; it records the packet-level criteria it was assigned.**

### 1.1 The D2 aggregate is gone, atomically (stamped bytes)

Round-12 reject reason (`reports/round-12/adjacency/contract.md:28`, quoted): "D2 is summarized as one aggregate dependency edge … That aggregate does not expose each source→target relation with its own applicability and justification." State of the stamped packet:

- `## coupling_edges` (`packet-v2-05.md:104`) holds **34 rows**: BR01–BR05 carried row-by-row from the live D3 bridge ledger, plus **D2E-01…D2E-29 — one row per live `coupling_note`** of `examples/culture-d2/packet.d2.yml` (the v1 aggregate row `D2-EDGES` appears **0** times; census of the section).
- Every edge `source` is a concrete record id — **0 non-record-id sources** (census: each source cell matches the record-id grammar; v1's "29 `coupling_note` fields over …" prose source is gone).
- Targets: 41 distinct ids, each present in the named artifact's bytes — spot-verified `R-01`, `SYN-23`, `A-03`, `M-18`, `L-36`, `L-22`, `L-13`, `L-17` in `examples/culture-d2/packet.d2.yml` (22:03 -0300). No range token is used as a target; `D2E-19` carries "deps: MAT-, GAR-" in its **limits prose only**, exactly as the section header's declared convention requires.
- Declared non-couplings (`spine-independence`) are self-targeted **by a convention declared in the section header**, not silent aggregates; the section header states the convention so no reader has to guess.
- Edge→claim crosswalk: header `| edge_id | source | relation | target_ids | claims | mechanism | limits |` (`packet-v2-05.md:108`); all 34 `claims` cells are non-empty subsets of the 15 ledger claim ids (census). Tool leg agrees: `python3 tools/harness/packet_links.py --packet reports/round-15/handoff/packet-v2-05.yml --repo-root .` → `links=50 resolved=50 findings=0`, exit 0 (22:04 -0300; the earlier 21:47 bytes produced 34 `E-EDGE-NO-CLAIM` findings — the `claims` column was the fix).

### 1.2 Shape gate on the stamped bytes

```
python3 tools/gates/handoff-packet-check.py reports/round-15/handoff/packet-v2-05.md   (22:04 -0300)
→ INFO scan: fields=16/16 glossary-entries=20 findings=0 ; exit 0
```

The claims.json requirement "handoff-packet-check still passes 16/16 + 20/20" is met on these bytes with zero findings. The mid-window failure and its fix are recorded in `review-9.md` §3 (before: `HO-CANON-CLAIM` on the A-17 role-cell wording at 21:47; after: "envelope and canon-wording kernel", `packet-v2-05.md:53`) — that before/after pair is the control for the wording fix.

## 2. Findings

### F10-1 (harness, aggregate class) — `resolve_edges()` never checks the edge `source`

`tools/harness/packet_links.py` (`resolve_edges`) validates `target_ids` concretely, flags self-declared `aggregate: true`, and enforces the claim crosswalk — but the **`source` field is never resolved**. A v1-shaped aggregate survivor — one row whose source is prose ("29 coupling_note fields over examples/culture-d2/packet.d2.yml") with concrete targets and a real claim id — passes with **zero findings**.

Reproduction (fixture packet, 21:52 -0300, lane root):

```
python3 tools/harness/packet_links.py --packet <pk1 fixture> --repo-root .
→ caught: E-TARGET-UNKNOWN (range "L-01–L-40"), E-EDGE-NO-CLAIM (ghost claim), E-EDGE-AGGREGATE (declared), M-DIGEST-MISSING ×3
→ NOT caught: edge E-AGG-SURVIVOR, source "29 coupling_note fields over examples/culture-d2/packet.d2.yml", targets [L-01, L-02], claim CL01 → no finding
```

Impact on the stamped packet: none — all 34 sources are concrete record ids (§1.1). Impact on the claim: the round-12 reject reason could regress past the harness undetected.
**Owner:** O-impl (shard-2) — resolve `source` through the record index exactly like targets. **Control:** rerun the pk1 fixture; expected after fix: `E-SOURCE-UNKNOWN`, exit 1.

### F10-2 (chain, pending dependency) — durable builder + frozen baseline not landed

claims.json after_required names "a durable builder tool with --selftest and a frozen expected.json baseline". At window close (22:05 -0300): `tools/build-handoff-v2.py` — **absent**; `reports/round-15/handoff/expected.json` — **absent**. The landed validators are `tools/harness/packet_uncertainty.py` + `packet_links.py` (both with passing selftests: 19/19, 31/31) and `reports/round-15/run-validation.py` (`--selftest` → 37/37 controls, exit 0, 21:49 -0300, receipt on stdout). The render→check→freeze loop of v2-design §6 therefore has no durable, re-runnable entry point yet.
**Owner:** O-impl + O-frozen seats. **Control:** the tool exists, `--selftest` exits 0, and a first frozen baseline file is committed in-lane; `--root` isolated tamper probes pass.

### F10-3 (chain, pending dependency) — round-12 contract-audit re-run receipt not landed

The O claim requires "the round-12 contract audit re-run over v2 yields a semantic PASS verdict (or the remaining gaps are named with owner notes)". No contract-audit receipt exists under `reports/round-15/` at window close. This reviewer deliberately makes **no** audit verdict of its own: §1 records the §4-field-level evidence this seat measured (uncertainty dimension present and populated; claim-to-record links resolving; aggregate dissolved; crosswalk present), but the audit seat's independent verdict is its own artifact.
**Owner:** O-contract-audit seat. **Control:** dated receipt file in `reports/round-15/` citing the stamped packet digests.

### F10-4 (cross-reference) — the F9-1 line-anchor trap is also a coupling risk

Edge target specs of the form `<artifact>#L01` would silently line-anchor (see `review-9.md` F9-1); coupling edges currently use bare record ids in `target_ids` (safe), but any future edge/link spec in that shape is exposed to the same bypass. One fix should close both.

## 3. What this seat verified but does not verdict

- `run-validation.py --selftest`: 37/37 controls pass (21:49 -0300), including filed-round preservation, unsafe-pointer rejection, builder-discovery skips-gates, and metric command+date carrying. The full `python3 reports/round-15/run-validation.py` run is the parent's counting command; this seat did not run it (it writes `reports/round-15/validation.json`, outside this seat's write scope).
- Shard/docs coherence: `shard-1.md`/`shard-2.md` claims about the two harness modules match the observed module behavior on every probe this seat ran, except where F9-1/F9-3/F10-1 name the gaps.
- Coverage gap F9-2 (`review-9.md`) also affects coupling completeness (18/20 lexemes and 6/6 names have no edge pointing at them); the D2 side has no such gap — its 29 notes are each an edge.

## 4. Re-run battery for the parent (if bytes changed)

```
python3 tools/gates/handoff-packet-check.py reports/round-15/handoff/packet-v2-05.md    # expect 16/16, 20, findings=0, exit 0
python3 tools/harness/packet_links.py --packet reports/round-15/handoff/packet-v2-05.yml --repo-root .   # expect 0 findings
python3 tools/harness/packet_uncertainty.py --packet reports/round-15/handoff/packet-v2-05.yml           # expect claims=15 findings=0
```

Every measurement above names its command and run time (2026-10-17 21:2x–22:05 -0300 = 2026-10-18T00:2x–01:05Z). No canon decision, no lore receipt, no transfer acceptance, and no real-world rights ruling is claimed or implied by this file.
