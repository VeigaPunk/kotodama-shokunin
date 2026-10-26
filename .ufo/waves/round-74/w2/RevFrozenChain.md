# Seat RevFrozenChain — ATTACK: the freeze chronology (round 74, wave 2, falsify)

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (read-only for me; my only write is this file
plus scratch under `.ufo/waves/round-74/RevFrozenChain-scratch/`, removed after use).
Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; operative freeze F3 `00c408a0af2fa5ddf65af2224152ce258b26d896`;
claim Ca lands `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`; claim C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`;
lane main at dispatch `1d7add3f7b9eaf6f3349c56c36f6d06325d74236`.

**Verdict in one paragraph.** The frozen bytes are honest where it matters most: `claims.json` and
`ledger.json` are byte-identical at `<freeze>` and at every land and at `main` (Q4 PASS), the freeze is a
first-parent ancestor of both lands, and both counters reproduce their PASS lines in my own clone
(`ACCEPT-C-74: PASS legs=13/13`, `ACCEPT-CA-74: PASS legs=11/11`). The claim does **not** survive three
attacks: the frozen Ca `do_nothing_control` clause demands `RECEIPTS red` while the committed control
receipt prints `LEG PASS RECEIPTS` (F2); the `RECEIPTS` leg itself is materialization-prefix dependent —
the same bytes fail when the counter's temp root is outside `/tmp` (F1, reproduced); and the guard
sentence "no seat has scored landed data" is false under the plain git sense of "landed" because the
re-freeze that rewrote two claim legs and two ledger entries followed a seat's scoring of the landed
first-freeze commit (F3). Q2 passes: every ledger change maps to an R74-M9 category. Two low-severity
record defects remain (F4 provenance sentence, F5 duplicated `axes_note`), plus one disclosed pinning
gap (F6).

## Method and environment

- Coordinates read from the **frozen commit** (`git show 00c408a0:...`), not the graded tree, and
  re-read at `de93d91c` and `3595c919` for the chronology.
- Counter runs happened **only inside throwaway clones** (assignment recipe): `mktemp -d` + `git init` +
  `git clone` + `git branch -f main <lands>` in the clone only. No write to the lane, the fleet root,
  `scripts/`, `templates/`, `.ufo/state`, or `shokuknow`.
- Environment note: at 2026-10-25 ~23:05 `/tmp` was **100% full** (`df -h /tmp` → `128G 128G 331M 100%`,
  later `24M` free), so the do-nothing control and the round-73 re-runs were made with
  `TMPDIR` under my home scratch. That is what exposed F1. The two PASS runs used the default `/tmp`
  before it filled.
- No network fetches, so no User-Agent record is owed; no tool installs, no pacman, no upgrades.

```
$ python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8d722… --freeze 00c408a0af2f… --fleet-root /home/vgpnk/Projects/shokunin
…
LEG PASS INDEX
ACCEPT-C-74: PASS legs=13/13
exit=0
```

```
$ python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0cb6a… --freeze 00c408a0af2f… --fleet-root /home/vgpnk/Projects/shokunin
…
LEG PASS STAMP
     stamped=evaluated=measured=5e4796c0cb6a tree=83257915923c counter=8052f1e25c36 clone=/tmp/r74-ca-q8vcvthc/lands
