# ScoutOverlap — round 89 w1 report

Seat: scout, read-only reconnaissance. Full findings with path:line pointers are in `.ufo/waves/round-89/w1/stage/ScoutOverlap/recon.md`. Probe hashes are in `stage/ScoutOverlap/probes-sha256.txt`.

## Findings
- **(a) C overlap.** The corpus already has two parallel evidentiality sub-sections:
  - `corpus/knowledge/linguistics/semantics-pragmatics.md:66-82` (`## 4. Evidentiality and mirativity`, 5-row table)
  - `syntax-typology.md:69-82` (5-row sizing table)

  There are also scattered lines in semantic-fields-lexicon-building, conlang-methodology, morphological-typology, inca, haudenosaunee and consistency-verification-checklist. **The registry has zero evidentiality, mirativity or epistemic-modality rows and zero wals.info chapter or feature rows.** S002 is the WALS CLDF dataset only. S199's "epistemic" is gesture. All existing citations (Aikhenvald 2004, Willett 1988, DeLancey 1997, Palmer 1986, Barnes 1984, Faller 2002, Fleck 2007) are bibliography-only and have never been rechecked.
  - Verdict: a dedicated entry is new ground only if it covers what is absent. That means the argued evidential/epistemic separation (today one clause, :68), WALS 77A/78A counts and coding types, evidential × person/tense, and registry-backed verification. Restating the existing size→culture tables is repackaging.
  - There is an existing inconsistency the entry should resolve rather than copy. On Turkish, semantics-pragmatics.md:79 says "optional but rich … not forced", while syntax-typology.md:77 says "2-term … hearsay marked even in formal writing".
  - wals.info/chapter/77 and /78 (de Haan) were live (200) as new-id candidates. 77A: 181/166/71 of 418. 78A: affix 131, tense 24, particle 65, modal 7, mixed 10.
- **(b) F repeat check.**
  - In form, F is a first. No round has ever advanced a registry `recheck` cell by re-verification. The only prior change is policy: round-49.md:89 sets `—`→`365d`. The r82 queue tool has never been consumed.
  - In substance, the 16 rows are 10-16 days old (opened 10-19, 10-22 and 10-25), and most were already re-opened by non-author seats in their own rounds (r50, r51, the r52 closure, the r72 closure). F is a short-interval liveness check, not drift detection.
  - **Pause risk.** The round-11 L0 line (`/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:47`) ends "Freshness axis-move claims are paused until ruled". It has no L0 ANSWER, and the pause is restated in about 20 LOG/SCORECARD places through r86. F is the first freshness claim since r11. claims.json's "does not depend on" reading is an interpretation, not a ruling.
- **(c) The 16 rows.** Each row's original Gate quote, `path:line`, live status and fit to the r89 bounds is tabulated in recon.md. Defects that will bite the F author:
  - **S104** ("Pseudo Family: LSFic", 19 chars) and **S875** ("安土・桃山", 5 chars) fail the ≥20-char bound. A 21-char replacement for S875 that is present in the raw page: "記録作成等の措置を講ずべき無形の民俗文化財".
  - **S105**'s JSON quote breaks `first_quote` (inner `"`), so use curly quotes. S105 is also superseded by S126.
  - **S009** and **S106**: inline HTML markup breaks the old quotes against raw bytes. Working raw-matching substitutes are given.
  - **S032**'s r49 URL (api.crossref.org) fails `url_ok`. Use the doi.org URL, which reaches a linkinghub stub carrying the title.
  - **S142** matches only after `pdftotext`.
  - **S157/S163**: live gives a TSPD bot challenge (not passed). For S157, Wayback 20260830052642 has the quote. For S163, the latest Wayback captures are archived challenges. Only 20260312095851 `id_` fetched with `--compressed` contains the quote.
  - **Window edge:** a recheck date of 2027-02-02 (today+90d) does NOT advance, because the predicate is strict `>`. Use a date ≥ 2027-02-03.

## Commands observed (rc)
- grep tool over corpus/knowledge, SOURCES.md, LOG.md, corpus/lessons: ok
- `cat claims.json; sed/grep l0-questions.md; grep SCORECARD.md`: rc 0
- python3 cell extraction over SOURCES.md, and `measure89.quote_ok/first_quote/contains` over original quotes: rc 0
- `curl -sS -L` on the 16 row URLs (all 200), 2 Wayback, 2 CDX-listed `id_` (+`--compressed`), 4 WALS pages: rc 0; `pdftotext` S142: rc 0
- `sha256sum` probe bodies → stage/probes-sha256.txt: rc 0; `rm -rf /fast/scratch/hyaku/kotodama-r89/ScoutOverlap`: rc 0 (verified absent)

## Paths written
- `.ufo/waves/round-89/w1/stage/ScoutOverlap/recon.md`
- `.ufo/waves/round-89/w1/stage/ScoutOverlap/probes-sha256.txt`
- `.ufo/waves/round-89/w1/ScoutOverlap.md` (this file)

## Unresolved
- Pause scope (L0/operator).
- S142's non-author re-open history was checked by filename grep only.
- Probes were single plain requests. They are not F captures and must not stand in for them.
- No frozen file is amended.

Tools installed or upgraded: none (RULES.md not needed; no installs). No production, git or jj writes.
