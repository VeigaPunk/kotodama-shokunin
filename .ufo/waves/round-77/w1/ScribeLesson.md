# ScribeLesson — round 77 (hyaku run 10), wave 1 — report

Seat `ScribeLesson` (role: scribe; **leaf**: no delegation, no background jobs, no `task` spawns). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `211f9526800906e0c585d878d265c37e5e090c15`, measured 2026-10-27. I wrote the round-lesson draft and this report; the stage directory holds five receipts. I did **not** edit `CLAIMS-DRAFT.md`, any filed lesson, `reports/round-76/**`, `reports/round-77/**`, `LOG.md`, `SCORECARD.md`, `SKILL.md`, `SHONEN.md`, `corpus/**`, the shokuknow tree, or any git/jj state.

**The claims moved under this seat.** I read `CLAIMS-DRAFT.md` at 22:22, 22:33 and 22:49; the draft is written against the 22:49 bytes (`sha256 ac5aead40d337f903057a36313162ebac2ee539aa1a673310c6116fd01784883`, 8592 bytes; the 22:33 bytes were `ed249cdf…392fa8b`, 8456 bytes). The earlier revisions are unrecoverable (untracked file, overwritten), so the delta in this report is my own reading, not a byte diff. The 22:49 revision adopts this seat's D2 correction verbatim in substance (p. 114 / PDF p. 4, the 17-word attribution-bearing quote, "reported from the cited 2008 work").

## 1. Products

| path (relative to the lane) | state |
|---|---|
| `.ufo/waves/round-77/w1/drafts/corpus/lessons/round-77.md` | draft; 98 lines / 32156 bytes (`wc -l -c` → `98 32156`); sections `## Gate` (admit table, route records, refused/held table, triage, non-author spot-check), `## Mistakes` (16 rows), `## Corrections`, `## Census`, `## Sources & frontier`, `## Routed to the L1`; 10 `L1-FILL` cells — `grep -c "L1-FILL"` → 10 |
| `.ufo/waves/round-77/w1/stage/ScribeLesson/receipt-01-base-counts.txt` | base counts, command + output |
| `.ufo/waves/round-77/w1/stage/ScribeLesson/receipt-02-census.txt` | census validate/census, exit and rows |
| `.ufo/waves/round-77/w1/stage/ScribeLesson/receipt-03-staged-census.txt` | staged-set census + per-file path-present sweep |
| `.ufo/waves/round-77/w1/stage/ScribeLesson/receipt-04-l76-19.txt` | L76-19 `stated_text` re-derivation |
| `.ufo/waves/round-77/w1/stage/ScribeLesson/receipt-05-probes.txt` | network probes, each UA bound to its response; D2 page sweep and byte-identity |

The draft remains a **skeleton**: S897's quote and locator are `L1-FILL` (ScoutDocS897's capture), the committed evidence windows and digests are `L1-FILL`, the lands revisions and counter output are `L1-FILL`, and the non-author spot-check is `L1-FILL`. No quote, digest, revision or counter result is invented.

## 2. Checks run (command → raw result)

**G1 — base counts.** 820 — `git -C … show 211f952…:corpus/SOURCES.md | grep -cE '^\| S[0-9]+ \|'`; 253 — `git -C … ls-tree -r --name-only 211f952… -- corpus/knowledge | grep -c '\.md$'`; 32 — the same over `-- corpus/knowledge/linguistics`.

