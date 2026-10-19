- Seat: A01 | executor | claim A | date 2026-10-19 | baseline 4a7aede

# A01 — r7-packet audit slice: `declared-in-r7/` packet + claims-map + `repin.json`

**Assignment** (`reports/round-35/targets.json`, seat `A01`): "Audit slice: the
declared-in-r7 packet + claims-map + repin.json — cross-domain language scan,
lore-owned references stay routed, no canon/clearance assertions." Claim A
(`reports/round-35/claims.json:54-65`).

**Write scope:** this file only. Every command below is read-only (`sha256sum`,
`grep`, `awk`, `sed`, `git rev-parse/status`, `date`, `python3 -B` over the
harness tools). No git commit/push, no filed byte edited, no corpus/tools write,
no `--freeze` of declared-in-r7, and **no `reports/round-*/run-validation.py`
was executed in-tree**. Commands ran with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

**Snapshot.** `git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`
(= declared baseline, `reports/round-35/claims.json:9`); `git status --porcelain`
→ only `?? reports/round-35/` (tree clean at HEAD otherwise); observation time
`date -u` → `2026-10-19T08:17:40Z`.

## 1. Surface inventory — every digest claim re-measured

Seven files are in this slice. Live `sha256sum` at the snapshot:

| path | live sha256 | digest claimed at | resolves |
|---|---|---|---|
| `reports/round-34/handoff/declared-in-r7/packet.md` | `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` | `repin.json:14`, `expected.json:192`, `freeze.txt:2` | yes |
| `…/declared-in-r7/twin.json` | `0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599` | `repin.json:27`, `expected.json:195`, `freeze.txt:3` | yes |
| `…/declared-in-r7/expected.json` | `bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55` | `repin.json:28` | yes |
| `…/declared-in-r7/freeze.txt` | `3969954bd817f5ab00137c018c82d6642fa15ac8dedc856ff1b761c9716c1223` | `repin.json:29` | yes |
| `…/declared-in-r7/claims-map.md` | `d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c` | `repin.json:30`, `expected.json:169`, `freeze.txt:10` | yes |
| `…/declared-in-r7/run.log` | `ffae4ecdcf2558693e9ace21e918572e84d6be6607a5b8a5284805ab7e11136c` | not digest-claimed (informational) | n/a |
| `reports/round-34/handoff/repin.json` | `1022b603d343abdcdb2dd1823ae42db44d2b35fb0ca676650ec2d970fa4e9458` | self | n/a |
| `tools/exercise-handoff-e2e.py` (the surface `repin.json:12` pins) | `34c85f5773fb1925ff7d454f873a2e88fa8246af10c6830468041dd44452eea9` | `repin.json:12` `surface_sha256_after` | yes |

Also re-measured: `expected.json`'s `inputs` block (`expected.json:124-183`,
58 members) against live bytes → **58 checked / 0 mismatched / 0 missing**; and
`repin.json:17`'s `surface_sha256` for the r6 baseline
(`reports/round-30/handoff/declared-in-r6/expected.json`) → live
`ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0`, equal.

**Verdict:** 8/8 digest claims resolve; no digest drift in the audited slice.

## 2. Cross-domain language scan (method + classified hits)

Method: per-family regex sweeps over all seven surfaces, then hit-by-hit manual
classification (negation / routing / source-block name / link spec / technical
usage / bleed). Families are the `PROVINCE.md:16-20` refuses list plus the
canon/clearance/promotion/closure families the claim A threshold names.

