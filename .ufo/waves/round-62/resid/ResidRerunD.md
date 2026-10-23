VERDICT ResidRerunD: HOLDS

Seat: KotodamaR62.ResidRerunD (read-only leaf, residual falsify, claim D reproduction)
Measured revision: a2c5caa59b2d67ce35e53d6ce0217030a66cdd48; freeze commit 9143fc442c209f6fd832bc7bf53ef5c0cd161ea1
Method: independent sandbox clone `/fast/scratch/hyaku/kotodama-r62/resid/ResidRerunD/clone`, checked out at a2c5caa5 with GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE unset. Both counters run exactly once each. No installs performed (operator directive 2026-10-19: nothing needed installing). No `lsp` device exists in this session's tool inventory, so all caller/definition/diagnostic checks were done by git-level and text-level evidence; recorded here as tool unavailability, not as semantic proof.

# 1. Reproduction — `python3 -B reports/round-62/accept-d.py` (run once, cwd = clone root)

```
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
KEEP PASS bad=[]
FRESH PASS reused=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T12:13Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

All 16 frozen legs (claims.json `claims.D.legs`) PASS; predicate line `ACCEPT-D-62: PASS`; exit 0.

# 2. Reproduction — `python3 -B reports/round-62/locate-control.py` (run once, cwd = clone root)

```
RECOVER PASS located=True passes_used=3 requests(live,capture)=(3, 5) want=(3, 5) pass_waits=2 virtual_s=136 detail=https://web.archive.org/web/20240529024530id_/https://example-live.invalid/talaria
EXHAUST PASS located=False passes_used=3 requests(live,capture)=(3, 9) want=(3, 9) pass_waits=2 virtual_s=168 detail=https://example-live.invalid/talaria HTTPError; https://web.archive.org/web/20240529024530id_/https://example-live.invalid/talaria HTTPError
ABSENT PASS located=False passes_used=3 requests(live,capture)=(3, 3) want=(3, 3) pass_waits=2 virtual_s=120 detail=https://example-live.invalid/talaria quote-absent; https://web.archive.org/web/20240529024530id_/https://example-live.invalid/talaria quote-absent
FIRSTOK PASS located=True passes_used=1 requests(live,capture)=(1, 0) want=(1, 0) pass_waits=0 virtual_s=0 detail=https://example-live.invalid/talaria
CAPTUREOK PASS located=True passes_used=1 requests(live,capture)=(1, 1) want=(1, 1) pass_waits=0 virtual_s=0 detail=https://web.archive.org/web/20240529024530id_/https://example-live.invalid/talaria
DNSFAIL PASS located=False passes_used=3 requests(live,capture)=(3, 3) want=(3, 3) pass_waits=2 virtual_s=120 detail=https://example-live.invalid/talaria URLError; https://web.archive.org/web/20240529024530id_/https://example-live.invalid/talaria URLError
LOCATE-CONTROL-62: PASS
exit=0
```

Note [INFO]: `telemetry/final-measures.txt` contains only the accept-d.py and accept-o.py receipts; the authoritative receipt for the locate control is `reports/round-62/telemetry/locate-control.txt` (referenced by claims.json `revision_note_1`). Compared against that file.

# 3. Leg-by-leg comparison against the authoritative receipt

Receipt block in `telemetry/final-measures.txt` (blob sha256 b098624e516e5e801eca12b6c547748b309e2c565d822e5a8306ac6d79d6e1d4 — byte-identical to the lane working-tree file and to `git show origin/main:reports/round-62/telemetry/final-measures.txt`):

```
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
KEEP PASS bad=[]
FRESH PASS reused=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T12:05Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

Byte diff (`diff` of receipt block vs my captured output) found exactly two differences, both expected:

