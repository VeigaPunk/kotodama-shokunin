# ScribeRows — round 82, wave 1 (rows S904–S907 + the round lesson's `## Gate` draft)

Verdict: both deliverables are written and checked; the L1 has since landed its own
S904–S908 rows and the entry, so this report records (a) the draft as delivered,
(b) the measurements it is built on, and (c) six findings — two of them concrete
defects in the landed rows that the L1 can fix before freeze. Nothing installed,
nothing in the lane mutated outside this wave's directory, scratch removed.

## 1. Behaviour (what the draft files do)

- `drafts/rows/S904-S907.md` — four Registry rows in the contract shape, one line
  each, no literal or escaped pipe inside a cell: S904 Homer *Odyssey* (Butler,
  Gutenberg #1727, tier A), S905 Tacitus *Germania* (Church and Brodribb,
  Wikisource, tier A), S906 Ovid *Metamorphoses* VIII–XV (Riley, Gutenberg
  #26073, tier B), S907 EB11 "Guest" (Wikisource, tier B). All four `mined`,
  `opened 2026-11-04`, `recheck 365d`, `used-by
  corpus/knowledge/myth-symbol/guest-right-hospitality-law.md`. Each `source`
  cell names the live URL, the byte accounting, the UA pair and the same-page
  capture **that the installed evidence record names** (2026-09-25, 2026-02-06,
  2025-10-13, 2019-10-23); each `anchor` is `quote located: 「…」 (<n> words)`.
- `drafts/lesson-gate.md` — the lesson's `## Gate` block in this lane's shape:
  claim D admitted with the four rows and their fetch records; the superseded
  EB11 "Guest" reject (with the misread filed as the mistake behind QUALITY 30);
  one fresh reject (Frazer, *The Golden Bough*, filed as row S908, tier C,
  status `rejected`, QUALITY 27 fields: artifact + span + `present` + `flip`);
  two carried rejects (heraldry ground held, EB11 Coin/Mint with its disputed
  ground); claim O as an explicit L1 slot this seat did not verify; freshness
  carried paused; the census block with the before-state measured and the
  after-state `<L1>` slots; a `## Mistakes` slot naming six classes, each with
  the command that shows it and red-before evidence in
  `stage/ScribeRows/census-dryrun.txt`.

## 2. Gates run (command → output)

| check | command (abbreviated) | output |
|---|---|---|
| draft row shape | `split('|')` over the four draft lines | 13 fields, 11 non-empty cells, 0 empties, no `\|` |
| draft anchor counts | `len(span.split())` vs `(N words)` | 25 / 24 / 22 / 9 — all match |
| draft anchor presence | whitespace-normalise the fetched bodies, `count(span)` | 1 / 1 / 1 / 1 |
| capture presence (installed captures) | `id_` raw fetch of each installed capture, `count(span)` | 904 1, 905 1 (raw and folded), 906 1, 907 folded 1 / raw 0 |
| UA binding | one request per URL with the browser-shaped UA and one with the default | both `HTTP 200`, byte-identical bodies on all four rows and on S908, wall absent |
| census dry run (base bytes + rows spliced after S903) | the seven SOURCES-CONTRACT commands from `reports/round-49/run-validation.py` | rows 827 → 831, `NF!=13` 0, duplicate ids none, tier A=500 B=314 C=17, status mined=736 queued=58 rejected=37 |
| used-by existence (dry run, at that moment) | census used-by loop, cwd = lane root | 764 mined paths, exactly 4 missing — the four rows' shared entry path (absent then) |
| used-by existence (now) | same loop over the current worktree | no missing paths (entry landed, 28992 B) |
| registry placement (R81-M5 class) | rows after the `## Paths` line | good variant none; end-append variant `S904,S905,S906,S907` |
| row-shape class | `NF!=13` on a variant with one injected pipe | 1 (class detected; the shifted cell also corrupts the status histogram — the class's real cost) |
| landed rows: anchors | `count(span)` live and captured, `len(span.split())` vs declared | all five present 1/1; counts 8/8, 20/20, 11/11, 9/9; S908 declared 18 for a 16-word span — reported, and the L1 corrected it to 16 |
| entry citation lint (state evidence, not this seat's object) | `python3 -B tools/check-cited-lines.py corpus/knowledge/myth-symbol/guest-right-hospitality-law.md` | `CITED-LINES: 0 finding(s) in 1 file(s)`, exit 0 |

## 3. Findings

**F1 — the S907 reject ground is false on both artifacts, and the live page
carries prose.** Planned ground: "a plain fetch returns the Wikibase scaffold, not
article prose." Measured live (`curl -sSL <url>` → `HTTP 200, 13771 B transferred /
60273 B decoded`, byte-identical under both UAs): the sentence is a text node
inside the ProofreadPage paragraph — `grep -n 'one who receives hospitality'
guest-plain.txt` → line 518, paragraph closing `</p>` inside
`div.prp-pages-output`. The cited 2019-10-23 capture carries it once after
whitespace folding (raw 0: the HTML line-wraps it). The real limit is depth: a
single ~55-word gloss. L1 reproduced this and filed the first misread as the
mined mistake behind the new QUALITY 30.

**F2 — S905 substitution is forced, twice over.** On the planned Hovamol page the
hemistichs sit in separate `ws-poem-line` spans: `'Hail to the giver! a guest has
come;'` occurs 0 times in the served bytes; the longest contiguous poem run found
is 5 words (`'Where shall the stranger sit?'`, count 1). L1 also found the page
duplicates row S320 (same Bellows translation, Gutenberg #73533). S905 is Tacitus,
*Germania* ch. XXI, whose 24-word anchor is present once in body and capture.

**F3 — the carried EB11 "Mint" ground no longer holds.** `/Mint` → `HTTP 200,
148302 B`, 47165 characters of visible text, opening "MINT (Lat. moneta ; Mid.
Eng. mynt ) a place where coins are manufactured with the authority of the
state."; `/Coin` → `HTTP 200, 61002 B`, prose but a ~50-word stub. The carried
disposition stands (nothing depends on it) and the Gate records it as
carried-with-disputed-ground, not as a live reject.

**F4 — evidence-set conflict, resolved by the L1.** `reports/round-82/evidence/
S904.txt`–`S907.txt` were written by another seat while this seat was measuring
(different UA string, compressed byte counts). L1 ruled: the installed set stays
(the counter grades it and the rows cite it), this seat's `stage/S90*.txt` stay as
the independent second reading. The draft rows were then re-pointed at the
installed captures and byte figures; nothing was rewritten by this seat in
`reports/round-82/` or `corpus/`.

**F5 — context measured while verifying.** Base gap sweep: `git ls-tree -r
--name-only c285b2af… corpus/knowledge | grep -icE "guest|hospital|xenia|hospitium|stranger"`
→ 0 filenames; `git grep -inE "^- topic:.*(guest|hospital|xenia|hospitium)"` → 3
files, only `culture-material/cuisine-food-lexicon.md` names guest-right, and it
owns it as a table token at `:95,:138,:170` (bread-and-salt, `namak-halāl`). That
is the partial owner the entry points to one-way. `reports/round-82/telemetry/
census-start.txt` is a 34-line warning list ending `ok …/corpus/SOURCES.md` /
`census-start-exit=0`, not the seven counts; the counts are in `before.txt`.

**F6 — two defects found in the landed rows, both fixed by the L1.** (a) S907's
source cell inverted the byte accounting (read "60273 bytes transferred, 13771
decoded"; the record says transferred 13771, decoded 60273) — now corrected in
the landed row. (b) S908's anchor declared 18 words for a 16-word span
(「magic is a spurious system of natural law as well as a fallacious guide of
conduct」, `len(span.split())` → 16) — corrected to 16. The L1's census re-run is
green (exit 0, 832 rows). Everything else in the landed rows checks out: tiers,
status, `opened`, `recheck` and `used-by` match the draft's intent, and every
landed anchor is present once in both the live body and the capture the row
names. The draft rows and the Gate bullets were then re-pointed at the landed
anchors and at tier C for S907, so draft and registry no longer diverge.

## 4. Touched surfaces

Written (only these, all absolute):
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/rows/S904-S907.md`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/lesson-gate.md`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeRows/S904.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeRows/S905.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeRows/S906.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeRows/S907.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeRows/reject-golden-bough.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeRows/probe-eb11-mint.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeRows/census-dryrun.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeRows/sources-spliced-preview.md`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeRows/sources-endappend-preview.md`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeRows/sources-shape-mutant-preview.md`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/ScribeRows.md` (this report)

Not touched: `corpus/`, `tools/`, `reports/round-82/` (read only), `LOG.md`,
`SCORECARD.md`, git/jj state, the fleet repo, other lanes, `/home/vgpnk/Projects/shokuknow`.
No tool was installed. Scratch `/fast/scratch/hyaku/kotodama-r82/ScribeRows` removed
after the stage copies were made.

## 5. Out of scope / not verified here

- Claim O (`tools/check-sources-recheck.py`) — not read, not run; the Gate line
  for it is an explicit L1 slot, not an admission.
- The knowledge entry — the entry seat's object. This seat supplies rows,
  captures and the measured gap sweep. The `CITED-LINES: 0 finding(s)` line in
  §2 is state evidence read off the landed file, not this seat's deliverable.
- `corpus/lessons/round-82.md` — this seat wrote only the `## Gate` draft; the
  lesson assembly is the L1's.

## 6. Known limits

- `curl -w %{size_download}` reports transferred bytes; where the host or archive
  serves gzip the record states the decoded size separately (S904 265452 → 717784
  B; S905 41809 → 163266 B live, capture 36977 → 134891 B; S906 332350 → 853821
  B; S907 13771 → 60273 B; Frazer 858758 → 2287382 characters). This is exactly
  the axis on which the two evidence sets first looked contradictory.
- Word counts are whitespace splits of the quoted span; braced words count as one
  (Ovid's `{against them}` is two).
- The census dry run is pinned to the round base bytes
  (`git show c285b2af…:corpus/SOURCES.md`, 827 rows) because the worktree moved
  during the run (832 rows, entry present, `rejected=38` at the last read). Its
  "4 missing used-by" line is the state before the entry landed, not a current
  defect.
- The EB11 "Coin" URL was fetched once, default UA only; Mint ran the UA pair.
- QUALITY 27's mechanical one-liner greps a `| … | refused |` table row. This
  lane's Gate is a bullet list (round-81 shape), so that one-liner prints nothing
  and the reject stays review-only; the artifact + span + `present` fields are
  written for a human or a re-shaped check.
