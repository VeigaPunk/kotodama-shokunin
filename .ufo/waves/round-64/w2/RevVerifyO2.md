# RevVerifyO2 — claim O counter re-verification (round 64, wave 2)

Seat: `kotodama-r64.RevVerifyO2` (reviewer; judged axes coverage / operability / calibration).
Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Scratch:
`/home/vgpnk/.cache/hyaku/kotodama-r64-w2/RevVerifyO2/`. No counter edit, no tool edit, no commit,
no index/jj mutation, no subagent dispatch, no tool installs. Lane writes: this report plus three
telemetry receipts (§8).

## Verdict

**Three byte streams were captured in this wave, and the label moved only on the last one.** The full
23-leg capture was run on all three:

| Counter bytes (`sha256sum reports/round-64/accept-o.py`) | Full 23-leg capture | Frozen predicate |
|---|---|---|
| `6d9c9354f0d7a9535aba4e781541b04626dd3a91791175a7d5f845c559615fa1` (rev4 label, mtime 23:54:09) | **22 PASS, 1 FAIL — `MUT`**, exit=1, 426 s | **FAIL** |
| `760ddd4d6d1c0ef1f2c4d0dbd6cd5ef286be1e3b8b2fc5cded2bd6258c08f5a7` (rev4 label, repaired in place at 00:08:52) | **23/23 PASS**, `MUT PASS bad=[] mutants=10`, exit=0, 426 s | **PASS** |
| `cdee063e39e1ecdb739519f76cd878e0108d0c5c3de8a6d8cd873830a5349dab` (**rev5 stamp**, mtime 00:18:26) | **23/23 PASS**, `MUT PASS bad=[] mutants=10`, exit=0, 426 s | **PASS** |

Receipts: `telemetry/final-measures-o-rev4.txt` (red rev4, sha256 `fed0ded2…`, explicitly labelled
falsification evidence), `telemetry/final-measures-o-rev4-760ddd4d.txt` (passing pre-stamp source,
sha256 `fd91552a…`), and `telemetry/final-measures-o-rev5.txt` (canonical rev5 stamp, sha256
`1cb15569…`). Every run pinned the counter sha before and after: bytes did not move during any
capture.

**Receipt-integrity warning:** claim O's declared land `telemetry/final-measures-o.txt` was left
holding truncated mid-run fragments relabelled "FINAL, rev5" by repeated streaming captures (three
samples: 822 B/7 legs, 2 251 B/22 legs, 838 B/7 legs; sha256 `947a0c5d…`, `7c120dfc…`, `0ef19df5…`)
— see HIGH-5. Its second capture did complete at 00:44:32 (3 498 B, 33 lines, sha256 `8e5c7ade…`,
23/23 legs PASS, `MUT PASS`, `ACCEPT-O-64: PASS`, `exit=0`, counter `cdee063e…`), so the path is
currently a valid complete receipt; the process defect (writing streaming stdout under a "complete"
header) remains and the L1 intends a verified re-run against the committed tip. The independent
complete receipts are `final-measures-o-rev5.txt` and `final-measures-o-rev4*.txt`.

The FAIL on `6d9c9354` had one cause: rev4's `m5` replacement was mis-indented, so the mutant did
not compile and the new `EDGE_SCHEMEREL` isolation arm could not pass (§4, HIGH-1). The repair landed
at 00:08:52 (`760ddd4d`): m5 rebuilt as `f04dc002…`, compiles, `EDGE_SCHEMEREL PASS` /
`EDGE_SLASHLESS FAIL`, `MUT PASS`; rev5 (`cdee063e`) stamps that history and passes identically.
**Against the bytes now on disk (`cdee063e`) the frozen predicate holds.** The claim sentence "each
fail exactly their pinned leg" remains unmeasured and is false for m1 and m2 over the EDGE set
(§4, HIGH-3).

The assignment's original checkpoints (all PASS, m5 killing only EDGE_SLASHLESS, PASS+exit=0) were
not met by the first rev4 bytes; they are met by both repaired streams except that "m5 killing only
EDGE_SLASHLESS" is still only verified for m1/m2-style exclusivity by an out-of-band sweep, not by
the counter (HIGH-3). The rev4 label covered two streams until rev5 documented both shas in its
revision history (HIGH-4).

