# CritFrontier — round 77 / wave 2 — attack on the Sources & frontier work

Seat `CritFrontier` (wave-2 falsifier, leaf; no subagents, no background jobs). Lane
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `211f9526800906e0c585d878d265c37e5e090c15`.
Named item under attack: the round-77 **Sources & frontier** surface — the staged Search-log note +
Paths bullet (`.ufo/waves/round-77/w1/stage/ScoutPathsSearch/sections.md`, reported in
`w1/ScoutPathsSearch.md`) and the lesson draft's `## Gate` + `## Sources & frontier`
(`w1/drafts/corpus/lessons/round-77.md`, reported in `w1/ScribeLesson.md`), graded by the staged
counter `w1/stage/ExecAdaptC/accept-c.py` + `claims-C.skeleton.json` + `SCHEMA-NOTE.md`.
All reads absolute under the lane; base content via `git show 211f952…:<path>`. Measured 2026-10-27.
Nothing outside `.ufo/waves/round-77/w2/` was written; no fleet/lane file was mutated; no scratch
was needed (no fixture); no installs (pacman paused; `git`, `python3`, `grep`, `sed` already present).

**Verdict in one line:** the Paths order S897→S898 is correct and the staged-file counts
(11/11/1/10) are true, but the Search-log note drops the claim's own negative sweep set (the exact
omission), the S898 Gate quote is 111 characters against the counter's frozen ≤80-character cap,
and the S897 Gate row is an unmerged `L1-FILL` whose staged evidence additionally fails two
evidence legs as filed (2617-char excerpt < 4096; fetched 2026-10-28Z vs access-date 2026-10-27).

---

## F1 — the exact omission: the Search-log note omits the claim's own negative sweep (the ground sweep over the base corpus)

**Counterexample.** The emitted note
(`w1/stage/ScoutPathsSearch/sections.md` lines 18–42) enumerates "Where searched" as exactly one
set: the eleven staged `naming-systems*` files plus the package's 132-row `SOURCES.append.md`. Its
counts are `Identified 11 theme files, screened 11, included 1 … excluded 10`. The claim it serves
(`CLAIMS-DRAFT.md` claim C) is a negative-sweep claim: *"Ground (negative sweep scope =
corpus/knowledge only): at the base the corpus holds no Chinese-language system-level account of
personal naming"*, established by `git grep -l -E 'lishisuo\.cssn\.cn|onomastica\.ijppan'
211f952… -- corpus/knowledge` → exit 1 (re-derived by ScoutDocS898 for its half: `onomastica|Kałużyńska|Kaluz` over `corpus/knowledge` → nothing; widening to `corpus/SOURCES.md` → only S543, a different document). That sweep *is a searched set* — and it is absent from the note's "Where searched" and from its counts.

**Precedent (the format the note copies).** Round 76's note
(`git show 211f952…:corpus/SOURCES.md`, `## Search log`, `**State-standard calendar compilation
(round 76).**`) carries the sweep inside "Where searched" verbatim: *"base coverage was swept with
the exact `git grep -l -E 'GB/T 33661' <base> -- corpus/knowledge` command."* Rule 5
(`/home/vgpnk/Projects/shokunin/CORPUS.md:126-128`): *"A negative claim carries its sweep."*
Claim C's negative premise is carried by that grep; the note, which exists precisely to record the
searched sets, records only the candidate set. A reader of the filed note cannot tell that the
base corpus was searched at all — the one set whose emptiness is the claim's ground.

**Second limb of the same omission.** The document-identity sweep over `corpus/SOURCES.md`
(820 rows; ScoutDocS898 measured only S543 Reszegi 2023 matching `onomastica`) is also a searched
set for this round and is likewise unrecorded. COLLCHECK's whole premise — that S897/S898 are new
documents, not re-registrations — rests on it.

**Impact.** Fixable defect, not a tradeoff. The INDEX `required_sections` regex
(`claims-C.skeleton.json`: `(?i)^\*\*[^*]*naming-system[^*]*\(round 77\)`) passes on the note as
emitted, so the counter will not catch it — this is exactly the class of hole the Gate/log review
exists for (r76 R76-M3 taught that regex-matched required_sections accept any conforming line).
The negative claim's sweep is the substance of rule 5; dropping it makes the note PRISMA-shaped
but ground-blind.

**Smallest safe correction.** Extend "Where searched" with the two measured sweeps before the
count block, mirroring r76:
`…; base coverage was swept with the exact git grep -l -E 'lishisuo\.cssn\.cn|onomastica\.ijppan'
<base> -- corpus/knowledge` command (no match), and corpus/SOURCES.md was swept for the two
documents (S543 only — a different document).` Optionally add the swept-set sizes (253 knowledge
files, 820 rows) so the searched set counts are actual, per this seat's brief. Also fix the
overclaim "each read directly on 2026-10-27": ScoutPathsSearch's own report says it read the
files' `ground:`/`topic:`/`source:` headers, not each file in full — say "headers and source
blocks of all eleven read".

