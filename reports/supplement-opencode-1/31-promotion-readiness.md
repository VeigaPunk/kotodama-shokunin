# 31 — Promotion-readiness review (author-side)

Role: worker 31 of supplement-opencode-1, REVIEWER scope. Subject: kotodama-shokunin
promotion (shonen → shokunin) gates per fleet `PROTOCOL.md` §Promotion gates and the
`SHONEN.md` checklist. Baseline: `fe34faaafbe0add59ff68827a0df6c5782a72404` (repo HEAD at
review time; working tree hashes checked equal — see below).

**Non-independence disclosure.** This review is produced by a dispatched subagent of the
kotodama-shokunin supplement wave. Per `PROTOCOL.md` §Promotion gates, "a subagent the lane
dispatched is still the lane": nothing here is non-author verification. No `[x]` may be written
from this report, no rank/roster update is made or proposed as landed, and this worker is not
an external independent verifier.

## Baseline identity (commands and observed results)

- `git rev-parse HEAD` → `fe34faa…a72404`; `git status --short` → `?? reports/` only.
- `sha256sum` of `SHONEN.md`, `SKILL.md`, `PROVINCE.md`, `LOG.md`, `SCORECARD.md`, `AGENTS.md`
  compared against `git show fe34faa:<path> | sha256sum` → identical for all six (e.g. SHONEN
  `7999d09b6b8e6f89…`).
- Canonical form: `sed -n '425,435p' PROTOCOL.md | sed 's/^    //' | sed 's/<name>/kotodama-shokunin/'`
  diffed against `SHONEN.md` → empty diff (byte-identical modulo `<name>`). All four boxes are
  unmarked `[ ]`; no `[~]` or `[x]` exists in `SHONEN.md` at baseline.
