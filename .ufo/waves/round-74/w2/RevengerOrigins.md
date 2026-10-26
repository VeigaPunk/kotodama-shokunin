# RevengerOrigins — round 74, wave 2 (falsify; hyaku run 7)

ATTACK assigned: reverse-engineer the original intent behind round-73's five routed defects
(`corpus/lessons/round-73-verifier-spotcheck.md:83-88`, §6 items 1-5) and the six inherited
round-73 w2 files committed at the freeze, then compare with what round 74 actually did.

Revisions read: base `f7104cbce186bc2e1522abf0cfd619cc834628bb`, operative freeze
`00c408a0af2fa5ddf65af2224152ce258b26d896`, claim Ca lands `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`,
claim C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`, lane main at read
`1d7add3f7b9eaf6f3349c56c36f6d06325d74236` (`git log --oneline 00c408a..main` = 1d7add3, c4bf61a,
d7a3840, 5e4796c). Post-freeze diff touches no counter, claim or ledger:
`git diff --stat 00c408a 1d7add3 -- reports/round-74/` lists only telemetry files added/edited
(`census-end`, `controls-{c,ca}`, `junk-{c,ca}`, `measures-{c,ca}`) — `accept-c.py`/`accept-ca.py`
byte-identical at freeze and lands (sha256 `8d30487fa469…` / `8052f1e25c36…`).

Clone: `D=$(mktemp -d /tmp/RevengerOrigins-XXXX)` → `/tmp/RevengerOrigins-8TCd`;
`git -C /tmp/RevengerOrigins-8TCd rev-parse --show-toplevel` printed `/tmp/RevengerOrigins-8TCd`,
then `git clone -q …/kotodama-shokunin /tmp/RevengerOrigins-8TCd/lane`; all detach/branch moves were
inside it. No writes to the fleet repo, no writes to the lane outside this report and a scratch dir
that was removed afterwards (`.ufo/waves/round-74/revorig-scratch/`, now deleted).

Fetch hygiene: no external URL was fetched for this item — every attack target is committed lane
bytes, so there is no UA line to record and no "no capture" ruling was needed (no CDX probe engaged).
No tool was installed or upgraded (pacman not run; no uv/npx/binary install). Host note: `/tmp`
was at 98-100 % (128 G, 679 M free) during my runs; one default-TMPDIR control failed with
`ERROR: checkout f7104cb… failed: fatal: cannot create directory at 'reports/round-47/scribe':
No space left on device` (my own clone/scratch were deleted afterwards). See F2 — that accident is
what exposed the RECEIPTS channel below.

---

## 0. Routed item 1 — commit/discard the six inherited files, record what RevengerOrigins.md holds, stop post-push seat writes

Intent reconstructed: the five tracked files' late-write bytes and the untracked seat report were
the only carriers of round-73 wave-2 content that never reached a tree; the closers wanted a
decision ON RECORD (commit or discard), the report's content summarised, and the write-after-push
class stopped.

What round 74 did — **closed in substance for the data half**:

- All six are tracked at the freeze with the pinned bytes:
  `git ls-tree 00c408a -- .ufo/waves/round-73/w2/{CritEntryAmendFinal.md,ExecSelftestAll.md,ScribeLogScorecard.md,SimplifierEntries.md,drafts/log-entry.md,RevengerOrigins.md}`
  yields blobs whose sha256 equal the ledger's `must_track` values
  (`reports/round-74/ledger.json` `must_track`), e.g. `CritEntryAmendFinal.md 290a6ccd839c…`,
  `RevengerOrigins.md 7d14591923af…` — while the same five at base have DIFFERENT hashes
  (`CritEntryAmendFinal.md 246de174216d…`, `ExecSelftestAll.md 0d24aeed83b9…`,
  `ScribeLogScorecard.md f4f14669fc0d…`, `SimplifierEntries.md 985dd8838360…`,
  `drafts/log-entry.md 01d503258c8a…`) and `RevengerOrigins.md` is absent at base
  (`git ls-tree 00c408a -- …RevengerOrigins.md` prints it; `git ls-tree -r f7104cb -- …RevengerOrigins.md`
  prints nothing). So the committed bytes are the late-write bytes, not the base blobs.
- The blobs are identical at freeze and lands and the counter re-checks it:
  `LEG PASS TRACKED paths=6 problems=[]` (my run).
- The report's content is recorded: `.ufo/waves/round-74/w1/ExecLeftovers.md:31` (verdict row:
  "a real 450-line seat report that arrived 2m25s after the fleet report was filed and 1m41s after
  the round was marked complete; F5/F6 are still open at HEAD") and `:199-263` (arrival timeline,
  dispatch entry, what it holds). The file is committed at the freeze (blob `90694bead7f2`).
- The lesson row is `corpus/lessons/round-74.md:168` (R74-M1, state "fixed at freeze").

F7 (LOW) — the operational half ("stop seats writing after the push") got no mechanism, and the
class recurred inside round 74: `corpus/lessons/round-74.md:177` (R74-M10) records two parked
round-73 seats appending `## Post-wave update` sections to TRACKED round-73 wave-1 reports, repaired
by restoring from the branch. At my read `git status --porcelain` in the lane still shows the whole
`.ufo/waves/round-74/w2/` directory untracked, i.e. the recurrence condition (seat bytes present,
uncommitted, at push time) is unchanged; the only guard is that the L1 must commit before pushing.
Proposed fix: make "commit every seat report and require `git status --porcelain` to be empty before
the push" a numbered step in the round-75 prompt/spec, and a probe item that checks the tree is
clean at closure.

