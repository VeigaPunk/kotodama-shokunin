# ScribeRowsLesson — round-88 scoped findings

Seat: ScribeRowsLesson (scribe), kotodama round 88, milestone r88-v1.
Date: 2026-11-04. Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Pins: base `4956282281dac1306cfbe59523e46dde99749d75`; pre-dispatch controls
`0c8c733088df8c4f06770c9e714360eed7f29272`; frozen claims + counter
`4b76524c51e1c2f76c99eeb3b629cfac08a44a76`.

Axes judged: operability, depth. Leaf member — no subagents dispatched.

## What I produced

Two stage artifacts, both drafts for L1 to integrate. Nothing is landed.

- `.ufo/waves/round-88/w1/stage/ScribeRowsLesson/sources-rows.txt` — the three
  candidate registry rows S931/S932/S933 in the fleet 11-cell schema
  (`NF=13` measured on each line), the three Gate lines, the quote
  verification, and the reject Gate candidate.
- `.ufo/waves/round-88/w1/stage/ScribeRowsLesson/lesson.md` — the Gate prose,
  the Mistakes table, and a per-item disposition of every R87 routed defect.
- `.ufo/waves/round-88/w1/stage/ScribeRowsLesson/receipts/` — 25 receipt files
  (source copies with digests, wayback captures, counter outputs, census
  output and diff, probes).

## Sources actually opened (not search snippets)

Three external pages were fetched with a plain request on 2026-11-04 and the
bytes saved:

| id | source | live fetch | quote (≤25 words) located |
|---|---|---|---|
| S931 | Chrisomalis 2018, "The writing of numbers", Terrain 70 — https://journals.openedition.org/terrain/17506 | HTTP 200, 190567 B, sha256 `834d7621e477f8352a16a39c5ec7f39418e5abb2aedbec280343f30b0c4ec9ce` | "All numerical notations fall into five basic typological categories, across two dimensions" (12 w) |
| S932 | O'Connor & Robertson, "Babylonian numerals", MacTutor — https://mathshistory.st-andrews.ac.uk/HistTopics/Babylonian_numerals/ | HTTP 200, 65959 B, sha256 `ac4701fbcc05c878372e95f8c62334bd3d80f39c429844083bdbb9eb476f9d5f` | "A much more serious problem was the fact that there was no zero to put into an empty position." (19 w) |
| S933 | O'Connor & Robertson, "Egyptian numerals", MacTutor — https://mathshistory.st-andrews.ac.uk/HistTopics/Egyptian_numerals/ | HTTP 200, 23397 B, sha256 `5f6ef5ee12caca32f77c51673bb0ab17763d15ed6c6d0ee34a024d15a018d1b5` | "separate symbols for one unit, one ten, one hundred, one thousand, one ten thousand, one hundred thousand, and one million" (20 w) |

Same-page Wayback captures named in the rows: S931 → 20251023013631 (190137 B,
sha256 `130809407dfbc353730be3f36eaf61e7f35f1fc29b9218d5339bfa10dfd712bd`,
carries the quoted sentences; its embedded original normalizes to the live
URL); S932 → 20261013115420 and S933 → 20261021145158, both byte-identical to
the live copies.

Access note, disclosed in the S931 row: the *closest* capture of the Terrain
URL (20260223185515) serves an Anubis bot-check interstitial, not the
article, so it is not used as the anchor and no challenge was passed.

## Row changes old → new

| id | old | new | kind |
|---|---|---|---|
| S931 | — | new row, tier A, status mined, used-by `corpus/knowledge/linguistics/numerals-and-measures.md` | append |
| S932 | — | new row, tier B, status mined, used-by `corpus/knowledge/linguistics/numerals-and-measures.md` | append |
| S933 | — | new row, tier B, status mined, used-by `corpus/knowledge/linguistics/numerals-and-measures.md` | append |

