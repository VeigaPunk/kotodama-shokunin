# W3 attack — ExecRerunBoth (measurements re-run at both landings)

Verdict: **PARTIAL** — every measured leg, count, control and mutation probe reproduces with
zero divergence (C 13/13 exit 0, Ca 12/12 exit 0, selftests 85/85 and 154/154, all six
before/after counts equal the frozen claims). One defect, documentary and non-scoring: the
frozen `reports/round-75/claims.json` `status` sentence says the freeze commit adds "the
do-nothing and junk-landing controls"; git history says those four receipts entered later
(§7). No data claim is falsified.

All work in scratch clones under
`/fast/scratch/hyaku/kotodama-r75/ExecRerunBoth/` (seat dir, removed at yield); every git call
names `-C`; no lane byte, index or jj/git state touched; no tool installed.

Lane state at dispatch: `main = 82ced5c` (telemetry/report-only) over `4f5e3b2` (claim C) over
`012e8d3` (claim Ca) over `5d01674` (freeze) over base `f556d10`. First-parent chain verified:
`git merge-base --is-ancestor` freeze→Ca yes, Ca→C yes, freeze→C yes; parents
`012e8d3 → 5d01674`, `4f5e3b2 → 012e8d3`.

## 1. Claim C — `accept-c.py` at 4f5e3b2535c2c06c51627dc2736c40183847cae1

Clone: `…/ExecRerunBoth/c/lane` (`rev-parse --show-toplevel` = that path, HEAD = the lands rev).
Full stdout, exit code 0:

```
# round-75 acceptance counter — claim C (shokuknow narrative-structure-frameworks assimilation)
# counter sha256 (self): 315c5f3f27fd36b7ee92cb5bff9c34c27a5013e28218d9481ee7f74b5c7ce261
# stamped revision: 4f5e3b2535c2c06c51627dc2736c40183847cae1
# evaluated revision: 4f5e3b2535c2c06c51627dc2736c40183847cae1
# measured revision (lane main): 4f5e3b2535c2c06c51627dc2736c40183847cae1
# tree: 43a96e737f250fb8e5bed93abc13c6b9ba608bdb
# base revision: f556d1049fe651d3d63975600b13acd9fb686f15
# freeze revision: 5d0167464309d8133991b30f7d7a7011a6a0fd14
# config sha256 (frozen claims.json): 3d600b7179b001192594e409b4fc0190d3676d0acc70b9d528877dc77257a2f5
# config source: git show 5d0167464309d8133991b30f7d7a7011a6a0fd14:reports/round-75/claims.json (never the graded tree)
# frozen legs: 13 (ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,SCRATCHMIRROR,COLLCHECK,FROZENCFG,INDEX)
# frozen map: .ufo/waves/round-75/assimilation/id-renumber-map.json sha256=778068a431db1f82e9492007f0f4ecf03af21c46679695e91f9981dff56d5155
# materialized: git clone of /fast/scratch/hyaku/kotodama-r75/ExecRerunBoth/c/lane, checkout --detach 4f5e3b2535c2 at /fast/scratch/hyaku/kotodama-r75/ExecRerunBoth/hs/kotodama-r75/counter/r75-lands-oraqahwk/clone
# worktree graded: no (leg bytes read only from the checkout and the git-archive base tree)
# lane worktree HEAD (disclosure only): 4f5e3b2535c2c06c51627dc2736c40183847cae1
# access date: 2026-10-27
# adopted rows: S885 S886 S887 S888 S889 S890 S891 S892 S893 (staged S876/S885/S917/S921 S902 S904 S864 S865 S866 S905 S919 S870)
# reused rows: - (staged -)
# entries: corpus/knowledge/myth-symbol/narrative-structure-frameworks.md ; corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md ; corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md

LEG PASS ENTRIES
LEG PASS ROWS
LEG PASS REPOINTED
LEG PASS GATE
LEG PASS EVIDENCE
LEG PASS REJECTS
LEG PASS GROUND
LEG PASS CITEDLINES
     files=3 last-line=CITED-LINES: 0 finding(s) in 3 file(s)
LEG PASS CENSUS
     exit=0 last-line=file	ok	/fast/scratch/hyaku/kotodama-r75/ExecRerunBoth/hs/kotodama-r75/counter/r75-lands-oraqahwk/clone/corpus/SOURCES.md
LEG PASS SCRATCHMIRROR
     receipt@0 append@2 rows=9 entries=3
LEG PASS COLLCHECK
     ids=808 staged=132 collisions=26 guard=ok/ok map=12
LEG PASS FROZENCFG
     freeze 5d0167464309: constants from git show 5d0167464309:reports/round-75/claims.json (sha256 3d600b7179b00119); rows S885 S886 S887 S888 S889 S890 S891 S892 S893; entries 3; fragments 9; terms 2; refused S870; access 2026-10-27
  lands 4f5e3b2535c2: lands==freeze=no first-parent-chain=yes claims@lands=frozen-bytes map=.ufo/waves/round-75/assimilation/id-renumber-map.json(sha256-match) ledger=frozen-bytes counter=self-pinned
LEG PASS INDEX
     corpus/README.md: 6 section(s), myth-symbol=32, last footer total=252 vector=32/32/40/29/24/95, 3 adopted row(s), 822 base / 831 lands line(s), 12 exempt line(s)
ACCEPT-C-75: PASS legs=13/13
EXIT=0
```