ACCEPT-CA-74: PASS legs=11/11
exit=0
```

## Answers to the four questions

### (1) Is `claims.json` byte-identical across the three freezes? Which changes were made, and when?

No.

```
$ for c in de93d91c 3595c919 00c408a0; do git rev-parse $c:reports/round-74/claims.json; done
dd75cd1964d0c897198b148e425bd7d466e0bfa1   # de93d91c
93ac4ff0a1b4b05985134b23e8425793a36b38ef   # 3595c919
93ac4ff0a1b4b05985134b23e8425793a36b38ef   # 00c408a0
```

So `de93d91c` → `3595c919` changed the claims blob; `3595c919` → `00c408a0` changed **nothing** in it.
The re-freeze-2 commit touched exactly three lines (`git diff --numstat de93d91c 3595c919 -- reports/round-74/claims.json`
→ `3 3`):

1. `claims.json:6` `axes_note` — a 5th verbatim copy of a 195-character sentence was **added**
   (count of `The freshness pause is a lane-filed L0 disposition … does not rest on the pause being ruled.`
   is 4 at `de93d91c`, 5 at `3595c919`/`00c408a0`; lengths 1132 → 1327). See F5.
2. `claims.json:207` `APPENDONLY` — added `…except the six must_track paths (inherited files pinned by TRACKED)`.
3. `claims.json:209` `SEPARABLE` — replaced `no byte in that set cites a lane S-id >= S881`
   with `no byte in that set cites S881, S882, S883 or S884 (the lane ids claim C adds)`.

**Were those changes made after a seat scored landed data?** Timeline (`git reflog show main`,
`git log --format='%h a=%ad c=%cd'`):

```
1d7add3 main@{2026-10-25 22:59:06}: export from jj
c4bf61a main@{2026-10-25 22:50:09}: export from jj
d7a3840 main@{2026-10-25 22:49:29}: export from jj
5e4796c main@{2026-10-25 22:48:30}: export from jj   # claim Ca lands
00c408a main@{2026-10-25 22:46:35}: export from jj   # operative freeze
3595c91 main@{2026-10-25 22:37:37}: export from jj   # re-freeze (claims/ledger changed here)
de93d91 main@{2026-10-25 22:28:25}: export from jj   # first freeze (author date 20:47:05; committer 22:28:24)
```

- **No claim data existed before the operative freeze.** `git log --first-parent` over
  `f7104cb..main` lists only the three freezes before the first landing; the first landing (`5e4796c`,
  Ca) has `00c408a` as parent and an author time **one second after** the freeze
  (`5e4796c^ = 00c408a0…`). So no seat could have scored claim-C/Ca data when any rule changed.
- **But the first freeze commit itself was on main and was scored.** `de93d91` exported at 22:28:25;
  `ExecCaCounter` ran the counter there and its report (added in the same 22:37:37 commit that changed the
  legs) says: `The real run at the committed freeze de93d91cab5a4f19fbe20b948abca67b8e9c7650` and
  `re-freezing needs this blob`; `reports/round-74/telemetry/controls-ca.txt` as committed at `3595c919`
  stamps `measured revision (lane main): de93d91cab5a…`. So the sequence is
  **de93 on main → seat scores it and reports three mismatches → legs/ledger changed at 22:37:37 → seat
  re-verifies → freeze 3**. Whether this violates the guard depends on the meaning of "landed data"
  (see F3); the claim does not define the term.
- Wave-1 report mtimes vs commit times: 42 of the 44 wave-1 reports span 21:14:37–22:26:29 (before the
  first freeze was exported at 22:28:25); only `ExecCaCounter.md` (22:44:59) and `ExecJunkFixtures.md`
  (22:58:04) postdate it, and the only wave-1 report citing a land hash is `ExecJunkFixtures.md`
  (`c4bf61a8d722…`), a line added by the post-freeze commit `1d7add3` (`git log -S'c4bf61a8d722'` →
  `1d7add3`).

### (2) Did the ledger change between freezes, and does every change appear in R74-M9?

Yes, at re-freeze 2 only (`git rev-parse 3595c919:reports/round-74/ledger.json` ==
`00c408a0:…` = `91919e926cc8…`); numstat `42 33` (75 lines).

```
$ git diff de93d91c 3595c919 -- reports/round-74/ledger.json
-LC-01 "disposition": "REPAIR"  → "ANNOTATE"   (statement_after removed)
-LC-09 argv "f7104cbce186…" → "HEAD"           (rederive updated; truth stays 95)
-13 × "observed_at_base": "<token> (prose…)" → "observed_at_base": "<token>" + "observed_note": "(prose…)"
```

Every hunk maps to a named R74-M9 category (`corpus/lessons/round-74.md:176`):
"ledger tokens normalized, LC-01 moved to ANNOTATE and LC-09 de-pinned (its truth does not move with
claim C), claims text amended for the must_track exemption and the lane-id set, the counter redacts the
literals…". The 13 prose moves are the "ledger tokens normalized" / BASEMISMATCH-prose fix; the LC-01
`statement_after` removal is implied by "moved to ANNOTATE". **No ledger change is undisclosed.**
The 5th `axes_note` copy is the only *claims* change not named by that list (F5).

### (3) Is "no seat scored landed data" true for each freeze?

True under the claim's own vocabulary (delivered data at `<lands>`), false under the ordinary repo sense
(any commit exported to `main`):

- de93d91c (first freeze): no landing existed yet — true trivially.
- 3595c919 (re-freeze): `de93d91c` had been on `main` for 9 minutes and a seat had scored it
  (`ExecCaCounter`, plus the counter's own `measured revision (lane main): de93d91c` receipt) — false
  under the broad reading.
- 00c408a0 (operative freeze): same, and the re-freeze-2 edits were fitted to that run — false under the
  broad reading. Under the narrow reading ("claim data landed"), all three are true because the first
  landing is at 22:46:35, after 00c408a0.

The lesson line (`corpus/lessons/round-74.md:9`) and R74-M9 both state the unqualified sentence, so a
reader cannot tell which sense is meant. See F3.

### (4) Which later commits touched the frozen files?

None.

```
$ git log 00c408a0af2fa5ddf65af2224152ce258b26d896..main -- reports/round-74/claims.json reports/round-74/ledger.json
[end]
$ git diff --stat 00c408a0af2fa5ddf65af2224152ce258b26d896 main -- reports/round-74/claims.json reports/round-74/ledger.json
[end]
$ for c in 5e4796c0cb6a… c4bf61a8d722… d7a3840 1d7add3 main; do git rev-parse $c:reports/round-74/claims.json $c:reports/round-74/ledger.json; done
93ac4ff0a1b4b05985134b23e8425793a36b38ef / 91919e926cc84113cc98b24902de9a049223e43b   (all five)
```

**This limb of the attack FAILED: the frozen files are immutable after 00c408a0 and identical at both
lands and main.**

## Findings

### F1 — HIGH — the `RECEIPTS` leg is materialization-prefix dependent; the graded PASS flips to FAIL outside `/tmp`

`reports/round-74/accept-ca.py:183` normalizes only paths that *contain* `/tmp` or `/var/tmp`:

```
RECEIPT_TMP_RE = re.compile(r"/(?:var/)?tmp/[^\s:,\"']+")
# :1721 def normalize_receipt(text): return RECEIPT_TMP_RE.sub("<TMP>", text or "")
…
if normalize_receipt(body) != normalize_receipt(rerun[key]):   # :1824
    problems.append("%s: committed stdout differs from the re-run …")
