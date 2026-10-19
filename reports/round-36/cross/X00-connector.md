- Seat: X00 | connector | claim cross | date 2026-10-19 | baseline ce103bf

# X00 — the round-36 collision matrix and integration order

Mission (`reports/round-36/targets.json`, seat `X00`): *"Collision matrix: register
content vs r7 freeze read set (component files are read-set members — a re-freeze
question), timekeeping row vs README order, recount vs the validators; integration
order."*

Read-only seat: this file is the only byte I wrote. Every reading below is a command
output or a `file:line`, taken at baseline `ce103bf5885af00023cdc4a174c17602476cdcf8`
(= `git rev-parse HEAD`, equal to `git rev-parse ce103bf`). Every command ran with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` from the lane root.

## 0. The headline: claim D's `before` is stale — the register-form domain is not empty

The matrix's most consequential row is not a file collision but a **premise
collision**. Claim D (`reports/round-36/claims.json`) declares:

> `before`: "Register-form domain empty (reports/round-25/argot/ + SCORECARD r25
> row); register law/strata exist but the form class has no instances"

That reading is **real but historical**. It is r25's measurement, filed at
`SCORECARD.md:312` ("the register-form domain in the delivered D4 packet is
EMPTY"). It was **closed two rounds later**, by r26 — `SCORECARD.md:329` records
claim D `register-stratum`: *"The round-17 register forecast CLOSED: the `stamp`
attestation register lands in the delivered furnace-league tree — 8 verified
register forms (tuum/kit/lom/nees/huum/mees/reek/saam)… derivation replay clean
(8 derived pairs, 0 violations over 170 records)"*. The landing commit is
`4f09c99` ("round-26: admit D/O/C — register stratum closes the r17 forecast"):

```
$ git log --oneline -S "STAMP-LENGTHEN" -- examples/culture-d4/components/04-lexicon.yml
4f09c99 round-26: admit D/O/C — register stratum closes the r17 forecast; r5 pin chain (devin)
```

Measured on the live bytes at `ce103bf`, the eight forms are present and wired:

| surface | path | reading |
|---|---|---|
| component rows | `examples/culture-d4/components/04-lexicon.yml:236-243` | L-56 `kit`, L-57 `lom`, L-55 `tuum`, L-58 `nees`, L-59 `huum`, L-60 `mees`, L-61 `reek`, L-62 `saam` — each `register: stamp` with `construction: STAMP-REVERSE`/`STAMP-LENGTHEN`, `derived_from`, `derivation`, `doublet_of` |
| assembled packet | `examples/culture-d4/packet.d4.yml:1053-1170` | the same 8 rows, packet-formatted (`id: "L-55"` … `register: "stamp"`) |
| register registry | `examples/culture-d4/packet.d4.yml:1329` | `registers:` block (QREG-01…08) |
| register law | `examples/culture-d4/packet.d4.yml:2788` | `register_law:` block (RGL-01…05) |
| derivation leg | `tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | exit **0**, `records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0` |
| law leg | `tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | exit **0**, `law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 … dangling=0 findings=0` |

A census of the packet's own lexicon block confirms the count:

```
$ python3 - (parse examples/culture-d4/packet.d4.yml)
lexicon rows total: 62 register-scoped: 8
  register-scoped: L-55 L-56 L-57 L-58 L-59 L-60 L-61 L-62
