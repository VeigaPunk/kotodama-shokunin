# ScribeLesson — round 79 W1 pre-data recon report

Seat: ScribeLesson (leaf, W1). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base `44f76d456c1b326a71ffdb381590af825cbf11be` = HEAD at observation (`git rev-parse HEAD`). Date of observation: 2026-10-30.

Stage (own files only): `.ufo/waves/round-79/w1/stage/ScribeLesson/`
- `lesson-round-79.draft.md` — Gate, Mistakes, pending-vs-observed table, Trends, routed list.
- `s897-row.draft.md` — own-work registry row, quote, cell rationale, shape check.
- `used-by-plan.draft.md` — planned used-by and tool registry map (TBD where L1 must choose).
- `receipts/` — `observation-receipt.txt`, `census-validate-head.txt`, `dining-retest.txt`, `validate-base-file.txt`, `validate-fixture-with-S897.txt`, `SOURCES.fixture-with-S897.md`, `SHA256SUMS.txt`.

## 1. Mission items

### 1a. R78 routed defect 2 — census-end S884 token (`[OBSERVED]`)

Source: `corpus/lessons/round-78-verifier-spotcheck.md:67`.

| receipt / registry | line | S884 used-by token |
|---|---|---|
| `reports/round-78/telemetry/census-start.txt` | 33 | `…worldbuilding-setting-practice.amend-2026-10-23.md` |
| `reports/round-78/telemetry/census-end.txt` (committed `4b255745`, sha256 `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867`) | 33 | `…worldbuilding-setting-practice.amend-2026-10-24-r13.md` |
| `corpus/SOURCES.md` S884 row, field 12 (at `4b255745` and at HEAD `44f76d45`) | 839 | `…worldbuilding-setting-practice.amend-2026-10-23.md` |
| `census validate` re-run at HEAD (this seat, `census-validate-head.txt`) | — | `…amend-2026-10-23.md`, exit 0 |

- The `…24-r13.md` token exists in no path in the lane history for this entry. `git log --all --name-only` finds the worldbuilding amend only as `…amend-2026-10-23.md`. The only `24-r13` amend in history is `corpus/knowledge/culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md` (round-72 assimilation). `[INFERENCE]` The census-end token is a stem/suffix splice from that other entry's filename; not verified against a generator.
- `census-end.txt` carries no revision stamp and no tree hash (QUALITY criterion 17). The receipt is committed bytes, so the lesson records it as a defect of the evidence record, not as a registry change.
- Correction shape (for L1; not written here): append-only Ca-style record binding the sha256 above, the measured revision, old token and actual token; frozen counter re-derives mismatch 1 at base → 0 after correction; do-nothing, lying correction, wrong revision and changed receipt must fail. `[PENDING-TOOL-PROOF]`

### 1b. R78 routed defect 3 — R78-M1 fix not demonstrated able-to-fail (`[OBSERVED]` pointer error)

- `corpus/lessons/round-78.md:11` (R78-M1) cites `.ufo/waves/round-77/w2/ExecCaPass.md:24-34` for the red evidence. Lines 24-34 are the verdict header of that file (lines 15-32). The BASEMISMATCH failure is at `ExecCaPass.md:265-278` and in the receipt `.ufo/waves/round-77/w2/stage/ExecCaPass/graded-legs.txt:1-6`.
- R78-M1 also cites `MutCaLedger.md:43-84`. That range holds the D07 `HEAD` survivor (row e1 at `:53`, analysis `:58-88`), a different finding.
- The R78-M1 fix (store the observed token from the exact pinned-base command; refuse stated == observed) is not implemented: `accept-ca.py` checks only the type of `observed_at_base` (`:1712-1714`); the comparison exists only in the BASEMISMATCH leg (`:1866`). W2 named the fix as advisory. Red-before for the fix is `[PENDING-TOOL-PROOF]`.

### 1c. Exact R77 BASEMISMATCH red evidence (`[OBSERVED]`)

