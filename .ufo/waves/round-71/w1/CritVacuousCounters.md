# Counter-vacuity review: C, Ca, D

## C — entry substance is not counted

**Counterexample:** ACCEPT-C-71 counts the partition size, registry rows, and that the entry's cited-line check exits 0. A 12-row-citing entry can pass while containing only source citations plus a superficial topic/gap line and no meaningful coverage. `check-cited-lines.py` is a clause-scoping lint, not a substance/quality score; the inventory itself warns that line count is not a quality score (`reports/round-71/telemetry/controls-c.txt`, caveat at lines 7–12).

**Smallest safe correction:** Add an explicit structural substance leg to the frozen predicate and counter: require a minimum number of nonempty, substantive `- topic:` entries (e.g. 8, each with a minimum content length), and a minimum number of distinct cited-source bullets within those topic sections (e.g. 12 total). Count only topic content, excluding headings, metadata, and source-list boilerplate. Prefer this combined floor over raw file length, which can be padded. This is a contract/counter change, not merely a recommendation to inspect the entry manually.

**Impacted axis:** coverage (C); the present predicate measures existence/citations, not usable coverage.

## Ca — wrong receipt identity / copy attack

**Counterexample:** The Ca counting command searches `reports/round-71/telemetry/measures-{o,ca,d}.txt` and `controls-{o,ca,d}.txt`—six round-71 paths, not the six round-70 telemetry receipts identified in the claim's V70-1 surface and `before` clause (`reports/round-70/telemetry/measures-{o,ca,d}.txt` and `controls-{o,ca,d}.txt`). The local round-70 telemetry directory contains those six named receipt files; the round-71 telemetry directory currently contains controls only, not round-71 measures (observed via directory listing). Thus a header block on newly created round-71 receipt copies can satisfy the six-file grep without repairing the original V70-1 receipts. The grep also counts matching lines globally per file rather than validating the six required distinct header fields exactly once or ensuring original receipt bytes remain below a marker.

**Smallest safe correction:** Point the six-file check explicitly at the six `reports/round-70/telemetry/{measures,controls}-{o,ca,d}.txt` paths (or use an explicit six-element file list, not a wildcard), and validate each file separately: all six distinct required fields, header block precedes preservation marker, and original payload/hash is preserved. The predicate and receipt must name those exact files.

**Impacted axis:** calibration (Ca), provenance/identity of the repaired records.

## D — no-git exit-2 guard

**Counterexample tested against implementation:** `reports/round-71/accept-d.py` returns 2 only when `_has_git_dir()` is false; this invokes `git -C LANE rev-parse --git-dir`. In the current lane, `.git` exists and that command succeeds (`.git`), so the ordinary in-repository case cannot vacuously take the no-git branch. It is a semantic check for a usable Git repository, not a direct `.git` existence check: a present but malformed `.git` file/directory or an inaccessible/broken git executable can make it return false and report “no git.” That is a narrower diagnostic inaccuracy, not evidence that a normal valid `.git` tree exits 2.

**Smallest safe correction:** If the contract literally means “when `.git` is absent,” make the guard test the lane's `.git` path (including the worktree `.git` file case), and reserve exit 2 for absence. If instead a valid object store is required for the selftest, retain `rev-parse` but describe the condition as “Git repository unavailable,” and distinguish malformed/unavailable Git from absent `.git` in the diagnostic. Preserve the existing successful selftest path whenever rev-parse succeeds.

**Impacted axis:** depth (D), plus correctness of the no-git classification. No ordinary-valid-`.git` vacuous exit-2 counterexample found.
