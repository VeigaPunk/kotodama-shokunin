# ExecCounterMatrix — final C and Ca counter leg pass/fail matrices (round 76 kotodama, wave 2 falsification)

Seat: ExecCounterMatrix (executor). Read-only falsification. No source file edited, no build/test/lint/formatter
run, no commit, no push.

## Revisions used (committed bytes only)

| role | revision | note |
|---|---|---|
| base | `98c486bdb4650ba5b8e651d332910e8ee60ad121` | tree `6e961f92169764069d36136752671301ce971677` |
| frozen C/Ca config | `df0f0309d61e5485bb17035d3f8791b1e6a11d40` | tree `94c4050014ebaa6c5dcad5c3298de4e0ab4320aa` |
| Ca landing | `a43ed807ea38b5fc5a7875a839d576cea73aba7c` | tree `b2e4fbb3d862f1da5c0069859ac1b6a1dca332a6` |
| C landing | `722e69ff6361aadf148cb46acbf6ac8fd147f59a` | tree `24d943fc3388a335b4892db0917ef69eb5679ade` |
| measured-outcome commit | `af6744353937e56f296e3094fb077baa1e22f65f` | "round-76: record measured claim outcomes"; carries the two final receipts |

`a43ed807ea38` is an ancestor of `722e69ff6361` (`git merge-base --is-ancestor` → true), so the Ca landing
precedes the C landing on the first-parent chain.

Frozen artifact digests are identical at the freeze and at both landings (so the counters were never edited
after the freeze):

- `reports/round-76/claims.json` sha256 `facd1cb766e97e00…` at df0f030, a43ed807, 722e69f
- `reports/round-76/ledger.json` sha256 `d609c8b06b9abfa2…` at df0f030, a43ed807, 722e69f
- `reports/round-76/accept-c.py` sha256 `5fc8e3c772823d2d8c3b204b4332f5f3aa959f8845a010adae1b6555c7d76165` at df0f030, a43ed807, 722e69f
- `reports/round-76/accept-ca.py` sha256 `c1fc755e926f8d25e622469ec018bc9ad6c22b2f99ba83447fa95baab4a9695b` at df0f030, a43ed807, 722e69f
- `.ufo/waves/round-76/assimilation/id-renumber-map.json` sha256 `a9f530e26cbbd607d156a2fc32cc4ed241f9c37b79e17dc17cc5335f184f4092` at df0f030 and 722e69f (matches `claims.json` `map.sha256`)

Each final receipt's self-declared `# counter sha256 (self):` equals the committed counter digest above
(`measures-c.txt:7`, `measures-ca.txt:2`), so both receipts were produced by the frozen counter bytes.

## Leg denominators (frozen)

- C: 13 leg slots — `claims.json` `claims[id=C].legs` has **13 entries with `INDEX` listed twice**
  (positions 10 and 13; the counter's `LEGS` tuple at `accept-c.py:6381-6395` likewise lists `("INDEX", leg_index)`
  twice). Distinct leg *names* for C = 12; the frozen denominator is 13 because one leg is double-counted.
- Ca: 12 leg slots — `claims.json` `claims[id=Ca].legs` has 12 entries, no duplicate; `accept-ca.py:289-291`
  `REQUIRED_LEGS` has the same 12 names in the same order (LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY,
  R1EXEMPT, NOSTUB, SEPARABLE, RECEIPTS, COMBINED, FROZENCFG, STAMP).

## Final matrices (committed receipts)

### Claim C — `reports/round-76/telemetry/measures-c.txt` (committed at af67443)

Run: `python3 -B reports/round-76/accept-c.py --root . --lands 722e69ff6361aadf148cb46acbf6ac8fd147f59a
--freeze df0f0309d61e5485bb17035d3f8791b1e6a11d40 --fleet-root /home/vgpnk/Projects/shokunin
--work /fast/scratch/hyaku/kotodama-r76/final-c-counter`