## F2 — S898's Gate quote is 111 characters; the frozen-cap counter demands ≤80 — deterministic GATE/EVIDENCE red, and worse, GATE goes green on the *title*

**Counterexample (measured).**

```
$ python3 - <<'EOF'
q = "According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees"
print(len(q), len(q.split()))            # → 111 17
t = "Flowers, Plants, and Trees in Female Naming in China"
print(len(t))                            # → 52
EOF
```

The lesson draft's S898 admit row (`w1/drafts/corpus/lessons/round-77.md:20`) quotes the 17-word
attribution-bearing sentence the 22:49 claims adopted. But `w1/stage/ExecAdaptC/accept-c.py`
`MAX_QUOTE_CHARS = 80` (:187), `quote_ok` (:386-390), `QUOTE_RE` matching `«…»`, `"…"` **and**
`“…”` (:196). The claims text itself says only "≤25-word located quotes" — the char cap is
inherited lineage, and the staged counter kept it; SentinelSources F4 flagged exactly this
dependency for the earlier staged cell.

**The sharper defect is not the red — it is the wrong green.** `leg_gate` (:2033-2037) accepts
*any* `quoted_spans(row)` that passes `quote_ok`. The S898 row's own document cell carries the
ASCII-quoted article title `"Flowers, Plants, and Trees in Female Naming in China"` — 52 chars,
9 tokens, **passes both caps**. So GATE reports green while the actual 111-char Gate quote is
invisible to it. Then `_evidence_gate_quotes` (:1003-1010) collects that title as the quote to
find in the committed `S898.txt` window — a window the draft itself insists "must cover PDF p. 4"
(the 88-terms sentence). The title appears on the PDF in ALL-CAPS header form (`IRENA
KAŁUŻYŃSKA — Onomastica LXIX…` title page / running head), so the title-case span will not fold
into the window text (`_evidence_fold` = NFKC+whitespace only, no case-fold :988-989): EVIDENCE
goes red "Gate quote is absent from the stored window". A passing landing would need the title
string verbatim inside the evidence window — i.e., EVIDENCE would be verifying the citation title,
not the located Gate quote. The r76 Gate rows had no quoted spans in their document cell (their
format wrote `candidate a — S894, National Archives of Japan, https://…` with no `"` or `«`
delimiters except inside the quote cell); the r77 draft's title-in-ASCII-quotes is a new hazard.

**Impact.** If the L1 files the draft as-is: EVIDENCE red on S898; GATE green-for-the-wrong-reason
(a false positive hiding the over-cap quote). If the L1 "fixes" the red by quoting the title or a
different ≤80-char span without re-checking attribution, it drifts from the claims' own
attribution-bearing requirement (ScribeLesson R77-M14: the attribution clause is what the quote is
*for*). This is a fixable defect: the quote family has a conforming member.

**Smallest safe correction.** Make the Gate quote the 76-char, 12-token, verbatim-and-located span
`According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms` — still the
attribution-bearing prefix, still §3 ¶1 second sentence, journal p. 114 / PDF p. 4 — and drop the
ASCII quotes around the document title in the admit cell (use the «…»/italic form or none, so the
only quote-shaped span in the row is the Gate quote). One-line change in the lesson draft; no
counter change needed (cap stays 80 — changing the cap to fit the quote would be aiming).

## F3 — S897 Gate row is still L1-FILL although ScoutDocS897 already delivered a located quote — a merge-order gap that also masks three evidence-side defects

