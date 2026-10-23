# CtlONoArchive — Round 62 wave 1: claim O archive-fallback controls

Seat `KotodamaR62.CtlONoArchive` (leaf, no dispatch). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
branch `main`, jj-colocated. Claims read from `reports/round-62/claims.json` before any fixture existed.

## Scope of this seat

One item from `claims.json` → `controls_required_before_data.O`: the archive-fallback control for
claim O. The brief named three mutants of the tool contract, all "the contract but the archived
capture is mishandled":

1. **first-url-only** — only the first URL of the source cell is tried (the `; capture` copy is never fetched).
2. **archive-host-only** — only a `web.archive.org` capture counts as an archive, so the counter's
   local fixture captures (`/web/<ts>id_/…` served by `127.0.0.1`) are skipped.
3. **archive-first** — the archived capture is tried *before* the live page.

Expected detector (brief): `GEN`/`BOUND` FAIL on `DEAD_ARCHIVE`, `ARCHIVE_CAPTION`, `DEAD_THEN_BODY2`.

**Outcome: the frozen counter detects all three mutants (GEN and BOUND FAIL in every run).**
No archive defect slipped through. One honest independent implementation of the frozen contract
PASSES every leg, so the counter is satisfiable and the failures are attributable to the mutants.

## Method

- Counter under test: the frozen `reports/round-62/accept-o.py`, SHA-256
  `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551` — matches the brief exactly.
- Sandbox: `git clone -q <lane> /fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlONoArchive/clone`
  then `git checkout -q f0173481047a93c46798f90b68d71d4f169d2642`; `git rev-parse HEAD` =
  `f0173481047a93c46798f90b68d71d4f169d4642`… (verbatim: `f0173481047a93c46798f90b68d71d4f169d2642`).
  `GIT_DIR`/`GIT_WORK_TREE`/`GIT_INDEX_FILE` unset. `git status --porcelain` in the clone is empty
  at the end; `clone/tools/reopen-row.py` was removed again (final tool state **ABSENT**).
- **No counter was edited.** The frozen counter was run byte-identical from the clone in every run.
  A clearly-labelled **PROBE copy** of the lane's *in-flight revision-1* counter was used only for
  the supplementary section below: `probe-rev1/accept-o.py.PROBE-rev1`, SHA-256
  `7041054f8c22710fa9f34a958e857f97060a2cf470e9e29364f306670b4fea3a` (diff vs the frozen counter:
  revision-1 caption-class widening, `url=` checking in GEN, DEFAULT burst schedule, ORDER repeated
  ids, EXIT default-registry, ERR both-stream anchoring). The lane's working-tree counter has
  SHA-256 `7041054f…`; the frozen one in the clone has `bfd17a30…`. The brief's frozen SHA is the
  latter, and that is what every receipt below scores.
