# ExecCounterO — claim O counter verification (round 64, wave 1)

Seat: `kotodama-r64.ExecCounterO` (executor, operability axis). Lane root
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` (jj-colocated, read-only git/jj used;
no commits, no jj/git mutations). Scratch: `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ExecCounterO/`.

Verdict: **ACCEPT-O-64: PASS** — all 23 legs of `reports/round-64/accept-o.py` (rev3) printed
`PASS` in one full lane-root run, the verdict line is `ACCEPT-O-64: PASS`, and the process exit
code is `0`. The tool under test is byte-unchanged this round.

---

## 1. Files changed (lane writes only)

| Path | Change | Bytes / sha256 |
|---|---|---|
| `reports/round-64/telemetry/final-measures-o.txt` | overwritten with the complete headered receipt (prior content was a stale 22-leg partial, sha256 `aef3faf6edf5834670b4ea4da7ed5342cc4f5c800048010d451171ee1a9183e4`; that exact prior byte content is preserved at `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ExecCounterO/prior-partial-final-measures-o.txt`, sha256 identical) | 3847 B, sha256 `009bbde3c7720a496b26f224646a5d99e6e55f247d22b9d9c38da93ccad84193` |
| `reports/round-64/telemetry/mut-o.txt` | **created** — MUT-only run receipt + sha256 of each of the ten mutant sources | 2840 B, sha256 `7c5df1d5d2256cce84a3152a9e299d46ea7191031ff3c03ad47e85153aca1842` |
| `reports/round-64/telemetry/edge-o.txt` | **created** — the eight redirect-edge/DRIP legs run receipt | 1561 B, sha256 `134d00444559837144ecf3d89df5618afa2b15168d83c49384800e48e59b9536` |
| `reports/round-64/telemetry/control-o.txt` | **created** — the claim's anti-baseline control (round-63 counter cannot score the new legs; docstring-only tool patch leaves GEN green and every mutant still killed) | 2972 B, sha256 `49eae130179c1125965097d75e2c6eb1ab2c4c5931e69c9311cc1d0c2ce11652` |
| `reports/round-64/mutants/{m1,m10,m2,m3,m5,m6,m7,m8,m9,mread}.py` | **created** — the ten byte-patched mutant sources, copied verbatim from the counter's own build dir (`work/mutants/`), each verified byte-identical to `tools/reopen-row.py` with the counter's own needle→replacement applied (see §5) | per-file sha256 listed in `reports/round-64/telemetry/mut-o.txt` |

Not touched: `reports/round-64/accept-o.py` (frozen rev3 — no edit, no revision appended),
`tools/reopen-row.py`, `claims.json`, `SCORECARD.md`, `LOG.md`, any corpus file, the jj index
and the lane git index.

`reports/round-64/mutants/` was created empty by attempt-1 and stayed empty (counter builds its
mutants under its own tempdir, `work/mutants/`, and deletes the tempdir at exit). It is now
populated with the ten mutant sources so the kill set is inspectable without re-running.

## 2. Step (1) — tool byte-identity

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
$ sha256sum tools/reopen-row.py
c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0  tools/reopen-row.py
$ git show ff30a205c8d23b35f1ac533740121a955a9fda96:tools/reopen-row.py | sha256sum
c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0  -
$ git diff --stat ff30a205c8d23b35f1ac533740121a955a9fda96 -- tools/reopen-row.py
(empty)
$ git status --porcelain tools/reopen-row.py
(empty)
```

Round-63 capability record (`reports/round-63/telemetry/freeze-sha256.txt`, the record the
SCORECARD round-63 operability row points at) carries the same value:

```
c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0  tools/reopen-row.py
```

**Tool byte-unchanged this round: yes** (worktree == base `ff30a205` blob == round-63 record).
The SCORECARD round-63 operability row names the *earlier* tool hash `0d965ccb` (the pre-MEDIUM-1
repair bytes) in its prose; the round-63 freeze receipt and `rev-hold-lift.md` both record
`c0f10a84…` as the patched bytes. **Defect (calibration, bookkeeping):** the SCORECARD prose and the
freeze receipt disagree about which bytes the round-63 capability was closed on; the SCORECARD row
should cite `c0f10a84…` (or both hashes with their dates). I did not edit SCORECARD.md — out of this
seat's scope.

## 3. Step (2) — the full run (detached, full stdout captured)

