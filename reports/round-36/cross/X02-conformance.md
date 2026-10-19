- Seat: X02 | critic | claim cross | date 2026-10-19 | baseline ce103bf

# X02 — conformance audit: append-only, F-C13-1 prevention, draft-only rule, telemetry readiness

**Mission** (`reports/round-36/targets.json`, seat X02): conformance critic —
append-only discipline, F-C13-1 prevention, draft-only rule.

**Audit instant:** 2026-10-19T09:26:38Z (`date -u +%Y-%m-%dT%H:%M:%SZ`), with
re-checks through 09:31Z. Lane HEAD `ce103bf5885af00023cdc4a174c17602476cdcf8`
(`git rev-parse HEAD`), baseline commit time `2026-10-19T06:21:36-03:00`
(`git log -1 --format=%cI HEAD`). Env `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`.

**Method.** Read-only except where §2.5 says otherwise: git state queries, a
per-file mtime scan over 30 filed rounds, a static AST/text census of all 30
filed runners, the guard's own CLI controls (a tool, not a round runner —
permitted), and the three register legs run read-only against the live D4
packet. No `reports/round-*/run-validation.py` was executed, in-tree or
otherwise, by this seat. Durable output is this file only; the one transient
tree is named in §7.

**Fragment population at audit.** At the first audit instant
(2026-10-19T09:26:38Z) `find reports/round-36 -type f` returned the four
round-level files only (`claims.json`, `targets.json`, `telemetry/
dispatch-declared.json`, `telemetry/availability-attempt-1.json`) — **zero seat
fragments**. Two landed during the audit window: `reports/round-36/cov/C01-audit.md`
and `reports/round-36/depth/D01-design.md` (measured at 09:32Z). §4's scan is
therefore partial; see `## Owed`.

**This is a moving-tree audit, and the tree moved under it.** §1 and §2 below
record the state at 09:26Z; §0a records a filed-byte write that was **in flight
during this seat's own audit window** and is the round's most serious conformance
item. Read §0a before relying on §1.

---

## 0a. HEADLINE — F-C13-1-class breach, RECURRENT: filed receipts rewritten in-tree ≥4 times during the wave

**Status: observed live 2026-10-19T09:26–09:34Z; **still dirty at this seat's
close** (`reports/round-35/validation.json`); record owed. Not repaired by this
seat (§7).**

This is the F-C13-1 shape — *"breached in flight, restored, record owed"*
(`reports/round-33/calib/C13-consistency.md:178`) — but on rounds 34/35 rather
than r5/r6/r7, by a **different mechanism**, and it is **not a one-off**: this
seat captured **three distinct divergent blob states** plus a restored one, and
the r35 receipt was still diverged when this fragment was written.

**This is not a lone reading.** Seat `Ca05` reached the same mechanism
independently in `reports/round-36/calib/Ca05-receipt.md` §1 and §5 (it names
`:10`/`:26` for r34, `:9`/`:36` for r35, `:23` for r33's relocatable form, and
records its own 06:32:04 capture with a `git checkout` containment). Two
independent seats, same defect, same lines.

### The captures (each is a real content divergence, not an mtime touch)

| # | instant (UTC) | file | blob seen | HEAD blob | sha256 | state |
|---|---|---|---|---|---|---|
| 0 | 09:28:15 | `round-34/validation.json` | `e89cd3e0…` | `e89cd3e0…` | `ba2fa4dc…` | written; restored identical (mtime-only) |
| 1 | 09:29:26 | `round-35/validation.json` | `1c30633c…` | `11f241a4…` | — | **diverged** (7,697 vs 7,820 B); restored |
| 2 | 09:32:05 | `round-34/validation.json` | `257b74c9…` | `e89cd3e0…` | — | **diverged** (7,424 vs 7,209 B); restored |
| 3 | 09:33:23 | `round-35/validation.json` | `9b85cd08…` | `11f241a4…` | `8a40245d…` | **diverged — STILL DIRTY at close** |

Mtimes advanced with each write and are the durable trace: r34 now `06:32:16`,
r35 `06:33:23` (both post-baseline; r33 still `03:50:16`).

`reports/round-33/validation.json` was **never written** at any sampling
(mtime `03:50:16`, pre-baseline; blob `4e8089a9…` = HEAD, sha256 `93b28f36…`) —
which is itself the strongest evidence for the root cause, since r33 is the one
relocatable runner.

### Capture 2 is the worst variant: the in-tree write turns a green receipt red

`git diff HEAD -- reports/round-34/validation.json` at 09:32:05:

```
-  "acceptance_checks_passed": true,
+  "acceptance_checks_passed": false,
     "O": { … "passed": true → false,
-      "failures": [],
+      "failures": ["O1-O5: O2: inventory counts differ: 30 runners, {'guarded-refresh': 19, 'unguarded-in-place': 11}"],
-        "guarded-refresh": 18,
+        "guarded-refresh": 19,
-        "status": "green"
+        "status": "failed"
```

The cause is a **stale assertion inside the r34 runner itself**:

```
reports/round-34/run-validation.py:209
    expected_counts = {"guarded-refresh": 18, "unguarded-in-place": 11}
reports/round-34/run-validation.py:210
    if len(runners) != 29 or m["class_counts"] != expected_counts:
```

The filed r34 receipt (`e89cd3e0…` / `ba2fa4dc…`) records `acceptance True`,
`O.passed True`, `guarded-refresh 18` — correct at **its own** measurement
instant (`4a7aede`, when 29 runners existed). At HEAD the live census is **30
runners / 19 guarded** (`reports/round-36/...` runner does not yet exist, so the
two extra are the r34 and r35 runners). So re-running the r34 runner today
**necessarily** produces a red receipt, and if it publishes in-tree it
**overwrites the filed green record with a false red**. That is a worse outcome
than a silent rewrite: it corrupts the historical verdict in the live tree.

