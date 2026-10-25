# ScribeSkillGates — SKILL.md §Gates and probes rows for rounds 71-72 (round-73 w1, hyaku run 7)

- Seat: ScribeSkillGates (leaf; no delegation, no background jobs, no `task` spawns, no lane/fleet mutation).
- Lane root: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
- HEAD at measurement: `8841ad3b896a0227674fa0725b818c999118046f` — equals `reports/round-73/claims.json` `.base`.
- `git status --porcelain` at measurement (untracked only): `.ufo/waves/round-72/w1/ScoutMergeScan.md`, `.ufo/waves/round-72/w1/ScribeLesson.md`, `.ufo/waves/round-73/`, `reports/round-73/`. The working copy is **not** clean; the first two are exactly routed defect R1.
- Date: 2026-10-25 (pre-data; claims still DRAFT-v0).
- Tools installed: **none** (nothing needed). Live fetches: **none** (pure local work, so no User-Agent record applies; no Wayback/CDX probe needed).
- Writes made: this report and the draft named below. Nothing else in the lane, fleet, siblings or `/home/vgpnk/Projects/shokuknow` was touched.

## Verdict

1. **Five rows are missing, not six.** The registry's last row is `accept-o-69` (SKILL.md:697). Exactly five `reports/round-*/accept-*.py` files lack a registry row: `round-71/accept-c.py`, `round-71/accept-ca.py`, `round-71/accept-d.py`, `round-72/accept-c.py`, `round-72/accept-ca.py`. `reports/round-70/` contains **no** `accept-*.py`; round-70's claims were counted by shell pipelines. So the R3 wording "accept-ca-70..72 / accept-c-70..72" names two gates that never existed, and a Ca correction row should state the observed token as five counters.
2. **Draft rows are ready and shape-valid.** Five rows in the registry's own 8-column shape are drafted at the exact anchor (insert after SKILL.md:697, before the blank 698, ahead of the paragraph at 699). Each drafted row has exactly 8 cells and each matches the round-70 claim-O enumeration regex (`grep -cE '^\| [^|]+ \| (gate|probe) \| .*reports/round-[0-9]+/accept-[a-z]+\.py'` → 5/5), so inserting them restores that predicate from `36 != 41` to `41 == 41`.
3. **`accept-c-72 --selftest` is red at HEAD (10/11, exit 1)** — deterministic, tree-independent: the fixture writes `.ufo/waves/round-72/assimilation/validate-receipt.txt` (`accept-c.py:70`, written `:716`) while leg `GROUND` reads `reports/round-72/telemetry/gap-sweep.txt` (`:71`, read `:380`), which the fixture never creates. The `ground_zeros` mutant is therefore non-discriminating. The drafted self-test cell records the measured red rather than a passing claim.
4. **Both round-72 counters print a literal leg denominator.** `ACCEPT-C-72: … legs=10/10` (`accept-c.py:552`) and `ACCEPT-CA-72: … legs=12/12` (`accept-ca.py:231`) print the full denominator on FAIL too — measured: `ACCEPT-C-72: FAIL legs=10/10`, `ACCEPT-CA-72: FAIL legs=12/12`. A receipt check that greps the denominator without the `PASS` token can read a failure as a full pass; same class as routed defect R2.
5. **`accept-d-71` emits `ACCEPT-D-69: …`** (it delegates to the frozen round-69 counter), so a grep for `ACCEPT-D-71` finds nothing. The drafted row states the printed token.

## Registry facts measured

| probe | command | result |
|---|---|---|
| rows present | `grep -cE '^\| [^|]+ \| (gate\|probe) \| .*reports/round-[0-9]+/accept-[a-z]+\.py' SKILL.md` | `36` |
| counter files | `find reports -name 'accept-*.py' \| sort \| wc -l` | `41` |
| missing rows | per-file `grep -qF "reports/<rel>" SKILL.md` loop | the five round-71/72 files only |
| rounds 70-72 in registry | `grep -n 'round-7[012]' SKILL.md` | no output |
| table header | `grep -n '^| name | kind | entry command' SKILL.md` | line 648 (8 columns) |
| last row / anchor | `read SKILL.md:695-700` raw | last row 697, blank 698, prose from 699 |

## Gate/counter inventory relevant to the rows

