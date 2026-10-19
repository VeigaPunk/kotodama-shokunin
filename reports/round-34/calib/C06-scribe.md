- Seat: C06 | scribe | C | date 2026-10-19 | baseline da68a6d

# C06 — Landed-changes material for claim C (box-1 durable re-survey + A09 R1–R8 anchor reissue)

**Mission** (`reports/round-34/targets.json:60`): "Scribe: Landed-changes material for claim C."
Claim C (`reports/round-34/claims.json:54-66`): pin the box-1 executable-surface evidence
durable at SKILL.md sha256 `f9bd07c2…`, and file the A09 R1–R8 SKILL anchor reissue as
**new rows** (old anchors recorded as superseded readings; filed rows untouched).

Every number below was measured this seat at baseline `da68a6d` (worktree clean,
`git status --porcelain` → only `?? reports/round-34/`), env
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. No file was written outside this
fragment. No round runner was executed (F-C13-1 rule; `reports/round-34/targets.json:9`).

---

## 1. Landed set — what claim C adds (three artifacts, all NEW files)

| # | path | kind | status | content source | landed by |
|---|---|---|---|---|---|
| L1 | `reports/round-34/craft/box1-resurvey-durable.json` | durable machine receipt (28 rows + digest pin + date) | **not yet on disk** — path fixed by `reports/round-34/claims.json:60` and `reports/round-34/targets.json:56` | C02's fenced JSON, values re-measured from §2/§3 below | integrator |
| L2 | `reports/round-34/craft/box1-resurvey-receipt.md` (proposed name) | dated human receipt binding L1 to its counting commands | **not yet on disk**; no landed fragment fixes this path | C05 receipt draft, then C09 fold | integrator — **path `to-verify`** |
| L3 | `reports/round-34/craft/skill-anchor-reissue.md` (proposed name) | A09 R1–R8 anchor reissue: old anchor → new anchor → owning row | **not yet on disk**; no landed fragment fixes this path | C03's table (this fragment supplies the measured shift map, §4) | integrator — **path `to-verify`** |

Zero **edited** files. Claim C's declared `after_required` is satisfied by additions only
(`reports/round-34/claims.json:60`); §5 is the byte-preservation control.

The directory `reports/round-34/craft/` does not exist yet (`find reports/round-34 -type f`
→ `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`,
`depth/D11-preservation.md`); the integrator creates it when landing L1–L3.

## 2. Before-state, measured at baseline

| fact | measured value | command |
|---|---|---|
| SKILL.md digest | `f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` | `sha256sum SKILL.md` |
| SKILL.md length | 732 lines (was 715 at `da68a6d^`) | `wc -l SKILL.md` |
| SKILL.md blob at HEAD | `4d7a5c99c3d7f9f413ed348f8f62d79cb5ec538a` | `git rev-parse HEAD:SKILL.md`; `git hash-object SKILL.md` (equal ⇒ worktree = filed bytes; `git diff --numstat -- SKILL.md` empty) |
| box-1 survey at those bytes | `{"named": 28, "resolvable": 28, "unnamed_in_skill": [], "skill_sha256": "f9bd07c2…"}`, **exit 0** | `python3 -B reports/round-30/craft/box1-survey.py` |
| durable receipt for that digest | **none** — the r33 adjacency record says so in as many words: "A fresh box-1 survey reports 28/28 and this digest, but only as console output, not a new durable receipt" | `reports/round-33/adj/audit-assembled.md:30` |
| last filed box-1 receipt | `reports/round-30/craft/box1-landed-survey.json:4` pinned `83b0a78a…` (sha256 `aa8b6c15…`) | `sha256sum reports/round-30/craft/box1-landed-survey.json` |
| current-at-HEAD pin carriers that read stale | `reports/round-31/validation.json:1026`, `reports/round-32/validation.json:1000`, `reports/round-32/final-dossier.md:46,133`, `reports/round-32/dossier-d1{1,2,3}-*.md:50,97,48`, `reports/round-32/scribe/fragment-ledger.md:178,235` — all name `79fe91d3…` | `grep -rn "79fe91d3" --include=*.md --include=*.json .` (filed rows, never edited) |

## 3. The durable JSON is a **hand-assembled** artifact, not a tee of stdout (finding S-C06-1)

