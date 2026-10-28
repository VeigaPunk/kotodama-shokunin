# ExecCensusEnd — census machinery check (round 77, wave 1)

Verdict: **BUILD PASS** — the assigned census command is green at base (exit 0) and green on a
mirrored registry carrying the two draft S897/S898 rows (exit 0, no E03/E04, warning set
unchanged). Three landing-design constraints fell out of the controls (E11 ordering, E12
placement, one-sided E04 `supersedes` exemption) and are recorded below for the C-lands design.

Lane base `211f9526800906e0c585d878d265c37e5e090c15`; lane HEAD is that revision and the
working-tree registry is byte-identical to the base blob:

```
$ git -C …/kotodama-shokunin rev-parse HEAD
211f9526800906e0c585d878d265c37e5e090c15
$ sha256sum corpus/SOURCES.md
51b18f1c98996056287e0eae4d24cd682b3d756fe898e50f7356cbf680af8301  corpus/SOURCES.md
$ git -C … show 211f952…:corpus/SOURCES.md | sha256sum
51b18f1c98996056287e0eae4d24cd682b3d756fe898e50f7356cbf680af8301  -
```

Nothing was written outside `…/.ufo/waves/round-77/w1/stage/ExecCensusEnd/` and this report.
The real `corpus/SOURCES.md` was never touched. Receipts: `…/w1/stage/ExecCensusEnd/`
(`README.txt` holds every command with its exit code).

## Receipt 1 — base run, roster path

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
      --root /home/vgpnk/Projects/shokunin kotodama
exit=0
kotodama	W04	S127 duplicate url voices.uchicago.edu/…/research-statement across scopes
… (28 x W04, 4 x W01) …
kotodama	W01	S893 tierC mined used-by=corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
```
Raw: `census-base.out` (3769 bytes). stderr `census-base.err` (0 bytes).
Warning counts: `grep -cE '\tW04\t' census-base.out` → **28 — grep**; `grep -cE '\tW01\t'` → **4 — grep**;
E-codes: `grep -cE '\tE[0-9]+\t' census-base.out` → **0 — grep**.

## Receipt 2 — mirrored registry + the two draft rows

Mirror built from the base tree, not from the working copy:

```
$ mkdir -p <scratch>/mirror
$ git -C …/kotodama-shokunin archive 211f952… | tar -x -C <scratch>/mirror     # 205M
$ sha256sum <scratch>/mirror/corpus/SOURCES.md
51b18f1c98996056287e0eae4d24cd682b3d756fe898e50f7356cbf680af8301  -            # == base
```
Mirror fidelity control (untouched registry, `--file`): exit **0 — validate --file**, same 28 W04 +
4 W01 + `ok`, stderr empty (`census-mirror-base.out`), and
`census --file …/mirror/corpus/SOURCES.md` → `file rows 820` (`census-mirror-base-census.out`).

Draft rows (`rows-897-898.md`, appended inside the Registry table): S897 → D1
`lishisuo.cssn.cn/…/t20210316_5318560.shtml` (+ 20240111092427 capture), S898 → D2
`onomastica.ijppan.pl/…/download/574/763/` (+ 20251231111748 and 20260901045105 captures);
kind `paper`, status `mined`, opened `2026-10-27`, recheck `365d`, used-by the planned entry
`corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`. Field shape:
`awk -F'|' '/^\| S(897|898) /{print $2, NF}'` → **13 fields (11 cells) each** — awk.

```
$ wc -l <scratch>/mirror-draft/corpus/SOURCES.md
955            # base 953 + 2
$ grep -n '^## ' <scratch>/mirror-draft/corpus/SOURCES.md
26:## Registry  855:## Paths  892:## Search log  906:## Leads (unopened)   # rows sit at 852,853 → inside Registry
$ sources-census.sh validate --file <scratch>/mirror-draft/corpus/SOURCES.md
exit=0
… 28 x W04, 4 x W01 …
file	ok	<scratch>/mirror-draft/corpus/SOURCES.md
```
`grep -cE '\tE[0-9]+\t' census-mirror-draft.out` → **0 — grep**;
`grep -cE '\tE0[34]\t'` → **0 — grep**;
`grep -E 'S89[789]' census-mirror-draft.out` → **no lines — grep** (the new rows raise no finding);
stderr 0 bytes. Census after append: `census --file …` → `file rows 822`, `tier.A 495`,
`status.mined 727`, `queued 58`, `rejected 37` (`census-mirror-draft-census.out`); base was
`820 / 493 / 725` → **+2 rows, +2 tier.A, +2 mined — sources-census.sh census**. This matches the
claim's `820 → 822` target and shows the ROWS leg's unit is exactly the `| S### |` line.

