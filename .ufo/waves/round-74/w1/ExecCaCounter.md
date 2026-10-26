# ExecCaCounter — claim-Ca counter for round 74 (freeze-pinned, 11 legs)

Seat `ExecCaCounter-2`, 2026-10-25. Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
base `f7104cbce186bc2e1522abf0cfd619cc834628bb`. Leaf seat: no delegation, no background jobs, no
`task` spawns. Writes: this report and
`.ufo/waves/round-74/counters/accept-ca.py` only (nothing under `reports/round-74/`, no fleet-repo
write, no lane git/jj state or index change; every git call was read-only `show`/`clone`/
`rev-parse`/`cat-file`/`merge-base`/`diff`, plus throwaway fixture repos under `/tmp/ExecCaCounter/`).

Deliverable: `.ufo/waves/round-74/counters/accept-ca.py` — 2142 lines, `sha256
8128281b9c06bcd7f3c46723c4304997ca50356ec38f8def68b7b83a325c4105`, executable. Adapted from
`reports/round-73/accept-ca.py` (r3, sha `222d4dd6…`) and rewritten for the round-74 predicate set.

## 1. What it implements

CLI (exactly the item's contract, no gate-weakening flags — `--min-pairs` is gone on purpose, H5):

```
python3 -B .ufo/waves/round-74/counters/accept-ca.py --root <lane> \
    --lands <40hex> --freeze <40hex> --fleet-root <fleet> [--main main]
python3 -B .ufo/waves/round-74/counters/accept-ca.py --selftest
```

Exit 0 = eleven legs pass; 1 = a leg fails; 2 = input error (bad `--lands`/`--freeze`, claims or
base unresolvable at `--freeze`, clone failure, selftest failure). Receipt header lines are the
QUALITY 17/19 grammar of `tools/check-receipt-seq.py` (`# counter sha256 (self)`, `# stamped
revision`, `# evaluated revision`, `# measured revision (lane main)`, `# tree`), then a
`PAIR …` line per pair and `LEG PASS|FAIL <name>` per leg, ending `ACCEPT-CA-74: PASS legs=11/11`.

The eleven frozen legs are implemented one-to-one (names taken from
`reports/round-74/claims.json` claim `Ca`): LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY,
NOSTUB, SEPARABLE, TRACKED, RECEIPTS, FROZENCFG, STAMP. Two evaluation arms run in real clones:
`base` (from the frozen claims `base`) and `lands`; every `observe_cmd` and every re-derivation
command runs with `cwd` inside the relevant clone.

### Hardening map (round-73 survivors → what the code does)

| id | round-73 survivor | implementation here |
|---|---|---|
| H1 | config read from the graded tree (r2/r3 bug class; CritFrozenCfg) | `load_frozen()` reads `claims.json` **and** `ledger.json` with `git show <freeze>:<path>` only; there is no worktree fallback at any path. `FROZENCFG` also requires `freeze != lands`, `merge-base --is-ancestor freeze lands` == 0, `base` an ancestor of `freeze`, and the lands blobs of both config files byte-identical to the frozen blobs (a post-freeze config edit is a leg FAIL while the frozen bytes still grade). |
| H2 | echo/constant-printer + interpreter + non-repo operands (MutLedgerCa M1a/M1b/M2a/M2b/M9, M8a dead pin; M3a) | `observe_problem()`: argv list only (a string is rejected by name), `argv[0]` ∈ `{git, grep, wc, sha256sum, ls}`, interpreters/`sed`/`awk`/`env`/`echo`/`printf`/`find`/`cat` refused, shell-composing metacharacters (`\| & ; < > \` $(` newline) refused, every path operand must resolve **inside the clone at the observed revision** (absolute paths and `../../` rejected), every 40-hex operand must be an object of that clone (dead pin = FAIL), read-only git subcommands only, `git -C/-c/--git-dir/--work-tree` refused. `rederive` is `shlex.split` and must pass the same guard. |
| H3 | pasted re-derivation commands never executed (MutLedgerCa M5) | ANNOTATE runs the pair's `rederive` (which NOSTUB requires the row to carry verbatim) inside the lands clone and requires the observed token in its stdout, boundary-matched. |
| H4 | SEPARABLE wider than the frozen sentence (CritAppendOnly F1) | exactly three byte sets are scanned — the ledger text at `<freeze>`, the ledger's own string fields (incl. `statement_after` path/parse), the correction rows that **lead** with a pair id, and Ca telemetry receipts (basename contains `ca`) — for `S<id> >=` the frozen floor and the frozen `worldbuilding-setting-practice*` family. The round-73 added-line scan is deliberately absent. |
| H5 | 10-pair floor | `min_pairs = max(10, frozen ">= N")`; no CLI override exists; LEDGER and BASEMISMATCH both enforce it (selftest `min-pairs`). |
| H6 | receipts asserted in prose only (MutLedgerCa landed-bytes finding) | RECEIPTS finds the two round-73 PASS receipts **by content** under `reports/round-74/telemetry/` at `<lands>` and checks the full header: `stamped == evaluated == measured == 2d1cd914…` (parsed from the frozen RECEIPTS leg) and `tree == git rev-parse 2d1cd914…^{tree}`. |

Additional round-73 survivors closed as a side effect: row↔pair matching by **leading id** only
(MutLandedCa M01/M02), REPAIR `statement_after` mandatory with **last-match** semantics plus
"base stated_text absent at lands" (M04/M11 shadow repair), `expected_after` cross-checked against
the re-read statement (M15), boundary-matched token containment (`0` is not found inside a 40-hex
hash, M8a/M8b), `stated_text` must sit **on** the stated line (M6b, now a LEDGER problem), empty
observed token = unobservable (fail closed), and `observed_at_base`, when the ledger records it,
must equal the counter's own base observation.

## 2. Frozen-constant derivation (verified on the real draft claims text)

`FROZENCFG` derives its constants from the frozen leg sentences, so the frozen wording *is* the
contract:

| constant | frozen source | derived value now |
|---|---|---|
| round / base | `round`, top-level `base` | `74` / `f7104cbce186bc2e1522abf0cfd619cc834628bb` |
| pair floor | LEDGER leg `">= N unique pairs"` | `10` |
| separable S-id floor | SEPARABLE leg `S881` | `881` |
| claim-C family | SEPARABLE leg `(worldbuilding-setting-practice*)` | `worldbuilding-setting-practice` |
| protected files | APPENDONLY leg `"zero removed lines in …"` | `LOG.md, SCORECARD.md, corpus/lessons/round-73.md, corpus/lessons/round-72.md` |
| round-73 lands revision | first 40-hex of the RECEIPTS leg | `2d1cd9140d3a6c42296d71e4f29587582a4a88c0` |
| ledger path | claim `Ca`.`ledger` | `reports/round-74/ledger.json` |
| leg set | claim `Ca`.`legs` | exactly the eleven names above |

Evidence (draft claims copied into a throwaway clone at `/tmp/ExecCaCounter/smoke`, committed as a
stand-in freeze `d5ea0b2f…`, then `load_frozen()` called directly):

```
round = 74
base = f7104cbce186bc2e1522abf0cfd619cc834628bb
ledger_rel = reports/round-74/ledger.json
min_pairs = 10
separable_min_id = 881
c_family = worldbuilding-setting-practice
protected = ['LOG.md', 'SCORECARD.md', 'corpus/lessons/round-73.md', 'corpus/lessons/round-72.md']
receipts_rev = 2d1cd9140d3a6c42296d71e4f29587582a4a88c0
leg_names = [LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY, NOSTUB, SEPARABLE, TRACKED, RECEIPTS, FROZENCFG, STAMP]
problems = []
```

If any of those sentences is reworded before freeze so that a constant no longer parses, FROZENCFG
(and the leg that needs the constant) fails closed — that is the intended behaviour, not a fallback.

## 3. Required ledger shape (the freeze must satisfy this)

Documented in the module docstring; restated because the ledger author is a different seat:

* top-level `round` (74), `claim` (`"Ca"`), `base` (== the frozen claims base), `fleet_pin`
  (40-hex), `fleet_report` (path; default `.ufo/reports/round-73/kotodama.md`), `must_track`,
  `pairs`.
* `must_track` entries must carry a **64-hex sha256 of the worktree-at-base bytes**, either
  `{"path": …, "sha256": …}` or bare paths plus a `must_track_sha256` map. A path with no
  recorded sha256 fails TRACKED closed (the frozen TRACKED leg requires the ledger to record it).
* every pair: `id`, `stated_at` (`path:line`; `stated_text` must sit **on that line**),
  `stated_text`, `stated_parse` or `stated_token` (needed for token-level annotation rows),
  `observe_cmd` (argv over the H2 allowlist), optional `parse` (with a capture group),
  `expected_after`, `disposition` ∈ {REPAIR, ANNOTATE}, `rederive` (argv-clean, must return the
  observed token).
* every REPAIR pair **must** carry `statement_after: {path, parse}` (capture group); it is read at
  `<lands>` with **last-match** semantics, must equal the observed token, must differ from the base
  stated token, and the base `stated_text` must be gone from that file.
* every pair must be red at the frozen base (stated token ≠ observed token); a green pair fails
  BASEMISMATCH. The ledger may record `observed_at_base`; if it does, it is cross-checked.
* observations are **lane-repository only** (cwd = lane clone, rev = base or lands). Fleet-repo
  observations cannot be expressed; the fleet report is read by the APPENDONLY leg alone.
* `find` and `cat` are **not** allowlisted (H2 wording: read-only git/grep/wc/sha256sum/ls-class
  only). A ledger pair using `find … | wc -l` fails LEDGER.

## 4. Verification actually exercised

1. `--selftest`: exit 0, `SELFTEST OK: 134 checks across 33 scenarios reported-fail=0` (every
   scenario asserts the **named** leg's verdict, plus its exit code; full transcript kept at
   `/tmp/ExecCaCounter/selftest.txt`, 134 assertions):

   `do-nothing, clean, stub-rows, no-rederive, fake-rederive, append-only-removal,
   protected-in-place, unnamed-in-place, guard-shell-string, guard-interpreter,
   guard-echo-printer, guard-out-of-clone, guard-dead-pin, min-pairs, config-edit-ledger,
   config-edit-claims, non-ancestor-freeze, repair-no-statement, shadow-repair, tracked-missing,
   tracked-changed, receipt-fail-line, receipt-wrong-rev, separable-sid, separable-family,
   fabricated-base-observation, green-pair, stated-line-mismatch, parse-miss, prose-row,
   expected-after-mismatch, worktree-only-ledger, cli-errors`

   The fixture is a real git repo (`D=$(mktemp -d)` per chain, `git -C <lane> rev-parse
   --show-toplevel` verified == the lane dir before the first commit, throwaway identity from
   `SELFTEST_ENV`): 11 pairs (10 ANNOTATE + 1 REPAIR), a protected-file set, a fleet repo with the
   pinned report, and receipts whose headers match the frozen round-73 revision. Clean landing is
   11/11; the do-nothing control (lands == freeze) is `FAIL` with `red=11 min=10`, REPAIR/ANNOTATE/
   NOSTUB/RECEIPTS/FROZENCFG red.
2. Real draft-claims parse (§2) and a real-bytes do-nothing run: in `/tmp/ExecCaCounter/smoke/lane`
   at the real base with the draft claims as stand-in freeze, the counter prints
   `ACCEPT-CA-74: FAIL legs=1/11` — SEPARABLE PASS over the real round-73 correction rows, LEDGER/
   TRACKED/RECEIPTS/APPENDONLY/FROZENCFG/STAMP failing for the reasons named (no committed ledger,
   freeze not an ancestor of base). Transcript: `/tmp/ExecCaCounter/real-base-do-nothing.txt`.
3. Receipt integration probe on the real round-73 receipt bytes (see §5): RECEIPTS
   `PASS found={'ACCEPT-C-73': 'reports/round-74/telemetry/receipt-c-73.txt',
   'ACCEPT-CA-73': 'reports/round-74/telemetry/receipt-ca-73.txt'} problems=[]`, SEPARABLE PASS
   with `scanned=['reports/round-74/telemetry/receipt-ca-73.txt']`.

Not exercised: a graded run over a real round-74 landing (no ledger and no landing exist yet), the
real fleet-pin comparison with a real `fleet_pin`, and any network fetch (none was needed).

## 5. Two integration facts the freeze/dry-run must honour (measured, not assumed)

**(a) The round-73 Ca PASS receipt needs `--main`, or STAMP is red.** `reports/round-73/accept-ca.py`
takes `measured` from `rev-parse main`, and a fresh clone's `main` is the lane tip
(`f7104cb…`), not `2d1cd914…`. Measured in `/tmp/ExecCaCounter/r73/lane` (clone, detached at
2d1cd914):

```
# measured revision (lane main): f7104cbce186bc2e1522abf0cfd619cc834628bb
LEG FAIL STAMP
ACCEPT-CA-73: FAIL legs=8/9        <- plain command, as the routed item words it

# with --main 2d1cd9140d3a6c42296d71e4f29587582a4a88c0
# stamped = # evaluated = # measured = 2d1cd9140d3a6c42296d71e4f29587582a4a88c0
# tree: 516ea6c7d9265ae58ebc21fded41f925ddc504b2
ACCEPT-CA-73: PASS legs=9/9
```

My RECEIPTS leg requires `stamped == evaluated == measured == 2d1cd914…` (the frozen leg's own
words), so the Ca-73 receipt **must** be produced with that flag; the plain command yields a FAIL
receipt and the leg goes red.

**(b) The round-73 C PASS receipt needs `--census-sh` in a clone.** `accept-c.py` derives
`--fleet-root`'s sibling `scripts/`; from a `/tmp` clone the census is not found and the receipt
reads `ACCEPT-C-73: FAIL legs=10/11` (`LEG FAIL CENSUS`). With `--census-sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`: `ACCEPT-C-73: PASS legs=11/11`, header
`stamped = evaluated = measured = 2d1cd914…`, `tree: 516ea6c7…` — which my RECEIPTS leg accepts
(probe in §4.3). Both receipts must be **committed at `<lands>`** under
`reports/round-74/telemetry/`; RECEIPTS locates them by content, so the filenames are free.

## 6. Risks and open edges (stated, not hidden)

1. **APPENDONLY's in-place clause is the literal frozen sentence and is strict.** "in-place edits
   permitted only in files a ledger REPAIR pair names" is implemented as: every base..lands file
   with removed lines that is not in the protected four must be named by a REPAIR pair
   (`stated_at` or `statement_after` path). Claim C's landing changes `corpus/SOURCES.md` (S877
   used-by, old→new in place), and likely `corpus/README.md` (footer), `corpus/QUALITY.md`,
   `SKILL.md`, `SHONEN.md`. Unless a Ca REPAIR pair names each such file, APPENDONLY fails — this
   is a **freeze-time decision**: either the ledger names them (a registry-line or footer pair does
   this naturally) or the frozen APPENDONLY wording is amended before freeze. I did not weaken the
   implementation to make a landing pass; the selftest proves the clause fires (`unnamed-in-place`).
