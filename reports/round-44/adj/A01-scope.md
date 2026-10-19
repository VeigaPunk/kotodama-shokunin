# A01 — Bleed / scope verification (round 44, cross-claim)

- **Seat:** `A01` (verifier, claim `cross`)
- **Mission:** confirm no cross-domain bleed (no canon, no lore decision, no
  packet surface), `PROVINCE.md` still accurate, and the only corpus delta is
  the single C landing + README. Report any scope violation.
- **Baseline commit:** `c9f4eaa` (`git rev-parse HEAD` →
  `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d`)
- **Observation window:** `2026-10-19T17:19Z`–`17:32Z` (wave in flight). Four
  passes: baseline + `op/O02`, `op/O03`; nine seats (Addendum A); the concrete C
  target `myth-symbol/dream-vision-trance.md` (Addendum B); then nineteen seats,
  including `scout/K02`'s competing cartography target and `cov/C01`'s drafted
  dream entry (Addendum C).
- **Scope verdict:** **PASS at baseline and at artifact level; no scope
  violation observed.** Two clauses (which C target lands and the applied
  corpus delta) remain **`to-verify` at integration** — the integrator must
  choose one of two in-province targets, and C's freshness clause favors only
  one of them (Addendum C). The exact post-landing gate is §7.

## 0. Clause-by-clause verdict

| Scope clause | Verdict | Basis |
|---|---|---|
| No canon claim / no lore decision | **PASS** (contract + O artifact + C01 draft) | `claims.json:60-69` non-goals; `QUALITY.md:18-19`; handoff contract `:17-18`; O09 body canon-word scan = 0 hits (§3); C01's draft declares NON-CANON and a §15 canon boundary (`C01-entry-draft.md:7`, `:392-394`) |
| No packet-surface change | **PASS** | `claims.json:66`, `targets.json:8`; 13 packet-surface digests pinned (§5); `git status --porcelain corpus tools examples` empty at baseline |
| `PROVINCE.md` still accurate | **PASS (structural)** | every path it names exists; six-partition "Owns" set matches the tree; ownership split mirrored by the handoff contract (§6) |
| Only corpus delta = single C entry + README | **PASS at baseline / `to-verify` on landing** | corpus clean, 223 tracked entries; two competing in-province targets — `myth-symbol/dream-vision-trance.md` (drafted) and `culture-material/cartography-and-mapmaking.md` (undrafted) — must resolve to **one**; gate in §7, conflict in §8C |
| Seats write only their out path | **PASS so far** | 32/32 out paths in-province and unique; nineteen filed out files audited (Addenda A–C); each attests no tracked-byte edit; scratch writes are the mandated `TMPDIR` (§8) |

No scope violation was found to report. §9 lists the residual findings that are
**not** violations (two `to-verify` filing decisions and one pre-existing
README defect owned by C02).

## 1. Method

Read-only inspection plus digest pinning. Commands were run from the repo root
with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; nothing outside
`reports/round-44/adj/` and `.scratch/a01/` was written. I did not run any
`run-validation.py`, did not execute the round runner, and did not edit a
tracked byte.

Evidence base:

- `reports/round-44/claims.json` (claim contract and non-goals)
- `reports/round-44/targets.json` (32 seat missions and out paths)
- `reports/round-44/telemetry/dispatch-declared.json`
- `PROVINCE.md`, `corpus/QUALITY.md`, `corpus/README.md`,
  `corpus/knowledge/synthesis/worldbible-integration-contract.md`
- `reports/round-43/op/O09-scribe.md:356-870` (the body claim O lands)
- `reports/round-44/op/O02-verify.md`, `reports/round-44/op/O03-defects-verify.md`
  (the only seat outputs present during the window)

## 2. Baseline tree state — zero corpus delta

At baseline `c9f4eaa`, before any seat output landed:

```
$ git status --porcelain=v1
?? reports/round-44/

$ git status --porcelain corpus tools examples
(no output)

$ git diff --stat
(no output)

$ find corpus/knowledge -name '*.md' | wc -l
223

$ git ls-files 'corpus/knowledge/*.md' | wc -l
223
```

