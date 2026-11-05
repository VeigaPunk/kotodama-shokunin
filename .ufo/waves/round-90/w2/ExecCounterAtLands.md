# ExecCounterAtLands — round-90 w2 receipt ( Kotodama / Godspeed )

## What ran

Frozen instrument re-run from a clean shared clone pinned to the lands revision:

```
git clone --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r90/ExecCounterAtLands/clone
git -C /fast/scratch/hyaku/kotodama-r90/ExecCounterAtLands/clone checkout 7f3a7aa6615624afadc2cc2d2d4f7ad225f44761
# HEAD detached at 7f3a7aa6; git status --porcelain = 0 entries
```

Ran from the production worktree (cwd /home/vgpnk/Projects/shokunin/kotodama-shokunin), never modified:

```
python3 -B reports/round-90/measure90.py --root .../clone --freeze d0b6f2a7... --lands 7f3a7aa6... --claim O --work work/O
python3 -B reports/round-90/measure90.py --root .../clone --freeze d0b6f2a7... --lands 7f3a7aa6... --claim C --work work/C
python3 -B reports/round-90/separability90.py --repo .../clone --freeze d0b6f2a7... --lands 7f3a7aa6... --work work/S --receipt receipts/separability90.json
```

For the record, the same invocation against the **lands-copy** of separability90.py (line for line what ships in 7f3a7aa6) refuses rc=2 before grading; see "Lands-copy divergence" below. Fixture was created directly via the clone, not via Python, so git authoring/config defaults are untouched.

## Claim O — rc 0 (PASS)

```
LEG PASS MATERIALIZE expected=lands 7f3a7aa6615624afadc2cc2d2d4f7ad225f44761 materialized observed=work/O/mat
LEG PASS TOOL expected=tools/check-advance-evidence.py sha256 121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed observed=121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed
LEG PASS SELFTEST expected=rc 0 and SELFTEST PASS 67/67 observed=SELFTEST PASS 67/67
LEG PASS REFUSALS expected=13 refusal cases each ok observed=all ok
LEG PASS MUTATION expected=killed==total>=42, 0 survived, 0 broken-pattern observed=MUTATION-SCORE: 43/43 killed, 0 survived, 0 broken-pattern
LEG PASS STUB expected=stub-work-with-tools.txt records the stub failing SELFTEST and MUTATION observed=recorded
MEASURE90-O: PASS legs=6/6
RC_O=0
```

(rc echoed by the shell into receipts/measure90-O.out.)

## Claim C — rc 0 (PASS)

```
LEG PASS MATERIALIZE expected=lands 7f3a7aa6615624afadc2cc2d2d4f7ad225f44761 materialized observed=work/C/mat
LEG PASS ENTRY expected=entry mode passes ENTRY,SHAPE,TOPIC,NEWIDS,GATE,CAPTURE observed=clean
LEG PASS INDEX expected=index tool exit 0 over the lands tree observed=CORPUS-INDEX: OK files=262 rows=262 findings=0
LEG PASS APPENDONLY expected=no base row changed; >=3 new mined A/B rows cited; README row observed=clean
MEASURE90-C: PASS legs=4/4
RC_C=0
```

Grader receipt (work/C/entry-receipt.txt, staged in stage dir as well):

```
LEG PASS ENTRY expected=>=12000B, >=6 h2, header keys observed=clean
LEG PASS SHAPE expected=>=5 data rows x >=3 cols, no filler repetition observed=clean
LEG PASS TOPIC expected=>=10 shared content words with the declared topic observed=clean
LEG PASS NEWIDS expected=>=3 new mined A/B rows opened 2026-11-04 and cited observed=clean
LEG PASS GATE expected=each new id has a located gate line observed=clean
LEG PASS CAPTURE expected=each gate quote occurs in its committed capture observed=clean
ENTRY-EVIDENCE: PASS legs=6/6
```

## Separability — production worktree copy (3c6dda1d…, i.e. post-fe59fc35 rc0 pass)

```
VERDICT O: PASS legs=6/6
VERDICT C: PASS legs=4/4
SANDBOX O: paths=8 graded=7 substrate=0 structural=['corpus/.overlay-keep']
ABSENT other-claim paths in overlay O: 6/6 absent (entry, SOURCES, lesson, evidence/, README, check-corpus-index.py)
SANDBOX C: paths=278 graded=9 substrate=1 structural=none
ABSENT other-claim paths in overlay C: 4/4 absent (mutants.py, mutation-score.{txt,json}, controls/stub-tool.txt)
SHARED declared in both overlays: reports/round-90/claims.json, reports/round-90/measure90.py, tools/check-advance-evidence.py
MATERIALIZED O: other-claim paths found under run-O/mat: none
MATERIALIZED C: other-claim paths found under run-C/mat: none
SUMMARY O=PASS C=PASS expected=O=PASS,C=PASS matched=True negative=skipped
SEPARABILITY: PASS
CLAIMS: BOTH-PASS (O=PASS, C=PASS)
RC_SEP=0
```

