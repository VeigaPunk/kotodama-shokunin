# R16-O03 — fixer: F9-2 handoff-packet v2 lexeme/name link coverage (keyed build 07)

- seat: **R16-O03** (fixer, claim O, round 16 — operator regimen loop 1, GLM
  round 2 of 2, 16w zai glm-5.3-flash-low @ host-pinned MAX), 2026-10-17 local
  (-03:00); window 23:28–00:05 local = 2026-10-18T02:28–03:05Z.
- assignment (verbatim): "FIX R16-O03 (F9-2 link coverage): bring handoff
  packet v2 lexeme/name link coverage to design §3.2.4 (18/20 lexemes + 6
  names currently orphaned) — amend the packet (new keyed build packet-v2-07
  with re-pinned digests + frozen baseline refresh) or document the deviation
  with an owner note; gate still 16/16 + 20/20;
  reports/round-16/fixes/link-coverage.md."
- write scope: **this file**, `reports/round-16/fixes/orphan-census.py`,
  `reports/round-16/handoff/packet-v2-07.md`,
  `reports/round-16/handoff/packet-v2-07.yml`,
  `reports/round-16/handoff/expected-v2-07.json`, plus gitignored scratch
  `.scratch/r16o03/` (`TMPDIR=$PWD/.scratch` set before every scratch-writing
  command). No filed round-8–15 byte was written or edited; build 05 and
  `reports/round-15/handoff/expected.json` are byte-identical to their filed
  state (§6); no git operation; no canon, rank, or real-world rights claim.
  All artifacts here are NON-CANON.
- tree at fix: HEAD `0ce7714` ("round-16: declare GLM-2 claims C/O…"), round-16
  work untracked; sibling O-fixer's `tools/harness/packet_links.py` post-fix
  bytes landed during the window (§5).

## 0. Object under fix, stamped

| object | sha256 | note |
|---|---|---|
| `reports/round-15/handoff/packet-v2-05.md` | `24f9dd39bdadf05fcd7961d3c7b63f5aadc047330ba4b25a5bc5d61d35d38d3b` | the filed packet the fix amends via a NEW keyed build |
| `reports/round-15/handoff/packet-v2-05.yml` | `39cf4d53b02a1a9026e3a9a302cd1031d1b6a55fc2b8ea9d7b7eb877fa1dfcd6` | machine twin |
| `reports/round-15/handoff/review-9.md` | the F9-2 source (reviewer, stamped bytes) | finding: 18/20 lexemes (L03–L20), all 6 names (N01–N06), M01–M03, O02–O03, U03–U06 link-orphaned vs v2-design §3.2 rule 4 |
| `reports/round-15/handoff/v2-design.md` | `9a6057315e4a63598ab3c70209a41aa466ebbd42768308b42f40f1328ac00a26` | §3.2 rule 4: "every delivered record id … appears in ≥1 claim link or edge target — no orphan records" |

Byte-drift warning: the §0 digests still match the tree (re-checked 2026-10-18
03:00Z, §6); if they ever stop matching, re-run §4's battery before citing.

## 1. Disposition — coverage completed, not deviation-documented

