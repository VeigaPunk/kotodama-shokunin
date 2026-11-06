# ExecGraderV11 — grader v11 (claim O harm repair), round 99 w1

Seat: ExecGraderV11 (leaf; sole writer of `tools/check-advance-evidence.py`). Lane
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`. No commit, no jj mutation, no model choice, no
pacman, no sysctl, no fleet-repo write. Scratch `/fast/scratch/hyaku/kotodama-r99/ExecGraderV11`
(removed before yield). Stage `.ufo/waves/round-99/w1/stage/ExecGraderV11/`.

## 1. Bytes

| file | sha256 | how measured |
|---|---|---|
| v10 base `stage/ExecGraderV11/v10-base.py` | `d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7` | `sha256sum` rc 0 (matches the frozen v10 sha) |
| **v11 lane** `tools/check-advance-evidence.py` | **`717341dcff329a8c8aea9e6e807a16b70bc24818edfc31681780a24f68ee76f2`** | `sha256sum` rc 0; `V11-READY` carries the same line |

Two interim v11 byte sets were superseded before landing: `a56965b5…` (first helper) and
`73b0355c…` (second helper). CriticO99's `EARLY.md` proved a reopened forgery and two
over-refusals in the first; probing their suggested fix found a third load-bearing reopen
(`## I<U+0301>. address`) in the second. Only `717341dc…` is measured below and named in
`V11-READY`. `a56965b5…` and `73b0355c…` must not be measured.

## 2. What each repaired branch now implements

| # | finding | line | rule the code implements |
|---|---|---|---|
| F4 | heading mark over-refusal (Mc) | 806-848, 850-856 | `_heading_forged_mark(h)` (nested in the entry TOPIC leg): a combining mark must not change what the heading anchors. `plain` is the heading with every mark removed (NFKD, then category M); when `(head_anchors, head_span_anchors)` differ between `h` and `plain` (line 831) the marks are load-bearing and the heading is refused. That is the whole forgery family: a mark on a numbering token stops it being a list number (CM1 `## 1<U+0301>. address`, and the roman-numeral shape `## I<U+0301>. address`), a mark on a list dash or a lone mark token turns a list mark into a content token (CriticO99 `## 1. address —<U+093E>`). A script-neutral mark (name `COMBINING …`, line 836) is additionally refused when the mark-free token is exactly a declared phrase (line 846) — CMW2 `## addre<U+0301>ss address`. Marks that change no anchor are orthography and stay clean |
| F1 | HEADING-NUMBER false refusal | 757-770 | the v10 loop is removed; `_nonascii_number` keeps two arms — a non-ASCII numeral anywhere in the token, or a trailing non-ASCII full stop with a numeral — which is exactly the v10 truth table (its first arm was subsumed by the non-ASCII-numeral arm; the `any(... for p in [])` disjunct was always False). `_content_toks` still strips the token, so ROMAN1/SUP1/FWPER1 fail the span leg |
| F2 | dead `_dispo_match` Me extension | 349-357 | the v10 `category(c)[0] == 'M'` check inside the `if m:` block is removed: `DISPO_RE`/`DISPO_ANY_RE` reach the verdict through the literal alternatives `NOT[ _-]?LOCATED\|LOCATED`, so `group(2)` is always one of four ASCII spellings and can carry no mark; the mark channel is the raw-line scan and the NFKD recovery. The Cf check is kept |
| F3 | unpinned NFKD Me branch | unchanged | kept load-bearing; pinned by the new `round-99 NFKDME1` selftest pin and battery99 NFKDME1 |

CriticO99 EARLY repairs, same helper: the `—<U+093E>` forgery is refused by the anchor-diff arm
(831); NFD Latin, IPA, Cyrillic stress and NFD French are accepted because they change no anchor;
`## I<U+0301>. address` is refused by the same arm.

## 3. Measurements (all rc recorded)

