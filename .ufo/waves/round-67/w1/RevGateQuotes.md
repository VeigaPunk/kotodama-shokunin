# RevGateQuotes — gate-quote review, round 67 (reviewer leaf)

Reviewed 2026-10-24 12:32–12:48Z, refreshed 12:49Z (final binding audit on all 32 filled Gate lines); lane tip at review start `b78f8b8e` (@ empty).
Read-only: no installs/upgrades, no git/jj writes, no writes outside this seat's
report path. Snapshot note: the r67 `rows/` tree and `reports/round-67/accept-ca.py`
were both still moving while I audited (fragments landed 12:37-12:44Z; the L1 applied
a QUOTES-leg fix at 12:42:13Z and re-stamped the base receipts at 12:46:47Z); every
count below is timestamped.

Method. `tools/check-gate-quotes.py` on `corpus/lessons/round-66.md`,
`.ufo/waves/round-67/stage/lesson-draft.md` (in place of the unfiled
`corpus/lessons/round-67.md`) and `stage/gate-rows.md`; `--selftest` (52/52).
Then mutation tests of the detector's row-shape coverage, verbatim binding of every
Gate quote to its registry anchor cell and its `row-*.txt` fragment, a scan of all
registry `rejected` rows, mechanical execution of the QUOTES-leg expression against
the live counter bytes, and `tools/check-row-fragments.py` over the r67 rows tree.
No `lsp` device is exposed to this seat (none in the tool inventory; `xd://` lists
only `ast_edit` and `debug`), so semantic work used the lane's own checkers plus
Python; text grep only as the literal fallback.

## HIGH

### H1 (fixed 12:42–12:46Z; audit trail not preserved). The QUOTES leg was dead by construction at `b78f8b8e`
At `b78f8b8e`, `reports/round-67/accept-ca.py:272-276` read:

```python
gate_ids = set(re.findall(r"\bS(8[0-2]\d)\b", lesson_text)) & {f"S{n}" for n in range(805, 829)}
```

`findall` with a capture group returns the group only (`"805"`) and the intersection
is with **S-prefixed** ids, so `gate_ids` was always empty: executing the leg's own
dedented lines on a perfect lesson naming all of S805-S828 gave
`gate_ids = set() | leg passes = False` — ACCEPT-CA-67 could never print PASS, and
the base control could not detect it because it fails earlier on the absent lesson
(`telemetry/dry-run-ca.txt:13` → `QUOTES FAIL exit=2 gate_ids=0 clean=True`;
`w1/ExecCounterSmokeCa.md:77` had judged the leg "correct"). The r66 leg
(`reports/round-66/accept-ca.py:190`) had no intersection and counted correctly, so
this was a regression.
Current bytes (verified 12:44Z): the L1 applied `r"\b(S8[0-2]\d)\b"`; the same exec
now yields `gate_ids=24, passes True`, and `sha256(accept-ca.py)` is
`5382ffed6f6cbbec4d62bebd5131d2e1bb2d5b6ff621de32dec916010543653c`.
**Stale-pin resolved 12:46Z, audit trail not preserved.** The L1 re-ran
`telemetry/dry-run-ca.txt` and `controls-ca.txt` at base with the shipped counter:
both now pin `5382ffed…` (matching `sha256sum`), STAMP PASS at `ad5b52b0`, every leg
FAIL on base, `controls-ca.txt` says "revised counter rev1". But `grep -i
'original|preserv|supersed|pre-fix|5e8915'` on both receipts exits 1 — the earlier
bytes and the pre-fix sha are gone, while QUALITY criterion 17 requires the original
receipt bytes to stay preserved below a marker when a re-stamp corrects attribution.
Remaining gaps: (a) preserve the pre-fix receipt bytes below a marker (or record the
revision in the lesson’s telemetry note), and (b) add the perfect-lesson control —
nothing in the control set would have failed a dead QUOTES leg, and the fix is still
unproven by any committed receipt. `accept-c.py` (3e5f1a58) and `accept-o.py`
(f21e9b43) still match their receipts.

### H2. A quote-free Gate passes the QUOTES leg (verified on the fixed counter)
The id count is taken over `lesson_text`, not the `## Gate` section
(`accept-ca.py:272`), and `check-gate-quotes.py` only inspects quoted spans, so a Gate
whose rows quote nothing is clean. Executed with the current counter expression at
12:47Z:

| input | checker | gate_ids (fixed leg) | QUOTES |
|---|---|---|---|
| perfect lesson (24 ids, quotes) | 0 findings | 24 | PASS |
| `stage/lesson-draft.md` (32 Gate rows; 30 placeholders with no quoted span, only S825/S826 filled) | `GATE_QUOTES: 0 findings`, exit 0 | 24 | PASS |
| `stage/gate-rows.md` (28/32 filled) | 0 findings | 24 | PASS |

So inlining the skeleton's Gate (or landing with the 4 rows still MISSING) satisfies
Ca’s QUOTES leg while almost no Gate quote exists. Lands rule: every one of the 24 Gate lines
must carry a quoted span that is a byte-verbatim substring of its fragment anchor, and
a non-author must re-open a sample. Reproduce the hole with any quote-free Gate file,
then re-run after integration:

