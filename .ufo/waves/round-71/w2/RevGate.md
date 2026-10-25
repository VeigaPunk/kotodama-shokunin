# RevGate — round-71 lesson Gate falsify seat (wave 2)

- Seat: `L1Kotodama71.RevGate` (leaf reviewer, read-only on lane; this file is the only write)
- Date: 2026-10-25 · lane HEAD `ccadb59` · checker sha256 per wave-1 MutGateQuotes `54981859…`
- Scope: `python3 -B tools/check-gate-quotes.py corpus/lessons/round-71.md` (expect 0 findings); the 13 Gate quotes ≤25 words; quotes match the fetched page text (≥5 spot-checks).

## Verdict summary

| check | result | verdict |
|---|---|---|
| checker prints `GATE_QUOTES: 0 findings`, exit 0 | reproduced | PASS as printed, but **vacuous** (finding F1) |
| 13 Gate quotes ≤25 words (whitespace split) | max 15 words (S861); all 13 ≤25 | PASS |
| quotes verbatim in fetched page text | 13/13 exact substrings (more than the 5 asked) | PASS |
| ACCEPT-CA-71 gate leg matches its declared predicate | the counter never runs the checker | FAIL (finding F2) |

## Findings by severity

### F1 — HIGH: `check-gate-quotes.py` never scans the round-71 Gate rows, so its "0 findings" doesn't verify anything

- Its row regex is `ROW = re.compile(r"^(?:-\s+(?:\*\s+)?|\*\s+)(S\d+)\b")` (`tools/check-gate-quotes.py:102`), so it only accepts bullet rows (`- S187 — …`). `scan_line` returns `[]` for any line that doesn't match `ROW`. The round-71 Gate is a pipe table (`| S861 — UNESCO Tango 00258 | … |`), so the checker parses none of its rows.
- Evidence (importing the module, read-only):
  `python3 -B -c 'import importlib.util as u;s=u.spec_from_file_location("g","tools/check-gate-quotes.py");g=u.module_from_spec(s);s.loader.exec_module(g);sec=g.gate_section(open("corpus/lessons/round-71.md").read());print(len(sec),len(g.gate_rows(sec)))'`
  prints `31 0`: the Gate section has 31 lines and the checker parses 0 rows.
- Mutation proof (on a temp copy that includes `corpus/SOURCES.md`; the lane was not touched):
  - Replace the S873 table quote with a 40-word quote: `GATE_QUOTES: 0 findings`, exit 0. **The mutant survives.**
  - Add the same 40-word quote as a bullet row `- S873 — "…"`: `…:12 S873 words=40`, `GATE_QUOTES: 1 findings`, exit 1. The cap logic works; only the row format is unrecognized.
- The same blind spot hits round 69 and 70: their Gates are also tables (1 table row and 0 bullet rows each; rounds 65–68 use 23–32 bullet rows). `python3 -B tools/check-gate-quotes.py corpus/lessons/round-70.md corpus/lessons/round-69.md` gives `0 findings`, exit 0. This is the root cause of CritClaimSizing's wave-1 observation that the checker "exits 0 on the unfixed 27-word quote" at base. The V70-3 escape happened because the checker never read the row, not because the word cap failed.
- Why wave 1 missed it: MutGateQuotes killed 5/5 mutants, but only against `--selftest`. All 52 selftest fixtures are bullet rows (`lesson('- S900 — …')`), with no table-form fixture. ReviewerGateBattery's `--selftest 52/52` has the same limit.
- Consequence: the Ca leg "check-gate-quotes exit 0 with 0 findings" (in the `claims.json` Ca predicate and target) is satisfied by any table-form Gate, whatever its quotes contain. It can't fail, so it is no evidence for V70-3 or for the round-71 Gate.
- Smallest fix (for the owning lane, not this seat): make `ROW`/`gate_rows` also accept `^\|\s*(S\d+)\b` table rows and scan only the quote cell, and add table-form fixtures to the selftest (a 26-word table quote must be flagged; a 25-word one must pass). Keep the docstring's "Gate row" definition in sync.

### F2 — MEDIUM: ACCEPT-CA-71 doesn't run the leg its predicate declares

- The `claims.json` Ca predicate: "`python3 -B tools/check-gate-quotes.py corpus/lessons/round-71.md` exits 0 with 0 findings". `reports/round-71/accept-ca.py` never calls the checker (`rg -n 'gate-quotes|GATE_QUOTES' reports/round-71/accept-ca.py` has no matches).
- Instead, `accept-ca.py:97-101` counts the whitespace-split words of `corpus/lessons/round-70.md` line 13, column 4: `r70[12].split("|")[3]`. That is a different file, a hard-coded line index, and the whole cell rather than the quote. Inserting any line above the round-70 table silently retargets the leg.
- Observed: `python3 -B reports/round-71/accept-ca.py` gives `LEG PASS V70-3 words=25 (want <=25)` and `ACCEPT-CA-71: PASS`, exit 0. The round-70 quote really is 25 words. It is verbatim from `tools/check-supersession-settlement.py:20-21`, where the trim stops at "…frozen ruling set," before "not globally —". So the value is true, but the counter measures something other than the declared predicate. Because of F1, running the declared command would also pass vacuously.