```

The committed receipts were produced with `/tmp` clones, so their `materialized:`/`clone:` lines read
`… at /tmp/r73-…` → `<TMP>`. When the counter's own clone lives under any other root, only the `/tmp/...`
tail is replaced and the parent directory survives, so the byte comparison fails although nothing about
the round-73 receipts changed. Reproduced with the assignment's own control (do-nothing at the operative
freeze, only `TMPDIR` changed):

```
$ cd <clone> && git branch -f main 00c408a0af2fa5ddf65af2224152ce258b26d896
$ TMPDIR=<home>/…/RevFrozenChain-scratch/tmp python3 -B reports/round-74/accept-ca.py \
    --root . --lands 00c408a0af2f… --freeze 00c408a0af2f… --fleet-root /home/vgpnk/Projects/shokunin
…
LEG FAIL RECEIPTS
     rev=2d1cd9140d3a receipts=['accept-c-73=50c60bb67f16', 'accept-ca-73=864c94192854'] problems=['reports/round-74/telemetry/accept-c-73-at-lands.txt: committed stdout differs from the re-run (bda16ca6deec vs 75c3423f2f0d)', 'reports/round-74/telemetry/accept-ca-73-at-lands.txt: committed stdout differs from the re-run (55544779204d vs c29b1990cfc0)']
