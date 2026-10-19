- Seat: D20 | verifier | claim D | date 2026-10-19 | baseline da68a6d

# D20 — independent verification: D11's preservation claim + the D05 draft's stale figures

Mission (targets.json, seat D20): "Verify D11's preservation claim with your own
git commands; verify the D05 draft contains zero occurrences of the six stale
figures (74, 56-as-native-form, 16-as-findings, 15-as-hold, conflicts 4,
quarantine 3 in their stale contexts)."

Everything below was produced by this seat's own commands at the instants named.
No filed-round file was written by me; no `reports/round-*/run-validation.py` was
executed (F-C13-1); all runs used `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1` from the repo root.

## 0. What was available when I ran

| artifact | state at my dispatch | consequence |
|---|---|---|
| `reports/round-34/depth/D11-preservation.md` | **landed** (first read: 253 lines, sha256 `31f6848e…`; re-read at close: **340 lines**, `5bab52e5…`) | §1–§2 verify it |
| `reports/round-34/depth/D05-packet-draft.md` (my named object) | **absent** at 04:00, 04:03, 04:07, 04:12 (polled) | §3 ran instead against the draft **instance** D05 rendered into `.scratch/d05/declared-in-r7/` — see §3.1 and `## Owed` |
| `reports/round-34/handoff/declared-in-r7/` (the filed revision) | **absent** | §4 is therefore a pre-filed-build instant; the post-build re-run is owed |
| `reports/round-34/run-validation.py` | **absent** (as the shared rules state) | not run, nothing to run |

D11's mission was to *make* the preservation proof; mine is to *verify* it. I
therefore re-derived every number in it from scratch rather than reading its
conclusions: §1 is a claim-by-claim re-run, §2 adds three honesty checks D11 did
not perform (index-flag masking, filter divergence, index-vs-HEAD).

## 1. D11's preservation claim, re-run claim by claim

Baseline of record: HEAD = `da68a6d705e41f369f21e8607bfaab5b54077f84`
(`git rev-parse HEAD`), i.e. exactly the declared `baseline_commit: "da68a6d"`
(`reports/round-34/claims.json:7`). Working tree is at that commit, so every
comparison below is "on-disk vs the filed bytes".