So all 223 knowledge entries are tracked and unmodified, and no tool or example
byte is modified. The only untracked path is this round's report directory,
which is the sanctioned output surface (`targets.json:5-6`).

Partition counts at baseline (sum 223):

```
linguistics 25 · myth-symbol 26 · culture-material 25 · synthesis 29 ·
verification 24 · civilizations 94
```

## 3. Claim O artifact — scope-inert by scan

Claim O lands the r43 O09 fenced body as
`tools/harness/basename-couples-resolver.py`. I extracted the fenced region
independently and scanned it:

```
$ awk 'NR>=356 && NR<=870' reports/round-43/op/O09-scribe.md > .scratch/a01/o09-fenced.txt
$ wc -l .scratch/a01/o09-fenced.txt
515
$ sha256sum .scratch/a01/o09-fenced.txt
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64  .scratch/a01/o09-fenced.txt
```

The digest matches the claim-pinned `43ce341f…` (`claims.json:34`), so the body
I scanned is the body that lands.

Scope scans over those 515 lines — all **zero hits**:

```
$ grep -nE "open\([^)]*['\"][wa]|\.write\(|os\.remove|shutil|subprocess|urllib|requests|socket|http[s]?://|\.\./\.\.|/home/|/tmp/" <body>
(no output)

$ grep -niE "canon|lore-shokunin|world bible|worldbible" <body>
(no output)

$ grep -niE "packet" <body>
(no output)
```

Positive read surfaces (all in-repo, read-only):

- `HERE`/`LANE` walk upward to the directory containing `corpus/knowledge`
  (`:27-34`), then `KNOW = <lane>/corpus/knowledge` (`:35`).
- `LIVE_PATH = KNOW/linguistics/phonetics-phonology.md` (`:272`), opened
  `"rb"`/`encoding="utf-8"` at `:164` and `:322`; `open(__file__, "rb")` at
  `:463` only to hash itself for the JSON census.
- `glob.glob(os.path.join(KNOW, "*", "*.md"))` at `:135`, `:221` — corpus
  enumeration only.
- No `sys.dont_write_bytecode` bypass: the body sets
  `sys.dont_write_bytecode = True` (`:24`), so it does not drop `__pycache__`.

