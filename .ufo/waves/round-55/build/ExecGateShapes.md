# ExecGateShapes — round 55

## Files and behavior

- Implemented the checker at `/fast/scratch/hyaku/kotodama-r55/ExecGateShapes/check-gate-quotes.py`; copied it to `/fast/scratch/hyaku/kotodama-r55/ExecGateShapes/lane/tools/check-gate-quotes.py` in the requested sandbox clone. No source file in the live lane was edited.
- Preserved existing word-count finding details and `GATE_QUOTES` summary. Added indented hard-wrap joining, guillemets, ellipses between spans, `- * S###` rows, escaped straight quotes, and documented whitespace-only tokenization (`mother-in-law` remains one token).
- `doubled-locator` compares the first citation span after the access-date locator separator with text in the locator, including quoted locator titles; it requires a later quote span.
- `truncated-grounds` loads the same-S-id `teaches` cell from the neighboring `corpus/SOURCES.md`, ignores quote delimiters and trailing full stops/whitespace, and reports only a strict prefix. Missing registry files/rows are silent skips.
- New-class findings outside round 54 in the final round-49-through-54 run: **none**. Round 49 and 50 had no findings; rounds 51–53 retained only existing `words=<n>` findings.
- No tools were installed or updated.

## Commands and outputs

Commands below ran from `/fast/scratch/hyaku/kotodama-r55/ExecGateShapes/lane`; each shell wrapper printed the child process's actual status as `EXIT_CODE` and then returned shell status 0. Runs marked superseded are retained to show the iteration history; only the final run is acceptance evidence.

### Superseded first-draft selftest

Command: `python3 -B tools/check-gate-quotes.py --selftest; result=$?; printf 'EXIT_CODE=%s\n' "$result"; exit 0`

Output:
```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS doubled-locator-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-green want=none got=none
SELFTEST: 21/21 pass
EXIT_CODE=0
```

### Superseded first-draft acceptance

Command: `python3 -B reports/round-55/accept-o.py; result=$?; printf 'EXIT_CODE=%s\n' "$result"; exit 0`

Output:
```text
DOUBLED PASS count=13 missing=[] extra=[]
TRUNC PASS count=17 missing=[] extra=[]
NOFALSE PASS stray=[]
EXIT PASS round54=1 adversarial=1
ESCAPE PASS missing=[] extra=[]
KEEP53 PASS exit=1 lines=12 base=12 first_diff=none
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 21/21 pass
EXIT_CODE=0
```

### Superseded first-draft six-lesson scan

Command: `python3 -B tools/check-gate-quotes.py corpus/lessons/round-49.md corpus/lessons/round-50.md corpus/lessons/round-51.md corpus/lessons/round-52.md corpus/lessons/round-53.md corpus/lessons/round-54.md; result=$?; printf 'EXIT_CODE=%s\n' "$result"; exit 0`

