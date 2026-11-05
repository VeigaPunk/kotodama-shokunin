# ExecSeparability — round-90: claims O and C are causally separable

Seat: ExecSeparability-2 · 2026-11-04 · milestone r90-v1 · lane kotodama
Frozen predicate read first: `reports/round-90/claims.json` at
`d0b6f2a7f9cc36272682749a9b047b739406f0c8` (base `6b0b86e4…`), unamended.

Deliverable: `.ufo/waves/round-90/w1/stage/ExecSeparability/separability90.py`
(L1 installs it as `reports/round-90/separability90.py`), plus the two receipts
in the same stage dir. Nothing outside the stage dir and this report was written.

## What the harness does

```
python3 -B reports/round-90/separability90.py --repo <lane> --freeze <40hex> \
    --lands <40hex> --work <existing-dir> [--expect O=PASS,C=FAIL] [--negative] \
    [--no-substrate] [--counter <40hex|worktree>] [--receipt PATH]
```

1. **One materialization.** `git archive --format=tar <lands>` is read as a
   binary stream and fed to `tar -x` (248,401,920 bytes for the freeze tree, no
   checkout). Both selections come from that single tree.
2. **Two overlay sandboxes.** Each overlay is a fresh `git init` repo whose
   `objects/info/alternates` points at the lane's object database (read-only; the
   lane is only `archive`/`show`/`ls-tree`'d, never written). The selected paths
   are copied in, committed with the **lands commit as parent**, and
   `git ls-tree -r` of that commit is asserted to be exactly the declared
   selection, so no sibling path can be smuggled in. The counter is then run
   against the overlay repo and the overlay commit.
3. **One pinned instrument.** `reports/round-90/measure90.py` is copied from the
   lane worktree (or an explicit revision), sha256-printed and matched against
   `reports/round-90/counter-revisions.md`; `claims.json` is always read from
   `--freeze`. The freeze holds counter rev 1 (`4091cda9…`), which *refuses*
   (rc2) instead of failing `ENTRY` when the entry is absent; revisions 2–6
   changed only absent-artifact branches, never a leg name, threshold or
   constant, so the harness runs the lane's shipping instrument and prints both
   hashes. This run: `rev=6 6e1ea6a5…`, `COUNTER AT LANDS … same=no`.
4. **Fresh run dir per counter run.** `measure90` extracts into `<work>/mat` with
   `exist_ok=True`; a reused work dir grades a stale extraction. The first draft
   of this harness did exactly that and printed `LEG PASS TOOL` with the tool
   deleted from the overlay — the negative proof caught it, and every run now
   gets `run-<claim>-<tag>-<commit12>`.

## Overlay path sets

| overlay | claim paths | non-graded extras |
|---|---|---|
| O | `tools/check-advance-evidence.py`, `reports/round-90/mutants.py`, `reports/round-90/mutation-score.{txt,json}`, `reports/round-90/controls/stub-tool.txt`, `reports/round-90/claims.json`, `reports/round-90/measure90.py` | `corpus/.overlay-keep` (0 B) |
| C | the entry, `corpus/SOURCES.md`, `corpus/lessons/round-90.md`, `reports/round-90/evidence/`, `corpus/README.md`, `reports/round-90/claims.json`, `reports/round-90/measure90.py`, `tools/check-advance-evidence.py` (instrument only), `tools/check-corpus-index.py` | `corpus/knowledge/**` (261 entries) |

Two declared extras, both printed on stdout, neither read by the other claim:

* **O structural marker** `corpus/.overlay-keep` — `measure90`'s `MATERIALIZE`
  leg tests `os.path.isdir(mat/corpus)` for *both* claims and git cannot store an
  empty directory. Zero bytes, not a claim path, read by no leg.
* **C substrate** `corpus/knowledge/**` — C's `INDEX` leg runs
  `tools/check-corpus-index.py`, which counts every partition file against
  `corpus/README.md` (`audit()`: MISSING_ROW/GHOST_ROW/HEADER_DRIFT/TOTALS_DRIFT).
  Truncating the tree fails INDEX for reasons unrelated to C. The count coupling
  is visible in the C negative proof below (`files=260 … findings=5` after one
  file was dropped). `--no-substrate` turns the extra off.

