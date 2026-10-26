# CritMistakeRows — round 74, wave 2 (kotodama, hyaku run 7) — critic

Seat: `CritMistakeRows` (leaf; no subagents, no background jobs, no fleet/lane writes).
Lane repo read-only: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; operative freeze `00c408a0af2fa5ddf65af2224152ce258b26d896`;
claim Ca lands `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`; claim C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`;
lane `main` at dispatch `1d7add3f7b9eaf6f3349c56c36f6d06325d74236`.

ATTACK: the `## Mistakes` table (R74-M1..M10) of `corpus/lessons/round-74.md`, plus R74-M9's chronology.

Scratch (outside both trees): `/var/tmp/CritMistakeRows-3/` (clone of the lane, `git clone` at
`lab.YCLi/lane`, local `main` forced per run inside it only) and `/tmp/CritMistakeRows-3.G2W4/`.
`/tmp` was 100% full (`/dev/nvme1n1p1 128G 128G 14M 100% /tmp`), so the lab clone lives under `/var/tmp`;
`TMPDIR=/var/tmp/CritMistakeRows-3` was exported for every counter run. No tools installed (nothing needed);
no pacman. Nothing written under `kotodama-shokunin/` except this file.

---

## Verdict (short)

The class column survives: all ten rows use a class from the `.ufo/waves/kaika-w1/mistakes.md` §5 vocabulary
(`vacuous`, `survivor`, `stale-premise`, `reference-drift`, `number-drift`, `scope`, `attribution`, `landing`,
`provider`) and no row uses a foreign one. Every evidence pointer I was asked to run resolves except the one
inside R74-M9 (F1). The table does **not** survive on three counts: one row's fix points at the wrong artifact and
misdescribes it (M9), two rows' state fields are contradicted by committed bytes (M4 false at its own commit, M3
stale at main), and one row's fix description is false about its own artifact (M7). Four round-level defects the
table should carry are absent (F2, F3, F4, and the M10 set).