Output (this broad one-period heuristic was discarded after the L1 steer; the registry-prefix implementation below is the final behavior):
```text
corpus/lessons/round-51.md:33 S076 words=34
corpus/lessons/round-51.md:36 S079 truncated-grounds
corpus/lessons/round-51.md:38 S081 truncated-grounds
corpus/lessons/round-51.md:39 S082 truncated-grounds
corpus/lessons/round-51.md:43 S086 truncated-grounds
corpus/lessons/round-51.md:44 S087 truncated-grounds
corpus/lessons/round-51.md:67 S110 truncated-grounds
corpus/lessons/round-51.md:68 S111 truncated-grounds
corpus/lessons/round-51.md:78 S121 words=30
corpus/lessons/round-52.md:34 S096 words=23
corpus/lessons/round-52.md:41 S134 truncated-grounds
corpus/lessons/round-52.md:42 S134 truncated-grounds
corpus/lessons/round-52.md:43 S134 truncated-grounds
corpus/lessons/round-52.md:44 S134 truncated-grounds
corpus/lessons/round-52.md:45 S134 truncated-grounds
corpus/lessons/round-52.md:47 S134 truncated-grounds
corpus/lessons/round-52.md:48 S135 truncated-grounds
corpus/lessons/round-52.md:49 S135 truncated-grounds
corpus/lessons/round-52.md:50 S135 truncated-grounds
corpus/lessons/round-52.md:53 S135 truncated-grounds
corpus/lessons/round-52.md:54 S135 truncated-grounds
corpus/lessons/round-52.md:55 S136 truncated-grounds
corpus/lessons/round-52.md:59 S139 words=26
corpus/lessons/round-52.md:62 S139 truncated-grounds
corpus/lessons/round-52.md:63 S139 truncated-grounds
corpus/lessons/round-52.md:66 S140 words=27
corpus/lessons/round-52.md:68 S142 words=34
corpus/lessons/round-52.md:69 S143 truncated-grounds
corpus/lessons/round-52.md:70 S143 truncated-grounds
corpus/lessons/round-52.md:71 S143 truncated-grounds
corpus/lessons/round-52.md:72 S144 truncated-grounds
corpus/lessons/round-52.md:73 S144 truncated-grounds
corpus/lessons/round-52.md:74 S144 truncated-grounds
corpus/lessons/round-52.md:75 S145 truncated-grounds
corpus/lessons/round-52.md:76 S146 truncated-grounds
corpus/lessons/round-52.md:77 S147 truncated-grounds
corpus/lessons/round-52.md:78 S147 truncated-grounds
corpus/lessons/round-52.md:79 S148 truncated-grounds
corpus/lessons/round-52.md:80 S149 truncated-grounds
corpus/lessons/round-52.md:81 S149 truncated-grounds
corpus/lessons/round-52.md:82 S150 truncated-grounds
corpus/lessons/round-52.md:83 S151 truncated-grounds
corpus/lessons/round-52.md:84 S152 truncated-grounds
corpus/lessons/round-52.md:87 S155 words=31
corpus/lessons/round-52.md:92 S157 truncated-grounds
corpus/lessons/round-52.md:93 S158 truncated-grounds
corpus/lessons/round-52.md:94 S159 words=30
corpus/lessons/round-52.md:94 S159 truncated-grounds
corpus/lessons/round-52.md:97 S162 truncated-grounds
corpus/lessons/round-52.md:98 S163 truncated-grounds
corpus/lessons/round-52.md:99 S164 words=29
corpus/lessons/round-52.md:99 S164 truncated-grounds
corpus/lessons/round-52.md:100 S165 truncated-grounds
corpus/lessons/round-52.md:101 S166 truncated-grounds
corpus/lessons/round-52.md:102 S167 truncated-grounds
corpus/lessons/round-52.md:103 S168 truncated-grounds
corpus/lessons/round-52.md:104 S169 truncated-grounds
corpus/lessons/round-52.md:105 S170 truncated-grounds
corpus/lessons/round-52.md:106 S171 truncated-grounds
corpus/lessons/round-52.md:107 S172 truncated-grounds
corpus/lessons/round-52.md:108 S172 truncated-grounds
corpus/lessons/round-52.md:109 S173 truncated-grounds
corpus/lessons/round-52.md:110 S174 truncated-grounds
corpus/lessons/round-52.md:111 S175 truncated-grounds
corpus/lessons/round-52.md:112 S176 truncated-grounds
corpus/lessons/round-52.md:113 S177 truncated-grounds
corpus/lessons/round-52.md:114 S178 truncated-grounds
corpus/lessons/round-52.md:116 S179 truncated-grounds
corpus/lessons/round-52.md:117 S180 truncated-grounds
corpus/lessons/round-53.md:40 S187 truncated-grounds
corpus/lessons/round-53.md:41 S187 truncated-grounds
corpus/lessons/round-53.md:42 S187 words=28
corpus/lessons/round-53.md:42 S187 truncated-grounds
corpus/lessons/round-53.md:43 S188 truncated-grounds
corpus/lessons/round-53.md:45 S188 truncated-grounds
corpus/lessons/round-53.md:46 S189 truncated-grounds
corpus/lessons/round-53.md:47 S189 truncated-grounds
corpus/lessons/round-53.md:49 S189 words=28
corpus/lessons/round-53.md:49 S189 truncated-grounds
corpus/lessons/round-53.md:50 S189 truncated-grounds
corpus/lessons/round-53.md:52 S190 truncated-grounds
corpus/lessons/round-53.md:53 S190 truncated-grounds
corpus/lessons/round-53.md:55 S190 truncated-grounds
corpus/lessons/round-53.md:56 S191 truncated-grounds
corpus/lessons/round-53.md:57 S192 truncated-grounds
corpus/lessons/round-53.md:58 S192 words=40
corpus/lessons/round-53.md:58 S192 truncated-grounds
corpus/lessons/round-53.md:59 S192 truncated-grounds
corpus/lessons/round-53.md:60 S193 truncated-grounds
corpus/lessons/round-53.md:61 S194 truncated-grounds
corpus/lessons/round-53.md:62 S194 words=28
corpus/lessons/round-53.md:62 S194 truncated-grounds
corpus/lessons/round-53.md:63 S194 truncated-grounds
corpus/lessons/round-53.md:64 S195 truncated-grounds
corpus/lessons/round-53.md:84 S200 words=27
corpus/lessons/round-53.md:84 S200 truncated-grounds
corpus/lessons/round-53.md:85 S200 truncated-grounds
corpus/lessons/round-53.md:86 S200 truncated-grounds
corpus/lessons/round-53.md:87 S200 truncated-grounds
corpus/lessons/round-53.md:88 S201 truncated-grounds
corpus/lessons/round-53.md:89 S201 truncated-grounds
corpus/lessons/round-53.md:90 S201 truncated-grounds
corpus/lessons/round-53.md:91 S201 truncated-grounds
corpus/lessons/round-53.md:92 S202 truncated-grounds
corpus/lessons/round-53.md:93 S202 truncated-grounds
corpus/lessons/round-53.md:94 S202 truncated-grounds
corpus/lessons/round-53.md:95 S202 truncated-grounds
corpus/lessons/round-53.md:96 S202 truncated-grounds
corpus/lessons/round-53.md:97 S202 truncated-grounds
corpus/lessons/round-53.md:98 S202 truncated-grounds
corpus/lessons/round-53.md:99 S203 truncated-grounds
corpus/lessons/round-53.md:100 S203 truncated-grounds
corpus/lessons/round-53.md:101 S203 truncated-grounds
corpus/lessons/round-53.md:102 S203 truncated-grounds
corpus/lessons/round-53.md:103 S203 truncated-grounds
corpus/lessons/round-53.md:107 S204 truncated-grounds
corpus/lessons/round-53.md:108 S204 truncated-grounds
corpus/lessons/round-53.md:109 S205 words=36
corpus/lessons/round-53.md:110 S205 words=30
corpus/lessons/round-53.md:110 S205 truncated-grounds
corpus/lessons/round-53.md:111 S205 words=26
corpus/lessons/round-53.md:111 S205 truncated-grounds
corpus/lessons/round-53.md:113 S207 truncated-grounds
corpus/lessons/round-53.md:114 S208 truncated-grounds
corpus/lessons/round-53.md:115 S208 truncated-grounds
corpus/lessons/round-53.md:116 S208 truncated-grounds
corpus/lessons/round-53.md:117 S209 truncated-grounds
corpus/lessons/round-53.md:118 S210 truncated-grounds
corpus/lessons/round-53.md:119 S211 truncated-grounds
corpus/lessons/round-53.md:120 S212 truncated-grounds
corpus/lessons/round-53.md:121 S212 truncated-grounds
corpus/lessons/round-53.md:122 S212 truncated-grounds
corpus/lessons/round-53.md:123 S212 truncated-grounds
corpus/lessons/round-53.md:124 S212 truncated-grounds
corpus/lessons/round-53.md:125 S212 truncated-grounds
corpus/lessons/round-53.md:127 S213 truncated-grounds
corpus/lessons/round-53.md:128 S214 words=27
corpus/lessons/round-53.md:128 S214 truncated-grounds
corpus/lessons/round-53.md:129 S215 truncated-grounds
corpus/lessons/round-53.md:130 S215 truncated-grounds
corpus/lessons/round-53.md:131 S215 truncated-grounds
corpus/lessons/round-53.md:132 S216 truncated-grounds
corpus/lessons/round-53.md:133 S217 words=11
corpus/lessons/round-53.md:133 S217 truncated-grounds
corpus/lessons/round-53.md:134 S218 truncated-grounds
corpus/lessons/round-53.md:135 S218 truncated-grounds
corpus/lessons/round-53.md:136 S219 truncated-grounds
corpus/lessons/round-53.md:137 S220 truncated-grounds
corpus/lessons/round-53.md:138 S220 truncated-grounds
corpus/lessons/round-53.md:139 S220 truncated-grounds
corpus/lessons/round-53.md:140 S220 truncated-grounds
corpus/lessons/round-53.md:142 S221 truncated-grounds
corpus/lessons/round-53.md:143 S222 truncated-grounds
corpus/lessons/round-53.md:144 S222 truncated-grounds
corpus/lessons/round-53.md:145 S222 truncated-grounds
corpus/lessons/round-53.md:148 S223 truncated-grounds
corpus/lessons/round-53.md:151 S223 truncated-grounds
corpus/lessons/round-53.md:152 S223 truncated-grounds
corpus/lessons/round-53.md:153 S223 truncated-grounds
corpus/lessons/round-53.md:154 S223 truncated-grounds
corpus/lessons/round-53.md:155 S223 truncated-grounds
corpus/lessons/round-53.md:156 S223 truncated-grounds
corpus/lessons/round-53.md:158 S223 truncated-grounds
corpus/lessons/round-53.md:159 S223 truncated-grounds
corpus/lessons/round-53.md:160 S224 words=28
corpus/lessons/round-53.md:160 S224 truncated-grounds
corpus/lessons/round-53.md:161 S225 truncated-grounds
corpus/lessons/round-53.md:162 S225 truncated-grounds
corpus/lessons/round-53.md:163 S226 truncated-grounds
corpus/lessons/round-53.md:164 S227 truncated-grounds
corpus/lessons/round-53.md:165 S227 truncated-grounds
corpus/lessons/round-53.md:166 S227 truncated-grounds
corpus/lessons/round-53.md:167 S228 truncated-grounds
corpus/lessons/round-53.md:168 S228 truncated-grounds
corpus/lessons/round-53.md:169 S228 truncated-grounds
corpus/lessons/round-53.md:170 S229 truncated-grounds
corpus/lessons/round-53.md:171 S229 truncated-grounds
corpus/lessons/round-53.md:177 S233 truncated-grounds
corpus/lessons/round-53.md:178 S234 truncated-grounds
corpus/lessons/round-53.md:179 S234 truncated-grounds
corpus/lessons/round-53.md:180 S235 truncated-grounds
corpus/lessons/round-53.md:181 S236 words=29
corpus/lessons/round-53.md:181 S236 truncated-grounds
corpus/lessons/round-53.md:182 S237 truncated-grounds
corpus/lessons/round-53.md:183 S238 truncated-grounds
corpus/lessons/round-54.md:23 S239 doubled-locator
corpus/lessons/round-54.md:24 S240 doubled-locator
corpus/lessons/round-54.md:25 S241 truncated-grounds
corpus/lessons/round-54.md:26 S242 truncated-grounds
corpus/lessons/round-54.md:27 S243 doubled-locator
corpus/lessons/round-54.md:28 S244 truncated-grounds
corpus/lessons/round-54.md:30 S246 doubled-locator
corpus/lessons/round-54.md:32 S248 truncated-grounds
corpus/lessons/round-54.md:33 S249 doubled-locator
corpus/lessons/round-54.md:34 S250 truncated-grounds
corpus/lessons/round-54.md:35 S251 truncated-grounds
corpus/lessons/round-54.md:37 S253 truncated-grounds
corpus/lessons/round-54.md:39 S255 truncated-grounds
corpus/lessons/round-54.md:43 S259 doubled-locator
corpus/lessons/round-54.md:43 S259 truncated-grounds
corpus/lessons/round-54.md:46 S262 doubled-locator
corpus/lessons/round-54.md:47 S263 truncated-grounds
corpus/lessons/round-54.md:48 S264 truncated-grounds
corpus/lessons/round-54.md:49 S265 doubled-locator
corpus/lessons/round-54.md:49 S265 truncated-grounds
corpus/lessons/round-54.md:50 S266 doubled-locator
corpus/lessons/round-54.md:51 S267 doubled-locator
corpus/lessons/round-54.md:52 S268 doubled-locator
corpus/lessons/round-54.md:59 S275 doubled-locator
corpus/lessons/round-54.md:59 S275 truncated-grounds
corpus/lessons/round-54.md:60 S276 truncated-grounds
corpus/lessons/round-54.md:61 S277 doubled-locator
corpus/lessons/round-54.md:61 S277 truncated-grounds
corpus/lessons/round-54.md:62 S278 truncated-grounds
corpus/lessons/round-54.md:63 S279 truncated-grounds
GATE_QUOTES: 215 findings
EXIT_CODE=1
```

