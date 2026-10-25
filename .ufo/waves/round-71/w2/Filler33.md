# Filler33 — sentinel — variant 32

**Assignment:** re-run one frozen claim counting command at lane HEAD in a fresh clone; report exact
output + exit code; findings only.
**Command under test:** `reports/round-71/accept-c.py` (frozen claim-C counter).
**Verdict: command reproduces `ACCEPT-C-71: PASS`, exit 0, byte-identical output in a fresh clone of
lane HEAD — but the PASS certifies less than the counter's docstring claims (3 ungraded/vacuous legs,
F2–F4), and at the HEAD this seat started on (`14c88d9b`) the receipt the certified entry points at
was not in HEAD at all (F1). The lane advanced during the run and committed that receipt
(`c21213a`); re-run at the new HEAD `baf3b6a` still PASSes, exit 0, receipt present. Both revisions
are reported separately below — see §1b.**

Lane untouched: the only file this seat wrote is this report. All mutations were made in throwaway
copies under `/tmp/k71w2-f33/`. No packages installed or upgraded.

---

## 1. HEAD identity and fresh clone

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
$ git rev-parse HEAD
14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6
$ git rev-parse HEAD^{tree}
2a9f2ab5622b62a51c7f49df0577bd659ce191c8
$ git status --porcelain
?? reports/round-71/telemetry/measures-c.txt          # <-- untracked, see F1
$ jj log -r '@|@-' --no-graph
050a65a2278f                                           # empty working-copy commit
14c88d9b9bb3 round-71: wave-2 spec/plan/dispatch evidence (40 seats)
```

Fresh clone (no hardlinks, no working-copy state, no `.jj`, no untracked files):

```
$ git clone --quiet --no-hardlinks /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/k71w2-f33/clone
$ cd /tmp/k71w2-f33/clone && git rev-parse HEAD && git status --porcelain | wc -l
14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6
0
$ sha256sum reports/round-71/accept-c.py
1df995c2207c50f37f8e1b5187fa7b0cd0e985e54c7667c662105293628d5db4  reports/round-71/accept-c.py
$ git show HEAD:reports/round-71/accept-c.py | sha256sum
1df995c2207c50f37f8e1b5187fa7b0cd0e985e54c7667c662105293628d5db4  -
```

Counter bytes at HEAD == bytes on disk == the sha the claim-C receipt self-stamps. Environment:
Python 3.14.8, git 2.56.0, jj 0.45.1.

## 1b. HEAD moved during this run (both revisions reported)

The lane advanced while this seat was executing. Timeline, all from git, no inference:

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
$ git rev-parse HEAD          # at seat start, and for every result in §2–§3
14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6
$ git rev-parse HEAD          # at report time
baf3b6a65aef9bacc6319e8904c423b788dc8af6
$ git log --oneline --diff-filter=A -1 -- reports/round-71/telemetry/measures-c.txt
c21213a round-71: commit C receipt (measures-c.txt) + lesson R71-M5 (declared-counter defect) + w2 findings
$ git diff --stat 14c88d9b HEAD | tail -1
24 files changed, 5415 insertions(+), 1 deletion(-)      # SOURCES.md and the entry NOT among them
```

Re-run at the new HEAD, second fresh clone:

```
$ rm -rf /tmp/k71w2-f33/clone2
$ git clone --quiet --no-hardlinks /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/k71w2-f33/clone2
$ cd /tmp/k71w2-f33/clone2 && git rev-parse HEAD && git status --porcelain | wc -l
baf3b6a65aef9bacc6319e8904c423b788dc8af6
0
$ python3 -B reports/round-71/accept-c.py --root . ; echo $?
… 7× LEG PASS (identical detail strings to §2) …
ACCEPT-C-71: PASS
0
$ test -e reports/round-71/telemetry/measures-c.txt && echo receipt-present
receipt-present
$ git show HEAD:reports/round-71/accept-c.py | sha256sum
1df995c2207c50f37f8e1b5187fa7b0cd0e985e54c7667c662105293628d5db4  -     # counter unchanged
$ git show HEAD:reports/round-71/telemetry/measures-c.txt | sha256sum
1d4467a6c52c679342954bc6de63b9f8b7b19eefb88816f4ca03ea1dad0c9efe  -     # receipt now in HEAD
```