2. **ANNOTATE row tokens are not column-aware** (MutLandedCa M03 residual): a row that carries both
   tokens in the wrong columns still passes ANNOTATE/NOSTUB. The frozen leg asks for "id + old
   token + new token + the re-derivation command"; H3 makes a swapped *command* fail, but a swapped
   *token pair* with a correct command is not caught. Fixing it would need a frozen row grammar.
3. **ANNOTATE truth can still be an author-appended line inside a non-protected file** (MutLedgerCa
   M3b class) — only REPAIR pairs get a statement re-read. The frozen ANNOTATE leg does not ask for
   one, and inventing it would be wider than the sentence.
4. **SEPARABLE's telemetry scan set is the r73 convention** (filenames containing `ca`). A combined
   Ca+C receipt whose filename lacks `ca` is read by RECEIPTS but not scanned by SEPARABLE.
5. **`FROZENCFG` fails if the frozen leg set is not exactly these eleven names** — a late addition
   or rename of a Ca leg is a hard FAIL, by design (label == leg == receipt name).
6. **STAMP requires `measured == lands`.** The graded invocation passes no `--main`, so `lands`
   must be the lane `main` tip (as in round 73); a lands commit off `main` is a STAMP FAIL by
   construction (round-73 harness note, kept).
7. The counter's own sha256 is only pinned inside its receipt (not in `claims.json`); the graded
   receipt must be produced from these frozen bytes
   (`8128281b9c06bcd7f3c46723c4304997ca50356ec38f8def68b7b83a325c4105`). Any later edit to this
   file invalidates that pin and must be recorded as a counter revision with a red-before.