### F3 — LOW: V70-5's "candidate with reason+flip" leg is a bare word match

- `accept-ca.py`: `candidate_ok = bool(re.search(r"flip", lt, re.I))` matches the word "flip" anywhere in the lesson. The lesson does carry 8 rejected candidates, each with reason and flip (lines 34–40), so the content is present. But the counter can't tell that apart from a lone "flip" anywhere, which is a do-nothing-reachable leg.

## PASS evidence

### Checker run

`cd kotodama-shokunin && python3 -B tools/check-gate-quotes.py corpus/lessons/round-71.md; echo $?` gives `GATE_QUOTES: 0 findings`, then `0`. As F1 shows, this pass is vacuous.

### Word counts (whitespace split of the quoted span in each table row)

Command: parse `^| S8` rows of `corpus/lessons/round-71.md`, take the `"…"` span in column 3, and count `len(q.split())`.

| row | words | row | words |
|---|---|---|---|
| S861 | 15 | S868 | 10 |
| S862 | 12 | S869 | 11 |
| S863 | 8 | S870 | 6 |
| S864 | 10 | S871 | 10 |
| S865 | 8 | S872 | 8 |
| S866 | 10 | S873 | 6 |
| S867 | 7 | | |

All 13 rows are present (S861–S873, no gaps or duplicates) and all are ≤25. Each Gate quote is a verbatim prefix or substring of the longer (≤24-word) quote in `.ufo/waves/round-71/w1/ScoutOpenSourcesC.md`.

### Quote vs fetched page

Method: fetch each URL from the `corpus/SOURCES.md` rows 816–828 (Wayback capture URL where the Gate says "capture", live URL where it says "live"), strip tags and decode HTML, apply NFC and whitespace collapse, then do an exact `str.find`. All fetches returned HTTP 200 with no CAPTCHA frame ("human visitor") in any body.

| row | URL fetched | match | context located |
|---|---|---|---|
| S861 | web.archive.org/web/20260925201518/…/tango-00258 | exact | "…embodiments of that identity, the music, dance and poetry of tango both embodies…" |
| S862 | web.archive.org/web/20220323094705/…/mevlevi-sema-ceremony-00100 | exact | "…fast of several hours, the whirlers begin to rotate on their left feet…" |
| S863 | web.archive.org/web/20210514035531/…/chhau-dance-00337 | exact | "…martial practices. Its vocabulary of movement includes mock combat techniques, stylized gaits…" |
| S864 | web.archive.org/web/20210227223454/…/carnival-of-oruro-00003 | exact | "…the dancers walk the four kilometres of the processional route and repeat…" |
| S865 | web.archive.org/web/20210302140159/…/flamenco-00363 | exact | "Flamenco baile is a dance of passion, courtship, expressing…" |
| S866 | web.archive.org/web/20241111072724/…/talchum-…-01742 | exact | "…dance, music and theatre. An ensemble of six to ten musicians accompanies masked performers who…" |
| S867 | web.archive.org/web/20200330004935/…/kabuki-theatre-00163 | exact | "Two other major role types are aragoto (rough style) and wagoto (soft style)." |
| S868 | www.abt.org/explore/learn/ballet-dictionary/ (live) | exact | "Positions of the arms. Although the positions of the feet are standard in all methods…" (the Gate locator says "Positions of the arms", which matches) |
| S869 | web.archive.org/web/20260907171642/…/benesh-international/ | exact | "Benesh Movement Notation (BMN) is a system for documenting human movement. It is mainly used…" |
| S870 | ickl.org (live) | exact | "…originated by Rudolf Laban, known as Kinetography Laban or Labanotation." (the page has a space before "," and "." from markup; this is normalized) |
| S871 | wisdomlib.org/…/the-natyashastra/d/doc209696.html (live) | exact | "…five a Saṃghātaka. Thus the Aṅgahāras consist of six, seven, eight or nine Karaṇas." |
| S872 | wisdomlib.org/hinduism/book/the-mirror-of-gesture (live) | exact | "…by Nandikeshvara: an encyclopedic manual of the art of gesticulation." |
| S873 | plato.stanford.edu/entries/dance/ (live) | exact | "What counts as “philosophy” of dance? This is a vexed methodological question." (substantive revision Sep 3, 2025, consistent with "rev. 2025") |

13/13 match, well beyond the 5 spot-checks asked for.

## Residual risk and verification gaps

- Paragraph locators (for example "¶3") were spot-read in context only and not counted paragraph by paragraph. Context is consistent with the stated sections.
- Live pages (S868, S870–S873) can drift. Matches hold as of the 2026-10-25 fetch. Wayback captures are fixed by timestamp.
- No LSP check: this is Python tooling plus markdown, and the evidence comes from running the module, so no language server was needed.
- F1 also makes the round-69 and round-70 Gate quote-cap claims unverified by tool. I only re-counted round 70's single quote (25 words, verbatim); I did not re-audit round 69's quote.

## Tooling

No installs or updates: curl and the python3 stdlib only. No pacman transaction. Scratch files are in `/tmp/revgate/` (fetched HTML) plus a temp lesson copy that was deleted after the mutation run.
