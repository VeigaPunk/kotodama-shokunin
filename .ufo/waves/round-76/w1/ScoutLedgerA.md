# ScoutLedgerA — round 76 w1 recon: Ca ledger pairs L76-01..L76-08 (sweep F1-F5, F7-F9)

Base `98c486bdb4650ba5b8e651d332910e8ee60ad121` (lane HEAD, `git rev-parse HEAD` printed it). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
**Verdict: 8 of 8 pairs red at base, all ANNOTATE (every stated site is the append-only round-75 lesson).** Nothing was installed, nothing outside the stage dir and this report was written, no lane git state was touched, scratch `/fast/scratch/hyaku/kotodama-r76/ScoutLedgerA` was deleted.

Artifacts (all under `.ufo/waves/round-76/w1/stage/ScoutLedgerA/`): `pairs.json` (the 8 pairs, round-75 ledger pair schema minus `statement_after`, which only REPAIR pairs carry), `build-pairs.py` (builds the pairs and runs each `observe_cmd`), `validate-pairs.py` (grades them with the round-75 `accept-ca.py` helpers, read-only import).

## Finding-to-pair map

The brief's lesson-line list maps to sweep findings as: lines 3-5 = F1, 15 = F2, 313-315 = F3, 330-333 = F4, 92-95 = F5, 244-246 = F7, 53-56 = F8 (whole-document census), 46-52 = F9 (note 2 windows). The sweep's own F6 (Ca command lacking `--combined`) is not in this brief and not paired. Line numbers in the sweep are against `4f5e3b2`; **at base the R75-M1 row is line 312** (not 313) and the R74-M8 `fails` text is line 332; the others match.

| id | stated_at (base) | stated text (token) | observe_cmd (argv, no pipe) | parse | stated → observed |
|---|---|---|---|---|---|
| L76-01 | `corpus/lessons/round-75.md:4` | `` `git cat-file -e HEAD:reports/round-75/claims.json` → absent, so the round's `` (`absent`) | `git grep -c -E '^' 98c486b… -- reports/round-75/claims.json` | `count-presence` | `absent` → `present` |
| L76-02 | `…:15` | ``the claims are `DRAFT`.`` (`DRAFT`) | `git grep -o -E '"status": "[A-Z]+' 98c486b… -- reports/round-75/claims.json` | `"status": "([A-Z]+)` | `DRAFT` → `FINAL` |
| L76-03 | `…:312` | `` `git cat-file -e HEAD:reports/round-75/claims.json` still fails: nothing of the round is committed `` (`fails`) | `git cat-file -t 98c486b…:reports/round-75/claims.json` | `^(\w+)$` | `fails` → `blob` |
| L76-04 | `…:332` | `` (`git cat-file -e HEAD:reports/round-75/accept-c.py` fails); the freeze must install both at the `` (`fails`) | `git cat-file -t 98c486b…:reports/round-75/accept-c.py` | `^(\w+)$` | `fails` → `blob` |
| L76-05 | `…:92` | `` `myth-symbol/narrative-structure-frameworks.md` (6862 B), `` (`6862`) | `git ls-tree -l 98c486b… -- corpus/knowledge/myth-symbol/narrative-structure-frameworks.md` | `blob [0-9a-f]+\s+(\d+)\s` | `6862` → `30920` |
| L76-06 | `…:55` | ``maximum available — the round-74 R74-M6 allowance, used as written. The other six declare `excerpt` `` (`excerpt`) | `git grep -o -E '^window-scope: [a-z-]+' 98c486b… -- reports/round-75/evidence/S891.txt` | `window-scope: ([a-z-]+)` | `excerpt` → `whole-document` |
| L76-07 | `…:246` | ``S886, S887, S891, S892 → `amend-2026-10-23`; S888, S889, S890, S893 → base.`` (`amend-2026-10-23`) | `git grep -o -E '^\| S891 \|.*' 98c486b… -- corpus/SOURCES.md` | `narrative-structure-frameworks\.(amend-2026-10-23b?)\.md` | `amend-2026-10-23` → `amend-2026-10-23b` |
| L76-08 | `…:47` | ``occur in the stored `--- window ---` text. S888's window (`chars=4097 before=10`) and S892's`` (`10`) | `git grep -o -E '^window: chars=[0-9]+ min=[0-9]+ pad=[0-9]+ before=[0-9]+' 98c486b… -- reports/round-75/evidence/S888.txt` | `before=(\d+)` | `10` → `3266` |

