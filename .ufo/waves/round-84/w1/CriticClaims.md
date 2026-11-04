# CriticClaims — round 84 (hyaku run 15), w1: attack on claims D and O

READ-ONLY seat. No lane byte was written except this report and
`.ufo/waves/round-84/w1/stage/CriticClaims/attack.md`. All counter runs read committed blobs at
`81499ee45b5751d388fefc78583810878de01ecd` / `3ca2cf288fb593618e0559ea86a36e2dd3110eb8` /
`e160a72e4adf1620e09f812b913d4ece0fcd5243`; work trees lived outside the lane and are not cited.

**Headline.** Both counters refuse the do-nothing control correctly and are red at the freeze
(D 2/10, O 2/8). But the round as briefed cannot be landed green:

1. **The brief's freeze revision is the wrong one.** `claims.json` was revised at
   `e160a72e` (r1, 10:28, pre-dispatch) after `3ca2cf28` (10:14). Every landing inherits r1's
   bytes, so `--freeze 3ca2cf28` fails `FROZENCFG` deterministically (shown below).
2. **r1 also renamed the two graded headings.** The brief's `## 2. The decision table` /
   `## 4. Attested anchors` exist in **0 of 257** knowledge files; r1's
   `## 2. Six design decisions` / `## 3. Attested anchors` are the house shape of the five
   institution entries landed in r82. A seat that follows the brief literally fails `DECISIONS` +
   `ANCHORS` at the r1 freeze and `FROZENCFG` at the 3ca2cf28 freeze — a double bind.
3. **The brief's O tool CLI is not the counter's CLI.** Brief: `... selftest` (positional).
   Counter: `["--selftest"]`. A literal build exits 2 and fails `SELFTEST`.
4. **Claim O's before-text is false as written**: `tools/check-craft-exercise.py:45-80,199-211`
   already applies four ordered sound laws to a proto-lexicon. The honest before is narrower
   ("no rule-set-driven general applier"), and the `BEFORE` leg cannot see the difference.
5. **r84's `SOURCED` leg is a kill-power regression on r83**: it dropped r83's
   `unknown = [s for s in cited if s not in reg]`. Anchors citing fabricated ids now pass.
6. **The frozen row contract is not graded.** `ROWS` reads only cells 7, 8, 10. `source`
   (URL + status + bytes + sha256 + capture), `anchor` (locus), `teaches` are unread.
7. **`DEMO` runs exactly one input, the committed one.** A tool that copies
   `examples/sound-laws/expected.tsv` and prints a canned summary passes every leg.

## 1. Before-state re-derived at `81499ee4`

Method: `git archive 81499ee45b5751d388fefc78583810878de01ecd | tar -x` into a scratch tree, then
the frozen commands verbatim; the registry count uses `accept-d84.py`'s own `ROW_LINE` /
11-cell predicate.

### Claim D

| clause | re-derived | verdict |
|---|---|---|
| 257 files under `corpus/knowledge` | 257 `.md`, 257 files total | TRUE |
| filename sweep `witch|witchcraft|sorcer|malefic` = 0 basenames | 0 | TRUE |
| `grep -rlE '^- topic: .{0,160}\b(witchcraft|sorcery|witch|sorcerer|malefic)'` = 0 files | 0 | TRUE |
| "the word-boundary term set occurs 19 times across 10 files" | **19 occurrences / 10 files** under `\b(witch|witchcraft|sorcery|sorcerer|malefic)\b`; **22 occurrences / 12 files** under `claims.json`'s `surface_re` `\b(witch|witches|witchcraft|sorcer[a-z]*|malefic[a-z]*)\b` | TRUE only for the topic-scan set; the two sets are not the same |
| 837 registry rows | 837 rows, all 11 cells, S001–S913, no duplicates, 76 numbers unused below 913 | TRUE |
| no `- gap filled:` owner for the surface | TRUE as *owner*; one gap-filled line **mentions** it: `myth-symbol/amulets-talismans-apotropaic-marks.md:4` (`witch mark`, as an absence probe) | TRUE with care |
| S914–S917 free | S914–S917 absent at base and at r1 | TRUE |

The 19/10 number is not wrong; it is the **topic-scan** alternation, not the `surface_re`. An entry
that writes "the word-boundary term set occurs 19 times" while grading with `surface_re` can be
falsified with the four extra hits (`sorceress` in `civilizations/kongo-kingdom.md:45`, `sorcery`
in `myth-symbol/binding-speech-complex.md:26,164` and `myth-symbol/color-symbolism.md:22`,
`Sorcerer's` in `myth-symbol/myth-folktale-genres.md:54`, plus the second `witch's` in
`amulets…:72,104`). The entry must name the regex it counted with.