| family | packet.md | claims-map.md | twin.json | expected.json | repin.json | classification |
|---|---|---|---|---|---|---|
| `canon\w*` | 18 | 9 | 8 | 1 | 2 | negation, lore-ownership routing, source-block names, gate code `D3-CANON`, link spec `packet.d4.yml#canon`; **one class filed as A01-F1** |
| clearance/permission/consultation/rights/attribution/licence | 10 | 7 | 10 | 0 | 1 | all negations or factual source descriptions |
| promotion/ratification/approval/sign-off | 12 | 2 | 12 | 0 | 0 | all negations or alternatives offered to lore |
| closure/finalization | 7 | 2 | 4 | 1 | 1 | filed-round status, engineering closure of a routed wart, mathematical set, carried D2 record id |
| lore/world-bible/entity-key/chronology | 26 | 6 | 11 | 4 | 2 | routing or negation (§3) |
| out-of-repo path (`/home/`, `../`, sibling) | 1 | 0 | 0 | 0 | 0 | `packet.md:16` recipient field only |
| game-dev (game/sprite/tile/unity/godot/hitbox) | 0 | 0 | 0 | 0 | 0 | zero real hits — matches are the substring in "textile" (`packet.md:139`, `:164`; `twin.json:945`, `:1234`) |
| chousa (research method/methodology/literature review) | 0 | 0 | 0 | 0 | 0 | zero |
| kake (web publishing/deploy/website/hosting) | 0 | 0 | 0 | 0 | 0 | zero |
| kotoba (prompt/skill craft/tool schema/agent config) | 0 | 0 | 0 | 0 | 0 | zero |
| fleet protocol (`.ufo`/swarm/dispatch/worker) | 0 | 0 | 0 | 0 | 0 | zero; "seat" appears 6× as in-lane process reference (`packet.md:324` glossary gloss "assembly seat" for L09 `ruma`; `claims-map.md:18,51,135,234,242`) |

Representative classified hits (the ones a reader would stop on):

- `packet.md:7` `canon_standing: not canonized — lore disposition required
  (lore-shokunin owns canon)` — negation **plus** routing.
- `packet.md:18` `baseline_bible_ref | none — … cannot be imported as canon
  without a lore baseline and a new reviewed handoff` — negation plus routing.
- `packet.md:254` `accept always means retain as non-canon candidate material;
  it never means canonize` — explicit negation, the strongest anti-assertion
  line in the packet.
- `packet.md:276` `not bible-wide consistency and not a canon decision
  (contract §8 step 3)` — negation of exactly the two lore-owned axes.
- `packet.md:143` (CL13) / `:299` (OQ-V2-01) — the real-language sweep and
  community consultation are **not** performed; clearance is routed, never
  inferred.
- `packet.md:139` `findspot dating is the museum catalogue's own attribution,
  and no independent re-dating … is claimed` — "attribution" as a factual
  statement about a source record, not a rights/attribution ruling
  (`PROVINCE.md:17-18`).
- `packet.md:306` `closed by the O seat's landed per-family resolution … retained
  only as the re-open id if the O bytes are reverted` — an engineering closure of
  a routed wart with a stated re-open condition, not a round or canon closure.
- `packet.md:165` `NR1 declares a closed discrete set allowed_offsets [2, 8, 20]`
  — mathematical "closed".
- `expected.json:184` `"pins computational inputs only; not lore acceptance, not
  canon, not completion of the round arc"` — negation of all three.
- `repin.json:5` `"NON-CANON engineering evidence; a pin is integrity, never
  truth and never clearance"` and `:53` `"pins the cascade surfaces only; not
  canon, not lore acceptance, not round admission"` — explicit negations; the
  pin's own canon field refuses exactly the `PROVINCE.md:16` refusal.

## 3. Lore-owned references stay routed (not absorbed)

Every lore-owned item reachable from the three surfaces maps to a routing row in
`requested_decisions` (`packet.md:252-272`) or `open_questions`
(`packet.md:297-308`):

