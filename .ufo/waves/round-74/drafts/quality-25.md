# QUALITY criterion 25 — draft, revision 2 (post-wave-1; seat ScribeQuality25)

Target for the append: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/QUALITY.md` (append-only, after
criterion 24; this draft does not write it).

Revision 2 exists because wave-1 rejected revision 1. `CritQuality25` measured that r1's own checker printed
`CONFIG: PASS / JUNK: PASS / LEGTEXT: PASS`, exit 0, for a counter that grades the graded tree, and returned
**REJECT AS DRAFTED — fixable, not a tradeoff.** (`CritQuality25.md:5`). `CritMistakeFix` F8 found a second
defect of the same kind: QUALITY 25, as worded, fails on the round's own control receipts
(`CritMistakeFix.md:371`), because a config control must *print* the literal a r1 clause forbade.
`CritFrozenCfg` §4–§5 supplied the freeze/anchor scheme, and `RevClaimsFidelity` F1 the counter-path ruling.
The revision keeps r1's subject and drops every mechanism the round does not ship, marking the rest
**proposed, not shipped** below.

## What the round ships (measured, not assumed)

| fact | evidence |
|---|---|
| Claim-C counter: `--root --lands --freeze [--fleet-root] [--selftest]`; 13-leg table (incl. `INDEX`); refusal prints `ACCEPT-C-74: FAIL legs=0/13 (refused: …)` and returns 2 | `.ufo/waves/round-74/counters/accept-c.py` sha256 `b2dc1b64…`, `main()`, `refuse()` |
| C reads every constant with `git_bytes(root, "show", "%s:%s" % (freeze, CLAIMS))`; the map is `git show <freeze>:<map.path>` hashed against the frozen `map.sha256` | same file, `load_frozen_config()`, `_map_records()`, `leg_frozencfg()` |
| C's FROZENCFG fails when `<freeze>` is not on `rev-list --first-parent <lands>`, when the base is not an ancestor, when the map at `<freeze>` does not hash to `map.sha256`, or when `claims.json` at `<lands>` hashes differently from the frozen bytes | `leg_frozencfg()` |
| C's receipt lines: `# freeze revision: <freeze>`, `# config sha256 (frozen claims.json): <h>`, `# config source: git show <freeze>:reports/round-74/claims.json (never the graded tree)`, `# frozen legs: 13 (…)`, `# frozen map: <path> sha256=<h>` | `print_receipt()` |
| Claim-Ca counter: same CLI plus `--fleet-root`; 11 legs; refusal prints `ACCEPT-CA-74: FAIL legs=0/11 (REFUSED: …)` | `.ufo/waves/round-74/counters/accept-ca.py` sha256 `76d00b88…`, `_refuse()` |
| Ca's LEGCOUNT: refuses when the frozen leg names/count differ from its table | `main_check()`, the `LEGCOUNT` block |
| Ca's FROZENCFG fails when `<freeze>` is not an ancestor, is not on the lands first-parent chain, the base is not an ancestor of `<freeze>`, or `claims.json`/`ledger.json` are absent at `<freeze>`/`<lands>` or have different blob ids there | `leg_frozencfg()` |
| Ca's receipt lines: `# freeze: <freeze> (config read at this commit only)`, `# ledger: reports/round-74/ledger.json source=freeze sha256=<h>` | `main_check()` |
| Neither counter runs the junk fixtures; the generator is `counters/junk-fixtures.py` sha256 `d4789c39…` (J1–J7, `--run-r73`) | `ExecJunkFixtures.md` §artifacts, `junk-fixtures.py` |
| The four receipts this criterion names do not exist yet — `reports/round-74/telemetry/` holds only `census-start.txt`; they are what the freeze commit must add | `ls reports/round-74/telemetry` |
| The counters currently sit at `.ufo/waves/round-74/counters/`; the criterion names `reports/round-74/accept-{c,ca}.py` and the freeze must land them there (one path in claim `after`, claim `counter`, SKILL row and freeze commit — `RevClaimsFidelity` F1) | `RevClaimsFidelity.md` F1 |

Both counters implement the LEGCOUNT refusal as these bytes stand: `accept-c.py` compares the frozen list in
order (`LEGCOUNT: the frozen claims.json lists %d legs`) against a 13-leg table that includes `INDEX`, and
`accept-ca.py` compares count and name set against its 11. The bytes moved under this revision (C:
`e5290e51…` → `507b365b…` → `b2dc1b64…`; Ca: `5b76e006…` → `fd0ad795…` → `76d00b88…`), so every fact in the table above is
stamped with the sha it was read at, 2026-10-25 22:09 local.

## The criterion, as it would be appended