```

**Consequence for the round.** D's `after_required` — *"register-form domain
non-empty with verified forms (derivation replay clean over the new forms; law gate
exit 0 over them; typed pipeline holds updated with named gaps)"* — is **already
true at baseline**. Two of its three named legs were measured green above; the
typed pipeline is green too (`tools/gates/typed-pipeline-gate.py
examples/culture-d4/packet.d4.yml` → exit 0, `summary: 20/20 legs passed`). An
executor that "authors register-form component content" against this premise will
either (a) re-derive content that already exists and collide with L-55…L-62, or
(b) land duplicates. **The collision to route is a claim-repair, not a build.**
This is a reportable collision for the parent, not something X00 may fix (no
filed-byte edits, and the claim text is the parent's).

The narrow residue that is *not* already closed, if the parent wants to re-aim D:
`reports/round-26/register/review.md` §3 records "13 of the 54 delivered lexicon
records yield an unusable form" and the r28 law leg found the QREG-05..08
dangling-register defect (fixed r30, `SCORECARD.md:400`). Those are named gaps, not
an empty domain.

## 1. Collision A — register content vs the r7 freeze read set

**This is the collision the mission names, and it is a real one — currently
benign, structurally dangerous.**

The v3 exercise's read set is `tools/exercise-handoff-e2e.py:1939-1962`
(`V3_READ_SET`), 58 members, and it includes **every surface claim D would touch**:

- `:157-170` `D4_COMPONENTS` — all **12** `examples/culture-d4/components/*.yml`
  (members 34–45 of the read set), of which `04-lexicon.yml` (member 37) is the
  form-carrying file;
- `:151` `D4_PACKET` → `examples/culture-d4/packet.d4.yml` (member 28);
- `:152-154` `D4_TYPED_PACKET`, `D4_TYPED_LABELS`, `D4_HOLDS` (members 29–31);
- `:171-175` `D4_ASSEMBLER`, `D4_TYPED_TOOL`, `D4_TYPED_GATE`, `D4_ASSEMBLY_GATE`
  (members 46–49).

The freeze that pins them is `reports/round-34/handoff/declared-in-r7/`
(`freeze.txt` `packet_sha256: 45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`),
whose `expected.json` carries a 58-entry `inputs` digest map. **I measured the
whole read set against the live tree:**

```
read set: 58 match: 58 mismatch: 0 missing: 0
```

So **there is no drift today** — the r34 freeze is in sync with `ce103bf`. The
collision is prospective: *any* byte change to `04-lexicon.yml` or `packet.d4.yml`
makes the freeze red (`E2E-DIGEST` naming the changed file, per
`tools/exercise-handoff-e2e.py` selftest control "tamper read-set: exit 1
E2E-DIGEST naming the changed file"), and the repair is the sanctioned **re-freeze**
path, not an edit of the pinned bytes.

Re-freeze is a four-anchor operation. `reports/round-34/depth/D09-freeze-design.md`
§3.2 names the anchors and the audit rule: *"exit 0 iff all four anchors agree per
digest; exit 1 naming the disagreeing anchors; exit 2 (could-not-evaluate) if an
anchor is missing"*, with the measured caveat at `:177-178`: *"All four anchors live
**inside** the frozen dir, so they bound single-file edits, not a wholesale
re-freeze (which is legitimate by design). The dir-level anchor must therefore be an
external…"*. The r34 `freeze.txt` shows the mechanism in action — it is **10 lines**
and its last three lines are the re-freeze diff rows:

```
re-frozen packet_sha256: 41f92ee9b3f8444b73d29a5faff09944be5e5c7f… -> 45f5713261762a959ba77b057654c8db06d140e1…
re-frozen twin_sha256:   493d97700cc29b92376b0001a603cd759e7248e1… -> 0e22913850cd85bc393fe6d0d7a8bf448e9b253a…
re-frozen input reports/round-34/handoff/declared-in-r7/claims-map.md: 0121559452f2… -> d181de28ccaf…
```

`D09-freeze-design.md:58` warns of the trap this round must avoid: *"`freeze.txt`'s
diff iterates only the *new* inputs, so a path **dropped** from the read set prints
[no row]"* — i.e. a re-freeze that silently drops a member is invisible in the diff.
And the read set is not cosmetic: `V3_READ_SET` includes
`reports/round-34/handoff/declared-in-r7/claims-map.md` (member 57), which is
**already a re-freeze row in r34's own receipt**, and the same file is named by
`CLAIMS_MAP` at `tools/exercise-handoff-e2e.py:188`.

**Ordering rule this implies.** If claim D changes any D4 byte, the re-freeze must
land **before** the round's acceptance run, and the re-freeze must be a *new*
`declared-in-rN` directory rather than an in-place edit — `reports/round-34/depth/D06-twin-expected.md:121`
states the rule: *"an edit to the packet **must** be followed by a re-freeze, never
by patching `expected.json`"*. `--freeze` of the r34 directory is **forbidden** for
this seat and every seat (pinned bytes; hard boundary in my brief).

## 2. Collision B — the timekeeping row vs README order

**The spare is stale against the live README in three separate ways.** The routed
artifact is `reports/round-35/cov/C04-timekeeping-spare.md`; claim C's `before`
("CM 24 / total 211") is *correct*, but the drafted landing instructions are not.

**(i) The README it was written against no longer exists.** `C04-timekeeping-spare.md`
is a draft whose counts rest on `reports/round-35/cov/C11-readme-delta.md`, and C11
§0 pins the README at

> `053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`, 106 218 bytes, 493 lines, measured at HEAD `4a7aede`

The live file is a **different byte string**:

```
$ sha256sum corpus/README.md
51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0  corpus/README.md
$ wc -c corpus/README.md ; wc -l corpus/README.md
125229 corpus/README.md
523 corpus/README.md
```

C11's line map is therefore **wrong for every anchor it names**. C11 `§1` places
`## culture-material/ (18)` at line 169 and the totals at 469/471-473; live:

```
$ grep -n "^## culture-material/\|^Total knowledge entries\|^Counts checked\|^revision:" corpus/README.md
3:revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the
160:## myth-symbol/ (23)
186:## culture-material/ (24)
492:Total knowledge entries: 211.
494:Counts checked 2026-10-19 from the repo root:
```

Revision 2.0 moved both the section headers and the totals (`corpus/README.md:504-505`:
*"Revision 2.0 moved the totals 201 → 211, `## myth-symbol/` 19 → 23 and
`## culture-material/` 18 → 24 with the ten round-35 entries."*). **An integrator
applying C11's delta by line number will corrupt the file.** The delta must be
re-derived against `51b966af…`, not replayed.

**(ii) The insertion point is well-defined.** The index is filename-sorted
(ASCII) inside each section; the live culture-material section holds exactly 24
rows (`sed -n '186,212p' corpus/README.md | grep -c '^- \`'` → `24`), and the new
entry's sort position is unambiguous:

```
insert after textile-technology.md  before trade-economy-lexicon.md  index 19
```

**(iii) The sweep the claim names is currently green at the old count, so the
delta is a pure +1 and the acceptance test is already specified.**
`python3 -B reports/round-28/readme/sweep.py` → exit 0, `rows 211 files 211`,
`missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`,
`totals_ok True`, `footer_ok True`. Note the sweep's `footer.date` is
`2026-10-19` — it reads the README's own footer, so the footer text must move with
the counts. Claim C's `after_required` (CM 25 / total 212, README rev 2.1,
`212 rows == 212 files`) is consistent with this instrument; the risk is only the
**stale line map**, not the target numbers.

**A second, sharper collision inside the spare: its absence sweep no longer holds.**
The spare's gap statement asserts, for 28 instrument terms, *"**0 for every term**"*
and for near-misses a fixed table. Re-measured over the live tree
(`grep -ril -- "$kw" corpus/knowledge/*/*.md | wc -l`):

| term | spare claims | live | disposition |
|---|---|---|---|
| `curfew` | 0 | **1** | `corpus/knowledge/culture-material/fire-fuel-light.md` — the r35 entry, **landed after the spare was drafted** |
| `chronometer` | 2 | 4 | drift |
| `hour` | 8 | 17 | drift |
| `bell` | 81 | 87 | drift |
| `clock` | 6 | 82 | drift |
| `astrolabe` | 2 | 2 | match |
| `star clock` | 2 | 2 | match |
| `obelisk` / `meridian` / `time zone` | 1 each | 1 each | match |
| the other 27 instrument terms | 0 | 0 | match |

The `curfew` collision is the material one. `fire-fuel-light.md` landed in r35
(`git cat-file -e 4a7aede:corpus/knowledge/culture-material/fire-fuel-light.md` →
**absent**; present at `ce103bf`; culture-material 18 → 24) and it **owns the
time-signal institution** the spare claims is unowned:

- `fire-fuel-light.md:4` — "the fire-risk apparatus — night watch and *vigiles*,
  **curfew as a fire ordinance that became a time ordinance**, …"
- `:81` — "**The night watch.** Rome's *vigiles* … the watchman's call as the
  town's clock. Design rule: a fire watch is the cheapest way to give a pre-modern
  city a *night institution*"
- `:82` — "**Curfew.** *Couvre-feu* means, literally, 'cover the fire' … Craft use:
  **the curfew bell is the easiest way to make a town's clock *audible***, and its
  abolition is an era seam."
- `:112` — the risk word-bank row `curfew` < `couvre-feu`

The spare's own `- couples:` list (27 paths, **all resolving** — I checked every one)
**does not name `fire-fuel-light.md`**, and 11 of the 24 live culture-material files
are unnamed. So the spare, as routed, would land an entry that duplicates
`fire-fuel-light.md`'s night-watch/curfew institution and cites a couples list that
omits it. **This is a landing-blocker for claim C, not a formatting issue** — the
two auditors C01/C02 and verifier C03 must disposition the overlap (shrink the spare
to the *device* and hand the *institution* to `fire-fuel-light.md`, or declare the
boundary explicitly) before the row is inserted.

The spare's *device* claim is still clean: `grep -rl -i
"sundial\|gnomon\|clepsydra\|escapement\|clockmaker" corpus/knowledge/*/*.md` → no
files, and `corpus/knowledge/culture-material/timekeeping-instruments.md` does not
exist. So the gap is real for the instrument; it is the **institution** half that
collides.

## 3. Collision C — the recount vs the validators

Claim Ca asks for a recount ledger over rounds 33–35's filed counting commands.
The collision is a **standing rule, not a file**: three of the filed commands are
`python3 reports/round-<N>/run-validation.py`, and running any of those in-tree is
**absolutely forbidden** (F-C13-1; my brief states it as ABSOLUTE). They cannot be
recounted by execution. The recount seat must use the same disposition the peer
review seat already adopted — `reports/round-36/review/R03-cross-review.md:236,239,241`
records exactly this: *"could-not-reproduce-in-tree"* for the r33/r34/r35 runner
rows, with the reason *"(filed runner, F-C13-1)"*.

I re-ran every **non-runner** filed command myself, read-only, and all are green:

| round | claim | command | observed |
|---|---|---|---|
| 33 | O | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | exit 0, `findings: 0` |
| 33 | O | `… --selftest` | exit 0, `SELFTEST OK: 28/28 checks passed` |
| 33 | O | `test -s reports/round-33/op/O05-falsifier-disposition.md` | exit 0 |
| 34 | D | `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md` | exit 0, `INFO scan: fields=16/16 glossary-entries=20 findings=0` |
| 34 | D | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0, `packet_sha256=45f57132…` |
| 34 | O | `python3 tools/harness/receipt_guard_adoption.py --selftest` | exit 0, `"selftest_passed": true` |
| 34 | C | `python3 -B reports/round-30/craft/box1-survey.py` | exit 0, `"resolvable": 28`, `skill_sha256 f9bd07c2…` |
| 35 | C | partition census | `21 / 23 / 24 / 29 / 20 / 94` = 211 |
| 35 | C | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `totals.files 211`, `read_only true`, `deterministic true` |
| 35 | O | `python3 -B tools/exercise-handoff-e2e.py --selftest` | exit 0 |
| 35 | O | `… --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | **exit 1** (expected), `E2E-READSET: … reports/round-20/handoff/claims-map.md — the baseline row is superseded` |
| 33/34/35 | C,O,A | `python3 reports/round-<N>/run-validation.py` | **not executed** — F-C13-1; disposition `could-not-reproduce-in-tree` |

**The validators collide with the ledger in one more way worth flagging:** the
r34 runner **writes its own receipt** — `reports/round-34/run-validation.py:6`
("default (measure + guard the receipt via `tools/harness/receipt_guard.py`)"),
`OUTPUT`/`ROUND` at `:11-13`. That is precisely why F-C13-1 exists and why
`could-not-reproduce-in-tree` is the honest disposition rather than "match".

## 4. Live filed-byte mutations observed mid-round (evidence for the parent)

**A peer is executing filed round-runners in-tree right now.** I caught **two**
filed receipts rewritten during this session and restored both. This is not my
write; I report the measurement because a peer breach of F-C13-1 is exactly the
kind of thing the connector seat exists to surface.

**Mutation 1 — `reports/round-34/validation.json`**, seen while measuring §1:

```
$ git status --porcelain          # after my §1 read-set measurement
 M reports/round-34/validation.json
?? reports/round-36/
$ git diff --stat reports/round-34/validation.json
 reports/round-34/validation.json | 26 +++++++++++++++-----------
 1 file changed, 15 insertions(+), 11 deletions(-)
```

The diff's content is the r34 runner's **own** O2 leg failing:

```
-  "acceptance_checks_passed": true,
+  "acceptance_checks_passed": false,
-        "O1-O5: …",   "failures": [],
+        "failures": [ "O2: inventory counts differ: 30 runners, {'guarded-refresh': 19, 'unguarded-in-place': 11}" ],
-                "guarded-refresh": 18,
+                "guarded-refresh": 19,
```

Only `reports/round-34/run-validation.py` writes that file, and the mutation's
mtime is `2026-10-19 06:28:15 -0300` (= 09:28:15Z) — inside the concurrent seat
window (peer fragments under `reports/round-36/` carry mtimes 06:28–06:29).

**Mutation 2 — `reports/round-35/validation.json`**, seen ~90 s later while
re-verifying §0/§1 (`git status` after the re-verification pass):

```
$ git status --porcelain
 M reports/round-35/validation.json
?? reports/round-36/
$ git diff --stat reports/round-35/validation.json
 reports/round-35/validation.json | 6 ++----
 1 file changed, 2 insertions(+), 4 deletions(-)
$ git diff reports/round-35/validation.json | head
-            "measurement": {
-              "manifest": "pending-by-construction: integrator files the MANIFEST row in the same close pass"
-            },
+            "measurement": {},
-  "measured_at_utc": "2026-10-19T06:19:14.685566-03:00",
+  "measured_at_utc": "2026-10-19T06:29:42.347669-03:00",
```

The `measured_at_utc` moving to `06:29:42 -0300` (09:29:42Z) is the timestamp of
the *re-run*, proving the file was regenerated by executing
`reports/round-35/run-validation.py` (same "measure + guard the receipt via
`tools/harness/receipt_guard.py`" mode as r34 — `reports/round-35/run-validation.py:4`).

**What I can state and what I cannot.** Stated: both files were modified
mid-session, each carrying its own runner's recomputed receipt; I restored both
byte-exactly —

```
$ git checkout -- reports/round-34/validation.json
$ sha256sum reports/round-34/validation.json
ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a  reports/round-34/validation.json
$ git show HEAD:reports/round-34/validation.json | sha256sum
ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a  -
$ git checkout -- reports/round-35/validation.json
$ sha256sum reports/round-35/validation.json
328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124  reports/round-35/validation.json
$ git show HEAD:reports/round-35/validation.json | sha256sum
328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124  -
$ git status --porcelain
?? reports/round-36/            # clean
```

Not stated: **the owner.** I bisected the fifteen commands I ran (`c31` live +
selftest, `box1-survey`, `receipt_guard --json` + `--selftest`, handoff gate, battery,
`assemble-culture-d4.py --check`, `assemble-d4-typed.py --selftest`,
`typed-pipeline-gate`, `argot-derivation-gate`, `register-law-gate`, `e2e --selftest`,
`e2e v3 --quiet`, `e2e v3 --baseline r6`, readme sweep, inventory) and **none of them
reproduced either mutation** — each left the tree clean. Both mutations carry their
own runner's recomputed receipt and a fresh `measured_at_utc`, which identifies the
cause as a **peer seat executing filed round-runners in-tree** — the forbidden
F-C13-1 action. That attribution is **`to-verify`** — owner: the round-36
integrator (match the mtimes against the peer fragments' own claims;
`reports/round-36/review/R03-cross-review.md:236,239,241` shows the review seat
correctly refused to run these, so the actor is a different seat).

The parent should (a) confirm both receipts are byte-clean at integration time —
**any seat that ran a filed runner after r34/r35 were filed will have left them
dirty, and the round cannot be admitted over modified filed bytes**; (b) note that
**the r34 O2 leg now reports `acceptance_checks_passed: false` when re-run**, because
a 19th guarded runner exists that did not when r34 was filed — a *re-measurement*
artifact of running a filed runner after the fact, not a defect in r34. That is a
second, independent argument for the `could-not-reproduce-in-tree` disposition in §3;
(c) sweep the other filed receipts (r33 and earlier) for the same in-place rewrite
before closing.

## 5. Integration order (the seat's actual deliverable)

Dependencies are directed; the order below is forced, not advisory.

1. **Repair claim D's premise first (parent, before any D seat lands).** D's
   `after_required` is already satisfied at `ce103bf` (§0). Either re-aim D at the
   genuine residue (the 13 unusable forms, `reports/round-26/register/review.md` §3;
   the named typed-pipeline gaps) or mark D's register-form leg as
   already-closed-by-r26 and re-scope. Landing register content now **collides with
   L-55…L-62**.
2. **Then, and only if a D4 byte changes: re-freeze before any acceptance run.**
   New `declared-in-rN` directory; all four anchors consistent
   (`reports/round-34/depth/D09-freeze-design.md` §3.2); never `--freeze` the r34
   dir; never patch `expected.json` (`D06-twin-expected.md:121`); re-point
   `V3_BASELINE_DEFAULT`/`V3_FROZEN_DIR_DEFAULT` (`tools/exercise-handoff-e2e.py:1937-1938`)
   as a new supersession row. Verified state today: read set **58/58 match**, so if
   D is re-scoped to touch nothing, **no re-freeze is needed at all** — that is the
   cheapest path and it is available.
3. **Claim C: re-derive C11's delta against the live README before applying.**
   C11 targets `053966a2…`/493 lines; live is `51b966af…`/523 lines/125 229 bytes.
   Insert the new row after `textile-technology.md`; bump the section header
   `## culture-material/ (24)` → `(25)` at `corpus/README.md:186`, the totals line
   `:492` `211` → `212`, and the footer `:494-495` `(total 211 files; directory
   totals 21/23/24/29/20/94)` → `(total 212 …; 21/23/25/29/20/94)`; bump the
   revision block to 2.1. **Gate: `reports/round-28/readme/sweep.py` exit 0 with
   `rows 212 files 212`, `footer_ok True`.** Blocked until §2's
   `fire-fuel-light.md` overlap is dispositioned by C01/C02/C03.
4. **Claim Ca: recount in parallel with 1–3** (it touches no artifact the others
   write). Execute only the non-runner commands (§3 table); file the three runner
   rows as `could-not-reproduce-in-tree` with the F-C13-1 reason and the R03
   precedent. Do **not** execute a round runner in-tree.
5. **Telemetry last.** `reports/round-36/telemetry/dispatch-declared.json` is
   `open-at-seat-close`; its closing snapshot is owed once `validation.json` lands
   (`AGENTS.md` "Close what you open"), and the §4 filed-receipt mutations belong
   in that snapshot as measured rows with an owner.
6. **Before admission: re-verify every filed receipt byte is clean.** §4 caught two
   filed `validation.json` files rewritten in-tree by a peer this session; I restored
   both. Confirm `git status --porcelain` shows only `reports/round-36/` before the
   round is closed, and sweep r33-and-earlier receipts for the same in-place rewrite.

**Non-collisions (checked, to close the matrix).** `corpus/README.md` is **not** in
`V3_READ_SET` (`any('README' in r for r in V3_READ_SET)` → `False`), so claim C's
README edit cannot drift the r7 freeze; the same holds for
`tools/exercise-handoff-e2e.py` and `reports/round-28/readme/sweep.py`. So **claims
C and Ca are freeze-neutral**; only D is freeze-coupled. That asymmetry is the
single most useful integration fact this seat produces.

## Owed

- `reports/round-36/cross/X00-connector.md` — this file (delivered).
- **Owner: round-36 integrator** — decide D's re-scope (§0) before D seats land;
  the claim text is the parent's to amend, not a seat's.
- **Owner: C01/C02/C03** — disposition the `fire-fuel-light.md` night-watch/curfew
  overlap (§2) before the spare's row is inserted into `corpus/README.md`.
- **Owner: round-36 integrator** — attribute the two filed-receipt mutations
  (`reports/round-34/validation.json`, `reports/round-35/validation.json`, §4) to a
  seat; `to-verify` here. Both are restored byte-exact by X00; re-verify before
  admission.
- **Owner: Ca seat** — the recount ledger itself; X00 supplies the disposition rule
  and the measured non-runner readings (§3), not the ledger.

## Citations

- `reports/round-36/targets.json` — seat `X00` mission/out; `shared_rules`.
- `reports/round-36/claims.json` — claims D/C/Ca `before`/`after_required`;
  `axes_in_play`.
- `REGIMEN.md` — position 4 provider/fallback; per-round contract.
- `tools/exercise-handoff-e2e.py:151-188` (`D4_*`, `CLAIMS_MAP`),
  `:1937-1962` (`V3_BASELINE_DEFAULT`, `V3_FROZEN_DIR_DEFAULT`, `V3_READ_SET`);
  `python3 -c "import runpy; …"` → read set 58 members, members 28–49 = D4 surfaces.
- `reports/round-34/handoff/declared-in-r7/{freeze.txt,expected.json,run.log}` —
  `packet_sha256 45f57132…`, 58-entry `inputs`, re-freeze diff rows.
- `reports/round-34/depth/D09-freeze-design.md:58,:125-138,:156,:177-178` — four
  anchor audit; dropped-member blind spot.
- `reports/round-34/depth/D06-twin-expected.md:121` — re-freeze, never patch.
- `SCORECARD.md:312` (r25 "domain … EMPTY"), `:329` (r26 register-stratum closed),
  `:400` (r30 QREG-05..08 fix).
- `examples/culture-d4/components/04-lexicon.yml:236-243` — L-55…L-62,
  `register: stamp`.
- `examples/culture-d4/packet.d4.yml:1053-1170` (L-55…L-62), `:1329` (`registers:`),
  `:2788` (`register_law:`).
- `tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` → exit 0,
  `records=187 register_scoped=14 derived_pairs=8 … violations=0`.
- `tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` → exit 0,
  `law_rows=5 … dangling=0 findings=0`.
- `tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → exit 0,
  `summary: 20/20 legs passed`.
- `reports/round-25/argot/current-state.md:76-79`, `reports/round-25/argot/delta.md:52,:257`
  — the historical empty-domain reading.
- `reports/round-26/register/forms.md` §1 (the eight forms), `reports/round-26/register/review.md` §3
  (13 unusable forms).
- `corpus/README.md:3` (revision 2.0), `:160` (`## myth-symbol/ (23)`), `:186`
  (`## culture-material/ (24)`), `:492` (totals 211), `:494-495` (footer),
  `:504-505` (rev 2.0 delta); `sha256sum` → `51b966af…`; `wc` → 523 lines / 125 229 B.
- `reports/round-35/cov/C11-readme-delta.md` §0/§1 — target README `053966a2…`,
  106 218 B, 493 lines at `4a7aede` (stale).
- `reports/round-35/cov/C04-timekeeping-spare.md` — the spare; its absence sweep and
  near-miss table (re-measured in §2).
- `corpus/knowledge/culture-material/fire-fuel-light.md:3,:4,:81,:82,:112` — the
  night-watch/curfew institution; `git cat-file -e 4a7aede:…` → absent.
- `reports/round-28/readme/sweep.py` → exit 0, `rows 211 files 211`, `footer_ok True`.
- `reports/round-36/review/R03-cross-review.md:225-250` — peer recount table and the
  `could-not-reproduce-in-tree` precedent.
- `reports/round-34/run-validation.py:6,:11-13` and
  `reports/round-35/run-validation.py:4` — both runners write their own receipts
  ("measure + guard the receipt via `tools/harness/receipt_guard.py`").
- `git status --porcelain`, `git diff`, `git checkout --`, `sha256sum`,
  `git show HEAD:…` — the §4 mutations and their byte-exact restorations
  (`round-34` → `ba2fa4dc…`, `round-35` → `328e97b3…`).
