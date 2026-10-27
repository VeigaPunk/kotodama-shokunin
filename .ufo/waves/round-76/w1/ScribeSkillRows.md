# ScribeSkillRows — round 76 / w1 (hyaku run 10)

Verdict: **DRAFTED, not installed.** The two round-76 gate-registry rows, the SHONEN.md:6 registry
summary edit text and the `SKILL.md:707` pre-freeze-sha repair are staged at
`.ufo/waves/round-76/w1/drafts/skill-rows.md` (lane-relative, 17,998 bytes at hand-off). Nothing in `SKILL.md`,
`SHONEN.md`, `reports/**`, the fleet repo or `/home/vgpnk/Projects/shokuknow` was written. `SKILL.md:707`
itself was not edited — only its replacement text is staged, because the lane's protected files are the
L1's at the freeze.

Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `98c486bdb4650ba5b8e651d332910e8ee60ad121`.
Scratch `/fast/scratch/hyaku/kotodama-r76/ScribeSkillRows/`, deleted at exit; the raw probe receipt is
copied to `.ufo/waves/round-76/w1/stage/ScribeSkillRows/sha-and-count-probe.txt` (40 lines).

## 1. What the draft contains

1. `accept-c-76` and `accept-ca-76` as eight-cell rows for the gate/probe table whose header is
   `SKILL.md:648` — `| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |`
   — to be inserted after the `accept-ca-75` row (`:708`) and before the `accept-c-73 / accept-ca-73
   correction` note row (`:709`). Verified placement anchors: the header is `SKILL.md:648` —
   `git show 98c486b:SKILL.md | sed -n '648p'` → `| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |`;
   the round-75 rows are `:707`/`:708` and the note row is `:709` — `git -C … grep -n 'accept-c-75\|accept-ca-75' 98c486b -- SKILL.md`
   → `98c486b…:SKILL.md:707:` / `98c486b…:SKILL.md:708:`.
2. The Ca row prints the FULL measuring command including `--combined <C-lands 40-hex>` and states the
   pinned-main requirement (the lane's local `main` pinned to the `--lands` revision, else
   `# measured revision (lane main)` diverges). The requirement is read off the round-75 counter:
   `accept-ca.py:2736-2747` resolves `measured` from `main_branch`; `_pin_main_plain` (`:2155-2160`) is what
   the RECEIPTS leg does to its clone. The routed round-75 defect is `corpus/lessons/round-75-verifier-spotcheck.md:124`
   — "Claim-Ca published command lacks `--combined` and the pinned main" — and `corpus/lessons/round-75.md:452-453`.
3. The row cells carry `<AT-INSTALL: …>` placeholders **only** for the selftest count and the counter
   sha256, both of which exist only after landing; draft §1 carries the placeholders and draft §5 item 3 names the command that fills them.
   Every other token is either contract (from `spec.json` items `ExecAdaptC`/`ExecAdaptCa` and the draft
   claims) or inherited from round-75 bytes; the draft's §0 table marks which is which.
4. SHONEN.md:6 edit text (see §3 below) and the `SKILL.md:707` repair (see §2 below).

## 2. The `SKILL.md:707` sha defect — which hash is which

- `315c5f3f27fd36b7ee92cb5bff9c34c27a5013e28218d9481ee7f74b5c7ce261` is the **committed** counter. Three
  independent derivations agree: `sha256sum reports/round-75/accept-c.py` → `315c5f3f…ce261`;
  `git show 98c486b:reports/round-75/accept-c.py | sha256sum` → `315c5f3f…ce261`; and a fresh reassembly
  from `.ufo/waves/round-75/w2/parts/*.py` via `.ufo/waves/round-75/w2/assemble.sh` →
  `315c5f3f…ce261` with `cmp -s` → `IDENTICAL_TO_COMMITTED`. History holds no other bytes at that path:
  one revision keyed it —
  `for rev in $(git rev-list --all -- reports/round-75/accept-c.py); do …; done` → `11d4413e7739… 315c5f3f…ce261`.
- `fa5060b91bdb6e76947aa7a0daab6d037b40a3be9f978e257783c7180c314d3f` is a **pre-freeze stamp**, not a
  hash of any byte in the repo. It is written in `reports/round-75/telemetry/selftest-c.txt:2`
  (`# counter sha256 fa5060b9…`, whose line 1 says "before the freeze") and repeated in `SKILL.md:707` in
  abbreviated form. Sweeps: `find . -path ./.git -prune -o -type f -print0 | xargs -0 sha256sum | grep -c '^fa5060b91bdb'`
  → `0` — no file in the lane working tree hashes to it; `grep -rl <full 64-hex> . --exclude-dir=.git` →
  `./reports/round-75/telemetry/selftest-c.txt` plus this seat's draft (which quotes it). So the row's
  citation names bytes that exist in no commit.