| # | D11 asserted | my command | my observation | verdict |
|---|---|---|---|---|
| 1 | tree clean vs HEAD | `git diff-index --quiet HEAD; echo EXIT=$?` | `EXIT=0` | **confirmed** |
| 2 | 29/29 filed rounds with 0 changed rows | `for i in 5 6 7 $(seq 8 33); do git diff --name-only HEAD -- reports/round-$i \| wc -l; done` | 29 rounds, every count `0` | **confirmed** |
| 3 | 1909/1909 blob identities | raw `sha256`-of-disk vs `git hash-object` vs `git ls-tree da68a6d` blob, over a **wider** set: all of `reports/round-1..33/**`, `corpus/lessons/**`, `tools/gates/frozen/**` | `filed_paths_checked: 2325`, `mismatched_vs_baseline: 0`, `missing: 0` | **confirmed and extended** (their 1909 is the `reports/round-5..33` subset; my 2325 covers every filed surface named in the shared rules) |
| 4 | `git ls-files 'reports/round-*' \| wc -l` = 1909 | same | `1909`; and the round-5..33 enumeration is also `1909` | **confirmed** (the two sets are equal at this instant because round-34 is untracked) |
| 5 | 5 revision freeze digests re-computed, matching | `sha256sum` of each `packet.md` vs its `freeze.txt` `packet_sha256` | r2 `a97a0f0a…`, r3 `084dc5db…`, r4 `5f58db4a…`, r5 `e3fb1ca5…`, r6 `6ced88ad…` — **5/5 match on-disk** | **confirmed** |
| 6 | twin digests r2/r5/r6 match; r3/r4 have no twin.json | `sha256sum` + `test -f` | r2 `d3de56a8…`, r5 `b849e2f9…`, r6 `6633443d…` match their `twin_sha256` lines; r3 and r4 have **no** `twin.json` (their `freeze.txt` carries `parent_packet_sha256` + `validator_binding` instead) | **confirmed** |
| 7 | r5/r6 `re-frozen packet_sha256:` chain intact | `grep re-frozen freeze.txt` | r5 `69ce3877… -> e3fb1ca5…`; r6 `ec30b11f… -> 6ced88ad…`; both agree with on-disk bytes | **confirmed** |
| 8 | expected.json digests (5 rows) | `sha256sum` | all 5 identical to D11's table, char for char (`4879e760…`, `737e5484…`, `c2d4eb7a…`, `855603f6…`, `ea1e2927…`) | **confirmed** |
| 9 | set fingerprint `1713e725…` | `git ls-files $(for i in 5 6 7 $(seq 8 33); do echo reports/round-$i; done) \| xargs sha256sum \| LC_ALL=C sort \| sha256sum` | `1713e725abbd3a73b03ff2e42a8774adcd9b8c294c458f25d4657065b126ce71` — exact match | **confirmed** |
| 10 | 0 filed files with mtime after the commit | `git log -1 --format=%cI HEAD` → `2026-10-19T03:52:53-03:00`; `find <rounds 5..33> -type f -newermt <that>` | `0` | **confirmed** |
| 11 | `reports/round-2`, `reports/round-4` do not exist; revision homes are rounds 22/23/25/26/30 | `test -e` ×4; `git ls-files 'reports/**/declared-in-*'` | all four paths `ABSENT`; homes exactly `reports/round-22/handoff/declared-in-r2`, `reports/round-23/wording/declared-in-r3`, `reports/round-25/v3-supersession/declared-in-r4`, `reports/round-26/handoff/declared-in-r5`, `reports/round-30/handoff/declared-in-r6` | **confirmed** (D11's path correction is right) |
| 12 | "30 round dirs on disk vs 29 in HEAD" | `ls -d reports/round-*` vs `git ls-tree --name-only HEAD reports/` | `30` vs `29` — the extra one is the untracked `reports/round-34/` | **confirmed** |

**Unprovable as stated (not a defect):** D11 pins its own pre-closing digest
`b6ba30c9…`. That version no longer exists on disk — the fragment was extended to
340 lines after my first read — so I **cannot** reproduce it (`to-verify` by
construction; sha256 is not invertible). D11 already says this is not a fixed
point and asks the integrator to pin the final digest. Current digest at my close:
`5bab52e3583983b55365459cc39507eaffad2f1e25371f65b72afddb85952a12`. Nothing in
D11's *preservation* argument depends on that self-pin.

## 2. Hardening: three ways `git diff` could have lied, all checked

D11's proof rests on git's view of the worktree. That view can be disabled without
any visible trace, so I tested the three mechanisms explicitly:

```
$ git ls-files -v reports/ corpus/lessons/ tools/gates/frozen/ | grep -vc '^H '
0                       # no assume-unchanged ('h') and no skip-worktree ('S') entries
$ test -f .gitattributes && cat .gitattributes || echo "(none)"
(none)                  # no clean/smudge filters, so raw bytes == blob bytes
$ git diff --cached --name-only HEAD | wc -l
0                       # index itself is not staged away from HEAD
$ git config --get core.filemode
true                    # a mode change on a filed file would be reported
```

Combined with §1 row 3 (raw sha256 of the on-disk bytes equals the blob recorded in
the `da68a6d` tree), this closes the "git says clean but the bytes moved" route:
there is no index flag that could hide a modification and no filter that could make
`hash-object` diverge from the raw bytes I hashed myself.

**Verdict on D11's claim: verified, not merely reproduced.** All 12 checkable
assertions hold; the single unverifiable item is a self-pin D11 itself disclaims.
Claim D's preservation half ("filed rounds 8-33 and r2/r4/r5/r6 packet bytes
untouched", `reports/round-34/claims.json:30`) holds at the pre-build instant and,
per §4, still held at 04:13:18 — after 46 seat fragments had been written into
`reports/round-34/`.

## 3. The D05 draft against the six stale figures

### 3.1 The object I verified (and why it is not the fragment)

`reports/round-34/depth/D05-packet-draft.md` did not exist after four polls
(04:00 → 04:12). D05's seat did render its draft, into its own scratch tree:

```
.scratch/d05/declared-in-r7/packet.md   106,667 B  sha256 10ac976622f6bad615c897ffe3ef9d8aff9908a3ba7d7bea9b61361bc3b799f5  mtime 04:09
.scratch/d05/declared-in-r7/twin.json   104,714 B  sha256 80be664d92b4b6bfa435cceb753f48ff3e5223741a618d8c7ee6787bfa060e31  mtime 04:09
```

I verified **that instance**, because it is the only rendered r7 draft that exists
and it is materially different from r6 (106,667 B vs 105,584 B; digest 10ac9766… vs
6ced88ad…). It is *not* durable (`.scratch/` is gitignored — `git check-ignore -v`
→ `.gitignore:6:.scratch/`), and it is not the fragment the integrator will
consume. **The same command must be re-run on the durable draft** — see `## Owed`.

### 3.2 The scanner, and the false-positive trap that makes an un-scoped scan wrong

The six figures are *D4* figures. The identical digits are **live and correct** in
the same files for the D2 channel, which I measured myself:

```
examples/culture-d2/typed-labels.d2.yml#coverage (read at da68a6d):
  typed_labels 58 · native-form 46 · translated-label 10 · borrowed-strata 2
  findings_total 16 · findings_hold_or_fail 15 · label_findings_hold 10 · label_findings_fail 2
  conflicts 4 · rank_quarantine_handles 3 · rank_rules_unresolved_items 13 · reconciliation_records 10
examples/culture-d4/typed-labels.d4.yml#coverage (live, the ground truth the draft must carry):
  typed_labels 82 · native-form 64 · translated-label 12 · borrowed-strata 6
  findings_total 12 · findings_hold_or_fail 12 · label_findings_hold 12 · label_findings_fail 0
  conflicts 0 · rank_quarantine_handles 0 · rank_rules_unresolved_items 0 · reconciliation_records 6
  rank_rules_component 4 · rank_rules_normalized 4 · rank_rules_gate_projected 4
examples/culture-d4/expected-holds.json#counts: {"hold": 12, "note": 0, "fail": 0}, 12 rows
```

So a naive "count the digits 74/56/16/15/4/3" scan hits correct D2 rows and would
"succeed" by mutilating live numbers. My scanner therefore (a) matches figure
patterns, (b) attributes each hit to D4 or D2 by the artifact path the line cites,
and (c) reports the two classes separately. D16 §2 reached the same rule
independently, at a coarser grain; §3.4 needs one more grain (assertion vs
re-attribution), which is where the interesting result is.

I also had to fix one of **my own** patterns before trusting it: an alternative
`hold-or-fail\s*\(\s*1[0-9]` fires on the *live* wording
`…all 12 are hold-or-fail (12 label holds, 0 label fails)` that D05's draft
actually uses. Removed. Scanner source is inlined in §5 so the integrator reruns
the exact discriminating version, not a remembered approximation.

### 3.3 Controls

| control | artifact (sha256) | expected | observed |
|---|---|---|---|
| positive — filed default is stale | `reports/round-30/handoff/declared-in-r6/packet.md` (`6ced88ad…`) | flags > 0 | **11 D4 flags** — S1 1, S2 1, S3 1, S4 2, S5 3, S6 3 — plus 4 D2-attributed live rows correctly excluded |
| positive — older filed revisions still stale | r2 `a97a0f0a…` / r4 `5f58db4a…` | flags > 0 | r2: **15** (its `A-30` manifest row is stale too, `:68`), r4: **11** |
| positive — same content under a different path | `.scratch/d08/declared-in-r7/packet.md` (`6ced88ad…`, byte-identical to r6) | identical flags to r6 | **identical 11** — belt-and-braces on the discriminator |
| alignment — the new claims map | `.scratch/d15/…/declared-in-r7/claims-map.md` (`f71751e0…`) | D4 rows live-accurate | **1 hit only**: `:115` `…reports/round-18/d4/holds.md's reading of 15 holds / 1 note stands filed as a superseded measurement` — a supersession note, with live `hold 12, note 0, fail 0` asserted at `:114` |
| negative — my own trap | the four D2 rows in every packet above | must not be flagged as stale | correctly classed `D2-attributed` (`:49` A-11, `:129` D2-CL01, `:266` RD-D2-01, `:284` D2 read-only facts) |

### 3.4 Result on the D05 draft: 0 stale *assertions*

```
.scratch/d05/declared-in-r7/packet.md   FLAGGED_LINES=4   D2-attributed-rows=4
   S1 typed_labels=74     0
   S2 native-form=56      0
   S3 findings_total=16   0
   S4 hold=15             0
   S5 conflicts=4         2      (lines 152, 307)
   S6 quarantine=3        2      (lines 152, 307)
.scratch/d05/declared-in-r7/twin.json   FLAGGED_LINES=6   D2-attributed-rows=2
   S1 0  S2 0  S3 0  S4 0
   S5 3   (1156, 1158, 2620)     S6 3   (1156, 1158, 2620)
```

Four figures are gone **outright**: the draft asserts `typed_labels 82`
(`:148`, `:285`), `native-form 64`, `findings_total 12` / `findings_hold_or_fail 12`
(`:148`), and `hold 12, note 0, fail 0` (`:149`). Each of those four is the value I
measured live in §3.2, so the four S1–S4 figures are corrected value-for-value.

The ten surviving `conflicts 4` / `quarantine 3` occurrences are **not stale
contexts** — they are the re-attribution claim D required. Each one sits in a
clause that names the owner as D2 and asserts the live D4 value in the same line:

- `:152` D4-CL09 — "…(rank_rules_component 4, rank_rules_normalized 4,
  rank_rules_gate_projected 4), with zero act rules, zero residuals, **zero
  unresolved rank items, zero quarantine handles and zero conflicts** …; open: the
  thirteen unresolved rank items, three quarantine handles and four conflicts the
  pre-family-clean generation inherited **are no longer D4-owned** and were not
  resolved in D2, where they stay open (**OQ-V2-03**)"
