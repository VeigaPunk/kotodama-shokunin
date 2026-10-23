# CtlORawSubstring — Claim O raw-HTML control (pre-data)

## Scope and axes

- Axis: **operability** (claim O, `reports/round-62/accept-o.py`). Probe axes: location verdict fidelity (body vs caption vs absent), attempt/request accounting, exit semantics, argument order, private-host refusal, default timing, and input-error handling.
- Frozen clone revision: `f0173481047a93c46798f90b68d71d4f169d2642` (sandbox clone at `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/clone`).
- Frozen counter: `reports/round-62/accept-o.py`, SHA-256 `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551` — identical before and after every run (verified by `sha256sum` after the last run; no PROBE copy of the counter was made, and the counter was never edited).
- Prerequisites read: round-62 `claims.json` (claim O statement, legs, `controls_required_before_data.O`), round-61 verifier spot-check section 7, the frozen counter's docstring + implementation, godspeed skill, `/home/vgpnk/.omp/agent/RULES.md`.
- Scratch root: `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring`. **No lane implementation, registry, lesson, or counter file was edited.** The only lane write is this report.
- Installs/updates: **none** (no pacman, no uv, no npm, no cargo). Only the stock `python3` (3.14) already on the host was used.

## What was built

One tool implementation with a single-line switch, `EXTRACT_MODE`, holding **all** the contract behaviour (registry parsing, source-cell URL list with `; capture` fallback, first quoted span of the anchor cell, NFKC/casefold/non-word-run normalisation, three attempts per URL per pass, the pass/gap/pass retry budget, the LOCATED > CAPTION_ONLY > ABSENT > UNREACHABLE > REFUSED ordering, `--allow-private` refusal without a request, `NO_ROW`/`NO_QUOTE` (quote under eight normalised words, or no URL, with no request), the `ROW <ID> <VERDICT> attempts=<n> url=<url|->` line, the `REOPEN: <k>/<m> located` summary, exit 0/1/2, and the five `REOPEN_ERROR` input-error cases with no traceback). The only mutation is the **location** rule.

Five variants were built from that one source by changing exactly one line (`EXTRACT_MODE = "..."`); every diff is a single line, shown below.

- `split` (**faithful**): BODY and CAPTION are separated. `figcaption` and any element whose `class`/`id` contains `caption` (case-insensitive) and its descendants go to CAPTION, together with the values of `alt`, `title`, `aria-label`, `content` and every `data-*` attribute; `script`/`style`/`noscript`/`template` are neither. This is the contract behaviour and it is the **positive calibration**: it must PASS.
- `raw` (**the assigned control**): location is a normalised **substring** search over the raw HTML bytes — attributes and captions included, no body/caption split at all.
- `flat`: tag markup is erased, attribute values are kept inline, caption and script text are kept as body text (no body/caption split). A "raw-ish" variant that keeps attribute values searchable.
- `strip`: tags are stripped (regex) and caption text is kept as body text — the second variant requested by the brief.
- `stripns`: tags are stripped and `script`/`style` blocks are dropped, caption text kept as body text.

### Behaviour matrix (per fixture class, one synthetic document per class, same quotes)

| class | split | raw | flat | strip | stripns |
|---|---|---|---|---|---|
| BODY | LOCATED | LOCATED | LOCATED | LOCATED | LOCATED |
| BODY_SPLIT | LOCATED | **ABSENT** | LOCATED | LOCATED | LOCATED |
| CAP_FIG (figcaption) | CAPTION_ONLY | **LOCATED** | **LOCATED** | **LOCATED** | **LOCATED** |
| CAP_ATTR (alt/title/aria-label/data-*) | CAPTION_ONLY | **LOCATED** | **LOCATED** | **ABSENT** | **ABSENT** |
| CAP_CLASS (class/id contains `caption`) | CAPTION_ONLY | **LOCATED** | **LOCATED** | **LOCATED** | **LOCATED** |
| SCRIPT (quote only in `<script>`) | ABSENT | **LOCATED** | **LOCATED** | **LOCATED** | ABSENT |
| ABSENT | ABSENT | ABSENT | ABSENT | ABSENT | ABSENT |

