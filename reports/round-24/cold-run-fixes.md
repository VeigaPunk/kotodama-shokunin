# Round 24 — cold-run fixes (COLD-RUN 3, fixer seat)

- **Seat:** COLD-RUN 3 (fixer), O-cold-run lane, round 24. Non-author
  verifier: this seat authored none of the lane's artifacts in rounds 8–23.
- **Date:** 2026-10-18. Union intake: `cold-run-a.md` (F1–F5),
  `cold-run-b.md` (F1–F6), `cold-run-conditions.md` (C1–C8), plus this seat's
  own independent execution of the same executable surface.
- **Method:** every fix below is wording/pointer-level in `SKILL.md`, applied
  with a **measured control**; every break too large for that class is named
  as a box-3 condition (§3). No git commits; no rounds-8–23 artifacts
  touched; scratch under `.scratch/r24-o3/` (`TMPDIR=$PWD/.scratch`).
- **Concurrency note:** `SKILL.md` is being edited by sibling round-24 seats
  while this seat worked (diff hunks at old lines ~126/151/210/328/370 are not
  this seat's). The six hunks of this seat are listed in §2; each is
  **line-count-neutral**, so this seat introduced zero line drift. Line
  numbers below were read at 13:35 and may shift under sibling edits.

## 1. Union intake → disposition map

| Finding (source) | One-line statement | Disposition |
|---|---|---|
| A-F1 / scribe item-1 reading / B-F5 | prose checklist is 1-of-4 executable by design | FX1–FX3 resolve the undeclared siblings; reading itself = §3 N7 (process, parent) |
| A-F2 | item 2 names no invocation scope | **fixed** (FX1) |
| A-F3 | item 3 has no operand and no declared status | **fixed** (FX2) |
| A-F4 | item 4 names no real packet to check | **fixed** (FX3); real-artifact operand stays §3 N4 |
| A-F5 = B-F1 = scribe-C1 | battery row (`SKILL.md:501`) inverted vs measured behavior | already fixed by D-audit seats; deduped, controls re-verified (FX4) |
| B-F2 | d4-repin replay exit 0 pin hides an in-repo-TMPDIR fail-closed precondition | **fixed** (FX5); cross-seat contradiction adjudicated |
| B-F3 = scribe-C3 | round-5/6/7 `run-validation.py` exit 1 at clean HEAD; imperative wording implies pass | condition §3 N1 |
| B-F4 = scribe-C4 | the three scripts overwrite filed tracked receipts in place | condition §3 N2 |
| B-F5 | "executable checklist" has two readings; four-file set not per-seat enumerated | condition §3 N7 (process) |
| B-F6 | "executable where a tool exists" caveat missing on D3 replay checklist | **fixed** (FX6) |
| scribe-C2 = this seat's independent find | typed-pipeline-gate fed the derived typed packet reads a plausible false red | **convention named in SKILL.md** (FX7); code repair stays §3 N3 |
| scribe-C5 | "isolated repo export" undefined; needs `.git` history | condition §3 N5 |
| scribe-C6 | per-gate input paths need `ls` discovery | no fix (friction only, per scribe) |
| scribe-C7 | D3 "snapshot mode" clause has no executable referent (no round-7 frozen manifest) | condition §3 N6 |
| scribe-C8 | stray fences `:129`/`:154`/`:217`/`:352` | not this seat's lane (D-seat content audit; scribe concurs) |

## 2. Fixes applied (each with control)

### FX1 — checklist item 2 gains its executable scope (A-F2)

- Before: "`provenance-audit`'s `missing-calibration` family checks the
  declared shape only." — no scope named; two executors can pick different
  paths and both read exit 0 (A's ambiguity).
- After (SKILL.md, checklist item 2): "`provenance-audit
  corpus/knowledge`: `missing-calibration` checks declared shape only)."
- Control (this seat, 13:2x): `python3 tools/gates/provenance-audit.py
  corpus/knowledge` → **exit 0**, `files=199` (corpus count reproduced);
  `--selftest` → exit 0 (A-E1 independently reproduced by B-E16 on the
  synthesis partition: exit 0, files=29).

### FX2 — checklist item 3 declares its prose status + machinery (A-F3)

- Before: bare prose, undeclared — a fresh seat cannot tell executability was
  considered (A: "unlike item 1 it does not even declare its own prose
  status").
- After: "…who may wear it — prose gap (machinery:
  `costume-era-consistency-gate`)."
- Control: `costume-era-consistency-gate.py --selftest` → **exit 0**;
  committed defect fixture → **exit 1** (planted findings) — machinery real,
  item honestly declared prose.

### FX3 — checklist item 4 names its enforcement surface (A-F4)

- Before: bare prose; the enforcing gate existed but no line connected them.
- After: "…open questions — `handoff-packet-check` enforces per packet; no
  canon here."
- Control: `handoff-packet-check.py --selftest` → **exit 0**; fixture run →
  **exit 1**, 11 `HO-*` findings (recipient/open-questions/canon legs among
  the ids, matching A-E5/E6). Note: a *real* handoff packet operand still
  does not exist in the four files → §3 N4.

### FX4 — battery row break: NOT re-fixed (dedupe), controls re-verified (A-F5 = B-F1 = scribe-C1)

- The D-audit fixer already corrected the `SKILL.md:501` battery cell in the
  working tree with before/after controls (`reports/round-24/audit-fixes.md`
  F3; independently found as F-1 in `audit-gates.md`); the corrected cell is
  present at `SKILL.md:501` at fix time. Re-fixing would double-edit a
  sibling's live hunk.
- This seat's independent controls **agree with the fix**: default
  `check-gate-battery.py` → **exit 0** (7/7 selftests); with
  `--baselines-root reports/round-9/baselines` → **exit 2** (flag *replaces*
  the roots). One measurement correction for the record: the flag run
  uncovers **6** distinct gates (`phonology-sanity`, `lexicon-coverage`,
  `costume-era`, `provenance-audit`, `d4-typed-labels-check-gate`,
  `d4-assembly-check-gate` — parsed from the run's JSON), not the 4 quoted in
  `cold-run-a.md` E8 / scribe-C1; the corrected SKILL.md cell's generic
  "frozen-root gates" wording is accurate either way.

### FX5 — d4-repin exit-0 pin gains its TMPDIR precondition (B-F2), contradiction adjudicated

- Before: "`tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` (3 rows, exit
  0; …)" — B measured exit 2 `mirror_unsafe` under the round-mandated
  `TMPDIR=$PWD/.scratch` (B-E20), while scribe-§A claimed 3/3 pass with an
  in-repo TMPDIR. Contradiction inside the union.
- Adjudication (this seat, both arms): `TMPDIR=$PWD/.scratch` → **exit 2**,
  3× `mirror_unsafe` ("temporary root is inside the repo");
  `TMPDIR=/tmp/cr3-tmp` → **exit 0**, 3/3 reproduced. Verdict: B-E20 and the
  audit-3 seat are right; the scribe's §A replay row misrecords its TMPDIR.
- After (SKILL.md, family-clean Propagation/tamper row): "(3 rows, exit 0 —
  requires TMPDIR outside the repo, `mirror_unsafe` exit 2 otherwise,
  measured 2026-10-18 round-24 cold run; …)".

### FX6 — D3 replay checklist gains the executability caveat (B-F6)

- Heading now reads `### D3 replay checklist (executable where a tool
  exists)` — matching the main checklist's caveat, so step 4's manual first
  half is covered by the same declaration. Heading-line-only edit.

### FX7 — gate-input convention named (scribe-C2 = this seat's independent find)

- This seat independently hit the same false red the scribe recorded:
  `typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` →
  **exit 1, 14/16 legs** (`L2-channel` with 8 `DERIV-REPLAY` FAILs NM-01…08;
  `L3-routing-consistency` with 6 `'null'` routing rows), while
  `… packet.d4.yml` → **exit 0, 19/19** and flagless no-arg → **exit 0,
  16/16** (B-E24 reproduced). Gate bytes are unchanged since the round-22
  freeze (`sha256 tools/gates/typed-pipeline-gate.py` =
  `04ad4bb4…` = the MANIFEST pin).
- Root causes (both verified, both code-level, NOT wording-fixable):
  1. `L3-routing-consistency`: `routed_slots` (`typed-pipeline-gate.py:749`)
     lacks the null-ish filter `moved_field()` applies to `off_channel_field`
     (`:186-194`); the committed packet's 6 per-record rows carry YAML
     `owed_slot: null`, which the lane's reader keeps as the string `'null'`.
  2. `L2-channel`: in the typed-input direction the gate rebuilds legacy
     bytes via the D2 `yaml_lines` round-trip; this seat diffed the rebuild
     against committed bytes: 5730 differing lines, `rules:` blocks re-nested
     (e.g. `rule: "CX-01"` 6-space vs 8-space indent at packet line ~1950) —
     the rebuilt variant is what manufactures the 8 `DERIV-REPLAY` findings;
     neither committed packet produces them directly (`naming-collision-gate`
     on each: exit 1 but 0 `DERIV-REPLAY` lines). Rebuild bytes preserved at
     `.scratch/r24-o3/rebuilt-legacy.yml`.
- After (SKILL.md, slot-label routing intro, last line): "Gate input is the
  source packet (`packet.d4.yml`), never the typed packet — feeding it back
  reads a false red (exit 1, 14/16 legs, measured 2026-10-18 round-24 cold
  run)." The code repair itself is §3 N3 (pin cascade).

## 3. Named box-3 conditions (larger than pointer-level; not fixed this round)

- **N1 (major, B-F3 = scribe-C3):** `reports/round-5/6/7/run-validation.py`
  all exit 1 at clean HEAD with distinct causes (round-5 O-leg expects live
  replay exit 0 that SKILL.md itself documents as exit 2; round-6 pins
  byte prefixes structurally unre-publishable under append-only errata;
  round-7 totals/collision control). Needs dated expected-verdict errata —
  wording fix would have to invent verdict policy.
- **N2 (major, B-F4 = scribe-C4):** the three scripts rewrite filed tracked
  `reports/round-N/validation.json` in place; the isolation caveat covers
  only battery/replay. Needs a documented run-in-disposable-copy instruction
  (or a script change). Hygiene: the pre-existing
  ` M reports/round-7/validation.json` present at seat start was restored by
  another seat during this round (gone from `git status` at 13:35).
- **N3 (major, scribe-C2 mechanism):** repairing the typed-input direction
  itself — `routed_slots` nullish guard and a faithful legacy rebuild —
  changes pinned gate/serializer bytes (`d4-repin` gate sha pin, battery
  baselines), i.e. a repin cascade routed like the round-22→25 recipe.
- **N4 (major, A-F4 remainder):** no real costume/era artifact set and no
  real handoff packet path is named in the four files; items 3/4 gain
  declarations, not operands.
- **N5 (minor, scribe-C5):** "isolated repo export" must be defined as
  history-retaining (clone/worktree) for the round-3 restore-and-replay leg.
- **N6 (minor, scribe-C7):** D3 step 2 "snapshot mode" names no manifest;
  none exists for round-7 — needs an erratum naming the `--frozen` option or
  dropping the clause.
- **N7 (process, B-F5 + A-F1):** the parent should pin (a) which reading of
  "the SKILL.md executable checklist" future cold runs execute (A and B
  diverged productively), and (b) the exact four-file set per seat.

## 4. Verification summary

- This seat's six edits are line-count-neutral (verified per-edit: 2→2,
  1→1, 1→1, 4→4, 2→2, 1→1); they were applied at a 600-line state
  (`wc -l` at 13:29). Sibling seats' concurrent edits (net −2) moved the
  file to **598** before close (`wc -l` at 13:35) — not this seat's delta.
- `git status --short` at close: ` M SKILL.md` (combined seat edits) + the
  round-24 untracked reports; **no tools/, corpus/, examples/, or rounds-8–23
  paths modified by this seat**; no git mutations.
- Controls re-runnable: `python3 tools/gates/provenance-audit.py
  corpus/knowledge` (0); `…/costume-era-consistency-gate.py --selftest` (0) +
  fixture (1); `…/handoff-packet-check.py --selftest` (0) + fixture (1, 11
  HO-*); `python3 tools/check-gate-battery.py` (0) vs
  `--baselines-root reports/round-9/baselines` (2);
  `TMPDIR=<outside> python3 tools/replay-frozen.py
  tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` (0) vs in-repo TMPDIR
  (2); `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`
  (0, 19/19) vs `…packet.d4.typed.yml` (1, 14/16) vs flagless (0, 16/16).

## 5. Seat hygiene

Writes: this file and `.scratch/r24-o3/` (gitignored scratch) only. No
commits, no pushes, no edits to filed artifacts of rounds 8–23. Read scope:
the four cold-run files, the three sibling round-24 reports named in §1
(read for the union after this seat's independent execution was complete),
and tool/corpus files strictly as needed to verify fixes and controls.
