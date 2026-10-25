# ScribeQuality22 — criterion 22 draft (round 73, W1)

Seat: scribe (draft-only). Lane: `kotodama-shokunin`, worktree HEAD == base
`8841ad3b896a0227674fa0725b818c999118046f` (read-only; no jj/git write).
Report path: `.ufo/waves/round-73/w1/ScribeQuality22.md`
Report: .ufo/waves/round-73/w1/ScribeQuality22.md

## Behavior (deliverable)

Drafted `corpus/QUALITY.md` criterion 22 as text only, at the path the item
names: `.ufo/waves/round-73/w1/drafts/quality-22.md` (1 line, 1877 chars,
sha256 `efd7d14850d548a5417d249c3255b0e7331b5159ca6fcf07cd1c3b17f54e4a1d`).
House style of criteria 20/21: one physical line per criterion (QUALITY.md
lines 61 = 570 chars, 63 = 1164 chars; the file holds 21 criteria and ends with
`\n`). Content, as drafted (verbatim):

```
22. **A wall reject carries its UA record** — adds to criterion 21 (the probed URL) and criterion 10 (ordinary means). A Gate reject whose ground is a challenge, wall, HTTP 403 or 429 records in its Gate line (a table row or one prose line), verbatim, the first probe's exact User-Agent with its status line, then the retry under an ordinary browser UA (Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36) with its status line, in the form `UA=curl/8.7.1 → HTTP 403; retry UA=Mozilla/5.0 … → HTTP 403`. A wall that persists under that UA stays a valid reject only with the second status line beside the first; a reject filed on one status line, or on a UA its line does not name, is unverified (criterion 12); a second line that serves the page (2xx) must name the challenge marker it saw, or it falsifies the reject, which is then re-scoped, not rejected. Browser automation and solved captchas remain forbidden (criterion 10) and are never the retry. Check: each such reject line matches `grep -qE 'UA=[^ ]+ .*HTTP [0-9]{3}.*retry UA=Mozilla/5\.0 .*HTTP [0-9]{3}'`; a line missing the record exits 1 — shown able to fail on corpus/lessons/round-72.md:31-32 (Gate reject rows carrying no UA record, exit 1) and corpus/lessons/round-71.md:34 (a CAPTCHA-wall reject, exit 1), and passing on a record-bearing line (exit 0). The grep proves shape and order only — never that the UA strings are verbatim, that the retry ran, or whether a 2xx second line is a served page or a challenge; a reviewer re-probes. Grounded in corpus/lessons/round-72.md:103 (the UNESCO "live CAPTCHA wall" was a UA artefact: browser UA served HTTP 200, plain curl walled) and the round-71 reject sweep at corpus/lessons/round-71.md:33-40, whose wall rejects carry no UA at all; drafted by seat ScribeQuality22 (`.ufo/waves/round-73/w1/ScribeQuality22.md`).
```

Required elements, each present: (a) a wall/challenge/403/429 reject records
the exact first-probe UA + its status line and the browser-UA retry + its status
line, verbatim, on the Gate line; (b) a wall that persists under the browser UA
stays a valid reject only with the second status line; (c) browser automation
and solved captchas stay forbidden under criterion 10, never a retry; (d) one
named grep as the red-before check; (e) grounding in `corpus/lessons/round-72.md`
§Routed to round 73 (post-landing, ScoutCDXCanonical) at line 103.

## Red-before check (one grep, run on real lesson bytes)

