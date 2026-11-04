# Round 82 verifier spot-check — kotodama (non-author)

author: hyaku closure (non-author integrator, @m_zfl)
Round: kotodama 82 · base `c285b2afb19d4b64320e18df1f55e426bf2d0b0c` ·
lane tip `1d650c8c321607b65a25e5f916173f3106911ff1` · report
`.ufo/reports/round-82/kotodama.md` (fleet `b65e613b…`).
Verified 2026-11-04 on Linux/omp, fleet root `/home/vgpnk/Projects/shokunin`,
lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. I did not author this
round and did not improve it.

## 1. Conformance (step 1)

- **Report authorship and ordering.** `git -C <fleet> log --format='%an | %H' -- .ufo/reports/round-82/kotodama.md`
  → `kotodama-shokunin | b65e613bf644c530da4ded3b153fa7deea5f48ca` (lane
  identity, 2026-11-04 08:48:00 -0300), 35 s after the lane tip
  `1d650c8c` (08:47:25) — the report lands last and cites the records commit.
- **`SHONEN` heading.** Present, under `## SHONEN`, with one line per box
  (four `[~]` lines, each carrying a pointer). No `[x]` is claimed.
- **Cited commits.** All 13 lane hashes named by the report exist and pass
  `git merge-base --is-ancestor <h> main` against the branch ref (the repo is
  jj-colocated, HEAD detached at `1d650c8c`):
  `25907323`, `41c6de89`, `696835ee`, `ea667212`, `d1129213`, `277fdf4a`,
  `7d3a5bcd`, `fafa3ea5`, `3bb408ae`, `6c525ba4`, `3a59daaf`, `1d650c8c`,
  `c285b2af` (base) — 13/13 `OK-ANC`.
- **Repo state.** `scripts/hyaku/jj-lane.sh state <lane>` → `branch=main
  local=1d650c8c… remote=1d650c8c… ahead=0 behind=0 head=detached tracked=0
  untracked=0`; `git status --porcelain` empty. No uncommitted round work,
  pushed.
- **Dispatched prompt.** `.ufo/prompts/kotodama-round-82.md` is committed by
  the lane identity (`9114dbc6`, “hyaku inline attempt 1”) and carries the
  template contract: §1 MISSION/AXES binding, §2 claims, §2b frontier step,
  §3 L2 floor (one batched call, ≥8 seats), §4 report contract with the
  required sections and marker rule, §5 commit/push scope and L0 side channel.
  The five child-lane items are present: report path (absolute), commit-then-
  push and report-last ordering, `SHONEN` heading, commit-hash citation, write
  scope. The §6 run-15 route map it quotes names `task.agentModelOverrides`
  in `~/.omp/agent/config.yml` as the authority; `MISSION.md` §L2 states its
  role-class buckets as advisory, so no alias-level contradiction is
  checkable — observed, not a defect.
- **Report contract.** The six required sections appear in order (work
  performed, landed changes, before → after, sources & frontier, trend
  verdicts, SHONEN); every landed change is tied to a LOG entry and a commit.
  Real committed work, not a marker → lane status `ok`.
- **Wave.** `spec-v1.json`: 14 items under the 8–16 band; roles 3 scout,
  3 executor, 2 scribe, 1 connector, 2 critic, 1 mutation-tester, 1 sentinel,
  1 reviewer = 14; attack share 4/14 = 29 % ≥ 25 %; one connector. `w1-results.json`
  carries 14 named seat outputs, no dead seat; `w1.ready` + `.dispatched`
  present; `w1-dispatch.json` has one `taskCall` with 14 tasks.

Conformance defects are named in §6; per the closure rules they are
status-neutral and do not bar admission.

## 2. Claim re-checks

### Claim O — operability, capability acquisition (`tools/check-sources-recheck.py`)

Re-measured (tool run by me, not evidence-quoted):

