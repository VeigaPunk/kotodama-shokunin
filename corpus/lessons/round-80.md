# Round 80 — kotodama (Windows host, 2026-10-31)

Base `a8aaeceb42fb4e01f37181697f88aaddb9629e01` (round-79 verifier
spot-check commit); freeze `08e4fb31b7df688bd3f47a415b7b1ac061934444`;
claim O lands `c365f6ceff1ed6b331a81cf0b0cf529931e04561`; claim D lands
`66af053061bcb14a2839564389e7892e017db221` then `70db282d07552248027dc63254e20fda21a8065f`
(evidence-capture records corrected to name their row ids; the first graded
run at `66af0530` FAILed ROWS and its receipt is kept as the leg's
demonstrated-failure evidence).

## Gate

Candidates considered and dispositioned (frozen pre-data at
`reports/round-80/claims.json`, freeze `08e4fb31`):

- **ADMITTED — claim O (operability): the round-79 carry-in W1 hardening of
  `tools/ledger-token-guard.py`, landed as a QUALITY 23 revision with
  red-befores, plus the never-launched W2-class mutation pass.** Four
  hardenings from the round-79 wave's adopted-but-unlanded findings: replace-ref
  refusal + `GIT_NO_REPLACE_OBJECTS` pin (MutPath F6), 1 MiB ledger input cap +
  deep-JSON stable refusal (SentinelLimits F1/F3), expanded `GIT_*` env drop
  (SentinelLimits F9), distinct-observation floor (MutVacuous F7). Red-befores:
  old bytes (sha `504c51c6…`) accept all four junk shapes — the 1 MiB ledger
  PASSes, the duplicate-observation ledger PASSes pairs=2, deep JSON escapes as
  an unlabelled `RecursionError` traceback, the replace-ref ledger is graded
  over shadowed bytes (`reports/round-80/telemetry/w1-w2-guard-revision-run80.txt`
  section 1); hardened bytes (sha `cca7db17…`) refuse all four at exit 2 with
  stable labels (section 2). Detection regression green on new distinct-pair
  fixtures (red: exit 1 failed=3 mismatched=2 vacuous=1; green: exit 0 PASS
  pairs=4); 16/16 round-79 refusal fixtures still refuse; selftest 13/13;
  W2 mutation pass 5/5 caught, clean scenario green before the mutant rows
  (sections 3–5). Frozen counter `ACCEPT-O-80: PASS legs=10/10`, exit 0, at
  `--lands c365f6ce… --freeze 08e4fb31…`
  (`telemetry/lands-o-graded-r2.txt`). Recorded behavior change: the hardened
  floor refuses the round-79 probe ledgers themselves — their D01–D10 pairs
  share ONE `observe` object, the exact MutVacuous F7 junk class
  (`counter-revisions.md`).
