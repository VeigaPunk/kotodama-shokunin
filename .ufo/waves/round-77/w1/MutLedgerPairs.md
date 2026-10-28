# MutLedgerPairs — ledger-pair mutation attacks (round-77 W1)

Seat: MutLedgerPairs (leaf). Scope: attack the DRAFT Ca ledger candidates
(`.ufo/waves/round-77/w1/stage/ScoutLedger{A,B,C}/pairs.json`) with five
mutations per pair family and report which the LEDGER leg catches.
Lane base: `211f9526800906e0c585d878d265c37e5e090c15` (read-only).

## 0. Detector identity and method

- Detector = the LEDGER leg of round-76's counter, the schema parent the draft
  names ("Schema inherits round 76's"): copied unmodified into scratch.
  - `sha256sum $S/detector/accept-ca-r76.py /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-76/accept-ca.py`
    → `c1fc755e926f8d25e622469ec018bc9ad6c22b2f99ba83447fa95baab4a9695b` (both, byte-identical copy).
- The detector's own `leg_ledger()` runs on pristine, mutated and restored
  BYTES; the lane bytes are only read. Base observations resolve inside a
  throwaway clone of the lane materialized at base by the counter's own
  `materialize()` (asserted `rev-parse --show-toplevel` == clone dir, head == base).