## 1. Routed item 2 — PASS-at-lands receipts for ACCEPT-C-73 / ACCEPT-CA-73

Intent: the round-73 PASS verdicts existed only in seat prose; a committed, typed receipt was asked
for, under `reports/round-73/telemetry/` (spotcheck `:85`).

What round 74 did — **closed in substance, stronger than asked, with a form deviation**:

- `reports/round-74/telemetry/accept-c-73-at-lands.txt` and `accept-ca-73-at-lands.txt` are committed
  and carry `# counter sha256 (self): 95aee881…` / `222d4dd6…`, `stamped`/`evaluated`/`measured` =
  `2d1cd9140d3a…`, `# tree: 516ea6c7d926…`, and the terminal lines
  `ACCEPT-C-73: PASS legs=11/11` / `ACCEPT-CA-73: PASS legs=9/9`.
- The Ca counter does not trust them: `LEG PASS RECEIPTS rev=2d1cd9140d3a
  receipts=['accept-c-73=50c60bb67f16', 'accept-ca-73=864c94192854'] problems=[]` in my run at the
  tip (raw receipt sha256 prefixes `50c60bb67f16`/`864c94192854`).
- F6 (LOW, form only): the routed path `reports/round-73/telemetry/` was not used. The claim's wave-1
  correction F3/F4 chose one canonical path under `reports/round-74/telemetry/` and the change is
  disclosed (`corpus/lessons/round-74.md:169`, claims.json F3/F4). No fix needed; recorded so the
  routing's literal wording is not mistaken for an unmet requirement.

## 2. Routed item 3 — "Ca 9 scenarios" vs `SELFTEST OK: 10 scenarios`, and the ERROR-line label

Intent: reconcile the prose count with the receipt, and mark the `ERROR: base … is not a commit`
stderr line as the control's expected output rather than a failure.

What round 74 did — **closed in substance**:

- Two ANNOTATE pairs, `LC-02` (`LOG.md:4297`, 9→10) and `LC-03` (`fleet:.ufo/reports/round-73/kotodama.md:10`,
  9→10), with the re-derivation command `git grep -h -o -E 'SELFTEST OK. [0-9]+ scenarios' f7104cb -- reports/round-73/telemetry/selftest-r3.txt`;
  SCORECARD rows exist (`SCORECARD.md` `## Corrections — round 74`, LC-02/LC-03) and my run re-ran
  them: `LEG PASS ANNOTATE rows=14 annotate-pairs=12 unannotated=0 []`.
- The ERROR-line label landed: `SKILL.md:707` — "r3's `ERROR: base 8841ad3b… is not a commit` stderr
  line is the expected frozen-base-absent control output, not a failure."