Thought: O overlays manifest 8 paths, not 7, because overlay O carries O_STRUCTURAL `corpus/.overlay-keep` (0-byte marker so `os.path.isdir(corpus)` holds under the counter's MATERIALIZE isdir test); this is a declared non-graded structural path, not substrate — the harness partitions it explicitly.

## Lands-copy divergence — lands refusal, post-lands fix exists

Lands-copy receipt:

```
SEPARABILITY90 freeze=d0b6f2a7... lands=7f3a7aa6...
O: <no run>   (died in build_overlay before the counter started)
C: <no run>
rc=2   (instrument refuses its own input, not measured on claims)
```

- `git show 7f3a7aa6:reports/round-90/separability90.py` sha256 = 3c6dda1d… (production file, "rev=6" post-fe59fc35)
- exact diff lands → production: `expected = sorted(present)` → `expected = sorted(set(present))` (line 251, one-line fix in fix commit fe59fc35 "w2 falsification wave spec, validated dispatch, ready handoff (11 seats) and separability set-overlay fix")
- reproduced failure with the lands copy (exact lands bytes,ISIS not a different checkout):
  `python3 -B clone/reports/round-90/separability90.py --repo clone --freeze d0b6f2a7… --lands 7f3a7aa6… --work work/S2 --receipt receipts/separability90-lands-copy.out`
  → `SEPARABILITY90_ERROR: overlay C tree is not the declared selection: extra=[] missing=[]`, `rc=2`
- inspecting `build_overlay`: `selected = tuple(graded) + tuple(substrate)` can place one rel path twice (graded spec also covered by a substrate directory glob), e.g. one C_SPEC also inside `corpus/knowledge/`. The production file's `sorted(set(present))` collapses that duplicate so the tree-must-equal-selection assert holds; the lands copy does not, and the assert fires before any counter print. Same for overlay O when a graded spec is also under `corpus/knowledge/`.

## Verifications

| what | how | result |
|---|---|---|
| counter rev | `reports/round-90/counter-revisions.md` rev 6 row + `sha256sum(reports/round-90/measure90.py)` | `6e1ea6a5…` both in doc and file; rev-6 rationale matches observed rc0onceleg-name-keying fix (reads through `dict(re.findall(...))` → `{name: verdict}`) |
| separability worktree bytes | `sha256sum reports/round-90/separability90.py` = `3c6dda1d…` | matches the production file that runs green; differs from lands \(1e68ebf0…\) exactly by the documented one-liner; separability90.py is not in counter-revisions (only measure90.py is), so expost separability bytes are lane worktree bytes, as intended |
| freeze claims.json vs worktree | `git show d0b6f2a7…:reports/round-90/claims.json \| sha256sum` = `9c161eee…`; `sha256sum reports/round-90/claims.json` = `9c161eee…` | identical (9c161eee…) |
| lands worktree, claims.json | `cmp(...)` | differs at base `6b0b86e4` (claims.json absent at base) as expected |
| lands-counter byte identity | `cmp <(git show 7f3a7aa6:measure90.py) <worktree measure90.py>` and same against clone | identical both ways |
| clone cleanliness | `git status --porcelain` at 7f3a7aa6 | 0 entries |

## Receipts (staged before scratch rm)

- `receipts/measure90-O.out` — LEG lines O + rc
- `receipts/measure90-C.out` — LEG lines C + rc
- `receipts/entry-receipt.txt` — the lands grader's own 6/6 receipt (work/C)
- `receipts/separability90.out`, `receipts/separability90.json`, `receipts/separability90.json.json` — production separability run and both receipts
- `receipts/separability90-lands-copy.log` — the lands-copy refusal (feature: same command as production, only measured instrument differs)
- `separability90.lands.py` — verbatim lands copy for future byte-exact re-run reference

No production files modified (cwd lane only read); .ufo/waves/round-90/w2/. This is the only file written outside receipts/, plus the staged counterparts in stage/.

All four expected behaviors observed green at lands: claim O PASS (rc 0), claim C PASS (rc 0), separability PASS on the production stock, and the production stock is also the historical post-fix copy — the lands ramp line `expected = sorted(present)` is the only intemperie and is already corrected in the lane worktree `3c6dda1d…`.