| check | command | result | rc |
|---|---|---|---|
| selftest | `python3 -B tools/check-advance-evidence.py --selftest --work <scratch>/st` | `SELFTEST PASS 175/175` (v10 161 + 14 round-99 pins) | 0 |
| battery99 | `python3 -B reports/round-99/controls/battery99.py --tool <lane>/tools/check-advance-evidence.py --work <scratch>/battery` | `BATTERY-SUMMARY survivors=0 unnamed=0 refused=37 traceback=0 clean=9 not-clean=0` | 0 |
| REG | `grep '^REG ' battery-v11.txt` vs `reports/round-95/controls/reg-v5.txt` | 34 lines, `diff` empty | 0 |
| critic98 | `CRIT_WORK=… CRIT_BATTERY=…/battery98.py CRIT_TOOL=…/check-advance-evidence.py CRIT_OUT_JSON=… python3 -B .ufo/waves/round-98/w2/stage/CriticO98b/attacks_critic98.py` | `CRITIC-O98 survivors=24 unnamed=0 refused=1 traceback=0`, `OVERREFUSAL n=0 ids=none`, PLAINMOVE `REFUSED-CONTROL` | 0 |
| critic97 | same shape with `.ufo/waves/round-97/w1/stage/ExecBattery97/battery97.py` and `…/CriticO97/attacks_critic97.py` | `CRITIC-O97 survivors=3 unnamed=0 refused=22 traceback=0`; DEL1 `VERDICT-CTRL`, ENC1 `VERDICT-COMBINE`, ROMAN1/SUP1/FWPER1 `FAIL TOPIC`, all `REFUSED-NAMED`; CYRH1/ZWSH1/BELH1 rc 0 | 0 |
| critic99 (not a frozen leg) | `…/CriticO99/attacks_critic99.py` with battery99 | `CRITIC-O99 survivors=32 unnamed=0 refused=15 traceback=0 overrefusal=0`; `BENIGN n=28 clean=28 overrefusal=0`; `PROBE n=2 clean=2`; `OVERREFUSAL n=0 ids=none` | 0 |
| counter | `python3 -B reports/round-99/predispatch.py --root <lane> --work <scratch>/counter --base-rev 527df3fe…` | `PREDISPATCH-99: PASS legs=16/16`; O0-O6 PASS (O6 `136/136 killed, 0 survived, 0 broken-pattern` floor 132), C1-C9 PASS (the coverage seat landed during this seat's work) | 0 |
| mutation | `python3 -B …/MutationTester99/mutants99.py --tool <lane>/tools/check-advance-evidence.py --work <scratch>/mut` | `MUTATION-SCORE: 136/136 killed, 0 survived, 0 broken-pattern` | 0 |

v10 baselines for the same commands (frozen receipts): battery99 over v10 `0/0/37/0/3/6`
(`battery99-control-v10.txt`), critic98 over v10 `OVERREFUSAL n=2`
(`critic98-on-v10.txt`). v11 closes both without losing a refusal: refused stays 37, critic98
survivors stay 24, critic97 is unchanged.

## 4. Revert-shows-red (scratch copies, never the lane file)

Each copy is the v11 bytes with one branch reverted; `--selftest --work <scratch>/st-<arm>`.

| arm | patch | rc | failing lines |
|---|---|---|---|
| Mc (v10 behaviour) | the helper call replaced by v10's unconditional `problems.append('h2 heading carries a combining mark (HEADING-COMBINING)')` | 1 | `SELFTEST FAIL 167/175`; `BAD round-99 MCOK1 … rc=1`, `MCOK2`, `VISOK1`, `DEVAOK1`, `VIETNFD`, `LATMARKINDIC`, `CYR`, `FRENCH` all rc=1 |
| HEADING-NUMBER | the v10 loop re-inserted after `_nonascii_number` | 1 | `SELFTEST FAIL 173/175`; `BAD round-99 NUMOK1: a bare roman-numeral h2 section heading stays clean: rc=1`, `BAD round-99 NUMOK2 … rc=1` |
| anchor-diff arm | `if (head_anchors(h), head_span_anchors(h)) != (…)` → `if False:` | 1 | `SELFTEST FAIL 171/175`; `BAD round-97 CM1 … rc=0`, `BAD round-99 CM1-DEVANAGARI … rc=0`, `BAD round-99 MARKDASH … rc=0`, `BAD round-99 ROMANMARK … rc=0` |
| phrase arm | `if any(norm(p) == norm(bare) for p in phrases):` → `if False:` | 1 | `SELFTEST FAIL 174/175`; `BAD round-97 CMW2: combining mark inside a heading phrase word refused: rc=1` |

## 5. New selftest pins (14; 161 → 175)

`NFKDME1` refused (`VERDICT-COMBINE`); `MCOK1`, `MCOK2`, `VISOK1`, `DEVAOK1` clean; `NUMOK1`,
`NUMOK2` clean; `CM1-DEVANAGARI` (mark on the numbering digit) refused; `MARKDASH` (mark glued to
a list dash) refused; `VIETNFD` (NFD Latin) clean; `ROMANMARK` (mark on a roman-numeral token)
refused; `LATMARKINDIC` (mark that changes no anchor) clean; `CYR` (Cyrillic stress) clean;
`FRENCH` (NFD French, whole-token phrase test) clean.

## 6. Mutation

Driver `.ufo/waves/round-99/w1/stage/MutationTester99/mutants99.py` (not mine; never edited),
sha256 `cf58e12632037e2d923ec0add6de431374def80d899603f8b067a91852872ffd`, pin
`reports/round-99/controls/mutants99.sha256` = same, first receipt
`reports/round-99/controls/mutation99-first.txt` `DRIVER-SHA256` = same and `TOOL sha256
717341dc…`. Census against the final bytes: 136 mutants, 136 patterns match exactly, 0 broken.
My run: `python3 -B …/mutants99.py --tool <lane>/tools/check-advance-evidence.py --work
<scratch>/mut` → rc 0, `MUTATION-SCORE: 136/136 killed, 0 survived, 0 broken-pattern`
(`mutation-after-repair.txt`, 136 mutant rows, no SURVIVED/BROKEN line). MutationTester99's own
first measurement reports the same score on the same tool sha. Two earlier interim runs (135
mutants, 4 broken patterns) were against the superseded helpers and are not evidence.

## 7. Not closed (honest residuals)

- `A-DEVLETTERDIGIT` (`## 1र. address`) and `A-ZWJDIGIT` (`## 1<U+200D>. address`) survive v11
  and survive v10; widening `_nonascii_number` beyond the frozen tokens was not authorised here.
- `A-LATMARKINDIC`, `A-DEVLETTERMARK`, `A-MARKTOK-NUM`, `A-MARKTOK-FIRST`, `A-SUFFIX-MC`,
  `A-SUFFIX-VIS` survive, but in each the mark changes no anchor: the mark-deleted twin also
  passes (measured rc 0 for both twins of all six). They are padding shapes, not mark-enabled
  forgeries; refusing them needs a span-rule change (route to round 100).
- `A-MCWORD-NOTWIN` is mis-labelled in the critic99 driver: battery99's `_heads97` appends the
  clean phrase word, so the fixture does contain a clean twin; it passes on v10 too.
- A neutral mark that changes no anchor is accepted on any base, including a cross-script one
  (`## address र<U+0301>`). That is the deliberate trade that buys Cyrillic stress and NFD
  French; it is not load-bearing (the heading anchors without the mark too).

## 8. Final state

Counter over the landed tree: `PREDISPATCH-99: PASS legs=16/16`, rc 0 (`counter.txt`). Every O
leg and every C leg passes; O6 binds the pinned driver `cf58e126…` and measures `136/136 killed,
0 survived, 0 broken-pattern`.

Files written: `tools/check-advance-evidence.py` (v11, `717341dc…`), stage `v10-base.py`,
`V11-READY`, `selftest.txt`, `battery-v11.txt`, `critic98-v11.txt`, `critic97-v11.txt`,
`critic99-v11.txt`, `counter.txt`, `mutation-after-repair.txt`, `DONE`. No other lane file
touched; `git status` shows `M tools/check-advance-evidence.py` (mine) plus other seats' files.
Nothing committed by this seat. No tool was installed or upgraded (none needed).