**Counterexample.** `w1/drafts/corpus/lessons/round-77.md:19` holds
`quote = L1-FILL`, `locator = L1-FILL`, `evidence = L1-FILL` for S897 — but
`w1/stage/ScoutDocS897/evidence.txt` already supplies them:
`quote: 名的使用要早于姓，兩者組合是一種後起的文化習慣` (23 chars, 1 whitespace token — inside both
caps), `locator: article lead (unnumbered introduction, paragraphs 2-4)… Quote = lead paragraph 2,
sentence 3`, `window` present, `access-date: 2026-10-27`. Meanwhile ScoutDocS897's recorded wave
output (`w1/w1-results.json`) is an unfinished scratchpad ("Oops window min 4096 not met because
anchor near start; must set start 0 and end 4096+?… Need report evidence actual outputs + exact
commands/raw…") and **no `w1/ScoutDocS897.md` report exists** — `ls w1/` shows ScoutDocS898.md but
no S897 sibling. The seat's official delivery is its truncated thought-stream; the usable artifact
lives only in `stage/`.

**Three latent defects inside that staged evidence the L1-FILL is hiding:**

1. `window: chars=2617 … before=551 after=2043` with `window-scope: excerpt` — under
   `MIN_WINDOW_CHARS = 4096` (counter :185, :1981-1983) an excerpt window of 2617 chars is EVIDENCE
   red. The scout's own truncated output recognised this and died mid-fix. The L1 must regenerate
   the window (extend `after` to ≥4096, or `window-scope: whole-document` with
   `visible-chars: 30676` as staged — ScoutDocS897 itself recorded 30676 visible chars).
2. `fetched: 2026-10-28T01:31:09Z` / `live-403 … 2026-10-28T01:31:07Z` / wayback `01:27:43Z` — UTC
   dates say the open happened on **2026-10-28Z**, while `access-date: 2026-10-27` and the claims'
   `access_date` and Gate declare the 27th. Evidence `access-date` is graded for presence against
   the declared date; a `fetched:` line saying the 28th next to `access-date: 27th` is exactly the
   "record states a token the artifact contradicts" class claim Ca exists to mine. (The response
   `Date` headers are server-side; the discrepancy is a timezone artifact and must be
   explained or the `fetched` line restated as local-date — it is unverifiable as filed.)
3. The scout prompt was built on a stale premise — *"The L1 probe got HTTP 403 (162 bytes) under
   BOTH the plain UA and the browser-shaped UA"* (w1/spec.json ScoutDocS897 item) — false per
   SentinelSources F1 and ScribeLesson G5 (browser UA → 200, 143252 B). The evidence correctly
   records the per-UA truth (`curl → 403/162`, `browser → 200/143252`), so the artifact survives,
   but any L1 lift of the *prompt's* summary into the row would resurrect the refuted claim.

**Impact.** Fixable defects. If L1 fills the Gate from `stage/ScoutDocS897/evidence.txt` verbatim,
it imports a failing window and a self-contradicting date pair; if L1 fills only the quote/locator
cells, the S897 row is conforming on its face (23 chars ≤ 80, located, dated) and GATE/EVIDENCE
still depend on the regenerated window.

**Smallest safe correction.** L1 fills S897's quote/locator from the evidence file (they are
delivered and conforming), regenerates the window to ≥4096 chars or `whole-document` scope, and
reconciles `fetched`/`access-date` (e.g. `fetched: 2026-10-27T<local>` or a note that response
Dates are UTC+1-day artifacts) before committing `reports/round-77/evidence/S897.txt`.

## F4 — informational: what is conforming and must not be "fixed"

- **Paths order S897→S898: PASS.** `sections.md` (b) emits
  `- Chinese naming structure and inventory — S897 → S898: …` — S897 (structure/history) precedes
  S898 (classification/inventory), matching the seat-spec order and the INDEX regex
  `^- [^\n]*S897[^\n]*S898`. Placement: appended at the end of `## Paths` (integrator's stated
  choice); r76 put its claim's bullet first — cosmetic variance, no leg grades position.
- **Staged-set counts: PASS.** `identified 11 / screened 11 / included 1 / excluded 10` — the 11
  files verify (`naming-systems.amend-2026-10-23{,b,c}` + `…-24{,-r10,-r11,-r12,-r13,-r14,-r15,-r16}`),
  1 adopted + 10 dispositioned, each exclusion carries a file-named reason and a flip where held.
  `40 − 11 = 29` outside-bound arithmetic is consistent across ScoutPathsSearch and ScribeLesson's
  staged census. `grep -c '^|' SOURCES.append.md` → 134 = header + separator + 132 data rows —
  true as stated.
