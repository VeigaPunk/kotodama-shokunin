# Round 76 — RevengerMistakes (wave 1, leaf): the mistake class that files a number against the artifact in hand

Seat `RevengerMistakes`, wave 1, leaf (no delegation, no background jobs). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
base `98c486bdb4650ba5b8e651d332910e8ee60ad121`. Every repo read below is `git -C <lane> show <rev>:<path>` or a read under the lane;
no tracked lane byte was written; this seat wrote only under `.ufo/waves/round-76/w1/`, and no fleet-root byte and no
`shokuknow` byte was written. The "fixture" is a file (repaired copy of the lesson), not a git
repository, so no identity/toplevel assertion was owed. Scratch `/fast/scratch/hyaku/kotodama-r76/RevengerMistakes/` was deleted before
yield; the receipts live at `.ufo/waves/round-76/w1/stage/RevengerMistakes/` (`SHA256SUMS.txt` there). Tool installs: **none**.

**Verdict.** Round 76's `## Mistakes` row is **`attribution`**: a number is read from the artifact the author had in hand — a staged
copy, the probe-receipt set, a plan — and filed in a sentence whose subject is a different artifact (the landed path, the committed
evidence, the receipt). It recurs in rounds 73, 74 and 75, and the criterion captured against it in round 75
(`corpus/QUALITY.md:127`, criterion 27) did not fire: its Check reads only Gate reject rows, and its selector matches **0** rows of the
very lesson that carries the defects. Round 75's own `## Mistakes` records none of the three sites (its rows are M1 sequencing,
M2 instrument, M3 number-drift). The fix ships with a red-before: one line, **six** numbers non-clean at base, exit 0 after exactly
those six cells are repaired.

## 1. The class, and why not `number-drift`

The vocabulary's two candidates are `number-drift` and `attribution`. The recorded round-74/75 rows under `number-drift`
(R74-M4, R75-M3) are prose counts that disagree with a receipt; the recorded `attribution` row (R74-M5) is a register row binding a
URL to the *next* row's quote. The three sites below are the R74-M5 shape, not the R74-M4 shape: each number is **true of another
artifact** at the same moment. The staged copies really are 6862/5933/2514 B; the probe-receipt set really does carry three
whole-document windows; the probe receipt for S885 really does say 111486 B. Nothing drifted with time — the number was bound to the
wrong object, and the object named in the sentence says something else. The round-75 wave-3 seat reached the same reading
independently: `.ufo/waves/round-75/w3/ExecCountsSweep.md:97` says F5's numbers are "simply the wrong artifact — QUALITY 27's class,
in the triage prose". `attribution` is therefore the class, and criterion 27 is the captured criterion that was supposed to catch it.

## 2. The three sites, measured at base

All at `98c486b`, all re-derived by me (no reliance on the wave-3 report for the numbers).

| # | lesson site (at base) | what it states | what the artifact it names says | command |
|---|---|---|---|---|
| 1 | `corpus/lessons/round-75.md:92-95` | the three adopted entries are `6862 B` / `5933 B` / `2514 B` | the lane paths named in the same sentence are `30920` / `24166` / `23049` B; `6862/5933/2514` are exactly the staged `shokuknow` copies | `git -C $L cat-file -s 98c486b:corpus/knowledge/myth-symbol/narrative-structure-frameworks.md` → `30920`; `wc -c /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/myth-symbol/narrative-structure-frameworks.md` → `6862` |
| 2 | `corpus/lessons/round-75.md:53-56` and `:325-326` | "Whole-document windows are honest here, **three times** … The other **six** declare `excerpt`"; "this round exercises it **three times**" | `reports/round-75/evidence/*.txt` carries **four** whole-document (S885, S886, S887, **S891**) and **five** excerpt — the "three" is the probe-receipt histogram (receipts exist for S885/S886/S887/S888/S889/S890/S892 only) | `git -C $L grep -c 'window-scope: whole-document' 98c486b -- 'reports/round-75/evidence/S*.txt'` → S885:1, S886:1, S887:1, S891:1 |
| 3 | `corpus/lessons/round-75.md:28` | S885 evidence capture "HTTP 200, **111486 B**, body sha256 `2bcdd019…`" | `reports/round-75/evidence/S885.txt` says `bytes: 109588`, `sha256: 20b571d7…` — the cell carries the probe receipt's bytes | `git -C $L show 98c486b:reports/round-75/evidence/S885.txt \| sed -n '5,6p'` → `bytes: 109588` / `sha256: 20b571d7a6a9…` |