### Registry-backed draft run with missing import (superseded failure)

Command: `python3 -B tools/check-gate-quotes.py --selftest; result=$?; printf 'EXIT_CODE=%s\n' "$result"; exit 0`

Output:
```text
Traceback (most recent call last):
  File "/fast/scratch/hyaku/kotodama-r55/ExecGateShapes/lane/tools/check-gate-quotes.py", line 401, in <module>
    sys.exit(main())
    ^^^
NameError: name 'sys' is not defined. Did you forget to import 'sys'?
EXIT_CODE=1
```

Command: `python3 -B reports/round-55/accept-o.py; result=$?; printf 'EXIT_CODE=%s\n' "$result"; exit 0`

Output:
```text
DOUBLED FAIL count=0 missing=['S239', 'S240', 'S243', 'S246', 'S249', 'S259', 'S262', 'S265', 'S266', 'S267', 'S268', 'S275', 'S277'] extra=[]
TRUNC FAIL count=0 missing=['S241', 'S242', 'S244', 'S248', 'S250', 'S251', 'S253', 'S255', 'S259', 'S263', 'S264', 'S265', 'S275', 'S276', 'S277', 'S278', 'S279'] extra=[]
NOFALSE PASS stray=[]
EXIT PASS round54=1 adversarial=1
ESCAPE FAIL missing=[('S901', 'words=26'), ('S902', 'words=26'), ('S904', 'words=22'), ('S905', 'words=26')] extra=[]
KEEP53 FAIL exit=1 lines=0 base=12 first_diff='<none>' vs 'corpus/lessons/round-53.md:42 S187 words=28'
FORMAT FAIL malformed_runs=['round54', 'adversarial', 'round53']
SELFTEST FAIL exit=1 ?
EXIT_CODE=1
```