Because the counter bytes are identical at `14c88d9b` and `baf3b6a`, and neither `corpus/SOURCES.md`
nor the entry changed between them, the §2 output applies unchanged to both revisions. The three
mutating probes (F2–F4) were re-run at `baf3b6a` and reproduce identically:

```
F2@baf3b6a EXIT=0  topic-lines=0   → LEG PASS SWEEP (topic-owners=[]) , ACCEPT-C-71: PASS
F3@baf3b6a EXIT=0  find-count=37   → LEG PASS COUNTS (36/243)     , ACCEPT-C-71: PASS
F4@baf3b6a EXIT=0  opened=2024-01-01 → LEG PASS ROWS              , ACCEPT-C-71: PASS
```


## 2. Exact command, exact output, exit code

```
$ cd /tmp/k71w2-f33/clone
$ python3 -B reports/round-71/accept-c.py --root .
LEG PASS ENTRY
     corpus/knowledge/culture-material/dance-performance-movement-codes.md
LEG PASS COUNTS
     culture-material=36 corpus=243 (want 36/243)
LEG PASS CITED
     distinct S-ids cited=13 (want >=12)
LEG PASS ROWS
     missing=[] not-mined=[] usedby-missing=[]
LEG PASS USEDBY-PATHS
     missing-paths=[]
LEG PASS CITED-LINES
     exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
LEG PASS SWEEP
     filename-owners=['corpus/knowledge/culture-material/dance-performance-movement-codes.md'] topic-owners=['corpus/knowledge/culture-material/dance-performance-movement-codes.md:20:- topic: how cultures codify the moving body — movement vocabulary, notation systems, dance-song-voice coupling, festival-ritual performance, and the social/role codes of performance — as a design system for invented cultures.']
ACCEPT-C-71: PASS
$ echo $?
0
```

stderr: empty (0 bytes). Re-run in the same clone: stdout byte-identical (`cmp` clean), exit 0.
Same command in the live lane: stdout byte-identical (`diff` clean), exit 0 — no leg depends on
working-copy-only or untracked bytes.

**PASS.** 7/7 legs pass, exit 0, reproducible, clone == lane.

## 3. Independent re-derivation at HEAD (counter-independent)

| Fact | Independent command | Result | Matches counter |
|---|---|---|---|
| culture-material `.md` count | `find corpus/knowledge/culture-material -type f \| wc -l` | 36 | yes |
| corpus total | `find corpus/knowledge -type f -name '*.md' \| wc -l` | 243 | yes |
| cited ids | regex over entry | `S861…S873`, exactly 13, no extras | yes |
| registry rows | `grep -cE '^\s{0,3}\|\s*S[0-9]{3,}\s*\|' corpus/SOURCES.md` | 797 | yes (receipt says 797) |
| 13 rows mined, used-by entry | cell parse | 13/13 `mined`, used-by = entry path | yes |
| 13 rows opened this round | cell parse | 13/13 `opened=2026-10-25`, tier A×12 / B×1 | **not checked by counter (F4)** |
| cited-line discipline | `python3 -B tools/check-cited-lines.py <entry>` | `0 finding(s) in 1 file(s)`, exit 0 | yes |

The claim's data predicate genuinely holds at HEAD: 13 new rows, all mined, all used by the entry,
counts 36/243, one topic owner, zero cited-line findings.

Reproduction at the receipt's stamped revision (not just HEAD):

```
$ git worktree add --quiet --detach /tmp/k71w2-f33/at8c 8c203bd9
$ cd /tmp/k71w2-f33/at8c && python3 -B reports/round-71/accept-c.py --root . | tail -1 ; echo $?
ACCEPT-C-71: PASS
0
$ git rev-parse 8c203bd9^{tree}
ffb5c5497e788d8dbecb6079c7be37cc5fdbd33a      # == receipt's "# tree:" line
```

`8c203bd9` is an ancestor of HEAD; between it and HEAD only `corpus/SOURCES.md` changed (1 line, the
S860 verify-at correction), which no claim-C leg reads — so the HEAD PASS is consistent with the
stamped receipt.

---

## 4. Findings

### F1 — was HIGH at `14c88d9b`; RESOLVED at `baf3b6a` (receipt committed `c21213a`)

**State at seat-start HEAD `14c88d9b`** — the committed entry cited a path that did not exist in that
tree:

