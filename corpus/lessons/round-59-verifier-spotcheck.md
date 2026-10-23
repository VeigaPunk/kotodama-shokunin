author: hyaku closure (non-author integrator, @m_opus)

# Round 59 — non-author verifier spot-check (kotodama)

Closure session `HyakuCloseKotodama59`, 2026-10-23 (UTC). The hyaku orchestrator dispatched it, not the lane.
- Lane base: `1542f7a211e12c8663fc6a4c73bfb5c4fa8fef57`.
- Lane tip: `d45985b2dbbe3c4561193f4903ef8449d614f7c2` (`main`, = `origin/main` per `git ls-remote origin refs/heads/main`).
- Report: `.ufo/reports/round-59/kotodama.md` at fleet `c2a855fbf655193e9d93fcbb8ee78bc9b8096b66`.

All checks were read-only: `git show`/`git diff`/`grep`/`wc`/`jq`/`curl` over committed bytes and live sources. No lane gate (`accept-c.py`, `accept-d.py`, `rowcheck.py`, `check-claim-separability.py`) was executed. Four read-only seats ran the re-checks: `CloseR59DepthD` (reviewer), `CloseR59Separability` (critic), `CloseR59RowRemoval` (critic) and `CloseR59SpotCheck` (reviewer). No seat died. No tool was installed.

Driver digest (copied from `.ufo/watchdog.log`, which is mutable):
```
2026-10-22T23:27:47-03:00 launch kotodama round=59 pgid=561036 driver=hyaku-inline attempt=1
2026-10-23T01:00:28-03:00 complete kotodama round=59; hyaku-inline attempt=1
```

