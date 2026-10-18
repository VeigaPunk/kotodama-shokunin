# Round-24 skill-audit fixes — audit-3 fixer seat

- Date: 2026-10-18. Baseline audited: `8fbcee9` (round-24 declare commit); claim
  baseline `b5d9844`. Non-author verifier: this seat authored none of the lane's
  artifacts in rounds 8–23.
- Scope: SKILL.md table rows — every executable claim re-run against current
  tools, every in-repo line-number citation re-resolved against current bytes.
- Method: no silent rewrites. Each stale row below is either fixed with a
  before/after control recorded here, or carries a dated erratum pointer in the
  row itself. Nothing was committed; the working tree holds the fixes, git
  history is untouched.

## Verification summary (rows checked, not stale)

All commands run at `8fbcee9` from the lane root; scratch under
`.scratch/audit3` (`TMPDIR=$PWD/.scratch/audit3`), except the frozen replay,
whose tool refuses an in-repo scratch root (`mirror_unsafe`) and was run with
`TMPDIR=/tmp/audit3-tmp` — its own designed boundary.

| Claim (SKILL.md row) | Command | Result |
|---|---|---|
| d2 typed-labels selftest, 163/163 (family-clean §, `:261-262`) | `python3 tools/d2-typed-labels.py --selftest` | exit 0, `163/163 checks passed`, "no file outside the temporary directory touched" |
| packet_uncertainty selftest (`:89`) | `python3 tools/harness/packet_uncertainty.py --selftest` | exit 0 |
| uncertainty grep = 0 (`:386`) | `grep -ci uncertainty tools/gates/handoff-packet-check.py` | `0` |
| fixture ledger five columns, none uncertainty (`:386`, `:651`) | `sed -n '651p' tools/gates/handoff-packet-check.py` | `\| record_id \| kind \| statement \| provenance \| evidence_status \|` |
| handoff-packet-check selftest + fixture run (gates table `:496`) | `--selftest`; run on `tools/gates/fixtures/handoff-packet-check.md` | selftest exit 0; fixture exit 1 — correct: `.expected` lists HO-* finding ids (expected-findings fixture, verdict map "1 findings") |
| round-22 d4-repin frozen generation 3 rows, exit 0 (`:295`) | `python3 tools/replay-frozen.py tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` | exit 0, `3/3 rows reproduced the recorded verdicts` (typed-labels-check 0/0, d4-assembly 0/0, typed-pipeline-gate count 12/12) |
| D2/D3 assemblers + coupling + craft exercise + inventory (gates table) | `assemble-d2.py --check`, `assemble-culture-d3.py --check`, `check-evidence-coupling.py examples/culture-d3/packet.json`, `check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json`, `source-audit-inventory.py --json`, `naming-collision-gate.py --selftest` | all exit 0 |
| expected-holds keys `counts, holds, notes, packet_sha256, projection_sha256, projector_sha256, schema` (`:209`) | python json load | all present (plus `revision_note`); counts `hold:12, note:0, fail:0` matches `:267-268`  (evidence: re-measured live 2026-10-18; commands in audit-fixes.md §3) |
| profile `d4`, `repin_history[2]`, schema `kotodama-typed-pipelines-v1` (`:212`, `:295`) | python json load `tools/gates/typed-pipelines.json` | `profiles[0].id == "d4"`, `len(repin_history) == 3`, schema matches |
| passenger tokens 0 hits in packet (`:215`) | `grep -c` for `TR-04#a`,`TR-06#a`,`WR-02#g`,`WR-09#g`,`WR-08#g`,`SR-01#a` in `examples/culture-d4/packet.d4.yml` | all `0` (still true today) |
| named-inputs false-difference control (`:208`) | `d2-typed-labels.py --check examples/culture-d4/typed-labels.d4.yml` alone vs `--check <artifact> --packet examples/culture-d4/packet.d4.yml` | artifact-alone exit 1; named pair exit 0 "byte-identical deterministic projection" — the row's behavior reproduces (first attempt used a wrong packet path and got exit 2; not a row defect) |
| line-number citations, 25 of 27 | scripted token-in-range check (`.scratch/audit3/check_linerefs.py`) over `d2-typed-labels.py`, `assemble-d4-typed.py`, `typed-pipeline-gate.py` refs incl. `:2471`, `:2636-2732`, `:2837-2838`, `:2980`, `:3011/:3024/:3032`, `:3045/:3053-3054`, `:3063/:3073/:3099`, `:3109`, `:3114/:3119`, `:3343`, `SERIALIZER:62`, `ROUTED_KINDS:65`, `carry_findings:276-288`, `garment rename:296-310`, gate `:481-485`, `:696-734`, `:736-753` | PASS (the two fails are F1/F2 below) |
| round-18/22 report citations resolve (`holds.md`, `review-1/2/4.md`, `neg-1/2.md`, `manifest.md`, `determinism.md`, `interop-1.md`, round-18 `gate/design.md`, `repin.md:15,18`, `analysis.md:18,101`, `round-22.md:63`, `deployed-replay.json`, `impl.md`) | file existence + line spot-checks | all resolve; `review-4.md:56` and `holds.md:94-97,170-171` carry the 3-holds+1-note measurement; `review-1.md:22-35` carries the six-obligation derivation |
| self-citation `SKILL.md:47` (`:150`, `:183`) | read line 47 | "adding typing fields cannot exempt a string from checking" — correct target |

