# ScribeLesson — round-93 lesson draft (kotodama)

Stage: `.ufo/waves/round-93/w1/stage/ScribeLesson/` (lane-relative to `/home/vgpnk/Projects/shokunin/kotodama-shokunin`).

## Files written

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-93/w1/stage/ScribeLesson/round-93.md` — the lesson draft for the L1 to copy to `corpus/lessons/round-93.md`. 15460 bytes, 89 lines, md5 `b716ed6ca9be70c3c1b20e97b112f747`.
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-93/w1/stage/ScribeLesson/reopen/S961.html`, `S962.html`, `S963.html`, `S964.html` — my independent 2026-11-05 re-opens of the four admitted sources (plain `curl`, default UA). S961, S963 and S964 are byte-identical to the committed captures (`sha256 61f464e4…`, `3eb97d8a…`, `c8eba504…`); the S962 re-open differs byte-wise from the committed capture (`fb3effcf…` vs committed `098eed5c…`, same 49042 bytes) — the served page carries a per-request token, but the quoted span is present in both.
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-93/w1/stage/ScribeLesson/reopen/cand/*.bin` — one plain-`curl` probe per screened DOAJ candidate (34 files), the source of the access outcomes quoted in the Gate bullets.

No production file was touched: nothing under `corpus/`, `tools/`, `reports/` outside the stage dir, `SKILL.md`, `PROVINCE.md`, `SCORECARD.md` or `LOG.md` was written. No commit, push, or mutating git/jj command was run. Scratch `/fast/scratch/hyaku/kotodama-r93/ScribeLesson/` was removed before this report.

## Gate lines copied

Copied byte-identically from `reports/round-93/gate-lines.md` (verified by an exact-string containment test over all four lines, rc 0):

- `- S961 admit A/mined. https://bop.unibe.ch/linguistik-online/article/view/1426 — accessed 2026-11-05 — body: “the speech acts of greeting and leave-taking denoted by the German verb”`
- `- S962 admit A/mined. https://pressto.amu.edu.pl/index.php/srp/article/view/21548 — accessed 2026-11-05 — body: “despite their apparent formal resemblance, came to codify totally opposite”`
- `- S963 admit A/mined. https://bop.unibe.ch/linguistik-online/article/view/3847 — accessed 2026-11-05 — body: “greetings tend to be brief today”`
- `- S964 admit A/mined. https://oaj.fupress.net/index.php/ss/article/view/17732 — accessed 2026-11-05 — body: “compiled a pool of words, expressions, and sayings”`

## Mistakes rows (exactly as specified)

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| R93-M1 | survivor | the first v4 mutation run scored 80/83 with survivors dispo-anchor-revert, gap-lesson-graded-off and head-qualify-off: the negatives passed through another leg, so each fixture named a leg it did not isolate | none | each v4 negative now pins the exact failing leg (chk_leg), and the fixtures were isolated; red-before 80/83, after 83/83, receipt reports/round-93/mutation-score.txt |
| R93-M2 | vacuous | the round-92 search log excluded sixteen candidates by title only, with no per-candidate reason, per the round-92 spot-check §4 at corpus/lessons/round-92-verifier-spotcheck.md | none | QUALITY criterion 37 below, and this round's search log gives a reason per exclusion |
| R93-M3 | stale-premise | the round-92 claim C before-description says sound-symbolism.md has no ideophone-class entry, but §6 holds one | none | corrected below as an append-only erratum, not by editing the frozen round-92 text |

## Numbers measured, with commands and dates

- DOAJ article API, five query strings, 2026-11-05, `curl -sS "https://doaj.org/api/search/articles/<query>?pageSize=10"`: `greeting formulas` 10, `greetings ritual` 10, `farewell formulas` 10, `fórmulas de saludo` 10, `politeness formulae greeting` 6 records on the first page. With `?pageSize=100` the API's `total` field returned 30 / 17 / 12 / 11 / 6 for the same strings. The brief's screen-time counts (14, 10, 10, 10, 10) are written into the draft as the round's recorded per-query figures, with an explicit sentence saying the DOAJ index is live and that only the screened set is reproducible; the counts are not presented as re-runnable invariants.
- Screened set: 38 distinct records, deduplicated by DOI (or by full-text URL where the record carries no DOI) over the five first pages; one article appears twice (journal page plus download stub). After removing the four opened articles and the two unreachable candidates, 31 candidates are listed with one reason each.
- Per-candidate probe, 2026-11-05, plain `curl -sSL --max-time 40`, default UA: 34 candidate URLs probed; HTTP 200 for 26, HTTP 403 for 4 (Tandfonline, MDPI, Annales UP Kraków, Anuario de Estudios Filológicos), HTTP 404 for 1 (PsyJournals), HTTP 500 for 1 (onomastics.ru), HTTP 202 with an empty body for 1 (doi.org De Gruyter front door), TLS verification failure (curl rc 60) for 2 (univ-bejaia.dz, journals.us.edu.pl), DNS resolution failure (curl rc 6) for 1 (radab.mosuljournals.com), redirect-to-HTTP with TLS failure (rc 60) for 1 (emerita.revistas.csic.es).
- Unreachable pair re-confirmed 2026-11-05: `https://www.mdpi.com/2226-471X/11/9/179` → HTTP 403, 400-byte access-denied body (matches the committed `reports/round-93/evidence/unreachable-mdpi-403.raw`); `https://univ-bejaia.dz/revue/jslcs/article/view/394` → curl rc 60, TLS verify failure, 0 bytes, not retried with verification disabled.
- Gate-line byte check, 2026-11-05: exact-string containment of all four `gate-lines.md` lines in the draft → all four present, rc 0.
- Multi-id / table-id lint on the draft, 2026-11-05: `python3 -B tools/check-cited-lines.py .ufo/waves/round-93/w1/stage/ScribeLesson/round-93.md` → `CITED-LINES: 0 finding(s) in 1 file(s)`, rc 0.
- S-id scan of the draft, 2026-11-05: the only S-ids present are S961–S964; 0 lines carry an S-id together with a LOCATED / NOT LOCATED token; 0 lines carry more than one distinct S-id.
- Round-91 quarantine tally re-derived from `corpus/lessons/round-91.md`, 2026-11-05: 21 verdict rows — LOCATED 3, PARTIAL 3, ABSENT 10, UNREACHABLE 3, UNVERIFIABLE 2.
- `considerthese/` check, 2026-11-05: `ls -d /home/vgpnk/Projects/shokunin/kotodama-shokunin/considerthese` → rc 2, no such file or directory.
- Mutation receipt, read from `reports/round-93/mutation-score.txt` (committed at freeze `174fd5a8`): `MUTATION-SCORE: 83/83 killed, 0 survived, 0 broken-pattern`, header `# tool sha256 9799a96c…`; the three R93-M1 survivor names appear in `reports/round-93/mutants.py` (lines 103, 113, 134) and are recorded KILLED in the receipt. The red-before 80/83 figure comes from the brief, not from a committed artifact I could locate (grep for "80/83" across the lane returns only the dispatch/spec text), and the draft attributes it as specified without claiming an artifact for it.

## Constraints checked

- Non-canon: the Understanding section states that no claim about canon, lore acceptance, real-world rights or cultural permission is made, and the design rules are labelled "(design, not sourced)".
- One S-id per line on any line stating a fact about a real language: enforced in the Understanding section (S961, S962, S963, S964 each on their own line) and verified by the lint above; table rows carry no S-id.
- No line contains an S-id together with LOCATED / NOT LOCATED, and no line starts with an S-id followed by a verdict; the only LOCATED tokens in the draft are in the Quarantine tally, on a line with no S-id.
- The Gate bullets carry no S-id, and the two unreachable candidates are recorded as NOT rows, not as admitted rows.

## Constraints I could not fully satisfy

- The brief's per-query counts (14, 10, 10, 10, 10) do not match what the DOAJ article API returns on 2026-11-05 for those exact query strings (first-page counts 10/10/10/10/6; `total` 30/17/12/11/6). I wrote the brief's figures into the draft as the round's screen-time counts and added a sentence saying the index is live and that only the screened set is reproducible, rather than asserting the counts as re-runnable. If the L1 prefers, the sentence can be rewritten to attribute the counts to the scout's own capture.
- The 80/83 red-before of R93-M1 has no committed artifact I could find; the draft records it as the brief states, and the receipt that does exist measures only the 83/83 result.
- The brief's line "QUALITY criterion 37 below" is implemented as a proposed criterion paragraph immediately under the Mistakes table, flagged for the integrator to land in `corpus/QUALITY.md` (which currently ends at criterion 36). I did not edit `corpus/QUALITY.md`; it is production and read-only for this seat.
- The MDPI article's title is written as the DOAJ record gives it ("Pragmatic Variation in Greeting and Farewell Formulae in Rural Austria"); the brief names the same article with the same title and URL, and the 403 is recorded from the committed raw capture and from my re-probe.
- I could not establish from the S962 capture whether the per-request byte difference between the committed capture and my re-open is a session token or a content revision; the quoted span is present in both, and the draft's S962 line is copied from `gate-lines.md` unchanged.

## Tooling

No tool was installed or upgraded: the work needed only `curl`, `python3`, `git` (read-only) and `pdftotext`, all present on the host. No pacman transaction was run (host-wide pacman pause respected).
