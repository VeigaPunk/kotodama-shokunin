# RevWaveEvidence — round-66 v2 wave-evidence check (claim Ca, defect D3)

Seat: RevWaveEvidence (reviewer, calibration). Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin
(base 94209e8f80969dbac48d56c5d0e2e623635b8616). Read-only: no lane file, index, .git/.jj or jj state
was written. No tools installed. Findings ordered by severity; every claim cites a path/line I read.

---

## 0. Time-of-read snapshot (the literal ask)

### 0.1 First read — 08:29:5x (wave 64 seats still spawning; `run.stderr` still 0 bytes)

Complete file list under `.ufo/waves/round-66/` at that moment (7 files, 0 seat reports):

```
.ufo/waves/round-66/gen-spec.py                        32800 B  08:28
.ufo/waves/round-66/run.stderr                             0 B  08:29
.ufo/waves/round-66/spec-v2.json                       73163 B  08:28
.ufo/waves/round-66/taskcall-v2.json                   98412 B  08:29
.ufo/waves/round-66/stage/mut-o/mut1_no_partial_exit.py
.ufo/waves/round-66/stage/mut-o/mut2_unresolved_to_base.py
.ufo/waves/round-66/stage/mut-o/mut3_silent_skip.py
.ufo/waves/round-66/stage/mut-o/mut4_suppress_unresolved.py
.ufo/waves/round-66/w1/swarm-registry.json             13410 B  08:29
```

`rows/` and `stage/` existed but `rows/` was empty; `w1/` held only `swarm-registry.json`.
So at wave start: **0/64 seat reports**; every file present is pre-wave instrumentation.
`run.stderr` is 0 bytes (no dispatch-error text is retained anywhere yet).

### 0.2 Later snapshot — 08:34:34 (the dir changed under me while reading)

```
.ufo/waves/round-66/w1/     ConnectorSiblings.md 7984 B, RevBaseCensus.md 13343 B,
                            ScoutPartialOwners.md 7297 B, swarm-registry.json
.ufo/waves/round-66/stage/  execcountersmokeo.md 8.0K, separability-real-probe.txt 4.0K,
                            mut-o/ (pre-wave), mut-o-counter/, mut-c/, mut-reg/,
                            _scratch/, _readme-build/
.ufo/waves/round-66/rows/   0 files
total: 30,515 files, 590 MB under the wave dir
```

4 of 64 seats had produced an artifact (3 depth-1 `w1/*.md` + 1 `stage/*.md` + 1 `stage/*.txt`).
At the last check before this seat returned (08:35:37) depth-1 `w1/*.md` had grown to **14**
(this report included), `rows/` was still empty, and the lane showed
`M tools/check-claim-separability.py` + `?? reports/round-66/` from other seats.
Seats were still running, so this is a snapshot, not a completion verdict — but it is enough to
show the two instrument defects below are structural, not load-related.

---

## 1. HIGH — the D3 leg can never evidence R65-D3, and it penalises honest dead-seat logging

`reports/round-66/accept-ca.py:144-155` implements D3 as:

```python
seat_paths = re.findall(r"(.ufo/waves/round-66/\S+\.md)", d3)       # :146
existing   = [p for p in seat_paths if os.path.isfile(...)]         # :147
reported   = len(seat_paths)                                        # :149
d3_ok = reported >= 8 and len(existing) >= 8 and len(existing) == reported \
        and re.search(r"(?i)(seat|report|status)", d3)               # :150-152
```

Four independent defects, each reproduced against the committed seed
`reports/round-66/telemetry/seat-evidence.txt`:

1. **`existing == reported` turns the ">=8 floor" into "every named file must exist".**
   The seed names **65** paths (64 seat names + the literal placeholder `<SEAT>.md` from its own
   header line `# report: each seat writes .ufo/waves/round-66/w1/<SEAT>.md`). Measured now:
   `named=65 existing=3` → `d3_ok = False`. D3 cannot pass while the placeholder line exists, and
   the only two ways out are (a) editing the Ca land, or (b) creating a file literally named
   `.ufo/waves/round-66/w1/<SEAT>.md` — i.e. a false stamp. A do-nothing integration passes by
   deleting the line; neither outcome is "dispatch evidence".
