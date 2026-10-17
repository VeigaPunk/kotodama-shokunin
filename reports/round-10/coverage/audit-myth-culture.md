# R10-C24 — auditor: myth-symbol + culture-material partition counts and index-vs-files diff

- seat: R10-C24 auditor. lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  assignment: *myth-symbol + culture-material counts + diff*; deliverable
  `reports/round-10/coverage/audit-myth-culture.md`.
- date: 2026-10-17. All times below are UTC; the lane's local clock is UTC−03:00
  (= UTC−3). T0 (pre-landing) window 21:26:25Z–21:29:02Z; CLOSE window
  21:40:12Z–21:46:17Z (last command).
- role limits: this seat counts and diffs. Its only write is this file (plus
  scratch under `.scratch/`). It admits no claim, edits no corpus file, and
  absorbs no sibling fragment's evidence as its own. It does not judge
  new-entry quality (that is R10-C11..C20) or index-row prose (R10-C21/C22).
- revision binding: `git rev-parse HEAD` = `e3a1ec9435787328ac9f828f96cb6390e4916b8f`
  ("round-10: availability attempt 3"); declared round-10 `baseline_revision` =
  `9dc18ec1339bffd6f81e74f1a5742464ef578749` ("round-9: admit F/O/D"), and
  `git merge-base --is-ancestor 9dc18ec… HEAD` → true. At T0
  `git diff --name-status 9dc18ec… HEAD -- corpus/knowledge` was empty, i.e.
  both partitions were byte-identical to the baseline; at CLOSE the worktree
  carries the round-10 wave: 10 untracked entries corpus-wide (5 of them in this
  seat's partitions) plus ` M corpus/README.md` (§3.1).
- declared counting command (`reports/round-10/claims.json` C):
  `python3 reports/round-10/run-validation.py` — present from ≈21:31Z; sha256[:16]
  `23d6dc09002fe18c` at CLOSE. This seat did **not execute** the runner (it writes
  `reports/round-10/validation.json`, another seat's filed artifact); it imported
  the module read-only and called `entry_checks()` directly. No file was written
  by that import.

## 1. Verdict

1. **T0: both partitions were unchanged from the round-9 close, and their indexes
   were exact.** myth-symbol 16 files = 16 index rows = header `(16)`;
   culture-material 16 = 16 = 16; zero rows without files, zero files without
   rows, zero duplicate rows (§2.3). No round-10 entry had landed in either
   partition at T0 (`git status --porcelain` empty at 21:27:20Z, §2.1), so the
   C-claim partition minimums were **not yet satisfied at T0** — a scheduling
   fact, not a finding against any worker.
2. **CLOSE: myth-symbol 19 files (16 + 3), culture-material 18 files (16 + 2).**
   Both partitions clear the C-claim minimum (≥2 each); the five new entries are
   listed and digest-pinned in §4. Landing timeline from this seat's 60 s poll
   (`.scratch/r10c24-poll.log`, scratch/disposable; quoted §3.1): 16/16 through
   21:31:46Z; 16/17 at 21:32:46Z; 18/17 at 21:34:31Z; **19/18 from 21:38:01Z**,
   stable through 21:45:01Z.
3. **Index-vs-files is exact for both partitions at CLOSE, both directions.**
   header = index rows = on-disk files: myth-symbol **19 = 19 = 19**;
   culture-material **18 = 18 = 18**; zero missing rows, zero phantom rows, zero
   duplicate rows (§3.2).
4. **README global counts reconcile at CLOSE.** Section headers sum **189**
   (linguistics 19, myth-symbol 19, culture-material 18, synthesis 24,
   verification 15, civilizations 94) = footer line "Total knowledge entries:
   189." = `find corpus/knowledge -name '*.md' | wc -l` = **189** (§3.2).
   README digest at CLOSE `9df4b7c579b89d6ff51ace4600cb0518b897d2e6d0819150e3fde6bbf5b8333c`,
   stable from 21:40:12Z to 21:46:17Z.
5. **Frontmatter readings at CLOSE.** **A** (strict singular `- source:` +
   `verified-at:` + `recheck:` in the opening block): myth-symbol **19/19**,
   culture-material **0/18**. **B** (singular *or* plural source leg):
   19/19 and 18/18. **C** (anywhere): 19/19 and 18/18. The culture-material
   A-gap is the documented fleet-text question, not a round-10 defect: the same
   measurement over the whole corpus at T0 reproduces round-9's close exactly —
   **A 64/179 missing, B 3/179 (the same three `verification/` files),
   C 0/179** (§2.4). The two new culture-material entries follow the partition's
   established plural-only form.
6. **Entry-level gate over both partitions at CLOSE:**
   `python3 tools/gates/provenance-audit.py corpus/knowledge/myth-symbol/ corpus/knowledge/culture-material/`
   → `files=37 marks=45 mark-lines=41 findings=0 blocked=0`, exit 0 (§3.3). The
   other six gates take a culture packet (`<culture-packet.yml>`), not corpus
   entries, so they are not applicable to this surface (usages captured §6).
7. **Two of the five new entries fail the declared counting command's per-entry
   legs** — finding **F1** (§5), digest-paired: `transport-mobility-lexicon.md`
   fails the *named-gap* leg; `plant-symbolism.md` fails the *named-gap* leg
   **and** the *retrievable-locator* leg. The other three pass all four legs.
   This seat does not disposition F1: both entries name their gaps and cite
   sources in prose forms the runner's regexes do not accept (§4, §5), so the
   fix is entry-side (add the accepted form) or runner-side (widen the regexes)
   — the parent's / X03's call.
8. **No duplication.** Each of the five new entries shares fewer than four
   content terms (len>3) with every one of the 179 baseline titles, and with each
   other — no near-duplicate of a committed entry (§3.4).
9. **Fragment coverage for the five new entries holds at CLOSE.** Each is named
   in ≥1 `reports/round-10/coverage/*.md` fragment (the runner's `unmentioned`
   check), and all ten authorship fragments `C01.md`…`C10.md` are present
   (§3.5).

## 2. T0 measurements (pre-landing), 21:26:25Z–21:29:02Z

### 2.1 Revision, cleanliness, baseline identity

```
$ git rev-parse HEAD
e3a1ec9435787328ac9f828f96cb6390e4916b8f
$ git merge-base --is-ancestor 9dc18ec1339bffd6f81e74f1a5742464ef578749 HEAD && echo ancestor
ancestor
$ git diff --name-status 9dc18ec1339bffd6f81e74f1a5742464ef578749 HEAD -- corpus/knowledge/
(empty)
$ git status --porcelain corpus/knowledge/ corpus/README.md        # 21:27:20Z
(empty)
```

Both partitions and the README were, at T0, the committed bytes of the declared
baseline — every T0 count below grades bytes identical under both revisions.

### 2.2 Counts

```
$ ls -1 corpus/knowledge/myth-symbol/*.md | wc -l
16
$ ls -1 corpus/knowledge/culture-material/*.md | wc -l
16
$ find corpus/knowledge -name '*.md' | wc -l
179
$ python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge | head -20
  ... "totals": { "files": 179, "files_with_any_mark": 128, ... }, exit=0
```

### 2.3 Index-vs-files (T0), both partitions

Script (row = `^- \`<file>.md\`` inside the partition's `## <partition>/ (N)`
section, up to the next `## `):

```
python3 - <<'PY'
import os, re
root="corpus/knowledge"; readme="corpus/README.md"
txt=open(readme,encoding="utf-8").read()
for part in ("myth-symbol","culture-material"):
    files=sorted(f for f in os.listdir(os.path.join(root,part)) if f.endswith(".md"))
    m=re.search(r"^## %s/ \((\d+)\)\s*$"%(re.escape(part)), txt, re.M)
    nxt=re.search(r"^## ", txt[m.end():], re.M)
    body=txt[m.end(): m.end()+nxt.start()]
    rows=re.findall(r"^- `([^`]+\.md)`", body, re.M)
    print(part, f"files={len(files)} header={m.group(1)} rows={len(rows)}",
          "files_not_indexed=",sorted(set(files)-set(rows)),
          "rows_missing_file=",sorted(set(rows)-set(files)))
PY
```

Observed 21:26:25Z:

```
myth-symbol      files=16 header=16 rows=16 files_not_indexed=[] rows_missing_file=[]
culture-material files=16 header=16 rows=16 files_not_indexed=[] rows_missing_file=[]
```

Corpus-wide at 21:29:02Z (basename join, all partitions): on_disk=179,
index_rows=179, rows_without_file=[], files_without_row=[], duplicate_basenames=[].
Each of the 16+16 index rows also carries a non-empty description whose first
terms overlap its entry's `- topic:` line (0 low-overlap flags in both
partitions) — rows are not stale against entry topics at T0.

### 2.4 Corpus-wide source-leg readings A/B/C (regression check)

```
python3 - <<'PY'
import re, pathlib
root = pathlib.Path('corpus/knowledge')
def head(t): return re.split(r'^## ', t, maxsplit=1, flags=re.M)[0]
A=B=C=0; n=0; bmiss=[]
for p in sorted(root.rglob('*.md')):
    n+=1; t=p.read_text(encoding='utf-8'); h=head(t)
    a = bool(re.search(r'^-\s*source\s*:',h,re.M)) and bool(re.search(r'^-\s*verified-at\s*:',h,re.M)) and bool(re.search(r'^-\s*recheck\s*:',h,re.M))
    b = bool(re.search(r'^-\s*sources?\s*:',h,re.M)) and bool(re.search(r'^-\s*verified-at\s*:',h,re.M)) and bool(re.search(r'^-\s*recheck\s*:',h,re.M))
    c = bool(re.search(r'(?:^[-*]\s|;\s)sources?\s*:',t,re.M)) and bool(re.search(r'(?:^[-*]\s|;\s)verified-at\s*:',t,re.M)) and bool(re.search(r'(?:^[-*]\s|;\s)recheck\s*:',t,re.M))
    A+=a; B+=b; C+=c
    if not b: bmiss.append(p.as_posix())
print(f"files={n}  A={A}/{n} missing={n-A}   B={B}/{n} missing={n-B}   C={C}/{n} missing={n-C}")
print("B-remainder:", bmiss)
PY
```

Observed 21:28:21Z:

```
files=179  A=115/179 missing=64   B=176/179 missing=3   C=179/179 missing=0
B-remainder: ['corpus/knowledge/verification/citation-format-and-source-registry.md',
 'corpus/knowledge/verification/myth-consistency-gate.md',
 'corpus/knowledge/verification/provenance-audit-ledger-format.md']
```

This reproduces round-9's close-of-round table verbatim
(`reports/round-9/metadata/audit.md` §1: A 64/179, B 3/179, C 0/179, same
B-remainder) — **no regression on this axis**, and the same open fleet-text
question (singular `source:` vs plural `sources:`) is still unresolved rather
than newly broken. Partition-scoped T0 values: myth-symbol A/B/C = 16/16/16;
culture-material = 0/16, 16/16, 16/16.

### 2.5 Frontmatter census, duplication, dangling refs (T0)

- Field census (opening block, fields `topic, sources, couples, source,
  verified-at, recheck`, each exactly once, in that order): myth-symbol
  **nonconforming=0/16**; culture-material nonconforming=16/16 — all sixteen
  carry `sources:` but no singular `- source:` line (the reading-A gap above,
  matching round-9 V10's criterion, which accepts the plural form).
- Cross-partition digest duplication: no two files in the two partitions share a
  sha256 (`duplicates: none`).
- `couples` reference resolution: culture-material 206 refs, 0 dangling;
  myth-symbol 100 refs, 2 regex hits that are **prose shorthands, not path
  claims** — `culture-material/costume files` in `color-symbolism.md:4,163` and
  `culture-material/crafts` in `pantheon-archetypes.md:25` — cleared by reading
  the contexts; no dangling path claim exists.

## 3. CLOSE measurements, 21:40:12Z–21:46:17Z

### 3.1 Counts and the landing timeline

```
$ ls -1 corpus/knowledge/myth-symbol/*.md | wc -l      # 21:46:10Z
19
$ ls -1 corpus/knowledge/culture-material/*.md | wc -l # 21:46:10Z
18
$ git ls-files --others --exclude-standard -- corpus/knowledge
corpus/knowledge/culture-material/transport-mobility-lexicon.md
corpus/knowledge/culture-material/vessel-container-lexicon.md
corpus/knowledge/linguistics/language-shift-obsolescence-revival.md
corpus/knowledge/linguistics/numerals-and-measures.md
corpus/knowledge/linguistics/sound-symbolism.md
corpus/knowledge/myth-symbol/direction-symbolism.md
corpus/knowledge/myth-symbol/divination-omen-systems.md
corpus/knowledge/myth-symbol/plant-symbolism.md
corpus/knowledge/verification/header-conformance-readings.md
corpus/knowledge/verification/verification-independence-anti-circularity.md
```

Poll receipts (60 s cadence, `.scratch/r10c24-poll.log`, scratch/disposable;
columns: UTC time, myth files, culture files, `git status --porcelain
corpus/knowledge/` line count):

```
2026-10-17T21:26:46Z myth=16 culture=16 untracked_or_modified=0
2026-10-17T21:29:46Z myth=16 culture=16 untracked_or_modified=0
2026-10-17T21:30:46Z myth=16 culture=16 untracked_or_modified=1
2026-10-17T21:31:46Z myth=16 culture=16 untracked_or_modified=2
2026-10-17T21:32:46Z myth=16 culture=17 untracked_or_modified=3
2026-10-17T21:34:31Z myth=18 culture=17 untracked_or_modified=6
2026-10-17T21:36:16Z myth=18 culture=17 untracked_or_modified=8
2026-10-17T21:38:01Z myth=19 culture=18 untracked_or_modified=10
2026-10-17T21:45:01Z myth=19 culture=18 untracked_or_modified=10
```

(Full log lines 21:26:46Z…21:50:16Z are in that file; the lines elided above are
the same series at 21:27:46Z, 21:28:46Z, 21:39:46Z, 21:41:31Z, 21:43:16Z. The
file is scratch and disposable; the load-bearing evidence is the dated command
outputs quoted in this fragment.)

Post-CLOSE stability re-check, 21:51:52Z (five minutes after the CLOSE window):
counts still 19 / 18, `corpus/README.md` still `9df4b7c579b89d6f…`, and the
poll series held `myth=19 culture=18` on every tick from 21:38:01Z through
21:50:16Z (late log lines: `21:46:46Z`, `21:48:31Z`, `21:50:16Z`, all
`myth=19 culture=18 untracked_or_modified=10`). This fragment's CLOSE numbers
therefore also describe the tree five minutes later; re-pin the digests before
reusing them (F5).

### 3.2 Index-vs-files at CLOSE

```
myth-symbol      files=19 header=19 rows=19 missing_rows=[] phantom=[] dups=[]
culture-material files=18 header=18 rows=18 missing_rows=[] phantom=[] dups=[]
headers=[('linguistics','19'),('myth-symbol','19'),('culture-material','18'),
         ('synthesis','24'),('verification','15'),('civilizations','94')]
sum=189  total_line=189  on_disk=189
$ sha256sum corpus/README.md
9df4b7c579b89d6ff51ace4600cb0518b897d2e6d0819150e3fde6bbf5b8333c  corpus/README.md
```

README index-row text at CLOSE: 43 `## myth-symbol/ (19)`, 65
`## culture-material/ (18)`, 302 `Total knowledge entries: 189.` The two new
rows per partition are present by exact `^- \`<file>\` — ` form (row presence is
verified; row *prose* is R10-C21/C22's surface).

### 3.3 Entry-level gate at CLOSE

```
$ python3 tools/gates/provenance-audit.py corpus/knowledge/myth-symbol/ corpus/knowledge/culture-material/
... INFO scan: files=37 marks=45 mark-lines=41 findings=0 blocked=0
exit=0
```

(T0 value for the same command: files=32 marks=15 mark-lines=15 findings=0
blocked=0, exit 0. The mark rise is the new entries' own `to-verify` inventory —
a marker count, not a verdict.)

### 3.4 Duplication at CLOSE

For each new entry: title content terms (len>3) intersected with each of the 179
baseline titles; maximum overlap observed < 4 in every case (no candidate row
emitted), and no new entry's slug or title collides with an existing file. Script
in §6.

### 3.5 Declared-runner per-entry legs, digest-paired (21:46:17Z)

`run-validation.py` sha256[:16] `23d6dc09002fe18c`; `corpus/README.md`
sha256[:16] `9df4b7c579b89d6f`. Read-only import of the runner module; no write.

```
5a6ef38fdec92e6d  gap=True  decision=True  fm_missing=[]  locators=22  direction-symbolism.md
a9fd5e8fc2b00529  gap=False decision=True  fm_missing=[]  locators=0   plant-symbolism.md
6666e7dbd5cc5a4b  gap=True  decision=True  fm_missing=[]  locators=17  divination-omen-systems.md
d0a2c836a838c0a6  gap=False decision=True  fm_missing=[]  locators=6   transport-mobility-lexicon.md
073e7fc54b600a81  gap=True  decision=True  fm_missing=[]  locators=26  vessel-container-lexicon.md
```

Fragment mention check (each new entry named in ≥1 coverage fragment):

```
direction-symbolism        -> C04.md C06.md review-C04.md audit-unchanged.md
plant-symbolism            -> C04.md C06.md review-C04.md audit-unchanged.md
divination-omen-systems    -> C05.md review-C04.md
transport-mobility-lexicon -> C07.md C08.md review-C07.md review-C08.md audit-unchanged.md
vessel-container-lexicon   -> C07.md review-C08.md
```

Authorship fragments present: `C01.md C02.md C03.md C04.md C05.md C06.md
C07.md C08.md C09.md C10.md` (10/10 at CLOSE).

## 4. New-entry ledger — this seat's partitions

| entry | partition | sha256[:16] @21:46:17Z | lines | author seat | runner legs (gap / decision / fm / locators) |
|---|---|---|---|---|---|
| `direction-symbolism.md` | myth-symbol | `5a6ef38fdec92e6d` | 202 | C04 | pass / pass / pass / 22 |
| `plant-symbolism.md` | myth-symbol | `a9fd5e8fc2b00529` | 196 | C06 | **FAIL** / pass / pass / **0** |
| `divination-omen-systems.md` | myth-symbol | `6666e7dbd5cc5a4b` | 218 | C05 | pass / pass / pass / 17 |
| `transport-mobility-lexicon.md` | culture-material | `d0a2c836a838c0a6` | 128 | C07/C08 | **FAIL** / pass / pass / 6 |
| `vessel-container-lexicon.md` | culture-material | `073e7fc54b600a81` | 175 | C07/C08 | pass / pass / pass / 26 |

Full digests: `direction-symbolism`
`5a6ef38fdec92e6db552cdd4e3d5f264cb19fb105d7881676ab73d86d3a35426`;
`plant-symbolism`
`a9fd5e8fc2b005293569b9bd7225a4a42002183458aa7e36ece147793623d63f`;
`divination-omen-systems`
`6666e7dbd5cc5a4bd9833b3e842843854af8ef7b365396c6d1737aac8cbf2ba4`;
`transport-mobility-lexicon`
`d0a2c836a838c0a6b5830d8413610687d993d08b0df92244b7a9304c077dd8ab`;
`vessel-container-lexicon`
`073e7fc54b600a81a75e0db480f73597e2295f8daa317a74e9246846b5de2df3`.

Attribution note: author fragments self-identify as C04 = direction register,
C06 = `plant-symbolism.md`, C07/C08 = the two culture-material entries; C05's
fragment (`C05.md`) is the third myth-symbol seat, whose entry is
`divination-omen-systems.md` (the only myth-symbol new entry whose fragment is
C05.md). This seat verified only that each entry has ≥1 mentioning fragment, not
which seat authored which file.

## 5. Findings and observations

**F1 — HIGH — two new entries fail the declared counting command's per-entry
legs.** Evidence: §3.5 (digest-paired, runner sha256[:16] `23d6dc09002fe18c`).
The legs come from `reports/round-10/run-validation.py` `entry_checks()`
(`:349`), with `gap_field` at `:363`, `gap_heading` at `:365`, `decision` at
`:368`, `URL_RE` at `:110`, `REPO_PATH_RE` at `:111`.

- `culture-material/transport-mobility-lexicon.md` — *named-gap* leg fails: the
  file contains **zero** occurrences of the string `gap` (case-insensitive,
  `grep -c -i gap` → 0). It states its contribution in `## 11. Handoff note`,
  line 126: `- **This entry supplies**: the four-layer frame, the
  route-institution table, …`, which is a gap statement in substance but not in
  the runner's accepted forms (`gap:` / `gap filled:` / `gap addressed:` /
  `gap served:` in prose, or a `## ` heading containing `gap`).
- `myth-symbol/plant-symbolism.md` — *named-gap* leg fails **and**
  *retrievable-locator* leg fails: the file names its gap twice — `- topic:`
  line 3 ("… the gap this entry fills, since the partition covers fauna
  (`animal-symbolism.md`) but has no flora file …") and body line 12
  (`- **The gap statement.** This partition covers fauna in depth …`) — but
  neither matches the runner's regexes (no `gap:` colon form; no heading
  contains `gap`). Locators: `grep -c 'http'` → 0 and `grep -c 'corpus/'` → 0,
  so neither `URL_RE` nor `REPO_PATH_RE` matches; the entry's sources name
  venues in prose (e.g. voluspa.org) and cite in-corpus files without the
  `corpus/` prefix (e.g. `myth-symbol/celestial-symbolism-calendars.md` in its
  `- recheck:` line), which the runner does not count as a locator.
- Consequence: with these bytes, claim C cannot pass the runner's per-entry
  checks for these two entries regardless of the other partitions. Disposition
  is **not** this seat's: entry-side fix (add a runner-recognized `gap:` line /
  URL or `corpus/…` path) and runner-side widening (accept `**…gap…**` lines and
  bare `partition/file.md` paths) are both available; the reviewers
  (`review-C06.md`, `review-C07.md`, `review-C08.md`) and X03 own the call.
  Recorded here because the auditor's count is what the round's acceptance
  command will read.

**F2 — DOCUMENTED, no action — culture-material fails reading A of the source
leg (0/18).** This is the pre-existing open fleet-text question (singular
`source:` vs plural `sources:`), unchanged by round 10: corpus-wide A/B/C at T0
reproduces round-9's close exactly (§2.4), and the two new culture-material
entries follow the partition's established plural-only form. Under the runner's
own `C_FRONTMATTER_FIELDS` (`:81`) the source leg reads the plural form, so this
is not an acceptance failure; it is recorded so a later strict-A sweep does not
read the 18 files as new debt.

**F3 — OBSERVATION (cross-shard, not this seat's) — filed/other-surface bytes
modified in the live tree.** During the CLOSE window `git status --porcelain`
shows ` M SKILL.md`, ` M corpus/README.md`, ` M reports/round-9/validation.json`
(plus, transiently, `M reports/round-5/validation.json` observed by sibling
reviewers). The round-10 F targets say "never rewrite filed report bytes —
corrections are new entries"; whether these are authorised F-seat
regenerations or an unlogged overwrite is the parent's call. Observed
read-only; not dispositioned here.

**F4 — OBSERVATION — hard-link counts on new entries fluctuate.** `stat -c '%h'`
on the new entries returned 20 / 2 / 1 at 21:34Z and 1 / 20 / 1 at 21:35:51Z —
sibling seats copy trees with hard links, so a byte write through either path is
visible at both; inode identity, not duplication. Noted so a later reader does
not read the changing `ls -l` link column as file churn. (The `find . -samefile`
sweep found no in-repo second link; the other links point outside the repo.)

**F5 — NOTE — one entry was revised mid-audit.** `divination-omen-systems.md`
digest moved `d1d938a1771d8ff0` (21:40:12Z) → `6666e7dbd5cc5a4b` (21:43:10Z),
and `transport-mobility-lexicon.md` moved `36a7370ff49cda98` (21:40:12Z) →
`d0a2c836a838c0a6` (21:46:10Z); both were re-checked after the change, and all
verdicts quoted in §3.5 are digest-paired to the CLOSE bytes. Anyone re-running
these checks later must re-pin the digests.

## 6. Re-runnable command block

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch

# 1. counts
ls -1 corpus/knowledge/myth-symbol/*.md | wc -l
ls -1 corpus/knowledge/culture-material/*.md | wc -l
find corpus/knowledge -name '*.md' | wc -l
python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge

# 2. index-vs-files, both partitions + global totals
python3 - <<'PY'
import re, pathlib
txt=open('corpus/README.md',encoding='utf-8').read(); root=pathlib.Path('corpus/knowledge')
for part in ("myth-symbol","culture-material"):
    files=sorted(p.name for p in (root/part).glob('*.md'))
    m=re.search(r"^## %s/ \((\d+)\)\s*$"%(re.escape(part)), txt, re.M)
    nxt=re.search(r"^## ", txt[m.end():], re.M); body=txt[m.end(): m.end()+nxt.start()]
    rows=re.findall(r"^- `([^`]+\.md)`", body, re.M)
    print(part, f"files={len(files)} header={m.group(1)} rows={len(rows)}",
          sorted(set(files)-set(rows)), sorted(set(rows)-set(files)))
hdrs=re.findall(r'^## ([a-z-]+)/ \((\d+)\)\s*$', txt, re.M)
print("sum_headers=", sum(int(c) for _,c in hdrs),
      "total_line=", re.search(r"(?m)^Total knowledge entries:\s*(\d+)\.", txt).group(1),
      "on_disk=", len(list(root.rglob('*.md'))))
PY

# 3. entry-level gate (entry files; the other six gates take a culture-packet.yml)
python3 tools/gates/provenance-audit.py corpus/knowledge/myth-symbol/ corpus/knowledge/culture-material/

# 4. declared-runner per-entry legs, read-only (does NOT write validation.json)
python3 - <<'PY'
import importlib.util, hashlib, os
spec=importlib.util.spec_from_file_location("rv","reports/round-10/run-validation.py")
rv=importlib.util.module_from_spec(spec); spec.loader.exec_module(rv)
for rel in sorted(os.popen("git ls-files --others --exclude-standard -- corpus/knowledge/myth-symbol corpus/knowledge/culture-material").read().split()):
    d=hashlib.sha256(open(rel,'rb').read()).hexdigest()[:16]; r=rv.entry_checks(rel)
    print(d, f"gap={r['gap']} decision={r['decision_record']} fm={r['missing_frontmatter']} locators={len(r['locators'])}", rel)
PY
```

## 7. Handoff notes

- Write scope respected: this file is the only write of this seat (plus
  `.scratch/r10c24-poll.log` and `.scratch/r10c24-titles-baseline.txt`, both
  untracked scratch). No corpus file, README row, gate, or filed receipt was
  edited; no git operation was performed.
- Two independent count methods agree on both partitions (glob count and
  README-section parse; §2.2/§2.3, §3.1/§3.2), and the corpus-wide total
  reconciles three ways (headers sum, footer line, disk walk).
- The C-claim minimums for this seat's partitions are **satisfied** at CLOSE
  (myth-symbol +3 ≥ 2, culture-material +2 ≥ 2); the residual risk to claim C
  from this surface is F1 (two entries failing the runner's own per-entry legs),
  not the counts.
- F1 needs a disposition before round acceptance is re-run; re-running
  `python3 reports/round-10/run-validation.py` after any entry-side edit will
  change `reports/round-10/validation.json` (X03's artifact), so the re-run
  belongs to X03/the parent, not to this seat.