```text
$ git ls-tree --name-only c285b2af… tools/ | grep -c recheck
0
$ git grep -c RECHECK-QUEUE c285b2af… -- tools/ reports/ | wc -l
0
$ git show 25907323…:corpus/SOURCES.md > /tmp/…/SOURCES.md   # sha256 2f60171c8879f99e…
$ python3 tools/check-sources-recheck.py --selftest
SELFTEST: PASS (13 checks)                       # exit 0
$ python3 tools/check-sources-recheck.py --registry … --as-of 2026-11-04 --window 90
RECHECK-QUEUE: 0 due / 18 upcoming / 14 on-release / 827 rows
$ python3 tools/check-sources-recheck.py --registry … --as-of 2027-11-01 --window 90
RECHECK-QUEUE: 813 due / 0 upcoming / 14 on-release / 827 rows   # 813 DUE lines
$ python3 tools/check-sources-recheck.py --registry .ufo/waves/round-82/w1/stage/ExecEvidence/probes/12-cell-row.md --as-of 2026-11-04
RECHECK-ERROR line 5: row has 12 cells, expected 11             # exit 2
```

Gate evidence verified, not executed (PROTOCOL §Gate standard):
`reports/round-82/telemetry/lands-o82-graded-r3.txt` — `ACCEPT-O-82: PASS
legs=7/7`, stamped/evaluated `41c6de89`, measured main `696835ee`, tree
`1047ebb7`, counter sha256 `07e4b2db…`, config read from freeze `25907323`
(sha `4cabb5ad…`); `selftest-o82-r3.txt` 16 checks; `controls-o.txt` refuses
at `--lands`=base; `junk-o.txt` JO1–JO3 each fail on the named leg with the
clean fixture green first.

Precision note (not a claim failure): “at base nothing read the registry's
`recheck` cells” is broader than its two sweeps support — base
`tools/check-row-fragments.py:131` binds the cell as `_recheck` (ignored) and
`tools/check-supersession-settlement.py:90` unpacks it unused. The absent
capability the claim actually demonstrates is the due-date derivation/queue,
and that is 0 at base and present after.

**Verdict: improved** (claims measured at `41c6de89`).

### Claim D — depth (`corpus/knowledge/myth-symbol/guest-right-hospitality-law.md`)

Re-measured:

```text
$ git ls-tree -r --name-only c285b2af… corpus/knowledge | grep -c '\.md$'
255
$ git ls-tree -r --name-only 1d650c8c… corpus/knowledge | grep -c '\.md$'
256
$ git show c285b2af…:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}…'    # 827
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md           # 832
$ wc -c corpus/knowledge/myth-symbol/guest-right-hospitality-law.md
29719
$ sed -n '/^## 3\. Attested anchors/,/^## 4\./p' <entry> | grep -cE '^- '        # 22
# each of the 22 bullets carries exactly one distinct S-id (awk over the same span → 22×1)
$ python3 tools/check-cited-lines.py <entry>
CITED-LINES: 0 finding(s) in 1 file(s)           # exit 0
```

Gate evidence verified: `lands-d82-graded-r4.txt` — `ACCEPT-D-82: PASS
legs=8/8`, stamped/evaluated/measured `6c525ba4`, tree `93febbb8`, counter
sha256 `767f3962…`, config from re-freeze `3bb408ae` (sha `25bd11c5…`);
`selftest-d82-r2.txt` 13 checks; `controls-d.txt` refuses at base;
`junk-d.txt` JD1–JD3. `lands-d82-graded-r2.txt` is a genuine red-before:
`LEG FAIL SEPARABLE (foreign: ['corpus/QUALITY.md'])` FAIL 7/8, answered by
the r3 re-freeze `3bb408ae` (adds the already-landed claim-C path to
`sibling_paths`; constants only, and the D verdict does not read it).
`git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'` = 256.
The base absence clause re-derives: filename sweep 0 of 255; institutional
core `xenia|hospitium|guest-friend|theoxeny` 0 lines.

**Verdict: improved** (measured at `6c525ba4`).

### Claim C — calibration (QUALITY criterion 30 + a falsified reject ground)

Re-measured:

```text
$ git show c285b2af…:corpus/QUALITY.md | grep -c '^30\. '
0
$ grep -c '^30\. ' corpus/QUALITY.md
1
$ grep -n '^30\. ' corpus/QUALITY.md
207:30. **A "no quotable prose" reject records a folded re-read and a capture probe before it is filed** …
```