The check is the single `grep -qE` the criterion names. I extracted it from the
draft's own bytes (`grep -oP "grep -qE '\K[^']*"`), confirmed it equals the
string I tested (`EXTRACT-EQ-TESTED: yes`), and replayed it:

| input (line under test) | provenance | grep exit | required |
|---|---|---|---|
| constructed record-bearing row (`UA=curl/8.7.1 → HTTP 403; retry UA=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36 → HTTP 403`) | `/tmp/ScribeQuality22/pass-constructed.txt` | 0 | 0 |
| `corpus/lessons/round-72.md:31` (real Gate reject row, no UA record) | extracted verbatim to `/tmp/ScribeQuality22/fail-r72-31.txt` | 1 | 1 |
| `corpus/lessons/round-72.md:32` (real Gate reject row, no UA record) | `/tmp/ScribeQuality22/fail-r72-32.txt` | 1 | 1 |
| `corpus/lessons/round-71.md:34` (real wall reject: "ich.unesco.org live CAPTCHA walls", no UA) | `/tmp/ScribeQuality22/fail-r71-34.txt` | 1 | 1 |
| `corpus/lessons/round-71.md:38-39` (real wall rejects: `live 403`, no UA) | `awk 'NR==38||NR==39'` | 1 | 1 |
| control: browser UA only, one attempt | `/tmp/ScribeQuality22/ctl-one-status.txt` | 1 | 1 |
| control: plain UA + retry with no second status | `/tmp/ScribeQuality22/ctl-no-second-status.txt` | 1 | 1 |
| tolerance: `UA=Wget/1.21.4` + Safari-macOS retry; `UA=python-requests/2.31.0` + Firefox retry | `/tmp/ScribeQuality22/ctl-tolerance.txt:1-2` | 0, 0 | 0, 0 |
| limit evidence: `UA=curl/8.7.1 → HTTP 403; retry UA=Mozilla/5.0 … → HTTP 200` | `/tmp/ScribeQuality22/ctl-tolerance.txt:3` | 0 (the grep cannot reject a served 2xx — hence the prose rule) | 0 |

File-level red before the criterion exists:
`grep -nE '^\|.*\| *(rejected|refused) *\|' corpus/lessons/round-72.md | grep -vcE "$RX"`
prints `2` against a total of `2` Gate reject rows — every round-72 reject row
fails the record check. `grep -nE 'UA=|User-Agent|Mozilla|curl/' corpus/lessons/round-72.md`
answers NONE, and the round-71 sweep at lines 33-40 also carries no UA token
(awk over that range, `grep -nE 'UA|User-Agent|curl|Mozilla'` → NONE).

## Quoted lesson lines (located, each ≤25 words under `wc -w`)

- `corpus/lessons/round-72.md:103` — "The UNESCO \"live CAPTCHA wall\" was a UA artefact" (9 words); "all eight element URLs serve HTTP 200 full narrative under a browser-shaped UA" (14); "the wall appears only with a plain-curl UA" (9).
- `corpus/lessons/round-71.md:33` — "rejected this round: ScoutOpenSourcesC refused 8 candidates for claim C —" (11).
- `corpus/lessons/round-71.md:34` — "ich.unesco.org live CAPTCHA walls (flip: Wayback captures of the same elements," (11).
- `corpus/lessons/round-71.md:38-39` — "Princeton Noh (live 403; flip: Kabuki)" (6); "Britannica/RAD live 403 (flip: Wayback)" (6).
- `corpus/lessons/round-72.md:31` — "staged row's quoted span absent from the fetched page" (9).

## Gates (read-only; nothing run as a product verification)

| command | observed |
|---|---|
| `wc -l`/`awk length` on the draft | `lines=1 chars=1877 bytes=1890`; `^22\. ` count 1; numbered-criterion lines 1 |
| `sha256sum .ufo/waves/round-73/w1/drafts/quality-22.md` | `efd7d14850d548a5417d249c3255b0e7331b5159ca6fcf07cd1c3b17f54e4a1d` |
| `grep -oP "grep -qE '\K[^']*" <draft>` then compare with the tested string | equal (`EXTRACT-EQ-TESTED: yes`); replay reproduces 0/1/1/1/1/1 over the six fixtures |
| `awk '{printf "%d:%d\n", NR, length($0)}' corpus/QUALITY.md` | 61:570 (criterion 20), 63:1164 (criterion 21), 21 criteria, file ends `0a` |
| `tail -c 1 corpus/QUALITY.md \| xxd` | `0a` (newline-terminated; blank lines separate criteria at 58/60/62) |
| `grep -c 'QUALITY' reports/round-73/claims.json` | `4`; `quality_candidate` names "QUALITY 22 — UA-record clause for 'wall/CAPTCHA' rejects" |
| `grep -n 'QUALITY' reports/round-72/accept-ca.py` | `:91` QUAL20 leg (`re.findall(r"^20\. ", q, re.M)`, count == 1), `:170` append-only filed set includes `corpus/QUALITY.md` |
| `git rev-parse HEAD`; `git ls-files --others --exclude-standard .ufo/waves/round-73` | HEAD == base `8841ad3b`; both my files untracked |

No live fetch was made and no download occurred, so no User-Agent was used and
no fetch-hygiene record applies to this seat. No tool installed or upgraded; no
package manager invoked.

## Touched surfaces

- Wrote `.ufo/waves/round-73/w1/drafts/quality-22.md` (draft criterion, 1 line).
- Wrote `.ufo/waves/round-73/w1/ScribeQuality22.md` (this report).
- Scratch only in `/tmp/ScribeQuality22/` (grep fixtures: `pass-constructed.txt`,
  `fail-r72-31.txt`, `fail-r72-32.txt`, `fail-r71-wall.txt`, `fail-r71-34.txt`,
  `ctl-one-status.txt`, `ctl-no-second-status.txt`, `ctl-tolerance.txt`).
- No edit to `corpus/QUALITY.md`, `corpus/lessons/**`, counters, tools, claims,
  LOG/SCORECARD/SKILL/SOURCES, the fleet repo or `shokuknow`; no commit, push,
  jj or git-index write.

## Findings for the L1 / attacking seats

1. **Draft is leg-shaped.** QUALITY.md is one physical line per criterion and
   `reports/round-72/accept-ca.py:91-93` grades criterion presence with
   `re.findall(r"^20\. ", q, re.M) == 1`. The draft is a single line starting
   `22. `, so the same leg shape for 22 counts 1. No round-73 counter exists at
   base (`reports/round-73/` holds only `claims.json` and `telemetry/`), so no
   frozen leg reads criterion 22 unless the L1 adds a QUAL22 leg.
2. **Append mechanics.** QUALITY.md ends `0a` and separates criteria with blank
   lines (58/60/62 are empty). The landing append must therefore be a blank line
   then the criterion line — a bare concatenation would leave 21's line and 22's
   line unseparated. QUALITY.md sits in accept-ca's append-only filed set
   (round-72 `accept-ca.py:170`), so the append must remove zero lines; the draft
   removes none.
3. **The in-scope red is round-71, not round-72.** Round-72's two Gate reject
   rows are quote-absence rejects (no wall ground), so they prove the predicate's
   red but are not offenders under the criterion's scope. The real wall rejects
   are `corpus/lessons/round-71.md:34` (`ich.unesco.org live CAPTCHA walls`) and
   `:38-39` (`live 403` twice), both exit 1, and lines 33-40 carry no UA token at
   all. A reviewer should not read the round-72 citation as "round 72 filed a bad
   wall reject"; the criterion text says only "Gate reject rows carrying no UA
   record".
4. **The grep is not overfitted.** It passes `UA=Wget/1.21.4`,
   `UA=python-requests/2.31.0`, Safari/macOS and Firefox browser UAs, so it does
   not force curl or Chrome; verbatimness of the UA is prose, not shape. The two
   negative controls (one attempt; retry with no second status) exit 1, so the
   "second status line" clause is mechanically enforced.
5. **Stated limits, and the weakest leg.** (a) The grep proves shape and order
   only — it cannot see whether the UA strings are verbatim or whether a retry
   happened; (b) a 2xx second line matches the grep, so the "serves the page ⇒
   re-scope, not reject" rule is review-only; (c) the grep does not decide
   "wall-grounded" — the selector is the closure's, so a scout who mislabels a
   wall as "unreachable" or "no quotable passage" escapes the selector. (c) is the
   attack surface: criterion 12's re-test-tool output and a reviewer re-probe are
   the only catches, and they are not mechanical.
6. **Interplay with 10 and 21.** Criterion 21 already requires every Gate reject
   to name the URL it rejected; 22 puts the UA record on that same line, so a wall
   reject line carries both. Criterion 10's `tools/check-source-access.py` reads
   bypasses a *row* reports in its cells, not lesson lines, so 22 adds a
   lesson-side record the checker does not see — no overlap, no double-count, and
   the automation/captcha ban stays where 10 puts it.
7. **One discretionary clause beyond the item's must-list.** "A second line that
   serves the page (2xx) must name the challenge marker it saw, or it falsifies
   the reject" is mine, not the item's. It closes the loophole that a retry which
   actually serves the source still reads as a valid wall reject. If the L1 trims
   it, the three required elements and the named grep still stand.
8. **R1 class (round 73).** Both files are untracked at base
   (`git ls-files --others --exclude-standard .ufo/waves/round-73` lists them
   among the w1 seat files); the L1 must commit them, since untracked w1 seat
   files are exactly the R1 defect the round is repairing.

## Out of scope (not done, by design)

- No edit to `corpus/QUALITY.md`: criterion 22 is drafted text only, not landed
  bytes.
- No counter run (no round-73 counter exists), no claim attack, no judgment, no
  commit/push/jj write, no message to another seat, no delegation.
- No live probe of any wall, no User-Agent used, no download, no tool install.

## Artifacts

- Draft: `.ufo/waves/round-73/w1/drafts/quality-22.md` (sha256 `efd7d148…`)
- Report: `.ufo/waves/round-73/w1/ScribeQuality22.md`

## Inbound IRC, not this seat's scope — flag RETRACTED by its sender (2026-10-25)

`R50ReopenRowS105` first flagged `corpus/evidence/round50/spans.tsv` as recording
S105 quote offsets uniformly −80 in the tail (创建文件夹… 27507 vs 27587;
第 6 章 辅助功能 30581 vs 30661) and −48 at the head (edition line 0 vs 48)
against capture `e3ca8f4fdd15420b80096a75.txt` (sha `2197abe2…`).

**The sender retracted it in a second message.** The `offset` column is the
span-block start, not the quote position: `start = max(0, off − CONTEXT)` with
CONTEXT=80 (`build-spans.py:44,119`; docstring lines 17–18/25 name
`offset + quote's position in span` as the anchor char N). The sender re-verified
S105-1/2/8/34 as `capture[off:off+len(span)] == span_file` exactly, quote at
span-index 80 (48 for the clamped head row); peers re-verified all 55 rows with
0 mismatches. So the −80/−48 gap is the designed context window, not drift, and
there is **no defect** — only a naming note that the bare header `offset` is
mildly ambiguous against the entries' `char N` quote positions. The sender's
report `.ufo/waves/round-50/w2/R50ReopenRowS105.md` is corrected and row S105
survived re-open.

Disposition: **neither message verified by me, and neither answered.** That
evidence tree lives in the sibling lane `chousa-shokunin`, outside this seat's
lane-read scope, and this seat's ticket is criterion 22 (no bearing on quote
offsets). I did not reply, per the seat rule against messaging other seats. This
section records the pair of messages so the retraction travels with the flag;
it is not evidence for criterion 22 and no number here was exercised by me.
