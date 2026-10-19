- Seat: A07 | verifier | claim A | date 2026-10-19 | baseline 4a7aede

# A07 — independent re-run of the A-block command set

**Dependency state.** At my first read `reports/round-35/` held only `claims.json`,
`targets.json` and `telemetry/`; `adj/` did not exist. I therefore derived the A-block
command set from the A-claim's `after_required` (`reports/round-35/claims.json:54-65`) plus
the six slice missions (`targets.json:254-294`) and ran it myself (§1). A01, A05, A06 and
A11 landed while I wrote; I then replayed their cited values command by command (§2).
A02, A03, A04 and A08 had not landed at my close — their *surfaces* are covered by §1 rows
13-17, and the literal citation replay is owed (§Owed).

Method: every command ran in-tree **except** the r6-row replay, which ran in an isolated
`git archive HEAD` copy under `.scratch/a07-iso`. No `reports/round-*/run-validation.py`
was executed anywhere; no `--freeze` mode was used. `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1` for all runs. `git status --porcelain` after every run:
`?? reports/round-35/` only.

## 1. Per-surface verification (independently derived command set)

| # | surface (slice) | command | observed | verdict |
|---|---|---|---|---|
| 1 | r7 freeze digests (A01) | `sha256sum reports/round-34/handoff/declared-in-r7/*` vs `repin.json` `R34-D-new-row.digests` | packet `45f57132…fac19`, twin `0e229138…96599`, expected `bbe15887…9d55`, freeze.txt `3969954b…1223`, claims-map `d181de28…8980c` — **5/5 MATCH** | green |
| 2 | r7 artifact manifest (A01) | parse the 58 `A-nn` rows of `packet.md` §artifact_manifest; re-hash + stat each path | **58/58** rows: digest AND byte count match live bytes | green |
| 3 | r7 read-set vs frozen twin (A01) | compare each manifest row's path+digest to `expected.json` `.inputs` | **0 mismatches**; `.inputs` has 58 entries | green |
| 4 | r6 stale row (A01) | `sha256sum reports/round-30/handoff/declared-in-r6/expected.json` | `ea1e2927…da8a0` == `repin.json` `R34-D-stale-row.surface_sha256` | green |
| 5 | r7 default chain (A01) | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0; `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f57132…fac19` | green |
| 6 | renderer selftest (A01/O) | `python3 -B tools/exercise-handoff-e2e.py --selftest` | exit 0; positive run + **17 controls** | green |
| 7 | **R34-N1 defect** (A01/O) | isolated copy: `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | exit 1; `KeyError: 'reports/round-20/handoff/claims-map.md'` at `tools/exercise-handoff-e2e.py:3822` in `v3_exercise` on `assembly.digests[rel]` | reproduced |
| 8 | gate stdout pin (A01) | `python3 -B tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md` | exit 0; stdout sha256 `7c5810479045c26bcc3b1c7364934f53147641504a766eeffeaaec4d2d624685` == `expected.json` `cross_refs.gate_stdout_sha256` | green |
| 9 | contract digest pin (A01/A03/A05) | `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` | `5f4c02bf…f79069` == `expected.json` `cross_refs.contract_digest` == pin at `examples/culture-d3/handoff.md:27,74` == `examples/handoff-packet.sample.md:21` == `examples/handoff-packet.sample.yml:45,78` == `reports/round-33/adj/contract-read-record.md:5` | green |
| 10 | claims ledger (A01) | independent parse of the `CL` rows of `packet.md` | **27** rows (`D2-CL01`, `D2-CL02`, `CL01–CL13`, `D4-CL01–D4-CL12`), statuses **16 supported / 7 partial / 4 unresolved** == `freeze.txt:6`, `expected.json` `uncertainty.statuses` | green |
| 11 | successor map re-parse (A01) | `D4_ROW_RE` literal at `tools/exercise-handoff-e2e.py:2286` applied to `declared-in-r7/claims-map.md` | exactly **12** matching rows == `repin.json` `R34-D-edit-set.successor_row` | green |
| 12 | renderer edit sites (A01) | `grep -n 'declared-in-r7\|CLAIMS_MAP' tools/exercise-handoff-e2e.py` | `CLAIMS_MAP` `:184`; `V3_BASELINE_DEFAULT` `:1933`; `V3_FROZEN_DIR_DEFAULT` `:1934` — all → `declared-in-r7` == `repin.json` `R34-D-default-pointer.surface` | green |
| 13 | guard tool (A02) | `python3 -B tools/harness/receipt_guard_adoption.py --selftest`; then `--json` | selftest exit 0, `selftest_passed` true; `--json` exit 0, `census_complete` true, `runner_count` **29**, `class_counts` **{guarded-refresh 18, unguarded-in-place 11}**, `hazard_count` 11, `gaps` [] | green, see **F1** |
| 14 | adoption inventory (A02) | `json.load` + field compare vs the live `--json` | inventory: `runner_count` **28**, `class_counts` **{17, 11}**, `date` 2026-10-19, `glob` `reports/round-*/run-validation.py`; per-runner class disagreements vs live: **0**; only-in-live: `reports/round-34/run-validation.py` (`guarded-refresh`) | **F1** |
| 15 | guard-tool write confinement (A02) | `grep -nE "'/home\|/srv/\|/mnt/\|expanduser\|os.getenv\(.HOME" tools/harness/receipt_guard_adoption.py` | no hit outside `RESOLVE_ATTRS` (`:70`, a *recognition* list for scanned runners); `ROOT = Path(__file__).resolve().parents[2]` (`:58,:871,:897`); the `OUTPUT` constants at `:899-1013` are fixture text inside the selftest's synthetic `.scratch` runners, per its own `limits` | green |
| 16 | examples repoint (A03) | `git show da68a6d -- examples/`; residual-value sweep | 4 files repointed `50c4c2f2…` → `5f4c02bf…`; residual `50c4c2f2…` occurrences are **all** in filed/frozen bytes (`corpus/lessons/round-2-adjacency.md`, `tools/gates/frozen/handoff-packet-check/{r9-pre,r18-post}/packet.md`, `reports/round-7/**`, `reports/supplement-opencode-1/**`) — **none on a live surface** | green, with **F2** |
| 17 | contract digest history (A03) | `git log -- corpus/…/worldbible-integration-contract.md` + per-commit hash | `5f4c02bf…` since `e1694ba` (round-8, **2026-10-17 17:44:17 -0300**); previous value at `291c714` was `50c4c2f2…` | green (informs F2) |
| 18 | SKILL.md/AGENTS.md attribution (A04) | `git show --name-only 4a7aede` / `da68a6d` | r33 (`da68a6d`) carries **all** SKILL.md/AGENTS.md hunks; **r34 carries none** — its non-report paths are exactly `LOG.md`, `SCORECARD.md`, `tools/exercise-handoff-e2e.py`, `tools/harness/receipt_guard_adoption.py` | **F3** |
| 19 | reissue pins (A04/A05) | `wc -l`, `sha256sum`, `git show 139e3b6:SKILL.md` | HEAD `732` / `f9bd07c2bd134623…`; `139e3b6` `715` / `79fe91d3d42917a1…` == `craft/anchor-reissue.md:8-9`. AGENTS.md `42 → 40` == `:33` row R | green |
| 20 | live stale anchor cites (A04) | `grep -rn 'SKILL\.md:715\|SKILL\.md:713-715' corpus/lessons/` | **exactly 7** (`README.md:242,244`; `round-32.md:7,33,41,55,57`) == `anchor-reissue.md:35-38` | green |
| 21 | box-1 durable receipt (A05) | read receipt; re-run its own `reverify` command `python3 -B reports/round-30/craft/box1-survey.py` | receipt `skill_sha256` `f9bd07c2…` == live `SKILL.md`; `skill_lines` 732 == live; re-run exit 0 with `named 28 / resolvable 28 / unnamed_in_skill [] / skill_sha256 f9bd07c2…` == the receipt's `survey_stdout` | green |
| 22 | ceilings errata sweeps (A05) | five `grep -rl` sweeps over `corpus/knowledge/` | file counts **2 / 1 / 1 / 1 / 3** == the errata table's hits+files columns | green |
| 23 | errata's pre-existing-hit claim (A05) | `sed -n '106p' corpus/knowledge/linguistics/sound-symbolism.md`; `git log -1 --` it | line 106 carries "assign **which semantic fields** carry ideophones"; the file last moved in `94ca098` (round-10) → "pre-existing, false when written" verifies; `register-strata-attestation.md:315` carries §13 | green |
| 24 | contract-read-record (A05) | read + digest | `file_sha256` `5f4c02bf…` == live contract bytes; `:9` disclaims lore read/acceptance/receipt/canon standing | green, see **F6** |
| 25 | PROVINCE accuracy (A06) | `git log -1 -- PROVINCE.md`; `git show --name-only 4a7aede`; partition census | PROVINCE.md unchanged since `c53782a` (2026-10-17); partitions live 21/19/18/29/20/94 = **201**; every r34 path is `reports/round-34/**`, `LOG.md`, `SCORECARD.md` or `tools/**` → the new tool, the r7 packet and the repointed renderer all fall under `PROVINCE.md:9-11` | green |
| 26 | sibling-write / out-of-lane (A06) | `grep -rnE '/home/vgpnk' reports/round-33/ reports/round-34/ tools/harness/receipt_guard_adoption.py` | only **read-only citations** of `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44,45`, each marked out-of-lane / routed-not-absorbed (`calib/C16-receipt.md:69,130,169`; `K03-open-items.md:69-70,128`; `C01-item-01.md:247,305`). No write to any sibling path | green |
| 27 | preservation (A, all slices) | `git status --porcelain` after every in-tree run above | only `?? reports/round-35/` | green |
| 28 | r34 receipt consistency (cross) | read-only `reports/round-34/validation.json` | sha256 `ba2fa4dcf8f29a13…` == LOG's `ba2fa4dc…`; `acceptance_checks_passed` true; `baseline_revision` `da68a6d`; `runner_sha256` `be11ff46f1fe399c…` == the live sha of `reports/round-34/run-validation.py` as read by the guard census; `missing_dependencies` `[cross/X00-connector.md, depth/D17-verify-gates.md]` == LOG's "two seats never landed" | green |

## 2. Replay of the landed A-fragments' cited values

`A01-r7-packet.md`, `A05-records.md`, `A06-province.md` and `A11-verify-2.md` landed while
this seat ran. Every value below was re-executed by me at the same HEAD; **all reproduce
except the two defects filed in §3 (F5, F6)**.

### A01 — every cited value reproduces

| A01 claim (line) | my re-run | match |
|---|---|---|
| renderer `surface_sha256_before` `a5e4a8c5…` / `after` `34c85f57…` (`:16`) | `git show da68a6d:tools/exercise-handoff-e2e.py \| sha256sum` → `a5e4a8c5dda9d63c…`; live and `git show 4a7aede:…` → `34c85f5773fb1925…` | yes |
| `packet_uncertainty.py --packet twin.json --require-oq --json` → exit 0, claims 27, findings `[]` (`:237-238`) | exit 0, `{"claims": 27, "findings": []}` | yes |
| `packet_links.py --packet twin.json --repo-root . --json` → exit 0, 105/105 (`:239-240`) | exit 0, `resolved 105`, findings `[]` | yes |
| 12-row re-extraction → `--claims-json` → exit 0, claims 12, findings `[]` (`:241-243`) | rebuilt faithfully (`claim_id` + `uncertainty{status,basis}` from the heading + `u.basis` line): exit 0, `{"claims": 12, "findings": []}`, statuses 8/2/2, min basis 354 chars | yes |
| canon family line counts 18 / 9 / 8 / 1 / 2 (`:54`) | per-**line** counts: packet 18, claims-map 9, twin 8, expected 1, repin 2 | yes (unit is lines; see §4) |
| manifest path-prefix counts examples 32 / tools 12 / reports 9 / corpus 5 (`:226` instrument) | `grep -oE '\| [A-Z]-[0-9]+ \| [^ \|]+'` → 32/12/9/5, total 58 | yes |
| game-dev family: zero real hits (`:60`) | verdict holds; see F7 for an enumeration gap | verdict yes |
| cited line refs `expected.json:192,195,169,124`, `freeze.txt:2,3,10`, `repin.json:14,27,28,29,30,12` | all resolve to the claimed digest/pin lines | yes |
| resolution greps `prepared-not-accepted` / `not canonized` / `canonical` / `ACCOUNT-CLOSURE` (`:293`) | 1 / 5 / 5 / 1 hits, all resolving | yes |
| renderer line checks `:2290,:2779,:3521-3531,:3819,:3822` (`:294`) | `:2290` docstring "The twelve D4 rows…", `:2779` scope cell, `:3521` `unresolved_claims`, `:3819` input-drift leg, `:3822` the KeyError site | yes |

### A05 — reproduces except F5/F6

| A05 claim (line) | my re-run | match |
|---|---|---|
| errata sweeps 2/1/1/1/3 (`:283`) | 2/1/1/1/3 | yes |
| `which semantic fields` → 6 lines / 3 files (`:284`) | **7 lines / 3 files** under case-sensitive, `-i`, `--include='*.md'` and `\b…\b` variants | **no — F5** |
| `sed -n '106p' sound-symbolism.md`; last move `94ca098` (`:285-286`) | both exact | yes |
| `sha256sum reports/round-33/adj/contract-read-record.md` `e415ac6b18e287…` (`:299`) | `e415ac6b18e28750…` | yes |
| contract at `139e3b6` and live both `5f4c02bf…` (`:300`) | both `5f4c02bfc4e6e4e9…` | yes |
| `diff <(sed -n '137,150p' C08-item-08.md) contract-read-record.md` → only the two slots differ (`:301`) | two slot lines differ **plus a second hunk** `10,14d9` | **partly — F6** |
| `C08-item-08.md:141-144` is the draft (`:182`) | the draft block is C08 `:137-145`; `:141-144` is its middle | **no — F6** |
| `sha256sum reports/round-30/craft/box1-survey.py` `d923ae0f…` (`:289`) | `d923ae0fcd544513…` | yes |
| SKILL.md `f9bd07c2…` / 732 lines (`:288`) | exact | yes |
| `git diff --stat da68a6d 4a7aede -- tools/exercise-handoff-e2e.py` → 11+/10- (`:293`) | `11 insertions(+), 10 deletions(-)` | yes |
| `git log --oneline -3 -- tools/exercise-handoff-e2e.py` (`:294`) | `4a7aede`, `71cd9d3`, `3b13a2f` | yes |
| `grep -c "append one item" AGENTS.md` → 0, rc=1; `wc -l` 40 (`:149`) | 0 / rc=1; 40 | yes |
| `git show 139e3b6:AGENTS.md \| sed -n '42p'` (`:298`) | the excised `### 2.2 SKILL.md — append one item …` line | yes |
| `grep -n -i "game-dev\|…\|web publish"` over five surfaces → rc=1 (`:302`) | rc=1 | yes |
| `ls` spot-check of 15 corpus/tool paths cited by the ceilings entry → 0 missing (`:304`) | exhaustive instead of spot: **25 distinct cited paths, 0 missing** | yes (stronger) |
| **A05-F1** box-1 row digests 27/28, stale row `tools/exercise-handoff-e2e.py` `a5e4a8c5…` (`§3.1`) | independently re-hashed all 28 rows: **27 match, 1 stale — exactly that row** (`a5e4a8c5…` row vs live `34c85f57…`) | **confirmed** |
| **A05-P1** the audit token is `SKILL.md:732`, `:731` the preceding clause (`§3.2`) | `sed -n '729,732p'`: `:732` is the `(audit: python3 -c …)` line, `:731` the clause | **confirmed** |

### A06 — every cited value reproduces

`git rev-parse HEAD:PROVINCE.md` `313b182f251564b7997b06996b4f063370778f11`; `sha256sum
PROVINCE.md` `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`;
`wc -l -c` `31 1636`; `git log --oneline -- PROVINCE.md` only `c53782a`, `a527120`;
`ls -d reports/round-*` **31**; `ls tools/gates/*.py` **12**; `find corpus/knowledge
-maxdepth 1 -mindepth 1 -type d` **6**; `grep -cEi 'non-canon|not canonized|lore'
packet.md` **25**; `git check-ignore -v …/run.log` → `.gitignore:3:*.log`; the 7
non-canon-stamped example files each carry ≥1 stamp (`:46`); manifest prefix counts
32/12/9/5 (`:226`); `grep -c -i kotodama /home/vgpnk/Projects/shokunin/MANIFEST.json`
**84**. All match.

### A11 — every cited value reproduces

`git ls-tree 4a7aede reports/round-34/run-validation.py` → `100644 blob
08f0ebbbc41d22446cb7931086b3b24520f9ff4e`; `receipt_guard_adoption.py --selftest` →
`"selftest_passed": true`; `grep -nE 'parents\[[3-9]\]|\.\./\.\./\.\.'` over the two tools
→ rc=1 (no matches); the filed inventory reads 28/17 (`:406`) — which is **my F1**, i.e.
A11 corroborates the drift rather than the live value.

## 3. Defects and findings filed

### A07-F1 — `op/adoption-inventory.json` is a mid-round census; HEAD reads one runner more (medium)

`reports/round-34/op/adoption-inventory.json` records `runner_count` 28 and
`class_counts` `{guarded-refresh: 17, unguarded-in-place: 11}`. Re-running the landed tool
at HEAD gives `runner_count` **29** and `{guarded-refresh: 18, unguarded-in-place: 11}`.
The delta is exactly one runner — `reports/round-34/run-validation.py`, class
`guarded-refresh` (guard call `:517`, dominated by `:533`) — the round's own runner, which
did not exist when the census was taken. Per-runner class disagreements: **0**; the
inventory's only defect is coverage.

Not a fabrication and not wrong for its own date: `op/O02-tool-source.md:34,41` declared
28 / 17,11 at the time, and the inventory's `date` is 2026-10-19. The r34 ADMITTED
`LOG.md` entry already carries the HEAD-accurate figure (29 / 18 / 11), and
`A11-verify-2.md:406` reads the filed artifact as 28/17 — so the durable JSON is the one
artifact left at the stale count.

Owner: **A08 assembled audit / integrator.** Consequences: (a) a consumer reading the
inventory as a HEAD census is off by one; (b) a round-35 validation leg must assert
`29 / 18 / 11` (or read the inventory's own `date`-scoped numbers), else it fails against
the live tool. Filed bytes stay unedited; the correction is a new-record note.

### A07-F2 — repointed surfaces carry an under-dated measurement provenance (low)

`examples/culture-d3/handoff.md:27` ("§1 pin, **re-measured 2026-10-17** from current
bytes") and `examples/handoff-packet.sample.yml:79` (`digest_computed: "2026-10-17,
working tree"`) now carry `5f4c02bf…`, a value written on **2026-10-19** by r33
(`da68a6d`, 2026-10-19T03:52:53-0300). Two readings, and the text does not disambiguate:
the date names *when the measurement was performed* (false — 2026-10-19) or *which bytes
the value describes* (true — the contract has hashed `5f4c02bf…` since `e1694ba`,
2026-10-17 17:44:17 -0300, so a 10-17 measurement yields it too). The repoint itself is
correct: the superseded `50c4c2f2…` was the pre-round-8 digest.

Owner: **A03 slice / integrator.** The assembled audit should state the corrected reading
(value valid from 2026-10-17; the act of re-measurement was 2026-10-19). No in-place edit
is available under append-only discipline.

### A07-F3 — A04's slice wording attributes to r34 bytes that r34 never moved (low, scope/coverage)

`targets.json:278` describes A04 as "the round-33/34 SKILL.md edits (C14 fixes, O05
re-key, N1/N4/N5) + AGENTS.md excision". `git show --name-only 4a7aede` lists **no**
`SKILL.md` or `AGENTS.md`; every hunk in the 33–34 window is in `da68a6d` (r33). The r34
artifacts that *describe* the movement are `craft/anchor-reissue.md` and
`craft/box1-resurvey-durable.json` (verified in §1 rows 19-21).

Owner: **A04 / A08.** Attribute the SKILL.md/AGENTS.md bytes to r33 alone, filing the r34
reissue/box-1 records as descriptions of them; otherwise a reader hunting for r34 SKILL.md
hunks finds none and may mis-score the slice. Auditability is intact — the pins
(732/`f9bd07c2…`, 715/`79fe91d3…`, 42→40) all reproduce.

### A07-F5 — A05's `which semantic fields` line count is one short (low, defect against A05)

`A05-records.md:284` claims `grep -rn -i "which semantic fields" corpus/knowledge/` →
**6 lines / 3 files**. The instrument returns **7 lines / 3 files** at HEAD, and stays 7
under case-sensitive, `-i`, `--include='*.md'` and word-boundary variants. The seven:
`sound-symbolism.md:106`; `register-strata-attestation.md:399`;
`register-lexicon-ceilings.md:3,4,24,303,314` (per-file 1/1/5). The file count agrees, and
A05's verdict is unaffected (the errata's own table counts **files**, where 3 is right).
Owner: **A05 / A08** — correct the number when the audit is assembled, and state the
sweep's unit (see §4).

### A07-F6 — A05's contract-read-record diff characterization understates its own diff (low, defect against A05)

`A05-records.md:183` and `:301` characterize `diff <(sed -n '137,150p'
reports/round-33/calib/C08-item-08.md) reports/round-33/adj/contract-read-record.md` as
"only the two `<…>` slots filled — no field invented, no scope line dropped". Re-running
it: the slot hunk (`6,7c6,7`) is as claimed, **and** a second hunk `10,14d9` deletes five
extract lines — C08 `:146` (closing fence), `:147` (blank) and the first three lines of
C08's own **Surface** paragraph (`:148-150`, continuing to `:153`): "the round-scoped path
… is the cheapest landing, but the contract's wording asks for a *record*, and whether a
round-scoped report satisfies that (versus a durable lane surface) is the
integrator's/operator's call" — explicitly flagged `to-verify` by C08.

The filed record (9 lines) does not carry that paragraph, which is expected (it sits
outside C08's fenced draft block), and A05's "no scope line dropped" reading is correct
for the block. Two things are nevertheless imprecise: the diff is not "only the two slot
lines", and the draft block is C08 `:137-145`, not `:141-144` (`A05-records.md:182`).

Owner: **A05 / A08.** Material point for the assembled audit: the record's **surface
question** (does a round-scoped report satisfy contract §1's ask for a *record*, versus a
durable lane surface?) is flagged `to-verify` only in `C08-item-08.md:148-153` and is
carried by neither the filed record nor A05's verdict table. It should be listed as an
open item with owner integrator/operator — a routed-not-absorbed candidate, not a defect
in the record.

### A07-F7 — A01's game-dev row under-enumerates its own substring class (low, precision note)

`A01-r7-packet.md:60` gives the game-dev family 0 real hits and names the matches as the
substring in "textile" (`packet.md:139`, `:164`; `twin.json:945`, `:1234`). A01's own
token list includes `unity`, which also matches **"community"** — 6 occurrences on 4 lines
in `packet.md` (`:3,143,144,154`) and 5 lines in `twin.json` (`:1004,1006,1019,1188,1190`).
The verdict (zero real game-dev hits) is unaffected; the enumeration is incomplete.
Owner: **A01 / A08** — extend the note so a re-runner matching the same tokens does not
read the extra hits as unfiled bleed.

### A07-F4 — the language leg needs a term-collision exemption list (observation, instrument)

A mechanical scan of the round's **new** bytes for
`canoniz*|canonical|canon|promotion|promoted|clearance|approval|approve[ds]?|closure|closed`
flags 81 lines in `reports/round-34/handoff/**` and 2 in `craft/`+`op/adoption-inventory.json`;
15 and 1 respectively carry no negation marker on the same line. Inspected individually,
**zero** are lore-claim bleed; all fall in four benign classes:

- repo paths and identifiers: `packet.d4.yml#canon` (`claims-map.md:62`, `packet.md:151`, `twin.json:1016`), the twin field `ACCOUNT-CLOSURE` (`twin.json:130`), the JSON key `not_a_promotion_verdict` (`box1-resurvey-durable.json:9`);
- `canonical` for the era-tag namespace (`claims-map.md:122`, `packet.md:151` — "canonical E0–E3 tag");
- `closed` for defect/ledger closure, not a round-closure verdict (`claims-map.md:126`, `packet.md:306`, `twin.json:2614`, manifest class "closed round-6 source ledger", `packet.md:50-53`);
- negations that sit on the previous line: `claims-map.md:22` — the sentence starts at `:21` "**no** real-world referent, date, clearance or canon standing is claimed by any row".

Owner: **A08 / S04** — carry the exemption list, or the leg reports ~16 false positives.

### A07-G1 — green result worth carrying into the audit

Scanning **only added lines** of every r33/r34 non-report surface (`SKILL.md`, `AGENTS.md`,
`examples/**`, `corpus/knowledge/linguistics/register-lexicon-ceilings.md`,
`tools/exercise-handoff-e2e.py`, `tools/harness/receipt_guard_adoption.py`) yields
**exactly one** hit: `SKILL.md` "…clearance gate. Verify the native coda adapter, not
merely a permissive…" — the negation in "neither is a green clearance gate". The touched
live surfaces carry **no** promotion/canon/clearance/closure language outside negations.

## 4. Instrument notes for the integrator

- The claims ledger's 27 rows do **not** all share the `CL` prefix: the D2 rows are
  `D2-CL01`/`D2-CL02`. A regex keyed on `^(D4-)?CL\d+` finds only 25 rows and mis-reports
  the status census as 15/7/3. Use `(D2-)?(D4-)?CL\d+` (§1 row 10).
- `freeze.txt` is prose, not a `sha256  path` listing; a `while read sha path` loop over it
  produces ten spurious `MISSING` rows. Machine-checkable digests live in `repin.json`
  `R34-D-new-row.digests` and `expected.json`.
- **Sweep unit matters.** The ceilings errata's "hits" column equals its "files" column in
  all five rows (per-line occurrences are 4/2/2/4/7); A01's `canon\w*` counts are per
  **line** (18/9/8/1/2 — exact); A05's `which semantic fields` number is off because of
  this (F5). Every sweep in the assembled audit should name its unit.
- A `--claims-json` extraction must carry `claim_id` **and** `uncertainty{status,basis}`
  (the tool rejects extra keys). An extraction carrying only id/kind/channel/status returns
  exit 1 with 12 `U-FIELD-MISSING` findings — my first pass did this and is not an A01
  defect; the faithful rebuild reproduces A01's exit 0 / claims 12 / findings `[]`.

## Owed

- `reports/round-35/adj/A02-adoption-tool.md`
- `reports/round-35/adj/A03-examples.md`
- `reports/round-35/adj/A04-skill-agents.md`
- `reports/round-35/adj/A08-audit-draft.md`

Owed work: the literal citation-by-citation replay of those four fragments' command lists
(they did not exist at my read time). §1 rows 13-17 already cover A02's and A03's surfaces
and §1 row 18 covers A04's attribution question, so the integrator can complete the replay
by diffing each fragment's cited command and claimed value against §1; any value that
differs is a defect against that slice and inherits the verdicts filed here. A08 is the
assembled audit and consumes F1–F7.

## Citations

Commands (all 2026-10-19 at HEAD `4a7aede`, cwd the lane repo, `TMPDIR=$PWD/.scratch`,
`PYTHONDONTWRITEBYTECODE=1`):

- `sha256sum reports/round-34/handoff/declared-in-r7/*`; `sha256sum reports/round-30/handoff/declared-in-r6/expected.json`
- `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md`; `sha256sum SKILL.md`; `wc -l < SKILL.md`; `git show 139e3b6:SKILL.md | wc -l`
- `sha256sum reports/round-33/adj/contract-read-record.md`; `sha256sum reports/round-30/craft/box1-survey.py`
- `sha256sum tools/exercise-handoff-e2e.py`; `git show da68a6d:tools/exercise-handoff-e2e.py | sha256sum`; `git show 4a7aede:tools/exercise-handoff-e2e.py | sha256sum`
- `git show 139e3b6:corpus/knowledge/synthesis/worldbible-integration-contract.md | sha256sum`
- `git rev-parse HEAD:PROVINCE.md`; `sha256sum PROVINCE.md`; `wc -l -c PROVINCE.md`; `git log --oneline -- PROVINCE.md`; `git log -1 --format='%h %ci %s' -- PROVINCE.md`
- `git log --oneline -- corpus/knowledge/synthesis/worldbible-integration-contract.md`; per-commit `git show <c>:… | sha256sum`
- `git show --stat --name-only da68a6d`; `git show --stat --name-only 4a7aede`; `git show --name-only 4a7aede | grep -v '^reports/'`
- `git show da68a6d -- SKILL.md AGENTS.md examples/`; `git show 4a7aede -- LOG.md`; `git show 139e3b6:AGENTS.md | sed -n '42p'`
- `git diff --stat da68a6d 4a7aede -- tools/exercise-handoff-e2e.py`; `git log --oneline -3 -- tools/exercise-handoff-e2e.py`
- `git ls-tree 4a7aede reports/round-34/run-validation.py`; `git check-ignore -v reports/round-34/handoff/declared-in-r7/run.log`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0
- `python3 -B tools/exercise-handoff-e2e.py --selftest` → exit 0
- isolated copy `git archive HEAD | tar -x -C .scratch/a07-iso` then
  `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` → exit 1, KeyError
- `python3 -B tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md` → exit 0, stdout sha256 `7c581047…`
- `python3 -B tools/harness/packet_uncertainty.py --packet …/twin.json --require-oq --json` → exit 0
- `python3 -B tools/harness/packet_links.py --packet …/twin.json --repo-root . --json` → exit 0
- `python3 -B tools/harness/packet_uncertainty.py --claims-json .scratch/a07-claims12.json --json` → exit 0
- `python3 -B tools/harness/receipt_guard_adoption.py --selftest` → exit 0; `--json` → exit 0
- `python3 -B reports/round-30/craft/box1-survey.py` → exit 0
- `diff <(sed -n '137,150p' reports/round-33/calib/C08-item-08.md) reports/round-33/adj/contract-read-record.md` → rc=1, hunks `6,7c6,7` + `10,14d9`
- `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done`
- `grep -rl -i '<pattern>' corpus/knowledge/` × 5 (errata sweeps) and `grep -rn -i "which semantic fields" corpus/knowledge/` under four variants
- `grep -rn 'SKILL\.md:715\|SKILL\.md:713-715' corpus/lessons/ | wc -l` → 7
- `grep -rl '50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1' .`
- `grep -nE '/home\|expanduser\|os.getenv\(.HOME' tools/harness/receipt_guard_adoption.py`; `grep -nE 'parents\[[3-9]\]|\.\./\.\./\.\.'` over both tools
- `grep -rnE '/home/vgpnk' reports/round-33/ reports/round-34/ tools/harness/receipt_guard_adoption.py`
- `grep -c -i kotodama /home/vgpnk/Projects/shokunin/MANIFEST.json` → 84 (read-only, outside repo)
- `ls -d reports/round-* | wc -l` → 31; `ls tools/gates/*.py | wc -l` → 12; `find corpus/knowledge -maxdepth 1 -mindepth 1 -type d | wc -l` → 6
- `git status --porcelain` → `?? reports/round-35/` only
- inline `python3 -B` parsers: manifest row parse + re-hash (58 rows), `expected.json` `.inputs` compare, claims-row tally, `D4_ROW_RE` application, 12-row claims-json rebuild, inventory-vs-live class diff, box-1 28-row re-hash, negation classification

Paths:

- `reports/round-35/claims.json:54-65`; `reports/round-35/targets.json:254-294`, `:296-301`
- `reports/round-35/adj/A01-r7-packet.md:16,54,60,226,237-243,293,294`; `A05-records.md:149,182,183,283,284,288-304`; `A06-province.md:46,217-228`; `A11-verify-2.md:355-371,406`
- `reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json,freeze.txt,claims-map.md,run.log}`; `reports/round-34/handoff/repin.json`
- `reports/round-34/op/adoption-inventory.json`; `reports/round-34/op/O02-tool-source.md:34,41,68-87`
- `reports/round-34/craft/anchor-reissue.md:6,8-9,15-38`; `reports/round-34/craft/box1-resurvey-durable.json:9,30`
- `reports/round-34/validation.json`; `reports/round-34/run-validation.py:4,238-256,514-517,533`
- `reports/round-30/handoff/declared-in-r6/expected.json`; `reports/round-30/craft/box1-survey.py:4,8,11`
- `reports/round-33/adj/contract-read-record.md:1-9`; `reports/round-33/calib/C08-item-08.md:113,137-153`; `reports/round-33/calib/{C16-receipt.md:69,130,169,K03-open-items.md:69-70,128,C01-item-01.md:247,305}`
- `reports/round-29/defects/regression.md:52`; `reports/round-27/run-validation.py:1388-1389`; `reports/round-28/run-validation.py:1348-1349`
- `tools/exercise-handoff-e2e.py:184,138,1933-1934,2286,2292,3822`; `tools/harness/receipt_guard_adoption.py:58,70,113,447,455,873,899-1013`; `tools/harness/packet_uncertainty.py:26,41-42,124-215`
- `tools/gates/handoff-packet-check.py`; `tools/gates/frozen/handoff-packet-check/{r9-pre,r18-post}/packet.md`
- `corpus/knowledge/synthesis/worldbible-integration-contract.md`; `corpus/knowledge/linguistics/register-lexicon-ceilings.md:291-317`; `corpus/knowledge/linguistics/sound-symbolism.md:106`; `corpus/knowledge/linguistics/register-strata-attestation.md:315,399`
- `corpus/lessons/README.md:242,244`; `corpus/lessons/round-32.md:7,33,41,55,57`; `corpus/lessons/round-2-adjacency.md`
- `examples/culture-d3/{README.md:104,handoff.md:27,74}`; `examples/handoff-packet.sample.md:21`; `examples/handoff-packet.sample.yml:45,78,79`
- `SKILL.md:3,517-518,729-732,732`; `AGENTS.md` (40 at HEAD, 42 at `139e3b6`); `PROVINCE.md:9-11,16-20,22-25`
- `LOG.md` (r34 in-progress entry 28/17/11; r34 ADMITTED entry 29/18/11)