### Claim O

| clause | re-derived | verdict |
|---|---|---|
| `ls-tree … tools examples \| grep -ciE 'sound.?law\|soundchange'` = 0 | 0 | TRUE, regex-brittle |
| `git grep -c SOUNDLAWS <base> -- tools examples reports` = 0 lines | 0 | TRUE |
| `examples/sound-laws/` absent | 0 paths | TRUE |
| `GATE-REGISTRY: 0 missing / 74 registered / 61 instruments / 0 dead` + `INFO: 25 tools without a row` | exact match (ran `tools/check-gate-registry.py --root .` on the base tree) | TRUE |
| "no committed tool applies ordered sound laws to a lexicon" / "can only *check* … never derive" | **FALSE**: `tools/check-craft-exercise.py:45-80` defines `law_l1..law_l4`, `:199-211` computes `out = word; for fn in funcs: out = fn(out)` over the proto-lexicon and compares to the declared derivation, with a reversed-order control | overstated |

The sweep is also blind by construction: the base tree contains
`examples/supplement-opencode-1/sound-change-vs-taboo.json`, and `grep -iE 'sound.?law|soundchange'`
matches neither `sound-change` spelling. A looser `sound|chang` finds it. The defensible before is:
"no committed tool is driven by a **rule set**, none exposes `apply`/`selftest`, and the only law
engine is four laws hardcoded to one exercise (`tools/check-craft-exercise.py:50-80`)". The
`BEFORE` leg (`filename regex` + `SOUNDLAWS` marker) cannot catch the difference, so the report —
not the counter — must carry the precise claim.

## 2. Kill power: landings that satisfy the frozen after-state text but are not the claimed work

### Claim D

I reproduced the frozen leg predicates verbatim on synthetic text (transcript in
`stage/CriticClaims/attack.md`).

| landing | legs it passes | which leg catches it |
|---|---|---|
| **A. stub entry**: ≥16000 bytes of padding, 7 `## ` sections, 6 filler decision rows, 20 filler anchor bullets over 4 ids (`17×S914 + S915 + S916 + S917`), 4 well-formed rows, ids also named in prose | all 10 (`bullets=20 ids=4 malformed=0`) | **none** |
| **B. fabricated provenance**: four 11-cell rows, `status=mined`, `opened=2026-11-04`, `used-by` correct, but `source=x`, `anchor=x`, `teaches=x` (`grew=4 problems=none`) | all 10 | **none** — `ROWS` reads only cells 7, 8, 10; the frozen row contract's fetch facts, locus and `teaches` are ungraded |
| **C. false anchors**: 20 bullets over `S998`, `S999`, `S9910`, `S9911` (nonexistent), with S914–S916 named once in prose | `ANCHORS` + `SOURCED` | **none in r84**; r83's `SOURCED` (`accept-d83.py:158-162`, `unknown = [s for s in cited if s not in reg]`, receipt `cited=6 unknown=none new_cited=4`) would have killed it. r84 dropped the existence check. |
| **D. one-line citation**: "the four rows S914–S917 are opened this round" | — | `LINT` **kills a legitimate landing**: `check-cited-lines` prints `MULTI-ID … S914,S917`. `SOURCED` (≥3 new ids as substrings) and `LINT` (≤1 distinct id per line) pull opposite ways; the entry must put one id per line |
| **E. 259th file**: another seat lands a knowledge file first | all 10 | **none** — no leg counts knowledge files at lands; the "258th" clause is ungraded |

Junk-battery coverage is honest for the three cases it names (`stub-entry`→`ENTRY`,
`anchor-two-ids`→`ANCHORS`, `row-queued`→`ROWS`). It does not test A/B/C/E.

### Claim O

