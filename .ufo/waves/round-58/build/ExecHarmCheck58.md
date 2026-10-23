# ExecHarmCheck58 — no-harm receipt for the owned axes (operability, calibration)

Seat: `KotodamaR58A2.ExecHarmCheck58`. Axes: **operability**, **calibration**. Advisory only: this seat writes no lane file except this report; nothing here is a verdict on claim C.

Sandbox clone: `/fast/scratch/hyaku/kotodama-r58/ExecHarmCheck58/sandbox` = `git clone --no-checkout` of the lane, checked out detached at **`adc28834502c132f55f8080440b1e2f91708713a`** (`round-58: declaration dry-run receipt at revision 5`, on top of claim base `80f48c2c`). Every command below ran there with `timeout 900`, `python3 -B`, stdlib only; nothing was written into the lane or the fleet repo, no git/jj write command was run anywhere. Scratch code and outputs: `/fast/scratch/hyaku/kotodama-r58/ExecHarmCheck58/`.

## 1. The six receipts

| # | command (cwd = sandbox at `adc2883`) | exit | reading |
|---|---|---|---|
| 1 | `python3 -B reports/round-57/accept-o.py` | **0** | `ACCEPT-O-57: PASS` — GEN, REAL, MULTI, MUTANTS, KEEP, FORMAT, SELFTEST all PASS |
| 2 | `python3 -B tools/check-gate-quotes.py --selftest` | **0** | `SELFTEST: 52/52 pass` |
| 3 | `python3 -B tools/check-source-access.py` | **0** | `ACCESS: 2 flagged rows, 0 findings` (S094, S132 — both `rejected`, so no finding) |
| 4 | `python3 -B reports/round-28/readme/sweep.py` | **0** | `rows 233 files 233`, `missing_from_index 0`, `topic_mismatch 0`, `totals_ok True`, `footer_ok True` |
| 5 | `python3 -B tools/check-gate-battery.py` | **0** | `summary {'battery_exit': 0, 'fail': 0, 'pass': 7, 'unevaluable': 0}`; `baselines_found 20, coverage 10/10, pinned 20`; `findings []` |
| 6 | `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` | **0 at base / 1 live** | read-only; at the declaration revision the lane is `kotodama ok` (W04 warnings only). On the **live** working tree now: exit 1, **17 × E05** — see §2.1 |

Raw transcript: `/fast/scratch/hyaku/kotodama-r58/ExecHarmCheck58/receipt-final.txt` (pasted in §3).

**Verdict on the receipt: green.** All six commands pass at the declaration revision `adc2883`; round 58 has not broken any of them. The one non-green reading is the fleet census against the *live* working tree, and that is caused by the round's own new rows, not by the instruments (§2.1).

## 2. Flags — what is not green, with the exact measurement

### 2.1 Fleet census `validate` is red: 17 new rows use a `kind` outside the contract enum (BLOCKING for lane hygiene)

```
$ cd /home/vgpnk/Projects/shokunin && ./scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
kotodama	E05	S505 kind=web      kotodama	E05	S514 kind=web      kotodama	E05	S524 kind=web
kotodama	E05	S506 kind=web      kotodama	E05	S515 kind=web      kotodama	E05	S525 kind=web
kotodama	E05	S507 kind=web      kotodama	E05	S518 kind=web      kotodama	E05	S526 kind=web
kotodama	E05	S508 kind=web      kotodama	E05	S519 kind=web      kotodama	E05	S527 kind=web
kotodama	E05	S509 kind=web      kotodama	E05	S532 kind=record   kotodama	E05	S542 kind=web
                                   kotodama	E05	S536 kind=record
                                   kotodama	E05	S537 kind=record
exit 1
```

- The contract enum is `SOURCES-CONTRACT-v1` line 24 (and the same enum in the census awk, line 78): `spec · docs · paper · code · tool · dataset · talk · book · community · own-work`. **`web` and `record` are not members.** `corpus/SOURCES.md` had 0 rows of either kind at base; all 17 are new round-58 rows.
- Cause: the **wave brief's own row template** prescribes `<kind: docs/paper/book/web/record/dataset/community>` — it conflicts with the contract. Seats followed the brief.
- Measured repair (scratch clone, `fixcheck3`, live SOURCES with `corpus/knowledge` symlinked so used-by resolves): map `web → docs`, `record → dataset` in those 17 cells →