- `:307` OQ-V3-05 — "**D4's own holds stay open: twelve form holds, zero rank holds,
  zero notes and zero fails**; the thirteen unresolved rank items, three quarantine
  handles and four conflicts recorded by the pre-family-clean generation **are
  D2-owned residuals, removed from D4 ownership** … and still open in D2 (OQ-V2-03)"
- twin `:1156`/`:1158`/`:2620` — the same two sentences verbatim (twin parity holds:
  the twin is a faithful projection of the Markdown on these rows)

Assertion-level classifier over all ten occurrences, requiring **both** a D2-owner
phrase **and** a live D4 assertion on the same line:

```
S5+S6 occurrences in D05 draft: 10 | stale-level failures: 0
```

**Verdict: PASS — zero occurrences of the six stale figures in stale (D4-asserted)
contexts.** Two limits on that verdict, stated so the integrator can weigh it:
(i) it is a verdict on the scratch instance §3.1 names, not on the durable draft;
(ii) it is a verdict on the **six figures my mission names plus the 13/3/4 they
travel with** — it is not a proof that every figure in the draft equals a live
value. `A-30` (`:68`: `82 labels (64 native-form / 12 translated-label / 6
borrowed-strata), 12 findings, 0 unresolved rank items, 4 era-alias rows`) and the
D4 read-only card (`:285`) both read live in the draft, and the D2 surfaces
(`:49`, `:129`, `:266`, `:284`, `:301`) all match my D2 measurement in §3.2
value-for-value, but the exhaustive per-figure audit of all 27 ledger rows is
D03/D18's leg, not mine.

