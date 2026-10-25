# RevClaimsFidelity — round 72 frozen-claims attack (AXES.md §A + round prompt §9)

Seat: L1Kotodama72.RevClaimsFidelity (reviewer, leaf). Scope: only the two frozen claims in
`reports/round-72/claims.json` (frozen 2026-10-25), attacked against AXES.md §A
("Working the axes — a round is 1–3 claims") and the round prompt §9 claim-sizing rules.
No repo mutation; all reads are read-only. No tools installed. Evidence pointers below are
path:line or command outputs taken this review.

## 0. Facts established (evidence)

- Lane branch `main` tip is still the declared base `b60c7b1` (`git log main`); `reports/round-72/`
  and `.ufo/waves/round-72/` are **untracked** (`git status --porcelain`) — claims.json is not yet
  hash-pinned by any commit.
- Base facts verified from `git show b60c7b1:`: `corpus/QUALITY.md` has 0 lines `^20\. ` and 0 `^21\. `;
  `LOG.md` has no `round-72`; `corpus/knowledge/**` has 0 `*heritage-taxonomy*`; `corpus/SOURCES.md`
  has 797 S-rows, 0 S874, 0 S875; `reports/round-71/telemetry/measures-ca.txt` already contains an
  appended re-stamp receipt pairing `f706aacd` with `64da9e14` (lines 7–15) next to the original
  `1ce25fb9`@`64da9e14` header (lines 1–4); `.ufo/waves/round-71/assimilation/id-renumber-map.json`
  is the only id-map in the tree (no `corpus/id-renumber-map.json`) and has 0 occurrences of
  `65ff151`/`99e3d63`; fleet repo `/home/vgpnk/Projects/shokunin/.ufo/reports/round-71/kotodama.md`
  lines 57–58 still say "map S861→S992 recorded for adoption".
- W2 uncommitted set at base (git status + `git cat-file -e`): committed-but-modified = {Filler30.md,
  RevReceipts.md}; untracked = {CritTrends.md, Filler28.md, Filler36.md, RevCounterCa.md, RevEntry.md}.
  Already committed-and-clean: RevSeparability.md, CritGaming2.md, RevRows.md, RevCausality.md, Filler33.md.
- Counter state at review time: `.ufo/waves/round-72/counters/` contains only the **Ca draft**
  (`accept-ca.py`, mtime 2026-10-25 11:24); no `accept-c.py` draft exists. No do-nothing/red-before
  telemetry receipts exist for either claim (`reports/round-72/telemetry/` = baseline.txt, census-start.txt only).
- Assimilation receipts exist: `validate/census-validate-mirror.exit` ("exit=0"), `mirror-fidelity.txt`
  (mirror = lane + the two placeholder entries), `rows-shape-mirror.txt` (799 rows, NF=13, 0 malformed,
  0 escaped pipes), `collcheck-*` (collisions 0B), `mutations/VERDICT.md` (real intersection
  S859..S873 = 15 caught; S874/S875 ∉ reg-ids).

## 1. Verdict summary

Both claims are **not clean**. Do-nothing cannot reach either full target (good), but several
§9 checks fail or are unverifiable in the current declared/draft state: (a) the Ca draft counter,
as written, **cannot print PASS on any lands** (three blocker bugs), and one Ca leg is already true
at base; (b) universal clauses appear without full-set enumeration in both claims; (d) axes are
distinct and claims are causally separable (pass); (e) kill rules are falsifiable in form but two
kill-rule clauses have no enumerating command, the CASTAMP leg sentence contradicts its counter
condition, and claims.json is not yet committed (freeze not hash-pinned).

## 2. Violations (by severity)

### F1 — HIGH, (a)/(e): CASTAMP leg is already true at base, and the draft counter implements a different sentence
Claim text: `"CASTAMP: an appended receipt re-stamps measures-ca at 64da9e14 with its true counter sha f706aacd"`.
- **before==after for this leg**: base `measures-ca.txt` already contains exactly that appended receipt
  (lines 7–15: `# re-stamped round 71 (append-only): previous bytes preserved below.` + header pairing
  `f706aacd`@`64da9e14`). The claim's before-text ("pairs counter sha 1ce25fb9 with stamp 64da9e14
  where the counter is f706aacd") describes only the first embedded block; the correction the leg demands
  already exists in the committed bytes. A do-nothing control reaches this sub-target.
- The draft counter implements a **different predicate**: `"64da9e14" in receipt and "f706aacd" in receipt
  and re.search(r"1ce25fb9.{0,120}64da9e14", receipt, re.S) is None` (accept-ca.py:110-113). Verified on
  the base blob: the `1ce25fb9…64da9e14` pairing spans 84 chars, so the regex matches forever, and an
  "appended" receipt cannot make it absent. The condition can only pass by editing measures-ca.txt in
  place (a rewrite the kill rule does not forbid but the leg wording and claim title do). Claim sentence ≠
  counter condition — exactly the §9 freeze violation ("the same condition in the counter's code").

