# CriticSeparability57 — round 57 residual falsify: separability and declaration conformance

Seat: KotodamaR57.CriticSeparability57 (read-only leaf). Lane tip measured: `78d83b5e7145317a048c8f584d62739168b836bd`.
Sandbox: `/fast/scratch/hyaku/kotodama-r57/CriticSeparability57/` (clones `tip`, `baseC`, `baseO`; GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE unset). No tools installed or updated. No predicate amended.

## Findings

### F1 — MEDIUM — the declared separability command cannot evaluate between the claim lands and the records commit
Command, in clone `tip` at 78d83b5e:
```
$ python3 -B tools/check-claim-separability.py reports/round-57/separability-manifest.json
SEPARABILITY_INPUT_ERROR unit REC lands 'corpus/lessons/round-57.md', which is absent from the worktree under '/fast/scratch/hyaku/kotodama-r57/CriticSeparability57/tip'
exit 2
```
Cause: `reports/round-57/separability-manifest.json:36-49` puts the records unit `REC` into the manifest with `corpus/lessons/round-57.md`, which does not exist until records land. The declaration only states an expectation before landing (`reports/round-57/claims.json:212`, "exit 2 ... naming the absent C land"). It says nothing about the state after C and O land but before records, and at that point the command still exits 2. So separability cannot be shown at the commits where C and O actually landed. This is not a dependency finding, and exit 2 never reads as 0.

Derived measurement (not the declared command): I made a sandbox copy of the manifest with only `REC` removed (`/fast/scratch/hyaku/kotodama-r57/CriticSeparability57/manifest-noREC.json`; base, C and O units byte-equal) and ran it with `--root` set to the tip clone:
```
SEPARABILITY: 0 findings
exit 0
stderr: SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=2
```
The dynamic leg runs each acceptance on base plus that unit's lands, so it covered C, including the live LOCATE leg, and O.
Smallest safe correction: no rule change. Records SHOULD run the declared command only at the records commit and SHOULD file this derived receipt beside it, labelled as derived. Future manifests SHOULD declare the expected exit for the window after the claims land and before records.

### F2 — MEDIUM (tradeoff carried from round 56, not a defect of C) — records' edits to `corpus/SOURCES.md` will count as C's landed bytes
- `reports/round-57/claims.json:15` says records rows take S481-S499. Those rows go into `corpus/SOURCES.md`, which is a land of C only (`separability-manifest.json:9-12`). It is not one of REC's lands (`:39-48`).
- C uses `"tree": "WORKTREE"`. At the records commit, C's landed bytes will therefore include records-authored SOURCES rows and cell edits. The dynamic leg will then measure C as base plus (C ∪ records rows), not C at 78d83b5e.
- If `corpus/SOURCES.md` were listed under REC instead, the checker would report it as `SEPARABILITY_OVERLAP`.
- Round 56 accepted the same shape (c8af23f records carried SOURCES cell fixes, and 3569d24 reported "separability 0 findings").

Impacted axes: separability provenance for C.
Smallest safe correction: the records receipt SHOULD also run the derived manifest with `"tree"` pinned to `78d83b5e7145317a048c8f584d62739168b836bd` for C and `43f1e781` for O. That is the separability of what actually landed. The canonical judge decides whether WORKTREE-at-records is acceptable.

### F3 — LOW — O's predicate reads one of C's lands, and the dynamic leg is blind to that coupling
`reports/round-57/accept-o.py:319` copies the lane's `corpus/SOURCES.md` into each REAL fixture. KEEP (`:434-438`) runs the checker on lessons 49-56 against the lane registry and compares the output with a pin made at base. The O dynamic leg only runs base plus O, with base SOURCES.
I measured O on the full tip (base + C + O):
```
$ python3 -B reports/round-57/accept-o.py   (clone tip, no --seed)
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
GEN PASS ... REAL PASS ... MULTI PASS ... MUTANTS PASS ... KEEP PASS changed=[] ... FORMAT PASS ... SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
exit 0
```
So C's SOURCES rows do not disturb O today. [INFERENCE] If records edit a SOURCES cell (teaches or anchor) of a row cited in the Gate sections of lessons 49-56, KEEP or REAL could flip at the records commit. Records item 4 (S410) and item 5 route through superseding rows, which lowers the risk without removing it (`claims.json:214-218`).
Smallest safe correction: re-run `accept-o.py` without `--seed` at the records commit and file the receipt.