- Why 9 became 10 is disclosed in round-73's own `reports/round-73/counter-revisions.md` r3 row
  ("selftest gains scenario 7b 'worktree-only ledger'"), so the annotation's 9→10 is consistent with
  the counter history; the guard against a future reader thinking LOG was always wrong is thin
  (neither the SCORECARD row nor R74-M4 cites the r3 cause) — LOW, folded into F5's neighbourhood.
- F5 (MEDIUM) below is a separate status-drift defect in the same table.

## 3. Routed item 4 — counter hardening (junk landings, graded-tree config, constant printers, SEPARABLE)

Intent: the four channels that let junk landings score PASS in round 73 must not survive into
round 74's counters; the round-73 predicates stand for round 73.

What round 74 did — **closed in substance for all four named channels** (verified by reading the
committed controls and by the counter's own legs):

- Junk landings are all rejected: `junk-c.txt` tail `# C summary: J1=FAIL, J2=FAIL, J3=FAIL, J9=FAIL`
  and `# ACCEPTED JUNK LANDINGS: none`; `junk-ca.txt:181-182`
  `# Ca summary: J4=FAIL, J4b=FAIL, J5=FAIL, J6=FAIL, J7=FAIL, J8=FAIL, J9=FAIL` /
  `# ACCEPTED JUNK LANDINGS: none` (round-73 survivors J3/J4b/J5/J6/J7 are the same fixtures now red).
- Graded-tree config: `FROZENCFG` reads `git show 00c408a…:reports/round-74/claims.json`
  (sha256 `270e31790e2932c8…` printed), red on the J3/J9 graded-tree `claims.json` edits and on the
  J4/J4b graded-tree ledger edits; ledger/claims are byte-pinned at lands.
- Constant printers: the observe allowlist is argv-level and excludes interpreters; selftest
  scenarios `shell-string`, `interpreter`, `constant-printer`, `out-of-clone` each make LEDGER red.
- SEPARABLE is a closed read list (`scanned=[…]` printed) and red on a planted correction-row
  citation of a lane id (`separable-lane-row`, `separable-sid`, `separable-family` scenarios; J7).
- The Ca counter's own selftest receipt is committed and substantive:
  `SELFTEST OK: 179 checks across 41 scenarios reported-fail=0`.

Two defects survive this channel:

**F1 (HIGH) — the frozen Ca claim is false at the round's final tree.**
`python3 -B reports/round-74/accept-ca.py --root . --lands 1d7add3f7b9e --freeze 00c408a0af2f --fleet-root /home/vgpnk/Projects/shokunin`
in my clone prints

```
LEG FAIL APPENDONLY
     protected=['LOG.md', 'SCORECARD.md', 'corpus/lessons/round-74.md', 'corpus/lessons/round-73.md', 'corpus/lessons/round-72.md', 'reports/round-73/claims.json', 'reports/round-73/ledger.json'] protected-removed=0 … problems=['corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]']
…
ACCEPT-CA-74: FAIL legs=10/11
EXIT-CA=1
```

The byte is claim C's own landing: the S877 used-by in-place edit at `corpus/SOURCES.md:832`. The
frozen Ca APPENDONLY leg allows changed lines only on REPAIR `stated_at` lines plus appends
(`claims.json` Ca legs[5]); `SOURCES.md:832` is neither. So the two frozen claims cannot both hold at
one tree. The round knows it and works around it: `junk-ca.txt:63-64` NOTE (L1) says the two claims
"conflict when both land in one tree; claim Ca is therefore measured at its OWN landing commit" —
a post-freeze reinterpretation of `<lands>` that the claim text does not contain, while Ca's kill
rule says "any leg false at `<lands>` -> the claim fails as declared". The wave-1 F5 correction
fixed the read side (SEPARABLE's read set) and left the write side (APPENDONLY's changed-lines
clause) with the same hole.
Proposed fix: add a frozen `cross_claim_inplace` exemption to the Ca APPENDONLY leg naming
`corpus/SOURCES.md` line of the S877 used-by cell (derived from C's ROWS leg, not hard-coded), and
re-measure Ca at the tip; or land Ca strictly after C and define `<lands>` once, in the claim.

**F2 (MEDIUM) — the hardened RECEIPTS leg measures the environment, not the receipts.**
Ran at Ca's own lands with `TMPDIR` outside `/tmp` (forced by the full `/tmp`):

```
LEG FAIL RECEIPTS
     rev=2d1cd9140d3a receipts=['accept-c-73=50c60bb67f16', 'accept-ca-73=864c94192854'] problems=['reports/round-74/telemetry/accept-c-73-at-lands.txt: committed stdout differs from the re-run (bda16ca6deec vs 14478ddbf6f6)', 'reports/round-74/telemetry/accept-ca-73-at-lands.txt: committed stdout differs from the re-run (55544779204d vs 9c9d8a80d7f4)']
ACCEPT-CA-74: FAIL legs=10/11   (exit 1)
```

Same revision, same counter bytes, same committed receipts — the raw receipt hashes
(`50c60bb67f16`, `864c94192854`) are identical to the values printed in the PASSING tip run and in
`measures-ca.txt`. The cause is in the code: `reports/round-74/accept-ca.py:183`
`RECEIPT_TMP_RE = re.compile(r"/(?:var/)?tmp/[^\s:,\"']+")` normalizes only `/tmp`-rooted paths,
while `:844`/`:1730` pass the caller's `TMPDIR` to the re-run subprocess. The round-73 counters embed
their materialization paths (`# materialized: git archive … at /tmp/r73-lands-…/lands`,
`# clone: /tmp/r73-ca-…/lands`), so a re-run under a different `TMPDIR` cannot match. Demonstrated:

```
python3 - <<EOF
import re; R=re.compile(r'/(?:var/)?tmp/[^\s:,"\']+')
R.sub('<TMP>', '# clone: /tmp/r73-ca-iinqsd_r/lands head=2d1cd9140d3a')
R.sub('<TMP>', '# clone: /home/vgpnk/…/revorig-scratch/r74-ca-a1l8ymb5/lands head=2d1cd9140d3a')
EOF
'# clone: <TMP> head=2d1cd9140d3a'
'# clone: /home/vgpnk/…/revorig-scratch/r74-ca-a1l8ymb5/lands head=2d1cd9140d3a'
sha256(normalize(committed accept-c-73-at-lands.txt))[:12] = bda16ca6deec
sha256(normalize(committed accept-ca-73-at-lands.txt))[:12] = 55544779204d
```

`bda16ca6deec`/`55544779204d` are exactly the "committed stdout" values in the failing run, so the
committed side is right and the re-run side moved. Proposed fix: normalize the actual `TMPDIR` root
(and any `# clone:` / `# materialized:` path token) rather than a `/tmp`-shaped literal; or force
`TMPDIR=/tmp` for the re-run; add a selftest scenario with `TMPDIR` outside `/tmp`.

## 4. Routed item 5 — the README last footer is the live value

Intent (spotcheck `:87`): the stale footers stay by append-only design, the later footer is live, so
"any census reader must take the last footer".

What round 74 did — **annotated and routed forward; not fixed. This is the one routed item left open
in substance.**

- The round's own instrument does take the last footer: `reports/round-74/accept-c.py:1758-1827`
  reads the last `Counts checked` block, compares total/vector to the landed tree and requires older
  footers byte-identical; `LEG PASS INDEX` in my run at the tip.
- The pre-existing reader still takes the FIRST footer. Running it read-only in my clone at the tip:

```
$ python3 -B reports/round-28/readme/sweep.py
rows 247 files 249
missing_from_index 4 ['culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md', 'culture-material/heritage-taxonomy-models.md', 'linguistics/conlang-scholarship.amend-2026-10-23.md', 'linguistics/conlang-scholarship.md']
orphan_rows 2 ['civilizations/conlang-scholarship.amend-2026-10-23.md', 'civilizations/conlang-scholarship.md']
header_drift {'culture-material': {'declared': 36, 'files': 40}, 'linguistics': {'declared': 30, 'files': 32}}
footer {"date": "2026-10-25", "command": "python3 tools/source-audit-inventory.py …", "total": 243, "dir_totals": [30, 29, 36, 29, 24, 95]}
footer_live {"total": 249, "dir_totals": [32, 29, 40, 29, 24, 95], …}
footer_findings [{"class": "FOOTER_TOTAL", "declared": 243, "live": 249}, {"class": "FOOTER_DIR_TOTALS", …}]
EXIT=1
```

  `sweep.py:64-71,106-113` parses with `FOOTER_RE.search` — first match wins. The three footers are at
  `corpus/README.md:751` (243 / 30-29-36-29-24-95), `:794` (247 / 32-29-38-29-24-95) and `:815`
  (249 / 32-29-40-29-24-95); sweep reads :751.
- Round 74 names this and defers it: `corpus/README.md:816-819` — "`reports/round-28/readme/sweep.py`
  still parses the first one, so its own totals legs stay red until a successor instrument names the
  authoritative footer" — and `corpus/lessons/round-74.md` "Routed to round 75" item 3 M3 repeats it.
- **F4 (MEDIUM)**: the routed obligation was "any census reader must take the last footer" and the
  only committed census/index reader still does the opposite. The fix is small (change
  `footer_reading`/`FOOTER_RE` to take the last block, as `accept-c.py` already does, or land a
  successor instrument and name it in the census step); leaving it red means the routed defect
  survives a second round with only a prose note.

## 5. Additional finding in the Ca landing itself

**F3 (MEDIUM) — the round's own gate-registry row records a measurement at counter bytes that are
not the landed counter, and counts its own receipt contradicts.**
`SKILL.md:706` (accept-ca-74, row added by the Ca landing `5e4796c`):

> "`python3 -B reports/round-74/accept-ca.py --selftest` — measured at counter sha256
> `76d00b88325f…`: exit 0, `SELFTEST OK: 138 checks across 37 scenarios reported-fail=0`; receipt
> `reports/round-74/telemetry/selftest-ca.txt`"

Landed counter: `git show 1d7add3:reports/round-74/accept-ca.py | sha256sum` =
`8052f1e25c36…` (identical to the freeze blob and to `.ufo/waves/round-74/counters/accept-ca.py`).
Landed receipt `reports/round-74/telemetry/selftest-ca.txt` last line:
`SELFTEST OK: 179 checks across 41 scenarios reported-fail=0`, and the lesson agrees
(`corpus/lessons/round-74.md:175`, R74-M8: "179 checks across 41 scenarios"). `76d00b88325f` appears
in no committed counter: it is the pre-freeze build. The wave-1 drafter flagged exactly this action —
`.ufo/waves/round-74/drafts/skill-gates-rows.md:131-133` "**The Ca counter changed after its measured
selftest.** … Re-run the selftest at freeze and file `selftest-ca.txt` from those bytes if they
differ", and `.ufo/waves/round-74/w1/ScribeSkillGates.md:177` — and the row was landed with the stale
pin anyway. Secondary cause: the selftest receipts carry no `# stamped revision:` / `# counter sha256
(self):` header (`selftest-ca.txt` starts at `selftest: do-nothing -> …`), unlike the QUALITY 17/19
grammar `tools/check-receipt-seq.py:24-31` requires, so nothing in the receipt can disprove the row.
Proposed fix: append a correction note row (in-place edit of :706 would trip Ca APPENDONLY's
changed-lines clause) giving `8052f1e25c36… / 179 checks / 41 scenarios`, and make the selftest
receipts carry the stamped revision + counter sha256 so a later reader can check the pin.

**F5 (MEDIUM) — the round's own new lesson rows state a status that is false at lands.**
`corpus/lessons/round-74.md:170-171` (R74-M3, R74-M4) end with state `pending landing`, but both fixes
are in earlier commits: R74-M3's counters/controls were installed at the freeze
(`corpus/lessons/round-74.md:175` R74-M8 "counters installed at the declared paths in the freeze
commit"), and R74-M4's SCORECARD rows landed in `5e4796c` (22:48:30), the direct parent of the commit
that added the lesson (`d7a3840`, 22:49:29). Nothing after them changes it, so at `1d7add3` the file
asserts a stale state in the same table whose M4 row is about number drift. Proposed fix: a
`## Corrections` note in the round-75 lesson (round-74's lesson is append-only) and an
ANNOTATE pair next round so the counter re-derives it.

---

## 6. Dispositions

| routed item (spotcheck §6) | what round 74 did | disposition |
|---|---|---|
| 1 commit/discard six files + record + stop post-push writes | six committed unchanged at `de93d91` (blob sha256 = `must_track`), content recorded in `w1/ExecLeftovers.md:31,199-263`, `TRACKED` leg pins them | data half **closed in substance**; process half **open** (F7: class recurred in R74-M10; w2 dir untracked at read) |
| 2 PASS-at-lands receipts | committed at `reports/round-74/telemetry/` and re-executed by the `RECEIPTS` leg | **closed in substance** (stronger); path differs from routing (F6, disclosed) |
| 3 scenario-count reconciliation + ERROR label | `LC-02`/`LC-03` ANNOTATE 9→10, re-derived by the counter; label at `SKILL.md:707` | **closed in substance**; attribution nuance (r3 added scenario 7b) not carried into the row (LOW) |
| 4 counter hardening | graded-tree config, constant printers, SEPARABLE, junk landings all closed and controlled (`ACCEPTED JUNK LANDINGS: none` ×2) | **closed in substance** for the named channels; new channel found (F2) and joint-tree conflict at the root of F1 |
| 5 README last footer | round's own `INDEX` leg takes the last footer; `sweep.py` still takes the first and is red; disclosed and routed to round 75 | **open** (F4 — annotated, not fixed) |

## 7. Attacks that FAILED (the claim survived) — with the evidence

- Six inherited files "committed unchanged": survived — freeze blob sha256 equal the ledger
  `must_track` and differ from the base blobs for all five tracked files; `RevengerOrigins.md` is
  absent at base and 450 lines at freeze.
- PASS-at-lands receipts "are typed, not re-executed": survived — the counter re-executes the
  round-73 counters at `2d1cd91` and compares stdout (`LEG PASS RECEIPTS` at the tip, raw receipt
  hashes `50c60bb67f16`/`864c94192854`); an edited receipt fails (fixture J9/J8 in `junk-ca.txt`).
- "9 scenarios is right, 10 is the counter lying": survived as an annotation, not a repair —
  the counter's own history discloses the r3 scenario addition (`reports/round-73/counter-revisions.md`
  r3: "selftest gains scenario 7b"), and the r3 receipt says 10; the round neither rewrote the frozen
  prose nor the receipt.
- Junk landings still pass: survived (all nine fixtures rejected; the five round-73 survivors now red).
- Config read from the graded tree: survived — `FROZENCFG` reads `00c408a`, sha256 pinned; graded-tree
  edits are red.
- Ledger constant-printers: survived — argv allowlist excludes interpreters; J4/J4b red.
- SEPARABLE wider than frozen: survived — closed read list; planted lane-id citation red.
- `LAND`/`DO-NOTHING` shapes: survived — `lands == base` refused (`FAIL legs=0/11`), `lands == freeze`
  graded FAIL (7/11 Ca, 4/13 C), no refusal.

## 8. Confidence

- F1, F2, F3, F4, F5 are direct executions/hashes of committed bytes in my own clone (high).
- The positive control "Ca PASS 11/11 at `5e4796c` with the default `TMPDIR`" could not be re-run
  here: `/tmp` filled to 100 % mid-round and the rerun aborted with `No space left on device`
  (external host condition, and the same condition that produced F2's evidence). Substitutes relied
  on: the committed `measures-ca.txt` (full STAMP grammar, `PASS legs=11/11` at `5e4796c`) and my
  `5e4796c` run in which every leg except `RECEIPTS` passed with the committed receipts byte-identical
  — the residual risk is that some other `5e4796c`-only leg is also environment-sensitive (unseen).
- The "routed item 3 intent" reading (reconcile = annotate, not rewrite) is inference from the
  append-only design; the spotcheck's own text ("by append-only design") supports it.
- No semantic-proof tool (`lsp`) was needed: every target is a git object, a committed text file, or
  a run of a committed counter; no definition/call-site reconstruction was involved.
