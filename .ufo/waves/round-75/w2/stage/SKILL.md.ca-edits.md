# SKILL.md — claim Ca staged edits (round 75, wave 2)

Seat `ScribeSkillFinal`. Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; base
`f556d1049fe651d3d63975600b13acd9fb686f15`. Worktree HEAD is that same revision; `git status --porcelain`
shows uncommitted `M SHONEN.md`, `M SKILL.md`, `M reports/round-28/readme/sweep.py` plus untracked
`.ufo/waves/round-75/` and `reports/round-75/` — all ignored here and never graded. **Nothing in this file
was applied.** This seat did not write SKILL.md.

Claim Ca `fixed_surfaces` (`reports/round-75/claims.json`, 22398 B, mtime 15:09, still `frozen: null`) puts two
obligations on SKILL.md-adjacent files:

1. `{"path": "SKILL.md", "line": 701, "required": "this is narrative evidence, not a standalone committed receipt"}`
2. `{"path": "reports/round-75/telemetry/selftest-r72-repeat.txt", "required": "SELFTEST: 10/11"}`

## 0. How the counter enforces them (verified in the installed counter source)

Counter `accept-ca.py` (lane copy `.ufo/waves/round-75/counters/accept-ca.py`, 151903 B, sha256
`d167093537864fc9572fedec2ee8cd0f8e1f86c7c6daa380e81bfde893975bdb`):

| mechanism | counter location | what it checks |
|---|---|---|
| `REPAIR` leg, fixed-surface loop | lines 1545-1554 | for every `fixed_surfaces` item with string `path` and string `required`: read `git show <lands>:<path>`, cut to `line` when an int is given, fail the leg unless `required` is a **substring** of it (or of the whole file when no `line`). No sha256, no byte comparison. |
| `APPENDONLY` leg, exemption list | lines 1718-1722 | a fixed surface carrying an int `line` is added to the allowed changed lines for that path, so rewriting SKILL.md:701 is not a removed line. Claim Ca `legs[4]` names "the exact SKILL.md:701 correction declared in fixed_surfaces" as that exemption. |

Neither surface freezes a `sha256`, so the wording beyond the required sentence is free; the wording below is
the minimal one. The line-701 check uses the **literal** line number at `<lands>`: it holds only while no
landing inserts a line above 701 in SKILL.md (claim C does not edit SKILL.md).

## (a) In-place correction of SKILL.md line 701

Base line 701 (891 characters, 8 cells, 9 `|`) is the `accept-c-72` gate row. Its self-test cell calls the
SCORECARD narrative block a *receipt*: `... got exit=1`; receipt: SCORECARD.md `## Corrections — round 73`)`.
`## Corrections — round 73` is a section of a larger prose file, not a standalone committed receipt — the word
is wrong, and claim Ca requires the correction.

**OLD — base `f556d10…:SKILL.md` line 701, verbatim:**

<!-- OLD-701 -->
| accept-c-72 | gate | `python3 -B reports/round-72/accept-c.py --root . --lands <40-hex> [--fleet-root <fleet>]` | Output ends `ACCEPT-C-72: PASS` or `: FAIL legs=10/10` — the denominator is a literal, so a FAIL receipt still reads `legs=10/10`; 0 pass / 1 fail; 2 on missing or non-40-hex `--lands`, or when `--root` has no `.git`; a missing `<fleet>/scripts/sources-census.sh` is an uncaught FileNotFoundError (exit 1, no verdict line). | `python3 -B reports/round-72/accept-c.py --selftest` — measured `SELFTEST: 10/11`, exit 1 at HEAD (`--- clean fixture: expected PASS 10/10, got exit=1`; receipt: SCORECARD.md `## Corrections — round 73`) | base `b60c7b14…`, ids S874/S875, both entry paths, scratch-mirror receipt path, ten mutants pinned in script | read-only against `--lands` via `git show`; selftest builds `tempfile.mkdtemp` fixtures and leaves them behind | kotodama-shokunin |
<!-- /OLD-701 -->

