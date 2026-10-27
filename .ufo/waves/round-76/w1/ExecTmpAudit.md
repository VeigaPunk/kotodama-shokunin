# ExecTmpAudit — round 76 (hyaku run 10), wave 1

Routed defect: hardcoded `/tmp` scratch roots (prompt §7.4).

**Verdict.** The defect is real and smaller than the grep suggests: of **139** grep hits at base
`98c486bdb4650ba5b8e651d332910e8ee60ad121`, **14** are literal `/tmp` write/scratch roots (5 shell
variables in frozen wave helpers, 6 string assignments in frozen rounds, 3 copies of one constant in the
active round-75 counter), **6** are `os.environ.get("TMPDIR", "/tmp")` fallbacks, **8** are
`tempfile.mkdtemp()` with no `dir=` (7 frozen, 1 active; two further ones sit in a frozen `UNPARSED`
draft), and the remaining **111** are 99 comments / doc-and-prompt strings / embedded fixture text /
frozen run receipts plus 12 code-position read-only or guard uses. Only **one**
hit is a `tools/` file — `tools/harness/couples-reference-extractor.py:270` — and it turns out *not*
to be a literal-`/tmp` root at all: it honours `TMPDIR` but ignores `--work`/`$HYAKU_SCRATCH` **and
leaks its fixture tree** (measured below). The active literal-`/tmp` root that does matter is
`reports/round-75/accept-ca.py:2175 R74_TMPDIR = "/tmp"`, which the round-76 Ca counter would
inherit; I show by measurement that the stated reason for it is wrong, and stage an advisory diff.

Bounds honoured: no write outside `.ufo/waves/round-76/w1/`; the fleet repo, the lane git/jj state,
`reports/round-75/**`, `corpus/**`, `.ufo/state`, `LOG.md`/`SCORECARD.md`/`SKILL.md`/`SHONEN.md` and
`shokuknow` were read only. All scratch lived in `/fast/scratch/hyaku/kotodama-r76/ExecTmpAudit/` and
was deleted before yielding. No tool was installed or upgraded (python3 stdlib only).

## 1. Inventory at base

Sweep (the routed command, run verbatim):

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -n \
    -E '("/tmp["/]|dir=.?/tmp|mkdtemp\(\)|/tmp/)' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- '*.py' '*.sh' | wc -l
139
```

Raw output kept at `stage/ExecTmpAudit/grep-hits.txt` (139 lines, grep exit 0). Classification of
every one of those lines is machine-produced by `stage/ExecTmpAudit/classify-tmp-hits.py` — for each
line it decides, by tokenizer position, whether the literal sits in code, in a string, in a comment or
in a frozen `.txt` receipt — and joined to the scanner's class:

```
$ python3 -B classify-tmp-hits.py grep-hits.txt <98c486b export> check-scratch-root.py > hits-classified.tsv
$ awk -F'\t' 'NR>1{print $3"/"$4"/"$5}' hits-classified.tsv | sort | uniq -c | sort -rn
     83 frozen/string/clean
     15 active/string/clean
     11 frozen/code/clean
      7 frozen/code/UNROUTED
      6 frozen/string/HIT
      5 frozen/shell-code/HIT
      3 frozen/string/FALLBACK
      3 active/string/HIT
      3 active/string/FALLBACK
      1 frozen/shell-comment/clean
      1 frozen/shell-code/clean
      1 active/code/UNROUTED