### F4 — LOW — the "frozen predicate" sentence in the counters' docstrings is not the claims.json sentence
- `reports/round-57/accept-c.py:36-37` prints `ACCEPT-C-57: every leg above prints PASS.` and `reports/round-57/accept-o.py:18-19` prints `ACCEPT-O-57: every leg below prints PASS on the checker under test.`
- Both docstrings call this "the same sentence in reports/round-57/claims.json". The claims.json predicates (`:21`, `:127`) are long leg-by-leg sentences.
- `claims.json:9` (`predicate_rule`) asks for "the same sentence here, as the same condition in its counter's code ... and as the same label in every receipt".
- Condition, label and legs do agree (F6). Only the docstrings' claim that the sentence is identical is false.

Smallest safe correction: a records erratum. Editing the instrument would change a scored rule, so it SHOULD NOT be edited now.

### F5 — LOW — the provenance wording "before any seat scored" overstates
`reports/round-57/claims.json:5`: "declared ... before any wave dispatch and before any seat scored". The two pre-dispatch critic seats scored the first instruments at `51726fa6`:
- `.ufo/waves/round-57/predispatch/CriticClauseListC57.md:3,34-43,79-89` records ACCEPT-C-57 PASS on three no-sourcing fixtures.
- `CriticClauseListO57.md:3,20` records PASS on two cheat checkers.

The rules then changed:
- the base moved from 6f08c494 to 0314aa98 (accept-c FRESH leg; accept-o REAL leg and neutral patches; reopen-quote 8-word minimum and refusals);
- the declaration was revised at 13226c18.

This is a rule change after seats scored. It was disclosed (`claims.json:7`, `base_note`), made before any data, and made before build dispatch, so it is legitimate pre-dispatch hardening, not post-hoc rescaling. The sentence should read "before build dispatch and before any build seat scored".

### F6 — PASS — everything else requested holds
- **Declaration predates both lands.** History is linear: `0314aa9 → 13226c1 → 286288f → 43f1e78 → 78d83b5`. `git merge-base --is-ancestor 13226c18 43f1e781` and `git merge-base --is-ancestor 13226c18 78d83b5e` both exit 0, and so does `0314aa98 → 13226c18`.
- **Timeline** (lane reflog, all "export from jj", times -0300):

  | Event | Time |
  |---|---|
  | 13226c1 declaration | 20:27:48 |
  | 286288f dry-run receipt (measured revision 13226c18; `declaration-dry-run.txt:1` at 23:28:07Z) | 20:28:14 |
  | `build-dispatch.json` mtime | 20:28:17.30 |
  | First build report (`ScribeQuality10.md`) | 20:30:09 |
  | 43f1e78 O land | 20:34:24 |
  | 78d83b5 C land | 21:01:52 |

  C's author date of 20:34:24 equals O's commit time. That is jj opening a new change right after O's commit, not a back-date.
- **No rule changed after the declaration or after any build seat scored.** `git diff --quiet 13226c18 HEAD -- reports/round-57/claims.json reports/round-57/separability-manifest.json reports/round-57/*.py reports/round-57/controls tools/check-claim-separability.py tools/check-source-access.py reports/round-28/readme/sweep.py reports/round-57/base-gate-keep.txt reports/round-57/base-knowledge-files.txt` exits 0. The only change to `reports/round-57` after the declaration is `telemetry/declaration-dry-run.txt` (286288f, before dispatch). The instruments are byte-identical between base 0314aa98 and the tip (`git diff --stat 0314aa98 HEAD -- accept-c.py accept-o.py reopen-quote.py tools/check-source-access.py` is empty).
- **The agreement check passes.** `python3 -B reports/round-57/claims-agree.py` prints `AGREE claims=['C', 'O']`, exit 0. It compares only base and lands, so I also checked the manifest against claims.json by script:
  - `exports` are equal for C and O;
  - each manifest acceptance argv equals its `counting_command`;
  - each predicate starts with `ACCEPT-<id>-57:`.