No existing row's status, recheck or used-by cell is changed — no immutable-cell
edit. Registry counts measured on a scratch copy of the lane corpus with the
three rows appended inside `## Registry`: rows 854→857, tier.A 505→506,
tier.B 326→328, tier.C 23, status.mined 753→756, queued 58, rejected 43.

The three URLs are absent from the current registry, so no E04 duplicate and no
new W04. A sibling seat's uncommitted draft
(`reports/round-88/corrective-source-rows.txt`) proposes S934/S935 for
different subjects; no id collision, and this seat neither amends nor endorses
that draft.

## Gate candidate: admit + reject

Admit: S931 (A/mined), S932 (B/mined), S933 (B/mined), each with URL, access
date 2026-11-04, a ≤25-word verbatim quote and its location.

Reject candidate A (claim-level, no S-id, no registry row): the overstrong
teleological universal claim — that numeral notations universally progress
toward a perfect decimal positional system — is refused. Grounds are the opened
source's own sentences: "This avoids the teleological argument of Ifrah (1987)
and Dehaene (1997) that sees decimal, positional numeration as the end-point of
a developmental sequence towards perfection." and "In fact, using this typology
it is evident that there is no perfect system." Re-test tool and verbatim
output are carried in the Gate line
(`receipts/reject-retest.txt`: both needles HIT over the saved S931 bytes).

Why a claim-level rejection and not a rejected registry row: a SOURCES row
asserts what a source teaches; the only source opened here refutes the
teleological claim rather than teaching it, and filing S931 twice would trip
the census duplicate-URL rule on the same URL in the same scope.

## Measured checks (author-side, scratch; L1 re-runs on the landed tree)

| check | command | rc | result |
|---|---|---|---|
| row shape | `awk -F'\|'` on the three draft lines | — | NF=13 each (11 cells) |
| census validate | `scripts/sources-census.sh validate --file <scratch SOURCES.md> --today 2026-11-04` | 1 | output **byte-identical** to the same command on the unmodified registry (`diff` rc=0, 0 bytes) — no new E-code, no new W-code |
| census counts | `scripts/sources-census.sh census --file <scratch>` | 0 | rows 854→857, tier.A 505→506, tier.B 326→328, mined 753→756 |
| access check | `python3 -B tools/check-source-access.py --root <scratch> --sources <scratch SOURCES.md>` | 0 | "ACCESS: 3 flagged rows, 0 findings" — identical to the live baseline (3 pre-existing rejected rows; no new flagged row) |
| cited-lines lint | `python3 -B tools/check-cited-lines.py <entry with drafted section>` | 0 | "CITED-LINES: 0 finding(s) in 1 file(s)" — S-ids appear only in prose lines, never in a table row |
| frozen D counter on a scratch git fixture | `python3 -B reports/round-88/measure88.py --root <fixture> --base <base> --lands <lands> --claim D --work <dir>` | 0 | **7/7 legs passed**: heading 0→1, table-rows 5, table-columns 4, new-rows-cited 3 (S931/S932/S933), new-rows-mined 3 (A/mined, B/mined, B/mined), growth-bytes 2508 ≥ 2500 |

The D fixture is a scratch git repo (base `0eef7f75`, lands `54a0f12a`) carrying
the drafted section and the drafted rows. It measures the frozen counter over
draft bytes; it is **not** a claim that the lane lands the claim.

## Claim O — measured, and not met

At the freeze revision the frozen counter's five score legs already read
honest 13/13, constant-pass 3, shotgun-all-labels 4, extra-id 4, filename-only
0 — all five pass. The three battery legs fail, because
`tools/check-finding-sets.py` exists at no revision in this repo
(`git log --all -- tools/check-finding-sets.py` returns nothing). Total 6/9
legs, rc 1. **The O claim is not met at the freeze revision and this report
does not assert that it is met anywhere.** The comparator is the lands-side
deliverable of another seat.

## Findings (reported, not repaired)

