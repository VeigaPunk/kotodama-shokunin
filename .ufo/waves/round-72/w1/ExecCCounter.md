# ExecCCounter — round-72 wave-1 executor report

Seat: `L1Kotodama72.ExecCCounter` (leaf; no subagent dispatch, no labrat used).
Assignment: draft the coverage counter for frozen claim C at scratch path
`.ufo/waves/round-72/counters/accept-c.py`.

## Files changed (only the two assigned paths)

1. `.ufo/waves/round-72/counters/accept-c.py` — **written** (32.6 KB, executable,
   stdlib-only Python 3). This is the draft; the L1 copies it to
   `reports/round-72/accept-c.py` after review.
2. `.ufo/waves/round-72/w1/ExecCCounter.md` — this report.
No writes into `reports/round-72/`, no writes to the fleet repo, sibling lanes,
shokuknow, scripts, templates, or `.ufo/state`. Land tool installs; pacman untouched.

## Behavior of the counter

`python3 -B reports/round-72/accept-c.py --root . --lands <40hex>` (also accepts
`--base`, `--fleet-root`, `--census-sh` overrides; `--selftest` runs the fixture
matrix). It reads every lane file as committed bytes via `git show <lands>:<path>`
(and `git show <base>:corpus/SOURCES.md` for the frozen base registry), prints one
`LEG PASS|FAIL <NAME>` line per leg in the frozen order, then
`ACCEPT-C-72: PASS legs=10/10` (or `FAIL legs=10/10`). Exit 0 all pass, 1 any
fail, 2 input error. Legs:

| leg | check |
|---|---|
| ENTRIES | both `corpus/knowledge/culture-material/heritage-taxonomy-models.md` and `heritage-taxonomy-models.amend-2026-10-24-r13.md` exist at lands; header block (before first `##`) carries all labels source/verified-at/recheck/ground/topic/gap-filled/sources/couples/scope |
| ROWS | registry id set at lands minus base == exactly `{S874,S875}`, nothing removed; both rows status `mined`; each new row's used-by cell is a non-empty subset of the two entry paths and the union of used-by == both entries |
| REPOINTED | every `source:` bullet in both entries cites exactly one id ≥ S874 whose registry row URL (normalized `netloc+path` keys, query/fragment/trailing-slash tolerant) matches the cited URL — catches arithmetic id-shift and foreign staged ids (S863/S867/S967) |
| GATE | `corpus/lessons/round-72.md` `## Gate` names S874/S875 with their registered URL, access date `2026-10-25`, a quoted locator of ≤25 words on each row; ≥1 `admitted` row and ≥1 `rejected` row; the section carries both `reason` and `flip` |
| REJECTS | lesson names `narrative-structure-frameworks.md` + S870 and `worldbuilding-setting-practice.amend-2026-10-23.md` + S899/S900, plus a refusal/quarantine marker |
| GROUND | receipt shows the gap sweep at the 797-row registry returning 0 for ihchina and bunka; independently re-verified: base registry `ihchina` hits == 0 and `bunka.go.jp` hits == 0 |
| CITEDLINES | materializes the two committed entries and runs `tools/check-cited-lines.py`; exit 0 and `0 finding(s)` |
| CENSUS | `scripts/sources-census.sh validate --root <fleet-root> kotodama` (fleet root = lane parent by default) exits 0 and `HEAD == lands` |
| SCRATCHMIRROR | `…/assimilation/validate-receipt.txt` exists, shows `validate --file`, `exit 0`, and carries S874/S875; the receipt's introducing commit is a strict ancestor of the registry-append commit (the commit where `S874` first appears in `corpus/SOURCES.md`) |
| COLLCHECK | `…/assimilation/reg-ids`, `staged-ids`, `collisions` (or under `validate/`): staged-ids contains S874/S875, reg-ids does not, and the collisions file carries zero id tokens |

CENSUS is the leg the claim itself defines as running the census command against
the worktree; CITEDLINES runs the committed tool on materialized committed bytes.
Everything else is pure `git show`.

## Evidence retained

- Selftest: `SELFTEST: 11/11` — 1 clean fixture (expects `PASS legs=10/10`) +
  10 mutants, each asserting the final run FAILs and that a specific leg is the
  one that fails: drop_entry→ENTRIES, repoint→REPOINTED, rows→ROWS,
  gate_quote/no_rejects→GATE, ground_zeros→GROUND, receipt_no_exit→SCRATCHMIRROR,
  collisions→COLLCHECK, multi_id_line→CITEDLINES, head_ahead→CENSUS. Fixtures are
  real git repos (base→receipt/mirror→lands commits) built in `/tmp`; the real
  `tools/check-cited-lines.py` is copied into the fixture to exercise the real tool.
- `python3 -m py_compile` OK; bad `--lands` exits 2 with an error line.
- Reference grounding: frozen `reports/round-72/claims.json` (base `b60c7b1`, 10
  legs, kill rule), wave spec `dispatch.json` (ExecScratchMirror ROW1/ROW2
  normalized rows, ScribeEntries header fields, ScribeLesson Gate/reject shapes),
  `corpus/SOURCES.md` registry schema (11 columns, `mined`, used-by convention),
  round-71 lesson Gate table shape, `tools/check-cited-lines.py` CLI, round-71
  receipt header conventions.

## Risks / notes for the L1

- **8 vs 9 header fields**: the operator brief said “all 8 header fields”, but
  frozen claims.json leg ENTRIES and the ScribeEntries wave task both enumerate
  nine labels (source, verified-at, recheck, ground, topic, gap-filled, sources,
  couples, scope). The counter implements the frozen nine; a header missing any
  one of them fails ENTRIES.
- The counter encodes a **receipt content contract** the L1 must produce at
  `.ufo/waves/round-72/assimilation/validate-receipt.txt` (committed before the
  registry append): it must contain `797`, a line showing ihchina sweep 0, a line
  showing bunka sweep 0, the literal `--file`, an `exit 0` (or `rc=0`) marker,
  and the tokens S874/S875. The fixture receipt is the template.
- SCRATCHMIRROR is enforced as commit ancestry (receipt commit strictly before the
  append commit), not by parsing an embedded timestamp, so it holds even if the
  receipt's internal stamp format differs; an embedded ISO timestamp is not
  required by the counter.
- CENSUS requires `HEAD == lands`, so run the counter with the lane checked out
  at lands; also expect the census script at `<fleet-root>/scripts/sources-census.sh`
  (override with `--fleet-root` / `--census-sh` if the fleet layout differs).
- The counter never passes on a stub/empty state: every leg reads real committed
  bytes, and the fixtures prove each leg is non-vacuous (one mutant per leg).
- No blockers. The lane's git state was never mutated; only `/tmp` fixtures were
  created by the selftest (auto-cleaned).
