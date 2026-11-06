# kotodama round 99 — non-author verifier spot-check

author: hyaku closure (non-author integrator, @m_zfl)

Closed 2026-11-06. Base `527df3fee305b3454446946e6779ece45456307e`, freeze `b1b80562edfc8f6082aec74bbbf0f25e152708a8`, after `3f415f84ecdb8f700899b15cc5741f40ced89ac3`.
Report: fleet `.ufo/reports/round-99/kotodama.md`. Prompt: fleet `.ufo/prompts/kotodama-round-99.md`.

Driver digest (copied from the mutable `.ufo/watchdog.log`):

```
2026-11-06T00:55:10-03:00 launch kotodama round=99 pgid=3826949 driver=hyaku-inline attempt=1
2026-11-06T07:56:44-03:00 lane-dead-no-report kotodama round=99; retry same round (hyaku-inline attempt=1: L1 ended without a landed report: FAIL report_of (missing, unchanged, no SHONEN heading, or < 400B): .ufo/reports/round-99/kotodama.md)
2026-11-06T07:56:47-03:00 launch kotodama round=99 pgid=1021740 driver=hyaku-inline attempt=2
2026-11-06T08:18:51-03:00 complete kotodama round=99; hyaku-inline attempt=2
```

## 1. Step-1 conformance — pass (two minor defects, status-neutral)

- `git log --format='%an %H' -- .ufo/reports/round-99/kotodama.md` (fleet repo) → `kotodama-shokunin 01232d60d84e569f84fcacc64b0989335283d22b` (2026-11-06 08:17:47 -0300). The last lane commit `3f415f84` is 08:17:25, so the report was filed after its commits.
- `## SHONEN` heading present (`grep -c '^## SHONEN'` → 1) with 4 `[~]` lines, matching the 4 boxes in `SHONEN.md` (`grep -c '^- \['` → 4). No box is `[x]`.
- Cited commits `527df3fe…`, `b1b80562…`, `60ead722…`, `3f415f84…`: each `git rev-parse` resolves to a full hash and `git merge-base --is-ancestor <hash> main` → ok. `git log 527df3fe..3f415f84` → 3 commits, all authored `kotodama-shokunin <kotodama@shokunin.local>`.
- `scripts/hyaku/jj-lane.sh state …` → `branch=main local=3f415f84… remote=3f415f84… ahead=0 behind=0 head=detached tracked=0 untracked=0`. `git status --porcelain` → 0 lines. `git ls-remote origin refs/heads/main` → `3f415f84ecdb8f700899b15cc5741f40ced89ac3`.
- The prompt carries the template contract: `grep -n '^## '` shows §§1, 2, 2b, 3, 4, 5 identical to `templates/round-prompt.md`, plus hyaku addendum §6.
- Freeze precedes work: `b1b80562` at 01:03:44 -0300, after the 00:55:10 launch and before any seat output; `git diff --stat b1b80562 3f415f84 -- reports/round-99/{predispatch.py,claims.json,predispatch-base.txt,controls/battery99.py}` → empty. `battery99.py` sha256 `87f426aa…` = `battery99.sha256`.
- Defect D1 (path): 11 of 12 seat reports sit at `w1/<Seat>.md`; ReviewerC99's is at `w1/stage/ReviewerC99/review.md` (no `w1/ReviewerC99.md`), while report §Work says each seat writes `w1/<Seat>.md`. The evidence exists; the stated path is wrong for one seat.
- Defect D2 (evidence): `w1-results.json` records `output: null` for all 12 seats (kernel restart). The report discloses this; seat evidence rests on the wave-dir files (12 `DONE` markers present).

## 2. Claims

The frozen counter is `reports/round-99/predispatch.py`. Committed evidence read, not executed (PROTOCOL §Gate standard, Closure consequence): `predispatch-base.txt` → `PREDISPATCH-99: FAIL legs=6/16`; `predispatch-lands.txt` → `PREDISPATCH-99: PASS legs=16/16`, `rc=0`. The lands receipt was measured on the tree committed as `60ead722`; `git diff --stat 60ead722 3f415f84` → only `.ufo/waves/round-99/w1-results.json`, so it grades `3f415f84` too.