| landing | legs it passes | which leg catches it |
|---|---|---|
| **A. hardcoded example**: `apply` copies `examples/sound-laws/expected.tsv` → `--out`, prints `SOUNDLAWS: 12 words / 6 rules / 12 changes`, writes 12 trace lines cycling the six rule names, `--selftest` prints `SELFTEST: PASS (99 checks)`, the three malformed cases exit 2 | all 8 | **none** — `DEMO` runs only the committed input with `cwd=<work>/tree`, so the expected file is readable; the junk battery's `copy-input` stub does not test copy-the-expected |
| **B. canned selftest**: `print("SELFTEST: PASS (99 checks)")` with no checks | `SELFTEST` | **none** — only rc and the parsed count are read |
| **C. synthetic trace**: correct line count and rule coverage, arbitrary columns 2/4/5 | `DEMO` | **none** — `DEMO` reads only `len(tl)`, `tl.split("\t")[2]`, and `len(tl)==c` |
| **D. literal brief CLI**: `... selftest` positional only | — | `SELFTEST` **kills a correct-per-brief tool**: it runs `["--selftest"]`, argparse exits 2, `n=-1` |
| **E. trace rule = ordinal** | — | `DEMO` kills it (`set(rule_names) <= fired`); the contract only says the column is "rule" |
| **F. `SKILL.md` row that merely names the tool in cell 3** (no command) | `REGISTRY` | only the name is checked |

## 3. Controls

### Do-nothing (`--lands 81499ee4`, `--freeze 3ca2cf28`, existing `--work`)

```
ACCEPT-D-84: FAIL legs=0/10 (refused: lands equals the frozen base -- do-nothing control)
exit=2
ACCEPT-O-84: FAIL legs=0/8 (refused: lands equals the frozen base -- do-nothing control)
exit=2
```

Both refuse before any leg, exit 2. Correct.

### Red-before (`--lands 3ca2cf28`, `--freeze 3ca2cf28`)

```
ACCEPT-D-84
LEG FROZENCFG   PASS freeze 3ca2cf28 lands 3ca2cf28 sha256 d8ee0b974189
LEG BEFORE      PASS entry_at_base=False files=257/257 rows=837/837 owned=none
LEG ENTRY       FAIL entry absent at lands
LEG SECTIONS    FAIL error: [Errno 2] No such file or directory: '<work>/tree/corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md'
LEG DECISIONS   FAIL error: [Errno 2] … same path
LEG ANCHORS     FAIL error: [Errno 2] … same path
LEG LINT        FAIL no CITED-LINES summary: 'CITED_LINES_ERROR no such file or directory: corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md'
LEG ROWS        FAIL rows=837 grew=0 floor=4 problems=['S914 missing', 'S915 missing', 'S916 missing', 'S917 missing']
LEG SOURCED     FAIL error: [Errno 2] … same path
LEG SEPARABLE   FAIL error: no commit touching a claim path in 81499ee4..3ca2cf28
ACCEPT-D-84: FAIL legs=2/10
exit=1
```

```
ACCEPT-O-84
LEG FROZENCFG   PASS freeze 3ca2cf28 lands 3ca2cf28 sha256 d8ee0b974189
LEG BEFORE      PASS tool_at_base=False example_files=0 marker_files=0
LEG TOOL        FAIL tool absent at lands
LEG SELFTEST    FAIL rc=2 checks=-1 floor=20 tail="… can't open file '<work>/tree/tools/apply-sound-laws.py'"
LEG DEMO        FAIL no single summary line (rc=2): "… can't open file '<work>/tree/tools/apply-sound-laws.py'"
LEG NEGATIVE    FAIL cases=3 problems=['missing-rules rc=2 …', 'bad-json rc=2 …', 'empty-from rc=2 …']
LEG REGISTRY    FAIL no row names tools/apply-sound-laws.py
LEG SEPARABLE   FAIL error: no commit touching a claim path in 81499ee4..3ca2cf28
ACCEPT-O-84: FAIL legs=2/8
exit=1
```

### The freeze mismatch (decisive)

`claims.json` blobs: `3ca2cf28` = `9849def442cec2cbcf2f098a9e2ed948237447db`,
`e160a72e` = `de2282df31889d7306db0c593a82f964e8e5912b`. The r1 commit changes exactly three
lines (the `after` sentence and the two heading literals). Grading the r1 tree with the
brief-named freeze:

```
D --lands e160a72e --freeze 3ca2cf28  ->  LEG FROZENCFG FAIL freeze 3ca2cf28 lands e160a72e sha256 ff545df6c108
D --lands e160a72e --freeze e160a72e  ->  LEG FROZENCFG PASS freeze e160a72e lands e160a72e sha256 ff545df6c108
O --lands e160a72e --freeze 3ca2cf28  ->  LEG FROZENCFG FAIL freeze 3ca2cf28 lands e160a72e sha256 ff545df6c108
O --lands e160a72e --freeze e160a72e  ->  LEG FROZENCFG PASS freeze e160a72e lands e160a72e sha256 ff545df6c108
```

