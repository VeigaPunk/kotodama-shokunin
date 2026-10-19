# C08 — source-shelf verification (claim C, non-author)

- Seat: `C08` | role: verifier | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7`
- Out path: `reports/round-48/cov/C08-shelf.md` (this file)
- Mission: verify the cartography entry's source shelf — external shelf honestly marked `(to-verify)`, no unread work asserted-read, in-corpus shelf resolves, no fabricated source.
- Non-author statement: I drafted no entry fragment and edited no shelf. Every judgement is from live HEAD bytes or the r48 filed bytes pinned in §1; commands are in §8.

**Verdict in one line.** Honesty passes; **shelf unity fails**. The C02 head (the assembly spec's landing head) is per-item marked and digest-pinned but **omits eight works the body names** (four secondary, four primary/exemplar); the C01 entry's own shelf is body-closed but carries **one blanket `(to-verify)` over twenty works** and a head block the assembly spec says it does not have. Both r47 shelf blockers I was prepared to flag are already fixed in the live draft. No fabricated source detected; no unread work is presented as inspected.

**Read-cut note.** At my first read cut `reports/round-48/cov/` was empty; the C01/C02 drafts appeared while this seat ran. I re-audited the real bytes and pinned them. The files are being written concurrently by other seats, so this verdict is **at these digests**, not at any later revision:

| Artifact | Lines | sha256 |
|---|---:|---|
| `reports/round-48/cov/C02-header.md` | 263 | `2ff5b15da54eba4ff2f99be0eac2ba6e584b3edf782ac546b6241b067bd96653` |
| C02 fenced head block (extracted) | 23 | `708dec15e0fb2563c258a680800e20892719c1480b0c364507c5799edf849816` |
| `reports/round-48/cov/C01-entry.md` | 473 | `4c2815a766f12926ba14e14e2b164a8f65245a246223ae4258993e0a831c272d` |
| C01 fenced entry block (extracted, head + body) | 228 | `e52556572341bd82545f841cee01e7bf2c581c268910ff2a6f0c2f087cf44f84` |

---

## 1. What each draft carries

| | C02 head | C01 entry (head + body) |
|---|---|---|
| In-corpus shelf bullets | 11 files | 11 files (inline, not bulleted) |
| sha256 pins | **11** (all unique) | **0** |
| External shelf works | **10** | **20** |
| Inline `(to-verify)` on external shelf | **10 of 10** (per item) | **1**, a blanket over all 20 |
| Couples targets | 19 backticked, 19 resolve | 14 plain paths, 14 resolve |
| Anchor tokens (head block) | 66 | 75 |
| Head fields | 8, correct order | 7 (`- source:` missing; `gap filled` before `topic`) |
| Body | none (head only) | 228 fenced lines, head + body |

`reports/round-48/cov/W01-landing-spec.md:78-79` designates C02's fence as the complete head and C01's fence as **"body only (first line `## 1.`; no second H1, no head fields)"**. C01's fence does not match that description: its first line is an H1 and it carries head fields (`C01-entry.md:67`: "Fenced block = the complete entry (head block + body)"). See S2.

---

## 2. In-corpus shelf — resolves, and the C02 pins are current

All 11 C02 anchor files exist and all **11 sha256 pins match the live `a01405d` tree**:

| File | sha256 at `a01405d` | Pin |
|---|---|---|
| `myth-symbol/cosmology-cosmography.md` | `165f292b95852459842900a091c6a40e1cd39b209b8fe2d84e62ecad6266ed2e` | yes |
| `myth-symbol/sacred-topography-pilgrimage.md` | `241113b5a1259b04de889ebc458736ab8860e015b9afa9f74479bcc8bc165459` | yes |
| `myth-symbol/direction-symbolism.md` | `5a6ef38fdec92e6db552cdd4e3d5f264cb19fb105d7881676ab73d86d3a35426` | yes |
| `culture-material/architecture-settlement-lexicon.md` | `9af04e751206c32bc1ca38a73ef16a27a3e2e4a696454dd1bb5e22ed27bada9f` | yes |
| `culture-material/writing-media-surface-economy.md` | `f039e6e120ed050ff16adebc0ad5cd9cff7965337799fe7cbc725ba0823d4601` | yes |
| `culture-material/transport-mobility-lexicon.md` | `86e5f9520e07e3ebb5d518183bb273d1ee8c22cca9c3ef1d35cf8fcef6d5aa70` | yes |
| `culture-material/craft-artisan-lexicon.md` | `fd678d82fcc5134f5c5c0a65b15106b35cabe67bfd935d45df4fa16524f30288` | yes |
| `culture-material/trade-economy-lexicon.md` | `760a9df61364916b69e91c4d7f21ee4bff6bf138af6643f585afdcb10f05f277` | yes |
| `civilizations/mesoamerica-primary-sources.md` | `d04d8913e704961533d123857d87c93d8cfc25b89c854b1f6c3f5bcf1d0db530` | yes |
| `linguistics/naming-systems.md` | `d972a1d65e7a8fba34f44e1cd57019c175a8ed24671ef95f3e0ea3d1ed9ffb3d` | yes |
| `verification/calibration-registry.md` | `cf7cceee9008a9db768d074671f490e4e99feb59ed4e10fb21fa0b72a4e0454c` | yes |