| # | leg | verdict | receipt line | detail (abridged) |
|---|---|---|---|---|
| 1 | ENTRIES | PASS | :24 | — |
| 2 | ROWS | **FAIL** | :25-26 | registry line added outside the frozen row_set: `- calendar-standard design — S896 → S895 → S894: start with `; `**State-standard calendar compilation (round 76).** Question` |
| 3 | REPOINTED | PASS | :27 | — |
| 4 | GATE | PASS | :28 | — |
| 5 | EVIDENCE | PASS | :29 | — |
| 6 | REJECTS | PASS | :30 | — |
| 7 | GROUND | PASS | :31 | — |
| 8 | CITEDLINES | PASS | :32 | `CITED-LINES: 0 finding(s) in 1 file(s)` |
| 9 | CENSUS | PASS | :34 | `exit=0` |
| 10 | INDEX (slot 1) | PASS | :36-37 | 6 sections, culture-material=41, footer total=253, vector 32/32/41/29/24/95 |
| 11 | COLLCHECK | **FAIL** | :38-39 | `map record S938 -> S895 names a document the row does not: https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno; ids=817 staged=132 collisions=35 guard=ok/ok map=7` |
| 12 | FROZENCFG | PASS | :40-42 | freeze df0f030 constants read from `git show`; `claims@lands=frozen-bytes`, `map=(sha256-match)`, `ledger=frozen-bytes` |
| 13 | INDEX (slot 2) | PASS | :43 | identical detail to slot 1 (same `leg_index` function) |

**Verdict: `ACCEPT-C-76: FAIL legs=11/13` (exit=1).** PASS 11 + FAIL 2 = 13 = the frozen denominator. ✔ sums.

### Claim Ca — `reports/round-76/telemetry/measures-ca.txt` (committed at af67443)

Run: `python3 -B reports/round-76/accept-ca.py --root . --lands a43ed807ea38b5fc5a7875a839d576cea73aba7c
--freeze df0f0309d61e5485bb17035d3f8791b1e6a11d40 --fleet-root /home/vgpnk/Projects/shokunin
--combined 722e69ff6361aadf148cb46acbf6ac8fd147f59a --main a43ed807ea38b5fc5a7875a839d576cea73aba7c
--work /fast/scratch/hyaku/kotodama-r76/final-ca-counter`

| # | leg | verdict | receipt line | detail (abridged) |
|---|---|---|---|---|
| 1 | LEDGER | **FAIL** | :4 | L76-13 stated_at path `corpus/knowledge/myth-symbol/narrative-structure-frameworks.md` outside the frozen append-only allowlist; L76-19 stated_text not found at the specified base lesson line |
| 2 | BASEMISMATCH | PASS | :5 | `red=20, min=10` |
| 3 | REPAIR | **FAIL** | :6 | L76-16 `statement_after` no-match in SKILL.md |
| 4 | ANNOTATE | **FAIL** | :7 | L76-19/20/21 `rederive` not executable under the frozen argv parser (L76-20/21 treat the base revision as a path operand; L76-19 treats `chars=` as a path operand) |
| 5 | APPENDONLY | PASS | :8 | protected paths unchanged; no rule-2 edits |
| 6 | R1EXEMPT | **FAIL** | :9 | `reports/round-76/telemetry/r1exempt-green.txt` and `r1exempt-red.txt` not committed at Ca-lands |
| 7 | NOSTUB | **FAIL** | :10 | stubs `L76-19:rederive-cmd`, `L76-20:rederive-cmd`, `L76-21:rederive-cmd` |
| 8 | SEPARABLE | **FAIL** | :11 | L76-13's stated_at path is a forbidden read (`corpus/knowledge/**`) |
| 9 | RECEIPTS | PASS | :12 | round-75 Ca PASS receipt re-ran at frozen lands |
| 10 | COMBINED | **FAIL** | :13 | C-owned README heading change at line 410 outside Ca's frozen APPENDONLY exemption; `owned_inplace` config has no valid line number |
| 11 | FROZENCFG | PASS | :14 | frozen bytes match |
| 12 | STAMP | PASS | :15 | stamped=evaluated=measured Ca-lands |

**Verdict: `ACCEPT-CA-76: FAIL legs=5/12` (exit=1).** PASS 5 + FAIL 7 = 12 = the frozen denominator. ✔ sums.

## No-data controls (committed, at the freeze)

