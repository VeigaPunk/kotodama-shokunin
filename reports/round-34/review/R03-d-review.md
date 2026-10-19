- Seat: R03 | reviewer | claim D | date 2026-10-19 | baseline da68a6d

# R03 — third D pass: contract §9 compliance + byte-preservation evidence

Scope of this seat: the claim-D r7 build's compliance with contract §9
(versioning / invalidation / retcon safety, `corpus/knowledge/synthesis/worldbible-integration-contract.md:138-157`)
plus §4's freeze/manifest and version rules, and an **independent** verification of
the byte-preservation evidence. No D-block builder fragment existed when this seat
read the round directory (`find reports/round-34 -type f` → `claims.json`,
`targets.json`, `telemetry/dispatch-declared.json`, plus `depth/D11-preservation.md`
which landed during this seat's run). I therefore review the *claim as declared*
and the *surfaces the build must touch*, and re-verify D11.

## Verdict (this seat)

- **Byte-preservation leg: PASS at the pre-build instant.** My own re-run of every
  D11 command reproduces its numbers exactly (§4 below). 0 changed rows, 1909/1909
  filed files byte-identical, fingerprint `1713e725…`, 0 post-commit mtimes.
- **§9 compliance leg: NOT YET COMPLIANT.** 2 blockers + 4 major findings below.
  The decisive one: the r6 ledger prose is not a rendering artifact of the packet —
  it is the content of a *pinned input file* (`CLAIMS_MAP`), so a claim-D build that
  "rewrites the claim-ledger/OQ prose" by editing the packet draft **cannot pass
  claim D's own counting command**. The route must change (F1/F2).

## 1. What §9 (and §4/§8) require of the r7 revision

| Requirement | Binding text | What r7 must carry |
|---|---|---|
| Freeze released versions; corrections are new records with `supersedes`/`derived_from`, never rewrites | `worldbible-integration-contract.md:151` | An explicit supersedes/derived_from record naming r6; r6 bytes untouched |
| Old→new record mappings | `:153` | A per-figure old→new mapping table (not just "numbers refreshed") |
| Exact delivered versions/digests, **no auto-upgrade** | `:155` | The renderer-default move is an *adopted revision*, recorded with both digests — not a silent default flip |
| Freeze the manifest before review; a changed referenced file invalidates the delivery digest | `:70` | r7's manifest rows re-measure the inputs it actually read, incl. the new claims-map |
| Revised bytes require a new version | `:55` | A `packet_version` bump (see F3) |
| Immutable bytes + digest manifest on submission | `:129` | r7 freeze.txt/expected.json + the filed predecessors stay filed |
| Change classification + downstream action | `:144-146` | r7 must state its change class and which accepted figures changed |

## 2. Findings (defects filed against the D block)

### F1 — BLOCKER: the D4 ledger prose is an input, not a render
- The packet's twelve D4 claim rows are **carried verbatim** from a filed round-20
  file: `tools/exercise-handoff-e2e.py:184` `CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"`,
  parsed by `v3_parse_claims_map` (`:2290-2320`, requires 12 rows each with
  statement/basis/links), declared in the packet at `packet.md:3`, `:125` and as
  manifest row **A-57** at `packet.md:95` (digest `4b1b9a35…`).
- The stale figures live in that map: `reports/round-20/handoff/claims-map.md:104`
  (`typed_labels 74 … native-form 56 … findings_total 16, findings_hold_or_fail 15`),
  `:116` (`hold 15, note 1`), `:124` (`conflicts (4), quarantine handles (3)`),
  `:158` (`rank_rules_unresolved_items 13 … rank_quarantine_handles 3 … conflicts 4`),
  `:251` (the `OQ-V3-05` table row). The r6 packet reproduces them at `:148`, `:149`,
  `:150`, `:152`, `:307`.
- The e2e **rejects any packet it cannot re-assemble**: the `frozen-packet` check
  compares the freshly assembled packet digest against the frozen baseline and
  raises `E2E-DIGEST` (`:3934-3939`; v1 twin of the same check at `:1486-1491`).
- Consequence: a hand-written `packet.md` (or a r4-style `build-revision.py` output)
  can never satisfy claim D's second counting command
  `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` with
  `packet_sha256 == freeze.txt`. **The corrected prose must enter through the
  renderer's inputs**, i.e. a **new** claims-map file (the round-20 one is filed and
  must not be edited, §9:151), with `CLAIMS_MAP` re-pointed at it as a drafted
  before/after block. Recommended home: `reports/round-34/handoff/claims-map.md`.