The criterion names its scope, the two read guards (tag→separator,
U+00A0/U+2003→space), the required `raw <n> / folded <m>` record, the
same-page capture probe, a red-before check, its limits, and its grounding.
The falsified ground re-derives independently: live
`…/1911_Encyclopaedia_Britannica/Mint` HTTP 200, 148,302 decoded bytes,
27 `</p>`, opening span present once; capture `20260608000413` HTTP 200,
122,055 bytes, 28 `</p>`, span present once. Round-81's filed ground is at
`corpus/lessons/round-81.md:80–81` and `:155–156`; the correction is kept as
append-only history (criterion 30 says “round 81's filed reject stands as
history”).

**Verdict: improved** (measured at `3a59daaf`).

## 3. Axis verdicts

| axis | claim | verdict | basis |
|---|---|---|---|
| operability | O | improved | tool lands, selftest 13, both queue readings re-derived, gate `PASS legs=7/7` at its lands |
| depth | D | improved | 256th knowledge file, 22 single-id anchors, lint 0, rows 827 → 832, gate `PASS legs=8/8` |
| calibration | C | improved | criterion 30 present (0 → 1); its falsified ground re-measured live and in capture |
| coverage | — | unchanged | the four rows are the D move itself, no new surface beyond its scope |
| freshness | — | unchanged | round-11 L0 pause stands; no live source re-verified for an existing entry |
| adjacency | — | unchanged | transclusion/Parsoid observation reported in the lesson, not absorbed; `git diff-tree -r --name-status c285b2af 1d650c8c -- PROVINCE.md` empty |

No axis is harmed: `git diff c285b2af 1d650c8c -- SCORECARD.md` adds the
round-82 section and one capability row and lowers no recorded score.

## 4. Discernment spot-check (non-author, LEARNING.md)

Re-opened each source myself (plain requests, 2026-11-04). Quotes are counted
on the fetched bytes with tags→separator and nbsp/U+2003→space for the folded
count.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S904 Odyssey xiv / D admit | admit, tier A | `https://www.gutenberg.org/cache/epub/1727/pg1727.txt` (717,782 B; sha256 `b167ce5e…` matches the record) | agree | 「for all strangers and beggars are from Jove」 present exactly once, raw-contiguous, Book XIV (swineherd Eumaeus to the disguised Odysseus); the byte count and quote location are as filed; 8-word quote ≤25 |
| S905 Germania xxi / D admit | admit, tier A | `https://en.wikisource.org/wiki/Germania_(Church_%26_Brodribb)` (163,266 B decoded) | agree | 20-word span present once folded, ch. XXI, immediately inside the feud/heritable-enmity passage the row's `teaches` names; tier A is right for the ethnographic statement |
| S906 Metamorphoses viii / D admit | admit, tier B | `https://www.gutenberg.org/cache/epub/26073/pg26073.txt` (853,821 B) | agree | span present once folded (viii, Baucis and Philemon); the record's honest `raw 0 / folded 1` is explained by the line wrap after “them,” and the nbsp in the preceding sentence — this is the QUALITY-30 shape, disclosed before the criterion binds; tier B for a 19th-c. translation is right |
| S907 EB11 “Guest” / D admit | admit, tier C | `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Guest` (60,273 B decoded) | agree | 9-word gloss present once folded; the article is a dictionary gloss with no institutional content, so tier C and “never sole support” is the correct scope; the `note:` on the first read matches the page's Parsoid template block |
| S908 Frazer / D reject | reject, tier C | `https://www.gutenberg.org/cache/epub/3623/pg3623.txt` (2,331,343 B) | agree | the 16-word span is present once and is the stage-law sentence (“a false science as well as an abortive art” follows); the row rejects framework status, not the sentence's existence, and names the flip. Stricter than QUALITY 2's literal flag-on-first-use, but a rejection is taste kept with its reason — no harm, and the stricter read is stated |
| Claim O tool | admit (capability) | re-ran `tools/check-sources-recheck.py --selftest` and both as-of readings over the frozen blob | agree | 13 checks; `0/18/14/827` and `813/0/14/827` reproduce exactly; 813 `DUE` lines at the projection date; malformed committed fixture exits 2 with a labelled error and no traceback |
| Claim C overturned ground (round-81 EB11 “Mint”) | reject overturned | live Wikisource page + `20260608000413` capture | agree | folded re-read finds the article prose in both (27 and 28 `</p>`; span once); the round-81 ground was an extractor artifact, and the correction is filed as a criterion plus history, not a rewrite |
| Claim D entry | admit | `corpus/knowledge/myth-symbol/guest-right-hospitality-law.md` | agree | 29,719 B, provenance trio first, six decisions, five-field lexicon with worked derivation, 22 anchors one S-id each, canon handoff present, lint 0 |