- **ADMITTED — claim D (depth): the sea as a lexical surface.**
  `corpus/knowledge/culture-material/maritime-seafaring-lexicon.md` lands as
  the 254th knowledge file: six-decision table, attested anchors with exactly
  one S-id per cited line (`tools/check-cited-lines.py` sha
  `a9b0fbd5…` prints 0 findings), craft checklist, non-canon worked example,
  lore handoff. Three rows opened this round by ordinary means (plain curl,
  HTTP 200 each, same-page Wayback captures on file, automation: none; capture
  records `reports/round-80/evidence/S898.txt`–`S900.txt`):
  - **S898** — William Falconer, *An Universal Dictionary of the Marine*
    (London: T. Cadell, 1769), Project Gutenberg #57705,
    `https://www.gutenberg.org/files/57705/57705-h/57705-h.htm`, fetched
    2026-10-31 (HTTP 200, 1986595 bytes); Wayback capture of the same page
    2026-09-08, CDX status 200. Located quote (19 words): 「KEEL, the
    principal piece of timber in a ship, which is usually first laid on the
    blocks in building.」 Tier A for the 1769 English marine terminology.
  - **S899** — Admiral W. H. Smyth, *The Sailor's Word-Book* (London: Blackie
    and Son, 1867), Project Gutenberg #26000,
    `https://www.gutenberg.org/cache/epub/26000/pg26000.txt`, fetched
    2026-10-31 (HTTP 200, 2037292 bytes); Wayback capture 2026-07-21, CDX
    status 200. Located quote (18 words): 「A carved bust or full-length
    figure over the cut-water of a ship; the remains of an ancient
    superstition.」 Tier A for the 1867 RN vocabulary including its recorded
    sea-superstition entries.
  - **S900** — "Ship", *Encyclopaedia Britannica* 11th edn (1911), Wikisource
    transcription, `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Ship`,
    fetched 2026-10-31 (HTTP 200, 1340476 bytes); Wayback capture 2026-03-06,
    CDX status 200. Located quote (22 words): 「The changes from sail power to
    steam power for propulsion, and from wood to iron and steel for
    constructional purposes, proceeded together」 Tier B (survey, a century
    old; period claims stop at 1911).
  Frozen counter `ACCEPT-D-80: PASS legs=7/7`, exit 0, at `--lands
  70db282d… --freeze 08e4fb31…` (`telemetry/lands-d-graded-r2.txt`). Gap
  discipline: the topic-line sweep at base returns 5 files, all under
  `civilizations/` (single-tradition notes) — named in the entry's gap cell
  and pointed one-way in its §1; the entry owns no wayfinding (that stays
  polynesia-navigation's).
- **Junk landings (QUALITY 26b shape, post-landing):** six junk commits —
  old tool at lands (TOOL), replace refusal stubbed (TOOL+REPLACE), claims
  shrunk in the graded tree (FROZENCFG), entry deleted (ENTRY), table-row
  S-id mutant (LINT), S899 status flipped (ROWS) — each FAILs on its named
  leg (`telemetry/junk-landings.txt`, generator
  `counters/junk-fixtures.py`, run against a checkout-free plumbing clone;
  the battery's own red evidence for the ROWS leg is the first graded run at
  `66af0530`, `telemetry/lands-d-graded.txt`).
- **REJECTED (carried): naming-systems expansion** — reviewed and not
  admitted in r77, upheld r78, upheld r79; no new evidence this round.
- **REJECTED (carried): dining/tableware knowledge entry** — ground already
  held (r79 Gate); unchanged.
- **Freshness (historically the lowest non-retired axis): paused** by the
  unresolved round-11 L0 question — operator ruling, same disposition as
  rounds 77/78/79. The SCORECARD carries no saturation line/window, so the
  stagnation nudge is not invoked; the pause is the recorded reason no
  freshness move was declared.
- **Append-only corrections (carry-in):** the three wording defects routed by
  the round-79 spot-check are corrected in
  `reports/round-80/corrections/r80-annotations.md` and a `## Corrections —
  round 80` section appended to `corpus/lessons/round-79.md`; no filed bytes
  rewritten.

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R80-M1 | provider (Windows) — text-mode writes corrupt byte-pinned fixture artifacts; the R79-M2 class recurred at three NEW write sites in one round: (a) accept-d's selftest fixture copied `tools/check-cited-lines.py` through `open(..., "w")` → CRLF → sha mismatch against the frozen pin, so the LINT leg was red for the wrong reason in the selftest; (b) the junk battery's `.git/objects/info/alternates` got a trailing CR (git read the object directory as `…objects?`); (c) the battery's first clone design died outright on the R79-M3 uncheckoutable `>` paths at checkout and again at `read-tree` under `core.protectNTFS` | `reports/round-80/telemetry/selftests-o-d-freeze.txt` (the first selftest receipt shows the scenario flagged BAD before the LF fix); the junk battery's failed receipts were superseded in-place before any commit — the committed `telemetry/junk-landings.txt` is the passing run of the plumbing-only design | the selftest's own scenario check (`missing=['LEG PASS LINT']`); the battery's assertion errors | all fixture writes pin `newline="\n"` (or `newline=""` for git meta-files); the junk battery uses a checkout-free plumbing clone (bare init + fetch + alternates wrapper + `read-tree`/`update-index`/`commit-tree`, `core.protectNTFS=false` on the throwaway wrapper) so no worktree is ever materialized. Class note: the LF discipline is per-write-site, not per-project — every new fixture writer must re-earn it |
| R80-M2 | measurement — a counter crash prints nothing greppable: `accept-o.py`'s NOSTUB fixture env carried `GIT_AUTHOR_*` but no `GIT_COMMITTER_*`, git refused the fixture commit (`Committer identity unknown`), and the `CalledProcessError` — not a `GitFail` — escaped the leg's `except` clause, so the first graded run at lands `c365f6ce` exited 1 with ZERO leg lines | `reports/round-80/telemetry/lands-o-graded.txt` (the crashed run's complete output, committed as the fix's red-before); fixed counter r2 sha `6a5e76c3…` (r1 `8cdee013…` pinned in the freeze receipt) | the empty receipt itself (no `LEG ` lines = not a receipt per QUALITY 19) | committer identity added to the fixture env; revision recorded with selftest re-run (`telemetry/selftest-o-r2-nostubfix.txt`, `SELFTEST-O80: PASS`, no predicate moved); the r2 graded run prints all 10 legs and PASSes |
| R80-M3 | measurement hygiene — a shell loop's `echo "$(basename $f …) -> exit=$?"` ran command substitution before `"$?"`, so every refusal fixture appeared to exit 0; the defect was in the measurement harness, not the tool | round-80 working notes (superseded); the verbose re-run showed every fixture refusing correctly with `exit=2` | verbose re-run of the same fixtures outside the loop | capture `rc=$?` on the line immediately after the command, before any substitution; the committed fixture receipts (`junk-landings.txt`, counter receipts) carry per-fixture verdict lines from the counters themselves, not from shell `$?` |
| R80-M4 | landing geometry — the junk battery's first draft built the O-side junk commits on top of the claim-D lands, outside claim O's separable window: JO3's `SEPARABLE` leg FAILed on the corpus paths lands-D had added (they are not in O's carve-outs), a fixture-geometry defect that would have graded O against a lands it never declared | `reports/round-80/telemetry/junk-landings.txt` first draft (superseded in scratch before commit; the committed run builds O junk on `--lands-o c365f6ce`) | the battery's own SEPARABLE FAIL line on JO3 | the generator takes `--lands-o` and `--lands` separately: each claim's junk commits build on that claim's own lands commit, mirroring QUALITY 7's separable windows |

## Sources & frontier

Registry rows 821 → 824 (S898, S899, S900 opened this round; no prior-row
cell changed). Counting: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` = 824 (at the claim-D lands; 821 at base `a8aaece`).
Census receipts: `reports/round-80/telemetry/census-start.txt` (exit 0,
warnings W01/W04 only, same profile as r79) and `census-end.txt` (exit 0).
Knowledge files 253 → 254
(`git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'`).
Sourced claim: D rests on S898/S899/S900 (opened this round). S897's
annotation defects (host spelling, miscount) are corrected append-only; see
the Corrections section in `corpus/lessons/round-79.md`.
