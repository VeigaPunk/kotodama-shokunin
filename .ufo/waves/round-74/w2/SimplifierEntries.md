# SimplifierEntries — round 74 wave 2 (falsify), hyaku run 7

**Attack (by cutting):** the two landed entries
`corpus/knowledge/culture-material/worldbuilding-setting-practice.md` (base, 4317 words, body 3694)
and `…worldbuilding-setting-practice.amend-2026-10-23.md` (amend, 2219 words, body 1494).
Question asked: which sections/sentences can go without losing a claim a row, Gate record or leg needs,
and without dropping below the 478-word floor or losing a located quote. Every cut below was applied
**for real** in a scratch clone and scored with the frozen counters.

**Revisions.** base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; operative freeze F3
`00c408a0af2fa5ddf65af2224152ce258b26d896`; claim C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`;
claim Ca lands `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`; lane main at dispatch `1d7add3`.

**Fetch record (QUALITY 21/22/24).** This seat made **no network fetch**: every measurement is on committed
bytes, so no User-Agent and no CDX ruling is owed. `check-cited-lines.py`, `accept-c.py`, `accept-ca.py`
were run from the tree; no tool was installed or upgraded (tooling record at the end).

**Method.** `D=$(mktemp -d); git -C "$D" init -q; git clone -q <lane> "$D/lane"`; every branch/checkout/commit
happened inside `$D/lane` only. The lane tree at `/home/vgpnk/Projects/shokunin/kotodama-shokunin` was never
written by this seat — the only file written there is this report. Counter invocations are exactly

```
python3 -B reports/round-74/accept-c.py  --root . --lands <lands> --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
python3 -B reports/round-74/accept-ca.py --root . --lands <lands> --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
```

with the clone's local `main` forced to `<lands>` (`git branch -f main <lands>`), which every run reports back
as `# measured revision (lane main): <lands>`.

**Baseline, unmodified bytes.**

```
# claim C at its own lands
ACCEPT-C-74: PASS legs=13/13                                            (exit 0)

# claim Ca at its own lands
ACCEPT-CA-74: PASS legs=11/11                                           (exit 0)

$ python3 -B tools/check-cited-lines.py <both entries>
CITED-LINES: 0 finding(s) in 2 file(s)                                  (exit 0)
```

**Verdict.** The falsification target **FAILED**: no content-preserving cut breaks a leg. 19 scored states
(13 single cuts, 2 cumulative cuts, 3 floor probes, 1 floor-exact state) all returned the expected verdict, and
every deletion left `ENTRIES`, `ROWS`, `REPOINTED`, `INDEX`, `CITEDLINES` green. What the attack did find is
**bloat** (F1/F2: 361 words of restatement, deletable at zero cost) and **two defects in the legs**, one about
how little `ENTRIES` certifies (F3) and two about the counters' composability and environment sensitivity
(F5/F6). F4 records the cuts I hold back and why.

---

## F1 — MEDIUM — the base entry restates itself in 7 places; 214 words are deletable with all 13 legs green

Each line below restates a claim that is retained, verbatim or in table form, a few lines away. Each was
deleted **alone** in a fresh clone at `c4bf61a` and scored; each kept `ACCEPT-C-74: PASS legs=13/13`.