```
$ sources-census.sh validate --file corpus/SOURCES.md --today 2026-10-23
      1 ok
     22 W04
CENSUS_EXIT=0
```

i.e. **the kind cells are the only blocker**; no E-code survives the rewrite. `web → docs` is the honest mapping for a served page; `record → dataset` for S532/S536/S537 (record/register pages). `accept-c.py` does not test `kind`, so ACCEPT-C-58 can go green while the fleet census stays red — worth fixing in the same landing.

### 2.2 S511's host rate-limits: the frozen predicate can flip to FAIL with no change to the row (calibration risk)

`https://www.land.vic.gov.au/` (root) and `.../place-naming/aboriginal-place-naming/how-to-get-started` (row page) intermittently answer **403**.

- A full `accept-c.py` run at **02:12Z** returned `LOCATE FAIL passing=43 cited=44 failing=['S511: … HTTPError']`, `BOILER FAIL … ['S511: not-located']`, `TOPIC FAIL … ['S511: quote_hits=1 not-located']` — the row was fine at 02:04Z.
- Repeating `rowcheck.check_row` on S511 eight times: `LOCATE 8/8`, **`BOILER` failed 2/8 (`root-unfetchable … HTTPError`)**, `TOPIC` failed 1/8.
- Direct root fetches: 2 OK then `HTTPError 403`.

