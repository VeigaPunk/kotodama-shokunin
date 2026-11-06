# ExecGraderV10 — grader v10 (round 98, operability)

v9 sha256 (verified copy): 1021dc9db778042d8049920292d96930f31481e77bce2b36f577ea2d88b5717b (stage/ExecGraderV10/v9-base.py, rc 0 sha256sum)
v10 sha256: d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7 (lane tools/check-advance-evidence.py)

## New diagnostics (lane file line numbers at time of writing)
- `VERDICT-CTRL` raised at line 318-320 (new): refuse any category `Cc` byte inside a verdict span, naming the codepoint `U+{o:04X}` (U+007F DEL).
- `VERDICT-COMBINE` raised at line 321-323 (new): refuse any combining mark (category `M*` = Mn/Mc/Me, incl. U+20DD) in the verdict span, naming the codepoint. Also `_refuse_disguised` line 349 (m→`M*`) and line 358 (nfkd_nomark strips all `M*`).
- Heading / `TOPIC`: `HEADING-NUMBER` guard at line 759-765 (U+FF0E etc. non-ASCII numerals or full stop ending); concretely, non-ASCII numerals are stripped as list marks in `_content_toks` via `isnum` → `_nonascii_number`, so phrase-only heads (ROMAN1/SUP1/FWPER1) no longer reach the span floor and TOPIC refuses by name (`LEG FAIL TOPIC`). ROMANOK stays clean because the numeral is stripped and the retained words (`The address` etc.) still meet the anchor span.

## Measurements (all commands `rc` noted; work dirs under /fast/scratch/hyaku/kotodama-r98/ExecGraderV10, never /tmp)
- Selftest: `python3 -B .../tools/check-advance-evidence.py --selftest --work $PWD/absst` rc 0 → `SELFTEST PASS 161/161` (161 = 155 v9 pins + 6 new: DEL1, ENC1, ROMAN1, SUP1, FWPER1, ROMANOK). File: stage/ExecGraderV10/selftest.txt. NOTE: with a relative --work, both v9 and v10 show 4 environmental BADs (capture byte-copies checks); predispatch uses an absolute --work and there v9 measured PASS 155/155 rc0. With absolute --work v10 PASSes 161/161 rc0.
- Battery98: `python3 -B .../reports/round-98/controls/battery98.py --tool .../tools/check-advance-evidence.py --work $PWD/battery` rc 0 → `BATTERY-SUMMARY survivors=0 unnamed=0 refused=36 traceback=0 clean=3 not-clean=0`. G0/ZWNJ1/ROMANOK CLEAN. File: stage/ExecGraderV10/battery-v10.txt. All 34 reg-v5 REG lines byte-identical in battery output (counted with python, all 34 present).
- Critic97 replay: `CRIT_WORK=$PWD/crit CRIT_BATTERY=.../ExecBattery97/battery97.py CRIT_TOOL=.../tools/check-advance-evidence.py CRIT_OUT_JSON=$PWD/crit.json python3 -B .../CriticO97/attacks_critic97.py` rc 0 →
  - `CLASS DEL1 ... named=VERDICT-CTRL outcome=REFUSED-NAMED`
  - `CLASS ENC1 ... named=VERDICT-COMBINE outcome=REFUSED-NAMED`
  - `CLASS ROMAN1/SUP1/FWPER1 ... named=TOPIC outcome=REFUSED-NAMED`
  - `CLASS CYRH1/ZWSH1/BELH1 rc=0` (benign clean-twin controls; listed SURVIVOR by the driver)
  - `CRITIC-O97 survivors=3 unnamed=0 refused=22 traceback=0`
  File: stage/ExecGraderV10/critic97-v10.txt.
- Frozen counter (read-only predispatch, base-rev bcf664aa089ddbd1fac85772ed22a38d1b454d23): `python3 -B .../reports/round-98/predispatch.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin --work $PWD/counter --base-rev bcf664aa...` rc 1 → LEG O0 PASS, O1 PASS 161/161 rc0, O2 PASS, O3 FAIL (sha pin missing or malformed: reports/round-98/controls/mutants98.sha256 — MutationTester98 not yet landed), O4 PASS (34/34 REG), O5 PASS (tally survivors=3 unnamed=0 refused=22 traceback=0, not-refused-named=[], benign-not-rc0=[]); C legs still FAIL (entry/registry not landed by sibling seats). File: stage/ExecGraderV10/counter.txt.

## MutationTester98 dependency
Bounded wait (`for i in $(seq 1 180); do [ -f .../MutationTester98/DONE ] && break; sleep 60; done`, timeout 1200) — see mutation section below (updated when DONE lands).

## Tools installed
None. Tooling authorization read acknowledged; no installs were needed; pacman untouched.

## Attacks.md INFERENCE verification
- Verdict-window Mn-only cause for ENC1: CONFIRMED (v9 `_refuse_disguised` verdict_raw Mn check; v9 `_refuse_verdict_channel` had no M-check at all).
- `_NUM2` ASCII-only causing ROMAN1/SUP1/FWPER1: CONFIRMED (numeric regex used `\\d` and `[IVXLCDM]+` only).
- DEL1 outside the C0 set: CONFIRMED (v9 loop `if o < 0x20` excluded 0x7F).