| gate | file | legs | self-test |
|---|---|---|---|
| accept-c-71 | `reports/round-71/accept-c.py` (132 lines) | `ENTRY`, `COUNTS`, `CITED`, `ROWS`, `USEDBY-PATHS`, `CITED-LINES`, `SWEEP` (7) | none — `--selftest` is an argparse error |
| accept-ca-71 | `reports/round-71/accept-ca.py` (150 lines) | `V70-1`..`V70-5`, `QUARANTINE` (6) | none — `--selftest` is an argparse error |
| accept-d-71 | `reports/round-71/accept-d.py` (106 lines) | delegates to frozen `reports/round-69/accept-d.py` (8 legs: `STAMP`, `SECTION`, `TABLE`, `STATES`, `FIELDS`, `SIGNATURES`, `EVIDENCE`, `SOURCE`) | `--selftest` (no-git guard) |
| accept-c-72 | `reports/round-72/accept-c.py` (803 lines) | `ENTRIES`, `ROWS`, `REPOINTED`, `GATE`, `REJECTS`, `GROUND`, `CITEDLINES`, `CENSUS`, `SCRATCHMIRROR`, `COLLCHECK` (10) | `--selftest`, 1 clean + 10 mutants |
| accept-ca-72 | `reports/round-72/accept-ca.py` (249 lines) | `QUAL20`, `W2FILES`, `LOGCORR`, `LESSONCORR`, `REPORTCORR`, `MAPCORR`, `CASTAMP`, `QUAL21`, `CAPOEIRA`, `APPENDONLY`, `REPORTLAST`, `NOHARM` (12) | none — `--selftest` is an argparse error |

## Runs exercised (all read-only; no lane bytes written)

| command | exit | observed |
|---|---|---|
| `--help` on all five counters | 0 each | CLI shapes as drafted (see draft §5) |
| `python3 -B reports/round-71/accept-d.py --selftest` | 0 | `GREEN FIXTURE: PASS (legs 8/8)`, `DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8)`, `SELFTEST: 2/2` |
| `python3 -B reports/round-71/accept-d.py --root .` | 0 | `ACCEPT-D-69: PASS legs=8/8` |
| `python3 -B reports/round-72/accept-c.py --selftest` | **1** | `SELFTEST: 10/11`; clean fixture `LEG FAIL GROUND` — `receipt missing: reports/round-72/telemetry/gap-sweep.txt`; then `ACCEPT-C-72: FAIL legs=10/10` |
| `accept-c-72` with no `--lands` / `--lands deadbeef` | 2 / 2 | `ERROR: --lands must be a 40-hex commit` |
| `accept-c-72 --root <empty tmp dir> --lands <40 hex>` | 2 | `ERROR: not a git repository: /tmp/scg-nogit-…` |
| `accept-ca-72 --lands deadbeef` | 2 | `ERROR: --lands must be 40 hex` |
| `accept-ca-72 --lands 0000…0000` (well-formed, absent) | 1 | `LEG FAIL REPORTLAST`; `LEG FAIL NOHARM` (`corpus materialization failed`); `ACCEPT-CA-72: FAIL legs=12/12` |
| `accept-c-71 --selftest`, `accept-ca-71 --selftest` | 2 / 2 | `error: unrecognized arguments: --selftest` |
| `accept-ca-72 --selftest` | 2 | `error: the following arguments are required: --lands` |

Scratch hygiene: `accept-c-72 --selftest` left eleven `tempfile.mkdtemp` trees at `/tmp/r72st-*` (`build_fixture` never cleans up). This seat removed exactly the ones its own run created; the temporary `--root` probe dir `/tmp/scg-nogit-*` and the `/tmp/scg_*.out` captures were removed or confined to `/tmp`.

## Touched surfaces

- `kotodama-shokunin/.ufo/waves/round-73/w1/drafts/skill-gates-rows.md` — new (the drafted rows + anchor + per-gate detail + measured runs + findings).
- `kotodama-shokunin/.ufo/waves/round-73/w1/ScribeSkillGates.md` — new (this report).
- `/tmp` scratch only otherwise. SKILL.md, claims.json, corpus, reports, git index and fleet root untouched.

## Out of scope (deliberately not done)

- SKILL.md was not edited; no row was inserted. The canonical writer applies the draft.
- No full data-counter run for accept-c-71 / accept-ca-71 / accept-c-72 / accept-ca-72: the seat's brief authorised only `--selftest`/`--help` on read-only gates. Their verdict maps are taken from the scripts' own print statements plus the measured exit-1/exit-2 paths, not from a green round run.
- No row drafted for `accept-c-70` / `accept-ca-70`: no such files exist; drafting them would invent a gate.
- The `accept-c-72` selftest fixture gap and the hardcoded denominators were **reported, not repaired** — repairing a filed round's counter bytes is the canonical writer's decision, and R3's own Ca disposition covers registry rows only.

## Artifact paths

- Draft: `.ufo/waves/round-73/w1/drafts/skill-gates-rows.md`
- Report: `.ufo/waves/round-73/w1/ScribeSkillGates.md`