`reports/round-76/telemetry/controls-c.txt` and `controls-ca.txt` were committed in `58e6c81` ("record final
frozen no-data controls") and are present unchanged at 722e69f and af67443.

| control | receipt | verdict | PASS+FAIL vs denominator |
|---|---|---|---|
| C lands == freeze | `controls-c.txt:55` | `ACCEPT-C-76: FAIL legs=1/13` (exit=1) — only FROZENCFG green (:50) | 1+12 = 13 ✔ |
| C lands == base | `controls-c.txt:62` | `ACCEPT-C-76: FAIL legs=0/13 (refused: lands 98c486bdb465 is the frozen claim base …)` (exit=2) | 0+0 = 0, refused ✔ |
| Ca lands == freeze | `controls-ca.txt:65` | `ACCEPT-CA-76: FAIL legs=5/12` (exit=1) — green: BASEMISMATCH, APPENDONLY, RECEIPTS, FROZENCFG, STAMP | 5+7 = 12 ✔ |
| Ca lands == base | `controls-ca.txt:71` | `ACCEPT-CA-76: FAIL legs=0/12 (refused: --lands equals the frozen base 98c486bdb465)` (exit=2) | 0+0 = 0, refused ✔ |

Both counters' do-nothing shapes hold: the base is refused (exit 2, `legs=0/N`), the freeze is graded (exit 1),
and every data leg is red at the freeze. The C claim's own `do_nothing_control` text ("at lands == freeze the
ENTRIES, ROWS, GATE, EVIDENCE, GROUND and INDEX data legs must fail while FROZENCFG is green; lands==base must
be refused (exit 2)") is satisfied by the committed receipt.

Two controls named in the frozen Ca `do_nothing_control` are **absent from the committed receipt**:
(3) a run with no `--work`/`$HYAKU_SCRATCH`/`$TMPDIR` refused with exit 2 and no leg line, and (4) a run without
`--combined` refused with exit 2. `controls-ca.txt` contains only control 1 (lands==freeze) and control 2
(lands==base). The no-scratch and no-`--combined` refusals are exercised by the counter's own selftest instead
(`selftest-ca.txt`: `scratch-noroot -> exit=2`, `combined-required -> exit=2`, all legs `-`), so the behaviour is
covered but not by the named control receipt.

## Frozen leg-table defect (falsifies the frozen denominator)

`claims.json` `claims[id=C].legs` lists **INDEX twice** (13 entries, 12 distinct names) and the counter's
`LEGS` tuple repeats `("INDEX", leg_index)` (`accept-c.py:6381-6395`). Both final receipts therefore print two
identical INDEX lines (`measures-c.txt:36` and `:43`, byte-identical detail). Consequences:

- The frozen C denominator 13 overstates the number of distinct checks: one check is graded twice.
- The claim's declared after-state ("`ACCEPT-C-76: PASS legs=13/13`") can never be a 13-distinct-check pass.
- The frozen claims' own after-state text was written against this denominator and is not independently
  falsifiable as stated.

## Root causes of each red leg, from committed bytes

### C — ROWS (red at C-landing)
`git diff 98c486bdb465 722e69ff6361 -- corpus/SOURCES.md` adds 8 lines: the three rows S894/S895/S896 plus two
**prose** lines that are not registry rows —

- `- calendar-standard design — S896 → S895 → S894: start with the state-press account …` (SOURCES.md:854)
- `**State-standard calendar compilation (round 76).** Question: does one staged calendar amendment …` (SOURCES.md:902)

`accept-c.py:1598-1603` (leg_rows) compares the base→lands line multiset and fails any added non-blank line that
does not match the row pattern. The two prose lines are added by `cab5247` — a commit **ancestor of the freeze
`df0f030`** — so they are already present in the frozen tree. `## Paths` is a pre-existing convention section at
base (SOURCES.md:849 with a bullet at :851), and round-prose blocks like
`**Pastoralism and animal husbandry (rows S048–S069).** Round 50, 2026-10-21.` are pre-existing at base too.
**The red is therefore not caused by the round-76 data landing; it is baked into the freeze.** The freeze is
self-inconsistent: the frozen row_set admits only S894-S896 while the frozen tree already carries two extra
non-row lines, and the counter diffs against base, so no landing can turn ROWS green without editing
`corpus/SOURCES.md` to remove a pre-existing convention section. Same two lines are named in the freeze-time
control receipt (`controls-c.txt:30`), confirming they predate the landing.

### C — COLLCHECK (red at C-landing)
`accept-c.py:3626-3631` requires each frozen map record's URL to be document-compatible with the landed row's
source cell (`urls_compatible`, `accept-c.py:471-483` — exact host+path, or one path contained in the other).
The frozen map records `S938 -> S895` with `document_normalized:
openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=…` (`id-renumber-map.json` `map.S938`), while the landed
S895 row's source cell carries `…/bzgk/std/newGbInfo?hcno=…` and its Wayback wrapper. `showGb` and `newGbInfo`
are different paths, so neither contains the other and the check fails. The row's own text says showGb
"redirects here by HTTP 302" — the map's `S938` entry retains the alias URL rather than the redirect target.
The frozen `claims.json` `row_set` for S895 documents the collapse as `staged: "S932/S938"` "one row", so the map
record and the row disagree. **Not fixable by the landing; the map blob is sha-pinned by `claims.json`
`map.sha256` and must stay byte-identical for FROZENCFG to stay green.** Same message at the freeze control
(`controls-c.txt:48`) — pre-existing at the freeze.

### Ca — LEDGER (red at Ca-landing; also red at the freeze)
Two defects in the **frozen** `reports/round-76/ledger.json` (sha `d609c8b0…`, identical at all three revisions):

1. `L76-13` has `disposition: ANNOTATE` with `stated_at:
   corpus/knowledge/myth-symbol/narrative-structure-frameworks.md:8` — a knowledge file, not one of the frozen
   append-only allowlist `{LOG.md, SCORECARD.md, corpus/lessons/round-75.md, corpus/QUALITY.md}`. The pair is
   also a forbidden read for SEPARABLE (`corpus/knowledge/**`), which is the eighth red leg.
2. `L76-19` has `stated_text: "S892's window (\`chars=4097 before=284\`)"` and `stated_at:
   corpus/lessons/round-75.md:48`. At base the file reads (lines 47-48):
   `… text. S888's window (\`chars=4097 before=10\`) and S892's` / `   (\`chars=4097 before=284\`) both start at …`
   — "S892's" ends line 47 and the window phrase opens line 48, so the frozen stated_text never occurs
   contiguously and `norm()`-folded membership fails (`accept-ca.py:1569-1573`).

Both are properties of the frozen ledger, not of the landing, so LEDGER/SEPARABLE cannot be turned green without
rewriting frozen bytes — which the Ca kill rule forbids ("the after-state never requires rewriting frozen bytes").

### Ca — REPAIR (red)
`L76-16` `statement_after` = `{path: "SKILL.md", parse: "^\\| accept-c-75 \\|.*?committed counter sha256
\`([0-9a-f]{12})\`"}`. The Ca landing `a43ed807` did edit SKILL.md (word-diff: `Measured 2026-10-27 at counter
sha256 \`fa5060b91bdb…\`` → `2026-10-27: committed \`reports/round-75/accept-c.py\` … \`315c5f3f27fd…\``), but the
new wording has **no** `committed counter sha256` phrase (`git show a43ed807:SKILL.md | grep -c 'committed counter
sha256'` → 0), so the frozen parse cannot match (`accept-ca.py:1409-1413` → "statement_after no-match").

### Ca — ANNOTATE and NOSTUB (red, same three pairs)
`L76-19`, `L76-20`, `L76-21` carry `rederive` strings that the frozen argv parser cannot execute:

- L76-19: `git grep -h -E ^window: chars= 98c486b… -- reports/round-75/evidence/S892.txt` — `chars=` becomes a
  path operand (the pattern is not quoted).
- L76-20/21: `git grep -h -o -E ^sha256: [0-9a-f]{8} 98c486b… -- …` — the base revision becomes a path operand.

The frozen parser splits with `shlex.split` and rejects metacharacters outside a pattern operand
(`accept-ca.py:1377-1382`, `observe_problem` at :1207). The `observe_cmd` arrays in the same ledger entries are
correctly formed argv lists; only the `rederive` strings are broken. NOSTUB red for the same three ids
(`measures-ca.txt:10`) because the SCORECARD correction rows carry the frozen `rederive` string, which the
counter cannot execute either. Note the SCORECARD at `a43ed807` does contain all 19 ANNOTATE rows under
`## Corrections — round 76` (19 `| L76-` rows) — the rows landed; the frozen rederive strings did not.

### Ca — R1EXEMPT (red)
The leg requires `reports/round-76/telemetry/r1exempt-green.txt` and `r1exempt-red.txt` committed at Ca-lands.
Neither file exists in any commit (`git log --all -- 'reports/round-76/telemetry/r1exempt*'` empty;
`git rev-list --all --objects | grep round-76/telemetry/r1exempt` empty). The round-76 `reports/round-76/fixtures/`
holds only the three JSON fixtures (`r1exempt-green.json`, `r1exempt-mixed.json`, `r1exempt-red.json`); the
**receipts** were never committed. Round-75 precedents exist at `reports/round-75/telemetry/junk-ca.txt` and
round-74 at `reports/round-74/telemetry/junk-ca.txt`, so the pattern is known but round 76 did not land it.

### Ca — COMBINED (red)
`accept-ca.py:1913-1925` reads `claim_c_owned_inplace` from the frozen `claims.json` and requires each entry to
carry an integer `base_line` within range. The frozen `claims.json` `claims[id=C].owned_inplace[0]` is
`{path: "corpus/README.md", base_text: "## culture-material/ (40)", after_text: "## culture-material/ (41)"}` —
**no `base_line` key** (`python3` over `git show df0f030…:reports/round-76/claims.json` confirms the key set is
exactly `path`/`base_text`/`after_text`). The counter reports
`claim-C owned-inplace line has invalid line number: {'path': 'corpus/README.md', …}` and therefore cannot
exempt the C-owned README heading change (base SOURCES/README line 410 `## culture-material/ (40)` → lands
line 410 `## culture-material/ (41)`). **Frozen-config defect:** the C landing cannot make Ca's COMBINED leg
green, and the Ca landing cannot fix it either, because the fix would be to edit frozen `claims.json`.

## Claim verdicts (exact)

| claim | axis | frozen declared after-state | measured | verdict |
|---|---|---|---|---|
| **C** | coverage | `ACCEPT-C-76: PASS legs=13/13` (exit 0) | `ACCEPT-C-76: FAIL legs=11/13` (exit 1) at C-landing `722e69ff6361` | **FAILED AS DECLARED.** Red legs ROWS, COLLCHECK. 11+2 = 13 = denominator. |
| **Ca** | calibration | `ACCEPT-CA-76: PASS legs=12/12` (exit 0) | `ACCEPT-CA-76: FAIL legs=5/12` (exit 1) at Ca-landing `a43ed807ea38` | **FAILED AS DECLARED.** Red legs LEDGER, REPAIR, ANNOTATE, R1EXEMPT, NOSTUB, SEPARABLE, COMBINED. 5+7 = 12 = denominator. |

No axis score is advanced; the lane's own `SCORECARD.md` at `af67443` records the same verdicts ("failed as
declared; no score delta") and `corpus/lessons/round-76.md` names the same failing legs. My independent count
from the committed receipts agrees with the lane's record.

### Substantive (non-counter) state that did land

Claim C's *substance* landed and is visible in committed bytes, even though the counter refuses it:

- knowledge tree 252 → 253 `.md` files (`git ls-tree -r --name-only 98c486b… -- corpus/knowledge | grep -c '\.md$'`
  → 252; same at 722e69f → 253); the admitted entry
  `corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md` is present at 722e69f
  (added by `788bd56`), and the three non-admitted candidate paths
  (`…-2026-10-24-r10.md`, `era-periodization-models.amend-2026-10-23b.md`, `…-2026-10-23c.md`) are absent —
  matching the frozen `min_admitted: 1`.
- registry 817 → 820 rows (817 at base, 820 at 722e69f), exactly S894/S895/S896 added
  (`grep -cE '^\| S89[456] '` → 3), one row per document.
- base ground sweep is empty and the receipt is committed: `reports/round-76/telemetry/gap-sweep.txt`
  (3 fragments × `base matches: 0`, exit=1), and the census end receipt exits 0
  (`reports/round-76/telemetry/census-end.txt`, last line `kotodama ok …`, `exit=0`).

Claim Ca's *substance* also landed partially: 19 ANNOTATE rows are in `SCORECARD.md` `## Corrections — round 76`
at `a43ed807`, and SKILL.md was repaired — but the frozen counter cannot accept either because of the defects
above.

## Receipt-grammar note (falsification risk, not a leg verdict)

`tools/check-receipt-seq.py` (QUALITY 17/19 grammar) requires each receipt to carry **all five** headers
`# stamped revision:`, `# evaluated revision:`, `# measured revision (lane main):`, `# tree:`,
`# counter sha256 (self):` with `stamped == evaluated == measured`, the recorded tree equal to
`git rev-parse <stamped>^{tree}`, and the recorded sha256 equal to the counter's.

- `measures-c.txt` carries all five (`grep -cE '^# (stamped|evaluated|measured|tree|counter sha256)'` → 5),
  stamped=evaluated=measured=`722e69ff6361`, tree `24d943fc3388a335b4892db0917ef69eb5679ade` = the real tree of
  722e69f, sha = the committed `accept-c.py` digest. ✔ conforms.
- `measures-ca.txt` carries **one** header-shaped line (`grep -c …` → 1) and **no `# tree:` line** (`grep -c '^# tree:'`
  → 0); its single header is a free-text line
  (`# stamped/evaluated/measured a43ed807…; freeze df0f030…; counter sha256 c1fc755e…`), not the five
  `# <key>: <value>` forms the tool's regexes require. The Ca claim's STAMP leg text itself names
  "QUALITY 17/19 grammar of tools/check-receipt-seq.py". The Ca counter's own STAMP leg is green because it
  checks its in-process header, not the committed receipt file — so the leg verdict stays PASS while the
  committed receipt is not machine-readable by the named grammar.

Also absent: `reports/round-76/telemetry/measures-ca-head.txt`, which `claims.json` `claims[id=Ca].legs[9]`
(COMBINED) names as the receipt that "carries the Ca-lands stamp and exact combined revision/tree". It exists
in no commit and in no worktree file (`git log --all -- '…/measures-ca-head.txt'` empty; not in
`reports/round-76/telemetry/`). The committed `measures-ca.txt` is the receipt that was actually landed.

## Artifact-status note (evidence provenance)

At the time this seat began, `reports/round-76/telemetry/measures-c.txt` and `measures-ca.txt` were **untracked
in the lane worktree** (not committed at any revision: `git log --all -- 'reports/round-76/telemetry/measures*'`
returned nothing, and `git rev-list --all --objects | grep 'reports/round-76/telemetry/measures'` returned
nothing). They were subsequently committed by the L1 in `af6744353937e56f296e3094fb077baa1e22f65f`
("round-76: record measured claim outcomes"), and the committed blobs are byte-identical to the worktree copies
(`diff -q` → identical for both). Every matrix above is read from the committed blobs at af67443.

## What I did not do

- Did not edit any claim, counter, ledger, lane file, or report; did not commit or push.
- Did not run the counters, the census, the selftests, or any build/test/lint/formatter. Every verdict quoted is
  read from a **committed** receipt; every structural fact was re-derived read-only from committed blobs
  (`git show <rev>:<path>`, `git diff`, `git ls-tree`, `grep`, `python3` over `git show` output).
- Did not run the wave-1 or wave-2 selftest scripts (no builds/tests per the seat bounds).

## Scratch

No scratch directory was created under `/fast/scratch/hyaku/kotodama-r76/ExecCounterMatrix` — every check was
read-only against the lane repo's committed objects. Two temporary files (`/tmp/mc-committed.txt`,
`/tmp/mca-committed.txt`) were written for a byte-identity diff and deleted immediately after use.

## Tools

No install, upgrade, or package transaction was performed. No pacman transaction was run (host pacman pause
respected). `/home/vgpnk/.omp/agent/RULES.md` was not required to be read because no tool install occurred;
per the seat's tooling note no install was expected for this read-only wave.
