# R24-BOX4 — bleed verification (non-author): cross-domain boundaries on the newest content

Date: 2026-10-18. Seat: round-24 box-4 (bleed) reviewer. I am a **non-author**:
I authored none of the lane's artifacts reviewed here. Assignment: verify
SHONEN box 4 ("no cross-domain bleed; `PROVINCE.md` accurate") by
independently re-checking the cross-domain boundaries on the newest content —
the rounds 19–23 LOG entries, the D4 artifacts, and handoff v3 — and account
for the filed D2→D4 bleed tail in the verdict, as a named condition, not
silently.

This file is this seat's only output. No filed round artifact (rounds 8–23),
source file, gate, baseline, or pin was modified; no git commit/push was run.

## Verdict

**Box 4: verified-with-conditions.**

- **Cross-domain bleed: none found** in the rounds 19–23 LOG entries, the D4
  artifacts, or handoff v3. Every canon mention is a refusal or disclaimer;
  no real-world rights/attribution ruling exists; no game-mechanics content
  exists. Detail in §2.
- **`PROVINCE.md`: accurate** for every surface the newest content exercises
  (§4). Digest unchanged since its round-21 record.
- **The filed D2→D4 fixture bleed tail is accounted for as the box's
  conditions** (§3). Its fix is verified live on the current tree by this
  seat's own census and gate run; the tail's open remainder is named in three
  conditions (3a–3c) so the box is green only with those conditions attached.

## 1. Scope and method (what this seat read and ran)

Read in full:

- `PROVINCE.md` (31 lines; digest below).
- `LOG.md:3258-3338` — the five rounds 19–23 entries plus the round-22
  append-only correction.
