# MutToolO — landed claim-O mutation probe

## Scope and axes

Measured revision: `efbee29cd8c0872a4fb89db34c489d4a9960916c` (2026-10-23).
Target: `tools/check-cited-lines.py`.
Axis under challenge: **operability**. Probe axes: detector sensitivity, behavioral coverage, isolation, and exact restoration.

**Result: 9 independent single-line mutants; 8 killed, 1 survived, 0 inconclusive.** The survivor exposes an output-order coverage gap in ACCEPT-O-61. It does not change the already-frozen ACCEPT-O-61 PASS or ACCEPT-C-61 FAIL verdicts.

Only the isolated clone was mutated. No product fix, counter change, integration, delegation, external research, or installation was performed. `reports/round-61/accept-c.py` was never run. This report is this seat's only lane write.

## Setup and detector

Scratch root: `/fast/scratch/hyaku/kotodama-r61/w2/MutToolO/`.
Clone: `/fast/scratch/hyaku/kotodama-r61/w2/MutToolO/clone`.

Commands executed with `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` unset:

```text
timeout 120 git -c gc.auto=0 clone --shared --no-checkout /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r61/w2/MutToolO/clone
timeout 120 git -c gc.auto=0 -c core.hooksPath=/dev/null -C /fast/scratch/hyaku/kotodama-r61/w2/MutToolO/clone checkout --detach efbee29cd8c0872a4fb89db34c489d4a9960916c
```

Checkout output: `HEAD is now at efbee29 round-61: claim C lands the footwear entry, S652-S692 and its README index row`.
Shared cloning avoided copying large Git object packs; mutations affected ordinary clone worktree files, not shared objects.

Every acceptance invocation used this exact inner command, with the clone as cwd:

```text
timeout 600 python3 -B reports/round-61/accept-o.py
```

`run-detector.py` in the scratch root recorded exit status, full stdout/stderr, elapsed time, and tool/counter SHA-256 before and after each invocation. It set `TMPDIR` inside the seat's scratch root, unset the three Git variables above, imposed a 4,900,000-byte regular-file limit, bounded communication to 590 seconds, and killed/reaped its process group. Each recorder process also had an outer `timeout 600`. No background jobs or services were started. All acceptance runs completed in 0.409–1.023 seconds; none timed out.

Run order was `pristine → M01 → restored-M01 → M02 → restored-M02 → … → M09 → restored-M09`. Thus each mutant had a passing pristine-byte run immediately before it and a passing exact-restoration run after it. The detector itself generates fresh randomized fixture bytes on each invocation; this is the same bounded detector, not a claim of identical random fixtures.

Full raw receipts are under scratch `evidence/<label>.json`, with separate `<label>.stdout.txt` and `<label>.stderr.txt`; labels are the names in the tables below. All acceptance stderr captures were empty.

## Mutants and outcomes

Each row changes exactly one behavior-bearing source line, independently from pristine bytes. Unlisted legs passed.

| ID / receipt label | Source line and single-point mutation | Expected detector | Actual counter exit / failed legs | Verdict |
|---|---|---|---|---|
| M01 / `M01-regex-boundary` | 44: `re.compile(r"\bS\d{3,}\b")` → `re.compile(r"S\d{3,}")` | GEN/CLEAN reject lookalike matches | 1; GEN, CLEAN | **Killed** |
| M02 / `M02-sort-order` | 55: numeric key `int(text[1:])` → lexical key `text[1:]` | GEN rejects lexically ordered mixed-width ids | 1; GEN | **Killed** |
| M03 / `M03-table-detection` | 59: `line.lstrip().startswith("|")` → `line.startswith("|")` | GEN rejects missed indented table rows | 1; GEN | **Killed** |
| M04 / `M04-distinct-id-count` | 55: `sorted(set(SID.findall(line)), …)` → `sorted(SID.findall(line), …)` | GEN/CLEAN reject duplicate-match counting; REAL may also differ | 1; GEN, CLEAN, REAL | **Killed** |
| M05 / `M05-summary-count` | 135: summary `len(findings)` → `len({(display, number) for _, display, number, _ in findings})` | GEN rejects counting offending lines instead of findings | 1; GEN | **Killed** |
| M06 / `M06-exit-codes` | 136: `return 1 if findings else 0` → `return 0` | GEN/REAL reject successful exit despite findings | 1; GEN, REAL | **Killed** |
| M07 / `M07-md-filter` | 88: `name.endswith(".md")` → `name.endswith((".md", ".txt"))` | GEN rejects scanning the deliberately excluded `.txt` fixture | 1; GEN | **Killed** |
| M08 / `M08-utf8-handling` | 72: `raw.decode("utf-8")` → `raw.decode("utf-8", errors="replace")` | ERR rejects accepting malformed UTF-8 | 1; ERR | **Killed** |
| M09 / `M09-finding-order` | 133: iterate `findings` → `reversed(findings)` | An order-sensitive GEN/REAL check should reject reversed line order | 0; none | **Survived** |