The claims.json O branch offers "completed … or the deviation documented with
an owner note". This fix **completes** the coverage; no deviation note is
needed (`deviation_docs: null` in the round validator's own reading). The
reviewer's recommended fix shape is used: per-record links in the dotted
`A-02#<collection>.<record>` form, which also sidesteps the F9-1 line-anchor
collision (review-9.md §2 F9-1).

## 2. The fix — keyed build 07 (`reports/round-16/handoff/packet-v2-07.{md,yml}`)

Generated deterministically from the build-05 bytes by asserted textual
transforms (builder kept in `.scratch/r16o03/build.py`; generation stamp
**2026-10-18T02:55:01Z**; every manifest digest/byte-count re-measured live at
that stamp). Delta vs build 05:

1. **33 per-record claim links added** (dotted form, all anchored to A-02 =
   `examples/culture-d3/packet.json`, whose pinned bytes deliver every record):
   - **CL01** (+22): `A-02#lexicon.L03`…`A-02#lexicon.L20` (the 18 lexemes
     whose E0→E1 derivation the SC1 claim states — each glossary row is
     "changed by SC1" or "unchanged into E1") and
     `A-02#utterances.U03`…`U06` (the E1 spoken-form layer the claim
     describes; U06 is the ritual-citation-keeps-E0 witness).
   - **CL03** (+6): `A-02#names.N01`…`N06` — the name records NR1 governs
     (name-giving at the chosen offset).
   - **CL04** (+5): `A-02#materials.M01`–`M03` (RR1's prohibition is
     material-class-scoped; M02 is literally the `plant-cloth` record) and
     `A-02#objects.O02`–`O03` (the felt vs plant-cloth assembly garments that
     carry the material assignments the rule checks).
2. **2 links re-anchored dotted**: build 05's
   `examples/culture-d3/packet.json#L01` / `#L02` (CL01, CL02) become
   `A-02#lexicon.L01` / `A-02#lexicon.L02` — record addressing instead of the
   L-shaped selector that F9-1 showed could line-anchor; the amended packet
   now contains **zero** `path#L<n>`-shaped specs (grep sweep = 0).
3. **Keyed-build identity**: `packet_id` …`build07`, producer row
   "round-16 keyed packet build 07", dependency profile build 07, fresh
   generation stamps; manifest row **A-25 re-pinned** to the post-fix harness
   `sha256:66d854cc710f0b143e0a254d03e7f59ebce2c6b759d336ca368a9689babbd899`
   (33643 bytes; was `f81bc9f7…`, 28527 bytes). No other manifest digest moved.
4. **Validation section re-measured**: coverage row now cites the census tool
   (§3) with 0 orphans; a build-05 comparison control row records the
   before-state (33 orphans, exit 1); the link row states
   `links=83 resolved=83 findings=0`; all run stamps refreshed.

Claims, uncertainty statuses, bases, edges, glossary payload, and
requested_decisions are byte-for-byte the build-05 content (twin census: 15
claims both twins, 34 edges both, statuses supported 8 / partial 5 /
unresolved 2; link deltas exactly CL01 +22, CL03 +6, CL04 +5; total links
50 → **83**).

### Siting note for the parent (why build 07 is under `reports/round-16/handoff/`)

Round-15's `run-validation.py` `find_packet()` ranks the highest numbered
packet first, and its filed `expected.json` pins build 05's digest. A
packet-v2-0x dropped into `reports/round-15/handoff/` would silently retarget
the filed round-15 validation and fail its frozen-baseline digest check. The
round-16 validator explicitly sanctions keyed builds "under
reports/round-15/handoff/ or reports/round-16/" — the round-16 tree is used
here so the filed round-15 receipt stays reproducible forever. If the sibling
fixer lands a packet-v2-06, the same siting applies.

## 3. The standing control — `reports/round-16/fixes/orphan-census.py`

Re-runnable census (selftest 3/3): enumerates delivered D3 record ids from
`examples/culture-d3/packet.json` `id` fields (lexicon, names, utterances,
materials, objects, costumes, eras, beliefs, symbols, references, bridges,
sound_changes, speech_rules, naming_rule, rank_rules — **64** ids; the round
validator's own universe is 63 because it omits `naming_rule`/NR1, which is
covered anyway — no coverage difference), extracts carried ids from the packet
machine surface (claim-link selector tails, edge targets, sources, edge ids),
and exits 1 if any delivered id is carried by neither. Definition note: build
05's own inventory wording counts edge ids as carriers; the strict §3.2.4
letter (claim link or edge target) additionally leaves BR01–BR05 covered only
as edge rows — the round validator records exactly this as
`letter_rule_orphans` without failing, because the bridges are themselves the
edges that carry them.

## 4. Battery on the final bytes (all commands 2026-10-17 23:55 local = 2026-10-18T02:55Z, lane root)

| check | command | observed |
|---|---|---|
| census before | `python3 reports/round-16/fixes/orphan-census.py --packet reports/round-15/handoff/packet-v2-05.yml` | exit 1 — 64 delivered, **33 orphans** = the F9-2 list (L03–L20, N01–N06, M01–M03, O02–O03, U03–U06) |
| census after | `… --packet reports/round-16/handoff/packet-v2-07.yml` | exit 0 — 64 delivered, 56 carried in claim links, 8 edges-only (BR01–BR05, O01, O04, U01), **0 orphans** |
| shape gate | `python3 tools/gates/handoff-packet-check.py reports/round-16/handoff/packet-v2-07.md` | exit 0, `INFO scan: fields=16/16 glossary-entries=20 findings=0` |
| uncertainty | `python3 tools/harness/packet_uncertainty.py --packet …packet-v2-07.yml --require-oq` | exit 0, `claims=15 findings=0` |
| links | `python3 tools/harness/packet_links.py --packet …packet-v2-07.yml --repo-root .` | exit 0, `links=83 resolved=83 findings=0` (post-fix judge: record semantics before line anchors on JSON bytes; edge sources resolved) |
| assemblers | `python3 tools/assemble-culture-d3.py --check ; python3 tools/assemble-d2.py --check` | both byte-identical, exit 0 |
| coupling guard | `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` | exit 0, findings [] |
| round counting command (check mode, no receipt write) | `python3 reports/round-16/run-validation.py --check` | O-side: chooses `packet-v2-07` as the amended keyed build, gate 16/16+20/20, its own F9-2 census `orphans: []` with F9-2-list calibration on build 05; selftests grew 31→38 green; the only 2 claim-O failures are the validation seat's own regression-fixture authoring mismatches (§7) |

Frozen baseline refresh: `reports/round-16/handoff/expected-v2-07.json`
(schema `kotodama-frozen-run-v1`, profile `kotodama-handoff-v2/1`), all values
measured from bytes: `packet_sha256
1295f5b35c35a0c57f4e8a85800d75385fd1a1d5fe1d3e04727949407a4567d7`,
`packet_yml_sha256
717e29e5aecf4c1f5e2e154964553674cd559c7fbbddc0b5688fc489afd6438b`,
`gate_stdout_sha256
7c5810479045c26bcc3b1c7364934f53147641504a766eeffeaaec4d2d624685`
(re-measured after the pin: identical), `links {83, resolved 83, findings 0}`,
`orphan_census {delivered 64, orphans 0, exit 0}` with the build-05 control,
28 pinned input digests, `baseline_digest
e023e752d315a4bd…` (sha256 over the canonical sort-keys JSON of the payload
minus the digest key — recipe stated here so it is re-computable). It
supersedes the build-05 pins while leaving the filed round-15 bytes untouched.

## 5. Harness dependency (sibling O-fixer), observed

`tools/harness/packet_links.py` moved `f81bc9f7…` → `66d854cc…` (~02:40Z)
during this window: F9-1 closed (record semantics before line anchors on JSON
bytes; dangling `#L99` → `L-SELECTOR-UNRESOLVED`, exit 1) and F10-1 closed
(edge sources resolved: `E-SOURCE-UNKNOWN` / `E-EDGE-NO-SOURCE` /
`E-SOURCE-UNRESOLVED`); selftest 31 → **38** checks, green and deterministic.
`tools/harness/packet_uncertainty.py` unchanged (`cdcc1931…`, round-15 bytes).
Stability: 3 polls at 60s cadence (02:51–02:54Z) showed no further movement;
build 07's digests were pinned after that window. Build 05's own 34 edge
sources are all concrete record ids, so the post-fix judge stays exit 0 on the
filed packet too (verified in the round validator's run).

## 6. Filed-bytes integrity (end of window, 2026-10-18T03:00Z)

`git status --porcelain`: the only tracked modification in the lane is
`tools/harness/packet_links.py` (the sibling fixer's sanctioned change, §5);
no file under `reports/round-8` … `reports/round-15` is modified. The build-05
twins still hash `24f9dd39…` / `39cf4d53…` exactly as `reports/round-15/
handoff/expected.json` pins them. No commit or push was made.

## 7. Named remainders for the parent (not this seat's writes)

- `reports/round-16/validation.json` (23:53:59) predates packet-v2-07
  (23:55:28) and reads `acceptance_checks_passed: false`; the counting command
  must be re-run on the settled tree. Its two claim-O failures are the
  validator's own fixture authoring, not packet or harness defects: (a) the
  aggregate-source fixture edge also lacks `target_ids` and `claims`, so the
  harness correctly emits four codes (`E-EDGE-NO-CLAIM`,
  `E-EDGE-NO-SOURCE`, `E-EDGE-NO-TARGETS`, `E-SOURCE-UNKNOWN`) where the
  fixture expects two; (b) the "clean"-edge harm-none fixture has an unmapped
  source and no targets/claims — a genuinely clean edge passes the judge, as
  build 07's 34 real edges do (exit 0). Owner: round-16 validation seat.
- Claim-C failures in the same check are the C shards' still-unfiled evidence
  paths — owner: C-shard/map workers.
- v2-design §6's durable builder (`tools/build-handoff-v2.py`) remains absent
  (round-15 OQ-V2-07 carries it); build 07 was produced by the asserted
  transform builder in `.scratch/r16o03/build.py` (gitignored scratch, not a
  deliverable).

## 8. What this fix does not claim

No canon standing, no lore acceptance, no transfer readiness, no real-language
clearance (CL13 stays unresolved and routed); uncertainty statuses and bases
are unchanged from build 05; the gate pass is shape-level (16/16 + 20/20),
not semantic lore review; the freshness axis-move pause is untouched.

## 9. Re-run battery

```
python3 reports/round-16/fixes/orphan-census.py --selftest
python3 reports/round-16/fixes/orphan-census.py --packet reports/round-15/handoff/packet-v2-05.yml   # exit 1, 33 orphans (F9-2 list)
python3 reports/round-16/fixes/orphan-census.py --packet reports/round-16/handoff/packet-v2-07.yml   # exit 0, 0 orphans
python3 tools/gates/handoff-packet-check.py reports/round-16/handoff/packet-v2-07.md                 # 16/16, 20, findings=0, exit 0
python3 tools/harness/packet_uncertainty.py --packet reports/round-16/handoff/packet-v2-07.yml --require-oq   # 15 claims, 0 findings
python3 tools/harness/packet_links.py --packet reports/round-16/handoff/packet-v2-07.yml --repo-root .        # 83/83, 0 findings
sha256sum reports/round-16/handoff/packet-v2-07.md reports/round-16/handoff/packet-v2-07.yml          # vs expected-v2-07.json pins
python3 reports/round-16/run-validation.py --check                                                    # O-side green (see §7 remainders)
```
