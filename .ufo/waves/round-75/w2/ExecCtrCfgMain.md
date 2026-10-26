# ExecCtrCfgMain — round 75, wave 2: the counter's config block and entry point

Seat: executor (leaf). Both files are function definitions only; nothing of the round's data was
graded (the lane tree is still the base). Files written:
`parts/part-cfg.py`, `parts/part-main.py`, this report, and the three receipts beside it
(`ExecCtrCfgMain-tests-main.txt`, `ExecCtrCfgMain-tests-cfg.txt`, `ExecCtrCfgMain-receipt-p1.txt`).
No lane/fleet byte outside `.ufo/waves/round-75/w2/` was written; read-only git only; no installs,
no pacman (`curl`/`git`/`python3` sufficed). Scratch `/fast/scratch/hyaku/kotodama-r75/ExecCtrCfgMain/`
(mock clone, assembled counter, transcripts) removed after copying the receipts.

```
3250a6d8b5788d028e2e31b0d3f6af72a38ee79baeb4d5ae1f38a39487775a89  parts/part-cfg.py   (585 lines)
9237ca0bdabeea6b9e376e5485941272c5b7fda4caf79086cae43ca09dfde56a  parts/part-main.py  (265 lines)
```

## 1. The wording as I read it

`part-cfg.py` implements CFG-CONTRACT §"cfg": `load_frozen_config(root, freeze)` returns **exactly**
the 23 named keys, every value read with `git show <freeze>:reports/round-75/claims.json`, plus the
shared leg helpers the contract assigns to this file (`_row_url_keys _gate_admit_row
_min_entry_words _evidence _window _entry_citations`) at their round-74 names and signatures.
`part-main.py` implements the frozen claim-C leg **set and order**
(`ENTRIES ROWS REPOINTED GATE EVIDENCE REJECTS GROUND CITEDLINES CENSUS SCRATCHMIRROR COLLCHECK
FROZENCFG INDEX`), `run_legs`, `print_receipt`, `refuse` and `main`, with the claim's own control
text: "`<lands> == <freeze>` is graded, not refused" and "`lands == the frozen claim base` is a
refusal that still prints FAIL".

Readings I had to take (each is a comment in the file):

| # | Ambiguity | Reading taken |
|---|---|---|
| A1 | GATE needs "access date 2026-10-27"; claims.json has no `access_date` key | Derive: `claim.access_date`, else `doc.access_date`, else the most frequent `YYYY-MM-DD` in the frozen `after`+`legs` text (ties -> earliest). No candidate = `ConfigError` (refuse). Never hardcode the date. On the current draft it yields `2026-10-27`. |
| A2 | REPOINTED forbids "staged ids `S864..S876`/`S885..S921`" but `S885` is itself an adopted lane id | `forbidden_ids = staged ids − lane ids` (CritCCounterVacuity repair 4, SimplifierRows §8c). Currently 11 ids: S864 S865 S866 S870 S876 S902 S904 S905 **S917** S919 S921 — S885 (identity map) and every lane id are never forbidden. |
| A3 | `refused_staged` may name S870 in prose that also names lane id S893 | Keep only ids that are **staged and not lane** -> `["S870"]`; raw prose in `refused_staged_text`. A re-quoted row is therefore derivable as `row_staged[sid] ∩ refused_staged`, which is how the r75 GATE re-quote clause (staged S870 -> lane S893) is reachable without a `forced_new_quotes` key. |
| A4 | `counts` "may be {}" | Faithful pass-through of `rejects.counts`: every int-valued key is coerced to `int`, non-integer values are dropped, nothing is synthesised. After the L1's pre-data edit (2) the frozen draft carries `{adopted 3, path_present 6, refused 31, total_staged_files 40, note "<prose>"}`; the loader yields exactly the four ints (the `note` prose stays in the frozen file, not in cfg). Before that edit it yielded `{}`. |
| A5 | `map.sha256` is `null` in the draft | A non-64-hex digest at freeze is `ConfigError` (refuse): an unpinnable map makes FROZENCFG/COLLCHECK ungradeable. **Freeze prerequisite** (see §6). |
| A6 | claim text says "one row per distinct document", staged side written `S876/S885/S917/S921` | `_row_pairs` accepts one id, a `/`-separated string or a JSON list, returns `(lane, [staged…])`; a staged id claimed by two lane rows is refused as an ambiguous map. |
| A7 | "each row source carrying the document URL" but Persée full text is only readable page by page | A per-page transcription is a **view** of the document and a Wayback wrapper a **carrier**: `_doc_url_key` folds both, `_row_url_keys` returns raw ∪ folded keys, `_gate_admit_row` joins on folded keys. So a row whose source cell carries `/doc/<slug>` still joins a page-level citation, and a page the cell does not carry still joins by document. |
| A8 | INDEX "myth-symbol heading equals the live count (32)" is another claim's line | `owned_inplace` is passed through verbatim (`corpus/README.md`, `## myth-symbol/ (29)` -> `(32)`) so the INDEX leg can exempt exactly those README heading lines (H4). This file does not grade README. |

