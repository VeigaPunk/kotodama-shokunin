# ExecAdaptCa — round 76, wave 1: ACCEPT-CA-76 counter + draft claim Ca

Seat: ExecAdaptCa (leaf executor; no delegation, no background work left running, no lane git/jj mutation).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `98c486bdb4650ba5b8e651d332910e8ee60ad121`.
Everything below is staged only: **nothing was written to `reports/round-76/`, `SCORECARD.md`, `LOG.md`,
`corpus/**`, or any tracked lane path** (`git -C … status --porcelain` shows only the pre-existing untracked
`.ufo/waves/round-76/` and `reports/round-76/` directories; the only new path is
`.ufo/waves/round-76/w1/stage/ExecAdaptCa/`).

## Verdict

**GREEN on the scoped build; freeze-ready with four named preconditions; one probe inconclusive and discarded.**

- `reports/round-76/accept-ca.py` has a complete draft: 3743 lines, sha256
  `3ef37ef84d82473b8e62659d40c9e9d587856e33f38e4db63b1ccd0380e768eb`
  (`sha256sum .ufo/waves/round-76/w1/stage/ExecAdaptCa/accept-ca.py`).
- `python3 -B accept-ca.py --selftest` → `SELFTEST: 170/170`, exit 0 — 170 checks across 43 scenarios
  (round-75 receipt was 154/154; the 16 new checks are the three defect controls plus the two new
  disposition-class mutants).
- The draft claim object for freeze is written and its leg table parses through the counter's own frozen-config
  loader with **zero problems**.

## Files

| path (lane-relative) | what |
|---|---|
| `.ufo/waves/round-76/w1/stage/ExecAdaptCa/accept-ca.py` | ACCEPT-CA-76 counter (adapted from `reports/round-75/accept-ca.py`) |
| `.ufo/waves/round-76/w1/stage/ExecAdaptCa/claim-Ca.json` | draft claim Ca object (title, before/after with the full command, ledger path, fixed_surfaces, kill_rule, do_nothing_control, counter, legs[12]); sha256 `45032afe65eefda087b0e81d4a6706f4a3add48200a241cc7989de6518020750` |
| `.ufo/waves/round-76/w1/stage/ExecAdaptCa/fixtures/r1exempt-{green,red,mixed}.json` | R1EXEMPT fixtures, copied byte-for-byte from `reports/round-75/fixtures/` (the counter finds `fixtures/` beside itself, else `.ufo/waves/round-76/counters/fixtures/`) |
| `.ufo/waves/round-76/w1/stage/ExecAdaptCa/selftest-ca.txt` | selftest run transcript (exit 0) |
| `.ufo/waves/round-76/w1/stage/ExecAdaptCa/r75-chain-rerun-work1.txt`, `…-work2.txt` | the round-75 parent instrument re-run at its own lands, twice under different `--work` roots (RECEIPTS premise + normalizer proof) |
| `.ufo/waves/round-76/w1/ExecAdaptCa.md` | this report |

