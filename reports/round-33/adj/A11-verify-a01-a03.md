- Seat: A11 | verifier | claim A | date 2026-10-19 | baseline 139e3b6

# A11 — independent re-run of the A01–A03 cited commands

**Assignment (targets.json A11):** "Independently re-run the cited commands in
A01-A03 fragments; same green or a filed defect with the differing output."

**Method.** Every command below was re-run by this seat from the lane root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, read-only (no write, no
revert, no git-mutating command, no install, no network). A01/A02/A03 fragments
did not exist when this seat started (`ls reports/round-33/adj/` → empty at
03:53Z); the command sets were therefore *derived first* from `targets.json`
missions and `reports/round-33/claims.json`, then compared row-for-row against
each fragment once it landed (A01 03:56Z, A02 03:58Z, A03 03:59Z). This is a
verification of commands and cited results only — not a semantic review, not
round acceptance, not a canon or clearance statement.

**Verdict: A01 PASS with 2 citation defects; A02 PASS with 1 citation defect and
its named finding A02-H1 independently confirmed; A03 PASS with all counts
reproduced and its A03-F1 finding independently corroborated plus one precision
refinement.** No claim in the three fragments was found false. Three bounded
citation defects are filed below for integrator application; none changes a
verdict, and no filed byte was written by this seat.

## 1. A01 (`adj/A01-province.md`) — re-run results

| A01 reported | A11 independent result | verdict |
|---|---|---|
| last touch `c53782a`; only other row `a527120` | `git log --format='%h %ci %s' -- PROVINCE.md` → `c53782a 2026-10-17 13:09:14 -0300 supplement-opencode-1: recheck sources…` then `a527120` | same |
| blob `313b182f251564b7997b06996b4f063370778f11` at HEAD and at `c53782a` | both `git rev-parse HEAD:PROVINCE.md` and `git rev-parse c53782a:PROVINCE.md` → `313b182f251564b7997b06996b4f063370778f11` | same |
| `git diff --quiet -- PROVINCE.md` exit 0 | exit 0; `git diff c53782a HEAD -- PROVINCE.md` empty | same |
| `sha256sum` = `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` | identical, at two samples (03:53:37Z, 03:56:59Z) | same |
| 31 lines, 1636 bytes | `wc -c -l PROVINCE.md` → `31 1636` | same |
| `git rev-list --count c53782a..HEAD` = 79 | 79; `git merge-base --is-ancestor c53782a HEAD` exit 0 | same |
| six partitions, counts 21/19/18/29/20/94 | `find corpus/knowledge -mindepth 1 -maxdepth 1 -type d` → exactly the six; per-partition `*.md` counts linguistics 21, myth-symbol 19, culture-material 18, synthesis 29, verification 20, civilizations 94 (no subdirectories, so recursive = direct) | same |
| `ls tools/gates/` → 12 gate scripts + `frozen/` + `expected/` + `fixtures/` | `ls tools/gates/*.py \| wc -l` → 12; the three support dirs present | same |
| 0 game/mechanic artifacts, 0 html/css/js | `git ls-files \| grep -ciE 'game\|rpg\|mechanic'` → 0; `… grep -cE '\.(html\|css\|js)$'` → 0 | same |
| refuses-list siblings are real lanes | `lore-`, `chousa-`, `kake-`, `kotoba-`, `game-dev-2d-`, `game-dev-3d-shokunin` all exist under the fleet root | same |
| fleet round-32 report 7541 bytes | `stat` → 7541 bytes, mtime 2026-10-18 22:01:59 -0300 | same |
| 4 kotodama L0 rows, lines 44-47 | `grep -n -i kotodama .ufo/l0-questions.md` → lines 44, 45, 46, 47 (rounds 2, 8, 9, 11) | same |
| `.ufo/reports/round-33/` absent | `ls` → No such file or directory | same |
| `reports/` = 1857 tracked | `git ls-files \| grep -c '^reports/'` → 1857 | same |