Raw receipts for all three are in `stage/RevengerMistakes/recurrence.txt` (the file prints each command above its output).

## 3. Recurrence across rounds — the point of the row

| round | recorded row / finding | stated | observed | command (raw output in `recurrence.txt`) |
|---|---|---|---|---|
| 73 | R73-M2 (`reference-drift`) | `SCORECARD.md:1401` "ACCEPT-CA-72 **PASS** legs=12/12" | `reports/round-72/telemetry/measures-ca.txt` "ACCEPT-CA-72: **FAIL** legs=12/12" | `sed -n '1401p'` / `grep -o 'ACCEPT-CA-72: [A-Z]* legs=[0-9/]*'` |
| 74 | R74-M4 (`number-drift`) | `LOG.md:4297` "Ca **9** scenarios" | `selftest-r3.txt:6` "SELFTEST OK: **10** scenarios" | `sed -n '4297p'` / `sed -n '6p'` |
| 74 | R74-M5 (`attribution`) | register S816/S817 bind each URL to the next row's quote | — | recorded row, `corpus/lessons/round-74.md` `## Mistakes` |
| 75 | R75-M3 (`number-drift`) | w1 draft "**eleven** ledger pairs (4 REPAIR, 7 ANNOTATE)" | `reports/round-75/ledger.json` **10** pairs, 6 REPAIR / 4 ANNOTATE | `python3 -c '…print(len(d["pairs"]))'` → `10` |
| 75 | **not recorded** — §2 above | three/four windows; staged/landed sizes; receipt/evidence bytes | as §2 | as §2 |

R73-M2 is classified `reference-drift` in the round-73 lesson, and its mechanism is a verdict token taken from the count instead of
the receipt's verdict field — the same binding error under another label. I note the label rather than silently reclassify it.

## 4. Captured-by: QUALITY 27 was captured and did not fire

`git -C $L show 98c486b:corpus/QUALITY.md | sed -n '127p'` begins:

```
27. **A reject reason names the artifact it was observed on** — … A finding observed on one artifact is never filed against another …
```

It was captured in round 75 out of R74-M5, and the round's own lesson then carried three instances it does not reach, because:

- its Check (`corpus/QUALITY.md:129`) reads "one line over the round's lesson at `<lands>`, printing one verdict line per reject
  row" — the three sites are a Gate **note**, the **triage prose**, and a Gate **cell**;
- its selector (`corpus/QUALITY.md:132`, `grep -E "^\|.*\| *refused *\|$"`) is inert on the lesson it was dispatched for. Measured at
  base:

```
$ git -C $L show 98c486b:corpus/lessons/round-75.md | grep -cE '^\|.*\| *refused *\|$'
0
$ git -C $L show 98c486b:corpus/lessons/round-75.md | grep -icE '^\|.*(refused|rejected)'
11
```

So the rule exists, the check selected nothing, and no criterion covered a number in prose. That is the "recurs despite a captured
criterion" condition this seat was asked to find, and it is why the fix below is a criterion plus a check rather than a prose note.

## 5. The fix, with its red-before

The check is one line (`stage/RevengerMistakes/check-filed-numbers.sh`, sha256 `d8c9be12ad20…`). It reads a lesson file and a revision
and re-derives, from that revision: (a) every `` `path` (`N` B) `` cell against `git cat-file -s <rev>:corpus/knowledge/<path>`, and
(b) the whole-document / excerpt histogram the lesson states against `reports/round-75/evidence/*.txt`. It exits non-clean on any
mismatch.