- The repair text replaces the unique substring
  ``Measured 2026-10-27 at counter sha256 `fa5060b91bdb…`: `SELFTEST: 85/85`, exit 0 (…; receipt `reports/round-75/telemetry/selftest-c.txt`).``
  — verified present exactly once (`old in line` → `True`, `line.count(old)` → `1`) — with the same
  sentence stamped `315c5f3f27fd…` and a clause that names the stale receipt honestly. The `85/85` figure
  is not re-measured by this seat; it cites the round-75 re-run at the landed bytes
  (`.ufo/waves/round-75/w3/ExecRerunBoth.md` §3: "`accept-c.py --selftest` → `SELFTEST: 85/85`, exit 0 …
  it reports `315c5f3f…ce261`, the frozen hash"). Marked **unrun here**.

## 3. SHONEN.md:6 — the edit text and its append-only constraint

Line 6 is the `asserted:` continuation of the SKILL bullet (643 characters —
`awk 'NR==6{print length($0)}' SHONEN.md` → `643`) and carries the round-75 registry summary
(rows 808/mined 713 at the round-75 Ca landing; 817/722 at the round-75 close). The four live numbers are
re-derived at base and match the draft claim's before-state: `817` rows — `git show 98c486b:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`;
`mined 722`, `queued 58`, `rejected 37` — per-status `grep -cE` on the same blob; `252` knowledge `.md`
files — `git ls-tree -r --name-only 98c486b corpus/knowledge | grep -c '\.md$'`; and the round-76 census
start closes clean — `tail -1 reports/round-76/telemetry/census-start.txt` → `exit=0`.

The draft gives the replacement parenthetical (`rows: 817 … 817+k rows / 722+k mined`, with
`k = distinct documents newly cited by the n>=2 admitted candidate entries`) **and** an append-only
fallback, because the Ca counter's APPENDONLY leg accepts a changed line only when it is a REPAIR pair's
`stated_at` line or an appended line (`accept-ca.py:59-68` leg text; the appended-line rule is `:63-64`). Consequence the L1 must respect:
if the frozen `reports/round-76/ledger.json` has no REPAIR pair on `SHONEN.md` line 6, an in-place rewrite
of that line is an undeclared edit and APPENDONLY would fail — use the appended-line form. If it has such
a pair, apply that pair's `statement_after` byte for byte (only one edit to the line). `reports/round-76/ledger.json`
does not exist yet at base, so this is a real fork, not a hypothetical.

## 4. Behaviour this seat exercised

- Read-only git (`show`, `rev-list`, `ls-tree`, `grep`) at `98c486b`; no git mutation anywhere; no fixture
  repo created (none was needed — no git command wrote).
- `sh .ufo/waves/round-75/w2/assemble.sh <scratch>/assembled-c.py` run once with `HYAKU_SCRATCH` pointing
  at the seat scratch dir; it wrote only under that scratch dir (`py_compile` cache included).
- `find … | xargs sha256sum` over the lane working tree: 129 MB `.git` excluded by `-prune`; 0 matches.
- Nothing else executed: no counter run, no `--selftest` run, no `chromium`/network fetch, no pacman.

## 5. Gates stated in the staged rows (contract, not measured)

`ACCEPT-C-76` = 13 legs, `ACCEPT-CA-76` = 12 legs, verdict lines `PASS legs=13/13` / `PASS legs=12/12`,
refusals `FAIL legs=0/<n> (refused: …)` exit 2, input errors `ERROR: …` exit 2 — all from the counter
contract in `.ufo/waves/round-76/w1/spec.json` (`ExecAdaptC`: "Keep the leg set (ENTRIES, ROWS, REPOINTED,
GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK, FROZENCFG, INDEX)";
`ExecAdaptCa`: "claim-Ca.json (…, legs[12])" and "make a missing flag a REFUSAL (exit 2) not a leg FAIL").
The twelve round-75 Ca leg names were read off `accept-ca.py:241-243` (`REQUIRED_LEGS`) so the row states
them; the round-76 counter must either match them or refuse under its own LEGCOUNT, which is what makes the
row self-falsifying rather than decorative.

