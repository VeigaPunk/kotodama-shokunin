# ReviewerO99 — non-author review of claim O (round 99, w1)

Seat: ReviewerO99 (attack reviewer, claim O operability). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base `527df3fee305b3454446946e6779ece45456307e` (grader v10, sha `d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7`);
freeze commit `b1b80562edfc8f6082aec74bbbf0f25e152708a8` (HEAD when the wave started). Landed v11 reviewed at working-tree
sha `717341dcff329a8c8aea9e6e807a16b70bc24818edfc31681780a24f68ee76f2` (ExecGraderV11 DONE binds this sha; three in-flight
revisions `a56965b5…` → `1759dc8b…` → `717341dc…` were observed and discarded mid-review — all measurements here are on the
final bytes). Scratch `/fast/scratch/hyaku/kotodama-r99/ReviewerO99` (removed before yield). No lane file edited; every probe
ran on scratch copies or through the frozen drivers read-only. No commit, no jj mutation, no model choice, no pacman, no
sysctl. Tools installed or updated by this seat: none.

## 1. Frozen counter, read-only (step 1)

Command: `python3 -B reports/round-99/predispatch.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin --work /fast/scratch/hyaku/kotodama-r99/ReviewerO99/counter --base-rev 527df3fee305b3454446946e6779ece45456307e`
(rc 0, wall 16m58.0s, output `counter.txt`, saved at `stage/ReviewerO99/counter.txt`):
`PREDISPATCH-99: PASS legs=16/16`.