### F2 — HIGH, (a): draft counter MAPCORR reads a non-existent path
Claim leg: `"MAPCORR: old->new recorded for id-renumber-map.json (65ff151 S861->S992 superseded by 99e3d63 S874->S1005)"`.
Counter: `MAP = "corpus/id-renumber-map.json"` (accept-ca.py:24). Verified: the only id-map in the base
tree is `.ufo/waves/round-71/assimilation/id-renumber-map.json`; `corpus/id-renumber-map.json` exists
nowhere. `blob()` raises → the counter exits 2 (`COUNTER ERROR`) on every lands; the declared after-state
command `accept-ca.py --root . --lands <lands>` cannot print PASS as drafted.

### F3 — HIGH, (a): draft counter reads the fleet report from the lane repo
Claim leg REPORTCORR/REPORTLAST require the round-72 fleet report. Counter: `FLEET_REPORT =
".ufo/reports/round-72/kotodama.md"` read via `blob(root, lands, FLEET_REPORT)` (accept-ca.py:26,102,128) —
i.e. `git -C <lane> show lands:.ufo/reports/round-72/kotodama.md`. That path exists only in the fleet repo
(`/home/vgpnk/Projects/shokunin/.ufo/reports/round-72/kotodama.md`); the lane has no such file. `fleet_root`
is parsed but unused. These legs error on every run → counter cannot complete. Must read the fleet commit
via `git -C <fleet> show`.

### F4 — HIGH, (b): W2FILES enumerates a different seven than the statement
Claim before: `"five round-71 w2 seat files are uncommitted (2 modified, 5 untracked)"`; leg:
`"W2FILES: the seven round-71 w2 seat files are committed at <lands>"`. The before-text is internally
inconsistent: it says "five" but enumerates 2 modified + 5 untracked = 7. The observed base set is 7:
Filler30.md, RevReceipts.md (modified), CritTrends.md, Filler28.md, Filler36.md, RevCounterCa.md, RevEntry.md
(untracked). The draft counter's W2 tuple (accept-ca.py:12-20) = {RevReceipts, RevCounterCa, RevSeparability,
CritGaming2, RevRows, RevCausality, Filler33} — five of those (RevSeparability, CritGaming2, RevRows,
RevCausality, Filler33) are already committed and unmodified at base, while Filler30/CritTrends/Filler28/
Filler36/RevEntry are not enumerated. The command does not enumerate the claim's seven files → statement
wider/different than its measure (the round-52/53 claim-sizing class).

### F5 — MEDIUM, (b): "append-only" universality exceeds the APPENDONLY enumeration
Claim title: "Round-71 routed defects K71-1..K71-8 land as **append-only corrections**"; kill rule repeats
rewrite-lethality. The only enumeration is `"APPENDONLY: git diff -U0 b60c7b1..<lands> -- LOG.md
corpus/lessons/round-71.md corpus/QUALITY.md shows no removed (-) lines other than diff headers"` —
three paths. Not enumerated: `reports/round-71/telemetry/measures-ca.txt` (whose CASTAMP correction, per
the draft counter, must EDIT the header), and `id-renumber-map.json` (MAPCORR writes an old→new record in
place — a JSON edit, not an append). Universal "append-only" without full-set enumeration.

### F6 — MEDIUM, (b): QUAL21 statement contains "every Gate reject records its URL"; counter only tests the criterion line
Claim leg: `"QUAL21: corpus/QUALITY.md carries '^21\. ' (CDX canonical-slug probe before ruling 'no capture';
every Gate reject records its URL)"`. Draft counter: `leg("QUAL21", bool(re.search(r"^21\\. ", q, re.M)))`
(accept-ca.py:78) — no enumeration of rejects/URLs. The parenthetical universal clause has no command term.

### F7 — MEDIUM, (e): Ca kill-rule clause "fleet report round-71" byte-rewrite has no enumerating command
Kill rule: `"any K71 defect landed by rewriting a filed byte (fleet report round-71, LOG.md entries <=
round-71, lesson round-71 filed sections), or any leg false at <lands> -> the claim fails as declared"`.
APPENDONLY covers LOG/lesson/QUALITY only; REPORTCORR checks the round-**72** report's text, not round-71
report byte integrity. A clause with no command term (claim-sizing addendum: move to falsifier or cut).

### F8 — MEDIUM, (e)/(b): C kill-rule clause "any cited source was not opened this round (2026-10-25) by the lane" is not enumerable over committed bytes
Opening is an event; only the lesson Gate's self-reported dates/quotes reference it. A command can enumerate
Gate lines but not the fact of opening. Universal clause with no command term.

### F9 — MEDIUM, (c)/process: the §9 pre-freeze control receipts are absent at review time
§9: "Before freezing, build the cheapest control that skips the claimed work, score it with the frozen
counter, and commit that receipt". Round-72 telemetry holds only `baseline.txt` and `census-start.txt`; no
`controls-ca.txt`/`controls-c.txt`, no red-before receipt scored with the frozen counters; the C counter does
not exist yet. `mutations/` proves the COLLCHECK guard and `MutGateQuotes.md` the quote-length check — not
claim-level do-nothing controls.