- Fixtures (all under `/fast/scratch/hyaku/kotodama-r62/CtlondamaR62…` — precisely:
  `/fast/scratch/hyaku/kotodama-r62/CtlONoArchive/`):
  - `probes/base/tools/reopen-row.py` — honest independent implementation of the frozen contract
    (SHA-256 `04c370daeaf3a7e18b74ae35c6460e5870637231e44b240af4b8b4e28f6c1452`).
  - `probes/m1-first-url-only/tools/reopen-row.py` — SHA-256 `caea23d3bc4103bf564dc93367baed11b10ff8d0038b7ec5d0be5136f98f8b32`.
  - `probes/m2-archive-host-only/tools/reopen-row.py` — SHA-256 `36507a26ae15467c7b4255bded6b2aa38762673da4b0bf856be48578abe76123`.
  - `probes/m3-archive-first/tools/reopen-row.py` — SHA-256 `fc03c985fe466aa761dfc744d8ce575bcbd699fcee10d1f4c7d19569a7448bd5`.
  - `probes/gen-mutants.py` (generator), `probes/per-class.py` (per-class diagnostic),
    `roots/<case>/tools/reopen-row.py` (the trees the counter was pointed at),
    `canon/<case>/tools/reopen-row.py` (cwd-relative trees), `logs/` (every run's full stdout).
  The mutants differ from the base in exactly one function (`row_urls`) plus the module docstring;
  the diffs are reproduced verbatim below. Every mutant keeps the bounded retry, the caption/body
  split, the verdict ladder, the exit-code contract and the `--allow-private` refusal, so only the
  archive handling differs.
- Every run was `timeout 900 python3 -B reports/round-62/accept-o.py` (the DEFAULT leg alone needs
  ~150 s of wall time: three passes, two 60 s gaps). No run exceeded the 900 s cap; no process
  tree remains. Random fixtures are generated per run by the unmodified counter (`random.SystemRandom`),
  so S-ids differ between runs — the failing class set was identical in every run of every case.
- **Installs: none.** No tool was installed or upgraded; nothing was needed (`python3` + the
  standard library only). Recorded per the operator tooling directive: tool=none, version=n/a,
  channel=none, reason=no install required.

### The one reporting slip, stated plainly

The appended `RECEIPT` line in `logs/*.run1.txt` … `*.run3.txt` was written by my own harness with
the field `frozen=ACCEPT-O-62: PASS|FAIL` (the counter's whole last line) instead of the required
`frozen=PASS|FAIL`. The counter's stdout is untouched; the receipts section below transcribes
`frozen=` from the counter's own `ACCEPT-O-62:` line, i.e. `PASS`/`FAIL`. `run4` and the
clone-internal and canon runs carry the corrected form in the log itself.

## The mutants (diffs against the honest base)

```diff
--- base/tools/reopen-row.py
+++ m1-first-url-only/tools/reopen-row.py
@@ -1,5 +1,8 @@
 #!/usr/bin/env python3
-"""Re-open registry rows and say where the row's anchor quote lives.
+"""PROBE M1 (control): the contract, but only the first URL of the source cell is tried.
+
+The archived capture listed after `; capture` is never fetched. Everything else (bounded retry,
+caption split, verdict ladder, exit codes) follows the contract.
+"""
@@ -126,8 +129,9 @@
 def row_urls(cells):
-    """The URLs a row lists, in order: the live page first, then any archived capture."""
-    return [trim(url) for url in URL_RE.findall(cells[2])]
+    """M1: only the first URL of the source cell is tried."""
+    urls = [trim(url) for url in URL_RE.findall(cells[2])]
+    return urls[:1]
```

```diff
--- base/tools/reopen-row.py
+++ m2-archive-host-only/tools/reopen-row.py
@@ -1,5 +1,9 @@
 #!/usr/bin/env python3
-"""Re-open registry rows and say where the row's anchor quote lives.
+"""PROBE M2 (control): the contract, but only a web.archive.org capture counts as an archive.
+
+The `; capture` URL of the source cell is used only when its host is web.archive.org; a capture
+listed under any other host is skipped. Everything else follows the contract.
+"""
@@ -126,8 +130,13 @@
 def row_urls(cells):
-    """The URLs a row lists, in order: the live page first, then any archived capture."""
-    return [trim(url) for url in URL_RE.findall(cells[2])]
+    """M2: the live URLs, then only the captures whose host is web.archive.org."""
+    parts = re.split(r";\s*capture\s+", cells[2], flags=re.I)
+    live = [trim(url) for url in URL_RE.findall(parts[0])]
+    capture = [trim(url) for part in parts[1:] for url in URL_RE.findall(part)]
+    kept = [url for url in capture
+            if (urllib.parse.urlsplit(url).hostname or "") == "web.archive.org"]
+    return live + kept
```

```diff
--- base/tools/reopen-row.py
+++ m3-archive-first/tools/reopen-row.py
@@ -1,5 +1,8 @@
 #!/usr/bin/env python3
-"""Re-open registry rows and say where the row's anchor quote lives.
+"""PROBE M3 (control): the contract, but the archived captures are tried before the live page.
+
+The row's URLs are used in reverse order, capture first. Everything else follows the contract.
+"""
@@ -126,8 +129,9 @@
 def row_urls(cells):
-    """The URLs a row lists, in order: the live page first, then any archived capture."""
-    return [trim(url) for url in URL_RE.findall(cells[2])]
+    """M3: the archived captures first, then the live page."""
+    urls = [trim(url) for url in URL_RE.findall(cells[2])]
+    return list(reversed(urls))
```

## Receipts

Format: `RECEIPT <YourName>/<case> counter-sha256=<sha256 of the counter you ran> rev=<rev> frozen=PASS|FAIL exit=<n> stopped-by=<legs that FAIL>`.
The counter is the frozen one (`bfd17a30…`) for every line unless the case name says `rev1-probe`.

```
RECEIPT CtlONoArchive/base counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlONoArchive/base-run2 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlONoArchive/base-run3 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlONoArchive/base-run4 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlONoArchive/base-clone-internal counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlONoArchive/base-canon-cwd counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none
RECEIPT CtlONoArchive/m1-first-url-only counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m1-first-url-only-run2 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m1-first-url-only-run3 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m1-first-url-only-run4 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m1-first-url-only-clone-internal counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m1-first-url-only-canon-cwd counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m2-archive-host-only counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m2-archive-host-only-run2 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m2-archive-host-only-run3 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m2-archive-host-only-run4 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m2-archive-host-only-clone-internal counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m2-archive-host-only-canon-cwd counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m3-archive-first counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m3-archive-first-run2 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m3-archive-first-run3 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m3-archive-first-run4 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m3-archive-first-clone-internal counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m3-archive-first-canon-cwd counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/base-rev1-probe counter-sha256=7041054f8c22710fa9f34a958e857f97060a2cf470e9e29364f306670b4fea3a rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN
RECEIPT CtlONoArchive/m1-first-url-only-rev1-probe counter-sha256=7041054f8c22710fa9f34a958e857f97060a2cf470e9e29364f306670b4fea3a rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m2-archive-host-only-rev1-probe counter-sha256=7041054f8c22710fa9f34a958e857f97060a2cf470e9e29364f306670b4fea3a rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
RECEIPT CtlONoArchive/m3-archive-first-rev1-probe counter-sha256=7041054f8c22710fa9f34a958e857f97060a2cf470e9e29364f306670b4fea3a rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND
```

Run counts: base 6 runs (4 with `--root`, 1 clone-internal, 1 cwd-relative), each mutant 6 runs
(4 with `--root`, 1 clone-internal, 1 cwd-relative), plus 4 revision-1 PROBE runs. 28 counter runs
in total. Sample sizes are uniform; the failing-leg set was identical in every run of every case.

## Verdicts (one per control item)

```
NONE-MET CtlONoArchive/first-url-only fixture=/fast/scratch/hyaku/kotodama-r62/CtlONoArchive/probes/m1-first-url-only/tools/reopen-row.py (sha256 caea23d3bc4103bf564dc93367baed11b10ff8d0038b7ec5d0be5136f98f8b32) — frozen FAIL 6/6, stopped-by=GEN,BOUND
NONE-MET CtlONoArchive/archive-host-only fixture=/fast/scratch/hyaku/kotodama-r62/CtlONoArchive/probes/m2-archive-host-only/tools/reopen-row.py (sha256 36507a26ae15467c7b4255bded6b2aa38762673da4b0bf856be48578abe76123) — frozen FAIL 6/6, stopped-by=GEN,BOUND
NONE-MET CtlONoArchive/archive-first fixture=/fast/scratch/hyaku/kotodama-r62/CtlONoArchive/probes/m3-archive-first/tools/reopen-row.py (sha256 fc03c985fe466aa761dfc744d8ce575bcbd699fcee10d1f4c7d19569a7448bd5) — frozen FAIL 6/6, stopped-by=GEN,BOUND
```

Reading: **NONE-MET** = no cheap fixture that skips the claimed work obtained frozen PASS. The
frozen counter rejected every archive-defective implementation (6/6 runs each), so no counter
change is needed for the archive fallback: the frozen predicate already discriminates it. Had any
mutant PASSed, the smallest counter change that would stop it would have been named here.

Positive calibration (not a control item, reported for the L1's benefit): the honest independent
implementation `probes/base/tools/reopen-row.py` (sha256 `04c370da…`) **PASSES** the frozen
counter 6/6 runs, all nine legs — the harness can pass, so the mutants' failures are caused by the
mutants and not by an unsatisfiable counter.

## What the failures show, class by class

`probes/per-class.py` reuses the frozen counter's own fixture builder (imported read-only from the
clone) to print the expected and the observed verdict/attempts for every class. Full output is in
`logs/per-class.txt`; the decisive rows:

| class | expected | base | m1 first-url-only | m2 archive-host-only | m3 archive-first |
|---|---|---|---|---|---|
| DEAD_ARCHIVE | LOCATED / 2 | LOCATED / 2 | **UNREACHABLE / 1** | **UNREACHABLE / 1** | **LOCATED / 1** |
| ARCHIVE_CAPTION | CAPTION_ONLY / 2 | CAPTION_ONLY / 2 | **UNREACHABLE / 1** | **UNREACHABLE / 1** | CAPTION_ONLY / 2 |
| DEAD_THEN_BODY2 | LOCATED / 4 | LOCATED / 4 | **UNREACHABLE / 9** | **UNREACHABLE / 9** | **LOCATED / 1** |
| the other 15 classes | — | all ok | all ok | all ok | all ok |

Reading the three mutants against the fixture's intent:

- **m1 (first URL only)** and **m2 (web.archive.org captures only)** are the same observable
  defect: the capture is never fetched. The live URL is `403`/`410`/`500` in these classes, so the
  row can only be located through the capture. m1/m2 therefore report `UNREACHABLE` (m1/m2 also
  spend all nine attempts on the dead live URL in `DEAD_THEN_BODY2`, which the contract allows:
  transient results are retried up to three attempts per URL per pass, three passes). m2 is caught
  because the counter's fixture serves the capture from `127.0.0.1` under a Wayback-shaped path
  (`/web/<ts>id_/https://<host><path>`), so a tool that requires the host `web.archive.org` skips
  it — exactly the failure mode the brief predicted.
- **m3 (archive first)** is caught differently: the capture still carries the quote, so the verdict
  is right (`LOCATED`) but the **attempt count and the request schedule are wrong**
  (`LOCATED / 1` instead of `LOCATED / 2` or `/ 4`), and the live URL is never fetched at all.
  BOUND sees it as `live: want=1 hits=0` (and `want=3 hits=0` for `DEAD_THEN_BODY2`).
- **`ARCHIVE_CAPTION` is order-blind.** With the capture first, the tool still makes one request to
  the live URL (`410`, one attempt, not transient) and one to the capture, i.e. the same
  `attempts=2` and the same per-path hit counts as the correct order. This class alone cannot
  detect an ordering defect; `DEAD_ARCHIVE` and `DEAD_THEN_BODY2` do. Worth knowing if the L1
  considers a capture-order-only mutation in a later round: it will be caught, but by the other
  two classes, not by `ARCHIVE_CAPTION`.
- **The frozen counter's other legs are not fooled by any of the three mutants** (`ORDER`, `EXIT`,
  `PRIV`, `DEFAULT`, `ERR` PASS in every run), which is what makes GEN+BOUND the discriminating
  pair for this defect.

## Supplementary (not a receipt against the frozen counter): the lane's revision-1 counter

The lane's working-tree `reports/round-62/accept-o.py` is a *revision 1* (SHA-256 `7041054f…`,
uncommitted in the lane tree) that widens the caption rule to any element whose class or id
contains `caption`, **`thumbnail` or `gallery`**, adds a `url=` check to GEN, adds a DEFAULT burst
schedule, an ORDER repeated-id case, an EXIT default-registry case and an ERR both-stream anchor.
Scored against a clearly-labelled PROBE copy of that file (`probe-rev1/accept-o.py.PROBE-rev1`):