The r47 shelf blockers are fixed in the live draft, verified independently:

- **"six" → "eleven"**: C02:117 says eleven and eleven are pinned (measured `digest pins: 11 knowledge + 1 aux`; the aux is the `corpus/README.md` digest in `verified-at`, correctly not a shelf pin).
- **craft ladder**: C02:124 cites `:54-65` and explicitly rejects `:44`; live `:44` is the steel-grading row and `:54` is the ladder header.
- **B3**: `naming-systems.md:70` is quoted verbatim ("Every renaming is datable; a map is an archive of coups"), with no "correction" proposed.
- **B8**: `cosmology-cosmography.md:27` is quoted and dispositioned in `- gap filled:`.

Anchor resolution: **66/66** anchor tokens in the C02 block and **75/75** in the C01 block resolve to an existing line (instrument §7). The only unresolved paths are the expected ones — the proposed slug and a `reports/` context path. Couples: C02 19/19, C01 14/14 resolve.

---

## 3. External shelf — honesty passes, closure fails

### 3.1 Marker posture

- **C02: 10 works, 10 per-item `(to-verify)`.** The shelf header says "not consulted this round (no network at seat time); … every edition, volume and page locator `(to-verify)`; no unread work is presented as inspected" (`C02:129`). This is the correct shape.
- **C01: 20 works, 1 blanket `(to-verify)`.** The header says "Every item is `(to-verify)` for edition, volume and page" (`C01:76`). Substantively honest — no work is asserted-read — but `to-verify-triage-protocol.md:15` says: "Attach it to the smallest uncertain proposition, **not to a whole culture or bibliography**." A single mark over 20 works is that anti-pattern (S3).
- **No external work is asserted-read** in either draft. Both say "not consulted"; C01's §13 adds "the historical dates are not [arithmetic]" and the shelf is explicitly a reading list.
- **Body sweep:** C01's body has 8 lines naming an external author without an inline marker. Four are the form-table rows (covered by that table's column header "Real exemplar (`to-verify` for edition)"); four are calibration rows at `C01:275-280` (Harley/Wood, Russell, Mundy, al-Idrisi/Needham) with no row-level mark (S6). C02's head has 0.

### 3.2 Shelf–body closure — the blocking finding

C01's body names **12 external works/exemplars** (the count that matters for closure). C01's shelf lists 20 — a superset of C02's 10 — but still omits **Needham** and the two table-marked exemplars, Snow and Minard. C02's shelf lists 10 and omits **eight** body-named works:

| Work named in the C01 body | Body line(s) | On C01 shelf | On C02 shelf |
|---|---|---|---|
| Harley (1989) | 275 | yes | yes |
| Wood (1992) | 275 | yes | yes |
| Campbell (1987) | 277 | yes | yes |
| Kain & Baigent (1992) | 146 | yes | yes |
| Mundy (1996) | 278, 280 | yes | **no** |
| al-Idrisi (1154) | 280 | yes | **no** |
| Russell (1991) | 276 | yes | **no** |
| Needham | 280 | **no** | **no** |
| *Tabula Peutingeriana* | 145 | yes | **no** |
| Mercator (1569; *Atlas* 1595) | 172 | yes | **no** |
| Snow 1854 | 151 | **no** | **no** |
| Minard 1869 | 151 | **no** | **no** |

