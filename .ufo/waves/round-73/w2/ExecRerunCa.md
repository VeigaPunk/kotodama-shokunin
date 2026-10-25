# ExecRerunCa — wave 2 attack on the claim-Ca measurement (round 73, hyaku run 7)

Seat: `ExecRerunCa` (leaf; no delegation, no background jobs, no `task` spawns, no labrat used).
Target: claim **Ca** — `reports/round-73/accept-ca.py` (r3), `reports/round-73/ledger.json`,
`SCORECARD.md` `## Corrections — round 73`, `SHONEN.md`/`SKILL.md` edits, `reports/round-73/telemetry/`.
Lane revision graded: `0316b8883b4f8d44b8efd720140e7f52f734a102` (tree `9b10fa06a2d3756c8bacfc8fc7b2115921370d97`).
Frozen inputs: `reports/round-73/claims.json` sha256 `5716523f3e8e…` and `reports/round-73/ledger.json`
sha256 `c912401dd511…`, both **byte-identical at `af65165` and at lands** (`git diff --stat` empty;
only `counter-revisions.md` was appended afterwards).

No tools installed; pacman not run. No network fetch. Throwaway clones used (all `/tmp`):

| label | path | revision |
|---|---|---|
| lands | `/tmp/tmp.EkHQkZt8iO/lane` | `0316b888` |
| base | `/tmp/tmp.MMvOgnpOzL/lane` | `8841ad3b` |
| Ca landing | `/tmp/tmp.odYaPbGFqe/lane` | `e62d7316` |
| r2 commit | `/tmp/tmp.SL3fDlvZY5/lane` | `35378990` |
| round-72 stamp | `/tmp/tmp.SUNkXz3gjN/lane` | `21ad3088` |
| mutation probe | `/tmp/tmp.Q8xmBaNyXO/lane` | `0316b888` + 2 throwaway commits |

`git -C "$D" rev-parse --show-toplevel` was checked for every probe root before the first commit; the
two mutation commits used `seat@example.invalid` only inside `/tmp/tmp.Q8xmBaNyXO`. The lane working
tree was not written except this report.

## Headline

The counter **does** print `ACCEPT-CA-73: PASS legs=9/9` at lands, exit 0, and every PAIR line
re-derives by hand. The measurement still has one **false green** (F1: SEPARABLE passes a byte it
reads that cites a claim-C path), one **false landed statement** (F2: the gate row documents a
selftest output the graded counter no longer prints), and a **mislabeled observation** (F3:
`observed_lands='245'` is a base-pinned value; the lands tree holds 247).

| # | severity | finding |
|---|---|---|
| F1 | **BLOCKER** | SEPARABLE is green at lands while an in-place added line the leg reads (SKILL.md `accept-c-73` row, added by the Ca commit) cites the claim-C path `reports/round-73/accept-c.py`; the added-line scan tests only the S-id half of the predicate. |
| F2 | **BLOCKER** | `SKILL.md:704` at lands says the `accept-ca-73` selftest "prints `SELFTEST OK: 9 scenarios`"; the graded r3 counter prints `SELFTEST OK: 10 scenarios`, and the r3 receipt in the same commit says 10. Stale gate row. |
| F3 | MAJOR | ANNOTATE's "observed token at `<lands>`" is base-pinned: the receipt prints `observed_lands='245'` for L01/L03 while the lands tree holds **247** `.md` files and the L03 row's own unpinned re-derivation command prints 247 at lands. Disclosed in prose, so no verdict flip. |
| F4 | MINOR | The counter's own USAGE block names `.ufo/waves/round-73/counters/accept-ca.py`, which is byte-identical to **r1** (the buggy revision), not the graded r3. |
| F5 | MINOR | L01/L02/L03 "re-derivation command" strings are not executable (`sh -c` syntax error: they embed prose `(count the .md paths) -> 245`); NOSTUB only checks the string is present. |
| F6 | MINOR | The Ca selftest receipts cite the claim-C path `reports/round-73/accept-c.py` (and its sha) but SEPARABLE's telemetry scan filters basenames without `ca`, so they are never scanned. |
| F7 | MINOR | No committed `ACCEPT-CA-73: PASS` receipt exists; the only committed `ACCEPT-CA-73` lines are three FAIL controls. The STAMP leg is satisfied only by live stdout. |

