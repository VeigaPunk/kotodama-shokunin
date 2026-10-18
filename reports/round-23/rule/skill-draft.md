# R23-D01..D03 — SKILL.md family-clean projection rule: consolidated draft

- Assignment: D R23-D01..D03 (rule drafters x3); deliverable is this draft plus
  the three review fragments (`fragment-D01.md`, `fragment-D02.md`,
  `fragment-D03.md`) in this directory.
- Date: 2026-10-18. Basis: `reports/round-22/bleed/design.md` (R22-D03), its
  measured basis `reports/round-22/bleed/analysis.md`, the landed
  implementation `reports/round-22/bleed/impl.md`, and the live tree at the
  round-23 declared baseline `0e81d9d99514631d6717e1ff354d5a5a759aa980`.
- Status: **draft only — SKILL.md is not edited by workers.** The orchestrator
  lands the subsection below (round-23 claims D: "drafted by workers …, landed
  by the orchestrator"). This seat ran no round validator and no scratch-writing
  command; all verification was read-only (`git show`, `grep -n`, `sha256sum`,
  `python3 -c` JSON reads), dated 2026-10-18.
- Claim elements covered (round-23 `claims.json` D): rule statement;
  injection-point warning (unconditional D2 `build_payload`); paired controls;
  round-25 implementation commitment. Every row of the subsection is cited;
  the citation ledger is §3.

## 0. Proposed placement

Insert the subsection at the end of the typed-pipeline block: after the
"### Derivation replay — replay the family's own build, by text transform"
section (which ends at `SKILL.md:242`) and before `## Error patterns`
(`SKILL.md:244`). This continues the existing sequence (Label typing →
Claim uncertainty → Slot-label routing → Derivation replay) with the ownership
rule those sections presuppose, and matches the placement the superseded
round-22 draft proposed (`reports/round-22/bleed/skill-rule-draft.md:6`).
This draft supersedes `reports/round-22/bleed/skill-rule-draft.md`: that draft
was written before the family-clean source landed and marked its controls as
prospective; this draft cites the landed controls and pins.

## 1. The exact SKILL.md subsection (verbatim)

<!-- BEGIN R23-D SKILL SUBSECTION — lift verbatim from "### Family-clean" through the round-25 paragraph -->

### Family-clean projection — a family's owned fields cite that family's own records

A multi-family projector selects data and provenance by the input packet's
declared family **before** constructing labels, rank ledgers, coverage, or
findings. Shared parser/gate code, tool paths, and diagnostic vocabulary may be
reused; another family's fixture records, bare component citations, owner
labels, romanization schemes, residuals, or conflict findings may not appear in
family-owned fields. Identity is at least `(family, source block/component,
record id)` — `GAR-01`, `WR-01`, or `E0` alone is not an identity, and a
same-ID foreign record is never reinterpreted as a local one. A declared
linguistic borrow ledger is not permission to borrow fixture data. Determinism
is not isolation: the pre-fix D4 projection passed its canonical gate 19/19
while carrying D2's 21-component rank fixture
(`reports/round-22/bleed/repin.md:15,18`; the rejected reading "deterministic
means family-clean", `corpus/lessons/round-22.md:63`). Executable authority
`tools/d2-typed-labels.py` (family dispatch `:2837-2838`; boundary checks
`P-FAMILY-SOURCE`/`P-FAMILY-RANK` `:2636-2732`; family-boundary controls
`_selftest_family` `:2980`; selftest 163/163,
`reports/round-22/bleed/impl.md:54,70`); design authority
`reports/round-22/bleed/design.md` (R22-D03); measured defect basis
`reports/round-22/bleed/analysis.md` §C1-C3; normative boundary
`examples/culture-d4/components/01-brief.yml:55-75,111-121`; worked instance
`examples/culture-d4/typed-labels.d4.yml` with
`examples/culture-d4/expected-holds.json` (counts hold:12 / note:0 / fail:0,
`supersedes_pins` naming the pre-fix projection/projector digests).

**Injection-point warning — an embedded-fixture builder invoked before family
dispatch injects the default family into every family.** At the round-21
baseline `46a03257…`, `run_pipeline` called `build_payload()`
**unconditionally** (`tools/d2-typed-labels.py:2613` at that revision),
packaging the embedded D2 constants (`:925-1197`) through a helper with **no
packet/family argument** (`:1235-1258`); the family alias leg invoked
afterward (`:2614`) annotated the foreign ledger without making it local. An
embedded fixture needs no disk read: with `load_packet_file` replaced by a
raising sentinel, `build_payload()` still returned the exact D2 ledger,
byte-equal to the filed D4 `rank_rules` (2/2 helper probes,
2026-10-18T14:42:15Z, `reports/round-22/bleed/analysis.md` §C3). A
foreign-tree-free rebuild therefore proves dependency isolation, not data
isolation. The landed dispatch (`tools/d2-typed-labels.py:2837-2838`:
`build_payload()` only when `family == DEFAULT_FAMILY` (`:2471`), else the
packet's own `family_rank_payload`) is the shape to preserve; add every new
family leg on the family side of that line.

| Paired control (design §Required paired controls) | Positive must show | Defect it defeats — Never | Landed control | Citation |
|---|---|---|---|---|
| D2 compatibility | the baseline D2 serialized projection keeps digest `a3aa452c…`; D2 `--check`/selftests pass; a D2 rank mutation still moves D2 | achieving compatibility by disabling rank projection globally | `boundary compatibility: D2 projection keeps its exact baseline digest`; `boundary D2 control: D2 rank projection remains enabled and responds to D2 mutation` | `tools/d2-typed-labels.py:3114,:3119`; digest at `reports/round-22/bleed/analysis.md:18` |
| D4 independence | a D4 packet-only mirror is byte-identical with no `examples/culture-d2/` tree **and** poisoning the embedded D2 fixture hooks (raising sentinels) leaves D4 output identical; the pre-fix artifact is refused semantically | reading filesystem absence as data isolation (the C3 result) | `boundary: packet-only D4 mirror is byte-identical without a foreign tree`; `boundary poison control: D4 never calls embedded D2 fixture machinery`; pre-fix bytes refused `P-FAMILY-SOURCE … GAR-01.owner: foreign owner '11-costumes'` | `tools/d2-typed-labels.py:3045,:3053-3054`; `reports/round-22/bleed/analysis.md:103-110`; `reports/round-22/bleed/impl.md:64` |
| Not empty-by-default | mutating declared `RK-01` authority/property/rank moves only the corresponding D4 projection; add/remove of one valid RK row moves coverage exactly once; malformed or duplicate declared records fail closed | replacing the foreign ledger with empty arrays and calling the family clean | `boundary local control: RK-01 authority/property/rank follow the local packet only`; `boundary coverage control: … counted exactly once`; `boundary malformed local rank set … fails closed` | `tools/d2-typed-labels.py:3063,:3073,:3099`; shape checks `P-FAMILY-RANK` `:2694-2732` |
| Owner-qualified citations | an absolute foreign citation, a short component citation, or a foreign owner/scheme injected into a family-owned field is rejected, while genuine `WR-*` orthography IDs and shared tool/schema references pass | a whole-document substring ban on the family token (it would reject method provenance and the packet's own contrast declarations) and any unqualified foreign citation passing | `boundary control: deterministic D2-owned label metadata is rejected`; `boundary control: foreign label … rejected`; `boundary: D4 WR writing ids and shared engine references are not substring-banned` | `tools/d2-typed-labels.py:3011,:3024,:3032`; `WR-*` are D4's own rules, `examples/culture-d4/components/03-orthography.yml:83-90` |
| No ID-based reinterpretation | same-ID foreign records fail ownership checks while the six local owed slots still route to their garments; ordinary era tags never import foreign eras | treating a shared ID or era tag as ownership evidence (D4 `GAR-01`/`GAR-06` keep D4 ranks/text, never a foreign `RANK_RESOLUTIONS`) | `boundary explicit same-id foreign label: emit refuses and preserves … output` | `tools/d2-typed-labels.py:3109`; identity definition `reports/round-22/bleed/design.md` §Decision |
| Honest borrowed language | the six `borrowed-strata` labels keep packet-declared donors, layer refs and adaptation rules; an undeclared donor in an owned source field stays a failure | legalizing an embedded fixture block by relabeling the ledger borrowed | `boundary: label texts, kinds, owed slots and all six borrow ledgers unchanged`; D4 no-import rows `D2B-01..04` | `tools/d2-typed-labels.py:2989`; `examples/culture-d4/components/01-brief.yml:111-121` |
| Propagation/tamper | a stale projection pin, a stale expected-hold set, or one changed typed routing byte fails the gate/adapter checks; a clean regeneration passes with new rows | re-blessing pins in place, freezing while upstream moves, or letting inherited findings ride into consumers | consumers copy the projector's own finding set (`carry_findings`); frozen generation `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` (3 rows, exit 0; deployed replay 33 peer pairs, 2026-10-18T14:56:01Z); profile row `$.profiles[0]` with `repin_history[2]` binding projector+expected; stale pins refuse exit 2 `L1-profile` | `tools/assemble-d4-typed.py:276-288`; `reports/round-22/bleed/evidence/deployed-replay.json`; `tools/gates/typed-pipelines.json`; `reports/round-22/bleed/impl.md:60` |

Thresholds and cautions that are part of the rule:

- **T1 — check owned fields structurally; substring bans are not ownership
  checks.** Explanatory negative provenance ("the foreign component was not
  read"), shared engine paths, and the receiving family's own reused ID space
  are legitimate; the structural checks above are the boundary
  (`reports/round-22/bleed/design.md` §Reusable machinery;
  `reports/round-22/bleed/analysis.md:60`; control
  `tools/d2-typed-labels.py:3032`).
- **T2 — equality and isolation are independent.** A deterministic projection
  can deterministically reproduce the wrong family; a byte-equality pass never
  grounds a family-ownership claim (`reports/round-22/bleed/repin.md:15,18`;
  poison control `tools/d2-typed-labels.py:3053-3054`).
- **T3 — both halves of every pair, or the fix is cosmetic.** The mirror
  control without the poison control proves dependency isolation only; the
  poison control without a local-packet mutation control cannot distinguish
  real selection from empty-by-default (`reports/round-22/bleed/analysis.md`
  §C3; `corpus/lessons/round-22.md:53`;
  `reports/round-22/bleed/design.md` §Required paired controls).
- **T4 — obligations and history survive a data cleanup.** Removing inherited
  findings removes misattribution, not debt: the six owed garment forms remain
  held (12 holds), and the removal is recorded as new rows with before/after
  digests (`examples/culture-d4/expected-holds.json` `revision_note` +
  `supersedes_pins` → pre-fix projection `cbcf997f…`, projector `76536a92…`;
  append-only discipline
  `corpus/knowledge/verification/gate-frozen-run-standard.md:50-78,102-142`;
  keep historical verdict / current reproduction / supersession distinct,
  `corpus/lessons/round-22.md:19`).
- Cautions that are part of the rule: this is an engineering boundary, not a
  canon, lore-acceptance, or real-world rights decision — handoffs stay
  prepared-not-accepted (`reports/round-22/bleed/design.md` §Decision final
  sentence; `reports/round-22/bleed/analysis.md` §Handoff limitation). A
  family-local leg the packet does not declare is reported as an explicit
  skip, never counted as evaluated (`tools/d2-typed-labels.py:3343`;
  `reports/round-22/bleed/design.md` §3).

**Round-25 implementation commitment.** Round 22 closed REJECTED on D and
routed the remaining integration to round 25 with the full recipe
(`LOG.md:3298-3309`; `reports/round-22/routed-resolution.json`
R21-ALIAS-COERCION, R21-MTIME-TIE-BREAK). Landed at the round-23 baseline
`0e81d9d`: the family-clean projector (`2819f687…`), the regenerated D4
projection/typed packet/expected holds, the combined-source profile row
(`repin_history[2]`), and the frozen `d4-repin` generation. Committed to
round 25: (1) a superseding handoff v3 claim map/baseline — D4-CL05/06/07/09
and OQ-V3-05 still describe the removed rank passengers
(`reports/round-22/bleed/repin.md:26-37`); (2) the PLACEHOLDER_RE
validator-wording disposition, so the full historical check runs without
weakening any placeholder rule (`reports/round-22/routed-resolution.json`
R21-MTIME-TIE-BREAK); (3) any combined-source successor row (D2 live/frozen
pins, v2) not landed under round 23's O claim
(`reports/round-23/claims.json` O). Until each lands, this rule's per-row
verification status is stated as landed or pending — never retroactively
green — and filed historical wording is not rewritten
(`corpus/lessons/round-22.md:19`).

<!-- END R23-D SKILL SUBSECTION -->

## 2. Integration notes for the orchestrator

1. Lift §1 verbatim (from `### Family-clean` through the round-25 paragraph)
   into `SKILL.md` after line 242. Wording-level edits are acceptable only if
   every citation survives unchanged; the citations are the deliverable's
   teeth.
2. Do not edit `LOG.md:3298-3309` (the filed round-22 rejection wording), any
   filed round 8-22 artifact, or `reports/round-22/bleed/*`. The subsection
   cites the historical record as filed and the landed source by digest and
   line; it does not reconcile the two by rewriting either. (Fragment-D01
   finding F2.)
3. Do not claim handoff v3 105/105-with-correct-wording or the full
   historical-check green in the same landing: both are round-25 tails named
   in the commitment paragraph. The round-23 D claim's counting command
   (`python3 reports/round-23/run-validation.py`) is the orchestrator's to
   declare and run; this draft is an input to it, not a pass receipt.
4. If the selftest control labels are ever refactored, update the table's
   "Landed control" citations as a new revision of this rule — never weaken
   the paired-control wording to keep stale line numbers green (fragment-D02
   finding F5).
5. The subsection quotes short digest prefixes (`a3aa452c…`, `2819f687…`,
   `cbcf997f…`, `76536a92…`, `0e81d9d`, `46a03257…`); full values are in the
   cited reports (`analysis.md:13-18`, `impl.md:3,41-46`). Keep the prefixes
   stable; they are keyed to those reports, not to HEAD.

## 3. Citation ledger (all verified 2026-10-18, baseline `0e81d9d` unless marked)

| Citation | Verified content | Verification (command class) |
|---|---|---|
| `tools/d2-typed-labels.py:2613` at `46a03257…` | `ledger = build_payload()` — unconditional, pre-dispatch | `git show 46a03257…:tools/d2-typed-labels.py \| sed -n '2599,2615p'` |
| `:925-1197`, `:1235-1258`, `:2614` at `46a03257…` | embedded D2 constants; `build_payload` with no family argument; alias leg after | same `git show` window + `analysis.md:92-97` (§D02) |
| `tools/d2-typed-labels.py:2837-2838` | `ledger = (build_payload() if family == DEFAULT_FAMILY else family_rank_payload(packet_path, packet, family))` | `grep -n "build_payload()"` + `sed -n '2825,2845p'` |
| `:2471`, `:2486` | `DEFAULT_FAMILY = "d2"`; family detection | `grep -n DEFAULT_FAMILY` |
| `:2636-2732` | `P-FAMILY-SOURCE` / `P-FAMILY-RANK` refusal sites | `grep -n "P-FAMILY-"` |
| `:2980`, `:2989`, `:3001`, `:3011`, `:3024`, `:3032`, `:3045`, `:3053-3054`, `:3063`, `:3073`, `:3078`, `:3084`, `:3099`, `:3109`, `:3114`, `:3119`, `:3343` | family-boundary control labels in `_selftest_family` and the alias-leg controls | `grep -n 'check("boundary\|check("family'` |
| source digest `2819f687…` | live `tools/d2-typed-labels.py` | `sha256sum tools/d2-typed-labels.py` |
| live D4 artifacts | `typed-labels.d4.yml` `60b526b0…`, `packet.d4.typed.yml` `ffece0fe…`, `expected-holds.json` `3826ba68…`, counts hold:12/note:0/fail:0, `revision_note` + `supersedes_pins` → `cbcf997f…`/`76536a92…` | `sha256sum` + `python3 -c` JSON reads |
| `tools/gates/typed-pipelines.json` `$.profiles[0]` + `repin_history[0..2]` | profile pins equal live bytes; `repin_history[2]` binds projector `2819f687…` + expected `3826ba68…` | digest walk of the JSON |
| `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` | 3 rows (check/assembly/typed-pipeline gates), exit 0 rows | `head` of the manifest |
| `reports/round-22/bleed/evidence/deployed-replay.json` | 33 peer pairs, `--require-live`, 2026-10-18T14:56:01Z | JSON read |
| `examples/culture-d4/components/01-brief.yml:55-75,111-121` | D4 design_problem anti-import sentence; `no_import` `D2B-01..04` | `sed -n '55,75p;111,121p'` |
| `examples/culture-d4/components/09-costumes.yml:133-137` | `RK-01..RK-04` packet-native rank rows | `sed -n '131,139p'` |
| `examples/culture-d4/components/03-orthography.yml:52`, `:83-90` | declared scheme `D4-roman-1 …`; `WR-01..WR-07` orthography rules | `sed -n '38,53p;83,90p'` |
| `tools/assemble-d4-typed.py:276-288` | `carry_findings` copies the projector finding set into the typed packet | `sed -n '270,290p'` |
| `reports/round-22/bleed/design.md` | rule source: §Decision `:5-11`, contract `:13-21`, delta `:23-30`, controls `:32-42`, integration `:44-48`, draft rule `:50-52` | Read |
| `reports/round-22/bleed/analysis.md` | C1 `:20-69` (24/41-field census), C2 `:71-88` (74 labels, stale owners, `d2-roman` 62/74), §C3 `:103-110` (sentinel probe), `:60` (negative-provenance example), digests `:13-18` | Read |
| `reports/round-22/bleed/impl.md` | `:54,70` (163/163), `:60` (stale-pin refusal exit 2 L1-profile), `:64` (`P-FAMILY-SOURCE … foreign owner '11-costumes'` on pre-fix bytes), `:74-76` (no integrated 19/19 or 105/105 asserted by that seat) | Read |
| `reports/round-22/bleed/repin.md` | `:15,18` (pre-fix 19/19 with contamination; D2 control digest), `:26-37` (stale v3 claim wording D4-CL05/06/07/09, OQ-V3-05) | Read |
| `reports/round-21/adjacency/ledger.json:93-110` | finding `A21-D4-XF-01` (filed, unfixed at filing) | `sed -n '93,110p'` |
| `reports/round-21/adjacency/A11-A12-handoff.md:23-29,39-47` | prior census: 4 D4 RK vs 21-component projection, 24 D2 rank-source references, dated commands | `sed -n` |
| `LOG.md:3298-3309` | round-22 rejection entry; "Routed to round 25 with the full recipe" | `grep -n` + `sed` |
| `reports/round-22/routed-resolution.json` | R21-ALIAS-COERCION (combined-source successor pins deferred to the round-25 bleed-fix integration), R21-MTIME-TIE-BREAK (PLACEHOLDER_RE false positive routed to round 25) | Read |
| `corpus/lessons/round-22.md:19,53,63` | distinct verdict fields; mirror-insufficiency; rejected readings incl. "deterministic means family-clean" | Read |
| `corpus/knowledge/verification/gate-frozen-run-standard.md:50-78,102-142` | frozen layout + freeze procedure (append-only/new-row discipline) | `sed -n` |
| `reports/round-23/claims.json` | claim D wording and O claim the commitment references | Read |

## 4. Review fragments

- `fragment-D01.md` (R23-D01) — rule statement + injection-point warning;
  revision-pinned citation discipline; the LOG-vs-landed-source finding.
- `fragment-D02.md` (R23-D02) — paired-controls mapping design → landed
  embedded controls; the dependency-vs-data-isolation asymmetry.
- `fragment-D03.md` (R23-D03) — placement, style conformance, r25 commitment
  wording, orchestrator do/don't list; this ledger's audit trail.

## 5. Limits

This file is a draft for the orchestrator's SKILL.md integration. It is not a
measurement, not a gate pass, and not the round verdict; the landed controls'
own receipts (`reports/round-22/bleed/{impl.md,verification.json}`,
`deployed-replay.json`, the frozen manifest) carry the measurements it cites.
No canon, lore acceptance, real-world truth, or permission/clearance decision
is made or implied. Round-23 counts and validation belong to the orchestrator
via the claim's declared counting command.