2. **A dead seat is unrepresentable.** R65-D3 (`corpus/lessons/round-65-verifier-spotcheck.md:78`)
   demands "retain per-seat last-error text for dead seats". Any dead seat's report path is absent,
   so naming it makes `len(existing) < reported` → FAIL. The honest receipt fails; the receipt that
   silently omits dead seats passes. The instrument rewards exactly the omission it was routed to fix.
3. **"per-seat status" and "last-error" are not checked at all.** The only textual guard is one
   case-insensitive substring `(seat|report|status)` over the whole file (`:152`) — the seed's own
   header comments (`# seat report files expected:`) satisfy it. No per-seat status field, no
   last-error field, no count of seats vs lines is parsed.
4. **Existence is the only predicate; emptiness passes.** `os.path.isfile` (`:147`) accepts 0-byte
   files. With the seed trimmed to 8 names, eight `touch`ed `.md` files pass D3 with **zero** seats
   dispatched. Nothing binds a named path to a seat, a dispatch, an agentId or a run.

Aggravating: `w1/swarm-registry.json` cannot stand in for dispatch proof either — all 64 members
have `"agentId": null` and `createdAt == updatedAt == 2026-10-24T11:29:01.355Z`, i.e. the registry
was written once at spawn-plan time and never updated. Its `members=64` is the spec's size, not a
dispatch count (this is also why "registry member count" is not evidence — see RevD3Evidence).

---

## 2. HIGH — 26 of 64 seat prompts never name a `w1/<SEAT>.md`, yet the D3 receipt names all 64

Cross-tabulating `spec-v2.json` prompts against the seed receipt:

* Seats whose own prompt asks for `w1/<SEAT>.md`: **38**.
* Seats whose prompt asks for `stage/*.md` or `rows/*.txt` instead: **26** —
  `ScoutGapScent`, `ScoutRow01-12`, `ScoutReject01-04` (rows), `ScribeEntrySpec`, `ScribeGateRows`,
  `ScribeLessonDraft`, `ScribeReadmePlan`, `ScribeS776Gate`, `ExecCounterSmokeC/O/Ca`
  (`stage/execcountersmokec|o|ca.md`), `ExecSeparabilityReal` (`stage/separability-real-probe.txt`).
* `reports/round-66/telemetry/seat-evidence.txt` nevertheless names a `w1/<SEAT>.md` for **all 64**.

Consequences: (i) if those 26 seats obey their prompts, D3 can only pass after the L1 edits the
receipt's name list down to the 38 w1-writers — and then D3's coverage silently excludes 26 seats;
(ii) `ExecSeparabilityReal` is specified to write **only** a `.txt` (`stage/separability-real-probe.txt`,
present, 4.0K), and D3's regex requires `\.md` (`accept-ca.py:146`), so that seat's artifact can never
be counted no matter what it does. The D3 leg's own docstring (`accept-ca.py:18-20`) says "names >=8
seat report files … that exist on disk" — the implementation is stricter than the text
(`existing == reported`) in one direction and weaker (no status/last-error) in the other, so the
frozen claim's quoted leg text is not what the counter does.

---

## 3. HIGH — D4 accepts a zero-run, degenerate-manifest receipt; the probe file supplies the exact passing shape

`accept-ca.py:157-161` (D4) is a three-token text check:

```python
re.search(r"^SEPARABILITY: \d+ findings$", d4, re.MULTILINE) and re.search(r"acceptance_runs=\d+", d4) \
and "PARTIAL" not in d4
```

`.ufo/waves/round-66/stage/separability-real-probe.txt:24-28` records a real tool run (plumbing
positive control, one WORKTREE unit, exit 0) printing:

```
SEPARABILITY: 0 findings
SEPARABILITY_NOTE units=1 ordered_pairs=0 acceptance_runs=0 skipped=0
```

That is a byte-exact pass for D4 (`^SEPARABILITY: 0 findings$`, `acceptance_runs=0`, no `PARTIAL`
before line 52) while `acceptance_runs=0` means **no dynamic run happened**, and the probe's own
first lines say "BLOCKED, NO VERDICT PRODUCED … This file is NOT the round-66 separability receipt"
(lines 1-5). Copying lines 27-28 into `reports/round-66/telemetry/separability-real.txt` (a Ca land)
satisfies the leg for a run that verified nothing. The leg parses no unit count, no
`ordered_pairs`, no `skipped`, and has no binding to the probe transcript or to the manifest,
so a hand-typed two-line file is indistinguishable from a real 4-unit bounded run.
(The whole-probe copy is blocked only by the incidental token `SEPARABILITY_PARTIAL` at line 52 —
an accident of wording, not a check.) Deeper manifest/run-count analysis is RevD4Bound's; this is the
false-stamp path visible from the evidence directory.