- cfg fields normally parsed from the frozen claims text were supplied from
  CLAIMS-DRAFT's frozen sets: `annotate_append = [LOG.md, SCORECARD.md,
  corpus/lessons/round-75.md, corpus/lessons/round-76.md]`,
  `repair_mutable = [corpus/README.md, SKILL.md, SHONEN.md]`, `base = 211f952…`,
  `CTX["fleet_root"] = /home/vgpnk/Projects/shokunin` (mirrors main_check).
  `min_pairs` was scoped to the pairs under test so the pristine baseline is
  judgeable (the frozen floor ≥10 applies to the whole ledger and is orthogonal
  to the per-pair mutations).
- Driver: `$S/mutate_driver.py` (receipt copy:
  `.ufo/waves/round-77/w1/stage/MutLedgerPairs/mutate_driver.py`).
  Invoking command: `python3 /fast/scratch/hyaku/kotodama-r77/MutLedgerPairs/mutate_driver.py`
  (full raw transcript: `stage/MutLedgerPairs/transcript.jsonl`, 1 JSON record per run).
- Verdict rule (delta method): a mutation is CAUGHT iff its run adds a problem
  string that the same source's pristine run does not contain; restoration =
  pristine re-run after the campaign reproduces the baseline exactly.

Inputs (pre-campaign hashes):
```
sha256sum stage/ScoutLedgerA/pairs.json stage/ScoutLedgerB/pairs.json stage/ScoutLedgerC/pairs.json
2d9821279e6760bee3bce9721a80db810b9ebf64b81fb33e0ac022e6ce4443f3  ScoutLedgerA/pairs.json
2d71982cae54beabd66ac16f13c6cbcd1c40c05d9a4a6a397d4e2a19761ad4f7  ScoutLedgerB/pairs.json
aef1b67759c95532440c454792fbc5b7ad577c93be14093b3228cfebb19307f9  ScoutLedgerC/pairs.json
```
Families available: ScoutLedgerC = 5 REPAIR (LC77-C-01..05, corpus/README.md);
ScoutLedgerB = 4 ANNOTATE (L77-B01..04, corpus/lessons/round-75.md);
ScoutLedgerA = 1 pair (A-01) with NO disposition. Plus a schema-faithful
ANNOTATE FIXTURE pair (FIX-A-01, built from real base bytes — labeled FIXTURE,
not scout output) that gives clean PASS→FAIL transitions.

## 1. MUTATION TABLE (mutation → expected LEDGER verdict → observed → rationale)

| # | Mutation | Expected | Observed (raw problem line(s), per family) | Verdict / rationale |
|---|----------|----------|--------------------------------------------|---------------------|
| a | corrupt `stated_text` by one char (outside the `stated_parse` span) | LEDGER red (`stated_text not found … at base`) | ANNOTATE fixture: `FIX-A-01: stated_text not found in corpus/lessons/round-76.md at base` (PASS→FAIL, 0→1 problems). REPAIR synth: ×5 `LC77-C-0n: stated_text not found in corpus/README.md at base` (PASS→FAIL 0→5). ScoutB: ×4 `L77-B0n: stated_text not found in corpus/lessons/round-75.md at base`. ScoutC: +3 visible (detail cap 8; total problems 7→11 = 4 new pairs red). | KILLED. leg_ledger requires `norm(stated_text)` to appear in the normalized base body AND on the stated_at line (accept-ca.py:1569-1573). |
| b1 | point `stated_at` at a non-allowlisted path (`corpus/lessons/round-77.md:4`) | ANNOTATE: out-of-set red. REPAIR: no stated_at allowlist in grammar — red only via site check | ANNOTATE fixture: `FIX-A-01: ANNOTATE stated_at path corpus/lessons/round-77.md is not one of the frozen append-only files ['LOG.md', 'SCORECARD.md', 'corpus/lessons/round-75.md', 'corpus/lessons/round-76.md']` + `stated_at path … absent at base`. ScoutB: same two-line red ×4 (b1 delta +5 within cap). REPAIR synth: NO allowlist red; ×5 `stated_at path corpus/lessons/round-77.md absent at base`. A-01 (no disposition): delta +1 absent-at-base only (allowlist branch keys on disposition). | KILLED for ANNOTATE pairs with the exact routed-defect-r76-#3 red (allowlist enforced at accept-ca.py:1498-1504). Grammar note: a REPAIR pair's `stated_at` has NO allowlist — the REPAIR-side out-of-set guard binds `statement_after.path` (see b2). |
| b2 | REPAIR `statement_after.path` → `LOG.md` (out of the frozen mutable set) | LEDGER red (mutable-set) | REPAIR synth: ×5 `LC77-C-0n: REPAIR statement_after path LOG.md is not one of the frozen mutable files ['corpus/README.md', 'SKILL.md', 'SHONEN.md']` (PASS→FAIL 0→5). | KILLED (accept-ca.py:1489-1495). n/a for ANNOTATE (no statement_after object in the grammar). |
| c1 | `observe_cmd` executable → `python3 -c print(<observed>)` | LEDGER red (interpreter) | all families: `<id>: interpreter/constant-printer binary 'python3' is refused (H2)` (fixture 0→1; synth 0→5; ScoutB +4; ScoutC +4; A-01 +1). | KILLED (INTERPRETERS list, accept-ca.py:1230-1231). |
| c2 | `observe_cmd` executable → `echo <observed>` | LEDGER red (out-of-allowlist) | all families: `<id>: argv[0] 'echo' not in the observe allowlist ['git', 'grep', 'wc', 'sha256sum', 'ls', 'cat', 'head', 'tail', 'cut'] (the echo/printf/interpreter channels are closed)` (fixture 0→1; synth 0→5; ScoutB +4; ScoutC +4; A-01 +1). | KILLED (OBSERVE_ALLOW, accept-ca.py:1232-1234). |
| d | move the pinned base revision out of rev position (inserted after `--`, i.e. path-operand position) | LEDGER red (operand-role parse) | REPAIR synth/ScoutC: `git grep path operand '211f9526…' does not exist in the clone` (grep-shaped pairs) and `git diff path operand '211f9526…' does not exist in the clone` (diff-shaped pairs) — synth PASS→FAIL 0→5; ScoutB ×4; fixture ×1. ScoutLedgerA: delta +0 — A-01's argv already reds earlier at the `-C` guard (`git -C '<lane>' is refused`), which masks the operand parse. | KILLED wherever the argv reaches role parsing (`_git_grep_problem`/`_git_diff_problem`, accept-ca.py:1046-1122): a 40-hex in path position is checked with `os.path.exists(clone/<40hex>)` and reds. Survivor only behind an earlier, stronger red (A-01) — the LEDGER leg still reds that pair, so no false-green. |
| e | `expected_after := observed_at_base` ("no-mismatch") | LEDGER green — NOT caught | delta +0 on every source; LEDGER stays PASS on the clean SYNTH and FIXTURE baselines under (e). Equality pre-check: all 5 ScoutC pairs, all 4 ScoutB pairs and the fixture ALREADY have `expected_after == observed_at_base` (`family … pristine expected_after==observed_at_base: […True]`); only A-01 differs (`3c2893bf…` vs `cb4f6c6a…`) and still adds no problem. Counterfactual `expected_after := "999"` also +0 (LEDGER PASS on clean baselines). | SURVIVES — coverage finding. leg_ledger only requires `expected_after` to be a non-empty string (accept-ca.py:1485-1487). `expected_after == observed_at_base` is the WELL-FORMED state for base-pinned observations (that is why the ANNOTATE count-pair rule forces the base pin, accept-ca.py:1806-1810), so there is no "no-mismatch red" to trigger. The real expected_after guards live downstream: REPAIR leg `expected_after=%r != statement=%r` (accept-ca.py:1757-1760; r76 selftest mutant "badexpected"), the count-pair base-pin (ANNOTATE leg), and the absence-pair guard in LEDGER itself (below). If the r77 counter wants a no-mismatch guard, it must be added — this mutant documents its absence. |

Absence-pair guard (the one expected_after-dependent check LEDGER does have,
accept-ca.py:1589-1596): exercised accidentally and correctly during harness
debugging — a count-shaped `git grep -c -E '^Base'` probe that reads 0 at base
(`git -C $S/work/base grep -c -E '^Base' 211f9526… -- corpus/lessons/round-76.md`;
empty stdout, `exit=1` — no line starts with "Base") combined with a positive
numeric `expected_after` produced `absence-observation pair (base count 0,
expected_after '999')`. The counter's exit-1→"0" mapping behaved correctly; the
probe pattern was my fixture bug and was fixed (pattern `^Base` → `Base`).

## 2. Pristine baseline findings — first attacks on the DRAFT candidates

Baseline problems are findings against the DRAFT pairs as staged (commands:
the driver run above; JSON-escaped evidence lines quoted verbatim).

1. ScoutLedgerA/pairs.json is INVALID JSON as staged —
   `json.loads: Invalid \escape: line 7 column 127 (char 457)` (bare `\(`
   inside the observe_cmd argv string; the `rederive`/`parse` fields escape
   correctly). The ledger build's `json.loads` would refuse the file.
   Fixed-for-parse copy (only the observe_cmd line's escapes doubled):
   `stage/MutLedgerPairs/ScoutLedgerA.parsecopy.json`.
2. ScoutLedgerA (after parse fix), 6 baseline problems:
   `round=None != frozen round 77`, `claim=None`,
   `ledger base=None != frozen base '211f9526…'` (bare array carries no frozen
   meta triple), `A-01: disposition=None`,
   `A-01: git -C '/home/vgpnk/Projects/shokunin/kotodama-shokunin' is refused
   (the counter fixes repo and cwd; only the --fleet-root may be named)`
   (observe_cmd names the LANE after `-C`; the guard admits only the fleet
   root), and `A-01: stated_text not found in SCORECARD.md at base`.
   Ground truth for the last one (the sentence IS on the stated line — one
   char short): base SCORECARD.md line 1559 reads
   `… still only ROWS and COLLCHECK red (`reports/round-76/telemetry/measures-c-final.txt`). No score delta.`
   (command: `git -C <lane> show 211f9526…:SCORECARD.md`, line 1559 segment) while the
   candidate's stated_text ends `…measures-c-final.txt).` — it drops the
   closing backtick before `)`. The pair's SEMANTIC mismatch is real at base
   (`git -C <lane> show 211f9526…:reports/round-76/telemetry/measures-c-final.txt`
   → `# measured revision (lane main): cb4f6c6a550b3233f3c12a266e72dee6f4bc126b`
   and `ACCEPT-C-76: FAIL legs=11/13`), so the defect is wiring, not discovery.