```bash
python3 -B tools/check-gate-quotes.py corpus/lessons/round-67.md   # exit 0
python3 -B - <<'PY'                                                # gate binding, exit 1 on a miss
import re,glob,sys
q=re.compile(r'"([^"\n]*)"|“([^“”\n]*)"')
lesson=open('corpus/lessons/round-67.md',encoding='utf-8').read()
gate=lesson.split('## Gate',1)[1].split('\n## ',1)[0]
frag={p.split('/')[-1][4:-4]:p for p in glob.glob('.ufo/waves/round-67/rows/*/row-S*.txt')}
bad=[]
for l in [x for x in gate.splitlines() if re.match(r'-\s+S\d+',x)]:
    sid=re.match(r'-\s+(S\d+)',l).group(1); qs=[a or b for a,b in q.findall(l)]
    if sid not in frag or not qs: bad.append((sid,'no-quote-or-fragment')); continue
    row=[x for x in open(frag[sid],encoding='utf-8').read().splitlines() if x.startswith('ROW=')][0]
    cells=[c.strip() for c in row.split('|')[1:-1]]
    if any(x not in cells[5] for x in qs) or max(len(x.split()) for x in qs)>25:
        bad.append((sid,'not-verbatim-or-over-cap'))
print('GATE_BIND:',bad or 'OK'); sys.exit(1 if bad else 0)
PY
```

## MEDIUM

### M1. `check-gate-quotes.py` false-green row-shape classes (mutation evidence)
On a copy of round-66.md, the canonical shape flagged a 26-word quote (exit 1); each
of these variants produced `GATE_QUOTES: 0 findings`, exit 0:

| variant of the S780 Gate row | exit |
|---|---|
| `- S780 \| "26 words" \| https://…` (house shape) | 1 |
| `\| S780 \| "26 words" \| https://…` (table row) | 0 |
| `- **S780** \| "26 words" \| https://…` (bold id) | 0 |
| 30-word quote hard-wrapped with a **column-0** continuation | 0 |
| same quote wrapped with an **indented** continuation | 1 |
| a second `## Gate` section carrying the only rows | 0 (only the first section is read) |

`ROW` requires the id as the first token of a bullet; `gate_rows` joins only indented
continuations; `gate_section` stops at the first following `##`. The tool has no
`located` check at all (cap and named pathologies only). The r67 house shape is
covered (25→0, 26→1 findings), so safety depends on the L1 keeping one physical line
per row.

### M2. The 25-word cap is per quoted run, and `(cont. in row)` is a documented bypass
Prose between spans splits the run, so the cap is evaded by construction: round-66
S795 quotes **28 source words** in two spans (10 + 18) and reports 0 findings; its
registry anchor is 28 words (S797 27, S798 27). The r67 Integration note prescribes the
same split for long anchors, and S813 already uses it (Gate line 23 words, ending
`…beak-like part` + `(cont. in row)`; its fragment anchor is 26–27). Decide whether the cap is
per run (tool, r66 precedent) or per row (prose claim). If per row, r66 has three
over-cap rows and S813’s fragment anchor must be shortened.

### M3. r67 Gate draft: 32/32 lines filled, all bound verbatim (final audit 12:49Z)
`stage/gate-rows.md` carries 32 Gate lines (24 opened + 8 rejects) and all are now
filled (S807/S808/S827/S828 landed at 12:48Z). Re-ran the checker (0 findings, exit 0)
and the fragment binding on the final bytes: **0 issues** — every quoted first span is
byte-verbatim in its fragment anchor cell and ≤25 words (S825 16w, S826 13w, S813 23w
+ `(cont. in row)`). Reject lines S801-S804 carry `REJECTED: …; flip: …` with anchor
quotes verbatim in the r66 row files (re-checked 12:49Z); S829-S832 carry both tokens;
S829/S830/S831 quote wall-page text (`"Just a moment..."`, `"Client Challenge"`,
`"JavaScript is disabled in your browser"`) — the draft now states these are
unreachability evidence, never source anchors; S832 quotes nothing.
Claim C needs all **24** mined rows and the draft now has them; the risk has moved to
the merge: `stage/lesson-draft.md` is still 2/32 filled (only S825/S826) with 30
placeholder rows, and Ca’s `>= 20` Gate leg cannot tell that object from a complete
one (H2). Integration must lift these 32 lines, one physical line per row.
Fragment drift: the scribe reports fragment bytes still moving (S805 teaches changed
during the pass). I re-bound the Gate lines against the live fragments after that
report (12:51Z) — still 0 mismatches over 28 fragment files, rows-tree anchor digest
`570ce9aced…`. Re-run the binding script at merge time and diff; a Gate quote that
lags its fragment is the one silent staleness class this lane has no leg for.