Also load-bearing for whoever writes `separability-manifest.json`: probe section [D] (lines 40-43)
records that in the lane copy `git rev-parse --verify main` == `94209e8f…` (main == base), so any
unit with a new land must declare `"tree": "WORKTREE"` or the run fails with
`SEPARABILITY_INPUT_ERROR`. Probe section [C] shows the manifest_units block as drafted in
`claims.json` fails shape pre-flight (`claims[1].lands[1]` = `.ufo/waves/round-66/stage/mut-o/` is
rejected as non-canonical because of the trailing slash). Those two are integration-blocking for
D4/O and are recorded here because the seat that found them wrote them to `stage/`, not to telemetry.

---

## 4. MED — the wave dir now contains five nested git repos and one nested jj repo inside a tracked tree

`.ufo` is tracked in this lane (2232 tracked files). At 08:34 `git status --porcelain
--untracked-files=normal .ufo/waves/round-66` reports `?? .ufo/waves/round-66/`, and the tree holds:

| path | size | nested repo |
|---|---|---|
| `w1/mut-entry-scratch/` | 130 MB | `.git/` + `.jj/` (full lane copy) |
| `stage/mut-c/` | 141 MB | `fx/.git` |
| `stage/mut-reg/` | 147 MB | `control/.git` |
| `stage/_scratch/` | 171 MB | `fixroot/.git` |
| `stage/mut-o-counter/` | 392 KB | `root/.git` |

Two concrete hazards, not just bloat:

1. **Integration/embed hazard.** The report directory `w1/` contains a full clone (12,033 files,
   including `.jj`). Any broad `git add`/`jj` snapshot of `.ufo/waves/round-66` will either refuse
   ("adding embedded git repository") or record a gitlink to a local path, and will pull ~590 MB of
   duplicate trees into the round's record. The reports themselves are 3 files at depth 1; the
   remaining 30,512 files are scratch. Nothing in the wave contract authorises clones inside `w1/` —
   the contract says seats write "at the exact paths your item names".
2. **Lane-mutation pointer.** `w1/mut-entry-scratch/.git/config` is a real clone
   (`url = https://github.com/VeigaPunk/kotodama-shokunin.git`), but its copied worktree admin keeps
   live pointers into the lane:
   `w1/mut-entry-scratch/.git/worktrees/ca02-wt-r34/gitdir` contains
   `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch/ca02-wt-r34/.git`.
   A `git worktree prune`, `git gc --prune`, or `git worktree add` executed inside that copy can
   therefore touch lane git state, which every seat's rules forbid. `stage/_scratch/fixroot/.git`
   additionally has `url = file:///home/vgpnk/Projects/shokunin/kotodama-shokunin` (a fleet/lane
   root probe). Recommendation: quarantine these directories out of the lane before the L1 commits
   (move to `/tmp` or delete), and keep mutant scratch outside `w1/`.

By design, non-`.md` artifacts are expected and legitimate — `rows/<SEAT>/row-S*.txt`,
`rows/<SEAT>/rejects.txt`, `stage/*.txt` (the claim C scouts and `ExecSeparabilityReal` are told to
write them). The finding is not that `.txt` exists; it is that D3 counts only `.md` (§2) while the
wave's own design makes `.txt` the primary artifact for 15 seats.

---

## 5. CLEAN (checked, no violation) — no seat prompt asks for a write outside `.ufo/waves/round-66/`

I scanned all 64 prompts for write verbs near `corpus/`, `reports/`, `tools/` paths. Every write
target named is under `.ufo/waves/round-66/` (`w1/`, `stage/`, `rows/`). The lane-relative mentions
are read-only or explicitly non-mutating:

* `ScoutRow01` … `ScoutReject04`: `corpus/SOURCES.md` appears only as a grep target
  ("grep it against corpus/SOURCES.md and all fragments"); the row template names the entry path as
  the future `used-by` value, not as a write.
* `ScribeEntrySpec`/`ScribeLessonDraft`/`ScribeReadmePlan`: read `claims.json`, `corpus/README.md`,
  `corpus/lessons/round-65.md`; write only `stage/*.md`.