- Precedent, and why it is not a route: round 25's `declared-in-r4` was exactly a
  hand-built prose correction (`reports/round-25/v3-supersession/freeze.txt:2` —
  "NOT by tools/exercise-handoff-e2e.py — the renderer still renders 3.1.1"), and the
  subsequent renderer builds r5/r6 reverted it (`reports/round-26/handoff/declared-in-r5/packet.md:149`
  again reads `hold 15, note 1`).

### F2 — BLOCKER: `OQ-V3-05`'s prose is a hardcoded literal in the renderer
- `tools/exercise-handoff-e2e.py:3523-3532` appends OQ-V3-05 with the literal text
  "twelve form holds + three rank holds + one note, thirteen unresolved rank items,
  three quarantine handles and four conflicts". This string is not read from any
  artifact; it is compiled in, so it cannot be corrected by any claims-map or packet
  edit. Same class: the narrative strings at `:2700` (hardcoded
  `reports/round-20/handoff/claims-map.md` path in packet prose) and `:2711-2712`
  (hardcoded supersedes statement naming round-20/packet.md 3.0.0).
- These require **drafted before/after text for the integrator** (shared-file rule),
  and the draft must land *before* the r7 freeze, or the frozen packet will carry the
  stale OQ row and claim D's "zero stale figures" threshold fails on its own bytes.

### F3 — MAJOR: no version bump planned (§4:55)
- `V3_PACKET_VERSION = "3.1.1"` (`:1932`), rendered into the packet at `:2642`,
  `:2728` and into r6's `expected.json` (`packet_version: 3.1.1`). r6's packet hashes
  to `6ced88ad…`; any r7 bytes differ, so per §4:55 the release version must move
  (e.g. 3.1.2+). Claim D's text does not mention a version bump; the freeze's
  expected.json must carry the new version or the packet and its baseline disagree.

### F4 — MAJOR: no supersedes/derived_from record exists to inherit (§9:151)
- `grep -nE 'parent|supersed|derived' reports/round-26/handoff/declared-in-r5/freeze.txt reports/round-30/handoff/declared-in-r6/freeze.txt`
  → **no matches**. `v3_freeze` (`:3978-4138`) writes only a `re-frozen <key>: old -> new`
  line when the *same directory* already held an `expected.json` (`:4109`), and
  for a fresh directory it writes the boilerplate `no tracked value changed since the
  previous freeze` (`:4125`). Neither records a predecessor revision.
- So r7 must carry the supersession itself, in two places: (a) the packet narrative
  (a drafted string edit beside `:2711-2712`) naming r6 by version, packet digest
  (`6ced88ad…`), expected.json digest (`ea1e2927…`) and freeze.txt digest
  (`6fe70c0c…`); (b) an old→new **mapping** file (§9:153) whose in-repo template is
  r4's `corrections:` block (`reports/round-25/v3-supersession/declared-in-r4/freeze.txt:5-11`).

### F5 — MAJOR: predecessor accuracy (avoid repeating r6's wrong chain)
- r6's own narrative supersedes the **round-20 3.0.0** build and the round-15 v2 build
  (`packet.md:3`, `:5`), never r5, and the r5/r6 renderer builds reverted r4's
  corrections (r4 freeze.txt corrections list; `corpus/lessons/round-25.md:82-85`
  measured the same delta independently). r7's statement must therefore be: it
  supersedes the r6 default **and re-instates, at live-measured values, the semantic
  corrections of `declared-in-r4`** — naming both. Any r7 prose that claims a clean
  r6→r7 lineage hides a reverted correction and is a §9 honesty defect.