## 1. Measured identity

```
$ /home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh state /home/vgpnk/Projects/shokunin/kotodama-shokunin
state branch=main local=097c21d0eba5023cfd38b767fb41d59409eef125 remote=097c21d0eba5023cfd38b767fb41d59409eef125 ahead=0 behind=0 head=detached tracked=8 untracked=35
# jj @ at first run start: 8325191b10edff408283f4325d11efd504a29f07 ; second run: 38efc473fee159645110c98fcb656860d7c4853d ; third (rev5) run: 9e9dc0d86f4b8d610f1101a3d9b19b08f7d2cd6c ; parent of all: 097c21d0
$ sha256sum tools/reopen-row.py
c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0  tools/reopen-row.py
$ git show ff30a205c8d23b35f1ac533740121a955a9fda96:tools/reopen-row.py | sha256sum
c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0  -
```

Runtime: host `python3` 3.14.8 (`sys.executable` for every tool/mutant subprocess, `run_tool`
`accept-o.py:409-420`); no proxy variables. **Tool byte-unchanged: yes.** Both counter captures were
made after `RevCounters` landed the respective bytes; `6d9c9354` was replaced during this seat's
session, which is why the first receipt is retained as falsification evidence rather than overwritten.

## 2. Capture A — `6d9c9354…` (rev4-label, first landing): FAIL

`reports/round-64/telemetry/final-measures-o-rev4.txt` (31 lines, sha256
`fed0ded28f1dc5a3ff3dd62c739cf3e17bf8593a902474a9302b6b0131158da3`), header: measured revision
`097c21d0…`, parent `097c21d0…`, jj @ `8325191b…`, counter sha `6d9c9354…` (unchanged pre/post),
tool sha `c0f10a84…`, command `python3 -B reports/round-64/accept-o.py --root .`, window
`02:59:50Z-03:06:56Z`, wall 426 s. Validation: 23 leg lines in `claims.json` order, 22 PASS, `FAIL:
['MUT']`, no SKIP, verdict `ACCEPT-O-64: FAIL`, last line `exit=1`.

```
MUT FAIL bad=["m5:EDGE_SCHEMEREL isolation=['EDGE_SCHEMEREL FAIL rows=[] tgt_hits=0 src_hits=0 tb=False']"] mutants=10
m5 kill evidence: m5->EDGE_SCHEMEREL FAIL rows=[] tgt_hits=0 src_hits=0 tb=False; EDGE_SLASHLESS FAIL rows=[] dir_hits=0 root_hits=0 exit=1
```

## 3. Capture B — `760ddd4d…` (repaired bytes, same label): PASS

`reports/round-64/telemetry/final-measures-o-rev4-760ddd4d.txt` (32 lines, sha256
`fd91552a1d4c83d298fe75a94f8d85dd278f9ae447b40fdc7547564750780f0c`), header names the repaired sha,
the same-frozen predicate, window `03:10:14Z-03:17:20Z`, wall 426 s, and the exactness caveat.
Validation: **23 leg lines, order match, 23 PASS, 0 FAIL/SKIP**, `MUT PASS bad=[] mutants=10`,
verdict `ACCEPT-O-64: PASS`, last line `exit=0`. m5's evidence on these bytes:
`m5->EDGE_SCHEMEREL PASS …; EDGE_SLASHLESS FAIL … exit=1`.

## 3b. Capture C — `cdee063e…` (rev5 stamp): PASS

`reports/round-64/telemetry/final-measures-o-rev5.txt` (32 lines, sha256
`1cb15569a610acfe753083bba5392558500134cd4efa6f2989f44cbe1d9a17a1`), header names revision 5, the
counter sha, tool sha, command, measured revision, window `03:20:12Z-03:27:18Z`, wall 426 s, and the
exactness caveat. Validation: **23 leg lines, order match, 23 PASS, 0 FAIL/SKIP**, `MUT PASS bad=[]
mutants=10`, verdict `ACCEPT-O-64: PASS`, last line `exit=0`. Counter sha unchanged before/after
(`cdee063e…`); the rev5 revision history documents rev4's red sha `6d9c9354…` and the pre-stamp
source `760ddd4d…`, and the m5 replacement literal plus the isolation arm are the same code as in
Capture B (rev5 adds the revision history/docstring text and renumbers lines). This is the canonical
passing receipt for the counter as stamped.