Command: `python3 -B tools/check-gate-quotes.py corpus/lessons/round-49.md corpus/lessons/round-50.md corpus/lessons/round-51.md corpus/lessons/round-52.md corpus/lessons/round-53.md corpus/lessons/round-54.md; result=$?; printf 'EXIT_CODE=%s\n' "$result"; exit 0`

Output:
```text
Traceback (most recent call last):
  File "/fast/scratch/hyaku/kotodama-r55/ExecGateShapes/lane/tools/check-gate-quotes.py", line 401, in <module>
    sys.exit(main())
    ^^^
NameError: name 'sys' is not defined. Did you forget to import 'sys'?
EXIT_CODE=1
```

### Registry-backed run before edge-case refinements (superseded)

Command: `python3 -B tools/check-gate-quotes.py --selftest; result=$?; printf 'EXIT_CODE=%s\n' "$result"; exit 0`

Output:
```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
FAIL doubled-locator-double-quoted-red want=doubled-locator got=none
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
SELFTEST: 23/24 pass
EXIT_CODE=1
```

Command: `python3 -B reports/round-55/accept-o.py; result=$?; printf 'EXIT_CODE=%s\n' "$result"; exit 0`

Output:
```text
DOUBLED PASS count=13 missing=[] extra=[]
TRUNC FAIL count=15 missing=['S263', 'S279'] extra=[]
NOFALSE PASS stray=[]
EXIT PASS round54=1 adversarial=1
ESCAPE PASS missing=[] extra=[]
KEEP53 PASS exit=1 lines=12 base=12 first_diff=none
FORMAT PASS malformed_runs=[]
SELFTEST FAIL exit=1 SELFTEST: 23/24 pass
EXIT_CODE=1
```

Command: `python3 -B tools/check-gate-quotes.py corpus/lessons/round-49.md corpus/lessons/round-50.md corpus/lessons/round-51.md corpus/lessons/round-52.md corpus/lessons/round-53.md corpus/lessons/round-54.md; result=$?; printf 'EXIT_CODE=%s\n' "$result"; exit 0`

Output:
```text
corpus/lessons/round-51.md:33 S076 words=34
corpus/lessons/round-51.md:78 S121 words=30
corpus/lessons/round-52.md:34 S096 words=23
corpus/lessons/round-52.md:59 S139 words=26
corpus/lessons/round-52.md:66 S140 words=27
corpus/lessons/round-52.md:68 S142 words=34
corpus/lessons/round-52.md:87 S155 words=31
corpus/lessons/round-52.md:94 S159 words=30
corpus/lessons/round-52.md:99 S164 words=29
corpus/lessons/round-53.md:42 S187 words=28
corpus/lessons/round-53.md:49 S189 words=28
corpus/lessons/round-53.md:58 S192 words=40
corpus/lessons/round-53.md:62 S194 words=28
corpus/lessons/round-53.md:84 S200 words=27
corpus/lessons/round-53.md:109 S205 words=36
corpus/lessons/round-53.md:110 S205 words=30
corpus/lessons/round-53.md:111 S205 words=26
corpus/lessons/round-53.md:128 S214 words=27
corpus/lessons/round-53.md:133 S217 words=11
corpus/lessons/round-53.md:160 S224 words=28
corpus/lessons/round-53.md:181 S236 words=29
corpus/lessons/round-54.md:23 S239 doubled-locator
corpus/lessons/round-54.md:24 S240 doubled-locator
corpus/lessons/round-54.md:25 S241 truncated-grounds
corpus/lessons/round-54.md:26 S242 truncated-grounds
corpus/lessons/round-54.md:27 S243 doubled-locator
corpus/lessons/round-54.md:28 S244 truncated-grounds
corpus/lessons/round-54.md:30 S246 doubled-locator
corpus/lessons/round-54.md:32 S248 truncated-grounds
corpus/lessons/round-54.md:33 S249 doubled-locator
corpus/lessons/round-54.md:34 S250 truncated-grounds
corpus/lessons/round-54.md:35 S251 truncated-grounds
corpus/lessons/round-54.md:37 S253 truncated-grounds
corpus/lessons/round-54.md:39 S255 truncated-grounds
corpus/lessons/round-54.md:43 S259 doubled-locator
corpus/lessons/round-54.md:43 S259 truncated-grounds
corpus/lessons/round-54.md:46 S262 doubled-locator
corpus/lessons/round-54.md:49 S265 doubled-locator
corpus/lessons/round-54.md:49 S265 truncated-grounds
corpus/lessons/round-54.md:50 S266 doubled-locator
corpus/lessons/round-54.md:51 S267 doubled-locator
corpus/lessons/round-54.md:52 S268 doubled-locator
corpus/lessons/round-54.md:59 S275 doubled-locator
corpus/lessons/round-54.md:59 S275 truncated-grounds
corpus/lessons/round-54.md:60 S276 truncated-grounds
corpus/lessons/round-54.md:61 S277 doubled-locator
corpus/lessons/round-54.md:61 S277 truncated-grounds
corpus/lessons/round-54.md:62 S278 truncated-grounds
GATE_QUOTES: 49 findings
EXIT_CODE=1
```