A stand-in file at the used-by path was created *in the mirror only* so E11 could resolve; it
stands in for the C-lands entry.

## Controls (hardlinked copies of the draft mirror, one row added)

```
ctl-e03.out        duplicate id S897, distinct URL/scope          exit=1  E03 x1  → file  E03  S897 duplicate id
ctl-e04.out        S899 same URL+scope as S898, no supersedes     exit=1  E04 x1  → file  E04  S898 duplicate url onomastica…/574/763 within scope …
ctl-e04super.out   same supersedes row INSERTED BEFORE S898       exit=1  E04 x1  (fires on S898)
ctl-e04super2.out  same supersedes row inserted AFTER S898        exit=0  E=0, "file ok"
ctl-e12.out        two draft rows appended at end of file         exit=1  E12 x2  (S897, S898)
ctl-e11entry.out   rows landed, used-by entry file absent         exit=1  E11 x2  (S897, S898)
ctl-minimal.out    registry-only mirror, no corpus tree           exit=1  E11 x755
```
`grep -cE '\tE[0-9]+\t' ctl-*.out` produced the E counts above; every control still prints the
same 28 W04 + 4 W01, so the errors are additions, not substitutions. Machinery selftest at the
same revision: `TMPDIR=<scratch>/tmp sources-census.sh selftest` → exit **0**, `selftest ok`,
**96 — grep -c '^killed'**, **0 — grep -c SURVIVED**, empty temp dir afterwards (`selftest.out`).

## Findings for the C-lands design

1. **Green by construction, not vacuous.** The base registry holds neither document and no id
   above S896: `git show 211f952…:corpus/SOURCES.md | grep -cE 'lishisuo\.cssn\.cn|onomastica\.ijppan\.pl|ONOMAST\.69|5318560'`
   → **0 each — grep**; `grep -oE '^\| S[0-9]+' | sort | tail -2` → **S895, S896 — grep/sort**.
   So no E03/E04 risk from the append itself; E03/E04 fire on demand (ctl-e03/ctl-e04), which is
   what makes the "0 E03/E04" result meaningful.
2. **E11 makes the row-append order-sensitive (§ sequencing for the counter).** `--file` sets the
   lane dir to `realpath(dirname(file)/..)` and E11 stats every `used-by` path there. Rows landing
   before the entry file → **2 E11 — validate**, exit 1 (ctl-e11entry). The two rows and the entry
   must land in the same C-lands commit (or the entry first). The claim's end census uses
   `--root …` against the real tree, so it is green only once the entry is on disk.
3. **Placement.** Appending at end-of-file puts the rows under `## Leads` and yields **2 E12 —
   validate** (ctl-e12). The Registry table ends at S896 (line 851 at base; `## Paths` follows), so
   the rows belong between S896 and `## Paths`.
4. **The `supersedes S###` E04 exemption is one-sided.** A correction row carrying
   `supersedes S898` passes when it follows S898 (ctl-e04super2 → exit 0) but makes the *older*
   row E04 when inserted before it (ctl-e04super → E04 on S898). Append-only practice is safe;
   inserting or re-ordering a registry row is not.
5. **Any draft-registry validation needs the corpus tree.** A registry-only mirror produces
   **755 E11 — grep -cE '\tE11\t' ctl-minimal.out**, exit 1, even though its E03/E04 sweep is
   clean (**0 — grep**). Wave-2 seats that want to pre-validate a draft SOURCES.md must mirror
   the tree (or the used-by targets), not just the file.

## Cell status of the draft rows (not evidence)

`rows-897-898.md` is schema-shaped, not evidence-bearing: the `anchor` (located quote + window
scope) and `teaches` cells are explicit DRAFT placeholders to be replaced verbatim from
`reports/round-77/evidence/S897.txt` / `S898.txt`, and `tier` is set to `A` under the registry's
"original paper for its own ground" rule for the L1 to confirm at freeze. `opened 2026-10-27` is
this round's access date. None of the placeholders creates a finding (no W/E line mentions S897
or S898 in `census-mirror-draft.out`), but a landed row with placeholder text would fail the
claim's own kill rule ("row without a same-page capture and live URL pair"), so they must not be
lifted as-is.

## Unrun (recorded, not claimed)

- Re-opening D1/D2 (fetch, UA binding, capture status) — belongs to the S897/S898 capture seats;
  this seat only read the claims' stated access facts.
- `reports/round-77/accept-c.py` — absent in the lane working tree at this revision
  (`ls reports/round-77/` → `telemetry` only), so the C-leg counter was not executed here; it is
  installed at the freeze.
- No build, lint, test or formatter run beyond the census commands and their selftest (wave in
  flight; the parent owns the post-integration gate).
- No tool installed or upgraded (nothing needed; pacman untouched).

No blockers.