### Claim O (operability, grader v10 → v11, harm repair)

Re-measured by me:

- `git show 527df3fe:tools/check-advance-evidence.py | sha256sum` → `d35b13c9…16af7` (v10); `git show 3f415f84:… | sha256sum` → `717341dc…76f2`. O0 agrees.
- Refusal-id census (`grep -oE '\(([A-Z][A-Z0-9]*-)*[A-Z][A-Z0-9]+\)' | sort -u`) at base vs after: every base id survives except `HEADING-NUMBER`, whose removal is the routed F1 repair; `VERDICT-COMBINE`, `HEADING-COMBINING` and all VERDICT-* ids remain. No other refusal disappeared.
- `grep -c "chk('"` 106 → 116 (selftest call sites; not 1:1 with the 161 → 175 tally, which I did not execute).
- Routed round-98 items: the `HEADING-NUMBER` append is gone (F1); `for p in []` survives only in a comment stating its removal (F2); benign twins MCOK1/MCOK2/VISOK1/DEVAOK1 with U+093E/U+0903/U+094D headings sit in the selftest at :2065–2068 (F4); pins CM1-DEVANAGARI, MARKDASH, ROMANMARK, NFKDME1 keep the forgery set refused.
- Mutation pin: `git show 3f415f84:.ufo/waves/round-99/w1/stage/MutationTester99/mutants99.py | sha256sum` → `cf58e126…2ffd` = `controls/mutants99.sha256` = receipt line 1 `DRIVER-SHA256 cf58e126…`.

Evidence-verified only: O1 `175/175 floor=168 rc=0`; O2 battery99 `0/0/37/0/9/0` (base `not-clean=6`); O3 REG 34/34 byte-identical; O4 critic98 `overrefusal=0 survivors=24` (base `overrefusal=2`, `clean-not-rc0=['OK-MCWORD','OK-DEVAHEAD']`); O5 critic97 unchanged; O6 `MUTATION-SCORE: 136/136 killed, 0 survived, 0 broken-pattern` (`controls/mutation99-first.txt`).

The round-98 harm (two false-refusal surfaces on valid input) is removed without a lost refusal. **Operability: improved.**

### Claim C (coverage, praise poetry and panegyric entry)

Re-measured by me:

- `git show 3f415f84:corpus/knowledge/linguistics/praise-poetry-panegyric.md | wc -c` → 45197; `grep -c '^## '` → 13. At `527df3fe` the path is absent (`fatal: …`).
- `grep -c '^| S[0-9]' corpus/SOURCES.md` → 930 at base, 941 after; highest id S1006 → S1017.
- Each of S1007–S1017 has exactly 1 registry row and ≥2 citing lines in the entry (S1007 40, S1008 5, S1009 5, S1010 5, S1011 6, S1012 6, S1013 3, S1014 3, S1015 2, S1016 3, S1017 3).
- `grep -c praise-poetry-panegyric corpus/README.md` → 3. `grep -c 'public property\|Xhosa rally'` on the entry → 0 (CriticC99 repairs present).
- `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → `kotodama ok …/corpus/SOURCES.md`, rc 0. Warnings W01/W04 are on pre-existing rows S127–S928 only; none on S1007–S1017.

**Coverage: improved.**

### SCORECARD harm check

`git diff 527df3fe 3f415f84 -- SCORECARD.md` only appends a round-99 axes block, a capability row and the round-100 plan; no earlier score or verdict changes.

### Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| operability | improved | Claim O: harm repaired, sha/refusal-id census/pin re-measured; O1–O6 evidence-verified |
| coverage | improved | Claim C re-measured as above |
| depth | unchanged | Oath L49/L51/L53 and praise-entry repairs are observation, not a claim |
| freshness | unchanged | Paused by open L0 round-11 and round-89 questions; not met, not waived |
| calibration | unchanged | QUALITY 41 added; author verdicts are honest (discernment self-graded unchanged, closure pending stated) |
| adjacency | unchanged | No move; deferrals to `orality-formulaic-language.md` and neighbour entries |

## 3. Discernment spot-check

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S1009 Barber, *Oral Tradition* 20/2 | admit (A) | `curl -sSL …/articles/20ii/Barber.pdf` → 200, 895589 B; `pdftotext` | agree | Quote "Obscurity in praise poetry could be deployed for political reasons." count 1; peer-reviewed journal on Yoruba oríkì, tier A fits |
| S1012 Pindar, trans. Myers, Gutenberg #10717 | admit (A) | `curl -sSL https://www.gutenberg.org/cache/epub/10717/pg10717.txt` → 200, 320993 B | agree | Quote "Yet praise is overtaken of distaste, wherewith is no justice, but from covetous men it cometh" count 1 (whitespace-normalized); primary text |
| S1016 Potts, ASNC skaldic introduction (SOURCES.md row 973) | admit (B) | `curl -sSL …/Introduction-to-Skaldic-Poetry_Debbie-Potts.pdf` → 200, 294812 B, sha256 `9d5bc813…` = L1 receipt | agree | Row quote "There certainly was money in poetry for the skald; court poets would receive generous rewards" is 15 words (≤25), count 1 in fresh bytes and in `evidence/S1016.txt` (`' '.join(t.split())`; plain `grep` misses it because pdftotext emits tab/non-breaking separators). Teaching resource, tier B fits |
| C14 Gourlay, "Long Trumpets of Northern Nigeria" | reject (scope) | `curl -sSL https://journal.ru.ac.za/…/download/1116/591/593` → 200, 1441621 B | agree | Satire-of-miserly-patron sentence count 1, inside an organological study of trumpets (title confirmed); a praise-poetry-scoped row would be mis-anchored |
| C6 Encyclopaedia Iranica, Court poetry | reject (access 403) | `curl -sS https://www.iranicaonline.org/articles/courts-and-courtiers-x/` → **200**, 400760 B, `<title>COURTS AND COURTIERS x. Court poetry - Encyclopaedia Iranica`, "panegyric" 13 hits | agree (at decision time) | The candidate record shows 403 Cloudflare ×3 plus PDF 403; not bypassing a challenge was right. Today the page serves from this host, so the access reason no longer holds: routed as R3 |

The spot-check agrees with the gate on 3/3 sampled admits and 2/2 sampled rejects.

## 4. Trend verdicts

- **expansion: improved.** An unowned surface (C8 owners 0/270 at base) gains a 13-h2 entry backed by 11 new mined tier A/B rows; census rc 0.
- **quality: improved.** The closure-ruled v10 harm is removed with no refusal lost (refusal-id census; O2–O6 evidence); three oath weak lines and three praise-entry support defects repaired.
- **discernment: improved.** Outside sample agrees on all admits and rejects; QUALITY 41 is a criterion shown able to fail (v10 battery99 not-clean=6). Same basis as the round-98 closure.

## 5. Ruling

Status ok. Both claims verify; no axis harmed. **Admitted: true (`admitted`).**

## 6. Routed defects (lane fixes next round)

1. R1 (D1): name ReviewerC99's actual report path, or file seat reports at `w1/<Seat>.md` as stated.
2. R2: table-cell support check for §-tables whose caption claims recorded cases (R99-M2; already planned for round 100).
3. R3: re-open C6 Iranica (now HTTP 200 with the article) and re-judge it on scope and tier.
4. R4: CriticO98b's 24 survivors and CriticO99's 6 anchor-neutral passes stay open (O4 bounds them at ≤24).
5. R5: freshness stays paused until L0 answers round-11 and round-89.

Operator note: SHONEN box 2 (end-to-end task logged: LOG round-99 entry + `predispatch-lands.txt`, re-checked here) looks checkable by a non-author. Box 3 rests on a lane seat (ReviewerO99), not an outside verifier. Promotion is operator-owned.