## Freeze demonstration — exact lines

```
$ python3 -B separability90.py --repo <lane> --freeze d0b6f2a7f9cc36272682749a9b047b739406f0c8 \
    --lands d0b6f2a7f9cc36272682749a9b047b739406f0c8 --work <dir> --expect O=PASS,C=FAIL --negative
COUNTER: source=worktree sha256=6e1ea6a5f96c6e92660e7a18c18b896d46dee3bf6368231e1a4a8fd7895406cd rev=6 (reports/round-90/measure90.py)
COUNTER AT LANDS: sha256=4091cda9e0b5af399e99e85898f3040b9070d4225cf11584a601fe4c19caf0ce same=no

MATERIALIZE: git archive --format=tar d0b6f2a7f9cc36272682749a9b047b739406f0c8 -> <work>/tree-lands (248401920 bytes, binary stream, no checkout)
--- measure90 --claim O on overlay O (lands=74b6d79e2fca4085d778f256100c3a8bd4cb65e6) ---
LEG PASS MATERIALIZE expected=lands 74b6d79e2fca4085d778f256100c3a8bd4cb65e6 materialized observed=<work>/run-O-positive-74b6d79e2fca/mat
LEG PASS TOOL expected=tools/check-advance-evidence.py sha256 121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed observed=121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed
LEG PASS SELFTEST expected=rc 0 and SELFTEST PASS 67/67 observed=SELFTEST PASS 67/67
LEG PASS REFUSALS expected=13 refusal cases each ok observed=all ok
LEG PASS MUTATION expected=killed==total>=42, 0 survived, 0 broken-pattern observed=MUTATION-SCORE: 43/43 killed, 0 survived, 0 broken-pattern
LEG PASS STUB expected=reports/round-90/controls/stub-tool.txt records the stub failing SELFTEST and MUTATION observed=recorded
MEASURE90-O: PASS legs=6/6

VERDICT O: PASS legs=6/6
SANDBOX O: paths=8 archive_bytes=248401920 graded=7 substrate=0 structural=['corpus/.overlay-keep']
ABSENT other-claim paths in overlay O: 6/6 absent -> corpus/knowledge/linguistics/petitionary-and-votive-formulae.md, corpus/SOURCES.md, corpus/lessons/round-90.md, reports/round-90/evidence, corpus/README.md, tools/check-corpus-index.py
SHARED declared in both overlays: reports/round-90/claims.json, reports/round-90/measure90.py, tools/check-advance-evidence.py
MATERIALIZED O: other-claim paths found under <work>/run-O-positive-74b6d79e2fca/mat: none

--- measure90 --claim C on overlay C (lands=7b332187f591096eb04f731709911e01bc7fe942) ---
LEG PASS MATERIALIZE expected=lands 7b332187f591096eb04f731709911e01bc7fe942 materialized observed=<work>/run-C-positive-7b332187f591/mat
LEG FAIL ENTRY expected=corpus/knowledge/linguistics/petitionary-and-votive-formulae.md exists at lands observed=entry absent at lands
LEG PASS INDEX expected=index tool exit 0 over the lands tree observed=CORPUS-INDEX: OK files=261 rows=261 findings=0
LEG FAIL APPENDONLY expected=no base row changed; >=3 new mined A/B rows cited; README row observed=0 qualifying new ids < 3; entry absent from corpus/README.md
MEASURE90-C: FAIL legs=2/4 failed=ENTRY,APPENDONLY

VERDICT C: FAIL legs=2/4 failed=ENTRY,APPENDONLY
SANDBOX C: paths=267 archive_bytes=248401920 graded=9 substrate=1 structural=none
ABSENT other-claim paths in overlay C: 4/4 absent -> reports/round-90/mutants.py, reports/round-90/mutation-score.txt, reports/round-90/mutation-score.json, reports/round-90/controls/stub-tool.txt
SHARED declared in both overlays: reports/round-90/claims.json, reports/round-90/measure90.py, tools/check-advance-evidence.py
MATERIALIZED C: other-claim paths found under <work>/run-C-positive-7b332187f591/mat: none
ABSENT at lands (not in the d0b6f2a7f9cc tree): corpus/knowledge/linguistics/petitionary-and-votive-formulae.md, corpus/lessons/round-90.md, reports/round-90/evidence

--- negative proof O: dropped tools/check-advance-evidence.py ---
dropped=tools/check-advance-evidence.py overlay_lands=3dc1d996253a711e60ec914cdcd22d1ef26753a1 verdict=FAIL rc=1 flip=TOOL PASS->FAIL
LEG FAIL TOOL expected=tools/check-advance-evidence.py sha256 121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed observed=absent
MEASURE90-O: FAIL legs=2/6 failed=TOOL,SELFTEST,REFUSALS,MUTATION

--- negative proof C: dropped corpus/knowledge/linguistics/color-terminology.md ---
dropped=corpus/knowledge/linguistics/color-terminology.md overlay_lands=ea6aab6fec66482406751bfabb4bf060c8279233 verdict=FAIL rc=1 flip=INDEX PASS->FAIL
LEG FAIL INDEX expected=index tool exit 0 over the lands tree observed=CORPUS-INDEX: FINDINGS files=260 rows=261 findings=5 ids=FOOTER_DIR_TOTALS,FOOTER_TOTAL,GHOST_ROW,HEADER_DRIFT,TOTALS_DRIFT
MEASURE90-C: FAIL legs=1/4 failed=ENTRY,INDEX,APPENDONLY

SUMMARY O=PASS C=FAIL expected=O=PASS,C=FAIL matched=True negative=pass
SEPARABILITY: PASS (each claim graded only by its own overlay; other claim paths absent O=6/6 C=4/4)
CLAIMS: PARTIAL (O=PASS, C=FAIL)
EXIT-RULE: --expect O=PASS,C=FAIL -> rc=0
```