Primary artifacts (committed, tracked at HEAD):

| artifact | lines | content |
|---|---|---|
| `.ufo/waves/round-77/w2/stage/ExecCaPass/graded-legs.txt` (sha256 `6e97b121e98120f7d5fa6378f7cb5eebe6f8e0c520e90bd7c13503b3e124e52b`) | 1-6 | `LEG FAIL BASEMISMATCH`; `red=10 min=10 … green-at-base=['D11'] unobserved/miss=[D01…D10 recorded-observed-at-base='1'!='149']`; `BASEMISMATCH_PASSED=False`; `LEG FAIL REPAIR` with `green=[] red=["D11(statement='253' truth='243')"]`; `REPAIR_PASSED=False` |
| `.ufo/waves/round-77/w2/ExecCaPass.md` (report) | 265-278 (§5.2), 196-216 (§5.1), 189 (V02) | same leg output in prose and the counter's own graded legs |
| `.ufo/waves/round-77/w2/stage/ExecCaPass/token-evidence.txt` | 1-12 | counter-function table: D01–D10 `observed='149' recorded_ob='1'`; `RED_AT_BASE 10/11` |
| `.ufo/waves/round-77/w2/ScoutLogPairs.md` | 45-57 (table), 64-80 (mechanism), 107-175 (raw) | independent base re-derivation; `grep -c '^#'` = 149 |
| `.ufo/waves/round-77/w2/stage/ExecCaPass/controls-summary.txt` | 83 | `V02-fabricated-observation rc=0 want=0 OK` (fabricated `"999"` passes `--ledger-check`) |
| probe ledger `.ufo/waves/round-77/w2/stage/ExecCaPass/ledger.json` = W1 `probe-real-ledger.json` | — | sha256 `b7509d2b0980f8c5824c417a8359c8f7107d3de6236cf486ac058947915d0704` |

Re-observed by this seat (read-only, base `211f9526800906e0c585d878d265c37e5e090c15` exists as a commit): `git show 211f9526:LOG.md | grep -c '^#'` = `149`; `corpus/README.md` totals `243 (:755)`, `247 (:798)`, `249 (:819)`, `252 (:830)`, `253 (:834)`.

Scope of the red (stated): the W2 run was in-process with lands = base; it shows the counter's leg functions over the probe, not a committed freeze run. The BASEMISMATCH half reads base only. Round-77 `--ledger-check` still returns `PASS pairs=11` (ExecCaPass §3), so build-check PASS and leg FAIL coexist on the same bytes.

### 1d. Dining / tableware candidate — REJECTED, already held (`[OBSERVED]`)

- `corpus/knowledge/culture-material/cuisine-food-lexicon.md:90` `## 6. Etiquette: the table as grammar` (table manners, chopstick grammar, commensality; `:90-93` as the claim draft says).
- `corpus/knowledge/culture-material/furniture-interior-lexicon.md:73` (dining table as boards on trestles) and `:99` (dining table and chair set).
- Verbatim re-test output: `receipts/dining-retest.txt`.
- No knowledge admission. The rejection is review-only for the overlap judgment (QUALITY 11); the grep is the measurable part (QUALITY 12).

### 1e. Own-work S897 draft row (`[OBSERVED]` shape, `[PENDING]` landing)

- Row text, cells, quote and rationale: `stage/ScribeLesson/s897-row.draft.md`.
- Quote (≤25 words, exact path and line): `.ufo/waves/round-77/w2/stage/ExecCaPass/graded-legs.txt:1` 「LEG FAIL BASEMISMATCH」 and `…graded-legs.txt:2` 「recorded-observed-at-base='1'!='149'」.
- Opened `2026-10-30`; kind `own-work`; tier A (precedent S859/S860; contract tier-A definition covers "the lane's own re-runnable gate output"); status `queued`; used-by `—` until the lesson lands (census E11 would fail a missing path); recheck `on-change`.
- Shape check: scratch `--file` validation, base vs with-row: rc 0 both, no E-codes, rows 820 → 821, `tier.A` 493 → 494, `queued` 58 → 59, no findings naming S897. Root-mode validation after landing is `[PENDING-TOOL-PROOF]`.