All 22 non-MUT leg detail lines are structurally identical between Captures A, B, C and the w1
rev3 receipt (`telemetry/final-measures-o.txt`) after normalising random S-ids, ephemeral ports and
fixture paths — same attempt counts, hit counts, and the deterministic wall values (`DEFAULT` 150 s /
bursts `[3,3,3]` / gaps `[60,60]`; `TIMEOUT` 6.0 s; `DRIP` 12.0 s / span 8.0 s). Only the ASCII
labelling of `MUT` differs across the four runs (rev3 PASS, rev4-first FAIL, repaired PASS, rev5
PASS).

## 4. Findings by severity

### HIGH-1 — rev4's first `m5` replacement did not compile; MUT (and the predicate) was unpassable — **fixed in `760ddd4d`, stamped in rev5 `cdee063e`**

`6d9c9354`'s `m5` replacement put a 12-space `if (` at `tools/reopen-row.py:604`, an 8-space block
level; the builder applies `tool_text.replace(needle, repl, 1)` verbatim (`:1086-1091`). Rebuilt
mutant sha256 `795b8d19…`, `py_compile` → `IndentationError: unexpected indent (line 605)`; of the
ten mutants, m5 was the only non-compiling one (all ten rebuilt and compiled here). Running the
landed counter against it printed both legs FAIL with `rows=[]` — the tool never imports — so the
`:1115-1121` requirement (`EDGE_SCHEMEREL PASS`) was unsatisfiable. Evidence:
`telemetry/m5-rev4.txt` (sha256 `4e019f1a…`). The repaired bytes replace the block with a
`slashless_relative` guard; rebuilt mutant `f04dc0029ed89fc35abd36564907ab2e47c1b44ca0baed4b7528327b5de3e710`
compiles and gives `EDGE_SCHEMEREL PASS` / `EDGE_SLASHLESS FAIL`, satisfying `pinned_fail` and the
isolation arm. My independent dedented variant (`804c9473…`) behaves identically, and w2 peers
(`RegFinalAudit`, `SupS719`, `SupS729`, `ResFixS737`, `SeparabilityRe`, `ReportFrag2`,
`OReceiptFresh`, `kumitate-r51.ResonantOpossum`) confirmed both the defect and the fix read-only.

### HIGH-2 — rev4's first docstring inverted the isolation contract — **fixed in `760ddd4d`, stamped in rev5**

`6d9c9354` said the paired run "requires the former to FAIL and the latter to PASS"
(`:117-119`), the reverse of the code (`EDGE_SCHEMEREL PASS` at `:1115-1121`, pinned
`EDGE_SLASHLESS FAIL`). The repaired bytes say "the former to PASS and the latter to FAIL", which
matches the code and the dispatch note. Recorded because prose/code drift of this class is what
lets a later reader "repair" the code to match wrong documentation.

### HIGH-3 — "each fail exactly their pinned leg" is not measured, and is false for m1 and m2 over the EDGE set

`accept-o.py:1093-1094` runs `run_legs = ["EDGE_SCHEMEREL","EDGE_SLASHLESS"] if name == "m5" else
pinned`. For the other nine mutants only the pinned legs execute, so `pinned_lines`/`pinned_fail`
(`:1099-1114`) can only ever see the pins; the rev3 docstring sentence "requires the observed
failure-leg set to equal its pins" (`:113-114`) remains true **by construction, not by measurement**,
and `claims.json`'s "ten byte-patched mutants each fail exactly their pinned leg" is stronger than
the mechanism.

Independent evidence on the landed bytes (`reports/round-64/telemetry/exactness-sweep-o.txt`, sha256
`429d568450e04e73933c12411822514cd7dbb9463512304358cfb1da8da5e089`; mutants rebuilt from the counter's
`MUTANTS` table, run against all seven EDGE legs):

