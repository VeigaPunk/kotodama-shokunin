# CtlOParsing — round 61, wave 1: claim O parser-gap controls

Seat `KotodamaR61.CtlOParsing` (leaf). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
branch `main`, revision `78ad4b176695e9fcd490ab607cb8218e2ce62738`. Claims read from
`reports/round-61/claims.json` before any fixture existed.

- Counter under test: `reports/round-61/accept-o.py`, sha256
  `1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd` (matches the brief).
- `reports/round-61/accept-c.py` is `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`;
  not run here — this seat's item is O only.
- Sandbox: `git clone -q <lane> /fast/scratch/hyaku/kotodama-r61/CtlOParsing/clone` then
  `git checkout -q 78ad4b176695e9fcd490ab607cb8218e2ce62738`; `git rev-parse HEAD` =
  `78ad4b176695e9fcd490ab607cb8218e2ce62738`. `git cat-file -e 942abdf4…` succeeds, so the
  REAL leg's `git archive` of the round base works. `GIT_DIR`/`GIT_WORK_TREE`/`GIT_INDEX_FILE`
  were not set.
- Fake tools were installed **only** at `clone/tools/check-cited-lines.py`. The lane tree has no
  `tools/check-cited-lines.py` (checked: `LANE_NO_TOOL`); nothing was written in the lane except
  this report. No git/jj write command was run in the lane or the fleet repo. No tool was
  installed or upgraded (nothing needed).

## Probe

`accept-o.py` exposes no `FLOOR`/`TOTAL`/base-list constant to move — `grep -nE 'FLOOR|TOTAL'
reports/round-61/accept-o.py` prints nothing. Every receipt below therefore carries
`probe=n/a`; there is no probe variant to score and none was invented.

## Fixtures (all under `/fast/scratch/hyaku/kotodama-r61/CtlOParsing/`)