(The `VERDICT`/`SANDBOX`/`ABSENT`/`SHARED`/`MATERIALIZED` lines are the harness's
own; the `LEG`/`MEASURE90` lines are the counter's, printed verbatim.)

**Separability statement.** At the freeze, O passes 6/6 with all six of C's
graded paths absent from its sandbox (entry, registry, lesson, evidence dir,
README, index tool) and none of them present under the materialized tree the
counter actually graded; C fails `ENTRY`+`APPENDONLY` with all four O-specific
paths absent (mutants.py, both mutation-score files, stub-tool.txt). The only
paths both sandboxes carry are the three declared shared instruments
(`claims.json`, `measure90.py`, `tools/check-advance-evidence.py`), which are the
instrument of C and the graded object of O, not either claim's evidence. Each
verdict is therefore produced without the other claim's graded files: the two
claims are graded independently, not by one landing that satisfies both.

## The harness can fail — deletion proofs

Each negative proof copies the overlay repo, deletes one required path, commits
the reduced tree over the overlay commit (asserting the path is gone from
`ls-tree`), and re-runs the counter. The harness picks the deletion whose leg
currently *passes*, so the line shows a real flip:

* O — dropping `tools/check-advance-evidence.py` flips `TOOL` PASS→FAIL
  (`observed=absent`) and takes SELFTEST, REFUSALS and MUTATION with it.
* C — dropping one counted partition file
  (`corpus/knowledge/linguistics/color-terminology.md`) flips `INDEX` PASS→FAIL
  (`files=260 rows=261 findings=5`). On a lands where the entry exists, the
  candidate list prefers the entry itself and flips `ENTRY` instead; at the
  freeze the entry is already absent, which is exactly why C fails there.

Both proofs are asserted (`negative=pass`); a negative that did not fail makes
the harness exit 1.

## Exit contract

Without `--expect` the run above prints

```
SUMMARY O=PASS C=FAIL expected=O=PASS,C=PASS matched=False negative=skipped
SEPARABILITY: PASS (each claim graded only by its own overlay; other claim paths absent O=6/6 C=4/4)
CLAIMS: PARTIAL (O=PASS, C=FAIL)
EXIT-RULE: both claims must pass in their own overlay -> rc=1
```

and exits 1: **exit 0 only when both claims pass in their own overlay** (plus
disjoint overlays, plus every requested negative proof failing). `--expect` does
not weaken a claim — it renames the exit predicate to "the observed verdicts
equal this requested pattern", which is how the at-freeze demonstration is
asserted; the counter's verdict lines and `CLAIMS:` always show the truth.
Refused input (bad revision, non-directory `--work`, a counter with no verdict
line) exits 2.

## Bounds and risks

1. **C has not been shown to pass.** No conforming lands exists yet: the entry,
   `corpus/lessons/round-90.md` and `reports/round-90/evidence/` are absent at
   the freeze, and building a synthetic one would duplicate ScribeEntry's work
   with unowned bytes. What is proven here is the separability property and that
   the C overlay carries every path C's legs read; whether C passes is decided by
   the lands run, and the harness names the failing leg if it does not.
2. **Counter revision.** HEAD `c0c628d8` commits counter rev 5 (`80a07a57…`); the
   worktree carries rev 6 (`6e1ea6a5…`, the `{name: verdict}` ENTRY-parse fix
   that ReviewerEntry-3 reported). This run pins rev 6 and prints
   `COUNTER AT LANDS … same=no` for the freeze lands. L1 should land the counter
   it intends to grade with; if lands ships a different counter the line turns
   `same=yes`/`no` and the harness still runs the pinned bytes, so both overlays
   are graded by one instrument.
3. **Freeze counter rev 1 refuses instead of failing** on the absent entry, so
   the at-freeze demonstration uses rev 6; `claims.json` (the frozen predicate,
   constants and kill rules) is read from the freeze in every run.
4. **Structural extras are declared, not hidden.** The O marker and the C
   substrate are the only non-claim paths in either sandbox, both printed with
   their sizes/counts; `ls-tree` equality against the declared selection means
   nothing else can be present.
5. **Scope.** This proves the two claims' graded path sets are disjoint and each
   claim passes/fails on its own overlay; it does not prove that no other
   counterfeit class exists, and it does not grade the scholarly truth of C's
   content (that is the closure's source re-open). No network was used; every
   surface is a committed revision.

## Files changed

| path | what |
|---|---|
| `.ufo/waves/round-90/w1/stage/ExecSeparability/separability90.py` | the harness (L1 installs as `reports/round-90/separability90.py`) |
| `.ufo/waves/round-90/w1/stage/ExecSeparability/freeze-demo-receipt.{txt,json}` | freeze run with `--expect O=PASS,C=FAIL --negative`, rc=0 |
| `.ufo/waves/round-90/w1/stage/ExecSeparability/freeze-default-receipt.{txt,json}` | freeze run without `--expect`, rc=1 |
| `.ufo/waves/round-90/w1/ExecSeparability.md` | this report |

No production file, no lane commit, no fleet-repo write, no `~/.local/bin` write.
Tooling: nothing installed (python3 3.14 + git were sufficient); scratch
`/fast/scratch/hyaku/kotodama-r90/ExecSeparability/` deleted after the receipts
were copied out.

## What L1 should run after integration

```
python3 -B reports/round-90/separability90.py --repo . \
  --freeze d0b6f2a7f9cc36272682749a9b047b739406f0c8 --lands <lands 40hex> \
  --work <existing dir>
```

Expect `MEASURE90-O: PASS legs=6/6`, `MEASURE90-C: PASS legs=4/4`,
`CLAIMS: BOTH-PASS`, `rc=0`. Add `--negative` to re-prove the deletion legs on
the integrated bytes; add `--receipt` to keep the machine copy.