1. [INFO] `LOCATE ... at=2026-10-23T12:05Z` (receipt) vs `at=2026-10-23T12:13Z` (rerun). The leg prints `datetime.now(timezone.utc)` at run time (accept-d.py:359-364); live wall clock, format identical, same located/cited/not_located values. My rerun's LOCATE was a real network fetch that located S693.
2. [INFO] The receipt's trailing `exit=0` line is absent from my captured file — artifact of my capture method (`tee` before the `echo exit=$?`); my run's exit status was 0 as printed.

Every other byte of all 16 legs matches. Locate-control rerun vs `telemetry/locate-control.txt` case block: `diff` exit 0 — byte-identical including all six cases' request counts and virtual waits.

# 4. Byte-identity of counters: 9143fc44 → a2c5caa5

- `git diff 9143fc44 a2c5caa59b2d67ce35e53d6ce0217030a66cdd48 -- reports/round-62/` → empty (no output).
- `diff <(git ls-tree -r 9143fc44 -- reports/round-62/) <(git ls-tree -r a2c5caa5 -- reports/round-62/)` → identical (all blob hashes equal).
- `git merge-base --is-ancestor 9143fc44 a2c5caa5` → true, so two-dot and three-dot diffs coincide.
- No commits touching `reports/round-62/` between freeze and measured revision (`git log 9143fc44..a2c5caa5 -- reports/round-62/` empty).
- sha256 at a2c5caa5 vs claims.json `freeze` block:

| file | sha256 @ a2c5caa5 | claims.json freeze | match |
|---|---|---|---|
| reports/round-62/accept-d.py | 0f60162532192c8e66054df1f6ce82edd6633e4413414810bd1fe1a188847f3a | accept_d_sha256 | yes |
| reports/round-62/accept-o.py | a222a156b95e0f716f0304c85bc38c2eb395f5dad5c9b4810476a87237ca8ba9 | accept_o_sha256 | yes |
| reports/round-62/locate-control.py | 67703e7fabaad5d7c2e0bca3a9bf6d15d821e134c795f73f55c91703fa07975e | locate_control_sha256 | yes |

Lane working-tree copies of accept-d.py and locate-control.py carry the same hashes (no post-measure drift of the instruments on disk).

# 5. Nothing landed after the measured revision changes a claimed object

- `git log --all --oneline a2c5caa5..` → exactly one commit on any ref: `25b44b8 round-62: final measures ...`, `2026-10-23 09:07:53 -0300`.
- Its full name-status: `A reports/round-62/telemetry/final-measures.txt` (36 insertions, new file only).
- Diffstat a2c5caa5..origin/main limited to claimed objects (`reports/round-62/`, `corpus/knowledge/culture-material/footwear-codes-terminology.md`, `corpus/SOURCES.md`, `tools/reopen-row.py`): only final-measures.txt. The repaired entry, SOURCES.md, tools/reopen-row.py and the frozen counters are untouched after the measured revision.
- Remote refs present: origin/main, origin/hyaku/s3-kotodama-r51-author, origin/hyaku/s3-ready66-kotodama; none carries commits beyond 25b44b8.

# 6. Independent spot-checks of the claimed object at a2c5caa5 (beyond the counter)

- Lines 63/74/75/93 at a2c5caa5 (`awk NR==63||74||75||93`):
  - 63: `- A sabot is a hollowed shoe made from one wooden block, worn especially by farmers and workers in the Netherlands, France, Belgium, etc. (S692)` — open list restored.
  - 74: `- A Bata Shoe Museum image caption says the heel originated in Western Asia centuries ago for horseback riding. (S665)` — caption attribution named.
  - 75: `- According to the BBC article, the earliest evidence we have of someone wearing heels is a 10th-century Persian bowl. (S666)` — hedge restored.
  - 93: `- Talaria are the wings or winged sandals worn on the feet of Hermes, or Mercury. (S693)` — support moved to new tier-B row.
