# MutRevision — round-79 W1 mutable-revision and option-injection fixtures

Seat: `MutRevision` (mutation-tester, leaf). Item 22 of `.ufo/waves/round-79/w1/spec.json`:
"mutable HEAD/main/rev syntax and option injection fixtures".
Base: `44f76d456c1b326a71ffdb381590af825cbf11be` (lane HEAD unchanged before and after).
Target: the round-77 ledger-check detector, the candidate the round-79 O guard would replace or extend.
Scope: O only. Ca, the census receipts, and claim counters were not examined or changed.

## 1. Bottom line

1. **The current detector's `--ledger-check` accepts a wrong recorded `observed_at_base`.** The pristine round-77 probe (`probe-real-ledger.pristine.json`) records `observed_at_base: "1"` on all ten ANNOTATE pairs. A fresh `git grep -c -E '^#'` at base returns `149` for the identical `observe_cmd`. The pristine probe still passes `PASS pairs=11`, so the "real probe green" baseline is a false green. Fixture E01 (`"2"`, no injection) also passes. Nothing in `--ledger-check` compares the recorded value with a fresh observation.
2. **Argv[0] is checked by basename only.** A file named `git` anywhere on disk, given as an absolute path, is executed and passes (D01; the marker was written three times and the ledger passed).
3. **`--opt=value` forms of git global options slip past an exact-match list.** `--git-dir=<path>` is accepted and reads a different repository's bytes (B03 proves the bytes differ from the clone). It passes because the count coincides and no value compare exists (see 1).
4. **Mutable `HEAD` is accepted in revision position** (A01, B01). This reproduces the round-77 D07 survivor. `HEAD~1` is also accepted (A12, via `REV_NAMES`). With a `--git-dir=` redirect, `HEAD` resolves to the redirected repository's HEAD, so it is mutable in practice, not just by name.
5. **Most other mutable spellings are refused accidentally, not by policy.** `HEAD~0`, `HEAD^^`, `HEAD@{0}`, `HEAD:LOG.md`, `main~0`, `origin/main`, `@{u}`, `@~0` and a short sha are refused only because the fallthrough treats them as a path that does not exist in the clone (message: `does not exist in the clone`). Only `main` and `FETCH_HEAD` are refused by the mutable-ref rule.

## 2. Basis (committed bytes read; ordinary access only)

| item | source | pin |
|---|---|---|
| draft O | `.ufo/waves/round-79/CLAIMS-DRAFT.md` (O paragraph) | base `44f76d4` |
| detector | `.ufo/waves/round-77/w2/stage/ConnClaimsCounter/accept-ca.py` (identical to `w1/stage/ExecAdaptCa/accept-ca.py`) | sha256 `ac2bc93d02932464f9ee43222ffe1d06dd5bf1a0e68fd38bd94e10a991489b2e` |
| probe ledger | `.ufo/waves/round-77/w2/stage/MutCaLedger/probe-real-ledger.pristine.json` | sha256 `b7509d2b0980f8c5824c417a8359c8f7107d3de6236cf486ac058947915d0704` |
| prior seat | `.ufo/waves/round-77/w2/MutCaLedger.md` (D07 `HEAD` survivor, e1) | read |
| routed defects | `corpus/lessons/round-78.md:11` (R78-M1); `corpus/lessons/round-78-verifier-spotcheck.md` routed defects 2 and 3 | read |
| criteria | `corpus/QUALITY.md` 9, 11, 23, 25–28 | read |
| base commit | `211f9526800906e0c585d878d265c37e5e090c15` is an ancestor of `44f76d4` and exists in the lane | verified |

Detector line references (round-77 `accept-ca.py`):
- `_bin` basename rule 1062; `GIT_GLOBAL_OPTS` exact list 1068; `REV_NAMES` 1070
- `_git_rev_problem` 1073 (returns None for every non-40-hex token); `_mutable_ref` 1085 (regex `[A-Za-z][A-Za-z0-9_.-]*`, excludes `/`, `:`-prefix, `PATH_EXTS`)
- `_is_fleet_c` 1114; `_git_problem` 1124; global-option exact compare 1141; `_git_grep_problem` 1176 with `-`-token blanket skip 1184 (same skip at 1263 and 1334)
- `_retarget_argv` 1415 (only `argv[2]` rewritten; `_bin(argv) != "git"` at 1423; fleet exception 1425); `run_observe` 1432
- `pair_problems` 1614; `observed_at_base` read as string only 1712; ANNOTATE rederive-vs-observed compare 1756 (runtime tokens only, never vs `observed_at_base`)
- `leg_basemismatch` 1847 compares recorded vs observed at 1866–1868 (full counter only)
- `run_ledger_check` 3904 (sets `fleet_root = None`; grades only `pair_problems`)

