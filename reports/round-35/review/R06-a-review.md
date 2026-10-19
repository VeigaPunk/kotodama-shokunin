- Seat: R06 | reviewer | claim A (adjacency) | date 2026-10-19 | baseline 4a7aede

# R06 — adversarial review: independent diff-based touched-surface census (rounds 33–34)

Mission: "any touched surface missed by K04's census? (run your own diff-based
census)." K04's fragment (`reports/round-35/scout/K04-touched-census.md`) does
not exist at review time — the owed path is recorded under `## Owed`. This
fragment therefore files my own census as the independent baseline, compares it
against the round-35 A-claim's declared surface list, and reports the surfaces
that list does not name.

## 1. Method (exact window and commands)

Window = the last two rounds' full byte footprint, from the round-32 admission
tree to the round-35 baseline:

- `git diff --name-status cdd66d7 4a7aede` → 172 changed paths: **160 A + 11 M + 1 D**
  (`git diff --name-status cdd66d7 4a7aede | awk '{print $1}' | sort | uniq -c`).
- `git diff --numstat cdd66d7 4a7aede | awk ...` → files 172, +58808 / −187.
- Per-round split: `git diff --name-status 139e3b6 da68a6d` (round 33, baseline
  = `reports/round-33/claims.json:11` `139e3b6`) and `git diff --name-status
  da68a6d 4a7aede` (round 34, baseline = `reports/round-34/claims.json:9`
  `da68a6d`).
- File-count reconciliation: `git ls-files | wc -l` = **2815** at HEAD;
  `git ls-tree -r --name-only 139e3b6 | wc -l` = **2655**;
  `git ls-tree -r --name-only cdd66d7 | wc -l` = **2656**. 160 A − 1 D = +159
  = 2656 → 2815, fully explained.

## 2. Census result — 158 report files + 14 out-of-report surfaces

Of the 172 changed paths, **158 are new files under `reports/round-33/` and
`reports/round-34/`** (`git diff --name-status cdd66d7 4a7aede -- reports/round-33
reports/round-34 | awk '{print $1}' | sort | uniq -c` → 158 A, zero M/D). The
remaining **14** are the surfaces an adjacency pass must own:

| # | path | round | status | risk class |
|---|---|---|---|---|
| 1 | `AGENTS.md` | 33 | M (−2) | rule text excision (r31 drafting residue, `LOG.md:3581-3582`) |
| 2 | `LOG.md` | 33+34 | M (+93, +54) | append-only bookkeeping |
| 3 | `REGIMEN.md` | 33 | **A** (new) | the round contract itself — names paths |
| 4 | `SCORECARD.md` | 33+34 | M (+29, +31/−3) | append-only verdict record |
| 5 | `SKILL.md` | 33 | M (+35/−18) | lane rule text; digest moved `79fe91d3…`→`f9bd07c2…` (`LOG.md:3577`) |
| 6 | `corpus/knowledge/linguistics/register-lexicon-ceilings.md` | 33 | M (+28/−0) | corpus bytes, append-only §12 errata |
| 7 | `corpus/lessons/README.md` | 33 | M (+130/−28) | index with 33 pinned rows |
| 8 | `examples/culture-d3/README.md` | 33 | M (+1/−1) | digest repoint |
| 9 | `examples/culture-d3/handoff.md` | 33 | M (+2/−2) | digest repoint |
| 10 | `examples/handoff-packet.sample.md` | 33 | M (+1/−1) | digest repoint |
| 11 | `examples/handoff-packet.sample.yml` | 33 | M (+2/−2) | digest repoint |
| 12 | `tools/exercise-handoff-e2e.py` | 34 | M (+11/−10) | live renderer: CLAIMS_MAP + v3 default move |
| 13 | `tools/harness/receipt_guard_adoption.py` | 34 | **A** (+1309) | new lane instrument |
| 14 | `.ufo/reports/round-32/kotodama.md` | pre-33 | **D** | fleet-root boundary (see F-R06-3) |

