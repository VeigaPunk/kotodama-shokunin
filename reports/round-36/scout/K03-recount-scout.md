- Seat: K03 | scout | claim Ca | date 2026-10-19 | baseline ce103bf

# K03 — recount scout: inventory of every counting command filed in rounds 33–35

Deliverable for claim **Ca** ("inventory every counting command filed in rounds 33-35
(claims.json counting_commands + validation.json receipts + SCORECARD commands) into a
per-command table"). This fragment is the **scout input** to Ca01/Ca02/Ca03: it
canonicalizes the command set, states where each was filed, and records what a re-run
does. It does not decide the ledger's disposition classes — that is the integrator's
call on Ca03's draft.

All measurements are at HEAD `ce103bf5885af00023cdc4a174c17602476cdcf8`
(`git rev-parse HEAD`, 2026-10-19) with `TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`. **This seat wrote no file outside `reports/round-36/`**: at the
first check `git status --porcelain` → `?? reports/round-36/` only. At the final check the
same command additionally showed ` M reports/round-35/validation.json` — an in-tree filed-byte
incident caused by a **peer** seat's `REFRESH_RECEIPTS=1` invocation, not by this seat;
it is documented with evidence and a recovery command in §4. **No filed round runner was
executed in-tree by this seat** (F-C13-1): every runner invocation below ran either with
`--check` (which by the runners' own docstrings "never writes the receipt",
`reports/round-33/run-validation.py:2`,
`:1449`; `reports/round-34/run-validation.py:5`; `reports/round-35/run-validation.py:5`)
or inside an isolated `git clone` under `.scratch/k03/`. `reports/round-34/handoff/declared-in-r7`
was never `--freeze`d.

## 1. The command set — where counting commands are filed

Four filing surfaces, all read for rounds 33–35:

| surface | path | what it carries |
|---|---|---|
| claim declaration | `reports/round-<N>/claims.json` → `claims[].counting_commands[]` | the declared per-claim counting command |
| acceptance receipt | `reports/round-<N>/validation.json` → `counting_command` + `claims[].command` | the runner command that produced the receipt |
| scorecard | `SCORECARD.md` round tables, "re-run command" column | the published re-run command(s) per axis |
| telemetry | `reports/round-<N>/telemetry/dispatch-declared.json` → `counting_command`; `observed-dispatch.json` → `counting_command` | the dispatch-time and observation-time counting commands |

Counts of filed command strings per surface:

| round | claims.json `counting_commands` entries | validation.json distinct `command` strings | SCORECARD distinct quoted re-run strings | telemetry `counting_command` records |
|---|---|---|---|---|
| 33 | 5 (O×3, C×1, A×1) | 1 (`python3 reports/round-33/run-validation.py`) | 2 (L588 c31 audit; L589/L590 r33 runner) | 2 (declared, observed) |
| 34 | 8 (D×3, O×3, C×2) | 1 (`python3 reports/round-34/run-validation.py`) | 4 (L615 gate + e2e; L616 guard selftest; L617 box1) | 2 |
| 35 | 7 (C×3, O×3, A×1) | 1 (`python3 reports/round-35/run-validation.py`) | 4 (L640 sweep; L641 e2e r6 replay + elided `--profile v3 --selftest`; L642 r35 runner) | 2 |
| **total** | **20 entries** | **3** | **10 quoted strings** | **6** |

Reconciling the 20 declared entries against the distinct-string counts, computed by
normalizing each string (stripping trailing `#` shell comments and r35's trailing
`(expect: exit 1, named diagnostic)` prose annotation) and de-duplicating:

| set | distinct strings |
|---|---|
| `claims.json` `counting_commands` (20 entries) | **15** |
| `SCORECARD.md` quoted re-run strings (10 occurrences) | **10** |
| union of the two | **17** |
| SCORECARD-only (quoted, absent from every `claims.json`) | **2** |

The 20 declared entries collapse to 15 distinct strings because each round's own runner
command is declared once per claim (2× in r33, 3× in r34, 3× in r35 = 8 entries over 3
strings) and r35's r6-replay entry differs from the SCORECARD form only by the prose
annotation. SCORECARD's 10 quoted occurrences reduce to 10 distinct strings of which
**exactly 2 are not declared in any `claims.json`**:

- `python3 -B reports/round-28/readme/sweep.py` (SCORECARD L640, r35 coverage row)
- `--profile v3 --selftest` (SCORECARD L641, r35 operability row — the elided tail of the
  full `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest`)

A third SCORECARD item is **not a quoted string at all**: the bare phrase "partition
census" (SCORECARD L640) names the census loop without reproducing it, so it is a prose
pointer to command #11 rather than an independently re-runnable command.

`validation.json` files also carry four per-claim `command` fields each (`A`/`C`/`O`/`cross`),
all byte-equal to that round's single runner command — 12 redundant entries over 3
distinct strings. The `cross` claim (`X1`/`X4` legs) is present in every receipt even
when `claims.json` declares no cross claim.

## 2. The canonical command table (20 declared entries over 15 distinct strings)

`filed` = the value the round recorded; `observed` = this seat's re-run at `ce103bf`.
"safe" = non-mutating at the current tree.

| # | round | surfaces | command (as filed) | filed result | observed at `ce103bf` | disposition |
|---|---|---|---|---|---|---|
| 1 | 33 | claims O, SCORECARD L588 | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | exit 0; 33 files / 33 rows / 78 queue rows; findings 0 | **identical**: exit 0, `PASS` ×6, `findings: 0`, 33/33/78 | **match** |
| 2 | 33 | claims O | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` | "still green" | exit 0, `SELFTEST OK: 28/28 checks passed` | **match** |
| 3 | 33 | claims O | `test -s reports/round-33/op/O05-falsifier-disposition.md` | disposition landed | exit 0 (file present, non-empty) | **match** |
| 4 | 33 | claims C, A; receipt; SCORECARD L589/L590 | `python3 reports/round-33/run-validation.py` | exit 0; `acceptance_checks_passed: true` | `--check` in isolated clone → **exit 1**, `acceptance_checks_passed: false`; claim A fails on leg `A3`; claim cross `X1` green with the real fleet root present | **mismatch** — one leg, cause named in §3.1 |
| 5 | 34 | claims D | `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md` | exit 0, 16/16, 20 glossary entries, findings 0 | **identical**: exit 0, `INFO scan: fields=16/16 glossary-entries=20 findings=0` | **match** |
| 6 | 34 | claims D, SCORECARD L615 | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0; `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` | **identical**: exit 0, same sha, `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed` | **match** |
| 7 | 34 | claims O, SCORECARD L616 | `python3 tools/harness/receipt_guard_adoption.py --selftest` | selftest green | `selftest_passed: true`, `live_runner_count: 30`, exit 0 | **match** |
| 8 | 34 | claims O | `python3 tools/harness/receipt_guard_adoption.py --json` | `class_counts {guarded-refresh: 18, unguarded-in-place: 11}`, 28 runners | `runner_count 30`, `{guarded-refresh: 19, unguarded-in-place: 11}`, `census_complete true` | **mismatch** — time drift, cause named in §3.2 |
| 9 | 34 | claims C, SCORECARD L617 | `python3 -B reports/round-30/craft/box1-survey.py` | 28/28 at `skill_sha256 f9bd07c2…` | **identical**: `named 28, resolvable 28, unnamed_in_skill []`, `skill_sha256 f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` | **match** |
| 10 | 34 | claims D/O/C | `python3 reports/round-34/run-validation.py` | exit 0; `acceptance_checks_passed: true` | `--check` in isolated clone → exit 0 but **`acceptance_checks_passed: false`**; claim O fails on leg `O2`; every other leaf byte-equal | **mismatch** — same root cause as #8 |
| 11 | 35 | claims C, SCORECARD L640 | `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md \| wc -l; done` | 21/23/24/29/20/94 (total 211) | **identical**: 21/23/24/29/20/94; `ls corpus/knowledge/*/*.md \| wc -l` → 211 | **match** |
| 12 | 35 | claims C | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `totals.files 211` (the r35 receipt's leg records `inventory_files: 211`; the `lines` total is **not** among the values r35 filed) | **identical**: `files: 211`, `lines: 38353` | **match on the filed figure**; the line total 38353 is this seat's own measurement, first recorded here, not a reproduction of a filed r35 value |
| 13 | 35 | claims O, SCORECARD L641 | `python3 -B tools/exercise-handoff-e2e.py --selftest` | selftest green | exit 0, control lines include tamper-baseline/tamper-read-set/tamper-scan/missing-artifact | **match** |
| 14 | 35 | claims O, SCORECARD L641 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | exit 1, `E2E-READSET` naming `reports/round-20/handoff/claims-map.md`, no traceback | **identical**: exit 1, same diagnostic, same named member, no traceback | **match** |
| 15 | 35 | claims O | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` | `v3_controls: 44`; `m13a/m13b/m14a/m14b` present | exit 0; `^  - ` control lines = **44**; m13b/m14a/m14b present | **match** |
| 16 | 35 | claims C, A | `python3 reports/round-35/run-validation.py` | exit 0; `acceptance_checks_passed: true` | `--check` in isolated clone → **exit 0, `acceptance_checks_passed: true`**; only the `manifest` leaf differs (§3.3) | **match** (see §3.3) |
| 17 | 35 | SCORECARD L640 (quoted) | `python3 -B reports/round-28/readme/sweep.py` | "sweep-green (211 rows == 211 files)" | exit 0; `rows 211 files 211`, `footer_ok True`, `readme_sha256 51b966af…` (equal to the value in the r35 receipt's `sweep_tail`) | **match** (SCORECARD-only; not in any `claims.json`) |
| 18 | 35 | SCORECARD L641 (quoted, elided) | `--profile v3 --selftest` (elided form of #15) | 44 controls | same as #15 → 44 | **match** (alias of #15; recorded because the SCORECARD string is not byte-equal to the declared one) |
| 19 | 35 | SCORECARD L640 (unquoted phrase) | "partition census" | 211 | same as #11 | **match** (alias of #11; not a re-runnable string as written) |
| 20 | 34 | SCORECARD L615 (same cell as #5/#6) | the gate + e2e pair, both already rows #5 and #6 | — | — | **match** (aliases of #5/#6; L615 quotes two commands in one cell) |

Additional filed commands not in `counting_commands` but which *are* counting commands
in the AGENTS.md sense (telemetry provenance):

| round | surface | command | filed | observed at `ce103bf` | disposition |
|---|---|---|---|---|---|
| 33 | telemetry `dispatch-declared.counting_command` | `date -u +%FT%TZ; sha256sum reports/round-33/claims.json reports/round-33/targets.json` | `ba69090f…` / `342c8f80…` | **identical** both digests | **match** (the `date` half is non-reproducible by construction) |
| 34 | telemetry `dispatch-declared.counting_command` | `date -u +%FT%TZ; sha256sum …; git rev-parse HEAD` | `f2b87ddb…` / `76d96524…` | **identical** both digests | **match** |
| 35 | telemetry `dispatch-declared.counting_command` | `date -u +%FT%TZ; sha256sum …; python3 -c 'len(…["seats"])'` | `ccfaafc3…` / `56ad0392…`, 64 seats | **identical** digests; `seats: 64` | **match** |
| 33 | telemetry `observed-dispatch.counting_command` | `AgentSwarm result summary …; date -u …` | 64 launched / 64 completed / 0 failed | not re-runnable (live AgentSwarm summary; no persisted raw payload) | **could-not-reproduce** — owner: orchestrator; the durable `observed-dispatch.json` is the surviving record |
| 34 | telemetry `observed-dispatch.counting_command` | `AgentSwarm result summary …` | 63 / 63 / 1 failed | not re-runnable, same reason | **could-not-reproduce** — owner: orchestrator |
| 35 | telemetry `observed-dispatch.counting_command` | `AgentSwarm result summary …; three prior summaries 'failed: 64' with 402` | 64 / 64 / 0 failed, plus 3×64 failed attempts | not re-runnable; the three attempts survive as durable files | **could-not-reproduce** for the summary; **match** for the attempt records (see §4) |

## 3. The three mismatches, with causes

### 3.1 R33 `A3` — tracked-path census constant (the only substantive drift)

Filed `reports/round-33/validation.json` → `claims.A.measurement.legs.A3.measurement`:
`baseline_paths: 2655`, `tracked_paths: 2655`, `unexpected_paths: []`, `status` length 89.
Re-run at HEAD: `baseline_paths: 2655`, **`tracked_paths: 2903`**, `unexpected_paths: []`,
`status` length **0**; the leg raises
`A3: tracked path count differs from 2655 (worktree=2903, baseline=2655)`
(`reports/round-33/run-validation.py:944`).

Cause — **gate design, not a lost artifact.** `A3` pins the *lane-open* census as a
literal (2655 = `git ls-tree -r --name-only 139e3b6 | wc -l`, verified) and requires the
working tree to equal it. The working tree at r33 close was the pre-commit tree, where
the 79 `reports/round-33/**` files were still untracked, so `tracked_paths == 2655`
held *by construction at measure time*. After admission the round's own artifacts become
tracked and the equality can never hold again. The growth is fully accounted for and
contains nothing unexplained:

| revision | tracked paths | delta |
|---|---|---|
| `139e3b6` (r33 baseline) | 2655 | — |
| `da68a6d` (r33 admitted) | 2735 | +80 |
| `4a7aede` (r34 admitted) | 2815 | +80 |
| `ce103bf` (r35 admitted) | 2903 | +88 |

Composition of the 248 added paths between `139e3b6` and `ce103bf`, by directory
(`git ls-tree` diff): `reports/round-33` +79, `reports/round-34` +79, `reports/round-35` +78,
`corpus/knowledge` +10 (the r35 claim-C entries), `REGIMEN.md` +1, `tools/harness` +1
(the r34 claim-O instrument); **0 removed**. So the leg's own `unexpected_paths: []`
check — the one that actually guards against out-of-scope writes — still passes; only
the frozen literal fails.

**Consequence for claim Ca's disposition:** this is a *self-invalidating gate*, the
same class as R34-N1/r21's mtime drift but structural rather than incidental. It is not
evidence that r33's scope watch was wrong at the time it ran (the filed receipt's
`status` list of 89 entries — 79 untracked `reports/round-33/**` paths (all 79 of the
`reports/` entries are under `reports/round-33/`) plus 10 modified shared paths
(`AGENTS.md`, `LOG.md`, `SKILL.md`, `REGIMEN.md`, `corpus/lessons/README.md`,
`corpus/knowledge/linguistics/register-lexicon-ceilings.md`, `examples/culture-d3/README.md`,
`examples/culture-d3/handoff.md`, `examples/handoff-packet.sample.md`,
`examples/handoff-packet.sample.yml`) — is the contemporaneous record and is not
reproducible from a post-admission tree). Worth routing as a finding to Ca03: the A3
leg should either pin the baseline census and assert *scope containment of the delta*
(as its `unexpected_paths` half already does) rather than equality, or accept a declared
round-artifact allowance.

### 3.2 R34 `O2` — runner census and adoption classes (time drift)

Filed: `28` runners, `{guarded-refresh: 18, unguarded-in-place: 11}`.
Observed: `30` runners, `{guarded-refresh: 19, unguarded-in-place: 11}`;
leg failure `O2: inventory counts differ: 30 runners, {'guarded-refresh': 19, 'unguarded-in-place': 11}`
(`reports/round-34/run-validation.py:211`).

Cause — **the tree gained runners after the round that counted them.** `ls reports/round-*/run-validation.py | wc -l`
→ **30** at HEAD; the 30 are `round-5..12, 14..35` (no r13). Rounds 33, 34 and 35 each
added a runner; r33's runner existed at r34 measure time, so the count moved 28 → 30 over
two rounds. All three new runners are classified `guarded-refresh`
(`receipt_guard_adoption.py --json`, `runners[27..29]` → rounds 33/34/35), which explains
`guarded-refresh` 18 → 19 rather than 18 → 21: the filed r34 receipt already counted the
r34 runner itself (its own `O2` leg asserts "this round's own runner not classified
guarded-refresh" → failure, `:217`), so r34 contributed 0 net to `guarded-refresh` and
r35 contributed +1. `unguarded-in-place` is unchanged at 11 — the r34 claim-O
instrument's finding that the hazard set is fixed and historical still holds.

This is the same class as the r21 recount's "R20 links 102 vs 105" and "mtime tie-break"
dispositions: a *revision boundary*, not a wrong number at filing time. Not a defect in
r34's evidence; the leg is simply non-hermetic under tree growth.

### 3.3 R34/R35 `manifest` leaf — the owed close-time input has since landed

Filed (both rounds), `claims.cross.measurement.legs.X1-X3.measurement.manifest`:
`"pending-by-construction: integrator files the MANIFEST row in the same close pass as this receipt"`.
Re-run: the leaf is **absent** — the leg now takes its other branch, because
`/home/vgpnk/Projects/shokunin/MANIFEST.json` (`reports/round-34/run-validation.py:22`,
`reports/round-35/run-validation.py:21`) now contains `rounds[]` entries for 33, 34 **and**
35. The runners' own `limits` say exactly this: "Fleet report, MANIFEST row,
observed-dispatch and the closing snapshot are close-time inputs; `--check` never creates
them."

Disposition: **match, expected direction.** The filed string was true at filing time and
became obsolete the moment the integrator landed the row; the *leg status stays green*
in both rounds. This is a normal lifecycle of a pending-by-construction leaf, not drift.
The same applies to `r35`'s `closing` leaf.

### 3.4 `R33 X1` — environment artifact, not a defect (recorded so it is not mistaken for one)

In a bare `git archive`/`git clone` of the lane repo, r33's `--check` reports three extra
failures on claim `cross`/leg `X1` (raising the total from one to four):
`fleet report lacks required headings: ['Before → after measurements', 'Landed changes', 'SHONEN', 'Work performed']`,
`fleet report has no ISO date`, `fleet report does not cite the round-33 runner`.
Cause: `reports/round-33/run-validation.py:24` sets `FLEET_ROOT = ROOT.parent` and reads
`.ufo/reports/round-33/kotodama.md` — which lives at the **fleet root**, i.e.
`/home/vgpnk/Projects/shokunin/.ufo/`, outside the lane repo (the repo's own `AGENTS.md`
scope; commit `139e3b6` is literally "fleet report belongs at the fleet root (.ufo/), not
the lane repo"). A clone of the lane repo alone has no fleet root.

Verified: with the real fleet report copied in at the fleet root position (byte-identical,
`sha256 254092071f2e75fc1dbcf31fbbd07544bdc7835995cfd375d7d08661c88518a7`, matching the
filed receipt's `input_sha256["fleet:.ufo/reports/round-33/kotodama.md"]`), r33's `X1`
leg goes green and the **only** remaining failure is `A3` (§3.1). The real fleet report
does carry all four headings (`kotodama.md:13` Work performed, `:55` Landed changes,
`:87` Before → after measurements, `:117` SHONEN) and the date `2026-10-19` in its title
line (`:1`). So `X1` is green in-tree and the artifact is clone-only.

## 4. IN-TREE FILED-BYTE INCIDENT observed during this recount (F-C13-1 class)

**A filed receipt was modified in-tree while this recount was running.** This is not my
write, and it is a recurrence of the round-33 F-C13-1 incident class
(`LOG.md:3548` "filed receipts written in-tree during round 33 (restored; record owed,
now filed)").

Observed state at 2026-10-19T09:34Z:

| path | working tree vs HEAD | sha256 |
|---|---|---|
| `reports/round-35/validation.json` | **content differs** (`git diff --numstat` = `2 4`) | live `8a40245dcecff27b…`, HEAD/filed `328e97b39eff69f4…` |
| `reports/round-34/validation.json` | content **identical**, mtime touched (06:32:16Z local) | `ba2fa4dcf8f29a13…` (== HEAD) |
| `reports/round-33/validation.json` | clean | `93b28f3635cc1176…` (== HEAD) |

The r35 delta is exactly two hunks: `claims.cross.measurement.legs.X1-X3.measurement`
went from `{"manifest": "pending-by-construction: …"}` to `{}`, and `measured_at_utc`
moved `06:19:14.685566-03:00` → `06:33:23.601283-03:00`. That is the signature of the
r35 runner **publishing** its receipt (it writes `measured_at_utc: now()` and re-derives
the `manifest` leaf, which is now empty because the MANIFEST row has since landed).

Cause, evidenced from the live process table (not inferred): a **peer seat's command ran
the filed runner in-tree with the guard deliberately bypassed**. Two processes were
observed mid-run:

```
PID 1111207 (06:33:44) / PID 1115469 (06:33:59), cwd = .scratch/x01-clone:
  export REFRESH_RECEIPTS=1 TMPDIR=… ; for r in 33 34 35; do git checkout -q -- reports/round-$r/validation.json; done
  for r in 33 34 35; do python3 -B reports/round-$r/run-validation.py …
```

That shell does `cd …/.scratch/x01-clone` — but `.scratch/x01-clone` is **not the lane
repo**, so its relative `git checkout`/`python3` invocations operate on whatever tree its
`.git`/working directory actually resolves to, and `REFRESH_RECEIPTS=1` is precisely the
environment value `tools/harness/receipt_guard.py:7` names as the *only* thing that
"permits a committed receipt write". A separate peer process (PID 1121261, 06:34:18) used
`unshare -rm` + `mount --bind .scratch/ca03/r35w …` to run the same runner with `--check`
inside a bind-mounted private copy — which is the **correct** isolated pattern. The
in-tree write is attributable to the `REFRESH_RECEIPTS=1` invocation, not to `--check`.

**Recovery (this seat's obligation, per AGENTS.md close-what-you-open and the F-C13-1
precedent):** the filed bytes are fully recoverable and two independent byte-identical
survivors exist, both matching the SCORECARD-filed `328e97b3…`:

- `git cat-file blob HEAD:reports/round-35/validation.json` → `328e97b39eff69f4…`
- `.scratch/x01-clone/reports/round-35/validation.json` → `328e97b39eff69f4…`
- `.scratch/ca03/r35w/reports/round-35/validation.json` → `328e97b39eff69f4…`

`git checkout -- reports/round-35/validation.json` restores the filed bytes exactly. **This
scout does not perform that restore**: writing inside `reports/round-1..35/**` is outside
my `out` path, and a filed-byte repair is the integrator's act. It is recorded here as a
**routed incident** with the exact recovery command, the pinned target digest, and the
culprit command line, so the integrator can restore and file the F-C13-1-class record.

Note for claim Ca's dispositions: the r35 `manifest` leaf that my §3.3 treats as
"expected-direction" is visible in this same live diff — the live file shows the leaf
already emptied by a fresh publish, confirming the mechanism named in §3.3 rather than
contradicting it.

## 5. Round 36's own availability record (cross-checked while counting)

`reports/round-36/telemetry/availability-attempt-1.json` — hyper / deepseek-v4.1-flash,
32 requested, 0 launched, 32 failed, `402 You're out of credits (hyper.charm.land)`,
agents `agent-386..agent-417`, disposition = declared devin fallback. Cross-checked
against `REGIMEN.md:14` ("hyper / deepseek-v4.1-flash; fallback devin/deepseek-v4-1-flash-high")
and `:73-76` (apply the declared fallback once). **Consistent with the regimen; the
fallback is declared, not improvised.** Not re-runnable (no persisted provider payload);
the durable record is the file.

For the r35 attempt comparison (a precedent this round's record follows):
`availability-attempt-{1,2,3}.json` each name a distinct key (opencode-go-3/4/5), 64
requested, 0 launched, 64 failed, identical 402 class, with `key_census_so_far` naming
keys 1/2 LIVE and 3/4/5 dry — and `observed-dispatch.json` records the reuse of key 1 as
a named deviation. The r36 attempt-1 record carries the same shape (0 launched, all
failed, one named failure class, a disposition citing the regimen clause).

## 6. What this inventory changes for claim Ca

- The **command set is 23 distinct commands**: 17 command strings (the union of the 15
  distinct `claims.json` strings and the 10 distinct SCORECARD strings, which overlap in
  8 places; 2 SCORECARD strings are not declared anywhere), plus 3 telemetry dispatch
  commands and 3 telemetry observation commands. The 20 declared entries and the 10
  SCORECARD occurrences are all accounted for against those 17.
- **17 of the 23 reproduce or match** at `ce103bf`: 14 of the 17 command strings (13 direct
  + 1 alias), plus all 3 dispatch `sha256sum` commands. **3 mismatch**, and every one has a named
  cause: one gate-design constant (§3.1), one time-drift count (§3.2), one
  pending-by-construction leaf whose input has landed (§3.3). **None is a fabricated or
  lost figure**, and none should be smoothed into a "match". The remaining 3 are the
  observation commands below.
- **3 observation commands are `could-not-reproduce`** (no persisted AgentSwarm payload;
  AGENTS.md forbids persisting private prompt payloads) — owner: orchestrator, durable
  record: the corresponding `observed-dispatch.json`.
- Reconciling the totals: 14 match + 3 mismatch = the 17 command strings; + 3 dispatch
  `sha256sum` matches = 20; + 3 `could-not-reproduce` observation commands = 23.
- No `counting_command` re-run **by this seat** wrote any byte: all runner invocations used
  `--check` (non-publishing by construction) in an isolated clone; all other commands are
  read-only (`ls`, `wc`, `sha256sum`, `--json`, `--selftest`, `test -s`, `git ls-tree`).
  A direct publish attempt inside a clone is **refused by design** —
  `receipt_guard: refusing overwrite path=reports/round-3{4,5}/validation.json
  committed_sha=ce103bf…; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]`,
  exit 3 — which is the r34 claim-O instrument working as filed. The one in-tree write that
  *did* occur was a peer's `REFRESH_RECEIPTS=1` bypass (§4), which is exactly the guard's
  documented escape hatch being used in-tree.
- **Caution for Ca04's independent re-run sample:** any re-run must use `--check` or a
  private bind-mount, never bare `python3 reports/round-N/run-validation.py` in-tree. With
  `REFRESH_RECEIPTS=1` set — and `unset` is not the default in every seat's environment —
  the runner publishes and overwrites a filed receipt.

## Owed

- **ROUTED INCIDENT — filed byte modified in-tree (§4).** `reports/round-35/validation.json`
  differs from HEAD (`8a40245d…` vs filed `328e97b3…`). This seat did not write it and did
  not restore it. **Integrator action owed:** `git checkout -- reports/round-35/validation.json`
  (verified to restore the filed `328e97b39eff69f4…`, which equals the SCORECARD-filed
  `328e97b3…` and the HEAD blob `11f241a4`), then file the F-C13-1-class incident record
  naming the `REFRESH_RECEIPTS=1` in-tree invocation as the cause. Pinned target digest:
  `sha256 328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124`.
  Surviving byte-identical sources: `git cat-file blob HEAD:reports/round-35/validation.json`,
  `.scratch/x01-clone/reports/round-35/validation.json`,
  `.scratch/ca03/r35w/reports/round-35/validation.json`.
- **`reports/round-36/calib/Ca03-ledger-draft.md` (Ca03) consumes this table.** This seat
  files the command inventory and observed values; Ca03 owns the ledger JSON's
  `disposition` vocabulary and Ca04 owns the 25 % independent re-run sample. Not owed by
  this seat, but Ca03 must not treat §3.1's `A3` as a "match" — it is a *dispositioned
  mismatch* with a structural cause.
- **The `A3` gate-design finding** (frozen lane-open census literal vs. post-admission
  tree) is a candidate routed finding for the integrator's SCORECARD/defects record. This
  scout files it here rather than absorbing it; no tool byte was changed.
- Nothing else owed. `reports/round-36/` at scout time held only `claims.json`,
  `targets.json` and `telemetry/` — no sibling fragment existed to read, so §2 is built
  from the filed rounds 33–35 bytes and live re-runs, not from a peer seat.

## Citations

Commands (all run 2026-10-19 from the lane root, `TMPDIR=$PWD/.scratch`,
`PYTHONDONTWRITEBYTECODE=1`, HEAD `ce103bf5885af00023cdc4a174c17602476cdcf8`):

- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 0; `lesson files: 33`, `index rows: 33`, `queue rows: 78`, `findings: 0`, six `PASS` lines
- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` → exit 0, `SELFTEST OK: 28/28 checks passed`
- `test -s reports/round-33/op/O05-falsifier-disposition.md` → exit 0
- `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md` → exit 0, `INFO scan: fields=16/16 glossary-entries=20 findings=0`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0, `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` → exit 1, `E2E-READSET: … reports/round-20/handoff/claims-map.md`
- `python3 -B tools/exercise-handoff-e2e.py --selftest` → exit 0; `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` → exit 0, 44 `^  - ` control lines
- `python3 tools/harness/receipt_guard_adoption.py --selftest` → `selftest_passed: true`; `--json` → `runner_count 30`, `class_counts {guarded-refresh: 19, unguarded-in-place: 11}`
- `python3 -B reports/round-30/craft/box1-survey.py` → `named 28, resolvable 28, skill_sha256 f9bd07c2…`
- `python3 -B reports/round-28/readme/sweep.py` → exit 0, `rows 211 files 211`, `footer_ok True`, `readme_sha256 51b966af…`
- `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → `totals.files 211`, `totals.lines 38353`
- `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → 21/23/24/29/20/94; `ls corpus/knowledge/*/*.md | wc -l` → 211
- `sha256sum reports/round-{33,34,35}/{claims,targets}.json` → `ba69090f…`/`342c8f80…`, `f2b87ddb…`/`76d96524…`, `ccfaafc3…`/`56ad0392…` (all equal the telemetry `durable_sources` pins)
- `python3 -c 'len(json.load(open("reports/round-N/targets.json"))["seats"])'` → r33 64, r34 63, r35 64, r36 32
- `sha256sum reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,claims-map.md,expected.json,freeze.txt}` → all five equal `reports/round-35/run-validation.py`'s `R7_PINS`
- `git diff 4a7aede22cd8395b01ce6dd9f46bcae364ca24e4 -- tools/exercise-handoff-e2e.py | wc -l` → 126 (filed r35 `renderer_diff_lines: 126`)
- `git ls-tree -r --name-only <rev> | wc -l` → 139e3b6 2655, da68a6d 2735, 4a7aede 2815, ce103bf 2903
- `git ls-tree` set-diff 139e3b6→ce103bf → +248 / −0; by directory: round-33 +79, round-34 +79, round-35 +78, corpus/knowledge +10, REGIMEN.md +1, tools/harness +1
- isolated recount: `git clone --no-hardlinks . .scratch/k03/clone` then
  `python3 -B reports/round-N/run-validation.py --check` for N=33/34/35 →
  r33 exit 1 (`A3`), r34 exit 0 with `acceptance_checks_passed: false` (`O2`), r35 exit 0 with `true`
- guard refusal (recorded, not worked around): in the clone, running the r34/r35 runners
  without `--check` → exit 3, `RECEIPT-GUARD-COMMITTED`; in the `git archive` copy → exit 3,
  `RECEIPT-GUARD-GIT` (no `.git` in the archive)
- `sha256sum ../.ufo/reports/round-33/kotodama.md` → `254092071f2e75fc1dbcf31fbbd07544bdc7835995cfd375d7d08661c88518a7` (== filed `input_sha256["fleet:.ufo/reports/round-33/kotodama.md"]`)
- `git status --porcelain` → `?? reports/round-36/` **plus ` M reports/round-35/validation.json`** (the in-tree incident of §4 — present at the final check, attributable to a peer's `REFRESH_RECEIPTS=1` invocation, not to this seat; `reports/round-34/validation.json` was mtime-touched with identical content; r33 clean)
- incident evidence: `ps -eo pid,etimes,lstart,cmd` → PIDs 1111207/1115469 (cwd `.scratch/x01-clone`, `export REFRESH_RECEIPTS=1 … for r in 33 34 35; do python3 -B reports/round-$r/run-validation.py`), PID 1121261 (`unshare -rm` + `mount --bind .scratch/ca03/r35w` + `--check`, the correct isolated pattern)
- `git diff --numstat HEAD -- reports/round-35/validation.json` → `2 4`; `git diff HEAD -- reports/round-35/validation.json` → the `X1-X3.measurement.manifest` leaf emptied and `measured_at_utc` 06:19:14→06:33:23
- `git cat-file blob HEAD:reports/round-35/validation.json | sha256sum` → `328e97b39eff69f4…` (== SCORECARD-filed `328e97b3…` == `.scratch/x01-clone/…` == `.scratch/ca03/r35w/…`)
- `git diff --quiet HEAD -- reports/round-34/validation.json` → identical content (mtime-only touch at 06:32:16 local)

Repo files:

- `reports/round-33/claims.json` (claims O/C/A `counting_commands`); `reports/round-33/validation.json` (`A3` measurement, `input_sha256`)
- `reports/round-34/claims.json`; `reports/round-34/validation.json` (`O` leg `O1-O5`, `class_counts`, `missing_dependencies`)
- `reports/round-35/claims.json`; `reports/round-35/validation.json` (`O` leg `O1-O7`: `v3_controls 44`, `quiet_sha`, `renderer_diff_lines 126`)
- `reports/round-33/run-validation.py:2,24,938,944,1028-1032,1449`; `reports/round-34/run-validation.py:5,22,199,202,211,217,323,325,401,522-526`; `reports/round-35/run-validation.py:5,21,139,201-206,329-331,424,492-496`
- `tools/harness/receipt_guard.py:7,35,57-64,140-146` (the `REFRESH_RECEIPTS=1` / `RECEIPT-GUARD-COMMITTED` contract)
- `reports/round-34/op/adoption-inventory.json` (`class_counts`, `declared_hazards`, `runners[27..29]`)
- `reports/round-34/handoff/declared-in-r7/freeze.txt` (packet/twin/claims-map pins + read set 58 files)
- `reports/round-3{3,4,5}/telemetry/{dispatch-declared,observed-dispatch}.json`; `reports/round-35/telemetry/availability-attempt-{1,2,3}.json`
- `reports/round-36/telemetry/{dispatch-declared,availability-attempt-1}.json`
- `SCORECARD.md:582-591, 610-618, 635-643` (round tables; re-run command column)
- `REGIMEN.md:13-14, 73-76` (position-4 provider and the fallback clause)
- `../.ufo/reports/round-33/kotodama.md:1,13,55,87,117` (fleet report; fleet root, read-only)
- `/home/vgpnk/Projects/shokunin/MANIFEST.json` (`rounds[]` now carries 33/34/35)
- `reports/round-21/recount/{ledger.json,dispositions.md,audit.md}` (the recount precedent: disposition vocabulary, `could-not-reproduce` handling, time-drift and environmental classes)
