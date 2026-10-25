# ExecReceiptRerun73 — PASS-at-lands receipts for the round-73 counters

Seat `ExecReceiptRerun73` (leaf; no delegation, no background job, no `task` spawn, no labrat), kotodama
round 74 / hyaku run 7, 2026-10-25. Item: round-73 closure routed defect 2 (PASS-at-lands receipts for
`accept-c.py` and `accept-ca.py`).

Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin` was read-only for me: no git write, no index
change, no worktree byte touched. Writes, both inside my assigned report/receipt paths:

- `.ufo/waves/round-74/w1/receipts/measures-c73-at-lands.txt` (6437 B, sha256 `34a95d34494025accfe2b0705dbdfd01ed8a45a275a9655f043f845b7fd00eca`)
- `.ufo/waves/round-74/w1/receipts/measures-ca73-at-lands.txt` (11912 B, sha256 `54ec0c2582de72b56199ad5f3bde972c9f533fd992f3cc7f2370390abdaff4e9`)
- this report.

No tool installed or upgraded; pacman not run. Claims (`reports/round-74/claims.json`) read first and
never edited.

## Headline

| counter | assignment's exact command | verdict | red leg |
|---|---|---|---|
| `reports/round-73/accept-c.py` | `--root . --lands 2d1cd91…` | **FAIL legs=10/11, exit 1** | **CENSUS** only |
| `reports/round-73/accept-ca.py` | `--root . --lands 2d1cd91… --fleet-root /home/vgpnk/Projects/shokunin` | **FAIL legs=8/9, exit 1** | **STAMP** only |

Neither exact command prints PASS at the round-73 lands `2d1cd9140d3a6c42296d71e4f29587582a4a88c0`.
Both reach PASS with one extra flag each, and the reason is different in each case:

- **C**: `leg_census` resolves the census script as `<fleet_root>/scripts/sources-census.sh` with
  `fleet_root` defaulting to `dirname(--root)`; inside a clone that parent holds no `scripts/`
  (the lands tree has no `scripts/` directory at all). `--fleet-root /home/vgpnk/Projects/shokunin`
  → `ACCEPT-C-73: PASS legs=11/11`, exit 0.
- **Ca**: `leg_stamp` requires `measured == lands`, and `measured` is `git rev-parse main` of the lane
  (accept-ca.py:896). Lane `main` is now `f7104cbce186bc2e1522abf0cfd619cc834628bb`, two commits past
  lands. `--main 2d1cd914…` → `ACCEPT-CA-73: PASS legs=9/9`, exit 0.

**It is not the fleet report.** The Ca `APPENDONLY` leg pins `.ufo/reports/round-72/kotodama.md` at
ledger `fleet_pin=80d8c9b5…`; that blob is byte-identical at the pin and at fleet HEAD
(`ea256ae7f9d758e0962a7fdfeea446d8963e3f7ef1314aeacc6a7334509834be`, checked today), and the leg is
green. The round-73 fleet report `.ufo/reports/round-73/kotodama.md` (fleet commit `dad39efd`,
20:43:14) is read by no round-73 Ca leg.

## 1. Environment and clone identity

```
D=/tmp/ExecReceiptRerun73/r73lands.NDA2p2tQ
git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"          exit 0
git -C "$D/lane" checkout -q --detach 2d1cd9140d3a6c42296d71e4f29587582a4a88c0   exit 0
git -C "$D/lane" rev-parse --show-toplevel   -> /tmp/ExecReceiptRerun73/r73lands.NDA2p2tQ/lane
git -C "$D/lane" rev-parse HEAD              -> 2d1cd9140d3a6c42296d71e4f29587582a4a88c0
git -C "$D/lane" rev-parse 'HEAD^{tree}'     -> 516ea6c7d9265ae58ebc21fded41f925ddc504b2
git -C "$D/lane" rev-parse '2d1cd91^{tree}'  -> 516ea6c7d9265ae58ebc21fded41f925ddc504b2
git -C "$D/lane" status --porcelain | wc -l  -> 0
git -C "$D/lane" rev-parse main              -> f7104cbce186bc2e1522abf0cfd619cc834628bb
python3 --version -> Python 3.14.8 ; git --version -> git 2.56.0
```

`$D` itself is not a repository (the clone is `$D/lane`); no commit was ever made, so the
"toplevel equals $D" fixture rule never applies here. The only `--detach` was on this throwaway clone,
as the item allows.

Counter bytes at lands (equal to the graded round-73 blobs):

```
95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416  reports/round-73/accept-c.py
222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89  reports/round-73/accept-ca.py
c912401dd511d712567d8a704a690bf02fa4a8253a628b8e67ab9473798356b9  reports/round-73/ledger.json
```

Each run re-printed its own `# counter sha256 (self):` line identical to these digests, and
`# tree: 516ea6c7d9265ae58ebc21fded41f925ddc504b2` in every run. No counter byte was altered.