```
$ cd /tmp/k71w2-f33/clone          # fresh clone of 14c88d9b
$ test -e reports/round-71/telemetry/measures-c.txt && echo present || echo ABSENT
ABSENT
$ sed -n '17p' corpus/knowledge/culture-material/dance-performance-movement-codes.md
- recheck: 180d — re-open the 13 rows' URLs/captures and re-locate the quoted spans (commit receipts: reports/round-71/telemetry/measures-c.txt)
$ git ls-tree --name-only HEAD reports/round-71/telemetry/
reports/round-71/telemetry/census-end.txt
reports/round-71/telemetry/census-start.txt
reports/round-71/telemetry/controls-c.txt
reports/round-71/telemetry/controls-ca.txt
reports/round-71/telemetry/controls-d.txt
reports/round-71/telemetry/measures-ca.txt
reports/round-71/telemetry/measures-d.txt
reports/round-71/telemetry/quarantine-verdicts.md
```

`measures-c.txt` existed only as an **untracked** file in the live lane (`git status` → `??`), and was
absent even at its own stamped revision `8c203bd9`:

```
$ cd /tmp/k71w2-f33/at8c && test -e reports/round-71/telemetry/measures-c.txt && echo present || echo ABSENT
ABSENT
```

That is a dead evidence pointer at that revision — `corpus/lessons/round-63-verifier-spotcheck.md`
item 2 ("Dead evidence pointer … a pointer must resolve at closure"). It also meant claim C, uniquely
among the round-71 claims, had a committed *control* (`controls-c.txt`) but no committed *measure*.

**Resolution.** Commit `c21213a` added the receipt; at the new HEAD `baf3b6a` the pointer resolves and
the receipt bytes (sha256 `1d4467a6…`) are exactly the bytes I read as untracked before the commit
(same 15 lines, same self-stamped counter sha `1df995c2…`, same `measured revision 8c203bd9`, same
`tree ffb5c549…`, same `ACCEPT-C-71: PASS` body). No rewrite of a filed round occurred.

**Residual (LOW, still open).** The receipt stamps `measured revision 8c203bd9` — an ancestor, not the
revision it is committed at — and states `measured in a materialized clone at the lands commit`. That
is reproducible (I re-ran at `8c203bd9`: PASS, exit 0, counter sha `1df995c2…`, tree `ffb5c549…`
matches the receipt), so it is protocol-conformant; the only gap is that the receipt does not record
the commit that landed it, so a reader at `baf3b6a` must use `git log --diff-filter=A` to find
`c21213a`. Optional one-line addition at next touch; nothing to re-run.

**Lesson for the round.** The wave-2 seat brief was issued against a HEAD that did not yet contain the
claim-C receipt; a verifier reading HEAD at dispatch time would have reported a dead pointer, and one
reading it minutes later would not. Any "reproduce at lane HEAD" verdict must name the revision it
measured, or it is not comparable (the R64/R67 class).


### F2 — MEDIUM — SWEEP leg passes vacuously when the entry has no topic line

`all(...)` over an empty list is `True`, so zero topic owners satisfies the leg:

```
$ cp -a clone pA && cd pA
# delete the entry's single "- topic:" line (line 20), then:
$ python3 -B reports/round-71/accept-c.py --root .
LEG PASS ENTRY … LEG PASS COUNTS … LEG PASS CITED … LEG PASS ROWS … LEG PASS USEDBY-PATHS …
LEG PASS CITED-LINES … LEG PASS SWEEP
     filename-owners=[…] topic-owners=[]
ACCEPT-C-71: PASS
$ echo $?
0
$ grep -c '^- topic:' corpus/knowledge/culture-material/dance-performance-movement-codes.md
0
```

An entry that lost its required topic line still certifies claim C. **Remediation:** require
`len(topic_owners) == 1` (and `startswith(ENTRY + ":")`), not `<= 1`.

### F3 — MEDIUM — COUNTS leg does not implement the method its docstring claims

Docstring: "partition count 35 -> 36 and corpus total 242 -> 243 (**find | wc -l**, not inventory
summary)". Code: non-recursive `os.listdir` + `.md` suffix filter. A file nested inside the partition
is invisible to the counter while the documented method disagrees:

```
$ cp -a clone pD && cd pD && mkdir -p corpus/knowledge/culture-material/nested && printf '# nested\n' > corpus/knowledge/culture-material/nested/x.md
$ find corpus/knowledge/culture-material -type f | wc -l
37
$ find corpus/knowledge -type f -name '*.md' | wc -l
244
$ python3 -B reports/round-71/accept-c.py --root .
LEG PASS COUNTS
     culture-material=36 corpus=243 (want 36/243)
ACCEPT-C-71: PASS        # exit 0
```