---

## F1 — BLOCKER: SEPARABLE's claim-C predicate is not applied to the added lines it reads

Frozen leg text (`claims.json`, Ca legs):

> SEPARABLE: no byte the Ca legs read (ledger, correction rows, Ca telemetry receipts) cites an S-id
> >= S876 or a claim-C path; count pairs measure at the pinned base revision so landing C cannot move them

The counter's own definition of a claim-C path (`reports/round-73/accept-ca.py:151-152`):

```
C_PATHS = ("corpus/knowledge/linguistics/conlang-scholarship", "corpus/lessons/round-73.md",
           "reports/round-73/accept-c.py", "reports/round-73/evidence", "corpus/SOURCES.md")
```

The leg **does** read in-place added lines (`accept-ca.py:805-810`), but applies only `SID_RE` to them:

```
    added = added_lines(root, base, lands, ("SKILL.md", "corpus/README.md",
                                            "README.md"))
    for line in added:
        for m in SID_RE.finditer(line):
            if int(m.group(1)) >= SEPARABLE_MIN_ID:
                problems.append("in-place added line cites S%s" % m.group(1))
```

A line the leg reads cites a claim-C path **at lands** — the `accept-c-73` gate row, which the Ca
landing commit `e62d731` added to `SKILL.md` (it names `reports/round-73/accept-c.py` twice):

```
$ cd /tmp/tmp.EkHQkZt8iO/lane
$ git diff -U0 8841ad3b896a0227674fa0725b818c999118046f..0316b8883b4f8d44b8efd720140e7f52f734a102 \
    -- SKILL.md corpus/README.md README.md | grep '^+' \
  | grep -nE 'corpus/lessons/round-73|corpus/knowledge/linguistics/conlang-scholarship|reports/round-73/accept-c\.py|reports/round-73/evidence|corpus/SOURCES\.md'
7:+| accept-c-73 | gate | `python3 -B reports/round-73/accept-c.py --root . --lands <40-hex>` | Output ends `ACCEPT-C-73: PASS` or `: FAIL legs=11/11`; 0 pass / 1 fail; 2 on a missing or malformed `--lands`. | `python3 -B reports/round-73/accept-c.py --selftest` (prints `SELFTEST: 29/29`) | base `8841ad3b…`, the five adopted registry rows (set in claims.json), both entry paths, evidence dir, the refused staged ids and campaign ids pinned in the script and in claims.json | read-only against `--lands` (materialized `git archive`); selftest builds `tempfile.mkdtemp` fixtures | kotodama-shokunin |
```

and the graded run still prints SEPARABLE green:

```
$ cd /tmp/tmp.EkHQkZt8iO/lane && python3 -B reports/round-73/accept-ca.py --root . \
    --lands 0316b8883b4f8d44b8efd720140e7f52f734a102 --fleet-root /home/vgpnk/Projects/shokunin
...
LEG PASS SEPARABLE
     scanned=['ledger', 'corrections-rows', 'reports/round-73/telemetry/controls-ca-r2.txt', 'reports/round-73/telemetry/controls-ca-r3.txt', 'reports/round-73/telemetry/controls-ca.txt', 'reports/round-73/telemetry/measures-ca72-rerun.txt'] problems=[]
...
ACCEPT-CA-73: PASS legs=9/9
EXIT=0
```

Both halves proved by mutation in the throwaway clone (`/tmp/tmp.Q8xmBaNyXO/lane`, main forced to the
mutant commit so STAMP is not the reason for a red):