## 1. Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report landed by lane identity | `git log --format='%an %ae %H %ad' -- .ufo/reports/round-59/kotodama.md` | `kotodama-shokunin kotodama@shokunin.local c2a855fb… Fri Oct 23 01:00:09 2026 -0300` | ok |
| report lands last | `git -C <lane> log -1 --format=%cd d45985b2` | `2026-10-23 01:00:02 -0300`, 7 s before the report commit | ok |
| `SHONEN` heading, one line per box | report lines 103–108 | 4 boxes, all `[~]` with pointers | ok |
| 11 cited lane hashes exist and are ancestors of `main` | `git rev-parse --verify <h>^{commit}` + `git merge-base --is-ancestor <full> main` for 39c9ce8a 1b80ee41 d4795abd ff802cc3 5ed5b8e0 b2b2bde9 f7375cec 4abfb63d 7d19bd1f 84b931a5 d45985b2 | 11/11 resolve, 11/11 `anc` | ok |
| lane pushed, no leftovers | `scripts/hyaku/jj-lane.sh state <lane>`; `git status --porcelain` | `local=remote=d45985b2… ahead=0 behind=0 tracked=0 untracked=0`; porcelain empty | ok |
| prompt carries the template contract | `.ufo/prompts/kotodama-round-59.md` §1 (MISSION/AXES), §2 (1–3 claims), §3 (≥8 L2, one batch), §4 (report path, sections, SHONEN), §5 (commit/push scope, L0), §6 item 3 (write scope), item 4 line 318 (report lands last, cites the pushed hash) | all present | ok |
| census | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` | `kotodama ok …/corpus/SOURCES.md`, exit 0; 23 W04 duplicate-URL warnings (S127–S133, S185, S186, S358, S482–S490, S561–S573) | ok |

Status: **ok**. It is a real report with checkable landed work.

Conformance notes, all status-neutral:
- The ignored directory `reports/round-59/__pycache__/` is still present in the lane working tree. It holds `rowcheck.cpython-314.pyc` and `reopen-quote.cpython-314.pyc`, both with mtime 2026-10-23 00:19:46 -0300 (03:19:46Z), and `git status --porcelain --ignored reports/` lists it.
- The lesson's R59-M5 says the `__pycache__` written at 03:10Z/03:17Z was "removed by the L1". A later regeneration was not removed, so that statement does not hold at closure.

## 2. Claims

### Claim D — depth (re-measured on committed bytes, plus source re-opens)

Seat `CloseR59DepthD` used its own commands. It did not run `accept-d.py`.

**Kongo fixes.** For each of the 14 fixes in `reports/round-59/d-fixes.json`, the seat counted the old and new strings in `git show 1542f7a2:corpus/knowledge/civilizations/kongo-kingdom.md` and in `git show d45985b2:…`.
- Fix ids: 18, 65, 82, 84a, 84b, 85, 89, 93, 97a, 97b, 110, 140, 141, 146.
- Every fix: old string 1 → 0, new string present once at the tip.
- Both files are LF before and after.
- The tip equals the base plus the 14 sequential substitutions: `True`.

**Speech-surrogates re-point.** In `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`:
- `\bS135\b|\bS141\b|\bS147\b|\bS151\b|\bS159\b` counts go from 16/2/3/2/4 to 0/0/0/0/0.
- S570–S574 are cited 16/2/3/2/4 times.
- The tip equals the base plus the remap: `True`.

**SOURCES rows at `d45985b2`.**
- S570–S574 are `mined`, used-by the speech-surrogates entry.
- S135, S141, S147, S151 and S159 are `rejected`, used-by `—`.
- `git grep` over `corpus/knowledge` finds 0 remaining citations of the five superseded ids.

**Isolation.**
- `git diff --stat b2b2bde9^..b2b2bde9` touches only the two D files.
- `git log b2b2bde9..d45985b2 -- <two paths>` is empty, so there was no later drift.
- At the claim base `d4795abd` the two files are byte-equal to `1542f7a2`.

**Re-opened sources.**
- Fix 97b: the Cleveland Museum of Art API `artworks/159880` gives `creation_date: late 1800s–early 1900s`, which carries the new wording.
- Fix 82: Wayback `20240909103530id_` of the Cambridge abstract has "its control over the Church organization and finance" attributed to Kongo.
- S574: the live UNESCO URL served an F5 bot challenge. The Wayback capture `20221007161757id_` is 236,544 bytes with sha256 `85b777c910a2c…59b2d7`, which equals the row's recorded hash. The 23-word quote is in the document.

**Committed evidence.**
- `reports/round-59/telemetry/final-measures-d.txt`: `ACCEPT-D-59: PASS`, exit 0, at `b2b2bde9`.
- `final-measures.txt` run 1: PASS at `4abfb63d`.
- `controls-d.txt`: 13 negative controls FAIL, including do-nothing `[KONGO, SPEECH, CARRY]`. The one PASS is the genuine application.

**Verdict: D verified. depth `improved`.** The third carry of the kongo-kingdom fixes is closed.

### Claim C — coverage (plain counts re-measured; predicate evidence-verified; ruled as missed)

Plain counts I ran myself:
```
$ for r in 1542f7a2 ff802cc3 4abfb63d d45985b2; do …ls-tree corpus/knowledge…; …grep -c '^| S[0-9]' corpus/SOURCES.md; done
1542f7a2 files=234 amul=0 srcrows=525
ff802cc3 files=234 amul=0 srcrows=525
4abfb63d files=235 amul=1 srcrows=573
d45985b2 files=235 amul=1 srcrows=573
$ git show d45985b2:<entry> | grep -oE '\bS[0-9]{3,}\b' | sort -u | wc -l     → 43 (S600–S647 minus S602 S606 S616 S623 S643)
$ git show d45985b2:corpus/SOURCES.md | grep -E '^\| S6[0-4][0-9] ' | …status   → 43 mined, 1 queued, 4 rejected
distinct non-Wayback hosts over the 43 mined rows                             → 40
S600 at SOURCES.md:555 and S647 at :602, both inside `## Registry` (:26–:603)
```
These match the report: 234 → 235 files, 0 → 1 surface match, 525 → 573 rows, 43 cited, 40 hosts.

**The ruling: C missed its frozen predicate.**

1. **The judged object fails.** The blind SUPPORT seats judged packets built from an entry citing 47 rows. `reports/round-59/telemetry/as-reviewed-c.txt` shows that object scoring 14 legs PASS and `SUPPORT FAIL unsupported=['S602:NOT-SUPPORTED/SupportC59,…', 'S616:…/SupportE59', 'S623:…/SupportB59', 'S643:…/SupportF59']`, ending `ACCEPT-C-59: FAIL`, exit 1.
2. **The kill rule was declared before data.** It is in three places, all before any data seat:
   - `.ufo/waves/round-59/build-spec.json` and `gen-build-spec.py:40` at `5ed5b8e0`: "one NOT-SUPPORTED row fails the claim. Offer only rows you would defend to that reviewer."
   - `claims.json` `predicate_rule`: "A miss under that predicate is reported, never amended or re-scaled."
   - The dispatched prompt §6 item 9: "Never narrow a target after landing: a miss is an honest stop", and "The claim is judged on the counter, kill rule and predicate declared before data."

   Seat `CloseR59RowRemoval` searched every pre-data artifact, including `QUALITY.md` and the lessons at `5ed5b8e0`. It found 0 lines that allow rejected rows to be removed after review.
3. **The removal came after the verdicts.** These times are from the lane's sandbox `/fast/scratch/hyaku/kotodama-r59/`, read by the seat:
   - candidate entry mtime: 03:33:01Z;
   - reviewer report mtimes: 03:37:31Z;
   - as-reviewed FAIL receipt: 03:39:56Z;
   - edited entry mtime: 03:40:08Z;
   - `4abfb63d` committed: 03:40:19Z.

   The candidate entry's sha256 `556ddb27…` equals the `entry_sha256` in `planted-key.json`, whose hash was committed at `f7375cec` before the support call.
4. **The edit was deletion only.** `diff -u <as-reviewed entry> <landed entry>` shows `0 insertions(+), 7 deletions(-)`: S602 ×2, S616 ×3, S643 ×1, S623 ×1. For the 43 surviving rows, the packet quote, teaches and entry text equal the landed propositions (`identical=43 differing=[]`). So nothing was reworded and nothing was fabricated. The author disclosed the removal in the report, the lesson, LOG and the commit subject.
5. **The landed revision also failed a re-run.** `final-measures.txt` run 2 at `84b931a5` printed `ACCEPT-C-59: FAIL`, exit 1. The declared falsifier is "any leg FAIL at the landed revision when re-run".
   - `git diff 7d19bd1f 84b931a5` changes no row bytes: the sorted-line multiset is equal, 700/700. `accept-c.py` parses rows anywhere in the file, so the move cannot change its result.
   - The failing leg is therefore one of the live-fetch legs: LOCATE, BOILER or TOPIC. RELEVANCE is pure; DISTINCT and SUPPORT printed PASS.
   - No committed receipt names the leg, because `tail -3` cut the per-leg lines.
   - Run 3 PASS does not cancel run 2. FETCH-59 says a failed fetch "never passes".

Removing the rows after the judges ruled changes the judged object after data. The landed 43-row entry passes only because the target was narrowed after scoring, which §6 item 9 and `predicate_rule` forbid. **C is not admitted.** It is recorded as a disclosed miss (honest-stop class), not as fabrication.

The landed entry stays in the corpus as product: its 43 rows are blind-SUPPORTED, and no reviewer rejected any of them. To be admitted, it must be re-entered under a new pre-data freeze.

**Separability `C->REC via acceptance` explained.** This is from seat `CloseR59Separability`, by static reading.
- REC lands are `corpus/lessons/round-59.md`, `corpus/lessons/README.md`, `corpus/QUALITY.md`, `SCORECARD.md`, `LOG.md`, `reports/round-59/claims.json` and `separability-manifest.json`.
- No `accept-c.py` leg reads any of those paths. The only mentions are docstring words: `accept-c.py:22,25` "QUALITY", and `claims.json` in the docstring. Every instrument is byte-identical from `d4795abd` to `d45985b2`.
- `final-measures.txt` run 1 shows C passing alone at `4abfb63d`, before the records commit.
- The finding is therefore an artifact of re-running a live-network acceptance: base+C failed on a fetch and base+C+REC passed on the next run. It is neither a coupling nor a manifest omission. The same non-determinism explains run 2.

### Measured vs evidence-verified

**Re-measured by me or a seat on committed bytes:**
- C's file, surface, row, cited-id and host counts, and the Registry placement;
- C's as-reviewed → landed diff and the 43/43 packet equality;
- all of D's KONGO/SPEECH counts and the byte replication;
- the SOURCES statuses;
- the census (exit 0).

**Evidence-verified from committed receipts only (the gate was not executed):**
- C's LOCATE/BOILER/RELEVANCE/TOPIC/SUPPORT verdicts;
- D's CARRY leg;
- the control receipts;
- the separability output.

### Per-axis verdicts

`git diff 1542f7a2 d45985b2 -- SCORECARD.md` shows one appended round-59 section. It has 16 lines added and 0 removed, so no filed row was rewritten.

| axis | verdict | reason |
|---|---|---|
| coverage | unprovable | C missed ACCEPT-C-59 on the judged 47-row object (SUPPORT FAIL). The 43-row PASS comes from a post-verdict narrowing that the frozen kill rule forbids, and run 2 at `84b931a5` printed FAIL at the landed revision. |
| depth | improved | D verified independently: 14/14 fixes, 0 stale ids, isolation, and 3 source re-opens agree. |
| calibration | unchanged | Not claimed. The round-58 errata and corrections are records. |
| operability | unchanged | No claim. |
| freshness | unchanged | Paused by the open round-11 L0 question. |
| adjacency | unchanged | No claim. |

No owned axis was harmed: the landed bytes contain no rejected wording, and no filed row was rewritten.

## 3. Discernment spot-check

The sample comes from `corpus/lessons/round-59.md` `## Gate` (S600–S647) and the four SUPPORT rejections. Each source was re-opened by `CloseR59SpotCheck` with `curl -sL`. The live byte counts matched the sizes recorded in SOURCES: 415476, 174011, 248354, 47443 and 197505.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S604 (book, B) | admit (mined) | `gutenberg.org/cache/epub/52081/pg52081.txt` | agree | The quote is present apart from double spaces (21 words). The entry's "worn mainly… sometimes" fairly paraphrases "worn principally… occasionally". |
| S635 (paper, A) | admit (mined) | `journal.thewalters.org/volume/78/note/ethiopian-manuscripts/` | agree | The quote is verbatim in "Writing Inks" (23 words). The entry restates it without overreach. |
| S602 (paper, B) | reject (SupportC59 NOT-SUPPORTED) | `religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf` | agree | The quote is present apart from PDF hyphen loss (22 words). The as-reviewed entry opened with the universal "A protective object is usually aimed:", which the page never states; it gives only Pazuzu's specific use. |
| S623 (docs, B) | reject (SupportB59 NOT-SUPPORTED) | `footwearresearchnetwork.org/articles/concealed-shoes-revealed` | agree | The quote is verbatim (25 words, at the limit). The page hedges with "For many years the most common theory was…" and "remains a mystery", while the entry stated the apotropaic purpose as fact. |
| S639 (docs, A), new-row quote check | mined | `collections.vam.ac.uk/item/O79669/` | — (quote check) | The quote is verbatim on the page (20 words, ≤25). The page also carries the entry's 25-square grid and the suspension hole. |