| id | class in vocab | evidence resolves | captured-by = rule that existed | fix shown able to fail | state honest |
|---|---|---|---|---|---|
| R74-M1 | yes (`landing`) | yes (`round-73-verifier-spotcheck.md:13`, `w1/ExecLeftovers.md` §Verdict) | no — `none` then two seat reports (F10) | **shown** (mutation arm `tracked-missing`/`tracked-blob-mismatch` → `TRACKED=FAIL`, `selftest-ca.txt`; base red is prose only) | yes (`fixed at freeze`; six pins re-hashed, all six match) |
| R74-M2 | yes (`landing`) | yes (both `git grep` forms exit 1 at base; `controls-ca*.txt` = 5/9, 4/9, 4/9) | `none` — correct | **shown** (`typed-receipt`/`receipt-wrong-rev`/`receipt-missing` → `RECEIPTS=FAIL`; RECEIPTS byte-compares stdout, `accept-ca.py:1824`) | yes |
| R74-M3 | yes (`survivor`) | yes (`MutPredicateC.md` F1–F7; 12 probes, survivors P1,P2,P3,P4,P5b,P6b,P7a,P7b = 8/12) | `none` — correct | shown after the fact (`junk-c/ca.txt` at `1d7add3`: every round-74 junk `accepted: no`) | **stale at main** (F8) |
| R74-M4 | yes (`number-drift`) | yes (`LOG.md:4297`, fleet `:10`, `selftest-r3.txt:6`, `grep -c scenarios SCORECARD.md` = 0) | yes (QUALITY 17/19/23 exist in `corpus/QUALITY.md` at base) | **shown** (the pair's re-derive command returns 10) | **FALSE — says `pending landing`, landed in `5e4796c`, an ancestor of the lesson's own commit (F8)** |
| R74-M5 | yes (`attribution`) | yes (`census-adjudication.json` S758 url=2025 page/quote=这个我肯定考虑过…, S759 url=2022 page/quote=Sowers-Wills, both `binding: id`, both `still_absent`) | no — a seat report, not a rule (F10) | n/a (`open — routed`, no fix claimed) | yes |
| R74-M6 | yes (`vacuous`) | yes (`S882.txt`: `window: chars=2953 min=4096 before=631 after=2289`, `visible-chars: 2953`, `window-scope: whole-document`; amendments present in `claims.json` at `de93d91` already) | no — a seat (F10) | **shown** (`w1/ExecEvidence.md:341,355`: `S882 FAIL window=2953 … (want >= 4096)`; code enforces both limbs, `accept-c.py:1208-1226`) | yes (weakness: the two named C-side mutants have no committed per-scenario output, F11) |
| R74-M7 | yes (`scope`) | yes (GATE leg carries both limbs; cell quote = 54 chars/7 tokens) | partly (`L1` exists in kaika §5; the seat is also named) | **NOT shown** — no committed red-before for the 80-char limb, **and the fix's own statement is false (F7)** | `resolved by L1 amendment` — not honest as written (F7) |
| R74-M8 | yes (`reference-drift`) | yes (`w1/RevClaimsFidelity.md` F1) | no — a seat (F10) | **shown** (`drafts/round-74.md:175`: `py_compile` exit 1, `SyntaxError: line 2159`, four revisions; after: `SELFTEST: 69/69` at all three freezes) | yes |
| R74-M9 | yes (`survivor`) | **the fix's cited artifact is the wrong one (F1)**; the individual repairs resolve | `none` — correct | **shown as a bundle** (ledger tokens, LC-01→ANNOTATE, LC-09 de-pinned, redaction, `proof.txt`, gap-sweep head all verified before/after) — but not re-checkable from the pointer | `fixed before data` — the pointer is false (F1), the claim-side control text is false (F2) |
| R74-M10 | yes (`scope`) | residue resolves (`.postwave.md` exist, round-73 blobs = `2d1cd91` blobs, `grep -c 'Post-wave update'` = 0) | no — `the misroot sweep` is not a rule (F10) | **NOT shown** as a failing command; and **the name set is wrong (F5, F6)** | `fixed` — over-claimed |

Rows whose state claims `fixed` without any red-before: **R74-M7** (`resolved by L1 amendment`) and
**R74-M10** (`fixed`). R74-M1/M2/M6/M8 do have a committed failure state (mutation arm or pre-fix output);
R74-M9's bundle does, but behind a false pointer.

---

## Findings

### F1 — HIGH — R74-M9's "post-repair control" is the *pre-repair* receipt, and it does not show "SEPARABLE red only"

The row's fix column says: "`telemetry/controls-ca.txt` at `00c408a0…` is the post-repair control and shows
SEPARABLE red only because the earlier receipt was still in the lands tree".

Two independent checks falsify the description.

```
$ for c in 3595c91 00c408a; do git show $c:reports/round-74/telemetry/controls-ca.txt | sha256sum; done
9df3e3a199d93653725d6dc3b3ee0cffd6275e925093e52ca6aa580f24f6e0d5  -
9df3e3a199d93653725d6dc3b3ee0cffd6275e925093e52ca6aa580f24f6e0d5  -
$ git show 00c408a:reports/round-74/telemetry/controls-ca.txt | sed -n '1,12p'
# controls-ca.txt — claim Ca do-nothing controls (round 74), measured at freeze de93d91cab5a… by the freeze-installed counter
# counter sha256 (self): dd755893f72cb8e93b8c53577188ad3b868bd3367c76b0ab789e19227ca520ec
# stamped revision: de93d91cab5a4f19fbe20b948abca67b8e9c7650
$ git show 00c408a:reports/round-74/accept-ca.py | sha256sum
8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f  -
$ git show 00c408a:reports/round-74/telemetry/controls-ca.txt | grep -E "^LEG (PASS|FAIL)|^ACCEPT"
LEG PASS LEDGER / LEG FAIL BASEMISMATCH / LEG FAIL REPAIR / LEG FAIL ANNOTATE / LEG FAIL NOSTUB /
LEG FAIL APPENDONLY / LEG FAIL SEPARABLE / LEG PASS TRACKED / LEG PASS RECEIPTS / LEG PASS FROZENCFG / LEG PASS STAMP
ACCEPT-CA-74: FAIL legs=5/11
```

The file at the operative freeze is byte-identical to the re-freeze's file, was produced by the **`de93d91`
counter** (`dd755893…`) at the **`de93d91`** freeze, and is red on **six** legs (`BASEMISMATCH`, `REPAIR`,
`ANNOTATE`, `NOSTUB`, `APPENDONLY`, `SEPARABLE`), with `RECEIPTS` **green**. The actual post-repair control is the
one committed in the landing commit:

```
$ git show 5e4796c:reports/round-74/telemetry/controls-ca.txt | sed -n '1,8p'
# controls-ca.txt — ... measured at freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 by the freeze-installed counter
# counter sha256 (self): 8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f
$ … | grep -E "^LEG FAIL|^ACCEPT"
LEG FAIL REPAIR / LEG FAIL ANNOTATE / LEG FAIL NOSTUB / LEG FAIL SEPARABLE
ACCEPT-CA-74: FAIL legs=7/11
```

Impacted axes: calibration (records fidelity). The fix is fixable prose, not a broken repair — the redaction fix
itself **is** shown able to fail: the unredacted literals `S909`, `S910`, `S894` and `worldbuilding-setting-practice`
appear in the `SEPARABLE` detail of the pre-repair receipt and are replaced by `<redacted lane id>` in the
post-repair one.

Smallest safe correction: rewrite the clause to read "`controls-ca.txt` at `3595c91`/`00c408a` is the **red-before**
(pre-repair counter `dd755893`, six red legs); the post-repair control is `controls-ca.txt` at `5e4796c` (counter
`8052f1e2`, `SEPARABLE` red only because the stale receipt is still in the `00c408a` lands tree)". Do not change
`claims.json` (frozen).

### F2 — HIGH — the frozen claim Ca's stated do-nothing-control shape is false against *both* committed controls

`claims.json` at the freeze (`sha256 270e31790e2932c8…`), claim Ca, `do_nothing_control`:

> "(1) lands == <freeze> FAILS with REPAIR, ANNOTATE, RECEIPTS red and FROZENCFG/LEDGER green"

The two controls that exist for Ca show `RECEIPTS` **PASS** and two extra red legs (`NOSTUB`, `SEPARABLE`, and at
`de93d91` also `BASEMISMATCH`/`APPENDONLY`). Raw: the `00c408a` and `5e4796c` `grep -E "^LEG (PASS|FAIL)"` blocks in
F1. The counter deliberately does not red `RECEIPTS` in this shape (`accept-ca.py:1843-1845`: freeze == lands prints
`NOTE lands == freeze: do-nothing control shape … a PASS is refused` **while the leg still returns PASS**).

R74-M9's fix column claims the "claims text amended for the must_track exemption and the lane-id set" — the
amendment did not reconcile this limb, and the pre-data rule ("a rule changed after any seat scores landed data is
not the claim's rule") makes the frozen text the rule. So a stated artifact of a frozen claim is contradicted by
the round's own committed receipts; the M-row set carries no row for it.

Impacted axes: calibration. Smallest safe correction: a round-75 row (class `stale-premise`) quoting the frozen
sentence and the two `LEG PASS RECEIPTS` lines, with the flip "state the observed red set, or make `RECEIPTS` red
in the do-nothing shape"; the frozen `claims.json` is not amended.

### F3 — HIGH — live defect with no Mistakes row: claim Ca is FALSE on the tree the round leaves

`accept-ca.py` at the round's final tree (my clone, `main` = `1d7add3`):

```
$ python3 -B reports/round-74/accept-ca.py --root . --lands 1d7add3f7b9eaf6f3349c56c36f6d06325d74236 \
    --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
LEG FAIL APPENDONLY
     … problems=['corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]']
…
ACCEPT-CA-74: FAIL legs=10/11
exit=1
```

Same counter, same freeze, at Ca's own lands:

```
$ python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3 …
ACCEPT-CA-74: PASS legs=11/11      exit=0
```

Claim C stays green at the same tree (`ACCEPT-C-74: PASS legs=13/13`, exit 0). So the two frozen claims conflict:
C's required in-place `used-by` change on the reused row S877 (`corpus/SOURCES.md:832`) is outside Ca's REPAIR
`stated_at` lines, and once C lands, Ca's `APPENDONLY` leg is permanently red. The frozen Ca kill rule is "any leg
false at `<lands>` -> the claim fails as stated", and no claim pins `<lands>`. The only record is a NOTE inside
`reports/round-74/telemetry/junk-ca.txt` (committed at `1d7add3`, after the lesson), plus `measures-ca.txt`'s header.
`grep -n "own landing\|APPENDONLY\|conflict" corpus/lessons/round-74.md` returns only rows 174/176 (unrelated
strings), i.e. **the lesson does not disclose it**.

Impacted axes: calibration and the claim itself. Smallest safe correction: append one row to `## Mistakes`
(class `survivor`, state `open — routed`): evidence = the two commands above; fix = "Ca is green only at its own
commit; any tree that also carries C's S877 change fails `APPENDONLY`; round 75 must either add the C-used-by line
to Ca's REPAIR set before freeze, or measure Ca at its own commit and say so in the Claims line". Also pin the two
`<lands>` commits in the Claims line, since today they are only in telemetry headers.

### F4 — HIGH — a counter changed twice after freeze with no `reports/round-74/counter-revisions.md`

`corpus/QUALITY.md:77` (criterion 23): "a leg or scenario changed after freeze is a recorded counter revision
(`reports/round-<N>/counter-revisions.md`: old sha, new sha, what moved, whether the predicate moved) with the
selftest re-run and a red-before".

```
$ for c in de93d91 3595c91 00c408a; do git show $c:reports/round-74/accept-ca.py | sha256sum; done
dd755893f72cb8e93b8c53577188ad3b868bd3367c76b0ab789e19227ca520ec  -
26dd04a4971e6dcee4bd7a021ef9f876a93a0ea2c2f27943ff60539c11c0fe53  -
8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f  -
$ git ls-tree -r --name-only 1d7add3 | grep -i counter-revision
reports/round-73/counter-revisions.md          # round 73's file survives; round 74's does not exist
$ ls reports/round-74/
accept-c.py  accept-ca.py  claims.json  evidence  ledger.json  telemetry
```

Three counter revisions, zero revision records; R74-M9 is the only place the changes are described, and it neither
gives old/new sha nor discusses whether each *predicate* moved (e.g. `SEPARABLE`'s scan set grew to include
`reports/round-74/telemetry/controls-ca.txt`, visible in the `scanned=[...]` diff). Re-freezing does not satisfy the
criterion as written: the changes are still "after freeze".

Impacted axes: calibration. Smallest safe correction: add `reports/round-74/counter-revisions.md` with the three
sha256s above, the moves per freeze (BASEMISMATCH leading-token, APPENDONLY must_track exemption, SEPARABLE lane-id
set + redaction, empty-tree pin exemption), `predicate-moved: yes/no` per item, the selftest re-run lines already in
`telemetry/selftest-ca.txt` (three distinct blobs: `7d6955f0…`, `2bc96a50…`, `eed1e32b…`), and the red-before (the
`de93d91` receipt with the literals). Reference it from R74-M9.

### F5 — MEDIUM — R74-M10's ten-name list contains two names that existed in no round-71..73 wave

Independently reproduced part of `.ufo/waves/round-74/w2/ExecWaveLedger.md` F3 (which already scores this HIGH at
26 collisions vs 10 listed):

```
$ python3 … # name fields of .ufo/waves/round-7{1,2,3}/w*/spec.json and results.json
ScribeQuality25 []
ExecEvidence []
ScribeMistakes ['.ufo/waves/round-73/w1/spec.json']
ExecCCounter ['.ufo/waves/round-72/w1/spec.json', '.ufo/waves/round-73/w1/spec.json']
```

The row's mechanism is "messages to seats named like the round-73 seats of this lane reached same-named parked
round-73 seats". For `ScribeQuality25` and `ExecEvidence` there is no such parked seat in round 71–73, so the row's
stated mechanism cannot apply to 2 of its 10 names, and the list is a subset of the 26-name intersection. The two
*observed appends* (`ExecLedger.md`, `ScribeReadmeIndex.md`) are unaffected.

Impacted axes: calibration (attribution). Smallest safe correction: replace the ten-name list with the computed
26-name intersection and mark the two names that did produce appends; keep the fix as is.

### F6 — MEDIUM — R74-M10's fix names no report and its failure state is not shown as a command

The row says "…the round-73 files restored from the branch (`git show main:<path>`), **and the report names the
misdelivery**". No report path is given. The two residue files do not say it either:

```
$ head -1 .ufo/waves/round-74/w1/ExecLedger.postwave.md
## Post-wave update — round 74 ledger finalization (L1 follow-up)
$ head -1 .ufo/waves/round-74/w1/ScribeReadmeIndex.postwave.md
## Post-wave update
$ grep -c "Post-wave update" .ufo/waves/round-73/w1/ExecLedger.md .ufo/waves/round-73/w1/ScribeReadmeIndex.md
0
0
$ for p in .ufo/waves/round-73/w1/{ExecLedger,ScribeReadmeIndex}.md; do git rev-parse 2d1cd91:$p 00c408a:$p; done
25dd5f52… 25dd5f52…        # restored: identical blob at the round-73 lands and at the freeze
56030504… 56030504…
```

So the state is verifiable *after* the fact (restored bytes + residue), but nothing committed shows the pre-fix
failure: the dirty worktree was thrown away, and no receipt records `git status` naming those two files. That is a
row whose state says `fixed` without a red-before (L1/CORPUS bar).

Impacted axes: calibration. Smallest safe correction: name the report that carries the disclosure (or add one
sentence to `w1/ExecLedger.postwave.md`), and commit the observed before-state as a one-line receipt (path list +
blob/sha mismatch), so the fix keeps its failing arm.

### F7 — MEDIUM — R74-M7's fix statement is false about its own artifact, and the 80-char limb has no committed red-before

The row's fix says "the cell carries the 54-character, 7-token first clause; **the full sentence stays on the evidence
file's `quote:` line**". It does not:

```
$ sed -n '13p;29p;31p;35p' reports/round-74/evidence/S877.txt
quote-chars: 54
locator: p.7 (PDF page 7; sentence: "Язык – главный / инструмент построения вымышленных миров, дающий названия для их / природных и социальных реалий, ..." — quote is the head clause, 54 chars / 7 tokens per the L1; …)
quote: Язык – главный инструмент построения вымышленных миров
Язык – главный инструмент построения вымышленных миров
$ python3 - # the 108-char span, measured in the stored window
upto реалий chars 108 tokens 15
```

The `quote:` line holds the same 54-character clause as the GATE cell; the 108-character/15-token span survives
only in the `locator:` prose, with PDF line-break markers (`/`) and a trailing `, ...`, i.e. neither verbatim nor on
the `quote:` line. The lesson's Gate note (line 26) repeats the same false sentence. And the 80-character limb has no
committed red-before: the arm exists as `MUTANTS["gate_quote_chars"]` (`accept-c.py:2727`) but the only committed
output is the count line `SELFTEST: 69/69 scenarios` (see F11). So the row is neither "resolved" as described nor
shown able to fail.

Impacted axes: coverage evidence. Smallest safe correction: put the folded 108-character span on the evidence file as
its own field (`sentence:` or a second `quote:`), correct the Gate note and the M7 fix column to "the full span is on
the evidence file's `sentence:` line, the `quote:` line is the admitted clause", and commit the failing arm (a
108-character cell → `LEG FAIL GATE`).

### F8 — MEDIUM — two state fields disagree with the tree they were committed in

R74-M4 state = `pending landing`, but the correction rows landed *before* the lesson was finalised:

```
$ git log --format='%h %ci %s' de93d91..main
1d7add3 2026-10-25 22:59:06 …junk-landing receipts…
c4bf61a 2026-10-25 22:50:09 …claim C landing fixes — entry header template tokens, lesson counts sentence
d7a3840 2026-10-25 22:49:29 …claim C landing…
5e4796c 2026-10-25 22:48:30 …claim Ca landing — SCORECARD corrections (12 annotated pairs)…
$ git show c4bf61a:SCORECARD.md | grep -n "| LC-0[23] "
1443:| LC-02 | 9 | 10 | git grep -h -o -E 'SELFTEST OK. [0-9]+ scenarios' f7104cbce186… -- reports/round-73/telemetry/selftest-r3.txt |
1444:| LC-03 | 9 | 10 | git grep -h -o -E 'SELFTEST OK. [0-9]+ scenarios' f7104cbce186… -- reports/round-73/telemetry/selftest-r3.txt |
```

`5e4796c` is a first-parent ancestor of `d7a3840`/`c4bf61a`, so at the lesson's own commit M4's fix was already
landed and green (`accept-ca` at `5e4796c`: `LEG PASS ANNOTATE rows=14 annotate-pairs=12`). R74-M3's
`pending landing` is true at `c4bf61a` but false at the tree the round leaves (`junk-c.txt`/`junk-ca.txt` land at
`1d7add3`). Both are the same state-drift class the table records as R74-M4 elsewhere.

Impacted axes: calibration. Smallest safe correction: set M4 to `fixed at landing (5e4796c)` and M3 to
`fixed at landing (1d7add3)` — or the honest alternative, `fixed at landing, receipt committed after the lesson`
— so no reader re-runs a green check looking for red.

### F9 — LOW — R74-M9's `LC-01 moved to ANNOTATE` contradicts the same lesson's own routed item

The routed item 3 says "M4 `SHONEN.md:6` still says '412 rows after round 56' against 804 rows (**a REPAIR**, since
SHONEN is not append-only)". The ledger at the operative freeze has `PAIR LC-01 disposition=ANNOTATE` and the landing
row is an annotation (`SCORECARD.md:1442`), while `SHONEN.md:6` still reads `412 rows after round 56` at `c4bf61a`.
One file, two classifications for one line. The M9 disposition is defensible (no in-place repair inside the claim),
but the lesson should say which is authoritative.