Because every landing is a descendant of `e160a72e`, its `claims.json` is r1's; `--freeze
3ca2cf28` can never pass `FROZENCFG`. The operative freeze is `e160a72e`.

House-shape check, base tree: `grep -rl '^## 2\. Six design decisions' corpus/knowledge` = 5
(`culture-material/footwear-codes-terminology.md`, `culture-material/maritime-seafaring-lexicon.md`,
`myth-symbol/guest-right-hospitality-law.md`, `myth-symbol/marriage-alliance-bridewealth.md`,
`myth-symbol/ordeal-judicial-proof-rituals.md`); the same five carry `## 3. Attested anchors`;
`^## 2\. The decision table` and `^## 4\. Attested anchors` = 0. r1 is right; the brief's two
literals are stale.

### Per-claim lands (protocol, not artifact)

r83 receipts (`reports/round-83/telemetry/lands-{d,o,c}83-final.txt`) show three different lands:
D `386e7002`, O `0f088572` (`span_parent=29f4b6a5` = the freeze), C `86f68b5b`
(`span_parent=386e7002` = D's lands). Grading both r84 claims at one shared tip deterministically
fails the earlier claim's `SEPARABLE`: `claim_span` returns the parent of the first own-path commit,
and `foreign` compares that parent with lands — the later claim's paths (D foreign: tool,
`examples/sound-laws/`, `SKILL.md`; O foreign: the entry, `corpus/SOURCES.md`) will have moved.
r84 must follow the r83 precedent: **each counter at its claim's own lands**, and each claim's own
paths complete before the other's first commit.

## 4. The frozen tool contract: where two correct implementations disagree

1. **Resume point after a replacement.** `from="a"`, `to="aa"` on `aa`: resume-after-the-matched-span
   → `aaaa` (2 changes); resume-after-the-emitted-output → `aa` (1 change). Demonstrated. The
   contract's "one left-to-right non-overlapping pass over the current word" forces the first
   (matches are taken on the current word and may not overlap), but it never says where scanning
   resumes after insertion; the second is defensible, and the example — not the contract — becomes
   the authority. `DEMO` pins only `c`.
2. **`#` semantics.** `post=["#"]`, `from="a"` on `t a k a`: boundary-slot reading → `t a k`
   (1 change); context-slot/length-guard reading → `t a k a` (0 changes). Both are natural; I wrote
   the second first and it silently never fired. The contract says only "`#` means the word start
   (pre) or word end (post)"; it never says whether `#` occupies a context slot, nor that it must be
   first (pre) / last (post). A rule with `#` mid-list is either unsatisfiable or an error — the
   contract forces neither.
3. **Trace `index`.** Undefined (pre-change segment index? post-change? character offset?). The
   counter never reads column 2 → unconstrained.
4. **Trace `before`/`after`.** Whole word vs local context; never read → unconstrained.
5. **Trace `rule`.** Name vs ordinal; the counter silently forces the `name` (`set(rule_names) ⊆ fired`),
   the contract says only "rule".
6. **`from`/`to` tokenisation.** Space-separated segment sequences (implied by "segment-tokenised"
   and by `pre`/`post` being lists) vs one segment string. `from: "k a"` has no unique reading.
7. **Identity rules** (`from == to`): "one trace line per change" — 0 or 1 line? Changes `c` and
   "every rule fires".
8. **Missing `pre`/`post`/`to` keys**: error or default? `NEGATIVE` tests only empty `from`,
   a missing file, and non-JSON.
9. **Adjacency**: `pre`/`post` immediately adjacent vs anywhere in the word; the counter cannot tell.

Reading the contract forces, at minimum: segments are space-separated tokens; `from`/`to` are
segment sequences (`to=""` deletes); rules apply in file order; each rule is one non-overlapping
left-to-right pass over the current word resuming after the matched span; `#` is a zero-width
boundary marker. Everything else (trace columns 2/4, `#` placement, identity rules) the contract
leaves open, and the committed example then decides it — a second authority.

## 5. One command that falsifies each after-state

Both were run at `3ca2cf28` and correctly report FALSIFIED (entry/tool absent); they exit 0 only if
every clause holds. Run from the lane root with the claim's lands.

**D** — `bash -c` with the lands as `$1`:

```bash
bash -c 'set -u; R=$(git rev-parse --show-toplevel); REV="$1"; E=corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md; D=$(mktemp -d); trap "rm -rf -- \"$D\"" EXIT; git -C "$R" show "$REV:$E" > "$D/entry.md" || { echo "FALSIFIED: entry absent"; exit 1; }; git -C "$R" show "$REV:corpus/SOURCES.md" > "$D/SOURCES.md"; git -C "$R" show "$REV:tools/check-cited-lines.py" > "$D/lint.py"; python3 - "$D" "$E" "$REV" <<"PY"
import re,sys,subprocess
D,E,REV=sys.argv[1:4]
t=open(D+"/entry.md",encoding="utf-8").read(); src=open(D+"/SOURCES.md",encoding="utf-8").read()
SID=re.compile(r"\bS\d{3,}\b"); ROW=re.compile(r"^ {0,3}\| *S\d{3,} *\|")
def sec(x,h):
    L=x.splitlines()
    try: s=next(i for i,l in enumerate(L) if l.strip()==h)
    except StopIteration: return None
    o=[]
    for l in L[s+1:]:
        if l.startswith("## "): break
        o.append(l)
    return o
def rows(b):
    o=[];h=False
    for l in (b or []):
        s=l.strip()
        if not s.startswith("|"): continue
        c=[v.strip() for v in s.strip("|").split("|")]
        if set("".join(c))<=set("-: "): continue
        if not h: h=True; continue
        o.append(c)
    return o
reg={};n=0
for l in src.splitlines():
    if not ROW.match(l): continue
    n+=1;c=[v.strip() for v in l.strip().strip("|").split("|")]
    if len(c)==11: reg[c[0]]=c
bad=[]
def chk(ok,m):
    if not ok: bad.append(m)
chk(len(t.encode())>=16000,"bytes<16000"); chk(len([l for l in t.splitlines() if l.startswith("## ")])>=7,"sections<7")
chk(len(rows(sec(t,"## 2. Six design decisions")))>=6,"decision rows<6")
blk=sec(t,"## 3. Attested anchors") or []; b=0; ids=set(); badb=0
for l in blk:
    if not l.startswith("- "): continue
    f=SID.findall(l)
    if len(f)!=1: badb+=1; continue
    b+=1; ids.add(f[0])
chk(b>=20 and len(ids)>=4 and badb==0,"anchors=%d ids=%d malformed=%d"%(b,len(ids),badb))
unknown=[s for s in sorted(set(SID.findall(t))) if s not in reg]
chk(not unknown,"unknown ids=%s"%unknown)
new=[s for s in ("S914","S915","S916","S917") if s in reg]
chk(len(new)==4,"new rows=%s"%new); chk(len([s for s in new if s in t])>=3,"cites<3 new rows")
for r in ("S914","S915","S916","S917"):
    c=reg.get(r)
    if not c: bad.append(r+" absent"); continue
    chk(c[7]=="mined",r+" status"); chk(c[8]=="2026-11-04",r+" opened"); chk(E in c[10],r+" used-by")
    chk(bool(re.search(r"https?://",c[1]) and re.search(r"sha256|SHA-256",c[1]) and re.search(r"\d{3}",c[1])),r+" source lacks url/status/bytes/sha256")
    chk(len(c[5])>8 and len(c[6])>20,r+" anchor/teaches thin")
chk(n>=841,"registry=%d<841"%n)
p=subprocess.run([sys.executable,"-B",D+"/lint.py",D+"/entry.md"],capture_output=True,text=True)
m=[l for l in p.stdout.splitlines() if l.startswith("CITED-LINES:")]
chk(p.returncode==0 and bool(m) and m[0].startswith("CITED-LINES: 0 "),"lint rc=%d %r"%(p.returncode,m[:1]))
print("FALSIFIED: "+"; ".join(bad) if bad else "SURVIVES all D after-state clauses")
sys.exit(1 if bad else 0)
PY' _ <lands>
```

**O** — the committed example plus two **held-out** cases (this is the clause `DEMO` never runs):