| lore-owned item (`PROVINCE.md:9-25`) | mention in the audited surfaces | routed row | verdict |
|---|---|---|---|
| canon standing | `packet.md:1,3,7,8,254,276`; `claims-map.md:22,56,60`; `repin.json:5,53` | `RD-01`…`RD-08`; `canon_standing` field | routed, never asserted |
| truth status of attributed beliefs / world-fact | `packet.md:259` (RD-02), `:302` (OQ-V2-04) | RD-02 + OQ-V2-04 | routed |
| world-bible entities / entity keys / baseline bible revision / receipt surface | `packet.md:16,18,19` (12 namespaced candidates, all unresolved), `:265` (RD-08), `:272` (RD-D4-05), `:300` (OQ-V2-02), `:308` (OQ-V3-06) | RD-08, RD-D4-05, OQ-V2-02, OQ-V3-06 | routed |
| chronology / dates | `packet.md:261` (RD-04, "no calendar exists; dates are lore's decision"), `:269` (RD-D4-02) | RD-04, RD-D4-02 | routed |
| bible-wide consistency | `packet.md:276` | refused by negation (contract §8 step 3) | refused, not absorbed |
| clearance / rights / community consultation | `packet.md:143,154,299`; `claims-map.md:158-164` | OQ-V2-01, RD-06, D4-CL11 | routed |
| lore acceptance of the envelope | `packet.md:8` (`prepared-not-accepted`, live value resolves at `examples/culture-d3/packet.json:362`); `expected.json:184`; `repin.json:53` | `handoff_status` + limits | refused by negation |
| bilateral same-revision read (contract §1) | `packet.md:14` ("still pending"), `:300` ("does not represent the acknowledgment as complete") | OQ-V2-02 | routed, not absorbed |

Unresolved claims (4: `D2-CL02`, `CL13`, `D4-CL09`, `D4-CL12`) each carry an
`open_questions` row naming them (`packet.md:301,299,307,308`) — re-verified
fresh in §8 (`--require-oq` exit 0, findings `[]`).

Source-resolution spot-checks of the routing text's own citations: `prepared-not-accepted`
resolves (`examples/culture-d3/packet.json:362`); the D4 canon wording resolves
(`examples/culture-d4/packet.d4.yml:1-2`, `name: "D4 culture drill — round-17
design build (NON-CANON)"`, `canon: "not canonized (D4 NON-CANON design drill)"`).

## 4. The machine twin is not an independent language surface

`twin.json` is the re-parsed projection of the delivered tables
(`packet.md:289`). Its canon/clearance/promotion hits are verbatim carries of
ledger rows and edge `limits` text (`twin.json:1019,1021,1139,1141,1203,1205`,
etc.), so it introduces no wording of its own. The one closure-family token that
looks novel — `"ACCOUNT-CLOSURE"` (`twin.json:130`) — sits inside
`artifact_manifest[9].record_ids` (187 tokens) and resolves to a **D2 packet
record id** (`examples/culture-d2/packet.d2.yml:1671`), i.e. the coverage-index
mechanism `claims-map.md:176-203` declares. Verdict: green.

## 5. Findings

### A01-F1 (named; severity low — technical usage) — affirmative "canonical E0–E3 tag(s)"

- **Sites:** `claims-map.md:122` (statement), `claims-map.md:127` (basis),
  `packet.md:151` (the D4-CL08 row, statement and basis), carried into
  `twin.json:1139,1141`.
- **Origin:** `examples/culture-d4/typed-labels.d4.yml:319` — "the normalized
  rank records already use the canonical tags, so the map is identity for every
  rule emitted here".
- **Reading:** "canonical" here means *the era tag from the packet's own era
  space* as opposed to a legacy alias handle (`packet.md:151`, `claims-map.md:119-128`).
  It asserts nothing about lore canon.
- **Why it is filed rather than passed over:** claim A's threshold is "no
  promotion/canon/clearance/closure language in the new artifacts outside
  negations" (`reports/round-35/claims.json:60`). This is canon-family language
  outside a negation, so it is recorded here with its exact sites.