### F6 — DO-NOT-BREAK: the new claims-map must retain the m11 selftest anchor
- The e2e selftest's m11 control copies the read set and mutates `CLAIMS_MAP` on the
  exact string `the run evidence is tools/assemble-d4-typed.py --selftest exit 0 with 12/12 checks`
  (`:4381-4395`; anchor present at `reports/round-20/handoff/claims-map.md:138`), then
  asserts the edit changed the file and that assembly raises `E2E-UNC`. If the D03/D05
  rewrite of D4-CL08 drops or rewords that sentence, the **selftest assertion fails**
  (`assert edited != victim.read_text()`). The new map's D4-CL08 row must keep that
  sentence verbatim, or D10's draft must also update `:4383`.
- `v3_build_fixture_root` (`:4130-4144`) copies `V3_READ_SET` by relative path, so a
  round-34 claims-map path needs no fixture change.

### F7 — ORDERING constraint (build sequence)
- The packet's `validation` prose embeds `V3_BASELINE_DEFAULT` (`:3183-3186`), so the
  packet that r7 freezes is a function of the *default constant*. Required order:
  (1) new claims-map + the drafted constant edits (`:184`, `:1932`, `:1933-1934`,
  `:2700`, `:2711-2712`, `:3523-3532`) applied by the integrator; (2)
  `python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-34/handoff/declared-in-r7`
  into a **fresh** directory (so no in-place re-freeze of a filed path can occur);
  (3) `--profile v3 --quiet` (must read `packet_sha256 == freeze.txt`) plus the gate,
  links and uncertainty legs.
- If the defaults are flipped to a directory that does not yet exist the freeze target
  is created by `v3_freeze` (`:4077` `target.mkdir(parents=True, exist_ok=True)`), so
  flipping first is safe; flipping **after** the freeze invalidates the frozen packet
  digest (self-reference at `:3185`).

### F8 — AUDITABLE ADOPTION (§9:155, no auto-upgrade)
- The re-pin cascade must record, per surface: old default path +
  `reports/round-30/handoff/declared-in-r6/expected.json` digest `ea1e2927…` → new r7
  path + its new digest, adoption date, reason, and the fact that r6 stays filed and
  green. "The default moved to declared-in-r7" alone is not an adopted-revision
  record and would violate §9:155's no-auto-upgrade rule.

### F9 — MAJOR (audit recipe): the stale-token census is *partial*, so whole-row diffs misreport
- Measured on the filed r6 pair (packet.md / twin.json occurrences):
  `typed_labels 74` 1/1, `native-form 56` 1/1, `findings_total 16` 2/2,
  `findings_hold_or_fail 15` 1/1, `hold 15, note 1` 1/1, `conflicts (4)` 1/1,
  `quarantine handles (3)` 1/1, `rank_rules_unresolved_items 13` 1/1,
  `rank_quarantine_handles 3` 1/1, `conflicts 4` 1/1,
  `thirteen unresolved rank items` 2/2, `three quarantine handles` 2/2,
  `four conflicts` 3/3, `three rank holds` 1/1, `one note` 1/1 — **15/15 tokens present.**
- Trap for the D20/close-time audit: `translated-label 12` and `borrowed-strata 6` are
  **correct in both** stale and live states, and `hold 12` appears in the r6 rows too
  (`:148` `examples/culture-d4/typed-labels.d4.yml#stats (fail 0, hold 12, labels 74)`).
  A row-level "contains a wrong number" test therefore both over- and under-reports;
  the audit must be token-level with the six live sources below as the reference.

## 3. Live-value census (reference for D03/D18 and the close-time audit)