3. ScoutLedgerB: 3 baseline problems, all the missing frozen meta triple
   (`round=None`, `claim=None`, `base=None`) — the 4 ANNOTATE pairs themselves
   pass every per-pair structural check (stated_text found on the stated lines
   at base; argvs clean; allowlisted stated_at paths). Strong candidates once
   wrapped in the meta object.
4. ScoutLedgerC: meta carries round+claim but no `base` (`ledger base=None !=
   frozen base '211f9526…'`); all 5 REPAIR pairs lack the required
   `statement_after` object (`LC77-C-0n: REPAIR without a statement_after
   object (the frozen REPAIR sentence names it)` ×5); and LC77-C-05 has a
   one-char stated_text drift — candidate says
   `the \`## linguistics/ (30)\` heading…` while base README line 791 says
   `The \`## linguistics/ (30)\` heading…` (capital T), so
   `LC77-C-05: stated_text not found in corpus/README.md at base` — the
   mutation-(a) defect class present in a pristine candidate (exactly the
   L76-19 class the draft says the build-time check must catch; it does).
5. SYNTH-COMPLETE REPAIR variant (scout C pairs + meta base + statement_after
   from each pair's own stated_parse + C-05 stated_text replaced by the exact
   base line 791 — deltas documented in the driver header; receipt
   `stage/MutLedgerPairs/synth_complete.json`): LEDGER PASS with 0 problems —
   i.e. completing those three fields yields a structurally clean REPAIR
   family, and every (a)/(b1)/(b2)/(c1)/(c2)/(d) mutation then reds it 5/5.