| cut | line | verbatim opening (≤25 tokens) | restated by | words | state sha | verdict |
|---|---|---|---|---|---|---|
| B1 | 30 | "The LitMemo advice is also inseparable from the settings document its own product sells (S881)." | §1 table row 1 col 3: "the page's own product calls to action sit beside the advice" | 15 | `a376f7b7c5ad…` | PASS 13/13 |
| B2 | 32 | "The method rules below are reports of what these two pages prescribe" … | `- sources:` ("never as the sole support of a claim about the world") + line 28 + §2, which quotes all three monograph claims | 66 | `b9071cf2f3a2…` | PASS 13/13 |
| B3 | 80 | "Set beside each other, the two orders agree on the premise, the near field, the depth rule and the recording rule" | the §4 Move table (lines 84–88), whose rows 3 and 5 state the same two differences | 43 | `d110f48aad19…` | PASS 13/13 |
| B4 | 176 | "The page explains why the last field is worth its row: it produces the generational value gap" | §7 country-sheet row 174 col 3: "it splits the generations' values" | 29 | `32e088c4c74e…` | PASS 13/13 |
| B5 | 239 | "Its multi-author rule continues: whoever changes a setting writes the change back into that copy" | §9 table rows 248–249 ("write the change back the same day"; "no setting facts in private notes") | 29 | `0e8b253d7362…` | PASS 13/13 |
| B6 | 241 | "For tabletop play it splits the document into a player-visible layer and a game-master-only layer" | §9 table row 250 ("split public and hidden layers") | 26 | `32900f0d6538…` | PASS 13/13 |
| B7 | 267 | "Nothing here rules on any world." | `- scope:` ("it decides no world's canon") and the rest of the same line | 6 | `90463b010824…` | PASS 13/13 |

Cumulative state (all seven applied, one commit `25abc126062c715829019bd658a9a736c0cd09b1`) — raw receipt:

```
$ git -C "$D/lane" diff --stat c4bf61a8d722 25abc126062c
 .../knowledge/culture-material/worldbuilding-setting-practice.md  | 8 +-------
 1 file changed, 1 insertion(+), 7 deletions(-)
$ wc -w corpus/knowledge/culture-material/worldbuilding-setting-practice.md
4103 corpus/knowledge/culture-material/worldbuilding-setting-practice.md
$ python3 -B reports/round-74/accept-c.py --root . --lands 25abc126062c… --freeze 00c408a0af2f… --fleet-root …
…
LEG PASS ENTRIES
LEG PASS ROWS
LEG PASS REPOINTED
LEG PASS GATE
LEG PASS EVIDENCE
LEG PASS REJECTS
LEG PASS GROUND
LEG PASS CITEDLINES
LEG PASS CENSUS
     exit=0 last-line=kotodama	ok	/tmp/r74-fleet-…/kotodama-shokunin/corpus/SOURCES.md
LEG PASS SCRATCHMIRROR
LEG PASS COLLCHECK
LEG PASS FROZENCFG
     constants from git show 00c408a0af2f:reports/round-74/claims.json (sha256 270e31790e29…
LEG PASS INDEX
ACCEPT-C-74: PASS legs=13/13                                            (exit 0)
base 4317 → 4103 words, body 3694 → 3480 (floor 478)
```

(detail lines elided where marked with `…`; the thirteen `LEG` lines and the verdict are verbatim)

**Proposed fix.** Delete lines 30, 32, 80, 176, 239, 241 and the first sentence of 267 in one commit. Nothing
else changes: no heading, no header field, no table row, no `source:` line.

**Conflict with a sibling finding.** `RevEntryBaseFinal.md:199` (F9) reaches line 32 from the other side and
proposes **C9** (`append (S877)`). C9 repairs the line's missing clause scope; B2 removes the line, which is a
digest of §2 and therefore carries no claim §2 does not carry with its quotes. **Apply one, not both** — B2
measured green alone and leaves no id-less three-claim line to repair.

## F2 — MEDIUM — the amendment restates its own header in 4 bullets; 147 words are deletable with all 13 legs green