1. **False green in the frozen counter's own transport selftest.** `measure88.py
   --selftest` exits 0 and prints three checks all `passed: true`, but its
   nominal exact-accepted positive child exits 1 with a FileNotFoundError
   traceback (it treats a JSON body as a pathname), and the extra-id check is
   assigned success independently of the observed outcome. Measured:
   `python3 -B reports/round-88/probe-counter-selftest.py --work <dir>` prints
   `false_green: true`, `child_rc: 1`, `suite_rc: 0`, exits 1
   (`receipts/probe-counter-selftest.json`). The frozen counter is not repaired
   and not re-scored here; the finding is recorded so the `battery-selftest:exit`
   leg is read as a transport fact only.
2. **A memorizing forgery still passes the 13-case battery.** A
   content-hash-keyed oracle carrying the full expected `(rc, ids, records)`
   table for every case payload scores **13/13** against the frozen counter
   (`receipts/probe6.py`). Opaque case filenames defeat filename-keyed and
   case-name-keyed oracles (both 0/13) but not content memorization —
   exactly the bound QUALITY 34 already states. The O claim's own bounds
   exclude arbitrary-forgery resistance, so this is a stated bound, not a kill.
3. **Frozen counter docstring drifts from its own code.** `measure88.py` line 13
   says "filename-oracle 1"; the EXPECT table and the frozen claims say 0, and
   the measured value is 0. Comment/code drift in a frozen file — reported, not
   edited.
4. **R87 routed defects — dispositions.** R87-C1 (membership → exact set
   equality) is addressed for the new comparator only, with the pre-dispatch
   red-before (12/12 each) against the new scores (4/4/0); the frozen r87
   counter is unchanged, as R87-C1 required. R87-C2 (literal `total=12` in the
   TOOL_ABSENT branch) is addressed in the new counter, which has no such
   branch and returns `INPUTS_ABSENT` rc=2. R87-C5 (receipt pinning) and
   R87-C6 (the "attack3/10" counting rule) are addressed in the round-88
   artifacts. R87-C3 (S929 quotation truncation), R87-C4 (LOG binding), R87-C7
   (SHONEN disclosure), R87-C9 (the untracked round-79 file) and the whole
   R86-C1/C2/C5/C6 family remain open and are named as open in the lesson.
   No item is claimed fixed without a receipt.

## Paths written

- `.ufo/waves/round-88/w1/stage/ScribeRowsLesson/sources-rows.txt`
- `.ufo/waves/round-88/w1/stage/ScribeRowsLesson/lesson.md`
- `.ufo/waves/round-88/w1/stage/ScribeRowsLesson/receipts/` (25 files)
- `.ufo/waves/round-88/w1/ScribeRowsLesson.md` (this report)

Scratch `/fast/scratch/hyaku/kotodama-r88/ScribeRowsLesson/` holds the working
copies and the scratch git fixtures; every receipt it contains was copied into
the stage directory first.

## Unresolved defects for the canonical judge

- O is unmet at the freeze revision (6/9 legs); the comparator
  `tools/check-finding-sets.py` is absent from every revision.
- The frozen counter's transport selftest is a false green (finding 1). A
  production comparator's independently passing selftest would not certify
  that instrument.
- The 13-case battery remains defeatable by content memorization (finding 2).
- R87-C3, R87-C4, R87-C7, R87-C9, R86-C1, R86-C2, R86-C5 and R86-C6 stay open.
- Formal planner-policy conflict (R86-C4) retained; L1 holds the planner seat.
- Chrisomalis 2004 (doi 10.1017/s0959774304000034) and Chrisomalis 2010
  (doi 10.1017/cbo9780511676062) answered HTTP 429 on 2026-11-04 and were not
  opened; Ifrah 1987 and Dehaene 1997 were likewise not opened. Nothing in the
  proposed rows or section depends on their text.
- No tools installed or upgraded. No production file, fleet-root tracked file
  or sibling stage was written. No git or jj mutation was made; no commit, no
  push.