8. A pair whose observation prints nothing or exits non-zero with empty stdout is unobservable →
   BASEMISMATCH fails closed; `grep -c` legitimately printing `0` with exit 1 remains observable
   (non-empty stdout), which is deliberate.

## 7. Tooling / hygiene

No tools installed, no upgrades, pacman untouched. Runtime: Python 3.14.8, git 2.56.0 (present).
No network access, no downloads, no live fetches, so no User-Agent record applies. All scratch
clones and the receipt transcripts live under `/tmp/ExecCaCounter/`. The lane's inherited round-73
wave-2 worktree state was not read for grading and not modified; `git status --porcelain` shows only
the pre-existing inherited entries plus the untracked `.ufo/waves/round-74/` and
`reports/round-74/` trees.

## Post-wave update (final claims, claim Ca, 11 legs)

The claims are FINAL. `.ufo/waves/round-74/counters/accept-ca.py` was rewritten in place against the
frozen Ca leg sentences (and F1-F19, `RevClaimsFidelity.md`, `CritCaVacuity.md`, `CritFrozenCfg.md`,
`ExecReceiptRerun73.md`). **This supersedes §6 item 7's counter pin**: the frozen bytes are now

- `.ufo/waves/round-74/counters/accept-ca.py`, 2707 lines, sha256
  `dd755893f72cb8e93b8c53577188ad3b868bd3367c76b0ab789e19227ca520ec`
  (installed later as `reports/round-74/accept-ca.py`; the STAMP leg re-hashes the running file, so
  the graded copy must be these bytes or the receipt must record a counter revision).