## Fixes

### F1 — slot-label routing T3 line refs drifted (`SKILL.md`, T3 bullet)

- Before: "`tools/d2-typed-labels.py:622`, `:793`" cited for "the projector
  projects every `form_slots` entry as a label and each owed slot then emits its
  own hold".
- Control (before): at HEAD `8fbcee9`, `:622` is the owner-metadata tuple
  `("costumes", "form_slots", "lexicon", "names")} | {"scheme": scheme}` and
  `:793` is `if label.get("kind") in SOUND_KINDS and status == "supplied":` —
  neither is the claimed statement. At the round-18 bytes `e571894` (when the
  row was written), `git show e571894:tools/d2-typed-labels.py` lines 621-623
  are the `form_slots` projection loop and lines 790-796 the `D2L_FORM …
  hold=True` emission — the citations were true then.
- Control (after): current bytes have the projection loop at `:639-643`
  (`for slot in packet.get("form_slots") or []:` → `labels.append(_form_slot_label(...))`)
  and the hold emission at `:808-814` (both `_fail(findings, D2L_FORM, …, hold=True)`).
- Cause: the round-22 family-dispatch/boundary edits inserted ~17-20 lines above
  both blocks (drift, not behavior change — both statements still exist and hold).
- Fix applied: refs updated to `:639` / `:808-814` at the round-24 baseline
  `8fbcee9`, with the round-18 provenance (`e571894`, `:622`/`:793`) kept in the
  row so the history is not rewritten.

### F2 — determinism message line ref drifted (`SKILL.md`, Derivation-replay "Determinism" row)