* `MutEntry`/`MutRegistry`/`MutCounterC`/`MutCounterO`/`MutTool`: mutate **copies** under `stage/`
  ("never the committed file").
* `SentinelScope` states the allowed roots (`reports/round-66/`, `.ufo/waves/round-66/`, claim
  land paths) as a guard, not as a write instruction.
* `ExecSeparabilityReal` is told to record into `stage/separability-real-probe.txt` and explicitly
  "Do NOT edit lane files" — correct, though it means the Ca land
  `reports/round-66/telemetry/separability-real.txt` has **no specified producer**; the L1 must
  write it, which is exactly the false-stamp surface in §3.

**Root-form divergence (low, but the misrooting class is real).** `gen-spec.py:19` and the seat's
own trailer say the `Report:` trailer is rendered relative to
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` and give an absolute lane path, while the
artifact `taskcall-v2.json` carries a *relative* trailer
(`Report: write your scoped findings to .ufo/waves/round-66/w1/<SEAT>.md`). The rendered
assignment I received had the absolute lane path, so the harness resolved it correctly this round.
Checked for the failure mode anyway: `/home/vgpnk/Projects/shokunin/.ufo/waves/round-66` does not
exist at 08:31 → **no misrooted reports yet**. Flagging it because a relative trailer resolved at
the fleet root would produce reports invisible to D3 (`os.path.isfile` under `root`), i.e. dispatch
would look dead.

---

## 6. Seat-by-seat report presence (snapshot 08:34:34)

Expected = the artifact path the seat's own prompt names; "w1 prompt?" = whether that path is
`w1/<SEAT>.md` (the only form D3 can count).

| class | seats | expected artifact | present at 08:34 |
|---|---|---|---|
| w1-report seats | 38 (all reviewers, critics, 4× mut, 2× revenger, sentinel, connector, simplifier, RevIntegrity, …) | `w1/<SEAT>.md` | 3 (`ConnectorSiblings`, `RevBaseCensus`, `ScoutPartialOwners`) |
| row scouts | 16 (`ScoutGapScent` + `ScoutRow01-12` + `ScoutReject01-03`) | `rows/<SEAT>/…txt` (GapScent: `rows/…/gap.md`) | 0 |
| stage scribes/executors | 9 (`Scribe*` ×5, `ExecCounterSmokeC/O/Ca`) | `stage/*.md` | 1 (`execcountersmokeo.md`) |
| separability executor | 1 (`ExecSeparabilityReal`) | `stage/separability-real-probe.txt` | 1 (present, self-declares BLOCKED) |

No seat returned a file with no findings: the three depth-1 reports carry verdicts
(`RevBaseCensus` 2 finding/verdict headings, `ScoutPartialOwners` 1, `ConnectorSiblings` 0 explicit
"finding" heading but a full per-sibling ownership verdict table — not a stub). No 0-byte report was
present at snapshot time; the empty-file attack in §1.4 was constructed from the code path, not from
an observed seat.

---

## 7. Residual risk and verification gaps

* **Wave in flight.** The per-seat table is a 08:34:34 snapshot; 60 of 64 seats had no artifact yet.
  I did not re-poll after 08:34 (and did not block on peers). The D3-unsatisfiability finding does
  not depend on arrival order: it follows from the seed's 65 named paths vs 38 w1-prompted seats.
* **Not run:** `reports/round-66/accept-ca.py` end-to-end (its D2 leg shells to git; and D3's outcome
  was reproduced exactly by applying its own regex/isFile predicate to the committed seed — `named=65
  existing=3`). I did not run `accept-c.py`, `accept-o.py`, or the separability tool (other seats own
  those; the probe transcript is the evidence I cite). No network fetches were made.
* **Deps recorded, not waited on:** `reports/round-66/separability-manifest.json` is absent (probe
  agrees); `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` and
  `corpus/lessons/round-66.md` are absent; `reports/round-66/telemetry/separability-real.txt` is
  absent. The planned `/tmp/r66-probe-copy` (1019 MB, `.jj` excluded) was not inspected by me.
* **What a closure must add to D3 to be honest** (beyond this round's exit): bind each named path to
  an agent id + a non-empty findings token, allow a `status=dead` line **without** a report path,
  and compare the count to the dispatched list rather than the spec list. As written, D3 can be
  satisfied by 8 `touch`ed files and a one-line receipt, or failed by an honest dead-seat note.