13 legs, order identical to the frozen `legs` list. Counter sha256 `315c5f3f…ce261` = the hash
in `telemetry/measures-c.txt`. Reproduces the committed receipt line-for-line except the
scratch path and the "materialized: git clone of …" origin string.

## 2. Claim Ca — `accept-ca.py` at 012e8d3c8b92f47c734f735d58d118d574fe6a14

Clone: `…/ExecRerunBoth/ca/lane`, local `main` pinned to 012e8d3 (STAMP reads `--main`; the
clone's `origin/main` was not used). Full stdout, exit code 0:

```
# counter sha256 (self): 98d8e7974c82d048db67fe8eebd06cd78308bc0e3233c922ec16f527fd1ac235
# stamped revision: 012e8d3c8b92f47c734f735d58d118d574fe6a14
# evaluated revision: 012e8d3c8b92f47c734f735d58d118d574fe6a14
# measured revision (lane main): 012e8d3c8b92f47c734f735d58d118d574fe6a14
# tree: c943f86b4cb24668682c3e46b40629104c5816dd
# claim: Ca  round: 75  base: f556d1049fe651d3d63975600b13acd9fb686f15
# freeze: 5d0167464309d8133991b30f7d7a7011a6a0fd14 (config read at this commit only)
# min-pairs: 10
# frozen legs: 12 (LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY, R1EXEMPT, NOSTUB, SEPARABLE, RECEIPTS, COMBINED, FROZENCFG, STAMP)
# combined revision: 4f5e3b2535c2c06c51627dc2736c40183847cae1
# counter: reports/round-75/accept-ca.py
# clone: /fast/scratch/hyaku/kotodama-r75/ExecRerunBoth/hs/kotodama-r75/r75-ca-kkq74ar9/lands head=012e8d3c8b92f47c734f735d58d118d574fe6a14
# base-clone: /fast/scratch/hyaku/kotodama-r75/ExecRerunBoth/hs/kotodama-r75/r75-ca-kkq74ar9/base head=f556d1049fe651d3d63975600b13acd9fb686f15
# ledger: reports/round-75/ledger.json source=freeze sha256=469fbb0ea43b00a13c57701260761ecdf8d7375615c0ac72878097ae56f429a7
PAIR L75-01 disposition=REPAIR stated_at=SHONEN.md:6 stated='412' observed_base='808' observed_lands='808' expected_after='808'
PAIR L75-02 disposition=REPAIR stated_at=corpus/README.md:344 stated='30' observed_base='32' observed_lands='32' expected_after='32'
PAIR L75-03 disposition=REPAIR stated_at=corpus/README.md:407 stated='36' observed_base='40' observed_lands='40' expected_after='40'
PAIR L75-04 disposition=ANNOTATE stated_at=corpus/README.md:813 stated='249' observed_base='247' observed_lands='247' expected_after='247'
PAIR L75-05 disposition=REPAIR stated_at=SHONEN.md:6 stated='367' observed_base='713' observed_lands='713' expected_after='713'
PAIR L75-06 disposition=REPAIR stated_at=SHONEN.md:6 stated='35' observed_base='58' observed_lands='58' expected_after='58'
PAIR L75-07 disposition=REPAIR stated_at=SHONEN.md:6 stated='10' observed_base='37' observed_lands='37' expected_after='37'
PAIR L75-08 disposition=ANNOTATE stated_at=corpus/lessons/round-74.md:37 stated='absent' observed_base='present' observed_lands='present' expected_after='present'
PAIR L75-09 disposition=ANNOTATE stated_at=corpus/lessons/round-74.md:38 stated='absent' observed_base='present' observed_lands='present' expected_after='present'
PAIR L75-10 disposition=ANNOTATE stated_at=LOG.md:4318 stated='43' observed_base='44' observed_lands='44' expected_after='44'
LEG PASS LEDGER
     pairs=10 min=10 source=freeze
LEG PASS BASEMISMATCH
     red=10 min=10 ids=['L75-01', 'L75-02', 'L75-03', 'L75-04', 'L75-05', 'L75-06', 'L75-07', 'L75-08', 'L75-09', 'L75-10']
LEG PASS REPAIR
     green=['L75-01', 'L75-02', 'L75-03', 'L75-05', 'L75-06', 'L75-07'] red=[]
LEG PASS ANNOTATE
     rows=25 annotate-pairs=4 unannotated=0 []
LEG PASS NOSTUB
     minimum-shape=leading-id+old-token+new-token+rederive stubs=[]
LEG PASS APPENDONLY
     protected=['LOG.md', 'SCORECARD.md', 'corpus/lessons/round-74.md', 'corpus/lessons/round-73.md', 'corpus/QUALITY.md', 'SHONEN.md', 'reports/round-73/claims.json', 'reports/round-73/ledger.json'] fleet-pin=3a7401609325 report=.ufo/reports/round-74/kotodama.md blob-sha256=354273bc972d repair-stated_at={'SHONEN.md': [6], 'corpus/README.md': [344, 407], 'SKILL.md': [701]} rule2-edits=0
LEG PASS R1EXEMPT
     verdicts={'green': True, 'red': False, 'mixed': False} receipts=['green=d111f02a0b8b', 'red=d3aecfbbb387'] problems=[]
LEG PASS SEPARABLE
     lane-ids=9 ids-sha256:1232f162 family-sha256:9b3cd004 forbidden=4 scanned=['ledger', 'corrections-rows', 'reports/round-75/telemetry/accept-ca-74-at-lands.txt', 'reports/round-75/telemetry/controls-ca.txt', 'reports/round-75/telemetry/r1exempt-green.txt', 'reports/round-75/telemetry/r1exempt-red.txt', 'reports/round-75/telemetry/selftest-r72-repeat.txt', 'stated:SHONEN.md:6', 'stated:corpus/README.md:344', 'stated:corpus/README.md:407', 'stated:corpus/README.md:813', 'stated:SHONEN.md:6', 'stated:SHONEN.md:6', 'stated:SHONEN.md:6', 'stated:corpus/lessons/round-74.md:37', 'stated:corpus/lessons/round-74.md:38', 'stated:LOG.md:4318'] problems=[]
LEG PASS RECEIPTS
     rev=5e4796c0cb6a receipts=['accept-ca-74=40d8a38b537f'] tools=[] problems=[]
LEG PASS COMBINED
     ca-lands=012e8d3c8b92 combined=4f5e3b2535c2 tree=43a96e737f25 problems=[]
LEG PASS FROZENCFG
     freeze=5d0167464309 first-parent-of-lands; round=75 base=f556d1049fe6 legs=[…12…] min-pairs=10 lane-ids=9 ids-sha256:1232f162 family-sha256:9b3cd004 protected=[…8…] receipts=5e4796c0cb6a
LEG PASS STAMP
     stamped=evaluated=measured=012e8d3c8b92 tree=c943f86b4cb2 counter=98d8e7974c82 clone=/fast/scratch/hyaku/kotodama-r75/ExecRerunBoth/hs/kotodama-r75/r75-ca-kkq74ar9/lands
ACCEPT-CA-75: PASS legs=12/12
EXIT=0
```

12 legs, frozen order. Counter sha256 `98d8e797…ac235` and ledger sha256 `469fbb0e…f429a7`
both equal the committed `measures-ca.txt` values; the ten PAIR lines are byte-equal to the
committed receipt.

## 3. Selftests (both counters, run at the lands rev with the frozen counter blobs)

- `accept-c.py --selftest` → `SELFTEST: 85/85`, exit 0. **Expected 85/85 — equal.**
- `accept-ca.py --selftest` → `SELFTEST OK: 154 checks across 39 scenarios reported-fail=0`,
  `SELFTEST: 154/154`, exit 0. **Expected 154/154 — equal.**

`accept-c.py` selftest was **not** stale here: it reports `315c5f3f…ce261`, the frozen hash
(the committed `telemetry/selftest-c.txt` pins the pre-freeze `fa5060b9…`, a difference the
controls critic also flags; this run closes it with the frozen blob).

## 4. Before / after counts (re-run at base and at the C landing)

| command | expected | measured base `f556d10` | expected | measured lands `4f5e3b2` |
|---|---|---|---|---|
| `git ls-tree -r --name-only <rev> corpus/knowledge \| grep -ci narrative` | 0 | **0** (grep exit 1, zero lines) | — | **3** |
| `git show <rev>:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | 808 | **808** | 817 | **817** |
| `git ls-tree -r --name-only <rev> corpus/knowledge \| grep -c '\.md$'` | 249 | **249** | 252 | **252** |

**All equal; no difference.** Cross-checks with a second, independent row pattern
(`^\| S[0-9]+`) give 808 / 817; 0 duplicate ids at lands; ids contiguous `S869 … S893`; the
nine added rows are exactly S885–S893 and the 808 base rows are byte-identical at lands
(`grep -Fxv -f lands base` = 0 rows, lands-not-base = 9 rows).

## 5. Independent derivation of the C claim's sub-assertions

- **Per-partition file counts at lands** (independent `ls-tree | grep -c '\.md$'`):
  civilizations 95, culture-material 40, linguistics 32, myth-symbol 32, synthesis 29,
  verification 24 → total 252, i.e. the INDEX footer vector `32/32/40/29/24/95` with
  `myth-symbol=32` and total 252 exactly as printed by the leg.
- **README line counts**: base 822, lands 831 — equals the leg's `822 base / 831 lands`.
- **The 478-word floor is calibrated**: the smallest base knowledge entry really is
  `corpus/knowledge/culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md` at
  **478** words (next 639). The three adopted entries are 5014 / 3951 / 3779 words.
- **Row shape**: all nine rows have exactly 11 cells, `| S885 | … | mined | 2026-10-27 | … |`,
  status cell literally `mined`, `used-by` = the citing entries.
- **used-by contraction cross-check** (independent parse): S885→all three entries;
  S886, S887→amend-2026-10-23; S888, S889, S890, S893→base entry; S891, S892→amend-2026-10-23b.
  The entries' own `- source:` lines are exactly `885 888 889 890 893` / `885 886 887` /
  `885 891 892`. **Exact match, both directions.**
- **Evidence windows**: recomputed `sha256` of each stored `--- window ---` block with my own
  parser (`--- window ---` → `--- quote ---`, trailing empties dropped, UTF-8, no trailing
  newline) = declared `window-sha256` for **9/9**; `window-bytes` = stored byte length 9/9;
  scope rule holds 9/9 (`whole-document` S885 3720, S886 3526, S887 3073, S891 2169 chars, each
  < 4096 and `== visible-chars`; `excerpt` S888 4096/5481, S889 4098/45276, S890 4098/7205,
  S892 4097/6973, S893 4103/7711). UA browser-shaped and identical to the round UA 9/9;
  access date 2026-10-27 9/9.
- **Anchor-quote location**: each row's anchor cell carries exactly one ≥8-char delimited span
  and each is present in its own stored window after NFKC + whitespace folding — **9/9 hits**
  (`Innombrables sont les récits du monde.`; `Étudier la « littérarité …`; `Loin de se limiter à
  l'interprétation des énoncés, la théorie sémantique`; `故事是一种深层的抽象结构，必须通过话语呈现`;
  `a new research area called “narratology of narrative generation”`; `describe a story as a
  hierarchical structure consisting of three major layers`; `les premières lexies suscitent
  l'établissement des cinq grands codes`; `Mais combien, et de quelle nature, sont ces codes ?`;
  `网络小说中的世界观，指的是故事设定中世间万物运转的方式，是故事发生的场景、规则`).
