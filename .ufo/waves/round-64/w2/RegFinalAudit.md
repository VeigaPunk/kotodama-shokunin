# RegFinalAudit — final registry audit of the 32 staged round-64 rows

Seat: kotodama-r64.RegFinalAudit (wave 2, lane `kotodama-shokunin`, declaration 097c21d, base ff30a205).
Scope: every cell rule on staged `S718–S749`; tier/kind histograms; no row edited.

## Snapshot

Pinned copy of `.ufo/waves/round-64/rows/` at audit time (read-only) in
`/home/vgpnk/.cache/hyaku/kotodama-r64-w2/RegFinalAudit/snapshot/`; independent auditor
`audit.py` next to it. Row SHA256 prefixes (12 hex):

```
S718 ea6f005da340  S719 bfb71fac2c39  S720 8266e8a9a325  S721 ca997cf34d31
S722 9ea461e8f411  S723 880ac7497816  S724 76a5ee5a4c89  S725 c69873ed58b9
S726 da1dda3b407e  S727 300d28f1093e  S728 7323601a82b6  S729 6f501f88c997
S730 8db9e1ee7f18  S731 fa7bdf4a1ba3  S732 dbfffe578e08  S733 a75550a9eee4
S734 783bcec33438  S735 b69b020852ff  S736 08cf18578fb3  S737 aca195c0acd7
S738 e2833278e36b  S739 a9e6abc0a23a  S740 62c2cd1d55cf  S741 08b648a6fc9b
S742 1f6be952c841  S743 98a7e7e84ff7  S744 0f1537d80e4d  S745 bbbf080ffdc0
S746 05debaf3112c  S747 5007120c5d27  S748 2b7e06d78887  S749 64c6fdd5fd66
```

Volatile rows observed mid-write during the window (named, not judged as final): **S729**
was rewritten from the wave-1 Farran et al. 2016 duplicate of S718 to Neer et al. 2025
(`hash d3ac805ef9f9 → 6f501f88c997`); S722, S739, S747 were rewritten at 23:50–23:51,
minutes before the snapshot. `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir
.ufo/waves/round-64/rows` reproduces **32/32 clean** on this snapshot.

Method: independent parser re-reading every cell from disk; rules taken from
`gen-w2.py` (kind enum line 45; anchor line 46; ROW shape line 72 `<one grounded learner
benefit, <= 25 words>`; self-check line 96) and from `reports/round-64/accept-c.py`
(ROWS/REJECTS/LINK semantics). Live anchor checks used the lane locator
`reports/round-61/reopen-quote.py <URL> "<quote>"` (no `--row`, rows are not integrated
yet). No tools installed.

## Per-row verdict table

`q` = quote words (first double-quoted span, counter-identical normalisation), `t` =
teaches words, `U` = used-by, `cap` = same-page archive capture in the source cell.