```sh
exec python3 -c 'import re,sys,subprocess as sp;L="/home/vgpnk/Projects/shokunin/kotodama-shokunin";W={n:i for i,n in enumerate("zero one two three four five six seven eight nine ten".split())};t=open(sys.argv[1],encoding="utf-8").read();rev=sys.argv[2];sz=[(p,int(n),next((int(sp.run(["git","-C",L,"cat-file","-s",rev+":"+c],capture_output=True,text=True).stdout) for c in ("corpus/knowledge/"+p,p) if sp.run(["git","-C",L,"cat-file","-e",rev+":"+c],capture_output=True).returncode==0),None)) for p,n in re.findall(r"`([^`]+\.md)` \((\d+) B\)",t)];files=sp.run(["git","-C",L,"ls-tree","-r","--name-only",rev,"reports/round-75/evidence/"],capture_output=True,text=True,check=True).stdout.split();bodies={f:sp.run(["git","-C",L,"show",rev+":"+f],capture_output=True,text=True,check=True).stdout for f in files};whole=[f for f in files if "window-scope: whole-document" in bodies[f]];exc=[f for f in files if "window-scope: excerpt" in bodies[f]];words=re.findall(r"(?:Whole-document windows are honest here,|exercises it) (\w+) times",t);stated=[W.get(w,-1) for w in words];e=re.search(r"The other (\w+) declare `excerpt`",t);s2=W.get(e.group(1),-2) if e else -2;[print("SIZE   {}: lesson says {} B, {} at {} = {} B  {}".format(p,n,"the lane path" if o is not None else "NO SUCH PATH",rev,o,"ok" if n==o else "MISMATCH")) for p,n,o in sz];print("HIST   whole-document: lesson states {} -> {} file(s) {}  {}".format(list(zip(words,stated)),len(whole),sorted(f.rsplit("/",1)[1] for f in whole),"ok" if all(n==len(whole) for n in stated) else "MISMATCH"));print("HIST   excerpt:        lesson states {} -> {} file(s) {}  {}".format((e.group(1),s2) if e else None,len(exc),sorted(f.rsplit("/",1)[1] for f in exc),"ok" if s2==len(exc) else "MISMATCH"));bad=[x for x in sz if x[1]!=x[2]]+[w for w,n in zip(words,stated) if n!=len(whole)]+(["other="+str(s2)] if s2!=len(exc) else []);print("VERDICT: "+("ok" if not bad else "MISFILED — {} number(s) in the lesson do not equal the artifact the sentence names, at {}".format(len(bad),rev)));sys.exit(0 if not bad else 1)' "$@"
```

### 5.1 Red-before — the round-75 lesson at base (exit 1, six cells)

`sh check-filed-numbers.sh lesson-base.md 98c486bdb4650ba5b8e651d332910e8ee60ad121`; `lesson-base.md` is
`git show 98c486b:corpus/lessons/round-75.md` (sha256 `3271c3f76bdd…`, equal to the git blob):

```
SIZE   myth-symbol/narrative-structure-frameworks.md: lesson says 6862 B, the lane path at 98c486bdb4650ba5b8e651d332910e8ee60ad121 = 30920 B  MISMATCH
SIZE   myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md: lesson says 5933 B, the lane path at 98c486bdb4650ba5b8e651d332910e8ee60ad121 = 24166 B  MISMATCH
SIZE   myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md: lesson says 2514 B, the lane path at 98c486bdb4650ba5b8e651d332910e8ee60ad121 = 23049 B  MISMATCH
HIST   whole-document: lesson states [('three', 3), ('three', 3)] -> 4 file(s) ['S885.txt', 'S886.txt', 'S887.txt', 'S891.txt']  MISMATCH
HIST   excerpt:        lesson states ('six', 6) -> 5 file(s) ['S888.txt', 'S889.txt', 'S890.txt', 'S892.txt', 'S893.txt']  MISMATCH
VERDICT: MISFILED — 6 number(s) in the lesson do not equal the artifact the sentence names, at 98c486bdb4650ba5b8e651d332910e8ee60ad121
exit=1
```

### 5.2 The fixture — six cells repaired, nothing else

`diff -u lesson-base.md lesson-repaired.md` (`stage/RevengerMistakes/fixture-diff.txt`; the fixture sha256 is `42c9f7401b0d…`):

```
-3. **Whole-document windows are honest here, three times.** S885 (3720 visible chars), S886 (3526) and
-   S887 (3073) are each shorter than the 4096-character floor, so `window-scope: whole-document` is the
-   maximum available — the round-74 R74-M6 allowance, used as written. The other six declare `excerpt`
+3. **Whole-document windows are honest here, four times.** S885 (3720 visible chars), S886 (3526), S887 (3073) and S891 (2169) are each shorter than the 4096-character floor, so `window-scope: whole-document` is the
+   maximum available — the round-74 R74-M6 allowance, used as written. The other five declare `excerpt`
-- **Adopted (3, from 3 staged entries):** `myth-symbol/narrative-structure-frameworks.md` (6862 B),
-  `myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md` (5933 B),
-  `myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md` (2514 B). The first two are the
+- **Adopted (3, from 3 staged entries):** `myth-symbol/narrative-structure-frameworks.md` (30920 B),
+  `myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md` (24166 B),
+  `myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md` (23049 B). The first two are the
-  `window-scope: whole-document` allowance is the fix, and this round exercises it three times (Gate
+  `window-scope: whole-document` allowance is the fix, and this round exercises it four times (Gate
```

### 5.3 Green — same check, repaired fixture (exit 0, every cell `ok`)

```
SIZE   myth-symbol/narrative-structure-frameworks.md: lesson says 30920 B, the lane path at 98c486bdb4650ba5b8e651d332910e8ee60ad121 = 30920 B  ok
SIZE   myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md: lesson says 24166 B, the lane path at 98c486bdb4650ba5b8e651d332910e8ee60ad121 = 24166 B  ok
SIZE   myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md: lesson says 23049 B, the lane path at 98c486bdb4650ba5b8e651d332910e8ee60ad121 = 23049 B  ok
HIST   whole-document: lesson states [('four', 4), ('four', 4)] -> 4 file(s) ['S885.txt', 'S886.txt', 'S887.txt', 'S891.txt']  ok
HIST   excerpt:        lesson states ('five', 5) -> 5 file(s) ['S888.txt', 'S889.txt', 'S890.txt', 'S892.txt', 'S893.txt']  ok
VERDICT: ok
exit=0
```

### 5.4 Criterion form (prints nothing when green)

```
$ sh check-filed-numbers.sh lesson-repaired.md 98c486b… | grep -E 'MISMATCH|MISFILED' | wc -l
0
```

## 6. What the round must land for this row

1. **QUALITY 29 (new; extends 27).** Proposed text, in the file's own shape:

   > **29. Every number filed about the repo names the artifact it was read from** — adds to criteria 12, 17, 19, 23 and 27.
   > Criterion 27 binds a Gate *reject reason* to the artifact it was observed on; this binds every number a round files — a count, a
   > byte size, a digest, a receipt verdict, a scenario tally — in any of its bytes (lesson, claims, ledger, SCORECARD row, entry
   > provenance): the number is re-derived from an artifact named in the same sentence (repo path + revision, or receipt + field) and
   > equals it. A number whose artifact is a staged copy, a probe receipt, a draft or a plan, while the sentence names the landed path,
   > the committed evidence or the receipt, is `MISFILED` even when the number is true of the artifact it came from.
   > *Check (red-before, pre-dispatch)* — the one-liner in §5, run over the previous round's lesson at the lands revision, filtered with
   > `grep -E 'MISMATCH|MISFILED'`; it must print nothing. Measured 2026-10-27 at `98c486b` (round-76 base): the round-75 lesson prints
   > six lines. *Limits, stated* — it reads the two shapes that lesson uses (`` `path` (`N` B) `` cells, and the
   > whole-document/excerpt histogram); a number in another shape, or one whose artifact is not a repo path, still needs a reader.

2. **Claim Ca carries the pair(s).** The round-76 Ca ledger already draws its sources from `ExecCountsSweep` F1-F13, the spotcheck §7
   and the round-75 `## Routed to round 76`; each of the six cells is a pair of the declared shape. The pair should carry the artifact
   explicitly — `artifact: corpus/lessons/round-75.md@98c486b…` plus the `observe` command — and `accept-ca.py`'s LEDGER leg should
   re-run `observe` and require its output to equal the pair's `observed` token; a pair with no `artifact:` is refused, which is the
   counter-side enforcement of criterion 29.

3. **Disposition.** `corpus/lessons/round-75.md` is append-only, so ANNOTATE: a row under `## Corrections — round 76` in
   `SCORECARD.md` carrying old token, new token (the six values in §5.2) and the re-derivation command. No REPAIR is needed for this
   instance — the false cells live only in the append-only lesson. `QUALITY.md` and the Ca counter are the mutable files that change.

## 7. Proposed `## Mistakes` row (paste-ready; the scribe assigns the final id)

```markdown
| R76-M1 | attribution | A filed number is read from the artifact the author had in hand and filed in a sentence whose subject is another artifact. Round 75: `corpus/lessons/round-75.md:92-95` states the three adopted entries are `6862 B`/`5933 B`/`2514 B` while the lane paths it names are `30920`/`24166`/`23049` — the stated trio is exactly the staged `shokuknow` copies (`wc -c` → 6862/5933/2514); `:53-56` says "Whole-document windows … three times … The other six declare `excerpt`" and `:325` repeats "three times" while `reports/round-75/evidence/*.txt` at base carries 4 whole-document (S885, S886, S887, **S891**) / 5 excerpt, i.e. the probe-receipt histogram (receipts exist for seven rows, not for S891/S893); `:28` files the probe receipt's `111486 B`/`2bcdd019…` as S885's evidence capture while `reports/round-75/evidence/S885.txt` says `109588`/`20b571d7…`. Same mechanism recorded as R74-M5 (attribution), R74-M4 and R75-M3 (number-drift), R73-M2 (reference-drift); commands in `.ufo/waves/round-76/w1/stage/RevengerMistakes/recurrence.txt` | `corpus/QUALITY.md:127` criterion 27 — captured after R74-M5 with the very rule "a finding observed on one artifact is never filed against another", but its Check reads only Gate reject rows and its selector matches none of this lesson: `git show 98c486b:corpus/lessons/round-75.md \| grep -cE '^\|.*\| *refused *\|$'` → `0` (loosened: `11`). Round 75's `## Mistakes` records none of the three sites | QUALITY 29 (§6.1) with the shipped one-line check; claim Ca carries each cell as a pair with an explicit `artifact:` and `accept-ca.py`'s LEDGER leg refuses a pair whose `observe` output ≠ its `observed` token. Red-before: `.ufo/waves/round-76/w1/stage/RevengerMistakes/check-filed-numbers.sh <lesson> 98c486b…` exits 1 printing six cells; on the fixture with only those six repaired it exits 0 (`red-filed-numbers.txt`, `green-filed-numbers.txt`, `fixture-diff.txt`) | proposed (red-before shown) |
```

## 8. Limits and what was not run

- The check covers the two shapes this lesson uses. It does **not** cover Gate cells whose bytes sit in one column and whose artifact is
  named in another (§2 site 3 was measured by hand); nor a prose count in any other grammar. That is stated as the criterion's limit,
  not papered over.
- Not run: `accept-c.py` / `accept-ca.py` (they do not exist at base — `git cat-file -e 98c486b:reports/round-76/accept-ca.py` fails;
  the round's counters are built later in the round, so no counter-side leg could be exercised here); no network fetch was needed for
  this row.
- I did not re-derive the round-73 SCORECARD/receipt pair beyond its two tokens (both printed in `recurrence.txt`), and I did not
  re-run the round-75 counters; the row's evidence is committed bytes plus the staged-copy `wc -c`.

## 9. Artifacts

`.ufo/waves/round-76/w1/stage/RevengerMistakes/` — `check-filed-numbers.sh` (`d8c9be12ad20…`), `lesson-base.md` (`3271c3f76bdd…`,
equal to the `98c486b` blob), `lesson-repaired.md` (`42c9f7401b0d…`), `fixture-diff.txt`, `red-filed-numbers.txt`,
`green-filed-numbers.txt`, `recurrence.txt`, `SHA256SUMS.txt`. Scratch root deleted on exit; no `/tmp` path is cited anywhere.