- **Owner / disposition:** owner A03 (the `examples/` origin) for any wording
  decision; **no byte change recommended in this slice** — the packet carries the
  D4-CL08 statement and basis verbatim under the clause grammar
  (`packet.md:125`), so dropping the word would break the verbatim-carry rule.
  State: routed, non-blocking.

### A01-F2 (named; informational) — R34-N1 mechanism, refined from `repin.json`'s wording

- **What `repin.json:21` records:** `KeyError: 'reports/round-20/handoff/claims-map.md'`
  — "the moved CLAIMS_MAP leaves the r6 row's read-set member unresolvable".
- **What the r34 renderer shows (static read at `34c85f57…`):** `V3_READ_SET`
  includes `CLAIMS_MAP` = `reports/round-34/handoff/declared-in-r7/claims-map.md`
  (`tools/exercise-handoff-e2e.py:184`, listed at `:1957`), while the r6
  baseline's `inputs` block names `reports/round-20/handoff/claims-map.md` pinned
  at `4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8`. Set
  diff of the two input maps: exactly one member each way (r6-only: the round-20
  map; r7-only: the r7 successor map).
- **Failure path:** `:3819`
  `assembly.digests.get(rel) != digest` → `None != pin` → `drifted` non-empty →
  `:3822` `assembly.digests[rel]` → **KeyError** on the absent key. So the
  refusal (exit 1) is correct, the mechanism is the unhandled KeyError, and the
  site is the *reporting* branch of the drift check, not the comparison itself.
- **Refinement the O-claim hardening should carry:** `reports/round-20/handoff/claims-map.md`
  **still exists** (24,888 bytes) and its live digest still equals the r6 pin
  (`4b1b9a35…`, measured this seat) — the member is unresolvable because it left
  the **read set**, not because the file vanished or drifted. A fix that merely
  re-adds the file to the read set would reproduce neither `E2E-DIGEST` nor the
  new `E2E-READSET` class; the diagnostic must distinguish "member not in the
  current read set" from "member present but drifted".
- **Status of `repin.json` itself:** not a defect in its record — the refusal
  intent, the exit code and the `routed` state are recorded correctly
  (`repin.json:19-22`, `:50`). The r6 bytes stay untouched (digest match, §1).
  Owner for the hardening: the O-claim integrator (this seat only refines the
  mechanism statement).
- **Corroboration (post-hoc, sibling seat):** `reports/round-35/scout/K03-keyerror-path.md`
  (K03, claim O) landed while this fragment was being written and independently
  reaches the same conclusion by a different route — an isolated-copy replay
  (exit 1, traceback `:4613` → `:4578` → `:3822`), the same one-member-each-way
  set diff, and the same "membership, not content drift" reading
  (`K03-keyerror-path.md:60-83`). K03 adds two details this slice did not
  measure and does not dispute: the exit `1` is CPython's uncaught-exception
  status rather than `EXIT_FAIL` (`tools/exercise-handoff-e2e.py:112-114`), so an
  acceptance leg asserting only `exit == 1` does not discriminate; and
  `E2E-READSET` occurs 0 times at HEAD (`K03-keyerror-path.md:99-103`). No
  conflict with A01-F2 — the two records are consistent and complementary.

## 6. PROVINCE conformance for this slice