Environment note: `/tmp` (128 G) reached **100 % full** during the seat (my second, optional clone
died with `No space left on device`; I removed my own partial clone). All runs reported here completed
before the fill; a later re-run may fail on ENOSPC inside the counters' own `/tmp` materializations.

## 2. Claim C — `accept-c.py`, exact command

Full stdout, exit code 1 (`receipts/measures-c73-at-lands.txt` RUN 1):

```
# round-73 acceptance counter — claim C (conlang-scholarship assimilation)
# counter sha256 (self): 95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416
# stamped revision: 2d1cd9140d3a6c42296d71e4f29587582a4a88c0
# evaluated revision: 2d1cd9140d3a6c42296d71e4f29587582a4a88c0
# measured revision (lane main): 2d1cd9140d3a6c42296d71e4f29587582a4a88c0
# tree: 516ea6c7d9265ae58ebc21fded41f925ddc504b2
# base revision: 8841ad3b896a0227674fa0725b818c999118046f
...
LEG PASS ENTRIES
LEG PASS ROWS
LEG PASS REPOINTED
LEG PASS GATE
LEG PASS EVIDENCE
LEG PASS REJECTS
LEG PASS GROUND
LEG PASS CITEDLINES
LEG FAIL CENSUS
     census script not found: /tmp/ExecReceiptRerun73/r73lands.NDA2p2tQ/scripts/sources-census.sh
LEG PASS SCRATCHMIRROR
LEG PASS COLLCHECK
ACCEPT-C-73: FAIL legs=10/11
```

stderr: 0 bytes. Ten of eleven legs are green at the closure lands; only CENSUS is red, and its detail
names the environment, not a graded byte.

**Cause, exactly.** `accept-c.py:926-928`:

```
script = census_sh or os.environ.get("KOTODAMA_CENSUS_SH") or \
    os.path.join(fleet_root, "scripts/sources-census.sh")
```

and `main` sets `fleet_root = args.fleet_root or os.path.dirname(os.path.abspath(root))`. In a clone at
`$D/lane` that parent is `$D`, which has no `scripts/`. The census script is a **fleet** artifact: it is
not in the lands tree (`git ls-tree 2d1cd914… | grep -x scripts` → nothing) and not in the lane
worktree. The round-73 claim's own `after`/`counter` sentence spells the command without any fleet flag:

```
`python3 -B reports/round-73/accept-c.py --root . --lands <lands>` prints ACCEPT-C-73: PASS legs=11/11
```

so the frozen sentence is reproducible only with the undocumented flag — the same finding wave-2
`ExecRerunC.md` §1/M5 recorded at `0316b88`. `SKILL.md:703` at lands repeats the flagless form and
already records the shortfall in its own words: "measured 10/11 and 1/11".

**Supplementary run (not the assignment command)** — `--fleet-root /home/vgpnk/Projects/shokunin`:

```
LEG PASS CENSUS
     exit=0 last-line=kotodama	ok	/tmp/r73-fleet-zy1r_6gb/kotodama-shokunin/corpus/SOURCES.md
...
ACCEPT-C-73: PASS legs=11/11     (exit 0)
```