Latent today (no subdirectories or non-`.md` files in the partition at HEAD — verified), but the
counter would silently accept a partition whose true `find` count drifted. **Remediation:** count with
`os.walk`/`find` semantics, or amend the docstring to state the listdir+`.md` method.

### F4 — MEDIUM — the "S ids opened this round" property is never read

Docstring: "cites >=12 NEW SOURCES rows (S ids opened this round, status mined, used-by lists the
entry path)". The counter reads `cells[8]` (status) and `cells[11]` (used-by); it never reads
`cells[9]` (opened). A pre-round row satisfies every leg:

```
$ cp -a clone pB && cd pB   # set S861 opened cell to 2024-01-01, everything else unchanged
$ awk -F'|' '/^\| S861 /{print "status=" $9 " opened=" $10}' corpus/SOURCES.md
status= mined  opened= 2024-01-01
$ python3 -B reports/round-71/accept-c.py --root .
LEG PASS CITED … LEG PASS ROWS … LEG PASS CITED-LINES … ACCEPT-C-71: PASS   # exit 0
```

The *fact* currently holds (13/13 `opened=2026-10-25`), but the frozen claim's "NEW" quantifier is
ungraded — the counter cannot distinguish this round's rows from old ones. **Remediation:** add a leg
`opened == <round date>` for the cited set, or pin the accepted id range (S861–S873).

### F5 — LOW — documented `exit 2 (input error)` is unreachable; missing input exits 1

```
$ python3 -B clone/reports/round-71/accept-c.py --root /tmp/k71w2-f33/does-not-exist
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/k71w2-f33/does-not-exist/corpus/knowledge/culture-material'
$ echo $?
1
```

A missing/wrong `--root` is indistinguishable from a craft FAIL — the same class
`reports/round-71/accept-d.py` was written to fix for a missing git store (there: exit 2 /
`COULD-NOT-EVALUATE`). **Remediation:** guard the four input opens and return 2.

### F6 — LOW — dead variable: the partition count is computed and never graded

`corpus = len([f for f in os.listdir(...) if os.path.isdir(...)])` is assigned and never used; only
`ctotal` (the sum) is compared. HEAD has 6 partition directories; the docstring's "partition count
35 -> 36" wording refers to files in culture-material, so the dead variable is also misleading.
**Remediation:** delete it, or grade `cm`/`ctotal` against named expectations.

### F7 — NOTE — CITED leg counts tokens over the whole file, not citations

`TOKEN_RE.findall(text)` scans every byte of the entry, so an S-id in prose or a table counts toward
`>=12`. The ROWS leg (mined + used-by) and `tools/check-cited-lines.py` (exit 0 here) close most of
the hole; the CITED leg alone would not. No action required for this round; worth tightening if the
leg is ever cited as the citation measure.

---

## 5. Disposition

- **Claim-C counter at `14c88d9b` (seat-start HEAD): PASS, exit 0, 7/7 legs, reproducible in a fresh
  clone, byte-identical to the live lane.** Independent re-derivation confirms the underlying facts
  (36/243, 13 new rows S861–S873 all mined with used-by the entry, 0 cited-line findings, one topic
  owner).
- **Claim-C counter at `baf3b6a` (HEAD at report time): PASS, exit 0, same 7/7 legs, receipt
  present.** Counter bytes unchanged (`1df995c2…`); nothing the counter reads changed between the two
  revisions.
- **F1 is closed.** At `14c88d9b` the entry's receipt pointer did not resolve (untracked
  `measures-c.txt`, absent from HEAD and from its own stamped revision); commit `c21213a` landed the
  receipt with the same bytes and it resolves at `baf3b6a`. Residual LOW: the receipt does not record
  the commit that landed it.
- **F2–F4 remain open against the counter code** (SWEEP passes with zero topic owners; COUNTS uses
  `listdir` rather than the docstring's `find | wc -l`; the "opened this round" column is never read).
  None turns today's green into a red — each is a one-leg repair, and the underlying facts I
  re-derived independently all hold.
- **F5–F7 are hygiene** (unreachable documented exit 2 / missing input graded as exit 1; dead
  `corpus` variable; CITED counts tokens anywhere in the file).