- Every path referenced by the three surfaces is in-repo and in-lane:
  `reports/round-34/handoff/**` (`PROVINCE.md:11`, this lane's own reports),
  `examples/**` (`PROVINCE.md:11`, non-canon examples), `tools/**`
  (`PROVINCE.md:11`, this lane's own gates),
  `corpus/knowledge/synthesis/worldbible-integration-contract.md`
  (`PROVINCE.md:10,22-25`, the lane's own adjacency contract).
- Zero sibling-repo / world-bible / domain-source-tree paths in the three
  surfaces (§2). The single `world-bible` token (`packet.md:16`) is the
  adjacency contract's own recipient field naming lore's ownership.
- No write outside `reports/round-34/**` by the audited artifacts: `repin.json:22`
  records "0 modified rows under reports/round-1..33, corpus/lessons,
  tools/gates/frozen", the LOG.md round-34 entry records "filed r2..r6 bytes
  untouched (P1: 0 moved protected paths)", and HEAD is clean except untracked
  `reports/round-35/` (this round's own dir).
- Refuses-list conformance (`PROVINCE.md:16-20`): no canon recording, no
  real-world rights/attribution ruling, no game mechanics, no general research
  method, no web publishing, no prompt/skill craft — all zero-hit or negation
  (§2).
- PROVINCE's owns/refuses lists themselves are seat A06's slice; this slice only
  confirms its own three surfaces are in-lane.

## 7. Verdicts (per surface, with basis)

| surface | verdict | basis |
|---|---|---|
| `declared-in-r7/packet.md` | green, one note (A01-F1) | 18 canon-family lines: all negation/routing/source-block/link-spec except the technical "canonical" at `:151`; 10 clearance lines all negations; lore items all routed (§3) |
| `declared-in-r7/claims-map.md` | green, one note (A01-F1) | 9 canon-family lines: `:22` negation, `:56,60` negation, `:61,62` source-block + link spec, `:122,127` technical (A01-F1), `:172,173` negation + routing |
| `declared-in-r7/expected.json` | green | `:184` limits is a negation; no canon/clearance language elsewhere; 58/58 inputs re-measured (§1) |
| `declared-in-r7/freeze.txt` | green | zero canon/clearance/promotion/lore tokens in 10 lines |
| `declared-in-r7/run.log` | green | zero such tokens in 14 lines |
| `declared-in-r7/twin.json` | green | all hits are verbatim carry of ledger/edge text or the carried D2 record id `ACCOUNT-CLOSURE` (§4) |
| `handoff/repin.json` | green | `:5` and `:53` are explicit negations; digest claims 8/8 resolve (§1); A01-F2 is a refinement, not a defect |

**Cross-surface verdict:** zero substantive cross-domain bleed, zero
canon/clearance assertions, all lore-owned items routed-not-absorbed; one
technical-token note filed (A01-F1) and one mechanism refinement filed (A01-F2).

## 8. Reproduced controls (fresh, this seat)

- `python3 -B tools/harness/packet_uncertainty.py --packet reports/round-34/handoff/declared-in-r7/twin.json --require-oq --json`
  → exit 0, `{"claims": 27, "findings": []}`.
- `python3 -B tools/harness/packet_links.py --packet reports/round-34/handoff/declared-in-r7/twin.json --repo-root . --json`
  → exit 0, `{"links_checked": 105, "resolved": 105, "findings": []}`.
- 12-row re-extraction from `claims-map.md` → `packet_uncertainty.py --claims-json`
  → exit 0, `{"claims": 12, "findings": []}` — independently reproduces the
  file's own `verified-at` claim (`claims-map.md:23-31`).
- `sha256sum` over the seven slice files + the renderer → 8/8 match the claimed
  digests (§1); `expected.json` inputs → 58/58 match.
- **Not run, by rule:** any `reports/round-*/run-validation.py`; any `--freeze`
  of declared-in-r7 (bytes stay pinned).

## Owed

- `reports/round-35/scout/K04-touched-census.md` — did not exist at this seat's
  run time (`ls reports/round-35/` → `claims.json`, `targets.json`, `telemetry`
  only; no `adj/` or `scout/` directory existed). This slice is self-contained:
  the touched-surface identity for my three artifacts was established
  independently from `repin.json`'s own rows (`repin.json:7-40`), the LOG.md
  round-34 entry, and git. Integrator follow-up: cross-check K04's risk-class
  assignment for the r7 packet against §5 — if K04 classes the "canonical" token
  as a bleed rather than a technical usage, A01-F1 is the filed site list to
  reconcile.

## Citations

**Paths (line references are to the snapshot in §1):**
- `reports/round-35/claims.json:9,54-65`
- `reports/round-35/targets.json` (seat `A01` object; `shared_rules` array)
- `reports/round-34/handoff/declared-in-r7/packet.md:1,3,7,8,14,16,18,19,125,139,143,144,151,154,155,165,252-272,254,259,261,263,265,267,269,270,272,276,289,297-308,299,300,301,302,306,307,308,324`
- `reports/round-34/handoff/declared-in-r7/claims-map.md:20-22,23-31,56,60,61,62,119-128,122,127,139-143,156-164,166-174,172,173,176-203,234,236,238-242`
- `reports/round-34/handoff/declared-in-r7/expected.json:124-183,169,184,192,195,196-206`
- `reports/round-34/handoff/declared-in-r7/freeze.txt:1-10`
- `reports/round-34/handoff/declared-in-r7/run.log:1-14`
- `reports/round-34/handoff/declared-in-r7/twin.json:130,945,1016,1019,1021,1139,1141,1203,1205,1234`
- `reports/round-34/handoff/repin.json:5,7-14,12,14,15-22,17,19-22,21,22,23-31,26-30,32-40,34-38,41-47,49-52,50,53`
- `reports/round-35/scout/K03-keyerror-path.md:19-31,60-83,99-103` (sibling claim-O scout; corroboration cited in A01-F2 only, read after this slice's own measurements were taken)
- `reports/round-30/handoff/declared-in-r6/expected.json` (`inputs` block: `reports/round-20/handoff/claims-map.md` → `4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8`)
- `reports/round-30/handoff/declared-in-r6/packet.md` (digest `6ced88ad…`, `repin.json:18` `stale_pin`)
- `tools/exercise-handoff-e2e.py:184,1933-1934,1957,2290,2566,2779,3521-3531,3819,3822`
- `examples/culture-d3/packet.json:362`
- `examples/culture-d4/packet.d4.yml:1-2`
- `examples/culture-d4/typed-labels.d4.yml:319`
- `examples/culture-d2/packet.d2.yml:1671`
- `PROVINCE.md:9-14,16-20,17-18,22-25`
- `REGIMEN.md:25-50,60-69`
- `LOG.md` (round-34 entries: "declared-in-r7 frozen (packet `45f57132…`) … `repin.json` records the cascade"; "filed r2..r6 bytes untouched (P1: 0 moved protected paths)")
- `reports/round-33/adj/` (format precedent for this slice)

**Commands (all read-only, run at `4a7aede`, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):**
- `git rev-parse HEAD`; `git status --porcelain`; `date -u '+%Y-%m-%dT%H:%M:%SZ'`
- `sha256sum reports/round-34/handoff/declared-in-r7/* reports/round-34/handoff/repin.json tools/exercise-handoff-e2e.py reports/round-20/handoff/claims-map.md reports/round-30/handoff/declared-in-r6/expected.json`
- python3 digest script: `repin.json` claims 8/8 match; `expected.json` inputs 58 checked / 0 mismatched / 0 missing; r6-vs-r7 input set diff = 1 member each way
- python3 regex family scan over the seven surfaces (counts in §2) + hit classification
- `python3 -B tools/harness/packet_uncertainty.py --packet reports/round-34/handoff/declared-in-r7/twin.json --require-oq --json` → exit 0, claims 27, findings `[]`
- `python3 -B tools/harness/packet_links.py --packet reports/round-34/handoff/declared-in-r7/twin.json --repo-root . --json` → exit 0, links 105/105, findings `[]`
- python3 12-row re-extraction of `claims-map.md` → `packet_uncertainty.py --claims-json` → exit 0, claims 12, findings `[]`
- `grep -n` resolution checks: `prepared-not-accepted`, `not canonized`, `canonical`, `ACCOUNT-CLOSURE`
- `awk`/`sed` line checks at `tools/exercise-handoff-e2e.py:2290,2779,3521-3531,3819,3822`