- All three archive mutants are still rejected (`GEN,BOUND` FAIL) — the archive discrimination
  survives the revision.
- **The honest base is rejected too**, and only on the two classes revision 1 added:
  `CAP_CLASS_THUMB` and `CAP_CLASS_GALLERY` (`want=CAPTION_ONLY/1: got=LOCATED/1`). The base
  implements the *frozen* contract, which names only `caption`; it does not treat a
  `class="thumbnail-description"` overlay as caption text. Every other leg passes under revision 1
  (including the new DEFAULT burst schedule `bursts=[3, 3, 3] gaps=[60, 60]` and the new `url=`
  and repeated-id checks).
- Conclusion for the L1: revision 1's caption widening is a **contract change**, not a hole — an
  implementation of the frozen contract is conformant to revision 0 and non-conformant to revision 1
  by construction. Whoever lands `tools/reopen-row.py` must implement whichever caption rule the
  counter will be frozen with; the two revision-1 classes are the exact places where the two
  readings differ, and the S665 live-run rationale quoted in the revision-1 docstring
  (`<p class="thumbnail-description">`) is the reason to prefer the wider rule.

## Risks and blockers

- None blocking. The archive-fallback requirement of claim O is enforced by the frozen counter;
  the L1 needs no counter change for it.
- Standing risk for the L1 (not a defect of the frozen counter): the frozen caption rule names only
  `caption`, while the lane's own revision-1 counter and the S665 live evidence name
  `thumbnail`/`gallery` too. A tool landing under the frozen rule alone will fail the revision-1
  counter on `CAP_CLASS_THUMB`/`CAP_CLASS_GALLERY` (measured above).
