author: hyaku closure (non-author integrator, @m_opus)

# Round 75 — kotodama: non-author closure spot-check

Lane `kotodama-shokunin`, lane-round 75, base `f556d1049fe651d3d63975600b13acd9fb686f15`, measured at lane tip
`f601f7f3c2132eb3b54020fc84626a66b75ddb72`. Dispatch digest (`.ufo/watchdog.log`, mutable, copied):

- 2026-10-27T13:29:20-03:00 launch kotodama round=75 pgid=2306172 driver=hyaku-inline attempt=1
- 2026-10-27T16:37:22-03:00 lane-dead-no-report kotodama round=75; retry same round (attempt 1 force-wrapped incomplete: 42-seat w1 only, no freeze, no report)
- 2026-10-27T16:37:25-03:00 launch kotodama round=75 pgid=2086915 driver=hyaku-inline attempt=2
- 2026-10-27T18:18:28-03:00 complete kotodama round=75; hyaku-inline attempt=2

I did not author the round. I re-measured by plain commands over committed bytes, re-opened sources over the network, and
verified the lane's gate evidence without executing it (PROTOCOL §Gate standard, Closure consequence).

## 1. Step-1 conformance

| check | command / observation | result |
|---|---|---|
| report committed by lane identity | `git log --format='%an %H' -- .ufo/reports/round-75/kotodama.md` → `kotodama-shokunin 15df0c2925c7…` | ok |
| `SHONEN` heading, one line per box | `grep -n '^## SHONEN'` → line 56; 4 `[~]` lines; `grep -cE '^- \[' SHONEN.md` → 4 boxes | ok, no `[x]` written |
| cited commits exist and are ancestors of `main` | `merge-base --is-ancestor` for 012e8d3, 4f5e3b2, 5d01674, 82ced5c, 15f3f8c, f556d10, f601f7f (short and full forms) | all ancestors |
| lane pushed, clean | `jj-lane.sh state` → `local=f601f7f… remote=f601f7f… ahead=0 behind=0 tracked=0 untracked=0`; `status --porcelain` empty; `ls-remote origin refs/heads/main` = `f601f7f3…` | ok |
| prompt carries template contract | `.ufo/prompts/kotodama-round-75.md` (658 lines): MISSION/AXES binding, claims rule, §2b frontier step, ≥8 L2 batched, commit/push scope (§5), L0 side channel, SHONEN heading, hash rule, write scope, hyaku addendum §6 | ok |
| report is real, not a marker | work performed, landed-change table tied to LOG `## Round 75`, hashes, before→after measurements | status `ok` |

Conformance defects (status-neutral): the lesson `corpus/lessons/round-75.md` opens with pre-freeze present-tense text
("no freeze commit exists", "claims are `DRAFT`") that `## Status at landing` supersedes by appended note, not rewrite
(permitted append-only handling, but the header misleads a first reader); one misrooted wave-1 seat file at the fleet root
was moved into the lane (`f601f7f`, R75-M4) — disclosed; a wave-2 seat `rm -rf`'d the round's shared scratch root —
disclosed; the report is committed as `15df0c2` while the lane tip it cites (`f601f7f`) predates it — correct ordering.

## 2. Claims — per-claim re-check

Re-measured = I ran a plain command and compared. Evidence-verified = I read committed gate evidence (selftest tally, control
runs, measured-at revision) and did not execute the gate.

### Claim C — coverage (narrative-structure-frameworks, sourced) — **improved** (re-measured + evidence-verified)

| measure | command (mine) | base | tip | reported |
|---|---|---|---|---|
| narrative-named knowledge files | `git ls-tree -r --name-only <rev> corpus/knowledge \| grep -ci narrative` | 0 | 3 (`myth-symbol/narrative-structure-frameworks{,.amend-2026-10-23,.amend-2026-10-23b}.md`) | 0 → 3 ✔ |
| knowledge `.md` files | `… \| grep -c '\.md$'` | 249 | 252 | 249 → 252 ✔ |
| registry rows | `git show <rev>:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | 808 | 817 (same at C landing `4f5e3b2`) | 808 → 817 ✔ |
| rows added by tier | awk over S885–S893 tier column | — | A 3, B 5, C 1 | A×3 B×5 C×1 ✔ |
| row status / used-by | awk over rows | — | all nine `mined`, each `used-by` a real entry path | ✔ |
| README index | tip `Total knowledge entries: 252`; 252 `- \`x.md\` —` rows; per-dir counts 32/32/40/29/24/95 = 252 | 247 index rows (footer 249 stood) | 252 | consistent ✔ |
| SOURCES append-only | `git diff --numstat` shows 0 deletions in `corpus/SOURCES.md` | — | — | ✔ |
| census | `sources-census.sh validate --root … kotodama` → exit 0 (W01 notes S881/S882/S884/S893 tier-C mined; W04 standing duplicate-url lines) | — | — | ✔ |