The census script it executes is the fleet worktree copy
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`,
sha256 `3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30`, clean in its worktree,
last committed at fleet `f47ad6ba8d306f8125597401cb2ce45c1297a593` (2026-10-25 09:29) — unchanged
since wave-2 measured it. The receipt does not name that revision (unchanged observation from
`ExecRerunC.md` M5); I record it here.

## 3. Claim Ca — `accept-ca.py`, exact command

Full stdout, exit code 1 (`receipts/measures-ca73-at-lands.txt` RUN 1):

```
# counter sha256 (self): 222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89
# stamped revision: 2d1cd9140d3a6c42296d71e4f29587582a4a88c0
# evaluated revision: 2d1cd9140d3a6c42296d71e4f29587582a4a88c0
# measured revision (lane main): f7104cbce186bc2e1522abf0cfd619cc834628bb
# tree: 516ea6c7d9265ae58ebc21fded41f925ddc504b2
...
LEG PASS LEDGER            pairs=8 min=8
LEG PASS BASEMISMATCH      found=8 min=8
LEG PASS REPAIR            green=['L04', 'L05', 'L08'] red=[]
LEG PASS ANNOTATE          rows=9 annotate-pairs=5 unannotated=0 []
LEG PASS NOSTUB            stubs=[]
LEG PASS APPENDONLY        lane-removed=0 fleet-pin=80d8c9b576d4 blob=ea256ae7f9d7 in-place=['SKILL.md(registry)', 'corpus/README.md(footer)']
LEG PASS SEPARABLE         problems=[]
LEG PASS TRACKED           paths=2 problems=[]
LEG FAIL STAMP
     stamped=evaluated=measured=2d1cd9140d3a tree=516ea6c7d926 counter=222d4dd6d408 clone=/tmp/r73-ca-4yuf9xt1/lands problems=['measured f7104cbce186bc2e1522abf0cfd619cc834628bb != lands 2d1cd9140d3a6c42296d71e4f29587582a4a88c0']
ACCEPT-CA-73: FAIL legs=8/9
```

stderr: 0 bytes. Eight of nine legs green; STAMP is red on **one** comparison.

**Cause, exactly.** `main_check` computes

```
measured = git(root, "rev-parse", "--verify", "--quiet", "%s^{commit}" % main_branch)   # main_branch="main"
```

and `leg_stamp` appends a problem whenever `header["measured"] != lands`. Lane `main` left lands twice
after the landing:

```
2d1cd914  round-73: SKILL rows (ExecSkillRows), four-space guard control, S879 durability correction note   20:36:09
c1b5b476  round-73: LOG entry, SCORECARD axes section                                                       20:36:38
f7104cbc  round-73 verifier spot-check (integrator, hyaku): non-author admit/reject                         20:47:05
```

`measured` is consumed nowhere except `leg_stamp` (`grep -n measured reports/round-73/accept-ca.py`
hits line 842 only, inside `leg_stamp`). That is why the single change of the measured ref flips
exactly one leg:

**Supplementary run (not the assignment command)** — `--main 2d1cd9140d3a6c42296d71e4f29587582a4a88c0`:

```
LEG PASS STAMP
     stamped=evaluated=measured=2d1cd9140d3a tree=516ea6c7d926 counter=222d4dd6d408 clone=/tmp/r73-ca-a8hrnxyx/lands
ACCEPT-CA-73: PASS legs=9/9     (exit 0)
```

Every other leg line is byte-identical to RUN 1 modulo the temp clone path (`diff` of the two runs is
only that line plus the `# measured`/`# clone` headers), which isolates STAMP as the sole difference.

The SKILL gate row at lands already carries `--fleet-root` for this counter (`SKILL.md:704`) but no
measured-ref flag, so the lane's own documented invocation is the one that now fails STAMP.

A third variant — forcing the clone's `main` to lands so that the plain command sees
`measured == lands` — **was not run**: the clone died with `No space left on device` while `/tmp` was
full, and I deleted my partial copy. It is logically equivalent to `--main <lands>` for `leg_stamp`
(which only compares the resolved hash), so the PASS above already establishes the outcome; the
variant is listed as unrun, not as verified.