- Counts at baseline: `git ls-files 'corpus/knowledge/**/*.md' | wc -l` = 179;
  `git ls-files 'corpus/knowledge/civilizations/*.md' | wc -l` = 94 (92 non-`primary-sources`,
  matching SKILL.md's "92 earlier-civilization bases"); `git ls-files 'tools/gates/*.py' | wc -l`
  = 7; tracked `tools/gates/fixtures/` files = 21.
- Ancestry: `git merge-base --is-ancestor <h> HEAD` → yes for `a527120`, `76c105b`, `49ac1a5`,
  `291c714` (round-1 commit), `1688790` (round 2), `c610e0a` (round 3).
- All command execution below ran inside a throwaway export (`tmp=$(mktemp -d); git archive
  fe34faa | tar -x -C "$tmp"`), not in the live worktree, because gate `--selftest` modes rewrite
  their committed fixtures (myth gate selftest prints "fixture and expected rewritten under
  tools/gates/fixtures/"). The live tree stayed byte-clean; the export was removed after use.

## SHONEN — four author-side assertions

Each line is author-side (`[~]`-class): evidence is presented; the gate itself still requires a
non-author `[x] <verifier>` per box. No box is checked here.

- [~] **Box 1** — decision tables, error patterns, checklists, cited sources exist in SKILL.md.
  Evidence: `SKILL.md:20-29` (6-row decision table), `:31-40` (6-row error patterns),
  `:55-65` (4-item executable checklist), `:98-106` (7-row gate registry). Cited surface pointers
  resolve at baseline: `linguistics/conlang-methodology.md`, `naming-systems.md`,
  `historical-linguistics.md`, `phonetics-phonology.md`, `semantics-pragmatics.md`;
  `myth-symbol/comparative-frameworks.md`, `ritual-liminality.md`;
  `culture-material/dress-through-eras.md`, `costume-semiotics.md`,
  `garment-lexicon-crosslinguistic.md`; `synthesis/era-language-staging.md`,
  `source-discipline-calibration.md`, `worldbible-integration-contract.md`,
  `consistency-verification-checklist.md`; all 7 registry pinned-value paths under
  `tools/gates/fixtures/` exist. Executability re-measured 2026-10-17 in the export: all 7 gate
  `--selftest` runs exit 0 (e.g. phonology "15/15 planted finding IDs present; 26 control cases
  passed"), `python3 tools/assemble-d2.py --check` exits 0 ("byte-identical deterministic
  assembly"), `tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md` exits 0
  ("fields=16/16 glossary-entries=20 findings=0"). Negative controls (actual CLI): empty file and
  malformed stdin both exit 2 with `FINDING G-DATA: UNEVALUABLE`. Residual: whether the tables
  are *real* enough to satisfy the gate is a non-author judgment; the registry table states the
  verdict map once in the section preamble (`:87-96`) rather than as a per-row column — a
  presentation observation for the reviewer, not asserted as a defect.
- [~] **Box 2** — at least one end-to-end domain task executed and logged.
  Evidence: `LOG.md:1967-1987` (round-3 entry, claim 1) records trigger → action → outcome →
  pointer for the D2 miniature-culture build and explicitly says "Task executed and logged
  end-to-end (SHONEN box 2 evidence)" (`LOG.md:1976-1978`). Pointers resolve:
  `examples/culture-d2/ASSEMBLY.md`, `tools/gates/frozen/round-3/MANIFEST.tsv` with 7 rows
  (gate/input/output sha256, exits, commands), `frozen/round-3/inputs/…` byte-copies, and
  `SCORECARD.md:32` capability row. Re-measured: committed `examples/culture-d2/packet.d2.yml`
  sha256 = `d5fb4088…bd96`, and `--check` regenerates it byte-identically. Residual (reviewer
  must weigh, not ignore): the frozen round-3 runs are a TSV-manifest pattern, not the per-gate
  digest-pinned `expected.json` "two evidences" form (§Gate standard) — the round-3 entry admits
  this (`LOG.md:1961-1962`); the round-4 frozen outputs (5 `.out` files) carry no manifest; and
  the committed packet (`d5fb4088…`) differs from the round-3 frozen input copy (`54be63…`,
  matching MANIFEST), consistent with a round-4 v1.1 regeneration not re-frozen. The in-flight
  wave claims (assembler `--selftest`, `tools/replay-frozen.py`) are **not landed at baseline**
  and were not counted.
- [~] **Box 3** — instructions executable by an agent without oral context.
  Evidence: SKILL.md decision-table surfaces resolve to the corpus files listed under Box 1;
  corpus map paths `corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,
  verification,civilizations}/` all exist; the packet-schema pointer ("schema in
  `corpus/knowledge/verification/`") resolves to that directory, whose per-gate spec files (8
  mention "packet") document the input shape; the runtime command battery under Box 1 ran from
  the document alone inside the export. Residual: the box asks for execution *without oral
  context*; the only valid test is a non-author agent cold-running SKILL.md — my run cannot
  certify it, and, per protocol, other wave workers are also still the lane.
- [~] **Box 4** — no cross-domain bleed; PROVINCE.md still accurate.
  Evidence: bounded bleed sweep `(?i)gameplay|game mechanic|hit ?points|d20 dice|stats block`
  over `corpus/knowledge/` → 0 matches; sampled entry `conlang-methodology.md` carries
  `sources:`/`couples:` and ends at the handoff ("hands language facts (never canon) to
  lore-shokunin", `:5`); the load-bearing handoff contract path
  `synthesis/worldbible-integration-contract.md` exists. **Observed accuracy gap for the
  reviewer:** `PROVINCE.md:9-11` "Owns" names only 4 knowledge dirs
  (linguistics, myth-symbol, culture-material, synthesis), while the repo and SKILL.md's corpus
  map also carry `verification/` (13 files) and `civilizations/` (94 files) — ~107 of 179
  entries are outside the stated Owns list. Whether that makes PROVINCE.md "still accurate"
  fails box 4 is a non-author ruling.

## Unresolved non-author verification requirements

1. **Named non-author verifier for every box.** Only a fresh lane or the integrator (not this
   worker, not any dispatched subagent of this wave) may write `[x] <verifier>` with one
   indented evidence pointer per box, in canonical form. SHONEN.md currently has no marks.
2. **Box 1 judgment.** A non-author must confirm the decision table / error patterns / checklist
   satisfy "real … cited sources", not merely that the pointers resolve.
3. **Box 2 acceptance.** A non-author must rule on the round-3 TSV-vs-`expected.json` gap, the
   unmanifested round-4 runs, and must re-verify commit `c610e0a` (and any cited hash) ancestry
   at closure; the in-flight wave work must not be read as landed evidence.
4. **Box 3 cold execution.** A non-author agent session must execute SKILL.md end-to-end with no
   oral context and record the transcript pointer.
5. **Box 4 ruling.** A non-author must decide the PROVINCE "Owns" completeness question above
   and, ideally, run a full cross-domain sweep (mine was bounded and pattern-based only).
6. **Promotion mechanics (integrator/operator-side, not performed here).** On promotion:
   SHONEN.md deleted, `MANIFEST.json` rank updated, review recorded in the promoter's lane
   report and repo `LOG.md` (§Promotion gates). No roster row or rank statement is made or
   implied by this report.
7. **Evidence freshness.** This review measured the immutable baseline `fe34faa`; the live
   worktree may contain other workers' in-flight changes, which this report neither assumes nor
   grades. All live-tree commands used were read-only; no commits, pushes, or shared-file writes
   were made outside this assigned path.

## Limits

- Freshness of corpus scholarship (source rechecks, external retrieval) is out of this worker's
  scope and belongs to the wave's source-recheck fragments; nothing here confirms or denies
  citation accuracy of corpus entries.
- SCORECARD axis scores were not re-derived; one note: the operability row's counting command
  (`ls tools/gates/*.py | wc -l`) yields 7 today (handoff gate added round 2) while the row text
  says "6 gates + deterministic merger" as measured against the round-1 commit — a historical
  measurement, flagged for calibration, not counted as a defect here.
- Verified date: 2026-10-17 (final check observed at 15:38Z per `date -u`); evidence is
  commit-addressed, not time-addressed. Final `git status --short` showed other wave workers'
  uncommitted changes (`06-pantheon.yml`, `07-myths-motifs.yml`, `tools/assemble-d2.py`, new
  `tools/*` and `corpus/lessons/supplement-opencode-1/`) — this review grades none of them.