- Before: "`tools/assemble-d4-typed.py:369` (`two consecutive builds are not
  byte-identical`)".
- Control: `grep -n "byte-identical" tools/assemble-d4-typed.py` → the message
  is at `:387`; current `:369` is `result["problems"].append(detail)` (the
  assembler-identity early-return). The round-22 `carry_findings` block
  (`:276-288`) landed above it and shifted the line.
- Fix applied: `:369` → `:387`, shift cause named in the row.

### F3 — battery default-exit claim stale (`SKILL.md`, battery row)

- Before: "the committed default currently exits 2 with `BASELINE-GATE-UNCOVERED`
  for myth and naming, whose pins live under `reports/round-9/baselines/`; add
  that root via `--baselines-root` to reach 0".
- Control (default): `python3 tools/check-gate-battery.py` → exit 0,
  summary `battery_exit: 0, pass: 7, fail: 0, unevaluable: 0`. Default roots now
  include `reports/round-9/baselines` (`tools/check-gate-battery.py:151`; the
  round-19 commit `caf1bea` integrated D4/battery roots).
- Control (flag): `python3 tools/check-gate-battery.py --baselines-root
  reports/round-9/baselines` → exit 2 with `BASELINE-GATE-UNCOVERED` findings,
  because `--baselines-root` replaces the roots for one run
  (`tools/check-gate-battery.py:100`, `:1332`) and the frozen-root gates lose
  coverage. The row's old advice, followed verbatim today, produces the exit-2
  it claims to cure.
- Fix applied: row rewritten to the current semantics (default 0 measured
  2026-10-18; flag replaces roots and a round-9-only root exits 2), with the
  superseded wording named and the historical citations kept, plus a controls
  pointer to this file.

### F4 — passenger-rows measured instance superseded (dated erratum, no rewrite)

- Before: "measured: the D4 expected file carries 3 `D2L-RANK` holds + 1 note
  naming …, each **0** hits in `examples/culture-d4/packet.d4.yml`
  (2026-10-18T11:32Z)" — present tense about a file that has since been
  repinned.
- Control: `python3` json load of `examples/culture-d4/expected-holds.json` →
  counts `{hold: 12, note: 0, fail: 0}`, zero `D2L-RANK` rows in `holds`, zero
  notes; the file carries `revision_note` + `supersedes_pins` naming the pre-fix
  projection/projector digests. The 3+1 passenger measurement itself is intact
  in the historical evidence (`reports/round-18/d4/review-4.md:56`;
  `reports/round-18/d4/holds.md:94-97,170-171`;
  `reports/round-22/bleed/analysis.md:101`) and the 0-hits property still
  reproduces (all six tokens `grep -c` → 0 in `packet.d4.yml`).
- Fix applied: a dated erratum appended **inside** the row
  ("erratum 2026-10-18, round-24 audit: … superseded pre-fix expectation …
  preserved at `reports/round-22/bleed/analysis.md:101` and in the file's
  `revision_note`/`supersedes_pins`, see T4 below"). The original measurement
  sentence was not deleted or altered — the row keeps its history and points at
  the supersession, matching the append-only discipline the same section
  requires (T4, `corpus/lessons/round-22.md:19`).

### F5 — unresolvable §4.2 anchor in the T3 bullet (handed over: box1-tables finding F3)

- Before: the T3 bullet ended "`reports/round-18/d4/holds.md` §4.2".
- Control: `grep -n "4\.2" reports/round-18/d4/holds.md` → 0 hits; the file's
  headers are §0-§7 only. §4 at `holds.md:131` is "Reconciliation B — the
  delivered tree's own declaration (6 holds / 0 notes / 0 fails)" and carries
  the six-`GAR-0n` substance the citation points at.
- Fix applied: `§4.2` → `§4`.

### F6 — unresolvable §3 anchor on a file with no numbered sections (handed over: box1-tables finding F4)

- Before: the family-clean cautions cited "`reports/round-22/bleed/design.md` §3"
  for "reported as an explicit skip, never counted as evaluated".
- Control: the file's headers are Decision / Source-level change contract /
  Expected D4 delta, not yet a measured post-fix result / Required paired
  controls / Integration obligations / Draft rule — no numbered sections. The
  explicit-skip rule is contract item 3 at `design.md:17` ("Do not call an
  absent/unsupported leg evaluated: report an explicit family-local skip or
  limitation"), with the companion wording at `:28`.
- Fix applied: `§3` → `"Source-level change contract" item 3, :17`, with the
  former wrong pointer named in the row.

### F7 — five stale corpus line pointers, consistent +2/+3 drift (handed over: box1-tables finding F5)

Each quote re-verified verbatim by this seat at the corrected line before editing:

| SKILL.md row | Before | After | Verified quote at the new anchor |
|---|---|---|---|
| slot-routing T4 caution ("a register label is not a channel") | `era-language-staging.md:114` | `:111` | `## 7. Regnal names and period vocabulary: type every label` |
| error-pattern row (sound laws vs translation/exonym) | `era-language-staging.md:124` | `:127` | "Apply sound laws to an **inherited spoken label**; separately track an unchanged written form, … translation, exonym, or official replacement" |
| error-pattern row (transliteration collision) | `naming-collision-gate.md:69-70` | `:72` | "A collision in that output channel, not native-script identity" |
| error-pattern row (shared garment label) | `naming-collision-gate.md:52` | `:54` | "A shared garment label need not mean identical cut or status" |
| error-pattern row (loanword switched referent) | `garment-lexicon-crosslinguistic.md:26` | `corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md:28,30` | "the loanword switched referent in transit" (:28) + "two coexisting names" (:30); directory corrected — the file lives under `culture-material/`, not `synthesis/` |