25. **A counter takes its constants from a named freeze commit and ships the junk landings it must reject** — adds to criteria 9, 11, 17, 19 and 23.
Scope: each round counter named by a claim's `counter` field (`reports/round-<N>/accept-c.py`, `reports/round-<N>/accept-ca.py`); the freeze commit is the commit that adds `claims.json`, `ledger.json`, both counters, the do-nothing receipts and the junk-landing receipts.
(a) **Constants and refusals.** The counter takes a required `--freeze <40hex>` beside `--lands` and refuses to grade — exit 2, verdict line `FAIL legs=0/<n> (refused: …)`, never a PASS — when a revision is not a 40-hex commit, when `<freeze>` is not a strict ancestor of `<lands>` on the lands first-parent chain, when `<lands>` equals the frozen base, when the frozen `claims.json` cannot be read at `<freeze>`, or when the frozen leg list and the counter's own leg table disagree (LEGCOUNT, clause (c)). Every constant is read with `git show <freeze>:reports/round-<N>/claims.json`; claim Ca adds `git show <freeze>:reports/round-<N>/ledger.json`, and claim C the renumber map whose sha256 the claim freezes (`map.sha256`). The FROZENCFG leg fails when the graded tree's `claims.json` differs from the frozen bytes (claim C: sha256 of the bytes; claim Ca: blob id for `claims.json` and `ledger.json`), when either file is absent at `<lands>` or `<freeze>`, when `<freeze>` is not on the lands first-parent chain, or when the map at `<freeze>` does not hash to `map.sha256`. The receipt says where the constants came from, in its own lines: `# config source: git show <freeze>:reports/round-<N>/claims.json (never the graded tree)` with `# config sha256 (frozen claims.json): <h>` (claim C), `# freeze: <freeze> (config read at this commit only)` with `# ledger: reports/round-<N>/ledger.json source=freeze sha256=<h>` (claim Ca). A receipt whose only config-source line names a graded tree or a lane worktree is the round-73 defect itself, not a disclosure of it: the counter reads its acceptance contract from the graded tree; a landing can rewrite the frozen claims.json and shrink its own test (MutPredicateC.md:71).
(b) **The freeze ships the junk landings it must reject.** The freeze commit carries `counters/junk-fixtures.py` and four receipts under `reports/round-<N>/telemetry/`: `junk-c.txt` (J1–J3), `junk-ca.txt` (J4, J4b, J5–J7), `controls-c.txt` and `controls-ca.txt`. Each junk receipt carries, per fixture, one line naming the fixture, its commit and the command, the counter's own `LEG FAIL <LEG>` line and its exit code, and the verdict the round-73 counters returned on the same fixture — the red-before. A fixture the round-74 counter does not fail on its named leg fails this criterion; a receipt typed without the run does not count, so the generator's sha256 and the fixture commit travel in the receipt. The round-73 red-before is measured, not hypothetical: five of the eight landings are accepted by the round-73 counters (`ExecJunkFixtures.md:9`, SURVIVORS `J3 J4b J5 J6 J7`, `ExecJunkFixtures.md:73`).

| fixture | junk landing | must FAIL |
|---|---|---|
| J1 | two header-only stub entries stand in for the mined prose (body word floor) | ENTRIES |
| J2 | every Gate admit quote absent from its evidence window | EVIDENCE |
| J3 | `claims.json` inside the graded tree shrinks the claim to two rows and one entry | FROZENCFG |
| J4 | every `observe_cmd` constant-prints `expected_after` (literal `python3 -c print` / `echo`) | LEDGER |
| J4b | evasive constant printer (`import os;print(str(…))`) that reads no clone byte | LEDGER |
| J5 | a correction row naming only its id | ANNOTATE |
| J6 | in-place edit of a frozen receipt outside both protected sets (`ACCEPT-CA-72` FAIL→PASS) | APPENDONLY |
| J7 | a Ca correction-section note citing claim-C rows incidentally | SEPARABLE |

(c) **One text.** The frozen `legs[]` array is authoritative for the leg set: the counter refuses (exit 2, `FAIL legs=0/<n> (refused: LEGCOUNT …)`) when the count or the names of its own leg table differ from the frozen list, it prints `# frozen legs: <n> (<NAMES>)` in the receipt, and every `LEG PASS|FAIL <NAME>` line carries a `<NAME>` that list names. A counter whose documentation, table or receipt names a leg the frozen list does not — or omits one it does — is not calibrated: round 73's counter declared `LEGS (8, fixed at freeze)` and names 8 while the driver runs and *requires* 9 legs (MutLandedCa.md:115).

Check (red-before, pre-dispatch) — one line, run by a reviewer on each counter source:
```
sh -c 'grep -q -- --freeze "$1" && grep -qE "\"show\", *\"%s:%s\"" "$1" && ! grep -qE "os\.path\.join\((mat|root|clone|treework)[^)]*CLAIMS" "$1"' _ reports/round-74/accept-c.py
```
meaning: a `git show <rev>:<path>` call is present, a `--freeze` argument exists, and no `claims.json` path is
joined from the graded materialization or the root. Measured 2026-10-25:

| source | exit | why |
|---|---|---|
| `counters/accept-c.py` (`b2dc1b64…`) | 0 | show at `load_frozen_config`/`leg_frozencfg`/`_map_records`; no graded-root join |
| `counters/accept-ca.py` (`76d00b88…`) | 0 | `show()` helper; no graded-root join |
| `reports/round-73/accept-c.py` | 1 | no `--freeze`; joins `mat` and `root` with `CLAIMS` |
| `reports/round-73/accept-ca.py` | 1 | no `--freeze` (the ledger is read at `<lands>`) |
| decoy: literal in a comment, no `--freeze` | 1 | first arm |
| decoy: `--freeze` arg + comment literal + `open(os.path.join(mat, CLAIMS))` | 1 | third arm |
| counter reading the graded tree under a literal path, decoy `git show` | **0** | the stated limit — see below |

Limits, stated: grep reads shape, not dataflow, so a counter can pass this one-liner while reading the graded
tree (the last row) — the verdict is the FROZENCFG leg and the J3 receipt, never the one-liner alone. The
one-liner also cannot prove the `git show` argument is the `--freeze` value, nor that a second read path is
absent. And a rewritten freeze commit is not detectable in the lane at all: only an external pin can decide it,
and today the fleet report records the freeze hash (round 73 recorded `af65165`, seven hex) — a lane seat cannot
close that hole.
Binds from round 74; no earlier round is retro-fitted.
Grounded in `corpus/lessons/round-74.md` `## Mistakes` R74-M3 (drafted at `.ufo/waves/round-74/drafts/mistakes.md:16`, landing with the lesson: Four counter channels survived round 73.), round-73 routed defect 4 (`junk landings pass 11/11, config read from graded tree, ledger constant-printers`, `corpus/lessons/round-73-verifier-spotcheck.md:87`) and the wave-2 mutation reports behind them.

## What it does not cover (one line)

It fixes where a counter's constants come from, that the frozen commit ships four receipts in which the round-74
counter fails each fixture on its named leg while the round-73 counters accepted five of the eight, and that the
leg labels are one set — it does not show the freeze commit predates the first scoring seat (only an external pin
decides that), nor that a fixture fails *only* its named leg.

## Proposed, not shipped — not required by this criterion

- A `reports/round-<N>/freeze.json` sidecar pinning each frozen file's sha256, and a fleet-root pin file written
  at freeze time (`CritFrozenCfg` §4.1, §4.3). Not shipped: no sidecar exists in the counters or the round-74
  tree.
- A counter-bytes pin (`counter sha256 (freeze)`) with a `counter-revisions.md` door (`CritFrozenCfg` §4.2.7).
  Shipped counters print their own sha256 only (`# counter sha256 (self):`) and compare no freeze copy.
- The phantom-descendant divergence run, and the `# config sha256:` **re-derivation** by the checker
  (`CritQuality25` §3): the printed digest ships, the re-derivation does not.
- Per-leg `label` + `leg_sha256` in `claims.json` with `LEG-TEXT` digests in the receipt (revision 1 clauses
  (a)/(c)). Not shipped — `grep -c '"leg_sha256"\|"label"' reports/round-74/claims.json` = 0 — and dropped:
  `CritQuality25` §2.1 measured that the digest table is satisfiable by prose while forcing a hard-coded digest
  into the counter, which is the `constant-observe` class this criterion's own J4b forbids.

## Honesty / bounds

- Every shipped-state line above was read from the bytes named, at the sha256 given, on 2026-10-25; both counters
  were edited by their executor seats during this revision (`accept-c.py` `e5290e51…` → `507b365b…` →
  `b2dc1b64…`; `accept-ca.py` `5b76e006…` → `fd0ad795…` → `76d00b88…`, all 2026-10-25 22:09 local), so neither the line numbers in the
  review reports nor an earlier revision of this draft describes them; the criterion text is phrased against
  behaviour and stamped facts, not line positions.
- The one-liner and all seven rows of its table are real runs of the pasted command, 2026-10-25; the decoys live
  in `/tmp/ScribeQuality25/` (`decoy.py`, `decoy2.py`, `limit.py`).
- The J1–J7 expected legs are `ExecJunkFixtures`' per-fixture expected verdicts; the four receipts do not exist
  yet, so no round-74 junk verdict is quoted anywhere above — only the round-73 red-before, which is filed.
- Not measured here: a round-74 counter run (these counters have not run at the time of writing), the fleet pin,
  and whether the freeze lands the counters at `reports/round-74/` as clause Scope requires.