Launched detached from the lane root (the run takes >300 s; DEFAULT leg alone is 150 s):

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
$ nohup bash -c 'python3 -B reports/round-64/accept-o.py --root . \
    > /home/vgpnk/.cache/hyaku/kotodama-r64-w1/ExecCounterO/run-o.txt 2>&1; \
    echo "exit=$?" >> …/run-o.txt' >/dev/null 2>&1 &
```

No concurrent run was writing `reports/round-64/telemetry/final-measures-o.txt` during my run
(checked `ps -ef` before launching: no other `accept-o.py --root .`; the only other O activity was
CriticO's independent scratch-tree run under `/home/vgpnk/.cache/…/CriticO/`), so the canonical
path was overwritten rather than a timestamped sibling. The receipt now installed carries an
r61-style header naming the measured revision and both sha256s, then the verbatim stdout, then
`exit=0` as the final line.

Receipt head (`reports/round-64/telemetry/final-measures-o.txt:1-4`):

```
# final measures, claim O (round 64), measured revision b7d22703dfb684713826a4064e614264867e8cd (jj working copy @, parent 097c21d0eba5023cfd38b767fb41d59409eef125 = round-64 declaration commit; lane base ff30a205c8d23b35f1ac533740121a955a9fda96), 2026-10-24T02:37Z; worktree otherwise as measured
# counters: reports/round-64/accept-o.py (revision 3, working-copy bytes) sha256 c27a9fefb37c4a107e83867fd03f9194d89ce4e0dc8364e9b1b23e7821987b18
# tool under test: tools/reopen-row.py sha256 c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0 (identical to the ff30a205 blob sha256 c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0 and to the round-63 capability record reports/round-63/telemetry/freeze-sha256.txt: yes)
# command: python3 -B reports/round-64/accept-o.py --root .  (launched detached; stdout+stderr captured in full)
```

## 4. Steps (3) and (4) — all 23 legs PASS, MUT names all ten mutants

`reports/round-64/telemetry/final-measures-o.txt`, legs in claims.json order (23 leg lines, every
one `PASS`; verified programmatically: 23 legs, `all PASS: True`, leg-name sequence equal to
`claims.json` `O.legs`):

```
TOOL PASS path=tools/reopen-row.py exists=True executable=True
INDEP PASS named=[]
GEN PASS rows=61 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=61 expected=61 repeated_args=5 repeated_printed=5
BOUND PASS bad=[] unlisted_requests=[]
EXIT PASS gen_exit=1 body_exit=0 default_registry_exit=0
PRIV PASS exit=1 rows=[('S2905', 'REFUSED', 0), ('S2514', 'REFUSED', 0), ('S2957', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2845', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1 bursts=[3, 3, 3] gaps=[60, 60]
ERR PASS bad=[]
REDIRECT PASS allow_private=[('S2944', 'REFUSED', 1)] hits_src=1 hits_target=0 no_flag=[('S2944', 'REFUSED', 0)] exits=1,1
MALFORMED PASS exit=1 rows=[('S2673', 'MALFORMED', 0), ('S2191', 'MALFORMED', 0), ('S2740', 'MALFORMED', 0)] traceback=False
GZIP PASS exit=1 rows=[('S2171', 'LOCATED', 1), ('S2671', 'CAPTION_ONLY', 1)]
TRUNC PASS exit=1 rows=[('S2114', 'TRUNCATED', 1), ('S2421', 'LOCATED', 1)] want=[('S2114', 'TRUNCATED', 1), ('S2421', 'LOCATED', 1)]
TIMEOUT PASS exit=1 rows=[('S2685', 'UNREACHABLE', 3)] wall=6.0s stall_hits=3 span=4.0s
EDGE_SCHEMEREL PASS rows=[('S2131', 'REFUSED', 1)] tgt_hits=0 src_hits=1 tb=False
EDGE_USERINFO PASS cross=[('S2219', 'REFUSED', 1)] tgt_hits=0 same_auth=[('S2471', 'UNREACHABLE', 6)] ok=True
EDGE_HTTPS PASS cross=[('S2682', 'REFUSED', 1)] tgt_hits=0 same_auth=[('S2306', 'UNREACHABLE', 6)] ok=True
EDGE_MALTARG PASS rows=[('S2145', 'UNREACHABLE', 1)] exit=1 tb=False
EDGE_SLASHLESS PASS rows=[('S2452', 'LOCATED', 2)] dir_hits=1 root_hits=0 exit=0
EDGE_308 PASS rows=[('S2161', 'LOCATED', 2)] tgt_hits=1 exit=0
EDGE_5TH200 PASS rows=[('S2560', 'LOCATED', 5, 'http://127.0.0.1:39233/cfin-oyufbkpsq')] final=http://127.0.0.1:39233/cfin-oyufbkpsq exit=0
DRIP PASS rows=[('S2711', 'UNREACHABLE', 3), ('S2008', 'LOCATED', 1)] wall=12.0s drip_hits=3 span=8.0s tb=False
MUT PASS bad=[] mutants=10 kill_evidence=[…]
ACCEPT-O-64: PASS
exit=0
```

(The DRIP leg is the paired control of the counter: the drip body times out per wall budget —
`UNREACHABLE attempts=3`, three requests spanning 8.0 s, wall 12.0 s — while the fast body of the
same content answers `LOCATED attempts=1`.)

**MUT leg (step 4).** The line reads `MUT PASS bad=[] mutants=10 kill_evidence=[…]` and names all
ten mutants, each with its pinned leg printing `FAIL`:

```
m1->EDGE_SCHEMEREL FAIL rows=[('S2982', 'LOCATED', 2)] tgt_hits=1 src_hits=1 tb=False
m10->EDGE_USERINFO FAIL cross=[('S2493', 'UNREACHABLE', 6)] tgt_hits=0 same_auth=[('S2023', 'UNREACHABLE', 6)] ok=True
m2->EDGE_USERINFO FAIL cross=[('S2048', 'REFUSED', 1)] tgt_hits=0 same_auth=[('S2142', 'REFUSED', 1)] ok=False
m3->EDGE_HTTPS FAIL cross=[('S2987', 'UNREACHABLE', 6)] tgt_hits=0 same_auth=[('S2499', 'UNREACHABLE', 6)] ok=True
m9->EDGE_MALTARG FAIL rows=[] exit=1 tb=True
m5->EDGE_SLASHLESS FAIL rows=[('S2749', 'UNREACHABLE', 2)] dir_hits=0 root_hits=1 exit=1
m6->EDGE_308 FAIL rows=[('S2076', 'UNREACHABLE', 1)] tgt_hits=0 exit=1
m7->EDGE_5TH200 FAIL rows=[('S2666', 'UNREACHABLE', 5, '-')] final=http://127.0.0.1:36401/cfin-ztanon exit=1
m8->GEN FAIL rows=61 wrong=1 ["REDIRECT_LOOP:S2087:want=UNREACHABLE/5:got=[('UNREACHABLE', 6)]"] summary_ok=True exit=1; BOUND FAIL bad=['REDIRECT_LOOP:l2:want=2:hits=3'] unlisted_requests=[]
mread->DRIP FAIL rows=[('S2513', 'UNREACHABLE', 3), ('S2791', 'LOCATED', 1)] wall=90.1s drip_hits=3 span=60.0s tb=False
```

Mutant set present: `m1, m10, m2, m3, m9, m5, m6, m7, m8, mread` — 10/10, `mutants=10`, `bad=[]`.

**Format note (calibration):** the counter does not print the literal token `pinned_fail=True` on a
PASS. `pinned_fail` appears only inside the `bad=[…]` list on failure (`accept-o.py:1087-1100`), so a
passing MUT line proves `pinned_fail=True` for all ten only indirectly, via `bad=[]` +
`mutants=10` + ten `kill_evidence` entries each showing its pinned leg printing `FAIL`. The correct
passing signature is the one present. (Same observation independently filed by ReviewerOReceipt.)

**Mutant source bytes verified** (every needle occurs exactly once in the tool, and each persisted
`reports/round-64/mutants/<name>.py` equals `tools/reopen-row.py` with the counter's own
needle→replacement applied — checked by parsing the `MUTANTS` table out of the frozen counter with
`ast`, not by re-typing the patches):

```
m1   pinned=EDGE_SCHEMEREL needle_count=1 bytes_match=True 545205e312b752e4…
m10  pinned=EDGE_USERINFO  needle_count=1 bytes_match=True 930f9804edb31312…
m2   pinned=EDGE_USERINFO  needle_count=1 bytes_match=True c743317cc9c6b581…
m3   pinned=EDGE_HTTPS     needle_count=1 bytes_match=True d773f173ca86d00b…
m9   pinned=EDGE_MALTARG   needle_count=1 bytes_match=True 4b0d7890e1c6aecb…
m5   pinned=EDGE_SLASHLESS needle_count=1 bytes_match=True 83ecd7341afe979f…
m6   pinned=EDGE_308       needle_count=1 bytes_match=True 9fcf7cd42f9a2099…
m7   pinned=EDGE_5TH200    needle_count=1 bytes_match=True 54d7c713ea868230…
m8   pinned=GEN,BOUND      needle_count=1 bytes_match=True d91560a11d0588ea…
mread pinned=DRIP          needle_count=1 bytes_match=True 660326454bdb216e…
ALL MATCH: True
```

Full sha256 values are in `reports/round-64/telemetry/mut-o.txt`.

## 5. Step (5) — `reports/round-64/mutants/` directory state

Before this seat: directory existed, **empty**, mtime 17:13 (attempt-1 artifact); the rev3 counter
builds its mutants under `work/mutants/` inside its own tempdir and `shutil.rmtree`s the tempdir at
exit, so the lane directory could never be populated by a plain run. After this seat: the directory
holds exactly the ten byte-patched mutant sources `m1.py, m10.py, m2.py, m3.py, m5.py, m6.py, m7.py,
m8.py, m9.py, mread.py`, each copied verbatim out of the counter's build dir during the live MUT run
(scratch copies in `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ExecCounterO/counter-mutants/`, and
verified byte-identical to the counter's own needle→replacement as shown above).

## 6. Additional receipts produced (declared claim-O lands that were absent and unowned)

`claims.json` `O.lands` names four telemetry files; before this seat only `final-measures-o.txt`
existed, and it was a stale partial. The other three were unowned in the live wave plan (flagged
independently by ReviewerOReceipt); CriticO confirmed in-band that it does not own
`control-o.txt`. All three are now present and green:

* `reports/round-64/telemetry/mut-o.txt` — `python3 -B reports/round-64/accept-o.py --root . --only MUT`
  → `MUT PASS bad=[] mutants=10 …`, `ACCEPT-O-64: PASS`, `exit=0` (1 PASS leg; the other 22 print
  `SKIP` by design of `--only`).
* `reports/round-64/telemetry/edge-o.txt` — `python3 -B reports/round-64/accept-o.py --root . --only
  EDGE_SCHEMEREL,EDGE_USERINFO,EDGE_HTTPS,EDGE_MALTARG,EDGE_SLASHLESS,EDGE_308,EDGE_5TH200,DRIP` →
  8 PASS legs (EDGE_SCHEMEREL/USERINFO/HTTPS/MALTARG/SLASHLESS/308/5TH200, DRIP), `ACCEPT-O-64: PASS`,
  `exit=0`.
* `reports/round-64/telemetry/control-o.txt` — the claim's anti-baseline, two controls:
  1. the round-63 counter cannot score these properties at all:
     `grep -nE 'EDGE_|DRIP' reports/round-63/accept-o.py` → **no matches** (grep exit 1), and
     `python3 -B reports/round-63/accept-o.py --root . --only MUT` → `error: unrecognized arguments:
     --only MUT`, exit 2;
  2. a do-nothing patch to the tool (docstring-only edit, patched sha256
     `f3789feee1488b9a64da05f93e8aeeac3afadbc173ef76ad6a7b3362e7e9bb61` vs lane
     `c0f10a84…`) run against the round-64 counter from a scratch root: `GEN PASS rows=61 wrong=0 []`
     plus `MUT PASS bad=[] mutants=10` with the same ten kills — i.e. the MUT leg is not satisfied by
     a cosmetic edit, and the kill set is real.

## 7. Open findings (no counter patch made; the counter is frozen rev3)

1. **MEDIUM — "fail exactly their pinned leg" is not verified by the counter (claim-text
   overstatement).** The counter runs each mutant with `--only <pinned>`; every other leg prints
   `SKIP`, so the observed failure set cannot exceed the pin set and exclusivity is never tested.
   Independently confirmed here on the m5 mutant (slashless-Location → server-root patch), built
   from the counter's own bytes and run with both legs enabled:
   ```
   $ python3 -B reports/round-64/accept-o.py --root <scratch>/m5root --only EDGE_SCHEMEREL,EDGE_SLASHLESS
   EDGE_SCHEMEREL FAIL rows=[('S2117', 'UNREACHABLE', 2)] tgt_hits=0 src_hits=1 tb=False
   EDGE_SLASHLESS FAIL rows=[('S2090', 'UNREACHABLE', 2)] dir_hits=0 root_hits=1 exit=1
   ACCEPT-O-64: FAIL
   exit=1
   ```
   So m5 fails **two** legs, not just its pin. (CriticO and ReviewerOReceipt observed the same
   independently.) Also note `m8` is pinned to **two** legs (GEN+BOUND), so "their pinned leg" is
   singular only for eight of the ten. The frozen predicate does not require exclusivity and the
   MUT leg passes as written; the claim sentence in `claims.json` (`O.statement`: "ten byte-patched
   mutants each fail exactly their pinned leg") is therefore stronger than what is measured.
   **Proposal (pre-data revision, not applied):** either (a) run each mutant over the full battery
   and require `set(failed legs) == set(pins)`, with forcing control = a mutant patched to break a
   second leg (e.g. m8 + a GZIP-breaking patch) which must then FAIL MUT; or (b) reword the claim
   sentence to "each fails its pinned leg" (the docstring's own weaker wording, `accept-o.py:85-88`).
   I did not edit the counter or `claims.json` — both are outside this seat's assignment.
2. **LOW — receipt header convention.** The frozen counter emits no measured-revision/sha256 header
   of its own; the header in `final-measures-o.txt` was prepended by this seat using the r61
   convention (`reports/round-61/telemetry/final-measures.txt:1-2`). It names
   `b7d22703dfb6…` (jj working copy @, parent `097c21d0…` = declaration commit), the counter sha256
   `c27a9fef…`, and the tool sha256 `c0f10a84…`. A future counter revision could emit its own
   header so the receipt is self-binding.
3. **LOW — the round-63 receipt cited by the counter docstring is not on disk.** The rev1/rev2
   revision history in `accept-o.py:95-108` cites
   `reports/round-64/telemetry/final-measures-o.txt` with counter sha `bb0c74a4…` as the forcing
   receipt for those revisions; the file on disk was a truncated 22-leg partial with no header, no
   MUT section, no verdict and no `exit=` line (sha256 `aef3faf6…`, preserved byte-identically in
   scratch). The cited `bb0c74a4…` measurement is therefore unverifiable from the lane. This seat's
   receipt replaces that file with the rev3 full run; the rev1/rev2 forcing receipt is not
   reconstructible and should be recorded as missing (it is also named as FIXTURE-O1 by
   RevengerCounter).
4. **LOW — SCORECARD prose vs freeze receipt on the tool hash** (see §2).
5. **INFO — `dry-run-o.txt` (397 B, 7 legs) and `dry-run-o-baseline-copy.txt` (397 B) are also
   truncated attempt-1 artifacts**; they are superseded by the three receipts installed here and are
   left untouched (they are attempt-1 evidence, not this seat's).

## 8. Risks and blockers

* **None blocking.** The claim's frozen predicate is met and evidenced: 23/23 legs PASS,
  `ACCEPT-O-64: PASS`, `exit=0`, tool bytes unchanged, ten mutants named and killed.
* **Residual (inherited, review-only per the counter docstring):** live behaviour on registry rows,
  DNS-rebind TOCTOU, and IDNA/IPv6 authority canonicalisation remain unpinned; the "same port,
  different host" hop stays fail-closed but unpinned. No live URL was fetched by this seat — every
  fixture is a local server on 127.0.0.1, and the tool was never pointed at a real registry row.
* **Concurrency note:** the receipts were produced against the working tree while other wave-1 seats
  were editing `LOG.md`/`SCORECARD.md`/corpus files. Nothing this seat's counter reads (the tool
  bytes, the counter bytes) changed during the run — verified by sha256 before and after
  (`c0f10a84…` and `c27a9fef…` respectively, re-hashed after the run finished).
* **Tools:** none installed or upgraded (no pacman, no uv/npx/binary fetch) — the work needed only
  the interpreter and coreutils already present.
* **Ownership note:** `reports/round-64/mutants/*.py` are *mutant fixtures*, byte-patched copies of
  `tools/reopen-row.py`. They are inert under the corpus sweeps (`accept-c.py` scans
  `corpus/knowledge` only) but a reviewer scanning `reports/**.py` should know they are deliberately
  defective copies, not lane tools.
