# RevAssimilationFinal — wave 2, round 73 (kotodama, hyaku run 7)

Seat: leaf reviewer, ATTACK of the assimilation-contract execution (prompt §6 item 10, lines 440–545)
against the LANDED state at `0316b8883b4f8d44b8efd720140e7f52f734a102` (base `8841ad3b…`).
Read-only. No mutations, no delegation, no fetches. All counter runs in the throwaway clone
`/tmp/tmp.SUAu7cDOW2/lane` (detached at 0316b88; `git rev-parse --show-toplevel` = `$D/lane` verified).

## Exercised checks (commands + results)

| # | check | command / artifact | result |
|---|---|---|---|
| 1 | Claim C counter at lands | `python3 -B reports/round-73/accept-c.py --root . --lands 0316b8883b4f8d44b8efd720140e7f52f734a102 --fleet-root /home/vgpnk/Projects/shokunin` (clone) | `ACCEPT-C-73: PASS legs=11/11`, exit 0 |
| 2 | Claim Ca counter at lands | `python3 -B reports/round-73/accept-ca.py --root . --lands 0316b88… --fleet-root /home/vgpnk/Projects/shokunin` (clone) | `ACCEPT-CA-73: PASS legs=9/9`, exit 0 |
| 3 | Cited-lines (lane's own check) | `python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/conlang-scholarship.md corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md` | `CITED-LINES: 0 finding(s) in 2 file(s)`, exit 0 |
| 4 | Root census (end state) | `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` | `kotodama ok … SOURCES.md`, exit 0 (W04 warnings allowed) |
| 5 | Registry id diff | `git show 8841ad3b:corpus/SOURCES.md` vs lands `corpus/SOURCES.md`, `grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'` → sort | adds exactly `S876 S877 S878 S879 S880` (799→804), zero removals |
| 6 | Base vs lands entry files | `git ls-tree -r 8841ad3b --name-only | grep conlang-scholarship` / `… 0316b88 …` | base: 0 matches; lands: both entries present (plus w1 drafts) |
| 7 | Mirror==append parity | `git show 0316b88:corpus/SOURCES.md | sha256sum` | `93d6046444f2170e…018774` == receipt's mirror hash `93d60464…` |
| 8 | Receipt-before-append order | `git log --format='%h %ad %s' --date=iso -- corpus/SOURCES.md .ufo/waves/round-73/assimilation/validate-receipt.txt` | receipt committed at freeze `af65165` 12:52:54; registry append at `85f17eb` 19:59:32 (strictly after) |
| 9 | Evidence committed pre-data | `git ls-tree -r af65165 --name-only | grep round-73/evidence` | `S876..S880.txt` all present at freeze; 5/5 at 85f17eb |
| 10 | Collision guard proof | `.ufo/waves/round-73/assimilation/guard-proof/guard-proof.txt` | A1 799/799; A2 planted `  | S881 |` (2 spaces): column-zero control misses (799), 0–3-space guard finds (800, collisions 17→18); A3 control 0 vs guard 1; real pair 799/132/17; `GUARD-PROOF: PASS` |
| 11 | Renumber map | `.ufo/waves/round-73/assimilation/id-renumber-map.json` | `map` key covers all five adopted ids: S881→S876, S882→S877, S892→S878, S893→S879, S901→S880 |
| 12 | used-by cells | `awk -F'|'` rows 831–835 | S876/S877 → conlang-scholarship.md; S878/S879/S880 → conlang-scholarship.amend-2026-10-23.md — exactly the citing entries, union = both |
| 13 | Forbidden ids in admitted entries | `grep -nE 'S894|S869|S909|S910|S915|S929|S930|S920|S922|S923|S728|S769|S806'` both entries | 0 matches (exit 1) |
| 14 | considerthese | `ls -ld considerthese` | no such dir; lesson line 8 and 130 record the absence |
| 15 | Source-repo read-only | grep of all committed round-73 artifacts for write-intent against `/home/vgpnk/Projects/shokuknow` | only reads/references (merge paths, register, QU); no command writes, commits, or campaign-tool runs into shokuknow |

## Obligation walk (item 10, lines 440–545) — artifact per obligation

1. **Source repo read-only — PASS.** No committed round-73 artifact (lesson, receipts, evidence, counters, wave reports) claims a write/commit/fetch/push into `/home/vgpnk/Projects/shokuknow`; nothing beyond read paths appears.
2. **ONE theme, 1–3 entries — PASS.** Theme: conlang scholarship. Two entries admitted: `corpus/knowledge/linguistics/conlang-scholarship.md` (S876/S877) and `…amend-2026-10-23.md` (S878/S879/S880). Within cap; both same theme; base had neither file.
3. **Every cited source re-grounded in-round — PASS.** Each of S876–S880 has a committed evidence capture (`reports/round-73/evidence/S<id>.txt`) with fetch line, browser-shaped UA, HTTP 200, bytes, 64-hex sha256, `quote-found-verbatim: yes`, quote inside its context window; Gate rows carry the same quotes with the lane's own access date 2026-10-25 and locators. Quotes ≤25 words verified (16/9/24/16/25).
4. **Append only rows the admitted entries cite — PASS.** Registry diff is exactly S876..S880; CITEDLINES 0 findings; each of the five ids appears on a `source:` line of an admitted entry (S876/S877 in base; S878/S879/S880 in amend) and the row URL matches verbatim.
5. **Id collision guard, 0–3-space pattern, planted-row proof — PASS.** guard-proof.txt A2: planted indented row caught by the 0–3-space guard, missed by the column-zero control; collisions file 17 (S859–S875); adopted ids absent from reg-ids and collisions.
6. **Scratch transformation + `validate --file` exit 0 before append — PASS.** Receipt at freeze `af65165` (12:52) strictly before append commit `85f17eb` (19:59): `validate --file` exit 0 on the mirrored corpus (5 rows + both entries, 799→804); post-append registry sha256 equals the receipt's mirror sha256 (`93d60464…`, verified). The receipt was additively extended at `0316b88` after first grading with an `## ids carried` block — documented in-file, original pre-append run intact.
7. **Quarantine hand-check of slice rows touching the theme — PASS.** `ScoutQuarantineConlang.md` hand-checks the three theme-touching register rows: S786→S869 PRESENT (title-page epigraph p. 1, live + Wayback 20100107110431); S812→S894 PRESENT in Crossref abstract but publisher page HTTP 429 (unverifiable at publisher, not fabrication → refused with flip); S827→S910 PRESENT in Crossref metadata but Springer challenge shell (not adopted). Verdicts land in the lesson Gate.
8. **Refused entries kept with reason+flip — PASS.** Gate rows for S894, S909/S910, S869, S915, S929/S930, S920/S922/S923 each carry reason, flip condition and probed URLs; families naming-systems/calendar/era/verification (+ worldbuilding-setting-practice/narrative-structure) recorded as not adopted with reason+flip.
9. **≥1 admit and ≥1 reject in lesson Gate — PASS.** 5 admits (S876–S880) + multiple rejects.
10. **Amendment files appended, not replaced — PASS.** Both admitted paths are new at base; no existing file overwritten; no byte removed from an existing knowledge file.
11. **Folded duplicate-target entries — PASS.** The staged `conlang-scholarship.amend-2026-10-23.md` is itself the folded round3(round4 pair (MERGE-REPORT.md:26, 55–56; superseded-passage header inside the staged file). MERGE-REPORT adopt checklist item 6 ("fold the two entries into the one file … citing the rows of both rounds") is satisfied by the landed amend: round 3's passage (peer-reviewed Russian venues S892/S893 → re-grounded S878/S879) and round 4's passage (S901 → S880) are both carried; S894 refused with flip. Item 10's re-grounding mandate explains the rewritten text.

## Findings (by severity)

- **BLOCKER: none.** The counter at the landed revision scores 11/11 (C) and 9/9 (Ca); no claim leg or admitted statement checked false.
- **MAJOR: none.**
- **MINOR G1 — wave-4 quarantine-first chronology is inherited from round 72, not asserted in-round.** Round-72's prompt carries item 10 with the wave-4 clause (kotodama-round-72.md:489–490), and round-72 adopted anyway, citing rounds 68–71 pre-directive verdicts as the discharged slice check (round-72 lesson:57). Round 73 (third round under the lane's reading) therefore inherits "adoption open"; the round-73 lesson line 95 ("slice … verdicted in rounds 68–71 and is not re-derived here") rests on that same reading, while item 10's text says the lane's *first* round under the item adopts nothing and hand-checks the full slice. If the dispatch order makes round 73 the first binding round, the two-entry admission would conflict with the clause; I could not verify dispatch timestamps (only prompt-file mtimes and commit dates). Fix: a one-line supersession note in the lesson pinning which round discharged the wave-4 duty and why (precedent: lesson round-72:57).
- **MINOR G2 — the full reg-ids/staged-ids lists are referenced by path+count, not pasted verbatim.** ExecRenumber.md (w1) pastes the 17-row collision list and the counts (799/132/17) and cites the files; the lesson repeats the counts. Item 10's "paste both id lists, the collision count and the renumber map" is thus substantially met (collision list and map are fully pasted; registers by file+count). If the strictest reading demands full 799- and 132-line paste, add them to a report annex. Not a claim-leg failure (COLLCHECK passes).
- **MINOR G3 — `tools/check-gate-quotes.py` is declared not the cap check** (lesson:67–68); quotes were counted manually (wc -w). I manually verified all five Gate quotes ≤25 words (16/9/24/16/25), so no defect, but the cap rests on manual counts.

## What I could NOT check

- **Live reachability of the five cited sources today.** This seat performed no fetches; the evidence captures are asserted at 2026-10-25 with HTTP 200, bytes and sha256. Verifying them would require re-fetching — not done.
- **Runtime write-history into shokuknow.** Static review of committed artifacts shows no write claims; actual process behavior of earlier sessions is not provable from bytes.
- **Exact dispatch order/timestamps of rounds 71/72** (only file mtimes and commit dates available) — the wave-4 reading in G1 depends on it.
- **The S894/S910 wall rulings** (Cambridge 429, Springer challenge) beyond the filed evidence and Gate rows — not re-probed by this seat.

## Verdict summary

The assimilation contract's obligations are satisfied by committed artifacts at 0316b88 with the two minor notes above; nothing found false, vacuous, stale, unsupported or harmful in the executed assimilation of the landed bytes. Both counters pass at the landed revision in a throwaway clone; census exit 0; CITEDLINES clean; receipt-before-append ordering holds; guard proof holds; evidence captures committed pre-data; folded pair handled per checklist item 6; refused entries kept with reason+flip; Gate carries ≥1 admit and ≥1 reject.