Tool output shape (`reports/round-30/craft/box1-survey.py:8-11`):
`date` (**hard-coded literal `"2026-10-18"`**), `named`, `resolvable`, `unnamed_in_skill`,
`skill_sha256`; exit 0 iff `resolvable == named` (`:12`).

Filed r30 receipt shape (`reports/round-30/craft/box1-landed-survey.json:2-8`):
`date`, `mode: "landed"`, `skill_sha256`, `named_in_skill`, `resolvable`, `unresolvable`,
`box1_note`.

Consequences the integrator must apply when landing L1:
- A verbatim redirect of the tool's stdout files `"date": "2026-10-18"` — a **wrong date** for
  a 2026-10-19 receipt. The date field must be written by the receipt, not inherited.
- Field names differ (`named`→`named_in_skill`, `unnamed_in_skill`→`unresolvable`) and `mode`
  / `box1_note` have no tool source, so L1 cannot be produced by `... > file`. Mirror the r30
  shape and add the per-row inventory.
- The r30 provenance's `REGISTER_CRAFT_SURVEY_MODE=landed` prefix
  (`reports/round-30/craft/review-D29-box1.md:158`) is **inert**: the tool reads no environment
  (`grep -c "environ\|getenv" reports/round-30/craft/box1-survey.py` → `0`). Do not repeat the
  prefix as if it selected a mode; if L1 needs a mode distinction, carry it as a field.

**28-row inventory re-measured this seat** (distinct `tools/*.py` paths named in SKILL.md;
command: python one-liner, `re.findall(r"tools/[\w./-]+\.py", skill)` deduped, each path
resolved with `Path.is_file()` and hashed). `named=28` matches the survey's count, and every
row resolves — this is the cross-check data for C02's rows and C07's independent re-run:

| # | path | SKILL.md line(s) | resolves | sha8 |
|---|---|---|---|---|
| 1 | `tools/assemble-culture-d3.py` | 673 | yes | `ba8d19d5` |
| 2 | `tools/assemble-culture-d4.py` | 207 | yes | `943f487b` |
| 3 | `tools/assemble-d2-typed.py` | 449 | yes | `c7e5a749` |
| 4 | `tools/assemble-d2.py` | 615 | yes | `8ea6bdde` |
| 5 | `tools/assemble-d4-typed.py` | 139,158,163,195,207,210,211,213,294 | yes | `92f5460b` |
| 6 | `tools/check-craft-exercise.py` | 616 | yes | `b5b890b4` |
| 7 | `tools/check-evidence-coupling.py` | 674 | yes | `849494b0` |
| 8 | `tools/check-gate-battery.py` | 617 | yes | `455b595a` |
| 9 | `tools/d2-typed-labels.py` | 35,169,208,258,272,281,288-293,304,308,329,479,481,483,491 | yes | `2819f687` |
| 10 | `tools/exercise-handoff-e2e.py` | 448 | yes | `a5e4a8c5` |
| 11 | `tools/gates/argot-derivation-gate.py` | 375-377,429,438 | yes | `b5406bcd` |
| 12 | `tools/gates/costume-era-consistency-gate.py` | 609 | yes | `e6bffd70` |
| 13 | `tools/gates/d4-assembly-check-gate.py` | 450 | yes | `df1a364b` |
| 14 | `tools/gates/d4-typed-labels-check-gate.py` | 451 | yes | `05f99629` |
| 15 | `tools/gates/handoff-packet-check.py` | 500,612 | yes | `e2fa3223` |
| 16 | `tools/gates/lexicon-coverage-audit.py` | 607 | yes | `2c4dd397` |
| 17 | `tools/gates/myth-consistency-gate.py` | 608 | yes | `5368b135` |
| 18 | `tools/gates/naming-collision-gate.py` | 610 | yes | `d9e4e8f4` |
| 19 | `tools/gates/phonology-sanity-gate.py` | 606 | yes | `d5fe087f` |
| 20 | `tools/gates/provenance-audit.py` | 611 | yes | `8a96aaf4` |
| 21 | `tools/gates/register-law-gate.py` | 409,410,418,430,439 | yes | `15f8b232` |
| 22 | `tools/gates/typed-pipeline-gate.py` | 138,187,196,209,212,418,431,439 | yes | `b749ad07` |
| 23 | `tools/harness/packet_links.py` | 452 | yes | `66d854cc` |
| 24 | `tools/harness/packet_uncertainty.py` | 89,128,501 | yes | `cdcc1931` |
| 25 | `tools/harness/r8_checks.py` | 454 | yes | `0fb21d8e` |
| 26 | `tools/harness/receipt_guard.py` | 453 | yes | `d2297da4` |
| 27 | `tools/replay-frozen.py` | 212,573,613 | yes | `a2fb5c98` |
| 28 | `tools/source-audit-inventory.py` | 614 | yes | `f617bb99` |