| cut | line | verbatim opening (≤25 tokens) | restated by | words | state sha | verdict |
|---|---|---|---|---|---|---|
| A4 | 89 | "The twenty-chapter figure is his 大概, in a sentence he closes with 「我觉得是问题不大的。」" | line 58 quotes the **same sentence with the same locator**; `- scope:` refuses a "boundary, a threshold or a measured optimum" | 33 | `e4e9a3b54a48…` | PASS 13/13 |
| A2 | 88 | "The disclosure material rests on one tier-C row and is a lead — useful for designing a disclosure plan" | `- sources:` ("§4 rests on that tier-C row alone … a lead; it is never the entry's rule") + `- recheck:` | 42 | `5a51b3830922…` | PASS 13/13 |
| A3 | 90 | "No second author's build order is compared here, so the order is not shown to be typical" | `- scope:` refuses "any claim that this order is the order other authors use" | 34 | `2a2e3d109c05…` | PASS 13/13 |
| A1 | 22 | "The 编者按 states the series' frame — 北京大学网络文学研究团队, twelve writers, a volume forthcoming" | the S883 `source:` line already records 编者按 at P2, the series host, the forthcoming volume and the P3–P6 credit roles | 38 | `1bd0a92fe476…` | PASS 13/13 |

Cumulative (A1+A2+A3+A4 with B1–B7, one commit `50bfb5c7cc0172c09aab90c1c75efe57606c3472`):

```
$ git -C "$D/lane" diff --stat c4bf61a8d722 50bfb5c7cc01
 .../worldbuilding-setting-practice.amend-2026-10-23.md | 4 ----
 .../knowledge/culture-material/worldbuilding-setting-practice.md | 8 +-------
 2 files changed, 1 insertion(+), 11 deletions(-)
ACCEPT-C-74: PASS legs=13/13                                            (exit 0)
base 4103 words / body 3480 ; amend 2072 words / body 1347 (floor 478 each)
$ python3 -B tools/check-cited-lines.py <both entries>   (at the cumulative state)
CITED-LINES: 0 finding(s) in 2 file(s)                                  (exit 0)
```

**Cost of A1, stated:** `twelve writers` (十二位作家) is a page fact that exists **only** in this bullet; the
S883 `source:` line records the host, the volume and the credit roles but not the count. If that fact is worth
a row, add "twelve writers" to the S883 `source:` line in the same commit; otherwise the cut is free.