- **C on base plus only its own lands.** Clone at 0314aa98, then claims.json and manifest from 13226c18, then the three C lands from 78d83b5e. Running `python3 -B reports/round-57/accept-c.py` prints:
  ```
  SET PASS count=233 ... added=['corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md'] removed=[]
  SWEEP PASS exit=0 rows 233 files 233 missing_from_index 0 []
  FLOOR PASS cited=42 floor=20
  RANGE PASS / STATUS PASS / USEDBY PASS / ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
  LOCATE PASS located=41 cited=42 need=34 at=2026-10-23T00:06Z not_located=['S422: ...legislation.gov.uk/aosp/1672/47/1995-08-01?view=plain HTTPError; https://www.legislation.gov.uk/aosp/1672']
  FRESH PASS rows_reusing_registry_urls=[]
  ACCEPT-C-57: PASS
  exit 0
  ```
  The live count today is 41 of 42, against 40 of 42 in the land message. That is ordinary live variance and well above the need of 34.
- **O on base plus only its own land.** Clone at 0314aa98, then claims.json and manifest from 13226c18, then `tools/check-gate-quotes.py` from 43f1e781. Running `python3 -B reports/round-57/accept-o.py` without `--seed` (seeds 472356795..799, real seeds 472356895..897) gives every leg PASS:
  - MUTANTS exits are `{'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}`;
  - SELFTEST reports 52/52;
  - the result is `ACCEPT-O-57: PASS`, exit 0;
  - the tool sha256 `54981859...` matches the seat hash in the O commit message.
- **No cross-citation.**
  - `git show 78d83b5 | rg '^\+' | rg 'check-gate-quotes|tools/|accept-o|html-entity'` finds nothing (rc=1).
  - `git show 43f1e78 | rg '^\+' | rg '\bS(41[3-9]|4[2-7][0-9]|480)\b|heraldry|herald|emblem|myth-symbol|SOURCES.md|corpus/README'` finds nothing (rc=1).
  - The full `tools/check-gate-quotes.py` contains no id in S413-S480 (rc=1).
  - The C entry cites exactly S413-S454, all inside its block.
  - C's export regex matches 0 base lines of `corpus/SOURCES.md` or `corpus/README.md`, so export novelty holds.
- **The predicate sentences match the code legs.** The claims.json clause legs are `SET SWEEP FLOOR RANGE STATUS USEDBY ACCESS LOCATE FRESH` and `GEN REAL MULTI MUTANTS KEEP FORMAT SELFTEST`, the same legs and order as `accept-c.py:87-158` and `accept-o.py:443-453`. Constants match the sentences:
  - TOTAL=233, FLOOR=20, S413-S480 and SHARE 0.8 with ceil (`accept-c.py:56-61,144`);
  - the 8-word minimum and a cap of four URLs (`reopen-quote.py:172-175`);
  - five GEN seeds, three REAL seeds, ten MULTI runs, three kill mutants plus three neutral patches, LESSONS 49-56, and the seed from os.urandom when `--seed` is absent (`accept-o.py:101,384-386,424-433`).

  FRESH compares every source-cell URL, not only the first four (`reopen-quote.py:201-206`), which matches the predicate. RANGE also requires each row to have at least 13 cells (`accept-c.py:116`). The sentence doesn't state this, but it only makes the leg stricter.
  Receipt labels are only `ACCEPT-C-57` and `ACCEPT-O-57` across `telemetry/controls-c.txt`, `controls-o.txt` and `declaration-dry-run.txt` (`rg -o 'ACCEPT-[A-Z]+-[0-9]+'`).

## Verdict

I **agree** with what landed. C at 78d83b5e and O at 43f1e781 each pass their frozen predicate on base 0314aa98 plus only their own lands. Neither cites the other. The declaration at 13226c18 predates both lands and the build dispatch. No rule changed after the declaration or after any build seat scored. The only rule change after seats scored was the disclosed pre-dispatch revision that followed the two critic seats (F5).

Exact fixes, none of which amends a predicate:
1. **F1:** at the records commit, run the declared separability command and file it together with the derived no-REC receipt above, labelled as derived.
2. **F2:** also file a derived separability run with C's tree pinned to 78d83b5e and O's to 43f1e781, so the result covers what landed rather than worktree bytes that include records rows.
3. **F3:** re-run `accept-o.py` without `--seed` at the records commit, because records will touch `corpus/SOURCES.md`, which KEEP and REAL read.
4. **F4, F5:** add an erratum in `corpus/lessons/round-57.md`:
   - the docstring "frozen predicate" lines in accept-c.py and accept-o.py summarise the claims.json predicate and are not the same sentence;
   - the `declared_at` wording should read "before build dispatch; after the two pre-dispatch critic seats scored 51726fa6".