Built from one template by `build_fakes.py` (sha256
`358f57196b07a7aa5795432608704caf50c3ca701bb2b6681c7cfd2296bb3240`). Each fixture is a
plausible but wrong clause-scoping lint: it parses paths, walks `.md`, sorts distinct ids,
prints the contract's `MULTI-ID`/`TABLE-ID`/summary lines, honours the exit-code contract, and
passes its own 17-check selftest (`selftest 17/17`, exit 0) plus INDEP. Only the gapped parser
detail differs. Selftest cases deliberately avoid the gap (as a real bad lint's tests would).

| case | fixture (`fakes/<case>/check-cited-lines.py`) | sha256 | gap |
|---|---|---|---|
| a-3digit | `fakes/a-3digit/check-cited-lines.py` | `4bc994438bfa7514701621474dab5b277a72ac623ddecdc1849c72ddee1e5c4e` | ids matched as `\bS\d{3}\b` (exactly 3 digits) |
| b-range | `fakes/b-range/check-cited-lines.py` | `4ded88e16a5ace571c181a17265e31582121eac2c7c60671f1148f7f7b5d9e70` | `S123–S456` / `S123-S456` treated as a range, neither id counted |
| c-separator | `fakes/c-separator/check-cited-lines.py` | `8389f3ffb6a3abf87ed1413e9d13416ecd30ef6575d758037ff931bd22a892f1` | only comma-adjacent runs yield several ids; `;`, ` and `, `/`, `–`, `-`, `)(`, space yield one |
| d-table | `fakes/d-table/check-cited-lines.py` | `f585aebafe32dd7dc1980bb1a8c35710b273a466e7497c0fe918a941197e8c65` | table rows skipped entirely (no `MULTI-ID`, no `TABLE-ID`) |
| e-indent | `fakes/e-indent/check-cited-lines.py` | `b9875076a10823b61ab3605720dbff54f1c9d2222c0dc32a0f96c7b07e9308b7` | table row recognised only when `|` is at column 0 (no `lstrip`) |
| f-duplicate | `fakes/f-duplicate/check-cited-lines.py` | `f0c1afbcfc2e09411ad469c00e0f76fa6b8dd942b3731a83b8d7250c37ed1c74` | occurrences counted, not distinct ids (a repeated single id flagged) |
| g-lookalike | `fakes/g-lookalike/check-cited-lines.py` | `c048660c4cfcb179c4b05fc840f8bd1ca79b421a5e6031587e5f4d3b82c274c9` | `re.compile(r"S\d{3,}")` — no word boundaries; `XS612`, `S612x`, `S612_` counted |
| honest (diagnostic, not a control) | `fakes/honest/check-cited-lines.py` | `0ff4eba5983b938866fb3faf8c84c172e0d28dd227526ab705ca2ef6a90f5d59` | contract parser `\bS\d{3,}\b`; shows the harness can pass |

Method per case: copy the fixture to `clone/tools/check-cited-lines.py`, then run
`cd clone && timeout 900 python3 -B reports/round-61/accept-o.py`; capture full stdout and the
exit code. The counter seeds its GEN fixture from `os.urandom(16)` every run, so every run is a
fresh random tree. Required sample: 5 runs per fake. Because b-range and e-indent depend on
random-separator / random-indent draws, and g-lookalike *passed*, each of those three was run
20 times.

## Receipts

All runs below terminated well inside the 900 s cap (whole batch of 86 runs ≈ 27 s wall). Exit
codes are the counter's, appended by the harness as `exit=`.

```
RECEIPT CtlOParsing/do-nothing counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=TOOL,INDEP,GEN,CLEAN,ERR,REAL
RECEIPT CtlOParsing/a-3digit counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN
RECEIPT CtlOParsing/b-range counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN,REAL
RECEIPT CtlOParsing/c-separator counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN,REAL
RECEIPT CtlOParsing/d-table counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN,REAL
RECEIPT CtlOParsing/e-indent counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN
RECEIPT CtlOParsing/f-duplicate counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=GEN,CLEAN,REAL
RECEIPT CtlOParsing/g-lookalike counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=none
RECEIPT CtlOParsing/honest counter-sha256=1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=none
```

Sample sizes behind those lines: a-3digit 5 runs, b-range 20, c-separator 5, d-table 5,
e-indent 20, f-duplicate 5, g-lookalike 20, honest 5, do-nothing 1. Every case's failing-leg
set was identical in every run (verified with
`grep -E '^(TOOL|INDEP|GEN|CLEAN|ERR|REAL) FAIL'` over `logs/*.txt`).

## Verdicts (one per control item)

```
VERDICT (0) do-nothing (no tool):        NONE-MET — frozen FAIL, all six legs (logs/do-nothing.run1.txt)
VERDICT (a) ids as S\d{3} only:          NONE-MET — fixture fakes/a-3digit, frozen FAIL 5/5 (GEN: 85-96 missing findings)
VERDICT (b) ranges S12–S15 not counted:  NONE-MET — fixture fakes/b-range, frozen FAIL 20/20 (GEN missing 2-11; REAL missing the 6 dash-pair lines of the base corpus)
VERDICT (c) separators other than comma: NONE-MET — fixture fakes/c-separator, frozen FAIL 5/5 (GEN missing 49-79, extra 16-25; REAL 335 vs 603)
VERDICT (d) table rows ignored:          NONE-MET — fixture fakes/d-table, frozen FAIL 5/5 (GEN missing 64-69; REAL 170 vs 603)
VERDICT (e) indented table rows:         NONE-MET — fixture fakes/e-indent, frozen FAIL 20/20 (GEN missing 7-16)
VERDICT (f) duplicate ids counted twice: NONE-MET — fixture fakes/f-duplicate, frozen FAIL 5/5 (GEN extra 18-27; CLEAN FAIL; REAL extra 65)
VERDICT (g) lookalikes counted:          CONTROL-MET — fixture fakes/g-lookalike/check-cited-lines.py passes the frozen counter 20/20 (exit 0, every leg PASS)
```

## The one met control — why GEN, CLEAN and REAL are blind to it

`fakes/g-lookalike` is identical to the contract parser except that its S-id regex has no word
boundaries (`re.compile(r"S\d{3,}")` instead of `re.compile(r"\bS\d{3,}\b")`). It therefore
counts `XS612`, `S612x`, `S612_` as `S612`, and would report a `MULTI-ID` finding on a line that
merely mentions different ids in such forms.

That the parser is genuinely wrong is shown by a differential probe
(`probe/lookalike.md`, sha256 `07c30d310ae3e5696e3c460d1d06cc198406ffcc2ebd19c52f4b3129925be189`,
four lines `- note XS612 and S613 here`, `- note S612x and S613 here`, `- note S612_ and S613 here`,
`- note s612 and S613 here`):

```
--- honest on probe
CITED-LINES: 0 finding(s) in 1 file(s)
exit=0
--- g-lookalike on probe
MULTI-ID probe/lookalike.md:1 S612,S613
MULTI-ID probe/lookalike.md:2 S612,S613
MULTI-ID probe/lookalike.md:3 S612,S613
CITED-LINES: 3 finding(s) in 1 file(s)
exit=1
```

The frozen counter never builds such a line. In `reports/round-61/accept-o.py`:

- line 110-112: the `lookalike` branch is
  `s = sid(rng); return f"- {filler} X{s} {s}x S{rng.randint(1, 99)} {s}_ {s.lower()}"`.
  All lookalike occurrences of the id reuse the **same** `s`, so a no-boundary regex still sees
  exactly one distinct id on the line — never two. The one independent id there,
  `S{randint(1, 99)}`, is 1-2 digits and cannot match `\d{3,}`.
- line 128: `kinds = ["plain", "single", "repeat", "lookalike", "multi", "table1", "tablen", "tableplain"]`;
  `write_tree` emits `kinds * 3` per file for four `.md` files (lines 127-135), but "lookalike"
  rows are never combined with a second real id.
- the `repeat` branch (line 108-109) likewise repeats one id, and `single`/`table1` carry one id.

So GEN, CLEAN and REAL are all structurally unable to distinguish boundary-aware from
boundary-blind matching: 20/20 runs pass with identical finding counts on the base corpus
(603/603) and on random fixtures. This is not a flake — it is a generator blind spot. A lint
that reads `XS612`/`S612x` as citations will be accepted by the frozen `ACCEPT-O-61` predicate.

## Flakiness

No flaky leg was observed. GEN's verdict was constant for every fixture across every run:

- b-range (the case whose fixture needs a dash-separated multi line): 20/20 GEN FAIL, missing
  2-11 findings — `write_tree` repeats each kind 3× per file for 4 files, i.e. ~12 guaranteed
  dash-draws from an 8-way separator choice plus extras, so the distinguishing line is
  effectively certain. The earlier worry that a run could draw no dash separator is not
  realised (worst observed gap: 2 missing, run 19).
- e-indent (needs an indented `table1` row): 20/20 GEN FAIL, missing 7-16 — `table1` rows are
  50% indented and there are ~12 per run.
- g-lookalike: 20/20 frozen PASS — see above; the blind spot is deterministic, not luck.

## Full run logs (verbatim, every run, stdout + exit)

```
@@@ logs/do-nothing.run1.txt
TOOL FAIL exists=False exit=None last=''
INDEP FAIL exists=False
GEN FAIL exit=2 want=71 got=0 missing=71 extra=0 unparsed=0 files=4 summary=None
CLEAN FAIL exit=2 findings=0 summary=None
ERR FAIL missing_exit=2 badutf8_exit=2
REAL FAIL exit=2 want=603 got=0 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 16, 'S395,S397'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

```
@@@ logs/a-3digit.run1.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=90 got=7 missing=85 extra=2 unparsed=0 files=4 summary=CITED-LINES: 7 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/a-3digit.run2.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=97 got=7 missing=96 extra=6 unparsed=0 files=4 summary=CITED-LINES: 7 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/a-3digit.run3.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=73 got=4 missing=70 extra=1 unparsed=0 files=4 summary=CITED-LINES: 4 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/a-3digit.run4.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=98 got=10 missing=95 extra=7 unparsed=0 files=4 summary=CITED-LINES: 10 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/a-3digit.run5.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=97 got=8 missing=93 extra=4 unparsed=0 files=4 summary=CITED-LINES: 8 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

```
@@@ logs/b-range.run1.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=75 got=71 missing=4 extra=0 unparsed=0 files=4 summary=CITED-LINES: 71 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run2.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=88 got=80 missing=8 extra=0 unparsed=0 files=4 summary=CITED-LINES: 80 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run3.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=88 got=78 missing=10 extra=0 unparsed=0 files=4 summary=CITED-LINES: 78 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run4.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=94 got=89 missing=5 extra=0 unparsed=0 files=4 summary=CITED-LINES: 89 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run5.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=83 got=76 missing=7 extra=0 unparsed=0 files=4 summary=CITED-LINES: 76 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run6.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=93 got=89 missing=4 extra=0 unparsed=0 files=4 summary=CITED-LINES: 89 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run7.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=85 got=81 missing=4 extra=0 unparsed=0 files=4 summary=CITED-LINES: 81 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run8.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=97 got=90 missing=7 extra=0 unparsed=0 files=4 summary=CITED-LINES: 90 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run9.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=89 got=85 missing=4 extra=0 unparsed=0 files=4 summary=CITED-LINES: 85 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run10.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=101 got=92 missing=9 extra=0 unparsed=0 files=4 summary=CITED-LINES: 92 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run11.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=84 got=73 missing=11 extra=0 unparsed=0 files=4 summary=CITED-LINES: 73 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run12.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=89 got=86 missing=3 extra=0 unparsed=0 files=4 summary=CITED-LINES: 86 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run13.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=91 got=86 missing=5 extra=0 unparsed=0 files=4 summary=CITED-LINES: 86 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run14.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=91 got=88 missing=3 extra=0 unparsed=0 files=4 summary=CITED-LINES: 88 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run15.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=85 got=77 missing=8 extra=0 unparsed=0 files=4 summary=CITED-LINES: 77 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run16.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=92 got=87 missing=5 extra=0 unparsed=0 files=4 summary=CITED-LINES: 87 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run17.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=90 got=84 missing=6 extra=0 unparsed=0 files=4 summary=CITED-LINES: 84 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run18.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=94 got=86 missing=8 extra=0 unparsed=0 files=4 summary=CITED-LINES: 86 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run19.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=95 got=93 missing=2 extra=0 unparsed=0 files=4 summary=CITED-LINES: 93 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/b-range.run20.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=97 got=92 missing=5 extra=0 unparsed=0 files=4 summary=CITED-LINES: 92 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=597 missing=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 9, 'S048,S069'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190,S238'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189,S238')] extra=[('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 7, 'S187,S188,S189,S190'), ('MULTI-ID', 'corpus/knowledge/linguistics/gesture-co-speech-pointing.md', 9, 'S187,S188,S189')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

```
@@@ logs/c-separator.run1.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=93 got=51 missing=64 extra=22 unparsed=0 files=4 summary=CITED-LINES: 51 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=335 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 16, 'S395,S397'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382')] extra=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 210, 'S053,S055'), ('MULTI-ID', 'corpus/knowledge/linguistics/sign-languages-manual-modality.md', 11, 'S077,S120'), ('MULTI-ID', 'corpus/knowledge/linguistics/sign-languages-manual-modality.md', 26, 'S074,S082')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/c-separator.run2.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=103 got=49 missing=79 extra=25 unparsed=0 files=4 summary=CITED-LINES: 49 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=335 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 16, 'S395,S397'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382')] extra=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 210, 'S053,S055'), ('MULTI-ID', 'corpus/knowledge/linguistics/sign-languages-manual-modality.md', 11, 'S077,S120'), ('MULTI-ID', 'corpus/knowledge/linguistics/sign-languages-manual-modality.md', 26, 'S074,S082')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/c-separator.run3.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=84 got=44 missing=61 extra=21 unparsed=0 files=4 summary=CITED-LINES: 44 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=335 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 16, 'S395,S397'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382')] extra=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 210, 'S053,S055'), ('MULTI-ID', 'corpus/knowledge/linguistics/sign-languages-manual-modality.md', 11, 'S077,S120'), ('MULTI-ID', 'corpus/knowledge/linguistics/sign-languages-manual-modality.md', 26, 'S074,S082')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/c-separator.run4.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=82 got=44 missing=57 extra=19 unparsed=0 files=4 summary=CITED-LINES: 44 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=335 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 16, 'S395,S397'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382')] extra=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 210, 'S053,S055'), ('MULTI-ID', 'corpus/knowledge/linguistics/sign-languages-manual-modality.md', 11, 'S077,S120'), ('MULTI-ID', 'corpus/knowledge/linguistics/sign-languages-manual-modality.md', 26, 'S074,S082')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/c-separator.run5.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=67 got=34 missing=49 extra=16 unparsed=0 files=4 summary=CITED-LINES: 34 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=335 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 16, 'S395,S397'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382')] extra=[('MULTI-ID', 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md', 210, 'S053,S055'), ('MULTI-ID', 'corpus/knowledge/linguistics/sign-languages-manual-modality.md', 11, 'S077,S120'), ('MULTI-ID', 'corpus/knowledge/linguistics/sign-languages-manual-modality.md', 26, 'S074,S082')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