## 4. Determinism

Each exact command was run twice in the same clone. Diffs (recorded verbatim in the receipts):

- C: one line — `# materialized: … /tmp/r73-lands-uprstgcv/lands` vs `/tmp/r73-lands-frjlbphy/lands`.
- Ca: three lines — the `# clone:`/`# base-clone:` temp paths and the STAMP detail's clone path.

No leg verdict, counter hash, tree hash or revision line moved. The exact command exited 1 in both
passes of each counter; each supplementary run was executed once (exit 0) — repeat-pass determinism is
claimed for the exact commands only.

## 5. Header grammar (`tools/check-receipt-seq.py`, lane copy at `f7104cb`, read-only)

| run | SEQ (stamped=evaluated=measured) | TREE | counter SHA | verdict |
|---|---|---|---|---|
| C exact | PASS `stamped=2d1cd914 evaluated=2d1cd914 measured=2d1cd914 equal=True` | PASS `recorded=516ea6c7 actual=516ea6c7` | PASS `recorded=95aee881 actual=95aee881` | `RECEIPT-SEQ: PASS` (0) |
| C +fleet-root | PASS (same) | PASS | PASS | `RECEIPT-SEQ: PASS` (0) |
| Ca exact | **FAIL** `stamped=2d1cd914 evaluated=2d1cd914 measured=f7104cbc equal=False` | PASS | PASS `222d4dd6` | `RECEIPT-SEQ: FAIL` (1) |
| Ca +main-pin | PASS (same) | PASS | PASS | `RECEIPT-SEQ: PASS` (0) |

The C counter's `# measured revision (lane main)` line is `git rev-parse HEAD` of `--root`, not the
`main` ref (`accept-c.py:1139-1140`); in a detached clone at lands it therefore reads `2d1cd914`, while
the lane's real `main` is `f7104cb`. That line is disclosure-only — no C leg reads it — but a receipt
cited as "measured == lands" must say that it is the clone's HEAD.

**Post-report / topo requirement.** `check-receipt-seq.py --topo` accepts a receipt only when the
commit that carries it (`git log -1 main -- <receipt>`) has parent == stamped revision. Any receipt of
these round-73 lands committed in round 74 is carried by a commit whose parent is `f7104cb` (round-74
base), never `2d1cd914`, so **TOPO cannot be claimed for these receipts** and they must be labelled as
post-report re-runs (header grammar satisfied, carrier parentage not). Rewriting history to make a
`2d1cd914`-parent carrier is out of bounds for every seat.

## 6. Why the fleet report is not the cause (probed, not assumed)

```
git -C /home/vgpnk/Projects/shokunin show 80d8c9b576d45d3c390e1e8edc6c149cfb698483:.ufo/reports/round-72/kotodama.md | sha256sum
  -> ea256ae7f9d758e0962a7fdfeea446d8963e3f7ef1314aeacc6a7334509834be
git -C /home/vgpnk/Projects/shokunin show HEAD:.ufo/reports/round-72/kotodama.md | sha256sum
  -> ea256ae7f9d758e0962a7fdfeea446d8963e3f7ef1314aeacc6a7334509834be
```

identical at the ledger's `fleet_pin` and at fleet HEAD (fleet HEAD `ebccb441…`, 21:34). The Ca
`APPENDONLY` leg's fleet half is green in both runs, with `fleet-pin=80d8c9b576d4 blob=ea256ae7f9d7`.
`.ufo/reports/round-73/kotodama.md` exists in the fleet git (commit `dad39efd`, 2026-10-25 20:43:14)
but no round-73 Ca leg path names it. So the Ca red is **lane vintage** (`main` advanced), not a fleet
mutation.

## 7. Labelling decision (what may be cited, and as what)

Handed to the L1 verbatim:

1. **`ACCEPT-C-73`**: the exact command is `FAIL legs=10/11`, red leg CENSUS, `census script not found:
   <clone-parent>/scripts/sources-census.sh`. Cause: fleet-root default, an environment leg, not a
   graded byte. Only a run that names `--fleet-root /home/vgpnk/Projects/shokunin` (or
   `KOTODAMA_CENSUS_SH`) prints `PASS legs=11/11`. A committed PASS-at-lands receipt for this counter
   is therefore **honest but must quote the flag**; the flagless form must never be presented as PASS.
2. **`ACCEPT-CA-73`**: the exact command is `FAIL legs=8/9`, red leg STAMP only, because
   `measured` = lane `main` = `f7104cb…` ≠ lands `2d1cd914…`. Only a run naming
   `--main 2d1cd914…` prints `PASS legs=9/9`, and in that run the header line
   `# measured revision (lane main)` names the pinned lands hash, not today's branch. A committed
   PASS-at-lands receipt for this counter is **honest only with that pin disclosed**; without the pin
   the receipt must be labelled `FAIL 8/9 (STAMP: lane main advanced)`.
3. Neither run alters a counter byte (`222d4dd6…`, `95aee881…` in every run).
4. Neither receipt can carry a `--topo` PASS (§5).

## 8. Consequence for the round-74 claim Ca draft (not edited — reported)

The draft's `RECEIPTS` leg demands "a PASS-at-lands receipt for ACCEPT-C-73 and for ACCEPT-CA-73, each
produced inside a clone materialized at round 73's lands …, whose header stamped==evaluated==measured==
that revision", and `STAMP` repeats it. As the draft stands:

- **C is satisfiable** with `--fleet-root` in a detached clone at lands (header
  `stamped=evaluated=measured=2d1cd914`, `PASS 11/11`), provided the receipt quotes the flag; it is
  **not** satisfiable in the flagless form the round-73 claim and `SKILL.md:703` document.
- **Ca is satisfiable only with a measured pin** (`--main 2d1cd914…`): today's lane `main` is
  `f7104cb`. If the round-74 counter re-derives `measured` from the cloned repo's `main`, the clone must
  be created with `main` at lands (a clone-local `git checkout -B main <lands>`, allowed only inside the
  throwaway clone) or the leg must accept the pinned form — otherwise the leg is unsatisfiable for any
  historical lands and the claim fails for a structural reason.

My receipts file both forms side by side with the label, so the landing seat can cite either without
re-running.

## 9. Risks / open items

- **Committing is not mine.** `receipts/*.txt` are untracked in the lane worktree; the round-74 landing
  must commit them and should cite them by path + sha256 (values in the header of this report).
- **`/tmp` is 100 % full** (128 G, 12 M free at close). The counters materialize `git archive` trees and
  clone under `/tmp`; further re-runs can fail with ENOSPC (my optional third-clone experiment already
  did). Any seat re-running these commands must free space first; the counters report ENOSPC as a
  materialization error (exit 2), not as a leg verdict.
- `accept-c.py`'s `# measured revision (lane main)` is the clone HEAD, not `main`; a round-74 receipt
  leg that compares that line to a real `main` must know this (round-73 minor m6, still live).
- The census script's identity is unnamed by the C counter (sha `3fb72615…`, fleet commit `f47ad6ba`);
  unchanged today, but a PASS receipt for C inherits the fleet worktree's live script.

## 10. Retained evidence

- `/tmp/ExecReceiptRerun73/` — `c73.out`, `c73.err`, `c73_run2.out`, `c73_fleet.out`,
  `c73_fleet.err`, `ca73.out`, `ca73.err`, `ca73_run2.out`, `ca73_mainlands.out`,
  `ca73_mainlands.err`, `clone-path.txt`; clone `/tmp/ExecReceiptRerun73/r73lands.NDA2p2tQ/lane`
  (detached at `2d1cd914`, clean, `main`=`f7104cb`).
- Counter/tree/sha provenance as quoted in §1; determinism diffs in §4; seq verdicts in §5; fleet blob
  hashes in §6.
- Not run: the clone-local `main`-to-lands variant (ENOSPC, §3); any write to the lane repo, its git
  state or the fleet repo; any `--selftest` run (out of item); any network fetch (none needed).