```
# mutation A: a claim-C path in an added footer line
$ printf '\nMutation probe: a Ca-authorized footer line that names a claim-C path `corpus/lessons/round-73.md`.\n' >> corpus/README.md
$ git add corpus/README.md && git commit -q -m "mutation: C path in an in-place added footer line"   # f90640cf2b608a36ebf2a8f1fc73ad3460039bff
$ python3 -B reports/round-73/accept-ca.py --root . --lands f90640cf2b608a36ebf2a8f1fc73ad3460039bff --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS SEPARABLE
     scanned=[...] problems=[]
ACCEPT-CA-73: PASS legs=9/9
EXIT=0

# mutation B (positive control): an S-id >= 876 in an added footer line
$ printf '\nMutation probe 2: a footer line citing S876.\n' >> corpus/README.md && git commit -qam "mutation: S876 in an in-place added footer line"   # a4fe2ab
$ python3 -B reports/round-73/accept-ca.py --root . --lands a4fe2ab --fleet-root /home/vgpnk/Projects/shokunin
LEG FAIL SEPARABLE
     scanned=[...] problems=['in-place added line cites S876']
ACCEPT-CA-73: FAIL legs=8/9
EXIT=1
```

So the leg enforces `S876` on added lines but not `claim-C path`, and the landed tree already contains
the C path. Under the leg's wording (`no byte the Ca legs read … cites … a claim-C path`) SEPARABLE is
false at lands; the claim's kill rule ("any leg false at `<lands>` → the claim fails as declared") would
fire. **Caveat stated plainly:** a grader who reads the parenthetical `(ledger, correction rows, Ca
telemetry receipts)` as an exhaustive read set would treat the added-line scan as extra hardening and
downgrade this to MAJOR. The substantive separability of the *verdict* survives (all pairs are
base-pinned or independent of C), and the citation is documentation of C's gate, not a data dependency.

## F2 — BLOCKER: the `accept-ca-73` gate row documents a selftest output the graded counter no longer prints

```
$ cd /tmp/tmp.EkHQkZt8iO/lane && sed -n '704p' SKILL.md | grep -o 'prints `SELFTEST OK: [0-9]* scenarios`'
prints `SELFTEST OK: 9 scenarios`

$ python3 -B reports/round-73/accept-ca.py --selftest | tail -1
SELFTEST OK: 10 scenarios — do-nothing control (BASEMISMATCH found=2, REPAIR/ANNOTATE/NOSTUB FAIL), clean landing 9/9, stub-row control (ANNOTATE+NOSTUB FAIL), append-only removal FAIL, in-place-outside-footer FAIL, shell-string argv FAIL, min-pairs gate FAIL, authorized SKILL.md registry append 9/9, CLI exit 2 on a bad --lands
EXIT=0

$ grep -n 'SELFTEST OK: 10 scenarios' reports/round-73/accept-ca.py
1332:    print("SELFTEST OK: 10 scenarios — do-nothing control (BASEMISMATCH "
```

Provenance (the row was correct at `3537899` and went stale when `85f17eb` bumped the counter to r3
without touching `SKILL.md`):

```
$ for r in 3537899031508864c1b3deb7c5dc3a81cf2333db 85f17eb 0316b8883b4f8d44b8efd720140e7f52f734a102; do
    echo -n "$r: "; git show $r:SKILL.md | sed -n '704p' | grep -o 'prints `SELFTEST OK: [0-9]* scenarios`'; done
3537899031508864c1b3deb7c5dc3a81cf2333db: prints `SELFTEST OK: 9 scenarios`
85f17eb: prints `SELFTEST OK: 9 scenarios`
0316b8883b4f8d44b8efd720140e7f52f734a102: prints `SELFTEST OK: 9 scenarios`
$ git show --stat --oneline 85f17eb | grep -c SKILL.md
0
$ grep -n 'SELFTEST OK: 9 scenarios' reports/round-73/telemetry/selftest-r2.txt
6:SELFTEST OK: 9 scenarios — ...
```