$ awk -F'\t' 'NR>1' hits-classified.tsv | wc -l
139
```

`scope=active` = `tools/`, `reports/round-7[3-5]/`, `.ufo/waves/round-75/counters/` and
`.ufo/waves/round-75/w2/stage/reports/`. Everything else is frozen evidence of a closed round.

### The 14 literal-`/tmp` scratch roots

| file | line | kind | disposition |
|---|---|---|---|
| `.ufo/waves/round-68/stage/mut-entry/run_accept_c.py` | 38 | string | frozen: fixture root of a closed round's mutation harness |
| `.ufo/waves/round-72/assimilation/validate/checks.py` | 60 | string | frozen: `--mirror` default `/tmp/r72-mirror` |
| `.ufo/waves/round-72/assimilation/validate/refresh-and-validate.sh` | 16, 17 | shell-code | frozen: `MIRROR=`/`ENTRIES=` literal roots |
| `.ufo/waves/round-73/assimilation/validate/mirror-validate.sh` | 7, 8, 27 | shell-code | frozen: `M=`/`ENT=` literal roots + `> /tmp/r73-mirror-census.out` |
| `.ufo/waves/round-73/evidence-build.py` | 14 | string | frozen: `TMP = "/tmp/r73-evidence"` |
| `.ufo/waves/round-74/apply-landing.py` | 38 | string | frozen: copy source `/tmp/ScribeReadmeIndex/r74/README.md` |
| `reports/round-17/run-validation.py` | 644, 658 | string | frozen: `run_command(..., tmpdir="/tmp")` ×2 |
| **`reports/round-75/accept-ca.py`** | **2175** | string | **active: `R74_TMPDIR = "/tmp"`** — §4 |
| **`.ufo/waves/round-75/counters/accept-ca.py`** | **2175** | string | **active: same constant, byte copy of the above** |
| **`.ufo/waves/round-75/w2/stage/reports/round-75/accept-ca.py`** | **2173** | string | **active: same constant, w2 staged copy** |

Historical rounds **1–60** (`reports/round-8…60/**`, `.ufo/waves/round-50…60/**`) are **frozen
evidence and stay unedited**; their hits are disclosed above and nowhere asserted to be clean. The
same holds for the round-61…75 wave machinery: closed rounds are not rewritten in wave 1.

### Active non-clean rows (everything above plus)

```
$ awk -F'\t' 'NR>1 && $3=="active" && $5!="clean"{print $1":"$2"  "$4"  "$5}' hits-classified.tsv
.ufo/waves/round-75/counters/accept-ca.py:2175              string  HIT
.ufo/waves/round-75/w2/stage/reports/round-75/accept-ca.py:2173  string  HIT
reports/round-73/accept-ca.py:347                            string  FALLBACK
reports/round-74/accept-ca.py:844                            string  FALLBACK
reports/round-74/accept-ca.py:1730                           string  FALLBACK
reports/round-75/accept-ca.py:2175                           string  HIT
tools/harness/couples-reference-extractor.py:270             code    UNROUTED
```

The three FALLBACKs are `"TMPDIR": os.environ.get("TMPDIR", "/tmp")` in the round-73/74 counters, i.e.
those instruments write under a literal `/tmp` whenever the host leaves `TMPDIR` unset. They are closed
rounds and are reported, not edited. `reports/round-75/accept-c.py:6024`
(`banned = {abspath("/tmp"), abspath(gettempdir())}`) is a guard, not a target, and is correctly clean.

### The `tools/` hit is not a literal `/tmp` root

`tools/harness/couples-reference-extractor.py:270` is `tmp = tempfile.mkdtemp()` — no `dir=`. Measured
consequences (`stage/ExecTmpAudit/extractor-before-after.txt`):

```
$ TMPDIR=<scratch>/base-tmp python3 -B base_extractor.py --selftest   # exit 0
$ ls -A <scratch>/base-tmp
tmpad6au8k7                       # the fixture tree is left behind
$ python3 -B base_extractor.py --selftest --work <scratch>/work3
base-extractor.py: error: unrecognized arguments: --work   # exit 2
```

So the file honours `TMPDIR` (it is *not* the hardcoded-`/tmp` case) but (a) ignores the lane's
`--work`/`$HYAKU_SCRATCH` route and (b) leaks. Its own docstring said the opposite —
"Read-only: opens corpus files, writes nothing" — which is also a calibration-grade false statement
about the file (for Ca: `tools/harness/couples-reference-extractor.py:15` at base, repairable).

## 2. Scanner `check-scratch-root.py` (staged, not installed)

`stage/ExecTmpAudit/check-scratch-root.py` — read-only, stdlib, creates no directory:

```
check-scratch-root.py --root <dir> --paths <glob…> [--allow <file>] [--strict] [--selftest] [--work <dir>]
```

* `--paths` is a repeatable glob list; `**` walks **hidden** segments (`.ufo`) — `glob.glob` refuses a
  leading dot, so a plain-glob tool would have reported "clean" over the lane's whole wave machinery.
  Written as an explicit matcher (`pattern_regex`) and covered by a fixture.
* Classes: `HIT` (write target under literal `/tmp`: `open(...,'w'/'a'/'x'/'+')`, `mkdir`/`makedirs`,
  `dir=`/`cwd=`/`default=`/`tmpdir=`/`work=`/`scratch=`/`root=` keywords, copy destinations,
  `rmtree`, `X = "/tmp"` for a scratch-named X, `{"TMPDIR": "/tmp"}`, shell redirection, `mktemp`,
  `NAME=…/tmp`, `cd`), `FALLBACK` (`os.environ.get("TMPDIR", "/tmp")`), `UNROUTED`
  (`mkdtemp`/`TemporaryDirectory`/… without `dir=`), `UNPARSED`. Exit 1 iff a non-allowlisted `HIT`
  (or, with `--strict`, any non-allowlisted `HIT`/`FALLBACK`/`UNROUTED`). `--allow` matches globs
  against `rel` **or** `rel:line`.
* Reported line = the line of the argument that carries the `/tmp` constant, so a grep hit and a
  scanner row name the same line (`reports/round-17/run-validation.py:644` and `:658` now agree with
  grep, where the AST call-head line had said 656).
* The scanner is not a `/tmp` writer itself: `scan_file(__file__)` yields no `HIT` (selftest row
  "scanner writes nothing under a literal /tmp").

Selftest — 18 fixtures plus 7 contract checks, **25 PASS / 0 FAIL, exit 0**
(`stage/ExecTmpAudit/selftest.txt`), run with `--work` inside my scratch:

```
$ python3 -B check-scratch-root.py --selftest --work <scratch>/work
...
PASS class fixtures/unrouted_mkdtemp.py got=['UNROUTED']
PASS allowlist suppresses
PASS hidden segment walked under ** checked=1 missing=[]
PASS scanner writes nothing under a literal /tmp []
SELFTEST_EXIT=0
$ grep -c '^PASS' selftest.txt
25
```

Fixtures cover the four routed cases (`mkdtemp(dir="/tmp")`, `mkdtemp(prefix=…, dir='/tmp')`,
`open('/tmp/x','w')`, shell `mktemp -d /tmp/foo.XXXXXX`), plus `open(mode='a')`, `Path('/tmp/x').mkdir`,
`{"TMPDIR": "/tmp"}`, `R74_TMPDIR = "/tmp"`, `cwd='/tmp/build'`, `> /tmp/out`, and non-hits: a comment, a
docstring forbidding `/tmp`, `open('/tmp/x')` / `open(...,'r')`, `os.listdir('/tmp')`, `cat`/`grep` of a
`/tmp` file, a `--work`-routed `dir=`, and an allowlisted hit.

The selftest is **shown able to fail**: deleting the `mktemp` shell rule and the `dir=` keyword rule in a
scratch copy flips 5 fixtures to FAIL and exits 1 (`stage/ExecTmpAudit/mutant.txt`):

```
FAIL class fixtures/hit_mkdtemp_dir.py got=[]
FAIL class fixtures/hit_mkdtemp_prefix_dir.py got=[]
FAIL class fixtures/hit_popen_cwd.py got=[]
FAIL class fixtures/hit_sh_mktemp.sh got=[]
FAIL hidden segment walked under ** checked=1 missing=[]
MUTANT_EXIT=1
```

Scan of the whole base tree (538 committed `.py`/`.sh` files, extracted with
`git archive 98c486b | tar -x -C full --wildcards '*.py' '*.sh'`; `find full -type f | wc -l` → 538):

```
$ python3 -B check-scratch-root.py --root full --paths '**/*.py' '**/*.sh'
checked=538 FALLBACK=6 HIT=14 UNPARSED=1 UNROUTED=276      EXIT=1
```

Active subset only (`stage/ExecTmpAudit/active.txt`):

```
checked=80 FALLBACK=3 HIT=2 UNROUTED=108                    EXIT=1
```

Of those 108 `UNROUTED` rows, `82` are `TemporaryDirectory()` and `1` is `NamedTemporaryFile()`; `25` are
bare `mkdtemp()` (`grep -oE '[A-Za-z_]+\(\) without' active.txt | sort | uniq -c`). The extractor is the
one I proved leaks; cleanup for the other 24 is **not verified** here.

The single `UNPARSED` row is `.ufo/waves/round-75/drafts/sweep-fixed.py` (a staged draft fragment the
`ast` refuses); it is scanned with the shell rules and is frozen w2 material, not a live tool.

## 3. Fix draft — `tools/harness/couples-reference-extractor.py`

`stage/ExecTmpAudit/couples-reference-extractor.py.diff` (75 lines, `patch -p1 --dry-run` exit 0, both
versions `compile()` clean). It does not edit the lane file.

* adds `scratch_root(work=None)`: `--work`, then `$HYAKU_SCRATCH`, then `$SHOKUNIN_SCRATCH`, then
  `tempfile.gettempdir()` — the same chain the round-75 counters use;
* `selftest(work=None)` creates one tree with `tempfile.mkdtemp(prefix="couples-ref-selftest-", dir=scratch_root(work))`
  and removes it in a `finally: shutil.rmtree(..., ignore_errors=True)`; the old body becomes
  `_selftest_checks(root)` and `tmp = tempfile.mkdtemp()` becomes `tmp = os.path.join(root, "fixture")`;
* `main` gains `--work` and passes it to `selftest`;
* the false docstring line "Read-only: opens corpus files, writes nothing" is replaced by the truth
  (entry/census are read-only; the selftest writes one routed tree and removes it).

Before/after under the scanner (`stage/ExecTmpAudit/scanner-before-after.txt`):

```
=== before (base tools/harness/couples-reference-extractor.py), --strict:
UNROUTED  tools/harness/couples-reference-extractor.py:270: mkdtemp() without dir=
checked=1 UNROUTED=1     EXIT=1
=== after (draft), --strict:
checked=1 clean          EXIT=0
```

Behaviour after the draft, executed in a lane-shaped fixture (`tools/harness/` +
`corpus/knowledge/linguistics/phonetics-phonology.md` at base):

```
$ python3 -B couples-reference-extractor.py --selftest --work <scratch>/work2
PASS … 8/8 …   EXIT=0
$ ls -A <scratch>/work2 | wc -l
0          # nothing left behind
```

The 8 selftest checks are unchanged in content and still all pass (`--census`/positional paths untouched).

## 4. Routed finding for the round-76 Ca counter (`R74_TMPDIR`)

`reports/round-75/accept-ca.py:2170-2175` keeps a literal `/tmp` for the round-74 counter's clones, with
the justification "its normalizer strips /tmp paths alone". That justification does not hold:
`normalize_receipt` applies **two** regexes, and the second —
`RECEIPT_R74_TMP_RE = (?<![\w./-])/(?:[^\s"']*/)?r74-ca-[^\s"']*` — strips any root prefix whose
directory carries the `r74-ca-` basename. Measured by importing the committed counter and calling its
own normalizer (`stage/ExecTmpAudit/normalizer.txt`):

```
raw       : clone=/fast/scratch/hyaku/kotodama-r76/ExecTmpAudit/work/r74-ca-abc123/lands head=5e4796c
normalized: clone=<TMP> head=5e4796c
raw       : clone=/tmp/r74-ca-abc123/lands head=5e4796c
normalized: clone=<TMP> head=5e4796c
```

A routed clone root normalizes identically, and `reports/round-74/accept-ca.py:1966` creates its clone
with `tempfile.mkdtemp(prefix="r74-ca-")`, so the prefix always survives. Advisory diff
`stage/ExecTmpAudit/accept-ca-r74-tmpdir.py.diff` (patch dry-run exit 0 against a
`reports/round-76/accept-ca.py` copy, `compile()` clean, scanner strict exit 0) replaces the constant
with `_r74_tmpdir()` — `RUN_STATE["work"]`, and a hard `SystemExit` when no work root is set rather than a
silent `/tmp` fallback:

```
=== before (base reports/round-75/accept-ca.py, the round-76 copy source), --strict:
HIT  reports/round-75/accept-ca.py:2175: R74_TMPDIR = '/tmp'   EXIT=1
=== after (advisory draft reports/round-76/accept-ca.py), --strict:
checked=1 clean                                                EXIT=0
```

This diff is **advisory**: it is written against the round-76 path the Ca seat creates, it is not applied
anywhere, and the round-75 counter itself is untouched. If the Ca seat prefers a different work-root
plumbing, the finding that matters is the measurement: the literal `/tmp` is not required.

## 5. Risks, blockers, unrun

* **Unrun (by design).** No counter run, no `accept-ca.py --selftest`, no lane build/lint: wave 1 is in
  flight and the parent owns the gate. The advisory counter diff is verified by `patch --dry-run` +
  `compile()` only, **not executed** — the RECEIPTS leg that consumes it is unproven here.
* **Inherited duplicates.** `R74_TMPDIR` exists in three committed copies
  (`reports/round-75/accept-ca.py`, `.ufo/waves/round-75/counters/accept-ca.py`,
  `.ufo/waves/round-75/w2/stage/reports/round-75/accept-ca.py`). A fix applies to whichever copy the
  round-76 counter derives from; the two wave-dir copies are frozen.
* **Scanner limits.** It sees literals, not values: `tempfile.gettempdir()` fallbacks, `$TMPDIR` trust and
  `os.environ.get("TMPDIR") or …` chains are outside `HIT` (the `UNROUTED` class exists precisely to keep
  that population visible: 276 rows at base). It parses `.py` with `ast` and `.sh` line-wise; a shell
  heredoc or an `eval`-built path would evade it. `UNROUTED` says nothing about cleanup for the 24
  `mkdtemp()` sites outside the extractor.
* **Frozen rounds untouched (declared, not fixed).** Round 1–60 reports and the round-50…75 wave
  machinery keep their literal `/tmp` roots: 14 `HIT` rows minus the 3 active ones are disclosed above.
* No blockers. Nothing left undone inside the assigned scope.
