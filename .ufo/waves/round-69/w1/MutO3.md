# MutO3 — mutation-test of the R68FROZEN leg (round-69 w1, hyaku run 6)

Seat: MutO3 (leaf, no subagents) · Milestone: r69-v1 · Date: 2026-10-24
Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin (base rev 793f79746712a79f915bb481215e54bbea8b5e7a)
Axes: **operability** (does the R68FROZEN leg actually detect a wrong-receipt mutation?) · **calibration** (are the recorded round-68 counter digests independently re-derivable?).

Target under test: `reports/round-69/accept-o.py`, leg `R68FROZEN` (lines 158–168): re-derives each round-68 counter's live sha256 and compares it against the `# counter sha256 (self):` line in that counter's own receipt (`R68_COUNTERS` at lines 52–56). All mutation work was done on a COPY under /tmp (`/tmp/muto3-w1/`); production bytes untouched; no git/jj mutations; no network fetches.

## 1. Independent verification — live vs recorded sha256 (all three counters)

Commands (independent of the counter's own Python regex logic — `sha256sum` + `grep` only):

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
$ sha256sum reports/round-68/accept-o.py reports/round-68/accept-ca.py reports/round-68/accept-c.py
f409096c9167989fb56ec2830e846c282201d37e5d6a6a1752e1697418a07fae  reports/round-68/accept-o.py
a6d1c1c24e779817a3344b063054d3c10bc09fcf466b578f38ba8008c6fc9925  reports/round-68/accept-ca.py
515fa492aac176b62dc776c16777d6f9cf1750bb31b802cdecaa4121ac7bbf7d  reports/round-68/accept-c.py

$ grep -H '^# counter sha256 (self):' reports/round-68/telemetry/final-measures-o.txt reports/round-68/telemetry/final-measures-ca.txt reports/round-68/telemetry/final-measures-c.txt
reports/round-68/telemetry/final-measures-o.txt:# counter sha256 (self): f409096c9167989fb56ec2830e846c282201d37e5d6a6a1752e1697418a07fae
reports/round-68/telemetry/final-measures-ca.txt:# counter sha256 (self): a6d1c1c24e779817a3344b063054d3c10bc09fcf466b578f38ba8008c6fc9925
reports/round-68/telemetry/final-measures-c.txt:# counter sha256 (self): 515fa492aac176b62dc776c16777d6f9cf1750bb31b802cdecaa4121ac7bbf7d
```

Shell re-derivation of the leg's comparison, pair by pair (each receipt has exactly one sha line):

```
$ for pair in "accept-o.py final-measures-o.txt" "accept-ca.py final-measures-ca.txt" "accept-c.py final-measures-c.txt"; do ...
MATCH count=1 counter=accept-o.py receipt=final-measures-o.txt live=f409096c9167 recorded=f409096c9167
MATCH count=1 counter=accept-ca.py receipt=final-measures-ca.txt live=a6d1c1c24e77 recorded=a6d1c1c24e77
MATCH count=1 counter=accept-c.py receipt=final-measures-c.txt live=515fa492aac1 recorded=515fa492aac1
--- distinct recorded digests:
3
```

The three recorded digests are pairwise distinct (sort -u → 3), so pointing any pair at a *wrong* receipt must produce a mismatch — the leg has a real job to do.

**VERDICT: PASS** — sha256 of reports/round-68/accept-o.py == recorded digest in reports/round-68/telemetry/final-measures-o.txt; same for accept-ca.py (final-measures-ca.txt) and accept-c.py (final-measures-c.txt). All three MATCH, independently of the counter's own code.

## 2. Baseline — unmutated copy

```
$ mkdir -p /tmp/muto3-w1 && cp .../reports/round-69/accept-o.py /tmp/muto3-w1/accept-o.py
$ sha256sum /tmp/muto3-w1/accept-o.py .../reports/round-69/accept-o.py
8724f9a08911661c099092606b7f058ba94a2ea7af00a7a26309d954e49ba121  /tmp/muto3-w1/accept-o.py
8724f9a08911661c099092606b7f058ba94a2ea7af00a7a26309d954e49ba121  .../reports/round-69/accept-o.py

$ cd /tmp/muto3-w1 && python3 -B accept-o.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin
LEG PASS STAMP self=8724f9a08911 committed=8724f9a08911
LEG PASS TOOL tools/check-settlement-fixture.py
LEG PASS FIXTURE rc=0 True
LEG PASS NEGCASE PASS fixture-negative rc=0 pending=0 missing_paths=1
LEG PASS LANE rc=0 True
LEG PASS NEGPROBE missing_paths=1 present=True
LEG PASS R68FROZEN mismatched=none
ACCEPT-O-69: PASS legs=7/7
exit=0
```

Baseline 7/7 including R68FROZEN PASS — the flip below is attributable to the mutation alone.

## 3. Mutation — point the accept-o.py pair at the WRONG receipt

Mutation applied to the COPY only (`/tmp/muto3-w1/accept-o.py`, mutated digest `1cdc2b1080d3…`): `R68_COUNTERS` first pair changed from `("accept-o.py", "final-measures-o.txt")` to `("accept-o.py", "final-measures-ca.txt")`. The other two pairs left correct, so a precise leg should name exactly one mismatch.

```
$ cd /tmp/muto3-w1 && sha256sum accept-o.py
1cdc2b1080d30d4b7b911ae457719e98efeb2c06d0440e3fd717445cc4aa8e48  accept-o.py
$ python3 -B accept-o.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin
LEG FAIL STAMP self=1cdc2b1080d3 committed=8724f9a08911
LEG PASS TOOL tools/check-settlement-fixture.py
LEG PASS FIXTURE rc=0 True
LEG PASS NEGCASE PASS fixture-negative rc=0 pending=0 missing_paths=1
LEG PASS LANE rc=0 True
LEG PASS NEGPROBE missing_paths=1 present=True
LEG FAIL R68FROZEN mismatched=['accept-o.py live=f409096c9167 recorded=a6d1c1c24e77']
ACCEPT-O-69: FAIL legs=5/7
exit=1
```

**VERDICT: PASS (mutation killed)** — the R68FROZEN leg flips PASS→FAIL and names exactly the mutated pair: `accept-o.py live=f409096c9167` (its true digest) vs `recorded=a6d1c1c24e77` (accept-ca.py's digest, read from the wrong receipt final-measures-ca.txt). The two unmutated pairs are correctly absent from `mismatched=`, and the counter exits 1.

Notes (expected behavior, not defects):
- STAMP also fires on the mutated copy (`self=1cdc2b1080d3 committed=8724f9a08911`): any byte-level edit of the counter is caught independently. Defense in depth holds.
- The kill is attributable to R68FROZEN's own logic, since the baseline run of the byte-identical copy passes 7/7 (STAMP PASS at the same location /tmp).

## 4. Observation filed for the integrating L1 (out of my write scope)

`reports/round-68/telemetry/final-measures-ca.txt` records the counter sha and per-leg lines only through `D1 PASS`, then contains a Python traceback (`NameError: name 'git_bytes' is not defined`, at `/tmp/r68/clone-aca/reports/round-68/accept-ca.py` lines 224/377/386) and **no final `ACCEPT-CA-68` summary line**. This is a filed round-68 historical artifact; the R68FROZEN leg only reads the sha line (present, count=1), so it is unaffected. Recorded here as an observed fact for Ca2/lane integration — I did not evaluate whether round-68 annotated this crashed run, and I edited nothing.

**VERDICT: NOT-EVALUATED** — whether the round-68 records annotate the crashed accept-ca.py final-measures run; needs the Ca2 lane / L1.

## Verdict summary

- VERDICT: PASS — independent sha256 verification of all three round-68 counters against their receipts (f409096c…/a6d1c1c2…/515fa492… each MATCH, one sha line per receipt, 3 distinct digests).
- VERDICT: PASS (mutation killed) — pointing accept-o.py's R68FROZEN comparison at final-measures-ca.txt flips the leg to FAIL with the exact pair named, counter exits 1; baseline copy passes 7/7.
- VERDICT: NOT-EVALUATED — annotation status of the accept-ca.py crashed-run receipt (finding for L1, see §4).