| id | kind | tier | q | t | status/date/recheck | U | cap | verdict |
|---|---|---|---|---|---|---|---|---|
| S718 | paper | A | 9 | 16 | mined/2026-10-23/180d | entry | yes | PASS |
| S719 | paper | B | 24 | 20 | mined/2026-10-23/180d | entry | yes | PASS (locator section 4, caveat phrase kept in quote) |
| S720 | paper | A | 24 | 20 | mined/2026-10-23/180d | entry | yes | PASS |
| S721 | paper | A | 18 | 13 | mined/2026-10-23/180d | entry | yes | PASS |
| S722 | paper | B | 17 | 17 | mined/2026-10-23/180d | entry | yes | PASS (section locator reworded; live LOCATED) |
| S723 | docs | B | 13 | **44** | mined/2026-10-23/180d | entry | yes | **FAIL — teaches 44 > 25** |
| S724 | book | B | 16 | 16 | mined/2026-10-23/180d | entry | yes | PASS |
| S725 | paper | B | 19 | 16 | mined/2026-10-23/180d | entry | yes | PASS |
| S726 | paper | A | 19 | 13 | mined/2026-10-23/180d | entry | yes | PASS (URL distinct from S737 by query id) |
| S727 | paper | B | 16 | 15 | mined/2026-10-23/180d | entry | yes | PASS (publisher abstract → B, correctly scoped) |
| S728 | book | B | 14 | 10 | mined/2026-10-23/180d | entry | yes | PASS (hedge "Frye relays Schieffelin's report" restored) |
| S729 | paper | A | 20 | 23 | mined/2026-10-23/180d | entry | yes | PASS (rewritten: Neer et al. 2025; meta + quote LOCATED) |
| S730 | book | B | 24 | 18 | mined/2026-10-23/180d | entry | yes | PASS |
| S731 | paper | A | 23 | 17 | mined/2026-10-23/180d | entry | yes | PASS |
| S732 | paper | B | 19 | 15 | mined/2026-10-23/180d | entry | yes | PASS |
| S733 | paper | A | 15 | 14 | mined/2026-10-23/180d | entry | yes | PASS |
| S734 | paper | A | 16 | 17 | mined/2026-10-23/180d | entry | yes | PASS |
| S735 | paper | A | 17 | 18 | mined/2026-10-23/180d | entry | yes | PASS ("tries to help" preserved) |
| S736 | paper | A | 10 | 15 | mined/2026-10-23/180d | entry | yes | PASS |
| S737 | paper | A | 25 | 16 | mined/2026-10-23/180d | entry | yes | PASS cells; **live re-check hit ConnectionResetError ×2** |
| S738 | book | A | 20 | 13 | mined/2026-10-23/180d | entry | yes | PASS (quote LOCATED in book PDF) |
| S739 | paper | A | 20 | 12 | mined/2026-10-23/180d | entry | yes | PASS (anchor now Results paragraph; LOCATED) |
| S740 | paper | A | 22 | **45** | mined/2026-10-23/180d | entry | yes | **FAIL — teaches 45 > 25**; live URL 403, capture HTTPError now |
| S741 | paper | A | 12 | 13 | mined/2026-10-23/180d | entry | yes | PASS |
| S742 | paper | A | 23 | 18 | mined/2026-10-23/180d | entry | yes | PASS cells; teaches still generic (setting only in scope+bullet) |
| S743 | paper | A | 10 | 18 | mined/2026-10-23/180d | entry | yes | PASS (nested curly quotes inside the span parsed correctly) |
| S744 | docs | B | 14 | 53 | rejected/2026-10-23/180d | — | no | PASS claim-C reject shape; quote unlocatable at live URL (redirect), TEST2 "quote-absent" |
| S745 | docs | A | 11 | 32 | rejected/2026-10-23/180d | — | no | PASS claim-C reject shape; live URL 403, quote unlocatable |
| S746 | docs | B | 17 | 45 | queued/2026-10-23/180d | — | no | PASS claim-C reject shape; no VERIFY/CAPTURE trailer |
| S747 | docs | B | **0** | 32 | rejected/2026-10-23/180d | — | no | PASS claim-C reject shape; **anchor carries no quote** (honest "wording not locatable", 403) |
| S748 | book | B | 11 | 45 | queued/2026-10-23/180d | — | `[UNRESOLVED]` | PASS claim-C reject shape; no VERIFY trailer |
| S749 | community | C | 21 | 25 | queued/2026-10-23/180d | — | no | PASS claim-C reject shape; C tier correct (community never A) |

Every row: exactly 11 cells, no empty cell, no `|` inside a cell, exactly one quoted span
except S747 (zero), all kinds inside `{spec, docs, paper, code, tool, dataset, talk,
book, community, own-work}`, all mined tiers A/B, all rejects `REJECTED:`/
`QUEUED-CANDIDATE:` + non-empty `; flip:` + used-by `—`.

## Histograms (staged vs registry)

| set | n | A | B | C |
|---|---|---|---|---|
| staged, all 32 | 32 | 18 (56.3%) | 13 (40.6%) | 1 (3.1%) |
| staged, mined only | 26 | 17 (65.4%) | 9 (34.6%) | 0 |
| registry S001–S717 | 643 | 406 (63.1%) | 228 (35.5%) | 9 (1.4%) |

Kind: paper 21, book 5, docs 5, community 1 (registry: docs 284, paper 202, book 108,
dataset 25, community 16, spec 6, tool 2). The mined set's A share is +2.3 pp over the
registry; no tier inflation was found on reread — review articles/abstracts
(S719, S722, S727, S732) are B, original studies A, open textbook B (S724), the
Nottingham RLO B (S723). The single C is the rejected Wikipedia row (S749).