**Conclusion:** landing this body adds one read-only harness tool under
`tools/harness/` (the lane's own gates, `PROVINCE.md:9-11`). It proposes no
write to `corpus/`, `examples/`, the packet surface, the world bible, or any
sibling tree.

## 4. Canon / lore boundary

Three independent guards are in force and consistent:

1. **Round contract.** Non-goals: "no promotion/canon/clearance/closure"
   (`claims.json:62`); C's after-required is a corpus entry + README, and C04
   audits it against "no canon claim" (`targets.json:32`).
2. **Admission bar.** `corpus/QUALITY.md:18-19`: "**Canon hygiene** — no entry
   decides what is true in any world. Canon recording and consistency
   verification belong to lore-shokunin; entries end at the handoff."
3. **Adjacency contract.** `corpus/knowledge/synthesis/worldbible-integration-contract.md:17-18`:
   "Kotodama owns generative craft … lore owns world-bible entities, relations,
   chronology, canon decisions … Each lane writes only its own authorized
   surfaces. A request from lore does not grant kotodama world-bible write
   access."

The O artifact contains **no canon/lore/world-bible wording** (§3). The Ca
artifact is a process gate over `claims.json` files (in-province calibration).
The C side is the only place a canon claim could enter, and its draft did not
exist during this window — so it is **`to-verify`**: C03 (source audit) and C04
(contract audit, canon clause) must pass before landing, and the post-landing
gate in §7 repeats the canon-word scan over the new entry.

No lore decision, no `lore-shokunin` record, and no world-bible byte is
proposed by any seat mission (`targets.json:13-44`).

## 5. Packet-surface pin

The round forbids packet-surface changes (`claims.json:66`, `targets.json:8`,
`targets.json:66`). I pinned the live packet surface at baseline; the
integrator can re-run the check after landing. **All must remain byte-identical.**

```
adfd7895461af85275d0170f7a2e057e0c5265ab2bc0ebadc298d2bae7766dc9  examples/handoff-packet.sample.md
751be0449edce03a54c21ed82b77f9d1f5e3faaf14ef2482c8525941e70cb95b  examples/handoff-packet.sample.yml
e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643  examples/culture-d2/packet.d2.yml
1b5010b7f449ec78755e9a8b0efea62c705af7ec5c592ceda6cf2c072dfac8a3  examples/culture-d2/packet.d2.typed.yml
a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43  examples/culture-d2/typed-labels.d2.yml
306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425  examples/culture-d3/packet.gates.yml
bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829  examples/culture-d3/packet.json
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182  examples/culture-d4/packet.d4.typed.yml
e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575  tools/gates/handoff-packet-check.py
66d854cc710f0b143e0a254d03e7f59ebce2c6b759d336ca368a9689babbd899  tools/harness/packet_links.py
cdcc19319269ee908577252485cc38288833b50987ed22a266c8eb01894b0e26  tools/harness/packet_uncertainty.py
5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069  corpus/knowledge/synthesis/worldbible-integration-contract.md
```

Frozen gate bytes are also untouched: `git status --porcelain tools/gates/frozen`
is empty, and no seat mission names a packet path or the handoff contract.
`examples/**` is in-province as a *reference surface* (`PROVINCE.md:10-11`) but
is nevertheless frozen by this round's non-goal; the pin above enforces that.

## 6. `PROVINCE.md` accuracy

Structural audit against the live tree at `c9f4eaa`:

| `PROVINCE.md` claim | Check | Result |
|---|---|---|
| Six knowledge partitions it names (`:9-10`) | each directory exists and is populated | **match** — linguistics 25, myth-symbol 26, culture-material 25, synthesis 29, verification 24, civilizations 94 |
| Handoff format at `corpus/knowledge/synthesis/worldbible-integration-contract.md` (`:23-24`) | file exists and is the canon-ownership contract | **match** — 28,421 bytes; `:1-5` states the interface; `:17-18` assigns canon to lore |
| "this lane's own gates" (`:10-11`) | round-44 adds `tools/harness/basename-couples-resolver.py` (+ Ca's freshness check) | **in-scope** — `tools/harness/` already holds the lane's resolver/guard/runner tools |
| "Only writes this standalone lane repository … its own fleet round reports" (`:27-29`) | round-44 writes are `tools/harness/*`, `corpus/knowledge/*` (one C entry), `corpus/README.md`, `reports/round-44/**` | **in-scope**; no sibling/world-bible write |
| Refuses: canon, rights rulings, game mechanics, general research method, web publishing, prompt/skill craft (`:16-20`) | no seat mission proposes any of these | **no conflict** |

No `PROVINCE.md` edit is proposed by any seat, and none is needed for the
round's declared changes. **Limit:** this is a *structural* accuracy check
(named paths, partition set, ownership split). It does not re-adjudicate the
domain description or the historical content of the corpus, which no round-44
artifact touches.

## 7. Corpus-delta invariant and post-landing gate

At baseline the corpus delta is zero (§2). The only admitted corpus change is
claim C: **one** new entry under one of the six partitions plus
`corpus/README.md`. Run this gate after the integrator applies C and before
admitting the round.

### 7.1 Exact-delta check (working tree, pre-commit)

```bash
# must print exactly two corpus paths:
#   corpus/README.md
#   corpus/knowledge/<partition>/<slug>.md
# The two filed candidates (Addendum C) are:
#   myth-symbol/dream-vision-trance.md             (drafted; carried from r42 R2)
#   culture-material/cartography-and-mapmaking.md  (fresh; undrafted)
# The integrator lands exactly ONE; substitute its exact path below. Never both.
git status --porcelain corpus/ | awk '{print $2}' | sort

# no deletion anywhere in corpus:
git diff --diff-filter=D --name-only corpus/        # expect empty

# README is the only *tracked* corpus file modified:
git diff --name-only corpus/                        # expect: corpus/README.md

# entry count moved by exactly +1:
test "$(find corpus/knowledge -name '*.md' | wc -l)" -eq 224 && echo 224-OK

# the new entry is exactly the C01 draft's intended path, nothing else new:
git status --porcelain corpus/knowledge | grep '^??'

# no baseline entry changed or removed (HEAD-relative, no scratch dependency):
git ls-tree -r --name-only HEAD -- corpus/knowledge | wc -l          # expect 223
git diff --name-status HEAD -- corpus/knowledge                      # expect empty
git status --porcelain corpus/knowledge                              # expect only the one ?? new entry
```

### 7.2 Packet re-freeze check (must be silent)

```bash
sha256sum -c <<'EOF'
adfd7895461af85275d0170f7a2e057e0c5265ab2bc0ebadc298d2bae7766dc9  examples/handoff-packet.sample.md
751be0449edce03a54c21ed82b77f9d1f5e3faaf14ef2482c8525941e70cb95b  examples/handoff-packet.sample.yml
e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643  examples/culture-d2/packet.d2.yml
1b5010b7f449ec78755e9a8b0efea62c705af7ec5c592ceda6cf2c072dfac8a3  examples/culture-d2/packet.d2.typed.yml
a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43  examples/culture-d2/typed-labels.d2.yml
306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425  examples/culture-d3/packet.gates.yml
bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829  examples/culture-d3/packet.json
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182  examples/culture-d4/packet.d4.typed.yml
e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575  tools/gates/handoff-packet-check.py
66d854cc710f0b143e0a254d03e7f59ebce2c6b759d336ca368a9689babbd899  tools/harness/packet_links.py
cdcc19319269ee908577252485cc38288833b50987ed22a266c8eb01894b0e26  tools/harness/packet_uncertainty.py
5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069  corpus/knowledge/synthesis/worldbible-integration-contract.md
EOF
```

### 7.3 Canon-word scan over the new entry

```bash
NEW=$(git status --porcelain corpus/knowledge | awk '/^\?\?/{print $2}')
grep -niE "canon (is|was|shall|will)|decides canon|world bible (says|records)|lore-shokunin (decides|rules)" "$NEW"
# expect: no hits that *decide*; the allowed form is the handoff disclaimer
#   "canon decisions belong to lore-shokunin" / "NON-CANON"
```

The entry passes only if C04's QUALITY.md clause-5 audit passes **and** this
scan finds no assertive canon decision. A disclaimer naming lore as the owner
is not bleed; a sentence that fixes world truth is.

## 8. Seat out-path compliance (wave in flight)

Contract-level check over `targets.json`:

```
seats=32  out_paths_valid=True  bad=[]  unique_out_paths=32
```

Every out path is relative and under one of the nine round-44 subdirectories
(`adj/ calib/ cov/ cross/ op/ plan/ review/ scout/ scribe/`); none escapes
with `..`, none is absolute, none collides.

Observed seat writes at the second pass (`17:25Z`): the nine out files listed in
Addendum A, plus `.scratch/o02-run/`, `.scratch/o03/`, `.scratch/o06*/`,
`.scratch/o07/`, `.scratch/o10/`, `.scratch/k01/`, `.scratch/x00/` working
dirs. `.scratch/` is gitignored (`.gitignore:6`) and is
the explicitly mandated `TMPDIR`; scratch products are working state, not
deliverables, and the O seats transcribe their measured outputs into their out
files. Neither edited a tracked byte:

```
$ git status --porcelain corpus tools/harness reports/round-43
(no output)
$ sha256sum tools/harness/couples-reference-extractor.py
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1   # claim's d8d23a26…
$ git status --porcelain=v1
?? reports/round-44/
```

Both O reports also self-attest no corpus staging and no packet write
(`O02-verify.md:299-311`, `O03-defects-verify.md:246-254`). No seat has written
under `corpus/` or `tools/` yet, as required: corpus changes are drafted as
fenced blocks and integrator-applied (`targets.json:6`).

## 8A. Addendum A — second-pass audit of late-landing seats (`17:25Z`)

Nine seat out files existed at the second pass. Each was scanned for the four
scope clauses (canon/lore, packet, corpus path, out-path compliance). None
proposes a corpus or packet write and none asserts canon.

| File | Scope-relevant statement | Verdict |
|---|---|---|
| `scout/K01` | "read-only scout. This file is the only report path written" (`:2`) | PASS |
| `op/O02` | "did not edit any tracked byte"; no corpus staging (`:14-15`, `:299-311`) | PASS |
| `op/O03` | "No file written outside `.scratch/o03/` and this out path" (`:251-252`) | PASS |
| `op/O06` | "No filed byte was edited. No corpus byte was staged." (`:14`); the `.scratch/o06` shadow trap was detected and re-extracted to a clean root (`:27-52`) | PASS — scratch only; no repo write |
| `op/O07` | witness "opened for reading only"; "Demotion is by record … never by editing bytes" (`:28`); pre-existing 212-entry snapshot in `.scratch/o07` noted, not created (`:42-44`) | PASS |
| `op/O08` | landing write set = new `tools/harness/basename-couples-resolver.py` + `reports/round-44/**`; no second resolver path (`:7-9`) | PASS |
| `op/O10` | independent fold; "No filed byte was edited by this seat" (`:6`) | PASS |
| `cross/X00` | out path "the only repo write"; "No filed byte edited, no corpus staging" (`:5`, `:10-11`) | PASS |
| `cross/X02` | scope audit: `git status --porcelain corpus/` = 0; nothing staged (`:125-137`); itself marked provisional (`:140-145`) | PASS, provisional like this report |

Re-measured with all nine present:

```
$ git status --porcelain=v1
?? reports/round-44/
$ git status --porcelain corpus
(empty)
$ find corpus/knowledge -name '*.md' | wc -l
223
$ find reports/round-44/calib reports/round-44/cov -type f
(empty)
$ sha256sum tools/harness/couples-reference-extractor.py
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1
```

The empty `calib/` and `cov/` directories matter: no seat has yet written a
durable artifact outside its out path (no census JSON, no C entry draft, no
freshness tool). Those deliverables are still report drafts or absent, so their
scope gates remain open (§7, §11).

## 8B. Addendum B — concrete C target audited (`17:27Z`)

`scout/K04-gap-verify.md` named the wave's C gap; `cov/C05-collision.md`
independently tested it. Target:
**`corpus/knowledge/myth-symbol/dream-vision-trance.md`** (myth-symbol
26 → 27, total 223 → 224). I re-ran the scope-relevant checks myself rather
than relying on either report.

### B.1 In-province and absent

```
$ ls corpus/knowledge/myth-symbol/dream-vision-trance.md
ls: cannot access '...': No such file or directory

$ find corpus/knowledge -type f | grep -iE 'dream|trance|vision|ecsta|shaman|incubat'
(no output)

$ printf '%s\n' dream-vision-trance.md | grep -E '^[a-z0-9]+(-[a-z0-9]+)*\.md$'
dream-vision-trance.md

$ ls -d corpus/knowledge/myth-symbol
corpus/knowledge/myth-symbol
```

`myth-symbol` is one of the six partitions `PROVINCE.md:9-10` grants this lane,
so the target is in-province. The exact path is free, and no corpus filename in
any partition carries the candidate's subject terms (no overwrite, no filename
collision).

### B.2 Ownership — with a false-positive control

Word-boundaried topic-line sweep returns **exactly two** hits:

```
$ grep -rilE -- '^- topic:.*\b(dream(s|ing|er|t)?|trance(s)?|ecsta[a-z]*|shaman[a-z]*|incubat[a-z]*|vision quest|visionary)\b' corpus/knowledge/*/*.md
corpus/knowledge/civilizations/mongol.md
corpus/knowledge/myth-symbol/divination-omen-systems.md
```

Both are adjacent, not owners of the state/induction complex:

- `divination-omen-systems.md:3` owns the **reading technology** ("question →
  technique → closed sign space → licensed reader"); `dream-oracles and
  incubation` is one row of fourteen, and its §8 boundary (`:147-158`) claims
  neither the altered state nor its specialist.
- `mongol.md:2-3` carries "shamanic vocabulary" as a civilization/lexical
  datum, not a system entry.

A naive substring sweep returned **five** hits; the extra three are artifacts of
`vision` inside other words, which is the control that shows the two-hit result
is the word-boundaried reading rather than a lucky count:

| file | matched substring |
|---|---|
| `civilizations/persia-achaemenid.md:2` | "road **provision**ing" |
| `culture-material/garment-lexicon-crosslinguistic.md:3` | "slot-di**vision**" |
| `verification/append-only-record-verification.md:3` | "index re**vision**" |

### B.3 Landing delta and README sites

C05's dry run (a byte-copy under `.scratch/c05/`, not the live tree) shows the
delta is exactly one added entry plus `corpus/README.md`. I verified the README
anchors it names, live:

```
$ sed -n '205p;215,216p;544p;548p' corpus/README.md
## myth-symbol/ (26)
- `divination-omen-systems.md` — …            # insertion point: new row before this
- `eschatology-world-end-systems.md` — …      # (filename order: dream-… sorts between)
Total knowledge entries: 223.
(total 223 files; directory totals 25/26/25/29/24/94).
```

The footer vector is correct at 223 today; the **rev-2.4 prose** at `:11` is not
(F3). A rev-2.5 edit must move the footer to `25/27/25/29/24/94`, the totals
line to 224, and `## myth-symbol/` to `(27)`, and must not copy the stale prose
vector.

### B.4 Verdict and conditions

- **Scope PASS for this target.** It is a reference/method entry in an owned
  partition; it proposes no packet, canon, or lore surface; the only other
  corpus file is the README; and no existing entry byte is overwritten.
- **Conditions (`to-verify`):** (i) C01's draft must use this exact slug and a
  topic that keeps the divination/state split; (ii) C03 and C04 must pass;
  (iii) the entry must end at the handoff (`QUALITY.md:18-19`) and mark
  restricted material rather than reconstruct it — K04 cites
  `verification/real-world-inspiration-boundaries.md:97` as the in-corpus rule;
  (iv) if K02 files a **different** gap, both candidates compete and claim C is
  +1 only — do not land both.
- **Minor:** C05's §4.3 post-landing command suggests `/tmp/after.sha256`.
  This round mandates `TMPDIR=$PWD/.scratch`, so use `.scratch/after.sha256`.
  C05 did not execute the command; this is a recommendation, not a violation.

## 8C. Addendum C — second C target filed; a claim-freshness conflict (`17:32Z`)

After Addendum B, `scout/K02-gap-scout.md` filed a **different** gap, and
`cov/C01-entry-draft.md` filed the fenced entry for K04's target. The round now
has two candidate corpus paths. I verified both against the live tree.

### C.1 The two targets

| Scout | Target | Partition | Status in the live tree |
|---|---|---|---|
| K02 (`K02-gap-scout.md:8`, §3.6, `:217-220`) | `culture-material/cartography-and-mapmaking.md` | culture-material | absent; **0** filename hits; **0** topic-line owners under `cartograph|mapmaking|portolan|cadastral|survey map` |
| K04 (`K04-gap-verify.md:10-13`) | `myth-symbol/dream-vision-trance.md` | myth-symbol | absent; 0 filename hits; 2 adjacent topic-line hits (§B.2) |

Independent cartography checks:

```
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '...': No such file or directory

$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0

$ grep -rilE -- '^- topic:.*(cartograph|mapmaking|portolan|cadastral|survey map)' corpus/knowledge/*/*.md
(no output)

$ ls corpus/knowledge/culture-material/ | sed -n '1,8p'
adornment-body-codes.md … calendar-festival-systems.md costume-semiotics.md …
```

`culture-material` is an owned partition (`PROVINCE.md:9-10`), the slug follows
the convention, and the sort position K02 names is real (the new row would fall
between `calendar-festival-systems.md` and `costume-semiotics.md`, matching
README `:240-241`; header `:234` is `## culture-material/ (25)`).

### C.2 The freshness conflict — verified, not inferred

Claim C's text requires "a gap with NO current owner (verified by a fresh
absence sweep at the 223 total, **not carried from a prior round**)"
(`claims.json:39`). The two candidates differ exactly on that clause:

- **Dream is carried.** `reports/round-42/scout/K02-myth-gaps.md:216` is a
  headed recommendation: "### R2 — Dream, vision and trance: the altered-state
  complex and the institutions that license it". K04's own report acknowledges
  the prior proposal (`K04-gap-verify.md:163`). The topic is unowned at HEAD —
  but it was named by a prior round, so it is a **carried** gap, not a fresh
  discovery.
- **Cartography is not carried.** K02's §3.6 measures the prior registries
  (r19/r35/r39/r40/r42/r43, root docs, lessons) and finds no cartography row;
  my spot checks of the live tree find zero filename and zero topic owners.
  Cartography is low-demand by raw mentions (K02 states this openly,
  `:179`), but it satisfies the "not carried" wording.

C01's draft follows K04 and says so: if K02 names a different gap, "this draft
is a **spare**, not the claim's landing; the integrator must choose one gap,
not land both" (`C01-entry-draft.md:9`; restated `:482`). C06 and S01 record the
same conflict independently (`C06-scribe.md:9-37`, `S01-integration-draft.md:65-75`).

### C.3 Scope verdict and what belongs to whom

- **Both targets are in-province.** Either landing is one corpus entry + the
  README, with no packet/canon/lore surface. So this conflict is **not a scope
  violation**; it is a claim-conformance (freshness) issue.
- **My seat does not choose.** C05 cleared the dream path for *collision*, not
  for *freshness* (`C05-collision.md:10, 17, 250-252`); K02/K04 disagree on
  what "carried" means; the integrator/X00 own the ruling.
- **Post-landing gate substitution:** if cartography lands, use §7 with
  `culture-material/cartography-and-mapmaking.md`; header `:234` 25→26, row
  between `:240` and `:241`, total `:544` 224, footer `:548` vector
  `25/26/26/29/24/94`. If dream lands, use §7 with
  `myth-symbol/dream-vision-trance.md`; vector `25/27/25/29/24/94`. **Never
  both** (225 would break the claim and the README arithmetic).
- **Record requirement:** if the carried dream target is chosen, the round
  record must name the "not carried" exception rather than present it as a
  fresh sweep — the r43 defect class was exactly a premise that was true in
  part but false as declared.

## 9. Findings for the integrator (none is a scope violation)

**F1 — census denominator ordering (cross-claim, X00 owns the ruling).**
Claim O's thresholds are pinned at 223 entries / 2730 refs
(`2556+166+0+7=2729` + 1 glob), but claim C moves the tree to 224. If O's
census artifact is produced after C lands, the tool will report `entries=224`
and the four-class totals will differ by the new entry's couples tokens. O03
independently flags the same (`O03-defects-verify.md:241-244`). The census
artifact must pin `baseline_commit` and `entries`, and the integrator must
either (a) measure O's census **before** applying C, or (b) file the 224
reading with the delta explained. This is a filing/ordering decision, not a
scope breach; it does not change the in-province status of either artifact.

**F2 — the landed tool self-reports `"round": 43`.** `payload["round"] = 43`
is hardcoded in the pinned body (fenced line 461; `O02-verify.md:319-327`).
Landing byte-exact means the tool's JSON output will call itself r43. The r44
census artifact must record this as the body's authoring provenance (or the
filing wrapper amends the artifact), not silently present it as an r44
measurement. Not bleed — a provenance label the integrator must not misstate.