### 3.5 Corroboration of the D01/D16 blocking finding (independent, partial)

D01 §1 and D16 §4 report that a fresh render from today's live artifacts
reproduces r6 **byte for byte**, because the twelve D4 claim rows are copied out of
the *filed* `reports/round-20/handoff/claims-map.md`
(`tools/exercise-handoff-e2e.py:184`) — so "regenerate the packet" in claim D's
`after_required` cannot clear the staleness by itself. I can confirm the
byte-identity half of that from my own `sha256sum`: `.scratch/d08/declared-in-r7/packet.md`
is `6ced88ad…`, identical to `reports/round-30/handoff/declared-in-r6/packet.md`,
with all 11 D4 stale flags intact. What I did **not** verify is the render path
that produced it (I did not re-run the renderer), so the causal half
(`CLAIMS_MAP` → verbatim copy) is `to-verify` from this seat and stays D01/D16's
claim. Consequence for my mission: the draft that clears the staleness must be
built from a **new** claims map, and D15's replacement exists only at
`.scratch/d15/reports/round-34/handoff/declared-in-r7/claims-map.md` (`f71751e0…`)
— see `## Owed` item 3.

## 4. Fresh preservation proof at my close instant (04:13:18-03:00)

D11's proof is a pre-build snapshot; mine is a **later** one, taken after 46 seat
fragments had landed under `reports/round-34/`. Both instants show the same bytes:

```
$ date -Is
2026-10-19T04:13:18-03:00
$ git rev-parse HEAD
da68a6d705e41f369f21e8607bfaab5b54077f84
$ git diff-index --quiet HEAD; echo "EXIT=$?"
EXIT=0
$ git diff --name-only HEAD | wc -l                  # whole tree vs HEAD
0
$ git diff --cached --name-only HEAD | wc -l         # index vs HEAD
0
$ git diff --name-only HEAD -- reports/round-5 ... reports/round-33 | wc -l
0
$ git ls-files <rounds 5..33> | xargs sha256sum | LC_ALL=C sort | sha256sum
1713e725abbd3a73b03ff2e42a8774adcd9b8c294c458f25d4657065b126ce71  -
$ git status --porcelain
?? reports/round-34/
```

The fingerprint is **identical to D11's** (`1713e725…` = `1713e725…`) at an instant
roughly 20 minutes and ~46 fragment writes later. Every scratch render this round
(D05's, D08's, D15's) landed under `.scratch/`, which `git check-ignore -v` resolves
to `.gitignore:6:.scratch/` — ignored paths cannot alter tracked bytes. This is the
strongest form of the claim available before the integrator writes the new
revision: no seat has touched a filed byte, and now two independent seats have
shown it with the same fingerprint at two different times.

## 5. Scanner source (inlined so the final audit reruns this exact version)

```python
#!/usr/bin/env python3
"""Six stale D4 figures, D4-context scoped. Usage: python3 -B <this> <files...>"""
import re, sys
FIGURES = [
 ("S1 typed_labels=74",   r"typed_labels[\s:=]*74\b|\b74\s+labels\b|\blabels\s+74\b"),
 ("S2 native-form=56",    r"native[- ]form[\s:=]*56\b|\b56\s+native[- ]form\b"),
 ("S3 findings_total=16", r"findings_total[\s:=]*16\b|\b16\s+findings\b|carries\s+16\s+findings"),
 ("S4 hold=15",           r"\bhold[\s:=]*15\b|\b15\s+holds\b|findings_hold_or_fail[\s:=]*15\b|\b15\s+are\s+hold-or-fail\b"),
 ("S5 conflicts=4",       r"conflicts[\s:=]*4\b|conflicts[\s:=]*\(4\)|\bfour\s+conflicts\b"),
 ("S6 quarantine=3",      r"quarantine[\s_]*handles[\s:=]*3\b|quarantine[\s_]*handles[\s:=]*\(3\)|\bthree\s+quarantine\s+handles\b"),
]
# NOTE: deliberately NO "hold-or-fail (1N label holds" alternative — it fires on live wording.
D2_SRC = re.compile(r"typed-labels\.d2\.yml|culture-d2/|packet\.d2|RD-D2-01|D2-CL0\d|D2 read-only|58\s+(typed\s+)?labels|46\s+native-form")
D4_SRC = re.compile(r"typed-labels\.d4\.yml|culture-d4/|expected-holds\.json|packet\.d4|OQ-V3-05|D4-CL\d\d|GAR-0\d|furnace|round-18/d4")
D2_OWNER = re.compile(r"D2-owned|D2 residuals?|no longer D4-owned|removed from D4 ownership|pre-family-clean generation|OQ-V2-03|stay open in D2|not re-attributed to D4")
LIVE_D4  = re.compile(r"zero conflicts|conflicts[\s:=]*0\b|zero quarantine handles|quarantine handles[\s:=]*0\b|zero rank holds|zero unresolved rank items|zero notes and zero fails|twelve form holds")
def attr(l):
    return "D4" if D4_SRC.search(l) else ("D2" if D2_SRC.search(l) else "?")
for path in sys.argv[1:]:
    try: lines = open(path, encoding="utf-8").read().split("\n")
    except FileNotFoundError: print("%s : MISSING" % path); continue
    flagged = d2 = 0
    for i, l in enumerate(lines, 1):
        for name, pat in FIGURES:
            if not re.search(pat, l): continue
            if attr(l) == "D2": d2 += 1; continue
            flagged += 1
            cls = "RE-ATTRIBUTED-OK" if (D2_OWNER.search(l) and LIVE_D4.search(l)) else "STALE-ASSERTION"
            print("%-10s %-22s :%-5d %s" % (path.split("/")[-1], name, i, cls))
    print("== %s  flagged=%d  d2-attributed=%d" % (path, flagged, d2))
```

## Owed

1. `reports/round-34/depth/D05-packet-draft.md` — **absent at 04:12** (polled four
   times). §3 verified the scratch instance D05 rendered instead; re-run §5's
   scanner against the durable fragment when it lands, and against the filed pair
   `reports/round-34/handoff/declared-in-r7/{packet.md,twin.json}` once the
   integrator writes them. Expected: S1–S4 = 0; S5/S6 non-zero only inside
   D2-owner clauses that assert the live D4 value in the same line.
2. `reports/round-34/handoff/declared-in-r7/freeze.txt` — does not exist, so I
   could not verify the new revision's own digest self-consistency (`packet_sha256`
   in `freeze.txt` == sha256 of the packet). This is D11's owed item 4 and mine.