| leg | result |
|---|---|
| O0 | PASS tool-sha256 717341dcff329a8c8aea9e6e807a16b70bc24818edfc31681780a24f68ee76f2 (must differ from v10 d35b13c9…) |
| O1 | PASS 175/175 floor=168 rc=0 |
| O2 | PASS survivors=0 unnamed=0 refused=37 traceback=0 clean=9 not-clean=0 required=0/0/37/0/9/0 rc=0 pin=receipt=driver |
| O3 | PASS 34 baseline REG lines, 34 byte-identical in battery99 output |
| O4 | PASS tally=CRITIC-O98 survivors=24 unnamed=0 refused=1 traceback=0 overrefusal=0 rc=0 clean-not-rc0=[] unexpected-clean=[] plainmove-refused=True survivor-max=24 |
| O5 | PASS tally=CRITIC-O97 survivors=3 unnamed=0 refused=22 traceback=0 rc=0 not-refused-named=[] benign-not-rc0=[] |
| O6 | PASS 136/136 killed, 0 survived, 0 broken-pattern (floor total 132) rc=0 |
| C1–C9 | all PASS (context only; not this seat's claim) |
| — | `PREDISPATCH-99: PASS legs=16/16` |

Leg-by-leg judgment (O0–O6), each checked against its claim text in `claims.json`:

- **O0 (tool sha differs from v10)** — PASS: landed tool sha256 `717341dc…` ≠ v10 `d35b13c9…` (measured, `sha256sum`).
- **O1 (selftest rc 0, N ≥ 168)** — PASS: my independent run of the landed file prints `SELFTEST PASS 175/175`, rc 0
  (161 v10 checks + 14 new round-99 pins; the v10 selftest on the same host was timed at 6.4 s).
- **O2 (battery99 0/0/37/0/9/0; driver sha == pin == receipt; receipt shows 0/0/37/3/6 over v10)** — PASS:
  `sha256sum reports/round-99/controls/battery99.py` = `87f426aa3333a573ec2fa39cdd75c554d804401ecd903573f1831aef89c7a26d` =
  pin file = receipt `BATTERY-SHA256`; receipt `TOOL-SHA256` = v10 sha and `BATTERY-SUMMARY survivors=0 unnamed=0 refused=37
  traceback=0 clean=3 not-clean=6` (the frozen CONTROL_SUMMARY). My own re-run of the pinned driver over my extracted v10
  bytes reproduced the control receipt byte-for-byte (`bat-v10.txt`, 46 classes identical), and over v11 gives
  `0/0/37/0/9/0` rc 0.
- **O3 (34 reg-v5 REG lines verbatim)** — PASS in the counter run (34/34 byte-identical); independently visible in
  `battery-v11.txt` (34 REG lines) vs `reports/round-95/controls/reg-v5.txt`.
- **O4 (critic98 replay: six clean classes rc 0, PLAINMOVE refused, OVERREFUSAL n=0, survivors ≤ 24, unnamed 0,
  traceback 0)** — PASS: counter reports `survivors=24 unnamed=0 refused=1 traceback=0 overrefusal=0` with the six
  `control-clean` classes rc 0; v10 baseline for the same pinned driver (`controls/critic98-on-v10.txt`) shows
  `OVERREFUSAL n=2` (OK-MCWORD, OK-DEVAHEAD) and 24 survivors, so both named harms are repaired and nothing new opened
  (survivor count unchanged at 24, identical id set per CriticO99's replay).
- **O5 (critic97 replay unchanged)** — PASS: `survivors=3 unnamed=0 refused=22 traceback=0`; DEL1/ENC1/ROMAN1/SUP1/FWPER1
  REFUSED-NAMED, CYRH1/ZWSH1/BELH1 rc 0.
- **O6 (mutation99 killed == total ≥ 132, 0 survived, 0 broken-pattern; driver sha == pin == first receipt)** — PASS:
  `MUTATION-SCORE: 136/136 killed, 0 survived, 0 broken-pattern` (floor 132); driver
  `.ufo/waves/round-99/w1/stage/MutationTester99/mutants99.py` sha `cf58e12632037e2d923ec0add6de431374def80d899603f8b067a91852872ffd`
  = pin `reports/round-99/controls/mutants99.sha256` = `DRIVER-SHA256` line 1 of `reports/round-99/controls/mutation99-first.txt`,
  whose line 2 binds the final tool `TOOL sha256=717341dc…`.

Do-nothing control: `predispatch-base.txt` records `PREDISPATCH-99: FAIL legs=6/16` over the base tree (O3, O5, C3, C4, C5,
C8 pass by construction; every O-leg that can fail, fails). Forgery controls (`controls/forgery/summary.txt`): F-O-SHA
(v10 + one comment line) → O0 PASS but O1/O2/O4 FAIL; F-O-LOOSE (deleting the two v10 refusal surfaces) → O2 FAIL
survivors=2 (CM1, CMW2) — deletion does not pass; P-O-FEAS (narrow to Mn/Me + disable HEADING-NUMBER) → O2 and O4 PASS,
so the target is reachable without loosening. All three committed in the freeze commit before any seat ran.

## 2. Pin binding and order (step 2)

| artifact | sha256 | pin file | receipt line | in freeze commit b1b8056? |
|---|---|---|---|---|
| `reports/round-99/controls/battery99.py` | `87f426aa3333a573ec2fa39cdd75c554d804401ecd903573f1831aef89c7a26d` | `battery99.sha256` = same | `battery99-control-v10.txt` `BATTERY-SHA256` = same | yes (`git show --stat b1b8056`); in-commit blob sha = live sha |
| `.ufo/waves/round-99/w1/stage/MutationTester99/mutants99.py` | `cf58e12632037e2d923ec0add6de431374def80d899603f8b067a91852872ffd` | `mutants99.sha256` = same | `mutation99-first.txt` `DRIVER-SHA256` = same | no (working tree; uncommitted, like v11) |
| `tools/check-advance-evidence.py` at `527df3f` | `d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7` (v10) | — | `battery99-control-v10.txt` `TOOL-SHA256` = same | yes (base blob) |
| `tools/check-advance-evidence.py` landed | `717341dcff329a8c8aea9e6e807a16b70bc24818edfc31681780a24f68ee76f2` (v11) | — | `mutation99-first.txt` line 2 = same | no (working tree) |

Order: driver mtime 01:18:50 < pin 01:19:07 < first receipt 01:37:15 (stat, full-iso). The receipt's first line is the
`DRIVER-SHA256` of the same bytes the pin names, and line 2 binds the final v11 — the mutation measurement was made against
the landed tool, not an intermediate. An earlier measurement against the superseded intermediate tool `a56965b5` is
preserved under its own honest name (`mutation99-first-superseded-tool-a56965b5.txt`, driver `8476735f…`). No commit
contains the mutation pin or first receipt (`git log -- <paths>` empty), matching the counter's design (they are read from
the working tree). The battery99 driver, its pin and its v10 receipt are all in the freeze commit (`git show --stat
b1b8056…` lists the three paths; `git show b1b8056:reports/round-99/controls/battery99.py | sha256sum` = `87f426aa…`), so
the frozen predicate predates every v11 byte.

## 3. v10 → v11 diff and shadowing (step 3)

`diff -u` v10 (2066 lines) vs v11: 4 hunks (v10 lines 346, 733, 796, 1995).

| # | branch (v10 → v11) | revert mutant | selftest | battery99 | shadowed? |
|---|---|---|---|---|---|
| B1 | `_dispo_match` Me check on group(2) (v10:349) removed as dead code (v11:351-356 comment) | M5: check restored | 175/175 unchanged | 0/0/37/0/9/0 unchanged | dead by construction: all three DISPO regexes contain zero non-ASCII bytes and group(2) is the ASCII literal `(NOT[ _-]?LOCATED|LOCATED)`, so it can never carry a combining mark; 7-shape Me probe (L⃝OCATED, NOT⃝LOCATED, ⃝LOCATED, LOCATED⃝, NOT_LOCATED⃝, LOCATED ⃝, ⃝ LOCATED) gives identical rc/outcome pairs on v10 and v11 |
| B2 | heading combining check narrowed: every category M (v10:742) → `_heading_forged_mark` anchor-invariance + phrase-equality rule (v11:806-856) | M1: v10 two-liner restored | FAIL | DEVAOK1/MCOK1/MCOK2/VISOK1 CLEAN→NOT-CLEAN | NO — pinned by 4 battery classes + selftest MCOK/VISOK/DEVAOK pins |
| B2a | sub-arm: anchor-invariance (`(head_anchors, head_span_anchors)` tuple compare) | M2: arm dropped | FAIL | CM1 REFUSED→SURVIVOR | NO — load-bearing for battery97 CM1 |
| B2b | sub-arm: script-neutral mark whose mark-stripped token equals a declared phrase | M3: arm dropped | FAIL | CMW2 REFUSED→SURVIVOR | NO — load-bearing for battery97 CMW2 |
| B3 | HEADING-NUMBER loop (v10:757-766) removed; `_nonascii_number` simplified (dead `for p in []` disjunct and arm subsumed by the non-ASCII-numeral arm removed; semantics equal) | M4: v10 expression + loop restored | FAIL | NUMOK1/NUMOK2 CLEAN→NOT-CLEAN | NO — removal pinned by the two benign twins (the round-98 mistake is not repeated) |
| B4 | selftest +14 round-99 pins (NFKDME1, MCOK1/2, VISOK1, DEVAOK1, NUMOK1/2, CM1-DEVANAGARI, MARKDASH, VIETNFD, ROMANMARK, LATMARKINDIC, CYR, FRENCH) | — | 161 → 175 | — | 161 v10 checks all still present and passing (no v10 pin weakened) |

No-weakening runs (my own, pinned drivers over landed v11):
- battery98 over v11: `BATTERY-SUMMARY survivors=0 unnamed=0 refused=36 traceback=0 clean=3 not-clean=0` rc 0
  (required 0/0/36/0/3/0) — `battery98-v11.txt`.
- battery97 over v11: `BATTERY-SUMMARY survivors=0 unnamed=0 refused=31 traceback=0 clean=2 not-clean=0` rc 0
  (required refused=31) — `battery97-v11.txt`.
- battery99 per-class diff v10-receipt vs v11 run: 46 classes; refusals lifted: NONE; new refusals: NONE; outcome
  changes exactly DEVAOK1/MCOK1/MCOK2/NUMOK1/NUMOK2/VISOK1 NOT-CLEAN→CLEAN.

## 4. Harm check (step 4)

Classes v11 accepts that v10 refused — every one is a valid-input repair, none is a forgery acceptance:

| class | evidence | classification |
|---|---|---|
| Devanagari/Oriya Mc marks (U+093E, U+0903, U+0B03) in heading words | battery99 MCOK1/MCOK2/VISOK1 NOT-CLEAN→CLEAN; critic98 OK-MCWORD rc 1→0 | valid (repair; closure F4) |
| Devanagari virama U+094D (Mn) in heading word | battery99 DEVAOK1; critic98 OK-DEVAHEAD | valid (repair; v9-era over-refusal) |
| bare non-ASCII numeral headings `## Ⅳ.`, `## 7．` | battery99 NUMOK1/NUMOK2 | valid (repair; closure F1) |
| NFD Latin orthography (Vietnamese, French), IPA, Cyrillic stress | selftest VIETNFD/FRENCH/CYR pins rc 0 on v11, refused on v10 | valid (repair; CriticO99 EARLY) |
| mark on a list dash / non-letter base where anchors are unchanged (`## 1. The addre´ss`-inert shapes) | my 48-probe matrix: 24 anchor-inert placements refused by v10, accepted by v11 (`harm-v10.txt` vs `harm-v11.txt`) | valid (v10 over-refusal) |
| real knowledge-tree headings `## Hózhǫ́, …` (dine-navajo.md:52), `## Gẹ̀lẹ̀dẹ́: …` (fon-dahomey.md:83) | exposure sweep: v10 flags 2/3010, v11 flags 0/3010 | valid (repair) |

Classes v11 refuses that v10 accepted: **none** (battery99 class diff shows no new refusal; CriticO99's 75-class delta
reports `0 classes newly refused`; my matrix's 8 v11 refusals are a subset of v10's 32). Forged inputs stay refused:
CM1 (`1́.` on numbering token — anchor-invariance arm), CMW2 (marked phrase word — phrase-equality arm), MARKDASH
(`—ा` list-mark lift, selftest pin), ROMANMARK (`Í.` roman numeral, selftest pin), CM1-DEVANAGARI (`1ा.` digit,
selftest pin), NFKDME1/ENC1 (verdict-token marks, unchanged NFKD/scan path). F-O-LOOSE's lesson holds: the protection was
re-derived, not deleted (M2/M3 mutants each reopen exactly one battery attack, so the new arms are individually
load-bearing).

## 5. Lane exposure (step 6)

Method: **predicate replication from extracted source** — the heading-check region (`def _nonascii_number` … the
HEADING-COMBINING loop) is extracted verbatim from each tool's bytes, exec'd per heading with the tool's own module
namespace; for v11 this is exactly `_heading_forged_mark` + the pre-filter (HEADING-NUMBER no longer exists). The harness
was validated against known tool outcomes: 11/11 shapes on v10 (incl. `## Ⅳ.` flagged, `## Ⅳ. Notes` not, battery99
control headings) and 18/18 shapes on v11 (incl. all six battery99 benign classes clean, CM1/CMW2/MARKDASH/ROMANMARK/
CM1-DEVANAGARI flagged, Hózhǫ́/Gẹ̀lẹ̀dẹ́ clean, NFD Vietnamese/French/Cyrillic clean, `Ⅳा.` inert-clean).

| sweep | headings | flagged |
|---|---|---|
| v10 over every `## ` in `corpus/knowledge/**/*.md` | 3010 | 2 — `civilizations/dine-navajo.md:52` (`Hózhǫ́`, U+0301 on ǫ), `civilizations/fon-dahomey.md:83` (`Gẹ̀lẹ̀dẹ́`, U+0300/U+0301) — both HEADING-COMBINING |
| v11, no declared phrases | 3010 | 0 |
| v11 with declared phrases `address;petition;efficacy` | 3010 | 0 |

The two v10-flagged headings are legitimate Navajo and Yoruba orthography that v9 also refused (Mn marks) — v11 repairs
them; entry-mode evaluation of those files is not otherwise affected (no entry under review carries them).

## 6. Verdict

**Claim O: PASS.** All legs O0–O6 PASS on one run of the frozen counter bytes over the landed lane tree with
`--base-rev 527df3fee305b3454446946e6779ece45456307e`. **First failing leg: none.** The two round-98-closure harm surfaces
(heading Mc over-refusal, HEADING-NUMBER bare-numeral refusal) are repaired with positive controls; every v10 refusal is
preserved (battery99 refused=37 identical class set, battery98 36, battery97 31, critic97 five forgeries, 34 REG lines);
no protection was deleted (F-O-LOOSE class avoided; each new arm is individually mutation-pinned, 136/136).

## Residual risk and verification gaps

1. **Orphan-mark acceptance (info).** A heading whose first token is a lone combining mark glued to content
   (`## ´1. The address`) is accepted: anchors are unchanged, so the anchor-invariance rule passes it. Cosmetically
   degraded, anchor-inert; no span or phrase lift is possible (verified in the matrix, `harm-v11.txt`).
2. **Phrase-equality arm is exact-match.** A mark-stripped token must equal a declared phrase (`addre´ss`→`address` is
   caught; `addre´sses` would not be) — but a near-miss token cannot anchor the phrase either (`norm` splits the mark),
   so no anchor is gained; the span/count legs still refuse phrase-only abuse (CM1/M2 evidence).
3. **critic98's 24 survivors remain open** (bounded by O4 at ≤ 24; identical id set on v10 and v11). Outside this claim
   by construction.
4. **Latin stacked-accent benign twins live in the selftest, not the frozen battery99** (battery99 is freeze-committed
   and cannot grow). The exposure sweep (0/3010 on v11) is the compensating measurement; a future battery would ideally
   carry VIETNFD/FRENCH/CYR as battery classes.
5. **MutationTester99's DONE landed at 01:52:23** (after my counter run started): its DONE line names driver sha
   `cf58e126…` = pin = first-receipt `DRIVER-SHA256`; `mutants99.py` bytes unchanged since 01:18:50, so the triple the
   counter's O6 read is the triple the seat shipped — no re-run required.
6. The counter does not fetch the network and does not measure claim C legs here beyond what predispatch prints; my scope
   is claim O only. Over-refusal outside battery99/critic98 benign sets is CriticO99's attack surface (their 75-class
   delta: `0 classes newly refused`, 20 of 23 v10 over-refusals repaired on the final bytes per their re-run).