## Findings

### Medium

1. **S723 teaches cell is 44 words (limit 25).**
   `…/rows/ScribeRowS723/row.txt`, cell 7: “Children of this age apply one simple word to
   many different referents (overextension) or hold one word to a single referent
   (underextension); both errors recede as vocabulary grows, so worldbuilders can treat
   early word breadth as a design variable rather than a fixed stage”.
   Rule: `gen-w2.py:72` `<one grounded learner benefit, <= 25 words>`. `accept-c.py` ROWS
   does **not** check teaches length, so the counter stays green while the row breaks the
   format. Fix: trim to ≤25 words keeping the over/underextension claim; do not touch the
   anchor or bullet (both pass; quote LOCATED).

2. **S740 teaches cell is 45 words (limit 25).**
   `…/rows/ScribeRowS740/row.txt`: “Documents that children overgeneralize noun titles
   (san versus chan, kun) rather than copying input verbatim, and that parental use of san
   for parent names does not grow with the child's age, so a designed address system can
   be rule-governed and still be mislearned.” Same rule, same invisibility to the counter.

### Low

3. **S747 anchor carries no verbatim quote.** Cell 6 now reads “Britannica Mortarboard
   entry, article lead (intended locator); live fetch 403 (Cloudflare challenge) on
   2026-10-23; wording not locatable”. The wave-1 fabricated meta-text anchor is gone
   (good), but the row-format rule “anchor carries a verbatim 8–25-word quote with
   locator” is unmet. `accept-c.py` REJECTS checks only shape/status/prefix/flip, so the
   claim is unaffected; record an explicit L1 acceptance or keep as the honest 403 record.

4. **S742 teaches stays generic.** “Gives worldbuilders a repeatable way to design
   explicit greeting instruction that builds peer welcome and shared classroom belonging.”
   The single-second-grade-classroom hedge lives in `scope` and in the (repaired) bullet
   (“In one second-grade classroom…”), not in teaches. Informational: wave-1 F5 is fixed
   where the entry text uses it; teaches overstates generality slightly.

5. **Reject rows carry no verification trailer and no capture.** S744–S749 have no
   `VERIFY:`/`CAPTURE:`/`ACCESS:` lines; S744/S745/S747/S749 have no `; capture` in the
   source cell and S748's is `[UNRESOLVED]`. Claim C exempts rejects from the capture
   rule, and S744's `TEST2: NOT_LOCATED … quote-absent` plus the rejection reasons are
   honest. Gap: the re-open evidence for S744/S745/S746/S748/S749 lives only in seat
   reports and the (pending) lesson Gate.

### Informational / dependencies

6. **Entry file absent at snapshot.** All 26 mined used-by cells name
   `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`, which does
   not exist in the lane (`ls` → ENOENT); `B2ExecEntry` proved assembly only in a scratch
   copy. FILE/ONEID/RESTATE/SWEEP/NO_HARM legs cannot pass until the L1 integrates.
   Not a row defect — dependency recorded, not judged.

7. **URL uniqueness holds.** 32 distinct live URLs, zero collisions with the 643-row
   registry when the query string is preserved. A query-stripped comparison produces
   false collisions (all `journals.plos.org/plosone/article` and `eric.ed.gov` rows
   collapse); note that `check-rows.py` keys duplicates on the raw URL string and
   `accept-c.py` `norm_url` drops the query, so LINK only passes because the full encoded
   URL is unique per line. S726 (`?id=ED252065`) and S737 (`?id=ED149852`) are distinct.

8. **S729 duplicate-of-S718 is resolved in the snapshot.** Wave-1 ReviewerRegistry F2/R2
   (26 rows bought 25 distinct works) no longer holds: S729 is now Neer, Brahmbhatt, Walsh
   & Warlaumont 2025, PLOS ONE 20(6):e0326569; live page meta matches the citation
   (title/authors/volume/issue/firstpage) and the 20-word anchor LOCATED. Because it was
   rewritten mid-window, the L1 must re-run check-rows + locator on the integrated bytes.