### Final requested selftest

Command: `python3 -B tools/check-gate-quotes.py --selftest; result=$?; printf 'EXIT_CODE=%s\n' "$result"; exit 0`

Output:
```text
PASS short-quote want=0 got=0
PASS exactly-25 want=0 got=0
PASS 26-words want=1 got=1
PASS curly-26-words want=1 got=1
PASS anchor-join-27 want=1 got=1
PASS two-separate-quotes want=0 got=0
PASS ellipsis-joined want=1 got=1
PASS leading-ellipsis want=0 got=0
PASS not-a-row want=0 got=0
PASS outside-the-gate-section want=0 got=0
PASS row-in-another-section want=0 got=0
PASS no-gate-section want=None got=None
PASS hard-wrapped-26 want=1 got=1
PASS guillemets-26 want=1 got=1
PASS ellipsis-between-spans want=1 got=1
PASS star-bullet-26 want=1 got=1
PASS hyphenated-whitespace-25 want=0 got=0
PASS doubled-locator-single-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-double-quoted-red want=doubled-locator got=doubled-locator
PASS doubled-locator-green want=none got=none
PASS doubled-locator-s273-escaped-green want=none got=none
PASS truncated-grounds-red want=truncated-grounds got=truncated-grounds
PASS truncated-grounds-whole-single-stop-green want=none got=none
PASS truncated-grounds-double-stop-green want=none got=none
SELFTEST: 24/24 pass
EXIT_CODE=0
```

### Final requested acceptance

Command: `python3 -B reports/round-55/accept-o.py; result=$?; printf 'EXIT_CODE=%s\n' "$result"; exit 0`

Output:
```text
DOUBLED PASS count=13 missing=[] extra=[]
TRUNC PASS count=17 missing=[] extra=[]
NOFALSE PASS stray=[]
EXIT PASS round54=1 adversarial=1
ESCAPE PASS missing=[] extra=[]
KEEP53 PASS exit=1 lines=12 base=12 first_diff=none
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 24/24 pass
EXIT_CODE=0
```

### Final requested six-lesson scan

Command: `python3 -B tools/check-gate-quotes.py corpus/lessons/round-49.md corpus/lessons/round-50.md corpus/lessons/round-51.md corpus/lessons/round-52.md corpus/lessons/round-53.md corpus/lessons/round-54.md; result=$?; printf 'EXIT_CODE=%s\n' "$result"; exit 0`

Output:
```text
corpus/lessons/round-51.md:33 S076 words=34
corpus/lessons/round-51.md:78 S121 words=30
corpus/lessons/round-52.md:34 S096 words=23
corpus/lessons/round-52.md:59 S139 words=26
corpus/lessons/round-52.md:66 S140 words=27
corpus/lessons/round-52.md:68 S142 words=34
corpus/lessons/round-52.md:87 S155 words=31
corpus/lessons/round-52.md:94 S159 words=30
corpus/lessons/round-52.md:99 S164 words=29
corpus/lessons/round-53.md:42 S187 words=28
corpus/lessons/round-53.md:49 S189 words=28
corpus/lessons/round-53.md:58 S192 words=40
corpus/lessons/round-53.md:62 S194 words=28
corpus/lessons/round-53.md:84 S200 words=27
corpus/lessons/round-53.md:109 S205 words=36
corpus/lessons/round-53.md:110 S205 words=30
corpus/lessons/round-53.md:111 S205 words=26
corpus/lessons/round-53.md:128 S214 words=27
corpus/lessons/round-53.md:133 S217 words=11
corpus/lessons/round-53.md:160 S224 words=28
corpus/lessons/round-53.md:181 S236 words=29
corpus/lessons/round-54.md:23 S239 doubled-locator
corpus/lessons/round-54.md:24 S240 doubled-locator
corpus/lessons/round-54.md:25 S241 truncated-grounds
corpus/lessons/round-54.md:26 S242 truncated-grounds
corpus/lessons/round-54.md:27 S243 doubled-locator
corpus/lessons/round-54.md:28 S244 truncated-grounds
corpus/lessons/round-54.md:30 S246 doubled-locator
corpus/lessons/round-54.md:32 S248 truncated-grounds
corpus/lessons/round-54.md:33 S249 doubled-locator
corpus/lessons/round-54.md:34 S250 truncated-grounds
corpus/lessons/round-54.md:35 S251 truncated-grounds
corpus/lessons/round-54.md:37 S253 truncated-grounds
corpus/lessons/round-54.md:39 S255 truncated-grounds
corpus/lessons/round-54.md:43 S259 doubled-locator
corpus/lessons/round-54.md:43 S259 truncated-grounds
corpus/lessons/round-54.md:46 S262 doubled-locator
corpus/lessons/round-54.md:47 S263 truncated-grounds
corpus/lessons/round-54.md:48 S264 truncated-grounds
corpus/lessons/round-54.md:49 S265 doubled-locator
corpus/lessons/round-54.md:49 S265 truncated-grounds
corpus/lessons/round-54.md:50 S266 doubled-locator
corpus/lessons/round-54.md:51 S267 doubled-locator
corpus/lessons/round-54.md:52 S268 doubled-locator
corpus/lessons/round-54.md:59 S275 doubled-locator
corpus/lessons/round-54.md:59 S275 truncated-grounds
corpus/lessons/round-54.md:60 S276 truncated-grounds
corpus/lessons/round-54.md:61 S277 doubled-locator
corpus/lessons/round-54.md:61 S277 truncated-grounds
corpus/lessons/round-54.md:62 S278 truncated-grounds
corpus/lessons/round-54.md:63 S279 truncated-grounds
GATE_QUOTES: 51 findings
EXIT_CODE=1
```

### Tool-call diagnostics

These two kernel diagnostics were not shell subprocesses and therefore have no process exit code.

JavaScript cell:
```js
const source = await read("/fast/scratch/hyaku/kotodama-r55/ExecGateShapes/check-gate-quotes.py");
log(JSON.stringify({type: typeof source, keys: source && Object.keys(source), sample: String(source).slice(0,80)}));
```
Output: `(no output)`. Reported the missing output through `xd://report_issue`.