- **GROUND re-derived**: all nine frozen fragments have **0** matches in base `corpus/SOURCES.md`;
  base knowledge carries no `narratology` occurrence.
- **Frozen digests equal at every graded rev**: `claims.json` sha256 `3d600b71…57a2f5` at freeze
  and at C-lands (and Ca-lands); `ledger.json` `469fbb0e…f429a7` at freeze, C-lands, Ca-lands;
  map sha256 `778068a4…d5155` at freeze = `claims.map.sha256`.
- **Counters unchanged after the freeze**: `git diff 5d01674..4f5e3b2` and
  `5d01674..012e8d3` over `accept-c.py`, `accept-ca.py`, `claims.json`, `ledger.json` are empty
  (the only freeze→C delta under `reports/round-75/` is the nine `evidence/S*.txt` files).
- **Ca append-only, independent `--numstat` base..Ca-lands** over the protected set:
  `33 0 SCORECARD.md`, `1 1 SHONEN.md`, `72 0 corpus/QUALITY.md`; zero lines removed anywhere
  (LOG.md, lessons 73/74, reports/round-73 * unchanged). SHONEN's single changed line is the
  pair L75-01/05/06/07 statement.
- **Ca SEPARABLE, independent**: ledger 0 hits of `S88[5-9]|S89[0-3]|
  narrative-structure-frameworks`; SCORECARD corrections section 0 hits; every Ca telemetry
  receipt 0 hits. (`controls-c.txt` carries 10 such lines but it is claim C's control, not one
  of the receipts Ca's `SEPARABLE` names.)

## 6. Do-nothing controls re-run

- C, `--lands 5d01674` (= freeze): `ACCEPT-C-75: FAIL legs=4/13`, exit 1; red ENTRIES, ROWS,
  REPOINTED, GATE, EVIDENCE, REJECTS, CITEDLINES, SCRATCHMIRROR, INDEX; green GROUND, CENSUS,
  COLLCHECK, FROZENCFG. **Identical to `telemetry/controls-c.txt` (4/13, exit 1, same leg set).**
- C, `--lands f556d10` (= base): `REFUSED: lands f556d1049fe6 is the frozen claim base…`,
  `ACCEPT-C-75: FAIL legs=0/13 (refused…)`, exit 2. **Identical to the receipt.**
- Ca, `--lands 5d01674` with `--combined 4f5e3b2`: `ACCEPT-CA-75: FAIL legs=7/12`, exit 1;
  red REPAIR, ANNOTATE, NOSTUB, RECEIPTS, STAMP; green LEDGER, BASEMISMATCH, APPENDONLY,
  R1EXEMPT, SEPARABLE, COMBINED, FROZENCFG. Satisfies the declared control (REPAIR+ANNOTATE
  red, R1EXEMPT/LEDGER/FROZENCFG green). Composition differs from `controls-ca.txt` only where
  my invocation differs from the receipt's: I supplied `--combined` (receipt's COMBINED red)
  and my local `main` was pinned to the Ca lands (so STAMP checks lands≠measured and is red,
  where the receipt's main was the freeze and STAMP was green). Both runs are 7/12 FAIL.
- Ca, `--lands f556d10`: `ACCEPT-CA-75: FAIL legs=0/12 (refused: --lands equals the frozen
  base f556d1049fe6)`, exit 2. **Identical to the receipt.**

## 7. Difference found (the one defect)

`claims.json` `status` reads: "…frozen by the commit that adds this file together with
ledger.json, id-renumber-map.json, both counters, **the do-nothing and junk-landing controls**
and the build evidence…".

Git history (lane repo, read-only):

| artifact | added at |
|---|---|
| `claims.json`, `ledger.json`, `accept-c.py`, `accept-ca.py`, `id-renumber-map.json`, `fixtures/r1exempt-{green,red,mixed}.json`, `telemetry/{census-start,gap-sweep,r1exempt-*,selftest-c,selftest-ca}.txt` | **5d01674** (freeze) ✔ as stated |
| `telemetry/controls-c.txt`, `telemetry/controls-ca.txt` | **012e8d3** (claim Ca landing) |
| `telemetry/junk-c.txt`, `telemetry/junk-ca.txt`, `telemetry/measures-c.txt`, `telemetry/measures-ca.txt` | **82ced5c** (post-landing measurement commit) |

Presence check: at the freeze the four control/junk receipts are **ABSENT**; at C-lands only
controls-c/-ca exist; at main all six exist. So the sentence is false for the four receipts it
names, and claim C's `do_nothing_control` (`…plus the junk-landing receipt junk-c.txt`) and
claim Ca's (`…plus junk-ca.txt fixtures J4f…J10`) point at paths that do not exist at either
graded rev — they exist only at main.

Impact: **none on any leg** (no leg reads those receipts; FROZENCFG reads only `claims.json` and
`ledger.json`), and **none on the controls' content**, which reproduces (§6). It is a
documentation falsehood inside the frozen config, and it also means the *junk-landing* evidence
was produced and committed after both landings rather than before data.

## 8. My own junk landings (fixture commits in scratch clones only)

Four positive mutations against real landed bytes, each on a `probe` branch with
`-c user.name=fixture -c user.email=f@f.invalid`, graded with `--lands <mutant sha>`:

| # | mutation | graded | verdict |
|---|---|---|---|
| P1 | S893 evidence window, one CJK character (`爽`→`痛`) | C `a57cc91d` | **FAIL 12/13**, only EVIDENCE red: `S893 window-sha256 '5e197a57a89464e6' != the recomputed digest … (6adbb38f763c524c)` |
| P2 | pre-existing row S504 teaches cell (`again`→`twice`), evidence restored | C `3b148d0a` | **FAIL 12/13**, only ROWS red: `pre-existing S504 line removed (every pre-existing row must stay byte-identical)` |
| P3 | revert SHONEN.md:6 repair token (`808`→`412`) | Ca `da7f58b2` (main pinned) | **FAIL 11/12**, only REPAIR red: `red=["L75-01(statement='412' truth='808')"]` |
| P4 | corrupt SCORECARD row L75-04 new token (`247`→`248`) | Ca `29333df8` (main pinned) | **FAIL 10/12**: ANNOTATE red (`unannotated=1 ["L75-04(row-leading-L75-04 stated='249' observed='247')"]`) and NOSTUB red (`stubs=['L75-04:new-token']`) |

All four junk landings were refused, each with the leg that owns the mutated surface red and
the other legs unaffected — the counters are sensitive on the graded bytes, not only on their
synthetic fixtures.

## 9. Risks / unverified

- Source *access* is not re-verified here by design: I re-derived the stored windows and their
  digests, and located the Gate quotes inside them, but did not re-fetch any URL (QUALITY 10/22
  binding is the fetch records' claim, and a refetch would produce an unbound new record).
  The lesson's own notes already disclose the byte drift on the Persée notices and the two
  missing probe receipts (S891, S893) — recorded, not repaired.
- No LSP involvement was needed; none recorded.
- The one defect in §7 is a claim-text/history mismatch; it changes no measured number.

## 10. Scratch / cleanup

Seat dir `/fast/scratch/hyaku/kotodama-r75/ExecRerunBoth/` (two lane clones, one `probe`
branch each with four fixture commits, `hs*` counter scratch) — deleted on yield. Nothing was
written outside this report and that dir; the fleet repo, `scripts/`, `templates/`,
`.ufo/state`, the shokuknow tree and every sibling lane were left untouched (all lane access
was `git -C … show/diff/log/log-tree` plus clone-once).