```bash
bash -c 'set -u; R=$(git rev-parse --show-toplevel); REV="$1"; D=$(mktemp -d); trap "rm -rf -- \"$D\"" EXIT; git -C "$R" show "$REV:tools/apply-sound-laws.py" > "$D/tool.py" || { echo "FALSIFIED: tool absent"; exit 1; }; git -C "$R" archive "$REV" examples/sound-laws | tar -x -C "$D" || { echo "FALSIFIED: example absent"; exit 1; }; python3 -B "$D/tool.py" selftest >/dev/null || { echo "FALSIFIED: positional selftest"; exit 1; }; python3 -B "$D/tool.py" --selftest >/dev/null || { echo "FALSIFIED: --selftest"; exit 1; }; python3 -B "$D/tool.py" apply --rules "$D/examples/sound-laws/rules.json" --input "$D/examples/sound-laws/proto-lexicon.tsv" --out "$D/o.tsv" --trace "$D/t.tsv" >/dev/null || { echo "FALSIFIED: apply"; exit 1; }; cmp -s "$D/o.tsv" "$D/examples/sound-laws/expected.tsv" || { echo "FALSIFIED: example not byte-identical"; exit 1; }; printf "{\"rules\":[{\"name\":\"A\",\"from\":\"a\",\"to\":\"i\",\"pre\":[],\"post\":[]},{\"name\":\"B\",\"from\":\"i\",\"to\":\"u\",\"pre\":[],\"post\":[]}]}" > "$D/r1.json"; printf "held\tb a n a\n" > "$D/w1.tsv"; python3 -B "$D/tool.py" apply --rules "$D/r1.json" --input "$D/w1.tsv" --out "$D/o1.tsv" >/dev/null || { echo "FALSIFIED: held-out ordered refused"; exit 1; }; [ "$(cat "$D/o1.tsv")" = "$(printf "held\tb u n u")" ] || { echo "FALSIFIED: ordered held-out -> $(cat "$D/o1.tsv" | tr "\t" "|")"; exit 1; }; printf "{\"rules\":[{\"name\":\"F\",\"from\":\"a\",\"to\":\"\",\"pre\":[],\"post\":[\"#\"]}]}" > "$D/r2.json"; printf "held\tt a k a\n" > "$D/w2.tsv"; python3 -B "$D/tool.py" apply --rules "$D/r2.json" --input "$D/w2.tsv" --out "$D/o2.tsv" >/dev/null || { echo "FALSIFIED: held-out boundary refused"; exit 1; }; [ "$(cat "$D/o2.tsv")" = "$(printf "held\tt a k")" ] || { echo "FALSIFIED: boundary deletion -> $(cat "$D/o2.tsv" | tr "\t" "|")"; exit 1; }; echo "SURVIVES: unseen rules applied; example byte-identical"' _ <lands>
```

The two held-out expectations (`b u n u`; `t a k`) were verified against a reference applier
implementing the forced reading of §4.

## 6. Smallest safe corrections

| # | defect | smallest safe correction | blocked axis |
|---|---|---|---|
| 1 | freeze/heading double bind | grade with `--freeze e160a72e…` (zero edits) and build `## 2. Six design decisions` / `## 3. Attested anchors`; do **not** also revert `claims.json` | D (blocking) |
| 2 | `selftest` vs `--selftest` | tool accepts both spellings (2 lines); no counter change | O (blocking if the brief is followed literally) |
| 3 | per-claim lands | run each counter at its claim's own lands (r83 precedent); record both revisions in the telemetry | D + O (protocol) |
| 4 | `SOURCED` dropped the unknown-id check | cannot be patched (counter frozen): the reviewer must assert every cited id exists and supports its sentence; record the gap for r85 | D (advisory) |
| 5 | `ROWS` ignores the row contract | reviewer reads cells 1, 5, 6 of S914–S917 against the fetched pages | D (advisory) |
| 6 | hardcoded example / canned selftest / synthetic trace | the tool's own `selftest` must include the two held-out cases above (a held-out case cannot live in the committed example); reviewer reruns §5's O command | O (advisory) |
| 7 | `LINT` × `SOURCED` trap | one id per line, everywhere, including `- verified-at:` and prose; run `check-cited-lines` before landing | D (advisory) |
| 8 | O before-text overstatement | state the before as "no rule-set-driven general applier"; cite `tools/check-craft-exercise.py:45-80,199-211`; never repeat "no committed tool applies ordered sound laws" | O (advisory) |
| 9 | 258th ordinal ungraded | entry's `- verified-at:` records the lands knowledge-file count (258) and the reviewer checks it | D (advisory) |
| 10 | 19/10 vs 22/12 | entry names the regex it counted with | D (calibration) |

No finding asks the round to renegotiate a target: the depth target (a 16 KB institution entry with
four new mined rows) and the operability target (a general, rules-driven applier with a committed
example) stand. What must change is the **invocation** (`--freeze`, per-claim lands), **two literal
headings**, **one CLI spelling**, and the **review checklist** that covers what the counters cannot.