- `reports/round-22/bleed/analysis.md` (the filed bleed census and source
  trace; includes the tail's own limits, `analysis.md:173-174`).
- `reports/round-21/adjacency/ledger.json:93-110` — the filing of
  **A21-D4-XF-01** (the D2→D4 fixture bleed, `filed: true`, `bleed: true`).
- `reports/round-20/handoff/v3.md` (handoff-e2e v3 usage/evidence map) and the
  v3 ledger's D4 row basis rows via `reports/round-20/handoff/twin.json:988`.
- `reports/round-23/pins/table.md` (post-fix pin table and open-debt limits).

Run by this seat (lane root, `TMPDIR=$PWD/.scratch` exported):

1. Fresh bleed census over the **current tree**
   `examples/culture-d4/typed-labels.d4.yml` (same leaf-walk method as the
   filed census): `rank-citations 0` (filed baseline: 24),
   `full-D2-path-fields 1` (filed baseline: 28; the survivor is the
   negative-provenance line, §3c), `short-rank-source-fields 0` (baseline 14),
   label owners `{09-costumes: 12, 04-lexicon: 54, 05-naming: 8}` (baseline
   owners were D2's `11-costumes/05-lexicon/13-naming`), label schemes
   `D4-roman-1 …` ×62 / null ×12 (baseline: `d2-roman` ×62), D2L-RANK findings
   `{}` (baseline: 3 holds + 1 note).
2. `python3 tools/gates/d4-typed-labels-check-gate.py` → exit 0,
   "byte-identical deterministic projection".
3. Digest controls: `sha256sum tools/d2-typed-labels.py` =
   `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` —
   matches the "round-22 final combined (live now)" pin
   (`reports/round-23/pins/table.md:18`); `sha256sum PROVINCE.md` =
   `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` and
   `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` =
   `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` — both
   match the values recorded by the round-21 boundary check
   (`reports/round-21/adjacency/ledger.json`, "PROVINCE and filed-round
   preservation" row). `git status --porcelain` is clean for `PROVINCE.md`,
   `SKILL.md`, `tools/d2-typed-labels.py`, and `examples/culture-d4/`.
4. Targeted greps over `examples/culture-d4/` and the `reports/round-19..23`
   trees: canon-assertion patterns (`canonized|now canon|is canon|canon: yes|
   accept…canon`), rights patterns (`copyright|licen[sc]e|fair use|
   attribution|public domain|trademark`), and game-mechanics patterns
   (`game-dev|game mechanic|gameplay|hit point|stat block|damage roll`); all
   hits read in context (§2).
5. Boundary rule spot-checks in the projector: family dispatch present
   (`tools/d2-typed-labels.py:604,614,625,834-842` — `family_label_metadata`,
   the `family == "d4"` metadata/validation branch, `validate_family_labels`;
   `_selftest_family` at `:2980,:3582`), and the family-clean rule landed in
   the skill (`SKILL.md:246,260,293,339`, the last citing the fix commit
   `0e81d9d` and projector `2819f687…`); line numbers as of this seat's read —
   a parallel round-24 seat is editing `SKILL.md` in the working tree (it
   shifted these anchors +2 during this review), so anchor on the quoted
   headings, not raw line numbers.

## 2. Cross-domain boundary re-check — findings by refused domain

Per `PROVINCE.md:16-20`, the lane refuses: canon (lore-shokunin), real-world
rights/attribution rulings, game mechanics (game-dev-2d/3d), general
source-research method (chousa), web publishing (kake), prompt/skill craft
(kotoba).

| Domain | Finding | Evidence (read in context by this seat) |
|---|---|---|
| Canon | **None.** All canon mentions in scope are NON-CANON declarations, handoff boundaries, or refusals. The D4 packet's own key reads `canon: "not canonized (D4 NON-CANON design drill)"` (`examples/culture-d4/packet.d4.yml:2`); every D4 component carries `NON-CANON` + `canon_boundary` routing canon to lore (e.g. `components/12-provenance.yml:46-50,68-69`); the v3 packet's `canon_standing` is `not canonized — lore disposition required` (`reports/round-22/handoff/declared-in-r2/packet.md:9`, same rows in the r20 v3 baseline's twin `reports/round-20/handoff/twin.json:988`); the rounds 19–23 LOG entries and pin tables claim no canon standing (`reports/round-23/pins/table.md:52-54`; `pins/d4profile.md:56`). | Grep pattern set of §1.4; the only "canonized" hits in rounds 19–23 are `"not canonized (D4 NON-CANON design drill)"` or refusal language (e.g. `reports/round-20/handoff/frozen.md:131`, `reports/round-23/pins/v2.md:52`). |
| Real-world rights/attribution | **None.** Lexical hits for license/rights/attribution are (a) explicit disclaimers — "no rights, attribution, or permission ruling is made or implied" (`components/12-provenance.yml:50`; `brief.md:10`; `components/01-brief.yml:266-267`) and the v3 ledger's D4-CL11 rights disclaimer (per the r21 boundary scan I spot-checked, `reports/round-21/adjacency/entries.md:50,56`) — or (b) in-world cultural design content: "furnace right", the maker's stamp, the "license to speak a name" (`components/09-costumes.yml:30,138,96`; `components/05-naming.yml:11,42-139`). These are fictional sumptuary/naming institutions, not rulings on reference works. | Grep set of §1.4. |
| Game mechanics | **None.** Pattern hits were linguistic replay fields (`expected: tumhai`, formation stems) and pipeline hold sets — design-debt bookkeeping, not game rules. The in-world rank/entitlement records (`effect: permit`, RK-01..RK-04, four properties from `components/09-costumes.yml:133-137`) are culture/costume-material content per the lane's domain, matching the filed r21 finding that these are "explicitly fictional culture/institution records" (`reports/round-21/adjacency/entries.md:19`). No game-dev reference, stat block, or gameplay loop appears in the reviewed content. | Grep set of §1.4. |
| Chousa / kake / kotoba | **None.** No general-research-method, web-publishing, or prompt/skill-craft content in the reviewed newest content; the rounds 19–23 entries are lane-local engineering records (source re-checks within the lane's own corpus, tool pins, handoff mechanics). | LOG.md:3258-3338; reports/round-19..23 trees via §1.4 greps. |

Corroborating (cited, spot-checked — not re-derived): the r21 boundary scan of
the round-19 corpus entries and the v2/v3 handoff packets found no
out-of-province content and filed the one fixture-bleed finding it did find
(`reports/round-21/adjacency/entries.md:10-62`); the r19/r20 adjacency
reports state the same for their waves (`reports/round-19/adjacency.md:87,106-120`;
`reports/round-20/adjacency.md:154-191`).

## 3. The filed D2→D4 bleed tail — accounting (the box's conditions)

The tail, in full: the committed D4 typed-label projection reproduced D2's
rank system (24 fully qualified D2 rank-source citations + 3 quarantine + 14
short-component references; 74 labels with D2 owners and the `d2-roman`
scheme; three D2 rank holds + one D2 note). Filed **A21-D4-XF-01**,
`reports/round-21/adjacency/ledger.json:93-110` (`severity: material
fixture-boundary defect`, `filed: true`), prior disclosure at
`reports/round-20/handoff/packet.md` D4-CL09; censused and source-traced at
`reports/round-22/bleed/analysis.md` (baselines at revision `46a0325…`);
designed family-clean (`reports/round-22/bleed/design.md`); implemented in the
round-22 window at commit `0e81d9d` per the append-only correction
(`LOG.md:3312-3324`; the r22 rejection row `LOG.md:3298-3310` stands as
written); the family-clean projection rule landed in the skill in round 23
(`LOG.md:3332`; `SKILL.md:246-293,339` — see the §1.5 line-drift note) with
successor pins (`reports/round-23/pins/table.md`).

This seat's independent current-tree verification (§1.1-§1.2): the bleed is
**gone live** — 0 fully qualified D2 rank citations, 0 short D2 rank-source
fields, D4-local owners and the D4-declared `D4-roman-1` scheme on all 74
labels, zero D2L-RANK findings, and the D4 gate exits 0 over the live bytes,
with the live projector digest matching the pinned `2819f687…`.

Box 4 is therefore **verified-with-conditions**; the conditions are the tail's
open remainder, none silent:

- **3a — open design debt the fix does not touch.** The fix must not be read
  as resolving D2's historical rank debts or filling D4's owed terms — the
  tail's own limit (`reports/round-22/bleed/analysis.md:173-174`). Live state
  agrees: 15 D2 holds + 1 note (D2) and the 12 D4 garment/slot holds remain
  open (`reports/round-23/pins/table.md:52-54`; D4's committed hold set is the
  12 `D2L-FORM-UNRESOLVED` rows in `examples/culture-d4/expected-holds.json`).
- **3b — the ledger row of record.** The r22 ledger row still reads
  "D (failed as declared) … never implemented" (`LOG.md:3298-3310`) as the
  verdict of record; only the append-only correction (`LOG.md:3312-3324`)
  re-describes the tree state, and the row stands by design. Box 4 reads the
  pair together; a reader of the row alone would mis-date the fix.
- **3c — the sanctioned residual.** Exactly one `examples/culture-d2/` string
  remains in the live projection: `$.era_reconciliation.basis[1]`
  (`examples/culture-d4/typed-labels.d4.yml`), which states the D2 costume leg
  is **not** read for family d4. The filed census excludes it as explanatory
  negative provenance, not a source binding
  (`reports/round-22/bleed/analysis.md:60`); this seat concurs with that
  reading and confirms it is the only survivor. Condition: any future digest
  drift, substring ban, or re-census must keep distinguishing it from an
  import rather than silently reclassifying it in either direction.

No other intra-lane or cross-domain bleed was found on the newest content.

## 4. `PROVINCE.md` accuracy

- **Load-bearing contract exists** and is digest-unchanged since its r21
  record: `corpus/knowledge/synthesis/worldbible-integration-contract.md`
  (`PROVINCE.md:22-24`; §1.3 digests).
- **Owned partitions exist**: `corpus/knowledge/{linguistics,myth-symbol,
  culture-material,synthesis,verification,civilizations}` all present
  (`PROVINCE.md:9-11`).
- **Refused siblings exist** at the fleet root: `lore-shokunin`,
  `game-dev-2d-shokunin`, `game-dev-3d-shokunin`, `chousa-shokunin`,
  `kake-shokunin`, `kotoba-shokunin` (`PROVINCE.md:16-20`; matches the r19
  sibling sweep, `reports/round-19/scope.md:119`).
- **`PROVINCE.md` is unmodified**: sha256 `05b34a57…` equals the r21-recorded
  digest and git status is clean (§1.3). The newest content does not expand
  ownership: the verification/civilization partitions remain in support of
  linguistic-cultural coupling, and contested scope was routed (the XF-01
  filing routed to the projector owner; `ledger.json:93-110`), never absorbed.

## 5. Coverage limits (stated, not hidden)

- The five rounds 19–23 LOG entries were read in full; the rounds 19–23
  **report trees** were covered by the targeted greps of §1.4 plus close reads
  of the boundary-bearing files named in §1 — not every byte of every report.
- The v3 packet's 27 claim rows were not re-read row-by-row by this seat; this
  seat read the v3 evidence map (`v3.md`), the D4 row basis in the machine
  twin, and spot-checked the r21 row-level scan that did read them
  (`entries.md:10,50,56`).
- The fix's *history* (r22 window writes, interrupt, sweep-in) is taken from
  the filed record; the decisive check this seat ran is the **live result**
  (census + gate + digest), which does not depend on that history being
  narrated correctly.
- No round validator was run by this seat; validators belong to their writers.
  This report is a boundary verdict, not round acceptance, and claims no canon,
  lore acceptance, real-world clearance, or rights standing.