Python cell:
```python
import re
line = '- S900 — URL — accessed 2026-10-22 — "Section", ¶1: "Section", ¶1: "real".\n'
quote = re.compile(r'"(?:\\.|[^"\\\n])*"|“[^“”\n]*”|«[^«»\n]*»')
accessed = re.search(r' — accessed \d{4}-\d{2}-\d{2} — ', line)
spans = [(m.start(), m.end(), m.group(0)[1:-1]) for m in quote.finditer(line) if m.start() >= accessed.end()]
before = line[accessed.end():spans[0][0]]
locator = before.rsplit(': ', 1)[0]
print(repr(before), repr(locator), spans, spans[0][2].strip() in locator)
```
Output:
```text
'' '' [(37, 46, 'Section'), (52, 61, 'Section'), (67, 73, 'real')] False
```

## Final checker source

Source path: `/fast/scratch/hyaku/kotodama-r55/ExecGateShapes/check-gate-quotes.py`.

```python
#!/usr/bin/env python3
"""Gate quote-cap check for corpus lessons (round 54, routed defect repair).

Round 53's `## Gate` section carried five rows whose quoted material ran to
26-36 words per line because a quote fragment was joined to another quoted
fragment on the same line (the round-53 verifier spot-check, routed defect 3:
"five round-53 `## Gate` lines joined quote fragments so the quoted words per
line reached 26-36, and no check caught it"). No tool in `tools/` looked at
the length of a Gate quotation, so the defect survived the round-53 gate.

This tool reads the `## Gate` section of a lesson and reports every row
whose quoted material breaks the lane's 25-word quotation cap.

What it reads
  * Only the `## Gate` section of each file: from the `## Gate` heading up to
    (not including) the next `## ` heading. `### ` sub-headings stay inside the
    section; nothing outside it is read.
  * Only `- S### ` rows inside that section, including `- * S### ` rows.
    Indented continuation lines are joined to the row before its quotes are checked.

How a quotation is found
  * Quoted spans are straight `"..."`, curly `“...”`, or guillemet `«...»`
    pairs. The spans are taken left to right and never overlap: a straight pair
    is preferred when one starts there, so a straight span that contains curly
    quotes is read whole rather than cut in two.
  * Spans on one row are grouped into *runs*. A run is a maximal group of
    consecutive spans with nothing but punctuation and whitespace between
    them (no letter, digit or underscore). A run is what a reader receives as
    one continuous quotation; two spans separated by prose ("... .
    Geography paragraph, line 82: ...") are two quotations, not one.

Word count rule
  * A run's word count is the sum over its spans of
    `len(span_text.split())`: the text between quotation marks is split on
    whitespace and every non-empty token counts as one word. Thus `mother-in-law`
    is one token, not three. Punctuation-only tokens count ("(39%)" is one word)
    and an ellipsis token counts as one word. No stemming, de-duplication, or
    punctuation stripping.

  * `over-cap` reports a run with more than 25 words.
  * `ellipsis-joined` reports an ellipsis joining fragments inside a span or
    between spans of one run; a leading or trailing omission marker is not
    reported.
  * `doubled-locator` reports a first cited span whose text also appears in the
    locator after the `accessed <date> — ` field, when another quoted span
    follows. This catches repeated single- or double-quoted locator text without
    mistaking escaped quotes inside one span for a repeated locator.
  * `truncated-grounds` reports Grounds text that is a proper prefix (shorter,
    not equal) of the same S-id's registry `teaches` cell, ignoring quote
    delimiters and trailing full stops or whitespace. Missing registry files or
    rows are skipped. A complete Grounds sentence, including one ending in a
    single full stop, is not reported.
  * A row is reported once per offending run and once per new shape; if a run
    has two quote findings, the over-cap count takes precedence.

Usage:
  python3 -B check-gate-quotes.py <lesson.md>...
  python3 -B check-gate-quotes.py --selftest

Output: one line per finding on stdout, then a summary line. Existing quote
findings retain their original detail; shape findings use their class name.
  <path>:<line> <S-id> words=<n> | doubled-locator | truncated-grounds
Exit codes: 0 no findings; 1 findings; 2 could not evaluate (a path is
missing or unreadable, a file has no `## Gate` section, or no path was
given; the reason goes to stderr as `GATE_QUOTES_ERROR:`). Read-only, Python
3 standard library only, no network.
"""

import argparse
import os
import re
import sys

# The lane's quotation cap for a Gate quote.
MAX_WORDS = 25
# `## Gate` opens the section; the next `## ` heading closes it.
GATE_HEADING = re.compile(r"^##\s+Gate\b")
NEXT_H2 = re.compile(r"^##\s")
# A Gate row: `- S187 — https://...`.
ROW = re.compile(r"^-\s+(?:\*\s+)?(S\d+)\b")
# A quoted span: straight, curly, or guillemet quote pairs.
QUOTE = re.compile(r'"(?:\\.|[^"\\\n])*"|“[^“”\n]*”|«[^«»\n]*»')
# Any letter, digit or underscore: prose between two spans breaks a run.
WORDISH = re.compile(r"[\w]", re.UNICODE)
# An ellipsis: the single character or three dots.
ELLIPSIS = re.compile(r"…|\.\.\.")


def gate_section(text):
    """The `## Gate` section as [(line_number, line)], or None if absent."""
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if GATE_HEADING.match(line):
            start = index + 1
            break
    if start is None:
        return None
    body = []
    for index in range(start, len(lines)):
        if NEXT_H2.match(lines[index]):
            break
        body.append((index + 1, lines[index]))
    return body


def quoted_spans(line):
    """Non-overlapping quoted spans as (start, end, inner text)."""
    return [(m.start(), m.end(), m.group(0)[1:-1]) for m in QUOTE.finditer(line)]


def quote_run_details(line):
    """Quoted spans grouped by punctuation-only gaps, with gap ellipses noted."""
    runs = []
    current = []
    previous_end = None
    joined_ellipsis = False
    for start, end, text in quoted_spans(line):
        if previous_end is not None:
            gap = line[previous_end:start]
            if WORDISH.search(gap):
                runs.append((current, joined_ellipsis))
                current = []
                joined_ellipsis = False
            elif ELLIPSIS.search(gap):
                joined_ellipsis = True
        current.append(text)
        previous_end = end
    if current:
        runs.append((current, joined_ellipsis))
    return runs


def quote_runs(line):
    """Quoted spans of one line grouped into runs of one continuous quotation."""
    return [run for run, _ in quote_run_details(line)]


def run_words(run):
    """Word count of a run: whitespace split of each span's inner text."""
    return sum(len(text.split()) for text in run)


def ellipsis_joins(text):
    """True when an ellipsis inside one span joins two fragments."""
    for match in ELLIPSIS.finditer(text):
        if text[:match.start()].strip() and text[match.end():].strip():
            return True
    return False


def registry_teaches(path):
    """Read source teaches cells from the SOURCES.md beside a lesson corpus."""
    source_path = os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(path)), "..", "SOURCES.md"))
    try:
        with open(source_path, "r", encoding="utf-8") as handle:
            lines = handle.readlines()
    except (OSError, UnicodeError):
        return {}
    teaches = {}
    for line in lines:
        if not line.startswith("| S"):
            continue
        cells = line.rstrip("\r\n").split("|")
        if len(cells) != 13:
            continue
        s_id = cells[1].strip()
        if re.fullmatch(r"S\d+", s_id):
            teaches[s_id] = cells[7].strip()
    return teaches