**NEW — line 701 to write (959 characters; sha256 of the line plus one `\n` is
`f6d41163fc2e1a2cd4d64db0cc318b54fc07fcd64fbc541df95f086449d8800a`):**

<!-- NEW-701 -->
| accept-c-72 | gate | `python3 -B reports/round-72/accept-c.py --root . --lands <40-hex> [--fleet-root <fleet>]` | Output ends `ACCEPT-C-72: PASS` or `: FAIL legs=10/10` — the denominator is a literal, so a FAIL receipt still reads `legs=10/10`; 0 pass / 1 fail; 2 on missing or non-40-hex `--lands`, or when `--root` has no `.git`; a missing `<fleet>/scripts/sources-census.sh` is an uncaught FileNotFoundError (exit 1, no verdict line). | `python3 -B reports/round-72/accept-c.py --selftest` — measured `SELFTEST: 10/11`, exit 1 at HEAD (`--- clean fixture: expected PASS 10/10, got exit=1`; recorded in SCORECARD.md `## Corrections — round 73` — this is narrative evidence, not a standalone committed receipt) | base `b60c7b14…`, ids S874/S875, both entry paths, scratch-mirror receipt path, ten mutants pinned in script | read-only against `--lands` via `git show`; selftest builds `tempfile.mkdtemp` fixtures and leaves them behind | kotodama-shokunin |
<!-- /NEW-701 -->

Exactly one substring changed, inside the self-test cell:

- old: ``` `--- clean fixture: expected PASS 10/10, got exit=1`; receipt: SCORECARD.md `## Corrections — round 73`) ```
- new: ``` `--- clean fixture: expected PASS 10/10, got exit=1`; recorded in SCORECARD.md `## Corrections — round 73` — this is narrative evidence, not a standalone committed receipt) ```

Every other byte of the row is identical (entry command, verdict map, pinned values, write scope, owner).
Cell count is 8 before and after; no cell gains a `|`. The required sentence appears verbatim, so the
REPAIR leg's containment check is satisfied by construction.

**Do not copy the worktree line.** The uncommitted `M SKILL.md` diff already rewrites this same line to
"*a round-73 execution was recorded as a measured side finding in SCORECARD.md `## Corrections — round 73`
and corpus/lessons/round-73.md R73-M4: …*". That text is not base bytes, is not graded, and is longer than the
minimal correction. The staged line above is computed from `git show f556d10…:SKILL.md`, not from it.

## (b) Gate rows to append

Placement: **after base line 706 (`accept-ca-74`) and before base line 707** (the
`accept-c-73 / accept-ca-73 correction` `note` row) — registry rows stay in round order, `note` rows trail,
which is how round 74's rows were added. Column shape is line 706's: 8 cells, 9 `|`; no cell below contains a `|`.

| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|---|
| accept-ca-75 | gate | `python3 -B reports/round-75/accept-ca.py --root . --lands <40-hex> --freeze <40-hex> --fleet-root /home/vgpnk/Projects/shokunin` (COMBINED needs `--combined <40-hex>`; `--main` defaults to `main`) | Output ends `ACCEPT-CA-75: PASS legs=12/12` (exit 0) or `: FAIL legs=<n>/12` (exit 1, n = passing legs), after one `LEG PASS` or `LEG FAIL` line per leg. A refusal prints `ACCEPT-CA-75: FAIL legs=0/12 (refused: …)` and exits 2: a frozen leg table that is not exactly the twelve implemented legs (LEGCOUNT), `--lands` equal to the frozen claims base, or `freeze == lands` with every leg green. Input errors print `ERROR: …` on stderr, no verdict line, exit 2: missing `--lands`, `--freeze` or `--fleet-root`; a non-40-hex `--lands`, `--freeze` or `--combined`; a `--fleet-root` that is not a directory; an absent `--lands`, `--freeze` or `--combined` commit; an unreadable frozen `claims.json`; a frozen base that is not a commit. A `--freeze` off the lands first-parent chain is graded, not refused: FROZENCFG reads FAIL, exit 1. Without `--combined` the COMBINED leg fails on `the explicit --combined revision is required`, exit 1. | `python3 -B reports/round-75/accept-ca.py --selftest` — the green form prints `SELFTEST OK: <n> checks across <m> scenarios reported-fail=0: <labels>` and exits 0. Measured 2026-10-27 at counter sha256 `d1670935…`: exit 1, no `SELFTEST OK:` line, seven `SELFTEST FAIL:` lines (`clean exit`, `clean RECEIPTS`, `clean text`, `annotate-other-token NOSTUB`, `r1-rule2-exempt exit`, `r1-rule2-exempt text`, `repair-no-statement LEDGER`) — the counter's own fixture landing does not yet satisfy RECEIPTS. | frozen pair floor 10; nine-executable observe allowlist git, grep, wc, sha256sum, ls, cat, head, tail, cut; claims and ledger read at `--freeze` only; round-74 lands `5e4796c0…` with freeze `00c408a0…` for RECEIPTS | read-only — `git show` plus `git archive`/clone materialized under a scratch tempdir; `observe_cmd` argv only, never a shell | kotodama-shokunin |
| accept-c-75 | gate | `python3 -B reports/round-75/accept-c.py --root . --lands <40-hex> --freeze <40-hex> [--fleet-root /home/vgpnk/Projects/shokunin]` | **DECLARED GRAMMAR ONLY — NOT MEASURED; DO NOT LAND AS-IS.** The counter docstring declares `ACCEPT-C-75: PASS legs=13/13` (exit 0) or `ACCEPT-C-75: … legs=<n>/<n>`, refusals `ACCEPT-C-75: FAIL legs=0/13 (refused: …)` exit 2, and `ERROR:` plus exit 2 on input error. The staged bytes (`.ufo/waves/round-75/counters/accept-c.py`, sha256 `5e65ba73…`, 511 lines) end at the marker `# --- PART B ---` and implement no argument parser, no leg and no driver: both the graded form and `--selftest` exit 0 printing nothing, so no verdict line exists today. | `python3 -B reports/round-75/accept-c.py --selftest` — no `--selftest` branch exists in the staged bytes: exit 0, no output. The docstring promises one git init plus base/freeze/lands commits per mutant. | frozen claim C leg set (13: ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK, FROZENCFG, INDEX); constants read at `--freeze`; `lands == base` refused | declared read-only: clone plus `git archive` into scratch | kotodama-shokunin |

### accept-ca-75 — sentence-by-sentence verification