| Figure (r6 stale site) | r6 value | Live value | Live source (read 2026-10-19) |
|---|---|---|---|
| `typed_labels` (`packet.md:148`) | 74 | **82** | `examples/culture-d4/typed-labels.d4.yml:46` |
| `labels_by_kind.native-form` (`:148`) | 56 | **64** | `…typed-labels.d4.yml:37` |
| `labels_by_kind.translated-label` (`:148`) | 12 | 12 (unchanged — trap) | `…typed-labels.d4.yml:38` |
| `labels_by_kind.borrowed-strata` (`:148`) | 6 | 6 (unchanged — trap) | `…typed-labels.d4.yml:36` |
| `findings_total` (`:148`) | 16 | **12** | `…typed-labels.d4.yml:32` |
| `findings_hold_or_fail` (`:148`) | 15 | **12** | `…typed-labels.d4.yml:31` |
| `label_findings_hold` / `label_findings_fail` (`:148`) | — / 0 | 12 / 0 | `…typed-labels.d4.yml:34, :33` |
| `conflicts` (`:150`, `:152`) | 4 | **0** | `…typed-labels.d4.yml:30` |
| `rank_quarantine_handles` (`:150`, `:152`) | 3 | **0** | `…typed-labels.d4.yml:40` |
| `rank_rules_unresolved_items` (`:152`) | 13 | **0** | `…typed-labels.d4.yml:44` |
| expected-holds `hold/note/fail` (`:149`) | 15/1/0 | **12/0/0** | `examples/culture-d4/expected-holds.json` `counts` (sha256 `e6ae9828…`) |
| `OQ-V3-05` family (`:307`, code `:3524`) | 15 holds + 13/3/4 | 12 holds, 0 note, 0 items / 0 handles / 0 conflicts | as above |

`claims.json:27-28`'s live shorthand (82/64/12/12, hold 12/0, conflicts 0, quarantine 0)
is **correct against the bytes I read** — the "12/12" reading is
`findings_total 12` + `findings_hold_or_fail 12` (`…typed-labels.d4.yml:32, :31`).

## 4. Byte-preservation verification (independent, this seat)

My own commands, repo root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

```
$ git diff --name-only HEAD | wc -l                 -> 0
$ git status --porcelain                            -> ?? reports/round-34/
$ git ls-files <round-5..33> | xargs sha256sum | LC_ALL=C sort | sha256sum
  1713e725abbd3a73b03ff2e42a8774adcd9b8c294c458f25d4657065b126ce71  -
$ git ls-files 'reports/round-*' | wc -l            -> 1909
$ git log -1 --format=%cI HEAD                      -> 2026-10-19T03:52:53-03:00
$ find reports/round-{5,6,7,8..33} -type f -newermt 2026-10-19T03:52:53-03:00 | wc -l -> 0
$ git ls-files 'reports/**/declared-in-*' | sed 's#/[^/]*$##' | sort -u
  reports/round-22/handoff/declared-in-r2
  reports/round-23/wording/declared-in-r3
  reports/round-25/v3-supersession/declared-in-r4
  reports/round-26/handoff/declared-in-r5
  reports/round-30/handoff/declared-in-r6
```

Every value matches `depth/D11-preservation.md` (Evidence A/B/C/E/F and its path
correction). **Verdict: D11 verified by an independent seat, 0 defects.** Its Owed
item 2 (post-build re-run) is the correct home for the close-time proof.

### r7-specific witness table (for the close-time re-run)

Each digest below must still hold after the r7 build and the re-pin edits land; if
one moves, a filed or input byte was rewritten:

```
4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8  reports/round-20/handoff/claims-map.md
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182  examples/culture-d4/packet.d4.typed.yml
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
a97a0f0a0a497cb4410124607065df7686bbc7f78b4b46bdaaaa1d66ba4d1b6e  reports/round-22/handoff/declared-in-r2/packet.md
084dc5db9a8d923bb06a987b0b437bf5bfee3caac2e41cd16743da0c71499250  reports/round-23/wording/declared-in-r3/packet.md
5f58db4a52b688568eac054b1c75e9bd110843370a1943cf4353fff75b46aa03  reports/round-25/v3-supersession/declared-in-r4/packet.md
e3fb1ca500d62981b59129f898ef7e4b2843b1fa5ab7d12e8fc16818d1f764b8  reports/round-26/handoff/declared-in-r5/packet.md
6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb  reports/round-30/handoff/declared-in-r6/packet.md
6fe70c0c2b3a03ee82181a4906dc9670f73424c54efddec8fc632d213cca5d59  reports/round-30/handoff/declared-in-r6/freeze.txt
ea1e29276478477aa9e0605172723c63cd9d0b8e63e7d478896951895abda8a0  reports/round-30/handoff/declared-in-r6/expected.json
```