def doubled_locator(line):
    """True when the first cited span repeats text from its accessed locator."""
    accessed = re.search(r" — accessed \d{4}-\d{2}-\d{2} — ", line)
    if accessed is None:
        return False
    spans = [span for span in quoted_spans(line) if span[0] >= accessed.end()]
    quote_index = None
    locator = ""
    for index, span in enumerate(spans):
        before = line[accessed.end():span[0]]
        if re.search(r":\s+$", before):
            quote_index = index
            locator = before.rsplit(":", 1)[0]
            break
    if quote_index is None or quote_index + 1 >= len(spans):
        return False
    quoted_title = spans[quote_index][2].strip()
    return bool(quoted_title) and quoted_title in locator


def comparable_teaches(text):
    """Drop quote delimiters and trailing full stops/whitespace for comparison."""
    return re.sub(r'["“”«»]', "", text).rstrip().rstrip(".").rstrip()


def truncated_grounds(line, s_id, teaches):
    """True when Grounds is an incomplete prefix of its registry teaches cell."""
    source_teaches = teaches.get(s_id)
    if not source_teaches:
        return False
    match = re.search(r"\bGrounds:\s*(.*?)\. Seat:", line)
    if match is None:
        return False
    grounds = comparable_teaches(match.group(1))
    source_teaches = comparable_teaches(source_teaches)
    return bool(grounds and len(grounds) < len(source_teaches)
                and source_teaches.startswith(grounds))


def scan_line(line, number, teaches=None):
    """Findings on a logical row as (line_number, s_id, words, reason) tuples."""
    row = ROW.match(line)
    if not row:
        return []
    s_id = row.group(1)
    teaches = teaches or {}
    findings = []
    for run, gap_ellipsis in quote_run_details(line):
        words = run_words(run)
        if words > MAX_WORDS:
            findings.append((number, s_id, words, "over-cap"))
        elif gap_ellipsis or any(ellipsis_joins(text) for text in run):
            findings.append((number, s_id, words, "ellipsis-joined"))
    if doubled_locator(line):
        findings.append((number, s_id, 0, "doubled-locator"))
    if truncated_grounds(line, s_id, teaches):
        findings.append((number, s_id, 0, "truncated-grounds"))
    return findings


def gate_rows(section):
    """Gate rows with their indented physical continuation lines joined."""
    rows = []
    number = None
    logical_line = None
    for line_number, line in section:
        if ROW.match(line):
            if logical_line is not None:
                rows.append((number, logical_line))
            number = line_number
            logical_line = line
        elif logical_line is not None and line[:1].isspace() and line.strip():
            logical_line += " " + line.strip()
        elif logical_line is not None:
            rows.append((number, logical_line))
            number = None
            logical_line = None
    if logical_line is not None:
        rows.append((number, logical_line))
    return rows


def scan_text(text, teaches=None):
    """Findings in a whole document as (line_number, s_id, words, reason)."""
    section = gate_section(text)
    if section is None:
        return None
    findings = []
    for number, line in gate_rows(section):
        findings.extend(scan_line(line, number, teaches))
    return findings


def check(paths):
    """Findings per path as (path, findings); a path that cannot be read is
    reported with findings None."""
    results = []
    for path in paths:
        try:
            with open(path, "r", encoding="utf-8") as handle:
                text = handle.read()
        except OSError as exc:
            results.append((path, None, "unreadable: %s" % exc.strerror))
            continue
        findings = scan_text(text, registry_teaches(path))
        if findings is None:
            results.append((path, None, "no `## Gate` section"))
            continue
        results.append((path, findings, None))
    return results


def run(paths):
    """Print the findings and return the exit code."""
    if not paths:
        print("GATE_QUOTES_ERROR: no lesson file given", file=sys.stderr)
        return 2
    results = check(paths)
    errors = 0
    total = 0
    reasons = {"over-cap": 0, "ellipsis-joined": 0}
    for path, findings, error in results:
        if findings is None:
            errors += 1
            print("GATE_QUOTES_ERROR: %s: %s" % (path, error), file=sys.stderr)
            continue
        for number, s_id, words, reason in findings:
            detail = reason if reason in ("doubled-locator", "truncated-grounds") else "words=%d" % words
            print("%s:%d %s %s" % (path, number, s_id, detail))
            reasons[reason] = reasons.get(reason, 0) + 1
        total += len(findings)
    print("GATE_QUOTES: %d findings" % total)
    if errors:
        return 2
    return 1 if total else 0