Evidence-verified: `telemetry/selftest-c.txt` `SELFTEST: 85/85` (78 mutants); `controls-c.txt` do-nothing control `lands==freeze`
`FAIL legs=4/13`, `lands==base` REFUSED exit 2; `measures-c.txt` `ACCEPT-C-75: PASS legs=13/13` at `4f5e3b2`, counter constants
read from freeze `5d01674`; gate registry rows `accept-c-75`/`accept-ca-75` exist in `SKILL.md` (the lane's registry home).
S893 (tier C) is not sole support: its entry also cites A/B rows S885, S888–S890. Entry provenance trio (`source:`,
`verified-at:`, `recheck:`) present in all three entries.

### Claim Ca — calibration (round-74 routed defects R1–R4 / ledger of 10 pairs) — **improved** (re-measured + evidence-verified; command caveat)

Re-derived the ledger's own observations at base and at Ca landing `012e8d3c8b92f47c734f735d58d118d574fe6a14`:

| pair | stated at base | observed (my command) | at Ca landing |
|---|---|---|---|
| L75-01/05/06/07 SHONEN.md:6 | "412 rows … 367 mined, 35 queued, 10 rejected" | base registry histogram `rows=808 mined=713 queued=58 rejected=37` | line states 808/713/58/37 (= histogram at 012e8d3) ✔ |
| L75-02 README:344 | `linguistics/ (30)` | `git diff --shortstat 4b825dc f556d10 -- 'corpus/knowledge/linguistics/*.md'` → 32 files | heading `(32)` ✔ |
| L75-03 README:407 | `culture-material/ (36)` | same, culture-material → 40 files | heading `(40)` ✔ |
| L75-04 README:813 (ANNOTATE) | footer 249 | `git grep -c -E '^- \`[^\`]+\.md\` —' f556d10 -- corpus/README.md` → 247 | footer stands; SCORECARD `## Corrections — round 75` row 249→247 ✔ |
| L75-08/09 round-74:37,38 (ANNOTATE) | span "absent" | `git grep -c 非凡特性来自最初造物主 f556d10 -- reports/round-74/evidence/S883.txt` → 1; `…这个我肯定考虑过… S884.txt` → 1 | correction rows present ✔ |
| L75-10 LOG:4318 (ANNOTATE) | "43 of 44" | `git diff --shortstat 4b825dc f556d10 -- ':(glob).ufo/waves/round-74/w2/*.md'` → 44 files | correction row present ✔ |

All 10 pairs were red at base and the 6 REPAIR pairs are green at the Ca landing. APPENDONLY: `git diff --numstat f556d10 f601f7f`
shows 0 deletions in LOG.md, SCORECARD.md, QUALITY.md, SOURCES.md, the round-73/74 lessons; only deletions are the repaired
statements in SHONEN.md (1), SKILL.md (1), README.md (3: two stale headings + the reorganised myth-symbol heading) and the sweep script.
SHONEN.md has no `[x]`. Evidence-verified: `selftest-ca.txt` `SELFTEST: 154/154` (39 scenarios); `controls-ca.txt` `lands==freeze`
`FAIL legs=7/12`, `lands==base` REFUSED exit 2; `measures-ca.txt` `ACCEPT-CA-75: PASS legs=12/12` at `012e8d3` with `--combined 4f5e3b2`.
**Caveat (confirmed from the lane's own wave-3 record, not re-executed):** the claim text's published command omits
`--combined` and the pinned local main and then prints `FAIL legs=11/12`; the substantive Ca predicates I re-measured above are
independent of that flag. Status-neutral defect routed below.

### Exploratory claims
None declared.

## 3. Axis verdicts (match the MANIFEST entry)

| axis | verdict | basis |
|---|---|---|
| coverage | **improved** | claim C re-measured (0→3 entries, 808→817 rows, 249→252 files) |
| calibration | **improved** | claim Ca re-measured (10/10 pairs red at base, repaired/annotated, append-only intact); the lesson's own newly-filed false counting statements are disclosed and routed in the same record (marked, not hidden), so no harm |
| every other owned axis | **unchanged** | `git diff f556d10 f601f7f -- SCORECARD.md` is append-only (+42 lines: `## Corrections — round 75`, `## Axes — round 75`); no existing row edited |

## 4. Discernment spot-check (LEARNING.md) — sources re-opened 2026-10-27

| item · decision | re-opened source | agree/disagree | reason |
|---|---|---|---|
| S885 Barthes 1966 · **admit** (tier A) | `curl -A <Chrome UA> https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113` → HTTP 200, 111487 B | **agree** | the row quote «Innombrables sont les récits du monde.» occurs in the tag-stripped, NFKC-folded body |
| S888 UCASS syllabus · **admit** (tier B) | `https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf` → 200, 225123 B (same as row); `pdftotext` | **agree** | 故事是一种深层的抽象结构，必须通过话语呈现 found exactly once (item 一, 第二讲); note: the lane's own lesson says the Gate quote lies past the first stored window, a defect it recorded |
| S891 S/Z reading sheet via Wayback · **admit** (tier B) | `web.archive.org/web/20041220223357id_/…barth70.html` → 200, 3898 B (same as row) | **agree** | the quote is present once after HTML-entity decode and tag strip (the page wraps «cinq grands codes» in `<Q>`), so a raw-byte search misses it and a normalised search finds it |
| S893 chinawriter 2023 · **admit** (tier C, re-opened document) | `https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html` → 200, 45238 B (same as row) | **agree** | the 39-char 世界观 span is present; used alongside A/B rows, not as sole support |
| staged S870 span · **reject** | same page as S893 | **agree** | `作品中的人物名字和地名也一样` and the three shorter fragments `人物的名字`, `名字和地名`, `地名也一样` all return 0 hits; reason and flip are located |
| Persée `docAsPDF/…1120.pdf` · **reject** (CAPTCHA) | `https://www.persee.fr/docAsPDF/comm_0588-8018_1966_num_8_1_1120.pdf` | **agree** | HTTP 403, 294 B, `This resource is protected by altcha`; not bypassed |
| S891 live URL · **reject as live-only anchor** | `https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html` | **agree** | returns 200 with a `bobcmn` script shell (47524 B vs the row's 46013 B — byte-unstable, as the lane's own note on drift says) not the document text; archive capture is the honest anchor |
| round-74 S899/S900 reject reasons · **reclassified** (lesson `## Corrections`) | `reports/round-74/evidence/S883.txt`, `S884.txt` at base | **agree** | each staged span occurs once in its own page capture; the old "absent" reason was false |

Newly written rows re-opened: S893 (above) and S891 (above); quotes are ≤25 words and ≤80 chars (S893 39 chars, S891 68 chars/9 tokens).
`sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → **exit 0**. Where the round's *entry prose* goes past the
page (S/Z "design order follows", Todorov's Formalist adoption, five-vs-six participants) the lane's wave-3 seats found it and the lesson
routes it; I confirmed that the landed lesson counts are false as wave 3 says (`wc -c` of the three entries is 30920/24166/23049, the Gate
text still carries 6862/5933/2514; four whole-document windows in `reports/round-75/evidence/` against the "three" in Gate note 3; `accept-ca.py:2175 R74_TMPDIR = "/tmp"`).

## 5. Trend verdicts

- **expansion: improved** — 3 admitted entries on ground absent at base (`grep -ci narrative` 0 → 3), each `source:` citing `mined` rows S885–S893; 808 → 817 rows (not a quota).
- **quality: unchanged** — the new gates carry green selftests and controls, but the round's own landed bytes carry known defects (lesson counting statements, `accept-c.py` fails its own QUALITY 23 limb 1, QUALITY 27 selector inert, several entry sentences wider than the cited page); all are disclosed and routed, none left unmarked, none a regression of a previously admitted entry — no basis for either `improved` or `harmed`. I agree with the lane's self-grade.
- **discernment: improved** — my spot-check agrees with every sampled admit (4) and reject (3) and with the round-74 reclassification; the disagreement the lane found against its own round-74 gate became a grounded lesson (R2) and QUALITY criterion 27 (its inertness is a routed defect, not an ungrounded criterion).

## 6. Verdict

No claim fails; no axis harmed. Round 75 is **admitted**. SHONEN boxes are not fully checkable by a non-author from this review alone
(the lane-owned `[~]` boxes need an operator promotion review; this spot-check is a verifier-on-record for the registry-summary and
end-to-end boxes only) — operator-owned, not written here.

## 7. Defects routed to round 76 (lane must fix)

1. **Counting statements in `round-75.md`** that ExecCountsSweep F1–F13 and my re-measure show false at the landed bytes (entry byte sizes, "three" whole-document windows, anchor-absent-from-window cells, S885/S887 byte counts, deleted `assimilation/validate/…` path): append a correction entry; do not rewrite.
2. **Claim-Ca published command** lacks `--combined` and the pinned main — state the full measuring command in the next claim text/SCORECARD; `accept-ca.py` writes under `/tmp` (`R74_TMPDIR`) and falls back to the system tempdir.
3. **`accept-c.py` fails QUALITY 23 limb 1 (`GROUND_RECEIPT`)**, and QUALITY 27's selector matches none of the round's reject rows — fix the selector or supersede 27 with a row naming it.
4. **Entry sentences wider than the page** (S891 "design order follows"; Todorov/Formalists; five-vs-six participants; `grep -n 'four levels'` still matching negations): mark each in the entries by appended amendment.
5. **Pre-freeze counter sha** (`fa5060b9…`) cited by `selftest-c.txt` and `SKILL.md:707` — the committed counter is `315c5f3f…`; the lesson overstates "no landed byte existed"; incomplete mutation coverage (`MutLandedC` M1 only, `MutIndexRejectsGround` none) — re-run.
6. Carry forward from the lesson `## Routed to round 76` items 1–8 (six path-present files, register adjacency guard, S877 supersede row, R75-M2 in counter, Persée byte-instability, S892 URL wrap, S787↔S893 pointer).
7. Round-74 closure R1/R3/R4 remain open pointers (APPENDONLY over-protects a contract-permitted `used-by` cell; dangling pushed-hash pointer; carried-over lane items).