### 1f. Used-by planned lesson / tool registry

See `stage/ScribeLesson/used-by-plan.draft.md`. Summary: lesson `corpus/lessons/round-79.md` (absent, `[OBSERVED]`); O guard tool path and Ca correction record path are not named in `CLAIMS-DRAFT.md`, so they are TBD by L1, not invented.

## 2. Ca disposition (pre-freeze, observed)

- `[OBSERVED]` No SCORECARD / SHONEN statement names the S884 used-by token or `census-end.txt`. `SCORECARD.md:1480` mentions `S884` only as the round-74 evidence path for a quote. Under `CLAIMS-DRAFT.md`'s "Pre-freeze scope disposition", Ca is therefore rejected as a claim before freeze unless L1 finds a corresponding self-assessment row; its correction lands as unclaimed conformance repair. This is a recommendation for L1; the freeze decision is L1's.

## 3. Verification status

| item | status |
|---|---|
| R77 BASEMISMATCH red present, exact lines | `[OBSERVED]` |
| Base counts 149 and 243/247/249/252/253 | `[OBSERVED]` (this seat) |
| S884 token mismatch at HEAD and in committed census-end | `[OBSERVED]` |
| `…24-r13` token origin in another entry | `[INFERENCE]` (name match only) |
| Dining holds | `[OBSERVED]` (grep output) |
| S897 row shape | `[OBSERVED]` in scratch fixture |
| Fix for R78-M1 is able-to-fail | `[PENDING-TOOL-PROOF]` |
| Ca correction turns mismatch 1 → 0 under a frozen counter | `[PENDING-TOOL-PROOF]` |
| O guard behaviour | `[PENDING-TOOL-PROOF]` (no code this seat) |

Not run: any build, lint, test, selftest, counter, or `--ledger-check`. The graded legs were not re-executed; their receipts were read and hashed.

## 4. Host, tool and scope record

- Reads: `RULES.md`, the godspeed skill, round-79 CLAIMS-DRAFT and spec, QUALITY.md criteria 6–28, round-77 and round-78 lessons and spot-checks, round-77 W1/W2 reports and receipts, SOURCES.md, SCORECARD/LOG/SHONEN (grep), corpus lexicons, `scripts/sources-census.sh` (read-only, `census` and `validate` modes).
- Git: read-only only (`cat-file`, `show`, `log`, `ls-files`, `status`, `rev-parse`). No commit, add, checkout, reset, push or clone. Lane `git status --porcelain` after work: only the pre-existing `?? .ufo/waves/round-79/` and `?? reports/round-79/` (not written by this seat) plus this seat's own stage files.
- Scratch: `/fast/scratch/hyaku/kotodama-r79/ScribeLesson/` created explicitly; read-only symlinks in a fixture to the lane's `corpus/knowledge`, `corpus/lessons`, `SKILL.md`, `reports`; copies of receipts made; scratch removed (symlinks unlinked before removal; targets verified intact).
- Tool installs: none. `pacman` not invoked. No `~/.local/bin` or PATH changes. No host service changes.
- Delegation: none (leaf seat). No model parameters set.
- Files written by this seat: `.ufo/waves/round-79/w1/ScribeLesson.md` and `.ufo/waves/round-79/w1/stage/ScribeLesson/**` only.

## 5. Checks the main agent should run (not run here)

1. After landing S897 with the lesson: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit 0, `kotodama ok`; W01 for S884 remains until the Ca correction lands.
2. The S897 row's sha256 and anchor lines against `graded-legs.txt` before flipping `queued` → `mined`.
3. The R78-M1 pointer correction and any fix proof: red-before on a committed fixture, not on the probe copy.

Report: .ufo/waves/round-79/w1/ScribeLesson.md
