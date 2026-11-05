# kotodama round-93 — verifier spot-check

author: hyaku closure (non-author integrator, @m_zfl)

Round: kotodama round 93, attempt 1. Base `8b2ce60a7bbf015f42a6c9e5c45e994e4c2f7742`, freeze `174fd5a8e05b3919a7854a4495c2fe0f28080775` (rev 2), lands `95e7a5cff1687b21d982607ab0bfd8e381c3036c`, lane tip `80614d0f30f20791dc47a95ad9437088a00e4fce`. Report: `.ufo/reports/round-93/kotodama.md` (fleet commit `1859920c`, author `kotodama-shokunin <kotodama@shokunin.local>`, committer date 2026-11-05 13:23:28 -03:00 — after the lane tip 13:22:44, before the driver complete line 13:23:52, so commit-before-report ordering holds).

## 1. Conformance results

| check | result |
|---|---|
| report committed in fleet repo by lane identity | PASS — `git log --format='%an %H' -- .ufo/reports/round-93/kotodama.md` → `kotodama-shokunin <kotodama@shokunin.local> 1859920c` |
| `SHONEN` heading, one line per box | PASS — 4 `[~]` lines for the 4 canonical boxes; no `[x]`; report itself states no non-author verifier checked a box |
| every cited lane commit exists and is an ancestor of the branch ref | PASS — `8b2ce60a`, `80614d0f`, `174fd5a8`, `95e7a5cf`, `3c81f922`, `1928e00d`, `9778ccc2`, `1473606b` all `git merge-base --is-ancestor <h> refs/heads/main` true (jj-colocated; tested against the branch ref, not `@{u}`) |
| no uncommitted round work; pushed | PASS — `jj-lane.sh state` → `local=80614d0f remote=80614d0f ahead=0 behind=0 tracked=0 untracked=0`; `git status --porcelain` empty |
| prompt carries the template contract | PASS — `.ufo/prompts/kotodama-round-93.md` (committed `23069d2c`) renders `templates/round-prompt.md` verbatim (lane/round/root substituted) plus hyaku addendum §6; all five child-lane items and the round-level items present; no L2 route map quoted, so no MISSION bucket mismatch to check |
| dispatch/complete digest | PASS — watchdog.log lines 2855 (`2026-11-05T11:12:49-03:00 launch kotodama round=93 pgid=1186363 driver=hyaku-inline attempt=1`) and 2878 (`2026-11-05T13:23:52-03:00 complete kotodama round=93; hyaku-inline attempt=1`) match the digest copied into the closure notes |
| report marker predicate | PASS — real report: named claims, evidence pointers, landed-changes table with hashes, measurements, Sources & frontier, trend verdicts, SHONEN |
| wave evidence durable | PASS — `.ufo/waves/round-93/w1-*` committed in the lane repo at `80614d0f` (this fleet's convention: child lanes carry wave evidence in their own repos) |
| LOG.md round-93 entry | PASS — appended entry naming claims, freeze, lands, receipts |

## 2. Per-claim re-check

### Claim O — operability (evidence-verified, lane gate NOT executed)

The claim rests on the lane's own grader/selftest, so per PROTOCOL §Gate standard (Closure consequence) I verified its committed evidence and never ran the sibling's gate.

- Tool identity: `git show 95e7a5cf:tools/check-advance-evidence.py | sha256sum` → `9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7` — matches `claims.json` and the frozen TOOL leg; base tool re-hashes to `905be2fe…` as declared.
- Frozen receipt `reports/round-93/final/lands-O.txt`: header pins stamped/evaluated/measured revision `95e7a5cf`, tree `f048b0bd`; `MEASURE93-O: PASS legs=10/10`; SELFTEST leg records `SELFTEST PASS 114/114` with OKCOUNT 114 ok lines; STABILITY 4 concurrent runs rc 0; REFUSALS 25 named cases; MUTATION `83/83 killed, 0 survived` with receipt `reports/round-93/mutation-score.txt` (tail confirms `KILLED …` rows); BATTERY 26 attacks, survivors=A1, named-refusals=25, unnamed=0.
- Revision measured: the lands receipt names the lands revision and the counter sha `fb3ca1c2…`; the mutation receipt names the live tool sha (MUTRECEIPT PASS in the same receipt).
- Red-before preserved: `reports/round-93/controls/v3-base-counterfeits.txt` header `observed: 16 SURVIVORS rc=0 (… A6g-unnamed-crash rc=1)` — exactly the reported 16 survivors + 1 unnamed traceback; Totals line confirms `SURVIVORS 16; refused 5 (unnamed 1)`.
- Do-nothing controls: `controls/O-base-refusal.txt` and `controls/C-base-refusal.txt` show the counter refuses `--lands <base>` (`MEASURE93_ERROR: … a do-nothing landing cannot pass`); `controls/C-freeze-rev2.txt` shows claim C failing at the freeze on ENTRY and APPENDONLY before the entry landed, as declared.
- Freeze discipline: `reports/round-93/claims.json` at `174fd5a8` declares both claims and legs; `counter-revisions.md` documents the rev1→rev2 change (census leg path) as made before data.

Verdict: **improved** — the committed evidence is internally consistent and pins the measured revision.

### Claim C — coverage (re-measured by me, plain commands over committed bytes)

| measure | command (at `8b2ce60a` / `95e7a5cf`) | observed | reported | match |
|---|---|---|---|---|
| greeting/leave-taking filename owners | `git ls-tree -r --name-only <rev> corpus/knowledge \| grep -ci greet` | 0 → 1 (`greeting-leave-taking-formulae.md`) | 0 → 1 | YES |
| linguistics files | `git ls-tree -r --name-only <rev> corpus/knowledge/linguistics \| wc -l` | 37 → 38 | 37 → 38 | YES |
| registry rows | `git show <rev>:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | 884 → 888 | 884 → 888 | YES |
| tier-A rows (any status) | awk tier cell == A | 522 → 526 | 522 → 526 (labelled "mined A rows" in the report table) | YES (values) |
| mined rows (any tier) | awk status cell == mined | 777 → 781 | 777 → 781 (SCORECARD) | YES |
| entry size | `wc -c corpus/knowledge/linguistics/greeting-leave-taking-formulae.md` | 21043 | 21043 | YES |
| SOURCES.md append-only | `git diff --numstat base lands -- corpus/SOURCES.md` | `6 0` (4 rows + search-log note; no base row touched) | rows + note only | YES |
| README index row | `grep greeting-leave-taking corpus/README.md` | line 357 present | INDEX leg PASS | YES |
| census | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` | rc 0; only pre-existing W04 (duplicate URLs across scopes) and W01 (tierC mined) findings, none on S961–S964 | rc 0 at lands | YES |
| counter receipt | `reports/round-93/final/lands-C.txt` | `MEASURE93-C: PASS legs=6/6`; POSITIVE leg: v4 grades the round-92 landed entry `1473606b` 9/9 | PASS 6/6 | YES |

Defect (label only, status-neutral): the report's before→after table row "mined A rows 522 → 526" carries tier-A-any-status values; actual mined-A counts are 466 → 470 and mined-any is 777 → 781 (the SCORECARD row labels the same numbers correctly as "A 522 → 526, mined 777 → 781"). Delta +4 either way; the four new rows are tier A, status mined, opened 2026-11-05, cited by the entry. Claim C verifies; only the report-table label is wrong (an erratum for the round-94 report).

Verdict: **improved**.

## 3. Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| operability | improved | claim O evidence-verified (above) |
| coverage | improved | claim C re-measured (above) |
| depth | unchanged | no admitted entry re-verified, deepened or superseded this round (SCORECARD row and report agree); no entry found stale-unmarked |
| freshness | unchanged | paused by open L0 kotodama round-11/round-89, disclosed; no freshness claim made |
| calibration | unchanged | observation only (round-92 routed items → QUALITY 37 + round-94 routes); no scored claim, no harm |
| adjacency | unchanged | ConnectorOverlap found dangling cross-references (`politeness-taboo-euphemism.md`), routed, not absorbed; SCORECARD diff is append-only |

No axis harmed: `git diff base tip -- SCORECARD.md` is +29 lines, append-only; no score decreased; no verdict in the round is a trade.

## 4. Discernment spot-check (LEARNING.md)

Sampled from `corpus/lessons/round-93.md` `## Gate`: 2 of 4 admits re-opened fresh (HTTP 200 on 2026-11-05, quotes located in the fresh bytes after HTML normalization), 2 of the not-row rejections re-opened (both recorded access failures reproduced). Plus all four committed capture digests re-hashed against `reports/round-93/evidence/manifest.json`.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S963 Mapunda & Sommer 2017 (Ngoni/Swahili greetings) | admit A/mined | `https://bop.unibe.ch/linguistik-online/article/view/3847` fresh fetch 200 + committed capture `reports/round-93/evidence/S963.html` (sha MATCH) | agree | quote "greetings tend to be brief today" located in fresh bytes and capture; teaches cell grounded (brevity; older speakers read the Swahili turn as lack of respect — RR-1 wording applied before landing) |
| S964 Trubnikova 2025 (Russian leave-taking) | admit A/mined | `https://oaj.fupress.net/index.php/ss/article/view/17732` fresh fetch 200 + committed capture S964.html (sha MATCH) | agree | quote "compiled a pool of words, expressions, and sayings" located fresh; teaches cell honestly scopes it as a pilot study, not a population sample |
| MDPI "Pragmatic Variation in Greeting and Farewell Formulae in Rural Austria" | not a row (unreachable) | `https://www.mdpi.com/2226-471X/11/9/179` fresh plain curl | agree | HTTP 403 reproduced to the plain request; no challenge passed; recording it unassessed-for-access rather than rejected is exactly the criterion-37 rule |
| Esan/àlago greeting ritual article | not a row (unreachable) | `https://univ-bejaia.dz/revue/jslcs/article/view/394` fresh plain curl | agree | TLS certificate verification failure reproduced (`unable to get local issuer certificate`), not bypassed; not a row is correct |

Gate agreement is 4/4 on the sample. Registry rows S961–S964 re-read at HEAD: 13-column rows, tier A scoped, anchors carry DOI/revision + opened 2026-11-05, status mined, used-by names the entry, quotes are 6–13 words and located in the captures — contract v1 conformant. Criterion 37 landed in `corpus/QUALITY.md` with its per-bullet sweep (observed 0 reason-less bullets over 31 exclusion bullets) and a red-before on the round-92 bytes (16 title-only exclusions in one prose paragraph) — the fix is shown able to fail.

## 5. Trend verdicts (non-author, agreeing with the report)

- **expansion: improved** — a dedicated admitted entry on ground with zero filename owners at base, citing four new mined A rows on uncovered coverage-map ground; census rc 0; README row present.
- **quality: unchanged** — no admitted entry was re-verified, deepened or superseded; no entry found false-or-stale-and-unmarked; the four re-opens cover only the new rows.
- **discernment: improved** — the round-92 closure disagreement became lesson R93-M2 and grounded QUALITY criterion 37 with red-before; my independent spot-check agrees with the gate on both sampled admits and both sampled rejects (LEARNING.md's improved condition: agreement, or disagreement-turned-criterion — both hold).

The spot-check axis table (§3) and the MANIFEST closure entry carry the same verdicts.

## 6. Routed defects the lane must fix in round 94

1. **Erratum owed:** the round-93 report's "mined A rows 522 → 526" table label vs values mismatch (values are tier-A-any-status; mined-any 777 → 781, mined-A 466 → 470). Fix as an append-only erratum in the round-94 report naming the round-93 text; never rewrite the filed bytes.
2. **Selftest pin gaps (MutationTesterV4, endorsed):** script/style strip, comment strip, entity unescape, disposition case rule, base-row `opened` identity cell — five surviving mutants with recipes in `corpus/lessons/round-93.md` `## Routed to round 94`; the shipped v4 performs each check, so these are pins, not counterfeit channels.
3. **CriticClaims93 counterfeits (endorsed):** A1 Cyrillic lookalike, B1 soft hyphen, G1 numbered phrase-only headings, H1 manifest list values, I1 short registry rows, J1 en-dash verdict token; plus the narrow lowercase-unanchored-verdict channel (dispo-any-casei). The frozen round-93 predicate does not claim these classes; round 94 must fix them against a new freeze without weakening v4 on any round-92/93 class.
4. **Dangling cross-references:** `culture-material/adornment-body-codes.md:5` and `costume-semiotics.md:143` point at the greeting domain; `politeness-taboo-euphemism.md` holds no greeting line — resolve or re-point in round 94.
5. **Open re-decisions:** the three round-92 re-decisions (Awetí 2015, Zulu Lexikos 2011, Turkish Signifiances 2020) and the 16 title-only exclusions under criterion 37; L0 kotodama round-92 overlap question (`ideophones-mimetics.md` vs `sound-symbolism.md` §6) still unanswered.

## 7. Operator note (promotion is operator-owned)

All four SHONEN boxes now have landed, non-author-checkable evidence (SKILL.md decision/error tables with cited sources; LOG round-93 end-to-end entry with a graded instrument; selftest 114/114 + mutation 83/83 receipts at `9799a96c`; PROVINCE accuracy via ConnectorOverlap with no sibling content absorbed). Nothing here is a promotion decision; the boxes remain `[~]` until the operator's reviewer marks them.