Full `stated_text`, `stated_parse`, `why`, `rederive` are in `pairs.json` (`stated_text` is verbatim from the base line, single line, whitespace-normalised containment).

## Raw observation output (run from the lane, read-only; `build-pairs.py`)

```
L76-01 rc=0 stated='absent' observed='present'   out: 98c486b…:reports/round-75/claims.json:227
L76-02 rc=0 stated='DRAFT' observed='FINAL'      out: 98c486b…:reports/round-75/claims.json:"status": "FINAL
L76-03 rc=0 stated='fails' observed='blob'       out: blob
L76-04 rc=0 stated='fails' observed='blob'       out: blob
L76-05 rc=0 stated='6862' observed='30920'       out: 100644 blob 29baa5159af1fb122f655e483fa29d7d9d58c418   30920	corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
L76-06 rc=0 stated='excerpt' observed='whole-document'  out: 98c486b…:reports/round-75/evidence/S891.txt:window-scope: whole-document
L76-07 rc=0 stated='amend-2026-10-23' observed='amend-2026-10-23b'  out: …corpus/SOURCES.md:| S891 | Roland Barthes, S/Z (Paris: Seuil, 1970), … (row text, first narrative-structure-frameworks match is amend-2026-10-23b.md)
L76-08 rc=0 stated='10' observed='3266'          out: 98c486b…:reports/round-75/evidence/S888.txt:window: chars=4096 min=4096 pad=400 before=3266
```
(`98c486b…` abbreviates the full 40-hex in the table above; the commands carry it in full.) `red_at_base: true` for all eight; `observed_at_base == expected_after` for all eight.

Grading with the round-75 counter's own functions (`validate-pairs.py`, `importlib` of `reports/round-75/accept-ca.py`, `observe_problem` static+dynamic guard on both `observe_cmd` and `rederive`, `stated_token`, stated-text-on-line check at base):
```
L76-01 on_line=True in_body=True stated_tok='absent' anchored=True observe_problem=None rederive_problem=None observed='present' parsed=True red= True
L76-02 … stated_tok='DRAFT' … observed='FINAL' … red= True
L76-03 … stated_tok='fails' … observed='blob' … red= True
L76-04 … stated_tok='fails' … observed='blob' … red= True
L76-05 … stated_tok='6862' … observed='30920' … red= True
L76-06 … stated_tok='excerpt' … observed='whole-document' … red= True
L76-07 … stated_tok='amend-2026-10-23' … observed='amend-2026-10-23b' … red= True
L76-08 … stated_tok='10' … observed='3266' … red= True
```
(every line `on_line=True in_body=True … anchored=True observe_problem=None rederive_problem=None parsed=True`; full output reproduced by `python3 -B validate-pairs.py` in the stage dir against `pairs.json`). No pipe, no shell; executables are only `git`. No absence-observation pair (no `git grep -c|-l` reading 0 with a positive numeric `expected_after`); numeric `expected_after` pairs (L76-05, L76-08) pin the base 40-hex as a bare argv element, as the round-75 NOCOUNT/base-pin leg requires.

## Supporting measurements (commands as typed)