**G2 — census.** `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit `0`; `sources-census.sh census … kotodama` → exit `0`, `kotodama rows 820`, `tier.A 493`, `tier.B 311`, `tier.C 16`, `status.mined 725`, `status.queued 58`, `status.rejected 37`.

**G3 — staged set** (read-only shokuknow tree). 40 — `find . -name '*.md' | wc -l`; 11 — `ls naming-systems.amend-*.md | wc -l`; 10 path-present at base / 30 absent — per-file `git -C <lane> cat-file -e 211f952…:<rel>` sweep (list in receipt 03); so 1 adopted, 29 non-adopted absent = 1 refused + 9 held + 19 out-of-theme.

**G4 — L76-19 re-derived.** `git -C … show 211f952…:corpus/lessons/round-75.md | sed -n '48p' | grep -cF "S892's window (\`chars=4097 before=284\`)"` → `0`; the line's own text is `(\`chars=4097 before=284\`) both start at the document head …`; a Python substring test on the exact ledger `stated_text` prints `stated_text in line48: False`. The "window" in the ledger's phrase belongs to the S888 clause on the previous line.

**G5 — routes, per UA.** D1 live plain UA → `403 text/html 162`; browser UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36` → `200 text/html 143252`, title `單名與雙名` ×3, sha256-16 `f14f7a5c03cb187f`; D1 capture `20240111092427id_` → `200 text/html 143457`, title ×3, sha256-16 `68c6ed377334199f`.

**G6 — D2 identity and the claims' quote.** live PDF `200 application/pdf 417093`; capture `20251231111748id_` `200 … 546440`; capture `20260901045105id_` `200 … 417093`; `cmp -s` live vs 2026-09-01 capture → silent, one `sha256sum` line `5d1bfa5a5f01bee68e090155ed683d848e6f75dbc456b8b631be81c1fa8d29bc` for both. `pdfinfo` → `Pages: 13`. PDF p.4 head → `114   Irena Kałużyńska`. Page-by-page sweep for the claims' phrase → `p4: 1`, every other page `0`. p.4 context: §3 heading, then "There are many terms denoting various species of plants and trees in China." and "According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees (general terms, species or the parts of flowers or trees) among the names of women figuring in the research material of the work…".

**G7 — claims' ground sweep.** `git -C … grep -l -E 'lishisuo\.cssn\.cn|onomastica\.ijppan' 211f952… -- corpus/knowledge` → no output, exit `1`.

**G8 — lane-row absence.** `git -C … show 211f952…:corpus/SOURCES.md | grep -cE '^\| S903 \|'` → `0`; max ids `S894 S895 S896`.

**G9 — README surface.** `grep -n "Total knowledge entries" corpus/README.md` → `755, 798, 819, 830, 834` (243/247/249/252/253); `## linguistics/ (32)` at `:344`; `:824` says the round-28 sweep still parses the first footer.

**G10 — peer-pointer sample re-checked** (`ScribeMistakes` rows, since I merged them). Verified: `measures-c-final-c28ea.txt:12` (frozen legs, INDEX twice), `:25-26` and `controls-c.txt:30-31` (`registry line added outside the frozen row_set`), `:38-39`/`controls-c.txt:48-49` (S938→S895 `showGb`), `controls-c.txt:57` (expected exit=1), `measures-ca.txt:4` (L76-13 allowlist + L76-19), `:7-8` (ANNOTATE/NOSTUB), `:10` (R1EXEMPT receipts absent), `:13` (COMBINED line 410), `controls-ca.txt:40/54/58/67`, `selftest-ca.txt:44-45` (`170/170`), `accept-c.py:6381-6397` (`LEGS` with INDEX twice), ledger sha `d609c8b0…` identical at `b4965d5c`/`df0f0309`/`a43ed807`, fleet `1cd8e33c` numstat `1 1` on the r76 report, `corpus/QUALITY.md` 29 criteria / 0 "lane report" / 0 `^30.`, prompt `:86` vs `:345-348` and route map `:151-155`, validator `SWARM_ROLES` (10 roles, no planner) and `unknown_role` at `:989` (peer said 988). **One peer pointer failed as cited:** `controls-ca.txt:56` is `LEG PASS RECEIPTS`, not a RECEIPTS failure; the correct red is the F0 control `.ufo/waves/round-76/w1/stage/L1/freeze-ca-control-ledger-redbefore.txt:56-57` (`LEG FAIL RECEIPTS`, `receipts=[]`, missing `accept-ca-75-at-lands.txt`) — see F11.

**Not run (reported as unrun).** `reports/round-77/accept-c.py`, `accept-ca.py`, `claims.json` do not exist at draft time (`ls reports/round-77` → `telemetry`); every r77 leg is unrun, and the non-author spot-check has no reviewer.

## 3. Claims revisions, 22:22 → 22:33 → 22:49

What moved (my reading of the three revisions):

1. **D1 route** — 22:22: "live: HTTP 403 wall both UAs at L1 probe". 22:33: "Live plain UA HTTP 403 / 162-byte WAF page; browser-shaped UA HTTP 200 / 143252-byte article. Do not claim both UAs were blocked." My probes (G5) agree with the new text, and the live browser-UA copy is now named the located source.
2. **S933 ground** — 22:22 refused `…10-24.md` partly because the live CN page no longer carries the text; 22:33 says "S933 archived rather than live, so route alone is not a refusal" and refuses on S936 (bibliography bridge) plus the misdescribed S934.
3. **S934** — 22:33 names the finding: "the captured PDF is Kałużyńska, not the staged Słon Poland title" (confirmed by G6/capture `20251231111748id_`).
4. **Triage scope** — 22:22 named four staged naming entries; 22:33 dispositions all eleven (1 adopted, 1 refused, 9 held).
5. **Adoption mode** — 22:33 adds "Rewrite, do not copy … remove legacy staged `source:` IDs S886/S888/S889/S890/S891/S896". No check reads the landed entry's cited ids, so this is an instruction, not a control (F5).
6. **Leg lists** — the 22:22 claim C list contained the literal token `LEDGELIST?`; the 22:33 list is the 13-name lineage set with `SCRATCHMIRROR` and "exactly one INDEX", and Ca names its 12-leg set. The token that seat `ScribeMistakes` flagged as a freeze stopper is therefore **gone from the current bytes**; their row needs that qualifier.

7. **D2 locator and quote form** — 22:49 adopts p. 114 / PDF p. 4 and the 17-word form "According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees", and adds the right characterization ("reported from the cited 2008 work, not a universal or exhaustive taxonomy"). Closed in the claim text.

Still open in the 22:49 bytes: the entry-rewrite control (F3), the README footer authority (F4). The D2 item becomes a landing requirement: the committed `S898.txt` window must reach PDF p. 4 or EVIDENCE is red.

## 4. Findings

**F1 — D2's only located quote was misplaced and cut before its attribution (high; closed by the 22:49 claims revision).** The 22:33 text said "§3 ¶1, journal p.115 / PDF p.5 … 'there were altogether 88 terms …' (10 words)"; the 22:49 text says p. 114 / PDF p. 4, second sentence, and quotes the 17-word form with its attribution, so the defect is fixed pre-freeze — the measurement below is why. Measured (G6): the phrase occurs once in the 13-page PDF, on journal p. 114 / PDF p. 4; the sentence begins "According to Kałużyńska (2008, pp. 223, 232), …", so the fragment as quoted claims a finding the paper attributes to her earlier work. A p. 5 evidence window cannot contain the quote, so EVIDENCE would go red if it is graded on the claims' locator. The same locator was independently re-derived by seat `ScribeMistakes` (`.ufo/waves/round-77/w1/stage/ScribeMistakes/d2-locator-sweep.txt`: `pdf_page=4 hits=1`, printed labels p4=114 / p5=115).

**F2 — a staged row's document cell contradicts the capture it carries (high; refusal already right).** `SOURCES.append.md` S934 describes Słon, *Onomastica* 68; its capture `20251231111748id_/…/574/763/` is Kałużyńska, *Onomastica* LXIX 2025 (G6). The 22:33 claims now say this; the row's own ordering (document cell first, capture second) is what let the misdescription pass in the staging tree.

**F3 — the entry rewrite has no control (high; open).** The staged entry cites `source: S903` (no lane row — G8) and six ids that are other documents in-lane. The 22:33 instruction says to rewrite; ROWS/COLLCHECK grade `row_set` only, so nothing reads the landed entry's citations.

**F4 — "the README index row + footer" is under-specified (medium; open).** Five totals at base, six after landing; `:824` records that the round-28 sweep parses the first; `## linguistics/ (32)` becomes stale at 33. The frozen INDEX leg must name the graded footer block and the heading's status.

**F5 — the 22:22 scope gap is closed, not a live defect (informational).** Four vs eleven staged files: the 22:33 text dispositions all eleven. Recorded so no later reader grades the 22:22 text as the claim.

**F6 — the 22:22 route sentence was contradicted by a filed probe and is now corrected (informational).** Same event as F5: the claim moved, not the probe. The lesson row (R77-M15) keeps the class: one status may not stand for two request shapes.

**F7 — L76-19 class reproducible (informational, supports the LEDGER guard).** G4.

**F8 — base numbers hold (informational).** 820/A493/B311/C16/mined725/queued58/rejected37 exit 0; 253 files; 32 linguistics; ground sweep empty; `253→254` and `820→822` consistent.

**F9 — D2's captures are not interchangeable (informational).** `20251231111748id_` is 546440 bytes, `20260901045105id_` is 417093 and byte-identical to the live PDF (G6). Only the latter supports "byte-identical"; the former is the S934 capture and a different encoding.

**F10 — the claims' "820 rows" start line matches the receipt (informational).** The 22:33 frontier line names the seven numbers this seat measured; `census-start.txt` itself carries no count line, so the claims rest on the re-derivation (receipt 02), not on the receipt file alone.

**F11 — one `ScribeMistakes` pointer was wrong as cited (medium; corrected, and the limb restored).** Their R77-M7 cited `controls-ca.txt:56` for a RECEIPTS failure; that line is `LEG PASS RECEIPTS`. The same class is genuinely red one revision earlier: `freeze-ca-control-ledger-redbefore.txt:56-57` prints `LEG FAIL RECEIPTS` with `receipts=[]` and `problems=['receipt reports/round-76/telemetry/accept-ca-75-at-lands.txt is not committed at lands']`, and the F0 control's own `# expected:` line (`:67`) lists neither RECEIPTS nor SEPARABLE nor COMBINED — so the leg fired red *and* the expectation omitted it. The merged R77-M7 now carries both limbs (RECEIPTS red at F0, green by F4; R1EXEMPT red at F0 and Ca-lands). The peer applied the same correction.

## 5. Peer merge (`ScribeMistakes`)

Their 12 rows (R77-M1…M12, mined from `corpus/lessons/round-76-verifier-spotcheck.md` §1/§5) are merged as R77-M1…M12; my own four findings are R77-M13…M16. The merged table's last column keeps their distinction: **only R77-M10 and R77-M12 have executed red proofs**; the rest are `owed` with the fixture named, exactly as their caveats require — none is written as demonstrated. Their caveat on the report-rewrite class is adopted: it is a **checklist line, not a QUALITY criterion** (29 criteria at base, none names the lane report, slot 30 is `ScribeQuality30`'s ledger criterion) — verified independently (`grep -c -E '^[0-9]{1,2}\. \*\*'` → `29`; `grep -c -i 'lane report'` → `0`; `grep -c '^30\.'` → `0`). Their `LEDGELIST?` freeze-stopper note is **stale against the 22:33 bytes** and is recorded as closed in §3 item 6. They then sharpened R77-M3; I re-derived its counts before taking them: the F0 control prints `grep -c "^LEG FAIL"` → `8`, `^LEG PASS` → `4`, `ACCEPT-CA-76: FAIL legs=4/12`; the final freeze `7` / `5` / `legs=5/12`; both `# expected:` lines name three expected-red legs and two expected-green, so 5 red legs at F0 (4 at F4) are unlisted and LEDGER — expected green — is red at both. The draft's R77-M3 now carries those numbers.

## 6. Touched surfaces

Writes: five receipts, the draft, this report — all under `.ufo/waves/round-77/w1/`. Reads: lane git (`show`, `ls-tree`, `grep`, `status`, `rev-parse`), the shokuknow tree, `scripts/sources-census.sh`, the fleet prompt and `PROTOCOL`/`QUALITY`/the validator (read-only), the round-76 telemetry receipts, and ordinary HTTP requests. No pacman, no installs (none needed), no fixture git repo, no fleet-root write. Scratch `/fast/scratch/hyaku/kotodama-r77/ScribeLesson` was removed after the receipts were copied and again after the D2 re-fetch (`ls` → `No such file or directory`).

## 7. Out of scope / not done

- **S897's quote.** Not produced: that is ScoutDocS897's capture; the cell is `L1-FILL`.
- **Counters.** None exists; no leg was run; every counter-dependent cell is `L1-FILL`.
- **Spot-check.** No non-author review yet; the draft carries the requirement and its record path.
- **Claims and filed records.** Not edited; F1/F3/F4 are routed as decisions.
- **Held files.** Not adjudicated; only their dispositions as the claims state them are recorded.