def lesson(rows):
    """A whole lesson document whose `## Gate` section carries `rows`."""
    return "# Round 60 — lesson (kotodama)\n\n## Gate\n\n%s\n\n## Status\n" % rows


def selftest():
    """Cases exercising spans, row shapes, word counts, and ellipsis rules."""
    long_quotes = " ".join(["w%d" % n for n in range(26)])
    hard_wrapped = " ".join(["w%d" % n for n in range(26)])
    hyphenated = " ".join(["w%02d" % n for n in range(1, 24)] + ["mother-in-law", "twenty-six"])
    cases = [
        ("short-quote", lesson('- S900 — p. 1: "one two three".\n'), 0),
        ("exactly-25", lesson('- S900 — p. 1: "%s".\n'
                              % " ".join(["w%d" % n for n in range(25)])), 0),
        ("26-words", lesson('- S900 — p. 1: "%s".\n' % long_quotes), 1),
        ("curly-26-words", lesson('- S900 — p. 1: “%s”.\n' % long_quotes), 1),
        ("anchor-join-27", lesson('- S900 — Table 2 "Counts of pointing forms used": '
                                  '"%s".\n'
                                  % " ".join(["w%d" % n for n in range(22)])), 1),
        ("two-separate-quotes", lesson('- S900 — p. 1: "%s". Next paragraph: "%s".\n'
                                       % (" ".join(["a%d" % n for n in range(13)]),
                                          " ".join(["b%d" % n for n in range(13)]))), 0),
        ("ellipsis-joined", lesson('- S900 — Abstract: "The first two '
                                   '… have recognition as emblems".\n'), 1),
        ("leading-ellipsis", lesson('- S900 — Abstract: "…the steep mountains '
                                    'and rugged topography of the region".\n'), 0),
        ("not-a-row", lesson('The gate says "%s".\n'
                             % " ".join(["w%d" % n for n in range(40)])), 0),
        ("outside-the-gate-section",
         "## Gate\n\n- S900 — p. 1: \"short\".\n\n## Later\n\n- S901 — p. 1: \"%s\".\n"
         % " ".join(["w%d" % n for n in range(40)]), 0),
        ("row-in-another-section",
         "## Intro\n\n- S901 — p. 1: \"%s\".\n\n## Gate\n\n- S900 — p. 1: \"short\".\n"
         % " ".join(["w%d" % n for n in range(40)]), 0),
        ("no-gate-section", "# Round 60 — lesson (kotodama)\n\n## Status\n", None),
        ("hard-wrapped-26", lesson('- S900 — p. 1: "%s\n  %s".\n'
                                   % (" ".join(hard_wrapped.split()[:13]),
                                      " ".join(hard_wrapped.split()[13:]))), 1),
        ("guillemets-26", lesson('- S900 — p. 1: «%s».\n' % long_quotes), 1),
        ("ellipsis-between-spans",
         lesson('- S900 — p. 1: "alpha bravo charlie delta echo foxtrot golf hotel" '
                '… "india juliet kilo lima mike november oscar papa quebec romeo sierra tango '
                'uniform victor".\n'), 1),
        ("star-bullet-26", lesson('- * S900 — p. 1: "%s".\n' % long_quotes), 1),
        ("hyphenated-whitespace-25", lesson('- S900 — p. 1: "%s".\n' % hyphenated), 0),
    ]
    failures = 0
    for name, body, want in cases:
        findings = scan_text(body)
        got = None if findings is None else len(findings)
        ok = got == want
        failures += not ok
        print("%s %s want=%s got=%s" % ("PASS" if ok else "FAIL", name, want, got))

    class_cases = [
        ("doubled-locator-single-quoted-red",
         lesson("- S900 — URL — accessed 2026-10-22 — Section 'X': \"X\": \"real quote\".\n"),
         None, "doubled-locator"),
        ("doubled-locator-double-quoted-red",
         lesson('- S900 — URL — accessed 2026-10-22 — "Section", ¶1: "Section", ¶1: "real".\n'),
         None, "doubled-locator"),
        ("doubled-locator-green",
         lesson("- S900 — URL — accessed 2026-10-22 — Section 'X': \"other\": \"real quote\".\n"),
         None, None),
        ("doubled-locator-s273-escaped-green",
         lesson('- S273 — URL — accessed 2026-10-22 — Title (EN): "Gold death-mask of a man, known by the conventional name \\"mask of Agamemnon\\"".\n'),
         None, None),
        ("truncated-grounds-red",
         lesson("- S900 — p. 1: \"short\". Grounds: the keeper was a. Seat: Scout.\n"),
         {"S900": "the keeper was a guardian."}, "truncated-grounds"),
        ("truncated-grounds-whole-single-stop-green",
         lesson("- S900 — p. 1: \"short\". Grounds: the keeper was owed. Seat: Scout.\n"),
         {"S900": "the keeper was owed."}, None),
        ("truncated-grounds-double-stop-green",
         lesson("- S900 — p. 1: \"short\". Grounds: the keeper was owed.. Seat: Scout.\n"),
         {"S900": "the keeper was owed."}, None),
    ]
    for name, body, source_teaches, want in class_cases:
        findings = scan_text(body, source_teaches)
        got = [] if findings is None else [reason for _, _, _, reason in findings]
        expected = [] if want is None else [want]
        ok = got == expected
        failures += not ok
        print("%s %s want=%s got=%s" %
              ("PASS" if ok else "FAIL", name, want or "none", ",".join(got) or "none"))
    total = len(cases) + len(class_cases)
    print("SELFTEST: %d/%d pass" % (total - failures, total))
    return 1 if failures else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    return run(args.paths)


if __name__ == "__main__":
    sys.exit(main())
```

## Risks / blockers

- `truncated-grounds` is intentionally silent without the matching registry source row; this avoids broad one-period false positives. The comparison removes quote delimiters to tolerate the existing S263/S279 wrapping differences, then applies the strict-prefix test.
- No blockers. No build, lint, formatter, or unrelated tests were run.