### Actual pristine detector output

Exit 0:

```text
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN PASS exit=1 want=99 got=99 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 99 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
```

### Actual mutant detector outputs

M01, exit 1:

```text
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN FAIL exit=1 want=94 got=112 missing=0 extra=18 unparsed=0 files=4 summary=CITED-LINES: 112 finding(s) in 4 file(s)
CLEAN FAIL exit=1 findings=18 summary=CITED-LINES: 18 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
```

M02, exit 1:

```text
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN FAIL exit=1 want=85 got=85 missing=8 extra=8 unparsed=0 files=4 summary=CITED-LINES: 85 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
```

M03, exit 1:

```text
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN FAIL exit=1 want=94 got=85 missing=9 extra=0 unparsed=0 files=4 summary=CITED-LINES: 85 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
```

M04, exit 1:

```text
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN FAIL exit=1 want=87 got=108 missing=0 extra=21 unparsed=0 files=4 summary=CITED-LINES: 108 finding(s) in 4 file(s)
CLEAN FAIL exit=1 findings=16 summary=CITED-LINES: 16 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL FAIL exit=1 want=603 got=668 missing=[('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 45, 'S380,S382'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 52, 'S378,S379'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 55, 'S374,S375')] extra=[('MULTI-ID', 'corpus/knowledge/civilizations/australia-aboriginal.md', 160, 'S0047404500007600,S0047404500007600'), ('MULTI-ID', 'corpus/knowledge/civilizations/chimu.md', 22, 'S0718,S0718'), ('MULTI-ID', 'corpus/knowledge/civilizations/kongo-kingdom.md', 43, 'S404,S404')] r60_line_in_reference=True
ACCEPT-O-61: FAIL
```

M05, exit 1:

```text
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN FAIL exit=1 want=116 got=116 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 87 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
```

M06, exit 1:

```text
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN FAIL exit=0 want=87 got=87 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 87 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL FAIL exit=0 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
```

M07, exit 1:

```text
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN FAIL exit=1 want=95 got=96 missing=0 extra=1 unparsed=0 files=4 summary=CITED-LINES: 96 finding(s) in 5 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
```

M08, exit 1:

```text
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN PASS exit=1 want=106 got=106 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 106 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR FAIL missing_exit=2 badutf8_exit=1 noargs_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: FAIL
```

M09, exit 0:

```text
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN PASS exit=1 want=91 got=91 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 91 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
```

## Survivor: ordering is not observed by the counter

The tool's contract says findings appear in line order; its documented two-finding order is MULTI-ID before TABLE-ID. M09 reverses both while retaining the finding set, summary and exit code.

Counter source explains the observed survival: `reports/round-61/accept-o.py:89-99` parses findings into a **set**; GEN (`174-175`) and REAL (`207-209`) compare those sets. They cannot distinguish a valid finding sequence from its reversal. This is a coverage finding, not permission to change the contract or a revision of the frozen verdict.

A direct, bounded witness was additionally run on pristine, M09 and restored bytes using the same command each time:

```text
timeout 30 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE TMPDIR=/fast/scratch/hyaku/kotodama-r61/w2/MutToolO/tmp python3 -B tools/check-cited-lines.py /fast/scratch/hyaku/kotodama-r61/w2/MutToolO/order.md
```

Fixture bytes (34 bytes, final newline present):

```text
- first S612 S613
| S614 | S615 |
```

Pristine **and restored** actual stdout, both exit 1:

```text
MULTI-ID /fast/scratch/hyaku/kotodama-r61/w2/MutToolO/order.md:1 S612,S613
MULTI-ID /fast/scratch/hyaku/kotodama-r61/w2/MutToolO/order.md:2 S614,S615
TABLE-ID /fast/scratch/hyaku/kotodama-r61/w2/MutToolO/order.md:2 S614,S615
CITED-LINES: 3 finding(s) in 1 file(s)
```