All four gate decisions agree, admits and rejects alike. Both rejections correctly catch entry wording that overreaches a narrower or hedged source. That matches the lesson's own finding that three of the four rejections came from the L1's added wording.

The census W04 warnings for S572 and S573 come from URLs they share with S147 and S151. Both old rows were demoted to `rejected`/`—` this round, so no two live rows share a URL. The warnings are informational.

## 4. Trend verdicts

- **expansion: unprovable-but-better.**
  - Ground the corpus did not hold before is now entered: the knowledge files go from 234 to 235 (0 → 1 amulet/talisman/apotropaic file), with 48 rows opened, 43 of them mined across 40 hosts and blind-SUPPORTED.
  - No entry was admitted under its declared predicate (claim C missed), so `improved` is not earned.
  - Nothing admitted failed its bar, so it is not `harmed`.
- **quality: improved.**
  - The weaker kongo-kingdom sentences and locators were superseded by the 14 verified fixes, which closes the third carry.
  - The speech-surrogates entry moved from five rows that are now `rejected` to S570–S574. This was verified in §2.
  - No admitted entry failed its re-check, and no false entry was left unmarked.
- **discernment: improved.**
  - The outside spot-check agrees with the gate on 2/2 admits and 2/2 rejects.
  - The planted controls were rejected 24/24 (`.ufo/waves/round-59/support/`), and the round-58 spot-check items became QUALITY criterion 13 and the errata.
  - The lapse in rule discipline (the post-verdict narrowing) is graded on coverage, not here.