## 4. Anchor reissue scope — measured shift map for C03's table (support, not a substitute)

The 715 → 732 delta is **not uniform**, so a single "+17" reissue row would be wrong.
Hunk map from the only round-33 SKILL.md landing (`git show da68a6d -- SKILL.md | grep "^@@"`;
numstat `35 18 SKILL.md`):

| old range | new range | delta | shifted band |
|---|---|---|---|
| `@@ -125,7 +125,7 @@` | equal | 0 | old < 581 |
| `@@ -476,19 +476,19 @@` | equal | 0 | old < 581 |
| `@@ -498,7 +498,7 @@` | equal | 0 | old < 581 |
| `@@ -581,7 +581,9 @@` | **+2** | +2 | old 581–690 |
| `@@ -691,17 +693,31 @@` | **+14** | +16 | old 691–710 |
| `@@ -711,5 +727,6 @@` | **+1** | +16 | old 711–715 (tail) |

Measured spot checks at HEAD (each `sed -n '<n>p' SKILL.md`):
- **unchanged**: `:47` (self-cite referent, text identical pre/post — `git show da68a6d^:SKILL.md | sed -n '47p'` equals `sed -n '47p' SKILL.md`), `:294`, `:456`, `:458`, `:522` (`## Checklist (executable where a tool exists)`), `:534` (last content line), `:535` blank, `:536` (`## Corpus map`).
- **+2**: D3 heading `:660` → `:662` (`## Source-bounded culture drill — D3 (round 7)`).
- **+16** in the tail: old `:710` → `:726`; old `:713-715` (the round-31-landed availability/dispatch checklist item, verified verbatim against `git show da68a6d^:SKILL.md | sed -n '710,715p'`) → **`:729-731`**, with the re-keyed audit one-liner now at `:732`.