```
@@@ logs/d-table.run1.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=87 got=23 missing=64 extra=0 unparsed=0 files=4 summary=CITED-LINES: 23 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=170 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 109, 'S372,S373,S412')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/d-table.run2.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=87 got=23 missing=64 extra=0 unparsed=0 files=4 summary=CITED-LINES: 23 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=170 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 109, 'S372,S373,S412')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/d-table.run3.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=91 got=23 missing=68 extra=0 unparsed=0 files=4 summary=CITED-LINES: 23 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=170 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 109, 'S372,S373,S412')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/d-table.run4.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=97 got=28 missing=69 extra=0 unparsed=0 files=4 summary=CITED-LINES: 28 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=170 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 109, 'S372,S373,S412')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/d-table.run5.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=86 got=20 missing=66 extra=0 unparsed=0 files=4 summary=CITED-LINES: 20 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=170 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 44, 'S374,S375'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 109, 'S372,S373,S412')] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

```
@@@ logs/e-indent.run1.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=83 got=75 missing=8 extra=0 unparsed=0 files=4 summary=CITED-LINES: 75 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run2.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=101 got=87 missing=14 extra=0 unparsed=0 files=4 summary=CITED-LINES: 87 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run3.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=86 got=75 missing=11 extra=0 unparsed=0 files=4 summary=CITED-LINES: 75 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run4.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=94 got=83 missing=11 extra=0 unparsed=0 files=4 summary=CITED-LINES: 83 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run5.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=97 got=85 missing=12 extra=0 unparsed=0 files=4 summary=CITED-LINES: 85 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run6.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=82 got=71 missing=11 extra=0 unparsed=0 files=4 summary=CITED-LINES: 71 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run7.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=92 got=79 missing=13 extra=0 unparsed=0 files=4 summary=CITED-LINES: 79 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run8.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=87 got=72 missing=15 extra=0 unparsed=0 files=4 summary=CITED-LINES: 72 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run9.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=79 got=64 missing=15 extra=0 unparsed=0 files=4 summary=CITED-LINES: 64 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run10.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=82 got=71 missing=11 extra=0 unparsed=0 files=4 summary=CITED-LINES: 71 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run11.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=81 got=71 missing=10 extra=0 unparsed=0 files=4 summary=CITED-LINES: 71 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run12.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=90 got=76 missing=14 extra=0 unparsed=0 files=4 summary=CITED-LINES: 76 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run13.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=86 got=72 missing=14 extra=0 unparsed=0 files=4 summary=CITED-LINES: 72 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run14.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=81 got=74 missing=7 extra=0 unparsed=0 files=4 summary=CITED-LINES: 74 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run15.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=85 got=77 missing=8 extra=0 unparsed=0 files=4 summary=CITED-LINES: 77 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run16.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=85 got=69 missing=16 extra=0 unparsed=0 files=4 summary=CITED-LINES: 69 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run17.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=76 got=65 missing=11 extra=0 unparsed=0 files=4 summary=CITED-LINES: 65 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run18.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=79 got=65 missing=14 extra=0 unparsed=0 files=4 summary=CITED-LINES: 65 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run19.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=92 got=80 missing=12 extra=0 unparsed=0 files=4 summary=CITED-LINES: 80 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/e-indent.run20.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=90 got=77 missing=13 extra=0 unparsed=0 files=4 summary=CITED-LINES: 77 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