**F3 — pre-existing README rev-2.4 prose-vector defect (C02 owns).**
`corpus/README.md:5-12` says the vector moved to `25/23/26/25/24/94`, which
sums to **217**, while the measured directory totals are `25/26/25/29/24/94` =
**223** and the footer at `:548` is already correct. This is not a round-44
scope violation and not caused by this wave; C02's mission already names it.
It is reported here because the C landing must not propagate the stale vector
into rev 2.5 — a README present-tense vector that sums to 217 would be a false
claim in an in-province artifact.

**F4 — the C target is now a two-candidate choice, and only one is fresh.**
`C01-entry-draft.md` now exists: it is a properly fenced, NON-CANON draft with
a §15 canon boundary, so the draft bytes themselves raise no scope issue. But
the wave has two in-province candidates (Addendum C): K04's dream target
(drafted, collision-cleared, but **named in r42** at
`reports/round-42/scout/K02-myth-gaps.md:216`) and K02's cartography target
(undrafted, **not carried**). Claim C's wording at `claims.json:39` requires
"not carried from a prior round", so the freshness clause selects cartography
unless the integrator records a named exception. This seat does not rule on
that — C05's clearance is a collision result, not a freshness result. What
remains `to-verify` either way: C02's README edit, C03's source audit, C04's
contract audit, and the §7 post-landing gate on whichever path is chosen. Never
land both.