ACCEPT-CA-74: FAIL legs=6/11
exit=1
```

The normalized diff of the two committed receipts against a re-run of the same round-73 counters at
`2d1cd914` is exactly the surviving prefix (nothing else differs):

```
--- committed
+++ rerun
-# materialized: git archive of the stamped revision at <TMP>
+# materialized: git archive of the stamped revision at /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-74/RevFrozenChain-scratch<TMP>
-     exit=0 last-line=kotodama	ok	<TMP>
+     exit=0 last-line=kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-74/RevFrozenChain-scratch<TMP>
-# clone: <TMP> head=2d1cd9140d3a…
+# clone: /home/…/RevFrozenChain-scratch<TMP> head=2d1cd9140d3a…
```

Blast radius: the claim's after-state ("prints `ACCEPT-CA-74: PASS legs=11/11`") is reproducible only
when the grader's clone root is literally under `/tmp` — and on this host `/tmp` is currently 100% full
(`df -h /tmp` → `331M`/`24M` free), so the assignment's own `mktemp -d` recipe cannot materialize the
clone at all. A legitimate grader with `TMPDIR` on another filesystem gets a false FAIL.

**Proposed fix.** Normalize the *whole* materialization root passed in by the counter (e.g. replace
`re.escape(os.path.dirname(freeze_tmp)) + r"/[^\s:,\"']+"` and every recorded clone root), or compare on
lines with the `materialized:`/`clone:`/`base-clone:` fields stripped, and pin `TMPDIR` in the counter's
run environment while recording it in the receipt header. Re-generate both round-73-at-lands receipts and
the controls, then re-run the counter from a non-`/tmp` root to prove the leg is path-independent.

### F2 — HIGH — the frozen Ca `do_nothing_control` clause requires `RECEIPTS red`; its committed receipt prints `LEG PASS RECEIPTS`

`reports/round-74/claims.json:216` (byte-identical at all three freezes):

> `(1) lands == <freeze> FAILS with REPAIR, ANNOTATE, RECEIPTS red and FROZENCFG/LEDGER green`

`reports/round-74/telemetry/controls-ca.txt` at the operative freeze (`HEAD`, committed by `5e4796c`,
stamped `00c408a0af2f`, counter `8052f1e25c36`):

```
33:LEG FAIL REPAIR
35:LEG FAIL ANNOTATE
45:LEG PASS RECEIPTS
46:     rev=2d1cd9140d3a receipts=['accept-c-73=50c60bb67f16', 'accept-ca-73=864c94192854'] problems=[]
47:     NOTE lands == freeze: do-nothing control shape; the strict-ancestor requirement is not applied to this run and a PASS is refused
52:ACCEPT-CA-74: FAIL legs=7/11
```

And the same at the earlier `3595c919` receipt (measured at `de93d91c`, counter `dd755893`):
`45:LEG PASS RECEIPTS … 52:ACCEPT-CA-74: FAIL legs=5/11`. The clause matches the counter's *synthetic*
selftest (`selftest-ca.txt:2` `selftest: do-nothing -> … RECEIPTS=FAIL …`) but not the real freeze, where
the two round-73 receipts re-execute green. My own `/tmp` control run reproduces `LEG PASS RECEIPTS`; my
non-`/tmp` run reproduces `LEG FAIL RECEIPTS` (F1). So the declared red set is environment-dependent and
the committed evidence contradicts the frozen sentence.

**Proposed fix.** At the next disclosed freeze, either (a) amend the clause to "`RECEIPTS green when the
committed round-73 receipts match the re-run verbatim; red when the materialization root differs from the
one the receipts were produced under`", or (b) make `leg_receipts` deterministically red at
`lands == freeze` (as it already declares "a PASS is refused") and commit a receipt that shows
`LEG FAIL RECEIPTS`. Do not leave a frozen control clause that its own committed receipt falsifies.

### F3 — MEDIUM — the "no seat has scored landed data" guard is unqualified and false under the plain git sense

The frozen guard (`claims.json:3`): "frozen by the commit that adds this file …; no seat has scored landed
data. A rule changed after any seat scores landed data is not the claim's rule." R74-M9
(`corpus/lessons/round-74.md:176`) asserts "No seat had scored landed data at any of the three freezes."

Evidence that a seat scored the *landed* first freeze before the rules changed:

```
$ git reflog show main --date=iso | head -4
de93d91 main@{2026-10-25 22:28:25}: export from jj
3595c91 main@{2026-10-25 22:37:37}: export from jj
00c408a main@{2026-10-25 22:46:35}: export from jj
5e4796c main@{2026-10-25 22:48:30}: export from jj
```

```
$ git show 3595c919:reports/round-74/telemetry/controls-ca.txt | head -8
# controls-ca.txt — claim Ca do-nothing controls (round 74), measured at freeze de93d91cab5a… by the freeze-installed counter
…
# counter sha256 (self): dd755893f72cb8ec…
# measured revision (lane main): de93d91cab5a4f19fbe20b948abca67b8e9c7650
```

`.ufo/waves/round-74/w1/ExecCaCounter.md:333` (added by `3595c919`):
"The real run at the committed freeze `de93d91cab5a…` … exposed three mismatches; all three are fixed in
`.ufo/waves/round-74/counters/accept-ca.py` … (the freeze copy at `de93d91` is the previous bytes
`dd755893…`; re-freezing needs this blob)." The same commit rewrote `APPENDONLY`, `SEPARABLE`, `LC-01`
(REPAIR→ANNOTATE) and `LC-09` (de-pinned).

So: the rule changed after a seat scored a commit that was on `main`, at 22:37:37, 9 minutes after de93
landed. It did **not** change after any seat scored the claims' delivered data (none existed before
22:46:35). The frozen sentence cannot distinguish the two. The attack therefore succeeds on the wording,
not on the deliverable.

**Proposed fix.** Define "landed data" in the claim (e.g. "the claim's data at its `<lands>` commit — the
entries, rows, SKILL/SCORECARD/lesson edits — never the freeze/control commits") and add that definition
to R74-M9, stating that the re-freeze-2 edits were fitted to control runs at the landed freeze commit
`de93d91c`. Without that, a reader who takes `main` as "landed" can disqualify the operative claim by its
own guard.

### F4 — LOW — the frozen status sentence's provenance is false at the operative freeze

`claims.json:3` says the claim is "frozen by the commit that adds this file together with ledger.json,
id-renumber-map.json, both counters, the six inherited round-73 w2 files and the do-nothing and
junk-landing controls". At `00c408a0` the commit adds **none** of those (`git show --stat 00c408a0`:
`.ufo/waves/round-74/counters/accept-ca.py`, `w1/ExecCaCounter.md`, `reports/round-74/accept-ca.py`,
`reports/round-74/telemetry/selftest-ca.txt`). At `de93d91c` the commit adds `claims.json`, `ledger.json`,
the map, the counters, the six inherited files and `junk-fixtures.py`, but **no** do-nothing control
receipts (first committed at `3595c919`) and no `junk-c`/`junk-ca` receipts (committed at `1d7add3`). The
sentence describes no single commit.

**Proposed fix.** Replace it with: "first frozen by `de93d91c…`; operative freeze `00c408a0…` (claims and
ledger bytes carried unchanged from `3595c919…`)". The graded semantics (`--freeze 00c408a0`) are correct;
only the self-description is wrong.

### F5 — LOW — `axes_note` carries the same 195-character sentence four times at the first freeze and five at the operative freeze

```
$ git show de93d91c:reports/round-74/claims.json | grep -o "The freshness pause is a lane-filed L0 disposition" | wc -l   # 4
$ python3: axes_note length 1132 (de93) → 1327 (3595/00c408); occurrence count 4 → 5
```

The 5th copy was added by re-freeze 2 and is the only claims change R74-M9 does not name. No leg reads
`axes_note` (`grep -c axes_note reports/round-74/accept-c.py reports/round-74/accept-ca.py` → `0`,`0`), so
it is cosmetic, but it is a generator defect (`build-claims-final.py` appends the sentence unconditionally)
inside the authoritative frozen rule text.

**Proposed fix.** Dedupe the sentence in `build-claims-final.py` and re-emit; name the `axes_note` edit in
R74-M9 if it is repeated at the next freeze.

### F6 — LOW (disclosed) — `LC-09`'s de-pin removes the only revision literal from its `observe_cmd`

`ledger.json:353` now has `… "4b825dc6…", "HEAD", "--", "corpus/knowledge/civilizations/*.md"`, and the
SEPARABLE leg still says every observation is "the token the pair's observe_cmd returns in the clone at
the revision the ledger names". `LC-09` names no revision; only `expected_after: "95"` pins the number.
The counter evaluates `HEAD` in the base clone and in the lands clone (my runs print
`observed_base='95' observed_lands='95'`), so grading is deterministic *for the two clones the counter
makes*, but the ledger's own vocabulary is now vacuous for this pair. R74-M9 discloses the de-pin
("LC-09 de-pinned"), so this is a residual gap, not an undisclosed edit.

**Proposed fix.** State in the pair's `why` that `HEAD` is the clone revision (`<base>` in the base clone,
`<lands>` in the lands clone) and that grading is confined to those two clones, or pin the literal
`5e4796c0…` for the lands side and keep the base literal for `observed_at_base`.

## Attacks that FAILED (the claim survived)

- **Frozen files after the operative freeze**: zero commits touch `claims.json`/`ledger.json` in
  `00c408a0..main`; blobs identical at `5e4796c`, `c4bf61a`, `d7a3840`, `1d7add3`, `main` (Q4).
- **Freeze ancestry and config sourcing**: `de93d91c`/`3595c919` are ancestors of `00c408a0`; the counter
  header prints `config sha256 (frozen claims.json): 270e3179…` and `config source: git show 00c408a0af2f:…`,
  matching the frozen blob (content hash `270e31790e2932c8…`), not the tree.
- **Legs reproduce at the lands**: `ACCEPT-C-74: PASS legs=13/13` at `c4bf61a`, `ACCEPT-CA-74: PASS
  legs=11/11` at `5e4796c`, both from a throwaway clone whose local `main` was pinned to the land
  (`git branch -f main <lands>` inside the clone only).
- **Ledger-change disclosure (Q2)**: all 75 changed lines fall under R74-M9's named categories.
- **False attribution check**: the named Ca junk classes (`stub-rows`, `append-only-removal`,
  `protected-in-place`, `unnamed-in-place`, `shell-string`, `interpreter`, `constant-printer`, `min-pairs`,
  `config-edit-*`, `typed-receipt`) all exist as selftest scenarios in `selftest-ca.txt:43`
  (`SELFTEST OK: 179 checks across 41 scenarios reported-fail=0`), even though the claim attributes them to
  `junk-ca.txt`, which holds only `J4, J4b, J5, J6, J7, J8, J9`. That is a loose pointer, not a missing control.

## Residual risk and verification gaps

1. **F1 is a grading hazard today.** `/tmp` is 100% full on this host; any grader who follows the
   assignment's `mktemp -d` recipe will fail at clone materialization (I hit
   `fatal: cannot create directory at …: No space left on device` at 23:05). The PASS-at-lands result is
   only reproducible from a `/tmp` clone. This needs a host-level cleanup or a counter that tolerates a
   different temp root (F1's fix).
2. **Ca at the combined tree.** `junk-ca.txt`'s T0 (both claims landed in one tree) shows
   `T0 Ca: FAIL legs=9/11 red=APPENDONLY,SEPARABLE`, disclosed there as a frozen-claims limit ("claim Ca is
   therefore measured at its OWN landing commit"). The assignment grades Ca at `5e4796c`, which passes; a
   reader grading the final `main` tree with the Ca counter gets FAIL. I did not treat this as a new
   finding because the receipt states it, but it is the largest undisclosed-to-the-claims limit: the two
   frozen claims are not jointly satisfiable at the final tree.
3. **No seat report pins the claims bytes it scored.** Wave-1 reports quote leg text
   (`RevClaimsFidelity.md:161` quotes the old `>= S881` wording; `ExecCaCounter.md:343-344` the new one),
   but none records `sha256(claims.json)`. So "which frozen bytes each seat attacked" is inferable from
   commit order only; a report-level config hash would close that gap.
4. **Self-referential control receipt.** `controls-ca.txt` at `<freeze>` is itself in the SEPARABLE read
   set (`scanned=[… 'reports/round-74/telemetry/controls-ca.txt' …]`); the committed control therefore
   measures a tree that contains its own previous output. R74-M9 names this ("SEPARABLE red only because
   the earlier receipt was still in the lands tree"), and the regenerated receipt in `5e4796c` fixes the
   text, but the do-nothing control can never be run at the freeze that first commits it without this
   self-reference. Worth a sentence in the control's own header.

## Tooling record

No installs, no upgrades, no pacman (paused host-wide). Tools used: `git` (read-only in the lane; writes
only in `/tmp` and my home scratch clone), `python3 -B`, coreutils. Scratch removed after the run.