**Defect A11-D1 — `corpus/README.md:95` is the wrong pointer for the census
(citation, bounded fix).** A01-2 states: "the 19/19/18/29/20/94 census in
`corpus/README.md:95` is a *previous revision's* reading". Line 95 is
`revision: 1.4 — Round-19 index refresh: the thin partitions gained ten new` —
the census string does not occur there. The string occurs at `:19`, `:100`
(`partition counts 19/19/18/29/20/94). Two limits are recorded rather than`),
`:476` and `:488`; the README's own per-partition live reading is at `:90-93`
(`civilizations 94, linguistics 19, myth-symbol 19, culture-material 18,
synthesis 29, verification 20 — 199 files`). Bounded fix: repoint `:95` → `:100`
(or `:90-93` for the live reading). Verdict impact: none — the underlying
observation is correct.

**Defect A11-D1b — the drift characterization is imprecise (same row).** A01
writes "current totals are one/two higher per partition". Measured: only
`linguistics` moved (census 19 → live 21, +2); `myth-symbol` 19, `culture-material`
18, `synthesis` 29, `verification` 20, `civilizations` 94 are **identical** to
the census. The drift is linguistics-only. Bounded fix: replace "one/two higher
per partition" with "linguistics 19 → 21; the other five partitions unchanged".