```
@@@ logs/f-duplicate.run1.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=88 got=111 missing=0 extra=23 unparsed=0 files=4 summary=CITED-LINES: 111 finding(s) in 4 file(s)
CLEAN FAIL exit=1 findings=13 summary=CITED-LINES: 13 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=668 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 52, 'S378,S379'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 55, 'S374,S375')] extra=[('MULTI-ID', 'corpus/knowledge/civilizations/australia-aboriginal.md', 160, 'S0047404500007600,S0047404500007600'), ('MULTI-ID', 'corpus/knowledge/civilizations/chimu.md', 22, 'S0718,S0718'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 43, 'S404,S404')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/f-duplicate.run2.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=96 got=123 missing=0 extra=27 unparsed=0 files=4 summary=CITED-LINES: 123 finding(s) in 4 file(s)
CLEAN FAIL exit=1 findings=15 summary=CITED-LINES: 15 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=668 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 52, 'S378,S379'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 55, 'S374,S375')] extra=[('MULTI-ID', 'corpus/knowledge/civilizations/australia-aboriginal.md', 160, 'S0047404500007600,S0047404500007600'), ('MULTI-ID', 'corpus/knowledge/civilizations/chimu.md', 22, 'S0718,S0718'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 43, 'S404,S404')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/f-duplicate.run3.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=107 got=129 missing=0 extra=22 unparsed=0 files=4 summary=CITED-LINES: 129 finding(s) in 4 file(s)
CLEAN FAIL exit=1 findings=12 summary=CITED-LINES: 12 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=668 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 52, 'S378,S379'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 55, 'S374,S375')] extra=[('MULTI-ID', 'corpus/knowledge/civilizations/australia-aboriginal.md', 160, 'S0047404500007600,S0047404500007600'), ('MULTI-ID', 'corpus/knowledge/civilizations/chimu.md', 22, 'S0718,S0718'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 43, 'S404,S404')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/f-duplicate.run4.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=75 got=93 missing=0 extra=18 unparsed=0 files=4 summary=CITED-LINES: 93 finding(s) in 4 file(s)
CLEAN FAIL exit=1 findings=12 summary=CITED-LINES: 12 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=668 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 52, 'S378,S379'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 55, 'S374,S375')] extra=[('MULTI-ID', 'corpus/knowledge/civilizations/australia-aboriginal.md', 160, 'S0047404500007600,S0047404500007600'), ('MULTI-ID', 'corpus/knowledge/civilizations/chimu.md', 22, 'S0718,S0718'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 43, 'S404,S404')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
@@@ logs/f-duplicate.run5.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN FAIL exit=1 want=95 got=117 missing=0 extra=22 unparsed=0 files=4 summary=CITED-LINES: 117 finding(s) in 4 file(s)
CLEAN FAIL exit=1 findings=7 summary=CITED-LINES: 7 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL FAIL exit=1 want=603 got=668 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 52, 'S378,S379'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 55, 'S374,S375')] extra=[('MULTI-ID', 'corpus/knowledge/civilizations/australia-aboriginal.md', 160, 'S0047404500007600,S0047404500007600'), ('MULTI-ID', 'corpus/knowledge/civilizations/chimu.md', 22, 'S0718,S0718'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 43, 'S404,S404')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
exit=1
```