`85f17eb` added `reports/round-73/telemetry/selftest-r3.txt` saying `SELFTEST OK: 10 scenarios`, so the
lane ships two contradictory statements about the same counter. This row is the one L08's
`statement_after` parse reads (`(?s).*\| (accept-[a-z]+-\d+) \|`), i.e. the Ca REPAIR statement itself.
`ExecSkillRows.md` F1 (independent seat) reached the same conclusion; I re-derived it here from the
counter bytes, not from that report.

## F3 — MAJOR: `observed_lands` is a base-pinned number, and the L03 row's own re-derivation command disagrees with its "new token" at lands

```
$ cd /tmp/tmp.EkHQkZt8iO/lane && python3 -B reports/round-73/accept-ca.py --root . --lands 0316b888... 
PAIR L01 disposition=ANNOTATE stated_at=corpus/README.md:732 stated='243' observed_base='245' observed_lands='245' expected_after='245'
PAIR L03 disposition=ANNOTATE stated_at=corpus/README.md:736 stated='243' observed_base='245' observed_lands='245' expected_after='245'

$ find corpus/knowledge -type f -name '*.md' | wc -l          # at LANDS
247
$ find corpus/knowledge -type f -name '*.md' | wc -l          # at BASE (/tmp/tmp.MMvOgnpOzL/lane)
245
$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge | grep '"files"'
    "files": 247,                                              # LANDS
    "files": 245,                                              # BASE
```

Cause: L01/L02/L03 `observe_cmd` hard-code `8841ad3b…`, so the field the receipt labels
`observed_lands` is the output of a command that cannot see lands (the ledger's `frozen_note` and the
SEPARABLE leg both declare this pinning: "count pairs measure at the pinned base revision so landing C
cannot move them"). The SCORECARD rows disclose 247 in prose, so a reader is not misled about the
current count:

```
$ awk '/^## Corrections — round 73/,0' SCORECARD.md | grep -o 'README footer line `Total knowledge entries: 247.` carried by claim C'
README footer line `Total knowledge entries: 247.` carried by claim C
```

but the ANNOTATE leg's wording ("the observed token at `<lands>`") and the receipt field are false as
lands observations, and the L03 row mixes a base-pinned token with an unpinned command:
`python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` prints
`"files": 247` at the graded revision while the row's new-token column says 245.

## F4 — MINOR: the counter's USAGE points at the superseded r1 copy

```
$ sha256sum .ufo/waves/round-73/counters/accept-ca.py reports/round-73/accept-ca.py
f8ebb5d849c9113d2d227494be0ec1403c746dd9124a505da0373e608bb97865  .ufo/waves/round-73/counters/accept-ca.py
222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89  reports/round-73/accept-ca.py
$ diff -q .ufo/waves/round-73/counters/accept-ca.py /tmp/ExecRerunCa/accept-ca-r1.py && echo IDENTICAL-TO-r1
IDENTICAL-TO-r1
$ grep -n '\.ufo/waves/round-73/counters/accept-ca.py' reports/round-73/accept-ca.py
121:  python3 -B .ufo/waves/round-73/counters/accept-ca.py --root . \
123:  python3 -B .ufo/waves/round-73/counters/accept-ca.py --selftest
```

The graded counter's docstring tells the operator to run a different, older file (r1: worktree-ledger
acceptance, `9 scenarios`). `counter-revisions.md` registers r1's bug, but nothing marks the scratch
copy stale.

## F5 — MINOR: three correction rows carry non-executable "re-derivation commands"