Preservation leg, independently confirmed: **zero modifications to filed rounds
1–32 bytes in the window** — `git diff --name-status cdd66d7 4a7aede -- reports/`
filtered to non-`A` statuses returns nothing but the round-33/34 additions
(`git diff --name-status cdd66d7 4a7aede -- reports/ | grep -vE '^A[[:space:]]'`
→ exit 1, no output); the same filter restricted to `round-([1-9]|[12][0-9]|3[0-2])/`
returns nothing.

## 3. Findings

### F-R06-1 (missed surface, green-but-unfiled) — `corpus/lessons/README.md`

Round 33's **largest live non-report edit** (+130/−28; 43 454 bytes / 448 lines
at HEAD) is not named in the round-35 A-claim's surface list
(`reports/round-35/claims.json:56` names "the round-33/34 SKILL.md and AGENTS.md
and ceilings edits" but not the lessons index) and no A01–A10 mission
(`reports/round-35/targets.json` seats A01–A10) assigns it. It is the only
r33-touched surface carrying 33 byte/line/sha8 pins that a later edit could
silently invalidate, so it is exactly the surface an adjacency pass exists for.

Independent re-measure at HEAD (script: parse `^\|\s*`(corpus/lessons/[^`]+\.md)`\s*\|`
rows, recompute sha256[:8], bytes, `splitlines()` per row):

- 33 index rows, exactly one per `corpus/lessons/*.md` file, **zero duplicates**,
  zero files without a row, zero rows naming a missing file.
- **Zero** rows whose `bytes=`/`lines=`/`sha8=` cells disagree with live bytes.
  The only row my checker flags is the self-referential README row itself
  (`corpus/lessons/README.md:70`), whose cells are `bytes=0 lines=0
  sha8=self-referential` by design.
- Verdict: **green**, but *unfiled* — the assembled audit
  (`reports/round-35/adj/A08-audit-draft.md`) should either add this surface with
  this evidence or record it as an explicit exclusion with a reason.

### F-R06-2 (artifact-set gap) — `declared-in-r7/run.log` is untracked

Round-34 claim D's `after_required` names the landing as "packet.md + twin +
expected.json + freeze.txt + **run.log**" (`reports/round-34/claims.json:38`).
The file exists on disk (`reports/round-34/handoff/declared-in-r7/run.log`,
1603 B, mtime Oct 19 04:34) but is **not in git**:
`git ls-files reports/round-34/handoff/declared-in-r7/` returns only
`claims-map.md`, `expected.json`, `freeze.txt`, `packet.md`, `twin.json`.
Cause: `.gitignore:3` `*.log`. A fresh clone therefore cannot see the freeze
run's console transcript, and the claim as written is unsatisfiable without
`git add -f`.

Scope/honesty note: this is a **systemic pattern, not an r34 regression** — the
same untracked `run.log` sits in `reports/round-30/handoff/declared-in-r6/`
(same claim shape at r30) and in ≥6 earlier handoff dirs (r11, r20, r22, r23,
r26, r27, r28 per `git status --porcelain --ignored`). Severity: low —
`freeze.txt` + `expected.json` carry the digests, and the packet/twin pair is
tracked. Owner: integrator (file the transcript under a non-`.log` name, or
`git add -f` and record the exception), or record the omission as an accepted
class. Not a blocker for claim A; it *is* a named-finding the audit document
should carry rather than pass silently.

### F-R06-3 (boundary observation, green) — the `.ufo` deletion is pre-baseline and the REGIMEN path resolves at the fleet root

The single deletion in the window, `.ufo/reports/round-32/kotodama.md`, belongs
to commit `139e3b6` ("fleet report belongs at the fleet root (.ufo/), not the
lane repo", author+committer date 2026-10-18 22:06 −0300). That commit **is the
declared baseline of round 33** (`reports/round-33/claims.json:11`), so the
deletion is pre-baseline for both rounds and was authored by the parent, not a
seat. At HEAD the repo carries **zero tracked `.ufo` paths**
(`git ls-files .ufo | wc -l` → 0; `ls -R .ufo` → no such directory), so the
round-35 hard boundary "fleet `.ufo/**`" has no in-lane surface to violate.

`REGIMEN.md:46` still requires the per-round report at
`.ufo/reports/round-<N>/kotodama.md`. Read-only check of the fleet root
(`/home/vgpnk/Projects/shokunin/.ufo/reports/`, outside this repo): round-33
(`kotodama.md`, 8312 B, 2026-10-19 03:45) and round-34 (`kotodama.md`, 6259 B,
2026-10-19 04:53) both exist. Verdict: green — the clause is satisfied at the
fleet root; the deletion was the correction that made that true.

### F-R06-4 (negative result, load-bearing for X00/R08) — freeze read-set ∩ touched surfaces = ∅

The v1/v3 read sets (`tools/exercise-handoff-e2e.py:118-142`, `:462`) contain
exactly one `corpus/knowledge` member, `CONTRACT =
corpus/knowledge/synthesis/worldbible-integration-contract.md` (`:118`), and
their `examples/` members are `culture-d3/packet.json`, `packet.gates.yml`,
`controls.json`, `expected.json`, `components/{04,05,06,07}*.json` (`:119-128`)
and `culture-d2/packet.d2.yml`, `typed-labels.d2.yml` (`:129-130`). Therefore:

- **None** of the four r33-edited `examples/` files (README.md, handoff.md,
  handoff-packet.sample.md/.yml) is a read-set member.
- The r33-edited ceilings entry is not referenced by the freeze apparatus at all
  (`grep -rln register-lexicon-ceilings reports/round-34/handoff/declared-in-r7/
  reports/round-30/handoff/declared-in-r6/ tools/` → no hits).
- The contract file itself was **not** touched in the window and last moved in
  round 8 (`git log -1 -- corpus/knowledge/synthesis/worldbible-integration-contract.md`
  → `e1694ba`). Its live sha256 is
  `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`
  (`sha256sum`), exactly the value r33 wrote into all four repointed files
  (`git diff 139e3b6 da68a6d -- examples/`) — the repoints are **accurate
  readings** of live bytes, not read-set edits.

So a re-freeze sees drift from r33/r34 only through round-34's *intentional*
default move to `declared-in-r7` (`tools/exercise-handoff-e2e.py:1933-1934`),
which is claim D's own landing. This is the evidence X00/R08 need; it also
bounds R08's "would a re-freeze see drift?" question for the round-35 C-claim:
ten new `corpus/knowledge/*` entries are outside the read set, but the integrator
must not touch `corpus/knowledge/synthesis/worldbible-integration-contract.md`.

### F-R06-5 (spot check, green) — language scan and PROVINCE conformance of the touched live surfaces

`grep -n -iE '\b(canon|clearance|promotion|promote|closure|closed)\b'` on the
seven non-bookkeeping touched surfaces: every hit is a negation, a NON-CANON
declaration, or a lore-ownership pointer — e.g.
`examples/handoff-packet.sample.md:15` ("canon_standing: not canonized — lore
disposition required"), `corpus/lessons/README.md:15` ("**Canon:** NON-CANON
engineering evidence"), ceilings entry `:3` ("canon decisions belong to
lore-shokunin"), `:241` ("This lane's own, and NON-CANON").
`tools/harness/receipt_guard_adoption.py`: **zero** hits. No promotion,
clearance or closure assertion appears on any touched live surface.

PROVINCE spot check at HEAD: `PROVINCE.md:9-11` owns "this lane's own gates,
source-check records, non-canon examples and reports" → the new instrument
`tools/harness/receipt_guard_adoption.py` and the r7 packet directory are inside
the owns list; nothing in the census lands on the refuses list (`PROVINCE.md:16-20`:
canon, rights/attribution rulings, game mechanics, general source-research
method, web publishing, prompt/skill craft). Full re-verification remains
A06/A11's leg; this is a spot check only.

## 4. Method limitation (honest bound)

A git-diff census sees **content changes only**. A file rewritten to identical
bytes, or edited and reverted inside the window, leaves no trace; mtime-only
touches are invisible. The complement to this census is the r33/r34 fragment-level
touch lists (K04's mission) — without that fragment the 14-surface list above is
complete for byte changes and *unverified* for no-net-change touches.

## Owed

- `reports/round-35/scout/K04-touched-census.md` — missing at review time; the
  integrator must diff K04's census against §2 above and file any surface in
  K04's list that my diff cannot see (no-net-change touches), or record that
  K04's list is a subset of mine.

## Citations

Paths (all relative to the repo root unless noted):

- `reports/round-35/claims.json:56` (A-claim surface list), `:11` (baseline 4a7aede)
- `reports/round-35/targets.json` seats A01–A10, K04 (missions)
- `reports/round-33/claims.json:11` (r33 baseline `139e3b6`); `reports/round-34/claims.json:9` (r34 baseline `da68a6d`), `:38` (claim D artifact list incl. run.log)
- `REGIMEN.md:46` (fleet report path clause)
- `.gitignore:3` (`*.log`)
- `PROVINCE.md:9-11`, `:16-20`, `:27-29`
- `tools/exercise-handoff-e2e.py:118-142`, `:184`, `:462`, `:1933-1934`
- `corpus/lessons/README.md:70` (self-referential row), `:49` (C31 rule), `:107-111` (revision-3 block)
- `LOG.md:3577` (SKILL.md digest move), `:3581-3582` (AGENTS.md excision)
- `reports/round-34/handoff/declared-in-r7/` (5 tracked files; `run.log` on disk only)
- `/home/vgpnk/Projects/shokunin/.ufo/reports/round-33/kotodama.md`, `round-34/kotodama.md` (read-only, fleet root, outside this repo)

Commands run (all in-tree, read-only; `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `git diff --name-status cdd66d7 4a7aede | awk '{print $1}' | sort | uniq -c` → 160 A / 11 M / 1 D
- `git diff --name-status cdd66d7 4a7aede -- reports/round-33 reports/round-34 | awk '{print $1}' | sort | uniq -c` → 158 A
- `git diff --name-status cdd66d7 4a7aede -- reports/ | grep -vE '^A[[:space:]]'` → no output (exit 1)
- `git diff --numstat cdd66d7 4a7aede | awk ...` → 172 files, +58808 / −187
- `git ls-files | wc -l` → 2815; `git ls-tree -r --name-only 139e3b6 | wc -l` → 2655; `git ls-tree -r --name-only cdd66d7 | wc -l` → 2656
- `git ls-files .ufo | wc -l` → 0; `ls -R .ufo` → no such directory
- `git ls-files reports/round-34/handoff/declared-in-r7/` → 5 files (no run.log); `ls -la` of the same dir → run.log 1603 B present
- `git status --porcelain --ignored` → untracked `reports/round-35/`; ignored `run.log` in r11/r20/r22/r23/r26/r27/r28/r30 handoff dirs
- `git log --format='%h %ad %s' -3 -- corpus/knowledge/synthesis/worldbible-integration-contract.md` → last move `e1694ba` (round 8)
- `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` → `5f4c02bf…`
- `git diff 139e3b6 da68a6d -- examples/` → 4 digest repoints `50c4c2f2…` → `5f4c02bf…`
- `git diff da68a6d 4a7aede -- tools/exercise-handoff-e2e.py` → CLAIMS_MAP + V3 default move, +11/−10
- `python3 -B` row-audit script over `corpus/lessons/README.md` → 33 rows, 0 duplicates, 0 mismatches (script inline in §3 F-R06-1)
- `grep -n -iE '\b(canon|clearance|promotion|promote|closure|closed)\b' <7 touched surfaces>` → negations/pointers only
- `grep -rln register-lexicon-ceilings reports/round-34/handoff/declared-in-r7/ reports/round-30/handoff/declared-in-r6/ tools/` → no hits
- `ls -la /home/vgpnk/Projects/shokunin/.ufo/reports/round-33/ /home/vgpnk/Projects/shokunin/.ufo/reports/round-34/` → kotodama.md present in both (read-only, out-of-repo)