```
m1 (pins [EDGE_SCHEMEREL])  FAILs EDGE_SCHEMEREL, EDGE_USERINFO, EDGE_HTTPS   <- 2 extra
m2 (pins [EDGE_USERINFO])   FAILs EDGE_USERINFO, EDGE_MALTARG                 <- 1 extra
```

(An independent sweep by `kumitate-r51.ResonantOpossum` over all ten mutants' EDGE/GEN/BOUND/DRIP
legs agrees: m1 and m2 exceed as above; m3, m5, m6, m7, m9, m10 exact over EDGE; m8 equals
{GEN,BOUND}; mread equals {DRIP}. CORE legs were not swept for the EDGE-pinned mutants, so collateral
CORE-leg failures remain unexcluded.) Repairs available: either run each mutant over the full battery and
require `failed == pins` (forcing control: m1/m2 must then FAIL MUT, and their pins widened or the
mutants narrowed as m5 was), or reword the claim to "each fails its pinned leg" and strike
`:113-114`. This is the one open claim-integrity item; it does **not** block the frozen predicate,
which only requires every leg to PASS.

### HIGH-4 — one revision label covered two byte streams; rev5 documents them, cite receipts by sha

The label "revision 4" was used for `6d9c9354` and again, unchanged, for `760ddd4d` after the
in-place repair. A receipt citing "rev4" alone is therefore unfalsifiable: only the counter sha
identifies the bytes. The rev5 stamp (`cdee063e`) resolves this for the record: its revision history
names rev4's sha `6d9c9354…`, records that its m5 block did not compile, and names the pre-stamp
source `760ddd4d…` plus the forcing receipts (this report, `m5-rev4.txt`, `CriticO`,
`ReviewerCounterO2`). Residual rule for the round: cite receipts by measured sha, not by label; the
three receipts here do so in both header and filename.

### HIGH-5 — the canonical O receipt path was left holding truncated mid-run snapshots labelled "FINAL, rev5"