```
$ cd /tmp/tmp.EkHQkZt8iO/lane && sh -c 'git ls-tree -r --name-only 8841ad3b896a0227674fa0725b818c999118046f corpus/knowledge (count the .md paths) -> 245'
sh: -c: line 1: syntax error near unexpected token `('
$ python3 -B reports/round-73/accept-ca.py ... | grep NOSTUB
LEG PASS NOSTUB
     minimum-shape=id+stated+observed+rederive stubs=[]
```

L01, L02 and L03 embed prose (`(count the .md paths) -> 245`) inside the `rederive` string;
`leg_nostub` only checks the string is present verbatim in the row. L06's and L07's commands do run
and reproduce (`ACCEPT-CA-72: FAIL`; the eight ids).

## F6 — MINOR: Ca selftest receipts cite the claim-C path; the SEPARABLE telemetry filter skips them

```
$ grep -n "accept-c.py" reports/round-73/telemetry/selftest.txt reports/round-73/telemetry/selftest-r3.txt
reports/round-73/telemetry/selftest.txt:2:$ python3 -B reports/round-73/accept-c.py --selftest
reports/round-73/telemetry/selftest.txt:8:95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416  reports/round-73/accept-c.py
reports/round-73/telemetry/selftest-r3.txt:2:$ python3 -B reports/round-73/accept-c.py --selftest
reports/round-73/telemetry/selftest-r3.txt:8:95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416  reports/round-73/accept-c.py
$ sed -n '792p' reports/round-73/accept-ca.py
        if "ca" not in os.path.basename(path):
```

`claims.json`'s do-nothing control itself names `reports/round-73/telemetry/selftest.txt` as the Ca
selftest receipt; that receipt carries a C_PATHS member (`reports/round-73/accept-c.py`) and its sha,
and the scanner's basename filter means SEPARABLE never sees it. Combined with F1, SEPARABLE's
claim-C half is the weak half of the leg.

## F7 — MINOR: no committed positive receipt

```
$ grep -rn "ACCEPT-CA-73" reports/round-73/telemetry/ | cut -c1-90
reports/round-73/telemetry/controls-ca-r2.txt:41:ACCEPT-CA-73: FAIL legs=4/9
reports/round-73/telemetry/controls-ca-r3.txt:41:ACCEPT-CA-73: FAIL legs=4/9
reports/round-73/telemetry/controls-ca.txt:41:ACCEPT-CA-73: FAIL legs=5/9
$ grep -rl "ACCEPT-CA-73: PASS" reports/ | head
reports/round-73/claims.json
```

The STAMP leg speaks of "the receipt"; only the live stdout exists. I did check that the live stdout
satisfies the cited grammar (`tools/check-receipt-seq.py`):

```
$ python3 -B reports/round-73/accept-ca.py --root . --lands 0316b888... --fleet-root /home/vgpnk/Projects/shokunin > /tmp/ExecRerunCa/ca-lands-run.txt
$ python3 -B tools/check-receipt-seq.py --root . /tmp/ExecRerunCa/ca-lands-run.txt
SEQ-/tmp/ExecRerunCa/ca-lands-run.txt PASS stamped=0316b888 evaluated=0316b888 measured=0316b888 equal=True
TREE-/tmp/ExecRerunCa/ca-lands-run.txt PASS recorded=9b10fa06 actual=9b10fa06
RECEIPT-SEQ: PASS
```

---

## Re-derived PAIR lines (hand-run, base clone and lands clone)

Each ledger `observe_cmd` was executed with `cwd` set to the base clone and to the lands clone; the
output matches the graded receipt line for line.

| id | disp | observed @ base | observed @ lands | receipt line | match |
|---|---|---|---|---|---|
| L01 | ANNOTATE | `245` | `245` (command pins base; tree truth 247) | `observed_base='245' observed_lands='245'` | yes / pinned |
| L02 | ANNOTATE | `38` | `38` | `38` / `38` | yes |
| L03 | ANNOTATE | `245` | `245` (command pins base; tree truth 247) | `245` / `245` | yes / pinned |
| L04 | REPAIR | `505:## Error patterns` | `505:## Error patterns` | `505` / `505` | yes |
| L05 | REPAIR | `564:## Checklist (executable where a tool exists)` | same | `564` / `564` | yes |
| L06 | ANNOTATE | `ACCEPT-CA-72: FAIL` | `ACCEPT-CA-72: FAIL` | `FAIL` / `FAIL` | yes |
| L07 | ANNOTATE | `F1, F2/F3, F4, F5, F6, F8, F9, SCOUT-LIVE` | same | same / same | yes |
| L08 | REPAIR | `accept-ca-72` | `accept-ca-73` | `accept-ca-72` / `accept-ca-73` | yes |

Supporting hand checks: base `SCORECARD.md:1401` = "… ACCEPT-CA-72 PASS legs=12/12 at the measured
revision"; base `LOG.md:4280` = "pre-data corrections F1-F9 + SCOUT-LIVE documented there";
base `SKILL.md:697` = "| accept-o-69 | gate | …"; base `corpus/README.md` lines 407/732/736 =
`## culture-material/ (36)`, `Total knowledge entries: 243.`, `(total 243 files; directory totals
30/29/36/29/24/95).`; round-72 `pre_data_corrections` ids = `['F1','F2/F3','F4','F5','F6','F8','F9',
'SCOUT-LIVE']` (8, no F7); round-72 `measures-ca.txt:29` = `ACCEPT-CA-72: FAIL legs=12/12` with
`LEG FAIL REPORTCORR fleet-rev=MISSING` and `LEG FAIL REPORTLAST commits=10 report-names-lands=False`.
Base partition counts: civilizations 95 / culture-material 38 / linguistics 30 / myth-symbol 29 /
synthesis 29 / verification 24 = 245 — so the filed `36` and `243` are the only wrong cells, exactly
as L02/L03 say. `SHONEN.md:6` at lands reads `:505` / `:564` and keeps the old values in its
correction clause (`Pointers ':468'/':522' corrected to ':505'/…`); at base it reads `:468` / `:522`.

## Counter revisions r1 → r2 → r3 (disclosed differences are real; no undisclosed one)

```
$ sha256sum /tmp/ExecRerunCa/accept-ca-r1.py /tmp/ExecRerunCa/accept-ca-r2.py reports/round-73/accept-ca.py
f8ebb5d849c9113d2d227494be0ec1403c746dd9124a505da0373e608bb97865  r1
be1917950bfb992dc4be30be00c0f1bf3b317b6fc88bea2431344cafaec4cde0  r2
222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89  r3
$ git log --oneline --all -- reports/round-73/accept-ca.py
85f17eb round-73 C: ...; counter r3 + receipts
3537899 round-73 Ca: counter r2 ...
af65165 round-73: freeze ...
$ diff -u accept-ca-r1.py accept-ca-r2.py
-        r = git(clone, "show", "%s:%s" % (lands, rel))
+        r = git(clone["path"] if isinstance(clone, dict) else clone,
+                "show", "%s:%s" % (lands, rel))
$ diff -u accept-ca-r2.py reports/round-73/accept-ca.py
  +    if rel == LEDGER_REL:
  +        return None, "absent", None, "", \
  +            "ledger %s is not committed at %s (the default ledger is never read from the worktree)" % (rel, lands)
  +        # ---- 7b. a ledger present only in the worktree (not committed at lands) must fail LEDGER ----
  +        ... 15 lines ...
  -    print("SELFTEST OK: 9 scenarios — do-nothing control (BASEMISMATCH "
  +    print("SELFTEST OK: 10 scenarios — do-nothing control (BASEMISMATCH "
1 file changed, 19 insertions(+), 1 deletion(-)
```

Only three commits touch the file; the r1→r2 delta is exactly the disclosed `load_ledger` bug fix
(predicate unchanged: the frozen LEDGER leg already required committed bytes), and the r2→r3 delta is
exactly the disclosed default-path guard plus scenario 7b (and its message). No pair, leg, token,
threshold or kill rule moved. `red-before-r3.txt` reproduces: with only the guard removed
(`/tmp/ExecRerunCa/noguard.py`, sha `83af3df7…`), the selftest prints
`SELFTEST FAIL: wt-only LEDGER: got 'PASS' want 'FAIL'`, exit 1 — byte-identical to the committed
red-before line.

## Graded run, controls, historical revisions, selftest

```
# LANDS (graded) — PASS, exit 0
# stamped/evaluated/measured: 0316b8883b4f8d44b8efd720140e7f52f734a102, tree 9b10fa06a2d3,
# counter 222d4dd6d408, ledger source=lands sha256=c912401dd511…
ACCEPT-CA-73: PASS legs=9/9

# BASE, explicit --ledger, fresh clone whose main is lands — FAIL 4/9 (STAMP red: measured 0316b888 != lands base)
# BASE, r1 counter, main forced to base — FAIL 5/9, red REPAIR/ANNOTATE/NOSTUB/TRACKED, STAMP PASS  == controls-ca.txt
# BASE, r3 counter, main forced to 3537899 — FAIL 4/9, STAMP red as disclosed                    == controls-ca-r3.txt
# e62d731, r1 (main=e62d731) — FAIL 8/9, SEPARABLE red (in-place added line cites S876, S880)     == counter-revisions.md
# e62d731, r3              — FAIL 8/9, SEPARABLE red (same)
# 3537899, r2 (main=3537899) — PASS 9/9
# 3537899, r3                — PASS 9/9
```

The r1 receipt quoted in `counter-revisions.md` ("FAIL legs=8/9, SEPARABLE red for a separate reason,
ledger source=worktree-uncommitted") reproduces exactly, including the S876/S880 cause: the Ca
landing commit's own SKILL.md row text cited claim-C registry ids, and `3537899` rewrote that row text
to remove them (`git diff base..e62d731 -- SKILL.md` shows `five rows S876..S880`, lands shows
`the five adopted registry rows (set in claims.json)`).

Selftest at lands: `SELFTEST OK: 10 scenarios`, exit 0; it exercises the do-nothing control, clean
landing 9/9, stub-row control, append-only removal, in-place-outside-footer, shell-string argv,
min-pairs gate, authorized SKILL.md registry append 9/9, CLI exit 2 on bad `--lands`, and the
worktree-only ledger scenario. All scenario assertions are on leg states, not on prose.

## Round-72 counter re-run at its own stamp (L06's "R2 rerun")

```
$ cd /tmp/tmp.SUNkXz3gjN/lane   # checked out at 21ad3088cb64f7275e5541804e168f15d21d26d0
$ sha256sum reports/round-72/accept-ca.py
f080c240ffdc47f0453f4527e23d271112c999dc59d3d63d2703aae10880629f
$ python3 -B reports/round-72/accept-ca.py --root . --lands 21ad3088cb64f7275e5541804e168f15d21d26d0 \
    --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS QUAL20 … LEG PASS NOHARM (census exit=0)
ACCEPT-CA-72: PASS legs=12/12
EXIT=0
```

Matches `reports/round-73/telemetry/measures-ca72-rerun.txt` (same counter sha, same 12 legs, PASS).
The committed receipt `reports/round-72/telemetry/measures-ca.txt` still reads `FAIL legs=12/12` with
`REPORTCORR fleet-rev=MISSING` / `REPORTLAST report-names-lands=False` — so the L06 annotation ("true
at that revision only after the report landed; the filed row is never repaired") is sound. Fleet
side: `.ufo/reports/round-72/kotodama.md` is sha256 `ea256ae7f9d7…` both at the ledger's `fleet_pin`
`80d8c9b5` and at current fleet HEAD `0d1c5e51`, `git diff --numstat pin..HEAD` empty.

## Other admitted statements checked and true

- `SCORECARD.md` `## Corrections — round 73` facts: `243` written at `498db73` (round-71 claim C lands)
  and not reconciled — confirmed by `git log -S 'Total knowledge entries: 243' -- corpus/README.md`;
  the two uncounted round-72 culture-material files are `770100f`'s heritage-taxonomy pair — confirmed
  by `git log --diff-filter=A --name-only -- corpus/knowledge/culture-material`.
- `SHONEN.md` repair: lands line 6 says `:505` / `:564`, keeps `:468` / `:522` in its own correction
  clause, and `grep -n '^## Error patterns$' SKILL.md` → 505, `^## Checklist …` → 564 at lands.
- `L08`: exactly seven rows were inserted (`accept-c-71, accept-ca-71, accept-d-71, accept-c-72,
  accept-ca-72, accept-c-73, accept-ca-73`), last row id `accept-ca-73`.
- "The round-70 pair has no counter bytes in git (only receipts at 453676a2)": `git cat-file -t
  453676a2` → `commit`; `git ls-tree -r lands reports/round-70 | grep accept` → nothing.
- Measured side finding: `python3 -B reports/round-72/accept-c.py --selftest` at base prints
  `SELFTEST: 10/11`, `--- clean fixture: expected PASS 10/10, got exit=1`, exit 1 — exactly as the
  SCORECARD row says.
- APPENDONLY: `git diff --numstat base..lands -- LOG.md SCORECARD.md corpus/lessons/round-72.md
  corpus/lessons/round-71.md` → only `16 0 SCORECARD.md` (zero removals); `LOG.md:4280` and
  `SCORECARD.md:1401` are byte-identical at lands; `corpus/README.md` was changed only by appending at
  EOF (`git diff base..lands -- corpus/README.md` = one `@@ -761,3 +761,17 @@` append).
- TRACKED: both round-72 seat reports are absent at base, present at lands (`ScoutMergeScan.md` 13412 B,
  `ScribeLesson.md` 19765 B), committed by `e62d731`; their content is a seat-shaped report (assignment,
  verdict table, scratch paths, shas), not a stub.

## What I could NOT check

- **Authorship/provenance of the two round-72 seat reports** — only that they are tracked, non-empty,
  absent at base, committed by the Ca landing, and self-consistent as seat reports. Git cannot prove
  the named seats wrote them.
- **The exact environment of the committed receipts.** `STAMP`'s "measured revision (lane main)" is
  read from the *root repo's* `main` ref; in a fresh clone that ref points at the graded lands commit,
  so reproducing a historical receipt's STAMP requires forcing the clone-local `main` to that
  revision (I did that). `controls-ca-r3.txt` discloses the same clone-dependence.
- **The causal story behind round-72's `REPORTCORR`/`REPORTLAST` failure** — I verified the leg states
  (`fleet-rev=MISSING`, `report-names-lands=False`) and the post-report PASS, not the fleet timing.
- **Future fleet state.** `leg_appendonly` reads the *live* fleet repo (`git show fleet HEAD:…`), so
  the Ca verdict is not a function of the lane revision alone; today the pinned blob is unchanged.
- **Whether claims.json's "no seat has scored landed data" held for every other seat** — not my lane.
- **L07's "overstated the set by one slot"** — the id list is verified (8 ids, no F7); the phrase is a
  judgment about counting `F1-F9` as nine slots, and is defensible either as 1 (F7 missing) or 2 (F7
  missing plus F2/F3 merged) depending on whether ids or integers are counted.
- **Wave-1 dead seats** (`ConnectorSiblings`, `ScribeMistakes`, `ExecScratchMirror`): their reports are
  absent; nothing in the Ca measurement depends on them that I could see, and I did not attempt to
  reconstruct them.

## Bottom line for the judge

`ACCEPT-CA-73: PASS legs=9/9` is reproducible, the ledger and claims are byte-frozen, the revision
history is honestly disclosed, and all eight PAIR lines re-derive. It is **not** a clean pass: F1 is a
false green on the leg that exists to prove Ca does not lean on C (a Ca-added line citing
`reports/round-73/accept-c.py` passes), F2 is a false gate-row statement about the graded counter's
own selftest, and F3 mislabels a base-pinned number as a lands observation.