## 2. Deliberate r75 deltas (each traceable to a w1 finding)

D1 multi-id staged rows (SimplifierRows §4, ExecRenumber §2/§3, RevAssimilationContract F1/F2) —
`row_staged` values are LISTs; identity is the document, not the occurrence.
D2 by-document map, no id arithmetic (ExecRenumber §1, §94-99).
D3 page-level Persée URLs + carrier/view folds, `%20` == raw space (SimplifierRows §4.1, SentinelScope S-75-2/S-75-9).
D4 `window-scope: excerpt|whole-document` (R74-M6; SentinelScope §7) — parsed in `_evidence`/`_window`,
graded by leg-evidence's `_evidence_core`.
D5 `terms` (r74 `cjk_terms` renamed by the frozen text; `ground.cjk_terms` still accepted as source).
D6 `owned_inplace` (README partition-heading exemption, A8).
D7 staged-only `refused_staged` (A3), so S885/S893 are never reported as refused staged rows.
M1-M6 in `part-main.py`: base refusal still prints FAIL; `lands == freeze` graded; LEGCOUNT against
the frozen list; scratch root `--work` / `$HYAKU_SCRATCH/kotodama-r75/counter` /
`/fast/scratch/hyaku/kotodama-r75/counter`, `/tmp` refused, per-run dir removed; receipt header per
PART A's docstring; `--selftest` says so instead of raising `NameError` when the selftest parts are
absent.

## 3. Positive / mutant table (all executed)

Mock landing: `git clone --shared` of the lane at `f556d10`, then `freeze` (claims.json with the
by-document map and its sha256 filled, map sha `4468f54e…d98e`), then `lands` (three draft entries,
the nine S885–S893 rows from the validate corpus, evidence from the probe receipts, lesson draft).
Assembled counter = PART A (1–510) + part-cfg + 13 stub legs + part-main, `python3 -B -m py_compile`
clean; with `__file__` injected, 41 cfg-level checks and the main battery below.

### 3a. main (receipt: `ExecCtrCfgMain-tests-main.txt`)

| case | expected | observed |
|---|---|---|
| P1 lands (stub legs) | PASS 13/13, exit 0, receipt header | `ACCEPT-C-75: PASS legs=13/13`, exit 0, all 13 `LEG PASS` lines |
| P2 `lands == freeze` | **graded** (13 legs run) | 13 `LEG PASS` lines, `PASS legs=13/13`, exit 0 — no refusal |
| X1 `lands == base` | refusal, FAIL line, exit 2 | `REFUSED: lands f556d104… is the frozen claim base …` + `ACCEPT-C-75: FAIL legs=0/13 (refused: …)`, exit 2 |
| X2 frozen `legs[]` has 12 | LEGCOUNT refusal, exit 2 | refused, both name lists printed, exit 2 |
| X3 no claims.json at freeze | refusal, exit 2 | refused (`cannot read … at freeze 2425ff85`), exit 2 |
| X4 lands not descended from base (orphan root) | refusal, exit 2 | refused (`claim base … is not an ancestor of lands …`), exit 2 |
| X5 `--work /tmp/r75-x` | refusal (QUALITY 14) | refused, exit 2 |
| X6 `--selftest` with no selftest parts | refusal, not `NameError` | refused, exit 2 |
| X7 `--lands deadbeef` / X8 unknown revision | exit 2, no verdict line | both exit 2 |
| freeze whose claim C is renamed | refusal | `carries no claim with id C`, exit 2 |
| scratch root | created/removed | `--work`/$HYAKU_SCRATCH trees, default `/fast/scratch/hyaku/kotodama-r75/counter`; every run left the work dir empty |
| receipt grammar | `tools/check-receipt-seq.py` | `SEQ-… PASS stamped=e672afbf evaluated=e672afbf measured=e672afbf equal=True`, `TREE-… PASS`, `RECEIPT-SEQ: PASS` |

### 3b. cfg (receipt: `ExecCtrCfgMain-tests-cfg.txt`, 41 PASS / 0 FAIL)

