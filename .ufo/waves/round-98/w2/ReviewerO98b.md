# ReviewerO98b — non-author review of claim O (round 98, w2)

Seat: ReviewerO98b (attack reviewer, claim O). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base `bcf664aa089ddbd1fac85772ed22a38d1b454d23`; freeze `db88f107606aae90efe01344551c7e1ea71cd419` (HEAD; parent = base).
Scratch `/fast/scratch/hyaku/kotodama-r98/ReviewerO98b` (removed before yield). No lane file was edited by this
seat; every probe ran on a scratch copy. No commit, no jj mutation, no model choice.

## 1. Frozen counter, read-only (step 1)

Command (final, after the mutation pin landed): `python3 -B reports/round-98/predispatch.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin --work /fast/scratch/hyaku/kotodama-r98/ReviewerO98b/counter2 --base-rev bcf664aa089ddbd1fac85772ed22a38d1b454d23` — rc=0, wall 1016.50 s, output `counter2.txt`.

| leg | result |
|---|---|
| O0 | PASS tool-sha256 d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7 (differs from v9 1021dc9d…) |
| O1 | PASS 161/161 floor=160 rc=0 |
| O2 | PASS survivors=0 unnamed=0 refused=36 traceback=0 clean=3 not-clean=0 required=0/0/36/0/3/0 rc=0 pin=receipt=driver |
| O3 | PASS 128/128 killed, 0 survived, 0 broken-pattern (floor total 126) rc=0 |
| O4 | PASS 34 baseline REG lines, 34 byte-identical in battery98 output |
| O5 | PASS tally=CRITIC-O97 survivors=3 unnamed=0 refused=22 traceback=0 rc=0 not-refused-named=[] benign-not-rc0=[] |
| — | `PREDISPATCH-98: PASS legs=15/15` |