This also explains the *benign* environmental reading seat `Ca05` reached
(`Ca05-receipt.md` §4: "Observed in a clone at `4a7aede` with a **clean**
worktree (exactly 29 runners): **29 / 18 / 11** — exactly r34's filed
expectation … **Environmental growth**"). Ca05's diagnosis is correct *for a
clone at `4a7aede`*. My capture adds the in-tree consequence: at HEAD the same
leg goes red, and the runner's publish path writes that red over the filed
green. **Both readings are true of different working trees**; neither is
smoothed.

### Capture 1's diff (r35, the pending-note loss)

- `"X1-X3".measurement` lost its pending-by-construction note
  (`{"manifest": "pending-by-construction: integrator files the MANIFEST row in the same close pass"}`
  → `{}`);
- `"measured_at_utc"` moved `2026-10-19T06:19:14.685566-03:00` →
  `2026-10-19T06:29:26.436020-03:00`.

Capture 3 is the same shape with `measured_at_utc` →
`2026-10-19T06:33:23.601283-03:00`.

**The mtimes are the durable trace** even after a restore: r34 and r35 receipts
carry post-baseline mtimes (`06:28:15`, `06:31:01`, `06:29:59`) while their bytes
match HEAD — the evidentiary shape round 33 filed for r6 ("mtime-only, bytes
never differed", `C13-consistency.md:178`).

**The writer.** A seat's isolated-verification loop, caught live in `/proc` and
`/tmp`:

```
PID 986235  cd .scratch/ca05-iso && export TMPDIR=… REFRESH_RECEIPTS=1
            && for pair in "33 da68a6d" "34 4a7aede" "35 ce103bf"; do …
            sha256sum reports/round-$r/validation.json
            timeout 280 python3 reports/round-$r/run-validation.py … ; done
/tmp/ca05-r34.log: receipt_guard: REFRESH_RECEIPTS=1 permits overwrite path=reports/round-34/validation.json … [RECEIPT-GUARD-REFRESH]
/tmp/ca05-r35.log: receipt_guard: REFRESH_RECEIPTS=1 permits overwrite path=reports/round-35/validation.json … [RECEIPT-GUARD-REFRESH]
                   receipt: reports/round-35/validation.json
```

The seat's intent was isolation (`cd .scratch/ca05-iso`, `REFRESH_RECEIPTS=1` —
the round-34 `O05-routing.md:205` guarded-refresh protocol). **The intent was
defeated by the runners themselves**, which is the finding:

> `reports/round-34/run-validation.py:10-11,26` and
> `reports/round-35/run-validation.py:9-10,36` **hardcode the live repo path**:
> `ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"` followed by
> `os.chdir(ROOT)`.

So `--check` and non-`--check` runs alike relocate to the live tree before any
write, and `out_path = f"{ROUND}/validation.json"` then resolves **in-tree**. An
isolated copy cannot protect these two runners. Every other runner in the
population derives its root relatively — my census over all 30
(`grep -c '^ROOT = "/home'` / `ROOT = Path(__file__)`):

| class | rounds |
|---|---|
| relative root (`ROOT = Path(__file__).resolve().parents[2]`) | 28 runners: 5–33 (r19 uses a different relative form) |
| **absolute hardcoded root** | **only 34 and 35** |

*Caveat on my own census:* the `grep -c` above counts the **string pattern**
`^ROOT = "/home`; my first pass reported "27 relative" because r19 matches
neither pattern (its root is derived by a different relative expression, verified
separately). The load-bearing claim is the narrow one and it is exact: **exactly
two runners hardcode an absolute live path, and they are r34 and r35.**

**Why the guard did not stop it.** The guard is an accident brake, not a sandbox
(`tools/harness/receipt_guard.py:13-14`), and the seat supplied the one value
that disarms it (`REFRESH_RECEIPTS=1`, `:7-8`). The guard reported the write
faithfully in every log; nothing suppressed it. Note the guard *did* stop the
same loop for r33 — the `ca05-r33.log` shows `[RECEIPT-GUARD-REFRESH]` and a
`receipt:` line, yet r33's bytes never moved, because r33's relocatable root
made the write land in the **clone**. The guard is uniform; the runners are not.

**Corroborating convergent evidence.** Independent `/proc` sweeps during the same
window show the same hazard being exercised repeatedly by several seats:
`PID 991199` (`unshare -rm --propagation private` + `mount --bind .scratch/ca03/r35w` over the live
repo), `PID 1000939` (`.scratch/ca04-iso35`, `REFRESH_RECEIPTS=1`),
`PID 1008279` (`.scratch/k03/clone`, `reports/round-34/run-validation.py --check`),
`PID 1005756` (`.scratch/k03/clone`, r33 runner). The `mount --bind` and
`unshare` forms **do** work; the plain `cd <clone>` form **cannot**, for r34/r35.
This is a *route* defect, not a single careless seat.

**Conformance consequence.** The round's ABSOLUTE rule ("never execute any
`reports/round-*/run-validation.py` in-tree — F-C13-1 prevention; isolated
`git archive` copies only") is **BREACHED on rounds 34 and 35, repeatedly**. The
declared counting command for the Ca claim is *re-run every counting command
filed in rounds 33–35* — so the Ca block is precisely the block that touches
these runners, and its own method is what produced the breach. The round's
`non_goals` (`claims.json:36`) also lists "no filed byte rewrites"; that is
breached too.

**Routed to the integrator (this seat does not repair — §7):**

1. **Restore the still-dirty receipt first, then record the incident.**
   `reports/round-35/validation.json` is at `9b85cd08…` / `9a…`-class content at
   this writing, not HEAD `11f241a4…`. Restore it, then file the write + restore
   as a new append-only `LOG.md`/telemetry row naming all four captures: mtimes
   (`06:28:15`, `06:31:01`, `06:29:59`), the divergent blobs (`1c30633c…`,
   `257b74c9…`, `9b85cd08…`), the restored digests, and the writer evidence.
   Exactly the treatment F-C13-1 prescribed (`C13-consistency.md:178`) and that
   r33's C13 found still owed for r5/r6/r7. **A bare "tree clean at close" is
   false at this instant.**
2. **Check whether any *other* seat already re-ran the r34 runner and left a red
   receipt behind that was then restored** — capture 2 shows the publish path
   writes a **false red** over the filed green (§0a). If any seat reported the
   r34 O leg as failed, that report rests on a contaminated run, not on r34's
   actual verdict.
3. **Re-run the Ca recounts under a real namespace or bind-mount**, not a plain
   `cd <clone>`: `unshare -rm` + `mount --bind` (the `ca03` route) is the only
   form that survives r34/r35's absolute `os.chdir`. Seat `Ca05` used a clone +
   `--check` and verified byte-identity afterwards — that worked, but only
   because `--check` returns before the write; the publish path cannot be run
   safely from a clone at all.
4. **File the hardcoded-root defect as its own finding.** The r34/r35 runners
   contradict `O05-routing.md`'s own routing table — R-A ("guarded runner →
   `REFRESH_RECEIPTS=1` refresh") is safe only if the runner honors the copy it
   is run from, and these two do not. A successor runner should adopt
   `ROOT = Path(__file__).resolve().parents[2]` like the other 28. Filed runners
   are never edited; the fix is a new runner generation.
5. **State in the closing snapshot** that the r34 and r35 receipts carry
   post-baseline mtimes, with the reason and the restored digests.

**Limit of this finding.** The mtimes prove the writes happened; the `/tmp` logs
and `/proc` sweeps prove the mechanism; the blob comparisons prove three
divergences were real. I cannot prove *which* concurrent seat produced each
specific write — several seats ran r34/r35 runners in the window (my `/proc`
sweeps caught at least five distinct loops), and seat `Ca05` §5 names a sibling
`.scratch/x01-clone` loop as *its* probable writer. The **mechanism** is
established; the per-write **identity** is `to-verify`. I did not observe the
restoring actions, only their results.

---

## 0b. HEADLINE — claim D's declared `before` is stale and its `after` is already true

This is the conformance item the integrator must disposition before claim D can
be judged at all. It is a **claim-declaration defect**, not a seat defect.

Claim D (`reports/round-36/claims.json`, `claims[0]`) declares:

| field | declared text |
|---|---|
| `before` | "Register-form domain empty (`reports/round-25/argot/` + SCORECARD r25 row); register law/strata exist but the form class has no instances" |
| `after_required` | "register-form domain non-empty with verified forms (**derivation replay clean over the new forms; law gate exit 0 over them; typed pipeline holds**)" |

Both halves are falsified by the live bytes at `ce103bf`, because the register
form class **was built in round 26** and has been present for ten rounds:

| leg (read-only, live `examples/culture-d4/packet.d4.yml`) | command | reading |
|---|---|---|
| derivation replay | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0` — **exit 0** |
| register law | `python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | `law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0` — **exit 0** |
| typed pipeline | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed` — **exit 0** |

The historical before/after is visible in the filed receipts themselves:

| round | receipt | `register_scoped` | `derived_pairs` |
|---|---|---|---|
| 25 | `reports/round-25/validation.json` (`label: argot-gate-d4`, `exit: 0`, `date: 2026-10-18`) | 6 | **0** |
| 26 | `reports/round-26/validation.json` (same command, `date: 2026-10-18`) | 14 | **8** |
| 36 (this audit) | live run above | 14 | **8** |

Round 26 closed it on the record: `SCORECARD.md:329` reads *"The round-17
register forecast CLOSED: the `stamp` attestation register lands in the
delivered furnace-league tree — 8 verified register forms
(tuum/kit/lom/nees/huum/mees/reek/saam) … derivation replay clean (8 derived
pairs, 0 violations over 170 records)"*. Round 25's own leg file
(`reports/round-25/argot/execution-4.md:110`) says the empty-domain reading is a
*"structural pass on an empty register domain"* — a statement about **round 25's
tree**, correctly scoped to it, which the round-36 claim has carried forward as
if it still held.

**Conformance consequence.** Claim D as written cannot verify: its
`after_required` conditions (replay clean, law gate exit 0, typed holds) are
**already true before any round-36 work**, so no round-36 change can move them,
and a runner that asserts them would go green on an unchanged tree. Per
`REGIMEN.md` ("each claim one axis-move … with falsifiable before→after"), the
claim needs a re-declaration naming what is actually still absent. Two
candidates are visible in the filed record and are **not** mine to choose:
(a) the r25 `D4L-ARGOT-COVERAGE` hold — the forecast derivation *relation*
declared but not delivered (`execution-4.md:100`); (b) r26's own named gaps
(`SCORECARD.md:329`: "head2 empty proper domain, syllabify disagreement on
15/62, register law needs a future component"). Either is a real remaining
move; "the domain is empty" is not. Owner: integrator (claim re-declaration,
append-only — never an in-place edit of `claims.json`).

**Also flagged:** the round-36 `before` cites `reports/round-25/argot/` and the
SCORECARD r25 row, but the SCORECARD row at `:329` (r26) already supersedes it
in the same file. A claim that cites the superseded row while the superseding
row sits 17 lines below is the exact staleness shape this seat exists to catch.

---

## 1. Append-only discipline — VERDICT: **HOLDS at 09:26Z, BREACHED REPEATEDLY from 09:28Z, STILL DIRTY at close**

Read §0a first: the 09:26Z readings below are correct for that instant and were
superseded by four filed-receipt writes (09:28:15, 09:29:26, 09:31:01, 09:32:05,
09:33:23 local). At this seat's close `reports/round-35/validation.json` was
**still not byte-identical to HEAD**.

**State at the first audit instant (2026-10-19T09:26:38Z):**

| check | command | result |
|---|---|---|
| index vs HEAD | `git diff-index --quiet HEAD; echo EXIT=$?` | `EXIT=0` |
| worktree vs HEAD | `git diff --name-only HEAD \| wc -l` | `0` |
| untracked | `git status --porcelain` | exactly `?? reports/round-36/` |
| filed-round writes after baseline commit | `find reports/round-{5..35} -type f -newermt "2026-10-19 06:21:36" \| wc -l` | `0` |
| aggregate filed-round fingerprint | `git ls-files $(for i in 5 6 7 $(seq 8 35); do echo reports/round-$i; done) \| xargs sha256sum \| LC_ALL=C sort \| sha256sum` | `a3f7870a95e1f9b13a67b928302c5f109a0bcb55ede1be12af1619ec7526d2ad` |

**State at 09:31Z (during the §0a divergence):**

| check | result |
|---|---|
| `git status --porcelain` | ` M reports/round-35/validation.json` + `?? reports/round-36/` |
| `git diff --name-only HEAD` | `reports/round-35/validation.json` (1 row) |
| filed files newer than baseline | **2**: `reports/round-34/validation.json` (06:28:15), `reports/round-35/validation.json` |

**State at 09:34Z (this seat's close — NOT clean):**

| check | result |
|---|---|
| `git status --porcelain` | ` M reports/round-35/validation.json` + `?? reports/round-36/` |
| `git diff-index --quiet HEAD` | `EXIT=1` |
| r33 / r34 / r35 receipts vs HEAD | r33 `4e8089a9…` YES; r34 `e89cd3e0…` YES; **r35 `9b85cd08…` NO** (HEAD `11f241a4…`, sha256 `8a40245d…`) |
| filed files newer than baseline | **2** — r34 (`06:28:15`→`06:31:01`) and r35 (`06:29:59`) |

**State at 09:30–09:32Z (a transient clean window, mid-recurrence):**

| check | result |
|---|---|
| `git status --porcelain` | exactly `?? reports/round-36/` |
| `git diff-index --quiet HEAD` | `EXIT=0` |
| r33 / r34 / r35 receipts vs HEAD | all three byte-identical (`4e8089a9…`, `e89cd3e0…`, `11f241a4…`) |
| filed files newer than baseline | **2** — the mtimes persist after the bytes were restored |

That clean window is why "restored" must never be reported as "resolved": within
four minutes of it, capture 3 re-diverged r35 and it stayed dirty.

**Fingerprint caveat this seat must state rather than smooth.** `a3f7870a…` is
unchanged across every sampling. That is **not** a green, and the honest reason
is sampling: the fingerprint was computed at 09:26Z (pre-breach), ~09:28Z (after
my sweep run), and 09:33Z (post-restore) — **it never sampled the window
09:29:00–09:29:59Z in which `reports/round-35/validation.json` held
`1c30633c…`**. The instrument would have moved had it sampled the divergence,
since it reads working-tree bytes via `git ls-files | xargs sha256sum`. I record
this as a **sampling limitation, `to-verify`**: a periodic fingerprint cannot
witness a write-and-restore that completes between samples, so §0a's direct blob
comparison (`git hash-object` vs `git rev-parse HEAD:<path>`) is the
authoritative check, and the **mtime** is the durable trace. Any close-time
claim resting on the fingerprint alone must be re-derived from blob hashes plus
mtimes.

The fingerprint was measured **before** the §2.5 in-tree sweep run and again
**after** it: identical value, so the one command this seat ran in-tree wrote
nothing (that command is not the §0a writer). It differs from round 34's
`1713e725…` because rounds 34 and 35 are now tracked and in scope — this is a
new population, not a drift.

**Why mtime, not just git.** `.gitignore:3-4` ignore `*.log` and
`__pycache__/`, so filed `…/run.log` files and stale `__pycache__` trees are
*invisible* to `git status`. The mtime scan covers them. One such artifact is
live and correctly ignored: `reports/round-34/handoff/declared-in-r7/run.log`
(`git status --porcelain --ignored reports/round-34` → `!! …`), and it is
**untracked, not pinned** — `git ls-files reports/round-34/handoff/declared-in-r7/`
returns the five pinned files (`claims-map.md`, `expected.json`, `freeze.txt`,
`packet.md`, `twin.json`) and **not** `run.log`. Its mtime predates the baseline,
so it has not been rewritten either. The r7 pinned bytes themselves are
untouched: `claims-map.md` `d181de28…`, `packet.md` `45f57132…`, `twin.json`
`0e229138…`, `freeze.txt` `3969954b…`, `expected.json` `bbe15887…` — all match
`freeze.txt`'s own declared pins, and no `--freeze` of that directory occurred
(the round forbids it).

No round-36 file records writing a filed path (`grep -rn
"write\|wrote\|edited" reports/round-36/` → only the two rule declarations in
`targets.json:4`, `:20` and the `non_goals` string in `claims.json:36`). The
§0a writer is a seat's scratch loop, not a filed fragment.

## 2. F-C13-1 prevention — VERDICT: **BREACHED on r34/r35 (§0a); HOLDS for the other 28**

### 2.1 Independent 30-runner census (critic-side, static, read-only)

Population: **30 runners** (`ls reports/round-*/run-validation.py | wc -l` → 30;
there is no `reports/round-13/`). My census is independent of the filed
inventory and **matches the live instrument exactly**:

| source | runner_count | guarded-refresh | unguarded-in-place |
|---|---|---|---|
| `reports/round-34/op/adoption-inventory.json` (filed, `date: 2026-10-19`) | 28 | 17 | 11 |
| `python3 tools/harness/receipt_guard_adoption.py --json` (live, now) | **30** | **19** | 11 |
| this seat's AST/text census (independent) | **30** | **19** | 11 |

Guarded: 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33,
**34, 35**. Unguarded: 5, 6, 7, 8, 9, 10, 11, 12, 19, 21, 29.

**The filed inventory is stale by two rows and is now superseded.** Round 34's
`op/adoption-inventory.json` was correct at its read time (28 runners) but
rounds 34 and 35 have since added `reports/round-34/run-validation.py`
(`be11ff46f1fe399cbedcba956d39134a39e25fcfbb74e4b3dc958f2ab47090f9`) and
`reports/round-35/run-validation.py`
(`4ed1ae59386acb8fa17e33dd4d6eba9d7a40581b85f45a33f104529e924bede0`), both
guarded. The unguarded class is unchanged at **11** — no new hazard. The live
instrument self-reports `runner_count: 30`, so re-running it supersedes the
filed file; per the append-only rule that is a **new generation**, not an edit
of `reports/round-34/op/adoption-inventory.json`.

**Unresolved sub-detail, `to-verify`.** My own AST pass found receipt-write sites
by the narrow idiom `write_text`/`open(…,"w")`/`json.dump` on a `validation.json`
literal for only r5`:194`, r6`:336`, r7`:1171`, r19`:21`; the remaining seven
unguarded runners (8, 9, 10, 11, 12, 21, 29) write their receipt through idioms
my narrow grep did not match (the instrument's docstring names the wider set:
`os.replace`/`os.rename`/`shutil.move`/`Path.replace` and subprocess-embedded
strings). The instrument resolves them; my independent pass did not reproduce
those seven sites. This is a **scope limit of my check**, not a disagreement —
the class counts agree exactly, and the instrument's `limits` block states the
same static-analysis caveat. Recorded as `to-verify`, not smoothed.

### 2.2 The absolute rule binds all 30 runners, not only the 11 unguarded ones

`tools/harness/receipt_guard.py:7-8` (docstring): *"Only the exact environment
value REFRESH_RECEIPTS=1 permits a committed receipt write."* An adopted runner
still rewrites its filed receipt in place under that variable — the guard is an
accident brake, not a sandbox (`:13-14`). The round's no-in-tree-execution rule
therefore applies to all 30; the adoption class only governs *which* off-tree
protocol is used.

### 2.3 Guard rail independently confirmed in-tree (tool CLI, not a runner)

```
$ python3 tools/harness/receipt_guard.py reports/round-5/validation.json ; echo EXIT=$?
receipt_guard: refusing overwrite path=reports/round-5/validation.json committed_sha=ce103bf… committed_blob=778c3f5e172405d73eab790b8d6fee4c3282caa0; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]
EXIT=3
```

`main()` (`tools/harness/receipt_guard.py:354-369`) calls `guard_receipt` and
returns — the CLI has **no write path**, so this control cannot mutate a filed
receipt. Confirmed: the §1 fingerprint is unchanged after the run.

### 2.4 Live-process check — this is how §0a was caught

`ps -eo pid,etimes,cmd | grep -E "run-validation" | grep -v grep | wc -l` →
**0** at 09:26Z. **Non-zero at 09:29Z**: an independent `/proc` sweep (walking
every PID's `cwd` and `cmdline`) found **16 live processes** touching filed
runners concurrently, including several running `reports/round-35/run-validation.py`
and `reports/round-34/run-validation.py` from inside `.scratch/` clones. That
sweep is what surfaced the §0a write; the static §1 checks alone would have
missed it, because the tree was clean both before and after the divergence.

The same sweep is a **standing hazard detector for this round**: while a parallel
wave is running, "no runner executing" is only ever true for an instant, and any
in-tree check must name its sampling time. At 09:30Z the wave was still running
(PID 1041554 and others), so §0a's restoration is not evidence that the wave
stopped — only that the bytes converged.

### 2.5 The draft-only rule vs the C claim's second counting command

`reports/round-36/claims.json` claim C lists two counting commands; the second
is `python3 -B reports/round-28/readme/sweep.py` — a **filed round script under
`reports/round-28/`**. This is the sharpest conformance tension in the round and
it deserves an explicit ruling rather than a silent default.

| question | measured answer | evidence |
|---|---|---|
| is it read-only? | **yes** — its docstring states "read-only over the repo: it opens `corpus/README.md` and `corpus/knowledge/**` for reading and has no code path that writes inside the lane"; the only write branch (`:257`, `:397`) is inside its `selftest()` temp-dir fixture builder | `reports/round-28/readme/sweep.py:1-31`, `:240-262` |
| does the round's ABSOLUTE rule forbid it? | **no** — the rule names only `reports/round-*/run-validation.py` (`targets.json:9`); `sweep.py` is not a runner | `reports/round-36/targets.json:9` |
| does it drift the tree when run in-tree? | **no** — I ran it in-tree once; fingerprint `a3f7870a…` before == after; `git status --porcelain` still exactly `?? reports/round-36/` | §1 above |
| is the practice already precedented? | **yes, twice** — `reports/round-33/calib/C03-item-03.md:72,257,345` and `reports/round-33/adj/A05-corpus.md:189-210`/`A12-verify-a04-a06.md:43` both ran it, and A12 explicitly checked the write branch is selftest-confined before doing so | filed fragments |

**Verdict: conformant as declared, with a recommendation.** Because the script is
filed and read-only, running it in-tree neither edits filed bytes nor executes a
runner, so the C claim's command is legal. I nonetheless record that this seat
executed it **both** in-tree and in an isolated `git archive HEAD` copy
(`.scratch/x02-iso/`), with identical readings (`ok True`, `footer_ok True`,
`footer_findings []`, `readme_sha256 51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`)
— so the isolated-copy discipline costs nothing here and is the better default
for any filed instrument. Recommendation to the integrator: prefer the isolated
form for uniformity; do not treat the in-tree form as a violation.

## 3. Telemetry readiness — VERDICT: READY WITH GAPS (2 items owed)

### 3.1 Declared digests verify exactly

```
b8d1af8fd1fb3814e707e24965a6bd404e83158ae26d48d852118d7abec470b8  reports/round-36/claims.json
39ddbc72345d15bc9ec3aa272e161b9e9c7ce652301abca3f55a9c3e28c343d8  reports/round-36/targets.json
48cbee5a4b723dd4eb38230a30086853ed9962d82cc10a7be578434eb72fab16  reports/round-36/telemetry/dispatch-declared.json
ecbcdd4ca880b8acb543386ac21a74817ad54d84ec14e0476dd30ef83e5df1db  reports/round-36/telemetry/availability-attempt-1.json
```

`dispatch-declared.json`'s two `durable_sources` digests match the live files
exactly. Requested-vs-observed separation is honest: allocation is labelled a
declaration, counters for launches/completions/failures/concurrency/route are
**absent rather than inferred zero**, and `closing_snapshot` reads
`"open-at-seat-close: owed once validation.json lands"` per `AGENTS.md` "Close
what you open". No fabricated zero. Compliant.

### 3.2 Seat count 32 == 32 — no round-34-style breach

| source | value |
|---|---|
| `reports/round-36/targets.json:3` `"seat_count"` | 32 |
| `len(d['seats'])` | 32 |
| `grep -o '"id":' reports/round-36/targets.json \| wc -l` | 32 |
| unique ids / unique out-paths | 32 / 32 |
| `claims.json:13` `requested_workers` | 32 |
| role census | executor 12, scribe 6, verifier 4, scout 3, reviewer 3, critic 2, planner 1, connector 1 |
| claim census | D 14, C 6, Ca 6, cross 6 |

Round 34's 64-declared-vs-63-enumerated discrepancy does **not** reproduce.

### 3.3 GAP — the devin (attempt-2) dispatch has no availability record

The round's **actual** route is `devin/deepseek-v4-1-flash-high` (declared
fallback after the hyper 402). The only availability artifact filed is
`availability-attempt-1.json`, which records the **hyper** attempt:
`launched_workers: 0, completed_workers: 0, failed_workers: 32`, failure class
`402 You're out of credits (hyper.charm.land)`, disposition "re-dispatches … as
attempt-2". Nothing on disk yet records attempt-2's own launch/completion
counts, route confirmation, or partial-failure detail. Per `AGENTS.md`
("Keep requested allocation/model separate from observed launches, completions,
failures, runtime concurrency and actual route") and `REGIMEN.md`
("every L2 prompt leads with …"), the devin attempt needs its own observed
record. Owner: integrator, post-batch.

*Observation, not a defect:* `availability-attempt-1.json` reports
`launched_workers: 0` alongside `failed_workers: 32`. That is coherent given its
own `failure_basis` ("all 32 seats failed at launch; zero started") — the seats
were requested, never started. It is a labelling choice worth keeping explicit
rather than a miscount, and the record already explains it.

### 3.4 GAP — no `inputs/` snapshot

`ls reports/round-36/telemetry/` → the two JSON records only. The round-33
convention the closing snapshot must follow is
`reports/round-33/telemetry/{dispatch-declared.json, observed-dispatch.json,
availability-close-33.json, inputs/{claims.json,targets.json}}`. Owed for round
36 post-batch: the observed record, the devin availability sample, and the
redacted `inputs/` snapshot that makes the two declared digests reproducible
after `.scratch` cleanup.

### 3.5 Closing-snapshot digest pins (critic-side close-time reference)

`AGENTS.md` requires the closing snapshot to name the record it closes and that
record's SHA-256 at close time. Reference digests measured at 2026-10-19T09:26Z:

```
48cbee5a4b723dd4eb38230a30086853ed9962d82cc10a7be578434eb72fab16  reports/round-36/telemetry/dispatch-declared.json
ecbcdd4ca880b8acb543386ac21a74817ad54d84ec14e0476dd30ef83e5df1db  reports/round-36/telemetry/availability-attempt-1.json
```

If either differs at close time, that record was edited in place and the closure
is non-conformant. The closing snapshot is additionally gated on
`reports/round-36/validation.json`, which cannot exist until
`reports/round-36/run-validation.py` is authored — **the runner does not exist
yet** (`ls reports/round-36/run-validation.py` → No such file), so no seat can
have satisfied a counting command with it. All three round-36 `counting_commands`
that name `reports/round-36/run-validation.py` (D and Ca claims) are **unrunnable
by construction** until the integrator lands the runner.

## 4. Fragment-level scan — population near-empty at this instant

At 09:26Z `find reports/round-36 -type f` returned only the four round-level
files. Two fragments landed during the audit window (`cov/C01-audit.md`,
`depth/D01-design.md`, measured at 09:32Z), so the population is **2 of 32** at
this writing — 30 seats have not landed. So:

- neither landed fragment records writing a filed path (a `grep -rn
  "write\|wrote\|edited" reports/round-36/` returns only rule declarations and
  the `non_goals` string — see §1);
- the 32 seat out-paths are 32 distinct paths under `reports/round-36/`, all
  inside the permitted write scope (`targets.json:4`);
- the F-C13-1 fragment scan must be **re-run after the batch closes** (`## Owed`),
  and it must be run against a **frozen copy**, not the live tree — §0a shows the
  live tree is writable by seat scratch loops throughout the wave.

## 5. Conformance items for the integrator (ordered)

1. **Record the §0a filed-receipt incident** (highest priority — it is the
   round's only filed-byte breach). Bytes are restored; the *record* is owed.
   Name the mtimes, the captured divergence, the restored digests, the writer
   evidence, and the hardcoded-root mechanism. Do not let a clean `git status`
   stand in for the history.
2. **Disposition claim D's stale `before`/already-true `after`** (§0b). Re-declare
   D against a still-absent move (the r25 `D4L-ARGOT-COVERAGE` relation, or
   r26's named gaps), as an append-only claim revision — never an in-place edit
   of `claims.json`. Until then D is not falsifiable and cannot be admitted.
3. **Re-run the Ca recounts under `unshare -rm` + `mount --bind`**, not a plain
   `cd <clone>` (§0a item 2) — the plain form cannot isolate r34/r35.
4. **File the attempt-2 (devin) availability record** + the observed-dispatch
   record + the `inputs/` snapshot under `reports/round-36/telemetry/` (§3.3,
   §3.4).
5. **Digest-pin the closing snapshot** to
   `dispatch-declared.json` = `48cbee5a…` and
   `availability-attempt-1.json` = `ecbcdd4c…`, or record a new row if either
   changed (§3.5).
6. **Re-run the live adoption census** (`receipt_guard_adoption.py --json`) and
   file it as a **new generation** naming the superseded round-34 inventory; the
   unguarded class stays 11, the population moved 28 → 30 (§2.1).
7. **Re-run §6's audit after the last fragment lands**, then again after the
   integrator's shared-file edits (SCORECARD, LOG, MANIFEST, runner). The §1
   checks must stay at 0 rows, and the **blob-hash** check (not the fingerprint
   alone) must show every filed receipt equal to HEAD.
8. **Do not phrase the adoption instrument as permission to run filed runners
   in-tree** — the guard permits in-place writes under `REFRESH_RECEIPTS=1`
   (§2.2); the absolute rule stands for all 30 runners.
9. **Ruling recorded for the C claim's filed-script command** (§2.5): legal as
   declared; prefer the isolated-copy form for uniformity.

## 6. Re-audit procedure (verbatim, read-only, no runner executed)

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1

# 1. append-only
git diff-index --quiet HEAD; echo "diff-index EXIT=$?"      # expect EXIT=0
git status --porcelain                                       # expect only '?? reports/round-36/'

# 1b. THE AUTHORITATIVE FILED-BYTE CHECK (§0a): blob hash + mtime, per receipt.
#     The fingerprint below CANNOT witness a write-and-restore between samples.
for r in 33 34 35; do f=reports/round-$r/validation.json
  printf "r%s mtime=%s same=%s\n" "$r" "$(stat -c %y $f | cut -d. -f1)" \
    "$([ "$(git hash-object $f)" = "$(git rev-parse HEAD:$f)" ] && echo YES || echo NO)"
done
# expect: r33 03:50:16 YES | r34 06:31:01 YES | r35 06:29:59 ??? 
#         (r34/r35 mtimes post-baseline = the §0a writes)
#         At THIS seat's close r35 read: sha256 8a40245d… blob 9b85cd08… vs HEAD
#         11f241a4… -> same=NO. Restore before any "clean at close" claim.

find reports/round-{5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35} \
  -type f -newermt "$(git log -1 --format=%cI HEAD)" | wc -l   # expect 2 (r34, r35) — NOT 0
git ls-files $(for i in 5 6 7 $(seq 8 35); do echo reports/round-$i; done) \
  | xargs sha256sum | LC_ALL=C sort | sha256sum                 # a3f7870a… — see the sampling caveat in §1

# 2. F-C13-1
ps -eo pid,cmd | grep -E "run-validation" | grep -v grep | wc -l   # expect 0, but sample it repeatedly
python3 tools/harness/receipt_guard_adoption.py --json | python3 -c \
  "import sys,json;d=json.load(sys.stdin);print(d['runner_count'],d['class_counts'])"
  # expect 30 {'guarded-refresh': 19, 'unguarded-in-place': 11} at this HEAD

# 3. the register legs (read-only over the live packet)
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml      # expect exit 0, derived_pairs=8
python3 tools/gates/register-law-gate.py    examples/culture-d4/packet.d4.yml      # expect exit 0, findings=0
python3 tools/gates/typed-pipeline-gate.py  examples/culture-d4/packet.d4.yml      # expect exit 0, 20/20 legs

# 4. telemetry
sha256sum reports/round-36/telemetry/dispatch-declared.json   # compare to 48cbee5a…
sha256sum reports/round-36/telemetry/availability-attempt-1.json  # compare to ecbcdd4c…
python3 -c "import json;d=json.load(open('reports/round-36/targets.json'));print(d['seat_count'],len(d['seats']))"  # expect 32 32
```

**Limit of this audit (stated, not hidden).** §1 detects any content change and
any write to a filed file, including gitignored ones, at its **sampling times**;
§2.4 detects executing processes only while they run. Neither can prove the
*absence* of an in-tree execution of one of the 19 adopted runners under
`REFRESH_RECEIPTS=1` if that execution reproduced the receipt bytes identically
**between samples** — §0a is the proof that this exact failure mode is real this
round, not hypothetical: a write-and-restore completed inside a two-minute
window, leaving only an mtime. For that class the evidence is the mtimes, the
blob hashes, the fragments' declarations, and the guard's refusal path (§2.3).
The 11 unguarded runners are fully covered, because any execution rewrites their
receipt and moves its mtime — but "fully covered" means *detectable*, not
*prevented*. And §4's fragment scan covers 2 of 32 seats at this writing.

## 7. Transient artifacts (declared, no durable value)

All under the gitignored `.scratch/` (`.gitignore:6`): `.scratch/x02-iso/` (the
isolated `git archive HEAD` copy used for the sweep cross-check) and
`.scratch/x02-capture/` (verbatim copies taken at 09:33Z, kept as raw evidence of
§0a). Honest note on the pair: `r35-9b85cd08.json` (sha256 `8a40245d…`) captured
the **divergent** r35 state, but `r34-e89cd3e0.json` (sha256 `ba2fa4dc…`) captured
the **already-restored** r34 state — the restore beat my copy. So the r34
divergence is documented by the `git diff` transcript in §0a and by the mtime,
not by a preserved divergent file. No file outside `.scratch/` and this fragment
was written. **This seat wrote no filed byte and executed no
`reports/round-*/run-validation.py`** in-tree or in a copy; the `/proc` sweep and
`/tmp` logs in §0a were read, never produced.

## Owed

| owed path / item | owner | why |
|---|---|---|
| **restore `reports/round-35/validation.json` to HEAD `11f241a4…`** | integrator | §0a — **still dirty at this seat's close** (`9b85cd08…` / sha256 `8a40245d…`); nothing may be called clean until restored |
| **§0a incident record** (LOG.md + telemetry row: four captures, mtimes `06:28:15`/`06:31:01`/`06:29:59`, divergent blobs `1c30633c…`/`257b74c9…`/`9b85cd08…`, restored digests, writer evidence) | integrator | the round's only filed-byte breach and its recurrence; F-C13-1 precedent (`C13-consistency.md:178`) |
| check for red-receipt contamination of any seat's r34 report | integrator | §0a capture 2 — the in-tree r34 publish writes a **false red** over the filed green; any seat that reported the r34 O leg failed read a contaminated run |
| hardcoded-root finding (r34/r35 runners defeat every plain-copy isolation) | integrator | §0a — needs its own finding row; the fix is a new runner generation, never an edit. Independently reached by seat Ca05 (`calib/Ca05-receipt.md` §1, §5) |
| re-scan of the remaining seat fragments for §2.4/§4 | integrator (or follow-up critic) | fragments still landing; run §6 step 2 against a frozen copy after the batch closes |
| claim D re-declaration (append-only) | integrator | §0b — the declared before is stale and the after is already true; not a seat's to edit |
| `reports/round-36/telemetry/observed-dispatch.json` + attempt-2 (devin) availability record + `inputs/` snapshot | integrator | §3.3, §3.4 — post-batch only |
| closing snapshot, digest-pinned, stating the r34/r35 post-baseline mtimes | integrator | §3.5 — gated on `reports/round-36/validation.json`, which cannot exist until the runner is authored |
| new-generation adoption census superseding `reports/round-34/op/adoption-inventory.json` | integrator | §2.1 — filed inventory is 28 runners; live is 30 |
| the seven unguarded write sites my narrow idiom missed (r8, 9, 10, 11, 12, 21, 29) | this seat / follow-up | §2.1 `to-verify` — class counts agree with the instrument, but my independent pass did not reproduce those sites |
| per-write identification of the r34/r35 writers | follow-up | §0a limit — ≥5 concurrent loops ran these runners; the mechanism is established, the identity is `to-verify` |

## Citations

- `reports/round-36/targets.json:3` (`seat_count: 32`), `:4` (write scope), `:9`
  (the ABSOLUTE runner rule), seat X02 object (mission/out), 32-seat enumeration
- `reports/round-36/claims.json:13` (`requested_workers: 32`), `claims[0]` (claim
  D: `before`, `after_required`, `counting_commands`), claim C's two counting
  commands, `:36` (`non_goals`)
- `reports/round-36/telemetry/dispatch-declared.json` (digests `b8d1af8f…`,
  `39ddbc72…`, `closing_snapshot`), `availability-attempt-1.json` (402 record)
- `reports/round-33/telemetry/{dispatch-declared.json,observed-dispatch.json,availability-close-33.json,inputs/}`
  (the closing-snapshot convention)
- **§0a filed-receipt breach (recurrent):** `git status --porcelain` dirty at
  09:29Z, 09:32Z, 09:33Z, 09:34Z, clean at 09:30Z/09:31:21–09:32:01Z;
  `git hash-object` vs `git rev-parse HEAD:<path>` → r33 `4e8089a9…`=`4e8089a9…`
  (sha256 `93b28f36…`, **never written**), r34 `e89cd3e0…`=`e89cd3e0…` (sha256
  `ba2fa4dc…`) after `257b74c9…` at 09:32:05, r35 `11f241a4…` vs `1c30633c…`
  (09:29) and `9b85cd08…` (09:33, sha256 `8a40245d…`, **still dirty at close**);
  `stat -c '%y'` → `03:50:16` (r33), `06:28:15`/`06:31:01` (r34), `06:29:59`
  (r35); `git diff HEAD -- reports/round-34/validation.json` (capture 2:
  `acceptance_checks_passed true→false`, `O.passed true→false`,
  `status green→failed`, `guarded-refresh 18→19`);
  `git diff HEAD -- reports/round-35/validation.json` (captures 1 & 3:
  `X1-X3.measurement`, `measured_at_utc` → `06:29:26` / `06:33:23`);
  `wc -c` vs `git cat-file -s` (7,697/7,820; 7,424/7,209)
- **§0a capture 2 root cause:** `reports/round-34/run-validation.py:209`
  (`expected_counts = {"guarded-refresh": 18, "unguarded-in-place": 11}`), `:210`
  (`if len(runners) != 29 or m["class_counts"] != expected_counts`), `:242`
  (`"resolvable": 28`), `:250`; live census `30 / {'guarded-refresh': 19,
  'unguarded-in-place': 11}`; filed r34 receipt records `acceptance True`,
  `O.passed True`, `guarded-refresh 18`
- **§0a mechanism:** `reports/round-34/run-validation.py:10-11` (`ROOT =
  "/home/vgpnk/Projects/shokunin/kotodama-shokunin"`, `ROUND = "reports/round-34"`),
  `:26` (`os.chdir(ROOT)`), `:530` (`check_only`), `:532-534` (`out_path = f"{ROUND}/validation.json"`
  then `open(out_path, "w")`); `reports/round-35/run-validation.py:9-10,36,502-504`
  (same shape); contrast `reports/round-33/run-validation.py:23` (`ROOT =
  Path(__file__).resolve().parents[2]`); my 30-runner census
  (`grep -c '^ROOT = "/home'` → abs=1 for r34/r35 only)
- **§0a independent convergence (seat Ca05):**
  `reports/round-36/calib/Ca05-receipt.md` §1 (`:29-33` names r34`:10`/`:26`,
  r35`:9`/`:36`, r33`:23`; `:37-38` the write sites), §4 (`:126-135`, the
  29/18/11 clone reading and "Environmental growth"), §5 (`:146-173`, its own
  06:32:04 capture, the `git checkout` containment, the `.scratch/x01-clone`
  probable writer, "a real, reproducible defect in the isolation protocol"),
  §6 (`:176-178` summary)
- **§0a writer evidence (this seat):** `/proc` sweeps (`/proc/<pid>/cwd` +
  `cmdline`) → PID 986235 (`.scratch/ca05-iso`, `REFRESH_RECEIPTS=1`, loop
  `"33 da68a6d" "34 4a7aede" "35 ce103bf"`), PID 991199 (`unshare -rm
  --propagation private` + `mount --bind .scratch/ca03/r35w`), PID 1000939
  (`.scratch/ca04-iso35`), PID 1008279 (`.scratch/k03/clone`, r34 `--check`),
  PID 1005756 (`.scratch/k03/clone`, r33); `/tmp/ca05-r33.log`, `/tmp/ca05-r34.log`,
  `/tmp/ca05-r35.log` (`[RECEIPT-GUARD-REFRESH]`, `receipt:` lines),
  `/tmp/k03-r34.json` (7,424 bytes); rapid blob sampling 09:31:21–09:32:05
- **F-C13-1 precedent for §0a's shape:** `reports/round-33/calib/C13-consistency.md:178`
  ("breached in flight, restored, record owed"; the r6 "mtime-only" reading),
  `:23`, `:214-236`; `LOG.md:3548-3567`; `reports/round-34/op/O05-routing.md:7-9`,
  `:124`, `:133-136` (B4: "receipt that claims isolation while writing in-tree"),
  `:205` (R-A guarded-refresh), `:212-237` (R-B isolated-copy-only)
- **claim-D staleness (§0b):** `SCORECARD.md:312` (r25 "the register-form domain
  in the delivered D4 packet is EMPTY"), `SCORECARD.md:329` (r26 "The round-17
  register forecast CLOSED … 8 verified register forms … 8 derived pairs, 0
  violations"), `reports/round-25/validation.json` (`records=156
  register_scoped=6 derived_pairs=0`, `label: argot-gate-d4`, `exit: 0`),
  `reports/round-26/validation.json` (`records=170 register_scoped=14
  derived_pairs=8`), `reports/round-25/argot/execution-4.md:100` (the
  `D4L-ARGOT-COVERAGE` hold), `:110` ("structural pass on an empty register
  domain")
- **register legs (live runs, read-only):** `tools/gates/argot-derivation-gate.py`
  → `records=187 register_scoped=14 derived_pairs=8 … violations=0` exit 0;
  `tools/gates/register-law-gate.py` → `law_rows=5 … findings=0` exit 0;
  `tools/gates/typed-pipeline-gate.py` → `20/20 legs passed` exit 0
- **F-C13-1 / guard:** `tools/harness/receipt_guard.py:7-8`, `:13-14`, `:354-369`;
  `tools/harness/receipt_guard_adoption.py` docstring + `--json` (`runner_count
  30`, `class_counts {'guarded-refresh': 19, 'unguarded-in-place': 11}`);
  `reports/round-34/op/adoption-inventory.json` (`runner_count 28`,
  `{'guarded-refresh': 17, 'unguarded-in-place': 11}`, `date 2026-10-19`);
  unguarded write sites r5`:194`, r6`:336`, r7`:1171`, r19`:21` (this seat's own
  pass); `LOG.md:3548-3567` (F-C13-1 incident)
- **draft-only / filed-script question:** `reports/round-28/readme/sweep.py:1-31`
  (read-only docstring), `:240-262` (write branch inside `selftest()`),
  `:411-424` (`main`, no write); `reports/round-33/calib/C03-item-03.md:72,257,345`,
  `reports/round-33/adj/A05-corpus.md:189-210`, `reports/round-33/adj/A12-verify-a04-a06.md:43`
  (prior in-tree runs + the write-branch check)
- **r7 freeze surface:** `reports/round-34/handoff/declared-in-r7/freeze.txt`
  ("read set: 58 files; component digests 26/26; d4 pins 8/8"),
  `expected.json` `inputs` (58 entries, 19 under `examples/culture-d4/`),
  `packet.md:35` (58 read-set files + one inline-payload row), `:72-83`
  (A-34…A-45 = D4 components 01-12), `tools/exercise-handoff-e2e.py:1937-1938`
  (`V3_BASELINE_DEFAULT`/`V3_FROZEN_DIR_DEFAULT`), `:188` (`CLAIMS_MAP`),
  `git ls-files reports/round-34/handoff/declared-in-r7/` (5 pinned files,
  `run.log` untracked)
- **coverage surface:** `for p in …; do ls corpus/knowledge/$p/*.md | wc -l; done`
  → `21 23 24 29 20 94`, total 211; `corpus/README.md:492` (`Total knowledge
  entries: 211.`), `:494` (counts footer), `:502-504` (revision 2.0 moved
  201 → 211); `reports/round-28/readme/sweep.py --json` → `ok True`,
  `footer_ok True`, `footer_findings []`,
  `readme_sha256 51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`
- `REGIMEN.md` (per-round contract: 1–3 falsifiable claims; one batched AgentSwarm
  at declared size; no fabricated sources)
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/AGENTS.md` (append-only;
  telemetry snapshot fields; requested-vs-observed; null-not-zero counters;
  close-what-you-open; the r36-specific telemetry paragraph)
- `.gitignore:3-4` (`*.log`, `__pycache__/`), `:6` (`.scratch/`)
- Commands run (all read-only at `ce103bf` unless noted): `date -u
  +%Y-%m-%dT%H:%M:%SZ` → `2026-10-19T09:26:38Z`; `git rev-parse HEAD`;
  `git log -1 --format=%cI HEAD` → `2026-10-19T06:21:36-03:00`;
  `git diff-index --quiet HEAD`; `git diff --name-only HEAD`; `git status
  --porcelain`; `git status --porcelain --ignored reports/round-{5,34,35}`;
  `find reports/round-{5..35} -type f -newermt "2026-10-19 06:21:36"` → 0;
  `git ls-files <rounds 5-35> | xargs sha256sum | LC_ALL=C sort | sha256sum`
  → `a3f7870a…` (twice, before and after the sweep run); the 30-runner AST
  census python heredoc; `ps -eo pid,etimes,cmd | grep run-validation` → 0;
  `python3 tools/harness/receipt_guard.py reports/round-5/validation.json` →
  exit 3 `[RECEIPT-GUARD-COMMITTED]`;
  `python3 tools/harness/receipt_guard_adoption.py --json`;
  `python3 -B reports/round-28/readme/sweep.py --json` (in-tree, once) and the
  same in `.scratch/x02-iso/`; `sha256sum reports/round-36/{claims.json,
  targets.json,telemetry/*.json}`; the three gate runs in §6 step 3;
  `git ls-files reports/round-34/handoff/declared-in-r7/`