Two reissue rows that are **not** plain re-points (findings S-C06-2, S-C06-3):
- **S-C06-2 — A09 R5's `AGENTS.md:42` anchor no longer exists at baseline.** Pre-round-33 it
  read `### 2.2 \`SKILL.md\` — append one item to "## Checklist (executable where a tool exists)" (after :534)`
  (`git show da68a6d^:AGENTS.md | sed -n '40,44p'`; file was 42 lines). `da68a6d` removed it:
  `git show da68a6d --numstat -- AGENTS.md` → `0 2 AGENTS.md`; live `AGENTS.md` is 40 lines
  (sha256 `5ae7a9c8abab0843cfc6db09849f2fff369c0e880085deb546ec7ab764333808`, equal to the r33
  audit's reading `reports/round-33/adj/audit-assembled.md:41`) and `grep -n "SKILL.md" AGENTS.md`
  → **0 hits**. The reissue row must read **withdrawn at `da68a6d` (anchor deleted, no re-point)**,
  not "old `:42` → new `:N`".
- **S-C06-3 — the checklist-position defect is still open, so the reissue must say so.** A09's
  R5 half and open item Q-32-3 locate the executable item "outside `## Checklist` (`:522-534`)"
  (`corpus/lessons/round-32.md:57`; `corpus/lessons/README.md:244`). At HEAD the item sits at
  `:729-731` while `## Checklist` still ends at `:534` — the reissue records the *new address*
  and carries the *open* status; a reissue that reads as a fix would be a false green.

## 5. Work-performed / commit-ready material for claim C

- **Landed-changes line (fleet report §"Landed changes", claim C):** three new files —
  `reports/round-34/craft/box1-resurvey-durable.json` (28/28 resolved at SKILL.md
  `f9bd07c2…`, dated, digest-pinned), its dated receipt, and the A09 R1–R8 anchor reissue
  table; **zero** edits to `SKILL.md`, `AGENTS.md`, `corpus/lessons/**`, or any
  `reports/round-1..33/**` byte.
- **Before → after (claim C):** *before* — box-1 green only as console output at the new
  digest (`reports/round-33/adj/audit-assembled.md:30`); last filed receipt pinned the
  superseded `83b0a78a…` (`reports/round-30/craft/box1-landed-survey.json:4`); A09's R1–R8
  anchor list stale with no reissue (`reports/round-33/adj/A09-pins.md:105-114`).
  *after* — a durable, re-runnable receipt at `f9bd07c2…` (L1) plus a reissue table whose
  every old anchor is measured against `da68a6d^` and every new anchor against `da68a6d` (L3),
  with old anchors filed as **superseded readings**.
- **Regeneration recipe for L1** (paste into the receipt, citing §2/§3):
  `sha256sum SKILL.md` → `f9bd07c2…`; `wc -l SKILL.md` → 732;
  `python3 -B reports/round-30/craft/box1-survey.py` → exit 0, 28/28; then write the
  hand-assembled JSON per §3.
- **Byte-preservation control (verified this seat):**
  `git status --porcelain reports/round-30 reports/round-32 reports/round-33` → **empty**;
  `git status --porcelain` → only `?? reports/round-34/`; `git diff --numstat -- SKILL.md` and
  `-- AGENTS.md` → empty; `git hash-object SKILL.md` == `git rev-parse HEAD:SKILL.md`.
- **Superseded-reading inventory for the receipt** (record, never edit — `A09-pins.md:67-75`
  class E2/E3): `79fe91d3…` at `reports/round-31/validation.json:1026`,
  `reports/round-32/validation.json:1000`, `reports/round-32/final-dossier.md:46,133`,
  `reports/round-32/dossier-d11-shonen-boxes.md:50,205`,
  `reports/round-32/dossier-d12-capability-inventory.md:97`,
  `reports/round-32/dossier-d13-operator-decisions.md:48`,
  `reports/round-32/scribe/fragment-ledger.md:178,235`,
  `reports/round-33/op/{K01,O05,O08}*` (K01 `:136`, O05 `:270`, O08 `:208,340`),
  `reports/round-33/calib/C04-item-04.md:34,317,409`,
  `reports/round-33/calib/C06-item-06.md:184,245,267`,
  `reports/round-33/calib/C15-ledger-draft.json:150,165`;
  `83b0a78a…` at `reports/round-30/craft/box1-landed-survey.json:4` and
  `reports/round-30/validation.json:449`; `56`-class line anchors in
  `corpus/lessons/{README.md:242,244,245, round-14.md:141, round-15.md:25, round-19.md:88,100,101,179, round-25.md:44, round-31.md:46, round-32.md:7,33,41,55,57,58}`
  (`grep -rn "SKILL\.md:[0-9]" corpus/lessons/*.md` → 7 files). All filed bytes stay untouched.

## 6. Scribe findings

| id | finding | class | owner |
|---|---|---|---|
| S-C06-1 | The durable receipt cannot be a stdout redirect: the tool hard-codes `"date": "2026-10-18"` (`box1-survey.py:8`) and its field names differ from the filed r30 receipt shape; the `REGISTER_CRAFT_SURVEY_MODE=landed` prefix has no effect (0 env reads). | real — would land a mis-dated receipt | integrator + C02 |
| S-C06-2 | A09 R5's live anchor `AGENTS.md:42` was deleted by `da68a6d` (`0 2 AGENTS.md`); the reissue row must record withdrawal, not a re-point. | real — reissue completeness | integrator + C03 |
| S-C06-3 | The anchor reissue's old→new map is banded (0 / +2 / +16), and the misplaced checklist item is still misplaced at `:729-731`; a uniform shift or a "fixed" reading would be false. | real — reissue accuracy | integrator + C03/C08 |
| S-C06-4 | Scribe-side: `reports/round-34/calib/` held no C fragments at this seat's reads, so L2/L3 paths are proposals, and the 28-row cross-check table in §3 is author-side measurement (C07 owns the independent re-run). | procedural | integrator |

## Owed

- `reports/round-34/calib/C01-survey-run.md`, `C02-receipt-json.md`, `C03-anchor-reissue.md`,
  `C05-receipt.md` — not on disk at this seat's reads (`ls reports/round-34/calib/` → empty).
  L1's exact JSON rows come from C02; L3's table from C03. This fragment supplies the measured
  shift map (§4) and the 28-row cross-check (§3) those seats must reproduce or contradict.
- The landed **paths** of L2 (`…/box1-resurvey-receipt.md`) and L3 (`…/skill-anchor-reissue.md`)
  are proposals — `reports/round-34/claims.json:60` fixes only L1's path. Marked `to-verify`
  until C05/C09 name them; the integrator should adopt these names or record its own.
- `reports/round-34/depth/D11-preservation.md` (claim D) and `reports/round-34/cross/*` were not
  read by this seat; cross-claim collision handling is X00/X02's, not restated here.

## Citations

- `reports/round-34/targets.json:60` (C06 mission + out path), `:5-11` (shared rules), `:10` (missing-dependency rule); `reports/round-34/claims.json:54-66` (claim C full text incl. `:56` claim, `:60` after_required); `reports/round-34/telemetry/dispatch-declared.json:16-17` (baseline commit).
- `reports/round-30/craft/box1-survey.py:5-12`; `reports/round-30/craft/box1-landed-survey.json:2-8`; `reports/round-30/craft/review-D29-box1.md:158`; `reports/round-30/validation.json:444-452`.
- `reports/round-33/adj/audit-assembled.md:30,41`; `reports/round-33/adj/A09-pins.md:39-41,67-83,105-114,120-127` (E2/E3 digest sites, R1–R8 list, findings); `reports/round-33/adj/A16-shonen-material.md:20-33`.
- `reports/round-31/validation.json:1020-1028`; `reports/round-32/validation.json:1000`; `reports/round-32/final-dossier.md:46,131,133`; `reports/round-32/dossier-d11-shonen-boxes.md:50,205`; `reports/round-32/dossier-d12-capability-inventory.md:97`; `reports/round-32/dossier-d13-operator-decisions.md:48`; `reports/round-32/scribe/fragment-ledger.md:176,178,235`.
- `corpus/lessons/README.md:242,244,245`; `corpus/lessons/round-14.md:141`; `corpus/lessons/round-15.md:25`; `corpus/lessons/round-19.md:88,100,101,179`; `corpus/lessons/round-25.md:44`; `corpus/lessons/round-31.md:46`; `corpus/lessons/round-32.md:7,33,41,55,57,58`.
- `SKILL.md:47,149,183,294,456,458,522,534,535,536,662,726,729,730,731,732` (measured addresses at `f9bd07c2…`/732 lines); `AGENTS.md:1-40`.
- Commands run this seat (2026-10-19, repo root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`): `ls reports/round-34/ reports/round-34/calib/`; `find reports/round-34 -type f`; `sha256sum SKILL.md AGENTS.md PROVINCE.md reports/round-34/claims.json reports/round-34/targets.json reports/round-30/craft/box1-landed-survey.json reports/round-30/craft/box1-survey.py`; `wc -l SKILL.md`; `python3 -B reports/round-30/craft/box1-survey.py` → exit 0, `{"named": 28, "resolvable": 28, "unnamed_in_skill": [], "skill_sha256": "f9bd07c2…"}`; python one-liner enumerating distinct `tools/*.py` names in SKILL.md with line numbers, resolution and per-file sha256 prefix (§3 table); `grep -c "environ\|getenv" reports/round-30/craft/box1-survey.py` → 0; `git status --porcelain`; `git status --porcelain reports/round-30 reports/round-32 reports/round-33` → empty; `git diff --numstat -- SKILL.md AGENTS.md` → empty; `git hash-object SKILL.md` == `git rev-parse HEAD:SKILL.md` → `4d7a5c99…`; `git log --oneline -3 -- SKILL.md AGENTS.md`; `git show da68a6d --numstat -- SKILL.md AGENTS.md`; `git show da68a6d -- SKILL.md | grep "^@@"`; `git show da68a6d^:SKILL.md | wc -l` → 715 and `| sha256sum` → `79fe91d3…`; `git show da68a6d^:SKILL.md | sed -n '47p;710,715p'`; `git show da68a6d^:AGENTS.md | wc -l` → 42 and `| sed -n '40,44p'`; `grep -n "SKILL\.md" AGENTS.md` → 0 hits; `grep -n "^## " SKILL.md`; `grep -n "^- \[ \]" SKILL.md`; `sed -n '<n>p' SKILL.md` for the anchor spot-checks; `grep -rn "79fe91d3\|f9bd07c2" --include=*.md --include=*.json --include=*.py .`; `grep -rn "SKILL\.md:[0-9]" corpus/lessons/*.md`.