```
@@@ logs/g-lookalike.run1.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=79 got=79 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 79 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run2.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=93 got=93 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 93 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run3.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=95 got=95 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 95 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run4.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=91 got=91 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 91 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run5.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=75 got=75 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 75 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run6.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=95 got=95 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 95 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run7.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=98 got=98 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 98 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run8.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=92 got=92 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 92 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run9.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=80 got=80 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 80 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run10.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=73 got=73 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 73 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run11.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=84 got=84 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 84 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run12.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=84 got=84 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 84 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run13.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=94 got=94 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 94 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run14.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=94 got=94 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 94 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run15.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=74 got=74 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 74 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run16.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=88 got=88 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 88 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run17.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=80 got=80 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 80 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run18.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=87 got=87 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 87 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run19.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=90 got=90 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 90 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/g-lookalike.run20.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=95 got=95 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 95 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```

```
@@@ logs/honest.run1.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=89 got=89 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 89 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/honest.run2.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=97 got=97 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 97 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/honest.run3.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=89 got=89 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 89 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/honest.run4.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=76 got=76 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 76 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
@@@ logs/honest.run5.txt
TOOL PASS exists=True exit=0 last='selftest 17/17'
INDEP PASS exists=True
GEN PASS exit=1 want=91 got=91 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 91 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
exit=0
```