`reports/round-64/telemetry/final-measures-o.txt` (claim O's declared land) was overwritten in the
worktree at 00:31:47 (-0300): 2 251 B, 30 lines, sha256
`7c120dfc050b3170eb680b39bfbed6849d7d0699d408b75010c8190f71a85e6e`; `git status` shows it as
` M` against the committed rev3 receipt (`95c9194:…` blob sha256 `009bbde3…`, 3 847 B, 29 lines).
Its own header reads `ACCEPT-O-64 evidence (FINAL, rev5)`, `measured revision: 95c9194…`,
`command: python3 -B reports/round-64/accept-o.py --root .`, `date: 2026-10-24T00:28:55-03:00`, then
`--- complete command output ---`. The output is **not complete**: it contains the 22 non-MUT legs
(`TOOL`…`DRIP`, all PASS) and stops at `DRIP`'s line; **no `MUT` line, no `ACCEPT-O-64:` verdict, no
`exit=` line**, and the file's last byte is `tb=False\n`. A full run takes 426 s and MUT alone ~255 s,
so the file is a snapshot taken ~3 minutes into a ~7-minute run and then labelled final; the one leg
missing is the leg that distinguishes rev5 from the red rev4 bytes. Preserved byte-identically in my
scratch as `final-measures-o-FINAL-rev5-truncated.txt`.

The same pattern repeated on further captures: at 00:28:56 a 7-leg / 822 B sample (sha256
`947a0c5d…`, peer-observed by `LessonFinal`), and at 00:37:26 the canonical path held 838 B /
15 lines,
sha256 `0ef19df5a69418dc98059c6c3f9ea93816dceedec2c2944461339a41733e5cff`, header
`ACCEPT-O-64 evidence (FINAL, rev5, second capture)`, 7 leg lines, no MUT/verdict/exit. The defect is
structural: the capture writes streaming stdout straight to the declared land under a header that
asserts `--- complete command output ---` from the first byte, so every reader and every `git add` in
the following ~7 minutes sees a "FINAL" receipt that is truncated; the one leg that runs longest
(`MUT`) is exactly the one missing. The L1 acknowledged and will not commit the worktree file as-is,
re-running and verifying 23 legs + MUT + verdict + exit before committing. Recommended process: run
to scratch, validate the 23-leg order plus `MUT` and the verdict/exit lines, then install atomically;
never label streaming output complete.

The two complete receipts survive under sibling names and are correct: the committed rev3 receipt is
preserved as `telemetry/final-measures-o-rev3.txt` (sha256 `009bbde3…`, 29 lines, 23 legs, PASS/exit
0), and the complete rev5 capture is `telemetry/final-measures-o-rev5.txt` (sha256 `1cb15569…`,
23/23, PASS/exit 0). The parent's second capture did eventually complete at 00:44:32: the canonical
path now holds 3 498 B / 33 lines, sha256
`8e5c7ade6c8fc232345ddc44fb994d645c86bbf48e8989ba87e29f8d5b8c46b9`, header `… (FINAL, rev5, second
capture)`, counter `cdee063e…`, 23 legs in claims order all PASS, `MUT PASS bad=[] mutants=10` with
`m5->EDGE_SCHEMEREL PASS …; EDGE_SLASHLESS FAIL …`, `ACCEPT-O-64: PASS`, last line `exit=0` — I
validated it after the write settled, and it is a valid complete receipt. The process defect stands
regardless: for ~7 minutes the declared land held a prefix under a "complete command output" header,
and the L1 intends a verified re-run against the committed tip before committing. (The C and Ca
"FINAL" receipts carry their verdict lines; O is the anomalous one.)

### MEDIUM-1 — `--only` still hides the 13 core legs and a 1-leg partial run prints green

Docstring: "legs not run print `<LEG> SKIP`". On `760ddd4d`:
`python3 -B reports/round-64/accept-o.py --root . --only DRIP` prints `TOOL SKIP` … `DRIP PASS` …
`MUT SKIP`, **0 of 13 core legs printed**, `ACCEPT-O-64: PASS`, exit=0. `run_core` (`:462`) still
gates the whole core block, and `legs` contains only the printed legs. Unknown selectors **are**
now rejected: `--only NOSUCHLEG` → `ACCEPT_O_INPUT_ERROR unknown --only leg(s): NOSUCHLEG`, exit 2
(`:444-449`) — the rev3 fail-open half is closed. The frozen command has no `--only`, so the frozen
predicate is unaffected.

### MEDIUM-2 — `run_core` executes the full core block for any core-named selector

`:462-465`. Any `--only` naming a core leg (e.g. GEN/BOUND) still runs the ~150 s DEFAULT fixture,
including inside every `m8` inner run; a peer `--only MUT` run costs ~255 s and the full capture
426 s for this reason. Docstring "`--only` runs just the named legs" is false for 13 of 23 legs.

### MEDIUM-3 — receipt/land drift: `reports/round-64/mutants/` still holds rev3 mutants

`reports/round-64/mutants/m5.py` is sha256 `83ecd7341afe979f…` — the rev3 broad patch, not the rev4
`795b8d19…` and not the repaired `f04dc002…`. The directory was populated from the w1 build and not
refreshed, so the inspectable kill set does not match the counter it is filed under. Older receipts
`final-measures-o.txt` / `mut-o.txt` / `edge-o.txt` / `control-o.txt` remain correctly labelled
rev3 (`c27a9fef…`) evidence and must not be cited as rev4 measurements.

### MEDIUM-4 — hermeticity exceptions inherited

`EDGE_USERINFO`'s same-authority control requires the OS resolver to fail the literal name
`u@127.0.0.1` (CPython 3.14.8 keeps userinfo in `Request.host`), and `run_tool` inherits the ambient
environment (proxy variables would be honoured; none here). Values hold on this host only.

### LOW-1 — receipt header not self-binding; LOW-2 — rev1/rev2 forcing receipt `bb0c74a4…` absent from disk; LOW-3 — `m9` kill evidence is a traceback (`tb=True`)

As in the w1 seats' findings; none affects the frozen predicate.

## 5. Repair validation (evidence, not applied by me)

* My dedented variant of the `6d9c9354` m5 replacement: mutant `804c9473…`, `py_compile` OK, paired
  run `EDGE_SCHEMEREL PASS` / `EDGE_SLASHLESS FAIL` (exit 1).
* The landed repaired m5 (`760ddd4d`): mutant `f04dc0029ed89fc35abd36564907ab2e47c1b44ca0baed4b7528327b5de3e710`,
  `py_compile` OK, paired run `EDGE_SCHEMEREL PASS rows=[('S2989','REFUSED',1)]` /
  `EDGE_SLASHLESS FAIL rows=[('S2731','UNREACHABLE',2)] dir_hits=0 root_hits=1`.
* End-to-end on the repaired bytes (`Capture B`): `MUT PASS bad=[] mutants=10`, `ACCEPT-O-64: PASS`,
  exit=0, 23/23 legs.

## 6. Residual risk and verification gaps

* **Exactness is unmeasured** (HIGH-3): m1/m2 demonstrably exceed their pins over the EDGE set;
  CORE-leg collateral failures are unexcluded for every mutant; the m5 isolation arm is a hand-paired
  special case, not a general audit.
* **Label provenance** (HIGH-4): cite counter sha, never "rev4"; a future edit under the same label
  would again make receipts ambiguous.
* **One canonical runtime** (Python 3.14.8); the userinfo-resolver and redirect semantics are
  version/environment-bound.
* **Timing legs are wall-clock** and were run under concurrent wave-2 load; values matched across
  all three receipts, so no anomaly, but they are not CPU-independent proofs.
* **No live-network behaviour** was exercised; every fixture binds loopback and the tool was never
  pointed at a real registry row (review-only per the counter docstring).
* The rev3 full run was killed mid-flight on parent routing; no fresh rev3 full receipt was produced
  (the w1 rev3 receipt was used for comparison, bytes unchanged).

## 7. Assigned quick-leg re-run

The originally assigned quick battery (`--only GEN,MUT,BOUND,EDGE_SCHEMEREL,EDGE_SLASHLESS,DRIP`)
was launched on rev3 and killed when the parent rerouted ("do not burn a full run on rev3") and then
rev4 landed; the full captures supersede it. The individual legs it names are all covered by
Captures A and B (`GEN`/`BOUND` PASS in both; `EDGE_SCHEMEREL`/`EDGE_SLASHLESS` PASS in both full
runs; `DRIP` PASS in both; `MUT` FAIL→PASS), so no comparison gap remains against the w1
`ExecCounterO` receipt (§3, all 22 non-MUT leg details identical).

## 8. Lane writes

| Path | Content | sha256 |
|---|---|---|
| `.ufo/waves/round-64/w2/RevVerifyO2.md` | this report | — |
| `reports/round-64/telemetry/final-measures-o-rev4.txt` | Capture A (`6d9c9354…`, FAIL) — falsification evidence | `fed0ded28f1dc5a3…` |
| `reports/round-64/telemetry/final-measures-o-rev4-760ddd4d.txt` | Capture B (repaired bytes, 23/23 PASS) | `fd91552a1d4c83d2…` |
| `reports/round-64/telemetry/final-measures-o-rev5.txt` | Capture C (rev5 stamp `cdee063e…`, 23/23 PASS — canonical) | `1cb15569a610acfe…` |
| `reports/round-64/telemetry/m5-rev4.txt` | m5 rebuild + compile + paired-leg evidence on `6d9c9354…` | `4e019f1ad484f13a…` |
| `reports/round-64/telemetry/exactness-sweep-o.txt` | m1/m2 collateral-failure sweep (exclusivity evidence) | `429d568450e04e73…` |

Scratch (not in lane): `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/RevVerifyO2/` —
`full-rev4-stdout.txt`, `full-rev4r-stdout.txt`, `rev4-pre.txt`, `rev4r-pre.txt`, `m5rev4/`,
`m5dedent/`, `m5r2/`, `sweep-m1/`, `sweep-m2/`, `only-nosuchleg.txt`, `rev4-only-drip.txt`,
plus the killed-rev3 partials.

## 9. Tools installed or updated

None. Host `python3` 3.14.8 and coreutils only; no pacman/uv/npx/binary fetch.