## 3. Restoration evidence

```
stage ScoutLedgerA/pairs.json sha256 (pre):  2d9821279e6760bee3bce9721a80db810b9ebf64b81fb33e0ac022e6ce4443f3
stage ScoutLedgerA/pairs.json sha256 (post): 2d9821279e6760bee3bce9721a80db810b9ebf64b81fb33e0ac022e6ce4443f3
stage ScoutLedgerB/pairs.json sha256 (pre):  2d71982cae54beabd66ac16f13c6cbcd1c40c05d9a4a6a397d4e2a19761ad4f7
stage ScoutLedgerB/pairs.json sha256 (post): 2d71982cae54beabd66ac16f13c6cbcd1c40c05d9a4a6a397d4e2a19761ad4f7
stage ScoutLedgerC/pairs.json sha256 (pre):  aef1b67759c95532440c454792fbc5b7ad577c93be14093b3228cfebb19307f9
stage ScoutLedgerC/pairs.json sha256 (post): aef1b67759c95532440c454792fbc5b7ad577c93be14093b3228cfebb19307f9
baseline-pre == restored-post (ledger flag + problems): True
```
Mutated variants were never written to the stage tree; all runs consumed fresh
bytes copies in scratch. Lane repo untouched (clone + `git show` only).

## 4. Receipts, scope notes, unrun checks

- Receipts copied to `.ufo/waves/round-77/w1/stage/MutLedgerPairs/`:
  `transcript.jsonl` (one JSON record per run: source, family, mutation,
  bytes sha256, ledger flag, authoritative problem list), `mutate_driver.py`,
  `ScoutLedgerA.parsecopy.json`, `synth_complete.json`, `annotate_fixture.json`.
- Family coverage: REPAIR = ScoutLedgerC (+SYNTH); ANNOTATE = ScoutLedgerB +
  fixture; ScoutLedgerA's undispositioned pair graded unfiltered. b2 is n/a
  outside REPAIR by grammar.
- Unrun (reported as unrun): downstream legs (BASEMISMATCH, REPAIR, ANNOTATE,
  APPENDONLY, …) were not executed — wave 1 has no lands tree or lands
  SCORECARD to grade; their expected_after behavior above is cited from
  accept-ca.py lines, not run. No `git`/`jj` mutation anywhere in the lane; no
  pacman; no tool installs this seat (nothing to record).
- Scratch `/fast/scratch/hyaku/kotodama-r77/MutLedgerPairs/` deleted after
  receipt copy, per scratch discipline.