Of these, four are secondary works missing from C02's shelf (Mundy, al-Idrisi, Russell, Needham) and four are primary works or exemplars (*Tabula*, Mercator, Snow, Minard); the form table marks the exemplar column "`to-verify` for edition", so Snow and Minard are marked even though they are not shelf entries. The defect is one-directional: **body ⊆ shelf**. A shelf wider than the body is fine; C02 carries five works the body does not name (Monmonier, Jacob, Ptolemy, Snyder, Dilke) and C01 carries four more (Edson, Boone, Pickles, Buisseret), which is reading-list breadth, not a defect.

Evidence: `C01-entry.md:145-152` (form exemplars), `:172` (Mercator in the projection table), `:275-280` (calibration rows); C02 shelf `:129`; C01 shelf `:76`.

### 3.3 Fabrication check — what can and cannot be concluded

- **No invented-looking entry found.** Every work is a standard cartographic reference cited at book level; no page, percentage or quotation is presented as inspected.
- **Corroboration is thin:** only Boone (2000) is independently registered in-corpus (`myth-symbol/direction-symbolism.md:78`). The other `Harley` hit in the corpus (`civilizations/celts.md:167`) is "British Library Harley MS 5280" — the Harleian collection, not J. B. Harley, and is **not** corroboration.
- **Limit:** no network. I did not check an imprint, edition, volume or page against a catalogue. "Not fabricated" means *nothing is presented as read and every uncertain locator is marked*; it does not mean the bibliography is bibliographically confirmed.

---

## 4. Findings

Severity: **B** = must fix before apply; **P1/P2/P3** = should fix / note.