### F10 — LOW, (e): claims.json is not committed (freeze not hash-pinned)
`reports/round-72/` is untracked; `main` is still at base. Frozen-in-principle by header date only; a
post-data edit to the untracked claims.json would be invisible to git. Commit claims.json + counters before
any data lands.

### F11 — LOW, (a): SCRATCHMIRROR leg names a receipt file that does not exist
Claim leg: `"SCRATCHMIRROR: the scratch-mirror validation receipt (.ufo/waves/round-72/assimilation/validate-receipt.txt) shows census validate --file exit 0 on the mirrored corpus BEFORE the registry append, with the two rows in it"`.
Verified: no `validate-receipt.txt` exists; the actual receipts are `validate/census-validate-mirror.exit`
("census validate --file … -> exit=0"), `census-validate-mirror.out`, and `mirror-fidelity.txt` (mirror =
lane + the two placeholder entries). If the C counter checks the named path, it fails on correct data —
same class as F2/F3. Align the leg to the real receipt paths (or ensure the counter globs the validate dir).

## 3. Clean checks

- **(d) axes**: Ca=calibration, C=coverage — distinct axes ✓. Kinds records vs assimilation-sourced ✓.
- **(d) causal separability**: disjoint mutable surfaces (Ca → LOG.md, lesson round-71, QUALITY.md,
  measures-ca.txt, id map, fleet report; C → knowledge entries, SOURCES registry rows, lesson round-72,
  assimilation receipts). Ca verifies without C landed and vice versa ✓.
- **(a) shape**: both after-states are one command (`accept-ca.py --root . --lands <lands>` /
  `accept-c.py --root . --lands <lands>`) printing a single PASS verdict with a leg count matching the leg
  lists (12/12, 10/10) — shape-compliant, but not executable as drafted (F2/F3/F4) and `<lands>` must be
  pinned by the final report.
- **(e) kill rules falsifiable**: yes, in form; and the leg names in ExecCaCounter/ExecCCounter wave
  prompts mirror the frozen claims (no silent narrowing seen between claims.json and spec.json).

## 4. Do-nothing reasoning (per claim)

**Claim Ca at lands==base** (no-op commit): QUAL20 fails (0 committed `^20\. `), W2FILES fails (RevCounterCa
untracked), LOGCORR fails (no `round 72` in LOG), LESSONCORR fails (no `## Corrections (round 72)`),
QUAL21 fails, CAPOEIRA fails, REPORTLAST fails (no lane commits, no report). Vacuously true at base:
APPENDONLY (empty diff) and possibly NOHARM (census exit 0 with warnings). REPORTCORR/MAPCORR error (exit 2)
due to the draft bugs. → overall FAIL; do-nothing cannot reach the target. Sub-targets already reached by
do-nothing: CASTAMP (literal reading, F1), APPENDONLY, NOHARM.

**Claim C at lands==base**: ENTRIES fails (0 heritage files), ROWS fails (no S874/S875), GATE fails (no
lesson Gate), REJECTS fails (no refusals recorded), CITEDLINES cannot pass (no entries), SCRATCHMIRROR fails
(no receipt), COLLCHECK fails (no collcheck files). GROUND is true at base by design (gap sweep returns 0
owners — that is the claim's point); CENSUS may pass. → overall FAIL; do-nothing cannot reach the target.

## 5. Residual risk / verification gaps

- The C counter (`accept-c.py`) is not drafted at review time; its leg conditions cannot yet be diffed
  against the claim. Receipts so far are pre-fix: `validate/cited-lines-mirror.out` shows 2 MULTI-ID
  findings (lines 6, 21) — the entries must reach 0 findings at lands.
- Final `<lands>` hash, the committed fleet report, and census-end exit 0 must be re-verified after landing
  (out of this seat's scope).
- Rejection preconditions match the staged data (S870/S899/S900 in staged-ids; `reg-to-staged.txt` traces
  them to payload-absent register rows) — no contradiction found.

## 6. Required fixes before data lands

1. Rewrite the Ca counter: MAP → `.ufo/waves/round-71/assimilation/id-renumber-map.json`; fleet-report legs
   via `git -C <fleet-repo> show <fleet-commit>:<path>`; W2 tuple → exactly {Filler30, RevReceipts,
   CritTrends, Filler28, Filler36, RevCounterCa, RevEntry}; CASTAMP condition → match the literal appended-
   receipt sentence (or change the claim leg, never post-hoc).
2. Add command terms for F5/F6/F7/F8 clauses, or move them to the falsifier per the claim-sizing addendum.
3. Commit claims.json + counters, and run+commit do-nothing control receipts for both frozen counters
   (red-before), before any data lands.