M09 actual stdout, exit 1:

```text
TABLE-ID /fast/scratch/hyaku/kotodama-r61/w2/MutToolO/order.md:2 S614,S615
MULTI-ID /fast/scratch/hyaku/kotodama-r61/w2/MutToolO/order.md:2 S614,S615
MULTI-ID /fast/scratch/hyaku/kotodama-r61/w2/MutToolO/order.md:1 S612,S613
CITED-LINES: 3 finding(s) in 1 file(s)
```

## Hashes and restoration evidence

Pristine tool SHA-256 (`P`):

```text
a9b0fbd5809b3764b2309cd8a82625c75ca1d6dd7c498309387050312078804a
```

Counter SHA-256, unchanged before and after **all 19 acceptance runs**:

```text
5f1530a485d307544ccbde94a8c1f80b3f9d5360b7c8a4966259174e3d3bb99d
```

Every mutation started from P; each acceptance run's mutated before/after hashes were identical to its row below. Every restoration returned to P before the next mutant was applied.

| Mutant | Mutated SHA-256 before = after detector | Restored SHA-256 before = after detector |
|---|---|---|
| M01 | `a758da83e3a6a85e2faa80d2da584c7d8e4d9ceda2ae056f55ceca89d45af334` | P |
| M02 | `edcc57cfaa9a8538fd4f9d0742c8f8a2f110a599af09b7429564d8208a013f3a` | P |
| M03 | `977105b2591e57e105b602a68b87e1d7fba73bd65237392d0a423a01641beea8` | P |
| M04 | `dc7889dc0d26c0c04a057cfc7bd7c36be7fbd5f7f04a4d6170578d98482cda2a` | P |
| M05 | `1c37c25ad6d9a0802e194e1b8dc903b80e0d1ad11c4dcf4c599501979da62578` | P |
| M06 | `5d5af3fc388144cab68673ea6e4eb272af1f5bfb5058c13600bc47c65dce5dfb` | P |
| M07 | `805158a5a58e261e04a322a6820122d72fc9b4328d376a4d5c099dc6511b4dc9` | P |
| M08 | `1de929258fb7aa47a2adc3b4db0eed83b858806b086f7c404d407266029c2716` | P |
| M09 | `ab4632b8cfeb936e48ac317529068e353ff3485513d8c160e1ad51938ae1cfa4` | P |

All restoration runs printed every leg PASS and `ACCEPT-O-61: PASS`, exit 0. Their observed GEN counts were:

| Receipt label | want = got | missing / extra | Files |
|---|---:|---|---:|
| `restored-M01` | 90 | 0 / 0 | 4 |
| `restored-M02` | 86 | 0 / 0 | 4 |
| `restored-M03` | 101 | 0 / 0 | 4 |
| `restored-M04` | 85 | 0 / 0 | 4 |
| `restored-M05` | 89 | 0 / 0 | 4 |
| `restored-M06` | 73 | 0 / 0 | 4 |
| `restored-M07` | 104 | 0 / 0 | 4 |
| `restored-M08` | 87 | 0 / 0 | 4 |
| `restored-M09` | 83 | 0 / 0 | 4 |

Every restoration also observed REAL `want=603 got=603 missing=[] extra=[] r60_line_in_reference=True`, CLEAN `exit=0 findings=0`, and ERR exits `2/2/2`.

Final byte-for-byte comparison:

```text
timeout 30 cmp /fast/scratch/hyaku/kotodama-r61/w2/MutToolO/pristine-check-cited-lines.py /fast/scratch/hyaku/kotodama-r61/w2/MutToolO/clone/tools/check-cited-lines.py
```

Observed no output, exit 0. The subsequent `sha256sum` printed P for both the saved pristine file and restored clone target, and the unchanged counter hash above. Final restored acceptance output:

```text
TOOL PASS exists=True
INDEP PASS exists=True names=[]
GEN PASS exit=1 want=83 got=83 missing=0 extra=0 unparsed=0 files=4 summary=CITED-LINES: 83 finding(s) in 4 file(s)
CLEAN PASS exit=0 findings=0 summary=CITED-LINES: 0 finding(s) in 1 file(s)
ERR PASS missing_exit=2 badutf8_exit=2 noargs_exit=2
REAL PASS exit=1 want=603 got=603 missing=[] extra=[] r60_line_in_reference=True
ACCEPT-O-61: PASS
```

No detector or tool changes were retained. Tool installs/updates: **none**.