## 3. Method and receipts

- Driver: `stage/MutRevision/driver.py`. It creates two fixture repos under scratch with `git rev-parse --show-toplevel` asserted equal to each fixture dir before any commit, a wrapper named `git`, and a marker script. It mutates pair D07 of the pristine probe in one run per mutant (groups A–E), runs the pinned detector `--ledger-check` against the lane (read-only, clone into `--work`), and writes raw outputs. Scratch was removed after copying.
- Run 1 and run 2 gave identical verdicts for the 25 shared mutants. Run 2 corrected the E02 control (its first version was labelled "true" but used the recorded value `1`).
- Receipts (stage): `raw/<id>.txt` (27 files: verdict, exit, marks, argv, detector output), `summary.tsv`, `lane-state.txt` (before and after, unchanged), `baseline-pristine.txt`, `run-driver.log`, `ledgers/*.json` (27 mutated ledgers, each differing from the pristine probe in one pair's fields as listed), `accept-ca.src-copy.py` (sha `ac2bc93d…`, matches the pin).
- Direct fixture probes (not via the detector) are recorded in section 6.

## 4. Mutant results (run 2; one pair, D07, changed as listed)

| id | change | verdict | exit | basis |
|---|---|---|---|---|
| baseline | pristine probe (`observed_at_base` "1") | ACCEPTED | 0 | `PASS pairs=11`; recorded 1 ≠ fresh 149 (F1) |
| A01 | rederive rev `211f…` → `HEAD` | ACCEPTED | 0 | `REV_NAMES` accepts (F4) — reproduces round-77 e1 survivor |
| A02 | `HEAD~0` | REFUSED | 1 | accidental: "path operand … does not exist in the clone" |
| A03 | `HEAD^^` | REFUSED | 1 | accidental (same message) |
| A04 | `HEAD@{0}` | REFUSED | 1 | accidental |
| A05 | `HEAD:LOG.md` | REFUSED | 1 | accidental |
| A06 | `main~0` | REFUSED | 1 | accidental |
| A07 | `origin/main` | REFUSED | 1 | accidental (slash makes it a non-mutable "path") |
| A08 | `FETCH_HEAD` (control) | REFUSED | 1 | policy: "mutable ref" |
| A09 | `main` (control, round-77 D06 form) | REFUSED | 1 | policy: "mutable ref" |
| A10 | `211f952` (7-hex, digit-first) | REFUSED | 1 | accidental |
| A11 | `@{u}` | REFUSED | 1 | accidental |
| A12 | `HEAD~1` | ACCEPTED | 0 | `REV_NAMES` (F4) |
| A13 | `@~0` | REFUSED | 1 | accidental |
| B01 | observe + rederive rev → `HEAD` | ACCEPTED | 0 | F4 |
| B02 | `--git-dir=<optrepo2>/.git` + `HEAD` (count 2) | ACCEPTED | 0 | F3 + F1: observed 2 vs recorded 1 is not compared |
| B03 | `--git-dir=<optrepo1>/.git` + `HEAD` (same count, other bytes) | ACCEPTED | 0 | F3: reads fixture bytes; count coincides |
| B04 | separated `--git-dir <path>` (control) | REFUSED | 1 | policy: "option '--git-dir' is refused" (1141) |
| B05 | separated `-c diff.external=<prog>` before `grep` (control) | REFUSED | 1 | policy: "option '-c' is refused" |
| B06 | attached `-ccore.quotepath=off` | REFUSED | 1 | runtime only: validator accepts; git exits 129 (F7) |
| B07 | attached `--namespace=x` + 40-hex base | ACCEPTED | 0 | validator gap; harmless for a 40-hex object lookup |
| C01 | `--textconv` after `grep` | ACCEPTED | 0 | `-` blanket skip (F6); valid option, not exploited |
| C02 | `--open-files-in-pager` (no value) | REFUSED | 1 | runtime only: git exits 128 (F7) |
| D01 | argv[0] = `<scratch>/…/git` wrapper (basename `git`) | ACCEPTED | 0 | marker `WRAPPER RAN` written 3× (F2) |
| D02 | argv[0] = `/usr/bin/git` (control) | ACCEPTED | 0 | basename rule |
| D03 | argv[0] = `/usr/bin/python3` (control) | REFUSED | 1 | policy: "interpreter … refused (H2)" |
| E01 | `observed_at_base` "2", no other change | ACCEPTED | 0 | F1: no compare |
| E02 | `observed_at_base` "149" (fresh value) | ACCEPTED | 0 | F1: the correct value passes too; compare absent in both directions |

Fresh base observations (read-only `git -C <lane> grep -c -E '^#' 211f… -- LOG.md`) show `211f9526…:LOG.md:149`. The same check for every ANNOTATE pair (D01–D10) gives 149 against the recorded `1`. D11 (REPAIR) records no `observed_at_base`.

## 5. Findings (ranked)

**F1 — HIGH — no recorded-vs-observed compare in `--ledger-check`; the pristine probe is a false green.**
Evidence: baseline and E01 (`"2"`) and E02 (`"149"`) all PASS; the ten ANNOTATE pairs record `1` against a fresh `149` (section 4). `pair_problems` reads `observed_at_base` as a string only (1712) and compares runtime tokens only for ANNOTATE rederive-vs-observe (1756). The recorded-vs-observed compare exists only in `leg_basemismatch` (1847–1868), which `--ledger-check` never runs. This matches R78-M1: the fix is not present in this candidate, so R78 routed defect 3 remains open.
Consequence for O: the draft's "rejects an observed_at_base differing from the actual observation" must be implemented in the ledger-check path itself; the pristine probe cannot serve as a green baseline (it fails that clause on its own bytes). [INFERENCE, not executed: the full `leg_basemismatch` would also flag these pairs, since it compares `rec` against `obs` at 1866–1868.]

**F2 — HIGH — argv[0] basename check admits any executable named `git`.**
Evidence: D01. `_bin` (1062) uses `os.path.basename(argv[0])`; `_retarget_argv` (1423) and `run_observe` (1432) execute `argv[0]` as given. The wrapper's marker shows three invocations in one check (the call sites were not separately identified); the ledger passed.
Consequence: any ledger that names an absolute path ending in `/git` runs arbitrary code during the check. The constant-printer channel the draft closes (J4 class) is reachable by the same route. [INFERENCE for constant printers: not run; D01 proves only the admission.]

**F3 — HIGH — attached `--opt=value` global options bypass the exact-match list; `--git-dir=` reads other repositories.**
Evidence: B03 (fixture `optrepo1`, HEAD count 1, other bytes). Direct check: `git -C <lane> --git-dir=<optrepo1>/.git grep -h -E '^#' HEAD -- LOG.md` prints `# Different heading`; the lane at base prints `# kotodama-shokunin — iteration log (append-only)`. The count (1) matches the recorded `1` and PASS follows. Separated `--git-dir <path>` (B04) and `-c` (B05) are refused. `GIT_GLOBAL_OPTS` (1068) compares exact tokens at 1141 only.
Consequence: observations can be redirected to an arbitrary repository; the count-based check cannot see it. `--namespace=x` (B07) is also accepted; it does not change a 40-hex lookup here.

**F4 — HIGH — mutable `HEAD` (and `HEAD~1`) accepted in revision position.**
Evidence: A01, A12, B01. `REV_NAMES` (1070) is accepted unconditionally by `_git_rev_problem` (1080). The lane's clone is detached at base, so the pinned-ness of `HEAD` holds only through the clone procedure (`materialize` asserts `HEAD == base`, per round-77 W2 `MutCaLedger.md` §2; not re-read here), not through the grammar. Under F3, `HEAD` names the redirected repository's tip, which moves. This is the round-77 e1 survivor, reproduced.
Recommendation: positive grammar in revision slots, `40-hex` or `HEAD` only (the W2 "narrow or extend" choice). Decide `HEAD~1` and `@` explicitly.

**F5 — MEDIUM — most other mutable spellings are refused accidentally.**
Evidence: A02–A07, A10, A11, A13 refuse only with `does not exist in the clone`. The mutable-ref regex (1085) excludes `/`, `:`, `~`, `@`, and digit-first names, so they fall through to a path test. A repository that happened to contain a file with that name would let it through (not tested).
Recommendation: refuse by positive grammar with its own message, so each refusal is policy-named and not a side effect of path existence.

**F6 — MEDIUM — grep option blanket skip.**
Evidence: `_git_grep_problem` (1184), and the same pattern at 1263 and 1334, skip every `-`-token without validation. C01 (`--textconv`) is accepted. Recommendation: an explicit grep-option allowlist (`-c -l -E -F -e -i -n -h -o`, plus any the counters need).

**F7 — LOW (runtime only, not policy) — attached `-c<name>=` and `--open-files-in-pager`.**
Evidence: B06 (git exit 129 on `-ccore.quotepath=off`) and C02 (git exit 128 on `--open-files-in-pager`). Direct check: `git -C <fixture> -cdiff.external=<prog> diff …` also exits 129 (git 2.56 requires `-c` as a separate token). A separated `-c diff.external=<prog> diff` *does* execute `<prog>` (marker `EXTDIFF RAN` written), so the exec channel exists; the validator closes it for the separated form (B05 refused). `git grep -O`/`--open-files-in-pager` did not execute in this build (exit 128, unresolvable revision). These are fail-closed by git, not by the validator; they must still be refused by policy.

**F8 — source-read, UNRUN — fleet `-C` operand is not retargeted when a fleet root is set.**
Evidence: `_is_fleet_c` (1114) and the exception at 1425 leave `-C <fleet-root>` un-rewritten. `_git_problem` (1124–1131) then sends `HEAD` (accepted, F4) to the fleet repository. `run_ledger_check` (3904) sets `fleet_root = None`, so `--ledger-check` never exercises this; the full LEDGER leg does. This would read a moving working tree and violate "grade committed bytes". Not run here: no full-counter invocation with `--fleet-root` was executed. Needs a fixture before O relies on it.

**F9 — unprobed clause.** The draft's "rejects `stated_token` equal to the actual observation" was not probed (no pair was built where the stated token is anchored to a computed observation). Left for the O seat.

## 6. Direct fixture probes (preserved in the report, not the detector)

- `git -C <optrepo1> grep -c -E '^#' -O<prog> …` and `--open-files-in-pager=<prog>`: rejected by git 2.56 as `unable to resolve revision` (exit 128). A bare `-O` is rejected the same way.
- `git -C <optrepo1> -cdiff.external=<marker> diff HEAD~1 HEAD -- LOG.md`: exit 129 (attached form is not valid git syntax).
- `git -C <optrepo1> -c diff.external=<marker> diff HEAD~1 HEAD -- LOG.md`: exit 0; `EXTDIFF RAN argv=…` written to the marker.
- `git -C <scratch> --git-dir=<optrepo2>/.git grep -c -E '^#' HEAD -- LOG.md`: exit 0, `HEAD:LOG.md:2` (fixture bytes; the lane's HEAD is not involved).
- `git -C <lane> grep -c -E '^#' 211f9526… -- LOG.md`: `…:LOG.md:149` (read-only).

Fixture root assertion: every fixture repo's `git rev-parse --show-toplevel` equalled its own directory before any commit; no commit or write touched the lane, the fleet root or `~/.local/bin`.

## 7. Expected red-before for the O guard (what must flip)

Must become REFUSED (current candidate ACCEPTS): baseline pristine (F1), E01, A01, A12, B01, B02, B03, B07, C01, D01. Must become REFUSED by policy, not by path accident: A02–A07, A10, A11, A13.
Must stay REFUSED (already): A08, A09, B04, B05, D03, and by runtime: B06, C02 (but add policy refusals too).
Must stay ACCEPTED (controls): E02 (`149`), D02 (absolute real `git`).

The pristine baseline cannot remain a green fixture under O. The O acceptance fixture must be a corrected probe (E02-style, recorded `149`), and the ten ANNOTATE pairs' recorded `1` is a defect of the round-77 probe that the round-79 lane must correct in its own records (not here).

## 8. Reproduction (driver; scratch recreated, stage receipts overwritten)

```
mkdir -p /fast/scratch/hyaku/kotodama-r79/MutRevision && cd /fast/scratch/hyaku/kotodama-r79/MutRevision
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-79/w1/stage/MutRevision/driver.py
```

Single mutant (after the driver has written `ledgers/`):
```
cd <scratch> && python3 -B <pinned accept-ca.py> --ledger-check <stage>/ledgers/D01.json --root /home/vgpnk/Projects/shokunin/kotodama-shokunin --base 211f9526800906e0c585d878d265c37e5e090c15 --work <scratch>/work/D01
```

## 9. Limits, tools, scratch

- Not run: the full counter (no freeze, lands, fleet root), the full `leg_basemismatch`, any O guard implementation, and any Ca/census check.
- No tool installs or upgrades. Used existing `git 2.56.0` and `python3 3.14.8`. No pacman, no uv, no host or service change. No `task`/delegation.
- No edits to shared files. Lane git unchanged (`git status --porcelain` = 2 lines before and after, pre-existing). No commits, no pushes. Fixture repos were initialized only under scratch with verified roots. Scratch `/fast/scratch/hyaku/kotodama-r79/MutRevision` removed after receipts were copied to stage.
- Preserved receipts: no existing file modified. New files only: `MutRevision.md` and `stage/MutRevision/` (driver, ledgers, raw, summary, lane-state, baseline, log, source copy).

Report: .ufo/waves/round-79/w1/MutRevision.md