## Live anchor verification (independent, snapshot quotes)

Re-ran the lane locator on 26 of 26 mined rows: **24 LOCATED**, S737 `ConnectionResetError`
(ERIC reset, twice; row VERIFY says LOCATED — transient, not evidence of absence), S740
`HTTPError` on the live URL (403 confirmed by `curl -w %{http_code}`) and on its archived
capture now; S740's LOCATED claim rests on earlier seat evidence and is outside the LIVE
subset. Rejects: S744/S745/S747 unlocatable by design (redirect/403); S746/S748/S749 not
re-opened here (no live quote test run for queued rows beyond S748/S749's seat reports).

## Residual risk and verification gaps

- Teaches-length failures (S723, S740) are invisible to `accept-c.py`; only this audit and
  the row-format rule catch them. If the L1 integrates without trimming, claim C still
  passes but the "one grounded learner benefit ≤25" contract is false in the registry.
- S740's anchor is currently unverifiable at both live and archived URLs; treat its
  "verbatim" status as seat-attested until a reopen succeeds.
- Volatile rows (S729, S739, S722, S747) were written minutes before the snapshot; hashes
  above are the only reproducible state. Re-run `check-rows.py` after integration.
- The entry and the README/sweep integration are unproven in the lane; `ACCEPT-C-64` was
  not and could not be run here.
- `check-rows.py` weaknesses observed (not defects of the rows): teaches length unchecked,
  duplicate detection on raw URL strings, quote locator presence unchecked.
- The counter audited here is `accept-c.py` **revision 3 (pre-data)**, not rev 0: it adds
  the queued disposition, `teaches_copy` RESTATE rejection, the locator sha pin and the
  three-retry LIVE leg. Even at rev 3 it checks neither teaches length nor the kind enum,
  so findings 1–2 and the kind column rest on the row-format rule alone.
- `corpus/SOURCES.md` is modified only at S687 (mined→queued, the allowed APPEND
  exception); no S718+ row is integrated, so the 643-row registry histogram above is the
  correct base.

## Peer-relayed claim-O item, independently reproduced (outside row scope)

RevVerifyO2 reported that `accept-o.py` rev4's `m5` mutant is syntactically invalid as
landed. Reproduced here without editing any counter (read-only `ast.literal_eval` of
`MUTANTS`, exact single `str.replace` on `tools/reopen-row.py`, `py_compile`):

- `m5` replacement lands after the 8-space `target = …` line; its second line keeps 12
  spaces → `IndentationError: unexpected indent` at mutant line 605. Rebuilt mutant
  sha256 `795b8d196eec4b64344b39338bf73a3cc6a73c075671702d4b963959a6e6ecb6` (matches the
  seat's hash). The builder (accept-o.py:1086–1091) writes the replacement verbatim, no
  dedent → `MUT` cannot pass → `ACCEPT-O-64` cannot pass.
- Minimal fix verified: dedent the `if`/`else` to 8 spaces (bodies 12), keeping pins
  `["EDGE_SLASHLESS"]`. Corrected mutant sha256
  `804c9473d752833e143971b734f44b64d853e93f4edafbd64a64f504be35babc`, counter run
  `--only EDGE_SCHEMEREL,EDGE_SLASHLESS`:
  `EDGE_SCHEMEREL PASS rows=[('S2979', 'REFUSED', 1)] …`
  `EDGE_SLASHLESS FAIL rows=[('S2257', 'UNREACHABLE', 2)] … exit=1`.
  That satisfies the isolation check at accept-o.py:1115–1121 and `pinned_fail`.
- The rev4 docstring prose (accept-o.py:118) is inverted against the code: it says the
  `EDGE_SCHEMEREL,EDGE_SLASHLESS` run requires the former to FAIL and the latter to PASS,
  while the isolation check requires SCHEMEREL PASS and the pin requires SLASHLESS FAIL.
  A repair must fix both the replacement indent and that sentence.
- The seat's own rebuilt run (`EDGE_SCHEMEREL FAIL rows=[]`) was the invalid tool failing
  to run, not a genuine isolation violation; the corrected mutant isolates cleanly.

This is a counter defect, not a row finding; no counter or row was edited here.
