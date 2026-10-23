VERDICT: ALL-FAIL

| variant | fixture path | failing legs | exit |
|---|---|---|---|
| junk | `.ufo/waves/round-58/control/CtlJunk58/fixture.patch` plus the untracked entry below | LOCATE, BOILER, TOPIC | 1 |

Cheapest variant I could NOT build: the prescribed junk fixture passing the complete counter without changing its sources or quotes. The ten invalid-host rows returned `URLError`; all ten real-page quotes were measured `quote-absent`. A positive LOCATE result would require different evidence or a different instrument, not the assigned fixture. This is a limit of this control, not a claim that every shortcut is blocked.

Installs: none. Existing Python stdlib, Git and GNU timeout were sufficient; no package-manager transactions.

## Counterexample and exact fixture

The attempted shortcut adds the claimed filename and index bookkeeping without learning toponymy. Its entry consists of twenty arbitrary noun-pair design prompts, each citing one distinct row from S500 through S519 individually. All twenty rows have kind `docs`, tier `B`, status `mined`, and used-by exactly `corpus/knowledge/linguistics/toponymy-place-names.md`.

Each fabricated anchor is a 12-word random-word sentence. Ten contain `place name river town`. S500–S509 point to `https://nonexistent-host-r58.invalid/x00` through `/x09`; S510–S519 point to ten unrelated Python standard-library documentation pages. The teaches cell and citing entry line deliberately reuse two quote nouns, without copying a six-word quote run. This makes the control stronger than junk that fails merely for missing citations or mismatched cells.

The README adds the entry's exact topic text, changes the linguistics count from 28 to 29, and changes the total and footer to 234. No existing knowledge file is removed. No instrument file was modified.

Exact artifacts, all paths relative to the lane root:

- Tracked README/SOURCES diff: `.ufo/waves/round-58/control/CtlJunk58/fixture.patch` (captured with sandbox `git diff --no-ext-diff --no-color`).
- Untracked entry: `.ufo/waves/round-58/control/CtlJunk58/untracked/corpus/knowledge/linguistics/toponymy-place-names.md`. Apply the patch to the declaration checkout and copy this entry to its corresponding corpus path to reconstruct the fixture.
- Full counter stdout: `.ufo/waves/round-58/control/CtlJunk58/junk.stdout.txt`.
- Counter stderr: `.ufo/waves/round-58/control/CtlJunk58/junk.stderr.txt` (empty).
- Counter exit status: `.ufo/waves/round-58/control/CtlJunk58/junk.exit.txt`.
- Command, timing and result: `.ufo/waves/round-58/control/CtlJunk58/junk.run.json`.
- Ordinary-GET receipts and complete served HTML: `.ufo/waves/round-58/control/CtlJunk58/opened-pages/opened-pages.json` and its named sibling `.html` files. All ten real pages returned HTTP 200 by plain urllib GET; no browser, login, captcha handling or access-control circumvention was used.

## Measured evidence

Sandbox: `/fast/scratch/hyaku/kotodama-r58/CtlJunk58/clone`, cloned with `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` unset and checked out at declaration receipt `d4a5ea31cde8cd20633f2ec03ae22296e389082b`. No Git or jj write was made in the lane or fleet repository. Lane writes are confined to this report and its artifact directory.

One counter run, at 2026-10-23T01:13:29Z, using the frozen command from the clone root:

```text
timeout 1200 python3 -B reports/round-58/accept-c.py
```

- PASS: SET (234 files, only the specified entry added), SWEEP (234 rows/files, no missing index row), FLOOR (20 citations), RANGE, STATUS, USEDBY, ACCESS, RELEVANCE (20/20), FRESH.
- FAIL: LOCATE (0/20; ten `URLError`, ten `quote-absent`), BOILER (0/20, all `not-located`), TOPIC (0/20, all `not-located`). The ten keyword-stuffed quotes each had `quote_hits=1`, but could not establish page-backed topic evidence.
- Final stdout line: `ACCEPT-C-58: FAIL`; counter exit: **1**. Elapsed: 0.500 s. No timeout or process remains running.

## Impacted axes and smallest safe correction

**Axes:** coverage (a filename and citation count are not learned content), provenance/access (fabricated quotes and nonexistent hosts), relevance/topic (self-authored noun overlap and keyword stuffing), and control discrimination (rejecting apparent structural completeness).

The strongest local counterexample is that **RELEVANCE passes all twenty fabricated rows**, despite LOCATE finding none. Its lexical overlap is therefore not independent evidence of truth or provenance. ACCESS also passes, as its specified purpose is detecting recorded access-control circumvention, not validating URL reachability.

The complete frozen predicate rejects this control. No acceptance-predicate correction is demonstrated as necessary by this run. The smallest safe action is to retain fail-closed, every-row LOCATE and the full conjunction; do not promote RELEVANCE or structural gates into an independent admission authority. BOILER and TOPIC failures here are downstream of non-location, not evidence that their root-page or located-page branches were exercised. No broader saturation or canonical judgment is claimed.

Report: .ufo/waves/round-58/control/CtlJunk58.md