## 10. Scope-violation register

| # | Violation | Evidence | Status |
|---|---|---|---|
| — | none observed | §2–§8 | **no entry** |

No canon claim, no lore decision, no packet-surface edit, no sibling/world-bible
write, no `PROVINCE.md` drift, and no out-of-path seat write was observed at
baseline or across the nineteen seat outputs audited (§8A–8C). Two reviewers
filed after that pass and independently corroborate the C conflict without
raising a scope finding (`review/R01-review.md:142-159`,
`review/R02-review.md:25-26`); R02 explicitly leaves the packet-pin leg to this
report (`R02-review.md:19`).

## 11. Limits (`to-verify`)

1. The wave was in flight. Nineteen seat outputs existed at the final pass, but
   C02 (README), C03 (source audit), C04 (contract audit), and all Ca artifacts
   were still absent. C01's draft and both C targets exist (Addenda B/C); their
   scope compliance is gated by §7 and the owning audits, not certified here.
   The carried-vs-fresh C conflict is recorded (§8C), not ruled — that decision
   belongs to the integrator with K02/K04/C05.
2. The corpus delta is necessarily **pre-landing**: seats may only draft
   fenced blocks (`targets.json:6`), and the integrator applies them. This
   report certifies the baseline is clean and supplies the exact post-landing
   check; it does not claim the landing has happened.
3. `PROVINCE.md` accuracy is checked structurally (named paths, partition set,
   ownership split). Domain-description and historical-content accuracy are
   outside a single round's evidence and were not re-adjudicated.
4. Packet-surface digests are SHA-256 at baseline `c9f4eaa`; if the tree moves
   for any unrelated reason before land, the §7.2 check must be read against
   the moved tree, not blindly re-run.

## 12. Reproduce

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin

git rev-parse HEAD                                  # c9f4eaa707b6e…
git status --porcelain corpus tools examples        # empty at baseline
find corpus/knowledge -name '*.md' | wc -l          # 223
for d in corpus/knowledge/*/; do printf '%s ' "$d"; ls "$d"*.md | wc -l; done

awk 'NR>=356 && NR<=870' reports/round-43/op/O09-scribe.md \
  | sha256sum                                        # 43ce341f…ad64
awk 'NR>=356 && NR<=870' reports/round-43/op/O09-scribe.md \
  | grep -nE "open\([^)]*['\"][wa]|\.write\(|subprocess|urllib|http" # empty

sha256sum tools/harness/couples-reference-extractor.py # d8d23a26…
sha256sum examples/handoff-packet.sample.md           # adfd7895…
```