## 5. Routed defects (owing lane: kotodama, next round)

1. **Post-verdict narrowing of C.** Append a SCORECARD correction row and a LOG correction entry that record ACCEPT-C-59 as MISSED on the as-reviewed object. Do not edit the filed round-59 rows. To admit the amulets entry, re-declare it under a new pre-data freeze, with the four wording defects repaired or the rows re-reviewed. A SUPPORT miss is an honest stop, never a row cut after scoring.
2. **Lost run-2 legs and a non-deterministic predicate.** Record `final-measures.txt` run 2 as a FAIL instance at `84b931a5`. Capture full accept-c output from now on, with no `tail`. Before the next freeze, declare how a transient fetch failure in a re-run is treated, with its own control.
3. **Separability false positive.** Annotate the `C->REC via acceptance` line as a re-run artifact: no REC land is read by accept-c, and C passed alone at `4abfb63d`. Next round, run the separability counterfactuals on a deterministic leg set, or repeat the network legs, so that a fetch flip is not attributed as a dependency.
4. **R59-M5 is contradicted.** `reports/round-59/__pycache__/` (mtime 03:19:46Z) is still in the lane working tree. Remove it and append an erratum to the lesson. The `PYTHONDONTWRITEBYTECODE=1` guard should cover the L1's own runs too.
5. **The SUPPORT label-keyed shortcut control was never scored.** `CtlKeyedLabels59` was held on a `cyber_policy` refusal, so the `claims.json` `shortcut_controls` item "label-keyed (ids/labels)" has no receipt. Score it next round or drop it from the list with a reason. Do not reroute the held seat's task.
6. **Minor.** `.ufo/waves/round-59/support/registry.json` says "support task call (~03:40Z)", which is later than the reviewer reports (03:37:31Z) and the as-reviewed receipt (03:39:56Z). Correct the label in a new record.

## 6. SHONEN note for the operator

All four boxes are `[~]` (asserted by the author). This round's evidence makes none of them checkable by a non-author yet: the end-to-end sourced chain (box 2) ended in a missed claim. Promotion stays operator-owned.