| claim | verified at |
|---|---|
| CLI flags and defaults (`--root .`, `--lands`, `--freeze`, `--fleet-root`, `--main main`, `--combined`, `--selftest`) | `accept-ca.py:3354-3363` |
| `LEG PASS <name>` / `LEG FAIL <name>` plus an indented detail line per leg | `accept-ca.py:280-285` |
| `ACCEPT-CA-75: PASS legs=12/12` / `: FAIL legs=<n>/12`, exit 0/1 | `accept-ca.py:2561-2569` |
| refusal line `ACCEPT-CA-75: FAIL legs=0/12 (refused: …)`, exit 2 | `accept-ca.py:2430-2432` (printer), 2564-2565 (freeze == lands green), 2467-2468 (LEGCOUNT), 2476-2477 (lands == base) |
| LEGCOUNT = frozen leg table must equal the twelve implemented names | `accept-ca.py:203-205` (names), 2465-2468 (refusal) |
| missing `--lands`/`--freeze`/`--fleet-root` → `ERROR: …`, exit 2 | `accept-ca.py:3366-3369` |
| non-40-hex `--lands`/`--freeze`/`--combined` → exit 2 | `accept-ca.py:3372-3378` |
| `--fleet-root` not a directory → exit 2 | `accept-ca.py:3380-3382` |
| absent `--lands`/`--freeze`/`--combined` commit → `ERROR: … is not a commit in <root>`, exit 2 | `accept-ca.py:2446-2457` |
| unreadable frozen `claims.json` → `ERROR: claims file … is not committed at --freeze`, exit 2 | `accept-ca.py:584-594`, 2459-2462 |
| frozen base not a commit → exit 2 | `accept-ca.py:2472-2474` |
| `--freeze` off the lands first-parent chain → FROZENCFG FAIL, not a refusal | `accept-ca.py:2351-2355`; measured: selftest scenario `freeze-off-first-parent` → exit 1, `LEG FAIL FROZENCFG` |
| no `--combined` → COMBINED FAIL with `the explicit --combined revision is required`, exit 1 | `accept-ca.py:2311-2313` |
| pair floor 10, nine-entry observe allowlist, round-74 lands/freeze, receipt `ACCEPT-CA-74: PASS legs=11/11` | `accept-ca.py:183-199` (constants) |
| read-only, scratch materialization | `accept-ca.py:2479` (`tempfile.mkdtemp(prefix="r75-ca-")`), observe allowlist excludes interpreters and shell metacharacters (`accept-ca.py:1017-1055`) |
| selftest red with seven failing checks | measured run: `TMPDIR=<scratch> python3 -B .ufo/waves/round-75/counters/accept-c.py --selftest` → exit 1, 51 output lines, 34 `selftest:` blocks, 7 distinct `SELFTEST FAIL:` lines, no `SELFTEST OK:` line (full transcript in this seat's report) |

### accept-c-75 — why the row is provisional (measured)

- File: `.ufo/waves/round-75/counters/accept-c.py`, 20043 B, sha256
  `5e65ba73e88c422980f2bab1b78ee612540cd424c3d4a98af9969d9547bddc8a`, 511 lines, last line `# --- PART B ---`.
- `python3 -B .ufo/waves/round-75/counters/accept-c.py --selftest` → exit 0, stdout empty, stderr empty.
- `python3 -B .ufo/waves/round-75/counters/accept-c.py --root . --lands f556d10… --freeze f556d10…` → exit 0,
  empty output.
- No `def main`, no `argparse`, no `REQUIRED_LEGS`, no leg implementation exists in the file (grep).
- `reports/round-75/accept-c.py` does not exist yet (`reports/round-75/` holds only `claims.json`,
  `ledger.json`, `telemetry/`), so the entry path in the row is prospective.
- Drift to settle at the freeze: the counter docstring says "eight adopted rows (S885..S892), two entries";
  the claims now name nine rows (S885..S893) and three entries. The counter reads its constants from the
  frozen claims (`claims[id=C]…`), so the docstring is prose, but the frozen `legs[]` must still equal the
  implemented table or LEGCOUNT refuses.

**Landing rule for the L1:** land `accept-c-75` only after `reports/round-75/accept-c.py` implements its
driver; then replace the verdict and self-test cells with a re-measurement. Landing the row against the
current bytes would state a verdict line the file cannot print — the round-74 `accept-ca-74` row failure
class (a pinned sha256 and scenario count that existed nowhere).

**Arithmetic the landing must keep:** two new `gate` rows naming `reports/round-75/accept-c.py` and
`reports/round-75/accept-ca.py`, landed together with both counter files, move the registry invariant from
`45 == 45` to `47 == 47` (measured at base: 45 `gate`/`probe` rows naming round counters, 45
`reports/**/accept-*.py` blobs). A `gate` row without its counter file (or the reverse) breaks it; a `note`
row would not.

## (c) Ledger pairs that point into SKILL.md

`reports/round-75/ledger.json` (10751 B, mtime 14:55) holds **10** pairs:

| pairs | disposition | `stated_at` |
|---|---|---|
| L75-01, L75-05, L75-06, L75-07 | REPAIR | `SHONEN.md:6` |
| L75-02 | REPAIR | `corpus/README.md:344` |
| L75-03 | REPAIR | `corpus/README.md:407` |
| L75-04 | ANNOTATE | `corpus/README.md:813` |
| L75-08, L75-09 | ANNOTATE | `corpus/lessons/round-74.md:37`, `:38` |
| L75-10 | ANNOTATE | `LOG.md:4318` |

- **No pair points into SKILL.md.** No `stated_at` is SKILL.md and no `statement_after.path` is SKILL.md, so
  neither the line-701 correction nor the selftest receipt takes a REPAIR or ANNOTATE disposition.
- The two SKILL.md-adjacent obligations are `fixed_surfaces` entries, enforced inside the `REPAIR` leg's
  fixed-surface loop (containment at `<lands>`) and exempted from `APPENDONLY` by the `line` field. The
  selftest receipt carries no `line`, so it is read whole-file.
- **No pair cites `reports/round-75/telemetry/selftest-r72-repeat.txt`** either; the receipt is closed by the
  same fixed-surface loop, not by a SCORECARD correction row.
- Consequence: the L1 must land the SKILL.md edit and the receipt with the Ca landing; they are not closed by
  any correction row, and claim Ca's kill rule fails the claim on any false leg at `<lands>`.
- Line-number fragility (restated): the check slices line 701 literally; any landing that inserts a line above
  701 before `<lands>` moves the target. Claim C does not touch SKILL.md, so the frozen `line: 701` stays
  correct for this round's landings.

## (d) The staged receipt

Path: `.ufo/waves/round-75/w2/stage/reports/round-75/telemetry/selftest-r72-repeat.txt` (1543 B).

- Requirement: claim Ca `fixed_surfaces` entry 2 requires the content `SELFTEST: 10/11`; verified present.
- Provenance: `python3 -B reports/round-72/accept-c.py --selftest` run in a scratch clone of the lane checked
  out `--detach` at `f556d1049fe651d3d63975600b13acd9fb686f15` (tree `bb2e1b6fa5221db1f11cb3148a1fee7813d20639`);
  counter `reports/round-72/accept-c.py`, sha256
  `355e67f1bdb15d52368ad454d68d8391fd72d1de59622570689c4822d21da3c1`; exit 1; stderr empty; measured
  2026-10-27.
- The stdout block in the staged file was byte-compared against the captured run (equality true, including the
  trailing two blank lines and the tab in the CENSUS detail line).
- Why a repeat and not a transcription: at base `reports/round-72/telemetry/` holds `baseline.txt`,
  `census-start.txt`, `census-end.txt`, `controls-c.txt`, `controls-ca.txt`, `gap-sweep.txt`,
  `measures-c.txt`, `measures-ca.txt` — **no selftest receipt**. The prior record of the red is narrative:
  `SCORECARD.md:1423` (`## Corrections — round 73`) and `corpus/lessons/round-73.md:111` (R73-M4). Both are
  cited in the receipt's header as the prior record; neither is the receipt.

## Findings and limits

1. **`accept-c.py` is incomplete** (PART A only, ends at `# --- PART B ---`; no driver). The `accept-c-75` row
   therefore states declared grammar plus the measured emptiness, and is marked not-ready-to-land.
2. **`accept-ca.py --selftest` is red** at sha256 `d1670935…` (exit 1, seven failing checks). The row records
   the red rather than claiming a green selftest; QUALITY 23 wants a green selftest receipt before the falsify
   wave, so this is a freeze blocker unless the counter is repaired.
3. **Claims/counter drift:** docstring "eight adopted rows / two entries" vs claims "nine rows S885..S893 /
   three entries".
4. **Ledger has 10 pairs, not the 11 the w1 draft recorded** — consistent with claim Ca's after-state (6
   REPAIR, 4 ANNOTATE).
5. **No ledger pair anchors either SKILL.md obligation** (see (c)); a reader looking for a pair id will find
   none, and that is the correct state, not a gap.
6. Nothing was applied to SKILL.md or any lane file; the only executions were read-only git, the two
   counter invocations above, and the round-72 selftest repeat, all inside
   `/fast/scratch/hyaku/kotodama-r75/ScribeSkillFinal/` (deleted before this seat yielded; receipts copied
   into the wave dir first).
7. No tool was installed or upgraded; no network access in this seat, so no User-Agent record applies.