| ID | Sev | Location | Finding | Evidence | Fix |
|---|---|---|---|---|---|
| **S1** | **B** | C02 shelf `:129` vs C01 body `:145-152`, `:172`, `:275-280` | **Shelf–body non-closure.** The head W01 designates for landing lists 10 works; the body names 12. Eight body-named works have no C02 shelf entry: Mundy, al-Idrisi, Russell, Needham (secondary) and the *Tabula Peutingeriana*, Mercator, Snow, Minard (primary/exemplar). | Table §3.2; C02 shelf work count 10; C01 shelf 20. | Merge C01's 20-item set into the landing head, add Needham, and keep the exemplar-column mark (addendum §5). |
| **S2** | **B** | `C01-entry.md:67`, fence `:70-298`; `W01-landing-spec.md:79` | **Assembly contradiction.** W01 says C01's fence is "body only (first line `## 1.`; no second H1, no head fields)". The fence actually starts with an H1 and 7 head fields; C01's own text says "complete entry (head block + body)". Concatenating per the spec duplicates the H1 and the head fields. The C01 head is also **missing `- source:`** and orders `gap filled` before `topic`, and C01:9's "11-field head block" is false — 7 fields are present. | Extracted block first line is the H1; field scan: `gap filled` (72), `topic` (73), `sources` (74), `couples` (77), `verified-at` (78), `recheck` (79), `scope` (80). W01:79 quoted. | Land **one** head (C02's, 8 fields). Slice C01's fence at the first `## 1.` for the body. Do not use C01's head. (W01/C13 own the wire; this is the shelf's delivery path.) |
| **S3** | P1 | C01 shelf `:76` | One blanket `(to-verify)` over 20 works — the triage protocol's named anti-pattern. | `to-verify-triage-protocol.md:15`, quoted §3.1. | Carry C02's per-item marks when merging. |
| **S4** | P2 | C02:128 | `:78-88` overshoots: `:78` is the CAL-03 heading, `:87` the last content line, `:88` blank, `:89` CAL-04. | `sed -n '86,90p'`; file is 190 lines. | `:78-87`. |
| **S5** | P2 | C02:143 | "this block keeps the shelf at 2 lines" — the external shelf is **1 physical line**. The 23-line block count is correct; the shelf sub-count is not. | Extracted block: 23 lines; lines containing "External standard shelf": **1**. | Say "1 line", or drop the sub-count. |
| **S6** | P2 | C01:275-280 | Four calibration rows cite external works (275 Harley/Wood; 276 Russell; 278 Mundy; 280 al-Idrisi/Needham) with no row-level or table-level mark; only the shelf blanket and §13 cover them. | Body sweep: 4 unmarked calibration rows. | Add a table caption "all external attributions `(to-verify)`" or per-row marks. |
| **S7** | P3 | C02:118; C01 shelf prose | `:102` is quoted as "not cartographic"; the live phrase is "not cartographic claims". Truthful substring, but the marks do not signal the truncation. | `sed -n '102p'`. | Quote the full phrase or add an ellipsis. |
| **S8** | P3 | C01 in-corpus shelf `:75` | No sha256 pins. C01 says every line was re-read, but the pin is the durable evidence; C02's 11 pins are stronger. | `digest pins: 0 knowledge` on the C01 block. | Carry C02's 11 pins into the merged head. |
| **S9** | P3 | C01:280 vs both shelves | Needham is cited in the diffusion calibration row but appears on neither shelf. (At an earlier read, C13's Tier A listed Needham 1959 vol. 3; C13 is being rewritten and I do not rely on it.) | `grep -c Needham` = 1 in body; 0 in both shelf lines. | Add Needham (1959), *Science and Civilisation in China*, vol. 3, with `(to-verify)`, or drop the attribution. |

**Passes, stated explicitly:** 11/11 digest pins; 66/66 and 75/75 anchor tokens; 19/19 and 14/14 couples; `- topic:` byte-equal to the r44 seed (775 chars; sha256 with newline `9424fb81c22fe8c9a468d75aa291e1b5943a268b8699320915de52d7bda3459a`, matching C02's claim); 10/10 per-item marks on C02's shelf; no unread work asserted-read; no fabricated source detected; no existing corpus entry overwritten (the proposed slug is still absent at `a01405d`).

---

## 5. Required merge (for the integrator/drafter)

1. **One head, C02's** (8 ordered fields), because W01 designates it and C01's head is out of contract.
2. **Replace C02's 10-item external shelf with C01's 20-item set**, keeping C02's per-item `(to-verify)` style. Addendum — the ten works C01's shelf adds over C02's (five are body-cited: Mundy, al-Idrisi, Russell, *Tabula*, Mercator; the other five are shelf breadth and may be kept or cut with a recorded reason), plus Needham:

```text
Edson (2007), *The World Map, 1300–1492* (Johns Hopkins UP) `(to-verify)`;
Mundy (1996), *The Mapping of New Spain* (U. Chicago Press) `(to-verify)`;
Boone (2000), *Stories in Red and Black* (U. Texas Press) `(to-verify)`;
Pickles (2004), *A History of Spaces* (Routledge) `(to-verify)`;
Buisseret, ed. (1992), *Monarchs, Ministers, and Maps* (U. Chicago Press) `(to-verify)`;
Russell (1991), *Inventing the Flat Earth* `(to-verify)`;
al-Idrisi, *Nuzhat al-mushtāq* (1154) `(to-verify)`;
the *Tabula Peutingeriana* (13th-c. copy) `(to-verify)`;
Ortelius, *Theatrum Orbis Terrarum* (1570) `(to-verify)`;
Mercator (1569; *Atlas* 1595) `(to-verify)`;
Needham (1959), *Science and Civilisation in China*, vol. 3 `(to-verify)`.
```

3. **Slice C01's fence at the first `## 1.`** and land that as the body; do not land C01's head.
4. **Fix S4-S7** in the same edit.
5. If a shorter shelf is preferred, a drop must be recorded with a reason and the body must stop citing the dropped work; a silent drop is the r47 defect class in a new dress.

---

## 6. Acceptance gate (what the final assembled entry must pass)

1. **Unity:** exactly one H1, exactly one `- sources:` block, 8 head fields in order.
2. **Closure:** every **secondary work** named in the body appears on the shelf; primary works/exemplars may instead be covered by a column-level `(to-verify)` mark. This is a set check, not a prose judgement.
3. **Markers:** every external bullet carries `(to-verify)`; no blanket-only shelf if the draft lists individual works.
4. **Pins:** every pinned digest matches `sha256sum` at the apply-time HEAD; no pin is "updated from memory".
5. **No asserted-read:** every `consulted|fetched|inspected|read` hit is a negative/limit statement or an in-corpus re-read.
6. **Instrument:** checks 1-4 in §7 exit 0; check 5 lists only whitelisted lines.

---

## 7. Re-runnable instrument

`python3 -B shelf_audit.py <entry.md>`. Resolves `corpus/...`, `../...`, partition-relative and bare-basename anchors; verifies knowledge-file digests; counts external bullets/marks; compares a spelled digest count to the measured knowledge-pin count; lists body external-author lines without an inline marker. Aux digests (e.g. `corpus/README.md`) are verified but excluded from the shelf count.

```python
#!/usr/bin/env python3
"""Shelf-provenance audit for the cartography entry (head block or full entry).

Usage: python3 -B shelf_audit.py <entry.md> [--root .] [--entry-dir corpus/knowledge/culture-material]
Checks 1-4 are gating; 5 is a review list.
  1. every path:line anchor resolves and its line exists
  2. every sha256 pin matches the live file named on its line
  3. every external-shelf bullet carries an inline (to-verify)
  4. a spelled digest count equals the measured knowledge-file pin count
  5. body lines naming a shelf author without (to-verify)
"""
import re, sys, hashlib, pathlib

root = pathlib.Path('.'); entry_dir = pathlib.Path('corpus/knowledge/culture-material')
args = sys.argv[1:]
for opt in ('--root', '--entry-dir'):
    if opt in args:
        i = args.index(opt); val = args[i+1]; del args[i:i+2]
        if opt == '--root': root = pathlib.Path(val)
        else: entry_dir = pathlib.Path(val)
src = pathlib.Path(args[0])
lines = src.read_text(encoding='utf-8').splitlines()
fail, review, skipped = [], [], []

n_anchor = 0
for i, l in enumerate(lines, 1):
    cur = None
    for m in re.finditer(r'([A-Za-z0-9_][A-Za-z0-9_./-]*\.md)|:([0-9][0-9,\-–]*)', l):
        if m.group(1):
            cur = m.group(1)
            if cur.startswith('corpus/'):
                cands = [root / cur]
            elif cur.startswith('../'):
                cands = [entry_dir / cur]
            elif '/' in cur:
                cands = [root / 'corpus/knowledge' / cur]
            else:
                cands = [entry_dir / cur] + sorted((root / 'corpus/knowledge').glob(f'*/{cur}'))
            hit = next((c for c in cands if c.exists()), None)
            if hit is None:
                if cur.startswith('reports/') or cur.endswith('cartography-and-mapmaking.md'):
                    skipped.append((i, cur))
                else:
                    fail.append(f'path missing {cur} (line {i})')
            cur = hit if hit else cur
        elif m.group(2) is not None and cur is not None:
            n_anchor += 1
            if not isinstance(cur, pathlib.Path) or not cur.exists():
                continue
            nlines = len(cur.read_text(encoding='utf-8').splitlines())
            for part in m.group(2).replace('–', '-').split(','):
                if part and int(part.split('-')[-1]) > nlines:
                    fail.append(f'anchor out of range {cur}:{m.group(2)} (file has {nlines}; line {i})')
print(f'anchors checked: {n_anchor}')
for i, c in skipped: print(f'  not-a-shelf-anchor (expected absent/context): {c} line {i}')

digests = 0; digests_aux = 0
for i, l in enumerate(lines, 1):
    for m in re.finditer(r'sha256 `([0-9a-f]{64})`', l):
        pm = re.search(r'`([^`]+\.md)`', l)
        if pm and pm.group(1).startswith('corpus/knowledge/'): digests += 1
        else: digests_aux += 1
        if not pm:
            fail.append(f'digest without file path on its line (line {i})'); continue
        p = root / pm.group(1)
        if not p.exists():
            fail.append(f'digest target missing {pm.group(1)}'); continue
        live = hashlib.sha256(p.read_bytes()).hexdigest()
        if live != m.group(1):
            fail.append(f'digest mismatch {pm.group(1)}: pinned {m.group(1)[:12]} live {live[:12]}')
print(f'digest pins: {digests} knowledge + {digests_aux} aux')

ext, in_ext = [], False
for i, l in enumerate(lines, 1):
    s = l.strip()
    if 'External standard shelf' in s: in_ext = True; continue
    if in_ext and re.match(r'^- [a-z ]+:', s): break
    if in_ext and s.startswith('- ') and not s.startswith('- `corpus/'):
        ext.append((i, s))
unmarked = [x for x in ext if 'to-verify' not in x[1]]
print(f'external bullets: {len(ext)}; without (to-verify): {len(unmarked)}')
for i, s in unmarked: fail.append(f'external bullet without (to-verify) line {i}: {s[:80]}')

words = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11}
for i, l in enumerate(lines, 1):
    m = re.search(r'sha256 pinned for the (\w+) load-bearing', l)
    if m and m.group(1) in words and words[m.group(1)] != digests:
        fail.append(f'spelled digest count "{m.group(1)}" != measured {digests} (line {i})')

names = ['Harley','Wood','Monmonier','Jacob','Ptolemy','Campbell','Edson','Kain','Baigent',
         'Mundy','Boone','Pickles','Buisseret','Snyder','Dilke','Idrisi','Ortelius',
         'Mercator','Peutinger','Russell','Frisius','Snellius','Cassini','Torrens','Snow','Minard','Needham']
for i, l in enumerate(lines, 1):
    if any(n in l for n in names) and 'to-verify' not in l:
        review.append((i, l.strip()[:140]))
print(f'body external-name lines without inline marker (review): {len(review)}')
for i, s in review: print(f'  REVIEW {i}: {s}')

print('\nFAIL' if fail else '\nPASS (checks 1-4)')
for f in fail: print('  -', f)
sys.exit(1 if fail else 0)
```

Measured behaviour at the pinned digests:

```
$ python3 -B shelf_audit.py .scratch/c08/r48-head.md     # C02 head, 23 lines
anchors checked: 66
digest pins: 11 knowledge + 1 aux
external bullets: 0; without (to-verify): 0
body external-name lines without inline marker (review): 0
PASS (checks 1-4)

$ python3 -B shelf_audit.py .scratch/c08/r48-entry.md    # C01 entry, 228 lines
anchors checked: 75
digest pins: 0 knowledge + 0 aux
external bullets: 0; without (to-verify): 0
body external-name lines without inline marker (review): 8
PASS (checks 1-4)
```

Note: the "external bullets: 0" line is expected — each draft puts its external shelf on one physical bullet line, so the per-bullet count is 1/1, not 10/20. The per-item marker count is measured separately in §3 (`11` marks on C02's single shelf line, of which 10 are works and 1 is the header statement; `1` on C01's).

---

## 8. What I did not verify

- **External bibliographic truth.** No network; every edition/volume/page remains `(to-verify)`. I did not check a catalogue.
- **Body semantics outside the shelf.** I checked that cited works exist in the shelf and that quoted anchor text is present; I did not judge whether each citation supports its sentence (C04/C06 own that).
- **The final assembled entry.** It does not exist yet; the files I audited are live drafts. Re-run §7 on the assembly.
- **C13's candidate head.** It was being rewritten during the seat; I do not base any finding on it.

---

## 9. Commands and write-surface statement

All commands from the lane root, 2026-10-19, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l            # 223
$ ls corpus/knowledge/culture-material/*.md | wc -l     # 25
$ sha256sum corpus/knowledge/{myth-symbol/cosmology-cosmography,myth-symbol/sacred-topography-pilgrimage,
    myth-symbol/direction-symbolism,culture-material/architecture-settlement-lexicon,
    culture-material/writing-media-surface-economy,culture-material/transport-mobility-lexicon,
    culture-material/craft-artisan-lexicon,culture-material/trade-economy-lexicon,
    civilizations/mesoamerica-primary-sources,linguistics/naming-systems,
    verification/calibration-registry}.md                # 11/11 equal to C02's pins
$ sed -n '44p;54p;65p' corpus/knowledge/culture-material/craft-artisan-lexicon.md
| Steel (Japan) | **tamahagane** …            # :44 is grading, not the ladder
| System | Apprentice | Journeyman | Master | Entry rite / mechanism |   # :54
- Design rule: pick a rung system and then break it deliberately …      # :65
$ sed -n '86,90p' corpus/knowledge/verification/calibration-registry.md
                                                  # :87 content, :88 blank, :89 CAL-04
$ grep -n 'Every renaming is datable' corpus/knowledge/linguistics/naming-systems.md
70:… Every renaming is datable; a map is an archive of coups.
$ sha256sum reports/round-48/cov/C02-header.md reports/round-48/cov/C01-entry.md
2ff5b15d…  reports/round-48/cov/C02-header.md
4c2815a7…  reports/round-48/cov/C01-entry.md
$ python3 -B .scratch/c08/shelf_audit.py .scratch/c08/r48-head.md
anchors 66; pins 11+1; PASS
$ python3 -B .scratch/c08/shelf_audit.py .scratch/c08/r48-entry.md
anchors 75; pins 0; review 8; PASS
```

**Write surface:** this file only — `reports/round-48/cov/C08-shelf.md`. Disposable artifacts under `.scratch/c08/` (`head-block.md`, `r47-assembled.md`, `r48-head.md`, `r48-entry.md`, `shelf_audit.py`). No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed.