Pre-edit tool digests, recorded so the *expected* movement of the two shared files is
distinguishable from a preservation failure:
`a5e4a8c5dda9d63c177a3dce75a8716ba5d285371d0a37a2535f6c323e7619df  tools/exercise-handoff-e2e.py`,
`e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575  tools/gates/handoff-packet-check.py`.
These **should** change when the integrator applies the F1/F2/F3 drafts; the change
must be recorded in the round report (new digest + date + reason), not treated as a
preservation violation.

## 5. Judge note

- Claim D's preservation sub-leg verifies **now** (pre-build) and its close-time form
  is specified in §4.
- Claim D's §9 sub-leg **cannot verify on the declared route**: the counting command
  re-assembles the packet from `CLAIMS_MAP`, so unless F1's input route and F2's
  literal edit are drafted and applied, `--profile v3 --quiet` fails with `E2E-DIGEST`
  and the "zero stale figures" threshold is unmet on r7's own bytes. This is a
  route change, not a quality objection: the packet-input route is the only one that
  also satisfies §9:151 (round-20 stays filed).
- If the integrator adopts the route, the remaining §9 dossier items are F3 (version),
  F4 (supersedes + mapping), F5 (accurate predecessor naming), F8 (auditable
  adoption rows).

## Addendum — D-block landings cross-checked (same wave, after §2-§5 were written)

The D01/D02/D03/D04/D08/D10/D11/D12/D14/D16/K01/K02/P01 fragments landed while this
seat was reviewing. Re-checked against F1-F9:

- **F1 (input route) — addressed, convergently.** `D01-layout.md:149-168` drafts a new
  `reports/round-34/handoff/claims-map-v3-next.md` + the `CLAIMS_MAP` swap;
  `D02-render.md:71,:140` states independently that render/default-move alone
  re-emits the stale digits and needs one of the two input routes. My F1 therefore
  stands as the *route requirement* and is met by the drafts — the integrator must
  apply them **before** the r7 freeze (D01:262 order; D10's "order matters" note).
- **F2 (hardcoded OQ literal) — addressed.** `D04-oq-glossary.md:67-90` drafts the
  before/after for `:3523-3532` — the same range this seat corrected its own citation
  to; `D01-layout.md:176-189` and `P01-d-plan.md:64-65` carry the same edit.
- **F3 (version) — CLOSED by P01, but the drafts disagree.** `P01-d-plan.md:66-67`
  decides `3.1.1 → 3.1.2` and requires the revision paragraph to name 3.1.2 with
  3.1.1/`declared-in-r6` superseded, while **`D10-repin-drafts.md:86-94` says
  "`V3_PACKET_VERSION` stays `3.1.1` unless P01/D01 decide otherwise"** and
  `D10:306` lists it as open. Reconciliation item: the applier must follow P01
  (`:66`) and the D10 note must be read as superseded, or the frozen r7 pair will
  carry an unchanged version against new bytes (§4:55).
- **F4 (supersedes/derived_from record) — addressed in plan.** `P01-d-plan.md:185`
  requires the cascade file to name r6 + `6ced88ad…` as superseded and to carry the
  old→new mapping; `D10-repin-drafts.md:113-175` (Draft B) supplies the
  `kotodama-pin-repoint-v1` supersession rows, incl. the r6 *refusal* control. My F4
  remains as the acceptance test: r7's packet narrative itself must name r6's
  version+digest (P01:66-67), or §9:151 is only satisfied outside the packet digest.
- **F5 (predecessor accuracy) — still open, no fragment owns it.** No landed fragment
  names the r4 correction as reverted-by-r5/r6 and reinstated at live values;
  `D04-oq-glossary.md:61,271` cites `declared-in-r4/packet.md:310` as the "canonical
  prior correction" for OQ-V3-05 — the right evidence, but the r7 narrative must
  carry the three-way statement (supersedes r6 default; re-instates r4's correction
  at live values; r5/r6 renderer builds had reverted it).
- **F6 (m11 selftest anchor) — still open, no fragment owns it.** No round-34
  fragment other than this one mentions the control; `K01-packet-state.md:190` quotes
  the anchor sentence but not the control. Whoever wins the claims-map rewrite of
  D4-CL08 must keep `tools/exercise-handoff-e2e.py:4383`'s anchor verbatim in the new
  map, or the draft must update `:4383` in the same revision — otherwise
  `--selftest` fails at `assert edited != victim.read_text()` and the O-claim's
  selftest leg goes red for a D-caused reason.
- **F7/F8/F9 — no change**; F9's token census is the recommended close-time audit
  input (D18/D20).
- **New finding F10 — MAJOR (citation accuracy, P01).** `P01-d-plan.md:185`'s §9 table
  mis-cites the contract by 1-4 lines: it attributes the PATCH row to `:141` (real
  `:144`), "Freeze released versions…" to `:147` (real `:151`), "State compatibility"
  to `:149` (real `:152`), "old→new mappings" to `:151` (real `:153`), "Lore pins exact
  versions" to `:154` (real `:155`). Measured:
  `grep -n "Freeze released versions; corrections are new records\|Editorial correction with unchanged forms\|State compatibility in observable terms\|Maintain old→new record mappings\|Lore pins exact delivered versions" corpus/knowledge/synthesis/worldbible-integration-contract.md`
  → `144`, `151`, `152`, `153`, `155`. Only `:156` is correct. The integrator must
  not quote P01's §9 line numbers into `LOG.md`/receipts without fixing them; the
  requirement text itself is unaffected.

## Owed

- `reports/round-34/depth/D05-packet-draft.md`, `depth/D06-twin-expected.md`,
  `depth/D07-gate-run.md`, `depth/D09-freeze-design.md`, `depth/D13-negatives.md`,
  `depth/D15-gap-fill.md`, `depth/D17-verify-gates.md`, `depth/D19-verify-repin.md`,
  `depth/D20-verify-preservation.md`, `review/R01-d-review.md`, `review/R02-d-review.md`
  excerpts — **absent at this seat's final read**; F1's input route, F4's supersession
  block, F5, F6 and F10 must be re-checked against D05/D10's landed bytes and the
  final validator. If D05/P01 ship a hand-written packet without the applied input
  route (F1) or without the F6 anchor retention, the fragment-level verdict for
  claim D reads **rejected-route (F1/F6)**, not "pending verification".
- `reports/round-34/review/R02-d-review.md` — the pin-census pass (K02/R02) is not
  mine; I did not attempt a full `declared-in-r6` census beyond `grep -rl`, which
  returns 14 in-repo surfaces plus `.scratch/r30-run` (`grep -rn "declared-in-r6" -l`).
- `reports/round-34/run-validation.py` — does not exist yet (S04 spec). Its
  preservation leg should run the §4 command set, not restate D11's narrative.
- Post-build preservation re-run (D11 Owed 2) — owed to the integrator; §4's witness
  table is the recommended input to it.

## Citations

Contract / declaration (read-only):

- `corpus/knowledge/synthesis/worldbible-integration-contract.md` — SHA-256
  `5f4c02bfc4e6…`; `:55` (revised bytes require a new version), `:70` (freeze the
  manifest; a changed referenced file invalidates the digest), `:129` (immutable
  bytes + digest manifest), `:138-157` (§9), specifically `:144-146` (change
  classification), `:151` (freeze; supersedes/derived_from), `:153` (old→new
  mappings), `:155` (exact digests; no auto-upgrade).
- `reports/round-34/claims.json:21-36` (claim D before/after, counting commands,
  thresholds); `:68-74` (non-goals).
- `reports/round-34/targets.json:5-11` (shared rules), `:67` (this seat's row).
- `REGIMEN.md:27-43` (admit only when every claim verifies).

Builder / renderer surfaces (read-only; drafts owed to the integrator):

- `tools/exercise-handoff-e2e.py` — SHA-256 `a5e4a8c5…`; `:34,:38-39,:57` (module
  narrative naming the round-20 map), `:184` (`CLAIMS_MAP`), `:1932`
  (`V3_PACKET_VERSION = "3.1.1"`), `:1933-1934` (defaults), `:2290-2320`
  (`v3_parse_claims_map`), `:2642,:2728,:2835,:4011,:4088` (version render sites),
  `:2700` (hardcoded map path in prose), `:2711-2712` (hardcoded supersedes
  statement), `:3183-3186` (validation prose embeds `V3_BASELINE_DEFAULT`),
  `:3523-3532` (hardcoded `OQ-V3-05` literal), `:3934-3939` (`frozen-packet`
  / `E2E-DIGEST`), `:3978-4138` (`v3_freeze`; `:4109` re-freeze diff,
  `:4125` fresh-dir boilerplate), `:4130-4144` (`v3_build_fixture_root`),
  `:4381-4395` (m11 control on `CLAIMS_MAP`).
- `tools/gates/handoff-packet-check.py` — pre-edit SHA-256 `e2fa3223…` (the gate leg's
  tool; not modified by this seat).

Filed bytes relied on (read-only, never written):

- `reports/round-30/handoff/declared-in-r6/{packet.md,expected.json,freeze.txt,run.log,twin.json}`
  — `packet.md:3,:5,:95,:125,:148,:149,:150,:152,:307`; r6 digests as §4.
- `reports/round-20/handoff/claims-map.md:104,:116,:124,:138,:158,:251`.
- `examples/culture-d4/typed-labels.d4.yml:29-46` (coverage block),
  `examples/culture-d4/expected-holds.json` (`counts`, `pin_generations`,
  `supersedes_pins`).
- `reports/round-25/v3-supersession/declared-in-r4/{packet.md,freeze.txt}` — r4's
  hand-built corrections and its `corrections:` mapping block.
- `reports/round-26/handoff/declared-in-r5/packet.md:149`, `freeze.txt` — the reverted
  state and the absence of `parent|supersed|derived` lines.
- `corpus/lessons/round-25.md:82-85` (prior independent measurement of the same
  delta; advisory only), `reports/round-22/bleed/repin.md:26-37`.
- `reports/round-34/depth/D11-preservation.md:56-180,217-253` (verified by this seat).

Round-34 fragments relied on by the Addendum (read-only):

- `reports/round-34/depth/D01-layout.md:35,:54,:61,:126-129,:143-168,:176-189,:238,:248,:262,:278-292`.
- `reports/round-34/depth/D02-render.md:71,:140,:171,:179-185`.
- `reports/round-34/depth/D04-oq-glossary.md:5,:45-51,:56-90,:194,:218-229,:246,:271`.
- `reports/round-34/depth/D10-repin-drafts.md:43-48,:80-94,:113-175,:306`.
- `reports/round-34/plan/P01-d-plan.md:19-35,:60-75,:100,:180-190,:263`.
- `reports/round-34/scout/K01-packet-state.md:42,:48,:91,:190,:376`.

Commands run by this seat (all read-only; no `run-validation.py` executed in-tree;
no file outside `reports/round-34/` written):

- `git diff --name-only HEAD | wc -l` → 0; `git status --porcelain` →
  `?? reports/round-34/`; `git diff-index --quiet HEAD` → EXIT=0.
- `git ls-files <round-5..33> | xargs sha256sum | LC_ALL=C sort | sha256sum` →
  `1713e725abbd3a73b03ff2e42a8774adcd9b8c294c458f25d4657065b126ce71`;
  `git ls-files 'reports/round-*' | wc -l` → 1909.
- `git log -1 --format=%cI HEAD` → `2026-10-19T03:52:53-03:00`; mtime scan over
  round-5..33 → 0 files newer.
- `git ls-files 'reports/**/declared-in-*'` → the five homes in §4.
- `sha256sum` over the §4 witness table (14 paths) and the two tool files.
- `grep -nE 'parent|supersed|derived' reports/round-26/.../freeze.txt reports/round-30/.../freeze.txt`
  → no matches (exit 1).
- Token census over `reports/round-30/handoff/declared-in-r6/{packet.md,twin.json}`
  (15 tokens × 2 files, counts in F9) via `python3 -c` with `re.findall`.
- `grep -n "OQ-V3-05" tools/exercise-handoff-e2e.py reports/round-20/handoff/claims-map.md`
  → `:3524` and `:251` respectively.
- `grep -rl "declared-in-r6"` (excl. `.git/`, `.scratch/`) → 14 in-repo surfaces.