- `git merge-base --is-ancestor 5d0167464309d8133991b30f7d7a7011a6a0fd14 98c486bdb4650ba5b8e651d332910e8ee60ad121` → exit 0 (round-75 freeze is an ancestor of base).
- `git cat-file -t 98c486b…:reports/round-75/accept-ca.py` / `git ls-tree -l 98c486b… -- reports/round-75/accept-ca.py` → blob / `100755 blob 05a4196f… 166430`.
- F5 siblings: `git ls-tree -l 98c486b… -- …amend-2026-10-23.md …amend-2026-10-23b.md` → `24166` / `23049` (lesson states 5933 B / 2514 B); `wc -c` on the worktree agrees for all three (30920/24166/23049).
- F8 census: `git grep -h -E '^window-scope:' 98c486b… -- 'reports/round-75/evidence/*.txt'` → 4 `whole-document` (S885, S886, S887, S891), 5 `excerpt` (S888, S889, S890, S892, S893); lesson says 3 / 6 and repeats "three times" at line 325 (R74-M6 pointer, not a separate pair).
- F7 siblings: registry `used-by` at base — S885 row: base + `amend-2026-10-23` + `amend-2026-10-23b` (lesson: base + `amend-2026-10-23`); S891 and S892 rows: `amend-2026-10-23b` only (lesson: `amend-2026-10-23`). Entry `source:` lines agree (`amend-2026-10-23b.md:3-5` cites S885, S891, S892).
- F9 sibling: `git grep -c -E '^window: chars=4097 min=4096 pad=400 before=2020' 98c486b… -- reports/round-75/evidence/S892.txt` → `…:1` (lesson note: `chars=4097 before=284`).

## Cautions for Ca (what a reader should know before freezing these pairs)

1. **F1-F4 are already acknowledged in prose at base but not corrected where the false statement sits.** The base lesson carries `## Status at landing` (line ~404-420: "no freeze commit exists", "the claims are `DRAFT`", "neither counter is committed" … this section supersedes them) and wave-3 item 1 lists F1-F13 as routed defects. The statements at lines 4, 15, 312, 332 are unchanged and still false, so the pairs are valid; but the ledger's `why` must not claim they are unknown. F7 (`used-by` mapping, L76-07) is **not** in the lesson's wave-3 item 1 list and no SCORECARD/LOG/QUALITY/SKILL/SHONEN row at base names it (`git grep` over those five files for `ExecCountsSweep|6862|30920|whole-document|before=3266` found only unrelated LOG:4326 and SKILL:291 hits) — it is the one pair no one has annotated.
2. **Vocabulary mismatch in L76-03/04** (`fails` vs `blob`): a pipe-free argv cannot print an exit status. `git cat-file -e` succeeds exactly when `git cat-file -t` prints a type, which the `why` states. If Ca prefers one vocabulary, L76-01's `count-presence` form (`absent`/`present`) is the cleaner one and can replace both, at the cost of a second pair on the same path (L76-01 already uses claims.json; L76-04 would need an accept-c.py `git grep -c -E '^'` form).
3. **Counter dependency.** L76-01 uses the `count-presence` parse and L76-05 uses `git ls-tree -l`; both are accepted by the round-75 `observe_problem` (checked above). A round-76 `accept-ca.py` adapted from round 75 must keep `count-presence` and `ls-tree` in the allowlist grammar or L76-01/05 need a different form.
4. **Line numbers are base numbers.** If the L1 appends to the lesson before the freeze nothing above line 404 moves (append-only), so the stated sites stay stable; the R75-M1 row at 312 (not 313) is the only deviation from the sweep's numbering.
5. **Not covered here:** F6 (Ca command without `--combined`; sweep row 26) and F10-F13; they are outside the brief. F6's site is `claims.json` Ca `after` + lesson:14, observation is a counter run (not expressible as a read-only argv), so it is probably not ledger-eligible.

## Unrun / not done

- The pairs were not run through a full `accept-ca.py` (no round-76 counter exists yet); only the round-75 helper functions were exercised, from the live lane at HEAD = base rather than from a materialised base clone. Result is equal because HEAD is base and `git status --short` showed only untracked `.ufo/waves/round-76/` and `reports/round-76/`.
- No attempt to write SCORECARD correction rows or `statement_after` paths (none apply: no REPAIR pair).

Report: .ufo/waves/round-76/w1/ScoutLedgerA.md