**Defect A11-D3 — an mtime reading is presented under a snapshot stamp it
postdates (precision).** A01 declares its snapshot as `2026-10-19T03:53:56Z`
(`A01-province.md:9`) and dates the 5-row `git status` to that stamp (`:100`),
then prints `stat` mtimes `00:54:15.802084688` / `00:54:18.608932265 -0300`
(`:106-108`) = **03:54:15Z / 03:54:18Z**, i.e. 19-22 s *after* the declared
snapshot, with the `stat` command itself undated (it is absent from A01's own
dated command list). Both readings are individually correct — A03 cites the same
numbers as its run #2 — so this is a dating gap, not a false measurement: the
`stat` belongs to a later sample inside a ~14 s window (after 03:54:18Z, before
the run-#3 mtimes at 03:54:32Z). Bounded fix: date the `stat` command or
annotate it "postdates the 03:53:56Z status reading". Note for honesty: the
mutant mtimes are **no longer re-observable** by any seat (the files were
restored at 03:55:27Z), so this seat can confirm the numbers are mutually
consistent across A01/A03 but cannot re-measure them.

## 2. A02 (`adj/A02-handoff.md`) — re-run results

| A02 reported | A11 independent result | verdict |
|---|---|---|
| gate on `declared-in-r6/packet.md` → exit 0, `fields=16/16 glossary-entries=20 findings=0` | identical line, exit 0 (03:53:37Z) | same |
| gate `--selftest` → exit 0, 11 findings across 9 ids, malformed exit 2, CLI from another cwd | identical selftest line, exit 0 | same |
| `exercise-handoff-e2e.py --profile v3 --quiet` → exit 0, `packet_sha256=6ced88ad…` | identical line and sha256, exit 0 (03:54:20Z) | same |
| packet/twin digests = `freeze.txt` | `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` / `6633443d70ce44ed2bb43ab58aa60a1c98e4bbc79b2f577a63181c89dc16fd4e` — equal to `freeze.txt:2-3` | same |
| links 105/105, uncertainty 27 claims, no findings | `packet_links.py` → 105 checked / 105 resolved / findings []; `packet_uncertainty.py --require-oq` → claims 27 / findings [] | same |
| contract digest `5f4c02bf…` | `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` → `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` | same |
| r6 is current by renderer wiring, `tools/exercise-handoff-e2e.py:1933-1934` | `sed -n '1933,1934p'` → `V3_BASELINE_DEFAULT = "reports/round-30/handoff/declared-in-r6/expected.json"` / `V3_FROZEN_DIR_DEFAULT = "reports/round-30/handoff/declared-in-r6"` | same |
| exactly six `declared-in*` dirs | `find reports -maxdepth 4 -type d -name 'declared-in*'` → 6: round-22/`declared-in`, round-22/`declared-in-r2`, round-23/wording/`declared-in-r3`, round-25/v3-supersession/`declared-in-r4`, round-26/handoff/`declared-in-r5`, round-30/handoff/`declared-in-r6` | same |
| `git status --porcelain` over rounds 15/20/30 empty | empty (whole tree clean apart from the three declared rows) | same |

**A02-H1 independently confirmed — both columns.** This is A02's substantive
finding, so both its sides were re-measured rather than accepted.

- *Packet side*, quoted exactly: `packet.md:148` D4-CL05 carries "typed_labels
  74, labels_by_kind native-form 56 / translated-label 12 / borrowed-strata 6,
  findings_total 16, findings_hold_or_fail 15"; `:149` D4-CL06 "hold 15, note 1,
  fail 0"; `:150` D4-CL07 "conflicts (4), quarantine handles (3)"; `:152`
  D4-CL09 "rank_rules_unresolved_items 13 … rank_quarantine_handles 3 … conflicts
  4"; `:307` OQ-V3-05 repeats them. A02's quotes are verbatim.
- *Live side*: `examples/culture-d4/typed-labels.d4.yml` `coverage` block →
  `typed_labels: 82` (`:46`), `labels_by_kind` `native-form 64 /
  translated-label 12 / borrowed-strata 6` (`:35-39`), `findings_total: 12`
  (`:32`), `findings_hold_or_fail: 12` (`:31`), `conflicts: 0` (`:30`),
  `rank_quarantine_handles: 0` (`:40`), `rank_rules_unresolved_items: 0` (`:44`),
  `reconciliation_records: 6` (`:45`); `examples/culture-d4/expected-holds.json`
  `counts` → `{'hold': 12, 'note': 0, 'fail': 0}`.
- *Self-contradiction inside the same packet*: `packet.md:68` A-30 says "82
  labels (64 native-form / 12 translated-label / 6 borrowed-strata), 12
  findings, 0 unresolved rank items, 4 era-alias rows" and `:69` A-31 says "12
  holds / 0 note / 0 fail" — i.e. the manifest rows agree with live bytes while
  the claim-ledger and open-question prose at `:148-152,307` do not. A02-H1 is
  confirmed as stated, including its "every green check missed it" reasoning
  (the gate is shape-only; the link resolver checks target existence, not quoted
  numbers).

**Defect A11-D2 — `packet.md:54` is the wrong pointer for the A-17 gate pin
(citation, bounded fix).** A02 §2 states the gate tool's digest is pinned at
"`packet.md:54`" with value `e2fa3223b2aa5738…`. Line 54 is
`| A-16 | reports/round-6/parent-reconciliation.json | … |
1b9b16710ae128185b5f1cdb339e4afd3dd09063b59974128271d23287892162 | 17,075 bytes |`.
The A-17 row carrying `tools/gates/handoff-packet-check.py` and
`e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575` is at
**`:55`** (and the same digest is restated at `:102`). Bounded fix: repoint `:54`
→ `:55`. Verdict impact: none — the digest value itself is correct.

## 3. A03 (`adj/A03-scope.md`) — re-run results

| A03 reported | A11 independent result | verdict |
|---|---|---|
| `git ls-files \| wc -l` = 2655 | 2655, at four samples 03:53:09Z → 04:00:19Z | same |
| `git ls-tree -r --name-only 139e3b6 \| wc -l` = 2655 | 2655 | same |
| `git diff --stat 139e3b6..HEAD` empty | empty, exit 0 | same |
| protected roots 1830 / 179 / 237 | `git ls-files reports/round-{1..32}` → 1830; `corpus/lessons` → 179; `tools/gates/frozen` → 237 | same |
| `git status --porcelain -uall` over the three protected roots → 0 rows | 0 rows | same |
| 3 status rows at final reading | 3 rows at 03:56:59Z and 04:00:19Z (` M LOG.md`, `?? REGIMEN.md`, `?? reports/round-33/`) | same |
| `LOG.md` is a pure append, 18 insertions, 0 deletions | `git diff --numstat LOG.md` → `18	0	LOG.md`; `--stat` → `1 file changed, 18 insertions(+)` | same |
| r5/r7 restored digests `73a66f74…` / `2f4c1e15…` | `sha256sum` = `73a66f7464ead0d99318750422256ceafac3d8c2d283f94604eb258abc1bb794` / `2f4c1e159b60d78250074c51f013d13aac3cf1b140a623d197a0883e5ecac6f3`, each equal to `git show HEAD:<path> \| sha256sum` | same |
| `acceptance_checks_passed: false` in both r5/r7 | confirmed in the restored bytes | same |
| `.ufo/reports/round-33` absent | No such file or directory | same |
| exactly one `.ufo` file newer than 2026-10-19 00:00 | `find .ufo -type f -newermt "2026-10-19 00:00"` → exactly `.ufo/reports/round-104/game-dev-2d.md` | same |
| stray fleet-root dir `bash: ` predates the round | exists, mtime Oct 18 14:01, containing only `home/…` | same |
| r5/r6/r7 writers: `run-validation.py` writes `HERE/validation.json` | `reports/round-5/run-validation.py:194` and `reports/round-7/run-validation.py:1171-1172` write `HERE / "validation.json"`; `reports/round-6/run-validation.py:336` does the same and `:283` reads round-5's receipt | same |
| prior instances cited | `corpus/lessons/round-20.md:120` records the same signature (battery error → `replay-frozen.py` could-not-evaluate, `0a126b70…` → `cd8c0ec2…`); `reports/round-32/scope.md:171` and `reports/round-28/scope.md:12` record the round-27 rewrite-then-restore | same |
| probable writer C05, `to-verify` | `.scratch/c05-tmp/r{5,6,7}.log` and `.scratch/c05-iso/` exist with the stated mtimes (00:54:39-42) | corroborated as artifacts; attribution stays `to-verify` (see §5) |

## 4. Independent corroboration of A03-F1 (filed-byte mutation) — and one refinement

This seat observed the mutation window independently of all four fragments that
report it, and adds a measurement none of them made.

**Own sample set** (`git status --porcelain` / `stat` / `git diff`):

| time (UTC) | observation |
|---|---|
| 03:53:09Z | **3 rows, clean** — 16 s *before* A03's run #1 (mtimes 00:53:25.196 / 00:53:28.557), so the tree is independently confirmed clean immediately before the first in-tree run |
| 03:55:19Z | **5 rows**; `stat` → r5 mtime `00:54:32.592439623`, r7 `00:54:35.490143993` (= A03's run #3); `git diff` shows the mutated r5 `O` error and the r7 inventory `{files: 189, raw_lines: 688, …}` → `{files: 201, raw_lines: 717, …}` |
| 03:56:38Z | 3 rows; `sha256sum` r5/r7 **equal to `git show HEAD:` bytes** — restoration confirmed independently of A03's 03:57:47Z reading |
| 03:56:59Z | `git diff --stat -- 'reports/round-*'` empty — no filed-round delta remains |
| 03:57:57Z / 03:59:46Z / 04:00:19Z | 3 rows, clean |

Two independent seats (O07 at 03:55:11Z, A03 at 03:55:25Z) report the same
mutant r5 digest `fe926984e8d15728c43c44b2fc4c0f60058f784aa4aa4b7c2e6aecc04a4dfeee`
14 s apart, and this seat observed the diff live at 03:55:19Z between those two
samples — so the mutated bytes were stable across the 03:55:11-03:55:25Z window,
not churning.

**New measurement — the mutant bytes are reproducible, and the r5 leg is
root-invariant.** `.scratch/c05-iso/` is a committed-tree copy in which the
isolated leg ran. Its r5 receipt:

```
sha256sum .scratch/c05-iso/reports/round-5/validation.json
→ fe926984e8d15728c43c44b2fc4c0f60058f784aa4aa4b7c2e6aecc04a4dfeee   (3,221 bytes)
```

— **byte-identical to the digest observed in-tree at 03:55:11Z/03:55:25Z**, and
identical in size (3,221 bytes) to the short fail-closed receipt the in-tree run
left. That is positive evidence for A03's "one runner executed twice against two
roots" inference at the r5 leg: the same generator, the same inputs, a
deterministic (wall-clock-free) receipt, two roots, one digest. The filed r5
receipt is 17,366 bytes, so both runs replaced a full historical receipt with a
short could-not-evaluate one — consistent with A03's "live-re-measurement
contamination of historical receipts, not corrections".

**Refinement (not a contradiction) to A03-F1's r6 sentence.** A03 writes "Round
6 came out byte-identical (re-run, same bytes), so it carries no residual risk."
The first half is confirmed by this seat (in-tree r6 stayed
`32c621efaccca71db3b49a9151e3a37fd3663bcd97d9a6a71d745f6034158441`, 1,218 bytes,
at every sample). The second half is weaker than stated: the r6 and r7 receipts
are **not root-invariant**, because both chain-read a predecessor's receipt
(`reports/round-6/run-validation.py:283` reads round-5's; `reports/round-7/run-validation.py:1016`
reads round-6's):

| receipt | in-tree (observed) | isolated copy (`c05-iso`) | equal? |
|---|---|---|---|
| r5 | `fe926984…` (3,221 B) | `fe926984…` (3,221 B) | **yes** |
| r6 | `32c621ef…` (1,218 B) | `483697cbeabf9f341248ea1793c83c7d43f48dd12e7ac55ed1768bc7d045ddff` (1,259 B) | no |
| r7 | `af0cf4ed32d68c2b96284b49de97cfe75900c512299d4dd7423580e9573912a4` | `5d11551e922f895bd7563fc3fb60f894e0e3ffec4917251384969e94094a6819` (7,572 B) | no |

So "r6 carries no residual risk" should read: *the in-tree r6 run left the filed
bytes unchanged*, which is what the residual-risk argument needs; the r6/r7
receipts being chain-sensitive is a separate property. Bounded fix: reword that
sentence. No verdict change — A03-F1's class identification, window, digests,
restoration and routing all hold.

## 5. What this seat did **not** verify (limits)

- **Writer attribution.** A03 marks "probable writer = C05" as `to-verify`; this
  seat confirms the `c05-*` scratch artifacts exist and that the r5 leg's bytes
  are reproducible, but the in-tree leg's author remains inference — no process
  table or session log is readable. Attribution stays `to-verify`.
- **The mutant mtimes** A01 reports (03:54:15/18Z) cannot be re-observed after
  the 03:55:27Z restore; they are consistent across A01 and A03 but unprovable
  by re-measurement.
- **A02-H1's fix path** (a new packet revision from live bytes) was not
  attempted; it is routed, and this seat files no fix.
- **A01's A01-2/A01-3 spot-grep method** is not an exhaustive per-file audit of
  all 382 corpus files; this seat re-ran the same spot checks and did not
  broaden them.
- No round-33 `run-validation.py` exists yet (A03's own owed item), so no claim
  threshold was exercised here; this fragment verifies commands, not round
  admission.

## Verdict table

| fragment | commands re-run | result | defects filed |
|---|---|---|---|
| A01 | 14 command families | **PASS** — every measured value reproduced | A11-D1 (`README.md:95` pointer), A11-D1b (drift wording), A11-D3 (undated mtime reading) |
| A02 | 9 command families + A02-H1 both sides | **PASS** — all green legs reproduced; A02-H1 confirmed against packet quotes *and* live bytes | A11-D2 (`packet.md:54` pointer) |
| A03 | 13 command families | **PASS** — all counts and digests reproduced | none (one refinement to A03-F1's r6 wording, §4) |

No fragment was found to contain a false claim. All three defects are citation
or wording precision, each with a bounded fix, none verdict-changing. Nothing in
this verification absorbs contested scope, promotes anything, or rules on canon.

## Owed: none

This seat's mission was A01-A03 verification; all three fragments landed during
the wave and were verified. The integrator still owns A03's own owed item
(`reports/round-33/run-validation.py` does not exist, so no claim-A counting
command can be run by any seat) and the disposition of A03-F1/A11-D1/D1b/D2/D3.
Because a repeat in-tree validator run would recreate A03-F1's delta, the
integrator should re-run `git status --porcelain -uall -- reports/round-{1..32}
corpus/lessons tools/gates/frozen` (expect 0 rows) and re-compare the r5/r6/r7
digests before filing the round record.

## Citations

Fragments verified (all read in full):
- `reports/round-33/adj/A01-province.md` (all 198 lines), `reports/round-33/adj/A02-handoff.md`
  (all 180 lines), `reports/round-33/adj/A03-scope.md` (all 265 lines)

Binding inputs:
- `reports/round-33/claims.json:8` (baseline), `:53-65` (claim A), `:57` (c53782a phrasing)
- `reports/round-33/targets.json:58` (A11 mission), `:5-11` (shared_rules)

Defect anchors:
- `corpus/README.md:19,90-93,95,100,476,488` (census location vs A01's `:95`)
- `reports/round-30/handoff/declared-in-r6/packet.md:54,55,102` (A-16 vs A-17 row)
- `reports/round-33/adj/A01-province.md:9,100,106-108` (snapshot stamp vs undated stat)

A02-H1 evidence:
- `reports/round-30/handoff/declared-in-r6/packet.md:68,69,148,149,150,152,307`
- `examples/culture-d4/typed-labels.d4.yml:30,31,32,35-39,40,44,45,46`
- `examples/culture-d4/expected-holds.json` (`counts` = hold 12 / note 0 / fail 0)

A03-F1 corroboration:
- `reports/round-30/handoff/declared-in-r6/freeze.txt:2-3`; `reports/round-30/handoff/declared-in-r6/run.log`
- `.scratch/c05-iso/reports/round-{5,6,7}/validation.json` (digests above),
  `.scratch/c05-tmp/r{5,6,7}.log`, `.scratch/c05-iso/` mtime 00:54:37
- `reports/round-5/run-validation.py:194`; `reports/round-7/run-validation.py:8,1171-1172`;
  `reports/round-6/run-validation.py:283,336`
- `corpus/lessons/round-20.md:120`; `reports/round-32/scope.md:171`; `reports/round-28/scope.md:12`
- `reports/round-33/op/O07-baseline-receipt.md:150-205`;
  `reports/round-33/adj/A16-shonen-material.md:208-209`;
  `reports/round-33/adj/A01-province.md:99-137`

Commands run by this seat (all 2026-10-19, lane root,
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; read-only):
- `date -u '+A11_UTC=%Y-%m-%dT%H:%M:%SZ'` (03:53:09Z, 03:53:37Z, 03:53:57Z, 03:54:20Z,
  03:55:19Z, 03:56:38Z, 03:56:59Z, 03:57:57Z, 03:59:46Z, 04:00:19Z)
- `git rev-parse HEAD`; `git log -1 --format='%H %ci %s'`; `git log --format='%h %ci %s' -- PROVINCE.md`;
  `git log --oneline -- PROVINCE.md | wc -l`; `git rev-list --count c53782a..HEAD`;
  `git merge-base --is-ancestor c53782a HEAD`; `git rev-parse HEAD:PROVINCE.md`;
  `git rev-parse c53782a:PROVINCE.md`; `git diff --quiet -- PROVINCE.md`;
  `git diff c53782a HEAD -- PROVINCE.md`
- `sha256sum PROVINCE.md` (×2); `wc -c -l PROVINCE.md`
- `find corpus/knowledge -maxdepth 1 -mindepth 1 -type d`; per-partition `ls <dir>/*.md | wc -l`
  and `find <dir> -name '*.md' | wc -l` (six partitions); `ls tools/gates/*.py | wc -l`; `ls tools/gates/`
- `git ls-files | wc -l` (×4); `git ls-tree -r --name-only 139e3b6 | wc -l`;
  `git diff --stat 139e3b6..HEAD`; `git ls-files reports/round-{1..32} | wc -l`;
  `git ls-files corpus/lessons | wc -l`; `git ls-files tools/gates/frozen | wc -l`;
  `git ls-files | grep -c '^reports/'`; `git ls-files | grep -c '^reports/round-'`;
  `git ls-files | grep -c '^corpus/'`; `git ls-files | awk -F/ '{print $1}' | sort | uniq -c`;
  `git ls-files | grep -cE '\.(html|css|js)$'`; `git ls-files | grep -ciE 'game|rpg|mechanic'`;
  `git ls-files kotodama-shokunin/ | wc -l`
- `git status --porcelain` (10 samples, times above); `git status --porcelain --untracked-files=all reports/round-33/ | wc -l`;
  `git status --porcelain -uall -- reports/round-{1..32} corpus/lessons tools/gates/frozen | wc -l`;
  `git diff --stat -- 'reports/round-*'`; `git diff --stat -- reports/round-5/validation.json reports/round-7/validation.json`;
  `git diff reports/round-5/validation.json`; `git diff reports/round-7/validation.json`;
  `git diff --stat LOG.md`; `git diff --numstat LOG.md`
- `sha256sum reports/round-{5,6,7}/validation.json`; `git show HEAD:reports/round-{5,6,7}/validation.json | sha256sum`;
  `stat -c '%y %n'` on r5/r6/r7 receipts and `.scratch/c05-iso` trees
- `python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md`;
  `… --selftest`; `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet`;
  `python3 tools/harness/packet_uncertainty.py --packet …/twin.json --require-oq --json`;
  `python3 tools/harness/packet_links.py --packet …/twin.json --json`
- `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md`;
  `sha256sum reports/round-30/handoff/declared-in-r6/{packet.md,twin.json}`;
  `cat reports/round-30/handoff/declared-in-r6/freeze.txt`; `cat …/run.log`
- `sed -n` reads of `tools/exercise-handoff-e2e.py:1930-1938`,
  `tools/gates/handoff-packet-check.py:1-40`, `reports/round-5/run-validation.py:194`,
  `reports/round-6/run-validation.py:283,336`, `reports/round-7/run-validation.py:1-14,1171-1172`
- `python3` read of `examples/culture-d4/typed-labels.d4.yml` coverage block and
  `examples/culture-d4/expected-holds.json`
- `find reports -maxdepth 4 -type d -name 'declared-in*'`;
  `find /home/vgpnk/Projects/shokunin/.ufo -type f -newermt "2026-10-19 00:00"`;
  `ls -la /home/vgpnk/Projects/shokunin/.ufo/reports/round-33`; `ls -la "/home/vgpnk/Projects/shokunin/bash: "`;
  `ls -la .scratch/c05-iso/`; `ls .scratch/c05-tmp/`; `head .scratch/c05-tmp/r{5,6}.log`
- `grep -n -i kotodama /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`;
  `grep -n` for the census string and the A-17 row
- `ps -eo pid,etimes,lstart,args | grep -i python` (no round-33 runner live at 03:56Z;
  the only matching process was a peer seat's own status sampler, PID 80829)

FILES: reports/round-33/adj/A11-verify-a01-a03.md | SUMMARY: Independent re-run of the
A01–A03 cited commands: A01/A02/A03 all PASS with every measured value reproduced; three
bounded citation defects filed (A01's `corpus/README.md:95` census pointer and its
"one/two higher per partition" wording, A02's `packet.md:54` gate-pin pointer) plus A01's
undated mtime reading; A02-H1 confirmed on both packet quotes and live D4 bytes; A03-F1
independently corroborated, with the in-tree mutant r5 digest measured byte-identical to
the isolated copy's (root-invariant, reproducible) and a refinement to the r6 wording.