### F8 — three stray code fences swallowed the document's rendering (handed over: box1-tables finding F6)

- Before: a 4-backtick opener after the uncertainty section (old :129) and two
  3-backtick lines that could not close it (old :154, :217). In strict
  CommonMark the unclosed fence rendered the remainder of the file as one code
  block.
- Control (before): fence-scan found exactly `` ```` `` (:129), `` ``` `` (:154),
  `` ``` `` (:217); control (after): the same scan finds **zero** fence lines,
  and the table-shape scan (every `|` row followed by a `|` row or blank line)
  finds no broken rows. Bytes/truth of all citations unchanged — three debris
  lines deleted.
- Fix applied: the three lines deleted; no prose touched.

## Reconciliation with the other round-24 seats

- `reports/round-24/audit-gates.md` (audit seat 1, gates registry): its single
  stale finding F-1 is this seat's F3 (battery row inverted) — its independent
  measurements (default exit 0, 19/19 baseline rows pinned across the three
  committed roots; round-9-only root exit 2 via root replacement at
  `check-gate-battery.py:100`, roots at `:148-152`) corroborate the fix this
  seat landed; the two control sets agree.
- `reports/round-24/box1-tables.md` (box-1 table auditor): handed over findings
  F1-F6 with verified anchors. Its F1/F2 are this seat's F2/F1 (same anchors,
  independently derived); its F3/F4/F5/F6 are this seat's F5/F6/F7/F8 above,
  each re-verified here before fixing.
- `reports/round-24/skill-audit.md` (the declared audit-table artifact) never
  landed during this seat's polling window (~15 min, 60 s cadence). The
  fix evidence above is an independent re-derivation, not a transcription of
  that file; if it lands later with further stale rows, they route to a
  follow-up fix pass.

## Not done here / dispositions

- `reports/round-10/drift/fix-18.md` round-3-manifest replay ("live tree reads
  exit 2, 7/7 `gate_digest_mismatch`") was not re-run: reproducing it requires
  rebuilding an isolated tree at pin `291c714` (a git-worktree mutation of the
  lane's `.git`, out of this seat's write scope). The row is already dated and
  framed as a measured control, not a live-state claim — no staleness introduced.
- Historical refs pinned to named revisions (round-21 baseline `46a03257…`
  `:2613`, `:925-1197`, `:1235-1258`) were not re-resolved against HEAD by
  design — the row states the revision it cites.
- Corpus (`corpus/knowledge/...`) line citations in audited rows spot-checked
  where they anchor a fixed row (F7 verified all five verbatim); the full
  corpus sweep is box1-tables.md §"Verified support inventory", which this
  seat's spot-checks corroborated.

- Concurrent working-tree note: during this seat's edit window, three
  checklist-section hunks appeared in SKILL.md from another round-24 seat
  (checklist items 2-4: a `provenance-audit corpus/knowledge` rewording, a
  costume-item "prose gap (machinery: `costume-era-consistency-gate`)"
  addition, and a handoff-item "`handoff-packet-check` enforces per packet"
  addition) — consistent with `audit-gates.md` O-3. They are not this seat's
  writes and were left untouched; the post-fix integrity checks (fence scan,
  table-shape scan) were re-run on the combined file and pass.

FILES: reports/round-24/audit-fixes.md (this file); SKILL.md (fixes F1-F8 above).
No other files written. No commits made.