**Synergy with two sibling findings — these cuts retire their objects.** `RevEntryAmendFinal.md:98` (F2) shows
`编者按` never occurs on the page, so A1 removes one of the two mislabels the reviewer found (line 3 still needs
the reviewer's "editorial intro" fix). `RevEntryAmendFinal.md:121` (F4) shows `about different books` is
unsupported; A3 deletes the sentence rather than rewriting it, which is the cleaner repair of the same defect.

## F3 — HIGH (finding about the legs, not about bloat) — `ENTRIES` certifies 478 words of *shape*, and the two entries were landed at 3694/1494 body words: 87% and 68% of the body can be deleted mid-section with `PASS legs=13/13`

The leg's own docstring is honest ("body at least the base tree's smallest entry in words … a length-and-shape
gate only"), but the frozen `after` sentence reports `PASS legs=13/13` as the claim's observable, and no reader
of that line can tell a 3694-word entry from a 485-word stub. Measured bracket:

```
# below the floor — base entry truncated to §1 (393 body words)
LEG FAIL ENTRIES
     corpus/knowledge/culture-material/worldbuilding-setting-practice.md body has 393 words (floor 478 = the smallest knowledge entry at base)
ACCEPT-C-74: FAIL legs=12/13                                            (state c331789650a8…)

# below the floor — amendment truncated to §1 (285 body words)
LEG FAIL ENTRIES
     corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md body has 285 words (floor 478 = the smallest knowledge entry at base)
ACCEPT-C-74: FAIL legs=12/13                                            (state 3462a935992c…)

# just above the floor — base §1+§2 (764), amendment §1–§3 (682)
ACCEPT-C-74: PASS legs=13/13                                            (state a2154e1f704b…)

# at the floor, truncated MID-SENTENCE — base body 485, amendment body 485
ACCEPT-C-74: PASS legs=13/13                                            (state 1afe1ab2d38cbd40d68981dfd9df713571f0593a, exit 0)
base entry now 1108 words total, last bytes: '…not a means of communication but its subject and topic (S877).\n'
amend entry now 1210 words total, last bytes: '…laws, mechanics\n\n- The premise is the world's origin: 「万事万物都从最初造物主而来」 (loc: P68) (S883).\n'
```

The floor is **one global constant** — the smallest entry in `corpus/knowledge` at base — applied to every
entry of every claim. It therefore measures the corpus's weakest pre-existing file, not this claim's content.
The truncation test also shows the leg accepts an entry whose last table or list is cut mid-section: no leg
counts headings, tables, quotes or sections beyond "at least one `## `".

**Proposed fix (frozen, objective, no re-review).** Add `entries_min_words` to `claims.json` per entry, set to
the non-author-reviewed body length (e.g. 3400 and 1300), and have `leg_entries` read it from `<freeze>`; keep
the 478 floor as a second, corpus-level check. Two lines of counter code, and `PASS` then means what a reader
of the claim will assume it means. Alternative if the claim must stay untouched: the `after` sentence should
print the measured body words rather than the leg count alone, so an 87% truncation is visible in the receipt.

## F4 — LOW — cuts I measured but hold back, with their exact cost

Each passes 13/13 alone, so each is a *legitimate* deletion by the counters' standards; each loses something a
human reader would miss. Listed so nobody applies them silently.

| candidate | line | words | state sha | what it costs |
|---|---|---|---|---|
| B8 | base 220 | 41 | `eb287ee7c4ab…` | removes the only prose that attributes the four failure rows to tuduku; the §8 table cannot carry the id (`TABLE-ID` is a `check-cited-lines` finding), so the merged row set loses its source binding |
| A6 | amend 83 | 89 | `61d29c4cea44…` | the amendment's only worked application ("Worked example, hypothetical and canon-free: take a premise \"the dead answer, at a price paid in memory\"."). Not a source claim; it is the entry's own application of §2–§4 |
| A7 | amend 87 (first two sentences) | ~25 (not run) | not run | needs an antecedent rewrite ("a different audience is neither evidence against it…") or the last clause dangles; the saving does not justify the edit |
| A5 | amend 23 | ~40 (not run) | not run | holds a located quote (`您最擅长构建缜密恢宏的世界观`, loc P8) that appears nowhere else in the entry, i.e. the only located evidence for the frame-separation claim |

## F5 — MEDIUM (finding about the legs) — `accept-ca.py` is not green at claim C's lands: `APPENDONLY` red on the S877 row that claim C edits in place. The two claims are order-dependent, and the shipped tree cannot be re-verified by Ca's counter

Observed while establishing the baseline; not caused by any cut (the same verdict appears at unmodified
`c4bf61a` and at the cumulative-cut commit).

```
$ python3 -B reports/round-74/accept-ca.py --root . --lands c4bf61a8d722f9168ce0fd8021a6261c000610c5 --freeze 00c408a0af2f… --fleet-root /home/vgpnk/Projects/shokunin
LEG FAIL APPENDONLY
     … problems=['corpus/SOURCES.md: changed lines outside REPAIR stated_at lines [832]']
ACCEPT-CA-74: FAIL legs=10/11                                           (exit 1)

$ … --lands 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3      # Ca's own lands
ACCEPT-CA-74: PASS legs=11/11                                           (exit 0)

$ sed -n '832p' corpus/SOURCES.md        # at C's lands
| S877 | М.Ю. Сидорова, О.Н. Шувалова, «Интернет-лингвистика: вымышленные языки», М.: «1989.ру», 2006, 184 с., …
$ git diff --stat f7104cbce186 c4bf61a8d722 -- corpus/SOURCES.md
 corpus/SOURCES.md | 6 +++++-
 1 file changed, 5 insertions(+), 1 deletion(-)
```

Line 832 is **S877's row**, whose used-by cell claim C changes in place — lawful under C's ROWS leg ("changed
lines elsewhere are a subset of the REPAIR stated_at lines plus appended lines" … "except the six must_track
paths" does not cover a modified registry row), and fatal under Ca's APPENDONLY leg, which classifies any
changed non-append line as a red. So the two frozen claims are jointly satisfiable **only in the order
Ca → C**, and `PASS legs=11/11` is a property of `5e4796c`, never of the tree that ships. Both claims survive
as written (each is measured at its own `<lands>`), so this is a leg-composition defect, not a false claim.

**Proposed fix.** Either (a) Ca's `after` names its lands ("prints PASS legs=11/11 **at 5e4796c**"), or
(b) `APPENDONLY` exempts a changed line that a sibling claim's frozen ROWS leg declares as an in-place edit
(S877 at `claims.json` C.`reused_rows`), so a re-run at the tip is green. (a) is one sentence and needs no
counter change; (b) is a genuine fix but couples the two counters.

## F6 — LOW (finding about the legs, robustness) — `RECEIPTS` is sensitive to `$TMPDIR`; a re-run on any host whose temp root is not `/tmp` is a false red

A/B on the **same** lands revision (`50bfb5c7cc01…`), same bytes, only the environment differs:

```
$ TMPDIR=/tmp python3 -B reports/round-74/accept-ca.py … 
LEG PASS RECEIPTS
ACCEPT-CA-74: FAIL legs=10/11                    # only the F5 APPENDONLY red

$ TMPDIR=<lane>/.ufo/waves/round-74/w2/tmp-simplifier python3 -B reports/round-74/accept-ca.py …
LEG FAIL RECEIPTS
     … problems=['reports/round-74/telemetry/accept-c-73-at-lands.txt: committed stdout differs from the re-run (bda16ca6deec vs 75e822b3c1b9)', "…accept-ca-73-at-lands.txt: … (55544779204d vs 2c044ed7d25a)"]
ACCEPT-CA-74: FAIL legs=9/11
```

Cause, read off the counter: `normalize_receipt()` (`reports/round-74/accept-ca.py:1721-1723`) masks only
`/(?:var/)?tmp/[^\s:,"']+` (`:183`), while the re-run is executed with the caller's `TMPDIR` (`:1730`). Any
temp root outside `/tmp` (a CI runner, a scratch disk, a seat following the round's own "scratch under your
own directory" rule) leaks into the compared stdout and reds a byte-identical receipt. The failure is **closed**
(a red, never a false PASS), so no claim is falsely certified.

**Proposed fix.** Normalize the `TMPDIR` actually in force as well (`RECEIPT_TMP_RE` union
`re.escape(os.environ.get("TMPDIR") or "/tmp")`), or pin `TMPDIR=/tmp` in the re-run environment at `:1730`.

## F7 — LOW (environment) — one non-reproducible base-materialization failure under `/tmp` pressure; the counter fails closed, so this must not be scored as a claim defect

```
ERROR: materialize f7104cbce186 failed (git rc=0, tar rc=2):
ACCEPT-C-74: (no verdict line, exit 2)
```

The identical command re-run seconds later on the same bytes printed `ACCEPT-C-74: PASS legs=13/13` (exit 0),
and every later run at the same revision was green. Host state at the time: `df -h /tmp` →
`128G 128G 183M 100% /tmp`; `du -sh /tmp` could not finish inside 300 s. A second round of runs was therefore
executed with `TMPDIR` on a seat-owned scratch directory (which is what surfaced F6). Recorded so a later seat
does not read one red harness line as a claim failure: the counter's error path prints `ERROR:` and exits 2
without a verdict, i.e. it fails closed.

---

## Preserved contract (what no proposed cut touches)

- **All five `source:` lines** stay byte-identical (S877, S881, S882 in the base entry; S883, S884 in the
  amendment). `ROWS`' used-by cells are derived from exactly these lines — measured green in every state.
- **All nine header fields** on both entries (`source, verified-at, recheck, ground, topic, gap-filled,
  sources, couples, scope`; plus `refuses` in the base entry). The `- topic:` value is the string `INDEX`
  compares to the `corpus/README.md` row, so the topic line is untouchable by this kind of cut — verified by
  `LEG PASS INDEX` in all 19 states.
- **Every `## §` heading** in both entries: the proposed cuts remove sentences and bullets, never a section, so
  `ENTRIES`' "at least one `## `" and the body-start location are unchanged.
- **Every unique located quote**: the only quote a proposed cut removes is `「我觉得是问题不大的。」` at
  amendment line 89, which is quoted with the same locator at line 58. B8/A5/A6/A7 (the held-back set) are the
  only candidates that would drop a unique quote or a unique attribution.
- **One id per line, no id in a table row**: `check-cited-lines.py` prints
  `CITED-LINES: 0 finding(s) in 2 file(s)` at the cumulative-cut state, and `REPOINTED` stays green because
  every deleted line was an *additional* statement, never the only citation of a row.
- **Registry and index bytes**: untouched (the cuts are confined to the two entry files); `ROWS` and `INDEX`
  green in every state.
- **Provenance of the pre-append mirror**: `.ufo/waves/round-74/assimilation/validate/…` and
  `.ufo/waves/round-74/drafts/…` hold uncut copies of both entries. No leg compares them to the landed bytes
  (`SCRATCHMIRROR` reads the receipt and the commit order only), so a cut does not break the receipt — but a
  cut makes those committed copies a snapshot rather than a copy. That is the tradeoff of applying F1/F2 and
  the reason the receipt is a pre-append artifact.

## Tradeoff summary

- F1+F2 (−361 words, 11 whole statements) improves the maintainability axis at zero cost to any leg and no loss
  of a claim: every deleted statement is a second copy of a claim retained in a table row, a header field, or a
  sentence a few lines away. It also removes one id-less three-claim line (F1/B2) and two of the amendment's
  defective labels (F2/A1, A3) that siblings found from the fidelity side.
- F3 is not a cut I recommend applying; it is the boundary of what `PASS legs=13/13` means. Applying it would
  harm the fidelity axis (it deletes sourced content), which is where this seat stops.
- The next deletion past F1/F2 cannot be justified without a reader: B8/A6/A5/A7 each remove comprehension or
  attribution, which is the axis this seat must not damage.

## Reproduction (the scratch clone was deleted after the run)

Every cut is a **whole-line deletion** in exactly one file, so reproduction is exact:

```
D=$(mktemp -d) && git -C "$D" init -q && git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"
cd "$D/lane" && git checkout -q --detach c4bf61a8d722f9168ce0fd8021a6261c000610c5
git branch -f main c4bf61a8d722f9168ce0fd8021a6261c000610c5
# base entry: delete lines 30, 32, 80, 176, 239, 241 (descending) and replace the 6-token opening of old line 267
#   "Nothing here rules on any world. No layer assignment" -> "No layer assignment"
# amendment: delete lines 22, 88, 89, 90 (descending)
git commit -qam "cumulative redundancy cut" && git branch -f main HEAD
python3 -B reports/round-74/accept-c.py --root . --lands "$(git rev-parse HEAD)" \
  --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin   # PASS legs=13/13
```

Line numbers are the **lands** numbers (`c4bf61a`); deleting descending keeps them valid.

## Tooling record

No tool installed or upgraded. Used as found: `git`, `python3`, `coreutils`, the repo's own
`reports/round-74/accept-c.py`, `reports/round-74/accept-ca.py`, `tools/check-cited-lines.py`.
`pacman` never invoked (host-wide pause). Host note for other seats: `/tmp` was at 100% (183 MB free) during
this seat's runs; a `TMPDIR` on your own scratch avoids both the space and the F6 false red.