C1 23 keys == contract · C2 rows S885..S893 · C3 `row_staged["S885"] == ["S876","S885","S917","S921"]`
· C4 three entries · C5 `terms` · C6 nine fragments · C7 `refused_staged == ["S870"]` · C8
`access_date 2026-10-27` · C9 thirteen frozen legs in claim order · C10/C11 forbidden = the eleven
staged ids the lane does not hold, no lane id · C12 `owned_inplace` · C13 map pinned · C14 `counts`
(`{}` on the blob the battery ran against; after the L1's pre-data edit the same loader yields
`{adopted 3, path_present 6, refused 31, total_staged_files 40}`, re-verified by execution)
· C15 `frozen_sha256` == the freeze blob's digest · C16 `row_doc` · C17 Persée page view folds to
`/doc/<slug>` · C18 Wayback carrier folds to the encoded original · C19 `docAsPDF` folds · C20 a page
the row cell does not carry joins by document · C21 `_row_has_url` true for the S892 capture, false
for an unrelated document · C22 `_gate_admit_row` joins a page-only, **id-less** admit row · C23 S892
`excerpt` 4097-char window, digest recomputed · C24 the parsed `fetch` carries both carrier and
document · C25 the S892 fetch joins the row through plain `neutral_url_keys` · C26 S885
`whole-document` 3720 == `visible-chars` · C27/C28 absent evidence / missing marker -> None · C29
`_all` keeps the verbatim line · C30/C31 citations · C32 `_row_pairs` spellings · C33 base floor 478.

### 3c. mutants (each turns its own check red)