Reading of the matrix: `raw` loses `BODY_SPLIT` as well, because the raw bytes carry the tag punctuation *inside* the quoted span (`"A B C, <em>d</em> — <b>e</b>"`), so the whole-word run that the contract requires is interrupted by `<em>`/`</em>` markup that normalisation turns into spaces but which still separates the words; the substring test then also fails on the em-dash. `strip`/`stripns` lose `CAP_ATTR`, because a regex tag strip also removes the attribute value that carried the quote. `stripns` is the only variant that keeps `SCRIPT` correct.

### Exact diffs (one line each)

```diff
--- probe_faithful/tools/reopen-row.py
+++ probe_raw/tools/reopen-row.py
@@ -47,7 +47,7 @@
-EXTRACT_MODE = "split"
+EXTRACT_MODE = "raw"
--- probe_faithful/tools/reopen-row.py
+++ probe_flat/tools/reopen-row.py
@@ -47,7 +47,7 @@
-EXTRACT_MODE = "split"
+EXTRACT_MODE = "flat"
--- probe_faithful/tools/reopen-row.py
+++ probe_strip/tools/reopen-row.py
@@ -47,7 +47,7 @@
-EXTRACT_MODE = "split"
+EXTRACT_MODE = "strip"
--- probe_faithful/tools/reopen-row.py
+++ probe_stripns/tools/reopen-row.py
@@ -47,7 +47,7 @@
-EXTRACT_MODE = "split"
+EXTRACT_MODE = "stripns"
```

### Fixture paths and SHA-256

| Path | Role | SHA-256 |
|---|---|---|
| `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/probe_faithful/tools/reopen-row.py` | faithful contract implementation (positive calibration) | `b14f5c91dfc01e11b907f1ff7f201ec87791837caadcac056d8793b7c8d55ae6` |
| `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/probe_raw/tools/reopen-row.py` | **assigned control** (raw-HTML substring) | `42af525cd35ab0bb087bcccbcd2bf845eac5a7b5449b5b934810b1725976fcc3` |
| `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/probe_flat/tools/reopen-row.py` | markup erased, attributes kept, no split | `b38bf31d7276462ec938bcfd49e8d2ff639f082819afc49e17dbf5806bc789c9` |
| `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/probe_strip/tools/reopen-row.py` | tags stripped, caption text kept as body | `760a8c4cf0e020f83507bd795455e3df8718fdea9450796120d129a35ae8ac06` |
| `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/probe_stripns/tools/reopen-row.py` | tags stripped, script/style dropped | `7e8e0ef8f557fee28388149ef67d68381a3fabb70655e093cba2d43f8b98a276` |
| `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/clone/tools/reopen-row.py` | the raw control placed at the clone's `tools/reopen-row.py` (never in the lane) | `42af525cd35ab0bb087bcccbcd2bf845eac5a7b5449b5b934810b1725976fcc3` |

The counter is run with `--root <dir>`; each probe root contains exactly one `tools/reopen-row.py`, and the counter copies that file into a fresh temp directory and runs it there with `cwd` set to the temp dir, as its INDEP leg requires. The `raw` case was additionally run with the control physically at `<clone>/tools/reopen-row.py` (`--root <clone>`), i.e. at the path the brief names. No fixture was placed in `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (verified: `tools/reopen-row.py` absent there).

## Full frozen-counter receipts

Every run used the same unmodified detector from the frozen clone. Working directory for every run: `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/clone`.

```sh
env TMPDIR=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/tmp2 PYTHONDONTWRITEBYTECODE=1 \
  timeout 900 python3 -B reports/round-62/accept-o.py --root <root>