3. `.scratch/d15/reports/round-34/handoff/declared-in-r7/claims-map.md`
   (`f71751e0…`) — the new claims map that D05's clean draft was rendered from
   exists **only in gitignored scratch**. The integrator must land it durably under
   `reports/round-34/handoff/` before re-pointing
   `tools/exercise-handoff-e2e.py:184`; the file contents themselves are D15's
   deliverable, the durable-path decision is the integrator's.
4. Post-build re-run of §4's fingerprint by the integrator after the new revision
   and the `:1933-1934` default move are applied (D11 owed item 2). My §4 proves
   the pre-build instant only.

## Citations

Round declaration and contract (read-only):

- `reports/round-34/targets.json` — seat D20 row (`role: verifier`, `claim: D`,
  `mission`, `out: depth/D20-verify-preservation.md`); `shared_rules` (F-C13-1,
  "shared-file changes … DRAFTED … applied by the integrator", missing-dependency rule).
- `reports/round-34/claims.json:7` baseline commit; `:21-37` claim D
  `before`/`after_required`; `:30` "filed rounds 8-33 and r2/r4/r5/r6 packet bytes untouched".
- `REGIMEN.md:25-53` per-round contract.

Verified filed bytes (read-only; every digest in §1 measured by `sha256sum`):

- `reports/round-22/handoff/declared-in-r2/{packet.md,twin.json,expected.json,freeze.txt}`
- `reports/round-23/wording/declared-in-r3/{packet.md,expected.json,freeze.txt}`
- `reports/round-25/v3-supersession/declared-in-r4/{packet.md,expected.json,freeze.txt}`
- `reports/round-26/handoff/declared-in-r5/{packet.md,twin.json,expected.json,freeze.txt}`
- `reports/round-30/handoff/declared-in-r6/{packet.md:68,:69,:148,:149,:150,:152,:307; twin.json:1087-1158,:2619-2620; expected.json; freeze.txt; run.log}`
- `.gitignore:6` (`.scratch/` ignored), `.gitattributes` (absent)

Live inputs measured by this seat:

- `examples/culture-d4/typed-labels.d4.yml:29-47` (the `coverage` block cited in §3.2)
- `examples/culture-d4/expected-holds.json` (`counts`, 12 rows)
- `examples/culture-d2/typed-labels.d2.yml` (`coverage` block, read at `#coverage`)

Artifacts of other seats cited (not authored by me):

- `reports/round-34/depth/D11-preservation.md` — 253 lines at first read
  (`31f6848e…`), 340 lines at close (`5bab52e5…`); its `## Owed` item 1 names this
  fragment as the awaited verification.
- `.scratch/d05/declared-in-r7/{packet.md,twin.json}` — the draft instance of §3.1.
- `.scratch/d08/declared-in-r7/packet.md` (`6ced88ad…`), `.scratch/d15/…/declared-in-r7/claims-map.md` (`f71751e0…`).
- `reports/round-34/depth/D01-layout.md` §1, `D16-gap-fill.md` §2/§4 — the
  `CLAIMS_MAP` finding §3.5 corroborates only in its byte-identity half.

Commands relied on: `git rev-parse HEAD`; `git diff-index --quiet HEAD`;
`git diff --name-only HEAD`; `git diff --cached --name-only HEAD`;
`git ls-files` (incl. `-v`, `-s`); `git ls-tree -r da68a6d`; `git hash-object`;
`git status --porcelain`; `git check-ignore -v`; `git log -1 --format=%cI`;
`sha256sum`; `find -newermt`; `python3 -B` (scanner + live-byte reads); `date -Is`.