Result: 8/8 sampled decisions agree; one of them (the Mint reject) is a
disagreement the gate itself found and turned into criterion 30, which is the
learning the discernment trend counts.

## 5. Trend verdicts

- **expansion: improved.** Re-measured: knowledge files 255 → 256 and
  registry rows 827 → 832 at `1d650c8c`; the new entry sits on ground no file
  owned at base (filename sweep 0 of 255, institutional core 0 lines) and its
  four `mined` rows were opened this round and are cited by it; one new
  capability row (`registry recheck-cadence auditor`) enters SCORECARD.
- **quality: unchanged.** No existing entry was re-verified, deepened or
  superseded this round; `QUALITY 20` excludes instrument work from this
  observable, and the new entry is expansion, not a re-verification pass.
  No admitted entry fails its re-check.
- **discernment: improved.** A measured lesson produced a grounded criterion
  (QUALITY 30), a filed reject ground was re-measured and falsified with the
  disagreement kept as append-only history, the round's own repeat of the
  same artifact is mined (R82-M1), and this non-author spot-check agrees on
  every sampled admit and the reject.

`improved`/`unchanged` only; no trend is `harmed`.

## 6. Routed defects (lane to fix next round)

1. **Empty record cited as evidence.** `reports/round-82/counter-revisions.md`
   is 0 bytes at `1d650c8c` (`git cat-file -s HEAD:reports/round-82/counter-revisions.md`
   = 0) while the report (§Work performed, “Record:”), SCORECARD and the
   lesson cite it as the counter-revision record. Land the record bytes (or a
   superseding record) and point the citations at it.
2. **Line-number erratum.** The report's R82-M2 parenthetical and the lesson
   row R82-M2 say `RECHECK-ERROR line 7`; the committed probe
   (`.ufo/waves/round-82/w1/stage/ExecEvidence/malformed-row-probe.txt:7`) and
   the committed fixture print `line 5`. Append a named erratum in the next
   round's report/lesson — the filed bytes stay as history.
3. **Gate registry rows missing.** `accept-o82` and `accept-d82` have no rows
   at the lane's registry home (`SKILL.md` `## Gates and probes`; the table's
   last accept rows are `accept-c-75`/`accept-ca-75`, so rounds 76–82 are a
   standing gap). The Gate standard requires name, kind, entry command,
   verdict map, self-test, pinned values, write scope and owner.
4. **Lesson `## Gate` omits per-row URL and access date.** CORPUS.md rule 1
   asks the Gate to record, for every new row, the URL, the access date and
   the ≤25-word located quote; the quotes/word counts/locations are present
   but the URLs and dates live only in `SOURCES.md`. Add them in the next
   Gate block.
5. **S908 row shape.** Its `teaches` opens `rejected:` (contract spelling
   `REJECTED:`), and its `anchor` cell names no chapter/page — the location
   (“chapter III”) exists only in `reports/round-82/evidence/reject-golden-bough.txt`.
   Correct as a superseding row or a shape fix, not an in-place rewrite of
   the filed reason.
6. **Scratch-path commands in committed receipts.** `malformed-row-probe.txt`
   and `quality30-probe.txt` cite `/fast/scratch/…` (and a `/tmp` working
   copy in this closure's re-check, deliberately not used as evidence). The
   committed fixtures make them re-runnable, but cite repo-relative paths
   next round so the pointer resolves at closure.
7. **Claim O before-wording (low).** Rephrase “nothing read the registry's
   `recheck` cells” to “no tool derived a due date or queue” — the narrower
   statement is what the two sweeps prove and what the claim demonstrates.
   The claim stands either way.

Promotion note (operator-owned): all four `SHONEN` boxes are `[~]` with
resolvable pointers; boxes 2–4 look checkable by a non-author from committed
bytes, and box 1's three pointers resolve (`SKILL.md:20`, `:505`, `:564`).
No `[x]` was written by this verifier, and promotion is not decided here.