| mutant | result |
|---|---|
| CM1 staged list carries `BOGUS` | `ConfigError: row_set carries a non-S-id staged item: 'BOGUS'` |
| CM2 `map.sha256: null` (the draft's value) | `ConfigError: claim map.sha256 at freeze is not a 64-hex digest …` |
| CM3 one staged id claimed by two lane rows | `ConfigError: row_set maps staged S876 to both S885 and S886` |
| CM4 `ground.terms` emptied | `ConfigError: ground.terms at freeze is empty` |
| CM5 frozen `legs[]` one short | `frozen_legs` = 12 -> main's LEGCOUNT refuses (X2) |
| CM6 `_doc_url_key` replaced by raw `norm_url` (fold removed) | C20 a page the cell does not carry no longer joins; C22's page-only admit row is not found (`(False, None)`) |
| CM7 carrier disclosure removed (`_archive_original -> None`) | C25 goes red: the S892 fetch key stays `web.archive.org/…` and never meets the row |
| CM8 naive `staged ∪ lane` forbidden set | would put `S885` in the forbidden set and fail the honest entry's `source: S885` line |
| (main) refusal for `lands == base` removed | the do-nothing control would print `PASS legs=13/13` instead of X1's refusal |

## 4. Interface notes for the leg parts (not defects, but load-bearing)

1. **Carrier-aware joins.** `_row_url_keys(lands_rows, sid)` returns **raw ∪ document** keys. A leg
   that re-implements the comparison with `neutral_url_keys(...)` only works when the two sides spell
   the URL the same way. For S892 the evidence `fetch:` is the Wayback wrapper and the row cell is the
   live URL; `_evidence` therefore appends the carried original to the parsed `fetch`/`url`/`final-url`
   values (`GET <wrapper> (original <url>)`) so a plain
   `neutral_url_keys(urls_in(ev["fetch"])) ∩ _row_url_keys(...)` joins. The stored bytes are untouched
   (`_text`/`_all` keep the verbatim line). Prefer `_row_has_url(lands_rows, sid, url)` or
   `_url_keys(urls_in(...))` against `_row_url_keys(...)`; `leg-evidence.py`, `leg-gate.py`,
   `leg-repointed.py`, `leg-index.py`, `leg-mirror-coll.py` already call `_doc_url_key`/`_url_keys`/
   `_row_has_url`, so this is consistent with what is on disk.
2. **`_evidence` return shape**: first-wins scalar header dict (capture-evidence grammar:
   `url ua http bytes sha256 visible-chars window-scope window-sha256 window-bytes access-date
   http-status fetch user-agent locator quote …`) plus `_text`, `_window`, `_all` (verbatim
   `(key, value)` pairs, for QUALITY 22 two-request records), `_original` (carried URLs). Missing
   file -> `None`. No flag line is ever read.
3. **`run_legs` catches `Missing`, `OSError`, `RuntimeError`, `ValueError`, `TypeError`, `KeyError`,
   `AttributeError`, `SubprocessError`** per leg: a leg expecting a cfg key the contract does not
   carry produces a red line, not a traceback. `cfg` has exactly the 23 contract keys — in
   particular there is **no `path_present`**, `forced_new_quotes` or `folded_dropped`
   (`leg-rejects.py:180` already guards with `cfg.get("path_present") or []`, so its path-present
   clause is inert at r75 by design; the *number* is reachable as `cfg["counts"]["path_present"]` = 6,
   but the file list is not, and activating the clause needs a contract amendment, not a counter edit).
4. **Assembly order**: `part-selftest-fixtures.py` and `part-selftest-run.py` must be concatenated
   immediately **before** `part-main.py`'s guard (contract item 5). `main(--selftest)` looks
   `run_selftest` up in `globals()` and refuses with a clear line when it is absent (X6), so a wrong
   order is visible instead of a `NameError`. `part-selftest-run.py` invokes the counter as a
   subprocess with `TMPDIR` set into its own scratch; that does not change `_scratch_root`, which
   still refuses a `/tmp` root.
5. **`print_receipt`** prints the PART A header fields, including `# frozen map: <path> sha256=…`, the
   `# materialized: <how> at <path>` line, and `# lane worktree HEAD (disclosure only): …`. It is
   `stamped == evaluated == measured == <lands>` with `<lands>^{tree}`, which is what
   `tools/check-receipt-seq.py` accepted (receipt `ExecCtrCfgMain-receipt-p1.txt`).

## 5. Evidence and honesty of the claims above

Everything in §3 was executed in this session against the mock landing. The mock's landed registry is
the round's validate corpus (`.../assimilation/validate/corpus/SOURCES.md`), its evidence files are the
committed probe receipts (`S885`-`S890`, `S892`) plus two copies for `S891`/`S893`, and its entries are
the drafts — i.e. a **shape** mock, not the real landing, and no r75 data was judged. `S893`/`S891`
share S885's window in the mock; that is a mock artefact, not a claim about the landing. The counter
was never run against the lane worktree.

## 6. Freeze prerequisites this piece creates (for the L1, before dispatch)

1. `claims[C].map.sha256` must be a 64-hex digest of the committed
   `.ufo/waves/round-75/assimilation/id-renumber-map.json` at the freeze (today `null` -> refusal).
2. `claims.json` at `<lands>` must be **byte-identical** to the freeze blob; FROZENCFG grades that,
   and editing the file after the freeze is a red leg by design (H3).
3. `claims[C].legs` must keep exactly these 13 names in this order, and `ground.terms` must stay
   non-empty, or the counter refuses (LEGCOUNT / ConfigError) rather than grading.
4. The current draft (`e8007fc2d457d2e9408cd18565e51264a6a09b8623419e3b6895ad3f3f37692b`, 25 345 B —
re-read after the L1's three pre-data edits) loads cleanly through `part-cfg.py`: 9 rows, 3 entries,
`counts {adopted 3, path_present 6, refused 31, total_staged_files 40}`, 7
`refused_files_pending_triage` strings, `refused_staged ["S870"]`, 11 forbidden ids, 13 frozen legs
(INDEX last, its SHONEN clause removed without touching the leg's name), `map.sha256` still `null`.
Verified by execution, not by reading. The 41-check battery (§3b) ran against the previous blob
(`2308e298…16e7`); every check it makes is blob-content independent except C14, which now yields the
four counts.
5. `rejects.path_present_bytes_differ` (the r74 file list) is still absent: `counts.path_present` is a
   number, not a path list. `leg-rejects.py:180` reads `cfg.get("path_present") or []`, so its
   path-present clause stays inert unless the freeze adds the list — that would need a CFG-CONTRACT
   amendment, since cfg carries exactly the 23 contract keys.

## 7. Risks / blockers

- **R1 (medium, freeze-time)**: the by-document map does not exist yet and its sha256 is `null`; until
  the freeze fills both, the counter refuses (by design) and FROZENCFG/COLLCHECK cannot be graded.
- **R2 (medium, interface)**: a leg that compares URLs with raw `norm_url` keys only will fail on the
  S892 Wayback carrier and on any page-level Persée citation the row cell does not spell out. The
  carrier disclosure in `_evidence` covers the evidence side; the row side needs `_row_url_keys`
  (already used by the parts on disk).
- **R3 (low)**: `_gate_admit_row` falls back to an id-token match after the URL join (r74 behaviour).
  A Gate admit row that carries the id but a wrong URL therefore still *joins*; the URL check inside
  the GATE leg is what catches it. I did not strengthen this because the frozen GATE wording puts the
  URL requirement on the leg, not on the join.
- **R4 (low)**: `access_date` derivation reads `after`/`legs` prose. If the freeze rewords those
  clauses to carry two different dates equally often, the earliest wins deterministically; pinning
  `claims[C].access_date` removes the ambiguity entirely.
- No blocker stopped this seat: both files are complete, tested and staged.