## Files changed

- Lane: `.ufo/waves/round-61/w1/CtlOParsing.md` (this report) — the only lane write, one write call.
- Scratch (`/fast/scratch/hyaku/kotodama-r61/CtlOParsing/`): `clone/` (sandbox clone; the fixture
  tool lives at `clone/tools/check-cited-lines.py`), `build_fakes.py`, `fakes/<case>/check-cited-lines.py`
  (8 files), `probe/lookalike.md`, `logs/*.txt` (86 files). No process left running; every command
  was wrapped in `timeout` (≤ 900 s).

## Risks carried by claim O

1. **Frozen `ACCEPT-O-61` cannot detect lookalike counting.** A shipped
   `tools/check-cited-lines.py` using `re.compile(r"S\d{3,}")` (no `\b`) passes the predicate in
   every run (20/20) yet invents `MULTI-ID` findings on text such as `XS612`/`S612x`/`S612_`
   next to a different id (probe above). If the round-61 O implementation should happen to omit
   the word boundaries, no leg will say so. Under the contract regex `\bS\d{3,}\b` the issue
   does not arise.
2. Two parser gaps are stopped by GEN **only** (a-3digit, e-indent): their REAL leg passes on the
   base corpus, so a regression in the generator alone would let them through — but 20/20
   (e) and 5/5 (a) show GEN currently carries that load reliably.
3. No flaky leg was observed in 86 runs; b-range and e-indent, the two cases whose fixture
   depends on a random draw, failed GEN 20/20 each with margin (worst b run still missed 2
   findings, worst e run missed 7).
4. Probe status: `probe=n/a` legitimately — `accept-o.py` has no `FLOOR`/`TOTAL`/base-list
   constant; the only probe described by the round's rules is an accept-c.py one.

## Blockers

None. No installs were made; no external state was touched; nothing was committed or pushed.