### What the final legs required beyond the wave-1 draft

| leg | change implemented |
|---|---|
| LEDGER | allowlist is now `{git, grep, wc, sha256sum, ls, cat, head, tail, cut}` (interpreters, `echo`/`printf`/`true`, and shell metacharacters refused); role-aware `git` guards (a `git grep`/`git diff` **pattern** is no longer mistaken for a path; `HEAD` and 40-hex revs are allowed, branch-shaped revs are refused as mutable; `:(exclude)`/glob pathspecs allowed); **absence-observation pair refused**; `stated_text` must sit on the `stated_at` line in the BASE tree; a `fleet:` stated side (grammar R5) resolves at its `stated_fleet` pin |
| BASEMISMATCH | unchanged in spirit: clone at base, **every** pair red, none unobservable, none a parse-miss, count >= floor |
| REPAIR | a REPAIR pair **may not pin a revision** (its truth must be observed in the clone at lands — CritCaVacuity X4) and **may not sit on a line claim C appends to** (a README totals/footer line) |
| ANNOTATE | a **count pair** (numeric `expected_after`) must pin the frozen base revision in its `observe_cmd`; rows must LEAD with the id; the re-derivation command is RE-RUN at lands and must print the observed token |
| APPENDONLY | **line-level**: the seven protected files (now including `reports/round-73/{claims,ledger}.json`) must show zero removed lines; every changed line elsewhere must be a REPAIR pair's `stated_at` line or an appended line; the fleet round-73 report at `fleet_pin` must hash to the ledger's recorded sha256, be unchanged at fleet HEAD, and hold no uncommitted bytes under the fleet root |
| NOSTUB | placeholder set is exactly `{TODO, TBD, FIXME, XXX, n/a, ?}` or `<...>` |
| SEPARABLE | read set exactly as worded (ledger at freeze + rows leading with a pair id + the Ca-named telemetry receipts/controls + every pair's `stated_at` line); frozen forbidden stated_at set `{corpus/SOURCES.md, corpus/knowledge/**, corpus/lessons/round-74.md, reports/round-74/evidence/**, .ufo/waves/round-74/assimilation/**}`; the round-73 added-line scan is gone |
| TRACKED | tracked at **freeze and lands** with **identical blob ids**, non-empty, sha256 equal to `must_track` (sha source: object entry, `must_track_sha256`, or `content_pins.sha256_expected_after`) |
| RECEIPTS | **re-executes** the round-73 counters: clone of `2d1cd914`, local `main` pinned to it, `accept-c-73 --census-sh <fleet>/scripts/sources-census.sh` and `accept-ca-73 --main <rev> --fleet-root <fleet>`, requiring exit 0, the exact lines `ACCEPT-C-73: PASS legs=11/11` / `ACCEPT-CA-73: PASS legs=9/9`, and the committed `reports/round-74/telemetry/accept-c-73-at-lands.txt` / `accept-ca-73-at-lands.txt` to carry that stdout with stamped==evaluated==measured==`2d1cd914…` and the round-73 counter sha256 values |
| FROZENCFG | `<freeze>` must be a **first-parent-chain** ancestor of lands; config read only via `git show <freeze>:…`; lands claims/ledger byte-identical to the freeze blobs |
| driver | `ACCEPT-CA-74: PASS legs=11/11` from the leg table length; **LEGCOUNT refusal (exit 2, prints FAIL)** when the frozen leg table is not the eleven names; **`--lands == frozen base` refusal**; `lands == freeze` grades (FROZENCFG green, NOTE'd) but a PASS for that shape is refused |

### Selftest (exercised, exit 0)

```
$ python3 -B .ufo/waves/round-74/counters/accept-ca.py --selftest
SELFTEST OK: 141 checks across 38 scenarios reported-fail=0: do-nothing, clean, lands-eq-base, legcount, stub-rows, no-rederive, annotate-other-token, append-only-removal, protected-in-place, unnamed-in-place, shell-string, interpreter, constant-printer, out-of-clone, dead-pin, absence-pair, min-pairs, config-edit-ledger, config-edit-claims, freeze-off-first-parent, repair-no-statement, shadow-repair, tracked-missing, tracked-blob-mismatch, typed-receipt, receipt-wrong-rev, receipt-missing, separable-sid, separable-family, fabricated-base-observation, green-pair, stated-line-mismatch, prose-row, expected-after-mismatch, repair-pinned-observation, worktree-only-ledger, stamp-measured, cli-errors
```

Every one of the eleven legs has a named failing mutant: LEDGER (shell-string, interpreter,
constant-printer, out-of-clone, dead-pin, absence-pair, min-pairs, stated-line-mismatch,
worktree-only-ledger), BASEMISMATCH (fabricated-base-observation, green-pair, min-pairs), REPAIR
(shadow-repair, expected-after-mismatch, repair-no-statement, repair-pinned-observation), ANNOTATE
(stub-rows, annotate-other-token, prose-row), APPENDONLY (append-only-removal, protected-in-place,
unnamed-in-place), NOSTUB (stub-rows, no-rederive, prose-row), SEPARABLE (separable-sid,
separable-family), TRACKED (tracked-missing, tracked-blob-mismatch), RECEIPTS (typed-receipt,
receipt-wrong-rev, receipt-missing), FROZENCFG (config-edit-ledger, config-edit-claims,
freeze-off-first-parent), STAMP (stamp-measured). Controls: `lands == freeze` FAILS with
REPAIR/ANNOTATE/RECEIPTS red and LEDGER/FROZENCFG green; `lands == base` is a refusal printing FAIL;
LEGCOUNT is a refusal.

### RECEIPTS exercised on the real round-73 lands (not a graded receipt)

In a throwaway clone at `2d1cd914…` with local `main` pinned to it:

```
accept-c-73  --root . --lands 2d1cd914… --census-sh <fleet>/scripts/sources-census.sh   exit 0
  ACCEPT-C-73: PASS legs=11/11   counter sha256 95aee881…  tree 516ea6c7d926…
accept-ca-73 --root . --lands 2d1cd914… --main 2d1cd914… --fleet-root <fleet>           exit 0
  ACCEPT-CA-73: PASS legs=9/9    counter sha256 222d4dd6…  tree 516ea6c7d926…
```

Two runs of each were compared: the raw stdout differs only in `/tmp` materialization paths, and after
the leg's normalization (`/tmp…` → `<TMP>`) both runs are **byte-identical** (C and Ca each). So the
committed receipts must be produced by exactly these commands and committed stdout-only; the leg
normalizes the volatile clone roots and nothing else.

### Smoke run against the real draft ledger (pre-freeze advice, not graded)

`freeze` synthesized in a `/tmp` clone at `f7104cb` carrying `reports/round-74/claims.json` (FINAL)
and `.ufo/waves/round-74/drafts/ledger-draft.json` as `reports/round-74/ledger.json`; lands = freeze.
Result `ACCEPT-CA-74: FAIL legs=3/11`, green APPENDONLY/FROZENCFG/STAMP, and the reds are the
pre-freeze ledger work the final claims already anticipate:

1. **LEDGER** — LC-04/LC-05/LC-13/LC-14 are absence pairs (base count 0, after-state 1): F3/F4 deletes
   them, and the counter refuses them by name. LC-11's pattern `gzip.decompress -> 23443 -> [0-9]+
   bytes` carries `>` and is refused as a shell metacharacter (rewrite the pattern, e.g. a character
   class, or match `23443` only).
2. **REPAIR** — LC-01, LC-09, LC-10 pin a revision (`f7104cb…`, `4b825dc…`): a REPAIR truth must be
   observed in the clone at lands, so these must either read the graded tree (`HEAD`/path) or become
   ANNOTATE pairs. Their after-states cannot turn green through a base-pinned observation.
3. **SEPARABLE** — LC-12's `stated_at` line (`reports/round-73/claims.json:11`) cites `S894`, which is
   `>= S881`: the pair must be dropped or the stated line changed (the draft's own `dropped_candidates`
   already reasons this way for S879's row).
4. **TRACKED** — with the six files taken from the *committed* base tree the recorded
   `content_pins.sha256_expected_after` does not match; the freeze commit must carry the late
   worktree bytes (then the pin matches by construction).
5. **RECEIPTS** — the two receipts do not exist yet; they must be committed at lands under the two
   paths the frozen leg names.

### Deviations / readings the closure must know

1. **`lands == freeze`:** the frozen sentence says "strict ancestor", but the control requires
   FROZENCFG green at `lands == freeze`. Implemented as: graded (no refusal), strictness not applied,
   NOTE printed, and the driver refuses an all-green PASS for that shape (so a freeze commit that
   pre-bakes the data still cannot pass).
2. **Receipt comparison is normalized on `/tmp` paths only** (see above). Without that, "verbatim"
   is unsatisfiable for a re-run; every other byte must match exactly.
3. **Absence semantics:** `git grep -c/-l` with no match and exit 1 yields the token `0` (grammar R1)
   so such a pair is diagnosable; the leg then refuses it as an absence pair. It is never scored green.
4. **Fleet stated side (`fleet:<path>:<line>` + `stated_fleet`)** is accepted and resolved at its pin
   (grammar R5), because the draft ledger's LC-03 uses it; the frozen text only says "in the BASE
   tree", so a closure that drops LC-03 can ignore this door.
5. **`must_track` sha sources** are ordered: object entry → `must_track_sha256[path]` →
   `content_pins[…].sha256_expected_after`. The frozen text says "the ledger's must_track values";
   the draft ledger carries paths plus `content_pins`, hence the fallback.
6. **ANNOTATE's count-pin rule** keys on a numeric `expected_after` (the only mechanical reading of
   "count pairs measure at the pinned base revision").
7. `--main` (default `main`) feeds STAMP's `measured` header; the graded invocation passes nothing, so
   `lands` must be the `main` tip at grading time (round-73 harness note, kept).

### Files touched in this update

- `.ufo/waves/round-74/counters/accept-ca.py` — rewritten legs, guards, selftest (sha above).
- this report (appended section).
No other path written; no git write, no index change, no commit, no fleet write; no install, no
network. `/tmp` scratch clones removed; `/tmp` was at 87% (18 G free) during the seat.

## Post-wave update 2 (three counter/claims mismatches from the real freeze run)

The real run at the committed freeze `de93d91cab5a4f19fbe20b948abca67b8e9c7650`
(`reports/round-74/telemetry/controls-ca.txt`) exposed three mismatches; all three are fixed in
`.ufo/waves/round-74/counters/accept-ca.py`, 2787 lines, sha256
`26dd04a4971e6dcee4bd7a021ef9f876a93a0ea2c2f27943ff60539c11c0fe53` (the freeze copy at `de93d91`
is the previous bytes `dd755893…`; re-freezing needs this blob).

| # | leg | change implemented | new wording covered |
|---|---|---|---|
| 1 | APPENDONLY | the six ledger `must_track` paths are **exempt** from the changed-lines rule (`must_track-exempt=6` printed in the detail); new files with no base blob are appended lines; nothing else changed | `…changed lines elsewhere are a subset of the stated_at lines of REPAIR pairs plus appended lines, except the six must_track paths (pinned by TRACKED)` |
| 2 | SEPARABLE | the id test is now **membership in the frozen claim-C row set** (`row_set` ids of claim C at `<freeze>`: S881, S882, S883, S884), never "every id >= S881"; campaign-namespace ids (S894/S909/S910 …) in a stated_at line are not lane rows. The family-path test and the forbidden stated_at set are unchanged | `no byte in that set cites S881, S882, S883 or S884 (the lane ids claim C adds) or names worldbuilding-setting-practice*` |
| 3 | BASEMISMATCH | the `observed_at_base` cross-check compares **only the leading whitespace-delimited token** of the recorded value (the rest is prose) with the freshly observed token | same leg, cross-check made robust to the normalized ledger |

Fallbacks, fail-closed: if claim C carries no `row_set`, the lane-id set is taken from the ids named
in the Ca SEPARABLE leg text; if neither yields an id the FROZENCFG/SEPARABLE legs refuse (no
"everything passes" default). The `must_track` exemption reads the same path/sha list TRACKED grades,
so a must_track file whose blob no longer matches its pin fails **TRACKED** while APPENDONLY still
exempts it — TRACKED is the gate, by construction.

### Selftest (exercised, exit 0)

```
$ python3 -B .ufo/waves/round-74/counters/accept-ca.py --selftest
SELFTEST OK: 174 checks across 41 scenarios reported-fail=0: do-nothing, clean, lands-eq-base, legcount, stub-rows, no-rederive, annotate-other-token, append-only-removal, protected-in-place, unnamed-in-place, shell-string, interpreter, constant-printer, out-of-clone, dead-pin, absence-pair, min-pairs, config-edit-ledger, config-edit-claims, freeze-off-first-parent, repair-no-statement, shadow-repair, tracked-missing, tracked-blob-mismatch, typed-receipt, receipt-wrong-rev, receipt-missing, separable-lane-row, separable-non-lane-id, basemismatch-leading-token, separable-sid, separable-family, fabricated-base-observation, green-pair, stated-line-mismatch, prose-row, expected-after-mismatch, repair-pinned-observation, worktree-only-ledger, stamp-measured, cli-errors
```

New mutants required by this follow-up, all exercised:

- **`tracked-blob-mismatch`** — a must_track file rewritten at lands: `TRACKED` FAIL **and**
  `APPENDONLY` PASS (the file is exempt; TRACKED is the gate), detail carries `must_track-exempt=`.
- **`separable-lane-row`** — a stated_at line reading `entries: 0 (S883)` (`IDS.md:1`): `SEPARABLE`
  FAIL with `cites S883 (a claim-C lane row)`.
- **`separable-non-lane-id`** — a stated_at line reading `entries: 0 (S909)` (`IDS.md:2`):
  `ACCEPT-CA-74: PASS legs=11/11` (S909 is not a lane row).
- **`basemismatch-leading-token`** — `observed_at_base = "1 (key02 present in keys.txt)"`:
  `ACCEPT-CA-74: PASS legs=11/11` (leading token only).

### Re-verified on real bytes at the committed freeze (not a graded receipt)

```
$ python3 -B .ufo/waves/round-74/counters/accept-ca.py --root . \
    --lands de93d91cab5a4f19fbe20b948abca67b8e9c7650 \
    --freeze de93d91cab5a4f19fbe20b948abca67b8e9c7650 \
    --fleet-root /home/vgpnk/Projects/shokunin --main de93d91cab5a4f19fbe20b948abca67b8e9c7650
LEG PASS LEDGER        pairs=13 min=10 source=freeze
LEG PASS BASEMISMATCH  red=13 min=10 ids=[LC-01, LC-02, LC-03, LC-06, LC-07, LC-08, LC-09, LC-11, LC-12, LC-15, LC-16, LC-17, LC-18]
LEG FAIL REPAIR        red=[LC-01(observation pinned to f7104cbce186…), LC-09(observation pinned to 4b825dc642cb…)]
LEG FAIL ANNOTATE      no '## Corrections — round 74' section; annotate-pairs=11
LEG FAIL NOSTUB        rederive/rows absent (same cause)
LEG PASS APPENDONLY    protected-removed=0 fleet-pin=dad39efd2798 blob-sha256=000bab3a3664 must_track-exempt=6
LEG PASS SEPARABLE     lane-ids=[S881, S882, S883, S884] problems=[]
LEG PASS TRACKED       paths=6 problems=[]
LEG PASS RECEIPTS      rev=2d1cd9140d3a receipts=[accept-c-73=50c60bb67f16, accept-ca-73=864c94192854]
LEG PASS FROZENCFG     freeze=de93d91cab5a first-parent-of-lands
LEG PASS STAMP         stamped=evaluated=measured=de93d91cab5a
ACCEPT-CA-74: FAIL legs=8/11        (exit 1)
```

That is exactly the do-nothing control shape the claim demands (REPAIR/ANNOTATE red, config legs
green), and it confirms the three fixes on the frozen ledger bytes: APPENDONLY, SEPARABLE and
BASEMISMATCH now pass, and **RECEIPTS passes at the committed freeze** — the two committed receipts
match the re-executed round-73 stdout (only `/tmp` clone paths normalized).

One pre-landing item is visible on these bytes and is not one of the three: **LC-01 and LC-09 still
pin a revision** (`f7104cb…`, `4b825dc…`) while being REPAIR pairs. They are red at freeze (correct
for the control) and will stay red at the lands commit for the same reason, because the frozen REPAIR
sentence observes the truth "in a clone at `<lands>`". Fix at freeze by de-pinning their
`observe_cmd` (read `HEAD`/the graded path) or reclassifying them as ANNOTATE; the counter's message
names the pin so the choice is visible in the receipt.