### M4. Pre-integration fragment checker is hard-bound to round 66's entry
`tools/check-row-fragments.py:40` `ENTRY = "corpus/knowledge/culture-material/games-play-sport-contests.md"`,
no `--entry`. `--rows .ufo/waves/round-67/rows` → **44 findings in 26 files** (12:52Z
snapshot), of which **24 are `used-by` false positives** — one for every mined r67
fragment, which names `medicine-healing-codes.md`. Real mined-row items surfaced:
`teaches-length` S814 246, S818 242 (>240) and `quote-words` S813 27 (>25, the F8
anchor); reject-row items (S829 274, S830 311 teaches length; quote-words 3, 3, 2, 0;
`status/tier/no-capture`) are expected for rejects. As shipped, the tool cannot gate
r67 fragments.

### M5. Only 9 of 22 `rejected` registry rows carry `REJECTED:` + `flip:`
Base scan of `corpus/SOURCES.md`: 22 rows with `status=rejected`; 13 lack both tokens
in the teaches cell — S047, S094, S135, S141, S145, S147, S151, S159, S233, S602,
S616, S623, S643 (each has rejection prose instead; none a `flip:`). `accept-ca.py`
D4 (`:207-238`) enforces the tokens only for S801-S804, so Ca passes while the general
property is false for 59% of rejected rows. Do not state the convention universally
in round-67.md; qualify it to rows opened from r65 on, or repair those cells.

### M6. L1’s C-APPEND/Ca-D4 sequencing: counters agree, the lands arrays do not
The L1’s resolution (C lands at A_c with only S805-S828 appended; Ca lands later at
A_ca with S829+ rejects) is implementable for the counters I checked: `accept-c.py`
APPEND reads the registry only, and Ca’s D4/QUOTES at A_ca see the later rows and the
lesson. Tension to record, not a leg failure: claim C’s `lands` array in
`reports/round-67/claims.json` includes `corpus/lessons/round-67.md`, but the L1’s
message says A_ca carries “the S829+ reject rows (plus the round-67 lesson)”. Either
the lesson lands at A_c (where its Gate names S829-S832 rows that do not yet exist in
the registry) or C’s lands array is inaccurate. No counter leg reads that array, so
this is a records statement for the L1 to make consistent in the lesson’s own
integration note.

## LOW

### L1. round-66.md Gate provenance overclaim (pattern the r67 lesson copies)
The header says each quote is "the anchor quote of that row's own final `row-*.txt`
artifact, verbatim". Audit of all 23 rows: quoted runs ≤25 words (max 25, S779/S796);
**20/23** verbatim in their `row-*.txt`; S776 has no `row-*.txt` (its artifact is
`stage/s776-gate.md`, copied from round-65’s S753 line); S783 and S795 are absent from
their fragments because R66-M1/M2 replaced those anchors in the registry only — the
untracked r66 fragments still hold the superseded anchors. All 23 quotes **do** bind
verbatim (Unicode-normalized) to their registry anchor cells (0 mismatches), so the
substantive located property holds and only the provenance wording does not. Reword to
"the row's registry anchor cell" or refresh S783/S795 fragments before the D1 manifest
commits them as durable evidence.

### L2. Fill recipe now agrees with the landed lines (was uncapped at first review)
The earlier draft’s recipe printed `cells[6]` uncapped (S813’s 26–27-word anchor would
have been pasted over-cap). The current recipe caps mined anchors at 25 words, drops
trailing function words, then appends `(cont. in row)`. I simulated it mechanically
against `row-S813.txt` and the output is **identical** to the landed draft line
(23 words, ending `…role of the beak-like part` + `(cont. in row)`). Resolved; the
remaining item is the fragment itself (S813 anchor 26–27 words, F8), not the recipe.

### L3. `truncated-grounds` is dead while drafting
`registry_teaches` resolves `<lesson dir>/../SOURCES.md`; for
`.ufo/waves/round-67/stage/*` that path does not exist (empty map), so the check only
goes live at `corpus/lessons/`. A clean stage run is weaker than a clean integration
run; noted so it is not read as more.

## Named attacks
Detector shortcut classes (table/bold/col-0 wrap/second `##` section → M1); stale
receipt (the QUOTES leg’s own construction → H1, plus the post-fix stale base receipt
→ H1); false stamps (no perfect-lesson control → H1/H2); moved-worktree claims (not
this axis; the QUOTES leg reads `root` bytes only); fabricated anchors (bound 20 r67
+ 23 r66 Gate quotes to fragments/registry anchors → L1); duplicate/tier inflation
(out of scope); cap evasion by multi-span split (M2).

## Residual risk and verification gaps
- The original H1 defect is proven by executing the leg’s own expression, not by a
  counter run: I am barred from writes outside `.ufo/waves/round-67/` and
  `accept-ca.py` needs `--root` + `--lands` in a materialized clone. The post-fix
  claim (24/24 passes) was proven the same way against the current bytes; an
  end-to-end run at base is still owed as the re-stamped control.
- "Located" was verified against fragment anchor cells and registry anchor cells, not
  live pages (no re-open in this box); live location is claim C’s / the re-open seats’
  leg.
- The r67 rows tree moved during the audit; the 8-MISSING list and
  check-row-fragments counts are snapshots — re-run at integration.
- No `lsp` device available to this seat; semantic claims rest on the lane’s checkers,
  the quoted commands and their outputs.

## Report

`.ufo/waves/round-67/w1/RevGateQuotes.md`