```

The timeout wrapper return code is recorded as `exit=`. Each counter run creates fresh randomised local fixtures, so generated IDs and diagnostic ordering differ across runs. All five stderr streams were empty (0 bytes).

### raw (the assigned control; tool at `<clone>/tools/reopen-row.py`)

```text
### case=raw root=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/clone
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=12 ["CAP_FIG:S6474:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_ATTR:S2392:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_ATTR:S2784:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "BODY_SPLIT:S5466:want=LOCATED/1:got=[('ABSENT', 1)]", "SCRIPT:S8697:want=ABSENT/1:got=[('LOCATED', 1)]", "ARCHIVE_CAPTION:S2885:want=CAPTION_ONLY/2:got=[('LOCATED', 2)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S6065', 'REFUSED', 0), ('S6476', 'REFUSED', 0), ('S8709', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2413', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlORawSubstring/raw counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN

> **Report correction (one edit, disclosed).** The `raw` receipt's `PRIV` line above was first written with a transcription slip (`'S6476', 'REFUSED', 0)` missing its opening parenthesis). It has been restored here to the exact bytes of `/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/receipts-final/raw.txt`. This is the only edit to this report after the initial write, it changes no verdict, count, leg, or conclusion, and it restores the pasted stdout to the counter's real output. The authoritative copies of all five runs remain the retained files under `receipts-final/`.

### flat

```text
### case=flat root=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/probe_flat
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=10 ["SCRIPT:S4585:want=ABSENT/1:got=[('LOCATED', 1)]", "ARCHIVE_CAPTION:S5509:want=CAPTION_ONLY/2:got=[('LOCATED', 2)]", "CAP_FIG:S8545:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "SCRIPT:S1380:want=ABSENT/1:got=[('LOCATED', 1)]", "CAP_CLASS:S2616:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_CLASS:S2465:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S3523', 'REFUSED', 0), ('S4214', 'REFUSED', 0), ('S3434', 'REFUSED', 0)]
DEFAULT PASS rows=[('S4511', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlORawSubstring/flat counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN

### strip (tags stripped, figcaption/class=caption text kept as body)

```text
### case=strip root=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/probe_strip
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=10 ["CAP_CLASS:S1430:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_FIG:S9394:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "ARCHIVE_CAPTION:S8320:want=CAPTION_ONLY/2:got=[('LOCATED', 2)]", "ARCHIVE_CAPTION:S1602:want=CAPTION_ONLY/2:got=[('LOCATED', 2)]", "SCRIPT:S9431:want=ABSENT/1:got=[('LOCATED', 1)]", "CAP_ATTR:S8892:want=CAPTION_ONLY/1:got=[('ABSENT', 1)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S4758', 'REFUSED', 0), ('S6319', 'REFUSED', 0), ('S9138', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1283', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlORawSubstring/strip counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN

### stripns (tags stripped, script/style dropped)

```text
### case=stripns root=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/probe_stripns
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=8 ["CAP_FIG:S5103:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_CLASS:S2762:want=CAPTION_ONLY/1:got=[('LOCATED', 1)]", "CAP_ATTR:S7211:want=CAPTION_ONLY/1:got=[('ABSENT', 1)]", "CAP_ATTR:S4818:want=CAPTION_ONLY/1:got=[('ABSENT', 1)]", "ARCHIVE_CAPTION:S9889:want=CAPTION_ONLY/2:got=[('LOCATED', 2)]", "ARCHIVE_CAPTION:S1762:want=CAPTION_ONLY/2:got=[('LOCATED', 2)]"] summary_ok=False exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S4595', 'REFUSED', 0), ('S2713', 'REFUSED', 0), ('S2291', 'REFUSED', 0)]
DEFAULT PASS rows=[('S7548', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT CtlORawSubstring/stripns counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN

### faithful (positive calibration: the contract implementation)

```text
### case=faithful root=/fast/scratch/hyaku/kotodama-r62/KotodamaR62.CtlORawSubstring/probe_faithful
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S7674', 'REFUSED', 0), ('S8026', 'REFUSED', 0), ('S4815', 'REFUSED', 0)]
DEFAULT PASS rows=[('S3010', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT CtlORawSubstring/faithful counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=

## Verdicts

CONTROL-MET raw — the raw-HTML substring control **is** caught by the frozen counter: `GEN FAIL` (12 wrong rows of 37) and `ACCEPT-O-62: FAIL`, exit 1. The fixture that skips the claimed work (body/caption separation) does **not** obtain frozen PASS, so the counter has teeth on this control. The stopped leg is exactly `GEN`; `TOOL INDEP ORDER BOUND EXIT PRIV DEFAULT ERR` all PASS, confirming the failure is a location-verdict failure and not a side effect of request-count, exit-code, refusal, timing or input-error defects.

NONE-MET flat — no fixture obtained frozen PASS; the existing `GEN` leg already stops the no-split variant. Smallest counter change needed: none.

NONE-MET strip — no fixture obtained frozen PASS; the existing `GEN` leg already stops the strip-tags-but-caption-as-body variant. Smallest counter change needed: none.

NONE-MET stripns — no fixture obtained frozen PASS; the existing `GEN` leg already stops the strip-and-drop-script variant. Smallest counter change needed: none.

## What this means for claim O

- **The frozen counter discriminates the raw-HTML shortcut.** The assigned control was expected to fail `GEN` on the `CAP_*` and `SCRIPT` classes, and it does: `CAP_FIG`, `CAP_ATTR`, `CAP_CLASS` and `ARCHIVE_CAPTION` all come out `LOCATED` where the contract requires `CAPTION_ONLY`, and `SCRIPT` comes out `LOCATED` where the contract requires `ABSENT`. The raw control additionally breaks `BODY_SPLIT` (raw bytes carry the inter-word tag markup), so it fails on 12 rows rather than 8; that is a strictly stronger failure, not a weaker one, and it is recorded rather than smoothed over.
- **The contract is implementable and the counter is satisfiable.** The faithful variant (`EXTRACT_MODE = "split"`) passes **all nine legs** — `ACCEPT-O-62: PASS`, exit 0 — with `GEN wrong=0` on 37 randomised rows, `BOUND` clean, `DEFAULT` at `UNREACHABLE attempts=9` in 150 s of wall time, `PRIV` refusing all three loopback rows with `attempts=0`, and `ERR` clean on all five bad inputs. That is the positive calibration the round's control list asks for, so the four failures above are attributable to the location mutation rather than to an unsatisfiable predicate.
- **Consequence for the lane implementation.** Any `tools/reopen-row.py` that satisfies `ACCEPT-O-62` must (a) keep body text and caption text in separate buckets, with `figcaption` and any `class`/`id` containing `caption` and their descendants in the caption bucket; (b) treat the values of `alt`, `title`, `aria-label`, `content` and every `data-*` attribute as caption text; (c) treat `script`/`style`/`noscript`/`template` content as neither body nor caption; (d) match the quote as a **contiguous whole-word run** of the normalised body text (a plain substring over raw bytes fails `BODY_SPLIT`); and (e) keep the attribute-bearing `CAP_ATTR` case reachable, which a regex tag-strip destroys. The `split` implementation at `probe_faithful/tools/reopen-row.py` satisfies all of these and is available to the L1 as a reference; it is **not** written to the lane by this seat.

## Risks, blockers, boundaries

- **No blocker.** Every leg of every case was exercised; all five runs completed with empty stderr and full stdout captured.
- **Fixture randomness.** Each counter run regenerates its fixture (`random.SystemRandom()`), so the `S####` identifiers and the six-row sample printed inside the `GEN` detail differ between runs; only the class names and the wrong-row count are stable across runs. The `wrong` counts (12 / 10 / 10 / 8 / 0) and the class sets are stable and reproduce.
- **Scope note.** The `strip`/`stripns`/`flat` variants are extra probes beyond the two the brief asked for; they exist to separate *which* part of the location rule each failure class exercises, so that the lane implementation can be told exactly which behaviours are load-bearing. They are labelled as such above and none of them is presented as the assigned control.
- **Boundaries observed.** No lane file other than this report was written; the counter was never edited and no PROBE copy was made; no `git`/`jj` write command ran against either repository (the clone was created with the sanctioned `git clone` + `git checkout` of the frozen revision, and `git status` was used read-only); no network fetch was performed (all fixtures are local, and the counter judges O on an offline random fixture); no `du`/`find` over `/fast/scratch`; no process I started is still running (verified by `ps`); every process was capped with `timeout`; every file written is under my scratch root or is this report.
- **Tooling.** No install or update was needed or performed; the operator's tooling directive is satisfied vacuously, and `python3` (3.14, pre-existing) was the only tool used.