The first read-only run, made before the mutation pin existed, was `rc=1` with
`PREDISPATCH-98: FAIL legs=14/15`, the only failure being
`O3 FAIL sha pin missing or malformed: reports/round-98/controls/mutants98.sha256` (saved as
`counter.txt`). After `MutationTester98b` landed the pin and first receipt, the same frozen
counter bytes pass all 15 legs. C1–C9 all PASS on this run (not this seat's claim; context only).

Do-nothing control: `predispatch-base.txt` records 5/15. My independent reproduction over a
`git archive bcf664aa` tree gives 3/15 because the extracted base commit lacks the round-98
control files and `.git`: O2 fails "driver missing", O4 has no REG output, C3 has no git tree.
O4 was verified independently on v9 (battery98 over v9 emits 34/34 REG lines byte-identical to
`reports/round-95/controls/reg-v5.txt`), and C3 passes on base by construction (registry
unchanged). The legs that matter — O0/O1/O2/O3/O5 — reproduce as FAIL on base.

## 2. Pin binding and commit order (step 2)

| artifact | sha256 | pin file | receipt line |
|---|---|---|---|
| `reports/round-98/controls/battery98.py` | `cdb77c4b5092800899fec2d27b6b69b1afbcc83fd1ec022fd7d5940b3714968b` | `battery98.sha256` = same | `battery98-control-v9.txt` `BATTERY-SHA256` = same |
| `.ufo/waves/round-98/w1/stage/MutationTester98/mutants98.py` | see §2b | `mutants98.sha256` | `mutation98-first.txt` `DRIVER-SHA256` |
| `tools/check-advance-evidence.py` at `db88f107` | `1021dc9db778042d8049920292d96930f31481e77bce2b36f577ea2d88b5717b` (v9) | — | `battery98-control-v9.txt` `TOOL-SHA256` = same |
| `tools/check-advance-evidence.py` worktree (v10) | `d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7` | — | — |

Commands: `sha256sum reports/round-98/controls/battery98.py` rc 0; `sha256sum tools/check-advance-evidence.py`
rc 0; `git -C … show db88f107:tools/check-advance-evidence.py | sha256sum` rc 0; `git -C … show bcf664aa:tools/check-advance-evidence.py | sha256sum` rc 0 (same v9 sha).

Commit order (`git log --format=%H -- <path>`):

| path | commits |
|---|---|
| `reports/round-98/controls/battery98.py` | `db88f107606aae90efe01344551c7e1ea71cd419` only |
| `reports/round-98/controls/battery98.sha256` | `db88f107…` only |
| `reports/round-98/controls/battery98-control-v9.txt` | `db88f107…` only |
| `tools/check-advance-evidence.py` | last commit `fc5ba047…` (round-97); no commit contains v10 |

`git show --stat db88f107` lists battery98.py, battery98.sha256, battery98-control-v9.txt,
critic97-on-v9.txt, predispatch.py, claims.json and the forgery controls — all in the freeze
commit. HEAD is `db88f107`; its parent is `bcf664aa`. mtimes: battery98.py 22:20:52 < pin
22:21:09 < v9 receipt 22:21:09 < freeze commit 22:29:10 < v10 tool 22:42:34. v10 is an
uncommitted working-tree modification (`git status` `M tools/check-advance-evidence.py`), so
no v10 byte exists in any commit and the v9 receipt predates the v10 byte on disk.

### 2b. Mutation pin and first receipt

| artifact | sha256 | pin | first receipt |
|---|---|---|---|
| `.ufo/waves/round-98/w1/stage/MutationTester98/mutants98.py` | `dd88caec75b86b0174d63521a6796c682675cc6ba50a2233862afb04057efb0f` | `mutants98.sha256` = same | `mutation98-first.txt` `DRIVER-SHA256` = same |

Commands: `sha256sum .ufo/waves/round-98/w1/stage/MutationTester98/mutants98.py` rc 0; `cat
reports/round-98/controls/mutants98.sha256` rc 0; `cat reports/round-98/controls/mutation98-first.txt`
rc 0. mtimes: driver 23:27:24 < pin 00:09:04 < first receipt 00:26:23 — the driver bytes predate
the pin and the receipt, and no repair follows the first receipt (the driver mtime is unchanged
and the receipt's `DRIVER-SHA256` equals the pin). The first receipt is the full driver stdout:
`TOOL sha256=d35b13c9…`, `CLEAN-FIRST selftest_rc=0 SELFTEST-PASS-line=True`, 128 mutant rows and
`MUTATION-SCORE: 128/128 killed, 0 survived, 0 broken-pattern`.

Red-before control (`stage/MutationTester98b/red-before-v9.txt`): the same pinned driver over v9
gives `MUTATION-SCORE: 117/128 killed, 0 survived, 11 broken-pattern` — the 11 v10-only patterns
(`verdict-ctrl-cc-narrow`, `verdict-combine-window-off`, `nonascii-number-off`,
`fullwidth-stop-strip-off`, the four round-98 selftest fixtures, …) do not match v9, so the
driver is v10-specific and the v9 run is red as expected.

Independent mutation measurement (my own run, scratch copy):
`python3 -B .ufo/waves/round-98/w1/stage/MutationTester98/mutants98.py --tool tools/check-advance-evidence.py --work <scratch>/mutrun`
→ rc 0, `MUTATION-SCORE: 128/128 killed, 0 survived, 0 broken-pattern` (floor 126). All 128
patterns match v10 exactly (`src.count(old)` 128/128; 46 exactly-once, 82 replace-all).

## 3. v9 → v10 diff and shadowing (step 3)

`diff -u v9.py v10.py` has 6 hunks (v9 lines 315, 343, 352, 736, 755, 1944). Method: each new
refusal branch was deleted by exact string replacement (`assert src.count(old) == 1`) in a
scratch copy; the tool's own selftest (161 checks) and battery98 (39 classes) were run against
each mutant. Baseline v10: selftest PASS 161/161; battery98 0/0/36/0/3/0.

| # | branch (v10 line) | mutant | selftest | battery98 | shadowed? |
|---|---|---|---|---|---|
| B1 | `Cc` verdict control (318) | `o < 0x20` | FAIL 160/161 — BAD round-98 DEL1 | DEL1 SURVIVOR | NO |
| B2 | scan combining-mark (321) | branch removed | FAIL 160/161 — BAD round-98 ENC1 (message loses U+20DD) | unchanged (ENC1 still refused by the NFKD path) | pinned by selftest message; redundant for the battery class |
| B3 | `_dispo_match` Mn→M (349) | `== 'Mn'` | PASS 161/161 | unchanged | **YES — dead** |
| B4 | NFKD nomark Mn→M (358) | `!= 'Mn'` | PASS 161/161 | unchanged | unpinned (load-bearing, see F3) |
| B5 | heading combining Mn/Me→M (742) | `in ('Mn','Me')` | PASS 161/161 | unchanged | unpinned (load-bearing, see F4) |
| B6 | HEADING-NUMBER loop (757–766) | loop removed | PASS 161/161 | unchanged | **unpinned; false-positive surface (F1)** |
| B7 | `isnum` `_nonascii_number` (782) | extension removed | FAIL 158/161 — BAD ROMAN1/SUP1/FWPER1 | ROMAN1/SUP1/FWPER1 SURVIVOR | NO |

Reachability probes beyond the pins:
- B3: 8 Me token shapes (`LOCA⃝TED`, `L⃝OCATED`, `LOCATED⃝`, `⃝LOCATED`, `NOT⃝LOCATED`,
  `NOT_LOCATED⃝`, `LOCATED ⃝`, `⃝ LOCATED`) give identical rc/messages with B3 present and
  removed. `\b(NOT[ _-]?LOCATED|LOCATED)\b` cannot capture a token containing the mark, so the
  branch is unreachable; the scan or the NFKD path always fires first.
- B4: gained line `- S001 L⃝OCATED recheck moved …` → v10 rc 2 `VERDICT-COMBINE`; B4-removed
  rc 0 `PASS 9/9`. The branch is the only catch for a mark between L and O.
- B5: heading `## 1. address<U+093E>` (Devanagari vowel sign, Mc) → v10 `FAIL TOPIC`
  (`HEADING-COMBINING`); B5-removed `PASS 9/9`.
- B6: entry + `## Ⅳ.` → v10 `FAIL TOPIC` (`HEADING-NUMBER`); B6-removed `PASS 9/9`. Entry +
  `## Ⅳ. Ⅴ.` same. Entry + `## Ⅳ. Notes` passes on both (the branch does not fire).
  The branch fires only when every token after the first is also a non-ASCII number, i.e. the
  heading has no content word. Such a heading cannot anchor (`head_anchors` needs ≥2 raw
  tokens; `head_span_anchors` needs ≥2 content tokens), so the branch adds no protection and
  only refuses otherwise-valid entries. It is not the mechanism that closes ROMAN1/SUP1/FWPER1
  — B7 is.

## 4. No weakening (step 4)

- battery97 over v10: `survivors=0 unnamed=0 refused=31 traceback=0 clean=2 not-clean=0`; G0
  CLEAN, ZWNJ1 CLEAN (`battery97-v10.txt`, driver sha 79efb67c…).
- battery98 over v10: `0/0/36/0/3/0`; ROMANOK CLEAN, G0 CLEAN, ZWNJ1 CLEAN (`battery98-v10.txt`).
- battery98 over v9: `5/0/31/0/3/0` — reproduces `battery98-control-v9.txt` exactly.
- critic97 replay over v9: `survivors=8 unnamed=0 refused=17 traceback=0`; over v10:
  `survivors=3 unnamed=0 refused=22 traceback=0`. DEL1 `VERDICT-CTRL`, ENC1
  `VERDICT-COMBINE`, ROMAN1/SUP1/FWPER1 `FAIL TOPIC`; CYRH1/ZWSH1/BELH1 rc 0.
- REG: 34/34 baseline lines byte-identical, no extras.
- Diff review: every code hunk broadens a refusal or strips more heading tokens; no check is
  removed or relaxed. The only new behaviour with no protective value is B6 (F1).

## Findings

**F1 (medium) — HEADING-NUMBER is an unpinned false-refusal branch.** `tools/check-advance-evidence.py:757-766`.
It fires only on headings whose tokens are all non-ASCII numbers, which cannot anchor, so its
removal changes no pinned outcome (selftest 161/161; battery98 unchanged at 0/0/36/0/3/0) while
it refuses a valid entry that carries a bare numeral heading (`## Ⅳ.` → `FAIL TOPIC`
`HEADING-NUMBER`, mutant PASS 9/9). Its stated intent (“a heading that would anchor only
through it”) is not what it implements. The implementation also carries a dead clause
`any(... for p in [])` (always False) and a first `and` chain subsumed by the later
`any(ord(c) > 127 …)` clause.

**F2 (low) — `_dispo_match` Me extension is unreachable.** `tools/check-advance-evidence.py:349`.
Removal changes nothing across the selftest, battery98 and an 8-shape Me token sweep; the
`\b…\b` match cannot capture a token containing the mark, so the scan or NFKD path always
fires first. Dead code.

**F3 (low) — NFKD Me extension is load-bearing but unpinned.** `:358`. `L⃝OCATED` is refused by
v10 only because of this branch (B4-removed passes 9/9); no selftest pin or battery class uses
that shape (ENC1 is `LOCA⃝TED`, caught by the scan). A future regression could remove it
silently.

**F4 (medium) — heading Mc extension is a v9→v10 over-refusal regression.** `:742`. v9 checks
`category in ('Mn','Me')`; v10 checks `category[0] == 'M'`, adding Mc. A valid heading
`## 1. The addre<U+0903>ss address` (Devanagari visarga, Mc) is CLEAN on v9 (rc 0, `PASS 9/9`)
and refused on v10 (`FAIL TOPIC` `HEADING-COMBINING`); the B5-removed mutant passes again. Any
h2 heading carrying an Mc mark (e.g. a Devanagari/Bengali/Oriya visarga) is now refused;
CriticO98b measured U+0903 and U+0B03 independently. The comment above the check still says
“categories Mn/Me”, so the code and its documentation disagree. No selftest pin or battery class
exercises Mc; the branch is load-bearing but unpinned.

**F5 (info) — “by name” for ROMAN1/SUP1/FWPER1 is the generic TOPIC leg.** The critic driver's
`FAIL_RE` matches `FAIL TOPIC`; there is no dedicated diagnostic on those three. This is
consistent with the frozen claim's operational definition (O5) and with battery98's token list
(`LEG FAIL TOPIC`), but the named channel is weaker than DEL1/ENC1's codepoint-bearing
`VERDICT-*` messages.

## Honest saturation

The claim does not assert that v10 is unbreakable. CriticO98b's 25 fresh classes leave 24
survivors on v10 (and the same 24 on v9), all outside battery98's coverage; they do not touch the
five claim-O classes or any O0–O5 leg. The claim's "after" is a bounded successor move over the
five named CriticO97 forgeries, and that is what it measures. No saturation claim is made or
implied.

## Verdict

**Claim O: PASS.** The frozen predicate ("Claim O holds iff legs O0–O5 PASS") is satisfied on one
run of the frozen counter bytes over the landed tree with `--base-rev bcf664aa…`:
`PREDISPATCH-98: PASS legs=15/15`, rc 0. **First failing leg: none.** The only interim failure was
O3 before `MutationTester98b` landed `mutants98.sha256` and `mutation98-first.txt`; both now bind
`dd88caec…`, the same bytes as the driver, and O3 re-measures 128/128 killed, 0 survived,
0 broken-pattern.

Findings F1–F5 are defects outside the frozen predicate: F1 and F4 are new v9→v10 refusal
surfaces (F4 is a measured regression on a valid Mc-marked heading), F2 is dead code, F3 is an
unpinned load-bearing branch, F5 is a naming-strength note. None changes an O0–O5 outcome; they
are routed to round 99, not used to re-target this claim.