Impacted axes: calibration. Smallest safe correction: add "LC-01 is annotated this round and routed as a REPAIR"
to the routed item, or drop the "a REPAIR" parenthetical there.

### F10 — LOW — the `captured-by` column is a finder column for six rows

CORPUS's rule is "captured-by (the `QUALITY.md` criterion or protocol rule that should have caught it, or `none`)".
Rows M1 (`none — the verifier spot-check, then ExecLeftovers`), M5 (`ScoutQuarantine816817.md §4`), M6
(`ScribeMistakes (wave-1 follow-up)`), M7 (`this seat …, confirmed by the L1 amendment`), M8 (`RevClaimsFidelity
F1 (wave 1)`) and M10 (`the misroot sweep`) name the seat/report that found the mistake, not a criterion that should
have caught it. M1 additionally self-contradicts: the wave-1 draft's own note says "M1 `none` (PROTOCOL `landed means
committed` binds the report …)" — if that protocol rule binds, `none` is the wrong value. Every named rule that *is*
named (QUALITY 17/19/23 in M4; L1 in M7) did exist before the round (`git show f7104cb:corpus/QUALITY.md` carries
16/17/19/…/23/24; `.ufo/waves/kaika-w1/mistakes.md` §5 carries L1–L5), so this is a form defect, not a fabrication.

Impacted axes: calibration. Smallest safe correction: give the rule (`QUALITY 23` for M8; `PROTOCOL landed-means-
committed` for M1; `QUALITY 21`-style Gate/reject discipline for M5) and keep the seat as a parenthesis.

### F11 — LOW — for claim C the selftest receipt is a count, so no named mutant's redness is committed

```
$ for c in de93d91 3595c91 00c408a; do git show $c:reports/round-74/telemetry/selftest-c.txt; done
SELFTEST: 69/69 scenarios
exit=0                       # identical at all three freezes
$ python3 -B reports/round-74/accept-c.py --selftest        # my clone, main = c4bf61a
SELFTEST: 69/69 scenarios
exit=0
```

`MUTANTS` holds 57 named arms (`accept-c.py:2702-2775`, `drop_entry` … `index_older_footer_edited`) including the two M6 names
(`window_scope_whole_4096`, `window_scope_visible_mismatch`) and the M7 name (`gate_quote_chars`), and my re-run is
green — so the harness works. But a count line cannot distinguish "the arm fired and passed" from "the arm was
deleted"; the observed failure text L1 asks for is not committed for any claim-C arm, while the Ca receipt does print
`scenario -> exit=N LEG=FAIL` per arm. The round's end-to-end junk receipts (`junk-c.txt`: J1→ENTRIES, J2→EVIDENCE,
J3→FROZENCFG, J9→leg deletion) do carry observed failure text, so the *channel* is covered; only the specific M6/M7
mutants lack it.

Impacted axes: coverage evidence. Smallest safe correction: run two arms by hand and commit their stdout
(`SELFTEST: 68/69 scenarios` + the failing scenario line) under `reports/round-74/telemetry/`, as the round already
did for Ca.

---

## R74-M9's chronology against `git log` — the attack that FAILED

Everything the row asserts about ordering and about the specific reds is true:

```
$ git log --format='%h %p %ci' de93d91^..main     # first-parent chain, timestamps
de93d91 2026-10-25 22:28:24 -0300   (first freeze)
3595c91 parent=de93d91 22:37:37 -0300   (re-freeze)
00c408a parent=3595c91 22:46:35 -0300   (operative freeze)
5e4796c parent=00c408a 22:48:30 -0300   (Ca landing)
d7a3840 parent=5e4796c 22:49:29 -0300   (C landing)
c4bf61a parent=d7a3840 22:50:09 -0300   (C landing fixes)
1d7add3 parent=c4bf61a 22:59:06 -0300   (telemetry)
$ git rev-parse de93d91c 3595c919 00c408a0
de93d91cab5a4f19fbe20b948abca67b8e9c7650 / 3595c9192ac4d066d01b937b2513d2d0eea55f4f / 00c408a0af2fa5ddf65af2224152ce258b26d896
```

- three freezes, in the stated order, on one first-parent chain, and the short shas are unique;
- the first control really was produced by the `de93d91`-installed counters: `counter sha256 (self)` =
  `8d30487f…`/`dd755893…`, exactly the blobs committed at `de93d91`;
- every red reason the row names is in that receipt: BASEMISMATCH's prose-after-token
  (`LC-01 … '804 (argv prints `f7104cbce186…'`), APPENDONLY naming the six inherited files, GROUND
  (`receipt names a 19-row registry; the base holds 804`), COLLCHECK (`no indent-guard proof … no four-space
  control`), SEPARABLE with `S909`,`S910`,`S894` on the `LC-16`/`LC-12` stated lines
  (`corpus/lessons/round-73.md:138` carries `S909/S910/S929/S930/S923`; `reports/round-73/claims.json:11` carries
  `S894`/`S910`);
- every repair the row lists is observable: ledger `observed_at_base` prose → tokens
  (`'804 (argv prints …' → '804'`), `LC-01` `REPAIR → ANNOTATE`, `LC-09`'s empty-tree pin gone, the
  `must_track-exempt=6` and `lane-ids=4` constants in `FROZENCFG`, `guard-proof/proof.txt` absent at `de93d91`
  and present at `00c408a`, gap-sweep head line without the registry sentence at `de93d91` and
  `registry: 804-row registry at base …` at `00c408a`.

So the chronology attack fails on order, attribution and red reasons. What breaks is only the row's pointer to its
own post-repair control (F1).

Other attacks that FAILED, stated plainly:

- **Class column.** Ten rows, all in the kaika §5 vocabulary; no invented class.
- **M1's pins.** All six ledger `must_track.sha256` values equal `sha256(git show de93d91:<path>)` (verified by
  hashing), the sixth is absent at `f7104cb`, present at `de93d91`/`main`, and `TRACKED` is `PASS paths=6` at the
  lands and at `1d7add3`.
- **M2.** Both `git grep` forms return 0 lines at `f7104cb`; the two receipts carry
  `stamped=evaluated=measured=2d1cd9140d3a…`, `ACCEPT-C-73: PASS legs=11/11`, `ACCEPT-CA-73: PASS legs=9/9`, and the
  RECEIPTS leg byte-compares stdout (`normalize_receipt(body) != normalize_receipt(rerun[key])` → fail).
- **M3's channel arithmetic.** `MutPredicateC.md` has 12 probes and its survivors are 8 (P1, P2, P3, P4, P5b, P6b,
  P7a, P7b); the round-74 junk battery rejects every fixture (`accepted: no` × 7 in `junk-ca.txt`, × 4 in
  `junk-c.txt` = 11 fixtures), with the round-73 red-before re-run in the same file.
- **M4's numbers.** `LOG.md:4297` "Ca 9 scenarios", fleet `:10` same, `selftest-r3.txt:6` `SELFTEST OK: 10
  scenarios`, `grep -c scenarios SCORECARD.md` = 0.
- **M5.** Exactly as described, `binding: id` on both, both under `still_absent`.
- **M6.** The amendment is in the frozen claims at the *first* freeze, the evidence file satisfies
  `whole-document` (2953 = 631+33+2289 = `visible-chars`), the counter enforces both limbs, and the pre-amendment
  failure is committed (`ExecEvidence.md:341,355`).
- **M8.** The `SyntaxError` red-before is committed verbatim at `.ufo/waves/round-74/drafts/round-74.md:175`
  (`py_compile` exit 1, four revisions with sha256s), and `SELFTEST: 69/69`/`179 checks across 41 scenarios` are
  the receipts.

---

## Limits of this attack (not claimed)

- I did not re-fetch any source (no network attack in this seat) and did not re-derive the Gate's S877 PDF sentence
  beyond the stored window; the 108-character span is measured from the stored window text, not from the PDF.
- "No seat had scored landed data at any of the three freezes" is not falsifiable from local bytes; left as an
  assertion.
- I did not adjudicate the sibling `ExecWaveLedger.md` F3/F4/F7 findings beyond reproducing the two `NOWHERE-PRIOR`
  names and the tracked status of that report; where it and this report overlap (M10), they agree.
- The full idiom `python3 -B reports/round-74/accept-ca.py` at `1d7add3` was run once (18 s); the C counter once
  (33 s) plus `--selftest` (~30 s). No other counter run was repeated.