No tool installs; no package manager calls (pacman untouched). Scratch lived only under
`/fast/scratch/hyaku/kotodama-r76/ExecAdaptCa/` and was deleted before this report was written
(`ls /fast/scratch/hyaku/kotodama-r76/` no longer lists it; the round root and other seats' dirs are intact).

## Defects closed while adapting (the three routed ones, plus three mechanical carry-overs)

1. **System-temp scratch roots removed (round-75 verifier spotcheck §7 item 2).**
   `scratch_dir()` is now `--work`, else `$HYAKU_SCRATCH`, else `$TMPDIR`, else `ScratchRefused`; there is no
   `tempfile.gettempdir()` fallback, no `R74_TMPDIR`, and children get `TMPDIR` only from the resolved root
   (`_child_env`).
   - `grep -nE '"/tmp|/tmp/' .ufo/waves/round-76/w1/stage/ExecAdaptCa/accept-ca.py` → **no output, exit 1**
     (run; pasted verbatim; the `grep-exit=1` was printed by the shell).
   - Refusal shape: `ACCEPT-CA-76: FAIL legs=0/12 (refused: no scratch root: pass --work, or set
     $HYAKU_SCRATCH (preferred) or $TMPDIR; this counter never invents the system temp dir)`, exit 2, and
     **no `LEG ` line is printed**. Selftest scenario `scratch-noroot` runs the counter as a subprocess with
     `HYAKU_SCRATCH`/`TMPDIR` removed and asserts exit 2, the refusal text, and `"LEG " not in stdout`.
   - After both real round-75 re-runs: `ls /tmp | grep -E '^r7[0-9]-ca-'` → `no-r7x-ca-leftovers`.
2. **`--combined` is an input requirement again.** `main_check` refuses (exit 2, no leg line) when
   `--combined` is absent, *before* any commit or leg work; the COMBINED leg keeps its defensive guard but can
   no longer be the thing that goes red for a missing flag. Selftest scenario `combined-required` asserts
   exit 2 and zero leg lines. The draft claim prints the complete command, including `--combined <C-lands>`,
   and the pinned-main requirement (`--main <Ca-lands>`, or a clone whose `main` is pinned to `<Ca-lands>` —
   STAMP compares `measured` to `lands`).
3. **APPENDONLY over-protection (round-74 closure R1) kept.** The rule-2 exemption is unchanged: SOURCES rows
   are compared semantically by row id, only status/recheck/used-by cells are exempt, and `R1EXEMPT` still
   proves it both ways plus the mixed case from the three fixtures. Selftest receipts: `r1-rule2-exempt` exit 0
   with APPENDONLY/R1EXEMPT PASS, `r1-teaches-red` and `r1-mixed-red` exit 1 with APPENDONLY FAIL
   (`changed outside the rule-2 cells`).
4. **Hardcoded constants removed.** Round-75 hardcoded the declared sweep-tool repair
   (`reports/round-28/readme/sweep.py` + its receipt names), a lesson-correction check for literal lane ids
   `S899`/`S900`, and a single claim-C family. All three are gone: the REPAIR leg now honours only the frozen
   `fixed_surfaces` (`required` / `line` / `sha256`) contract, the claim-C family is parsed as a **set** from
   the frozen SEPARABLE text, and every constant (round, base, paths, revs, receipt names, pass line, pair
   floor, class lists, forbidden paths) is read with `git show <freeze>:reports/round-76/claims.json` and
   `…/ledger.json` (QUALITY 25/26/28).
5. **Disposition bound to the frozen file classes.** A REPAIR pair whose `statement_after.path` is not in the
   frozen mutable list, and an ANNOTATE pair whose `stated_at` path is not in the frozen append-only list, now
   fail LEDGER — an annotation on a mutable file cannot be used to skip the repair it owes. Mutants:
   `repair-not-mutable` and `annotate-on-mutable` (both LEDGER FAIL, with the class named in the detail).
6. **Leak-proof output.** Every printed leg detail and NOTE is now redacted against the frozen claim-C lane
   ids and family names by construction (`leg()`/`note()` scrub through `CTX["cfg"]`), because the counter's own
   stdout becomes a committed telemetry receipt inside the SEPARABLE read set. The repo-wide leak assertions in
   the selftest still run (`do-nothing`, `clean`, `separable-family`).

## Evidence (command → raw result)

```
$ grep -nE '"/tmp|/tmp/' .ufo/waves/round-76/w1/stage/ExecAdaptCa/accept-ca.py ; echo "grep-exit=$?"
grep-exit=1                                   # no literal /tmp scratch root anywhere in the counter

$ HYAKU_SCRATCH=/fast/scratch/hyaku/kotodama-r76/ExecAdaptCa python3 -B accept-ca.py --selftest
selftest-exit=0
SELFTEST OK: 170 checks across 43 scenarios reported-fail=0: do-nothing, clean, lands-eq-base,
combined-required, scratch-noroot, legcount, legorder, stub-rows, no-rederive, annotate-other-token,
rederive-backtick, append-only-removal, protected-in-place, unnamed-in-place, r1-rule2-exempt,
r1-teaches-red, r1-mixed-red, shell-string, interpreter, constant-printer, out-of-clone, dead-pin,
absence-pair, min-pairs, config-edit-ledger, config-edit-claims, freeze-off-first-parent,
repair-no-statement, repair-not-mutable, annotate-on-mutable, shadow-repair, separable-lane-row,
separable-family, fabricated-base-observation, green-pair, stated-line-mismatch, prose-row,
expected-after-mismatch, worktree-only-ledger, stamp-measured, receipts-r75-fail,
combined-missing-entry, cli-errors
SELFTEST: 170/170
```
(full transcript: `stage/ExecAdaptCa/selftest-ca.txt`; the scenarios print one
`selftest: <name> -> exit=<n> <leg>=<state>` line each — `grep -c "^selftest: " selftest-ca.txt` = 40.)

**RECEIPTS premise, measured against the real lane** (the leg re-runs the round-75 instrument, so its pinned
revs had to be shown to reproduce their PASS line — they do):

```
$ git clone --no-checkout <lane> lane && git -C lane checkout -q -B main 012e8d3c8b92f47c734f735d58d118d574fe6a14
$ HYAKU_SCRATCH=…/work python3 -B reports/round-75/accept-ca.py --root . \
    --lands 012e8d3c8b92f47c734f735d58d118d574fe6a14 \
    --freeze 5d0167464309d8133991b30f7d7a7011a6a0fd14 \
    --fleet-root /home/vgpnk/Projects/shokunin \
    --combined 4f5e3b2535c2c06c51627dc2736c40183847cae1 --main main --work …/work
exit=0
LEG PASS LEDGER … LEG PASS RECEIPTS … LEG PASS COMBINED … LEG PASS FROZENCFG … LEG PASS STAMP
ACCEPT-CA-75: PASS legs=12/12
```
(full: `stage/ExecAdaptCa/r75-chain-rerun-work1.txt`.) The run was repeated with a second, differently named
`--work` root (`…-work2.txt`; also `ACCEPT-CA-75: PASS legs=12/12`, exit 0), and the counter's own receipt
normalizer was then applied to both transcripts:

```
$ python3 - <<'EOF'   # load accept-ca.py, normalize_receipt(text, work) both transcripts
identical-after-normalization: True
raw-identical: False
NORM-A: # clone: <TMP> head=012e8d3c8b92f47c734f735d58d118d574fe6a14
NORM-B: # clone: <TMP> head=012e8d3c8b92f47c734f735d58d118d574fe6a14
EOF
```
i.e. the committed receipt and a later re-run compare equal after normalizing volatile clone roots (our work
root, the round-75 `r75-ca-` roots, and any system-temp path either instrument prints), and are **not** equal
raw — so the comparison is doing real work.

**Draft claim parses through the counter's frozen-config loader with no problems.** A throwaway repo holding
`claims.json` = `{round:76, base, claims:[C(row_set S894..S898, entries), <claim-Ca.json>]}` plus a ledger was
committed, and `load_frozen()` was called on it:

```
problems: []
round = 76 ; min_pairs = 10
leg_names = ['LEDGER','BASEMISMATCH','REPAIR','ANNOTATE','APPENDONLY','R1EXEMPT','NOSTUB','SEPARABLE',
             'RECEIPTS','COMBINED','FROZENCFG','STAMP']
c_families = ['calendar-festival-systems', 'era-periodization-models']
protected = ['LOG.md','SCORECARD.md','corpus/lessons/round-75.md','corpus/QUALITY.md','SHONEN.md']
separable_forbidden = ['corpus/SOURCES.md','corpus/knowledge/**','reports/round-76/evidence/**',
                       '.ufo/waves/round-76/assimilation/**']
lane_row_ids = [894,895,896,897,898]
repair_mutable = ['SHONEN.md','SKILL.md','corpus/README.md']
annotate_append = ['LOG.md','SCORECARD.md','corpus/lessons/round-75.md','corpus/QUALITY.md']
receipt_paths = {'accept-ca-75': 'reports/round-76/telemetry/accept-ca-75-at-lands.txt'}
receipts_rev = 012e8d3c8b92f47c734f735d58d118d574fe6a14
receipts_freeze = 5d0167464309d8133991b30f7d7a7011a6a0fd14
receipts_combined = 4f5e3b2535c2c06c51627dc2736c40183847cae1
receipts_counter = reports/round-75/accept-ca.py
receipts_pass_line = ACCEPT-CA-75: PASS legs=12/12
r1_receipt_paths = {'green': '…/r1exempt-green.txt', 'red': '…/r1exempt-red.txt'}
combined_receipt_path = reports/round-76/telemetry/measures-ca-head.txt
```

## What the draft claim pins (for the freeze)

- Ledger `reports/round-76/ledger.json`, `round: 76`, `claim: "Ca"`, `base: 98c486b…`, `>= 10` unique pairs;
  **REPAIR** pairs must repair a statement in `SHONEN.md`, `SKILL.md` or `corpus/README.md` (frozen mutable
  list) and carry `statement_after`; **ANNOTATE** pairs must be filed against `LOG.md`, `SCORECARD.md`,
  `corpus/lessons/round-75.md` or `corpus/QUALITY.md` (frozen append-only list) and get a row leading with
  their id under `## Corrections — round 76` in `SCORECARD.md` carrying id + old token + new token + the
  re-derivation command.
- `fixed_surfaces: []` — round 76 declares no tool repair, so APPENDONLY only has to explain REPAIR stated_at
  lines and appended lines (plus the rule-2 SOURCES cells). The counter still supports
  `required` / `line` / `sha256` entries if the L1 adds one before the freeze.
- The 12 frozen legs, in order, as `legs[12]` in `claim-Ca.json`; the counter refuses any other table or order
  (`legcount`, `legorder` scenarios).

## Freeze preconditions (things this seat cannot install)

1. Install the counter at `reports/round-76/accept-ca.py` **and** copy `fixtures/` beside it (or to
   `.ufo/waves/round-76/counters/fixtures/`); R1EXEMPT fails without the three R1 fixtures, and the selftest's
   R1 scenarios likewise.
2. Write `reports/round-76/ledger.json` with the class-respecting pairs above, then freeze it with the claims.
   Changing the mutable/append-only lists is allowed only by editing the REPAIR/ANNOTATE leg text **before**
   the freeze — the counter parses the lists from those strings.
3. Produce the receipts at the landing: `reports/round-76/telemetry/accept-ca-75-at-lands.txt` (stdout of the
   round-75 re-run, stamped `012e8d3…`, counter sha256 = the round-75 counter's blob at that rev),
   `measures-ca-head.txt`, `r1exempt-green.txt` / `r1exempt-red.txt`, `controls-ca.txt`.
4. Measure with `--main <Ca-lands>` (or a clone whose `main` is pinned to `<Ca-lands>`), `--combined <C-lands>`
   and an explicit `--work`; a run without a scratch root now refuses, so any receipt-producing wrapper must
   pass one.

## Unrun checks and one inconclusive probe

- **Not run:** a graded ACCEPT-CA-76 run at a real freeze/lands (neither `reports/round-76/claims.json` nor
  `reports/round-76/ledger.json` exists yet at this writing — the L1 installs them at the freeze).
- **Not run:** generation of the real `accept-ca-75-at-lands.txt` / `measures-ca-head.txt` / `controls-ca.txt`
  receipts (they belong to the freeze and landing commits).
- **Not run:** the do-nothing controls at freeze/base on the real lane.
- **Inconclusive, discarded:** an ad-hoc probe that drove the counter over the selftest fixture with the real
  `legs[12]` text and a class-respecting 11-pair ledger returned exit 1, `5/12`
  (LEDGER/BASEMISMATCH/ANNOTATE/NOSTUB/APPENDONLY/RECEIPTS/COMBINED red, REPAIR/SEPARABLE/R1EXEMPT/FROZENCFG/
  STAMP green). The probe was stopped by the L1's finalize directive before its per-leg detail lines were
  captured, so **no cause is established** — it is reported as unproven, not as a counter result. Two
  candidates are visible in the probe's own construction (its pairs pointed at `LOG.md:1..10` while the
  probe's ten statement lines actually start at line 3, which alone explains the LEDGER failure, and it is not
  shown whether the replacement ledger took effect before the freeze commit the probe used). A re-run that
  keeps the per-leg detail lines would settle it; the authoritative evidence in this report is the selftest
  (fixture classes) and the frozen-config parse check, not this probe.

## Risks

- The counter is data-driven but strict: a ledger pair filed on a file outside the frozen class lists, or an
  ANNOTATE row that does not lead with its id, is LEDGER/ANNOTATE red by design. If the round's statements
  genuinely live in another mutable file, widen the REPAIR leg text before the freeze.
- The round-75 parent instrument the RECEIPTS leg re-runs keeps its own internal system-temp constant
  (`R74_TMPDIR`) for the round-74 child it re-runs. The round-76 counter contains no such constant and writes
  nothing there, but the *chain* still does for a few seconds; after four real re-runs no residue was found
  (`ls /tmp | grep -E '^r7[0-9]-ca-'` → none). Say this in the lesson rather than claiming "no system temp in
  the chain".
- `stage/…/selftest-ca.txt` and the two re-run transcripts cite `/fast/scratch/…` clone paths that are now
  deleted; they are records of a run, not citable paths.