- The counter was **not** modified by this seat. The revision-1 PROBE copy lives only under this
  seat's scratch directory and is clearly labelled; it is not a counter revision and no predicate
  was re-scaled. Nothing was committed, pushed, deployed or judged.
- The lane tree was not written to except for this report. `git status --porcelain` in the lane
  shows only other seats' pre-existing changes (`reports/round-62/accept-d.py`, `accept-o.py`,
  `claims.json`, `separability-manifest.json` modified; `.ufo/waves/round-62/`,
  `reports/round-62/locate-control.py`, `reports/round-62/telemetry/locate-control.txt` untracked).
  The lane's `tools/reopen-row.py` is still **ABSENT** (`ls` → No such file), as expected before
  the build wave lands it.
- No network fetches, no archive.org traffic, no credentials touched: every fixture is an offline
  local HTTP server on `127.0.0.1` started by the counter itself.

## Full stdout of every run (verbatim, with exit codes)

### Frozen counter, `--root <tree>` method

```text
@@@ base.run1.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S8143', 'REFUSED', 0), ('S2529', 'REFUSED', 0), ('S4224', 'REFUSED', 0)]
DEFAULT PASS rows=[('S9361', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
@@@ base.run2.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S8362', 'REFUSED', 0), ('S6726', 'REFUSED', 0), ('S9823', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1548', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
@@@ base.run3.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S8866', 'REFUSED', 0), ('S3803', 'REFUSED', 0), ('S5790', 'REFUSED', 0)]
DEFAULT PASS rows=[('S4268', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
@@@ base.run4.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S8822', 'REFUSED', 0), ('S9087', 'REFUSED', 0), ('S3852', 'REFUSED', 0)]
DEFAULT PASS rows=[('S7305', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
@@@ m1-first-url-only.run1.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=6 ["DEAD_THEN_BODY2:S6977:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "ARCHIVE_CAPTION:S8941:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "ARCHIVE_CAPTION:S8435:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S3339:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S9481:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S7645:want=LOCATED/4:got=[('UNREACHABLE', 9)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S9450', 'REFUSED', 0), ('S4051', 'REFUSED', 0), ('S8327', 'REFUSED', 0)]
DEFAULT PASS rows=[('S6812', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
@@@ m1-first-url-only.run2.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=6 ["ARCHIVE_CAPTION:S5183:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S3041:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "ARCHIVE_CAPTION:S4965:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S3693:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "DEAD_ARCHIVE:S1449:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S4824:want=LOCATED/4:got=[('UNREACHABLE', 9)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S9535', 'REFUSED', 0), ('S1318', 'REFUSED', 0), ('S9618', 'REFUSED', 0)]
DEFAULT PASS rows=[('S3212', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
@@@ m1-first-url-only.run3.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=6 ["DEAD_THEN_BODY2:S4548:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "ARCHIVE_CAPTION:S3892:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "ARCHIVE_CAPTION:S4788:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S7456:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S8309:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S1623:want=LOCATED/4:got=[('UNREACHABLE', 9)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S4648', 'REFUSED', 0), ('S7098', 'REFUSED', 0), ('S4562', 'REFUSED', 0)]
DEFAULT PASS rows=[('S7014', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
@@@ m1-first-url-only.run4.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=6 ["DEAD_ARCHIVE:S7765:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S5645:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S8814:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "DEAD_THEN_BODY2:S6724:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "ARCHIVE_CAPTION:S8748:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "ARCHIVE_CAPTION:S2536:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S8683', 'REFUSED', 0), ('S4637', 'REFUSED', 0), ('S9988', 'REFUSED', 0)]
DEFAULT PASS rows=[('S6659', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
@@@ m2-archive-host-only.run1.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=6 ["ARCHIVE_CAPTION:S5613:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "ARCHIVE_CAPTION:S5168:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S7521:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "DEAD_THEN_BODY2:S1435:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "DEAD_ARCHIVE:S8390:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S5586:want=LOCATED/2:got=[('UNREACHABLE', 1)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['ARCHIVE_CAPTION:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S6533', 'REFUSED', 0), ('S1541', 'REFUSED', 0), ('S6015', 'REFUSED', 0)]
DEFAULT PASS rows=[('S8192', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
@@@ m2-archive-host-only.run2.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=6 ["DEAD_ARCHIVE:S5523:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S7369:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "ARCHIVE_CAPTION:S6360:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S2668:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "ARCHIVE_CAPTION:S2640:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S1558:want=LOCATED/4:got=[('UNREACHABLE', 9)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S9215', 'REFUSED', 0), ('S2330', 'REFUSED', 0), ('S3257', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1954', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
@@@ m2-archive-host-only.run3.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=6 ["DEAD_THEN_BODY2:S3289:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "DEAD_THEN_BODY2:S3832:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "ARCHIVE_CAPTION:S4680:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S6639:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S4296:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "ARCHIVE_CAPTION:S7872:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S9670', 'REFUSED', 0), ('S8691', 'REFUSED', 0), ('S8890', 'REFUSED', 0)]
DEFAULT PASS rows=[('S4643', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
@@@ m2-archive-host-only.run4.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=6 ["ARCHIVE_CAPTION:S7401:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S5001:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "DEAD_ARCHIVE:S6312:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S8571:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "ARCHIVE_CAPTION:S3518:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S1622:want=LOCATED/4:got=[('UNREACHABLE', 9)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5367', 'REFUSED', 0), ('S6326', 'REFUSED', 0), ('S1485', 'REFUSED', 0)]
DEFAULT PASS rows=[('S9401', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
@@@ m3-archive-first.run1.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=4 ["DEAD_ARCHIVE:S2740:want=LOCATED/2:got=[('LOCATED', 1)]", "DEAD_THEN_BODY2:S8493:want=LOCATED/4:got=[('LOCATED', 1)]", "DEAD_THEN_BODY2:S4984:want=LOCATED/4:got=[('LOCATED', 1)]", "DEAD_ARCHIVE:S2431:want=LOCATED/2:got=[('LOCATED', 1)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S8155', 'REFUSED', 0), ('S8239', 'REFUSED', 0), ('S2753', 'REFUSED', 0)]
DEFAULT PASS rows=[('S4308', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
@@@ m3-archive-first.run2.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=4 ["DEAD_ARCHIVE:S4831:want=LOCATED/2:got=[('LOCATED', 1)]", "DEAD_THEN_BODY2:S1650:want=LOCATED/4:got=[('LOCATED', 1)]", "DEAD_ARCHIVE:S6019:want=LOCATED/2:got=[('LOCATED', 1)]", "DEAD_THEN_BODY2:S9651:want=LOCATED/4:got=[('LOCATED', 1)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S6312', 'REFUSED', 0), ('S1030', 'REFUSED', 0), ('S3790', 'REFUSED', 0)]
DEFAULT PASS rows=[('S4115', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
@@@ m3-archive-first.run3.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=4 ["DEAD_THEN_BODY2:S9448:want=LOCATED/4:got=[('LOCATED', 1)]", "DEAD_ARCHIVE:S5697:want=LOCATED/2:got=[('LOCATED', 1)]", "DEAD_ARCHIVE:S5527:want=LOCATED/2:got=[('LOCATED', 1)]", "DEAD_THEN_BODY2:S7823:want=LOCATED/4:got=[('LOCATED', 1)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5493', 'REFUSED', 0), ('S2291', 'REFUSED', 0), ('S5004', 'REFUSED', 0)]
DEFAULT PASS rows=[('S4745', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
@@@ m3-archive-first.run4.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=4 ["DEAD_ARCHIVE:S8942:want=LOCATED/2:got=[('LOCATED', 1)]", "DEAD_ARCHIVE:S1188:want=LOCATED/2:got=[('LOCATED', 1)]", "DEAD_THEN_BODY2:S7529:want=LOCATED/4:got=[('LOCATED', 1)]", "DEAD_THEN_BODY2:S8538:want=LOCATED/4:got=[('LOCATED', 1)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S1516', 'REFUSED', 0), ('S3388', 'REFUSED', 0), ('S5056', 'REFUSED', 0)]
DEFAULT PASS rows=[('S8134', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

### Frozen counter, clone-internal method (the fake placed at `clone/tools/reopen-row.py`)

```text
@@@ cloneinternal.base.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S8043', 'REFUSED', 0), ('S3190', 'REFUSED', 0), ('S8290', 'REFUSED', 0)]
DEFAULT PASS rows=[('S3590', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
@@@ cloneinternal.m1-first-url-only.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=6 ["ARCHIVE_CAPTION:S7938:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "ARCHIVE_CAPTION:S9030:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S4235:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S2138:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S6763:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "DEAD_THEN_BODY2:S4834:want=LOCATED/4:got=[('UNREACHABLE', 9)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['ARCHIVE_CAPTION:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S4911', 'REFUSED', 0), ('S6106', 'REFUSED', 0), ('S3269', 'REFUSED', 0)]
DEFAULT PASS rows=[('S5771', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
@@@ cloneinternal.m2-archive-host-only.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=6 ["DEAD_THEN_BODY2:S4717:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "ARCHIVE_CAPTION:S1025:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S6660:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "DEAD_ARCHIVE:S9033:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "ARCHIVE_CAPTION:S2222:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S9077:want=LOCATED/2:got=[('UNREACHABLE', 1)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S9475', 'REFUSED', 0), ('S9678', 'REFUSED', 0), ('S7418', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2957', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
@@@ cloneinternal.m3-archive-first.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=4 ["DEAD_THEN_BODY2:S4073:want=LOCATED/4:got=[('LOCATED', 1)]", "DEAD_ARCHIVE:S9451:want=LOCATED/2:got=[('LOCATED', 1)]", "DEAD_ARCHIVE:S5596:want=LOCATED/2:got=[('LOCATED', 1)]", "DEAD_THEN_BODY2:S5119:want=LOCATED/4:got=[('LOCATED', 1)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S8064', 'REFUSED', 0), ('S3114', 'REFUSED', 0), ('S4806', 'REFUSED', 0)]
DEFAULT PASS rows=[('S3467', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

### Frozen counter, cwd-relative method (no `--root`; the tree is the working directory)

```text
@@@ canon.base.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S4227', 'REFUSED', 0), ('S3818', 'REFUSED', 0), ('S2028', 'REFUSED', 0)]
DEFAULT PASS rows=[('S3479', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
@@@ canon.m1-first-url-only.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=6 ["DEAD_ARCHIVE:S8962:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "ARCHIVE_CAPTION:S5069:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_THEN_BODY2:S4605:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "DEAD_THEN_BODY2:S7446:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "DEAD_ARCHIVE:S1026:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "ARCHIVE_CAPTION:S8197:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_ARCHIVE:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S3253', 'REFUSED', 0), ('S2987', 'REFUSED', 0), ('S8315', 'REFUSED', 0)]
DEFAULT PASS rows=[('S7670', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
@@@ canon.m2-archive-host-only.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=6 ["DEAD_THEN_BODY2:S6318:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "DEAD_THEN_BODY2:S5444:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "ARCHIVE_CAPTION:S7420:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S8882:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S1442:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "ARCHIVE_CAPTION:S4336:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S7383', 'REFUSED', 0), ('S1876', 'REFUSED', 0), ('S1192', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2454', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
@@@ canon.m3-archive-first.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=4 ["DEAD_THEN_BODY2:S5615:want=LOCATED/4:got=[('LOCATED', 1)]", "DEAD_THEN_BODY2:S8319:want=LOCATED/4:got=[('LOCATED', 1)]", "DEAD_ARCHIVE:S9615:want=LOCATED/2:got=[('LOCATED', 1)]", "DEAD_ARCHIVE:S9086:want=LOCATED/2:got=[('LOCATED', 1)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5152', 'REFUSED', 0), ('S3418', 'REFUSED', 0), ('S3823', 'REFUSED', 0)]
DEFAULT PASS rows=[('S8196', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
```

### Revision-1 PROBE copy (supplementary, not the frozen counter)

```text
@@@ rev1.base.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=51 wrong=4 ["CAP_CLASS_THUMB:S5441:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_CLASS_GALLERY:S4869:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_CLASS_GALLERY:S4935:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_CLASS_THUMB:S5764:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]"] summary_ok=False exit=1
ORDER PASS printed=51 expected=51 repeated_args=5 repeated_printed=5
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S4748', 'REFUSED', 0), ('S2099', 'REFUSED', 0), ('S2078', 'REFUSED', 0)]
DEFAULT PASS rows=[('S9846', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
ACCEPT-O-62: FAIL
@@@ rev1.m1-first-url-only.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=51 wrong=16 ["DEAD_THEN_BODY2:S7862:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "DEAD_THEN_BODY2:S7862:url_want=http://127.0.0.1:44069/web/20255634762230id_/https://grkxev.org/etulmxp/yxvbfo/xwsblgoe:got=['-']", "CAP_CLASS_THUMB:S2528:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_CLASS_GALLERY:S6021:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_CLASS_GALLERY:S5236:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "ARCHIVE_CAPTION:S6638:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]"] summary_ok=True exit=1
ORDER PASS printed=51 expected=51 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2563', 'REFUSED', 0), ('S5336', 'REFUSED', 0), ('S3696', 'REFUSED', 0)]
DEFAULT PASS rows=[('S7147', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
ACCEPT-O-62: FAIL
@@@ rev1.m2-archive-host-only.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=51 wrong=16 ["DEAD_ARCHIVE:S2096:want=LOCATED/2:got=[('UNREACHABLE', 1)]", "DEAD_ARCHIVE:S2096:url_want=http://127.0.0.1:34471/web/20258633518850id_/https://xzwva.org/lkuk:got=['-']", "CAP_CLASS_GALLERY:S6542:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "DEAD_THEN_BODY2:S6904:want=LOCATED/4:got=[('UNREACHABLE', 9)]", "DEAD_THEN_BODY2:S6904:url_want=http://127.0.0.1:34471/web/20251569077690id_/https://asqdvhe.org/zkwgs:got=['-']", "ARCHIVE_CAPTION:S9177:want=CAPTION_ONLY/2:got=[('UNREACHABLE', 1)]"] summary_ok=True exit=1
ORDER PASS printed=51 expected=51 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['DEAD_ARCHIVE:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'ARCHIVE_CAPTION:arch:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=0', 'DEAD_ARCHIVE:arch:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S3832', 'REFUSED', 0), ('S5341', 'REFUSED', 0), ('S3046', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1632', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
ACCEPT-O-62: FAIL
@@@ rev1.m3-archive-first.txt
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=51 wrong=8 ["DEAD_THEN_BODY2:S6091:want=LOCATED/4:got=[('LOCATED', 1)]", "CAP_CLASS_THUMB:S3287:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "DEAD_ARCHIVE:S7682:want=LOCATED/2:got=[('LOCATED', 1)]", "DEAD_THEN_BODY2:S2235:want=LOCATED/4:got=[('LOCATED', 1)]", "CAP_CLASS_THUMB:S3516:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_CLASS_GALLERY:S2637:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]"] summary_ok=False exit=1
ORDER PASS printed=51 expected=51 repeated_args=5 repeated_printed=5
BOUND FAIL bad=['DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0', 'DEAD_THEN_BODY2:live:want=3:hits=0', 'DEAD_ARCHIVE:live:want=1:hits=0']
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S9029', 'REFUSED', 0), ('S2465', 'REFUSED', 0), ('S6428', 'REFUSED', 0)]
DEFAULT PASS rows=[('S4650', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
ACCEPT-O-62: FAIL
```

### Per-class diagnostic (`probes/per-class.py`, full output)

```text
=== roots/base
ok  ABSENT         want=ABSENT/1 got=('ABSENT', 1)
ok  ARCHIVE_CAPTION want=CAPTION_ONLY/2 got=('CAPTION_ONLY', 2)
ok  BODY           want=LOCATED/1 got=('LOCATED', 1)
ok  BODY_SPLIT     want=LOCATED/1 got=('LOCATED', 1)
ok  CAP_ATTR       want=CAPTION_ONLY/1 got=('CAPTION_ONLY', 1)
ok  CAP_CLASS      want=CAPTION_ONLY/1 got=('CAPTION_ONLY', 1)
ok  CAP_FIG        want=CAPTION_ONLY/1 got=('CAPTION_ONLY', 1)
ok  DEAD           want=UNREACHABLE/9 got=('UNREACHABLE', 9)
ok  DEAD_ARCHIVE   want=LOCATED/2 got=('LOCATED', 2)
ok  DEAD_THEN_BODY2 want=LOCATED/4 got=('LOCATED', 4)
ok  GONE           want=UNREACHABLE/1 got=('UNREACHABLE', 1)
ok  NOQUOTE        want=NO_QUOTE/0 got=('NO_QUOTE', 0)
ok  NOROW          want=NO_ROW/0 got=('NO_ROW', 0)
ok  PLAIN          want=LOCATED/1 got=('LOCATED', 1)
ok  SCRIPT         want=ABSENT/1 got=('ABSENT', 1)
ok  SHORT          want=NO_QUOTE/0 got=('NO_QUOTE', 0)
ok  TRANSIENT2     want=LOCATED/3 got=('LOCATED', 3)
ok  TRANSIENT_PASS want=LOCATED/4 got=('LOCATED', 4)
=== roots/m1-first-url-only
ok  ABSENT         want=ABSENT/1 got=('ABSENT', 1)
DIFF ARCHIVE_CAPTION want=CAPTION_ONLY/2 got=('UNREACHABLE', 1)
ok  BODY           want=LOCATED/1 got=('LOCATED', 1)
ok  BODY_SPLIT     want=LOCATED/1 got=('LOCATED', 1)
ok  CAP_ATTR       want=CAPTION_ONLY/1 got=('CAPTION_ONLY', 1)
ok  CAP_CLASS      want=CAPTION_ONLY/1 got=('CAPTION_ONLY', 1)
ok  CAP_FIG        want=CAPTION_ONLY/1 got=('CAPTION_ONLY', 1)
ok  DEAD           want=UNREACHABLE/9 got=('UNREACHABLE', 9)
DIFF DEAD_ARCHIVE   want=LOCATED/2 got=('UNREACHABLE', 1)
DIFF DEAD_THEN_BODY2 want=LOCATED/4 got=('UNREACHABLE', 9)
ok  GONE           want=UNREACHABLE/1 got=('UNREACHABLE', 1)
ok  NOQUOTE        want=NO_QUOTE/0 got=('NO_QUOTE', 0)
ok  NOROW          want=NO_ROW/0 got=('NO_ROW', 0)
ok  PLAIN          want=LOCATED/1 got=('LOCATED', 1)
ok  SCRIPT         want=ABSENT/1 got=('ABSENT', 1)
ok  SHORT          want=NO_QUOTE/0 got=('NO_QUOTE', 0)
ok  TRANSIENT2     want=LOCATED/3 got=('LOCATED', 3)
ok  TRANSIENT_PASS want=LOCATED/4 got=('LOCATED', 4)
=== roots/m2-archive-host-only
ok  ABSENT         want=ABSENT/1 got=('ABSENT', 1)
DIFF ARCHIVE_CAPTION want=CAPTION_ONLY/2 got=('UNREACHABLE', 1)
ok  BODY           want=LOCATED/1 got=('LOCATED', 1)
ok  BODY_SPLIT     want=LOCATED/1 got=('LOCATED', 1)
ok  CAP_ATTR       want=CAPTION_ONLY/1 got=('CAPTION_ONLY', 1)
ok  CAP_CLASS      want=CAPTION_ONLY/1 got=('CAPTION_ONLY', 1)
ok  CAP_FIG        want=CAPTION_ONLY/1 got=('CAPTION_ONLY', 1)
ok  DEAD           want=UNREACHABLE/9 got=('UNREACHABLE', 9)
DIFF DEAD_ARCHIVE   want=LOCATED/2 got=('UNREACHABLE', 1)
DIFF DEAD_THEN_BODY2 want=LOCATED/4 got=('UNREACHABLE', 9)
ok  GONE           want=UNREACHABLE/1 got=('UNREACHABLE', 1)
ok  NOQUOTE        want=NO_QUOTE/0 got=('NO_QUOTE', 0)
ok  NOROW          want=NO_ROW/0 got=('NO_ROW', 0)
ok  PLAIN          want=LOCATED/1 got=('LOCATED', 1)
ok  SCRIPT         want=ABSENT/1 got=('ABSENT', 1)
ok  SHORT          want=NO_QUOTE/0 got=('NO_QUOTE', 0)
ok  TRANSIENT2     want=LOCATED/3 got=('LOCATED', 3)
ok  TRANSIENT_PASS want=LOCATED/4 got=('LOCATED', 4)
=== roots/m3-archive-first
ok  ABSENT         want=ABSENT/1 got=('ABSENT', 1)
ok  ARCHIVE_CAPTION want=CAPTION_ONLY/2 got=('CAPTION_ONLY', 2)
ok  BODY           want=LOCATED/1 got=('LOCATED', 1)
ok  BODY_SPLIT     want=LOCATED/1 got=('LOCATED', 1)
ok  CAP_ATTR       want=CAPTION_ONLY/1 got=('CAPTION_ONLY', 1)
ok  CAP_CLASS      want=CAPTION_ONLY/1 got=('CAPTION_ONLY', 1)
ok  CAP_FIG        want=CAPTION_ONLY/1 got=('CAPTION_ONLY', 1)
ok  DEAD           want=UNREACHABLE/9 got=('UNREACHABLE', 9)
DIFF DEAD_ARCHIVE   want=LOCATED/2 got=('LOCATED', 1)
DIFF DEAD_THEN_BODY2 want=LOCATED/4 got=('LOCATED', 1)
ok  GONE           want=UNREACHABLE/1 got=('UNREACHABLE', 1)
ok  NOQUOTE        want=NO_QUOTE/0 got=('NO_QUOTE', 0)
ok  NOROW          want=NO_ROW/0 got=('NO_ROW', 0)
ok  PLAIN          want=LOCATED/1 got=('LOCATED', 1)
ok  SCRIPT         want=ABSENT/1 got=('ABSENT', 1)
ok  SHORT          want=NO_QUOTE/0 got=('NO_QUOTE', 0)
ok  TRANSIENT2     want=LOCATED/3 got=('LOCATED', 3)
ok  TRANSIENT_PASS want=LOCATED/4 got=('LOCATED', 4)
```