- **Opened dates: PASS as drafted.** Gate section declares `Access date: 2026-10-27` and each
  admit row carries `2026-10-27`; but see F3.2 — S897's staged `fetched:` says the 28th UTC.
- **Reject table shape: PASS.** The refused/held table header carries `reason` + `flip` cells
  (counter `_gate_tables` reject-detection :1155-1157) and the refused staged ids
  S933/S934/S936 appear in it, satisfying the REJECTS leg's Gate presence half. Held ids listed in
  the same table are extra rows the reject parser also harvests — conforming, since the leg needs
  ≥1 reject row and every refused id present, but the L1 should confirm no leg reads "held" rows
  as refusals (the table's `disposition` wording distinguishes them).
- **Frontier section: PASS.** `## Sources & frontier` records 820→L1-FILL(822), the
  document-map (S897←S897, S898←S903), byte-identical D2 capture, absent `considerthese/` — all
  independently re-verified (base registry 820, max id S896; `ls -d considerthese` absent).
- **S898 title-span in the document cell:** after F2's fix it is the only quote-shaped span
  that must not exist; every other quoted span in the admit rows is intentional.

## Evidence index (commands + outputs, all run this session)

```
$ git -C <lane> show 211f952…:corpus/SOURCES.md | grep -n '^## \|^# '
→ 26:## Registry / 853:## Paths / 890:## Search log / 904:## Leads (unopened)   [via ScoutPathsSearch, re-verified]
$ git -C <lane> show 211f952…:corpus/SOURCES.md | grep -c '^| S'
→ 820                                                                            [ScoutPathsSearch, consistent]
$ git -C <lane> show 211f952…:corpus/SOURCES.md | sed -n '/State-standard calendar compilation/,/Leads (unopened)/p'
→ r76 note carries "base coverage was swept with the exact git grep -l -E 'GB/T 33661' …"  [verbatim above]
$ grep -n 'Search log' /home/vgpnk/Projects/shokunin/CORPUS.md
→ 126: 5. **Search log.** … identified / screened / included / excluded counts … A negative claim carries its sweep.
$ grep -n 'Gate' /home/vgpnk/Projects/shokunin/CORPUS.md
→ 113: The round lesson's `## Gate` records, for every new row, the URL, the access
→ 114: date, and a ≤25-word quote with its location grounding `teaches`.
$ grep -n 'MAX_QUOTE_TOKENS\|MAX_QUOTE_CHARS\|QUOTE_RE\|MIN_WINDOW_CHARS\|def quote_ok\|def quoted_spans\|_evidence_gate_quotes\|def _evidence_fold\|def leg_gate' \
    w1/stage/ExecAdaptC/accept-c.py
→ 185:MIN_WINDOW_CHARS=4096 · 186-187:25/80 · 196:QUOTE_RE (「」 "" “” «») · 382-390 quoted_spans/quote_ok
   · 988-989 _evidence_fold = nfkc_ws (no case-fold) · 1003-1010 _evidence_gate_quotes · 2011+ leg_gate
$ python3 -c "print(len('According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees'))" → 111
$ python3 -c "print(len('According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms'))"            → 76
$ python3 -c "print(len('名的使用要早于姓，兩者組合是一種後起的文化習慣'))"                                              → 23
$ grep -n 'quote\|locator\|window\|fetched\|access-date' w1/stage/ScoutDocS897/evidence.txt
→ quote 23 chars located lead ¶2 s3 · window chars=2617 · fetched 2026-10-28T01:31:09Z · access-date 2026-10-27
$ ls w1/ | grep -i scoutdoc
→ ScoutDocS898.md only (no ScoutDocS897.md)
$ python3 -c "…w1-results.json…" → ScoutDocS897 output = truncated scratchpad (verbatim excerpt above)
```

## Not run / out of scope

- `reports/round-77/accept-c.py` does not exist at lands yet (no freeze, no landing); the staged
  counter was read, not executed — F2/F3 predictions are from its source, labeled as such.
- The 12-leg Ca counter and ledger pairs are other seats' lanes.
- Whether the r77 freeze keeps `MAX_QUOTE_CHARS = 80` is the L1's call; F2's correction is safe
  under either cap, which is why it is the recommended fix rather than "drop the cap".