- Base d42ffb89 same lines: `... Netherlands, France, and Belgium. (S692)` / `- A heel originated in Western Asia for horseback riding before Europeans adopted it. (S665)` / `- The earliest evidence of someone wearing heels comes from a 10th-century Persian bowl. (S666)` / `- Hermes' talaria were winged leather boots. (S687)` — matches claims.json `unmoved_command` exactly.
- `git diff --numstat d42ffb89 a2c5caa5`: footwear entry 4/4 (exactly the four lines), SOURCES.md 2/1.
- Full SOURCES.md diff d42ffb89→a2c5caa5: exactly (a) S687 used-by cell `corpus/knowledge/culture-material/footwear-codes-terminology.md` → `—` (all other cells byte-equal), (b) one inserted row S693 at line 648. APPEND's S687 exception in code compares `text.split("|")[:-2]` and last cell — i.e. permits only the used-by cell to change, as the predicate allows.
- S693 row shape: live URL first (`https://www.dictionary.com/browse/talaria`), then capture of the same page (`web.archive.org/web/20240529024530id_/https://www.dictionary.com/browse/talaria`, capture index 1 ≤ 3, 20240529 past-dated vs 2026-10-23, url_key equal); tier `B`; status `mined`; opened `2026-10-23`; used-by the entry; quote "the wings or winged sandals on the feet of Hermes, or Mercury." names Hermes, footwear TOPIC rule satisfied (talaria in lexicon).
- No registry URL reuse: S693 keys (dictionary.com/browse/talaria) disjoint from all base-row URL keys (FRESH leg recomputed this; spot-consistent).

# 7. Counter non-vacuity (attack angle: could PASS be a rubber stamp?)

Read the full leg implementations (accept-d.py 1-396) and the control receipts:
- `telemetry/controls-rescore.txt` (revision-1 instruments, sha 0f601625/a222a156, 2026-10-23T12:04:05Z): CtlDCaptureShapes-bare-web-path and -different-page and -future-timestamp fixtures each end `ROWS FAIL ... bad=['S693:urls'] ... ACCEPT-D-62: FAIL / exit=1`; honest-positive fixtures PASS. The instrument demonstrably fails on out-of-spec rows.
- `telemetry/locate-control.txt`: the same control on a PASSES=1 mutant prints FAIL on RECOVER/EXHAUST/ABSENT/DNSFAIL with `LOCATE-CONTROL-62: FAIL / exit=1` — the locate treatment is shown able to fail.
- My rerun's LOCATE performed a live fetch of the S693 URLs (located=1), not a cached or skipped leg. ACCESS/LINT genuinely exec'd `tools/check-source-access.py` and `tools/check-cited-lines.py` (exit 0).

# Findings summary

- [SEV-BLOCKER]: none.
- [SEV-LOW]: none.
- [INFO] LOCATE `at=` timestamp differs receipt-vs-rerun (12:05Z vs 12:13Z): inherent live-clock print, not a state difference.
- [INFO] SET prints `lines=108 base=108` while `wc -l` reports 107: the entry file's last line has no trailing newline, so `read().split("\n")` yields 108 elements; base and measured are treated identically (base also 107 by `wc -l`), so no asymmetry. Not a defect.
- [INFO] `final-measures.txt` does not itself contain a locate-control section; that receipt lives in `telemetry/locate-control.txt`. Comparison in §2 uses the correct file.

# Residual risk and verification gaps

- The LOCATE leg's pass is one live observation per run; a row could be reachable now and unreachable later (the claim's own fetch_treatment accepts this risk and freezes it: "No further allowance: an unreachable row fails").
- `review_only` items in claims.json (wording carried by the page beyond shared words; new-row quote being page body, not caption; lore handoff) are explicitly out of the counter's scope and were not re-adjudicated here.
- Claim O's receipt (accept-o.py) sits in final-measures.txt and its counter hash matches the freeze, but reproducing O was not this seat's assignment; unverified here.
- jj working-copy state of the lane at review time was not inspected (bounds: no git/jj writes in the lane); all history evidence is from the sandbox clone's refs, which showed the lane's origin/main at 25b44b8 with nothing else above a2c5caa5 on any ref.