Inherited-and-to-reconfirm (flagged in draft §0): the refusal/ERROR enumerations, `--lands == --freeze`
graded-not-refused (C), `freeze == lands` all-green refusal (Ca), and "a `--freeze` off the lands
first-parent chain is a FROZENCFG leg FAIL, not a refusal" (`accept-ca.py:2585-2596`, `problems.append`,
not `_refuse`).

## 6. Findings

- **F1 (the assigned defect, confirmed).** `SKILL.md:707` cites counter sha `fa5060b9…`, bytes that exist
  in no commit; the committed counter is `315c5f3f…` (§2). Repair text staged; not installed.
- **F2 (new, install blocker).** The SHONEN.md:6 rewrite is only legal if the frozen Ca ledger declares a
  REPAIR pair on that line; otherwise it must be an appended line (§3). The draft carries both forms; an
  in-place rewrite chosen without checking the ledger fails APPENDONLY.
- **F3 (new, row correctness).** Round-75's Ca row said "COMBINED needs `--combined`" but did not say what
  a missing flag produces: `accept-ca.py:2550-2552` returns a **leg FAIL**, which the verifier routed as a
  false red claim (`round-75-verifier-spotcheck.md:76`: prints `FAIL legs=11/12`). The round-76 row states
  the refusal explicitly and the claim text must show the full command; if the landed counter keeps the leg
  FAIL, the row is wrong and must be corrected against the counter.
- **F4 (scope note).** The two new rows cannot be measured before landing: `git ls-tree 98c486b reports/round-76/`
  prints nothing, so at base there is no `reports/round-76/accept-c.py`, `accept-ca.py`, `claims.json` or
  `ledger.json`. The only measured artefacts in this draft are the round-75 hashes/counts of §2-§3 and the
  numeric before-state of §3.
- **F5 (carry-over, not repaired here).** The round-75 receipt `selftest-c.txt` keeps its pre-freeze stamp;
  the draft proposes an ANNOTATE row rather than editing round-75 evidence, since `reports/round-75/**` is
  outside every seat's write scope this round.
- **F6 (new, row-vs-counter reconciliation).** The scratch rules now collide: round 76 must "honour
  `--work`/`$TMPDIR`/`$HYAKU_SCRATCH`" while round 75 refuses a root that is (inside) the system temporary
  directory — and `_forbidden_scratch` (`accept-c.py:6021-6028`) bans `tempfile.gettempdir()` itself, which
  *is* `$TMPDIR` when it is set. A naive adaptation therefore refuses its own documented fallback. The staged
  rows say `/tmp` (the literal) and honour a non-`/tmp` `$TMPDIR`; the landed counter must match, else the
  row is corrected to the counter at install. Also noted: the counter's message text says "QUALITY 14", but
  `corpus/QUALITY.md:45` (item 14) is the judged-object criterion — the scratch rule lives in prompt §7.4;
  the rows quote the counter's token verbatim rather than re-citing the wrong item.

## 7. Touched surfaces

Written (all lane-relative, all under `.ufo/waves/round-76/w1/`): `drafts/skill-rows.md` (the staged
rows / SHONEN text / `:707` repair); `stage/ScribeSkillRows/sha-and-count-probe.txt` (raw probe receipt);
`ScribeSkillRows.md` (this report).
Scratch `/fast/scratch/hyaku/kotodama-r76/ScribeSkillRows/` used and removed.
Read only: the lane worktree + git at `98c486b`, `.ufo/waves/round-75/**`, and two read-only probes of the
fleet tree — `git -C /home/vgpnk/Projects/shokunin status --porcelain` (its pre-existing `M`/`??` entries are
not this seat's) and `ls /home/vgpnk/Projects/shokunin/.ufo`. The fleet `scripts/` directory was not opened. Not touched: fleet repo, `scripts/`, `templates/`, `.ufo/state`,
`.ufo/watchdog.log`, `LOG.md`, `SCORECARD.md`, `SKILL.md`, `SHONEN.md`, `corpus/**`, `reports/**`,
`shokuknow/**`, sibling lanes, the git index.

## 8. Out of scope / not run

No install or upgrade (nothing needed; no tool recorded). No counter run, no selftest, no control matrix,
no network fetch, no source opening. The suite of install-time checks (row shape, cell count, counter
selftests, `/tmp` grep, Ca graded command with and without `--combined`) is written as a checklist in draft
§5 and left unrun — the L1 runs them once after all wave-1 seats land.