So ACCEPT-C-58 is **non-deterministic on S511**. Options for the L1: swap S511 for a stable authority page, or add a Wayback capture beside the direct URL (the lane's own QUALITY criterion 10 treats "challenge met, then read through an ordinary copy" as not-a-bypass).

### 2.3 S506's anchor quote is 26 words — it will trip the 25-word Gate cap in the round-58 lesson

`check-gate-quotes.py` caps a quoted run in a `## Gate` section at 25 words. S506's first quoted span is 26 words:

```
$ python3 -B tools/check-gate-quotes.py /fast/scratch/.../gatetest/lesson506.md
…/lesson506.md:5 S506 words=26
GATE_QUOTES: 1 findings      exit 1
```

The same holds for records row **S569** (30 words). When writing `corpus/lessons/round-58.md`, quote a ≤25-word span of each (a shorter span still satisfies the row's LOCATE leg, which only requires the quote to be found on the page).

### 2.4 SUPPORT leg: it flipped FAIL → PASS inside the wave, and the mechanism is worth pinning

- At **02:04Z**: `SUPPORT FAIL … unsupported=[S500,S506,S512,S518,S524,S530,S536,S542: no verdict]`, and `.ufo/waves/round-58/support/SupportA58.md` did not exist although `registry.json` already listed `SupportA58` with an `agentId`.
- At **02:12Z**: `SUPPORT PASS unsupported=[] seats=['SupportA58','SupportB58','SupportC58','SupportD58','SupportE58','SupportF58']`.
- Mechanics confirmed by reading `accept-c.py:207-231`: seats are the `registry.json` members with `role: reviewer` **and a non-empty `agentId`**; verdicts are read only from `.ufo/waves/round-58/support/<Seat>.md`, line-initial `^VERDICT S\d{3} (SUPPORTED|NOT-SUPPORTED)`. A seat listed but with no file silently contributes nothing; **one** `NOT-SUPPORTED` anywhere fails the leg for that row. The build-wave reviewer seats (`ReviewSupersedeA58` … `ReviewCODH58`, `.ufo/waves/round-58/build/`) are records reviewers and do not feed this leg — the support wave is a separate producer, which is why the leg was red until it landed.

### 2.5 Pre-existing reds that are not round-58 harm (do not chase them)

- `python3 -B tools/check-gate-quotes.py corpus/lessons/*.md` → **67 findings, exit 2** at `adc2883` *and* on the live tree (identical count). Two of the errors are `no ## Gate section` for `round-56-verifier-spotcheck.md` and `round-57-verifier-spotcheck.md`. Pre-existing; the selftest (the declared receipt) is green.
- `check-readme-revisions.py` emits 1 warning `REVISION-ORPHAN lines=[166,177]` (exit 0) at base — pre-existing.
- Census **W04** warnings (same URL under two scopes) grew 14 → **22**: 8 new ones from records rows (S564/S565/S566/S569/S570/S571/S572/S573 duplicating S433/S438/S440/S453/S135/S141/S147/S151). W04 does **not** affect the exit status.

## 3. Pasted transcript (sandbox at `adc2883`, then read-only live census)

```
### [1] python3 -B reports/round-57/accept-o.py  (sandbox clone @ adc2883)
# tool tools/check-gate-quotes.py sha256 54981859e2032226abd52f8d04da0070995a5a9ecf89f014d4de63841a8716c7
# seeds [962504340, 962504341, 962504342, 962504343, 962504344] real-seeds [962504440, 962504441, 962504442]
GEN PASS lessons=5 failing=0 []
REAL PASS lessons=3 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] neutral_failing=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1, 'neutral-decode': 0, 'neutral-check': 0, 'neutral-run': 0}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 52/52 pass
ACCEPT-O-57: PASS
exit 0

### [2] python3 -B tools/check-gate-quotes.py --selftest  (sandbox clone @ adc2883)
PASS behavioural-continue-after-unreadable want=valid-findings-and-exit-2 got=(2, '/tmp/check-gate-quotes-selftest-i37oh6cv/entity.md:5 S901 html-entity\nGATE_QUOTES: 1 findings\n', "GATE_QUOTES_ERROR: /tmp/check-gate-quotes-selftest-i37oh6cv/invalid-utf8.md: not valid UTF-8 ('utf-8' codec can't decode byte 0xff in position 16: invalid start byte)\n")
SELFTEST: 52/52 pass
exit 0

### [3] python3 -B tools/check-source-access.py  (sandbox clone @ adc2883)
ACCESS: 2 flagged rows, 0 findings
exit 0

### [4] python3 -B reports/round-28/readme/sweep.py  (sandbox clone @ adc2883)
parts {"civilizations": 95, "culture-material": 29, "linguistics": 28, "myth-symbol": 28, "synthesis": 29, "verification": 24}
rows 233 files 233
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 233 totals_ok True
footer {"date": "2026-10-22", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 233, "dir_totals": [28, 28, 29, 29, 24, 95]}
footer_live {"total": 233, "dir_totals": [28, 28, 29, 29, 24, 95], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 215e23f8690d1f2a2b1f19c358ed10baa6b302e4ba9f2b863f734fa7b2d4987a
exit 0

### [5] python3 -B tools/check-gate-battery.py  (sandbox clone @ adc2883)
exit 0
summary {'battery_exit': 0, 'fail': 0, 'pass': 7, 'unevaluable': 0}
baselines {'baselines_found': 20, 'coverage': '10/10', 'pinned': 20, 'unevaluable': 0}
findings []

### [6] /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama  (read-only, live lane)
exit 1
kotodama	E05	S505 kind=web
kotodama	E05	S506 kind=web
kotodama	E05	S507 kind=web
kotodama	E05	S508 kind=web
kotodama	E05	S509 kind=web
kotodama	E05	S514 kind=web
kotodama	E05	S515 kind=web
kotodama	E05	S518 kind=web
kotodama	E05	S519 kind=web
kotodama	E05	S524 kind=web
kotodama	E05	S525 kind=web
kotodama	E05	S526 kind=web
kotodama	E05	S527 kind=web
kotodama	E05	S532 kind=record
kotodama	E05	S536 kind=record
kotodama	E05	S537 kind=record
kotodama	E05	S542 kind=web
(W04 warning lines suppressed: 22)
```

At the same base revision the same census command reads `kotodama ok …/corpus/SOURCES.md` with 14 W04 warnings and exit 0 — i.e. §2.1 is introduced by the round's rows, not inherited.

## 4. Landmines measured by simulation (each was executed, not inferred)

All in throw-away copies under `/fast/scratch/hyaku/kotodama-r58/ExecHarmCheck58/{sim-land,sim-full,sim-reg2,sim-reg3,sim-reg4,fixcheck3,gatetest}`.

| # | move | measured result |
|---|---|---|
| L1 | add `corpus/knowledge/linguistics/toponymy-place-names.md` only | `accept-c SET PASS count=234`; `sweep` stays **exit 1** until `corpus/README.md` gains the index row, the section count (`## linguistics/ (28)` → `(29)`), `Total knowledge entries: 234.` and the footer `(total 234 files; directory totals 29/28/29/29/24/95)` — all four together give `rows 234 files 234 / footer_ok True / exit 0` |
| L2 | README index row text ≠ entry's `- topic:` field | `topic_mismatch 1` → sweep exit 1. The row text must equal the topic field with continuations space-joined (the live entry's 710-char topic currently matches) |
| L3 | `used-by` cell separated by `;` | census `E11 S501 missing used-by corpus/…; corpus/…` exit 1 — the census splits `used-by` on **commas only**, while `accept-c` USEDBY splits on `[,;]`. Commas only, or accept-c goes green and the census goes red |
| L4 | a `\|` inside any cell (e.g. inside the quote) | census `E01 S500 fields=12`; `check-source-access` → `ACCESS_INPUT_ERROR row S500 … has 12 cells, not 11`, **exit 2** → accept-c `ACCESS` leg FAIL. No pipes inside cells |
| L5 | bypass vocabulary in `source`/`anchor`/`teaches` (e.g. "the paywall was bypassed") | `ACCESS_FINDING status S501 mined`, exit 1 → accept-c ACCESS leg FAIL. Words to avoid in row cells: bypass, captcha, VPN, logged-in, session cookies, "solved/passed … challenge/login/paywall" |
| L6 | row appended after `## Paths` | census `E12 S500 row outside Registry section` → rows must sit inside `## Registry` (live rows are, 495-552 < 553) |
| L7 | two rows, same URL **and** same scope cell | census `E04 S502 duplicate url … within scope …`; same URL in *different* scopes is only W04 |
| L8 | new row reuses a URL already named below S500 | accept-c `FRESH FAIL rows_reusing_registry_urls=['S500']` (measured with `un.org/en/observances/sign-languages-day`, which S077 owns) |
| L9 | entry text contains a range such as `S500-S559` | accept-c `RANGE FAIL range_notation=['S500-S559']` — any `S###` + dash/`to` + `S###` span fails it. (The live entry carried this in its `- sources:` bullet earlier in the wave; it is now clear: `spans: []`) |
| L10 | entry without `- couples:` and without `calibrat*` | `tools/gates/provenance-audit.py corpus/knowledge` → `FINDING missing-couples`, `FINDING missing-calibration`, exit 1, `files=234 … findings=2`; with both present → `findings=0`, exit 0 |
| L11 | `accept-c` SUPPORT leg | needs `.ufo/waves/round-58/support/registry.json` members with `role: reviewer` + non-empty `agentId`, and a `<Seat>.md` per seat with line-initial `VERDICT S### SUPPORTED` for **every** cited row; verified PASS with two synthetic seats, FAIL with none (`SUPPORT FAIL … no registry: FileNotFoundError`) |

## 5. State of the claim counter at the time of writing (advisory)

`python3 -B reports/round-58/accept-c.py` on the live tree, 02:11-02:12Z: SET, SWEEP, FLOOR (44 ≥ 20), RANGE, STATUS, TIER, USEDBY, ACCESS, RELEVANCE, FRESH, DISTINCT (23 hosts ≥ 10), SUPPORT PASS; **LOCATE / BOILER / TOPIC fail on S511 only**, and that failure is the intermittent 403 of §2.2, not a row defect. Earlier in the same wave the counter was red for `range_notation=['S500-S559']` + `S559: no row` and for README `missing_from_index/topic_mismatch/footer` — both since repaired by the L1.

## 6. Risks and blockers

1. **Blocker for lane hygiene (not for ACCEPT-C-58):** 17 `kind=web|record` cells → fleet census `validate` exit 1. Repair is a 17-cell rewrite (`web→docs`, `record→dataset`), measured to clear every E-code.
2. **Calibration risk:** S511 makes the frozen predicate non-deterministic (BOILER 2/8 failures, one full-run LOCATE failure). A re-run check of ACCEPT-C-58 can fail with no code change.
3. **Lesson risk:** S506 (26 words) and S569 (30 words) anchors exceed the Gate 25-word cap; quote a shorter span in `corpus/lessons/round-58.md`.
4. **Sequencing facts:** the SWEEP leg needs the README edits *and* the entry; the ACCESS leg needs every SOURCES row to have exactly 11 cells (one pipe breaks it); the census `used-by` check needs the entry file on disk *before* the rows are validated; the SUPPORT leg needs its own registry + per-seat verdict files, which the build wave's reviewer seats do not produce.
5. Nothing here re-tests SUPPORT's substance — that is the reviewers' and the L1's call.

## 7. Bounds kept

No file in the lane or the fleet repo was created, edited or deleted by this seat except this report; no git/jj write command was run anywhere; every process ran under `timeout` (max observed wall time 96 s for `accept-c.py`); no subagent was spawned.

installs: none (nothing installed or updated; `uv 0.13.0` was already present and is what `reopen-quote.py` uses for PDF text).
